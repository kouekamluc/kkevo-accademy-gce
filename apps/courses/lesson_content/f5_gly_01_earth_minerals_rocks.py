"""Form 5 Geology (0555): Earth, minerals and rocks (modules 1 to 3; 13 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geology", "form-5")

M1 = "Introduction, Solar System & Global Tectonics"
M2 = "Crystallography & Mineralogy"
M3 = "Petrology: Igneous, Sedimentary & Metamorphic Rocks"

LESSONS = []

# ------------------------------------------------------------------ 1. Geology and its branches
LESSONS.append(lesson(
    module=M1, topic="Geology and its branches",
    title="What is geology? Branches and careers",
    slug="gly1-geology-and-its-branches",
    minutes=18,
    summary="Geology is the scientific study of the Earth: its materials, structure, processes and history; it has many branches (such as mineralogy, petrology, hydrogeology) and leads to careers in mining, oil, water supply and hazard work.",
    objectives=[
        "Define geology and explain why it matters in Cameroon",
        "Name and define the main branches of geology",
        "Match each branch to the question it answers",
        "Describe careers that use geology",
    ],
    key_concepts=["Geology", "Branches of geology", "Hydrogeology", "Economic geology", "Geologist"],
    blocks=[
        H("Introduction"),
        T("When a borehole is drilled in your town, someone must decide where to drill. When a road is cut through a hill near Bamenda, "
          "someone must check that the slope will not slide. When a company looks for gold in the East Region, someone must read the rocks. "
          "That someone is a geologist."),
        D("**Geology** is the scientific study of the Earth: the materials it is made of, its structure, the processes that shape it, "
          "and its history over about 4.6 billion years.", title="Geology"),
        T("Geology asks four big questions. What is the Earth made of? How is it built? What processes change it? How has it changed in the past? "
          "Each question has its own branch of geology."),
        H("The main branches"),
        KEY("Branches and the question each one answers", "Learn the branch name with its key question.", cards=[
            ["Mineralogy", "The study of minerals: their composition, crystals and properties."],
            ["Petrology", "The study of rocks: how igneous, sedimentary and metamorphic rocks form and what they contain."],
            ["Structural geology", "The study of how rocks are bent, broken and tilted (folds, faults, joints)."],
            ["Stratigraphy", "The study of layered rocks, their order and their ages."],
            ["Palaeontology", "The study of fossils and ancient life."],
            ["Geomorphology", "The study of landforms and the surface processes that make them."],
            ["Hydrogeology", "The study of groundwater, the water held in rocks below the ground."],
            ["Economic geology", "The study of useful rocks, minerals, ores, oil and coal and how they are found and used."],
        ]),
        T("There are more branches. **Geophysics** uses physics (waves, gravity, magnetism) to study the Earth. **Geochemistry** uses chemistry. "
          "**Volcanology** studies volcanoes and **seismology** studies earthquakes. **Engineering geology** applies geology to roads, dams and buildings. "
          "**Environmental geology** deals with pollution and natural hazards."),
        MISTAKE("Defining hydrogeology as the study of water",
                "The Board's report on a recent paper says many candidates defined hydrogeology as the study of water. That is too wide. "
                "Hydrogeology is the study of **groundwater**: water found below the surface in soil and rock. Always write the word groundwater."),
        H("Geology in Cameroon"),
        T("Cameroon is a good place to study geology. Mount Cameroon is an active volcano. Old granite and gneiss rocks form much of the land. "
          "The country has gold, bauxite, iron ore, rutile (a titanium mineral) and oil. Lake Nyos, a crater lake in the north-west, released a deadly cloud "
          "of carbon dioxide gas in 1986, which shows why geologists study hazards."),
        EX("Worked example 1: which branch?",
           intro="A student asks four questions. Name the branch of geology that answers each one.",
           steps=[
               S("Question 1: How did this granite crystallise from magma?", text="This is about the formation of a rock: **petrology**."),
               S("Question 2: Why does this layer of rock tilt and then stop at a crack?", text="Tilts and cracks are rock deformation: **structural geology**."),
               S("Question 3: How deep should the borehole go to reach water?", text="Water below ground: **hydrogeology**."),
               S("Question 4: What is the age order of these fossil-bearing layers?", text="Order of layers: **stratigraphy**; the fossils themselves: **palaeontology**."),
           ]),
        H("Careers that use geology"),
        KEY("Where geologists work", "A geologist may work for a company, a government service or a school.", cards=[
            ["Mining and minerals", "Finding and assessing gold, bauxite, iron ore, rutile, limestone and building stone."],
            ["Petroleum", "Reading sedimentary basins to find oil and gas; Cameroon has the Douala and Rio del Rey basins."],
            ["Water supply", "Siting boreholes and wells; protecting groundwater from pollution."],
            ["Engineering", "Checking rock and soil before building roads, bridges, dams and houses."],
            ["Hazards and environment", "Monitoring volcanoes, landslides and gas hazards; advising on safe land use."],
            ["Teaching and research", "Universities, schools and national geological survey work."],
        ]),
        EX("Worked example 2: link a job to a branch",
           intro="A village needs a borehole on a hillside. Explain which branches of geology help and how.",
           steps=[
               S("Find where water is stored", text="**Hydrogeology** tells us where groundwater collects and how deep the water table is."),
               S("Know the rocks underneath", text="**Petrology** and **mineralogy** identify whether the rock is sandy (holds water) or hard crystalline rock (holds little)."),
               S("Check the ground structure", text="**Structural geology** shows cracks and faults that may carry water."),
               S("Conclusion", text="Several branches work together; no single branch gives the whole answer."),
           ]),
        QUIZ("Which branch of geology studies fossils?", ["Mineralogy", "Palaeontology", "Hydrogeology", "Petrology"], 1,
             "Palaeontology is the study of fossils and ancient life.", hint="Fossils are the remains of ancient life.",
             feedback=["Mineralogy studies minerals, not fossils.", "", "Hydrogeology studies groundwater.", "Petrology studies rocks, although fossils may be found inside them."]),
        QUIZ("A geologist maps a fault and measures how the rocks are tilted. Which branch is this?",
             ["Structural geology", "Economic geology", "Geomorphology", "Geochemistry"], 0,
             "Faults and tilting are structures made by rock deformation.", hint="Think of folds, faults and joints.",
             feedback=["", "Economic geology deals with useful minerals and fuels.", "Geomorphology deals with surface landforms.", "Geochemistry studies the chemistry of rocks and minerals."]),
        TIP("Exam link: Paper 1 asks short multiple-choice questions on definitions and branches. Paper 2 can ask you to define terms such as hydrogeology. "
            "Learn each definition in one precise sentence."),
        PQ("Define geology and name any four branches of geology.",
           "Geology is the scientific study of the Earth: its materials, structure, processes and history. Four branches: mineralogy, petrology, stratigraphy, hydrogeology (others: structural geology, palaeontology, geomorphology, economic geology)."),
        PQ("What is hydrogeology? Give one reason a hydrogeologist is useful in a rural community.",
           "Hydrogeology is the study of groundwater, the water held in soil and rock below the surface. A hydrogeologist can choose a good site and depth for a borehole or well and advise how to protect the water from pollution."),
        PQ("Name two ways in which geology helps the economy of Cameroon.",
           "Any two: finding and assessing mineral resources (gold, bauxite, iron ore, rutile, limestone); finding oil and gas in sedimentary basins; locating groundwater; engineering surveys for roads and dams; warning of hazards such as volcanic eruptions."),
        SUM("Geology is the scientific study of the Earth's materials, structure, processes and history.",
            "Branches include mineralogy (minerals), petrology (rocks), structural geology, stratigraphy, palaeontology, geomorphology, hydrogeology and economic geology.",
            "Hydrogeology is the study of groundwater, not of water in general.",
            "Geologists work in mining, petroleum, water supply, engineering, hazards and teaching.",
            "Cameroon's volcano, old basement rocks, minerals, oil and hazards make geology useful here."),
    ],
))

# ------------------------------------------------------------------ 2. The solar system
LESSONS.append(lesson(
    module=M1, topic="The solar system",
    title="The solar system: origin, planets and meteorites",
    slug="gly1-the-solar-system",
    minutes=20,
    summary="The Sun and planets formed about 4.6 billion years ago from a spinning cloud of gas and dust; rocky planets lie close to the Sun, giant planets far away, and meteorites are fragments from space that reach the ground.",
    objectives=[
        "Describe the nebular hypothesis for the origin of the solar system",
        "Compare terrestrial and giant planets",
        "Define meteoroid, meteor and meteorite and name the three types of meteorite",
        "Explain why meteorites help geologists",
    ],
    key_concepts=["Nebula", "Terrestrial planets", "Giant planets", "Asteroid belt", "Meteorite", "Chondrite"],
    blocks=[
        H("Introduction"),
        T("On a clear night in Garoua or Bertoua, far from city lights, you can see thousands of stars and sometimes a streak of light that lasts a second. "
          "That streak is a tiny piece of rock burning up in the air. Geologists study the solar system because the Earth is a part of it and was formed with it."),
        D("The **solar system** is the Sun and everything that orbits it: eight planets, their moons, the asteroid belt, comets and smaller bodies.", title="Solar system"),
        H("Origin: the nebular hypothesis"),
        T("The most accepted explanation is the **nebular hypothesis**. About 4.6 billion years ago, a huge cloud of gas and dust, called a **nebula**, began to collapse "
          "under its own gravity. Most of the matter fell to the centre and became the Sun. The rest flattened into a spinning disc."),
        T("In the disc, dust grains stuck together into small bodies called planetesimals. These collided and joined to make the planets. "
          "Close to the hot Sun only rock and metal could stay solid, so small rocky planets formed there. Far from the Sun it was cold enough for ice and gas to collect, "
          "so giant planets formed."),
        KEY("Steps of formation", "Remember the order.", cards=[
            ["1. Nebula", "A cloud of gas and dust collapses under gravity."],
            ["2. Sun and disc", "The centre becomes the Sun; the rest spins in a flat disc."],
            ["3. Planetesimals", "Grains and small bodies collide and stick together."],
            ["4. Planets", "Planetesimals grow into planets; the leftovers form asteroids and comets."],
        ]),
        H("The planets"),
        T("Starting from the Sun, the planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune. They fall into two groups."),
        KEY("Two groups of planets", "The groups differ in size, density and composition.", cards=[
            ["Terrestrial (rocky) planets", "Mercury, Venus, Earth, Mars. Small, dense, rocky with metal cores, few or no moons, close to the Sun."],
            ["Giant planets", "Jupiter and Saturn (gas giants) and Uranus and Neptune (ice giants). Large, low density, many moons, far from the Sun."],
        ], note="The asteroid belt lies between Mars and Jupiter."),
        CODE("Planet     Distance from Sun (AU)   Orbit time (Earth years)\n"
             "Mercury    0.39                     0.24\n"
             "Venus      0.72                     0.62\n"
             "Earth      1.00                     1.00\n"
             "Mars       1.52                     1.88\n"
             "Jupiter    5.2                      11.9\n"
             "Saturn     9.6                      29.4\n"
             "Uranus     19.2                     84\n"
             "Neptune    30.1                     165", "text", title="Planets (rounded values)",
             caption="1 AU (astronomical unit) is the average distance from the Earth to the Sun, about 150 million km."),
        T("Notice the pattern: the farther a planet is from the Sun, the longer it takes to go round. The Earth is the only planet known to have liquid water on its surface and life."),
        EX("Worked example 1: a distance",
           intro="Mars is 1.52 AU from the Sun. Taking 1 AU as 150 million km, find the distance in millions of km.",
           steps=[
               S("Multiply", math=r"1.52 \times 150 = 228"),
               S("State the answer with units", text="Mars is about 228 million km from the Sun."),
           ], check=r"228 \div 150 = 1.52"),
        H("Meteorites"),
        D("A **meteoroid** is a small rocky or metallic body moving in space. A **meteor** is the streak of light seen when it burns in the atmosphere. "
          "A **meteorite** is a piece that survives and lands on the ground.", title="Meteoroid, meteor, meteorite"),
        KEY("Three types of meteorite", "They differ in how much rock and metal they hold.", cards=[
            ["Stony", "Mostly silicate minerals, like Earth's mantle rocks. The most common type. Chondrites hold small round grains called chondrules; they are among the oldest solid material."],
            ["Iron", "Mostly iron and nickel alloy. Dense and heavy. Thought to come from the cores of broken-up bodies."],
            ["Stony-iron", "A mix of silicate minerals and iron-nickel metal. The rarest group."],
        ]),
        T("Meteorites matter because they are samples of the early solar system. The oldest give ages of about 4.57 billion years, which is how the age of the Earth is estimated. "
          "Iron meteorites also suggest what the Earth's own core is like, since we cannot sample it."),
        EX("Worked example 2: classify a find",
           intro="A farmer finds a heavy dark stone that is attracted to a magnet and is mostly metal when cut. Which type of meteorite is it likely to be?",
           steps=[
               S("Read the clues", text="Heavy, magnetic and mostly metal."),
               S("Match to a type", text="Iron-nickel metal points to an **iron meteorite**."),
               S("Be careful", text="Many ordinary heavy rocks also look dark; a laboratory test is needed to be sure."),
           ]),
        MISTAKE("Mixing meteor and meteorite",
                "A meteor is the flash of light in the sky. A meteorite is the solid object found on the ground. Both come from the same meteoroid."),
        QUIZ("Which group of planets has small size, high density and a rocky surface?",
             ["Giant planets", "Terrestrial planets", "Ice giants", "Gas giants"], 1,
             "The terrestrial planets (Mercury, Venus, Earth, Mars) are small, dense and rocky.", hint="The word terrestrial comes from the Latin for Earth.",
             feedback=["Giant planets are large with low density.", "", "Ice giants are Uranus and Neptune, which are large.", "Gas giants (Jupiter and Saturn) are large and made mostly of gas."]),
        TIP("Exam link: Paper 1 may ask about the origin of the solar system, planet groups and meteorite types. Paper 2 can ask for a description of how the planets formed. "
            "Use the words nebula, gravity and planetesimals."),
        PQ("Describe briefly how the solar system formed.",
           "About 4.6 billion years ago a nebula of gas and dust collapsed under gravity. Most of the matter formed the Sun at the centre. The rest spun as a flat disc, where grains stuck together into planetesimals that collided and grew into planets, moons and asteroids."),
        PQ("State two differences between terrestrial planets and giant planets.",
           "Terrestrial planets are small, dense and rocky, with few or no moons, and lie near the Sun. Giant planets are large, low in density, made mostly of gas or ice, have many moons and lie far from the Sun."),
        PQ("Distinguish between a meteor and a meteorite, and name the three types of meteorite.",
           "A meteor is the streak of light made when a meteoroid burns up in the atmosphere; a meteorite is a piece that reaches the ground. The three types are stony, iron and stony-iron."),
        SUM("The solar system formed about 4.6 billion years ago from a collapsing nebula of gas and dust (nebular hypothesis).",
            "Terrestrial planets are small, dense and rocky; giant planets are large and made mostly of gas or ice.",
            "The asteroid belt lies between Mars and Jupiter; planets farther from the Sun take longer to orbit.",
            "A meteor is a streak of light; a meteorite is a space rock found on the ground.",
            "Meteorites are stony, iron or stony-iron, and give the age of the solar system and clues about the Earth's core."),
    ],
))

# ------------------------------------------------------------------ 3. Seismic waves and the Earth's interior
LESSONS.append(lesson(
    module=M1, topic="Seismic waves and the Earth's interior",
    title="Seismic waves (P, S and L) and the layers of the Earth",
    slug="gly1-seismic-waves-and-earths-interior",
    minutes=22,
    summary="Earthquakes send P, S and L waves; how these waves speed up, slow down or stop shows that the Earth has a crust, mantle, liquid outer core and solid inner core separated by the Moho, Gutenberg and Lehmann discontinuities.",
    objectives=[
        "Define focus and epicentre and describe P, S and L waves",
        "Explain how seismic waves reveal the layers of the Earth",
        "Describe the crust, mantle, outer core and inner core, and name the discontinuities",
        "Use the S-P time gap to find the distance to an earthquake",
    ],
    key_concepts=["Focus", "Epicentre", "P wave", "S wave", "L wave", "Discontinuity", "Moho", "Shadow zone"],
    blocks=[
        H("Introduction"),
        T("Nobody has been to the centre of the Earth. The deepest hole ever drilled is about 12 km, but the centre is over 6 000 km down. "
          "Geologists learn about the inside by listening to earthquakes. An earthquake is like a bell that rings through the whole planet."),
        D("The **focus** is the point underground where an earthquake starts. The **epicentre** is the point on the surface directly above the focus.", title="Focus and epicentre"),
        H("The three kinds of seismic wave"),
        T("Waves of energy spread from the focus. **Seismographs** record them. There are two kinds of body wave (which travel through the Earth) and surface waves (which travel along the ground)."),
        KEY("P, S and L waves", "Learn the order of arrival: P first, S second, L last.", cards=[
            ["P wave (primary)", "Fastest. A push-pull (compressional) wave that moves the ground back and forth in the direction of travel. Passes through solids, liquids and gases."],
            ["S wave (secondary)", "Slower than P. A shake from side to side (shear wave), at right angles to the direction of travel. Passes through solids only, not through liquids."],
            ["L wave (long or surface wave)", "Slowest. Travels along the surface of the Earth, with the largest movement. Does the most damage to buildings."],
        ]),
        MISTAKE("Saying S waves cannot travel through the Earth",
                "S waves do travel through solid rock. They stop only at liquid. The fact that S waves do not pass through the outer core is the proof that it is liquid."),
        H("Layers of the Earth"),
        IMG("f5gly1-interior.svg", alt="Cross-section of the Earth showing crust, mantle, outer core and inner core with their depths",
            caption="Figure 1. The layers of the Earth (not to scale)."),
        KEY("What each layer is like", "Depths are approximate.", cards=[
            ["Crust", "Thin outer skin, about 5 to 10 km under the oceans and up to about 70 km under big mountain ranges. Continental crust is mainly granite-type rock; oceanic crust is basalt."],
            ["Mantle", "From the base of the crust to about 2 900 km. Hot, dense rock rich in iron and magnesium (peridotite). Solid, but the part below the lithosphere flows slowly."],
            ["Outer core", "From about 2 900 km to 5 150 km. Liquid iron and nickel."],
            ["Inner core", "From about 5 150 km to the centre at about 6 371 km. Solid iron and nickel, kept solid by the huge pressure."],
        ]),
        D("A **discontinuity** is a boundary inside the Earth where seismic waves suddenly change speed. The **Moho** (Mohorovicic discontinuity) lies between the crust and the mantle. "
          "The **Gutenberg discontinuity** lies between the mantle and the outer core at about 2 900 km. The **Lehmann discontinuity** lies between the outer core and the inner core at about 5 150 km.",
          title="Discontinuities"),
        T("The **lithosphere** is the crust plus the rigid top of the mantle. Under it is the **asthenosphere**, a weak, partly flowing zone. This is what allows plates to move (next lesson)."),
        H("How the waves show the layers"),
        T("When waves meet a boundary between materials, they change speed and bend. At the Moho, waves speed up, so the mantle is denser and different from the crust. "
          "At the Gutenberg discontinuity, P waves slow down and bend, and S waves stop completely. This is why we conclude that the outer core is liquid."),
        T("Because of the bending and stopping, there are regions on the far side of the Earth where some waves are not recorded. These are called **shadow zones**. "
          "The S-wave shadow covers the whole far side of the Earth, which shows that a liquid layer lies inside."),
        EX("Worked example 1: what do the waves show?",
           intro="Seismographs on the opposite side of the Earth from an earthquake record P waves but no S waves. What does this show?",
           steps=[
               S("Recall what stops S waves", text="S waves cannot travel through liquids."),
               S("Apply", text="Their waves must have crossed a liquid part of the Earth on the way."),
               S("Conclusion", text="Part of the Earth's core is liquid: the **outer core**."),
           ]),
        H("Finding the distance to an earthquake"),
        T("P waves arrive before S waves. The bigger the gap between them, the farther away the earthquake. A seismologist uses the gap, called the **S-P time lag**, to find the distance. "
          "(The speeds below are invented for practice; real speeds change with the rock.)"),
        F(r"d = \dfrac{t}{\dfrac{1}{v_S} - \dfrac{1}{v_P}}", title="Distance from the S-P time lag"),
        EX("Worked example 2: distance from the lag",
           intro="In a practice problem P waves travel at 6 km/s and S waves at 3.5 km/s. The S wave arrives 25 seconds after the P wave. How far away is the focus?",
           steps=[
               S("Write the time for each wave over distance d", math=r"t_P = \dfrac{d}{6}, \quad t_S = \dfrac{d}{3.5}"),
               S("The lag is the difference", math=r"25 = \dfrac{d}{3.5} - \dfrac{d}{6}"),
               S("Combine", math=r"\dfrac{1}{3.5} - \dfrac{1}{6} = \dfrac{5}{42}, \text{ so } 25 = \dfrac{5d}{42}"),
               S("Solve", math=r"d = 25 \times \dfrac{42}{5} = 210 \text{ km}"),
           ], check=r"\dfrac{210}{3.5} - \dfrac{210}{6} = 60 - 35 = 25"),
        QUIZ("Which wave arrives last and causes most damage to buildings?", ["P wave", "S wave", "L wave", "Body wave"], 2,
             "L (surface) waves are slowest, so they arrive last, and have the biggest ground movement.", hint="The long waves travel along the ground surface.",
             feedback=["P waves arrive first.", "S waves arrive second.", "", "Body waves include P and S, which arrive earlier."]),
        QUIZ("The Gutenberg discontinuity separates", ["the crust and the mantle", "the mantle and the outer core", "the outer core and the inner core", "the lithosphere and the crust"], 1,
             "It lies at about 2 900 km, between the mantle and the liquid outer core.", hint="It is at 2 900 km.",
             feedback=["That is the Moho.", "", "That is the Lehmann discontinuity.", "The lithosphere includes the crust; it is not a boundary of that kind."]),
        TIP("Exam link: Paper 1 often asks which wave goes through liquids, the order of arrival and the layer depths. Paper 2 may ask you to label a section of the Earth and "
            "explain how seismic waves give evidence for a liquid outer core. Give both observations: S waves stop, P waves slow and bend."),
        PQ("Distinguish between the focus and the epicentre of an earthquake.",
           "The focus is the point underground where the earthquake starts; the epicentre is the point on the surface directly above the focus."),
        PQ("State two differences between P waves and S waves.",
           "P waves are faster and travel through solids, liquids and gases; they are compressional. S waves are slower, travel through solids only and are shear waves (side-to-side motion)."),
        PQ("Explain how seismic waves show that the outer core of the Earth is liquid.",
           "S waves stop at the boundary between the mantle and the outer core (about 2 900 km) and are not recorded on the far side of the Earth, which means the outer core cannot be solid. P waves also slow down and bend as they enter it, creating a shadow zone."),
        SUM("Seismic waves start at the focus; the epicentre is the surface point above it.",
            "P waves are fastest and pass through solids and liquids; S waves pass through solids only; L waves are slowest and most damaging.",
            "The Earth has a crust, mantle, liquid outer core and solid inner core.",
            "The Moho, Gutenberg and Lehmann discontinuities mark the main boundaries.",
            "The S-P lag gives the distance to the earthquake."),
    ],
))

# ------------------------------------------------------------------ 4. Plate tectonics
LESSONS.append(lesson(
    module=M1, topic="Plate tectonics",
    title="Continental drift, seafloor spreading and plate tectonics",
    slug="gly1-plate-tectonics",
    minutes=24,
    summary="Wegener proposed continental drift from evidence such as the fit of Africa and South America; seafloor spreading supplied the mechanism, and plate tectonics explains plate boundaries, earthquakes and volcanoes.",
    objectives=[
        "State the evidence for continental drift",
        "Explain seafloor spreading and its evidence",
        "Describe divergent, convergent and transform boundaries with examples",
        "Calculate simple plate movement from a rate and a time",
    ],
    key_concepts=["Continental drift", "Seafloor spreading", "Mid-ocean ridge", "Plate", "Divergent", "Convergent", "Subduction", "Transform"],
    blocks=[
        H("Introduction"),
        T("Look at a world map. The west coast of Africa, including the Cameroon coast on the Gulf of Guinea, looks like it could fit into the east coast of South America. "
          "That is not a coincidence. The two continents were once joined and have drifted apart."),
        H("Continental drift"),
        D("**Continental drift** is the idea, put forward by the German scientist Alfred Wegener in 1912, that the continents were once joined in one supercontinent (**Pangaea**) "
          "and have slowly moved apart.", title="Continental drift"),
        KEY("Wegener's evidence", "Each clue points to former joining.", cards=[
            ["Fit of the coasts", "Africa and South America fit together like pieces of a jigsaw, especially at the edge of the continental shelf."],
            ["Fossils", "The same fossils (such as the reptile Mesosaurus and the plant Glossopteris) occur on continents now far apart."],
            ["Rocks and mountains", "Rock types and mountain belts match across the Atlantic."],
            ["Climate", "Glacial deposits are found in warm places such as Africa and India today."],
        ]),
        T("Most scientists rejected the idea at first because Wegener could not explain how continents could plough through solid ocean floor. He had no mechanism."),
        H("Seafloor spreading"),
        T("In the 1950s and 1960s, studies of the ocean floor supplied the missing mechanism. Long underwater mountain chains called **mid-ocean ridges** run through the oceans, "
          "such as the Mid-Atlantic Ridge. Hot mantle rock rises under the ridge, melts, and forms new basalt crust."),
        D("**Seafloor spreading** is the process in which new oceanic crust forms at mid-ocean ridges and the sea floor moves slowly away from the ridge on both sides.", title="Seafloor spreading"),
        KEY("Evidence for seafloor spreading", "The ocean floor is young, and its pattern is symmetrical.", cards=[
            ["Age of rocks", "Rocks are youngest at the ridge and get older with distance from it. The oldest ocean floor is far younger than the oldest continents."],
            ["Magnetic stripes", "Basalt records the Earth's magnetic field as it cools. Stripes of normal and reversed magnetism are matching on each side of the ridge."],
            ["Sediment thickness", "Sediment is thin or missing at the ridge and gets thicker away from it."],
        ]),
        H("Plate tectonics"),
        D("**Plate tectonics** is the theory that the lithosphere is broken into rigid **plates** that move slowly over the weaker asthenosphere, "
          "carrying continents and oceans with them. Plates move a few centimetres a year.", title="Plate tectonics"),
        T("Plates move because of heat flow in the mantle (convection currents), the push of new crust at ridges (ridge push) and the pull of sinking plate edges (slab pull). "
          "Most earthquakes and volcanoes occur along plate boundaries."),
        IMG("f5gly1-boundaries.svg", alt="Three cross-sections showing plates moving apart at a divergent boundary, together at a convergent boundary and past each other at a transform boundary",
            caption="Figure 1. The three kinds of plate boundary (schematic)."),
        KEY("Three kinds of boundary", "Name them by the plate movement.", cards=[
            ["Divergent (constructive)", "Plates move apart; magma rises; new crust forms. Examples: Mid-Atlantic Ridge, the East African Rift."],
            ["Convergent (destructive)", "Plates move together. A dense oceanic plate sinks under another plate (subduction), forming a trench, volcanoes and strong earthquakes. Examples: the Andes (ocean-continent), Japan and the Mariana Islands (ocean-ocean). When two continents collide there is no subduction and fold mountains form, as in the Himalayas."],
            ["Transform (conservative)", "Plates slide past each other; crust is neither made nor destroyed. Strong earthquakes occur. Example: the San Andreas Fault in California."],
        ]),
        T("Cameroon lies inside the African plate, far from its edges, so it has few big earthquakes. The Atlantic Ocean opened between Africa and South America more than 100 million years ago. "
          "The Cameroon Volcanic Line is not on a plate boundary, and its exact cause is still debated by geologists."),
        EX("Worked example 1: how wide could the ocean grow?",
           intro="Two plates move apart at a total rate of 2.5 cm per year. How wide is the new ocean after 10 million years?",
           steps=[
               S("Multiply rate by time", math=r"2.5 \times 10\,000\,000 = 25\,000\,000 \text{ cm}"),
               S("Convert to kilometres", math=r"25\,000\,000 \text{ cm} = 250 \text{ km}"),
               S("Answer", text="About 250 km of new ocean has opened."),
           ]),
        EX("Worked example 2: classify the boundary",
           intro="A boundary has a deep ocean trench, a chain of volcanoes on the continent beside it and strong earthquakes. Name the boundary type and the process.",
           steps=[
               S("Trench and volcanoes", text="These form where one plate sinks beneath another."),
               S("Name it", text="A **convergent** boundary, with **subduction** of the oceanic plate beneath the continental plate."),
           ]),
        MISTAKE("Thinking the continents plough through the oceans",
                "Continents do not move alone. They are carried on plates that include ocean floor, and the plates move over the asthenosphere. "
                "That is why Wegener's idea was improved into plate tectonics."),
        QUIZ("New oceanic crust forms at", ["a trench", "a transform fault", "a mid-ocean ridge", "a fold mountain"], 2,
             "Magma rises and cools at the mid-ocean ridge, a divergent boundary.", hint="Think about where plates move apart.",
             feedback=["At a trench, oceanic crust is destroyed by subduction.", "At a transform fault, plates slide past each other.", "", "Fold mountains form where continents collide."]),
        TIP("Exam link: Paper 1 asks for evidence, boundary types and examples. Paper 2 may ask for labelled diagrams of the three boundaries. Draw arrows to show the movement and "
            "name one example of each type."),
        PQ("State three pieces of evidence that support the idea of continental drift.",
           "Any three: the matching fit of the coasts of Africa and South America; the same fossils on different continents (Mesosaurus, Glossopteris); matching rocks and mountain belts; glacial deposits in warm regions today."),
        PQ("Describe the evidence for seafloor spreading.",
           "Ocean-floor rocks are youngest at the mid-ocean ridge and older farther away; the magnetic stripes on each side of the ridge are symmetrical; sediment is thin at the ridge and thicker away from it."),
        PQ("Compare divergent and convergent plate boundaries, with one example of each.",
           "At a divergent boundary plates move apart and new crust forms, for example the Mid-Atlantic Ridge. At a convergent boundary plates move together and crust is destroyed by subduction or folded in a collision, for example the Andes or the Himalayas."),
        SUM("Wegener proposed continental drift from evidence such as fit, fossils, rocks and climate, but had no mechanism.",
            "Seafloor spreading: new crust forms at mid-ocean ridges; ocean floor is youngest at the ridge and shows magnetic stripes.",
            "Plate tectonics: the lithosphere is broken into plates that move over the asthenosphere.",
            "Boundaries: divergent (apart), convergent (together, subduction), transform (past each other).",
            "Cameroon lies inside the African plate; the Cameroon Volcanic Line is not on a plate boundary."),
    ],
))

# ------------------------------------------------------------------ 5. Crystals and symmetry
LESSONS.append(lesson(
    module=M2, topic="Crystals and symmetry",
    title="Crystal faces, interfacial angles and symmetry",
    slug="gly1-crystals-and-symmetry",
    minutes=24,
    summary="A crystal has flat faces, edges and corners; the angle between two faces of the same mineral is always the same (interfacial angle), and symmetry is described by planes (surfaces), axes (lines) and a centre (point).",
    objectives=[
        "Define crystal, face, edge and interfacial angle",
        "State the law of constancy of interfacial angles",
        "Distinguish plane, axis and centre of symmetry",
        "Count the symmetry elements of a cube",
    ],
    key_concepts=["Crystal", "Face", "Edge", "Interfacial angle", "Plane of symmetry", "Axis of symmetry", "Centre of symmetry"],
    blocks=[
        H("Introduction"),
        T("Table salt, which is the mineral halite, forms tiny cubes. Under a hand lens you can see every grain is a small cube with flat, shiny faces. "
          "The shape is not an accident. It shows how the atoms inside are arranged. Crystallography is the study of such shapes."),
        D("A **crystal** is a solid with its atoms arranged in a regular, repeating pattern, often bounded by flat natural surfaces.", title="Crystal"),
        KEY("Parts of a crystal", "Three words to describe the outside.", cards=[
            ["Face", "A flat surface that bounds the crystal."],
            ["Edge", "The line where two faces meet."],
            ["Corner (solid angle)", "The point where three or more faces and edges meet."],
        ]),
        T("A cube has 6 faces, 12 edges and 8 corners. There is a simple check called Euler's rule: faces plus corners equals edges plus 2. For the cube, 6 + 8 = 14 and 12 + 2 = 14."),
        H("Interfacial angles"),
        D("The **interfacial angle** is the angle between the normals (lines at right angles) to two faces of a crystal. "
          "For two faces meeting at an edge, it equals 180 degrees minus the inside angle between the faces.", title="Interfacial angle"),
        IMG("f5gly1-interfacial.svg", alt="Edge-on view of two crystal faces with a normal drawn to each; the interfacial angle is between the normals",
            caption="Figure 1. The interfacial angle is measured between the normals to two faces."),
        T("Textbooks differ: some measure the angle between the faces themselves (the inside angle). In this course we use the angle between the normals, and a cube's interfacial angle is 90 degrees either way. "
          "**Check which your textbook uses.** A contact goniometer (an angle-measuring instrument) is used to measure it."),
        KEY("Law of constancy of interfacial angles", "Steno's law (1669).", cards=[
            ["The law", "The angle between corresponding faces of crystals of the same mineral is always the same, measured at the same temperature."],
            ["What it means", "Crystals may be large or small, perfect or distorted, but the angles stay the same. Different minerals have different angles."],
        ]),
        EX("Worked example 1: interfacial angle of a hexagonal prism",
           intro="Quartz often forms six-sided prisms. The six side faces are equal and meet at inside angles of 120 degrees. Find the interfacial angle between neighbouring faces.",
           steps=[
               S("Use the rule", math=r"\text{interfacial angle} = 180^\circ - \text{inside angle}"),
               S("Substitute", math=r"180^\circ - 120^\circ = 60^\circ"),
               S("Check with the six faces", math=r"360^\circ \div 6 = 60^\circ"),
           ]),
        H("Symmetry"),
        T("A crystal shows **symmetry** when parts of it repeat. We describe it with three elements of symmetry. The Board's report says many candidates confuse them: "
          "a plane is a **surface**, an axis is a **line**, and a centre is a **point**."),
        IMG("f5gly1-symmetry.svg", alt="A cube with a shaded plane of symmetry through its middle and a dashed four-fold axis through two opposite faces",
            caption="Figure 2. One plane and one axis of a cube."),
        KEY("Elements of symmetry", "Plane, axis, centre.", cards=[
            ["Plane of symmetry", "An imaginary flat surface that cuts the crystal into two halves; one half is the mirror image of the other."],
            ["Axis of symmetry", "An imaginary line through the crystal; when the crystal turns one full turn (360 degrees) about it, it looks the same more than once. A 2-fold axis (diad) repeats twice, 3-fold (triad) three times, 4-fold (tetrad) four times, 6-fold (hexad) six times."],
            ["Centre of symmetry", "An imaginary point such that every face has an equal, parallel face on the opposite side."],
        ]),
        EX("Worked example 2: symmetry of a cube",
           intro="Count the planes and axes of symmetry of a cube.",
           steps=[
               S("Planes", text="3 planes parallel to pairs of faces, plus 6 planes along diagonals through opposite edges: **9 planes**."),
               S("Axes", text="3 tetrads (through the centres of opposite faces), 4 triads (through opposite corners) and 6 diads (through the midpoints of opposite edges): **13 axes**."),
               S("Centre", text="**1 centre** (the middle of the cube)."),
               S("Total", math=r"9 + 13 + 1 = 23 \text{ elements of symmetry}"),
           ]),
        MISTAKE("Calling a plane a line and an axis a point",
                "A plane of symmetry is a surface (a mirror). An axis of symmetry is a line about which the crystal is rotated. A centre of symmetry is the point. "
                "Say the right word for each and say what it does."),
        QUIZ("An axis of symmetry is", ["an imaginary surface that divides the crystal into mirror-image halves", "an imaginary line about which the crystal can be rotated", "an imaginary point in the middle of the crystal", "the edge where two faces meet"], 1,
             "An axis is a line. Rotating through 360 degrees about it, the crystal shows the same appearance more than once.", hint="Which of these is a line?",
             feedback=["That is a plane of symmetry.", "", "That is a centre of symmetry.", "That is an edge, not an element of symmetry."]),
        QUIZ("Two crystals of quartz, one large and one small, are measured. Their interfacial angles will be", ["different, because they have different sizes", "the same, according to the law of constancy of interfacial angles", "different, because one is older", "impossible to measure"], 1,
             "Corresponding interfacial angles of one mineral are constant.", hint="Size does not change the angle.",
             feedback=["Size does not change the angles.", "", "Age does not change the angles.", "A goniometer can measure them."]),
        TIP("Exam link: Paper 1 asks for definitions and for counting faces or symmetry elements. Paper 2 asks you to define terms and to distinguish a plane from an axis of symmetry. "
            "Always say plane = surface, axis = line."),
        PQ("Define (a) face, (b) edge and (c) interfacial angle of a crystal.",
           "(a) A face is a flat surface bounding a crystal. (b) An edge is the line where two faces meet. (c) The interfacial angle is the angle between the normals to two faces."),
        PQ("Distinguish between a plane of symmetry and an axis of symmetry.",
           "A plane of symmetry is an imaginary surface dividing a crystal into two halves, one the mirror image of the other. An axis of symmetry is an imaginary line about which the crystal rotated through 360 degrees shows the same face more than once."),
        PQ("Find the interfacial angle between neighbouring side faces of a regular six-sided prism.",
           "Inside angle 120 degrees, so the interfacial angle is 180 - 120 = 60 degrees."),
        SUM("A crystal is bounded by faces, edges and corners; the cube has 6 faces, 12 edges and 8 corners.",
            "The interfacial angle is the angle between the normals to two faces; it is constant for a mineral (Steno's law).",
            "A plane of symmetry is a surface; an axis is a line; a centre is a point.",
            "A cube has 9 planes, 13 axes and 1 centre of symmetry."),
    ],
))

# ------------------------------------------------------------------ 6. The six crystal systems
LESSONS.append(lesson(
    module=M2, topic="The six crystal systems",
    title="The six crystal systems and their axes",
    slug="gly1-six-crystal-systems",
    minutes=22,
    summary="Crystals are grouped into six systems (cubic, tetragonal, orthorhombic, monoclinic, triclinic, hexagonal) by the lengths of their crystal axes and the angles between them; each mineral belongs to one system.",
    objectives=[
        "Describe crystal axes and how they are used to classify crystals",
        "State the axial lengths and angles of the six systems",
        "Give common mineral examples of each system",
        "Identify the system from axial data",
    ],
    key_concepts=["Crystal axes", "Cubic", "Tetragonal", "Orthorhombic", "Monoclinic", "Triclinic", "Hexagonal"],
    blocks=[
        H("Introduction"),
        T("Halite forms cubes, quartz forms six-sided prisms with pointed tops, and gypsum forms flat blade-like crystals. These shapes are different because the internal "
          "arrangement of atoms is different. Geologists put crystals into groups called crystal systems."),
        D("**Crystal axes** are imaginary lines through the centre of a crystal, used as a frame of reference. Crystals are classified into systems by the **lengths** "
          "of the axes (called a, b and c) and the **angles** between them.", title="Crystal axes"),
        T("Three axes are used for most systems: a, b and c. The angles between them are alpha (between b and c), beta (between a and c) and gamma (between a and b). "
          "The hexagonal system uses four axes, with three equal axes in one plane at 120 degrees to each other, and one axis at right angles."),
        KEY("The six systems", "A comparison you must know.", cards=[
            ["Cubic (isometric)", "Three axes of equal length at 90 degrees to each other. Examples: halite, galena, pyrite, fluorite, garnet."],
            ["Tetragonal", "Two axes equal and the third (c) different; all at 90 degrees. Examples: zircon, rutile, cassiterite."],
            ["Orthorhombic", "Three axes of different lengths, all at 90 degrees. Examples: olivine, topaz, barite, sulphur."],
            ["Monoclinic", "Three axes of different lengths; two angles 90 degrees and one (beta) not 90 degrees. Examples: gypsum, orthoclase feldspar, mica, augite."],
            ["Triclinic", "Three axes of different lengths and no angle is 90 degrees. Examples: plagioclase feldspar, kyanite, microcline."],
            ["Hexagonal", "Three equal axes at 120 degrees in one plane and a fourth axis of a different length at right angles to them. Examples: quartz, calcite, beryl, hematite."],
        ], note="Many textbooks list seven systems by treating the trigonal system (quartz, calcite) separately from the hexagonal. We follow the six-system scheme: check your textbook."),
        CODE("System         Axial lengths    Axial angles\n"
             "Cubic          a = b = c        90, 90, 90\n"
             "Tetragonal     a = b, c differs 90, 90, 90\n"
             "Orthorhombic   a, b, c differ   90, 90, 90\n"
             "Monoclinic     a, b, c differ   90, 90, beta (not 90)\n"
             "Triclinic      a, b, c differ   none is 90\n"
             "Hexagonal      a1 = a2 = a3, c  90 to c; 120 between the a axes",
             "text", title="Summary table"),
        T("Rutile, the titanium mineral that Cameroon is known for, is tetragonal. Quartz, the most common mineral in sand and many granites, is in the hexagonal system. "
          "Halite, the mineral in table salt, is cubic."),
        H("Using the table"),
        EX("Worked example 1: classify from the axes",
           intro="A mineral has three axes of different lengths. Two angles are 90 degrees and the third is 105 degrees. Name the system.",
           steps=[
               S("Compare the lengths", text="The three axes are all different, so it is not cubic or tetragonal."),
               S("Compare the angles", text="Only two angles are 90 degrees, so it is not orthorhombic (three at 90) or triclinic (none at 90)."),
               S("Name it", text="It is **monoclinic**."),
           ]),
        EX("Worked example 2: classify from the data",
           intro="A crystal has a = b = 4.6 units and c = 2.95 units, with all angles 90 degrees. Which system is it, and give one example mineral.",
           steps=[
               S("Compare the lengths", text="Two axes are equal and the third is different (4.6, 4.6 and 2.95)."),
               S("Compare the angles", text="All are 90 degrees."),
               S("Name it", text="**Tetragonal**. Rutile and cassiterite are examples."),
           ]),
        MISTAKE("Mixing up cubic and tetragonal",
                "Both have all angles at 90 degrees. In the cubic system all three axes are equal. In the tetragonal system only two are equal and the third is different (longer or shorter)."),
        MISTAKE("Thinking the shape alone gives the system",
                "A crystal may be distorted by growth, but the angles between its faces stay constant. Use the axes and the interfacial angles, not just the outline."),
        QUIZ("A mineral has three unequal axes, all at 90 degrees. The system is", ["cubic", "tetragonal", "orthorhombic", "monoclinic"], 2,
             "Unequal axes at right angles is the orthorhombic system.", hint="Count how many axes are equal.",
             feedback=["Cubic needs three equal axes.", "Tetragonal needs two equal axes.", "", "Monoclinic has one angle that is not 90 degrees."]),
        QUIZ("Which mineral crystallises in the cubic system?", ["Quartz", "Gypsum", "Halite", "Plagioclase"], 2,
             "Halite forms cubes.", hint="Think of table salt.",
             feedback=["Quartz is hexagonal.", "Gypsum is monoclinic.", "", "Plagioclase feldspar is triclinic."]),
        TIP("Exam link: Paper 1 asks you to match systems with axial data or with example minerals. Paper 2 can ask you to describe the crystal systems in a table. "
            "Learn the table above, with one mineral for each system."),
        PQ("State the axial lengths and angles of the tetragonal system, with one example mineral.",
           "Two axes equal and the third different (a = b, c differs); all three angles are 90 degrees. Example: rutile (or zircon, cassiterite)."),
        PQ("Distinguish between the monoclinic and triclinic systems.",
           "In the monoclinic system two angles are 90 degrees and one is not. In the triclinic system none of the angles is 90 degrees. In both, the three axes have different lengths."),
        PQ("Name the crystal system of each mineral: halite, quartz, olivine, gypsum.",
           "Halite: cubic. Quartz: hexagonal (trigonal). Olivine: orthorhombic. Gypsum: monoclinic."),
        SUM("Crystal axes (a, b, c) and the angles between them are used to classify crystals.",
            "Cubic: equal axes, 90 degrees. Tetragonal: a = b, c differs, 90 degrees. Orthorhombic: unequal axes, 90 degrees.",
            "Monoclinic: unequal axes, one angle not 90. Triclinic: unequal axes, no angle 90. Hexagonal: three equal axes at 120 degrees and a fourth.",
            "Examples: halite (cubic), rutile (tetragonal), olivine (orthorhombic), gypsum (monoclinic), plagioclase (triclinic), quartz (hexagonal)."),
    ],
))

# ------------------------------------------------------------------ 7. Physical properties of minerals
LESSONS.append(lesson(
    module=M2, topic="Physical properties of minerals",
    title="Identifying minerals: colour, streak, lustre, cleavage, hardness and density",
    slug="gly1-physical-properties-of-minerals",
    minutes=25,
    summary="Minerals are identified by colour, streak (colour of the powder), lustre, cleavage, fracture, Mohs hardness and specific gravity; hardness and specific gravity can be measured, and specific gravity is weight in air divided by loss of weight in water.",
    objectives=[
        "Define colour, streak, lustre, cleavage and fracture precisely",
        "Use the Mohs scale and simple tools to find hardness",
        "Calculate specific gravity from weights in air and in water",
        "Identify a mineral from a set of properties",
    ],
    key_concepts=["Colour", "Streak", "Lustre", "Cleavage", "Fracture", "Mohs hardness", "Specific gravity"],
    blocks=[
        H("Introduction"),
        T("A trader at a mining site in the East Region shows you a shiny yellow stone and says it is gold. How can you tell if it is gold or a cheaper mineral? "
          "You cannot rely on colour alone. Geologists use a set of physical properties that can be tested with simple tools."),
        D("A **mineral** is a naturally occurring, solid, inorganic substance with a definite chemical composition and an ordered atomic structure.", title="Mineral"),
        H("Appearance properties"),
        KEY("Colour, streak and lustre", "The Board's report says candidates often define these wrongly.", cards=[
            ["Colour", "The colour of the mineral as you see it. It can vary for the same mineral (quartz can be clear, white, purple or smoky), so it is not always reliable."],
            ["Streak", "The **colour of the powder** of a mineral, seen when it is rubbed on an unglazed porcelain streak plate. It is more reliable than colour. Hematite is often grey-black but its streak is red-brown. Minerals harder than the plate (about 6.5) leave no streak."],
            ["Lustre", "The **appearance of a mineral in reflected light**. Types: metallic (pyrite, galena), vitreous or glassy (quartz), pearly, silky (some gypsum), resinous, greasy, dull or earthy."],
        ]),
        MISTAKE("Defining streak as the powder, or lustre as colour",
                "Streak is the **colour** of the powder, not the powder itself. Lustre is how the mineral shines in reflected light, not its colour."),
        H("Breaking properties"),
        D("**Cleavage** is the tendency of a mineral to break along flat, smooth surfaces called cleavage planes, which are planes of weak bonding in the atomic structure.", title="Cleavage"),
        D("**Fracture** is the nature of the surface of a freshly broken mineral where it breaks irregularly and not along cleavage planes. Types: conchoidal (smooth curved, like broken glass: quartz), "
          "uneven or irregular, hackly (jagged), fibrous.", title="Fracture"),
        CODE("Mineral    Cleavage\n"
             "Mica       1 direction (thin flexible sheets)\n"
             "Feldspar   2 directions at about 90 degrees\n"
             "Halite     3 directions at 90 degrees (cubes)\n"
             "Calcite    3 directions not at 90 degrees (rhombs)\n"
             "Fluorite   4 directions (octahedra)\n"
             "Quartz     none (conchoidal fracture)", "text", title="Examples of cleavage"),
        H("Hardness"),
        D("**Hardness** is the resistance of a mineral to scratching. It is measured on the **Mohs scale**, a list of ten reference minerals from 1 (softest) to 10 (hardest). "
          "It is a scale of order, not equal steps.", title="Mohs hardness"),
        CODE("1 Talc        6 Orthoclase feldspar\n"
             "2 Gypsum      7 Quartz\n"
             "3 Calcite     8 Topaz\n"
             "4 Fluorite    9 Corundum\n"
             "5 Apatite    10 Diamond", "text", title="Mohs scale"),
        T("Simple tools: a fingernail has hardness about 2.5, a copper coin about 3, a steel nail or knife about 5.5 and a glass plate about 5.5. "
          "A mineral that scratches glass but is scratched by quartz has hardness between 5.5 and 7."),
        H("Specific gravity"),
        D("**Specific gravity (SG)** is the density of a mineral divided by the density of water. It has no unit. It shows how heavy a mineral is for its size. "
          "Water has an SG of 1.", title="Specific gravity"),
        F(r"SG = \dfrac{W_a}{W_a - W_w}", title="From two weighings"),
        T("Here $W_a$ is the weight of the mineral in air and $W_w$ is its weight when hung in water. The loss of weight in water equals the weight of the water displaced (Archimedes' principle)."),
        EX("Worked example 1: find the specific gravity",
           intro="A mineral weighs 53.0 g in air and 33.0 g in water. Find its specific gravity and say which mineral it could be (quartz is about 2.65, galena about 7.5).",
           steps=[
               S("Find the loss of weight in water", math=r"53.0 - 33.0 = 20.0 \text{ g}"),
               S("Divide", math=r"SG = \dfrac{53.0}{20.0} = 2.65"),
               S("Identify", text="An SG of 2.65 matches **quartz**."),
           ], check=r"20.0 \times 2.65 = 53.0"),
        EX("Worked example 2: identify from properties",
           intro="A mineral is brassy yellow with a metallic lustre, hardness 6 to 6.5 (it scratches glass but not quartz), black streak and no cleavage. Which is it: pyrite, gold or chalcopyrite?",
           steps=[
               S("Test hardness", text="Gold is soft (2.5 to 3); a mineral that scratches glass is not gold."),
               S("Use streak", text="Pyrite gives a greenish-black to black streak. Gold gives a golden-yellow streak."),
               S("Conclude", text="The mineral is **pyrite**, often called fool's gold."),
           ]),
        QUIZ("The colour of a mineral's powder is its", ["lustre", "streak", "cleavage", "fracture"], 1,
             "Streak is the colour of the powder.", hint="It is found with a porcelain plate.",
             feedback=["Lustre is the appearance in reflected light.", "", "Cleavage is breaking along flat planes.", "Fracture is the nature of a freshly broken surface."]),
        QUIZ("A mineral weighs 75 g in air and 65 g in water. Its specific gravity is", ["0.13", "1.15", "7.5", "6.5"], 2,
             "Loss of weight = 10 g, so SG = 75 divided by 10 = 7.5 (like galena).", hint="First find the loss of weight in water.",
             feedback=["That is 10 divided by 75, upside down.", "That is 75 divided by 65, which forgets the loss of weight.", "", "That uses the weight in water, not the loss."]),
        TIP("Exam link: Paper 1 asks for Mohs scale order, definitions and simple SG items. Paper 2 may ask you to define streak, fracture and lustre exactly. "
            "Use the exact wording: streak is a colour, fracture is the nature of a broken surface, lustre is the appearance in reflected light."),
        PQ("Define (a) streak, (b) lustre and (c) fracture.",
           "(a) Streak is the colour of the powder of a mineral. (b) Lustre is the appearance of a mineral in reflected light. (c) Fracture is the nature of the surface of a freshly broken mineral."),
        PQ("Distinguish between cleavage and fracture.",
           "Cleavage is breaking along flat, smooth planes of weak bonding; a mineral may have one or more directions. Fracture is an irregular break not along such planes, such as the curved conchoidal fracture of quartz."),
        PQ("A mineral weighs 63.0 g in air and 43.0 g in water. Find its specific gravity.",
           "Loss of weight in water = 63.0 - 43.0 = 20.0 g. SG = 63.0 divided by 20.0 = 3.15."),
        SUM("Colour varies; streak (colour of the powder), lustre (appearance in reflected light), cleavage and fracture help identify a mineral.",
            "Hardness uses the Mohs scale from 1 (talc) to 10 (diamond): fingernail about 2.5, copper coin about 3, steel nail about 5.5.",
            "Specific gravity = weight in air divided by the loss of weight in water; it has no unit.",
            "Always use several properties, not colour alone."),
    ],
))

# ------------------------------------------------------------------ 8. Rock-forming minerals
LESSONS.append(lesson(
    module=M2, topic="Rock-forming minerals",
    title="Rock-forming silicate and non-silicate minerals",
    slug="gly1-rock-forming-minerals",
    minutes=22,
    summary="Most rocks are made of a few silicate minerals (quartz, feldspars, micas, amphiboles, pyroxenes, olivine) built from silica tetrahedra, plus non-silicates such as calcite, hematite, pyrite, gypsum and halite.",
    objectives=[
        "Name the most common elements and minerals of the crust",
        "Describe the silica tetrahedron and the main silicate groups",
        "Name the main non-silicate groups with examples and formulae",
        "Distinguish felsic from ferromagnesian minerals",
    ],
    key_concepts=["Silicate", "Silica tetrahedron", "Feldspar", "Quartz", "Mica", "Carbonate", "Sulphide", "Oxide"],
    blocks=[
        H("Introduction"),
        T("Most of the sand on the beaches at Limbe and Kribi is made of quartz. The grey and pink granite blocks used in buildings are made of quartz, feldspar and mica. "
          "Of the thousands of known minerals, only a few dozen make up most rocks. These are the rock-forming minerals."),
        T("Eight elements make up most of the Earth's crust. Oxygen is the most abundant (nearly half by weight), then silicon (over a quarter), then aluminium, iron, calcium, sodium, potassium and magnesium. "
          "Because oxygen and silicon are so common, the commonest minerals are **silicates**."),
        D("A **silicate** is a mineral that contains silicon and oxygen. Its building block is the **silica tetrahedron**: one silicon atom joined to four oxygen atoms, in the shape of a pyramid with four faces.", title="Silicates"),
        H("The silicate groups"),
        T("The tetrahedra join to each other in different ways. The way they join controls the cleavage and the properties of the mineral."),
        KEY("Main silicate minerals", "Learn one point about each.", cards=[
            ["Olivine", "Single tetrahedra. Olive-green, glassy, no cleavage. Found in basic and ultrabasic rocks such as basalt and peridotite."],
            ["Pyroxene (augite)", "Single chains. Dark green to black; two cleavages at about 90 degrees. In basalt and gabbro."],
            ["Amphibole (hornblende)", "Double chains. Dark; two cleavages at about 56 and 124 degrees. In granite, diorite and metamorphic rocks."],
            ["Mica (muscovite, biotite)", "Sheets. One perfect cleavage, so it splits into thin flexible flakes. Muscovite is pale; biotite is dark brown to black."],
            ["Feldspars", "Frameworks. The most abundant group in the crust. Hardness about 6, two cleavages at about 90 degrees. Orthoclase contains potassium; plagioclase contains sodium and/or calcium."],
            ["Quartz", "A framework of silicon and oxygen only (SiO2). Hardness 7, no cleavage, conchoidal fracture, glassy lustre. Very resistant to weathering, so it is the main mineral in sand."],
        ]),
        T("Silicates are also grouped by colour. **Felsic** (light-coloured) minerals are rich in silica, feldspar and quartz. **Ferromagnesian** (dark) minerals are rich in iron and magnesium: olivine, pyroxene, amphibole and biotite."),
        H("Non-silicate minerals"),
        T("Non-silicates are grouped by the negative part of the formula. Learn one example and its formula for each group."),
        KEY("Common non-silicate groups", "Name, formula and where it is found.", cards=[
            ["Carbonates", "Calcite, CaCO3: the main mineral of limestone and marble. Fizzes in dilute hydrochloric acid. Dolomite is CaMg(CO3)2."],
            ["Oxides", "Hematite, Fe2O3 (iron ore); magnetite, Fe3O4 (iron ore, magnetic); rutile, TiO2 (titanium ore). Bauxite, the aluminium ore, is a mixture of aluminium hydroxide minerals."],
            ["Sulphides", "Pyrite, FeS2; galena, PbS (lead ore); chalcopyrite, CuFeS2 (copper ore)."],
            ["Sulphates", "Gypsum, CaSO4.2H2O (used in plaster); barite, BaSO4."],
            ["Halides", "Halite, NaCl (rock salt); fluorite, CaF2."],
            ["Native elements", "Minerals found as a single element: gold (Au), sulphur (S), graphite and diamond (C), copper (Cu)."],
        ]),
        EX("Worked example 1: name the group",
           intro="Name the mineral group (silicate, carbonate, oxide, sulphide, sulphate or halide) for each: PbS, CaCO3, Fe2O3, NaCl.",
           steps=[
               S("PbS", text="Lead combined with sulphur: a **sulphide** (galena)."),
               S("CaCO3", text="Contains the carbonate group CO3: a **carbonate** (calcite)."),
               S("Fe2O3", text="Iron combined with oxygen only: an **oxide** (hematite)."),
               S("NaCl", text="Sodium combined with chlorine: a **halide** (halite)."),
           ]),
        EX("Worked example 2: which minerals in granite?",
           intro="A coarse pink and grey rock has light-coloured, glassy grains, pink or white grains with two cleavages at 90 degrees and flakes that peel into thin sheets. Name the minerals.",
           steps=[
               S("Glassy grains, no cleavage", text="**Quartz**."),
               S("Pink or white grains with two cleavages at about 90 degrees", text="**Feldspar** (orthoclase gives the pink colour)."),
               S("Flakes that peel into sheets", text="**Mica** (biotite or muscovite). The rock is **granite**."),
           ]),
        MISTAKE("Thinking all minerals are silicates",
                "Silicates are the biggest group, but calcite (carbonate), hematite (oxide), pyrite (sulphide), gypsum (sulphate) and halite (halide) are not. "
                "Check the formula: silicates contain Si and O."),
        QUIZ("Which mineral is made only of silicon and oxygen (SiO2)?", ["Feldspar", "Mica", "Quartz", "Olivine"], 2,
             "Quartz is SiO2.", hint="It is hardness 7 and very common in sand.",
             feedback=["Feldspar also contains aluminium and potassium, sodium or calcium.", "Mica contains aluminium, potassium and other elements.", "", "Olivine contains iron and magnesium."]),
        QUIZ("Calcite (CaCO3) belongs to the", ["silicates", "carbonates", "sulphides", "oxides"], 1,
             "It contains the carbonate group CO3.", hint="Look at the group in the formula.",
             feedback=["It contains no silicon.", "", "It contains no sulphur.", "It has carbon as well as oxygen, so it is a carbonate."]),
        TIP("Exam link: Paper 1 asks for the group or formula of common minerals and for mineral properties. Paper 2 may ask you to name the rock-forming minerals of a rock such as granite or basalt. "
            "Learn the formulae in the table."),
        PQ("State the building block of all silicate minerals.",
           "The silica tetrahedron: one silicon atom surrounded by four oxygen atoms."),
        PQ("Name four non-silicate minerals and state the mineral group of each.",
           "Calcite (carbonate), hematite (oxide), pyrite (sulphide), halite (halide); also gypsum (sulphate), gold (native element)."),
        PQ("Distinguish between felsic and ferromagnesian minerals, with two examples of each.",
           "Felsic minerals are light-coloured and rich in silica and aluminium: quartz and feldspar. Ferromagnesian minerals are dark and rich in iron and magnesium: olivine, pyroxene (also amphibole, biotite)."),
        SUM("Oxygen and silicon are the commonest elements in the crust, so silicates are the commonest minerals.",
            "The silica tetrahedron is SiO4; the way tetrahedra join gives olivine, pyroxene, amphibole, mica, feldspar and quartz.",
            "Felsic minerals are light; ferromagnesian minerals are dark.",
            "Non-silicate groups: carbonates, oxides, sulphides, sulphates, halides and native elements."),
    ],
))

# ------------------------------------------------------------------ 9. The rock cycle
LESSONS.append(lesson(
    module=M3, topic="The rock cycle",
    title="The rock cycle: three rock families and the processes that link them",
    slug="gly1-the-rock-cycle",
    minutes=20,
    summary="Igneous, sedimentary and metamorphic rocks are linked in the rock cycle: cooling magma makes igneous rock, weathering and burial make sedimentary rock, heat and pressure make metamorphic rock, and melting returns rock to magma.",
    objectives=[
        "Define rock and name the three rock families",
        "Describe how each family forms",
        "Name the processes that link the rock types in the rock cycle",
        "Trace a rock through the cycle with examples from Cameroon",
    ],
    key_concepts=["Rock", "Igneous", "Sedimentary", "Metamorphic", "Weathering", "Lithification", "Rock cycle"],
    blocks=[
        H("Introduction"),
        T("The rocks around you are not permanent. The granite hill near Yaounde is slowly breaking into sand. The sand in a river carried to the coast may one day be buried and turned into sandstone. "
          "Deep under a mountain, sandstone may be baked into a harder rock. Rocks are always changing from one kind to another."),
        D("A **rock** is a natural solid made of one or more minerals (or sometimes of organic matter, such as coal).", title="Rock"),
        KEY("The three rock families", "They differ in how they form.", cards=[
            ["Igneous", "Formed when magma or lava cools and crystallises. Examples: granite, basalt, gabbro."],
            ["Sedimentary", "Formed from sediments (broken rock pieces, chemical deposits or organic remains) that are compacted and cemented. Examples: sandstone, shale, limestone, coal."],
            ["Metamorphic", "Formed when an existing rock is changed, while still solid, by heat, pressure or chemical fluids. Examples: marble, slate, gneiss."],
        ]),
        H("The rock cycle"),
        D("The **rock cycle** is the set of processes by which rocks change from one type to another over geological time. It is not a one-way circle: a rock can take shortcuts.", title="Rock cycle"),
        IMG("f5gly1-rockcycle.svg", alt="Diagram of the rock cycle linking magma, igneous rock, sediments, sedimentary rock and metamorphic rock with arrows labelled by the processes",
            caption="Figure 1. The rock cycle (schematic). Arrows show the processes."),
        KEY("Processes in the rock cycle", "Know the name of each process and what it does.", cards=[
            ["Cooling and crystallisation", "Magma or lava cools and forms crystals: igneous rock."],
            ["Weathering and erosion", "Rock is broken down (weathering) and the pieces are removed (erosion)."],
            ["Transport and deposition", "Sediment is carried by water, wind or ice and laid down in layers."],
            ["Compaction and cementation (lithification)", "Burial squeezes the sediment, and minerals from water glue the grains together: sedimentary rock."],
            ["Metamorphism", "Heat, pressure and fluids change rock without melting it: metamorphic rock."],
            ["Melting", "At great depth rock melts to magma, and the cycle starts again."],
            ["Uplift", "Earth movements raise rocks to the surface, where weathering attacks them."],
        ]),
        T("The cycle is driven by two energy sources. The Earth's internal heat drives melting, metamorphism and uplift. The Sun's energy drives the weather, which causes weathering and erosion."),
        EX("Worked example 1: trace a granite",
           intro="Granite is uplifted and exposed. Describe one path it may take to become a metamorphic rock.",
           steps=[
               S("Weathering and erosion", text="Rain, temperature changes and roots break the granite into sand and clay, which rivers carry away."),
               S("Deposition and lithification", text="The sand is laid down in layers, buried, compacted and cemented into **sandstone**."),
               S("Metamorphism", text="Deep burial or mountain building heats the sandstone and presses it, and it changes into **quartzite**."),
           ]),
        T("Cameroon shows all the families. Much of the country sits on very old crystalline basement rocks such as granite and gneiss. "
          "Mount Cameroon is built of basalt, an igneous rock. The coastal Douala Basin holds sedimentary rocks."),
        EX("Worked example 2: name the process",
           intro="Name the process at each arrow: (a) sandstone changes to quartzite; (b) magma becomes granite; (c) loose sand becomes sandstone.",
           steps=[
               S("(a)", text="Heat and pressure change a rock without melting it: **metamorphism**."),
               S("(b)", text="Magma cools and crystallises: **solidification (crystallisation)**."),
               S("(c)", text="Compaction and cementation: **lithification** (diagenesis)."),
           ]),
        MISTAKE("Saying the rock cycle always goes igneous, sedimentary, metamorphic in order",
                "There are shortcuts. Igneous rock can become metamorphic without ever being a sediment, and any rock can melt. Describe the process, not just the order."),
        MISTAKE("Saying metamorphic rocks are melted rocks",
                "Metamorphic rocks form in the solid state. If the rock melts completely it becomes magma, and when that cools it becomes igneous rock."),
        QUIZ("Which process turns loose sediment into sedimentary rock?", ["Weathering", "Melting", "Compaction and cementation", "Metamorphism"], 2,
             "Compaction squeezes the grains and cementation glues them.", hint="The grains must be pressed and glued together.",
             feedback=["Weathering breaks rocks down.", "Melting gives magma.", "", "Metamorphism changes existing rock with heat and pressure."]),
        QUIZ("Marble is a metamorphic rock formed from", ["sandstone", "limestone", "granite", "shale"], 1,
             "Limestone, made of calcite, recrystallises into marble.", hint="Marble is mostly calcite.",
             feedback=["Sandstone gives quartzite.", "", "Granite gives gneiss.", "Shale gives slate."]),
        TIP("Exam link: Paper 1 asks which process forms which rock. Paper 2 may give a rock cycle diagram with arrows to name or label. "
            "Learn the process names: crystallisation, weathering, erosion, transport, deposition, lithification, metamorphism, melting."),
        PQ("Define a rock and name the three families of rock.",
           "A rock is a natural solid made of one or more minerals. The three families are igneous, sedimentary and metamorphic."),
        PQ("Name the processes by which (a) igneous rock becomes sediment and (b) sediment becomes sedimentary rock.",
           "(a) Weathering, erosion, transport and deposition. (b) Compaction and cementation (lithification, diagenesis)."),
        PQ("Describe how a limestone may be changed into magma by the rock cycle.",
           "The limestone is buried deeply by mountain building. Heat and pressure change it to marble (metamorphism). If it goes deeper and the temperature rises enough, the marble melts to form magma."),
        SUM("The three rock families are igneous, sedimentary and metamorphic.",
            "Magma cools to form igneous rock; weathering, transport, deposition and lithification form sedimentary rock; heat and pressure form metamorphic rock; melting forms magma.",
            "The cycle has shortcuts and is driven by the Earth's heat and the Sun's energy.",
            "Cameroon has basement granite and gneiss, basalt on Mount Cameroon and sedimentary basins."),
    ],
))

# ------------------------------------------------------------------ 10. Igneous rocks
LESSONS.append(lesson(
    module=M3, topic="Igneous rocks",
    title="Igneous rocks: magma, Bowen's series and intrusive structures",
    slug="gly1-igneous-rocks",
    minutes=26,
    summary="Igneous rocks crystallise from magma; texture shows cooling speed (plutonic coarse, volcanic fine), silica content gives acid to ultrabasic types, Bowen's series shows the order of crystallisation, and bodies such as dykes, sills, laccoliths and batholiths are intrusions.",
    objectives=[
        "Distinguish magma from lava and plutonic from volcanic rocks",
        "Classify igneous rocks by silica content and texture",
        "Describe Bowen's reaction series",
        "Describe dykes, sills, laccoliths and batholiths",
    ],
    key_concepts=["Magma", "Lava", "Plutonic", "Volcanic", "Acid and basic", "Bowen's series", "Dyke", "Sill", "Laccolith", "Batholith"],
    blocks=[
        H("Introduction"),
        T("Granite blocks are used for building and for kitchen worktops. Basalt is crushed for road stone. Both are igneous rocks, but they look different: granite has big, visible crystals, and basalt looks fine and dark. "
          "The reason is how fast they cooled."),
        D("**Magma** is molten rock underground, with dissolved gases. **Lava** is molten rock that has reached the surface and lost most of its gas.", title="Magma and lava"),
        H("Texture and place of cooling"),
        KEY("How cooling speed gives texture", "Slow cooling gives big crystals; fast cooling gives small ones.", cards=[
            ["Plutonic (intrusive)", "Magma cools slowly deep underground: coarse crystals you can see. Examples: granite, gabbro."],
            ["Hypabyssal", "Cools at shallow depth in dykes and sills: medium crystals. Example: dolerite."],
            ["Volcanic (extrusive)", "Lava cools quickly at the surface: fine crystals, or glass if very fast. Examples: basalt, rhyolite, obsidian (glass)."],
        ]),
        H("Classification by silica content"),
        CODE("Class           Silica (SiO2)   Colour   Plutonic     Volcanic\n"
             "Acid            over 66%        light    granite      rhyolite\n"
             "Intermediate    52 to 66%       medium   diorite      andesite\n"
             "Basic           45 to 52%       dark     gabbro       basalt\n"
             "Ultrabasic      under 45%       very dark peridotite  (rare)",
             "text", title="Igneous rocks by silica content"),
        T("Acid rocks contain quartz and light minerals. Basic rocks contain dark minerals such as pyroxene and olivine, and plagioclase rich in calcium. "
          "Basic magma is hotter and runny. Acid magma is cooler and sticky."),
        H("Bowen's reaction series"),
        T("In the 1920s the American geologist N. L. Bowen showed that minerals crystallise from cooling magma in a fixed order. "
          "High-temperature minerals form first. As the magma cools, the first crystals react with the melt to form the next mineral in the series."),
        IMG("f5gly1-bowen.svg", alt="Bowen's reaction series showing the discontinuous series olivine, pyroxene, amphibole, biotite on one side and the continuous plagioclase series on the other, merging to K-feldspar, muscovite and quartz",
            caption="Figure 1. Bowen's reaction series. The top is hottest."),
        KEY("Two branches that join", "Know both branches and the last minerals.", cards=[
            ["Discontinuous series (dark minerals)", "Olivine, then pyroxene, then amphibole, then biotite mica. Each mineral changes into a different one."],
            ["Continuous series (plagioclase)", "From calcium-rich to sodium-rich plagioclase. The crystal structure stays the same while the composition changes gradually."],
            ["Last to crystallise", "The two branches join. Then K-feldspar (orthoclase), muscovite and finally quartz form at the lowest temperature."],
        ]),
        T("Bowen's series explains why olivine and quartz are almost never found together. Olivine forms at high temperature and quartz at the lowest. "
          "It also shows that basic rocks (gabbro, basalt) are rich in the minerals at the top, and acid rocks (granite) in those at the bottom."),
        H("Intrusive structures"),
        D("An **intrusion** is a body of igneous rock formed when magma forced its way into older rocks and cooled underground. A **concordant** intrusion lies parallel to the layers it enters; "
          "a **discordant** one cuts across them.", title="Intrusion"),
        IMG("f5gly1-intrusions.svg", alt="Cross-section showing a batholith at the base, a dyke cutting upward across layers, a sill between layers, a laccolith that arches the layers above it, and a volcano",
            caption="Figure 2. Igneous intrusions (schematic)."),
        KEY("Main intrusions", "Note which are concordant and which are discordant.", cards=[
            ["Batholith", "A huge discordant mass of coarse rock, usually granite, over 100 square km at the surface, formed deep in the crust."],
            ["Dyke", "A narrow, wall-like sheet that cuts across the layers (discordant). Often vertical."],
            ["Sill", "A sheet that lies along the layers (concordant), usually horizontal."],
            ["Laccolith", "A concordant mass with a flat floor and a domed top that pushes the layers above upwards. Mushroom or lens shaped."],
        ]),
        EX("Worked example 1: classify two rocks",
           intro="Rock X is coarse, light-coloured, with quartz, pink feldspar and mica. Rock Y is fine-grained, dark and holds no visible crystals. Name each and say how each formed.",
           steps=[
               S("Rock X", text="Coarse crystals mean slow cooling at depth. Quartz and a lot of light minerals mean acid. It is **granite**, a plutonic rock."),
               S("Rock Y", text="Fine grain means fast cooling at the surface. Dark colour means basic. It is **basalt**, a volcanic rock."),
           ]),
        EX("Worked example 2: use Bowen's series",
           intro="A magma cools slowly. Which of olivine, quartz and amphibole forms first, and which last?",
           steps=[
               S("Rank by temperature", text="Olivine crystallises at the highest temperature, amphibole at an intermediate one, and quartz at the lowest."),
               S("Answer", text="Olivine first, then amphibole, and quartz last."),
           ]),
        MISTAKE("Mixing up dyke and sill",
                "Both are sheets. A dyke cuts **across** the layers; a sill lies **along** (between) them. Remember: dyke = discordant."),
        QUIZ("Which igneous rock is coarse-grained and basic?", ["Granite", "Basalt", "Gabbro", "Rhyolite"], 2,
             "Gabbro is the coarse, plutonic equivalent of basalt.", hint="Plutonic and basic.",
             feedback=["Granite is coarse but acid.", "Basalt is basic but fine-grained.", "", "Rhyolite is acid and fine-grained."]),
        QUIZ("Which intrusion lies along the bedding planes and is horizontal?", ["Dyke", "Sill", "Batholith", "Volcanic neck"], 1,
             "A sill is a concordant sheet.", hint="Concordant means parallel to the layers.",
             feedback=["A dyke cuts across the beds.", "", "A batholith is a huge mass, not a sheet.", "A neck is a pipe-shaped body that fed a volcano."]),
        TIP("Exam link: Paper 1 asks for rock names, textures and Bowen's order. Paper 2 may ask you to describe and sketch igneous structures. "
            "Draw the beds first, then show clearly whether the intrusion crosses them (dyke) or lies between them (sill)."),
        PQ("Distinguish between magma and lava.",
           "Magma is molten rock underground that holds dissolved gases. Lava is molten rock at the surface after most of the gas has escaped."),
        PQ("Explain why granite has large crystals but basalt has very small crystals.",
           "Granite forms from magma cooling slowly deep in the crust, so crystals have time to grow large. Basalt forms from lava cooling quickly at the surface, so only tiny crystals form."),
        PQ("Describe Bowen's reaction series.",
           "It shows the order of crystallisation of minerals from a cooling magma. The discontinuous series goes olivine, pyroxene, amphibole, biotite. The continuous series goes from calcium-rich to sodium-rich plagioclase. The two join to give K-feldspar, muscovite and finally quartz."),
        PQ("Distinguish between a dyke and a sill.",
           "A dyke is a discordant sheet of igneous rock that cuts across the bedding, usually vertical. A sill is a concordant sheet that lies along the bedding, usually horizontal."),
        SUM("Magma is underground; lava is at the surface. Slow cooling makes coarse (plutonic) rock; fast cooling makes fine (volcanic) rock.",
            "By silica: acid (granite, rhyolite), intermediate (diorite, andesite), basic (gabbro, basalt), ultrabasic (peridotite).",
            "Bowen's series: olivine, pyroxene, amphibole, biotite and calcium-rich to sodium-rich plagioclase join to K-feldspar, muscovite and quartz.",
            "Dykes cut across; sills lie along the layers; laccoliths dome the layers above; batholiths are huge granite masses."),
    ],
))

# ------------------------------------------------------------------ 11. Volcanism and the Cameroon Volcanic Line
LESSONS.append(lesson(
    module=M3, topic="Volcanism and the Cameroon Volcanic Line",
    title="Volcanoes and the Cameroon Volcanic Line (Mount Cameroon)",
    slug="gly1-volcanism-cameroon-volcanic-line",
    minutes=22,
    summary="A volcano is a vent where magma, ash and gas reach the surface; Mount Cameroon is an active volcano on the Cameroon Volcanic Line, a chain of volcanoes and crater lakes running from the Gulf of Guinea into the highlands of the north-west.",
    objectives=[
        "Describe the parts of a volcano and the materials it erupts",
        "Compare shield, composite and cinder cone volcanoes",
        "Describe the Cameroon Volcanic Line and Mount Cameroon",
        "Explain the benefits and hazards of volcanism in Cameroon",
    ],
    key_concepts=["Volcano", "Vent", "Crater", "Lava", "Pyroclasts", "Shield volcano", "Cameroon Volcanic Line", "Mount Cameroon"],
    blocks=[
        H("Introduction"),
        T("On clear days the slopes of Mount Cameroon rise above Buea and Limbe, thick with forest and plantations. Beneath that peace is a living volcano. "
          "The volcano has erupted several times in the last century, and the soils it makes help farmers."),
        D("A **volcano** is an opening (vent) in the Earth's crust through which magma, gases, ash and rock fragments reach the surface, and also the hill or mountain built from these materials.", title="Volcano"),
        H("Parts and products"),
        KEY("Parts of a volcano", "From the inside outwards.", cards=[
            ["Magma chamber", "A large pocket of magma deep in the crust."],
            ["Conduit (pipe) and vent", "The channel along which magma rises and the opening at the surface."],
            ["Crater", "The bowl-shaped hollow at the top around the vent."],
            ["Cone", "The hill built from layers of lava and ash."],
        ]),
        KEY("What a volcano erupts", "Three kinds of product.", cards=[
            ["Lava", "Molten rock flowing on the surface. Basaltic lava is runny and spreads far."],
            ["Pyroclasts", "Solid fragments thrown out: ash, cinders, and larger bombs."],
            ["Gases", "Mostly water vapour and carbon dioxide, with sulphur gases."],
        ]),
        KEY("Types of volcano", "The shape depends on the magma.", cards=[
            ["Shield volcano", "Broad, gentle slopes built of runny basaltic lava. Eruptions are usually gentle."],
            ["Composite (strato) volcano", "Steep cone of alternating lava and ash layers; thicker magma, more explosive."],
            ["Cinder cone", "Small steep cone of loose cinders around a vent."],
        ]),
        H("The Cameroon Volcanic Line"),
        T("The **Cameroon Volcanic Line** (CVL) is a chain of volcanoes, crater lakes and igneous centres about 1 600 km long. It runs from islands in the Gulf of Guinea, "
          "through Mount Cameroon on the coast, and north-east through the volcanic highlands of the West and North-West regions towards the Adamawa area and Nigeria."),
        T("It is unusual because it crosses both ocean and continent, and it does not lie on a plate boundary. Geologists still debate its cause, with ideas such as rising hot mantle and "
          "lines of weakness in the lithosphere. Say that the origin is **debated** in an exam if asked."),
        KEY("Features along the line", "Learn a few named examples.", cards=[
            ["Mount Cameroon", "The highest peak in West and Central Africa, about 4 000 m high (sources give 4 040 m or 4 095 m: check your textbook). An active volcano of basaltic lava. Recent eruptions include 1999, 2000 and 2012."],
            ["Mount Manengouba and the Bambouto mountains", "Large old volcanoes with calderas (wide collapse craters), in the West and Littoral highlands."],
            ["Mount Oku", "A high volcanic mountain in the North-West Region with a crater lake."],
            ["Crater lakes (such as Lake Nyos and Lake Monoun)", "Lakes formed in volcanic craters; they hold gas that can be dangerous (see the geohazards lesson)."],
        ]),
        EX("Worked example 1: describe Mount Cameroon",
           intro="Describe Mount Cameroon in four points.",
           steps=[
               S("Place", text="It lies on the coast of the South-West Region, near Buea, on the Cameroon Volcanic Line."),
               S("Type of rock", text="It is built mainly of basaltic lava and ash."),
               S("Activity", text="It is active; it has erupted a number of times, for example in 1999, 2000 and 2012."),
               S("Height", text="About 4 000 m, the highest mountain in West and Central Africa."),
           ]),
        H("Benefits and hazards"),
        KEY("Benefits", "Volcanic regions are valuable.", cards=[
            ["Fertile soils", "Weathered basalt and ash give rich soil for banana, oil palm, rubber, tea and food crops."],
            ["Building materials", "Basalt is crushed for roads and concrete."],
            ["Tourism and water", "Crater lakes and climbing events, and springs from the mountain slopes."],
        ]),
        KEY("Hazards", "Hazards must be monitored.", cards=[
            ["Lava flows", "Burn and bury farms and roads, though people can usually walk away."],
            ["Ash and gas", "Ash can damage roofs, crops and lungs; gases can be toxic."],
            ["Earthquakes", "Magma movement can cause small earthquakes before an eruption."],
            ["Gas from crater lakes", "A sudden release of carbon dioxide can kill by suffocation, as at Lake Nyos in 1986."],
        ]),
        EX("Worked example 2: why are volcanic slopes farmed?",
           intro="Explain why people farm on the slopes of Mount Cameroon despite the risk.",
           steps=[
               S("Soil", text="Weathered basalt and ash give mineral-rich, fertile soils."),
               S("Rainfall and water", text="The mountain receives heavy rain, and there are many springs."),
               S("Balance", text="Eruptions are infrequent, so the benefit outweighs the occasional risk. Monitoring and warnings reduce the danger."),
           ]),
        MISTAKE("Saying the Cameroon Volcanic Line is on a plate boundary",
                "Cameroon lies inside the African plate. The CVL is not at a boundary, and its cause is debated. Do not claim it is formed by plates colliding or splitting."),
        QUIZ("Mount Cameroon is built mainly of", ["granite", "basalt", "limestone", "gneiss"], 1,
             "It is a basaltic volcano.", hint="It is a volcanic rock.",
             feedback=["Granite is a plutonic rock, not volcanic.", "", "Limestone is a sedimentary rock.", "Gneiss is a metamorphic rock."]),
        QUIZ("Which statement about the Cameroon Volcanic Line is correct?", ["It lies along the boundary of the African plate", "It is a chain of volcanoes and crater lakes about 1 600 km long", "It has no active volcano", "It contains only granite"], 1,
             "It is a long chain of volcanic centres crossing ocean and continent.", hint="Think of its length and its features.",
             feedback=["It lies inside the African plate.", "", "Mount Cameroon is active.", "It is mostly volcanic rock such as basalt, plus other igneous types."]),
        TIP("Exam link: Paper 1 asks about parts of a volcano and volcano types. Paper 2 may ask you to describe Mount Cameroon and the Cameroon Volcanic Line with benefits and hazards. "
            "Use named places and say that the origin of the line is debated."),
        PQ("State three products of a volcanic eruption.",
           "Lava, pyroclasts (ash, cinders and bombs) and gases such as water vapour and carbon dioxide."),
        PQ("Describe the Cameroon Volcanic Line.",
           "A chain of volcanoes and crater lakes about 1 600 km long, from the Gulf of Guinea islands through Mount Cameroon and the highlands of the West and North-West regions. It crosses ocean and continent, is not on a plate boundary and its cause is debated."),
        PQ("Give two benefits and two hazards of volcanism in Cameroon.",
           "Benefits: fertile soil for farming; building stone such as basalt; tourism. Hazards: lava flows; ash falls; toxic gases and gas release from crater lakes such as Lake Nyos."),
        SUM("A volcano is a vent where magma, ash and gas reach the surface; it has a chamber, conduit, vent, crater and cone.",
            "Shield volcanoes are broad and gentle; composite volcanoes are steep and more explosive; cinder cones are small.",
            "The Cameroon Volcanic Line is a chain of volcanoes and crater lakes about 1 600 km long, not on a plate boundary; its origin is debated.",
            "Mount Cameroon is an active basaltic volcano, about 4 000 m high.",
            "Volcanoes bring fertile soils and resources, and also hazards."),
    ],
))

# ------------------------------------------------------------------ 12. Sedimentary rocks
LESSONS.append(lesson(
    module=M3, topic="Sedimentary rocks",
    title="Sedimentary rocks: formation, types and structures",
    slug="gly1-sedimentary-rocks",
    minutes=24,
    summary="Sedimentary rocks form when weathered material is eroded, transported, deposited and turned to rock by compaction and cementation; they are clastic, chemical or organic, and show structures such as bedding, graded bedding and ripple marks.",
    objectives=[
        "Describe weathering, transport, deposition and diagenesis",
        "Classify clastic, chemical and organic sedimentary rocks with examples",
        "Describe bedding, graded bedding, cross-bedding, ripple marks and mud cracks",
        "Link grain size and rounding to the history of the sediment",
    ],
    key_concepts=["Sediment", "Diagenesis", "Clastic", "Chemical", "Organic", "Bedding", "Graded bedding", "Ripple marks"],
    blocks=[
        H("Introduction"),
        T("The sand on a river bank, the clay used by potters and the limestone burnt to make cement are all sediments or sedimentary rocks. "
          "Sedimentary rocks cover most of the Earth's land surface in a thin layer, and they hold nearly all fossils, oil, gas and coal."),
        D("A **sedimentary rock** is a rock formed from sediments: pieces of older rocks, chemical precipitates or the remains of living things, which are laid down and made hard.", title="Sedimentary rock"),
        H("How sedimentary rocks form"),
        KEY("Four stages", "In order.", cards=[
            ["1. Weathering and erosion", "Rock is broken down by weather and removed."],
            ["2. Transport", "Water, wind or ice carries the sediment. Grains become smaller and rounder with distance."],
            ["3. Deposition", "The sediment settles in layers when the energy of the carrying agent falls, for example in a lake, delta or sea."],
            ["4. Diagenesis (lithification)", "Burial gives **compaction** (grains pressed closer, water squeezed out) and **cementation** (minerals such as silica, calcite or iron oxide crystallise between grains and glue them)."],
        ]),
        H("Types of sedimentary rock"),
        KEY("Three groups", "By how the sediment was made.", cards=[
            ["Clastic (detrital)", "Made of broken rock fragments (clasts). Named by grain size."],
            ["Chemical", "Formed when minerals come out of water solution, for example when water evaporates or by chemical reaction."],
            ["Organic", "Made from the remains of plants or animals."],
        ]),
        CODE("Clastic rocks (grain size)\n"
             "Rock          Grains                 Size\n"
             "Conglomerate  rounded pebbles        over 2 mm\n"
             "Breccia       angular fragments      over 2 mm\n"
             "Sandstone     sand grains            0.06 to 2 mm\n"
             "Siltstone     silt                   0.004 to 0.06 mm\n"
             "Shale/clay    clay                   under 0.004 mm", "text", title="Clastic rocks"),
        T("Rounded pebbles show they travelled far. Angular fragments (breccia) show they were deposited close to their source."),
        CODE("Chemical and organic rocks\n"
             "Rock             Origin            Made of\n"
             "Rock salt        chemical (evaporite)   halite\n"
             "Gypsum rock      chemical (evaporite)   gypsum\n"
             "Limestone        chemical or organic    calcite (shells)\n"
             "Ironstone        chemical               iron minerals\n"
             "Coal             organic                carbon from plants", "text", title="Chemical and organic rocks"),
        H("Sedimentary structures"),
        IMG("f5gly1-bedding.svg", alt="Left panel: a bed with coarse grains at the bottom and fine grains at the top. Right panel: a wavy bed surface with a current arrow",
            caption="Figure 1. Graded bedding (left) and ripple marks (right)."),
        KEY("Structures to know", "The Board says many candidates describe these wrongly.", cards=[
            ["Bedding (stratification)", "Layers of sediment laid down one above the other, separated by bedding planes. The oldest layer is at the bottom if undisturbed."],
            ["Graded bedding", "A bed in which grain size changes gradually: coarse at the bottom, finer towards the top. It forms when a current slows down."],
            ["Cross-bedding", "Thin sloping layers inside a bed, left by migrating dunes or ripples. Shows current direction."],
            ["Ripple marks", "Small wavy ridges on the bed surface made by moving water or wind over sediment."],
            ["Mud cracks", "Polygon cracks in clay that dried in the sun. Show the sediment was once wet and then exposed."],
        ]),
        MISTAKE("Mixing up graded bedding with a series of different beds",
                "Graded bedding is one bed in which the grain size changes smoothly, coarse below and fine above. It is not a set of separate beds."),
        EX("Worked example 1: read the history of a sediment",
           intro="A rock has rounded pebbles in a sandy matrix cemented by iron oxide. Name the rock and describe what its grains tell us.",
           steps=[
               S("Name", text="Rounded pebbles over 2 mm: a **conglomerate**."),
               S("History of the pebbles", text="The rounding shows the pebbles were carried a long way by a river or the waves."),
               S("Cement", text="Iron oxide glued the grains: this is **cementation**, the last stage of diagenesis."),
           ]),
        EX("Worked example 2: how long to form a bed?",
           intro="In a practice problem (figures invented for practice) mud collects at 1 mm every 100 years. How long would a 30 cm bed take?",
           steps=[
               S("Convert 30 cm to mm", math=r"30 \text{ cm} = 300 \text{ mm}"),
               S("Number of 1 mm layers", math=r"300 \times 100 \text{ years}"),
               S("Answer", math=r"30\,000 \text{ years}"),
           ]),
        QUIZ("A sedimentary rock made of angular fragments over 2 mm is", ["conglomerate", "breccia", "sandstone", "shale"], 1,
             "Breccia has angular fragments over 2 mm.", hint="Angular, not rounded.",
             feedback=["Conglomerate has rounded pebbles.", "", "Sandstone has smaller grains.", "Shale is made of clay."]),
        QUIZ("Graded bedding is a bed in which", ["the grains are coarse at the top and fine at the bottom", "the grains are coarse at the bottom and finer towards the top", "the surface is wavy", "the layers are tilted"], 1,
             "Coarse below, finer above.", hint="Think of a current slowing down.",
             feedback=["That would be reverse grading.", "", "That describes ripple marks.", "That describes tilted beds or cross-bedding."]),
        TIP("Exam link: Paper 1 asks for rock types and grain sizes. Paper 2 can ask you to describe graded bedding and ripple marks, name clastic rocks and explain diagenesis. "
            "Write what each looks like and how it formed."),
        PQ("Define graded bedding and ripple marks.",
           "Graded bedding is a bed in which grain size changes gradually, coarse at the bottom and finer towards the top. Ripple marks are small undulations made on a sediment surface by moving water or wind."),
        PQ("Describe how loose sand becomes sandstone.",
           "The sand is buried, compaction squeezes the grains closer and removes water, and cementation by minerals such as silica or iron oxide glues the grains together. These processes are called diagenesis (lithification)."),
        PQ("Name one clastic, one chemical and one organic sedimentary rock.",
           "Clastic: sandstone (or shale, conglomerate). Chemical: rock salt (or gypsum). Organic: coal (or limestone made of shells)."),
        SUM("Sedimentary rocks form by weathering, erosion, transport, deposition and diagenesis (compaction and cementation).",
            "Types: clastic (named by grain size), chemical and organic.",
            "Rounded grains travelled far; angular grains travelled a short way.",
            "Structures: bedding, graded bedding (coarse below, fine above), cross-bedding, ripple marks and mud cracks."),
    ],
))

# ------------------------------------------------------------------ 13. Metamorphic rocks
LESSONS.append(lesson(
    module=M3, topic="Metamorphic rocks",
    title="Metamorphic rocks: contact, regional and dynamic metamorphism",
    slug="gly1-metamorphic-rocks",
    minutes=22,
    summary="Metamorphic rocks form when heat, pressure or fluids change an existing rock in the solid state: contact metamorphism near intrusions, regional metamorphism in mountain belts and dynamic metamorphism along faults.",
    objectives=[
        "Define metamorphism and name its agents",
        "Distinguish contact, regional and dynamic metamorphism",
        "Describe foliated and non-foliated metamorphic rocks",
        "Name the parent rock of common metamorphic rocks",
    ],
    key_concepts=["Metamorphism", "Parent rock", "Contact", "Regional", "Dynamic", "Foliation", "Marble", "Gneiss"],
    blocks=[
        H("Introduction"),
        T("Marble is used for floors and statues. Slate was used for roofing and school writing boards. Both were once other rocks that were changed deep in the Earth. "
          "A metamorphic rock keeps no memory of being sediment or magma, but clues remain."),
        D("**Metamorphism** is the change of an existing rock (the **parent rock**) into a new rock by heat, pressure or chemically active fluids, while the rock stays solid.", title="Metamorphism"),
        KEY("Agents of metamorphism", "Each one changes the rock differently.", cards=[
            ["Heat", "From magma or from deep burial. Makes minerals recrystallise or react to form new ones."],
            ["Pressure", "From the weight of overlying rock or from sideways squeezing during mountain building. Flattens minerals and makes them line up."],
            ["Chemically active fluids", "Hot water and gases that carry ions and change mineral composition."],
        ]),
        H("Types of metamorphism"),
        KEY("Three types", "Learn where each occurs.", cards=[
            ["Contact (thermal) metamorphism", "Heat from an igneous intrusion bakes the surrounding rock in a zone called the metamorphic aureole. High temperature, low pressure. Limestone becomes marble; sandstone becomes quartzite; shale becomes hornfels."],
            ["Regional metamorphism", "Occurs over very large areas in mountain belts at plate collisions. High temperature and high pressure. Shale becomes slate, then phyllite, then schist, then gneiss as the grade rises."],
            ["Dynamic (cataclastic) metamorphism", "Occurs along fault zones where rock is crushed and sheared. High stress, little heat. Gives fault breccia and mylonite."],
        ]),
        T("The **grade** of metamorphism is how strongly the rock has been changed. Slate is low grade, schist is medium grade and gneiss is high grade."),
        H("Texture: foliated and non-foliated"),
        D("**Foliation** is the layered or banded texture of a rock in which flaky minerals (mica) or bands of minerals are lined up at right angles to the squeezing direction.", title="Foliation"),
        CODE("Parent rock    Metamorphic rock    Texture\n"
             "Shale          Slate               foliated, splits into sheets\n"
             "Slate          Phyllite            foliated, silky sheen\n"
             "Phyllite       Schist              foliated, visible mica\n"
             "Granite/shale  Gneiss              banded, coarse\n"
             "Limestone      Marble              non-foliated, interlocking calcite\n"
             "Sandstone      Quartzite           non-foliated, very hard\n"
             "Shale (baked)  Hornfels            non-foliated, fine and hard\n"
             "Coal           Anthracite          non-foliated", "text", title="Common metamorphic rocks"),
        T("Non-foliated rocks form when the minerals are not flat, as in limestone (calcite) and sandstone (quartz), or when heat is the main agent. "
          "Much of Cameroon's basement is made of old gneiss, schist and granite, which were deeply buried and changed long ago."),
        EX("Worked example 1: name the parent rock",
           intro="Name the parent rock of (a) marble, (b) quartzite, (c) slate.",
           steps=[
               S("(a)", text="Marble is made of recrystallised calcite: parent **limestone**."),
               S("(b)", text="Quartzite is made of fused quartz grains: parent **sandstone**."),
               S("(c)", text="Slate is the low-grade product of mud rocks: parent **shale**."),
           ]),
        EX("Worked example 2: which type of metamorphism?",
           intro="Limestone next to a granite intrusion becomes marble in a zone 200 m wide. Name the type, and describe why the rock has no foliation.",
           steps=[
               S("Type", text="Heat from the intrusion is the main agent: **contact metamorphism**."),
               S("No foliation", text="Pressure is low, so minerals are not squeezed into lines. Calcite also forms interlocking, non-flat grains. Marble is non-foliated."),
           ]),
        MISTAKE("Saying metamorphic rocks melt",
                "If rock melts it becomes magma. Metamorphism happens in the solid state, with minerals recrystallising or reacting."),
        QUIZ("Which type of metamorphism is caused mainly by heat from an igneous intrusion?", ["Regional", "Dynamic", "Contact", "Burial"], 2,
             "Contact metamorphism bakes the rock beside the intrusion.", hint="Think of what touches the hot magma.",
             feedback=["Regional metamorphism affects large areas in mountain belts.", "Dynamic metamorphism happens along faults.", "", "Burial metamorphism is a low-grade type not covered here."]),
        QUIZ("Which is a foliated metamorphic rock?", ["Marble", "Quartzite", "Hornfels", "Schist"], 3,
             "Schist shows visible aligned mica flakes.", hint="Look for a rock with mica flakes lined up.",
             feedback=["Marble is non-foliated.", "Quartzite is non-foliated.", "Hornfels is non-foliated.", ""]),
        TIP("Exam link: Paper 1 asks for parent rocks and metamorphic types. Paper 2 may ask you to distinguish the types of metamorphism and name the agents. "
            "Always link each type to its place and agents."),
        PQ("Define metamorphism and list its three agents.",
           "Metamorphism is the change of an existing rock into a new rock by heat, pressure or chemically active fluids while it stays solid. The agents are heat, pressure and chemically active fluids."),
        PQ("Distinguish between contact and regional metamorphism.",
           "Contact metamorphism is local, around an igneous intrusion, caused mainly by heat (high temperature, low pressure). Regional metamorphism covers large areas in mountain belts, caused by high temperature and high pressure, and gives foliated rocks."),
        PQ("Name the metamorphic rock formed when (a) limestone and (b) shale undergo increasing regional metamorphism.",
           "(a) Limestone becomes marble. (b) Shale becomes slate, then phyllite, then schist, then gneiss."),
        SUM("Metamorphism changes a rock in the solid state by heat, pressure or chemically active fluids.",
            "Contact metamorphism: heat near an intrusion. Regional: heat and pressure in mountain belts. Dynamic: crushing along faults.",
            "Foliated rocks (slate, phyllite, schist, gneiss) show layering; non-foliated rocks (marble, quartzite, hornfels) do not.",
            "Parent rocks: limestone gives marble, sandstone gives quartzite, shale gives slate."),
    ],
))
