"""A Level Geography (0750), Lower Sixth: Biogeography & Pedology; Tectonic, Slope, Coastal & Arid Geomorphology.

KKEVO draft lessons, written from the KKEVO master curriculum blueprint (L6M3, L6M4). A reviewer should check them
against the Board's syllabus and standard textbooks. Teaching figures marked "invented for practice" are not real data.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "lower-sixth")

M_BIO = "Biogeography & Pedology"
M_GEO = "Tectonic, Slope, Coastal & Arid Geomorphology"

LESSONS = []

# ---------------------------------------------------------------------------
# Biogeography & Pedology / Soil-forming factors and soil profiles
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_BIO, topic="Soil-forming factors and soil profiles",
    title="Jenny's soil-forming factors and reading a soil profile",
    slug="gpl2-soil-forming-factors-and-profiles",
    minutes=24,
    summary="Soil as a system shaped by climate, organisms, relief, parent material and time (Jenny's equation), how horizons form, and how to measure and describe a profile.",
    objectives=[
        "Explain how each of Jenny's five factors influences soil formation",
        "Describe and explain the O, A, E, B, C and R horizons of a soil profile",
        "Calculate texture percentages, organic content and moisture content from field data",
        "Evaluate the usefulness of the factorial model of soil formation",
    ],
    key_concepts=["Pedology", "Jenny's equation", "Active and passive factors", "Soil horizon", "Eluviation", "Illuviation", "Soil texture"],
    blocks=[
        H("Introduction"),
        T("Drive from Yaoundé towards Buea and the colour of the roadside soil changes. Around Yaoundé the cuttings are deep red. "
          "On the slopes of Mount Cameroon the soils are dark and rich, formed on volcanic rock. In many valley floors the soil is "
          "grey and wet. All three lie in a hot, wet country, so climate alone cannot explain the difference.\n\n"
          "At O Level you learned what soil is made of. At A Level you must explain **why** soils differ from place to place, "
          "using a model of the soil-forming factors and the evidence of the soil profile."),
        D("**Pedology** is the study of soils as natural bodies: how they form, how they are classified and how they are "
          "distributed. A **soil** is a natural body of mineral particles, organic matter, water and air, organised into "
          "layers (horizons) that form in place through the interaction of several factors over time.", title="Pedology and soil"),
        D("The American soil scientist Hans Jenny (1941) wrote soil as a function of five factors: climate, organisms, relief "
          "(topography), parent material and time. The dots stand for other local factors.",
          title="Jenny's factorial equation", formula=r"S = f(cl,\ o,\ r,\ p,\ t,\ \ldots)"),
        KEY("The five factors", "Each factor works through processes. Always say how the factor acts, not only that it matters.", cards=[
            ["Climate (cl)", "Rainfall minus evaporation sets the direction of water movement: downward leaching or upward capillary rise. Temperature sets the speed of chemical weathering and decomposition."],
            ["Organisms (o)", "Plants supply litter and humus; roots open the soil; earthworms, termites and ants mix it; micro-organisms decompose litter and release nutrients. People clear, plough and fertilise."],
            ["Relief (r)", "Slope angle controls drainage and erosion: thin, well-drained soils on steep slopes; thick, wet soils at the foot. Aspect and altitude change local climate."],
            ["Parent material (p)", "The rock or deposit the soil forms from sets the texture and the starting minerals: basalt gives clay-rich, base-rich soil; granite and sandstone give sandier, more acid soil."],
            ["Time (t)", "Young soils keep the character of the parent material and have weak horizons. Old soils have deep, well-developed horizons and may be strongly leached."],
        ]),
        T("Many textbooks call climate and organisms the **active** factors because they supply the energy and the agents of change, "
          "and relief, parent material and time the **passive** factors because they set the conditions. Some textbooks add people "
          "as a sixth, anthropogenic factor. Check which grouping your textbook uses."),
        TIP("The factors are not independent. Climate controls vegetation, so climate and organisms work together. Relief changes "
            "local climate and drainage. A strong answer shows these links instead of treating the five factors as a list."),
        H("The soil profile"),
        D("A **soil profile** is a vertical section from the surface down to the unweathered rock. A **horizon** is a layer "
          "roughly parallel to the surface that differs from the layers above and below in colour, texture, structure or chemistry. "
          "Horizons are formed in place by soil processes; they are not deposited one on top of another like sedimentary beds.",
          title="Profile and horizon"),
        IMG("algpl2-soil-profile.svg", alt="A soil column with horizons O, A, E, B, C and R from top to bottom, each labelled, and an arrow showing water moving down",
            caption="Figure 1. A generalised soil profile. Not every soil has every horizon."),
        D("**Eluviation** is the washing out of fine material (clay, humus, iron) from an upper horizon by water moving down. "
          "**Illuviation** is the deposition of that material lower down. The E horizon is the eluvial zone, the B horizon the "
          "illuvial zone. **Leaching** is the removal of soluble substances (bases such as calcium and potassium) in solution.",
          title="Eluviation, illuviation and leaching"),
        T("You describe a profile by its properties. **Texture** is the proportion of sand, silt and clay. **Structure** is the way "
          "particles clump into peds (crumb, blocky, platy). **Colour** gives clues: red and yellow mean iron oxides in well-drained "
          "soil; grey and blue-grey mean waterlogging; dark brown or black means humus. **pH** measures acidity, and **organic "
          "content** is found by burning a dry sample (loss on ignition)."),
        H("Worked examples"),
        EX("Worked example 1: texture from a sieve and settling test", intro="A 60 g dry sample from a farm near Bafia separates into 27 g sand, 21 g silt and 12 g clay. Find the percentages and name the texture class.", steps=[
            S("Percentage of sand", math=r"\frac{27}{60}\times 100 = 45\%"),
            S("Percentage of silt", math=r"\frac{21}{60}\times 100 = 35\%"),
            S("Percentage of clay", math=r"\frac{12}{60}\times 100 = 20\%"),
            S("Classify on a texture triangle", text="45 percent sand, 35 percent silt and 20 percent clay plots in the loam class: a balanced, fertile mixture."),
        ], check=r"45 + 35 + 20 = 100"),
        EX("Worked example 2: organic and moisture content", intro="A fresh sample weighs 120 g and 96 g after oven drying. A 50.0 g portion of the dry soil weighs 46.5 g after burning off the organic matter. Find the moisture content (as a percentage of dry mass) and the organic content.", steps=[
            S("Water lost", math=r"120 - 96 = 24\text{ g}"),
            S("Moisture content", math=r"\frac{24}{96}\times 100 = 25\%"),
            S("Organic matter burnt off", math=r"50.0 - 46.5 = 3.5\text{ g}"),
            S("Organic content (loss on ignition)", math=r"\frac{3.5}{50.0}\times 100 = 7.0\%"),
        ]),
        EX("Worked example 3: essay plan", intro="Assess the relative importance of climate and parent material in the formation of soils.", steps=[
            S("Introduction", text="Define soil and state Jenny's equation. Thesis: climate is usually dominant over large areas and long periods; parent material dominates locally and in young soils."),
            S("Climate dominant", text="Zonal soils follow climate belts: deep ferralitic soils in the hot, wet tropics on many different rocks. Leaching or capillary rise depends on rainfall minus evaporation."),
            S("Parent material dominant", text="Young volcanic soils on Mount Cameroon are dark and base-rich because of the basalt; soils on limestone stay alkaline even in wet climates; sandy soils on sandstone drain freely."),
            S("Links and other factors", text="Time decides which wins: the longer a soil forms, the more climate overrides the rock. Relief and organisms modify both."),
            S("Conclusion", text="Climate is the main control at continental scale; parent material matters most at local scale and early in soil development."),
        ]),
        H("Evaluating the factorial model"),
        T("Jenny's equation is useful because it gives a checklist for explaining any soil and for comparing two soils that differ "
          "in only one factor (for example a sequence of soils down a slope, or of soils of different ages). Its limits: the factors "
          "interact, so their separate effects are hard to measure; it names conditions but does not describe the processes "
          "(leaching, humification) that actually make horizons; time is hard to date; and it underplays people, who now change "
          "soils faster than any natural factor."),
        MISTAKE("Listing the factors without the process", "'Climate affects soil' earns little. Write 'high rainfall exceeds evaporation, so water moves down and leaches bases, making the soil acid'."),
        MISTAKE("Treating horizons as deposited layers", "Horizons develop in place from the top down through soil processes. Layers of river or volcanic deposits are parent material, not horizons."),
        MISTAKE("Calculating moisture as a share of the wet mass", "State which base you use. Many field guides express moisture as a percentage of the dry mass; show the formula so the examiner can follow."),
        QUIZ("In which horizon do clay, iron and humus washed down from above accumulate?",
             ["The A horizon", "The E horizon", "The B horizon", "The C horizon"], 2,
             "The B horizon is the illuvial horizon, where material eluviated from above is deposited.",
             hint="Think of the horizon below the washed-out (eluvial) one.",
             feedback=["The A horizon is topsoil, where humus mixes with minerals; it loses material rather than gaining it.",
                       "The E horizon is the eluvial zone that loses material.", "",
                       "The C horizon is weathered parent material below the solum."]),
        QUIZ("Which pair are usually described as the passive soil-forming factors?",
             ["Climate and organisms", "Relief and parent material", "Climate and time", "Organisms and relief"], 1,
             "Relief, parent material and time set the conditions; climate and organisms supply energy and agents.",
             feedback=["These are the active factors.", "", "Climate is an active factor.", "Organisms are an active factor."]),
        PQ("A 40.0 g dry soil sample weighs 37.2 g after ignition. Calculate its organic content and comment on what it suggests.",
           r"Loss = 40.0 - 37.2 = 2.8 g. Organic content = 2.8 / 40.0 x 100 = 7.0 percent. This is a moderate humus content, typical of a topsoil under vegetation; a cultivated, eroded soil would usually show less."),
        PQ("Explain how relief influences soil depth and drainage.",
           "Plan: (1) Steep slopes: rapid runoff and erosion remove soil as it forms, so soils are thin and stony, and water drains quickly. (2) Gentle crests: little erosion, free drainage, deep weathered soils. "
           "(3) Foot of slope and valley floor: material and water arrive from upslope, soils are thick and often waterlogged and gleyed. (4) Aspect and altitude change temperature and rainfall, changing weathering and vegetation. Link to the catena idea."),
        PQ("Describe and explain the main horizons of a soil profile. (Use a labelled diagram.)",
           "Model answer: draw Figure 1. O: litter and humus from vegetation. A: dark topsoil where humus mixes with minerals; earthworms and roots active. E: pale horizon where eluviation and leaching have removed clay, iron and humus. "
           "B: illuvial horizon where these collect, often redder or denser. C: weathered parent material. R: unweathered bedrock. Explain that water moving down drives the E to B transfer."),
        PQ("'The factorial model explains soils but not soil formation.' Discuss.",
           "Plan: For: Jenny's equation lists conditions; it does not show processes such as leaching, humification or cheluviation; factors interact, so it cannot isolate causes. "
           "Against: by comparing soils that differ in one factor (climosequence, toposequence, chronosequence), the model does reveal how each factor works; it guides fieldwork. Judgement: it is a strong framework for explanation, and must be combined with the study of pedogenic processes (next lesson)."),
        TIP("Biogeography has its own questions in the physical section of Paper 1 (multiple choice) and Paper 2 (essays). Soils of "
            "Cameroon are also tested in the Cameroon section of Paper 3, and a soil pit or vegetation survey can be a fieldwork topic. "
            "Learn the profile diagram so that you can draw it quickly.", title="Exam link"),
        SUM("Soil = f(climate, organisms, relief, parent material, time); climate and organisms are usually called active, the rest passive.",
            "Each factor works through processes: water balance, temperature, mixing, drainage, mineral supply and duration.",
            "Horizons O, A, E, B, C, R form in place; eluviation removes fine material from E and illuviation deposits it in B.",
            "Texture, organic content and moisture are percentages of a measured mass: show the formula and base.",
            "The factorial model is a useful checklist, but the factors interact and it does not describe processes."),
    ],
))

# ---------------------------------------------------------------------------
# Biogeography & Pedology / Pedogenic processes
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_BIO, topic="Pedogenic processes",
    title="Pedogenic processes: ferralitization, podzolization, calcification, gleization and salinization",
    slug="gpl2-pedogenic-processes",
    minutes=25,
    summary="How the water balance drives the main soil-forming processes, what profile each produces, and how farmers can manage the ferralitic soils of southern Cameroon.",
    objectives=[
        "Explain how the balance of precipitation and evapotranspiration controls the direction of water movement in soil",
        "Describe and explain ferralitization (laterization), podzolization, calcification, gleization and salinization",
        "Link each process to a climate, a profile and a soil type",
        "Suggest and justify measures to manage ferralitic soils for farming",
    ],
    key_concepts=["Pedogenic process", "Water balance", "Ferralitization (laterization)", "Podzolization", "Cheluviation", "Calcification", "Gleization", "Salinization"],
    blocks=[
        H("Introduction"),
        T("Road builders in southern Cameroon dig red gravel from pits beside the road. In places, that red material has hardened "
          "into a crust like brick, called laterite. Farmers on the same red soils find that yields fall quickly after the forest "
          "is cleared. Both facts come from one soil-forming process working for a very long time under a hot, wet climate.\n\n"
          "The last lesson listed the factors. This lesson explains the **processes** that turn those factors into horizons."),
        D("A **pedogenic process** is a set of physical, chemical and biological changes that adds, removes, transforms or moves "
          "material within a soil and so builds its horizons. The four basic kinds are additions (litter, dust), losses (leaching, "
          "erosion), transformations (weathering, humification) and translocations (movement within the profile).",
          title="Pedogenic process"),
        D("The direction of water movement depends on precipitation (P) and potential evapotranspiration (PET). If P is greater "
          "than PET, water moves down and leaches the soil. If PET is greater than P, water is drawn up by capillary action and "
          "salts are deposited near the surface.", title="The soil water balance", formula=r"\text{surplus} = P - PET"),
        H("Ferralitization (laterization)"),
        T("In the hot, wet tropics, high temperatures and abundant water make chemical weathering (hydrolysis) intense and deep. "
          "Silica and bases (calcium, magnesium, potassium) are leached away. Iron and aluminium oxides, which are much less soluble, "
          "stay behind and give the soil its red or yellow colour. The result is a deep, clay-rich but nutrient-poor **ferralitic "
          "soil** (latosol, oxisol). Humus does not build up because litter decomposes fast."),
        T("Where the water table rises and falls through the year, iron collects in a mottled zone. If this zone is exposed and dries, "
          "it can harden irreversibly into **laterite** (ironstone or hardpan). The southern plateau of Cameroon is dominated by "
          "ferralitic soils; check your textbook for the local names and their exact distribution."),
        IMG("algpl2-two-profiles.svg", alt="Two soil columns side by side: a ferralitic soil with a thin humus layer, a thick red B horizon, a mottled zone and deep rotted rock; and a podzol with thick acid litter, a bleached E horizon, a dark humus band and an iron-rich Bs horizon",
            caption="Figure 1. A ferralitic soil and a podzol compared (schematic, not to scale)."),
        H("Podzolization"),
        T("In cool, wet climates under coniferous forest or heath, needles decay slowly into an acid mor humus. Organic acids made by "
          "the litter attach to iron and aluminium and carry them down in solution: this is **cheluviation** (movement by chelation). "
          "The E horizon is left bleached and ash-grey, and humus and iron are deposited in a dark Bh and an orange Bs horizon, "
          "sometimes as a thin iron pan that blocks drainage. Podzols also form on very sandy, acid parent material in the tropics."),
        H("Calcification, salinization and gleization"),
        KEY("Three more processes", "Each matches a different water regime.", cards=[
            ["Calcification", "Semi-arid grasslands: P is close to or a little below PET. Leaching is weak, so calcium carbonate is moved only part way down and builds a calcium-rich layer. Grass roots add deep, dark humus. Example: chernozems of the temperate steppes."],
            ["Salinization", "Hot, dry areas where PET is much greater than P, or where irrigation raises the water table. Water rises by capillary action and evaporates, leaving salts at or near the surface. Crops fail on a white salt crust."],
            ["Gleization", "Waterlogged soils in valley floors, swamps or above an impermeable layer. Without oxygen, iron is reduced from the red ferric form to the grey-blue ferrous form. Gleys are grey with orange mottles where air enters along roots."],
        ]),
        TIP("Use the water balance to sort the processes quickly: large surplus = ferralitization or podzolization (leaching); "
            "small deficit = calcification; large deficit or bad irrigation = salinization; permanent saturation = gleization."),
        H("Worked examples"),
        EX("Worked example 1: water balance and process", intro="Station X has P = 1 600 mm and PET = 1 100 mm a year. Station Y has P = 450 mm and PET = 1 900 mm (figures invented for practice). Which way does soil water move at each, and which processes are likely?", steps=[
            S("Station X", math=r"P - PET = 1600 - 1100 = +500\text{ mm}"),
            S("Interpret X", text="A surplus: water drains downward. If hot, intense hydrolysis and leaching give ferralitization; if cool with acid litter, podzolization."),
            S("Station Y", math=r"P - PET = 450 - 1900 = -1450\text{ mm}"),
            S("Interpret Y", text="A large deficit: water is drawn upward by capillary action and evaporates, so salts and carbonates collect near the surface. Salinization is likely, especially if land is irrigated without drainage."),
        ]),
        EX("Worked example 2: essay plan on ferralitic soils", intro="Identify the problems of ferralitic soils for farmers and suggest measures to overcome them.", steps=[
            S("Introduction", text="Define ferralitic soil and explain briefly how ferralitization makes it: deep weathering, leaching of silica and bases, residual iron and aluminium."),
            S("Problem 1: low fertility", text="Bases leached, low nutrient-holding capacity of the clays; most nutrients are in the vegetation, not the soil. Measure: return crop residues, compost and manure; use fertiliser in small, frequent doses; agroforestry with nitrogen-fixing trees."),
            S("Problem 2: acidity and aluminium", text="Acid soils release aluminium that harms roots. Measure: liming; choose tolerant crops such as cassava."),
            S("Problem 3: erosion and hardening", text="Once cleared, heavy rain removes the thin humus; exposed mottled layers may harden into laterite. Measure: keep ground covered (mulch, cover crops), contour ridges, avoid clearing steep slopes, keep fallow periods."),
            S("Conclusion", text="The soils can be farmed sustainably if the surface organic layer is protected and nutrients are recycled, which is what traditional bush fallowing achieved."),
        ]),
        EX("Worked example 3: identify the process", intro="A profile has a grey horizon with orange streaks along old root channels, on a valley floor near a stream. Name and explain the process.", steps=[
            S("Clue 1: grey colour", text="Grey or blue-grey means iron in its reduced (ferrous) form, which happens without oxygen."),
            S("Clue 2: orange mottles along roots", text="Air enters along root channels, so iron is oxidised there to orange ferric compounds."),
            S("Clue 3: valley floor", text="A high water table keeps the soil saturated."),
            S("Answer", text="Gleization, producing a gley soil."),
        ]),
        MISTAKE("Mixing up ferralitization and podzolization", "Both involve leaching, but in ferralitization silica is removed and iron and aluminium stay; in podzolization iron and aluminium are removed from the E horizon by organic acids. Check which element moves."),
        MISTAKE("Answering a soil-management question with general farm problems", "When a question asks how farmers can overcome the problems of a soil, keep to the soil (fertility, acidity, erosion, structure). Lack of capital or markets is not a soil problem."),
        QUIZ("Which process removes iron and aluminium from the upper horizon by means of organic acids?",
             ["Ferralitization", "Podzolization", "Calcification", "Salinization"], 1,
             "Podzolization works by cheluviation: organic acids from acid litter carry iron and aluminium down.",
             hint="Think of the bleached horizon under coniferous forest.",
             feedback=["In ferralitization iron and aluminium stay behind; silica is removed.", "",
                       "Calcification concerns calcium carbonate, not iron and aluminium.",
                       "Salinization brings salts up to the surface."]),
        QUIZ("An irrigation scheme in a hot, dry region floods fields without drains. Which soil problem is most likely after some years?",
             ["Podzolization", "Gleization only", "Salinization", "Laterite formation"], 2,
             "Irrigation raises the water table; capillary rise and strong evaporation leave salts at the surface.",
             feedback=["Podzols need cool, wet conditions and acid litter.", "Waterlogging may occur, but the characteristic problem in a hot, dry region is salt build-up.", "",
                       "Laterite needs long, intense leaching in a wet tropical climate."]),
        PQ("Explain why ferralitic soils are deep but infertile.",
           "Deep: high temperature and abundant water make hydrolysis fast, and the process has gone on for a very long time on old, stable surfaces, so rock is rotted to great depth. "
           "Infertile: the same water leaches silica and bases out of the profile; the remaining kaolinite clay and iron and aluminium oxides hold few nutrients; litter decomposes so fast that little humus builds up."),
        PQ("Compare the processes and profiles of a podzol and a chernozem.",
           "Podzol: cool, wet, P greater than PET; acid mor litter; cheluviation of iron and aluminium; bleached E; Bh and Bs horizons; acid, infertile. "
           "Chernozem: semi-arid grassland, P close to PET; weak leaching; calcium carbonate collects in the lower profile (calcification); deep, dark humus from grass roots; neutral to alkaline, very fertile. Key contrast: direction and strength of water movement."),
        PQ("Station Z has P = 900 mm and PET = 1 200 mm (invented for practice). Calculate the water balance and suggest the dominant process.",
           "P - PET = 900 - 1 200 = -300 mm, a moderate deficit. Leaching is weak and incomplete, so calcium carbonate is moved only part way down: calcification is likely, under grassland. A larger deficit or irrigation without drainage would risk salinization."),
        TIP("Paper 2 essays can ask how a soil forms and how it can be managed. The Cameroon section of Paper 3 has asked about the "
            "characteristics of the zonal soils of the South Cameroon Low Plateau, which are ferralitic. Learn their profile and properties.",
            title="Exam link"),
        SUM("The water balance (P minus PET) sets the direction of water movement and so the dominant process.",
            "Ferralitization: deep hydrolysis, silica and bases leached, iron and aluminium oxides remain; may harden to laterite.",
            "Podzolization: acid litter, cheluviation of iron and aluminium, bleached E over dark Bh and orange Bs.",
            "Calcification (semi-arid), salinization (strong evaporation or bad irrigation) and gleization (waterlogging) complete the set.",
            "Manage ferralitic soils by protecting the organic surface, recycling nutrients, liming and controlling erosion."),
    ],
))

# ---------------------------------------------------------------------------
# Biogeography & Pedology / Soil catenas
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_BIO, topic="Soil catenas",
    title="Soil catenas: how soils change from hilltop to valley floor",
    slug="gpl2-soil-catenas",
    minutes=22,
    summary="Why soils change in a regular sequence down a slope, the processes that move water, soil and solutes downslope, and how catenas guide land use in humid tropical Cameroon.",
    objectives=[
        "Define a catena and name the slope units from crest to valley floor",
        "Explain the soil found on each unit using drainage, throughflow, creep and wash",
        "Calculate a slope gradient as a ratio, a percentage and an angle",
        "Evaluate the catena as a model and apply it to land use",
    ],
    key_concepts=["Catena", "Toposequence", "Throughflow", "Colluvium", "Lateral eluviation", "Hydromorphic soil", "Slope gradient"],
    blocks=[
        H("Introduction"),
        T("Walk down a hill near Yaoundé or in the Western Highlands. On the rounded hilltop the soil is red and drains well. Lower down "
          "it becomes yellower and wetter. In the valley bottom, where raffia palms often grow, the soil is grey, sticky and "
          "waterlogged. The climate and the rock may be the same along the whole walk. What changes is the **position on the slope**.\n\n"
          "This lesson develops the relief factor of Jenny's equation into a model you can draw and use."),
        D("A **catena** is a sequence of linked soils that changes in a regular way down a slope, usually from the same parent "
          "material and under the same climate, because of differences in drainage and in the movement of material downslope. "
          "The term was introduced by the soil scientist Geoffrey Milne, working in East Africa in the 1930s.", title="Catena"),
        D("A **toposequence** is a set of soils that differ mainly because of relief. A catena is a toposequence in which the soils are "
          "also linked by the transfer of water, solutes and particles from upslope to downslope.", title="Toposequence"),
        IMG("algpl2-catena.svg", alt="Cross-section of a slope from a flat crest down a steeper mid-slope to a valley floor with a stream; the soil layer is thin at the top and middle and thick and grey at the bottom where the water table is close to the surface",
            caption="Figure 1. A typical humid tropical catena (schematic)."),
        H("The slope units and their soils"),
        KEY("From crest to valley floor", "Read the catena as a set of slope units, each with its own processes and soil.", cards=[
            ["1 Crest (interfluve)", "Flat or gently convex. Water drains downward and away; little erosion. Deep, well-drained, red (oxidised iron) soils, often strongly leached."],
            ["2 Upper and mid slope", "Steeper and convex to straight. Soil creep, rainsplash and wash move material away as fast as it forms; water moves sideways as throughflow. Thin, stony, well-drained soils."],
            ["3 Lower slope (footslope)", "Concave. Material from above is deposited as colluvium; throughflow brings solutes. Thicker, browner or yellower soils, less well drained."],
            ["4 Valley floor", "Water table at or near the surface for much of the year. Fine particles and solutes collect. Deep, grey, gleyed hydromorphic soils, sometimes with organic peat, and alluvium near the stream."],
        ]),
        D("**Throughflow** is water moving sideways downslope within the soil. It carries dissolved bases and fine clay from upslope, "
          "a process called **lateral eluviation**. **Colluvium** is soil and rock debris moved downslope by creep and wash and "
          "deposited at the foot of the slope. A **hydromorphic** soil is one whose properties are dominated by waterlogging.",
          title="Throughflow, colluvium and hydromorphic soils"),
        T("Two kinds of catena are often distinguished. In the first, the whole slope is on one parent material and the differences come "
          "from drainage and downslope transfer. In the second, the slope crosses different rocks, so parent material also changes. "
          "Milne described both; most exam answers use the first."),
        H("Worked examples"),
        EX("Worked example 1: slope gradient", intro="On a map, a hillside falls 30 m in height over a horizontal distance of 600 m. Express its gradient as a ratio, a percentage and an angle.", steps=[
            S("Ratio (vertical interval to horizontal equivalent)", math=r"\frac{30}{600} = \frac{1}{20}\ \Rightarrow\ 1\text{ in }20"),
            S("Percentage", math=r"\frac{30}{600}\times 100 = 5\%"),
            S("Angle", math=r"\theta = \tan^{-1}(0.05) \approx 2.9^{\circ}"),
            S("Meaning for soils", text="A gentle slope: drainage is free but slow erosion keeps soils of moderate depth; steeper units would have thinner soils."),
        ]),
        EX("Worked example 2: explaining the valley-floor soil", intro="Explain why the valley-floor soil of a humid tropical catena is grey and fine textured.", steps=[
            S("Water", text="Throughflow and overland flow from the whole slope converge on the valley floor, and the water table is high."),
            S("Chemistry", text="Saturation removes oxygen, so iron is reduced to grey ferrous forms (gleization)."),
            S("Texture", text="Fine clay and silt carried by wash and lateral eluviation settle in the low-energy valley floor."),
            S("Conclusion", text="The soil is hydromorphic: grey, fine, often rich in organic matter and in bases leached from upslope."),
        ]),
        EX("Worked example 3: essay plan", intro="With reference to a named area, explain how soils vary along a slope and how this influences land use.", steps=[
            S("Introduction", text="Define catena; name the area (for example a hillside in the humid south or the Western Highlands of Cameroon) and state that climate and rock are constant along it."),
            S("Crest and upper slope", text="Red, deep or thin well-drained soils; used for tree crops and food crops, but fertility is low and erosion risk rises with slope."),
            S("Lower slope", text="Thicker colluvial soils with more nutrients and moisture; often the most intensively farmed (maize, cocoyams, vegetables)."),
            S("Valley floor", text="Gleyed, waterlogged soils; used for raffia palms, rice or dry-season vegetables if drained; risk of flooding."),
            S("Evaluation", text="Land use also depends on access, tenure and markets, so the catena explains part, not all, of the pattern."),
        ]),
        H("Evaluating the catena model"),
        T("Strengths: it explains a soil pattern you can see in the field in a single afternoon; it links soil to hydrology and slope "
          "processes; it helps to choose land use and to plan soil surveys. Limits: real slopes are irregular and may cross several "
          "rocks; old landscapes may carry soils formed under past climates; and farming, terracing and drainage can change the "
          "natural sequence."),
        MISTAKE("Describing only colour", "Explain each soil by its process: drainage, throughflow, creep, wash, deposition, gleization. Colour is evidence, not the explanation."),
        MISTAKE("Saying the valley-floor soil is the least fertile", "Valley-floor soils often receive bases and fine material from upslope. Their problem is waterlogging, not a lack of nutrients."),
        QUIZ("Which process mainly carries dissolved bases sideways from the upper slope to the lower slope?",
             ["Capillary rise", "Throughflow", "Rockfall", "Infiltration on the crest only"], 1,
             "Throughflow moves water and solutes laterally downslope within the soil.",
             feedback=["Capillary rise is upward movement, not downslope.", "", "Rockfall moves rock fragments, not dissolved bases.", "Infiltration is entry into the soil; it does not move material along the slope."]),
        QUIZ("On which unit of a humid tropical catena would you expect the deepest gleyed soil?",
             ["The crest", "The convex upper slope", "The straight mid-slope", "The valley floor"], 3,
             "The valley floor has a high water table and receives water and fine material from upslope.",
             feedback=["The crest drains freely and is well oxidised.", "The upper slope loses material by creep and wash.", "The mid-slope drains freely and loses material.", ""]),
        PQ("A slope falls 45 m over a horizontal distance of 300 m. Calculate the gradient as a percentage and as an angle (to 1 decimal place).",
           r"Gradient = 45 / 300 = 0.15, so 15 percent. Angle = inverse tan of 0.15, about 8.5 degrees. This is steeper than the 5 percent slope in the worked example, so expect thinner soils and more wash."),
        PQ("Draw and label a soil catena and explain the soil on each slope unit.",
           "Use Figure 1. Crest: deep, red, well drained, leached. Upper and mid slope: thin, stony; creep and wash remove material; throughflow carries solutes away. "
           "Lower slope: colluvium accumulates, soils thicker and wetter. Valley floor: gleyed, grey, fine-textured; high water table. Label throughflow arrows and the water table."),
        PQ("To what extent does the catena concept explain variations in land use on a hillside?",
           "Plan: Explains: soil depth, drainage and fertility change with slope position, so crops are matched to units (tree crops on crests, food crops on footslopes, raffia or rice in valleys). "
           "Limits: land tenure, distance to the road and markets, population pressure and terracing also shape land use. Judgement: a strong physical framework that must be combined with human factors."),
        TIP("A catena makes a good fieldwork study (soil pits at intervals down a slope) and suits essay questions in the physical "
            "section of Paper 2. Draw the cross-section with labelled units and arrows; examiners reward the diagram.", title="Exam link"),
        SUM("A catena is a linked sequence of soils down a slope on the same rock and climate.",
            "Crest: deep, red, well drained. Upper slope: thin, stony. Lower slope: colluvium, thicker. Valley floor: gleyed, grey, waterlogged.",
            "Throughflow, lateral eluviation, creep and wash move water, solutes and particles downslope.",
            "Gradient = vertical interval / horizontal equivalent; give it as a ratio, a percentage or an angle.",
            "The model explains much of the soil pattern but must be combined with human factors for land use."),
    ],
))

# ---------------------------------------------------------------------------
# Biogeography & Pedology / Tropical rainforest and savanna ecosystems
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_BIO, topic="Tropical rainforest and savanna ecosystems",
    title="Tropical rainforest and savanna ecosystems compared",
    slug="gpl2-rainforest-and-savanna-ecosystems",
    minutes=25,
    summary="Climate, structure, productivity and plant adaptations of the tropical rainforest and the savanna, the debate on the origin of savanna, and strategies to conserve the selva.",
    objectives=[
        "Compare the climate, structure and productivity of tropical rainforest and savanna",
        "Explain plant adaptations to light competition, heavy rain, drought and fire",
        "Evaluate climatic, edaphic and human (fire) explanations of the savanna",
        "Assess strategies to conserve rainforest vegetation and wildlife",
    ],
    key_concepts=["Ecosystem", "Biome", "Net primary productivity", "Stratification", "Xerophyte", "Pyrophyte", "Climatic climax", "Plagioclimax"],
    blocks=[
        H("Introduction"),
        T("Cameroon is often described as 'Africa in miniature' because it holds both great biomes of tropical Africa. The south and "
          "east are covered by dense evergreen rainforest, with protected areas such as the Dja Faunal Reserve and Korup National "
          "Park. Moving north, the forest gives way to wooded grassland on the Adamawa Plateau and to drier savanna and Sahelian "
          "vegetation in the Far North.\n\n"
          "At O Level you described these vegetation types. At A Level you explain how each ecosystem works and argue about why the "
          "savanna exists at all."),
        D("An **ecosystem** is a community of living organisms interacting with each other and with the non-living environment, "
          "linked by flows of energy and cycles of nutrients. A **biome** is a large-scale ecosystem defined by its climax vegetation, "
          "such as tropical rainforest (selva) or savanna.", title="Ecosystem and biome"),
        D("**Net primary productivity (NPP)** is the rate at which plants store energy as new biomass after their own respiration, "
          "often given in grams of dry matter per square metre per year. It measures how much food an ecosystem can support.",
          title="Net primary productivity"),
        H("The tropical rainforest"),
        T("Climate: hot all year (about 25 to 28 degrees Celsius), small annual range, heavy rainfall (often 1 500 to over 2 000 mm) "
          "with no long dry season. These conditions allow growth all year, so NPP and biomass are the highest of any land biome, and "
          "species diversity is very high."),
        T("Structure: the forest is **stratified**. Emergent trees rise above a dense, continuous canopy; below are an understorey of "
          "young trees, a shrub layer and a dark forest floor where only a few per cent of the light arrives. Adaptations include "
          "**buttress roots** that support tall trees on shallow soils, **drip-tip leaves** that shed heavy rain, thin smooth bark, "
          "**lianas** that climb to the light and **epiphytes** that grow on branches to reach it."),
        H("The savanna"),
        T("Climate: hot, with a marked wet season and a dry season of several months; rainfall is lower and less reliable than in the "
          "rainforest. Vegetation is grassland with scattered trees and shrubs, the proportion of trees falling towards drier areas. "
          "Biomass and NPP are lower, and fire is a regular part of the dry season."),
        T("Adaptations: many trees are **xerophytes** (adapted to drought), with deep tap roots, small or waxy leaves, and leaves shed "
          "in the dry season. Many are **pyrophytes** (fire-adapted), with thick, corky bark and buds protected below ground; the baobab "
          "stores water in its trunk. Grasses die back above ground and regrow from roots and seeds when the rains return."),
        CODE("""
Feature                 Tropical rainforest            Savanna
Rainfall regime         heavy, all year                wet season and dry season
Structure               4-5 layers, closed canopy      grass with scattered trees
Biomass                 very large                     moderate
NPP (often quoted)      about 2 200 g/m2/yr            about 900 g/m2/yr
Main nutrient store     biomass                        soil
Key stresses            light competition, heavy rain  drought, fire, grazing
Typical adaptations     buttresses, drip tips, lianas  deep roots, thick bark, deciduous
""", "text", title="Table 1. Rainforest and savanna compared (NPP values are approximate figures often quoted; check your textbook)"),
        H("Why is there savanna? A debate"),
        KEY("Three explanations", "Most geographers now combine them.", cards=[
            ["Climatic", "The long dry season and low, variable rainfall do not support closed forest, so savanna is the climatic climax of the wet-and-dry tropics."],
            ["Edaphic (soil)", "Poor, shallow or seasonally waterlogged soils, or hard laterite crusts, stop tree growth even where rainfall could support forest."],
            ["Biotic and human", "Repeated burning, grazing and clearing by people hold back trees. Where fire is kept out, woodland often returns, so much savanna may be a plagioclimax."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: comparing productivity", intro="Using the approximate values in Table 1, how many times more productive is the rainforest than the savanna, and why?", steps=[
            S("Ratio", math=r"\frac{2200}{900} \approx 2.4"),
            S("Explain: growing season", text="Rainforest plants grow all year; savanna growth stops in the dry season."),
            S("Explain: structure", text="Several layers of leaves capture almost all the light in the rainforest; savanna has a single grass layer and scattered trees."),
            S("Conclusion", text="About two and a half times more productive, because both water and the length of the growing season limit the savanna."),
        ]),
        EX("Worked example 2: essay plan", intro="'The savanna is a climatic climax.' Discuss.", steps=[
            S("Introduction", text="Define climax and savanna; outline the three explanations."),
            S("For", text="Savanna matches the wet-and-dry climate belt across Africa; drought-adapted plants; tree cover falls with rainfall."),
            S("Against: soils", text="Savanna also occurs in wetter areas on laterite crusts and waterlogged soils; patches of forest grow along rivers (gallery forest) in the same climate."),
            S("Against: fire and people", text="Burning experiments show trees return when fire is excluded; long human use explains derived savanna at forest edges, for example parts of the forest-savanna boundary in central Cameroon (check your textbook)."),
            S("Conclusion", text="Climate sets the potential, but soils and especially fire decide the actual vegetation; much savanna is a fire-maintained plagioclimax."),
        ]),
        EX("Worked example 3: conserving the selva", intro="Explain three strategies to conserve vegetation and wildlife in the tropical rainforest.", steps=[
            S("Strategy 1: protected areas", text="National parks and reserves (for example Korup, Dja) protect whole ecosystems; they work only with patrols, local support and benefits for nearby people."),
            S("Strategy 2: sustainable forest management", text="Selective logging with long rotation cycles, replanting and certification keeps the canopy and seed trees."),
            S("Strategy 3: agroforestry and alternative incomes", text="Growing cocoa or food crops under shade trees, and income from ecotourism or non-timber products, reduce the need to clear forest."),
            S("Link to the system", text="Each strategy keeps the biomass, which holds most of the nutrients in this ecosystem (see the nutrient cycling lesson)."),
        ]),
        MISTAKE("Describing vegetation without explaining it", "Link each feature to a cause: drip tips because of heavy rain, buttresses because of shallow soils and great height, thick bark because of fire."),
        MISTAKE("Answering a conservation question with soil conservation measures", "When a question asks about preserving vegetation and fauna, give strategies for the forest and its wildlife, not contour ploughing or terracing."),
        QUIZ("Which adaptation helps savanna trees survive regular dry-season fires?",
             ["Drip-tip leaves", "Thick, corky bark", "Buttress roots", "Epiphytic growth"], 1,
             "Thick bark insulates the living tissue from the heat of grass fires.",
             feedback=["Drip tips shed water in heavy rain; they do not protect against fire.", "", "Buttresses support tall rainforest trees.", "Epiphytes are a rainforest adaptation to reach light."]),
        QUIZ("Woodland grows back on a savanna plot that has been protected from fire for twenty years. What does this suggest?",
             ["The savanna there is a climatic climax", "The savanna there is a fire-maintained plagioclimax", "The soil has turned into laterite", "Rainfall has fallen sharply"], 1,
             "If trees return when fire is removed, fire (often set by people) was holding the vegetation back: a plagioclimax.",
             feedback=["A climatic climax would not change when fire is removed.", "", "Laterite would make tree growth harder, not easier.", "Falling rainfall would reduce tree cover."]),
        PQ("Explain how rainforest trees are adapted to competition for light.",
           "Tall straight trunks with branches only at the top to reach the canopy; emergents rising above it; lianas rooted in the ground that climb towards the light; epiphytes growing on branches high up; large leaves in the dark understorey to capture the little light there. Each is a response to the dense, multi-layer canopy."),
        PQ("Compare the structure and productivity of the rainforest and the savanna.",
           "Rainforest: four or five layers, closed canopy, very large biomass, NPP about 2 200 g per square metre per year (often quoted). Savanna: grass layer with scattered trees, moderate biomass, NPP about 900. Explain: all-year growth and full light capture in the forest versus seasonal drought and fire in the savanna."),
        PQ("Assess the role of people in creating and maintaining the savanna.",
           "Plan: People: burning for hunting, grazing and clearing; derived savanna at forest margins; woodland returns under fire protection. Other causes: seasonal drought (climatic), poor or waterlogged soils and laterite (edaphic). Judgement: people strongly shape savanna, but climate decides where fire can spread, so causes are combined."),
        TIP("Biogeography appears in the physical sections of Paper 1 and Paper 2. In Paper 2 questions on the selva have asked about "
            "managing and conserving the ecosystem, not only describing it. The vegetation of Cameroon is also tested in Paper 3, and a "
            "vegetation survey (quadrats, transects) is a common fieldwork topic.", title="Exam link"),
        SUM("Rainforest: hot and wet all year, stratified, very high biomass, NPP and diversity.",
            "Savanna: wet and dry seasons, grass with scattered trees, lower NPP, regular fire.",
            "Adaptations answer stresses: light and heavy rain in the forest; drought and fire in the savanna.",
            "Savanna is explained by climate, soils and fire together; much of it is a plagioclimax.",
            "Conservation of the selva must keep the biomass: protected areas, sustainable logging, agroforestry."),
    ],
))

# ---------------------------------------------------------------------------
# Biogeography & Pedology / Nutrient cycling
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_BIO, topic="Nutrient cycling",
    title="Nutrient cycling: Gersmehl's model and managing ecosystems",
    slug="gpl2-nutrient-cycling-gersmehl",
    minutes=25,
    summary="Gersmehl's three-store model of nutrient cycling, how stores and flows differ between rainforest and savanna, residence times, and how the model guides ecosystem management.",
    objectives=[
        "Draw and explain Gersmehl's model with its stores, inputs, outputs and transfers",
        "Compare the nutrient cycles of the tropical rainforest and the savanna",
        "Calculate store percentages and residence times from data",
        "Use the model to explain the effects of clearance and to propose management",
    ],
    key_concepts=["Nutrient cycle", "Gersmehl's model", "Biomass store", "Litter store", "Soil store", "Residence time", "Ecosystem management"],
    blocks=[
        H("Introduction"),
        T("A tall rainforest grows on poor ferralitic soil. How is that possible? The answer is that the forest keeps its nutrients "
          "moving quickly in a tight cycle between the trees, the litter on the ground and the thin topsoil. Break that cycle by "
          "clearing the trees and most of the nutrients leave with them.\n\n"
          "This lesson gives you a model to show this on one diagram, and to use it to argue how an ecosystem should be managed."),
        D("A **nutrient cycle** is the movement of mineral nutrients (such as nitrogen, phosphorus, potassium, calcium) between the "
          "living and non-living parts of an ecosystem. Unlike energy, which flows through once, nutrients are used again and again.",
          title="Nutrient cycle"),
        D("The geographer P. F. Gersmehl (1976) modelled the nutrient cycle as three **stores**: biomass (B, living plants and "
          "animals), litter (L, dead organic matter on the surface) and soil (S). Circles are drawn in proportion to the size of each "
          "store and arrows in proportion to the size of each flow.", title="Gersmehl's model"),
        KEY("Flows in the model", "Learn the names exactly; examiners expect them.", cards=[
            ["Inputs", "Nutrients dissolved in rainfall (and dust) enter the biomass and soil; weathering of rock releases nutrients into the soil."],
            ["Transfers", "Litterfall: biomass to litter. Decomposition: litter to soil. Uptake: soil to biomass through roots."],
            ["Outputs", "Runoff carries nutrients from the litter and soil surface; leaching removes them from the soil in drainage water."],
        ]),
        IMG("algpl2-gersmehl.svg", alt="Two Gersmehl diagrams. Rainforest: a very large biomass circle, a small litter circle and a small soil circle joined by thick arrows. Savanna: a small biomass circle, a small litter circle and a very large soil circle joined by thinner arrows",
            caption="Figure 1. Gersmehl's model for the tropical rainforest and the savanna (schematic sizes)."),
        H("Rainforest and savanna compared"),
        T("**Rainforest.** The biomass is by far the largest store. Litter is a small store because heat and moisture let decomposers "
          "break it down in months. The soil store is small because the leached ferralitic soil holds few nutrients and roots take them "
          "up almost as fast as they are released. All transfers are large and fast. Leaching is high because of heavy rain."),
        T("**Savanna.** The soil is the largest store: grasses put much of their growth into roots, which die and add organic matter "
          "to the soil, and leaching is weaker. The biomass store is smaller and much of it is burnt or grazed each dry season. Litter is "
          "small because fire removes it. Flows are smaller and slower and pulse with the wet season."),
        D("The **residence time** of a nutrient in a store is the average time it stays there: the size of the store divided by the "
          "rate at which material flows in (or out) each year.", title="Residence time", formula=r"\text{residence time} = \frac{\text{store}}{\text{annual flow}}"),
        H("Worked examples"),
        EX("Worked example 1: where are the nutrients?", intro="An area of rainforest holds 500 units of a nutrient in biomass, 10 in litter and 90 in soil (invented for practice). Find the percentage in each store, and the percentage left if all biomass is cleared and removed.", steps=[
            S("Total", math=r"500 + 10 + 90 = 600"),
            S("Biomass share", math=r"\frac{500}{600}\times 100 \approx 83.3\%"),
            S("Litter and soil shares", math=r"\frac{10}{600}\times 100 \approx 1.7\%,\quad \frac{90}{600}\times 100 = 15\%"),
            S("Left after clearance", math=r"\frac{10 + 90}{600}\times 100 \approx 16.7\%"),
            S("Meaning", text="Removing the trees removes more than four fifths of the nutrients. The biomass, not the soil, is the fragile store."),
        ]),
        EX("Worked example 2: residence time of litter", intro="Rainforest litter store = 10 units, litterfall = 20 units a year. A coniferous forest has a litter store of 300 units and litterfall of 10 units a year (invented for practice). Compare residence times.", steps=[
            S("Rainforest", math=r"\frac{10}{20} = 0.5\text{ year}"),
            S("Coniferous forest", math=r"\frac{300}{10} = 30\text{ years}"),
            S("Explain", text="Heat and moisture let decomposers work fast in the tropics; cold and acid needles slow decomposition in the taiga, so litter piles up."),
        ]),
        EX("Worked example 3: essay plan on ecosystem management", intro="Show how knowledge of the nutrient cycle can help in the better management of the selva ecosystem.", steps=[
            S("Introduction", text="Draw the rainforest Gersmehl model and state that the biomass is the main and most fragile store."),
            S("Effect of clearance", text="Removing biomass removes most nutrients; with no canopy, rain hits bare soil, increasing runoff and leaching outputs; the small soil store is exhausted in a few years."),
            S("Management 1: keep the biomass", text="Selective logging, protected areas and leaving trees standing keep the store and the litterfall transfer."),
            S("Management 2: keep the cycle short", text="Agroforestry and shade crops keep litter falling; mulch and residues feed the litter store; cover crops reduce runoff and leaching."),
            S("Management 3: allow recovery", text="Long bush fallows let the biomass store rebuild before the next clearing; shortening fallows breaks the cycle."),
            S("Conclusion", text="Management must protect the biomass and the litter-to-soil transfer, because the soil cannot store the nutrients by itself."),
        ]),
        MISTAKE("Calling the soil the main store in the rainforest", "In the rainforest the soil is a small store; most nutrients are held in the biomass. That is why clearance is so damaging."),
        MISTAKE("Describing the cycle when the question asks for management", "If the question asks how the model helps management, use the model briefly, then spend your answer on measures linked to each store and flow."),
        QUIZ("In Gersmehl's model, which flow moves nutrients from the litter store to the soil store?",
             ["Uptake", "Litterfall", "Decomposition", "Leaching"], 2,
             "Decomposers break down dead matter and release nutrients into the soil.",
             feedback=["Uptake is soil to biomass.", "Litterfall is biomass to litter.", "", "Leaching is an output from the soil."]),
        QUIZ("Which store is largest in a savanna nutrient cycle?",
             ["Biomass", "Litter", "Soil", "All three are equal"], 2,
             "Grass roots die into the soil, fire removes litter, and leaching is weaker, so the soil is the main store.",
             feedback=["The biomass is largest in the rainforest, not the savanna.", "Fire keeps the litter store small.", "", "The model's point is that the stores differ in size."]),
        PQ("Draw a Gersmehl diagram for the tropical rainforest and explain the relative size of each store.",
           "Draw Figure 1 (left). Biomass largest: year-round growth gives huge plant mass. Litter small: fast decomposition in heat and moisture. Soil small: leached ferralitic soil with low nutrient-holding capacity and rapid uptake by roots. Thick arrows show fast transfers; label rainfall input, weathering input, runoff and leaching outputs."),
        PQ("A savanna stores 120 units in biomass, 5 in litter and 375 in soil (invented for practice). Calculate the percentage in each store and comment.",
           "Total 500. Biomass 24 percent, litter 1 percent, soil 75 percent. The soil is the main store, unlike the rainforest; burning or grazing the biomass removes less of the total, but erosion of topsoil would be very damaging."),
        PQ("Explain why shifting cultivation with long fallows was sustainable in the rainforest, while permanent clearance is not.",
           "Short clearings were surrounded by forest; after a few years of cropping, the plot was left for many years so the biomass store and litter cycle rebuilt. Permanent clearance removes the biomass store for good, increases runoff and leaching outputs, and the small soil store is soon exhausted. Shortened fallows under population pressure have the same effect."),
        TIP("Paper 2 physical questions have linked the nutrient cycle to managing the selva. Practise one diagram and three management "
            "measures, each tied to a store or flow in the model.", title="Exam link"),
        SUM("Gersmehl's model: three stores (biomass, litter, soil), inputs (rain, weathering), outputs (runoff, leaching) and transfers (litterfall, decomposition, uptake).",
            "Rainforest: biomass is the main and most fragile store; litter and soil are small; flows are fast.",
            "Savanna: soil is the main store; biomass is smaller and burnt or grazed; flows are slower and seasonal.",
            "Residence time = store / annual flow: short for tropical litter, long for taiga litter.",
            "Management must protect the biomass and keep the litter-to-soil cycle going."),
    ],
))

# ---------------------------------------------------------------------------
# Biogeography & Pedology / Plant succession
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_BIO, topic="Plant succession",
    title="Plant succession: psammosere, hydrosere and the climax debate",
    slug="gpl2-plant-succession-seres",
    minutes=25,
    summary="How vegetation develops through seral stages to a climax, the psammosere and hydrosere in detail, secondary succession on tropical fallows, and how to judge the climax concept.",
    objectives=[
        "Define succession, sere, pioneer community, climax and plagioclimax",
        "Describe and explain the stages of a psammosere and a hydrosere",
        "Interpret transect data showing changes along a succession",
        "Evaluate the monoclimax and polyclimax views and apply them to tropical fallows",
    ],
    key_concepts=["Succession", "Sere", "Prisere and subsere", "Pioneer species", "Climatic climax", "Plagioclimax", "Psammosere", "Hydrosere"],
    blocks=[
        H("Introduction"),
        T("When a farmer near Mbalmayo abandons a field, it does not stay bare. Within a year it is covered by weeds and fast-growing "
          "shrubs; after a few years pioneer trees such as the umbrella tree (Musanga) appear; after many decades, the plot looks more "
          "and more like the surrounding forest. On the lava flows of Mount Cameroon, by contrast, plants must start on bare rock. "
          "Both are examples of **plant succession**."),
        D("**Succession** is the gradual, directional change in the plant community of an area over time, as each community alters the "
          "environment (soil, light, moisture) and makes it suitable for the next. Each stage is a **seral stage**, and the whole "
          "sequence is a **sere**.", title="Succession and sere"),
        D("A **prisere** (primary succession) starts on a surface never vegetated before: bare rock, new sand, open water. A "
          "**subsere** (secondary succession) starts where vegetation has been removed but soil remains: abandoned farms, burnt or "
          "logged land. Subseres are faster because soil and seeds are already present.", title="Primary and secondary succession"),
        KEY("How succession works", "The same processes drive every sere.", cards=[
            ["Colonisation", "Pioneer species tolerate harsh conditions: lichens on rock, salt-tolerant grasses on sand, submerged plants in water."],
            ["Modification", "Plants trap sediment, add organic matter, build soil, shade the ground and change moisture and pH."],
            ["Competition and replacement", "Taller, more demanding species arrive and shade out the pioneers."],
            ["Stabilisation", "Change slows as the community comes into balance with the climate: the climax."],
        ]),
        H("The psammosere (sand dunes)"),
        T("On a sandy coast with onshore winds, a psammosere develops inland from the beach. **Embryo dunes** form where salt-tolerant "
          "pioneers trap blown sand. **Fore dunes (yellow dunes)** grow higher as marram grass, which thrives when buried and binds sand "
          "with long roots, takes over. **Grey dunes** further inland are fixed: humus darkens the sand, mosses and lichens appear and "
          "rainwater leaches shell calcium so pH falls. **Dune slacks** are damp hollows near the water table. Inland, heath and scrub "
          "lead to woodland, the climax where the climate allows."),
        CODE("""
Distance from    Zone          Species   Bare sand   Soil pH
the sea (m)                    found     (% cover)
     20          embryo dune       2         80        8.4
     60          yellow dune       5         45        8.0
    150          grey dune        11         10        7.1
    300          scrub            16          0        6.2
""", "text", title="Table 1. A dune transect (figures invented for practice)"),
        H("The hydrosere (fresh water)"),
        IMG("algpl2-hydrosere.svg", alt="Cross-section of a lake edge: submerged plants in open water, floating-leaved plants, a reed swamp at the edge, fen with shrubs on the wet margin and woodland on dry land, with an arrow showing zones advancing into the lake",
            caption="Figure 1. Zones of a hydrosere. In space they mirror the stages in time."),
        T("In a shallow lake, submerged plants trap silt and their remains build up the bed. Floating-leaved plants follow as the water "
          "shallows, then reeds and rushes at the edge (reed swamp). Accumulating organic matter raises the surface above the water "
          "table, creating fen and marsh with sedges and shrubs, and finally woodland. The zones around the lake show the stages: "
          "each zone advances into the water over time."),
        H("Climax and its critics"),
        T("Frederic Clements argued that in any climate region succession leads to one **climatic climax** (the monoclimax view). "
          "Arthur Tansley argued for a **polyclimax**: soil, drainage or relief can hold a stable community different from the climatic "
          "one (an edaphic climax). Where people hold the vegetation back by burning, grazing or cutting, the stable result is a "
          "**plagioclimax**. A **subclimax** is a stage that stays for a long time because some factor stops further change. Modern "
          "ecologists also stress that disturbance (storms, fire, tree falls) is normal, so the climax is rarely reached everywhere."),
        H("Worked examples"),
        EX("Worked example 1: interpreting the dune transect", intro="Use Table 1 to describe and explain the changes inland.", steps=[
            S("Describe", text="From 20 m to 300 m, species rise from 2 to 16, bare sand falls from 80 to 0 percent, and pH falls from 8.4 to 6.2."),
            S("Explain species and cover", text="Inland, sand is fixed, salt spray and wind decrease, and humus holds water, so more demanding species can survive and cover becomes complete."),
            S("Explain pH", text="Fresh sand is rich in shell fragments (calcium carbonate); rain leaches this over time and humus adds organic acids, so older dunes are more acid."),
            S("Conclusion", text="Distance from the sea stands for time: the transect shows succession in space."),
        ]),
        EX("Worked example 2: secondary succession on a forest fallow", intro="Describe and explain the stages of vegetation recovery on an abandoned farm in the humid forest zone.", steps=[
            S("Stage 1 (first year)", text="Weeds and grasses from seeds in the soil and from nearby; fast-growing, light-demanding."),
            S("Stage 2 (a few years)", text="Shrubs and climbers form dense bush; fast-growing pioneer trees such as Musanga shade the ground."),
            S("Stage 3 (decades)", text="Shade-tolerant forest trees grow under the pioneers, which die out; litter and humus rebuild the nutrient cycle."),
            S("Climax", text="Over a long period the plot approaches mature forest, unless it is cleared again; frequent clearing holds it at bush, a plagioclimax."),
        ]),
        EX("Worked example 3: essay plan", intro="Evaluate the concept of the climatic climax.", steps=[
            S("Introduction", text="Define succession and Clements's monoclimax."),
            S("Strengths", text="Explains the broad match between climate belts and vegetation; predicts the direction of change on fallows and dunes."),
            S("Weaknesses", text="Polyclimax: soils and drainage give stable edaphic climaxes; plagioclimaxes are widespread; disturbance and climate change mean many areas never stabilise."),
            S("Tropical evidence", text="Savanna maintained by fire, and secondary forest on long fallows, show how people shape the end point."),
            S("Conclusion", text="A useful model of the potential vegetation, but the actual vegetation is often a polyclimax or plagioclimax."),
        ]),
        MISTAKE("Mixing up primary and secondary succession", "If soil remains (abandoned farm, burnt forest), it is secondary. Primary succession starts on surfaces with no soil, such as new lava or sand."),
        MISTAKE("Listing stages without the processes", "Explain how each stage changes the conditions for the next: trapping sand, adding humus, shading, lowering pH."),
        QUIZ("Which plant is typical of the yellow (fore) dune stage of a psammosere?",
             ["Marram grass", "Water lily", "Oak or other woodland trees", "Reeds"], 0,
             "Marram grass grows well when buried by sand and binds the dune with long roots.",
             feedback=["", "Water lilies are floating-leaved plants of a hydrosere.", "Woodland is the climax inland.", "Reeds belong to the reed swamp of a hydrosere."]),
        QUIZ("Vegetation on a plot is kept as grassland by burning every dry season. What is it?",
             ["A prisere", "A climatic climax", "A plagioclimax", "A pioneer community"], 2,
             "Human burning deflects and holds the succession: a plagioclimax.",
             feedback=["A prisere is primary succession on a new surface.", "A climatic climax would be reached if burning stopped and the climate allowed.", "", "Pioneers are the first colonisers."]),
        PQ("Distinguish between a prisere and a subsere, with an example of each.",
           "Prisere: primary succession on a surface with no soil or vegetation, e.g. new lava on Mount Cameroon or newly deposited sand (psammosere). Subsere: secondary succession where vegetation is removed but soil remains, e.g. an abandoned farm in the forest zone. Subseres are faster because soil, seeds and roots remain."),
        PQ("Describe and explain the stages of a hydrosere. (Use a labelled diagram.)",
           "Draw Figure 1. Submerged plants trap silt and add organic matter; floating-leaved plants as the water shallows; reed swamp at the edge; fen and marsh as peat raises the surface; shrubs, then woodland on dry land. Each stage shallows and dries the site, allowing the next."),
        PQ("Using Table 1, calculate the change in pH from the embryo dune to the scrub zone and explain it.",
           "8.4 - 6.2 = 2.2 units of pH lower inland. Shell fragments are leached by rain over time and humus adds organic acids, so the older, inland dunes are more acid."),
        TIP("Succession is a frequent Paper 1 topic (stages, terms) and appears in Paper 2 physical essays. In Paper 3, a vegetation "
            "transect or quadrat survey is a natural fieldwork study: practise presenting and explaining transect data like Table 1.",
            title="Exam link"),
        SUM("Succession: directional change through seral stages; each community changes conditions for the next.",
            "Prisere starts with no soil; subsere starts where soil remains, so it is faster.",
            "Psammosere: embryo, yellow (marram), grey dunes, slacks, scrub, woodland; pH falls and species rise inland.",
            "Hydrosere: submerged, floating, reed swamp, fen, woodland as the lake fills.",
            "Clements's monoclimax versus Tansley's polyclimax; people create plagioclimaxes."),
    ],
))

# ---------------------------------------------------------------------------
# Tectonic, Slope, Coastal & Arid Geomorphology / Plate tectonics and landforms
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_GEO, topic="Plate tectonics and landforms",
    title="Plate tectonics: boundaries, landforms and the Cameroon Volcanic Line",
    slug="gpl2-plate-tectonics-landforms",
    minutes=25,
    summary="The evidence and mechanisms of plate tectonics, the landforms of divergent, convergent and transform boundaries and hotspots, and the volcanoes of Cameroon with their benefits and hazards.",
    objectives=[
        "Explain the evidence for plate tectonics and the forces that move plates",
        "Explain the landforms of each type of plate boundary and of hotspots",
        "Calculate rates of sea-floor spreading from distance and age",
        "Assess the benefits and hazards of living in volcanic regions such as the Cameroon Volcanic Line",
    ],
    key_concepts=["Lithosphere", "Asthenosphere", "Sea-floor spreading", "Subduction", "Divergent boundary", "Convergent boundary", "Transform fault", "Hotspot"],
    blocks=[
        H("Introduction"),
        T("Mount Cameroon, the highest mountain in West and Central Africa, is an active volcano: it erupted in 1999 and 2000, sending "
          "lava towards villages and the coast road. Yet thousands of farmers grow cocoa, bananas and food crops on its slopes, attracted "
          "by fertile volcanic soils. To understand why the volcano is there, and why people accept the risk, you need the theory of "
          "plate tectonics."),
        D("The **lithosphere** is the rigid outer shell of the Earth (crust plus uppermost mantle), broken into plates. Below it the "
          "**asthenosphere** is hotter and weaker and can flow very slowly. Plates move a few centimetres a year over the asthenosphere.",
          title="Lithosphere and asthenosphere"),
        H("Evidence and mechanism"),
        T("Alfred Wegener proposed continental drift in 1912, using the fit of the continents, matching rocks and fossils across "
          "oceans and evidence of past climates. His idea lacked a mechanism. From the 1960s, ocean surveys showed **sea-floor "
          "spreading**: new crust forms at mid-ocean ridges, rocks get older away from the ridge, and bands of reversed and normal "
          "magnetism lie symmetrically on both sides. Earthquakes and volcanoes cluster along narrow belts that mark plate edges."),
        T("Plates move because of **mantle convection** (heat from the interior), **ridge push** (new, hot, high lithosphere slides away "
          "from the ridge) and **slab pull** (cold, dense ocean lithosphere sinks at subduction zones and drags the plate). Many "
          "geologists now think slab pull is the strongest force; check the emphasis in your textbook."),
        IMG("algpl2-plates.svg", alt="Cross-section showing a mid-ocean ridge with plates moving apart, oceanic crust moving towards a trench, the ocean plate sinking beneath a continent at a subduction zone, and volcanic fold mountains on the continent fed by rising magma",
            caption="Figure 1. A divergent and a convergent boundary in cross-section (schematic, not to scale)."),
        H("Boundaries and their landforms"),
        KEY("Plate boundaries", "Name the boundary, the process and the landforms.", cards=[
            ["Divergent (constructive)", "Plates move apart; magma rises and makes new crust. Oceans: mid-ocean ridges, shallow earthquakes, fissure volcanoes (Iceland). Continents: rift valleys bounded by normal faults (East African Rift)."],
            ["Convergent: ocean-continent", "Dense ocean plate subducts: deep trench, explosive andesitic volcanoes and fold mountains on the continent (Andes)."],
            ["Convergent: ocean-ocean and continent-continent", "Ocean-ocean: trench and volcanic island arc (Japan). Continent-continent: neither sinks far; crust crumples into high fold mountains with no volcanoes (Himalayas)."],
            ["Transform (conservative)", "Plates slide past each other along a fault; no crust made or destroyed; shallow but strong earthquakes (San Andreas Fault)."],
        ]),
        D("A **hotspot** is a plume of unusually hot mantle that rises under a plate and feeds volcanoes away from plate boundaries. "
          "As the plate moves over it, a chain of volcanoes forms that gets older away from the active end (Hawaii).", title="Hotspot"),
        H("The Cameroon Volcanic Line"),
        T("A line of volcanoes runs from the islands of the Gulf of Guinea (Bioko, São Tomé, Príncipe, Annobón) north-east through Mount "
          "Cameroon, Manengouba, the Bamboutos and Oku massifs, towards the Adamawa Plateau. It lies **inside** the African plate, not on a "
          "boundary. Its origin is debated: a hotspot, a zone of weakness in the lithosphere reactivated by plate movement, or a "
          "combination. Unlike Hawaii, the volcanoes do not get steadily older along the line. Check your textbook for the explanation it "
          "prefers."),
        T("Landforms include the large composite volcano of Mount Cameroon with many small cinder cones on its flanks, crater lakes such "
          "as Lake Nyos and Lake Barombi Mbo, and basalt lava plateaus in the Western Highlands. In 1986 a sudden release of carbon "
          "dioxide from Lake Nyos killed many people and animals in the valleys below: a volcanic hazard without an eruption."),
        H("Worked examples"),
        EX("Worked example 1: spreading rate", intro="Rock 100 km from a mid-ocean ridge is 5 million years old. Find the rate at which this plate moves away from the ridge in cm per year, and the full spreading rate.", steps=[
            S("Convert the distance", math=r"100\text{ km} = 100\times 1000\times 100 = 10^{7}\text{ cm}"),
            S("Rate on one side", math=r"\frac{10^{7}\text{ cm}}{5\times 10^{6}\text{ yr}} = 2\text{ cm/yr}"),
            S("Full spreading rate (both plates)", math=r"2\times 2 = 4\text{ cm/yr}"),
        ], check=r"4\text{ cm/yr}\times 5\times 10^{6}\text{ yr} = 200\text{ km between rocks of equal age}"),
        EX("Worked example 2: why the Himalayas have no volcanoes", intro="Explain why fold mountains at a continent-continent boundary lack the volcanoes found in the Andes.", steps=[
            S("Andes", text="Dense oceanic lithosphere subducts beneath South America; water released from the sinking slab lowers the melting point of the mantle above, making magma that rises to form volcanoes."),
            S("Himalayas", text="Both plates are continental and buoyant, so neither subducts deeply; there is no sinking slab to generate magma."),
            S("Result", text="Crust is thickened by folding and thrust faulting into very high mountains, with frequent earthquakes but few or no volcanoes."),
        ]),
        EX("Worked example 3: essay plan", intro="Explain why people continue to live in volcanic regions despite the risks, and examine measures to reduce volcanic hazards.", steps=[
            S("Benefits", text="Fertile volcanic soils (cash and food crops on Mount Cameroon); tourism (crater lakes, climbing Mount Cameroon); geothermal energy and building stone; cooler, healthier highland climates."),
            S("Why the risk is accepted", text="Eruptions are infrequent and lava often moves slowly; people may lack land elsewhere; ties to ancestral land; perception that the risk is low."),
            S("Mitigation", text="Monitoring of earthquakes, gases and ground swelling; hazard maps and land-use zoning; degassing Lake Nyos with pipes to release CO2 slowly."),
            S("Adaptation", text="Evacuation plans and drills, warning systems, education, insurance and emergency shelters."),
            S("Conclusion", text="Benefits are daily and visible, hazards rare; good monitoring and planning let people keep the benefits while reducing the risks."),
        ]),
        MISTAKE("Giving only the benefits", "Questions on why people live in volcanic areas expect you to weigh the benefits against the risks they accept. Name the hazard as well as the attraction."),
        MISTAKE("Calling Mount Cameroon a plate-boundary volcano", "The Cameroon Volcanic Line is within the African plate. Do not put it on a subduction zone; explain the debated intraplate origin."),
        QUIZ("Which landform is produced where two plates of oceanic lithosphere converge?",
             ["A rift valley", "A volcanic island arc and trench", "Fold mountains without volcanoes", "A transform fault"], 1,
             "One ocean plate subducts beneath the other, forming a trench and a curved chain of volcanic islands.",
             feedback=["Rift valleys form where plates diverge.", "", "That is a continent-continent boundary.", "Transform faults form where plates slide past each other."]),
        QUIZ("Which evidence most directly shows sea-floor spreading?",
             ["The jigsaw fit of Africa and South America", "Symmetrical magnetic stripes and increasing rock age away from ridges", "Glacial deposits in tropical Africa", "Coal seams in Antarctica"], 1,
             "Ocean rocks record reversals of the magnetic field in matching bands on both sides of the ridge, and get older away from it.",
             feedback=["This supported continental drift, not spreading of the ocean floor.", "", "Past climates supported drift, not spreading.", "Fossil fuels in cold places support drift."]),
        PQ("Rock 150 km from a ridge is 3 million years old. Calculate the rate of plate movement in mm per year.",
           r"150 km = 150 000 000 mm. Rate = 150 000 000 / 3 000 000 = 50 mm per year on that side (5 cm per year)."),
        PQ("Describe and explain the landforms found at a divergent plate boundary.",
           "Plan: Plates pull apart; mantle decompression melting gives basaltic magma. Ocean: mid-ocean ridge with central rift, transform offsets, fissure eruptions, new crust, shallow earthquakes. Continent: crust stretches, blocks drop between normal faults, forming a rift valley with steep scarps, lakes and volcanoes (East African Rift). Use a labelled diagram."),
        PQ("'The Cameroon Volcanic Line cannot be explained by plate boundary processes.' Discuss.",
           "Plan: Agree: it lies inside the African plate, far from any boundary; no subduction or spreading. Explanations: hotspot or mantle plume; reactivated lithospheric weakness; edge effects between thick and thin lithosphere. Evidence against a simple hotspot: no clear age progression. Judgement: plate tectonics still provides the framework (plate stresses, mantle flow), but not boundary processes; origin debated."),
        TIP("Geomorphology has its own questions in Paper 1 and in the physical section of Paper 2, where questions have combined "
            "volcanic benefits with measures to reduce hazards. The relief of Cameroon, including the volcanic line, is tested in "
            "Paper 3.", title="Exam link"),
        SUM("Rigid lithospheric plates move over the asthenosphere, driven by mantle convection, ridge push and slab pull.",
            "Divergent: ridges and rift valleys. Convergent: trenches, volcanic fold mountains, island arcs, or high fold mountains without volcanoes. Transform: faults and earthquakes.",
            "Spreading rate = distance from ridge / age of rock; double it for the full rate.",
            "The Cameroon Volcanic Line is intraplate; its origin is debated.",
            "Volcanic regions offer fertile soils, tourism and energy; hazards are reduced by monitoring, zoning and preparedness."),
    ],
))

# ---------------------------------------------------------------------------
# Tectonic, Slope, Coastal & Arid Geomorphology / Weathering
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_GEO, topic="Weathering",
    title="Weathering: processes, climatic controls and deep tropical weathering",
    slug="gpl2-weathering-processes-controls",
    minutes=24,
    summary="Physical, chemical and biological weathering at A Level depth, how climate controls weathering (Peltier, Van't Hoff), and how deep tropical weathering produces tors and inselbergs.",
    objectives=[
        "Explain the main physical, chemical and biological weathering processes",
        "Explain how climate, rock type and rock structure control the type and rate of weathering",
        "Apply the Van't Hoff rule to estimate changes in chemical weathering rates",
        "Explain deep weathering in the tropics and the two-stage formation of tors and inselbergs",
    ],
    key_concepts=["Weathering", "Hydrolysis", "Carbonation", "Freeze-thaw", "Pressure release", "Peltier diagram", "Weathering front", "Inselberg"],
    blocks=[
        H("Introduction"),
        T("In southern Cameroon, road cuttings show rock rotted to a soft, red or mottled clay many metres deep. Here and there a smooth "
          "granite dome rises above the plains like an island. Both come from weathering, the first stage of almost every landform in "
          "this module. Weathering prepares material for mass movement, rivers, waves and wind to remove.\n\n"
          "At O Level you named the types of weathering. Here you explain the processes, what controls them, and the landforms they "
          "leave in the tropics."),
        D("**Weathering** is the breakdown and decay of rock at or near the Earth's surface, in place (in situ), by physical, chemical "
          "and biological processes. Unlike erosion, it needs no moving agent. The layer of loose weathered material is the "
          "**regolith**; deeply rotted rock that keeps the original rock structure is **saprolite**.", title="Weathering"),
        H("Physical (mechanical) weathering"),
        KEY("Physical processes", "Rock breaks into smaller pieces without a change in its minerals.", cards=[
            ["Freeze-thaw", "Water in joints expands by about 9 percent when it freezes, wedging rock apart. Needs many cycles around 0 degrees Celsius and moisture: high mountains and cold climates."],
            ["Thermal expansion (insolation)", "Large daily temperature ranges in deserts heat and cool the outer layer more than the inside; with a little moisture, flakes peel off."],
            ["Salt crystallisation", "Salt crystals growing from evaporating water in pores exert pressure: important in deserts and on coasts."],
            ["Pressure release (dilatation)", "When overlying rock is eroded, the unloaded rock expands and cracks parallel to the surface, giving sheeting joints and exfoliation domes."],
        ]),
        H("Chemical weathering"),
        T("Chemical weathering changes the minerals themselves. **Hydrolysis** is the reaction of minerals with water: feldspar in granite "
          "turns into kaolinite clay, releasing ions in solution; this is why granite rots to clay with quartz grains. **Oxidation** "
          "turns iron in minerals into red-brown iron oxides. **Hydration** is the absorption of water into minerals, making them swell. "
          "**Solution** dissolves soluble minerals such as rock salt. **Carbonation** is the solution of limestone by rainwater containing "
          "dissolved carbon dioxide (carbonic acid):"),
        F(r"\mathrm{CaCO_3 + H_2O + CO_2 \rightarrow Ca(HCO_3)_2}", title="Carbonation of limestone"),
        T("**Biological weathering** includes root wedging, burrowing animals, and organic acids from lichens and decaying plants that "
          "speed up chemical reactions. In the tropics, termites and plant acids are important."),
        H("What controls weathering?"),
        T("**Climate** is the main control. Chemical reactions speed up with heat and need water. The **Van't Hoff rule** states that "
          "the rate of a chemical reaction roughly doubles for each 10 degree Celsius rise in temperature. The geomorphologist Louis "
          "Peltier (1950) drew a diagram of weathering regions using mean annual temperature and rainfall: strong chemical weathering in "
          "hot, wet climates, strong frost weathering in cold, moist ones, and slight weathering in hot or cold deserts."),
        F(r"\text{rate factor} = 2^{\,\Delta T / 10}", title="Van't Hoff rule (approximate)"),
        T("**Rock type** matters: minerals that form at high temperatures (olivine, feldspar) are less stable at the surface and weather "
          "faster than quartz. **Rock structure** matters: joints, bedding planes and faults let water in and increase the surface area "
          "attacked. **Vegetation** and **time** also control how deep the weathering goes."),
        H("Deep weathering, tors and inselbergs"),
        IMG("algpl2-deep-weathering.svg", alt="Two panels: first, thick regolith over jointed granite with rounded corestones above an irregular weathering front; second, the regolith stripped away leaving a stack of rounded blocks (a tor) standing above the lowered surface",
            caption="Figure 1. The two-stage model: deep weathering, then stripping of the regolith (schematic)."),
        T("In the humid tropics, hot, wet conditions acting over millions of years on stable land surfaces can rot rock to depths of "
          "tens of metres. The lower boundary between rotted and fresh rock is the **weathering front** (basal surface of weathering). "
          "Where joints are widely spaced, unweathered **corestones** survive. If erosion later strips the regolith, perhaps after a "
          "change to a drier climate or uplift, the corestones and the high points of the front are exposed as **tors** and, on a "
          "large scale, as dome-shaped **inselbergs** (bornhardts). This two-stage idea is linked to D. L. Linton's work on tors; other "
          "writers explain inselbergs by slope retreat under semi-arid conditions, so check your textbook."),
        H("Worked examples"),
        EX("Worked example 1: Van't Hoff rule", intro="By how many times would chemical weathering speed up if mean temperature rose from 15 to 35 degrees Celsius, other things equal?", steps=[
            S("Temperature change", math=r"\Delta T = 35 - 15 = 20^{\circ}\text{C}"),
            S("Number of 10-degree steps", math=r"\frac{20}{10} = 2"),
            S("Rate factor", math=r"2^{2} = 4"),
            S("Meaning", text="Chemical weathering is about four times faster: one reason weathering is so deep in the humid tropics."),
        ]),
        EX("Worked example 2: weathering in two climates", intro="Compare the dominant weathering in the humid south of Cameroon and in the Sahara.", steps=[
            S("Humid south", text="Hot and wet all year: hydrolysis and oxidation dominate (Peltier's strong chemical region); deep red saprolite and ferralitic soils."),
            S("Sahara", text="Very dry, large daily temperature range: salt crystallisation and thermal stress, with slow chemical weathering because water is scarce."),
            S("Conclusion", text="Temperature sets the speed of reactions, but water decides whether chemical weathering can happen at all."),
        ]),
        EX("Worked example 3: essay plan", intro="Assess the importance of climate in controlling the type and rate of weathering.", steps=[
            S("Introduction", text="Define weathering; state the controls: climate, rock type, structure, vegetation, time."),
            S("Climate important", text="Peltier's diagram; Van't Hoff rule; freeze-thaw needs cycles around 0 degrees; deep tropical weathering."),
            S("Other controls", text="Granite and basalt weather differently in the same climate; dense joints speed weathering; limestone is weathered by carbonation even in cool climates."),
            S("Interaction", text="Vegetation (organic acids) and time strengthen climatic effects; microclimates matter (shade, aspect)."),
            S("Conclusion", text="Climate controls the broad pattern; rock type and structure control local variation and detailed landforms."),
        ]),
        MISTAKE("Using weathering and erosion as the same thing", "Weathering happens in place with no moving agent. Once material is carried away by water, ice, wind or gravity, it is erosion or mass movement."),
        MISTAKE("Saying that hot deserts have no chemical weathering", "It is slow, not absent: dew and rare rain allow some salt weathering and hydration. Say which process dominates and why."),
        QUIZ("Which process turns feldspar in granite into kaolinite clay?",
             ["Carbonation", "Hydrolysis", "Freeze-thaw", "Pressure release"], 1,
             "Hydrolysis is the reaction of silicate minerals with water.",
             feedback=["Carbonation attacks calcium carbonate (limestone).", "", "Freeze-thaw breaks rock physically; it does not change minerals.", "Pressure release cracks rock; it does not make clay."]),
        QUIZ("A granite dome far below its original cover has curved sheets peeling off its surface. Which process is mainly responsible?",
             ["Pressure release", "Carbonation", "Oxidation", "Root wedging"], 0,
             "Removal of the overlying rock lets the granite expand, forming sheeting joints parallel to the surface.",
             feedback=["", "Granite has no calcium carbonate.", "Oxidation changes colour; it does not create curved sheets.", "Roots widen existing cracks; they do not create curved sheeting."]),
        PQ("Using the Van't Hoff rule, estimate how much faster chemical weathering is at 40 degrees than at 10 degrees Celsius.",
           r"Change = 30 degrees = 3 steps of 10 degrees. Factor = 2 x 2 x 2 = 8. About eight times faster, other things equal."),
        PQ("Explain the formation of tors and inselbergs in tropical regions. (Use diagrams.)",
           "Stage 1: deep chemical weathering (hydrolysis) under a hot, wet climate along joints; closely jointed rock rots to saprolite; widely jointed parts survive as corestones; an irregular weathering front forms. "
           "Stage 2: change in climate or base level allows erosion to strip the regolith, exposing corestones as tors and larger unjointed masses as inselbergs. Mention alternative views (slope retreat)."),
        PQ("With reference to a Peltier-type diagram, explain how weathering varies with climate.",
           "Hot, wet: strong chemical weathering (fast reactions, plenty of water). Cold, moist: strong frost action (many freeze-thaw cycles). Hot or cold dry: weak weathering, mainly physical (salt, thermal stress) because water is scarce. Temperate: moderate chemical with some frost. Explain each with temperature and water."),
        TIP("Weathering supports questions on slopes, landforms and soils in Paper 1 and Paper 2. In Paper 2 essays, link weathering "
            "to the landform (tor, inselberg, exfoliation dome) rather than describing processes on their own.", title="Exam link"),
        SUM("Weathering breaks rock in place; physical processes break it, chemical processes change its minerals.",
            "Key chemical processes: hydrolysis, oxidation, hydration, solution, carbonation; biological agents speed them up.",
            "Climate is the main control: Van't Hoff (rate doubles per 10 degrees) and Peltier's weathering regions.",
            "Rock type, joints, vegetation and time explain local differences.",
            "Deep tropical weathering and later stripping produce tors and inselbergs (two-stage model)."),
    ],
))

# ---------------------------------------------------------------------------
# Tectonic, Slope, Coastal & Arid Geomorphology / Slope processes and mass movement
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_GEO, topic="Slope processes and mass movement",
    title="Slope processes and mass movement: forces, types and management",
    slug="gpl2-slope-processes-mass-movement",
    minutes=25,
    summary="Why slopes fail (shear stress against shear strength), the factor of safety, slow and rapid mass movements classified by speed and water, slope evolution theories and how to reduce landslide risk.",
    objectives=[
        "Explain slope stability using shear stress, shear strength and the factor of safety",
        "Classify mass movements by speed, water content and type of movement",
        "Explain the causes of rapid mass movement, distinguishing it from soil erosion",
        "Evaluate measures to reduce the impacts of mass movement and theories of slope evolution",
    ],
    key_concepts=["Mass movement", "Shear stress", "Shear strength", "Factor of safety", "Pore water pressure", "Soil creep", "Rotational slump", "Mudflow"],
    blocks=[
        H("Introduction"),
        T("In late October 2019, after days of heavy rain, a hillside collapsed onto homes in the Gouache neighbourhood of Bafoussam, "
          "killing dozens of people (check the exact figures in your textbook or a reliable report). Landslides also affect roads in the "
          "Western Highlands and on the slopes of Mount Cameroon in most rainy seasons. Why do some slopes stay stable for centuries and "
          "then fail in one night?"),
        D("**Mass movement** is the downslope movement of weathered material (regolith, soil, rock) as a mass under the direct influence "
          "of gravity. Water may help, but the material is not carried by a flowing river, wind or ice. **Soil erosion** is different: "
          "particles are removed one by one by running water or wind.", title="Mass movement"),
        H("Why slopes fail"),
        T("Gravity pulls material on a slope. The part of the weight acting down the slope is the **shear stress**. The resistance of "
          "the material, from friction between particles, cohesion (binding by clay, roots) and the strength of the rock, is the "
          "**shear strength**. A slope fails when shear stress becomes greater than shear strength."),
        D("The **factor of safety** compares resisting and driving forces. If F is greater than 1 the slope is stable; if F falls to 1 "
          "or below, failure is likely.", title="Factor of safety", formula=r"F = \frac{\text{shear strength}}{\text{shear stress}}"),
        KEY("What changes the balance?", "Most landslides have a long-term preparing cause and a short-term trigger.", cards=[
            ["Increase shear stress", "Steepening or undercutting by rivers, waves or road cuttings; adding weight (buildings, saturated soil, waste dumps); earthquake shaking."],
            ["Reduce shear strength", "Water: high pore water pressure pushes grains apart and reduces friction; weathering of rock to clay; removal of vegetation and its roots; bedding planes or joints dipping out of the slope."],
            ["Typical triggers", "Intense or prolonged rainfall, an earthquake, or a cut made at the foot of the slope."],
        ]),
        H("Types of mass movement"),
        IMG("algpl2-mass-movement.svg", alt="Chart with water content from dry to wet on the horizontal axis and speed from slow to fast on the vertical axis: rockfall and rockslide dry and fast; mudflow wet and fast; earthflow moderately wet and fairly fast; slump in the middle; soil creep dry and slow; solifluction wet and slow",
            caption="Figure 1. Mass movements by speed and water content (a simplified version of the classification triangles used in textbooks, such as Carson and Kirkby's)."),
        T("**Slow movements.** **Soil creep** is the very slow downslope movement of soil, often by heave: particles rise at right angles "
          "to the slope when the soil wets (or freezes) and settle vertically when it dries, so each cycle moves them slightly downhill. "
          "Evidence: bent tree trunks, tilted fences and walls, terracettes. **Solifluction** is the slow flow of saturated soil, typical "
          "of periglacial areas where the subsoil is frozen."),
        T("**Rapid movements.** **Falls**: rock drops freely from a steep face. **Slides**: a coherent mass moves along a plane, either "
          "straight (translational slide along a bedding plane) or curved (a **rotational slump**, which leaves a back-tilted block and a "
          "curved scar, common in clays). **Flows**: material moves like a fluid; **earthflows** and **mudflows** need a lot of water, "
          "and volcanic mudflows are called lahars. Rainsplash and sheetwash also move soil on slopes, but they act grain by grain."),
        H("Slope form and evolution"),
        T("Many slopes have a convex upper part (creep dominant), a straight middle (rapid movements, wash) and a concave foot "
          "(deposition). Three classic theories explain how slopes change over time: W. M. Davis's **slope decline** (slopes become "
          "gentler as the land is worn down, in humid climates), W. Penck's **slope replacement** (gentle lower slopes grow upward and "
          "replace steeper ones) and L. C. King's **parallel retreat** (slopes keep their angle and retreat, leaving pediments, in "
          "semi-arid climates). Real slopes often show features of more than one."),
        H("Worked examples"),
        EX("Worked example 1: factor of safety before and after rain", intro="A slope has a shear strength of 120 kPa and a shear stress of 100 kPa. After a week of heavy rain, pore water pressure lowers the shear strength to 90 kPa (figures invented for practice). Calculate F each time.", steps=[
            S("Before the rain", math=r"F = \frac{120}{100} = 1.2"),
            S("Interpret", text="F is greater than 1: the slope is stable."),
            S("After the rain", math=r"F = \frac{90}{100} = 0.9"),
            S("Interpret", text="F is below 1: shear stress exceeds strength and the slope is likely to fail. Water reduced the strength; the shear stress did not even need to rise."),
        ]),
        EX("Worked example 2: explaining a landslide in a highland town", intro="Explain three causes of a rapid mass movement on a densely settled hillside in a wet highland region.", steps=[
            S("Heavy rainfall", text="Prolonged rain saturates deep weathered regolith; pore water pressure rises and shear strength falls."),
            S("Removal of vegetation", text="Clearing for farms and houses removes roots that bind the soil and reduces interception and transpiration."),
            S("Cutting and loading the slope", text="Excavating the foot of the slope for building plots and roads steepens it, while houses add weight higher up, increasing shear stress."),
        ]),
        EX("Worked example 3: essay plan on reducing the impacts", intro="Propose measures to reduce the negative impacts of mass movements and assess their effectiveness.", steps=[
            S("Engineering", text="Drainage (pipes, channels) to lower pore water pressure; retaining walls, gabions and rock bolts; regrading to gentler angles. Effective but costly."),
            S("Biological", text="Replanting deep-rooted vegetation and keeping forest on steep slopes; cheap and sustainable but slow to work."),
            S("Planning", text="Hazard mapping and banning building on steep or previously failed slopes; building codes; resettlement where risk is high. Depends on enforcement."),
            S("Warning and preparedness", text="Rain gauges and warnings, monitoring of cracks, community education and evacuation."),
            S("Conclusion", text="Combining drainage, vegetation and land-use control works best; engineering alone is too costly for most towns."),
        ]),
        MISTAKE("Confusing mass movement with soil erosion", "Soil erosion removes particles one at a time by water or wind; mass movement moves a whole mass under gravity. Measures differ too: contour ploughing is a soil erosion measure, drainage and retaining walls are mass movement measures."),
        MISTAKE("Drifting into earthquakes and volcanoes", "An earthquake can trigger a landslide, but when a question is on mass movement, explain the slope processes; do not write about earthquake or volcanic hazards in general."),
        QUIZ("A slope has F = 1.5. Heavy rain halves its shear strength while the shear stress stays the same. What is the new factor of safety?",
             ["0.5", "0.75", "1.5", "3.0"], 1,
             "F = strength / stress; halving strength halves F: 1.5 / 2 = 0.75, so the slope is likely to fail.",
             feedback=["This would need strength to fall to one third.", "", "F must change when strength changes.", "Halving strength reduces F; it does not double it."]),
        QUIZ("Which feature is the best evidence of soil creep?",
             ["A curved scar with a back-tilted block", "Bent tree trunks and tilted fence posts", "A fan of boulders below a cliff", "A lobe of mud that flowed onto a road"], 1,
             "Slow, continuous creep tilts posts and makes trees curve as they keep growing upright.",
             feedback=["That shows a rotational slump.", "", "That is scree from rockfall.", "That is a mudflow or earthflow."]),
        PQ("A slope has a shear strength of 150 kPa and a shear stress of 125 kPa. Rain reduces the strength by 25 percent (invented for practice). Calculate F before and after and comment.",
           r"Before: F = 150 / 125 = 1.2 (stable). After: strength = 150 x 0.75 = 112.5 kPa, F = 112.5 / 125 = 0.9 (below 1, failure likely). Water lowers strength through pore water pressure."),
        PQ("Briefly explain three causes of the sudden movement of weathered material and soil down a slope.",
           "Any three, each explained: heavy or prolonged rain raising pore water pressure; undercutting by a river or a road cutting steepening the slope; removal of vegetation; adding weight with buildings; earthquake shaking; weak clay layers or bedding dipping out of the slope."),
        PQ("Evaluate the theories of slope evolution of Davis, Penck and King.",
           "Davis: slope decline, humid climates, slopes flatten over time. Penck: slope replacement from the base upward, depends on rate of uplift and erosion. King: parallel retreat, semi-arid, leaves pediments and inselbergs. Evaluation: each fits some climates and rocks; they are hard to test because slope change takes so long; modern studies measure processes instead. Judgement: useful models, none universal."),
        TIP("Mass movement has been one of the most popular physical questions in Paper 2, combined with measures to reduce its effects. "
            "Keep strictly to mass movement, name each measure and say how it changes shear stress or shear strength.", title="Exam link"),
        SUM("Slopes fail when shear stress exceeds shear strength; F = strength / stress, unstable when F is 1 or less.",
            "Water is the main trigger: pore water pressure lowers strength; undercutting, loading and shaking raise stress.",
            "Slow: creep, solifluction. Rapid: falls, slides (translational, rotational slump), flows (earthflow, mudflow).",
            "Mass movement moves a whole mass under gravity; soil erosion removes grains by water or wind.",
            "Reduce impacts by drainage, retaining structures, vegetation, hazard mapping and warnings."),
    ],
))

# ---------------------------------------------------------------------------
# Tectonic, Slope, Coastal & Arid Geomorphology / Coastal processes and landforms
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_GEO, topic="Coastal processes and landforms",
    title="Coastal processes and landforms: waves, tides, erosion and deposition",
    slug="gpl2-coastal-processes-landforms",
    minutes=25,
    summary="How waves and tides work, wave refraction and longshore drift, the erosional and depositional landforms they create, and how to study a coast in the field.",
    objectives=[
        "Explain how waves form and why destructive and constructive waves have different effects",
        "Explain wave refraction, longshore drift and tidal range",
        "Explain the formation of erosional and depositional coastal landforms",
        "Plan coastal fieldwork and process its measurements",
    ],
    key_concepts=["Fetch", "Swash and backwash", "Wave refraction", "Longshore drift", "Tidal range", "Wave-cut platform", "Spit", "Sediment cell"],
    blocks=[
        H("Introduction"),
        T("Cameroon's coast is short but varied. Near Limbe, black sand beaches and rocky points are made from the volcanic rocks of "
          "Mount Cameroon. Around Kribi, long sandy beaches are broken by rocky outcrops, and the Lobé Falls drop almost straight into "
          "the sea. Between them, the Wouri estuary at Douala is fringed by mangrove swamps. Each of these coasts reflects a balance "
          "between the energy of waves and tides and the material available."),
        H("Waves"),
        D("Waves are formed by wind blowing over the sea surface, which transfers energy to the water. Their size depends on wind speed, "
          "the time the wind blows and the **fetch**, the distance of open water over which the wind blows. Water particles move in "
          "near-circular orbits; the energy, not the water, travels forward. Wave energy rises with the square of wave height.",
          title="Waves and fetch", formula=r"E \propto H^{2}"),
        T("As a wave enters shallow water, friction with the bed slows its base, the wave steepens and breaks. The water rushing up the "
          "beach is the **swash**; the water running back is the **backwash**. **Constructive waves** are low, long and gentle (few per "
          "minute); their strong swash moves sediment up the beach and builds it. **Destructive waves** are high, steep and frequent; "
          "their strong backwash drags material offshore and they erode cliffs."),
        H("Refraction, longshore drift and tides"),
        IMG("algpl2-wave-refraction.svg", alt="Plan view of a coast with a central headland and bays on each side; wave crests bend to follow the coast, orthogonal lines converge on the headland and spread out in the bays where beaches have formed",
            caption="Figure 1. Wave refraction concentrates energy on headlands and spreads it in bays."),
        T("**Wave refraction**: waves slow down first where the water is shallow, off headlands, so the crests bend to become almost "
          "parallel to the coast. Lines drawn at right angles to the crests (orthogonals) converge on headlands, concentrating energy "
          "and erosion there, and diverge in bays, where energy is low and beaches form. Over time this tends to straighten coasts."),
        T("**Longshore drift**: where waves approach at an angle, the swash moves sediment up the beach at that angle but the backwash "
          "returns it straight down the slope under gravity. Material zig-zags along the coast in the direction of the prevailing waves. "
          "A stretch of coast within which sediment moves largely as a closed system is a **sediment cell**."),
        D("**Tides** are the regular rise and fall of the sea caused mainly by the gravitational pull of the Moon and Sun. The **tidal "
          "range** is the difference in height between high and low water. **Spring tides** (largest range) occur when Sun and Moon are "
          "aligned, at new and full moon; **neap tides** (smallest range) when they are at right angles. Tidal range controls the "
          "width of the zone that waves attack and the strength of tidal currents in estuaries.", title="Tides and tidal range"),
        H("Landforms of erosion"),
        T("Waves erode by **hydraulic action** (air compressed in cracks), **abrasion** (waves hurling sediment at the rock), "
          "**attrition** (sediment wearing itself smaller and rounder) and **solution** (on limestone). Wave attack is concentrated "
          "between high and low tide, cutting a **notch**. The cliff above collapses and retreats, leaving a gently sloping "
          "**wave-cut platform** exposed at low tide. On headlands, erosion along joints forms **caves**, which may meet to form an "
          "**arch**; when the arch collapses a **stack** remains, eroded later to a **stump**."),
        TIP("Rock structure decides the outline. Where bands of hard and soft rock meet the coast at right angles (a discordant coast), "
            "headlands and bays form. Where they run parallel to it (a concordant coast), the coast is straighter, with coves where waves "
            "break through the hard band."),
        H("Landforms of deposition"),
        KEY("Depositional landforms", "Deposition happens where wave energy falls or sediment supply is large.", cards=[
            ["Beach", "Accumulation of sand or shingle between low tide and the highest storm waves; features include berms (ridges at high-tide levels) and cusps."],
            ["Spit", "A ridge of sand or shingle joined to the land at one end, built by longshore drift where the coast changes direction, often with a curved (recurved) end and salt marsh or mangrove behind it."],
            ["Bar and tombolo", "A bar grows across a bay, enclosing a lagoon; a tombolo joins an island to the mainland."],
            ["Salt marsh and mangrove", "Fine sediment settles in sheltered estuaries and behind spits; in the tropics, mangroves trap mud with their roots, as in the Wouri estuary."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: wave energy", intro="Storm waves 3 m high replace normal waves 1.5 m high. How many times more energy do they carry?", steps=[
            S("Use the relationship", math=r"E \propto H^{2}"),
            S("Ratio of heights", math=r"\frac{3}{1.5} = 2"),
            S("Ratio of energy", math=r"2^{2} = 4"),
            S("Meaning", text="Doubling wave height gives four times the energy: storms do most of the erosion on many coasts."),
        ]),
        EX("Worked example 2: tidal range and a beach profile", intro="At a beach, high water is 2.6 m and low water 0.4 m above chart datum. A beach profile rises 3 m over a horizontal distance of 40 m. Find the tidal range and the beach angle.", steps=[
            S("Tidal range", math=r"2.6 - 0.4 = 2.2\text{ m}"),
            S("Beach gradient", math=r"\frac{3}{40} = 0.075"),
            S("Beach angle", math=r"\tan^{-1}(0.075) \approx 4.3^{\circ}"),
            S("Interpret", text="A gentle beach of fine sand; shingle beaches are usually steeper because coarse material lets swash soak in and weakens the backwash."),
        ]),
        EX("Worked example 3: explaining a spit", intro="Explain the formation of a spit. (Use a labelled diagram.)", steps=[
            S("Supply and drift", text="Longshore drift carries sand along the coast in the direction of the prevailing waves."),
            S("Change of direction", text="Where the coast turns (for example at an estuary mouth), drift continues into deeper, calmer water and material is deposited, building a ridge out from the land."),
            S("Growth and recurve", text="The ridge lengthens; waves from a second direction or refraction curve its end landward."),
            S("Behind the spit", text="Sheltered water allows mud to settle: salt marsh or mangrove forms. A river current or tidal flow stops the spit from closing the estuary."),
        ]),
        H("Studying a coast in the field"),
        T("Coastal fieldwork is less often chosen than river or urban studies, which is a reason to prepare it carefully. Useful methods: "
          "beach profiles with ranging poles and a clinometer at fixed intervals; measuring pebble size and roundness at points along "
          "the beach to test longshore drift; timing a float to measure drift rate; counting waves per minute to classify them; "
          "sketching landforms. Always plan safety: tide times, no work under cliffs, work in groups."),
        MISTAKE("Saying the water travels with the wave", "In open water the water moves in circles; only energy travels forward. Water moves forward only when the wave breaks (swash)."),
        MISTAKE("Drawing longshore drift with the backwash at an angle", "Swash goes up at the angle of wave approach; backwash returns straight down the beach at right angles to the shoreline, under gravity."),
        QUIZ("Why does wave energy concentrate on headlands?",
             ["Headlands are made of softer rock", "Waves slow first in shallow water off the headland and bend, so orthogonals converge on it", "Tides are higher at headlands", "Longshore drift carries energy to headlands"], 1,
             "This is wave refraction.",
             feedback=["Headlands are usually made of harder rock, which is why they stand out.", "", "Tidal height does not depend on headlands.", "Longshore drift moves sediment, not energy, along the coast."]),
        QUIZ("Which wave type builds beaches?",
             ["Destructive waves with strong backwash", "Constructive waves with strong swash", "Storm waves with a long fetch", "Steep waves breaking ten or more times a minute"], 1,
             "Low, gentle waves push sediment up the beach with a swash stronger than the backwash.",
             feedback=["Strong backwash removes material.", "", "Storm waves are usually destructive.", "Frequent, steep waves are destructive."]),
        PQ("Calculate the tidal range if high water is 3.1 m and low water 0.2 m above datum, and explain why tidal range matters for coastal erosion.",
           "Range = 3.1 - 0.2 = 2.9 m. A larger range spreads wave attack over a wider vertical zone (less concentrated notching) and gives wider intertidal platforms; a small range concentrates attack at one level. Range also controls the strength of tidal currents in estuaries."),
        PQ("Explain the formation of a stack. (Use diagrams.)",
           "Headland of resistant rock with joints; wave refraction concentrates energy on it. Hydraulic action and abrasion enlarge joints into caves; caves on both sides meet to form an arch; the arch is weakened by erosion below and weathering above until it collapses, leaving an isolated stack; further erosion leaves a stump."),
        PQ("Plan a fieldwork study to test whether longshore drift is moving material along a named beach.",
           "Hypothesis: pebble size decreases and roundness increases in the direction of drift. Method: sample 20 pebbles at five points along the beach; measure long axis and roundness; record wave approach angle; float test timed over a measured distance. Present: graphs of mean size against distance. Analyse: test the trend (for example Spearman rank). Safety: tide tables, avoid cliffs."),
        TIP("Coastal landforms are examined in Paper 1 and in the physical section of Paper 2. In Paper 3, coastal processes are one "
            "possible fieldwork topic; the Board's report noted that few candidates choose it and those who do often answer poorly, so "
            "a well-planned coastal study can stand out.", title="Exam link"),
        SUM("Wave size depends on wind speed, duration and fetch; energy rises with the square of height.",
            "Constructive waves build beaches (strong swash); destructive waves erode (strong backwash).",
            "Refraction concentrates energy on headlands; longshore drift moves sediment along the coast; tides set the range of attack.",
            "Erosion: notch, cliff, wave-cut platform, cave, arch, stack, stump. Deposition: beach, spit, bar, tombolo, marsh or mangrove.",
            "Fieldwork: beach profiles, pebble analysis, float tests, with careful safety planning."),
    ],
))

# ---------------------------------------------------------------------------
# Tectonic, Slope, Coastal & Arid Geomorphology / Coral reefs and sea-level change
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_GEO, topic="Coral reefs and sea-level change",
    title="Coral reefs and sea-level change: theories, landforms and threats",
    slug="gpl2-coral-reefs-sea-level-change",
    minutes=25,
    summary="Conditions for coral growth, fringing reefs, barrier reefs and atolls with the theories of Darwin, Daly and Murray, eustatic and isostatic sea-level change, the coastal landforms they leave, and present-day threats.",
    objectives=[
        "State and explain the conditions needed for coral reef growth",
        "Describe the three reef types and evaluate the theories of their formation",
        "Distinguish eustatic and isostatic change and explain landforms of emergence and submergence",
        "Assess the effects of present-day sea-level rise and warming on reefs and low-lying coasts",
    ],
    key_concepts=["Coral polyp", "Fringing reef", "Barrier reef", "Atoll", "Eustatic change", "Isostatic change", "Raised beach", "Ria"],
    blocks=[
        H("Introduction"),
        T("Cameroon has no large coral reefs, and that is itself a useful fact. Coral needs warm, clear, salty and sunlit water. The "
          "Gulf of Guinea coast receives large, muddy rivers, and parts of it have cooler upwelling water, so reefs are few. Compare "
          "the Red Sea or the Indian Ocean islands, where reefs line the coasts.\n\n"
          "This lesson also deals with sea-level change, because the history of reefs is a history of changing sea level, and because "
          "low-lying coasts such as Douala's face rising seas today."),
        D("A **coral reef** is a ridge or mound of limestone built by colonies of tiny animals, **coral polyps**, which take calcium "
          "carbonate from sea water to build skeletons. Algae (zooxanthellae) live inside the polyps and supply them with food by "
          "photosynthesis, which is why reef corals need light.", title="Coral reef"),
        KEY("Conditions for reef growth", "Textbook values differ slightly; check yours.", cards=[
            ["Temperature", "Warm water, generally not below about 18 degrees Celsius, with best growth in the low to high 20s. Hence reefs are mainly within the tropics, best developed on the east coasts of continents where warm currents flow, and scarce where cold currents flow."],
            ["Light and depth", "Clear, shallow water (usually less than about 50 m) so the algae can photosynthesise."],
            ["Clean, salty water", "Normal sea salinity and little sediment: river mouths with fresh, muddy water kill coral."],
            ["Base and water movement", "A firm, shallow platform to grow on, and wave action that brings oxygen and food; reefs grow fastest on the seaward side."],
        ]),
        H("Types of reef and how they form"),
        T("A **fringing reef** is attached to the shore or separated by a very shallow channel. A **barrier reef** lies some distance "
          "offshore, separated from the land by a wide, deeper lagoon (the Great Barrier Reef of Australia is the largest example). An "
          "**atoll** is a ring of reef enclosing a lagoon, with no central island, common in the Pacific and Indian Oceans (the "
          "Maldives)."),
        IMG("algpl2-coral-reefs.svg", alt="Three cross-sections: a volcanic island with a fringing reef at the shoreline; the island lower in the sea with a barrier reef separated by a lagoon; the island submerged with only a ring of reef around a lagoon forming an atoll",
            caption="Figure 1. Darwin's subsidence theory: fringing reef, barrier reef, atoll."),
        KEY("Three theories", "Each explains part of the evidence.", cards=[
            ["Darwin: subsidence (1842)", "A fringing reef forms around a volcanic island. The island slowly sinks; the reef grows upward and stays near the surface, becoming a barrier reef and then an atoll when the island disappears. Supported by deep drilling on atolls, which found reef limestone hundreds of metres thick over volcanic rock."],
            ["Daly: glacial control", "In the ice age, sea level was much lower and the cold water killed coral; waves planed off platforms. As the ice melted and the sea rose, coral grew up on the edges of these platforms."],
            ["Murray: antecedent platform", "Reefs grew on existing submarine platforms built up by sediment to a suitable depth; no subsidence is needed."],
        ]),
        H("Sea-level change"),
        D("A **eustatic** change is a worldwide change in sea level caused by a change in the volume of ocean water: water stored as ice "
          "in glacial periods lowers the sea; melting and warming (thermal expansion) raise it. An **isostatic** change is a local "
          "change in the level of the land: a heavy ice sheet pushes the crust down, and when the ice melts the land slowly rises again "
          "(isostatic rebound). Tectonic uplift and sediment loading also change land level.", title="Eustatic and isostatic change"),
        T("At the peak of the last glacial period, about 20 000 years ago, sea level was roughly 120 m lower than today (check the "
          "figure in your textbook). Rivers cut valleys down to the low sea level. As the ice melted, the sea rose and drowned them."),
        KEY("Landforms of changing sea level", "Ask: did the sea fall relative to the land, or rise?", cards=[
            ["Emergence (relative fall)", "Raised beaches and wave-cut platforms above the present shore, relic (abandoned) cliffs, marine terraces."],
            ["Submergence (relative rise)", "Rias (drowned river valleys), fjords (drowned glacial troughs), drowned estuaries and coasts with long inlets; barrier islands may migrate inland."],
        ]),
        T("Many broad tropical estuaries, including the Cameroon estuary at Douala, are commonly interpreted as river mouths drowned by "
          "the rise in sea level after the last glacial period; check your textbook's account."),
        H("Worked examples"),
        EX("Worked example 1: how far an ice sheet depresses the crust", intro="A simple isostatic estimate: depression = ice thickness x (ice density / mantle density). Find the depression under 1 000 m of ice, with ice density 0.9 and mantle density 3.3 (g per cubic cm).", steps=[
            S("Set up", math=r"d = 1000\times \frac{0.9}{3.3}"),
            S("Calculate", math=r"d \approx 273\text{ m}"),
            S("Meaning", text="When the ice melts, the land can rise by a similar amount over thousands of years, producing raised beaches far above the present sea."),
        ]),
        EX("Worked example 2: can the reef keep up?", intro="A reef grows upward at 5 mm per year while sea level rises at 4 mm per year (figures invented for practice). What happens over 100 years?", steps=[
            S("Reef growth", math=r"5\times 100 = 500\text{ mm} = 50\text{ cm}"),
            S("Sea-level rise", math=r"4\times 100 = 400\text{ mm} = 40\text{ cm}"),
            S("Compare", text="The reef gains 10 cm on the sea: it keeps pace. If warming or acidification slowed growth below 4 mm a year, the reef would drown slowly."),
        ]),
        EX("Worked example 3: essay plan", intro="Evaluate the theories that explain the formation of coral reefs.", steps=[
            S("Introduction", text="Define reef types; outline the conditions for coral."),
            S("Darwin", text="Explains the sequence fringing, barrier, atoll; supported by thick reef limestone over volcanic rock in drill holes; but some reefs show no subsidence."),
            S("Daly", text="Explains flat lagoon floors and the role of glacial sea-level change; but coral did survive in warm areas during glacials, and platforms are not all wave-cut."),
            S("Murray", text="Explains reefs on submarine banks; but cannot explain the great thickness of reef limestone found by drilling."),
            S("Conclusion", text="Subsidence explains most atolls; glacial sea-level changes shaped the detail; different reefs may need different explanations."),
        ]),
        H("Reefs and coasts today"),
        T("Sea level is rising by a few millimetres a year at present, through thermal expansion and the melting of glaciers and ice "
          "sheets. Warmer water causes **coral bleaching** (corals expel their algae and may die); more carbon dioxide in the ocean makes "
          "it more acidic and slows skeleton building; pollution, sediment and overfishing add stress. Low-lying coasts face flooding, "
          "erosion and salt water entering aquifers. In Cameroon, low-lying parts of Douala and the mangrove coasts are among the areas "
          "most exposed."),
        MISTAKE("Mixing up eustatic and isostatic", "Eustatic: the sea changes everywhere (volume of water). Isostatic: the land moves locally (loading or unloading of the crust). Link each to its cause."),
        MISTAKE("Listing coral conditions without explaining them", "Give the reason with each condition: light because of the algae, clear water because sediment smothers polyps and blocks light, salt water because fresh water kills polyps."),
        QUIZ("Why are coral reefs rare near the mouths of large rivers?",
             ["River water is too warm", "Fresh, sediment-laden water lowers salinity, blocks light and smothers polyps", "Rivers bring too much oxygen", "Tides are too small near rivers"], 1,
             "Coral needs clear, salty water; river water is fresh and muddy.",
             feedback=["River water is not too warm for coral.", "", "Oxygen helps coral; that is not the problem.", "Tidal range is not the reason."]),
        QUIZ("A beach and a wave-cut platform are found 10 m above present sea level. What do they show?",
             ["Submergence of the coast", "Emergence of the coast", "Present-day longshore drift", "A ria coast"], 1,
             "A relative fall in sea level (or rise of the land) has left old shoreline features above the present sea.",
             feedback=["Submergence would drown features below sea level.", "", "Longshore drift works at the present shoreline.", "A ria is a drowned valley, a feature of submergence."]),
        PQ("Sea level rises at 3.5 mm per year. How much will it rise in 40 years? Comment on one effect on a low-lying tropical coast.",
           r"3.5 x 40 = 140 mm, or 14 cm. Effects: more frequent flooding at high tides and in storms, erosion of beaches and mangroves, salt water reaching wells and farmland; impacts are greatest where land is also sinking."),
        PQ("Describe and explain the conditions required for the growth of coral reefs.",
           "Warm water (generally above about 18 degrees Celsius), because polyps and algae are tropical organisms; clear, shallow water so algae get light for photosynthesis; normal salinity; little sediment; a firm platform; wave action for oxygen and food. Explain each condition."),
        PQ("Distinguish between eustatic and isostatic changes in sea level and name one landform produced by each.",
           "Eustatic: global change in the volume of sea water (ice ages, melting, thermal expansion); post-glacial rise drowned river valleys as rias and estuaries. Isostatic: local rise or fall of the land (ice loading and rebound, tectonics); rebound after ice melt left raised beaches above the present shore."),
        TIP("Coral reefs and sea-level change belong to geomorphology in Paper 1 and the physical section of Paper 2. Be ready to draw "
            "the three reef stages and to evaluate more than one theory; questions on rising sea level also link to the environmental "
            "issues section.", title="Exam link"),
        SUM("Coral needs warm, clear, shallow, salty, sediment-free water and a firm base; algae in the polyps need light.",
            "Fringing reef, barrier reef and atoll; Darwin (subsidence), Daly (glacial control), Murray (antecedent platform).",
            "Eustatic change alters the volume of the ocean; isostatic change moves the land.",
            "Emergence leaves raised beaches and relic cliffs; submergence produces rias, fjords and drowned estuaries.",
            "Warming, acidification and sea-level rise threaten reefs and low-lying coasts today."),
    ],
))

# ---------------------------------------------------------------------------
# Tectonic, Slope, Coastal & Arid Geomorphology / Landforms of hot deserts
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_GEO, topic="Landforms of hot deserts",
    title="Landforms of hot deserts: the work of wind and water",
    slug="gpl2-hot-desert-landforms",
    minutes=25,
    summary="Aeolian erosion, transport and deposition, dunes and wind-eroded landforms, the fluvial landforms of flash floods (wadis, fans, bajadas, playas, pediments, inselbergs) and the debate on wind versus water.",
    objectives=[
        "Explain the processes of wind erosion, transport and deposition",
        "Explain the formation of aeolian landforms, including barchan and seif dunes",
        "Explain the formation of fluvial desert landforms produced by episodic floods",
        "Evaluate the relative importance of wind and water, present and past, in shaping hot deserts",
    ],
    key_concepts=["Aeolian processes", "Deflation", "Abrasion", "Saltation", "Barchan", "Seif dune", "Pediment", "Pluvial period"],
    blocks=[
        H("Introduction"),
        T("North of Cameroon's Far North Region lies the Sahara, the largest hot desert on Earth. Most people imagine it as endless sand "
          "dunes, but sand seas cover only part of it; much more is bare rock, gravel plains and mountains cut by dry valleys. Rain is "
          "rare, but when it comes it falls in violent storms that do a great deal of work in a few hours.\n\n"
          "Hot deserts are areas with very low and unreliable rainfall (often under about 250 mm a year) and high evaporation. Their "
          "landforms come from two agents: wind and occasional running water."),
        D("**Aeolian** processes are those caused by wind. Wind can move only fine material, so it works best where the ground is dry, "
          "loose and bare of vegetation, conditions found in hot deserts.", title="Aeolian processes"),
        H("Wind erosion and transport"),
        KEY("Processes", "Wind erodes in two ways and transports in three.", cards=[
            ["Deflation", "Wind lifts and removes loose, fine particles, lowering the surface and leaving coarser stones behind."],
            ["Abrasion", "Wind-blown sand blasts rock surfaces, smoothing and undercutting them. It is strongest within about a metre or two of the ground, where most sand moves."],
            ["Transport", "Suspension: fine dust carried high, sometimes across oceans. Saltation: sand grains bounce in low arcs, the main mode of sand transport (studied by R. A. Bagnold). Surface creep: larger grains pushed along by impacts of saltating grains."],
        ]),
        T("Wind-eroded landforms: **deflation hollows** (basins scoured out by wind, sometimes down to the water table to form oases); "
          "**desert pavement or reg** (a surface of closely fitted stones left after fines are blown away); **ventifacts** (stones with "
          "faces cut by sand blasting); **yardangs** (streamlined ridges of soft rock parallel to the wind); **zeugen** (tabular ridges "
          "where a hard cap protects softer rock beneath, cut by abrasion along joints); and **rock pedestals** undercut at the base, "
          "where abrasion is strongest."),
        H("Wind deposition: dunes"),
        T("Sand accumulates in **ergs** (sand seas). The shape of dunes depends on sand supply, wind direction and vegetation. A "
          "**barchan** is a crescent dune with its horns pointing downwind. It forms where winds blow mostly from one direction and sand "
          "is limited; sand blows up the gentle windward slope and slips down the steep slip face, so the dune migrates downwind. A "
          "**seif** (linear) dune is a long ridge formed where winds blow from two main directions, which pile sand into a line between "
          "them."),
        H("The work of water in deserts"),
        IMG("algpl2-desert.svg", alt="Cross-section of a desert landscape: a steep mountain front, a gently sloping rock pediment at its foot, alluvial fans joining into a bajada, a flat salt-crusted playa, and a steep-sided inselberg rising from the plain",
            caption="Figure 1. Landforms from a mountain front to a desert basin (schematic, not to scale)."),
        T("Desert rain falls in short, intense storms on bare ground, so infiltration is low and **flash floods** carry huge loads. "
          "Rivers flow in steep-sided, flat-floored **wadis** that are dry most of the time. Where a wadi leaves the mountains, the flow "
          "spreads and loses energy, depositing an **alluvial fan**; fans join into a continuous apron called a **bajada**. Water that "
          "reaches the basin floor forms a temporary lake that evaporates to leave a flat, salt-crusted **playa**."),
        T("A **pediment** is a gently sloping rock surface at the foot of a mountain front, often with a thin cover of debris, meeting the "
          "steep front at a sharp angle. It may be cut by sheetfloods and by the retreat of the mountain front (King's parallel retreat). "
          "**Inselbergs** are steep isolated hills left as the front retreats, or exposed after deep weathering in an earlier wetter "
          "climate. **Mesas** (flat-topped tablelands) and **buttes** (smaller remnants) form where horizontal hard caps protect softer "
          "rock."),
        H("Wind or water?"),
        T("Early writers thought wind made most desert landforms. Most geomorphologists now think water is more important for erosion, "
          "even though rain is rare: flash floods move vast amounts of material, and many landforms (wadis, fans, pediments) are clearly "
          "fluvial. Many features are also relics of **pluvial periods**, wetter phases in the past when rivers and lakes were much "
          "larger; Lake Chad, for example, was far bigger several thousand years ago (check your textbook for the evidence). Wind "
          "dominates the transport of sand and the shaping of dunes and is locally important for erosion."),
        H("Worked examples"),
        EX("Worked example 1: dune migration", intro="A barchan migrates 15 m a year towards a road 300 m away (figures invented for practice). How long before it reaches the road?", steps=[
            S("Time = distance / rate", math=r"t = \frac{300}{15}"),
            S("Calculate", math=r"t = 20\text{ years}"),
            S("Management", text="Fences, planting of drought-tolerant vegetation or spraying to stabilise sand can slow migration; smaller dunes move faster than large ones."),
        ]),
        EX("Worked example 2: explaining a barchan", intro="Explain the formation and shape of a barchan dune.", steps=[
            S("Conditions", text="A steady wind from one direction, limited sand on a firm surface, and an obstacle or patch where sand first collects."),
            S("Profile", text="Saltating grains move up the gentle windward slope; at the crest they fall into the sheltered lee and avalanche down a steep slip face (about 30 to 34 degrees, the angle of rest of dry sand)."),
            S("Plan shape", text="The lower edges carry less sand and move faster than the centre, so they run ahead as horns pointing downwind."),
        ]),
        EX("Worked example 3: essay plan", intro="'Water, not wind, is the main agent shaping landforms in hot deserts.' Discuss.", steps=[
            S("Introduction", text="Define hot deserts; state the two agents and that rainfall is rare but intense."),
            S("Water", text="Flash floods, wadis, alluvial fans, bajadas, playas, pediments; many landforms inherited from pluvial periods."),
            S("Wind", text="Deflation hollows, reg, ventifacts, yardangs, zeugen; all dune forms; dust transport over great distances."),
            S("Evaluation", text="Water does most erosion and shapes the large landforms; wind dominates sand transport and deposition; relative importance varies between deserts and over time."),
            S("Conclusion", text="Agree for erosional landforms, with the qualification that many are relics of wetter periods and dunes are purely aeolian."),
        ]),
        MISTAKE("Confusing hot deserts with desertification", "A hot desert is a natural, very dry environment. Desertification is land degradation in drylands (often semi-arid areas such as the Sahel) caused by climate variations and human activities. Do not use the two terms as synonyms."),
        MISTAKE("Describing wind as the agent for every desert landform", "Wadis, fans, bajadas and playas are made by water. Name the agent and the process for each landform."),
        QUIZ("Which landform forms where alluvial fans at the foot of a mountain front merge?",
             ["Playa", "Bajada", "Yardang", "Barchan"], 1,
             "A bajada is a continuous apron of coalescing fans.",
             feedback=["A playa is the flat basin floor where flood water evaporates.", "", "A yardang is a wind-eroded ridge.", "A barchan is a crescent dune."]),
        QUIZ("Long linear dunes form between two dominant wind directions. What are they called?",
             ["Barchans", "Seif dunes", "Zeugen", "Ventifacts"], 1,
             "Seif (linear) dunes extend parallel to the resultant of two wind directions.",
             feedback=["Barchans need one dominant wind direction.", "", "Zeugen are erosional ridges of rock.", "Ventifacts are wind-cut stones."]),
        PQ("A barchan moves 25 m a year. How long will it take to cover 1 km? Name two ways of slowing it.",
           "1 km = 1 000 m; time = 1 000 / 25 = 40 years. Slow it by sand fences that trap sand upwind, planting drought-tolerant vegetation, or covering the windward slope (mulch, gravel) to stop saltation."),
        PQ("Explain the formation of zeugen and yardangs.",
           "Both are made by wind abrasion (sand blasting) in areas of strong, steady winds. Zeugen: horizontal bands of hard rock over soft rock; abrasion attacks joints in the hard cap and then cuts down into the soft rock, leaving tabular ridges. Yardangs: vertical or steep bands of hard and soft rock parallel to the wind; soft bands are scoured out, leaving streamlined ridges with blunt upwind ends."),
        PQ("Describe and explain the landforms found between a desert mountain front and the centre of a basin. (Use a diagram.)",
           "Draw Figure 1. Mountain front with wadis; pediment: gently sloping rock surface cut by sheetfloods and retreat of the front; alluvial fans where flash floods lose energy at the mountain foot, merging into a bajada; playa where flood water collects and evaporates leaving salts; isolated inselbergs or buttes left by retreat of the front."),
        TIP("Desert landforms belong to geomorphology in Paper 1 and the physical section of Paper 2. Questions on drought and "
            "desertification belong to the environmental issues section of Paper 2, where the Board has noted that many candidates "
            "failed to separate the two ideas; this lesson's landforms give you the physical background.", title="Exam link"),
        SUM("Hot deserts are very dry; wind and rare but violent flash floods shape them.",
            "Wind erodes by deflation and abrasion and transports by suspension, saltation and surface creep.",
            "Aeolian landforms: deflation hollows, reg, ventifacts, yardangs, zeugen; barchans (one wind) and seifs (two winds).",
            "Fluvial landforms: wadis, alluvial fans, bajadas, playas, pediments, inselbergs, mesas and buttes.",
            "Water does most erosion and many landforms are relics of pluvial periods; wind dominates sand transport."),
    ],
))
