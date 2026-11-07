"""A Level Biology (0710), Lower Sixth, modules 1-3: Cytology & Membrane Physiology, Biological Molecules &
Enzymology, Nucleic Acids / Protein Synthesis & Cell Division. 17 lessons, one practice set each (see the practice
file of the same name).

Scope notes: the blueprint lists ideas, not a Board syllabus. Facts are the standard A Level ones. Where textbooks differ
the lesson says "check your textbook". All numbers in worked data are teaching data and are labelled.
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "lower-sixth")

M1 = "Cytology & Membrane Physiology"
M2 = "Biological Molecules & Enzymology"
M3 = "Nucleic Acids, Protein Synthesis & Cell Division"

LESSONS = []

# ------------------------------------------------------------------ 1. Eukaryotic ultrastructure
LESSONS.append(lesson(
    module=M1,
    topic="Prokaryotic and eukaryotic cells",
    title="Eukaryotic cell ultrastructure and the work of organelles",
    slug="bil1-eukaryotic-ultrastructure",
    minutes=22,
    summary="The electron microscope shows the ultrastructure of eukaryotic cells. Learn each organelle's structure and function, and how they cooperate to make, modify and export a protein.",
    objectives=[
        "Describe the structure and function of the nucleus, ER, Golgi apparatus, mitochondria, lysosomes and ribosomes",
        "Explain how organelles work together to make and export a protein",
        "Link the organelles in a cell to its function (for example a secretory cell and a muscle cell)",
        "Identify the organelles on an electron micrograph drawing",
    ],
    key_concepts=["Ultrastructure", "Nucleus", "Rough endoplasmic reticulum", "Golgi apparatus", "Mitochondrion", "Lysosome", "80S ribosome"],
    blocks=[
        H("Introduction"),
        T("A cell in the pancreas of a person in Yaounde makes insulin. A muscle cell in a footballer's leg in Douala burns "
          "glucose to release energy. Both are eukaryotic cells, but they look different inside. The difference is the "
          "number of each organelle, and it reflects the job of the cell."),
        D("**Ultrastructure** is the fine detail of a cell seen with an electron microscope. A **eukaryotic cell** has its DNA "
          "inside a nucleus and has membrane-bound organelles. Animals, plants, fungi and protoctists are made of eukaryotic cells.",
          title="Definitions"),
        IMG("al-bil1-euk-cell.svg", alt="Diagram of an animal cell showing nucleus, nucleolus, ribosomes, rough ER, mitochondria, lysosome, Golgi apparatus and cell membrane",
            caption="Figure 1. An animal cell (drawing, not to scale)."),
        H("The organelles"),
        KEY("Structure and function", "Learn each structure with its job.", cards=[
            ["Nucleus", "Surrounded by a double membrane (the nuclear envelope) with nuclear pores. Contains chromatin (DNA with histone proteins) and the nucleolus, which makes ribosomal RNA and assembles ribosomes. It controls the cell by storing genes and making mRNA."],
            ["Rough ER", "Flattened sacs (cisternae) with 80S ribosomes on the outside. Proteins made on these ribosomes enter the sacs, are folded and are carried in vesicles."],
            ["Smooth ER", "Tubes with no ribosomes. It makes lipids and steroids and, in liver cells, helps to detoxify drugs."],
            ["Golgi apparatus", "A stack of flattened sacs. It modifies proteins (for example by adding sugars), sorts and packages them into vesicles for secretion, and makes lysosomes."],
            ["Mitochondrion", "Double membrane. The inner membrane is folded into cristae and surrounds the matrix. Site of aerobic respiration, making ATP. It has its own circular DNA and 70S ribosomes."],
            ["Lysosome", "A membrane-bound sac of hydrolytic (digestive) enzymes. It digests worn-out organelles and material taken in by phagocytosis."],
            ["Ribosome", "Eukaryotic ribosomes are 80S, made of ribosomal RNA and protein, with no membrane. They make proteins. Free ribosomes make proteins for use inside the cell. Ribosomes on the rough ER make proteins for export or for membranes."],
        ]),
        T("Plant cells also have a cell wall of cellulose, chloroplasts and a large permanent vacuole surrounded by a membrane called the "
          "**tonoplast**. Animal cells have centrioles, which organize the spindle in cell division. Many textbooks say that higher plant cells "
          "have no centrioles. Check your textbook."),
        H("Organelles working together"),
        KEY("From gene to secreted protein", "Follow an enzyme made for export.", cards=[
            ["1", "The gene in the nucleus is transcribed to mRNA. The mRNA leaves through a nuclear pore."],
            ["2", "A ribosome on the rough ER translates the mRNA. The polypeptide enters the ER sac."],
            ["3", "A transport vesicle buds off the ER and carries the protein to the Golgi apparatus."],
            ["4", "The Golgi modifies the protein and packages it in a secretory vesicle."],
            ["5", "The vesicle moves to the cell surface membrane and fuses with it. The protein is released by exocytosis. Mitochondria supply the ATP."],
        ]),
        EX("Worked example 1: linking structure to function", intro="Electron micrographs show that cell P has a huge amount of rough ER and many Golgi stacks, while cell Q has very many mitochondria with densely packed cristae. Suggest what each cell does.", steps=[
            S("Cell P", text="Rough ER and Golgi are used for making and exporting proteins. P is likely a secretory cell, for example an enzyme-secreting cell of the pancreas."),
            S("Cell Q", text="Mitochondria make ATP. Dense cristae give a large inner membrane area for the enzymes of ATP production. Q needs a lot of energy, for example a muscle cell or a sperm tail cell."),
            S("Conclude", text="The number of organelles reflects the work the cell does."),
        ]),
        EX("Worked example 2: tracing a protein", intro="Radioactive amino acids are given to a cell for a short time. State, in order, the structures that become radioactive.", steps=[
            S("Where proteins are made", text="Ribosomes on the rough ER make the polypeptide, so the rough ER is labelled first."),
            S("Where they go next", text="Transport vesicles carry the protein to the Golgi apparatus."),
            S("The exit", text="Secretory vesicles carry it to the cell surface membrane, where it is released."),
            S("Answer", text="Rough ER, then vesicles, then Golgi apparatus, then secretory vesicles, then the cell surface membrane."),
        ]),
        MISTAKE("Saying the nucleus makes proteins", "The nucleus stores the genes and makes mRNA. Ribosomes make proteins. The nucleolus makes ribosomal RNA."),
        MISTAKE("Saying mitochondria 'make energy'", "Energy cannot be made. Mitochondria release energy from food molecules and use it to make ATP."),
        QUIZ("Which structure modifies proteins and packages them into vesicles?",
             ["Smooth ER", "Golgi apparatus", "Lysosome", "Nucleolus"], 1,
             "The Golgi apparatus modifies, sorts and packages proteins.",
             hint="Think of the 'post office' of the cell.",
             feedback=["Smooth ER makes lipids and steroids.", "", "Lysosomes digest materials. They are made by the Golgi but do not package other proteins.", "The nucleolus makes ribosomal RNA."]),
        QUIZ("A cell has been treated with a drug that stops ribosomes attaching to the ER. Which product is most affected?",
             ["Proteins for export", "Lipids", "DNA replication", "ATP production in mitochondria"], 0,
             "Ribosomes on the rough ER make the proteins that are exported or put into membranes.",
             hint="Which proteins are made on the rough ER?",
             feedback=["", "Lipids are made on the smooth ER.", "DNA replication happens in the nucleus and needs no ribosomes on the ER.", "Mitochondria make ATP with their own enzymes and ribosomes."]),
        H("Practice"),
        PQ("State two differences between rough and smooth endoplasmic reticulum.", "Rough ER has ribosomes on its surface and smooth ER has none. Rough ER makes and transports proteins, while smooth ER makes lipids and steroids and detoxifies drugs."),
        PQ("Describe the structure of a mitochondrion and explain how its structure suits its function.", "It has an outer membrane and an inner membrane folded into cristae, enclosing the matrix. The cristae give a large surface area for the electron transport chain and ATP synthase. The matrix contains enzymes of the Krebs cycle. It also has circular DNA and 70S ribosomes so it can make some of its own proteins."),
        PQ("An enzyme made in a pancreatic cell is secreted. Name the organelles it passes through, in order, from synthesis to release.", "Rough ER (synthesis and folding), transport vesicle, Golgi apparatus (modification and packaging), secretory vesicle, cell surface membrane (exocytosis)."),
        TIP("Exam link: cell structure is tested in Paper 1 (matching an organelle with a function, or reading a labelled drawing), in Paper 2 (drawing and describing organelles, and linking structure to function) and in the practical paper (drawing from slides and micrographs). Always say what the structure *does*, not only what it is."),
        SUM("Eukaryotic cells have a nucleus and membrane-bound organelles. Their ribosomes are 80S.",
            "The nucleus holds DNA and makes mRNA. The rough ER and Golgi make, modify and package proteins. Smooth ER makes lipids.",
            "Mitochondria carry out aerobic respiration and make ATP. Lysosomes digest.",
            "The organelles cooperate: nucleus, rough ER, vesicles, Golgi, vesicles, cell surface membrane.",
            "The organelles present reflect the cell's job."),
    ],
))

# ------------------------------------------------------------------ 2. Prokaryotes and magnification
LESSONS.append(lesson(
    module=M1,
    topic="Prokaryotic and eukaryotic cells",
    title="Prokaryotes compared with eukaryotes, magnification and resolution",
    slug="bil1-prokaryotes-and-magnification",
    minutes=22,
    summary="Prokaryotic cells have no nucleus or membrane-bound organelles and have 70S ribosomes. Compare them with eukaryotes, and calculate magnification and actual size from drawings and micrographs.",
    objectives=[
        "Describe the structure of a bacterial cell and compare it with a eukaryotic cell",
        "Outline the endosymbiont idea for mitochondria and chloroplasts",
        "Calculate magnification and actual size, with correct units",
        "Distinguish magnification from resolution and compare light and electron microscopes",
    ],
    key_concepts=["Prokaryote", "Nucleoid", "Plasmid", "70S ribosome", "Magnification", "Resolution", "Scale bar"],
    blocks=[
        H("Introduction"),
        T("Bacteria live on the skin of your hand, in the soil of a cocoa farm and in the gut of a goat. A single bacterium is tiny: "
          "hundreds of them side by side would barely cover the width of a pencil line. To study such cells we need two ideas: how a prokaryotic "
          "cell is built, and how to measure what we see under a microscope."),
        D("A **prokaryotic cell** has no nucleus. Its DNA is a circular molecule lying free in a region of the cytoplasm called the "
          "**nucleoid**. It has no membrane-bound organelles and its ribosomes are 70S.", title="Definition"),
        IMG("al-bil1-prok-cell.svg", alt="Bacterial cell with capsule, cell wall, cell membrane, circular DNA, plasmid, ribosomes and flagellum",
            caption="Figure 1. A bacterial cell (drawing, not to scale)."),
        H("Comparing prokaryotes and eukaryotes"),
        CODE("""Feature        Prokaryote (bacterium)          Eukaryote (animal or plant)
DNA            circular, in a nucleoid,        linear, with histones, inside
               no histones (naked)             a nuclear envelope
Ribosomes      70S                             80S in the cytoplasm
                                               (70S in mitochondria)
Organelles     none with membranes             mitochondria, ER, Golgi, etc.
Cell wall      peptidoglycan (murein)          cellulose (plants), chitin
                                               (fungi), none in animals
Typical size   0.5 to 5 micrometres            10 to 100 micrometres
Division       binary fission                  mitosis""", "text", title="Table 1. Prokaryote and eukaryote compared"),
        T("Many bacteria also have a slime **capsule**, flagella for swimming and small circular DNA molecules called **plasmids**. "
          "Plasmids often carry genes for antibiotic resistance."),
        KEY("The endosymbiont idea", "Mitochondria and chloroplasts look like small prokaryotes.", cards=[
            ["Evidence", "They have circular DNA, 70S ribosomes and a double membrane. They divide by a process like binary fission and are about the size of bacteria."],
            ["Idea", "They may have come from prokaryotes that were taken into an early eukaryotic cell and stayed there as partners. This is a widely accepted theory, not an observation."],
        ]),
        H("Magnification, resolution and measuring"),
        D("**Magnification** is how many times larger an image is than the real object. **Resolution** is the smallest distance between two points that can still be seen as separate.",
          title="Two different ideas", formula=r"\text{magnification} = \frac{\text{size of image}}{\text{actual size}}"),
        T("A light microscope can resolve about 0.2 micrometres (200 nm). An electron beam has a much shorter wavelength, so a transmission electron microscope "
          "resolves far smaller details (about 0.5 nm or better; check your textbook for exact values). Raising the magnification does not improve "
          "resolution. Beyond the limit, a larger image is just a larger blur."),
        TIP("Convert all lengths to the same unit before dividing. 1 mm = 1000 micrometres (µm). 1 µm = 1000 nm. Magnification has no unit."),
        EX("Worked example 1: magnification", intro="A mitochondrion in an electron micrograph is 42 mm long. Its actual length is 1.5 µm. Calculate the magnification.", steps=[
            S("Convert to the same unit", math=r"42\ \text{mm} = 42\,000\ \mu\text{m}"),
            S("Apply the formula", math=r"\text{magnification} = \frac{42\,000}{1.5} = 28\,000"),
            S("State the answer", text="The magnification is ×28 000. It has no unit."),
        ]),
        EX("Worked example 2: using a scale bar", intro="A micrograph shows a scale bar 25 mm long labelled 5 µm. A nucleus measures 40 mm across. Find the actual diameter of the nucleus.", steps=[
            S("Find the magnification from the bar", math=r"\frac{25\ \text{mm}}{5\ \mu\text{m}} = \frac{25\,000\ \mu\text{m}}{5\ \mu\text{m}} = 5000"),
            S("Rearrange for actual size", math=r"\text{actual size} = \frac{\text{image size}}{\text{magnification}} = \frac{40\,000\ \mu\text{m}}{5000}"),
            S("Calculate", math=r"= 8\ \mu\text{m}"),
        ], check=r"8 \times 5000 = 40\,000\ \mu\text{m} = 40\ \text{mm}"),
        MISTAKE("Mixing units", "Dividing 42 mm by 1.5 µm gives 28, not 28 000. Always convert first."),
        MISTAKE("Confusing magnification with resolution", "A bigger image is not a clearer image. Only a shorter wavelength of the radiation (electrons) gives better resolution."),
        QUIZ("Which feature is found in a bacterial cell but NOT in an animal cell?",
             ["Ribosomes", "A cell surface membrane", "A cell wall containing peptidoglycan", "DNA"], 2,
             "Peptidoglycan (murein) cell walls are characteristic of bacteria.",
             hint="Animal cells have no cell wall at all.",
             feedback=["Both have ribosomes.", "All cells have a cell surface membrane.", "", "All cells contain DNA."]),
        QUIZ("A drawing of a cell is 60 mm long. The magnification is ×1500. What is the actual length?",
             ["0.04 µm", "40 µm", "90 µm", "4 µm"], 1,
             "Actual size = 60 mm ÷ 1500 = 0.04 mm = 40 µm.",
             hint="Rearrange: actual = image ÷ magnification, then convert mm to µm.",
             feedback=["The result in mm is 0.04, which is 40 µm, not 0.04 µm.", "", "This multiplies 60 by 1500 and does not convert units.", "A factor of 10 is lost when converting mm to µm."]),
        H("Practice"),
        PQ("State three structural differences between a prokaryotic and a eukaryotic cell.", "Prokaryotes have no nucleus (DNA is a naked circular loop in the nucleoid), have 70S ribosomes and no membrane-bound organelles, and have peptidoglycan walls. Eukaryotes have a nucleus with linear DNA and histones, 80S ribosomes and membrane-bound organelles."),
        PQ("A bacterium is 2 µm long. Calculate its length in a micrograph at magnification ×10 000, in mm.", "2 µm × 10 000 = 20 000 µm = 20 mm."),
        PQ("Explain why an electron microscope shows more detail than a light microscope.", "Electrons have a much shorter wavelength than light, so the electron microscope has a much higher resolution. It can show two points that are very close together as separate."),
        TIP("Exam link: magnification calculations appear in Paper 1 and Paper 2, and the practical paper asks for scaled drawings and measurements. Show the formula and the unit conversion. The Board's reports note that candidates lose marks for poor calculations."),
        SUM("Prokaryotes have a naked circular DNA in a nucleoid, 70S ribosomes, no membrane-bound organelles and a peptidoglycan wall.",
            "Mitochondria and chloroplasts resemble bacteria, which supports the endosymbiont theory.",
            "Magnification = image size ÷ actual size. Convert to the same unit first.",
            "Resolution is the ability to see two close points as separate. Electron microscopes have higher resolution."),
    ],
))

# ------------------------------------------------------------------ 3. Fluid-mosaic model
LESSONS.append(lesson(
    module=M1,
    topic="The fluid-mosaic model",
    title="The fluid-mosaic model of membrane structure",
    slug="bil1-fluid-mosaic-model",
    minutes=22,
    summary="Cell membranes are a fluid bilayer of phospholipids with a mosaic of proteins, cholesterol and carbohydrate chains. Learn the parts, what each does, what affects fluidity and permeability, and the evidence.",
    objectives=[
        "Describe the fluid-mosaic model and explain why phospholipids form a bilayer",
        "State the roles of integral and peripheral proteins, cholesterol, glycoproteins and glycolipids",
        "Explain how temperature, unsaturated fatty acids and cholesterol affect fluidity",
        "Explain why some substances cross the bilayer easily and others need proteins",
    ],
    key_concepts=["Phospholipid bilayer", "Amphipathic", "Integral protein", "Peripheral protein", "Cholesterol", "Glycoprotein", "Fluidity", "Partially permeable"],
    blocks=[
        H("Introduction"),
        T("Every cell is wrapped in a membrane only about 7 nm thick, which is about ten thousand times thinner than a sheet of paper. "
          "Yet this thin layer keeps the cell contents in, lets food in and waste out, receives hormone signals and lets cells recognize one another. "
          "In 1972, Singer and Nicolson described a model that explains how it works: the **fluid-mosaic model**."),
        D("The **fluid-mosaic model** says that a membrane is a **fluid** bilayer of phospholipid molecules in which protein molecules are "
          "scattered like a **mosaic**. The molecules can move sideways, so the membrane is not rigid.", title="Definition"),
        IMG("al-bil1-membrane.svg", alt="Cell surface membrane: phospholipid bilayer with cholesterol, a channel protein, a glycoprotein, a glycolipid and a peripheral protein",
            caption="Figure 1. The fluid-mosaic model (drawing, not to scale)."),
        H("The parts of the membrane"),
        T("A **phospholipid** is **amphipathic**: it has a hydrophilic (water-loving) phosphate head and two hydrophobic (water-hating) fatty acid tails. "
          "In water the heads face the water on both sides and the tails hide in the middle, so a **bilayer** forms by itself."),
        KEY("Components and roles", "Know each one with its function.", cards=[
            ["Phospholipids", "Form the bilayer. The hydrophobic core stops ions and large polar molecules from crossing easily. Small non-polar molecules (oxygen, carbon dioxide) dissolve in the core and pass through."],
            ["Integral proteins", "Span the bilayer. Channel proteins and carrier proteins allow ions and polar molecules to cross. Others are enzymes or receptors for hormones."],
            ["Peripheral proteins", "Sit on one surface. They may anchor the cytoskeleton or act as enzymes."],
            ["Cholesterol", "Sits between phospholipid tails in animal membranes. It makes the membrane less fluid at high temperature, stops tails packing too tightly at low temperature and reduces leakage of ions."],
            ["Glycoproteins and glycolipids", "Carbohydrate chains on the outside. They act as receptors and as markers for cell recognition, and they help cells stick together."],
        ]),
        H("Fluidity and permeability"),
        T("Fatty acid tails that are **unsaturated** have double bonds, which put kinks in the tails. Kinks stop tails packing closely, so the membrane "
          "is more fluid. Higher temperature also makes the molecules move faster and the membrane more fluid. If the temperature is too high, "
          "proteins denature and the membrane becomes leaky."),
        D("A membrane is **partially permeable**. Small non-polar molecules cross freely. Water crosses slowly through the bilayer and faster through "
          "protein channels called aquaporins. Ions and large polar molecules such as glucose cannot cross the bilayer and need channel or carrier proteins.",
          title="Permeability"),
        T("Evidence for fluidity: if the membrane proteins of a mouse cell and a human cell are labelled with different fluorescent markers and the cells are "
          "fused, the two colours mix around the surface within about 40 minutes. The proteins can therefore move sideways (check your textbook for the details of this experiment)."),
        EX("Worked example 1: magnification of a membrane", intro="A membrane is 7 nm thick. In a micrograph it measures 2.1 mm across. Calculate the magnification.", steps=[
            S("Convert to the same unit", math=r"2.1\ \text{mm} = 2.1 \times 10^{6}\ \text{nm}"),
            S("Divide", math=r"\frac{2.1 \times 10^{6}}{7} = 300\,000"),
            S("Answer", text="The magnification is ×300 000."),
        ]),
        EX("Worked example 2: beetroot practical (teaching data)", intro="Discs of beetroot of equal size are kept for 10 minutes in water at different temperatures. The red pigment (betalain) that leaks out is measured as absorbance: 20 °C 0.05, 30 °C 0.06, 40 °C 0.09, 50 °C 0.30, 60 °C 0.72, 70 °C 0.85. Explain the results.", steps=[
            S("Describe", text="Below 40 °C there is very little leakage. Between 40 and 60 °C the leakage rises steeply and then levels off."),
            S("Explain the rise", text="High temperature denatures the membrane proteins and makes the phospholipids so fluid that gaps appear. The membrane becomes more permeable and the pigment leaks out of the vacuole."),
            S("Explain the levelling", text="By 70 °C nearly all membranes are damaged, so little pigment is left to leak."),
        ]),
        MISTAKE("Saying the membrane has 'pores' that let everything through", "Most of the bilayer is a barrier. Specific proteins let specific substances through. Say channel or carrier proteins."),
        MISTAKE("Saying cholesterol makes the membrane more fluid at all temperatures", "Cholesterol is a buffer: it reduces fluidity when warm and prevents solidifying when cool."),
        QUIZ("Why do the phospholipids in a membrane form a bilayer in water?",
             ["The tails are attracted to water", "The heads are hydrophilic and face the water, while the tails are hydrophobic and face each other", "The heads are hydrophobic", "The proteins hold them in a sheet"], 1,
             "Heads face water on both sides and tails hide from water in the middle.",
             hint="Which part of the molecule likes water?",
             feedback=["The tails are hydrophobic and avoid water.", "", "The heads are the hydrophilic part.", "The bilayer forms because of the molecules' properties, not because proteins hold them."]),
        QUIZ("Why does a membrane with more unsaturated fatty acids stay fluid at low temperature?",
             ["Double bonds make the tails straight", "Kinks in the tails prevent close packing", "Unsaturated tails are hydrophilic", "Double bonds make cholesterol unnecessary"], 1,
             "Double bonds put kinks in the tails, so the tails cannot pack tightly.",
             hint="What do double bonds do to the shape of a fatty acid?",
             feedback=["They bend the tails, not straighten them.", "", "All fatty acid tails are hydrophobic.", "Cholesterol is still found in animal membranes."]),
        H("Practice"),
        PQ("Explain why the model is called 'fluid mosaic'.", "Fluid: the phospholipids and many proteins can move sideways in the plane of the membrane. Mosaic: the proteins are scattered through the bilayer in a pattern like the pieces of a mosaic."),
        PQ("Explain why oxygen can diffuse through a membrane but sodium ions cannot.", "Oxygen is small and non-polar, so it dissolves in the hydrophobic core of the bilayer. Sodium ions are charged and are repelled by the hydrophobic tails, so they need channel or carrier proteins."),
        PQ("State two roles of glycoproteins in the cell surface membrane.", "They act as receptors for hormones and other signals, and as antigens (markers) for cell recognition. They can also help cells to attach to each other."),
        TIP("Exam link: membrane structure appears in Paper 1 (labelled diagrams and functions) and in Paper 2 (describing the model, fluidity and permeability). It is also linked to the practical paper through the beetroot membrane experiment. Name the part and state its function."),
        SUM("Membranes are fluid phospholipid bilayers with a mosaic of proteins (integral and peripheral).",
            "Cholesterol regulates fluidity and reduces leakage. Glycoproteins and glycolipids work in recognition and receptors.",
            "Unsaturated tails and higher temperature increase fluidity. Very high temperature denatures proteins and makes the membrane leaky.",
            "Small non-polar molecules diffuse through the bilayer. Ions and large polar molecules need channel or carrier proteins."),
    ],
))

# ------------------------------------------------------------------ 4. Water potential
LESSONS.append(lesson(
    module=M1,
    topic="Water potential",
    title="Water potential, solute potential and pressure potential",
    slug="bil1-water-potential",
    minutes=24,
    summary="Water potential measures the tendency of water to move. Use the equation water potential = solute potential + pressure potential to predict the direction of osmosis, to describe turgor and plasmolysis and to analyse potato-cylinder data.",
    objectives=[
        "Define water potential, solute potential and pressure potential and state their units and signs",
        "Use the equation water potential = solute potential + pressure potential in calculations",
        "Predict the direction of net water movement between cells and solutions",
        "Describe turgid, flaccid and plasmolysed cells and estimate the water potential of tissue from potato data",
    ],
    key_concepts=["Water potential", "Solute potential", "Pressure potential", "Osmosis", "Turgor", "Incipient plasmolysis", "Isotonic point"],
    blocks=[
        H("Introduction"),
        T("In the dry season a farmer near Ngaoundere waters a wilting tomato plant. Within an hour the leaves stand up again. Nothing has been added "
          "to the leaves, so what changed? Water entered the cells and pushed their contents against the cell wall. To explain this exactly, "
          "biologists use a quantity called **water potential**."),
        D("**Water potential** (symbol $\\Psi$, the Greek letter psi) is a measure of the tendency of water molecules to move from one place to another. "
          "It is measured in kilopascals (kPa). Pure water at standard pressure has the **highest** water potential, which is defined as **zero**. "
          "All solutions have a water potential below zero (negative).", title="Definition"),
        D("**Osmosis** is the net movement of water molecules from a region of higher (less negative) water potential to a region of lower (more negative) "
          "water potential, through a partially permeable membrane.", title="Osmosis"),
        H("The equation"),
        F(r"\Psi = \Psi_s + \Psi_p", title="Water potential of a cell"),
        KEY("The terms", "Learn the signs.", cards=[
            ["Solute potential, Ψs", "The effect of dissolved solutes. It is always zero or negative. More solute means a more negative Ψs."],
            ["Pressure potential, Ψp", "The pressure on the water. In a plant cell it is the pressure of the cell contents pushing against the wall (turgor). It is usually positive or zero."],
            ["Water potential, Ψ", "The sum of the two. Water moves towards the more negative Ψ."],
        ]),
        T("In an open beaker the solution is at atmospheric pressure, so its Ψp is zero and its Ψ is equal to its Ψs. In a plant cell, the wall allows "
          "pressure to build up. A cell that is **turgid** has a high positive Ψp. A **flaccid** cell has Ψp = 0. A **plasmolysed** cell has lost water so far "
          "that the membrane has pulled away from the wall. **Incipient plasmolysis** is the point at which the membrane is just beginning to pull away: "
          "Ψp = 0, so Ψ = Ψs."),
        T("A fully turgid cell in pure water reaches equilibrium when Ψ = 0, so Ψp is equal in size to Ψs but opposite in sign. Water stops entering "
          "because the pressure of the wall balances the pull of the solutes. This is why a plant cell does not burst."),
        EX("Worked example 1: finding water potential", intro="A plant cell has a solute potential of -900 kPa and a pressure potential of +400 kPa. Calculate its water potential.", steps=[
            S("Write the equation", math=r"\Psi = \Psi_s + \Psi_p"),
            S("Substitute", math=r"\Psi = (-900) + (+400)"),
            S("Calculate", math=r"\Psi = -500\ \text{kPa}"),
        ], check=r"-900 + 400 = -500"),
        EX("Worked example 2: direction of water movement", intro="Cell X has Ψs = -900 kPa and Ψp = +400 kPa. Its neighbour, cell Y, has Ψs = -1100 kPa and Ψp = +500 kPa. In which direction will water move?", steps=[
            S("Cell X", math=r"\Psi_X = -900 + 400 = -500\ \text{kPa}"),
            S("Cell Y", math=r"\Psi_Y = -1100 + 500 = -600\ \text{kPa}"),
            S("Compare", text="-500 kPa is higher (less negative) than -600 kPa. Water moves from X to Y down the water potential gradient."),
            S("Note", text="Cell Y has the more negative Ψs but also the larger Ψp. Look at the total, not at one term."),
        ]),
        EX("Worked example 3: a cell placed in a solution", intro="A flaccid-looking cell has Ψs = -800 kPa and Ψp = +300 kPa. It is placed in an open beaker of sugar solution with Ψ = -300 kPa. (a) Which way does water move? (b) At equilibrium, assuming Ψs does not change, what is Ψp?", steps=[
            S("Water potential of the cell", math=r"\Psi = -800 + 300 = -500\ \text{kPa}"),
            S("(a) Direction", text="The solution (-300 kPa) is higher than the cell (-500 kPa), so water enters the cell."),
            S("(b) At equilibrium", text="The cell Ψ rises until it equals -300 kPa."),
            S("Solve for Ψp", math=r"\Psi_p = \Psi - \Psi_s = -300 - (-800) = +500\ \text{kPa}"),
        ], check=r"-800 + 500 = -300"),
        H("Potato cylinders: estimating the water potential of tissue"),
        T("Cylinders of potato of the same size are weighed and placed in sucrose solutions of different concentrations. After a fixed time they are dried and "
          "reweighed. A cylinder gains mass when water enters (solution has higher Ψ than the tissue) and loses mass when water leaves. At the concentration where "
          "there is no change in mass, the solution and the tissue have the same Ψ."),
        IMG("al-bil1-potato-graph.svg", alt="Graph of percentage change in mass of potato cylinders against sucrose concentration, crossing zero at 0.25 mol per dm3",
            caption="Figure 1. Teaching data: change in mass of potato cylinders. The line crosses 0% at 0.25 mol per dm3."),
        T("The percentage change is (final mass - initial mass) / initial mass × 100. From Figure 1, the cylinder gains 3% at 0.2 and loses 3% at 0.3, so the "
          "line crosses zero at 0.25 mol per dm3. A table of values would show that a sucrose solution of this concentration has a water potential of about "
          "-650 kPa (an approximate teaching value). That is the water potential of the potato cells, because the tissue is at equilibrium with the solution."),
        TIP("When you prepare a dilution, use the proportion: for 20 cm3 of 0.2 mol per dm3 sucrose from a 1.0 mol per dm3 stock, take 4 cm3 of stock and add 16 cm3 of distilled water (0.2/1.0 × 20 = 4)."),
        MISTAKE("Saying 'water moves from high concentration of water to low concentration of water' without water potential", "Use water potential: water moves from higher (less negative) to lower (more negative) water potential."),
        MISTAKE("Thinking -900 is higher than -500", "Negative numbers are lower the more negative they are. -500 is higher than -900."),
        QUIZ("A solution in an open beaker has a solute potential of -400 kPa. What is its water potential?",
             ["+400 kPa", "0 kPa", "-400 kPa", "-800 kPa"], 2,
             "In an open beaker the pressure potential is zero, so Ψ = Ψs = -400 kPa.",
             hint="What is the pressure potential in an open beaker?",
             feedback=["Solutions always have a negative water potential.", "Only pure water at standard pressure has Ψ = 0.", "", "This doubles the value for no reason."]),
        QUIZ("A cell has Ψ = -600 kPa. It is placed in a solution with Ψ = -400 kPa. What happens?",
             ["Water leaves the cell", "Water enters the cell", "No net movement", "The cell becomes plasmolysed"], 1,
             "The solution has the higher water potential, so water enters the cell by osmosis.",
             hint="Which is higher, -400 or -600?",
             feedback=["Water leaves only if the solution has the lower Ψ.", "", "There is a difference in Ψ, so there is a net movement.", "Plasmolysis happens when water leaves."]),
        H("Practice"),
        PQ("Define water potential and state the water potential of pure water.", "Water potential is a measure of the tendency of water molecules to move from one region to another. Pure water at standard pressure has a water potential of zero, the highest value."),
        PQ("A cell has Ψs = -700 kPa and is flaccid (Ψp = 0). It is placed in pure water. Describe what happens and state the final Ψp at equilibrium, assuming Ψs stays the same.", "The cell has Ψ = -700 kPa, lower than water (0 kPa), so water enters by osmosis and the cell becomes turgid. At equilibrium Ψ = 0, so Ψp = 0 - (-700) = +700 kPa."),
        PQ("Use the equation to explain why a plant cell in a concentrated sucrose solution can reach incipient plasmolysis.", "Water leaves the cell, which reduces the volume and the pressure potential. When Ψp falls to zero the membrane is just beginning to pull away from the wall. At this point Ψ = Ψs, and the cell is at equilibrium with a solution of the same Ψ."),
        TIP("Exam link: water potential calculations and potato-cylinder data appear in Paper 1 and Paper 2, and osmosis experiments are common in the practical paper. Show the equation, substitute with signs, and state the direction of movement using the words 'higher' and 'lower' water potential."),
        SUM("Water potential Ψ is measured in kPa. Pure water is 0 and solutions are negative.",
            "Ψ = Ψs + Ψp. Ψs is zero or negative. Ψp is positive in a turgid cell and zero in an open solution.",
            "Water moves by osmosis from higher (less negative) to lower (more negative) Ψ through a partially permeable membrane.",
            "At incipient plasmolysis Ψp = 0 so Ψ = Ψs. In potato data, the concentration giving no change in mass has the same Ψ as the tissue."),
    ],
))

# ------------------------------------------------------------------ 5. Passive transport
LESSONS.append(lesson(
    module=M1,
    topic="Transport across membranes",
    title="Diffusion, facilitated diffusion and surface area to volume ratio",
    slug="bil1-passive-transport",
    minutes=22,
    summary="Passive transport needs no energy from the cell. Explain simple and facilitated diffusion with Fick's law, calculate surface area to volume ratios and use agar-cube data.",
    objectives=[
        "Define diffusion and facilitated diffusion and state the factors that affect the rate",
        "Use the idea of Fick's law to compare rates of diffusion",
        "Calculate surface area to volume ratios and explain why cells and exchange organs are small or folded",
        "Distinguish simple diffusion, facilitated diffusion and osmosis",
    ],
    key_concepts=["Diffusion", "Concentration gradient", "Fick's law", "Facilitated diffusion", "Channel protein", "Carrier protein", "Surface area to volume ratio"],
    blocks=[
        H("Introduction"),
        T("When a pot of groundnut soup is cooked in a kitchen in Bafoussam, the smell reaches the next room within minutes. No one carries it there. "
          "The scent molecules spread out by themselves. The same process moves oxygen into cells and carbon dioxide out. It needs no energy from the cell, "
          "and it is called **passive transport**."),
        D("**Diffusion** is the net movement of molecules or ions from a region of higher concentration to a region of lower concentration, down a concentration "
          "gradient, as a result of their random movement. It is passive because it uses the kinetic energy of the particles, not ATP.", title="Definition"),
        D("**Facilitated diffusion** is the passive movement of molecules or ions down their concentration gradient through channel proteins or carrier proteins "
          "in a membrane. It is needed for ions and polar molecules that cannot pass through the hydrophobic core.", title="Definition"),
        H("Factors that affect the rate"),
        F(r"\text{rate of diffusion} \propto \frac{\text{surface area} \times \text{concentration difference}}{\text{thickness of the exchange surface}}", title="Fick's law"),
        KEY("What makes diffusion faster", "Apply each to a real surface such as a gill or an alveolus.", cards=[
            ["Larger surface area", "More room for molecules to cross. Villi, alveoli and gills have folded surfaces."],
            ["Steeper concentration gradient", "A bigger difference between the two sides. Blood flow keeps the gradient steep by removing absorbed molecules."],
            ["Thinner surface", "A shorter distance to travel. An alveolar wall is one cell thick."],
            ["Higher temperature", "Particles move faster."],
            ["Smaller, non-polar molecules", "Cross the bilayer more easily."],
        ]),
        T("Facilitated diffusion has an extra feature. **Channel proteins** have a water-filled pore that is open to particular ions. **Carrier proteins** bind a molecule, "
          "change shape and release it on the other side. Because the number of carriers is limited, the rate levels off when all carriers are busy (the carriers are saturated). "
          "Simple diffusion through the bilayer does not level off in this way: the rate keeps increasing in proportion to the gradient."),
        H("Surface area to volume ratio"),
        T("As a cell or organism gets bigger, its volume increases faster than its surface area. A cube of side $s$ has surface area $6s^2$ and volume $s^3$, so its surface area to "
          "volume ratio is $6/s$. Large ratios help exchange. This is why cells are small and why exchange organs are folded or flattened."),
        EX("Worked example 1: surface area to volume ratio", intro="Calculate the surface area to volume ratio of cubes of side 1 cm, 2 cm and 4 cm.", steps=[
            S("1 cm cube", math=r"\frac{6 \times 1^2}{1^3} = \frac{6}{1} = 6 : 1"),
            S("2 cm cube", math=r"\frac{6 \times 2^2}{2^3} = \frac{24}{8} = 3 : 1"),
            S("4 cm cube", math=r"\frac{6 \times 4^2}{4^3} = \frac{96}{64} = 1.5 : 1"),
            S("Conclusion", text="The ratio falls as the cube gets larger. Diffusion from the surface to the centre becomes too slow, so large organisms need transport systems."),
        ]),
        EX("Worked example 2: agar cubes", intro="A 3 cm cube of agar containing an indicator is left in dilute acid until the acid has diffused 0.5 cm in from every face. Calculate the percentage of the volume that the acid has reached.", steps=[
            S("Total volume", math=r"3^3 = 27\ \text{cm}^3"),
            S("Volume not reached", text="The unreached part is a cube of side 3 - 2 × 0.5 = 2 cm.", math=r"2^3 = 8\ \text{cm}^3"),
            S("Volume reached", math=r"27 - 8 = 19\ \text{cm}^3"),
            S("Percentage", math=r"\frac{19}{27} \times 100 = 70.4\%"),
        ]),
        EX("Worked example 3: using Fick's law", intro="Membrane P has twice the surface area of membrane Q and is half as thick. The concentration difference is the same. Compare the rates of diffusion.", steps=[
            S("Area", text="Doubling area doubles the rate."),
            S("Thickness", text="Halving the thickness doubles the rate again."),
            S("Total", math=r"2 \times 2 = 4"),
            S("Answer", text="P diffuses four times faster than Q."),
        ]),
        MISTAKE("Saying diffusion 'uses' or 'needs' energy", "It does not need energy from the cell. Particles move by their own kinetic energy. Active transport is the process that uses ATP."),
        MISTAKE("Saying facilitated diffusion goes against the gradient", "Facilitated diffusion is passive and always goes down the concentration gradient. The protein only provides a pathway."),
        QUIZ("Which feature distinguishes facilitated diffusion from simple diffusion?",
             ["It uses ATP", "It needs a channel or carrier protein", "It moves substances against the gradient", "It only moves water"], 1,
             "Facilitated diffusion uses membrane proteins, but needs no ATP and moves down the gradient.",
             hint="Which molecules cannot cross the bilayer alone?",
             feedback=["Facilitated diffusion is passive.", "", "It moves down the gradient.", "Water moves by osmosis, and facilitated diffusion is for ions and polar molecules."]),
        QUIZ("A cube of side 2 cm has a surface area to volume ratio of 3:1. What is the ratio for a cube of side 6 cm?",
             ["1:1", "6:1", "0.5:1", "9:1"], 0,
             "Ratio = 6/s = 6/6 = 1. The ratio is 1:1.",
             hint="The ratio of a cube is 6 divided by its side.",
             feedback=["", "This is the ratio for a 1 cm cube.", "This is a calculation error: 6/6 = 1.", "The ratio decreases as the cube grows."]),
        H("Practice"),
        PQ("Explain why the rate of facilitated diffusion reaches a maximum as the concentration gradient increases.", "The rate depends on the number of channel or carrier proteins. When all the carriers are in use (saturated), a larger concentration difference cannot increase the rate further."),
        PQ("Calculate the surface area to volume ratio of a cube of side 3 cm.", "Surface area = 6 × 3² = 54 cm². Volume = 3³ = 27 cm³. Ratio = 54/27 = 2:1."),
        PQ("Explain how the structure of the alveolar wall makes diffusion of oxygen fast.", "It is only one cell thick, so the diffusion distance is short. The very large total surface area gives more room for diffusion. A rich blood supply removes oxygen and keeps the concentration gradient steep."),
        TIP("Exam link: diffusion and surface area to volume ratio appear in Paper 1 and Paper 2 and in practical work with agar cubes and Visking tubing. Show the formula for surface area and volume and state the ratio as a number to 1."),
        SUM("Diffusion is passive movement down a concentration gradient. Facilitated diffusion uses channel and carrier proteins and is also passive.",
            "The rate depends on surface area, concentration difference and thickness: rate is proportional to area × gradient ÷ thickness.",
            "Surface area to volume ratio falls as size increases, so large organisms need exchange surfaces and transport systems.",
            "Carrier-mediated transport saturates. Simple diffusion does not."),
    ],
))

# ------------------------------------------------------------------ 6. Active and bulk transport
LESSONS.append(lesson(
    module=M1,
    topic="Transport across membranes",
    title="Active transport, endocytosis and exocytosis",
    slug="bil1-active-and-bulk-transport",
    minutes=22,
    summary="Active transport moves substances against their gradient using ATP and carrier proteins. Vesicles move large particles in (endocytosis) and out (exocytosis). Compare all the transport processes and interpret evidence.",
    objectives=[
        "Define active transport and explain how it differs from diffusion",
        "Describe the sodium-potassium pump and co-transport of glucose",
        "Describe phagocytosis, pinocytosis and exocytosis",
        "Interpret data to decide whether a process is active or passive",
    ],
    key_concepts=["Active transport", "ATP", "Sodium-potassium pump", "Co-transport", "Endocytosis", "Phagocytosis", "Pinocytosis", "Exocytosis"],
    blocks=[
        H("Introduction"),
        T("A root hair cell in the soil of a cassava farm takes in nitrate ions even though the cell already contains more nitrate than the soil water. "
          "Diffusion would move nitrate the other way. The cell must use energy to pull the ions in. This is **active transport**."),
        D("**Active transport** is the movement of molecules or ions across a membrane against their concentration gradient, using energy from ATP and "
          "specific carrier proteins.", title="Definition"),
        KEY("How active transport differs from diffusion", "Learn all four points.", cards=[
            ["Direction", "Against the concentration gradient, from low to high concentration."],
            ["Energy", "Needs ATP from respiration. It stops if respiration stops."],
            ["Proteins", "Needs specific carrier proteins (pumps), which are saturated at high concentration."],
            ["Cells", "Cells that do much active transport have many mitochondria."],
        ]),
        H("Pumps and co-transport"),
        T("The **sodium-potassium pump** is a carrier protein in the cell surface membrane of animal cells. Each cycle uses one ATP to move three sodium ions out "
          "of the cell and two potassium ions in. This keeps the sodium concentration low inside the cell. The inside becomes slightly negative compared with the outside."),
        T("In **co-transport**, the sodium gradient made by the pump is used to move another substance. In the epithelium of the small intestine, a co-transport protein "
          "carries sodium ions and glucose molecules into the cell together. Sodium moves down its gradient, which provides the energy to pull glucose in against its own "
          "gradient. The pump outside then removes the sodium. Only the pump uses ATP directly."),
        H("Bulk transport"),
        T("Large particles cannot cross a membrane through proteins. They are carried inside vesicles made from the membrane itself. This needs ATP."),
        KEY("Bulk transport", "Move by vesicles.", cards=[
            ["Endocytosis", "The membrane folds in and pinches off to form a vesicle that carries material into the cell."],
            ["Phagocytosis", "Endocytosis of solid particles, such as a phagocyte engulfing a bacterium. The vesicle then joins a lysosome."],
            ["Pinocytosis", "Endocytosis of droplets of liquid."],
            ["Exocytosis", "A vesicle fuses with the cell surface membrane and releases its contents outside, for example enzymes or hormones. It adds to the membrane."],
        ]),
        CODE("""Process                  Energy (ATP)   Direction vs gradient   Proteins
Simple diffusion         no             down                    no
Facilitated diffusion    no             down                    channel/carrier
Osmosis (water)          no             down water potential    aquaporins may help
Active transport         yes            against                 carrier (pump)
Endo/exocytosis          yes            not applicable          none (vesicles)""", "text", title="Table 1. Transport processes compared"),
        EX("Worked example 1: is it active transport? (teaching data)", intro="Potassium ion uptake by root slices is 20 units per hour in normal air. In an oxygen-free tank it falls to 4 units per hour. With a respiratory poison present it falls to 3 units per hour. Explain.", steps=[
            S("Identify the pattern", text="Uptake depends on oxygen and is stopped by a poison that blocks respiration."),
            S("Link to ATP", text="Without oxygen or with the poison, less ATP is made."),
            S("Conclude", text="The uptake needs ATP, so it is active transport. A small uptake remains (3-4 units) because some ions enter by diffusion."),
        ]),
        EX("Worked example 2: sodium-potassium pump arithmetic", intro="A cell uses 10 000 ATP molecules in a short period for its sodium-potassium pumps. How many sodium ions leave and how many potassium ions enter, and what is the net number of positive charges removed?", steps=[
            S("Sodium out", math=r"3 \times 10\,000 = 30\,000"),
            S("Potassium in", math=r"2 \times 10\,000 = 20\,000"),
            S("Net charge removed", math=r"30\,000 - 20\,000 = 10\,000\ \text{positive charges}"),
        ]),
        MISTAKE("Saying active transport needs 'no concentration gradient'", "It works against a gradient, from low to high concentration. The gradient is the reason energy is needed."),
        MISTAKE("Calling bulk transport 'diffusion of large particles'", "Endocytosis and exocytosis are active processes with vesicles and need ATP."),
        QUIZ("Which observation is the best evidence that a substance is entering a cell by active transport?",
             ["Uptake rate rises in proportion to concentration outside", "Uptake continues against a concentration gradient and stops when respiration is blocked", "Uptake is faster at high temperature", "Uptake needs a large surface area"], 1,
             "Movement against the gradient that stops without ATP shows active transport.",
             hint="What does active transport need that diffusion does not?",
             feedback=["That is typical of simple diffusion.", "", "Temperature speeds up diffusion too.", "Area affects all transport."]),
        QUIZ("What is exocytosis?",
             ["A vesicle fuses with the cell surface membrane and releases its contents", "The cell takes in a solid particle", "Water moves out of the cell by osmosis", "An ion moves through a channel"], 0,
             "In exocytosis, vesicles carry material to the membrane and release it outside.",
             hint="'Exo' means outside.",
             feedback=["", "That is phagocytosis.", "That is osmosis.", "That is facilitated diffusion."]),
        H("Practice"),
        PQ("Explain why cells in the lining of the small intestine have many mitochondria.", "Absorption of glucose and amino acids involves active transport and co-transport, which need ATP. Mitochondria make the ATP by aerobic respiration."),
        PQ("Describe how glucose is absorbed from the lumen of the ileum into an epithelial cell by co-transport.", "The sodium-potassium pump removes sodium ions from the cell, making the sodium concentration low inside. Sodium ions enter with glucose through a co-transport protein, moving down the sodium gradient. The energy from this lets glucose enter against its own concentration gradient."),
        PQ("Distinguish between phagocytosis and pinocytosis.", "In phagocytosis the cell takes in solid particles, such as bacteria, in a vesicle. In pinocytosis it takes in droplets of fluid."),
        TIP("Exam link: transport across membranes is in Paper 1 (comparing processes, graphs of uptake against concentration or oxygen) and Paper 2 (descriptions and explanations). The Board's reports note that candidates lose marks when they say that diffusion or osmosis 'uses energy'. A 'plateau' on a graph of uptake against concentration points to carrier proteins."),
        SUM("Active transport uses ATP and carrier proteins to move substances against their gradient.",
            "The Na-K pump moves 3 Na out and 2 K in per ATP. Co-transport uses the sodium gradient to bring glucose into the cell.",
            "Endocytosis (phagocytosis and pinocytosis) takes material in by vesicles. Exocytosis releases material by vesicles. Both use ATP.",
            "Evidence for active transport: against the gradient, needs oxygen and ATP, stopped by respiratory poisons, shows saturation."),
    ],
))

# ------------------------------------------------------------------ 7. Carbohydrates
LESSONS.append(lesson(
    module=M2,
    topic="Carbohydrates",
    title="Monosaccharides, disaccharides and polysaccharides",
    slug="bil1-carbohydrates",
    minutes=23,
    summary="Carbohydrates are sugars and their polymers. Learn alpha and beta glucose, glycosidic bonds formed by condensation, and how the structures of starch, glycogen and cellulose suit their functions. Include the biochemical tests.",
    objectives=[
        "Describe the structure of alpha and beta glucose and the formation of glycosidic bonds by condensation",
        "Compare starch, glycogen and cellulose in structure and function",
        "Calculate the molecular formula and relative molecular mass of disaccharides and polysaccharides",
        "Describe the Benedict's and iodine tests, including the test for a non-reducing sugar",
    ],
    key_concepts=["Monosaccharide", "Glycosidic bond", "Condensation", "Hydrolysis", "Starch", "Glycogen", "Cellulose", "Reducing sugar"],
    blocks=[
        H("Introduction"),
        T("A cassava root, a plantain and a stick of sugar cane all store energy as carbohydrates, but the carbohydrate in each is different. "
          "Cassava and plantain store starch. Sugar cane stores sucrose. A tree trunk is mostly cellulose, which humans cannot digest. All are built from sugar units, joined in different ways."),
        D("A **monosaccharide** is a single sugar unit, such as glucose, fructose or galactose. A **disaccharide** has two units joined, and a **polysaccharide** has many. "
          "The general formula of a simple sugar is $(\\mathrm{CH_2O})_n$.", title="Definitions"),
        IMG("al-bil1-glucose.svg", alt="Haworth ring diagrams of alpha-glucose and beta-glucose, differing in the position of the OH on carbon 1",
            caption="Figure 1. Alpha-glucose and beta-glucose. Only the OH on carbon 1 differs."),
        H("Joining sugars"),
        D("A **glycosidic bond** joins two monosaccharides. It forms in a **condensation** reaction, in which a molecule of water is removed. "
          "The bond is broken by **hydrolysis**, in which water is added.", title="Definitions"),
        KEY("The three common disaccharides", "Each is made from two monosaccharides, with loss of one water.", cards=[
            ["Maltose", "Glucose + glucose. Formula C12H22O11. A reducing sugar."],
            ["Sucrose", "Glucose + fructose. Formula C12H22O11. A non-reducing sugar. The sugar in sugar cane."],
            ["Lactose", "Glucose + galactose. Formula C12H22O11. The sugar in milk. A reducing sugar."],
        ]),
        H("Polysaccharides"),
        KEY("Structure and function", "Compare the three.", cards=[
            ["Starch", "The storage polysaccharide of plants, made of alpha-glucose. It is a mixture of amylose (unbranched, alpha-1,4 bonds, coiled into a helix) and amylopectin (alpha-1,4 chains with alpha-1,6 branches). It is compact and insoluble, so it does not change the water potential of the cell."],
            ["Glycogen", "The storage polysaccharide of animals and fungi, made of alpha-glucose. It is like amylopectin but more highly branched. Many ends allow glucose to be released quickly."],
            ["Cellulose", "The structural polysaccharide of plant cell walls, made of beta-glucose in unbranched chains. Every second glucose is inverted, with beta-1,4 bonds. Many hydrogen bonds between chains form strong microfibrils."],
        ]),
        H("Tests"),
        CODE("""Test                   Method                              Positive result
Reducing sugar         Add Benedict's solution, heat       Blue turns green, yellow,
                       in a water bath                     orange, then brick-red
Non-reducing sugar     Do the reducing test first (negative). Boil with dilute HCl to
                       hydrolyse, neutralise with sodium hydrogencarbonate, then
                       repeat the Benedict's test          Brick-red precipitate
Starch                 Add iodine solution                 Yellow-brown turns blue-black""", "text", title="Table 1. Tests for carbohydrates"),
        EX("Worked example 1: formula and mass of maltose", intro="Two glucose molecules (C6H12O6) join by condensation to form maltose. Give the formula of maltose and its relative molecular mass (Ar: C = 12, H = 1, O = 16).", steps=[
            S("Add the two glucose molecules", math=r"2\,\mathrm{C_6H_{12}O_6} = \mathrm{C_{12}H_{24}O_{12}}"),
            S("Remove one water", math=r"\mathrm{C_{12}H_{24}O_{12}} - \mathrm{H_2O} = \mathrm{C_{12}H_{22}O_{11}}"),
            S("Relative molecular mass", math=r"12 \times 12 + 22 \times 1 + 11 \times 16 = 144 + 22 + 176 = 342"),
        ], check=r"2 \times 180 - 18 = 342"),
        EX("Worked example 2: a starch chain", intro="A starch chain has 1000 glucose units joined by alpha-1,4 bonds. How many water molecules are removed, and what is its relative molecular mass?", steps=[
            S("Number of bonds", text="1000 units need 999 bonds, and each bond removes one water."),
            S("Water removed", math=r"999\ \text{molecules}"),
            S("Mass", math=r"1000 \times 180 - 999 \times 18 = 180\,000 - 17\,982 = 162\,018"),
        ], check=r"1000 \times 162 + 18 = 162\,018"),
        MISTAKE("Saying cellulose is made of alpha-glucose", "Cellulose is made of beta-glucose. Starch and glycogen are made of alpha-glucose."),
        MISTAKE("Concluding that a sugar is 'not a sugar' because Benedict's test is negative", "Sucrose is a sugar but not a reducing sugar. Boil with acid first, then neutralise and repeat the test."),
        QUIZ("Which pair of monosaccharides forms sucrose?",
             ["Glucose and glucose", "Glucose and galactose", "Glucose and fructose", "Fructose and galactose"], 2,
             "Sucrose is glucose + fructose.",
             hint="Sucrose is table sugar from sugar cane.",
             feedback=["That makes maltose.", "That makes lactose.", "", "This is not a common disaccharide in food."]),
        QUIZ("Why is glycogen better than amylose for rapid release of glucose?",
             ["It is made of beta-glucose", "It has many branches, so many ends can be hydrolysed at the same time", "It is soluble", "It has no glycosidic bonds"], 1,
             "Enzymes can remove glucose from many chain ends at once.",
             hint="Think about the number of free ends.",
             feedback=["Glycogen is made of alpha-glucose.", "", "Glycogen is a compact, insoluble store.", "It has alpha-1,4 and alpha-1,6 glycosidic bonds."]),
        H("Practice"),
        PQ("Distinguish between a condensation reaction and a hydrolysis reaction.", "Condensation joins two molecules and releases a molecule of water, forming a bond such as a glycosidic bond. Hydrolysis uses a molecule of water to break the bond."),
        PQ("Explain how the structure of cellulose makes it suitable for the cell wall.", "Beta-glucose units form long straight, unbranched chains. Many hydrogen bonds between neighbouring chains form microfibrils that have great tensile strength, so the wall resists the pressure of a turgid cell."),
        PQ("Describe how you would show that a solution contains sucrose and no reducing sugar.", "Add Benedict's solution and heat: no colour change to brick-red, showing no reducing sugar. Boil a fresh sample with dilute hydrochloric acid to hydrolyse sucrose, neutralise with sodium hydrogencarbonate, add Benedict's solution and heat. A brick-red precipitate now shows a non-reducing sugar was present."),
        TIP("Exam link: carbohydrates appear in Paper 1 (structures, tests) and Paper 2 (comparisons of starch, glycogen and cellulose) and in the practical paper (Benedict's and iodine tests, and food tests). Always name the bond (alpha-1,4 or beta-1,4) and relate structure to function."),
        SUM("Monosaccharides join by condensation to form glycosidic bonds. Hydrolysis breaks them.",
            "Alpha-glucose forms starch and glycogen. Beta-glucose forms cellulose. Only the OH on carbon 1 differs.",
            "Starch (amylose and amylopectin) and glycogen are compact stores. Cellulose is a strong structural fibre.",
            "Benedict's detects reducing sugars. Sucrose needs acid hydrolysis first. Iodine detects starch."),
    ],
))

# ------------------------------------------------------------------ 8. Lipids
LESSONS.append(lesson(
    module=M2,
    topic="Lipids",
    title="Triglycerides, phospholipids and the roles of lipids",
    slug="bil1-lipids",
    minutes=22,
    summary="Lipids are non-polar molecules made of fatty acids, glycerol and other groups. Learn the ester bond, saturated and unsaturated fatty acids, phospholipids, and why lipids are good energy stores. Include the emulsion test.",
    objectives=[
        "Describe the structure of a triglyceride and the formation of ester bonds",
        "Distinguish saturated, monounsaturated and polyunsaturated fatty acids",
        "Describe the structure of a phospholipid and relate it to its role",
        "State the functions of lipids and describe the emulsion test",
    ],
    key_concepts=["Triglyceride", "Ester bond", "Fatty acid", "Saturated", "Unsaturated", "Phospholipid", "Emulsion test"],
    blocks=[
        H("Introduction"),
        T("Palm oil from the coast, groundnut oil in a market in Mbouda, and the fat in a piece of beef are all lipids. They do not dissolve in water. "
          "They store energy, insulate the body and form every cell membrane. All lipids are made mainly of carbon, hydrogen and oxygen, with much less oxygen than carbohydrates."),
        D("A **triglyceride** is made of one **glycerol** molecule joined to three **fatty acids** by **ester bonds**. Each ester bond forms in a condensation reaction "
          "that releases one molecule of water, so three waters are released.", title="Definition"),
        CODE("""glycerol + 3 fatty acids  ->  triglyceride + 3 water

Example: glycerol C3H8O3 + 3 palmitic acid C16H32O2
         -> triglyceride C51H98O6 + 3 H2O""", "text", title="Equation 1. Making a triglyceride"),
        H("Fatty acids"),
        KEY("Saturated and unsaturated", "The difference is in the hydrocarbon tail.", cards=[
            ["Saturated", "No carbon-carbon double bonds. The tails are straight and pack closely, so the lipid has a higher melting point and is solid at room temperature (animal fats)."],
            ["Monounsaturated", "One double bond. The tail has a kink. The lipid is usually liquid (olive oil)."],
            ["Polyunsaturated", "Two or more double bonds. Many kinks, so it is liquid at room temperature (most plant oils)."],
        ]),
        T("A phospholipid is like a triglyceride, but one fatty acid is replaced by a **phosphate group**. The phosphate head is hydrophilic and the two fatty acid tails are hydrophobic, "
          "so a phospholipid is amphipathic. In water it forms the bilayer of cell membranes."),
        H("Functions of lipids"),
        KEY("Roles", "Link each role to a property.", cards=[
            ["Energy store", "A gram of lipid releases about 39 kJ, compared with about 17 kJ for a gram of carbohydrate (approximate values; check your textbook). Lipids are insoluble, so they do not change water potential."],
            ["Insulation", "Fat under the skin reduces heat loss. Myelin around nerves insulates electrically."],
            ["Buoyancy and protection", "Fat cushions organs such as the kidneys. Fat is less dense than water."],
            ["Waterproofing", "Waxes on leaves and insect cuticles reduce water loss."],
            ["Membranes and hormones", "Phospholipids form membranes. Cholesterol is a sterol that is used to make steroid hormones."],
            ["Metabolic water", "Oxidation of lipid releases more water per gram than carbohydrate, which helps desert animals."],
        ]),
        H("The emulsion test"),
        T("Shake a little of the sample with ethanol so that the lipid dissolves. Pour the clear mixture into water. If lipid is present, it forms tiny droplets, "
          "and a white cloudy **emulsion** appears. No lipid gives a clear mixture."),
        EX("Worked example 1: water released", intro="One triglyceride forms from glycerol and three fatty acids. How many water molecules are made, and how many are made when 200 triglyceride molecules form?", steps=[
            S("Per triglyceride", text="One water per ester bond, and there are three ester bonds."),
            S("For 200 molecules", math=r"3 \times 200 = 600\ \text{water molecules}"),
        ]),
        EX("Worked example 2: energy store (approximate values)", intro="A seed contains 20 g of lipid. Another seed contains 20 g of carbohydrate. Use 39 kJ per g for lipid and 17 kJ per g for carbohydrate to compare the energy stored.", steps=[
            S("Lipid seed", math=r"20 \times 39 = 780\ \text{kJ}"),
            S("Carbohydrate seed", math=r"20 \times 17 = 340\ \text{kJ}"),
            S("Compare", math=r"\frac{780}{340} = 2.3"),
            S("Conclude", text="The lipid store holds about 2.3 times as much energy, so lipid is a more compact store. This matters for seeds, which must be light for dispersal."),
        ]),
        MISTAKE("Saying a triglyceride has three glycerol molecules", "It has one glycerol and three fatty acids."),
        MISTAKE("Saying unsaturated fatty acids have fewer hydrogen atoms 'because they are shorter'", "They have double bonds, so each double bond takes the place of two hydrogen atoms. The chain length is the same."),
        QUIZ("What type of bond joins a fatty acid to glycerol?",
             ["Glycosidic bond", "Peptide bond", "Ester bond", "Hydrogen bond"], 2,
             "A fatty acid and glycerol join by an ester bond in a condensation reaction.",
             hint="The bond has the same name as the reaction that makes oil-based perfumes.",
             feedback=["A glycosidic bond joins sugars.", "A peptide bond joins amino acids.", "", "Hydrogen bonds are weak bonds between molecules."]),
        QUIZ("Why do plants such as the groundnut store energy as oil in the seed?",
             ["Oil is soluble in water", "Oil stores more energy per gram than starch", "Oil has no hydrogen", "Oil is easier to digest"], 1,
             "Lipids release about twice as much energy per gram as carbohydrates, so a seed can be small and light.",
             hint="Think about the energy released per gram.",
             feedback=["Lipids are insoluble in water.", "", "Lipids contain many hydrogen atoms.", "Lipids are not digested faster than starch."]),
        H("Practice"),
        PQ("Draw a labelled diagram or describe the structure of a phospholipid.", "A glycerol backbone has two fatty acid tails (hydrophobic) joined by ester bonds, and a phosphate group (hydrophilic head) on the third carbon."),
        PQ("Describe the emulsion test for lipids.", "Dissolve the sample by shaking with ethanol, filter or pour the clear liquid into water. A white cloudy emulsion shows lipid is present."),
        PQ("Explain why saturated fats are solid at room temperature but plant oils are liquid.", "Saturated fatty acid tails are straight, so the molecules pack closely and have strong attractions between them, giving a high melting point. Unsaturated tails are kinked by double bonds, so they pack less closely and the lipid stays liquid."),
        TIP("Exam link: lipids appear in Paper 1 (bonds, formulas) and Paper 2 (structure and function) and in food tests in the practical paper. State the type of bond and name the product of the condensation reaction."),
        SUM("A triglyceride is glycerol plus three fatty acids joined by ester bonds, with three waters released.",
            "Saturated fatty acids have no double bonds and are solid. Unsaturated ones have kinks and are liquid.",
            "A phospholipid has a hydrophilic phosphate head and two hydrophobic tails. It forms the membrane bilayer.",
            "Lipids store energy compactly, insulate, protect, waterproof and form membranes and steroids. The emulsion test uses ethanol then water."),
    ],
))

# ------------------------------------------------------------------ 9. Amino acids and protein structure
LESSONS.append(lesson(
    module=M2,
    topic="Amino acids and protein structure",
    title="Amino acids, peptide bonds and the four levels of protein structure",
    slug="bil1-amino-acids-proteins",
    minutes=24,
    summary="Proteins are polymers of amino acids joined by peptide bonds. Describe the primary, secondary, tertiary and quaternary structures, the bonds that hold them, fibrous and globular proteins, and denaturation.",
    objectives=[
        "Draw or describe the general structure of an amino acid and the formation of a peptide bond",
        "Describe the four levels of protein structure and the bonds at each level",
        "Compare fibrous and globular proteins with examples such as collagen and haemoglobin",
        "Explain denaturation and the effect of a single amino acid change",
    ],
    key_concepts=["Amino acid", "Peptide bond", "Primary structure", "Alpha helix", "Beta-pleated sheet", "Tertiary structure", "Quaternary structure", "Denaturation"],
    blocks=[
        H("Introduction"),
        T("Egg white turns from clear to white when you fry an egg in a pan. The protein albumin has changed shape and cannot change back. "
          "A protein's shape decides its job, and its shape is decided by the order of its amino acids. This lesson explains how."),
        D("An **amino acid** has a central carbon atom bonded to an amino group ($-\\mathrm{NH_2}$), a carboxyl group ($-\\mathrm{COOH}$), a hydrogen atom and a variable **R group**. "
          "There are 20 different R groups in the amino acids used to make proteins.", title="Definition"),
        CODE("""        H     R     O
        |     |     ||
   H2N--C--- C --- C--OH      (general structure: amino group,
        |                      central C with H and R, carboxyl group)
        H""", "text", title="Figure 1. General structure of an amino acid (simplified)"),
        H("The peptide bond"),
        T("Two amino acids join when the carboxyl group of one reacts with the amino group of the other. A molecule of water is removed in this **condensation** reaction, "
          "and the **peptide bond** (C-N) is formed. Two amino acids make a dipeptide, and many make a **polypeptide**. Hydrolysis breaks the bond by adding water."),
        EX("Worked example 1: mass of a peptide", intro="Glycine has a relative molecular mass of 75. Calculate the relative molecular mass of a tripeptide made of three glycine molecules (glycine-glycine-glycine).", steps=[
            S("Add three amino acids", math=r"3 \times 75 = 225"),
            S("Number of peptide bonds", text="Three amino acids need 2 bonds, and each releases one water (Mr 18)."),
            S("Subtract", math=r"225 - 2 \times 18 = 189"),
        ], check=r"3 \times 75 - 2 \times 18 = 189"),
        H("Four levels of structure"),
        KEY("Structure and bonds", "Learn what holds each level together.", cards=[
            ["Primary", "The sequence of amino acids in the polypeptide, held by peptide bonds. It is decided by the gene."],
            ["Secondary", "Regular folding of the chain into an alpha helix or a beta-pleated sheet, held by hydrogen bonds between the C=O and N-H groups of the backbone."],
            ["Tertiary", "The overall 3-D shape of one polypeptide, held by bonds between R groups: hydrogen bonds, ionic bonds, disulfide bridges (between cysteine residues) and hydrophobic interactions."],
            ["Quaternary", "Two or more polypeptides (and sometimes a non-protein group) combined. Haemoglobin has four polypeptides, each with a haem group."],
        ]),
        T("**Fibrous proteins** such as collagen are long, strong and insoluble. Three polypeptides wind together into a rope, strengthened by cross-links, so collagen gives strength to tendons and skin. "
          "**Globular proteins** such as enzymes and haemoglobin are rounded and soluble. Their hydrophilic R groups face outward and hydrophobic R groups face the centre."),
        D("**Denaturation** is a permanent change in the shape of a protein, caused by high temperature, extreme pH or some chemicals. The weak bonds (hydrogen, ionic) that hold the tertiary structure break, "
          "so the active site or binding site loses its shape. The primary structure is not changed.", title="Definition"),
        T("A single change in the primary structure can change the shape. In sickle cell haemoglobin, the amino acid glutamic acid at position 6 of each beta-polypeptide is replaced by valine. "
          "The hydrophobic valine makes the molecules stick together at low oxygen concentration, and the red blood cells are distorted."),
        EX("Worked example 2: counting", intro="Haemoglobin has two alpha chains of 141 amino acids and two beta chains of 146 amino acids. Calculate the total number of amino acids and the number of peptide bonds.", steps=[
            S("Total amino acids", math=r"2 \times 141 + 2 \times 146 = 282 + 292 = 574"),
            S("Peptide bonds", text="Each chain of n amino acids has n - 1 bonds, so the total is 574 - 4 (one fewer per chain)."),
            S("Calculate", math=r"574 - 4 = 570"),
        ]),
        EX("Worked example 3: possible sequences", intro="How many different tripeptides can be made from the 20 amino acids if each position can be any of them?", steps=[
            S("Choices at each position", text="20 choices for each of the 3 positions."),
            S("Multiply", math=r"20 \times 20 \times 20 = 20^3 = 8000"),
            S("Meaning", text="Even a very short chain has thousands of possible sequences, so a protein of hundreds of residues has an enormous number of possible sequences."),
        ]),
        MISTAKE("Saying the primary structure is destroyed by denaturation", "Denaturation breaks weak bonds that hold the tertiary (and secondary) structure. Peptide bonds are not broken."),
        MISTAKE("Saying hydrogen bonds hold the primary structure", "Peptide bonds hold the primary structure. Hydrogen bonds hold secondary structure and help with tertiary structure."),
        QUIZ("Which bonds hold the alpha helix together?",
             ["Peptide bonds between R groups", "Hydrogen bonds between backbone groups", "Disulfide bridges between helices", "Ester bonds"], 1,
             "Hydrogen bonds between the C=O and N-H of the backbone give the secondary structure.",
             hint="Secondary structure is about the backbone, not the R groups.",
             feedback=["Peptide bonds link amino acids in the primary structure.", "", "Disulfide bridges are part of the tertiary structure.", "Ester bonds are in lipids."]),
        QUIZ("What happens to an enzyme when it is denatured by heat?",
             ["Its peptide bonds break", "Its amino acid sequence changes", "The tertiary structure and active site change shape", "It becomes a lipid"], 2,
             "Heat breaks the weak bonds holding the 3-D shape, so the active site changes.",
             hint="Which bonds are weak enough to break at moderate temperatures?",
             feedback=["Peptide bonds need strong acids or enzymes to break.", "The sequence stays the same.", "", "A protein stays a protein."]),
        H("Practice"),
        PQ("State two differences between the structure of collagen and haemoglobin.", "Collagen is fibrous, with three polypeptides wound into a rope, insoluble and strong. Haemoglobin is globular, with four polypeptides folded into a ball, soluble and with a haem group."),
        PQ("Describe how a peptide bond is formed between two amino acids.", "The carboxyl group of one amino acid reacts with the amino group of the other, in a condensation reaction. A water molecule is lost and a C-N peptide bond forms."),
        PQ("Explain how a change in a single amino acid in the primary structure may alter the function of a protein.", "A different R group may form different bonds, so the tertiary structure folds differently and the shape of the protein changes. For example, the change of glutamic acid to valine in sickle cell haemoglobin makes the molecule stick together at low oxygen."),
        TIP("Exam link: protein structure appears in Paper 1 (levels and bonds) and Paper 2 (descriptions, structure and function, enzymes, denaturation, haemoglobin and collagen). It also links to practical work with the biuret test (purple colour with peptide bonds)."),
        SUM("Amino acids have an amino group, a carboxyl group, hydrogen and an R group. Peptide bonds form by condensation.",
            "Primary: sequence. Secondary: helices and sheets by hydrogen bonds. Tertiary: 3-D shape by R-group bonds. Quaternary: several polypeptides.",
            "Fibrous proteins (collagen) are strong and insoluble. Globular proteins (enzymes, haemoglobin) are rounded and soluble.",
            "Denaturation changes the shape but not the sequence. A change in one amino acid can change the shape."),
    ],
))

# ------------------------------------------------------------------ 10. Enzyme kinetics
LESSONS.append(lesson(
    module=M2,
    topic="Enzyme kinetics",
    title="Enzyme action and the Michaelis-Menten curve",
    slug="bil1-enzyme-kinetics",
    minutes=24,
    summary="Enzymes lower activation energy through the active site. Explain how temperature, pH and substrate concentration affect rate, and use the Michaelis-Menten equation, Vmax and Km to analyse data.",
    objectives=[
        "Explain enzyme action using the active site, the induced fit model and activation energy",
        "Describe the effect of temperature, pH and enzyme and substrate concentration on rate",
        "Define Vmax and Km and read them from a Michaelis-Menten curve",
        "Use v = Vmax[S]/(Km + [S]) to calculate rates and substrate concentrations",
    ],
    key_concepts=["Active site", "Induced fit", "Activation energy", "Initial rate", "Vmax", "Km", "Michaelis-Menten equation", "Saturation"],
    blocks=[
        H("Introduction"),
        T("Papain from pawpaw leaves is used to tenderise meat in many kitchens. A small amount of papain can break down a lot of meat protein, and then it can do the same again. "
          "Enzymes are biological catalysts, and this lesson shows how to describe their speed using measurements and a simple equation."),
        D("An **enzyme** is a globular protein that acts as a biological catalyst. It lowers the **activation energy** of a reaction, so the reaction goes faster, and it is not used up. "
          "The **active site** is the region of the enzyme where the substrate binds.", title="Definitions"),
        T("In the **induced fit** model the active site is not a rigid lock. When the substrate binds, the active site changes shape slightly to fit it more closely, "
          "which puts strain on the bonds of the substrate. The enzyme-substrate complex forms the products, which leave the active site."),
        H("Factors affecting rate"),
        KEY("Factors", "Always use the idea of kinetic energy and shape.", cards=[
            ["Temperature", "Rate rises as molecules gain kinetic energy and collide more often with enough energy. Above the optimum the enzyme starts to denature and the rate falls steeply."],
            ["pH", "Each enzyme has an optimum pH. Changes in pH alter the charges on R groups, break ionic and hydrogen bonds and change the active site."],
            ["Substrate concentration", "The rate rises as more substrate is available, then levels off at Vmax when all active sites are in use."],
            ["Enzyme concentration", "The rate is proportional to enzyme concentration when substrate is in excess."],
        ]),
        H("The Michaelis-Menten curve"),
        T("The **initial rate** ($v$) is measured at the start of a reaction, before the substrate is used up or product builds up. A graph of $v$ against substrate concentration $[S]$ "
          "is a curve that rises steeply and then levels off."),
        IMG("al-bil1-mm-curve.svg", alt="Michaelis-Menten curve of initial rate against substrate concentration, with Vmax at 50 and Km at 2",
            caption="Figure 1. Teaching data: Vmax = 50 µmol per min, Km = 2 mmol per dm3."),
        D("**Vmax** is the maximum rate, reached when all the active sites are saturated. **Km** (the Michaelis constant) is the substrate concentration at which the rate is half of Vmax. "
          "A low Km means the enzyme reaches half of its maximum rate at a low substrate concentration, so it has a high affinity for the substrate.", title="Vmax and Km",
          formula=r"v = \frac{V_{\max}[S]}{K_m + [S]}"),
        EX("Worked example 1: reading the curve", intro="Use Figure 1 to find Vmax and Km.", steps=[
            S("Vmax", text="The curve levels off towards 50 µmol per min, so Vmax = 50."),
            S("Half of Vmax", math=r"\frac{50}{2} = 25\ \mu\text{mol per min}"),
            S("Read across", text="The rate is 25 when [S] = 2 mmol per dm3, so Km = 2 mmol per dm3."),
        ]),
        EX("Worked example 2: calculating a rate", intro="Vmax = 50 µmol per min and Km = 2 mmol per dm3. Calculate the rate at [S] = 8 mmol per dm3.", steps=[
            S("Substitute", math=r"v = \frac{50 \times 8}{2 + 8}"),
            S("Calculate", math=r"v = \frac{400}{10} = 40\ \mu\text{mol per min}"),
        ], check=r"\frac{40}{50} = 0.8 = \frac{8}{2+8}"),
        EX("Worked example 3: finding a concentration", intro="With the same enzyme, at what [S] is the rate 40 µmol per min?", steps=[
            S("Rearrange", math=r"[S] = \frac{v K_m}{V_{\max} - v}"),
            S("Substitute", math=r"[S] = \frac{40 \times 2}{50 - 40} = \frac{80}{10}"),
            S("Answer", math=r"[S] = 8\ \text{mmol per dm}^3"),
        ]),
        TIP("Extension (check your textbook): plotting 1/v against 1/[S] gives a straight line (the Lineweaver-Burk plot) with a gradient of Km/Vmax and a y-intercept of 1/Vmax. For this enzyme the y-intercept is 1/50 = 0.02 and the gradient is 2/50 = 0.04."),
        MISTAKE("Saying the rate levels off because the substrate runs out", "It levels off because all the enzyme active sites are occupied (saturated). The substrate is not used up in an initial-rate measurement."),
        MISTAKE("Reading Km from the x-axis at Vmax", "Km is the substrate concentration at half of Vmax, not at Vmax."),
        QUIZ("Enzyme P has Km = 1 mmol per dm3 and enzyme Q has Km = 10 mmol per dm3 for the same substrate. Which statement is correct?",
             ["Q has the higher affinity", "P has the higher affinity", "Both have the same affinity", "P has the higher Vmax"], 1,
             "A low Km means half of Vmax is reached at a low substrate concentration, so affinity is high.",
             hint="Which enzyme works well at low substrate concentration?",
             feedback=["The higher Km of Q means lower affinity.", "", "The Km values differ.", "Km tells us nothing about Vmax."]),
        QUIZ("Why does the rate of an enzyme-catalysed reaction fall above the optimum temperature?",
             ["The substrate becomes more concentrated", "The enzyme is denatured and the active site loses its shape", "The activation energy increases", "The enzyme is used up"], 1,
             "High temperature breaks the weak bonds that hold the active site in shape.",
             hint="What happens to the tertiary structure when it is heated too much?",
             feedback=["The concentration does not change.", "", "Activation energy does not change, but fewer enzymes work.", "Enzymes are not used up, but they are denatured."]),
        H("Practice"),
        PQ("Define Km and state what a low Km indicates.", "Km is the substrate concentration at which the reaction rate is half of Vmax. A low Km shows a high affinity of the enzyme for its substrate."),
        PQ("An enzyme has Vmax = 50 µmol per min and Km = 2 mmol per dm3. Calculate the rate at 18 mmol per dm3.", "v = 50 × 18 / (2 + 18) = 900 / 20 = 45 µmol per min."),
        PQ("Explain why the rate of reaction increases with substrate concentration and then levels off.", "At low substrate concentration many active sites are empty, so more substrate means more enzyme-substrate complexes and a higher rate. At high concentration all active sites are occupied (saturated), so the rate cannot rise above Vmax."),
        TIP("Exam link: enzymes are in Paper 1 (graphs and factors), Paper 2 (calculations, curves and explanations) and the practical paper (experiments with catalase, amylase or protease, and design of controls). Always use the terms active site, enzyme-substrate complex and denaturation."),
        SUM("Enzymes lower activation energy through the active site (induced fit) and are not used up.",
            "Rate rises with temperature to the optimum, then falls because of denaturation. Each enzyme has an optimum pH.",
            "Vmax is the maximum rate and Km is the substrate concentration at half of Vmax. v = Vmax[S]/(Km + [S]).",
            "The curve levels off because the active sites are saturated."),
    ],
))

# ------------------------------------------------------------------ 11. Enzyme inhibition and regulation
LESSONS.append(lesson(
    module=M2,
    topic="Enzyme inhibition and regulation",
    title="Competitive and non-competitive inhibition and allosteric regulation",
    slug="bil1-enzyme-inhibition",
    minutes=24,
    summary="Inhibitors reduce enzyme activity. Compare competitive and non-competitive inhibition using curves, Vmax and Km, and explain allosteric regulation and end-product inhibition.",
    objectives=[
        "Explain competitive and non-competitive inhibition in terms of the active site",
        "Predict and interpret the effect of each inhibitor on Vmax and Km",
        "Calculate rates with and without an inhibitor",
        "Describe allosteric regulation and end-product inhibition",
    ],
    key_concepts=["Competitive inhibitor", "Non-competitive inhibitor", "Allosteric site", "Apparent Km", "End-product inhibition", "Feedback"],
    blocks=[
        H("Introduction"),
        T("Ethanol is sometimes given in hospital to a person who has swallowed methanol. Both alcohols compete for the same enzyme, alcohol dehydrogenase. "
          "If ethanol is present, less methanol is converted into toxic products. This is an example of **competitive inhibition**, and it shows how a "
          "molecule can control an enzyme without damaging it."),
        D("An **inhibitor** is a substance that reduces the rate of an enzyme-catalysed reaction. A **competitive inhibitor** has a shape similar to the substrate and "
          "binds to the active site, so the substrate cannot bind. A **non-competitive inhibitor** binds to a different place on the enzyme, the **allosteric site**, "
          "and changes the shape of the active site.", title="Definitions"),
        H("Comparing the two"),
        KEY("Competitive and non-competitive", "Learn the effect on Vmax and Km.", cards=[
            ["Competitive", "Competes with substrate for the active site. At a high substrate concentration the substrate outcompetes the inhibitor, so the same Vmax is reached. More substrate is needed to reach half of Vmax, so the apparent Km increases."],
            ["Non-competitive", "Binds at the allosteric site and distorts the active site. Raising the substrate concentration does not overcome it, because some enzyme molecules are always out of action. Vmax decreases. Km stays the same."],
        ]),
        IMG("al-bil1-inhibition-curves.svg", alt="Three rate curves: no inhibitor, competitive inhibitor with the same Vmax but a higher Km, and non-competitive inhibitor with a lower Vmax",
            caption="Figure 1. Teaching data. No inhibitor: Vmax 50, Km 2. Competitive: Vmax 50, apparent Km 5. Non-competitive: Vmax 25, Km 2."),
        T("Some textbooks also describe an **uncompetitive** inhibitor and **irreversible** inhibitors, which form permanent bonds with the enzyme. Check your textbook for the level required."),
        EX("Worked example 1: comparing rates (teaching data)", intro="Without inhibitor Vmax = 50 µmol per min and Km = 2 mmol per dm3. A competitive inhibitor raises the apparent Km to 5 mmol per dm3 and leaves Vmax unchanged. A non-competitive inhibitor halves Vmax and leaves Km at 2. Calculate the rate and the percentage inhibition at [S] = 5 mmol per dm3 for each.", steps=[
            S("No inhibitor", math=r"v = \frac{50 \times 5}{2 + 5} = 35.7"),
            S("Competitive", math=r"v = \frac{50 \times 5}{5 + 5} = 25.0"),
            S("Non-competitive", math=r"v = \frac{25 \times 5}{2 + 5} = 17.9"),
            S("Percentage inhibition", math=r"\frac{35.7 - 25.0}{35.7} \times 100 = 30\%\ \text{(competitive)};\quad \frac{35.7 - 17.9}{35.7} \times 100 = 50\%\ \text{(non-competitive)}"),
        ]),
        EX("Worked example 2: raising the substrate concentration", intro="Using the same data, compare the percentage inhibition at [S] = 50 mmol per dm3.", steps=[
            S("No inhibitor", math=r"v = \frac{50 \times 50}{2 + 50} = 48.1"),
            S("Competitive", math=r"v = \frac{50 \times 50}{5 + 50} = 45.5,\quad \frac{48.1 - 45.5}{48.1} \times 100 = 5.5\%"),
            S("Non-competitive", math=r"v = \frac{25 \times 50}{2 + 50} = 24.0,\quad \text{inhibition} = 50\%"),
            S("Conclude", text="Competitive inhibition almost disappears at a high substrate concentration. Non-competitive inhibition does not."),
        ]),
        H("Allosteric regulation and end-product inhibition"),
        T("Many enzymes in metabolic pathways have an allosteric site. A molecule that binds there changes the shape of the active site. If the shape becomes less suitable the molecule "
          "is an allosteric inhibitor. If it becomes more suitable the molecule is an allosteric activator. Enzymes with several subunits often show a **sigmoid** (S-shaped) curve of rate "
          "against substrate concentration, because binding of substrate to one subunit makes the other subunits bind more easily (cooperativity)."),
        D("**End-product inhibition** is a form of negative feedback. In a pathway $A \\rightarrow B \\rightarrow C \\rightarrow D$, the final product D binds to the allosteric site of the first enzyme "
          "and inhibits it. When D accumulates, the pathway slows down. When D is used, the inhibition is removed and the pathway speeds up again.", title="Definition"),
        MISTAKE("Saying a competitive inhibitor 'destroys' the enzyme", "The binding is usually reversible and the enzyme is not damaged. Removing the inhibitor or adding more substrate restores activity."),
        MISTAKE("Saying that a non-competitive inhibitor binds to the active site", "It binds at a different place (an allosteric site) and changes the shape of the active site."),
        QUIZ("Which graph change shows a non-competitive inhibitor?",
             ["Vmax stays the same, Km increases", "Vmax decreases, Km stays the same", "Both Vmax and Km decrease", "Vmax increases"], 1,
             "A non-competitive inhibitor puts some enzyme molecules out of action, so Vmax falls. It does not affect substrate binding in the free enzyme, so Km is unchanged.",
             hint="Can adding more substrate overcome it?",
             feedback=["That is competitive inhibition.", "", "Both falling is characteristic of uncompetitive inhibition (check your textbook).", "An inhibitor cannot increase Vmax."]),
        QUIZ("Why is end-product inhibition useful to a cell?",
             ["It makes the pathway faster when product builds up", "It stops the cell making more product than it needs", "It destroys the enzyme", "It makes substrates more concentrated"], 1,
             "It is negative feedback: when the product accumulates, it slows its own production.",
             hint="What does negative feedback do?",
             feedback=["That is the opposite.", "", "The enzyme is not destroyed.", "Substrates are not affected directly."]),
        H("Practice"),
        PQ("Explain why a competitive inhibitor does not reduce Vmax.", "At a very high substrate concentration, substrate molecules greatly outnumber the inhibitor molecules, so substrate occupies nearly all the active sites. The maximum rate is therefore the same as without inhibitor."),
        PQ("Describe and explain the effect of a non-competitive inhibitor on the rate of reaction at high substrate concentration.", "The rate is lower than without inhibitor, and Vmax is reduced. The inhibitor binds at the allosteric site and changes the shape of the active site, so some enzyme molecules cannot bind substrate. More substrate cannot overcome this."),
        PQ("Calculate the rate at [S] = 5 mmol per dm3 for an enzyme with Vmax = 25 µmol per min and Km = 2 mmol per dm3.", "v = 25 × 5 / (2 + 5) = 125 / 7 = 17.9 µmol per min."),
        TIP("Exam link: inhibition appears in Paper 1 (graph recognition) and Paper 2 (explanations, calculations and controls) and in practical planning (adding inhibitors to enzyme experiments). Name the site where the inhibitor binds and say what happens to Vmax and Km."),
        SUM("A competitive inhibitor binds the active site. Vmax is unchanged and the apparent Km increases. It can be overcome by more substrate.",
            "A non-competitive inhibitor binds an allosteric site. Vmax decreases and Km is unchanged. More substrate does not overcome it.",
            "Allosteric regulation uses binding at a site other than the active site to switch an enzyme up or down.",
            "End-product inhibition is negative feedback on the first enzyme in a pathway."),
    ],
))

# ------------------------------------------------------------------ 12. DNA and RNA structure
LESSONS.append(lesson(
    module=M3,
    topic="DNA and RNA structure",
    title="The structure of DNA and RNA",
    slug="bil1-dna-rna-structure",
    minutes=23,
    summary="Nucleotides join by phosphodiester bonds into polynucleotides. Describe the double helix with antiparallel strands and complementary base pairing, compare DNA with RNA, and use Chargaff's rules for calculations.",
    objectives=[
        "Describe the structure of a nucleotide and of a polynucleotide",
        "Describe the DNA double helix, antiparallel strands and complementary base pairing",
        "Compare DNA with mRNA, tRNA and rRNA",
        "Calculate base percentages, base-pair numbers, hydrogen bonds and lengths",
    ],
    key_concepts=["Nucleotide", "Phosphodiester bond", "Purine and pyrimidine", "Complementary base pairing", "Antiparallel", "Double helix", "mRNA, tRNA and rRNA"],
    blocks=[
        H("Introduction"),
        T("Every person in a family in Bamenda carries a copy of the same instructions in a molecule far too thin to see. In a human cell about two metres of DNA fit into a nucleus a few micrometres across. "
          "The way DNA is built explains how it stores information, how it can be copied and why it is so stable."),
        D("A **nucleotide** has three parts: a pentose sugar (deoxyribose in DNA, ribose in RNA), a phosphate group and a nitrogen-containing base. "
          "Nucleotides join by **phosphodiester bonds** between the phosphate of one nucleotide and the sugar of the next, in a condensation reaction, to form a **polynucleotide**.", title="Definitions"),
        KEY("The bases", "Four in DNA; one difference in RNA.", cards=[
            ["Purines (two rings)", "Adenine (A) and guanine (G)."],
            ["Pyrimidines (one ring)", "Cytosine (C) and thymine (T). In RNA, uracil (U) replaces thymine."],
        ]),
        IMG("al-bil1-dna-structure.svg", alt="DNA double helix drawn as a ladder with two sugar-phosphate backbones, base pairs and hydrogen bonds, strands running in opposite directions",
            caption="Figure 1. DNA (ladder form). The strands are antiparallel: one runs 5' to 3' downwards and the other 3' to 5'."),
        H("The double helix"),
        T("A DNA molecule has two polynucleotide strands wound around each other as a **double helix**. The sugar-phosphate backbones are on the outside. The bases point inwards and "
          "pair by **hydrogen bonds**: adenine pairs with thymine (two hydrogen bonds) and guanine pairs with cytosine (three hydrogen bonds). This is **complementary base pairing**. "
          "A purine always pairs with a pyrimidine, so the width of the helix is constant."),
        T("The two strands are **antiparallel**. One runs from the 5' end (a free phosphate on carbon 5') to the 3' end (a free hydroxyl on carbon 3'), and the other runs in the opposite direction. "
          "The helix makes one full turn every 3.4 nm, which is 10 base pairs, so the distance between neighbouring base pairs is 0.34 nm."),
        KEY("Why DNA is a good store of information", "Link structure to function.", cards=[
            ["Stable", "Many hydrogen bonds hold the strands, and the bases are protected inside the backbone."],
            ["Can be copied", "Complementary base pairing allows each strand to act as a template."],
            ["Very large", "A long molecule can carry a great amount of information in the sequence of bases."],
            ["Information can be read", "The strands can be separated, because hydrogen bonds are weak, to allow access to the sequence."],
        ]),
        H("RNA"),
        CODE("""Feature        DNA                          RNA
Sugar          deoxyribose                  ribose
Bases          A, T, G, C                   A, U, G, C
Strands        two (double helix)           usually one
Length         very long                    short
Types          one main type                mRNA, tRNA, rRNA
Location       nucleus (also mitochondria)  made in nucleus, works mainly
                                            in cytoplasm""", "text", title="Table 1. DNA compared with RNA"),
        T("**Messenger RNA (mRNA)** carries a copy of a gene to the ribosomes. **Transfer RNA (tRNA)** is a folded single strand that carries an amino acid and has an anticodon. "
          "**Ribosomal RNA (rRNA)** is part of the structure of ribosomes."),
        EX("Worked example 1: Chargaff's rules", intro="In a sample of double-stranded DNA, thymine makes up 22% of the bases. Calculate the percentages of the other three bases.", steps=[
            S("Apply A = T", text="Adenine pairs with thymine, so A = 22%."),
            S("Remaining bases", math=r"100 - (22 + 22) = 56\%"),
            S("Apply G = C", math=r"\text{G} = \text{C} = \frac{56}{2} = 28\%"),
        ], check=r"22 + 22 + 28 + 28 = 100"),
        EX("Worked example 2: a DNA fragment", intro="A DNA fragment is 1000 base pairs long (2000 nucleotides) and 28% of its bases are adenine. Calculate the number of each base, the number of hydrogen bonds and the length of the fragment (0.34 nm per base pair).", steps=[
            S("Adenine", math=r"0.28 \times 2000 = 560"),
            S("Thymine", text="T = A = 560."),
            S("Guanine and cytosine", math=r"\frac{2000 - 2 \times 560}{2} = 440\ \text{each}"),
            S("Hydrogen bonds", math=r"560 \times 2 + 440 \times 3 = 1120 + 1320 = 2440"),
            S("Length", math=r"1000 \times 0.34 = 340\ \text{nm}"),
        ]),
        MISTAKE("Saying that A pairs with U in DNA", "Uracil is found only in RNA. In DNA, A pairs with T."),
        MISTAKE("Saying hydrogen bonds join nucleotides in the same strand", "Phosphodiester bonds join the nucleotides in a strand. Hydrogen bonds join the two strands."),
        QUIZ("A DNA sample has 30% adenine. What is the percentage of guanine?",
             ["30%", "20%", "40%", "70%"], 1,
             "A = T = 30%, so G + C = 40%, and G = C = 20%.",
             hint="Work out T first, then share the remainder.",
             feedback=["That is the percentage of thymine.", "", "That is G + C together.", "That is not possible, because A + T is already 60%."]),
        QUIZ("Which is a difference between DNA and mRNA?",
             ["mRNA contains deoxyribose", "mRNA contains uracil instead of thymine", "mRNA is double stranded", "mRNA is longer than DNA"], 1,
             "RNA has ribose and uracil. It is usually single stranded and much shorter.",
             hint="Think about the bases.",
             feedback=["DNA contains deoxyribose.", "", "mRNA is single stranded.", "DNA molecules are much longer."]),
        H("Practice"),
        PQ("Describe how two nucleotides are joined in a polynucleotide.", "A condensation reaction forms a phosphodiester bond between the phosphate group on the 5' carbon of one nucleotide and the hydroxyl on the 3' carbon of the sugar of the other nucleotide. A water molecule is released."),
        PQ("Explain why a purine always pairs with a pyrimidine in DNA.", "A purine has two rings and a pyrimidine has one, so a pair has three rings and fits the constant width of the double helix. Two purines would be too wide and two pyrimidines too narrow for hydrogen bonds to form."),
        PQ("A fragment of DNA of 500 base pairs contains 150 guanine bases. How many adenine bases does it contain?", "G = C = 150, so G + C = 300. The total number of bases is 1000, so A + T = 700 and A = 350."),
        TIP("Exam link: nucleic acids appear in Paper 1 (base pairing, calculations) and Paper 2 (structure and function, comparing DNA and RNA). Do not call the strands 'parallel', and always name the type of bond: phosphodiester within a strand, hydrogen between strands."),
        SUM("A nucleotide has a pentose sugar, a phosphate and a base. Phosphodiester bonds join nucleotides.",
            "DNA is a double helix of antiparallel strands. A pairs with T (2 hydrogen bonds), G pairs with C (3 hydrogen bonds).",
            "RNA has ribose, uracil and is usually single stranded. There are mRNA, tRNA and rRNA.",
            "Chargaff's rules: A = T and G = C in double-stranded DNA."),
    ],
))

# ------------------------------------------------------------------ 13. DNA replication
LESSONS.append(lesson(
    module=M3,
    topic="DNA replication",
    title="Semi-conservative replication and the Meselson-Stahl experiment",
    slug="bil1-dna-replication",
    minutes=24,
    summary="DNA replicates semi-conservatively. Describe the roles of helicase and DNA polymerase, the leading and lagging strands, and interpret the Meselson-Stahl results with calculations of band proportions.",
    objectives=[
        "State that replication is semi-conservative and explain the meaning",
        "Describe the roles of helicase, primase, DNA polymerase and ligase at the replication fork",
        "Explain the leading and lagging strands and Okazaki fragments",
        "Interpret the Meselson-Stahl experiment and calculate the proportions of DNA types in each generation",
    ],
    key_concepts=["Semi-conservative", "Helicase", "DNA polymerase", "Leading strand", "Lagging strand", "Okazaki fragment", "Meselson-Stahl"],
    blocks=[
        H("Introduction"),
        T("Every cell division in a growing child needs a complete, accurate copy of all the DNA. In 1958, Meselson and Stahl showed how the copy is made. They grew bacteria in a medium with heavy nitrogen "
          "(15N) and followed the heavy DNA through later generations. Their result is a classic piece of reasoning from data."),
        D("In **semi-conservative replication** each new DNA molecule has one original (parent) strand and one newly made strand.", title="Definition"),
        H("The mechanism"),
        KEY("Enzymes at the replication fork", "Know the order and the jobs.", cards=[
            ["Helicase", "Unwinds the double helix and breaks the hydrogen bonds between the bases, making two template strands."],
            ["Primase", "Makes a short RNA primer, which gives DNA polymerase a 3' end to start from."],
            ["DNA polymerase", "Adds free nucleotides to the 3' end of a growing strand, matching them by complementary base pairing. It works only in the 5' to 3' direction."],
            ["DNA ligase", "Joins the fragments of the lagging strand by forming phosphodiester bonds."],
        ]),
        IMG("al-bil1-replication-fork.svg", alt="Replication fork with helicase, a continuous leading strand and a lagging strand made of Okazaki fragments with RNA primers",
            caption="Figure 1. A replication fork moving to the right. The leading strand is made continuously towards the fork. The lagging strand is made in fragments away from the fork."),
        T("Because the strands are antiparallel and DNA polymerase works only from 5' to 3', the two new strands are made differently. On one template, the **leading strand** is made continuously, in the same direction as the fork moves. "
          "On the other template, the **lagging strand** is made in short pieces called **Okazaki fragments**, each one starting with a new primer and made away from the fork. DNA ligase later joins the fragments."),
        H("The Meselson-Stahl experiment"),
        T("Bacteria were grown for many generations in a medium with 15N, so that all their DNA was heavy (15N/15N). They were then moved to a medium with ordinary nitrogen (14N) and left to divide. DNA from each generation was spun in a "
          "centrifuge in a density gradient. Heavy DNA settles lower than light DNA, and hybrid DNA settles between."),
        IMG("al-bil1-meselson-stahl.svg", alt="Four centrifuge tubes showing a heavy band at the start, a hybrid band in the first generation, hybrid and light bands in equal amounts in the second, and a thin hybrid and thick light band in the third",
            caption="Figure 2. Results of the Meselson-Stahl experiment."),
        KEY("Reading the results", "Each model predicts something different.", cards=[
            ["Semi-conservative", "Generation 1: all hybrid (15N/14N). Generation 2: half hybrid, half light. This is what was found."],
            ["Conservative", "Generation 1 would be half heavy and half light with no hybrid band. This was not found."],
            ["Dispersive", "Every generation would give a single band, with density getting lighter each time. Generation 2 would not show a light band and a hybrid band separately, so it was also rejected."],
        ]),
        EX("Worked example 1: proportions", intro="Calculate the proportion of hybrid and light DNA molecules after 3 generations in 14N.", steps=[
            S("Number of DNA molecules", math=r"2^3 = 8"),
            S("Hybrid molecules", text="Only the two original 15N strands are conserved, so only 2 molecules are hybrid."),
            S("Fractions", math=r"\frac{2}{8} = 25\%\ \text{hybrid},\quad \frac{6}{8} = 75\%\ \text{light}"),
            S("General rule", math=r"\text{hybrid} = \frac{2}{2^n} = 2^{1-n}"),
        ], check=r"25\% + 75\% = 100\%"),
        EX("Worked example 2: strands", intro="How many strands containing 15N are there after 5 generations in 14N, and what fraction of all strands is this?", steps=[
            S("Total strands", math=r"2 \times 2^5 = 64"),
            S("Strands with 15N", text="The two original strands are never replaced. Every new strand is made of 14N."),
            S("Fraction", math=r"\frac{2}{64} = \frac{1}{32} = 3.1\%"),
        ]),
        EX("Worked example 3: replication time (teaching data)", intro="A bacterial chromosome has 4.6 million base pairs. Two forks move away from one origin at 1000 nucleotides per second each. Estimate the time to copy it.", steps=[
            S("Combined speed", math=r"2 \times 1000 = 2000\ \text{nucleotides per second}"),
            S("Time", math=r"\frac{4\,600\,000}{2000} = 2300\ \text{s}"),
            S("In minutes", math=r"\frac{2300}{60} = 38\ \text{min}"),
        ]),
        MISTAKE("Saying the new DNA is 'half old and half new' without saying it is half of each molecule", "Each new molecule has one old strand and one new strand. It is not half of the molecules old and half new."),
        MISTAKE("Saying DNA polymerase adds nucleotides to the 5' end", "It adds to the 3' end, so strands grow from 5' to 3'."),
        QUIZ("In the Meselson-Stahl experiment, why did the first generation produce only one band, at a position between heavy and light?",
             ["All the DNA was light", "All the DNA molecules were hybrid, with one old (15N) strand and one new (14N) strand", "The DNA was dispersed in fragments", "The DNA was not replicated"], 1,
             "Semi-conservative replication gives hybrid molecules, with one heavy strand and one light strand.",
             hint="Each new molecule has one parent strand.",
             feedback=["The old strands are still heavy.", "", "That is the dispersive model, which does not fit later generations.", "The cells had divided."]),
        QUIZ("Which enzyme joins Okazaki fragments?",
             ["DNA polymerase", "Helicase", "DNA ligase", "Primase"], 2,
             "DNA ligase makes phosphodiester bonds between fragments.",
             hint="It 'ligates', which means ties together.",
             feedback=["DNA polymerase adds nucleotides.", "Helicase unwinds DNA.", "", "Primase makes the RNA primer."]),
        H("Practice"),
        PQ("Describe what happens at the replication fork.", "Helicase unwinds the DNA and breaks hydrogen bonds. Primase makes RNA primers. DNA polymerase adds nucleotides to the 3' end of each primer by complementary base pairing, making a continuous leading strand and a lagging strand in fragments, which ligase joins."),
        PQ("Explain why the lagging strand is made in fragments.", "DNA polymerase can add nucleotides only to the 3' end, so it can only work from 5' to 3'. On the lagging strand this is away from the fork, so the polymerase makes a short fragment, and each new section of template opened by the fork needs a new primer."),
        PQ("After 4 generations in 14N, what percentage of DNA molecules in a Meselson-Stahl experiment is hybrid?", "Number of molecules = 2⁴ = 16. Hybrid molecules = 2. The percentage is 2/16 × 100 = 12.5%."),
        TIP("Exam link: replication appears in Paper 1 (enzymes, Meselson-Stahl) and Paper 2 (describing the mechanism and interpreting the experiment with calculations). Use the terms 3' end, template, complementary base pairing and name each enzyme with its job."),
        SUM("Replication is semi-conservative: each new molecule has one old and one new strand.",
            "Helicase unwinds, primase makes primers, DNA polymerase adds nucleotides to the 3' end, and ligase joins the fragments.",
            "The leading strand is continuous. The lagging strand is made in Okazaki fragments.",
            "Meselson and Stahl found: generation 1 all hybrid, generation 2 half hybrid and half light. After n generations hybrid = 2/2^n."),
    ],
))

# ------------------------------------------------------------------ 14. Genetic code and transcription
LESSONS.append(lesson(
    module=M3,
    topic="The genetic code, transcription and translation",
    title="The genetic code and transcription",
    slug="bil1-genetic-code-transcription",
    minutes=23,
    summary="A gene is a sequence of bases that codes for a polypeptide. Describe the features of the triplet code, how RNA polymerase makes mRNA from the template strand, and how eukaryotic mRNA is processed.",
    objectives=[
        "Define gene, codon and the genetic code and state its features",
        "Describe transcription, naming the template strand, RNA polymerase and the direction of synthesis",
        "Write the mRNA sequence from a DNA template and state the amino acids using a codon table",
        "Describe the processing of eukaryotic pre-mRNA (capping, tailing and splicing)",
    ],
    key_concepts=["Gene", "Triplet code", "Codon", "Degenerate", "Template strand", "RNA polymerase", "Intron and exon", "Splicing"],
    blocks=[
        H("Introduction"),
        T("Two sisters in Limbe have different blood groups, and a farmer's maize can be resistant to a disease while his neighbour's is not. Differences like these come from differences "
          "in genes. A gene is not a mystery: it is a sequence of bases, and cells read it in a fixed way."),
        D("A **gene** is a length of DNA that codes for a polypeptide (or a functional RNA). The **genetic code** is the set of rules by which the sequence of bases in DNA (and mRNA) "
          "is translated into the sequence of amino acids in a polypeptide. A **codon** is a triplet of bases on mRNA that codes for one amino acid or a signal.", title="Definitions"),
        KEY("Features of the genetic code", "Learn all five.", cards=[
            ["Triplet", "Three bases code for one amino acid. With four bases, there are 4 × 4 × 4 = 64 possible triplets, enough for 20 amino acids."],
            ["Degenerate", "Most amino acids are coded for by more than one codon. 61 codons code for amino acids and 3 are stop codons."],
            ["Non-overlapping", "Each base is part of only one codon, and the message is read in order from a fixed start."],
            ["Universal", "Almost all organisms use the same code, with a few small exceptions."],
            ["Start and stop", "AUG codes for methionine and is the usual start codon. UAA, UAG and UGA are stop codons and code for no amino acid."],
        ]),
        CODE("""Part of the mRNA codon table (standard code)
AUG  Met (start)      CCA  Pro         GAA  Glu
GCU  Ala              AAA  Lys         GAC  Asp
UUU  Phe              UGG  Trp         GUG  Val
GGU  Gly              GAG  Glu         UAA, UAG, UGA  stop""", "text", title="Table 1. Some codons"),
        H("Transcription"),
        D("**Transcription** is the making of an mRNA molecule from a DNA gene. Only one of the two DNA strands, the **template strand**, is copied. "
          "The mRNA has the same sequence as the other strand (the coding strand), with uracil in place of thymine.", title="Definition"),
        KEY("Steps in transcription", "In the nucleus of a eukaryote.", cards=[
            ["1", "The enzyme RNA polymerase binds to the start of the gene (the promoter). The DNA double helix unwinds and the hydrogen bonds break over a short section."],
            ["2", "RNA nucleotides line up opposite the template strand by complementary base pairing: A with U, T with A, C with G, G with C."],
            ["3", "RNA polymerase joins the nucleotides by phosphodiester bonds, adding them to the 3' end, so the mRNA grows 5' to 3'."],
            ["4", "At the end of the gene, the mRNA is released and the DNA closes up."],
        ]),
        T("In eukaryotes, the first RNA made is **pre-mRNA**. It contains **exons** (parts that code) and **introns** (non-coding sequences). Before it leaves the nucleus, the introns are cut out and the exons are joined: this is **splicing**. "
          "A cap is added to the 5' end and a tail of many adenine nucleotides (the poly-A tail) is added to the 3' end. The mature mRNA then leaves through a nuclear pore. Prokaryotes have no introns and no nucleus, so translation can start while transcription is still going on."),
        EX("Worked example 1: from DNA to mRNA to amino acids", intro="The template strand of part of a gene is 3'-TAC GGT CTT ATT-5'. Write the mRNA and the amino acids using Table 1.", steps=[
            S("Complementary RNA bases", text="A pairs with U, T with A, G with C and C with G."),
            S("Pair each base", math=r"\text{TAC GGT CTT ATT} \rightarrow \text{AUG CCA GAA UAA}"),
            S("Write the mRNA with its ends", text="5'-AUG CCA GAA UAA-3'."),
            S("Translate", text="AUG = Met, CCA = Pro, GAA = Glu, UAA = stop. The polypeptide is Met-Pro-Glu."),
        ]),
        EX("Worked example 2: gene length", intro="The coding region of an mRNA has 927 nucleotides, including the stop codon. How many amino acids are in the polypeptide?", steps=[
            S("Codons", math=r"\frac{927}{3} = 309\ \text{codons}"),
            S("Remove the stop codon", math=r"309 - 1 = 308\ \text{amino acids}"),
        ], check=r"(308 + 1) \times 3 = 927"),
        EX("Worked example 3: an intron (teaching data)", intro="A gene has 3000 nucleotides in the section transcribed. Two introns of 600 and 400 nucleotides are removed. How long is the spliced coding message (ignoring the cap and tail)?", steps=[
            S("Subtract the introns", math=r"3000 - 600 - 400 = 2000"),
            S("Comment", text="The mature mRNA is shorter than the gene. This is why a gene in eukaryotes is longer than the message that is translated."),
        ]),
        MISTAKE("Writing T in mRNA", "RNA has uracil, not thymine. Write A, U, G and C."),
        MISTAKE("Mixing up the template strand with the mRNA", "The mRNA is complementary to the template strand, so it has the same sequence as the coding strand (with U for T)."),
        QUIZ("Which statement describes the genetic code as degenerate?",
             ["Each codon codes for more than one amino acid", "Most amino acids are coded for by more than one codon", "Codons overlap", "It is different in every species"], 1,
             "There are 64 codons and only 20 amino acids, so most amino acids have several codons.",
             hint="Compare 64 codons with 20 amino acids.",
             feedback=["That would be ambiguous. Each codon codes for only one amino acid.", "", "The code is non-overlapping.", "The code is almost universal."]),
        QUIZ("What is the mRNA sequence made from the template strand 3'-TAC-5'?",
             ["5'-UAC-3'", "5'-AUG-3'", "5'-ATG-3'", "5'-TAC-3'"], 1,
             "A pairs with U (from T), T with A, and C with G: AUG.",
             hint="Pair each base, remembering that RNA has uracil.",
             feedback=["This copies the template without pairing.", "", "RNA does not contain thymine.", "This writes the template again."]),
        H("Practice"),
        PQ("Describe how mRNA is made in transcription.", "RNA polymerase binds to the start of the gene and unwinds the DNA. RNA nucleotides pair with the bases of the template strand by complementary base pairing, and RNA polymerase joins them by phosphodiester bonds, adding to the 3' end. The mRNA is released at the end of the gene."),
        PQ("Explain why the code must be a triplet code.", "There are 20 amino acids. A code of one base could specify only 4 and a code of two bases only 16 (4²). A triplet code gives 64 (4³) codons, enough for all 20 amino acids and stop signals."),
        PQ("State two ways in which pre-mRNA is processed before it leaves the nucleus.", "Introns are removed and exons joined (splicing), a cap is added at the 5' end, and a poly-A tail is added at the 3' end."),
        TIP("Exam link: transcription and the code appear in Paper 1 (writing mRNA, codon tables) and Paper 2 (describing transcription, explaining the features of the code, eukaryote and prokaryote differences). Always state the direction (5' to 3') and the enzyme."),
        SUM("A gene is a sequence of DNA bases that codes for a polypeptide. The code is a triplet, degenerate, non-overlapping and almost universal.",
            "Transcription: RNA polymerase copies the template strand into mRNA by complementary base pairing, 5' to 3'.",
            "Eukaryotic pre-mRNA has introns removed, a cap and a poly-A tail added.",
            "Number of amino acids = (number of coding nucleotides ÷ 3) − 1 stop codon."),
    ],
))

# ------------------------------------------------------------------ 15. Translation and mutations
LESSONS.append(lesson(
    module=M3,
    topic="The genetic code, transcription and translation",
    title="Translation and the effect of mutations",
    slug="bil1-translation-mutations",
    minutes=24,
    summary="Ribosomes read mRNA codon by codon, using tRNA to bring amino acids. Describe initiation, elongation and termination, and predict the effects of substitution, insertion and deletion mutations.",
    objectives=[
        "Describe the structure and role of tRNA and the parts of a ribosome used in translation",
        "Describe initiation, elongation and termination",
        "Translate an mRNA sequence using a codon table",
        "Predict the effects of silent, missense and nonsense substitutions and of frameshift mutations",
    ],
    key_concepts=["tRNA", "Anticodon", "Ribosome", "A site and P site", "Initiation", "Elongation", "Termination", "Point mutation", "Frameshift"],
    blocks=[
        H("Introduction"),
        T("Insulin made by bacteria is used by people with diabetes. The bacteria read a human gene and make human insulin, because every living cell reads mRNA with the same code. "
          "The reading is called translation, and it happens on ribosomes in the cytoplasm."),
        D("**Translation** is the making of a polypeptide at a ribosome, using the sequence of codons on mRNA. A **transfer RNA (tRNA)** is a folded single strand of RNA with an **anticodon** at one end and an "
          "amino acid attachment site at the other. The anticodon is complementary to the codon.", title="Definitions"),
        IMG("al-bil1-translation.svg", alt="Ribosome with large and small subunits on an mRNA strand, two tRNAs with anticodons, and a growing polypeptide chain",
            caption="Figure 1. Translation. The tRNA on the left (P site) carries the growing chain. The tRNA on the right (A site) brings the next amino acid."),
        H("Stages of translation"),
        KEY("Three stages", "Know what happens at each.", cards=[
            ["Initiation", "The small ribosomal subunit binds to the mRNA at the start codon AUG. A tRNA carrying methionine, with the anticodon UAC, pairs with AUG. The large subunit joins."],
            ["Elongation", "A tRNA with the matching anticodon enters the A site. A peptide bond forms between the amino acid in the A site and the polypeptide on the tRNA in the P site, a reaction catalysed by the ribosome. The ribosome then moves one codon along the mRNA (translocation), so the tRNA that has lost its chain leaves and the next codon moves into the A site."],
            ["Termination", "A stop codon (UAA, UAG or UGA) reaches the A site. No tRNA matches it. A release factor binds, the polypeptide is released and the ribosome subunits separate."],
        ]),
        T("Energy from ATP and GTP is needed to attach each amino acid to its tRNA and to move the ribosome. Many ribosomes can read one mRNA at the same time. The group is called a **polysome**, and it makes many copies of the polypeptide quickly. "
          "Proteins for export are made on ribosomes attached to the rough ER."),
        H("Mutations"),
        D("A **mutation** is a change in the sequence of bases in DNA. A **point mutation** changes one base. **Insertion** and **deletion** add or remove bases.", title="Definition"),
        KEY("Effects of point mutations on the polypeptide", "Compare with the original sequence AUG CCA GAA UAA (Met-Pro-Glu).", cards=[
            ["Silent", "The new codon codes for the same amino acid because the code is degenerate. CCA to CCG still codes for Pro."],
            ["Missense", "The new codon codes for a different amino acid. GAA to GUA changes Glu to Val. In sickle cell haemoglobin, GAG changes to GUG in the mRNA, so Glu becomes Val."],
            ["Nonsense", "The new codon is a stop codon, so the polypeptide is shorter. GAA to UAA gives Met-Pro only."],
            ["Frameshift", "Insertion or deletion of a number of bases that is not a multiple of three changes every codon after the change. Deleting the first C of CCA gives AUG CAG AAU AAG GCU UAA and a very different polypeptide (Met-Gln-Asn-Lys-Ala) if the mRNA continues."],
        ]),
        EX("Worked example 1: translating an mRNA", intro="Translate the mRNA 5'-AUG CCA GAA UAA-3' and write the anticodon of each tRNA that is used.", steps=[
            S("Read the codons", text="AUG, CCA, GAA, UAA."),
            S("Amino acids", text="Met, Pro, Glu, stop. The polypeptide is Met-Pro-Glu."),
            S("Anticodons (complementary, written 3' to 5')", math=r"\text{AUG} \rightarrow \text{UAC};\ \text{CCA} \rightarrow \text{GGU};\ \text{GAA} \rightarrow \text{CUU}"),
            S("Note", text="UAA has no tRNA. It is read by a release factor."),
        ]),
        EX("Worked example 2: classify mutations", intro="The mRNA 5'-AUG CCA GAA UAA-3' mutates in three different ways: (a) CCA becomes CCG, (b) GAA becomes GUA, (c) GAA becomes UAA. Describe the effect of each.", steps=[
            S("(a)", text="CCG still codes for Pro. This is a silent mutation and the polypeptide is Met-Pro-Glu."),
            S("(b)", text="GUA codes for Val. This is a missense mutation, giving Met-Pro-Val."),
            S("(c)", text="UAA is a stop codon. This is a nonsense mutation, giving Met-Pro."),
        ]),
        EX("Worked example 3: counting nucleotides", intro="A polypeptide has 250 amino acids. What is the minimum number of nucleotides in the coding region of the mRNA, including the stop codon?", steps=[
            S("Codons for amino acids", math=r"250"),
            S("Add the stop codon", math=r"250 + 1 = 251"),
            S("Nucleotides", math=r"251 \times 3 = 753"),
        ]),
        MISTAKE("Saying the anticodon is on the mRNA", "The codon is on mRNA. The anticodon is on tRNA and is complementary to the codon."),
        MISTAKE("Saying that a frameshift always changes only one amino acid", "A frameshift changes every codon after the mutation, so the polypeptide is usually completely different from that point."),
        QUIZ("A tRNA has the anticodon GGU. Which mRNA codon does it pair with?",
             ["CCA", "GGU", "CCU", "AGG"], 0,
             "Anticodon GGU pairs with CCA (G with C, G with C, U with A).",
             hint="Pair each base: G with C and U with A.",
             feedback=["", "This is the anticodon itself.", "The last base U would pair with A, not U.", "This does not pair with the anticodon."]),
        QUIZ("Which type of mutation is most likely to have no effect on the polypeptide?",
             ["Nonsense", "Frameshift", "Silent", "Deletion of one base"], 2,
             "A silent mutation changes the codon but not the amino acid, because the code is degenerate.",
             hint="Which one keeps the same amino acid?",
             feedback=["A nonsense mutation shortens the polypeptide.", "A frameshift changes many codons.", "", "A single deletion causes a frameshift."]),
        H("Practice"),
        PQ("Describe the role of tRNA in translation.", "A tRNA carries a specific amino acid to the ribosome. Its anticodon pairs with the complementary codon on the mRNA, so the amino acids are placed in the order decided by the mRNA."),
        PQ("Explain why a deletion of three bases may have less effect than a deletion of one base.", "Deleting three bases removes one codon (or changes two codons) but keeps the reading frame for the rest of the mRNA, so only one amino acid is lost or changed. Deleting one base shifts the reading frame and changes all later codons."),
        PQ("A mutation changes the mRNA codon GAG to GUG. State the type of mutation and its effect on the polypeptide.", "It is a missense point mutation. Glutamic acid is replaced by valine. In haemoglobin this change causes sickle cell anaemia."),
        TIP("Exam link: translation and mutations are tested in Paper 1 (codon tables, anticodons) and Paper 2 (describing initiation, elongation and termination, and explaining the effects of mutations). Name the codon, the anticodon and the site (A or P) in your description."),
        SUM("Translation takes place on ribosomes. Each tRNA carries an amino acid and has an anticodon complementary to the mRNA codon.",
            "Initiation at AUG, elongation with peptide bonds and movement of the ribosome, termination at a stop codon.",
            "Silent, missense and nonsense are point mutations. Frameshift mutations come from insertions or deletions that are not multiples of three.",
            "The degenerate code reduces the effect of some mutations."),
    ],
))

# ------------------------------------------------------------------ 16. Cell cycle and mitosis
LESSONS.append(lesson(
    module=M3,
    topic="The cell cycle and mitosis",
    title="The cell cycle and the stages of mitosis",
    slug="bil1-cell-cycle-mitosis",
    minutes=24,
    summary="The cell cycle has interphase (G1, S, G2) and mitosis. Describe the stages of mitosis, count chromosomes and chromatids, and calculate the mitotic index and the duration of each stage from root-tip counts.",
    objectives=[
        "Describe the phases of the cell cycle and its checkpoints",
        "Describe the events of prophase, metaphase, anaphase and telophase and cytokinesis",
        "State the number of chromosomes and chromatids at each stage",
        "Calculate the mitotic index and the time spent in each stage from cell counts",
    ],
    key_concepts=["Cell cycle", "Interphase", "Chromatid", "Centromere", "Spindle", "Mitosis", "Cytokinesis", "Mitotic index"],
    blocks=[
        H("Introduction"),
        T("A cut on your hand heals within days because skin cells divide to replace the lost cells. In a cocoa farm, the growing tip of a root makes new cells all the time. "
          "Both processes use **mitosis**, which makes two daughter cells that have exactly the same chromosomes as the parent cell."),
        D("The **cell cycle** is the sequence of events from the formation of a cell to its own division. It has **interphase** (when the cell grows and copies its DNA) and the **mitotic phase**, "
          "which includes mitosis (division of the nucleus) and cytokinesis (division of the cytoplasm).", title="Definition"),
        KEY("Phases of interphase", "Most of the cycle is interphase.", cards=[
            ["G1 (first gap)", "The cell grows, makes proteins and organelles. A checkpoint at the end checks that the cell is large enough and the DNA is undamaged."],
            ["S (synthesis)", "DNA is replicated. Each chromosome now has two identical sister chromatids joined at the centromere."],
            ["G2 (second gap)", "The cell makes proteins needed for division. A checkpoint checks that all the DNA has been copied correctly."],
        ]),
        T("A third checkpoint, in metaphase, makes sure that all chromosomes are attached to the spindle before the chromatids are pulled apart. Cells that do not divide, such as mature nerve cells, leave the cycle in a resting state called G0. "
          "Cancer happens when cells ignore these controls and divide without stopping."),
        H("The stages of mitosis"),
        IMG("al-bil1-mitosis-stages.svg", alt="Four cells showing prophase, metaphase, anaphase and telophase of mitosis in a cell with four chromosomes",
            caption="Figure 1. Mitosis in an animal cell with four chromosomes (2n = 4)."),
        KEY("What happens", "Learn the order: PMAT.", cards=[
            ["Prophase", "Chromosomes condense and become visible, each made of two chromatids. The nucleolus disappears and the nuclear envelope breaks down. Centrioles move to the poles and spindle fibres begin to form."],
            ["Metaphase", "Chromosomes line up on the equator of the cell, each attached to spindle fibres by its centromere."],
            ["Anaphase", "The centromeres divide. The spindle fibres shorten and pull the sister chromatids (now called chromosomes) to opposite poles. Mitochondria supply ATP."],
            ["Telophase", "Chromosomes reach the poles and uncoil. Nuclear envelopes re-form around each group. The spindle breaks down."],
            ["Cytokinesis", "In animal cells, a cleavage furrow pinches the cell in two. In plant cells, vesicles form a cell plate across the middle, which becomes a new cell wall."],
        ]),
        T("Mitosis produces two **genetically identical** daughter cells. It is used for growth, tissue repair, replacement of cells and asexual reproduction."),
        CODE("""Stage            Chromosomes     Chromatids      DNA molecules
                 (human cell)    (human cell)    (per cell)
G1               46              46              46
After S phase    46              92              46 -> 92 (each chromosome
(G2, prophase,                                   has two double helices)
 metaphase)      46              92
Anaphase         92              92              92
After mitosis    46 in each      46 in each      46 in each
(each daughter)  daughter cell   daughter cell   daughter cell""", "text", title="Table 1. Counting chromosomes and chromatids in a human cell (2n = 46)"),
        H("Counting cells: the mitotic index"),
        D("The **mitotic index** is the proportion of cells in a tissue that are undergoing mitosis.", title="Definition",
          formula=r"\text{mitotic index} = \frac{\text{number of cells in mitosis}}{\text{total number of cells}} \times 100\%"),
        EX("Worked example 1: mitotic index (teaching data)", intro="In a root-tip squash, 250 cells were counted: 190 in interphase, 36 in prophase, 8 in metaphase, 6 in anaphase and 10 in telophase. Calculate the mitotic index.", steps=[
            S("Cells in mitosis", math=r"36 + 8 + 6 + 10 = 60"),
            S("Divide by the total", math=r"\frac{60}{250} \times 100 = 24\%"),
        ], check=r"190 + 60 = 250"),
        EX("Worked example 2: time spent in each stage", intro="The whole cell cycle in these root-tip cells takes 20 hours. Use the counts above to estimate the time spent in prophase and in metaphase.", steps=[
            S("The idea", text="The fraction of cells seen in a stage is about equal to the fraction of the cycle time that the stage lasts."),
            S("Prophase", math=r"\frac{36}{250} \times 20 = 2.88\ \text{h}"),
            S("Metaphase", math=r"\frac{8}{250} \times 20 = 0.64\ \text{h} = 38\ \text{minutes}"),
            S("Conclude", text="Prophase is the longest stage of mitosis in this sample. Metaphase is the shortest."),
        ]),
        TIP("In the practical, squash the root tip in warm hydrochloric acid and stain it (for example with acetic orcein) so the chromosomes are visible. Count at least 100 to 200 cells in several fields of view to make the estimate reliable."),
        MISTAKE("Saying that the chromosome number doubles in S phase", "The number of chromosomes stays the same in S phase. The DNA is copied so each chromosome has two chromatids. The chromosome number doubles only briefly in anaphase."),
        MISTAKE("Calling the nuclear division 'cell division'", "Mitosis is nuclear division. Cell division also needs cytokinesis."),
        QUIZ("A human cell has 46 chromosomes in G1. How many chromatids are present in the same cell in metaphase?",
             ["23", "46", "92", "184"], 2,
             "After S phase each chromosome has two chromatids: 46 × 2 = 92.",
             hint="What happens to each chromosome in S phase?",
             feedback=["This is the number in a gamete.", "This is the number of chromosomes, not chromatids.", "", "This is double the correct number."]),
        QUIZ("In which stage of mitosis do the sister chromatids separate?",
             ["Prophase", "Metaphase", "Anaphase", "Telophase"], 2,
             "The centromeres divide in anaphase, and spindle fibres pull the chromatids apart.",
             hint="Which stage shows V-shaped chromosomes moving to the poles?",
             feedback=["Chromosomes condense in prophase.", "Chromosomes line up in metaphase.", "", "Nuclear envelopes re-form in telophase."]),
        H("Practice"),
        PQ("Describe what happens to the chromosomes during metaphase and anaphase.", "In metaphase the chromosomes line up on the equator, attached to spindle fibres at their centromeres. In anaphase the centromeres divide and the spindle fibres shorten, pulling the sister chromatids to opposite poles."),
        PQ("In a sample of 200 cells from an onion root tip, 30 are in mitosis. Calculate the mitotic index and suggest why it is higher in a root tip than in a mature leaf.", "Mitotic index = 30/200 × 100 = 15%. A root tip contains meristem cells that divide to make the root grow, but mature leaf cells have stopped dividing."),
        PQ("Explain why the daughter cells made by mitosis are genetically identical.", "DNA is replicated in S phase by semi-conservative replication, so each chromosome has two identical chromatids. In anaphase one chromatid of each chromosome goes to each pole, so each daughter nucleus receives one copy of every chromosome."),
        TIP("Exam link: mitosis appears in Paper 1 (identifying stages on drawings, counting chromosomes) and Paper 2 (descriptions, mitotic index, links to cancer and growth). The practical paper often uses root-tip squashes or prepared slides. Describe what the chromosomes do, not just the name of the stage."),
        SUM("The cell cycle: G1, S (DNA replication), G2, then mitosis and cytokinesis, with checkpoints.",
            "Prophase: chromosomes condense. Metaphase: line up. Anaphase: chromatids separate. Telophase: nuclei re-form.",
            "Mitosis makes genetically identical cells for growth, repair and asexual reproduction.",
            "Mitotic index = cells in mitosis ÷ total cells × 100. Time in a stage ≈ fraction of cells × cycle time."),
    ],
))

# ------------------------------------------------------------------ 17. Meiosis
LESSONS.append(lesson(
    module=M3,
    topic="Meiosis",
    title="Meiosis and the sources of genetic variation",
    slug="bil1-meiosis",
    minutes=24,
    summary="Meiosis halves the chromosome number to make haploid gametes. Describe meiosis I and II, crossing over and independent assortment, calculate possible combinations, and compare meiosis with mitosis.",
    objectives=[
        "Define haploid, diploid, homologous chromosomes and bivalent",
        "Describe the stages of meiosis I and meiosis II",
        "Explain how crossing over and independent assortment produce variation",
        "Calculate the number of possible chromosome combinations and compare meiosis with mitosis",
    ],
    key_concepts=["Haploid and diploid", "Homologous chromosomes", "Bivalent", "Crossing over", "Chiasma", "Independent assortment", "Non-disjunction"],
    blocks=[
        H("Introduction"),
        T("Brothers and sisters from the same parents are not identical, except identical twins. Each child gets a different mixture of the parents' genes. This variety is made in the cells that make "
          "sperm and eggs, by a special division called **meiosis**."),
        D("**Meiosis** is a type of nuclear division in which a diploid cell (2n) divides twice to make four haploid cells (n) that are genetically different. "
          "**Homologous chromosomes** are a pair of chromosomes, one from each parent, with the same genes in the same order, though they may carry different alleles.", title="Definitions"),
        T("In humans, a body cell has 46 chromosomes in 23 homologous pairs (2n = 46). A gamete has 23 (n = 23). At fertilization, two gametes fuse and the diploid number is restored."),
        IMG("al-bil1-meiosis-overview.svg", alt="A diploid cell with two pairs of chromosomes dividing in meiosis I into two cells and in meiosis II into four haploid cells",
            caption="Figure 1. Overview of meiosis in a cell with four chromosomes (2n = 4)."),
        H("The stages"),
        KEY("Meiosis I: the number of chromosomes is halved", "Homologous chromosomes separate.", cards=[
            ["Prophase I", "Chromosomes condense. Homologous chromosomes pair up (synapsis) to form bivalents. Non-sister chromatids cross over at points called chiasmata and exchange pieces of DNA. The nuclear envelope breaks down."],
            ["Metaphase I", "Bivalents line up on the equator. The way each pair faces the poles is random (independent assortment)."],
            ["Anaphase I", "Homologous chromosomes are pulled to opposite poles. The centromeres do not divide, so each chromosome still has two chromatids."],
            ["Telophase I", "Two haploid cells form (cytokinesis may follow)."],
        ]),
        KEY("Meiosis II: like mitosis", "Sister chromatids separate.", cards=[
            ["Prophase II and metaphase II", "Chromosomes line up singly on the equator of each cell."],
            ["Anaphase II", "Centromeres divide and sister chromatids are pulled apart."],
            ["Telophase II", "Four haploid cells form, each with single-chromatid chromosomes."],
        ]),
        H("Sources of variation"),
        KEY("Three sources", "Meiosis and fertilization together make genetically different offspring.", cards=[
            ["Crossing over", "Chromatids of homologous chromosomes swap sections in prophase I, giving new combinations of alleles on a chromosome."],
            ["Independent assortment", "Each bivalent lines up independently in metaphase I, so maternal and paternal chromosomes are shuffled into the gametes in many combinations."],
            ["Random fertilization", "Any sperm can fuse with any egg."],
        ]),
        EX("Worked example 1: combinations of chromosomes", intro="A cell has 2n = 6 (three pairs of chromosomes). How many different combinations of chromosomes are possible in the gametes by independent assortment alone (ignoring crossing over), and how many different zygotes from random fertilization?", steps=[
            S("Gametes", math=r"2^n = 2^3 = 8"),
            S("Zygotes", math=r"8 \times 8 = 64"),
        ]),
        EX("Worked example 2: humans", intro="Calculate the number of possible combinations of chromosomes in human gametes (n = 23) and in zygotes, ignoring crossing over.", steps=[
            S("Gametes", math=r"2^{23} = 8\,388\,608"),
            S("Zygotes", math=r"(2^{23})^2 = 2^{46} = 70\,368\,744\,177\,664 \approx 7.0 \times 10^{13}"),
            S("Comment", text="Crossing over makes the real number far larger. This is why every person, except identical twins, is genetically unique."),
        ]),
        EX("Worked example 3: maize", intro="Maize has 2n = 20. How many different chromosome combinations are possible in its gametes?", steps=[
            S("Haploid number", math=r"n = 10"),
            S("Combinations", math=r"2^{10} = 1024"),
        ]),
        CODE("""Feature              Mitosis                    Meiosis
Number of divisions  one                        two
Daughter cells       two, diploid               four, haploid
Genetically          identical                  different
Pairing of           no                         yes (bivalents)
homologues
Crossing over        no                         yes (prophase I)
Occurs in            all body cells that        cells that make gametes
                     divide
Purpose              growth, repair,            gametes, variation
                     asexual reproduction""", "text", title="Table 1. Mitosis compared with meiosis"),
        T("Sometimes a pair of chromosomes fails to separate in meiosis. This is **non-disjunction**. A gamete with an extra chromosome 21 that fuses with a normal gamete makes a zygote with 47 chromosomes, "
          "which causes Down's syndrome (trisomy 21)."),
        MISTAKE("Saying that homologous chromosomes separate in meiosis II", "They separate in meiosis I (anaphase I). Sister chromatids separate in meiosis II."),
        MISTAKE("Using the same number for diploid and haploid cells", "A diploid human cell has 46 chromosomes. A haploid cell has 23. Meiosis halves the number."),
        QUIZ("At which stage of meiosis does crossing over happen?",
             ["Prophase I", "Anaphase I", "Prophase II", "Telophase II"], 0,
             "Crossing over happens between non-sister chromatids of homologous chromosomes when they are paired in prophase I.",
             hint="Crossing over needs paired homologous chromosomes.",
             feedback=["", "In anaphase I the homologues separate.", "Homologues are no longer paired in prophase II.", "Meiosis is nearly finished by telophase II."]),
        QUIZ("A cell with 2n = 8 undergoes meiosis. How many chromosomes are in each of the four daughter cells?",
             ["2", "4", "8", "16"], 1,
             "Meiosis halves the number: 8 ÷ 2 = 4.",
             hint="Gametes are haploid.",
             feedback=["This is a quarter of the original number.", "", "This would be the result of mitosis.", "The number does not double."]),
        H("Practice"),
        PQ("Explain how independent assortment leads to genetic variation.", "In metaphase I each bivalent lines up on the equator in a random orientation, so which chromosome of each pair goes to which pole is random. With n pairs there are 2ⁿ different combinations of maternal and paternal chromosomes in the gametes."),
        PQ("Describe the difference between anaphase I and anaphase II.", "In anaphase I homologous chromosomes are pulled to opposite poles and each still has two chromatids. In anaphase II the centromeres divide and sister chromatids are pulled to opposite poles."),
        PQ("State three differences between mitosis and meiosis.", "Mitosis has one division and meiosis has two. Mitosis makes two diploid cells and meiosis makes four haploid cells. Mitosis makes identical cells but meiosis makes genetically different cells. Only meiosis has pairing of homologous chromosomes and crossing over."),
        TIP("Exam link: meiosis appears in Paper 1 (identifying stages, chromosome numbers) and Paper 2 (describing stages, explaining variation, comparing with mitosis, non-disjunction). Show exactly which chromosomes or chromatids separate at each division."),
        SUM("Meiosis is two divisions that make four haploid, genetically different cells from one diploid cell.",
            "Meiosis I separates homologous chromosomes. Meiosis II separates sister chromatids.",
            "Variation comes from crossing over (prophase I), independent assortment (metaphase I) and random fertilization. The number of gamete combinations is 2^n.",
            "Non-disjunction gives gametes with an extra or missing chromosome."),
    ],
))
