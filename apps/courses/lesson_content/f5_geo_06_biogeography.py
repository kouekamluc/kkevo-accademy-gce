"""Form 5 Geography: Biogeography (soil, vegetation and ecosystems). 7 lessons, one practice set each.

The Board treats these as elementary concepts: soil-forming processes and biomes other than the tropical
rainforest, tropical grassland (savanna) and tropical desert are not studied in detail.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Biogeography"
SOIL = "Soil"
VEG = "Vegetation"
ECO = "Ecosystems"

LESSONS = []

# ------------------------------------------------------------------ 1. Soil components and profile
LESSONS.append(lesson(
    module=MODULE,
    topic=SOIL,
    title="Soil: its components and the soil profile",
    slug="bio-soil-components-and-the-soil-profile",
    minutes=20,
    summary="What soil is, the five things it contains (mineral particles, humus, air, water and living things) and how to draw and label the four horizons (O, A, B and C) of a soil profile.",
    objectives=[
        "Define soil and outline its components",
        "Illustrate the main layers (horizons) of the soil profile with a labelled diagram",
        "Describe the characteristics of each horizon",
        "Explain why the topsoil is the most important layer for farming",
    ],
    key_concepts=["Soil", "Mineral particles", "Humus", "Soil air and water", "Soil profile", "Horizon", "Topsoil", "Subsoil", "Bedrock"],
    blocks=[
        H("Introduction"),
        T("A farmer in Bamenda digs a hole to plant cocoyams. The top of the hole is dark and crumbly. Deeper down, the "
          "earth is lighter and harder. At the bottom, there are stones. Without knowing it, the farmer has just "
          "looked at a **soil profile**."),
        T("Soil is where most of our food grows. Maize, cassava, plantains, groundnuts and cocoa all depend on it. "
          "In this lesson you will learn what soil is made of and how it is arranged in layers."),
        D("**Soil** is the thin, loose layer on the surface of the Earth made of broken rock, dead plant and animal matter, "
          "air and water, in which plants grow.", title="Definition: soil"),
        H("What soil is made of"),
        T("Good soil is a mixture. It contains five main components. Look at the pie chart to see the usual share of "
          "the first four. The exact amounts change from one soil to another."),
        IMG("f5g-bio-soil-components.svg", alt="Pie chart of a typical good soil: mineral particles about 45 percent, water about 25 percent, air about 25 percent, organic matter about 5 percent",
            caption="Figure 1. The approximate make-up of a typical good soil by volume."),
        KEY("The five components of soil", "Each one has a job.", cards=[
            ["Mineral particles", "Tiny pieces of rock (sand, silt and clay). They are the largest part of soil and give it its texture."],
            ["Organic matter", "Dead leaves, roots and animals that are rotting. The dark, rotted part is called humus."],
            ["Air", "Fills the gaps between particles. Roots and soil animals need oxygen to live."],
            ["Water", "Held in the gaps. Plants take up water and dissolved minerals through their roots."],
            ["Living things", "Earthworms, termites, insects, fungi and bacteria. They mix the soil and rot dead matter."],
        ]),
        D("**Humus** is dark, rotted organic matter. It holds water and nutrients and makes soil fertile.", title="Definition: humus"),
        T("Mineral particles come in three sizes. **Sand** is the largest and feels rough. **Silt** is in the middle. "
          "**Clay** is the smallest and feels sticky when wet. Sandy soil lets water drain very fast. Clay soil holds water "
          "and may become waterlogged. A mixture of the three, called loam, is best for most crops."),
        TIP("Do not forget the fifth component. Many students list only rock, air, water and humus. Living things "
            "are a component too, and examiners award a mark for them."),
        H("The soil profile"),
        T("If you dig a trench through the soil, you can see that it is arranged in layers. Each layer is called a "
          "**horizon**. The vertical cut through all the horizons is the **soil profile**."),
        D("A **soil profile** is a vertical section through the soil from the surface down to the bedrock, showing its "
          "layers (horizons).", title="Definition: soil profile"),
        IMG("f5g-bio-soil-profile.svg", alt="Soil profile with four horizons: O horizon leaf litter, A horizon topsoil, B horizon subsoil, C horizon broken rock, and bedrock below",
            caption="Figure 2. A simple soil profile with the O, A, B and C horizons above the bedrock."),
        KEY("The horizons from top to bottom", "Learn them in this order.", cards=[
            ["O horizon", "A thin layer of leaf litter and humus on the surface. Not always shown in simple diagrams."],
            ["A horizon (topsoil)", "Dark and rich in humus. Full of roots and living things. The most fertile layer."],
            ["B horizon (subsoil)", "Lighter in colour, with little humus. Holds minerals and clay washed down from the A horizon."],
            ["C horizon", "Large and small pieces of weathered rock. Roots rarely reach it."],
            ["Bedrock", "The solid rock below, from which the soil's mineral particles came."],
        ]),
        T("The layers change slowly, not sharply. A profile shows the pattern in the most common soils. The thickness "
          "of each horizon differs from place to place. For example, soils on steep slopes are thinner than soils "
          "on flat plains."),
        EX("Model answer: draw and label a soil profile", intro="Draw a labelled diagram of a soil profile. (5 marks)", steps=[
            S("Draw a tall rectangle", text="Divide it with horizontal lines into four or five layers. Make the top layer thin and the A and B layers thicker."),
            S("Label the horizons in order", text="Write O (litter), A (topsoil), B (subsoil), C (weathered rock) and bedrock from top to bottom."),
            S("Add a short note to each label", text="Topsoil: dark, humus, roots. Subsoil: lighter, minerals washed down. C: broken rock. Bedrock: solid rock."),
            S("Add an arrow and a title", text="Draw an arrow marked depth going down. Write the title Soil profile above the diagram."),
        ]),
        EX("Model answer: why is topsoil so important?", intro="Explain why the topsoil (A horizon) is the most important layer for farmers. (4 marks)", steps=[
            S("Point 1: it is rich in humus", text="Humus holds water and nutrients, so crops get food. It also makes the soil crumbly, so roots can spread."),
            S("Point 2: most roots are here", text="Roots of maize, beans and vegetables stay mostly in the A horizon, so this is where they take up water and nutrients."),
            S("Point 3: many living things", text="Earthworms, termites and bacteria are most active here. They mix the soil and rot dead matter into humus."),
            S("Conclusion", text="If the topsoil is washed away, crop yields fall quickly. This is why farmers must protect it."),
        ]),
        MISTAKE("Mixing up the order of the horizons", "Remember the order from the top: O, A, B, C. A helpful phrase is "
                "Organic, Above, Below, Crumbled rock. Always write the letters on your diagram and name each layer."),
        MISTAKE("Calling the soil profile a type of soil", "The profile is not a kind of soil. It is a vertical cut that shows the layers. "
                "Say 'a soil profile shows the layers (horizons) of the soil'."),
        QUIZ("Which horizon is usually the darkest and most fertile?",
             ["The B horizon", "The A horizon", "The C horizon", "The bedrock"], 1,
             "The A horizon (topsoil) contains the most humus, so it is dark, rich in nutrients and full of roots.",
             hint="Humus is dark and is found near the surface.",
             feedback=["The B horizon is lighter and has little humus.", "",
                       "The C horizon is mostly broken rock with very little organic matter.",
                       "Bedrock is solid rock and has no humus."]),
        QUIZ("Which of the following is the organic part of soil?",
             ["Sand", "Clay", "Humus", "Pieces of weathered rock"], 2,
             "Humus is made from rotted plants and animals, so it is organic. Sand, clay and rock pieces are mineral.",
             hint="Organic means it comes from living things.",
             feedback=["Sand is a mineral particle from rock.", "Clay is a very small mineral particle.", "",
                       "Weathered rock is mineral, not organic."]),
        TIP("Exam link: Paper 1 (multiple choice) often asks you to name a horizon or a component. Paper 2 Section B can ask "
            "you to define soil, list its components and draw and label a soil profile. A neat labelled sketch earns "
            "most of the marks.", title="Exam link"),
        PQ("Define soil and name the five components of soil.",
           "Soil is the thin, loose surface layer of the Earth made of broken rock, dead organic matter, air and water, in which plants grow. "
           "The five components are mineral particles, organic matter (humus), air, water and living organisms such as worms and bacteria."),
        PQ("Draw a labelled diagram of a soil profile showing four layers above the bedrock.",
           "The diagram shows a vertical rectangle with, from the top, the O horizon (leaf litter and humus), the A horizon (dark topsoil with "
           "roots), the B horizon (lighter subsoil with minerals washed down), the C horizon (broken rock) and the solid bedrock below. "
           "Each layer is labelled and the diagram has a title."),
        PQ("Describe the difference between topsoil and subsoil.",
           "The topsoil (A horizon) is dark, rich in humus, full of roots and living things and is the most fertile layer. The subsoil "
           "(B horizon) is lighter, contains little humus and holds minerals and clay washed down from the topsoil. Fewer roots grow there."),
        PQ("Explain why a mixture of sand, silt and clay (loam) is good for farming.",
           "Sand makes the soil loose so that water drains and air can enter. Clay holds water and nutrients. Silt is in between. "
           "Together they give a soil that holds enough water without becoming waterlogged and that roots can grow through easily."),
        SUM("Soil is the thin, loose layer of broken rock, dead matter, air and water in which plants grow.",
            "The components are mineral particles, organic matter (humus), air, water and living things.",
            "A soil profile is a vertical section showing the horizons: O, A, B, C and then the bedrock.",
            "The A horizon (topsoil) is dark, rich in humus and the most fertile. The B horizon (subsoil) is lighter and holds minerals washed down.",
            "In the exam, draw a neat labelled profile and give one note for each layer."),
    ],
))

# ------------------------------------------------------------------ 2. Main soil types and climate zones
LESSONS.append(lesson(
    module=MODULE,
    topic=SOIL,
    title="Main soil types and the climatic zones they belong to",
    slug="bio-main-soil-types-and-climate-zones",
    minutes=20,
    summary="The main tropical soils (red ferrallitic, tropical black clay and desert soils), where each is found, how climate and vegetation shape them and why rainforest soils are red but not very fertile.",
    objectives=[
        "State the major soils in relation to the tropical climatic zones",
        "Describe the main characteristics of ferrallitic, tropical black clay and desert soils",
        "Explain the link between climate, vegetation and soil",
        "Identify typical soil types in Cameroon and name where they occur",
    ],
    key_concepts=["Ferrallitic soil", "Tropical black clay soil", "Desert soil", "Leaching", "Climatic zone", "Soil fertility"],
    blocks=[
        H("Introduction"),
        T("Travel by road from Douala to Maroua and you cross all of Cameroon's climates. In the south the earth is red and the "
          "forest is thick. In the Adamawa the land opens into grassland. Near Maroua the land is dry, with thorny trees "
          "and pale, sandy ground."),
        T("The soil changes as the climate changes. This lesson looks at the main soil types of the tropics and shows how "
          "climate, vegetation and soil are linked."),
        T("The Board asks for the major soils in relation to climatic zones. We keep to the main tropical types. For extra soil "
          "types such as soils of cooler climates, check your textbook."),
        D("A **climatic zone** is a large region with a similar pattern of temperature and rainfall. In this course we use the "
          "tropical humid, tropical wet and dry, and tropical dry zones.", title="Definition: climatic zone"),
        H("Why climate affects soil"),
        T("Rain and heat act on the rock and on the dead plant matter. They decide how fast rock breaks up and how fast "
          "leaves rot. They also decide how much water moves down through the soil."),
        D("**Leaching** is the washing of soluble minerals and nutrients downwards out of the topsoil by water moving down "
          "through the soil.", title="Definition: leaching"),
        T("In very wet places, leaching is strong. In dry places, there is little water to move anything, and soils stay thin."),
        IMG("f5g-bio-transect.svg", alt="Cross-section from the humid south to the dry north showing tropical rainforest with red ferrallitic soil, savanna with red-brown and black clay soil and desert with thin sandy soil",
            caption="Figure 1. Climate, vegetation and soil change together from the humid south to the dry north."),
        H("Ferrallitic (red tropical) soils"),
        KEY("Ferrallitic soils", "Found in the tropical humid (equatorial) zone, under rainforest.", cards=[
            ["Where", "Hot, wet areas with rain all year, such as the forest of southern Cameroon and the Congo Basin."],
            ["Colour", "Red or yellow-red, because iron and aluminium compounds are left behind after other minerals are washed out."],
            ["Texture", "Deep, with a lot of clay. The soil is often several metres deep."],
            ["Fertility", "Low once the forest is cleared. Heavy rain leaches nutrients and the humus layer is thin."],
        ]),
        T("This surprises many students. The rainforest is lush, but the soil beneath it is not rich. Dead leaves rot in "
          "days in the heat and damp. The forest takes up the nutrients straight away. Most nutrients are stored in the "
          "living trees, not in the soil."),
        T("When farmers clear the forest, this quick recycling stops. The first crops grow well. After a few years, "
          "the nutrients are used up and washed away, and yields fall. This is why shifting cultivation is common in the "
          "forest zone."),
        H("Tropical black clay soils"),
        KEY("Tropical black clay soils", "Found mainly in the tropical wet and dry (savanna) zone.", cards=[
            ["Where", "Savanna areas with a clear dry season, especially flat, low-lying land. Check your textbook for local names."],
            ["Colour", "Dark grey or black, because of fine clay and organic matter."],
            ["Texture", "Very sticky and heavy when wet. In the dry season it shrinks and cracks deeply."],
            ["Fertility", "Often fertile because it holds nutrients and water. But it is hard to work, both wet and dry."],
        ]),
        T("In the Far North region, dark clay soils are used for sorghum grown in the dry season. They hold water "
          "after the rains end. Check your textbook for the local name and crops."),
        T("Other savanna soils are red-brown and sandy to loamy, with a thinner humus layer than forest soil. They "
          "support grassland and scattered trees."),
        H("Desert soils"),
        KEY("Desert soils", "Found in the tropical dry zone with very little rain.", cards=[
            ["Where", "Hot deserts such as the Sahara and the dry Sahel edge near Lake Chad."],
            ["Colour", "Pale: grey, yellow or light brown."],
            ["Texture", "Thin, sandy or stony. Wind has often blown the fine particles away."],
            ["Fertility", "Very low. Almost no humus, and sometimes salty. Crops grow only where water is supplied (irrigation or an oasis)."],
        ]),
        CODE(
            "Zone            Rainfall          Natural vegetation   Main soil\n"
            "--------------  ----------------  -------------------  ----------------------\n"
            "Tropical humid  Over 1500 mm      Rainforest           Red ferrallitic\n"
            "Wet and dry     About 600-1500mm  Savanna grassland    Red-brown, black clay\n"
            "Tropical dry    Under 250 mm      Thorn scrub, sparse  Thin, sandy desert soil",
            "text", title="Table 1. Climate, vegetation and soil in the tropics (approximate rainfall)"),
        TIP("When you answer, always link the three: the climate gives the vegetation, the vegetation gives the "
            "humus, and the climate and humus together give the soil."),
        T("Soil does not depend on climate alone. Some soils depend mostly on the rock beneath. For example, the volcanic "
          "slopes of Mount Cameroon and parts of the Western Highlands have soils formed from lava. These are often very "
          "fertile. Check your textbook for details."),
        EX("Model answer: explain why the soils of the rainforest are red but not very fertile", intro="Explain why soils under tropical rainforest are red and have low fertility once the forest is cleared. (5 marks)", steps=[
            S("Point 1: heavy rain and heat", text="The climate is hot and wet all year, so rock breaks down deeply and large amounts of water move down through the soil."),
            S("Point 2: leaching", text="The water washes soluble minerals and nutrients out of the topsoil. This is leaching."),
            S("Point 3: the red colour", text="Iron and aluminium compounds are left behind. The iron gives the red or yellow-red colour."),
            S("Point 4: fast recycling", text="Humus layer is thin because dead leaves rot fast and the trees take up the nutrients quickly."),
            S("Conclusion", text="When the forest is cleared, the nutrient supply stops and heavy rain leaches the rest, so fertility falls."),
        ]),
        EX("Model answer: describe the link between climate, vegetation and soil in the savanna", intro="Describe how climate, vegetation and soil are linked in a savanna area. (4 marks)", steps=[
            S("Climate", text="Savanna has a wet season and a dry season, with rainfall of about 600 to 1500 mm a year."),
            S("Vegetation", text="This supports tall grass and scattered trees, not dense forest. Grass dies back in the dry season."),
            S("Soil", text="Less leaching and less leaf fall than in the forest give red-brown or black clay soils with moderate humus."),
            S("Link", text="Each part depends on the others: rainfall controls plants, plants supply humus, and the humus and climate form the soil."),
        ]),
        MISTAKE("Saying the rainforest has very fertile soil", "Lush plants do not mean rich soil. Most nutrients are in the living "
                "plants, and heavy rain leaches the soil. Explain this in your answer."),
        MISTAKE("Giving the wrong colour reason", "Ferrallitic soils are red because of iron compounds left behind after leaching, "
                "not because of burning or dead leaves."),
        QUIZ("Which soil is typical of the tropical rainforest zone?",
             ["Thin, pale desert soil", "Red ferrallitic soil", "Black cracking clay soil only", "Volcanic soil only"], 1,
             "Red ferrallitic soils form in the hot, wet climate where heavy leaching leaves iron compounds behind.",
             hint="Think of the red earth along forest roads in southern Cameroon.",
             feedback=["Desert soil is thin and pale because of very little rain.", "",
                       "Black clay soils are typical of savanna areas with a dry season.",
                       "Volcanic soils depend on the rock, not on the rainforest climate."]),
        QUIZ("What is leaching?",
             ["Wind blowing soil away", "Water washing nutrients downwards out of the topsoil", "Plants taking up water", "Animals digging in the soil"], 1,
             "Leaching is the downward washing of soluble minerals by water moving through the soil.",
             hint="It involves water moving down through the soil.",
             feedback=["That is wind erosion, not leaching.", "", "That is plant uptake, not leaching.", "That is mixing by soil animals."]),
        TIP("Exam link: Paper 1 asks which soil goes with which climate or vegetation. Paper 2 Section B asks you to describe soils "
            "of a zone and explain the link with climate. Use the table above as your revision card.", title="Exam link"),
        PQ("State the main soil of the tropical humid zone, the tropical wet and dry zone and the tropical dry zone.",
           "The tropical humid zone has red ferrallitic soils. The tropical wet and dry (savanna) zone has red-brown and black clay soils. "
           "The tropical dry zone has thin, pale, sandy desert soils."),
        PQ("Describe two characteristics of desert soils.",
           "Desert soils are thin and sandy or stony because little rock breaks down and wind removes fine particles. They contain very little "
           "humus because few plants grow, so they have low fertility and are often pale in colour."),
        PQ("Explain why farming on ferrallitic soils is difficult after the forest has been cleared.",
           "The nutrients are stored in the trees, so when the forest is cleared the supply stops. The humus layer is thin. Heavy rain leaches "
           "the remaining nutrients and may erode the bare soil. Yields therefore fall after a few years."),
        PQ("Explain how climate affects the type of soil that forms in an area.",
           "Climate controls how fast rock breaks up and dead plants rot, and how much water moves through the soil. Hot, wet climates cause "
           "deep weathering and strong leaching, giving red ferrallitic soils. Dry climates cause thin soils with little humus. Climate also "
           "controls the vegetation, which provides the humus."),
        SUM("Climate, vegetation and soil are linked: rainfall and temperature decide the plants and the soil.",
            "Ferrallitic soils are red, deep and leached. They are found under rainforest and are not very fertile once the trees are cleared.",
            "Tropical black clay soils and red-brown soils belong to the savanna. Black clays are often fertile but hard to work.",
            "Desert soils are thin, sandy and pale, with very little humus.",
            "Leaching is the downward washing of nutrients. It is strongest in hot, wet climates."),
    ],
))

# ------------------------------------------------------------------ 3. Soil erosion and conservation
LESSONS.append(lesson(
    module=MODULE,
    topic=SOIL,
    title="Soil erosion and soil conservation",
    slug="bio-soil-erosion-and-conservation",
    minutes=22,
    summary="The difference between soil erosion and soil conservation, the natural and human causes of erosion, its effects on farming, rivers and people, and the main methods of conserving soil.",
    objectives=[
        "Differentiate between soil erosion and soil conservation",
        "Describe the causes of soil erosion",
        "Outline the consequences of soil erosion",
        "Describe the methods of soil conservation with diagrams",
    ],
    key_concepts=["Soil erosion", "Soil conservation", "Runoff", "Gully", "Terracing", "Contour ploughing", "Mulching", "Cover crops", "Afforestation", "Crop rotation"],
    blocks=[
        H("Introduction"),
        T("After a heavy storm in the Western Highlands, the streams run brown. That brown colour is soil. It has been "
          "washed from farms on the hillsides. It took hundreds or thousands of years to form, but a few storms can "
          "remove it."),
        T("This lesson explains why soil is lost, what happens when it is lost, and how farmers can protect it."),
        D("**Soil erosion** is the removal of soil from the land surface, mainly by running water and wind, faster than "
          "new soil forms.", title="Definition: soil erosion"),
        D("**Soil conservation** is the use of methods to protect the soil from erosion and to keep it fertile.",
          title="Definition: soil conservation"),
        T("Do not confuse the two. Erosion is the problem. Conservation is the solution."),
        H("How the soil is eroded"),
        T("Rain falls on the ground. If the ground is covered by plants, the leaves slow the raindrops, the roots hold the "
          "soil and water soaks in. If the ground is bare, raindrops hit the soil hard and the water runs off quickly, "
          "carrying soil with it. This moving water is called **runoff**."),
        IMG("f5g-bio-erosion.svg", alt="Two slopes in heavy rain: a bare slope with fast runoff carrying soil away and a slope with trees and roots where water soaks in",
            caption="Figure 1. Runoff carries soil away from a bare slope; plants protect the soil."),
        T("Three common forms of water erosion are sheet erosion (a thin layer removed from a wide area), rill erosion "
          "(small channels) and **gully erosion** (deep channels cut by running water). Wind erosion is common in dry "
          "areas, where it blows away dry, loose soil. Check your textbook for more detail on each form."),
        H("Causes of soil erosion"),
        KEY("Natural causes", "Present even without people.", cards=[
            ["Heavy rain", "Raindrops loosen soil and fast runoff carries it away."],
            ["Steep slopes", "Water flows faster downhill, so it carries more soil."],
            ["Strong wind", "Dry, loose soil in dry areas is blown away."],
            ["Soil type", "Loose sandy soils and dry soils are easily carried by wind and water."],
        ]),
        KEY("Human causes", "These make erosion much worse.", cards=[
            ["Deforestation", "Cutting trees removes roots and cover. Logging, charcoal burning and clearing for farms are examples."],
            ["Overgrazing", "Too many cattle, goats or sheep eat the grass and trample the soil, leaving it bare."],
            ["Poor farming", "Ploughing up and down a slope, farming steep hills and leaving the land bare after harvest."],
            ["Bush burning", "Fire removes the plant cover and exposes the soil."],
            ["Overcultivation", "Growing crops year after year without rest wears the soil out and makes it loose."],
            ["Construction and mining", "Roads, buildings, sand and stone quarries leave bare ground."],
        ]),
        H("Consequences of soil erosion"),
        T("The first and most serious effect is the loss of the fertile topsoil. After that, other problems follow."),
        KEY("Effects of soil erosion", "On land, rivers and people.", cards=[
            ["On farms", "Topsoil is lost, so crop yields fall. Deep gullies cut fields in two."],
            ["On rivers and dams", "Eroded soil settles in rivers, lakes and reservoirs. This is called silting. Rivers fill, floods become more likely and dams lose water storage."],
            ["On people", "Less food, lower farm income, hunger and migration of farmers to towns or new land."],
            ["On land", "Spreading bare, unusable land. In dry areas, this can lead to desertification."],
        ]),
        H("Methods of soil conservation"),
        T("Conservation methods do two jobs. They slow the water down so it soaks in, and they cover or bind the soil "
          "so it cannot be carried away."),
        IMG("f5g-bio-conservation.svg", alt="Left: a hillside cut into flat steps (terraces). Right: contour lines around a hill with furrows along them, stopping water from running down",
            caption="Figure 2. Terracing and contour ploughing slow down water on slopes."),
        CODE(
            "Method              How it works                                 Used on\n"
            "------------------  -------------------------------------------  ---------------\n"
            "Terracing           Flat steps cut into the slope slow water     Steep hillsides\n"
            "Contour ploughing   Furrows across the slope hold water          Gentle slopes\n"
            "Mulching            Leaves or straw cover soil, protect it       Any farm\n"
            "Cover crops         Low plants (beans, grass) keep soil covered  Between crops\n"
            "Afforestation       Planting trees; roots bind soil              Bare, steep land\n"
            "Crop rotation       Changing crops keeps nutrients balanced      Farms\n"
            "Windbreaks          Rows of trees slow the wind                  Dry areas\n"
            "Controlled grazing  Fewer animals so grass can recover           Pastures",
            "text", title="Table 1. Main methods of soil conservation"),
        T("In the Mandara Mountains of the Far North, farmers build stone terraces on steep slopes. This is a traditional "
          "example of soil conservation. Check your textbook for other Cameroonian examples."),
        EX("Model answer: describe how terracing and contour ploughing conserve soil", intro="Describe how terracing and contour ploughing reduce soil erosion. (5 marks)", steps=[
            S("Terracing: what it is", text="Farmers cut the slope into a series of flat steps, with a low wall or bank at the edge of each step."),
            S("Terracing: how it works", text="Each flat step slows down the runoff and lets water soak into the soil, so less soil is carried downhill."),
            S("Contour ploughing: what it is", text="Farmers plough and plant along the contour lines, across the slope, and not up and down it."),
            S("Contour ploughing: how it works", text="Each furrow acts as a small barrier that holds water and soil. Water soaks in rather than rushing downhill."),
            S("Conclusion", text="Both methods slow the flow of water, so they protect topsoil and keep crop yields."),
        ]),
        EX("Model answer: causes and effects of soil erosion", intro="Describe two human causes of soil erosion and outline two consequences. (6 marks)", steps=[
            S("Cause 1: deforestation", text="Trees are cut for timber, fuelwood and farms. Without roots, the soil is loose and bare, so rain and wind carry it away."),
            S("Cause 2: overgrazing", text="Too many animals eat all the grass and trample the soil. The bare ground is easily eroded."),
            S("Consequence 1: lower yields", text="Topsoil, with its humus and nutrients, is lost, so crops grow badly and farmers earn less."),
            S("Consequence 2: silting and floods", text="Eroded soil settles in rivers and reservoirs, so the water level rises and floods become more likely."),
        ]),
        MISTAKE("Using erosion and conservation as if they mean the same thing", "Erosion is the loss of soil. Conservation is "
                "protecting soil from loss. If a question says 'soil conservation', give methods, not causes."),
        MISTAKE("Giving only one-word answers", "Write 'Terracing: flat steps slow runoff so water soaks in.' not just 'terracing'. "
                "Marks are given for the explanation."),
        QUIZ("Which of the following is a method of soil conservation?",
             ["Burning the bush", "Ploughing up and down the slope", "Planting cover crops", "Cutting down trees on a steep hill"], 2,
             "Cover crops keep the soil covered and their roots hold it. The other three increase erosion.",
             hint="A conservation method protects the soil.",
             feedback=["Bush burning removes cover and exposes the soil.", "Ploughing up and down gives water a channel to flow fast.", "",
                       "Cutting trees removes roots that hold the soil."]),
        QUIZ("What is the most direct effect of soil erosion on a farm?",
             ["More rain", "Loss of fertile topsoil and lower yields", "A hotter climate", "A bigger harvest"], 1,
             "Erosion carries away the topsoil, which holds humus and nutrients, so yields fall.",
             hint="Think about which layer is lost first.",
             feedback=["Erosion does not make rain.", "", "Erosion does not change the climate.", "Yields usually fall, not rise."]),
        TIP("Exam link: Paper 1 may ask for a cause, an effect or a method. Paper 2 Section B can ask you to differentiate between "
            "soil erosion and soil conservation, describe causes and consequences and describe methods. Use diagrams for "
            "terracing and contour ploughing.", title="Exam link"),
        PQ("Differentiate between soil erosion and soil conservation.",
           "Soil erosion is the removal of soil by wind or running water, faster than new soil forms. Soil conservation is the use of methods "
           "such as terracing, mulching and tree planting to protect the soil from erosion and keep it fertile."),
        PQ("Describe three causes of soil erosion.",
           "First, deforestation removes tree cover and roots so the soil is exposed. Second, overgrazing leaves the ground bare and trampled. "
           "Third, farming up and down a slope lets runoff flow fast. Heavy rain and steep slopes also increase erosion."),
        PQ("Outline three consequences of soil erosion.",
           "Fertile topsoil is lost, so crop yields fall and farmers earn less. Eroded soil silts up rivers and dams, which can cause floods. "
           "Gullies cut fields, and people may move away or go hungry. In dry areas the land may become desert."),
        PQ("Describe three methods of soil conservation.",
           "Terracing cuts flat steps in a slope to slow runoff. Mulching covers the soil with leaves or straw so rain cannot hit it. "
           "Afforestation plants trees whose roots bind the soil. Contour ploughing, cover crops and crop rotation are other correct methods."),
        SUM("Soil erosion is the removal of soil by water or wind. Soil conservation is protecting the soil from it.",
            "Causes: heavy rain and steep slopes, plus deforestation, overgrazing, poor farming, bush burning and construction.",
            "Consequences: loss of topsoil, lower yields, silted rivers and dams, floods, hunger and migration.",
            "Methods: terracing, contour ploughing, mulching, cover crops, afforestation, crop rotation, windbreaks, controlled grazing.",
            "In the exam, always explain how each method works and draw a diagram if you can."),
    ],
))

# ------------------------------------------------------------------ 4. World vegetation types and factors
LESSONS.append(lesson(
    module=MODULE,
    topic=VEG,
    title="World vegetation types and the factors that affect them",
    slug="bio-world-vegetation-types-and-the-factors-affecting-them",
    minutes=20,
    summary="What natural vegetation is, how the main world vegetation types are classified and located, and how climate, soil, relief and human activity decide where each type grows.",
    objectives=[
        "Define vegetation and classify the main vegetation types on the world map",
        "Locate the main vegetation belts by latitude and climate",
        "Describe the factors that affect the distribution of vegetation",
        "Explain how altitude changes vegetation on a mountain such as Mount Cameroon",
    ],
    key_concepts=["Vegetation", "Natural vegetation", "Forest", "Grassland", "Desert", "Tundra", "Climate", "Relief", "Altitude", "Human activity"],
    blocks=[
        H("Introduction"),
        T("Climb Mount Cameroon from Buea. At the bottom you walk through thick forest. Higher up, the climate is cooler "
          "and the plants change. Near the top there are mostly grasses and low plants. In a few hours you have crossed "
          "several kinds of vegetation."),
        T("The same thing happens, on a much bigger scale, as you travel from the equator towards the poles. This "
          "lesson shows you the main types of vegetation in the world and why each one grows where it does."),
        D("**Vegetation** is the plant cover of an area. **Natural vegetation** is the plant cover that grows without help or "
          "interference from people.", title="Definition: vegetation"),
        T("In most places today, people have changed the natural vegetation by farming, logging and building. The "
          "type of vegetation that would grow in a place if people had not changed it is still a useful idea."),
        H("Classifying the main vegetation types"),
        T("Geographers group vegetation into a few main types. Each one is linked to a climate. A simple "
          "classification has five main groups."),
        KEY("Main groups of vegetation", "Find each one on the world map.", cards=[
            ["Forests", "Tropical rainforest, temperate forest and coniferous forest. Trees form a continuous cover."],
            ["Grasslands", "Tropical grassland (savanna) and temperate grassland. Grass dominates, with few trees."],
            ["Desert vegetation", "Hot desert: sparse plants such as scrub, grasses and cactus. Plants are widely spaced."],
            ["Mediterranean vegetation", "Evergreen shrubs and small trees in lands with hot, dry summers and mild, wet winters."],
            ["Cold and mountain vegetation", "Tundra near the poles and alpine vegetation high on mountains: mosses, lichens and low shrubs."],
        ]),
        T("The Board asks for detailed knowledge of only three types: tropical rainforest, tropical grassland (savanna) "
          "and tropical desert. These are studied in the next lesson. For the other types, you only need to know their "
          "names and where they are found."),
        IMG("f5g-bio-vegetation-belts.svg", alt="Bands of vegetation from the equator to the pole: tropical rainforest, savanna, hot desert, Mediterranean scrub, temperate forest and grassland, coniferous forest, tundra and polar ice, with Cameroon between about 2 and 13 degrees north",
            caption="Figure 1. Idealised vegetation belts in the northern hemisphere. Short blue marks show the Equator (0), the Tropic of Cancer (23.5 N) and the Arctic Circle (66.5 N)."),
        T("This figure is a simple model. The real map is more complicated, because mountains, oceans and winds break "
          "the pattern. Use your atlas to see the real pattern."),
        CODE(
            "Vegetation type          Typical location           Typical climate\n"
            "-----------------------  -------------------------  -------------------------------\n"
            "Tropical rainforest      Near the equator           Hot, wet all year\n"
            "Savanna grassland        Either side of the forest  Hot, wet and dry seasons\n"
            "Hot desert               About 20-30 degrees N, S   Hot, very dry\n"
            "Mediterranean scrub      West sides of continents   Hot dry summer, mild wet winter\n"
            "Temperate forest, grass  Mid-latitudes              Mild, rain in all seasons\n"
            "Coniferous forest        Far north                  Long, cold winters\n"
            "Tundra                   Near the poles             Very cold, little precipitation",
            "text", title="Table 1. Main vegetation types, where they are found and their climate"),
        T("Cameroon lies between about 2 and 13 degrees north of the equator. It has three of the types in the figure. "
          "In the south there is rainforest. In the Adamawa and the north there is savanna. In the "
          "extreme north, near Lake Chad, the land is dry and the vegetation is thorny scrub and sparse grass."),
        H("Factors that affect vegetation"),
        KEY("Four main factors", "Remember: climate, soil, relief, human activity.", cards=[
            ["Climate", "The most important factor. Temperature, rainfall and sunshine decide which plants can grow."],
            ["Soil", "Deep, fertile soils support dense vegetation. Thin, dry or salty soils support few plants."],
            ["Relief", "Height (altitude), slope and aspect. Higher places are colder. Steep slopes have thin soils."],
            ["Human activity", "Farming, logging, grazing, burning, mining and building replace natural vegetation."],
        ]),
        T("**Climate.** Plants need warmth, water and light. Rainforest needs heat and rain all year. Grass grows where "
          "rain falls in one season. Desert plants survive where rain is rare. Conifers survive cold winters."),
        T("**Soil.** Plants take water and nutrients from the soil. Deep soil lets trees spread roots. Thin sandy soil in "
          "the desert cannot hold water."),
        T("**Relief.** Temperature falls with height, by about 6 degrees Celsius for every 1000 metres. So high places have "
          "vegetation like that of colder regions. Steep slopes have thin soil, so only small plants grow there."),
        T("**Human activity.** People cut forest for timber and farms, burn grassland, and graze animals. Cities and "
          "roads remove vegetation completely."),
        T("Mount Cameroon shows the effect of altitude. Forest grows on the lower slopes. Higher up, the climate is "
          "cooler and the forest gives way to mountain grassland. The pattern is similar on other high mountains."),
        EX("Model answer: classify and locate vegetation types", intro="Name the vegetation type found at each of the following places and give one reason. (a) The Congo Basin near the equator (b) the Sahara (c) the far north of Canada. (6 marks)", steps=[
            S("(a) Tropical rainforest", text="The climate is hot and wet all year, so tall, evergreen trees grow in dense layers."),
            S("(b) Hot desert vegetation", text="Rainfall is very low, so only widely spaced, drought-resistant plants and scrub grow."),
            S("(c) Coniferous forest and tundra", text="Winters are very long and cold, so only cold-resistant conifers, mosses and lichens survive. Check your textbook for the exact belts."),
        ]),
        EX("Model answer: factors affecting vegetation", intro="Describe how climate and relief affect the distribution of vegetation. (6 marks)", steps=[
            S("Climate: rainfall", text="Heavy rain all year allows dense forest. Seasonal rain gives grassland. Very little rain gives desert plants."),
            S("Climate: temperature", text="Warm areas allow quick growth. Very cold areas allow only tundra plants such as mosses and lichens."),
            S("Relief: altitude", text="Temperature falls with height, so vegetation changes as you climb. On Mount Cameroon, forest gives way to grassland near the top."),
            S("Relief: slope", text="Steep slopes have thin, easily eroded soil, so only small plants or grass grow."),
        ]),
        MISTAKE("Naming only one factor, climate", "Climate is the main factor, but exam questions ask for several. Always add soil, relief and "
                "human activity, each with an example."),
        MISTAKE("Using vegetation and climate as if they were the same", "Vegetation is the plant cover. Climate is the weather pattern that "
                "helps decide it. Write 'the climate controls the vegetation'."),
        QUIZ("Which vegetation type is found near the equator?",
             ["Tundra", "Tropical rainforest", "Coniferous forest", "Hot desert"], 1,
             "The equator has hot, wet weather all year, which suits tropical rainforest.",
             hint="Think of the Congo Basin and southern Cameroon.",
             feedback=["Tundra is near the poles.", "", "Coniferous forests are in cold, high latitudes.",
                       "Hot deserts are around 20 to 30 degrees from the equator, where rain is rare."]),
        QUIZ("How does going up a mountain change the vegetation?",
             ["It becomes more like the vegetation of colder regions", "It becomes more like a rainforest", "It does not change", "It always becomes desert"], 0,
             "Temperature falls with height, so vegetation changes to types found in colder places.",
             hint="Think about temperature as you climb.",
             feedback=["", "A rainforest needs heat, but the temperature falls as you climb.", "Mount Cameroon shows that it changes.",
                       "Mountains are not always dry. Many have forest and grassland."]),
        TIP("Exam link: Paper 1 asks you to match a vegetation type to a climate or a place. Paper 2 Section B can ask you to define "
            "vegetation, classify the types on a world map and describe the factors that affect vegetation.", title="Exam link"),
        PQ("Define vegetation and name four main types of vegetation.",
           "Vegetation is the plant cover of an area. Four types are tropical rainforest, savanna grassland, hot desert vegetation and "
           "coniferous forest. Others are tundra and Mediterranean scrub."),
        PQ("State where the following are found: (a) tropical rainforest (b) hot desert (c) tundra.",
           "Tropical rainforest is found near the equator, in places such as the Congo Basin and southern Cameroon. Hot deserts are found "
           "around 20 to 30 degrees north and south of the equator, such as the Sahara. Tundra is found near the poles, in the far north "
           "of Canada and Russia."),
        PQ("Describe how soil and human activity affect vegetation.",
           "Deep fertile soil supports dense vegetation, while thin dry soil supports few plants. People cut forests for timber and farms, "
           "burn grassland and overgraze, so natural vegetation is replaced by farms, towns and bare ground."),
        PQ("Explain how altitude affects vegetation on a high mountain.",
           "Temperature falls with altitude, by about 6 degrees Celsius for every 1000 metres. Plants that need heat cannot grow higher up. "
           "On a mountain such as Mount Cameroon, forest on the lower slopes gives way to mountain grassland near the top. Soils are also thinner."),
        SUM("Vegetation is the plant cover of an area. Natural vegetation grows without human interference.",
            "The main groups are forests, grasslands, desert vegetation, Mediterranean vegetation and cold or mountain vegetation.",
            "In the northern hemisphere the belts run from rainforest at the equator, through savanna and desert, to temperate forest, coniferous forest and tundra.",
            "Distribution is controlled by climate, soil, relief (altitude and slope) and human activity.",
            "Climate is the most important factor, but always mention the other three."),
    ],
))

# ------------------------------------------------------------------ 5. Rainforest, grassland and desert
LESSONS.append(lesson(
    module=MODULE,
    topic=VEG,
    title="Rainforest, grassland and desert vegetation: adaptations and problems",
    slug="bio-rainforest-grassland-and-desert-vegetation",
    minutes=25,
    summary="The characteristics of tropical rainforest, tropical grassland (savanna) and tropical desert vegetation, how plants adapt to local conditions, and the problems and solutions for world vegetation.",
    objectives=[
        "State the main characteristics of tropical rainforest, tropical grassland and tropical desert vegetation",
        "Describe how plants adapt to the local environmental conditions in each",
        "Describe problems faced by world vegetation: deforestation, bush fires, overgrazing and desertification",
        "Outline solutions to these problems",
    ],
    key_concepts=["Tropical rainforest", "Savanna", "Tropical desert", "Adaptation", "Xerophyte", "Deforestation", "Bush fire", "Overgrazing", "Desertification"],
    blocks=[
        H("Introduction"),
        T("Cameroon is often called Africa in miniature. From the forest near Ebolowa to the dry plains near Maroua, you "
          "can see all three tropical vegetation types in one country. Each type has plants that can survive its own climate."),
        D("An **adaptation** is a feature of a plant (or animal) that helps it to survive in its environment.", title="Definition: adaptation"),
        H("Tropical rainforest"),
        T("The tropical rainforest grows where it is hot (around 27 degrees Celsius) and wet all year, with more than "
          "about 1500 mm of rain. It is found near the equator: the Congo Basin, the Amazon and parts of south-east Asia. In "
          "Cameroon it covers much of the South, East and South-West regions."),
        IMG("f5g-bio-rainforest-layers.svg", alt="Profile of a tropical rainforest showing the emergent layer, canopy, understorey and forest floor",
            caption="Figure 1. The layers of a tropical rainforest."),
        KEY("Characteristics of the rainforest", "What you see.", cards=[
            ["Evergreen", "Trees keep leaves all year. There is no single leaf-fall season, because growth is possible all year."],
            ["Dense and tall", "Trees reach 40 m or more. Growth is thick, with several layers."],
            ["Many species", "Hundreds of species in a small area, with few of any one kind."],
            ["Hardwoods", "Tough, valuable timber such as mahogany and iroko."],
            ["Climbers and epiphytes", "Lianas climb trunks. Epiphytes grow on branches to reach light."],
        ]),
        KEY("Adaptations of rainforest plants", "To heat, heavy rain and little light.", cards=[
            ["Drip tips", "Leaves have pointed tips and a waxy surface to shed heavy rain quickly."],
            ["Buttress roots", "Wide, flat roots spread out from the base of tall trees to support them in thin soil."],
            ["Tall growth", "Trees race upwards to reach the sunlight in the canopy."],
            ["Large leaves", "Understorey plants have large leaves to catch the little light that reaches the ground."],
        ]),
        H("Tropical grassland (savanna)"),
        T("The savanna grows where it is hot all year and there is a wet season and a long dry season, with about 600 to "
          "1500 mm of rain. It lies on either side of the rainforest. In Cameroon it covers the Adamawa and the North. Waza "
          "National Park in the Far North is a famous savanna park."),
        KEY("Characteristics of the savanna", "What you see.", cards=[
            ["Tall grass", "Grasses grow tall in the wet season, then turn yellow and dry in the dry season."],
            ["Scattered trees", "Trees such as acacia and baobab grow far apart, often with flat tops."],
            ["Seasonal change", "Green and lush in the rains; brown and bare in the dry season."],
        ]),
        KEY("Adaptations of savanna plants", "To a long dry season and fire.", cards=[
            ["Deep roots", "Trees send roots deep to reach water far below the surface."],
            ["Shedding leaves", "Many trees lose leaves in the dry season to reduce water loss."],
            ["Thick bark", "Resists bush fires. The tree can survive and grow again."],
            ["Water storage", "The baobab stores water in its thick trunk."],
            ["Thorns and small leaves", "Acacia has small leaves and thorns, which reduce water loss and protect against grazing animals."],
            ["Grass regrowth", "Grass dies back above ground but its roots survive and sprout after fire or rain."],
        ]),
        H("Tropical desert"),
        T("The tropical desert has less than about 250 mm of rain in a year, and the rain is unreliable. It is very hot by "
          "day and can be cool at night. The Sahara is the largest hot desert. In Cameroon, the dry edge near Lake Chad "
          "is part of the Sahel, a semi-desert."),
        KEY("Characteristics of desert vegetation", "What you see.", cards=[
            ["Sparse cover", "Plants are small and far apart, and much of the ground is bare."],
            ["Scrub and grasses", "Low thorny shrubs, tufts of grass, and a few trees such as acacia or date palm near water."],
            ["Short life cycles", "Some plants grow, flower and seed within days of rain."],
        ]),
        KEY("Adaptations of desert plants", "To very little water and heat. Plants adapted to dry places are called xerophytes.", cards=[
            ["Long or wide roots", "Very deep roots reach water far below. Wide, shallow roots catch rain quickly."],
            ["Thick, waxy stems", "Cacti and other succulents store water in fleshy stems. Wax reduces water loss."],
            ["Small leaves or spines", "A small leaf area reduces water loss through the leaves."],
            ["Seeds wait", "Seeds lie dormant, sometimes for years, and sprout only after rain."],
        ]),
        CODE(
            "Feature       Rainforest         Savanna                 Desert\n"
            "------------  -----------------  ----------------------  ---------------------\n"
            "Rainfall      Over 1500 mm       600-1500 mm, seasonal   Under 250 mm\n"
            "Plant cover   Dense, tall        Grass, scattered trees  Sparse, bare ground\n"
            "Leaves        Evergreen, drip    Often shed in dry time  Small, spiny, waxy\n"
            "Main problem  Little light below Dry season and fire     Lack of water",
            "text", title="Table 1. Comparing the three tropical vegetation types"),
        H("Problems faced by world vegetation"),
        KEY("Four main problems", "Know a cause and an effect for each.", cards=[
            ["Deforestation", "The clearing of forest. Causes: logging, farming, fuelwood, roads, mines. Effects: loss of habitat and species, soil erosion, flooding."],
            ["Bush fires", "Fires lit to clear land or to hunt. Effects: destroy plants and animals, expose soil, release smoke."],
            ["Overgrazing", "Too many animals on too little land. They eat the grass and trample the soil, leaving it bare."],
            ["Desertification", "The spread of desert-like conditions into dry lands, caused by drought, overgrazing and tree-cutting."],
        ]),
        KEY("Solutions", "Match the solution to the problem.", cards=[
            ["Against deforestation", "Replant trees (reforestation and afforestation), selective logging, national parks (such as Korup), laws and education, efficient cooking stoves."],
            ["Against bush fires", "Firebreaks, controlled burning, education, penalties for careless burning."],
            ["Against overgrazing", "Limit herd sizes, rotate grazing, grow fodder, plant grass."],
            ["Against desertification", "Plant trees as windbreaks and shelterbelts, protect trees, manage water, farm with soil-conserving methods."],
        ]),
        EX("Model answer: adaptations of savanna plants", intro="Describe two ways in which savanna plants have adapted to the long dry season and bush fires. (4 marks)", steps=[
            S("Adaptation 1: deep roots and leaf loss", text="Savanna trees such as acacia send deep roots to reach water below the surface. Many shed leaves in the dry season, which reduces water loss."),
            S("Adaptation 2: thick bark", text="The thick bark of many trees protects them from fire, so they survive and sprout again."),
            S("Add an example", text="The baobab stores water in its trunk, so it can survive months without rain."),
        ]),
        EX("Model answer: deforestation and its solutions", intro="Describe the causes of deforestation in a tropical rainforest and outline two solutions. (6 marks)", steps=[
            S("Cause 1: logging", text="Companies cut valuable trees for timber. Roads built for logging open more forest to settlement."),
            S("Cause 2: farming and fuelwood", text="Farmers clear forest for crops, and families cut trees for firewood and charcoal."),
            S("Solution 1: replanting and protection", text="Plant new trees to replace those cut, and set up protected areas such as national parks."),
            S("Solution 2: sustainable logging and education", text="Cut only selected trees, enforce laws and teach people why forests matter."),
        ]),
        MISTAKE("Giving adaptations without saying how they help", "Do not write only 'thick bark'. Write 'thick bark, which protects the tree from "
                "fire'. The how-it-helps part earns the mark."),
        MISTAKE("Mixing up the three types", "Remember: rainforest is wet all year and evergreen, savanna has seasons with grass and scattered "
                "trees, desert has sparse plants. Do not give drip tips for desert plants or thorns for rainforest trees."),
        QUIZ("Why do rainforest leaves have drip tips?",
             ["To store water", "To shed heavy rain quickly", "To reduce the light they receive", "To attract animals"], 1,
             "A drip tip lets water run off the leaf quickly, so the leaf dries and does not stay wet in the heavy rain.",
             hint="Think of how much rain falls in the forest.",
             feedback=["Storing water is a desert adaptation, not a rainforest one.", "",
                       "Rainforest plants need light, not less of it.", "Drip tips do not attract animals."]),
        QUIZ("Which is an adaptation of a desert plant?",
             ["Large thin leaves", "Leaves that are always wet", "Thick, waxy stems that store water", "Buttress roots"], 2,
             "Thick, waxy stems store water and reduce water loss, which helps survival in a dry climate.",
             hint="Desert plants must save water.",
             feedback=["Large thin leaves lose a lot of water.", "Wet leaves are a rainforest feature, not a desert one.", "",
                       "Buttress roots support tall rainforest trees."]),
        TIP("Exam link: Paper 1 asks for characteristics, adaptations and causes of problems. Paper 2 Section B asks for descriptions of "
            "rainforest, savanna or desert vegetation plus problems and solutions. Write three or four points, each with the how-it-helps part.", title="Exam link"),
        PQ("State three characteristics of tropical rainforest vegetation.",
           "It is evergreen, so trees keep leaves all year. It is dense and tall, with trees of 40 metres or more arranged in layers. It has "
           "many species and valuable hardwoods such as mahogany. It also has lianas and epiphytes."),
        PQ("Describe two adaptations of plants to a desert environment.",
           "Many desert plants have long roots that reach deep water or wide roots that catch rain quickly. Others have thick, waxy stems that "
           "store water, small leaves or spines that reduce water loss, or seeds that stay dormant until rain falls."),
        PQ("Describe how overgrazing and bush fires harm vegetation.",
           "Overgrazing means too many animals eat and trample the plants, so the soil is left bare and can be eroded. Bush fires burn plants "
           "and young trees, destroy habitats and expose the soil to erosion, so the vegetation cannot easily regrow."),
        PQ("Outline solutions to desertification.",
           "Plant trees as windbreaks and protect existing ones. Control grazing by reducing herd sizes. Manage water carefully and use soil-"
           "conserving farming such as contour ploughing and mulching. Teach local people how to protect the land."),
        SUM("Tropical rainforest: hot, wet, evergreen, dense, tall, many species. Adaptations: drip tips, buttress roots, tall growth.",
            "Savanna: tall grass and scattered trees, with wet and dry seasons. Adaptations: deep roots, thick bark, leaf loss, water storage.",
            "Desert: sparse plants called xerophytes. Adaptations: long or wide roots, waxy stems, small leaves or spines.",
            "Problems: deforestation, bush fires, overgrazing and desertification.",
            "Solutions: replanting, protected areas, firebreaks, controlled grazing, windbreaks and education."),
    ],
))

# ------------------------------------------------------------------ 6. What is an ecosystem
LESSONS.append(lesson(
    module=MODULE,
    topic=ECO,
    title="What is an ecosystem? Structure and functioning",
    slug="bio-what-is-an-ecosystem",
    minutes=20,
    summary="What an ecosystem is, its living (biotic) and non-living (abiotic) parts, the roles of producers, consumers and decomposers, and how energy flows and nutrients are recycled.",
    objectives=[
        "Define an ecosystem and give examples",
        "Illustrate the structure of an ecosystem: biotic and abiotic components",
        "Describe the roles of producers, consumers and decomposers",
        "Outline how energy flows and nutrients are recycled in an ecosystem",
    ],
    key_concepts=["Ecosystem", "Biotic", "Abiotic", "Producer", "Consumer", "Decomposer", "Energy flow", "Nutrient cycling"],
    blocks=[
        H("Introduction"),
        T("Think of a pond near your village. Water, mud, sunlight, algae, fish, frogs, insects and birds all live "
          "and work together there. If the water dries up or the fish disappear, the whole pond changes. We call such a "
          "community and its surroundings an ecosystem."),
        D("An **ecosystem** is a community of living things (plants, animals and micro-organisms) together with their "
          "non-living surroundings (such as soil, water, air and sunlight), all linked together and interacting.", title="Definition: ecosystem"),
        T("Ecosystems can be large or small. A rainforest, the savanna of the Far North, Lake Chad, Mount Cameroon, a "
          "mangrove swamp near Limbe, a pond and even a farm are all ecosystems."),
        H("The structure of an ecosystem"),
        T("Every ecosystem has two kinds of components. **Biotic** components are the living things. **Abiotic** components "
          "are the non-living things."),
        D("**Biotic** means living (plants, animals, fungi and bacteria). **Abiotic** means non-living (sunlight, temperature, "
          "water, soil, air and rocks).", title="Definition: biotic and abiotic"),
        IMG("f5g-bio-ecosystem.svg", alt="Diagram of an ecosystem: the Sun gives energy to producers, which are eaten by consumers; dead matter goes to decomposers, which return nutrients to the soil and air, the non-living part",
            caption="Figure 1. The structure of an ecosystem: biotic parts (producers, consumers, decomposers) and abiotic parts."),
        KEY("The living (biotic) parts", "Three groups, each with a different role.", cards=[
            ["Producers", "Green plants and algae. They make their own food from sunlight, water and carbon dioxide by photosynthesis."],
            ["Consumers", "Animals that cannot make food. Herbivores eat plants, carnivores eat animals, omnivores eat both."],
            ["Decomposers", "Fungi, bacteria and some small animals. They feed on dead plants and animals and return nutrients to the soil."],
        ]),
        KEY("The non-living (abiotic) parts", "They set the conditions for life.", cards=[
            ["Sunlight", "The source of energy. Plants use it to make food."],
            ["Water", "Needed by all living things. Dissolves nutrients for plants."],
            ["Soil", "Gives plants support, water and nutrients. Many animals live in it."],
            ["Air", "Contains oxygen for breathing and carbon dioxide for photosynthesis."],
            ["Temperature", "Decides how fast living things grow and which species can live there."],
        ]),
        TIP("Do not forget decomposers when you list the components of an ecosystem. Without them, dead matter would pile up and "
            "the nutrients would never be reused."),
        H("The functioning of an ecosystem"),
        T("An ecosystem works because of two linked processes. **Energy flows** through it in one direction. "
          "**Nutrients** are recycled in a cycle."),
        D("**Energy flow** is the passage of energy through an ecosystem, from the Sun to the producers, then to the consumers. "
          "The energy goes in one direction only and most of it is lost as heat.", title="Definition: energy flow"),
        T("Plants capture a small part of the Sun's energy in photosynthesis. When a goat eats a plant, only part of the "
          "plant's energy passes to the goat. The rest is used by the plant for its own life or lost as heat. At each step, "
          "only about one tenth of the energy is passed on to the next level. This is why food chains are short."),
        D("**Nutrient cycling** is the recycling of nutrients (such as nitrogen and phosphorus) between the soil, plants, "
          "animals and decomposers.", title="Definition: nutrient cycling"),
        T("Plants take up nutrients from the soil. Animals get the nutrients by eating plants or other animals. When "
          "plants and animals die, or when animals produce waste, decomposers break them down and return the nutrients "
          "to the soil. Plants can then use them again."),
        CODE(
            "Energy at the start (Sun's energy captured by plants): 10 000 units\n"
            "Passed to herbivores (about one tenth):               1 000 units\n"
            "Passed to first carnivores (about one tenth):           100 units\n"
            "Passed to second carnivores (about one tenth):           10 units",
            "text", title="Table 1. How energy falls along a food chain (rough rule: about 10 percent passes on)"),
        T("This is a rule of thumb. The real share varies, but it is always small."),
        EX("Model answer: describe the structure of an ecosystem", intro="Using a named ecosystem, describe its biotic and abiotic components. (6 marks)", steps=[
            S("Name the ecosystem", text="A pond near a village in the Western Highlands."),
            S("Biotic components", text="Producers: algae and water plants. Consumers: insects, tadpoles, fish and birds. Decomposers: bacteria and fungi in the mud."),
            S("Abiotic components", text="Water, sunlight, temperature, dissolved oxygen and the mud at the bottom."),
            S("Link them", text="Producers use sunlight to make food. Consumers eat them. Decomposers rot dead matter and return nutrients to the water and mud."),
        ]),
        EX("Model answer: energy flow and nutrient cycling", intro="Explain the difference between energy flow and nutrient cycling in an ecosystem. (4 marks)", steps=[
            S("Energy flow", text="Energy comes from the Sun, passes from plants to herbivores to carnivores, and is lost as heat. It moves in one direction and is not reused."),
            S("Nutrient cycling", text="Nutrients move from the soil to plants, then to animals. Decomposers return them to the soil. They are reused again and again."),
            S("Conclusion", text="Energy flows through the ecosystem and leaves it, while nutrients go round and round in a cycle."),
        ]),
        MISTAKE("Saying decomposers are consumers", "Decomposers feed on dead matter, but they have their own role: they break it down and "
                "return nutrients to the soil. Always list them as a separate group."),
        MISTAKE("Saying energy is recycled", "Energy is not recycled. It flows in one direction and is lost as heat. Only nutrients are recycled."),
        QUIZ("Which of these is an abiotic component of an ecosystem?",
             ["A fungus", "A grasshopper", "Sunlight", "A baobab tree"], 2,
             "Abiotic means non-living. Sunlight is non-living. The other three are living things.",
             hint="Abiotic means not alive.",
             feedback=["A fungus is a living decomposer.", "A grasshopper is a living consumer.", "", "A baobab is a living producer."]),
        QUIZ("What is the role of decomposers?",
             ["They make food from sunlight", "They eat plants", "They break down dead matter and return nutrients to the soil", "They give the ecosystem energy"], 2,
             "Decomposers rot dead plants and animals, which returns nutrients to the soil for plants to use.",
             hint="Think of what happens to a fallen leaf.",
             feedback=["That is the work of producers.", "That is the work of herbivores.", "",
                       "Energy comes from the Sun, not from decomposers."]),
        TIP("Exam link: Paper 1 asks you to identify biotic and abiotic components or the role of a group. Paper 2 Section B asks you to "
            "define an ecosystem and draw and label its structure. A labelled diagram like Figure 1 earns most marks.", title="Exam link"),
        PQ("Define an ecosystem and give two examples.",
           "An ecosystem is a community of living things together with their non-living surroundings, all linked and interacting. Examples "
           "include a tropical rainforest, a savanna, a pond or a farm."),
        PQ("Differentiate between biotic and abiotic components.",
           "Biotic components are the living parts of an ecosystem, such as plants, animals, fungi and bacteria. Abiotic components are the "
           "non-living parts, such as sunlight, water, soil, air and temperature."),
        PQ("Describe the roles of producers, consumers and decomposers.",
           "Producers, mainly green plants, use sunlight to make food by photosynthesis. Consumers are animals that eat plants or other animals "
           "to get energy. Decomposers, such as fungi and bacteria, break down dead matter and return nutrients to the soil."),
        PQ("Explain why energy flows through an ecosystem but nutrients are recycled.",
           "Energy comes from the Sun and passes along the food chain, but at each step a large part is lost as heat, so it cannot be reused. "
           "Nutrients are not lost in this way. Decomposers return them to the soil, where plants take them up again, so they go round in a cycle."),
        SUM("An ecosystem is a community of living things and their non-living surroundings, interacting.",
            "Biotic parts: producers, consumers and decomposers. Abiotic parts: sunlight, water, soil, air and temperature.",
            "Energy flows in one direction from the Sun through producers to consumers, and about one tenth passes on at each step.",
            "Nutrients are recycled: soil to plants to animals, then decomposers return them to the soil.",
            "Draw and label an ecosystem diagram in the exam."),
    ],
))

# ------------------------------------------------------------------ 7. Food chains and food webs
LESSONS.append(lesson(
    module=MODULE,
    topic=ECO,
    title="Food chains and food webs",
    slug="bio-food-chains-and-food-webs",
    minutes=20,
    summary="The difference between a food chain and a food web, the trophic levels, examples from a savanna and a pond, and what happens to the other organisms when one link is removed.",
    objectives=[
        "Differentiate between a food chain and a food web",
        "Identify producers and primary, secondary and tertiary consumers in a food chain",
        "Illustrate a food chain and a food web with labelled diagrams",
        "Explain what happens when one link in a food chain or web is removed",
    ],
    key_concepts=["Food chain", "Food web", "Trophic level", "Producer", "Primary consumer", "Secondary consumer", "Tertiary consumer", "Herbivore", "Carnivore"],
    blocks=[
        H("Introduction"),
        T("In the dry season in Waza National Park, grass turns brown and herds of antelope move to find food. Lions follow "
          "the antelope. When the rains come, the grass grows again and insects multiply. Everything in the park is linked "
          "through who eats whom."),
        T("This lesson shows how to draw and read those links in food chains and food webs."),
        D("A **food chain** is a single line showing who eats whom in an ecosystem, starting with a producer. Each arrow "
          "points to the animal that eats the one before it, and shows the flow of energy.", title="Definition: food chain"),
        D("A **food web** is a set of many food chains linked together. It shows that most animals eat more than one "
          "kind of food and are eaten by more than one kind of animal.", title="Definition: food web"),
        H("Food chains and trophic levels"),
        T("Each step in a food chain is a **trophic level**. A trophic level is the feeding level of an organism."),
        IMG("f5g-bio-food-chains.svg", alt="Two food chains: savanna grass to grasshopper to lizard to eagle, and pond algae to tilapia to catfish to kingfisher",
            caption="Figure 1. A savanna food chain and a pond food chain, with trophic levels."),
        KEY("Trophic levels", "Learn the names and the order.", cards=[
            ["Level 1: producer", "Green plants or algae. They make food by photosynthesis."],
            ["Level 2: primary consumer", "A herbivore. It eats producers."],
            ["Level 3: secondary consumer", "A carnivore (or omnivore) that eats primary consumers."],
            ["Level 4: tertiary consumer", "A carnivore that eats secondary consumers. At the top of the chain, there are no predators."],
        ]),
        T("A **herbivore** eats only plants. A **carnivore** eats only animals. An **omnivore** eats both. A **predator** hunts "
          "and kills other animals, which are its **prey**."),
        T("Chains are short, usually three to five links. This is because about 90 percent of the energy is lost at each level, "
          "so very little is left for a fifth level."),
        TIP("The arrows show the flow of energy, so they point from the food to the eater, not from the eater to the food. "
            "Write grass to grasshopper, not grasshopper to grass."),
        H("Food webs"),
        T("In real ecosystems, nothing eats only one thing. A lizard eats grasshoppers, but also beetles. An eagle eats "
          "lizards, birds and snakes. These cross-links make a web."),
        IMG("f5g-bio-food-web.svg", alt="Savanna food web with grass and acacia at the bottom, grasshopper and antelope above them, then lizard, small bird and lion, and snake and eagle at the top",
            caption="Figure 2. A simple savanna food web. Arrows point to the eater."),
        T("In this web, the antelope eats grass and acacia. The grasshopper eats grass and acacia. The lizard and the "
          "small bird both eat grasshoppers. The eagle eats the lizard and the small bird. The snake eats the lizard. "
          "The lion eats the antelope."),
        H("What happens when one link is removed?"),
        T("Every organism in the web depends on others. If one is removed, other organisms are affected. This is why "
          "ecosystems are fragile."),
        KEY("Effects of removing a link", "Use the food web in Figure 2.", cards=[
            ["Remove the grasshopper (disease or pesticide)", "The lizard and the small bird lose a food source. Their numbers may fall. Then the eagle and snake may also decline, if they have no other food."],
            ["Remove the lion (hunting)", "Antelope are no longer hunted, so their numbers grow. They eat more grass and acacia, so the plants may be overgrazed."],
            ["Remove the grass (drought or fire)", "The grasshopper and antelope lose food and decline. The animals above them then decline too."],
        ]),
        T("A food web with many links is more stable. If one food source disappears, an animal can switch to another. "
          "A simple chain is easily broken."),
        T("People can also break food chains. Overhunting, overfishing, pesticides and the clearing of forest remove or "
          "poison links. For example, spraying a crop with a strong pesticide can kill the insects that birds depend on."),
        EX("Model answer: identify the parts of a food chain", intro="In the chain algae, tilapia, catfish, kingfisher, name (a) the producer (b) the primary consumer (c) the tertiary consumer (d) the trophic level of the catfish. (4 marks)", steps=[
            S("(a) Producer", text="Algae. They make their own food by photosynthesis."),
            S("(b) Primary consumer", text="Tilapia. It eats the algae."),
            S("(c) Tertiary consumer", text="Kingfisher. It eats catfish, which is a secondary consumer."),
            S("(d) Trophic level of the catfish", text="Level 3, a secondary consumer, because it eats the tilapia (a primary consumer)."),
        ]),
        EX("Model answer: effects of removing a link", intro="Using Figure 2, explain what may happen to the savanna ecosystem if all the grasshoppers are killed by a pesticide. (5 marks)", steps=[
            S("Direct effect", text="The lizard and the small bird both eat grasshoppers, so they lose a food source."),
            S("Knock-on effect", text="Their numbers may fall. The snake eats lizards and the eagle eats both lizards and birds, so they also lose food."),
            S("Effect on plants", text="Fewer insects eat grass and acacia leaves, so plants may grow more, until other grazers move in."),
            S("Conclusion", text="Removing one link affects many organisms, so food webs show how dependent living things are on each other."),
        ]),
        MISTAKE("Drawing arrows the wrong way", "An arrow means 'is eaten by' or 'gives energy to'. It points to the eater."),
        MISTAKE("Saying a food web is just a bigger chain", "A food web is made of many chains that cross each other. The links between chains "
                "are what make it different."),
        QUIZ("In the chain grass, grasshopper, lizard, eagle, what is the lizard?",
             ["Producer", "Primary consumer", "Secondary consumer", "Tertiary consumer"], 2,
             "The lizard eats the grasshopper, which is a primary consumer, so it is a secondary consumer.",
             hint="Count the steps from the producer.",
             feedback=["The producer is the grass.", "The grasshopper is the primary consumer.", "",
                       "The eagle is the tertiary consumer."]),
        QUIZ("What is the main difference between a food chain and a food web?",
             ["A chain has no producers", "A web shows many linked chains, a chain shows one line", "A web has only plants", "They are the same"], 1,
             "A food chain is one line of feeding links. A food web joins many chains together.",
             hint="Think of one line and a net.",
             feedback=["Both start with producers.", "", "A web has plants and animals.", "They are not the same: a web contains several chains."]),
        TIP("Exam link: Paper 1 often shows a short food chain or web and asks you to identify a level or predict an effect. "
            "Paper 2 Section B may ask you to differentiate a chain from a web and draw an example.", title="Exam link"),
        PQ("Differentiate between a food chain and a food web.",
           "A food chain is a single line of feeding links, from a producer to consumers. A food web is many food chains joined together, "
           "showing that most animals eat and are eaten by more than one kind of organism."),
        PQ("Draw a food chain with four organisms from a savanna or pond and label each trophic level.",
           "Grass (producer), then grasshopper (primary consumer), then lizard (secondary consumer), then eagle (tertiary consumer). "
           "The arrows point from the food to the eater: grass, grasshopper, lizard, eagle. In a pond, algae, tilapia, catfish and kingfisher "
           "give a correct answer too."),
        PQ("Explain why food chains rarely have more than five links.",
           "At each trophic level about 90 percent of the energy is lost, mainly as heat from the animal's life processes. Very little energy "
           "is left after four or five steps to support another level of consumers."),
        PQ("Explain what may happen to a food web when one predator at the top is removed.",
           "The animals it ate are no longer hunted, so their numbers may rise. They then eat more of their own food, such as grass, so the "
           "plants may be overgrazed. Other predators may have more competition, and the balance of the ecosystem changes."),
        SUM("A food chain is a single line of feeding links starting with a producer. A food web joins many chains.",
            "Trophic levels: producers, primary consumers (herbivores), secondary consumers and tertiary consumers.",
            "Arrows point from the food to the eater and show energy flow.",
            "About one tenth of the energy passes on at each level, so chains are short.",
            "If one link is removed, other organisms are affected. Webs with many links are more stable."),
    ],
))
