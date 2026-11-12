"""A Level Food Science and Nutrition (0740), Upper Sixth: Food Engineering & Preservation Technology,
Post-Harvest Commodity Technology, and Food Quality Assurance & Legislation.
14 lessons, one per topic, one practice set each (see the practice file of the same name).

Scope notes: the outline comes from KKEVO's master curriculum blueprint, not a Board syllabus booklet. Facts are the
standard A Level ones; where textbooks differ the lesson says "check your textbook". Numbers in worked data are teaching
data and are labelled. Cameroonian standards and institutions are stated only in general terms ("check the current
rules"). Exam comments paraphrase the GCE Board's 2023 Advanced Level subject report. Clinical and safety teaching is
for study only.
"""

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "upper-sixth")

M1 = "Food Engineering & Preservation Technology"
M2 = "Post-Harvest Commodity Technology"
M3 = "Food Quality Assurance & Legislation"

LESSONS = []

# ------------------------------------------------------------------ 1. Thermal processing kinetics
LESSONS.append(lesson(
    module=M1,
    topic="Thermal processing kinetics",
    title="Thermal death kinetics: D-value, z-value, F0 and blanching",
    slug="fsu1-thermal-processing-kinetics",
    minutes=25,
    summary="Heat kills micro-organisms at a predictable (first-order) rate. Use the D-value, z-value and F0 to calculate how long a food must be heated, and explain why blanching is used before freezing, canning and drying.",
    objectives=[
        "Explain thermal death as a first-order process and use the D-value to calculate survivors and heating time",
        "Use the z-value to convert D-values and heating times between temperatures",
        "Define F0 and the 12D concept, and calculate F0 from a temperature record",
        "Explain the purposes, method and effects of blanching",
    ],
    key_concepts=["Thermal death", "D-value", "z-value", "F0-value", "12D concept", "Lethal rate", "Blanching", "Peroxidase test"],
    blocks=[
        H("Introduction"),
        T("A can of sardines or tomato paste from a shop in Douala may sit in a hot warehouse for a year and still be safe to eat. "
          "The reason is not luck. The food was heated inside a sealed can for a carefully calculated time. Too little heat leaves "
          "dangerous spores alive; too much heat wrecks the colour, flavour and vitamins. **Thermal processing kinetics** is the "
          "science that finds the right balance by measuring how fast heat kills micro-organisms."),
        H("Thermal death is a first-order process"),
        T("When a population of bacteria or spores is held at a constant lethal temperature, the same *fraction* of them dies in each "
          "equal period of time. If 90% die in the first 2 minutes, 90% of the survivors die in the next 2 minutes, and so on. This is "
          "a **first-order** (logarithmic) death. It means a few cells always survive for a while, and the number of survivors can only be "
          "reduced to a very small chance, never exactly to zero."),
        D("The **D-value** (decimal reduction time) is the time at a stated constant temperature needed to destroy 90% of the "
          "organisms, that is, to reduce their number by one factor of ten (one log cycle). It is written $D_T$, for example $D_{121.1}$.",
          title="D-value", formula=r"D = \frac{t}{\log_{10} N_0 - \log_{10} N}", note="t is the heating time, N0 the starting number, N the number surviving."),
        F(r"\log_{10} N = \log_{10} N_0 - \frac{t}{D}", title="Survivor equation"),
        IMG("alfsu1-survivor-curve.svg", alt="Graph of log10 of the number of survivors against heating time: a straight line falling from 6 to 0 over 12 minutes; one log cycle is a fall of 2 minutes, which is the D-value",
            caption="Figure 1. A survivor curve: on a log scale death is a straight line. The time for one log cycle is D."),
        T("A bigger D-value means a more heat-resistant organism. Bacterial **spores** (for example of *Clostridium botulinum*, the cause of "
          "botulism) have far larger D-values than the ordinary growing (vegetative) cells of *Salmonella*. The D-value also depends on the "
          "food: acid, fat and low water activity change it. That is why published D-values apply only to the stated food and temperature."),
        EX("Worked example 1: survivors and heating time",
           intro="A food contains $10^{6}$ spores per can. The spores have D = 2.0 min at the process temperature. (a) How long must the can be heated to reduce the count to $10^{2}$ per can? (b) How many spores per can remain after 6 minutes? (Teaching data.)",
           steps=[
               S("(a) Number of log cycles needed", math=r"\log_{10}(10^6) - \log_{10}(10^2) = 6 - 2 = 4"),
               S("Time = number of log cycles times D", math=r"t = 4 \times 2.0 = 8.0 \text{ min}"),
               S("(b) Log cycles killed in 6 min", math=r"\frac{6}{2.0} = 3 \text{ log cycles}"),
               S("Survivors", math=r"10^6 \times 10^{-3} = 10^3 = 1000 \text{ spores per can}"),
           ], check=r"\log_{10} N = 6 - \frac{8}{2} = 2"),
        H("The z-value: how D changes with temperature"),
        D("The **z-value** is the rise in temperature needed to reduce the D-value to one tenth (one log cycle). A small z means the "
          "organism's heat resistance changes quickly with temperature. For the spores that matter in canning, z is about 10 °C. "
          "For many vegetative bacteria and enzymes z is larger or smaller, so always use the value given.",
          title="z-value", formula=r"z = \frac{T_2 - T_1}{\log_{10} D_1 - \log_{10} D_2}"),
        IMG("alfsu1-tdt-curve.svg", alt="Graph of log D against temperature: a straight line falling from D = 12 minutes at 100 degrees to D = 0.012 minutes at 130 degrees; a rise of 10 degrees cuts D by a factor of ten, so z = 10 degrees",
            caption="Figure 2. The thermal death time (TDT) curve. The temperature rise for one log cycle of D is z."),
        F(r"D_T = D_{ref} \times 10^{\frac{T_{ref} - T}{z}}", title="D at another temperature"),
        T("Heating hotter shortens the time enormously. With z = 10 °C, raising the temperature by 10 °C cuts the time by ten times. This is "
          "why high-temperature short-time processes can protect quality: the microbes die much faster than flavour and vitamins are lost, "
          "because the quality factors usually have a *larger* z-value (about 25 to 40 °C)."),
        EX("Worked example 2: finding z and a new D-value",
           intro="A spore has D = 12 min at 100 °C and D = 1.2 min at 110 °C. Find z, then find D and the time for a 6-log reduction at 115 °C. (Teaching data.)",
           steps=[
               S("Find z", math=r"z = \frac{110 - 100}{\log_{10} 12 - \log_{10} 1.2} = \frac{10}{1} = 10\,{}^\circ\text{C}"),
               S("D at 115 °C", math=r"D_{115} = 12 \times 10^{(100-115)/10} = 12 \times 10^{-1.5} = 0.379 \text{ min}"),
               S("Time for 6 log cycles", math=r"t = 6 \times 0.379 = 2.28 \text{ min}"),
           ]),
        H("The F-value and F0"),
        D("The **F-value** is the equivalent time, at a stated reference temperature, of all the heat a food receives. It is the total lethal effect "
          "of the process expressed as minutes at the reference temperature. **F0** (F-zero) is the F-value for the reference temperature "
          "121.1 °C (250 °F) with z = 10 °C. It is the standard measure of the sterilising value of a canning process.",
          title="F0-value"),
        F(r"F_0 = \int_0^t 10^{\frac{T - 121.1}{10}}\,dt \;\approx\; \Delta t \sum L, \qquad L = 10^{\frac{T-121.1}{10}}", title="Lethal rate and F0"),
        T("The **lethal rate** L compares the killing at temperature T with the killing at 121.1 °C. At 121.1 °C, L = 1. At 111.1 °C, L = 0.1 "
          "(ten times slower). At 131.1 °C, L = 10. Because the temperature inside a can changes with time, you add up the lethal rates "
          "recorded at the **cold spot** (the slowest-heating point) to get the F0 delivered."),
        KEY("The 12D concept", "The minimum botulinum cook for low-acid canned food is to reduce the spores of *Clostridium botulinum* by 12 log cycles (12D), so that a chance of survival is about one in $10^{12}$ spores.", cards=[
            ["Teaching D-value", "D121.1 is about 0.25 min for the spores (published values are often quoted between about 0.1 and 0.25 min; check your textbook)."],
            ["Minimum F0", "12 times 0.25 = 3.0 min. Commercial processes use a larger F0 to include other, more resistant spoilage spores and a safety margin."],
            ["Result", "A starting load of 1000 spores per can falls to $10^{3}$ times $10^{-12}$ = $10^{-9}$ spores per can: about one can in a billion."],
        ]),
        EX("Worked example 3: calculating F0 from a cold-spot record",
           intro="A thermocouple in the cold spot of a can records the temperatures below every 2 minutes (invented for practice). Calculate F0 and say whether it reaches a target F0 of 6 min.",
           steps=[
               S("Calculate the lethal rate at each reading", text="Use L = 10^((T - 121.1)/10). Examples: at 110 °C, L = 10^(-1.11) = 0.078; at 119 °C, L = 10^(-0.21) = 0.617."),
               S("Add the lethal rates", math=r"\sum L = 0.008+0.078+0.309+0.617+1+1+0.490+0.078 = 3.58"),
               S("Multiply by the time interval", math=r"F_0 \approx 3.58 \times 2 = 7.16 \approx 7.2 \text{ min}"),
               S("Compare with the target", text="7.2 min is greater than 6 min, so the process meets the target. Heating the can longer than needed only damages quality."),
           ]),
        CODE("""Time (min)   Cold-spot T (C)   L = 10^((T-121.1)/10)
  2            100               0.008
  4            110               0.078
  6            116               0.309
  8            119               0.617
 10            121.1             1.000
 12            121.1             1.000
 14            118               0.490
 16            110               0.078
                          Sum L = 3.580
         F0 = 3.580 x 2 min = 7.16 min""", "text", title="Table 1. F0 from a heat-penetration record (teaching data)"),
        EX("Worked example 4: an equivalent process at a lower temperature",
           intro="A process needs F0 = 3.0 min. How long would the cold spot need at 115 °C and at 110 °C, if the temperature were held constant? (z = 10 °C.)",
           steps=[
               S("Formula", math=r"t = F_0 \times 10^{(121.1 - T)/10}"),
               S("At 115 °C", math=r"t = 3.0 \times 10^{0.61} = 3.0 \times 4.07 = 12.2 \text{ min}"),
               S("At 110 °C", math=r"t = 3.0 \times 10^{1.11} = 3.0 \times 12.9 = 38.6 \text{ min}"),
               S("Meaning", text="Each 10 °C drop multiplies the time by ten, so low temperatures need much longer, with more damage to quality."),
           ]),
        H("Blanching"),
        D("**Blanching** is a short heat treatment, with steam or hot water at about 70 to 100 °C for seconds to a few minutes, followed by quick cooling. "
          "It is not meant to sterilise. It is applied to vegetables and some fruits before freezing, canning or drying.", title="Blanching"),
        KEY("Why blanch?", "Learn the purposes and the side effects.", cards=[
            ["Inactivates enzymes", "Peroxidase, catalase, polyphenol oxidase and lipoxygenase would otherwise cause off-flavours, browning and loss of colour during frozen or dried storage."],
            ["Colour and texture", "Green vegetables turn a brighter green (air is driven from the tissue); some tissues soften and shrink so cans fill better."],
            ["Cleans and reduces microbes", "Removes dirt and some surface micro-organisms and cuts the load before canning."],
            ["Costs", "Loss of water-soluble vitamins (such as vitamin C) and minerals by leaching, and heat damage; use steam or short times to limit loss. The hot waste water is a pollution load."],
        ]),
        T("**Peroxidase test.** Peroxidase is a relatively heat-stable enzyme that is easy to test for, so it is used as an indicator of adequate "
          "blanching. A cut piece of the vegetable is treated with a hydrogen peroxide and guaiacol solution. A brown-red colour means peroxidase "
          "is still active, so blanching was too short. No colour means the enzyme was destroyed."),
        MISTAKE("Saying the D-value is the time to kill all the organisms", "D is the time to kill 90% (one log cycle). Because death is logarithmic, you must multiply D by the number of log cycles. The process designer chooses the number of cycles from the hazard."),
        MISTAKE("Mixing up D and z", "D is a *time* (minutes) at one temperature. z is a *temperature* (degrees) that changes D by a factor of ten. Check the units of your answer."),
        MISTAKE("Thinking blanching sterilises", "Blanching stops enzymes and cleans the food. A blanched vegetable still needs freezing, drying, acidifying or canning to keep safely."),
        QUIZ("An organism has D = 3 min at a given temperature. Starting from $10^{5}$ cells, how long does it take to reach $10^{1}$ cells?",
             ["4 min", "12 min", "15 min", "30 min"], 1,
             "From $10^{5}$ to $10^{1}$ is 4 log cycles. Time = 4 times 3 min = 12 min.",
             hint="Count the log cycles first, then multiply by D.",
             feedback=["This is the number of log cycles, not the time.", "", "This uses 5 log cycles (the starting exponent) instead of the 4 cycles between $10^{5}$ and $10^{1}$.", "This treats D as the time to kill everything and multiplies by 10."]),
        QUIZ("A spore has z = 10 °C. Heating at 111.1 °C instead of 121.1 °C, the process time must be about",
             ["10 times shorter", "the same", "10 times longer", "2 times longer"], 2,
             "Lowering the temperature by one z-value makes D ten times longer, so the time for the same effect is ten times longer.",
             hint="A fall of one z changes D by what factor, and in which direction?",
             feedback=["Heating less hot cannot shorten the time: the direction is reversed.", "The time is unchanged only if the temperature is unchanged.", "", "Doubling is not related to a log cycle."]),
        H("Practice"),
        PQ("Define D-value and z-value.", "The D-value is the time, at a constant stated temperature, for a 90% reduction (one log cycle) in the number of viable organisms. The z-value is the temperature change needed to change the D-value by a factor of ten (one log cycle)."),
        PQ("Spores in a food have D = 0.5 min at 121.1 °C. Calculate the time at 121.1 °C to reduce $10^{4}$ spores per can to $10^{-3}$ spores per can (a chance of one in a thousand that a can contains a survivor).", "Log cycles = 4 - (-3) = 7. Time = 7 x 0.5 = 3.5 min. The result $10^{-3}$ per can means that on average one can in a thousand holds a live spore."),
        PQ("A spore has D = 20 min at 90 °C and D = 2 min at 100 °C. Find z and the D-value at 110 °C.", "z = (100 - 90)/(log 20 - log 2) = 10/1 = 10 °C. D at 110 °C = 2 x 10^((100-110)/10) = 2 x $10^{-1}$ = 0.2 min."),
        PQ("Explain why blanching is used before freezing vegetables, and how you would check that it was adequate.", "Freezing slows but does not stop enzymes such as peroxidase and lipoxygenase, which cause off-flavour, browning and colour loss during storage. Blanching destroys them. It also brightens colour, removes air and cleans the food. To check: the peroxidase test (guaiacol and hydrogen peroxide); no brown-red colour shows the enzyme is inactive. Limit losses by using steam or short times and cooling fast."),
        TIP("Exam link: thermal processing is examined in Paper 1 (D, z, F0 definitions and simple calculations), in Paper 2 (food science and preservation essays) and as the theory behind canning and pasteurisation. Show every log-cycle step in a calculation and give units (minutes, °C)."),
        SUM("Thermal death of microbes is first-order: equal times kill equal fractions, so survivors fall as a straight line on a log scale.",
            "D-value = time at one temperature for a 90% (one log) reduction; time = number of log cycles times D.",
            "z-value = temperature rise for D to fall ten-fold; D at another temperature = D(ref) times 10^((Tref - T)/z).",
            "F0 = sterilising value expressed as minutes at 121.1 °C (z = 10 °C); the 12D cook for botulinum is about 3 min with D = 0.25 min (teaching value).",
            "Blanching inactivates enzymes, brightens colour and cleans food; it costs some vitamins, and the peroxidase test checks it."),
    ],
))

# ------------------------------------------------------------------ 2. Pasteurization and canning
LESSONS.append(lesson(
    module=M1,
    topic="Pasteurization and canning",
    title="Pasteurisation, UHT treatment and canning (commercial sterilisation)",
    slug="fsu1-pasteurization-canning",
    minutes=25,
    summary="Pasteurisation destroys pathogens with mild heat but is not sterilisation; canning achieves commercial sterility for shelf-stable food. Compare the time-temperature combinations, the equipment, the pH 4.6 rule and the causes of can spoilage.",
    objectives=[
        "Distinguish pasteurisation, UHT treatment and commercial sterilisation, with typical conditions and their purposes",
        "Describe an HTST plant and calculate a holding-tube volume and the saving from regeneration",
        "Explain the pH 4.6 rule and list the stages of canning, saying why each is done",
        "Identify the main types and causes of can spoilage and the tests used to detect them",
    ],
    key_concepts=["Pasteurisation", "HTST and LTLT", "UHT and aseptic packaging", "Alkaline phosphatase test", "Commercial sterility", "Low-acid and acid foods", "Exhausting and double seam", "Cold spot", "Flat sour and swells"],
    blocks=[
        H("Introduction"),
        T("A carton of UHT milk can stand on a shop shelf in Yaoundé for months, but a bag of pasteurised milk or yoghurt must stay "
          "cold and is used within days. A tin of tomato paste lasts years. All three foods were heat-treated, but with very different "
          "aims. This lesson sorts out those aims and the conditions used for each."),
        D("**Pasteurisation** is a mild heat treatment (below 100 °C for most foods) that destroys pathogens and reduces the number of spoilage "
          "organisms and enzymes. Pasteurised food is not sterile, so it needs a second hurdle such as refrigeration, low pH or packaging "
          "to keep. The process was named after Louis Pasteur, who studied heating wine and beer to stop spoilage.", title="Pasteurisation"),
        KEY("Typical milk heat treatments", "Conditions vary a little between countries; learn these standard values and check your textbook.", cards=[
            ["LTLT (batch or holder)", "About 63 °C for 30 min. Simple equipment; used in small dairies."],
            ["HTST (continuous)", "About 72 °C for 15 s in a plate heat exchanger. The most common method for fresh milk."],
            ["UHT", "About 135 to 150 °C for a few seconds, then aseptic packaging. Shelf-stable for months without a refrigerator."],
            ["In-container sterilisation", "About 115 to 120 °C for 10 to 20 min in sealed bottles or cans. Cooked flavour and colour."],
        ]),
        T("**What is the target?** The conditions must destroy the most heat-resistant non-spore-forming pathogen present. For milk, textbooks "
          "name *Mycobacterium tuberculosis* in the past and *Coxiella burnetii* (the cause of Q fever) today; check your textbook. HTST and LTLT "
          "also destroy *Salmonella*, *Listeria* and *Brucella*, but they do not kill bacterial spores."),
        H("The HTST plant"),
        T("In a high-temperature short-time plant the milk flows continuously through thin channels between stainless steel plates:"),
        KEY("Route of the milk", "Follow the milk in order.", cards=[
            ["1 Balance tank and pump", "Raw milk, held cold at about 4 °C, is fed at a steady rate."],
            ["2 Regeneration section", "Hot pasteurised milk warms the incoming cold milk (heat recovery) and is itself pre-cooled."],
            ["3 Heating section", "Hot water or steam heats the milk to 72 °C or more."],
            ["4 Holding tube", "Its length and diameter give a residence time of at least 15 s at the pasteurising temperature."],
            ["5 Flow diversion valve", "If the temperature falls below the set point, the valve sends under-heated milk back to the start."],
            ["6 Regeneration and cooling sections", "The milk gives heat to cold milk and is cooled to about 4 °C, then packed."],
        ]),
        EX("Worked example 1: the holding-tube volume",
           intro="A plant treats 2 000 litres per hour and must hold the milk at 72 °C for at least 15 s. What volume must the holding tube have? If its internal diameter is 5 cm, how long must it be, on the simple assumption that all the milk moves at the average speed?",
           steps=[
               S("Flow in litres per second", math=r"\frac{2000}{3600} = 0.556 \text{ L/s}"),
               S("Volume = flow times time", math=r"0.556 \times 15 = 8.33 \text{ L} = 8.33 \times 10^{-3} \text{ m}^3"),
               S("Cross-section of the tube", math=r"A = \pi \times 0.025^2 = 1.96 \times 10^{-3} \text{ m}^2"),
               S("Length", math=r"L = \frac{8.33 \times 10^{-3}}{1.96 \times 10^{-3}} = 4.24 \text{ m}"),
               S("Real design", text="Some milk moves faster than the average, in the centre of the tube. A real holding tube is designed for the fastest-moving particle, so it is longer than 4.24 m."),
           ]),
        EX("Worked example 2: why regeneration saves energy",
           intro="1 000 litres of milk (1.03 kg per litre; specific heat 3.93 kJ per kg per °C) are heated from 4 °C to 72 °C. Find the heat needed with no heat recovery and with 90% regeneration. (Teaching values.)",
           steps=[
               S("Mass", math=r"1000 \times 1.03 = 1030 \text{ kg}"),
               S("Heat with no recovery", math=r"Q = m c \Delta T = 1030 \times 3.93 \times 68 = 275\,000 \text{ kJ} \approx 275 \text{ MJ}"),
               S("With 90% regeneration", text="The incoming milk is pre-heated to 4 + 0.9 x 68 = 65.2 °C by the outgoing milk. Only the last 6.8 °C is heated by the utility: 10% of the heat, about 27.5 MJ."),
           ]),
        H("Checking that milk was pasteurised"),
        KEY("Tests", "Enzyme tests show whether the heat treatment was right.", cards=[
            ["Alkaline phosphatase test", "This enzyme is destroyed at slightly more than the pasteurising conditions. It must be negative: a positive result means under-heating or raw milk added."],
            ["Peroxidase test", "Peroxidase survives normal pasteurisation. A negative result shows the milk was heated much too hot (above about 80 °C)."],
            ["Methylene blue or resazurin reduction", "Estimates the bacterial quality of the milk: a faster colour loss means more bacteria."],
        ]),
        H("UHT treatment and aseptic packaging"),
        T("UHT (ultra-high temperature) treatment gives *commercial sterility* with a very short, very hot heating, so the nutrients and flavour "
          "suffer less than in a long in-can process. It can be **direct** (steam is injected into the milk, then the added water is flashed off "
          "under vacuum) or **indirect** (plate or tubular heat exchangers). The sterile product is then packed into sterile cartons "
          "in a sterile environment: **aseptic packaging**. Any contamination after the heat treatment ruins the benefit, so hygiene at the "
          "filling machine is critical."),
        H("Canning and commercial sterility"),
        D("**Commercial sterility** means that the food is free of micro-organisms that can grow under normal non-refrigerated storage and "
          "free of pathogens and their toxins. It does not mean that every spore has been destroyed.", title="Commercial sterility"),
        D("A **low-acid food** has a pH above 4.6 (meat, fish, most vegetables, milk, many soups). An **acid food** has a pH of 4.6 or below "
          "(most fruit, tomatoes with added acid, pickles). *Clostridium botulinum* spores cannot germinate and make toxin below about pH 4.6.",
          title="The pH 4.6 rule"),
        T("Low-acid foods therefore need a **retort** (a pressure vessel) with steam at about 115 to 121 °C and a process with a calculated F0 "
          "(see the last lesson). Acid foods can be heated at 100 °C or less, in boiling water or by hot-fill, because the survivors cannot grow."),
        IMG("alfsu1-canning-flow.svg", alt="Flow diagram of canning: receive and wash, peel and blanch, fill with brine and headspace, exhaust, double seam, retort, cool in chlorinated water, then dry, label, store and incubate",
            caption="Figure 1. The stages of canning a low-acid food."),
        KEY("Why each stage is done", "Examiners ask for the purpose, not only the name.", cards=[
            ["Blanching and filling", "Blanching removes enzymes and air; fill weight and a small headspace leave room for expansion."],
            ["Exhausting", "Removing air (by heating, steam flow or vacuum) lowers the pressure, reduces oxidation and corrosion, and avoids the can bulging in the retort."],
            ["Double seaming", "Interlocks the lid and body to form an airtight, hermetic seal that stops recontamination."],
            ["Retorting", "Heats the sealed can to the calculated F0. Pressure in the retort stops the can from bursting as the contents expand."],
            ["Cooling", "Cans are cooled quickly (to about 40 °C) in chlorinated water to stop overcooking. A seam can briefly draw in a little water as the vacuum forms, so the water must be clean and cans must be handled dry afterwards."],
        ]),
        T("**Heat penetration.** The time depends on how fast the cold spot heats. In a liquid or thin soup, **convection** currents mix the contents "
          "and the cold spot is on the axis near the bottom. In a thick paste, solid meat or a packed product, heat moves only by "
          "**conduction**, so the geometric centre heats slowly and the time is much longer. Larger cans, thick contents and a low retort temperature "
          "all lengthen the process."),
        H("Spoilage of canned foods"),
        KEY("Types of spoilage", "Learn the clue and the cause.", cards=[
            ["Under-processing", "Spoilage by organisms that survived: the process F0 was too low or the cold-spot time was wrong."],
            ["Flat sour", "Thermophilic spore-formers (such as *Geobacillus stearothermophilus*) make acid without gas; the can ends stay flat but the food is sour."],
            ["Thermophilic gas swell", "Thermophilic anaerobes make gas; the can bulges. Common if cans are stored in a hot warehouse."],
            ["Hydrogen swell", "Not microbial: acid food attacks the tin plate and releases hydrogen. Cans with acid contents are usually lacquered."],
            ["Leaker spoilage", "Faulty seams or dirty cooling water let bacteria in after processing. Mixed bacteria in the can are the clue."],
        ]),
        T("**Quality control.** Seams are measured and cut open for inspection; samples of each batch are **incubated** (often at 37 °C and, for "
          "thermophiles, 55 °C) for several days and examined for swelling, pH change and microbes. A swollen can must never be opened or "
          "tasted: it may contain botulinum toxin."),
        MISTAKE("Saying pasteurised milk is sterile", "Pasteurisation kills pathogens and most vegetative bacteria, but spores and some others survive. That is why pasteurised milk must be kept cold and has a short shelf life."),
        MISTAKE("Using pH 4.6 loosely", "The 4.6 limit divides low-acid from acid foods because of *Clostridium botulinum*. A food with pH 6.5 is low-acid and needs a retort process. Do not say that all fruits are acid foods without checking."),
        QUIZ("Which test must be NEGATIVE if milk has been correctly pasteurised?",
             ["Peroxidase", "Alkaline phosphatase", "Methylene blue", "Turbidity"], 1,
             "Alkaline phosphatase is destroyed at slightly higher than pasteurising conditions, so a negative test means the milk was heated enough.",
             hint="Which enzyme is destroyed by correct pasteurisation?",
             feedback=["Peroxidase survives correct pasteurisation, so it should be positive.", "", "This test gives a microbial quality estimate, not a yes or no for heating.", "The turbidity test is used for sterilised milk, not for pasteurised."]),
        QUIZ("A can of cooked beef (pH 6.2) swells in a warm store room. Its seam is perfect. The most likely cause is",
             ["Hydrogen swell", "Leaker spoilage", "Thermophilic spoilage after under-processing", "A dent in the can body"], 2,
             "A perfect seam rules out leaker spoilage. Meat is low-acid, so hydrogen swell is unlikely. Gas from surviving thermophilic spore-formers in a warm store fits.",
             hint="Think about seams, then pH, then temperature of storage.",
             feedback=["Hydrogen swell happens with acid foods that attack the tin plate; this food is low-acid.", "A perfect seam makes leakage unlikely.", "", "A dent does not cause gas production; the swelling comes from gas made inside."]),
        H("Practice"),
        PQ("State two differences between pasteurisation and commercial sterilisation.", "Pasteurisation uses mild heat (below 100 °C), kills pathogens and most vegetative organisms but not spores, and needs refrigeration or another hurdle; shelf life is days to weeks. Commercial sterilisation uses higher temperatures (about 115 to 121 °C or UHT), destroys the spores that can grow in storage, and gives a shelf-stable product for months or years."),
        PQ("A plant pasteurises 3 600 litres of milk per hour at 72 °C for 15 s. Calculate the volume of the holding tube.", "Flow = 3 600 / 3 600 = 1 L/s. Volume = 1 x 15 = 15 L."),
        PQ("Explain why low-acid foods need a retort process but fruit can be processed in boiling water.", "Low-acid foods (pH above 4.6) allow spores of Clostridium botulinum to germinate and make toxin, so spores must be destroyed: this needs temperatures above 100 °C, which require a pressure retort. Acid foods (pH 4.6 or below) do not allow botulinum growth, so heating to 100 °C or less kills the acid-tolerant vegetative spoilage organisms and is enough."),
        PQ("Describe the stages of canning peas and give the purpose of exhausting and cooling in chlorinated water.", "Wash and grade, blanch, fill with hot brine leaving a headspace, exhaust, double-seam, retort at the calculated time and temperature, cool, dry, label, store and incubate samples. Exhausting removes air to lower oxidation and corrosion and prevent bulging. Chlorinated cooling water kills any bacteria drawn in through the seam while the can contracts, preventing leaker spoilage."),
        TIP("Exam link: pasteurisation and canning appear in Paper 1 (conditions, tests, spoilage types) and Paper 2 (processing essays: expect to describe the stages and give reasons). The Board's 2023 report notes flow diagrams of manufacturing processes were poorly drawn in some essays: practise drawing the canning flow with a purpose beside each stage."),
        SUM("Pasteurisation (63 °C for 30 min, 72 °C for 15 s) kills pathogens but not spores; the product still needs chilling.",
            "UHT (about 135 to 150 °C for seconds) with aseptic packaging gives commercial sterility with less damage to quality.",
            "Alkaline phosphatase must be negative in properly pasteurised milk; peroxidase positive.",
            "Low-acid foods (pH above 4.6) need retort sterilisation to an F0 that controls Clostridium botulinum; acid foods can be heated at 100 °C or less.",
            "Canning stages: blanch, fill, exhaust, double seam, retort, cool, store; spoilage includes flat sour, swells, under-processing and leakers."),
    ],
))

# ------------------------------------------------------------------ 3. Low-temperature preservation
LESSONS.append(lesson(
    module=M1,
    topic="Low-temperature preservation",
    title="Chilling, freezing and the cold chain",
    slug="fsu1-low-temperature-preservation",
    minutes=24,
    summary="Chilling slows spoilage; freezing makes water unavailable as ice. Learn how ice crystal size, freezing rate and storage temperature control quality, calculate the heat removed in freezing, and explain chilling injury, freezer burn and the cold chain.",
    objectives=[
        "Distinguish chilling from freezing and explain how low temperature preserves food",
        "Explain slow, quick and individual quick freezing (IQF) and their effect on ice crystals and quality",
        "Calculate the heat to be removed to freeze a food, including latent heat",
        "Explain chilling injury, freezer burn, recrystallisation, thawing drip and the importance of the cold chain",
    ],
    key_concepts=["Chilling", "Chilling injury", "Freezing curve and latent heat", "Slow and quick freezing", "IQF", "Cryogenic freezing", "Freezer burn", "Recrystallisation", "Cold chain"],
    blocks=[
        H("Introduction"),
        T("Fish on ice at a landing site in Limbe, chilled milk at a dairy, frozen chicken in a supermarket: all rely on cold. Low "
          "temperatures preserve food without cooking it, so the fresh appearance, flavour and most nutrients are kept. But cold only *slows* "
          "spoilage; it does not make food sterile. This lesson explains what cold does, how freezing works, and why a broken cold chain ruins quality."),
        D("**Chilling** is the cooling of food to a temperature just above its freezing point, usually between about -1 °C and 8 °C (a household "
          "refrigerator is about 0 to 5 °C). **Freezing** cools the food below its freezing point so that most of its water turns into ice, "
          "with frozen storage at -18 °C or lower.", title="Chilling and freezing"),
        H("How cold preserves food"),
        KEY("Three effects", "Learn all three for essays.", cards=[
            ["Slower reactions", "Chemical and enzyme reactions and microbial growth slow as temperature falls. A rough rule: the rate halves or more for every 10 °C fall (a Q10 of 2 to 3)."],
            ["Less available water", "In frozen food, ice is not available to microbes. The remaining unfrozen water holds the dissolved solutes, so its water activity falls."],
            ["Stops most growth", "Most bacteria and moulds stop growing below about -10 °C, and nothing grows at -18 °C. But enzymes and fat oxidation continue very slowly."],
        ]),
        H("Chilling"),
        T("Chilling extends shelf life by days or weeks. **Psychrotrophic** organisms (for example *Pseudomonas* in fish and meat, and *Listeria "
          "monocytogenes*) still grow slowly in a refrigerator, so chilled foods have a limited life and must be kept clean and cold from "
          "the start. Precooling, fast cooling after cooking, and keeping to a steady temperature are important."),
        EX("Worked example 1: the effect of temperature on shelf life",
           intro="A chilled fish product keeps for 6 days at 5 °C. Assume its shelf life halves for every 10 °C rise (Q10 = 2). Find the shelf life at 15 °C and at 25 °C. (Teaching data.)",
           steps=[
               S("From 5 °C to 15 °C", math=r"\frac{6}{2} = 3 \text{ days}"),
               S("From 5 °C to 25 °C", math=r"\frac{6}{4} = 1.5 \text{ days}"),
               S("Meaning", text="A fish left on a warm market table for a day uses up most of its life. Keeping cold at the right time is more important than the final cold store."),
           ]),
        T("**Chilling injury.** Many tropical and sub-tropical fruits and vegetables are damaged by temperatures that are cold but above freezing. Bananas "
          "chilled below about 12 to 13 °C turn dull and grey-brown and fail to ripen; mangoes, papaya, avocado and sweet potatoes also suffer, "
          "while the exact limits vary (check your textbook). Such produce is stored cool, not cold."),
        H("Freezing"),
        T("When food is cooled, its temperature falls to the **initial freezing point** (slightly below 0 °C, because dissolved sugars and salts lower the "
          "freezing point; for example about -1 to -2 °C for meat and fish). Ice then forms, and the temperature stays nearly constant for a long "
          "time because the latent heat of fusion of water must be removed. Only after most of the water has frozen does the temperature fall quickly."),
        IMG("alfsu1-freezing-curve.svg", alt="Freezing curve of a food: temperature falls from 20 degrees to about minus 1.5 degrees (A), then nearly levels off during the plateau when ice forms (B), then falls to storage temperature (C)",
            caption="Figure 1. A freezing curve: the plateau B is where most of the latent heat is removed."),
        D("**Latent heat of fusion**: the energy removed to change water into ice with no temperature change, about 334 kJ per kg of ice. "
          "It is much larger than the heat removed in cooling the same mass of food (about 3.5 kJ per kg per °C above freezing).", title="Latent heat"),
        F(r"Q = m c_1 (T_i - T_f) + m\, w\, x\, L + m c_2 (T_f - T_s)", title="Heat to freeze a food"),
        T("Here m is the mass, c1 and c2 are the specific heats above and below freezing, Ti the starting temperature, Tf the initial "
          "freezing point, Ts the storage temperature, w the fraction of water in the food, x the fraction of that water frozen at Ts, and L the latent heat."),
        EX("Worked example 2: the refrigeration load",
           intro="Find the heat to freeze 10 kg of meat from 15 °C to -18 °C. Water content 70%; 90% of the water is frozen at -18 °C; initial freezing point -1.5 °C; specific heat 3.5 kJ per kg per °C above freezing and 1.8 below; L = 334 kJ per kg. (Teaching values.)",
           steps=[
               S("Cool to the freezing point", math=r"10 \times 3.5 \times (15 - (-1.5)) = 10 \times 3.5 \times 16.5 = 577.5 \text{ kJ}"),
               S("Freeze the water", math=r"10 \times 0.70 \times 0.90 \times 334 = 6.3 \times 334 = 2104.2 \text{ kJ}"),
               S("Cool the frozen meat", math=r"10 \times 1.8 \times (-1.5 - (-18)) = 10 \times 1.8 \times 16.5 = 297 \text{ kJ}"),
               S("Total", math=r"577.5 + 2104.2 + 297 = 2978.7 \text{ kJ} \approx 0.83 \text{ kWh}"),
               S("Comment", text="About 71% of the heat is latent heat (2104.2 / 2978.7). This is why freezing takes far more energy than chilling."),
           ]),
        H("Slow and quick freezing"),
        T("The rate of freezing decides the size and place of the ice crystals. In **slow freezing** (for example in a domestic freezer or a big "
          "block), ice forms first *outside* the cells, draws water out of them and makes a few large crystals that distort and break cell walls. When thawed, "
          "the cells cannot reabsorb the water, so there is a large **drip loss**, a soft texture and a loss of soluble nutrients. In **quick freezing**, "
          "many small crystals form throughout the tissue, including inside cells, so there is less damage. (The rate is often judged by how fast the "
          "ice front moves through the food; for quick freezing figures of at least about 1 cm per hour are quoted: check your textbook.)"),
        KEY("Freezing methods", "Match the method to the product.", cards=[
            ["Air blast", "Very cold air (about -30 to -40 °C) at high speed. For whole carcasses, packs and general use."],
            ["Plate (contact)", "Food packs pressed between refrigerated plates. Fast for flat packs such as fish fillets or burgers."],
            ["IQF: fluidised bed", "Small pieces (peas, diced vegetables, shrimps) are lifted by an upward air stream, frozen separately and stay free-flowing."],
            ["Cryogenic", "Contact with liquid nitrogen (about -196 °C) or carbon dioxide. Extremely fast, high quality, but costly."],
            ["Immersion or spray", "Packs or whole fish in cold brine; fast but salt uptake must be controlled."],
        ]),
        EX("Worked example 3: ice expansion",
           intro="Water expands by about 9% when it freezes (ice density 0.917 g per mL). A sealed container holds 900 g of water in juice that freezes completely. By how much does the volume of that water increase?",
           steps=[
               S("Volume as ice", math=r"\frac{900}{0.917} = 981.5 \text{ mL}"),
               S("Increase", math=r"981.5 - 900 = 81.5 \text{ mL} \approx 9\%"),
               S("Practical meaning", text="Packages for frozen liquids need headspace, and glass bottles filled to the top may crack."),
           ]),
        H("Quality problems in frozen storage"),
        KEY("Causes and prevention", "Know each in a sentence.", cards=[
            ["Freezer burn", "Ice at the surface of unwrapped food sublimes (changes straight to vapour), leaving dry, pale, tough patches. Prevent by tight, moisture-proof packaging."],
            ["Recrystallisation", "Temperature fluctuations melt small crystals and refreeze them on larger ones; texture is damaged. Keep storage temperature steady."],
            ["Rancidity in fatty foods", "Fat oxidation continues slowly in frozen storage (for example oily fish). Use oxygen-proof packaging and low temperature."],
            ["Thawing losses", "Slow thawing at warm temperature allows bacterial growth on the thawed surface and drip loss. Thaw in a refrigerator or cook from frozen; never refreeze thawed raw food."],
        ]),
        T("**The cold chain** is the unbroken series of low-temperature steps from the producer to the consumer: precooling, cold store, refrigerated "
          "transport, retail display and home storage. A single break (a truck with a failed cooler, a power cut in a market) allows growth and recrystallisation that "
          "cannot be reversed. In places where mains electricity is unreliable, backup generators, insulated boxes with ice, and temperature records "
          "are the practical tools for protecting a cold chain."),
        MISTAKE("Saying freezing kills micro-organisms", "Freezing stops the growth of most microbes, and some die, but many survive and grow again when the food thaws. Freezing is not a sterilising treatment."),
        MISTAKE("Explaining drip loss by 'the water leaks out'", "The key point is cell damage: slow freezing forms large extracellular crystals that rupture or distort cell walls, so the thawed tissue cannot reabsorb its water."),
        QUIZ("Which freezing method gives free-flowing, individually frozen peas?",
             ["Plate freezing", "Slow freezing in a block", "Fluidised-bed IQF", "Immersion in warm brine"], 2,
             "In a fluidised-bed freezer, cold air lifts the small pieces so that each freezes separately without clumping.",
             hint="Which method keeps pieces apart as they freeze?",
             feedback=["Plate freezing presses packs between plates and freezes a solid block.", "A block of peas would stick together.", "", "Warm brine does not freeze food."]),
        QUIZ("Why does the temperature of meat stay nearly constant for a long time near -1.5 °C while it freezes?",
             ["The freezer is switched off", "Latent heat of fusion is being removed as water turns to ice", "Meat is a good insulator and cannot cool", "Fat melts at that temperature"], 1,
             "Removing heat from water at its freezing point turns it into ice without lowering the temperature, until most of the water is frozen.",
             hint="Where is the heat going if the temperature does not fall?",
             feedback=["The refrigeration is working; the plateau is physical.", "", "Insulation slows cooling but does not create a plateau.", "Fat does not melt at -1.5 °C; the effect is the freezing of water."]),
        H("Practice"),
        PQ("Distinguish between chilling and freezing, giving one risk of each.", "Chilling keeps food at about -1 to 8 °C: reactions and microbial growth are slowed but psychrotrophs such as Listeria and Pseudomonas still grow, so shelf life is limited (and tropical fruit may suffer chilling injury). Freezing converts most water to ice at -18 °C or below, stopping microbial growth; the risks are ice-crystal damage and drip loss, freezer burn and recrystallisation, and survival of microbes that grow after thawing."),
        PQ("Explain why quick freezing gives a better quality product than slow freezing.", "Quick freezing forms many small ice crystals throughout the tissue, including inside the cells, so cell walls are little damaged and cells keep their structure. Slow freezing forms large crystals outside cells that draw water out and tear walls. On thawing, slowly frozen food loses much water as drip and is soft and mushy, with loss of soluble nutrients."),
        PQ("Calculate the heat needed to freeze 5 kg of fish: water content 75%, 80% of the water frozen at storage temperature, L = 334 kJ per kg. Give only the latent heat part.", "Mass of ice = 5 x 0.75 x 0.80 = 3.0 kg. Latent heat = 3.0 x 334 = 1002 kJ."),
        PQ("Describe two causes of quality loss in frozen storage and how to prevent each.", "Freezer burn: ice sublimes from unwrapped surfaces, leaving dry pale tough patches; prevent with tight moisture-proof packaging. Recrystallisation: temperature fluctuations let small crystals melt and re-form as larger ones, damaging texture; prevent with steady -18 °C or lower and avoiding repeated door openings or thaw-refreeze cycles."),
        TIP("Exam link: low-temperature preservation appears in Paper 1 (definitions, freezing methods, chilling injury) and in Paper 2 essays on preservation. Link ice-crystal size to drip loss, and always say 'slows' not 'stops' for chilling."),
        SUM("Chilling (about -1 to 8 °C) slows spoilage; freezing (-18 °C or lower) makes water unavailable as ice. Neither sterilises.",
            "During freezing, a plateau appears near the initial freezing point while latent heat (about 334 kJ per kg of ice) is removed: this is most of the energy.",
            "Quick freezing and IQF give small crystals and little drip loss; slow freezing gives large crystals and cell damage.",
            "Freezer burn, recrystallisation, rancidity and thawing losses are prevented by good packaging, steady low temperature and careful thawing.",
            "An unbroken cold chain from producer to consumer is essential; tropical fruit may need cool, not cold, storage because of chilling injury."),
    ],
))

# ------------------------------------------------------------------ 4. Dehydration
LESSONS.append(lesson(
    module=M1,
    topic="Dehydration",
    title="Dehydration: drying curves, sun, drum, spray and freeze-drying",
    slug="fsu1-dehydration",
    minutes=24,
    summary="Drying preserves food by lowering water activity. Learn the drying curve, the main methods (sun, hot-air, drum, spray, freeze-drying), the quality changes, and the mass-balance calculations for moisture removal.",
    objectives=[
        "Explain how dehydration preserves food using water activity and calculate moisture content on wet and dry bases",
        "Describe the three stages of a drying curve and the factors that affect the drying rate",
        "Compare sun, hot-air, drum, spray and freeze-drying: principle, products, advantages and limits",
        "Carry out mass balances for drying and explain the quality changes that drying causes",
    ],
    key_concepts=["Water activity", "Moisture content (wet and dry basis)", "Constant-rate and falling-rate periods", "Case hardening", "Sun and solar drying", "Drum drying", "Spray drying", "Freeze-drying (sublimation)", "Rehydration"],
    blocks=[
        H("Introduction"),
        T("Dried fish, maize, groundnuts, cassava chips, powdered milk and instant coffee all keep for months because the water has been "
          "removed. Drying is one of the oldest and still one of the most important preservation methods. It also makes food lighter and "
          "smaller, which saves transport and storage costs. But drying done badly, for example slow drying in damp weather, "
          "lets moulds grow and can produce aflatoxins. This lesson explains the science and the main industrial methods."),
        D("**Dehydration (drying)** is the removal of most of the water from a food by evaporation (or sublimation in freeze-drying) so that the "
          "water activity falls low enough to stop microbial growth and slow chemical and enzyme reactions.", title="Dehydration"),
        KEY("Water activity limits", "Approximate lowest water activity (aw) for growth. Revise the full idea from Lower Sixth.", cards=[
            ["Most bacteria", "About 0.91 (Staphylococcus aureus can grow down to about 0.86)."],
            ["Most yeasts", "About 0.88."],
            ["Most moulds", "About 0.80."],
            ["Xerophilic moulds and osmophilic yeasts", "About 0.60 to 0.65. Below about 0.6 no microbial growth, but enzymes, browning and fat oxidation can continue."],
        ]),
        H("Moisture content: two ways to express it"),
        F(r"\text{Wet basis: } M_{wb} = \frac{\text{mass of water}}{\text{total mass}}, \qquad \text{Dry basis: } X = \frac{\text{mass of water}}{\text{mass of dry solids}}", title="Moisture content"),
        T("The wet basis is used on labels and in trade (maize at 13% moisture). The dry basis is used in drying calculations because the mass of "
          "dry solids stays constant, while the total mass changes as water leaves."),
        EX("Worked example 1: converting wet and dry basis",
           intro="Fresh cassava is 80% moisture on the wet basis. Dried chips are 10% moisture (wet basis). Convert both to the dry basis.",
           steps=[
               S("Fresh cassava: take 100 g", text="80 g water and 20 g dry solids."),
               S("Dry basis", math=r"X = \frac{80}{20} = 4.0 \text{ kg water per kg dry solids}"),
               S("Dried chips: take 100 g", text="10 g water and 90 g solids."),
               S("Dry basis", math=r"X = \frac{10}{90} = 0.111 \text{ kg water per kg dry solids}"),
           ]),
        H("The drying curve"),
        T("When a wet food is placed in warm, moving air, its drying rate changes with time in three stages."),
        IMG("alfsu1-drying-curve.svg", alt="Drying rate against moisture content: a short warm-up rise, a level constant-rate period at high moisture, then a falling-rate period as moisture decreases towards the equilibrium value",
            caption="Figure 1. A drying rate curve. Moisture content falls from right to left."),
        KEY("Stages of drying", "Learn what controls each stage.", cards=[
            ["Warm-up period", "The food heats up to the wet-bulb temperature; drying speeds up."],
            ["Constant-rate period", "Free water at the surface evaporates like water from an open dish. The rate depends on the air (temperature, humidity, speed), not on the food."],
            ["Falling-rate period", "Below the critical moisture content the surface is no longer wet. Water must move from the inside by diffusion, so the rate depends on the food (thickness, structure) and slows. Most of the drying time of foods is spent here."],
        ]),
        T("**Factors that speed drying:** higher air temperature, lower air humidity, faster air flow, smaller pieces and larger surface area, "
          "and pre-treatments such as blanching (breaks cell structure) or slicing. **Case hardening** happens if the surface dries so "
          "fast that it forms a hard, dry skin which traps moisture inside; it is avoided by lowering the air temperature early in the process."),
        EX("Worked example 2: time in the constant-rate period",
           intro="A batch has 50 kg of dry solids. Its moisture falls from X = 3.0 to the critical value X = 1.0 kg water per kg solids at a constant rate of 20 kg of water per hour. How long does the constant-rate period last? (Teaching data.)",
           steps=[
               S("Water removed", math=r"50 \times (3.0 - 1.0) = 100 \text{ kg}"),
               S("Time", math=r"t = \frac{100}{20} = 5 \text{ h}"),
               S("Note", text="The falling-rate period that follows is slower, so the total time is longer than the constant-rate period alone."),
           ]),
        H("Drying methods"),
        KEY("Sun and solar drying", "Cheapest, but weather-dependent.", cards=[
            ["Open sun drying", "Food spread on mats or concrete. Very cheap and widely used for grains, fish, cassava and cocoa. Risks: rain, dust, insects, birds, slow drying, contamination and mould."],
            ["Solar dryers", "A cabinet or tunnel with a transparent cover and black absorber heats the air and shields food from rain and insects. Drier, cleaner product and a shorter time, with low running cost."],
        ]),
        KEY("Industrial drying", "Match the method to the form of the food.", cards=[
            ["Hot-air (cabinet, tunnel, belt, fluidised bed)", "Hot air passes over or through solid pieces (vegetables, fruit slices, grains, cassava chips)."],
            ["Drum drying", "A thin film of puree, paste or slurry is spread on a heated, slowly rotating steel drum and scraped off as flakes after about one rotation. Used for instant potato, infant cereals and banana flakes. Short contact, but the high surface temperature can cause a cooked flavour."],
            ["Spray drying", "A liquid is sprayed as fine droplets into a chamber of hot air (inlet about 150 to 250 °C). Water evaporates in seconds and a powder is collected. Used for milk, instant coffee, egg and cocoa-based powders. Droplets stay at about the wet-bulb temperature, so heat damage is small despite the hot air."],
            ["Freeze-drying", "The food is frozen, placed under a vacuum, and ice changes straight to vapour (sublimation) with gentle heat; the last water is then removed by desorption. Shape, flavour, colour and nutrients are very well kept and it rehydrates quickly, but it is slow and costly. Used for premium coffee, herbs and some ready meals."],
        ]),
        EX("Worked example 3: mass balance of drying cassava chips",
           intro="100 kg of fresh cassava chips at 65% moisture (wet basis) are dried to 12% moisture. Find the mass of dried product and the water removed. (Teaching data.)",
           steps=[
               S("Dry solids are unchanged", math=r"100 \times (1 - 0.65) = 35 \text{ kg}"),
               S("Mass of dried product", math=r"\frac{35}{1 - 0.12} = 39.77 \text{ kg}"),
               S("Water removed", math=r"100 - 39.77 = 60.23 \text{ kg}"),
               S("Check", math=r"39.77 \times 0.12 = 4.77 \text{ kg of water left; } 35 + 4.77 = 39.77")
           ]),
        EX("Worked example 4: a spray dryer",
           intro="A spray dryer takes 1 000 kg per hour of milk concentrate containing 20% solids and produces a powder with 4% moisture (96% solids). Find the powder produced and the water evaporated per hour. (Teaching data.)",
           steps=[
               S("Solids in feed", math=r"1000 \times 0.20 = 200 \text{ kg/h}"),
               S("Powder", math=r"\frac{200}{0.96} = 208.3 \text{ kg/h}"),
               S("Water evaporated", math=r"1000 - 208.3 = 791.7 \text{ kg/h}"),
           ]),
        H("What drying does to quality"),
        T("**Physical:** shrinkage, case hardening and a loss of the ability to take up water again (rehydration), especially after fast or hot drying. "
          "**Chemical:** loss of volatile flavour and aroma, browning (Maillard and enzymatic), loss of vitamin C and carotenoids, and oxidation "
          "of fat in dried fatty foods. **Biological:** most microbes are not killed, only stopped, and they grow when the food is rewetted. "
          "Good drying needs correct pre-treatment (blanching, and sulphite for some fruits), moisture-proof packaging, and cool, dry storage."),
        MISTAKE("Thinking dried food is sterile", "Drying lowers aw so that microbes cannot grow, but spores and many cells survive. A dried food that takes up water again (leaking packaging, damp storage) can spoil quickly."),
        MISTAKE("Using the wrong basis in mass balances", "Water content on a wet basis changes with the total mass. Keep the dry solids constant and recalculate the total mass from them, as in worked example 3."),
        QUIZ("Which drying method uses a vacuum and sublimation of ice?",
             ["Spray drying", "Drum drying", "Freeze-drying", "Tunnel drying"], 2,
             "In freeze-drying frozen food is placed under vacuum and ice sublimes to vapour; this preserves shape and flavour.",
             hint="Which method needs the food to be frozen first?",
             feedback=["Spray drying evaporates droplets in hot air.", "Drum drying evaporates a film on a heated drum.", "", "Tunnel drying uses hot air passing over trays."]),
        QUIZ("During which period does the drying rate depend mainly on how fast water moves inside the food?",
             ["Warm-up period", "Constant-rate period", "Falling-rate period", "All three equally"], 2,
             "After the critical moisture content the surface is no longer saturated and internal diffusion limits the rate.",
             hint="At which stage is the surface no longer wet?",
             feedback=["In warm-up the food is being heated to the wet-bulb temperature.", "In the constant-rate period free surface water evaporates, governed by the drying air.", "", "The factors differ between the periods."]),
        H("Practice"),
        PQ("Explain how dehydration preserves food.", "Removing water lowers the water activity below the minimum for microbial growth (about 0.6 to 0.9 depending on the organism). With little available water microbes cannot grow, and enzyme and chemical reactions are slowed. The smaller mass and volume also reduce storage and transport costs. It is not sterilisation, so packaging must keep out moisture."),
        PQ("Distinguish the constant-rate period from the falling-rate period of drying.", "In the constant-rate period free water on the surface evaporates and the rate depends on the drying air (temperature, humidity, velocity). In the falling-rate period, below the critical moisture content, water must diffuse from inside to the surface, so the rate depends on the food structure and thickness and slows steadily."),
        PQ("Compare spray drying and freeze-drying of coffee.", "Spray drying atomises a coffee extract into hot air and gives a fine powder quickly and cheaply, with some loss of aroma. Freeze-drying freezes the extract, then removes ice by sublimation under vacuum, giving granules that keep aroma and flavour and dissolve easily, but the process is slow and costly because of the vacuum and refrigeration."),
        PQ("250 kg of fish at 70% moisture is dried to 13% moisture. Calculate the mass of dried fish.", "Dry solids = 250 x 0.30 = 75 kg. Dried mass = 75 / (1 - 0.13) = 75 / 0.87 = 86.2 kg. (Water removed = 163.8 kg.)"),
        TIP("Exam link: dehydration appears in Paper 1 (definitions and methods), in Paper 2 essays on preservation (compare methods, give advantages and limits), and in Paper 3 when moisture is determined. In calculations always show the dry-solids step."),
        SUM("Dehydration lowers water activity so that microbes cannot grow; it is not sterilisation.",
            "The drying curve has a warm-up stage, a constant-rate period (surface water, controlled by the air) and a falling-rate period (internal diffusion, controlled by the food).",
            "Sun drying is cheap but risky; solar dryers protect food; drum, spray and freeze-drying suit pastes, liquids and premium foods respectively.",
            "Mass balances keep the dry solids constant: dried mass = solids / (1 - final moisture).",
            "Drying causes shrinkage, loss of aroma, browning and vitamin loss; freeze-drying keeps the most quality at the highest cost."),
    ],
))

# ------------------------------------------------------------------ 5. Irradiation, MAP and additives
LESSONS.append(lesson(
    module=M1,
    topic="Irradiation, modified atmosphere packaging and additives",
    title="Irradiation, modified atmosphere packaging and food additives",
    slug="fsu1-irradiation-map-additives",
    minutes=25,
    summary="Three more preservation tools: ionising radiation (a cold process measured in grays), modified atmosphere packaging (CO2, N2, O2 mixtures) and chemical additives (preservatives, antioxidants and others, controlled by the ADI).",
    objectives=[
        "Explain how irradiation preserves food, the dose categories, and its advantages, limits and labelling",
        "Calculate the dose needed for a required microbial reduction from a D10 value",
        "Explain how modified atmosphere packaging works and the role of N2, CO2 and O2",
        "Classify food additives, name examples and functions, and explain the ADI and why preservative action depends on pH",
    ],
    key_concepts=["Ionising radiation, gray (Gy)", "Dose categories", "D10 value", "Radura", "Modified atmosphere packaging", "Controlled atmosphere storage", "Food additive classes", "E numbers", "ADI", "Undissociated acid"],
    blocks=[
        H("Introduction"),
        T("Potatoes that do not sprout for months, fresh meat in a sealed tray that stays red, and a soft drink that does not go mouldy: three different "
          "technologies at work. This lesson covers radiation, packaging gases and chemicals. Each works best as one of several barriers "
          "(hurdles) and none is a substitute for clean raw materials and good hygiene."),
        H("Food irradiation"),
        D("**Food irradiation** exposes food to a controlled dose of **ionising radiation**: gamma rays from the radioactive isotopes cobalt-60 "
          "(or caesium-137), or machine-made electron beams or X-rays. The radiation breaks chemical bonds, including the DNA of microbes, insects "
          "and sprouting tissue, without raising the temperature much. The food does not become radioactive at the permitted energies.",
          title="Irradiation"),
        D("The **absorbed dose** is measured in grays. **1 gray (Gy) = 1 joule of energy absorbed per kilogram of food.** Doses in food are given in "
          "kilograys (1 kGy = 1000 Gy).", title="Dose: the gray"),
        KEY("Dose categories", "Approximate ranges from FAO, IAEA and WHO teaching; check your textbook for exact figures.", cards=[
            ["Low dose (below about 1 kGy)", "Sprout inhibition in potatoes, yams and onions (about 0.05 to 0.15 kGy), insect disinfestation of grain and dried fruit, delay of ripening."],
            ["Medium dose (about 1 to 10 kGy)", "Reduces spoilage organisms and pathogens such as Salmonella in meat, poultry, fish and spices; extends the shelf life of chilled food."],
            ["High dose (above about 10 kGy)", "Sterilisation of food for special users (for example immunocompromised patients) and some spices. Not for general use; the Codex general standard sets a general limit of about 10 kGy average dose, so check the current text."],
        ]),
        T("Some textbooks use special words for these aims: **radurisation** (reducing spoilage organisms), **radicidation** (reducing pathogens) and "
          "**radappertisation** (sterilisation). A food treated by irradiation must be labelled in most countries, often with the **Radura** symbol (a "
          "stylised plant in a circle); labelling rules vary, so check the rules where you live."),
        EX("Worked example 1: the dose for a required reduction",
           intro="*Salmonella* in a poultry product has D10 = 0.6 kGy (the dose that destroys 90%). Find the dose to give a 5-log reduction, and the survivors from an initial $10^{6}$ cells per gram after that dose. (Teaching D10; real values depend on the food and conditions.)",
           steps=[
               S("Dose = number of log cycles times D10", math=r"5 \times 0.6 = 3.0 \text{ kGy}"),
               S("Survivors", math=r"10^6 \times 10^{-5} = 10^1 = 10 \text{ cells per gram}"),
               S("Check the energy", text="3 kGy is 3 000 J per kg. If all that energy became heat in water (4 180 J per kg per °C) the rise would be under 1 °C: irradiation is a cold process."),
           ]),
        KEY("Advantages and limits", "A balanced answer needs both.", cards=[
            ["Advantages", "Cold process; treats packaged food; no chemical residue; penetrates thick packs; destroys insects without fumigants; can extend shelf life and reduce pathogens such as Salmonella."],
            ["Limits", "Does not destroy toxins already formed, most viruses or prions; high doses can cause off-flavours (especially in fatty food) and some vitamin loss; cannot rescue spoiled food; needs costly, licensed plants and trained staff; some consumers distrust it."],
        ]),
        H("Modified atmosphere packaging (MAP)"),
        D("**Modified atmosphere packaging** replaces the air in a sealed pack with a gas mixture chosen to slow spoilage. The gas composition is "
          "set at packing and then changes slowly through respiration, absorption and leakage. **Controlled atmosphere (CA) storage** is "
          "the same idea for large stores or containers, where the gases are monitored and held within limits.", title="MAP"),
        KEY("The three gases", "Each has a job.", cards=[
            ["Nitrogen (N2)", "An inert filler. It displaces oxygen, prevents pack collapse as CO2 dissolves, and slows fat oxidation."],
            ["Carbon dioxide (CO2)", "Slows the growth of moulds and aerobic bacteria (bacteriostatic) in meat, fish, cheese and bakery foods. It dissolves in water and fat, so pack volume can shrink. Too high a level may harm some produce."],
            ["Oxygen (O2)", "Kept very low for most foods to limit aerobic spoilage and oxidation. High oxygen (about 70 to 80%) is used with CO2 in packs of fresh red meat to keep the bright red oxymyoglobin colour, and kept low in packs of fresh produce so that respiration slows but does not become anaerobic."],
        ]),
        T("**Packaging requirements.** The pack must be a good barrier to gases and moisture (laminated or multilayer films, or rigid trays with lidding film) "
          "and must be heat-sealed without leaks. A gas-to-product volume ratio of at least about 2:1 to 3:1 is commonly used so that enough CO2 is present. "
          "MAP is combined with **chilling**: it slows spoilage but does not stop it. In packs of chilled fish, low oxygen could allow "
          "*Clostridium botulinum* type E to grow without obvious spoilage, so strict temperature control is essential."),
        EX("Worked example 2: gas volumes in a pack",
           intro="A tray holds 400 mL of cooked meat. The packer uses a gas-to-product ratio of 2:1 and a mixture of 30% CO2 and 70% N2. How much CO2 and N2 are in each tray?",
           steps=[
               S("Gas volume", math=r"2 \times 400 = 800 \text{ mL}"),
               S("CO2", math=r"0.30 \times 800 = 240 \text{ mL}"),
               S("N2", math=r"0.70 \times 800 = 560 \text{ mL}"),
           ]),
        T("**Related technologies.** Vacuum packaging removes the air and is simple, but gives no CO2 and can squash soft foods. **Active packaging** "
          "includes oxygen scavengers, ethylene absorbers and moisture absorbers; **intelligent packaging** uses time-temperature indicators and "
          "freshness indicators to show the condition of the food."),
        H("Food additives"),
        D("A **food additive** is a substance that is not normally eaten as a food or used as a typical ingredient, and that is added "
          "intentionally for a technological purpose in manufacture, processing, packaging or storage. Contaminants and nutrients added to improve "
          "nutritive value are normally treated separately.", title="Food additive"),
        KEY("Main classes with examples", "International numbers (INS, written as E numbers in Europe) identify them.", cards=[
            ["Preservatives", "Benzoic acid and benzoates (E210 to E213) in soft drinks and sauces; sorbic acid and sorbates (E200 to E203) in cheese and baked goods; sulphur dioxide and sulphites (E220 and others) in dried fruit and wine; nitrites (E249, E250) in cured meat."],
            ["Antioxidants", "Ascorbic acid (E300) and tocopherols (E306) in oils; BHA and BHT in fats and snacks; citric acid (E330) as a metal-binding synergist."],
            ["Emulsifiers and stabilisers", "Lecithin (E322) and mono- and diglycerides in margarine and chocolate; pectin, xanthan gum and carboxymethylcellulose in jams, sauces and drinks."],
            ["Colours and sweeteners", "Beta-carotene, curcumin and anthocyanins (natural) and synthetic dyes such as tartrazine (E102); aspartame, saccharin and acesulfame K."],
            ["Flavour enhancers, acidulants, others", "Monosodium glutamate (E621); citric, lactic and malic acids; sodium bicarbonate (raising agent); anti-caking agents in powders."],
        ]),
        T("**How preservatives work: the pH effect.** Weak-acid preservatives such as benzoic, sorbic and propionic acids act mainly in the "
          "**undissociated** (uncharged) form, which can enter the microbial cell. The proportion of the acid that is undissociated depends on the pH of the food "
          "and on the acid's pKa (the pH at which 50% is undissociated). They are therefore useful in acid foods and weak in neutral ones."),
        F(r"\text{fraction undissociated} = \frac{1}{1 + 10^{\,pH - pK_a}}", title="Undissociated acid"),
        EX("Worked example 3: benzoic acid at different pH",
           intro="Benzoic acid has a pKa of 4.2. What percentage is undissociated in a soft drink at pH 3.2 and in a sauce at pH 5.2?",
           steps=[
               S("pH 3.2", math=r"\frac{1}{1 + 10^{3.2 - 4.2}} = \frac{1}{1 + 0.1} = 0.909 \Rightarrow 90.9\%"),
               S("pH 5.2", math=r"\frac{1}{1 + 10^{5.2 - 4.2}} = \frac{1}{1 + 10} = 0.0909 \Rightarrow 9.1\%"),
               S("Meaning", text="At pH 5.2 only a tenth as much of the active form is present as at pH 3.2, so benzoate protects the acid drink well and the weaker acid sauce poorly."),
           ]),
        H("Safety of additives: the ADI"),
        D("The **acceptable daily intake (ADI)** is the amount of an additive, in mg per kg of body weight per day, that can be eaten every day for a "
          "lifetime without appreciable risk. It is normally set by dividing the highest dose with no observed adverse effect in animal studies (the NOAEL) by a "
          "safety factor of 100. International expert committees (the FAO/WHO Joint Expert Committee on Food Additives, JECFA) evaluate additives, and Codex "
          "publishes the General Standard for Food Additives with maximum levels.", title="ADI", formula=r"\text{ADI} = \frac{\text{NOAEL}}{100}"),
        EX("Worked example 4: ADI and a child's drinks",
           intro="An additive has a NOAEL of 500 mg per kg body weight per day (invented for practice). A soft drink contains 150 mg per litre. How many litres per day would a 20 kg child have to drink to reach the ADI?",
           steps=[
               S("ADI", math=r"\frac{500}{100} = 5 \text{ mg/kg/day}"),
               S("ADI for the child", math=r"5 \times 20 = 100 \text{ mg/day}"),
               S("Volume to reach it", math=r"\frac{100}{150} = 0.67 \text{ L}"),
               S("Meaning", text="A small child could reach the ADI with less than a litre of this drink, so regulators set limits that allow for children and for several sources of the same additive."),
           ]),
        MISTAKE("Saying irradiated food is radioactive", "At the energies permitted, irradiation does not make food radioactive. The food is like food that has been X-rayed at the airport: it carries no radiation afterwards."),
        MISTAKE("Saying MAP keeps food fresh without refrigeration", "MAP is used together with chilling. It slows aerobic spoilage but can allow anaerobic pathogens such as C. botulinum to grow in fish and cooked foods if temperature control fails."),
        QUIZ("Which gas in a MAP tray of fresh red meat is used to keep the meat red?",
             ["High oxygen", "Pure nitrogen", "Pure carbon dioxide", "A vacuum"], 0,
             "High oxygen (together with CO2) keeps myoglobin as bright red oxymyoglobin. Nitrogen and a vacuum give a purple-red colour.",
             hint="Which gas turns myoglobin into oxymyoglobin?",
             feedback=["", "Nitrogen only gives low oxygen, so myoglobin turns purple and the meat looks dull.", "Carbon dioxide slows bacteria but without oxygen the pigment does not form oxymyoglobin, so the meat looks purple or brown.", "Vacuum removes oxygen and gives a purple colour."]),
        QUIZ("Sodium benzoate protects a pH 3.5 drink better than a pH 6 sauce because",
             ["benzoate is destroyed at high pH", "more of the acid is in the undissociated form at low pH", "the sauce contains more water", "benzoate only works above pH 5"], 1,
             "The undissociated molecule enters the microbial cell; low pH keeps most of the acid undissociated.",
             hint="Which form of the acid is the active one?",
             feedback=["The molecule is not destroyed; its form changes with pH.", "", "Water content does not explain the pH effect.", "It works better, not only, at lower pH."]),
        H("Practice"),
        PQ("State two advantages and two limitations of food irradiation.", "Advantages: a cold process that does not heat the food; can treat food in its final package; destroys insects and reduces Salmonella and spoilage organisms; inhibits sprouting without chemicals. Limitations: does not remove toxins already formed or inactivate most viruses; high doses cause off-flavours; cannot improve spoiled food; the plant is costly and licensed; some consumers are wary."),
        PQ("A spice has D10 = 1.2 kGy for a mould spore. What dose gives a 4-log reduction?", "Dose = 4 x 1.2 = 4.8 kGy."),
        PQ("Explain the roles of nitrogen and carbon dioxide in modified atmosphere packaging of bread and cheese.", "Carbon dioxide inhibits moulds and aerobic bacteria that spoil the product. Nitrogen is an inert filler that replaces oxygen, slows oxidation of fat and prevents the pack from collapsing as CO2 dissolves in the food. A barrier film and a gas to product ratio near 2:1 are used."),
        PQ("An additive has an ADI of 2 mg per kg body weight per day. Calculate the maximum daily intake for a 60 kg adult, and explain what ADI means.", "60 x 2 = 120 mg per day. The ADI is the amount that can be eaten daily for a lifetime without appreciable health risk, normally set as the NOAEL divided by a safety factor of 100."),
        TIP("Exam link: irradiation, MAP and additives appear in Paper 1 (definitions, examples, classes of additive) and in Paper 2 essays on food preservation or on additives and food safety. Give examples with functions, and avoid emotional language: examiners want the balance of benefit and risk."),
        SUM("Irradiation is a cold process measured in grays (1 Gy = 1 J per kg); dose categories are low (sprouting, insects), medium (pathogens, spoilage) and high (sterilisation).",
            "Required dose = number of log cycles times D10; irradiated food is not radioactive and must usually be labelled.",
            "MAP replaces air with N2, CO2 and O2 mixtures, with barrier packaging and chilling; CA storage is the controlled bulk version.",
            "Additive classes include preservatives, antioxidants, emulsifiers, stabilisers, colours, sweeteners, flavour enhancers and acidulants.",
            "Weak-acid preservatives work through the undissociated form, so they need low pH; the ADI (NOAEL divided by 100) controls safety."),
    ],
))

# ------------------------------------------------------------------ 6. Post-harvest physiology
LESSONS.append(lesson(
    module=M2,
    topic="Post-harvest physiology",
    title="Post-harvest physiology: respiration, ethylene and ripening",
    slug="fsu1-post-harvest-physiology",
    minutes=24,
    summary="Harvested fruit and vegetables are still alive. Learn respiration, the respiratory quotient, climacteric and non-climacteric behaviour, the role of ethylene and how temperature, humidity and atmosphere control storage life.",
    objectives=[
        "Explain why harvested produce is still alive and write the equation for aerobic respiration",
        "Calculate the respiratory quotient and the heat and sugar used by respiring produce, and apply Q10",
        "Distinguish climacteric from non-climacteric fruit and describe the changes of ripening",
        "Explain how temperature, humidity, atmosphere and ethylene control are used to extend storage life",
    ],
    key_concepts=["Post-harvest respiration", "Respiratory quotient (RQ)", "Q10", "Climacteric and non-climacteric", "Ethylene", "Ripening changes", "Transpiration", "Maturity indices", "Controlled and modified atmosphere"],
    blocks=[
        H("Introduction"),
        T("A bunch of green plantain cut in a farm near Mbanga can be sold green in Douala two days later, and a mango picked mature but "
          "unripe is ripe by the time it reaches the market. In both cases the fruit is still **alive**. After harvest it has no roots or leaves to supply it, "
          "so it lives on its own stores of sugar and starch, and these stores cannot be replaced. **Post-harvest physiology** is the study "
          "of these changes. The aim of post-harvest technology is to slow them just enough to keep the produce good until it is eaten."),
        H("Respiration after harvest"),
        D("**Respiration** is the controlled oxidation of stored carbohydrate (and organic acids and fats) to release energy, carbon dioxide and water. "
          "It continues after harvest and is the main process that uses up the produce's food reserves and gives out heat.", title="Respiration"),
        F(r"\mathrm{C_6H_{12}O_6} + 6\,\mathrm{O_2} \;\longrightarrow\; 6\,\mathrm{CO_2} + 6\,\mathrm{H_2O} + \text{energy (about 2 803 kJ per mole of glucose as heat)}", title="Aerobic respiration"),
        D("The **respiratory quotient (RQ)** is the volume (or moles) of CO2 produced divided by the volume (or moles) of O2 used. An RQ of about 1.0 shows "
          "that carbohydrate is the substrate; below 1.0 suggests fat (about 0.7); above 1.0 suggests organic acids or, if far above 1, anaerobic "
          "(fermentative) respiration.", title="Respiratory quotient", formula=r"RQ = \frac{\text{CO}_2 \text{ produced}}{\text{O}_2 \text{ used}}"),
        EX("Worked example 1: RQ of glucose and of malic acid",
           intro="Calculate the RQ when (a) glucose and (b) malic acid, C4H6O5, are fully oxidised. Equation for malic acid: C4H6O5 + 3 O2 gives 4 CO2 + 3 H2O.",
           steps=[
               S("(a) Glucose: 6 CO2 for 6 O2", math=r"RQ = \frac{6}{6} = 1.0"),
               S("(b) Malic acid: 4 CO2 for 3 O2", math=r"RQ = \frac{4}{3} = 1.33"),
               S("Meaning", text="Fruit that is using acids as well as sugars, such as ripening fruit, shows an RQ a little above 1. A much higher value would show fermentation, as when oxygen is too low in the storage atmosphere."),
           ]),
        T("**The respiration rate** is measured in mg of CO2 produced per kg of produce per hour. It is a good guide to how perishable the produce is: "
          "produce with a high rate (leafy vegetables, peas, sweet corn, ripe fruit) loses quality quickly; produce with a low rate (citrus, "
          "dry onions, potatoes, yams after curing) keeps much longer."),
        EX("Worked example 2: heat and sugar used",
           intro="Fruit respires at 20 mg of CO2 per kg per hour. Use 1 mg of CO2 = 10.6 J of heat (from 2 803 kJ per mole of glucose and 6 mol CO2 = 264 g). Find the heat per kg per hour, and the mass of glucose used per kg per day.",
           steps=[
               S("Heat per kg per hour", math=r"20 \times 10.6 = 212 \text{ J} = 0.059 \text{ W per kg}"),
               S("CO2 per kg per day", math=r"20 \times 24 = 480 \text{ mg}"),
               S("Glucose used (180.2 g gives 264 g CO2)", math=r"480 \times \frac{180.2}{264.1} = 327 \text{ mg} = 0.33 \text{ g per kg per day}"),
               S("Meaning", text="The heat load matters in stores: 5 tonnes of produce at 100 mg CO2 per kg per hour give off about 1.5 kW, which refrigeration must remove."),
           ]),
        H("Temperature and the Q10 rule"),
        D("**Q10** is the factor by which a reaction rate increases for a 10 °C rise in temperature. For respiration of most produce Q10 is about 2 to 3. "
          "Cooling is therefore the single most effective tool for extending storage life.", title="Q10", formula=r"Q_{10} = \frac{\text{rate at } (T+10)\,{}^\circ\text{C}}{\text{rate at } T\,{}^\circ\text{C}}"),
        EX("Worked example 3: using Q10",
           intro="A fruit respires at 12 mg CO2 per kg per hour at 10 °C and at 30 mg at 20 °C. (a) Find Q10. (b) Predict the rate at 30 °C. (c) The fruit keeps 4 days at 30 °C; estimate its life at 20 °C, assuming life is inversely proportional to rate. (Teaching data.)",
           steps=[
               S("(a) Q10", math=r"Q_{10} = \frac{30}{12} = 2.5"),
               S("(b) Rate at 30 °C", math=r"30 \times 2.5 = 75 \text{ mg CO}_2\,\text{kg}^{-1}\text{h}^{-1}"),
               S("(c) Life at 20 °C", math=r"4 \times 2.5 = 10 \text{ days}"),
           ]),
        H("Climacteric and non-climacteric fruit"),
        IMG("alfsu1-climacteric.svg", alt="Graph of respiration rate against time: a climacteric fruit shows a fall, then a rise to a peak during ripening and then a decline; a non-climacteric fruit shows a steady decline with no peak",
            caption="Figure 1. Two respiration patterns after maturity."),
        D("**Climacteric fruit** show a marked rise in respiration (the climacteric) and a burst of ethylene production at the start of ripening, and can "
          "ripen after harvest. **Non-climacteric fruit** show no such rise and ripen only on the plant; they do not improve in eating quality after harvest.", title="Climacteric and non-climacteric"),
        KEY("Examples", "Learn four of each.", cards=[
            ["Climacteric", "Banana, plantain, mango, papaya, avocado, tomato, apple, pear, guava, passion fruit."],
            ["Non-climacteric", "Orange and other citrus, pineapple, grape, strawberry, watermelon, cucumber, pepper."],
            ["Practical meaning", "Climacteric fruit can be harvested mature but unripe, transported firm, and ripened near the market. Non-climacteric fruit must be harvested when ripe."],
        ]),
        H("Ethylene and ripening"),
        T("**Ethylene** (C2H4) is a gaseous plant hormone made by plants, especially in ripening fruit and damaged tissue. In climacteric fruit it is "
          "**autocatalytic**: a little ethylene triggers more ethylene production. In commercial ripening rooms bananas and mangoes are exposed to ethylene "
          "(of the order of 10 to 100 ppm, at a controlled temperature and high humidity; check your textbook for figures). Some traders use calcium carbide "
          "to give off acetylene, which has a similar effect, but it can be contaminated and dangerous to handle and is banned or restricted in "
          "many places: check the current rules."),
        KEY("What happens during ripening", "These are the changes examiners expect.", cards=[
            ["Colour", "Chlorophyll breaks down (green fades); carotenoids or anthocyanins show or are made (yellow, orange, red)."],
            ["Texture", "Pectin-splitting enzymes (such as polygalacturonase) soften the cell walls."],
            ["Sugar and acid", "Starch changes to sugars (in a banana almost all of the starch), organic acids fall, and the fruit becomes sweeter."],
            ["Flavour", "Volatile esters and other aroma compounds form; astringent tannins fall and astringency goes."],
        ]),
        T("**Maturity versus ripeness.** A fruit must be picked mature enough to ripen properly. Common maturity indices are skin colour, firmness, "
          "days after flowering, the fullness or angularity of the fingers of a banana, total soluble solids (measured with a refractometer in °Brix), and the "
          "starch test with iodine for apples."),
        H("Controlling post-harvest life"),
        KEY("Tools", "Match each tool to the process it controls.", cards=[
            ["Temperature", "Precool soon after harvest and store at the lowest safe temperature (above the chilling-injury limit)."],
            ["Humidity", "Fresh produce loses water by transpiration and shrivels. High relative humidity (about 85 to 95%) slows the loss; too wet allows rot."],
            ["Atmosphere", "Low O2 (about 2 to 5%) and raised CO2 in controlled or modified atmosphere slow respiration and ethylene action; too low O2 causes fermentation."],
            ["Ethylene control", "Keep climacteric fruit apart from sensitive produce; use ethylene absorbers (potassium permanganate), ventilation, or 1-MCP (blocks the ethylene receptor) where permitted."],
            ["Handling", "Bruises and cuts raise respiration and ethylene and let rot in: harvest with care, use clean crates and avoid pressing."],
        ]),
        MISTAKE("Saying non-climacteric fruit do not respire", "All living produce respires. Non-climacteric fruit show no rise in respiration and no ethylene burst at ripening; they still respire at a lower rate."),
        MISTAKE("Mixing up maturity and ripeness", "Mature means the fruit is able to ripen after harvest. Ripe means it is ready to eat. Mango and banana are harvested mature but unripe; their ripening can be managed afterwards."),
        QUIZ("Which fruit is non-climacteric?",
             ["Banana", "Mango", "Pineapple", "Avocado"], 2,
             "Pineapple, like citrus and grapes, does not show a climacteric rise and must be picked when ripe.",
             hint="Which fruit does not ripen further after being cut from the plant?",
             feedback=["Banana is climacteric: it is harvested green and ripened.", "Mango is climacteric.", "", "Avocado is climacteric: it ripens only after harvest."]),
        QUIZ("The respiratory quotient of tissue respiring only glucose in air is",
             ["0.7", "1.0", "1.33", "0.5"], 1,
             "Six CO2 are produced for six O2 used, so RQ = 1.",
             hint="Count CO2 and O2 in the glucose equation.",
             feedback=["0.7 is typical of fat as substrate.", "", "1.33 is the value for malic acid.", "0.5 does not match any common substrate."]),
        H("Practice"),
        PQ("Define the respiratory quotient and say what an RQ of 1.0 shows.", "RQ is the ratio of CO2 produced to O2 consumed. An RQ of about 1.0 shows that carbohydrate (such as glucose) is the substrate of aerobic respiration."),
        PQ("Rates of respiration are 25 mg CO2 per kg per hour at 10 °C and 62.5 mg at 20 °C. Calculate Q10 and predict the rate at 30 °C.", "Q10 = 62.5 / 25 = 2.5. Rate at 30 °C = 62.5 x 2.5 = 156.25, about 156 mg CO2 per kg per hour."),
        PQ("Distinguish climacteric from non-climacteric fruit, with two examples of each, and say why the difference matters to a trader.", "Climacteric fruit (banana, mango) show a rise in respiration and ethylene at ripening and can ripen after harvest, so they can be picked mature but unripe, shipped firm and ripened near the market. Non-climacteric fruit (pineapple, citrus) do not ripen further after harvest, so they must be picked ripe, and have a shorter marketable life once ripe."),
        PQ("Explain how storing bananas in a cool, humid store with a low oxygen atmosphere extends their life.", "Cool temperature lowers the respiration rate (Q10 of 2 to 3) and ethylene action; high humidity limits water loss by transpiration; low O2 and raised CO2 reduce respiration and ethylene action. The temperature must not fall below the chilling limit of about 12 to 13 °C and O2 must not be so low that fermentation begins."),
        TIP("Exam link: post-harvest physiology appears in Paper 1 (climacteric examples, RQ, ethylene) and in Paper 2 essays on storage of fruits and vegetables and on the causes of post-harvest loss. Name the process and the factor controlling it."),
        SUM("Harvested produce is alive: respiration uses up reserves, releases heat and CO2, and is the main cause of quality loss.",
            "RQ = CO2 produced / O2 used: 1.0 for carbohydrate, about 0.7 for fat, above 1 for organic acids or fermentation.",
            "Q10 of 2 to 3: every 10 °C of cooling cuts the respiration rate by half or more.",
            "Climacteric fruit (banana, mango, tomato) have a respiration peak and ethylene burst; non-climacteric fruit (citrus, pineapple) do not.",
            "Control uses low temperature, high humidity, modified or controlled atmosphere, ethylene management and gentle handling."),
    ],
))

# ------------------------------------------------------------------ 7. Cereals, milling and baking
LESSONS.append(lesson(
    module=M2,
    topic="Cereals, milling and baking",
    title="Cereals, roller milling of wheat and the science of baking",
    slug="fsu1-cereals-milling-baking",
    minutes=25,
    summary="Follow cereal grain from structure to flour to bread: roller milling, extraction rate, gluten, the stages of breadmaking, staling, and the processing of maize, sorghum, millet and composite flours.",
    objectives=[
        "Describe the structure of a cereal grain and what each part contributes",
        "Describe roller milling of wheat, conditioning and extraction rate, and carry out milling calculations",
        "Explain the role of gluten and of each ingredient and stage in breadmaking, including staling",
        "Describe the processing of maize, sorghum, millet and rice and the use of composite flours",
    ],
    key_concepts=["Grain structure", "Conditioning", "Break and reduction rolls", "Extraction rate", "Gluten (gliadin and glutenin)", "Fermentation and proof", "Starch gelatinisation", "Staling and retrogradation", "Composite flour"],
    blocks=[
        H("Introduction"),
        T("Bread, buns, beignets, couscous made from maize, and porridge from sorghum all begin as grain. Wheat does not grow well in much of Cameroon, "
          "and wheat flour is mostly imported (check the current figures), so there is strong interest in using local maize, sorghum, millet and "
          "cassava in bakery products. To do this well, a food scientist needs to know what is in a grain, how it is milled, and what gives bread its structure."),
        H("The structure of a cereal grain"),
        KEY("Three parts of a wheat grain", "The same plan applies to maize, sorghum and rice, with differences of detail.", cards=[
            ["Bran (about 13 to 15%)", "The outer layers: pericarp, seed coat and the aleurone layer. Rich in fibre, minerals and B vitamins; tough and dark."],
            ["Endosperm (about 80 to 85%)", "The food store, mostly starch granules held in a protein matrix. This is what is milled into white flour."],
            ["Germ (about 2 to 3%)", "The embryo: rich in oil, protein, vitamin E and B vitamins. The oil makes whole grain flour go rancid faster."],
        ]),
        T("Wheat grain is about 70% starch, 10 to 14% protein, 2% fat and 1.5% minerals. **Hard wheat** has more protein (about 11 to 14%) and gives strong "
          "flour for bread; **soft wheat** has less protein (about 8 to 10%) and suits cakes and biscuits; **durum wheat** is used for pasta."),
        H("Roller milling of wheat"),
        IMG("alfsu1-milling-flow.svg", alt="Flow diagram of roller milling: cleaning, conditioning, break rolls, sifting and purifying, reduction rolls to white flour, with bran and germ removed as a by-product stream",
            caption="Figure 1. Stages of roller milling."),
        KEY("What happens at each stage", "Learn the purpose of each step.", cards=[
            ["Cleaning", "Sieves, aspirators, destoners and magnets remove stones, dust, metal, straw and foreign seeds."],
            ["Conditioning (tempering)", "Water is added to bring the grain to about 15 to 17% moisture and the grain rests for several hours. This toughens the bran so that it comes off in large flakes, and mellows the endosperm so that it breaks into particles easily."],
            ["Break rolls", "Pairs of corrugated steel rolls turning at different speeds crack the grain open and scrape the endosperm off the bran as coarse particles (semolina)."],
            ["Sifting and purifying", "Sieves (plansifters) separate the particles by size; purifiers use air currents to remove bran specks."],
            ["Reduction rolls", "Smooth rolls grind the clean semolina into fine flour. Repeated grinding and sifting give a number of flour streams that are blended."],
        ]),
        D("The **extraction rate** is the percentage of the grain that is recovered as flour: mass of flour divided by mass of grain milled, times 100. "
          "White flour is about 72 to 78%; wholemeal flour is 100% (nothing is removed). The rest is bran and germ offals, used mainly for animal feed.", title="Extraction rate", formula=r"\text{extraction rate} = \frac{\text{mass of flour}}{\text{mass of grain}} \times 100\%"),
        T("**Flour quality** is judged by colour (the lower the ash or mineral content, the whiter the flour, because bran is rich in minerals), protein content and quality, "
          "moisture (about 14% or below for safe storage) and enzyme activity. The **falling number** test measures alpha-amylase: grain that "
          "has sprouted in the field gives a low falling number and a sticky crumb. White flour is often enriched with iron and B vitamins, and with folic acid "
          "(see the fortification lesson); check the current rules in your country."),
        EX("Worked example 1: water for conditioning",
           intro="1 000 kg of wheat at 11% moisture is to be conditioned to 16% moisture before milling. How much water must be added?",
           steps=[
               S("Dry solids stay the same", math=r"1000 \times (1 - 0.11) = 890 \text{ kg}"),
               S("Mass of grain at 16% moisture", math=r"\frac{890}{1 - 0.16} = 1059.5 \text{ kg}"),
               S("Water to add", math=r"1059.5 - 1000 = 59.5 \text{ kg}"),
           ], check=r"\frac{1059.5 - 890}{1059.5} = 0.16"),
        EX("Worked example 2: extraction rate and flour yield",
           intro="A mill grinds 5 tonnes of cleaned wheat and obtains 3.6 tonnes of white flour. What is the extraction rate? How much flour is made from 8 tonnes at the same rate? (Teaching data.)",
           steps=[
               S("Extraction rate", math=r"\frac{3.6}{5} \times 100 = 72\%"),
               S("Flour from 8 t", math=r"8 \times 0.72 = 5.76 \text{ tonnes}"),
               S("By-products", text="5 - 3.6 = 1.4 t of bran, germ and other offals (28%)."),
           ]),
        H("Gluten and the science of breadmaking"),
        D("**Gluten** is the elastic protein network formed when wheat flour is mixed with water and kneaded. It is made from two groups of wheat proteins: "
          "**glutenin** (gives strength and elasticity) and **gliadin** (gives extensibility, so the dough can stretch). The network traps the carbon dioxide made by the yeast, "
          "so the dough rises. Maize, rice, sorghum and millet do not form gluten, which is why 100% maize bread does not rise like wheat bread.", title="Gluten"),
        KEY("Roles of ingredients", "Say what each does and what happens without it.", cards=[
            ["Flour", "Starch and gluten-forming protein build the structure."],
            ["Water", "Hydrates the protein to form gluten and starch to gelatinise; typically about 55 to 65% of the flour weight."],
            ["Yeast (Saccharomyces cerevisiae)", "Ferments sugar to carbon dioxide and ethanol, which make the dough rise and form flavour."],
            ["Salt (about 2%)", "Flavour; strengthens gluten; slows the yeast and controls the rate of fermentation."],
            ["Sugar and fat", "Sugar feeds the yeast and browns the crust; fat softens the crumb, lubricates the gluten and delays staling."],
            ["Improvers", "Ascorbic acid and enzymes strengthen dough and improve volume; some are regulated, so check local rules (for example potassium bromate is banned in many countries)."],
        ]),
        F(r"\mathrm{C_6H_{12}O_6} \;\longrightarrow\; 2\,\mathrm{C_2H_5OH} + 2\,\mathrm{CO_2}", title="Alcoholic fermentation by yeast"),
        EX("Worked example 3: gas from yeast",
           intro="In a dough, 10 g of glucose is fermented completely by yeast. Find the mass of CO2 and its volume at 30 °C and 1 atmosphere (R = 0.08206 L atm per mol per K; molar mass of glucose 180.2 g per mol; CO2 44.0 g per mol).",
           steps=[
               S("Moles of glucose", math=r"\frac{10}{180.2} = 0.0555 \text{ mol}"),
               S("Moles of CO2 (2 per glucose)", math=r"2 \times 0.0555 = 0.111 \text{ mol}"),
               S("Mass of CO2", math=r"0.111 \times 44.0 = 4.89 \text{ g}"),
               S("Volume at 303 K", math=r"V = \frac{nRT}{P} = 0.111 \times 0.08206 \times 303 = 2.76 \text{ L}"),
           ]),
        KEY("Stages of breadmaking", "Learn the order and the change at each stage.", cards=[
            ["1 Mixing and kneading", "Gluten forms and gas bubbles are trapped; yeast is spread through the dough."],
            ["2 Bulk fermentation", "Yeast produces CO2 and flavour; the dough rises. Enzymes (amylases) break some starch to sugars for the yeast."],
            ["3 Knock-back, shaping and proof", "Large gas pockets are removed, the dough is shaped, and the final rise (proof) in a warm humid place."],
            ["4 Baking", "Oven spring: gas expands and ethanol evaporates. At about 60 to 80 °C starch gelatinises and gluten sets; yeast is killed at about 55 °C. The crust browns by Maillard and caramelisation reactions above about 150 °C; the crumb reaches only about 98 to 100 °C."],
            ["5 Cooling", "The structure sets and moisture spreads; slicing before cooling gives a gummy crumb."],
        ]),
        T("**Staling.** Bread becomes firm and crumbly over a day or two, mainly because the starch (especially amylopectin) slowly **retrogrades**: its chains "
          "re-form ordered crystalline structures, and moisture moves from crumb to crust. It is *not* chiefly a drying-out process, as warming stale bread "
          "briefly reverses it. Fat, emulsifiers such as mono- and diglycerides and anti-staling enzymes slow it; refrigeration speeds it; freezing stops it."),
        EX("Worked example 4: a baker's formula and a composite flour",
           intro="A dough uses flour 100%, water 60%, yeast 2%, salt 2%, sugar 5% and fat 4% (baker's percentages, based on flour weight). (a) How much dough is made from 1 000 g of flour? (b) A composite flour is 80% wheat (12% protein) and 20% cassava (2% protein). What is the protein of the blend?",
           steps=[
               S("(a) Add the percentages", math=r"100 + 60 + 2 + 2 + 5 + 4 = 173\% \;\Rightarrow\; 1.73 \times 1000 = 1730 \text{ g}"),
               S("(b) Weighted mean", math=r"0.80 \times 12 + 0.20 \times 2 = 9.6 + 0.4 = 10.0\%"),
               S("Meaning", text="Replacing 20% of the flour by cassava lowers the protein and dilutes the gluten, so the loaf is smaller. Gluten, emulsifiers and a lower level of replacement can compensate."),
           ]),
        H("Tropical cereals and composite flours"),
        KEY("Processing of local cereals", "Compare with wheat.", cards=[
            ["Maize", "Dry milling removes the germ and bran to give grits, meal and flour (the germ oil makes whole maize meal spoil faster). Wet milling separates starch, gluten meal, germ and fibre for industrial products."],
            ["Sorghum and millet", "Hard grains; the bran may contain tannins or oil. Decortication (pounding or abrasive dehulling) before milling gives a better flour. No gluten, so they are used in porridges, flat breads and local beers."],
            ["Rice", "Paddy is dehusked to brown rice; milling removes bran and germ to give white rice, which loses vitamins and fibre. Parboiling before milling keeps more nutrients."],
            ["Composite flour", "A blend of wheat with maize, sorghum, cassava or other local flour (often 10 to 30%) to cut wheat imports. Bread volume falls as the proportion rises."],
        ]),
        T("**Storage.** Grain is stored at about 13 to 14% moisture or less (check your local rules for each grain). Insects (weevils, the larger grain borer), moulds that "
          "can make aflatoxins, and rodents cause losses. Dry the grain quickly, clean the store, use hermetic or well-ventilated stores and check regularly."),
        MISTAKE("Explaining staling as simple drying", "Staling is mainly starch retrogradation and water redistribution. A stale loaf can be freshened by warming because the starch crystals melt; a simply dried loaf could not be revived."),
        MISTAKE("Confusing extraction rate with flour moisture or protein", "Extraction rate is the percentage of the grain that becomes flour. A high rate gives darker flour with more fibre and minerals; a low rate gives whiter flour with less."),
        QUIZ("Which part of the wheat grain is milled into white flour?",
             ["Bran", "Germ", "Endosperm", "Aleurone only"], 2,
             "White flour is the milled starchy endosperm. Bran and germ are removed as offals.",
             hint="Which part holds the starch and protein store?",
             feedback=["Bran is the fibre-rich outer layers, removed in white flour.", "The germ is removed because its oil makes the flour go rancid.", "", "The aleurone is part of the bran layers."]),
        QUIZ("Why does bread made only from maize flour not rise like wheat bread?",
             ["Maize contains no starch", "Maize does not form a gluten network to trap the gas", "Yeast cannot ferment maize", "Maize flour is too acid"], 1,
             "Gluten-forming proteins are specific to wheat (and related cereals), so the dough cannot hold the gas.",
             hint="What network holds the carbon dioxide in a wheat dough?",
             feedback=["Maize is rich in starch.", "", "Yeast ferments sugars from maize starch perfectly well.", "Acidity is not the problem."]),
        H("Practice"),
        PQ("Define extraction rate. 4.5 tonnes of wheat give 3.2 tonnes of flour. Calculate the extraction rate.", "Extraction rate is the percentage of the grain recovered as flour. 3.2 / 4.5 x 100 = 71.1%."),
        PQ("Explain the purpose of conditioning (tempering) wheat before milling.", "Adding water (to about 15 to 17% moisture) and resting makes the bran tougher so it comes off in large flakes rather than powder, and makes the endosperm softer so it grinds easily to flour. This gives cleaner separation of flour and bran, a higher yield and whiter flour."),
        PQ("Describe what happens in the dough and the loaf at each of: kneading, fermentation, baking.", "Kneading develops the gluten network (glutenin and gliadin) and traps air. Fermentation: yeast ferments sugars to CO2 and ethanol, so the dough rises and develops flavour. Baking: gas expands (oven spring), starch gelatinises and gluten sets at about 60 to 80 °C, yeast dies, and the crust browns by Maillard and caramelisation reactions."),
        PQ("Why is bread made with 30% cassava flour smaller and denser than bread from wheat flour only? Suggest one way to improve it.", "Cassava has little protein and no gluten, so replacing wheat dilutes the gluten network and the dough holds less gas, giving less volume. Improvement: add vital wheat gluten, use an emulsifier or enzyme improver, or lower the replacement level to about 10 to 20%."),
        TIP("Exam link: cereals, milling and baking appear in Paper 1 (structure, extraction rate, gluten, staling) and in Paper 2 essays on cereal products. Paper 3 cookery work may involve doughs and batters: link the stages of breadmaking to practical observations."),
        SUM("A grain has bran (fibre), endosperm (starch and protein, milled to white flour) and germ (oil and vitamins).",
            "Roller milling: clean, condition, break rolls, sift, purify, reduction rolls; extraction rate = flour / grain times 100 (white about 72 to 78%).",
            "Gluten (glutenin and gliadin) traps CO2 from yeast fermentation; maize, sorghum and millet do not form gluten.",
            "Baking gelatinises starch, sets gluten and browns the crust by Maillard and caramelisation; staling is mainly starch retrogradation.",
            "Local cereals are milled differently (decortication, dry or wet milling); composite flours save wheat but lower loaf volume."),
    ],
))

# ------------------------------------------------------------------ 8. Roots, tubers and plantain
LESSONS.append(lesson(
    module=M2,
    topic="Roots, tubers and plantain",
    title="Cassava, yam, cocoyam and plantain: detoxification, storage and processing",
    slug="fsu1-roots-tubers-plantain",
    minutes=24,
    summary="Roots, tubers and plantain are staple foods of Cameroon that spoil fast. Study cassava cyanide and its removal in gari and bobolo, yam dormancy, curing and storage, plantain processing, and why post-harvest losses are so high.",
    objectives=[
        "Explain the cyanogenic glucoside problem in cassava and how each processing step lowers cyanide",
        "Describe the main processing methods for cassava (gari, fufu, bobolo or miondo, flour) and do a mass balance",
        "Explain curing, dormancy, storage and spoilage of yam and cocoyam",
        "Describe plantain ripening, products (chips, flour) and causes of browning and losses",
    ],
    key_concepts=["Linamarin and linamarase", "Hydrogen cyanide and konzo", "Post-harvest physiological deterioration", "Fermentation and pressing", "Garification", "Yam dormancy and curing", "Cocoyam oxalate", "Plantain starch to sugar", "Acrylamide in fried chips"],
    blocks=[
        H("Introduction"),
        T("Gari, fufu, bobolo or miondo, boiled or fried yam, roasted or fried plantain: roots, tubers and plantain feed millions of people in Cameroon. They "
          "give cheap energy (mostly starch) but have two weaknesses. They contain a lot of water (60 to 80%), so they are **bulky and perishable**, and "
          "some of them contain **natural toxins** that must be removed in preparation. Processing is how people have made them safe, storable and convenient for centuries."),
        CODE("""Approximate composition per 100 g of the edible part (check your food composition table)
Food         Water (g)   Starch/carbohydrate (g)   Protein (g)   Fat (g)
Cassava       60-65          30-35                    1-2          0.3
Yam           65-75          20-27                    1.5-2        0.2
Cocoyam       65-75          20-25                    1.5-2        0.2
Plantain      60-70          25-30                    1-1.5        0.3""", "text", title="Table 1. Approximate composition (typical ranges for teaching)"),
        T("Note the low protein: a diet that is mostly roots and plantain needs other foods (beans, groundnuts, fish, leaves) to meet protein needs. "
          "The Board's 2023 report asks students to learn the Food Composition Table (FCT) well, so practise reading it for these foods."),
        H("Cassava: the cyanide problem"),
        D("**Cyanogenic glucosides** are compounds that release hydrogen cyanide (HCN) when the tissue is crushed. In cassava the main one is "
          "**linamarin** (with a little lotaustralin). When cells are broken, the enzyme **linamarase** (in separate cell compartments) splits linamarin to a "
          "cyanohydrin, which then breaks down to HCN gas and acetone. Bitter varieties and the peel contain much more than sweet varieties and the pulp.", title="Linamarin"),
        T("**Health effects.** A single large dose of raw or poorly processed bitter cassava can cause acute poisoning (headache, vomiting, dizziness, in severe cases death). "
          "A long diet of inadequately processed bitter cassava, especially with little protein (sulphur amino acids are needed to detoxify cyanide), is "
          "linked to **konzo**, a sudden and permanent paralysis of the legs reported in several African countries, and to tropical ataxic neuropathy; "
          "the thiocyanate formed can also add to goitre where iodine is lacking. Hence the importance of full processing."),
        KEY("How processing removes cyanide", "Each step has a different effect. Learn it as a chain.", cards=[
            ["Peeling", "Removes the rind, which has the highest concentration."],
            ["Grating or crushing", "Breaks cells so that linamarase meets linamarin; HCN is released and can escape."],
            ["Fermentation (soaking or pressing under sacks)", "Microbial and plant enzymes continue the breakdown; acids form; flavour develops. Soaking or a long ferment gives large removals."],
            ["Pressing and draining", "Water-soluble glucosides and free cyanide leave in the liquid."],
            ["Roasting, frying or steaming", "HCN is a gas (it boils at about 26 °C), so heat drives off what is left. Boiling whole pieces for a short time is *less* effective."],
            ["Sun drying of chips or grated pulp", "Some HCN escapes as the pieces dry; small pieces and thin layers help. Sun-dried whole roots keep more."],
        ]),
        T("A commonly quoted safety guideline (WHO, Codex) is that cassava flour and gari should contain no more than about 10 mg of total hydrogen cyanide per kg: check the "
          "current standard before quoting it in an answer."),
        EX("Worked example 1: cyanide removal",
           intro="Grated cassava mash contains 200 mg HCN equivalents per kg (dry basis). After fermentation, pressing and roasting the gari contains 12 mg per kg (dry basis). (a) What percentage was removed? (b) What further removal would be needed to reach 10 mg per kg? (Teaching data.)",
           steps=[
               S("(a) Percentage removed", math=r"\frac{200 - 12}{200} \times 100 = 94\%"),
               S("(b) Total needed for 10 mg per kg", math=r"\frac{200 - 10}{200} \times 100 = 95\%"),
               S("Conclusion", text="The process must remove at least 95%. Here 94% falls just short, so a longer fermentation or more thorough roasting would be advised."),
           ]),
        H("Cassava products"),
        KEY("Main products", "Know the steps of at least two.", cards=[
            ["Gari", "Peel, wash, grate, put in sacks and press under weights for two to four days (fermentation and dewatering), sieve, then roast in a shallow pan with constant stirring (garification) to a dry, crisp granule. Stored dry."],
            ["Fufu (cassava or water fufu)", "Peeled roots are soaked for two to four days until soft, fibres removed, the paste sieved and boiled or steamed and pounded."],
            ["Bobolo or miondo (cassava sticks)", "Fermented (retted) cassava is ground to a paste, wrapped in leaves and steamed or boiled. Sold as a ready staple."],
            ["Cassava flour and chips", "Peeled roots are sliced, dried, then milled. Fast drying in thin layers keeps quality; slow drying invites mould."],
            ["Starch and tapioca", "Industrial products from washing the grated pulp and settling the starch."],
        ]),
        EX("Worked example 2: a gari mass balance",
           intro="100 kg of fresh roots lose 20% of their mass as peel. The peeled root has 35% dry matter. If the gari is dried to 12% moisture and no dry matter is lost, how much gari is made? (Teaching data.)",
           steps=[
               S("Peeled roots", math=r"100 \times 0.80 = 80 \text{ kg}"),
               S("Dry matter", math=r"80 \times 0.35 = 28 \text{ kg}"),
               S("Gari at 12% moisture", math=r"\frac{28}{1 - 0.12} = 31.8 \text{ kg}"),
               S("Real yields", text="Real yields are lower, because starch and sugars are lost with the pressed liquid and as waste, and roots vary: check local data."),
           ]),
        T("**Post-harvest physiological deterioration (PPD).** Cassava roots start to deteriorate very quickly after harvest: blue-black streaks appear in the vascular tissue "
          "within a day or two (oxidative reactions after wounding) and the root becomes unmarketable within a few days. So cassava is processed or "
          "sold on the day of harvest or soon after, or stored by waxing, in moist sawdust, or as dried chips. (Check your textbook for timings.)"),
        H("Yam and cocoyam"),
        T("**Yam** tubers have a **dormancy period** of a few months after harvest, when respiration is low and sprouting does not occur. When dormancy ends, "
          "sprouting begins and respiration rises, so stored tubers lose mass and starch. Spoilage comes from rots (fungi such as *Penicillium* and *Botryodiplodia*, "
          "and bacteria), sprouting, insects, nematodes and rodents. Tubers are cured and then stored in a cool, dry, shaded and well-ventilated place such as a "
          "yam barn."),
        D("**Curing** is a short treatment of freshly harvested tubers in warm (about 29 to 32 °C) and very humid air (above about 90%) for a few days. Wounds heal by forming a layer of "
          "cork (periderm), which seals the surface against water loss and rot-causing microbes. (Conditions vary, check your textbook.)", title="Curing"),
        EX("Worked example 3: loss in store",
           intro="A trader's store loses about 5% of the mass of its yams each month from respiration, sprouting and rot, each month taken on the mass left at the start of the month. How much of 100 kg remains after 6 months? (Teaching rate, invented for practice.)",
           steps=[
               S("Compound loss", math=r"100 \times 0.95^{6}"),
               S("Calculate", math=r"0.95^6 = 0.7351 \Rightarrow 73.5 \text{ kg}"),
               S("Meaning", text="About a quarter of the yams are lost in six months, before any damage by rot is counted separately. Good curing and ventilation cut this."),
           ]),
        T("**Cocoyam (taro and macabo)** contains needle-like crystals of calcium oxalate, which make raw tubers and leaves irritating to the mouth and skin. "
          "Thorough cooking, soaking or fermentation removes most of the irritation. (Oxalate also binds calcium; see the anti-nutrient lessons from Lower Sixth.) "
          "Some wild yams contain bitter alkaloids and must be processed with care."),
        H("Plantain"),
        T("Plantain is climacteric (see the post-harvest physiology lesson). Green plantain is rich in starch (about 20 to 30%); on ripening, the starch is "
          "converted to sugars, the peel yellows and then blackens, and the flesh softens. Products depend on the stage:"),
        KEY("Stage and product", "Choose the right ripeness.", cards=[
            ["Green (unripe)", "Boiled, fried as chips, or dried and milled to plantain flour. Firm and starchy; low in sugar."],
            ["Ripe", "Roasted or fried as slices; sweet and soft because of the sugars; darkens fast on frying and absorbs more oil."],
            ["Plantain chips", "Thin slices of unripe plantain, often soaked or blanched, then fried in hot oil (about 160 to 180 °C) and salted. Low sugar gives a pale colour."],
            ["Flour", "Peeled slices are dried, then milled. Used in porridges and baked foods; peel and dust browning is controlled by quick drying and acidified rinse."],
        ]),
        T("**Browning and acrylamide.** Peeled or cut plantain, yam and potato brown quickly because polyphenol oxidase makes brown pigments in the air. Brief soaking in water or a "
          "dilute acid, blanching, or fast processing limits it. Frying starchy foods at high temperatures can also form **acrylamide**, a potentially harmful compound, from the amino "
          "acid asparagine and reducing sugars. Lower frying temperatures, avoiding over-browning and choosing unripe (low sugar) plantain reduce it."),
        MISTAKE("Saying cassava is poisonous and therefore unsafe to eat", "Properly processed cassava is a safe staple. The risk comes from cutting corners: short fermentation, not pressing, or eating raw bitter roots. Name the steps that remove cyanide."),
        MISTAKE("Using short boiling of whole pieces as a cyanide treatment", "Whole boiled pieces keep much of their linamarin because the cells are not broken. Grating, fermenting and draining are far more effective."),
        QUIZ("Which step of gari making breaks cassava cells so that linamarase can act on linamarin?",
             ["Roasting", "Grating", "Peeling", "Sieving"], 1,
             "Grating or crushing ruptures the cells, allowing the enzyme to meet its substrate and release HCN.",
             hint="Which step damages the tissue?",
             feedback=["Roasting drives off HCN gas but does not release it.", "", "Peeling removes the rind but does not damage the pulp cells.", "Sieving only separates by particle size."]),
        QUIZ("Curing yam tubers before storage is done to",
             ["start sprouting early", "heal wounds with a layer of cork and reduce rot and water loss", "dry the tubers completely", "chill the tubers below 5 °C"], 1,
             "Warm, humid curing encourages wound periderm, sealing damaged areas against microbes and water loss.",
             hint="Which problem do cut or bruised surfaces cause?",
             feedback=["Sprouting is not wanted; it uses up reserves.", "", "Complete drying would shrivel the tubers.", "Yams suffer chilling injury at low temperatures."]),
        H("Practice"),
        PQ("Describe how the cyanide content of cassava is reduced during gari production.", "Peeling removes the cyanide-rich rind. Grating breaks the cells so linamarase hydrolyses linamarin to cyanohydrin and HCN. Fermentation under pressure continues the enzyme and microbial breakdown and drains the liquid containing soluble glucosides and cyanide. Roasting drives off the remaining HCN gas, which boils at about 26 °C."),
        PQ("120 kg of cassava roots lose 25% as peel. The peeled roots contain 32% dry matter. Calculate the mass of gari at 11% moisture, assuming no dry matter is lost.", "Peeled = 120 x 0.75 = 90 kg. Dry matter = 90 x 0.32 = 28.8 kg. Gari = 28.8 / 0.89 = 32.4 kg."),
        PQ("Explain why yam tubers are cured and stored in well-ventilated barns.", "Curing in warm humid air heals wounds with a cork layer, which reduces water loss and entry of rot organisms. A cool, shaded, ventilated barn keeps respiration low, avoids heat and moisture build-up that favour rots and sprouting, and keeps rodents and insects easier to control."),
        PQ("Why are plantain chips made from unripe rather than ripe plantain?", "Unripe plantain has high starch and low sugar, so chips fry to a crisp, pale product with little oil uptake. Ripe plantain has high sugar, which browns and burns quickly in frying (Maillard reaction) and gives a soft, oily slice; low sugar also lowers acrylamide formation."),
        TIP("Exam link: root crops, plantain and their products appear in Paper 1 (cyanide, curing, products), Paper 2 essays on food processing and the use of local staples, and in practical work with the Food Composition Table. Always link the processing step to the hazard it removes."),
        SUM("Roots, tubers and plantain are starchy, high-moisture and perishable foods with low protein.",
            "Cassava has linamarin; crushing releases HCN through linamarase. Peeling, grating, fermenting, pressing and roasting remove it; guideline about 10 mg HCN per kg in flour or gari (check the current standard).",
            "Gari, fufu, bobolo or miondo and flour are the main cassava products; cassava itself spoils within days (PPD).",
            "Yam is cured (warm, humid, to heal wounds) then stored cool, dry and ventilated; dormancy ends with sprouting and mass loss.",
            "Plantain starch changes to sugar on ripening; unripe plantain is used for chips and flour; frying limits and acrylamide control matter."),
    ],
))

# ------------------------------------------------------------------ 9. Oilseeds and oils
LESSONS.append(lesson(
    module=M2,
    topic="Oilseeds and oils",
    title="Oilseeds and oils: extraction, refining, hydrogenation, margarine and rancidity",
    slug="fsu1-oilseeds-oils",
    minutes=25,
    summary="From seed or palm fruit to refined oil and margarine: pressing and solvent extraction, the four refining steps, hydrogenation, the margarine flow diagram, the three types of rancidity and how oil quality is tested.",
    objectives=[
        "Describe extraction of oil from oilseeds and palm fruit by pressing and solvent extraction, and calculate oil recovery",
        "Describe the refining steps (degumming, neutralisation, bleaching, deodorisation) and the purpose of each",
        "Explain hydrogenation and the manufacture of margarine with a flow diagram",
        "Define rancidity, explain its types and prevention, and calculate FFA, peroxide and iodine values",
    ],
    key_concepts=["Oilseeds and palm oil", "Pressing and solvent extraction", "Degumming, neutralisation, bleaching, deodorisation", "Hydrogenation and trans fats", "Margarine emulsion", "Hydrolytic, oxidative and ketonic rancidity", "Free fatty acids", "Peroxide value", "Iodine and saponification values"],
    blocks=[
        H("Introduction"),
        T("Palm oil, groundnut oil, soybean oil, cottonseed oil and shea butter are all part of Cameroon's food and farming economy. Fats and oils give "
          "energy (about 37 kJ per gram, more than twice that of carbohydrate), carry the fat-soluble vitamins and make food smooth and tasty. "
          "But oils spoil, and the Board's 2023 report notes that many candidates could not define rancidity or give measures to prevent it, or "
          "draw the flow diagram of margarine manufacture. This lesson covers both clearly."),
        H("Sources and extraction"),
        KEY("Common oils", "Learn one example of each type.", cards=[
            ["Palm oil (mesocarp of the fruit)", "About half saturated (palmitic acid); red because of carotenes; semi-solid at room temperature."],
            ["Palm kernel and coconut oil", "From the kernel; rich in lauric acid and about 80% or more saturated; solid in cool weather."],
            ["Groundnut, soybean, sunflower, cottonseed", "Mainly unsaturated (oleic and linoleic acids); liquid at room temperature. Soybean also has some linolenic acid. Crude cottonseed oil contains gossypol, a toxin removed in refining."],
            ["Shea butter (kernels of the shea tree)", "A solid vegetable fat, used locally in cooking and also in cosmetics and chocolate industries."],
        ]),
        T("**Seed preparation:** cleaning, dehulling or cracking (the hulls absorb oil), grinding or flaking to break the cell walls, and **conditioning** (heating with a little moisture "
          "to rupture cells, coagulate protein and make the oil flow more easily)."),
        KEY("Extraction methods", "Compare them.", cards=[
            ["Mechanical pressing", "A screw press (expeller) or hydraulic press squeezes the oil out. Simple and no solvent, but the press cake still holds about 5 to 10% oil."],
            ["Solvent extraction", "The flaked seed is washed with hexane, which dissolves the oil; the solvent is evaporated and reused. Leaves under 1% oil in the meal. Needs a safe plant because hexane is flammable. Often a pre-press removes most of the oil first."],
            ["Palm oil (mill)", "Bunches are steamed (sterilised, which stops lipase making free fatty acids and loosens the fruit), the fruit is stripped, digested to a mash and pressed; the oil is clarified and dried. Small producers boil and pound the fruit and skim the oil."],
        ]),
        EX("Worked example 1: oil recovery",
           intro="100 kg of oilseed contains 45 kg of oil. (a) A press leaves 8% oil in the cake. How much oil is recovered? (b) A solvent plant leaves 1% oil in the meal. How much oil is recovered? Treat the rest of the seed as non-oil matter of 55 kg. (Teaching data.)",
           steps=[
               S("(a) Cake mass x contains 55 kg of non-oil matter and 8% oil", math=r"0.92\,x = 55 \Rightarrow x = 59.8 \text{ kg}"),
               S("Oil left in the cake", math=r"0.08 \times 59.8 = 4.8 \text{ kg}"),
               S("Oil recovered by pressing", math=r"45 - 4.8 = 40.2 \text{ kg} \Rightarrow \frac{40.2}{45} = 89\%"),
               S("(b) Solvent: meal mass", math=r"0.99\,x = 55 \Rightarrow x = 55.6 \text{ kg},\; 0.01 \times 55.6 = 0.56 \text{ kg left}"),
               S("Oil recovered", math=r"45 - 0.56 = 44.4 \text{ kg} \Rightarrow \frac{44.4}{45} = 98.8\%"),
           ]),
        H("Refining crude oil"),
        T("Crude oil contains gums (phospholipids), free fatty acids, pigments, trace metals, odours and traces of water. Refining removes these to give a stable, bland, clear oil. "
          "The usual sequence is called RBD (refined, bleached, deodorised):"),
        KEY("Four refining steps", "Say what is removed and how.", cards=[
            ["1 Degumming", "Water or dilute acid hydrates the phospholipids (gums), which are removed by centrifuge. They would darken the oil and make it foam; lecithin is a useful by-product."],
            ["2 Neutralisation", "Sodium hydroxide reacts with free fatty acids to form soaps (soapstock), which are separated by centrifuge and washed out."],
            ["3 Bleaching", "The oil is heated with activated clay (bleaching earth) which adsorbs pigments, traces of metals, soap and peroxides; filtered."],
            ["4 Deodorisation", "Steam is passed through the hot oil (about 180 to 240 °C) under vacuum, which strips off volatile compounds that cause smell and taste, and remaining free fatty acids."],
            ["Winterisation (some oils)", "The oil is chilled and the high-melting fraction is filtered off so that a salad oil stays clear in a refrigerator."],
        ]),
        EX("Worked example 2: soap and sodium hydroxide in neutralisation",
           intro="1 000 kg of crude oil contains 5% free fatty acid, calculated as oleic acid (M = 282.5 g per mol). NaOH is M = 40.0. Find the theoretical mass of NaOH needed and of sodium oleate soap formed (M = 304.4). (Teaching data.)",
           steps=[
               S("Mass of oleic acid", math=r"1000 \times 0.05 = 50 \text{ kg}"),
               S("Moles (kmol)", math=r"\frac{50}{282.5} = 0.177 \text{ kmol}"),
               S("NaOH (1 mol per mol of acid)", math=r"0.177 \times 40.0 = 7.08 \text{ kg}"),
               S("Soap", math=r"0.177 \times 304.4 = 53.9 \text{ kg}"),
               S("Note", text="In practice a small excess of alkali is used, and some neutral oil is lost in the soapstock, which is why refining loss is more than the free fatty acid itself."),
           ]),
        H("Hydrogenation and margarine"),
        D("**Hydrogenation** adds hydrogen to the carbon-carbon double bonds of unsaturated fatty acids in the presence of a nickel catalyst at about 140 to 225 °C. "
          "The oil becomes more saturated and its melting point rises, so a liquid oil becomes a soft or hard fat. It also becomes more resistant to oxidation. "
          "Partial hydrogenation can create **trans fatty acids**, which raise LDL cholesterol and lower HDL, so modern practice avoids it; interesterification and blending of fats "
          "are used instead.", title="Hydrogenation"),
        D("**Margarine** is a water-in-oil emulsion containing at least about 80% fat (many countries set this as a minimum; check local rules), up to about 16% water or skim milk, "
          "salt, an emulsifier such as lecithin, flavour (often diacetyl), colour (beta-carotene) and added vitamins A and D.", title="Margarine"),
        IMG("alfsu1-margarine-flow.svg", alt="Flow chart of margarine manufacture: an oil phase and a water phase are mixed and emulsified, pasteurised, then chilled, crystallised, worked and packed",
            caption="Figure 1. Margarine manufacture. Do not confuse it with cheese, which starts from milk and rennet."),
        T("In the **chilling** step the emulsion is cooled rapidly in a scraped-surface heat exchanger (a 'votator'), which makes many small fat crystals; a "
          "working unit then plasticises it and it is packed. A good margarine has the right mixture of liquid oil and solid fat so that it is spreadable from the refrigerator."),
        EX("Worked example 3: a margarine formulation",
           intro="A 500 kg batch of margarine is 80% fat, 16% water or skim milk, 2% salt and 2% of emulsifier, flavour, colour and vitamins. How much of each is needed?",
           steps=[
               S("Fat", math=r"500 \times 0.80 = 400 \text{ kg}"),
               S("Aqueous phase", math=r"500 \times 0.16 = 80 \text{ kg}"),
               S("Salt", math=r"500 \times 0.02 = 10 \text{ kg}"),
               S("Minor ingredients", math=r"500 \times 0.02 = 10 \text{ kg}"),
           ], check=r"400 + 80 + 10 + 10 = 500"),
        H("Rancidity"),
        D("**Rancidity** is the deterioration of fats and oils (and fatty foods) that produces unpleasant, stale or soapy tastes and smells, making them unfit to eat.", title="Rancidity"),
        KEY("Three types", "Examiners expect type, cause and example.", cards=[
            ["Hydrolytic rancidity", "Water and lipase enzymes (or heat) split triglycerides into free fatty acids and glycerol. Short-chain acids such as butyric acid smell sour or soapy. Seen in butter, damaged palm fruit and whole milk products."],
            ["Oxidative rancidity (auto-oxidation)", "Oxygen attacks unsaturated fatty acids by a free-radical chain reaction (initiation, propagation, termination), forming hydroperoxides that break down to aldehydes and ketones with stale, painty odours. Speeded by heat, light and traces of iron and copper."],
            ["Ketonic rancidity", "Moulds (such as Aspergillus and Penicillium) form methyl ketones from saturated fatty acids in foods like coconut, dried nuts and biscuits."],
        ]),
        KEY("Preventing rancidity", "Match each measure to the cause.", cards=[
            ["Exclude oxygen", "Airtight containers, nitrogen flushing, vacuum or MAP packaging."],
            ["Antioxidants", "Tocopherols, BHA, BHT, propyl gallate or ascorbyl palmitate; citric acid binds metal traces."],
            ["Light and heat", "Store in cool places in opaque or coloured containers; avoid reusing frying oil for too long."],
            ["Water and enzymes", "Dry the product, heat-treat to inactivate lipase (as in palm fruit sterilisation), keep oil free of moisture."],
            ["Avoid metals and moulds", "Use stainless steel, keep stores clean and dry."],
        ]),
        H("Testing oil quality"),
        CODE("""Value                  Measures                       Formula (teaching)
Free fatty acid (FFA)  Hydrolytic rancidity           % FFA (as oleic) = 28.2 x N x V / W
Acid value (AV)        Free acids (mg KOH per g)      AV = 56.1 x N x V / W
Peroxide value (PV)    Primary oxidation (meq per kg) PV = (S - B) x N x 1000 / W
Iodine value (IV)      Unsaturation (g I2 per 100 g)  IV = (B - S) x N x 12.69 / W
Saponification value   Average chain length (mg KOH)  SV = (B - S) x N x 56.1 / W
N = normality of the titrant, V = titre (mL), W = mass of oil (g),
S = sample titre, B = blank titre.""", "text", title="Table 1. Oil quality tests"),
        EX("Worked example 4: FFA, acid value and peroxide value",
           intro="10.0 g of oil is titrated with 0.100 M NaOH and needs 4.5 mL to neutralise the free acids. Another 2.0 g sample needs 4.2 mL of 0.0100 N sodium thiosulphate (blank 0.2 mL) in a peroxide test. Calculate FFA (as oleic), acid value and peroxide value.",
           steps=[
               S("FFA", math=r"\% \text{FFA} = \frac{28.2 \times 0.100 \times 4.5}{10.0} = 1.27\%"),
               S("Acid value", math=r"\text{AV} = \frac{56.1 \times 0.100 \times 4.5}{10.0} = 2.52 \text{ mg KOH/g}"),
               S("Peroxide value", math=r"\text{PV} = \frac{(4.2 - 0.2) \times 0.0100 \times 1000}{2.0} = 20 \text{ meq/kg}"),
               S("Meaning", text="A high peroxide value shows early oxidation. Fresh refined oils are usually under about 10 meq per kg, but check the standard that applies to the oil in your country."),
           ]),
        T("**The iodine value** is high for unsaturated oils: typical teaching values are about 10 for coconut oil, about 50 for palm oil, about 90 for groundnut "
          "oil and over 120 for soybean oil. Hydrogenation lowers it. For a pure fatty acid with n double bonds the iodine value is 253.8 n divided by its "
          "molar mass, times 100: for oleic acid (M = 282.5) it is 89.9, for linoleic acid (M = 280.5, two double bonds) 181.0."),
        MISTAKE("Mixing up hydrolytic and oxidative rancidity", "Hydrolytic needs water and lipase and frees fatty acids. Oxidative needs oxygen and attacks double bonds. Say which type your example shows and the cause."),
        MISTAKE("Drawing a cheese diagram for margarine", "The Board's 2023 report notes that some candidates mixed up the margarine flow diagram with that for cheese. Margarine starts from oil and an aqueous phase and is emulsified and crystallised; cheese starts from milk and rennet."),
        QUIZ("Which refining step removes soaps formed from free fatty acids?",
             ["Degumming only", "Neutralisation with sodium hydroxide followed by separation and washing", "Deodorisation by steam", "Hydrogenation"], 1,
             "NaOH converts free fatty acids to soap, which is removed in the soapstock by centrifuge and washing.",
             hint="Which step uses alkali?",
             feedback=["Degumming removes phospholipids, not soaps.", "", "Deodorisation removes volatile odours and traces of free acids by steam distillation.", "Hydrogenation saturates double bonds."]),
        QUIZ("Which treatment is most likely to cause trans fatty acids?",
             ["Winterisation", "Partial hydrogenation", "Bleaching with clay", "Degumming with water"], 1,
             "In partial hydrogenation some double bonds change from cis to trans form on the catalyst surface.",
             hint="Which step uses nickel and hydrogen?",
             feedback=["Winterisation only separates solids by cooling.", "", "Bleaching removes pigments.", "Degumming removes phospholipids."]),
        H("Practice"),
        PQ("Define rancidity and describe two measures that prevent it.", "Rancidity is the deterioration of fats and oils producing unpleasant stale or soapy tastes and smells. Prevention: exclude oxygen (airtight, nitrogen-flushed or vacuum packs); add antioxidants such as tocopherol, BHA or BHT; keep cool and in the dark; avoid metals such as iron and copper; inactivate lipase and keep the product dry."),
        PQ("Draw and describe the flow diagram for margarine manufacture.", "Prepare the oil phase (blended refined oils and fat, emulsifier, vitamins A and D, colour) and the aqueous phase (water or skim milk, salt, preservative, flavour). Mix them to form a pre-emulsion; pasteurise; chill rapidly and crystallise in a scraped-surface heat exchanger; work or rest in a tube to give plasticity; pack. The product is a water-in-oil emulsion with about 80% fat."),
        PQ("Calculate the iodine value of linoleic acid, M = 280.5 with two double bonds. (Atomic mass of iodine 126.9, I2 = 253.8.)", "IV = (2 x 253.8 / 280.5) x 100 = 181.0 g of iodine per 100 g."),
        PQ("5.0 g of oil requires 3.0 mL of 0.0100 N sodium thiosulphate with a blank of 0.2 mL. Calculate the peroxide value.", "PV = (3.0 - 0.2) x 0.0100 x 1000 / 5.0 = 5.6 meq per kg."),
        TIP("Exam link: oils and fats appear in Paper 1 (definitions, tests, rancidity, hydrogenation), Paper 2 (the Board's 2023 report lists rancidity and the margarine flow diagram as weak areas) and Paper 3 (tests for fats and oils). For a flow diagram, draw boxes in order, label each stage and give the purpose."),
        SUM("Oil is recovered by pressing (5 to 10% left in the cake) or by solvent extraction (under 1% left); palm fruit is steamed first to inactivate lipase.",
            "Refining: degumming, neutralisation, bleaching, deodorisation (RBD); winterisation for salad oils.",
            "Hydrogenation adds H2 over a nickel catalyst; partial hydrogenation forms trans fats. Margarine is a water-in-oil emulsion with about 80% fat.",
            "Rancidity is hydrolytic (lipase and water), oxidative (oxygen and double bonds) or ketonic (moulds); prevent with antioxidants, no oxygen, cool, dark, dry storage.",
            "FFA, acid value, peroxide value, iodine value and saponification value are the main quality tests."),
    ],
))

# ------------------------------------------------------------------ 10. Meat and dairy
LESSONS.append(lesson(
    module=M2,
    topic="Meat and dairy",
    title="From muscle to meat, curing, and the processing of milk",
    slug="fsu1-meat-dairy",
    minutes=25,
    summary="Rigor mortis and the conversion of muscle to meat, ageing, pH and colour problems, curing and smoking; then milk composition, standardisation, cream, butter, cheese and yoghurt, with the calculations that go with them.",
    objectives=[
        "Explain the post-mortem changes of muscle: glycolysis, pH fall, rigor mortis, resolution and ageing",
        "Explain curing with nitrite and the role of smoking, and the faults PSE, DFD and cold shortening",
        "Describe the composition of milk and the processing of cream, butter, cheese and yoghurt",
        "Calculate standardisation of milk fat, added water from freezing point and lactic acid formed in fermentation",
    ],
    key_concepts=["Glycolysis and pH fall", "Rigor mortis and resolution", "Ageing and cold shortening", "PSE and DFD", "Myoglobin colour", "Curing with nitrite", "Casein and whey", "Homogenisation and standardisation", "Churning", "Rennet and acid coagulation"],
    blocks=[
        H("Introduction"),
        T("A butcher in a market in Bafoussam hangs a carcass overnight and the meat is stiff in the morning; two days later it is easier to chew. A dairy turns the same milk into "
          "pasteurised milk, butter, cheese and yoghurt. These changes are chemical and biological, and understanding them explains many questions about quality and safety."),
        H("From muscle to meat"),
        T("In a live animal, muscle gets oxygen from the blood and makes ATP by aerobic respiration. At slaughter the blood stops. The muscle keeps working for a while, but "
          "without oxygen it breaks down its **glycogen** to **lactic acid** (anaerobic glycolysis). The lactic acid cannot be removed, so the **pH falls** from about 7.2 to about 5.5 to 5.7 "
          "in 12 to 24 hours."),
        IMG("alfsu1-rigor.svg", alt="Graph against hours after slaughter: muscle pH falls from 7.2 to about 5.5 within about 24 hours while stiffness rises to a maximum at about 18 to 24 hours, then decreases slowly in the resolution phase",
            caption="Figure 1. pH fall and stiffness after slaughter (beef; times vary with species and temperature)."),
        D("**Rigor mortis** is the stiffening of muscle after death. As ATP runs out, the actin and myosin filaments lock together as permanent **actomyosin** cross-bridges and the muscle becomes hard "
          "and inextensible. It begins within a few hours, is complete in 12 to 24 hours in beef (sooner in poultry and pork) and passes off with **resolution**.", title="Rigor mortis"),
        KEY("Stages", "Learn the order.", cards=[
            ["Pre-rigor", "Muscle is still soft; ATP is being used up; pH is falling. Meat can be cooked now but may toughen if cooled too soon."],
            ["Rigor", "ATP is gone and actomyosin has formed; muscle is stiff, tough and less able to hold water."],
            ["Resolution and ageing", "Muscle's own enzymes (calpains and cathepsins) slowly break down structural proteins, so the meat tenderises. Beef is aged at 0 to 4 °C for days to a few weeks."],
        ]),
        EX("Worked example 1: pH change and lactic acid",
           intro="Muscle pH falls from 7.2 to 5.5. (a) By what factor does the hydrogen ion concentration increase? (b) Muscle holds 10 g of glycogen (as glucose units, 162 g per mol) per kg and all of it is converted to lactic acid (90.1 g per mol, 2 mol per glucose unit). How much lactic acid is made per kg?",
           steps=[
               S("(a) Factor", math=r"10^{7.2 - 5.5} = 10^{1.7} = 50"),
               S("(b) Moles of glucose units", math=r"\frac{10}{162} = 0.0617 \text{ mol}"),
               S("Lactic acid", math=r"2 \times 0.0617 \times 90.1 = 11.1 \text{ g per kg}"),
               S("Meaning", text="Real muscle stops at pH 5.5 to 5.7 because the enzymes of glycolysis are inhibited by the acidity, so not all the glycogen is used. A low pH also slows spoilage bacteria."),
           ]),
        KEY("Quality faults", "Link each to the cause and the pH.", cards=[
            ["Cold shortening", "Muscle chilled below about 10 °C before rigor sets in contracts strongly and is very tough. Prevented by controlling chilling rate or electrical stimulation."],
            ["Thaw rigor", "Muscle frozen before rigor contracts violently on thawing with high drip loss."],
            ["PSE (pale, soft, exudative)", "Mostly pigs: very rapid pH fall while the carcass is still warm denatures proteins; pale, watery, poor water holding."],
            ["DFD (dark, firm, dry)", "Animals stressed or exhausted before slaughter use up glycogen, so little lactic acid forms and pH stays high (above about 6.0). The meat is dark, sticky and spoils quickly because bacteria thrive at the higher pH."],
        ]),
        T("**Colour.** Fresh meat colour depends on myoglobin: purple-red when no oxygen is present, bright red **oxymyoglobin** when oxygen binds (bloom), and brown **metmyoglobin** "
          "when the iron is oxidised during storage. Cooking changes it to grey-brown."),
        H("Curing and smoking"),
        D("**Curing** is the treatment of meat with salt, nitrite (and sometimes nitrate), sugar and ascorbate. Nitrite is reduced to nitric oxide, which combines with myoglobin to give pink "
          "nitrosomyoglobin; on cooking this becomes stable pink nitrosohaemochrome (the colour of ham and bacon).", title="Curing"),
        KEY("What curing does", "Give four roles of nitrite.", cards=[
            ["Colour", "Stable pink colour after cooking."],
            ["Preservation", "Salt lowers water activity and nitrite inhibits Clostridium botulinum and other bacteria."],
            ["Flavour", "Gives the characteristic cured flavour."],
            ["Antioxidant", "Slows fat oxidation. Ascorbate speeds nitrite reduction and reduces the formation of nitrosamines, which are potentially carcinogenic, so the level of nitrite is restricted by law (check the current limit)."],
        ]),
        T("**Methods:** dry curing (rubbing with salt mix), brine curing (immersion) and injection of brine. **Smoking** deposits phenols, aldehydes and other compounds on the surface, "
          "which add flavour and colour, act as antimicrobials and antioxidants, and help to dry the product. Careful smoking avoids high levels of polycyclic aromatic hydrocarbons "
          "(PAHs), which are carcinogenic. Smoked and dried meat and fish are common across Cameroon; the kiln design and temperature control matter for both quality and safety."),
        EX("Worked example 2: nitrite in a cure",
           intro="A brine is injected to give 120 mg of sodium nitrite per kg of meat in 50 kg of meat. What mass of nitrite is needed? (Teaching figure; check the legal limit that applies.)",
           steps=[
               S("Total nitrite", math=r"120 \times 50 = 6000 \text{ mg} = 6.0 \text{ g}"),
               S("Meaning", text="Only a few grams are used for 50 kg of meat, so accurate weighing is critical for safety as well as quality."),
           ]),
        H("Milk and its composition"),
        KEY("Composition of cow's milk (approximate)", "Check the Food Composition Table for exact figures.", cards=[
            ["Water", "About 87%."],
            ["Fat", "About 3.5 to 4.5%, as tiny globules in an oil-in-water emulsion."],
            ["Protein", "About 3.3%: roughly 80% casein (curdled by acid or rennet) and 20% whey proteins (lactoglobulin and lactalbumin; remain soluble after acid or rennet coagulation, but denature with heat)."],
            ["Lactose", "About 4.6 to 4.8%: the milk sugar. Fermented to lactic acid by bacteria."],
            ["Minerals and vitamins", "About 0.7% ash, rich in calcium and phosphorus; vitamins A, B2 and B12."],
        ]),
        T("**Reception tests.** Milk arriving at a dairy is checked for temperature, smell, titratable acidity (about 0.14 to 0.16% as lactic acid in fresh milk), density (about 1.030 g per mL), the "
          "alcohol test (acid or heat-unstable milk curdles), fat and added water (from the freezing point). Fresh milk freezes at about -0.52 to -0.55 °C; added water raises the freezing point towards 0 °C."),
        EX("Worked example 3: added water",
           intro="Normal milk freezes at -0.520 °C. A sample freezes at -0.468 °C. Estimate the percentage of added water.",
           steps=[
               S("Rise in freezing point", math=r"0.520 - 0.468 = 0.052 \,{}^\circ\text{C}"),
               S("Fraction of added water", math=r"\frac{0.052}{0.520} = 0.10"),
               S("Answer", text="About 10% of the sample is added water."),
           ]),
        H("Dairy processing"),
        KEY("Operations", "Know the purpose of each.", cards=[
            ["Clarification and separation", "A centrifuge removes dirt and separates cream (high fat) from skim milk."],
            ["Standardisation", "Cream and skim milk are blended to give a standard fat content (for example 3.0% fat)."],
            ["Homogenisation", "Milk is forced through a narrow valve at high pressure to break fat globules into tiny ones, preventing a cream layer from forming and giving a richer body."],
            ["Heat treatment and packing", "Pasteurisation or UHT (see the earlier lesson), cooling, and packing."],
        ]),
        EX("Worked example 4: standardising milk fat (Pearson square)",
           intro="Whole milk contains 4.0% fat and skim milk 0.1% fat. In what proportions must they be mixed to give 3.0% fat? How much of each is needed for 1 000 kg?",
           steps=[
               S("Parts of whole milk", math=r"3.0 - 0.1 = 2.9"),
               S("Parts of skim milk", math=r"4.0 - 3.0 = 1.0"),
               S("Total parts and masses", math=r"2.9 + 1.0 = 3.9;\; \text{whole} = \frac{2.9}{3.9} \times 1000 = 743.6 \text{ kg};\; \text{skim} = 256.4 \text{ kg}"),
           ], check=r"0.7436 \times 4.0 + 0.2564 \times 0.1 = 3.0"),
        KEY("Dairy products", "Give the key change for each.", cards=[
            ["Butter", "Cream (about 35 to 40% fat) is pasteurised, ripened and churned. Churning breaks the fat globule membrane, so the oil-in-water emulsion inverts to a water-in-oil emulsion; buttermilk drains; the butter is washed, salted and worked to about 80% fat and 16% water."],
            ["Cheese", "Milk is coagulated by rennet (chymosin cuts a protein, kappa-casein, so casein micelles clump with calcium) and/or lactic acid (casein sets near pH 4.6). The curd is cut, heated, drained of whey, salted, pressed and ripened by enzymes and bacteria for flavour and texture."],
            ["Yoghurt", "Milk is heated to about 85 to 90 °C (denatures whey proteins for a firmer gel), cooled to 42 to 45 °C and inoculated with Streptococcus thermophilus and Lactobacillus delbrueckii subsp. bulgaricus. They ferment lactose to lactic acid until the pH reaches about 4.5 and the casein sets; then it is cooled."],
            ["Evaporated and condensed milk, milk powder", "Evaporated milk is concentrated and sterilised in cans; sweetened condensed milk is preserved by high sugar (low water activity); powder is made by spray drying."],
        ]),
        EX("Worked example 5: lactic acid in yoghurt",
           intro="Lactose (M = 342.3) is converted to 4 mol of lactic acid (M = 90.1) per mole: C12H22O11 + H2O gives 4 C3H6O3. Yoghurt reaches 9 g of lactic acid per litre from milk with 47 g of lactose per litre. What fraction of the lactose was used?",
           steps=[
               S("Moles of lactic acid", math=r"\frac{9}{90.1} = 0.0999 \text{ mol}"),
               S("Moles of lactose used", math=r"\frac{0.0999}{4} = 0.0250 \text{ mol} \Rightarrow 0.0250 \times 342.3 = 8.55 \text{ g}"),
               S("Fraction", math=r"\frac{8.55}{47} = 0.18 = 18\%"),
           ]),
        MISTAKE("Saying the pH of meat is lowered by an acid added at slaughter", "The pH falls because the muscle itself makes lactic acid from its glycogen. A stressed animal with low glycogen makes little acid, giving DFD meat."),
        MISTAKE("Saying churning adds fat to cream", "Churning does not add fat; it breaks the fat-globule membranes so the fat clumps and the emulsion changes from oil-in-water to water-in-oil."),
        QUIZ("Which condition produces dark, firm, dry (DFD) meat?",
             ["Very rapid pH fall while the carcass is warm", "Exhaustion of glycogen before slaughter, so the pH stays high", "Curing with nitrite", "Freezing before rigor"], 1,
             "Stressed animals with little glycogen make little lactic acid, so the pH stays above about 6.0.",
             hint="Where does the lactic acid come from?",
             feedback=["That describes PSE meat.", "", "Nitrite curing gives a pink colour, not DFD.", "That gives thaw rigor."]),
        QUIZ("Why does yoghurt set into a gel?",
             ["Rennet cuts kappa-casein", "Lactic acid lowers the pH to about 4.5, near the isoelectric point of casein", "The fat melts", "Lactose crystallises"], 1,
             "Lactic acid from lactose fermentation lowers pH until the casein micelles lose their charge and clump into a gel.",
             hint="Which acid is made by the starter cultures?",
             feedback=["That is the main mechanism for cheese.", "", "Fat has no part in gelation.", "Lactose is fermented, not crystallised."]),
        H("Practice"),
        PQ("Explain why meat is stiff 12 hours after slaughter but more tender after a week at 2 °C.", "After slaughter ATP is used up and actin and myosin form permanent actomyosin bonds: rigor mortis, which is complete in beef at 12 to 24 hours. During ageing, the muscle's own enzymes (calpains and cathepsins) gradually break down structural proteins, so rigor resolves and the meat becomes tender."),
        PQ("Describe the role of nitrite in curing bacon.", "Nitrite forms nitric oxide, which reacts with myoglobin to give the stable pink colour of cured meat after cooking; with salt it inhibits spoilage bacteria and Clostridium botulinum; it contributes cured flavour and slows fat oxidation. Ascorbate is added to help reduce nitrosamine formation, and the level is limited by law."),
        PQ("Calculate the masses of cream (40% fat) and skim milk (0.05% fat) obtained by separating 2 000 kg of milk containing 4% fat.", "Let c be the cream: 0.40 c + 0.0005 (2000 - c) = 0.04 x 2000. c = (80 - 1.0) / (0.40 - 0.0005) = 79.0 / 0.3995 = 197.7 kg. Skim = 2000 - 197.7 = 1802.3 kg."),
        PQ("Describe the manufacture of set yoghurt and explain why the milk is heated before the starter is added.", "Standardise and homogenise the milk, heat to 85 to 90 °C for 15 to 30 minutes, cool to 42 to 45 °C, inoculate with Streptococcus thermophilus and Lactobacillus bulgaricus, fill pots and incubate for several hours until pH about 4.5, then cool. Heating denatures the whey proteins, which bind to casein and give a firmer, smoother gel, and destroys competing microbes and gives the starter a clean start."),
        TIP("Exam link: meat and dairy appear in Paper 1 (rigor, curing, composition, products) and in Paper 2 essays on animal products. Paper 3 may include testing milk or cooking meat and dairy dishes: link scientific reasons (pH, protein coagulation) to what you see."),
        SUM("After slaughter glycogen forms lactic acid (pH 7.2 to about 5.5) and ATP falls, giving rigor mortis; enzymes later tenderise the meat during ageing.",
            "PSE, DFD, cold shortening and thaw rigor are faults caused by the speed of the pH fall, glycogen level and chilling.",
            "Curing uses salt, nitrite and ascorbate for colour, flavour and safety; smoking adds flavour and preservation.",
            "Milk is about 87% water, 4% fat, 3.3% protein (casein and whey), 4.7% lactose; processing includes separation, standardisation, homogenisation and heat treatment.",
            "Butter is a churned water-in-oil emulsion; cheese is rennet and acid curd; yoghurt is lactose fermented by two starter bacteria."),
    ],
))

# ------------------------------------------------------------------ 11. Beverages
LESSONS.append(lesson(
    module=M2,
    topic="Beverages",
    title="Beverage technology: cocoa, coffee, beer and fruit juices",
    slug="fsu1-beverages",
    minutes=25,
    summary="The science behind four beverage chains: cocoa bean fermentation and chocolate, coffee processing and roasting, malting and brewing of beer, and fruit juice extraction, clarification and preservation, with calculations of yield, alcohol and dilution.",
    objectives=[
        "Describe the fermentation, drying and processing of cocoa and explain what each stage achieves",
        "Compare dry and wet processing of coffee and explain the changes during roasting",
        "Describe malting, mashing, boiling, fermentation and maturation in brewing, and the role of the enzymes",
        "Describe the preparation and preservation of fruit juices and calculate yields, dilution and alcohol",
    ],
    key_concepts=["Cocoa fermentation", "Cocoa butter and tempering", "Dry and wet coffee processing", "Roasting and Maillard", "Malting", "Mashing and amylases", "Hops and wort boiling", "Ale and lager yeast", "Brix", "Pectinase and clarification"],
    blocks=[
        H("Introduction"),
        T("Cocoa from the Centre and South regions, coffee from the western highlands and the Littoral, beer on every town's menu, fruit juices from pineapple and orange: "
          "beverages are big business in Cameroon, which is one of the world's important cocoa producers and also grows robusta and arabica coffee. "
          "Flavour in each case is not simply picked from the plant; it is *made* by processing, and a small change in a step can change the quality and the price."),
        H("Cocoa"),
        T("A cocoa pod holds 30 to 40 seeds (beans) surrounded by sweet, white, sticky **pulp**. The raw bean is bitter, astringent and tastes nothing like chocolate. "
          "The flavour is made by **fermentation**, **drying** and **roasting**."),
        KEY("Fermentation (five to seven days in heaps under banana leaves or in boxes)", "Learn the sequence of microbes and what each does.", cards=[
            ["1 Yeasts (first day or two)", "The pulp sugars are fermented to ethanol under low oxygen; pectin breaks down and the pulp drains away as 'sweatings'."],
            ["2 Lactic acid bacteria", "Ferment sugars and citric acid to lactic acid."],
            ["3 Acetic acid bacteria (aerobic)", "As turning of the heap lets air in, they oxidise ethanol to acetic acid. This reaction is exothermic: the heap rises to about 45 to 50 °C."],
            ["4 Inside the bean", "Heat and acid kill the embryo; cell structures break down; polyphenols oxidise and bitterness falls; proteolysis produces amino acids and peptides and enzymes make reducing sugars, which are the precursors of chocolate flavour."],
        ]),
        T("**Drying** (sun drying on mats or raised trays for about a week, turning often) lowers the moisture from about 60% to about 7%. Too fast drying traps acetic acid; too slow "
          "allows mould and off-flavours; drying over smoky fires gives smoky beans. A **cut test** checks quality: well-fermented beans are brown inside with fissures, "
          "under-fermented beans are slaty (grey-purple) and mouldy beans are rejected."),
        KEY("From bean to chocolate", "Know the order and the key change.", cards=[
            ["Cleaning and roasting", "About 120 to 150 °C. Maillard reactions between the precursors form the true chocolate aroma; some acetic acid and water are lost."],
            ["Winnowing", "Shells are removed to leave the nibs."],
            ["Grinding", "Nibs are ground to cocoa liquor (cocoa mass); the heat of friction melts the cocoa butter (about 50% of the nib)."],
            ["Pressing", "Cocoa butter is pressed out, leaving cocoa cake which is milled to cocoa powder (sometimes alkalised to darken the colour)."],
            ["Chocolate", "Liquor, cocoa butter, sugar (and milk powder) are mixed, refined to fine particles, conched (heated and stirred for hours to remove acids and develop flavour) and tempered."],
        ]),
        T("**Tempering.** Cocoa butter can crystallise in several forms (polymorphs). Slow, controlled cooling and warming seeds the stable form (form V), which gives a glossy surface and a clean snap and "
          "melts just below body temperature. Untempered chocolate becomes dull and grey with fat bloom."),
        EX("Worked example 1: yield of dried cocoa",
           intro="100 kg of fermented wet beans at 60% moisture are dried to 7% moisture. How much dried cocoa is obtained? (Teaching figures.)",
           steps=[
               S("Dry matter", math=r"100 \times 0.40 = 40 \text{ kg}"),
               S("Mass at 7% moisture", math=r"\frac{40}{0.93} = 43.0 \text{ kg}"),
               S("Water lost", math=r"100 - 43.0 = 57.0 \text{ kg}"),
           ]),
        H("Coffee"),
        T("The coffee cherry has a skin, a sweet pulp, a slippery layer (mucilage), a thin paper-like parchment and the two beans (seeds). Robusta (*Coffea canephora*) is the main species of lowland Cameroon; arabica "
          "(*Coffea arabica*) grows at higher altitude. Robusta has about twice the caffeine (about 2 to 2.5%) of arabica (about 1.2%)."),
        KEY("Two ways to get green coffee", "Compare them.", cards=[
            ["Dry (natural) process", "Whole cherries are dried in the sun on mats or platforms for two to four weeks to about 11 or 12% moisture, then hulled to remove the dried husk and parchment. Simple, low water use; risk of mould and uneven quality. Common for robusta."],
            ["Wet (washed) process", "Cherries are pulped by machine, the beans are fermented for 12 to 36 hours to break down the mucilage, washed, then dried (as parchment coffee) to 10 to 12% moisture and hulled. Needs water; gives a cleaner, brighter cup; waste water must be treated. Common for arabica."],
        ]),
        T("**Roasting.** Green beans are heated to about 200 to 230 °C for 10 to 15 minutes. Water evaporates, the beans swell and turn brown through **Maillard reactions**, "
          "caramelisation and breakdown of chlorogenic acids. Hundreds of aroma compounds form, and carbon dioxide is trapped. A light roast keeps more acidity; a dark roast has more body "
          "and bitterness. Roasted beans lose about 12 to 20% of their mass. Ground coffee goes stale as the aroma escapes and the oils oxidise, so it is packed in oxygen-proof bags. "
          "**Instant coffee** is made by extracting roasted coffee with hot water and then spray-drying or freeze-drying the extract."),
        EX("Worked example 2: roast loss",
           intro="A roaster loses 15% of the mass of green coffee. (a) What mass of roasted coffee comes from 1 000 kg of green? (b) What mass of green is needed for 500 kg of roasted coffee?",
           steps=[
               S("(a) Roasted", math=r"1000 \times (1 - 0.15) = 850 \text{ kg}"),
               S("(b) Green needed", math=r"\frac{500}{0.85} = 588 \text{ kg}"),
           ]),
        H("Beer"),
        T("Beer is made from **malted** cereal, water, hops and yeast. Barley malt is classical; in warm countries, sorghum malt, maize, rice or cassava starch are often used "
          "as cheaper **adjuncts**. Traditional beers in Cameroon include sorghum beers of the north (such as bili-bili; check local names) and fermented palm sap (palm wine), "
          "but the same biochemistry applies."),
        KEY("Malting: making the enzymes", "Three steps.", cards=[
            ["Steeping", "Barley is soaked for one to two days until the moisture rises to about 42 to 46%."],
            ["Germination", "Five or six days at about 15 to 20 °C. The grain makes amylases (starch-splitting), proteases and cell-wall enzymes, which soften the endosperm. This is 'modification'."],
            ["Kilning", "Hot air dries the green malt to about 4% moisture, stopping growth and preserving the enzymes; the temperature of kilning sets the colour and flavour of the malt."],
        ]),
        KEY("Brewing and fermentation", "Learn the order and the purpose.", cards=[
            ["Milling and mashing", "Crushed malt (grist) is mixed with warm water. At about 63 to 72 °C the amylases convert starch to fermentable sugars (mainly maltose) and dextrins; proteases make amino acids for the yeast. The resulting liquid is the **wort**."],
            ["Lautering", "The sweet wort is filtered through the bed of husks (spent grain), which is used as animal feed."],
            ["Boiling with hops", "About an hour. It sterilises the wort, destroys the enzymes, coagulates proteins, concentrates it, and extracts the hop bitter acids (the alpha-acids are isomerised to bitter iso-alpha acids)."],
            ["Cooling and fermentation", "The wort is cooled and aerated and yeast is added. Ale yeast (Saccharomyces cerevisiae, top-fermenting) works at about 18 to 22 °C; lager yeast (Saccharomyces pastorianus, bottom-fermenting) at about 8 to 12 °C. Sugar becomes ethanol and CO2."],
            ["Maturation, filtration, packing", "Cold conditioning clarifies the beer and removes off-flavours; it is filtered, carbonated, and pasteurised or sterile filtered before bottling."],
        ]),
        EX("Worked example 3: water in steeping",
           intro="1 000 kg of barley at 12% moisture is steeped to 45% moisture. How much water does it take up?",
           steps=[
               S("Dry matter", math=r"1000 \times 0.88 = 880 \text{ kg}"),
               S("Mass at 45% moisture", math=r"\frac{880}{0.55} = 1600 \text{ kg}"),
               S("Water taken up", math=r"1600 - 1000 = 600 \text{ kg}"),
           ]),
        EX("Worked example 4: theoretical alcohol",
           intro="A wort has 100 g of fermentable sugar per litre. Using C6H12O6 giving 2 C2H5OH + 2 CO2, find the theoretical ethanol mass and the percentage by volume (ethanol density 0.789 g per mL), and the yield if the real efficiency is 90%.",
           steps=[
               S("Mass of ethanol from 180.2 g of glucose is 2 x 46.07 = 92.14 g", math=r"100 \times \frac{92.14}{180.16} = 51.1 \text{ g per litre}"),
               S("Volume of ethanol", math=r"\frac{51.1}{0.789} = 64.8 \text{ mL per litre} = 6.5\% \text{ v/v}"),
               S("At 90% efficiency", math=r"0.90 \times 6.5 = 5.8\% \text{ v/v}"),
               S("Mass of CO2", text="100 - 51.1 = 48.9 g of carbon dioxide per litre is released; this is why fermenters must be vented."),
           ]),
        H("Fruit juices"),
        T("Juice is made from sound, ripe fruit. Pineapple, orange, mango, passion fruit and guava are common in Cameroon. The main stages are:"),
        KEY("Juice processing", "Give a reason for each step.", cards=[
            ["Washing, sorting, grading", "Removes dirt, mould and unripe or damaged fruit."],
            ["Extraction", "Citrus by an extractor that avoids the bitter peel oil; pineapple and mango by crushing and pressing or pulping."],
            ["Straining and finishing", "Removes seeds, fibres and excess pulp."],
            ["Enzyme treatment", "Pectinase breaks down pectin, which lowers viscosity, raises the yield, and clarifies clear juices (apple, pineapple). Cloudy juices keep their cloud."],
            ["Deaeration", "Removes air so that vitamin C and colour are not oxidised and foaming is avoided."],
            ["Heat treatment and filling", "Acid juice (pH below 4) is pasteurised (about 85 to 95 °C for seconds) and filled hot or aseptically. This destroys spoilage yeasts and moulds and enzymes such as pectin methylesterase, which would make orange juice lose its cloud."],
            ["Concentration", "Evaporators or freezing concentrate the juice to about 60 to 65 °Brix, which saves transport and storage. It is reconstituted with water before drinking."],
        ]),
        D("**Degrees Brix** (°Brix) is the concentration of dissolved solids, as grams of sucrose per 100 g of solution, measured by a refractometer. The **Brix to acid ratio** is the total soluble solids divided by the titratable acidity (as citric acid) and shows how sweet or sharp a juice tastes.", title="°Brix"),
        EX("Worked example 5: reconstituting concentrate",
           intro="A juice concentrate has 60 °Brix. How much water must be added to 1 kg of concentrate to give a drink of 12 °Brix? An orange juice has 12 °Brix and 0.8% acid: what is its Brix to acid ratio?",
           steps=[
               S("Solids balance", math=r"60 \times 1 = 12 \times (1 + w)"),
               S("Solve", math=r"1 + w = 5 \Rightarrow w = 4 \text{ kg of water}"),
               S("Brix to acid ratio", math=r"\frac{12}{0.8} = 15"),
           ]),
        MISTAKE("Saying that cocoa flavour comes from the bean as it is picked", "The flavour precursors form during fermentation inside the bean, and the chocolate aroma forms during roasting. Underfermented beans are bitter and slaty, however carefully roasted."),
        MISTAKE("Confusing the roles of malt and hops", "Malt supplies the enzymes and the starch that becomes the fermentable sugar. Hops give bitterness, aroma and some preservation. Yeast makes the alcohol."),
        QUIZ("Which group of organisms causes the temperature of fermenting cocoa to rise?",
             ["Yeasts in the first hours", "Lactic acid bacteria", "Acetic acid bacteria oxidising ethanol", "Moulds"], 2,
             "Oxidation of ethanol to acetic acid by acetic acid bacteria is strongly exothermic and raises the heap to 45 to 50 °C.",
             hint="Which reaction needs air and gives out heat?",
             feedback=["Yeasts act first under low oxygen and make ethanol.", "Lactic acid bacteria make acid but contribute little heat.", "", "Moulds are a defect in cocoa, not part of the planned fermentation."]),
        QUIZ("In brewing, the main purpose of mashing is to",
             ["sterilise the wort", "convert starch to fermentable sugars using malt enzymes", "add bitterness from hops", "produce alcohol"], 1,
             "Malt amylases act in warm water to break starch into maltose and dextrins.",
             hint="Which enzymes are made during malting?",
             feedback=["Sterilisation is the job of wort boiling.", "", "Bitterness comes from hops during boiling.", "Alcohol is made by the yeast during fermentation."]),
        H("Practice"),
        PQ("Describe the roles of fermentation and drying in the production of cocoa beans.", "Fermentation (heap or box, five to seven days) breaks down the pulp, kills the embryo, and produces flavour precursors (amino acids, peptides, reducing sugars) and oxidises polyphenols so bitterness falls. Drying removes water to about 7% so the beans keep without mould and stops fermentation, with slow enough drying to let acetic acid escape."),
        PQ("Outline the steps in the production of beer, from malted barley to bottled beer.", "Milling malt, mashing (amylases make fermentable sugars), lautering to separate the wort from the spent grain, boiling with hops (sterilises, bitter acids, protein coagulation), cooling and aerating, fermenting with yeast (sugar to ethanol and CO2), maturing, filtering, carbonating, pasteurising or sterile filtering, and filling."),
        PQ("500 kg of dried coffee cherries give 270 kg of green coffee, which loses 14% of its mass in roasting. Calculate the roasted mass.", "Roasted mass = 270 x 0.86 = 232.2 kg."),
        PQ("Describe two differences between the dry and the wet processing of coffee.", "Dry process: whole cherries are sun-dried then hulled; low water use; more risk of mould and uneven quality; common for robusta. Wet process: cherries are pulped, fermented to remove mucilage and washed, then dried as parchment; needs plenty of water and treatment of waste water; gives a cleaner cup; common for arabica."),
        TIP("Exam link: beverages appear in Paper 1 (steps, definitions, enzymes) and Paper 2 essays on the processing of cocoa, coffee, beer and fruit juices (flow diagrams with reasons are rewarded). Add reasons for every stage and link them to the chemistry (Maillard, enzymes, fermentation)."),
        SUM("Cocoa: pulp fermentation by yeasts, lactic and acetic acid bacteria makes flavour precursors; drying to about 7% moisture; roasting forms the aroma; cocoa butter is tempered in chocolate.",
            "Coffee: dry or wet processing to green beans (10 to 12% moisture); roasting at 200 to 230 °C gives Maillard flavours and a 12 to 20% mass loss.",
            "Beer: malting makes the enzymes, mashing makes the sugars, boiling with hops adds bitterness, yeast ferments sugar to ethanol and CO2.",
            "Juices: extraction, straining, enzyme treatment, deaeration, pasteurisation and hot or aseptic filling; concentrates are diluted by a solids balance.",
            "Calculations rely on dry matter, solids balances and the equation for fermentation of glucose."),
    ],
))

# ------------------------------------------------------------------ 12. HACCP
LESSONS.append(lesson(
    module=M3,
    topic="HACCP",
    title="HACCP: the seven principles and building a plan",
    slug="fsu1-haccp",
    minutes=25,
    summary="Hazard Analysis and Critical Control Points is a preventive system for food safety. Learn the hazard types, the preliminary tasks and seven principles, build a CCP table for a product, and see why testing the end product alone is not enough.",
    objectives=[
        "Define HACCP, hazard, risk, control measure, CCP and critical limit",
        "Classify biological, chemical and physical hazards, and carry out a simple hazard analysis",
        "State the preliminary steps and seven principles in order and apply them to a product",
        "Explain why prevention at CCPs is better than end-product testing, using growth and sampling calculations",
    ],
    key_concepts=["Hazard and risk", "Biological, chemical and physical hazards", "Prerequisite programmes", "Flow diagram", "Critical control point", "Critical limit", "Monitoring", "Corrective action", "Verification and validation", "Records"],
    blocks=[
        H("Introduction"),
        T("In a canteen kitchen a pot of rice is cooked at midday and left on the counter until evening. By then bacterial toxins may have formed that reheating cannot destroy. "
          "Testing the finished rice would be too late, and no inspector can taste every portion. **HACCP** (Hazard Analysis and Critical Control Points) solves this "
          "by finding the few steps where something can go wrong and controlling them, every time, with measurements and records. It began in the 1960s in work on safe food for space "
          "missions, and is now the basis of food safety law and standards worldwide, including the Codex guidelines."),
        D("**HACCP** is a systematic, preventive approach to food safety. It identifies, evaluates and controls the **hazards** that are significant for the safety of food at "
          "each step of production, rather than relying on testing the finished product.", title="HACCP"),
        KEY("Key words", "Define each precisely in an answer.", cards=[
            ["Hazard", "A biological, chemical or physical agent in food, or a condition of food, that can cause harm to health."],
            ["Risk", "The likelihood of the hazard causing harm, combined with how severe the harm would be."],
            ["Control measure", "An action or activity that prevents or eliminates a hazard or reduces it to an acceptable level (cooking, chilling, filtering, washing, pH control)."],
            ["CCP (critical control point)", "A step at which control can be applied and is essential to prevent, eliminate or reduce a hazard to an acceptable level."],
            ["Critical limit", "A criterion (maximum or minimum value) that separates acceptable from unacceptable at a CCP: for example 72 °C for 15 seconds."],
        ]),
        H("Types of hazard"),
        KEY("Three groups", "Give at least two examples of each.", cards=[
            ["Biological", "Pathogenic bacteria (Salmonella, Listeria monocytogenes, E. coli O157, Clostridium botulinum, Staphylococcus aureus and its toxin), viruses (norovirus, hepatitis A), parasites, and moulds that make mycotoxins."],
            ["Chemical", "Pesticide and veterinary drug residues, aflatoxins, heavy metals, cleaning chemicals, unauthorised or excessive additives, natural toxins (cassava cyanide, histamine in spoiled fish) and **allergens** (groundnut, milk, egg, gluten, fish)."],
            ["Physical", "Glass, metal fragments, stones, bone, wood, plastic, jewellery."],
        ]),
        H("Before HACCP: prerequisite programmes"),
        T("HACCP works only on a base of good basic hygiene, called **prerequisite programmes (PRPs)**, also known as GMP or good hygiene practice: clean premises, safe water, "
          "personal hygiene, pest control, cleaning and disinfection, supplier control, maintenance and training (see the next lesson). A HACCP plan should deal with the "
          "specific hazards that these programmes cannot control by themselves."),
        H("The twelve steps: preparation and seven principles"),
        IMG("alfsu1-haccp-steps.svg", alt="The five preliminary tasks (team, product description, intended use, flow diagram, on-site confirmation) leading to the seven principles of HACCP",
            caption="Figure 1. The five preliminary tasks and seven principles of HACCP (Codex)."),
        KEY("Preliminary tasks", "These come first.", cards=[
            ["1 Assemble the HACCP team", "Staff who know the product and process (production, quality, maintenance, a food technologist), led by a trained person."],
            ["2 Describe the product", "Composition, pH, water activity, processing, packaging, shelf life and storage conditions."],
            ["3 Identify the intended use and consumers", "Eaten hot or cold, ready to eat, vulnerable groups (infants, elderly, pregnant women, people with weak immunity)."],
            ["4 Construct a flow diagram", "All steps from raw material to dispatch."],
            ["5 Confirm the flow diagram on site", "Walk the process, including night shifts and weekends, and correct the diagram."],
        ]),
        KEY("Seven principles", "Learn the order and the question each answers.", cards=[
            ["1 Conduct a hazard analysis", "What hazards are likely at each step, how severe, and what control measures exist?"],
            ["2 Determine the CCPs", "Which steps are essential for control (often with a decision tree)?"],
            ["3 Establish critical limits", "What value must be met at each CCP?"],
            ["4 Establish a monitoring system", "Who measures what, how and how often?"],
            ["5 Establish corrective actions", "What happens when a critical limit is not met?"],
            ["6 Establish verification procedures", "How do we confirm that the plan works and is followed?"],
            ["7 Establish documentation and records", "What evidence is kept?"],
        ]),
        T("**Finding CCPs.** A decision tree asks, for each hazard and step: Is there a control measure? Is the step designed to eliminate or reduce the hazard to an acceptable level? Could "
          "contamination occur or rise to an unacceptable level? Will a *later* step eliminate or reduce it? If a later step does, the earlier step is not a CCP. Versions of the tree differ; check your textbook."),
        EX("Worked example 1: scoring a hazard",
           intro="Rank two hazards in cooked chicken, using severity and likelihood each scored 1 (low) to 3 (high), risk = severity x likelihood: (a) Salmonella surviving undercooking: severity 3, likelihood 2 without control. (b) A bone fragment: severity 2, likelihood 1. Which is significant?",
           steps=[
               S("(a) Salmonella", math=r"3 \times 2 = 6"),
               S("(b) Bone", math=r"2 \times 1 = 2"),
               S("Decision", text="Salmonella has the higher score and needs a CCP (cooking). The bone fragment is controlled by prerequisite programmes (deboning checks, a sieve or X-ray) and a lower priority. The team sets the score at which a hazard is considered significant."),
           ]),
        EX("Worked example 2: a HACCP table for cooked chicken portions",
           intro="Flow diagram: receive chilled chicken, store at 4 °C, prepare, cook, cool, pack, store chilled, dispatch. Identify the CCPs and their limits. (Teaching limits: check the limits used where you work.)",
           steps=[
               S("Hazards at the steps", text="Receiving: pathogens and temperature abuse. Cooking: survival of Salmonella and Campylobacter. Cooling: growth of surviving spores and recontamination. Packing: foreign bodies."),
               S("CCP 1 Cooking", text="Critical limit: core temperature of at least 75 °C (a commonly taught limit). Monitoring: probe thermometer in the thickest portion of each batch. Corrective action: continue cooking, re-check; if time is lost, discard. Verification: calibration of probes weekly, record review, microbiological sampling."),
               S("CCP 2 Cooling", text="Critical limit: for example from 60 to 20 °C in a stated number of hours and then to 5 °C (check the limits that apply). Monitoring: time and temperature records. Corrective action: rapid chilling or discard."),
               S("Records", text="Temperature logs, calibration records, corrective action reports, supplier certificates: signed and dated."),
           ]),
        CODE("""Step         Hazard                 Control        CCP?  Critical limit        Monitoring             Corrective action
Receiving    Pathogens, temp abuse  Supplier spec  no    Delivery 5 C max     Probe on delivery      Reject load
Cooking      Salmonella survives    Heat           YES   Core 75 C            Probe, each batch      Re-cook, discard
Cooling      Spore growth           Fast chill     YES   60 to 5 C, set time  Time and temp log      Chill or discard
Packing      Glass, metal           Metal detector no    (PRP, inspection)    Test piece each shift  Re-inspect product""", "text", title="Table 1. Excerpt of a HACCP table for cooked chicken (teaching data)"),
        H("Monitoring, corrective action and verification"),
        KEY("Details examiners ask about", "Say who, how and what.", cards=[
            ["Monitoring", "Measurements or observations to show a CCP is in control: temperature, time, pH, flow rate, metal detector tests. Must be fast (no time for laboratory culture) and recorded, either continuous (a thermograph) or at planned intervals."],
            ["Corrective action", "Immediate: stop, isolate the product (hold), decide whether it can be reprocessed, used for another purpose or destroyed. Then find the cause, fix it, and record."],
            ["Verification", "Validation (is the plan scientifically capable of controlling the hazard?), calibration of instruments, review of records, internal audit, product testing, and external audits."],
            ["Records", "Show that the plan is followed: they are essential evidence and must be kept for a set period."],
        ]),
        H("Why prevention beats testing: two calculations"),
        EX("Worked example 3: growth in the temperature danger zone",
           intro="Bacteria on cooked rice double every 20 minutes at warm room temperature. The rice starts with 100 cells per gram. How many cells per gram after 2 h and after 4 h?",
           steps=[
               S("Number of doublings in 2 h", math=r"\frac{120}{20} = 6"),
               S("After 2 h", math=r"100 \times 2^6 = 6400 \text{ per gram}"),
               S("After 4 h", math=r"100 \times 2^{12} = 409\,600 \text{ per gram}"),
               S("Meaning", text="Time and temperature control are essential. The rule is to keep food either hot (above about 60 °C) or cold (below about 5 °C), and to avoid the zone between (check your national guidance for exact limits)."),
           ]),
        EX("Worked example 4: the limits of end-product testing",
           intro="10% of the units of a batch carry a pathogen. A laboratory tests n = 5 units chosen at random, and rejects the batch if any is positive. What is the chance of detecting the problem? How would it change with n = 20? With only 1% contaminated and n = 5?",
           steps=[
               S("Probability of a clean unit", math=r"1 - 0.10 = 0.90"),
               S("Detect with n = 5", math=r"1 - 0.90^5 = 1 - 0.590 = 0.41 \;(41\%)"),
               S("Detect with n = 20", math=r"1 - 0.90^{20} = 1 - 0.122 = 0.88 \;(88\%)"),
               S("1% contaminated, n = 5", math=r"1 - 0.99^5 = 0.049 \;(\text{about } 5\%)"),
               S("Meaning", text="Testing can miss most contamination when it is rare. This is why HACCP controls the process at the CCP, and uses testing to verify, not to ensure, safety."),
           ]),
        MISTAKE("Calling every step a CCP", "A plan with too many CCPs becomes impossible to monitor. A CCP is a step where control is essential and where there is no later step to remove the hazard. Many hazards are controlled by prerequisite programmes."),
        MISTAKE("Confusing verification with monitoring", "Monitoring is routine checking that the limit is met at the CCP, by the operator, in real time. Verification is a periodic check that the whole system works: calibration, records review, audits, testing."),
        QUIZ("Which of these is a critical limit?",
             ["The thermometer is checked every week", "A core temperature of at least 75 °C", "The cook records the temperature", "The cook is retrained"], 1,
             "A critical limit is a measurable value that separates acceptable from unacceptable: here, at least 75 °C.",
             hint="Look for a numerical criterion.",
             feedback=["This is a verification activity (calibration).", "", "This is monitoring (recording).", "This is a corrective action or training measure."]),
        QUIZ("A probe shows that a batch of chicken reached only 68 °C. What is the correct first corrective action?",
             ["Pack it, because 68 °C is close enough", "Hold the batch, continue cooking until the limit is met, then record", "Add more salt", "Test the product after packing"], 1,
             "Corrective action restores control and protects the consumer: the batch is held and re-cooked, then the event is recorded and the cause investigated.",
             hint="What must be done before the product goes any further?",
             feedback=["Close is not within the critical limit.", "", "Salt does not control Salmonella in cooked chicken.", "End-product testing cannot replace control."]),
        H("Practice"),
        PQ("Define a CCP and give an example from the production of pasteurised milk.", "A critical control point is a step at which control can be applied and is essential to prevent, eliminate or reduce a food safety hazard to an acceptable level. In pasteurised milk the heat treatment is a CCP, with a critical limit of at least 72 °C for 15 seconds, monitored by a recording thermograph and a flow diversion valve."),
        PQ("List the seven principles of HACCP in order.", "1 Conduct a hazard analysis. 2 Determine the critical control points. 3 Establish critical limits. 4 Establish a monitoring system. 5 Establish corrective actions. 6 Establish verification procedures. 7 Establish documentation and record keeping."),
        PQ("A product has 5% of units contaminated. A sample of 10 units is tested. Calculate the probability that at least one contaminated unit is found.", "P(none) = 0.95^10 = 0.599. P(at least one) = 1 - 0.599 = 0.401, about 40%. So a 10-unit sample would miss contamination about 60% of the time."),
        PQ("A small business makes smoked fish. Suggest three hazards and a CCP for the process.", "Hazards: biological (pathogens such as Listeria or Staphylococcus growing if the fish is warm or drying is slow; parasites), chemical (excessive polycyclic aromatic hydrocarbons from smoke; histamine in spoiled fish) and physical (bones, grit). CCP: the smoking and drying step, with critical limits for the temperature and time, or the final moisture content or water activity of the dried fish, monitored on each batch."),
        TIP("Exam link: HACCP appears in Paper 1 (principles, definitions, order of steps) and in Paper 2 essays on food safety and quality systems (give a table of step, hazard, CCP, limit, monitoring, corrective action). Use a specific product and give numerical critical limits where you are sure of them."),
        SUM("HACCP is a preventive system that controls hazards at critical control points instead of relying on end-product testing.",
            "Hazards are biological, chemical (including allergens) or physical; risk is likelihood combined with severity.",
            "Five preliminary tasks (team, product, intended use, flow diagram, on-site confirmation), then seven principles: hazard analysis, CCPs, critical limits, monitoring, corrective actions, verification, records.",
            "Prerequisite programmes (GMP) must be in place first; a step is a CCP only where control is essential and no later step removes the hazard.",
            "Bacterial growth is exponential and sampling often misses rare contamination, which is why time-temperature control and monitoring matter."),
    ],
))

# ------------------------------------------------------------------ 13. GMP and ISO 22000
LESSONS.append(lesson(
    module=M3,
    topic="GMP and ISO 22000",
    title="Good Manufacturing Practice and the ISO 22000 food safety management system",
    slug="fsu1-gmp-iso-22000",
    minutes=24,
    summary="GMP are the basic hygiene and manufacturing conditions every food business needs; ISO 22000 is the international standard that joins prerequisite programmes, HACCP and management. Learn the main GMP areas, cleaning and sanitising calculations, traceability and the structure of ISO 22000.",
    objectives=[
        "Describe the main areas of GMP and give the reason for each requirement",
        "Explain cleaning and sanitation, and calculate the dilution of a chlorine sanitiser",
        "Explain traceability and recall and the reconciliation of a batch",
        "Describe ISO 22000: purpose, structure, PRPs, OPRPs, CCPs, certification, and how it relates to HACCP and GMP",
    ],
    key_concepts=["GMP and good hygiene practice", "Premises and equipment", "Personal hygiene", "Cleaning and sanitising", "Pest control", "Traceability and recall", "ISO 22000", "Prerequisite and operational PRPs", "PDCA", "Certification"],
    blocks=[
        H("Introduction"),
        T("Two bakeries use the same recipe. One has a floor that is hard to clean, staff who wear their work clothes outside, and flour bins left uncovered. The other has smooth surfaces, "
          "hand-washing stations, labelled stores and written cleaning schedules. Both could have a HACCP plan on paper, but only the second can make it work. "
          "**Good Manufacturing Practice (GMP)** is that base of conditions and habits. **ISO 22000** is a standard that organises it all in one management system."),
        D("**GMP** (also called good hygiene practice, GHP, or prerequisite programmes) are the basic conditions and activities needed to keep a hygienic environment throughout the "
          "food chain and to make food that is safe and of consistent quality. In many countries GMP are written into law for food businesses.", title="GMP"),
        H("The main areas of GMP"),
        KEY("Premises and equipment", "Layout and surfaces are designed so that hygiene is easy.", cards=[
            ["Site and layout", "Away from pollution; flow from raw to finished product in one direction so raw and cooked foods do not cross; separation of high-risk and low-risk areas."],
            ["Buildings", "Smooth, impervious, easily cleaned walls and floors; sloped floors with drains; good lighting and ventilation; screened windows; doors that close."],
            ["Equipment", "Food-grade stainless steel or plastic; smooth, without crevices; designed so that it can be dismantled and cleaned; maintained and calibrated."],
        ]),
        KEY("People and materials", "Most contamination comes from people and raw materials.", cards=[
            ["Personal hygiene", "Hand washing with soap and clean water at the right times; clean protective clothing, hair covering and no jewellery; no work with diarrhoea, vomiting or infected wounds; training and a clear reporting rule."],
            ["Raw materials and suppliers", "Specifications; approved suppliers; inspection on receipt; temperature checks; rejection of damaged or out-of-date goods."],
            ["Water and ice", "Potable water for ingredients and cleaning, tested regularly; safe storage tanks."],
            ["Storage and transport", "Clean, dry, cool stores; first in, first out (FIFO) rotation; goods off the floor and away from walls; separate chemicals; temperature control in transport."],
        ]),
        KEY("Control of the environment", "Keep pests and dirt out and waste away.", cards=[
            ["Pest control", "Proofing of buildings, screens, bait stations and traps used safely, a regular inspection programme, and no food left out."],
            ["Waste", "Covered bins that are emptied often, waste areas away from production, drains kept clear."],
            ["Chemicals", "Cleaning chemicals and pesticides stored apart from food, labelled and used by trained staff."],
        ]),
        H("Cleaning and sanitation"),
        T("**Cleaning** removes soil (food, fat, dirt) with detergent. **Sanitising** (disinfecting) then reduces the surviving microbes to a safe level. Disinfecting a dirty surface does not work: "
          "organic matter uses up the sanitiser. The usual sequence is: remove loose soil, pre-rinse, wash with detergent, rinse, sanitise, final rinse (if needed) and dry."),
        KEY("Four factors in cleaning (Sinner's circle)", "A shortfall in one is made up by the others.", cards=[
            ["Chemical action", "Type and concentration of detergent or sanitiser."],
            ["Temperature", "Hot water melts fat and speeds reactions, within limits for the equipment and the product."],
            ["Mechanical action", "Scrubbing, spray pressure or turbulence."],
            ["Time", "The contact time needed for the chemical to act."],
        ]),
        T("Large equipment such as milk pipelines and tanks is cleaned in place (**CIP**) by pumping detergent and sanitiser through without dismantling. "
          "Chlorine-based sanitisers (such as sodium hypochlorite) are cheap and effective, but are used at the right concentration, are inactivated by organic matter, "
          "and are never mixed with acids or with other cleaning products."),
        EX("Worked example 1: diluting bleach",
           intro="A household bleach contains 5% sodium hypochlorite as available chlorine, which is 50 000 mg per litre (ppm). You need a sanitiser at 200 ppm. (a) What dilution is needed, and how many mL of bleach per litre of solution? (b) How many mL for a 20-litre tank? (Always follow the label and local guidance.)",
           steps=[
               S("(a) Dilution factor", math=r"\frac{50\,000}{200} = 250 \text{ (1 part bleach in 250 parts of solution)}"),
               S("mL per litre", math=r"\frac{1000}{250} = 4 \text{ mL per litre}"),
               S("(b) For 20 litres", math=r"4 \times 20 = 80 \text{ mL}"),
           ], check=r"\frac{80 \times 50\,000}{20\,000} = 200 \text{ ppm}"),
        H("Documentation, traceability and recall"),
        D("**Traceability** is the ability to follow a food and its ingredients through all stages of production and distribution: one step back (the supplier of each ingredient) and one step forward (the customer of each batch). "
          "It relies on batch or lot codes, records and labelling. A **recall** removes unsafe food that has already been distributed.", title="Traceability"),
        T("Good records include supplier details, batch codes of ingredients used in each batch, processing records, cleaning records, training records, calibration of instruments, "
          "customer complaints and a written recall procedure that is tested by a **mock recall**."),
        EX("Worked example 2: reconciling a batch in a mock recall",
           intro="A plant made 12 000 packs in lot 2310. It shipped 5 000 packs to distributor A, 4 000 to B and 2 000 to C, and 1 000 were still in the store. In a mock recall 8 700 packs are accounted for in the distributors' stores and the retail chain. What percentage of the shipped packs were traced? (Teaching data.)",
           steps=[
               S("Packs shipped", math=r"5000 + 4000 + 2000 = 11\,000"),
               S("Check the total", math=r"11\,000 + 1000 = 12\,000"),
               S("Percentage traced", math=r"\frac{8700}{11\,000} \times 100 = 79.1\%"),
               S("Meaning", text="79% is not enough in a real recall. Sound systems aim for close to 100%. Missing packs are traced through distributor records and retailers."),
           ]),
        H("ISO 22000"),
        D("**ISO 22000** is an international standard, published by the International Organization for Standardization, that sets out the requirements for a **food safety management "
          "system (FSMS)** for any organisation in the food chain, from farms and feed producers to manufacturers, transport, storage, retail and catering. The current edition is ISO 22000:2018 "
          "(it replaced the 2005 edition; check the current edition).", title="ISO 22000"),
        KEY("Key elements", "Four ideas bring it together.", cards=[
            ["Interactive communication", "Information is shared along the food chain: suppliers, customers, authorities, and inside the organisation."],
            ["System management", "Policy, objectives, responsibilities, resources, documented information, internal audits and management review. Top management must lead."],
            ["Prerequisite programmes (PRPs)", "The basic conditions and activities (the GMP above). Operational PRPs (OPRPs) are specific control measures for hazards identified in the analysis whose control is not through a CCP."],
            ["HACCP principles", "Hazard analysis, CCPs, critical limits, monitoring, corrective actions, verification and records, as in Codex."],
        ]),
        T("ISO 22000:2018 uses the common management system structure of ISO standards, with clauses 4 to 10: context of the organisation, leadership, planning, support, operation, performance evaluation and improvement. "
          "It uses the **Plan-Do-Check-Act (PDCA)** cycle at two levels: for the whole management system and, inside the 'Operation' clause, for the operational processes (the HACCP plan). "
          "Where a measurement shows that a control is not working, the system requires corrective action and improvement."),
        KEY("HACCP, GMP and ISO 22000 compared", "Learn the difference.", cards=[
            ["GMP", "The base hygiene conditions and practices."],
            ["HACCP", "A method for analysing hazards and controlling them at CCPs."],
            ["ISO 22000", "A management system that contains PRPs and HACCP and adds management commitment, communication, documentation, audit and continual improvement."],
        ]),
        T("**Certification.** An organisation can be audited against ISO 22000 by an independent certification body. ISO itself does not issue certificates. Schemes such as FSSC 22000 "
          "(which builds on ISO 22000 with specific PRP requirements) are recognised by the Global Food Safety Initiative and are demanded by many large buyers. "
          "Small businesses may find certification costly, but the same principles can be applied in a simpler form."),
        MISTAKE("Saying ISO 22000 replaces HACCP", "ISO 22000 includes the HACCP principles and the prerequisite programmes inside a wider management system. HACCP is one part of it."),
        MISTAKE("Sanitising before cleaning", "Dirt and fat protect microbes and use up the sanitiser. Always clean first, rinse, then sanitise."),
        QUIZ("Which element is NOT part of the ISO 22000 food safety management system?",
             ["Interactive communication", "Prerequisite programmes", "HACCP principles", "Guaranteed zero microbial counts in every product"], 3,
             "ISO 22000 requires a system to control hazards, not a guarantee of zero microbes; it does not make that promise.",
             hint="Which statement is a promise rather than a system requirement?",
             feedback=["It is one of the four key elements.", "PRPs are a key element.", "The HACCP principles are built in.", ""]),
        QUIZ("A cleaner sprays a sanitiser on a greasy bench and wipes it. What is wrong?",
             ["Nothing: the sanitiser removes grease", "The bench should have been cleaned with detergent and rinsed first", "Sanitisers should be mixed with detergents for greasy surfaces", "The sanitiser should be hotter than 100 °C"], 1,
             "Organic soil shields microbes and inactivates chlorine-based sanitisers, so surfaces must be cleaned and rinsed first.",
             hint="What is the correct order of cleaning steps?",
             feedback=["Sanitisers do not remove grease.", "", "Mixing products can release toxic gases and reduce the effect of the sanitiser.", "Hot sanitiser is neither practical nor necessary."]),
        H("Practice"),
        PQ("State five GMP requirements for a food processing plant, each with its purpose.", "Smooth, washable surfaces (easy to clean so no soil harbours microbes); one-way flow from raw to cooked areas (prevents cross-contamination); hand washing and clean protective clothing (stops workers spreading microbes); potable water (so that water does not contaminate food); pest control (keeps rodents and insects out); FIFO stock rotation (prevents spoilage of old stock); batch coding (traceability)."),
        PQ("A sanitiser at 100 ppm is made from a 5% bleach (50 000 ppm). How many mL of bleach are needed for 10 litres?", "Volume = 100 x 10 000 mL / 50 000 = 20 mL of bleach, made up to 10 litres with water."),
        PQ("Explain the difference between HACCP and ISO 22000.", "HACCP is a method for finding and controlling significant food safety hazards at critical control points. ISO 22000 is an international management system standard for food safety that includes the HACCP principles and prerequisite programmes, and adds management commitment, communication along the food chain, planning, internal audit, management review and continual improvement. An organisation can be certified to ISO 22000 by an independent body."),
        PQ("Explain what traceability means and why it is needed in a recall.", "Traceability is following a food and its ingredients one step back to the suppliers and one step forward to the customers using batch codes and records. In a recall it lets the company find exactly which batches are affected and where they went, so that only the unsafe products are withdrawn, quickly."),
        TIP("Exam link: GMP and quality systems appear in Paper 1 (definitions, ISO 22000 elements, order of cleaning) and in Paper 2 essays on food safety management. Give reasons for each GMP rule and link GMP to HACCP, ISO 22000 and legislation."),
        SUM("GMP are the base conditions for food safety: premises, equipment, personnel, raw materials, water, storage, pest control, waste, cleaning and records.",
            "Clean first, rinse, then sanitise; cleaning depends on chemical action, temperature, mechanical action and time; CIP is used for pipelines and tanks.",
            "Traceability (one step back, one step forward) with batch codes lets a recall find and withdraw affected product.",
            "ISO 22000 is a food safety management system standard (edition 2018) built on interactive communication, system management, PRPs and the HACCP principles; PDCA runs at two levels.",
            "Certification is by independent certification bodies; FSSC 22000 is a scheme built on ISO 22000."),
    ],
))

# ------------------------------------------------------------------ 14. Codex and Cameroonian food standards
LESSONS.append(lesson(
    module=M3,
    topic="Codex Alimentarius and Cameroonian food standards",
    title="Codex Alimentarius, food labelling and national food standards in Cameroon",
    slug="fsu1-codex-cameroon-standards",
    minutes=24,
    summary="Codex Alimentarius is the international reference for food standards, hygiene, additives, contaminants and labelling. Learn how it works, what a label must show, how energy and claims are calculated, and how ANOR and food control fit in Cameroon (check current rules).",
    objectives=[
        "Explain what Codex Alimentarius is, who runs it, what it contains and why it matters for trade and consumers",
        "Distinguish standards, codes of practice, guidelines and legal regulations",
        "List the mandatory items on a prepackaged food label and carry out label calculations (energy, claims, ingredient order)",
        "Describe in general terms how food standards and food control work in Cameroon and what to check in current rules",
    ],
    key_concepts=["Codex Alimentarius Commission", "FAO and WHO", "JECFA and MRLs", "Standard, code, guideline", "WTO SPS Agreement", "Food labelling", "Allergen declaration", "Nutrient content claims", "ANOR", "Food control agencies"],
    blocks=[
        H("Introduction"),
        T("A box of cocoa products leaving Douala for Europe, a bag of rice imported into Cameroon, and a packet of biscuits on a shop shelf are all covered by rules about what is safe, "
          "what may be added and what must be written on the label. Countries could each invent their own rules, but that would make trade slow and confusing. "
          "**Codex Alimentarius** (Latin for 'food code') is the shared international reference. National standards bodies such as Cameroon's **ANOR** use it as a model."),
        H("What Codex Alimentarius is"),
        D("**Codex Alimentarius** is a collection of internationally adopted food standards, guidelines and codes of practice. It is run by the **Codex Alimentarius Commission**, created in 1963 by the "
          "Food and Agriculture Organization (FAO) and the World Health Organization (WHO), with the aim of protecting consumers' health and ensuring fair practices in the food trade. "
          "The Codex secretariat is based at FAO in Rome. Membership is open to countries (and the European Union) that belong to FAO or WHO; most countries of the world take part.", title="Codex"),
        KEY("What Codex contains", "Learn at least four types.", cards=[
            ["Commodity standards", "What a named food (for example edible fats, fish, cereals, honey, fruit juices) must be like."],
            ["General standards", "Rules that apply to all foods: labelling of prepackaged foods, additives (the General Standard for Food Additives), contaminants and toxins, irradiation."],
            ["Codes of practice and hygiene", "The General Principles of Food Hygiene, with the HACCP system as an annex, and codes for particular products."],
            ["Limits and guidelines", "Maximum residue limits (MRLs) for pesticides and veterinary drugs, maximum levels for contaminants such as aflatoxins and heavy metals, and guidelines on nutrition labelling and claims."],
        ]),
        T("The numbers of the best-known texts are: General Standard for the Labelling of Prepackaged Foods (CXS 1-1985), General Principles of Food Hygiene (CXC 1-1969), General Standard for "
          "Food Additives (CXS 192-1995) and General Standard for Contaminants and Toxins in Food and Feed (CXS 193-1995). Check the current numbers and editions before quoting them in an answer."),
        KEY("How Codex works", "Science first, then agreement.", cards=[
            ["Scientific advice", "Independent expert bodies advise: JECFA (additives, contaminants, veterinary drugs), JMPR (pesticide residues) and JEMRA (microbiological risk)."],
            ["Committees", "Subject committees (hygiene, labelling, additives, contaminants, pesticide residues, nutrition) and regional coordinating committees, including one for Africa, where member countries discuss regional needs."],
            ["Decisions", "Standards are agreed by the Commission, normally by consensus, in steps that allow member comments."],
            ["Status", "Codex texts are recommendations. They are not laws, but countries often adopt them into their own regulations."],
        ]),
        D("The WTO Agreement on the Application of Sanitary and Phytosanitary Measures (the SPS Agreement) recognises Codex standards as the international reference for food safety in trade. "
          "A country that follows Codex can more easily defend its rules, and an exporter that meets Codex can more easily sell abroad. Importing countries or regions may set stricter rules, "
          "which exporters must also meet.", title="Codex and trade"),
        H("Standards, codes, guidelines and regulations"),
        KEY("Four different things", "Do not mix them.", cards=[
            ["Standard", "A document agreed by consensus that gives rules or specifications (for composition, quality, limits). Voluntary unless made compulsory by law."],
            ["Code of practice", "A set of recommended practices, for example for hygiene or handling of a product."],
            ["Guideline", "Advice on how to apply a rule or system."],
            ["Regulation (law, decree, order)", "A legal rule made by the State that must be obeyed and can be enforced, with inspection and penalties. A regulation may make a standard compulsory."],
        ]),
        H("Food labelling"),
        T("The Codex labelling standard gives the basic list for prepackaged food. Learn it as a checklist and add anything the national rules require."),
        KEY("Mandatory items on a prepackaged food label", "Check the current national requirements as well.", cards=[
            ["Name of the food", "True and specific name; special condition if needed (dried, smoked, irradiated)."],
            ["List of ingredients", "In **descending order of weight** at the time of manufacture, including additives by class name and name or number."],
            ["Net contents", "In metric units (g, kg, mL, L)."],
            ["Name and address", "Of the manufacturer, packer, distributor or importer."],
            ["Country of origin", "If omission would mislead."],
            ["Lot identification", "A batch code that allows traceability."],
            ["Date marking and storage", "Date of minimum durability ('best before') or 'use by', with storage instructions."],
            ["Allergens", "Declare foods known to cause hypersensitivity: cereals containing gluten, crustaceans, eggs, fish, peanuts, soybeans, milk, tree nuts, and sulphite at 10 mg per kg or more."],
        ]),
        T("**Nutrition labelling** normally gives energy, protein, available carbohydrate and fat, with sodium and any nutrient for which a claim is made. The **energy** is calculated with "
          "conversion factors: protein 17 kJ (4 kcal) per gram, available carbohydrate 17 kJ (4 kcal), fat 37 kJ (9 kcal), alcohol 29 kJ (7 kcal) and fibre 8 kJ (2 kcal)."),
        EX("Worked example 1: the energy value on a label",
           intro="A biscuit contains per 100 g: protein 10 g, fat 3 g, available carbohydrate 70 g. Calculate the energy in kJ and in kcal.",
           steps=[
               S("Energy in kJ", math=r"10 \times 17 + 3 \times 37 + 70 \times 17 = 170 + 111 + 1190 = 1471 \text{ kJ}"),
               S("Energy in kcal", math=r"10 \times 4 + 3 \times 9 + 70 \times 4 = 40 + 27 + 280 = 347 \text{ kcal}"),
               S("Check", text="1471 kJ divided by 4.184 is 351.6 kcal; the small difference arises from rounding of the conversion factors (17 kJ and 4 kcal)."),
           ]),
        EX("Worked example 2: can the product claim 'low fat'?",
           intro="A Codex guideline allows a 'low fat' claim for solid foods that have no more than 3 g of fat per 100 g, and 'low energy' if not more than 170 kJ (40 kcal) per 100 g. Biscuit A has 2.8 g of fat per 100 g. Biscuit B has 3.4 g. Biscuit A has 1471 kJ per 100 g. Which claims are allowed? (Check the current guideline and the national rule.)",
           steps=[
               S("Biscuit A: fat", math=r"2.8 \le 3.0 \Rightarrow \text{'low fat' allowed}"),
               S("Biscuit B: fat", math=r"3.4 > 3.0 \Rightarrow \text{not allowed}"),
               S("Low energy for A", math=r"1471 > 170 \Rightarrow \text{not 'low energy'}"),
               S("Lesson", text="A claim is allowed only when the criterion in the rule is met. A 'low fat' food can still be high in sugar and energy."),
           ]),
        EX("Worked example 3: the ingredient list",
           intro="A fruit drink is made from 700 g water, 200 g pineapple juice concentrate, 80 g sugar, 15 g citric acid and 5 g sodium benzoate. Write the list in the correct order.",
           steps=[
               S("Order by mass, largest first", text="Water (700 g), pineapple juice concentrate (200 g), sugar (80 g), citric acid (15 g), sodium benzoate (5 g)."),
               S("Additives", text="Citric acid is an acidity regulator and sodium benzoate is a preservative; they are declared with their function and name or number, for example 'preservative (E211)'."),
           ]),
        H("Contaminants and residue limits"),
        T("Codex sets **maximum levels** for contaminants (aflatoxins in peanuts, lead in some foods) and **MRLs** for pesticide and veterinary drug residues. They are decided from the "
          "toxicology (the ADI for the compound) and from typical diets. For total aflatoxins in peanuts intended for further processing the Codex maximum level is about 15 micrograms per kg; check the current text, because limits vary by product and many importing regions apply stricter limits. "
          "Exporters of groundnuts, cocoa and coffee must also meet the buyer's requirements."),
        EX("Worked example 4: checking an intake against the ADI",
           intro="A pesticide has an ADI of 0.01 mg per kg body weight per day. A 60 kg adult eats 0.3 kg of a vegetable per day with residue at 0.5 mg per kg. What fraction of the ADI is eaten? (Teaching figures, invented.)",
           steps=[
               S("Daily intake", math=r"0.3 \times 0.5 = 0.15 \text{ mg}"),
               S("Per kg of body weight", math=r"\frac{0.15}{60} = 0.0025 \text{ mg/kg}"),
               S("Fraction of the ADI", math=r"\frac{0.0025}{0.01} = 0.25 = 25\%"),
               S("Meaning", text="25% of the ADI from this one food. Regulators check several foods together, since the sum must stay below 100%."),
           ]),
        H("Food standards and food control in Cameroon"),
        T("Check the current rules for every point in this section. Names of ministries and agencies and their roles are reorganised from time to time."),
        KEY("What to know in general", "These points are widely stated; confirm with your textbook or the current official sources.", cards=[
            ["ANOR (Agence des Normes et de la Qualité)", "Cameroon's national standards and quality agency. It prepares and adopts national standards (often using Codex or ISO texts as a basis), takes part in international standardisation, and runs conformity assessment and certification activities. National standards carry the prefix NC (Norme Camerounaise)."],
            ["Ministries and services", "Several state bodies share food control: those responsible for public health, trade and consumer protection, livestock and fisheries (animal products and fish), agriculture (plant health and pesticides), and industry. Inspectors check premises, labels and products at markets, borders and factories."],
            ["Regional and international", "Cameroon takes part in regional African standardisation and in Codex and ISO work, and trades under the rules of its trading blocs and the WTO."],
            ["Labels and documents", "Bilingual labelling (French and English) and approved weights and measures are expected for packaged food in the national market; check the current rule. Exporters may need health, phytosanitary and quality certificates."],
        ]),
        MISTAKE("Saying Codex standards are laws that every country must obey", "Codex texts are recommendations. They become binding only when a country adopts them in its own regulations, though the WTO SPS Agreement makes them the reference for resolving trade disputes."),
        MISTAKE("Quoting a standard number or a limit from memory without a check", "Standards are revised. Say 'the Codex maximum level, currently about ...' and show the method, as the examiners value the reasoning and the units more than a remembered number."),
        QUIZ("Who created the Codex Alimentarius Commission, and what are its main aims?",
             ["The WTO and ISO, to set tariffs on food", "FAO and WHO, to protect consumer health and ensure fair practice in the food trade", "The European Union, to harmonise European food law", "ANOR, to certify Cameroonian foods"], 1,
             "FAO and WHO established the Commission in 1963 for consumer protection and fair trade.",
             hint="Which two UN agencies deal with food and health?",
             feedback=["Codex is not a tariff body, and ISO is separate.", "", "Codex is global, not European.", "ANOR is a national body that may use Codex texts."]),
        QUIZ("On a label, a list of ingredients must be in order of",
             ["alphabetical order", "descending order of weight at the time of manufacture", "ascending order of cost", "order of their E numbers"], 1,
             "The largest ingredient by weight is named first, so consumers can judge the composition.",
             hint="What does a consumer want to know first?",
             feedback=["Alphabetical order hides what the product is mostly made of.", "", "Cost is not used.", "E numbers do not set the order."]),
        H("Practice"),
        PQ("State the full name and the role of Codex Alimentarius, and say why it matters for exporters of cocoa and groundnuts.", "Codex Alimentarius (the Food Code) is a set of international food standards, guidelines and codes of practice created by the FAO/WHO Codex Alimentarius Commission (1963) to protect consumer health and ensure fair practice in the food trade. It matters for exporters because its maximum levels (for example for aflatoxins and pesticide residues) and hygiene codes are the international reference under the WTO SPS Agreement, and buyers expect products to meet them or stricter rules."),
        PQ("List six pieces of information that must appear on the label of a prepackaged food.", "Name of the food; list of ingredients in descending order of weight; net contents; name and address of manufacturer or packer; lot identification; date of minimum durability or use by and storage instructions; and allergen declaration (country of origin and instructions for use where needed)."),
        PQ("A yoghurt contains per 100 g: protein 4 g, fat 3 g, available carbohydrate 7 g. Calculate its energy in kJ using 17 kJ per g for protein and carbohydrate and 37 kJ per g for fat.", "Energy = 4 x 17 + 3 x 37 + 7 x 17 = 68 + 111 + 119 = 298 kJ per 100 g (about 71 kcal)."),
        PQ("Distinguish a food standard from a food regulation and explain how a standard can become binding.", "A standard is an agreed specification (composition, quality, limits) that is voluntary. A regulation is a legal rule made by the State, with inspection and penalties for breaking it. A standard becomes binding when a law or decree makes it compulsory, for example by referring to it or copying its requirements."),
        TIP("Exam link: Codex and national standards appear in Paper 1 (what Codex is, label contents, definitions) and in Paper 2 essays on food legislation and consumer protection. Where you are not sure of a current rule, say 'check the current rules' and describe the principle; use concrete examples."),
        SUM("Codex Alimentarius is the FAO/WHO set of international food standards, codes and guidelines (Commission founded 1963); texts are recommendations that countries may adopt.",
            "Codex includes commodity and general standards, hygiene codes with HACCP, MRLs, maximum levels for contaminants and guidelines on labelling and claims, with scientific advice from JECFA and JMPR.",
            "The WTO SPS Agreement recognises Codex as the international reference for food safety in trade.",
            "A label shows the name, ingredients in descending order of weight, net contents, maker, lot, date and storage, and allergens; energy uses 17, 37 and 17 kJ per gram of protein, fat and carbohydrate.",
            "In Cameroon, ANOR prepares national (NC) standards and several ministries share food control; check the current rules and responsibilities."),
    ],
))

