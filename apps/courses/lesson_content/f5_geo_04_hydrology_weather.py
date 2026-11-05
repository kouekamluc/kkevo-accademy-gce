"""Form 5 Geography: Hydrology, Meteorology and Climatology (part 1: the water cycle, atmosphere, weather, condensation).

8 lessons, one practice set each. Figures are KKEVO's own drawings (static/lessons/diagrams/f5g-wx-*.svg).
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Hydrology, Meteorology and Climatology"
HC = "The hydrological cycle"
ATM = "The earth's atmosphere"
WC = "Weather and climate"
FC = "Forms of condensation"

LESSONS = []

# ------------------------------------------------------------------ 1. Global water and the water cycle
LESSONS.append(lesson(
    module=MODULE, topic=HC,
    title="Global water resources and the water cycle",
    slug="wx-global-water-and-the-water-cycle",
    minutes=20,
    summary="Where the earth's water is stored (oceans about 97 percent, fresh water about 3 percent, most of it ice and groundwater) and how the water cycle moves water as a system through evaporation, condensation, precipitation, runoff and infiltration.",
    objectives=[
        "Describe the distribution of global water resources",
        "Define the hydrological (water) cycle",
        "Illustrate the pathways of the water cycle as a system at the global scale",
        "Outline why most of the world's water is not easily available for people",
    ],
    key_concepts=["Hydrosphere", "Fresh water", "Water cycle", "System", "Evaporation", "Transpiration", "Condensation", "Precipitation", "Runoff", "Infiltration"],
    blocks=[
        H("Introduction"),
        T("A fisherman at Limbe launches his canoe on the Atlantic Ocean. Far inland, a farmer near Maroua waits for the first "
          "rain of the season. A woman in Bamenda collects water from a spring. All three depend on the same water."),
        T("The water on earth is used again and again. The rain that falls on Mount Cameroon today may be water that left the sea "
          "last week. Geographers call this movement the **water cycle**. This lesson shows where the water is kept and how it moves."),
        H("Where is the earth's water?"),
        D("The **hydrosphere** is all the water on or near the earth's surface: oceans, ice, groundwater, lakes, rivers, soil moisture "
          "and water vapour in the air.", title="Hydrosphere"),
        T("Most water is salty. The oceans and seas hold **about 97 percent** of all water. Only **about 3 percent** is fresh water, "
          "the kind people can drink and farmers can use."),
        IMG("f5g-wx-global-water.svg",
            alt="Two bars. The top bar shows that oceans hold about 97 percent of water and fresh water about 3 percent. The bottom bar splits fresh water into ice (about two-thirds), groundwater (almost one-third) and a very small share in lakes, soil, rivers and the air.",
            caption="Figure 1. Where the earth's water is stored (approximate shares)."),
        T("Look at the second bar. Of the fresh water, **about two-thirds is locked up as ice** in ice caps and glaciers, far from "
          "most people. **Almost all of the rest is groundwater**, stored underground in rocks and soil."),
        T("Lakes, soil moisture, rivers and the atmosphere together hold **less than 1 percent of the fresh water**. Yet rivers like "
          "the Sanaga and the Benue, and lakes like Lake Chad, are the water that most people actually use."),
        KEY("Orders of magnitude to remember", "Do not memorise long decimals. Remember the size order.", cards=[
            ["Oceans and seas", "By far the largest store: about 97 percent of all water. Salty."],
            ["Ice caps and glaciers", "The largest store of fresh water: about two-thirds of it."],
            ["Groundwater", "The second largest fresh store, found underground."],
            ["Lakes, rivers, soil, air", "Tiny shares, but they are the easiest water to reach."],
        ]),
        TIP("**Exam link.** Paper 1 (multiple choice) often asks for the largest store of water or the largest store of fresh water. "
            "Paper 2 Section B can ask you to describe the distribution of global water resources, usually from a bar chart or pie chart. "
            "Use words such as 'about' and 'most', and name the biggest stores first."),
        H("The water cycle as a system"),
        D("The **hydrological (water) cycle** is the continuous movement of water between the oceans, the atmosphere and the land, "
          "driven by the sun's energy and by gravity.", title="Definition"),
        D("A **system** is a set of parts that are linked together by flows. A system has **stores** (places where water is kept) "
          "and **flows** or **pathways** (the movements between them).", title="System"),
        T("At the **global scale** the water cycle is a **closed system**. Water is moved around inside the system, but almost no "
          "water enters it or leaves it. Only energy from the sun enters. At the scale of a river basin the system is open. "
          "You will study that in the next lesson."),
        KEY("The main pathways", "Each pathway is a process that moves water.", cards=[
            ["Evaporation", "Liquid water becomes water vapour. Most of it comes from the oceans, heated by the sun."],
            ["Transpiration", "Plants lose water vapour through their leaves. A forest or a cocoa farm adds a lot of vapour to the air."],
            ["Condensation", "Water vapour cools and turns back into tiny water droplets. Clouds form."],
            ["Precipitation", "Water falls from clouds as rain, hail, snow or sleet."],
            ["Surface runoff", "Water flows over the land surface into streams and rivers."],
            ["Infiltration", "Water soaks into the soil. Deeper movement down into the rock is percolation."],
            ["Groundwater flow", "Water moves slowly underground and may reach rivers or the sea."],
        ]),
        IMG("f5g-wx-water-cycle.svg",
            alt="A diagram of the water cycle: evaporation arrows rise from the sea, transpiration arrows rise from a tree, clouds form and wind carries vapour inland, precipitation falls on a hill, then surface runoff flows downhill, infiltration goes into the ground and groundwater flows back towards the sea.",
            caption="Figure 2. The global water cycle: sea, air and land."),
        T("The cycle has no real start or end. If you begin at the sea: the sun heats the water, which evaporates. The vapour rises, "
          "cools and condenses into clouds. Winds carry the clouds over the land. Rain falls. Some water runs off and some soaks in. "
          "Both routes lead back to the sea."),
        EX("Worked example 1: describing the water cycle", intro="With the help of a labelled diagram, describe the water cycle. (A model answer, one step for each paragraph.)", steps=[
            S("Draw the diagram first", text="Sketch the sea, a hill and clouds. Label evaporation, transpiration, condensation, precipitation, surface runoff, infiltration and groundwater flow, with arrows. This earns marks quickly."),
            S("Define it", text="The water cycle is the continuous movement of water between the sea, the air and the land, powered by the sun."),
            S("Describe the upward part", text="The sun heats the sea and water evaporates. Plants also release vapour by transpiration. The warm, moist air rises."),
            S("Describe the cloud stage", text="The rising air cools, so the vapour condenses into droplets. Clouds form and the wind blows them over the land."),
            S("Describe the return to the surface", text="Precipitation falls. Some water flows over the ground as surface runoff, and some soaks in by infiltration and moves as groundwater. Rivers and groundwater return the water to the sea."),
        ]),
        EX("Worked example 2: distribution of water", intro="Describe the distribution of the world's water resources. (A model answer.)", steps=[
            S("Point: most water is in the oceans", text="The oceans and seas hold about 97 percent of all water, so only about 3 percent is fresh."),
            S("Point: fresh water is mostly not available", text="About two-thirds of the fresh water is ice in ice caps and glaciers, and most of the rest is groundwater."),
            S("Point: easy water is scarce", text="Rivers, lakes, soil moisture and the atmosphere hold less than 1 percent of the fresh water, although people use these stores most."),
        ]),
        MISTAKE("Saying that fresh water is plentiful", "Fresh water is only about 3 percent of all water, and most of that is ice or deep groundwater. Say that the water people can easily reach is a very small share."),
        MISTAKE("Mixing up evaporation and condensation", "Evaporation: liquid becomes vapour (needs heat, goes UP). Condensation: vapour becomes liquid droplets (needs cooling, forms clouds). Use the memory aid: condensation = clouds."),
        QUIZ("Which store holds the largest share of the earth's fresh water?", ["Rivers and lakes", "Ice caps and glaciers", "The atmosphere", "The oceans"], 1,
             "About two-thirds of all fresh water is ice in ice caps and glaciers. The oceans hold most water but it is salty.",
             hint="The question asks about FRESH water only, so leave out the salty oceans.",
             feedback=["Rivers and lakes are used by many people, but they hold a tiny share of fresh water.", "",
                       "The atmosphere holds only a very small amount of water vapour.", "The oceans hold most of all water, but it is salty, not fresh."]),
        QUIZ("Plants losing water vapour through their leaves is called:", ["Infiltration", "Condensation", "Transpiration", "Precipitation"], 2,
             "Plants release water vapour through their leaves by transpiration.",
             hint="Think of the 'trans' in 'transport' and what leaves do.",
             feedback=["Infiltration is water soaking into the soil.", "Condensation is vapour turning into droplets, as in cloud formation.", "",
                       "Precipitation is water falling from the sky as rain, hail or snow."]),
        PQ("Which store holds about 97 percent of the earth's water?", "The oceans and seas. This water is salty."),
        PQ("Name the process by which water vapour changes into water droplets and forms clouds, and say what must happen to the air for this to occur.", "Condensation. The air must cool (for example when it rises) so that it cannot hold all its vapour."),
        PQ("Explain why the global water cycle is called a closed system.", "Water is moved between the sea, air and land inside the cycle, but almost no water enters or leaves the earth. Only the sun's energy enters. So the same water is recycled."),
        PQ("Draw and label a sketch of the water cycle, showing at least five processes. Describe what happens to rain that falls on a hillside.", "The sketch shows evaporation, transpiration, condensation, precipitation, surface runoff, infiltration and groundwater flow. Rain on a hillside either flows downhill as surface runoff into streams, or soaks into the soil by infiltration and then moves as groundwater. Both routes lead to rivers and then the sea."),
        SUM("About 97 percent of the earth's water is in the oceans. Only about 3 percent is fresh water.",
            "About two-thirds of fresh water is ice and almost all the rest is groundwater. Rivers, lakes, soil moisture and the air hold less than 1 percent of fresh water.",
            "The water cycle is the continuous movement of water between sea, air and land, driven by the sun and gravity.",
            "At the global scale it is a closed system. The main pathways are evaporation, transpiration, condensation, precipitation, surface runoff, infiltration and groundwater flow."),
    ],
))

# ------------------------------------------------------------------ 2. The drainage basin system
LESSONS.append(lesson(
    module=MODULE, topic=HC,
    title="The drainage basin as a system",
    slug="wx-the-drainage-basin-system",
    minutes=22,
    summary="The drainage basin (catchment) with its watershed, river, tributaries, source, confluence and mouth, and how it works as an open system with inputs, stores, flows and outputs.",
    objectives=[
        "Define a drainage basin and name its parts (watershed, river, tributary, source, confluence, mouth)",
        "Illustrate the water cycle at the drainage basin scale as an open system",
        "Describe the main inputs, outputs, flows and storages of a drainage basin",
        "Explain how vegetation and soil affect the flow of water in a basin",
    ],
    key_concepts=["Drainage basin", "Watershed", "Tributary", "Confluence", "Open system", "Interception", "Stemflow", "Throughflow", "Surface runoff", "Groundwater flow"],
    blocks=[
        H("Introduction"),
        T("Rain that falls on the Adamawa plateau does not stay there. Some of it flows into streams that join other streams, "
          "and in the end it reaches the sea. The Benue, for example, flows out of Cameroon and joins the River Niger in Nigeria."),
        T("Every river is fed by the land around it. The area of land that feeds one river is called its **drainage basin**. "
          "Understanding the basin helps us to explain floods, droughts, and the work of dams like the one at Lagdo on the Benue."),
        H("Parts of a drainage basin"),
        D("A **drainage basin** (or **catchment area**) is the area of land drained by a river and its tributaries.", title="Drainage basin"),
        D("The **watershed** is the high ground, an imaginary line along ridges or hills, that separates one drainage basin from the next. "
          "Rain that falls on one side flows into one river. Rain that falls on the other side flows into a different river.", title="Watershed"),
        IMG("f5g-wx-basin-plan.svg",
            alt="Plan view of a drainage basin. A dashed line shows the watershed. A main river runs from its source at the top to its mouth at the sea. Three tributaries join the main river, one at a confluence.",
            caption="Figure 1. A drainage basin seen from above (a general sketch, not a real place)."),
        KEY("Words for the parts of a river system", "Learn these and label them on your sketches.", cards=[
            ["Source", "Where a river begins, often in highland."],
            ["Tributary", "A smaller river or stream that flows into a larger river."],
            ["Confluence", "The point where two rivers meet."],
            ["Mouth", "Where a river ends, at the sea or a lake."],
            ["Channel", "The path along which the river flows, between its banks."],
        ]),
        H("The basin as an open system"),
        T("A drainage basin is an **open system**. Water and energy cross its boundary: rain comes in from the atmosphere, and water "
          "leaves by evaporation and by the river flowing out to the sea. In the global cycle the system is closed. In a basin it is open."),
        IMG("f5g-wx-basin-system.svg",
            alt="Cross-section of a hillside drainage basin. Precipitation falls on a tree and the ground. Arrows show stemflow, throughfall, infiltration, percolation, surface runoff, throughflow and groundwater flow towards a river. Evaporation and transpiration leave upwards. River flow leaves to the sea.",
            caption="Figure 2. Inputs, outputs, stores and flows in a drainage basin."),
        KEY("Inputs and outputs", "These cross the boundary of the basin.", cards=[
            ["Input: precipitation", "Rain, hail or snow falling on the basin. This is the main input."],
            ["Output: evaporation", "Water vapour lost from the ground and from water surfaces."],
            ["Output: transpiration", "Water vapour lost from plants."],
            ["Output: river flow", "Water carried by the river out of the basin, to the sea or a lake."],
        ]),
        KEY("Stores", "Places where water is held for some time inside the basin.", cards=[
            ["Interception store", "Water held on leaves and branches. Some evaporates without ever reaching the ground."],
            ["Surface storage", "Puddles, ponds and lakes."],
            ["Soil moisture store", "Water held in the soil, used by plant roots."],
            ["Groundwater store", "Water held in the pores and cracks of rock below the water table."],
        ]),
        KEY("Flows", "Movements of water inside the basin.", cards=[
            ["Stemflow", "Water running down the trunks and stems of plants."],
            ["Throughfall", "Rain that drips through leaves or falls between them."],
            ["Infiltration and percolation", "Water soaking into the soil (infiltration) and moving deeper into the rock (percolation)."],
            ["Surface runoff", "Water flowing over the ground. This is the fastest flow, and the main cause of flash floods."],
            ["Throughflow", "Water moving sideways through the soil, towards the river."],
            ["Groundwater flow", "Very slow movement of water through the rock below the water table. It feeds rivers in the dry season."],
        ]),
        TIP("**Exam link.** Paper 2 Section B often asks you to draw and label a drainage basin or to explain inputs, outputs, flows and stores. "
            "Draw the cross-section and give each label a one-line meaning. A good answer says which flows are fast (surface runoff) and which are slow (groundwater flow)."),
        H("How the basin responds to rain"),
        T("The path water takes decides how fast it reaches the river. Surface runoff is fast. Water that infiltrates and flows as "
          "groundwater takes days, weeks or longer. This is why a river can still flow in the dry season: groundwater keeps feeding it."),
        T("Vegetation slows the water. Leaves intercept rain, roots hold the soil open so that more water infiltrates, and transpiration "
          "returns water to the air. When forest is cleared, more rain runs off quickly and floods become more likely. Bare, hard or built-up "
          "ground (such as concrete in a town) has the same effect."),
        EX("Worked example 1: defining and drawing", intro="Define a drainage basin. With the aid of a diagram, name three of its features. (A model answer.)", steps=[
            S("Define", text="A drainage basin is the area of land that is drained by a river and its tributaries."),
            S("Draw", text="Draw a plan view: a dashed watershed line around a river with one or two tributaries, and the sea at the bottom."),
            S("Name features", text="Label the source (where the river starts), a tributary (a small river joining the main river), the confluence (where they meet), the mouth (where the river reaches the sea) and the watershed (the boundary of the basin)."),
        ]),
        EX("Worked example 2: tracing the water", intro="Describe what can happen to rain that falls on a forested hillside in a drainage basin. (A model answer.)", steps=[
            S("Interception", text="Some rain is caught on leaves and branches (interception store). Part of it evaporates straight back to the air."),
            S("Reaching the ground", text="The rest reaches the ground as throughfall or by stemflow down the trunks."),
            S("On or in the ground", text="Some water infiltrates into the soil and some flows over the surface as surface runoff. Water in the soil moves sideways as throughflow, or downwards by percolation to the groundwater store."),
            S("Leaving the basin", text="Surface runoff, throughflow and groundwater flow all reach the river. The river carries the water out of the basin. Transpiration and evaporation return some water to the air."),
        ]),
        MISTAKE("Mixing up throughflow and groundwater flow", "Throughflow is sideways movement of water through the soil, near the surface. Groundwater flow is movement through the rock below the water table. Throughflow is faster."),
        MISTAKE("Writing 'watershed' for the river", "The watershed is the boundary (high ground) around the basin, not a river and not an area of water."),
        QUIZ("What is the line of high ground that separates two drainage basins called?", ["Confluence", "Tributary", "Watershed", "Mouth"], 2,
             "The watershed is the boundary between two basins. Rain on either side flows to different rivers.",
             hint="It is a boundary, not a river and not a place where rivers meet.",
             feedback=["The confluence is where two rivers meet.", "A tributary is a smaller river that joins a larger one.", "", "The mouth is where a river ends, at the sea or a lake."]),
        QUIZ("Which flow is the fastest way for water to reach a river after heavy rain?", ["Groundwater flow", "Percolation", "Surface runoff", "Infiltration"], 2,
             "Surface runoff moves over the ground and reaches the river quickly, so it causes flash floods.",
             hint="Which flow takes place on top of the ground, not inside it?",
             feedback=["Groundwater flow is very slow.", "Percolation is a slow movement down into rock.", "", "Infiltration is water soaking into the ground, which delays its arrival in the river."]),
        PQ("Define a drainage basin.", "A drainage basin is the area of land drained by a river and its tributaries. It is bounded by a watershed."),
        PQ("State two inputs and two outputs of a drainage basin.", "Inputs: precipitation (rain, hail, snow). Outputs: any two of evaporation, transpiration and river flow to the sea."),
        PQ("Explain how forest clearance can make floods more likely in a drainage basin.", "Fewer leaves means less interception, and fewer roots means less infiltration. So more rain runs off the surface quickly as surface runoff and reaches the river at the same time. The river rises faster and floods."),
        PQ("Draw a labelled cross-section of a drainage basin showing the input, three stores, three flows and the outputs.", "The sketch shows precipitation (input); the interception store, soil moisture store and groundwater store; infiltration, surface runoff and throughflow (or other flows) with arrows; and evaporation, transpiration and river flow as outputs."),
        SUM("A drainage basin is the area drained by a river and its tributaries. The watershed is its boundary.",
            "Learn the parts of a river system: source, tributary, confluence, mouth and channel.",
            "A basin is an open system. Inputs: precipitation. Outputs: evaporation, transpiration and river flow.",
            "Stores: interception, surface storage, soil moisture and groundwater. Flows: stemflow, throughfall, infiltration, percolation, surface runoff, throughflow, groundwater flow.",
            "Surface runoff is fast and groundwater flow is slow. Vegetation slows water and reduces flood risk."),
    ],
))


# ------------------------------------------------------------------ 3. Structure of the atmosphere
LESSONS.append(lesson(
    module=MODULE, topic=ATM,
    title="The structure of the atmosphere",
    slug="wx-structure-of-the-atmosphere",
    minutes=20,
    summary="What the atmosphere is, its four layers (troposphere, stratosphere, mesosphere, thermosphere), the main features of the troposphere and stratosphere, and why the atmosphere matters to life.",
    objectives=[
        "Define the atmosphere",
        "Draw the structure of the atmosphere",
        "Outline the main characteristics of the troposphere and the stratosphere",
        "Explain why the atmosphere is important to life on earth",
    ],
    key_concepts=["Atmosphere", "Troposphere", "Tropopause", "Stratosphere", "Ozone layer", "Mesosphere", "Thermosphere"],
    blocks=[
        H("Introduction"),
        T("Climb Mount Cameroon from the warm coast near Limbe and the air becomes cooler at every step. By the summit, "
          "more than 4000 metres up, it is much colder than on the beach. The air itself is changing as you go higher."),
        T("The air that surrounds the earth is the **atmosphere**. We live at the very bottom of it. "
          "In this lesson you will learn how it is built, in layers, and why it protects us."),
        H("What is the atmosphere?"),
        D("The **atmosphere** is the layer of gases that surrounds the earth. It is held in place by gravity.", title="Definition"),
        T("Dry air is mostly **nitrogen (about 78 percent)** and **oxygen (about 21 percent)**. The rest is small amounts of other gases, "
          "such as argon and carbon dioxide. The air also holds **water vapour**, which varies from place to place and is the source of clouds and rain."),
        T("Air is thickest at the earth's surface and thins out with height. There is no sharp upper edge: the atmosphere fades gradually "
          "into space. Most of the air is within the lowest few kilometres."),
        H("The four layers"),
        T("Scientists divide the atmosphere into layers by the way **temperature changes with height**. From the ground upwards, the "
          "layers are the troposphere, the stratosphere, the mesosphere and the thermosphere. The boundary between two layers is called a "
          "'pause', for example the tropopause."),
        IMG("f5g-wx-atmosphere-layers.svg",
            alt="A column of four layers: troposphere (to about 12 km), stratosphere (to about 50 km) with the ozone layer inside, mesosphere (to about 85 km) and thermosphere. A graph shows temperature falling, rising, falling and rising again through the four layers.",
            caption="Figure 1. Layers of the atmosphere and how temperature changes with height. Heights and temperatures are approximate."),
        TIP("When you draw the atmosphere in an exam: draw a tall column, mark the four layers with straight boundary lines, label the heights "
            "(about 12 km, 50 km, 85 km), and name the three 'pauses'. Add one note about temperature in each layer. The heights are averages and vary with place and season."),
        KEY("The troposphere", "The layer we live in.", cards=[
            ["Height", "From the ground to about 12 km on average. It is thicker over the equator (about 16 km) and thinner over the poles (about 8 km)."],
            ["Temperature", "Falls with height, about 6 °C for every 1000 m. The top is very cold, about minus 55 °C."],
            ["Contents", "Holds most of the air and nearly all of the water vapour and clouds."],
            ["Weather", "All the weather takes place here: rain, wind, storms. Air rises and sinks easily."],
            ["Top", "The boundary above is the tropopause."],
        ]),
        KEY("The stratosphere", "The layer above the troposphere, up to about 50 km.", cards=[
            ["Temperature", "Stays cold at first, then rises with height up to about 0 °C at the top."],
            ["Why it warms", "The ozone layer absorbs harmful ultraviolet (UV) rays from the sun, and this warms the air."],
            ["Ozone layer", "A zone with more ozone gas, in the lower part of the stratosphere, roughly 15 to 35 km up."],
            ["Weather", "Very little: the air is dry and calm, with few clouds. Jets often fly near the bottom of it to avoid storms."],
        ]),
        T("The two upper layers are less important for this syllabus. In the **mesosphere** (to about 85 km) temperature falls again, and it "
          "is the coldest layer. Meteors burn up here. In the **thermosphere** (above about 85 km) temperature rises, because the very thin air "
          "absorbs strong energy from the sun."),
        D("The **ozone layer** is a zone in the stratosphere that contains ozone gas. It absorbs most of the sun's harmful ultraviolet rays.", title="Ozone layer"),
        H("Why the atmosphere matters"),
        T("The atmosphere makes life on earth possible. It gives us oxygen to breathe and carbon dioxide for plants. "
          "It acts like a blanket that keeps the earth warm at night. It supplies the water vapour for clouds and rain, which farmers across Cameroon depend on. "
          "The ozone layer protects us from UV rays, and the air burns up most meteors before they reach the ground."),
        TIP("**Exam link.** Paper 1 asks short factual questions such as 'In which layer does most weather occur?' or 'Which layer contains ozone?'. "
            "Paper 2 Section B can ask for a labelled sketch of the layers and a description of the troposphere and stratosphere."),
        EX("Worked example 1: draw and describe", intro="Draw a labelled diagram of the atmosphere and describe the troposphere. (A model answer.)", steps=[
            S("Diagram", text="A column with four layers: troposphere (0 to about 12 km), stratosphere (to about 50 km), mesosphere (to about 85 km), thermosphere (above). Mark the tropopause, stratopause and mesopause."),
            S("Height and contents", text="The troposphere is the lowest layer. It holds most of the air and almost all of the water vapour."),
            S("Temperature", text="Temperature falls with height, by about 6 °C per 1000 m, to about minus 55 °C at the top."),
            S("Weather", text="All weather happens here, because the air mixes, rises and cools to form cloud and rain."),
        ]),
        EX("Worked example 2: stratosphere and ozone", intro="Outline the main characteristics of the stratosphere. (A model answer.)", steps=[
            S("Position", text="It lies above the troposphere, between about 12 km and 50 km."),
            S("Temperature", text="Temperature rises with height, because ozone absorbs ultraviolet rays and warms the air."),
            S("Ozone layer", text="The ozone layer is in this layer and protects living things from the sun's harmful ultraviolet rays."),
            S("Weather", text="The air is calm and dry, with very little cloud and no real weather."),
        ]),
        MISTAKE("Saying that temperature always falls with height", "It falls only in the troposphere and mesosphere. It rises in the stratosphere (ozone absorbs UV) and thermosphere."),
        MISTAKE("Putting weather and clouds in the stratosphere", "Nearly all weather is in the troposphere. The stratosphere is dry and calm."),
        MISTAKE("Mixing up the ozone layer and the greenhouse effect", "The ozone layer in the stratosphere blocks UV rays. The 'blanket' that keeps the earth warm is the greenhouse effect of gases in the lower atmosphere. They are different things."),
        QUIZ("In which layer of the atmosphere does most weather occur?", ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], 1,
             "The troposphere holds most air, vapour and cloud. Rain, wind and storms all occur there.",
             hint="It is the layer closest to the ground.",
             feedback=["The stratosphere is dry and calm with very few clouds.", "", "The mesosphere is much higher, where meteors burn up.", "The thermosphere is the outer layer, with very thin air."]),
        QUIZ("What happens to the temperature in the stratosphere as height increases?", ["It falls", "It stays exactly the same", "It rises", "It rises then falls to below minus 100 °C"], 2,
             "It rises, because ozone absorbs ultraviolet rays and warms the air.",
             hint="Think about what the ozone layer does with the sun's rays.",
             feedback=["Temperature falls with height in the troposphere, not in the stratosphere.", "It is cold at the bottom and warmer at the top, so it is not constant.", "", "That is not the pattern in the stratosphere."]),
        PQ("Define the atmosphere.", "The atmosphere is the layer of gases (mainly nitrogen and oxygen) that surrounds the earth, held in place by gravity."),
        PQ("Name the four layers of the atmosphere in order, from the ground upwards.", "Troposphere, stratosphere, mesosphere, thermosphere."),
        PQ("State three characteristics of the troposphere.", "Any three: it is the lowest layer (up to about 12 km); temperature falls with height (about 6 °C per 1000 m); it holds most air and nearly all water vapour and cloud; all weather happens here."),
        PQ("Explain why the stratosphere gets warmer with height. State one reason why the atmosphere is important to people.", "The ozone layer in the stratosphere absorbs ultraviolet rays and this heats the air. The atmosphere gives us oxygen to breathe, protects us from UV rays, and supplies the water vapour for rain."),
        SUM("The atmosphere is the layer of gases around the earth, mostly nitrogen (about 78 percent) and oxygen (about 21 percent).",
            "The four layers are the troposphere, stratosphere, mesosphere and thermosphere, separated by the tropopause, stratopause and mesopause.",
            "Troposphere: lowest layer, temperature falls with height, holds most air and water vapour, all weather.",
            "Stratosphere: temperature rises with height, contains the ozone layer, calm and dry.",
            "The atmosphere supplies oxygen and rain, keeps the earth warm, and the ozone layer shields us from UV rays."),
    ],
))

# ------------------------------------------------------------------ 4. Weather versus climate
LESSONS.append(lesson(
    module=MODULE, topic=WC,
    title="Weather and climate, and the weather elements",
    slug="wx-weather-versus-climate-and-weather-elements",
    minutes=18,
    summary="The difference between weather and climate, and the main weather elements (temperature, rainfall, pressure, wind, humidity, sunshine, cloud) with their units and instruments.",
    objectives=[
        "Differentiate between weather and climate (meaning and characteristics)",
        "Identify the main weather elements",
        "State the unit and the instrument used for each weather element",
        "Use examples from Cameroon to illustrate weather and climate",
    ],
    key_concepts=["Weather", "Climate", "Weather elements", "Temperature", "Rainfall", "Atmospheric pressure", "Wind", "Humidity", "Sunshine", "Cloud cover"],
    blocks=[
        H("Introduction"),
        T("A student in Douala says, 'It rained heavily this afternoon.' Her cousin in Maroua replies, 'Here it is dry and hot today.' "
          "They are talking about the **weather** on one day."),
        T("The same student also says, 'Douala is wet for most of the year, and Maroua has a long dry season.' This is a statement about "
          "**climate**. Weather and climate are connected, but they are not the same thing."),
        H("Weather and climate"),
        D("**Weather** is the condition of the atmosphere at a particular place and time. It describes what the atmosphere is like over a short time: "
          "an hour, a day or a week.", title="Weather"),
        D("**Climate** is the average weather of a place over a long period. The usual period is at least 30 years.", title="Climate"),
        KEY("Weather compared with climate", "Learn these contrasts for the exam.", cards=[
            ["Time", "Weather: short term (hours, days). Climate: long term (average over about 30 years)."],
            ["Change", "Weather changes quickly, even in one day. Climate changes very slowly."],
            ["Description", "Weather is described as it happens: 'hot and sunny today'. Climate is described by averages and patterns: 'hot, wet, with a dry season'."],
            ["Area", "Weather is for one place and moment. Climate describes the typical conditions of a larger region."],
            ["Example", "Weather: a storm over Buea on Tuesday. Climate: Buea's wet climate, with heavy rain for most of the year."],
        ]),
        H("The weather elements"),
        D("The **weather elements** are the measurable parts of the atmosphere that together make up the weather.", title="Weather elements"),
        CODE("""Element            Unit               Instrument
Temperature        degrees Celsius    Maximum-minimum thermometer
Rainfall           millimetres (mm)   Rain gauge
Air pressure       hectopascals (hPa) Barometer
Wind direction     compass direction  Wind vane
Wind speed         km/h or m/s        Anemometer
Humidity           percent (%)        Hygrometer (wet and dry bulb)
Sunshine           hours              Sunshine recorder
Cloud cover        oktas (eighths)    Observation by eye""", "text", title="Table 1. Weather elements, units and instruments"),
        T("**Temperature** is how hot or cold the air is. **Rainfall** is the amount of water that falls from the sky. "
          "**Air pressure** is the weight of the air pressing on the surface. **Wind** is moving air: we measure its direction and its speed. "
          "**Humidity** is the amount of water vapour in the air. **Sunshine** is the number of hours of bright sun. **Cloud cover** is how much of the sky is covered by cloud."),
        T("The next lesson describes the instruments in detail. You should remember the table above."),
        TIP("**Exam link.** Paper 1 often asks you to match an element to an instrument, or to say whether a statement describes weather or climate. "
            "Paper 2 Section B can ask 'Differentiate between weather and climate' for a few marks, so learn the two definitions and at least three differences."),
        EX("Worked example 1: differentiating", intro="Differentiate between weather and climate. (A model answer.)", steps=[
            S("Define weather", text="Weather is the state of the atmosphere at a place at a particular time, over a short period such as a day."),
            S("Define climate", text="Climate is the average weather of a place over a long period, usually 30 years or more."),
            S("Contrast change", text="Weather changes from hour to hour and day to day. Climate changes only slowly over many years."),
            S("Give examples", text="'Heavy rain in Douala this morning' is weather. 'Douala has a hot, wet climate' is climate."),
        ]),
        EX("Worked example 2: weather or climate?", intro="Say whether each statement is about weather or climate: (a) 'Bamenda was foggy at 7 a.m. today.' (b) 'Maroua has one short rainy season and a long dry season.' (c) 'Yesterday's maximum temperature in Garoua was higher than today's.'", steps=[
            S("(a)", text="Weather: it describes one place at one time (7 a.m. today)."),
            S("(b)", text="Climate: it describes a pattern that repeats every year."),
            S("(c)", text="Weather: it compares two particular days."),
        ]),
        MISTAKE("Calling a single hot day 'the climate'", "One day, one week or even one year is weather. Climate needs a long record, about 30 years, to find the average."),
        MISTAKE("Mixing up the instruments", "Rain gauge = rainfall. Barometer = pressure. Hygrometer = humidity. Anemometer = wind speed. Wind vane = wind direction. A thermometer is for temperature only."),
        MISTAKE("Giving the wrong unit for rainfall", "Rainfall is measured in millimetres, not centimetres or litres. Temperature is in degrees Celsius."),
        QUIZ("Which statement describes climate?", ["It is raining in Kribi now.", "Last Monday was hot and dry in Garoua.", "Yaounde has a hot, humid climate with two rainy seasons.", "Tomorrow's maximum temperature will be 30 °C."], 2,
             "Statement C describes the typical, repeated pattern of a place over many years.",
             hint="Look for the statement that describes a long-term pattern, not one day.",
             feedback=["That is weather: one place at one moment.", "That is weather: a particular day.", "", "That is a weather forecast for one day."]),
        QUIZ("Which instrument measures air pressure?", ["Hygrometer", "Anemometer", "Barometer", "Rain gauge"], 2,
             "A barometer measures air pressure, in hectopascals.",
             hint="Its name starts with 'baro', from a Greek word meaning weight.",
             feedback=["A hygrometer measures humidity.", "An anemometer measures wind speed.", "", "A rain gauge measures rainfall."]),
        PQ("Define weather and climate.", "Weather is the state of the atmosphere at a place at a particular time (short term). Climate is the average weather of a place over a long period, usually at least 30 years."),
        PQ("List five weather elements.", "Any five of: temperature, rainfall, air pressure, wind (direction and speed), humidity, sunshine, cloud cover."),
        PQ("Name the instrument used to measure (a) rainfall, (b) wind speed, (c) humidity.", "(a) Rain gauge, (b) anemometer, (c) hygrometer (wet and dry bulb thermometers)."),
        PQ("Give three differences between weather and climate.", "Weather is short term, climate is long term (about 30 years or more). Weather changes quickly, climate changes slowly. Weather is the actual condition at a time, climate is the average pattern. Weather example: rain in Douala today. Climate example: Douala is wet for most of the year."),
        SUM("Weather is the state of the atmosphere at a place and time (short term). Climate is the average weather over a long period, about 30 years or more.",
            "Weather changes quickly. Climate changes slowly and is described by averages and patterns.",
            "The main weather elements are temperature, rainfall, pressure, wind, humidity, sunshine and cloud cover.",
            "Know the unit and instrument for each: thermometer, rain gauge, barometer, wind vane, anemometer, hygrometer, sunshine recorder."),
    ],
))


# ------------------------------------------------------------------ 5. Weather instruments
LESSONS.append(lesson(
    module=MODULE, topic=WC,
    title="Weather instruments and the Stevenson screen",
    slug="wx-weather-instruments-and-the-stevenson-screen",
    minutes=22,
    summary="How each weather instrument (max-min thermometer, rain gauge, barometer, wind vane, anemometer, hygrometer, sunshine recorder) is used and read, why the Stevenson screen is built as it is, and how to site a school weather station.",
    objectives=[
        "Describe the main weather instruments and the element each one measures",
        "Describe how each instrument is used to collect and record information",
        "Explain why a Stevenson screen is built the way it is",
        "Outline the rules for choosing the site of a school weather station",
    ],
    key_concepts=["Maximum-minimum thermometer", "Rain gauge", "Barometer", "Wind vane", "Anemometer", "Hygrometer", "Sunshine recorder", "Stevenson screen"],
    blocks=[
        H("Introduction"),
        T("Many farmers in the Western Highlands say that they can feel when rain is coming. A feeling is not a measurement. "
          "A school weather station can measure the weather every day with simple instruments, and a record kept over years shows the climate of the town."),
        T("In this lesson you will learn how each instrument works, how to read it, and where to put it so that the readings are fair."),
        H("Temperature, rainfall and wind instruments"),
        IMG("f5g-wx-instruments-1.svg",
            alt="Four instruments: a rain gauge with funnel, bottle and measuring cylinder; a maximum-minimum U-shaped thermometer with two index markers; a wind vane with a head and a tail; a cup anemometer with three cups.",
            caption="Figure 1. A rain gauge, a maximum-minimum thermometer, a wind vane and a cup anemometer."),
        KEY("Maximum-minimum thermometer", "Measures the highest and lowest temperature since it was last set.", cards=[
            ["How it works", "A U-shaped tube holds liquid. As the liquid moves, it pushes small index markers. The markers stay at the highest and lowest points."],
            ["How to read it", "Read the bottom of the marker on the maximum side for the highest temperature and on the minimum side for the lowest."],
            ["How to reset", "Use a small magnet to bring each marker back to touch the liquid. Then record the readings at the same time every day."],
            ["Unit", "Degrees Celsius (°C)."],
        ]),
        KEY("Rain gauge", "Measures how much rain has fallen.", cards=[
            ["How it works", "Rain falls into a funnel and runs into a bottle. The funnel makes the collecting area known, and the bottle stops evaporation."],
            ["How to read it", "Pour the water into a measuring cylinder made for that funnel. Read the scale at eye level, at the bottom of the curved water surface."],
            ["How to record", "Do it at the same time every day, then empty the bottle. The unit is millimetres (mm)."],
            ["Meaning of 1 mm", "1 mm of rain is 1 litre of water on every square metre of ground."],
        ]),
        KEY("Wind vane and anemometer", "Wind has direction and speed.", cards=[
            ["Wind vane", "A pointer that swings freely. The head turns into the wind. So it points to the direction the wind comes FROM. A west wind comes from the west."],
            ["Anemometer", "Cups catch the wind and spin. The faster they spin, the stronger the wind. A dial or counter shows the speed in km/h or metres per second."],
            ["Siting", "Place both high and in the open, away from walls and trees that block or change the wind."],
        ]),
        H("Pressure, humidity, sunshine and cloud"),
        IMG("f5g-wx-instruments-2.svg",
            alt="Four panels: an aneroid barometer dial with a needle, a wet-and-dry bulb hygrometer with two thermometers and a water bottle, a sunshine recorder with a glass ball and a burnt card, and circles showing cloud cover from 0 to 8 oktas.",
            caption="Figure 2. A barometer, a hygrometer, a sunshine recorder and the oktas scale for cloud cover."),
        KEY("Barometer", "Measures air pressure.", cards=[
            ["How it works", "An aneroid barometer contains a sealed metal box. When air pressure changes, the box changes shape and moves a needle."],
            ["How to read it", "Tap the glass gently, then read the needle against the scale in hectopascals (hPa)."],
            ["What it tells us", "Average pressure at sea level is about 1013 hPa. A steady rise usually means fair weather, and a quick fall often means cloud and rain are coming."],
        ]),
        KEY("Hygrometer (wet and dry bulb)", "Measures humidity.", cards=[
            ["How it works", "Two thermometers stand side by side. One bulb is dry. The other is wrapped in a wet wick, which dips into water."],
            ["Why the wet bulb is cooler", "Water evaporates from the wick and cools the bulb. In dry air more water evaporates, so the wet bulb reads lower."],
            ["How to read it", "Read both thermometers and find the difference. Use tables to turn the difference into relative humidity (%). No difference means the air is full of water vapour (100 percent)."],
        ]),
        KEY("Sunshine recorder and cloud cover", "Sunshine in hours, cloud in oktas.", cards=[
            ["Sunshine recorder", "A glass ball focuses bright sun and burns a mark on a card. The length of the burnt line shows the hours of sunshine. The card is changed each day."],
            ["Cloud cover", "Judged by eye. Divide the sky into 8 parts. 0 oktas is clear sky and 8 oktas is completely covered."],
        ]),
        H("The Stevenson screen"),
        IMG("f5g-wx-stevenson-screen.svg",
            alt="A white wooden box on four legs standing on short grass, with a double roof, slatted sides and a door. Labels explain each feature, and an arrow shows the box stands about 1.25 metres above the ground.",
            caption="Figure 3. A Stevenson screen."),
        D("A **Stevenson screen** is a white, louvred wooden box on legs. It holds thermometers and a hygrometer. It shelters them from sun, rain and wind but lets the outside air flow through.", title="Stevenson screen"),
        T("Every feature has a reason. Remember them as pairs: feature and purpose."),
        KEY("Why it is built this way", "Feature and purpose.", cards=[
            ["White paint", "Reflects sunlight, so the box does not heat up and give false readings."],
            ["Louvred (slatted) sides", "Let air move freely through the box, so the thermometers read the real air temperature. They also keep out rain and direct sun."],
            ["Double roof", "Stops the sun from heating the inside. Air can pass between the two layers."],
            ["Legs, about 1.25 m high", "Keep the instruments clear of the hot ground, at a standard height so readings from different places can be compared."],
            ["Door facing away from the sun", "The observer's body and the sun do not heat the thermometers when the door is opened. In the northern hemisphere the door faces north."],
        ]),
        H("Choosing a site for a school weather station"),
        T("A good site is flat, open ground with short grass. Keep it away from trees, walls and buildings: they shade the instruments, block wind and rain, "
          "and make heat. Do not place it on concrete or tarmac, because these heat up in the sun. Fence it so that children and animals stay out, "
          "but keep it easy to reach so that readings are taken at the same time every day."),
        TIP("**Exam link.** Paper 1 asks which instrument measures which element, and why the Stevenson screen is white or louvred. "
            "Paper 2 Section B can ask you to describe an instrument and how it is used to collect and record information, so learn one clear sentence for how it works and one for how it is read."),
        EX("Worked example 1: describing an instrument", intro="Describe how a rain gauge is used to measure rainfall. (A model answer.)", steps=[
            S("Set it up", text="The gauge is placed in an open space, away from trees and buildings, with the funnel above the ground so that splashes do not enter."),
            S("How it collects", text="Rain falls into the funnel and runs into the collecting bottle below."),
            S("How it is read", text="At the same time each day, the water is poured into a measuring cylinder and read at eye level in millimetres."),
            S("How it is recorded", text="The reading is written in a record table. The bottle is emptied and replaced."),
        ]),
        EX("Worked example 2: Stevenson screen", intro="Explain why a Stevenson screen is painted white and has louvred sides. (A model answer.)", steps=[
            S("White paint", text="White reflects sunlight. If it were dark, the screen would absorb heat and the thermometers would read too high."),
            S("Louvred sides", text="The slats allow air to flow through, so the temperature inside is the same as the air outside."),
            S("Rain and sun kept out", text="The slats slope downwards, so rain and direct sunshine cannot reach the instruments."),
        ]),
        MISTAKE("Saying the wind vane points where the wind is going", "A wind vane points INTO the wind. Wind direction is named by where the wind comes from."),
        QUIZ("Why is a Stevenson screen painted white?", ["It looks cleaner", "It reflects sunlight so the inside does not become too hot", "It keeps the rain out", "It attracts the wind"], 1,
             "White reflects sunlight. This keeps the air inside at the true air temperature.",
             hint="Think about what a dark colour does in the sun.",
             feedback=["Appearance is not the reason.", "", "Rain is kept out by the roof and louvres, not the paint.", "Paint colour has no effect on wind."]),
        QUIZ("A wind vane has its head pointing towards the north-west. From which direction is the wind blowing?", ["South-east", "North-west", "North-east", "South-west"], 1,
             "The head of a wind vane points into the wind, so the wind comes from the north-west.",
             hint="The head points INTO the wind.",
             feedback=["That is where the wind is going, not where it comes from.", "", "The head points north-west, not north-east.", "The head points north-west, not south-west."]),
        PQ("Name the instrument used to measure (a) the highest and lowest temperature in a day, (b) air pressure, (c) wind speed.", "(a) Maximum-minimum thermometer, (b) barometer, (c) anemometer."),
        PQ("In what unit is rainfall measured, and what does 1 mm of rain mean?", "Millimetres (mm). 1 mm of rain is 1 litre of water on every square metre of ground."),
        PQ("Explain how a wet and dry bulb hygrometer shows how humid the air is.", "Water evaporates from the wet bulb's wick and cools it. In dry air more water evaporates, so the wet bulb reads much lower than the dry bulb. In humid air the two readings are close. The difference between the readings is used with tables to find the relative humidity."),
        PQ("Describe where and how you would site a school weather station.", "Choose flat, open ground with short grass, away from trees, walls and buildings. Avoid concrete and tarmac. Fence it for safety but keep it accessible. Put the Stevenson screen on legs about 1.25 m high with the door facing away from the sun, and take readings at the same time each day."),
        SUM("Each element has its own instrument: max-min thermometer, rain gauge, barometer, wind vane, anemometer, hygrometer, sunshine recorder.",
            "Rainfall is read in mm from the measuring cylinder. Pressure is read in hPa. Wind vane shows where the wind comes FROM.",
            "The wet and dry bulb difference gives humidity. The sunshine recorder burns a mark on a card. Cloud is judged in oktas.",
            "The Stevenson screen is white, louvred, double-roofed, on legs, with the door facing away from the sun. All of this protects the readings.",
            "A good site is open, flat, grassed, away from buildings and trees, and read at the same time every day."),
    ],
))

# ------------------------------------------------------------------ 6. Recording and presenting weather data
LESSONS.append(lesson(
    module=MODULE, topic=WC,
    title="Recording and presenting weather data, and simple weather maps",
    slug="wx-recording-presenting-weather-data-and-simple-weather-maps",
    minutes=25,
    summary="How to record weather data in tables, present it in line, bar and climate graphs, calculate means, ranges and totals, and read a simple weather map with the standard symbols.",
    objectives=[
        "Describe how weather data is recorded and presented in tables and graphs",
        "Calculate the mean, range and total from weather data",
        "Describe the pattern shown on a climate graph",
        "Read a simple weather map using the standard symbols",
    ],
    key_concepts=["Weather record", "Line graph", "Bar graph", "Climate graph", "Mean", "Range", "Total", "Weather map", "Isobar", "Station symbol"],
    blocks=[
        H("Introduction"),
        T("A weather station records numbers every day: temperature, rainfall and more. Numbers in a notebook are hard to understand. "
          "A farmer near Bafoussam wants to know which months are wettest. A planner wants to know how hot the dry season gets. "
          "Geographers solve this by organising the numbers into **tables, graphs and maps**."),
        H("Recording data"),
        T("Readings are written in a **table**. Each row is a day or a month, and each column is an element. Always give the unit and the time of observation."),
        CODE("""Climate data for Kuma (a fictitious station)
Month       Rainfall (mm)   Mean temperature (°C)
January          18              27
February         32              28
March            95              28
April           152              27
May             208              26
June            262              25
July            305              24
August          335              24
September       248              25
October         176              26
November         62              26
December         22              26""", "text", title="Table 1. Monthly climate data for Kuma (fictitious)"),
        H("Presenting data in graphs"),
        KEY("Which graph for which data?", "Choose the type that suits the element.", cards=[
            ["Line graph", "Best for values that change continuously, such as temperature through the year. Join the points with a line."],
            ["Bar graph", "Best for separate amounts such as monthly rainfall. Draw bars of equal width with gaps between them."],
            ["Climate graph", "Joins both: bars for rainfall, a line for temperature, with the months along the bottom. Rainfall scale on the left and temperature scale on the right."],
        ]),
        IMG("f5g-wx-climate-graph.svg",
            alt="A climate graph for the fictitious station Kuma. Twelve bars show monthly rainfall, from 18 mm in January up to 335 mm in August and down to 22 mm in December. A line above shows temperature between 24 and 28 degrees Celsius.",
            caption="Figure 1. Climate graph for Kuma (a fictitious station). Rainfall in mm on the left, temperature in degrees Celsius on the right."),
        TIP("When you draw a graph: give it a title, label both axes with units, choose an even scale that fits the space, plot carefully, and add a key if you show two things. "
            "Marks are lost for missing labels and uneven scales."),
        H("Calculating from weather data"),
        D("**Total** = add all the values.  **Mean (average)** = total divided by the number of values.  **Range** = highest value minus lowest value.", title="Three calculations",
          formula=r"\text{mean} = \frac{\text{total}}{\text{number of values}}\qquad \text{range} = \text{highest} - \text{lowest}"),
        T("For a day, the **mean temperature** is often found with the maximum and minimum readings: add them and divide by 2. The daily range is the maximum minus the minimum."),
        EX("Worked example 1: calculations for Kuma", intro="Use the Kuma data. Find (a) the total annual rainfall, (b) the range of mean monthly temperature, (c) the mean temperature for the year, (d) the total rainfall from June to September.", steps=[
            S("(a) Total rainfall", math=r"18 + 32 + 95 + 152 + 208 + 262 + 305 + 335 + 248 + 176 + 62 + 22 = 1915", text="The total annual rainfall is 1915 mm."),
            S("(b) Range of temperature", math=r"28 - 24 = 4", text="Highest 28 °C (February and March), lowest 24 °C (July and August). The range is 4 °C."),
            S("(c) Mean temperature", math=r"\frac{312}{12} = 26", text="The 12 monthly temperatures add up to 312, so the mean is 26 °C."),
            S("(d) June to September", math=r"262 + 305 + 335 + 248 = 1150", text="The total is 1150 mm."),
        ]),
        EX("Worked example 2: describing a climate graph", intro="Describe the climate of Kuma from the graph. (A model answer.)", steps=[
            S("Temperature", text="It is hot all year. The mean monthly temperature stays between 24 °C and 28 °C, a small range of 4 °C."),
            S("Rainfall pattern", text="Rainfall is high from April to October and peaks in August at 335 mm. January and December are the driest months, with 18 mm and 22 mm."),
            S("Total", text="The annual rainfall is 1915 mm, so the climate is hot and wet, with a short drier season from November to March."),
        ]),
        H("Simple weather maps"),
        T("A **weather map** (or weather chart) shows the weather at one time over a large area. Each weather station has a **station symbol** which carries "
          "several pieces of information. Lines called **isobars** join places with the same air pressure."),
        IMG("f5g-wx-weather-map.svg",
            alt="A simple weather map of fictitious Mbanga. Kuma: 33 degrees, clear, light north wind. Mbanga: 30, half cloud, north-east wind. Ekoa: 24, overcast with rain, north-west wind. Dibo: 27, half cloud, north wind. Isobars read 1014, 1012 and 1010.",
            caption="Figure 2. A simple weather map of Mbanga (a fictitious region), with a key."),
        KEY("How to read a station symbol", "Four things to look for.", cards=[
            ["Circle", "Cloud cover: empty is clear, half-filled is half cloud, filled is overcast."],
            ["Wind staff", "A line from the circle pointing to where the wind comes FROM. More feathers mean a stronger wind."],
            ["Number", "Temperature in degrees Celsius."],
            ["Rain symbol", "Dots show that rain is falling."],
        ]),
        T("Isobars are labelled in hectopascals. The air tends to move from higher pressure to lower pressure, so the wind blows across the isobars. "
          "The pressure map can help to explain the weather. You will meet pressure and winds in a later topic."),
        EX("Worked example 3: reading the weather map", intro="Use Figure 2. (a) Which station is the hottest? (b) Which station has rain? (c) What is the weather at Mbanga? (A model answer.)", steps=[
            S("(a) Hottest", text="Kuma: the symbol shows 33 °C."),
            S("(b) Rain", text="Ekoa: it has rain symbols and an overcast sky (a filled circle)."),
            S("(c) Mbanga", text="Half of the sky is covered by cloud, the temperature is 30 °C, and the wind comes from the north-east."),
        ]),
        TIP("**Exam link.** Paper 1 gives you a table or graph and asks for a mean, range or total, or asks you to read a station symbol. "
            "Paper 2 Section B can ask how weather data are presented, or ask you to describe a climate graph. Always quote figures from the graph in your answer."),
        MISTAKE("Mixing up range and mean", "Range = highest minus lowest. It shows how much the values vary. Mean is the average. They are different numbers."),
        MISTAKE("Reading the wrong axis on a climate graph", "Rainfall is read against the left scale (bars). Temperature is read against the right scale (line). Check the labels first."),
        QUIZ("The maximum temperature in a day was 31 °C and the minimum was 21 °C. What was the daily range?", ["10 °C", "26 °C", "52 °C", "5 °C"], 0,
             "Range = 31 - 21 = 10 °C.",
             hint="Range is the highest value minus the lowest value.",
             feedback=["", "26 °C is the mean of 31 and 21, not the range.", "52 °C is the sum of the two readings.", "5 °C is half of the range."]),
        QUIZ("Which type of graph is best for showing monthly rainfall?", ["A line graph", "A bar graph", "A pie chart of temperature", "A map"], 1,
             "Rainfall is a total for each month, so separate bars are used.",
             hint="Rainfall in each month is a separate amount.",
             feedback=["A line graph suits continuously changing values such as temperature.", "", "A pie chart for temperature does not show rainfall.", "A map shows places, not monthly totals."]),
        PQ("A school weather station records daily rainfall of 4 mm, 0 mm, 12 mm, 8 mm and 6 mm. Find the total and the mean.", "Total: 4 + 0 + 12 + 8 + 6 = 30 mm. Mean: 30 divided by 5 = 6 mm."),
        PQ("The mean monthly temperatures in a town are 22, 24, 25, 26 and 23 degrees Celsius. Find the range.", "Highest 26 minus lowest 22 = 4 °C."),
        PQ("Describe how a climate graph shows rainfall and temperature.", "Bars show monthly rainfall using the left-hand scale in millimetres. A line shows mean monthly temperature using the right-hand scale in degrees Celsius. Months are along the bottom."),
        PQ("On a weather map, a station has a half-filled circle, a number 30, and a staff with two feathers pointing south-west. Describe the weather.", "Half of the sky is covered with cloud, the temperature is 30 °C, and the wind is fairly strong (two feathers) and blows from the south-west."),
        SUM("Weather data are recorded in tables with units and times, then shown in line graphs, bar graphs or climate graphs.",
            "A climate graph has bars for rainfall (left scale) and a line for temperature (right scale), with the months along the bottom.",
            "Total = add the values. Mean = total divided by the number of values. Range = highest minus lowest.",
            "A weather map has station symbols (cloud cover, wind staff, temperature, rain) and isobars joining places of equal pressure."),
    ],
))


# ------------------------------------------------------------------ 7. Precipitation and its forms
LESSONS.append(lesson(
    module=MODULE, topic=FC,
    title="Precipitation and its forms",
    slug="wx-precipitation-and-its-forms",
    minutes=20,
    summary="What precipitation is, how condensation forms cloud droplets and rain, and how rain, hail, snow, sleet, fog, mist and dew form.",
    objectives=[
        "Define precipitation",
        "Explain how condensation leads to the formation of precipitation",
        "Identify the main forms of precipitation and condensation: rain, hail, snow, sleet, fog, mist and dew",
        "Describe how each form is produced",
    ],
    key_concepts=["Precipitation", "Condensation", "Condensation nuclei", "Dew point", "Rain", "Hail", "Snow", "Sleet", "Fog", "Mist", "Dew"],
    blocks=[
        H("Introduction"),
        T("Early in the morning at Bamenda, the grass is wet although it did not rain in the night. In the afternoon the sky "
          "turns dark and heavy rain falls on the market. Both are water from the air, but they form in different ways."),
        T("In this lesson you will learn how water vapour turns into water we can see, and the forms it takes."),
        H("What is precipitation?"),
        D("**Precipitation** is water that falls from the atmosphere to the earth's surface, as a liquid (such as rain) or as a solid (such as hail or snow).", title="Precipitation"),
        D("**Condensation** is the change of water vapour into tiny drops of liquid water. It happens when air is cooled.", title="Condensation"),
        T("Warm air can hold more water vapour than cold air. When air cools it can hold less. The temperature at which air is full of "
          "vapour is called the **dew point**. If the air cools below the dew point, the extra vapour condenses."),
        T("Condensation needs tiny particles in the air, such as dust, smoke or sea salt. They are called **condensation nuclei**. "
          "The vapour condenses on them to form cloud droplets."),
        H("How rain forms"),
        T("A cloud is made of billions of tiny droplets. They are so small and light that air currents keep them up. "
          "Inside the cloud the droplets bump into each other and join together to make bigger drops. When the drops are heavy enough, "
          "they fall as **rain**."),
        IMG("f5g-wx-condensation-forms.svg",
            alt="Three small scenes. Cloud and rain: warm air rises, cools, and forms cloud with rain falling. Dew: droplets on cool grass at night. Fog and mist: a layer of cloud at ground level between trees.",
            caption="Figure 1. Three ways that cooling air produces water we can see: cloud and rain, dew, and fog."),
        KEY("Ways that air can be cooled", "The cause is always cooling.", cards=[
            ["Rising", "Air that rises goes into lower pressure, expands and cools. This makes clouds and rain."],
            ["Contact", "Air touching a cold surface, such as grass on a clear night, cools. This makes dew."],
            ["Cooling at ground level", "A thick layer of air near the ground cools. This makes fog or mist."],
        ]),
        H("The forms"),
        CODE("""Form    What it is                        How it forms
Rain    Drops of liquid water             Cloud droplets join and become heavy
Hail    Balls or lumps of ice             Ice grows in layers in tall storm clouds
Snow    Ice crystals                      Vapour freezes where it is below 0 degrees C
Sleet   Rain and snow mixed               Snow melts partly as it falls
Fog     Cloud at ground level, you        Air near the ground cools below dew point
        see less than 1 km
Mist    A thinner fog, you see more       As fog, but with fewer, smaller droplets
        than 1 km
Dew     Drops on grass and leaves         Surface cools at night; air touching it
                                          reaches dew point""", "text", title="Table 1. Forms of precipitation and condensation"),
        T("**Hail** forms in tall storm clouds with strong rising air. Raindrops are carried up to freezing levels, where they freeze. "
          "They fall, collect more water, and are lifted again. Each trip adds a layer of ice. When the stones are too heavy, they fall. "
          "Hail can damage crops, roofs and cars."),
        T("**Snow** forms when water vapour freezes into ice crystals at temperatures below 0 °C. It does not fall in the lowlands of Cameroon, but it "
          "is common in cold regions of the world. **Sleet** is a mixture of rain and partly melted snow."),
        T("**Fog** and **mist** are clouds that touch the ground. They form on calm, clear nights when the ground cools and cools the air above it. "
          "Fog is thick, with visibility under 1 km. Mist is thinner. Hill fog forms when moist air is forced up a slope and cools. "
          "**Dew** forms on grass, leaves and roofs on clear, calm nights. The surface loses heat and cools below the dew point of the air that touches it."),
        TIP("Some books say that dew, fog and mist are forms of condensation rather than true precipitation, because they do not fall from clouds. The syllabus lists them together "
            "with rain, hail, snow and sleet, so learn all seven and how each one forms."),
        TIP("**Exam link.** Paper 1 gives a description and asks you to name the form (for example 'a layer of cloud at ground level'). "
            "Paper 2 Section B may ask you to define precipitation and to describe how any three forms occur."),
        EX("Worked example 1: dew and fog", intro="Describe how dew and fog form. (A model answer.)", steps=[
            S("Condition", text="Both form on clear, calm nights. The sky is clear, so the ground loses heat quickly and cools."),
            S("Dew", text="Air touching the cold ground, grass or leaves is cooled to the dew point. Some vapour condenses into drops on the surface. These drops are dew."),
            S("Fog", text="If a deeper layer of air cools below dew point, the vapour condenses on dust particles into millions of tiny droplets in the air. This is fog, a cloud at ground level."),
        ]),
        EX("Worked example 2: hail", intro="Explain how hail forms. (A model answer.)", steps=[
            S("Where", text="It forms in tall storm clouds, where strong currents of air rise."),
            S("Freezing", text="Raindrops are carried up to levels below freezing and freeze into small pellets of ice."),
            S("Growing", text="The pellets fall, collect water and are carried up again. Each trip freezes a new layer on the stone."),
            S("Falling", text="When the hailstone is too heavy for the rising air to hold it, it falls to the ground."),
        ]),
        MISTAKE("Saying that dew falls from the sky", "Dew forms on the surface when the air touching it cools. It does not fall from clouds."),
        MISTAKE("Thinking that harmattan haze is mist", "Harmattan haze is dust blown from the Sahara. Mist and fog are made of water droplets."),
        QUIZ("Which form of condensation is a cloud touching the ground, which reduces visibility to less than 1 km?", ["Dew", "Fog", "Hail", "Sleet"], 1,
             "Fog is a cloud at ground level, with visibility under 1 km.",
             hint="It is a cloud, but at ground level.",
             feedback=["Dew forms as drops on surfaces, not as a cloud in the air.", "", "Hail is lumps of ice that fall from storm clouds.", "Sleet is a mixture of rain and partly melted snow."]),
        QUIZ("What must happen to air for water vapour to condense?", ["It must be heated", "It must be cooled to its dew point", "It must become drier", "It must stop moving"], 1,
             "Air condenses its vapour when it is cooled to its dew point.",
             hint="Think about a cold bottle of water on a hot day.",
             feedback=["Heating makes air able to hold more vapour.", "", "Drier air has less vapour to condense.", "The movement of air has no direct effect on condensation."]),
        PQ("Define precipitation.", "Precipitation is water that falls from the atmosphere to the ground as a liquid (rain) or as a solid (hail, snow)."),
        PQ("Name four forms of precipitation or condensation.", "Any four of: rain, hail, snow, sleet, fog, mist, dew."),
        PQ("Explain how fog forms.", "On a clear, calm night the ground loses heat and cools the air above it. When the air cools below its dew point, the vapour condenses into tiny droplets in the air. The droplets form a cloud at ground level."),
        PQ("Describe the difference between hail and sleet.", "Hail is a hard lump of ice built up in layers inside a storm cloud, and it can fall in hot weather. Sleet is a mixture of rain and partly melted snow, found in cold weather."),
        SUM("Precipitation is water that falls from the atmosphere as liquid or solid. Condensation is vapour changing to droplets, by cooling to the dew point.",
            "Rain forms when cloud droplets join together and become heavy enough to fall.",
            "Hail: ice in layers in storm clouds. Snow: ice crystals below 0 °C. Sleet: rain and partly melted snow.",
            "Fog and mist: cloud at ground level, from cooled air. Dew: drops on cool surfaces on clear, calm nights."),
    ],
))

# ------------------------------------------------------------------ 8. The three types of rainfall
LESSONS.append(lesson(
    module=MODULE, topic=FC,
    title="The three types of rainfall",
    slug="wx-the-three-types-of-rainfall",
    minutes=24,
    summary="How convectional, relief (orographic) and frontal (cyclonic) rainfall form, with annotated diagrams and examples from West and Central Africa, including Mount Cameroon and the Western Highlands.",
    objectives=[
        "Illustrate the three main types of rainfall with annotated diagrams",
        "Describe how convectional, relief and frontal rainfall form",
        "Explain why a rain shadow forms on the leeward side of highlands",
        "Identify the type of rainfall that is common in a given place",
    ],
    key_concepts=["Convectional rainfall", "Relief (orographic) rainfall", "Frontal (cyclonic) rainfall", "Windward", "Leeward", "Rain shadow", "Air mass", "Front"],
    blocks=[
        H("Introduction"),
        T("Rain does not fall for one reason only. The afternoon storms of the Congo basin, the heavy rain on the slopes of Mount Cameroon "
          "and the steady rain of a rainy day in a cool country have different causes. All of them come from air that is cooled, but "
          "the way the air is made to rise is different."),
        T("Geographers recognise three main types of rainfall, named after the reason for the rising air: **convection**, **relief** and **fronts**."),
        H("Convectional rainfall"),
        D("**Convectional rainfall** is rain caused by air that is heated at the ground, rises (convection), cools and condenses.", title="Convectional rainfall"),
        IMG("f5g-wx-convectional-rain.svg",
            alt="Sun heats hot ground. Arrows show warm air rising, cooling at the condensation level, forming a tall cloud and giving heavy rain. Four numbered steps explain the process.",
            caption="Figure 1. Convectional rainfall."),
        T("The sun heats the ground strongly. The ground heats the air above it. Warm air is light, so it rises in strong currents. As it rises "
          "it cools. At the condensation level the vapour condenses into a tall cloud called a cumulonimbus. Heavy rain falls, often with thunder and lightning. "
          "The storm is short, usually in the afternoon, when the ground is hottest."),
        T("**Where it is common:** hot, wet places near the equator. This includes the equatorial forest of Central Africa, such as the Congo basin and the forest zone of southern Cameroon. "
          "It also happens inland in the hot season in many tropical regions."),
        H("Relief (orographic) rainfall"),
        D("**Relief rainfall** (also called **orographic rainfall**) is rain caused by moist air that is forced to rise over high land, then cools and condenses.", title="Relief rainfall"),
        IMG("f5g-wx-relief-rain.svg",
            alt="Moist wind blows from the sea and rises up a mountain. Cloud forms and rain falls on the windward slope. On the leeward slope dry air sinks and warms, giving a rain shadow.",
            caption="Figure 2. Relief rainfall and the rain shadow."),
        T("Moist air from the sea meets a range of highland. It cannot go through it, so it is forced up. It cools as it rises. "
          "At some height the vapour condenses and clouds form. Rain falls on the **windward** slope, the side that faces the wind."),
        T("On the **leeward** slope, the sheltered side, the air sinks. Sinking air is warmed and dried, so there is little cloud and rain. "
          "This dry area is the **rain shadow**."),
        T("**Cameroon examples:** Mount Cameroon stands beside the Atlantic coast. The moist south-west winds from the ocean are forced up the slopes. "
          "The wet side of the mountain receives very heavy rain, and the coast at its foot is often named as one of the wettest places in Africa "
          "(check your textbook for figures). The Western Highlands around Bamenda and Bafoussam also force moist air upwards and have a high rainfall, "
          "so relief rain is important to the farming of the region."),
        H("Frontal (cyclonic) rainfall"),
        D("**Frontal rainfall** is rain caused where a warm air mass meets a cold air mass. The boundary between them is called a **front**.", title="Frontal rainfall"),
        IMG("f5g-wx-frontal-rain.svg",
            alt="A side view of a front. Cold, dense air forms a wedge near the ground. Warm, light air slides up over the cold air along a sloping boundary. Cloud forms along the boundary and rain falls.",
            caption="Figure 3. Frontal rainfall."),
        T("Warm air is lighter than cold air. When the two meet, the cold air stays low, like a wedge. The warm air is forced to rise over it. "
          "As it rises it cools, vapour condenses and cloud forms along the front. Rain is often steady and can last for hours or days. "
          "Fronts are usually found with areas of low pressure called depressions (cyclones), so this rain is also called **cyclonic** rainfall."),
        T("**Where it is common:** in the middle latitudes, such as western Europe, where cold and warm air masses meet. It is not the main type of rain in Cameroon. "
          "In West Africa a similar meeting of moist air from the Atlantic and dry air from the Sahara brings rain in the rainy season. This will be studied in the topic on climate (check your textbook)."),
        CODE("""Type            Why the air rises          Typical rain             Common in
Convectional    Ground heated by the sun   Heavy, short, thunder    Equatorial areas
Relief          Air forced up highland     Heavy on windward side   Mount Cameroon,
                                                                    Western Highlands
Frontal         Warm air rises over cold   Steady, long-lasting     Middle latitudes""", "text", title="Table 1. The three types of rainfall compared"),
        TIP("**Exam link.** Paper 1 describes a place or a diagram and asks which type of rainfall it shows. "
            "Paper 2 Section B often says 'With the aid of a labelled diagram, describe how ... rainfall forms'. "
            "Always draw the diagram, number the steps (heating or forcing, rising, cooling, condensation, rain), and name an example."),
        EX("Worked example 1: convectional rainfall", intro="With the aid of a labelled diagram, describe how convectional rainfall forms. (A model answer.)", steps=[
            S("Diagram", text="Draw the sun, the heated ground, arrows of rising air, a condensation level, a cumulonimbus cloud and rain. Label each part."),
            S("Heating", text="The sun heats the ground strongly. The ground heats the air above it, so the air expands and becomes lighter."),
            S("Rising and cooling", text="The warm air rises in strong currents (convection). As it rises it cools."),
            S("Condensation and rain", text="At the condensation level the vapour condenses into a tall cloud, and heavy rain falls, often with thunder. It is common in equatorial areas in the afternoon."),
        ]),
        EX("Worked example 2: relief rainfall and rain shadow", intro="Explain why the windward side of Mount Cameroon receives more rain than the leeward side. (A model answer.)", steps=[
            S("Moist wind", text="Moist winds from the Atlantic Ocean blow towards the mountain."),
            S("Forced to rise", text="The mountain forces the air to rise up the windward slope. The air cools as it rises."),
            S("Condensation", text="The vapour condenses to form cloud, and rain falls heavily on the windward slope."),
            S("Leeward side", text="After the crest, the air sinks down the leeward slope. It warms and becomes drier, so there is little rain: a rain shadow."),
        ]),
        MISTAKE("Mixing up windward and leeward", "Windward = the side facing the wind (wet). Leeward = the sheltered side (dry, rain shadow)."),
        QUIZ("Which type of rainfall is caused when moist air is forced to rise over mountains?", ["Convectional", "Relief", "Frontal", "Cyclonic"], 1,
             "Relief rainfall is caused by moist air forced upwards by high land.",
             hint="Think of the shape of the land, its 'relief'.",
             feedback=["Convectional rain is caused by the heating of the ground.", "", "Frontal rain happens where two air masses meet.", "Cyclonic is another name for frontal rain."]),
        QUIZ("What is the dry area on the sheltered side of a mountain called?", ["Windward slope", "Condensation level", "Rain shadow", "Front"], 2,
             "The rain shadow is the dry area on the leeward side, where air sinks and warms.",
             hint="The mountain shields it from the rain.",
             feedback=["The windward slope is the wet side that faces the wind.", "The condensation level is the height where cloud forms.", "", "A front is the boundary between a warm and a cold air mass."]),
        PQ("Name the three types of rainfall.", "Convectional, relief (orographic) and frontal (cyclonic)."),
        PQ("Give one place in Cameroon where relief rainfall is important and say why.", "Mount Cameroon (or the Western Highlands around Bamenda). Moist winds from the Atlantic are forced up the highland, cool, and condense to give heavy rain on the windward side."),
        PQ("Explain what a rain shadow is and why it forms.", "A rain shadow is a dry area on the leeward side of highland. The air has lost most of its moisture on the windward side. On the leeward side it sinks, warms and becomes drier, so little cloud and rain form."),
        PQ("Draw an annotated sketch to show how frontal rainfall forms and describe the rain it gives.", "The sketch shows cold, dense air as a wedge near the ground, warm, lighter air rising over it along a sloping front, cloud along the boundary and rain. Frontal rain is often steady and lasts for hours or days."),
        SUM("Convectional rain: ground heated, warm air rises, cools, condenses into tall clouds, heavy rain, often with thunder in the afternoon. Common in equatorial areas.",
            "Relief rain: moist air forced up highland, cools, condenses. Heavy on the windward side, with a rain shadow on the leeward side. Mount Cameroon and the Western Highlands.",
            "Frontal rain: warm air rises over cold air at a front. Steady, long-lasting rain, mainly in middle latitudes.",
            "In all three types air rises, cools and condenses. The difference is what makes the air rise."),
    ],
))
