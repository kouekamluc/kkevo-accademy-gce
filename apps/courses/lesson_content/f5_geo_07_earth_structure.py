"""Form 5 Geography: Geomorphology, the structure of the Earth (6 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Geomorphology"
TOPIC = "The structure of the Earth"

LESSONS = []

# ------------------------------------------------------------------ 1. Structure of the Earth
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="The structure of the Earth: crust, mantle and core",
    slug="geo-structure-of-the-earth",
    minutes=20,
    summary="The Earth has four main layers (crust, mantle, outer core and inner core); the crust and the top of the mantle form the lithosphere, which is split into plates, and earthquake waves show us what is inside.",
    objectives=[
        "Illustrate the structure of the Earth with a labelled cross-section",
        "Describe the crust, mantle, outer core and inner core",
        "Define the lithosphere and explain what a plate is",
        "Explain in simple terms how earthquake waves tell us about the inside of the Earth",
    ],
    key_concepts=["Crust", "Mantle", "Outer core", "Inner core", "Lithosphere", "Tectonic plate", "Seismic waves"],
    blocks=[
        H("Introduction"),
        T("Mount Cameroon is an active volcano. When it erupts, red-hot rock comes out of the ground near Buea and Limbe. "
          "Where does that rock come from? It comes from deep inside the Earth."),
        T("Nobody has ever travelled to the centre of the Earth. The deepest hole ever drilled is only about 12 km deep, and the "
          "centre is more than 6,000 km down. So how do geographers know what the inside looks like? In this lesson you will learn "
          "the layers of the Earth and the clues that reveal them."),
        D("The **structure of the Earth** is the way the Earth is built from layers, one inside the other, like an onion. "
          "Each layer is different in thickness, temperature and the material it is made of.", title="Structure of the Earth"),
        H("The four layers"),
        T("The Earth has four main layers. Starting at the outside, they are the **crust**, the **mantle**, the **outer core** and the "
          "**inner core**. The distance from the surface to the centre is about 6,370 km."),
        IMG("f5g-geo-earth-layers.svg", alt="Cross-section of the Earth showing the thin crust, thick mantle, liquid outer core and solid inner core, with their thicknesses",
            caption="Figure 1. The layers of the Earth (not to scale: the crust is drawn thicker than it really is)."),
        KEY("What each layer is like", "Learn the four layers from the outside in.", cards=[
            ["Crust", "The thin, solid, rocky skin. Thickness about 5 to 10 km under the oceans and up to about 70 km under high mountains. We live on it."],
            ["Mantle", "The thickest layer, about 2,900 km. Hot rock that is mostly solid but flows very slowly. It holds most of the Earth's volume."],
            ["Outer core", "Liquid iron and nickel, about 2,200 km thick. Very hot. Its movement makes the Earth's magnetic field."],
            ["Inner core", "A solid ball of iron and nickel with a radius of about 1,200 km. The hottest part, but squeezed solid by the huge pressure."],
        ], note="Temperature and pressure both increase as you go deeper."),
        H("Two kinds of crust"),
        D("**Continental crust** is thick (often 30 to 50 km), lighter and mostly made of granite-type rock. **Oceanic crust** is thin "
          "(about 5 to 10 km), denser and mostly made of basalt-type rock. The difference in density matters at plate margins.",
          title="Continental and oceanic crust"),
        H("Lithosphere and plates"),
        D("The **lithosphere** is the rigid outer shell of the Earth. It is made of the crust and the uppermost part of the mantle, about 100 km "
          "thick altogether. Below it is the **asthenosphere**, a layer of hot, soft rock that can flow slowly.", title="Lithosphere"),
        T("The lithosphere is not one piece. It is cracked into large slabs called **tectonic plates**. The plates float on the soft asthenosphere "
          "and move very slowly, only a few centimetres a year, about as fast as your fingernails grow."),
        IMG("f5g-geo-lithosphere-plates.svg", alt="Cross-section showing continental crust, oceanic crust, rigid upper mantle forming the lithosphere, and the soft asthenosphere below, with a plate boundary",
            caption="Figure 2. The lithosphere is made of crust plus rigid upper mantle and is broken into plates."),
        T("Africa sits on the African plate, and Cameroon is inside this plate, far from its edges. Most earthquakes and volcanoes happen at the "
          "edges of plates. The next lessons explain why."),
        H("How do we know? Earthquake waves"),
        T("Scientists cannot drill to the core, but they can study **seismic waves**. These are shock waves that travel through the Earth after "
          "an earthquake. Instruments called seismographs record them all around the world."),
        T("The waves speed up, slow down, bend or stop when they pass from one layer into another. By timing how long they take to reach "
          "stations on the other side of the world, scientists work out what the layers are made of."),
        KEY("Two clues from the waves", "Two main kinds of body wave travel through the Earth.", cards=[
            ["P waves (primary)", "Fast. They can travel through solids and liquids."],
            ["S waves (secondary)", "Slower. They can travel only through solids, not through liquids."],
        ], note="S waves are not recorded on the far side of the Earth. This shows that part of the core is liquid."),
        TIP("Exam link: this topic is tested in Paper 1 (multiple choice on the layers and their features) and in Paper 2 Section B "
            "(physical geography), where you may be asked to draw and label the structure of the Earth. Always label the four layers and add one fact to each label."),
        EX("Model answer: illustrate and describe the structure of the Earth",
           intro="Draw a labelled cross-section of the Earth and describe its layers. (6 marks)",
           steps=[
               S("Drawing", text="Draw a large circle. Add three more circles inside it, so there are four zones. Label from the outside: crust, mantle, outer core, inner core. Write 'not to scale' under it."),
               S("Crust", text="The crust is the thin, solid outer layer. It is about 5 to 70 km thick. Continental crust is thicker and lighter than oceanic crust."),
               S("Mantle", text="The mantle lies below the crust and is about 2,900 km thick. It is hot rock that is mostly solid but flows very slowly."),
               S("Outer core", text="The outer core is a liquid layer of iron and nickel, about 2,200 km thick."),
               S("Inner core", text="The inner core is a solid ball of iron and nickel at the centre, with a radius of about 1,200 km. It is solid because of the very high pressure."),
           ]),
        EX("Model answer: how do we know the outer core is liquid?",
           intro="Explain how earthquake waves show that part of the Earth's core is liquid. (4 marks)",
           steps=[
               S("Point", text="S waves cannot pass through liquids, but P waves can."),
               S("Evidence", text="After an earthquake, seismographs on the opposite side of the Earth do not record S waves. P waves are still recorded there, although they have been slowed and bent on the way."),
               S("Explanation", text="The S waves must have been stopped by a liquid layer in the middle of the Earth. The only place this layer can be is the outer core."),
           ]),
        MISTAKE("Mixing up the crust and the lithosphere", "The crust is only the outer layer. The lithosphere is the crust plus the rigid top of the mantle. Plates are pieces of the lithosphere, not pieces of the crust only."),
        QUIZ("Which layer of the Earth is the thickest?", ["Crust", "Mantle", "Outer core", "Inner core"], 1,
             "The mantle is about 2,900 km thick, much more than any other layer.",
             hint="Compare the thicknesses in Figure 1.",
             feedback=["The crust is the thinnest layer, only about 5 to 70 km.", "",
                       "The outer core is about 2,200 km thick, thinner than the mantle.",
                       "The inner core has a radius of about 1,200 km, thinner than the mantle."]),
        QUIZ("Why is the inner core solid although it is very hot?", [
            "It is cooled by the mantle above it", "The pressure on it is extremely high", "It is made of rock, not metal", "It is close to the surface"], 1,
             "The huge pressure at the centre squeezes the metal so tightly that it cannot melt, even at very high temperature.",
             hint="Think about what increases with depth besides temperature.",
             feedback=["The mantle is cooler, but the inner core is the hottest layer.", "",
                       "The inner core is made of iron and nickel.", "It is at the centre, the furthest point from the surface."]),
        PQ("Name the four layers of the Earth from the surface to the centre, and state one feature of each.",
           "Crust: thin, solid outer layer. Mantle: thick layer of hot rock that flows slowly. Outer core: liquid iron and nickel. Inner core: solid iron and nickel at the centre."),
        PQ("Define the lithosphere.",
           "The lithosphere is the rigid outer shell of the Earth, made of the crust and the uppermost part of the mantle. It is about 100 km thick and is broken into tectonic plates."),
        PQ("Explain why continental crust and oceanic crust behave differently when plates meet.",
           "Oceanic crust is thinner and denser, so it tends to sink below lighter, thicker continental crust where the two meet. Continental crust is too light to sink easily."),
        PQ("State two ways in which seismic waves help scientists to know the inside of the Earth.",
           "Their speed changes when they pass from one layer to another, which shows the layers and their materials. S waves do not pass through liquid, so their absence on the far side of the Earth shows that the outer core is liquid."),
        SUM("The Earth has four layers: crust, mantle, outer core and inner core. The crust is thin and solid; the mantle is thick, hot and flows very slowly.",
            "The outer core is liquid iron and nickel; the inner core is solid because of the very high pressure.",
            "Continental crust is thick and light; oceanic crust is thin and dense.",
            "The lithosphere is the crust plus the rigid upper mantle. It is split into plates that move a few centimetres a year on the asthenosphere.",
            "Scientists learn about the inside of the Earth from seismic waves: S waves cannot pass through the liquid outer core."),
    ],
))

# ------------------------------------------------------------------ 2. Rocks by origin
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Rocks by origin: igneous, sedimentary and metamorphic",
    slug="geo-rocks-by-origin",
    minutes=22,
    summary="Rocks are classified by how they formed: igneous rocks from cooled magma or lava, sedimentary rocks from layers of compressed sediments, and metamorphic rocks from older rocks changed by heat and pressure.",
    objectives=[
        "Classify rocks into igneous, sedimentary and metamorphic according to their origin",
        "Describe how each type of rock is formed",
        "Differentiate between the types of rock using their characteristics and examples",
        "Illustrate the rock cycle with a labelled diagram",
    ],
    key_concepts=["Igneous rock", "Intrusive and extrusive", "Sedimentary rock", "Metamorphic rock", "Rock cycle", "Magma and lava"],
    blocks=[
        H("Introduction"),
        T("Look at the black rock on the slopes of Mount Cameroon, the grey stone in a building site in Douala, or the sand and gravel at a river bank "
          "on the Sanaga. These are all rocks, but they were made in very different ways."),
        T("Geographers sort rocks into three groups by their **origin**, that is, how they were formed. Knowing the group tells you a lot about "
          "the rock's appearance and its uses."),
        D("A **rock** is a natural solid made of one or more minerals. Rocks are classified by origin into **igneous**, **sedimentary** and **metamorphic** rocks.", title="Rock"),
        H("Igneous rocks"),
        D("**Igneous rocks** are formed when hot liquid rock cools and becomes solid. Underground the liquid rock is called **magma**. "
          "When it reaches the surface it is called **lava**.", title="Igneous rock"),
        T("There are two kinds, depending on where the cooling happens."),
        KEY("Intrusive and extrusive igneous rocks", "The place of cooling decides the size of the crystals.", cards=[
            ["Intrusive (plutonic)", "Magma cools slowly deep underground. Large crystals can grow. Example: granite."],
            ["Extrusive (volcanic)", "Lava cools quickly on the surface. Crystals are tiny or the rock looks glassy. Example: basalt."],
        ], note="Slow cooling gives big crystals. Fast cooling gives small crystals."),
        T("Igneous rocks are hard and have no layers and no fossils. They are made of interlocking crystals. Many are resistant to weathering. "
          "Granite is used for building and monuments. Basalt is crushed for road stone. The black rocks around Mount Cameroon are volcanic."),
        H("Sedimentary rocks"),
        D("**Sedimentary rocks** are formed from sediments: pieces of rock, sand, mud and the remains of living things that are deposited, "
          "usually in water, and then turned into solid rock.", title="Sedimentary rock"),
        T("They form in steps. Weathering and erosion break rocks into pieces. Rivers, wind or the sea carry the pieces and **deposit** them in layers, for example "
          "on a lake bed or the sea floor. New layers bury the old ones. The weight **compacts** the lower layers. Natural cements glue the grains together. "
          "This is called **cementation**."),
        T("Sedimentary rocks have **layers** (called beds or strata). They often contain **fossils**, the remains of ancient plants and animals. "
          "Many are softer than igneous rocks. Some, such as sandstone, are porous, so they can hold water and oil."),
        KEY("Three groups of sedimentary rocks", "Sedimentary rocks have different sources.", cards=[
            ["Mechanical (clastic)", "Broken pieces of older rock, such as sandstone (sand grains), shale and clay (mud) and conglomerate (rounded pebbles)."],
            ["Organic", "Remains of living things, such as coal (plants) and some limestone (shells and skeletons)."],
            ["Chemical", "Minerals left behind when water evaporates, such as rock salt."],
        ]),
        H("Metamorphic rocks"),
        D("**Metamorphic rocks** are old rocks that have been changed by great heat, great pressure, or both, without melting. "
          "The word means 'changed form'.", title="Metamorphic rock"),
        T("Heat and pressure occur deep underground, near molten magma and where plates collide and build mountains. "
          "The minerals in the rock are rearranged and often form bands or new crystals. The rock becomes harder and more compact."),
        CODE("""Original rock     Becomes (metamorphic)
Limestone         Marble
Shale (mudstone)  Slate
Sandstone         Quartzite
Granite           Gneiss""", "text", title="Examples of change"),
        T("Marble is used for floors and statues. Slate splits into thin sheets and is used for roofing and floor tiles."),
        H("Comparing the three types"),
        CODE("""Type          Formed by                  Features                 Examples
Igneous       Cooling of magma or lava   Crystals, no layers,     Granite, basalt
                                         no fossils, hard
Sedimentary   Deposit and compaction     Layers, fossils,         Sandstone, limestone,
              of sediments               often softer             shale, coal
Metamorphic   Heat and pressure          Hard, banded or          Marble, slate,
              change old rock            crystalline, no fossils  quartzite, gneiss""", "text", title="Summary table"),
        H("The rock cycle"),
        T("Rocks do not stay the same forever. Over millions of years each type can be changed into another. This continuing change is the **rock cycle**."),
        IMG("f5g-geo-rock-cycle.svg", alt="Rock cycle: magma cools to igneous rock, weathering makes sediments, compaction makes sedimentary rock, heat and pressure make metamorphic rock, melting makes magma again",
            caption="Figure 1. The rock cycle."),
        TIP("Exam link: Paper 1 asks you to identify rock types from their description and examples. In Paper 2 Section B you may draw the rock cycle or describe how one rock type forms. "
            "Always name the process on each arrow of the rock cycle."),
        EX("Model answer: how are sedimentary rocks formed?",
           intro="Describe how sedimentary rocks are formed. (5 marks)",
           steps=[
               S("Breakdown", text="Weathering and erosion break existing rocks into small pieces called sediments, such as sand and mud."),
               S("Transport and deposition", text="Rivers, wind and the sea carry the sediments and deposit them in layers, often on lake beds or the sea floor."),
               S("Compaction", text="New layers bury the older ones. The weight of the layers above squeezes the lower layers and pushes out water."),
               S("Cementation", text="Minerals in the water act as a cement and stick the grains together, forming solid rock such as sandstone. Fossils may be trapped in the layers."),
           ]),
        EX("Model answer: differentiate between granite and basalt",
           intro="Granite and basalt are both igneous rocks. Explain why they look different. (4 marks)",
           steps=[
               S("Granite", text="Granite is intrusive. Magma cools slowly deep underground, so there is time for large crystals to grow. The rock is coarse-grained."),
               S("Basalt", text="Basalt is extrusive. Lava cools quickly on the surface, so crystals are tiny. The rock is fine-grained, dark and dense."),
               S("Conclusion", text="The speed of cooling, which depends on where the rock cools, controls the crystal size."),
           ]),
        MISTAKE("Calling marble or slate a sedimentary rock", "They come from limestone and shale, which are sedimentary, but they have been changed by heat and pressure. They are metamorphic."),
        MISTAKE("Saying metamorphic rock is formed by melting", "Metamorphic rock is changed in the solid state. If the rock melts completely it becomes magma, and the cycle starts again."),
        QUIZ("A rock has clear layers and contains shell fossils. It is most likely", ["igneous", "sedimentary", "metamorphic", "volcanic lava"], 1,
             "Layers and fossils are signs of a sedimentary rock, formed from deposited sediments.",
             hint="Which type forms from material laid down in layers?",
             feedback=["Igneous rocks have interlocking crystals, no layers and no fossils.", "",
                       "Metamorphic rocks are changed by heat and pressure, which destroys fossils.",
                       "Lava is liquid rock. It forms igneous rock when it cools."]),
        QUIZ("Limestone is changed by heat and pressure. What does it become?", ["Slate", "Granite", "Marble", "Sandstone"], 2,
             "Limestone becomes marble when it is metamorphosed.",
             hint="Look at the table of examples of change.",
             feedback=["Slate comes from shale or mudstone.", "Granite is igneous, formed from cooled magma.", "",
                       "Sandstone is sedimentary and is not formed by changing limestone."]),
        PQ("Define igneous rock and give two examples.",
           "Igneous rock is formed when magma or lava cools and becomes solid. Examples are granite (intrusive) and basalt (extrusive)."),
        PQ("State two differences between sedimentary rocks and igneous rocks.",
           "Sedimentary rocks have layers and may contain fossils; igneous rocks have no layers and no fossils. Sedimentary rocks are made of compacted sediments; igneous rocks are made of interlocking crystals from cooled magma or lava."),
        PQ("Describe how marble is formed.",
           "Limestone, a sedimentary rock, is changed by great heat and pressure, for example near hot magma or where plates collide. The minerals are rearranged into new crystals. The rock does not melt. The result is hard, crystalline marble."),
        PQ("Draw a simple rock cycle and name the processes between the stages.",
           "Magma cools and solidifies to igneous rock. Weathering and erosion turn it into sediments. Deposition, compaction and cementation make sedimentary rock. Heat and pressure change rock into metamorphic rock. Melting of any rock gives magma again."),
        SUM("Rocks are classified by origin: igneous, sedimentary and metamorphic.",
            "Igneous rocks form when magma or lava cools. Intrusive rocks (granite) cool slowly with large crystals; extrusive rocks (basalt) cool quickly with small crystals.",
            "Sedimentary rocks form from sediments that are deposited, compacted and cemented. They have layers and fossils (sandstone, limestone).",
            "Metamorphic rocks are old rocks changed by heat and pressure without melting (marble, slate).",
            "The rock cycle shows how any type can become another over millions of years."),
    ],
))

# ------------------------------------------------------------------ 3. Plate margins and landscape formation
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Plate margins and landscape formation: folding, faulting, mountains and volcanoes",
    slug="geo-plate-margins-and-landscape-formation",
    minutes=24,
    summary="Plates move at constructive, destructive and conservative margins; folding, faulting, fold mountains, rift valleys, ocean trenches and volcanoes are landscape-forming processes at these margins.",
    objectives=[
        "Describe the movement of tectonic plates and the three types of plate margin",
        "Explain how folding and faulting happen at plate margins",
        "Explain how fold mountains, rift valleys, volcanoes and ocean trenches form",
        "Illustrate plate margins with labelled sketches",
    ],
    key_concepts=["Tectonic plate", "Constructive margin", "Destructive margin", "Conservative margin", "Subduction", "Folding", "Faulting", "Fold mountain", "Rift valley", "Ocean trench"],
    blocks=[
        H("Introduction"),
        T("Why are there high mountains in some countries and none in others? Why do volcanoes and earthquakes occur in some places and almost never in others? "
          "The answer lies in the movement of the plates that make up the Earth's lithosphere."),
        T("The Board's syllabus no longer treats folding, faulting, mountains, plains and plateaus as separate topics. Instead, you must understand them as "
          "**processes of landscape formation at plate margins**. That is what this lesson teaches."),
        H("Plates and their movement"),
        T("The lithosphere is broken into several large plates and many smaller ones. Examples are the African, Eurasian, South American, North American and Pacific plates. "
          "The plates move slowly on the soft asthenosphere. Scientists think that heat from inside the Earth makes the mantle rock circulate in slow **convection currents**, "
          "and these help to move the plates."),
        D("A **plate margin** (or plate boundary) is the place where two plates meet. Most earthquakes, volcanoes and young fold mountains are found along plate margins.", title="Plate margin"),
        IMG("f5g-geo-margins-three-types.svg", alt="Three panels showing plates moving apart (constructive), together (destructive) and sliding past each other (conservative)",
            caption="Figure 1. The three types of plate margin."),
        KEY("Three types of plate margin", "The type of margin depends on how the plates move.", cards=[
            ["Constructive", "Plates move apart. Magma rises and makes new crust. Examples: Mid-Atlantic Ridge, East African Rift."],
            ["Destructive", "Plates move together. One plate sinks (subduction) and crust is destroyed. Examples: Andes, Himalayas, Japan."],
            ["Conservative", "Plates slide past each other. Crust is neither made nor lost. Example: San Andreas Fault, California."],
        ]),
        H("Folding and faulting"),
        T("When plates push together, the rock layers between them are squeezed. If the rock is flexible, it bends into **folds**. If the rock is brittle, it cracks into **faults**."),
        IMG("f5g-geo-fold-fault.svg", alt="Left, rock layers bent into an upfold (anticline) and a downfold (syncline) by squeezing. Right, two faults with a block between them dropped to make a rift valley",
            caption="Figure 2. Folding by compression and faulting by tension (a rift valley)."),
        D("**Folding** is the bending of rock layers when they are squeezed by compression. An upfold is an **anticline** and a downfold is a **syncline**. "
          "**Faulting** is the cracking of rock and the movement of the blocks along the crack, which is called a **fault**.", title="Folding and faulting"),
        H("Constructive margins: ridges and rift valleys"),
        T("At a constructive margin the plates are pulled apart. Magma rises through the gap, cools and adds new crust. Under the oceans, this builds a **mid-ocean ridge**, such as the "
          "Mid-Atlantic Ridge between Africa and South America. Volcanoes form along the ridge, and Iceland is a ridge that has built up above the sea."),
        T("On land, when the crust is stretched, it cracks along two roughly parallel faults. The block between the faults sinks and forms a steep-sided valley, the **rift valley**. "
          "The East African Rift Valley is the best-known example. It has volcanoes and lakes, and earthquakes happen there."),
        H("Destructive margins: trenches, fold mountains and volcanoes"),
        T("At a destructive margin two plates move together. Oceanic crust is denser than continental crust, so when they meet, the oceanic plate is forced down into the mantle. "
          "This is **subduction**."),
        IMG("f5g-geo-subduction.svg", alt="Cross-section where an oceanic plate sinks beneath a continental plate, forming an ocean trench, fold mountains and a volcano with magma rising",
            caption="Figure 3. An oceanic plate sinking under a continental plate (subduction)."),
        KEY("What forms where an ocean plate meets a continent", "Follow the landforms in Figure 3 from left to right.", cards=[
            ["Ocean trench", "A very deep, narrow valley on the sea floor where the plate bends down. Example: the Peru-Chile Trench."],
            ["Fold mountains", "Sediments on the sea floor and edge of the continent are squeezed and crumpled upwards. Example: the Andes."],
            ["Volcanoes", "The sinking plate melts. Magma rises through the continental crust and erupts. Earthquakes happen along the sinking plate."],
        ]),
        T("Two continents can also collide. Neither plate sinks easily because both are light. The rock between them is squeezed upwards into great ranges of fold mountains, "
          "such as the Himalayas and the Alps. There are earthquakes, but few volcanoes. Where two oceanic plates meet, one sinks and a curved chain of volcanic islands forms (an island arc), with a deep trench beside it."),
        H("Conservative margins"),
        T("At a conservative margin the plates slide past each other. The plates can lock, then slip suddenly. This releases energy as earthquakes. "
          "There are no volcanoes and no large mountains. The San Andreas Fault in California is a famous example."),
        H("Mountains, plateaus and plains in this story"),
        T("Uplift at plate margins raises land into **mountains** and **plateaus** (large areas of high, fairly flat land). Over time, weathering, erosion and deposition wear down high land "
          "and spread the material over **plains** (low, flat land). You will study those wearing-down processes in the next topic."),
        T("Cameroon lies inside the African plate, away from its edges. Mount Cameroon belongs to the **Cameroon Line**, a line of volcanic mountains and islands that runs "
          "from the Atlantic Ocean into the highlands of the country. It is not on a plate margin. For the explanation of how it formed, check your textbook."),
        TIP("Exam link: Paper 1 asks which margin forms which landform. Paper 2 Section B often asks you to explain how fold mountains, rift valleys or volcanoes form. "
            "Draw a labelled sketch with arrows showing plate movement. A sketch earns marks and keeps your explanation in order."),
        EX("Model answer: explain how fold mountains are formed",
           intro="With the help of a sketch, explain how fold mountains are formed. (6 marks)",
           steps=[
               S("Sketch", text="Draw two plates with arrows pointing towards each other and layers of sediments between them. Draw the layers crumpled into upfolds and downfolds. Label: plate, direction of movement, sediments, anticline, syncline."),
               S("Plates move together", text="At a destructive margin two plates move towards each other, for example an oceanic plate and a continental plate."),
               S("Sediments are squeezed", text="Layers of sediment lie in the sea between the plates. The plates push on them from both sides, so they are squeezed and compressed."),
               S("Folding and uplift", text="The layers bend into upfolds and downfolds and are pushed upward. Over millions of years the folds are raised into high ranges, such as the Andes and the Himalayas."),
           ]),
        EX("Model answer: how does a rift valley form?",
           intro="Explain how a rift valley is formed at a constructive margin. (5 marks)",
           steps=[
               S("Plates move apart", text="Two plates, or two parts of one plate, are pulled in opposite directions. The crust is stretched and put under tension."),
               S("Faulting", text="The brittle rock cracks along two roughly parallel faults."),
               S("Block drops", text="The block of land between the faults sinks, while the land on both sides stays high. This leaves a long, steep-sided valley. The East African Rift Valley is an example."),
           ]),
        EX("Model answer: how do volcanoes form at a destructive margin?",
           intro="Explain why volcanoes occur at destructive plate margins. (5 marks)",
           steps=[
               S("Subduction", text="The denser oceanic plate sinks below the continental plate into the hot mantle."),
               S("Melting", text="As it sinks, heat and pressure melt the plate and the rock above it, forming magma."),
               S("Eruption", text="Magma is lighter than the solid rock around it, so it rises through cracks. It collects in a magma chamber and erupts at the surface through a vent, building a volcano."),
           ]),
        MISTAKE("Saying that mountains form because the land is 'pushed up' without naming the margin", "Always say which plates move, in which direction, and what is squeezed or pulled. 'Plates move together, rock layers are folded and uplifted' earns more marks."),
        MISTAKE("Putting volcanoes at conservative margins", "At conservative margins plates only slide past, so there is no magma. Expect earthquakes, not volcanoes."),
        QUIZ("Which type of plate margin is the East African Rift Valley associated with?", ["Destructive", "Conservative", "Constructive", "None, because it is a plain"], 2,
             "The rift valley forms where the crust is pulled apart. That is a constructive (divergent) setting.",
             hint="How do the plates move when a rift valley forms?",
             feedback=["Destructive margins are where plates move together.",
                       "Conservative margins are where plates slide past each other.", "",
                       "A rift valley is a landform created by faulting, not a plain."]),
        QUIZ("What is subduction?", ["Plates sliding past each other", "A denser plate sinking below another plate", "Lava cooling on the surface", "Magma rising at a ridge"], 1,
             "In subduction a denser (usually oceanic) plate is forced down below another plate into the mantle.",
             hint="Think about what happens when oceanic and continental plates meet.",
             feedback=["That describes a conservative margin.", "", "That is the formation of extrusive igneous rock.", "That is what happens at a constructive margin."]),
        PQ("Name the three types of plate margin and state how the plates move at each.",
           "Constructive margin: plates move apart. Destructive margin: plates move together. Conservative margin: plates slide past each other."),
        PQ("Define faulting and folding.",
           "Folding is the bending of rock layers by compression. Faulting is the cracking of rock and the movement of blocks along the crack (the fault)."),
        PQ("Explain why an ocean trench is found where an oceanic plate meets a continental plate.",
           "The denser oceanic plate is forced to sink below the lighter continental plate. As it bends downwards it forms a very deep, narrow valley on the sea floor, the ocean trench."),
        PQ("Why are there no volcanoes along the San Andreas Fault?",
           "It is a conservative margin. The plates slide past each other, so no crust is destroyed and no magma is made. The movement causes earthquakes only."),
        SUM("Plates move at three kinds of margin: constructive (apart), destructive (together) and conservative (past each other).",
            "Folding bends rock layers by compression; faulting cracks rock and moves blocks.",
            "Constructive margins: ridges, rift valleys and volcanoes. Destructive margins: trenches, fold mountains and volcanoes. Conservative margins: earthquakes.",
            "Mountains and plateaus are raised at plate margins; erosion and deposition later wear them down and build plains.",
            "Cameroon is inside the African plate. Mount Cameroon is on the Cameroon Line: check your textbook for how it formed."),
    ],
))

# ------------------------------------------------------------------ 4. Volcanic eruptions
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Volcanic eruptions: parts, types, products and distribution",
    slug="geo-volcanic-eruptions",
    minutes=22,
    summary="A volcano is an opening in the crust through which magma, gases and ash erupt; learn its parts, its types by shape and activity, what it produces and where volcanoes are found.",
    objectives=[
        "Define a volcanic eruption and a volcano",
        "Illustrate and describe the main parts of a volcano",
        "Describe the types of volcano and the products of an eruption",
        "Describe the distribution of volcanoes and explain it using plate margins",
    ],
    key_concepts=["Volcano", "Vent", "Crater", "Magma chamber", "Lava", "Pyroclasts", "Shield volcano", "Composite volcano", "Active, dormant and extinct", "Distribution"],
    blocks=[
        H("Introduction"),
        T("Mount Cameroon rises beside the Atlantic coast near Limbe and Buea. It is the highest peak in Cameroon and it is an active volcano. "
          "Farmers on its slopes grow crops in the rich soil, while the mountain also reminds everyone that the Earth is alive underneath."),
        T("In this lesson you will learn what a volcano is, how it is built, what comes out of it and why volcanoes are found where they are."),
        D("A **volcanic eruption** is the release of magma, gases and fragments of rock from inside the Earth onto the surface. "
          "A **volcano** is the opening in the crust, and the cone-shaped hill built around it, from which this material escapes.", title="Volcano and eruption"),
        H("Parts of a volcano"),
        IMG("f5g-geo-volcano-parts.svg", alt="Cross-section of a volcano showing the magma chamber, main vent, side vent, crater, cone made of layers of ash and lava, lava flow and ash cloud",
            caption="Figure 1. The parts of a volcano (cross-section, not to scale)."),
        KEY("Learn these parts", "Follow the path of magma from the bottom up.", cards=[
            ["Magma chamber", "A large underground pool of molten rock below the volcano."],
            ["Vent", "The pipe through which magma rises. The main vent leads to the crater; side vents may break through the cone."],
            ["Crater", "The bowl-shaped hollow at the top of the cone, around the main vent."],
            ["Cone", "The hill built up by layers of lava and ash from many eruptions."],
        ]),
        T("When pressure in the magma chamber becomes too great, magma is forced up the vent. Gas dissolved in the magma expands, like the fizz in a shaken bottle, and "
          "this can make the eruption explosive."),
        H("Types of volcano by shape"),
        IMG("f5g-geo-volcano-types.svg", alt="Three volcano shapes: wide shield volcano, tall steep composite cone and small cinder cone, with their features",
            caption="Figure 2. Three main types of volcano."),
        T("The shape depends on the kind of lava and on how violently the volcano erupts."),
        T("**Shield volcanoes** have runny lava. It flows a long way before it sets, so the volcano becomes wide with gentle slopes. Eruptions are fairly gentle. "
          "Mauna Loa in Hawaii is an example."),
        T("**Composite (strato) volcanoes** have thick, sticky lava and a lot of ash. They erupt violently and build tall, steep cones made of alternate layers of ash and lava. "
          "Mount Fuji in Japan and Mount Etna in Italy are examples."),
        T("**Cinder cones** are small, steep cones made of loose ash and cinders thrown out of a vent. They form quickly and are often found on the sides of larger volcanoes."),
        H("Active, dormant and extinct"),
        KEY("Classifying volcanoes by activity", "Look at how recently they erupted.", cards=[
            ["Active", "Has erupted recently or is likely to erupt again. Mount Cameroon is active."],
            ["Dormant", "'Sleeping'. Has not erupted for a long time but could erupt again."],
            ["Extinct", "Not expected to erupt again. The magma supply has gone."],
        ], note="It can be hard to tell dormant from extinct: some volcanoes thought to be extinct have erupted again."),
        H("Products of an eruption"),
        T("An eruption can send out materials in three states."),
        KEY("What comes out of a volcano", "Gas, liquid and solid.", cards=[
            ["Gases", "Steam, carbon dioxide, sulphur dioxide and others. Some gases are poisonous."],
            ["Lava", "Molten rock that flows on the surface. Runny lava travels far; sticky lava piles up near the vent."],
            ["Pyroclasts", "Solid fragments thrown into the air: ash (fine dust), lapilli (small stones) and volcanic bombs (large lumps)."],
        ]),
        T("Two more products are dangerous. A **pyroclastic flow** is a fast cloud of hot gas and ash that rushes down the slopes. A **lahar** (volcanic mudflow) is a river of ash and water, "
          "for example when rain falls on loose ash or a crater lake spills out."),
        H("Where are volcanoes found?"),
        T("Volcanoes are not spread evenly over the Earth. Most are found along plate margins."),
        KEY("Pattern of distribution", "Link each group to a margin.", cards=[
            ["Pacific Ring of Fire", "A ring of destructive margins around the Pacific Ocean, with about three quarters of the world's active volcanoes. Includes Japan, the Philippines and the Andes."],
            ["Mid-ocean ridges", "Constructive margins such as the Mid-Atlantic Ridge. Iceland is on this ridge."],
            ["East African Rift", "Where the African plate is slowly splitting, giving volcanoes such as Kilimanjaro and Nyiragongo in eastern Africa."],
            ["Hot spots", "A few volcanoes form far from plate edges, over very hot places in the mantle. Hawaii is the usual example."],
        ]),
        T("Mount Cameroon is also away from a plate edge. It is part of the Cameroon Line. Check your textbook for the explanation."),
        TIP("Exam link: Paper 1 may ask you to identify parts of a volcano on a diagram or match a volcano type to its features. In Paper 2 Section B you may be asked to draw "
            "and label a volcano and describe where volcanoes occur. Label at least five parts and name an example."),
        EX("Model answer: describe the structure of a volcano",
           intro="With the help of a labelled diagram, describe the main parts of a volcano. (5 marks)",
           steps=[
               S("Diagram", text="Draw a cone with a crater at the top and a vertical pipe down to a magma chamber. Label: crater, vent, cone, layers of ash and lava, magma chamber. Add a side vent and a lava flow."),
               S("Underground", text="The magma chamber is a pool of molten rock beneath the volcano. The vent is the pipe that carries the magma upward."),
               S("At the surface", text="The magma erupts through the crater at the top of the cone. The cone is built of layers of lava and ash from many eruptions."),
           ]),
        EX("Model answer: compare shield and composite volcanoes",
           intro="Describe the differences between a shield volcano and a composite volcano. (4 marks)",
           steps=[
               S("Shape", text="A shield volcano is wide with gentle slopes. A composite volcano is tall with steep slopes."),
               S("Lava", text="Shield volcanoes have runny lava that flows far. Composite volcanoes have thick, sticky lava that does not flow far."),
               S("Eruption", text="Shield volcanoes erupt gently. Composite volcanoes erupt violently, throwing out ash as well as lava, so their cone has layers of ash and lava."),
           ]),
        EX("Model answer: describe the distribution of volcanoes",
           intro="Describe the world distribution of active volcanoes and explain the pattern. (6 marks)",
           steps=[
               S("Pattern", text="Most active volcanoes lie in narrow belts. The largest belt is the Pacific Ring of Fire. Others follow the mid-ocean ridges and the East African Rift."),
               S("Explanation", text="These belts are plate margins. At destructive margins plates are subducted and melt. At constructive margins magma rises where plates pull apart."),
               S("Exceptions", text="A few volcanoes, such as Hawaii, are away from plate margins, above hot spots in the mantle."),
           ]),
        MISTAKE("Thinking that all volcanoes are cone-shaped mountains that erupt lava", "Many eruptions are mostly ash and gas. Shield volcanoes are wide and low. Always state the product and the type."),
        MISTAKE("Confusing magma and lava", "Magma is molten rock underground. Lava is molten rock on the surface."),
        QUIZ("Which part of a volcano is the pipe through which magma rises?", ["Crater", "Vent", "Magma chamber", "Cone"], 1,
             "The vent is the pipe. The crater is the bowl at the top of it.",
             hint="Think about the path the magma takes.",
             feedback=["The crater is the hollow at the top, where the vent reaches the surface.", "",
                       "The magma chamber is the underground store of magma.", "The cone is the hill built from lava and ash."]),
        QUIZ("A tall, steep volcano made of alternate layers of ash and lava is called a", ["shield volcano", "cinder cone", "composite volcano", "rift volcano"], 2,
             "Composite (strato) volcanoes have sticky lava and ash that build steep cones in layers.",
             hint="Look at the layers in the cone.",
             feedback=["Shield volcanoes are wide and low, made of runny lava.",
                       "A cinder cone is small and made of loose cinders.", "",
                       "'Rift volcano' is not a standard type."]),
        PQ("Define lava and name two pyroclastic products.",
           "Lava is molten rock that flows out onto the Earth's surface. Pyroclastic products include ash, lapilli (small stones) and volcanic bombs."),
        PQ("State the difference between an active and an extinct volcano.",
           "An active volcano has erupted recently or may erupt again. An extinct volcano is not expected to erupt again because its magma supply has gone."),
        PQ("Why are most volcanoes found along plate margins?",
           "At destructive margins a plate sinks and melts, and the magma rises. At constructive margins plates move apart and magma rises through the gap. Both processes produce magma near plate edges."),
        PQ("Describe two products of a volcanic eruption that are dangerous to people.",
           "Pyroclastic flows are fast clouds of hot gas and ash that burn and bury everything. Poisonous gases such as sulphur dioxide can make people ill. Lahars (mudflows) can bury villages in the valleys below."),
        SUM("A volcanic eruption releases magma, gases and rock fragments through a vent. Parts: magma chamber, vent, crater, cone.",
            "Shield volcanoes are wide with runny lava; composite volcanoes are steep with sticky lava and ash; cinder cones are small.",
            "Volcanoes are active, dormant or extinct.",
            "Products: gases, lava and pyroclasts (ash, lapilli, bombs), plus pyroclastic flows and lahars.",
            "Most volcanoes lie on plate margins (Ring of Fire, mid-ocean ridges, East African Rift); a few are over hot spots."),
    ],
))

# ------------------------------------------------------------------ 5. Earthquakes
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Earthquakes: causes, measurement and distribution",
    slug="geo-earthquakes",
    minutes=20,
    summary="An earthquake is a shaking of the ground caused by a sudden release of energy; learn focus, epicentre, seismic waves, causes, the Richter and Mercalli scales, and where earthquakes occur.",
    objectives=[
        "Define an earthquake, focus and epicentre",
        "Explain the causes of earthquakes",
        "Describe how earthquakes are measured with the Richter and Mercalli scales",
        "Describe the distribution of earthquakes and link it to plate margins",
    ],
    key_concepts=["Earthquake", "Focus", "Epicentre", "Seismic waves", "Seismograph", "Richter scale (magnitude)", "Mercalli scale (intensity)", "Distribution"],
    blocks=[
        H("Introduction"),
        T("Most Cameroonians will never feel a strong earthquake, because Cameroon is far from the edges of tectonic plates. But in Japan, Chile or Turkey, "
          "earthquakes are part of life. They can also be felt in Africa, especially along the East African Rift and in parts of North Africa."),
        T("In this lesson you will learn the vocabulary of earthquakes, what causes them, how scientists measure them and where they occur."),
        D("An **earthquake** is a sudden shaking or trembling of the ground caused by a rapid release of energy in the Earth's crust or upper mantle.", title="Earthquake"),
        H("Focus, epicentre and seismic waves"),
        IMG("f5g-geo-earthquake-focus.svg", alt="Side view of the ground showing the fault, the focus underground, the epicentre on the surface directly above it, and seismic waves spreading out",
            caption="Figure 1. Focus, epicentre and seismic waves."),
        KEY("Key words", "Learn these three terms exactly.", cards=[
            ["Focus", "The point underground where the rock breaks and the earthquake starts."],
            ["Epicentre", "The point on the surface directly above the focus. Damage is usually greatest here."],
            ["Seismic waves", "Shock waves that spread out from the focus in all directions."],
        ]),
        T("There are three main kinds of wave. **P waves** (primary) are the fastest and arrive first. **S waves** (secondary) arrive second. "
          "**Surface waves** (L waves) travel along the ground, arrive last and cause most of the damage because they shake the ground strongly."),
        H("Causes of earthquakes"),
        T("Most earthquakes happen along **faults** at plate margins. Plates do not move smoothly. Their edges get stuck, and stress builds up in the rocks for years. "
          "When the stress becomes greater than the strength of the rock, the rock suddenly slips along the fault. The stored energy is released as seismic waves."),
        T("Other causes are less common. Rising magma and eruptions can shake the ground near a volcano. Human activities such as filling a large reservoir behind a dam, deep mining "
          "or underground explosions can occasionally trigger small earthquakes."),
        KEY("Causes in summary", "One main cause and three smaller ones.", cards=[
            ["Plate movement", "The main cause: sudden slip along faults at plate margins."],
            ["Volcanic activity", "Moving magma and eruptions shake the ground."],
            ["Human activity", "Large reservoirs, mining and explosions can trigger small quakes."],
        ]),
        H("Measuring earthquakes"),
        T("A **seismograph** is an instrument that detects and records ground movement. Its record is called a seismogram. "
          "Scientists use the arrival times of waves at several stations to find the epicentre."),
        D("The **Richter scale** measures the **magnitude** of an earthquake, that is, the energy released. "
          "It is a number, for example 6.5. The scale is not a straight line: each whole number up means the ground shakes about 10 times more, and about 30 times more energy is released. "
          "There is no upper limit, but quakes above 8 are very rare.", title="Richter scale"),
        D("The **Mercalli scale** measures the **intensity** of an earthquake, that is, the effects felt at a place, from I (not felt) to XII (total destruction). "
          "It is based on what people see and feel, so the same earthquake can have different intensities in different places.", title="Mercalli scale"),
        CODE("""Magnitude   Amplitude compared with magnitude 5
5           same (starting point)
6           10 times
7           100 times
8           1,000 times""", "text", title="Richter scale: each step is about 10 times bigger"),
        T("Today scientists often use a related measure called the moment magnitude, which is reported on the same type of scale. For your exam, know the Richter scale (magnitude) and the Mercalli scale (intensity)."),
        H("Where do earthquakes occur?"),
        T("Earthquakes occur mainly in long, narrow belts that follow plate margins."),
        KEY("Pattern of distribution", "Link each belt to a margin.", cards=[
            ["Pacific Ring of Fire", "The most active belt: destructive and conservative margins around the Pacific, from Chile and Japan to California."],
            ["Alpine-Himalayan belt", "Where continents collide, from the Mediterranean through Turkey to the Himalayas."],
            ["Mid-ocean ridges", "Mostly small, shallow earthquakes at constructive margins."],
            ["East African Rift", "Earthquakes along the rift where the African plate is splitting."],
        ]),
        T("Deep earthquakes occur at destructive margins, along the sinking plate. Earthquakes at constructive margins are shallow. "
          "Strong earthquakes are rare in the middle of plates, as in most of Cameroon. For the earthquake history of Cameroon, check your textbook."),
        TIP("Exam link: Paper 1 tests the definitions (focus, epicentre) and the two scales. Paper 2 Section B may ask you to explain the causes of earthquakes and describe their distribution. "
            "Use a sketch like Figure 1 and say that most quakes lie on plate margins."),
        EX("Model answer: causes of earthquakes",
           intro="Explain how earthquakes are caused at plate margins. (5 marks)",
           steps=[
               S("Plates move", text="Tectonic plates are always moving slowly. At plate margins, such as conservative or destructive margins, their edges can lock together at a fault."),
               S("Stress builds up", text="While the plates are locked, the rocks are squeezed or stretched and strain energy builds up."),
               S("Sudden release", text="When the stress is greater than the strength of the rock, the rocks slip suddenly along the fault. The energy is released as seismic waves that shake the ground. The place where the rock breaks is the focus."),
           ]),
        EX("Model answer: distinguish magnitude from intensity",
           intro="Distinguish between the Richter scale and the Mercalli scale. (4 marks)",
           steps=[
               S("Richter", text="The Richter scale measures magnitude, the energy released at the focus, using a seismograph. One number is given for the earthquake, and each step is about ten times bigger."),
               S("Mercalli", text="The Mercalli scale measures intensity, the effects at a particular place, from I to XII. It is based on observations of damage and what people felt."),
               S("Difference", text="Richter uses instrument readings; Mercalli uses effects. One earthquake has one magnitude but different intensities at different places."),
           ]),
        MISTAKE("Saying the epicentre is underground", "The focus is underground. The epicentre is on the surface directly above the focus."),
        MISTAKE("Thinking a magnitude 7 earthquake is only a little bigger than magnitude 6", "The Richter scale rises in steps of about 10 times in ground movement. Magnitude 7 is ten times bigger in amplitude than 6."),
        QUIZ("The point on the Earth's surface directly above the focus is the", ["fault", "epicentre", "seismograph", "vent"], 1,
             "The epicentre is directly above the focus.",
             hint="Where is the focus: on the surface or underground?",
             feedback=["A fault is the crack along which rocks move.", "",
                       "A seismograph is the instrument that records earthquakes.",
                       "A vent is an opening of a volcano."]),
        QUIZ("Which statement about the Richter scale is correct?", [
            "It measures damage to buildings", "It measures the magnitude, and each whole number is about ten times bigger", "It runs from I to XII", "It was invented to measure volcanoes"], 1,
             "Richter measures magnitude, and each step is about ten times greater in ground motion.",
             hint="Remember which scale has Roman numerals.",
             feedback=["Damage is measured by the Mercalli scale.", "", "I to XII is the Mercalli scale.", "It measures earthquakes, not volcanoes."]),
        PQ("Define focus and epicentre.",
           "The focus is the point underground where the rock breaks and the earthquake starts. The epicentre is the point on the surface directly above the focus."),
        PQ("Give two causes of earthquakes.",
           "Movement of tectonic plates along faults at plate margins is the main cause. Others are volcanic activity and human activities such as filling large reservoirs or deep mining."),
        PQ("State two differences between the Richter scale and the Mercalli scale.",
           "Richter measures magnitude (energy) with a seismograph and gives a number such as 6.5, with no fixed top. Mercalli measures intensity (effects) by observation and runs from I to XII."),
        PQ("Describe the distribution of earthquakes in the world.",
           "Earthquakes occur mostly in narrow belts along plate margins: the Pacific Ring of Fire, the Alpine-Himalayan belt, mid-ocean ridges and the East African Rift. They are rare in the interiors of plates."),
        SUM("An earthquake is a sudden shaking of the ground. The focus is underground; the epicentre is on the surface above it.",
            "Seismic waves: P waves arrive first, S waves second, and surface waves last and cause most damage.",
            "Most earthquakes are caused by sudden slip along faults at plate margins. Volcanic and human activity cause a few.",
            "The Richter scale measures magnitude (about 10 times greater for each whole number). The Mercalli scale measures intensity (I to XII) by effects.",
            "Earthquakes occur along plate margins, as in the Ring of Fire, Alpine-Himalayan belt, mid-ocean ridges and East African Rift."),
    ],
))

# ------------------------------------------------------------------ 6. Geo-hazards
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Volcanic and earthquake hazards: impacts and mitigation",
    slug="geo-hazards-impacts-and-mitigation",
    minutes=24,
    summary="Volcanic eruptions and earthquakes have harmful and useful effects; people reduce the risk through monitoring, prediction, preparation, safer buildings, evacuation plans and emergency response.",
    objectives=[
        "Describe the negative and positive impacts of volcanic eruptions and earthquakes",
        "Distinguish between what can and cannot be predicted",
        "Outline strategies for preparing for, reducing and responding to these hazards",
        "Use African examples in general terms to support an answer",
    ],
    key_concepts=["Geo-hazard", "Primary and secondary effects", "Prediction", "Monitoring", "Preparation", "Mitigation", "Evacuation", "Earthquake-resistant building"],
    blocks=[
        H("Introduction"),
        T("In August 1986, a cloud of gas rose from Lake Nyos, a crater lake in the North-West Region of Cameroon. It killed many people and animals in the villages nearby. "
          "It came without warning. Today scientists have studied the lake and made it safer. Check your textbook for the full account."),
        T("Mount Cameroon is also an active volcano near towns with many thousands of people. For people who live close to volcanoes, planning ahead is a matter of life and death."),
        D("A **geo-hazard** is a natural event in the Earth, such as a volcanic eruption or an earthquake, that threatens people, property or the environment. "
          "A **hazard** becomes a **disaster** when it harms many people.", title="Geo-hazard"),
        H("Impacts of volcanic eruptions"),
        KEY("Negative impacts", "Think about people, property, farms and transport.", cards=[
            ["People", "Deaths and injuries from pyroclastic flows, ash, lava, poisonous gases and lahars. People lose their homes."],
            ["Property and farms", "Lava and ash bury houses, roads and crops. Heavy ash can make roofs collapse and kill farm animals."],
            ["Economy and transport", "Ash clouds close airports. Tourism and trade fall. Rebuilding costs a great deal."],
        ]),
        KEY("Positive impacts", "Volcanoes also bring benefits.", cards=[
            ["Fertile soils", "Weathered volcanic rock and ash make rich soil, so farmers often live on volcanic slopes, as on and around Mount Cameroon."],
            ["Energy and minerals", "Geothermal energy comes from heat underground, for example in the East African Rift in Kenya. Volcanic areas also give building stone and minerals."],
            ["Tourism", "Visitors come to see volcanoes and hot springs. This creates jobs."],
        ]),
        H("Impacts of earthquakes"),
        T("Earthquakes cause **primary effects**, caused directly by the shaking, and **secondary effects**, which follow from them."),
        KEY("Primary and secondary effects", "The shaking comes first, then the chain of consequences.", cards=[
            ["Primary", "Buildings and bridges collapse. People are killed or trapped. Roads, pipes and power lines break."],
            ["Secondary", "Fires from broken gas pipes or electric wires, landslides, tsunamis at the coast, disease from dirty water, homelessness and loss of jobs."],
        ]),
        T("The positive effects of earthquakes are few. They can create new landforms and open springs. The need to rebuild can lead to safer buildings and better planning."),
        H("Can they be predicted?"),
        T("**Prediction** means saying when and where a hazard will happen. **Monitoring** means watching for warning signs."),
        T("Volcanoes can be monitored. Before an eruption, scientists may record many small earthquakes, swelling of the ground, changes in gas and rising temperature. "
          "This helps them to warn people and to decide when to evacuate, although the exact time is still difficult to give."),
        T("Earthquakes cannot be predicted accurately. Scientists can say which places are at high risk from past records and fault maps. They cannot say the day or hour. "
          "In some countries sensors give a few seconds of warning after a quake starts, which is enough to stop trains and gas supplies."),
        H("Preparing and reducing the damage"),
        IMG("f5g-geo-hazard-cycle.svg", alt="Four boxes in a cycle: monitor, prepare, warn and respond, recover",
            caption="Figure 1. The hazard management cycle."),
        KEY("Strategies that save lives", "Use these headings in your answers.", cards=[
            ["Monitoring and hazard maps", "Seismographs and gas and ground sensors. Maps show danger zones so that homes are not built there."],
            ["Building design", "Earthquake-resistant buildings: strong steel or reinforced concrete frames, cross-bracing, flexible foundations, low and light structures. Steeply sloping roofs near volcanoes help ash slide off."],
            ["Education and drills", "Teach 'drop, cover and hold on' in earthquakes. Practise drills in schools. Keep emergency kits with water, food and a torch."],
            ["Evacuation plans", "Marked escape routes, warning sirens, shelters and exclusion zones around volcanoes. Everyone should know the plan."],
            ["Emergency response", "Search and rescue, first aid, clean water and temporary shelter. Governments, the Red Cross and other organisations send aid."],
        ]),
        T("Rich countries can afford strong buildings and advanced monitoring. Poorer countries may not. Education, simple drills and community plans cost little and still save lives. "
          "Money, trained rescue workers and good roads make a big difference after the event."),
        H("African examples (general)"),
        T("**Nyiragongo**, in the Democratic Republic of Congo near the town of Goma, has erupted several times. Lava has flowed towards Goma and many families have had to move. "
          "The city is close to the volcano, so monitoring and evacuation plans are important there."),
        T("**Lake Nyos** in Cameroon showed a different danger: a large amount of gas escaped suddenly from a lake in a volcanic area. Since then, scientists have installed pipes to release "
          "the gas slowly and safely. For dates and numbers, check your textbook."),
        T("**Mount Cameroon** is monitored because people live on its slopes. If you need a local example in an answer, say that people near the volcano need warning systems and "
          "evacuation routes, and check your textbook for details."),
        TIP("Exam link: Paper 1 may ask for the positive and negative effects or for a strategy. Paper 2 Section B is likely to ask you to describe the impacts and the ways of reducing them. "
            "A strong answer gives a point, an example or detail, and an explanation, and separates short-term effects from long-term effects."),
        EX("Model answer: impacts of a volcanic eruption",
           intro="Describe the negative impacts of volcanic eruptions on people and the environment. (6 marks)",
           steps=[
               S("Loss of life", text="Pyroclastic flows, lahars and poisonous gases can kill people and animals quickly. Many others are injured or made homeless."),
               S("Damage to farms and property", text="Lava and ash bury houses, roads and fields. Crops are destroyed, so food becomes scarce and prices rise."),
               S("Wider effects", text="Ash clouds stop flights and trade, and tourism falls. Gases and ash can pollute the air and water."),
           ]),
        EX("Model answer: managing earthquake risk",
           intro="Outline how the damage from earthquakes can be reduced. (6 marks)",
           steps=[
               S("Building design", text="Build strong frames with cross-bracing and flexible foundations so buildings sway rather than collapse. Follow building codes."),
               S("Education and drills", text="Teach people to drop, cover and hold on. Hold regular school drills and prepare emergency kits, so that people know what to do."),
               S("Planning and response", text="Use hazard maps so that schools and hospitals are not built on weak ground. Have trained rescue teams, first aid and shelters ready."),
           ]),
        MISTAKE("Saying that scientists can predict earthquakes exactly", "They can say where earthquakes are likely, not when. Warning times are seconds, not days. Volcanoes can often be monitored for warning signs."),
        MISTAKE("Listing effects without developing them", "A mark is earned for a point plus a detail. Write 'buildings collapse because the ground shakes, trapping people', not just 'buildings collapse'."),
        QUIZ("Which of these is a SECONDARY effect of an earthquake?", ["Buildings collapse", "Fires start from broken gas pipes", "The ground shakes", "A fault slips"], 1,
             "Fires start after the shaking, so they are a secondary effect.",
             hint="Which one happens as a result of the shaking?",
             feedback=["Collapse is caused directly by the shaking, so it is primary.", "",
                       "The shaking itself is the event, not a secondary effect.", "Fault movement is the cause of the earthquake."]),
        QUIZ("Which strategy is a correct way to reduce earthquake damage?", [
            "Build with heavy roofs and no frames", "Keep all supplies in one building next to the fault", "Teach drills and use strong, flexible building designs", "Wait for exact predictions"], 2,
             "Education and strong, flexible buildings reduce deaths and damage.",
             hint="Which choice is a realistic way to prepare in advance?",
             feedback=["Heavy roofs and weak frames collapse and kill people.",
                       "Supplies should be stored in safe places, not beside the fault.", "",
                       "Earthquakes cannot be predicted exactly, so we must prepare before they strike."]),
        PQ("Give two positive effects of volcanic eruptions.",
           "Volcanic ash and rock weather into fertile soils for farming. Geothermal energy and minerals can be used, and volcanoes attract tourists."),
        PQ("Explain why earthquakes are more difficult to predict than volcanic eruptions.",
           "Volcanoes give warning signs such as small earthquakes, ground swelling and gas changes that can be monitored. Earthquakes happen when stress in the rock suddenly exceeds its strength, with no clear warning signs, so only the places at risk can be identified."),
        PQ("Outline three ways of preparing for an earthquake.",
           "Build earthquake-resistant buildings, teach drills such as drop, cover and hold on, and prepare emergency kits and evacuation plans."),
        PQ("Describe two ways in which the response to a disaster differs in a rich and a poor country.",
           "Rich countries can afford strong buildings, advanced monitoring and well-equipped rescue services, so fewer people die. Poorer countries have fewer resources, so they depend more on education, community plans and international aid."),
        SUM("Volcanic hazards: pyroclastic flows, ash, lava, gases and lahars. Earthquake hazards: collapse, fires, landslides and tsunamis.",
            "Volcanoes also bring fertile soils, geothermal energy, minerals and tourism.",
            "Volcanoes can be monitored for warning signs; earthquakes cannot be predicted accurately.",
            "Reduce harm by monitoring, hazard maps, strong building design, drills, evacuation plans and emergency response.",
            "African examples: Nyiragongo (DR Congo), Lake Nyos and Mount Cameroon; check your textbook for details."),
    ],
))
