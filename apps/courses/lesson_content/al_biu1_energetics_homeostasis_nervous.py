"""Upper Sixth Biology: Cellular Bioenergetics & Respiration; Homeostasis, Excretion & Osmoregulation;
Nervous, Sensory, Endocrine & Muscular Systems. 20 lessons, one practice set each (practice file of the same name).

Content source: KKEVO master curriculum blueprint (modules BIO-0710-U6M1, U6M2, U6M3). It is not a Board syllabus booklet.
Conventions used here (textbooks differ, so check your textbook):
- ATP yield per glucose: 2.5 ATP per NADH and 1.5 ATP per FADH2 (modern values), giving about 30 to 32;
  older books use 3 and 2, giving 36 to 38.
- Resting potential about -70 mV, threshold about -55 mV, peak about +40 mV.
Numbers on graphs and in tables labelled as teaching values are simple illustrations, not measured results.
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "upper-sixth")

M1 = "Cellular Bioenergetics & Respiration"
M2 = "Homeostasis, Excretion & Osmoregulation"
M3 = "Nervous, Sensory, Endocrine & Muscular Systems"

LESSONS = []

# ------------------------------------------------------------------ 1. Mitochondrion structure
LESSONS.append(lesson(
    module=M1,
    topic="Mitochondrion structure",
    title="The mitochondrion: structure linked to function",
    slug="biu1-mitochondrion-structure",
    minutes=20,
    summary="The two membranes, cristae, matrix, DNA and 70S ribosomes of a mitochondrion; where each stage of respiration happens; how structure fits function; and how to calculate size and magnification.",
    objectives=[
        "Label the outer membrane, intermembrane space, inner membrane, cristae and matrix of a mitochondrion",
        "Explain how folding the inner membrane and the contents of the matrix suit the mitochondrion to aerobic respiration",
        "State where glycolysis, the link reaction, the Krebs cycle and oxidative phosphorylation take place",
        "Calculate magnification and real size from a mitochondrion in an electron micrograph",
    ],
    key_concepts=["Mitochondrion", "Cristae", "Matrix", "Intermembrane space", "ATP synthase", "Mitochondrial DNA", "Endosymbiont theory", "Magnification"],
    blocks=[
        H("Introduction"),
        T("A footballer at a Yaounde stadium, a sperm cell swimming towards an egg and a heart beating all night have one thing in common: "
          "they need a steady supply of **ATP**, the cell's energy carrier. Most of that ATP is made in small organelles called **mitochondria**."),
        T("In Lower Sixth you met the mitochondrion as one of the organelles of the eukaryotic cell. In this module we use it as the "
          "site of aerobic respiration. This lesson looks at the structure; the next lessons follow the chemistry."),
        D("A **mitochondrion** is a double-membrane organelle, usually 0.5 to 1 micrometre wide and 2 to 5 micrometres long (sizes vary), "
          "in which the later stages of aerobic respiration take place and most of the cell's ATP is made.",
          title="Definition: mitochondrion"),
        IMG("al-biu1-mitochondrion.svg", alt="Section through a mitochondrion showing the outer membrane, intermembrane space, folded inner membrane forming cristae, matrix, circular DNA, 70S ribosomes and ATP synthase.",
            caption="Figure 1. A mitochondrion in section (diagram, not to scale)."),
        H("The parts and what they do"),
        KEY("Four compartments", "Learn each part together with its job.", cards=[
            ["Outer membrane", "Smooth and fairly permeable to small molecules. It separates the organelle from the cytoplasm."],
            ["Intermembrane space", "The narrow gap between the two membranes. Protons (H⁺) are pumped into it, so it becomes acidic."],
            ["Inner membrane", "Folded into cristae. Very impermeable to H⁺. Carries the electron carriers and ATP synthase."],
            ["Matrix", "The fluid inside. Contains enzymes of the link reaction and Krebs cycle, circular DNA and 70S ribosomes."],
        ]),
        T("The **inner membrane** is folded into shelf-like or tube-like **cristae**. The folds give a much larger surface area, so many more "
          "electron-transport chains and ATP synthase molecules fit in one mitochondrion. Cells that use a lot of ATP, such as muscle and "
          "liver cells, have mitochondria with many cristae."),
        T("**ATP synthase** appears under the electron microscope as stalked knobs on the matrix side of the inner membrane. "
          "Because the inner membrane is almost impermeable to H⁺, a concentration difference of protons can be built up across it. You will see in a later lesson why this is essential."),
        T("The **matrix** contains the enzymes of the Krebs cycle, NAD and FAD, coenzyme A, and its own genetic system: a small circular "
          "DNA molecule and 70S ribosomes. The organelle can therefore make some of its own proteins. It divides by binary fission."),
        D("The **endosymbiont theory** says that mitochondria arose from aerobic bacteria that were taken into an ancestral cell and stayed. "
          "Evidence: a double membrane, circular naked DNA, 70S ribosomes, a size like a bacterium, and division by binary fission.",
          title="Endosymbiont theory"),
        H("Where each stage of respiration takes place"),
        CODE("""Stage                       Site                              Needs oxygen?
Glycolysis                  Cytoplasm (cytosol)               No
Link reaction               Matrix                            Not directly
Krebs cycle                 Matrix                            Not directly
Oxidative phosphorylation   Inner membrane (cristae)          Yes, O2 is the final electron acceptor""", "text",
             title="Sites of respiration in a eukaryotic cell"),
        TIP("The link reaction and Krebs cycle do not use oxygen themselves, but they stop soon after oxygen runs out, because the carriers NAD and FAD can no longer be re-formed by the electron transport chain."),
        H("Calculating size and magnification"),
        F(r"\text{magnification} = \frac{\text{size of image}}{\text{actual size}}", title="Magnification"),
        T("Convert both measurements to the same unit before dividing. 1 mm = 1000 micrometres (µm)."),
        EX("Worked example 1: finding the magnification", intro="On an electron micrograph a mitochondrion is 45 mm long. Its real length is 1.5 µm. Find the magnification.", steps=[
            S("Convert the image length to micrometres", math=r"45 \text{ mm} = 45 \times 1000 = 45\,000 \ \mu\text{m}"),
            S("Divide image size by actual size", math=r"\frac{45\,000}{1.5} = 30\,000"),
            S("State the answer", text="The magnification is ×30 000."),
        ], check=r"1.5 \times 30\,000 = 45\,000 \ \mu\text{m} = 45 \text{ mm}"),
        EX("Worked example 2: finding the real size", intro="A micrograph at ×20 000 shows a mitochondrion 60 mm long. What is its real length?", steps=[
            S("Rearrange the formula", math=r"\text{actual size} = \frac{\text{image size}}{\text{magnification}}"),
            S("Convert units", math=r"60 \text{ mm} = 60\,000 \ \mu\text{m}"),
            S("Divide", math=r"\frac{60\,000}{20\,000} = 3 \ \mu\text{m}"),
        ]),
        EX("Worked example 3: linking structure to function", intro="Explain why a mitochondrion in a flight muscle cell has many closely packed cristae.", steps=[
            S("Say what the cristae are", text="Folds of the inner membrane."),
            S("State the effect", text="They give a large surface area for electron-transport chains and ATP synthase."),
            S("Link to the cell", text="Muscle cells use ATP quickly, so more ATP synthase means ATP can be made faster."),
        ]),
        MISTAKE("Saying that mitochondria make energy", "Energy cannot be made. Mitochondria transfer energy from glucose and other fuels into ATP. Write 'release energy for ATP synthesis' or 'make ATP'."),
        MISTAKE("Putting the electron transport chain in the matrix", "The electron carriers are in the inner membrane. The Krebs cycle enzymes are in the matrix. Mixing the two up loses marks on every respiration question."),
        QUIZ("Which feature of a mitochondrion gives the largest surface area for ATP production?",
             ["The smooth outer membrane", "The folded inner membrane (cristae)", "The intermembrane space", "The circular DNA"], 1,
             "The cristae increase the area of inner membrane that carries the electron transport chain and ATP synthase.",
             hint="Which membrane carries the ATP synthase?",
             feedback=["The outer membrane is smooth and is not the site of ATP synthesis.", "", "The space is a compartment, not a membrane with carriers.", "DNA carries genes; it does not provide surface area."]),
        QUIZ("Which observation supports the endosymbiont theory?",
             ["Mitochondria have a nucleus", "Mitochondria contain 80S ribosomes", "Mitochondria contain circular DNA and 70S ribosomes", "Mitochondria have one membrane only"], 2,
             "Circular DNA and 70S ribosomes are bacterial features.",
             hint="Compare with prokaryote cells.",
             feedback=["Mitochondria have no nucleus.", "80S ribosomes are eukaryotic cytoplasmic ribosomes; mitochondria have 70S.", "", "Mitochondria have two membranes."]),
        PQ("(a) Name the part of a mitochondrion where the Krebs cycle occurs. (b) A mitochondrion is 2.4 µm long and appears 48 mm long in a micrograph. Calculate the magnification.",
           r"(a) The matrix. (b) 48 mm = 48 000 µm. Magnification = 48 000 / 2.4 = 20 000, so ×20 000."),
        PQ("Explain how the structure of the inner membrane of a mitochondrion makes it suited to ATP production.",
           "It is folded into cristae, giving a large surface area for many electron carriers and ATP synthase molecules. It is almost impermeable to H⁺, so a proton gradient can be built up between the intermembrane space and the matrix, which drives ATP synthase."),
        PQ("State two pieces of evidence that mitochondria were once free-living bacteria.",
           "Any two of: they have their own circular DNA; they have 70S ribosomes; they are about the size of a bacterium; they divide by binary fission; they have a double membrane (the inner one resembling the bacterial membrane)."),
        PQ("Cells of the heart muscle contain more mitochondria than cells of the skin's outer layer. Suggest why.",
           "Heart muscle contracts continuously and needs a very large and steady supply of ATP, so it needs many mitochondria for aerobic respiration. Skin surface cells are dead or inactive and need little ATP."),
        TIP("Mitochondrial structure appears in Paper 1 as a labelled-diagram question and in Paper 2 as a description of structure related to function, often with a magnification calculation."),
        SUM("A mitochondrion has an outer membrane, an intermembrane space, a folded inner membrane (cristae) and a matrix.",
            "Cristae give a large surface area for electron carriers and ATP synthase; the matrix holds Krebs cycle enzymes, circular DNA and 70S ribosomes.",
            "Glycolysis is in the cytoplasm; link reaction and Krebs cycle are in the matrix; oxidative phosphorylation is on the inner membrane.",
            "Magnification = image size / actual size, using the same units."),
    ],
))

# ------------------------------------------------------------------ 2. Glycolysis
LESSONS.append(lesson(
    module=M1,
    topic="Glycolysis",
    title="Glycolysis: splitting glucose in the cytoplasm",
    slug="biu1-glycolysis",
    minutes=22,
    summary="The four stages of glycolysis (phosphorylation, lysis, oxidation, ATP formation), the ATP invested and made, the net gain of 2 ATP and 2 NADH per glucose, and the fate of pyruvate.",
    objectives=[
        "Describe the stages of glycolysis and state where it occurs",
        "Explain why two ATP are used before four are made",
        "State the net products of glycolysis per molecule of glucose",
        "Define substrate-level phosphorylation and calculate the products from several glucose molecules",
    ],
    key_concepts=["Glycolysis", "Phosphorylation", "Triose phosphate", "NAD", "Substrate-level phosphorylation", "Pyruvate", "Net yield"],
    blocks=[
        H("Introduction"),
        T("When you eat boiled cassava or rice, starch is digested to glucose and carried in the blood to every cell. "
          "Respiration begins with **glycolysis** (from Greek words meaning 'sweet splitting'). It takes place in the cytoplasm of every living cell, "
          "from bacteria to the cells of your muscles. It is the one stage that all organisms share, and it needs no oxygen."),
        D("**Glycolysis** is the pathway in the cytoplasm in which one molecule of glucose (6C) is converted to two molecules of pyruvate (3C), "
          "with a net gain of two ATP and two reduced NAD (NADH).",
          title="Definition: glycolysis"),
        IMG("al-biu1-glycolysis.svg", alt="Flow diagram of glycolysis: glucose, fructose 1,6-bisphosphate, two triose phosphates, two pyruvate, with ATP used, NADH formed and ATP made.",
            caption="Figure 1. The main stages of glycolysis (simplified)."),
        H("The four stages"),
        KEY("Stages to learn in order", "Each stage has a clear purpose.", cards=[
            ["1 Phosphorylation", "Two ATP each transfer a phosphate group to the sugar: glucose becomes hexose bisphosphate (fructose 1,6-bisphosphate). This makes it reactive and traps it in the cell."],
            ["2 Lysis", "The 6C sugar splits into two 3C molecules, triose phosphate."],
            ["3 Oxidation", "Each triose phosphate loses hydrogen. NAD accepts it and becomes NADH. A second phosphate (from inorganic phosphate, Pi) is added."],
            ["4 ATP formation", "The phosphate groups are passed to ADP, making ATP. Each triose phosphate ends as pyruvate."],
        ]),
        T("Stage 1 costs 2 ATP. Stages 3 and 4 happen **twice** for every glucose because two triose phosphates are formed. "
          "Four ATP are made in stage 4, so the **net gain** is 4 − 2 = 2 ATP."),
        D("**Substrate-level phosphorylation** is the formation of ATP by transferring a phosphate group directly from a phosphorylated substrate to ADP. "
          "It does not involve the electron transport chain or a proton gradient.",
          title="Definition: substrate-level phosphorylation"),
        F(r"\text{glucose} + 2\text{NAD}^+ \rightarrow 2\text{ pyruvate} + 2\text{NADH} + 2\text{H}^+ \quad (\text{net } +2\text{ ATP})", title="Summary equation (simplified)"),
        CODE("""Per molecule of glucose
ATP used                 2   (stage 1)
ATP made                 4   (stage 4)
Net ATP                  2
NADH made                2   (stage 3)
Pyruvate made            2   (3C each)
Carbon atoms             6C  ->  3C + 3C""", "text", title="Balance sheet of glycolysis"),
        TIP("Textbooks name each intermediate (glucose 6-phosphate, glyceraldehyde 3-phosphate and so on). Your syllabus is about the four stages and the balance sheet, so learn those first. Check your textbook for which intermediate names your teacher expects."),
        H("What happens to pyruvate?"),
        T("The next step depends on oxygen. With oxygen, pyruvate enters the mitochondrion and the link reaction. Without oxygen, pyruvate is converted to lactate or ethanol "
          "(see the lesson on anaerobic pathways). Either way, glycolysis needs a supply of **NAD**. If NADH is not turned back into NAD, glycolysis stops."),
        H("Worked examples"),
        EX("Worked example 1: the balance sheet", intro="Explain why glycolysis uses 2 ATP but gives a net gain of only 2 ATP although 4 ATP are made.", steps=[
            S("ATP used", text="2 ATP are used in the phosphorylation stage, one for each of the two phosphate groups added to glucose."),
            S("ATP made", text="Two triose phosphates are formed, and each gives 2 ATP, so 4 ATP are made."),
            S("Net gain", math=r"4 - 2 = 2 \text{ ATP}"),
        ]),
        EX("Worked example 2: several molecules", intro="A yeast cell breaks down 10 molecules of glucose by glycolysis. How many ATP (net), NADH and pyruvate molecules are made?", steps=[
            S("Net ATP", math=r"10 \times 2 = 20"),
            S("NADH", math=r"10 \times 2 = 20"),
            S("Pyruvate", math=r"10 \times 2 = 20"),
        ], check=r"20 \text{ pyruvate} \times 3\text{C} = 60\text{C} = 10 \times 6\text{C}"),
        EX("Worked example 3: why is glucose phosphorylated?", intro="Give two reasons why glucose is phosphorylated at the start of glycolysis.", steps=[
            S("Reason 1", text="Phosphorylated glucose cannot pass back through the cell surface membrane, so it is trapped in the cell."),
            S("Reason 2", text="It is made more reactive (it has more energy), so the enzymes can split it into triose phosphates."),
        ]),
        MISTAKE("Quoting 4 ATP as the yield", "Four ATP are made but two are used, so the net yield is 2 ATP. Always say 'net' when you give the answer."),
        MISTAKE("Writing that glycolysis happens in the mitochondrion", "Glycolysis takes place in the cytoplasm. It needs no oxygen. Only the later stages use the mitochondrion."),
        QUIZ("What is the net yield of glycolysis from one glucose molecule?",
             ["2 ATP, 2 NADH, 2 pyruvate", "4 ATP, 2 NADH, 1 pyruvate", "2 ATP, 4 NADH, 2 pyruvate", "36 ATP"], 0,
             "4 ATP are made minus 2 used gives 2 ATP; 2 triose phosphates give 2 NADH and 2 pyruvate.",
             hint="Count what is made, then subtract what is used.",
             feedback=["", "4 ATP is the gross yield, and glucose gives two pyruvate, not one.", "Only 2 NADH are made, one per triose phosphate.", "That is a whole-respiration figure for older textbooks, not glycolysis."]),
        QUIZ("In which stage of glycolysis is NAD reduced?",
             ["Phosphorylation of glucose", "Splitting of hexose bisphosphate", "Oxidation of triose phosphate", "Formation of the cell wall"], 2,
             "Triose phosphate loses hydrogen, which NAD accepts.",
             hint="NAD is reduced when a substrate is oxidised.",
             feedback=["Phosphorylation uses ATP; it does not involve NAD.", "Splitting is lysis, not a redox reaction.", "", "That has no place in respiration."]),
        PQ("(a) State where glycolysis occurs. (b) State the net yield of ATP and NADH from one glucose molecule.",
           "(a) In the cytoplasm (cytosol). (b) Net 2 ATP and 2 NADH."),
        PQ("Explain why glycolysis uses two ATP molecules before it makes any.",
           "ATP phosphorylates glucose to hexose bisphosphate. The phosphorylated sugar is more reactive and is trapped inside the cell, and it can be split into two triose phosphates. The ATP invested is repaid when four ATP are made later."),
        PQ("A researcher measures the products of 25 glucose molecules that are respired by glycolysis only. Calculate the net number of ATP and the number of pyruvate molecules.",
           "Net ATP = 25 × 2 = 50. Pyruvate = 25 × 2 = 50."),
        PQ("Define substrate-level phosphorylation and give one place in glycolysis where it occurs.",
           "ATP formation by direct transfer of a phosphate from a phosphorylated substrate to ADP, without the electron transport chain. It occurs when triose phosphate (as bisphosphoglycerate, and later phosphoenolpyruvate) passes its phosphate to ADP, forming 4 ATP per glucose."),
        TIP("Glycolysis questions in Paper 2 usually ask for stages, net yield and location. In Paper 1 the net yield and the role of NAD are favourite points."),
        SUM("Glycolysis occurs in the cytoplasm and needs no oxygen.",
            "Stages: phosphorylation (2 ATP used), lysis, oxidation (NAD to NADH), ATP formation (4 ATP made).",
            "Net yield per glucose: 2 ATP, 2 NADH and 2 pyruvate.",
            "ATP is made by substrate-level phosphorylation; NAD must be regenerated for glycolysis to continue."),
    ],
))

# ------------------------------------------------------------------ 3. Link reaction and Krebs cycle
LESSONS.append(lesson(
    module=M1,
    topic="The link reaction and Krebs cycle",
    title="The link reaction and the Krebs cycle",
    slug="biu1-link-reaction-krebs-cycle",
    minutes=24,
    summary="How pyruvate becomes acetyl CoA, how the Krebs cycle in the matrix releases CO2 and forms NADH, FADH2 and ATP, and how to total the products per glucose.",
    objectives=[
        "Describe the link reaction and state its products",
        "Outline the Krebs cycle, naming the 6C, 5C and 4C compounds, decarboxylation and dehydrogenation steps",
        "State the products of one turn of the cycle and of the whole process per glucose",
        "Explain the role of the reduced coenzymes NADH and FADH2",
    ],
    key_concepts=["Link reaction", "Acetyl coenzyme A", "Oxidative decarboxylation", "Krebs cycle", "Oxaloacetate", "Citrate", "NADH", "FADH2", "Decarboxylation"],
    blocks=[
        H("Introduction"),
        T("After glycolysis, the energy in glucose is still mostly locked up in the two pyruvate molecules. If oxygen is available, pyruvate enters the "
          "mitochondrion. There it is broken down completely to carbon dioxide, which you breathe out. This lesson covers the **link reaction** "
          "and the **Krebs cycle**, both in the matrix."),
        H("The link reaction"),
        T("Pyruvate (3C) is moved into the matrix by a transport protein. It is **decarboxylated** (a carbon is removed as CO₂) and **dehydrogenated** "
          "(hydrogen is removed and taken by NAD). The remaining 2C acetyl group is joined to **coenzyme A** to form **acetyl CoA**."),
        F(r"\text{pyruvate (3C)} + \text{CoA} + \text{NAD}^+ \rightarrow \text{acetyl CoA (2C)} + \text{CO}_2 + \text{NADH} + \text{H}^+", title="Link reaction"),
        T("This happens **twice** per glucose, because glycolysis gives two pyruvate."),
        H("The Krebs cycle"),
        D("The **Krebs cycle** is a cycle of enzyme-controlled reactions in the matrix in which the acetyl group of acetyl CoA is oxidised completely to CO₂, "
          "with the formation of reduced NAD, reduced FAD and a small amount of ATP. It is named after Hans Krebs, who worked it out in the 1930s.",
          title="Definition: Krebs cycle"),
        IMG("al-biu1-krebs.svg", alt="Link reaction converting pyruvate to acetyl CoA, then the Krebs cycle of six compounds from oxaloacetate to citrate and back, showing CO2, NADH, FADH2 and ATP outputs.",
            caption="Figure 1. The link reaction and Krebs cycle (simplified)."),
        KEY("Key steps in one turn of the cycle", "Follow the carbon atoms: 2 + 4 = 6, then 6 - 1 - 1 = 4.", cards=[
            ["Entry", "Acetyl CoA (2C) joins oxaloacetate (4C) to form citrate (6C). Coenzyme A is released and reused."],
            ["Two decarboxylations", "Citrate (6C) loses CO₂ to become a 5C compound, which loses CO₂ again to become a 4C compound. Two CO₂ are released per turn."],
            ["Four dehydrogenations", "Hydrogen is removed in four steps: three are taken by NAD (3 NADH) and one by FAD (1 FADH₂)."],
            ["One ATP", "One ATP is made by substrate-level phosphorylation (in mammals many books say GTP first, which then makes ATP; check your textbook)."],
            ["Regeneration", "The 4C compound is converted back to oxaloacetate, so the cycle can accept another acetyl group."],
        ]),
        T("The cycle turns **twice** for every glucose, because two acetyl CoA are formed. Oxygen is not used directly. "
          "The reduced coenzymes NADH and FADH₂ carry the hydrogen (electrons and protons) to the inner membrane, where they are used in oxidative phosphorylation."),
        CODE("""Products per molecule of glucose
Stage              CO2     NADH    FADH2    ATP (substrate-level)
Glycolysis          0       2       0        2 (net)
Link reaction (x2)  2       2       0        0
Krebs cycle (x2)    4       6       2        2
TOTAL               6      10       2        4""", "text", title="Totals per glucose"),
        T("All six carbon atoms of glucose have now left as CO₂ (2 from the link reaction and 4 from the Krebs cycle). This is why a cell needs oxygen "
          "only at the very end: the carbon is removed without oxygen, and oxygen is needed to remove the hydrogen."),
        H("Worked examples"),
        EX("Worked example 1: totals from two turns", intro="Calculate the number of NADH, FADH₂ and ATP made by the Krebs cycle alone from one glucose molecule.", steps=[
            S("Number of turns", text="One glucose gives 2 acetyl CoA, so the cycle turns twice."),
            S("NADH", math=r"3 \times 2 = 6"),
            S("FADH₂", math=r"1 \times 2 = 2"),
            S("ATP", math=r"1 \times 2 = 2"),
        ]),
        EX("Worked example 2: a carbon account", intro="Show that the carbon atoms of one glucose are all accounted for as CO₂ by the end of the Krebs cycle.", steps=[
            S("Glucose to pyruvate", math=r"6\text{C} \rightarrow 2 \times 3\text{C}"),
            S("Link reaction", math=r"2 \times 1\text{C} \text{ lost as CO}_2 = 2\text{ CO}_2"),
            S("Krebs cycle", math=r"2 \text{ turns} \times 2 \text{ CO}_2 = 4 \text{ CO}_2"),
            S("Total", math=r"2 + 4 = 6 \text{ CO}_2 \text{ (equal to the 6 C in glucose)}"),
        ]),
        EX("Worked example 3: effect of lack of oxygen", intro="Explain why the Krebs cycle slows down when a cell has no oxygen, even though oxygen is not a reactant in the cycle.", steps=[
            S("Link to NAD", text="The cycle needs NAD and FAD to accept hydrogen."),
            S("Oxygen at the end", text="Without oxygen the electron transport chain stops, so NADH and FADH₂ cannot be oxidised back to NAD and FAD."),
            S("Result", text="NAD and FAD run out; the dehydrogenation steps and so the cycle stop."),
        ]),
        MISTAKE("Saying that the Krebs cycle makes most of the ATP", "The cycle makes only 1 ATP per turn directly. Most ATP comes later, from NADH and FADH₂ in oxidative phosphorylation."),
        MISTAKE("Counting the cycle once per glucose", "Every product of the link reaction and Krebs cycle must be doubled for one glucose molecule."),
        QUIZ("How many molecules of CO₂ are released by the link reaction and Krebs cycle together, per molecule of glucose?",
             ["2", "4", "6", "12"], 2,
             "Link reaction: 2. Krebs cycle: 4. Total 6, equal to the carbon in glucose.",
             hint="Count per pyruvate first, then double.",
             feedback=["That is the link reaction only.", "That is the Krebs cycle only.", "", "That would double count; glucose has only 6 carbon atoms."]),
        QUIZ("Which compound combines with acetyl CoA at the start of the Krebs cycle?",
             ["Citrate", "Pyruvate", "Oxaloacetate", "Succinate"], 2,
             "Acetyl (2C) + oxaloacetate (4C) gives citrate (6C).",
             hint="The 4C compound is regenerated at the end.",
             feedback=["Citrate is the product, not the reactant.", "Pyruvate is converted to acetyl CoA before the cycle.", "", "Succinate is an intermediate inside the cycle."]),
        PQ("Describe the link reaction.",
           "Pyruvate enters the matrix. It is decarboxylated (CO₂ removed) and dehydrogenated (hydrogen taken by NAD to form NADH). The 2C acetyl group joins coenzyme A to form acetyl CoA, which enters the Krebs cycle."),
        PQ("Outline the Krebs cycle, naming the products of one turn.",
           "Acetyl CoA (2C) combines with oxaloacetate (4C) to form citrate (6C). Citrate is decarboxylated and dehydrogenated in steps, forming a 5C and then 4C compounds, and oxaloacetate is regenerated. One turn releases 2 CO₂ and produces 3 NADH, 1 FADH₂ and 1 ATP."),
        PQ("Calculate the total NADH made from one glucose molecule in glycolysis, the link reaction and the Krebs cycle together.",
           "Glycolysis 2 + link reaction 2 + Krebs cycle 6 = 10 NADH."),
        PQ("Explain the importance of NADH and FADH₂ in respiration.",
           "They carry hydrogen (electrons and protons) from glycolysis, the link reaction and the Krebs cycle to the electron transport chain on the inner membrane. There the energy of the electrons is used to pump protons, which drives ATP synthesis, so these coenzymes link the early stages to most of the ATP production."),
        TIP("Examiners often set a table of products or ask you to complete the carbon-atom count in the cycle. Practise redrawing the cycle with 6C, 5C and 4C labels."),
        SUM("The link reaction (matrix) converts pyruvate to acetyl CoA, releasing CO₂ and forming NADH.",
            "The Krebs cycle begins when acetyl CoA joins oxaloacetate to form citrate; two decarboxylations and four dehydrogenations follow.",
            "One turn: 2 CO₂, 3 NADH, 1 FADH₂, 1 ATP. Per glucose, double everything.",
            "Totals per glucose (glycolysis to Krebs): 6 CO₂, 10 NADH, 2 FADH₂, 4 ATP."),
    ],
))

# ------------------------------------------------------------------ 4. Electron transport chain and chemiosmosis
LESSONS.append(lesson(
    module=M1,
    topic="Oxidative phosphorylation",
    title="The electron transport chain and chemiosmosis",
    slug="biu1-electron-transport-chemiosmosis",
    minutes=24,
    summary="How electrons from NADH and FADH2 flow along carriers in the inner mitochondrial membrane, how protons are pumped, and how ATP synthase uses the proton gradient (chemiosmotic theory) to make ATP, with oxygen as the final acceptor.",
    objectives=[
        "Describe the passage of electrons along the electron transport chain to oxygen",
        "Explain how the energy released pumps protons into the intermembrane space",
        "Explain chemiosmosis and the working of ATP synthase",
        "Predict the effects of cyanide and of uncouplers on respiration",
    ],
    key_concepts=["Oxidative phosphorylation", "Electron transport chain", "Proton gradient", "Chemiosmosis", "ATP synthase", "Final electron acceptor", "Uncoupler", "Cyanide"],
    blocks=[
        H("Introduction"),
        T("Most of the ATP from respiration is made in the last stage, **oxidative phosphorylation**. The name tells you what happens: ADP is "
          "phosphorylated (a phosphate is added), using energy released by the oxidation of NADH and FADH₂. It takes place on the inner membrane of the mitochondrion."),
        T("Cassava is a staple in Cameroon, and it is a useful example here. Raw cassava roots contain compounds that release **cyanide**. "
          "Cyanide poisons the last carrier in the chain, so cells stop making ATP almost at once, even though oxygen is present. This is why cassava must be soaked, grated and cooked well before it is eaten."),
        D("**Oxidative phosphorylation** is the formation of ATP using energy released as electrons pass along the electron transport chain from reduced coenzymes to oxygen, "
          "coupled to a flow of protons through ATP synthase.",
          title="Definition: oxidative phosphorylation"),
        IMG("al-biu1-etc.svg", alt="Inner mitochondrial membrane with complexes I, III and IV, ubiquinone, cytochrome c and ATP synthase; electrons flow along the carriers and protons are pumped to the intermembrane space and return through ATP synthase.",
            caption="Figure 1. The electron transport chain and ATP synthase (simplified)."),
        H("The electron transport chain"),
        T("The chain is a series of electron carriers held in the inner membrane: protein complexes I, II, III and IV, with two mobile carriers, "
          "**ubiquinone (coenzyme Q)** between complexes I/II and III, and **cytochrome c** between III and IV."),
        T("**Step 1.** NADH gives its two electrons to complex I and becomes NAD⁺, ready to be used again in glycolysis, the link reaction and the Krebs cycle. FADH₂ gives its electrons "
          "to complex II (the succinate dehydrogenase enzyme of the Krebs cycle), entering the chain at a lower energy level."),
        T("**Step 2.** The electrons pass from carrier to carrier, each carrier having a lower energy level. At each step energy is released."),
        T("**Step 3.** Complexes I, III and IV use this energy to pump **protons (H⁺)** from the matrix into the intermembrane space. Complex II does not pump."),
        T("**Step 4.** At the end of the chain, complex IV passes the electrons to **oxygen**, the **final electron acceptor**. Oxygen combines with the electrons and with H⁺ from the matrix to form **water**."),
        F(r"\tfrac{1}{2}\text{O}_2 + 2\text{H}^+ + 2e^- \rightarrow \text{H}_2\text{O}", title="Final step"),
        H("Chemiosmosis and ATP synthase"),
        T("The pumping builds up a higher concentration of H⁺ in the intermembrane space than in the matrix. The inside of the matrix is also slightly more negative. "
          "Together this is an **electrochemical (proton) gradient**, also called the proton-motive force. The inner membrane is impermeable to H⁺, so protons can return only through **ATP synthase**."),
        D("**Chemiosmosis** is the synthesis of ATP using the energy of a proton gradient across a membrane, as protons diffuse back through ATP synthase. "
          "It was proposed by Peter Mitchell in 1961 (Nobel Prize 1978).",
          title="Chemiosmotic theory"),
        T("As H⁺ flow down their gradient through the channel in ATP synthase, a part of the enzyme rotates. The movement changes the shape of the catalytic sites, "
          "so ADP and inorganic phosphate (Pi) are joined to make ATP."),
        KEY("How many protons?", "Textbooks quote slightly different numbers; use these unless your teacher says otherwise.", cards=[
            ["NADH", "Electrons enter at complex I. About 10 H⁺ are pumped per NADH (4 + 4 + 2 at complexes I, III, IV)."],
            ["FADH₂", "Electrons enter at complex II. About 6 H⁺ are pumped per FADH₂ (III and IV only)."],
            ["ATP synthase", "About 4 H⁺ pass through for each ATP made (3 for the rotor and 1 for bringing in Pi)."],
        ]),
        T("So one NADH gives about 10 ÷ 4 = 2.5 ATP and one FADH₂ about 6 ÷ 4 = 1.5 ATP. Older textbooks give 3 and 2. **Check your textbook** and use its figures in calculations."),
        H("Interfering with the chain"),
        CODE("""Substance          Action                                           Effect
Cyanide, carbon    Binds to complex IV; electrons cannot reach O2    Chain stops, no proton gradient,
monoxide (CO)                                                         ATP production falls
Oligomycin         Blocks the ATP synthase channel                   Protons cannot return; chain slows
Uncoupler (DNP)    Makes the membrane leaky to H+                    O2 use continues, little ATP, heat
Brown fat protein  Natural channel for H+ (thermogenin, UCP1)        Energy released as heat in infants""", "text",
             title="Poisons and uncouplers"),
        H("Worked examples"),
        EX("Worked example 1: following the electrons", intro="Describe what happens to the electrons from one NADH molecule.", steps=[
            S("Entry", text="NADH donates 2 electrons to complex I and is oxidised to NAD⁺."),
            S("Along the chain", text="Electrons pass via ubiquinone, complex III, cytochrome c and complex IV, losing energy at each step."),
            S("Use of energy", text="The energy released pumps H⁺ across the inner membrane at complexes I, III and IV."),
            S("End", text="At complex IV the electrons combine with O₂ and H⁺ to make water."),
        ]),
        EX("Worked example 2: effect of an uncoupler", intro="An uncoupler is added to respiring mitochondria. Predict what happens to (a) oxygen uptake, (b) ATP made, (c) heat produced.", steps=[
            S("What the uncoupler does", text="It lets H⁺ leak back across the inner membrane without passing through ATP synthase."),
            S("(a) Oxygen uptake", text="Rises. The proton gradient cannot build up, so the chain keeps running faster and keeps using oxygen."),
            S("(b) ATP", text="Falls, because the protons do not drive ATP synthase."),
            S("(c) Heat", text="Rises, since the energy released by the electrons is lost as heat."),
        ]),
        EX("Worked example 3: why cyanide is fatal", intro="Explain why a person poisoned by cyanide dies even when there is plenty of oxygen in the blood.", steps=[
            S("Block", text="Cyanide binds to complex IV and stops electrons passing to oxygen."),
            S("Chain halts", text="Carriers stay reduced, no protons are pumped, no proton gradient forms."),
            S("Result", text="ATP synthesis stops. Tissues that need most ATP, such as brain and heart, fail first. Oxygen is present but cannot be used."),
        ]),
        MISTAKE("Saying that oxygen is needed to make ATP directly", "Oxygen is the final electron acceptor. It keeps the chain moving so that the proton gradient is maintained. ATP is made by ATP synthase."),
        MISTAKE("Saying that protons are pumped by ATP synthase", "Protons are pumped by complexes I, III and IV (energy from electrons). ATP synthase lets protons flow back and uses that flow to make ATP."),
        QUIZ("Which is the final electron acceptor in the electron transport chain?",
             ["NAD⁺", "Water", "Oxygen", "Cytochrome c"], 2,
             "Oxygen accepts the electrons and protons at complex IV to form water.",
             hint="What is breathed in for respiration?",
             feedback=["NAD⁺ is the acceptor in glycolysis and the Krebs cycle, not at the end of the chain.", "Water is the product, not the acceptor.", "", "Cytochrome c passes electrons to complex IV; it is not the last carrier."]),
        QUIZ("What provides the energy for the pumping of protons across the inner membrane?",
             ["ATP hydrolysis", "The flow of electrons along carriers", "Diffusion of glucose", "The flow of protons through ATP synthase"], 1,
             "Energy released as electrons pass from carrier to carrier is used to pump protons.",
             hint="Think about which step comes before the proton gradient exists.",
             feedback=["ATP is the product, not the energy source for the pumps.", "", "Glucose is not involved at this stage.", "That flow makes ATP; it comes after the pumping."]),
        PQ("Explain how the electron transport chain leads to the synthesis of ATP.",
           "Electrons from NADH and FADH₂ pass along carriers in the inner membrane. The energy released is used to pump H⁺ from the matrix to the intermembrane space, creating a proton gradient. H⁺ flow back through ATP synthase down their gradient, and the energy of this flow is used to join ADP and Pi to form ATP (chemiosmosis). Oxygen accepts the electrons at the end, forming water."),
        PQ("State two roles of oxygen in aerobic respiration in the mitochondrion.",
           "It is the final electron acceptor, so the chain keeps working; and it combines with electrons and H⁺ to form water, which removes the electrons and allows NAD and FAD to be regenerated."),
        PQ("Using the figures in this lesson, calculate how many ATP would be made from 4 FADH₂ molecules.",
           "Each FADH₂ pumps about 6 H⁺ and about 4 H⁺ are needed per ATP, so each gives 6 ÷ 4 = 1.5 ATP. 4 × 1.5 = 6 ATP."),
        PQ("A drug increases the permeability of the inner mitochondrial membrane to H⁺. Predict and explain the effect on body temperature.",
           "H⁺ leak back across the membrane without passing through ATP synthase, so the energy of the proton gradient is released as heat instead of making ATP. Respiration speeds up to try to make ATP, and body temperature rises."),
        TIP("Examiners like the words 'proton gradient' and 'down the gradient through ATP synthase'. Avoid 'the ATP is made by oxygen'. Cyanide and uncouplers are good examples to quote."),
        SUM("Electrons from NADH and FADH₂ pass along carriers in the inner membrane to oxygen, the final acceptor, forming water.",
            "Energy released pumps H⁺ into the intermembrane space at complexes I, III and IV, forming a proton gradient.",
            "H⁺ flow back through ATP synthase and drive ATP synthesis (chemiosmosis).",
            "About 2.5 ATP per NADH and 1.5 ATP per FADH₂ (older books: 3 and 2). Cyanide blocks the chain; uncouplers dissipate the gradient."),
    ],
))

# ------------------------------------------------------------------ 5. ATP yield
LESSONS.append(lesson(
    module=M1,
    topic="Oxidative phosphorylation",
    title="Counting the ATP yield of respiration",
    slug="biu1-atp-yield-per-glucose",
    minutes=22,
    summary="How to total the ATP from glycolysis, the link reaction, the Krebs cycle and oxidative phosphorylation, why the yield is a range (about 30 to 32, or 36 to 38 in older books), and how efficient respiration is.",
    objectives=[
        "Calculate the ATP yield per glucose from the numbers of NADH, FADH₂ and substrate-level ATP",
        "State the conventions (2.5 and 1.5, or 3 and 2 ATP per reduced coenzyme) and explain why the yield is only approximate",
        "Explain the effect of the shuttle that carries glycolytic NADH into the mitochondrion",
        "Calculate the efficiency of aerobic respiration and compare it with anaerobic respiration",
    ],
    key_concepts=["ATP yield", "NADH", "FADH₂", "Substrate-level ATP", "Shuttle", "Efficiency", "Respiratory substrate"],
    blocks=[
        H("Introduction"),
        T("Exam questions often say: 'How many molecules of ATP are made when one molecule of glucose is completely respired?' The honest answer is "
          "**about 30 to 32** in modern books and **36 to 38** in older books. This lesson shows you exactly where the numbers come from, so you can calculate the "
          "answer by whichever convention your teacher or textbook uses."),
        KEY("Two conventions", "Both are in use; always say which one you are using.", cards=[
            ["Modern values", "1 NADH = 2.5 ATP and 1 FADH₂ = 1.5 ATP. Total about 30 to 32 ATP per glucose."],
            ["Older textbook values", "1 NADH = 3 ATP and 1 FADH₂ = 2 ATP. Total about 36 to 38 ATP per glucose."],
        ]),
        TIP("Textbooks differ here, so check your textbook. In this course we show the modern values first and the older values in brackets. In the exam, write the figure your syllabus uses and show your working."),
        H("The ingredients"),
        CODE("""Per glucose, from the previous lessons
Stage                    NADH    FADH2    ATP (substrate-level)
Glycolysis (cytoplasm)    2       0        2
Link reaction             2       0        0
Krebs cycle               6       2        2
TOTAL                    10       2        4""", "text", title="Reduced coenzymes and ATP made without the chain"),
        F(r"\text{ATP} = (\text{NADH} \times 2.5) + (\text{FADH}_2 \times 1.5) + \text{substrate-level ATP}", title="Modern convention"),
        F(r"\text{ATP} = (10 \times 2.5) + (2 \times 1.5) + 4 = 25 + 3 + 4 = 32", title="Maximum yield, modern values"),
        F(r"\text{ATP} = (10 \times 3) + (2 \times 2) + 4 = 30 + 4 + 4 = 38", title="Maximum yield, older values"),
        H("Why 30 to 32 and not exactly 32?"),
        T("The NADH made in glycolysis is in the cytoplasm, but NADH cannot cross the inner membrane. Its electrons are carried in by a **shuttle**. "
          "In some tissues (liver, heart) the malate-aspartate shuttle delivers them to NADH in the matrix, so each glycolytic NADH is worth 2.5 ATP. "
          "In others (skeletal muscle, brain) the glycerol phosphate shuttle delivers them to FAD, so each is worth only 1.5 ATP."),
        T("In addition, some of the proton gradient is used for other jobs, for example importing pyruvate and phosphate into the matrix, and the membrane is slightly leaky. "
          "So the real yield is a little lower than the maximum. The values are best estimates, not exact numbers."),
        F(r"\text{With the glycerol phosphate shuttle: } 32 - 2 \times (2.5 - 1.5) = 30 \text{ ATP}", title="Lower limit, modern values"),
        H("Worked examples"),
        EX("Worked example 1: yield per pyruvate", intro="Calculate the ATP made from one pyruvate molecule from the link reaction onward (modern values).", steps=[
            S("Link reaction", text="1 NADH"),
            S("Krebs cycle (one turn)", text="3 NADH, 1 FADH₂, 1 ATP"),
            S("Total reduced coenzymes", text="4 NADH and 1 FADH₂, and 1 ATP"),
            S("Add", math=r"(4 \times 2.5) + (1 \times 1.5) + 1 = 10 + 1.5 + 1 = 12.5 \text{ ATP}"),
        ], check=r"2 \times 12.5 + 2 + (2 \times 2.5) = 32 \text{ ATP per glucose}"),
        EX("Worked example 2: percentage from oxidative phosphorylation", intro="What percentage of the maximum 32 ATP (modern values) is made by oxidative phosphorylation?", steps=[
            S("ATP from the chain", math=r"(10 \times 2.5) + (2 \times 1.5) = 28"),
            S("Percentage", math=r"\frac{28}{32} \times 100 = 87.5\%"),
            S("Conclusion", text="About 88 percent of the ATP is made by oxidative phosphorylation."),
        ]),
        EX("Worked example 3: efficiency", intro="The complete oxidation of one mole of glucose releases about 2870 kJ. The hydrolysis of one mole of ATP releases about 30.5 kJ. Calculate the efficiency if 32 ATP are made. (These are textbook values; they vary slightly between books.)", steps=[
            S("Energy captured in ATP", math=r"32 \times 30.5 = 976 \text{ kJ}"),
            S("Efficiency", math=r"\frac{976}{2870} \times 100 = 34\%"),
            S("Where is the rest?", text="About 66 percent is released as heat, which helps to keep mammals warm."),
        ]),
        EX("Worked example 4: comparing with glycolysis alone", intro="How many times more ATP does complete aerobic respiration give than glycolysis ending in lactate? Use 30 ATP aerobic.", steps=[
            S("Anaerobic yield", text="2 ATP per glucose."),
            S("Ratio", math=r"\frac{30}{2} = 15"),
            S("Meaning", text="A cell that depends on glycolysis only must break down about 15 times as much glucose for the same ATP."),
        ]),
        H("Other respiratory substrates"),
        T("Fatty acids give more ATP per gram than carbohydrates because they contain more hydrogen. Palmitic acid (16C) is cut into 8 acetyl CoA by 7 rounds of beta-oxidation, "
          "which make 7 FADH₂ and 7 NADH. Each acetyl CoA gives 10 ATP in the Krebs cycle and chain (3 NADH, 1 FADH₂, 1 ATP)."),
        F(r"(7 \times 1.5) + (7 \times 2.5) + (8 \times 10) - 2 = 106 \text{ ATP}", title="Palmitic acid (modern values; 2 ATP used to activate the fatty acid)"),
        MISTAKE("Giving one fixed number without a convention", "Write 'about 30 to 32 ATP' or state '38 ATP with 3 and 2 ATP per reduced coenzyme'. Do not mix the two systems in one calculation."),
        MISTAKE("Forgetting the ATP made without the chain", "The 2 ATP from glycolysis and 2 from the Krebs cycle are added to the ATP from NADH and FADH₂. Do not omit them."),
        QUIZ("Using 2.5 ATP per NADH and 1.5 per FADH₂, how many ATP are made by oxidative phosphorylation from 6 NADH and 2 FADH₂?",
             ["12", "15", "18", "24"], 2,
             "6 × 2.5 = 15 and 2 × 1.5 = 3, total 18.",
             hint="Calculate each coenzyme, then add.",
             feedback=["That counts 6 × 2 only.", "That leaves out the FADH₂.", "", "Check each product: 6 × 2.5 = 15 and 2 × 1.5 = 3. Substrate-level ATP is not part of this question."]),
        QUIZ("Why is the ATP yield from glycolytic NADH sometimes lower than that from mitochondrial NADH?",
             ["Glycolytic NADH is not oxidised", "Its electrons enter the mitochondrion by a shuttle that may pass them to FAD", "Glycolysis produces no NADH", "NADH is destroyed in the cytoplasm"], 1,
             "In the glycerol phosphate shuttle the electrons are passed to FAD, so they enter the chain at a lower level and yield about 1.5 ATP.",
             hint="NADH cannot cross the inner membrane.",
             feedback=["It is oxidised, after its electrons are brought in by a shuttle.", "", "Glycolysis makes 2 NADH.", "NADH is not destroyed; it is carried in by a shuttle."]),
        PQ("Calculate the maximum ATP yield from one glucose using 2.5 ATP per NADH and 1.5 ATP per FADH₂. State where each part of the total comes from.",
           "Glycolysis: 2 ATP and 2 NADH. Link reaction: 2 NADH. Krebs cycle: 6 NADH, 2 FADH₂, 2 ATP. Total 10 NADH, 2 FADH₂, 4 ATP. ATP = 25 + 3 + 4 = 32 (about 30 to 32 allowing for the shuttle)."),
        PQ("Using 3 ATP per NADH and 2 ATP per FADH₂, calculate the maximum yield per glucose, and say why textbooks give different figures.",
           "10 × 3 + 2 × 2 + 4 = 38. Newer research shows that about 10 H⁺ are pumped per NADH and about 4 H⁺ are needed per ATP, giving about 2.5 ATP; the older figures were rounded whole numbers, and some of the proton gradient is used for other jobs."),
        PQ("The complete oxidation of one mole of glucose releases about 2870 kJ and 30 ATP are made, each worth 30.5 kJ per mole. Calculate the efficiency.",
           "30 × 30.5 = 915 kJ. 915 / 2870 × 100 = about 32 percent. The rest is released as heat."),
        PQ("Compare the number of ATP made from one glucose by aerobic respiration and by lactate fermentation, and explain the difference.",
           "Aerobic: about 30 to 32. Lactate fermentation: 2. In fermentation, pyruvate is not fully oxidised and the electron transport chain is not used, so most of the energy remains in lactate and only the substrate-level ATP of glycolysis is made."),
        TIP("In calculation questions, show the table of NADH, FADH₂ and ATP first. Marks are given for each correct count even if the final answer follows a different convention."),
        SUM("Per glucose: 10 NADH, 2 FADH₂ and 4 substrate-level ATP (2 in glycolysis, 2 in the Krebs cycle).",
            "Modern values: 2.5 ATP per NADH, 1.5 per FADH₂, so about 30 to 32 ATP. Older books: 3 and 2, so 36 to 38.",
            "The range arises from the shuttle for glycolytic NADH and from other uses of the proton gradient.",
            "Efficiency is about one third; the rest is heat. Aerobic respiration gives about 15 times the ATP of fermentation."),
    ],
))

# ------------------------------------------------------------------ 6. Respiratory quotient
LESSONS.append(lesson(
    module=M1,
    topic="Respiratory quotient and anaerobic pathways",
    title="The respiratory quotient (RQ)",
    slug="biu1-respiratory-quotient",
    minutes=22,
    summary="How to define and calculate the respiratory quotient from equations and from respirometer data, the typical values for carbohydrate, lipid and protein, and what an RQ tells you about the substrate and about anaerobic respiration.",
    objectives=[
        "Define the respiratory quotient and state its formula",
        "Calculate RQ from a balanced equation and from gas volumes",
        "State typical RQ values for carbohydrate, lipid and protein and interpret an RQ value",
        "Describe how a simple respirometer is used to measure oxygen uptake and RQ",
    ],
    key_concepts=["Respiratory quotient", "Respiratory substrate", "Respirometer", "Oxygen uptake", "Carbon dioxide output", "Soda lime"],
    blocks=[
        H("Introduction"),
        T("When you run, your body burns a mixture of carbohydrate and fat. A person fasting for a long time, or an oil-rich seed such as a "
          "groundnut or castor seed germinating, burns more lipid. Can we tell what is being burned without opening the body or the seed? "
          "Yes: by comparing the carbon dioxide produced with the oxygen used. That ratio is the **respiratory quotient**."),
        D("The **respiratory quotient (RQ)** is the volume (or number of moles) of carbon dioxide produced divided by the volume (or number of moles) of oxygen taken in, over the same time and at the same temperature and pressure.",
          title="Definition: respiratory quotient"),
        F(r"\text{RQ} = \frac{\text{volume of CO}_2 \text{ produced}}{\text{volume of O}_2 \text{ consumed}}", title="Formula"),
        T("RQ has **no unit**, because it is a ratio of two volumes. At the same temperature and pressure, equal numbers of molecules of any gas occupy the same volume, "
          "so the ratio of volumes equals the ratio of moles in the balanced equation."),
        H("Calculating RQ from an equation"),
        T("Write the balanced equation for the complete oxidation of the substrate, then read the moles of CO₂ and O₂."),
        EX("Worked example 1: glucose", intro="Find the RQ for glucose, C₆H₁₂O₆.", steps=[
            S("Balanced equation", math=r"\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2 \rightarrow 6\text{CO}_2 + 6\text{H}_2\text{O}"),
            S("Moles of CO₂ and O₂", text="6 mol CO₂ and 6 mol O₂."),
            S("Divide", math=r"\text{RQ} = \frac{6}{6} = 1.0"),
        ], check=r"\text{Atoms: C } 6 = 6;\ \text{H } 12 = 12;\ \text{O } 6 + 12 = 12 + 6"),
        EX("Worked example 2: palmitic acid", intro="Find the RQ for the fatty acid palmitic acid, C₁₆H₃₂O₂.", steps=[
            S("Balanced equation", math=r"\text{C}_{16}\text{H}_{32}\text{O}_2 + 23\text{O}_2 \rightarrow 16\text{CO}_2 + 16\text{H}_2\text{O}"),
            S("Divide", math=r"\text{RQ} = \frac{16}{23} = 0.70"),
            S("Why lower than glucose", text="A fatty acid has much less oxygen in its molecule, so more oxygen has to be taken in to oxidise it."),
        ], check=r"\text{O atoms: } 2 + 46 = 48 = 32 + 16"),
        CODE("""Respiratory substrate          Typical RQ
Carbohydrate (glucose)         1.0
Lipid (fat, oil)               about 0.7
Protein                        about 0.9
Mixture in a resting person    about 0.8
Anaerobic respiration          more than 1, or CO2 with no O2 used (RQ undefined)
Organic acid (e.g. malic acid) more than 1 (about 1.33)""", "text", title="Typical RQ values (check your textbook for small differences)"),
        T("An RQ of **1.0** suggests carbohydrate; about **0.7** suggests lipid; about **0.9** suggests protein; values between mean a mixture. "
          "A value **above 1.0** suggests that some carbon dioxide comes from anaerobic respiration (in hard exercise, lactic acid is also buffered by hydrogencarbonate in the blood, which releases extra CO₂), or that the substrate is a more oxidised molecule such as an organic acid, or "
          "that fat is being made from carbohydrate (the carbohydrate already contains more oxygen than fat, so less oxygen is taken in)."),
        H("Measuring RQ with a respirometer"),
        T("A simple respirometer has a tube containing living material (germinating seeds, small insects such as woodlice or maggots), a capillary tube with a coloured drop, "
          "and a chemical that absorbs CO₂, such as **potassium hydroxide solution** or **soda lime**. The material is separated from the absorbent by a platform."),
        T("**Experiment 1, with CO₂ absorbent.** CO₂ is absorbed, so the drop moves towards the organism by a distance that shows the **volume of O₂ used**."),
        T("**Experiment 2, without absorbent.** CO₂ released replaces the O₂ used, so the drop moves by the **difference between O₂ used and CO₂ produced**. "
          "If the drop does not move, RQ = 1.0 (as for carbohydrate). If the drop moves towards the organism, more O₂ is used than CO₂ produced (RQ < 1.0)."),
        T("Use a **control tube** with glass beads of the same volume instead of living material, to allow for temperature and pressure changes. Keep the apparatus in a water bath at constant temperature."),
        EX("Worked example 3: respirometer data", intro="Germinating castor seeds in a respirometer used 60 mm³ of oxygen in 30 minutes (with absorbent). Without absorbent, the drop moved 18 mm³ towards the seeds. Find the RQ.", steps=[
            S("O₂ used", math=r"60 \text{ mm}^3"),
            S("Net volume change without absorbent", text="O₂ used minus CO₂ produced is 18 mm³."),
            S("CO₂ produced", math=r"60 - 18 = 42 \text{ mm}^3"),
            S("RQ", math=r"\frac{42}{60} = 0.70"),
            S("Conclusion", text="0.7 suggests the seeds are using lipid, as expected for oil-rich seeds (teaching data)."),
        ]),
        EX("Worked example 4: mixture of substrates", intro="A student at rest uses 300 cm³ of oxygen per minute and produces 240 cm³ of carbon dioxide per minute. Find the RQ. What fraction of the oxygen is used on carbohydrate if the other substrate is lipid with RQ 0.7?", steps=[
            S("RQ", math=r"\frac{240}{300} = 0.80"),
            S("Let x be the fraction of O₂ used on carbohydrate (RQ 1.0)", math=r"x(1.0) + (1 - x)(0.7) = 0.80"),
            S("Solve", math=r"0.7 + 0.3x = 0.80 \Rightarrow x = \frac{0.10}{0.30} = \frac{1}{3}"),
            S("Answer", text="One third of the oxygen is used to oxidise carbohydrate and two thirds to oxidise lipid (an estimate; protein is ignored)."),
        ]),
        MISTAKE("Turning the fraction upside down", "RQ is CO₂ produced over O₂ used. If you write O₂ over CO₂ the carbohydrate value would still be 1.0 but fat would give 1.4. Always put CO₂ on the top."),
        MISTAKE("Giving a unit", "RQ is a ratio of two volumes, so it has no unit."),
        MISTAKE("Using the equation without balancing it", "Count the atoms of C, H and O on both sides first. The RQ of fat depends on the correct number of O₂ molecules."),
        QUIZ("An organism respires and gives an RQ of 0.7. What is it most likely using as the substrate?",
             ["Carbohydrate", "Lipid", "Protein", "Ethanol made by fermentation"], 1,
             "Lipid has little oxygen in its molecule, so it needs more O₂ per CO₂: RQ about 0.7.",
             hint="Which substrate is very rich in hydrogen and poor in oxygen?",
             feedback=["Carbohydrate gives RQ = 1.0.", "", "Protein gives about 0.9.", "Fermentation uses no oxygen, so its RQ is not defined."]),
        QUIZ("In a respirometer with soda lime, what does the movement of the drop measure?",
             ["Volume of CO₂ produced", "Volume of O₂ used", "Volume of O₂ minus CO₂", "Volume of water vapour made"], 1,
             "Soda lime absorbs CO₂, so the pressure change is due to the loss of O₂ only.",
             hint="What does the absorbent remove?",
             feedback=["CO₂ is removed by the absorbent, so it cannot be measured here.", "", "That is what is measured when no absorbent is used.", "Water vapour is not measured in this way."]),
        PQ("Calculate the RQ of the fatty acid oleic acid, C₁₈H₃₄O₂, which needs 25.5 mol O₂ and gives 18 mol CO₂ per mole. Comment on the value.",
           "RQ = 18 / 25.5 = 0.71. It is close to 0.7, the typical RQ for lipid."),
        PQ("Define RQ and explain why the RQ of carbohydrate is 1.0.",
           "RQ = volume of CO₂ produced / volume of O₂ consumed. In the oxidation of glucose, 6 mol of CO₂ are produced for 6 mol of O₂ used, so the ratio is 1.0."),
        PQ("A mixture of insects in a respirometer used 24 mm³ of oxygen and produced 21.6 mm³ of CO₂ in 10 minutes. Calculate the RQ and say which substrate is most likely.",
           "RQ = 21.6 / 24 = 0.90. This is typical of protein (or a mixture of carbohydrate and lipid)."),
        PQ("Explain why a respirometer experiment needs a control tube containing glass beads.",
           "The beads have the same volume as the organism but do not respire. Any movement of the drop in the control tube is caused by changes in room temperature or atmospheric pressure, so the experimental readings can be corrected for it."),
        TIP("RQ appears in Paper 1 as a calculation or an interpretation question, and in Paper 3 (practical) with a respirometer. In Paper 2 you may be asked to explain a value above 1 as anaerobic respiration."),
        SUM("RQ = volume of CO₂ produced / volume of O₂ consumed; it has no unit.",
            "Carbohydrate 1.0, lipid about 0.7, protein about 0.9. A mixture gives values between.",
            "A respirometer with CO₂ absorbent measures O₂ used; without absorbent it shows the difference between O₂ used and CO₂ produced.",
            "RQ above 1.0 suggests anaerobic respiration or an oxygen-rich substrate; use a control tube for temperature and pressure changes."),
    ],
))

# ------------------------------------------------------------------ 7. Anaerobic pathways
LESSONS.append(lesson(
    module=M1,
    topic="Respiratory quotient and anaerobic pathways",
    title="Anaerobic pathways: lactate and ethanol fermentation",
    slug="biu1-anaerobic-respiration-fermentation",
    minutes=22,
    summary="How lactate and alcoholic fermentation regenerate NAD so that glycolysis can continue without oxygen, their ATP yield, the oxygen debt, and calculations on ethanol, carbon dioxide and ATP.",
    objectives=[
        "Describe lactate fermentation in muscle and alcoholic fermentation in yeast",
        "Explain why anaerobic respiration is needed to regenerate NAD and why its ATP yield is low",
        "Explain the oxygen debt and how lactate is dealt with afterwards",
        "Calculate masses and volumes of products formed by fermentation",
    ],
    key_concepts=["Anaerobic respiration", "Fermentation", "Lactate", "Ethanol", "NAD regeneration", "Oxygen debt", "Lactate dehydrogenase", "Cori cycle"],
    blocks=[
        H("Introduction"),
        T("A sprinter at the end of a 100 m race, a yeast cell in palm wine sap and a cassava root in a flooded field all respire "
          "without enough oxygen. Without oxygen the electron transport chain stops, NADH piles up and glycolysis would stop for lack of NAD. "
          "**Anaerobic respiration** solves this problem by turning NADH back into NAD without using oxygen."),
        D("**Anaerobic respiration** (fermentation) is the breakdown of glucose without oxygen. Glycolysis continues; pyruvate is converted to lactate or to ethanol and carbon dioxide, "
          "and NADH is oxidised to NAD. It gives a net 2 ATP per glucose.",
          title="Definition: anaerobic respiration"),
        H("Lactate fermentation (animals, some bacteria)"),
        T("In vigorously working muscle, pyruvate accepts hydrogen from NADH. The enzyme is **lactate dehydrogenase**."),
        F(r"\text{pyruvate} + \text{NADH} + \text{H}^+ \rightarrow \text{lactate} + \text{NAD}^+", title="Lactate fermentation"),
        T("The NAD formed returns to glycolysis, so that 2 ATP can still be made per glucose. No carbon dioxide is released. Lactate is made in the muscle and carried by blood to the liver."),
        H("Alcoholic fermentation (yeast, many plant tissues)"),
        T("Yeast converts pyruvate in two steps. First **pyruvate decarboxylase** removes CO₂ to make **ethanal**. Then **alcohol dehydrogenase** uses NADH to reduce ethanal to **ethanol**."),
        F(r"\text{pyruvate} \rightarrow \text{ethanal} + \text{CO}_2 \qquad \text{ethanal} + \text{NADH} + \text{H}^+ \rightarrow \text{ethanol} + \text{NAD}^+", title="Alcoholic fermentation"),
        F(r"\text{C}_6\text{H}_{12}\text{O}_6 \rightarrow 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2 \quad (+\ 2\text{ ATP})", title="Overall equation"),
        T("Raphia and oil palm sap fermented by yeasts and bacteria becomes palm wine, and yeast in dough makes bread rise: both depend on this pathway. The reaction is not reversible in yeast, and ethanol is toxic to yeast at about 12 to 15 percent."),
        KEY("Lactate and alcoholic fermentation compared", "Both regenerate NAD; they differ in the final product.", cards=[
            ["Lactate", "Pyruvate + NADH gives lactate + NAD. One step. No CO₂. Muscle. Reversible in the liver."],
            ["Ethanol", "Pyruvate loses CO₂ to give ethanal; ethanal + NADH gives ethanol + NAD. Two steps. CO₂ released. Yeast, plants. Not reversible."],
        ]),
        H("Oxygen debt"),
        T("After hard exercise you keep breathing heavily. The extra oxygen taken in after exercise is the **oxygen debt** (excess post-exercise oxygen consumption). It is used to oxidise "
          "some lactate to pyruvate in the liver (the pyruvate then enters the Krebs cycle) or to convert lactate back to glucose (the **Cori cycle**), to restore oxygen to myoglobin, and to restore ATP and creatine phosphate levels."),
        T("Lactate lowers the pH of muscle and blood, which reduces enzyme activity and contributes to the pain and tiredness of vigorous exercise."),
        H("Why is the yield so low?"),
        T("Glycolysis gives only 2 ATP. In fermentation the pyruvate is not oxidised further, so most of the chemical energy stays in the lactate or ethanol (ethanol can be burned as fuel). "
          "Fermenting cells therefore use glucose quickly. The comparison is about 2 ATP against about 30 to 32 ATP for aerobic respiration."),
        EX("Worked example 1: why is NAD regenerated?", intro="Explain why a cell without oxygen must convert pyruvate to lactate or ethanol.", steps=[
            S("Glycolysis needs NAD", text="The oxidation step of glycolysis uses NAD."),
            S("No oxygen", text="Without oxygen the electron transport chain cannot oxidise NADH to NAD."),
            S("Solution", text="Converting pyruvate to lactate or ethanol oxidises NADH to NAD, so glycolysis can continue to make 2 ATP per glucose."),
        ]),
        EX("Worked example 2: ethanol and CO₂ from yeast", intro="Yeast ferments 36 g of glucose (Mr 180). Calculate the mass of ethanol (Mr 46) and the volume of CO₂ at room temperature and pressure (1 mol = 24 dm³).", steps=[
            S("Moles of glucose", math=r"\frac{36}{180} = 0.20 \text{ mol}"),
            S("Moles of ethanol and CO₂", text="1 glucose gives 2 ethanol and 2 CO₂. So 0.40 mol of each."),
            S("Mass of ethanol", math=r"0.40 \times 46 = 18.4 \text{ g}"),
            S("Volume of CO₂", math=r"0.40 \times 24 = 9.6 \text{ dm}^3"),
        ], check=r"\text{Mass: } 2 \times 46 + 2 \times 44 = 180 \text{ g, equal to the mass of 1 mol glucose}"),
        EX("Worked example 3: ATP comparison", intro="A muscle makes 40 ATP by lactate fermentation. How many glucose molecules are used? How many would be needed aerobically at 30 ATP per glucose?", steps=[
            S("Fermentation", math=r"\frac{40}{2} = 20 \text{ glucose}"),
            S("Aerobic", math=r"\frac{40}{30} \approx 1.3 \text{ glucose}"),
            S("Comment", text="Anaerobic respiration uses about 15 times as much glucose for the same ATP."),
        ]),
        MISTAKE("Saying lactate is made in yeast or ethanol in muscle", "Yeast makes ethanol and CO₂. Muscle makes lactate and no CO₂. Learn the pairs: yeast with ethanol; mammals with lactate."),
        MISTAKE("Thinking fermentation makes the ATP from the pyruvate step", "The 2 ATP come from glycolysis (substrate-level). The conversion of pyruvate to lactate or ethanol makes no ATP; its purpose is to regenerate NAD."),
        QUIZ("What is the purpose of converting pyruvate to lactate in muscle?",
             ["To make more ATP", "To regenerate NAD so glycolysis can continue", "To remove carbon dioxide", "To make glucose"], 1,
             "NADH is oxidised to NAD, which glycolysis needs.",
             hint="Which coenzyme runs out when the chain stops?",
             feedback=["No additional ATP is made in this step.", "", "Lactate fermentation releases no CO₂.", "Glucose is made later in the liver, not in this step."]),
        QUIZ("Which of these is made when yeast ferments glucose?",
             ["Lactate only", "Ethanol and carbon dioxide", "Ethanol only", "Water and carbon dioxide"], 1,
             "Pyruvate loses CO₂ (to give ethanal) and then ethanal is reduced to ethanol.",
             hint="Think of what makes dough rise.",
             feedback=["Lactate is the product in animals.", "", "Carbon dioxide is also produced.", "That is the product of aerobic respiration, not fermentation."]),
        PQ("Describe the conversion of pyruvate to ethanol in yeast.",
           "Pyruvate is decarboxylated by pyruvate decarboxylase to ethanal and CO₂. Ethanal is then reduced to ethanol by alcohol dehydrogenase, using NADH, which is oxidised to NAD."),
        PQ("Explain what is meant by oxygen debt and how it is repaid.",
           "It is the extra oxygen taken in after exercise. It is used mainly in the liver to oxidise some lactate to pyruvate (which enters the Krebs cycle) or to convert lactate back to glucose, to restore myoglobin oxygen and to restore ATP and creatine phosphate."),
        PQ("Calculate the mass of glucose (Mr 180) that must be fermented by yeast to produce 9.2 g of ethanol (Mr 46).",
           "Moles of ethanol = 9.2 / 46 = 0.20 mol. Glucose gives 2 ethanol, so glucose = 0.10 mol. Mass = 0.10 × 180 = 18 g."),
        PQ("Give two reasons why anaerobic respiration gives much less ATP than aerobic respiration.",
           "Pyruvate is not oxidised further, so most of the energy stays in lactate or ethanol. The Krebs cycle and electron transport chain are not used, so the many ATP from NADH and FADH₂ are not made; only the 2 ATP from glycolysis."),
        TIP("In Paper 2, link anaerobic respiration to RQ (CO₂ released without O₂ used) and to sport or brewing for application marks. In Paper 3 you may investigate yeast fermentation by collecting gas."),
        SUM("Without oxygen, glycolysis continues if NADH is oxidised to NAD by converting pyruvate to lactate (animals) or ethanol and CO₂ (yeast).",
            "The net yield is 2 ATP per glucose, about one fifteenth of the aerobic yield.",
            "Oxygen debt is the extra oxygen needed after exercise to deal with lactate and restore stores.",
            "In calculations use 1 glucose gives 2 ethanol and 2 CO₂, or 2 lactate."),
    ],
))

# ------------------------------------------------------------------ 8. Feedback control
LESSONS.append(lesson(
    module=M2,
    topic="Feedback control",
    title="Homeostasis and feedback control",
    slug="biu1-feedback-control",
    minutes=20,
    summary="What homeostasis is and why it matters, the parts of a control loop (receptor, coordinator, effector), negative feedback with a set point, and the few important cases of positive feedback.",
    objectives=[
        "Define homeostasis and explain why a stable internal environment is needed",
        "Describe the parts of a negative feedback loop and apply them to an example",
        "Explain why negative feedback gives small fluctuations around a set point",
        "Give examples of positive feedback and explain how they differ",
    ],
    key_concepts=["Homeostasis", "Internal environment", "Set point", "Receptor", "Coordinator", "Effector", "Negative feedback", "Positive feedback", "Antagonistic effectors"],
    blocks=[
        H("Introduction"),
        T("A fisherman on the Wouri river works in the midday sun, and a mountain farmer near Bamenda shivers on a cold morning. "
          "Yet the temperature of the deep part of the body of both stays close to 37 °C. The blood glucose, water content, pH and "
          "salt balance of their bodies also stay within narrow limits. The control of this stable inside condition is called **homeostasis**."),
        D("**Homeostasis** is the maintenance of a relatively constant internal environment (the tissue fluid and blood) within narrow limits, in spite of changes in the external environment and in the activity of the body.",
          title="Definition: homeostasis"),
        T("Why does it matter? Enzymes work best at an optimum temperature and pH. Cells need a stable water potential so that they do not shrink or swell by osmosis. Nerve cells need the right ion concentrations. If the internal environment drifts too far, cells stop working."),
        H("A control loop"),
        IMG("al-biu1-feedback-loop.svg", alt="Negative feedback loop: stimulus, receptor, control centre, effector, response, variable returns towards set point, with a dashed arrow back to the stimulus.",
            caption="Figure 1. A negative feedback loop."),
        KEY("Parts of the loop", "Every homeostatic mechanism has the same parts.", cards=[
            ["Set point", "The normal or target value of the variable, for example 37 °C or 5 mmol per litre of blood glucose."],
            ["Receptor", "Detects a change in the variable (for example thermoreceptors, osmoreceptors, chemoreceptors)."],
            ["Coordinator (control centre)", "Compares the information with the set point and sends instructions (for example the hypothalamus, the pancreas or the brain stem)."],
            ["Effector", "Carries out the response (a muscle or a gland)."],
            ["Response", "Changes the variable. The change is detected by the receptor again, which closes the loop."],
        ]),
        D("**Negative feedback** is a control mechanism in which a change in a variable triggers a response that reverses the change and returns the variable towards its set point.",
          title="Definition: negative feedback"),
        T("Because the effector acts only when the variable moves away from the set point, the variable **oscillates** (rises and falls) in a small range around the set point. "
          "The control is never perfect, because there is a delay between detection and the effect of the response."),
        T("Many variables are controlled by **antagonistic effectors**, which push in opposite directions. For example, insulin lowers blood glucose and glucagon raises it; sweating cools and shivering warms. "
          "Two opposing controls give finer control than one, and allow correction in both directions."),
        H("Positive feedback"),
        D("**Positive feedback** is a process in which a change in a variable triggers a response that increases the change further, moving the variable away from the starting value.",
          title="Definition: positive feedback"),
        T("Positive feedback is not usually part of homeostasis, because it would cause a runaway change. It is useful when a process must be completed quickly, and it stops when an event is finished. Examples:"),
        CODE("""Process                         How the positive feedback works                   What stops it
Opening of Na+ channels         Depolarisation opens more Na+ channels            Inactivation of channels,
in an axon (action potential)   so more Na+ enter                                 K+ channels open
Labour (childbirth)             Stretch of the cervix triggers oxytocin, which    Birth of the baby removes
                                makes the uterus contract more, stretching more   the stretch
Blood clotting                  Platelets release substances that attract more    Clot seals the damaged
                                platelets and clotting factors                    vessel
Ovulation (LH surge)            High oestrogen increases LH release, which        Follicle ruptures; hormone
                                increases oestrogen                               levels change""", "text", title="Examples of positive feedback"),
        H("Worked examples"),
        EX("Worked example 1: a negative feedback loop for breathing", intro="Blood carbon dioxide rises during exercise. Describe how negative feedback brings it back to normal.", steps=[
            S("Receptors", text="Chemoreceptors in the medulla and in the carotid and aortic bodies detect a fall in blood pH caused by extra CO₂."),
            S("Coordinator", text="The breathing centre in the medulla oblongata sends more impulses."),
            S("Effectors", text="The diaphragm and intercostal muscles contract faster and more strongly, so breathing rate and depth increase."),
            S("Response and feedback", text="More CO₂ is removed in the lungs. Blood CO₂ and pH return towards normal and the signal to the breathing centre falls."),
        ]),
        EX("Worked example 2: reading a graph", intro="The core temperature of a person is recorded every 10 minutes: 37.0, 37.4, 37.7, 37.3, 36.9, 36.7, 37.0 °C. Explain the pattern in terms of feedback.", steps=[
            S("Fluctuation", text="The temperature rises above 37 °C and then falls below it: it oscillates around the set point."),
            S("Why it rises", text="A disturbance (such as exercise or a warm room) raised the temperature."),
            S("Why it returns", text="Receptors detected the rise, and effectors (sweating, vasodilation) cooled the body. The temperature fell slightly below the set point, then effectors (vasoconstriction, shivering) warmed it back to 37 °C."),
            S("Conclusion", text="Small fluctuations around a set point show that negative feedback is operating."),
        ]),
        EX("Worked example 3: positive or negative?", intro="During labour, stretching of the cervix increases the secretion of oxytocin. Oxytocin makes the uterus contract more strongly. State the type of feedback and explain.", steps=[
            S("Type", text="Positive feedback."),
            S("Reason", text="The response (stronger contraction) increases the stimulus (stretch) which produces more oxytocin, so the change increases rather than being reversed."),
            S("End", text="It stops when the baby is born and the stretch on the cervix is removed."),
        ]),
        MISTAKE("Saying that negative feedback means 'bad'", "'Negative' means that the response opposes the change. Negative feedback is the main way the body keeps conditions stable."),
        MISTAKE("Saying homeostasis keeps conditions constant", "It keeps them within narrow limits. The variable moves a little above and below the set point. Use the phrase 'relatively constant'."),
        QUIZ("Which of these is an example of positive feedback?",
             ["Sweating when the body is too hot", "Release of insulin when blood glucose rises", "Spread of depolarisation in an axon as Na⁺ channels open", "Increase in breathing rate when blood CO₂ rises"], 2,
             "Depolarisation opens Na⁺ channels, which causes more depolarisation, so the change builds up.",
             hint="Which one increases the change instead of reversing it?",
             feedback=["Sweating cools the body, so it reverses the change.", "Insulin lowers glucose: negative feedback.", "", "Faster breathing removes CO₂ and reverses the rise."]),
        QUIZ("What is the role of the coordinator in a feedback loop?",
             ["To detect changes in the environment", "To compare the information with the set point and send instructions to the effector", "To carry out the response", "To increase the size of the stimulus"], 1,
             "The coordinator (for example the hypothalamus) compares the input with the set point and sends a signal.",
             hint="It is neither the detector nor the doer.",
             feedback=["That is the receptor.", "", "That is the effector.", "Negative feedback reduces the stimulus; it does not increase it."]),
        PQ("Define homeostasis and explain why it is important to cells.",
           "Homeostasis is the maintenance of a relatively constant internal environment within narrow limits. It is important because enzymes need a stable temperature and pH to work well, cells need constant water potential to avoid osmotic damage, and nerve and muscle cells need stable ion concentrations."),
        PQ("Describe the parts of a negative feedback loop, using body temperature as an example.",
           "Receptors: thermoreceptors in the skin and hypothalamus detect a change. Coordinator: the hypothalamus compares with the set point of about 37 °C. Effectors: sweat glands, skin arterioles and muscles. Response: they cool or warm the body, returning the temperature to the set point, which reduces the original stimulus."),
        PQ("Explain why two antagonistic effectors give better control than one.",
           "With one effector, the variable can be corrected in only one direction and has to drift back passively in the other. Two opposing effectors can correct a rise or a fall quickly, so the variable stays closer to the set point."),
        PQ("Give one difference between positive and negative feedback and one example of positive feedback.",
           "Negative feedback reverses a change and keeps the variable near the set point; positive feedback increases the change and moves the variable away. An example is the release of oxytocin during labour (or blood clotting, or the opening of Na⁺ channels)."),
        TIP("Feedback appears in Paper 2 as part of almost every homeostasis question (temperature, glucose, osmoregulation). Name the receptor, coordinator and effector each time. The Board's 2023 report also asks candidates to link feedback to the hypothalamus and pituitary."),
        SUM("Homeostasis keeps the internal environment relatively constant, so enzymes, cells and nerves work normally.",
            "A control loop has a set point, receptor, coordinator, effector and response.",
            "Negative feedback reverses a change and gives small oscillations around the set point; antagonistic effectors improve control.",
            "Positive feedback amplifies a change for a short, complete event, such as an action potential, labour or clotting."),
    ],
))

# ------------------------------------------------------------------ 9. Liver and ornithine cycle
LESSONS.append(lesson(
    module=M2,
    topic="The liver and the ornithine cycle",
    title="The liver and the ornithine cycle",
    slug="biu1-liver-ornithine-cycle",
    minutes=22,
    summary="The structure of a liver lobule, the main functions of the liver, deamination of amino acids and the ornithine cycle that converts toxic ammonia into urea.",
    objectives=[
        "Describe the blood supply and the structure of a liver lobule",
        "List the main functions of hepatocytes",
        "Explain deamination and the formation of urea in the ornithine cycle",
        "Calculate nitrogen and urea masses from protein intake",
    ],
    key_concepts=["Hepatocyte", "Sinusoid", "Kupffer cell", "Hepatic portal vein", "Deamination", "Ammonia", "Ornithine cycle", "Urea", "Detoxification"],
    blocks=[
        H("Introduction"),
        T("The liver is the largest internal organ, with a mass of about 1.5 kg in an adult. It lies under the diaphragm on the right side. "
          "It is a chemical factory and warehouse: nearly every nutrient absorbed from the gut is processed here first. "
          "In Cameroon the liver is also at risk from malaria, hepatitis B, alcohol and some herbal medicines, so its work matters for health."),
        H("Structure of the liver"),
        T("The liver receives blood from two vessels. The **hepatic artery** brings oxygenated blood from the heart. The **hepatic portal vein** brings blood, rich in absorbed nutrients, from the gut. "
          "Both mix in channels called **sinusoids**, which run between rows of liver cells (**hepatocytes**), then drain into a branch of the **hepatic vein**."),
        T("The liver is built from thousands of **lobules** about 1 mm across. In a lobule, hepatocytes are arranged in rows radiating from a central vein. Sinusoids are lined by "
          "cells with gaps and contain **Kupffer cells**, macrophages that remove old red blood cells and bacteria. Small channels called **bile canaliculi** collect bile from hepatocytes and carry it to bile ducts."),
        KEY("What makes hepatocytes suited to their work", "Link each structure to a job.", cards=[
            ["Large surface area", "Microvilli face the sinusoids, so substances pass quickly between blood and cell."],
            ["Many mitochondria", "Release ATP for active transport and for the ornithine cycle."],
            ["Much smooth and rough ER and Golgi", "Make plasma proteins, cholesterol, bile salts; detoxify drugs."],
            ["Many lysosomes and peroxisomes", "Break down worn-out cell parts and harmful substances."],
            ["Glycogen granules and fat droplets", "Store energy."],
        ]),
        H("Functions of the liver"),
        CODE("""Area                 Function
Carbohydrate         Glycogen stored (glycogenesis) or broken down (glycogenolysis);
                     glucose made from amino acids and lipids (gluconeogenesis).
Protein              Deamination of excess amino acids; urea made; transamination;
                     plasma proteins (albumin, fibrinogen) made.
Lipid                Cholesterol made; fatty acids oxidised or packaged as lipoproteins.
Detoxification       Alcohol, drugs, hormones, ammonia broken down or made harmless.
Bile                 Bile salts made (emulsify fats); bile pigments from haemoglobin.
Storage              Vitamins A, D, B12, iron and glycogen.
Heat                 Metabolic reactions release heat that warms the blood.""", "text", title="Main functions"),
        H("Deamination and the ornithine cycle"),
        T("The body cannot store excess amino acids. In the liver, **deamination** removes the amine group (NH₂) from an amino acid. This forms ammonia (NH₃) and a keto acid. "
          "The keto acid may enter the Krebs cycle for respiration or be converted into carbohydrate or fat."),
        F(r"\text{amino acid} + \tfrac{1}{2}\text{O}_2 \rightarrow \text{keto acid} + \text{NH}_3", title="Deamination (simplified)"),
        T("**Ammonia is very toxic** and very soluble. It raises the pH of cells and upsets the nervous system. The liver therefore converts it at once to **urea**, which is far less toxic. "
          "This conversion is the **ornithine cycle** (also called the urea cycle). It costs ATP."),
        IMG("al-biu1-ornithine-cycle.svg", alt="Ornithine cycle: ornithine to citrulline (with carbamoyl phosphate), to argininosuccinate (with aspartate and ATP), to arginine (releasing fumarate), then arginine splits into urea and ornithine.",
            caption="Figure 1. The ornithine cycle (simplified)."),
        KEY("Outline of the cycle", "Ornithine is regenerated, so the cycle can repeat.", cards=[
            ["Step 1", "Ammonia, CO₂ and 2 ATP form carbamoyl phosphate (in the mitochondrion)."],
            ["Step 2", "Carbamoyl phosphate joins ornithine to form citrulline, which leaves the mitochondrion."],
            ["Step 3", "Citrulline joins aspartate (second nitrogen source, with ATP) to form argininosuccinate."],
            ["Step 4", "Argininosuccinate splits into arginine and fumarate; fumarate can enter the Krebs cycle."],
            ["Step 5", "Arginine is hydrolysed by arginase to urea and ornithine. Urea goes into the blood and is excreted by the kidneys."],
        ]),
        F(r"2\text{NH}_3 + \text{CO}_2 \rightarrow \text{CO(NH}_2)_2 + \text{H}_2\text{O}", title="Overall result (3 ATP used; textbooks count 3 ATP or 4 high-energy bonds, check yours)"),
        T("Urea, CO(NH₂)₂, has two nitrogen atoms. Other animals excrete nitrogen differently: bony fish excrete ammonia directly into water; birds and reptiles make uric acid, which needs little water."),
        H("Worked examples"),
        EX("Worked example 1: nitrogen and urea from protein", intro="A teenager eats 90 g of protein in a day. Protein is about 16 percent nitrogen by mass. If all the nitrogen is excreted as urea (Mr 60, nitrogen 28 of 60), find the mass of urea (a teaching estimate).", steps=[
            S("Mass of nitrogen", math=r"90 \times 0.16 = 14.4 \text{ g}"),
            S("Fraction of urea that is nitrogen", math=r"\frac{28}{60} = 0.467"),
            S("Mass of urea", math=r"\frac{14.4}{0.467} = 30.9 \text{ g}"),
            S("Comment", text="In practice about 80 to 90 percent of the nitrogen is excreted as urea, so the real mass is a little less."),
        ]),
        EX("Worked example 2: why not just excrete ammonia?", intro="Explain why mammals convert ammonia to urea.", steps=[
            S("Toxicity", text="Ammonia is toxic and raises pH, and it is very soluble and diffuses easily across membranes."),
            S("Water", text="To excrete it as ammonia, a great deal of water would be needed to dilute it. Mammals on land need to save water."),
            S("Urea", text="Urea is much less toxic and can be carried in blood and concentrated in urine."),
        ]),
        EX("Worked example 3: tracing the blood", intro="Describe the route of blood carrying glucose absorbed from the small intestine to the liver and back to the heart.", steps=[
            S("From gut", text="Capillaries of the villi, then the hepatic portal vein."),
            S("In the liver", text="Branches of the portal vein open into sinusoids, where glucose may be stored as glycogen."),
            S("Back to the heart", text="Blood leaves through the central vein, then the hepatic vein, to the vena cava and the heart."),
        ]),
        MISTAKE("Mixing up deamination and transamination", "Deamination removes NH₂ and produces ammonia and a keto acid. Transamination moves an amino group from one amino acid to a keto acid to make a different amino acid."),
        MISTAKE("Writing that urea is made in the kidney", "Urea is made in the liver. The kidney only removes it from the blood into the urine."),
        QUIZ("Which cells of the liver remove bacteria and old red blood cells?",
             ["Hepatocytes", "Kupffer cells", "Platelets", "Bile duct cells"], 1,
             "Kupffer cells are macrophages in the sinusoids.",
             hint="They are phagocytes lining the sinusoid.",
             feedback=["Hepatocytes carry out the chemical work of the liver.", "", "Platelets are blood fragments involved in clotting.", "Bile duct cells carry bile."]),
        QUIZ("Which statement about the ornithine cycle is correct?",
             ["It converts urea into ammonia", "It requires ATP and produces urea", "It occurs in the kidney", "It happens in the stomach"], 1,
             "Ammonia is converted to urea using ATP in the liver.",
             hint="It protects the body from a toxic gas.",
             feedback=["It makes urea; it does not break it down.", "", "It occurs in liver cells.", "The stomach does not make urea."]),
        PQ("Describe the structure of a liver lobule.",
           "Hepatocytes are arranged in rows radiating from a central vein. Between the rows are sinusoids, which receive blood from branches of the hepatic artery and hepatic portal vein and drain into the central vein. Kupffer cells lie in the sinusoids. Bile canaliculi between hepatocytes carry bile to bile ducts."),
        PQ("Explain what happens to excess amino acids in the body.",
           "They are deaminated in the liver: the amine group is removed to form ammonia and a keto acid. The keto acid is used in respiration or converted into glucose or fat. Ammonia is converted to urea in the ornithine cycle and excreted by the kidneys."),
        PQ("Calculate the mass of nitrogen in 150 g of protein that is 16 percent nitrogen, and the mass of urea (28 g of N in 60 g of urea) that contains this nitrogen.",
           "N = 150 × 0.16 = 24 g. Urea = 24 × 60 / 28 = 51.4 g."),
        PQ("Give three functions of the liver other than excretion, with an example of each.",
           "Regulation of blood glucose: stores glycogen. Production of bile: bile salts emulsify fats. Detoxification: breaks down alcohol or drugs. (Also: stores vitamins A and D and iron; makes plasma proteins; produces heat.)"),
        TIP("The liver and urea formation are asked in both Paper 1 (functions, which organ) and Paper 2 (deamination and the cycle). Learn the five steps in order and name ornithine as the compound regenerated."),
        SUM("The liver receives blood from the hepatic artery and hepatic portal vein; blood flows through sinusoids between hepatocytes to the central vein.",
            "Hepatocytes store glycogen, make plasma proteins and bile, detoxify drugs and alcohol, and make urea.",
            "Deamination makes ammonia; the ornithine cycle converts ammonia and CO₂ to urea using ATP.",
            "Urea is carried in blood to the kidney and excreted in urine."),
    ],
))

# ------------------------------------------------------------------ 10. Nephron: ultrafiltration and reabsorption
LESSONS.append(lesson(
    module=M2,
    topic="The nephron and the loop of Henle",
    title="The nephron: ultrafiltration and selective reabsorption",
    slug="biu1-nephron-ultrafiltration-reabsorption",
    minutes=24,
    summary="The structure of the nephron, how pressure filters blood in the renal corpuscle, how the proximal tubule reabsorbs most useful substances, and how to calculate filtration pressure, reabsorption and clearance.",
    objectives=[
        "Label the parts of a nephron and its blood supply",
        "Explain ultrafiltration, including the filtration barrier and the pressures involved",
        "Explain selective reabsorption in the proximal convoluted tubule and relate its structure to function",
        "Calculate net filtration pressure, percentage reabsorbed and glomerular filtration rate from data",
    ],
    key_concepts=["Nephron", "Renal corpuscle", "Glomerulus", "Podocyte", "Basement membrane", "Ultrafiltration", "Net filtration pressure", "Selective reabsorption", "Renal threshold", "GFR"],
    blocks=[
        H("Introduction"),
        T("Each human kidney contains about one million tiny filtering units called **nephrons**. Together they clean about 180 litres of blood plasma a day, "
          "yet only about 1.5 litres leave the body as urine. In this lesson we follow the filtrate from the blood into the tubule and see how most of it returns to the blood."),
        IMG("al-biu1-nephron.svg", alt="A nephron: Bowman's capsule with glomerulus in the cortex, proximal tubule, descending limb, loop of Henle in the medulla, ascending limb, distal tubule and collecting duct.",
            caption="Figure 1. A nephron and its collecting duct (simplified, not to scale)."),
        H("Structure of the nephron"),
        T("The nephron starts with the **renal corpuscle**: the **glomerulus** (a knot of capillaries) inside the cup-shaped **Bowman's capsule**. From the capsule the tubule runs as the "
          "**proximal convoluted tubule (PCT)**, the **loop of Henle** (descending and ascending limbs), the **distal convoluted tubule (DCT)** and finally joins a **collecting duct**. "
          "The renal corpuscle, PCT and DCT are in the cortex; the loop and collecting duct run into the medulla."),
        T("Blood enters the glomerulus through the **afferent arteriole** and leaves through the **efferent arteriole**, which is narrower. The wider vessel in and narrower out "
          "keeps the pressure in the glomerulus high."),
        H("Ultrafiltration"),
        D("**Ultrafiltration** is the filtration of blood plasma under high pressure through the filtration barrier of the glomerulus into the Bowman's capsule. Small molecules pass; large molecules and blood cells stay in the blood.",
          title="Definition: ultrafiltration"),
        KEY("The filtration barrier has three layers", "Substances must pass through all three.", cards=[
            ["Capillary endothelium", "Has many small pores (fenestrations); cells and large proteins cannot pass."],
            ["Basement membrane", "A network of collagen and glycoproteins; acts as the main filter and holds back proteins larger than about 68 000 Mr (check your textbook)."],
            ["Podocytes", "Cells of the capsule wall with finger-like extensions; the gaps between them (filtration slits) allow the filtrate to pass."],
        ]),
        T("The **glomerular filtrate** contains water, glucose, amino acids, urea, salts and vitamins. It contains no blood cells and almost no plasma protein. "
          "The filtrate is pushed out because the pressure in the glomerular capillaries is greater than the forces opposing filtration."),
        F(r"\text{net filtration pressure} = P_{\text{glomerulus}} - (\pi_{\text{plasma}} + P_{\text{capsule}})", title="Net filtration pressure"),
        T("Here P is hydrostatic pressure and π is the osmotic (oncotic) pressure of the plasma proteins, which pulls water back. Teaching values: glomerular pressure 55 mmHg, "
          "oncotic pressure 30 mmHg, capsule pressure 15 mmHg. Textbooks use slightly different values."),
        H("Selective reabsorption in the proximal tubule"),
        T("About 65 percent of the filtrate is reabsorbed in the PCT, including **all the glucose and amino acids**. The cells of the PCT wall are adapted for this:"),
        CODE("""Feature of PCT cell              Function
Microvilli (brush border)        Large surface area for absorption
Many mitochondria                ATP for active transport
Infoldings at base of cell       Large area to pass substances into tissue fluid
Tight junctions and close        Short diffusion distance; blood capillaries are
capillaries                      right beside the tubule
Transport proteins               Co-transport and facilitated diffusion""", "text", title="Proximal convoluted tubule cell"),
        T("Sodium ions are pumped out of the cell into the tissue fluid by the sodium-potassium pump. This lowers the Na⁺ concentration in the cell, so Na⁺ from the filtrate enter by "
          "**co-transport** with glucose or amino acids. Glucose then leaves into the blood by facilitated diffusion. Water follows by osmosis. "
          "Small proteins are taken in by endocytosis. Urea is reabsorbed partly by diffusion."),
        D("The **renal threshold** is the plasma concentration of a substance above which the transport proteins are saturated, so the substance appears in the urine. "
          "For glucose it is about 10 mmol per litre (textbooks differ), so glucose in urine suggests uncontrolled diabetes mellitus.",
          title="Definition: renal threshold"),
        CODE("""Substance         Blood plasma    Glomerular filtrate    Urine
Protein           present         almost absent          absent
Glucose           present         present                absent (healthy)
Urea              present         present                much higher
Water             present         present                less than filtrate
Red blood cells   present         absent                 absent""", "text", title="Comparing plasma, filtrate and urine"),
        H("Worked examples"),
        EX("Worked example 1: net filtration pressure", intro="Glomerular hydrostatic pressure is 55 mmHg, plasma oncotic pressure 30 mmHg and capsule pressure 15 mmHg. Calculate the net filtration pressure.", steps=[
            S("Opposing forces", math=r"30 + 15 = 45 \text{ mmHg}"),
            S("Net pressure", math=r"55 - 45 = 10 \text{ mmHg}"),
            S("Meaning", text="A net pressure of 10 mmHg forces fluid out of the glomerulus into the capsule."),
        ]),
        EX("Worked example 2: percentage reabsorbed", intro="In a day 180 litres of filtrate form and 1.5 litres of urine are produced. What percentage of the filtrate is reabsorbed?", steps=[
            S("Volume reabsorbed", math=r"180 - 1.5 = 178.5 \text{ litres}"),
            S("Percentage", math=r"\frac{178.5}{180} \times 100 = 99.2\%"),
        ], check=r"\frac{1.5}{180} \times 100 = 0.83\% \text{ is excreted}"),
        EX("Worked example 3: glomerular filtration rate", intro="Inulin is filtered freely and is neither reabsorbed nor secreted. A patient has urine inulin 25 mg/mL, urine flow 1.25 mL/min and plasma inulin 0.25 mg/mL. Find the GFR.", steps=[
            S("Formula", math=r"\text{GFR} = \frac{U \times V}{P}"),
            S("Substitute", math=r"\frac{25 \times 1.25}{0.25} = 125 \text{ mL/min}"),
            S("Per day", math=r"125 \times 60 \times 24 = 180\,000 \text{ mL} = 180 \text{ litres}"),
        ]),
        MISTAKE("Saying the glomerulus filters by size only", "Pressure is the driving force. Size (and charge) of molecules decides which can pass the barrier. Without high pressure there would be no filtration."),
        MISTAKE("Writing 'glucose is absent from filtrate'", "Glucose is present in the filtrate (it is a small molecule). It is absent from urine because it is reabsorbed in the PCT."),
        QUIZ("Which feature of the afferent and efferent arterioles helps to keep the pressure in the glomerulus high?",
             ["The afferent arteriole is narrower than the efferent", "The efferent arteriole is narrower than the afferent", "Both arterioles are very wide", "The glomerulus has no capillaries"], 1,
             "Blood enters through a wide vessel and leaves through a narrow one, so pressure builds up.",
             hint="Imagine pushing water through a narrow tap.",
             feedback=["It is the reverse.", "", "Wide outflow would lower the pressure.", "The glomerulus is a knot of capillaries."]),
        QUIZ("Why is glucose found in the filtrate but not in the urine of a healthy person?",
             ["It is too large to filter", "It is filtered, then all reabsorbed in the PCT", "It is broken down in the capsule", "It is secreted into the loop of Henle"], 1,
             "Glucose is small and filters freely, then is all reabsorbed by co-transport with Na⁺ and facilitated diffusion.",
             hint="Which part of the nephron reabsorbs about 65% of filtrate?",
             feedback=["Glucose is a small molecule and filters easily.", "", "The capsule does not break down glucose.", "Glucose is reabsorbed, not secreted."]),
        PQ("Describe how the structure of the glomerulus and Bowman's capsule is adapted for ultrafiltration.",
           "The efferent arteriole is narrower than the afferent, giving high pressure. The capillary endothelium has pores, the basement membrane acts as a filter, and podocytes leave gaps (filtration slits). Together they let small molecules pass but hold back cells and large proteins."),
        PQ("Explain how the cells of the proximal convoluted tubule are adapted to reabsorb glucose.",
           "Microvilli give a large surface area; many mitochondria provide ATP for the sodium-potassium pump, which maintains a low Na⁺ concentration in the cell. Na⁺ then enter with glucose by co-transport, and glucose leaves by facilitated diffusion at the base into the capillaries beside the tubule."),
        PQ("Calculate the net filtration pressure when glomerular pressure is 60 mmHg, plasma oncotic pressure 28 mmHg and capsule pressure 14 mmHg.",
           "Opposing pressure = 28 + 14 = 42 mmHg. Net pressure = 60 − 42 = 18 mmHg."),
        PQ("A diabetic patient's urine contains glucose. Explain why.",
           "Blood glucose is very high, so the filtrate contains more glucose than the transport proteins in the PCT can reabsorb (the renal threshold is exceeded). The excess remains in the filtrate and is excreted in urine."),
        TIP("Nephron structure and urine formation appear in every Paper 2 on excretion; a labelled nephron diagram is common in Paper 1. The Board's practical paper may include dissection of the urinogenital system of a bird or mammal."),
        SUM("Blood is filtered in the renal corpuscle under high pressure; the barrier is the endothelium, basement membrane and podocytes.",
            "Net filtration pressure = glomerular pressure − (oncotic pressure + capsule pressure).",
            "The PCT reabsorbs about 65% of filtrate, all of the glucose and amino acids, by active transport and co-transport.",
            "Healthy urine has no protein or glucose; GFR is about 125 mL per minute (180 litres per day)."),
    ],
))

# ------------------------------------------------------------------ 11. Loop of Henle
LESSONS.append(lesson(
    module=M2,
    topic="The nephron and the loop of Henle",
    title="The loop of Henle and the counter-current multiplier",
    slug="biu1-loop-of-henle-countercurrent",
    minutes=24,
    summary="How the loop of Henle builds a salt gradient in the medulla by the counter-current multiplier, how the vasa recta keep it, why long loops help desert animals, and how to calculate the water saved.",
    objectives=[
        "Describe the structure and permeability of the descending and ascending limbs",
        "Explain how the counter-current multiplier forms a gradient of solute concentration in the medulla",
        "Explain the role of the vasa recta and the collecting duct in concentrating urine",
        "Compare the loops of animals living in different habitats and calculate water needed to excrete solutes",
    ],
    key_concepts=["Loop of Henle", "Counter-current multiplier", "Descending limb", "Ascending limb", "Medullary gradient", "Vasa recta", "Hypertonic urine", "Water potential"],
    blocks=[
        H("Introduction"),
        T("A traveller in the Sahel on a hot day passes a zebu cow; a camel can go many days without drinking. Their urine is very concentrated: little water is lost with each unit of waste. "
          "Humans can also make urine up to four times more concentrated than blood. The structure that makes this possible is the **loop of Henle**."),
        D("The **loop of Henle** is the hairpin part of the nephron, running from the cortex into the medulla and back. Its counter-current arrangement builds up a high solute concentration in the tissue fluid of the medulla, "
          "so that water can be reabsorbed from the filtrate in the collecting duct.",
          title="Definition: loop of Henle"),
        IMG("al-biu1-loop-henle.svg", alt="Loop of Henle with descending limb losing water to the interstitial fluid, ascending limb pumping out sodium and chloride ions, collecting duct, and interstitial concentrations of 300, 600, 900 and 1200 mOsm per litre.",
            caption="Figure 1. The loop of Henle (teaching values in mOsm per litre of interstitial fluid)."),
        H("Two limbs with different permeability"),
        KEY("Different walls, different jobs", "This difference is the key to the mechanism.", cards=[
            ["Descending limb", "Wall is permeable to water and almost impermeable to Na⁺ and Cl⁻. Water leaves by osmosis, so the filtrate becomes more concentrated as it goes down."],
            ["Ascending limb (thick part)", "Wall is impermeable to water. Na⁺ and Cl⁻ are pumped out into the medulla (a Na⁺/K⁺/2Cl⁻ co-transporter powered by the sodium pump; many books say Cl⁻ follows Na⁺, check yours)."],
        ]),
        H("How the multiplier works"),
        T("**Step 1.** In the ascending limb, salt is pumped out. The medulla tissue fluid becomes more concentrated (lower water potential). The filtrate inside the limb loses salt and becomes dilute."),
        T("**Step 2.** The descending limb passes through this salty fluid. Water leaves by osmosis, so the filtrate in the descending limb becomes more and more concentrated, reaching the maximum at the bottom of the loop."),
        T("**Step 3.** The concentrated filtrate goes round the bend and flows up the ascending limb. Because the filtrate here is strongest at the bottom, more salt is available to be pumped out at the bottom than at the top."),
        T("The two flows go in **opposite directions** (counter-current). Each step of the pump makes only a small difference of about 200 mOsm between the two limbs at the same level, "
          "but because the flow is opposite the differences add up along the length. The concentration therefore **multiplies** from about 300 at the top to about 1200 mOsm per litre at the bottom of the medulla."),
        T("At the top of the ascending limb the filtrate is dilute (hypotonic) to the blood, about 100 mOsm. It then passes to the distal tubule and collecting duct. In the collecting duct, when ADH is present, water leaves by osmosis into the strongly salty medulla, so the urine becomes concentrated."),
        F(r"\text{multiplier effect: single effect } (\approx 200 \text{ mOsm}) \times \text{ counter-current flow} \Rightarrow \text{gradient } (300 \rightarrow 1200 \text{ mOsm})", title="Idea of the counter-current multiplier"),
        T("The **vasa recta** are long hairpin capillaries running beside the loop. They flow in a counter-current direction so that they take away water without washing out the salt of the medulla (a **counter-current exchanger**). Urea that diffuses out of the lower collecting duct also adds to the high concentration in the deep medulla."),
        H("Why loops differ in length"),
        T("About 85 percent of nephrons in humans are cortical (short loops); about 15 percent are juxtamedullary (long loops reaching deep into the medulla). Textbooks give slightly different figures. "
          "A longer loop builds a steeper and higher gradient, so the urine can be more concentrated and water is saved. Desert animals such as the kangaroo rat and the camel have very long loops. Animals that live in water, such as the beaver, have short loops and produce dilute urine."),
        H("Worked examples"),
        EX("Worked example 1: obligatory water loss", intro="A person must excrete 600 mmol of solutes a day. Calculate the smallest volume of urine if the maximum urine concentration is 1200 mmol per litre, and compare it with the volume needed if the urine could only reach the blood concentration of 300 mmol per litre.", steps=[
            S("Concentrated urine", math=r"\frac{600}{1200} = 0.5 \text{ litres}"),
            S("Blood concentration", math=r"\frac{600}{300} = 2.0 \text{ litres}"),
            S("Water saved", math=r"2.0 - 0.5 = 1.5 \text{ litres per day}"),
        ]),
        EX("Worked example 2: predicting an effect", intro="A diuretic drug blocks the pumping of ions out of the thick ascending limb (as loop diuretics do). Predict the effect on (a) the medulla gradient and (b) urine volume.", steps=[
            S("Gradient", text="Less Na⁺ and Cl⁻ are pumped out, so the gradient in the medulla is smaller."),
            S("Descending limb and collecting duct", text="Less water leaves by osmosis in the descending limb and in the collecting duct."),
            S("Urine", text="More water remains in the tubule, so a larger volume of dilute urine is produced."),
        ]),
        EX("Worked example 3: reading the figure", intro="In Figure 1 the interstitial concentrations are 300, 600, 900 and 1200 mOsm per litre. Explain why the filtrate at the bottom of the loop has a concentration of about 1200.", steps=[
            S("Osmosis", text="The descending limb is permeable to water, so water leaves until the filtrate is in balance with the fluid around it."),
            S("Result", text="At the bottom the surroundings are at 1200, so the filtrate rises to about 1200."),
        ]),
        MISTAKE("Saying that water is pumped out of the ascending limb", "Water leaves the descending limb (and collecting duct) by osmosis. The ascending limb pumps out ions, and its wall is impermeable to water."),
        MISTAKE("Saying that the loop itself makes concentrated urine", "The loop makes the concentration gradient. Concentrated urine forms in the collecting duct, which lets water leave by osmosis when ADH is present."),
        QUIZ("In which part of the nephron is the wall almost impermeable to water but actively pumps out Na⁺ and Cl⁻?",
             ["Descending limb", "Thick ascending limb", "Proximal tubule", "Bowman's capsule"], 1,
             "The thick ascending limb transports ions out, but water cannot follow.",
             hint="This is where the single effect is produced.",
             feedback=["The descending limb is permeable to water.", "", "The PCT is permeable to water.", "Bowman's capsule is part of the filtration barrier."]),
        QUIZ("Why does an animal with a longer loop of Henle produce more concentrated urine?",
             ["It has more glomeruli", "A longer loop builds a steeper salt gradient in the medulla", "Its filtrate has more protein", "Its bladder is larger"], 1,
             "More length allows more multiplication and a higher concentration at the bottom.",
             hint="Gradient is added along the length.",
             feedback=["The number of glomeruli does not set the gradient.", "", "Protein does not enter the filtrate.", "Bladder size is not related."]),
        PQ("Explain how the loop of Henle produces a high concentration of solutes in the medulla.",
           "In the thick ascending limb Na⁺ and Cl⁻ are pumped out into the medulla by active transport, and the wall is impermeable to water. This lowers the water potential of the medulla. Water leaves the descending limb by osmosis, making the fluid there more concentrated. Because the two limbs carry fluid in opposite directions, the small difference at each level is multiplied along the loop, giving a gradient from the cortex to the deep medulla."),
        PQ("Describe the role of the vasa recta.",
           "They are capillaries with a hairpin shape running beside the loop. Blood flows in the opposite direction in the two parts, so the vessels supply oxygen and remove reabsorbed water and ions without washing away the solutes of the medulla gradient."),
        PQ("Calculate the volume of water needed to excrete 700 mmol of solutes per day at a urine concentration of 350 mmol per litre and at 1400 mmol per litre.",
           "At 350: 700 / 350 = 2.0 litres. At 1400: 700 / 1400 = 0.5 litres. The more concentrated urine saves 1.5 litres of water."),
        PQ("Explain why the kangaroo rat, a desert animal, has longer loops of Henle than the beaver.",
           "A longer loop makes a steeper medulla gradient, so the urine is more concentrated and less water is lost in a dry habitat. The beaver has plenty of water, so it does not need to save water and has short loops and dilute urine."),
        TIP("The loop of Henle is a favourite essay topic in Paper 2. Always state the permeability of each limb, the active pumping of ions, and the opposite direction of flow. Draw a labelled diagram with concentrations."),
        SUM("The descending limb is permeable to water; the thick ascending limb pumps out Na⁺ and Cl⁻ and is impermeable to water.",
            "Counter-current flow multiplies a single effect of about 200 mOsm into a gradient of 300 to 1200 mOsm per litre.",
            "The vasa recta act as a counter-current exchanger that keeps the gradient.",
            "Longer loops make more concentrated urine, saving water; the collecting duct uses the gradient with ADH."),
    ],
))

# ------------------------------------------------------------------ 12. ADH and aldosterone
LESSONS.append(lesson(
    module=M2,
    topic="ADH and aldosterone",
    title="ADH, aldosterone and the control of water and salt",
    slug="biu1-adh-aldosterone",
    minutes=22,
    summary="How osmoreceptors, ADH, the renin-angiotensin-aldosterone system and the kidney keep the water potential, blood volume and sodium level of the blood within narrow limits.",
    objectives=[
        "Explain how ADH is released and how it changes the permeability of the collecting duct",
        "Describe the renin-angiotensin-aldosterone system and the action of aldosterone",
        "Explain the control of water balance as a negative feedback loop",
        "Interpret data on urine volume and concentration and on a daily water balance",
    ],
    key_concepts=["Osmoregulation", "Osmoreceptor", "ADH", "Aquaporin", "cAMP", "Aldosterone", "Renin", "Angiotensin II", "Diabetes insipidus"],
    blocks=[
        H("Introduction"),
        T("After a football match in Douala at midday, a player who has sweated a lot passes only a little dark yellow urine. After drinking a litre of water, "
          "the next visit to the toilet gives a lot of pale urine. The kidney is adjusting the amount of water it returns to the blood. "
          "The hormone responsible is **antidiuretic hormone (ADH)**. A second hormone, **aldosterone**, adjusts the salt (Na⁺) balance."),
        D("**Osmoregulation** is the control of the water potential (water and solute concentration) of the blood and tissue fluid, mainly by the kidneys.",
          title="Definition: osmoregulation"),
        H("ADH and water balance"),
        T("**Osmoreceptor cells** in the hypothalamus detect the water potential of the blood. When it falls (the blood is too concentrated, as in dehydration), the osmoreceptor cells lose water and shrink. "
          "They send impulses to **neurosecretory cells** whose cell bodies lie in the hypothalamus and whose axons run down into the **posterior pituitary**. ADH made in the hypothalamic cells is stored in the nerve endings in the posterior pituitary and released into the blood when impulses arrive."),
        T("ADH travels in blood to the **cells of the distal convoluted tubule and collecting duct**. It binds to receptors on the cell surface membrane. This activates a second messenger, **cyclic AMP (cAMP)**, which causes vesicles carrying **aquaporin-2** water channels to move to and fuse with the membrane. "
          "The wall becomes much more permeable to water. Water leaves the tubule by osmosis into the salty medulla (see the loop of Henle lesson) and enters the vasa recta."),
        KEY("Two situations", "Follow the change in the same order each time.", cards=[
            ["Blood too concentrated (dehydrated)", "More ADH is released. The collecting duct becomes more permeable. More water is reabsorbed. Small volume of concentrated urine. Water potential of blood rises."],
            ["Blood too dilute (after drinking)", "Less ADH is released. Fewer aquaporins in the membrane. Less water is reabsorbed. Large volume of dilute urine. Water potential of blood falls."],
        ]),
        T("This is **negative feedback**: the change (low water potential) triggers a response (more ADH, more water saved) that reverses the change. "
          "Thirst, which is controlled by the hypothalamus, adds to the response by encouraging drinking."),
        T("In **diabetes insipidus**, too little ADH is made or the kidney does not respond. The person produces large volumes of very dilute urine and is always thirsty. "
          "(This is a different disease from diabetes mellitus, which involves insulin.)"),
        H("Aldosterone and sodium balance"),
        T("When blood volume or blood pressure falls, or Na⁺ falls, cells of the **juxtaglomerular apparatus** in the kidney release the enzyme **renin**. Renin changes the plasma protein angiotensinogen "
          "(made in the liver) to angiotensin I. The enzyme ACE in the lungs converts angiotensin I to **angiotensin II**."),
        T("Angiotensin II narrows arterioles (raising blood pressure), stimulates the release of ADH and thirst, and stimulates the **adrenal cortex** to release **aldosterone**."),
        T("Aldosterone is a **steroid hormone**. It passes through the cell surface membrane of cells in the distal tubule and collecting duct, binds to a receptor inside the cell and "
          "switches on genes for more **Na⁺ channels** and **Na⁺/K⁺ pumps**. More Na⁺ is reabsorbed, K⁺ is secreted, and water follows by osmosis, so blood volume and pressure rise."),
        CODE("""Hormone       Made in                    Target                          Effect
ADH           Hypothalamus (stored in    Collecting duct and DCT         More aquaporins, more water
              posterior pituitary)                                       reabsorbed, urine concentrated
Aldosterone   Adrenal cortex             DCT and collecting duct         More Na+ channels and pumps,
                                                                         more Na+ and water reabsorbed""", "text", title="Comparison"),
        T("A hormone that raises blood volume is balanced by **atrial natriuretic peptide (ANP)**, released by the atria when stretched, which reduces Na⁺ reabsorption. You need only know that it opposes aldosterone."),
        H("Worked examples"),
        EX("Worked example 1: dehydration", intro="A person walks for hours without drinking. Describe how the body corrects the rise in blood concentration.", steps=[
            S("Detection", text="Osmoreceptors in the hypothalamus detect low water potential of the blood."),
            S("Hormone", text="The posterior pituitary releases more ADH."),
            S("Kidney", text="ADH causes more aquaporins in the collecting duct. More water is reabsorbed, giving a small volume of concentrated urine."),
            S("Feedback", text="Blood water potential rises towards normal, so ADH release falls. Thirst also makes the person drink."),
        ]),
        EX("Worked example 2: water balance", intro="A person takes in 2.5 litres of water per day (drink and food). Water is lost: urine 1.5 litres, sweat 0.5 litres, faeces 0.1 litre. How much is lost in breath if the person is in balance?", steps=[
            S("Total lost so far", math=r"1.5 + 0.5 + 0.1 = 2.1 \text{ litres}"),
            S("Balance means intake = output", math=r"2.5 - 2.1 = 0.4 \text{ litres}"),
            S("Answer", text="0.4 litre is lost in the breath."),
        ]),
        EX("Worked example 3: aldosterone and blood pressure", intro="Explain why a person who loses blood after an accident secretes more aldosterone.", steps=[
            S("Trigger", text="Lower blood volume and pressure make the juxtaglomerular cells release renin."),
            S("Chain", text="Angiotensinogen to angiotensin I to angiotensin II, which stimulates the adrenal cortex."),
            S("Effect", text="Aldosterone increases Na⁺ reabsorption, water follows, so blood volume increases."),
        ]),
        MISTAKE("Saying that ADH makes the kidney produce more urine", "'Antidiuretic' means 'against making urine'. ADH reduces the volume of urine by increasing water reabsorption."),
        MISTAKE("Saying that the hypothalamus makes aldosterone", "Aldosterone is made by the adrenal cortex. ADH is made in the hypothalamus but stored and released by the posterior pituitary."),
        QUIZ("What is the effect of ADH on the collecting duct?",
             ["It increases the number of aquaporin channels in the membrane", "It pumps sodium ions out of the duct", "It decreases water permeability", "It filters protein"], 0,
             "ADH, through cAMP, causes vesicles with aquaporin-2 to fuse with the membrane.",
             hint="Think about water permeability.",
             feedback=["", "That is aldosterone's effect (on Na⁺ uptake in the DCT and collecting duct).", "ADH increases it.", "The collecting duct does not filter."]),
        QUIZ("Which organ releases aldosterone?",
             ["Posterior pituitary", "Adrenal cortex", "Liver", "Hypothalamus"], 1,
             "The adrenal cortex releases aldosterone in response to angiotensin II.",
             hint="This gland lies above the kidney.",
             feedback=["It releases ADH and oxytocin.", "", "The liver makes angiotensinogen.", "It makes ADH but does not secrete aldosterone."]),
        PQ("Explain how ADH reduces the volume of urine.",
           "ADH binds to receptors on collecting duct cells, raising cAMP inside them. Vesicles with aquaporin-2 fuse with the surface membrane, so the wall becomes permeable to water. Water leaves the duct by osmosis into the salty medulla, so less water is lost and a smaller volume of concentrated urine is produced."),
        PQ("Describe the control of blood water potential as a negative feedback loop.",
           "Receptor: osmoreceptors in the hypothalamus. Coordinator: hypothalamus and posterior pituitary. Effector: collecting duct cells. If the water potential falls, more ADH is released, more water is reabsorbed and the water potential rises. If it rises, less ADH is released, less water is reabsorbed and the water potential falls."),
        PQ("Outline how aldosterone raises blood volume.",
           "Low blood volume or Na⁺ causes release of renin and then angiotensin II, which stimulates the adrenal cortex to release aldosterone. Aldosterone enters cells of the DCT and collecting duct and switches on genes for more Na⁺ channels and pumps. More Na⁺ is reabsorbed and water follows by osmosis, raising blood volume."),
        PQ("A patient passes 12 litres of very dilute urine a day and is always thirsty. Suggest a cause and explain the symptoms.",
           "Diabetes insipidus: too little ADH is made or the kidney cannot respond. The collecting duct stays impermeable to water, so little water is reabsorbed, giving a large volume of dilute urine. The loss of water raises the blood concentration, causing thirst."),
        TIP("In Paper 2 osmoregulation is a common essay. Use the sequence: stimulus, osmoreceptors, hypothalamus, posterior pituitary, ADH, target, response, feedback."),
        SUM("Osmoreceptors in the hypothalamus detect blood water potential; ADH is released from the posterior pituitary.",
            "ADH acts through cAMP to insert aquaporins in the collecting duct, so more water is reabsorbed and urine is concentrated.",
            "Low blood volume leads to renin, angiotensin II and aldosterone from the adrenal cortex, which raises Na⁺ reabsorption.",
            "Both hormones work by negative feedback to keep water potential, volume and Na⁺ steady."),
    ],
))

# ------------------------------------------------------------------ 13. Blood glucose regulation
LESSONS.append(lesson(
    module=M2,
    topic="Blood glucose regulation",
    title="Control of blood glucose: insulin, glucagon and second messengers",
    slug="biu1-blood-glucose-regulation",
    minutes=24,
    summary="How the islets of Langerhans release insulin and glucagon, how insulin lowers and glucagon raises blood glucose, the cAMP second-messenger cascade, and the two kinds of diabetes mellitus.",
    objectives=[
        "Describe the roles of alpha and beta cells and of insulin and glucagon in negative feedback control of blood glucose",
        "Explain how a beta cell releases insulin when blood glucose rises",
        "Describe the cyclic AMP second-messenger cascade for glucagon or adrenaline and explain amplification",
        "Compare type 1 and type 2 diabetes mellitus and interpret a glucose tolerance curve",
    ],
    key_concepts=["Blood glucose", "Islets of Langerhans", "Insulin", "Glucagon", "Glycogenesis", "Glycogenolysis", "Gluconeogenesis", "Second messenger", "cAMP", "Diabetes mellitus"],
    blocks=[
        H("Introduction"),
        T("Your brain uses glucose as its main fuel and cannot store it. If blood glucose falls too low you feel weak, shaky and confused; if it stays too high, "
          "blood vessels, kidneys and nerves are damaged over many years. The normal fasting value is about 4 to 6 mmol per litre of blood (about 70 to 100 mg per 100 mL). "
          "Blood glucose is kept in this range by two hormones from the pancreas."),
        T("The pancreas has a second role in the body, a **dual function**: most of the pancreas makes digestive enzymes. Scattered clusters of cells, the **islets of Langerhans**, make hormones. "
          "**Alpha cells** secrete **glucagon**. **Beta cells** secrete **insulin**."),
        H("Control by negative feedback"),
        KEY("Two hormones with opposite effects", "Antagonistic hormones give good control.", cards=[
            ["Insulin (beta cells), glucose too high", "Raises uptake of glucose by cells (more GLUT4 in the membrane of muscle and fat cells), speeds glycogenesis in liver and muscle (glycogen synthase active), increases respiration of glucose and conversion of glucose to fat."],
            ["Glucagon (alpha cells), glucose too low", "Acts on liver cells: more glycogenolysis (glycogen to glucose), more gluconeogenesis (glucose from amino acids and glycerol); less glucose use. Glucose is released into blood."],
        ]),
        T("Adrenaline, released in stress or exercise, acts like glucagon on liver and muscle glycogen and so raises blood glucose. Cortisol and growth hormone also raise blood glucose over a longer time."),
        D("**Glycogenesis** is the formation of glycogen from glucose. **Glycogenolysis** is the breakdown of glycogen to glucose. **Gluconeogenesis** is the formation of glucose from non-carbohydrates such as amino acids, glycerol and lactate.",
          title="Three key words"),
        H("How a beta cell senses glucose"),
        T("Glucose enters the beta cell through a glucose transporter (GLUT2) and is respired, so the cell's ATP concentration rises. ATP closes **ATP-sensitive potassium channels**. K⁺ cannot leave, so the membrane is **depolarised**. "
          "This opens **voltage-gated calcium channels**; Ca²⁺ enter and trigger **exocytosis** of vesicles that contain insulin. The more glucose, the more insulin is released."),
        H("The second-messenger cascade"),
        T("Glucagon and adrenaline are **first messengers**: they cannot enter the cell. They bind to receptors on the surface of liver cells and start a chain of events inside the cell."),
        IMG("al-biu1-camp-cascade.svg", alt="Cascade: hormone binds receptor, G protein activated, adenylyl cyclase active, ATP converted to cAMP, protein kinase A active, phosphorylase kinase, glycogen phosphorylase, glycogen to glucose.",
            caption="Figure 1. The cAMP cascade in a liver cell."),
        T("(1) The hormone binds its receptor. (2) A **G protein** is activated. (3) The G protein activates **adenylyl cyclase**. (4) Adenylyl cyclase converts ATP to **cyclic AMP (cAMP)**, the **second messenger**. "
          "(5) cAMP activates **protein kinase A**. (6) This activates phosphorylase kinase, which (7) activates **glycogen phosphorylase**. (8) That enzyme breaks glycogen into glucose phosphate, from which glucose is released into the blood."),
        T("Each active enzyme in the chain makes many molecules of the next, so the signal is **amplified**. One hormone molecule can lead to the release of a very large number of glucose molecules. The cascade stops when cAMP is broken down by phosphodiesterase."),
        H("Diabetes mellitus"),
        CODE("""Feature              Type 1                          Type 2
Cause                Immune system destroys beta     Cells respond poorly to insulin
                     cells; little or no insulin     (insulin resistance); beta cells tire
Usual onset          Childhood or young adult        Adults, often linked to being overweight
Treatment            Insulin injections, diet        Diet, exercise, tablets; sometimes insulin
Urine                Glucose present when the renal threshold is exceeded""", "text", title="Two kinds of diabetes"),
        T("Type 2 diabetes is becoming more common in towns and cities, linked to diets rich in sugar and fat and to less physical activity. A **glucose tolerance test** measures how quickly blood glucose returns to normal after a drink of glucose."),
        IMG("al-biu1-glucose-tolerance.svg", alt="Graph of blood glucose against time for a healthy person, who rises to about 7.8 and returns to about 4.6 by 2 hours, and for a person with diabetes, who starts higher, peaks near 14 and stays high.",
            caption="Figure 2. A glucose tolerance test (invented teaching data)."),
        H("Worked examples"),
        EX("Worked example 1: reading the glucose tolerance test", intro="Use Figure 2. Compare the two people.", steps=[
            S("Fasting value", text="Healthy: 4.6 mmol/L. Diabetes: 8.0 mmol/L, already high."),
            S("Peak", text="Healthy: 7.8 mmol/L at 30 minutes. Diabetes: 13.8 mmol/L at 90 minutes."),
            S("Return", text="Healthy returns to about 4.6 by 120 minutes. Diabetes is still near 12.8 at 120 minutes."),
            S("Conclusion", text="The person with diabetes cannot remove glucose from the blood quickly, because little insulin is released or cells do not respond to it."),
        ]),
        EX("Worked example 2: amplification", intro="In a teaching example, one receptor activates 10 G proteins, each G protein ends up making 100 molecules of cAMP and each cAMP leads to the activation of 10 molecules of glycogen phosphorylase. How many phosphorylase molecules are activated?", steps=[
            S("Multiply the stages", math=r"10 \times 100 \times 10 = 10\,000"),
            S("Meaning", text="Different stages multiply the effect of a single hormone molecule (the numbers are invented to show the idea)."),
        ]),
        EX("Worked example 3: after a meal", intro="Describe what happens when blood glucose rises after a meal of boiled yam.", steps=[
            S("Detection", text="Beta cells detect high glucose by an increase in ATP, closing K⁺ channels and opening Ca²⁺ channels."),
            S("Release", text="Insulin is released by exocytosis."),
            S("Effect", text="Muscle, fat and liver cells take up glucose, and glycogenesis speeds up. Blood glucose falls."),
            S("Feedback", text="As glucose falls, insulin release decreases."),
        ]),
        MISTAKE("Mixing up glycogen and glucagon", "Glycogen is a storage polysaccharide. Glucagon is a hormone. Examiners penalise writing one for the other."),
        MISTAKE("Saying that insulin 'converts' glucose to glycogen directly", "Insulin is a hormone that stimulates liver and muscle cells to take up glucose and activates the enzyme (glycogen synthase) that makes glycogen. Enzymes do the conversion."),
        QUIZ("Which hormone raises blood glucose by stimulating glycogenolysis in the liver?",
             ["Insulin", "Glucagon", "ADH", "Aldosterone"], 1,
             "Glucagon from alpha cells activates glycogen phosphorylase through cAMP.",
             hint="It is made by the alpha cells.",
             feedback=["Insulin lowers blood glucose.", "", "ADH controls water.", "Aldosterone controls Na⁺."]),
        QUIZ("What is the second messenger in the response of a liver cell to glucagon?",
             ["Glucose", "cAMP", "Insulin", "Glycogen"], 1,
             "The hormone binds the receptor, and adenylyl cyclase makes cAMP inside the cell.",
             hint="It is made from ATP by adenylyl cyclase.",
             feedback=["Glucose is released, not a messenger.", "", "Insulin is a different hormone.", "Glycogen is the substrate of the cascade."]),
        PQ("Describe how a rise in blood glucose leads to the release of insulin from a beta cell.",
           "Glucose enters the beta cell and is respired, raising ATP. ATP closes K⁺ channels, so the membrane depolarises. Voltage-gated Ca²⁺ channels open, Ca²⁺ enters and causes vesicles containing insulin to fuse with the membrane and release insulin by exocytosis."),
        PQ("Explain what is meant by a second messenger and how the cAMP cascade amplifies the effect of glucagon.",
           "A second messenger is a molecule made inside the cell when a hormone binds to its surface receptor; cAMP is an example. Each hormone-receptor complex activates many G proteins, each adenylyl cyclase makes many cAMP, and each enzyme activates many molecules of the next, so one hormone molecule causes the breakdown of very many glycogen molecules."),
        PQ("Explain why blood glucose control uses two hormones with opposite effects.",
           "Insulin lowers and glucagon raises blood glucose. With two opposing effectors, a rise or a fall can be corrected quickly and glucose stays close to the set point."),
        PQ("Compare type 1 and type 2 diabetes mellitus.",
           "In type 1 beta cells are destroyed (autoimmune), so little insulin is made; it is treated with insulin. In type 2 the body cells respond poorly to insulin; it is linked to diet and low activity, and is treated with diet, exercise and drugs, sometimes insulin."),
        TIP("Blood glucose control is often tested in Paper 1 as a data question (a graph of glucose and insulin levels) and in Paper 2 as an essay on negative feedback and second messengers."),
        SUM("Beta cells release insulin when glucose is high; alpha cells release glucagon when it is low. Together they give negative feedback control around about 4 to 6 mmol per litre.",
            "Insulin increases glucose uptake and glycogenesis; glucagon increases glycogenolysis and gluconeogenesis.",
            "Glucagon and adrenaline act through the G protein, adenylyl cyclase, cAMP and kinases, which amplifies the signal.",
            "Type 1 diabetes: little insulin; type 2: poor response to insulin."),
    ],
))

# ------------------------------------------------------------------ 14. Thermoregulation
LESSONS.append(lesson(
    module=M2,
    topic="Thermoregulation",
    title="Thermoregulation: endotherms and ectotherms",
    slug="biu1-thermoregulation",
    minutes=22,
    summary="How mammals keep a steady core temperature through the hypothalamus, skin and muscles, how ectotherms use behaviour, the cause of fever, and calculations with Q10 and the heat removed by sweating.",
    objectives=[
        "Distinguish endotherms from ectotherms and explain the advantages and costs of each",
        "Describe how the hypothalamus detects temperature and controls effectors in the skin and muscles",
        "Explain fever as a change of set point",
        "Calculate a temperature coefficient (Q10) and the cooling effect of sweat",
    ],
    key_concepts=["Endotherm", "Ectotherm", "Core temperature", "Thermoreceptor", "Vasodilation", "Vasoconstriction", "Sweating", "Shivering", "Brown fat", "Q10", "Fever"],
    blocks=[
        H("Introduction"),
        T("In the cool mornings of Dschang the common rainbow lizard (agama) sits on a rock, slowly warming in the sun, while the goat beside it stays at a steady body temperature all day. "
          "Both are controlling their temperature, in different ways. Temperature matters because enzyme-controlled reactions speed up when warm and denature when too hot."),
        KEY("Two strategies", "The difference is in the main source of heat.", cards=[
            ["Endotherm", "Produces most of its heat by its own metabolism (mammals and birds). Keeps a fairly constant core temperature (about 37 °C in humans). Uses much energy and food."],
            ["Ectotherm", "Gets most heat from the environment (reptiles, amphibians, fish, insects). Body temperature follows the surroundings; controlled by behaviour. Uses little food energy."],
        ]),
        T("**Endotherms** can be active at night and in cold climates, but must eat much more: a mouse uses far more energy per gram than a lizard of similar size. **Ectotherms** save energy, but they are slow when cold."),
        H("How heat is gained and lost"),
        CODE("""Process        Meaning
Metabolism     Heat released in cells, mainly liver and muscle (a gain)
Conduction     Direct transfer of heat between touching objects
Convection     Heat carried away by moving air or water
Radiation      Infrared heat given out by a warm body (or absorbed from the sun)
Evaporation    Loss of heat as sweat or water changes to vapour (about 2400 kJ per litre)""", "text", title="Heat exchange"),
        H("Control by the hypothalamus"),
        T("**Thermoreceptors** in the skin detect surface temperature. **Central thermoreceptors** in the hypothalamus detect the temperature of the blood. "
          "The **hypothalamus** (the preoptic area and a heat-loss and heat-gain centre) acts as the coordinator. It compares the information with the set point of about 37 °C and sends impulses to the effectors."),
        CODE("""                When too hot (heat loss)                 When too cold (heat gain and conservation)
Skin arterioles Vasodilation: more blood flows near the  Vasoconstriction: less blood flows near the
                surface; more heat lost by radiation      surface; less heat lost
Sweat glands    Secrete sweat; evaporation cools          Little or no sweat
Hair muscles    Hairs lie flat (little air trapped)       Hairs stand up (erector pili) and trap a
                                                          layer of warm air (small effect in humans)
Skeletal muscle No shivering                              Shivering: rapid contractions release heat
Metabolism      Reduced                                   Raised (thyroxine, adrenaline, brown fat)
Behaviour       Seek shade, remove clothes, drink         Put on clothes, seek warmth, curl up""", "text", title="Responses of a human"),
        T("**Brown adipose tissue**, present in babies and some adults, has mitochondria with a protein (thermogenin, UCP1) that lets protons leak back across the inner membrane. "
          "The energy is released as heat instead of making ATP (compare the uncoupler in the oxidative phosphorylation lesson)."),
        T("Strictly, **arterioles** change in diameter (not capillaries, which have no muscle). Many textbooks write 'vasodilation of skin capillaries'; check how your teacher words it."),
        H("Fever and the set point"),
        T("During an infection, such as malaria, white blood cells release chemicals called **pyrogens**. These raise the set point of the hypothalamus above 37 °C. "
          "The body now feels cold and responds as if it were too cool: vasoconstriction and shivering raise the temperature. "
          "When the infection is controlled, the set point returns to normal and the person sweats as the body cools. High temperature can slow some pathogens, but a temperature above about 41 °C is dangerous."),
        H("Temperature coefficient"),
        F(r"Q_{10} = \frac{R_2}{R_1} \quad \text{for a temperature rise of } 10{}^{\circ}\text{C}", title="Q10"),
        F(r"R_2 = R_1 \times Q_{10}^{(T_2 - T_1)/10}", title="For any temperature change"),
        T("Q10 is the factor by which the rate of a process increases for a rise of 10 °C. Many biological reactions have a Q10 of about 2 over the normal range; ectotherms' metabolic rates follow the temperature, but endotherms keep their own temperature constant."),
        H("Worked examples"),
        EX("Worked example 1: Q10 from data", intro="A lizard's heart rate is 12 beats per minute at 20 °C and 30 beats per minute at 30 °C. Calculate Q10 and predict the heart rate at 25 °C.", steps=[
            S("Q10", math=r"Q_{10} = \frac{30}{12} = 2.5"),
            S("Rate at 25 °C", math=r"R_2 = 12 \times 2.5^{(25-20)/10} = 12 \times 2.5^{0.5}"),
            S("Calculate", math=r"12 \times 1.58 = 19 \text{ beats per minute}"),
        ]),
        EX("Worked example 2: sweating", intro="During exercise, a runner has to lose 700 W of heat. Each litre of sweat that evaporates removes about 2400 kJ. How much sweat must evaporate in one hour?", steps=[
            S("Energy in one hour", math=r"700 \times 3600 = 2\,520\,000 \text{ J} = 2520 \text{ kJ}"),
            S("Sweat needed", math=r"\frac{2520}{2400} \approx 1.05 \text{ litres}"),
            S("Comment", text="Sweat that drips off without evaporating does not cool the body. High humidity, common in coastal Cameroon, slows evaporation."),
        ]),
        EX("Worked example 3: why do we shiver and have goose pimples?", intro="Describe the responses of the skin and muscles of a person standing in the cold on the Bamenda highlands.", steps=[
            S("Arterioles", text="Vasoconstriction reduces blood flow to the skin and so reduces heat loss."),
            S("Muscles", text="Shivering: rapid contractions use ATP and release heat."),
            S("Hair", text="Erector pili muscles contract; the hairs stand up (goose pimples). In humans this has little effect."),
            S("Metabolism", text="Thyroxine and adrenaline increase the metabolic rate."),
        ]),
        MISTAKE("Saying that blood vessels 'move' towards the surface", "Arterioles dilate, so more blood flows through the capillaries near the skin. The vessels do not move."),
        MISTAKE("Saying that fever is a failure of the thermostat", "In fever the set point is raised on purpose; the thermostat works against the new set point."),
        QUIZ("What happens to the skin arterioles of a person who is too hot?",
             ["Vasoconstriction", "Vasodilation", "No change", "They move deeper into the skin"], 1,
             "Dilation increases blood flow near the surface, so more heat is lost.",
             hint="You become red-faced after a run.",
             feedback=["That reduces heat loss, a response to cold.", "", "Arterioles are a main effector.", "Blood vessels do not move; their diameter changes."]),
        QUIZ("What is the main cause of the rise in body temperature during fever?",
             ["Failure of sweating", "Pyrogens raise the set point in the hypothalamus", "Loss of body hair", "A fall in metabolic rate"], 1,
             "The hypothalamus is reset to a higher value, so heat-gain responses operate until the new value is reached.",
             hint="The thermostat is reset.",
             feedback=["Sweating is switched off in the early stage because the body is trying to warm up.", "", "Hair loss is not relevant.", "Metabolic rate rises."]),
        PQ("Distinguish between an endotherm and an ectotherm and give one advantage of each.",
           "An endotherm produces most of its heat internally and keeps a constant core temperature; an ectotherm depends on external heat. Endotherm advantage: can be active in cold conditions and at night. Ectotherm advantage: needs much less food, since it does not use energy to make heat."),
        PQ("Describe how the body responds to a fall in the temperature of the blood.",
           "Central thermoreceptors in the hypothalamus detect the fall. The hypothalamus sends impulses to the skin arterioles (vasoconstriction), to the skeletal muscles (shivering), to sweat glands (stop sweating), and to endocrine glands (thyroxine, adrenaline), raising the metabolic rate. Heat loss falls and heat production rises."),
        PQ("An insect's metabolic rate is 15 units at 20 °C and 45 units at 30 °C. Calculate Q10 and explain what the value shows.",
           "Q10 = 45 / 15 = 3.0. The rate triples for a 10 °C rise: it is very temperature-dependent, as in an ectotherm, whose enzyme-controlled reactions speed up when warm."),
        PQ("Explain why a high humidity makes it harder for a person to lose heat by sweating.",
           "Sweat cools by evaporation, which needs the air to take up more water vapour. When the air is already almost saturated, evaporation is slow, so less heat is removed, and the sweat runs off without cooling."),
        TIP("Thermoregulation is common in Paper 2 (with a labelled skin diagram) and in Paper 1 (a graph of core temperature). Name each receptor, the hypothalamus, and each effector, and say whether it is a response to heat or cold."),
        SUM("Endotherms control temperature by internal heat production; ectotherms use behaviour and external heat.",
            "The hypothalamus compares information from skin and central thermoreceptors with a set point of about 37 °C.",
            "Heat loss: vasodilation, sweating. Heat gain and conservation: vasoconstriction, shivering, raised metabolism, brown fat.",
            "Fever raises the set point. Q10 = rate at (T + 10) divided by rate at T."),
    ],
))

# ------------------------------------------------------------------ 15. Resting potential
LESSONS.append(lesson(
    module=M3,
    topic="Resting and action potentials",
    title="The resting potential of a neurone",
    slug="biu1-resting-potential",
    minutes=22,
    summary="How the sodium-potassium pump, potassium leak channels and large negative ions in the cytoplasm set up a resting potential of about -70 mV, with the Nernst equation to calculate equilibrium potentials.",
    objectives=[
        "State the structure of a motor neurone and define potential difference across a membrane",
        "Explain how the distribution of ions, the sodium-potassium pump and the leak channels produce the resting potential",
        "Calculate the equilibrium potential of an ion with the Nernst equation",
        "Predict how changing the ion concentration changes the resting potential",
    ],
    key_concepts=["Neurone", "Resting potential", "Polarised membrane", "Sodium-potassium pump", "Leak channel", "Electrochemical gradient", "Nernst equation", "Equilibrium potential"],
    blocks=[
        H("Introduction"),
        T("An impulse travelling from your foot to your spinal cord is not electricity flowing through a wire. It is a wave of changes in the membrane of a nerve fibre. "
          "Before a wave can travel, the membrane must be ready. A neurone at rest has a voltage across its membrane, as a battery has. This is the **resting potential**. "
          "The Board's 2023 report found that many candidates could not distinguish the resting potential from the action potential, so this lesson is worth reading slowly."),
        T("A **motor neurone** has a cell body with the nucleus, short branching **dendrites**, and a long **axon** that carries impulses away from the cell body. Many axons are wrapped by a fatty "
          "**myelin sheath** made by Schwann cells, with small gaps called **nodes of Ranvier**. Axons can be more than a metre long in humans."),
        D("The **resting potential** is the potential difference across the membrane of an excitable cell that is not conducting an impulse. In a neurone it is about −70 mV (the inside is negative compared with the outside).",
          title="Definition: resting potential"),
        D("A membrane is **polarised** when there is a potential difference (a voltage) across it, because positive and negative charges are unequally distributed on the two sides.",
          title="Definition: polarised"),
        H("The three causes"),
        KEY("Why the inside is negative", "Three things work together.", cards=[
            ["1 Unequal ion distribution", "Inside the axon K⁺ is high (about 140 mmol/L) and Na⁺ low (about 15). Outside, Na⁺ is high (about 145) and K⁺ low (about 5). Large negative proteins and phosphates cannot leave."],
            ["2 The Na⁺/K⁺ pump", "Uses ATP to move 3 Na⁺ out and 2 K⁺ in. This removes one net positive charge each time and keeps the gradients going."],
            ["3 Leak channels", "The membrane has many open K⁺ leak channels and very few for Na⁺. K⁺ diffuses out down its gradient, leaving the inside more negative."],
        ]),
        T("Potassium ions diffuse out until the pull of the negative charge inside balances the tendency to diffuse out. Sodium ions are mostly kept out because few channels are open for them. "
          "A small number of Na⁺ leak in, which is why the resting potential (−70 mV) is less negative than the equilibrium potential of K⁺ (about −90 mV)."),
        T("The electrical force and the concentration gradient together make the **electrochemical gradient** of an ion. At the **equilibrium potential** the two are equal and opposite, so there is no net movement of that ion."),
        CODE("""Ion (teaching values for a mammalian axon, mmol per litre)
Ion     Outside    Inside     Equilibrium potential
Na+      145         15        about +61 mV
K+         5        140        about -89 mV
Cl-      110         10        about -64 mV
Resting potential of the axon: about -70 mV""", "text", title="Ion concentrations (teaching values)"),
        H("The Nernst equation"),
        F(r"E_{\text{ion}} = \frac{61.5}{z} \log_{10}\frac{[\text{ion}]_{\text{out}}}{[\text{ion}]_{\text{in}}} \ \text{mV at } 37{}^{\circ}\text{C}", title="Nernst equation (z = charge of the ion)"),
        EX("Worked example 1: equilibrium potential of K⁺", intro="Use the values in the table to calculate the equilibrium potential of K⁺.", steps=[
            S("Substitute", math=r"E_K = 61.5 \log_{10}\frac{5}{140}"),
            S("Ratio and log", math=r"\frac{5}{140} = 0.0357, \quad \log_{10}(0.0357) = -1.447"),
            S("Calculate", math=r"E_K = 61.5 \times (-1.447) = -89 \text{ mV}"),
        ]),
        EX("Worked example 2: equilibrium potential of Na⁺", intro="Calculate the equilibrium potential of Na⁺ (z = +1).", steps=[
            S("Substitute", math=r"E_{Na} = 61.5 \log_{10}\frac{145}{15}"),
            S("Calculate", math=r"61.5 \times \log_{10}(9.67) = 61.5 \times 0.985 = +61 \text{ mV}"),
            S("Meaning", text="If Na⁺ channels open, Na⁺ enter the cell and drive the membrane potential towards +61 mV. This is how the action potential rises."),
        ]),
        EX("Worked example 3: effect of high extracellular K⁺", intro="In an injury, K⁺ leaks from damaged cells so that the K⁺ outside a nerve rises from 5 to 10 mmol/L (a teaching illustration). Predict the effect on the resting potential and say why.", steps=[
            S("New equilibrium potential", math=r"E_K = 61.5 \log_{10}\frac{10}{140} = 61.5 \times (-1.146) = -70.5 \text{ mV}"),
            S("Effect", text="K⁺ now has less tendency to leave, so the inside becomes less negative: the membrane depolarises, from about −70 towards about −60 mV or less."),
            S("Consequence", text="The neurone is closer to the threshold and fires more easily; a very high K⁺ level can block conduction."),
        ]),
        T("Notice that you do not need the Nernst equation for most exam questions. You do need to explain, in words, the **distribution of ions**, the **permeability** of the membrane and the **pump**."),
        H("Comparing resting and action potential"),
        CODE("""Feature               Resting potential               Action potential
Membrane potential    about -70 mV (steady)           rises to about +40 mV, then falls
Permeability          K+ leak channels open;          Voltage-gated Na+ channels open, then
                      Na+ channels mostly closed      K+ channels open
Pump                  Na+/K+ pump active              Pump works; not the cause of the change
Energy                ATP needed to keep gradients    No extra ATP per spike; ions move down
                                                       gradients""", "text", title="Resting and action potentials compared"),
        MISTAKE("Saying that the resting neurone is 'inactive'", "The resting potential is maintained by active transport (the Na⁺/K⁺ pump uses ATP) and by diffusion. The membrane is busy."),
        MISTAKE("Saying that the membrane is impermeable to ions at rest", "It is permeable to K⁺ (leak channels) and slightly to Na⁺. It is the unequal permeability, together with the pump, that gives −70 mV."),
        QUIZ("What does the sodium-potassium pump do in a resting neurone?",
             ["Moves 3 Na⁺ out and 2 K⁺ in using ATP", "Moves 2 Na⁺ out and 3 K⁺ in using ATP", "Moves Na⁺ and K⁺ by facilitated diffusion", "Opens during depolarisation only"], 0,
             "It transports 3 Na⁺ out and 2 K⁺ in by active transport.",
             hint="More positive charge goes out than comes in.",
             feedback=["", "That is the wrong way round.", "It is an active process and needs ATP.", "It works at rest as well as during an action potential."]),
        QUIZ("Why is the inside of a resting axon negative compared with the outside?",
             ["Na⁺ leaks out faster than K⁺", "K⁺ leaks out faster than Na⁺ leaks in, and negative ions cannot leave", "Chloride ions are pumped in by ATP", "The axon has no ions"], 1,
             "K⁺ leaves through leak channels, the pump removes net positive charge, and anions stay inside.",
             hint="Which positive ion is more able to move across the membrane at rest?",
             feedback=["Na⁺ is mainly outside.", "", "Chloride is not pumped in by ATP in this way.", "It contains many ions."]),
        PQ("Explain how the resting potential of a neurone is produced and maintained.",
           "The Na⁺/K⁺ pump uses ATP to move 3 Na⁺ out and 2 K⁺ in, so Na⁺ is high outside and K⁺ high inside. K⁺ diffuses out through leak channels, which are much more numerous than Na⁺ channels, leaving the inside negative. Large negative ions cannot leave. This gives about −70 mV."),
        PQ("Calculate the equilibrium potential of Cl⁻ (z = −1) using outside 110 and inside 10 mmol per litre.",
           "E = (61.5 / −1) log10(110/10) = −61.5 × 1.041 = −64 mV."),
        PQ("Explain why the resting potential (−70 mV) is less negative than the equilibrium potential of K⁺ (−89 mV).",
           "The membrane at rest is also slightly permeable to Na⁺. Na⁺ leak in, making the inside less negative than the value the K⁺ alone would give."),
        PQ("Predict and explain the effect on the resting potential if the Na⁺/K⁺ pump is poisoned for several hours.",
           "Without ATP-driven pumping, Na⁺ gradually leaks in and K⁺ leaks out, so the concentration gradients run down and the resting potential becomes less negative (depolarised) and eventually the neurone cannot conduct impulses."),
        TIP("Say 'potential difference' (not 'charge'), name the ions, and state their direction of movement. The Board has reported that candidates mix up permeability, distribution and potential difference in the resting and action potentials, so write your answer in those three headings."),
        SUM("At rest, the inside of a neurone is about −70 mV relative to the outside.",
            "The Na⁺/K⁺ pump (3 out, 2 in), K⁺ leak channels and trapped anions produce this potential.",
            "The equilibrium potential of an ion comes from the Nernst equation: E = (61.5 / z) log10 (outside / inside) at 37 °C.",
            "The resting potential is a store of energy: it is the starting condition for the action potential."),
    ],
))

# ------------------------------------------------------------------ 16. Action potential and conduction
LESSONS.append(lesson(
    module=M3,
    topic="Resting and action potentials",
    title="The action potential and saltatory conduction",
    slug="biu1-action-potential-conduction",
    minutes=24,
    summary="The phases of an action potential (depolarisation, repolarisation, hyperpolarisation), the all-or-nothing law, the refractory period, and the faster saltatory conduction in myelinated axons, with calculations on speed and frequency.",
    objectives=[
        "Describe the events of an action potential and relate each to ion channels",
        "State and explain the all-or-nothing law and the refractory period",
        "Explain how an impulse is propagated and why saltatory conduction is faster",
        "Read an action-potential graph and calculate conduction times and maximum frequency",
    ],
    key_concepts=["Action potential", "Threshold", "Depolarisation", "Repolarisation", "Hyperpolarisation", "All-or-nothing law", "Refractory period", "Saltatory conduction", "Myelin sheath", "Node of Ranvier"],
    blocks=[
        H("Introduction"),
        T("When you touch a hot cooking pot in a kitchen in Bafoussam, an impulse travels from your fingertip to the spinal cord and back to your muscle in a fraction of a second. "
          "The impulse is a travelling **action potential**: a brief reversal of the voltage across the membrane."),
        D("An **action potential** is a rapid, temporary reversal of the potential difference across the membrane of an excitable cell, from about −70 mV to about +40 mV and back, caused by the opening of voltage-gated ion channels.",
          title="Definition: action potential"),
        IMG("al-biu1-action-potential.svg", alt="Graph of membrane potential in millivolts against time in milliseconds: rest at -70, threshold at -55, a rapid rise to +40, a fall below -70 and a slow return to rest.",
            caption="Figure 1. An action potential."),
        H("Phases of an action potential"),
        KEY("Follow the graph from left to right", "Each phase involves a change of permeability.", cards=[
            ["Resting (−70 mV)", "K⁺ leak channels open; voltage-gated channels closed."],
            ["Stimulus and threshold", "A stimulus opens a few voltage-gated Na⁺ channels. If the membrane reaches the threshold (about −55 mV), more open."],
            ["Depolarisation (to about +40 mV)", "Many voltage-gated Na⁺ channels open (positive feedback). Na⁺ rush in down their electrochemical gradient. The inside becomes positive."],
            ["Repolarisation", "Na⁺ channels close (inactivate) and voltage-gated K⁺ channels open. K⁺ leave, so the inside becomes negative again."],
            ["Hyperpolarisation (undershoot)", "K⁺ channels are slow to close, so the potential drops below −70 mV for a time."],
            ["Return to rest", "K⁺ channels close; the Na⁺/K⁺ pump and leak channels restore the resting potential and the ion gradients."],
        ]),
        T("The pump does not cause the action potential. Very few ions cross during one spike, so the gradients change very little. The pump restores the gradients afterwards."),
        H("The all-or-nothing law and the refractory period"),
        D("The **all-or-nothing law** states that an action potential either occurs fully or not at all. If the stimulus is below the threshold, no action potential is generated; stimuli above it all give a spike of the same size.",
          title="All-or-nothing law"),
        T("A stronger stimulus does not give a bigger spike. It gives **more frequent** spikes, and more neurones are stimulated. This is how the size of a stimulus is coded."),
        T("For a short time after an action potential the region of the axon cannot produce another: the Na⁺ channels are inactivated (**absolute refractory period**, about 1 to 2 ms), and for a little longer a stronger stimulus than normal is needed (**relative refractory period**). This has two effects: impulses travel in **one direction** only, since the region just passed is refractory, and the **maximum frequency** of impulses is limited."),
        H("Propagation and speed"),
        T("An action potential at one point makes a **local current** flow to the next region of the axon, depolarising it to threshold, and so the wave moves along. In an **unmyelinated** axon the action potential occurs at every point, so conduction is slow (about 0.5 to 2 m/s)."),
        T("In a **myelinated** axon the myelin sheath is a good electrical insulator. Ions can cross only at the **nodes of Ranvier** (about 1 mm apart), where there are many voltage-gated channels. "
          "The local current flows through the cytoplasm from one node to the next, and the action potential **jumps** from node to node. This is **saltatory conduction** (Latin saltare, to jump). It is much faster, up to about 100 m/s, and saves energy since fewer ions cross."),
        CODE("""Factor increasing speed             Reason
Myelination                         Saltatory conduction between nodes
Larger axon diameter                Lower resistance to current flow in the cytoplasm
Higher temperature                  Faster ion movement and channel opening""", "text", title="Factors affecting speed"),
        T("**Multiple sclerosis** is a disease in which the immune system damages myelin, so conduction slows or fails: it shows why myelin matters."),
        H("Worked examples"),
        EX("Worked example 1: reading the graph", intro="Use Figure 1. State the potential at rest, the threshold and the peak, and the time between the start of the rise and the return below −70 mV.", steps=[
            S("Rest", text="About −70 mV."),
            S("Threshold", text="About −55 mV, reached at about 1.5 ms."),
            S("Peak", text="About +40 mV at about 2 ms."),
            S("Duration", text="The potential rises from 1.5 ms and is below −70 mV by 3 ms: about 1.5 ms for the spike itself."),
        ]),
        EX("Worked example 2: conduction time", intro="An axon of length 1.0 m conducts at 100 m/s if myelinated and at 1.0 m/s if unmyelinated. Find the time for each.", steps=[
            S("Formula", math=r"\text{time} = \frac{\text{distance}}{\text{speed}}"),
            S("Myelinated", math=r"\frac{1.0}{100} = 0.01 \text{ s} = 10 \text{ ms}"),
            S("Unmyelinated", math=r"\frac{1.0}{1.0} = 1.0 \text{ s} = 1000 \text{ ms}"),
            S("Comparison", text="Myelination makes conduction 100 times faster in this example, and the unmyelinated impulse would take a full second to cross the length of a leg."),
        ]),
        EX("Worked example 3: maximum frequency", intro="The absolute refractory period of a neurone is 2 ms. What is the theoretical maximum frequency of impulses? What if it is 1 ms?", steps=[
            S("Formula", math=r"f_{\max} = \frac{1}{t_{\text{refractory}}}"),
            S("2 ms", math=r"\frac{1}{0.002} = 500 \text{ impulses per second}"),
            S("1 ms", math=r"\frac{1}{0.001} = 1000 \text{ impulses per second}"),
        ]),
        MISTAKE("Saying that Na⁺ leave during depolarisation", "Na⁺ enter the axon during depolarisation. K⁺ leave during repolarisation."),
        MISTAKE("Saying a bigger stimulus makes a bigger action potential", "All action potentials have the same size. A bigger stimulus gives a higher frequency of action potentials."),
        MISTAKE("Using 'repolarisation' to mean 'resting'", "Repolarisation is the movement back towards resting potential. After it, there is a short hyperpolarisation before the true resting potential is restored."),
        QUIZ("Which event causes the rising phase of an action potential?",
             ["Opening of voltage-gated K⁺ channels", "Opening of voltage-gated Na⁺ channels and Na⁺ entry", "Activity of the Na⁺/K⁺ pump", "Closing of K⁺ leak channels"], 1,
             "Na⁺ enter down their gradient and depolarise the membrane.",
             hint="The membrane becomes positive inside.",
             feedback=["K⁺ channels cause the falling phase.", "", "The pump restores the resting state; it is too slow for the spike.", "Leak channels are not the cause of the rise."]),
        QUIZ("Why does an action potential travel in one direction only?",
             ["The axon is shaped like a one-way tube", "The region behind is in its refractory period", "The sodium channels are only at one end", "The impulse is carried by diffusion of Na⁺"], 1,
             "Na⁺ channels behind the impulse are inactivated, so the local current can only depolarise the region ahead.",
             hint="Think about the recently active region.",
             feedback=["The axon has no one-way structure.", "", "Channels occur along the whole axon.", "The signal is an electrical wave, not diffusion."]),
        PQ("Describe the changes in ion movements during an action potential.",
           "When the threshold is reached, voltage-gated Na⁺ channels open and Na⁺ enter, depolarising the membrane to about +40 mV. Na⁺ channels then close and voltage-gated K⁺ channels open, so K⁺ leave and the membrane repolarises. K⁺ channels close slowly, giving a hyperpolarisation, and the pump and leak channels restore the resting potential."),
        PQ("State the all-or-nothing law and explain how an axon signals the strength of a stimulus.",
           "An action potential occurs fully when the threshold is reached, and not at all below it. A stronger stimulus gives action potentials at a higher frequency, and more neurones are stimulated, so strength is coded by frequency and number of neurones."),
        PQ("Explain why myelinated axons conduct impulses faster than unmyelinated axons.",
           "The myelin sheath insulates the axon so that ions can cross only at the nodes of Ranvier. The action potential jumps from node to node (saltatory conduction) by local currents, instead of being regenerated at every point."),
        PQ("An impulse travels 0.9 m along a myelinated motor neurone at 90 m/s. Calculate the time. If the absolute refractory period is 2 ms, calculate the maximum frequency.",
           "Time = 0.9 / 90 = 0.01 s = 10 ms. Maximum frequency = 1 / 0.002 = 500 per second."),
        TIP("The 2023 report shows that candidates lose marks by not separating resting and action potentials. Use a table of three headings: distribution of ions, permeability of the membrane and potential difference."),
        SUM("An action potential has depolarisation (Na⁺ in), repolarisation (K⁺ out) and hyperpolarisation, then the pump restores the resting state.",
            "It is all-or-nothing and has the same size; stimulus strength is coded by frequency.",
            "The refractory period makes conduction one-way and sets a maximum frequency.",
            "Saltatory conduction in myelinated axons is faster and uses less energy."),
    ],
))

# ------------------------------------------------------------------ 17. Synapses
LESSONS.append(lesson(
    module=M3,
    topic="Synapses",
    title="Synapses: cholinergic and adrenergic transmission",
    slug="biu1-synapses",
    minutes=24,
    summary="How an impulse crosses a cholinergic synapse by calcium entry, vesicle exocytosis and receptors, how adrenergic synapses differ, how EPSPs and IPSPs sum, and how toxins and drugs interfere.",
    objectives=[
        "Describe the sequence of events at a cholinergic synapse",
        "Explain how the transmitter is removed and why synapses make transmission one-way",
        "Explain spatial and temporal summation, and the roles of excitatory and inhibitory synapses",
        "Compare cholinergic and adrenergic synapses and explain the action of some drugs and poisons",
    ],
    key_concepts=["Synapse", "Neurotransmitter", "Acetylcholine", "Acetylcholinesterase", "Cholinergic synapse", "Adrenergic synapse", "EPSP", "IPSP", "Summation", "Neuromuscular junction"],
    blocks=[
        H("Introduction"),
        T("Neurones do not touch. Between the end of one and the start of the next is a gap of about 20 nm, the **synaptic cleft**. The impulse must cross this gap with the help of a chemical. "
          "Many farmers in Cameroon use organophosphate insecticides on crops, and poisoning from them shows what happens when one of the enzymes at the synapse is blocked."),
        D("A **synapse** is a junction between two neurones, or between a neurone and an effector cell, where information passes by a chemical **neurotransmitter** across a narrow gap.",
          title="Definition: synapse"),
        IMG("al-biu1-synapse.svg", alt="Cholinergic synapse: presynaptic knob with mitochondrion, vesicles of acetylcholine and calcium channel; synaptic cleft with acetylcholinesterase; postsynaptic membrane with receptor sodium channels.",
            caption="Figure 1. A cholinergic synapse."),
        H("Events at a cholinergic synapse"),
        T("A **cholinergic synapse** uses **acetylcholine (ACh)** as the transmitter. Examples include the neuromuscular junction, parasympathetic nerve endings and many synapses in the brain."),
        KEY("Sequence of events", "Learn these in order.", cards=[
            ["1", "An action potential arrives at the presynaptic knob and depolarises it."],
            ["2", "Voltage-gated Ca²⁺ channels open. Ca²⁺ diffuse in from the cleft."],
            ["3", "Ca²⁺ cause vesicles that contain ACh to move to the presynaptic membrane and fuse with it (exocytosis). ACh is released into the cleft."],
            ["4", "ACh diffuses across the cleft and binds to receptors on the postsynaptic membrane (receptors are Na⁺ channels)."],
            ["5", "The channels open and Na⁺ enter the postsynaptic neurone. This depolarises it: an excitatory postsynaptic potential (EPSP). If it reaches the threshold, an action potential starts."],
            ["6", "ACh is broken down by the enzyme acetylcholinesterase (AChE) into choline and ethanoate (acetate). The channels close."],
            ["7", "Choline is taken back into the presynaptic knob and is used with ATP to make more ACh (mitochondria supply the ATP)."],
        ]),
        T("Breaking down ACh is important: otherwise it would continue to stimulate the postsynaptic membrane, and a single impulse would cause repeated firing."),
        H("Properties of synapses"),
        T("**One-way transmission**: only the presynaptic knob has vesicles of transmitter, and only the postsynaptic membrane has receptors. **Synaptic delay**: about 0.5 ms for diffusion and the other steps. "
          "**Integration**: a postsynaptic neurone can add up signals from many presynaptic neurones. **Fatigue**: if a synapse is stimulated for a long time, the vesicles run out, so transmission fails."),
        D("**Summation** is the adding together of the effects of several subthreshold stimuli at a synapse. **Spatial summation** is the adding of EPSPs from different presynaptic neurones at the same time; **temporal summation** is the adding of EPSPs from one neurone arriving in quick succession.",
          title="Definition: summation"),
        T("Some synapses are **inhibitory**. The transmitter (for example GABA or glycine) opens Cl⁻ or K⁺ channels, so the postsynaptic membrane becomes more negative: an **inhibitory postsynaptic potential (IPSP)**. It is harder to reach the threshold. The neurone adds up all EPSPs and IPSPs."),
        H("Adrenergic synapses"),
        T("**Adrenergic synapses** release **noradrenaline** (norepinephrine). They are found at the ends of sympathetic neurones to organs such as the heart, which prepares the body for action. "
          "Noradrenaline binds to receptors on the target cell (many are G-protein linked and use a second messenger). It is removed mainly by **reuptake** into the presynaptic knob, and partly broken down by enzymes (MAO and COMT)."),
        CODE("""Feature              Cholinergic synapse              Adrenergic synapse
Transmitter          Acetylcholine                    Noradrenaline
Found at             Motor end plate, parasympathetic Sympathetic nerve endings
Receptor             Ion channel (Na+) or G protein   Mostly G-protein receptors
Removal              Broken down by AChE              Mostly reuptake into knob; enzymes""", "text", title="Comparison"),
        H("Drugs and poisons"),
        CODE("""Substance                  Action                                     Effect
Organophosphate pesticides Inhibit acetylcholinesterase                ACh builds up; continuous contraction,
and nerve agents                                                       muscle twitching, paralysis
Curare                     Blocks ACh receptors                        Muscle paralysis
Botulinum toxin            Stops release of ACh from the knob          Flaccid paralysis
Nicotine                   Mimics ACh, binds its receptors             Stimulation
Cocaine                    Blocks reuptake of noradrenaline (and       Prolonged stimulation
                           dopamine)""", "text", title="Substances that act at synapses"),
        H("Worked examples"),
        EX("Worked example 1: sequence", intro="Explain why the arrival of an action potential at the presynaptic knob leads to ACh release.", steps=[
            S("Depolarisation", text="The action potential opens voltage-gated Ca²⁺ channels in the presynaptic membrane."),
            S("Calcium entry", text="Ca²⁺ diffuse in down their concentration gradient."),
            S("Exocytosis", text="Ca²⁺ cause vesicles to fuse with the membrane and release ACh into the cleft."),
        ]),
        EX("Worked example 2: delay in a reflex", intro="A withdrawal reflex has a sensory neurone and a motor neurone with 2 synapses in total (an interneurone between them). The impulse travels 0.9 m at 60 m/s along the neurones, and each synapse adds a delay of 0.5 ms. Calculate the total time.", steps=[
            S("Conduction time", math=r"\frac{0.9}{60} = 0.015 \text{ s} = 15 \text{ ms}"),
            S("Synaptic delay", math=r"2 \times 0.5 = 1.0 \text{ ms}"),
            S("Total", math=r"15 + 1.0 = 16 \text{ ms}"),
        ]),
        EX("Worked example 3: summation", intro="A postsynaptic neurone has a resting potential of −70 mV and a threshold of −55 mV. Each EPSP raises the potential by 6 mV, and an IPSP lowers it by 4 mV. Three EPSPs and one IPSP arrive at the same time. Does the neurone fire?", steps=[
            S("EPSPs", math=r"3 \times 6 = +18 \text{ mV}"),
            S("IPSP", math=r"-4 \text{ mV}"),
            S("Net change", math=r"18 - 4 = +14 \text{ mV}"),
            S("New potential", math=r"-70 + 14 = -56 \text{ mV}"),
            S("Result", text="−56 mV is just below the threshold of −55 mV, so the neurone does not fire. One more EPSP would take it over the threshold (teaching numbers)."),
        ]),
        MISTAKE("Saying that the impulse itself crosses the gap", "The action potential does not cross. A chemical transmitter crosses, and a new action potential is started in the next neurone."),
        MISTAKE("Saying Na⁺ channels in the presynaptic membrane trigger release", "Voltage-gated Ca²⁺ channels, not Na⁺ channels, open at the presynaptic knob. Ca²⁺ entry causes exocytosis."),
        QUIZ("What is the role of acetylcholinesterase at a cholinergic synapse?",
             ["It makes ACh in the knob", "It breaks down ACh in the cleft", "It opens Ca²⁺ channels", "It carries ACh across the cleft"], 1,
             "It hydrolyses ACh to choline and ethanoate, ending the stimulation.",
             hint="It stops the signal.",
             feedback=["ACh is made by choline acetyltransferase.", "", "Calcium channels are voltage-gated.", "ACh crosses the cleft by diffusion."]),
        QUIZ("An organophosphate insecticide inhibits acetylcholinesterase. What is the likely effect on a skeletal muscle?",
             ["Relaxed paralysis", "Continuous contraction and twitching", "No effect", "Increased relaxation"], 1,
             "ACh stays in the cleft and keeps stimulating the muscle.",
             hint="What happens when ACh is not removed?",
             feedback=["Curare and botulinum toxin cause that kind of paralysis.", "", "It is a serious poison.", "More ACh gives more stimulation, not relaxation."]),
        PQ("Describe the events that occur at a cholinergic synapse after an action potential reaches the presynaptic knob.",
           "Voltage-gated Ca²⁺ channels open and Ca²⁺ enter. Vesicles containing ACh fuse with the presynaptic membrane and release ACh by exocytosis. ACh diffuses across the cleft and binds to receptors on the postsynaptic membrane. Na⁺ channels open, Na⁺ enter and depolarise the membrane (EPSP). If the threshold is reached an action potential starts. ACh is broken down by acetylcholinesterase and the products are recycled."),
        PQ("Explain what is meant by spatial and temporal summation.",
           "Spatial summation: EPSPs from several presynaptic neurones arrive at the same time and add together to reach the threshold. Temporal summation: several impulses from one presynaptic neurone arrive in quick succession, so the EPSPs add before they fade."),
        PQ("Explain why a synapse allows transmission in one direction only.",
           "Only the presynaptic knob contains vesicles with transmitter and voltage-gated Ca²⁺ channels, and only the postsynaptic membrane has receptors for the transmitter."),
        PQ("A reflex arc has 3 synapses. Nerve conduction takes 12 ms and each synapse adds 0.5 ms. Calculate the total delay and the percentage of the time that is due to synapses.",
           "Synaptic delay = 3 × 0.5 = 1.5 ms. Total = 13.5 ms. Percentage = 1.5 / 13.5 × 100 = 11 percent."),
        TIP("The synapse is part of the 2023 Paper 2 question on nerve impulses; marks are for the order of events (Ca²⁺, exocytosis, diffusion, receptors, Na⁺ channels, removal). Include the enzyme and say what happens to the products."),
        SUM("At a cholinergic synapse: action potential, Ca²⁺ entry, vesicle fusion, ACh diffusion, binding, Na⁺ entry, EPSP, ACh breakdown.",
            "Synapses give one-way transmission, delay, summation and integration; inhibitory synapses produce IPSPs.",
            "Adrenergic synapses release noradrenaline, mostly removed by reuptake.",
            "Organophosphates block acetylcholinesterase; curare blocks receptors; botulinum toxin stops release."),
    ],
))

# ------------------------------------------------------------------ 18. Sensory receptors
LESSONS.append(lesson(
    module=M3,
    topic="Sensory receptors",
    title="Sensory receptors: the retina and the organ of Corti",
    slug="biu1-sensory-receptors",
    minutes=24,
    summary="How receptors act as transducers producing a generator potential, how rods and cones detect light using rhodopsin, how the organ of Corti detects sound, and the ideas of sensitivity, acuity and adaptation.",
    objectives=[
        "Define a sensory receptor and explain transduction and the generator potential",
        "Compare rods and cones and explain the photochemistry of rhodopsin",
        "Describe how sound waves are detected in the cochlea and how pitch and loudness are coded",
        "Link retina structure to sensitivity and acuity",
    ],
    key_concepts=["Receptor", "Transducer", "Generator potential", "Rod", "Cone", "Rhodopsin", "Fovea", "Organ of Corti", "Hair cell", "Basilar membrane"],
    blocks=[
        H("Introduction"),
        T("A fisherman at Limbe at dusk can still see the bobbing float, but he sees it in grey: colour has disappeared. A drummer hears a sound as high or low, soft or loud. "
          "These abilities depend on **sensory receptors**, specialised cells that convert one form of energy into the electrical signals of the nervous system."),
        D("A **sensory receptor** is a cell or part of a cell that detects a stimulus and converts its energy into an electrical signal. Receptors are **transducers**: they convert the energy of the stimulus (light, sound, pressure, chemicals) into a change in membrane potential, the **generator potential**.",
          title="Definition: receptor and transduction"),
        T("A generator potential is a **graded** change: a bigger stimulus gives a bigger generator potential. If it reaches the threshold in the sensory neurone, action potentials are fired. A stronger stimulus gives a higher frequency of action potentials. "
          "Many receptors show **adaptation**: with constant stimulation the generator potential and the frequency of impulses fall (we stop feeling our clothes)."),
        H("The retina: rods and cones"),
        T("Light enters the eye, is focused by the cornea and the lens and falls on the **retina**. The retina has three layers of cells: the **photoreceptors** (rods and cones) at the back, then **bipolar neurones**, then **ganglion cells** whose axons form the **optic nerve**. "
          "The light must pass through the other layers to reach the photoreceptors."),
        CODE("""Feature              Rods                          Cones
Number               about 120 million             about 6 million
Pigment              Rhodopsin                     Three types of iodopsin (blue, green, red)
Light needed         Dim light (sensitive)         Bright light
Colour               No (black and white)          Yes (colour vision)
Connection           Many rods to one bipolar      Often one cone to one bipolar
                     neurone (convergence)         neurone in the fovea
Acuity (detail)      Low                           High
Where                Mostly outside the fovea      Concentrated in the fovea""", "text", title="Rods and cones (approximate numbers; check your textbook)"),
        T("Many rods converge on one bipolar neurone, so their small generator potentials add up (**summation**). This makes rods very **sensitive**, but the image is less detailed, so acuity is low. "
          "Cones in the **fovea** have a one-to-one connection, giving high **acuity**, but they need brighter light."),
        D("**Rhodopsin** is the light-sensitive pigment of rod cells. It consists of the protein **opsin** and a molecule called **retinal** (made from vitamin A). A photon of light changes the shape of retinal from 11-cis to all-trans, and the rhodopsin splits into opsin and retinal (it is **bleached**).",
          title="Definition: rhodopsin"),
        T("In the dark, Na⁺ channels in the rod are held open by cyclic GMP (cGMP), so the rod is partly depolarised and releases the transmitter glutamate continuously. "
          "In light, bleached rhodopsin activates a G protein (transducin) and then an enzyme that breaks down cGMP. The Na⁺ channels close, the rod becomes **hyperpolarised**, and it releases **less** transmitter. "
          "This change excites the bipolar and then the ganglion cells, which send action potentials in the optic nerve. In the dark, rhodopsin is made again, which takes a few minutes: this is **dark adaptation**."),
        T("**Vitamin A** is needed to make retinal, so lack of vitamin A leads to **night blindness**. Red palm oil, carrots and green leaves are good sources."),
        T("Colour vision is **trichromatic**: the three types of cone respond best to blue, green and red light, and the brain compares the signals. Red-green colour blindness is caused by a recessive allele on the X chromosome (see the genetics module)."),
        H("The organ of Corti"),
        T("Sound waves are collected by the pinna and pass along the ear canal to the **tympanic membrane (eardrum)**, which vibrates. Three small bones, the **malleus, incus and stapes**, transmit the vibrations to the **oval window**. "
          "Because the eardrum is much larger than the oval window and the bones act as levers, the pressure change is increased. The vibrations pass into the fluid (perilymph) of the **cochlea**."),
        T("In the cochlea, fluid waves make the **basilar membrane** vibrate. On the basilar membrane lies the **organ of Corti**, which contains **hair cells** whose tips (stereocilia) touch the overlying **tectorial membrane**. "
          "When the basilar membrane moves, the stereocilia bend against the tectorial membrane. This opens K⁺ channels (K⁺ enter from the endolymph around the hairs) and depolarises the hair cell, which releases transmitter at its base. "
          "Sensory neurones of the **auditory nerve** are stimulated and send action potentials to the brain."),
        KEY("How sound is coded", "Pitch and loudness are separate.", cards=[
            ["Pitch (frequency)", "Different parts of the basilar membrane vibrate for different frequencies: high-pitched sounds near the oval window (narrow, stiff end), low-pitched sounds further along (wider, floppy end). The brain interprets which neurones fire."],
            ["Loudness (amplitude)", "A louder sound makes the membrane move more, bending more hair cells and increasing the frequency of impulses."],
        ]),
        T("Humans hear about 20 to 20 000 Hz. Loud noise can damage the stereocilia permanently, so music at high volume is harmful."),
        H("Worked examples"),
        EX("Worked example 1: sensitivity and acuity", intro="Explain why an object seen at dusk looks grey and indistinct.", steps=[
            S("Dim light", text="Cones need bright light, so they do not respond. Only rods are active."),
            S("Colour", text="Rods contain one pigment, rhodopsin, and give no colour information, so the scene is grey."),
            S("Detail", text="Many rods converge on one bipolar neurone, so the brain cannot tell which rod was stimulated: low acuity."),
        ]),
        EX("Worked example 2: convergence", intro="A retina has about 126 million photoreceptors (120 million rods and 6 million cones) and about 1 million ganglion cells. Calculate the average number of photoreceptors per ganglion cell and comment.", steps=[
            S("Divide", math=r"\frac{126 \times 10^6}{1 \times 10^6} = 126"),
            S("Comment", text="On average more than 100 photoreceptors share one ganglion cell. Convergence is greatest among rods, and least in the fovea, where it is about one cone to one ganglion cell."),
        ]),
        EX("Worked example 3: the path of sound", intro="Number these parts in the order in which sound passes through them: stapes, tympanic membrane, hair cells, incus, malleus, oval window.", steps=[
            S("Order", text="Tympanic membrane, malleus, incus, stapes, oval window, (perilymph and basilar membrane), hair cells."),
            S("Why this matters", text="The ossicles amplify the pressure change and transfer it from air to fluid, where it is hard to move."),
        ]),
        MISTAKE("Saying rods have no pigment", "Rods contain rhodopsin. Cones contain iodopsins. Both are photopigments."),
        MISTAKE("Saying that light causes depolarisation of the rod", "In a rod, light causes hyperpolarisation. This reduces release of the transmitter. The bipolar neurone is then excited by the reduced release (many textbooks omit this detail; check yours)."),
        QUIZ("Which cells give high visual acuity?",
             ["Rods in the periphery", "Cones in the fovea", "Ganglion cells", "Bipolar cells with many rods connected"], 1,
             "Cones in the fovea each connect to one bipolar neurone, so fine detail is resolved.",
             hint="Where do we focus to read small print?",
             feedback=["Rods have convergence, so give low acuity.", "", "Ganglion cells carry the impulses; they do not detect light.", "Convergence reduces acuity."]),
        QUIZ("What bends when sound causes the basilar membrane to move?",
             ["Stereocilia of hair cells", "The cornea", "The oval window", "The auditory nerve"], 0,
             "Hair cell stereocilia bend against the tectorial membrane, opening ion channels.",
             hint="They are the tiny 'hairs' of the receptor cell.",
             feedback=["", "The cornea is part of the eye.", "The oval window transmits vibration to the cochlear fluid.", "The auditory nerve carries impulses."]),
        PQ("Define a transducer and explain what a generator potential is.",
           "A transducer converts one form of energy into another. A sensory receptor converts stimulus energy into a change in membrane potential, the generator potential. It is graded: it increases with the stimulus. If it reaches the threshold, action potentials are produced in the sensory neurone."),
        PQ("Describe what happens to rhodopsin in a rod cell in bright light.",
           "A photon makes retinal change from 11-cis to all-trans, so rhodopsin splits into opsin and retinal (it is bleached). This activates transducin and an enzyme which breaks down cGMP, so the Na⁺ channels close, the rod is hyperpolarised and releases less transmitter onto the bipolar neurone."),
        PQ("Compare rods and cones.",
           "Rods contain rhodopsin, are sensitive to dim light, give no colour and low acuity because many converge on one bipolar neurone. Cones contain three kinds of iodopsin, need bright light, give colour vision and high acuity, especially in the fovea."),
        PQ("Explain how the cochlea detects pitch and loudness.",
           "Different frequencies cause different parts of the basilar membrane to vibrate, so different hair cells and neurones fire: this codes pitch. A louder sound makes larger vibrations, bending more hair cells and producing more frequent impulses: this codes loudness."),
        TIP("Sensory receptors are tested in Paper 1 (labelled diagram of the retina or ear) and in Paper 2 (rod photochemistry or the organ of Corti). Practical Paper 3 may ask about dissection of an ox or goat eye."),
        SUM("Receptors are transducers: a stimulus produces a graded generator potential, which can cause action potentials.",
            "Rods contain rhodopsin and are sensitive but low in acuity; cones give colour and high acuity.",
            "Light bleaches rhodopsin, closes Na⁺ channels and hyperpolarises the rod. Vitamin A is needed for retinal.",
            "In the organ of Corti, vibrations bend the stereocilia of hair cells; position codes pitch, amplitude codes loudness."),
    ],
))

# ------------------------------------------------------------------ 19. Hypothalamus and pituitary
LESSONS.append(lesson(
    module=M3,
    topic="The hypothalamus and pituitary",
    title="The hypothalamus and pituitary: linking nerves and hormones",
    slug="biu1-hypothalamus-pituitary",
    minutes=22,
    summary="How the hypothalamus controls the posterior pituitary through neurosecretory cells and the anterior pituitary through releasing hormones in the portal vessels, and how negative feedback regulates the thyroid axis.",
    objectives=[
        "Compare nervous and endocrine coordination",
        "Describe how the hypothalamus controls the posterior pituitary (ADH and oxytocin)",
        "Describe how releasing and inhibiting hormones control the anterior pituitary through the hypophyseal portal vessels",
        "Explain the thyroid axis as a negative feedback loop and interpret hormone data",
    ],
    key_concepts=["Hypothalamus", "Neurosecretory cell", "Posterior pituitary", "Anterior pituitary", "Releasing hormone", "Hypophyseal portal vessels", "TSH", "Thyroxine", "Negative feedback"],
    blocks=[
        H("Introduction"),
        T("The nervous system and the endocrine system are two communication systems. The brain region that joins them is the **hypothalamus**. It lies beneath the thalamus, "
          "and below it hangs the **pituitary gland** (about the size of a pea), joined by a short stalk. The Board's 2023 report found that many candidates could not explain this link, "
          "so it is worth learning carefully."),
        CODE("""Feature            Nervous system                  Endocrine system
Signal             Electrical impulses and         Hormones in the blood
                   neurotransmitters
Speed              Very fast (milliseconds)        Slower (seconds to hours)
Duration           Short                           Longer lasting
Target             Specific muscle or gland        Any cell with the right receptor
Pathway            Neurones                        Bloodstream""", "text", title="Nervous and endocrine coordination"),
        H("The two parts of the pituitary"),
        KEY("Different origin, different control", "The two lobes are controlled in different ways.", cards=[
            ["Posterior pituitary (neurohypophysis)", "Nervous tissue. Contains the axon endings of neurosecretory cells whose cell bodies are in the hypothalamus. Stores and releases ADH and oxytocin."],
            ["Anterior pituitary (adenohypophysis)", "Glandular tissue. Makes its own hormones (TSH, ACTH, FSH, LH, growth hormone, prolactin) under the control of releasing and inhibiting hormones from the hypothalamus."],
        ]),
        H("Control of the posterior pituitary"),
        T("**Neurosecretory cells** are neurones that make hormones. In the hypothalamus their cell bodies make **ADH** and **oxytocin**. The hormones are packaged in vesicles, travel down the axons to the posterior pituitary and are stored in the axon endings. "
          "When impulses arrive (for example when the osmoreceptors detect low water potential), the vesicles release the hormone into nearby capillaries by exocytosis."),
        CODE("""Hormone     Made in               Released by            Main effect
ADH         Hypothalamus          Posterior pituitary    More water reabsorbed in the collecting duct
Oxytocin    Hypothalamus          Posterior pituitary    Uterus contracts in labour; milk ejection""", "text", title="Posterior pituitary hormones"),
        H("Control of the anterior pituitary"),
        T("Other neurosecretory cells in the hypothalamus make **releasing hormones** and **inhibiting hormones** (such as TRH, thyrotropin-releasing hormone). They release them from their axon endings into a network of capillaries at the base of the hypothalamus. "
          "These capillaries join to form the **hypophyseal portal vessels**, which carry the hormones directly to a second set of capillaries in the anterior pituitary. There, the hormones stimulate or inhibit the release of anterior pituitary hormones. "
          "The anterior pituitary hormones then enter the general blood circulation."),
        T("Many anterior pituitary hormones are **tropic hormones**: they act on another endocrine gland. For example TSH acts on the thyroid, ACTH on the adrenal cortex, FSH and LH on the ovaries and testes. Growth hormone and prolactin act directly on tissues."),
        H("An example of negative feedback: the thyroid axis"),
        T("Low body temperature or low thyroxine leads the hypothalamus to release **TRH**. TRH, through the portal vessels, stimulates the anterior pituitary to release **TSH**. TSH stimulates the thyroid gland to make and release **thyroxine** (which contains iodine). "
          "Thyroxine raises the basal metabolic rate. High thyroxine in the blood **inhibits** the release of TRH and TSH, so the system is stable. This is **negative feedback** at two levels."),
        T("Iodine deficiency prevents the making of thyroxine, so the negative feedback is lost, TSH remains high and the thyroid gland enlarges to form a **goitre**. Iodised salt prevents this disease in many regions, including mountain areas where soil iodine is low."),
        H("Worked examples"),
        EX("Worked example 1: interpreting hormone data", intro="Three patients have blood tests: Patient A has low thyroxine and high TSH. Patient B has low thyroxine and low TSH. Patient C has high thyroxine and low TSH. For each, say where the problem is likely to be.", steps=[
            S("Patient A", text="Low thyroxine with high TSH: the pituitary is responding properly (no feedback inhibition), so the fault is in the thyroid gland, or iodine is lacking."),
            S("Patient B", text="Low thyroxine with low TSH: the thyroid is not being stimulated, so the fault is in the pituitary or hypothalamus."),
            S("Patient C", text="High thyroxine and low TSH: the thyroxine is inhibiting TSH normally, so the thyroid is overactive or thyroxine is being taken as a drug."),
        ]),
        EX("Worked example 2: why do ADH and oxytocin not need a portal system?", intro="Explain.", steps=[
            S("Where they are made", text="The hormones are made in the cell bodies in the hypothalamus."),
            S("Transport", text="They travel inside the axons to the posterior pituitary, where the axon endings lie beside blood capillaries."),
            S("Conclusion", text="Because they are carried in axons, no portal vessels are needed. The anterior pituitary has no nerve link, so it needs the portal vessels."),
        ]),
        EX("Worked example 3: one hormone at a time", intro="Describe how the hypothalamus controls the release of TSH.", steps=[
            S("Step 1", text="Neurosecretory cells release TRH into capillaries at the base of the hypothalamus."),
            S("Step 2", text="Portal vessels carry TRH to the anterior pituitary."),
            S("Step 3", text="TRH stimulates anterior pituitary cells to release TSH into the blood."),
            S("Step 4", text="Thyroxine from the thyroid inhibits the release of TRH and TSH (negative feedback)."),
        ]),
        MISTAKE("Saying that the hypothalamus secretes hormones that are stored in the anterior pituitary", "The posterior pituitary stores ADH and oxytocin. The anterior pituitary makes its own hormones; the hypothalamus controls it with releasing and inhibiting hormones."),
        MISTAKE("Saying the pituitary is the 'master gland' that no other organ controls", "The pituitary is controlled by the hypothalamus and by feedback from target glands such as the thyroid."),
        QUIZ("Which hormone is made in the hypothalamus and released from the posterior pituitary?",
             ["TSH", "ADH", "Growth hormone", "Thyroxine"], 1,
             "ADH is made in neurosecretory cells and stored in the posterior pituitary.",
             hint="It controls water reabsorption in the collecting duct.",
             feedback=["TSH is made by the anterior pituitary.", "", "Growth hormone is made by the anterior pituitary.", "Thyroxine is made by the thyroid gland."]),
        QUIZ("What is the role of the hypophyseal portal vessels?",
             ["Carry oxygen to the brain", "Carry releasing hormones from the hypothalamus to the anterior pituitary", "Carry urine to the bladder", "Carry ADH from the pituitary to the kidney"], 1,
             "They provide a direct, concentrated delivery of hypothalamic hormones to the anterior pituitary.",
             hint="Portal means 'a vein linking two capillary networks'.",
             feedback=["They are not part of oxygen supply.", "", "They are not part of the urinary system.", "ADH is carried by the general circulation."]),
        PQ("Explain how the hypothalamus controls the posterior pituitary.",
           "Neurosecretory cells in the hypothalamus make ADH and oxytocin, which travel down their axons to the posterior pituitary and are stored in the axon endings. When impulses arrive in response to a stimulus, the hormones are released into the blood by exocytosis."),
        PQ("Explain how the hypothalamus controls the anterior pituitary.",
           "Neurosecretory cells release releasing and inhibiting hormones into capillaries at the base of the hypothalamus. The hypophyseal portal vessels carry them to the anterior pituitary, where they stimulate or inhibit the secretion of its hormones, such as TSH."),
        PQ("Describe how the level of thyroxine in the blood is controlled by negative feedback.",
           "Low thyroxine causes the hypothalamus to release TRH, which stimulates the anterior pituitary to release TSH. TSH stimulates the thyroid to release thyroxine. When thyroxine rises it inhibits the release of TRH and TSH, which reduces thyroxine production. The level therefore stays near the set point."),
        PQ("A person with a goitre has high TSH and low thyroxine. Explain this result.",
           "A lack of iodine means that the thyroid cannot make thyroxine. With low thyroxine there is no negative feedback, so the pituitary keeps secreting TSH. TSH stimulates the thyroid cells to grow, so the gland enlarges, forming a goitre."),
        TIP("Link the hypothalamus and pituitary to negative feedback, as the Board's report suggests. Use the exact words: neurosecretory cell, releasing hormone, portal vessels, tropic hormone."),
        SUM("The hypothalamus joins the nervous and endocrine systems.",
            "Neurosecretory cells make ADH and oxytocin, which are released from the posterior pituitary.",
            "Releasing hormones reach the anterior pituitary by portal vessels and control TSH, ACTH, FSH, LH, GH and prolactin.",
            "Thyroxine feeds back negatively on the hypothalamus and pituitary; iodine lack causes goitre."),
    ],
))

# ------------------------------------------------------------------ 20. Muscle and sliding filaments
LESSONS.append(lesson(
    module=M3,
    topic="Muscle structure and the sliding-filament theory",
    title="Striated muscle and the sliding-filament theory",
    slug="biu1-sliding-filament-muscle",
    minutes=24,
    summary="The ultrastructure of skeletal muscle, the bands of a sarcomere, how calcium, troponin and tropomyosin control cross-bridge cycling by actin and myosin, and how sarcomere calculations work.",
    objectives=[
        "Describe the structure of a muscle fibre and of a sarcomere, naming the bands",
        "Explain what happens to the bands (A, I, H) during contraction",
        "Describe the sliding-filament mechanism, including the roles of Ca²⁺, troponin, tropomyosin, myosin heads and ATP",
        "Calculate sarcomere changes and the shortening of a whole muscle",
    ],
    key_concepts=["Myofibril", "Sarcomere", "Actin", "Myosin", "Z line", "A band", "I band", "H zone", "Troponin", "Tropomyosin", "Sarcoplasmic reticulum", "Cross-bridge"],
    blocks=[
        H("Introduction"),
        T("A cyclist in the Tour du Cameroun and a bird in flight use the same machinery: **striated (skeletal) muscle**. It is called striated because under the microscope it shows cross-stripes. "
          "A muscle is made of long cells called **muscle fibres**; each fibre contains hundreds of thread-like **myofibrils**, and each myofibril is divided along its length into repeating units called **sarcomeres**."),
        D("A **sarcomere** is the contractile unit of striated muscle: the part of a myofibril between two Z lines. In relaxed human muscle it is about 2.2 µm long.",
          title="Definition: sarcomere"),
        IMG("al-biu1-sarcomere.svg", alt="A relaxed sarcomere: Z lines at each end, thin actin filaments attached to the Z lines, thick myosin filaments in the centre, with the I band, A band, H zone and M line marked.",
            caption="Figure 1. A relaxed sarcomere (diagram)."),
        H("Structure of a sarcomere"),
        KEY("Filaments and bands", "The bands are seen because of the arrangement of the two kinds of filament.", cards=[
            ["Thin filaments", "Actin, with the regulatory proteins tropomyosin and troponin. Attached to the Z lines."],
            ["Thick filaments", "Myosin, whose heads stick out in a spiral. Held in the centre at the M line."],
            ["A band", "The dark band; the full length of the myosin filaments (it includes the overlap with actin). Its length does not change."],
            ["I band", "The light band; actin only. It is shorter in contraction."],
            ["H zone", "The middle part of the A band with myosin only. It is shorter or disappears in contraction."],
            ["Z line", "The boundary of the sarcomere. Z lines move closer together in contraction."],
        ]),
        T("Around each myofibril lies the **sarcoplasmic reticulum**, a modified endoplasmic reticulum that stores Ca²⁺. **T-tubules** are inward extensions of the cell surface membrane (the sarcolemma) that carry the action potential deep into the fibre. "
          "Muscle fibres contain very many mitochondria beside the myofibrils."),
        H("The sliding-filament theory"),
        D("The **sliding-filament theory** states that muscle shortens because the thin actin filaments slide over the thick myosin filaments towards the centre of the sarcomere. The filaments themselves do not change length.",
          title="Sliding-filament theory"),
        T("**1 Excitation.** An action potential arrives at the **neuromuscular junction**, ACh is released and depolarises the sarcolemma. The action potential spreads along the T-tubules."),
        T("**2 Calcium release.** The action potential opens Ca²⁺ channels in the sarcoplasmic reticulum. Ca²⁺ flood into the cytoplasm around the filaments."),
        T("**3 Unblocking.** Ca²⁺ bind to **troponin**, changing its shape and pulling **tropomyosin** away from the myosin-binding sites on actin."),
        T("**4 Cross-bridge formation.** A myosin head, carrying ADP and Pi, binds to actin and forms a **cross-bridge**."),
        T("**5 Power stroke.** The head tilts, pulling the actin filament towards the centre of the sarcomere; ADP and Pi are released."),
        T("**6 Detachment.** A new ATP binds to the myosin head, which detaches from actin. ATP is then hydrolysed by the myosin head (ATPase), recocking the head for the next cycle."),
        T("The cycle repeats many times while Ca²⁺ is present and ATP is available. **Relaxation**: the nerve impulses stop, Ca²⁺ are pumped back into the sarcoplasmic reticulum by active transport, tropomyosin covers the binding sites, and the muscle relaxes."),
        T("After death ATP is no longer made. Myosin heads cannot detach from actin, so the muscles become stiff (**rigor mortis**)."),
        H("Energy for contraction"),
        T("Muscles store little ATP (enough for a few seconds). More is made from **creatine phosphate** (a quick reserve that gives its phosphate to ADP), then by aerobic respiration (slow, long-lasting) and by lactate fermentation (fast, short-lasting)."),
        CODE("""Feature              Slow-twitch (type I) fibre         Fast-twitch (type II) fibre
Speed of contraction Slow                               Fast
Fatigue              Slow to tire                       Tire quickly
Main ATP source      Aerobic respiration                Glycolysis (anaerobic)
Mitochondria, myoglobin  Many, much (red)               Fewer, little (pale)
Used in              Posture, marathon running          Sprinting, lifting""", "text", title="Two types of fibre"),
        H("Worked examples"),
        EX("Worked example 1: the bands", intro="A relaxed sarcomere is 2.2 µm long, the myosin filament is 1.6 µm long and each actin filament is 1.0 µm long (teaching values). Calculate the length of the A band, the I band (both halves together) and the H zone.", steps=[
            S("A band", math=r"\text{A band} = \text{myosin length} = 1.6 \ \mu\text{m}"),
            S("I band", math=r"\text{I band} = 2.2 - 1.6 = 0.6 \ \mu\text{m}"),
            S("H zone", math=r"\text{H zone} = 2.2 - 2(1.0) = 0.2 \ \mu\text{m}"),
        ]),
        EX("Worked example 2: during contraction", intro="The sarcomere shortens to 1.8 µm. Find the A band, I band and H zone, and the percentage shortening.", steps=[
            S("A band", text="Unchanged at 1.6 µm."),
            S("I band", math=r"1.8 - 1.6 = 0.2 \ \mu\text{m}"),
            S("H zone", math=r"\text{actin overlaps in the middle, so } 1.8 - 2.0 < 0 \text{ and the H zone has disappeared (0)}"),
            S("Percentage shortening", math=r"\frac{2.2 - 1.8}{2.2} \times 100 = 18\%"),
        ]),
        EX("Worked example 3: shortening of a whole muscle", intro="A muscle fibre 20 cm long is made of sarcomeres in series, each 2.2 µm long. If every sarcomere shortens to 1.8 µm, how long does the fibre become?", steps=[
            S("Length in µm", math=r"20 \text{ cm} = 200\,000 \ \mu\text{m}"),
            S("Number of sarcomeres", math=r"\frac{200\,000}{2.2} = 90\,909"),
            S("New length", math=r"90\,909 \times 1.8 = 163\,636 \ \mu\text{m} = 16.4 \text{ cm}"),
            S("Shortening", math=r"20 - 16.4 = 3.6 \text{ cm}"),
        ]),
        MISTAKE("Saying that the filaments shorten", "The filaments do not change length. They slide. The A band stays the same; the I band and H zone get shorter."),
        MISTAKE("Saying ATP is needed to join myosin to actin", "ATP is needed to detach the myosin head from actin (and to re-set it). The head binds after ATP has been hydrolysed and Ca²⁺ has exposed the site."),
        QUIZ("Which band does NOT change in length when a muscle contracts?",
             ["I band", "H zone", "A band", "Distance between Z lines"], 2,
             "The A band is the length of the myosin filaments, which do not shorten.",
             hint="It is the dark band.",
             feedback=["The I band gets shorter.", "The H zone gets shorter and may disappear.", "", "The Z lines move closer together."]),
        QUIZ("What is the role of Ca²⁺ in muscle contraction?",
             ["They bind to troponin and move tropomyosin off the myosin-binding sites", "They provide energy directly", "They break down ATP", "They bind to myosin and release actin"], 0,
             "Ca²⁺ binding to troponin uncovers the binding sites on actin.",
             hint="They are released from the sarcoplasmic reticulum.",
             feedback=["", "ATP provides energy.", "Myosin ATPase breaks ATP down.", "Detachment needs ATP."]),
        PQ("Describe the structure of a sarcomere.",
           "A sarcomere lies between two Z lines. Thin actin filaments are attached to the Z lines. Thick myosin filaments lie in the centre. The dark A band is the length of the myosin; the lighter I band contains only actin; the H zone is the central part of the A band with only myosin; the M line is in the middle."),
        PQ("Explain what happens to the I band, A band and H zone during contraction, and why.",
           "The I band and H zone get shorter and the A band stays the same. The actin filaments slide towards the centre between the myosin filaments, so the overlap increases, while the filaments themselves do not shorten."),
        PQ("Describe the roles of calcium ions, ATP, troponin and tropomyosin in the sliding-filament mechanism.",
           "An action potential makes the sarcoplasmic reticulum release Ca²⁺. Ca²⁺ bind to troponin, which moves tropomyosin away from the binding sites on actin. Myosin heads with ADP and Pi bind to actin and tilt, pulling the actin. New ATP binds, detaching the head, and its hydrolysis re-sets it for the next cycle."),
        PQ("A sarcomere is 2.4 µm long when relaxed and 2.0 µm when contracted. Calculate the percentage shortening. A muscle contains 50 000 sarcomeres in series: find its length relaxed and contracted.",
           "Shortening = 0.4 / 2.4 × 100 = 16.7 percent. Relaxed: 50 000 × 2.4 = 120 000 µm = 12 cm. Contracted: 50 000 × 2.0 = 100 000 µm = 10 cm."),
        TIP("Candidates should draw the sarcomere with labels and a second diagram for the contracted state. Sarcomere calculations and electron micrograph interpretation appear in Paper 1 and Paper 2."),
        SUM("A sarcomere has actin filaments attached to the Z lines and myosin filaments in the middle; the A band does not change length.",
            "In contraction the I band and H zone shorten as actin slides over myosin.",
            "Ca²⁺ from the sarcoplasmic reticulum bind troponin, move tropomyosin and allow cross-bridges; ATP detaches the heads and re-sets them.",
            "Energy comes from ATP, creatine phosphate, aerobic respiration and lactate fermentation."),
    ],
))
