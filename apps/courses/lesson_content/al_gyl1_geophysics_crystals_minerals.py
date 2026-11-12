"""A Level Geology (0755), Lower Sixth, modules 1-3: Geophysics & Global Plate Tectonics, Crystallography, and
Optical & Systematic Mineralogy. 14 lessons, one practice set each (see the practice file of the same name).

Scope notes: the outline comes from KKEVO's master curriculum blueprint (not a Board syllabus booklet). The O Level
course already covers seismic waves, layers of the Earth, basic plate tectonics, crystal faces and the physical
properties of minerals; these lessons go to A Level depth (refraction surveys, gravity anomalies and isostasy,
palaeomagnetic calculations, heat flow, Miller indices, stereograms, the polarizing microscope and silicate chemistry).
Where textbooks differ the lesson says "check your textbook". Worked data are teaching values unless a standard
constant is named. Exam facts follow the Board's 2023 Advanced Level subject report.
"""

from .dsl import *  # noqa: F403

COURSE = ("geology", "lower-sixth")

M1 = "Geophysics & Global Plate Tectonics"
M2 = "Crystallography"
M3 = "Optical & Systematic Mineralogy"

LESSONS = []

# ------------------------------------------------------------------ 1. Seismology
LESSONS.append(lesson(
    module=M1,
    topic="Seismology and the Earth's interior",
    title="Seismic refraction, reflection and the velocity structure of the Earth",
    slug="gyl1-seismology-earth-interior",
    minutes=25,
    summary="Seismic velocities depend on the elastic properties and density of rock. Refraction and reflection surveys, travel-time graphs and the global velocity-depth profile reveal the crust, mantle, core and their discontinuities.",
    objectives=[
        "Explain how P- and S-wave velocities depend on elastic moduli and density, and why S waves cannot cross a liquid",
        "Use Snell's law, the critical angle and a two-layer travel-time graph to find layer velocities and thickness",
        "Find the depth of a reflector from a two-way travel time",
        "Interpret the velocity-depth profile of the Earth: Moho, low-velocity zone, Gutenberg and Lehmann discontinuities, shadow zones",
    ],
    key_concepts=["Body waves", "Snell's law", "Critical angle", "Head wave", "Intercept time", "Crossover distance", "Two-way time", "Low-velocity zone", "Shadow zone"],
    blocks=[
        H("Introduction"),
        T("At O Level you learnt that P, S and L waves show the layers of the Earth. At A Level you must explain **why** the waves behave as they do, "
          "and use their travel times to measure depths. Oil companies working in the Douala and Rio del Rey basins use the same physics to map rock layers "
          "kilometres below the surface, and earthquake records from stations around the world map the core."),
        D("**Body waves** travel through the interior of the Earth: **P waves** (primary, compressional, particle motion parallel to the direction of travel) "
          "and **S waves** (secondary, shear, particle motion at right angles to the direction of travel). **Surface waves** travel along the surface: "
          "**Love waves** (horizontal shear) and **Rayleigh waves** (rolling motion). **Transverse** waves are those with motion at right angles to travel: "
          "S waves and Love waves.", title="Seismic waves"),
        H("What controls seismic velocity"),
        F(r"v_P = \sqrt{\dfrac{K + \frac{4}{3}\mu}{\rho}} \qquad v_S = \sqrt{\dfrac{\mu}{\rho}}", title="Velocity of body waves"),
        T(r"Here $K$ is the bulk modulus (resistance to change of volume), $\mu$ is the shear modulus (rigidity, resistance to change of shape) "
          r"and $\rho$ is density. A liquid has no rigidity, so $\mu = 0$ and $v_S = 0$: S waves cannot travel through a liquid. "
          r"P waves always travel faster than S waves because the numerator of the P-wave formula is larger. Velocity usually increases with depth "
          r"because pressure raises $K$ and $\mu$ more than it raises $\rho$."),
        H("Refraction and the critical angle"),
        F(r"\dfrac{\sin i}{v_1} = \dfrac{\sin r}{v_2} \qquad \sin i_c = \dfrac{v_1}{v_2}", title="Snell's law and the critical angle"),
        T(r"When a wave passes into a faster layer ($v_2 > v_1$) it bends away from the normal. At the **critical angle** $i_c$ the refracted ray travels "
          r"along the interface at speed $v_2$. This **head wave** sends energy back up to the surface at the critical angle all along its path."),
        IMG("algyl1-refraction-rays.svg", alt="Two-layer model: a source and geophones on the surface; a direct wave along the surface, a reflected wave from the interface, and a head wave that travels along the interface at velocity v2 after meeting it at the critical angle",
            caption="Figure 1. Direct, reflected and critically refracted (head) waves in a two-layer Earth."),
        T(r"Plot first-arrival time against distance and you get two straight lines. The direct wave has gradient $1/v_1$ and passes through the origin. "
          r"The head wave has gradient $1/v_2$ and, extended back, meets the time axis at the **intercept time** $t_i$. Beyond the **crossover distance** "
          r"$x_c$ the head wave arrives first, because it has travelled most of the way in the fast layer."),
        F(r"t = \dfrac{x}{v_2} + t_i \qquad t_i = \dfrac{2h\cos i_c}{v_1} \qquad x_c = 2h\sqrt{\dfrac{v_2 + v_1}{v_2 - v_1}}", title="Two-layer refraction"),
        IMG("algyl1-travel-time.svg", alt="Travel-time graph: direct line through the origin, refracted line with lower gradient that meets the time axis at the intercept time and crosses the direct line at the crossover distance",
            caption="Figure 2. Travel-time graph for v1 = 6 km/s, v2 = 8 km/s and h = 30 km (teaching values)."),
        EX("Worked example 1: a crust over the mantle", intro="Teaching values: crust velocity 6.0 km/s, upper mantle velocity 8.0 km/s, crust 30 km thick. Find the critical angle, the intercept time and the crossover distance.", steps=[
            S("Critical angle", math=r"\sin i_c = \dfrac{6.0}{8.0} = 0.75 \Rightarrow i_c = 48.6^{\circ}"),
            S("Intercept time", math=r"t_i = \dfrac{2(30)\cos 48.6^{\circ}}{6.0} = \dfrac{60 \times 0.661}{6.0} = 6.6 \text{ s}"),
            S("Crossover distance", math=r"x_c = 2(30)\sqrt{\dfrac{8.0 + 6.0}{8.0 - 6.0}} = 60\sqrt{7} = 159 \text{ km}"),
            S("Meaning", text="Stations closer than about 159 km record the direct wave first; farther stations record the head wave from the top of the mantle (the Pn wave) first."),
        ], check=r"\dfrac{158.7}{6.0} = 26.5 \text{ s} = \dfrac{158.7}{8.0} + 6.6"),
        EX("Worked example 2: depth to bedrock from the intercept time", intro="A shallow survey for a dam site gives a direct-wave velocity of 1 800 m/s, a refracted-wave velocity of 4 500 m/s and an intercept time of 0.040 s. How deep is the bedrock?", steps=[
            S("Critical angle", math=r"\sin i_c = \dfrac{1800}{4500} = 0.40 \Rightarrow i_c = 23.6^{\circ}"),
            S("Rearrange the intercept formula", math=r"h = \dfrac{t_i v_1}{2\cos i_c}"),
            S("Substitute", math=r"h = \dfrac{0.040 \times 1800}{2 \times 0.917} = 39 \text{ m}"),
        ]),
        H("Reflection surveys"),
        T(r"In a reflection survey the wave bounces off a boundary where the **acoustic impedance** (density times velocity) changes. For a reflector at depth $h$ "
          r"directly below the source, the **two-way time** is $t_0 = 2h/v$, so $h = v t_0 / 2$. At offset $x$, $t = \sqrt{x^2 + 4h^2}/v$, a hyperbola."),
        EX("Worked example 3: depth to a reflector", intro="A reflection returns after a two-way time of 0.80 s. The average velocity above the reflector is 2 500 m/s. Find its depth, then the arrival time at a geophone 1 500 m from the source.", steps=[
            S("Depth", math=r"h = \dfrac{v t_0}{2} = \dfrac{2500 \times 0.80}{2} = 1000 \text{ m}"),
            S("Arrival at 1 500 m", math=r"t = \dfrac{\sqrt{1500^2 + 2000^2}}{2500} = \dfrac{2500}{2500} = 1.0 \text{ s}"),
        ]),
        H("The velocity structure of the whole Earth"),
        IMG("algyl1-velocity.svg", alt="Graph of P- and S-wave velocity against depth: velocities jump at the Moho, dip slightly in the low-velocity zone, rise through the mantle, P drops and S falls to zero at 2 890 km, and both rise again at 5 150 km",
            caption="Figure 3. Schematic P- and S-wave velocities with depth (approximate values)."),
        KEY("Discontinuities and zones", "Depths are approximate; check your textbook for the exact values it uses.", cards=[
            ["Moho", "Base of the crust: about 5-10 km under oceans, 30-70 km under continents. P velocity jumps from about 6-7 to about 8 km/s. Some continental crust also shows a weaker Conrad discontinuity between upper and lower crust."],
            ["Low-velocity zone", "About 100-250 km deep. Velocities fall slightly because a small fraction of the rock is molten or close to melting. It matches the weak asthenosphere on which plates move."],
            ["Transition zone", "Velocity steps near 410 km and 660 km, caused by olivine changing to denser crystal structures."],
            ["Gutenberg discontinuity", "About 2 890 km: core-mantle boundary. P velocity drops sharply and S waves stop, so the outer core is liquid."],
            ["Lehmann discontinuity", "About 5 150 km: P velocity increases into the solid inner core."],
        ]),
        T("Because P waves are refracted at the core-mantle boundary, a **P-wave shadow zone** forms at angular distances of roughly 103 to 142 degrees from the focus. "
          "S waves are not recorded beyond about 103 degrees: the **S-wave shadow zone**. Textbooks quote slightly different limits."),
        MISTAKE("Using sin i_c = v2/v1", "The sine of an angle cannot exceed 1. The critical angle uses the slow velocity over the fast one: sin i_c = v1/v2."),
        MISTAKE("Listing only P and S when asked for transverse waves", "Transverse waves are S waves **and** Love waves. P waves and Rayleigh waves are not transverse. Read whether the question asks for body waves, surface waves or transverse waves."),
        T("**Evaluation.** The two-layer method assumes flat, uniform layers with velocity increasing downwards. A dipping layer gives different velocities when shot in opposite "
          "directions, so surveys are reversed. A slower layer under a faster one produces no head wave (the hidden layer problem), so its depth is wrongly calculated."),
        QUIZ("Why do S waves not pass through the outer core?",
             ["The outer core is too dense", "The outer core has zero rigidity because it is liquid", "S waves are absorbed by iron", "S waves are reflected by the Moho"], 1,
             "With shear modulus zero, the S-wave velocity is zero: a liquid cannot transmit shear.",
             hint="Look at the formula for v_S.",
             feedback=["Higher density would slow S waves, not stop them.", "", "Composition alone does not stop shear waves; the solid inner core is also iron and does transmit them.", "The Moho is the base of the crust, thousands of kilometres above the core."]),
        QUIZ("On a two-layer travel-time graph, the refracted arrivals have a gradient of 0.125 s/km. What is the velocity of the lower layer?",
             ["0.125 km/s", "6.0 km/s", "8.0 km/s", "12.5 km/s"], 2,
             "Gradient = 1/v2, so v2 = 1/0.125 = 8.0 km/s.",
             hint="Gradient of a distance-time line is time divided by distance.",
             feedback=["The gradient is the reciprocal of velocity, not the velocity.", "That would be a gradient of 0.167 s/km.", "", "You may have multiplied by 100."]),
        TIP("Exam link: Paper 1 often tests which waves cross liquids, which waves are transverse and the depths of discontinuities. Paper 2 essays ask you to explain how seismic evidence shows the internal structure and to contrast oceanic and continental crust. Paper 3 may give travel-time data to plot and interpret."),
        H("Practice"),
        PQ("State four differences between oceanic and continental crust.",
           "Oceanic crust is thinner (about 5-10 km against 30-70 km); denser (about 3.0 g/cm3 against about 2.7); basaltic and gabbroic and fairly uniform, while continental crust is varied, with granite and metamorphic rocks; younger (no older than about 200 million years, while continental rocks reach about 4 billion years); and it lacks the Conrad discontinuity and carries symmetrical magnetic stripes."),
        PQ(r"A refraction survey gives $v_1 = 6.2$ km/s, $v_2 = 8.1$ km/s and a crossover distance of 150 km. Calculate the crustal thickness.",
           r"From $x_c = 2h\sqrt{(v_2 + v_1)/(v_2 - v_1)}$: $h = \dfrac{x_c}{2}\sqrt{\dfrac{v_2 - v_1}{v_2 + v_1}} = 75\sqrt{\dfrac{1.9}{14.3}} = 75 \times 0.3645 = 27$ km."),
        PQ("Explain how seismology shows that the outer core is liquid and the inner core solid.",
           "S waves need rigidity; they stop at about 2 890 km and are absent beyond about 103 degrees from the focus, so the outer core has no rigidity: it is liquid. P waves slow sharply and are refracted there, forming the P shadow zone. At about 5 150 km P velocity increases again and some waves are interpreted as converting to S waves in the inner core, which shows the inner core is solid."),
        PQ("Give two limitations of interpreting a two-layer refraction survey.",
           "It assumes flat, uniform layers; a dipping interface gives false velocities unless the survey is reversed. A low-velocity layer beneath a faster one produces no head wave, so it is missed and the depth to deeper layers is wrongly calculated."),
        SUM(r"$v_P$ depends on bulk and shear moduli and density; $v_S = \sqrt{\mu/\rho}$, so S waves cannot cross liquids.",
            r"Critical angle: $\sin i_c = v_1/v_2$; the head wave travels along the interface at $v_2$.",
            r"Travel-time graph: gradients $1/v_1$ and $1/v_2$, intercept $t_i = 2h\cos i_c/v_1$, crossover distance beyond which the head wave arrives first.",
            r"Reflection: depth = velocity times two-way time divided by 2.",
            "Moho, low-velocity zone, 410 and 660 km steps, Gutenberg (about 2 890 km) and Lehmann (about 5 150 km) discontinuities, and the P and S shadow zones."),
    ],
))

# ------------------------------------------------------------------ 2. Gravity and isostasy
LESSONS.append(lesson(
    module=M1,
    topic="Gravity and isostasy",
    title="Gravity anomalies and isostasy: Airy, Pratt and isostatic rebound",
    slug="gyl1-gravity-isostasy",
    minutes=25,
    summary="Gravity surveys correct readings for latitude, height and rock mass to give free-air and Bouguer anomalies. Isostasy explains why mountains have deep roots, why oceans are low and why land rises after ice or rock is removed.",
    objectives=[
        "Calculate free-air and Bouguer anomalies from a gravity reading",
        "Interpret positive and negative Bouguer anomalies in terms of rock density",
        "Explain and compare the Airy and Pratt models of isostasy and calculate a mountain root",
        "Explain isostatic rebound after deglaciation and erosion",
    ],
    key_concepts=["Gravity anomaly", "Milligal", "Free-air correction", "Bouguer correction", "Isostasy", "Airy model", "Pratt model", "Depth of compensation", "Isostatic rebound"],
    blocks=[
        H("Introduction"),
        T("Mount Cameroon rises about 4 000 m above the sea. Such a heavy load should pull the ground down, and the extra mass should make gravity stronger on its summit. "
          "Careful measurements of gravity, corrected in the right way, tell geologists what lies below: dense intrusions, light granite, thick sediments or deep crustal roots."),
        D(r"**Gravitational acceleration** at the surface is about 9.8 m/s$^2$. Geophysicists measure small differences in it with a **gravimeter**. "
          r"The unit is the **milligal**: 1 mGal = $10^{-5}$ m/s$^2$, about one millionth of normal gravity. A **gravity anomaly** is the difference between "
          r"the corrected measured value and the value expected for a uniform Earth at that latitude.", title="Gravity and anomalies"),
        H("Corrections and anomalies"),
        KEY("Corrections to a reading", "Each correction removes an effect that has nothing to do with the rocks below.", cards=[
            ["Latitude", "Gravity is larger at the poles (nearer the centre, less spin). Subtract the normal (theoretical) gravity for the station's latitude."],
            ["Free-air", r"A station higher above sea level is farther from the centre, so gravity is lower. Add 0.3086 mGal for each metre of height."],
            ["Bouguer", r"The slab of rock between the station and sea level adds attraction. Subtract $2\pi G\rho h$, which is 0.0419 times the density in g/cm$^3$, in mGal per metre."],
            ["Terrain", "Nearby hills and valleys both reduce the reading; a terrain correction is added in rugged areas."],
        ]),
        F(r"\text{FAA} = g_{obs} - g_n + 0.3086h \qquad \text{BA} = \text{FAA} - 0.0419\rho h", title="Free-air and Bouguer anomalies (h in m, rho in g/cm3, anomalies in mGal)"),
        EX("Worked example 1: free-air and Bouguer anomalies", intro="Teaching values: a station at 400 m reads 978 150.0 mGal. Normal gravity at its latitude is 978 220.0 mGal. Use a rock density of 2.67 g/cm3.", steps=[
            S("Free-air correction", math=r"0.3086 \times 400 = 123.4 \text{ mGal}"),
            S("Free-air anomaly", math=r"978\,150.0 - 978\,220.0 + 123.4 = +53.4 \text{ mGal}"),
            S("Bouguer correction", math=r"0.0419 \times 2.67 \times 400 = 44.8 \text{ mGal}"),
            S("Bouguer anomaly", math=r"53.4 - 44.8 = +8.6 \text{ mGal}"),
            S("Interpret", text="A small positive Bouguer anomaly suggests slightly denser rock than average below the station."),
        ]),
        T("A **positive Bouguer anomaly** shows excess mass at depth: a gabbro intrusion, an ore body, or thin crust with dense mantle close to the surface, as under the oceans. "
          "A **negative Bouguer anomaly** shows a mass deficit: a granite pluton, a salt dome, a thick sedimentary basin or the low-density root under a mountain range."),
        MISTAKE("Mixing up the corrections", "The free-air correction is **added** (the station is too far from the centre). The Bouguer correction is **subtracted** (the rock slab added extra pull). Learn the reason, not just the sign."),
        H("Isostasy"),
        D("**Isostasy** is the state of gravitational balance in which the lithosphere floats on the denser, slowly flowing asthenosphere, so that every column of rock has the same mass above a **depth of compensation**.", title="Isostasy"),
        IMG("algyl1-isostasy.svg", alt="Left: Airy model, blocks of equal density with the tallest block having the deepest root. Right: Pratt model, blocks of different density standing on one flat base at the depth of compensation, the least dense block standing highest",
            caption="Figure 1. Airy and Pratt models of isostasy."),
        KEY("Two classical models", "Both balance mass in columns; they differ in how.", cards=[
            ["Airy", "Crust of one density, different thickness. High mountains have deep **roots** that push into the mantle, like a thick block of wood floating deeper in water."],
            ["Pratt", "Crust of different densities over one level base. High regions are made of lighter rock; low regions of denser rock."],
        ]),
        F(r"r = \dfrac{h\,\rho_c}{\rho_m - \rho_c}", title="Airy root under a mountain of height h"),
        EX("Worked example 2: the root of a mountain range", intro=r"A mountain range stands 3.0 km above the surrounding plain. Crust density 2.8 g/cm$^3$, mantle density 3.3 g/cm$^3$, normal crust 35 km thick. Use the Airy model.", steps=[
            S("Root", math=r"r = \dfrac{3.0 \times 2.8}{3.3 - 2.8} = \dfrac{8.4}{0.5} = 16.8 \text{ km}"),
            S("Total crustal thickness", math=r"35 + 3.0 + 16.8 = 54.8 \text{ km}"),
            S("Check with seismology", text="Refraction surveys do show the Moho much deeper under young mountain belts, which supports the Airy model there."),
        ]),
        EX("Worked example 3: Pratt density", intro=r"Pratt model: the depth of compensation is 100 km below sea level and a column standing at sea level has density 2.84 g/cm$^3$. What density must a column standing 2.0 km above sea level have?", steps=[
            S("Equal mass in each column", math=r"\rho_h (100 + 2.0) = 2.84 \times 100"),
            S("Solve", math=r"\rho_h = \dfrac{284}{102} = 2.78 \text{ g/cm}^3"),
        ]),
        H("Isostatic adjustment"),
        T(r"When a load is added, the lithosphere sinks; when a load is removed, it rises (**isostatic rebound**). An ice sheet 2.0 km thick (density 0.9 g/cm$^3$) "
          r"depresses the crust by about $2.0 \times 0.9 / 3.3 = 0.55$ km. Scandinavia and northern Canada are still rising today after their ice sheets melted about 10 000 years ago, "
          r"which is why raised beaches are found there. Erosion of a mountain also triggers uplift: remove 1 km of rock and the column rebounds by about $1 \times 2.8/3.3 = 0.85$ km, "
          r"so the surface drops by only about 0.15 km. This is why old mountain belts take so long to wear down."),
        T("**Evaluation.** Neither model is complete. The Airy model fits young fold mountains with seismically proven roots. The Pratt model fits mid-ocean ridges, which stand high because "
          "the hot mantle under them is less dense. Small loads such as a single volcano are held up partly by the strength of the lithosphere, which bends (flexural isostasy). "
          "Large free-air anomalies show regions not in balance, for example deep ocean trenches."),
        QUIZ("A survey across a granite pluton surrounded by schist would show",
             ["a positive Bouguer anomaly over the granite", "a negative Bouguer anomaly over the granite", "no anomaly because both are crystalline", "a free-air anomaly only"], 1,
             "Granite (about 2.65 g/cm3) is less dense than schist, so there is a mass deficit and a negative anomaly.",
             hint="Compare the densities.",
             feedback=["A positive anomaly needs denser rock, such as gabbro.", "", "Crystalline rocks still differ in density.", "The Bouguer anomaly is the one that reflects density contrasts below the station."]),
        QUIZ("In the Airy model a plateau 2.0 km high, with crust density 2.8 and mantle density 3.3 g/cm3, has a root of",
             ["2.0 km", "5.6 km", "11.2 km", "16.8 km"], 2,
             "r = 2.0 x 2.8 / 0.5 = 11.2 km.",
             hint="Use r = h rho_c / (rho_m - rho_c).",
             feedback=["The root is much deeper than the height.", "You divided by 1 instead of 0.5.", "", "That is the root for a 3.0 km mountain."]),
        TIP("Exam link: Paper 1 tests the meaning of anomalies and the two models. Paper 2 can ask you to explain isostasy with labelled diagrams and evidence (mountain roots, rebound). Show the formula and units in every calculation."),
        H("Practice"),
        PQ(r"A plateau stands 1.5 km above sea level. Using the Airy model with crust density 2.7 g/cm$^3$ and mantle density 3.3 g/cm$^3$, calculate its root.",
           r"$r = \dfrac{1.5 \times 2.7}{3.3 - 2.7} = \dfrac{4.05}{0.6} = 6.75$ km, about 6.8 km."),
        PQ("Explain why land in Scandinavia is rising today and give one piece of field evidence.",
           "During the last glaciation an ice sheet up to a few kilometres thick loaded the crust and pushed it down into the asthenosphere. When the ice melted the load was removed and the crust is slowly rising back towards balance (isostatic rebound), because the mantle flows back only slowly. Evidence: raised beaches and old shorelines now above sea level, and tide-gauge and GPS measurements of uplift."),
        PQ("Compare the Airy and Pratt models of isostasy and say where each fits best.",
           "Both say that columns of lithosphere have equal mass above a depth of compensation. Airy: uniform density, varying thickness, so mountains have roots; supported by seismic evidence of thick crust under young mountain belts. Pratt: varying density over a level base, so high regions are made of less dense rock; fits mid-ocean ridges, where hot, less dense mantle holds the ridge up. Real regions combine both, and small loads are partly supported by the flexural strength of the lithosphere."),
        PQ("A 1 km layer of rock is eroded from an isostatically balanced mountain (crust 2.8, mantle 3.3 g/cm3). By how much does the surface height actually fall? Explain.",
           r"Removing the load causes rebound of $1 \times 2.8/3.3 = 0.85$ km, so the surface falls by only $1 - 0.85 = 0.15$ km. Erosion is partly cancelled by uplift, which is why deeply eroded old mountain belts expose rocks that were once deep in the crust."),
        SUM("Gravity anomalies are measured in milligals after latitude, free-air, Bouguer and terrain corrections.",
            r"$\text{FAA} = g_{obs} - g_n + 0.3086h$; $\text{BA} = \text{FAA} - 0.0419\rho h$.",
            "Positive Bouguer anomalies mean dense rock below; negative ones mean light rock such as granite, salt, sediment or a mountain root.",
            r"Airy: same density, roots under mountains, $r = h\rho_c/(\rho_m - \rho_c)$. Pratt: different densities, level base.",
            "Removing ice or rock causes isostatic rebound; raised beaches are evidence."),
    ],
))

# ------------------------------------------------------------------ 3. Geomagnetism
LESSONS.append(lesson(
    module=M1,
    topic="Geomagnetism and palaeomagnetism",
    title="The Earth's magnetic field, remanent magnetism and magnetic stripes",
    slug="gyl1-geomagnetism-palaeomagnetism",
    minutes=24,
    summary="The geodynamo makes a dipole field that rocks record as they form. Inclination gives palaeolatitude, polar wander paths show that continents moved, and symmetrical magnetic stripes give the rate of seafloor spreading.",
    objectives=[
        "Describe the main features of the geomagnetic field and its origin in the outer core",
        "Explain how rocks acquire remanent magnetism (thermal, detrital and chemical)",
        "Calculate palaeolatitude from inclination and interpret apparent polar wander paths",
        "Explain magnetic stripes and use them to calculate spreading rates",
    ],
    key_concepts=["Geodynamo", "Declination", "Inclination", "Curie temperature", "Remanent magnetism", "Palaeolatitude", "Apparent polar wander path", "Magnetic reversal", "Magnetic stripes"],
    blocks=[
        H("Introduction"),
        T("A compass in Bamenda points almost due north and its needle, if free to tilt, dips only slightly, because Cameroon is near the magnetic equator. "
          "In Norway the same needle would dip steeply. Rocks that formed long ago remember the direction and dip of the field at the time and place they formed. "
          "Reading this memory proved that continents move and that the ocean floor spreads."),
        D("The **geomagnetic field** is close to the field of a bar magnet (a dipole) at the centre of the Earth, tilted by about 10 degrees from the rotation axis. "
          "It is described by **declination** (the angle between magnetic north and true north), **inclination** (the dip of the field below the horizontal) "
          "and **intensity** (strength, roughly 25 000 to 65 000 nanotesla at the surface, strongest near the poles).", title="The field"),
        T("The field is generated by the **geodynamo**: convection of liquid iron in the outer core, organised by the Earth's rotation, produces electric currents and so a magnetic field. "
          "This is why the field changes slowly with time (**secular variation**) and why it can **reverse** polarity. Averaged over a few thousand years, the magnetic poles lie close to the geographic poles."),
        H("How rocks record the field"),
        KEY("Remanent magnetism", "Magnetic minerals such as magnetite and haematite lock in the field direction.", cards=[
            ["Thermoremanent (TRM)", "Lava or intrusions cool through the **Curie temperature** (about 580 degrees C for magnetite). Below it the magnetic domains align with the field and are frozen in. The strongest and most reliable record."],
            ["Detrital (DRM)", "Magnetic grains settling in still water rotate like tiny compasses before burial. Weaker; found in red beds, lake and deep-sea sediments."],
            ["Chemical (CRM)", "New magnetic minerals grow below the Curie temperature during diagenesis or weathering and record the field at that later time."],
        ]),
        H("Inclination and palaeolatitude"),
        F(r"\tan I = 2\tan\lambda", title="Dipole equation (I = inclination, lambda = latitude)"),
        T(r"Inclination is $0^{\circ}$ at the magnetic equator and $90^{\circ}$ at the magnetic poles. Positive (downward) inclination means the northern hemisphere; "
          r"negative (upward) means the southern hemisphere for normal polarity. Measuring $I$ in an old rock gives its **palaeolatitude**, the latitude where it formed."),
        EX("Worked example 1: palaeolatitude", intro="A basalt flow has a remanent inclination of 30 degrees (downwards). At what latitude did it form?", steps=[
            S("Rearrange", math=r"\tan\lambda = \dfrac{\tan I}{2}"),
            S("Substitute", math=r"\tan\lambda = \dfrac{\tan 30^{\circ}}{2} = \dfrac{0.577}{2} = 0.289"),
            S("Answer", math=r"\lambda = 16.1^{\circ}\text{ N}"),
        ], check=r"2\tan 16.1^{\circ} = 0.577 = \tan 30^{\circ}"),
        EX("Worked example 2: a lava forming today near Douala", intro="Douala lies at about 4 degrees N. What inclination would a lava cooling there today record (dipole field)?", steps=[
            S("Use the equation", math=r"\tan I = 2\tan 4^{\circ} = 2 \times 0.0699 = 0.140"),
            S("Answer", math=r"I = 8.0^{\circ}", text="A shallow dip, as expected near the equator. Local field irregularities make real values differ a little."),
        ]),
        T("Palaeomagnetism gives latitude and the direction to the pole, but **not longitude**: a continent can be anywhere around a circle of latitude."),
        D("If the continents were fixed, the pole positions calculated from rocks of different ages would trace a path called an **apparent polar wander path (APWP)**. "
          "The paths from Europe and North America have the same shape but are separated by about the width of the Atlantic. When the Atlantic is closed, the two paths fit. "
          "So the pole did not wander: the continents moved.", title="Apparent polar wander paths"),
        H("Reversals and magnetic stripes"),
        T("Lava sequences show that the field has reversed many times. The present normal-polarity interval (the Brunhes chron) began about 0.78 million years ago. "
          "Dated reversals form the **geomagnetic polarity timescale**."),
        IMG("algyl1-magstripes.svg", alt="Map view of the ocean floor: a dashed ridge axis in the centre with black (normal) and white (reversed) stripes that form a mirror image on the two sides; a distance scale from 0 to 80 km",
            caption="Figure 1. Magnetic stripes are symmetrical about the ridge axis (simplified pattern)."),
        T("Basalt erupted at a mid-ocean ridge acquires TRM in the current field direction, then is split and carried away on both sides. Alternating bands of normal and reversed "
          "polarity therefore lie **parallel to the ridge** and **symmetrical** about it, getting older away from the axis. Vine and Matthews (and Morley, independently) used this in 1963 "
          "as strong evidence for seafloor spreading."),
        EX("Worked example 3: spreading rate", intro="The boundary of the present normal band (0.78 million years old) lies 23.4 km from the ridge axis on each side. Find the half and full spreading rates.", steps=[
            S("Half rate", math=r"\dfrac{23.4 \text{ km}}{0.78 \text{ Myr}} = 30 \text{ km/Myr} = 30 \text{ mm/yr} = 3.0 \text{ cm/yr}"),
            S("Full rate", text="Both plates move apart, so the full rate is twice the half rate: 6.0 cm/yr."),
        ]),
        MISTAKE("Explaining the theory instead of the evidence", "When asked how stripes support seafloor spreading, describe the stripes (parallel to the ridge, symmetrical, older outwards) and explain why that pattern is expected from new crust recording reversals. Do not just retell the whole theory."),
        MISTAKE("Saying that fossils carry the magnetism","Remanence is carried by magnetic minerals (magnetite, haematite), not by fossils."),
        MISTAKE("Thinking a reversal moves the continents", "A reversal swaps north and south magnetic poles worldwide. Polar wander paths, not reversals, show continental movement."),
        T("**Evaluation.** Palaeomagnetic results assume the field averages to a geocentric axial dipole and that the rock has not been reheated or chemically altered since it formed. "
          "Folded rocks must be restored to horizontal before the direction is used. Several samples from several sites are averaged."),
        QUIZ("A lava has a remanent inclination of 0 degrees. Where did it form?",
             ["At the magnetic equator", "At a magnetic pole", "At 45 degrees latitude", "It cannot be known"], 0,
             "tan 0 = 0, so latitude = 0: the magnetic equator.",
             hint="Use tan I = 2 tan latitude.",
             feedback=["", "At a pole the field is vertical: I = 90 degrees.", "At 45 degrees the inclination is about 63 degrees.", "Inclination gives latitude directly."]),
        QUIZ("Why are magnetic stripes symmetrical about a mid-ocean ridge?",
             ["The field is stronger at the ridge", "New crust forms at the ridge and moves away equally on both sides while recording reversals", "Sediments are thicker on both sides", "Transform faults copy the pattern"], 1,
             "Each band forms at the axis, is split and carried away on both plates, so the sequence is mirrored.",
             hint="Where does new crust form, and where does it go?",
             feedback=["Field strength does not create a symmetrical sequence of polarities.", "", "Sediments mask the stripes; they do not make them.", "Transform faults offset the stripes; they do not create them."]),
        TIP("Exam link: Paper 1 tests remanence, Curie temperature and the meaning of stripes. Paper 2 essays ask for palaeomagnetic evidence for continental drift and seafloor spreading; the Board's 2023 report notes that many candidates explained the theory without the evidence."),
        H("Practice"),
        PQ("A sandstone records an upward inclination of 20 degrees with normal polarity. Calculate its palaeolatitude and say which hemisphere.",
           r"$\tan\lambda = \tan 20^{\circ}/2 = 0.364/2 = 0.182$, so $\lambda = 10.3^{\circ}$. Upward (negative) inclination with normal polarity means the southern hemisphere: about 10 degrees S."),
        PQ("A reversal boundary 1.5 million years old lies 45 km from a ridge axis. Calculate the half spreading rate in mm/yr.",
           r"$45 \text{ km} / 1.5 \text{ Myr} = 30$ km/Myr. 1 km/Myr = 1 mm/yr, so the half rate is 30 mm/yr (full rate 60 mm/yr)."),
        PQ("Explain how apparent polar wander paths show that Europe and North America have moved apart.",
           "Poles calculated from rocks of each age on each continent form a path. The two paths have the same shape but do not coincide, which is impossible if there is only one pole at any time and the continents had not moved. Closing the Atlantic brings the paths together, so the continents were joined and have since separated."),
        SUM("The field is a tilted dipole made by the geodynamo in the liquid outer core; it shows secular variation and reversals.",
            "Rocks record the field as TRM (cooling through the Curie temperature), DRM (settling grains) or CRM (new mineral growth).",
            r"$\tan I = 2\tan\lambda$ gives palaeolatitude, but not longitude.",
            "Apparent polar wander paths of different continents match only if the continents moved.",
            "Magnetic stripes are parallel to and symmetrical about ridges; distance divided by age gives the spreading rate."),
    ],
))

# ------------------------------------------------------------------ 4. Heat flow
LESSONS.append(lesson(
    module=M1,
    topic="Heat flow",
    title="Heat flow: the Earth's internal heat and the geothermal gradient",
    slug="gyl1-heat-flow",
    minutes=22,
    summary="Internal heat from radioactive decay and the Earth's formation escapes by conduction, convection and magma. Heat flow equals thermal conductivity times the geothermal gradient, and it varies with tectonic setting and the age of oceanic crust.",
    objectives=[
        "Name the sources of the Earth's internal heat and the ways heat is transferred",
        "Calculate heat flow, geothermal gradient and temperature at depth",
        "Explain the pattern of heat flow across ridges, trenches, shields and volcanic regions",
        "Explain why heat flow and ocean depth change with the age of oceanic lithosphere",
    ],
    key_concepts=["Heat flow", "Geothermal gradient", "Thermal conductivity", "Radiogenic heat", "Conduction", "Convection", "Geotherm"],
    blocks=[
        H("Introduction"),
        T("Deep mines are hot: the deeper you go, the warmer the rock. That heat comes from inside the Earth and drives volcanoes, plate motion and the geodynamo. "
          "Geologists measure how much heat leaves each square metre of ground, and the pattern tells them where the lithosphere is thin and hot or thick and cold."),
        D(r"**Heat flow** $q$ is the rate at which heat escapes through each square metre of the surface, measured in milliwatts per square metre (mW/m$^2$). "
          r"The **geothermal gradient** $dT/dz$ is the rise in temperature with depth, in degrees C per km. **Thermal conductivity** $k$ (W m$^{-1}$ K$^{-1}$) is how easily a rock conducts heat.", title="Definitions"),
        F(r"q = k\,\dfrac{dT}{dz}", title="Heat flow by conduction"),
        H("Where the heat comes from"),
        KEY("Sources of internal heat", "Textbooks give different shares for each source; check your textbook.", cards=[
            ["Radiogenic heat", "Decay of long-lived isotopes uranium-238, uranium-235, thorium-232 and potassium-40. They are concentrated in the continental crust, especially in granite."],
            ["Primordial heat", "Heat left from the accretion of the Earth and the sinking of iron to form the core."],
            ["Core crystallisation", "Latent heat released as the inner core slowly freezes."],
        ]),
        KEY("How heat moves", "Different processes dominate in different layers.", cards=[
            ["Conduction", "Through the rigid lithosphere, atom to atom. Slow."],
            ["Convection", "In the mantle (solid but slowly flowing) and the liquid outer core. Hot material rises, cold sinks. Efficient."],
            ["Advection by magma", "Magma carries heat upwards quickly at ridges, hotspots and arcs."],
        ]),
        EX("Worked example 1: heat flow from a borehole", intro="In a borehole the temperature rises by 25 degrees C per km. The granite has a thermal conductivity of 2.5 W/m/K. Calculate the heat flow.", steps=[
            S("Convert the gradient to K per metre", math=r"25 \text{ K/km} = 0.025 \text{ K/m}"),
            S("Heat flow", math=r"q = 2.5 \times 0.025 = 0.0625 \text{ W/m}^2"),
            S("Answer", math=r"q = 62.5 \text{ mW/m}^2", text="Close to a typical continental value."),
        ]),
        EX("Worked example 2: temperature at depth", intro="Heat flow is 90 mW/m2 through rock with k = 3.0 W/m/K. The surface temperature is 27 degrees C. Estimate the temperature at 2 km depth.", steps=[
            S("Gradient", math=r"\dfrac{dT}{dz} = \dfrac{q}{k} = \dfrac{0.090}{3.0} = 0.030 \text{ K/m} = 30^{\circ}\text{C/km}"),
            S("Temperature", math=r"T = 27 + 30 \times 2 = 87^{\circ}\text{C}"),
        ]),
        H("The global pattern"),
        T("Typical heat flow is roughly 65 mW/m2 on continents and about 100 mW/m2 in oceans (approximate averages; check your textbook). "
          "Heat flow is **high** at mid-ocean ridges, continental rifts such as the East African Rift, hotspots and volcanic arcs, where hot material is close to the surface. "
          "It is **low** over old continental shields such as the Congo Craton, over old ocean floor, and at ocean trenches, where cold lithosphere sinks."),
        IMG("algyl1-heatflow.svg", alt="Graph of heat flow against age of oceanic lithosphere: very high near zero age, falling quickly and then slowly to below 50 mW per square metre at 120 million years",
            caption="Figure 1. Heat flow falls with the age of oceanic lithosphere (approximate cooling-plate curve)."),
        T(r"New oceanic lithosphere is hot. As it moves away from the ridge it cools, thickens and becomes denser, so it sinks. Two widely used approximations are "
          r"$q \approx 480/\sqrt{t}$ mW/m$^2$ and ocean depth $d \approx 2500 + 350\sqrt{t}$ m, with $t$ the age in millions of years (textbooks use slightly different constants). "
          r"This cooling explains why ridges stand high and why old ocean floor is deep."),
        EX("Worked example 3: 25-million-year-old ocean floor", intro="Use the approximations above for oceanic lithosphere 25 million years old.", steps=[
            S("Heat flow", math=r"q \approx \dfrac{480}{\sqrt{25}} = 96 \text{ mW/m}^2"),
            S("Depth", math=r"d \approx 2500 + 350\sqrt{25} = 4250 \text{ m}"),
            S("Compare", text="At 100 million years, q is about 48 mW/m2 and depth about 6 000 m: older floor is cooler and deeper."),
        ]),
        MISTAKE("Mixing units", "Heat flow is usually in mW/m2 but the formula with k in W/m/K and gradient in K/m gives W/m2. Multiply by 1 000 to get mW/m2. Convert degrees per km into degrees per metre first."),
        MISTAKE("Extending the surface gradient to the centre", "25 degrees C per km down to the core would give over 70 000 degrees C, which is impossible. Below the lithosphere the mantle convects, and the temperature rises only slowly with depth."),
        T("**Evaluation.** Measured heat flow can be disturbed by groundwater circulation (common near ridges, where much heat escapes through hydrothermal vents and is missed by probes), "
          "by recent climate change at the surface and by differences in rock conductivity. Several measurements are averaged."),
        QUIZ("Which setting has the lowest heat flow?",
             ["A mid-ocean ridge", "A continental rift", "An old continental shield", "A volcanic arc"], 2,
             "Old shields have thick, cold lithosphere and have lost much of their radiogenic heat.",
             hint="Think about thick, cold, ancient lithosphere.",
             feedback=["Ridges have the highest heat flow because hot mantle rises there.", "Rifts have thin lithosphere and rising magma.", "", "Arcs are heated by rising magma."]),
        QUIZ("Why does the ocean floor get deeper away from a mid-ocean ridge?",
             ["Sediment presses it down", "The lithosphere cools, contracts and becomes denser, so it sinks", "Trenches pull it down", "The mantle under it melts"], 1,
             "Cooling increases density, and isostasy makes the denser, thicker plate ride lower.",
             hint="Link heat flow, density and isostasy.",
             feedback=["Sediment is thin compared with the depth change and is not the main cause.", "", "Slab pull acts at the trench edge; depth increases smoothly far from trenches.", "Melting would make it lighter and higher."]),
        TIP("Exam link: Paper 1 asks about heat sources and where heat flow is high or low. Paper 2 may combine heat flow with plate tectonics, mantle convection or ocean floor topography. Always state units."),
        H("Practice"),
        PQ("Calculate the heat flow where the gradient is 40 degrees C per km and k = 2.0 W/m/K.",
           r"$q = 2.0 \times 0.040 = 0.080$ W/m$^2$ = 80 mW/m$^2$."),
        PQ("A geothermal well needs water at 200 degrees C. The surface temperature is 25 degrees C and the gradient is 35 degrees C per km. How deep must it be drilled?",
           r"Temperature rise needed = 175 degrees C. Depth = 175 / 35 = 5.0 km."),
        PQ("Describe and explain the variation of heat flow across an ocean from a mid-ocean ridge to a trench.",
           "Heat flow is highest at the ridge, where hot asthenosphere rises and magma is intruded. It falls with distance (roughly as one over the square root of age) because the lithosphere cools and thickens as it ages. It is lowest near the trench, where old, cold lithosphere bends down and sinks. Close to the ridge, measured values are scattered and often too low because seawater circulating through the crust removes heat."),
        SUM(r"Heat flow $q = k\,dT/dz$, measured in mW/m$^2$.",
            "Heat sources: radioactive decay of U, Th and K-40, primordial heat, and core crystallisation.",
            "Conduction dominates in the lithosphere; convection in the mantle and outer core; magma advects heat upwards.",
            "Heat flow is high at ridges, rifts, hotspots and arcs; low on old shields, old ocean floor and trenches.",
            "Oceanic lithosphere cools with age, so heat flow falls and ocean depth increases away from ridges."),
    ],
))

# ------------------------------------------------------------------ 5. Plate tectonics and the Wilson cycle
LESSONS.append(lesson(
    module=M1,
    topic="Plate tectonics and the Wilson cycle",
    title="Plate boundaries, driving forces and the Wilson cycle",
    slug="gyl1-plate-tectonics-wilson-cycle",
    minutes=25,
    summary="Rigid lithospheric plates move over the asthenosphere, driven mainly by slab pull and ridge push. Oceans open and close in a Wilson cycle, from continental rift to young and mature ocean, subduction, closure and continental collision.",
    objectives=[
        "Describe the lithosphere and the three types of plate boundary with their features and earthquakes",
        "Evaluate the forces that drive plates, and calculate plate speeds and Benioff zone dips",
        "Describe the six stages of the Wilson cycle with modern examples",
        "Relate the Cameroon margin and the Benue Trough to the opening of the South Atlantic",
    ],
    key_concepts=["Lithosphere", "Asthenosphere", "Constructive boundary", "Destructive boundary", "Conservative boundary", "Benioff zone", "Slab pull", "Ridge push", "Hotspot", "Wilson cycle", "Aulacogen"],
    blocks=[
        H("Introduction"),
        T("About 130 to 100 million years ago, in the Cretaceous, Africa and South America split apart and the South Atlantic Ocean opened. "
          "The coastal basins of Cameroon, such as the Douala basin, formed along the new continental margin. Plate tectonics links these events: "
          "oceans are born, grow, shrink and die, and the cycle repeats."),
        D("A **plate** is a rigid slab of **lithosphere** (crust plus uppermost mantle, roughly 100 km thick but thinner at ridges) that moves over the weak, partly molten **asthenosphere**. "
          "Most earthquakes, volcanoes and mountain building happen at plate boundaries.", title="Plates"),
        H("Plate boundaries"),
        KEY("Three kinds of boundary", "Learn the motion, features and earthquakes of each.", cards=[
            ["Constructive (divergent)", "Plates move apart; mantle rises and partly melts to make new oceanic crust. Mid-ocean ridges with a central rift valley, basaltic volcanism, high heat flow, shallow earthquakes. On land: rift valleys such as East Africa."],
            ["Destructive (convergent)", "Ocean-ocean: one plate subducts, giving a trench and an island arc (Japan). Ocean-continent: trench and an Andean-type volcanic mountain belt. Continent-continent: neither subducts easily; the crust thickens into fold mountains (Himalaya). Shallow, intermediate and deep earthquakes."],
            ["Conservative (transform)", "Plates slide past each other; crust is neither made nor destroyed. Transform faults offset ridges; on land, the San Andreas Fault. Shallow earthquakes, no volcanism."],
        ]),
        D("A **Benioff zone** (Wadati-Benioff zone) is the inclined band of earthquake foci that marks a subducting slab, from near the trench down to about 700 km. Its dip is found from the depth and horizontal distance of foci.", title="Benioff zone"),
        EX("Worked example 1: dip of a Benioff zone", intro="An earthquake focus lies 300 km deep and 400 km horizontally from the trench, on the line of the slab. Find the dip of the slab.", steps=[
            S("Tangent of the dip", math=r"\tan\theta = \dfrac{300}{400} = 0.75"),
            S("Dip", math=r"\theta = 36.9^{\circ}"),
        ]),
        H("What drives the plates?"),
        KEY("Driving forces", "Most geologists now think the plates are largely driven by their own weight.", cards=[
            ["Slab pull", "Cold, dense subducting lithosphere sinks and pulls the rest of the plate. Probably the largest force."],
            ["Ridge push", "Lithosphere slides down the elevated flanks of a ridge under gravity."],
            ["Mantle convection and drag", "Convection currents carry heat and may drag the base of plates, but the exact coupling is debated."],
        ]),
        T("**Evaluation.** Plates attached to long subducting slabs, such as the Pacific plate, move fastest (several cm per year), while plates with little subducting edge, such as the African plate, move slowly. "
          "This supports slab pull. Ridges are not always above upwelling convection cells and can migrate, which suggests ridges are passive cracks rather than the main drivers."),
        H("Hotspots and plate speeds"),
        T("A **hotspot** is a long-lived source of magma that is fixed relative to the moving plate, possibly fed by a mantle plume. A plate moving over it leaves a chain of volcanoes that get older away from the active one."),
        EX("Worked example 2: plate speed from a hotspot chain", intro="A volcano in a hotspot chain is 1 200 km from the active hotspot and its lavas are 15 million years old. Find the plate speed.", steps=[
            S("Speed", math=r"\dfrac{1200 \text{ km}}{15 \text{ Myr}} = 80 \text{ km/Myr}"),
            S("Convert", math=r"80 \text{ km/Myr} = 80 \text{ mm/yr} = 8 \text{ cm/yr}"),
        ]),
        T("The **Cameroon Volcanic Line** runs from the islands of the Gulf of Guinea through Mount Cameroon to the Adamawa plateau. It does not show a simple age progression like a hotspot chain, "
          "and its origin (plume, reactivated old shear zones, or small-scale mantle convection at the edge of the craton) is still debated. Check your textbook for the explanation it prefers."),
        H("The Wilson cycle"),
        D("The **Wilson cycle**, named after J. Tuzo Wilson, is the repeated opening and closing of ocean basins: a continent rifts, an ocean opens and widens, subduction begins, the ocean closes, and the continents collide to form a mountain belt, which may later rift again.", title="Wilson cycle"),
        IMG("algyl1-wilson.svg", alt="Six boxes in a cycle: 1 embryonic continental rift, East African Rift; 2 young narrow ocean, Red Sea; 3 mature wide ocean, Atlantic; 4 declining with subduction, Pacific; 5 terminal, Mediterranean; 6 suturing collision, Himalaya; arrow back to a new rift",
            caption="Figure 1. Stages of the Wilson cycle with modern examples."),
        KEY("What happens at each stage", "Rocks typical of each stage help you recognise ancient cycles.", cards=[
            ["1-2 Rifting and young ocean", "Doming, rift valleys, alkaline volcanism, continental red beds and evaporites in narrow seas; first oceanic crust."],
            ["3 Mature ocean", "Wide ocean with passive margins: thick shelf sandstones and limestones on both sides."],
            ["4-5 Subduction and closure", "Trenches, island arcs, andesite volcanism, granite batholiths, ophiolites (slices of ocean floor) thrust onto land."],
            ["6 Collision", "Fold mountains, thrusts, regional metamorphism; the join (suture) is marked by ophiolites."],
        ]),
        T("Some rifts fail. A **failed rift** (aulacogen) is an arm of a rift that stopped opening. The Benue Trough of Nigeria and northern Cameroon is widely described as the failed arm "
          "of the rift system that opened the South Atlantic in the Cretaceous. Older Wilson cycles closed ancient oceans to form the Pan-African belts, including the Central African Fold Belt across Cameroon."),
        EX("Worked example 3: how long to open an ocean?", intro="An ocean opens at a full spreading rate of 4.0 cm/yr. How wide is it after 100 million years?", steps=[
            S("Convert the rate", math=r"4.0 \text{ cm/yr} = 40 \text{ km/Myr}"),
            S("Width", math=r"40 \times 100 = 4000 \text{ km}", text="Similar to the width of the South Atlantic."),
        ]),
        MISTAKE("Saying plates float on liquid magma", "The asthenosphere is mostly solid; it flows very slowly because it is hot and contains a little melt. The outer core is the only liquid layer."),
        MISTAKE("Confusing crust and lithosphere", "Plates are lithosphere: crust plus the rigid top of the mantle. The difference between oceanic and continental lithosphere is thickness, density, composition and age, not that one is solid and the other liquid."),
        QUIZ("Deep earthquakes (300-700 km) occur mainly",
             ["at mid-ocean ridges", "along transform faults", "in Benioff zones at destructive margins", "in the middle of stable shields"], 2,
             "Only a cold subducting slab is brittle enough to break at such depths.",
             hint="Where does cold lithosphere go deep into the mantle?",
             feedback=["Ridge earthquakes are shallow because the lithosphere there is thin and hot.", "Transform earthquakes are shallow.", "", "Shields have few earthquakes, and these are shallow."]),
        QUIZ("Which present-day example represents the young-ocean stage of the Wilson cycle?",
             ["East African Rift", "Red Sea", "Atlantic Ocean", "Himalaya"], 1,
             "The Red Sea is a narrow ocean floored partly by new oceanic crust.",
             hint="Narrow, with new ocean floor just formed.",
             feedback=["That is the embryonic rift stage; no ocean floor yet.", "", "The Atlantic is the mature stage.", "That is the suturing (collision) stage."]),
        TIP("Exam link: Paper 1 often asks about boundary types, features and earthquake depths. Paper 2 essays ask you to describe and explain plate boundaries with labelled cross-sections, evaluate driving mechanisms or outline the Wilson cycle with examples."),
        H("Practice"),
        PQ("Describe the features of an ocean-continent destructive boundary.",
           "The denser oceanic plate subducts beneath the continent, forming a deep trench. An inclined Benioff zone of shallow to deep earthquakes marks the slab. At about 100 km depth, water released from the slab lowers the melting point of the mantle wedge, producing magma that rises to form andesitic volcanoes and granite batholiths in a mountain belt (for example the Andes). Sediments are scraped off into an accretionary wedge and the continental margin is folded and metamorphosed."),
        PQ("Earthquake foci below a volcanic arc are 150 km deep, 250 km from the trench. Calculate the dip of the Benioff zone.",
           r"$\tan\theta = 150/250 = 0.6$, so $\theta = 31.0^{\circ}$."),
        PQ("Evaluate the view that mantle convection is the main driving force of plate motion.",
           "For: the mantle does convect, carrying heat out of the Earth, and rising plumes and sinking slabs are part of convection. Against: plates with long subducting slabs move fastest, which points to slab pull; ridges can migrate and are not always above upwellings; the drag of convection on the plate base is uncertain and may even resist motion. Conclusion: plates are part of convection, but the main forces acting on them are slab pull and, to a lesser extent, ridge push."),
        PQ("Outline the Wilson cycle and give one modern example of each stage.",
           "Embryonic: a continent domes and rifts (East African Rift). Young: a narrow sea floored by new oceanic crust (Red Sea). Mature: a wide ocean with passive margins (Atlantic). Declining: subduction starts and the ocean shrinks (Pacific). Terminal: a small remnant ocean between converging continents (Mediterranean). Suturing: continents collide and fold mountains form (Himalaya). The thickened, weakened crust may later rift and start a new cycle."),
        SUM("Plates are rigid lithosphere moving over the weak asthenosphere.",
            "Constructive, destructive (three types) and conservative boundaries have distinctive features and earthquake depths; Benioff zones mark subducting slabs.",
            "Slab pull is probably the largest driving force, then ridge push; the role of convection drag is debated.",
            "Hotspot chains and magnetic stripes give plate speeds: distance divided by time.",
            "The Wilson cycle: rift, young ocean, mature ocean, subduction, closure, collision. The South Atlantic and the Benue failed rift are part of a Cretaceous opening."),
    ],
))

# ------------------------------------------------------------------ 6. Crystal morphology and symmetry
LESSONS.append(lesson(
    module=M2,
    topic="Crystal morphology and symmetry",
    title="Crystal morphology, interfacial angles and elements of symmetry",
    slug="gyl1-crystal-morphology-symmetry",
    minutes=23,
    summary="Crystal faces, edges, forms and habits reflect an ordered internal structure. Interfacial angles are constant for a mineral, and every crystal can be described by its planes, axes and centre of symmetry.",
    objectives=[
        "Use the terms face, edge, solid angle, form (open and closed) and habit correctly",
        "State the law of constancy of interfacial angles and convert internal angles to interfacial angles",
        "Identify planes, axes (diad, triad, tetrad, hexad) and centre of symmetry on crystal models",
        "Count the full symmetry of a cube and of a rectangular box-shaped crystal",
    ],
    key_concepts=["Crystal face", "Form", "Habit", "Interfacial angle", "Contact goniometer", "Plane of symmetry", "Axis of symmetry", "Centre of symmetry", "Euler's rule"],
    blocks=[
        H("Introduction"),
        T("A quartz crystal from a vein in Cameroon and a quartz crystal from Brazil can look very different in size and shape, "
          "yet the angles between matching faces are exactly the same. Crystallography explains why: the outer shape grows from an inner pattern of atoms that is identical in every quartz crystal."),
        D("A **crystal** is a solid with a regular, repeating three-dimensional arrangement of atoms (a **lattice**), bounded, when it grows freely, by flat **faces**. "
          "Two faces meet at an **edge**; three or more meet at a **solid angle** (corner).", title="Crystal"),
        F(r"F + V = E + 2", title="Euler's rule for a crystal (F faces, V solid angles, E edges)"),
        KEY("Describing shape", "These terms appear in Paper 2 and Paper 3 answers.", cards=[
            ["Form", "A set of faces related by the symmetry of the crystal, for example the six faces of a cube. A **closed form** encloses space alone (cube, octahedron); an **open form** does not (prism, pinacoid) and must combine with other forms."],
            ["Habit", "The general shape a mineral usually takes: prismatic (augite), tabular (barite), acicular or needle-like (rutile, some tourmaline), bladed (kyanite), equant (garnet), fibrous (asbestos)."],
            ["Zone", "A set of faces whose edges are parallel. The common direction is the zone axis."],
        ]),
        H("Constancy of interfacial angles"),
        D("The **interfacial angle** between two faces is the angle between their **normals** (lines at right angles to each face). It equals 180 degrees minus the internal angle measured between the faces. "
          "**Steno's law** (law of constancy of interfacial angles) states that for any mineral the angles between corresponding faces are always the same, whatever the size or shape of the crystal.", title="Interfacial angle and Steno's law"),
        IMG("algyl1-interfacial.svg", alt="Two crystal faces meeting at an edge with an internal angle of 120 degrees; the normals to the faces meet at 60 degrees, the interfacial angle",
            caption="Figure 1. The interfacial angle is the angle between face normals."),
        T("A **contact goniometer** is a protractor with a hinged arm. Its arms are pressed against two faces and it reads the internal angle; subtract from 180 degrees to get the interfacial angle."),
        EX("Worked example 1: quartz prism faces", intro="A goniometer reads 120 degrees between two adjacent prism faces of a quartz crystal. Find the interfacial angle.", steps=[
            S("Use the relation", math=r"\text{interfacial angle} = 180^{\circ} - 120^{\circ} = 60^{\circ}"),
            S("Interpret", text="Six prism faces at 60-degree interfacial angles go round a full circle: 6 x 60 = 360 degrees. This is the hexagonal prism of quartz."),
        ]),
        H("Elements of symmetry"),
        KEY("Three kinds of symmetry element", "Each is a test you can do on a model.", cards=[
            ["Plane of symmetry", "Divides the crystal into two halves that are mirror images of each other."],
            ["Axis of symmetry", "A line about which rotation brings the crystal into the same position n times in 360 degrees: diad (2-fold, every 180 degrees), triad (3-fold, 120), tetrad (4-fold, 90), hexad (6-fold, 60). Five-fold and higher axes are impossible in crystals because such shapes cannot fill space."],
            ["Centre of symmetry", "Every face has an identical, parallel face on the opposite side of the crystal. A crystal either has one centre or none."],
        ]),
        T("Many books write the number of axes before the type in Roman numerals: 3 iv means three tetrad axes, 4 iii means four triad axes, 6 ii means six diad axes. Some use the symbols 2, 3, 4, 6. Learn the notation your teacher uses and be consistent."),
        EX("Worked example 2: the full symmetry of a cube", intro="Count all the symmetry elements of a perfect cube.", steps=[
            S("Planes", text="3 planes parallel to the faces (axial planes) + 6 diagonal planes through opposite edges = 9 planes."),
            S("Tetrads", text="One through the centres of each pair of opposite faces: 3 iv."),
            S("Triads", text="One through each pair of opposite corners: 4 iii."),
            S("Diads", text="One through the midpoints of each pair of opposite edges: 12 edges, so 6 ii."),
            S("Centre and total", text="A centre is present. Total: 9 planes, 13 axes (3 iv, 4 iii, 6 ii) and a centre, 23 elements in all."),
        ], check=r"F + V = 6 + 8 = 14 = E + 2 = 12 + 2"),
        EX("Worked example 3: a box-shaped crystal", intro="A crystal is shaped like a matchbox, with three unequal edges at right angles. Count its symmetry.", steps=[
            S("Planes", text="Three planes, each parallel to one pair of faces. Diagonal planes do not work because the faces are rectangles of different sizes."),
            S("Axes", text="Three diads, each through the centres of a pair of opposite faces. No tetrads, because a rectangle repeats only twice in a turn."),
            S("Centre", text="Present: each face has an equal, parallel opposite."),
            S("Total", text="3 planes, 3 ii, centre. This is the full symmetry of the orthorhombic system (next lesson)."),
        ]),
        MISTAKE("Using the internal angle as the interfacial angle", "A goniometer reads the internal angle between faces. The interfacial angle is between the normals: subtract from 180 degrees."),
        MISTAKE("Defining the centre of symmetry as the middle of the crystal", "Every crystal has a middle. A centre of symmetry exists only if every face has a parallel, identical face directly opposite."),
        MISTAKE("Judging symmetry from a distorted crystal", "Real crystals often grow unevenly, so faces of one form differ in size. Symmetry belongs to the angles and the internal structure, so use ideal models and angles, not face sizes."),
        QUIZ("A crystal returns to the same appearance three times in one full rotation about an axis. The axis is a",
             ["diad", "triad", "tetrad", "hexad"], 1,
             "Three repeats in 360 degrees, every 120 degrees, is a triad (3-fold) axis.",
             hint="Count the repeats per full turn.",
             feedback=["A diad repeats twice per turn.", "", "A tetrad repeats four times.", "A hexad repeats six times."]),
        QUIZ("How many planes of symmetry does a cube have?",
             ["3", "6", "9", "13"], 2,
             "3 axial planes plus 6 diagonal planes.",
             hint="Do not forget the diagonal planes through opposite edges.",
             feedback=["These are only the planes parallel to the faces.", "These are only the diagonal planes.", "", "13 is the number of axes of symmetry."]),
        TIP("Exam link: Paper 1 asks you to count symmetry elements or name a type of axis. In Paper 3 you may be given a crystal model to describe: name its forms, count planes, axes and centre, and give the system. The Board's 2023 report notes many candidates could not list the symmetry of a model correctly."),
        H("Practice"),
        PQ("Distinguish between a closed form and an open form, with one example of each.",
           "A closed form is a set of symmetry-related faces that encloses space by itself, for example the cube or the octahedron. An open form cannot enclose space alone and must be combined with other forms, for example a prism (faces parallel to one axis) or a pinacoid (two parallel faces)."),
        PQ("A goniometer reads 109.5 degrees between two adjacent faces of an octahedron. What is the interfacial angle?",
           r"$180^{\circ} - 109.5^{\circ} = 70.5^{\circ}$."),
        PQ("Check Euler's rule for an octahedron and a rhombic dodecahedron (12 faces, 14 solid angles, 24 edges).",
           r"Octahedron: 8 faces, 6 solid angles, 12 edges: $8 + 6 = 14 = 12 + 2$. Rhombic dodecahedron: $12 + 14 = 26 = 24 + 2$. Both obey the rule."),
        PQ("Explain why crystals cannot have five-fold axes of symmetry.",
           "A crystal is built by repeating an identical unit cell to fill space with no gaps. Regular pentagons cannot tile a plane without gaps, so a lattice cannot have five-fold rotation symmetry. Only 2-, 3-, 4- and 6-fold axes are compatible with a repeating lattice."),
        SUM("Crystals have ordered internal structures; faces, edges and solid angles obey F + V = E + 2.",
            "A form is a set of symmetry-related faces (closed or open); habit is the usual shape.",
            "Interfacial angle = angle between normals = 180 degrees minus the internal angle; it is constant for a mineral (Steno's law).",
            "Symmetry elements: planes, axes (diad, triad, tetrad, hexad) and a centre.",
            "A cube has 9 planes, 13 axes (3 iv, 4 iii, 6 ii) and a centre; a box shape has 3 planes, 3 ii and a centre."),
    ],
))

# ------------------------------------------------------------------ 7. Axes and seven systems
LESSONS.append(lesson(
    module=M2,
    topic="Crystallographic axes and the seven crystal systems",
    title="Crystallographic axes, axial ratios and the seven crystal systems",
    slug="gyl1-axes-seven-crystal-systems",
    minutes=24,
    summary="Crystals are described by reference axes a, b and c and the angles between them. Axial lengths, axial angles and diagnostic symmetry define the seven crystal systems, from cubic to triclinic.",
    objectives=[
        "Draw and label crystallographic axes and axial angles with the standard conventions",
        "Calculate axial ratios from unit-cell lengths",
        "State the axes, angles and diagnostic symmetry of the seven crystal systems, with mineral examples",
        "Assign a crystal to its system from its axes or symmetry",
    ],
    key_concepts=["Crystallographic axes", "Axial angles", "Unit cell", "Axial ratio", "Crystal system", "Diagnostic symmetry", "Hexagonal axes"],
    blocks=[
        H("Introduction"),
        T("To describe the position of a crystal face we need a frame of reference, just as a map needs grid lines. Crystallographers use three (sometimes four) "
          "reference axes chosen to match the symmetry of the crystal. The lengths and angles of these axes sort every mineral into one of seven crystal systems."),
        D("**Crystallographic axes** are imaginary reference lines through the centre of a crystal, usually parallel to important edges or symmetry axes. "
          "They are labelled a, b and c (lower case). By convention **+a** points towards the observer, **+b** to the right and **+c** upwards. "
          "The **axial angles** are $\\alpha$ (between b and c), $\\beta$ (between a and c) and $\\gamma$ (between a and b).", title="Axes and angles"),
        IMG("algyl1-axes.svg", alt="Three crystallographic axes: +c vertical, +b to the right, +a towards the viewer, with negative ends dashed, and the angles alpha between b and c, beta between a and c, gamma between a and b",
            caption="Figure 1. Standard orientation of the crystallographic axes and axial angles."),
        D("The **unit cell** is the smallest repeating box of the crystal structure; its edge lengths are the axial lengths a, b and c (in angstroms, 1 angstrom = $10^{-10}$ m). "
          "The **axial ratio** compares them, usually with b set to 1: $a:b:c = \\frac{a}{b}:1:\\frac{c}{b}$. In tetragonal and hexagonal crystals the ratio is given as $c/a$.", title="Unit cell and axial ratio"),
        EX("Worked example 1: axial ratio of an orthorhombic mineral", intro="Teaching values: an orthorhombic mineral has a = 8.4, b = 12.0 and c = 6.0 angstroms. Find the axial ratio.", steps=[
            S("Divide each length by b", math=r"\dfrac{8.4}{12.0} : \dfrac{12.0}{12.0} : \dfrac{6.0}{12.0}"),
            S("Axial ratio", math=r"a:b:c = 0.70 : 1 : 0.50"),
        ]),
        EX("Worked example 2: quartz", intro="Quartz has a = 4.913 and c = 5.405 angstroms (standard values). Find c/a.", steps=[
            S("Ratio", math=r"\dfrac{c}{a} = \dfrac{5.405}{4.913} = 1.100"),
            S("Meaning", text="The c axis is about 10 percent longer than each a axis. The ratio is constant for quartz and fixes the angles of its pyramid faces."),
        ]),
        H("The seven crystal systems"),
        CODE("""
System        Axes                         Axial angles                    Diagnostic symmetry   Examples
Cubic         a1 = a2 = a3                 all 90                          4 triads (4 iii)      halite, galena, pyrite, garnet, fluorite
Tetragonal    a1 = a2, c longer/shorter    all 90                          1 tetrad (1 iv)       zircon, cassiterite, rutile
Hexagonal     a1 = a2 = a3 (at 120), c     a's at 120; c at 90 to them     1 hexad (1 vi)        beryl, apatite
Trigonal      as hexagonal                 as hexagonal                    1 triad (1 iii)       quartz, calcite, tourmaline, corundum
Orthorhombic  a, b, c all unequal          all 90                          3 diads (3 ii)*       olivine, topaz, baryte, enstatite
Monoclinic    a, b, c all unequal          alpha = gamma = 90, beta > 90   1 diad (1 ii)*        orthoclase, augite, hornblende, micas, gypsum
Triclinic     a, b, c all unequal          none is 90                      no axis, no plane     plagioclase (albite), microcline, kyanite, axinite
""", "text", title="The seven systems (angles in degrees)",
             caption="* In lower-symmetry classes the diads of orthorhombic and monoclinic crystals can be replaced by planes: orthorhombic needs three diads, or one diad where two planes meet; monoclinic needs one diad or one plane. Triclinic crystals have at most a centre."),
        T("**Diagnostic symmetry** is the minimum symmetry that every crystal of the system has. It is not the same as the full list of symmetry elements of the most symmetrical member. "
          "For example, every cubic crystal has four triads, but not every cubic crystal has three tetrads."),
        T("Some textbooks, including many O Level books, put trigonal crystals inside the hexagonal system and so speak of six systems. Others describe trigonal crystals with three equal "
          "rhombohedral axes inclined at equal angles. Check your textbook and use one description consistently."),
        EX("Worked example 3: which system?", intro="A crystal has three unequal axes. Two meet at 90 degrees and the third makes an angle of 116 degrees with c. Its only symmetry is one diad and one plane at right angles to it, and a centre. Name the system.", steps=[
            S("Axes", text="Three unequal axes, so not cubic, tetragonal, hexagonal or trigonal."),
            S("Angles", text="Two angles of 90 degrees and one oblique (beta = 116 degrees): monoclinic, not orthorhombic (all 90) or triclinic (none 90)."),
            S("Symmetry check", text="One diad plus one plane plus a centre is the full monoclinic symmetry. Answer: monoclinic."),
        ]),
        MISTAKE("Writing axes in capitals or as a+", "Label axes with lower-case letters and put the sign first: +a, -a, +b, -b, +c, -c. The Board's 2023 report noted labels such as a+ and capital letters."),
        MISTAKE("Wrong Greek letters", "Write alpha, beta and gamma properly, or in words. Do not write a for alpha or y for gamma, which can be confused with axis names."),
        MISTAKE("Giving the wrong diagnostic axis", "Tetragonal is 1 iv (one tetrad), hexagonal is 1 vi, trigonal is 1 iii, cubic is 4 iii (four triads, not three tetrads). Triclinic is not 'none': say no plane, no axis, and (in the normal class) a centre."),
        MISTAKE("Drawing triclinic a and b axes horizontal and at 90 degrees", "In a triclinic model none of the axial angles is 90 degrees, so the a and b axes must be drawn inclined."),
        QUIZ("A mineral has a1 = a2 and c of a different length, all at 90 degrees. Which system?",
             ["Cubic", "Tetragonal", "Orthorhombic", "Hexagonal"], 1,
             "Two equal horizontal axes and a different vertical axis, all at right angles: tetragonal.",
             hint="How many axes are equal, and at what angles?",
             feedback=["Cubic needs all three axes equal.", "", "Orthorhombic has all three axes unequal.", "Hexagonal has three horizontal axes at 120 degrees."]),
        QUIZ("Which is the diagnostic symmetry of the cubic system?",
             ["3 tetrad axes", "4 triad axes", "9 planes of symmetry", "A centre of symmetry"], 1,
             "Every cubic crystal, even the least symmetrical class, has four triads along the body diagonals.",
             hint="Which element is shared by all cubic classes?",
             feedback=["Some cubic classes, such as that of pyrite, lack tetrads.", "", "Only the most symmetrical class has 9 planes.", "Many systems can have a centre; it is not diagnostic."]),
        TIP("Exam link: Paper 1 often gives axial lengths and angles and asks for the system. Paper 2 can ask you to tabulate axes, axial angles and diagnostic symmetry for all systems. In Paper 3 you insert and label axes on a model and state its system with a reason."),
        H("Practice"),
        PQ("Tabulate the axes and axial angles of the orthorhombic, monoclinic and triclinic systems.",
           r"Orthorhombic: $a \ne b \ne c$, $\alpha = \beta = \gamma = 90^{\circ}$. Monoclinic: $a \ne b \ne c$, $\alpha = \gamma = 90^{\circ}$, $\beta > 90^{\circ}$. Triclinic: $a \ne b \ne c$, $\alpha \ne \beta \ne \gamma \ne 90^{\circ}$."),
        PQ("Teaching values: a monoclinic mineral has a = 4.8, b = 10.2, c = 6.0 angstroms. Calculate the axial ratio.",
           r"$a:b:c = \dfrac{4.8}{10.2} : 1 : \dfrac{6.0}{10.2} = 0.47 : 1 : 0.59$."),
        PQ("Describe the hexagonal axes and name the diagnostic symmetry of the hexagonal and trigonal systems.",
           "Four axes: three equal horizontal axes a1, a2 and a3 at 120 degrees to each other, and a vertical c axis of different length at right angles to them. Hexagonal diagnostic symmetry: one hexad (1 vi) parallel to c. Trigonal: one triad (1 iii) parallel to c."),
        PQ("A Paper 3-style crystal model has no plane of symmetry and no axis, but each face has a parallel opposite face. Name its system, give the reason and one example mineral.",
           "Triclinic. Reason: no plane and no axis of symmetry, only a centre of symmetry. Example: albite (plagioclase feldspar); also microcline, kyanite or axinite."),
        SUM("Axes a, b, c: +a towards you, +b right, +c up; alpha between b and c, beta between a and c, gamma between a and b.",
            "Axial ratio a:b:c with b = 1 (or c/a for tetragonal and hexagonal crystals) is constant for a mineral.",
            "Seven systems: cubic, tetragonal, hexagonal, trigonal, orthorhombic, monoclinic, triclinic.",
            "Diagnostic symmetry: 4 iii, 1 iv, 1 vi, 1 iii, 3 ii, 1 ii, no axis or plane.",
            "Label axes in lower case with the sign first and learn one example mineral for each system."),
    ],
))

# ------------------------------------------------------------------ 8. Miller indices
LESSONS.append(lesson(
    module=M2,
    topic="Miller indices",
    title="Miller indices: naming crystal faces and forms",
    slug="gyl1-miller-indices",
    minutes=23,
    summary="Miller indices (hkl) name a crystal face from the reciprocals of its intercepts on the axes, measured in unit lengths. Learn the method, negative and parallel faces, forms {hkl}, Miller-Bravais indices for hexagonal crystals and the zone rule.",
    objectives=[
        "Find Miller indices from intercepts given in unit lengths or in real lengths with an axial ratio",
        "Write indices correctly for faces parallel to an axis and for negative intercepts",
        "Distinguish a face (hkl), a form {hkl} and a direction [uvw], and name common forms",
        "Use Miller-Bravais indices (hkil) for hexagonal crystals and test whether a face lies in a zone",
    ],
    key_concepts=["Intercept", "Weiss parameters", "Miller indices", "Unit face", "Form", "Miller-Bravais indices", "Zone axis", "Zone law"],
    blocks=[
        H("Introduction"),
        T("A galena cube from a lead vein and a magnetite octahedron are both cubic, but their faces sit in different positions relative to the axes. "
          "Miller indices give every face a short name made of three whole numbers, so that geologists anywhere can say exactly which face they mean."),
        D("A face cuts the crystallographic axes at **intercepts**. Measured in units of the axial lengths a, b and c, these are the **Weiss parameters**. "
          "The **Miller indices** (h k l) are the reciprocals of the Weiss parameters, cleared of fractions and reduced to the smallest whole numbers. "
          "The **unit face** (parametral face) cuts all three axes at one unit and has indices (111).", title="Miller indices"),
        KEY("The method", "Four steps; always show them.", cards=[
            ["1 Intercepts", "Write where the face cuts a, b and c in unit lengths. A face parallel to an axis meets it at infinity."],
            ["2 Reciprocals", "Invert each intercept. The reciprocal of infinity is 0."],
            ["3 Clear fractions", "Multiply by the lowest common multiple of the denominators."],
            ["4 Write", "Put the numbers in round brackets, with no commas: (hkl). Show a negative index with a bar over the number."],
        ]),
        IMG("algyl1-miller.svg", alt="Three axes a, b and c with unit tick marks; a triangular face cuts a at 2 units, b at 3 units and c at 6 units",
            caption="Figure 1. A face cutting the axes at 2a, 3b and 6c."),
        EX("Worked example 1: the face in Figure 1", intro="A face cuts a at 2, b at 3 and c at 6 unit lengths. Find its Miller indices.", steps=[
            S("Intercepts", math=r"2,\ 3,\ 6"),
            S("Reciprocals", math=r"\tfrac{1}{2},\ \tfrac{1}{3},\ \tfrac{1}{6}"),
            S("Multiply by 6", math=r"3,\ 2,\ 1"),
            S("Indices", math=r"(321)"),
        ], check=r"\tfrac{1}{2} : \tfrac{1}{3} : \tfrac{1}{6} = 3 : 2 : 1"),
        EX("Worked example 2: a negative intercept and a parallel axis", intro="A face cuts the negative end of a at 1 unit, cuts b at 2 units and is parallel to c.", steps=[
            S("Intercepts", math=r"-1,\ 2,\ \infty"),
            S("Reciprocals", math=r"-1,\ \tfrac{1}{2},\ 0"),
            S("Multiply by 2", math=r"-2,\ 1,\ 0"),
            S("Indices", math=r"(\bar{2}10)", text="Read as 'bar two, one, zero'."),
        ]),
        H("Using the axial ratio"),
        T("If intercepts are given as real lengths, first divide each by the axial unit length (from the axial ratio) to turn them into unit lengths. Then follow the usual steps."),
        EX("Worked example 3: real lengths", intro="A mineral has axial ratio a:b:c = 0.5 : 1 : 0.8. A face cuts the axes at 1.0, 1.0 and 0.8 (same arbitrary length units). Find its indices.", steps=[
            S("Convert to unit lengths", math=r"\dfrac{1.0}{0.5} = 2,\ \dfrac{1.0}{1} = 1,\ \dfrac{0.8}{0.8} = 1"),
            S("Reciprocals", math=r"\tfrac{1}{2},\ 1,\ 1"),
            S("Multiply by 2", math=r"(122)"),
        ]),
        H("Faces, forms and directions"),
        KEY("Brackets matter", "Three kinds of bracket, three meanings.", cards=[
            ["(hkl)", "One face, for example (100), the front face of a cube."],
            ["{hkl}", "A form: all faces related by symmetry. Cube {100} has 6 faces; octahedron {111} has 8; rhombic dodecahedron {110} has 12."],
            ["[uvw]", "A direction, such as an axis or zone axis: [001] is the c axis."],
        ]),
        T("Useful patterns: (100), (010) and (001) are the faces cut by only one axis (pinacoid faces in lower-symmetry systems); (hk0) faces are parallel to c, so they are prism faces; "
          "(h0l) faces are parallel to b; (0kl) faces are parallel to a."),
        H("Hexagonal crystals: Miller-Bravais indices"),
        F(r"(hkil) \quad \text{with} \quad i = -(h + k)", title="Miller-Bravais indices"),
        T(r"Hexagonal and trigonal crystals have four axes, $a_1$, $a_2$, $a_3$ and c, so faces get four indices. The third index is fixed by the first two. "
          r"The basal pinacoid is $(0001)$; a first-order prism face is $(10\bar{1}0)$; a second-order prism face is $(11\bar{2}0)$."),
        H("Zones"),
        T(r"Faces whose intersection edges are parallel belong to a **zone**. A face $(hkl)$ lies in the zone with axis $[uvw]$ if $hu + kv + lw = 0$ (the zone law). "
          r"For example $(100)$ and $(010)$ both lie in the zone $[001]$: $1(0) + 0(0) + 0(1) = 0$ and $0(0) + 1(0) + 0(1) = 0$. This is the vertical prism zone of the crystal."),
        MISTAKE("Using the intercepts instead of their reciprocals", "Intercepts 1, 2, 3 do not give (123). Take reciprocals 1, 1/2, 1/3 and multiply by 6: (632)."),
        MISTAKE("Writing infinity or commas in the indices", "A face parallel to an axis gives index 0, not infinity. Write (210), not (2, 1, 0) or (2 1 infinity)."),
        MISTAKE("Forgetting to reduce", "A face cutting at 2, 2, 2 gives reciprocals 1/2, 1/2, 1/2, which reduce to (111): it is parallel to the unit face."),
        QUIZ("A face cuts a at 1, b at 1 and is parallel to c. Its Miller indices are",
             ["(110)", "(11∞)", "(001)", "(111)"], 0,
             "Reciprocals 1, 1, 0 give (110), a prism face parallel to c.",
             hint="What is the reciprocal of infinity?",
             feedback=["", "Infinity is never written: its reciprocal is 0.", "(001) is parallel to a and b, cutting only c.", "(111) cuts all three axes."]),
        QUIZ("How many faces does the cubic form {111} have?",
             ["4", "6", "8", "12"], 2,
             "{111} is the octahedron: one face in each octant.",
             hint="Each combination of signs of h, k and l gives one face.",
             feedback=["Half of the octahedron would be a tetrahedron, which belongs to a lower class.", "The cube {100} has 6 faces.", "", "The rhombic dodecahedron {110} has 12."]),
        TIP("Exam link: Paper 1 asks for indices from intercepts or the number of faces in a form. Paper 2 can ask you to explain how Miller indices are derived, with a worked example. In Paper 3 you may name the forms on a model using indices. Show every step."),
        H("Practice"),
        PQ("Find the Miller indices of a face with intercepts 1a, 2b and 3c.",
           r"Reciprocals $1, \tfrac{1}{2}, \tfrac{1}{3}$; multiply by 6: $(632)$."),
        PQ("Find the indices of a face cutting a at 2 units, parallel to b, and cutting c at 3 units.",
           r"Intercepts $2, \infty, 3$; reciprocals $\tfrac{1}{2}, 0, \tfrac{1}{3}$; multiply by 6: $(302)$."),
        PQ(r"A mineral has a:b:c = 0.6 : 1 : 1.2. A face cuts the axes at 0.6, 2.0 and 2.4 length units. Find its Miller indices.",
           r"Unit lengths: $0.6/0.6 = 1$, $2.0/1 = 2$, $2.4/1.2 = 2$. Reciprocals $1, \tfrac{1}{2}, \tfrac{1}{2}$; multiply by 2: $(211)$."),
        PQ(r"Give the four-index symbol of the hexagonal face with Miller-Bravais indices h = 2, k = 1, l = 1, and show your working.",
           r"$i = -(h + k) = -(2 + 1) = -3$, so the face is $(21\bar{3}1)$."),
        SUM("Intercepts in unit lengths (Weiss parameters), then reciprocals, then clear fractions: (hkl).",
            "Parallel to an axis gives 0; a negative intercept gives a bar over the index; reduce to the smallest integers.",
            "With real lengths, divide by the axial unit lengths first.",
            "(hkl) is a face, {hkl} a form, [uvw] a direction; cube {100}, octahedron {111}, dodecahedron {110}.",
            r"Hexagonal: $(hkil)$ with $i = -(h + k)$. Zone law: $hu + kv + lw = 0$."),
    ],
))

# ------------------------------------------------------------------ 9. Stereographic projection
LESSONS.append(lesson(
    module=M2,
    topic="Stereographic projection and crystal classes",
    title="Stereographic projection and the 32 crystal classes",
    slug="gyl1-stereographic-projection-classes",
    minutes=25,
    summary="A stereogram plots the face poles of a crystal on a flat circle while keeping their angles. Symbols for planes and axes show the symmetry, and the 32 possible combinations of symmetry elements are the crystal classes.",
    objectives=[
        "Explain how face poles are projected onto the primitive circle, and plot a pole from its angle",
        "Read symmetry elements and general forms from a stereogram",
        "State that there are 32 crystal classes and how they are shared among the seven systems",
        "Name the holosymmetric class of each system and the number of faces in its general form",
    ],
    key_concepts=["Spherical projection", "Face pole", "Primitive circle", "Stereogram", "Great circle", "Wulff net", "Crystal class", "Holosymmetric class", "General form"],
    blocks=[
        H("Introduction"),
        T("A crystal is three-dimensional, but exam papers and notebooks are flat. A stereogram is a way to draw the directions of all the faces of a crystal on paper so that "
          "the angles between faces can still be measured. It is the crystallographer's map."),
        D("Imagine the crystal at the centre of a large sphere. The normal to each face, drawn outwards from the centre, meets the sphere at the **face pole**. "
          "In the **stereographic projection**, each pole in the upper hemisphere is joined to the south pole of the sphere; where that line crosses the equatorial plane "
          "is its projected position. The equator projects as the **primitive circle**. Poles in the lower hemisphere are joined to the north pole instead.", title="Stereographic projection"),
        IMG("algyl1-stereo-principle.svg", alt="Left: vertical section of a sphere with a face pole P at angle rho from the vertical; a line from P to the south pole S crosses the equatorial plane at P prime. Right: a stereogram circle with an upper pole as a dot and a lower pole as an open circle",
            caption="Figure 1. Projecting a face pole, and the stereogram that results."),
        KEY("Reading a stereogram", "Conventions used in most textbooks.", cards=[
            ["Dots and circles", "A pole in the upper hemisphere is a dot; a pole in the lower hemisphere is an open circle. A dot inside a circle means a face above and a face below in the same direction."],
            ["Position", r"The angle $\rho$ from the c axis sets the distance from the centre; the angle $\phi$ round the circle sets the direction. A horizontal face (001) plots at the centre; vertical faces ($\rho = 90^{\circ}$) plot on the primitive."],
            ["Great circles", "Faces of one zone lie on one great circle. Vertical zones plot as straight diameters; inclined zones as arcs that meet the primitive at opposite points."],
            ["Symmetry symbols", "Mirror planes are solid lines (a solid primitive means a horizontal mirror). Axes: lens shape = diad, triangle = triad, square = tetrad, hexagon = hexad."],
        ]),
        F(r"r = R\tan\dfrac{\rho}{2}", title="Distance of a projected pole from the centre (R = radius of the primitive)"),
        EX("Worked example 1: plotting an octahedron face", intro=r"An octahedron face (111) of a cubic crystal makes $\rho = 54.7^{\circ}$ with the c axis. The primitive circle has radius 50 mm. How far from the centre is the pole?", steps=[
            S("Half the angle", math=r"\dfrac{\rho}{2} = 27.4^{\circ}"),
            S("Distance", math=r"r = 50\tan 27.4^{\circ} = 50 \times 0.518 = 25.9 \text{ mm}"),
            S("Check limits", text="rho = 0 gives r = 0 (centre); rho = 90 degrees gives r = 50 tan 45 = 50 mm (on the primitive)."),
        ]),
        T("In practice poles are plotted with a **Wulff net**, a printed stereographic grid of great and small circles. Because the projection keeps angles, the angle between two poles is read directly by rotating them onto the same great circle of the net."),
        H("Crystal classes"),
        D("A **crystal class** (point group) is one possible combination of symmetry elements. Only 2-, 3-, 4- and 6-fold axes, mirror planes and a centre are allowed, "
          "and they can be combined in only **32** ways. Each class belongs to one of the seven systems.", title="Crystal class"),
        CODE("""
System         Classes   Holosymmetric class   Symmetry of that class                Faces in general form
Triclinic         2      -1                    centre only                                    2
Monoclinic        3      2/m                   1 ii, 1 plane, centre                          4
Orthorhombic      3      mmm                   3 ii, 3 planes, centre                         8
Tetragonal        7      4/mmm                 1 iv + 4 ii, 5 planes, centre                 16
Trigonal          5      -3m                   1 iii + 3 ii, 3 planes, centre                12
Hexagonal         7      6/mmm                 1 vi + 6 ii, 7 planes, centre                 24
Cubic             5      m-3m                  3 iv + 4 iii + 6 ii, 9 planes, centre         48
Total            32
""", "text", title="The 32 classes in the seven systems",
             caption="Symbols are Hermann-Mauguin symbols; some textbooks name classes after a typical mineral instead. Check your textbook."),
        T("The **holosymmetric** (normal) class has the highest symmetry possible in its system. Its **general form** {hkl}, with no special relation to the symmetry elements, has the largest number of faces. "
          "Counting the poles of the general form on a stereogram is a quick way to recognise the class."),
        IMG("algyl1-stereo-mmm.svg", alt="Stereogram with a solid primitive circle and two solid perpendicular diameters, lens-shaped diad symbols at the centre and at the ends of both diameters, and four dot-in-circle pole pairs, one in each quadrant",
            caption="Figure 2. Stereogram of the general form in the holosymmetric orthorhombic class."),
        EX("Worked example 2: reading Figure 2", intro="Identify the symmetry and the class shown in Figure 2.", steps=[
            S("Mirrors", text="Two solid diameters and a solid primitive: three mirror planes at right angles."),
            S("Axes", text="Lens symbols at the centre and at the ends of both diameters: three diads at right angles."),
            S("Centre", text="Each upper pole (dot) has a lower pole (circle) at the opposite position, so there is a centre."),
            S("Count poles", text="4 dots + 4 circles = 8 faces in the general form."),
            S("Answer", text="3 ii, 3 planes and a centre: the holosymmetric orthorhombic class, mmm."),
        ]),
        MISTAKE("Using r = R tan rho", "That is a different (gnomonic) projection. The stereographic distance uses half the angle: r = R tan(rho/2), so poles stay inside the primitive."),
        MISTAKE("Plotting lower poles as dots", "Lower-hemisphere poles are open circles. Mixing them up hides a centre or a horizontal mirror."),
        MISTAKE("Confusing 32 classes with 7 systems", "There are 7 crystal systems and 32 classes. Each system contains between 2 and 7 classes."),
        QUIZ("On a stereogram, where does the pole of a vertical prism face plot?",
             ["At the centre", "On the primitive circle", "Halfway to the primitive", "Outside the primitive"], 1,
             "A vertical face has its normal horizontal (rho = 90 degrees), so its pole lies on the equator, which projects as the primitive.",
             hint="What is rho for a vertical face?",
             feedback=["The centre is for horizontal faces such as (001).", "", "That is for rho of about 53 degrees.", "Stereographic poles never fall outside the primitive."]),
        QUIZ("The general form of a class has 16 faces and the stereogram shows one tetrad. Which class is it?",
             ["mmm", "4/mmm", "6/mmm", "m-3m"], 1,
             "16 faces with a tetrad is the holosymmetric tetragonal class.",
             hint="Which system has a single tetrad?",
             feedback=["mmm has 8 faces and no tetrad.", "", "6/mmm has a hexad and 24 faces.", "m-3m has 48 faces and three tetrads."]),
        TIP("Exam link: Paper 1 may ask about the number of classes, stereogram conventions or the faces in a general form. Paper 2 can ask you to explain how a stereogram is constructed and to draw one for a named class, showing poles and symmetry symbols."),
        H("Practice"),
        PQ("Describe how the pole of a face in the upper hemisphere is plotted on a stereogram.",
           "Place the crystal at the centre of a sphere. Draw the normal to the face from the centre to meet the sphere: this is the face pole. Join the pole to the south pole of the sphere. The point where this line crosses the equatorial (primitive) plane is the projected pole, drawn as a dot. Its distance from the centre is R tan(rho/2), where rho is the angle between the face normal and the c axis."),
        PQ("A face has rho = 60 degrees. The primitive radius is 50 mm. How far from the centre is its pole?",
           r"$r = 50\tan 30^{\circ} = 50 \times 0.577 = 28.9$ mm."),
        PQ("Draw (describe) the stereogram of the general form of the holosymmetric tetragonal class 4/mmm.",
           "Solid primitive (horizontal mirror). Four solid diameters at 45 degrees (four vertical mirrors). A square (tetrad) at the centre and lens symbols (diads) at the ends of the four diameters. Sixteen poles: in each of the eight sectors between mirrors, one dot with a circle at the same position, giving 8 dots and 8 circles."),
        SUM("Face poles are found from face normals on a sphere and projected to the primitive plane; upper poles are dots, lower poles circles.",
            r"Distance from the centre: $r = R\tan(\rho/2)$; horizontal faces plot at the centre, vertical faces on the primitive.",
            "Zones lie on great circles; a Wulff net measures angles between poles.",
            "Symmetry symbols: solid lines for mirrors, lens, triangle, square and hexagon for 2-, 3-, 4- and 6-fold axes.",
            "There are 32 classes; holosymmetric general forms have 2, 4, 8, 16, 12, 24 and 48 faces from triclinic to cubic."),
    ],
))

# ------------------------------------------------------------------ 10. The polarizing microscope
LESSONS.append(lesson(
    module=M3,
    topic="The polarizing microscope",
    title="The polarizing microscope: thin sections, plane-polarised and crossed-polarised light",
    slug="gyl1-polarizing-microscope",
    minutes=22,
    summary="The petrological microscope examines 30-micrometre thin sections in plane-polarised light (PPL) and between crossed polars (XPL). Learn its parts, what each mode shows, and how to estimate magnification and grain size.",
    objectives=[
        "Name the parts of a polarizing microscope and state the function of each",
        "Explain how a thin section is made and why its thickness is standard",
        "List the properties observed in PPL and in XPL",
        "Calculate magnification, field of view and grain size",
    ],
    key_concepts=["Thin section", "Polarizer", "Analyser", "Plane-polarised light", "Crossed polars", "Rotating stage", "Bertrand lens", "Accessory plate", "Field of view"],
    blocks=[
        H("Introduction"),
        T("A hand lens shows that a granite contains light and dark grains. To be sure which feldspar is present, whether a dark grain is hornblende or augite, and how the grains grew, "
          "geologists cut the rock into a slice so thin that light passes through it and examine it with polarised light. This is the main tool of petrology."),
        D("A **thin section** is a slice of rock glued to a glass slide and ground to a standard thickness of **30 micrometres** (0.03 mm), then covered with a cover slip. "
          "At this thickness most silicate minerals are transparent, and the standard thickness means interference colours can be compared between sections.", title="Thin section"),
        D("Ordinary light vibrates in all directions at right angles to its path. **Plane-polarised light** vibrates in one plane only. A **polarizer** produces it; an **analyser** "
          "is a second polarizer set at 90 degrees to the first.", title="Polarised light"),
        IMG("algyl1-microscope.svg", alt="Schematic polarizing microscope from bottom to top: light source, polarizer, condenser and iris diaphragm, rotating stage with thin section, objective lens, accessory slot, analyser, Bertrand lens and eyepiece with cross-wires",
            caption="Figure 1. Main parts of a polarizing microscope (schematic, not to scale)."),
        KEY("Parts and functions", "Learn them from the light source upwards.", cards=[
            ["Polarizer (lower polar)", "Below the stage. Polarises the light before it enters the section. In many microscopes it vibrates east-west; check your microscope."],
            ["Condenser and iris diaphragm", "Focus the light onto the section and control the amount and angle of light."],
            ["Rotating stage", "Turns the section through 360 degrees; the degree scale (with vernier) measures angles such as extinction angles."],
            ["Objectives", "Low, medium and high power lenses, for example 4x, 10x and 40x."],
            ["Accessory slot", "Takes a gypsum (first-order red) plate, mica plate or quartz wedge to help identify interference colours and optic sign."],
            ["Analyser (upper polar)", "Can be pushed in or out. Set at 90 degrees to the polarizer, so with no mineral in the way the field is black."],
            ["Bertrand lens", "Flips in to view interference figures (conoscopic light), used to find whether a mineral is uniaxial or biaxial."],
            ["Eyepiece with cross-wires", "Magnifies the image; the cross-wires are parallel to the vibration directions of polarizer and analyser."],
        ]),
        H("PPL and XPL"),
        KEY("What each mode shows", "Always describe a mineral in PPL first, then in XPL, rotating the stage each time.", cards=[
            ["Plane-polarised light (PPL), analyser out", "Colour, pleochroism (colour change on rotation), relief (how strongly grain edges stand out), shape and habit, cleavage, fractures, inclusions and alteration."],
            ["Crossed polars (XPL), analyser in", "Isotropic or anisotropic behaviour, interference colours (birefringence), extinction and extinction angle, twinning and zoning."],
        ]),
        T("Between crossed polars, an **isotropic** material (volcanic glass, or a cubic mineral such as garnet) stays black in every position. An **anisotropic** mineral shows interference colours and goes black four times in a full turn of the stage; "
          "each black position is called **extinction**. **Opaque** minerals such as magnetite and pyrite are black in both PPL and XPL; they are studied with a reflected-light (ore) microscope."),
        H("Magnification and grain size"),
        F(r"\text{magnification} = \text{objective} \times \text{eyepiece} \qquad \text{field of view} \propto \dfrac{1}{\text{magnification}}", title="Magnification and field of view"),
        EX("Worked example 1: magnification", intro="A 10x eyepiece is used with a 10x objective and then with a 40x objective. Find the magnifications.", steps=[
            S("Low power", math=r"10 \times 10 = 100\times"),
            S("High power", math=r"40 \times 10 = 400\times"),
        ]),
        EX("Worked example 2: grain size from the field of view", intro="At 100x the field of view is 1.8 mm across. A feldspar crystal stretches across one quarter of the field. Estimate its length, then the field of view at 400x.", steps=[
            S("Grain length", math=r"\dfrac{1.8}{4} = 0.45 \text{ mm}"),
            S("Field at 400x", math=r"1.8 \times \dfrac{100}{400} = 0.45 \text{ mm}", text="Four times the magnification gives one quarter of the field width."),
            S("Use", text="0.45 mm is medium grained on most igneous grain-size scales; check the scale your textbook uses."),
        ]),
        EX("Worked example 3: reasoning from observations", intro="A colourless mineral with high relief stays black when the stage is rotated with the analyser in. Suggest what it might be.", steps=[
            S("Black in every position in XPL", text="The grain is isotropic, or it is an anisotropic mineral cut along an optic axis."),
            S("Use other evidence", text="High relief and an equant, rounded or six- or eight-sided outline fit garnet; a low-relief colourless grain could be glass or a basal section of quartz."),
            S("Conclusion", text="Probably garnet, but check several grains: if other grains of the same mineral show colours, it is anisotropic and this grain was a special section."),
        ]),
        MISTAKE("Mixing up colour and interference colour", "Colour and pleochroism are seen in PPL and are real absorption colours. Interference colours appear only in XPL and depend on birefringence and thickness, not on the mineral's real colour."),
        MISTAKE("Calling opaque minerals isotropic", "Opaque minerals let no light through, so they are black in PPL too. Isotropic minerals are transparent in PPL and black only in XPL."),
        MISTAKE("Not rotating the stage", "Pleochroism, extinction and twinning are seen only on rotation. Record what happens through a full turn."),
        QUIZ("Which property can be observed only with the analyser inserted?",
             ["Pleochroism", "Relief", "Interference colours", "Cleavage"], 2,
             "Interference colours arise when light split by an anisotropic mineral recombines at the analyser.",
             hint="Which property needs crossed polars?",
             feedback=["Pleochroism is seen in PPL as a change in colour on rotation.", "Relief is seen in PPL.", "", "Cleavage is seen best in PPL."]),
        QUIZ("A thin section is ground to 30 micrometres mainly so that",
             ["it fits on the stage", "interference colours of the same mineral can be compared between sections", "opaque minerals become transparent", "the rock does not break"], 1,
             "Interference colour depends on thickness; a standard thickness makes colours diagnostic.",
             hint="What changes with thickness in XPL?",
             feedback=["Any size slide fits; thickness is not about fitting.", "", "Opaque minerals stay opaque even at 30 micrometres.", "Thinner sections are actually more fragile."]),
        TIP("Exam link: Paper 1 asks for functions of parts and differences between PPL and XPL. Paper 2 may ask you to describe how to identify minerals in thin section, with a labelled diagram of the microscope. In Paper 3, describe a mineral or rock in a set order: PPL properties, then XPL properties."),
        H("Practice"),
        PQ("State the function of the analyser, the Bertrand lens and the rotating stage.",
           "Analyser: a second polarizer at 90 degrees to the lower one; inserted, it gives crossed polars so that interference colours and extinction can be seen. Bertrand lens: brings the interference figure into view (conoscopic observation) to tell uniaxial from biaxial minerals and find the optic sign. Rotating stage: turns the section so that pleochroism and extinction can be seen and angles measured on its degree scale."),
        PQ("List four properties observed in PPL and three in XPL.",
           "PPL: colour, pleochroism, relief, cleavage (also habit, alteration, inclusions). XPL: isotropic or anisotropic, interference colours (birefringence), extinction type and angle (also twinning and zoning)."),
        PQ("At 40x the field of view is 4.5 mm. A grain spans 0.3 of the field. How long is the grain, and what is the field of view at 100x?",
           r"Grain: $0.3 \times 4.5 = 1.35$ mm. Field at 100x: $4.5 \times 40/100 = 1.8$ mm."),
        SUM("A thin section is 30 micrometres thick, so standard interference colours can be compared.",
            "Parts from the bottom: light, polarizer, condenser and iris, rotating stage, objectives, accessory slot, analyser, Bertrand lens, eyepiece with cross-wires.",
            "PPL shows colour, pleochroism, relief, habit and cleavage; XPL shows isotropy, interference colours, extinction and twinning.",
            "Isotropic grains stay black in XPL; anisotropic grains go to extinction four times per turn; opaque grains are black in both.",
            "Magnification = objective x eyepiece; the field of view shrinks in proportion."),
    ],
))

# ------------------------------------------------------------------ 11. Optical properties
LESSONS.append(lesson(
    module=M3,
    topic="Optical properties of minerals",
    title="Relief, birefringence, interference colours, extinction and twinning",
    slug="gyl1-optical-properties",
    minutes=25,
    summary="Refractive index controls relief and the Becke line. Anisotropic minerals split light into two rays: birefringence times thickness gives the retardation and interference colour, and extinction angles, pleochroism and twinning complete the identification.",
    objectives=[
        "Explain relief and use the Becke line to compare refractive indices",
        "Distinguish isotropic, uniaxial and biaxial minerals and link them to crystal systems",
        "Calculate retardation from birefringence and thickness and relate it to interference colours",
        "Describe and measure straight, inclined and symmetrical extinction, and recognise twinning",
    ],
    key_concepts=["Refractive index", "Relief", "Becke line", "Double refraction", "Uniaxial", "Biaxial", "Birefringence", "Retardation", "Interference colour", "Extinction angle", "Twinning"],
    blocks=[
        H("Introduction"),
        T("In thin section, quartz and plagioclase are both colourless. How does a geologist tell them apart? By how they bend light, how bright their colours are between crossed polars, "
          "how they go into extinction and how they are twinned. Each of these optical properties comes from the crystal structure."),
        D(r"The **refractive index** $n$ of a mineral is the speed of light in a vacuum divided by its speed in the mineral: $n = c/v$. Most rock-forming minerals have $n$ between about 1.48 and 1.80.", title="Refractive index"),
        H("Relief and the Becke line"),
        D("**Relief** is how strongly a grain's outline and surface stand out against its surroundings. It depends on the difference between the refractive index of the mineral and that of the mounting medium (about 1.54). "
          "Quartz and feldspars (n close to 1.54) have **low relief**; olivine and pyroxenes have **high** relief; garnet has very high relief.", title="Relief"),
        T("The **Becke line** is a thin bright line along the grain boundary. When the focus is raised (the stage lowered), the Becke line moves **into the material of higher refractive index**. "
          "This tells you whether a grain has higher or lower n than the mounting medium or a neighbouring grain."),
        H("Isotropic and anisotropic minerals"),
        KEY("Optical classes", "The optical class follows from the crystal system.", cards=[
            ["Isotropic", "One refractive index; light travels at one speed in all directions. Cubic minerals (garnet, fluorite, halite) and glass. Black in all positions in XPL."],
            ["Uniaxial", "Tetragonal, hexagonal and trigonal minerals. Light is split into two rays except along one direction, the **optic axis**, parallel to c. Examples: quartz, calcite, zircon."],
            ["Biaxial", "Orthorhombic, monoclinic and triclinic minerals. Two optic axes. Examples: olivine, pyroxenes, amphiboles, micas, feldspars."],
        ]),
        T("In an anisotropic mineral, light entering in most directions splits into two rays that vibrate at right angles and travel at different speeds (**double refraction**). Calcite shows this so strongly that a clear cleavage rhomb doubles the image of a dot."),
        H("Birefringence and interference colours"),
        F(r"\delta = n_{high} - n_{low} \qquad \Delta = d \times \delta", title="Birefringence and retardation"),
        T(r"The **birefringence** $\delta$ is the difference between the highest and lowest refractive indices. The slow ray falls behind the fast ray by the **retardation** $\Delta$ (path difference), "
          r"which depends on birefringence and the thickness $d$. When the rays recombine at the analyser, some wavelengths cancel and an **interference colour** results. "
          r"Colours are grouped into orders: first-order greys, white, yellow and red (red at about 550 nm), then the brighter second and third orders, then pale high-order whites. "
          r"The **Michel-Levy chart** links retardation, thickness and birefringence."),
        EX("Worked example 1: quartz and calcite in a standard section", intro="Quartz has birefringence 0.009 and calcite 0.172. The section is 30 micrometres (30 000 nm) thick. Find each retardation and the expected colour.", steps=[
            S("Quartz", math=r"\Delta = 30\,000 \times 0.009 = 270 \text{ nm}", text="First-order grey to white: the typical colour of quartz."),
            S("Calcite", math=r"\Delta = 30\,000 \times 0.172 = 5160 \text{ nm}", text="Very high order: pale, pearly high-order white with faint pink and green tints."),
        ]),
        EX("Worked example 2: is the section too thick?", intro="In a student's section, quartz shows first-order yellow, about 400 nm. Estimate the thickness.", steps=[
            S("Rearrange", math=r"d = \dfrac{\Delta}{\delta} = \dfrac{400}{0.009} = 44\,000 \text{ nm}"),
            S("Answer", text="About 44 micrometres: thicker than the standard 30, so all interference colours in it are too high."),
        ]),
        T("Interference colour also depends on how the grain is cut. A section parallel to the optic axis shows the highest colour; a section at right angles to an optic axis stays dark. "
          "So use the **highest colour** shown by grains of a mineral when estimating its birefringence."),
        H("Extinction"),
        D("An anisotropic grain goes black (**extinction**) when the vibration directions of its two rays are parallel to those of the polarizer and analyser. This happens every 90 degrees of rotation. "
          "The **extinction angle** is the angle between the extinction position and a crystal feature such as a cleavage or long edge.", title="Extinction"),
        IMG("algyl1-extinction.svg", alt="Two grains seen between crossed polars, both dark. Left: cleavage traces parallel to the vertical cross-wire, straight extinction. Right: cleavage traces inclined to the vertical cross-wire, with the extinction angle marked",
            caption="Figure 1. Straight and inclined extinction."),
        KEY("Types of extinction", "Typical examples; values vary with composition and section, so check your textbook.", cards=[
            ["Straight (parallel)", "Extinct when the cleavage or length is parallel to a cross-wire. Orthopyroxene, biotite and muscovite (nearly), and elongate sections of orthorhombic minerals."],
            ["Inclined", "Extinct at an angle to the cleavage. Clinopyroxene (augite, roughly 35-45 degrees) and hornblende (smaller, roughly 12-30 degrees)."],
            ["Symmetrical", "Extinction bisects the angle between two cleavages, as in basal sections of amphiboles and pyroxenes."],
        ]),
        EX("Worked example 3: measuring an extinction angle", intro="A grain's cleavage is set parallel to the N-S cross-wire at a stage reading of 112 degrees. The grain goes into extinction at 150 degrees.", steps=[
            S("Angle turned", math=r"150^{\circ} - 112^{\circ} = 38^{\circ}"),
            S("Interpret", text="An inclined extinction angle of 38 degrees on a prismatic grain with two cleavages fits augite rather than an orthopyroxene."),
        ]),
        H("Pleochroism and twinning"),
        T("**Pleochroism** is a change in colour as the stage is rotated in PPL, because the two rays are absorbed differently. Biotite changes from dark brown to pale straw; hornblende from green to yellow-brown. "
          "**Twinning** is the symmetrical intergrowth of two or more crystals of one mineral. In XPL the parts go into extinction at different positions: **simple (Carlsbad) twins** in orthoclase and sanidine, "
          "**polysynthetic (lamellar) twins** in plagioclase (stripes), and **cross-hatched (tartan) twinning** in microcline."),
        MISTAKE("Moving the Becke line the wrong way", "With the focus raised (stage lowered) the Becke line moves into the material of higher refractive index. If you lower the focus, it moves the other way. Always say which way you moved the focus."),
        MISTAKE("Measuring extinction from the cross-wire, not from the cleavage", "The extinction angle is between the cleavage (or long edge) and the extinction position. Set the cleavage on a cross-wire first, note the reading, then rotate to extinction."),
        QUIZ("Which mineral has the highest interference colours in a standard thin section?",
             ["Quartz", "Orthoclase", "Calcite", "Garnet"], 2,
             "Calcite's birefringence (about 0.17) gives very high-order colours.",
             hint="Largest birefringence gives the largest retardation.",
             feedback=["Quartz shows only first-order grey and white.", "Orthoclase shows first-order grey.", "", "Garnet is isotropic and stays black."]),
        QUIZ("A mineral with a single optic axis must belong to which group of systems?",
             ["Cubic", "Tetragonal, hexagonal or trigonal", "Orthorhombic, monoclinic or triclinic", "Any system"], 1,
             "Uniaxial minerals have a unique c axis of high symmetry: tetragonal, hexagonal and trigonal.",
             hint="Which systems have a single unique axis?",
             feedback=["Cubic minerals are isotropic.", "", "These are biaxial.", "The optical class depends on the system."]),
        TIP("Exam link: Paper 1 often asks about relief, Becke line movement, birefringence and extinction types. Paper 2 can ask how optical properties distinguish named minerals (for example quartz from feldspar, or augite from hornblende)."),
        H("Practice"),
        PQ("Explain how quartz and orthoclase can be distinguished in thin section.",
           "Both are colourless with low relief and first-order grey interference colours. Orthoclase often shows Carlsbad (simple) twinning, has a lower refractive index than the mounting medium (Becke line moves out into the medium), shows cleavage and is often cloudy from alteration to clay. Quartz has no cleavage or twinning, is clear and unaltered, has a refractive index slightly above the medium and may show undulose (wavy) extinction."),
        PQ("A mineral of birefringence 0.036 is in a 30-micrometre section. Calculate the retardation and say which order of colours you expect (one order is about 550 nm).",
           r"$\Delta = 30\,000 \times 0.036 = 1080$ nm. $1080/550 \approx 2$, so near the top of the second order: bright second-order colours. This fits olivine."),
        PQ("In a 30-micrometre section a mineral shows maximum colours at about 1 100 nm. Estimate its birefringence.",
           r"$\delta = \Delta/d = 1100/30\,000 = 0.037$."),
        PQ("Describe the twinning used to recognise plagioclase and microcline.",
           "Plagioclase shows polysynthetic (lamellar) twinning: many thin parallel bands that are alternately light and dark in XPL. Microcline shows cross-hatched (tartan) twinning, two sets of fine twins at nearly right angles."),
        SUM("Relief depends on the difference in refractive index from the mounting medium; the Becke line moves into the higher-index material when the focus is raised.",
            "Cubic minerals are isotropic; tetragonal, hexagonal and trigonal are uniaxial; orthorhombic, monoclinic and triclinic are biaxial.",
            r"Retardation $\Delta = d\delta$ fixes the interference colour; quartz shows first-order grey and white, calcite high-order white.",
            "Extinction may be straight, inclined (measure the angle from the cleavage) or symmetrical.",
            "Pleochroism (biotite, hornblende) and twinning (Carlsbad, polysynthetic, cross-hatched) help identification."),
    ],
))

# ------------------------------------------------------------------ 12. Silicate structures
LESSONS.append(lesson(
    module=M3,
    topic="Silicate structures",
    title="Silicate structures: from isolated tetrahedra to frameworks",
    slug="gyl1-silicate-structures",
    minutes=24,
    summary="The silica tetrahedron links by sharing oxygens to form isolated, paired, ring, chain, sheet and framework silicates. The degree of sharing fixes the Si:O ratio, the charge to be balanced, and properties such as cleavage and order of crystallisation.",
    objectives=[
        "Describe the SiO4 tetrahedron and explain how tetrahedra polymerise by sharing oxygens",
        "Classify silicates as neso-, soro-, cyclo-, ino-, phyllo- and tectosilicates with Si:O ratios and examples",
        "Calculate the charge of a silicate unit and explain substitution of Al for Si and of Fe for Mg",
        "Relate structure to cleavage and to the order of crystallisation in Bowen's reaction series",
    ],
    key_concepts=["Silica tetrahedron", "Bridging oxygen", "Polymerisation", "Nesosilicate", "Inosilicate", "Phyllosilicate", "Tectosilicate", "Si:O ratio", "Ionic substitution", "Solid solution"],
    blocks=[
        H("Introduction"),
        T("About nine-tenths of the Earth's crust is made of silicate minerals. From the green olivine in the basalts of the Cameroon Volcanic Line to the mica and feldspar of granites, "
          "they are all built from one unit, the silica tetrahedron, joined in different ways. How the tetrahedra join explains their formulae, cleavage and the order in which they crystallise from magma."),
        D(r"The **silica tetrahedron** is one silicon ion (Si$^{4+}$) surrounded by four oxygen ions (O$^{2-}$) at the corners of a tetrahedron. Its charge is $4 - 4(2) = -4$, written $(\text{SiO}_4)^{4-}$. "
          r"The Si-O bond is very strong (roughly half ionic and half covalent). Tetrahedra join by sharing corner oxygens, called **bridging oxygens**; this is **polymerisation**.", title="The silica tetrahedron"),
        IMG("algyl1-silicates.svg", alt="Plan views of silica tetrahedra as triangles with a central silicon dot: isolated tetrahedra; a single chain; a double chain forming six-membered rings; and a continuous sheet of six-membered rings",
            caption="Figure 1. Isolated, single-chain, double-chain and sheet silicates (plan view; each triangle is one tetrahedron)."),
        H("The structural classes"),
        CODE("""
Class            Linkage                     O shared per    Unit         Si:O    Examples
                                             tetrahedron
Nesosilicate     isolated tetrahedra              0          SiO4         1:4     olivine, garnet, zircon
Sorosilicate     pairs                            1          Si2O7        2:7     epidote (with SiO4 also)
Cyclosilicate    rings (usually of six)           2          Si6O18       1:3     beryl, tourmaline
Inosilicate      single chains                    2          SiO3 (Si2O6) 1:3     pyroxenes (augite, enstatite)
Inosilicate      double chains                  2 and 3      Si4O11       4:11    amphiboles (hornblende)
Phyllosilicate   sheets                           3          Si2O5        2:5     micas, chlorite, clay minerals, talc
Tectosilicate    3-D framework                    4          SiO2         1:2     quartz, feldspars, feldspathoids
""", "text", title="Silicate classes in order of increasing polymerisation"),
        T(r"As more oxygens are shared, the Si:O ratio rises from 1:4 towards 1:2 and the negative charge per silicon falls from $-4$ to 0. The negative charge is balanced by metal cations "
          r"(Mg$^{2+}$, Fe$^{2+}$, Ca$^{2+}$, Na$^{+}$, K$^{+}$, Al$^{3+}$) that sit between the tetrahedra and bond them together."),
        EX("Worked example 1: charge of a silicate unit", intro="Calculate the charge of the double-chain unit Si4O11 and of the sorosilicate unit Si2O7.", steps=[
            S("Double chain", math=r"4(+4) + 11(-2) = 16 - 22 = -6 \Rightarrow (\text{Si}_4\text{O}_{11})^{6-}"),
            S("Pair", math=r"2(+4) + 7(-2) = 8 - 14 = -6 \Rightarrow (\text{Si}_2\text{O}_7)^{6-}"),
        ]),
        EX("Worked example 2: why a double chain is Si4O11", intro="Explain the Si:O ratio of an amphibole double chain by counting oxygens.", steps=[
            S("Repeat unit", text="The repeat of a double chain contains 4 tetrahedra: 2 share 2 oxygens each and 2 share 3 oxygens each."),
            S("Count oxygens", text="An unshared oxygen counts 1; a shared oxygen counts 1/2. Tetrahedra sharing 2 own 2 + 2(1/2) = 3 O. Tetrahedra sharing 3 own 1 + 3(1/2) = 2.5 O."),
            S("Total", math=r"2(3) + 2(2.5) = 11 \Rightarrow \text{Si}_4\text{O}_{11},\ \text{Si:O} = 4:11 = 0.36"),
        ], check=r"\text{single chain: } 1 \cdot 2 + 2 \cdot \tfrac{1}{2} = 3 \Rightarrow \text{SiO}_3"),
        H("Substitution and solid solution"),
        T(r"Ions of similar size and charge can replace each other in a structure (**ionic substitution**). Fe$^{2+}$ and Mg$^{2+}$ have the same charge and similar radii, so olivine ranges continuously "
          r"from Mg$_2$SiO$_4$ (forsterite) to Fe$_2$SiO$_4$ (fayalite): a **solid solution series**. Al$^{3+}$ can replace Si$^{4+}$ inside tetrahedra; the lost positive charge is made up by an extra cation. "
          r"In plagioclase the coupled substitution Ca$^{2+}$Al$^{3+}$ for Na$^{+}$Si$^{4+}$ links albite NaAlSi$_3$O$_8$ to anorthite CaAl$_2$Si$_2$O$_8$."),
        EX("Worked example 3: charge balance in orthoclase", intro=r"Show that orthoclase, KAlSi$_3$O$_8$, is neutral and explain why K is needed.", steps=[
            S("Positive charges", math=r"\text{K}^{+} + \text{Al}^{3+} + 3\,\text{Si}^{4+} = 1 + 3 + 12 = +16"),
            S("Negative charges", math=r"8\,\text{O}^{2-} = -16"),
            S("Explain", text="A pure SiO2 framework is neutral. Replacing one Si4+ by Al3+ in every four leaves a charge of -1, which K+ (large, in cavities of the framework) balances."),
        ]),
        H("Structure and properties"),
        KEY("Structure controls behaviour", "Use these links in Paper 2 essays.", cards=[
            ["Cleavage", "Breaks run along weak cation-oxygen bonds, never through tetrahedra. Pyroxene chains give two cleavages at about 87 and 93 degrees; wider amphibole double chains give about 56 and 124 degrees; mica sheets give one perfect basal cleavage; the quartz framework has no weak planes, so quartz has no cleavage (conchoidal fracture)."],
            ["Order of crystallisation", "In Bowen's reaction series, minerals with little polymerisation (olivine) crystallise first at high temperature, then pyroxene, amphibole and biotite, and the framework silicates quartz, K-feldspar and muscovite last at low temperature."],
            ["Ferromagnesian or felsic", "Ferromagnesian (mafic) silicates contain Fe and Mg and are dark and dense (olivine, pyroxene, amphibole, biotite). Felsic silicates are light and less dense (quartz, feldspars, muscovite)."],
        ]),
        MISTAKE("Saying cleavage breaks the tetrahedra", "Si-O bonds are the strongest in the structure. Cleavage follows the weaker bonds between cations and oxygens, between chains or sheets."),
        MISTAKE("Mixing up cyclosilicates and single chains", "Both have Si:O = 1:3, but rings are closed (beryl, tourmaline) while chains are endless (pyroxenes). Give the structure, not just the ratio."),
        QUIZ("Which silicate class has a Si:O ratio of 2:5?",
             ["Nesosilicate", "Single-chain inosilicate", "Phyllosilicate", "Tectosilicate"], 2,
             "Sheets share three oxygens per tetrahedron: Si2O5.",
             hint="Three oxygens shared per tetrahedron.",
             feedback=["Isolated tetrahedra are SiO4 (1:4).", "Single chains are SiO3 (1:3).", "", "Frameworks are SiO2 (1:2)."]),
        QUIZ("Why can Fe2+ substitute for Mg2+ in olivine?",
             ["Both are metals", "They have the same charge and similar ionic radii", "Fe is heavier than Mg", "Olivine contains no oxygen"], 1,
             "Substitution needs similar size and charge so the structure is not strained.",
             hint="What must a substituting ion match?",
             feedback=["Many metals cannot substitute for each other.", "", "Mass is not the controlling factor.", "Olivine is a silicate: it contains oxygen."]),
        TIP("Exam link: Paper 1 frequently asks for Si:O ratios, structural classes and examples. Paper 2 essays ask you to describe silicate structures with diagrams and relate them to cleavage and Bowen's reaction series; the Board's 2023 report noted confusion about the pyroxene structure."),
        H("Practice"),
        PQ("Describe the structure of a pyroxene and state how it explains the cleavage.",
           "Pyroxenes are single-chain inosilicates. Each SiO4 tetrahedron shares two oxygens with its neighbours, forming continuous chains with unit formula Si2O6 (Si:O = 1:3). The chains are linked by cations such as Mg2+, Fe2+ and Ca2+. Cleavage runs between the chains along the weaker cation-oxygen bonds, giving two prismatic cleavages at nearly 90 degrees (about 87 and 93 degrees)."),
        PQ("Calculate the charge of the ring unit Si6O18 and the Si:O ratio.",
           r"Charge $= 6(+4) + 18(-2) = 24 - 36 = -12$. Si:O = 6:18 = 1:3."),
        PQ("Explain why the tectosilicate quartz has no cleavage while mica has one perfect cleavage.",
           "In quartz every oxygen is shared between two tetrahedra in a three-dimensional framework of strong Si-O bonds, so there is no plane of weakness and it fractures conchoidally. In mica the tetrahedra form sheets, and sheets are held together by weaker bonds through K+ ions; the mineral splits easily parallel to the sheets."),
        SUM(r"The SiO$_4$ tetrahedron has charge $-4$; tetrahedra polymerise by sharing corner oxygens.",
            "Neso (SiO4), soro (Si2O7), cyclo (Si6O18), single chain (SiO3), double chain (Si4O11), sheet (Si2O5), framework (SiO2).",
            "More sharing raises the Si:O ratio from 1:4 to 1:2 and lowers the charge to be balanced by cations.",
            "Fe-Mg substitution makes solid solutions; Al for Si in tetrahedra is balanced by K, Na or Ca.",
            "Structure controls cleavage and the order of crystallisation in Bowen's series."),
    ],
))

# ------------------------------------------------------------------ 13. Rock-forming silicate minerals
LESSONS.append(lesson(
    module=M3,
    topic="Rock-forming silicate minerals",
    title="Rock-forming silicates: olivine, pyroxenes, amphiboles, micas, feldspars and quartz",
    slug="gyl1-rock-forming-silicates",
    minutes=25,
    summary="Learn the chemistry, crystal system, hand-specimen and thin-section properties and occurrence of the main rock-forming silicates, including the olivine and plagioclase solid solution series and how to name them by composition.",
    objectives=[
        "Give the formula, structure type and crystal system of the main rock-forming silicates",
        "Identify them in hand specimen and thin section from diagnostic properties",
        "Use forsterite and anorthite percentages to name olivine and plagioclase compositions",
        "Explain why olivine and quartz do not normally occur together",
    ],
    key_concepts=["Olivine", "Orthopyroxene", "Clinopyroxene", "Hornblende", "Biotite", "Muscovite", "Alkali feldspar", "Plagioclase series", "Quartz", "Garnet", "Forsterite content", "Anorthite content"],
    blocks=[
        H("Introduction"),
        T("A geologist mapping the granites and gneisses of southern Cameroon or the basalts of the West Region needs to name the minerals in each rock quickly. "
          "Only about a dozen silicate minerals make up most igneous and metamorphic rocks. This lesson gathers their key properties so that you can identify them in Paper 3 and explain them in Paper 2."),
        CODE("""
Mineral        Formula (simplified)              Structure       System         H       Cleavage
Olivine        (Mg,Fe)2SiO4                      isolated        orthorhombic   6.5-7   poor; conchoidal fracture
Garnet         e.g. Fe3Al2(SiO4)3                isolated        cubic          6.5-7.5 none
Enstatite/     (Mg,Fe)SiO3                       single chain    orthorhombic   5-6     2 at about 88/92
 hypersthene
Augite         (Ca,Na)(Mg,Fe,Al)(Si,Al)2O6       single chain    monoclinic     5-6     2 at about 87/93
Hornblende     complex Ca-Na-Mg-Fe-Al with OH    double chain    monoclinic     5-6     2 at about 56/124
Biotite        K(Mg,Fe)3AlSi3O10(OH)2            sheet           monoclinic     2.5-3   1 perfect basal
Muscovite      KAl2AlSi3O10(OH)2                 sheet           monoclinic     2-2.5   1 perfect basal
Orthoclase     KAlSi3O8                          framework       monoclinic     6       2 at 90
Plagioclase    NaAlSi3O8 to CaAl2Si2O8           framework       triclinic      6       2 at about 86/94
Quartz         SiO2                              framework       trigonal       7       none; conchoidal fracture
""", "text", title="Key data for the rock-forming silicates (H = Mohs hardness)",
             caption="Cleavage angles and hardness ranges are typical values; check your textbook."),
        H("The ferromagnesian minerals"),
        KEY("Olivine, pyroxenes and amphiboles", "Dark (mafic) minerals rich in Fe and Mg.", cards=[
            ["Olivine", "Hand: olive-green, glassy, granular, no good cleavage. Thin section: colourless, high relief, bright second- and third-order colours, irregular cracks, often altered to green serpentine along cracks. In basalt, gabbro and peridotite."],
            ["Pyroxenes", "Hand: dark green to black stubby prisms with two cleavages almost at right angles, vitreous lustre. Thin section: augite pale green or colourless, moderate-high relief, second-order colours, inclined extinction (about 35-45 degrees); orthopyroxene has low colours and straight extinction, hypersthene is pink-green pleochroic. In basalt, gabbro, andesite."],
            ["Hornblende", "Hand: black, elongated prisms, two cleavages at about 56 and 124 degrees. Thin section: strongly pleochroic green to yellow-brown, inclined extinction (smaller than augite), diamond-shaped basal sections. Contains OH, so it forms from wetter magmas: diorite, andesite, granite, amphibolite."],
        ]),
        KEY("Micas", "Sheet silicates with one perfect cleavage. Biotite is a mica: do not list mica and biotite as two different minerals.", cards=[
            ["Biotite", "Hand: black or dark brown, splits into thin elastic flakes. Thin section: strongly pleochroic brown to pale straw, near-straight extinction, mottled ('bird's eye') at extinction. In granite, schist, gneiss."],
            ["Muscovite", "Hand: silvery, colourless flakes. Thin section: colourless, bright second- to third-order colours, near-straight extinction. In granite, pegmatite, schist."],
        ]),
        H("The felsic minerals"),
        KEY("Feldspars and quartz", "Light-coloured, low relief, first-order colours.", cards=[
            ["Alkali feldspars", "Orthoclase (monoclinic) is often pink or white with two cleavages at 90 degrees and Carlsbad twins; sanidine is the high-temperature form in lavas; microcline (triclinic) shows cross-hatched twinning in XPL. Often cloudy from alteration to clay."],
            ["Plagioclase", "White to grey; fine parallel striations (twin lamellae) on cleavage surfaces in hand specimen; polysynthetic twinning and often zoning in thin section."],
            ["Quartz", "Hardness 7, no cleavage, conchoidal fracture, glassy. Thin section: clear, low relief, first-order grey and white, no alteration, sometimes wavy (undulose) extinction from strain."],
        ]),
        D("Plagioclase forms a complete solid solution from **albite** NaAlSi$_3$O$_8$ to **anorthite** CaAl$_2$Si$_2$O$_8$. Its composition is given as the percentage of anorthite (An): "
          "albite An 0-10, oligoclase 10-30, andesine 30-50, labradorite 50-70, bytownite 70-90, anorthite 90-100. Calcic plagioclase crystallises at higher temperature (the continuous series of Bowen).", title="The plagioclase series"),
        D("Olivine ranges from **forsterite** Mg$_2$SiO$_4$ to **fayalite** Fe$_2$SiO$_4$. The forsterite number Fo = 100 x Mg / (Mg + Fe), using atoms per formula. Mantle olivine is about Fo90.", title="The olivine series"),
        EX("Worked example 1: naming compositions", intro="(a) An olivine contains 1.6 Mg and 0.4 Fe atoms per formula. (b) A plagioclase contains Ca and Na in the ratio 65 : 35. Name each.", steps=[
            S("Olivine", math=r"\text{Fo} = 100 \times \dfrac{1.6}{1.6 + 0.4} = 80", text="Fo80: a magnesium-rich olivine."),
            S("Plagioclase", text="Ca/(Ca + Na) = 0.65, so An65. An 50-70 is labradorite."),
        ]),
        EX("Worked example 2: why olivine and quartz do not occur together", intro="Explain, with an equation, why forsterite and quartz are not found together in igneous rocks.", steps=[
            S("Silica content", text="Forsterite contains about 43 percent SiO2 by mass; it is silica-poor (undersaturated)."),
            S("Reaction", math=r"\text{Mg}_2\text{SiO}_4 + \text{SiO}_2 \rightarrow 2\,\text{MgSiO}_3", text="Forsterite plus silica react to form enstatite (orthopyroxene)."),
            S("Conclusion", text="If enough silica is present, olivine is used up to make pyroxene before quartz can crystallise. So olivine marks silica-poor rocks (basalt, gabbro) and quartz marks silica-rich rocks (granite, rhyolite)."),
        ], check=r"\text{Mg: } 2 = 2;\ \text{Si: } 1 + 1 = 2;\ \text{O: } 4 + 2 = 6"),
        EX("Worked example 3: identifying a hand specimen", intro="A pink mineral scratches glass but not quartz (hardness about 6), has two cleavages at right angles and a vitreous lustre. Identify it.", steps=[
            S("Hardness 6, two cleavages", text="Fits a feldspar, not quartz (H 7, no cleavage) or calcite (H 3)."),
            S("Pink colour and right-angle cleavage", text="Fits orthoclase; plagioclase is usually white or grey with striations."),
            S("Answer", text="Orthoclase feldspar."),
        ]),
        MISTAKE("Describing a mineral as a rock", "Pyroxene, hornblende and feldspar are minerals; basalt and granite are rocks. In a question on pyroxenes, give structure, crystal system, forms and physical properties of the mineral."),
        MISTAKE("Misspelling mineral names", "Write albite, oligoclase, andesine, labradorite, bytownite, anorthite exactly; examiners noted spellings such as 'byetowrite'."),
        QUIZ("Which mineral has two cleavages at about 56 and 124 degrees?",
             ["Augite", "Hornblende", "Orthoclase", "Biotite"], 1,
             "The double-chain structure of amphiboles gives this pair of cleavages.",
             hint="Double chains give oblique cleavages.",
             feedback=["Augite cleavages are nearly at right angles.", "", "Orthoclase cleavages are at 90 degrees.", "Biotite has one perfect basal cleavage."]),
        QUIZ("A plagioclase has composition An40. What is it called?",
             ["Oligoclase", "Andesine", "Labradorite", "Bytownite"], 1,
             "An 30-50 is andesine.",
             hint="Learn the boundaries at 10, 30, 50, 70 and 90.",
             feedback=["Oligoclase is An 10-30.", "", "Labradorite is An 50-70.", "Bytownite is An 70-90."]),
        TIP("Exam link: Paper 3 hand-specimen questions ask you to describe and identify minerals such as orthoclase, quartz and mica; give hardness, colour, cleavage and lustre. Paper 2 essays ask for a full description of a mineral group (structure, chemistry, crystallography, physical and optical properties, occurrence)."),
        H("Practice"),
        PQ("Describe the pyroxene group under the headings structure, crystallography and diagnostic physical properties.",
           "Structure: single-chain inosilicates; each tetrahedron shares two oxygens; unit Si2O6 (Si:O 1:3); chains linked by Mg2+, Fe2+ and Ca2+. Crystallography: monoclinic (augite, diopside) or orthorhombic (enstatite, hypersthene); stubby prisms with pinacoids. Physical properties: two prismatic cleavages at nearly 90 degrees, hardness 5-6, dark green to black, vitreous lustre, specific gravity about 3.2-3.6."),
        PQ("Calculate the mass percentage of SiO2 in forsterite, Mg2SiO4 (Mg = 24.3, Si = 28.1, O = 16.0).",
           r"Molar mass of Mg$_2$SiO$_4$ = 2(24.3) + 28.1 + 4(16.0) = 140.7. SiO$_2$ = 28.1 + 32.0 = 60.1. Percentage = 60.1/140.7 x 100 = 42.7 percent."),
        PQ("How would you distinguish biotite from hornblende in thin section?",
           "Both are pleochroic, but biotite occurs as flakes with one perfect cleavage, has near-straight extinction and a mottled appearance at extinction, and is brown to straw-coloured. Hornblende forms prisms with two cleavages at about 56 and 124 degrees (seen in basal sections), shows inclined extinction in long sections and is usually green to brown."),
        SUM("Olivine, pyroxenes, amphiboles and biotite are ferromagnesian; feldspars, quartz and muscovite are felsic.",
            "Cleavage separates pyroxene (about 90 degrees), amphibole (56/124), micas (one basal) and quartz (none).",
            "Plagioclase is named by An percent: albite, oligoclase, andesine, labradorite, bytownite, anorthite.",
            "Olivine is named by Fo number; olivine plus silica gives pyroxene, so olivine and quartz do not coexist.",
            "Describe minerals in order: hand specimen (colour, lustre, hardness, cleavage, habit), then PPL, then XPL."),
    ],
))

# ------------------------------------------------------------------ 14. Non-silicate and ore minerals
LESSONS.append(lesson(
    module=M3,
    topic="Non-silicate and ore minerals",
    title="Non-silicate minerals and ore minerals: classes, identification and metal content",
    slug="gyl1-non-silicate-ore-minerals",
    minutes=24,
    summary="Native elements, sulfides, oxides, carbonates, sulfates and halides include the main ore minerals. Identify them by streak, lustre, hardness, density and simple tests, and calculate metal content and ore grade.",
    objectives=[
        "Classify non-silicate minerals by their anion group, with formulae and examples",
        "Identify common ore and non-silicate minerals from diagnostic properties",
        "Define ore, ore mineral, gangue and grade, and calculate metal content and recoverable metal",
        "Name examples of mineral deposits in Cameroon and their ore minerals",
    ],
    key_concepts=["Native element", "Sulfide", "Oxide", "Carbonate", "Sulfate", "Halide", "Ore", "Ore mineral", "Gangue", "Grade", "Streak", "Specific gravity"],
    blocks=[
        H("Introduction"),
        T("Cameroon has important mineral resources: bauxite on the Adamawa plateau and in the West, iron ore in the South and East, cobalt and nickel near Lomie, "
          "and alluvial gold worked by small-scale miners in the East. Most of the metals come from non-silicate minerals. Knowing these minerals and how much metal they hold is the basis of economic geology."),
        D("Non-silicate minerals are classified by their **anion** (negative) group: **native elements** (one element, such as gold), **sulfides** (S$^{2-}$), **oxides** (O$^{2-}$) and hydroxides (OH$^{-}$), "
          "**halides** (Cl$^{-}$, F$^{-}$), **carbonates** (CO$_3^{2-}$), **sulfates** (SO$_4^{2-}$) and **phosphates** (PO$_4^{3-}$).", title="Classes of non-silicate minerals"),
        CODE("""
Mineral        Formula        Class        Lustre / colour            Streak               H        SG     Key feature
Gold           Au             native       metallic, golden yellow    golden yellow        2.5-3    19     malleable, very heavy
Graphite       C              native       metallic-dull, black       black                1-2      2.2    greasy, marks paper
Pyrite         FeS2           sulfide      metallic, brass yellow     greenish black       6-6.5    5.0    striated cubes, brittle
Chalcopyrite   CuFeS2         sulfide      metallic, deep brass       greenish black       3.5-4    4.2    tarnishes, softer than pyrite
Galena         PbS            sulfide      metallic, lead grey        lead grey            2.5      7.5    cubic cleavage, very heavy
Sphalerite     ZnS            sulfide      resinous, brown-black      pale brown-yellow    3.5-4    4.0    6 cleavage directions
Haematite      Fe2O3          oxide        metallic or earthy         red-brown            5.5-6.5  5.3    cherry-red streak
Magnetite      Fe3O4          oxide        metallic, black            black                5.5-6.5  5.2    strongly magnetic
Cassiterite    SnO2           oxide        adamantine, brown-black    pale brown-white     6-7      7.0    heavy for a non-metallic
Calcite        CaCO3          carbonate    vitreous, colourless-white white                3        2.7    fizzes in cold dilute HCl
Gypsum         CaSO4.2H2O     sulfate      vitreous-silky             white                2        2.3    scratched by fingernail
Baryte         BaSO4          sulfate      vitreous, white            white                3-3.5    4.5    heavy for a light mineral
Halite         NaCl           halide       vitreous, colourless       white                2.5      2.2    cubic cleavage, salty
Fluorite       CaF2           halide       vitreous, purple-green     white                4        3.2    octahedral cleavage
""", "text", title="Common non-silicate minerals (typical values; check your textbook)"),
        H("Identifying ore minerals"),
        T("Colour is unreliable: haematite can be steel-grey or red, and pyrite looks like gold. The **streak** (colour of the powder on unglazed porcelain) is more constant. "
          "**Specific gravity** is felt by hefting: metallic ores such as galena feel very heavy. Simple tests help: magnetite attracts a magnet; calcite fizzes in cold dilute hydrochloric acid while dolomite fizzes only when powdered. "
          "In thin section most ore minerals are **opaque**, so they are studied in polished section with a reflected-light microscope."),
        EX("Worked example 1: gold or pyrite?", intro="A student finds yellow metallic grains in a quartz vein. Describe two quick tests to decide whether they are gold or pyrite.", steps=[
            S("Streak", text="Gold leaves a golden-yellow streak; pyrite leaves a greenish-black streak."),
            S("Hardness and tenacity", text="Gold is soft (2.5-3) and malleable: a pin dents it. Pyrite is hard (6-6.5), cannot be scratched by a knife and is brittle."),
            S("Density", text="Gold (SG about 19) is far heavier than pyrite (SG about 5) and collects in the pan when panned."),
        ]),
        H("Ores, grade and metal content"),
        D("An **ore** is a rock from which a metal or mineral can be extracted at a profit. The **ore mineral** contains the valuable element (for example haematite for iron); the waste minerals are the **gangue** (often quartz, calcite or baryte). "
          "The **grade** is the concentration of metal in the ore, and the **cut-off grade** is the lowest grade that is profitable to mine; it changes with metal prices and costs.", title="Ore terms"),
        F(r"\%\ \text{metal in a mineral} = \dfrac{\text{mass of metal atoms in formula}}{\text{molar mass of formula}} \times 100", title="Metal content"),
        EX("Worked example 2: iron in haematite and magnetite", intro=r"Fe = 55.85, O = 16.00. Which mineral contains more iron by mass: haematite Fe$_2$O$_3$ or magnetite Fe$_3$O$_4$?", steps=[
            S("Haematite", math=r"\dfrac{2(55.85)}{2(55.85) + 3(16.00)} = \dfrac{111.7}{159.7} = 69.9\%"),
            S("Magnetite", math=r"\dfrac{3(55.85)}{3(55.85) + 4(16.00)} = \dfrac{167.55}{231.55} = 72.4\%"),
            S("Compare", text="Magnetite is slightly richer in iron, and it can be separated magnetically."),
        ]),
        EX("Worked example 3: grade and recoverable metal", intro="(a) A banded iron ore contains 40 percent haematite by mass and the rest quartz. Find its iron grade. (b) A copper deposit contains 2 million tonnes of ore at 1.5 percent Cu, and the plant recovers 85 percent. How much copper is produced?", steps=[
            S("(a) Grade", math=r"0.40 \times 69.9\% = 28.0\%\ \text{Fe}"),
            S("(b) Metal in the ore", math=r"2\,000\,000 \times 0.015 = 30\,000 \text{ t}"),
            S("(b) Recovered", math=r"30\,000 \times 0.85 = 25\,500 \text{ t Cu}"),
        ]),
        KEY("Examples from Cameroon", "Well-known occurrences; check the current status of projects and production with your teacher.", cards=[
            ["Bauxite", "An aluminium ore formed by intense tropical weathering; mainly the hydroxide gibbsite, Al(OH)3. Large deposits at Minim-Martap and Ngaoundal (Adamawa) and Fongo-Tongo (West)."],
            ["Iron ore", "Iron formations rich in haematite and magnetite, for example around Mbalam and Nkout in the south and east."],
            ["Cobalt, nickel and manganese", "Laterite deposits near Lomie (East), formed by weathering of ultramafic rocks."],
            ["Gold and rutile", "Alluvial gold is worked in the East and Adamawa regions. Rutile (TiO2) was mined in the past in the Centre region; check your textbook."],
        ]),
        MISTAKE("Calling bauxite a mineral", "Bauxite is a rock (an ore) made of several aluminium hydroxide minerals, mainly gibbsite, with clay and iron oxides."),
        MISTAKE("Confusing a rock with its mineral", "Marble is a rock made of calcite; limestone is a rock made mostly of calcite. Name the mineral when asked for a mineral and the rock when asked for a rock."),
        MISTAKE("Relying on colour", "Use streak, hardness, cleavage, lustre and specific gravity together. The Board's 2023 report gives red streak, metallic lustre and high specific gravity as the evidence for haematite."),
        QUIZ("A heavy, black, metallic mineral gives a black streak and attracts a magnet. What is it?",
             ["Haematite", "Magnetite", "Galena", "Graphite"], 1,
             "Magnetism and a black streak identify magnetite.",
             hint="Which iron oxide is magnetic?",
             feedback=["Haematite gives a red-brown streak and is at most weakly magnetic.", "", "Galena has a lead-grey streak, cubic cleavage and is not magnetic.", "Graphite is light (SG about 2.2) and soft."]),
        QUIZ("Which mineral fizzes in cold dilute hydrochloric acid?",
             ["Quartz", "Gypsum", "Calcite", "Baryte"], 2,
             "Carbonate reacts with acid to release carbon dioxide.",
             hint="Which mineral contains carbonate?",
             feedback=["Quartz does not react with dilute acids.", "Gypsum is a sulfate; it does not fizz.", "", "Baryte is a sulfate; it does not fizz."]),
        TIP("Exam link: Paper 3 hand-specimen questions often include ore minerals such as haematite, galena or pyrite: give streak, lustre, hardness, specific gravity and any test. Paper 1 tests formulae and classes. Paper 2 can ask about ore minerals and their uses, and metal-content calculations."),
        H("Practice"),
        PQ("Define ore, gangue and cut-off grade.",
           "Ore: a rock from which a metal or useful mineral can be extracted at a profit. Gangue: the worthless minerals that occur with the ore minerals, such as quartz or calcite. Cut-off grade: the lowest concentration of metal in the ore that can be mined and processed at a profit; it changes with prices and costs."),
        PQ("Calculate the percentage of lead in galena, PbS (Pb = 207.2, S = 32.1).",
           r"$\dfrac{207.2}{207.2 + 32.1} \times 100 = \dfrac{207.2}{239.3} \times 100 = 86.6$ percent."),
        PQ("Calculate the percentage of copper in chalcopyrite, CuFeS2 (Cu = 63.5, Fe = 55.8, S = 32.1), and explain why a chalcopyrite ore may still have a low copper grade.",
           r"Molar mass = 63.5 + 55.8 + 2(32.1) = 183.5. Cu = 63.5/183.5 x 100 = 34.6 percent. The ore grade depends on how much chalcopyrite is in the rock: if the rock contains only 3 percent chalcopyrite, the grade is about 3 x 0.346 = 1.0 percent Cu."),
        SUM("Non-silicates are classified by anion: native elements, sulfides, oxides and hydroxides, halides, carbonates, sulfates and phosphates.",
            "Identify ore minerals by streak, lustre, hardness, specific gravity, magnetism and acid tests; most are opaque in thin section.",
            "Ore, ore mineral, gangue, grade and cut-off grade are economic terms.",
            "Metal percent = mass of metal atoms over molar mass x 100; grade = mineral fraction x metal percent.",
            "Cameroon examples: bauxite (gibbsite), iron ore (haematite, magnetite), cobalt-nickel laterites and alluvial gold."),
    ],
))
