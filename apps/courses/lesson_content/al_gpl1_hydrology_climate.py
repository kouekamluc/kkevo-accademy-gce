"""A Level Geography (0750), Lower Sixth: Hydrology & Fluvial Geomorphology, and Meteorology & Climatology.
13 lessons (two for "Fluvial erosion, transport and deposition": processes, then the Hjulstrom curve), one practice
set each (see the practice file of the same name).

Scope notes: the outline comes from KKEVO's master curriculum blueprint, not a Board syllabus booklet. Facts are the
standard A Level ones; where textbooks differ the lesson says "check your textbook". Numbers in worked data are teaching
data and are labelled. Exam comments paraphrase the GCE Board's 2023 Advanced Level subject report.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "lower-sixth")

M1 = "Hydrology & Fluvial Geomorphology"
M2 = "Meteorology & Climatology"

LESSONS = []

# ------------------------------------------------------------------ 1. Hydrological cycle and drainage basin system
LESSONS.append(lesson(
    module=M1,
    topic="The hydrological cycle and the drainage basin system",
    title="The hydrological cycle and the drainage basin as an open system",
    slug="gpl1-hydrological-cycle-drainage-basin",
    minutes=24,
    summary="The global hydrological cycle is a closed system; a drainage basin is an open system of inputs, stores, flows and outputs. Learn every store and flow, the factors that control them and the water balance equation.",
    objectives=[
        "Describe the global hydrological cycle as a closed system with stores, fluxes and residence times",
        "Explain the drainage basin as an open system of inputs, stores, transfers and outputs",
        "Explain how vegetation, soil, rock and rainfall control interception, infiltration and overland flow",
        "Use the water balance equation P = Q + E + change in storage",
    ],
    key_concepts=["Closed and open systems", "Interception", "Infiltration capacity", "Throughflow", "Percolation", "Baseflow",
                  "Hortonian and saturated overland flow", "Water balance"],
    blocks=[
        H("Introduction"),
        T("When a heavy afternoon storm falls on the forest near Ebolowa, much of the rain never reaches a river quickly. Leaves "
          "catch some of it, the deep forest soil soaks up more, and the rest seeps slowly through the ground for days. When the "
          "same storm falls on a bare, compacted yard in a town, water runs off almost at once. A geographer explains the "
          "difference with a **systems** approach: stores of water joined by flows."),
        D("A **system** is a set of stores (where something is held) linked by flows (transfers). In a **closed system** energy "
          "enters and leaves but matter does not. In an **open system** both energy and matter cross the boundary.",
          title="Systems"),
        H("The global hydrological cycle: a closed system"),
        T("For the whole Earth, the amount of water is effectively fixed, so the **global hydrological cycle** is a closed "
          "system. Water moves between the oceans, the atmosphere and the land, driven by solar energy (which evaporates water) "
          "and gravity (which brings it down as precipitation and makes it flow downhill)."),
        KEY("Global stores", "Approximate shares of the Earth's water (figures differ slightly between textbooks).", cards=[
            ["Oceans", "About 97% of all water. Salty, so not directly usable."],
            ["Ice sheets and glaciers", "Most of the fresh water (roughly two thirds of it), mainly in Antarctica and Greenland."],
            ["Groundwater", "Most of the rest of the fresh water, in permeable rocks called aquifers."],
            ["Rivers, lakes, soil, atmosphere", "A tiny fraction of the total, but the part that cycles fastest."],
        ]),
        D("The **residence time** is the average time a water molecule stays in a store. It is about nine to ten days in the "
          "atmosphere, weeks in rivers, and thousands of years in deep groundwater or ice sheets.", title="Residence time"),
        H("The drainage basin: an open system"),
        D("A **drainage basin** is the area drained by a river and its tributaries. Its edge is the **watershed**. Water enters "
          "as precipitation and leaves as evapotranspiration, river discharge and, sometimes, deep groundwater flow, so the "
          "basin is an **open system**.", title="Drainage basin"),
        IMG("algpl1-basin-system.svg", alt="Systems diagram: precipitation passes through interception, surface, soil moisture and groundwater stores; overland flow, throughflow and baseflow feed the channel store and river discharge; evaporation and transpiration are outputs",
            caption="Figure 1. The drainage basin as an open system."),
        KEY("Stores and transfers", "Learn each term with a precise definition: the Board's report warns that bald one-word answers earn little.", cards=[
            ["Interception", "Precipitation caught by vegetation before it reaches the ground. Some evaporates from the leaves (interception loss); the rest drips off (throughfall) or runs down stems (stemflow)."],
            ["Infiltration", "The downward movement of water from the surface into the soil. The maximum rate the soil can absorb is the infiltration capacity (mm per hour)."],
            ["Throughflow", "Lateral (sideways) flow of water through the soil towards the river, often along root channels and soil pipes."],
            ["Percolation", "The downward movement of water from the soil into the underlying rock, to the groundwater store."],
            ["Groundwater flow and baseflow", "Slow movement of water through rock. The part that feeds the river is baseflow, which keeps rivers flowing in the dry season."],
            ["Overland flow", "Water flowing over the ground surface. It is the fastest route to the channel."],
        ]),
        H("Two kinds of overland flow"),
        T("**Infiltration-excess (Hortonian) overland flow** happens when rainfall intensity is greater than the infiltration "
          "capacity, for example on compacted laterite paths, tarred roads or crusted bare soil. It is named after the American "
          "hydrologist R. E. Horton. "
          "**Saturation-excess overland flow** happens when the soil is already full of water, so even gentle rain cannot "
          "infiltrate. It is common at the foot of slopes and in valley bottoms near the river late in the rainy season."),
        EX("Worked example 1: explaining an interception rate", intro="Explain how the form and intensity of precipitation affect the interception rate in a tropical forest.", steps=[
            S("Define", text="Interception is the precipitation caught and held by the vegetation canopy before it reaches the ground."),
            S("Intensity", text="In a short, light shower a dense canopy can hold most of the rain, so the interception rate is high. In a long, intense storm the leaves are soon full (the storage capacity is reached), so most rain becomes throughfall and the interception rate falls."),
            S("Form", text="Fine drizzle wets every leaf and is held; large raindrops in a convective storm hit hard and splash through. Hail bounces off."),
            S("Link back", text="So interception is highest, as a percentage, for light, gentle rain and lowest for intense, long storms."),
        ]),
        MISTAKE("Answering a different question", "The Board's 2023 report notes that, asked how rainfall affects interception, many candidates wrote about relief and soil, which control infiltration. Answer about the factor named in the question."),
        H("The water balance"),
        F(r"P = Q + E \pm \Delta S", title="Water balance equation"),
        T("P is precipitation, Q is runoff (river discharge), E is evapotranspiration and $\\Delta S$ is the change in storage (soil "
          "moisture and groundwater). All are usually given in mm over the basin for one year. In the wet season storage rises "
          "(recharge); in the dry season stored water is used and storage falls (utilisation)."),
        EX("Worked example 2: water balance", intro="In one year a basin receives 1 800 mm of precipitation. Runoff is 700 mm and storage rises by 50 mm. Find evapotranspiration and the runoff coefficient. (Teaching data.)", steps=[
            S("Rearrange", math=r"E = P - Q - \Delta S"),
            S("Substitute", math=r"E = 1800 - 700 - 50 = 1050 \text{ mm}"),
            S("Runoff coefficient", math=r"\frac{Q}{P} = \frac{700}{1800} = 0.389 \approx 39\%"),
            S("Interpret", text="About 39% of the rain leaves as river flow; most of the rest is evaporated or transpired, as expected in a hot, vegetated basin."),
        ], check=r"700 + 1050 + 50 = 1800"),
        EX("Worked example 3: from depth to volume", intro="The basin above has an area of 250 square kilometres. Convert the 700 mm of runoff into a volume and a mean discharge.", steps=[
            S("Change units", text="700 mm = 0.7 m and 250 km squared = 250 000 000 square metres."),
            S("Volume", math=r"0.7 \times 250\,000\,000 = 175\,000\,000 \text{ m}^3"),
            S("Mean discharge", math=r"\frac{175\,000\,000}{365 \times 24 \times 3600} \approx 5.55 \text{ m}^3/\text{s}"),
        ]),
        T("**Human impacts.** Deforestation removes the interception store and exposes soil to compaction, so overland flow rises. Urban surfaces "
          "are impermeable and drains speed water to rivers. Wells and boreholes lower groundwater; dams create new surface "
          "stores and increase evaporation. Each change alters how fast and how much water reaches the channel."),
        QUIZ("Which transfer is the slowest route by which rain reaches a river?",
             ["Overland flow", "Throughflow", "Groundwater flow (baseflow)", "Channel precipitation"], 2,
             "Groundwater moves very slowly through rock pores and joints, taking weeks to years.",
             hint="Think about how far below the surface the water travels.",
             feedback=["Overland flow over the surface is the fastest route.", "Throughflow in the soil is faster than flow through rock.", "", "Rain falling straight onto the channel arrives at once."]),
        QUIZ("Rain falls at 30 mm per hour on a soil with an infiltration capacity of 12 mm per hour. What happens?",
             ["All the rain infiltrates", "Infiltration-excess overland flow begins", "Saturation-excess overland flow begins", "Percolation stops"], 1,
             "Rainfall intensity is greater than the infiltration capacity, so the excess runs over the surface: Hortonian flow.",
             hint="Compare the rain rate with what the soil can absorb.",
             feedback=["The soil can only take 12 mm per hour.", "", "Saturation-excess flow needs a soil that is already full, which the question does not state.", "Percolation continues from the soil below."]),
        H("Practice"),
        PQ("Distinguish between throughflow and percolation.", "Both are movements of water below the surface. Throughflow is the lateral flow of water through the soil towards the river channel. Percolation is the vertical movement of water from the soil down into the rock, recharging the groundwater store."),
        PQ("A basin receives 2 000 mm of precipitation in a year. Evapotranspiration is 1 200 mm and storage falls by 100 mm. Calculate the runoff.", "Q = P - E - change in storage = 2 000 - 1 200 - (-100) = 900 mm. A fall in storage adds to runoff, because stored water is released to the river."),
        PQ("Explain why the global hydrological cycle is a closed system but a drainage basin is an open system.", "Globally, water is neither gained nor lost; only energy (solar radiation in, heat out) crosses the boundary, so it is closed. A drainage basin gains water as precipitation and loses it as evapotranspiration, river discharge and groundwater outflow across its boundary, so matter crosses it: it is open."),
        PQ("Essay plan: 'Examine the influence of vegetation on the drainage basin hydrological cycle.'", "Introduction: define the basin system and the vegetation store. Point 1: interception and interception loss reduce the water reaching the ground. Point 2: stemflow and throughfall delay arrival. Point 3: roots and leaf litter raise infiltration capacity and throughflow, reducing overland flow. Point 4: transpiration is a major output in tropical forest. Point 5: effects of removal (deforestation, farming) with an example. Evaluation: the effect depends on vegetation type, season and storm intensity; in very long storms the canopy saturates and its effect falls. Conclusion."),
        TIP("Exam link: the drainage basin system appears in Paper 1 (the physical section includes questions on meteorology, climatology and hydrology), in Paper 2 Section A essays, and in Paper 3 fieldwork, where stream channel studies are a popular choice. Define terms fully and use a labelled systems diagram."),
        SUM("The global hydrological cycle is a closed system; a drainage basin is an open system.",
            "Stores: interception, surface, soil moisture, groundwater, channel. Transfers: throughfall, stemflow, infiltration, throughflow, percolation, groundwater flow, overland flow.",
            "Overland flow is infiltration-excess (rain faster than infiltration capacity) or saturation-excess (soil already full).",
            "Water balance: P = Q + E plus or minus the change in storage.",
            "Vegetation, soil, rock and human land use control how fast and how much water reaches the river."),
    ],
))

# ------------------------------------------------------------------ 2. Storm hydrographs and river regimes
LESSONS.append(lesson(
    module=M1,
    topic="Storm hydrographs and river regimes",
    title="Storm hydrographs, the factors that shape them, and river regimes",
    slug="gpl1-storm-hydrographs-regimes",
    minutes=25,
    summary="A storm hydrograph shows how a river's discharge responds to one storm. Read lag time and peak discharge, explain flashy and subdued hydrographs, and describe simple and complex river regimes.",
    objectives=[
        "Calculate discharge from cross-sectional area and velocity",
        "Label a storm hydrograph and measure lag time, rise time and peak discharge",
        "Explain how basin, rainfall and human factors produce flashy or subdued hydrographs",
        "Describe and explain simple and complex river regimes",
    ],
    key_concepts=["Discharge", "Storm hydrograph", "Lag time", "Peak discharge", "Baseflow and stormflow",
                  "Flashy and subdued hydrographs", "Antecedent moisture", "River regime"],
    blocks=[
        H("Introduction"),
        T("After a heavy evening storm, a small stream in a Douala neighbourhood can rise and flood streets within an hour, then "
          "fall again by morning. A large river such as the Sanaga rises slowly and stays high for weeks. Hydrologists explain "
          "this with two tools: the **storm hydrograph** for a single storm and the **river regime** for the year."),
        D("**Discharge** (Q) is the volume of water passing a point in a river per second, measured in cubic metres per second "
          "(cumecs).", title="Discharge", formula=r"Q = A \times v"),
        T("A is the cross-sectional area of the water (width times mean depth, in square metres) and v is the mean velocity "
          "(metres per second)."),
        EX("Worked example 1: discharge", intro="A channel is 12 m wide with a mean depth of 1.5 m. A float shows a mean velocity of 0.8 m/s. Find the discharge.", steps=[
            S("Area", math=r"A = 12 \times 1.5 = 18 \text{ m}^2"),
            S("Discharge", math=r"Q = 18 \times 0.8 = 14.4 \text{ m}^3/\text{s}"),
        ]),
        TIP("Fieldwork link: a float measures surface velocity, which is faster than the mean velocity because the bed slows the water. Many textbooks multiply by a correction factor of about 0.8; check your textbook and say which method you used."),
        H("Reading a storm hydrograph"),
        IMG("algpl1-hydrograph.svg", alt="Storm hydrograph: rainfall bars at the top peak between 6 and 8 hours; discharge rises from 6 hours to a peak of about 43 cumecs at 18 hours then falls; lag time arrow from 7 to 18 hours; baseflow dashed beneath",
            caption="Figure 1. A storm hydrograph (teaching data)."),
        KEY("Parts of the hydrograph", "Use these terms when you describe one.", cards=[
            ["Rising limb", "Discharge increasing as storm water arrives. Its steepness shows how quickly the basin responds."],
            ["Peak discharge", "The highest discharge reached after the storm."],
            ["Lag time", "The time between peak rainfall and peak discharge."],
            ["Falling (recession) limb", "Discharge decreasing as storm water drains away. Usually gentler than the rising limb, because throughflow keeps arriving."],
            ["Baseflow and stormflow", "Baseflow is the slow groundwater contribution. Stormflow (quickflow) is the extra water from overland flow and fast throughflow."],
        ]),
        EX("Worked example 2: reading Figure 1", intro="Use Figure 1 to find the lag time, the rise time and the total rainfall.", steps=[
            S("Peak rainfall", text="The tallest bar (26 mm) falls between 6 and 8 hours; take its midpoint, 7 hours."),
            S("Peak discharge", text="The curve peaks at 18 hours."),
            S("Lag time", math=r"18 - 7 = 11 \text{ hours}"),
            S("Rise time", text="Discharge starts to rise at 6 hours, so the rise time is 18 - 6 = 12 hours."),
            S("Total rainfall", math=r"4 + 10 + 18 + 26 + 12 + 4 = 74 \text{ mm}"),
        ]),
        H("Flashy and subdued hydrographs"),
        T("A **flashy** hydrograph has a short lag time, a steep rising limb and a high peak: flood risk is high. A **subdued** "
          "hydrograph has a long lag time, gentle limbs and a low peak. The shape depends on how quickly water reaches the channel."),
        CODE("""Factor               Flashy (short lag)              Subdued (long lag)
Basin shape          circular: water arrives together elongated: arrival spread out
Basin size           small                           large
Slopes               steep                           gentle
Drainage density     high (many channels)            low
Rock                 impermeable (granite, clay)     permeable (sandstone, limestone)
Soil                 thin, compacted, clay           deep, sandy, well drained
Vegetation           bare or cleared                 dense forest (interception)
Antecedent moisture  soil already wet                soil dry, can absorb rain
Rain                 intense, short, convectional    light, steady
Land use             urban, drained, deforested      forested, terraced farmland""", "text", title="Table 1. Factors affecting hydrograph shape"),
        D("**Antecedent moisture** is the water already in the basin before a storm. Late in the rainy season soils are wet, so "
          "the same storm produces a much higher, quicker peak than early in the season.", title="Antecedent conditions"),
        EX("Worked example 3: explaining urban hydrographs", intro="Explain why urbanisation makes hydrographs more flashy.", steps=[
            S("Surfaces", text="Roofs, roads and concrete are impermeable, so infiltration falls and infiltration-excess overland flow rises."),
            S("Drains", text="Gutters and storm drains carry water straight to the river, shortening lag time."),
            S("Vegetation", text="Clearing removes interception and transpiration."),
            S("Channels", text="Straightened or lined channels speed water downstream; but rubbish blocking drains can cause local flooding."),
            S("Result", text="Shorter lag time, higher peak, steeper limbs."),
        ]),
        H("River regimes"),
        D("A **river regime** is the pattern of discharge over a year. A **simple regime** has one high-water and one low-water "
          "season, controlled by one main source (for example one rainy season). A **complex regime** has several peaks, "
          "because the river is fed by several sources or crosses several climate zones.", title="River regime"),
        T("In Cameroon, rivers draining the north (for example tributaries of the Benue and Logone) depend on a single rainy "
          "season, so they tend to show a simple regime, with very low flow in the long dry season. Rivers draining the southern "
          "plateau, where there are two rainy seasons, can show two high-water periods, though large basins and storage smooth "
          "them out. Check the exact months for named rivers in your textbook or atlas."),
        T("Regimes are also changed by people: dams store wet-season water and release it in the dry season, so downstream "
          "flow becomes more even. The dams on the Sanaga system are used in this way to support hydro-electric power."),
        MISTAKE("Measuring lag time from the start of the rain", "Lag time runs from peak rainfall to peak discharge. The time from the start of the rise to the peak is the rise time."),
        MISTAKE("Listing factors without explaining", "Say how each factor changes the route or speed of water: for example, 'clay is impermeable, so infiltration is low and overland flow carries water quickly to the channel'."),
        QUIZ("Which basin would give the shortest lag time?",
             ["Large, elongated, forested, on sandstone", "Small, circular, steep, on granite", "Large, circular, gentle slopes, deep sandy soil", "Small, elongated, terraced farmland"], 1,
             "Small size, circular shape, steep slopes and impermeable rock all speed water to the channel.",
             hint="Look for the answer where every factor speeds water up.",
             feedback=["Every factor here slows the response.", "", "Deep sandy soils and gentle slopes slow the response despite the circular shape.", "Terraces slow water, and elongated shape spreads arrival."]),
        QUIZ("Two identical storms hit the same basin, one in April and one in September near the end of a long rainy season. Why is the September peak higher?",
             ["The rain is more acidic", "The soils are already saturated, so more rain becomes overland flow", "Evaporation is higher in September", "The vegetation intercepts more rain"], 1,
             "High antecedent moisture means little infiltration, so runoff is faster and greater.",
             hint="What has happened to the soil after months of rain?",
             feedback=["Acidity does not change runoff speed.", "", "Higher evaporation would reduce runoff, not raise it.", "More interception would lower the peak."]),
        H("Practice"),
        PQ("A storm's peak rainfall is at 14:00 and the river's peak discharge is at 05:00 the next day. Calculate the lag time.", "From 14:00 to midnight is 10 hours; from midnight to 05:00 is 5 hours. Lag time = 15 hours."),
        PQ("Distinguish between baseflow and stormflow.", "Baseflow is the slow contribution of groundwater (and deep throughflow) to the river; it continues between storms and keeps the river flowing in the dry season. Stormflow (quickflow) is the extra discharge from overland flow and fast throughflow after rain; it forms the peak of the hydrograph."),
        PQ("Explain two ways in which deforestation can change a storm hydrograph.", "1. Interception is removed, so more rain reaches the ground at once, raising the peak and shortening lag time. 2. Bare soil is compacted and crusted by raindrop impact, so infiltration capacity falls and infiltration-excess overland flow increases, giving a steeper rising limb."),
        PQ("Essay plan: 'Assess the relative importance of physical and human factors in determining the shape of a storm hydrograph.'", "Introduction: define the hydrograph and lag time. Physical factors: basin size and shape, slope, rock, soil, drainage density, antecedent moisture, rainfall intensity, with a reason for each. Human factors: urbanisation, deforestation, drainage, dams, farming practices. Evaluation: physical factors set the basic shape; human factors modify it and can dominate in small urban basins; storm intensity and antecedent moisture can override everything in extreme events. Conclusion with a judgement."),
        TIP("Exam link: hydrographs are common in Paper 1 (reading lag time or choosing the basin that floods first), in Paper 2 essays on flooding and hydrology, and in Paper 3 data or fieldwork questions on discharge. Always quote values with units read from the graph."),
        SUM("Discharge Q = cross-sectional area times mean velocity, in cumecs.",
            "Lag time is from peak rainfall to peak discharge; rise time is from the start of the rise to the peak.",
            "Flashy hydrographs come from small, steep, impermeable, saturated, urban or cleared basins.",
            "A river regime is the yearly pattern of discharge: simple (one peak) or complex (several).",
            "Dams and land-use change alter both hydrographs and regimes."),
    ],
))

# ------------------------------------------------------------------ 3. Fluvial processes
LESSONS.append(lesson(
    module=M1,
    topic="Fluvial erosion, transport and deposition",
    title="River energy, erosion, transport and deposition",
    slug="gpl1-fluvial-processes",
    minutes=24,
    summary="A river's energy decides whether it erodes, transports or deposits. Learn the erosion and transport processes, competence and capacity, hydraulic radius and channel efficiency, and how these change downstream.",
    objectives=[
        "Explain how a river's energy is used and what controls it",
        "Describe the four erosion processes and the four transport processes",
        "Calculate hydraulic radius and use it to compare channel efficiency",
        "Explain the causes of deposition and the downstream changes in the Bradshaw model",
    ],
    key_concepts=["Potential and kinetic energy", "Hydraulic action", "Abrasion", "Attrition", "Solution (corrosion)",
                  "Traction, saltation, suspension, solution", "Competence and capacity", "Hydraulic radius", "Bradshaw model"],
    blocks=[
        H("Introduction"),
        T("In the dry season the Mungo river looks calm and clear. After heavy rain the same river turns brown, carries "
          "branches and rolls stones that knock together. Nothing has changed except the river's **energy**. Whether a river "
          "erodes, carries or drops material depends on how much energy is left after it has overcome friction."),
        H("Where a river's energy goes"),
        T("Water high in a basin has **potential energy**. As it flows downhill this becomes **kinetic energy**. Most of it "
          "(often quoted as about 95%) is used overcoming friction with the bed, banks and air, and in turbulence. Only the "
          "small remainder is available to erode and transport load. Energy rises with discharge and gradient, and falls with "
          "friction."),
        D("**Hydraulic radius** is the cross-sectional area of the water divided by the **wetted perimeter** (the length of bed "
          "and banks in contact with the water). A larger hydraulic radius means less of the water is in contact with the "
          "channel, so less energy is lost to friction: the channel is more **efficient**.", title="Hydraulic radius",
          formula=r"R = \frac{\text{cross-sectional area}}{\text{wetted perimeter}}"),
        EX("Worked example 1: comparing efficiency", intro="Channel A is 10 m wide and 2 m deep. Channel B is 20 m wide and 1 m deep. Both are rectangular. Which is more efficient?", steps=[
            S("Channel A", math=r"R = \frac{10 \times 2}{10 + 2 + 2} = \frac{20}{14} = 1.43 \text{ m}"),
            S("Channel B", math=r"R = \frac{20 \times 1}{20 + 1 + 1} = \frac{20}{22} = 0.91 \text{ m}"),
            S("Conclude", text="Both have the same area, but A has the larger hydraulic radius, so less friction per unit of water: A is more efficient and, other things equal, flows faster."),
        ]),
        TIP("Do not count the water surface in the wetted perimeter: only the bed and the two banks are wetted."),
        H("Erosion processes"),
        KEY("Four processes of fluvial erosion", "Learn the name and the mechanism.", cards=[
            ["Hydraulic action", "The force of moving water on the bed and banks. Air trapped in cracks is compressed and released, loosening rock. In very fast flow, collapsing bubbles (cavitation) add shock waves."],
            ["Abrasion (corrasion)", "Load carried by the river scrapes and grinds the bed and banks, like sandpaper. Swirling pebbles drill potholes. Usually the most effective process."],
            ["Attrition", "Particles of load knock against each other, becoming smaller and more rounded downstream. It wears the load, not the channel."],
            ["Solution (corrosion)", "Chemical dissolving of rock by river water, most effective on limestone and other soluble rocks."],
        ]),
        T("Rivers erode downward (**vertical erosion**), sideways (**lateral erosion**) and backward towards the source "
          "(**headward erosion**). Vertical erosion dominates where the river is high above base level; lateral erosion becomes "
          "more important downstream."),
        H("Transport processes"),
        KEY("How load is carried", "From largest to smallest particles.", cards=[
            ["Traction", "Large boulders and pebbles roll or slide along the bed, mostly in floods."],
            ["Saltation", "Smaller pebbles and sand bounce along the bed in a series of hops."],
            ["Suspension", "Fine silt and clay carried within the flow, making the water brown. Usually the largest part of the load."],
            ["Solution", "Dissolved minerals carried invisibly."],
        ]),
        D("**Competence** is the size of the largest particle a river can carry at a given velocity. **Capacity** is the total "
          "amount (volume or mass) of load it can carry. Both increase sharply with velocity and discharge, so most transport "
          "happens during a few floods each year.", title="Competence and capacity"),
        H("Deposition"),
        T("A river deposits when it loses energy and can no longer carry its load. This happens when velocity falls: where "
          "gradient decreases, where the river enters a lake or the sea, on the inside of meander bends, where discharge falls "
          "after a flood or in the dry season, where the channel widens, or when load suddenly increases (for example after a "
          "landslide). The largest particles are dropped first, so deposits are **sorted** by size."),
        H("Downstream changes: the Bradshaw model"),
        T("The Bradshaw model summarises how channel characteristics usually change from source to mouth. Discharge, width, "
          "depth, cross-sectional area, hydraulic radius and mean velocity increase downstream. Gradient, load particle size "
          "and channel roughness decrease. Mean velocity rises although gradient falls, because the deeper, more efficient "
          "channel loses less energy to friction."),
        EX("Worked example 2: explaining a fieldwork result", intro="Fieldwork on a stream near Buea found that mean velocity was higher at the lowest site than at the steep upper site. Explain this.", steps=[
            S("Expectation", text="Many students expect water to flow faster on steep slopes."),
            S("Friction upstream", text="Upstream the channel is shallow and rocky, with a small hydraulic radius and a rough bed, so most energy is lost to friction and turbulence."),
            S("Downstream", text="Downstream the channel is deeper and smoother with a larger hydraulic radius, and discharge is greater, so less energy is lost and mean velocity is higher."),
            S("Link to model", text="This agrees with the Bradshaw model."),
        ]),
        MISTAKE("Confusing attrition and abrasion", "Abrasion wears the bed and banks; attrition wears the load particles against each other."),
        MISTAKE("Saying a river is fastest in its upper course", "Turbulent flow over boulders looks fast, but the mean velocity is usually lower than downstream. Explain using hydraulic radius and friction."),
        QUIZ("Which process mainly makes river pebbles smaller and rounder downstream?",
             ["Hydraulic action", "Abrasion", "Attrition", "Solution"], 2,
             "Attrition is collision between particles of load, which chips off corners.",
             hint="Which process acts on the load itself?",
             feedback=["Hydraulic action is the force of water on the bed and banks.", "Abrasion wears the channel, using the load as a tool.", "", "Solution dissolves soluble rock; it does not round pebbles in a few kilometres."]),
        QUIZ("What does the competence of a river describe?",
             ["The total load it carries", "The largest particle it can move", "Its discharge", "Its ability to dissolve rock"], 1,
             "Competence refers to particle size; capacity refers to total amount.",
             hint="Competence is about size, capacity is about amount.",
             feedback=["That is capacity.", "", "Discharge is volume per second, not a measure of load.", "That is the process of solution."]),
        H("Practice"),
        PQ("A rectangular channel is 8 m wide and 2 m deep. Calculate its hydraulic radius.", "Area = 8 x 2 = 16 square metres. Wetted perimeter = 8 + 2 + 2 = 12 m. R = 16 / 12 = 1.33 m."),
        PQ("Outline four conditions under which a river deposits its load.", "1. Gradient decreases, for example where a river leaves highlands for a plain. 2. The river enters a standing body of water (lake or sea) and slows. 3. Discharge falls after a flood or in the dry season. 4. Water slows on the inside of a meander bend. Also: a sudden increase in load, or widening of the channel."),
        PQ("Explain why most sediment transport in a river happens during a few floods each year.", "Velocity and discharge are highest in floods. Competence and capacity rise very rapidly with velocity, so a flood can move boulders and huge volumes of load that are immobile at normal flow."),
        PQ("Essay plan: 'Explain the processes by which rivers erode and transport material, and how they vary along a river's course.'", "Introduction: energy and its controls. Erosion processes with mechanisms (hydraulic action, abrasion, attrition, solution), vertical and lateral erosion. Transport processes linked to particle size; competence and capacity. Variation downstream: Bradshaw model, more suspension and larger discharge downstream, more traction and vertical erosion upstream in floods. Evaluation: rock type, floods and human changes (dams trap load) can override the model. Conclusion."),
        TIP("Exam link: the erosion and transport processes are tested in Paper 1 (matching a process to a description) and in Paper 2 essays on river landforms. In Paper 3 stream fieldwork, link your measured width, depth and velocity to hydraulic radius and the Bradshaw model."),
        SUM("Only a small part of a river's energy is free for erosion and transport; the rest overcomes friction.",
            "Hydraulic radius = area / wetted perimeter; a larger value means a more efficient channel.",
            "Erosion: hydraulic action, abrasion, attrition, solution. Transport: traction, saltation, suspension, solution.",
            "Competence is the largest particle carried; capacity is the total load.",
            "Deposition happens when velocity falls; the Bradshaw model describes downstream changes."),
    ],
))

# ------------------------------------------------------------------ 4. Hjulstrom curve
LESSONS.append(lesson(
    module=M1,
    topic="Fluvial erosion, transport and deposition",
    title="The Hjulstrom curve: velocity, particle size and sediment movement",
    slug="gpl1-hjulstrom-curve",
    minutes=22,
    summary="The Hjulstrom curve links river velocity to particle size and shows when particles are eroded, transported or deposited. Learn to read its log scales, explain its shape and evaluate its limits.",
    objectives=[
        "Read the critical erosion velocity and settling velocity curves on log scales",
        "Explain why fine clay needs a higher velocity to erode than sand",
        "Use the curve to explain sorting, floods and deposition",
        "Evaluate the strengths and limitations of the Hjulstrom curve",
    ],
    key_concepts=["Hjulstrom curve", "Critical erosion (entrainment) velocity", "Settling (fall) velocity", "Cohesion",
                  "Logarithmic scale", "Sorting"],
    blocks=[
        H("Introduction"),
        T("In 1935 the Swedish geographer Filip Hjulstrom published a graph based on laboratory flume experiments. It shows, "
          "for particles of different sizes, the velocity at which a river picks them up and the velocity at which it drops "
          "them. Students often find it hard at first because both axes use **logarithmic scales**. Once read correctly, it "
          "explains a great deal about river behaviour."),
        D("On a **logarithmic scale** each equal step is a multiplication by 10: 0.01, 0.1, 1, 10, 100. Values between grid "
          "lines are not evenly spaced. Read carefully and give answers as approximate values or ranges.", title="Log scales"),
        IMG("algpl1-hjulstrom.svg", alt="Hjulstrom curve with log axes: particle size 0.001 to 1000 mm, mean velocity 0.1 to 1000 cm/s; an upper U-shaped critical erosion velocity curve with its lowest point in sand, a lower settling velocity curve, and zones of erosion, transport and deposition",
            caption="Figure 1. The Hjulstrom curve (schematic; values are approximate)."),
        KEY("The two curves and three zones", "Learn what each part means.", cards=[
            ["Critical erosion velocity (upper curve)", "The minimum velocity needed to pick up (entrain) particles of a given size from the bed."],
            ["Settling velocity (lower curve)", "Below this velocity, particles of that size fall out of the flow and are deposited."],
            ["Erosion zone", "Above the upper curve: particles are picked up and carried."],
            ["Transport zone", "Between the curves: particles already moving keep moving, but particles on the bed are not picked up."],
            ["Deposition zone", "Below the lower curve: particles settle."],
        ]),
        H("Explaining the shape"),
        T("**Sand (about 0.1 to 1 mm) is the easiest material to erode.** The upper curve is lowest here, at roughly 20 to 30 cm/s "
          "on most versions of the graph."),
        T("**Larger particles (gravel, pebbles, boulders) need more velocity** because they are heavier. This part of the curve "
          "rises steadily with size."),
        T("**Fine silt and clay also need high velocity**, even though they are tiny. Clay particles are flat and stick together "
          "(**cohesion**), and a clay bed is smooth, so there is little turbulence to lift particles. Fine particles also lie "
          "within the thin, slow layer of water next to the bed."),
        T("**Once in suspension, clay hardly ever settles.** The lower curve shows that clay keeps moving at velocities near "
          "zero. This is why rivers stay brown long after a storm and why fine clay is deposited only in very still water, such "
          "as lakes, reservoirs and backswamps."),
        EX("Worked example 1: reading the curve", intro="Using Figure 1, describe what happens to particles of 1 mm (coarse sand) as velocity falls from 100 cm/s to 3 cm/s.", steps=[
            S("At 100 cm/s", text="This is above the erosion curve for 1 mm (about 30 cm/s), so the particles are eroded and carried."),
            S("Between about 30 and 7 cm/s", text="Between the curves: particles already moving are transported, but no new ones are picked up."),
            S("Below about 7 cm/s", text="Below the settling curve for 1 mm, so they are deposited."),
            S("Conclusion", text="By 3 cm/s, 1 mm sand is deposited, while finer silt and clay are still carried. This produces sorting."),
        ]),
        EX("Worked example 2: a puzzle", intro="A river at 50 cm/s flows over a bed of sand and a bed of clay. Which is eroded? Explain.", steps=[
            S("Sand", text="The erosion velocity for medium sand is about 20 to 30 cm/s, below 50 cm/s, so the sand is eroded."),
            S("Clay", text="Fine clay needs roughly 100 cm/s or more because of cohesion, so the clay bed is not eroded."),
            S("Answer", text="The sand is eroded but the clay is not, even though clay particles are far smaller."),
        ]),
        H("Using the curve to explain landforms"),
        T("The curve explains **sorting** (coarse load is dropped first as velocity falls), the formation of **levees** (coarse "
          "sediment dropped first at the channel edge in floods), **point bars** (deposition where velocity is low on the inside "
          "of bends) and **delta** layering (gravel near the mouth, clay carried far into the sea)."),
        H("Evaluating the Hjulstrom curve"),
        KEY("Strengths and limits", "A Level essays expect evaluation of models.", cards=[
            ["Strengths", "Simple, visual summary of the relationship between velocity and particle size; explains sorting, the importance of floods and the special behaviour of clay; based on experimental data."],
            ["Limits", "Made in a laboratory flume with well-sorted, uniform particles; real beds are mixed, packed and armoured. It uses mean velocity, but bed velocity matters most. It ignores particle shape, density, water temperature and the amount of load already carried. The curves are really bands, not exact lines."],
        ]),
        MISTAKE("Reading log scales as if they were linear", "Halfway between 10 and 100 is about 30, not 55. Give approximate values and say 'about'."),
        MISTAKE("Saying 'the smaller the particle, the easier to erode'", "That is only true for particles larger than sand. Silt and clay need higher velocities because of cohesion."),
        QUIZ("Which particle size needs the lowest velocity to be eroded?",
             ["Clay", "Silt", "Sand", "Boulders"], 2,
             "The critical erosion curve has its lowest point in the sand range.",
             hint="Find the lowest point of the upper curve.",
             feedback=["Clay is cohesive and needs a high velocity.", "Silt also needs more velocity than sand.", "", "Boulders are heavy and need very high velocity."]),
        QUIZ("Why is fine clay deposited mainly in lakes and backswamps?",
             ["It is too heavy to be carried far", "It settles only when the water is almost still", "It dissolves in moving water", "It is eroded only by attrition"], 1,
             "The settling velocity for clay is extremely low, so clay stays in suspension until water is nearly still.",
             hint="Look at the lower curve at the left side.",
             feedback=["Clay is the lightest load, not the heaviest.", "", "Clay is carried in suspension, not dissolved.", "Attrition affects the size of load, not where clay settles."]),
        H("Practice"),
        PQ("Define critical erosion velocity and settling velocity.", "Critical erosion (entrainment) velocity is the minimum mean velocity at which particles of a given size are picked up from the bed. Settling (fall) velocity is the velocity below which particles of a given size can no longer be carried and are deposited."),
        PQ("Explain why particles of fine silt and clay need a higher velocity to be eroded than sand.", "Clay and fine silt are cohesive: the flat particles stick together by electrical attraction. A bed of fine particles is smooth, so there is little turbulence, and the particles lie within the slow layer of water near the bed. More energy is therefore needed to entrain them."),
        PQ("Using the Hjulstrom curve, explain why floods are so important in shaping river channels.", "In floods velocity may rise to well over 100 cm/s, enough to entrain gravel and pebbles (and cohesive clay banks) that are immobile at normal flow. Competence and capacity rise rapidly, so most erosion and transport happen in a few flood events."),
        PQ("Essay plan: 'Assess the usefulness of the Hjulstrom curve in explaining river processes.'", "Introduction: describe the curve and its origin (laboratory experiments, 1935). Uses: explains erosion, transport and deposition thresholds; sorting; behaviour of clay; landforms such as levees and deltas. Limits: flume with uniform particles; mean velocity versus bed velocity; ignores shape, density, packing and load concentration; curves are bands. Judgement: a useful general model for teaching and prediction, but field conditions need caution."),
        TIP("Exam link: Paper 1 often asks you to read the Hjulstrom curve or identify a zone; Paper 2 essays on fluvial processes reward a sketch of the curve with labelled zones. Always say values are approximate."),
        SUM("The Hjulstrom curve plots mean velocity against particle size on log scales.",
            "Upper curve: critical erosion velocity. Lower curve: settling velocity. Zones: erosion, transport, deposition.",
            "Sand is easiest to erode; clay needs high velocity because of cohesion but settles only in still water.",
            "The curve explains sorting, floods, levees, point bars and deltas.",
            "It is a laboratory model: use it with care in real rivers."),
    ],
))

# ------------------------------------------------------------------ 5. River landforms
LESSONS.append(lesson(
    module=M1,
    topic="River landforms",
    title="River landforms of erosion and deposition, and sinuosity",
    slug="gpl1-river-landforms",
    minutes=25,
    summary="Explain the formation of waterfalls, gorges, potholes, meanders, ox-bow lakes, floodplains, levees, braided channels and deltas, and calculate and interpret the sinuosity index from a map.",
    objectives=[
        "Explain the formation of waterfalls, gorges, potholes and interlocking spurs",
        "Explain meander development using helicoidal flow, and the formation of ox-bow lakes",
        "Explain floodplains, levees, braided channels and deltas",
        "Calculate the sinuosity index and interpret its value",
    ],
    key_concepts=["Waterfall and gorge", "Pothole", "Meander", "Helicoidal flow", "Thalweg", "River cliff and point bar",
                  "Ox-bow lake", "Floodplain and levee", "Braided channel", "Delta", "Sinuosity index"],
    blocks=[
        H("Introduction"),
        T("Cameroon has striking river landforms: the Lobe Falls near Kribi drop straight into the sea, the Ekom-Nkam falls "
          "plunge over a step in the western highlands, and the lower Wouri and Sanaga wind across wide, wet plains. Each "
          "landform is the result of the processes in the last two lessons acting on particular rocks and slopes."),
        H("Landforms mainly of erosion"),
        KEY("Upper-course landforms", "Vertical erosion dominates where the river is far above base level.", cards=[
            ["V-shaped valley and interlocking spurs", "Vertical erosion deepens the channel while weathering and mass movement wear back the valley sides, giving a V shape. The river winds around resistant spurs, which interlock."],
            ["Potholes", "Circular hollows in a rocky bed, drilled by pebbles swirled in eddies (abrasion)."],
            ["Rapids", "Stretches of turbulent water where bands of hard and soft rock alternate across the bed."],
        ]),
        EX("Worked example 1: formation of a waterfall and gorge", intro="Explain how a waterfall forms and retreats to leave a gorge.", steps=[
            S("Geology", text="A band of resistant rock (for example a basalt or granite) overlies weaker rock."),
            S("Differential erosion", text="The weak rock downstream is eroded faster by hydraulic action and abrasion, so a step forms in the long profile."),
            S("Plunge pool", text="Water falling over the step erodes a deep plunge pool by hydraulic action and abrasion from swirling load."),
            S("Undercutting", text="Spray and splash erode the weak rock behind the fall, undercutting the hard cap rock and leaving an overhang."),
            S("Collapse and retreat", text="The unsupported overhang collapses. The fall moves upstream, repeating the cycle and leaving a steep-sided gorge."),
        ]),
        H("Meanders"),
        D("A **meander** is a sinuous bend in a river. The **thalweg** is the line of deepest, fastest flow, which swings to the "
          "outside of each bend. **Helicoidal flow** is the corkscrew movement of water: surface water moves towards the outer "
          "bank, sinks, and returns along the bed to the inner bank.", title="Meander terms"),
        IMG("algpl1-meander.svg", alt="Cross-section of a meander bend: steep river cliff on the outside of the bend with deep water, a gentle point bar on the inside with deposits, and a corkscrew arrow showing helicoidal flow",
            caption="Figure 1. Cross-section across a meander bend."),
        EX("Worked example 2: meander development", intro="Explain how meanders form and migrate.", steps=[
            S("Riffles and pools", text="Even in a straight channel, deposits (riffles) and deeper sections (pools) form at regular spacing, so the thalweg begins to swing from side to side."),
            S("Outer bend", text="Fast flow and helicoidal flow concentrate energy on the outer bank, which is undercut by hydraulic action and abrasion, forming a steep river cliff."),
            S("Inner bend", text="Slow water on the inside deposits sediment, carried there by the return flow along the bed, building a point bar (slip-off slope)."),
            S("Migration", text="Erosion on the outside and deposition on the inside make the meander grow sideways and move downstream, widening the floodplain."),
        ]),
        D("An **ox-bow lake** forms when two outer bends erode towards each other until the neck is cut through, usually "
          "during a flood. The river takes the shorter course; deposition seals the old bend, leaving a curved lake that later "
          "fills with silt and vegetation.", title="Ox-bow lake"),
        H("Landforms mainly of deposition"),
        KEY("Lower-course landforms", "Deposition dominates where gradient is low and the river floods.", cards=[
            ["Floodplain", "Wide, flat land beside the river made of alluvium deposited during floods and by meander migration."],
            ["Levees", "In a flood, velocity drops sharply at the channel edge, so the coarsest sediment is dropped first, building raised banks. Fine clay settles further away in backswamps."],
            ["Braided channel", "A channel divided by islands of sediment (eyots), where load is large and discharge varies greatly, for example in semi-arid areas or below eroding mountains."],
            ["Delta", "Where a river enters a sea or lake, its velocity falls and it deposits load faster than waves and tides remove it. The river splits into distributaries. Deltas may be arcuate, bird's-foot or cuspate."],
        ]),
        T("An **estuary** is the tidal mouth of a river where tides remove sediment and keep the mouth open, as at the Wouri "
          "estuary near Douala, where the city's port lies."),
        H("Measuring meanders: the sinuosity index"),
        F(r"\text{Sinuosity index} = \frac{\text{actual channel length}}{\text{straight-line distance}}", title="Sinuosity index"),
        T("A value of 1 means a perfectly straight channel. Many textbooks call a channel **straight** below about 1.05, "
          "**sinuous** from about 1.05 to 1.5 and **meandering** above 1.5. Check the class limits in your textbook."),
        EX("Worked example 3: sinuosity from a map", intro="On a 1:50 000 map, a river between two bridges measures 25.2 cm along the channel (with a string) and 14 cm in a straight line. Calculate and interpret the sinuosity.", steps=[
            S("Ratio", math=r"\frac{25.2}{14} = 1.8"),
            S("Units", text="Both lengths are on the same map, so the scale cancels; you can also convert: 25.2 cm x 0.5 km/cm = 12.6 km and 14 cm = 7 km, giving 12.6 / 7 = 1.8."),
            S("Interpret", text="1.8 is above 1.5, so the river is strongly meandering. This suggests a gentle gradient, a wide floodplain and dominant lateral erosion and deposition: a middle or lower course."),
        ]),
        MISTAKE("Giving a number with no meaning", "The Board's 2023 report notes that many candidates calculated sinuosity but could not say what the value showed. Always state the class (straight, sinuous, meandering) and what it tells you about gradient, energy and the stage of the river."),
        MISTAKE("Explaining meanders with 'the river erodes the outside'", "Explain why: the thalweg and helicoidal flow concentrate energy on the outer bank, and return flow carries sediment to the inner bank."),
        QUIZ("Where is the point bar of a meander found?",
             ["On the outside of the bend", "On the inside of the bend", "In the plunge pool", "On top of the levee"], 1,
             "Slow flow on the inside of the bend deposits sediment as a point bar.",
             hint="Where is the water slowest?",
             feedback=["The outside of the bend is eroded into a river cliff.", "", "Plunge pools are at the foot of waterfalls.", "Levees are built by floods along the channel edges, not on bends specifically."]),
        QUIZ("A channel is 7.2 km long between two points that are 6.4 km apart in a straight line. How is it best described?",
             ["Straight", "Sinuous", "Meandering", "Braided"], 1,
             "7.2 / 6.4 = 1.125, between 1.05 and 1.5: sinuous.",
             hint="Divide channel length by straight-line distance.",
             feedback=["Straight would be below about 1.05.", "", "Meandering would be above 1.5.", "Braiding is about channel division by islands, not sinuosity."]),
        H("Practice"),
        PQ("A river measures 18.6 km along its channel between two points 12.0 km apart. Calculate the sinuosity and state its significance.", "Sinuosity = 18.6 / 12.0 = 1.55. It is above 1.5, so the river is meandering, suggesting low gradient, lateral erosion and deposition and a floodplain."),
        PQ("Explain the formation of levees.", "During floods the river spills over its banks. As the water leaves the channel, its depth falls and friction rises, so velocity drops sharply. The coarsest load is deposited first at the channel edge; finer material is carried further onto the floodplain. Repeated floods build raised banks (levees) of coarse material, with fine clay in backswamps behind."),
        PQ("Explain why braided channels are common below glaciers and in semi-arid regions.", "Both have very large loads of coarse sediment and highly variable discharge. When discharge falls, the river cannot carry its load and deposits it as bars and islands; the flow divides around them into many channels."),
        PQ("Essay plan: 'With the aid of diagrams, explain the formation of meanders and ox-bow lakes.'", "Introduction: define meander, thalweg and helicoidal flow. Formation: riffle and pool sequence, thalweg swing, erosion on outer bank (river cliff), deposition on inner bank (point bar), with a cross-section diagram. Migration downstream and widening of the floodplain. Ox-bow lake: narrowing neck, cutting through in flood, sealing by deposition, infilling; plan diagrams at three stages. Evaluation: the exact cause of initial meandering is debated, so check your textbook. Example. Conclusion."),
        TIP("Exam link: landforms are a Paper 2 essay favourite (explain with labelled diagrams) and appear in Paper 1. In Paper 3 map work you may be asked to calculate sinuosity and say what it means, using map evidence only."),
        SUM("Erosional landforms: V-shaped valleys, interlocking spurs, potholes, rapids, waterfalls and gorges.",
            "Meanders grow by erosion on the outer bend and deposition on the inner bend, driven by the thalweg and helicoidal flow.",
            "Ox-bow lakes form when a meander neck is cut through in a flood.",
            "Depositional landforms: floodplains, levees, braided channels and deltas.",
            "Sinuosity = channel length / straight-line distance; above about 1.5 is meandering. Always interpret the value."),
    ],
))

# ------------------------------------------------------------------ 6. Graded profile and rejuvenation
LESSONS.append(lesson(
    module=M1,
    topic="The graded profile and rejuvenation",
    title="Base level, the graded profile and rejuvenated landforms",
    slug="gpl1-graded-profile-rejuvenation",
    minutes=23,
    summary="A graded river has a smooth concave long profile balanced to its base level. A fall in base level rejuvenates the river, producing knickpoints, river terraces and incised meanders. Learn the causes, landforms and gradient calculations.",
    objectives=[
        "Explain base level and the idea of a graded long profile",
        "Explain the causes of rejuvenation: eustatic and isostatic change and tectonic uplift",
        "Explain the formation of knickpoints, river terraces and incised meanders",
        "Calculate and compare gradients from map or profile data",
    ],
    key_concepts=["Base level", "Graded profile", "Long profile", "Rejuvenation", "Eustatic change", "Isostatic change",
                  "Knickpoint", "River terrace", "Incised meander", "Gradient"],
    blocks=[
        H("Introduction"),
        T("A river cannot erode below the level of the water body it flows into. That level, its **base level**, controls the "
          "shape of the whole river. When base level changes, the river must adjust, and it leaves clues in the landscape: "
          "waterfalls far inland, steps of old floodplain high above the river, and deep winding gorges."),
        D("**Base level** is the lowest level to which a river can erode, normally sea level. A lake, a band of resistant rock or "
          "a dam can act as a temporary or **local base level** upstream of it.", title="Base level"),
        H("The long profile and grade"),
        D("The **long profile** is the gradient of a river from source to mouth. A **graded profile** is a smooth, concave "
          "curve, steep near the source and gentle near the mouth, in which the river has just enough energy to carry its load: "
          "erosion and deposition are in balance over time.", title="Graded profile"),
        T("The idea of grade is linked with the American geologist G. K. Gilbert and with W. M. Davis's cycle of erosion. In "
          "reality a perfectly graded profile is rare: changes in rock type, tributaries adding discharge and load, and changes "
          "of base level and climate keep interrupting it. Many geographers therefore treat grade as a tendency rather than a "
          "state that is reached. Check how your textbook defines it."),
        H("Calculating gradient"),
        F(r"\text{Gradient} = \frac{\text{vertical difference}}{\text{horizontal distance}}", title="Gradient"),
        EX("Worked example 1: gradient from a map", intro="A river falls from the 900 m contour to the 600 m contour over a horizontal distance of 4.5 km. Find the gradient.", steps=[
            S("Same units", text="Vertical difference = 900 - 600 = 300 m. Horizontal distance = 4.5 km = 4 500 m."),
            S("Divide", math=r"\frac{300}{4500} = \frac{1}{15}"),
            S("Express", text="Gradient = 1 in 15 (or about 0.067, or 6.7%)."),
        ]),
        EX("Worked example 2: comparing reaches", intro="Downstream, the same river falls 240 m over 6 km. Compare the two gradients.", steps=[
            S("Gradient", math=r"\frac{240}{6000} = \frac{1}{25}"),
            S("Compare", text="1 in 25 is gentler than 1 in 15: the river becomes gentler downstream, as expected for a concave profile."),
        ]),
        H("Rejuvenation"),
        D("**Rejuvenation** is renewed vertical erosion caused by a fall in base level (or a rise of the land), which gives the "
          "river extra potential energy.", title="Rejuvenation"),
        KEY("Causes of a relative fall in base level", "", cards=[
            ["Eustatic change", "A world-wide fall in sea level, for example when water is locked in ice sheets during a glacial period."],
            ["Isostatic change", "The land rises after a load is removed, for example when an ice sheet melts and the crust slowly rebounds."],
            ["Tectonic uplift", "Earth movements raise the land, as in rifting or doming of a plateau."],
            ["Local causes", "River capture, or a lake draining, can also lower a river's base level."],
        ]),
        IMG("algpl1-long-profile.svg", alt="Long profile: a dashed old graded profile ending at an old sea level and a new solid profile with a knickpoint midway, below which the river is graded to a lower new sea level",
            caption="Figure 1. A knickpoint formed by a fall in base level."),
        H("Rejuvenated landforms"),
        KEY("Landforms of rejuvenation", "Learn each with its formation.", cards=[
            ["Knickpoint", "A break of slope in the long profile where the new, steeper lower section meets the old profile. It is often marked by a waterfall or rapids and retreats upstream by headward erosion."],
            ["River terraces", "Remnants of an old floodplain left high above the river when renewed vertical erosion cuts down into it. Paired terraces lie at the same height on both sides (rapid down-cutting); unpaired terraces form when lateral migration and down-cutting combine."],
            ["Incised meanders", "Meanders cut deep into the land. Entrenched meanders have steep, symmetrical sides (rapid down-cutting); ingrown meanders are asymmetrical, with a gentle slip-off slope (slower down-cutting with lateral erosion)."],
        ]),
        EX("Worked example 3: explaining paired terraces", intro="Explain how paired river terraces form after a fall in sea level.", steps=[
            S("Before", text="The river meanders across a wide floodplain, graded to the old base level."),
            S("Base level falls", text="The river gains potential energy, and a knickpoint forms and retreats upstream."),
            S("Down-cutting", text="Behind the knickpoint the river erodes vertically into its own floodplain, forming a new, lower valley floor."),
            S("Result", text="The remnants of the old floodplain are left as flat steps at the same height on both sides: paired terraces. Repeated falls give a staircase of terraces."),
        ]),
        T("In Cameroon, rivers falling from the South Cameroon Plateau to the coastal lowland, such as the Sanaga at Edea, pass "
          "over falls and rapids that mark steps in their long profiles. Textbooks link such steps to uplift and changes of base "
          "level as well as to resistant rock; check your textbook for the explanation it gives for named examples."),
        MISTAKE("Calling every waterfall a knickpoint of rejuvenation", "Many waterfalls are caused by hard rock bands. A rejuvenation knickpoint is linked to a change of base level; look for terraces or incised meanders as supporting evidence."),
        MISTAKE("Mixing up eustatic and isostatic", "Eustatic = change in the level of the sea itself (global). Isostatic = the land moving up or down (local or regional)."),
        QUIZ("What is the break of slope called where a rejuvenated lower section of a long profile meets the old graded section?",
             ["Base level", "Knickpoint", "Watershed", "Plunge pool"], 1,
             "A knickpoint is the break of slope where the new profile meets the old one.",
             hint="Look for the sudden change in gradient.",
             feedback=["Base level is the sea level at the mouth.", "", "The watershed is the edge of the basin.", "A plunge pool may be found at a knickpoint waterfall, but the break of slope is the knickpoint."]),
        QUIZ("Melting of an ice sheet causes the land beneath to rise slowly. What kind of change is this?",
             ["Eustatic", "Isostatic", "Tectonic subduction", "Local base level"], 1,
             "Isostatic change is vertical movement of the land as loads are added or removed.",
             hint="Is it the sea or the land that moves?",
             feedback=["Eustatic change is a change in sea level itself.", "", "Subduction is a plate-boundary process, not rebound.", "A local base level is a lake or hard rock band."]),
        H("Practice"),
        PQ("A river falls 150 m over 3 km. Express the gradient as a ratio.", "150 / 3 000 = 1/20, so the gradient is 1 in 20 (0.05, or 5%)."),
        PQ("A knickpoint retreats upstream at an average rate of 0.5 m per year (teaching figure). How long would it take to retreat 8 km?", "8 km = 8 000 m. Time = 8 000 / 0.5 = 16 000 years."),
        PQ("Distinguish between entrenched and ingrown meanders.", "Both are incised meanders formed by rejuvenation. Entrenched meanders have steep, symmetrical valley sides because down-cutting was rapid with little lateral erosion. Ingrown meanders are asymmetrical, with a steep outer side and a gentle slip-off slope on the inner side, because down-cutting was slower and lateral erosion continued."),
        PQ("Essay plan: 'Explain the causes of river rejuvenation and the landforms that result.'", "Introduction: define base level, graded profile and rejuvenation. Causes: eustatic fall (glacial periods), isostatic uplift, tectonic uplift, local causes, with examples. Landforms: knickpoints and waterfalls (with long-profile diagram), paired and unpaired terraces (cross-section diagram), entrenched and ingrown meanders. Evaluation: grade is an ideal; rock type also creates knickpoints, so field evidence must be combined. Conclusion."),
        TIP("Exam link: Paper 2 essays may ask for causes and landforms of rejuvenation with diagrams; Paper 1 may test terms such as eustatic, isostatic and knickpoint. In Paper 3 map work, gradient calculations need consistent units and a clear ratio."),
        SUM("Base level is the lowest level of erosion, usually sea level; lakes and hard rock give local base levels.",
            "A graded profile is smooth and concave, with erosion and deposition in balance; it is more a tendency than a final state.",
            "Rejuvenation follows a fall in base level: eustatic, isostatic or tectonic.",
            "Landforms: knickpoints, paired and unpaired terraces, entrenched and ingrown meanders.",
            "Gradient = vertical difference / horizontal distance, in the same units."),
    ],
))

# ------------------------------------------------------------------ 7. Structure and composition of the atmosphere
LESSONS.append(lesson(
    module=M2,
    topic="Structure and composition of the atmosphere",
    title="The composition and layered structure of the atmosphere",
    slug="gpl1-atmosphere-structure",
    minutes=22,
    summary="The atmosphere is a mixture of permanent and variable gases arranged in four layers defined by how temperature changes with height. Learn the composition, the layers and their boundaries, and why temperature falls or rises in each.",
    objectives=[
        "Describe the composition of the atmosphere, separating permanent and variable gases",
        "Describe the four layers and their boundaries using a temperature-height graph",
        "Explain the temperature trend in each layer",
        "Use the environmental lapse rate to estimate temperatures with height",
    ],
    key_concepts=["Permanent and variable gases", "Water vapour", "Aerosols", "Troposphere", "Tropopause", "Stratosphere",
                  "Ozone layer", "Mesosphere", "Thermosphere", "Environmental lapse rate"],
    blocks=[
        H("Introduction"),
        T("Climbers on Mount Cameroon notice that the air grows colder and thinner as they rise; passengers on a long flight "
          "cruise above most of the weather, in calm air at about 10 to 12 km. Both experiences come from the structure of the "
          "atmosphere, which you need for every later topic in climatology."),
        D("The **atmosphere** is the envelope of gases held around the Earth by gravity. About half of its mass lies below "
          "roughly 5.5 km and most of it below about 30 km, so it is very thin compared with the Earth's radius.",
          title="Atmosphere"),
        H("Composition"),
        CODE("""Gas                 Share of dry air (by volume)   Notes
Nitrogen            about 78%                      largely inert
Oxygen              about 21%                      respiration, combustion
Argon               about 0.9%                     inert
Carbon dioxide      about 0.04% (over 400 ppm)     absorbs long-wave radiation; rising
Others              traces                         neon, helium, methane, ozone...""", "text", title="Table 1. The permanent and main gases of dry air (approximate)"),
        KEY("Variable components", "Small in amount but very important for weather and climate.", cards=[
            ["Water vapour", "From almost 0% over deserts to about 4% in humid tropical air. It stores latent heat, forms cloud and precipitation and is the most important natural greenhouse gas."],
            ["Carbon dioxide and methane", "Greenhouse gases whose concentrations are rising because of human activity."],
            ["Ozone", "Mostly in the stratosphere, where it absorbs ultraviolet radiation."],
            ["Aerosols", "Tiny particles of dust, salt, smoke and pollen. They act as condensation nuclei and scatter sunlight. Harmattan dust over northern Cameroon is an example."],
        ]),
        H("The four layers"),
        IMG("algpl1-atmosphere.svg", alt="Graph of height 0 to 110 km against temperature: temperature falls in the troposphere to about minus 56 at the tropopause, rises in the stratosphere to near 0 at 50 km, falls in the mesosphere to about minus 90 at 85 km, then rises in the thermosphere; ozone layer shaded 15 to 35 km",
            caption="Figure 1. Average temperature profile of the atmosphere (heights and temperatures approximate)."),
        KEY("Layers and boundaries", "The layers are defined by the direction of the temperature change.", cards=[
            ["Troposphere (0 to about 8 km at the poles, 16 to 18 km at the equator)", "Temperature falls with height, on average about 6.5 degrees C per km, because the air is heated from below by the ground. Contains almost all water vapour, cloud and weather. Thicker at the equator where convection is strong."],
            ["Stratosphere (to about 50 km)", "Temperature is constant at first, then rises, because ozone absorbs ultraviolet radiation. Stable air with little vertical mixing."],
            ["Mesosphere (to about 80 to 85 km)", "Temperature falls again to the coldest values in the atmosphere, about -90 degrees C, as there is little ozone to absorb energy."],
            ["Thermosphere (above 85 km)", "Temperature rises steeply as the few gas molecules absorb very short-wave solar radiation. The air is extremely thin."],
        ]),
        T("The boundaries are the **tropopause**, **stratopause** and **mesopause**. At the tropopause the fall in temperature "
          "stops: it acts as a lid on convection, which is why thunderstorm tops spread out into an anvil shape."),
        D("The **environmental lapse rate (ELR)** is the actual rate at which temperature falls with height in the troposphere "
          "at a given place and time. Its average is about 6.5 degrees C per 1 000 m, but it varies from day to day.",
          title="Environmental lapse rate"),
        EX("Worked example 1: temperature with height", intro="The temperature at sea level is 25 degrees C. Using the average ELR, estimate the temperature at 3 km and at a tropopause height of 12 km.", steps=[
            S("At 3 km", math=r"25 - 6.5 \times 3 = 5.5\,{}^\circ\text{C}"),
            S("At 12 km", math=r"25 - 6.5 \times 12 = -53\,{}^\circ\text{C}"),
            S("Comment", text="This is close to the observed tropopause temperatures of about -55 degrees C, which supports the model."),
        ]),
        EX("Worked example 2: explaining the stratosphere", intro="Explain why temperature increases with height in the upper stratosphere.", steps=[
            S("Absorber", text="The stratosphere contains the ozone layer, mostly between about 15 and 35 km."),
            S("Process", text="Ozone absorbs incoming ultraviolet radiation, converting it to heat."),
            S("Why upward warming", text="The highest layers receive the strongest ultraviolet first, so heating is greatest near the top of the stratosphere."),
            S("Effect", text="Warm air above cooler air is stable, so there is little vertical mixing or weather."),
        ]),
        MISTAKE("Saying the troposphere is heated directly by the sun", "Most solar radiation passes through the air and heats the ground; the air is heated from below by long-wave radiation, conduction and convection. That is why temperature falls with height."),
        MISTAKE("Confusing ozone depletion with global warming", "The ozone layer protects against ultraviolet radiation; its thinning is a separate problem from the enhanced greenhouse effect, though both involve human-made gases."),
        QUIZ("In which layer does almost all weather occur?",
             ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"], 0,
             "The troposphere holds nearly all the water vapour and has rising, mixing air.",
             hint="Where is the water vapour?",
             feedback=["", "The stratosphere is stable and very dry.", "The mesosphere has almost no water vapour.", "The thermosphere is extremely thin air."]),
        QUIZ("Why is the troposphere thicker over the equator than over the poles?",
             ["Ozone is concentrated at the equator", "Strong surface heating drives deep convection", "Gravity is weaker at the poles", "The stratosphere is absent at the equator"], 1,
             "Intense heating at the equator makes air rise high before the temperature fall stops.",
             hint="Think about rising air.",
             feedback=["Ozone is in the stratosphere and does not set tropopause height in this way.", "", "Gravity differences are tiny and are not the reason.", "The stratosphere exists over the whole Earth."]),
        H("Practice"),
        PQ("The temperature at a station at sea level is 30 degrees C. Estimate the temperature at 4 km using the average ELR.", "30 - 6.5 x 4 = 30 - 26 = 4 degrees C."),
        PQ("Explain the importance of water vapour in the atmosphere, although it forms only a small, variable share.", "It is the source of cloud and all precipitation; it absorbs and re-emits long-wave radiation, so it is the main natural greenhouse gas; and it stores latent heat, which is released on condensation and transfers energy from the tropics to higher latitudes and powers storms."),
        PQ("Describe and explain the changes of temperature with height through the four layers of the atmosphere.", "Troposphere: falls (heated from below by the ground). Tropopause: stops falling. Stratosphere: constant then rises (ozone absorbs ultraviolet). Mesosphere: falls to about -90 degrees C (little ozone). Thermosphere: rises steeply (absorption of very short-wave radiation by the few molecules). Use a labelled graph."),
        TIP("Exam link: the layers and composition are typical Paper 1 recall and graph-reading questions; in Paper 2 they support essays on the heat budget and climate change. Draw and label the temperature profile with approximate heights."),
        SUM("Dry air is about 78% nitrogen, 21% oxygen, 0.9% argon and about 0.04% carbon dioxide; water vapour and aerosols vary.",
            "The four layers are troposphere, stratosphere, mesosphere and thermosphere, separated by the tropopause, stratopause and mesopause.",
            "Temperature falls in the troposphere because the air is heated from below.",
            "Temperature rises in the stratosphere because ozone absorbs ultraviolet radiation.",
            "The average environmental lapse rate is about 6.5 degrees C per km, but it varies."),
    ],
))

# ------------------------------------------------------------------ 8. Radiation and heat balance
LESSONS.append(lesson(
    module=M2,
    topic="The radiation and heat balance",
    title="Solar and terrestrial radiation, the global heat budget and heat transfer",
    slug="gpl1-radiation-heat-balance",
    minutes=24,
    summary="The Earth balances incoming short-wave solar radiation with outgoing long-wave radiation. Learn the global heat budget, albedo, the natural greenhouse effect, the surplus at low latitudes and deficit at high latitudes, and how heat is transferred poleward.",
    objectives=[
        "Distinguish short-wave solar radiation from long-wave terrestrial radiation",
        "Describe the global heat budget and calculate albedo",
        "Explain the natural greenhouse effect",
        "Explain the latitudinal energy imbalance and the ways heat is transferred poleward",
    ],
    key_concepts=["Insolation", "Short-wave and long-wave radiation", "Albedo", "Global heat budget", "Greenhouse effect",
                  "Latitudinal energy imbalance", "Sensible and latent heat transfer", "Ocean currents"],
    blocks=[
        H("Introduction"),
        T("At midday in Garoua the sun is almost overhead for much of the year; in northern Europe in winter it barely rises "
          "above the horizon. Yet the tropics do not get hotter every year, and the poles do not get colder. The Earth stays in "
          "balance because energy is exchanged with space and moved from the tropics towards the poles."),
        D("**Insolation** (incoming solar radiation) is the short-wave energy from the sun reaching the Earth. **Terrestrial "
          "radiation** is the long-wave (infra-red) energy given off by the Earth's surface and atmosphere. The sun, being very "
          "hot, emits mainly short waves; the much cooler Earth emits long waves.", title="Two kinds of radiation"),
        H("The global heat budget"),
        T("Take the insolation reaching the top of the atmosphere as 100 units. Approximate textbook figures (they differ a "
          "little between sources, so check yours) are:"),
        CODE("""Incoming 100 units of short-wave radiation
  Reflected and scattered back to space     about 30   (clouds, air, surface)
  Absorbed by the atmosphere and clouds     about 20
  Absorbed by the surface                   about 50
                                            --------
                                            100

The surface loses its 50 units by long-wave radiation, by sensible
heat (conduction and convection) and by latent heat (evaporation).
In the long run the Earth emits about 70 units of long-wave
radiation to space, balancing the 70 units it absorbs.""", "text", title="Table 1. A simplified global heat budget (approximate)"),
        D("**Albedo** is the proportion of incoming radiation that a surface reflects. It is written as a decimal or a "
          "percentage. Fresh snow may reflect about 0.8 to 0.9, desert sand about 0.3 to 0.4, grassland about 0.2, dense "
          "forest about 0.1 to 0.2 and calm water with a high sun below 0.1. The Earth as a whole has an albedo of about 0.3.",
          title="Albedo", formula=r"\text{albedo} = \frac{\text{reflected radiation}}{\text{incoming radiation}}"),
        EX("Worked example 1: albedo", intro="A surface receives 800 W per square metre of solar radiation and reflects 200. Find its albedo and the energy it absorbs.", steps=[
            S("Albedo", math=r"\frac{200}{800} = 0.25"),
            S("Absorbed", math=r"800 - 200 = 600 \text{ W/m}^2"),
            S("Interpret", text="An albedo of 0.25 suggests a surface like dry grassland; 75% of the energy is absorbed and heats the ground."),
        ]),
        H("The natural greenhouse effect"),
        T("Short-wave solar radiation passes easily through the atmosphere. The warmed surface emits long-wave radiation, which "
          "**greenhouse gases** (water vapour, carbon dioxide, methane, nitrous oxide, ozone) and clouds absorb and re-emit in "
          "all directions, including back down to the surface (**counter-radiation**). This keeps the average surface "
          "temperature at about 15 degrees C instead of roughly -18 degrees C without it. The natural greenhouse effect is "
          "essential for life; the problem studied later is its **enhancement** by human emissions."),
        TIP("Cloudy nights are warmer than clear nights for the same reason: clouds absorb outgoing long-wave radiation and send "
            "some back. In the harmattan season in the north, clear dry nights can be surprisingly cool."),
        H("Factors that affect insolation at a place"),
        KEY("Controls on insolation", "", cards=[
            ["Angle of the sun", "When the sun is high, the same beam falls on a smaller area and passes through less atmosphere, so heating is greater."],
            ["Length of day", "Longer days in summer at high latitudes give more hours of insolation."],
            ["Cloud cover", "Clouds reflect and absorb insolation; the cloudy rainy season is often less hot by day than the dry season."],
            ["Surface albedo", "Light surfaces reflect more and absorb less."],
            ["Altitude", "Thinner air above highlands absorbs less, but the surface loses heat faster, so highlands such as the western grassfields are cooler overall."],
        ]),
        H("The latitudinal imbalance"),
        IMG("algpl1-energy-latitude.svg", alt="Graph of energy against latitude from 0 to 90 degrees: absorbed solar radiation is high at the equator and falls steeply poleward; outgoing long-wave radiation falls only slightly; the curves cross at about 38 degrees, giving a surplus at low latitudes and a deficit at high latitudes",
            caption="Figure 1. Surplus and deficit of radiation by latitude (schematic)."),
        T("Low latitudes absorb more solar radiation than they lose, giving a **surplus**; high latitudes lose more than they "
          "absorb, giving a **deficit**. The curves cross at roughly 35 to 40 degrees of latitude (textbooks differ). Since the "
          "tropics are not getting steadily hotter, energy must be transferred poleward."),
        KEY("How heat moves poleward", "", cards=[
            ["Atmospheric circulation", "Winds of the general circulation, the Hadley cells and mid-latitude depressions, carry warm air poleward and cold air towards the equator (sensible heat)."],
            ["Latent heat", "Water evaporated in the tropics carries hidden energy that is released when the vapour condenses at higher latitudes."],
            ["Ocean currents", "Warm currents such as the Gulf Stream carry heat poleward; cold currents such as the Benguela return cool water towards the equator."],
        ]),
        EX("Worked example 2: explaining the imbalance", intro="Explain why there is an energy surplus between the tropics and a deficit near the poles.", steps=[
            S("Sun angle", text="Near the equator the sun is high all year, so insolation is concentrated on small areas and passes through less atmosphere."),
            S("Poles", text="At high latitudes the sun is low, its energy is spread over large areas and passes through more atmosphere; there are long periods of darkness in winter."),
            S("Albedo", text="Ice and snow at high latitudes reflect much of what arrives."),
            S("Output", text="Outgoing long-wave radiation varies much less with latitude, so the tropics gain more than they lose and the poles lose more than they gain."),
        ]),
        MISTAKE("Saying greenhouse gases 'trap the sun's rays'", "They absorb outgoing long-wave radiation from the Earth, not incoming short-wave sunlight."),
        MISTAKE("Ignoring latent heat", "A full answer on heat transfer includes latent heat released by condensation as well as winds and ocean currents."),
        QUIZ("Which surface has the highest albedo?",
             ["Tropical rainforest", "Fresh snow", "Tarred road", "Calm sea at midday"], 1,
             "Fresh snow reflects most of the incoming radiation.",
             hint="Which surface looks brightest?",
             feedback=["Dense forest is dark and absorbs most radiation.", "", "Tar is dark and absorbs strongly.", "Water with a high sun reflects very little."]),
        QUIZ("What type of radiation do greenhouse gases mainly absorb?",
             ["Incoming ultraviolet", "Incoming visible light", "Outgoing long-wave (infra-red)", "Gamma rays"], 2,
             "The greenhouse effect works on the long-wave radiation emitted by the warmed surface.",
             hint="Which radiation comes from the Earth?",
             feedback=["Ultraviolet is absorbed mainly by stratospheric ozone.", "Most visible light passes through the atmosphere.", "", "Gamma rays are not part of the heat budget."]),
        H("Practice"),
        PQ("Of 340 units of radiation reaching a surface, 102 are reflected. Calculate the albedo.", "Albedo = 102 / 340 = 0.3 (30%)."),
        PQ("Explain why clear nights are colder than cloudy nights.", "At night there is no insolation, and the surface loses heat by long-wave radiation. Clouds absorb this radiation and re-emit part of it downward (counter-radiation), so the surface cools less. With clear skies the radiation escapes to space and the ground and air cool rapidly."),
        PQ("Essay plan: 'Explain the global heat budget and the means by which energy is transferred from low to high latitudes.'", "Introduction: insolation and terrestrial radiation. The vertical budget: reflected, absorbed by atmosphere, absorbed by surface; long-wave emission; greenhouse effect. The horizontal imbalance: surplus and deficit with a graph and reasons (sun angle, day length, albedo). Transfers: atmospheric circulation (Hadley cells, depressions), latent heat, ocean currents with examples. Evaluation: figures are averages; clouds and aerosols make the budget uncertain; human changes alter it. Conclusion."),
        TIP("Exam link: the heat budget is tested in Paper 1 (albedo, types of radiation) and in Paper 2 essays on the general circulation and climate change. A labelled diagram of surplus and deficit gains credit."),
        SUM("The sun emits short-wave radiation; the Earth emits long-wave radiation.",
            "Of 100 units of insolation, about 30 are reflected, 20 absorbed by the atmosphere and 50 by the surface (approximate).",
            "Albedo = reflected / incoming; snow is high, forest and water low.",
            "The natural greenhouse effect keeps the Earth about 33 degrees C warmer than it would otherwise be.",
            "Low latitudes have a surplus and high latitudes a deficit; winds, latent heat and ocean currents move heat poleward."),
    ],
))

# ------------------------------------------------------------------ 9. Lapse rates and stability
LESSONS.append(lesson(
    module=M2,
    topic="Lapse rates and atmospheric stability",
    title="Lapse rates, adiabatic cooling and atmospheric stability",
    slug="gpl1-lapse-rates-stability",
    minutes=25,
    summary="Rising air cools adiabatically at the dry or saturated rate. Comparing these with the environmental lapse rate shows whether air is stable, unstable or conditionally unstable, and explains clouds, thunderstorms and fohn winds.",
    objectives=[
        "Distinguish the environmental, dry adiabatic and saturated adiabatic lapse rates",
        "Calculate the condensation level and the temperature of rising and sinking air",
        "Explain absolute stability, absolute instability and conditional instability with a graph",
        "Apply stability to cloud types, thunderstorms, fog and the fohn effect",
    ],
    key_concepts=["Adiabatic temperature change", "Environmental lapse rate (ELR)", "Dry adiabatic lapse rate (DALR)",
                  "Saturated adiabatic lapse rate (SALR)", "Dew point", "Condensation level", "Stability", "Conditional instability",
                  "Fohn effect"],
    blocks=[
        H("Introduction"),
        T("On many afternoons in the rainy season, towering cumulonimbus clouds build over Yaounde and burst into thunderstorms; "
          "on other days a flat grey layer of cloud hangs all day without rain. The difference lies in the **stability** of the "
          "air, which depends on how fast a rising bubble of air cools compared with the air around it."),
        D("An **air parcel** is a bubble of air that moves as a unit. When it rises, the pressure around it falls, so it expands "
          "and cools without any heat being taken away. When it sinks it is compressed and warms. This is **adiabatic** "
          "temperature change.", title="Adiabatic change"),
        H("Three lapse rates"),
        KEY("Compare the three", "Only the ELR describes the surrounding air; the other two describe a moving parcel.", cards=[
            ["Environmental lapse rate (ELR)", "The actual fall in temperature with height in the still air at a place and time. Average about 6.5 degrees C per km, but it varies."],
            ["Dry adiabatic lapse rate (DALR)", "The cooling rate of a rising parcel that is not saturated: about 9.8, usually rounded to 10 degrees C per km. It is fixed."],
            ["Saturated adiabatic lapse rate (SALR)", "The cooling rate of a rising saturated parcel. Lower than the DALR, often 4 to 7 degrees C per km, because condensation releases latent heat. Textbooks quote different values; check yours."],
        ]),
        D("The **dew point** is the temperature at which air becomes saturated and water vapour condenses. The **condensation "
          "level** is the height at which a rising parcel cools to its dew point: the cloud base.", title="Dew point and condensation level"),
        T("A simple A Level method treats the dew point as constant, so the parcel cools at the DALR until its temperature "
          "equals the dew point. A more exact rule allows the dew point itself to fall by about 2 degrees C per km, which gives "
          "a cloud base of about 125 m for every degree between temperature and dew point. Use the method in your textbook and "
          "state it."),
        H("Stability and instability"),
        KEY("Three states", "Compare the parcel with the environment at the same height.", cards=[
            ["Absolute stability", "ELR is less than the SALR. A lifted parcel is always colder and denser than its surroundings, so it sinks back. Little cloud, or flat stratus; fog and haze may form."],
            ["Absolute instability", "ELR is greater than the DALR. A lifted parcel is always warmer than its surroundings and keeps rising. Strong convection, cumulus and cumulonimbus."],
            ["Conditional instability", "ELR lies between the SALR and the DALR. The parcel is stable while dry, but if it is forced up past the condensation level it may become warmer than the environment and rise freely."],
        ]),
        IMG("algpl1-stability.svg", alt="Temperature-height graph: environment line falls from 30 degrees at the surface at 8 degrees per km; rising air cools at 10 degrees per km to 20 degrees at 1 km, then at 5 degrees per km, crossing the environment line at about 1.7 km",
            caption="Figure 1. Conditional instability (teaching data)."),
        EX("Worked example 1: conditional instability", intro="Surface air at 30 degrees C has a dew point of 20 degrees C. The ELR is 8 degrees C per km. Rising air cools at 10 degrees C per km until saturated, then at 5 degrees C per km. Find the cloud base, the level at which the parcel becomes buoyant, and its state at 3 km. (Treat the dew point as constant.)", steps=[
            S("Condensation level", math=r"\frac{30 - 20}{10} = 1 \text{ km}"),
            S("Temperatures at 1 km", text="Parcel: 30 - 10 = 20 degrees C. Environment: 30 - 8 = 22 degrees C. The parcel is colder, so it rises only if forced (by relief, a front or convergence)."),
            S("Level of free convection", math=r"20 - 5(h - 1) = 30 - 8h \;\Rightarrow\; 3h = 5 \;\Rightarrow\; h \approx 1.7 \text{ km}"),
            S("At 3 km", text="Parcel: 20 - 5 x 2 = 10 degrees C. Environment: 30 - 24 = 6 degrees C. The parcel is 4 degrees warmer, so it rises freely: towering cumulonimbus may form."),
        ], check=r"20 - 5(\tfrac{5}{3} - 1) = 30 - 8 \times \tfrac{5}{3} \approx 16.7"),
        EX("Worked example 2: the fohn effect", intro="Moist air at 25 degrees C (dew point 15 degrees C) at sea level is forced over a mountain range 3 km high. Using DALR 10 and SALR 6 degrees C per km, find its temperature when it returns to sea level on the far side, assuming the moisture rained out on the windward side. (Teaching figures.)", steps=[
            S("Windward, dry ascent", text="Condensation level = (25 - 15) / 10 = 1 km; temperature there 15 degrees C."),
            S("Saturated ascent", math=r"15 - 6 \times 2 = 3\,{}^\circ\text{C at the summit}"),
            S("Leeward descent", text="Having lost its moisture as rain, the air sinks and warms at the DALR all the way down."),
            S("Result", math=r"3 + 10 \times 3 = 33\,{}^\circ\text{C}"),
            S("Interpret", text="The air is 8 degrees C warmer and much drier on the lee side: a fohn effect, and a rain-shadow area."),
        ]),
        H("Stability and weather"),
        T("Unstable air gives cumulus and cumulonimbus clouds, heavy showers and thunderstorms, typical of humid tropical "
          "afternoons. Stable air gives clear skies or layer clouds, poor dispersal of pollution, and fog. A **temperature "
          "inversion**, where temperature rises with height, is extremely stable: on calm clear nights in highland valleys cold "
          "air drains downslope and fog can form beneath an inversion."),
        MISTAKE("Using the DALR above the cloud base", "Once the parcel is saturated it cools at the SALR, because condensation releases latent heat."),
        MISTAKE("Comparing the wrong things", "Stability compares the parcel's temperature with the environment's temperature at the same height, not the parcel with the surface temperature."),
        QUIZ("The ELR is 4 degrees C per km, the DALR 10 and the SALR 6. What is the state of the air?",
             ["Absolutely stable", "Absolutely unstable", "Conditionally unstable", "Neutral"], 0,
             "The ELR is smaller than both adiabatic rates, so a rising parcel is always colder than its surroundings.",
             hint="Compare the ELR with the SALR.",
             feedback=["", "Absolute instability needs an ELR greater than the DALR.", "Conditional instability needs an ELR between 6 and 10.", "Neutral would need the ELR to equal the parcel's rate."]),
        QUIZ("Why is the SALR lower than the DALR?",
             ["Saturated air is heavier", "Condensation releases latent heat, which offsets some of the cooling", "Saturated air rises more slowly", "Clouds reflect sunlight"], 1,
             "Latent heat released on condensation partly cancels the expansion cooling.",
             hint="What happens to energy when vapour becomes liquid?",
             feedback=["Moist air is in fact slightly less dense, and density does not set the lapse rate.", "", "Speed of ascent does not change the rate of cooling per kilometre.", "Reflection affects insolation, not adiabatic cooling."]),
        H("Practice"),
        PQ("Surface air at 28 degrees C has a dew point of 19 degrees C. Treating the dew point as constant and using a DALR of 10 degrees C per km, find the height of the cloud base.", "Cloud base = (28 - 19) / 10 = 0.9 km = 900 m. The parcel's temperature there is 19 degrees C."),
        PQ("Air at 22 degrees C and dew point 14 degrees C crosses a 2.4 km range. Use DALR 10 and SALR 5 degrees C per km, and assume all condensed moisture falls on the windward side. Find the lee-side sea-level temperature.", "Condensation level = (22 - 14) / 10 = 0.8 km at 14 degrees C. Saturated ascent 1.6 km: 14 - 5 x 1.6 = 6 degrees C at the summit. Descent 2.4 km at the DALR: 6 + 24 = 30 degrees C."),
        PQ("Essay plan: 'Explain how atmospheric stability and instability influence weather.'", "Introduction: define adiabatic change, the three lapse rates and stability. Absolute stability with graph: layer cloud, fog, inversions, pollution. Absolute instability with graph: cumulonimbus, thunderstorms, heavy convectional rain. Conditional instability: need for a trigger (relief, fronts, convergence at the ITCZ), with a worked example. Applications: tropical afternoon storms, fohn winds and rain shadows. Evaluation: the ELR changes through the day, so the same place can be stable at dawn and unstable by afternoon. Conclusion."),
        TIP("Exam link: Paper 1 tests the lapse rates and stability states, often with a temperature-height graph; Paper 2 essays on precipitation and storms reward a labelled stability diagram. Show each step of any parcel calculation."),
        SUM("Rising air expands and cools adiabatically; sinking air is compressed and warms.",
            "DALR about 10 degrees C per km; SALR lower (often 4 to 7) because of latent heat; ELR varies, average 6.5.",
            "ELR below SALR: stable. ELR above DALR: unstable. ELR between them: conditionally unstable.",
            "Cloud base is where the rising air reaches its dew point.",
            "Instability gives cumulonimbus and thunderstorms; stability gives layer cloud, fog and inversions; descending dry air gives the fohn effect."),
    ],
))

# ------------------------------------------------------------------ 10. General circulation and jet streams
LESSONS.append(lesson(
    module=M2,
    topic="The general circulation and jet streams",
    title="The tricellular model, the ITCZ and jet streams",
    slug="gpl1-general-circulation-jet-streams",
    minutes=25,
    summary="The tricellular model links pressure belts and planetary winds through the Hadley, Ferrel and polar cells. Learn how the ITCZ migrates and gives southern Cameroon two rainfall maxima, how jet streams and Rossby waves work, and the model's limits.",
    objectives=[
        "Describe and explain the tricellular model of the general circulation",
        "Explain the surface pressure belts, planetary winds and the Coriolis effect",
        "Explain the seasonal migration of the ITCZ and its effect on rainfall in Cameroon",
        "Describe the subtropical and polar front jet streams and Rossby waves, and evaluate the model",
    ],
    key_concepts=["General circulation", "Hadley cell", "Ferrel cell", "Polar cell", "ITCZ", "Coriolis effect",
                  "Trade winds and westerlies", "Jet stream", "Rossby waves"],
    blocks=[
        H("Introduction"),
        T("Why does Yaounde have two rainy seasons, while Maroua has one long dry season with the dusty harmattan? The answer is "
          "not local: it lies in the planet-wide circulation of the atmosphere, which moves the surplus heat of the tropics "
          "towards the poles (the last lesson) and shifts north and south with the overhead sun."),
        D("The **general circulation** is the large-scale, average pattern of air movement around the Earth, including the "
          "pressure belts, planetary winds and vertical cells.", title="General circulation"),
        H("The tricellular model"),
        IMG("algpl1-tricellular.svg", alt="Section from equator to pole showing three circulation cells: Hadley cell from 0 to 30 degrees, Ferrel cell from 30 to 60, polar cell from 60 to 90; low pressure at the equator and 60 degrees, high pressure at 30 and 90; subtropical and polar front jets near the tropopause",
            caption="Figure 1. The tricellular model (northern hemisphere, simplified)."),
        KEY("Three cells", "Each hemisphere has three cells in the model.", cards=[
            ["Hadley cell (0 to 30 degrees)", "Intense heating at the equator makes air rise (low pressure, the ITCZ), cool and give heavy convectional rain. Aloft it flows poleward, cools, and sinks at about 30 degrees, forming the subtropical high pressure belt with dry, clear air and the world's hot deserts. Surface air returns to the equator as the trade winds. Named after George Hadley."],
            ["Ferrel cell (30 to 60 degrees)", "An indirect cell driven by the cells either side. Surface air flows poleward from the subtropical highs as the westerlies and rises at about 60 degrees where it meets cold polar air at the polar front. Named after William Ferrel."],
            ["Polar cell (60 to 90 degrees)", "Cold dense air sinks at the pole (high pressure) and flows outward as the polar easterlies, rising at the polar front."],
        ]),
        D("The **Coriolis effect** is the apparent deflection of moving air caused by the Earth's rotation: to the right in the "
          "northern hemisphere and to the left in the southern hemisphere. It is zero at the equator and strongest at the poles. "
          "It turns air flowing towards the equator into the north-east and south-east **trade winds**, and poleward air into "
          "the **westerlies**.", title="Coriolis effect"),
        H("The ITCZ and Cameroon's rainfall"),
        D("The **Inter-Tropical Convergence Zone (ITCZ)** is the low-pressure belt where the trade winds of the two hemispheres "
          "converge and air rises, bringing cloud and heavy rain. It follows the overhead sun, lagging it by a few weeks, moving "
          "north in the northern summer and south in the northern winter, more over land than over the ocean.", title="ITCZ"),
        EX("Worked example 1: two rainfall maxima", intro="Explain why a station on the southern Cameroon plateau, such as Yaounde, has two rainfall maxima in the year.", steps=[
            S("Overhead sun", text="Places near the equator have the overhead sun twice a year, around the equinoxes."),
            S("ITCZ passes twice", text="The rain belt of the ITCZ passes northward over the station in the first half of the year and southward again in the second half."),
            S("Two wet seasons", text="Each passage brings rising, unstable air and convectional rain, giving two rainy seasons, roughly March to June and September to November (check your textbook for exact months)."),
            S("Little dry season", text="Between them, in about July and August, the rain belt lies further north, so rainfall dips; the main dry season is when the ITCZ is far to the south, around December to February."),
        ]),
        EX("Worked example 2: one rainy season in the north", intro="Explain why Maroua has a single rainy season and a long dry season.", steps=[
            S("Latitude", text="Maroua lies far north of the equator, near the northern limit of the ITCZ's movement."),
            S("Wet season", text="Only in the northern summer does the rain belt reach it, bringing moist south-westerly monsoon air from the Gulf of Guinea; the two passages merge into one rainy season."),
            S("Dry season", text="For most of the year it lies under dry north-easterly air from the Sahara: the harmattan, with dust and low humidity."),
        ]),
        MISTAKE("Explaining two rainfall maxima with relief or altitude", "The Board's 2023 report notes that almost all candidates failed to explain a station's two rainfall maxima and its constant temperature. The answer is the double passage of the overhead sun and the ITCZ; constant high temperatures come from the high sun all year near the equator."),
        H("Jet streams"),
        D("**Jet streams** are narrow bands of very fast wind in the upper troposphere, near the tropopause, often well over "
          "150 km per hour. They form where there is a strong temperature contrast between air masses.", title="Jet streams"),
        KEY("The two main jets", "Both are westerly in the model.", cards=[
            ["Subtropical jet", "Near 30 degrees, at the poleward edge of the Hadley cell, at about 12 km or higher."],
            ["Polar front jet", "Above the polar front at roughly 40 to 60 degrees, at about 9 to 10 km. Its position shifts greatly."],
            ["Rossby waves", "The polar front jet meanders in large waves (usually four to six around the hemisphere). Ridges and troughs in these waves help form surface anticyclones and depressions and steer them."],
            ["Over West Africa", "In the northern summer an African easterly jet in the middle troposphere is linked with the West African monsoon and the storms that cross the Sahel. Check your textbook for detail."],
        ]),
        H("Evaluating the tricellular model"),
        T("The model is a useful simplification that explains the main pressure belts, winds and climate zones (wet equator, "
          "dry subtropics, stormy mid-latitudes). But it is an average: the real circulation shifts with the seasons, is "
          "broken into separate high and low cells by land and sea, and in mid-latitudes is dominated by Rossby waves, "
          "depressions and anticyclones rather than a simple Ferrel cell, which does not exist as a closed loop at any one time."),
        QUIZ("At about 30 degrees north and south, air sinks. What does this produce at the surface?",
             ["Low pressure and heavy rain", "High pressure and dry conditions", "The polar front", "The ITCZ"], 1,
             "Sinking air warms adiabatically and is dry, giving subtropical high pressure and the hot deserts.",
             hint="What happens to sinking air?",
             feedback=["Rising air gives low pressure and rain.", "", "The polar front is at about 60 degrees.", "The ITCZ is near the equator."]),
        QUIZ("In the northern hemisphere, air flowing from the subtropical high towards the equator is deflected to become which wind?",
             ["North-east trade wind", "South-east trade wind", "Westerly", "Polar easterly"], 0,
             "Air moving south is turned to its right by the Coriolis effect, so it comes from the north-east.",
             hint="Coriolis deflects to the right in the northern hemisphere.",
             feedback=["", "The south-east trades blow in the southern hemisphere.", "Westerlies blow poleward of 30 degrees.", "Polar easterlies blow from the polar high."]),
        H("Practice"),
        PQ("State the positions of the main surface pressure belts in the tricellular model.", "Equatorial low (ITCZ) near 0 degrees; subtropical highs near 30 degrees north and south; subpolar lows (polar front) near 60 degrees; polar highs near 90 degrees."),
        PQ("Explain why temperatures at Yaounde are fairly constant through the year.", "Near the equator the sun is high at noon throughout the year and day length hardly changes, so insolation varies little; cloud cover in the rainy seasons also limits heating. The annual temperature range is therefore small."),
        PQ("Essay plan: 'Evaluate the usefulness of the tricellular model in explaining world climates.'", "Introduction: purpose of the model. Explain each cell, the pressure belts and winds with a diagram. Strengths: explains the rainy equator, dry subtropics, westerlies and mid-latitude storms; heat transfer. Limits: an average; seasonal migration of the ITCZ; land-sea contrasts and monsoons; Ferrel cell not a real closed loop; jet streams and Rossby waves dominate mid-latitudes. Example: Cameroon's rainfall regimes. Judgement: a good first explanation that needs refinement."),
        TIP("Exam link: the general circulation is tested in Paper 1 (pressure belts, winds, jet streams) and Paper 2 essays on climates; in Paper 3 you may have to explain a climograph, for example two rainfall maxima or constant temperatures at a station. Name the ITCZ and the overhead sun."),
        SUM("The tricellular model has Hadley, Ferrel and polar cells in each hemisphere.",
            "Pressure belts: equatorial low, subtropical high, subpolar low, polar high; the Coriolis effect turns winds into trades, westerlies and polar easterlies.",
            "The ITCZ follows the overhead sun, giving southern Cameroon two rainfall maxima and the north one rainy season.",
            "The subtropical and polar front jets blow near the tropopause; Rossby waves steer weather systems.",
            "The model is a simplification: seasons, land and sea, and Rossby waves modify it."),
    ],
))

# ------------------------------------------------------------------ 11. Air masses, cyclones and anticyclones
LESSONS.append(lesson(
    module=M2,
    topic="Air masses, cyclones and anticyclones",
    title="Air masses, fronts, depressions, anticyclones and tropical cyclones",
    slug="gpl1-air-masses-cyclones-anticyclones",
    minutes=25,
    summary="Air masses take their temperature and humidity from their source regions. Learn the West African air masses and their boundary, how mid-latitude depressions form and bring a sequence of weather, the weather of anticyclones, and the conditions for tropical cyclones.",
    objectives=[
        "Classify air masses by source region and explain how they are modified",
        "Explain the tropical maritime and tropical continental air masses over Cameroon and their boundary",
        "Explain the formation and weather sequence of a mid-latitude depression and the weather of anticyclones",
        "Explain the conditions for tropical cyclone formation and why none form near the equator",
    ],
    key_concepts=["Air mass", "Source region", "Tropical maritime (mT)", "Tropical continental (cT)", "Front",
                  "Depression (mid-latitude cyclone)", "Occlusion", "Anticyclone", "Tropical cyclone"],
    blocks=[
        H("Introduction"),
        T("Between about November and March, people in Garoua and Maroua wake to dry, hazy mornings as the harmattan blows "
          "dust from the Sahara. From about May the wind turns south-westerly, the air becomes humid and the rains arrive. Two "
          "different **air masses** are taking turns over the country."),
        D("An **air mass** is a very large body of air, often over a thousand kilometres across, with fairly uniform temperature "
          "and humidity at each level. It gains these properties by staying over a **source region**, such as a warm ocean or a "
          "large desert, for several days.", title="Air mass"),
        KEY("Classification", "Two letters describe the source.", cards=[
            ["By latitude", "T = tropical (warm), P = polar (cold), A = arctic or antarctic (very cold), and in some schemes E = equatorial."],
            ["By surface", "m = maritime (over sea: moist), c = continental (over land: dry)."],
            ["Examples", "mT: warm and moist. cT: hot and dry. mP: cool and moist. cP: cold and dry."],
            ["Modification", "As an air mass moves it changes: warm air over a cold surface is cooled from below and becomes stable (fog, stratus); cold air over a warm surface is heated from below and becomes unstable (showers)."],
        ]),
        H("Air masses over Cameroon"),
        T("**Tropical maritime (mT) air** from the Gulf of Guinea and South Atlantic is warm and moist. It reaches Cameroon as "
          "the south-west monsoon and brings the rainy season. **Tropical continental (cT) air** from the Sahara is hot by day, "
          "dry and dusty: the north-east harmattan. The surface boundary between them is called the **Inter-Tropical "
          "Discontinuity (ITD)** or Inter-Tropical Front. It moves north in the northern summer, letting moist air reach the "
          "north, and south in the northern winter, when the harmattan can reach far south."),
        TIP("Some West African storms arrive as long lines of thunderstorms moving from east to west, often called line squalls or disturbance lines. They bring short, violent rain and strong gusts. Check your textbook for the detail it expects."),
        EX("Worked example 1: the seasons at Garoua", intro="Explain how the movement of air masses produces a wet season and a dry season at Garoua in northern Cameroon.", steps=[
            S("Northern summer", text="The overhead sun and the Inter-Tropical Discontinuity move north. Garoua lies south of the ITD, under moist mT monsoon air from the Gulf of Guinea."),
            S("Rain", text="Heating of this moist, unstable air, convergence and passing line squalls give convectional storms: the wet season."),
            S("Northern winter", text="The ITD moves south of Garoua. Dry cT harmattan air from the Sahara covers the area, with low humidity, dust haze and large daily temperature ranges: the dry season."),
            S("Conclusion", text="The seasons follow the north-south shift of the boundary between the two air masses."),
        ]),
        H("Mid-latitude depressions"),
        D("A **depression** (mid-latitude or extra-tropical cyclone) is a low-pressure system, with winds blowing anticlockwise "
          "around it in the northern hemisphere, formed where warm tropical air meets cold polar air along the polar front. A "
          "**front** is the boundary between two air masses.", title="Depression"),
        EX("Worked example 2: life cycle of a depression", intro="Outline the formation of a mid-latitude depression (the Norwegian or Bergen model).", steps=[
            S("Wave", text="Along the polar front, warm mT air meets cold mP air. A small wave develops, helped by divergence below the polar front jet."),
            S("Warm sector", text="The wave deepens. Warm air pushes poleward ahead as a warm front; cold air pushes behind as a cold front. Between them lies the warm sector. Pressure falls in the centre."),
            S("Mature stage", text="Rising warm air gives cloud and rain along both fronts; the system moves east with the westerlies."),
            S("Occlusion", text="The faster cold front catches the warm front and lifts the warm air off the ground: an occluded front. The supply of warm moist air is cut off and the depression fills and dies."),
        ]),
        IMG("algpl1-depression.svg", alt="Cross-section through a depression moving left to right: a steep cold front with cumulonimbus and heavy showers behind the warm sector, and a gentle warm front ahead with nimbostratus, altostratus and cirrus over cold air",
            caption="Figure 1. Section through a mid-latitude depression."),
        CODE("""Stage                Pressure        Cloud                    Weather
Warm front approaches falling         cirrus, then altostratus, steady rain, increasing
                                      nimbostratus
Warm sector          steady          stratus, low cloud       drizzle, mild, humid
Cold front passes    rises quickly   cumulonimbus             heavy showers, gusts,
                                                              temperature falls
Behind cold front    rising          scattered cumulus        clear, cool, showers""", "text", title="Table 1. Weather sequence as a depression passes (northern hemisphere)"),
        H("Anticyclones"),
        D("An **anticyclone** is a high-pressure system of sinking air, with light winds blowing clockwise around it in the "
          "northern hemisphere. Sinking air warms adiabatically and is stable, so cloud is rare.", title="Anticyclone"),
        T("In summer, anticyclones bring hot, sunny days and heat waves. In winter they bring clear, cold nights with frost and "
          "fog, and can trap pollution under an inversion. The subtropical highs over the Sahara are permanent anticyclones."),
        H("Tropical cyclones"),
        KEY("Conditions for formation", "Most textbooks list these; check the exact figures in yours.", cards=[
            ["Warm ocean", "Sea surface temperature of at least about 26 to 27 degrees C over a large area, to a depth of tens of metres."],
            ["Latitude", "Usually between about 5 and 20 degrees: enough Coriolis effect to start rotation. Within about 5 degrees of the equator it is too weak, so Cameroon's coast does not get tropical cyclones."],
            ["Atmosphere", "Low wind shear (winds similar at all heights), moist, unstable air and an initial disturbance."],
            ["Energy", "Latent heat released by condensation in the towering clouds powers the storm. Over land or cool water it loses this supply and decays."],
        ]),
        MISTAKE("Mixing up cyclone directions", "In the northern hemisphere air spirals anticlockwise into a depression and clockwise out of an anticyclone; the directions reverse in the southern hemisphere."),
        MISTAKE("Calling the harmattan a rain-bearing wind", "The harmattan is dry cT air from the Sahara; the rain-bearing air is the moist mT monsoon from the Atlantic."),
        QUIZ("Which air mass brings the rainy season to Cameroon?",
             ["Tropical continental", "Tropical maritime", "Polar continental", "Arctic"], 1,
             "Warm, moist mT air from the Gulf of Guinea arrives as the south-west monsoon.",
             hint="Which air mass is moist?",
             feedback=["cT air from the Sahara is dry: the harmattan.", "", "Polar air does not reach Cameroon.", "Arctic air does not reach the tropics."]),
        QUIZ("What weather is typical as a cold front passes?",
             ["Steady drizzle for many hours", "Heavy showers, gusty winds and a fall in temperature", "Clear skies and frost", "Fog and calm conditions"], 1,
             "The steep cold front lifts warm air rapidly, giving cumulonimbus and short, heavy showers.",
             hint="Think about the steep slope of the front.",
             feedback=["Drizzle belongs to the warm sector.", "", "Clear skies and frost are typical of winter anticyclones.", "Fog and calm are typical of anticyclones."]),
        H("Practice"),
        PQ("Distinguish between a maritime and a continental air mass.", "A maritime air mass forms over the ocean and is moist; a continental air mass forms over land and is dry. Both take their temperature from the latitude of the source region."),
        PQ("Explain why the harmattan reaches further south in some years than others.", "The harmattan is cT air north of the Inter-Tropical Discontinuity. The ITD moves south in the northern winter; when it moves unusually far south, dry dusty air covers more of the country."),
        PQ("Compare the weather of a summer anticyclone with that of a winter anticyclone.", "Both have sinking, stable air, light winds and little cloud. In summer the clear skies give strong insolation, hot days and possible drought. In winter the long, clear nights allow strong radiation cooling, giving frost, fog and temperature inversions that trap pollution."),
        PQ("Essay plan: 'Explain the conditions necessary for the formation of tropical cyclones and why they do not affect Cameroon.'", "Introduction: define tropical cyclone. Conditions: warm ocean (about 26 to 27 degrees C), latitude 5 to 20 degrees for Coriolis, low wind shear, moist unstable air, a trigger. Structure: eye, eye wall, spiral bands, latent heat engine. Decay over land. Cameroon: near the equator (weak Coriolis); Gulf of Guinea storms rarely organise into cyclones; check your textbook for any exceptions. Conclusion."),
        TIP("Exam link: Paper 1 often tests air-mass letters, front weather and the conditions for tropical cyclones; Paper 2 essays may ask for the formation and weather of depressions with a labelled cross-section."),
        SUM("Air masses take their properties from source regions: T, P, A by latitude and m, c by surface.",
            "Over Cameroon, moist mT monsoon air and dry cT harmattan air meet at the Inter-Tropical Discontinuity.",
            "Depressions form on the polar front, have warm and cold fronts, and end by occlusion.",
            "Anticyclones have sinking, stable air: hot sunny summers, cold foggy winter nights.",
            "Tropical cyclones need warm seas, 5 to 20 degrees latitude, low shear and latent heat."),
    ],
))

# ------------------------------------------------------------------ 12. Koppen classification and urban microclimates
LESSONS.append(lesson(
    module=M2,
    topic="Climate classification and urban microclimates",
    title="Koppen climate classification and the urban heat island",
    slug="gpl1-koppen-urban-microclimates",
    minutes=25,
    summary="Koppen's scheme classifies climates from temperature and rainfall data and links them to vegetation. Learn to classify a station, evaluate the scheme, and explain how cities create their own microclimates, especially the urban heat island.",
    objectives=[
        "Describe the main groups of the Koppen classification and their temperature and rainfall criteria",
        "Classify tropical stations as Af, Am or Aw from climate data",
        "Evaluate the strengths and weaknesses of the Koppen scheme",
        "Explain the urban heat island and other urban effects on climate, and ways to reduce them",
    ],
    key_concepts=["Climate classification", "Koppen groups A to E", "Af, Am, Aw", "Microclimate", "Urban heat island",
                  "Heat island intensity", "Anthropogenic heat", "Urban canyon"],
    blocks=[
        H("Introduction"),
        T("A geographer comparing Douala, Yaounde, Ngaoundere and Maroua needs a shared language for their climates. The most "
          "widely used is the classification devised by the German climatologist Wladimir Koppen in the early twentieth "
          "century. At a much smaller scale, the same geographer would find that the centre of Douala is warmer at night than "
          "the farmland outside it: a **microclimate** made by the city."),
        H("The Koppen classification"),
        T("Koppen used monthly mean temperature and precipitation, with boundaries chosen to match the limits of major "
          "vegetation types. Each climate gets a code of two or three letters."),
        KEY("The five main groups", "Thresholds differ slightly between versions of the scheme; check your textbook.", cards=[
            ["A: tropical", "Every month has a mean temperature of 18 degrees C or more. No winter."],
            ["B: dry", "Potential evaporation exceeds precipitation. BW = desert, BS = steppe (semi-arid); h = hot, k = cold."],
            ["C: warm temperate", "Coldest month between about -3 (or 0, in some versions) and 18 degrees C."],
            ["D: cold (snow)", "Coldest month below about -3 (or 0) degrees C, warmest month above 10 degrees C."],
            ["E: polar", "Warmest month below 10 degrees C (ET tundra, EF ice cap)."],
        ]),
        KEY("Subdividing the A climates", "Uses the rainfall of the driest month.", cards=[
            ["Af (tropical rainforest)", "Driest month has at least 60 mm."],
            ["Am (tropical monsoon)", "Driest month under 60 mm, but at least 100 minus (annual total / 25) mm, so a short dry season is offset by heavy annual rain."],
            ["Aw (tropical savanna, wet-and-dry)", "Driest month under 60 mm and under 100 minus (annual total / 25) mm: a marked dry season."],
        ]),
        EX("Worked example 1: classifying a station", intro="Station P (invented for practice): coolest month 23 degrees C; driest month 30 mm; annual total 1 500 mm. Classify it.", steps=[
            S("Group", text="Coolest month is 18 degrees C or more, so group A."),
            S("Af?", text="Driest month 30 mm is below 60 mm, so not Af."),
            S("Am threshold", math=r"100 - \frac{1500}{25} = 100 - 60 = 40 \text{ mm}"),
            S("Decide", text="30 mm is below 40 mm, so the dry season is too strong for Am: the station is Aw (tropical savanna)."),
        ]),
        EX("Worked example 2: a wetter station", intro="Station Q (invented for practice): coolest month 25 degrees C; driest month 45 mm; annual total 2 500 mm. Classify it.", steps=[
            S("Group", text="Coolest month above 18 degrees C: group A. Driest month 45 mm is below 60 mm: not Af."),
            S("Am threshold", math=r"100 - \frac{2500}{25} = 0 \text{ mm}"),
            S("Decide", text="45 mm is above 0 mm, so the station is Am: the heavy annual rain keeps the soil moist through a short dry season."),
        ]),
        T("Cameroon spans several Koppen types: humid tropical (A) climates in the south and on the coast, the savanna (Aw) "
          "climate across the centre, and semi-arid (BS) conditions near Lake Chad. Highland areas such as the western "
          "grassfields and the Adamawa plateau are cooler, and some versions place high stations in group C. Check your atlas "
          "for the codes it gives to named stations."),
        KEY("Evaluating Koppen", "", cards=[
            ["Strengths", "Uses simple, widely available data; clear numerical boundaries; links climate to vegetation; worldwide coverage, easy to map."],
            ["Weaknesses", "Uses monthly means, which hide extremes and day-to-day weather; boundaries are sharp lines while real change is gradual; ignores wind, cloud, humidity and the causes of climate (air masses, circulation); vegetation boundaries have been changed by people; highland climates fit poorly."],
        ]),
        H("Urban microclimates"),
        D("A **microclimate** is the climate of a small area that differs from the climate around it. The **urban heat island** "
          "(UHI) is the higher air temperature of a city compared with the surrounding countryside. Its **intensity** is the "
          "temperature difference between the warmest part of the city and the rural area.", title="Urban heat island"),
        IMG("algpl1-uhi.svg", alt="Night temperature transect across a city: about 21 degrees in rural areas, a sharp rise (cliff) at the edge, a plateau over the suburbs, a peak near 26 degrees over the central business district, and a dip over a park",
            caption="Figure 1. Urban heat island profile (teaching data)."),
        KEY("Why cities are warmer", "Each cause is a human action; explain how it raises temperature.", cards=[
            ["Surfaces", "Concrete, tar and roofing absorb and store heat by day (low albedo, high heat capacity) and release it at night."],
            ["Less evaporation", "Few plants and quick drainage mean less energy is used for evaporation, so more heats the air."],
            ["Anthropogenic heat", "Vehicles, generators, air-conditioners, industry and people release heat."],
            ["Urban canyons", "Tall buildings trap long-wave radiation between walls and reduce wind, so heat is not carried away."],
            ["Pollution dome", "Smoke and gases absorb outgoing long-wave radiation and re-emit it downward."],
        ]),
        T("The UHI is strongest at night, in calm, clear, anticyclonic weather, because rural areas then cool quickly while the "
          "city releases stored heat. Cities also change other elements: they have lower mean wind speeds but strong gusts "
          "around tall buildings, lower relative humidity, more haze and smog, and sometimes more convectional storms downwind."),
        EX("Worked example 3: heat island intensity", intro="On a calm night the central business district records 27.4 degrees C and a rural station 22.9 degrees C. Find the heat island intensity and suggest two measures to reduce it.", steps=[
            S("Intensity", math=r"27.4 - 22.9 = 4.5\,{}^\circ\text{C}"),
            S("Measure 1", text="Plant trees and create parks: shade and evapotranspiration cool the air (note the dip over the park in Figure 1)."),
            S("Measure 2", text="Use light-coloured roofs and paving with a higher albedo, so less insolation is absorbed."),
        ]),
        MISTAKE("Writing about the whole urban climate when asked about the heat island", "The Board's 2023 report notes that candidates asked how people cause higher urban temperatures drifted into precipitation and humidity. Keep to temperature and explain each human cause."),
        MISTAKE("Saying the heat island is strongest at midday", "It is usually strongest at night under calm, clear skies."),
        QUIZ("A station's coolest month is 24 degrees C and its driest month has 75 mm. What is its Koppen type?",
             ["Af", "Am", "Aw", "BS"], 0,
             "Group A (coolest month above 18 degrees C) and the driest month has 60 mm or more: Af.",
             hint="Check the driest month against 60 mm.",
             feedback=["", "Am needs a driest month below 60 mm.", "Aw needs a driest month below 60 mm and below the Am threshold.", "BS is a dry climate where evaporation exceeds rainfall."]),
        QUIZ("Under which conditions is the urban heat island most intense?",
             ["Windy, cloudy afternoons", "Calm, clear nights", "Rainy mornings", "Any time, with no difference"], 1,
             "Calm, clear nights let rural areas cool quickly while the city releases stored heat.",
             hint="When does the countryside cool fastest?",
             feedback=["Wind mixes the air and cloud reduces cooling, weakening the heat island.", "", "Rain cools surfaces and increases evaporation.", "Intensity varies strongly with weather and time of day."]),
        H("Practice"),
        PQ("Station R (invented for practice): coolest month 22 degrees C; driest month 25 mm; annual total 2 000 mm. Classify it, showing working.", "Group A (coolest month above 18 degrees C). Driest month below 60 mm, so not Af. Am threshold = 100 - 2 000 / 25 = 20 mm. 25 mm is above 20 mm, so the station is Am."),
        PQ("Examine two ways in which human activities are responsible for higher temperatures in urban areas than in the surrounding rural areas.", "1. Building materials such as concrete and tar have a low albedo and high heat capacity: they absorb insolation by day and release it at night, keeping the city warm. 2. Anthropogenic heat from vehicles, generators, air-conditioners and industry adds energy directly. Other valid causes: less vegetation and evaporation, urban canyons, the pollution dome."),
        PQ("Essay plan: 'Assess the value of the Koppen classification of climates.'", "Introduction: purpose and basis (temperature, rainfall, vegetation). Describe groups A to E and how codes are built. Strengths: simple data, objective boundaries, worldwide, links to vegetation. Weaknesses: monthly means, sharp boundaries, ignores causes and other elements, highland climates, vegetation altered by people. Example: classify Cameroonian regions and show where the scheme fits poorly. Judgement: valuable for description and teaching, less for explanation."),
        TIP("Exam link: Paper 1 may ask you to classify a station or name a Koppen group; Paper 2 Section A has included the urban heat island; Paper 3 statistics can ask you to draw and explain a climograph. Keep strictly to temperature when the question names the heat island."),
        SUM("Koppen classifies climates by monthly temperature and rainfall, matched to vegetation.",
            "Groups: A tropical, B dry, C warm temperate, D cold, E polar; Af, Am and Aw depend on the driest month.",
            "Am if the driest month is below 60 mm but at least 100 - annual/25 mm; otherwise Aw.",
            "The urban heat island is caused by surfaces, less evaporation, anthropogenic heat, canyons and pollution.",
            "It is strongest on calm, clear nights; parks, trees and reflective surfaces reduce it."),
    ],
))

# ------------------------------------------------------------------ 13. Global climate change
LESSONS.append(lesson(
    module=M2,
    topic="Global climate change",
    title="Global climate change: evidence, causes, impacts and responses",
    slug="gpl1-global-climate-change",
    minutes=25,
    summary="The Earth's climate has always changed, but recent warming is unusually fast and mainly caused by human greenhouse gas emissions. Learn the evidence, the natural and human causes, impacts on Cameroon and the Sahel, and mitigation and adaptation.",
    objectives=[
        "Describe the evidence for past and present climate change",
        "Explain natural causes of climate change and the enhanced greenhouse effect",
        "Explain the impacts of climate change, with examples from Cameroon and the Sahel",
        "Distinguish mitigation from adaptation and evaluate responses at different scales",
    ],
    key_concepts=["Climate change", "Proxy evidence", "Milankovitch cycles", "Enhanced greenhouse effect", "Carbon dioxide (ppm)",
                  "Positive feedback", "Mitigation", "Adaptation", "Paris Agreement"],
    blocks=[
        H("Introduction"),
        T("Lake Chad, on Cameroon's northern border, has shrunk greatly since the 1960s, and farmers across the Sahel describe "
          "rains that start later and fall more violently. Not every change is caused by global warming (water use and natural "
          "variability matter too), so geographers must weigh the evidence carefully. That weighing of evidence is what A Level "
          "essays on climate change reward."),
        D("**Climate change** is a long-term change in the average pattern of weather (temperature, precipitation, winds) over "
          "decades or longer. **Global warming** is the rise in the average temperature of the Earth's surface and lower "
          "atmosphere.", title="Definitions"),
        H("Evidence"),
        KEY("How we know the climate has changed", "", cards=[
            ["Instrumental records", "Thermometer records since about 1850 show global warming. The Intergovernmental Panel on Climate Change (IPCC) reported that 2011 to 2020 was about 1.1 degrees C warmer than 1850 to 1900."],
            ["Ice cores", "Air bubbles trapped in Antarctic and Greenland ice record past carbon dioxide levels and, through oxygen isotopes, past temperatures over hundreds of thousands of years."],
            ["Other proxies", "Tree rings, pollen in lake sediments, ocean sediment cores and corals record past climates. Ancient lake shorelines in the Sahara show it was much wetter several thousand years ago."],
            ["Present-day signs", "Retreating glaciers, shrinking Arctic sea ice, rising sea level (thermal expansion and melting ice) and earlier seasons in many regions."],
        ]),
        H("Natural causes"),
        KEY("Natural forcing", "These explain most past climate change.", cards=[
            ["Milankovitch cycles", "Slow changes in the Earth's orbit (eccentricity, about 100 000 years), the tilt of its axis (obliquity, about 41 000 years) and the wobble of the axis (precession, roughly 20 000 to 26 000 years) alter the timing and strength of insolation, pacing ice ages."],
            ["Solar output", "Small variations in the sun's energy, including the 11-year sunspot cycle."],
            ["Volcanic eruptions", "Large eruptions inject sulphate aerosols into the stratosphere, reflecting sunlight and cooling the Earth for a year or two."],
            ["Ocean and land changes", "Changes in ocean circulation, and over millions of years the movement of continents, alter heat transfer."],
        ]),
        H("Human causes: the enhanced greenhouse effect"),
        T("Burning coal, oil and gas, deforestation, cement making, rice paddies, cattle and landfill add carbon dioxide, "
          "methane and nitrous oxide to the atmosphere. These gases absorb more of the outgoing long-wave radiation and send part "
          "of it back to the surface, so the natural greenhouse effect is strengthened: the **enhanced greenhouse effect**. "
          "Carbon dioxide has risen from about 280 parts per million (ppm) before the industrial revolution to over 420 ppm today."),
        EX("Worked example 1: percentage increase", intro="Calculate the percentage increase in carbon dioxide from 280 ppm to 420 ppm.", steps=[
            S("Increase", math=r"420 - 280 = 140 \text{ ppm}"),
            S("Percentage", math=r"\frac{140}{280} \times 100 = 50\%"),
        ]),
        D("A **positive feedback** strengthens the original change. Example: warming melts snow and ice, exposing darker land "
          "and sea with a lower albedo, which absorb more insolation and warm further. Warmer air also holds more water vapour, "
          "itself a greenhouse gas.", title="Feedback"),
        T("Scientific assessments by the IPCC conclude that human influence is the main cause of the warming observed since the "
          "mid-twentieth century, because natural factors alone cannot explain its speed and pattern (for example, the "
          "stratosphere is cooling while the troposphere warms, which fits greenhouse forcing rather than a brighter sun)."),
        H("Impacts"),
        KEY("Impacts, global and in Cameroon", "Many local changes have several causes; say so in essays.", cards=[
            ["Sea-level rise", "Threatens low coasts such as the Wouri estuary around Douala with flooding and saltwater intrusion."],
            ["Rainfall and drought", "Sahel rainfall is highly variable; more intense storms and longer dry spells affect farming in the north. Lake Chad's shrinkage reflects both drought and water abstraction for irrigation."],
            ["Health and ecosystems", "Warmer conditions may extend the range of some disease vectors into cooler highlands; species ranges shift upslope."],
            ["Food and water security", "Crop yields, grazing and water supplies become less reliable, with knock-on effects on migration and livelihoods."],
        ]),
        EX("Worked example 2: an essay plan on causes", intro="'Discuss the view that recent climate change is mainly caused by human activity.' Plan the answer.", steps=[
            S("Introduction", text="Define climate change; state that climate has always changed naturally."),
            S("Natural causes", text="Milankovitch cycles act over tens of thousands of years, too slowly for recent change; solar output has not risen since the mid-twentieth century; volcanoes cause only short cooling."),
            S("Human causes", text="Rising greenhouse gases (280 to over 420 ppm CO2), deforestation; the enhanced greenhouse effect; feedbacks."),
            S("Evidence for human cause", text="Speed of warming; the pattern of a warming troposphere and cooling stratosphere; IPCC assessments."),
            S("Judgement", text="Natural factors explain past change, but recent warming is mainly human-caused. Local impacts, such as Lake Chad, combine global change with local water use."),
        ]),
        H("Responses"),
        D("**Mitigation** reduces the causes of climate change: cutting emissions or increasing carbon sinks. **Adaptation** "
          "adjusts to the effects: living with the change.", title="Mitigation and adaptation"),
        T("Mitigation includes renewable energy (Cameroon already draws much of its electricity from hydro-electric power), "
          "energy efficiency, reforestation and protecting forests such as those of the Congo Basin. Adaptation includes "
          "drought-resistant crops, water harvesting, better drainage and flood defences in coastal cities, and early-warning "
          "systems. Internationally, the Kyoto Protocol (1997) set emission targets for rich countries, and the Paris Agreement "
          "(2015) aims to keep warming well below 2 degrees C and to pursue efforts to limit it to 1.5 degrees C, with each "
          "country setting its own targets."),
        MISTAKE("Mixing up the ozone hole and global warming", "Ozone depletion lets in more ultraviolet; global warming is about long-wave radiation and greenhouse gases. They are different problems."),
        MISTAKE("Blaming every local change on global warming", "Weigh other causes, such as over-abstraction, deforestation and natural variability, and say which matters most in the example."),
        QUIZ("Which is an example of adaptation rather than mitigation?",
             ["Building a solar power plant", "Planting drought-resistant millet varieties", "Reducing deforestation", "Taxing carbon emissions"], 1,
             "Drought-resistant crops help people cope with the effects; the others reduce the cause.",
             hint="Does it reduce the cause or cope with the effect?",
             feedback=["Solar power cuts emissions: mitigation.", "", "Protecting forests keeps carbon stored: mitigation.", "A carbon tax aims to cut emissions: mitigation."]),
        QUIZ("Why is the Milankovitch theory not a good explanation of warming since 1950?",
             ["Orbital changes do not affect climate", "Orbital cycles act over tens of thousands of years, far too slowly", "The Earth's orbit has stopped changing", "It explains only cooling"], 1,
             "Orbital cycles change insolation very slowly, so they cannot explain rapid warming over decades.",
             hint="Compare the timescales.",
             feedback=["They clearly pace ice ages.", "", "The orbit changes continuously, but slowly.", "They explain both glacial and interglacial periods."]),
        H("Practice"),
        PQ("Carbon dioxide at a monitoring station rose from 315 ppm to 420 ppm. Calculate the percentage increase to one decimal place.", "Increase = 105 ppm. 105 / 315 x 100 = 33.3%."),
        PQ("Explain one positive feedback that may speed up global warming.", "Ice-albedo feedback: warming melts snow and sea ice, exposing darker land and ocean with a lower albedo. These absorb more insolation, warming the area further and melting more ice."),
        PQ("Suggest two adaptation measures for farmers in northern Cameroon and explain how each helps.", "1. Drought-resistant and early-maturing crop varieties: they can be harvested before the shorter rainy season ends. 2. Water harvesting (small dams, pits, contour bunds): they store runoff from intense storms for dry spells and reduce soil erosion. Others: agroforestry, irrigation, crop insurance and weather information."),
        PQ("Essay plan: 'Evaluate the effectiveness of international agreements in tackling global climate change.'", "Introduction: the global nature of the problem. Kyoto (1997): binding targets for rich countries; limits (major emitters outside or with no targets). Paris (2015): all countries, nationally set targets, 1.5 and 2 degree goals; limits (targets voluntary, current pledges not enough). Role of finance and technology for developing countries. Cameroon's position: low emissions, high vulnerability, forests as sinks. Judgement: agreements have raised awareness and set frameworks, but effectiveness depends on national action."),
        TIP("Exam link: climate change appears in Paper 1, in Paper 2 Section A, and in the Paper 2 section on contemporary environmental and development issues, which the Board's report shows is very popular. Answers need balance: natural and human causes, global and local scales, mitigation and adaptation."),
        SUM("Evidence comes from instrumental records, ice cores, other proxies and present-day changes such as glacier retreat and sea-level rise.",
            "Natural causes: Milankovitch cycles, solar output, volcanic eruptions, ocean changes.",
            "Human emissions have raised CO2 from about 280 to over 420 ppm, enhancing the greenhouse effect.",
            "Impacts include sea-level rise, changing rainfall, drought and food insecurity; local cases often have several causes.",
            "Mitigation reduces causes; adaptation copes with effects; Kyoto (1997) and Paris (2015) are the key agreements."),
    ],
))
