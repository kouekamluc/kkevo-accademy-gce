"""Form 5 Physics A: Measurement and the first part of Mechanics (16 lessons, one practice set each).

Course: Physics (O Level, 0580). Every numerical example uses g = 10 m/s^2 (g = 10 N/kg) unless a question says otherwise.
"""

from .dsl import *  # noqa: F403

COURSE = ("physics", "form-5")

M1 = "Measurement & Physical Quantities"
M2 = "Mechanics & Properties of Matter"
T_SI = "SI units"
T_MEAS = "Measuring length, mass, time and volume"
T_DEN = "Density and relative density"
T_VEC = "Scalars and vectors"
T_KIN = "Kinematics and motion graphs"
T_EQ = "Equations of uniformly accelerated motion"
T_NEW = "Newton's laws of motion and weight"
T_MOM = "Momentum and impulse"
T_MOMENTS = "Moments and centre of gravity"

LESSONS = []

# ------------------------------------------------------------------ 1. SI units
LESSONS.append(lesson(
    module=M1,
    topic=T_SI,
    title="SI base units, derived units and prefixes",
    slug="pha-si-base-and-derived-units",
    minutes=20,
    summary="Every physical quantity is a number and a unit. Learn the SI base units, how derived units such as the newton and the pascal are built from them, and how to change units with prefixes and standard form.",
    objectives=[
        "Name the SI base quantities and their units",
        "Define a derived unit and give the units of speed, force, pressure, energy and power",
        "Use the prefixes kilo, centi, milli, micro and mega to convert units",
        "Write numbers in standard form and convert cm3 to m3 and km/h to m/s",
    ],
    key_concepts=["Physical quantity", "SI unit", "Base unit", "Derived unit", "Prefix", "Standard form"],
    blocks=[
        H("Introduction"),
        T("At Mokolo market in Yaoundé a trader sells tomatoes by the kilogram. The buyer trusts the scale because a kilogram "
          "means the same thing in every market. Physics needs the same agreement for every measurement."),
        T("A measurement always has two parts: a **number** and a **unit**. The number 5 alone tells us nothing. "
          "5 kg, 5 m and 5 s are three different things."),
        D("A **physical quantity** is anything we can measure, such as length, mass, time or temperature. "
          "It is written as a number multiplied by a unit.", title="Definition: physical quantity"),
        D("The **SI** (Système International d'Unités, or International System of Units) is the set of units that scientists "
          "in nearly every country have agreed to use.", title="Definition: SI units"),
        H("Base quantities and base units"),
        T("A few quantities are chosen as the starting point. They are called **base quantities**. Their units are the "
          "**base units**. All other units are built from them."),
        CODE("""Base quantity        Unit        Symbol
length               metre       m
mass                 kilogram    kg
time                 second      s
electric current     ampere      A
temperature          kelvin      K""", "text", title="The base units you use most at O Level"),
        T("Two more base units exist: the **mole** (mol) for amount of substance, which you meet in Chemistry, and the "
          "**candela** (cd) for light intensity."),
        MISTAKE("Using the gram as the SI unit of mass", "The SI base unit of mass is the **kilogram** (kg), not the gram. "
                "When you put numbers into a formula such as $W = mg$, change grams to kilograms first."),
        H("Derived quantities and derived units"),
        D("A **derived unit** is a unit made by multiplying or dividing base units. A derived quantity is one whose unit is "
          "a derived unit. Some derived units have their own names.", title="Definition: derived unit"),
        CODE("""Quantity      Unit       Symbol   In other units
speed         metre per second   m/s
area          square metre       m2
volume        cubic metre        m3
density       kilogram per m3    kg/m3
force         newton             N        kg m/s2
pressure      pascal             Pa       N/m2
energy, work  joule              J        N m
power         watt               W        J/s
frequency     hertz              Hz       1/s""", "text", title="Common derived units"),
        EX("Worked example 1: base units of the newton and the pascal", intro="Write the newton and the pascal using only base units.", steps=[
            S("Use Newton's second law, force = mass × acceleration", math=r"F = ma"),
            S("Put in the base units of mass and acceleration", math=r"\text{N} = \text{kg} \times \text{m/s}^2 = \text{kg m/s}^2"),
            S("Pressure is force divided by area", math=r"p = \dfrac{F}{A}"),
            S("Divide the base units of the newton by m²", math=r"\text{Pa} = \dfrac{\text{kg m/s}^2}{\text{m}^2} = \text{kg m}^{-1}\,\text{s}^{-2}"),
        ]),
        H("Prefixes and standard form"),
        T("Some quantities are very big (the distance between towns) or very small (the thickness of a hair). A **prefix** "
          "placed before a unit multiplies it by a power of ten."),
        CODE("""Prefix   Symbol   Meaning             Factor
mega     M         one million         10^6
kilo     k         one thousand        10^3
centi    c         one hundredth       10^-2
milli    m         one thousandth      10^-3
micro    µ         one millionth       10^-6
nano     n         one billionth       10^-9""", "text", title="Prefixes"),
        D(r"**Standard form** writes a number as $a \times 10^n$, where $a$ is at least 1 and less than 10 and $n$ is a whole number. "
          r"For example $0.00045 = 4.5 \times 10^{-4}$ and $32\,000 = 3.2 \times 10^{4}$.", title="Definition: standard form"),
        EX("Worked example 2: change of units", intro="Convert (a) 2500 g to kg, (b) 350 cm to m, (c) 45 mm to m in standard form.", steps=[
            S("(a) 1 g = 10⁻³ kg", math=r"2500 \times 10^{-3} = 2.5 \ \text{kg}"),
            S("(b) 1 cm = 10⁻² m", math=r"350 \times 10^{-2} = 3.5 \ \text{m}"),
            S("(c) 1 mm = 10⁻³ m", math=r"45 \times 10^{-3} = 0.045 = 4.5 \times 10^{-2} \ \text{m}"),
        ]),
        EX("Worked example 3: area, volume and speed", intro="(a) Express 5 cm³ in m³. (b) Express 2.7 g/cm³ in kg/m³. (c) Express 72 km/h in m/s.", steps=[
            S("(a) Cube the length factor", math=r"1\ \text{cm}^3 = (10^{-2}\ \text{m})^3 = 10^{-6}\ \text{m}^3", text="A volume is length × length × length, so the factor is cubed."),
            S("Multiply by 5", math=r"5\ \text{cm}^3 = 5 \times 10^{-6}\ \text{m}^3"),
            S("(b) Change g to kg and cm³ to m³", math=r"2.7\ \dfrac{\text{g}}{\text{cm}^3} = 2.7 \times \dfrac{10^{-3}\ \text{kg}}{10^{-6}\ \text{m}^3} = 2.7 \times 10^{3} = 2700\ \text{kg/m}^3"),
            S("(c) 1 km = 1000 m and 1 h = 3600 s", math=r"72\ \text{km/h} = \dfrac{72 \times 1000}{3600} = 20\ \text{m/s}", text="To change km/h to m/s, divide by 3.6."),
        ]),
        MISTAKE("Changing cm³ to m³ by dividing by 100", r"Length changes by a factor of 100 from cm to m, but volume changes by $100^3 = 10^6$. "
                r"So $1\ \text{cm}^3 = 10^{-6}\ \text{m}^3$, and $1\ \text{cm}^2 = 10^{-4}\ \text{m}^2$."),
        MISTAKE("Leaving out the unit", "The Board's examiners keep reporting that candidates lose many marks for missing or wrong units. "
                "Write the unit on every answer, and make it match the quantity: m/s for speed, N for force, J for energy."),
        QUIZ("Which of these is NOT an SI base unit?", ["metre", "kilogram", "newton", "second"], 2,
             "The newton is a derived unit: 1 N = 1 kg m/s². The metre, kilogram and second are base units.",
             hint="A base unit cannot be written as a combination of other units.",
             feedback=["The metre is the base unit of length.", "The kilogram is the base unit of mass.", "", "The second is the base unit of time."]),
        QUIZ(r"The thickness of a wire is 0.45 mm. What is this in metres?",
             [r"$4.5 \times 10^{-4}$ m", r"$4.5 \times 10^{-2}$ m", r"$4.5 \times 10^{-5}$ m", r"$4.5 \times 10^{2}$ m"], 0,
             r"1 mm = $10^{-3}$ m, so $0.45 \times 10^{-3} = 4.5 \times 10^{-4}$ m.",
             hint="Multiply 0.45 by the factor for milli, then write the answer in standard form.",
             feedback=["", "This would be 0.045 m, which is 45 mm. You moved the decimal point the wrong way.", "That is 0.045 mm. Check the power of ten.", "This is a large number. Milli makes a quantity smaller, not bigger."]),
        TIP("SI units and conversions appear in Paper 1 multiple-choice questions (for example choosing the correct unit, or converting g/cm³ to kg/m³) "
            "and in every Paper 2 calculation, where the unit is part of the answer.", title="Exam link"),
        H("Practice questions"),
        PQ("Name the SI base unit of (a) length, (b) mass, (c) time. [3 marks]", "(a) the metre (m); (b) the kilogram (kg); (c) the second (s)."),
        PQ(r"Define the term 'derived unit' and write the unit of density in terms of base units. [2 marks]",
           r"A derived unit is made by multiplying or dividing base units. Density is mass ÷ volume, so its unit is kg/m³ (kg m⁻³)."),
        PQ(r"Change 3.6 km to metres and 450 g to kilograms. [2 marks]", r"3.6 km = 3.6 × 1000 = 3600 m. 450 g = 450 × 10⁻³ = 0.45 kg."),
        PQ(r"A taxi moves at 54 km/h. Express this speed in m/s. [2 marks]", r"54 × 1000 ÷ 3600 = 15 m/s (or 54 ÷ 3.6 = 15 m/s)."),
        SUM("A physical quantity is a number multiplied by a unit.",
            "The SI base units used most are the metre (m), kilogram (kg), second (s), ampere (A) and kelvin (K).",
            "A derived unit is built from base units: 1 N = 1 kg m/s², 1 Pa = 1 N/m², 1 J = 1 N m, 1 W = 1 J/s.",
            r"Prefixes change units by powers of ten: kilo $10^3$, centi $10^{-2}$, milli $10^{-3}$, micro $10^{-6}$.",
            r"Squares and cubes of length conversions are squared and cubed: $1\ \text{cm}^3 = 10^{-6}\ \text{m}^3$.",
            "Always write the unit with the number, and use SI units in formulae."),
    ],
))

# ------------------------------------------------------------------ 2. Length and time
LESSONS.append(lesson(
    module=M1,
    topic=T_MEAS,
    title="Measuring length and time",
    slug="pha-measuring-length-and-time",
    minutes=22,
    summary="Choose the right instrument for a length: metre rule, vernier callipers or micrometer screw gauge. Read the scales, correct a zero error, and time short events accurately by timing many oscillations.",
    objectives=[
        "Choose a suitable instrument to measure a given length",
        "Read a vernier scale and a micrometer screw gauge",
        "Explain and correct zero error and parallax error",
        "Find the period of a pendulum by timing many oscillations",
    ],
    key_concepts=["Metre rule", "Vernier callipers", "Micrometer screw gauge", "Zero error", "Parallax error", "Period"],
    blocks=[
        H("Introduction"),
        T("A tailor in Bamenda measures cloth with a tape. A carpenter measures a plank with a metre rule. "
          "A mechanic measures the thickness of a brake disc with a much finer tool. The size of the thing decides the instrument."),
        T("In this lesson you learn which instrument to use for which length, how to read each one, and how to avoid the "
          "two errors that students most often meet: **zero error** and **parallax error**."),
        H("Choosing the instrument"),
        CODE("""Instrument                 Smallest reading   Used for
metre rule                 1 mm (0.1 cm)      lengths of a few cm to 1 m
measuring tape             1 mm or 1 cm       long lengths, cloth, a room
vernier callipers          0.1 mm (0.01 cm)   diameter of a rod or a tube
micrometer screw gauge     0.01 mm            thickness of a wire or a sheet""", "text", title="Length instruments"),
        T("The smaller the smallest reading, the more **precise** the instrument. The right choice is the one whose smallest "
          "reading is small compared with the length you measure."),
        D("**Parallax error** is a wrong reading made when your eye is not directly in line with the mark on the scale. "
          "Look straight at the mark, with your eye above it.", title="Definition: parallax error"),
        D("**Zero error** is a reading shown by an instrument when it should read zero. It is **positive** if the reading is "
          "above zero and **negative** if it is below zero.", title="Definition: zero error", formula=r"\text{true reading} = \text{observed reading} - \text{zero error}"),
        H("The vernier callipers"),
        T("The vernier callipers has a fixed main scale in millimetres and a sliding **vernier scale** with 10 divisions. "
          "Those 10 divisions have the same length as 9 mm on the main scale, so each vernier division is 0.9 mm. "
          "That is how it reads to 0.1 mm."),
        KEY("How to read a vernier", "Use two readings and add them.", cards=[
            ["Step 1: main scale", "Read the whole millimetres just to the left of the vernier zero."],
            ["Step 2: vernier scale", "Find the vernier line that lines up exactly with a main-scale line. Multiply that line number by 0.1 mm."],
        ], note="Reading = main-scale reading + (aligned vernier line number × 0.1 mm)."),
        IMG("f5ph-a-vernier.svg", alt="A vernier scale with its zero just past 23 mm on the main scale and the fourth vernier line aligned with a main-scale line, giving 23.4 mm",
            caption="Figure 1. A vernier reading. The zero is just past 23 mm and vernier line 4 is aligned."),
        H("The micrometer screw gauge"),
        T("The micrometer measures small thicknesses very accurately. One full turn of the thimble moves the screw 0.5 mm. "
          "The thimble has 50 divisions, so each division is 0.5 ÷ 50 = 0.01 mm."),
        KEY("How to read a micrometer", "Again, two readings are added.", cards=[
            ["Sleeve", "Read the scale on the sleeve in whole and half millimetres, up to the edge of the thimble."],
            ["Thimble", "Read the thimble division that lines up with the line along the sleeve. Multiply it by 0.01 mm."],
        ], note="Always close the jaws gently with the ratchet. Over-tightening damages the screw and gives a wrong reading."),
        EX("Worked example 1: reading a micrometer with zero error", intro="A student measures a wire. The sleeve shows 5.5 mm and the thimble shows 28 divisions. With the jaws closed, the micrometer reads +0.02 mm. Find the true diameter.", steps=[
            S("Add the sleeve and thimble readings", math=r"5.5 + 28 \times 0.01 = 5.78\ \text{mm}"),
            S("Find the zero error", text="The jaws closed read +0.02 mm, so the zero error is +0.02 mm."),
            S("Subtract it from the observed reading", math=r"5.78 - 0.02 = 5.76\ \text{mm}"),
        ]),
        EX("Worked example 2: measuring something very thin", intro="50 sheets of paper make a pile 4.5 mm thick. Find the thickness of one sheet.", steps=[
            S("A single sheet is too thin to read, so measure many together", text="Measure the thickness of the pile with a ruler or callipers."),
            S("Divide by the number of sheets", math=r"\dfrac{4.5\ \text{mm}}{50} = 0.09\ \text{mm}"),
        ], check=r"0.09 \times 50 = 4.5\ \text{mm}"),
        H("Measuring time"),
        T("Time is measured in seconds with a stopwatch or a clock. The stopwatch may read to 0.01 s, but **you** start and "
          "stop it by hand, and your reaction time is about 0.2 s. This is the main error in a timing experiment."),
        D("The **period** $T$ of a pendulum is the time for one complete oscillation, that is, one swing out and back to the "
          "starting point. The **frequency** is the number of oscillations per second.", title="Definition: period",
          formula=r"T = \dfrac{\text{total time}}{\text{number of oscillations}}, \qquad f = \dfrac{1}{T}"),
        T("To reduce the effect of your reaction time, time **many** oscillations, for example 20, and divide. "
          "The error of 0.2 s is shared among 20 swings, so it matters much less."),
        EX("Worked example 3: timing a pendulum", intro="A student times 20 oscillations of a pendulum and gets 36.4 s. Find the period and the frequency.", steps=[
            S("Divide the total time by the number of oscillations", math=r"T = \dfrac{36.4}{20} = 1.82\ \text{s}"),
            S("Frequency is 1 divided by the period", math=r"f = \dfrac{1}{1.82} = 0.55\ \text{Hz}", text="Rounded to two significant figures."),
        ]),
        MISTAKE("Timing only one swing", "One oscillation is too short to time well. Time 20 oscillations and divide by 20. Start counting at zero as the bob passes the centre."),
        MISTAKE("Forgetting the zero error", "Check the instrument before you measure. If it reads +0.02 mm when closed, subtract 0.02 mm from every reading. If it reads −0.02 mm, add 0.02 mm."),
        QUIZ("Which instrument is best for measuring the diameter of a thin copper wire?",
             ["metre rule", "measuring tape", "vernier callipers", "micrometer screw gauge"], 3,
             "A thin wire needs the smallest reading, 0.01 mm. The micrometer is the most precise of the four.",
             hint="Choose the instrument with the smallest smallest-reading.",
             feedback=["A metre rule reads only to 1 mm, which is too coarse for a thin wire.", "A tape is for long lengths and reads to 1 mm or more.", "Callipers read to 0.1 mm. They are better than a rule but not as fine as the micrometer.", ""]),
        QUIZ("A micrometer reads +0.03 mm with the jaws closed. A wire reads 2.47 mm. What is the true diameter?",
             ["2.50 mm", "2.44 mm", "2.47 mm", "2.77 mm"], 1,
             "True reading = observed − zero error = 2.47 − 0.03 = 2.44 mm.",
             hint="The zero error is positive, so the instrument reads too high.",
             feedback=["You added the zero error. It is positive, so it must be taken away.", "", "You ignored the zero error.", "This is a decimal slip: 0.30 added instead of 0.03."]),
        TIP("Reading instruments and finding the period of a pendulum are common in Paper 2 practical-type questions and in Paper 1 multiple choice. "
            "Describing an experiment clearly (what you measure, what you repeat, what you divide by) earns marks.", title="Exam link"),
        H("Practice questions"),
        PQ("Why is it better to time 20 oscillations than 1 oscillation of a pendulum? [2 marks]",
           "Your reaction time in starting and stopping the watch gives an error of about 0.2 s. Over 20 oscillations this error is divided by 20, so the percentage error in the period is much smaller."),
        PQ("A pendulum makes 25 oscillations in 40 s. Find its period. [2 marks]", r"T = 40 ÷ 25 = 1.6 s."),
        PQ("A vernier callipers shows 17 mm on the main scale and the 6th vernier line is aligned. Give the reading in mm. [2 marks]", r"17 + 6 × 0.1 = 17.6 mm."),
        PQ("State two ways to avoid parallax error when reading a scale. [2 marks]", "Place your eye directly in front of the mark so that the line of sight is at right angles to the scale. Place the object touching the scale and read at the mark, not at an angle."),
        SUM("Choose the instrument by the size of the length: rule for cm, callipers for 0.1 mm, micrometer for 0.01 mm.",
            "Vernier reading = main scale + (aligned line × 0.1 mm). Micrometer reading = sleeve + (thimble divisions × 0.01 mm).",
            "True reading = observed reading − zero error.",
            "Avoid parallax error by looking straight at the mark.",
            "To time a short event, time many repeats and divide: T = total time ÷ number of oscillations.",
            "Measure many thin objects together (such as 50 sheets) and divide."),
    ],
))

# ------------------------------------------------------------------ 3. Mass and volume
LESSONS.append(lesson(
    module=M1,
    topic=T_MEAS,
    title="Measuring mass and volume",
    slug="pha-measuring-mass-and-volume",
    minutes=22,
    summary="Measure mass with a balance, and volume by a formula for regular solids, a measuring cylinder for liquids, and the displacement method for irregular solids. Know the difference between mass and weight.",
    objectives=[
        "Measure mass with a beam or electronic balance and state the units",
        "Find the volume of regular solids from their dimensions",
        "Measure the volume of a liquid and read the meniscus correctly",
        "Find the volume of an irregular solid by displacement",
    ],
    key_concepts=["Mass", "Balance", "Volume", "Measuring cylinder", "Meniscus", "Displacement method"],
    blocks=[
        H("Introduction"),
        T("At a filling station in Douala you buy petrol by the litre. At the market you buy rice by the kilogram. "
          "Litres measure **volume** and kilograms measure **mass**. This lesson shows how to measure both in a laboratory."),
        D("**Mass** is the amount of matter in an object. Its SI unit is the kilogram (kg). Mass does not change when the object moves to another place.", title="Definition: mass"),
        D("**Volume** is the amount of space an object occupies. Its SI unit is the cubic metre (m³). In the laboratory we use cm³ for small volumes.", title="Definition: volume"),
        H("Measuring mass"),
        T("Mass is measured with a **balance**. A beam balance compares the object with standard masses. "
          "An electronic balance shows the mass as a number. Before using an electronic balance, press the 'zero' (tare) button "
          "so that it reads 0.00 g when it is empty."),
        KEY("Mass and weight are different", "A spring balance does not measure mass. It measures the pull of gravity on the object, which is its **weight**, in newtons.", cards=[
            ["Mass", "Amount of matter. Unit: kg. Same everywhere. Measured with a balance."],
            ["Weight", "Force of gravity on the object. Unit: N. Changes with place. Measured with a spring balance."],
        ], note="You will study weight in the lesson on Newton's laws."),
        H("Volume of a regular solid"),
        T("If a solid has a regular shape, measure its dimensions and use a formula."),
        CODE("""Shape            Volume
cuboid           length x breadth x height
cube             side x side x side
cylinder         pi x radius^2 x height
sphere           (4/3) x pi x radius^3""", "text", title="Volume formulae"),
        EX("Worked example 1: volume of a cuboid and a cylinder", intro="(a) A block measures 5.0 cm by 4.0 cm by 3.0 cm. Find its volume. (b) A cylinder has radius 2.0 cm and height 10.0 cm. Find its volume.", steps=[
            S("(a) Multiply the three lengths", math=r"V = 5.0 \times 4.0 \times 3.0 = 60\ \text{cm}^3"),
            S("(b) Use the cylinder formula", math=r"V = \pi r^2 h = \pi \times 2.0^2 \times 10.0 = 126\ \text{cm}^3", text="Rounded to 3 significant figures."),
        ]),
        H("Volume of a liquid"),
        T("Liquids take the shape of their container, so we use a **measuring cylinder**. Stand it on a level table. "
          "The surface of water curves upwards at the glass. This curve is called the **meniscus**. "
          "Read the level at the **bottom of the meniscus**, with your eye at the same height."),
        T("One litre is 1000 cm³, so 1 mL = 1 cm³. Also 1 litre = 10⁻³ m³."),
        H("Volume of an irregular solid: displacement"),
        T("A stone or a key has no simple formula. Use **displacement**. When an object sinks in water, it pushes aside "
          "an equal volume of water. The water level rises by exactly the volume of the object."),
        KEY("Method", "Three steps with a measuring cylinder.", cards=[
            ["1. First level", "Half fill the cylinder with water and read the level $V_1$."],
            ["2. Lower the object", "Tie it to a thread and lower it gently until it is fully under the water. Read the new level $V_2$."],
            ["3. Subtract", "Volume of object = $V_2 - V_1$."],
        ], note="If the object is too big for the cylinder, use a displacement (eureka) can and collect the water that spills out. Measure the volume of the spilled water."),
        IMG("f5ph-a-cylinders.svg", alt="Two measuring cylinders. In the first the water level is at 36 cm cubed. In the second, with a stone in the water, the level is at 48 cm cubed.",
            caption="Figure 1. Finding the volume of a stone by displacement."),
        EX("Worked example 2: volume of a stone", intro="Use Figure 1 to find the volume of the stone.", steps=[
            S("Read the first level", text="The water is at 36 cm³."),
            S("Read the second level", text="With the stone, the water is at 48 cm³."),
            S("Subtract", math=r"V = 48 - 36 = 12\ \text{cm}^3"),
        ]),
        EX("Worked example 3: converting a volume of oil", intro="A shopkeeper in Bafoussam sells 2.5 litres of palm oil. Express this volume in cm³ and in m³.", steps=[
            S("Change litres to cm³", math=r"2.5\ \text{L} = 2.5 \times 1000 = 2500\ \text{cm}^3"),
            S("Change cm³ to m³", math=r"2500 \times 10^{-6} = 2.5 \times 10^{-3}\ \text{m}^3"),
        ]),
        MISTAKE("Reading the top of the meniscus", "Always read the bottom of the curved surface for water. Reading the top gives a volume that is too large."),
        MISTAKE("Using a floating object", "A piece of wax or cork floats, so displacement as above gives a wrong answer. Tie a heavy sinker to it so it is pushed fully under the water. Find the volume of the sinker alone first and subtract."),
        QUIZ("A stone is lowered into a measuring cylinder. The water level rises from 25 cm³ to 41 cm³. What is the volume of the stone?",
             ["16 cm³", "25 cm³", "41 cm³", "66 cm³"], 0,
             "The volume is the rise in level: 41 − 25 = 16 cm³.",
             hint="Volume of the object = new level − old level.",
             feedback=["", "This is the starting level. The stone's volume is the change.", "This is the final level, not the change.", "You added the two readings instead of subtracting."]),
        QUIZ("Which is a unit of mass?",
             ["newton", "kilogram", "cubic metre", "litre"], 1,
             "The kilogram is the SI unit of mass.",
             hint="Think about which unit you use when you buy rice.",
             feedback=["The newton is the unit of force and weight.", "", "The cubic metre is the unit of volume.", "The litre is a unit of volume."]),
        TIP("Methods of measuring volume, especially displacement, appear in Paper 1 and as part of the density questions in Paper 2. "
            "State the three steps clearly and say 'bottom of the meniscus'.", title="Exam link"),
        H("Practice questions"),
        PQ("Describe how to find the volume of a small stone using a measuring cylinder and water. [3 marks]",
           "Half fill the cylinder with water and read the level. Tie the stone to a thread and lower it gently until it is fully covered. Read the new level. The volume of the stone is the new level minus the first level."),
        PQ("A rectangular tank is 80 cm long, 50 cm wide and 40 cm deep. Find its volume in cm³ and in m³. [3 marks]",
           r"V = 80 × 50 × 40 = 160 000 cm³. In m³: 160 000 × 10⁻⁶ = 0.16 m³."),
        PQ("Why must you read a measuring cylinder with your eye level with the meniscus? [1 mark]", "To avoid parallax error. A reading from above or below gives a wrong value."),
        PQ("Write the SI units of mass and of volume. [2 marks]", "Mass: the kilogram (kg). Volume: the cubic metre (m³)."),
        SUM("Mass is the amount of matter in an object, in kg, measured with a balance.",
            "Volume is the space an object occupies. Its SI unit is m³; 1 cm³ = 10⁻⁶ m³ and 1 litre = 1000 cm³.",
            "Find the volume of a regular solid from its dimensions: cuboid l × b × h, cylinder πr²h.",
            "Measure liquid volume with a measuring cylinder. Read the bottom of the meniscus with your eye level with it.",
            "For an irregular solid use displacement: volume = new level − first level.",
            "A spring balance measures weight in newtons, not mass."),
    ],
))

# ------------------------------------------------------------------ 4. Density
LESSONS.append(lesson(
    module=M1,
    topic=T_DEN,
    title="Density and relative density",
    slug="pha-density-and-relative-density",
    minutes=24,
    summary="Density is mass per unit volume. Learn to calculate it, change between g/cm3 and kg/m3, find the density of solids and liquids in the laboratory, and define and use relative density.",
    objectives=[
        "Define density and use density = mass ÷ volume",
        "Convert between g/cm³ and kg/m³",
        "Describe how to find the density of a regular solid, an irregular solid and a liquid",
        "Define relative density and use it with a density bottle",
    ],
    key_concepts=["Density", "kg/m³", "g/cm³", "Relative density", "Density bottle", "Floating and sinking"],
    blocks=[
        H("Introduction"),
        T("Palm oil poured into water floats on top. A stone dropped into the same water sinks. Both fall under gravity, "
          "yet one stays on top and the other goes to the bottom. The reason is **density**."),
        D("The **density** of a substance is its mass per unit volume.", title="Definition: density",
          formula=r"\rho = \dfrac{m}{V}"),
        T(r"Here $\rho$ (the Greek letter rho) is the density, $m$ is the mass and $V$ is the volume. "
          r"The SI unit is **kg/m³**. In the laboratory we often use **g/cm³**."),
        KEY("Changing the unit", r"$1\ \text{g/cm}^3 = 1000\ \text{kg/m}^3$. Multiply g/cm³ by 1000 to get kg/m³.", cards=[
            ["Water", r"1 g/cm³ = 1000 kg/m³"],
            ["Aluminium", r"2.7 g/cm³ = 2700 kg/m³ (about)"],
            ["Iron", r"7.8 g/cm³ = 7800 kg/m³ (about)"],
        ], note="Density values in textbooks differ a little. Use the figures given in the question."),
        F(r"m = \rho V \qquad V = \dfrac{m}{\rho}", title="Rearranged"),
        H("Calculating density"),
        EX("Worked example 1: density of a stone", intro="A stone has mass 30 g. Its volume, found by displacement, is 12 cm³. Find its density in g/cm³ and in kg/m³.", steps=[
            S("Write the formula", math=r"\rho = \dfrac{m}{V}"),
            S("Substitute", math=r"\rho = \dfrac{30}{12} = 2.5\ \text{g/cm}^3"),
            S("Change to kg/m³", math=r"2.5 \times 1000 = 2500\ \text{kg/m}^3"),
        ], check=r"2.5 \times 12 = 30\ \text{g}"),
        EX("Worked example 2: mass from density", intro="The density of cooking oil is 920 kg/m³. Find the mass of 5 litres.", steps=[
            S("Change the volume to m³", math=r"5\ \text{L} = 5 \times 10^{-3}\ \text{m}^3"),
            S("Use m = ρV", math=r"m = 920 \times 5 \times 10^{-3} = 4.6\ \text{kg}"),
        ]),
        EX("Worked example 3: volume from density", intro="A piece of aluminium has mass 8.1 kg. The density of aluminium is 2700 kg/m³. Find its volume in m³ and in cm³.", steps=[
            S("Use V = m ÷ ρ", math=r"V = \dfrac{8.1}{2700} = 3.0 \times 10^{-3}\ \text{m}^3"),
            S("Change to cm³", math=r"3.0 \times 10^{-3} \times 10^{6} = 3000\ \text{cm}^3"),
        ]),
        H("Floating and sinking"),
        T("If a solid is **less dense** than water, it floats. If it is **more dense**, it sinks. Palm oil (about 900 kg/m³) floats "
          "on water (1000 kg/m³). A stone (2500 kg/m³) sinks. You will study this properly in the lesson on upthrust."),
        H("Relative density"),
        D("The **relative density** of a substance is the density of the substance divided by the density of water. "
          "It can also be written as the mass of a certain volume of the substance divided by the mass of an equal volume of water. "
          "It has **no unit**.", title="Definition: relative density",
          formula=r"\text{relative density} = \dfrac{\text{density of substance}}{\text{density of water}}"),
        T("Water has density 1000 kg/m³ (or 1 g/cm³). So the relative density of a substance is the same number as its density "
          "in g/cm³. The stone in example 1 has relative density 2.5."),
        H("Experiments"),
        KEY("Finding density", "Always measure a mass and a volume.", cards=[
            ["Regular solid", "Weigh it on a balance. Measure its sides and find the volume by formula. Divide."],
            ["Irregular solid", "Weigh it. Find the volume by displacement in a measuring cylinder. Divide."],
            ["Liquid", "Weigh an empty measuring cylinder. Pour in a known volume of liquid and weigh again. The mass of the liquid is the difference."],
        ]),
        T("A **density bottle** has a stopper and holds exactly the same volume each time it is filled. It is used to find the "
          "relative density of a liquid."),
        EX("Worked example 4: relative density with a density bottle", intro="A density bottle has mass 20 g when empty. Full of water its mass is 70 g. Full of a liquid its mass is 60 g. Find the relative density of the liquid and its density.", steps=[
            S("Mass of water", math=r"70 - 20 = 50\ \text{g}"),
            S("Mass of the same volume of liquid", math=r"60 - 20 = 40\ \text{g}"),
            S("Relative density", math=r"\dfrac{40}{50} = 0.8"),
            S("Density of the liquid", math=r"0.8 \times 1000 = 800\ \text{kg/m}^3"),
        ]),
        MISTAKE("Mixing units", "Do not put grams and m³ together. Use g with cm³ (answer in g/cm³) or kg with m³ (answer in kg/m³)."),
        MISTAKE("Giving relative density a unit", "Relative density is a ratio of two densities, so the units cancel. Write 2.5, not 2.5 g/cm³."),
        QUIZ("A block has mass 200 g and volume 80 cm³. What is its density?",
             ["0.4 g/cm³", "2.5 g/cm³", "16 000 g/cm³", "120 g/cm³"], 1,
             "ρ = m/V = 200 ÷ 80 = 2.5 g/cm³.",
             hint="Mass on top, volume at the bottom.",
             feedback=["You divided volume by mass. Density is mass ÷ volume.", "", "You multiplied mass and volume.", "You subtracted instead of dividing."]),
        QUIZ("The density of a liquid is 800 kg/m³. What is its relative density?",
             ["0.8", "800", "0.0008", "1.25"], 0,
             "Relative density = 800 ÷ 1000 = 0.8. It has no unit.",
             hint="Divide by the density of water, 1000 kg/m³.",
             feedback=["", "This is the density, not the relative density.", "You divided by 10⁶ instead of by 1000.", "You divided 1000 by 800, the wrong way round."]),
        TIP("Density is one of the most calculated quantities in Paper 1 and Paper 2. Always give a unit with density (kg/m³ or g/cm³) and none with relative density. "
            "Describing how to find the density of an irregular solid is a favourite experiment question.", title="Exam link"),
        H("Practice questions"),
        PQ("Define density and state its SI unit. [2 marks]", "Density is the mass per unit volume of a substance. Its SI unit is the kilogram per cubic metre (kg/m³)."),
        PQ("A metal block measures 10 cm by 5 cm by 4 cm and has mass 1560 g. Find its density in g/cm³ and kg/m³. [3 marks]",
           r"V = 10 × 5 × 4 = 200 cm³. ρ = 1560 ÷ 200 = 7.8 g/cm³ = 7800 kg/m³."),
        PQ("The density of mercury is 13 600 kg/m³. Find the mass of 0.002 m³ of mercury. [2 marks]", r"m = ρV = 13 600 × 0.002 = 27.2 kg."),
        PQ("Define relative density. Why does it have no unit? [2 marks]", "It is the density of a substance divided by the density of water. It is a ratio of two quantities with the same unit, so the units cancel."),
        SUM("Density = mass ÷ volume, $\\rho = m/V$. The SI unit is kg/m³.",
            "1 g/cm³ = 1000 kg/m³. Water has density 1000 kg/m³ (1 g/cm³).",
            "To find a density, measure a mass and a volume: formula for regular solids, displacement for irregular solids, a measuring cylinder or density bottle for liquids.",
            "Relative density = density of substance ÷ density of water. It has no unit.",
            "A substance less dense than water floats on it; a denser one sinks."),
    ],
))

# ------------------------------------------------------------------ 5. Scalars, vectors, adding
LESSONS.append(lesson(
    module=M1,
    topic=T_VEC,
    title="Scalars, vectors and adding vectors",
    slug="pha-scalars-vectors-and-adding",
    minutes=24,
    summary="Some quantities have size only (scalars), others have size and direction (vectors). Learn to tell them apart and to add vectors in a straight line, at right angles by Pythagoras, and by scale drawing.",
    objectives=[
        "Define scalar and vector quantities and classify common quantities",
        "Distinguish distance from displacement and speed from velocity",
        "Add vectors acting in the same line",
        "Find the resultant of two perpendicular vectors by calculation and by scale drawing",
    ],
    key_concepts=["Scalar", "Vector", "Displacement", "Resultant", "Pythagoras", "Scale drawing"],
    blocks=[
        H("Introduction"),
        T("Suppose you ask a taxi driver in Bafoussam, 'How far is the market?' He says, '2 km.' You still do not know where to go. "
          "You need a direction too: '2 km north.' Some quantities need a number and a unit only. Others need a direction as well."),
        D("A **scalar** quantity has **size (magnitude) only**. Examples: mass, time, distance, speed, energy, temperature, volume.", title="Definition: scalar"),
        D("A **vector** quantity has **size and direction**. Examples: displacement, velocity, acceleration, force, weight, momentum.", title="Definition: vector"),
        CODE("""Scalar                 Vector
distance               displacement
speed                  velocity
mass                   weight (a force)
energy                 force
time                   acceleration""", "text", title="Pairs to remember"),
        T("**Distance** is how far you travel along your path. **Displacement** is how far you are from the start, in a straight line, "
          "and in what direction. A runner who completes one lap of a 400 m track has travelled 400 m, but her displacement is 0 m."),
        H("Showing a vector"),
        T("A vector is drawn as an **arrow**. The length of the arrow shows the size, using a scale such as 1 cm for 10 N. "
          "The arrowhead shows the direction."),
        D("The **resultant** of two or more vectors is the single vector that has the same effect as all of them together.", title="Definition: resultant"),
        H("Adding vectors in the same line"),
        T("Vectors along the same line are added with a **sign**. Choose one direction as positive."),
        KEY("Same line", "Same direction: add. Opposite directions: subtract (and give the direction of the larger).", cards=[
            ["Same direction", "120 N and 80 N pull a cart forward: resultant = 120 + 80 = 200 N forward."],
            ["Opposite directions", "120 N forward and 80 N backward: resultant = 120 − 80 = 40 N forward."],
        ]),
        H("Adding vectors at right angles"),
        T("Place the vectors **tip to tail**: draw the first, then start the second where the first ends. The resultant joins the "
          "start of the first to the end of the second. When the two vectors are at 90°, the three vectors make a right-angled triangle."),
        F(r"R = \sqrt{a^2 + b^2} \qquad \tan\theta = \dfrac{b}{a}", title="Resultant of two perpendicular vectors"),
        IMG("f5ph-a-vec-add.svg", alt="A walker goes 40 m east then 30 m north. The two vectors are drawn tip to tail and the resultant is 50 m at 37 degrees north of east.",
            caption="Figure 1. Adding 40 m east and 30 m north. The resultant is 50 m."),
        EX("Worked example 1: a walk", intro="A boy walks 40 m east and then 30 m north. Find (a) the distance he walks, (b) his displacement from the start.", steps=[
            S("(a) Distance is the total path", math=r"40 + 30 = 70\ \text{m}"),
            S("(b) Magnitude of the displacement", math=r"R = \sqrt{40^2 + 30^2} = \sqrt{2500} = 50\ \text{m}"),
            S("Direction", math=r"\tan\theta = \dfrac{30}{40} = 0.75 \Rightarrow \theta = 36.9^\circ", text="The displacement is 50 m, 36.9° north of east."),
        ], check=r"50^2 = 2500 = 40^2 + 30^2"),
        EX("Worked example 2: a boat crossing a river", intro="A boat points straight across a river and moves at 4 m/s through the water. The river flows at 3 m/s downstream. Find the speed of the boat relative to the bank.", steps=[
            S("The two velocities are at right angles", text="Across: 4 m/s. Downstream: 3 m/s."),
            S("Use Pythagoras", math=r"v = \sqrt{4^2 + 3^2} = \sqrt{25} = 5\ \text{m/s}"),
            S("Direction", math=r"\tan\theta = \dfrac{3}{4} \Rightarrow \theta = 36.9^\circ", text="The boat is carried 36.9° downstream of the straight-across line."),
        ]),
        H("Adding vectors by scale drawing"),
        T("When the vectors are not at 90°, an O Level answer uses a scale drawing. Choose a scale, draw the vectors tip to tail "
          "with a ruler and protractor, measure the resultant and change it back with the scale."),
        EX("Worked example 3: scale drawing", intro="Two forces of 6 N and 8 N act on a point, with 60° between them. Find the resultant using the parallelogram method with a scale of 1 cm to 2 N.", steps=[
            S("Choose the scale", text="6 N becomes 3 cm. 8 N becomes 4 cm."),
            S("Draw the two lines from one point", text="Draw both lines starting at the point with 60° between them."),
            S("Complete the parallelogram", text="Draw a line from the end of each vector parallel to the other. The diagonal from the point is the resultant."),
            S("Measure the diagonal", math=r"\text{about } 6.1\ \text{cm} \Rightarrow 6.1 \times 2 = 12.2\ \text{N}", text="Calculation with the cosine rule gives 12.2 N. Your drawing may differ by a little."),
        ]),
        MISTAKE("Adding sizes of vectors at an angle", "5 N and 5 N at right angles do **not** make 10 N. They make $\\sqrt{50} = 7.1$ N. You may add the sizes only when the vectors point the same way."),
        MISTAKE("Forgetting the direction", "A vector answer needs a size **and** a direction. Write '50 m, 37° north of east', or give an angle on a diagram."),
        QUIZ("Which of these is a vector quantity?", ["Mass", "Speed", "Time", "Force"], 3,
             "A force has size and direction. Mass, speed and time have size only.",
             hint="Ask: do I need a direction to describe it completely?",
             feedback=["Mass has size only (kg).", "Speed has size only. Velocity is the vector.", "Time has size only.", ""]),
        QUIZ("Two forces of 9 N and 12 N act at right angles. What is the size of the resultant?",
             ["3 N", "21 N", "15 N", "225 N"], 2,
             r"R = $\sqrt{9^2 + 12^2} = \sqrt{225}$ = 15 N.",
             hint="Use Pythagoras; do not simply add.",
             feedback=["You subtracted. That works only for forces in opposite directions on the same line.", "You added. That works only for forces in the same direction.", "", "You forgot to take the square root."]),
        TIP("Scalars and vectors, and the resultant of two perpendicular forces, are common Paper 1 topics. In Paper 2 you may be asked to find a resultant by "
            "calculation or by scale drawing. State the scale and give the direction.", title="Exam link"),
        H("Practice questions"),
        PQ("Define a vector quantity and give two examples. [3 marks]", "A vector quantity has both size and direction. Examples: force and velocity (also displacement, acceleration and weight)."),
        PQ("A runner completes a full 400 m lap and returns to the start. State her distance and her displacement. [2 marks]", "Distance = 400 m. Displacement = 0 m, because she finishes where she started."),
        PQ("Find the resultant of a 16 N force acting east and a 12 N force acting north. Give the size and direction. [3 marks]",
           r"R = √(16² + 12²) = √400 = 20 N. tan θ = 12/16 = 0.75, so θ = 36.9°. The resultant is 20 N, 36.9° north of east."),
        PQ("Two boys pull a box. One pulls 70 N to the right and the other pulls 50 N to the left. Find the resultant force. [2 marks]", "70 − 50 = 20 N to the right."),
        SUM("A scalar has size only; a vector has size and direction.",
            "Distance and speed are scalars. Displacement and velocity are vectors.",
            "A resultant is the single vector with the same effect as several vectors together.",
            "In the same line: add vectors in the same direction and subtract those in opposite directions.",
            r"At right angles: $R = \sqrt{a^2 + b^2}$ and $\tan\theta = b/a$.",
            "For other angles, use a scale drawing: draw tip to tail or complete the parallelogram, measure and convert."),
    ],
))

# ------------------------------------------------------------------ 6. Resolving vectors
LESSONS.append(lesson(
    module=M1,
    topic=T_VEC,
    title="Resolving a vector into components",
    slug="pha-resolving-vectors",
    minutes=22,
    summary="A single slanting force or velocity can be split into two perpendicular components. Use F cos θ and F sin θ to resolve a vector, and use this for a rope pulling a load and a weight on a slope.",
    objectives=[
        "Explain what it means to resolve a vector",
        r"Calculate horizontal and vertical components using $F\cos\theta$ and $F\sin\theta$",
        "Find the components of a weight along and into a slope",
        "Combine two perpendicular components to get back the original vector",
    ],
    key_concepts=["Component", "Resolving", "Sine and cosine", "Inclined plane", "Perpendicular components"],
    blocks=[
        H("Introduction"),
        T("A young man in Limbe drags a heavy sack of cassava along the ground using a rope. He pulls slightly upwards, "
          "not exactly along the ground. Only part of his pull moves the sack forward. The other part lifts the sack a little."),
        T("To study this we split the single pull into two parts at right angles. This is called **resolving** the force."),
        D("**Resolving** a vector means replacing it by two **components** at right angles to each other that together have the same effect as the original vector.", title="Definition: resolving a vector"),
        H("The rule"),
        T(r"Suppose a force $F$ makes an angle $\theta$ with the horizontal. Draw a right-angled triangle with $F$ as the longest side (the hypotenuse). "
          r"The horizontal component is the side **next to** the angle and the vertical component is the side **opposite** it."),
        F(r"F_x = F\cos\theta \qquad F_y = F\sin\theta", title="Components"),
        IMG("f5ph-a-vec-resolve.svg", alt="An 80 N force at 30 degrees above the horizontal, resolved into a horizontal component of 69.3 N and a vertical component of 40 N.",
            caption="Figure 1. An 80 N force at 30° above the horizontal."),
        KEY("Which one is cos and which is sin?", r"Look at where the angle is. The component **touching the angle** uses cosine. The component **opposite the angle** uses sine.", cards=[
            ["Angle measured from the horizontal", r"horizontal part $= F\cos\theta$, vertical part $= F\sin\theta$"],
            ["Angle measured from the vertical", r"vertical part $= F\cos\theta$, horizontal part $= F\sin\theta$"],
        ]),
        EX("Worked example 1: a force at an angle", intro="A force of 80 N acts at 30° above the horizontal. Find its horizontal and vertical components.", steps=[
            S("Horizontal component", math=r"F_x = 80\cos 30^\circ = 80 \times 0.866 = 69.3\ \text{N}"),
            S("Vertical component", math=r"F_y = 80\sin 30^\circ = 80 \times 0.5 = 40\ \text{N}"),
        ], check=r"\sqrt{69.3^2 + 40^2} = \sqrt{4802 + 1600} = 80\ \text{N}"),
        EX("Worked example 2: a rope pulling a sack", intro="The man pulls the sack with a rope that makes 40° with the ground. The pull is 150 N. How much of it moves the sack along the ground and how much lifts it?", steps=[
            S("The part that moves the sack along the ground is the horizontal component", math=r"150\cos 40^\circ = 150 \times 0.766 = 115\ \text{N}"),
            S("The part that lifts it is the vertical component", math=r"150\sin 40^\circ = 150 \times 0.643 = 96.4\ \text{N}"),
            S("Conclusion", text="Only 115 N out of 150 N pulls the sack along the ground."),
        ]),
        T("If the man pulls at a smaller angle, the horizontal component grows. Pulling nearly flat uses almost all of the pull to move the sack."),
        H("Weight on a slope"),
        T("A box on a slope is pulled down by its weight, which acts straight down. We resolve this weight into one component "
          "**along the slope** (which tries to make the box slide down) and one **into the slope** (which presses the box on the surface)."),
        IMG("f5ph-a-slope.svg", alt="A block on a slope inclined at 30 degrees. The weight of 100 N acts vertically down. It is resolved into 50 N along the slope and 86.6 N into the slope.",
            caption="Figure 2. A weight of 100 N on a 30° slope."),
        F(r"\text{along the slope} = W\sin\theta \qquad \text{into the slope} = W\cos\theta", title="Weight on a slope of angle θ"),
        EX("Worked example 3: a box on a slope", intro="A box of mass 10 kg rests on a slope at 30°. Take g = 10 N/kg. Find the component of its weight (a) down the slope, (b) into the slope.", steps=[
            S("Find the weight", math=r"W = mg = 10 \times 10 = 100\ \text{N}"),
            S("(a) Along the slope", math=r"W\sin 30^\circ = 100 \times 0.5 = 50\ \text{N}"),
            S("(b) Into the slope", math=r"W\cos 30^\circ = 100 \times 0.866 = 86.6\ \text{N}"),
        ], check=r"\sqrt{50^2 + 86.6^2} = \sqrt{2500 + 7500} = 100\ \text{N}"),
        EX("Worked example 4: from components back to the vector", intro="A boat has a velocity component of 12 m/s east and 16 m/s north. Find its speed and direction.", steps=[
            S("Speed", math=r"v = \sqrt{12^2 + 16^2} = \sqrt{400} = 20\ \text{m/s}"),
            S("Direction", math=r"\tan\theta = \dfrac{16}{12} \Rightarrow \theta = 53.1^\circ", text="20 m/s at 53.1° north of east."),
        ]),
        MISTAKE("Swapping sine and cosine", r"Draw the triangle and mark the angle. The side touching the angle is $F\cos\theta$. A quick test: if $\theta = 0^\circ$, all of the force is horizontal, and $\cos 0^\circ = 1$."),
        MISTAKE("Calculator in radians", "Check that the calculator is in degree mode. $\\sin 30^\\circ$ must give 0.5."),
        QUIZ(r"A force of 100 N acts at 60° above the horizontal. What is the horizontal component?",
             ["86.6 N", "50 N", "100 N", "173 N"], 1,
             r"$F_x = 100\cos 60^\circ = 100 \times 0.5 = 50$ N.",
             hint="The angle is measured from the horizontal, so the horizontal component uses cosine.",
             feedback=["That is 100 sin 60°, the vertical component.", "", "That would be the case only if the force were exactly horizontal.", "A component can never be larger than the force itself."]),
        QUIZ("The weight of a block on a slope is 60 N and the slope is at 30°. What is the component of the weight along the slope?",
             ["52 N", "30 N", "60 N", "120 N"], 1,
             r"$W\sin 30^\circ = 60 \times 0.5 = 30$ N.",
             hint="The component along the slope uses the sine of the slope angle.",
             feedback=["That is 60 cos 30° = 52 N, the component into the slope.", "", "That is the whole weight.", "A component is never larger than the weight."]),
        TIP("Resolving a force appears in Paper 2 questions on forces at an angle (pulling a load, a slope). Show the triangle, write F cos θ or F sin θ, and give units. "
            "In Paper 1 you may be asked which component is larger at a given angle.", title="Exam link"),
        H("Practice questions"),
        PQ("Define 'resolving a vector'. [2 marks]", "Resolving a vector means replacing it by two perpendicular components that together have the same effect as the original vector."),
        PQ("A force of 50 N acts at 37° above the horizontal. Find its horizontal and vertical components (cos 37° = 0.80, sin 37° = 0.60). [2 marks]", "Horizontal: 50 × 0.80 = 40 N. Vertical: 50 × 0.60 = 30 N."),
        PQ("A trolley of weight 200 N is on a ramp at 20°. Find the component of the weight along the ramp. [2 marks]", r"200 × sin 20° = 200 × 0.342 = 68.4 N (about 68 N)."),
        PQ("A kicked ball leaves the ground at 20 m/s at 30° above the horizontal. Find the horizontal and vertical components of its velocity. [2 marks]", r"Horizontal: 20 cos 30° = 17.3 m/s. Vertical: 20 sin 30° = 10 m/s."),
        SUM("Resolving a vector splits it into two perpendicular components with the same effect.",
            r"For an angle $\theta$ from the horizontal: $F_x = F\cos\theta$ and $F_y = F\sin\theta$.",
            "The component touching the angle uses cosine; the component opposite the angle uses sine.",
            r"A weight $W$ on a slope of angle $\theta$ has component $W\sin\theta$ along the slope and $W\cos\theta$ into the slope.",
            r"Components can be recombined with $R = \sqrt{a^2 + b^2}$."),
    ],
))

# ------------------------------------------------------------------ 7. Speed, velocity, acceleration
LESSONS.append(lesson(
    module=M2,
    topic=T_KIN,
    title="Speed, velocity and acceleration",
    slug="pha-speed-velocity-acceleration",
    minutes=22,
    summary="Define distance, displacement, speed, velocity and acceleration, use speed = distance ÷ time and a = (v − u) ÷ t, find average speed, and recognise deceleration as negative acceleration.",
    objectives=[
        "Define speed, average speed, velocity and acceleration with their units",
        "Calculate speed, average speed and acceleration from data",
        "Convert between km/h and m/s",
        "Explain deceleration and the difference between speed and velocity",
    ],
    key_concepts=["Speed", "Average speed", "Velocity", "Acceleration", "Deceleration", "m/s²"],
    blocks=[
        H("Introduction"),
        T("A bush-taxi leaves a motor park and joins the main road. At first it creeps through the traffic. Then it speeds up, "
          "slows down at a checkpoint and stops. We can describe every part of this trip with three ideas: how fast it goes, "
          "in which direction, and how quickly its speed changes."),
        H("Speed and velocity"),
        D("**Speed** is the distance travelled per unit time. It is a scalar. SI unit: metre per second (m/s).", title="Definition: speed",
          formula=r"\text{speed} = \dfrac{\text{distance}}{\text{time}}"),
        D("**Average speed** is the total distance travelled divided by the total time taken.", title="Definition: average speed",
          formula=r"\text{average speed} = \dfrac{\text{total distance}}{\text{total time}}"),
        D("**Velocity** is the displacement per unit time, or the speed in a stated direction. It is a vector. SI unit: m/s.", title="Definition: velocity",
          formula=r"v = \dfrac{\text{displacement}}{\text{time}}"),
        T("A car moving at 20 m/s north and another at 20 m/s south have the same speed but different velocities."),
        KEY("Changing km/h and m/s", r"To change km/h to m/s divide by 3.6. To change m/s to km/h multiply by 3.6.", cards=[
            ["Example", r"90 km/h ÷ 3.6 = 25 m/s"],
            ["Check", r"1 km/h = 1000 m ÷ 3600 s = 0.278 m/s"],
        ]),
        EX("Worked example 1: speed of a bus", intro="A bus travels 240 km in 4 hours. Find its average speed in km/h and in m/s.", steps=[
            S("Use average speed = distance ÷ time", math=r"\dfrac{240}{4} = 60\ \text{km/h}"),
            S("Change to m/s", math=r"\dfrac{60}{3.6} = 16.7\ \text{m/s}"),
        ]),
        EX("Worked example 2: average speed for two stages", intro="A motorbike travels 30 km at 60 km/h and then 30 km at 30 km/h. Find the average speed for the whole trip.", steps=[
            S("Time for the first stage", math=r"t_1 = \dfrac{30}{60} = 0.5\ \text{h}"),
            S("Time for the second stage", math=r"t_2 = \dfrac{30}{30} = 1.0\ \text{h}"),
            S("Total distance ÷ total time", math=r"\dfrac{60}{0.5 + 1.0} = \dfrac{60}{1.5} = 40\ \text{km/h}", text="Notice that this is not (60 + 30) ÷ 2 = 45 km/h. The bike spends longer at the lower speed."),
        ]),
        EX("Worked example 3: a lap of a track", intro="An athlete runs one lap of a 400 m track in 50 s. Find her average speed and her average velocity for the lap.", steps=[
            S("Average speed", math=r"\dfrac{400}{50} = 8\ \text{m/s}"),
            S("Average velocity", text="Her displacement for a complete lap is 0 m, because she ends where she began.", math=r"\dfrac{0}{50} = 0\ \text{m/s}"),
        ]),
        H("Acceleration"),
        D("**Acceleration** is the rate of change of velocity: the change in velocity per unit time. It is a vector. SI unit: metre per second squared (m/s²).",
          title="Definition: acceleration", formula=r"a = \dfrac{v - u}{t}"),
        T("In the formula $u$ is the **initial** velocity, $v$ is the **final** velocity and $t$ is the time taken for the change. "
          "An acceleration of 2 m/s² means the velocity increases by 2 m/s every second."),
        T("If the speed decreases, the acceleration is negative. This is called **deceleration** or retardation. "
          "A car braking from 20 m/s to rest in 5 s has $a = (0 - 20) \\div 5 = -4$ m/s²."),
        EX("Worked example 4: accelerating car", intro="A car increases its speed from 5 m/s to 25 m/s in 8 s. Find its acceleration.", steps=[
            S("Write down the values", text="u = 5 m/s, v = 25 m/s, t = 8 s."),
            S("Use a = (v − u) ÷ t", math=r"a = \dfrac{25 - 5}{8} = \dfrac{20}{8} = 2.5\ \text{m/s}^2"),
        ]),
        EX("Worked example 5: a taxi braking", intro="A taxi moving at 20 m/s brakes and stops in 5 s. Find its acceleration.", steps=[
            S("The final velocity is zero", text="u = 20 m/s, v = 0, t = 5 s."),
            S("Substitute", math=r"a = \dfrac{0 - 20}{5} = -4\ \text{m/s}^2", text="The negative sign shows deceleration: the taxi loses 4 m/s every second."),
        ]),
        MISTAKE("Using speed and velocity as the same", "Speed is a scalar and has no direction. Velocity has a direction. A change of direction at constant speed is still a change of velocity, so it is an acceleration."),
        MISTAKE("Averaging the speeds", "Average speed = total distance ÷ total time. Do **not** add two speeds and divide by 2 unless the two stages last equal times."),
        MISTAKE("Wrong unit for acceleration", "The unit is m/s², not m/s. Acceleration is a change of velocity (m/s) per second, which is m/s ÷ s = m/s²."),
        QUIZ("A cyclist moves 150 m in 25 s. What is the speed?",
             ["6 m/s", "0.17 m/s", "3750 m/s", "175 m/s"], 0,
             "Speed = distance ÷ time = 150 ÷ 25 = 6 m/s.",
             hint="Divide distance by time.",
             feedback=["", "You divided time by distance.", "You multiplied distance and time.", "You added the two numbers."]),
        QUIZ("A train accelerates from 10 m/s to 30 m/s in 10 s. What is its acceleration?",
             ["2 m/s²", "4 m/s²", "0.5 m/s²", "20 m/s²"], 0,
             "a = (30 − 10) ÷ 10 = 2 m/s².",
             hint="Use the change in velocity, then divide by the time.",
             feedback=["", "This divides 40 by 10: you added the velocities instead of finding the change.", "You divided the time by the change in velocity.", "This is the change in velocity, not the acceleration."]),
        TIP("Speed, velocity and acceleration are tested in Paper 1 multiple choice and in the first part of many Paper 2 mechanics questions. "
            "Write the formula, substitute with units, and give the unit of your answer (m/s or m/s²).", title="Exam link"),
        H("Practice questions"),
        PQ("Define acceleration and state its SI unit. [2 marks]", "Acceleration is the rate of change of velocity (change in velocity per unit time). Its SI unit is m/s²."),
        PQ("A runner covers 100 m in 12.5 s. Find the average speed. [2 marks]", "100 ÷ 12.5 = 8 m/s."),
        PQ("Change 108 km/h to m/s. [2 marks]", "108 ÷ 3.6 = 30 m/s."),
        PQ("A lorry slows from 18 m/s to 6 m/s in 4 s. Find its acceleration and say what the sign shows. [3 marks]", "a = (6 − 18) ÷ 4 = −3 m/s². The negative sign shows deceleration: the speed is falling by 3 m/s every second."),
        SUM("Speed = distance ÷ time (scalar). Velocity = displacement ÷ time (vector). Both in m/s.",
            "Average speed = total distance ÷ total time.",
            "To change km/h to m/s divide by 3.6.",
            r"Acceleration $a = (v - u) \div t$, in m/s². It is the change in velocity per second.",
            "A negative acceleration is a deceleration: the object is slowing down.",
            "Always give units with your answers."),
    ],
))

# ------------------------------------------------------------------ 8. Motion graphs
LESSONS.append(lesson(
    module=M2,
    topic=T_KIN,
    title="Distance-time and speed-time graphs",
    slug="pha-motion-graphs",
    minutes=24,
    summary="A graph can show a whole journey. Read speed from the gradient of a distance-time graph, and acceleration and distance from the gradient and area of a speed-time graph.",
    objectives=[
        "Describe motion from a distance-time graph and find speed from its gradient",
        "Describe motion from a speed-time graph",
        "Find acceleration from the gradient of a speed-time graph",
        "Find distance travelled from the area under a speed-time graph",
    ],
    key_concepts=["Gradient", "Distance-time graph", "Speed-time graph", "Area under a graph", "Constant speed", "Rest"],
    blocks=[
        H("Introduction"),
        T("Picture a minibus journey from Buea to Limbe. The driver speeds up on the straight road, keeps a steady speed, "
          "stops to let passengers down and then moves again. A single graph can show all of this at once."),
        T("The Board's examiners report that candidates plot and read graphs better than before, but graphs are still a core "
          "skill. In this lesson you learn what each part of two graphs means."),
        H("Distance-time graphs"),
        T("On a **distance-time graph** the distance is on the vertical axis and the time on the horizontal axis."),
        KEY("Reading a distance-time graph", "The **gradient (slope)** of the graph is the speed.", cards=[
            ["Straight sloping line", "Constant speed. A steeper line means a higher speed."],
            ["Horizontal line", "The distance does not change, so the object is at rest."],
            ["Curved line", "The speed is changing. A line that gets steeper means the object is speeding up."],
        ], note=r"Speed = gradient = vertical change ÷ horizontal change."),
        IMG("f5ph-a-dt-graph.svg", alt="Distance-time graph. From O to P the distance rises to 40 m in 20 s. From P to Q it stays at 40 m for 10 s. From Q to R it rises to 120 m at 50 s.",
            caption="Figure 1. A distance-time graph for a cyclist."),
        EX("Worked example 1: reading Figure 1", intro="Use Figure 1 to find (a) the speed from O to P, (b) the speed from P to Q, (c) the speed from Q to R, (d) the average speed for the whole journey.", steps=[
            S("(a) O to P", math=r"\dfrac{40 - 0}{20 - 0} = 2\ \text{m/s}"),
            S("(b) P to Q", text="The line is horizontal. The distance does not change, so the speed is 0 m/s and the cyclist is at rest for 10 s."),
            S("(c) Q to R", math=r"\dfrac{120 - 40}{50 - 30} = \dfrac{80}{20} = 4\ \text{m/s}"),
            S("(d) Whole journey", math=r"\dfrac{120}{50} = 2.4\ \text{m/s}", text="Total distance ÷ total time."),
        ]),
        H("Speed-time graphs"),
        T("On a **speed-time graph** the speed (or velocity) is on the vertical axis. It shows how the speed changes, "
          "so it gives two things: the acceleration and the distance travelled."),
        KEY("Reading a speed-time graph", "Gradient = acceleration. Area under the graph = distance travelled.", cards=[
            ["Sloping up", "Constant positive acceleration: the speed rises steadily."],
            ["Horizontal line", "Constant speed (zero acceleration)."],
            ["Sloping down", "Constant deceleration: the speed falls steadily."],
        ], note="Speed-time and distance-time graphs look alike. Always read the axis labels first."),
        IMG("f5ph-a-vt-graph.svg", alt="Speed-time graph. Speed rises from 0 to 20 m/s in 10 s, stays at 20 m/s until 30 s, then falls to 0 at 40 s. The area under the graph is shaded.",
            caption="Figure 2. A speed-time graph for a taxi. The shaded area is the distance travelled."),
        EX("Worked example 2: acceleration from Figure 2", intro="Find the acceleration for (a) O to P, (b) P to Q, (c) Q to R.", steps=[
            S("(a) O to P", math=r"a = \dfrac{20 - 0}{10 - 0} = 2\ \text{m/s}^2"),
            S("(b) P to Q", text="The line is horizontal, so the speed is steady at 20 m/s and the acceleration is 0."),
            S("(c) Q to R", math=r"a = \dfrac{0 - 20}{40 - 30} = -2\ \text{m/s}^2", text="Negative: a deceleration of 2 m/s²."),
        ]),
        EX("Worked example 3: distance from the area", intro="Find the total distance travelled in Figure 2 and the average speed.", steps=[
            S("Triangle O to P", math=r"\tfrac{1}{2} \times 10 \times 20 = 100\ \text{m}"),
            S("Rectangle P to Q", math=r"20 \times (30 - 10) = 400\ \text{m}"),
            S("Triangle Q to R", math=r"\tfrac{1}{2} \times 10 \times 20 = 100\ \text{m}"),
            S("Total distance", math=r"100 + 400 + 100 = 600\ \text{m}"),
            S("Average speed", math=r"\dfrac{600}{40} = 15\ \text{m/s}"),
        ], check=r"\text{Trapezium: } \tfrac{1}{2}(20 + 40) \times 20 = 600\ \text{m}"),
        T("The whole shape in Figure 2 is a trapezium. Its area is $\\tfrac{1}{2}(\\text{sum of parallel sides}) \\times \\text{height}$. "
          "The parallel sides are the times 40 s and 20 s, and the height is 20 m/s."),
        H("Graphs with a negative speed"),
        T("If velocity is given a direction, a graph can go below the time axis. A negative velocity means the object moves in the "
          "opposite direction. This happens with a ball thrown upwards, which you meet in the lesson on free fall."),
        MISTAKE("Reading a distance-time graph as a picture of the path", "A line rising to the right does not mean the object goes uphill. It means the distance increases with time."),
        MISTAKE("Calling a horizontal line 'constant speed' on a distance-time graph", "On a distance-time graph a horizontal line means the object is **at rest**. On a speed-time graph a horizontal line means **constant speed**."),
        MISTAKE("Finding the area wrongly", "Use the scale of the axes, not the number of squares. Also keep every unit: m/s × s gives m."),
        QUIZ("On a distance-time graph, which feature shows that an object is at rest?",
             ["A line sloping upward", "A horizontal line", "A line sloping downward", "A curved line"], 1,
             "The distance does not change with time, so the line is horizontal.",
             hint="Ask what the distance does while time goes on.",
             feedback=["This shows constant speed, moving away.", "", "This shows the object returning, at constant speed.", "A curve shows a changing speed."]),
        QUIZ("On a speed-time graph, what does the area under the graph represent?",
             ["Acceleration", "Time taken", "Distance travelled", "Average force"], 2,
             "Speed × time = distance. The area under a speed-time graph is the distance.",
             hint="Multiply the units of the two axes: m/s × s.",
             feedback=["Acceleration is the gradient, not the area.", "Time is read from the horizontal axis.", "", "Force does not appear on this graph."]),
        TIP("Motion graphs appear in almost every Paper 1 and in Paper 2 mechanics questions. You may be asked to plot a graph from a table, "
            "find a gradient, or find an area. Always show the triangle you use for a gradient and give the unit.", title="Exam link"),
        H("Practice questions"),
        PQ("On a speed-time graph what quantity is given by (a) the gradient, (b) the area under the graph? [2 marks]", "(a) acceleration; (b) distance travelled."),
        PQ("A distance-time graph is a straight line from (0 s, 0 m) to (10 s, 50 m). Find the speed. [2 marks]", "Speed = gradient = 50 ÷ 10 = 5 m/s."),
        PQ("A car's speed rises steadily from 0 to 12 m/s in 6 s. Find the acceleration and the distance travelled in this time. [3 marks]", "a = 12 ÷ 6 = 2 m/s². Distance = area of triangle = ½ × 6 × 12 = 36 m."),
        PQ("A speed-time graph shows a car at a constant 15 m/s for 20 s. Find the distance travelled. [2 marks]", "Distance = area of the rectangle = 15 × 20 = 300 m."),
        SUM("On a distance-time graph the gradient is the speed; a horizontal line means rest.",
            "On a speed-time graph the gradient is the acceleration; a horizontal line means constant speed.",
            "The area under a speed-time graph is the distance travelled.",
            "A downward-sloping line on a speed-time graph shows deceleration.",
            "Read the axes first, use the scales, and give units."),
    ],
))

# ------------------------------------------------------------------ 9. Equations of motion
LESSONS.append(lesson(
    module=M2,
    topic=T_EQ,
    title="The equations of uniformly accelerated motion",
    slug="pha-equations-of-motion",
    minutes=25,
    summary="When acceleration is constant, four equations link u, v, a, s and t. Learn where they come from, how to choose the right one by listing what you know, and how to use them for starting, braking and overtaking.",
    objectives=[
        "State the equations v = u + at, s = ut + ½at², v² = u² + 2as and s = ½(u + v)t",
        "Explain where the equations come from using a speed-time graph",
        "List known and unknown quantities and choose a suitable equation",
        "Solve problems on speeding up and braking, with correct units",
    ],
    key_concepts=["Uniform acceleration", "Initial and final velocity", "Displacement", "Choosing an equation", "Braking distance"],
    blocks=[
        H("Introduction"),
        T("A driver on the road from Yaoundé to Bafia sees a goat and brakes. How far does the car travel before it stops? "
          "A driver who knows the answer keeps a safe distance. The answer comes from equations that apply whenever the "
          "acceleration is **constant**."),
        D("Motion is **uniformly accelerated** when the acceleration is constant: the velocity changes by the same amount every second, in a straight line.", title="Definition: uniform acceleration"),
        H("The equations and their symbols"),
        CODE("""Symbol   Quantity                  Unit
u        initial velocity          m/s
v        final velocity            m/s
a        acceleration              m/s2
t        time                      s
s        displacement (distance)   m""", "text", title="Symbols"),
        KEY("The four equations", "Each equation misses out one of the five quantities. Use the one that misses the quantity you neither know nor want.", cards=[
            [r"$v = u + at$", "No s"],
            [r"$s = ut + \tfrac{1}{2}at^2$", "No v"],
            [r"$v^2 = u^2 + 2as$", "No t"],
            [r"$s = \tfrac{1}{2}(u + v)t$", "No a"],
        ], note="These equations work only for constant acceleration in a straight line. Use SI units: m, s, m/s, m/s²."),
        H("Where they come from"),
        T("Draw a speed-time graph for an object that starts at speed $u$ and speeds up steadily to $v$ in time $t$. The graph is a straight line."),
        T(r"The gradient is the acceleration, so $a = \dfrac{v-u}{t}$. This rearranges to $v = u + at$. "
          r"The distance is the area under the line. The shape is a trapezium with parallel sides $u$ and $v$ and width $t$, so "
          r"$s = \tfrac{1}{2}(u+v)t$. Put $v = u + at$ into this and you get $s = ut + \tfrac{1}{2}at^2$. "
          r"Eliminating $t$ between the first and last equations gives $v^2 = u^2 + 2as$."),
        H("A method for every problem"),
        KEY("Four steps", "Follow them every time.", cards=[
            ["1. List", "Write u, v, a, s, t. Put in the values you know and mark the one you want with a question mark."],
            ["2. Choose", "Pick the equation that contains the three known and one wanted quantities."],
            ["3. Substitute", "Use SI units. If the object stops, v = 0. If it starts from rest, u = 0."],
            ["4. Answer", "Solve, then write the unit. A negative a means deceleration."],
        ]),
        EX("Worked example 1: starting from rest", intro="A car starts from rest and accelerates at 3 m/s² for 8 s. Find (a) its final velocity, (b) the distance it travels.", steps=[
            S("List", text="u = 0, a = 3 m/s², t = 8 s. Want v and s."),
            S("(a) Use v = u + at", math=r"v = 0 + 3 \times 8 = 24\ \text{m/s}"),
            S("(b) Use s = ut + ½at²", math=r"s = 0 + \tfrac{1}{2} \times 3 \times 8^2 = 96\ \text{m}"),
        ], check=r"s = \tfrac{1}{2}(u + v)t = \tfrac{1}{2}(0 + 24) \times 8 = 96\ \text{m}"),
        EX("Worked example 2: braking distance", intro="A car travelling at 20 m/s brakes and stops in a distance of 40 m. Find the deceleration and the time to stop.", steps=[
            S("List", text="u = 20 m/s, v = 0, s = 40 m. Want a and t."),
            S("Choose v² = u² + 2as (no t)", math=r"0 = 20^2 + 2a(40) \Rightarrow 0 = 400 + 80a"),
            S("Solve for a", math=r"a = -\dfrac{400}{80} = -5\ \text{m/s}^2", text="The car decelerates at 5 m/s²."),
            S("Find t with v = u + at", math=r"0 = 20 - 5t \Rightarrow t = 4\ \text{s}"),
        ], check=r"s = \tfrac{1}{2}(20 + 0) \times 4 = 40\ \text{m}"),
        EX("Worked example 3: speeding up over a distance", intro="A bus increases its speed from 10 m/s to 20 m/s over a distance of 150 m. Find its acceleration and the time taken.", steps=[
            S("List", text="u = 10 m/s, v = 20 m/s, s = 150 m. Want a and t."),
            S("Use v² = u² + 2as", math=r"400 = 100 + 2a(150) \Rightarrow 300 = 300a"),
            S("Solve", math=r"a = 1\ \text{m/s}^2"),
            S("Find t", math=r"t = \dfrac{v - u}{a} = \dfrac{20 - 10}{1} = 10\ \text{s}"),
        ], check=r"s = \tfrac{1}{2}(10 + 20) \times 10 = 150\ \text{m}"),
        MISTAKE("Using the equations when the acceleration changes", "They work only for **constant** acceleration. A car that is slowly pressing the accelerator has changing acceleration and these equations do not apply exactly."),
        MISTAKE("Forgetting the signs", "If the object slows down, a is negative. Put the negative sign in. Do not write a deceleration of 5 m/s² as +5."),
        MISTAKE("Mixing units", "Convert km/h to m/s before you substitute. A car at 72 km/h has u = 20 m/s."),
        QUIZ("A cyclist starts from rest and accelerates at 2 m/s² for 5 s. How far does she travel?",
             ["10 m", "25 m", "50 m", "5 m"], 1,
             r"$s = \tfrac{1}{2}at^2 = \tfrac{1}{2} \times 2 \times 25 = 25$ m.",
             hint="She starts from rest, so u = 0, and you know a and t.",
             feedback=["This is v = at = 10 m/s, the final velocity, not the distance.", "", "You forgot the one half: 2 × 25.", "You used only the time."]),
        QUIZ("Which equation has no time in it?",
             [r"$v = u + at$", r"$v^2 = u^2 + 2as$", r"$s = ut + \tfrac{1}{2}at^2$", r"$s = \tfrac{1}{2}(u+v)t$"], 1,
             r"$v^2 = u^2 + 2as$ contains $u$, $v$, $a$ and $s$ but not $t$.",
             hint="Look for the equation that lacks the letter t.",
             feedback=["This contains t.", "", "This contains t.", "This contains t."]),
        TIP("The equations of motion are a staple of Paper 2 calculation questions and appear in Paper 1 too. "
            "Show your list of u, v, a, s and t and the equation you use. Marks go for the formula, the substitution and the answer with its unit.", title="Exam link"),
        H("Practice questions"),
        PQ("State the equation of motion that does not involve time. [1 mark]", r"$v^2 = u^2 + 2as$."),
        PQ("A train starts from rest and reaches 30 m/s with an acceleration of 1.5 m/s². Find the time taken. [2 marks]", "v = u + at, so 30 = 0 + 1.5t, giving t = 20 s."),
        PQ("A motorbike moving at 15 m/s accelerates at 2 m/s² for 6 s. Find the distance it covers. [3 marks]", "s = ut + ½at² = 15 × 6 + ½ × 2 × 36 = 90 + 36 = 126 m."),
        PQ("A car moving at 25 m/s brakes with a deceleration of 5 m/s². Find its stopping distance. [3 marks]", "v² = u² + 2as, so 0 = 625 + 2(−5)s, giving s = 625 ÷ 10 = 62.5 m."),
        SUM(r"For constant acceleration: $v = u + at$, $s = ut + \tfrac{1}{2}at^2$, $v^2 = u^2 + 2as$ and $s = \tfrac{1}{2}(u+v)t$.",
            "They come from the speed-time graph: gradient = a and area = s.",
            "List u, v, a, s and t, mark what you want, and choose the equation without the quantity you do not know.",
            "Starting from rest means u = 0; stopping means v = 0.",
            "Use SI units, and put in a negative a for deceleration."),
    ],
))

# ------------------------------------------------------------------ 10. Free fall
LESSONS.append(lesson(
    module=M2,
    topic=T_EQ,
    title="Free fall and objects thrown upwards",
    slug="pha-free-fall",
    minutes=24,
    summary="Near the earth every freely falling object accelerates downwards at g = 10 m/s² (taking g = 10). Use the equations of motion for a dropped object and for one thrown upwards, with signs and a velocity-time graph.",
    objectives=[
        "Define free fall and state the value of g used in this course",
        "Solve problems on objects dropped from rest",
        "Solve problems on objects thrown upwards, including greatest height and time of flight",
        "Read a velocity-time graph for an object thrown upwards",
    ],
    key_concepts=["Free fall", "Acceleration due to gravity", "Air resistance", "Greatest height", "Time of flight", "Sign convention"],
    blocks=[
        H("Introduction"),
        T("A ripe mango drops from a tree in a compound in Mbalmayo. A moment later it hits the ground. "
          "A football kicked straight up in a school yard rises, stops for an instant, and comes back down. "
          "Both are moving under the pull of gravity only. They are in **free fall**."),
        D("**Free fall** is motion under the force of gravity alone, with air resistance ignored.", title="Definition: free fall"),
        D("The **acceleration due to gravity**, $g$, is the acceleration of a freely falling object near the earth's surface. In this course "
          "we use $g = 10\\ \\text{m/s}^2$. (A more exact value is 9.8 m/s². Use whichever the question gives.)", title="Definition: acceleration of free fall"),
        T("Two important facts follow. First, every object in free fall has the **same** acceleration, whatever its mass. "
          "A heavy and a light stone dropped together reach the ground at the same time. Second, in the air a feather falls slowly "
          "only because of **air resistance**. In a vacuum a feather and a stone fall together."),
        KEY("Using the equations of motion", "Take the direction of the motion at the start as positive.", cards=[
            ["Dropped downwards", "Take down as positive: a = +10 m/s², u = 0."],
            ["Thrown upwards", "Take up as positive: u is positive and a = −10 m/s² because gravity pulls down."],
        ], note="At the highest point the velocity is zero for an instant, but the acceleration is still 10 m/s² downwards."),
        H("Objects dropped from rest"),
        EX("Worked example 1: the falling mango", intro="A mango falls from a branch 20 m above the ground. Take g = 10 m/s². Find (a) the time to reach the ground and (b) its speed on arrival.", steps=[
            S("List (down positive)", text="u = 0, a = 10 m/s², s = 20 m. Want t and v."),
            S("(a) Use s = ut + ½at²", math=r"20 = 0 + \tfrac{1}{2}(10)t^2 \Rightarrow t^2 = 4 \Rightarrow t = 2\ \text{s}"),
            S("(b) Use v = u + at", math=r"v = 0 + 10 \times 2 = 20\ \text{m/s}"),
        ], check=r"v^2 = u^2 + 2as = 0 + 2(10)(20) = 400 \Rightarrow v = 20\ \text{m/s}"),
        EX("Worked example 2: depth of a well", intro="A stone dropped into a well takes 3.0 s to reach the water. Ignore the time sound takes to come back. Find the depth of the well (g = 10 m/s²).", steps=[
            S("List", text="u = 0, a = 10 m/s², t = 3.0 s. Want s."),
            S("Use s = ut + ½at²", math=r"s = 0 + \tfrac{1}{2}(10)(3.0)^2 = 45\ \text{m}"),
        ]),
        H("Objects thrown upwards"),
        T("When a ball is thrown upwards, gravity slows it down by 10 m/s every second. At the top it stops for an instant. "
          "Then it falls back and speeds up again. On the way down it passes each height with the same speed it had on the way up."),
        IMG("f5ph-a-ball-vt.svg", alt="Velocity-time graph for a ball thrown up at 20 m/s. A straight line falls from 20 m/s at 0 s through zero at 2 s to minus 20 m/s at 4 s.",
            caption="Figure 1. A ball thrown upwards at 20 m/s. The gradient is −10 m/s² all the time. Velocity is zero at 2 s, the highest point."),
        EX("Worked example 3: ball thrown straight up", intro="A ball is thrown vertically upwards at 20 m/s. Take g = 10 m/s². Find (a) the time to reach the highest point, (b) the greatest height, (c) the total time in the air until it returns, and (d) its velocity when it returns.", steps=[
            S("List (up positive)", text="u = +20 m/s, a = −10 m/s². At the top v = 0."),
            S("(a) Use v = u + at", math=r"0 = 20 - 10t \Rightarrow t = 2\ \text{s}"),
            S("(b) Use v² = u² + 2as", math=r"0 = 400 - 20s \Rightarrow s = 20\ \text{m}"),
            S("(c) Time down equals time up", math=r"2 + 2 = 4\ \text{s}"),
            S("(d) Same speed, opposite direction", math=r"v = -20\ \text{m/s}", text="It returns at 20 m/s downwards."),
        ], check=r"\text{Area under the graph above the axis} = \tfrac{1}{2}(2)(20) = 20\ \text{m}"),
        EX("Worked example 4: a stone thrown up from the ground", intro="A stone is thrown upwards at 15 m/s. Find the greatest height (g = 10 m/s²).", steps=[
            S("List", text="u = 15 m/s, v = 0, a = −10 m/s². Want s."),
            S("Use v² = u² + 2as", math=r"0 = 225 - 20s \Rightarrow s = 11.25\ \text{m}"),
        ]),
        MISTAKE("Saying heavier objects fall faster", "In free fall all objects have the same acceleration. In air the difference is caused by air resistance, which depends on the size and shape of the object."),
        MISTAKE("Thinking the acceleration is zero at the top", "At the highest point the **velocity** is zero for an instant, but gravity still pulls the ball with acceleration 10 m/s² downwards."),
        MISTAKE("Wrong sign for g", "If upwards is positive, g is −10 m/s². If downwards is positive, g is +10 m/s². Choose a direction and stay with it."),
        QUIZ("A stone is dropped from rest. How fast is it moving after 3 s (g = 10 m/s²)?",
             ["13 m/s", "30 m/s", "45 m/s", "3.3 m/s"], 1,
             "v = u + at = 0 + 10 × 3 = 30 m/s.",
             hint="Use v = u + at with u = 0.",
             feedback=["You added 10 and 3.", "", "This is the distance fallen in 3 s (45 m), not the speed.", "You divided 10 by 3."]),
        QUIZ("A ball is thrown upwards. At its highest point which statement is correct?",
             ["Velocity and acceleration are both zero", "Velocity is zero and acceleration is 10 m/s² downwards", "Velocity is 10 m/s and acceleration is zero", "Velocity is zero and acceleration is 10 m/s² upwards"], 1,
             "At the top the ball is momentarily at rest, but gravity still gives an acceleration of 10 m/s² downwards.",
             hint="The force of gravity does not stop acting at the top.",
             feedback=["Gravity still acts, so the acceleration is not zero.", "", "If the velocity were 10 m/s the ball would still be moving.", "Gravity acts downwards, not upwards."]),
        TIP("Free fall appears in Paper 1 and in Paper 2 calculations, and the Board's examiners note that Mechanics was poorly answered, so practise it. "
            "State which value of g you use (10 m/s² or 9.8 m/s²) and give the unit of the answer.", title="Exam link"),
        H("Practice questions"),
        PQ("Define free fall. [1 mark]", "Free fall is motion under the force of gravity alone, with air resistance ignored."),
        PQ("A coin is dropped from a bridge and hits the water after 2.5 s. Find the height of the bridge (g = 10 m/s²). [2 marks]", "s = ½gt² = ½ × 10 × 2.5² = ½ × 10 × 6.25 = 31.25 m (about 31 m)."),
        PQ("A ball is thrown upwards at 30 m/s. Find (a) the time to reach the top and (b) the greatest height (g = 10 m/s²). [3 marks]", "(a) 0 = 30 − 10t gives t = 3 s. (b) 0 = 900 − 20s gives s = 45 m."),
        PQ("Explain why a feather falls more slowly than a stone in air but not in a vacuum. [2 marks]", "In air the feather has a large air resistance compared with its weight, so its acceleration is small. In a vacuum there is no air resistance and both fall with the same acceleration g."),
        SUM("Free fall is motion under gravity alone. Near the earth g = 10 m/s² in this course (9.8 m/s² if stated).",
            "All objects in free fall have the same acceleration, whatever their mass.",
            "Dropped from rest: u = 0 and the equations of motion give t and v.",
            "Thrown upwards: take up as positive, a = −10 m/s², and v = 0 at the top.",
            "The time up equals the time down, and the object returns with the same speed it started with.",
            "A velocity-time graph for free fall is a straight line of gradient −10 m/s² (up positive)."),
    ],
))

# ------------------------------------------------------------------ 11. Newton's laws
LESSONS.append(lesson(
    module=M2,
    topic=T_NEW,
    title="Newton's three laws of motion",
    slug="pha-newtons-laws",
    minutes=25,
    summary="Newton's first law explains inertia and balanced forces, the second law gives F = ma, and the third law says forces come in equal and opposite pairs acting on different bodies. Learn each law, state it exactly, and use it.",
    objectives=[
        "State Newton's three laws of motion in correct words",
        "Explain inertia with everyday examples",
        "Use F = ma to find force, mass or acceleration",
        "Identify action-reaction pairs",
    ],
    key_concepts=["Inertia", "Resultant force", "F = ma", "Newton", "Action and reaction", "Balanced forces"],
    blocks=[
        H("Introduction"),
        T("A minibus brakes suddenly at a junction in Douala. The passengers jerk forward. No one pushed them. "
          "A loaded truck takes much longer to get going than an empty pickup, even if the engines push equally hard. "
          "A man pushing a canoe off the bank sees the canoe move away and himself move back a little. "
          "These three situations are explained by Newton's three laws."),
        T("The Board's examiners say candidates lose marks for poorly phrased laws and definitions, so learn the wording of each law carefully."),
        H("Newton's first law and inertia"),
        D("**Newton's first law:** a body stays at rest, or moves with constant velocity in a straight line, unless a resultant (unbalanced) force acts on it.", title="Newton's first law"),
        D("**Inertia** is the reluctance of a body to change its state of rest or of motion. The larger the mass of a body, the larger its inertia.", title="Definition: inertia"),
        T("In the minibus, the passengers were moving forward with the bus. When the bus stopped, the passengers' inertia kept them "
          "moving forward. A seat belt provides the resultant force that stops them."),
        T("If the **forces on a body are balanced** (the resultant is zero), the body either stays at rest or keeps moving with "
          "**constant velocity**. A car at a steady 90 km/h on a straight road has its driving force equal to the total of friction and air resistance."),
        H("Newton's second law"),
        D(r"**Newton's second law:** the resultant force acting on a body is equal to its mass multiplied by its acceleration, and the acceleration is in the direction of the force.",
          title="Newton's second law", formula=r"F = ma"),
        D("One **newton** is the force that gives a mass of 1 kg an acceleration of 1 m/s².", title="Definition: the newton", formula=r"1\ \text{N} = 1\ \text{kg m/s}^2"),
        T("Here $F$ is the **resultant** force, which is the net force after adding all the forces with their directions. "
          "For a given force, a larger mass gives a smaller acceleration. A loaded truck accelerates less than an empty pickup."),
        IMG("f5ph-a-forces.svg", alt="A 6 kg block on a floor with four forces: a 50 N pull to the right, a 20 N friction force to the left, a 60 N weight downwards and a 60 N normal reaction upwards.",
            caption="Figure 1. Forces on a block being pulled along a floor."),
        EX("Worked example 1: a block pulled along a floor", intro="In Figure 1 a 6 kg block is pulled with 50 N while friction is 20 N. Find its acceleration.", steps=[
            S("Vertical forces", text="Weight 60 N down and the normal reaction 60 N up cancel. There is no vertical acceleration."),
            S("Resultant horizontal force", math=r"F = 50 - 20 = 30\ \text{N}"),
            S("Use F = ma", math=r"a = \dfrac{F}{m} = \dfrac{30}{6} = 5\ \text{m/s}^2"),
        ]),
        EX("Worked example 2: a car", intro="A car of mass 1200 kg has a resultant forward force of 3000 N. Find its acceleration and the speed after 6 s from rest.", steps=[
            S("Acceleration", math=r"a = \dfrac{3000}{1200} = 2.5\ \text{m/s}^2"),
            S("Speed after 6 s", math=r"v = u + at = 0 + 2.5 \times 6 = 15\ \text{m/s}"),
        ]),
        EX("Worked example 3: finding the mass", intro="A force of 450 N gives a loaded handcart an acceleration of 1.5 m/s². Find the mass of the cart and its load.", steps=[
            S("Rearrange F = ma", math=r"m = \dfrac{F}{a}"),
            S("Substitute", math=r"m = \dfrac{450}{1.5} = 300\ \text{kg}"),
        ]),
        H("Newton's third law"),
        D("**Newton's third law:** if body A exerts a force on body B, then B exerts an equal and opposite force on A.", title="Newton's third law"),
        T("The two forces of a pair are called **action and reaction**. They have the same size, opposite directions, and they are "
          "the same type of force. Most important, they act on **different bodies**, so they never cancel each other."),
        KEY("Examples of action-reaction pairs", "Each pair acts on two different bodies.", cards=[
            ["Swimming", "The swimmer pushes the water backwards. The water pushes the swimmer forwards."],
            ["Walking", "Your foot pushes backwards on the ground. The ground pushes forwards on your foot."],
            ["Rocket", "The rocket pushes hot gas downwards. The gas pushes the rocket upwards."],
        ]),
        MISTAKE("Saying action and reaction cancel each other", "They are equal and opposite, but they act on **different** bodies. Forces cancel only when they act on the **same** body."),
        MISTAKE("Thinking a force is needed to keep an object moving", "An object moving at constant velocity has zero resultant force. A force is needed only to change the velocity (to speed up, slow down or turn)."),
        MISTAKE("Using one of the forces, not the resultant, in F = ma", "In F = ma, F is the resultant force. In worked example 1 it is 50 − 20 = 30 N, not 50 N."),
        QUIZ("A car moves at constant velocity along a straight road. Which statement is true?",
             ["The resultant force is zero", "The engine force is larger than the resistance", "The resultant force is forward", "No forces act on the car"], 0,
             "Constant velocity means zero acceleration, so by the first and second laws the resultant force is zero. The driving force equals the resistive forces.",
             hint="Constant velocity means the acceleration is zero.",
             feedback=["", "If this were true the car would accelerate.", "A forward resultant would make the car accelerate.", "Forces still act: the driving force and the resistance balance each other."]),
        QUIZ("A force of 20 N acts on a body of mass 4 kg. What is its acceleration?",
             ["80 m/s²", "5 m/s²", "0.2 m/s²", "16 m/s²"], 1,
             "a = F ÷ m = 20 ÷ 4 = 5 m/s².",
             hint="Divide force by mass.",
             feedback=["You multiplied force and mass.", "", "You divided mass by force.", "You subtracted the mass from the force."]),
        TIP("Newton's laws appear in Paper 1 and Paper 2. The Board expects the laws to be stated exactly; practise writing them. "
            "In calculations state the resultant force first, then F = ma, then the answer with its unit.", title="Exam link"),
        H("Practice questions"),
        PQ("State Newton's first law of motion. [2 marks]", "A body remains at rest, or moves with constant velocity in a straight line, unless acted on by a resultant (unbalanced) force."),
        PQ("Explain why passengers in a bus lean forward when the bus brakes suddenly. [2 marks]", "The passengers have inertia: they tend to keep moving forward at the bus's original velocity when the bus slows down."),
        PQ("A motorbike of mass 150 kg is driven by a force of 900 N against a resistance of 300 N. Find its acceleration. [3 marks]", "Resultant force = 900 − 300 = 600 N. a = F ÷ m = 600 ÷ 150 = 4 m/s²."),
        PQ("State Newton's third law and give one example. [3 marks]", "If A exerts a force on B, B exerts an equal and opposite force on A. Example: a rocket pushes gas downwards and the gas pushes the rocket upwards."),
        SUM("First law: no resultant force means constant velocity (or rest). Inertia is the reluctance to change motion.",
            r"Second law: $F = ma$, where $F$ is the resultant force. One newton gives 1 kg an acceleration of 1 m/s².",
            "Third law: forces come in equal and opposite pairs that act on two different bodies.",
            "Balanced forces cancel only when they act on the same body.",
            "A force is needed to change velocity, not to keep an object moving at constant velocity."),
    ],
))

# ------------------------------------------------------------------ 12. Weight, mass, resultant forces
LESSONS.append(lesson(
    module=M2,
    topic=T_NEW,
    title="Weight, mass and resultant force problems",
    slug="pha-weight-mass-and-resultant-force",
    minutes=24,
    summary="Weight is the pull of gravity on a mass (W = mg, in newtons). Compare mass and weight, find weight on the Moon, solve lift and car problems with F = ma, and explain terminal velocity.",
    objectives=[
        "Distinguish mass from weight and use W = mg",
        "Explain why weight changes from place to place but mass does not",
        "Solve resultant-force problems for a lift and a car",
        "Explain terminal velocity using balanced forces",
    ],
    key_concepts=["Weight", "Gravitational field strength", "W = mg", "Resultant force", "Friction", "Terminal velocity"],
    blocks=[
        H("Introduction"),
        T("A trader in Bamenda says, 'My sack of rice weighs 50 kilograms.' In everyday speech this is fine. In physics, "
          "'weight' and 'mass' are different quantities. The sack's **mass** is 50 kg. Its **weight** is about 500 newtons. "
          "Mixing them up is one of the commonest mistakes in Physics."),
        D("**Weight** is the force of gravity on an object. It is a vector, measured in newtons (N), and acts towards the centre of the earth.", title="Definition: weight"),
        D("**Gravitational field strength**, $g$, is the force of gravity on each kilogram of mass. On the earth's surface $g = 10$ N/kg "
          "(more exactly 9.8 N/kg). It is the same number as the acceleration of free fall in m/s².", title="Definition: gravitational field strength"),
        F(r"W = mg", title="Weight"),
        CODE("""Quantity   Mass                       Weight
Meaning    amount of matter           force of gravity on the object
Unit       kg                         N
Type       scalar                     vector (acts downwards)
Changes?   same everywhere            depends on g (place)
Measured   balance                    spring balance""", "text", title="Mass and weight compared"),
        H("Weight in different places"),
        T("The mass of an astronaut is the same on the Moon as on the earth. But the Moon's gravity is weaker, about 1.6 N/kg "
          "(check your textbook for the exact value). So her weight is smaller."),
        EX("Worked example 1: weight on the earth and the Moon", intro="A student has mass 60 kg. Find her weight (a) on the earth (g = 10 N/kg), (b) on the Moon (g = 1.6 N/kg).", steps=[
            S("(a) Earth", math=r"W = mg = 60 \times 10 = 600\ \text{N}"),
            S("(b) Moon", math=r"W = 60 \times 1.6 = 96\ \text{N}"),
            S("Mass", text="Her mass is 60 kg in both places."),
        ]),
        EX("Worked example 2: finding mass from weight", intro="A bag of cement has weight 500 N. Find its mass (g = 10 N/kg).", steps=[
            S("Rearrange W = mg", math=r"m = \dfrac{W}{g}"),
            S("Substitute", math=r"m = \dfrac{500}{10} = 50\ \text{kg}"),
        ]),
        H("Resultant force problems"),
        T("The resultant force on an object is the vector sum of all the forces. Use $F = ma$ where $F$ is the resultant. "
          "Draw the forces first, give a direction as positive, then subtract those that point the other way."),
        EX("Worked example 3: a car", intro="A car of mass 1000 kg is driven by an engine force of 4000 N. Friction and air resistance together are 1500 N. Find the acceleration.", steps=[
            S("Resultant force", math=r"F = 4000 - 1500 = 2500\ \text{N}"),
            S("Use F = ma", math=r"a = \dfrac{2500}{1000} = 2.5\ \text{m/s}^2"),
        ]),
        EX("Worked example 4: a person in a lift", intro="A person of mass 60 kg stands on a scale in a lift. Find the reading of the scale (the normal reaction R) when the lift (a) is at rest, (b) accelerates upwards at 2 m/s², (c) accelerates downwards at 2 m/s². Take g = 10 N/kg.", steps=[
            S("Weight of the person", math=r"W = 60 \times 10 = 600\ \text{N}"),
            S("(a) At rest, forces balance", math=r"R = 600\ \text{N}"),
            S("(b) Upwards: resultant upwards = R − W = ma", math=r"R - 600 = 60 \times 2 \Rightarrow R = 720\ \text{N}", text="The person feels heavier."),
            S("(c) Downwards: W − R = ma", math=r"600 - R = 60 \times 2 \Rightarrow R = 480\ \text{N}", text="The person feels lighter."),
        ]),
        H("Terminal velocity"),
        T("A parachutist jumps from a plane. At first the weight is bigger than the air resistance, so she accelerates downwards. "
          "As her speed grows, the air resistance grows too. Eventually the air resistance equals the weight. The forces are balanced, "
          "the resultant force is zero and she falls at a steady speed."),
        D("**Terminal velocity** is the constant (maximum) velocity reached by a falling object when the air resistance equals its weight, so the resultant force is zero.", title="Definition: terminal velocity"),
        T("When the parachute opens, the air resistance suddenly becomes bigger than the weight. She slows down until the air resistance "
          "again equals the weight, at a much smaller terminal velocity."),
        MISTAKE("Using kg as the unit of weight", "Weight is a force and is measured in newtons. The kilogram is the unit of mass. A 60 kg student has a weight of 600 N."),
        MISTAKE("Saying 'weight changes' when the mass changes", "Mass stays the same when you move to another planet. Only the weight changes, because g changes."),
        MISTAKE("Thinking the parachutist stops at terminal velocity", "At terminal velocity the acceleration is zero because the resultant force is zero, but the object keeps moving at a constant velocity."),
        QUIZ("A boy has a mass of 45 kg. What is his weight on the earth (g = 10 N/kg)?",
             ["4.5 N", "45 N", "450 N", "4500 N"], 2,
             "W = mg = 45 × 10 = 450 N.",
             hint="Multiply the mass by g.",
             feedback=["You divided by 10.", "This is the mass number. Weight must include g.", "", "You multiplied by 100."]),
        QUIZ("A parachutist is falling at terminal velocity. Which statement is correct?",
             ["Her weight is greater than the air resistance", "The air resistance is greater than her weight", "Her weight equals the air resistance", "The air resistance is zero"], 2,
             "At terminal velocity the resultant force is zero, so the air resistance upwards equals the weight downwards.",
             hint="Constant velocity means zero resultant force.",
             feedback=["Then she would still be speeding up.", "Then she would be slowing down.", "", "Air resistance is not zero; it has grown until it balances the weight."]),
        TIP("Weight and mass questions are common in Paper 1, and lift or resultant-force calculations appear in Paper 2. "
            "Write W = mg with the unit N. Say which g you use if the question does not give it.", title="Exam link"),
        H("Practice questions"),
        PQ("Distinguish between mass and weight. [3 marks]", "Mass is the amount of matter in a body, in kg, and is the same everywhere. Weight is the force of gravity on the body, in N, and depends on the value of g."),
        PQ("Find the weight of a 2.5 kg bag of sugar (g = 10 N/kg). [2 marks]", "W = mg = 2.5 × 10 = 25 N."),
        PQ("The weight of a rock on the Moon is 80 N. The Moon's g is 1.6 N/kg. Find its mass. [2 marks]", "m = W ÷ g = 80 ÷ 1.6 = 50 kg."),
        PQ("Explain why a parachutist reaches a terminal velocity. [3 marks]", "Air resistance increases as the speed increases. When it becomes equal to her weight, the resultant force is zero, so she stops accelerating and falls at a constant velocity."),
        SUM(r"Weight $W = mg$. It is a force in newtons. Mass is in kilograms and is the same everywhere.",
            "On the earth g = 10 N/kg (or 9.8 N/kg); on the Moon g is about 1.6 N/kg.",
            "For a resultant force, subtract opposing forces and use F = ma.",
            "A person in a lift: accelerating up gives R = m(g + a); accelerating down gives R = m(g − a).",
            "At terminal velocity the air resistance equals the weight and the resultant force is zero."),
    ],
))

# ------------------------------------------------------------------ 13. Momentum and conservation
LESSONS.append(lesson(
    module=M2,
    topic=T_MOM,
    title="Linear momentum and its conservation",
    slug="pha-momentum-and-conservation",
    minutes=24,
    summary="Momentum is mass times velocity. When bodies collide or explode and no outside force acts, the total momentum stays the same. Use this to find velocities after collisions and recoil.",
    objectives=[
        "Define linear momentum and state its unit",
        "State the principle of conservation of momentum",
        "Solve collision problems in which bodies join together or bounce apart",
        "Solve recoil (explosion) problems and distinguish elastic from inelastic collisions",
    ],
    key_concepts=["Momentum", "kg m/s", "Conservation of momentum", "Collision", "Recoil", "Elastic and inelastic"],
    blocks=[
        H("Introduction"),
        T("A loaded truck and a small motorbike both move at 10 m/s. Which is harder to stop? The truck, because it has more mass. "
          "A bullet has a tiny mass but a huge speed, and it is also hard to stop. "
          "Momentum combines mass and velocity into one quantity that measures how hard a moving body is to stop."),
        D("The **linear momentum** of a body is its mass multiplied by its velocity. It is a vector, in the same direction as the velocity. SI unit: kilogram metre per second (kg m/s).",
          title="Definition: linear momentum", formula=r"p = mv"),
        EX("Worked example 1: comparing momentum", intro="Find the momentum of (a) a truck of mass 5000 kg moving at 10 m/s, (b) a bullet of mass 0.02 kg moving at 300 m/s.", steps=[
            S("(a) Truck", math=r"p = 5000 \times 10 = 50\,000\ \text{kg m/s}"),
            S("(b) Bullet", math=r"p = 0.02 \times 300 = 6\ \text{kg m/s}"),
        ]),
        H("Conservation of momentum"),
        D("The **principle of conservation of momentum:** when two or more bodies act on each other (for example in a collision), "
          "their **total momentum stays constant**, provided that no external (outside) force acts on them.", title="Principle of conservation of momentum",
          formula=r"\text{total momentum before} = \text{total momentum after}"),
        T("Why does this work? By Newton's third law, when body A pushes body B, B pushes back on A with an equal and opposite force "
          "for the same time. A gains as much momentum as B loses. The total does not change."),
        KEY("Sign convention", "Momentum is a vector. In one straight line, give one direction a plus sign.", cards=[
            ["Right is positive", "A body moving to the right has positive momentum. One moving to the left has negative momentum."],
            ["A body at rest", "Momentum zero, since v = 0."],
        ]),
        H("Collisions"),
        IMG("f5ph-a-trolleys.svg", alt="Before the collision a 2 kg trolley moves right at 3 m/s towards a 1 kg trolley at rest. After the collision they join and move as one 3 kg trolley with unknown speed v.",
            caption="Figure 1. A collision in which the trolleys stick together."),
        EX("Worked example 2: trolleys stick together", intro="In Figure 1 a 2 kg trolley moving at 3 m/s hits a 1 kg trolley at rest. They join together. Find their common velocity.", steps=[
            S("Momentum before (right positive)", math=r"2 \times 3 + 1 \times 0 = 6\ \text{kg m/s}"),
            S("Momentum after: the combined mass is 3 kg", math=r"(2 + 1)v = 3v"),
            S("Equate", math=r"3v = 6 \Rightarrow v = 2\ \text{m/s}"),
        ], check=r"\text{After: } 3 \times 2 = 6\ \text{kg m/s} = \text{before}"),
        EX("Worked example 3: opposite directions", intro="A 3 kg trolley moving right at 4 m/s collides head-on with a 1 kg trolley moving left at 2 m/s. They stick together. Find their velocity.", steps=[
            S("Momentum before (right positive)", math=r"3 \times 4 + 1 \times (-2) = 12 - 2 = 10\ \text{kg m/s}"),
            S("Momentum after", math=r"(3 + 1)v = 4v"),
            S("Equate", math=r"4v = 10 \Rightarrow v = 2.5\ \text{m/s to the right}"),
        ]),
        T("In an **elastic collision** both momentum and kinetic energy (energy of motion) are conserved, and the bodies bounce apart. "
          "In an **inelastic collision** momentum is still conserved, but some kinetic energy changes to heat and sound. "
          "When the bodies stick together, as in worked example 2, the collision is inelastic."),
        T(r"Check with kinetic energy $\tfrac{1}{2}mv^2$. In example 2: before, $\tfrac{1}{2}(2)(3^2) = 9$ J. After, $\tfrac{1}{2}(3)(2^2) = 6$ J. 3 J has changed into other forms of energy."),
        H("Explosions and recoil"),
        T("Before a gun is fired, the gun and bullet are both at rest, so the total momentum is zero. After firing, the total must still be zero. "
          "The bullet has momentum forwards, so the gun has an equal momentum backwards. This is **recoil**."),
        EX("Worked example 4: recoil of a gun", intro="A gun of mass 4 kg fires a bullet of mass 0.02 kg at 300 m/s. Find the recoil velocity of the gun.", steps=[
            S("Total momentum before", math=r"0"),
            S("Momentum after (bullet direction positive)", math=r"0.02 \times 300 + 4v = 6 + 4v"),
            S("Equate to zero", math=r"6 + 4v = 0 \Rightarrow v = -1.5\ \text{m/s}", text="The gun recoils at 1.5 m/s, opposite to the bullet."),
        ]),
        MISTAKE("Forgetting the signs", "A body moving in the opposite direction has negative momentum. In example 3 the 1 kg trolley contributes −2 kg m/s."),
        MISTAKE("Using the mass of only one body after joining", "If the bodies stick together, use the **sum** of the masses after the collision."),
        MISTAKE("Saying momentum is conserved only in elastic collisions", "Momentum is conserved in every collision with no external force. Only kinetic energy is lost in an inelastic one."),
        QUIZ("What is the momentum of a 0.5 kg ball moving at 8 m/s?",
             ["16 kg m/s", "4 kg m/s", "8.5 kg m/s", "0.0625 kg m/s"], 1,
             "p = mv = 0.5 × 8 = 4 kg m/s.",
             hint="Multiply mass by velocity.",
             feedback=["You doubled instead of halving: 2 × 8.", "", "You added mass and velocity.", "You divided mass by velocity."]),
        QUIZ("A 2 kg trolley at 4 m/s hits a stationary 2 kg trolley and they stick. What is their speed after the collision?",
             ["8 m/s", "4 m/s", "2 m/s", "1 m/s"], 2,
             "Momentum before = 2 × 4 = 8 kg m/s. After: (2 + 2)v = 8, so v = 2 m/s.",
             hint="Total momentum before equals total momentum after, with both masses moving together.",
             feedback=["8 is the momentum in kg m/s, not the velocity. Divide it by the total mass.", "The speed would stay 4 m/s only if the mass did not increase. The momentum is shared by 4 kg.", "", "You divided the momentum by 8 instead of by the total mass 4 kg."]),
        TIP("Conservation of momentum is a standard Paper 2 calculation and often appears in Paper 1. Define momentum with its unit, "
            "state the principle with the condition 'no external force', and write the momentum before and after as two lines.", title="Exam link"),
        H("Practice questions"),
        PQ("State the principle of conservation of momentum. [2 marks]", "When bodies interact, the total momentum before equals the total momentum after, provided no external force acts on them."),
        PQ("A 1500 kg car moving at 12 m/s hits the back of a 1000 kg stationary car and they move off together. Find their velocity. [3 marks]", "Before: 1500 × 12 = 18 000 kg m/s. After: (1500 + 1000)v = 2500v. So v = 18 000 ÷ 2500 = 7.2 m/s."),
        PQ("A boy and his trolley have a combined mass of 80 kg after he throws forward a 4 kg bag at 5 m/s. Everything starts at rest. Find the recoil velocity of the boy and trolley. [3 marks]", "Momentum after = 0: 4 × 5 + 80v = 0, so v = −20 ÷ 80 = −0.25 m/s. They move backwards at 0.25 m/s."),
        PQ("Explain what happens to the momentum and the kinetic energy in an inelastic collision. [2 marks]", "The total momentum is conserved. Some kinetic energy is changed into other forms such as heat and sound."),
        SUM(r"Momentum $p = mv$, a vector, in kg m/s.",
            "In any collision or explosion, total momentum is conserved if no external force acts.",
            "Give one direction a positive sign. A body at rest has zero momentum.",
            "When bodies stick together, use the combined mass after the collision.",
            "Recoil: the total momentum after a gun fires is still zero, so the gun moves back.",
            "In an elastic collision kinetic energy is conserved too; in an inelastic collision it is not."),
    ],
))

# ------------------------------------------------------------------ 14. Impulse
LESSONS.append(lesson(
    module=M2,
    topic=T_MOM,
    title="Impulse and the force in a collision",
    slug="pha-impulse-and-force",
    minutes=24,
    summary="Impulse is force times the time it acts, and it equals the change in momentum. Use it to find average forces, read the area of a force-time graph, and explain seat belts, crumple zones and bending your knees.",
    objectives=[
        "Define impulse and state its units",
        "Use impulse = F t = change in momentum",
        "Find impulse from the area under a force-time graph",
        "Explain how a longer collision time reduces the force",
    ],
    key_concepts=["Impulse", "N s", "Change in momentum", "Force-time graph", "Average force", "Safety features"],
    blocks=[
        H("Introduction"),
        T("A goalkeeper at a school match in Bertoua catches a fast ball. If she keeps her hands stiff, the ball hurts. If she pulls "
          "her hands back as she catches it, it hurts much less. The ball loses the same momentum in both cases. "
          "What changes is the **time** over which it stops."),
        H("Impulse"),
        D("**Impulse** is the product of a force and the time for which it acts. Its unit is the newton second (N s). "
          "It is a vector in the direction of the force.", title="Definition: impulse", formula=r"\text{impulse} = F \times t"),
        T(r"Newton's second law says $F = ma$. Put $a = \dfrac{v - u}{t}$. Then $F = \dfrac{m(v - u)}{t}$, so $Ft = mv - mu$."),
        KEY("Impulse equals change in momentum", "The impulse on a body is equal to its change in momentum.", cards=[
            [r"$Ft = mv - mu$", "Impulse = final momentum − initial momentum"],
            [r"$F = \dfrac{mv - mu}{t}$", "Force = rate of change of momentum"],
        ], note="1 N s = 1 kg m/s. Both units describe the same quantity."),
        EX("Worked example 1: a kicked ball", intro="A footballer kicks a stationary ball of mass 0.4 kg. The kick lasts 0.02 s with an average force of 400 N. Find the impulse and the speed of the ball.", steps=[
            S("Impulse", math=r"Ft = 400 \times 0.02 = 8\ \text{N s}"),
            S("Impulse = mv − mu, with u = 0", math=r"8 = 0.4v - 0 \Rightarrow v = 20\ \text{m/s}"),
        ]),
        H("The force-time graph"),
        T("When a force changes while it acts, we cannot use $Ft$ directly. Draw a graph of force against time. "
          "The **area under the graph** is the impulse."),
        IMG("f5ph-a-impulse.svg", alt="Force-time graph of a kick. The force rises in a straight line from 0 to 800 N at 0.01 s then falls to 0 at 0.02 s. The triangle underneath is shaded.",
            caption="Figure 1. The area under a force-time graph is the impulse."),
        EX("Worked example 2: area under a force-time graph", intro="Use Figure 1 to find the impulse. The ball has mass 0.4 kg and starts at rest. Find its speed.", steps=[
            S("Area of the triangle", math=r"\tfrac{1}{2} \times 0.02 \times 800 = 8\ \text{N s}"),
            S("Impulse = change in momentum", math=r"8 = 0.4v \Rightarrow v = 20\ \text{m/s}"),
        ]),
        H("Reducing the force"),
        T("For a given change in momentum, the force is smaller if the time is longer. $F = \\dfrac{\\Delta p}{t}$."),
        EX("Worked example 3: catching a ball", intro="A goalkeeper catches a 0.5 kg ball moving at 12 m/s and stops it. Find the average force if (a) the stop takes 0.02 s with stiff hands, (b) it takes 0.1 s when she draws her hands back.", steps=[
            S("Change in momentum", math=r"mv - mu = 0 - 0.5 \times 12 = -6\ \text{kg m/s}", text="The size is 6 kg m/s."),
            S("(a) Stiff hands", math=r"F = \dfrac{6}{0.02} = 300\ \text{N}"),
            S("(b) Hands drawn back", math=r"F = \dfrac{6}{0.1} = 60\ \text{N}", text="The same momentum change, but five times the time gives one fifth of the force."),
        ]),
        EX("Worked example 4: a ball bouncing off a wall", intro="A 0.5 kg ball hits a wall at 10 m/s and rebounds at 6 m/s. The contact lasts 0.02 s. Find the impulse and the average force. Take the direction towards the wall as positive.", steps=[
            S("Initial momentum", math=r"mu = 0.5 \times 10 = +5\ \text{kg m/s}"),
            S("Final momentum (reversed direction)", math=r"mv = 0.5 \times (-6) = -3\ \text{kg m/s}"),
            S("Change in momentum", math=r"-3 - 5 = -8\ \text{kg m/s}", text="The impulse on the ball has size 8 N s, directed away from the wall."),
            S("Average force", math=r"F = \dfrac{8}{0.02} = 400\ \text{N}"),
        ]),
        KEY("Safety uses of a long stopping time", "Making the collision last longer reduces the force.", cards=[
            ["Seat belts and airbags", "They stretch or inflate, so the person stops over a longer time and feels a smaller force."],
            ["Crumple zones", "The front of a car folds in a crash, which increases the time of the collision."],
            ["Bending the knees", "A person landing from a jump bends the knees to stop over a longer time."],
        ]),
        MISTAKE("Ignoring the direction of a rebound", "When a ball bounces back, the final velocity has the opposite sign. The change in momentum is then larger than in a case where the ball just stops."),
        MISTAKE("Using grams", "Change the mass to kilograms. 400 g is 0.4 kg."),
        MISTAKE("Saying a seat belt reduces the momentum change", "The change in momentum is the same with or without a seat belt. The belt makes the **time** longer, so the **force** is smaller."),
        QUIZ("What is the impulse of a force of 50 N acting for 0.2 s?",
             ["10 N s", "250 N s", "0.004 N s", "50.2 N s"], 0,
             "Impulse = Ft = 50 × 0.2 = 10 N s.",
             hint="Multiply the force by the time.",
             feedback=["", "You divided 50 by 0.2.", "You divided 0.2 by 50.", "You added the two numbers."]),
        QUIZ("Why does a car's crumple zone reduce injuries?",
             ["It reduces the change in momentum of the passengers", "It increases the time of the collision, so the force is smaller", "It increases the mass of the car", "It makes the car stop in a shorter time"], 1,
             "The change in momentum is fixed by the speed. A longer collision time gives a smaller average force: F = Δp ÷ t.",
             hint="For the same change in momentum, what happens to the force when the time grows?",
             feedback=["The change in momentum is the same. Only the time changes.", "", "The crumple zone does not add mass.", "A shorter time would increase the force."]),
        TIP("Impulse and momentum questions appear in Paper 1 and Paper 2. Explaining safety features is a favourite: always say that the "
            "**time** increases and the **force** decreases for the same change in momentum.", title="Exam link"),
        H("Practice questions"),
        PQ("Define impulse and state its SI unit. [2 marks]", "Impulse is the force multiplied by the time for which it acts. Its SI unit is the newton second (N s)."),
        PQ("A force of 200 N acts on a 2 kg trolley for 0.5 s. The trolley starts from rest. Find its final velocity. [3 marks]", "Impulse = Ft = 200 × 0.5 = 100 N s. This equals mv, so v = 100 ÷ 2 = 50 m/s."),
        PQ("A 1000 kg car travelling at 15 m/s stops in 0.3 s in a crash. Find the average force on the car. [3 marks]", "Change in momentum = 1000 × 15 = 15 000 kg m/s. F = 15 000 ÷ 0.3 = 50 000 N."),
        PQ("Explain why a high-jumper bends her knees on landing. [2 marks]", "Bending her knees makes the time to stop longer. For the same change in momentum, the average force on her is smaller."),
        SUM("Impulse = force × time, measured in N s. It equals the change in momentum, $mv - mu$.",
            r"Average force $F = \dfrac{mv - mu}{t}$, the rate of change of momentum.",
            "The area under a force-time graph is the impulse.",
            "A longer collision time gives a smaller force for the same change of momentum.",
            "Seat belts, airbags, crumple zones and bending the knees all lengthen the time of the stop.",
            "A rebound reverses the sign of the final momentum."),
    ],
))

# ------------------------------------------------------------------ 15. Moments
LESSONS.append(lesson(
    module=M2,
    topic=T_MOMENTS,
    title="Moments and the principle of moments",
    slug="pha-moments-and-equilibrium",
    minutes=25,
    summary="The moment of a force is force times the perpendicular distance from the pivot. In equilibrium, clockwise moments equal anticlockwise moments. Solve see-saw, beam and spanner problems with units.",
    objectives=[
        "Define the moment of a force and state its unit",
        "State the principle of moments",
        "Solve problems on balanced beams, including a uniform beam with its weight at the centre",
        "State the two conditions for equilibrium",
    ],
    key_concepts=["Moment", "Pivot", "Perpendicular distance", "Principle of moments", "Equilibrium", "N m"],
    blocks=[
        H("Introduction"),
        T("It is easy to open a door by pushing near the handle, and hard to open it by pushing close to the hinges. "
          "A long spanner loosens a stubborn nut that a short spanner cannot. In both cases the **turning effect** of a force depends "
          "not only on the force but also on how far from the turning point it acts."),
        D("The **moment** of a force about a point is the force multiplied by the **perpendicular distance** from the point to the line of action of the force. "
          "The point is called the **pivot**. SI unit: newton metre (N m).", title="Definition: moment of a force", formula=r"\text{moment} = F \times d"),
        T("Moments are **clockwise** or **anticlockwise**, depending on which way they would turn the object. "
          "A see-saw tips one way if the clockwise moment is bigger, and the other way if the anticlockwise moment is bigger."),
        EX("Worked example 1: a spanner", intro="A mechanic pulls with a force of 40 N at the end of a spanner, 0.25 m from the centre of the nut. Find the moment. What force is needed at a distance of 0.5 m to give the same moment?", steps=[
            S("Moment", math=r"M = F \times d = 40 \times 0.25 = 10\ \text{N m}"),
            S("Same moment at 0.5 m", math=r"F = \dfrac{M}{d} = \dfrac{10}{0.5} = 20\ \text{N}", text="A longer spanner needs a smaller force."),
        ]),
        H("The principle of moments"),
        D("**The principle of moments:** when a body is in equilibrium, the sum of the clockwise moments about any point is equal to the sum of the anticlockwise moments about the same point.",
          title="Principle of moments", formula=r"\text{sum of clockwise moments} = \text{sum of anticlockwise moments}"),
        D("A body is in **equilibrium** when there is no resultant force and no resultant moment on it. It does not accelerate and it does not start turning.", title="Definition: equilibrium"),
        KEY("Two conditions for equilibrium", "Both must be true.", cards=[
            ["1. Forces", "The upward forces equal the downward forces (the resultant force is zero)."],
            ["2. Moments", "The clockwise moment equals the anticlockwise moment about any point."],
        ]),
        IMG("f5ph-a-beam-seesaw.svg", alt="A light plank balanced on a central pivot. A 200 N force acts downward 0.6 m to the left of the pivot and an unknown force F acts downward 0.4 m to the right.",
            caption="Figure 1. A light plank balanced on a pivot."),
        EX("Worked example 2: a balanced plank", intro="In Figure 1 the plank is balanced and its own weight can be ignored. Find the force F.", steps=[
            S("Anticlockwise moment about the pivot (the 200 N force on the left)", math=r"200 \times 0.6 = 120\ \text{N m}"),
            S("Clockwise moment (F on the right)", math=r"F \times 0.4"),
            S("Principle of moments", math=r"F \times 0.4 = 120 \Rightarrow F = 300\ \text{N}"),
        ], check=r"300 \times 0.4 = 120\ \text{N m}"),
        H("A uniform beam"),
        T("A **uniform** beam has the same thickness and material all along. Its weight acts at its **centre**. "
          "In a diagram, draw the weight arrow down from the middle of the beam. The pivot also pushes **upwards** on the beam, "
          "with a force called the **reaction** R."),
        IMG("f5ph-a-beam-uniform.svg", alt="A uniform 4 m plank pivoted 0.5 m from its left end. A load X acts down at the left end, the plank weight of 60 N acts down at its centre 1.5 m from the pivot, and the pivot reaction R acts upward.",
            caption="Figure 2. A uniform plank of weight 60 N balanced on a pivot."),
        EX("Worked example 3: a uniform plank", intro="The uniform plank in Figure 2 is 4.0 m long, with weight 60 N, and is balanced on a pivot 0.5 m from the left end by a load X at the left end. Find X and the reaction R.", steps=[
            S("Weight acts at the centre", text="The centre is 2.0 m from the left end, which is 1.5 m from the pivot."),
            S("Clockwise moment (weight, to the right of the pivot)", math=r"60 \times 1.5 = 90\ \text{N m}"),
            S("Anticlockwise moment (load, to the left of the pivot)", math=r"X \times 0.5"),
            S("Principle of moments", math=r"X \times 0.5 = 90 \Rightarrow X = 180\ \text{N}"),
            S("Upward force = downward forces", math=r"R = X + W = 180 + 60 = 240\ \text{N}"),
        ]),
        EX("Worked example 4: two children on a see-saw", intro="A girl of weight 300 N sits 1.5 m from the pivot of a see-saw. Where must her brother of weight 360 N sit on the other side to balance it?", steps=[
            S("Girl's moment", math=r"300 \times 1.5 = 450\ \text{N m}"),
            S("Brother's moment must be equal", math=r"360 \times d = 450"),
            S("Solve", math=r"d = \dfrac{450}{360} = 1.25\ \text{m}", text="The heavier brother sits closer to the pivot."),
        ]),
        MISTAKE("Using the wrong distance", "The distance must be measured **at right angles** to the line of the force, from the pivot. A slanting measurement gives the wrong moment."),
        MISTAKE("Forgetting the weight of the beam", "A uniform beam's own weight acts at its centre. If the beam is not pivoted at its centre, its weight gives a moment."),
        MISTAKE("Writing N instead of N m", "Moments have unit N m, not N. The Board's examiners report that many candidates also leave out the reaction at the pivot or draw the weight of a uniform object at the wrong point."),
        QUIZ("A force of 30 N acts at right angles to a spanner at 0.4 m from the nut. What is the moment?",
             ["12 N m", "75 N m", "30.4 N m", "0.013 N m"], 0,
             "Moment = F × d = 30 × 0.4 = 12 N m.",
             hint="Moment is force times perpendicular distance.",
             feedback=["", "You divided 30 by 0.4.", "You added the two numbers.", "You divided 0.4 by 30."]),
        QUIZ("A uniform metre rule is balanced at its 50 cm mark. A 4 N weight is hung at the 20 cm mark. At which mark must a 6 N weight be hung to balance it?",
             ["60 cm", "70 cm", "75 cm", "80 cm"], 1,
             "The 4 N weight is 30 cm from the pivot: 4 × 30 = 120 N cm. 6 × d = 120, so d = 20 cm from the pivot, which is at the 70 cm mark.",
             hint="Find the distance from the pivot first, then add it to the pivot position.",
             feedback=["This is only 10 cm from the pivot, so the moment would be 60 N cm, which is too small.", "", "This is 25 cm from the pivot, so the moment would be 150 N cm, which is too big.", "This is 30 cm from the pivot, the same as the 4 N weight. That would balance only if both weights were equal."]),
        TIP("Moments are a frequent Paper 2 question. The Board's examiners report that candidates often fail to draw the forces as arrows, to put the weight of a uniform object at its centre, to draw the upward reaction at the pivot, and to use the principle of moments correctly. "
            "Draw a clear force diagram first and give N m as the unit.", title="Exam link"),
        H("Practice questions"),
        PQ("Define the moment of a force about a point. [2 marks]", "The moment of a force is the force multiplied by the perpendicular distance from the pivot to the line of action of the force."),
        PQ("State the principle of moments. [2 marks]", "For a body in equilibrium, the sum of the clockwise moments about any point equals the sum of the anticlockwise moments about that point."),
        PQ("A uniform beam of weight 80 N and length 2 m is pivoted at its centre. A 50 N weight is hung 0.8 m from the pivot on one side. Where must a 40 N weight be placed on the other side to balance it? [3 marks]", "The beam's own weight acts at the pivot, so it has no moment. 50 × 0.8 = 40 N m. 40 × d = 40, so d = 1.0 m from the pivot, on the other side."),
        PQ("A crowbar is used to lift a stone. The effort of 120 N acts 1.5 m from the pivot. The stone is 0.3 m from the pivot. Find the force on the stone. [3 marks]", "Clockwise = anticlockwise: 120 × 1.5 = F × 0.3, so F = 180 ÷ 0.3 = 600 N."),
        SUM("Moment = force × perpendicular distance from the pivot, in N m.",
            "Principle of moments: in equilibrium, total clockwise moment = total anticlockwise moment.",
            "Equilibrium needs zero resultant force and zero resultant moment.",
            "The weight of a uniform beam acts at its centre. The pivot pushes upwards with a reaction R.",
            "A longer lever arm needs a smaller force for the same moment."),
    ],
))

# ------------------------------------------------------------------ 16. Centre of gravity and stability
LESSONS.append(lesson(
    module=M2,
    topic=T_MOMENTS,
    title="Centre of gravity and stability",
    slug="pha-centre-of-gravity-and-stability",
    minutes=24,
    summary="The centre of gravity is the point where the whole weight of a body seems to act. Find it for a flat card with a plumb line, use it in moments problems, and explain why a low centre of gravity and a wide base make a body stable.",
    objectives=[
        "Define the centre of gravity and state where it is for a uniform regular object",
        "Describe how to find the centre of gravity of an irregular flat card",
        "Use the centre of gravity in a moments problem with a metre rule",
        "Explain stable, unstable and neutral equilibrium, and what makes a body topple",
    ],
    key_concepts=["Centre of gravity", "Plumb line", "Stable equilibrium", "Unstable equilibrium", "Neutral equilibrium", "Base area"],
    blocks=[
        H("Introduction"),
        T("A boy in Kumba balances a long stick on one finger. He moves his finger until the stick stays level. "
          "At that spot the stick's whole weight seems to act. This special point is the **centre of gravity**."),
        D("The **centre of gravity** of a body is the point through which the whole weight of the body appears to act.", title="Definition: centre of gravity"),
        T("Every small part of a body is pulled down by gravity. We can replace all those small weights by one single weight acting at one point, the centre of gravity."),
        KEY("Where is the centre of gravity?", "For a **uniform** object of regular shape it is at the geometric centre.", cards=[
            ["Metre rule or uniform rod", "At the middle of its length."],
            ["Rectangular or square sheet", "Where the diagonals cross."],
            ["Circular disc or sphere", "At the centre."],
        ], note="For an irregular shape, or one with different materials in different places, the centre of gravity may be off-centre. It can even be outside the object, as in a ring."),
        H("Finding the centre of gravity of an irregular card"),
        KEY("The plumb line method", "Use a pin, a plumb line (a thread with a small weight) and a pencil.", cards=[
            ["1. Make holes", "Make three small holes near the edge of the card."],
            ["2. Hang the card", "Hang the card freely from a pin through one hole. Hang the plumb line from the same pin."],
            ["3. Mark the line", "When everything is still, mark the line of the thread on the card with the pencil."],
            ["4. Repeat", "Do the same with the other holes. The lines cross at the centre of gravity."],
        ], note="When the card hangs freely, its centre of gravity is directly below the pin. That is why the plumb line passes through it."),
        IMG("f5ph-a-cog.svg", alt="An irregular card with three holes A, B and C. Dashed lines from each hole cross at one point G, the centre of gravity.",
            caption="Figure 1. The three lines meet at the centre of gravity G."),
        T("Two lines are enough. The third line checks the result: if all three cross at one point, the work is accurate."),
        H("Using the centre of gravity in moments"),
        EX("Worked example 1: a metre rule", intro="A uniform metre rule of weight 1.0 N is balanced on a pivot at the 30 cm mark. A load is hung at the 5 cm mark. Find the weight of the load and its mass (g = 10 N/kg).", steps=[
            S("The rule's weight acts at its centre", text="The centre is at the 50 cm mark, which is 20 cm to the right of the pivot."),
            S("Clockwise moment (rule's weight)", math=r"1.0 \times 20 = 20\ \text{N cm}"),
            S("The load at 5 cm is 25 cm to the left of the pivot", math=r"W \times 25 = 20"),
            S("Solve", math=r"W = \dfrac{20}{25} = 0.8\ \text{N}"),
            S("Mass of the load", math=r"m = \dfrac{W}{g} = \dfrac{0.8}{10} = 0.08\ \text{kg} = 80\ \text{g}"),
        ]),
        H("Stability"),
        T("Why does a bus overloaded with luggage on the roof sometimes topple on a bend, while an empty one does not? The answer is stability."),
        CODE("""Type of equilibrium   What happens after a small push        Example
stable                it returns to its position           a ball in a bowl
unstable              it moves further away and falls      a pencil standing on its tip
neutral               it stays in its new position         a ball on a flat table""", "text", title="Three kinds of equilibrium"),
        KEY("What makes a body stable", "Two things help.", cards=[
            ["A low centre of gravity", "The body must be tilted a long way before the centre of gravity moves outside the base."],
            ["A wide base", "A larger base area makes it harder for the weight line to fall outside it."],
        ], note="This is why racing cars are low and wide, and why a heavy load should be placed low in a lorry."),
        IMG("f5ph-a-stability.svg", alt="Two tilted blocks. In the left block the vertical line down from the centre of gravity G falls inside the base, so it falls back. In the right block the line falls outside the base, so it topples.",
            caption="Figure 2. A body falls back if the vertical line through G falls inside the base. It topples if the line falls outside."),
        D("A tilted body **topples** when the vertical line through its centre of gravity falls **outside** its base. "
          "While the line is inside the base, the weight gives a moment that brings the body back.", title="Rule for toppling"),
        EX("Worked example 2: a bus on a sloping road", intro="A minibus has a wheel base (width) 1.6 m. Its centre of gravity is 1.0 m above the ground, midway between the wheels. Find the angle of tilt at which it begins to topple. What happens if luggage on the roof raises the centre of gravity to 1.4 m? (This worked example goes slightly beyond the blueprint; check your textbook.)", steps=[
            S("The bus topples when the vertical through G passes over the wheel on the low side", text="Half the base width is 0.8 m."),
            S("Use the triangle", math=r"\tan\theta = \dfrac{0.8}{1.0} = 0.8 \Rightarrow \theta = 38.7^\circ"),
            S("With luggage on the roof, the centre of gravity is at 1.4 m", math=r"\tan\theta = \dfrac{0.8}{1.4} = 0.571 \Rightarrow \theta = 29.7^\circ"),
            S("Conclusion", text="A higher centre of gravity makes the bus topple at a smaller angle of tilt. This is why overloaded roof racks are dangerous."),
        ]),
        MISTAKE("Saying the centre of gravity is always at the middle", "It is at the middle only for a uniform regular body. A hammer's centre of gravity is near its heavy head."),
        MISTAKE("Saying a heavy body is more stable", "Stability depends on the **position** of the centre of gravity and the **size of the base**, not on the weight alone."),
        MISTAKE("Forgetting the weight of the rule", "In a metre rule problem the rule's own weight acts at the 50 cm mark. Include its moment if the pivot is not at 50 cm."),
        QUIZ("Where is the centre of gravity of a uniform rectangular card?",
             ["At one corner", "Where the diagonals cross", "At the middle of a long edge", "Outside the card"], 1,
             "For a uniform rectangle it is at the geometric centre, where the diagonals meet.",
             hint="Think of balancing the card on a pin.",
             feedback=["A pin at a corner would not balance the card.", "", "This point would not balance the card.", "This is true only for shapes such as a ring."]),
        QUIZ("Which change makes a bus more stable?",
             ["Loading heavy goods on the roof", "Making the base narrower", "Placing heavy goods on the floor", "Raising the seats"], 2,
             "A heavy load on the floor lowers the centre of gravity. A lower centre of gravity means more stability.",
             hint="Stability improves with a lower centre of gravity and a wider base.",
             feedback=["This raises the centre of gravity.", "A narrower base makes it easier to topple.", "", "This raises the centre of gravity."]),
        TIP("Centre of gravity and stability questions appear in Paper 1 and as parts of the moments questions in Paper 2. The Board's examiners "
            "report that candidates often fail to recognise that the weight of a uniform object acts at its centre. For stability, always give two reasons: low centre of gravity and wide base.", title="Exam link"),
        H("Practice questions"),
        PQ("Define the centre of gravity of a body. [1 mark]", "The centre of gravity is the point through which the whole weight of the body appears to act."),
        PQ("Describe how to find the centre of gravity of an irregular piece of card. [4 marks]", "Make three holes near the edge. Hang the card from a pin through one hole with a plumb line from the pin. Mark the line of the thread on the card. Repeat with the other holes. The lines cross at the centre of gravity."),
        PQ("A uniform metre rule of weight 2 N is balanced on a pivot at the 40 cm mark by a load at the 10 cm mark. Find the weight of the load. [3 marks]", "The rule's weight acts at 50 cm, which is 10 cm from the pivot: 2 × 10 = 20 N cm. The load is 30 cm from the pivot: W × 30 = 20, so W = 0.67 N."),
        PQ("Give two reasons why a racing car is stable. [2 marks]", "It has a low centre of gravity, and a wide base."),
        SUM("The centre of gravity is the point where the whole weight of a body seems to act.",
            "For a uniform regular body it is at the geometric centre.",
            "Use a plumb line and three holes to find it for an irregular card.",
            "In moments problems, a uniform rule's weight acts at the 50 cm mark.",
            "A body is more stable with a low centre of gravity and a wide base.",
            "A tilted body topples when the vertical line through its centre of gravity falls outside its base."),
    ],
))
