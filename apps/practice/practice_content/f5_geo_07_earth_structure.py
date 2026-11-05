"""Practice sets for Form 5 Geography: Geomorphology, the structure of the Earth (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Geomorphology"
TOPIC = "The structure of the Earth"

SETS = []


def Q(prompt, right, wrongs, pos, steps, concept, skill, hint, feedback="", diagram="", diagram_alt=""):
    """Multiple choice with the correct option inserted at index `pos` (0 = A ... 3 = D)."""
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(right, correct=True))
    return MC(prompt, choices, steps=steps, concept=concept, skill=skill, hint=hint, feedback=feedback,
              diagram=diagram, diagram_alt=diagram_alt)


# ------------------------------------------------------------------ 1. Structure of the Earth
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Layers of the Earth, the lithosphere and plates",
    lesson="geo-structure-of-the-earth",
    questions=[
        Q("The diagram shows a cross-section of the Earth. Which letter shows the mantle?",
          "B", [("A", "A is the thin outer layer, the crust."), ("C", "C is the liquid outer core, found below the mantle."), ("D", "D is the inner core at the centre.")], 1,
          [S("Read the layers from the outside", text="A is the thin outer skin (crust). B is the thick layer below it (mantle). C is the liquid outer core. D is the solid inner core.")],
          concept="Layers of the Earth", skill="Interpretation", hint="Start at the surface and name each layer going inwards.",
          diagram="f5g-geo-q-layers.svg", diagram_alt="Cross-section of the Earth with four layers labelled A (outer crust), B (thick layer), C (outer core) and D (inner core)"),
        Q("Which layer of the Earth is liquid?",
          "The outer core", [("The crust", "The crust is solid rock."), ("The mantle", "The mantle is hot but mostly solid, and it flows only very slowly."), ("The inner core", "The inner core is solid because of the very high pressure.")], 2,
          [S("Recall", text="The outer core is liquid iron and nickel. S waves cannot pass through it.")],
          concept="Outer core", skill="Recall", hint="Think of the layer that stops S waves."),
        NUM("The distance from the Earth's surface to its centre is about 6,370 km. The inner core starts about 5,150 km below the surface. About how many kilometres is the radius of the inner core?",
            1220, steps=[S("Subtract", math=r"6370 - 5150 = 1220 \text{ km}")], tolerance=30, unit="km",
            concept="Radius of the inner core", skill="Calculation", hint="The radius of the inner core is the distance from its edge to the centre."),
        Q("What is the lithosphere?",
          "The crust and the uppermost part of the mantle", [("The liquid layer around the core", "That is the outer core."), ("The thick layer of hot rock that flows slowly", "That describes the mantle or asthenosphere, not the rigid lithosphere."), ("The layer of air around the Earth", "That is the atmosphere.")], 3,
          [S("Definition", text="The lithosphere is the rigid outer shell: the crust plus the rigid top of the mantle, about 100 km thick.")],
          concept="Lithosphere", skill="Recall", hint="It is rigid and it is broken into plates."),
        Q("Scientists know that part of the Earth's core is liquid mainly because",
          "S waves from earthquakes do not pass through it", [("it has been reached by drilling", "The deepest hole is only about 12 km deep."), ("volcanoes bring up liquid from the core", "Volcanic magma comes from the mantle or crust, not from the core."), ("the crust is thinner under the oceans", "The thickness of the crust says nothing about the core.")], 0,
          [S("Seismic evidence", text="S waves cannot travel through liquids. They are not recorded on the far side of the Earth, so the outer core must be liquid.")],
          concept="Seismic waves", skill="Concept", hint="Which kind of earthquake wave cannot travel through a liquid?"),
        Q("How does oceanic crust differ from continental crust?",
          "It is thinner and denser", [("It is thicker and lighter", "That describes continental crust."), ("It is thicker and denser", "Oceanic crust is thin, not thick."), ("It is the same thickness but older", "Oceanic crust is thinner and also younger than most continental crust.")], 1,
          [S("Compare", text="Oceanic crust is about 5 to 10 km thick and dense. Continental crust is thicker (often 30 to 50 km) and lighter.")],
          concept="Continental and oceanic crust", skill="Concept", hint="Which kind of crust sinks when plates meet?"),
        NUM("A plate moves at 5 cm a year. How far does it move in 1,000,000 years? Give the answer in kilometres. (100,000 cm = 1 km.)",
            50, steps=[S("Find the distance in centimetres", math=r"5 \times 1\,000\,000 = 5\,000\,000 \text{ cm}"),
                       S("Convert to kilometres", math=r"5\,000\,000 \div 100\,000 = 50 \text{ km}")], unit="km",
            concept="Speed of plate movement", skill="Calculation", hint="Multiply the yearly movement by the number of years, then convert centimetres to kilometres."),
        Q("The inner core is solid even though it is the hottest layer. Which is the best explanation?",
          "The pressure at the centre of the Earth is extremely high", [("It is made of rock that does not melt", "It is made of iron and nickel, and rock would melt at that temperature."), ("It is cooled by the crust", "The crust is much cooler but very far away."), ("It is too small to be liquid", "Size does not decide it. Pressure does.")], 2,
          [S("Reason", text="Both temperature and pressure increase with depth. At the centre the pressure is so great that the metal is squeezed solid.")],
          concept="State of the inner core", skill="Reasoning", hint="Besides temperature, what else increases as you go deeper?"),
    ]))

# ------------------------------------------------------------------ 2. Rocks by origin
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Igneous, sedimentary and metamorphic rocks",
    lesson="geo-rocks-by-origin",
    questions=[
        Q("Rocks that are formed when magma or lava cools and hardens are called",
          "igneous rocks", [("sedimentary rocks", "Sedimentary rocks form from deposited sediments."), ("metamorphic rocks", "Metamorphic rocks are old rocks changed by heat and pressure."), ("weathered rocks", "Weathering breaks rocks down. It is not a rock type.")], 1,
          [S("Recall", text="Igneous rocks are formed by cooling and solidifying of magma (underground) or lava (on the surface).")],
          concept="Igneous rocks", skill="Recall", hint="The word 'igneous' comes from a word meaning fire."),
        Q("Granite has large crystals but basalt has very small crystals. This is because",
          "basalt cools quickly on the surface", [("granite is formed from sediments", "Granite is igneous, not sedimentary."), ("basalt is formed deep underground", "Rocks formed deep underground cool slowly, like granite."), ("granite is heated by pressure", "Pressure and heat make metamorphic rocks, not granite.")], 3,
          [S("Link cooling speed to crystal size", text="Slow cooling underground (granite) allows large crystals to grow. Fast cooling of lava at the surface (basalt) gives tiny crystals.")],
          concept="Intrusive and extrusive rocks", skill="Concept", hint="Compare how fast magma cools underground and how fast lava cools in the open air."),
        Q("Which of these rocks is most likely to contain fossils?",
          "Limestone", [("Granite", "Granite formed from molten rock, which would destroy any living remains."), ("Marble", "Heat and pressure destroy fossils in metamorphic rocks."), ("Basalt", "Basalt is formed from hot lava, so it contains no fossils.")], 0,
          [S("Fossils and rock type", text="Fossils are found in sedimentary rocks, where the remains of plants and animals were buried in layers. Limestone is sedimentary.")],
          concept="Characteristics of sedimentary rocks", skill="Application", hint="Which of the three rock types forms from layers of buried sediments?"),
        Q("Marble is formed when limestone is changed by",
          "heat and pressure", [("cooling and solidifying", "That is how igneous rocks form."), ("deposition in a lake", "Deposition makes sedimentary rocks."), ("weathering by rain", "Weathering breaks rock down. It does not make marble.")], 2,
          [S("Metamorphism", text="Limestone is changed by great heat and pressure into marble. It does not melt.")],
          concept="Metamorphic rocks", skill="Recall", hint="Marble is a metamorphic rock. What does 'metamorphic' mean?"),
        Q("Which sequence shows the main stages in the formation of a sedimentary rock?",
          "Weathering, erosion, deposition, compaction, cementation", [("Melting, cooling, crystallisation", "That is the formation of an igneous rock."), ("Compaction, weathering, melting", "Melting does not form sedimentary rock."), ("Heat, pressure, recrystallisation", "That is how metamorphic rocks are formed.")], 0,
          [S("Order of stages", text="Rock is broken down (weathering), carried away (erosion), laid down in layers (deposition), squeezed (compaction) and glued (cementation).")],
          concept="Formation of sedimentary rocks", skill="Concept", hint="Think about what happens to sand after a river drops it."),
        Q("Slate is used for roofing because it splits into thin sheets. It was formed from shale by",
          "heat and pressure", [("slow cooling of magma", "That is the formation of intrusive igneous rock."), ("deposition of sand", "That forms sandstone."), ("evaporation of sea water", "That leaves chemical sedimentary rocks like salt.")], 1,
          [S("Metamorphic change", text="Shale is sedimentary. Pressure changes it into slate, which splits easily.")],
          concept="Examples of metamorphic rocks", skill="Application", hint="Slate is metamorphic. How are metamorphic rocks formed?"),
        Q("In the rock cycle, which process can turn any type of rock back into magma?",
          "Melting", [("Weathering", "Weathering makes sediments from rock."), ("Compaction", "Compaction turns loose sediments into sedimentary rock."), ("Deposition", "Deposition lays down sediments.")], 3,
          [S("Rock cycle", text="If rocks are carried deep enough and get hot enough, they melt into magma. When magma cools, new igneous rock forms and the cycle continues.")],
          concept="The rock cycle", skill="Concept", hint="Look at the arrow that points to magma in the rock cycle."),
        Q("A quarry worker finds a very hard rock with large interlocking crystals, no layers and no fossils. The rock is most likely",
          "granite, an intrusive igneous rock", [("sandstone, a sedimentary rock", "Sandstone has layers and grains, and may have fossils."), ("slate, a metamorphic rock", "Slate is fine-grained and splits into thin sheets."), ("limestone, a sedimentary rock", "Limestone is layered and often has fossils.")], 2,
          [S("Match the clues", text="Large crystals show slow cooling underground. No layers or fossils fit igneous rock. This is granite.")],
          concept="Identifying rocks", skill="Application", hint="Large crystals show that the rock cooled slowly."),
    ]))

# ------------------------------------------------------------------ 3. Plate margins
SD = "f5g-geo-q-subduction.svg"
SD_ALT = "Cross-section where an oceanic plate sinks under a continental plate. Letters mark an ocean trench (A), a volcano (B), fold mountains (C), the sinking plate (D), a magma chamber (E) and the mantle (F)"
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Plate margins, folding, faulting and the landforms they build",
    lesson="geo-plate-margins-and-landscape-formation",
    questions=[
        Q("What happens to the plates at a constructive margin?",
          "They move apart", [("They move together", "That is a destructive margin."), ("They slide past each other", "That is a conservative margin."), ("They do not move", "All plate margins involve plate movement.")], 0,
          [S("Recall", text="At a constructive margin plates move apart and new crust forms as magma rises.")],
          concept="Constructive margins", skill="Recall", hint="'Constructive' means building. What is being built?"),
        Q("In the diagram, which letter shows the fold mountains?",
          "C", [("A", "A is the ocean trench on the sea floor."), ("B", "B is a volcano, a cone built by erupted material."), ("D", "D is the oceanic plate sinking into the mantle.")], 2,
          [S("Read the diagram", text="Fold mountains are the crumpled ridges at the edge of the continent, above the sinking plate. They are labelled C.")],
          concept="Fold mountains", skill="Interpretation", hint="Look for the crumpled ridges at the edge of the continent.",
          diagram=SD, diagram_alt=SD_ALT),
        Q("In the diagram, why does the oceanic plate sink below the continental plate?",
          "It is denser than the continental plate", [("It is lighter than the continental plate", "A lighter plate would rise, not sink."), ("It moves faster than the continental plate", "Speed is not the reason. Density is."), ("It is thicker than the continental plate", "Oceanic crust is thinner.")], 1,
          [S("Compare density", text="Oceanic crust is denser (heavier) than continental crust, so when they meet, it is forced down into the mantle. This is subduction.")],
          concept="Subduction", skill="Reasoning", hint="Which kind of crust is heavier?",
          diagram=SD, diagram_alt=SD_ALT),
        Q("Which landform is formed when the crust is pulled apart and a block of land between two faults drops down?",
          "A rift valley", [("A fold mountain", "Fold mountains form when rock layers are squeezed."), ("An ocean trench", "Trenches form where a plate sinks."), ("A volcano", "Volcanoes are built by erupted material, not by a dropped block.")], 3,
          [S("Faulting", text="Tension cracks the crust along faults. The block between the faults sinks, forming a rift valley, as in East Africa.")],
          concept="Rift valleys", skill="Concept", hint="Think about two faults and the block between them."),
        NUM("Two plates move apart at 3 cm a year. How far apart will they be after 1,000,000 years? Give the answer in kilometres. (100,000 cm = 1 km.)",
            30, steps=[S("Distance in centimetres", math=r"3 \times 1\,000\,000 = 3\,000\,000 \text{ cm}"),
                       S("Convert to kilometres", math=r"3\,000\,000 \div 100\,000 = 30 \text{ km}")], unit="km",
            concept="Rate of plate movement", skill="Calculation", hint="Multiply the yearly movement by the number of years."),
        Q("The Himalayas are fold mountains formed where two continental plates collided. Why are there few volcanoes there?",
          "Neither plate sinks deeply enough to melt", [("There is no movement between the plates", "The plates are moving together and the mountains are still rising."), ("Fold mountains are always made of limestone", "Rock type does not decide whether volcanoes form."), ("The crust there is too thin", "The crust is very thick under the Himalayas.")], 1,
          [S("Collision margin", text="Both plates are light continental crust. They crumple upwards instead of sinking, so little magma is made.")],
          concept="Continental collision", skill="Reasoning", hint="Volcanoes need magma. Where does magma come from at destructive margins?"),
        Q("The San Andreas Fault is a conservative margin. Which hazard is most common there?",
          "Earthquakes", [("Volcanic eruptions", "No crust is destroyed and no magma is made at a conservative margin."), ("Formation of new oceanic crust", "That happens at constructive margins."), ("Subduction and trenches", "Plates slide past, so none sinks.")], 2,
          [S("Sliding plates", text="Plates lock and then slip suddenly, causing earthquakes. There are no volcanoes because there is no magma.")],
          concept="Conservative margins", skill="Application", hint="Think about what happens when two plates lock and then slip."),
        Q("Cameroon lies inside the African plate, far from its edges. Which statement is most likely to be true?",
          "Strong earthquakes are rare in most of the country", [("The country is crossed by a destructive margin", "Cameroon is inside a plate, not on a destructive margin."), ("The country has regular strong earthquakes like Japan", "Japan is on a destructive margin. Cameroon is not."), ("Fold mountains are forming in Cameroon today", "There is no plate collision in Cameroon.")], 3,
          [S("Location matters", text="Most strong earthquakes occur at plate margins. Cameroon is far from them, so strong earthquakes are rare. Mount Cameroon is a volcano on the Cameroon Line, which is not a plate margin; check your textbook for how it formed.")],
          concept="Cameroon and plate margins", skill="Application", hint="Where do most earthquakes occur: at plate edges or in the middle of plates?"),
    ]))

# ------------------------------------------------------------------ 4. Volcanic eruptions
VD = "f5g-geo-q-volcano.svg"
VD_ALT = "Cross-section of a volcano with letters: ash cloud (A), crater (B), side vent (C), lava flow (D), main vent (E), cone of ash and lava layers (F) and magma chamber (G)"
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Volcanoes: parts, types, products and distribution",
    lesson="geo-volcanic-eruptions",
    questions=[
        Q("In the diagram, which letter shows the crater?",
          "B", [("A", "A is the ash cloud above the volcano."), ("E", "E is the main vent, the pipe below the crater."), ("G", "G is the magma chamber, deep underground.")], 0,
          [S("Read the diagram", text="The crater is the bowl-shaped hollow at the top of the cone. It is labelled B.")],
          concept="Parts of a volcano", skill="Interpretation", hint="The crater is at the very top of the cone.",
          diagram=VD, diagram_alt=VD_ALT),
        Q("In the diagram, which letter shows the magma chamber?",
          "G", [("C", "C is a side vent, a branch of the main pipe."), ("E", "E is the main vent, the pipe that carries magma upward."), ("F", "F is the cone, built of layers of lava and ash.")], 3,
          [S("Read the diagram", text="The magma chamber is the underground pool of molten rock at the bottom of the vent. It is labelled G.")],
          concept="Parts of a volcano", skill="Interpretation", hint="It is underground, at the base of the vent.",
          diagram=VD, diagram_alt=VD_ALT),
        Q("Which description fits a shield volcano?",
          "Wide with gentle slopes and runny lava", [("Tall and steep with sticky lava", "That describes a composite volcano."), ("Small and made of loose cinders", "That describes a cinder cone."), ("Flat and made only of ash", "A volcano made only of loose ash would be a cinder cone, not a shield.")], 1,
          [S("Recall", text="Runny lava flows a long way before it sets, so the volcano becomes wide with gentle slopes. Mauna Loa in Hawaii is an example.")],
          concept="Types of volcano", skill="Recall", hint="Think about how far runny lava can flow."),
        Q("A volcano that has not erupted for a very long time but could erupt again is called",
          "dormant", [("active", "An active volcano has erupted recently."), ("extinct", "An extinct volcano is not expected to erupt again."), ("composite", "Composite describes the shape, not the activity.")], 2,
          [S("Recall", text="Dormant means 'sleeping': quiet now but able to erupt again.")],
          concept="Active, dormant and extinct", skill="Recall", hint="Which word means 'sleeping'?"),
        Q("Which of these is a pyroclastic product of an eruption?",
          "Volcanic ash", [("Lava", "Lava is molten rock that flows. Pyroclasts are solid fragments."), ("Carbon dioxide", "This is a gas."), ("Magma", "Magma is molten rock underground.")], 0,
          [S("Pyroclasts", text="Pyroclasts are solid fragments thrown into the air: ash, lapilli and volcanic bombs.")],
          concept="Products of eruption", skill="Recall", hint="'Pyro' means fire and 'clast' means broken piece."),
        NUM("A volcanic mudflow (lahar) travels 3 km in 6 minutes. Calculate its average speed in kilometres per hour.",
            30, steps=[S("Convert minutes to hours", math=r"6 \text{ minutes} = \frac{6}{60} = 0.1 \text{ hour}"),
                       S("Divide distance by time", math=r"\frac{3}{0.1} = 30 \text{ km/h}")], unit="km/h",
            concept="Speed of volcanic hazards", skill="Calculation", hint="Change 6 minutes into hours first."),
        Q("Most of the world's active volcanoes are found",
          "along plate margins, such as the Pacific Ring of Fire", [("in the middle of the large plates", "Only a few volcanoes, over hot spots, are far from plate edges."), ("only in hot tropical countries", "Volcanoes occur in cold places too, such as Iceland."), ("only under the Atlantic Ocean", "The Pacific Ring of Fire has more active volcanoes.")], 1,
          [S("Distribution", text="Volcanoes cluster at destructive margins (Ring of Fire), constructive margins (mid-ocean ridges) and rifts, where magma reaches the surface.")],
          concept="Distribution of volcanoes", skill="Concept", hint="Think about where magma is made."),
        Q("Farmers grow crops on the slopes of many volcanoes even though eruptions are dangerous. What is the main reason?",
          "Weathered volcanic rock and ash make fertile soil", [("Lava keeps the ground warm all year", "Warm ground is not the main reason."), ("There are no other flat places for farms", "Volcanic slopes are often steep. Fertile soil is the draw."), ("Volcanoes prevent droughts", "Volcanoes do not control rainfall.")], 3,
          [S("Positive impact", text="Ash and volcanic rock break down into soil rich in minerals. This soil is very fertile, as on the slopes of Mount Cameroon.")],
          concept="Benefits of volcanoes", skill="Application", hint="What does volcanic rock add to the soil?"),
    ]))

# ------------------------------------------------------------------ 5. Earthquakes
QD = "f5g-geo-q-earthquake.svg"
QD_ALT = "Side view of the ground showing an epicentre on the surface (A), the focus underground (B), a fault line (C) and seismic waves spreading out (D)"
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Earthquakes: focus, epicentre, scales and distribution",
    lesson="geo-earthquakes",
    questions=[
        Q("In the diagram, which letter shows the epicentre?",
          "A", [("B", "B is the focus, the underground point where the rock breaks."), ("C", "C is the fault line along which the rocks slip."), ("D", "D shows the seismic waves spreading out.")], 0,
          [S("Read the diagram", text="The epicentre is the point on the surface directly above the focus. It is labelled A.")],
          concept="Epicentre", skill="Interpretation", hint="It is on the ground surface, not underground.",
          diagram=QD, diagram_alt=QD_ALT),
        Q("In the diagram, which letter shows the focus?",
          "B", [("A", "A is the epicentre, on the surface above the focus."), ("C", "C is the fault line, a long crack, not a single point."), ("D", "D shows the waves that spread from the focus.")], 1,
          [S("Read the diagram", text="The focus is the point underground where the rock breaks and the earthquake starts. It is labelled B.")],
          concept="Focus", skill="Interpretation", hint="The focus is the starting point of the earthquake, underground.",
          diagram=QD, diagram_alt=QD_ALT),
        NUM("On the Richter scale, each whole number is about 10 times greater in ground movement than the one below. How many times greater is the ground movement of a magnitude 7 earthquake than a magnitude 5 earthquake?",
            100, steps=[S("Count the steps", text="From 5 to 7 is two steps."),
                        S("Multiply by 10 for each step", math=r"10 \times 10 = 100")],
            concept="Richter scale", skill="Calculation", hint="How many whole numbers are there between 5 and 7?"),
        Q("What is the main cause of earthquakes?",
          "Sudden slip of rocks along faults at plate margins", [("The Moon pulling on the Earth", "The Moon's pull causes tides, not earthquakes."), ("Heavy rainfall on mountains", "Rain may cause landslides, not earthquakes."), ("The spinning of the Earth", "The spin of the Earth does not cause earthquakes.")], 3,
          [S("Cause", text="Plates get stuck and stress builds up. When it exceeds the strength of the rock, the rock slips suddenly along a fault. This releases seismic waves.")],
          concept="Causes of earthquakes", skill="Concept", hint="Think about what happens at plate margins when plates lock."),
        Q("The Mercalli scale measures",
          "the intensity, or effects, of an earthquake at a place", [("the energy released at the focus", "That is the magnitude, measured by the Richter scale."), ("the depth of the focus", "Depth is found from seismograph records, not from the Mercalli scale."), ("the speed of the waves", "Wave speed is not what the Mercalli scale measures.")], 2,
          [S("Recall", text="Mercalli intensity runs from I to XII and is based on what people felt and the damage seen.")],
          concept="Mercalli scale", skill="Recall", hint="Which scale uses Roman numerals and describes damage?"),
        Q("A seismograph is an instrument that",
          "records the vibrations of the ground", [("predicts the exact time of an earthquake", "Earthquakes cannot be predicted exactly."), ("measures the heat inside a volcano", "That would be a thermometer or similar sensor."), ("measures the depth of the ocean", "Depth is measured by a different instrument (echo sounder).")], 1,
          [S("Recall", text="A seismograph detects and records ground vibrations. The record is a seismogram.")],
          concept="Measuring earthquakes", skill="Recall", hint="'Seismic' refers to earthquakes."),
        Q("Which of these is a belt where many earthquakes occur?",
          "The Pacific Ring of Fire", [("The Sahara Desert", "The Sahara is inside a plate, with few strong earthquakes."), ("The Amazon basin", "The interior of South America has few strong earthquakes."), ("The Congo basin", "It lies inside the African plate and strong earthquakes are rare.")], 2,
          [S("Distribution", text="Earthquakes follow plate margins. The Pacific Ring of Fire is the most active belt.")],
          concept="Distribution of earthquakes", skill="Recall", hint="Think about plate margins."),
        Q("The same earthquake was Mercalli intensity VIII in town X and intensity III in town Y. The best explanation is that",
          "town X was closer to the epicentre or had weaker buildings", [("the earthquake had two different magnitudes", "One earthquake has only one magnitude."), ("town Y was on the other side of the focus", "Intensity depends on distance and ground and buildings, not on a side of the focus."), ("Mercalli measures only the energy released", "That is Richter. Mercalli measures effects.")], 3,
          [S("Intensity varies", text="Intensity measures effects at a place. It is greatest near the epicentre and where buildings and ground are weak.")],
          concept="Magnitude and intensity", skill="Reasoning", hint="Which scale is about effects at a place?"),
    ]))

# ------------------------------------------------------------------ 6. Hazards, impacts and mitigation
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Impacts and management of volcanic and earthquake hazards",
    lesson="geo-hazards-impacts-and-mitigation",
    questions=[
        Q("Which of these is a positive impact of a volcanic eruption?",
          "Fertile soils for farming", [("Poisonous gases", "Gases are a danger, not a benefit."), ("Collapse of buildings", "Collapse of buildings is a negative effect, mostly of earthquakes."), ("Ash clouds that stop flights", "Ash closing airports is a negative effect.")], 0,
          [S("Positive effects", text="Volcanic ash and rock weather into rich soil. Other benefits are geothermal energy, minerals and tourism.")],
          concept="Positive impacts of volcanoes", skill="Recall", hint="Think about why farmers live near volcanoes."),
        Q("Which of these is a secondary effect of an earthquake?",
          "A tsunami that floods the coast", [("Buildings collapsing during the shaking", "Collapse is a primary effect, caused directly by the shaking."), ("The ground cracking along the fault", "Ground rupture is a primary effect."), ("The sudden release of energy at the focus", "This is the cause of the earthquake.")], 1,
          [S("Primary and secondary", text="Primary effects are caused directly by the shaking. Secondary effects follow from them, such as tsunamis, fires, landslides and disease.")],
          concept="Primary and secondary effects", skill="Concept", hint="Which effect happens after the shaking, as a result of it?"),
        Q("Why can volcanic eruptions often be monitored for warning signs, but earthquakes cannot be predicted exactly?",
          "Volcanoes show signs such as small tremors, ground swelling and gas changes", [("Volcanoes are always on plate margins", "Earthquakes also occur mainly at plate margins."), ("Earthquakes happen only at night", "Earthquakes can happen at any time."), ("Volcanoes erupt at the same time every year", "Eruptions do not follow a timetable.")], 2,
          [S("Warning signs", text="Rising magma gives warnings that instruments can detect. Earthquakes occur when stress suddenly exceeds the strength of the rock, with no reliable early signs.")],
          concept="Prediction and monitoring", skill="Reasoning", hint="Which hazard gives measurable signs beforehand?"),
        Q("Which building design reduces earthquake damage?",
          "A strong, cross-braced frame with flexible foundations", [("Heavy concrete roofs on thin walls", "Heavy roofs on weak walls collapse and trap people."), ("Tall buildings with no frame", "Buildings without a frame are the most likely to collapse."), ("Buildings made of loose, stacked stones", "Loose stones crumble when the ground shakes.")], 0,
          [S("Design", text="Cross-bracing and flexible foundations let a building sway without collapsing. Light roofs are safer than heavy ones.")],
          concept="Earthquake-resistant building design", skill="Application", hint="A building that can sway is safer than one that is rigid and weak."),
        Q("During an earthquake, a student in a classroom should",
          "drop, cover under a strong table and hold on", [("run to the stairs and use the lift", "Lifts can stick and stairs can collapse. Running during shaking is dangerous."), ("stand next to a window", "Glass can shatter and cause injuries."), ("go outside during the shaking and stand beside the wall", "Falling pieces from walls can injure people outside.")], 3,
          [S("Drill", text="Drop to the ground, take cover under a strong table or desk, and hold on until the shaking stops.")],
          concept="Earthquake drills", skill="Application", hint="Think about what protects you from falling objects."),
        Q("After the 1986 gas disaster at Lake Nyos in Cameroon, scientists installed pipes in the lake. What is the purpose of the pipes?",
          "To release the dissolved gas slowly and safely", [("To keep tourists away from the lake", "The pipes are for safety, not for blocking visitors."), ("To produce electricity from the lake water", "They were not built for power."), ("To stop the lake from filling with rain", "The pipes do not control the water level.")], 2,
          [S("Mitigation", text="Gas had built up in the deep water. Pipes carry the gas-rich water up so that the gas can escape in small amounts. For more detail, check your textbook.")],
          concept="Lake Nyos mitigation", skill="Application", hint="What was the danger at Lake Nyos?"),
        NUM("A town of 12,000 people is built near a volcano. 3,000 of them live in the danger zone and must be evacuated. What percentage of the population must be evacuated?",
            25, steps=[S("Divide and multiply by 100", math=r"\frac{3000}{12000} \times 100 = 25\%")], unit="%",
            concept="Evacuation planning", skill="Calculation", hint="Divide the people in the danger zone by the total population."),
        Q("Which statement best explains why a poorer country may suffer more deaths than a richer country in an earthquake of the same size?",
          "It may have fewer resources for strong buildings, monitoring and rescue", [("Earthquakes are always bigger in poorer countries", "Earthquake size depends on geology, not wealth."), ("Poorer countries have no tectonic plates", "All countries sit on tectonic plates."), ("Richer countries can predict earthquakes exactly", "No country can predict earthquakes exactly.")], 3,
          [S("Vulnerability", text="Wealth affects building quality, warning systems and the speed of rescue. Education and community plans help poorer countries cut the harm.")],
          concept="Rich and poor countries and hazards", skill="Reasoning", hint="What does a country need money for before and after a disaster?"),
    ]))
