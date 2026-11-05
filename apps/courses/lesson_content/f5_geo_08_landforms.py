"""Form 5 Geography, Geomorphology: Denudational processes and landforms (8 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Geomorphology"
TOPIC = "Denudational processes and landforms"

LESSONS = []

# ------------------------------------------------------------------ 1. Weathering
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Weathering: types, processes, landforms and factors",
    slug="land-weathering",
    minutes=22,
    summary="Weathering is the breaking down of rock where it lies, without movement. This lesson covers physical, chemical and biological weathering, the landforms they make, the factors involved and why weathering is strong in the humid tropics.",
    objectives=[
        "Define weathering and distinguish it from erosion",
        "Describe the types and processes of weathering",
        "Identify weathering landforms such as tors, exfoliation domes and regolith",
        "Explain how climate, rock type and vegetation affect weathering, and why it is strong in the humid tropics",
    ],
    key_concepts=["Weathering", "Physical weathering", "Chemical weathering", "Biological weathering", "Exfoliation", "Regolith", "Tor"],
    blocks=[
        H("Introduction"),
        T("Look at a road cutting in the Western Highlands, near Bafoussam or Bamenda. The top of the cutting is red-brown soil. "
          "Below it, the rock is soft and crumbly. Only deeper down do you find hard, fresh rock."),
        T("The rock has been broken down slowly by rain, heat, roots and living things. This is called **weathering**. "
          "It is the first step in shaping every landscape on Earth, from Mount Cameroon to the plains around Maroua."),
        D("**Weathering** is the breaking down or rotting of rock where it lies, caused by weather, water, plants and animals. "
          "The rock is not carried away while it is being weathered.", title="Weathering"),
        D("**Denudation** is the wearing down of the land surface. It includes weathering, erosion, transportation and deposition.",
          title="Denudation"),
        TIP("Weathering happens in one place. **Erosion** moves the broken pieces away. If rock fragments are being carried by a river, "
            "the word you need is erosion or transportation, not weathering.", title="Weathering is not erosion"),
        H("Types of weathering"),
        KEY("Three types", "Weathering is grouped by the way the rock is broken.", cards=[
            ["Physical (mechanical)", "The rock breaks into pieces. Its minerals do not change."],
            ["Chemical", "The minerals in the rock change or dissolve, so the rock rots and weakens."],
            ["Biological", "Plants, animals and people break or change the rock."],
        ]),
        H("Physical weathering"),
        T("**Temperature change (exfoliation).** In Cameroon's dry season, bare rock gets very hot by day and cools by night. "
          "The outer layer expands when hot and contracts when cool. Rock is a poor conductor of heat, so the surface changes more than the inside. "
          "Over many years this makes cracks, and curved sheets peel off like the skins of an onion."),
        IMG("f5g-land-exfoliation.svg", alt="A rock dome with curved sheets peeling off its outer surface, a sun for hot days and a moon for cool nights",
            caption="Figure 1. Exfoliation: heating by day and cooling by night make the outer sheets crack and peel off."),
        T("**Salt crystallisation.** Salty water enters small cracks, for example near the coast at Limbe or Kribi, or in dry areas where water evaporates. "
          "The water dries and salt crystals grow. The crystals push the crack wider, and pieces break off."),
        T("**Root action.** Roots grow into cracks and widen them as they thicken. Large trees can split rock in this way."),
        T("**Freeze-thaw** (frost action) happens when water freezes in a crack and expands. It is common in cold lands, "
          "but it is **rare in tropical lowlands** because the temperature seldom falls below freezing. "
          "So in answers about Cameroon, lead with temperature change, salt and roots."),
        H("Chemical and biological weathering"),
        T("Chemical weathering needs water. Rainwater is slightly acidic because it dissolves carbon dioxide from the air. "
          "Water in the soil gets more acid from rotting plants."),
        T("**Solution.** Some minerals simply dissolve in water and are washed away."),
        T("**Oxidation.** Oxygen reacts with iron in the rock and makes rust. This is why many tropical soils are red or yellow-brown."),
        T("**Hydrolysis.** Water reacts with some minerals, such as the feldspar in granite. The mineral changes into soft clay, "
          "and the grains of the rock fall apart."),
        T("**Biological weathering.** Roots widen cracks (physical). Rotting leaves make organic acids that attack rock (chemical). "
          "Termites, earthworms and burrowing animals mix and loosen the soil. Quarrying and building also break rock."),
        H("Weathering landforms"),
        D("**Regolith** is the layer of loose, weathered rock and soil above solid bedrock. In the humid tropics it can be many metres deep.",
          title="Regolith"),
        T("**Exfoliation domes** are rounded rock hills left when the outer sheets of a massive rock, such as granite, peel away (Figure 1)."),
        T("**Tors** are piles of rounded granite blocks standing on a hillside. They form in three stages. First, water enters the joints (cracks) of the rock. "
          "Second, chemical weathering rots the rock along the joints and leaves rounded blocks of fresh rock inside the regolith. "
          "Third, erosion removes the regolith and the blocks are left standing. Parts of West Africa have granite tors. "
          "For Cameroonian examples, check your textbook."),
        IMG("f5g-land-tor-formation.svg", alt="Three stages: jointed granite, chemical weathering below ground leaving rounded blocks in regolith, then the regolith removed leaving a tor",
            caption="Figure 2. How a tor forms: joints, weathering below ground, then removal of the regolith."),
        H("Factors that affect weathering"),
        KEY("Climate, rock type and vegetation", "These three factors decide how fast, and in what way, rock weathers.", cards=[
            ["Climate", "Heat speeds chemical reactions. Water is needed for chemical weathering. Big daily temperature changes cause exfoliation."],
            ["Rock type", "Hard rocks with few joints weather slowly. Rocks with many joints, or with minerals that dissolve or rot, weather faster."],
            ["Vegetation", "Roots break rock. Plant cover keeps the soil damp and adds acids. Bare rock suffers the daily heating and cooling."],
        ]),
        H("Why weathering is stronger in the humid tropics"),
        T("In the humid tropics, such as the forests of southern Cameroon, it is hot all year and rain is heavy. "
          "Heat and water together make chemical reactions fast. Dense vegetation adds roots and organic acids. "
          "Weathering goes on all year with no cold season to slow it. The result is a deep regolith."),
        T("In a hot desert it is also hot, but there is very little water. Chemical weathering is slow and temperature change is the main process."),
        EX("Model answer: explain why chemical weathering is stronger in the humid tropics than in a hot desert", intro="Explain why chemical weathering is more active in the humid tropics than in a hot desert.", steps=[
            S("Point 1: water", text="Chemical weathering needs water. The humid tropics have heavy rain all or most of the year. Deserts have very little rain."),
            S("Point 2: heat", text="High temperatures speed up chemical reactions such as oxidation and hydrolysis. The tropics are hot every month."),
            S("Point 3: vegetation", text="Dense forest gives organic acids from rotting leaves and keeps the soil damp, which attacks the rock."),
            S("Evidence", text="Deep red regolith is common in southern Cameroon. Desert rock is mostly bare and fresh."),
            S("Conclusion", text="Hot and wet conditions together make chemical weathering strongest in the humid tropics."),
        ]),
        EX("Model answer: describe how a tor is formed", intro="With the help of a labelled sketch, describe how a tor is formed.", steps=[
            S("Sketch", text="Draw three small stages as in Figure 2: jointed rock, rotted joints with rounded blocks, and the tor left standing. Label joints, regolith and tor."),
            S("Stage 1", text="Granite has joints. Rainwater enters them."),
            S("Stage 2", text="Chemical weathering rots the rock along the joints more than in the blocks between them. Rounded blocks are left in the regolith."),
            S("Stage 3", text="Running water and gravity remove the regolith. The rounded blocks stand as a tor."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling weathering 'erosion'", "Weathering breaks rock where it is. Erosion carries the pieces away. Use the right word."),
        MISTAKE("Using freeze-thaw for Cameroon", "Frost is rare in tropical lowlands. Use temperature change, salt crystallisation and root action as physical processes."),
        MISTAKE("Saying rain only 'washes' rock", "Rain causes chemical weathering by reacting with minerals. Name a process: solution, oxidation or hydrolysis."),
        QUIZ("Which process makes thin curved sheets peel off a bare rock dome?",
             ["Hydrolysis", "Exfoliation", "Salt crystallisation", "Solution"], 1,
             "Exfoliation is caused by repeated heating and cooling of the outer layer.",
             hint="Think of the skin of an onion.",
             feedback=["Hydrolysis is a chemical process that changes minerals into clay.", "",
                       "Salt crystals push cracks wider but do not peel curved sheets.", "Solution dissolves minerals; it does not peel the surface."]),
        QUIZ("Why is freeze-thaw weathering rare in the Cameroon lowlands?",
             ["There is no water", "The rocks are too soft", "The temperature seldom falls below freezing", "Roots protect the rock"], 2,
             "Freeze-thaw needs water to freeze in cracks, so it needs temperatures below zero.",
             hint="What must happen to water in a crack for it to expand?",
             feedback=["There is plenty of water in the humid lowlands.", "Rock hardness is not the reason.", "", "Roots actually break rock; they do not protect it."]),
        TIP("**Exam link.** Weathering appears in Paper 1 (multiple choice on definitions, types and factors) and in Paper 2 Section B (physical geography), "
            "where you may be asked to define it, describe processes and draw a labelled sketch of a tor or exfoliation dome.", title="Exam link"),
        H("Practice questions"),
        PQ("Define weathering.", "Weathering is the breaking down or rotting of rock where it lies, with little or no movement of the pieces."),
        PQ("Name two processes of physical weathering that are common in the tropics.",
           "Temperature change (exfoliation), salt crystallisation and root action. Any two."),
        PQ("Explain the part played by rock type in weathering.",
           "Hard rocks with few joints weather slowly. Rocks with many joints let water in, and rocks with minerals that dissolve or rot (such as feldspar in granite) weather faster. "
           "So rock type decides how fast and in what way a rock weathers."),
        PQ("Describe how a tor is formed.",
           "Water enters joints in granite. Chemical weathering rots the rock along the joints, leaving rounded blocks in the regolith. "
           "Running water and gravity then remove the regolith, and the blocks stand as a tor."),
        SUM("Weathering is the breaking down of rock in place. Erosion moves the pieces away.",
            "Physical weathering breaks rock without changing it: temperature change (exfoliation), salt crystallisation, root action. Freeze-thaw is rare in the tropics.",
            "Chemical weathering changes minerals: solution, oxidation, hydrolysis. Biological weathering is done by plants, animals and people.",
            "Weathering landforms include regolith, exfoliation domes and tors.",
            "Climate, rock type and vegetation control weathering. It is strongest in the humid tropics because of heat, heavy rain and dense vegetation."),
    ],
))

# ------------------------------------------------------------------ 2. Erosion, transportation and deposition
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Erosion, transportation and deposition",
    slug="land-erosion-transportation-and-deposition",
    minutes=20,
    summary="Erosion wears away land, transportation carries the load and deposition drops it. This lesson separates the three, names the agents (water, wind, waves) and explains the four erosion processes and four transport methods.",
    objectives=[
        "Differentiate erosion, transportation and deposition",
        "Name the agents of erosion and say where each works",
        "Describe hydraulic action, abrasion, attrition and solution",
        "Describe traction, saltation, suspension and solution as methods of transport",
    ],
    key_concepts=["Erosion", "Transportation", "Deposition", "Load", "Hydraulic action", "Abrasion", "Attrition", "Traction", "Saltation", "Suspension"],
    blocks=[
        H("Introduction"),
        T("After heavy rain in the rainy season, the River Wouri near Douala or the Sanaga near Edea looks brown. "
          "The brown colour is soil and sand carried by the water. Where did it come from? How is it carried? Where will it end up?"),
        T("These three questions are the three stages of this lesson: erosion, transportation and deposition. "
          "Together with weathering, they wear down the land. Geographers call this **denudation**."),
        D("**Erosion** is the wearing away of the land surface by a moving agent (water, wind or waves) which carries rock fragments with it.",
          title="Erosion"),
        D("**Transportation** is the movement of eroded material, called the **load**, from one place to another.", title="Transportation"),
        D("**Deposition** is the dropping of the load when the agent loses energy.", title="Deposition"),
        KEY("Three stages, one chain", "Think of a lorry: it loads, drives and unloads.", cards=[
            ["Erosion", "The agent picks up and wears away rock and soil."],
            ["Transportation", "The agent carries the load along."],
            ["Deposition", "The agent slows and drops the load."],
        ]),
        TIP("Weathering is different. It breaks rock in place and needs no moving agent. Erosion always needs a moving agent.", title="Do not mix with weathering"),
        H("Agents of erosion"),
        T("An **agent** is something that moves and carries material. The three agents in this syllabus are running water (rivers), wind and waves."),
        T("**Running water.** Rivers are the most important agent in Cameroon and in most of the world. They cut valleys and build plains."),
        T("**Wind.** Wind is strongest in dry lands with little plant cover, such as the Sahel near Lake Chad and the Sahara."),
        T("**Waves.** Waves shape the coast, for example around Limbe, Kribi and the Douala estuary."),
        H("Processes of erosion"),
        T("Every agent erodes in some of the same ways. The four main processes are listed below. Rivers use all four."),
        KEY("Four erosion processes", "Learn each name together with what it does.", cards=[
            ["Hydraulic action", "The force of moving water alone pushes into cracks and removes loose rock and soil. In waves, air squeezed into cracks also forces rock apart."],
            ["Abrasion (corrasion)", "The load, such as stones and sand, is hurled against the bed and banks and scrapes them like sandpaper."],
            ["Attrition", "The pieces of load knock against each other and break into smaller, rounder pieces."],
            ["Solution (corrosion)", "Water dissolves minerals in the rock and carries them away."],
        ]),
        T("Notice that attrition wears down the **load**, not the bed or banks. This is why pebbles far from the source are small and round, "
          "while stones near the source are large and angular (with sharp edges)."),
        H("Methods of transportation"),
        T("A river carries its load in four ways. Which way is used depends on the size of the pieces and the speed of the water."),
        IMG("f5g-land-transport.svg", alt="River cross-section showing fine particles in suspension, dissolved minerals in solution, stones bouncing in saltation and boulders rolling in traction",
            caption="Figure 1. Four ways a river moves its load. Larger pieces travel nearer the bed."),
        KEY("Four transport methods", "From the smallest load to the largest.", cards=[
            ["Solution", "Dissolved minerals are carried in the water. You cannot see them."],
            ["Suspension", "Fine clay and silt float in the water and make it look muddy."],
            ["Saltation", "Small stones and coarse sand bounce along the bed in short hops."],
            ["Traction", "Large stones and boulders are rolled or dragged along the bed. This needs a flood or fast water."],
        ]),
        T("Wind uses suspension (fine dust, as in the harmattan), saltation (sand grains bouncing) and surface creep, which is like traction. "
          "Waves move material along the coast by the drift described in the lesson on coasts."),
        H("Deposition"),
        T("An agent can only carry a load while it has enough energy. When the energy falls, the load is dropped, the heaviest pieces first."),
        T("**A river deposits** where it slows down: on the inside of a bend, on a flat flood plain, when it floods and spreads out, "
          "and where it enters a lake or the sea at its mouth. It also deposits in the dry season when its flow falls."),
        T("**Wind deposits** when it meets an obstacle or slows down, so sand is dropped as dunes."),
        T("**Waves deposit** in sheltered places where they are weak, such as bays, building beaches."),
        EX("Model answer: differentiate erosion, transportation and deposition", intro="Differentiate between erosion, transportation and deposition.", steps=[
            S("Erosion", text="Erosion is the wearing away of land by a moving agent such as a river, wind or waves, using processes like abrasion and hydraulic action."),
            S("Transportation", text="Transportation is the carrying of the eroded load by the agent, for example by traction, saltation, suspension or solution."),
            S("Deposition", text="Deposition is the dropping of the load when the agent loses energy, for example when a river slows at its mouth."),
            S("Link", text="The three stages follow one another. Erosion supplies the load, transportation moves it and deposition builds new landforms."),
        ]),
        EX("Model answer: how a river transports its load", intro="Describe how a river transports its load.", steps=[
            S("Sketch", text="Draw a river cross-section as in Figure 1 and label the four methods."),
            S("Solution", text="Minerals dissolved from the rocks are carried in the water."),
            S("Suspension", text="Fine particles of clay and silt float in the water."),
            S("Saltation", text="Small stones bounce along the bed."),
            S("Traction", text="Large boulders roll along the bed, mainly in floods."),
            S("Conclusion", text="The bigger the piece, the nearer the bed it travels and the more energy is needed to move it."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing abrasion and attrition", "Abrasion wears the **bed and banks**. Attrition wears the **load itself**. Remember: attrition makes the pebbles smaller and rounder."),
        MISTAKE("Forgetting solution in two places", "Solution is both an erosion process (dissolving rock) and a method of transport (dissolved minerals carried in water)."),
        MISTAKE("Saying a river deposits when it is fast", "Deposition happens when the river slows down and loses energy, not when it is fast."),
        QUIZ("Which erosion process breaks the pieces of a river's own load into smaller, rounder pieces?",
             ["Hydraulic action", "Abrasion", "Attrition", "Solution"], 2,
             "Attrition is the knocking of load against load. The pieces become smaller and rounder.",
             hint="Which process does NOT wear the bed or banks?",
             feedback=["Hydraulic action is the force of the water itself.", "Abrasion wears the bed and banks using the load.", "", "Solution dissolves minerals; it does not round pebbles."]),
        QUIZ("Small stones that bounce along a river bed in short hops are moving by",
             ["traction", "suspension", "solution", "saltation"], 3,
             "Saltation means hopping or bouncing along the bed.",
             hint="Think of the word 'jump'.",
             feedback=["Traction is rolling or dragging of larger boulders.", "Suspension is for fine particles floating in the water.", "Solution is dissolved minerals, which cannot be seen.", ""]),
        TIP("**Exam link.** Erosion, transportation and deposition are tested in Paper 1 (definitions, processes, methods) and Paper 2 Section B, "
            "where a labelled cross-section of a river showing the four methods of transport earns marks.", title="Exam link"),
        H("Practice questions"),
        PQ("Name the three agents of erosion studied in this course.", "Running water (rivers), wind and waves."),
        PQ("Distinguish between abrasion and attrition.",
           "Abrasion is the wearing of the river bed and banks by the stones and sand that the river carries. Attrition is the wearing of the load itself, "
           "as the pieces knock against each other and become smaller and rounder."),
        PQ("Describe the four ways in which a river carries its load.",
           "Solution: dissolved minerals carried in the water. Suspension: fine clay and silt carried in the water. Saltation: small stones bounce along the bed. "
           "Traction: large boulders are rolled along the bed."),
        PQ("Give two places where a river is likely to deposit its load.",
           "On the inside of a meander bend, on its flood plain, or at its mouth where it meets the sea. Any two."),
        SUM("Erosion wears away land, transportation carries the load and deposition drops it.",
            "The agents are running water, wind and waves.",
            "The four erosion processes are hydraulic action, abrasion, attrition and solution.",
            "A river transports its load by solution, suspension, saltation and traction. Bigger pieces travel nearer the bed.",
            "Deposition occurs when the agent loses energy, and the heaviest load is dropped first."),
    ],
))

# ------------------------------------------------------------------ 3. Rivers: erosional landforms
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="A river from source to mouth: erosional landforms",
    slug="land-rivers-erosional-landforms",
    minutes=22,
    summary="A river changes along its path from source to mouth. This lesson describes the three courses and the erosional landforms of the upper course: V-shaped valleys, interlocking spurs, waterfalls, rapids and gorges.",
    objectives=[
        "Define the main terms used to describe a river system",
        "Describe a river from source to mouth in three courses",
        "Describe and explain the formation of V-shaped valleys, interlocking spurs, waterfalls, rapids and gorges",
        "Draw labelled sketches of these landforms",
    ],
    key_concepts=["Source", "Tributary", "Confluence", "Mouth", "Long profile", "V-shaped valley", "Interlocking spurs", "Waterfall", "Rapids", "Gorge"],
    blocks=[
        H("Introduction"),
        T("The Sanaga is the longest river wholly inside Cameroon. It rises on the high ground of the Adamawa region and flows west and south-west to the Atlantic coast. "
          "The Benue also starts in the Adamawa area, but it flows north and west towards the Niger. "
          "Near its start a river is a small, fast, stony stream. Near the sea it is wide, slow and muddy."),
        T("A river is always changing as it goes downhill. In this lesson you learn the parts of a river, its three courses and the landforms that rivers erode in the upper course."),
        H("Parts of a river system"),
        D("The **source** is where a river begins, often a spring or a swampy hollow in high ground.", title="Source"),
        D("A **tributary** is a smaller stream that joins a larger river. The meeting point is a **confluence**.", title="Tributary and confluence"),
        D("The **mouth** is where a river enters the sea or a lake. A **watershed** is the high ground that separates one river basin from another. "
          "The **drainage basin** is the whole area drained by a river and its tributaries.", title="Mouth, watershed and drainage basin"),
        H("The three courses"),
        T("A river is divided into three courses. Their boundaries are not sharp lines. They change gradually."),
        IMG("f5g-land-river-profile.svg", alt="Long profile of a river falling steeply at first then gently to the sea, split into upper, middle and lower courses with features listed",
            caption="Figure 1. The long profile of a river: steep in the upper course and very gentle in the lower course."),
        KEY("Upper, middle and lower course", "The main work of the river changes along its length.", cards=[
            ["Upper course", "High and steep. The river cuts downwards (vertical erosion). Landforms: V-shaped valley, interlocking spurs, waterfalls, rapids, gorges."],
            ["Middle course", "Gentler slope. The river cuts sideways (lateral erosion) and carries a large load. Landforms: meanders and a wider valley."],
            ["Lower course", "Very gentle slope and a very wide valley. The river deposits its load. Landforms: flood plain, levees, delta."],
        ]),
        H("V-shaped valley"),
        T("In the upper course the river has a steep gradient and rocky load. It uses abrasion and hydraulic action to cut **downwards**. "
          "This is called **vertical erosion**. The valley becomes deep and narrow."),
        T("Weathering loosens rock on the valley sides. Rain and gravity (soil creep and small slips) move this material down into the river, "
          "which carries it away. The sides slope steeply to the river, so the valley has a V shape in cross-section."),
        D("A **V-shaped valley** is a narrow, steep-sided valley cut by a river by vertical erosion in its upper course. "
          "The river fills the bottom of the V.", title="V-shaped valley"),
        H("Interlocking spurs"),
        T("A **spur** is a ridge of high ground that sticks out into the valley. In the upper course the river is not strong enough to cut through "
          "a spur, so it winds around it. The spurs on the two sides of the valley are staggered, and they overlap like the teeth of a zip."),
        IMG("f5g-land-interlocking-spurs.svg", alt="Plan view of a river winding between spurs that alternate from each side, with a V-shaped cross-section beside it",
            caption="Figure 2. Interlocking spurs and a V-shaped valley."),
        H("Waterfalls and gorges"),
        T("A **waterfall** is a place where a river drops vertically over a step in its bed. Many waterfalls form where a layer of hard rock lies above a layer of soft rock."),
        T("Water and its load wear away the soft rock below the hard rock faster than the hard rock. This undercuts the hard rock and leaves an overhang. "
          "A deep **plunge pool** forms at the foot, where falling water swirls rocks around. In time the overhang has no support and collapses."),
        T("The waterfall now has a new position, a little further upstream. This repeats many times, so the waterfall **retreats upstream**."),
        IMG("f5g-land-waterfall.svg", alt="Side view of a waterfall over hard rock with soft rock undercut below, a plunge pool, a retreating fall and a gorge downstream",
            caption="Figure 3. A waterfall retreats upstream and leaves a gorge behind."),
        D("A **gorge** is a deep, narrow valley with very steep, almost vertical sides. Many gorges are formed as a waterfall retreats upstream "
          "and leaves a deep channel behind it.", title="Gorge"),
        T("**Rapids** are stretches where the river runs fast and shallow over a rough, uneven bed. They form where bands of hard and soft rock cross the river. "
          "The soft rock wears down more quickly and leaves a series of small steps of hard rock. The water is white and turbulent as it hurtles over them. "
          "A waterfall is a single large drop. Rapids are many small drops."),
        TIP("For named examples of waterfalls and gorges in Cameroon, check your textbook. "
            "In the exam you may use any well-known example you have studied.", title="Examples"),
        EX("Model answer: how a waterfall is formed", intro="With the help of a labelled diagram, explain how a waterfall is formed and how it changes with time.", steps=[
            S("Sketch", text="Draw Figure 3: hard rock over soft rock, the drop, the plunge pool and the gorge. Label each part."),
            S("Starting condition", text="A river flows over a band of hard rock lying on soft rock."),
            S("Undercutting", text="The soft rock is eroded faster by abrasion and hydraulic action, especially in the plunge pool. The hard rock is left as an overhang."),
            S("Collapse", text="The overhang is unsupported and breaks off. The fall moves upstream."),
            S("Result", text="Over a long time the waterfall retreats and leaves a steep-sided gorge downstream."),
        ]),
        EX("Model answer: describe the V-shaped valley", intro="Describe and explain the formation of a V-shaped valley.", steps=[
            S("Description", text="A narrow valley with steep sides, found in the upper course, with the river filling the bottom."),
            S("Vertical erosion", text="The river has a steep gradient and a coarse load. It cuts down into its bed by abrasion and hydraulic action."),
            S("Valley sides", text="Weathering loosens rock on the sides, and rain and gravity move it down to the river."),
            S("Removal of load", text="The river carries the material away, keeping the valley bottom narrow."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying that rivers cut sideways in the upper course", "The upper course is dominated by **vertical** erosion. Lateral (sideways) erosion is more important in the middle course."),
        MISTAKE("Confusing rapids and waterfalls", "A waterfall is one sharp vertical drop. Rapids are many small steps over a rough bed."),
        MISTAKE("A diagram without labels", "A sketch earns marks only when it is labelled: hard rock, soft rock, plunge pool, overhang and direction of retreat."),
        QUIZ("Which landform is formed when a waterfall retreats upstream?",
             ["Ox-bow lake", "Gorge", "Delta", "Levee"], 1,
             "A gorge is the deep, narrow valley left behind by a retreating waterfall.",
             hint="What is left behind between the old and the new position of the fall?",
             feedback=["An ox-bow lake is made by a meander in the lower course.", "", "A delta is a depositional landform at the mouth.", "A levee is a bank of silt beside a river in flood."]),
        QUIZ("Interlocking spurs are found mainly in the",
             ["upper course", "middle course", "lower course", "delta"], 0,
             "The river is too weak in the upper course to cut through spurs, so it winds around them.",
             hint="Where is the river small and the valley steep?",
             feedback=["", "In the middle course the valley is wider and the river makes meanders.", "In the lower course the land is flat and has a flood plain.", "A delta is at the mouth, where there are no spurs."]),
        TIP("**Exam link.** River landforms appear every year in Paper 2 Section B (physical geography), usually as 'with the aid of diagrams, describe...'. "
            "Paper 1 tests the names and conditions of formation in multiple-choice form.", title="Exam link"),
        H("Practice questions"),
        PQ("Define the terms source, tributary and mouth.",
           "The source is where a river begins. A tributary is a smaller stream that joins a larger river. The mouth is where a river enters the sea or a lake."),
        PQ("Name the three courses of a river and state the main work of the river in each.",
           "Upper course: vertical erosion. Middle course: lateral erosion and transportation. Lower course: deposition."),
        PQ("Describe, with a labelled sketch, how interlocking spurs are formed.",
           "In the upper course the river is too weak to cut through ridges of high ground that project into the valley. It winds around them. "
           "The spurs from the two valley sides overlap like the teeth of a zip. The sketch is a plan with the river winding between labelled staggered spurs."),
        PQ("Explain why a waterfall retreats upstream.",
           "Soft rock below hard rock is eroded faster. The hard rock is undercut and left as an overhang, which collapses. The fall then lies further upstream. "
           "This repeats, so the fall moves back and leaves a gorge."),
        SUM("A river system has a source, tributaries, a confluence and a mouth. It has three courses.",
            "In the upper course the river cuts down (vertical erosion) and makes V-shaped valleys and interlocking spurs.",
            "Waterfalls form where hard rock lies over soft rock. They retreat upstream and leave a gorge. Rapids are many small steps over a rough bed.",
            "Always support your answer with labelled sketches."),
    ],
))

# ------------------------------------------------------------------ 4. Rivers: depositional landforms
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Rivers: meanders, flood plains, levees, deltas and alluvial fans",
    slug="land-rivers-depositional-landforms",
    minutes=24,
    summary="In its middle and lower courses a river erodes sideways and deposits silt. This lesson describes how meanders, ox-bow lakes, flood plains, levees, deltas and alluvial fans are formed.",
    objectives=[
        "Describe and explain the formation of meanders and ox-bow lakes",
        "Describe how flood plains and levees are formed",
        "Explain the conditions for, and the formation of, a delta",
        "Describe an alluvial fan and say where it forms",
    ],
    key_concepts=["Meander", "Slip-off slope", "River cliff", "Ox-bow lake", "Flood plain", "Levee", "Delta", "Distributary", "Alluvial fan"],
    blocks=[
        H("Introduction"),
        T("Farmers in the lowlands of the Benue and along the Logone grow rice and vegetables on flat, fertile ground beside the river. "
          "That fertile soil was laid down by the river itself, in floods, over thousands of years."),
        T("In the middle and lower courses the river has less slope but a lot of load. It swings from side to side, "
          "and it drops silt when it slows down. This lesson covers the landforms that result."),
        H("Meanders"),
        D("A **meander** is a large bend in a river. Meanders are common in the middle and lower courses where the slope is gentle.", title="Meander"),
        T("The fastest water in a river does not run in the centre of a bend. It swings to the **outside** of the bend. "
          "There the river erodes the bank by hydraulic action and abrasion and undercuts it. A steep **river cliff** forms."),
        T("On the **inside** of the bend the water is slow and shallow. It cannot carry all its load, so it deposits sand and gravel. "
          "A gently sloping bank called a **slip-off slope** (or point bar) builds up."),
        IMG("f5g-land-meander.svg", alt="Plan of a meandering river with outer bank erosion and inner bank deposition and a cross-section from A to B with a steep cliff and gentle slope",
            caption="Figure 1. A meander: erosion on the outside of the bend, deposition on the inside."),
        T("Because the outside erodes and the inside builds up, the bend becomes larger and the river slowly moves across its valley."),
        H("Ox-bow lakes"),
        T("As meanders grow, the neck of land between two bends gets narrower. In a flood the river may break through the neck and take the short, straight path. "
          "Silt then seals off the ends of the old bend. The old bend is left as a curved lake, an **ox-bow lake**."),
        IMG("f5g-land-oxbow.svg", alt="Three stages: a meander loop with a narrowing neck, the river cutting through the neck, and a cut-off ox-bow lake",
            caption="Figure 2. From meander to ox-bow lake."),
        D("An **ox-bow lake** is a curved lake that was once a meander. It is cut off when the river takes a shorter route. "
          "In time it fills with silt and plants and becomes a marsh.", title="Ox-bow lake"),
        H("Flood plains and levees"),
        T("The **flood plain** is the flat land on either side of a river in the lower course. "
          "When the river floods, it spreads over the valley floor. The water slows and drops its load as a layer of fine, fertile silt called **alluvium**. "
          "Each flood adds a new layer, and the plain slowly rises."),
        T("**Levees** are natural embankments along the river banks. When water spills over the bank in a flood, it slows suddenly. "
          "The coarse material, which is heaviest, is dropped first, right next to the channel. Finer silt is carried further. "
          "Flood after flood, the banks are built higher than the flood plain beyond."),
        IMG("f5g-land-floodplain.svg", alt="Cross-section of a river valley with a channel between two levees, the flood level and layers of silt on a flat flood plain",
            caption="Figure 3. Flood plain and levees. Layers of silt are added by each flood."),
        TIP("Flood plains are good farmland but risky for homes. People in lowland towns on the Benue or Logone often move to higher ground in the rainy season.", title="Link to people"),
        H("Deltas"),
        D("A **delta** is a low, flat area of land built from silt that a river deposits where it enters a sea or lake. "
          "The river splits into many channels called **distributaries**.", title="Delta"),
        T("A large delta forms only when these conditions are met."),
        KEY("Conditions for a delta", "All are needed together.", cards=[
            ["Large load", "The river brings a great amount of silt and sand from its basin."],
            ["Weak waves and tides", "The sea does not sweep the load away, so it settles."],
            ["Shallow, sheltered water", "The water is shallow and calm, so deposits build up above sea level."],
        ]),
        T("The river slows as it meets the sea and drops its load. The channel is blocked by its own deposits, so it splits and goes around them. "
          "Each new channel is a distributary, and it builds more land. The coast pushes out into the sea."),
        IMG("f5g-land-delta.svg", alt="Plan of a delta with a river splitting into distributaries that spread over fan-shaped new land at the sea",
            caption="Figure 4. A delta with distributaries."),
        T("The **Niger Delta** in Nigeria, west of Cameroon, is one of the largest deltas in Africa. It has many distributaries and mangrove swamps. "
          "In Cameroon, the Wouri and the Sanaga reach the sea in coastal lowlands with mangrove swamps, but they do not make big deltas like the Niger. "
          "Check your textbook for details of the Cameroon river mouths."),
        H("Alluvial fans"),
        T("An **alluvial fan** is a fan-shaped heap of gravel, sand and silt. It forms where a fast mountain stream meets a flat plain. "
          "The stream suddenly loses its slope and energy, and it drops its load. It spreads into many channels. "
          "The coarse material, such as boulders and gravel, is dropped at the apex, and finer sand and silt are carried further to the fan edge."),
        IMG("f5g-land-alluvial-fan.svg", alt="Plan of an alluvial fan with a stream leaving a mountain front, spreading into channels and dropping coarse material near the apex and fine at the edge",
            caption="Figure 5. An alluvial fan at the foot of a mountain."),
        EX("Model answer: formation of a meander and an ox-bow lake", intro="With the aid of diagrams, describe how a meander is formed and how it may become an ox-bow lake.", steps=[
            S("Sketch", text="Draw plan views as in Figures 1 and 2 and label outer bank, inner bank, river cliff, slip-off slope and neck."),
            S("Meander", text="The fastest flow swings to the outside of a bend and erodes it, making a river cliff. The inside is slow, so silt is deposited as a slip-off slope."),
            S("Growth", text="The bend becomes larger. The neck of land between two bends narrows."),
            S("Cut-off", text="In a flood the river breaks through the neck and takes the shorter route."),
            S("Ox-bow lake", text="Deposits seal the ends of the old loop and leave a curved ox-bow lake."),
        ]),
        EX("Model answer: how a delta forms", intro="Explain how a delta forms.", steps=[
            S("Conditions", text="A large load, weak waves and tides, and shallow sheltered water are needed."),
            S("Deposition", text="The river slows as it meets the sea and drops its load. The channel becomes blocked."),
            S("Distributaries", text="The river splits into distributaries that go around the deposits and build more land."),
            S("Result", text="A flat, low area of new land spreads out into the sea."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up the two banks of a meander", "Erosion and the river cliff are on the **outside** of the bend. Deposition and the slip-off slope are on the **inside**."),
        MISTAKE("Saying levees are built by people only", "Natural levees are made by the river's own floods. People may also add artificial levees to protect towns."),
        MISTAKE("Using a delta for every river mouth", "A delta needs a large load and a weak sea. Many river mouths are estuaries, where the sea sweeps the load away."),
        QUIZ("On the inside of a meander bend the river",
             ["erodes strongly and forms a river cliff", "deposits material and forms a slip-off slope", "forms a waterfall", "cuts a gorge"], 1,
             "The water is slow on the inside of a bend, so it deposits sand and gravel as a slip-off slope.",
             hint="Is the water faster or slower on the inside?",
             feedback=["That happens on the outside of the bend.", "", "A waterfall needs a step of hard rock.", "A gorge forms in the upper course."]),
        QUIZ("Levees are made of coarse material because",
             ["the river floods only once", "coarse material is dropped first when floodwater slows at the bank", "wind blows sand onto the banks", "the sea pushes them up"], 1,
             "When the water spills over the bank it slows suddenly, and the heaviest material is dropped next to the channel.",
             hint="Which part of the load is dropped first when the water slows?",
             feedback=["Levees need many floods.", "", "Wind is not the agent here.", "The sea is not involved in making river levees."]),
        TIP("**Exam link.** These landforms are the most popular Paper 2 Section B questions. "
            "Always give conditions, a labelled diagram and the stages in order. Paper 1 tests names, conditions and positions along the river.", title="Exam link"),
        H("Practice questions"),
        PQ("Define a meander.", "A meander is a large bend in a river, common in the middle and lower courses."),
        PQ("Name the two landforms found on the opposite banks of a meander.", "A river cliff on the outside of the bend and a slip-off slope on the inside."),
        PQ("Explain how levees are formed.",
           "In a flood the river spills over its banks and slows. The coarse material is dropped first next to the channel. "
           "After many floods the banks are built up into raised embankments called levees. Finer silt is carried further and forms the flood plain."),
        PQ("State three conditions needed for the formation of a delta.",
           "A river with a large load, weak waves and tides at the mouth, and shallow, sheltered water."),
        SUM("A meander has a river cliff on the outside and a slip-off slope on the inside. If the neck is cut through, an ox-bow lake is left.",
            "Floods deposit alluvium on the flat flood plain. Coarse material forms levees beside the channel.",
            "A delta needs a large load, weak waves and tides and shallow water. The river splits into distributaries.",
            "An alluvial fan forms where a mountain stream meets a plain and loses energy. Coarse material is at the apex."),
    ],
))

# ------------------------------------------------------------------ 5. Wind and water in deserts
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Wind and water action in deserts",
    slug="land-wind-and-water-in-deserts",
    minutes=22,
    summary="Deserts are shaped by wind and by rare but violent floods. This lesson describes deflation, abrasion, mushroom rocks, inselbergs, sand dunes, wadis, playas and salt pans.",
    objectives=[
        "Describe wind erosion by deflation and abrasion and the landforms it makes",
        "Describe and explain the formation of barchans and seif dunes",
        "Describe the work of water in deserts: wadis, playas and salt pans",
        "Draw labelled sketches of desert landforms",
    ],
    key_concepts=["Deflation", "Abrasion", "Mushroom rock", "Inselberg", "Barchan", "Seif dune", "Wadi", "Playa", "Salt pan"],
    blocks=[
        H("Introduction"),
        T("In the Far North Region near Maroua and Lake Chad, the land becomes drier and bare as you go north. In the dry season the harmattan wind blows dust from the Sahara. "
          "Further north, the Sahara is a true desert. A **desert** has very little rain (usually less than 250 mm a year), few plants and a big difference between day and night temperatures."),
        T("Two agents shape a desert: **wind** all the time and **water** rarely. Rare rain falls in sudden storms and runs off bare ground. "
          "Both agents leave landforms that you must be able to describe."),
        H("Wind erosion"),
        T("Wind is a strong agent in deserts because there are few plants to protect the ground and the surface is dry and loose."),
        D("**Deflation** is the lifting and blowing away of loose, fine particles such as dust and sand by the wind. "
          "It lowers the land and can leave a **deflation hollow**. Stones too heavy to blow away are left on the surface.", title="Deflation"),
        D("**Abrasion** is wind-blown sand hitting rock surfaces and wearing them away, like a sandblaster. "
          "Sand grains are heavy, so they bounce close to the ground. Abrasion is greatest near the base of a rock.", title="Abrasion by wind"),
        H("Mushroom rocks and inselbergs"),
        T("A **mushroom rock** is a rock with a narrow base and a wider top. Sand grains blown near the ground abrade the base more than the top. "
          "Over time the base is worn narrow and the top is left wide."),
        T("An **inselberg** (German for 'island mountain') is a steep-sided, rounded hill of hard rock that stands alone on a flat plain. "
          "The softer rock around it has been weathered and eroded away. It stands out like an island. Inselbergs are common in tropical Africa, in dry and savanna areas. "
          "For Cameroonian examples, check your textbook."),
        IMG("f5g-land-mushroom-inselberg.svg", alt="A mushroom rock with a narrow base worn by wind-blown sand, and an inselberg rising steeply from a flat desert plain",
            caption="Figure 1. A mushroom rock and an inselberg."),
        H("Wind deposition: sand dunes"),
        T("Wind drops sand when it slows, for example when it meets an obstacle such as a rock or a bush. The sand piles up and grows into a dune."),
        T("Dunes move slowly downwind. Sand is blown up the gentle windward slope and falls over the crest. It slides down the steep far side, called the **slip face**."),
        D("A **barchan** is a crescent-shaped dune with its horns pointing downwind. It forms where sand is limited and the wind keeps one main direction. "
          "The gentle slope faces the wind and the steep slip face is on the sheltered side.", title="Barchan"),
        D("A **seif** (or longitudinal dune) is a long, narrow ridge of sand that lies in the same direction as the wind. "
          "Seif dunes form where there is plenty of sand and are often in groups with corridors between them.", title="Seif dune"),
        IMG("f5g-land-dunes.svg", alt="Plan view of a barchan and of seif dunes with wind arrows and a side view of a dune with a gentle windward slope and a steep slip face",
            caption="Figure 2. Barchan and seif dunes, and the profile of a dune."),
        TIP("In a drawing, make sure the horns of a barchan point **away from** the wind. A common slip is to draw them pointing into it.", title="Drawing a barchan"),
        H("Water action in deserts"),
        T("Rain is rare in a desert, but it is often sudden and heavy. With few plants and a baked, hard surface, water cannot sink in. "
          "It rushes over the surface as a **flash flood**, carrying large amounts of rock and soil. It is a very powerful agent for a short time."),
        T("A **wadi** (or dry valley) is a river channel in a desert that carries water only after rain. It is steep-sided and often flat-floored, filled with sand and gravel. "
          "Most of the time it is dry."),
        T("Where a wadi leaves the hills, the flood slows and drops gravel and sand in an alluvial fan (see the lesson on rivers)."),
        T("A **playa** is a flat, shallow basin with no outlet to the sea. After rain a temporary lake forms in it. "
          "When the water evaporates in the hot sun, it leaves a flat floor of fine silt. The salt from the water stays behind as a white crust. "
          "This salt-covered area is a **salt pan**."),
        IMG("f5g-land-wadi-playa.svg", alt="Profile from a dry hill down a wadi and alluvial fan to a flat playa with a salt pan",
            caption="Figure 3. Water in deserts: a wadi, an alluvial fan, a playa and a salt pan."),
        EX("Model answer: how a mushroom rock is formed", intro="With the aid of a labelled diagram, describe how a mushroom rock is formed.", steps=[
            S("Sketch", text="Draw Figure 1 (left side): a rock with a narrow base and wider top. Label wind direction, abrasion zone, narrow base and wider top."),
            S("Wind and sand", text="Strong winds in the desert pick up sand grains. The grains are heavy and are carried close to the ground."),
            S("Abrasion", text="The grains strike the base of the rock again and again and wear it away. This is abrasion."),
            S("Shape", text="The upper part is hit less often, so it stays wide while the base is worn narrow, giving a mushroom shape."),
        ]),
        EX("Model answer: how a barchan is formed", intro="Describe the shape of a barchan and explain how it is formed.", steps=[
            S("Shape", text="A crescent-shaped dune. Its horns point downwind. It has a gentle windward slope and a steep slip face."),
            S("Start", text="Wind slows at an obstacle and drops sand, making a small heap."),
            S("Growth", text="The wind carries more sand up the windward slope and over the crest. It falls on the slip face."),
            S("Horns", text="Sand moves faster at the edges, where the heap is thin, so the edges are carried ahead and form the horns."),
            S("Movement", text="The dune slowly moves downwind as sand is moved from the windward to the leeward side."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying deserts have no water action", "Water is rare, but flash floods are very powerful. Wadis, fans and playas are made by water."),
        MISTAKE("Saying mushroom rocks are worn at the top", "Wind-blown sand is carried close to the ground, so the **base** is worn most."),
        MISTAKE("Confusing deflation and abrasion", "Deflation blows loose particles away and lowers the ground. Abrasion uses the sand to wear away rock surfaces."),
        QUIZ("Which landform forms when wind-blown sand wears the base of a rock more than its top?",
             ["Inselberg", "Barchan", "Mushroom rock", "Playa"], 2,
             "Sand bounces near the ground, so the base is abraded most and the rock becomes mushroom-shaped.",
             hint="Think of the shape of the rock after the base is worn.",
             feedback=["An inselberg is an isolated hill that remains after the land around it is lowered.", "A barchan is a dune made of sand.", "", "A playa is a flat dry basin."]),
        QUIZ("A white crust of salt covers the floor of a flat desert basin. It is a",
             ["wadi", "salt pan", "seif dune", "mushroom rock"], 1,
             "A temporary lake dries up in the sun and leaves its salt behind as a salt pan.",
             hint="What is left after salty water evaporates?",
             feedback=["A wadi is a dry river valley.", "", "A seif is a ridge of sand.", "A mushroom rock is a rock shaped by wind abrasion."]),
        TIP("**Exam link.** Desert landforms appear in Paper 1 (multiple choice on names and conditions) and in Paper 2 Section B (physical geography), "
            "where they are often paired with coastal or river features. Sketch maps or labelled sketches earn marks.", title="Exam link"),
        H("Practice questions"),
        PQ("Distinguish between deflation and abrasion.",
           "Deflation is the blowing away of loose, fine particles by the wind, which lowers the surface. Abrasion is the wearing away of rock surfaces by wind-blown sand."),
        PQ("Describe the shape of a barchan.",
           "It is a crescent-shaped dune. The horns point downwind. The windward slope is gentle and the slip face on the sheltered side is steep."),
        PQ("Explain why flash floods are powerful in deserts.",
           "Desert ground is hard, dry and almost bare, so rain cannot sink in. It runs off in a rush over the surface and carries a lot of rock and soil."),
        PQ("Describe how a playa and a salt pan are formed.",
           "After rain a temporary lake forms in a flat basin with no outlet. The water evaporates in the sun and leaves a flat floor of silt. "
           "The salt that was dissolved in the water remains as a white crust, which is the salt pan."),
        SUM("Wind erodes by deflation (blowing away loose particles) and abrasion (sandblasting rocks).",
            "Abrasion near the ground makes mushroom rocks. Inselbergs are hard-rock hills left standing on a plain.",
            "Wind deposits sand as dunes. Barchans are crescents with horns downwind. Seif dunes are long ridges along the wind.",
            "Rare flash floods cut wadis, build fans and fill playas with temporary lakes. Evaporation leaves salt pans."),
    ],
))

# ------------------------------------------------------------------ 6. Waves and coastal landforms
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Wave action and coastal landforms",
    slug="land-waves-and-coastal-landforms",
    minutes=24,
    summary="Waves wear away some coasts and build up others. This lesson explains wave erosion and the landforms it makes (cliffs, platforms, caves, arches, stacks) and the depositional landforms (beaches, spits, bars, tombolos).",
    objectives=[
        "Describe how waves erode the coast",
        "Describe and explain the formation of cliffs, wave-cut platforms, caves, arches and stacks",
        "Explain longshore drift and the formation of beaches, spits and bars",
        "Relate coastal landforms to the Cameroon coast in general terms",
    ],
    key_concepts=["Waves", "Wave-cut platform", "Cliff", "Cave", "Arch", "Stack", "Longshore drift", "Beach", "Spit", "Bar", "Tombolo"],
    blocks=[
        H("Introduction"),
        T("Cameroon has a short Atlantic coast on the Gulf of Guinea. Around Limbe, at the foot of Mount Cameroon, the beaches are covered with dark volcanic sand. "
          "Near Kribi the beaches are lined with palms and the sand is pale. Near Douala the coast is low and muddy, with mangrove swamps along the Wouri estuary."),
        T("Why are these coasts so different? The answer is the work of waves, which erode rocky headlands and deposit sand and mud in sheltered places."),
        H("Wave action"),
        T("**Waves** are made when wind blows over the sea. The stronger the wind and the longer the stretch of open water it blows over, the bigger the waves. "
          "When waves reach the coast, they break. The water that rushes up the beach is the **swash**. The water that runs back down is the **backwash**."),
        T("Waves erode the coast by the same four processes as rivers."),
        KEY("Erosion by waves", "The sea does the work with force, load and chemistry.", cards=[
            ["Hydraulic action", "Waves crash into cracks. Air in the crack is squeezed and then released with force, which breaks rock apart."],
            ["Abrasion", "Waves hurl sand and pebbles at the cliff and wear it away."],
            ["Attrition", "Pebbles knock against each other and become smaller and rounder."],
            ["Solution", "Sea water dissolves some minerals in the rock."],
        ]),
        H("Erosional landforms"),
        T("**Cliffs and wave-cut platforms.** Waves attack the foot of a cliff at the high-tide line. They cut a **wave-cut notch**. "
          "The rock above is left without support and falls. The cliff face retreats inland. "
          "The base of the cliff is cut back, leaving a gently sloping shelf of rock which is the **wave-cut platform**. It is exposed at low tide."),
        IMG("f5g-land-cliff-platform.svg", alt="Cross-section of a cliff with a wave-cut notch at its foot and a wave-cut platform sloping to the sea, with the old cliff position dashed",
            caption="Figure 1. A cliff and wave-cut platform. The cliff retreats inland as the notch is cut."),
        T("**Caves, arches and stacks.** A headland sticks out into the sea, so waves attack it from both sides. The stages are as follows."),
        KEY("From crack to stump", "Four stages on a headland of hard rock with a weakness.", cards=[
            ["1. Crack", "Waves widen a weak crack by hydraulic action and abrasion."],
            ["2. Cave", "Over time the crack becomes a cave."],
            ["3. Arch", "The cave is cut through the headland, making an arch."],
            ["4. Stack and stump", "The roof of the arch collapses and leaves a pillar of rock, the stack. Later the stack is worn down to a low stump."],
        ]),
        IMG("f5g-land-headland-stack.svg", alt="Four panels: a crack in a headland, a cave, an arch and finally a stack and stump",
            caption="Figure 2. From headland to stack and stump."),
        H("Longshore drift"),
        T("Waves usually hit the coast at an angle because the wind blows at an angle. The swash carries sand and pebbles up the beach in the direction of the wind. "
          "The backwash runs straight back down the slope under gravity. The load moves in a zigzag along the coast."),
        D("**Longshore drift** is the movement of sand and pebbles along a coast by waves that hit the beach at an angle.", title="Longshore drift"),
        H("Depositional landforms"),
        T("**Beaches.** A beach is a strip of sand or pebbles at the edge of the sea. It forms in a sheltered bay where the waves are weak and the swash is stronger than the backwash. "
          "Fine sand makes gentle beaches. Pebbles make steeper beaches. The dark sand at Limbe comes from volcanic rock."),
        T("**Spits.** Where the coast changes direction suddenly, such as at a river mouth or a bay, longshore drift keeps moving the load straight on. "
          "The sand builds a long ridge that is joined to the land at one end and stretches out into the water. This is a **spit**. "
          "If the wind and waves change direction, the end of the spit bends into a hook."),
        IMG("f5g-land-spit.svg", alt="Plan of a coast with a sand spit growing from the land across a bay with a curved end and sheltered water behind",
            caption="Figure 3. A spit built by longshore drift."),
        T("The water behind a spit is calm and sheltered. Silt collects there and mangroves or salt marsh may grow."),
        T("**Bars.** A **bar** is a ridge of sand that grows right across the mouth of a bay and closes it. The water behind the bar is a **lagoon**. "
          "A **tombolo** is a bar that joins an island to the mainland."),
        T("Low, sandy coasts with lagoons and mangrove swamps are common along the Cameroon coast, for example near Douala. "
          "For details of local spits and lagoons, check your textbook."),
        EX("Model answer: how a wave-cut platform is formed", intro="With the aid of a labelled diagram, describe how a cliff and a wave-cut platform are formed.", steps=[
            S("Sketch", text="Draw Figure 1 and label the cliff, wave-cut notch, wave-cut platform, sea level and the old cliff position."),
            S("Notch", text="Waves attack the foot of the cliff at high tide by hydraulic action and abrasion and cut a notch."),
            S("Collapse", text="The rock above the notch is unsupported and collapses. The cliff retreats inland."),
            S("Platform", text="The cut-back leaves a gently sloping platform of rock in front of the cliff, shown at low tide."),
        ]),
        EX("Model answer: how a stack is formed", intro="Explain the formation of a stack.", steps=[
            S("Crack", text="Waves attack a headland and enlarge a weak crack."),
            S("Cave", text="The crack widens into a cave."),
            S("Arch", text="The cave is cut right through to make an arch."),
            S("Stack", text="The roof of the arch collapses. A pillar of rock is left separated from the land. This is a stack."),
            S("Stump", text="Waves keep eroding the base until only a low stump remains."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up stacks and stumps", "A stack is a tall pillar of rock. A stump is what is left when the stack is eroded to a low outcrop."),
        MISTAKE("Saying longshore drift moves straight along the beach", "Swash goes up at an angle and backwash goes straight down, so the load moves in a zigzag with an overall movement along the coast."),
        MISTAKE("Saying beaches form on exposed headlands", "Beaches form in sheltered bays where waves are weak. Headlands are eroded."),
        QUIZ("The correct order of features formed on a headland is",
             ["arch, cave, crack, stack", "crack, cave, arch, stack", "cave, crack, stack, arch", "stack, arch, cave, crack"], 1,
             "A crack is widened to a cave, the cave breaks through as an arch, and the arch roof falls to leave a stack.",
             hint="Start from the smallest feature.",
             feedback=["A cave cannot come after an arch.", "", "A crack comes first.", "This is the reverse order."]),
        QUIZ("A long ridge of sand joined to the land at one end and extending into the sea is a",
             ["stack", "tombolo", "spit", "cliff"], 2,
             "A spit is built by longshore drift where the coast changes direction.",
             hint="Which feature is joined to the land at only one end?",
             feedback=["A stack is a pillar of rock.", "A tombolo joins an island to the mainland, so it touches land at both ends.", "", "A cliff is a steep rock face."]),
        TIP("**Exam link.** Coastal landforms appear in Paper 1 (names, order of features) and Paper 2 Section B (physical geography), "
            "where a labelled diagram of cliffs and platforms or of a spit is expected. Section D may link to the Cameroon coast.", title="Exam link"),
        H("Practice questions"),
        PQ("Name the four processes by which waves erode the coast.", "Hydraulic action, abrasion, attrition and solution."),
        PQ("Define longshore drift.",
           "Longshore drift is the movement of sand and pebbles along a coast. Waves hit the beach at an angle, the swash carries material up the beach at that angle "
           "and the backwash returns straight down the slope, so the load moves in a zigzag along the coast."),
        PQ("Describe how an arch becomes a stack.",
           "Waves continue to erode the arch by hydraulic action and abrasion. The roof becomes unsupported and collapses. A pillar of rock is left separate from the land. "
           "This pillar is the stack."),
        PQ("Explain why a spit forms where the coast changes direction.",
           "Longshore drift carries sand along the coast. When the coast bends, the drift keeps moving the sand in the same direction. "
           "The sand is dropped in the calmer water beyond the bend and builds a ridge joined to the land at one end."),
        SUM("Waves erode by hydraulic action, abrasion, attrition and solution.",
            "A wave-cut notch makes the cliff retreat and leaves a wave-cut platform. Headlands become crack, cave, arch, stack and stump.",
            "Longshore drift moves sand in a zigzag along the coast.",
            "Beaches, spits, bars and tombolos are built where waves are weak or where the coast changes direction."),
    ],
))

# ------------------------------------------------------------------ 7. Drainage patterns
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Drainage patterns: dendritic, trellised and radial",
    slug="land-drainage-patterns",
    minutes=20,
    summary="A drainage pattern is the shape that a river and its tributaries make on a map. This lesson defines and illustrates dendritic, trellised and radial patterns, explains the rock and relief behind each and shows how to recognise them.",
    objectives=[
        "Define a drainage pattern",
        "Define and illustrate dendritic, trellised and radial drainage patterns",
        "Explain the rock and relief conditions that produce each pattern",
        "Identify the pattern on a map or sketch",
    ],
    key_concepts=["Drainage pattern", "Dendritic", "Trellised", "Radial", "Tributary", "Resistant rock", "Dome"],
    blocks=[
        H("Introduction"),
        T("Open an atlas or look at a map of the rivers of Cameroon. The Sanaga and its tributaries spread out like the branches of a tree. "
          "Rivers that start on a volcano flow away in different directions like the spokes of a wheel. "
          "In some other lands, rivers run in long parallel lines with short tributaries joining at right angles."),
        T("The shape made by a river and its tributaries is called a **drainage pattern**. The pattern is a clue to the rocks and relief of the land beneath."),
        D("A **drainage pattern** is the arrangement of a river and its tributaries as seen on a map or from the air.", title="Drainage pattern"),
        TIP("The syllabus asks for three patterns only: dendritic, trellised and radial. You do not need others.", title="Scope"),
        H("Dendritic pattern"),
        T("**Dendritic** means 'like a tree' (the Greek word for tree is dendron). The main river is like the trunk and the tributaries are like branches. "
          "Small tributaries branch off larger ones. They join at **acute angles** pointing downstream."),
        IMG("f5g-land-dendritic.svg", alt="Drainage like a tree: a main river with tributaries joining at acute angles and smaller branches",
            caption="Figure 1. Dendritic drainage pattern."),
        KEY("Conditions for dendritic drainage", "The land has no strong guiding structure.", cards=[
            ["Rock", "The same kind of rock everywhere (for example granite or horizontal sedimentary rock), so the rock resists erosion equally."],
            ["Relief", "A gentle slope in one general direction. Rivers can choose any route."],
        ]),
        T("This is the most common pattern. It covers large areas of the world on uniform rock."),
        H("Trellised pattern"),
        T("A **trellis** is a garden frame of crossing strips. In a **trellised** pattern the main rivers run in long, parallel lines. "
          "Their tributaries join them at **right angles**, so the whole pattern looks like a trellis or a rectangular grid."),
        IMG("f5g-land-trellised.svg", alt="Parallel main rivers crossed by tributaries joining at right angles along bands of soft rock between ridges of hard rock",
            caption="Figure 2. Trellised drainage pattern."),
        KEY("Conditions for trellised drainage", "The rocks are in alternating bands of hard and soft rock.", cards=[
            ["Rock", "Layers of resistant (hard) and weak (soft) rock stand side by side, tilted or folded into parallel ridges and valleys."],
            ["Relief", "Long ridges and valleys run parallel. Tributaries follow the soft-rock valleys at right angles to the main river."],
        ]),
        T("Rivers erode soft rock faster than hard rock. They cut valleys in the soft layers and leave the hard layers as ridges."),
        H("Radial pattern"),
        T("**Radial** means 'like the spokes of a wheel'. Rivers begin near a central high point and flow outwards in all directions."),
        IMG("f5g-land-radial.svg", alt="Streams flowing outwards in all directions from a central dome or volcano with circular contour lines",
            caption="Figure 3. Radial drainage pattern."),
        KEY("Conditions for radial drainage", "A single, central high point.", cards=[
            ["Rock", "Often a volcanic cone or a dome of uplifted rock."],
            ["Relief", "A rounded peak or dome with slopes that fall away in all directions. Contour lines are circular."],
        ]),
        T("A volcano, such as Mount Cameroon, is a good example of a high point from which streams flow outwards. "
          "On young volcanic rock some water may sink in. For a named example check your textbook."),
        H("Recognising drainage patterns on a map"),
        T("Follow these steps whenever you meet a river map."),
        KEY("Four steps", "Ask the questions in this order.", cards=[
            ["1. Look at the angles", "Right angles point to trellised. Acute angles in a branching form point to dendritic."],
            ["2. Look at the main rivers", "Parallel lines point to trellised. One trunk with branches points to dendritic."],
            ["3. Look at the centre", "Streams leaving a central point (and circular contours) point to radial."],
            ["4. Give the reason", "Name the rock and relief, such as uniform rock, bands of hard and soft rock, or a dome."],
        ]),
        EX("Model answer: define and illustrate a trellised drainage pattern", intro="Define a trellised drainage pattern, draw a sketch and explain how it forms.", steps=[
            S("Definition", text="A trellised pattern has long parallel main rivers with tributaries joining them at right angles, like a garden trellis."),
            S("Sketch", text="Draw two parallel rivers, short tributaries at right angles between them and label main river, tributary and right angle. Shade hard rock ridges."),
            S("Rock condition", text="It forms where hard and soft rocks lie in parallel bands."),
            S("Explanation", text="The rivers cut valleys along the soft rock and leave ridges of hard rock. Tributaries follow the valleys and join the main river at right angles."),
        ]),
        EX("Model answer: identify and explain a pattern from a description", intro="Rivers on a map flow outwards from the top of a circular hill in all directions. Name the pattern and explain it.", steps=[
            S("Name", text="This is a radial drainage pattern."),
            S("Clue", text="The streams start close to the central high point and spread out like spokes."),
            S("Cause", text="The central high point is a dome or volcano, so the land slopes away on all sides."),
            S("Conclusion", text="Water simply follows the slope, so the rivers flow in every direction."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling every branching pattern dendritic", "Check the angles. If tributaries meet the main river at right angles, it is trellised."),
        MISTAKE("Giving no cause", "A definition is not enough. Name the rock and relief conditions for each pattern."),
        MISTAKE("Mixing up radial and dendritic", "In a radial pattern the rivers start from a centre and spread out. In a dendritic pattern the rivers join to make one main river."),
        QUIZ("Which drainage pattern shows long parallel rivers with tributaries joining at right angles?",
             ["Dendritic", "Radial", "Trellised", "Centripetal"], 2,
             "A trellised pattern forms over alternating bands of hard and soft rock.",
             hint="Think of a garden trellis.",
             feedback=["A dendritic pattern has branching tributaries at acute angles.", "A radial pattern has rivers spreading from a centre.", "", "Centripetal drainage is not in this syllabus."]),
        QUIZ("A volcanic cone with streams flowing away from the top in all directions is most likely to show a",
             ["trellised pattern", "radial pattern", "dendritic pattern", "parallel pattern"], 1,
             "Radial drainage forms around a central high point where the slope falls away in all directions.",
             hint="Which pattern looks like the spokes of a wheel?",
             feedback=["Trellised needs alternating hard and soft rock bands.", "", "Dendritic forms on uniform rock with a gentle general slope.", "Parallel drainage is not one of the three patterns."]),
        TIP("**Exam link.** Drainage patterns come up in Paper 1 (identify the pattern from a sketch or map) and in Paper 2 Section A (map reading, interpreting rivers) "
            "and Section B (describe and illustrate). Practise sketching all three in under two minutes each.", title="Exam link"),
        H("Practice questions"),
        PQ("Define a drainage pattern.", "A drainage pattern is the arrangement of a river and its tributaries as seen on a map or from the air."),
        PQ("Name the drainage pattern that looks like a tree and state the rock conditions for it.",
           "Dendritic. It forms on uniform rock that resists erosion equally, with a gentle slope."),
        PQ("Draw and label a sketch of a radial drainage pattern and state where it forms.",
           "Sketch: a central high point with circular contours and streams spreading out from it like spokes. It forms around a volcano or a dome."),
        PQ("Explain how bands of hard and soft rock produce a trellised pattern.",
           "Rivers erode soft rock faster than hard rock, so they cut valleys along the soft bands. The hard bands remain as parallel ridges. "
           "Main rivers run along the ridges, and tributaries run along the soft-rock valleys and join them at right angles."),
        SUM("A drainage pattern is the shape formed by a river and its tributaries.",
            "Dendritic is tree-like and forms on uniform rock with a gentle slope.",
            "Trellised has parallel main rivers with right-angle tributaries and forms over alternating bands of hard and soft rock.",
            "Radial spreads out from a central high point, such as a volcano or dome."),
    ],
))

# ------------------------------------------------------------------ 8. Denudational hazards
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Denudational hazards: landslides, rockfall, mudflow and gas explosions",
    slug="land-denudational-hazards",
    minutes=24,
    summary="Slope and ground processes can kill people and destroy property. This lesson describes landslides, rockfall, mudflow and natural gas explosions, their causes and effects, and how they can be prevented or reduced, with the Cameroon hillsides as the main context.",
    objectives=[
        "Describe landslides, rockfall, mudflow and natural gas explosions",
        "Explain the natural and human causes of these hazards",
        "Outline the effects of the hazards on people and the environment",
        "Outline preventive and mitigation strategies for them",
    ],
    key_concepts=["Hazard", "Landslide", "Rockfall", "Mudflow", "Natural gas explosion", "Mitigation", "Prevention", "Early warning"],
    blocks=[
        H("Introduction"),
        T("In the rainy season, news from the Western Highlands sometimes reports that a hillside has slipped onto houses or blocked a road. "
          "The towns of the region, such as Bamenda and Bafoussam, are built on and among steep hills. Heavy rain, steep slopes and crowded settlement together make landslides a real threat."),
        D("A **hazard** is a natural or human-made event that can harm people, property or the environment.", title="Hazard"),
        T("**Denudational hazards** are hazards that come from the wearing down of land and the movement of rock and soil. "
          "In this lesson you will study four: landslides, rockfall, mudflow and natural gas explosions."),
        H("Landslides"),
        D("A **landslide** is the rapid downhill movement of a mass of soil, loose rock and plants along a slope.", title="Landslide"),
        T("A landslide usually has a surface along which the mass slips, called the **slip plane**. "
          "It often occurs where a layer of weathered rock and soil, the regolith, lies over solid rock that water cannot pass through."),
        IMG("f5g-land-landslide.svg", alt="Cross-section of a hillside with loose soil over solid rock, a slip plane, a mass of soil sliding downhill and debris at the foot",
            caption="Figure 1. A landslide: heavy rain soaks the regolith, which slips along a slip plane."),
        KEY("Causes of landslides", "A steep slope plus something that weakens it or pushes it.", cards=[
            ["Natural causes", "Heavy or long rain that soaks the soil and adds weight. Steep slopes. Deep weathered soil over solid rock. Earthquakes or volcanic activity that shake the ground."],
            ["Human causes", "Cutting down forest, so roots no longer bind the soil. Cutting into slopes for roads or houses. Poor drainage. Quarrying. Building heavy structures on slopes."],
        ]),
        H("Rockfall, mudflow and natural gas explosions"),
        T("**Rockfall** is the fall of single rocks or blocks from a steep cliff or rock face. "
          "Weathering widens cracks, and rocks break loose and fall, roll or bounce. Piles of loose rock called **scree** form at the foot."),
        T("**Mudflow** is the flow of soil that is soaked in water, like thick liquid mud. It travels down valleys and channels and can move fast and far. "
          "It is common where heavy rain falls on loose soil on a steep slope, and also near some volcanoes."),
        T("**Natural gas explosion.** Natural gas is mainly methane, a gas that burns easily. It collects in underground pockets in rock and in the rock around wells and mines. "
          "It may escape through cracks, wells or leaking pipes. When it mixes with air and meets a spark or flame, it explodes and burns."),
        IMG("f5g-land-hazard-types.svg", alt="Three panels: rockfall from a steep cliff to a scree slope, a mudflow flowing down a slope to houses, and a gas pocket under a building",
            caption="Figure 2. Rockfall, mudflow and a gas explosion."),
        KEY("Causes in short", "Each hazard has its own main triggers.", cards=[
            ["Rockfall", "Steep rock faces, weathering of cracks, rain, earthquakes, quarrying and blasting."],
            ["Mudflow", "Heavy rain on loose soil on slopes, bare ground without plants, volcanic activity."],
            ["Gas explosion", "Gas escaping from underground pockets, wells, mines or damaged pipes, near a spark or flame."],
        ]),
        H("Effects of the hazards"),
        T("**On people.** Deaths and injuries. Homes, schools and roads are destroyed. Families lose their land and belongings and must move away."),
        T("**On the economy.** Farmland and crops are buried. Roads and bridges are cut, so markets and towns are cut off. "
          "Governments and families pay for repairs and relief. Mines and wells may have to close after a gas explosion."),
        T("**On the environment.** Forests are torn away. Rivers are blocked by debris and may flood. The silt makes streams muddy. Fires after gas explosions can spread."),
        H("Prevention and mitigation"),
        T("**Prevention** means stopping the hazard from happening. **Mitigation** means reducing its harm when it cannot be stopped. "
          "A good answer gives both."),
        IMG("f5g-land-slope-protection.svg", alt="A protected hillside with trees, terraces, a retaining wall at the foot, a drain and houses well away from the slope foot",
            caption="Figure 3. Protecting a slope from landslides."),
        KEY("Strategies for slopes", "Plant, shape, support and drain.", cards=[
            ["Plant trees and grass", "Roots bind the soil. Leaves slow the rain. Afforestation protects bare slopes."],
            ["Terrace the slope", "Steps cut into the hill slow the water and make the slope flatter and safer for farming."],
            ["Build supports", "Retaining walls at the foot of slopes, and fences or nets below cliffs to catch falling rocks."],
            ["Improve drainage", "Drains and channels carry rainwater away so soil does not become soaked."],
            ["Plan and warn", "No building on very steep or weak slopes. Hazard maps. Early warning when rain is heavy. Evacuation plans and education of the public."],
        ]),
        T("For **natural gas** hazards, the main strategies are to detect and seal leaks, keep wells and pipes in good condition, "
          "ventilate mines and enclosed places and ban naked flames near gas vents. Workers need training and rules must be enforced."),
        H("Worked examples"),
        EX("Model answer: causes of landslides on West Cameroon hillsides", intro="Explain why landslides are a danger on the steep hillsides of western Cameroon.", steps=[
            S("Point 1: steep slopes", text="Much of the Western Highlands is steep. Gravity pulls loose soil downhill."),
            S("Point 2: heavy rain", text="Heavy rain in the wet season soaks the thick regolith. This makes it heavy and slippery, so it slides over the rock below."),
            S("Point 3: human action", text="People cut trees and dig into slopes for roads and houses. Roots no longer hold the soil and slopes are cut too steep."),
            S("Point 4: crowded settlement", text="Many houses are built on or below slopes, so more people are at risk."),
            S("Conclusion", text="A steep slope, heavy rain and human clearing of the slope together explain the danger."),
        ]),
        EX("Model answer: reducing the harm of landslides", intro="Outline measures that can reduce the effects of landslides.", steps=[
            S("Before: plant", text="Plant trees and grass on slopes. Roots bind the soil."),
            S("Before: shape and support", text="Build terraces and retaining walls. Improve drainage to remove rainwater."),
            S("Before: plan", text="Do not allow houses on very steep slopes or at the foot of unstable hills. Make hazard maps."),
            S("During: warn", text="Give an early warning in periods of heavy rain and move people to safe places."),
            S("After: relief", text="Rescue people, give shelter and food, and clear roads."),
        ]),
        H("Common mistakes"),
        MISTAKE("Blaming only nature", "Heavy rain alone does not cause most landslides. Human actions such as clearing trees and digging into slopes make them far more likely."),
        MISTAKE("Mixing prevention and mitigation", "Prevention stops the hazard. Mitigation reduces damage. Terraces and trees are prevention. Early warning and evacuation are mitigation."),
        MISTAKE("Calling mudflow and landslide the same", "A landslide is a mass of soil and rock sliding on a slip plane. A mudflow is a flow of soil mixed with so much water that it moves like thick liquid."),
        QUIZ("Which action would make a hillside landslide MORE likely?",
             ["Planting trees", "Building terraces", "Cutting down the forest on the slope", "Digging drains"], 2,
             "Roots bind the soil. Without them, rain easily loosens it.",
             hint="Which action removes something that holds the soil?",
             feedback=["Trees reduce landslide risk.", "Terraces reduce the risk.", "", "Drains remove water and reduce the risk."]),
        QUIZ("An early warning system and an evacuation plan are examples of",
             ["prevention", "mitigation", "deposition", "weathering"], 1,
             "Mitigation reduces harm when a hazard happens. A warning gives people time to move to safety.",
             hint="Do they stop the hazard happening or reduce the harm?",
             feedback=["Prevention stops the hazard; a warning does not stop it.", "", "Deposition is a process of landform building.", "Weathering is the breaking down of rock."]),
        TIP("**Exam link.** Denudational hazards appear in Paper 1 (causes, effects, strategies) and in Paper 2 Section B (physical geography). "
            "Section D may ask about hazards in Cameroon, where you can use the West Cameroon hillsides as a general example. "
            "For named events, check your textbook.", title="Exam link"),
        H("Practice questions"),
        PQ("Define a landslide.", "A landslide is the rapid downhill movement of a mass of soil, loose rock and plants along a slope."),
        PQ("State two human causes of landslides.", "Cutting down forest on slopes, cutting into slopes for roads or houses, poor drainage or quarrying. Any two."),
        PQ("Describe two effects of landslides on people.",
           "People are killed or injured. Houses, roads and schools are destroyed, so families lose their homes and their land. Farms may be buried and markets cut off."),
        PQ("Outline measures that can prevent or reduce landslides on a hillside.",
           "Plant trees and grass, build terraces and retaining walls, improve drainage, avoid building on steep slopes, make hazard maps and give early warnings in heavy rain."),
        SUM("Landslides, rockfall, mudflow and natural gas explosions are denudational hazards.",
            "Causes combine nature (steep slopes, heavy rain, weak regolith) and people (cutting trees and slopes, poor drainage, quarrying).",
            "Effects include deaths, destroyed homes and roads, buried farmland and blocked rivers.",
            "Prevention includes planting trees, terracing, retaining walls and drains. Mitigation includes hazard maps, early warning and evacuation."),
    ],
))
