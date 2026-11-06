"""Form 5 Biology: Transport, Excretion & Homeostasis and Coordination, Response & Locomotion.
14 lessons, one practice set each. Standard O Level facts; points where textbooks differ are marked 'check your textbook'.
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "form-5")

M1 = "Transport, Excretion & Homeostasis"
T_PLANT = "Transport in plants"
T_BLOOD = "Mammalian blood"
T_HEART = "The heart, blood vessels and lymphatic system"
T_KIDNEY = "Excretion and the kidney"
T_OSMO = "Osmoregulation, the liver and the skin"
M2 = "Coordination, Response & Locomotion"
T_RESP = "Plant responses"
T_NERV = "The human nervous system"
T_SENSE = "The eye and the ear"
T_ENDO = "The endocrine system"
T_SKEL = "The skeleton, joints and muscles"

LESSONS = []

# ------------------------------------------------------------------ 1. Water uptake and transpiration
LESSONS.append(lesson(
    module=M1, topic=T_PLANT,
    title="Water uptake, the xylem and transpiration",
    slug="bic-water-uptake-and-transpiration",
    minutes=22,
    summary="How root hairs take in water and mineral ions, how the xylem carries them up the plant, what transpiration is, what speeds it up, and why plants need it.",
    objectives=[
        "Describe how root hair cells take in water and mineral ions",
        "Describe the structure and function of the xylem",
        "Define transpiration and explain how the transpiration pull moves water upwards",
        "Explain how light, temperature, wind and humidity affect the rate of transpiration",
    ],
    key_concepts=["Root hair cell", "Osmosis", "Active transport", "Xylem", "Transpiration", "Transpiration pull", "Stomata", "Wilting"],
    blocks=[
        H("Introduction"),
        T("A farmer in Bafia plants cassava. At midday under the hot sun the leaves hang down and look dead. By evening, "
          "after the heat has gone, they stand up again. The plant has not been watered. What changed? The answer lies in how "
          "water moves through a plant."),
        T("A plant is mostly water. It takes water from the soil with its roots and carries it to every leaf. This lesson "
          "explains how it is done and why a hot, dry, windy day makes a plant lose water faster."),
        D("**Transport** in a plant is the movement of water, mineral ions and food from one part of the plant to another.",
          title="Definition: transport in plants"),
        H("Root hairs take in water and ions"),
        T("The tip of a young root is covered with tiny hairs. Each one is a **root hair cell**. It is a single cell with a long, "
          "thin extension that pushes between the soil particles."),
        KEY("Adaptations of a root hair cell", "Each feature helps the cell absorb more water and ions.", cards=[
            ["Long, thin extension", "Gives a very large surface area for absorbing water and ions."],
            ["Thin cell wall", "Water and ions can pass through quickly."],
            ["Cell sap with many dissolved substances", "The sap is more concentrated than the soil water, so water enters by osmosis."],
            ["Many mitochondria", "They release energy by respiration for active transport of mineral ions."],
        ]),
        D("**Osmosis** is the movement of water molecules from a region of high water concentration (a dilute solution) to a region of "
          "low water concentration (a concentrated solution) through a partially permeable membrane.", title="Definition: osmosis"),
        T("Water enters the root hair by osmosis. It then passes from cell to cell across the root (the cortex) until it reaches the xylem. "
          "Mineral ions, such as nitrate, are often more concentrated inside the root than in the soil. The root hair takes them in by "
          "**active transport**, which uses energy from respiration, against the concentration gradient."),
        TIP("Remember the two jobs. Water goes in by osmosis (no energy needed). Mineral ions go in mainly by active transport "
            "(energy needed). A waterlogged soil has little oxygen, so roots cannot respire well and take in fewer ions."),
        H("The xylem"),
        D("**Xylem** vessels are long, hollow tubes made of dead cells with no end walls. Their walls are thickened with lignin. "
          "They carry water and mineral ions upwards from the roots to the leaves and also support the plant.", title="Definition: xylem"),
        T("Xylem vessels join end to end, so a continuous column of water runs from the root to the leaf. The lignin makes the tubes "
          "strong. This is why wood, which is made of old xylem, is hard."),
        H("Transpiration"),
        D("**Transpiration** is the loss of water vapour from the aerial parts of a plant, mainly through the stomata of the leaves.",
          title="Definition: transpiration"),
        T("Inside a leaf, water evaporates from the wet walls of the mesophyll cells into the air spaces. The water vapour then "
          "diffuses out through the open **stomata** (small pores, mostly on the lower surface of the leaf) into the drier air outside."),
        CODE("""
Soil water
  -> root hair (osmosis)
  -> cortex cells
  -> xylem in root
  -> xylem in stem
  -> xylem in leaf
  -> mesophyll cell walls
  -> air spaces in leaf (evaporation)
  -> stomata (diffusion of water vapour)
  -> air outside
""", "text", title="The path of water through a plant"),
        KEY("What pulls water up a tall plant?", "Three ideas work together.", cards=[
            ["Transpiration pull", "Water leaving the leaf by evaporation pulls more water up the xylem behind it."],
            ["Cohesion", "Water molecules stick to each other, so the column of water does not break."],
            ["Adhesion", "Water molecules also stick to the walls of the narrow xylem, which helps hold the column up."],
        ]),
        T("Some textbooks also mention **root pressure** (a push from the roots, important only for small plants and at night) and "
          "**capillarity** (water rising in very narrow tubes). Check your textbook for how much weight your teacher gives them. "
          "In tall trees, the transpiration pull is the main force."),
        H("What changes the rate of transpiration?"),
        CODE("""
Factor            Effect on rate     Why
Light (brighter)  increases          stomata open wider
Temperature (up)  increases          faster evaporation
Wind (stronger)   increases          removes the moist air
Humidity (higher) decreases          air is already wet
""", "text", title="Factors affecting transpiration"),
        QUIZ("Which condition gives the fastest rate of transpiration?",
             ["A cool, still, humid day", "A hot, windy, dry day", "A cool, windy, humid night", "A hot, still, humid evening"], 1,
             "Heat speeds up evaporation, wind carries away water vapour near the leaf and dry air takes up more vapour.",
             hint="Which conditions dry washing quickly on a line?",
             feedback=["Cool, still and humid conditions slow evaporation and diffusion.", "",
                       "At night most stomata are closed and the humid air slows the loss further.",
                       "Humid air already holds much water vapour, so less leaves the leaf."]),
        H("Why transpiration matters"),
        KEY("Uses of transpiration", "It is not just a loss of water.", cards=[
            ["Pulls water and ions up", "It drives the flow of water and dissolved minerals from the roots."],
            ["Cools the leaf", "Evaporation takes heat from the leaf, like sweating."],
            ["Supplies water", "Water arrives for photosynthesis and keeps cells firm (turgid)."],
        ]),
        T("If a plant loses water faster than the roots can supply it, the cells lose turgor and the plant **wilts**, as the cassava did at "
          "midday. The stomata also close to save water."),
        EX("Worked example 1: why the cassava wilted", intro="Explain why cassava leaves wilt at midday and recover in the evening.", steps=[
            S("Say what is different at midday", text="It is hot, bright and often dry, so transpiration is very fast."),
            S("Compare loss and uptake", text="Water leaves the leaves faster than the roots can supply it."),
            S("Link to the cells", text="The leaf cells lose water and become flaccid (soft), so the leaf droops."),
            S("Explain the recovery", text="In the evening it is cooler and the stomata close. Water uptake catches up and the cells become turgid again."),
        ]),
        EX("Worked example 2: follow a water molecule", intro="List in order the structures that a water molecule passes through from the soil to the air.", steps=[
            S("Enter the plant", text="Root hair cell, by osmosis."),
            S("Cross the root", text="Cortex cells, then the xylem."),
            S("Travel upwards", text="Xylem of the root, stem and leaf."),
            S("Leave the plant", text="Mesophyll cell walls (evaporation), air spaces, stomata (diffusion), then the air."),
        ]),
        MISTAKE("Saying the xylem carries food", "Food (sugars) travels in the **phloem**. The xylem carries water and mineral ions upwards. "
                "Examiners often see the two swapped."),
        MISTAKE("Confusing transpiration with evaporation", "Evaporation happens from the wet cell walls inside the leaf. Transpiration is the whole process "
                "of water vapour leaving the plant. Define it as loss of water vapour from the aerial parts, mainly through stomata."),
        QUIZ("Which feature of a root hair cell helps it absorb water?",
             ["A thick waxy cuticle", "A long extension that gives a large surface area", "Many chloroplasts", "A cell wall made of lignin"], 1,
             "The long, thin extension increases the surface area for absorption.",
             hint="Think about why a big surface area helps any absorbing cell.",
             feedback=["A waxy cuticle stops water entering, it is found on leaves.", "",
                       "Root hairs are underground and do not photosynthesise.", "Lignin is in xylem walls and would make water entry harder."]),
        TIP("Exam link: Paper 1 (multiple choice) asks about the parts of the root hair cell, the xylem and the factors that change transpiration. "
            "Paper 2 can ask you to describe how water moves from the soil to the atmosphere. Spell xylem, osmosis and transpiration correctly.",
            title="Exam link"),
        PQ("Define transpiration.", "Transpiration is the loss of water vapour from the aerial parts of a plant, mainly through the stomata of the leaves."),
        PQ("Describe how a root hair cell is adapted to take in water and mineral ions.",
           "It has a long, thin extension with a large surface area and a thin wall. Its cell sap is more concentrated than the soil water, so water enters by osmosis. "
           "It has many mitochondria that supply energy for active transport of mineral ions."),
        PQ("Describe how water moves from the soil to a leaf and out into the air.",
           "Water enters the root hair by osmosis, crosses the cortex to the xylem and moves up the xylem to the leaf. It evaporates from the mesophyll cell walls "
           "into the air spaces and diffuses out through the stomata. The transpiration pull and the cohesion of water molecules keep the column moving."),
        PQ("Explain why a plant is more likely to wilt on a hot, windy day.",
           "Heat and wind make transpiration faster, so the leaves lose water faster than the roots can supply it. The cells lose turgor and the plant wilts."),
        SUM("Root hair cells absorb water by osmosis and mineral ions mainly by active transport.",
            "The xylem is a set of dead, hollow, lignified tubes that carry water and mineral ions upwards.",
            "Transpiration is the loss of water vapour from the aerial parts of a plant, mainly through stomata.",
            "The transpiration pull, with the cohesion of water molecules, moves water up the xylem.",
            "Light, heat and wind increase transpiration and high humidity reduces it.",
            "Transpiration pulls water up, cools the leaf and supplies water, but too much causes wilting."),
    ],
))

# ------------------------------------------------------------------ 2. Translocation and the potometer
LESSONS.append(lesson(
    module=M1, topic=T_PLANT,
    title="Translocation in the phloem and the potometer",
    slug="bic-translocation-and-the-potometer",
    minutes=22,
    summary="How the phloem carries sugars and amino acids from the leaves to where they are used or stored, how a ringing experiment shows it, and how a potometer measures water uptake.",
    objectives=[
        "Describe the structure of phloem and what translocation carries",
        "Explain the ringing (girdling) experiment",
        "Describe the potometer and the precautions needed when using it",
        "Calculate the rate of water uptake from potometer readings",
    ],
    key_concepts=["Phloem", "Sieve tube", "Companion cell", "Translocation", "Source and sink", "Potometer", "Rate of uptake"],
    blocks=[
        H("Introduction"),
        T("When you cut a sugar cane in a farm near Mbandjock, the juice is sweet. The sugar was made in the leaves and carried down into the stem to be stored. "
          "Moving food around the plant is called translocation. In the second half of this lesson you will also learn to measure how fast a plant takes in water."),
        D("**Translocation** is the movement of organic food substances (mainly sucrose and amino acids) in the phloem from where they are made or "
          "stored to where they are needed.", title="Definition: translocation"),
        H("The phloem"),
        T("The phloem is made of living cells. **Sieve tube cells** are joined end to end. The end walls have small holes and are called sieve plates. "
          "Each sieve tube cell has very little cytoplasm and no nucleus. Next to each one is a **companion cell**, which has a nucleus and many "
          "mitochondria and supplies the energy the sieve tube needs."),
        KEY("Xylem and phloem compared", "Learn the differences.", cards=[
            ["Xylem", "Dead, hollow, lignified tubes. Carries water and mineral ions. One direction only: upwards. Also gives support."],
            ["Phloem", "Living sieve tubes with companion cells. Carries sucrose and amino acids. Moves both up and down, from source to sink."],
        ]),
        T("A **source** is a part that makes or releases food, such as a green leaf or a storage root that is sprouting. A **sink** is a part that uses or stores "
          "food, such as a growing root tip, a young leaf, a fruit or a yam tuber. Translocation is an active process and needs energy, "
          "supplied by the companion cells."),
        T("Sugars are carried as **sucrose** because it dissolves well and is not very reactive. When it arrives at a sink it is changed into starch for storage "
          "or used in respiration."),
        H("Showing translocation: ringing a stem"),
        T("In a ringing (girdling) experiment, a ring of bark is cut from a woody stem. The ring removes the phloem but leaves the xylem in the middle."),
        CODE("""
Before:        After some weeks:
  leaves         leaves (healthy)
    |              |
  stem           stem swells ABOVE the ring
    |            [ring: bark removed]
  stem           stem BELOW the ring does not grow
    |              |
  roots          roots may starve
""", "text", title="The ringing experiment"),
        T("The leaves stay healthy because the xylem still brings water. Sugars made in the leaves cannot pass the ring, so they build up and the stem "
          "swells **above** the ring. Below the ring the stem and roots get no sugar and slowly die. The experiment shows that sugars travel down through the "
          "phloem, which lies in the bark."),
        QUIZ("In a ringing experiment, where does the stem swell and why?",
             ["Below the ring, because water cannot leave", "Above the ring, because sugars cannot pass downwards", "Above the ring, because water cannot pass upwards", "Below the ring, because sugars are made there"], 1,
             "The phloem is cut, so sucrose from the leaves piles up above the ring and the tissue swells.",
             hint="Which tube was removed, and what did it carry?",
             feedback=["Water goes up in the xylem, which was not removed.", "",
                       "Water continues to pass up the xylem, which is not cut.", "Sugars are made in the leaves, which are above the ring."]),
        MISTAKE("Saying the ringing experiment removes the xylem", "The ring of bark contains the phloem. The xylem is deeper, in the wood, and stays in place, so water still rises."),
        H("The potometer"),
        T("A **potometer** measures how fast a leafy shoot takes in water. Because almost all the water taken in is lost by transpiration, the rate of "
          "uptake is a good estimate of the rate of transpiration."),
        IMG("f5bi-c-potometer.svg", alt="A potometer: a leafy shoot in a bung joined to a water-filled tube and a horizontal capillary tube with an air bubble and a scale",
            caption="Figure 1. A potometer. As the shoot takes in water, the air bubble moves towards the shoot along the scale."),
        KEY("Setting up a potometer", "Follow the precautions.", cards=[
            ["Cut the shoot under water", "This stops air entering the xylem and breaking the water column."],
            ["Make every joint airtight", "Smear petroleum jelly round the bung. Air leaks would give false readings."],
            ["Keep the leaves dry", "Water drops on the leaf would block the stomata."],
            ["Introduce one air bubble", "Take the end out of water for a moment, then put it back. Record the start position."],
            ["Change one factor only", "For example, switch on a fan. Keep light and temperature the same."],
        ]),
        F(r"\text{rate of uptake} = \frac{\text{distance moved by the bubble}}{\text{time taken}}"),
        T("To find the **volume** of water taken up, treat the capillary tube as a cylinder. Its volume is the cross-section area times the distance moved."),
        F(r"V = \pi r^2 d"),
        EX("Worked example 1: rate of bubble movement", intro="In a potometer the bubble moves 45 mm in 15 minutes. Find the rate of movement.", steps=[
            S("Write the formula", math=r"\text{rate} = \frac{\text{distance}}{\text{time}}"),
            S("Substitute", math=r"\text{rate} = \frac{45\ \text{mm}}{15\ \text{min}}"),
            S("Calculate", math=r"\text{rate} = 3\ \text{mm per minute}"),
        ]),
        EX("Worked example 2: volume of water taken up", intro="The capillary tube has a radius of 0.5 mm. The bubble moves 30 mm in 5 minutes. Find the volume of water taken up and the rate in mm$^3$ per minute. Use $\\pi = 3.14$.", steps=[
            S("Volume of the cylinder", math=r"V = \pi r^2 d = 3.14 \times 0.5^2 \times 30"),
            S("Calculate", math=r"V = 3.14 \times 0.25 \times 30 = 23.55\ \text{mm}^3"),
            S("Divide by the time", math=r"\text{rate} = \frac{23.55}{5} = 4.71\ \text{mm}^3\text{ per minute}"),
        ]),
        TIP("A potometer measures water **uptake**. Some water is used in photosynthesis or kept in the cells, so uptake is slightly more than transpiration. "
            "Say 'rate of water uptake, an estimate of the rate of transpiration' in an exam answer."),
        QUIZ("Why must a shoot be cut under water when setting up a potometer?",
             ["To make it grow faster", "To stop air entering the xylem and breaking the water column", "To make the leaves wet", "To close the stomata"], 1,
             "An air bubble in the xylem breaks the continuous water column, and the shoot cannot draw up water.",
             hint="Think about the continuous column of water in the xylem.",
             feedback=["Cutting under water does not change the growth.", "",
                       "Wet leaves would block the stomata and give wrong results.", "Stomata are not controlled by cutting the stem under water."]),
        TIP("Exam link: Paper 1 often shows a potometer or a ringed stem and asks what you would observe or why a step is needed. Paper 2 may ask you to describe an "
            "experiment to compare the rate of transpiration in two conditions.", title="Exam link"),
        PQ("Name two substances carried in the phloem.", "Sucrose and amino acids."),
        PQ("Describe how companion cells help sieve tubes.", "Companion cells have a nucleus and many mitochondria. They supply energy for the movement of food in the sieve tubes, which have little cytoplasm and no nucleus."),
        PQ("A bubble in a potometer moves 36 mm in 12 minutes. Calculate the rate of movement.", "Rate = distance / time = 36 mm / 12 min = 3 mm per minute."),
        PQ("Describe an experiment using a potometer to show that wind increases the rate of water uptake.",
           "Set up the potometer with a leafy shoot cut under water and airtight joints. Record how far the bubble moves in five minutes in still air. Reset the bubble, then blow a fan at the shoot "
           "and record the distance in the same time, keeping light and temperature the same. The bubble moves further in wind, so uptake and transpiration are faster."),
        SUM("Translocation is the movement of sucrose and amino acids in the phloem, from sources to sinks, and needs energy.",
            "Phloem has living sieve tubes with sieve plates and companion cells. Xylem is dead, lignified and carries water upwards.",
            "The ringing experiment shows that food moves down in the phloem: the stem swells above the ring.",
            "A potometer measures the rate of water uptake, an estimate of the rate of transpiration.",
            "Rate = distance moved by the bubble divided by time. Volume = pi r squared times distance.",
            "Cut the shoot under water, keep joints airtight, leaves dry and change one factor at a time."),
    ],
))

# ------------------------------------------------------------------ 3. Blood composition and functions
LESSONS.append(lesson(
    module=M1, topic=T_BLOOD,
    title="What blood is made of and what it does",
    slug="bic-blood-composition-and-functions",
    minutes=22,
    summary="The four parts of blood (plasma, red cells, white cells and platelets), how each is built for its job, and the main functions of blood in transport, defence and regulation.",
    objectives=[
        "Name the components of mammalian blood",
        "Describe how red blood cells are adapted to carry oxygen",
        "Distinguish phagocytes from lymphocytes",
        "State the functions of plasma, red cells, white cells and platelets",
    ],
    key_concepts=["Plasma", "Red blood cell", "Haemoglobin", "Oxyhaemoglobin", "White blood cell", "Phagocyte", "Lymphocyte", "Platelet"],
    blocks=[
        H("Introduction"),
        T("At a hospital in Douala a nurse asks for blood donors. A small sample is taken and spun in a machine. It separates into a pale yellow liquid on top and a "
          "red layer at the bottom. Blood looks like one red liquid, but it is really a mixture of a liquid and several kinds of cells."),
        D("**Blood** is a red liquid tissue that flows round the body in the blood vessels. It is made of **plasma** and three kinds of cell parts: "
          "red blood cells, white blood cells and platelets.", title="Definition: blood"),
        H("Plasma"),
        T("**Plasma** is the pale yellow liquid part of blood. It is about 90% water. Many substances are dissolved in it and carried round the body."),
        KEY("What plasma carries", "The plasma is the transport liquid of the body.", cards=[
            ["Digested food", "Glucose, amino acids, vitamins and mineral ions from the gut to the cells."],
            ["Waste", "Urea from the liver to the kidneys. Carbon dioxide, mostly as hydrogencarbonate ions, to the lungs."],
            ["Hormones", "Chemical messengers from glands to target organs."],
            ["Plasma proteins", "These include fibrinogen, which is used in clotting."],
            ["Heat", "Heat made in muscles and the liver is spread round the body."],
        ]),
        H("Red blood cells"),
        D("**Red blood cells** (erythrocytes) are small, disc-shaped cells with no nucleus that contain **haemoglobin**. They carry oxygen from the lungs "
          "to the body cells.", title="Definition: red blood cell"),
        T("**Haemoglobin** is a red protein that contains iron. In the lungs, where there is a lot of oxygen, haemoglobin joins with oxygen to form "
          "**oxyhaemoglobin**, which is bright red. In the tissues, where oxygen is scarce, oxyhaemoglobin releases its oxygen and turns back into haemoglobin."),
        F(r"\text{haemoglobin} + \text{oxygen} \rightleftharpoons \text{oxyhaemoglobin}"),
        KEY("How a red blood cell is adapted", "Every feature helps it carry oxygen.", cards=[
            ["Biconcave disc shape", "A large surface area for the diffusion of oxygen. It is also flexible and can squeeze into narrow capillaries."],
            ["No nucleus", "More room for haemoglobin, so each cell carries more oxygen."],
            ["Full of haemoglobin", "Carries the oxygen."],
            ["Very small and numerous", "Many cells give a large total surface area."],
        ]),
        T("Red cells are made in the **red bone marrow** of bones such as the ribs, the sternum, the vertebrae and the ends of long bones. They live for about four months. "
          "Old cells are destroyed in the liver and the spleen."),
        H("White blood cells and platelets"),
        D("**White blood cells** (leucocytes) are larger than red cells, have a nucleus and protect the body against disease-causing microorganisms.", title="Definition: white blood cell"),
        KEY("Two kinds of white cell", "Both defend the body in different ways.", cards=[
            ["Phagocytes", "Have a lobed nucleus. They move out of the capillaries, engulf and digest bacteria. This is **phagocytosis**."],
            ["Lymphocytes", "Have a large, round nucleus. They make **antibodies**, proteins that attach to microbes and help to destroy them."],
        ]),
        D("**Platelets** are tiny fragments of cells with no nucleus. They help blood to clot when a vessel is damaged.", title="Definition: platelet"),
        CODE("""
Part          Nucleus?  Main job
Plasma        -         carries dissolved substances
Red cell      no        carries oxygen
Phagocyte     yes       engulfs microbes
Lymphocyte    yes       makes antibodies
Platelet      no        helps blood to clot
""", "text", title="Summary of the parts of blood"),
        H("Functions of blood"),
        KEY("What blood does for the body", "Learn three headings.", cards=[
            ["Transport", "Oxygen, carbon dioxide, food, urea, hormones and heat."],
            ["Protection", "Phagocytosis, antibodies and clotting."],
            ["Regulation", "Spreads heat, helping to keep the temperature steady, and helps to keep the water and pH of the body steady."],
        ]),
        EX("Worked example 1: name the cell", intro="Name the blood cell described: it is small, has no nucleus, is a biconcave disc and is full of a red pigment.", steps=[
            S("Check the nucleus", text="No nucleus, so it is not a white cell."),
            S("Check the shape and pigment", text="A biconcave disc with a red pigment (haemoglobin)."),
            S("Name it", text="It is a red blood cell (erythrocyte). Its job is to carry oxygen."),
        ]),
        EX("Worked example 2: explain a feature", intro="Explain why a red blood cell has no nucleus.", steps=[
            S("State the feature", text="Mature red blood cells have no nucleus."),
            S("Link to the space", text="This leaves more room inside the cell for haemoglobin."),
            S("Link to the function", text="More haemoglobin means that each cell can carry more oxygen."),
        ]),
        MISTAKE("Saying that white cells carry oxygen", "Only red cells carry oxygen, because only they contain haemoglobin. White cells defend the body."),
        MISTAKE("Saying that red cells have a nucleus", "Mature mammalian red blood cells have none. This is a favourite exam point."),
        QUIZ("Which part of the blood makes antibodies?",
             ["Red blood cells", "Platelets", "Lymphocytes", "Plasma"], 2,
             "Lymphocytes make antibodies that help to destroy microbes.",
             hint="Antibodies are made by a kind of white cell.",
             feedback=["Red cells carry oxygen.", "Platelets help clotting.", "", "Plasma carries dissolved substances. The cells make antibodies."]),
        QUIZ("What happens to haemoglobin in the lungs?",
             ["It releases carbon dioxide only", "It joins with oxygen to form oxyhaemoglobin", "It joins with urea", "It is destroyed"], 1,
             "In the lungs the oxygen level is high, so haemoglobin combines with oxygen.",
             hint="Which gas is plentiful in the lungs?",
             feedback=["Most carbon dioxide travels in the plasma, not on haemoglobin.", "",
                       "Urea is carried in the plasma.", "Haemoglobin is not destroyed. It is reused."]),
        TIP("Exam link: Paper 1 (multiple choice) may show a drawing of blood cells and ask you to name one, or ask which component does a job. Paper 2 can ask you to compare "
            "red and white cells. Spell phagocytosis, haemoglobin and lymphocyte correctly.", title="Exam link"),
        PQ("Name the four components of blood.", "Plasma, red blood cells, white blood cells and platelets."),
        PQ("State two ways in which a red blood cell is adapted to carry oxygen.",
           "It is a biconcave disc, which gives a large surface area for diffusion. It has no nucleus, so there is more room for haemoglobin. It contains haemoglobin, which combines with oxygen."),
        PQ("Describe the difference between a phagocyte and a lymphocyte.",
           "A phagocyte has a lobed nucleus and engulfs and digests bacteria (phagocytosis). A lymphocyte has a large round nucleus and makes antibodies."),
        PQ("List four substances carried in the plasma.", "Any four of: glucose, amino acids, mineral ions, urea, carbon dioxide (as hydrogencarbonate), hormones, plasma proteins, vitamins, heat."),
        SUM("Blood is made of plasma, red cells, white cells and platelets.",
            "Plasma is about 90% water and carries dissolved food, waste, hormones and heat.",
            "Red cells are biconcave discs with no nucleus, full of haemoglobin, and carry oxygen as oxyhaemoglobin.",
            "Phagocytes engulf microbes. Lymphocytes make antibodies.",
            "Platelets help blood to clot.",
            "Blood transports, protects and helps to regulate the body."),
    ],
))

# ------------------------------------------------------------------ 4. Blood groups and clotting
LESSONS.append(lesson(
    module=M1, topic=T_BLOOD,
    title="Blood groups, transfusion and blood clotting",
    slug="bic-blood-groups-and-clotting",
    minutes=24,
    summary="The ABO blood groups and the Rhesus factor, which transfusions are safe, and how a blood clot forms (thromboplastin, thrombin and fibrin).",
    objectives=[
        "State the antigens and antibodies of the ABO groups",
        "Work out which blood groups can safely be given to which",
        "Explain the Rhesus factor in simple terms",
        "Describe how blood clotting happens and why it matters",
    ],
    key_concepts=["Antigen", "Antibody", "ABO groups", "Agglutination", "Universal donor", "Rhesus factor", "Blood clotting", "Fibrin"],
    blocks=[
        H("Introduction"),
        T("After a road accident near Bamenda, a driver has lost a lot of blood. At the hospital the first thing the laboratory does is test his blood group. "
          "Giving the wrong blood can kill, so every transfusion is matched. In this lesson you learn why."),
        D("An **antigen** is a substance on the surface of a cell that the body can recognise as belonging to it or as foreign. "
          "An **antibody** is a protein, made by lymphocytes, that attaches to a particular antigen.", title="Definitions: antigen and antibody"),
        H("The ABO groups"),
        T("There are four blood groups: A, B, AB and O. Your group depends on the antigens on the surface of your red blood cells and the antibodies in your plasma. "
          "You never carry antibodies against your own antigens."),
        CODE("""
Group  Antigen on red cell  Antibody in plasma
A      A                    anti-B
B      B                    anti-A
AB     A and B              none
O      none                 anti-A and anti-B
""", "text", title="The ABO blood groups"),
        T("If blood is given to a person who has the matching antibody, the antibody attaches to the foreign red cells and they stick together in clumps. "
          "This is called **agglutination**. The clumps can block small blood vessels and cause death."),
        KEY("Who can give blood to whom?", "A donor's red cells must not carry an antigen that the recipient has an antibody against.", cards=[
            ["Group O", "No antigens on the red cells, so it can be given to everyone. It is the **universal donor**."],
            ["Group AB", "No antibodies in the plasma, so a person can receive any group. It is the **universal recipient**."],
            ["Group A", "Can give to A and AB. Can receive from A and O."],
            ["Group B", "Can give to B and AB. Can receive from B and O."],
        ]),
        CODE("""
Donor   Can safely give to
O       O, A, B, AB
A       A, AB
B       B, AB
AB      AB
""", "text", title="Safe transfusions"),
        TIP("Do not memorise blindly. Ask: does the donor red cell have an antigen that the recipient's plasma has an antibody for? If yes, the blood clumps."),
        EX("Worked example 1: is the transfusion safe?", intro="Can a person of group B safely receive blood from a group A donor?", steps=[
            S("Write down the donor's antigen", text="Group A red cells carry antigen A."),
            S("Write down the recipient's antibody", text="Group B plasma contains anti-A antibodies."),
            S("Compare", text="Anti-A will attach to antigen A, so the donor cells will clump."),
            S("Conclude", text="It is not safe."),
        ]),
        EX("Worked example 2: another transfusion", intro="Can a person of group AB safely receive blood from a group O donor?", steps=[
            S("Donor antigens", text="Group O cells have no antigens."),
            S("Recipient antibodies", text="Group AB plasma has no antibodies."),
            S("Conclude", text="Nothing can clump, so it is safe. (The donor's antibodies are so diluted in the recipient's larger volume of blood that they do not harm.)"),
        ]),
        MISTAKE("Mixing up the universal donor and recipient", "Group O is the universal **donor** (no antigens). Group AB is the universal **recipient** (no antibodies). "
                "Check each time with the antigen and antibody rule."),
        QUIZ("A person of group O needs a transfusion. Which donor groups are safe for this person?",
             ["A only", "AB only", "O only", "A, B and AB"], 2,
             "Group O plasma has anti-A and anti-B antibodies, so the donor cells must carry neither antigen. Only group O blood is safe.",
             hint="What antibodies does group O plasma contain?",
             feedback=["Group A cells carry antigen A, and anti-A would attack them.", "AB cells carry both antigens, so both antibodies would attack.", "",
                       "All of these carry A or B antigens, so they would be attacked."]),
        H("The Rhesus factor"),
        T("Another antigen on red cells is the **Rhesus factor**. A person who has it is **Rhesus positive** (Rh+). A person who does not is **Rhesus negative** (Rh-). "
          "A Rh- person does not have Rhesus antibodies at first, but makes them if Rh+ blood enters the body."),
        T("This matters in pregnancy. If a Rh- mother carries a Rh+ baby, some of the baby's blood may enter her blood at birth. She may then make antibodies that harm a later Rh+ baby. "
          "Doctors can give the mother an injection to prevent this. Check your textbook for how much detail you need."),
        H("Blood clotting"),
        D("**Blood clotting** is the change of liquid blood into a solid clot when a blood vessel is damaged. The clot stops loss of blood and keeps out microbes.", title="Definition: clotting"),
        CODE("""
Damaged tissue and platelets release thromboplastin
        |   (with calcium ions and vitamin K)
        v
prothrombin (inactive)  ->  thrombin (enzyme)
        |
        v
fibrinogen (soluble)    ->  fibrin (insoluble threads)
        |
        v
fibrin mesh traps red cells  =  clot  ->  scab
""", "text", title="Steps in blood clotting"),
        T("The fibrin threads make a net across the wound. Red blood cells and platelets are trapped in the net, and the clot dries into a hard **scab**. "
          "Under the scab the skin heals. Vitamin K is needed by the liver to make prothrombin, and calcium ions help the reaction."),
        T("In **haemophilia**, an inherited condition, blood does not clot properly because a clotting factor is missing, so even small cuts bleed for a long time. "
          "A clot that forms inside a healthy vessel is called a **thrombosis** and can block the flow of blood."),
        MISTAKE("Writing 'clothing' for clotting", "The Board's report notes that some candidates write 'clothing' for clotting. Clotting is the word for blood becoming a solid clot."),
        QUIZ("Which protein forms the threads that make up a blood clot?",
             ["Haemoglobin", "Fibrin", "Thrombin", "Antibody"], 1,
             "Soluble fibrinogen is changed into insoluble fibrin by thrombin. The fibrin threads form the net of the clot.",
             hint="It is made from fibrinogen.",
             feedback=["Haemoglobin is in red cells and carries oxygen.", "", "Thrombin is the enzyme that makes fibrin. It is not the threads.", "Antibodies attach to microbes."]),
        TIP("Exam link: Paper 1 (multiple choice) tests which donors are safe and the order of clotting steps. Paper 2 can ask you to describe how a clot forms and why clotting is important. "
            "Write the names in order: thromboplastin, thrombin, fibrin.", title="Exam link"),
        PQ("State the antigens and antibodies present in a person of blood group A.", "The red cells carry antigen A and the plasma contains anti-B antibodies."),
        PQ("Explain why a person of group A should not be given group B blood.",
           "Group B red cells carry antigen B. Group A plasma contains anti-B antibodies, which attach to the antigen and make the red cells clump (agglutinate). The clumps can block vessels."),
        PQ("Why is group O called the universal donor?", "Its red cells have no A or B antigens, so no antibody in a recipient's plasma can attach to them."),
        PQ("Describe how a blood clot forms.",
           "Damaged tissue and platelets release thromboplastin. With calcium ions this changes prothrombin into the enzyme thrombin. Thrombin changes soluble fibrinogen into insoluble fibrin threads. "
           "The threads trap red cells to make a clot that dries to a scab."),
        SUM("Blood groups A, B, AB and O depend on the antigens on red cells and the antibodies in plasma.",
            "Group O is the universal donor (no antigens). Group AB is the universal recipient (no antibodies).",
            "A transfusion is unsafe if the donor's antigen meets a matching antibody: the red cells agglutinate.",
            "Rhesus positive people have the Rhesus antigen. A Rh- mother and a Rh+ baby need care.",
            "Clotting: thromboplastin, then prothrombin to thrombin, then fibrinogen to fibrin and a clot.",
            "Clotting stops blood loss and keeps out microbes. Haemophilia is a failure to clot."),
    ],
))

# ------------------------------------------------------------------ 5. The heart and the cardiac cycle
LESSONS.append(lesson(
    module=M1, topic=T_HEART,
    title="The structure of the heart and the cardiac cycle",
    slug="bic-the-heart-and-the-cardiac-cycle",
    minutes=25,
    summary="The four chambers, valves and vessels of the mammalian heart, the double circulation, the stages of the cardiac cycle, the heart sounds, pulse and cardiac output.",
    objectives=[
        "Name and locate the chambers, valves and main vessels of the heart",
        "Trace the path of blood through the heart and the double circulation",
        "Describe the stages of the cardiac cycle and the action of the valves",
        "Calculate heart rate from a pulse count and cardiac output",
    ],
    key_concepts=["Atrium", "Ventricle", "Tricuspid valve", "Bicuspid valve", "Semilunar valve", "Double circulation", "Cardiac cycle", "Pulse", "Cardiac output"],
    blocks=[
        H("Introduction"),
        T("Put two fingers on your wrist. The beat you feel is your pulse. It was made by your heart, a muscular pump about the size of your fist that has been beating "
          "since before you were born and never rests. In this lesson you will see how it is built and how it works."),
        D("The **heart** is a muscular organ made of cardiac muscle that pumps blood round the body. It is supplied with blood by the **coronary arteries**.", title="Definition: heart"),
        H("Structure of the heart"),
        IMG("f5bi-c-heart.svg", alt="Section through the heart showing the right atrium and right ventricle on the left of the picture, the left atrium and thicker left ventricle on the right, the septum, valves and main vessels",
            caption="Figure 1. A section through the heart as seen from the front. The right side of the heart is on the left of the picture."),
        KEY("The four chambers", "The heart has two sides, separated by the **septum**. Each side has two chambers.", cards=[
            ["Right atrium", "Receives deoxygenated blood from the body through the vena cava."],
            ["Right ventricle", "Pumps deoxygenated blood to the lungs through the pulmonary artery."],
            ["Left atrium", "Receives oxygenated blood from the lungs through the pulmonary vein."],
            ["Left ventricle", "Pumps oxygenated blood to the whole body through the aorta. It has the thickest wall."],
        ]),
        T("The **atria** have thin walls because they only push blood a short distance into the ventricles. The **ventricles** have thick, muscular walls. "
          "The left ventricle is the thickest because it must push blood all round the body at high pressure. The right ventricle only has to reach the nearby lungs."),
        KEY("The valves", "Valves let blood flow in one direction only.", cards=[
            ["Tricuspid valve", "Between the right atrium and the right ventricle. It has three flaps."],
            ["Bicuspid valve", "Between the left atrium and the left ventricle. It has two flaps."],
            ["Semilunar valves", "At the start of the aorta and the pulmonary artery. They have cup-shaped (half-moon) flaps. They stop blood falling back into the ventricles."],
            ["Tendons", "Strong 'heart strings' that stop the flaps of the tricuspid and bicuspid valves from turning inside out when the ventricles contract."],
        ]),
        MISTAKE("Thinking all arteries carry oxygenated blood", "The **pulmonary artery** carries deoxygenated blood to the lungs. The **pulmonary vein** carries oxygenated blood to the heart. "
                "Arteries carry blood **away** from the heart and veins carry it **towards** the heart."),
        H("The double circulation"),
        T("Blood passes through the heart **twice** on every complete trip round the body. This is the **double circulation**. One loop goes to the lungs. "
          "The other goes to the rest of the body. The heart is a double pump."),
        CODE("""
Body
 -> vena cava
 -> RIGHT ATRIUM
 -> (tricuspid valve)
 -> RIGHT VENTRICLE
 -> (semilunar valve)
 -> pulmonary artery
 -> LUNGS (oxygen in, carbon dioxide out)
 -> pulmonary vein
 -> LEFT ATRIUM
 -> (bicuspid valve)
 -> LEFT VENTRICLE
 -> (semilunar valve)
 -> aorta
 -> Body
""", "text", title="The path of blood through the heart"),
        QUIZ("Which chamber of the heart receives oxygenated blood from the lungs?",
             ["Right atrium", "Right ventricle", "Left atrium", "Left ventricle"], 2,
             "The pulmonary veins bring oxygenated blood from the lungs into the left atrium.",
             hint="Oxygenated blood is on the left side of the heart.",
             feedback=["The right atrium receives deoxygenated blood from the body.", "The right ventricle pumps blood to the lungs.", "",
                       "The left ventricle pumps blood out, it does not receive it from the lungs."]),
        H("The cardiac cycle"),
        D("The **cardiac cycle** is the sequence of contraction and relaxation of the heart chambers during one heartbeat. "
          "Contraction is called **systole** and relaxation is called **diastole**.", title="Definition: cardiac cycle"),
        CODE("""
1 Atria fill with blood (heart relaxed).
2 Atria contract (atrial systole).
  Blood is pushed through the open tricuspid
  and bicuspid valves into the ventricles.
3 Ventricles contract (ventricular systole).
  The tricuspid and bicuspid valves SHUT.
  The semilunar valves OPEN.
  Blood leaves by the aorta and pulmonary artery.
4 Ventricles relax.
  The semilunar valves SHUT.
  Blood flows into the atria again.
""", "text", title="Stages of one heartbeat"),
        T("At rest, one cycle takes about 0.8 seconds. The sounds of the heart are 'lub, dub'. The 'lub' is the tricuspid and bicuspid valves closing. "
          "The 'dub' is the semilunar valves closing."),
        T("The **pulse** is the wave of stretch that passes along an artery each time the left ventricle pumps. You can count it at the wrist. "
          "The **heart rate** is the number of beats per minute. It rises in exercise because the muscles need more oxygen. A resting adult has a rate of about 70 beats per minute."),
        F(r"\text{cardiac output} = \text{stroke volume} \times \text{heart rate}"),
        T("The **stroke volume** is the volume of blood pushed out of one ventricle in one beat. The **cardiac output** is the volume pumped out of one ventricle in one minute."),
        EX("Worked example 1: heart rate", intro="A student counts 18 pulses in 15 seconds. Calculate her heart rate in beats per minute.", steps=[
            S("Find how many 15-second periods are in a minute", math=r"60 \div 15 = 4"),
            S("Multiply", math=r"18 \times 4 = 72"),
            S("State the answer", text="The heart rate is 72 beats per minute."),
        ]),
        EX("Worked example 2: cardiac output", intro="The stroke volume is 70 cm$^3$ and the heart rate is 72 beats per minute. Calculate the cardiac output.", steps=[
            S("Write the formula", math=r"\text{cardiac output} = \text{stroke volume} \times \text{heart rate}"),
            S("Substitute", math=r"70 \times 72 = 5040"),
            S("State the answer with units", text="The cardiac output is 5040 cm³ per minute, which is about 5.0 dm³ per minute."),
        ]),
        MISTAKE("Mixing up the valves", "Tricuspid has three flaps and is on the **right** side. Bicuspid has two flaps and is on the **left**. Memory trick: tRIcuspid goes with RIght."),
        MISTAKE("Misspelling the valves", "The Board's report notes that some candidates write 'similuma valve'. The correct term is **semilunar valve**. Learn the spelling: semi + lunar (moon)."),
        QUIZ("What stops blood flowing back from the aorta into the left ventricle?",
             ["The septum", "The bicuspid valve", "The semilunar valve", "The tendons"], 2,
             "The semilunar valve at the base of the aorta closes when the ventricle relaxes.",
             hint="Which valve is at the start of the aorta?",
             feedback=["The septum separates the left and right sides.", "The bicuspid valve is between the left atrium and ventricle.", "",
                       "Tendons hold the flaps of the tricuspid and bicuspid valves."]),
        TIP("Exam link: Paper 1 (multiple choice) usually has a labelled diagram of the heart and asks you to name a part or follow the blood. Paper 2 may ask you to describe the "
            "double circulation or the action of the valves. Draw a large, clear diagram and label with straight lines.", title="Exam link"),
        PQ("Name the chamber of the heart with the thickest wall and explain why it is thick.",
           "The left ventricle. It pumps blood to the whole body at high pressure, so its muscle wall is thick."),
        PQ("Describe the path of blood from the vena cava to the aorta.",
           "Vena cava, right atrium, tricuspid valve, right ventricle, semilunar valve, pulmonary artery, lungs, pulmonary vein, left atrium, bicuspid valve, left ventricle, semilunar valve, aorta."),
        PQ("State the function of the valves of the heart.", "They make blood flow in one direction only by closing to stop it flowing backwards."),
        PQ("Calculate the cardiac output of a person with a stroke volume of 60 cm$^3$ and a heart rate of 75 beats per minute.",
           "Cardiac output = 60 x 75 = 4500 cm³ per minute."),
        SUM("The heart has four chambers: two thin-walled atria and two thick-walled ventricles. The left ventricle has the thickest wall.",
            "Valves (tricuspid, bicuspid, semilunar) keep the blood flowing one way.",
            "Double circulation: right side to the lungs, left side to the body.",
            "In one cycle the atria contract, then the ventricles contract and the valves open and close in turn.",
            "Heart rate = pulse count per minute. Cardiac output = stroke volume x heart rate.",
            "The pulmonary artery carries deoxygenated blood and the pulmonary vein carries oxygenated blood."),
    ],
))

# ------------------------------------------------------------------ 6. Blood vessels and the lymphatic system
LESSONS.append(lesson(
    module=M1, topic=T_HEART,
    title="Arteries, veins, capillaries and the lymphatic system",
    slug="bic-blood-vessels-and-the-lymphatic-system",
    minutes=22,
    summary="How arteries, veins and capillaries are built for their jobs, how tissue fluid and lymph form and return to the blood, and how fatty deposits can cause heart disease.",
    objectives=[
        "Compare the structure and function of arteries, veins and capillaries",
        "Explain how tissue fluid forms and how lymph is formed and returns to the blood",
        "State the functions of the lymphatic system and lymph nodes",
        "Outline the causes of coronary heart disease",
    ],
    key_concepts=["Artery", "Vein", "Capillary", "Tissue fluid", "Lymph", "Lymph node", "Lacteal", "Coronary heart disease"],
    blocks=[
        H("Introduction"),
        T("When you cut your finger, bright red blood spurts out in pulses if an artery is cut, but flows slowly and darker if a vein is cut. The two kinds of vessel are different "
          "because they do different jobs. In this lesson you will learn why."),
        D("**Blood vessels** are the tubes that carry blood round the body. The three kinds are arteries, veins and capillaries.", title="Definition: blood vessels"),
        H("Arteries"),
        D("An **artery** carries blood **away** from the heart at high pressure.", title="Definition: artery"),
        T("Its wall is thick and has muscle and elastic fibres. The wall can stretch when blood is pushed in by the heart and spring back afterwards, which keeps the blood moving. "
          "The lumen (the space inside) is narrow. Arteries have no valves, except for the semilunar valves at the heart. The pulse is felt in an artery."),
        H("Veins"),
        D("A **vein** carries blood **towards** the heart at low pressure.", title="Definition: vein"),
        T("A vein has a thinner wall, less muscle and a wide lumen. Many veins have **valves** that stop blood flowing backwards. When the muscles around a vein squeeze, "
          "the valves make the blood go towards the heart."),
        H("Capillaries"),
        D("A **capillary** is a very small blood vessel with a wall only **one cell thick**. It joins the smallest arteries to the smallest veins.", title="Definition: capillary"),
        T("The thin wall lets oxygen, food and other substances pass out to the cells, and lets carbon dioxide and waste pass in. Capillaries are found in all tissues "
          "and are so narrow that red blood cells must pass in single file."),
        CODE("""
Feature        Artery       Vein        Capillary
Direction      from heart   to heart    between
Wall           thick        thin        one cell
Lumen          narrow       wide        very narrow
Valves         no           yes         no
Pressure       high         low         falling
Pulse          yes          no          no
""", "text", title="Blood vessels compared"),
        MISTAKE("Saying arteries always carry oxygenated blood", "Arteries carry blood away from the heart. The pulmonary artery carries deoxygenated blood. "
                "Define the vessels by **direction**, not by the oxygen content."),
        QUIZ("Which feature allows a capillary to exchange substances with the cells?",
             ["A thick elastic wall", "Valves in the lumen", "A wall one cell thick", "A wide lumen"], 2,
             "The very thin wall gives a short distance for diffusion.",
             hint="Think about distance for diffusion.",
             feedback=["A thick wall would slow exchange. That is an artery.", "Valves are found in veins.", "", "Capillaries are very narrow."]),
        H("Tissue fluid and lymph"),
        T("Blood pressure pushes some plasma out through the thin walls of the capillaries. This leaked plasma, without red blood cells and large proteins, is called **tissue fluid**. "
          "It bathes the cells, giving them oxygen and food and taking away their waste."),
        D("**Tissue fluid** is the fluid that fills the spaces between cells. It is formed from plasma that leaks out of the capillaries.", title="Definition: tissue fluid"),
        D("**Lymph** is tissue fluid that has entered the lymph vessels. It contains water, dissolved substances and lymphocytes.", title="Definition: lymph"),
        T("Most tissue fluid goes back into the capillaries. The rest drains into the tiny blindly ending **lymph capillaries**, which join to form larger lymph vessels. "
          "These vessels have valves, like veins. Lymph moves slowly as the body muscles squeeze the vessels. At the base of the neck, the large lymph vessels empty into "
          "veins (the subclavian veins), so the fluid returns to the blood."),
        KEY("Functions of the lymphatic system", "It does three jobs.", cards=[
            ["Drains tissue fluid", "It returns excess fluid to the blood and stops tissues from swelling."],
            ["Defends the body", "**Lymph nodes** are swellings along the lymph vessels. They filter out microbes and make lymphocytes."],
            ["Absorbs fat", "Lymph vessels in the villi of the small intestine, called **lacteals**, absorb fatty acids and glycerol."],
        ]),
        EX("Worked example 1: explain a swollen leg", intro="After a disease blocks the lymph vessels of a leg, the leg swells. Explain why.", steps=[
            S("Say what is happening to tissue fluid", text="Tissue fluid still forms from the plasma leaking out of the capillaries."),
            S("Say what is blocked", text="The excess fluid cannot drain into the lymph vessels."),
            S("Conclude", text="The fluid collects in the spaces between the cells, so the leg swells."),
        ]),
        EX("Worked example 2: link structure to function", intro="Explain why veins have valves but arteries do not.", steps=[
            S("Pressure in arteries", text="Blood in arteries is at high pressure from the heart, so it cannot flow backwards."),
            S("Pressure in veins", text="Blood in veins is at low pressure, so it could flow backwards."),
            S("Conclude", text="Valves in veins close to stop backflow and keep the blood moving towards the heart."),
        ]),
        H("Heart disease"),
        T("In **coronary heart disease**, the coronary arteries that feed the heart muscle become narrow because fatty deposits (such as cholesterol) build up in their walls. "
          "If a blood clot blocks a narrowed artery, part of the heart muscle gets no oxygen and the person has a heart attack. The risk is greater with a diet rich in "
          "animal fat, smoking, lack of exercise, stress and a family history of the disease. Regular exercise and a balanced diet lower the risk."),
        QUIZ("Which of these reduces the risk of coronary heart disease?",
             ["Eating more fried food", "Smoking", "Regular exercise", "Never walking"], 2,
             "Exercise keeps the heart muscle strong and helps to keep the arteries healthy.",
             hint="Which choice is a healthy habit?",
             feedback=["Fatty food raises the risk of fatty deposits.", "Smoking damages the arteries.", "", "A lack of exercise raises the risk."]),
        TIP("Exam link: Paper 1 (multiple choice) tests the differences between arteries and veins, and may show a vessel in cross-section. Paper 2 can ask you to compare the "
            "vessels or to explain how lymph forms. Use a comparison: 'an artery has a thick wall, but a vein has a thin wall'.", title="Exam link"),
        PQ("State two differences between an artery and a vein.", "An artery has a thick wall, a narrow lumen and no valves, and carries blood from the heart at high pressure. A vein has a thin wall, a wide lumen and valves, and carries blood to the heart at low pressure."),
        PQ("Explain how a capillary is adapted for the exchange of substances.", "Its wall is only one cell thick, so substances have a very short distance to diffuse. It is narrow and branches in all tissues, so it is close to every cell."),
        PQ("Describe how lymph is formed and how it returns to the blood.",
           "Plasma leaks from the capillaries to form tissue fluid. Excess tissue fluid drains into lymph capillaries and becomes lymph. Lymph flows in lymph vessels with valves and empties into veins near the neck."),
        PQ("State two functions of lymph nodes.", "They filter out microbes and they make lymphocytes."),
        SUM("Arteries have thick, elastic walls and carry blood away from the heart at high pressure.",
            "Veins have thin walls and valves and carry blood to the heart at low pressure.",
            "Capillaries have walls one cell thick, so exchange with the tissues is quick.",
            "Tissue fluid forms from plasma leaking out of capillaries. The excess drains into the lymph vessels as lymph and returns to the blood near the neck.",
            "Lymph nodes filter microbes and make lymphocytes. Lacteals absorb fats.",
            "Coronary heart disease comes from fatty deposits that narrow the coronary arteries."),
    ],
))

# ------------------------------------------------------------------ 7. Excretion and the nephron
LESSONS.append(lesson(
    module=M1, topic=T_KIDNEY,
    title="Excretion, the kidney and the nephron",
    slug="bic-excretion-the-kidney-and-the-nephron",
    minutes=28,
    summary="What excretion is and which organs do it, how a kidney is built, and how the nephron filters blood under pressure and then reabsorbs useful substances to make urine.",
    objectives=[
        "Define excretion and name the excretory products and organs of a mammal",
        "Outline excretion in plants and in some other animals",
        "Describe the structure of the kidney and the nephron",
        "Explain ultrafiltration and selective reabsorption and the composition of urine",
    ],
    key_concepts=["Excretion", "Urea", "Kidney", "Nephron", "Bowman's capsule", "Glomerulus", "Ultrafiltration", "Selective reabsorption", "Urine"],
    blocks=[
        H("Introduction"),
        T("After a football match in the hot sun, a boy's urine is small in volume and dark yellow. A few hours and several glasses of water later, it is pale and plentiful. "
          "His kidneys changed what they did. The kidneys clean the blood and also adjust its water content. In this lesson you will see how."),
        D("**Excretion** is the removal from the body of the waste products of metabolism (the chemical reactions in cells), and of substances in excess of the body's needs.",
          title="Definition: excretion"),
        MISTAKE("Mixing up excretion and egestion", "Excretion removes waste made **by the cells** (for example urea and carbon dioxide). **Egestion** (defaecation) removes undigested food "
                "that never entered the cells. Faeces are egested, not excreted."),
        KEY("Excretory products and organs in a human", "Each organ removes particular wastes.", cards=[
            ["Kidneys", "Urea, excess water and excess mineral ions, in urine."],
            ["Lungs", "Carbon dioxide and water vapour, in the air we breathe out."],
            ["Skin", "Water, mineral ions and a little urea, in sweat."],
            ["Liver", "Makes urea and the bile pigments from broken-down haemoglobin. These leave through the kidneys and the gut."],
        ]),
        H("Excretion in plants and other animals"),
        T("Plants do not have special excretory organs. Their wastes are mainly:"),
        CODE("""
Waste product         How the plant gets rid of it
Oxygen (from          diffuses out through
photosynthesis)       the stomata
Carbon dioxide        diffuses out through the
(from respiration)    stomata (mostly at night)
Water vapour          transpiration
Tannins, resins,      stored in leaves, bark and
latex, alkaloids      fruits, and lost when leaves
                      fall or bark peels
""", "text", title="Excretion in plants"),
        KEY("Excretion in some animals", "Check which examples your syllabus uses.", cards=[
            ["Amoeba", "Carbon dioxide and ammonia diffuse out through the cell membrane. A contractile vacuole removes excess water (osmoregulation)."],
            ["Earthworm", "Tube-like **nephridia** in each body segment remove nitrogen waste and water."],
            ["Insects", "**Malpighian tubules** remove nitrogen waste from the blood into the gut."],
            ["Mammals", "Two kidneys make urine, which contains urea."],
        ]),
        H("The urinary system and the kidney"),
        T("A human has two kidneys at the back of the abdomen. Blood enters each kidney in the **renal artery** and leaves in the **renal vein**. "
          "Urine leaves in the **ureter** and is stored in the **bladder**. It is passed out through the **urethra**."),
        IMG("f5bi-c-kidney.svg", alt="Section of a kidney showing the outer cortex, inner medulla and pelvis, with the renal artery, renal vein and ureter",
            caption="Figure 1. A section through a kidney."),
        T("A kidney has three regions. The **cortex** is the dark outer layer. The **medulla** is the inner layer. The **pelvis** is the space in the middle that collects urine "
          "and joins the ureter. Each kidney has about a million tiny filtering units called **nephrons**."),
        H("The nephron"),
        IMG("f5bi-c-nephron.svg", alt="A nephron: Bowman's capsule with glomerulus, proximal tubule, loop of Henle, distal tubule and collecting duct, with afferent and efferent arterioles",
            caption="Figure 2. One nephron. The capsule, glomerulus and both twisted tubules lie in the cortex. The loop of Henle and the collecting duct run into the medulla."),
        KEY("Parts of a nephron", "Learn them in the order that fluid flows.", cards=[
            ["Glomerulus", "A knot of capillaries inside the capsule."],
            ["Bowman's capsule", "A cup-shaped structure that surrounds the glomerulus."],
            ["Proximal convoluted tubule", "The first twisted tube."],
            ["Loop of Henle", "A U-shaped tube that dips into the medulla."],
            ["Distal convoluted tubule", "The second twisted tube."],
            ["Collecting duct", "Joins several nephrons and carries urine to the pelvis."],
        ]),
        H("Step 1: ultrafiltration"),
        D("**Ultrafiltration** is the filtering of blood under high pressure in the glomerulus. Small molecules pass into the Bowman's capsule. Cells and large proteins stay in the blood.",
          title="Definition: ultrafiltration"),
        T("The afferent arteriole that brings blood to the glomerulus is **wider** than the efferent arteriole that takes blood away. Blood is squeezed into a narrower space, "
          "so the pressure in the glomerulus is high. This forces water and small dissolved substances through the thin capillary wall and the capsule wall. "
          "The liquid that collects in the capsule is the **glomerular filtrate**."),
        CODE("""
Passes into the filtrate    Stays in the blood
water                       red blood cells
glucose                     white blood cells
amino acids                 platelets
urea                        plasma proteins
mineral ions                (too large)
""", "text", title="What is filtered and what is not"),
        H("Step 2: selective reabsorption"),
        D("**Selective reabsorption** is the taking back of useful substances from the filtrate into the blood as it flows along the tubule.", title="Definition: selective reabsorption"),
        KEY("Where reabsorption happens", "The filtrate loses useful substances all along the tubule.", cards=[
            ["Proximal tubule", "**All** the glucose and amino acids are taken back by active transport (using energy). Much of the water and many mineral ions are also reabsorbed."],
            ["Loop of Henle", "More water and salts are reabsorbed. This makes the medulla salty, which helps the kidney to make concentrated urine."],
            ["Distal tubule and collecting duct", "The amount of water reabsorbed depends on the body's needs and is controlled by the hormone ADH (see the next lesson). Some salts are also adjusted here."],
        ]),
        T("Urea is not reabsorbed to any great extent. As water is taken back, the urea becomes more concentrated and leaves in the urine. "
          "The urine then flows down the collecting duct into the pelvis, the ureter and the bladder."),
        CODE("""
Substance        Blood plasma  Filtrate  Urine
Plasma protein   present       absent    absent
Glucose          present       present   absent
Urea             present       present   very concentrated
Water            present       present   less than filtrate
""", "text", title="Plasma, filtrate and urine compared"),
        T("In a healthy adult, about 180 dm$^3$ of filtrate is formed in a day, but only about 1.5 dm$^3$ of urine. These are approximate values. Check your textbook for the figures your teacher uses."),
        EX("Worked example 1: how much is reabsorbed?", intro="A man forms 180 dm$^3$ of filtrate in a day and passes 1.5 dm$^3$ of urine. Calculate the percentage of the filtrate that is reabsorbed.", steps=[
            S("Volume reabsorbed", math=r"180 - 1.5 = 178.5\ \text{dm}^3"),
            S("Divide by the filtrate volume", math=r"\frac{178.5}{180} = 0.9917"),
            S("Convert to percent", math=r"0.9917 \times 100 \approx 99.2\%"),
        ]),
        EX("Worked example 2: glucose in urine", intro="A doctor finds glucose in a patient's urine. Explain how this can happen.", steps=[
            S("Say what normally happens", text="All the glucose in the filtrate is reabsorbed in the proximal tubule."),
            S("Say what is different", text="If the blood glucose is very high, as in untreated diabetes, more glucose is filtered than the tubule can take back."),
            S("Conclude", text="The rest stays in the filtrate and leaves in the urine."),
        ]),
        QUIZ("Which of these is NOT normally found in the glomerular filtrate?",
             ["Glucose", "Urea", "Plasma proteins", "Amino acids"], 2,
             "Plasma proteins are too large to pass through the capillary wall in the glomerulus.",
             hint="Which substance has the biggest molecules?",
             feedback=["Glucose is small and passes into the filtrate.", "Urea is small and passes into the filtrate.", "", "Amino acids are small and pass into the filtrate."]),
        QUIZ("Why is the pressure in the glomerulus high?",
             ["The efferent arteriole is wider than the afferent arteriole", "The afferent arteriole is wider than the efferent arteriole", "The Bowman's capsule is full of air", "The loop of Henle pulls blood in"], 1,
             "Blood enters through a wide vessel and leaves through a narrower one, so the pressure builds up.",
             hint="Compare the width of the vessel going in and the vessel going out.",
             feedback=["That is the wrong way round.", "", "The capsule is full of filtrate, not air.", "The loop of Henle is part of the tubule, not of the blood supply."]),
        H("When the kidneys fail"),
        T("If both kidneys fail, urea builds up in the blood. A patient can be treated by **dialysis**. In haemodialysis, the blood flows through tubes made of a partially permeable material "
          "that are surrounded by dialysis fluid. Urea and excess salts diffuse out into the fluid. The fluid has the normal concentration of glucose and salts so that these are not lost. "
          "Another treatment is a **kidney transplant** from a donor with a matching tissue type."),
        TIP("Exam link: Paper 1 (multiple choice) usually shows a diagram of a nephron and asks where filtration or reabsorption happens, or which substance is absent from urine. "
            "Paper 2 can ask you to describe how urine is formed. Learn the sequence: ultrafiltration, selective reabsorption, urine.", title="Exam link"),
        PQ("Define excretion and name two excretory organs.", "Excretion is the removal of the waste products of metabolism from the body. The kidneys (urea, water, salts) and the lungs (carbon dioxide) are excretory organs. The skin is another."),
        PQ("Describe how ultrafiltration takes place in the nephron.",
           "Blood enters the glomerulus through a wide afferent arteriole and leaves through a narrower efferent arteriole, so the pressure is high. This forces water, glucose, amino acids, urea and "
           "mineral ions through the capillary wall into the Bowman's capsule. Blood cells and plasma proteins are too large and remain in the blood."),
        PQ("Explain what happens to glucose in the proximal tubule.", "All the glucose in the filtrate is reabsorbed into the blood by active transport, so there is no glucose in normal urine."),
        PQ("State two differences between the composition of urine and glomerular filtrate.", "Urine has no glucose and no amino acids, but the filtrate has them. Urine has a much higher concentration of urea and less water."),
        SUM("Excretion is the removal of metabolic waste. The kidneys, lungs, skin and liver all play a part.",
            "Plants excrete oxygen, carbon dioxide and water vapour through the stomata and store other wastes in leaves and bark.",
            "A kidney has a cortex, a medulla and a pelvis. Each kidney contains many nephrons.",
            "Ultrafiltration takes place in the glomerulus under high pressure, because the afferent arteriole is wider than the efferent one.",
            "In selective reabsorption all the glucose and amino acids and much of the water and salts are taken back into the blood.",
            "Urine contains water, urea and salts. It has no glucose or protein in a healthy person."),
    ],
))

# ------------------------------------------------------------------ 8. Homeostasis: osmoregulation, liver and skin
LESSONS.append(lesson(
    module=M1, topic=T_OSMO,
    title="Homeostasis: ADH, the liver and temperature control by the skin",
    slug="bic-osmoregulation-the-liver-and-the-skin",
    minutes=28,
    summary="How negative feedback keeps the body steady, how ADH controls the water content of the blood, the main jobs of the liver, and how the skin controls body temperature.",
    objectives=[
        "Define homeostasis and explain negative feedback",
        "Explain how ADH controls the amount of water in the blood",
        "State the main homeostatic and other functions of the liver",
        "Describe the structure of the skin and how it controls body temperature",
    ],
    key_concepts=["Homeostasis", "Negative feedback", "Osmoregulation", "ADH", "Hypothalamus", "Deamination", "Thermoregulation", "Vasodilation", "Vasoconstriction"],
    blocks=[
        H("Introduction"),
        T("In Maroua at midday the temperature can pass 40 degrees Celsius. Yet your body temperature stays near 37 degrees Celsius. You sweat, you feel thirsty and you pass little urine. "
          "Your body is working to keep conditions inside it steady."),
        D("**Homeostasis** is the maintenance of a constant internal environment, such as steady body temperature, blood glucose, water content and pH.", title="Definition: homeostasis"),
        T("Most homeostasis works by **negative feedback**. A receptor detects a change away from the normal level. The brain or a gland sends a signal. An effector acts to bring the level back. "
          "When the level is normal, the action stops. The response is always **opposite** to the change."),
        CODE("""
Change away from normal level
   -> receptor detects it
   -> control centre (brain or gland)
   -> effector acts
   -> level returns to normal
   -> the correction stops (negative feedback)
""", "text", title="Negative feedback"),
        H("Osmoregulation and ADH"),
        D("**Osmoregulation** is the control of the water content and salt concentration of the blood and body fluids.", title="Definition: osmoregulation"),
        T("The **hypothalamus**, a part of the brain, contains receptors that detect how concentrated the blood is. When the blood is too concentrated, "
          "the **pituitary gland**, just under the hypothalamus, releases a hormone called **ADH** (antidiuretic hormone) into the blood. ADH reaches the kidneys."),
        KEY("What ADH does", "ADH changes how much water is reabsorbed.", cards=[
            ["Dehydrated (little water)", "More ADH is released. The walls of the distal tubule and collecting duct become **more permeable** to water. More water is reabsorbed. The urine is **small in volume and concentrated**."],
            ["Too much water", "Less ADH is released. The walls are less permeable. Less water is reabsorbed. The urine is **large in volume and dilute**."],
        ]),
        CODE("""
Sweating, no drinking
 -> blood more concentrated
 -> hypothalamus detects it
 -> pituitary releases MORE ADH
 -> kidney reabsorbs MORE water
 -> small volume of concentrated urine
 -> blood water content returns to normal
""", "text", title="Response to dehydration"),
        EX("Worked example 1: after drinking", intro="A girl drinks two litres of water quickly. Explain what happens to her urine.", steps=[
            S("Effect on the blood", text="The blood becomes more dilute, because there is more water."),
            S("Hormone response", text="The hypothalamus detects this and the pituitary releases less ADH."),
            S("Kidney response", text="The collecting duct is less permeable, so less water is reabsorbed."),
            S("Conclusion", text="She passes a large volume of dilute urine, which removes the extra water."),
        ]),
        QUIZ("What is the effect of a high level of ADH?",
             ["The kidney makes a large volume of dilute urine", "The kidney makes a small volume of concentrated urine", "The kidney stops making urea", "The kidney reabsorbs less water"], 1,
             "ADH makes the collecting duct more permeable, so more water returns to the blood.",
             hint="ADH is 'antidiuretic', which means against making a lot of urine.",
             feedback=["That happens when ADH is low.", "", "Urea is made in the liver, and ADH does not stop it.", "ADH increases the water reabsorbed."]),
        H("The liver"),
        T("The liver is the largest organ in the abdomen. It receives oxygenated blood from the **hepatic artery** and blood full of digested food from the intestine along the "
          "**hepatic portal vein**. Blood leaves in the **hepatic vein**."),
        KEY("Main functions of the liver", "A very busy organ.", cards=[
            ["Controls blood glucose", "Stores excess glucose as glycogen (under the control of insulin) and changes glycogen back to glucose when it is needed (under the control of glucagon)."],
            ["Deamination", "Removes the amino group from excess amino acids and changes it into **urea**, which the blood carries to the kidneys. The rest of each amino acid is used for energy."],
            ["Makes bile", "Bile is stored in the gall bladder. It helps to digest fats. It also contains bile pigments from broken-down red cells."],
            ["Detoxification", "Breaks down poisons, alcohol and drugs into harmless substances."],
            ["Makes plasma proteins", "Includes fibrinogen and prothrombin for clotting."],
            ["Stores substances", "Stores iron and vitamins A, D and B12."],
            ["Produces heat", "Its many chemical reactions release heat, which helps to warm the body."],
        ]),
        T("Red blood cells that are old are broken down in the liver and spleen. The iron is stored and the rest of the haemoglobin is changed into bile pigments."),
        H("The skin and temperature control"),
        T("The skin has an outer **epidermis** made of flat cells with a tough protein (keratin) on top. Below it is the **dermis**, which contains sweat glands, hair follicles with "
          "tiny muscles, blood vessels, sensory receptors and oil (sebaceous) glands. Under the dermis is a layer of **fat** that insulates the body."),
        T("Mammals keep their body temperature near **37 degrees Celsius**. The **hypothalamus** acts as the thermostat. It detects the temperature of the blood and receives signals from "
          "the skin. Then it sends nerve impulses to the skin and muscles."),
        CODE("""
When too HOT                  When too COLD
sweat glands make more sweat  sweat glands make less sweat
(evaporation cools the skin)
arterioles in the skin widen  arterioles in the skin narrow
(vasodilation): more blood    (vasoconstriction): less blood
near the surface, heat lost   near the surface, heat kept
hairs lie flat                hairs stand up, trapping air
no shivering                  muscles shiver and make heat
""", "text", title="Control of body temperature"),
        MISTAKE("Saying that blood vessels move towards the skin", "Blood vessels do not move. The **arterioles** supplying the skin capillaries become wider (vasodilation) or narrower (vasoconstriction). "
                "Say 'the arterioles dilate', not 'the capillaries move closer to the surface'."),
        MISTAKE("Saying that we sweat to lose heat from the sweat itself", "Sweating cools you because the water **evaporates**, and evaporation takes heat from the skin."),
        EX("Worked example 2: a runner on a hot day", intro="Explain how a runner's body keeps cool during a race in the heat.", steps=[
            S("Detect", text="The hypothalamus detects that the blood temperature has risen."),
            S("Respond: skin vessels", text="The arterioles in the skin dilate, so more blood flows near the surface and heat is lost by radiation."),
            S("Respond: sweat", text="The sweat glands make sweat. As it evaporates it takes heat from the skin."),
            S("Result", text="The body temperature falls back towards 37 degrees Celsius. This is negative feedback."),
        ]),
        QUIZ("In cold weather, which change happens in the skin?",
             ["Arterioles widen", "Hairs lie flat", "Sweat production increases", "Arterioles narrow"], 3,
             "Vasoconstriction reduces the blood flowing near the surface, so less heat is lost.",
             hint="The body must keep heat, not lose it.",
             feedback=["Widening arterioles loses heat. That happens in hot weather.", "Hairs stand up in the cold to trap air.", "More sweat is made in the heat.", ""]),
        TIP("Exam link: Paper 1 (multiple choice) tests ADH, the liver functions and the skin responses, and includes assertion and reasoning questions on homeostasis. "
            "Paper 2 may ask you to explain how the body keeps its temperature or water content steady. Use the words detect, respond and negative feedback.", title="Exam link"),
        PQ("Define homeostasis.", "Homeostasis is the maintenance of a constant internal environment in the body, for example constant temperature and water content of the blood."),
        PQ("Explain how ADH helps the body when a person is dehydrated.",
           "The blood becomes more concentrated and the hypothalamus detects this. The pituitary releases more ADH. ADH makes the collecting duct more permeable, so more water is reabsorbed. A small volume of concentrated urine is made and the water content of the blood rises."),
        PQ("State three functions of the liver.", "Any three of: stores glycogen and controls blood glucose, deamination to make urea, makes bile, detoxifies poisons, makes plasma proteins, stores iron and vitamins, produces heat."),
        PQ("Describe two ways in which the skin helps to lower body temperature when it is hot.", "Arterioles in the skin dilate so more heat is lost from the blood near the surface. Sweat glands release sweat that evaporates and cools the skin."),
        SUM("Homeostasis is keeping the internal environment constant, mostly by negative feedback.",
            "ADH from the pituitary makes the kidney reabsorb more water when the blood is too concentrated.",
            "High ADH gives a small volume of concentrated urine. Low ADH gives a large volume of dilute urine.",
            "The liver stores glycogen, makes urea by deamination, makes bile and plasma proteins, detoxifies and produces heat.",
            "The hypothalamus controls body temperature (about 37 degrees Celsius).",
            "When hot the skin arterioles dilate and sweat is made. When cold they narrow, hairs stand up and the muscles shiver."),
    ],
))

# ------------------------------------------------------------------ 9. Plant responses
LESSONS.append(lesson(
    module=M2, topic=T_RESP,
    title="Tropisms, taxes, nastic responses and auxins",
    slug="bic-tropisms-nastic-responses-and-auxins",
    minutes=24,
    summary="How plants respond to light, gravity, water and touch: tropisms, taxes and nastic movements, how auxins cause phototropism and geotropism, and how auxins are used in farming.",
    objectives=[
        "Define tropism, taxis and nastic response and give examples of each",
        "Describe phototropism, geotropism and hydrotropism in shoots and roots",
        "Explain how auxins cause shoots to bend towards light",
        "State two uses of auxins in agriculture",
    ],
    key_concepts=["Stimulus", "Response", "Tropism", "Phototropism", "Geotropism", "Hydrotropism", "Taxis", "Nastic response", "Auxin"],
    blocks=[
        H("Introduction"),
        T("A bean seedling grown in a dark box with a small hole at one side does not grow straight. The shoot bends towards the hole where the light comes in. "
          "Plants have no nerves or muscles, but they can still respond to their surroundings. In this lesson you will see how."),
        D("A **stimulus** is a change in the surroundings that an organism can detect. A **response** is the way the organism reacts to the stimulus.", title="Definitions: stimulus and response"),
        H("Tropisms"),
        D("A **tropism** is a growth response of part of a plant in a direction that depends on the direction of the stimulus.", title="Definition: tropism"),
        T("A **positive** tropism is growth **towards** the stimulus. A **negative** tropism is growth **away from** the stimulus. Plants respond slowly because they respond by growing."),
        KEY("Common tropisms", "The name tells you the stimulus.", cards=[
            ["Phototropism", "Response to **light**. Shoots grow towards light (positive). Roots usually grow away from light (negative)."],
            ["Geotropism", "Response to **gravity**. Roots grow downwards (positive). Shoots grow upwards (negative)."],
            ["Hydrotropism", "Response to **water**. Roots grow towards moist soil (positive)."],
            ["Chemotropism", "Response to a **chemical**. A pollen tube grows towards the ovule (positive)."],
            ["Thigmotropism", "Response to **touch**. The tendrils of a climbing bean plant wind round a support."],
        ]),
        CODE("""
Stimulus   Shoot                Root
Light      grows towards (+)    grows away (-)
Gravity    grows up (-)         grows down (+)
Water      -                    grows towards (+)
""", "text", title="Summary of tropisms"),
        TIP("Remember the usefulness. A shoot grows towards light to make food by photosynthesis. A root grows down and towards water to anchor the plant and absorb water and ions."),
        H("Taxes and nastic responses"),
        D("A **taxis** is the movement of a whole organism (or a free cell) towards or away from a stimulus.", title="Definition: taxis"),
        T("Examples are **phototaxis**, when a single-celled green organism such as *Chlamydomonas* swims towards light, and **chemotaxis**, when a sperm cell swims towards an egg cell."),
        D("A **nastic response** is a plant movement in response to a stimulus that does **not** depend on the direction of the stimulus.", title="Definition: nastic response"),
        T("The leaves of the sensitive plant, *Mimosa pudica*, fold up when touched, whichever side is touched. Some flowers open when it is bright and close when it is dark. "
          "These are quick movements that do not depend on growth in one direction."),
        CODE("""
Response   Who or what moves?       Depends on the
                                    direction of stimulus?
Tropism    part of a plant (growth) YES
Taxis      whole organism           YES
Nastic     part of a plant          NO
""", "text", title="Tropism, taxis and nastic response compared"),
        QUIZ("The leaflets of a sensitive plant fold when touched. This is an example of",
             ["a tropism", "a taxis", "a nastic response", "a growth hormone"], 2,
             "The response does not depend on the direction of the touch and the whole plant does not move, so it is nastic.",
             hint="Is the response directional?",
             feedback=["A tropism is growth towards or away from the stimulus.", "A taxis is movement of a whole organism.", "", "A hormone is a chemical, not a type of response."]),
        H("Auxins"),
        D("**Auxins** are plant hormones made in the tips of shoots and roots. They move to other parts and control growth by making cells elongate.", title="Definition: auxin"),
        T("The main natural auxin is called IAA. It is made in the growing tips and diffuses back along the shoot or root. A shoot tip makes enough auxin to make the cells below elongate."),
        IMG("f5bi-c-phototropism.svg", alt="Two panels: a straight shoot with light from the right and more auxin dots on the left shaded side, then a shoot bent to the right towards the light",
            caption="Figure 1. Phototropism. Auxin builds up on the shaded side, so that side grows faster and the shoot bends towards the light."),
        KEY("How auxins cause the responses", "Auxin moves away from light and down with gravity.", cards=[
            ["Phototropism in a shoot", "Light from one side makes the auxin move to the **shaded** side. A high auxin level **speeds up** elongation in a shoot. The shaded side grows faster and the shoot bends towards the light."],
            ["Geotropism in a root", "Gravity makes auxin collect on the **lower** side. In a root, a high auxin level **slows down** growth. The lower side grows slower and the root bends downwards."],
            ["Geotropism in a shoot", "Auxin collects on the lower side, which grows faster, so the shoot bends upwards."],
        ]),
        T("The same hormone speeds up growth in a shoot and slows it in a root. Roots are more sensitive to auxin than shoots. Some textbooks differ on the details, so check your textbook."),
        H("Evidence from experiments"),
        CODE("""
Treatment of the seedling            Result
Tip left alone, light from one side  bends towards light
Tip cut off                          does not bend, grows little
Tip covered with foil (opaque cap)   grows straight up
Base covered, tip in the light       bends towards light
""", "text", title="Experiments on a shoot with light from one side"),
        T("These results show that the tip detects the light and makes the auxin. The bending happens in the part below the tip."),
        EX("Worked example 1: a root in a horizontal pot", intro="A bean seedling is laid on its side in the dark. Explain why the root bends downwards.", steps=[
            S("The stimulus", text="Gravity, which pulls on the root in a downward direction."),
            S("Auxin movement", text="Auxin collects on the lower side of the root."),
            S("Effect in a root", text="A high auxin concentration slows down growth in a root, so the lower side grows more slowly than the upper side."),
            S("Result", text="The root bends downwards: positive geotropism."),
        ]),
        EX("Worked example 2: the foil cap", intro="A seedling has its shoot tip covered with a foil cap and light shines from one side. Predict the result and explain it.", steps=[
            S("Prediction", text="The shoot grows straight upwards and does not bend."),
            S("Reason", text="The tip, which detects light, is covered, so the auxin is not moved to the shaded side."),
            S("Conclusion", text="The tip is the part that senses light and makes auxin."),
        ]),
        H("Auxins in farming"),
        KEY("Uses of auxins", "Synthetic auxins are made in factories.", cards=[
            ["Rooting powder", "A cutting, such as a piece of cassava stem or a stem of a flowering shrub, is dipped in powder. It grows roots faster."],
            ["Selective weedkiller", "A large dose of synthetic auxin kills broad-leaved weeds in a field of narrow-leaved crops such as maize, because the weeds grow abnormally fast and die."],
            ["Fruit growing", "Auxin can make fruit set without fertilisation or prevent young fruits from falling early. Check your textbook for the uses your teacher stresses."],
        ]),
        MISTAKE("Calling a response a 'reflex' in plants", "Plants have no nervous system, so their responses are not reflexes. Say 'tropism' for a growth response and 'nastic response' for a non-directional movement."),
        MISTAKE("Saying that auxin makes the lit side grow more", "In phototropism auxin moves to the **shaded** side. That side grows faster and the shoot bends **towards** the light."),
        QUIZ("A shoot bends towards light because",
             ["auxin collects on the lit side", "auxin collects on the shaded side and speeds growth there", "auxin is destroyed in the dark", "the roots pull on the shoot"], 1,
             "Auxin moves to the shaded side. It speeds up cell elongation, so the shaded side grows faster and the shoot bends towards the light.",
             hint="Which side must grow faster for the shoot to bend towards the light?",
             feedback=["It collects on the shaded side.", "", "The auxin is not destroyed in the dark.", "Roots do not pull on the shoot."]),
        TIP("Exam link: Paper 1 (multiple choice) often shows a seedling experiment with foil caps or one-sided light and asks you to predict the result. Paper 2 can ask you to "
            "define tropism or explain phototropism using auxins. Write 'auxin moves to the shaded side' every time.", title="Exam link"),
        PQ("Define tropism and give one example.", "A tropism is a growth response of part of a plant in a direction decided by the stimulus. An example is the growth of a shoot towards light (positive phototropism)."),
        PQ("State two differences between a tropism and a nastic response.", "A tropism is a growth response whose direction depends on the direction of the stimulus. A nastic response is not directional and is often a quick movement, such as the folding of Mimosa leaves."),
        PQ("Explain how auxin makes a shoot bend towards light.", "Light from one side makes auxin move to the shaded side. Auxin makes the cells elongate, so the shaded side grows faster than the lit side and the shoot bends towards the light."),
        PQ("State two uses of synthetic auxins in agriculture.", "Rooting powder helps cuttings to grow roots. Selective weedkillers kill broad-leaved weeds in a cereal crop."),
        SUM("A tropism is a directional growth response of part of a plant. Positive means towards the stimulus and negative means away.",
            "Shoots are positively phototropic and negatively geotropic. Roots are positively geotropic and positively hydrotropic.",
            "A taxis is movement of a whole organism. A nastic response is not directional.",
            "Auxins are made in the tips of shoots and roots and control cell elongation.",
            "In a shoot, auxin collects on the shaded side and speeds growth, so the shoot bends towards light.",
            "Synthetic auxins are used in rooting powder and selective weedkillers."),
    ],
))

# ------------------------------------------------------------------ 10. Nervous system
LESSONS.append(lesson(
    module=M2, topic=T_NERV,
    title="Neurones, synapses, the brain and reflex actions",
    slug="bic-neurones-synapse-brain-and-reflex-actions",
    minutes=28,
    summary="The structure of sensory, relay and motor neurones, how impulses cross a synapse, the path of a reflex arc through the spinal cord, and the main parts of the brain.",
    objectives=[
        "Describe the structure and function of a motor neurone and name the three types of neurone",
        "Explain how an impulse crosses a synapse",
        "Trace the path of a simple reflex action and distinguish it from a voluntary action and a conditioned reflex",
        "State the functions of the main parts of the brain and spinal cord",
    ],
    key_concepts=["Central nervous system", "Neurone", "Synapse", "Acetylcholine", "Reflex arc", "Receptor", "Effector", "Conditioned reflex", "Cerebrum", "Cerebellum", "Medulla"],
    blocks=[
        H("Introduction"),
        T("You step on a thorn while walking to the stream. Before you even feel the pain, your foot has already jumped up. That quick action did not wait for you to decide. "
          "It was a reflex, and it protected you. In this lesson you will follow the path that the signal took."),
        D("The **nervous system** is made up of the **central nervous system** (CNS: the brain and the spinal cord) and the **peripheral nerves** that run from the CNS to all parts of the body.", title="Definition: nervous system"),
        H("Neurones"),
        D("A **neurone** is a nerve cell. It is a cell that carries electrical signals called **nerve impulses**.", title="Definition: neurone"),
        IMG("f5bi-c-neurone.svg", alt="A motor neurone with dendrites and a cell body with a nucleus on the left, a long axon with myelin sheath segments and nodes, and nerve endings on the right",
            caption="Figure 1. A motor neurone. The impulse travels from the cell body along the axon to the nerve endings."),
        KEY("Parts of a motor neurone", "Each part has a job.", cards=[
            ["Cell body", "Contains the nucleus and most of the cytoplasm."],
            ["Dendrites", "Short branches that receive impulses from other neurones."],
            ["Axon", "A very long fibre that carries the impulse away from the cell body."],
            ["Myelin sheath", "A fatty layer around the axon that insulates it and makes the impulse travel much faster. The gaps in the sheath are **nodes of Ranvier**."],
            ["Nerve endings", "Pass the impulse on to another neurone or to a muscle or gland."],
        ]),
        KEY("Three types of neurone", "A reflex arc uses all three.", cards=[
            ["Sensory neurone", "Carries impulses from a **receptor** to the CNS."],
            ["Relay (intermediate) neurone", "Short neurone inside the CNS that passes the impulse from the sensory to the motor neurone."],
            ["Motor neurone", "Carries impulses from the CNS to an **effector** (a muscle or a gland)."],
        ]),
        D("A **receptor** is a cell or organ that detects a stimulus. An **effector** is a muscle or gland that carries out the response.", title="Definitions: receptor and effector"),
        H("The synapse"),
        D("A **synapse** is a tiny gap between the nerve ending of one neurone and the next neurone, where the impulse is passed on by a chemical.", title="Definition: synapse"),
        CODE("""
1 The impulse arrives at the nerve ending.
2 Vesicles release a chemical transmitter
  (acetylcholine) into the gap.
3 Acetylcholine diffuses across the gap.
4 It attaches to receptors on the next neurone.
5 A new impulse starts in the next neurone.
6 An enzyme breaks down the transmitter,
  so the signal stops.
""", "text", title="How an impulse crosses a synapse"),
        T("A synapse works in **one direction only**, because only the first neurone has vesicles of transmitter. The nerve ending has many mitochondria to give energy for this."),
        MISTAKE("Misspelling the transmitter", "The Board's report notes that some candidates write 'acetylclorin' and 'acetochilin'. The correct word is **acetylcholine**. Learn it as acetyl + choline."),
        QUIZ("What carries the message across a synapse?",
             ["An electrical impulse that jumps the gap", "A chemical transmitter that diffuses across", "The myelin sheath", "A blood cell"], 1,
             "The impulse cannot jump the gap. The nerve ending releases a chemical (acetylcholine) which diffuses across and starts a new impulse.",
             hint="What is released from the vesicles?",
             feedback=["The gap is too wide for an electrical jump.", "", "The myelin sheath covers the axon and has nothing to do with the gap.", "Blood cells do not take part."]),
        H("Reflex actions"),
        D("A **reflex action** is a quick, automatic, involuntary response to a stimulus. It does not need to be thought about and often protects the body.", title="Definition: reflex action"),
        IMG("f5bi-c-reflex-arc.svg", alt="A reflex arc: receptor in the skin, sensory neurone with a ganglion entering the spinal cord, relay neurone in the grey matter, motor neurone leaving to a muscle effector",
            caption="Figure 2. A reflex arc. The impulse travels along the sensory neurone to the spinal cord, across the relay neurone and out along the motor neurone to the effector."),
        CODE("""
Stimulus (a thorn pricks the foot)
 -> RECEPTOR (pain receptor in the skin)
 -> SENSORY NEURONE (into the spinal cord)
 -> RELAY NEURONE (in the grey matter)
 -> MOTOR NEURONE (out of the spinal cord)
 -> EFFECTOR (leg muscle)
 -> Response (the leg is lifted)
""", "text", title="The reflex arc"),
        T("The path is called the **reflex arc**. The brain is not part of it, so the response is fast. The brain is informed afterwards, and that is when you feel pain. "
          "Other reflexes are blinking when something comes towards the eye, coughing, the knee jerk, the pupil getting smaller in bright light and the mouth watering at the smell of food."),
        CODE("""
Reflex action          Voluntary action
automatic              decided on
very fast              slower
brain not needed       brain (cerebrum) used
for the response       to decide
example: blinking      example: writing a letter
""", "text", title="Reflex and voluntary action compared"),
        T("A **conditioned reflex** is a reflex that has been learned. In Pavlov's famous experiment a dog was fed straight after a bell rang. After some time the dog's mouth watered "
          "when the bell rang, even when no food was given. The brain had linked the bell with food. A normal inborn reflex is called a **simple reflex**."),
        H("The spinal cord and the brain"),
        T("The **spinal cord** runs inside the backbone. In a cross-section, the **grey matter** is in the middle and is shaped like a butterfly. It contains the cell bodies of neurones. "
          "The **white matter** is outside and is made of axons with myelin sheaths. Sensory neurones enter at the **dorsal root**, where there is a swelling called a ganglion. "
          "Motor neurones leave at the **ventral root**."),
        KEY("The main parts of the brain", "The brain is protected by the skull, three membranes (the meninges) and a fluid.", cards=[
            ["Cerebrum", "The largest part. Controls thinking, memory, speech, voluntary actions and the interpretation of the senses."],
            ["Cerebellum", "Controls balance, posture and the smooth coordination of muscle movements."],
            ["Medulla oblongata", "Controls involuntary actions such as the heartbeat and breathing rate. It joins the brain to the spinal cord."],
            ["Hypothalamus", "Controls body temperature and water balance and controls the pituitary gland."],
            ["Pituitary gland", "The 'master' gland that makes many hormones. Studied in the next lessons."],
        ]),
        EX("Worked example 1: the hot pot", intro="A girl touches a hot pot and pulls her hand away. Describe the path of the nerve impulse.", steps=[
            S("Receptor", text="Heat receptors in the skin of the finger detect the heat."),
            S("Sensory neurone", text="Impulses pass along a sensory neurone to the spinal cord."),
            S("Relay neurone", text="A relay neurone in the grey matter of the spinal cord passes the impulses on."),
            S("Motor neurone", text="A motor neurone carries impulses to the muscles of the arm, the effector."),
            S("Response", text="The muscles contract and the hand is pulled away."),
        ]),
        EX("Worked example 2: why a reflex is fast", intro="Explain why a reflex action is faster than a voluntary action.", steps=[
            S("Path length", text="The impulse goes only through the spinal cord."),
            S("Fewer synapses", text="There are very few synapses on the path and no decision is made."),
            S("Conclusion", text="The brain is not needed for the response, so it takes less time."),
        ]),
        QUIZ("Which part of the brain controls balance and coordination of movement?",
             ["Cerebrum", "Cerebellum", "Medulla oblongata", "Pituitary gland"], 1,
             "The cerebellum coordinates muscle movement, balance and posture.",
             hint="Its name means 'little brain' and it lies at the back.",
             feedback=["The cerebrum is for thought and voluntary actions.", "", "The medulla controls heartbeat and breathing.", "The pituitary is a hormone gland."]),
        TIP("Exam link: Paper 1 (multiple choice) often gives a drawing of a reflex arc and asks you to label the neurones or arrange the steps. Paper 2 can ask you to describe a reflex action "
            "or compare reflex and voluntary actions. Use the order: stimulus, receptor, sensory neurone, relay neurone, motor neurone, effector, response.", title="Exam link"),
        PQ("Name the three types of neurone and state what each one does.", "Sensory neurones carry impulses from receptors to the CNS. Relay neurones pass impulses inside the CNS. Motor neurones carry impulses from the CNS to effectors."),
        PQ("Describe how an impulse is passed across a synapse.", "The impulse reaches the nerve ending, which releases acetylcholine into the synaptic gap. The acetylcholine diffuses across and attaches to receptors on the next neurone, which starts a new impulse. An enzyme then breaks it down."),
        PQ("Define a reflex action and give two examples.", "A reflex action is a quick, automatic, involuntary response to a stimulus. Examples are blinking and the knee jerk. (Coughing and the pupil reflex are also accepted.)"),
        PQ("State the functions of the cerebellum and the medulla oblongata.", "The cerebellum controls balance and coordination of muscles. The medulla oblongata controls involuntary actions such as the heartbeat and breathing."),
        SUM("The nervous system has the CNS (brain and spinal cord) and the nerves. A neurone carries nerve impulses.",
            "The three kinds of neurone are sensory, relay and motor. The myelin sheath makes an impulse travel faster.",
            "At a synapse a chemical, acetylcholine, carries the signal across the gap in one direction only.",
            "A reflex arc: receptor, sensory neurone, relay neurone, motor neurone, effector.",
            "A reflex is automatic and fast. A conditioned reflex is learned.",
            "The cerebrum is for thought, the cerebellum for balance and the medulla for the heartbeat and breathing."),
    ],
))

# ------------------------------------------------------------------ 11. The eye
LESSONS.append(lesson(
    module=M2, topic=T_SENSE,
    title="The structure and function of the eye",
    slug="bic-the-eye",
    minutes=26,
    summary="The parts of the eye and what each does, how the pupil reflex and accommodation work, the roles of rods and cones, and how short sight and long sight are corrected.",
    objectives=[
        "Name the parts of the eye and state the function of each",
        "Explain the pupil reflex in bright and dim light",
        "Explain accommodation for near and distant objects",
        "Describe short sight and long sight and how lenses correct them",
    ],
    key_concepts=["Cornea", "Iris", "Pupil", "Lens", "Retina", "Rods and cones", "Accommodation", "Short sight", "Long sight"],
    blocks=[
        H("Introduction"),
        T("In class you read the writing on the board, then look down at your book. Your eyes switch from far to near without any effort. "
          "When you step from a bright playground into a dark classroom, you cannot see well for a moment, then your sight adjusts. In this lesson you will see how the eye does all this."),
        D("The **eye** is the sense organ for sight. It contains receptor cells that detect light and send impulses along the optic nerve to the brain.", title="Definition: the eye"),
        IMG("f5bi-c-eye.svg", alt="Horizontal section of the eye showing cornea, aqueous humour, iris, lens, ciliary muscle, suspensory ligament, vitreous humour, retina, sclera, fovea and optic nerve",
            caption="Figure 1. A horizontal section through the human eye. Light enters on the left."),
        CODE("""
Part                  Function
Cornea                transparent; bends light (most of the
                      focusing)
Aqueous humour        watery fluid; keeps the shape of the
                      front of the eye
Iris                  coloured muscle; controls the size of
                      the pupil
Pupil                 hole in the iris; lets light in
Lens                  transparent and elastic; fine focus
                      onto the retina
Ciliary muscle        changes the shape of the lens
Suspensory ligaments  hold the lens; pulled tight or loose
Vitreous humour       jelly; keeps the eyeball in shape
Retina                contains rods and cones; detects light
Choroid               dark, with blood vessels; stops
                      reflection and supplies the retina
Sclera                tough white outer layer; protects
Optic nerve           carries impulses to the brain
""", "text", title="Parts of the eye and their functions"),
        T("Eyelids, eyelashes and tears protect the front of the eye. The thin, clear covering of the front of the eye is the **conjunctiva**. Tears wash away dust and contain "
          "an enzyme that kills bacteria."),
        H("Rods and cones"),
        KEY("The two kinds of light-sensitive cell in the retina", "Both are receptor cells.", cards=[
            ["Rods", "Work in dim light. They see in black, white and grey only. There are many of them near the edges of the retina."],
            ["Cones", "Work in bright light and give colour vision. There are three kinds, sensitive to red, green and blue light. They are packed close together at the **fovea**."],
        ]),
        T("The **fovea** is a small area of the retina directly behind the lens, with mainly cones. It gives the sharpest, most detailed vision. "
          "The **blind spot** is the place where the optic nerve leaves the eye. It has no receptor cells, so you cannot see an image that falls on it."),
        QUIZ("Which part of the retina gives the sharpest colour vision?",
             ["The blind spot", "The fovea", "The sclera", "The iris"], 1,
             "The fovea has the most cones, tightly packed, which gives sharp colour vision.",
             hint="It is the area that you point at the thing that you want to see clearly.",
             feedback=["The blind spot has no receptors at all.", "", "The sclera is the tough outer coat and has no receptors.", "The iris is a muscle that controls the pupil."]),
        H("The pupil reflex"),
        T("The iris has two sets of muscle: **circular muscles** arranged in rings and **radial muscles** arranged like the spokes of a wheel. They are antagonistic. "
          "The pupil reflex is a reflex action that protects the retina from damage in bright light and lets in more light in the dark."),
        CODE("""
                    BRIGHT light         DIM light
Circular muscles    contract             relax
Radial muscles      relax                contract
Pupil               gets smaller         gets larger
Light entering      less                 more
""", "text", title="The pupil reflex"),
        H("Accommodation"),
        D("**Accommodation** is the change in the shape of the lens so that light from objects at different distances is focused on the retina.", title="Definition: accommodation"),
        CODE("""
                       NEAR object          DISTANT object
Ciliary muscle         contracts            relaxes
Suspensory ligaments   slacken              pulled tight
Lens shape             thicker, rounder     thinner, flatter
Light bending          more                 less
""", "text", title="Accommodation"),
        T("When you look at a near object, the light rays are spreading out. The lens must bend them more, so it becomes **thicker**. When you look far away, the rays are almost parallel, so a **thinner** lens is enough."),
        MISTAKE("Mixing up the ligaments and the muscle", "For a **near** object the ciliary muscle **contracts**, which slackens the ligaments and lets the lens become rounder. A common error is to say that the ligaments contract. Ligaments cannot contract: they are pulled tight or become slack."),
        EX("Worked example 1: reading a book", intro="Explain what happens in the eye of a boy who looks from the board to his book.", steps=[
            S("The change", text="The object is now near, so light rays spread out more."),
            S("Ciliary muscle", text="The ciliary muscles contract."),
            S("Ligaments", text="The suspensory ligaments slacken."),
            S("Lens", text="The lens becomes thicker and more rounded and bends the light more, so the image is focused on the retina."),
        ]),
        H("Eye defects"),
        KEY("Short sight and long sight", "In both defects the image does not fall on the retina.", cards=[
            ["Short sight (myopia)", "The eyeball is too long or the lens is too strong. The image of a distant object forms **in front of** the retina. Distant objects are blurred. A **concave** (diverging) lens corrects it."],
            ["Long sight (hypermetropia)", "The eyeball is too short or the lens is too weak. The image of a near object forms **behind** the retina. Near objects are blurred. A **convex** (converging) lens corrects it."],
        ]),
        T("A **cataract** is a cloudy lens that blocks light. It is treated by replacing the lens with an artificial one. Some textbooks also describe **astigmatism**, where the cornea is uneven "
          "so some lines look blurred; it is corrected with a special lens. Check your textbook. A lack of vitamin A can damage the cornea and cause poor sight in dim light (night blindness)."),
        EX("Worked example 2: choosing a lens", intro="A girl cannot read the board but can read her book clearly. What is her defect and what lens will correct it?", steps=[
            S("Identify the problem", text="Distant objects are blurred and near objects are clear."),
            S("Name the defect", text="Short sight (myopia). The image forms in front of the retina."),
            S("Correct it", text="A concave lens spreads the light a little before it enters the eye, which moves the image back onto the retina."),
        ]),
        QUIZ("A boy has long sight. Which statement is correct?",
             ["He cannot see near objects clearly and needs a convex lens", "He cannot see distant objects clearly and needs a concave lens", "He cannot see colours and needs a convex lens", "He cannot see in dim light and needs a concave lens"], 0,
             "In long sight, the image of a near object falls behind the retina. A convex lens bends the light inwards before it reaches the eye.",
             hint="Long sight affects close work, like reading.",
             feedback=["", "That describes short sight.", "Long sight does not affect colour vision.", "Long sight is not about dim light."]),
        TIP("Exam link: Paper 1 (multiple choice) very often uses a labelled drawing of the eye and asks for a part or its function, or about accommodation and the pupil reflex. "
            "Paper 2 can ask you to describe how the eye focuses on a near object or to explain an eye defect. Draw the eye carefully and label with ruled lines.", title="Exam link"),
        PQ("State the function of the iris and the retina.", "The iris controls the size of the pupil and so the amount of light entering the eye. The retina contains the rods and cones, which detect light and send impulses along the optic nerve to the brain."),
        PQ("Describe how the pupil changes when a person walks from a dim room into bright sunlight.", "The circular muscles of the iris contract and the radial muscles relax, so the pupil gets smaller. This reduces the amount of light entering the eye and protects the retina."),
        PQ("Explain how the lens changes shape to focus on a nearby object.", "The ciliary muscles contract, so the suspensory ligaments slacken. The elastic lens becomes thicker and rounder and bends the light more strongly, so a clear image forms on the retina."),
        PQ("State two differences between rods and cones.", "Rods work in dim light and see black and white. Cones work in bright light and give colour vision. Cones are concentrated at the fovea."),
        SUM("The cornea and lens focus light onto the retina. The iris controls the size of the pupil. The retina has rods (dim light) and cones (colour).",
            "In bright light the circular muscles contract and the pupil gets smaller. In dim light the radial muscles contract and the pupil gets larger.",
            "For a near object the ciliary muscles contract, the ligaments slacken and the lens becomes thicker.",
            "For a distant object the ciliary muscles relax, the ligaments are tight and the lens is thinner.",
            "Short sight is corrected with a concave lens and long sight with a convex lens.",
            "The fovea gives sharp vision. The blind spot has no receptors."),
    ],
))

# ------------------------------------------------------------------ 12. The ear
LESSONS.append(lesson(
    module=M2, topic=T_SENSE,
    title="The structure of the ear: hearing and balance",
    slug="bic-the-ear-hearing-and-balance",
    minutes=22,
    summary="The outer, middle and inner ear, how sound travels as vibrations to the cochlea and is turned into impulses, how the Eustachian tube equalises pressure, and how the semicircular canals help balance.",
    objectives=[
        "Name the parts of the outer, middle and inner ear and state their functions",
        "Describe how sound is detected and turned into nerve impulses",
        "State the function of the Eustachian tube",
        "Explain how the semicircular canals help with balance",
    ],
    key_concepts=["Pinna", "Eardrum", "Ossicles", "Eustachian tube", "Cochlea", "Auditory nerve", "Semicircular canals", "Balance"],
    blocks=[
        H("Introduction"),
        T("At a market in Bafoussam, a hawker calls out the price of tomatoes. You hear him over the noise of the crowd. Your ear has caught the sound waves and turned them into signals for the brain. "
          "The ear also helps you to keep your balance when you ride a motorbike or walk on a narrow path. In this lesson you will follow the path of sound."),
        D("The **ear** is the sense organ for hearing and balance. It has three parts: the outer ear, the middle ear and the inner ear.", title="Definition: the ear"),
        IMG("f5bi-c-ear.svg", alt="The ear: pinna and ear canal on the left, the eardrum, three ossicles and the Eustachian tube in the middle ear, and the semicircular canals, cochlea and auditory nerve of the inner ear",
            caption="Figure 1. The structure of the ear. The three parts are the outer ear (pinna and canal), the middle ear (eardrum, ossicles) and the inner ear (cochlea and semicircular canals)."),
        KEY("The three parts of the ear", "Follow the sound from the outside inwards.", cards=[
            ["Outer ear", "The **pinna** collects sound waves and the **ear canal** leads them to the eardrum. The canal makes wax that traps dust and microbes."],
            ["Middle ear", "An air-filled space. It contains the **eardrum** and three small bones, the **ossicles**: the hammer (malleus), anvil (incus) and stirrup (stapes). The **Eustachian tube** joins it to the throat."],
            ["Inner ear", "Filled with fluid. It contains the **cochlea** for hearing and the **semicircular canals** for balance. The **auditory nerve** takes impulses to the brain."],
        ]),
        H("How we hear"),
        CODE("""
Sound waves enter the ear canal
 -> the EARDRUM vibrates
 -> the three OSSICLES carry and magnify the vibrations
 -> the stirrup pushes on the OVAL WINDOW
 -> the fluid in the COCHLEA vibrates
 -> sensory hair cells in the cochlea are stimulated
 -> impulses go along the AUDITORY NERVE
 -> the brain interprets them as sound
""", "text", title="The path of sound"),
        T("The ossicles act as a lever system. They make the vibrations stronger, because the oval window is much smaller than the eardrum. "
          "The cochlea is shaped like a snail shell. Different parts of it respond to different pitches. A louder sound makes bigger vibrations and stimulates the hair cells more."),
        H("The Eustachian tube"),
        D("The **Eustachian tube** is a narrow tube that joins the middle ear to the back of the throat. It lets air in and out to keep the air pressure on both sides of the eardrum equal.", title="Definition: Eustachian tube"),
        T("If the pressure is not equal, the eardrum is pushed in or out and cannot vibrate well. When you go up a mountain such as Mount Cameroon, or when a plane lands, your ears feel blocked. "
          "Swallowing or yawning opens the tube, and the pressure becomes equal again with a small pop. Infections can spread from the throat to the middle ear along the same tube."),
        QUIZ("What is the function of the ossicles?",
             ["To collect sound waves", "To carry and magnify vibrations from the eardrum to the oval window", "To change the pressure in the middle ear", "To detect the position of the head"], 1,
             "The three small bones pass the vibrations on and make them stronger.",
             hint="They lie between the eardrum and the oval window.",
             feedback=["The pinna collects sound waves.", "", "The Eustachian tube equalises pressure.", "The semicircular canals help with balance."]),
        H("Balance"),
        T("Three **semicircular canals** in the inner ear lie at right angles to each other, like the three corners of a box. They are filled with fluid. When the head turns, the fluid "
          "moves and bends sensory hair cells, which send impulses to the brain about the movement of the head. Because the three canals lie in different planes, the brain can tell "
          "which way the head turns."),
        T("Two small chambers, the **utricle** and **saccule**, contain hair cells and tiny stones. They detect the position of the head when it is still and the pull of gravity. "
          "Check your textbook for how much detail you need. The brain uses this information together with sight and touch to keep the body balanced. The cerebellum then coordinates muscles to stay upright."),
        MISTAKE("Saying that the semicircular canals are for hearing", "Hearing is done by the **cochlea**. The semicircular canals detect movement of the head and are for **balance**."),
        MISTAKE("Saying the eardrum is in the inner ear", "The eardrum lies between the outer ear and the middle ear. It is not part of the inner ear."),
        EX("Worked example 1: sound to nerve impulse", intro="Describe how a sound wave is changed into an impulse that goes to the brain.", steps=[
            S("Outer ear", text="The sound wave travels down the ear canal and makes the eardrum vibrate."),
            S("Middle ear", text="The ossicles carry the vibrations to the oval window and magnify them."),
            S("Inner ear", text="The fluid in the cochlea vibrates and stimulates the hair cells."),
            S("Impulse", text="The hair cells send impulses along the auditory nerve to the brain."),
        ]),
        EX("Worked example 2: blocked ears", intro="Explain why a passenger's ears feel blocked when a plane comes down quickly and why swallowing helps.", steps=[
            S("Pressure difference", text="The outside air pressure changes quickly, but the air in the middle ear stays at the old pressure."),
            S("Effect on the eardrum", text="The eardrum is pushed to one side and cannot vibrate well."),
            S("Swallowing", text="Swallowing opens the Eustachian tube, which lets air pass and makes the pressures equal."),
        ]),
        QUIZ("Which part of the ear contains the receptor cells for hearing?",
             ["Eardrum", "Semicircular canals", "Cochlea", "Ossicles"], 2,
             "The cochlea has the sensory hair cells that change vibrations into nerve impulses.",
             hint="It is shaped like a snail shell.",
             feedback=["The eardrum only vibrates.", "The semicircular canals are for balance.", "", "The ossicles pass on vibrations."]),
        TIP("Exam link: Paper 1 (multiple choice) shows a drawing of the ear and asks you to name a part, its function or the path of sound. Paper 2 can ask you to describe how sound is heard "
            "or how the ear helps balance. Learn the path in order and spell Eustachian and cochlea correctly.", title="Exam link"),
        PQ("Name the three ossicles.", "The hammer (malleus), the anvil (incus) and the stirrup (stapes)."),
        PQ("State the function of the Eustachian tube.", "It joins the middle ear to the throat so that the air pressure on both sides of the eardrum is the same."),
        PQ("Describe how the cochlea helps us to hear.", "The fluid in the cochlea vibrates when the stirrup pushes on the oval window. This stimulates sensory hair cells, which send impulses along the auditory nerve to the brain."),
        PQ("Explain how the semicircular canals detect movement of the head.", "The canals are filled with fluid and lie in three planes. When the head moves, the fluid moves and bends sensory hair cells, which send impulses to the brain."),
        SUM("The ear has outer, middle and inner parts. The pinna and canal collect sound.",
            "The eardrum and ossicles carry and magnify vibrations to the oval window of the cochlea.",
            "The cochlea has hair cells that turn vibrations into impulses carried by the auditory nerve.",
            "The Eustachian tube equalises the air pressure on both sides of the eardrum.",
            "The semicircular canals detect movement of the head and help to keep balance.",
            "The cochlea is for hearing. The semicircular canals are for balance."),
    ],
))

# ------------------------------------------------------------------ 13. The endocrine system
LESSONS.append(lesson(
    module=M2, topic=T_ENDO,
    title="Hormones and the endocrine glands",
    slug="bic-endocrine-system-and-hormones",
    minutes=26,
    summary="What hormones are, how the main endocrine glands (pituitary, thyroid, pancreas, adrenal, testes and ovaries) work, how insulin and glucagon control blood glucose, and how hormones differ from nerves.",
    objectives=[
        "Define hormone and endocrine gland and compare hormonal with nervous control",
        "State the hormone made by each main gland and its effect",
        "Explain how insulin and glucagon control blood glucose and describe diabetes",
        "Explain the effects of adrenaline and thyroxine",
    ],
    key_concepts=["Hormone", "Endocrine gland", "Pituitary gland", "Thyroxine", "Insulin", "Glucagon", "Diabetes", "Adrenaline", "Testosterone", "Oestrogen"],
    blocks=[
        H("Introduction"),
        T("A girl walking home at dusk is suddenly chased by a dog. Her heart pounds, her breathing quickens and her hands shake. Seconds earlier she was calm. "
          "A chemical in her blood, adrenaline, caused these changes. Chemicals like this are called hormones, and the glands that make them form the endocrine system."),
        D("A **hormone** is a chemical messenger made in an **endocrine gland**, carried in the blood and acting on target organs to change their activity.", title="Definition: hormone"),
        D("An **endocrine gland** is a gland without a duct. It releases its hormones directly into the blood.", title="Definition: endocrine gland"),
        CODE("""
Nervous control          Hormonal control
electrical impulses      chemical hormones
along neurones           in the blood
very fast                slower
short-lasting effect     longer-lasting effect
affects a small area     may affect many organs
""", "text", title="Nerves and hormones compared"),
        H("The main endocrine glands"),
        CODE("""
Gland        Hormone(s)               Main effect
Pituitary    ADH, growth hormone,     controls water
             FSH, LH and others       reabsorption, growth,
                                      the sex organs
Thyroid      thyroxine                controls metabolic rate
Pancreas     insulin                  lowers blood glucose
             glucagon                 raises blood glucose
Adrenal      adrenaline               prepares the body for
                                      'fight or flight'
Testes       testosterone             male features, sperm
Ovaries      oestrogen,               female features, the
             progesterone             menstrual cycle
""", "text", title="Glands and hormones"),
        H("The pituitary gland"),
        T("The **pituitary gland** is a pea-sized gland under the brain, joined to the hypothalamus. It is often called the **master gland**, because many of its hormones control other glands. "
          "It makes **growth hormone**, which controls growth of the bones and tissues, **FSH** and **LH**, which act on the ovaries and testes, and **ADH**, which controls water reabsorption in the kidney. "
          "Some textbooks say ADH is made in the hypothalamus and released by the pituitary. Check your textbook."),
        H("The thyroid gland"),
        T("The **thyroid gland** is in the neck. It makes **thyroxine**, a hormone that contains iodine. Thyroxine controls the **metabolic rate** (the rate of chemical reactions, including respiration) "
          "and is needed for growth. A lack of iodine in the diet causes the thyroid to swell in the neck. This is called **goitre**. Too much thyroxine causes weight loss and nervousness."),
        H("The pancreas and blood glucose"),
        T("The **pancreas** has two jobs. It makes digestive enzymes and it also makes the hormones **insulin** and **glucagon**. Both control the level of glucose in the blood, which must stay near a steady value. "
          "The liver is the main target of these hormones."),
        KEY("Insulin and glucagon", "They work in opposite ways. This is negative feedback.", cards=[
            ["Insulin", "Made when blood glucose is **high** (after a meal). It makes the liver and muscles change glucose into **glycogen** and makes cells take up glucose. Blood glucose falls."],
            ["Glucagon", "Made when blood glucose is **low** (between meals or after exercise). It makes the liver change glycogen into glucose. Blood glucose rises."],
        ]),
        CODE("""
Blood glucose too HIGH
 -> pancreas releases INSULIN
 -> liver: glucose -> glycogen
 -> blood glucose falls to normal

Blood glucose too LOW
 -> pancreas releases GLUCAGON
 -> liver: glycogen -> glucose
 -> blood glucose rises to normal
""", "text", title="Control of blood glucose"),
        T("In **diabetes mellitus**, blood glucose rises too high, because the pancreas does not make enough insulin or the body does not respond to it. The symptoms are thirst, a lot of urine, tiredness "
          "and glucose in the urine. Type 1 diabetes is treated with insulin injections and a controlled diet. Type 2 diabetes is often controlled by diet, exercise and sometimes tablets. Check your textbook for the details."),
        MISTAKE("Mixing up insulin and glucagon", "**Insulin** brings blood glucose **down**. **Glucagon** brings it **up**. A memory trick: insulin 'puts glucose in' (cells and liver store it)."),
        QUIZ("What does insulin do?",
             ["Raises blood glucose by changing glycogen to glucose", "Lowers blood glucose by helping the liver to change glucose to glycogen", "Controls the water content of the blood", "Speeds up the heartbeat"], 1,
             "Insulin lowers blood glucose by causing glucose to be stored as glycogen in the liver and muscles.",
             hint="Insulin is released after a meal.",
             feedback=["That is glucagon.", "", "That is ADH.", "That is adrenaline."]),
        H("The adrenal glands"),
        T("The two **adrenal glands** sit on top of the kidneys. They make **adrenaline**, which is released when we are frightened, angry or excited. It prepares the body for action, the so-called **fight or flight** response."),
        CODE("""
Effects of adrenaline
heart beats faster and harder
breathing becomes faster and deeper
liver changes glycogen to glucose
  (more glucose in the blood)
blood is sent to the muscles, away from
  the skin and gut (the skin looks paler)
pupils dilate (get larger)
""", "text", title="Adrenaline: the fight or flight response"),
        H("The gonads"),
        T("The **testes** make **testosterone**, which causes sperm production and the male secondary sexual characteristics: a deep voice, facial hair and broad shoulders. "
          "The **ovaries** make **oestrogen** and **progesterone**, which cause the female secondary sexual characteristics (breast growth and wider hips) and control the menstrual cycle and pregnancy. "
          "These hormones are studied in more detail in the lessons on reproduction."),
        EX("Worked example 1: after a sugary meal", intro="Explain what happens to the blood glucose level of a boy who drinks a large sugary drink.", steps=[
            S("Change", text="Glucose is absorbed into the blood and the level rises above normal."),
            S("Hormone", text="The pancreas detects this and releases insulin."),
            S("Response", text="The liver changes glucose into glycogen and the cells take up more glucose."),
            S("Result", text="The blood glucose level falls back to normal. This is negative feedback."),
        ]),
        EX("Worked example 2: a fright", intro="Explain how adrenaline helps a person to run away from danger.", steps=[
            S("Release", text="The adrenal glands release adrenaline into the blood."),
            S("Heart and lungs", text="The heart beats faster and the breathing is faster, so more oxygen is sent to the muscles."),
            S("Glucose", text="The liver releases glucose, so more fuel is available for respiration."),
            S("Result", text="The muscles get more energy and oxygen for running."),
        ]),
        QUIZ("Which gland is the 'master gland' that controls many other glands?",
             ["Thyroid", "Pancreas", "Pituitary", "Adrenal"], 2,
             "The pituitary gland makes hormones that control growth and other glands such as the ovaries and testes.",
             hint="It lies just under the brain.",
             feedback=["The thyroid makes thyroxine.", "The pancreas makes insulin and glucagon.", "", "The adrenal glands make adrenaline."]),
        TIP("Exam link: Paper 1 (multiple choice) matches a gland with its hormone or effect and uses assertion and reasoning questions on blood glucose. Paper 2 may ask you to "
            "explain how blood glucose is controlled. Name the gland, the hormone and the organ that responds.", title="Exam link"),
        PQ("Define a hormone.", "A hormone is a chemical messenger made in an endocrine gland and carried by the blood to a target organ, where it changes the activity."),
        PQ("State two differences between nervous and hormonal control.", "Nervous control uses electrical impulses along neurones and is very fast with a short-lived effect. Hormonal control uses chemicals in the blood and is slower with a longer-lasting effect."),
        PQ("Explain how insulin and glucagon keep the blood glucose level steady.", "When the blood glucose is high, the pancreas releases insulin and the liver changes glucose into glycogen, so the level falls. When it is low, the pancreas releases glucagon, and the liver changes glycogen into glucose, so the level rises."),
        PQ("State four effects of adrenaline on the body.", "Any four of: faster heartbeat, faster and deeper breathing, more glucose released into the blood by the liver, blood sent to the muscles, paler skin, larger pupils."),
        SUM("A hormone is a chemical messenger made in an endocrine gland and carried in the blood.",
            "Hormones act more slowly than nerves, but their effects last longer.",
            "The pituitary is the master gland. The thyroid makes thyroxine, which controls metabolic rate.",
            "Insulin lowers blood glucose and glucagon raises it. A lack of insulin causes diabetes.",
            "Adrenaline prepares the body for fight or flight.",
            "The testes make testosterone. The ovaries make oestrogen and progesterone."),
    ],
))

# ------------------------------------------------------------------ 14. Skeleton, joints and muscles
LESSONS.append(lesson(
    module=M2, topic=T_SKEL,
    title="The skeleton, joints and antagonistic muscles",
    slug="bic-skeleton-joints-and-antagonistic-muscles",
    minutes=28,
    summary="The functions of the skeleton, the axial and appendicular parts and the vertebrae, the types of joint and the structure of a synovial joint, and how pairs of antagonistic muscles move a limb.",
    objectives=[
        "State the functions of the skeleton and distinguish the axial from the appendicular skeleton",
        "Describe the structure of a typical vertebra and the vertebral regions",
        "Name the types of joint and describe a synovial joint",
        "Explain how antagonistic muscles, such as the biceps and triceps, move the forearm",
    ],
    key_concepts=["Axial skeleton", "Appendicular skeleton", "Vertebra", "Synovial joint", "Cartilage", "Ligament", "Tendon", "Antagonistic muscles", "Biceps and triceps"],
    blocks=[
        H("Introduction"),
        T("A footballer in Limbe tackles hard and goes down. The doctor checks his leg: the bones, the joints, the muscles and the tendons. Each part does a different job. "
          "In this lesson you will learn how the skeleton, joints and muscles work together to support and move the body."),
        KEY("Functions of the skeleton", "The bones do much more than hold us up.", cards=[
            ["Support", "Gives the body its shape and holds up the soft organs."],
            ["Protection", "The skull protects the brain, the ribs protect the heart and lungs and the vertebrae protect the spinal cord."],
            ["Movement", "Bones act as levers. Muscles pull on them."],
            ["Making blood cells", "Red blood cells are made in the red bone marrow."],
            ["Storage", "Bones store calcium and phosphate."],
        ]),
        H("Parts of the skeleton"),
        IMG("f5bi-c-skeleton.svg", alt="Simplified human skeleton with the skull, vertebral column and ribs coloured blue as the axial skeleton and the clavicle, arms, pelvis and legs coloured brown as the appendicular skeleton",
            caption="Figure 1. The human skeleton. Blue shows the axial skeleton and brown shows the appendicular skeleton."),
        D("The **axial skeleton** is the skull, the vertebral column, the ribs and the sternum. It forms the main axis of the body.", title="Definition: axial skeleton"),
        D("The **appendicular skeleton** is the bones of the limbs and the girdles that join them to the axial skeleton: the pectoral girdle (shoulder, with the scapula and clavicle) and the pelvic girdle (hip).", title="Definition: appendicular skeleton"),
        CODE("""
Arm:  humerus (upper arm)
      radius and ulna (forearm)
      carpals, metacarpals, phalanges
Leg:  femur (thigh)
      tibia and fibula (lower leg)
      patella (knee cap)
      tarsals, metatarsals, phalanges
""", "text", title="Main bones of the limbs"),
        H("The vertebral column"),
        T("The backbone is made of 33 small bones called **vertebrae**, separated by pads of cartilage called intervertebral discs, which absorb shocks and allow some movement. "
          "A typical vertebra has a **centrum** (the solid body), a **neural arch** that makes a hole called the neural canal for the spinal cord, a **neural spine** at the back and two **transverse processes** on the sides, "
          "where muscles attach."),
        CODE("""
Region     Number  Notes
Cervical     7     neck; atlas (1st) and axis (2nd)
Thoracic    12     have ribs attached
Lumbar       5     largest centra; carry most weight
Sacral       5     fused, joined to the pelvis
Caudal       4     fused; the tail bone (coccyx)
""", "text", title="Regions of the vertebral column"),
        T("The **atlas** supports the skull and allows nodding ('yes'). The **axis** has a peg that lets the atlas and skull rotate ('no'). Textbooks differ slightly on the counts in the sacral and caudal regions, so check your textbook."),
        MISTAKE("Mixing up the vertebra and the vertebral column", "A **vertebra** is one bone. The **vertebral column** is the whole chain of vertebrae. Write 'vertebrae' for more than one."),
        QUIZ("Which of these belongs to the appendicular skeleton?",
             ["Skull", "Ribs", "Pelvic girdle", "Vertebral column"], 2,
             "The pelvic girdle joins the legs to the body, so it is part of the appendicular skeleton.",
             hint="Which part joins the limbs to the body?",
             feedback=["The skull is part of the axial skeleton.", "The ribs are part of the axial skeleton.", "", "The vertebral column is part of the axial skeleton."]),
        H("Joints"),
        D("A **joint** is a place where two or more bones meet.", title="Definition: joint"),
        KEY("Kinds of joint", "Joints differ in how much movement they allow.", cards=[
            ["Fixed (immovable)", "The bones of the skull are joined by sutures. No movement."],
            ["Slightly movable", "The vertebrae are separated by cartilage discs. Small movement."],
            ["Ball-and-socket", "Shoulder and hip. Movement in all directions."],
            ["Hinge", "Elbow and knee. Movement in one plane, like a door."],
            ["Pivot", "Atlas and axis in the neck. Rotation."],
        ]),
        H("A synovial joint"),
        D("A **synovial joint** is a freely movable joint in which the bone ends are covered with cartilage and held in a capsule that contains a lubricating fluid.", title="Definition: synovial joint"),
        KEY("Parts of a synovial joint (for example the knee or the elbow)", "Each part reduces friction or holds the joint together.", cards=[
            ["Cartilage", "Smooth, slippery layer at the ends of the bones. It reduces friction and absorbs shocks."],
            ["Synovial membrane", "Lines the capsule and makes the synovial fluid."],
            ["Synovial fluid", "Lubricates the joint and reduces friction."],
            ["Capsule", "A tough bag that surrounds the joint and keeps in the fluid."],
            ["Ligaments", "Strong, slightly elastic cords that join **bone to bone** and hold the joint together."],
        ]),
        TIP("A trick to remember: **ligaments** join bone to bone and **tendons** join muscle to bone. A torn ligament is a **sprain**. A bone pulled out of its joint is a **dislocation**."),
        H("Muscles and antagonistic pairs"),
        T("**Skeletal muscles** are made of fibres that can **contract** (shorten). A muscle can pull, but it cannot push. It is joined to bones by **tendons**, which are strong and do not stretch. "
          "Therefore the movement of a limb in two directions needs two muscles that work as a pair. Muscle contraction needs energy from respiration."),
        D("**Antagonistic muscles** are pairs of muscles that have opposite effects: when one contracts, the other relaxes.", title="Definition: antagonistic muscles"),
        IMG("f5bi-c-arm.svg", alt="Two arm diagrams: the arm bends with the biceps contracted and the triceps relaxed, and the arm straightens with the triceps contracted and the biceps relaxed",
            caption="Figure 2. The biceps and the triceps are antagonistic muscles. The elbow joint is the pivot."),
        CODE("""
                     Biceps        Triceps
To BEND the arm      contracts     relaxes
(flexion)            (shortens)    (lengthens)
To STRAIGHTEN        relaxes       contracts
(extension)
""", "text", title="Biceps and triceps"),
        T("The biceps is on the front of the upper arm. It is attached by tendons to the scapula and the radius. When it contracts, it pulls the forearm up. The triceps is on the back of the upper arm and is attached "
          "to the scapula and humerus and to the ulna. When it contracts, it pulls the forearm back to straighten the arm. The muscle that bends a joint is a **flexor** and the one that straightens it is an **extensor**. "
          "The elbow acts as a lever, with the elbow joint as the **fulcrum** (pivot)."),
        EX("Worked example 1: lifting a bag", intro="Explain what the biceps and the triceps do when a girl lifts a bag of cassava to her chest.", steps=[
            S("Biceps", text="The biceps contracts and becomes shorter and thicker."),
            S("Tendon and bone", text="It pulls on the radius through its tendon, so the forearm bends up at the elbow joint."),
            S("Triceps", text="The triceps relaxes and lengthens, so it does not resist."),
        ]),
        EX("Worked example 2: why two muscles", intro="Explain why the arm needs two muscles to bend and straighten.", steps=[
            S("Muscle action", text="A muscle can only pull when it contracts. It cannot push."),
            S("One muscle bends", text="The biceps pulls the forearm up."),
            S("Another muscle straightens", text="The triceps must pull in the opposite direction. So two muscles, working in opposite ways, are needed."),
        ]),
        MISTAKE("Saying that muscles push", "A muscle can only **pull** when it contracts. The movement in the opposite direction needs another muscle, an antagonist."),
        MISTAKE("Mixing up tendons and ligaments", "Tendons join muscle to bone. Ligaments join bone to bone."),
        QUIZ("When you straighten your arm, what happens to the biceps and the triceps?",
             ["Both contract", "The biceps contracts and the triceps relaxes", "The biceps relaxes and the triceps contracts", "Both relax"], 2,
             "The triceps contracts to pull the forearm down and straighten the arm, while the biceps relaxes.",
             hint="The two muscles work as an antagonistic pair.",
             feedback=["Both cannot contract, because they pull in opposite directions.", "That bends the arm.", "", "If both relax, there is no movement."]),
        TIP("Exam link: Paper 1 (multiple choice) often shows the arm with its muscles labelled by letters and asks which muscle contracts, or tests the difference between ligaments and tendons. "
            "Paper 2 can ask you to describe a synovial joint or explain how antagonistic muscles work.", title="Exam link"),
        PQ("State three functions of the skeleton.", "Support, protection of organs (for example the brain by the skull) and movement. It also makes blood cells and stores minerals."),
        PQ("State two differences between a ligament and a tendon.", "A ligament joins bone to bone and is slightly elastic. A tendon joins muscle to bone and does not stretch."),
        PQ("Describe two ways in which a synovial joint is adapted to reduce friction.", "The bone ends are covered with smooth cartilage, and the joint contains synovial fluid that lubricates it."),
        PQ("Explain how the biceps and triceps work together to bend and straighten the forearm.", "To bend the arm the biceps contracts and the triceps relaxes. To straighten it the triceps contracts and the biceps relaxes. They are antagonistic, because muscles can only pull."),
        SUM("The skeleton supports, protects, allows movement, makes blood cells and stores minerals.",
            "The axial skeleton is the skull, the vertebral column, the ribs and the sternum. The appendicular skeleton is the limbs and the girdles.",
            "The vertebral column has cervical, thoracic, lumbar, sacral and caudal regions.",
            "Joints can be fixed, slightly movable, ball-and-socket, hinge or pivot. A synovial joint has cartilage, synovial fluid, a capsule and ligaments.",
            "Ligaments join bone to bone and tendons join muscle to bone.",
            "Muscles only pull, so limbs are moved by antagonistic pairs such as the biceps and triceps."),
    ],
))
