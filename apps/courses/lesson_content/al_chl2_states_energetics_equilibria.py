"""A Level Chemistry (Lower Sixth): States of Matter & Solid Lattices; Chemical Energetics & Thermodynamics; Chemical & Phase Equilibria.

Draft content: check against the official syllabus and your textbook. Every number was verified by script.
Data values (van der Waals constants, bond enthalpies, entropies, ionic radii) are typical textbook values stated in each question.
"""

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "lower-sixth")

M4 = "States of Matter & Solid Lattices"
M5 = "Chemical Energetics & Thermodynamics"
M6 = "Chemical & Phase Equilibria"

LESSONS = []

# ------------------------------------------------------------------ 1. Real gases
LESSONS.append(lesson(
    module=M4,
    topic="Kinetic theory and real gases",
    title="Ideal and real gases: the van der Waals equation",
    slug="chl2-real-gases-vdw",
    minutes=22,
    summary="Why real gases depart from PV = nRT, how the compressibility factor Z shows it, and how the van der Waals equation corrects pressure and volume.",
    objectives=[
        "State the assumptions of the kinetic theory of an ideal gas and the conditions where real gases obey them",
        "Explain deviations from ideal behaviour using intermolecular forces and molecular volume",
        "Use the compressibility factor Z = PV/nRT to describe a real gas",
        "Use the van der Waals equation to calculate the pressure of a real gas and compare it with the ideal value",
    ],
    key_concepts=["Ideal gas", "Kinetic theory", "Compressibility factor", "Intermolecular forces", "Excluded volume",
                  "van der Waals equation", "Constants a and b"],
    blocks=[
        H("Introduction"),
        T(r"A domestic gas cylinder in Douala or Yaounde holds butane. Inside, most of the butane is a liquid, yet it leaves the cylinder as a gas when you open the valve. "
          r"If butane behaved as an ideal gas, it could never be squeezed into a liquid at room temperature. Real gases can be liquefied because their particles attract one another and take up space."),
        T(r"In this lesson you learn where the ideal gas equation works, where it fails, and how the **van der Waals equation** repairs it with two small correction terms."),
        H("The ideal gas and its assumptions"),
        D(r"An **ideal gas** obeys $PV = nRT$ at all temperatures and pressures. The kinetic theory of such a gas assumes: (1) the particles are so small that their own volume is negligible; "
          r"(2) there are no forces of attraction or repulsion between particles; (3) collisions are perfectly elastic (no kinetic energy is lost); (4) particles move randomly and the mean kinetic energy is proportional to the Kelvin temperature.",
          title="Ideal gas and kinetic theory", formula=r"PV = nRT"),
        T(r"Here $P$ is pressure, $V$ the volume, $n$ the amount in mol, $T$ the temperature in kelvin and $R$ the gas constant. In this lesson $R = 8.314\ \mathrm{J\,K^{-1}\,mol^{-1}}$, which is the same as $0.08314\ \mathrm{dm^3\,bar\,K^{-1}\,mol^{-1}}$ (1 bar = 100 kPa)."),
        T(r"Assumptions (1) and (2) are never exactly true. Every real molecule has a size, and every real molecule attracts its neighbours at least weakly (London forces)."),
        H("Measuring the deviation: the compressibility factor"),
        D(r"The **compressibility factor** $Z$ of a gas is the ratio of its actual $PV$ to the ideal value $nRT$. For an ideal gas $Z = 1$ at every pressure.",
          title="Compressibility factor", formula=r"Z = \dfrac{PV}{nRT}"),
        IMG("al-chl2-real-gas-z.svg", alt="Graph of Z against pressure at 400 K from the van der Waals model. Helium rises above 1 steadily. Carbon dioxide and methane dip below 1 and then rise above it.",
            caption="Figure 1. Z against pressure for three gases (van der Waals model, 400 K). The dashed line is the ideal gas, Z = 1."),
        T(r"Read the graph in two parts. At **moderate pressure** the molecules are close enough to attract each other. They hit the wall less hard, so the pressure is lower than ideal and $Z < 1$. "
          r"At **high pressure** the molecules are packed so tightly that their own volume matters. The space left to move in is less than $V$, so the pressure is higher than ideal and $Z > 1$. "
          r"Helium has almost no attraction, so it shows only the second effect."),
        KEY("When does a real gas behave ideally?", r"A real gas comes closest to ideal behaviour at **low pressure** (molecules far apart) and **high temperature** (molecules fast, so attractions matter little).",
            cards=[["Low pressure", "Particles are far apart, so their volume and attractions are negligible."],
                   ["High temperature", "Kinetic energy is large compared with the attractions."],
                   ["Small, non-polar molecules", "He, H2 and Ne have the weakest forces and are the most ideal."]]),
        H("The van der Waals equation"),
        T(r"Johannes van der Waals corrected the two faulty assumptions separately. First, the molecules take up space, so the volume free to move in is $V - nb$, where $b$ is the volume excluded per mole. "
          r"Second, attractions pull each molecule back from the wall. This lowers the pressure by an amount proportional to $n^2/V^2$ (the number of pairs of molecules per volume squared), so the measured $P$ is replaced by $P + an^2/V^2$."),
        D(r"The van der Waals equation for $n$ mol of a real gas is given below. The constant $a$ measures the strength of the intermolecular attractions. The constant $b$ is the volume excluded by one mole of molecules (it is roughly four times the volume of the molecules themselves).",
          title="van der Waals equation", formula=r"\left(P + \dfrac{an^2}{V^2}\right)(V - nb) = nRT"),
        F(r"P = \dfrac{nRT}{V - nb} - \dfrac{an^2}{V^2}", title="Rearranged for the pressure"),
        CODE("gas    a / dm6 bar mol-2    b / dm3 mol-1\n"
             "He        0.0346              0.0238\n"
             "CH4       2.283               0.0428\n"
             "CO2       3.64                0.04267\n"
             "NH3       4.225               0.0371", "text", title="Typical van der Waals constants (check your textbook: sources differ slightly)"),
        T(r"A large $a$ goes with strong attractions and easy liquefaction: ammonia and carbon dioxide are far easier to liquefy than helium."),
        EX("Worked example 1: pressure of carbon dioxide", intro=r"Calculate the pressure of 1.00 mol of $\mathrm{CO_2}$ in a 1.00 dm$^3$ vessel at 300 K, first as an ideal gas and then with the van der Waals equation. Use $a = 3.64\ \mathrm{dm^6\,bar\,mol^{-2}}$, $b = 0.04267\ \mathrm{dm^3\,mol^{-1}}$ and $R = 0.08314\ \mathrm{dm^3\,bar\,K^{-1}\,mol^{-1}}$.", steps=[
            S("Ideal gas pressure", math=r"P = \dfrac{nRT}{V} = \dfrac{1.00 \times 0.08314 \times 300}{1.00} = 24.94\ \text{bar}"),
            S("Excluded volume term", math=r"V - nb = 1.00 - 0.04267 = 0.95733\ \text{dm}^3"),
            S("Pressure from the repulsion term", math=r"\dfrac{nRT}{V - nb} = \dfrac{24.942}{0.95733} = 26.05\ \text{bar}"),
            S("Subtract the attraction term", math=r"\dfrac{an^2}{V^2} = 3.64 \times \dfrac{1.00^2}{1.00^2} = 3.64\ \text{bar}"),
            S("Real pressure", math=r"P = 26.05 - 3.64 = 22.41\ \text{bar}"),
            S("Compressibility factor", math=r"Z = \dfrac{22.41 \times 1.00}{24.94} = 0.90", text="Z is below 1: attractions beat size at this pressure."),
        ], check=r"\left(22.41 + 3.64\right)(0.95733) = 24.94"),
        EX("Worked example 2: the gap shrinks at low pressure", intro=r"Repeat the calculation for 2.00 mol of $\mathrm{CO_2}$ in 10.0 dm$^3$ at 300 K (same constants). The gas is five times more dilute per mole.", steps=[
            S("Ideal pressure", math=r"P = \dfrac{2.00 \times 0.08314 \times 300}{10.0} = 4.99\ \text{bar}"),
            S("Repulsion term", math=r"\dfrac{nRT}{V - nb} = \dfrac{49.884}{10.0 - 0.08534} = 5.031\ \text{bar}"),
            S("Attraction term", math=r"\dfrac{an^2}{V^2} = \dfrac{3.64 \times 4.00}{100} = 0.1456\ \text{bar}"),
            S("Real pressure", math=r"P = 5.031 - 0.146 = 4.89\ \text{bar}", text="The real value is only about 2% below the ideal value. At low pressure a real gas is nearly ideal."),
        ]),
        EX("Worked example 3: choosing the more ideal gas", intro=r"Using the table, say which of He and $\mathrm{NH_3}$ is closer to ideal at 1.00 mol in 1.00 dm$^3$ at 300 K, and support it with Z. (Calculated vdW pressures: He 25.52 bar, $\mathrm{NH_3}$ 21.68 bar.)", steps=[
            S("Ideal pressure", math=r"P_{ideal} = 24.94\ \text{bar}"),
            S("Z for helium", math=r"Z = \dfrac{25.52}{24.94} = 1.02", text="Helium has tiny a (0.0346), so the volume term wins slightly."),
            S("Z for ammonia", math=r"Z = \dfrac{21.68}{24.94} = 0.87", text="Ammonia has a large a (4.225), so attractions lower the pressure by 13%."),
            S("Conclusion", text="Helium is much closer to ideal (Z = 1.02 against 0.87), as expected from its weak forces."),
        ]),
        MISTAKE("Mixing up a and b", r"Remember: $a$ goes with **attractions** and corrects the *pressure*; $b$ goes with **size** and corrects the *volume*. In $V - nb$ the volume is reduced, in $P + an^2/V^2$ the pressure is raised."),
        MISTAKE("Saying a real gas is ideal at low temperature", r"Low temperature makes deviations **worse**: slow molecules are caught by the attractions and the gas finally condenses. Ideal behaviour needs high temperature and low pressure."),
        TIP(r"Paper 1 often tests the direction of the deviation (Z above or below 1) and the meaning of $a$ and $b$. Paper 2 may ask you to use the van der Waals equation with data given in the question. Always state the units of $R$ you use."),
        QUIZ(r"A gas has $Z = 0.85$ at 100 bar. What is the main reason?", [
            "The molecules take up a large part of the volume",
            "Attractions between molecules lower the pressure",
            "The molecules collide inelastically",
            "The temperature is too high",
        ], 1, r"$Z < 1$ means $PV$ is smaller than $nRT$. The pressure is below the ideal value because attractions pull molecules back from the wall.",
             hint="Which effect lowers the pressure, and which raises it?",
             feedback=["Molecular volume raises the pressure and gives Z above 1.", "",
                       "Collisions are treated as elastic in both models; this is not the cause of Z below 1.",
                       "A high temperature reduces deviations; it does not explain Z below 1."]),
        QUIZ(r"Which pair of gases would you expect to show the **largest** and the **smallest** value of $a$?", [
            r"He largest, $\mathrm{NH_3}$ smallest", r"$\mathrm{NH_3}$ largest, He smallest", r"$\mathrm{CO_2}$ largest, $\mathrm{NH_3}$ smallest", r"He and $\mathrm{NH_3}$ the same",
        ], 1, r"Ammonia has strong hydrogen bonding and a large $a$ (4.225). Helium has very weak London forces and a very small $a$ (0.0346).",
             hint="Large a means strong attractions.",
             feedback=["This is reversed: helium has the weakest forces.", "", "Ammonia (4.225) has a larger a than carbon dioxide (3.64) in the table.", "Their intermolecular forces are very different."]),
        PQ(r"(a) State two assumptions of the kinetic theory of an ideal gas that are not true for a real gas. (b) Explain why $Z$ is below 1 for methane at moderate pressure.",
           r"(a) The volume of the particles is negligible; there are no intermolecular forces. (b) At moderate pressure the molecules are close enough for attractions to act. They hit the walls with less force, so the pressure and therefore $PV$ are lower than $nRT$, giving $Z < 1$."),
        PQ(r"Use the van der Waals equation to find the pressure of 0.500 mol of methane in 1.00 dm$^3$ at 300 K. $a = 2.283\ \mathrm{dm^6\,bar\,mol^{-2}}$, $b = 0.0428\ \mathrm{dm^3\,mol^{-1}}$, $R = 0.08314\ \mathrm{dm^3\,bar\,K^{-1}\,mol^{-1}}$. Compare it with the ideal value.",
           r"Ideal: $P = 0.500 \times 0.08314 \times 300 / 1.00 = 12.47$ bar. vdW: $nRT/(V - nb) = 12.471/(1.00 - 0.0214) = 12.74$ bar; $an^2/V^2 = 2.283 \times 0.25 = 0.571$ bar; $P = 12.74 - 0.57 = 12.17$ bar. The real pressure is about 2.4% below the ideal value."),
        PQ(r"Explain, using the two terms in the van der Waals equation, why helium liquefies only at very low temperature but butane liquefies under modest pressure at room temperature.",
           r"The term $a$ measures attraction. Butane has large London forces (large $a$), so at room temperature and modest pressure the attractions are enough to hold molecules together as a liquid. Helium has a tiny $a$: its atoms barely attract, so the kinetic energy must be made very small (very low temperature) before the weak attractions can hold them."),
        SUM(r"An ideal gas obeys $PV = nRT$; real gases do so best at low pressure and high temperature.",
            r"$Z = PV/nRT$ is 1 for an ideal gas, below 1 where attractions dominate and above 1 where molecular size dominates.",
            r"van der Waals equation: $(P + an^2/V^2)(V - nb) = nRT$. $a$ corrects for attractions and $b$ for molecular volume.",
            r"A large $a$ means strong attractions and easy liquefaction (for example $\mathrm{NH_3}$, $\mathrm{CO_2}$); helium has a very small $a$."),
    ],
))

# ------------------------------------------------------------------ 2. Unit cells
LESSONS.append(lesson(
    module=M4,
    topic="Unit cells and coordination numbers",
    title="Unit cells, coordination numbers and crystal density",
    slug="chl2-unit-cells-density",
    minutes=24,
    summary="The simple, body-centred and face-centred cubic unit cells: atoms per cell, coordination number, packing efficiency and how to calculate the density of a metal from its cell edge.",
    objectives=[
        "Define lattice, unit cell and coordination number",
        "Count the atoms in simple, body-centred and face-centred cubic cells",
        "Relate the cell edge to the atomic radius and find the packing efficiency",
        "Calculate the density of a metal or the atomic radius from cell data",
    ],
    key_concepts=["Crystal lattice", "Unit cell", "Coordination number", "Simple cubic", "Body-centred cubic",
                  "Face-centred cubic", "Close packing", "Packing efficiency"],
    blocks=[
        H("Introduction"),
        T(r"A copper wire, an iron roofing nail and an aluminium cooking pot are all crystalline solids. Inside, the atoms sit in a repeating three-dimensional pattern, like oranges stacked in a Mile 17 market. "
          r"The smallest block that repeats to build the whole stack is the **unit cell**. If you know the unit cell, you can calculate the density of the metal from first principles."),
        H("Lattice, unit cell and coordination number"),
        D(r"A **crystal lattice** is the regular three-dimensional arrangement of particles in a crystal. The **unit cell** is the smallest repeating part of the lattice that, when stacked in all directions, builds the whole crystal.",
          title="Lattice and unit cell"),
        D(r"The **coordination number** of a particle in a crystal is the number of nearest neighbours that touch it.", title="Coordination number"),
        T(r"Particles at the corners, faces or edges of a cell are shared with neighbouring cells, so only a fraction belongs to one cell."),
        KEY("Counting the share of each position", r"Add the shares of all the particles to find the number of atoms per unit cell.",
            cards=[["Corner", "Shared by 8 cells: counts 1/8"], ["Edge", "Shared by 4 cells: counts 1/4"],
                   ["Face", "Shared by 2 cells: counts 1/2"], ["Body (inside)", "Belongs to one cell: counts 1"]]),
        H("The three cubic cells"),
        IMG("al-chl2-unit-cells.svg", alt="Three cubes: simple cubic with atoms at the corners; body-centred cubic with an extra atom in the centre; face-centred cubic with extra atoms on the faces.",
            caption="Figure 1. Simple cubic, body-centred cubic and face-centred cubic unit cells."),
        CODE("cell   atoms/cell  CN   edge a vs radius r   packing efficiency\n"
             "sc        1         6    a = 2r              52.4 %\n"
             "bcc       2         8    a = 4r / root 3     68.0 %\n"
             "fcc       4        12    a = 2 root 2 r      74.0 %", "text", title="Summary of the cubic cells"),
        T(r"Counting: simple cubic $8 \times \tfrac18 = 1$. Body-centred $8 \times \tfrac18 + 1 = 2$. Face-centred $8 \times \tfrac18 + 6 \times \tfrac12 = 4$."),
        T(r"Atoms touch along different lines in each cell. In simple cubic they touch along an edge, so $a = 2r$. In body-centred cubic they touch along the body diagonal, which is $\sqrt{3}\,a$ long and holds four radii, so $a = 4r/\sqrt{3}$. In face-centred cubic they touch along the face diagonal, $\sqrt{2}\,a$ long, again four radii, so $a = 2\sqrt{2}\,r$."),
        D(r"The **packing efficiency** is the fraction of the cell volume filled by the atoms. For a cell with $Z$ atoms of radius $r$ and edge $a$:", title="Packing efficiency", formula=r"\text{efficiency} = \dfrac{Z \times \tfrac{4}{3}\pi r^3}{a^3}"),
        EX("Worked example 1: packing efficiency of face-centred cubic", intro=r"Show that the packing efficiency of a face-centred cubic metal is 74%.", steps=[
            S("Atoms per cell", math=r"Z = 4"),
            S("Edge in terms of r", math=r"a = 2\sqrt{2}\,r \Rightarrow a^3 = 16\sqrt{2}\,r^3"),
            S("Volume of the atoms", math=r"4 \times \tfrac{4}{3}\pi r^3 = \tfrac{16}{3}\pi r^3"),
            S("Divide", math=r"\dfrac{\tfrac{16}{3}\pi r^3}{16\sqrt{2}\,r^3} = \dfrac{\pi}{3\sqrt{2}} = 0.740", text="So 74.0% of the cell is filled and 26.0% is empty space."),
        ]),
        H("Close packing"),
        T(r"Face-centred cubic and **hexagonal close packing** (hcp) are both close-packed: each atom has 12 neighbours and the efficiency is 74%. They differ only in the stacking of layers. hcp repeats the layer order ABAB; face-centred cubic (also called cubic close packed) repeats ABCABC. "
          r"Copper, silver, gold and aluminium are face-centred cubic. Iron (at room temperature) and sodium are body-centred cubic. Magnesium and zinc are hcp."),
        H("Density from the unit cell"),
        D(r"The density of a crystal equals the mass of the atoms in one cell divided by the volume of the cell. For $Z$ atoms of molar mass $M$ in a cubic cell of edge $a$, with $N_A = 6.022 \times 10^{23}\ \mathrm{mol^{-1}}$:",
          title="Density from cell data", formula=r"\rho = \dfrac{Z\,M}{N_A\,a^3}"),
        TIP(r"Keep every length in cm when the density is wanted in $\mathrm{g\,cm^{-3}}$: 1 pm $= 10^{-10}$ cm, so 361 pm $= 3.61 \times 10^{-8}$ cm."),
        EX("Worked example 2: density of copper", intro=r"Copper is face-centred cubic with cell edge 361 pm. Its molar mass is $63.5\ \mathrm{g\,mol^{-1}}$. Calculate its density.", steps=[
            S("Convert the edge", math=r"a = 361\ \text{pm} = 3.61 \times 10^{-8}\ \text{cm}"),
            S("Cell volume", math=r"a^3 = (3.61 \times 10^{-8})^3 = 4.705 \times 10^{-23}\ \text{cm}^3"),
            S("Mass of 4 atoms", math=r"\dfrac{4 \times 63.5}{6.022 \times 10^{23}} = 4.218 \times 10^{-22}\ \text{g}"),
            S("Divide", math=r"\rho = \dfrac{4.218 \times 10^{-22}}{4.705 \times 10^{-23}} = 8.97\ \text{g cm}^{-3}"),
        ], check=r"\text{Data books give about } 8.96\ \text{g cm}^{-3}"),
        EX("Worked example 3: radius and density of iron", intro=r"Iron is body-centred cubic with cell edge 287 pm and molar mass $55.8\ \mathrm{g\,mol^{-1}}$. Find the atomic radius and the density.", steps=[
            S("Radius from the body diagonal", math=r"r = \dfrac{\sqrt{3}\,a}{4} = \dfrac{1.732 \times 287}{4} = 124\ \text{pm}"),
            S("Cell volume", math=r"a^3 = (2.87 \times 10^{-8})^3 = 2.364 \times 10^{-23}\ \text{cm}^3"),
            S("Mass of 2 atoms", math=r"\dfrac{2 \times 55.8}{6.022 \times 10^{23}} = 1.853 \times 10^{-22}\ \text{g}"),
            S("Density", math=r"\rho = \dfrac{1.853 \times 10^{-22}}{2.364 \times 10^{-23}} = 7.84\ \text{g cm}^{-3}"),
        ]),
        MISTAKE("Using the wrong relation between a and r", r"Do not use $a = 2r$ for every cell. That holds only for simple cubic. Draw the line along which atoms touch: edge (sc), body diagonal (bcc) or face diagonal (fcc)."),
        MISTAKE("Forgetting to cube the edge or to convert units", r"The volume is $a^3$, not $a$. A cell edge of 361 pm in the formula as 361 gives a nonsense answer. Convert to cm first."),
        TIP(r"The unit cell appears in Paper 1 (atoms per cell, coordination number, efficiency) and in Paper 2 calculations (density or radius from given data). Quote $N_A$ and the units you use."),
        QUIZ(r"How many atoms belong to one face-centred cubic unit cell?", ["2", "4", "6", "14"], 1,
             r"$8$ corners $\times \tfrac18 = 1$ and $6$ faces $\times \tfrac12 = 3$, a total of 4.",
             hint="Add the shares of corner and face atoms.",
             feedback=["2 is the count for body-centred cubic.", "", "6 is the number of faces, not the number of atoms.", "14 is the number of positions, ignoring that they are shared."]),
        QUIZ(r"Which cubic structure has the highest coordination number?", ["Simple cubic", "Body-centred cubic", "Face-centred cubic", "They are all equal"], 2,
             r"Face-centred cubic (like hcp) is close packed: coordination number 12, against 8 for bcc and 6 for simple cubic.",
             hint="Close packing gives the most neighbours.",
             feedback=["Simple cubic has only 6 neighbours.", "Body-centred cubic has 8 neighbours.", "", "The numbers are 6, 8 and 12."]),
        PQ(r"Aluminium is face-centred cubic with cell edge 405 pm and molar mass $27.0\ \mathrm{g\,mol^{-1}}$. Calculate its density and its atomic radius.",
           r"$a = 4.05 \times 10^{-8}$ cm, $a^3 = 6.643 \times 10^{-23}$ cm$^3$. Mass of 4 atoms $= 4 \times 27.0 / 6.022 \times 10^{23} = 1.793 \times 10^{-22}$ g. $\rho = 2.70\ \mathrm{g\,cm^{-3}}$. Radius $r = a/(2\sqrt{2}) = 405/2.828 = 143$ pm."),
        PQ(r"Show that the packing efficiency of a body-centred cubic structure is 68.0%.",
           r"$Z = 2$ and $a = 4r/\sqrt{3}$, so $a^3 = 64r^3/(3\sqrt{3})$. Atom volume $= 2 \times \tfrac43\pi r^3 = \tfrac83\pi r^3$. Efficiency $= \tfrac83\pi r^3 \times 3\sqrt{3}/(64 r^3) = \sqrt{3}\pi/8 = 0.680$."),
        PQ(r"Silver is face-centred cubic with atomic radius 144 pm. Calculate the cell edge in pm.",
           r"Atoms touch along the face diagonal, which holds 4 radii: $\sqrt{2}\,a = 4r$, so $a = 4 \times 144/1.414 = 407$ pm."),
        SUM(r"The unit cell is the smallest repeating unit; corner atoms count 1/8, edge 1/4, face 1/2 and body 1.",
            r"Atoms per cell and coordination numbers: simple cubic 1 and 6; body-centred 2 and 8; face-centred 4 and 12.",
            r"Edge and radius: $a = 2r$ (sc), $a = 4r/\sqrt{3}$ (bcc), $a = 2\sqrt{2}\,r$ (fcc). Packing efficiencies are 52.4%, 68.0% and 74.0%.",
            r"Density $\rho = ZM/(N_A a^3)$ with $a$ in cm for $\mathrm{g\,cm^{-3}}$."),
    ],
))

# ------------------------------------------------------------------ 3. Crystal lattices
LESSONS.append(lesson(
    module=M4,
    topic="Crystal lattices",
    title="Ionic and giant covalent lattices: NaCl, CsCl, diamond, graphite, fullerene and silica",
    slug="chl2-crystal-lattices",
    minutes=24,
    summary="The structures of sodium chloride, caesium chloride, diamond, graphite, C60 fullerene and silicon dioxide, how each structure explains the properties, and density calculations for ionic crystals.",
    objectives=[
        "Describe the NaCl and CsCl structures and their coordination numbers",
        "Use the radius ratio as a guide to the coordination number of an ionic crystal",
        "Describe the bonding and structure of diamond, graphite, fullerene (C60) and silicon dioxide",
        "Link structure to melting point, hardness and electrical conductivity, and calculate the density of an ionic crystal",
    ],
    key_concepts=["Ionic lattice", "Radius ratio", "Giant covalent structure", "Allotrope", "Delocalised electrons",
                  "Fullerene", "Silicon dioxide", "Coordination number"],
    blocks=[
        H("Introduction"),
        T(r"Table salt, a pencil lead, a diamond ring and beach sand are all solids made of lattices, yet they behave very differently. Salt dissolves in water, graphite writes on paper and conducts electricity, diamond cuts glass and sand (silica) will not melt on a kitchen fire. "
          r"The explanation lies in how the particles are arranged and how they are held."),
        H("Ionic lattices: sodium chloride and caesium chloride"),
        T(r"In an ionic crystal, positive and negative ions attract in all directions. Each ion is surrounded by as many oppositely charged ions as will fit around it. The ions are of different sizes, so how many fit depends on the ratio of the radii."),
        IMG("al-chl2-nacl-cscl.svg", alt="Left: part of the sodium chloride lattice with large chloride ions and small sodium ions alternating on a cubic grid. Right: caesium chloride cube with chloride ions at the corners and a caesium ion at the centre.",
            caption="Figure 1. The sodium chloride and caesium chloride lattices."),
        D(r"**Sodium chloride (rock-salt) structure.** The $\mathrm{Cl^-}$ ions form a face-centred cubic array and the smaller $\mathrm{Na^+}$ ions fill the holes between them. Every ion has 6 nearest neighbours of the opposite charge: coordination number 6:6. "
          r"The unit cell contains 4 $\mathrm{Na^+}$ and 4 $\mathrm{Cl^-}$ ions, that is 4 formula units.", title="NaCl"),
        D(r"**Caesium chloride structure.** The $\mathrm{Cl^-}$ ions sit at the corners of a simple cube and one $\mathrm{Cs^+}$ ion sits in the centre. Coordination number 8:8. The unit cell holds $8 \times \tfrac18 = 1$ chloride and 1 caesium ion: 1 formula unit.", title="CsCl"),
        CODE("radius ratio r+/r-    coordination number   shape around the cation\n"
             "0.225 - 0.414             4                 tetrahedral\n"
             "0.414 - 0.732             6                 octahedral\n"
             "0.732 - 1.00              8                 cubic", "text", title="Radius-ratio guide (a rule of thumb; check your textbook)"),
        T(r"The ratio of the cation radius to the anion radius gives a guide to the structure. For NaCl: $102/181 = 0.564$, in the octahedral range, so coordination number 6. For CsCl: $167/181 = 0.923$, above 0.732, so coordination number 8. The rule is a guide, not a law: it fails for some compounds."),
        EX("Worked example 1: density of sodium chloride", intro=r"The unit cell of NaCl has edge 564 pm. Take $M(\mathrm{NaCl}) = 58.5\ \mathrm{g\,mol^{-1}}$ and $N_A = 6.022 \times 10^{23}\ \mathrm{mol^{-1}}$. Calculate its density. The ionic radii are $\mathrm{Na^+}$ 102 pm and $\mathrm{Cl^-}$ 181 pm: check the edge from the radii as well.", steps=[
            S("Formula units per cell", text="4 Na+ and 4 Cl-, so 4 formula units."),
            S("Mass of the cell", math=r"\dfrac{4 \times 58.5}{6.022 \times 10^{23}} = 3.886 \times 10^{-22}\ \text{g}"),
            S("Volume of the cell", math=r"(5.64 \times 10^{-8})^3 = 1.794 \times 10^{-22}\ \text{cm}^3"),
            S("Density", math=r"\rho = \dfrac{3.886 \times 10^{-22}}{1.794 \times 10^{-22}} = 2.17\ \text{g cm}^{-3}"),
            S("Check the edge", math=r"a = 2(r_+ + r_-) = 2(102 + 181) = 566\ \text{pm}", text="Ions touch along the cell edge (Na+, Cl-, Na+ along the edge gives 2r+ + 2r-). 566 pm agrees with 564 pm."),
        ]),
        EX("Worked example 2: density of caesium chloride", intro=r"CsCl has cell edge 412 pm and $M = 168.4\ \mathrm{g\,mol^{-1}}$. Calculate the density.", steps=[
            S("Formula units per cell", text="1."),
            S("Mass of the cell", math=r"\dfrac{168.4}{6.022 \times 10^{23}} = 2.796 \times 10^{-22}\ \text{g}"),
            S("Volume of the cell", math=r"(4.12 \times 10^{-8})^3 = 6.993 \times 10^{-23}\ \text{cm}^3"),
            S("Density", math=r"\rho = \dfrac{2.796 \times 10^{-22}}{6.993 \times 10^{-23}} = 4.00\ \text{g cm}^{-3}"),
        ]),
        T(r"Ionic crystals have high melting points because many strong ionic attractions must be overcome. They are hard but brittle: a blow slides one layer so that like charges face each other and the crystal splits. They do not conduct when solid (ions fixed) but conduct when molten or dissolved (ions free to move)."),
        H("Giant covalent lattices"),
        T(r"Carbon forms several **allotropes** (different structural forms of the same element). Silicon dioxide forms a similar giant covalent network."),
        D(r"**Diamond.** Every carbon atom forms four single covalent bonds ($sp^3$) to four others in a tetrahedron (coordination number 4). The structure is a face-centred cubic arrangement with four more atoms in half of the tetrahedral holes: 8 atoms per unit cell. "
          r"All the electrons are held in bonds, so diamond is a very hard electrical insulator with a very high melting point.", title="Diamond"),
        D(r"**Graphite.** Each carbon bonds to three others ($sp^2$) in flat layers of hexagons, leaving one electron per atom delocalised across the layer. The layers are held together only by weak London forces. "
          r"So graphite is soft and slippery (layers slide) and conducts electricity along the layers, yet it has a very high melting point because of the strong bonds within each layer.", title="Graphite"),
        D(r"**Fullerene (C60).** Sixty carbon atoms form a hollow ball with 12 pentagons and 20 hexagons, like a football. Each carbon bonds to three others, with delocalised electrons. C60 is a **simple molecular** substance: separate molecules held by weak London forces. It is soft, soluble in non-polar solvents such as methylbenzene and sublimes at a much lower temperature than diamond.", title="Fullerene"),
        D(r"**Silicon dioxide (silica, quartz, sand).** Each silicon atom bonds to four oxygen atoms in a tetrahedron, and each oxygen bridges two silicon atoms: Si:O coordination 4:2, formula $\mathrm{SiO_2}$. "
          r"It is like diamond with an oxygen atom inserted into every Si-Si bond. It is hard, has a very high melting point and does not conduct.", title="Silica"),
        CODE("substance   bonding              melting point    conducts?      hardness\n"
             "NaCl        ionic lattice        high (801 C)     only molten    hard, brittle\n"
             "diamond     giant covalent       very high        no             hardest\n"
             "graphite    layers, delocalised  very high        yes (layers)   soft\n"
             "C60         simple molecular     low (sublimes)   no             soft\n"
             "SiO2        giant covalent       very high        no             hard", "text", title="Structure and properties"),
        EX("Worked example 3: counting in C60 and the diamond cell", intro=r"(a) Check that a C60 ball is consistent with 12 pentagons and 20 hexagons. (b) Count the atoms in the diamond cell.", steps=[
            S("Vertices (atoms)", math=r"V = \dfrac{12 \times 5 + 20 \times 6}{3} = \dfrac{180}{3} = 60", text="Each atom is shared by 3 faces."),
            S("Edges (bonds)", math=r"E = \dfrac{12 \times 5 + 20 \times 6}{2} = 90", text="Each bond is shared by 2 faces."),
            S("Euler check", math=r"V - E + F = 60 - 90 + 32 = 2", text="Euler's rule for a closed polyhedron holds, so the ball is consistent."),
            S("Diamond cell", math=r"8 \times \tfrac18 + 6 \times \tfrac12 + 4 = 8", text="Corners, faces and 4 atoms fully inside the cell."),
        ]),
        MISTAKE("Saying graphite conducts because it has ions", r"Graphite has no ions. It conducts because each carbon contributes one **delocalised electron** that can move along the layer."),
        MISTAKE("Saying covalent bonds break when C60 or iodine melts", r"Simple molecular substances melt by overcoming weak **intermolecular forces**, not the covalent bonds. Giant covalent substances (diamond, silica) must break strong covalent bonds, which is why their melting points are far higher."),
        TIP(r"Questions often ask you to explain a property from the structure: always name the particles, the forces or bonds that must be broken, and whether charge carriers can move."),
        QUIZ(r"Why is graphite a good lubricant and a conductor, while diamond is neither?", [
            "Graphite has ions and diamond has none",
            "Graphite has weak forces between layers and delocalised electrons; diamond has four localised bonds per atom",
            "Graphite has weaker covalent bonds in each layer than diamond",
            "Graphite is a molecular substance and diamond is ionic",
        ], 1, r"Layers slide because only weak forces hold them. Each carbon has one free electron, which carries current along the layer. In diamond every electron is in a bond.",
             hint="Compare how many bonds each carbon forms and what holds the layers.",
             feedback=["Neither is ionic.", "", "The bonds within graphite layers are very strong; it is the forces between layers that are weak.", "Diamond is giant covalent, not ionic."]),
        QUIZ(r"The radius ratio for a cation of 0.923 of the anion radius suggests which coordination number?", ["4", "6", "8", "12"], 2,
             r"A ratio between 0.732 and 1.00 allows 8 anions around the cation (CsCl structure).",
             hint="Use the radius-ratio guide.", feedback=["4 goes with a ratio under 0.414.", "6 goes with 0.414 to 0.732.", "", "12 is a metal close-packing number, not an ionic ratio result."]),
        PQ(r"Potassium chloride has the sodium chloride structure with cell edge 629 pm and $M = 74.6\ \mathrm{g\,mol^{-1}}$. Calculate its density. State the coordination number of each ion.",
           r"4 formula units per cell. Mass $= 4 \times 74.6 / 6.022 \times 10^{23} = 4.955 \times 10^{-22}$ g. Volume $= (6.29 \times 10^{-8})^3 = 2.489 \times 10^{-22}$ cm$^3$. $\rho = 1.99\ \mathrm{g\,cm^{-3}}$. Coordination number 6 for each ion (6:6)."),
        PQ(r"Explain the difference in melting point between silicon dioxide and carbon dioxide (solid, dry ice).",
           r"Silicon dioxide is a giant covalent lattice: every Si-O covalent bond in the whole crystal must be broken to melt it, so the melting point is very high. Solid carbon dioxide is a simple molecular crystal: only weak London forces between separate $\mathrm{CO_2}$ molecules are overcome, so it sublimes at very low temperature."),
        PQ(r"Describe the structure of C60 and explain why it dissolves in methylbenzene but diamond does not.",
           r"C60 is a hollow ball of 60 carbon atoms (12 pentagons, 20 hexagons), each bonded to three others. It is a simple molecular substance, held by weak London forces that methylbenzene molecules can replace by similar forces. Diamond is a giant network in which every atom is held by four strong covalent bonds; no solvent can break these, so it does not dissolve."),
        SUM(r"NaCl: 6:6 coordination, 4 formula units per cell. CsCl: 8:8, 1 formula unit per cell. The radius ratio $r_+/r_-$ is a guide.",
            r"Ionic crystals are hard, brittle, high-melting and conduct only when molten or dissolved.",
            r"Diamond (4 bonds, insulator), graphite (layers, delocalised electrons, conducts), C60 (simple molecules, low sublimation temperature) and silica (4:2 network) are explained by their structures.",
            r"Density of a crystal $= ZM/(N_A a^3)$ with $Z$ the number of formula units per cell."),
    ],
))

# ------------------------------------------------------------------ 4. Standard enthalpy changes
LESSONS.append(lesson(
    module=M5,
    topic="Standard enthalpy changes",
    title="Standard enthalpy changes and calorimetry",
    slug="chl2-standard-enthalpy-changes",
    minutes=24,
    summary="Enthalpy change, standard conditions, and the standard enthalpies of formation, combustion, neutralisation and solution, with calorimetry calculations from temperature changes.",
    objectives=[
        "Define enthalpy change, standard conditions and the standard enthalpies of formation, combustion, neutralisation and solution",
        "Write balanced equations that match each definition",
        "Calculate an enthalpy change from calorimetry data using q = mc(delta T)",
        "Explain why experimental values differ from data-book values",
    ],
    key_concepts=["Enthalpy change", "Exothermic", "Endothermic", "Standard conditions", "Standard enthalpy of formation",
                  "Standard enthalpy of combustion", "Enthalpy of neutralisation", "Enthalpy of solution", "Calorimetry"],
    blocks=[
        H("Introduction"),
        T(r"Charcoal on a roadside grill, wood in a village kitchen and gas in a cooker all release heat when they burn. A cold pack for a sports injury does the opposite: it takes in heat from the skin as its chemical dissolves. "
          r"Chemists compare these energy changes using **enthalpy changes**, measured under agreed standard conditions so that numbers from different laboratories can be compared."),
        H("Enthalpy change and standard conditions"),
        D(r"The **enthalpy change** $\Delta H$ of a reaction is the heat energy exchanged with the surroundings at constant pressure. $\Delta H$ is **negative** for an exothermic reaction (heat given out, temperature of surroundings rises) and **positive** for an endothermic reaction (heat taken in, temperature falls). It is measured in $\mathrm{kJ\,mol^{-1}}$.", title="Enthalpy change"),
        D(r"**Standard conditions** (marked by the symbol $\circ$ after $\Delta H$) are a pressure of 100 kPa (1 bar), a stated temperature (usually 298 K), each substance in its **standard state** (the most stable form at 100 kPa and 298 K) and solutions at $1\ \mathrm{mol\,dm^{-3}}$. Some books use 101 kPa: check your textbook.", title="Standard conditions"),
        H("Named standard enthalpy changes"),
        D(r"The **standard enthalpy of formation** $\Delta H_f^\circ$ is the enthalpy change when **one mole of a compound** is formed from its **elements in their standard states**. By definition $\Delta H_f^\circ$ of an element in its standard state is zero.",
          title="Formation", formula=r"2\mathrm{C(graphite)} + 3\mathrm{H_2(g)} + \tfrac12\mathrm{O_2(g)} \rightarrow \mathrm{C_2H_5OH(l)} \qquad \Delta H_f^\circ = -277.7\ \mathrm{kJ\,mol^{-1}}"),
        D(r"The **standard enthalpy of combustion** $\Delta H_c^\circ$ is the enthalpy change when **one mole of a substance is completely burned in oxygen**, with products in their standard states (carbon dioxide gas and liquid water).",
          title="Combustion", formula=r"\mathrm{C_2H_5OH(l)} + 3\mathrm{O_2(g)} \rightarrow 2\mathrm{CO_2(g)} + 3\mathrm{H_2O(l)} \qquad \Delta H_c^\circ = -1367\ \mathrm{kJ\,mol^{-1}}"),
        D(r"The **standard enthalpy of neutralisation** $\Delta H_{neut}^\circ$ is the enthalpy change when an acid and a base react to form **one mole of water**. For a strong acid and a strong base it is about $-57\ \mathrm{kJ\,mol^{-1}}$, because every such reaction is the same ionic change.",
          title="Neutralisation", formula=r"\mathrm{H^+(aq)} + \mathrm{OH^-(aq)} \rightarrow \mathrm{H_2O(l)} \qquad \Delta H_{neut}^\circ \approx -57\ \mathrm{kJ\,mol^{-1}}"),
        D(r"The **standard enthalpy of solution** $\Delta H_{sol}^\circ$ is the enthalpy change when **one mole of a substance dissolves** in so much water that further dilution produces no further heat change.",
          title="Solution", formula=r"\mathrm{NH_4NO_3(s)} \xrightarrow{aq} \mathrm{NH_4^+(aq)} + \mathrm{NO_3^-(aq)} \qquad \Delta H_{sol}^\circ \approx +25\ \mathrm{kJ\,mol^{-1}}"),
        T(r"Note the key phrases: **one mole** of the compound formed, **one mole** burned, **one mole** of water. If an equation gives two moles you must halve the enthalpy change for the named quantity. Fractions are allowed in the equations, as in the $\tfrac12\mathrm{O_2}$ above."),
        H("Measuring enthalpy changes: calorimetry"),
        D(r"In **calorimetry** the heat released or absorbed warms or cools a known mass of water. With $m$ the mass of water in g, $c$ its specific heat capacity ($4.18\ \mathrm{J\,g^{-1}\,K^{-1}}$) and $\Delta T$ the temperature change, the heat energy is $q$ and the molar enthalpy change follows by dividing by the moles $n$ that reacted:",
          title="Calorimetry equations", formula=r"q = mc\,\Delta T \qquad \Delta H = -\dfrac{q}{n}"),
        T(r"The minus sign appears because heat gained by the water was lost by the reaction. A temperature **rise** gives a **negative** $\Delta H$. Remember to convert $q$ from joules to kilojoules."),
        EX("Worked example 1: neutralisation", intro=r"50.0 cm$^3$ of $1.00\ \mathrm{mol\,dm^{-3}}$ hydrochloric acid is mixed with 50.0 cm$^3$ of $1.00\ \mathrm{mol\,dm^{-3}}$ sodium hydroxide in a polystyrene cup. The temperature rises by 6.8 K. Take the density of the solution as $1.00\ \mathrm{g\,cm^{-3}}$ and $c = 4.18\ \mathrm{J\,g^{-1}\,K^{-1}}$. Calculate $\Delta H_{neut}$.", steps=[
            S("Mass heated", math=r"m = 100\ \text{cm}^3 \times 1.00 = 100\ \text{g}"),
            S("Heat gained", math=r"q = 100 \times 4.18 \times 6.8 = 2842\ \text{J} = 2.842\ \text{kJ}"),
            S("Moles of water formed", math=r"n = 0.0500\ \text{dm}^3 \times 1.00 = 0.0500\ \text{mol}"),
            S("Enthalpy change per mole", math=r"\Delta H = -\dfrac{2.842}{0.0500} = -56.8\ \text{kJ mol}^{-1}"),
        ], check=r"\text{close to the accepted value of about } -57\ \text{kJ mol}^{-1}"),
        EX("Worked example 2: combustion of ethanol", intro=r"1.15 g of ethanol ($M = 46.0$) is burned under a metal can holding 250 g of water. The water temperature rises by 26.0 K. Calculate the enthalpy of combustion and say why it differs from the data-book value of $-1367\ \mathrm{kJ\,mol^{-1}}$.", steps=[
            S("Heat gained by the water", math=r"q = 250 \times 4.18 \times 26.0 = 27\,170\ \text{J} = 27.17\ \text{kJ}"),
            S("Moles of ethanol", math=r"n = \dfrac{1.15}{46.0} = 0.0250\ \text{mol}"),
            S("Enthalpy of combustion", math=r"\Delta H = -\dfrac{27.17}{0.0250} = -1087\ \text{kJ mol}^{-1}"),
            S("Compare", text="The experimental value is about 20% less exothermic than the data-book value. Much of the heat escapes to the air and warms the can; combustion may be incomplete (soot); and some ethanol evaporates."),
        ]),
        EX("Worked example 3: enthalpy of solution", intro=r"8.00 g of ammonium nitrate ($M = 80.0$) dissolves in 100 g of water and the temperature falls by 6.1 K. Take the mass heated as 100 g. Calculate $\Delta H_{sol}$ and state whether the process is exothermic.", steps=[
            S("Heat lost by the water", math=r"q = 100 \times 4.18 \times 6.1 = 2550\ \text{J} = 2.55\ \text{kJ}"),
            S("Moles dissolved", math=r"n = \dfrac{8.00}{80.0} = 0.100\ \text{mol}"),
            S("Enthalpy change", math=r"\Delta H = +\dfrac{2.55}{0.100} = +25.5\ \text{kJ mol}^{-1}", text="The temperature fell, so heat was taken in: the sign is positive and the process is endothermic."),
        ]),
        MISTAKE("Wrong sign in calorimetry", r"Temperature **rise** of the water means the reaction gave out heat: $\Delta H$ is **negative**. A temperature **fall** gives a positive $\Delta H$."),
        MISTAKE("Wrong equation for a defined enthalpy change", r"For $\Delta H_f^\circ$, the reactants must be **elements** in standard states and exactly one mole of the compound must form. For $\Delta H_c^\circ$ the equation must start with one mole of the substance burned and end with $\mathrm{CO_2(g)}$ and $\mathrm{H_2O(l)}$. For example, $\mathrm{C(graphite)} + \mathrm{O_2(g)} \rightarrow \mathrm{CO_2(g)}$ is both the formation of $\mathrm{CO_2}$ and the combustion of carbon."),
        TIP(r"Standard enthalpy changes appear in Paper 1 (matching equations and definitions) and Paper 2 (calorimetry and Hess cycles). In practical Paper 3, calorimetry needs a table of temperature readings, a plotted correction for heat loss and an estimate of error."),
        QUIZ(r"Which equation represents the standard enthalpy of formation of methanol, $\mathrm{CH_3OH(l)}$?", [
            r"$\mathrm{C(g)} + 4\mathrm{H(g)} + \mathrm{O(g)} \rightarrow \mathrm{CH_3OH(l)}$",
            r"$\mathrm{C(graphite)} + 2\mathrm{H_2(g)} + \tfrac12\mathrm{O_2(g)} \rightarrow \mathrm{CH_3OH(l)}$",
            r"$\mathrm{CH_3OH(l)} + \tfrac32\mathrm{O_2(g)} \rightarrow \mathrm{CO_2(g)} + 2\mathrm{H_2O(l)}$",
            r"$2\mathrm{C(graphite)} + 4\mathrm{H_2(g)} + \mathrm{O_2(g)} \rightarrow 2\mathrm{CH_3OH(l)}$",
        ], 1, r"Formation needs elements in their standard states (graphite, $\mathrm{H_2}$ gas, $\mathrm{O_2}$ gas) forming exactly one mole of the compound.",
             hint="What are the standard states of the elements?",
             feedback=["Gaseous atoms are not the standard states of the elements.", "", "This is the combustion of methanol.", "This forms two moles, not one."]),
        QUIZ(r"The temperature of the water in a calorimeter rises during a reaction. Which statement is correct?", [
            r"$\Delta H$ is positive because the water gained heat",
            r"$\Delta H$ is negative because the reaction released heat",
            r"$\Delta H$ is zero because energy is conserved",
            r"The reaction is endothermic",
        ], 1, r"The water gained heat from the reaction, so the reaction lost heat: $\Delta H < 0$, an exothermic reaction.",
             hint="Who lost the heat that the water gained?",
             feedback=["The sign refers to the reaction, not the water.", "", "Energy is conserved, but the reaction still loses energy to the surroundings.", "A temperature rise means heat given out: exothermic."]),
        PQ(r"Write equations that define (a) the standard enthalpy of formation of propane, $\mathrm{C_3H_8(g)}$, and (b) the standard enthalpy of combustion of propane.",
           r"(a) $3\mathrm{C(graphite)} + 4\mathrm{H_2(g)} \rightarrow \mathrm{C_3H_8(g)}$. (b) $\mathrm{C_3H_8(g)} + 5\mathrm{O_2(g)} \rightarrow 3\mathrm{CO_2(g)} + 4\mathrm{H_2O(l)}$. Each has one mole of propane; in (b) water is liquid."),
        PQ(r"25.0 cm$^3$ of $2.00\ \mathrm{mol\,dm^{-3}}$ HCl and 25.0 cm$^3$ of $2.00\ \mathrm{mol\,dm^{-3}}$ NaOH are mixed and the temperature rises by 13.5 K. Calculate $\Delta H_{neut}$ ($c = 4.18\ \mathrm{J\,g^{-1}\,K^{-1}}$, density $1.00\ \mathrm{g\,cm^{-3}}$).",
           r"$m = 50.0$ g; $q = 50.0 \times 4.18 \times 13.5 = 2821.5$ J $= 2.82$ kJ. $n = 0.0250 \times 2.00 = 0.0500$ mol. $\Delta H = -2.8215/0.0500 = -56.4\ \mathrm{kJ\,mol^{-1}}$."),
        PQ(r"1.60 g of methanol ($M = 32.0$) burned under 200 g of water raises its temperature by 38.0 K. Calculate the enthalpy of combustion of methanol and explain why the data-book value ($-726\ \mathrm{kJ\,mol^{-1}}$) is more exothermic.",
           r"$q = 200 \times 4.18 \times 38.0 = 31\,768$ J $= 31.77$ kJ. $n = 1.60/32.0 = 0.0500$ mol. $\Delta H = -31.77/0.0500 = -635\ \mathrm{kJ\,mol^{-1}}$. The experiment loses heat to the air and the can, combustion can be incomplete, and the conditions are not standard, so less heat reaches the water than the full enthalpy change."),
        SUM(r"$\Delta H < 0$ for exothermic and $\Delta H > 0$ for endothermic reactions; standard conditions are 100 kPa, 298 K and 1 mol dm$^{-3}$.",
            r"$\Delta H_f^\circ$: one mole of compound from its elements (zero for an element). $\Delta H_c^\circ$: one mole burned completely. $\Delta H_{neut}^\circ$: one mole of water formed. $\Delta H_{sol}^\circ$: one mole dissolved.",
            r"Calorimetry: $q = mc\Delta T$, then $\Delta H = -q/n$ in kJ per mole.",
            r"Experimental values are less exothermic than data-book values mainly because of heat loss and incomplete combustion."),
    ],
))

# ------------------------------------------------------------------ 5. Hess's law
LESSONS.append(lesson(
    module=M5,
    topic="Hess's law",
    title="Hess's law: energy cycles and level diagrams",
    slug="chl2-hess-law-cycles",
    minutes=22,
    summary="Hess's law states that the enthalpy change of a reaction is independent of the route; learn to build cycles, energy-level diagrams and to combine equations to find enthalpy changes that cannot be measured directly.",
    objectives=[
        "State Hess's law and explain why it follows from conservation of energy",
        "Find an unknown enthalpy change by drawing a cycle or an energy-level diagram",
        "Combine thermochemical equations by reversing and multiplying them",
        "Use solution enthalpies to find the enthalpy of hydration of a salt",
    ],
    key_concepts=["Hess's law", "State function", "Energy cycle", "Energy-level diagram", "Indirect route", "Enthalpy of hydration"],
    blocks=[
        H("Introduction"),
        T(r"When carbon burns in a limited supply of air, as in a charcoal stove with the door nearly shut, both carbon monoxide and carbon dioxide form. No one can measure the heat of making **only** carbon monoxide, because some CO$_2$ always forms. "
          r"Yet its enthalpy change is known exactly. The tool that makes this possible is **Hess's law**."),
        H("Hess's law"),
        D(r"**Hess's law** states that the total enthalpy change for a chemical reaction is the same whichever route is taken from the reactants to the products, provided the initial and final conditions are the same.",
          title="Hess's law"),
        T(r"Enthalpy is a **state function**: it depends only on the state of the system, not on how it got there. The law is the conservation of energy applied to chemical change. If two routes gave different energy changes, you could go round the loop and make energy from nothing."),
        H("Using a cycle"),
        IMG("al-chl2-hess-cycle.svg", alt="A triangle of reactions. C(s) and O2 at the top left, CO and half O2 at the top right, and CO2 at the bottom. The direct route to CO2 has enthalpy change -393.5. The two-step route goes via CO.",
            caption="Figure 1. A Hess cycle for the formation of carbon monoxide."),
        T(r"The unknown route $\Delta H_1$ goes from the elements to CO. The other route goes from the elements directly to $\mathrm{CO_2}$ ($\Delta H_2$). It also goes by way of CO and then on to $\mathrm{CO_2}$ ($\Delta H_1 + \Delta H_3$). Both routes start and end at the same places, so they must have the same total enthalpy change."),
        KEY("A method that always works", r"Draw the arrows, label every known enthalpy change, then equate the two routes.",
            cards=[["Step 1", "Write the equation you want, and the data equations."],
                   ["Step 2", "Find a common substance that all reactions can reach (often the combustion products)."],
                   ["Step 3", "Draw arrows from the start to the end by two routes."],
                   ["Step 4", "Route A total = Route B total; solve for the unknown."]]),
        EX("Worked example 1: enthalpy of formation of carbon monoxide", intro=r"Given $\Delta H_c^\circ(\mathrm{C,\ graphite}) = -393.5\ \mathrm{kJ\,mol^{-1}}$ and $\Delta H_c^\circ(\mathrm{CO}) = -283.0\ \mathrm{kJ\,mol^{-1}}$, find $\Delta H_f^\circ(\mathrm{CO})$.", steps=[
            S("Route 1 (direct)", math=r"\mathrm{C} + \mathrm{O_2} \rightarrow \mathrm{CO_2} \qquad \Delta H_2 = -393.5"),
            S("Route 2 (via CO)", math=r"\mathrm{C} + \tfrac12\mathrm{O_2} \rightarrow \mathrm{CO} \quad (\Delta H_1) \qquad \mathrm{CO} + \tfrac12\mathrm{O_2} \rightarrow \mathrm{CO_2} \quad (\Delta H_3 = -283.0)"),
            S("Equate the routes", math=r"\Delta H_1 + \Delta H_3 = \Delta H_2"),
            S("Solve", math=r"\Delta H_1 = -393.5 - (-283.0) = -110.5\ \text{kJ mol}^{-1}"),
        ], check=r"-110.5 + (-283.0) = -393.5"),
        H("Using energy-level diagrams"),
        T(r"An **energy-level diagram** draws each substance at a height that stands for its enthalpy. A downward arrow is exothermic, an upward arrow is endothermic. In example 1 the elements sit at the top, $\mathrm{CO_2}$ at the bottom, and CO in between. "
          r"The length of the arrow from the elements to $\mathrm{CO_2}$ (393.5) is the sum of the arrow to CO and the arrow from CO to $\mathrm{CO_2}$ (110.5 + 283.0)."),
        H("Combining equations"),
        T(r"Instead of drawing, you may combine the given equations. Rules: if you **reverse** an equation, change the sign of $\Delta H$. If you **multiply** an equation by a number, multiply $\Delta H$ by the same number. Then add the equations and the enthalpy changes, cancelling species that appear on both sides."),
        EX("Worked example 2: enthalpy of formation of methane", intro=r"Find $\Delta H_f^\circ(\mathrm{CH_4})$ for $\mathrm{C(graphite)} + 2\mathrm{H_2(g)} \rightarrow \mathrm{CH_4(g)}$. Data: $\Delta H_c^\circ(\mathrm{C}) = -393.5$, $\Delta H_c^\circ(\mathrm{H_2}) = -285.8$ and $\Delta H_c^\circ(\mathrm{CH_4}) = -890.3\ \mathrm{kJ\,mol^{-1}}$.", steps=[
            S("Keep the carbon equation", math=r"\mathrm{C} + \mathrm{O_2} \rightarrow \mathrm{CO_2} \qquad -393.5"),
            S("Double the hydrogen equation", math=r"2\mathrm{H_2} + \mathrm{O_2} \rightarrow 2\mathrm{H_2O(l)} \qquad 2(-285.8) = -571.6"),
            S("Reverse the methane equation", math=r"\mathrm{CO_2} + 2\mathrm{H_2O(l)} \rightarrow \mathrm{CH_4} + 2\mathrm{O_2} \qquad +890.3"),
            S("Add", math=r"\mathrm{C} + 2\mathrm{H_2} \rightarrow \mathrm{CH_4} \qquad -393.5 - 571.6 + 890.3 = -74.8\ \text{kJ mol}^{-1}", text="$\\mathrm{CO_2}$, $\\mathrm{H_2O}$ and $\\mathrm{O_2}$ cancel."),
        ], check=r"-393.5 - 571.6 + 890.3 = -74.8"),
        EX("Worked example 3: hydration of copper(II) sulfate", intro=r"Anhydrous copper(II) sulfate cannot be hydrated cleanly inside a calorimeter, but its enthalpies of solution can be measured. $\Delta H_{sol}(\mathrm{CuSO_4(s)}) = -66.1$ and $\Delta H_{sol}(\mathrm{CuSO_4{\cdot}5H_2O(s)}) = +11.7\ \mathrm{kJ\,mol^{-1}}$. Find $\Delta H$ for $\mathrm{CuSO_4(s)} + 5\mathrm{H_2O(l)} \rightarrow \mathrm{CuSO_4{\cdot}5H_2O(s)}$.", steps=[
            S("Draw the cycle", text="Both solids dissolve to give the same solution, $\\mathrm{Cu^{2+}(aq)} + \\mathrm{SO_4^{2-}(aq)}$."),
            S("Two routes from anhydrous salt to solution", math=r"\Delta H_{hyd} + (+11.7) = -66.1"),
            S("Solve", math=r"\Delta H_{hyd} = -66.1 - 11.7 = -77.8\ \text{kJ mol}^{-1}", text="Hydration is strongly exothermic: white powder turns blue and warms."),
        ]),
        MISTAKE("Not changing the sign when reversing", r"Reversing an equation reverses the heat flow: $\Delta H$ changes sign. Forgetting this is the most common error in Hess cycles."),
        MISTAKE("Not multiplying the enthalpy change", r"If the equation is doubled to balance, $\Delta H$ doubles too. Match the number of moles in your final equation."),
        TIP(r"Hess's law questions occupy a large share of Paper 2 energetics. Always show the cycle or the combined equations: examiners give marks for the method even if the arithmetic slips."),
        QUIZ(r"Hess's law is a consequence of which principle?", ["Conservation of mass", "Conservation of energy", "Le Chatelier's principle", "The ideal gas law"], 1,
             r"Enthalpy is a state function: if two routes gave different totals, energy would be created or destroyed around the loop.",
             hint="What cannot be created or destroyed?",
             feedback=["Mass is conserved, but that does not fix enthalpy totals.", "", "That concerns equilibrium shifts.", "That concerns gases only."]),
        QUIZ(r"The enthalpy change of reaction X is $-100\ \mathrm{kJ\,mol^{-1}}$. What is $\Delta H$ for $2$ moles of the **reverse** reaction?", [r"$-200$", r"$+200$", r"$+100$", r"$-100$"], 1,
             r"Reversing changes the sign (to $+100$) and doubling doubles the size: $+200\ \mathrm{kJ}$.", hint="Change the sign, then multiply.",
             feedback=["Doubling is right but the sign has not changed.", "", "The sign changed but not the doubling.", "Neither the sign nor the amount was adjusted."]),
        PQ(r"Use $\Delta H_c^\circ(\mathrm{C}) = -393.5$, $\Delta H_c^\circ(\mathrm{H_2}) = -285.8$ and $\Delta H_c^\circ(\mathrm{C_2H_6}) = -1560\ \mathrm{kJ\,mol^{-1}}$ to find $\Delta H_f^\circ(\mathrm{C_2H_6})$.",
           r"Target: $2\mathrm{C} + 3\mathrm{H_2} \rightarrow \mathrm{C_2H_6}$. Add $2 \times (-393.5) = -787.0$, $3 \times (-285.8) = -857.4$ and the reverse of the ethane combustion, $+1560$. Total $= -787.0 - 857.4 + 1560 = -84.4\ \mathrm{kJ\,mol^{-1}}$."),
        PQ(r"Given $\Delta H_f^\circ(\mathrm{NO_2}) = +33.2$ and $\Delta H_f^\circ(\mathrm{N_2O_4}) = +9.2\ \mathrm{kJ\,mol^{-1}}$, find $\Delta H$ for $2\mathrm{NO_2(g)} \rightarrow \mathrm{N_2O_4(g)}$.",
           r"Route 1: $\mathrm{N_2} + 2\mathrm{O_2} \rightarrow 2\mathrm{NO_2}$, $\Delta H = 2 \times 33.2 = +66.4$. Route 2: $\mathrm{N_2} + 2\mathrm{O_2} \rightarrow \mathrm{N_2O_4}$, $\Delta H = +9.2$. $\Delta H(\text{dimerisation}) = 9.2 - 66.4 = -57.2\ \mathrm{kJ\,mol^{-1}}$ (bond forming is exothermic)."),
        PQ(r"Explain, using conservation of energy, why the enthalpy change for converting graphite to diamond is the same whether it is calculated from combustion data or from an imagined direct conversion.",
           r"Both substances burn to the same product, $\mathrm{CO_2}$. The energy released burning graphite minus the energy released burning diamond is the energy difference between the two forms. Energy is conserved and enthalpy is a state function, so the result depends only on the start (graphite) and the end (diamond), not on the route."),
        SUM(r"Hess's law: $\Delta H$ is the same by any route between the same start and end points.",
            r"Cycles: equate the sum of arrows along two routes. Energy-level diagrams show the same with heights.",
            r"Combining equations: reverse changes the sign, multiplying multiplies $\Delta H$, then add and cancel.",
            r"Solution enthalpies let us find hydration and other enthalpies that cannot be measured directly."),
    ],
))

# ------------------------------------------------------------------ 6. Hess with formation and combustion data
LESSONS.append(lesson(
    module=M5,
    topic="Hess's law",
    title="Enthalpy changes from formation and combustion data",
    slug="chl2-hess-formation-combustion",
    minutes=22,
    summary="The two ready-made Hess formulae, delta H = sum of formation enthalpies of products minus reactants and the combustion version, with worked sign checks.",
    objectives=[
        "Derive and use delta H = sum of delta Hf (products) minus sum of delta Hf (reactants)",
        "Derive and use delta H = sum of delta Hc (reactants) minus sum of delta Hc (products)",
        "Calculate unknown enthalpies of formation and combustion from data tables",
        "Avoid sign, mole-number and state errors",
    ],
    key_concepts=["Enthalpy of formation", "Enthalpy of combustion", "Reaction enthalpy", "Elements in standard states", "Product minus reactant"],
    blocks=[
        H("Introduction"),
        T(r"Tables of standard enthalpies of formation are printed at the back of every chemistry textbook. A single number for each compound lets you predict the enthalpy change of thousands of reactions without a calorimeter. "
          r"In this lesson you turn the cycle of the last lesson into two short formulae and practise using them."),
        H("The formation formula"),
        T(r"Imagine every reaction taking an indirect route: break the reactants down into their elements, then build the products from those elements. The first step is the reverse of formation (opposite sign); the second step is formation."),
        D(r"The enthalpy change of any reaction equals the total standard enthalpy of formation of the products minus that of the reactants, each multiplied by its coefficient in the balanced equation.",
          title="Formation formula", formula=r"\Delta H^\circ_{reaction} = \sum n\,\Delta H_f^\circ(\text{products}) - \sum n\,\Delta H_f^\circ(\text{reactants})"),
        T(r"Elements in their standard states have $\Delta H_f^\circ = 0$, so they drop out of the sums."),
        H("The combustion formula"),
        T(r"Now take the other indirect route: burn the reactants completely, then reverse the burning of the products. Reactants burn (their $\Delta H_c$), and the products' burning is reversed (minus their $\Delta H_c$). So the combustion formula has reactants first:"),
        D(r"The enthalpy change of a reaction equals the total standard enthalpy of combustion of the **reactants** minus that of the **products**.",
          title="Combustion formula", formula=r"\Delta H^\circ_{reaction} = \sum n\,\Delta H_c^\circ(\text{reactants}) - \sum n\,\Delta H_c^\circ(\text{products})"),
        KEY("Remember the order", r"The order is opposite in the two formulae. Think of where the arrows point.",
            cards=[["Formation data", "Products minus reactants"], ["Combustion data", "Reactants minus products"],
                   ["Sign check", "Exothermic reactions should give negative answers when products are more stable"]]),
        CODE("substance         dHf / kJ per mol      substance        dHc / kJ per mol\n"
             "CO2(g)            -393.5                C(graphite)      -393.5\n"
             "H2O(l)            -285.8                H2(g)            -285.8\n"
             "C2H5OH(l)         -277.7                C3H8(g)          -2219.2\n"
             "CaCO3(s)          -1206.9               C2H4(g)          -1411\n"
             "CaO(s)            -635.1                C2H6(g)          -1560\n"
             "Fe2O3(s)          -824.2\n"
             "CO(g)             -110.5", "text", title="Data used in this lesson (typical textbook values)"),
        EX("Worked example 1: combustion of ethanol from formation data", intro=r"Calculate $\Delta H_c^\circ$ of ethanol using the table.", steps=[
            S("Equation", math=r"\mathrm{C_2H_5OH(l)} + 3\mathrm{O_2(g)} \rightarrow 2\mathrm{CO_2(g)} + 3\mathrm{H_2O(l)}"),
            S("Products", math=r"2(-393.5) + 3(-285.8) = -787.0 - 857.4 = -1644.4"),
            S("Reactants", math=r"(-277.7) + 3(0) = -277.7", text="Oxygen is an element in its standard state: zero."),
            S("Subtract", math=r"\Delta H = -1644.4 - (-277.7) = -1366.7\ \text{kJ mol}^{-1}"),
        ], check=r"\text{matches the data-book value of about } -1367\ \text{kJ mol}^{-1}"),
        EX("Worked example 2: enthalpy of formation of propane from combustion data", intro=r"Use $\Delta H_c^\circ(\mathrm{C}) = -393.5$, $\Delta H_c^\circ(\mathrm{H_2}) = -285.8$ and $\Delta H_c^\circ(\mathrm{C_3H_8}) = -2219.2\ \mathrm{kJ\,mol^{-1}}$ to find $\Delta H_f^\circ(\mathrm{C_3H_8})$.", steps=[
            S("Equation", math=r"3\mathrm{C(graphite)} + 4\mathrm{H_2(g)} \rightarrow \mathrm{C_3H_8(g)}"),
            S("Reactants burn", math=r"3(-393.5) + 4(-285.8) = -1180.5 - 1143.2 = -2323.7"),
            S("Product burns", math=r"\Delta H_c(\mathrm{C_3H_8}) = -2219.2"),
            S("Reactants minus products", math=r"\Delta H = -2323.7 - (-2219.2) = -104.5\ \text{kJ mol}^{-1}"),
        ]),
        EX("Worked example 3: hydrogenation of ethene", intro=r"Calculate $\Delta H$ for $\mathrm{C_2H_4(g)} + \mathrm{H_2(g)} \rightarrow \mathrm{C_2H_6(g)}$ using $\Delta H_c^\circ$ of ethene $-1411$, hydrogen $-285.8$ and ethane $-1560\ \mathrm{kJ\,mol^{-1}}$.", steps=[
            S("Reactants burn", math=r"-1411 + (-285.8) = -1696.8"),
            S("Product burns", math=r"-1560"),
            S("Reactants minus products", math=r"\Delta H = -1696.8 - (-1560) = -136.8\ \text{kJ mol}^{-1}", text="The reaction is exothermic. This value is also used to check the bond-enthalpy estimate in the next lesson."),
        ]),
        EX("Worked example 4: thermal decomposition", intro=r"Calculate $\Delta H$ for $\mathrm{CaCO_3(s)} \rightarrow \mathrm{CaO(s)} + \mathrm{CO_2(g)}$ using the formation data in the table.", steps=[
            S("Products", math=r"(-635.1) + (-393.5) = -1028.6"),
            S("Reactant", math=r"-1206.9"),
            S("Products minus reactants", math=r"\Delta H = -1028.6 - (-1206.9) = +178.3\ \text{kJ mol}^{-1}", text="Strongly endothermic: this is why lime kilns need continuous high heat."),
        ]),
        MISTAKE("Forgetting the coefficients", r"If the equation has $3\mathrm{H_2O}$, the enthalpy of formation of water is multiplied by 3. Balance the equation first."),
        MISTAKE("Using the wrong state of water", r"$\Delta H_f^\circ(\mathrm{H_2O(l)}) = -285.8$ but $\Delta H_f^\circ(\mathrm{H_2O(g)}) = -241.8$. Always check which state the equation shows."),
        TIP(r"Write 'products minus reactants' on your paper before you start. In Paper 2, quote the formula and show each sum separately; the working earns marks even if the final number is wrong."),
        QUIZ(r"Which expression gives $\Delta H$ for a reaction from standard enthalpies of **combustion**?", [
            r"$\Sigma\Delta H_c(\text{products}) - \Sigma\Delta H_c(\text{reactants})$",
            r"$\Sigma\Delta H_c(\text{reactants}) - \Sigma\Delta H_c(\text{products})$",
            r"$\Sigma\Delta H_c(\text{reactants}) + \Sigma\Delta H_c(\text{products})$",
            r"$\Sigma\Delta H_f(\text{reactants}) - \Sigma\Delta H_f(\text{products})$",
        ], 1, r"Burn the reactants, then reverse the burning of the products: reactants minus products.",
             hint="The combustion route goes through the combustion products.",
             feedback=["This is the formation version applied to combustion data.", "", "Adding is never correct.", "This mixes formation data with the wrong order."]),
        QUIZ(r"Why do elements in their standard states not appear in a formation sum?", [
            "They have no mass", "Their enthalpy of formation is zero by definition", "They are not involved in the reaction",
            "Their enthalpy is always negative"], 1, r"Forming an element from itself involves no change, so $\Delta H_f^\circ = 0$.",
             hint="What is the reaction for forming an element from itself?",
             feedback=["They have mass and take part.", "", "They often are involved (for example $\\mathrm{O_2}$ in combustion).", "Their value is zero, not negative."]),
        PQ(r"Calculate $\Delta H$ for $\mathrm{Fe_2O_3(s)} + 3\mathrm{CO(g)} \rightarrow 2\mathrm{Fe(s)} + 3\mathrm{CO_2(g)}$ using $\Delta H_f^\circ$: $\mathrm{Fe_2O_3} = -824.2$, $\mathrm{CO} = -110.5$, $\mathrm{CO_2} = -393.5\ \mathrm{kJ\,mol^{-1}}$.",
           r"Products: $2(0) + 3(-393.5) = -1180.5$. Reactants: $-824.2 + 3(-110.5) = -1155.7$. $\Delta H = -1180.5 - (-1155.7) = -24.8\ \mathrm{kJ\,mol^{-1}}$ per mole of $\mathrm{Fe_2O_3}$."),
        PQ(r"The enthalpy of combustion of liquid benzene is $-3267\ \mathrm{kJ\,mol^{-1}}$. Using $\Delta H_c^\circ(\mathrm{C}) = -393.5$ and $\Delta H_c^\circ(\mathrm{H_2}) = -285.8$, find $\Delta H_f^\circ(\mathrm{C_6H_6(l)})$.",
           r"$6\mathrm{C} + 3\mathrm{H_2} \rightarrow \mathrm{C_6H_6}$. Reactants: $6(-393.5) + 3(-285.8) = -2361.0 - 857.4 = -3218.4$. $\Delta H = -3218.4 - (-3267) = +48.6\ \mathrm{kJ\,mol^{-1}}$."),
        PQ(r"Calculate $\Delta H_c^\circ$ of butane, $\mathrm{C_4H_{10}(g)}$, given $\Delta H_f^\circ$ of butane $= -125.7$, $\mathrm{CO_2} = -393.5$ and $\mathrm{H_2O(l)} = -285.8\ \mathrm{kJ\,mol^{-1}}$.",
           r"$\mathrm{C_4H_{10}} + \tfrac{13}{2}\mathrm{O_2} \rightarrow 4\mathrm{CO_2} + 5\mathrm{H_2O(l)}$. Products: $4(-393.5) + 5(-285.8) = -1574.0 - 1429.0 = -3003.0$. Reactant: $-125.7$. $\Delta H = -3003.0 + 125.7 = -2877.3\ \mathrm{kJ\,mol^{-1}}$."),
        SUM(r"Formation data: $\Delta H = \Sigma n\Delta H_f(\text{products}) - \Sigma n\Delta H_f(\text{reactants})$.",
            r"Combustion data: $\Delta H = \Sigma n\Delta H_c(\text{reactants}) - \Sigma n\Delta H_c(\text{products})$.",
            r"Elements in their standard states have $\Delta H_f = 0$. Multiply each value by its coefficient and check the state of water.",
            r"Always write the balanced equation first and check that the sign matches whether the reaction should be exothermic or endothermic."),
    ],
))

# ------------------------------------------------------------------ 7. Bond enthalpies
LESSONS.append(lesson(
    module=M5,
    topic="Bond dissociation energies",
    title="Bond dissociation enthalpies and estimating enthalpy changes",
    slug="chl2-bond-enthalpies",
    minutes=22,
    summary="Bond dissociation and mean bond enthalpies, and the method delta H = bonds broken minus bonds formed, with comparisons against Hess-cycle values.",
    objectives=[
        "Define bond dissociation enthalpy and mean bond enthalpy",
        "Explain why bond breaking is endothermic and bond making exothermic",
        "Estimate the enthalpy change of a gas-phase reaction from mean bond enthalpies",
        "Explain why bond-enthalpy estimates differ from Hess-cycle values",
    ],
    key_concepts=["Bond dissociation enthalpy", "Mean bond enthalpy", "Bond breaking", "Bond making", "Gaseous state", "Estimated enthalpy change"],
    blocks=[
        H("Introduction"),
        T(r"When a butane cooker burns, the heat comes from rearranging atoms. Old bonds in butane and oxygen break, which costs energy. New bonds in carbon dioxide and water form, which releases energy. "
          r"The release is larger than the cost, so the flame gives out heat. If we know the energy of each type of bond, we can estimate the heat of a reaction without doing an experiment."),
        H("Bond dissociation enthalpy"),
        D(r"The **bond dissociation enthalpy** is the enthalpy change when **one mole of a particular bond** in a gaseous molecule is broken, forming gaseous atoms or fragments. It is always positive (endothermic) because energy must be supplied to pull atoms apart.",
          title="Bond dissociation enthalpy", formula=r"\mathrm{H_2(g)} \rightarrow 2\mathrm{H(g)} \qquad \Delta H = +436\ \mathrm{kJ\,mol^{-1}}"),
        D(r"The **mean bond enthalpy** is the average of the bond dissociation enthalpy of a given type of bond (such as C-H) taken over many different compounds. In methane the four C-H bonds are broken one after another with slightly different enthalpies; their mean is 413 kJ per mole.",
          title="Mean bond enthalpy"),
        CODE("bond     mean enthalpy / kJ per mol       bond     mean enthalpy / kJ per mol\n"
             "H-H       436                              C-H       413\n"
             "C-C       347                              C=C       614\n"
             "C-O       358                              C=O in CO2  805\n"
             "O-H       464                              O=O       498\n"
             "N-H       391                              N#N       945\n"
             "Cl-Cl     243                              H-Cl      432\n"
             "C-Cl      346                              Br-Br     193\n"
             "H-Br      366                              C-Br      285", "text", title="Mean bond enthalpies used in this lesson (typical textbook values; sources differ slightly)"),
        T(r"Notice that a double bond is stronger than a single bond (614 against 347) but less than twice as strong. A triple bond, as in $\mathrm{N_2}$ at 945, is very strong: this is why nitrogen is so unreactive."),
        H("The calculation method"),
        D(r"For a reaction in which all substances are gases, the enthalpy change is the energy needed to break all the bonds in the reactants minus the energy released when the bonds in the products form.",
          title="Bond enthalpy method", formula=r"\Delta H \approx \sum(\text{bonds broken}) - \sum(\text{bonds formed})"),
        KEY("Four steps", r"Always draw the full structural formula so you can count every bond.",
            cards=[["1", "Draw the bonds of each molecule (full structural formulae)."],
                   ["2", "Add the enthalpies of all the bonds broken (positive)."],
                   ["3", "Add the enthalpies of all the bonds formed."],
                   ["4", "Subtract: broken minus formed. A negative answer means exothermic."]]),
        EX("Worked example 1: combustion of methane (gas)", intro=r"Estimate $\Delta H$ for $\mathrm{CH_4(g)} + 2\mathrm{O_2(g)} \rightarrow \mathrm{CO_2(g)} + 2\mathrm{H_2O(g)}$.", steps=[
            S("Bonds broken", math=r"4(\text{C-H}) + 2(\text{O=O}) = 4(413) + 2(498) = 1652 + 996 = 2648\ \text{kJ}"),
            S("Bonds formed", math=r"2(\text{C=O}) + 4(\text{O-H}) = 2(805) + 4(464) = 1610 + 1856 = 3466\ \text{kJ}"),
            S("Subtract", math=r"\Delta H = 2648 - 3466 = -818\ \text{kJ mol}^{-1}"),
            S("Compare", text="The Hess value for gaseous water is $-802.3\\ \\mathrm{kJ\\,mol^{-1}}$ (from formation data). The estimate is within about 2%."),
        ]),
        EX("Worked example 2: ammonia synthesis", intro=r"Estimate $\Delta H$ for $\mathrm{N_2(g)} + 3\mathrm{H_2(g)} \rightarrow 2\mathrm{NH_3(g)}$.", steps=[
            S("Bonds broken", math=r"\text{N}{\equiv}\text{N} + 3(\text{H-H}) = 945 + 3(436) = 2253\ \text{kJ}"),
            S("Bonds formed", math=r"6(\text{N-H}) = 6(391) = 2346\ \text{kJ}", text="Each $\\mathrm{NH_3}$ has 3 N-H bonds."),
            S("Subtract", math=r"\Delta H = 2253 - 2346 = -93\ \text{kJ per equation}", text="The measured value is $-92.4$ kJ: excellent agreement."),
        ]),
        EX("Worked example 3: chlorination of methane", intro=r"Estimate $\Delta H$ for $\mathrm{CH_4(g)} + \mathrm{Cl_2(g)} \rightarrow \mathrm{CH_3Cl(g)} + \mathrm{HCl(g)}$.", steps=[
            S("Bonds broken", math=r"\text{C-H} + \text{Cl-Cl} = 413 + 243 = 656\ \text{kJ}", text="Only one C-H bond in methane is replaced."),
            S("Bonds formed", math=r"\text{C-Cl} + \text{H-Cl} = 346 + 432 = 778\ \text{kJ}"),
            S("Subtract", math=r"\Delta H = 656 - 778 = -122\ \text{kJ mol}^{-1}"),
        ]),
        EX("Worked example 4: hydrogenation of ethene", intro=r"Estimate $\Delta H$ for $\mathrm{C_2H_4(g)} + \mathrm{H_2(g)} \rightarrow \mathrm{C_2H_6(g)}$ and compare it with the Hess value of $-136.8\ \mathrm{kJ\,mol^{-1}}$ from the last lesson.", steps=[
            S("Bonds broken", math=r"\text{C=C} + \text{H-H} = 614 + 436 = 1050\ \text{kJ}"),
            S("Bonds formed", math=r"\text{C-C} + 2(\text{C-H}) = 347 + 826 = 1173\ \text{kJ}", text="The C=C becomes C-C and two new C-H bonds appear."),
            S("Subtract", math=r"\Delta H = 1050 - 1173 = -123\ \text{kJ mol}^{-1}"),
            S("Compare", text="The estimate $-123$ is about 10% smaller in size than $-136.8$. Mean values are averages and the real C=C, C-C and C-H bonds in these molecules differ a little from the means."),
        ]),
        H("Limits of the method"),
        T(r"Bond-enthalpy estimates are less accurate than Hess cycles using measured $\Delta H_f$ because mean values are averages. They also apply only to **gaseous** substances. If water appears as a liquid, the extra enthalpy of condensation must be added (about $-44\ \mathrm{kJ}$ per mole), and likewise for any solid or liquid reactant."),
        MISTAKE("Counting too few bonds", r"Draw the structures. $\mathrm{CO_2}$ has **two** C=O bonds. $\mathrm{H_2O}$ has **two** O-H bonds, and $2\mathrm{H_2O}$ has four. $\mathrm{NH_3}$ has three N-H bonds."),
        MISTAKE("Reversing the subtraction", r"With bond enthalpies the order is **broken minus formed**. With formation data it is products minus reactants. Using the wrong one gives the wrong sign."),
        TIP(r"Paper 1 and Paper 2 both use bond enthalpies. Quote the table values you use, show the broken and formed totals separately, and note that estimates apply to gases."),
        QUIZ(r"Which statement about bond enthalpies is correct?", [
            "Bond making is endothermic and bond breaking is exothermic",
            "Bond breaking is endothermic and bond making is exothermic",
            "Both bond breaking and bond making are endothermic",
            "Both bond breaking and bond making are exothermic",
        ], 1, r"Energy must be supplied to pull atoms apart (breaking is endothermic). Energy is released when atoms come together (making is exothermic).",
             hint="Does it take energy to pull two magnets apart?",
             feedback=["This is reversed.", "", "Making bonds releases energy.", "Breaking bonds takes in energy."]),
        QUIZ(r"Why is the bond-enthalpy estimate for a reaction usually less accurate than a value from $\Delta H_f$ data?", [
            "Bond enthalpies cannot be measured",
            "Mean bond enthalpies are averages over many compounds and apply to gases",
            "Bond enthalpies are always negative",
            "Hess cycles ignore bonds",
        ], 1, r"A mean value is not exact for the specific bond in each molecule, and liquids or solids need extra enthalpies of state change.",
             hint="Think about the word 'mean'.", feedback=["They can be measured.", "", "They are positive for breaking.", "Hess cycles use measured enthalpy changes that already include the actual bonds."]),
        PQ(r"Estimate $\Delta H$ for $\mathrm{H_2(g)} + \mathrm{Cl_2(g)} \rightarrow 2\mathrm{HCl(g)}$ using H-H 436, Cl-Cl 243, H-Cl 432 kJ per mole.",
           r"Broken: $436 + 243 = 679$. Formed: $2 \times 432 = 864$. $\Delta H = 679 - 864 = -185\ \mathrm{kJ\,mol^{-1}}$ (per equation)."),
        PQ(r"Estimate $\Delta H$ for $\mathrm{C_2H_6(g)} \rightarrow \mathrm{C_2H_4(g)} + \mathrm{H_2(g)}$ (data in the table). Explain why the sign is the opposite of that in worked example 4.",
           r"Broken: C-C $347$ + 2 C-H $826 = 1173$. Formed: C=C $614$ + H-H $436 = 1050$. $\Delta H = 1173 - 1050 = +123\ \mathrm{kJ\,mol^{-1}}$. This is the reverse of the hydrogenation, so the enthalpy change has the same size and the opposite sign."),
        PQ(r"The enthalpy change for $\mathrm{CH_4(g)} \rightarrow \mathrm{C(g)} + 4\mathrm{H(g)}$ is $+1652\ \mathrm{kJ\,mol^{-1}}$. Calculate the mean C-H bond enthalpy, and explain why it is a mean.",
           r"Four C-H bonds are broken: $1652/4 = 413\ \mathrm{kJ\,mol^{-1}}$. It is a mean because the four bonds are broken one after another and each requires a slightly different energy; the mean value is also used for C-H bonds in other compounds."),
        SUM(r"Bond breaking is endothermic; bond making is exothermic. Bond dissociation enthalpies are positive.",
            r"For gases: $\Delta H \approx \Sigma(\text{bonds broken}) - \Sigma(\text{bonds formed})$.",
            r"Draw structures and count every bond; use mean values from the data table.",
            r"Estimates differ from Hess-cycle values because mean bond enthalpies are averages and the method is exact only for gases."),
    ],
))

# ------------------------------------------------------------------ 8. Born-Haber cycles
LESSONS.append(lesson(
    module=M5,
    topic="Lattice energy and Born-Haber cycles",
    title="Lattice enthalpy and the Born-Haber cycle",
    slug="chl2-born-haber-cycles",
    minutes=24,
    summary="Build a Born-Haber cycle from atomisation, ionisation, electron affinity and lattice enthalpy to find an unknown term for NaCl and MgCl2.",
    objectives=[
        "Define lattice enthalpy, enthalpy of atomisation, ionisation enthalpy and electron affinity",
        "Draw a Born-Haber cycle for an ionic compound such as NaCl or MgCl2",
        "Calculate the lattice enthalpy or another unknown term from the cycle using Hess's law",
        "Include the correct number of moles and the second ionisation enthalpy where needed",
    ],
    key_concepts=["Lattice enthalpy", "Enthalpy of atomisation", "Ionisation enthalpy", "Electron affinity", "Born-Haber cycle", "Enthalpy of formation"],
    blocks=[
        H("Introduction"),
        T(r"Table salt forms when sodium metal burns in chlorine gas, giving out a lot of heat. Why is the product so stable? You cannot measure directly how much energy the ions release when they pack into a crystal. "
          r"The **Born-Haber cycle** uses Hess's law to find that energy from other measured quantities."),
        H("The definitions you need"),
        D(r"The **lattice enthalpy** $\Delta H_{latt}$ is the enthalpy change when **one mole of an ionic solid forms from its gaseous ions**. It is exothermic (negative). *Convention note:* some books define lattice enthalpy as the reverse (dissociation of the solid into gaseous ions, a positive value). Check your textbook. This course uses the formation convention.",
          title="Lattice enthalpy", formula=r"\mathrm{Na^+(g)} + \mathrm{Cl^-(g)} \rightarrow \mathrm{NaCl(s)} \qquad \Delta H_{latt} = -787\ \mathrm{kJ\,mol^{-1}}"),
        D(r"The **enthalpy of atomisation** $\Delta H_{at}$ is the enthalpy change when **one mole of gaseous atoms** forms from the element in its standard state. It is positive. For chlorine, the standard state is $\mathrm{Cl_2(g)}$, so $\tfrac12\mathrm{Cl_2(g)} \rightarrow \mathrm{Cl(g)}$ is $+122\ \mathrm{kJ\,mol^{-1}}$.", title="Atomisation"),
        D(r"The **first ionisation enthalpy** is the enthalpy change when one mole of gaseous atoms loses one mole of electrons to form gaseous $+1$ ions. It is positive. The second ionisation enthalpy removes a second electron from each $+1$ ion and is larger.", title="Ionisation"),
        D(r"The **first electron affinity** is the enthalpy change when one mole of gaseous atoms gains one mole of electrons to form gaseous $-1$ ions. It is negative for most non-metals (for chlorine $-349\ \mathrm{kJ\,mol^{-1}}$). The second electron affinity (adding an electron to a $-1$ ion) is positive.", title="Electron affinity"),
        H("The cycle for sodium chloride"),
        IMG("al-chl2-born-haber-nacl.svg", alt="Energy-level diagram: sodium solid and half chlorine at zero; up arrows for atomisation of sodium, atomisation of chlorine, ionisation of sodium; down arrows for electron affinity of chlorine and lattice enthalpy; a long arrow from the elements down to NaCl solid for the enthalpy of formation.",
            caption="Figure 1. Born-Haber cycle for NaCl. Steps up take in energy; steps down give it out."),
        T(r"The long route from the elements to $\mathrm{NaCl(s)}$ is the direct **formation** step. The other route goes through gaseous atoms, gaseous ions and finally the lattice. By Hess's law the two totals are equal."),
        F(r"\Delta H_f = \Delta H_{at}(\text{Na}) + \Delta H_{at}(\tfrac12\text{Cl}_2) + IE_1(\text{Na}) + EA_1(\text{Cl}) + \Delta H_{latt}", title="The NaCl cycle as an equation"),
        CODE("data for sodium chloride (kJ per mol)\n"
             "enthalpy of formation of NaCl(s)        -411\n"
             "atomisation of Na(s)                    +107\n"
             "atomisation of 1/2 Cl2(g)               +122\n"
             "first ionisation enthalpy of Na         +496\n"
             "first electron affinity of Cl           -349", "text", title="Teaching data (typical textbook values)"),
        EX("Worked example 1: lattice enthalpy of NaCl", intro=r"Use the data to calculate $\Delta H_{latt}$ for sodium chloride.", steps=[
            S("Write the equation", math=r"\Delta H_f = \Delta H_{at}(\mathrm{Na}) + \Delta H_{at}(\mathrm{Cl}) + IE_1 + EA_1 + \Delta H_{latt}"),
            S("Add the known steps", math=r"107 + 122 + 496 + (-349) = +376\ \text{kJ}"),
            S("Rearrange", math=r"\Delta H_{latt} = \Delta H_f - 376 = -411 - 376"),
            S("Result", math=r"\Delta H_{latt} = -787\ \text{kJ mol}^{-1}"),
        ], check=r"376 + (-787) = -411"),
        H("A cycle with a 2+ ion: magnesium chloride"),
        T(r"For $\mathrm{MgCl_2}$ two changes occur. Magnesium loses **two** electrons (first and second ionisation enthalpies) and there are **two** chlorine atoms (double the atomisation and electron affinity)."),
        CODE("data for magnesium chloride (kJ per mol)\n"
             "enthalpy of formation of MgCl2(s)       -641\n"
             "atomisation of Mg(s)                    +148\n"
             "first ionisation enthalpy of Mg         +738\n"
             "second ionisation enthalpy of Mg        +1451\n"
             "atomisation of Cl2(g) (2 Cl atoms)      +244\n"
             "first electron affinity of Cl (x2)      -698", "text", title="Teaching data (typical textbook values)"),
        EX("Worked example 2: lattice enthalpy of MgCl2", intro=r"Calculate $\Delta H_{latt}$ for $\mathrm{MgCl_2}$.", steps=[
            S("Sum of the gaseous steps", math=r"148 + 738 + 1451 + 244 + (-698) = +1883\ \text{kJ}"),
            S("Rearrange", math=r"\Delta H_{latt} = \Delta H_f - 1883 = -641 - 1883"),
            S("Result", math=r"\Delta H_{latt} = -2524\ \text{kJ mol}^{-1}", text="Much more exothermic than NaCl (-787): the $\\mathrm{Mg^{2+}}$ ion has twice the charge."),
        ]),
        EX("Worked example 3: finding the electron affinity", intro=r"A Born-Haber cycle can find any unknown term. For NaCl, $\Delta H_f = -411$, $\Delta H_{at}(\mathrm{Na}) = +107$, $IE_1 = +496$, $\Delta H_{at}(\tfrac12\mathrm{Cl_2}) = +122$ and $\Delta H_{latt} = -787$ (all in $\mathrm{kJ\,mol^{-1}}$). Find $EA_1$ of chlorine.", steps=[
            S("Rearrange the cycle", math=r"EA_1 = \Delta H_f - \Delta H_{at}(\mathrm{Na}) - \Delta H_{at}(\mathrm{Cl}) - IE_1 - \Delta H_{latt}"),
            S("Substitute", math=r"EA_1 = -411 - 107 - 122 - 496 - (-787)"),
            S("Result", math=r"EA_1 = -349\ \text{kJ mol}^{-1}"),
        ]),
        MISTAKE("Using the wrong atomisation for chlorine", r"The element is $\mathrm{Cl_2}$, but the equation of atomisation is per mole of **atoms**. For one $\mathrm{NaCl}$ use $\tfrac12\mathrm{Cl_2} \rightarrow \mathrm{Cl}$ (+122). For $\mathrm{MgCl_2}$, use two atoms (+244)."),
        MISTAKE("Leaving out the second ionisation enthalpy", r"If the metal forms a 2+ ion, add **both** ionisation enthalpies. Missing the second one is the most common error."),
        TIP(r"Born-Haber cycles feature in Paper 2 structured questions. Draw the cycle with labelled arrows, name every step, and give the sign of every enthalpy change."),
        QUIZ(r"Which step in a Born-Haber cycle is always exothermic?", [
            "Atomisation of the metal", "First ionisation of the metal", "Formation of the lattice from gaseous ions", "Atomisation of chlorine"], 2,
             r"Gaseous ions attract each other strongly and release a large amount of energy as they pack into the lattice.",
             hint="Which step brings oppositely charged ions together?",
             feedback=["Atomisation of the metal needs energy.", "Removing electrons needs energy.", "", "Breaking the Cl-Cl bond needs energy."]),
        QUIZ(r"Why do you use $+244$ for atomisation of chlorine in $\mathrm{MgCl_2}$ but $+122$ in $\mathrm{NaCl}$?", [
            "MgCl2 is a larger molecule", "MgCl2 contains two chlorine atoms per formula unit", "Magnesium is more reactive", "The Cl-Cl bond is stronger in MgCl2"], 1,
             r"The formula has two chlorine atoms: $2 \times 122 = 244$.", hint="Count the Cl atoms in the formula.",
             feedback=["Size of the molecule is irrelevant.", "", "Reactivity does not change the number of atoms.", "The Cl-Cl bond is the same in both cases."]),
        PQ(r"Calculate the lattice enthalpy of potassium chloride from: $\Delta H_f = -436.7$, $\Delta H_{at}(\mathrm{K}) = +89$, $IE_1(\mathrm{K}) = +419$, $\Delta H_{at}(\tfrac12\mathrm{Cl_2}) = +122$ and $EA_1(\mathrm{Cl}) = -349\ \mathrm{kJ\,mol^{-1}}$.",
           r"Gaseous steps: $89 + 419 + 122 - 349 = +281$. $\Delta H_{latt} = -436.7 - 281 = -717.7\ \mathrm{kJ\,mol^{-1}}$."),
        PQ(r"Calculate the first electron affinity of fluorine from: $\Delta H_f(\mathrm{LiF}) = -617$, $\Delta H_{at}(\mathrm{Li}) = +159$, $IE_1(\mathrm{Li}) = +520$, $\Delta H_{at}(\tfrac12\mathrm{F_2}) = +79$ and $\Delta H_{latt}(\mathrm{LiF}) = -1037\ \mathrm{kJ\,mol^{-1}}$.",
           r"$EA_1 = \Delta H_f - \Delta H_{at}(\mathrm{Li}) - IE_1 - \Delta H_{at}(\mathrm{F}) - \Delta H_{latt} = -617 - 159 - 520 - 79 + 1037 = -338\ \mathrm{kJ\,mol^{-1}}$."),
        PQ(r"Name each step in the Born-Haber cycle for NaCl and state whether it is endothermic or exothermic.",
           r"Atomisation of sodium (endothermic); atomisation of chlorine (endothermic); first ionisation of sodium (endothermic); electron affinity of chlorine (exothermic); lattice formation (strongly exothermic). The overall formation of NaCl is exothermic ($-411$) because the lattice enthalpy outweighs the positive terms."),
        SUM(r"Lattice enthalpy (formation convention) is the enthalpy change when one mole of ionic solid forms from gaseous ions: always exothermic.",
            r"The Born-Haber cycle: $\Delta H_f = \Delta H_{at}(\text{metal}) + \Delta H_{at}(\text{non-metal}) + IE + EA + \Delta H_{latt}$, with every term per formula unit.",
            r"Count atoms and electrons carefully: two chlorine atoms and two ionisation enthalpies for $\mathrm{MgCl_2}$.",
            r"Rearrange the cycle to find any one unknown term."),
    ],
))

# ------------------------------------------------------------------ 9. Lattice enthalpy trends and solution
LESSONS.append(lesson(
    module=M5,
    topic="Lattice energy and Born-Haber cycles",
    title="Lattice enthalpy trends and enthalpy of solution cycles",
    slug="chl2-lattice-trends-solution",
    minutes=22,
    summary="How ionic charge and radius control lattice enthalpy, a Born-Haber cycle for MgO, and the cycle linking lattice enthalpy, hydration enthalpies and enthalpy of solution.",
    objectives=[
        "Explain lattice enthalpy trends using ionic charge and radius",
        "Use second electron affinity in a Born-Haber cycle for an oxide",
        "Define hydration enthalpy and build a cycle for the enthalpy of solution",
        "Compare ionic-model and Born-Haber lattice enthalpies to judge covalent character",
    ],
    key_concepts=["Ionic charge", "Ionic radius", "Hydration enthalpy", "Enthalpy of solution", "Second electron affinity", "Covalent character"],
    blocks=[
        H("Introduction"),
        T(r"Magnesium oxide is used to line furnaces because it melts at about 2850 degrees C, far above sodium chloride at 801 degrees C. In a village kitchen, salt dissolves in cold water in seconds, but magnesium oxide (the white powder in some stomach remedies) hardly dissolves at all. "
          r"The explanation lies in the lattice enthalpy and in how it competes with the energy released when ions are surrounded by water."),
        H("What controls lattice enthalpy?"),
        T(r"The force between two ions depends on their charges and on the distance between their centres. For a lattice, this gives a useful proportionality:"),
        D(r"The magnitude of the lattice enthalpy is larger when the **charges** on the ions are larger and when the **ionic radii** are smaller (the ions are closer).", title="Trend rule",
          formula=r"\left|\Delta H_{latt}\right| \propto \dfrac{q_+\,q_-}{r_+ + r_-}"),
        CODE("compound   charges   lattice enthalpy / kJ per mol (teaching data)\n"
             "LiF        1+  1-       -1037\n"
             "NaBr       1+  1-        -751\n"
             "KCl        1+  1-        -718\n"
             "NaCl       1+  1-        -787\n"
             "MgCl2      2+  1-       -2524\n"
             "MgO        2+  2-       -3845", "text", title="Lattice enthalpies (values from the cycles in these lessons; books differ slightly)"),
        T(r"Compare NaCl and KCl: same charges, but $\mathrm{K^+}$ is larger than $\mathrm{Na^+}$, so the ions are further apart and the lattice enthalpy is less exothermic. "
          r"Compare NaCl and MgO: the charges are $1 \times 1$ against $2 \times 2$, four times larger. Allowing for the smaller ions (radii: $\mathrm{Na^+}$ 102 pm, $\mathrm{Cl^-}$ 181 pm, $\mathrm{Mg^{2+}}$ 72 pm, $\mathrm{O^{2-}}$ 140 pm), the ratio predicted by the rule is $4 \times \dfrac{102 + 181}{72 + 140} = 5.3$ and the Born-Haber values give $3845/787 = 4.9$. The rule works well for a rough comparison."),
        H("A cycle for magnesium oxide"),
        T(r"Oxygen needs two electrons. The first electron affinity of oxygen is exothermic ($-141$), but adding a second electron to the negative ion $\mathrm{O^-}$ is **endothermic** ($+798$) because the electron is repelled. The large lattice enthalpy of $\mathrm{MgO}$ pays for this."),
        CODE("data for magnesium oxide (kJ per mol)\n"
             "enthalpy of formation of MgO(s)         -602\n"
             "atomisation of Mg(s)                    +148\n"
             "first + second ionisation of Mg         +738 + 1451\n"
             "atomisation of 1/2 O2(g)                +249\n"
             "first electron affinity of O            -141\n"
             "second electron affinity of O           +798", "text", title="Teaching data (typical textbook values)"),
        EX("Worked example 1: lattice enthalpy of MgO", intro=r"Calculate $\Delta H_{latt}$ for magnesium oxide.", steps=[
            S("Ionisation of Mg", math=r"738 + 1451 = +2189\ \text{kJ}"),
            S("Total for the gaseous steps", math=r"148 + 2189 + 249 + (-141) + 798 = +3243\ \text{kJ}"),
            S("Rearrange", math=r"\Delta H_{latt} = \Delta H_f - 3243 = -602 - 3243"),
            S("Result", math=r"\Delta H_{latt} = -3845\ \text{kJ mol}^{-1}", text="Textbooks quote values between about $-3790$ and $-3850$; check yours."),
        ]),
        H("Enthalpy of solution: another cycle"),
        D(r"The **enthalpy of hydration** $\Delta H_{hyd}$ of an ion is the enthalpy change when **one mole of the gaseous ion** dissolves in water to form the aqueous ion. It is exothermic because water molecules are attracted to the ion (the oxygen end to cations, the hydrogen end to anions).",
          title="Hydration enthalpy", formula=r"\mathrm{Na^+(g)} \xrightarrow{aq} \mathrm{Na^+(aq)}"),
        T(r"To dissolve a salt you may imagine two steps: first break the lattice into gaseous ions (the reverse of lattice formation, so $-\Delta H_{latt}$), then hydrate the ions."),
        F(r"\Delta H_{sol} = -\Delta H_{latt} + \Delta H_{hyd}(\text{cation}) + \Delta H_{hyd}(\text{anion})", title="Cycle for enthalpy of solution"),
        EX("Worked example 2: dissolving sodium chloride", intro=r"$\Delta H_{latt}(\mathrm{NaCl}) = -787$, $\Delta H_{hyd}(\mathrm{Na^+}) = -406$ and $\Delta H_{hyd}(\mathrm{Cl^-}) = -364\ \mathrm{kJ\,mol^{-1}}$ (teaching values). Calculate $\Delta H_{sol}$.", steps=[
            S("Break the lattice", math=r"+787\ \text{kJ}"),
            S("Hydrate the ions", math=r"-406 + (-364) = -770\ \text{kJ}"),
            S("Add", math=r"\Delta H_{sol} = +787 - 770 = +17\ \text{kJ mol}^{-1}", text="A small positive value (measured values are close to zero). Salt dissolves anyway because the entropy increases (see the lesson on entropy)."),
        ]),
        EX("Worked example 3: dissolving magnesium chloride", intro=r"$\Delta H_{latt}(\mathrm{MgCl_2}) = -2524$, $\Delta H_{hyd}(\mathrm{Mg^{2+}}) = -1920$ and $\Delta H_{hyd}(\mathrm{Cl^-}) = -364\ \mathrm{kJ\,mol^{-1}}$. Calculate $\Delta H_{sol}$.", steps=[
            S("Break the lattice", math=r"+2524\ \text{kJ}"),
            S("Hydrate the ions", math=r"-1920 + 2(-364) = -2648\ \text{kJ}", text="There are two chloride ions per formula unit."),
            S("Add", math=r"\Delta H_{sol} = +2524 - 2648 = -124\ \text{kJ mol}^{-1}", text="Exothermic: the solution warms."),
        ]),
        H("Ionic model and covalent character"),
        T(r"A **theoretical lattice enthalpy** can be calculated from the charges and radii alone, treating the ions as perfect spheres. If it agrees with the Born-Haber value, the bonding is close to purely ionic. "
          r"A large difference suggests **covalent character**: a small, highly charged cation distorts (polarises) the large anion and shares some electron density. Silver halides are a standard example. Check your textbook for actual values."),
        MISTAKE("Mixing up lattice and hydration enthalpy", r"Lattice enthalpy forms a **solid** from gaseous ions; hydration forms **aqueous ions** from gaseous ions. In the solution cycle the lattice term appears with the sign reversed."),
        MISTAKE("Forgetting the factor of two", r"For $\mathrm{MgCl_2}$ you need hydration of **two** chloride ions. Count ions from the formula."),
        TIP(r"Questions commonly ask you to explain why one lattice enthalpy is more exothermic than another. Always mention both charge and radius, and say which is the same in the compounds being compared."),
        QUIZ(r"Which compound has the most exothermic lattice enthalpy?", ["KCl", "NaCl", "MgCl2", "MgO"], 3,
             r"MgO has the largest charges (2+ and 2-) and small ions, so its lattice enthalpy is the most exothermic of the four.",
             hint="Compare the charges first.", feedback=["K+ is large and charges are low.", "Singly charged ions.", "Mg2+ with Cl- is strong but with only one negative charge per ion.", ""]),
        QUIZ(r"Why is the second electron affinity of oxygen positive?", [
            "The second electron is added to a negative ion and is repelled", "Oxygen has a high first ionisation enthalpy",
            "Oxygen is a diatomic gas", "Magnesium has two outer electrons"], 0,
             r"Adding an electron to $\mathrm{O^-}$ means pushing it against the negative charge already there, so energy must be supplied.",
             hint="What are the charges of the ion and the electron?",
             feedback=["", "Ionisation enthalpy involves removing electrons.", "That affects atomisation, not the second electron affinity.", "That relates to magnesium, not the oxygen electron affinity."]),
        PQ(r"Explain why the lattice enthalpy of KCl ($-718$) is less exothermic than that of NaCl ($-787\ \mathrm{kJ\,mol^{-1}}$).",
           r"Both ions have charges of 1+ and 1-. The $\mathrm{K^+}$ ion is larger than $\mathrm{Na^+}$, so the distance between the ion centres is greater, the electrostatic attraction is weaker and the lattice enthalpy is less exothermic."),
        PQ(r"Use $\Delta H_{latt}(\mathrm{KCl}) = -718$, $\Delta H_{hyd}(\mathrm{K^+}) = -322$ and $\Delta H_{hyd}(\mathrm{Cl^-}) = -364\ \mathrm{kJ\,mol^{-1}}$ to calculate $\Delta H_{sol}$ for KCl.",
           r"$\Delta H_{sol} = +718 + (-322) + (-364) = +32\ \mathrm{kJ\,mol^{-1}}$ (teaching values). Endothermic: more energy is needed to separate the ions than is released by hydration."),
        PQ(r"Why is magnesium oxide almost insoluble in water, although magnesium chloride is very soluble?",
           r"$\mathrm{MgO}$ has a very large lattice enthalpy ($-3845$) because both ions have a 2 charge; the hydration enthalpies of $\mathrm{Mg^{2+}}$ and $\mathrm{O^{2-}}$ cannot pay back enough energy. $\mathrm{MgCl_2}$ has a lattice enthalpy of only $-2524$, and hydration of $\mathrm{Mg^{2+}}$ and two $\mathrm{Cl^-}$ ions gives a net exothermic solution ($-124$)."),
        SUM(r"Lattice enthalpy becomes more exothermic as ionic charges increase and ionic radii decrease: $|\Delta H_{latt}| \propto q_+q_-/(r_+ + r_-)$.",
            r"Oxides need the second electron affinity of oxygen, which is endothermic; the very large lattice enthalpy pays for it.",
            r"$\Delta H_{sol} = -\Delta H_{latt} + \Delta H_{hyd}(\text{cation}) + \Delta H_{hyd}(\text{anion})$.",
            r"Agreement between ionic-model and Born-Haber values suggests an almost purely ionic lattice; differences suggest covalent character."),
    ],
))

# ------------------------------------------------------------------ 10. Entropy
LESSONS.append(lesson(
    module=M5,
    topic="Entropy",
    title="Entropy and the direction of change",
    slug="chl2-entropy",
    minutes=22,
    summary="Entropy as a measure of how widely matter and energy are spread, how to predict and calculate entropy changes, and the second law: total entropy change decides feasibility.",
    objectives=[
        "Explain entropy in terms of the number of ways energy and particles can be arranged",
        "Predict the sign of the entropy change for a reaction or change of state",
        "Calculate the standard entropy change of a reaction from standard molar entropies",
        "Calculate the entropy change of the surroundings and the total entropy change",
    ],
    key_concepts=["Entropy", "Standard molar entropy", "Disorder", "Entropy change of the system", "Entropy change of the surroundings", "Second law", "Total entropy change"],
    blocks=[
        H("Introduction"),
        T(r"A cube of ice left on a table at Mile 4 market melts without anyone heating it, and the water later evaporates. Perfume spreads across a room, and a drop of ink spreads through a glass of water. "
          r"None of these changes can be explained by energy release alone: melting ice takes in heat. What drives them is the tendency of matter and energy to spread out. Chemists measure that tendency with **entropy**."),
        H("What is entropy?"),
        D(r"**Entropy**, $S$, is a measure of the number of ways in which the particles of a substance and their energy can be arranged. The more ways there are (the more spread out and 'disordered' the system), the higher the entropy. The unit is $\mathrm{J\,K^{-1}\,mol^{-1}}$. "
          r"The **standard molar entropy** $S^\circ$ is the entropy of one mole of a substance at 298 K and 100 kPa. Every substance above 0 K has a positive $S^\circ$; a perfect crystal at 0 K has zero entropy.",
          title="Entropy"),
        T(r"The word 'disorder' is a helpful picture but not exact: it is really about the number of **ways energy can be shared** among the particles. Four things raise the entropy of a substance."),
        KEY("What makes entropy larger", r"Compare the system before and after the change.",
            cards=[["Change of state", "Solid < liquid < gas. Gases have the greatest freedom."],
                   ["Temperature", "Heating gives more ways to share energy: S rises."],
                   ["More particles", "More moles of gas gives more arrangements."],
                   ["Mixing and dissolving", "Spreading particles through a larger volume raises S."]]),
        CODE("substance        S / J per K per mol (298 K)\n"
             "H2(g)             130.7\n"
             "N2(g)             191.6\n"
             "O2(g)             205.0\n"
             "NH3(g)            192.5\n"
             "H2O(l)             69.9\n"
             "H2O(g)            188.8\n"
             "CaCO3(s)           92.9\n"
             "CaO(s)             39.7\n"
             "CO2(g)            213.7", "text", title="Standard molar entropies (typical textbook values)"),
        T(r"Notice that water vapour (188.8) has far greater entropy than liquid water (69.9): that is the largest jump of the three states. Complex molecules also have higher entropy than simple ones of the same state because they can vibrate and rotate in more ways."),
        H("The entropy change of a reaction"),
        D(r"The standard entropy change of a reaction is found from the standard molar entropies of products and reactants, each multiplied by its coefficient:", title="Entropy change of the system",
          formula=r"\Delta S^\circ_{system} = \sum n\,S^\circ(\text{products}) - \sum n\,S^\circ(\text{reactants})"),
        EX("Worked example 1: ammonia synthesis", intro=r"Calculate $\Delta S^\circ$ for $\mathrm{N_2(g)} + 3\mathrm{H_2(g)} \rightarrow 2\mathrm{NH_3(g)}$.", steps=[
            S("Products", math=r"2 \times 192.5 = 385.0\ \text{J K}^{-1}"),
            S("Reactants", math=r"191.6 + 3 \times 130.7 = 191.6 + 392.1 = 583.7\ \text{J K}^{-1}"),
            S("Subtract", math=r"\Delta S^\circ = 385.0 - 583.7 = -198.7\ \text{J K}^{-1}\,\text{mol}^{-1}", text="Four moles of gas become two: fewer ways to arrange the particles, so the entropy falls."),
        ]),
        EX("Worked example 2: thermal decomposition of calcium carbonate", intro=r"Calculate $\Delta S^\circ$ for $\mathrm{CaCO_3(s)} \rightarrow \mathrm{CaO(s)} + \mathrm{CO_2(g)}$.", steps=[
            S("Products", math=r"39.7 + 213.7 = 253.4"),
            S("Reactant", math=r"92.9"),
            S("Subtract", math=r"\Delta S^\circ = 253.4 - 92.9 = +160.5\ \text{J K}^{-1}\,\text{mol}^{-1}", text="A gas forms from a solid: a large increase in entropy."),
        ]),
        H("The second law and the surroundings"),
        T(r"A reaction does not only change the entropy of the substances (the **system**). When it gives out heat, that heat spreads the particles of the **surroundings** and raises their entropy. When it takes in heat, it lowers the entropy of the surroundings."),
        D(r"The entropy change of the surroundings is $-\Delta H/T$, with $\Delta H$ in joules and $T$ in kelvin. The **second law of thermodynamics** says that a change is feasible (can occur spontaneously) only if the total entropy change is positive.",
          title="Second law", formula=r"\Delta S_{surr} = -\dfrac{\Delta H}{T} \qquad \Delta S_{total} = \Delta S_{system} + \Delta S_{surr} > 0"),
        EX("Worked example 3: total entropy change for ammonia synthesis", intro=r"For $\mathrm{N_2} + 3\mathrm{H_2} \rightarrow 2\mathrm{NH_3}$ at 298 K, $\Delta H = -92.4\ \mathrm{kJ}$ and $\Delta S_{system} = -198.7\ \mathrm{J\,K^{-1}}$. Calculate $\Delta S_{total}$.", steps=[
            S("Convert to joules", math=r"\Delta H = -92\,400\ \text{J}"),
            S("Surroundings", math=r"\Delta S_{surr} = -\dfrac{-92\,400}{298} = +310.1\ \text{J K}^{-1}"),
            S("Total", math=r"\Delta S_{total} = -198.7 + 310.1 = +111.4\ \text{J K}^{-1}", text="Positive, so the reaction is feasible at 298 K. 'Feasible' says nothing about speed: without a catalyst and high temperature it is far too slow."),
        ]),
        T(r"Entropy explains why an endothermic change can occur. Ammonium nitrate dissolving in water takes in heat ($\Delta H = +25.5\ \mathrm{kJ\,mol^{-1}}$), so $\Delta S_{surr} = -25\,500/298 = -85.6\ \mathrm{J\,K^{-1}}$. The change is feasible only because the system's entropy rises by more than 85.6 $\mathrm{J\,K^{-1}}$ as the crystal breaks into free ions."),
        MISTAKE("Mixing joules and kilojoules", r"$\Delta H$ is usually in kJ but entropy is in J. Convert $\Delta H$ to joules (multiply by 1000) before dividing by $T$, or convert $\Delta S$ to kJ."),
        MISTAKE("Saying a reaction is feasible only if the system's entropy rises", r"Feasibility depends on the **total** entropy change. The system's entropy can fall (as in ammonia synthesis) if the surroundings gain more."),
        TIP(r"A typical Paper 2 question gives entropies and asks for $\Delta S^\circ$, then asks you to explain the sign in terms of moles of gas. State the numbers of gas molecules before and after."),
        QUIZ(r"The entropy change is most positive for which process?", [
            r"$\mathrm{H_2O(g)} \rightarrow \mathrm{H_2O(l)}$", r"$\mathrm{H_2O(s)} \rightarrow \mathrm{H_2O(l)}$", r"$\mathrm{H_2O(l)} \rightarrow \mathrm{H_2O(g)}$", r"$2\mathrm{NO_2(g)} \rightarrow \mathrm{N_2O_4(g)}$"], 2,
             r"Going from liquid to gas gives the largest increase in freedom of the particles ($+118.9\ \mathrm{J\,K^{-1}\,mol^{-1}}$).",
             hint="Which change spreads the particles most?",
             feedback=["This reduces entropy: gas to liquid.", "This increases entropy but by less than boiling.", "", "Fewer gas molecules: entropy decreases."]),
        QUIZ(r"Which statement about the second law is correct?", [
            "Every reaction has a positive entropy change of the system", "A reaction is feasible if the total entropy change is positive",
            "Exothermic reactions always have a positive entropy change of the system", "Entropy always decreases in a feasible reaction"], 1,
             r"The second law applies to the total entropy change: system plus surroundings.", hint="Which entropy change must be positive?",
             feedback=["The system's entropy can fall.", "", "An exothermic reaction raises the entropy of the surroundings, not necessarily the system.", "The total entropy must increase."]),
        PQ(r"Predict the sign of the entropy change of the system for (a) $\mathrm{2H_2(g)} + \mathrm{O_2(g)} \rightarrow 2\mathrm{H_2O(l)}$, (b) $\mathrm{NH_4Cl(s)} \rightarrow \mathrm{NH_3(g)} + \mathrm{HCl(g)}$. Give a reason.",
           r"(a) Negative: three moles of gas form liquid water, a big loss of freedom. (b) Positive: a solid forms two moles of gas."),
        PQ(r"Calculate $\Delta S^\circ$ for $2\mathrm{H_2(g)} + \mathrm{O_2(g)} \rightarrow 2\mathrm{H_2O(l)}$ using $S^\circ$: $\mathrm{H_2} = 130.7$, $\mathrm{O_2} = 205.0$, $\mathrm{H_2O(l)} = 69.9\ \mathrm{J\,K^{-1}\,mol^{-1}}$.",
           r"Products $= 2 \times 69.9 = 139.8$. Reactants $= 2 \times 130.7 + 205.0 = 466.4$. $\Delta S^\circ = 139.8 - 466.4 = -326.6\ \mathrm{J\,K^{-1}\,mol^{-1}}$."),
        PQ(r"Explain why dissolving ammonium nitrate in water ($\Delta H = +25.5\ \mathrm{kJ\,mol^{-1}}$) can be feasible at 298 K.",
           r"$\Delta S_{surr} = -25\,500/298 = -85.6\ \mathrm{J\,K^{-1}}$. The solid breaks into freely moving ions in solution, so the system's entropy rises by more than 85.6 $\mathrm{J\,K^{-1}}$. Then $\Delta S_{total} > 0$ and the dissolving is feasible, even though it is endothermic."),
        SUM(r"Entropy measures the number of ways particles and energy can be arranged; $S$ rises for solid to liquid to gas, with heating, with more gas moles and with mixing.",
            r"$\Delta S^\circ_{system} = \Sigma nS^\circ(\text{products}) - \Sigma nS^\circ(\text{reactants})$, in $\mathrm{J\,K^{-1}\,mol^{-1}}$.",
            r"$\Delta S_{surr} = -\Delta H/T$ (with $\Delta H$ in J and $T$ in K).",
            r"A change is feasible if $\Delta S_{total} = \Delta S_{system} + \Delta S_{surr} > 0$; feasible does not mean fast."),
    ],
))

# ------------------------------------------------------------------ 11. Gibbs free energy
LESSONS.append(lesson(
    module=M5,
    topic="Gibbs free energy",
    title="Gibbs free energy, feasibility and equilibrium",
    slug="chl2-gibbs-free-energy",
    minutes=24,
    summary="Combine enthalpy and entropy as delta G = delta H - T delta S to decide whether a reaction is feasible, find the temperature at which it becomes feasible, and link delta G to the equilibrium constant.",
    objectives=[
        "Use delta G = delta H - T delta S to decide whether a reaction is feasible",
        "Predict how temperature changes feasibility for the four sign combinations of delta H and delta S",
        "Calculate the temperature at which a reaction becomes feasible",
        "Use delta G = -RT ln K to relate free energy to the equilibrium constant",
    ],
    key_concepts=["Gibbs free energy", "Feasibility", "Spontaneous change", "Temperature of change", "Equilibrium constant", "Standard free energy change"],
    blocks=[
        H("Introduction"),
        T(r"Limestone is heated in a kiln to make lime for cement. At room temperature calcium carbonate is perfectly stable, but above about 840 degrees C it decomposes. Why does temperature turn a non-feasible change into a feasible one? "
          r"The last lesson showed that feasibility depends on the total entropy change. Josiah Willard Gibbs combined the two ideas into a single quantity that uses only the reaction itself: the **Gibbs free energy change**."),
        H("The Gibbs equation"),
        T(r"Start from $\Delta S_{total} = \Delta S_{system} - \Delta H/T$. Multiply by $-T$: $-T\,\Delta S_{total} = \Delta H - T\,\Delta S_{system}$. The quantity on the right is defined as $\Delta G$."),
        D(r"The **Gibbs free energy change** $\Delta G$ of a reaction at temperature $T$ is given below. A reaction is **feasible** (spontaneous) when $\Delta G < 0$ and not feasible when $\Delta G > 0$. At $\Delta G = 0$ the system is at equilibrium. Use $T$ in kelvin and keep $\Delta H$ and $T\Delta S$ in the same units (usually kJ or J).",
          title="Gibbs free energy", formula=r"\Delta G = \Delta H - T\,\Delta S"),
        TIP(r"$\Delta S$ is normally in $\mathrm{J\,K^{-1}\,mol^{-1}}$ and $\Delta H$ in $\mathrm{kJ\,mol^{-1}}$. Divide $\Delta S$ by 1000 or multiply $\Delta H$ by 1000 before you subtract."),
        KEY("Four cases", r"The sign of $\Delta G$ depends on the signs of $\Delta H$ and $\Delta S$.",
            cards=[["dH negative, dS positive", "dG always negative: feasible at all temperatures."],
                   ["dH positive, dS negative", "dG always positive: never feasible."],
                   ["dH negative, dS negative", "Feasible at low temperature (when T dS is small)."],
                   ["dH positive, dS positive", "Feasible at high temperature (when T dS is large)."]]),
        D(r"At the temperature where $\Delta G = 0$ the reaction just becomes feasible (or stops being feasible). Setting $\Delta H - T\Delta S = 0$ gives:", title="Changeover temperature", formula=r"T = \dfrac{\Delta H}{\Delta S}"),
        EX("Worked example 1: ammonia synthesis", intro=r"For $\mathrm{N_2} + 3\mathrm{H_2} \rightarrow 2\mathrm{NH_3}$, $\Delta H = -92.4\ \mathrm{kJ}$ and $\Delta S = -198.7\ \mathrm{J\,K^{-1}}$. (a) Calculate $\Delta G$ at 298 K. (b) Find the temperature above which the reaction is no longer feasible.", steps=[
            S("Convert units", math=r"\Delta S = -0.1987\ \text{kJ K}^{-1}"),
            S("(a) Calculate at 298 K", math=r"\Delta G = -92.4 - 298 \times (-0.1987) = -92.4 + 59.2 = -33.2\ \text{kJ}"),
            S("(b) Changeover temperature", math=r"T = \dfrac{-92.4}{-0.1987} = 465\ \text{K}", text="Above 465 K ($192$ degrees C), $\\Delta G$ is positive: higher temperatures make the equilibrium yield of ammonia fall (see Le Chatelier's principle in industry)."),
        ]),
        EX("Worked example 2: limestone kiln", intro=r"For $\mathrm{CaCO_3(s)} \rightarrow \mathrm{CaO(s)} + \mathrm{CO_2(g)}$, $\Delta H = +178.3\ \mathrm{kJ}$ and $\Delta S = +160.5\ \mathrm{J\,K^{-1}}$. Find the temperature above which decomposition is feasible, and $\Delta G$ at 298 K and at 1273 K.", steps=[
            S("Changeover temperature", math=r"T = \dfrac{178\,300}{160.5} = 1111\ \text{K} = 838\ {}^\circ\text{C}"),
            S("At 298 K", math=r"\Delta G = 178\,300 - 298 \times 160.5 = +130\,500\ \text{J} = +130.5\ \text{kJ}", text="Positive: calcium carbonate does not decompose at room temperature."),
            S("At 1273 K (1000 degrees C)", math=r"\Delta G = 178\,300 - 1273 \times 160.5 = -26\,000\ \text{J} = -26.0\ \text{kJ}", text="Negative: decomposition is feasible, and kilns work at this temperature."),
        ]),
        H("Free energy and the equilibrium constant"),
        D(r"The standard free energy change is linked to the equilibrium constant $K$ of the reaction. $R = 8.314\ \mathrm{J\,K^{-1}\,mol^{-1}}$ and $\Delta G^\circ$ must be in joules. A negative $\Delta G^\circ$ gives $K > 1$ (products favoured); a positive $\Delta G^\circ$ gives $K < 1$ (reactants favoured).",
          title="Free energy and K", formula=r"\Delta G^\circ = -RT\ln K \qquad K = e^{-\Delta G^\circ/RT}"),
        EX("Worked example 3: K for ammonia at two temperatures", intro=r"Use $\Delta G^\circ = -33\,187\ \mathrm{J}$ at 298 K for ammonia synthesis to find $K$, then estimate $K$ at 700 K assuming $\Delta H$ and $\Delta S$ do not change.", steps=[
            S("K at 298 K", math=r"\ln K = \dfrac{33\,187}{8.314 \times 298} = 13.4 \Rightarrow K = 6.6 \times 10^{5}"),
            S("Free energy at 700 K", math=r"\Delta G = -92\,400 - 700 \times (-198.7) = +46\,690\ \text{J}"),
            S("K at 700 K", math=r"\ln K = \dfrac{-46\,690}{8.314 \times 700} = -8.02 \Rightarrow K = 3.3 \times 10^{-4}", text="K falls enormously on heating: at higher temperature the equilibrium mixture contains far less ammonia. The assumption of constant $\\Delta H$ and $\\Delta S$ is only approximate."),
        ]),
        MISTAKE("Using degrees Celsius", r"$T$ in $\Delta G = \Delta H - T\Delta S$ must be in kelvin. $25\ {}^\circ\mathrm{C}$ is 298 K."),
        MISTAKE("Thinking a negative free energy change means a fast reaction", r"$\Delta G < 0$ says the change is **possible**, not that it is quick. Diamond turning into graphite has $\Delta G < 0$ but does not happen on any human timescale because the activation energy is huge."),
        TIP(r"Gibbs free energy questions often finish with 'at what temperature does the reaction become feasible?': answer in kelvin and, if asked, convert to degrees Celsius by subtracting 273."),
        QUIZ(r"A reaction has $\Delta H > 0$ and $\Delta S > 0$. It is feasible", [
            "at all temperatures", "at no temperature", "only at low temperature", "only above a certain temperature"], 3,
             r"$\Delta G = \Delta H - T\Delta S$ becomes negative only when $T\Delta S$ is larger than $\Delta H$: at high enough temperature.",
             hint="Which term grows with temperature?",
             feedback=["That needs a negative dH and positive dS.", "That needs a positive dH and negative dS.", "Low temperature makes TdS small, so dG is positive.", ""]),
        QUIZ(r"The standard free energy change of a reaction at 298 K is $-20\ \mathrm{kJ\,mol^{-1}}$. What can you say about $K$?", [
            "K is less than 1", "K equals 1", "K is greater than 1", "K is negative"], 2,
             r"$K = e^{-\Delta G^\circ/RT}$: a negative $\Delta G^\circ$ makes the exponent positive, so $K > 1$.", hint="Use K = exp(-dG/RT).",
             feedback=["That corresponds to a positive dG.", "That corresponds to dG zero.", "", "K is never negative."]),
        PQ(r"The vaporisation of water has $\Delta H = +44.0\ \mathrm{kJ\,mol^{-1}}$ and $\Delta S = +118.9\ \mathrm{J\,K^{-1}\,mol^{-1}}$. Calculate $\Delta G$ at 298 K and the temperature at which $\Delta G = 0$. Compare it with the true boiling point of 373 K.",
           r"At 298 K: $\Delta G = 44\,000 - 298 \times 118.9 = +8568\ \mathrm{J} = +8.6\ \mathrm{kJ}$ (not feasible: water does not boil at 298 K). $T = 44\,000/118.9 = 370\ \mathrm{K}$, close to 373 K; the small difference arises because $\Delta H$ and $\Delta S$ change a little with temperature."),
        PQ(r"A reaction has $\Delta H = -100\ \mathrm{kJ}$ and $\Delta S = -300\ \mathrm{J\,K^{-1}}$. Find the temperature at which $\Delta G = 0$ and state whether the reaction is feasible at 400 K.",
           r"$T = -100\,000/(-300) = 333\ \mathrm{K}$. At 400 K: $\Delta G = -100\,000 - 400 \times (-300) = +20\,000\ \mathrm{J}$, positive, so not feasible. It is feasible only below 333 K."),
        PQ(r"A reaction has $\Delta G^\circ = +20.0\ \mathrm{kJ\,mol^{-1}}$ at 298 K. Calculate $K$ and say what the value means.",
           r"$\ln K = -20\,000/(8.314 \times 298) = -8.07$, so $K = 3.1 \times 10^{-4}$. $K$ is much less than 1: at equilibrium the mixture is almost entirely reactants."),
        SUM(r"$\Delta G = \Delta H - T\Delta S$ ($T$ in K; consistent units). Feasible if $\Delta G < 0$; equilibrium at $\Delta G = 0$.",
            r"Signs of $\Delta H$ and $\Delta S$ give four cases; the changeover temperature is $T = \Delta H/\Delta S$.",
            r"$\Delta G^\circ = -RT\ln K$: negative $\Delta G^\circ$ means $K > 1$; positive means $K < 1$.",
            r"Feasible does not mean fast: rate depends on activation energy."),
    ],
))

# ------------------------------------------------------------------ 12. Kc and Kp
LESSONS.append(lesson(
    module=M6,
    topic="Equilibrium constants Kc and Kp",
    title="Dynamic equilibrium and the constants Kc and Kp",
    slug="chl2-equilibrium-constants-kc-kp",
    minutes=24,
    summary="Dynamic equilibrium, the expressions for Kc and Kp including units and heterogeneous systems, and how to calculate each constant from equilibrium data.",
    objectives=[
        "Describe a dynamic equilibrium and the features of a system at equilibrium",
        "Write expressions for Kc and Kp, including units, for homogeneous and heterogeneous systems",
        "Calculate Kc and Kp from equilibrium concentrations or partial pressures",
        "Explain what the size of K says and what changes it",
    ],
    key_concepts=["Dynamic equilibrium", "Equilibrium constant", "Kc", "Kp", "Partial pressure", "Homogeneous equilibrium", "Heterogeneous equilibrium"],
    blocks=[
        H("Introduction"),
        T(r"Brown nitrogen dioxide gas in a sealed glass tube slowly turns paler when the tube is cooled, and darkens again when it warms up. The gas is a mixture of brown $\mathrm{NO_2}$ and colourless $\mathrm{N_2O_4}$ that keep converting into each other. "
          r"At any temperature the mixture settles at a fixed composition. The **equilibrium constant** tells us what that composition is."),
        H("Dynamic equilibrium"),
        D(r"A reaction is **reversible** if the products can react to give back the reactants, shown by the sign $\rightleftharpoons$. A reversible reaction in a closed system reaches **dynamic equilibrium** when the forward and reverse reactions go on at the same rate. The concentrations then stay constant, but both reactions continue.",
          title="Dynamic equilibrium"),
        IMG("al-chl2-equilibrium-graph.svg", alt="Graph of concentration against time. The concentration of N2O4 falls and the concentration of NO2 rises, and both level off at constant values after the equilibrium time.",
            caption="Figure 1. Starting with pure $\\mathrm{N_2O_4}$, the concentrations change until they become constant. They are constant but not equal."),
        KEY("Features of a system at equilibrium", r"These four statements are tested again and again.",
            cards=[["Dynamic", "Forward and reverse reactions continue at equal rates."],
                   ["Constant", "Concentrations (and macroscopic properties such as colour) do not change."],
                   ["Closed system", "No reactant or product can enter or leave."],
                   ["Same from both sides", "The same equilibrium is reached starting from reactants or from products."]]),
        H("The equilibrium constant Kc"),
        T(r"For the general reaction $a\mathrm{A} + b\mathrm{B} \rightleftharpoons c\mathrm{C} + d\mathrm{D}$ at equilibrium, the following ratio is constant at a given temperature."),
        D(r"The **equilibrium constant** $K_c$ is the ratio of the product concentrations to the reactant concentrations at equilibrium, each concentration raised to the power of its coefficient in the balanced equation. Concentrations are in $\mathrm{mol\,dm^{-3}}$ and written in square brackets.",
          title="Kc", formula=r"K_c = \dfrac{[\mathrm{C}]^c\,[\mathrm{D}]^d}{[\mathrm{A}]^a\,[\mathrm{B}]^b}"),
        T(r"The **units** of $K_c$ follow from the expression. For $\mathrm{N_2} + 3\mathrm{H_2} \rightleftharpoons 2\mathrm{NH_3}$, $K_c = [\mathrm{NH_3}]^2/([\mathrm{N_2}][\mathrm{H_2}]^3)$ has units $\mathrm{mol^2\,dm^{-6}}/(\mathrm{mol\,dm^{-3}} \times \mathrm{mol^3\,dm^{-9}}) = \mathrm{dm^6\,mol^{-2}}$. "
          r"If the powers on top and bottom match, $K_c$ has no units."),
        D(r"For gases it is often easier to use **partial pressures**. The partial pressure $p_A$ of a gas A in a mixture is its **mole fraction** times the total pressure: $p_A = x_A P$ (with $x_A = n_A/n_{total}$). The pressures of all the gases add up to the total pressure $P$. "
          r"$K_p$ uses the partial pressures:", title="Kp", formula=r"K_p = \dfrac{p_C^{\,c}\,p_D^{\,d}}{p_A^{\,a}\,p_B^{\,b}}"),
        T(r"**Heterogeneous equilibrium** has substances in more than one phase. The concentration of a pure solid or pure liquid is constant, so it is left out of $K_c$ and $K_p$. For $\mathrm{CaCO_3(s)} \rightleftharpoons \mathrm{CaO(s)} + \mathrm{CO_2(g)}$ the expressions are $K_c = [\mathrm{CO_2}]$ and $K_p = p_{\mathrm{CO_2}}$."),
        KEY("What K tells you, and what changes it", r"K describes the position of equilibrium at one temperature.",
            cards=[["K much greater than 1", "Products dominate at equilibrium."], ["K much less than 1", "Reactants dominate."],
                   ["Only temperature changes K", "Changing concentration, pressure or adding a catalyst does not change K."],
                   ["Reverse reaction", "K of the reverse is 1/K. For an equation doubled, K is squared."]]),
        EX("Worked example 1: esterification", intro=r"1.00 mol of ethanol and 1.00 mol of ethanoic acid are mixed with a little acid catalyst. At equilibrium 0.667 mol of ethyl ethanoate and 0.667 mol of water have formed. $\mathrm{C_2H_5OH} + \mathrm{CH_3COOH} \rightleftharpoons \mathrm{CH_3COOC_2H_5} + \mathrm{H_2O}$. Calculate $K_c$.", steps=[
            S("Moles of reactants at equilibrium", math=r"1.00 - 0.667 = 0.333\ \text{mol each}"),
            S("Expression", math=r"K_c = \dfrac{[\text{ester}][\text{water}]}{[\text{ethanol}][\text{acid}]}"),
            S("Volume V cancels because there are equal numbers of moles on both sides", math=r"K_c = \dfrac{0.667 \times 0.667}{0.333 \times 0.333} = 4.0", text="No units: the powers on top and bottom are equal."),
        ]),
        EX("Worked example 2: Kc with units", intro=r"At equilibrium in a 1.00 dm$^3$ vessel at one temperature, $[\mathrm{N_2}] = 0.50$, $[\mathrm{H_2}] = 1.50$ and $[\mathrm{NH_3}] = 0.20\ \mathrm{mol\,dm^{-3}}$. Calculate $K_c$ for $\mathrm{N_2} + 3\mathrm{H_2} \rightleftharpoons 2\mathrm{NH_3}$.", steps=[
            S("Expression", math=r"K_c = \dfrac{[\mathrm{NH_3}]^2}{[\mathrm{N_2}][\mathrm{H_2}]^3}"),
            S("Substitute", math=r"K_c = \dfrac{(0.20)^2}{(0.50)(1.50)^3} = \dfrac{0.040}{0.50 \times 3.375}"),
            S("Result", math=r"K_c = 0.0237\ \text{dm}^6\,\text{mol}^{-2}", text="K is much less than 1: reactants are favoured at this temperature."),
        ]),
        EX("Worked example 3: Kp", intro=r"For $\mathrm{PCl_5(g)} \rightleftharpoons \mathrm{PCl_3(g)} + \mathrm{Cl_2(g)}$ the equilibrium partial pressures are $p(\mathrm{PCl_5}) = 40.0$, $p(\mathrm{PCl_3}) = 30.0$ and $p(\mathrm{Cl_2}) = 30.0\ \mathrm{kPa}$. Calculate $K_p$ and give its units.", steps=[
            S("Expression", math=r"K_p = \dfrac{p(\mathrm{PCl_3})\,p(\mathrm{Cl_2})}{p(\mathrm{PCl_5})}"),
            S("Substitute", math=r"K_p = \dfrac{30.0 \times 30.0}{40.0}"),
            S("Result", math=r"K_p = 22.5\ \text{kPa}", text="Units: $\\mathrm{kPa^2/kPa} = \\mathrm{kPa}$."),
        ]),
        T(r"When the number of moles of gas is the same on both sides (for example $\mathrm{H_2} + \mathrm{I_2} \rightleftharpoons 2\mathrm{HI}$) $K_p$ and $K_c$ have the same value and no units. Otherwise they are related by $K_p = K_c(RT)^{\Delta n}$ with $\Delta n$ the change in moles of gas and consistent units; check your textbook for the units it prefers."),
        MISTAKE("Using initial amounts instead of equilibrium amounts", r"$K_c$ and $K_p$ use only **equilibrium** values. Moles at the start are not used until you subtract the amount reacted."),
        MISTAKE("Putting solids in the expression", r"Pure solids and liquids do not appear. Water appears only if it is a gas (or a solvent whose concentration changes, as in esterification, where it is part of the reacting mixture)."),
        TIP(r"Equilibrium constants appear in Paper 1 (units and expressions) and Paper 2 (calculations). Always write the expression before substituting, and give units unless they cancel."),
        QUIZ(r"Which is the correct expression for $K_c$ for $2\mathrm{SO_2(g)} + \mathrm{O_2(g)} \rightleftharpoons 2\mathrm{SO_3(g)}$?", [
            r"$\dfrac{[\mathrm{SO_3}]}{[\mathrm{SO_2}][\mathrm{O_2}]}$", r"$\dfrac{[\mathrm{SO_3}]^2}{[\mathrm{SO_2}]^2[\mathrm{O_2}]}$",
            r"$\dfrac{[\mathrm{SO_2}]^2[\mathrm{O_2}]}{[\mathrm{SO_3}]^2}$", r"$\dfrac{2[\mathrm{SO_3}]}{2[\mathrm{SO_2}] + [\mathrm{O_2}]}$"], 1,
             r"Products over reactants, each raised to its coefficient.", hint="Coefficients become powers.",
             feedback=["The powers are missing.", "", "This is the inverse (reactants over products).", "Coefficients are powers, not multipliers."]),
        QUIZ(r"The value of $K_c$ for a reaction is changed by", ["Adding a catalyst", "Increasing the pressure", "Changing the temperature", "Adding more reactant"], 2,
             r"$K_c$ depends only on temperature. Other changes alter the position of equilibrium temporarily, but when equilibrium is restored $K_c$ has the same value.",
             hint="What is the only variable fixed for K?",
             feedback=["A catalyst speeds both directions equally.", "Pressure changes the composition but not K.", "", "The composition re-adjusts and K is unchanged."]),
        PQ(r"At equilibrium for $2\mathrm{SO_2} + \mathrm{O_2} \rightleftharpoons 2\mathrm{SO_3}$ in a 1.00 dm$^3$ vessel there are 0.40 mol $\mathrm{SO_2}$, 0.20 mol $\mathrm{O_2}$ and 1.60 mol $\mathrm{SO_3}$. Calculate $K_c$ with units.",
           r"$[\mathrm{SO_2}] = 0.40$, $[\mathrm{O_2}] = 0.20$, $[\mathrm{SO_3}] = 1.60\ \mathrm{mol\,dm^{-3}}$. $K_c = (1.60)^2/((0.40)^2 \times 0.20) = 2.56/0.032 = 80.0\ \mathrm{dm^3\,mol^{-1}}$."),
        PQ(r"For $\mathrm{N_2O_4(g)} \rightleftharpoons 2\mathrm{NO_2(g)}$, the equilibrium partial pressures are $p(\mathrm{N_2O_4}) = 60\ \mathrm{kPa}$ and $p(\mathrm{NO_2}) = 40\ \mathrm{kPa}$. Calculate $K_p$ with units.",
           r"$K_p = p(\mathrm{NO_2})^2/p(\mathrm{N_2O_4}) = 40^2/60 = 26.7\ \mathrm{kPa}$."),
        PQ(r"Write the expressions for $K_c$ and $K_p$ for $\mathrm{CaCO_3(s)} \rightleftharpoons \mathrm{CaO(s)} + \mathrm{CO_2(g)}$, and explain why the solids do not appear.",
           r"$K_c = [\mathrm{CO_2}]$ and $K_p = p(\mathrm{CO_2})$. The concentration (density) of a pure solid is constant and does not change with the amount of solid, so it is built into the constant."),
        SUM(r"At dynamic equilibrium the forward and reverse rates are equal and the concentrations are constant in a closed system.",
            r"$K_c = [\text{products}]^{\text{coeff}}/[\text{reactants}]^{\text{coeff}}$ at equilibrium; $K_p$ uses partial pressures $p_A = x_AP$.",
            r"Pure solids and liquids are omitted; units follow from the expression.",
            r"Only temperature changes the value of K; a catalyst does not."),
    ],
))

# ------------------------------------------------------------------ 13. Equilibrium calculations
LESSONS.append(lesson(
    module=M6,
    topic="Equilibrium constants Kc and Kp",
    title="Equilibrium calculations: ICE tables, Kp and reaction quotient",
    slug="chl2-equilibrium-calculations",
    minutes=24,
    summary="Use initial-change-equilibrium tables to find equilibrium amounts from Kc, calculate Kp from the degree of dissociation, and use the reaction quotient Q to predict the direction of change.",
    objectives=[
        "Set up and solve an initial-change-equilibrium (ICE) table for Kc",
        "Solve a quadratic equation that arises in an equilibrium calculation",
        "Calculate Kp from the degree of dissociation and the total pressure",
        "Compare the reaction quotient Q with K to predict the direction of change",
    ],
    key_concepts=["ICE table", "Degree of dissociation", "Reaction quotient", "Equilibrium composition", "Quadratic solution", "Kp"],
    blocks=[
        H("Introduction"),
        T(r"A chemist making an ester for perfume needs to know how much product will form from a given mixture before she starts, so that she does not waste expensive ethanol. Knowing $K_c$ lets us predict the **equilibrium composition**. "
          r"The trick is to keep track of amounts in a table with three rows: initial, change and equilibrium."),
        H("The ICE method"),
        KEY("Steps", r"Use moles (not concentrations) in the table when volume is not given, and convert at the end if needed.",
            cards=[["I", "Initial amounts from the question (products are often zero)."],
                   ["C", "Change: let x mol react. Use the coefficients in the equation to link the changes."],
                   ["E", "Equilibrium amount = initial + change."],
                   ["Solve", "Put the E values in the Kc expression and solve for x."]]),
        EX("Worked example 1: hydrogen iodide", intro=r"1.00 mol of $\mathrm{H_2}$ and 1.00 mol of $\mathrm{I_2}$ are sealed in a 1.00 dm$^3$ vessel at 700 K, where $K_c = 54.0$ for $\mathrm{H_2} + \mathrm{I_2} \rightleftharpoons 2\mathrm{HI}$. Find the equilibrium amount of HI.", steps=[
            S("ICE table (mol)", text="H2: 1.00, change -x, equilibrium 1.00 - x. I2: same. HI: 0, change +2x, equilibrium 2x."),
            S("Kc expression", math=r"K_c = \dfrac{(2x)^2}{(1 - x)(1 - x)} = 54.0"),
            S("Take the square root of both sides", math=r"\dfrac{2x}{1 - x} = \sqrt{54.0} = 7.348"),
            S("Solve", math=r"2x = 7.348 - 7.348x \Rightarrow 9.348x = 7.348 \Rightarrow x = 0.786"),
            S("Equilibrium amounts", math=r"n(\mathrm{HI}) = 2x = 1.57\ \text{mol}; \qquad n(\mathrm{H_2}) = n(\mathrm{I_2}) = 1 - 0.786 = 0.214\ \text{mol}"),
        ], check=r"\dfrac{(1.572)^2}{(0.2139)^2} = 54.0"),
        EX("Worked example 2: a quadratic equation", intro=r"2.00 mol of ethanol and 1.00 mol of ethanoic acid reach equilibrium with $K_c = 4.0$ for $\mathrm{C_2H_5OH} + \mathrm{CH_3COOH} \rightleftharpoons \mathrm{CH_3COOC_2H_5} + \mathrm{H_2O}$. Find the amount of ester formed. (The volume cancels because the numbers of moles are equal on both sides.)", steps=[
            S("ICE table (mol)", text="Ethanol: 2.00 - x. Acid: 1.00 - x. Ester: x. Water: x."),
            S("Kc expression", math=r"\dfrac{x^2}{(2.00 - x)(1.00 - x)} = 4.0"),
            S("Expand", math=r"x^2 = 4.0(2.00 - 3.00x + x^2) \Rightarrow 3x^2 - 12x + 8 = 0"),
            S("Quadratic formula", math=r"x = \dfrac{12 \pm \sqrt{144 - 96}}{6} = \dfrac{12 \pm 6.928}{6}"),
            S("Choose the sensible root", math=r"x = 0.845\ \text{mol}", text="The other root, 3.15, is larger than the 1.00 mol of acid and is impossible."),
        ], check=r"\dfrac{(0.845)^2}{(1.155)(0.155)} = 4.0"),
        H("Kp and the degree of dissociation"),
        D(r"The **degree of dissociation** $\alpha$ is the fraction of the original substance that has dissociated at equilibrium. If you start with 1 mol of $\mathrm{N_2O_4}$, then $\alpha$ mol dissociate, giving $2\alpha$ mol of $\mathrm{NO_2}$ and leaving $(1 - \alpha)$ mol of $\mathrm{N_2O_4}$. The total is $(1 + \alpha)$ mol.",
          title="Degree of dissociation"),
        EX("Worked example 3: Kp for dinitrogen tetraoxide", intro=r"1.00 mol of $\mathrm{N_2O_4}$ is 20% dissociated ($\alpha = 0.20$) at equilibrium at a total pressure of 100 kPa. Calculate $K_p$ for $\mathrm{N_2O_4} \rightleftharpoons 2\mathrm{NO_2}$. Then find $\alpha$ at 200 kPa.", steps=[
            S("Moles at equilibrium", math=r"n(\mathrm{N_2O_4}) = 0.80,\quad n(\mathrm{NO_2}) = 0.40,\quad n_{total} = 1.20"),
            S("Partial pressures", math=r"p(\mathrm{N_2O_4}) = \dfrac{0.80}{1.20} \times 100 = 66.7\ \text{kPa};\qquad p(\mathrm{NO_2}) = \dfrac{0.40}{1.20} \times 100 = 33.3\ \text{kPa}"),
            S("Kp", math=r"K_p = \dfrac{(33.3)^2}{66.7} = 16.7\ \text{kPa}"),
            S("General result", math=r"K_p = \dfrac{4\alpha^2 P}{1 - \alpha^2}", text="Check: $4 \\times 0.04 \\times 100/0.96 = 16.7$."),
            S("At 200 kPa (same temperature, same Kp)", math=r"\alpha^2 = \dfrac{K_p}{K_p + 4P} = \dfrac{16.67}{16.67 + 800} = 0.0204 \Rightarrow \alpha = 0.143", text="Doubling the pressure lowers dissociation from 20% to 14.3%: the equilibrium shifts towards fewer gas molecules."),
        ]),
        H("The reaction quotient Q"),
        D(r"The **reaction quotient** $Q$ has the same form as $K_c$ but uses the concentrations at **any moment**. Compare $Q$ with $K$: if $Q < K$ the reaction moves forward (towards products); if $Q > K$ it moves backward; if $Q = K$ it is at equilibrium.",
          title="Reaction quotient Q"),
        EX("Worked example 4: which way does it go?", intro=r"For $\mathrm{H_2} + \mathrm{I_2} \rightleftharpoons 2\mathrm{HI}$ at 700 K, $K_c = 54.0$. A mixture has $[\mathrm{H_2}] = 0.10$, $[\mathrm{I_2}] = 0.10$ and $[\mathrm{HI}] = 1.0\ \mathrm{mol\,dm^{-3}}$. Predict the direction of change.", steps=[
            S("Calculate Q", math=r"Q = \dfrac{(1.0)^2}{(0.10)(0.10)} = 100"),
            S("Compare", math=r"Q = 100 > K_c = 54.0", text="Too much product: the reaction moves backward until Q falls to 54.0."),
        ]),
        MISTAKE("Forgetting the factor 2 in the change row", r"For $\mathrm{H_2} + \mathrm{I_2} \rightleftharpoons 2\mathrm{HI}$, if $x$ mol of each reactant is used, $2x$ mol of HI forms. The coefficient decides the change."),
        MISTAKE("Keeping an impossible root", r"A quadratic gives two answers. The one that makes any amount negative or larger than what was available must be rejected."),
        TIP(r"If both sides of $K_c$ are perfect squares, take the square root before solving: it avoids a quadratic. Always check your answer by substituting back into the $K_c$ expression."),
        QUIZ(r"A mixture has $Q = 2.0$ and $K_c = 8.0$ at the same temperature. The reaction", [
            "is at equilibrium", "moves towards the products", "moves towards the reactants", "stops"], 1,
             r"$Q < K$: too little product, so the forward reaction occurs until $Q$ rises to $K$.", hint="Compare Q with K.",
             feedback=["That needs Q equal to K.", "", "That needs Q greater than K.", "It moves; it does not stop."]),
        QUIZ(r"For $\mathrm{N_2O_4} \rightleftharpoons 2\mathrm{NO_2}$ at constant temperature, increasing the total pressure", [
            "raises the degree of dissociation", "lowers the degree of dissociation", "raises $K_p$", "lowers $K_p$"], 1,
             r"The equilibrium shifts towards fewer moles of gas (to $\mathrm{N_2O_4}$), so $\alpha$ falls. $K_p$ does not change at constant temperature.",
             hint="Which side has fewer gas molecules?",
             feedback=["It lowers it.", "", "K does not change with pressure.", "K does not change with pressure."]),
        PQ(r"For $\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{C} + \mathrm{D}$, $K_c = 9.0$. 1.00 mol each of A and B are placed in a 1.00 dm$^3$ vessel. Calculate the equilibrium amount of C.",
           r"$x^2/(1 - x)^2 = 9.0$, so $x/(1 - x) = 3$, $x = 3 - 3x$, $4x = 3$, $x = 0.75$ mol of C (and of D); 0.25 mol of each of A and B remain. Check: $0.75^2/0.25^2 = 9.0$."),
        PQ(r"For $\mathrm{N_2O_4} \rightleftharpoons 2\mathrm{NO_2}$, 1.00 mol of $\mathrm{N_2O_4}$ is 30% dissociated at 50 kPa total pressure. Calculate $K_p$.",
           r"$n(\mathrm{N_2O_4}) = 0.70$, $n(\mathrm{NO_2}) = 0.60$, total $= 1.30$. $p(\mathrm{N_2O_4}) = (0.70/1.30) \times 50 = 26.9$ kPa; $p(\mathrm{NO_2}) = (0.60/1.30) \times 50 = 23.1$ kPa. $K_p = 23.08^2/26.92 = 19.8\ \mathrm{kPa}$. (Using $4\alpha^2P/(1 - \alpha^2) = 4 \times 0.09 \times 50/0.91 = 19.8$.)"),
        PQ(r"For $\mathrm{H_2} + \mathrm{I_2} \rightleftharpoons 2\mathrm{HI}$ at 700 K ($K_c = 54.0$), a mixture contains $[\mathrm{H_2}] = 0.50$, $[\mathrm{I_2}] = 0.50$ and $[\mathrm{HI}] = 2.0\ \mathrm{mol\,dm^{-3}}$. Is it at equilibrium? If not, which way will it move?",
           r"$Q = (2.0)^2/(0.50 \times 0.50) = 16$. $Q < K_c$ ($16 < 54.0$), so the mixture is not at equilibrium; it moves forward, forming more HI."),
        SUM(r"ICE table: initial, change (using coefficients), equilibrium; substitute into $K_c$ and solve; reject impossible roots.",
            r"$K_p = 4\alpha^2P/(1 - \alpha^2)$ for $\mathrm{N_2O_4} \rightleftharpoons 2\mathrm{NO_2}$, from partial pressures $p = xP$.",
            r"$Q < K$: moves forward. $Q > K$: moves backward. $Q = K$: at equilibrium.",
            r"Increasing the pressure shifts equilibrium towards fewer moles of gas but does not change $K_p$."),
    ],
))

# ------------------------------------------------------------------ 14. Le Chatelier in industry
LESSONS.append(lesson(
    module=M6,
    topic="Le Chatelier's principle in industry",
    title="Le Chatelier's principle and industrial processes",
    slug="chl2-le-chatelier-industry",
    minutes=24,
    summary="Predict the effect of concentration, pressure, temperature and a catalyst on an equilibrium, support it with Q and K, and explain the conditions chosen in the Haber and Contact processes.",
    objectives=[
        "State Le Chatelier's principle and predict the effect of changing concentration, pressure and temperature",
        "Support predictions with the reaction quotient Q and the temperature dependence of K",
        "State what a catalyst does and does not do to an equilibrium",
        "Explain the conditions used in the Haber and Contact processes as compromises between yield, rate and cost",
    ],
    key_concepts=["Le Chatelier's principle", "Position of equilibrium", "Yield", "Rate", "Catalyst", "Haber process", "Contact process", "Compromise conditions"],
    blocks=[
        H("Introduction"),
        T(r"Cameroon's farmers rely on nitrogen fertilisers, and the nitrogen in them was made from air by the Haber process. Chemical engineers want as much ammonia as possible, as fast as possible, at the lowest cost. "
          r"These aims pull in different directions, and the principle of Le Chatelier helps explain how they strike a balance."),
        H("The principle"),
        D(r"**Le Chatelier's principle** states that if a change is made to a system at equilibrium, the position of equilibrium moves in the direction that opposes (reduces) the change.", title="Le Chatelier's principle"),
        KEY("Effects of changes on the position of equilibrium", r"Use this as a checklist.",
            cards=[["Add reactant (or remove product)", "Equilibrium moves to the right, using up the reactant."],
                   ["Increase pressure", "Moves towards the side with fewer moles of gas. No effect if the moles are equal."],
                   ["Increase temperature", "Moves in the endothermic direction. K falls for an exothermic forward reaction."],
                   ["Add a catalyst", "No change in position or K. It only speeds the approach to equilibrium."]]),
        T(r"Do not rely on the principle alone. Support it with numbers, using $Q$ and $K$."),
        EX("Worked example 1: effect of pressure on the Haber process", intro=r"For $\mathrm{N_2} + 3\mathrm{H_2} \rightleftharpoons 2\mathrm{NH_3}$ at equilibrium, the volume is suddenly halved at constant temperature. Show that the equilibrium moves right.", steps=[
            S("Concentrations double immediately", math=r"Q = \dfrac{(2[\mathrm{NH_3}])^2}{(2[\mathrm{N_2}])(2[\mathrm{H_2}])^3} = \dfrac{4}{2 \times 8} \times K_c = \dfrac{K_c}{4}"),
            S("Compare", math=r"Q = \dfrac{K_c}{4} < K_c", text="$Q < K$, so the reaction moves forward: more $\\mathrm{NH_3}$ forms, reducing the number of gas molecules and so opposing the rise in pressure."),
        ]),
        EX("Worked example 2: adding hydrogen", intro=r"At equilibrium $[\mathrm{N_2}] = 0.50$, $[\mathrm{H_2}] = 1.50$ and $[\mathrm{NH_3}] = 0.20\ \mathrm{mol\,dm^{-3}}$, so $K_c = 0.0237\ \mathrm{dm^6\,mol^{-2}}$. Extra hydrogen is added to raise $[\mathrm{H_2}]$ immediately to $2.00\ \mathrm{mol\,dm^{-3}}$. Which way does the equilibrium shift?", steps=[
            S("Calculate Q", math=r"Q = \dfrac{(0.20)^2}{(0.50)(2.00)^3} = \dfrac{0.040}{4.00} = 0.0100"),
            S("Compare", math=r"Q = 0.0100 < K_c = 0.0237", text="Forward reaction: more $\\mathrm{NH_3}$ forms and some of the added $\\mathrm{H_2}$ is used."),
        ]),
        H("Temperature: why K changes"),
        T(r"Changing concentration or pressure shifts the position but leaves $K$ unchanged. Temperature is different: it changes $K$. For an **exothermic** forward reaction a rise in temperature lowers $K$, because the reaction opposes the heating by moving in the endothermic (reverse) direction. "
          r"A simple model, with $\Delta H = -92.4\ \mathrm{kJ}$ and $\Delta S = -198.7\ \mathrm{J\,K^{-1}}$ taken as constant, gives the standard $K$ for ammonia synthesis from $K = e^{-\Delta G/RT}$:"),
        CODE("temperature   dG / kJ     K (simple model)\n"
             "298 K         -33.2       6.6 x 10^5\n"
             "673 K (400 C) +41.3       6.2 x 10^-4\n"
             "723 K (450 C) +51.3       2.0 x 10^-4\n"
             "773 K (500 C) +61.2       7.3 x 10^-5", "text", title="K for N2 + 3H2 <=> 2NH3 falls as the temperature rises"),
        T(r"These numbers are from a model with constant $\Delta H$ and $\Delta S$, so they are only a guide to the trend. The fall of K by a factor of about 10 000 from 298 K to 723 K shows why the equilibrium yield is poor at high temperature."),
        H("Industrial processes"),
        D(r"**Haber process.** $\mathrm{N_2(g)} + 3\mathrm{H_2(g)} \rightleftharpoons 2\mathrm{NH_3(g)}$, $\Delta H = -92\ \mathrm{kJ\,mol^{-1}}$ (per equation). Typical conditions: about 400 to 450 degrees C, about 150 to 250 atm, iron catalyst. Only about 10 to 20% is converted per pass (check your textbook); the ammonia is liquefied and removed and unreacted gases are recycled.",
          title="Haber process"),
        T(r"**Why not a low temperature?** The reaction is exothermic, so a low temperature gives a higher equilibrium yield but the rate is far too slow. 400 to 450 degrees C with a catalyst is a compromise between yield and rate. "
          r"**Why high pressure?** Four moles of gas become two, so high pressure raises the yield and also the rate. But very high pressure needs thick, expensive vessels and a lot of energy for compressors, so about 200 atm is a compromise on cost and safety."),
        D(r"**Contact process (sulfuric acid).** $2\mathrm{SO_2(g)} + \mathrm{O_2(g)} \rightleftharpoons 2\mathrm{SO_3(g)}$, $\Delta H = -196\ \mathrm{kJ}$ (per equation). Typical conditions: about 450 degrees C, 1 to 2 atm, vanadium(V) oxide catalyst, giving a conversion of about 99% with a second absorption stage. Even though three moles of gas become two, high pressure is not used because the yield is already high at about atmospheric pressure and high pressure would add cost and corrosion.",
          title="Contact process"),
        KEY("A catalyst and equilibrium", r"A catalyst lowers the activation energy of both forward and reverse reactions equally. It does not change the position of equilibrium or the value of K. It helps because it allows a lower temperature (better yield) for the same rate.",
            cards=[["Position of equilibrium", "Unchanged."], ["Value of K", "Unchanged."], ["Rate", "Faster in both directions; equilibrium is reached sooner."]]),
        MISTAKE("Saying a catalyst increases the yield", r"A catalyst does not change the equilibrium yield. It only reduces the time needed to reach equilibrium."),
        MISTAKE("Saying 'pressure shifts the equilibrium' when moles of gas are equal", r"If the number of gas moles is the same on both sides, changing pressure does not shift the equilibrium. Always count gas moles first."),
        TIP(r"Industrial equilibrium questions in Paper 2 usually have three parts: the effect on yield, the effect on rate, and the compromise chosen. Mention all three."),
        QUIZ(r"The forward reaction $\mathrm{N_2} + 3\mathrm{H_2} \rightleftharpoons 2\mathrm{NH_3}$ is exothermic. Increasing the temperature at constant pressure will", [
            "increase the equilibrium yield of ammonia", "decrease the equilibrium yield of ammonia", "have no effect on the equilibrium yield", "increase the value of $K_c$"], 1,
             r"The equilibrium moves in the endothermic direction (towards $\mathrm{N_2}$ and $\mathrm{H_2}$), so the yield falls and $K_c$ decreases.",
             hint="Which direction absorbs heat?",
             feedback=["This would happen if the reaction were endothermic.", "", "Temperature always changes the equilibrium position when the reaction has a non-zero dH.", "K decreases for an exothermic reaction."]),
        QUIZ(r"Which change does **not** alter the equilibrium amount of $\mathrm{SO_3}$ in $2\mathrm{SO_2} + \mathrm{O_2} \rightleftharpoons 2\mathrm{SO_3}$ ($\Delta H < 0$)?", [
            "Raising the pressure", "Raising the temperature", "Adding more oxygen", "Adding a vanadium(V) oxide catalyst"], 3,
             r"A catalyst speeds both directions equally; the equilibrium composition is unchanged.", hint="Which one only affects the rate?",
             feedback=["Higher pressure favours fewer gas moles: more SO3.", "Higher temperature favours the endothermic direction: less SO3.", "More O2 shifts the equilibrium to the right.", ""]),
        PQ(r"For the Haber process explain why a temperature of about 450 degrees C is used rather than 25 degrees C.",
           r"The forward reaction is exothermic, so a low temperature would give a higher equilibrium yield. But at 25 degrees C the rate is negligible. At about 450 degrees C the rate is high enough, with the iron catalyst, to reach equilibrium quickly. The lower yield per pass is accepted and unreacted gases are recycled."),
        PQ(r"In the Contact process, explain (a) why the temperature is about 450 degrees C and (b) why a pressure of only 1 to 2 atm is used.",
           r"(a) The forward reaction is exothermic: a lower temperature favours a higher yield, but is too slow; with the vanadium(V) oxide catalyst, about 450 degrees C gives a fast rate and a good yield. (b) Higher pressure would favour the side with fewer gas moles ($\mathrm{SO_3}$), but the yield is already about 99% at about atmospheric pressure, and higher pressure would add cost and corrosion problems for little gain."),
        PQ(r"Methanol is made by $\mathrm{CO(g)} + 2\mathrm{H_2(g)} \rightleftharpoons \mathrm{CH_3OH(g)}$, $\Delta H = -91\ \mathrm{kJ\,mol^{-1}}$. State the effect on the equilibrium yield of (a) increasing the pressure and (b) increasing the temperature. Give reasons.",
           r"(a) Three moles of gas become one, so higher pressure moves the equilibrium to the right and raises the yield. (b) The forward reaction is exothermic, so a higher temperature moves the equilibrium to the left, lowering the yield and $K$."),
        SUM(r"Le Chatelier's principle: the equilibrium shifts to oppose a change. Check with $Q$ against $K$.",
            r"Pressure shifts towards fewer gas moles; temperature shifts the position and changes $K$ (exothermic: $K$ falls as $T$ rises); concentration shifts the position only.",
            r"A catalyst changes only the rate, not the yield or $K$.",
            r"The Haber process (about 450 degrees C, about 200 atm, iron) and the Contact process (about 450 degrees C, 1 to 2 atm, $\mathrm{V_2O_5}$) use compromise conditions."),
    ],
))

# ------------------------------------------------------------------ 15. Raoult's law
LESSONS.append(lesson(
    module=M6,
    topic="Raoult's law and fractional distillation",
    title="Raoult's law and ideal liquid mixtures",
    slug="chl2-raoults-law",
    minutes=22,
    summary="Vapour pressure and mole fraction, Raoult's law for ideal mixtures and for a non-volatile solute, total pressure and vapour composition calculations.",
    objectives=[
        "Define vapour pressure and volatility",
        "State Raoult's law and the conditions for an ideal solution",
        "Calculate partial pressures, total pressure and vapour composition for an ideal mixture of two liquids",
        "Calculate the lowering of vapour pressure by a non-volatile solute",
    ],
    key_concepts=["Vapour pressure", "Volatility", "Mole fraction", "Raoult's law", "Ideal solution", "Partial vapour pressure", "Dalton's law"],
    blocks=[
        H("Introduction"),
        T(r"Petrol and diesel from a roadside pump differ in how easily they evaporate: petrol fumes reach you much faster. Palm wine ferments to a mixture of ethanol and water, and a distiller wants to know how much ethanol will leave in the vapour. "
          r"Raoult's law connects the composition of a liquid mixture to the composition of its vapour."),
        H("Vapour pressure and mole fraction"),
        D(r"The **vapour pressure** of a liquid is the pressure exerted by its vapour when the vapour is in dynamic equilibrium with the liquid in a closed container at a fixed temperature. A liquid with a high vapour pressure at a given temperature is more **volatile**.", title="Vapour pressure"),
        D(r"The **mole fraction** $x_A$ of component A in a mixture is the amount of A divided by the total amount of all components. The mole fractions add to 1.", title="Mole fraction", formula=r"x_A = \dfrac{n_A}{n_A + n_B}"),
        H("Raoult's law"),
        D(r"**Raoult's law**: in an ideal solution the partial vapour pressure of a component equals its mole fraction in the liquid times the vapour pressure of the pure component at the same temperature.",
          title="Raoult's law", formula=r"p_A = x_A\,p_A^{\circ} \qquad p_B = x_B\,p_B^{\circ}"),
        T(r"The total vapour pressure is the sum of the partial pressures (Dalton's law of partial pressures). The mole fraction of A in the **vapour** follows from the ratio of $p_A$ to the total pressure:"),
        F(r"P = p_A + p_B \qquad y_A = \dfrac{p_A}{P}", title="Total pressure and vapour composition (y is a mole fraction in the vapour)"),
        D(r"An **ideal solution** obeys Raoult's law at all compositions. It forms when the attractions between unlike molecules (A-B) are about equal to those between like molecules (A-A and B-B). Mixing is then neither exothermic nor endothermic ($\Delta H_{mix} \approx 0$) and the volume is the sum of the volumes of the pure liquids. Examples are close to ideal: hexane with heptane, or benzene with methylbenzene.", title="Ideal solution"),
        CODE("Teaching data at one temperature: pure A = 50 kPa, pure B = 20 kPa\n"
             "x(A) liquid   p(A)    p(B)    total P   y(A) vapour\n"
             "0.00           0.0    20.0     20.0      0.000\n"
             "0.20          10.0    16.0     26.0      0.385\n"
             "0.40          20.0    12.0     32.0      0.625\n"
             "0.60          30.0     8.0     38.0      0.789\n"
             "0.80          40.0     4.0     44.0      0.909\n"
             "1.00          50.0     0.0     50.0      1.000", "text", title="Ideal mixture of A and B (all values in kPa)"),
        T(r"The total pressure rises in a straight line from the pressure of pure B to that of pure A. At every composition the vapour is richer in the more volatile component A than the liquid (compare 0.40 in the liquid with 0.625 in the vapour)."),
        EX("Worked example 1: pressures and vapour composition", intro=r"A liquid mixture has $x_A = 0.40$ at a temperature where pure A has vapour pressure 50 kPa and pure B has 20 kPa. Find the partial pressures, the total pressure and the mole fraction of A in the vapour.", steps=[
            S("Mole fraction of B", math=r"x_B = 1 - 0.40 = 0.60"),
            S("Partial pressures", math=r"p_A = 0.40 \times 50 = 20.0\ \text{kPa} \qquad p_B = 0.60 \times 20 = 12.0\ \text{kPa}"),
            S("Total pressure", math=r"P = 20.0 + 12.0 = 32.0\ \text{kPa}"),
            S("Vapour composition", math=r"y_A = \dfrac{20.0}{32.0} = 0.625"),
        ], check=r"0.625 + 0.375 = 1"),
        EX("Worked example 2: composition from the total pressure", intro=r"For the same liquids, find the liquid composition for which the total vapour pressure is 40 kPa, and the vapour composition then.", steps=[
            S("Write P in terms of x_A", math=r"P = 50x_A + 20(1 - x_A) = 20 + 30x_A"),
            S("Set P = 40", math=r"40 = 20 + 30x_A \Rightarrow x_A = \dfrac{20}{30} = 0.667"),
            S("Vapour composition", math=r"p_A = 0.667 \times 50 = 33.3\ \text{kPa} \Rightarrow y_A = \dfrac{33.3}{40} = 0.833"),
        ]),
        H("A non-volatile solute"),
        T(r"When a **non-volatile** solute (one that does not evaporate, such as sugar or salt) dissolves in a solvent, only the solvent contributes to the vapour pressure. The solute particles occupy part of the surface, so fewer solvent molecules escape. Raoult's law gives the vapour pressure of the solvent as $p = x_{solvent}\,p^\circ$."),
        D(r"The **relative lowering of vapour pressure** equals the mole fraction of the solute:", title="Lowering of vapour pressure", formula=r"\dfrac{p^\circ - p}{p^\circ} = x_{solute}"),
        EX("Worked example 3: urea in water", intro=r"6.00 g of urea ($M = 60.0$, non-volatile) is dissolved in 90.0 g of water ($M = 18.0$) at 25 degrees C, where pure water has vapour pressure 3.17 kPa. Calculate the vapour pressure of the solution.", steps=[
            S("Moles of urea", math=r"n_{urea} = \dfrac{6.00}{60.0} = 0.100\ \text{mol}"),
            S("Moles of water", math=r"n_{water} = \dfrac{90.0}{18.0} = 5.00\ \text{mol}"),
            S("Mole fraction of water", math=r"x_{water} = \dfrac{5.00}{5.00 + 0.100} = 0.980"),
            S("Vapour pressure", math=r"p = 0.980 \times 3.17 = 3.11\ \text{kPa}", text="The lowering is $3.17 - 3.11 = 0.062$ kPa, equal to $x_{urea} \\times 3.17 = 0.0196 \\times 3.17$."),
        ]),
        MISTAKE("Using mass fraction or volume fraction", r"Raoult's law uses **mole fractions**. Convert masses to moles first."),
        MISTAKE("Assuming the vapour has the same composition as the liquid", r"The vapour is richer in the more volatile component. Find $y_A$ from $p_A/P$, not from $x_A$."),
        TIP(r"Raoult's law questions give pure-liquid vapour pressures at one temperature and ask for partial pressures, total pressure and vapour composition. Present them in a small table."),
        QUIZ(r"In an ideal mixture of A and B, the vapour above the liquid is richer than the liquid in", [
            "the less volatile component", "the more volatile component", "neither: the compositions are equal", "whichever component has the larger mole fraction"], 1,
             r"The more volatile component (higher $p^\circ$) contributes a larger share of the pressure, so it is enriched in the vapour.", hint="Which component evaporates more easily?",
             feedback=["The less volatile component is depleted in the vapour.", "", "The compositions are equal only for pure liquids.", "The vapour composition depends on p0, not just on the liquid mole fractions."]),
        QUIZ(r"Which condition describes an ideal solution of A and B?", [
            "A-B attractions are much stronger than A-A and B-B", "A-B attractions are much weaker than A-A and B-B",
            "A-B attractions are about the same as A-A and B-B", "A and B do not mix"], 2,
             r"If unlike and like attractions are about equal, molecules escape equally easily from the mixture: Raoult's law holds and there is no heat or volume change on mixing.", hint="Think about how easily a molecule leaves a mixture.",
             feedback=["Strong A-B attraction leads to negative deviation.", "Weak A-B attraction leads to positive deviation.", "", "Immiscible liquids are another case (steam distillation, a later lesson)."]),
        PQ(r"At a given temperature pure A has vapour pressure 50 kPa and pure B has 20 kPa. A liquid mixture has $x_A = 0.20$. Calculate the total vapour pressure and the mole fraction of A in the vapour.",
           r"$p_A = 0.20 \times 50 = 10.0$ kPa; $p_B = 0.80 \times 20 = 16.0$ kPa; $P = 26.0$ kPa. $y_A = 10.0/26.0 = 0.385$ (the vapour is almost twice as rich in A as the liquid)."),
        PQ(r"The vapour pressure of pure water at 25 degrees C is 3.17 kPa. Calculate the vapour pressure of a solution of 18.0 g of glucose ($M = 180$, non-volatile) in 180 g of water.",
           r"$n_{glucose} = 0.100$ mol; $n_{water} = 180/18.0 = 10.0$ mol; $x_{water} = 10.0/10.1 = 0.990$; $p = 0.990 \times 3.17 = 3.14$ kPa."),
        PQ(r"State three features of an ideal solution and explain why a mixture of two very similar hydrocarbons is expected to be nearly ideal.",
           r"Obeys Raoult's law at all compositions; $\Delta H_{mix} \approx 0$; no volume change on mixing. Two similar hydrocarbons have almost the same type and strength of intermolecular (London) forces, so the A-B attractions are the same as the A-A and B-B attractions."),
        SUM(r"Raoult's law: $p_A = x_Ap_A^\circ$ (with $x$ a mole fraction in the liquid). Total pressure $P = p_A + p_B$ and vapour composition $y_A = p_A/P$.",
            r"The vapour is richer than the liquid in the more volatile component.",
            r"An ideal solution has A-B attractions equal to A-A and B-B: $\Delta H_{mix} \approx 0$.",
            r"A non-volatile solute lowers the solvent's vapour pressure: $(p^\circ - p)/p^\circ = x_{solute}$."),
    ],
))

# ------------------------------------------------------------------ 16. Fractional distillation and azeotropes
LESSONS.append(lesson(
    module=M6,
    topic="Raoult's law and fractional distillation",
    title="Fractional distillation, non-ideal mixtures and azeotropes",
    slug="chl2-fractional-distillation-azeotropes",
    minutes=24,
    summary="Boiling-point (T-x) diagrams for ideal mixtures, how a fractionating column separates them, positive and negative deviations from Raoult's law, and minimum- and maximum-boiling azeotropes.",
    objectives=[
        "Read a boiling-point composition (T-x) diagram for an ideal mixture and explain fractional distillation",
        "Explain positive and negative deviations from Raoult's law in terms of intermolecular forces",
        "Describe minimum- and maximum-boiling azeotropes and what is collected on distilling them",
        "Explain why ethanol and water cannot be separated completely by fractional distillation",
    ],
    key_concepts=["Boiling-point diagram", "Fractional distillation", "Theoretical plate", "Positive deviation", "Negative deviation", "Azeotrope"],
    blocks=[
        H("Introduction"),
        T(r"Traditional distillers in many African villages boil fermented palm sap or maize mash in a drum and collect the vapour in a cooled pipe. The spirit that comes off is richer in ethanol than the mash, but never pure ethanol. "
          r"Laboratory and industrial distillation follows the same idea, repeated many times in a **fractionating column**, and it can fail in an instructive way for certain mixtures."),
        H("Boiling-point diagram for an ideal mixture"),
        T(r"A **boiling-point (T-x) diagram** plots the boiling temperature of a mixture at fixed pressure against its composition. There are two curves: the **liquid line** (the composition of the boiling liquid) and the **vapour line** (the composition of the vapour in equilibrium with it at that temperature)."),
        IMG("al-chl2-tx-ideal.svg", alt="Boiling-point diagram for an ideal mixture of A (lower boiling point) and B. A liquid curve lies below a vapour curve; both run from the boiling point of B at the left to that of A on the right. Green steps zig-zag between the curves toward pure A.",
            caption="Figure 1. T-x diagram for an ideal mixture (drawn with a simple model; the numbers are illustrative)."),
        T(r"Pick a liquid of composition $x$. Heat it until it boils at the temperature where the vertical line meets the liquid line. A horizontal line at that temperature meets the vapour line at the vapour composition $y$. The vapour is richer in A, the lower-boiling (more volatile) component. "
          r"If this vapour is condensed, it forms a liquid with composition $y$, which boils at a **lower** temperature and gives a vapour richer still. Repeating the cycle follows the green steps towards pure A."),
        D(r"**Fractional distillation** repeats the evaporation and condensation cycle many times in a fractionating column packed with glass beads or fitted with trays. Each cycle is called a **theoretical plate**. The temperature falls up the column, the more volatile component reaches the top and leaves first.",
          title="Fractional distillation"),
        EX("Worked example 1: repeated enrichment", intro=r"For an ideal mixture of A and B with $p_A^\circ/p_B^\circ = 50/20 = 2.5$, a liquid has $x_A = 0.40$. Find the vapour composition after each of the first three evaporation-condensation cycles. (Treat the ratio $2.5$ as constant; it varies a little with temperature.)", steps=[
            S("Cycle 1", math=r"y_A = \dfrac{0.40 \times 50}{0.40 \times 50 + 0.60 \times 20} = \dfrac{20}{32} = 0.625"),
            S("Cycle 2 (condense, then boil again)", math=r"y_A = \dfrac{0.625 \times 50}{0.625 \times 50 + 0.375 \times 20} = \dfrac{31.25}{38.75} = 0.806"),
            S("Cycle 3", math=r"y_A = \dfrac{0.806 \times 50}{0.806 \times 50 + 0.194 \times 20} = 0.912", text="Three theoretical plates take the composition from 40% to 91% A. A column with more plates reaches higher purity: six plates give about 99%."),
        ]),
        H("Non-ideal mixtures"),
        T(r"Many real mixtures do not obey Raoult's law. The reason is that A-B attractions differ from A-A and B-B attractions."),
        D(r"**Positive deviation:** the vapour pressure is **higher** than Raoult's law predicts. The A-B attractions are **weaker** than A-A and B-B, so molecules escape more easily. Mixing is **endothermic** ($\Delta H_{mix} > 0$) and there is a small increase in volume. Example: ethanol and water, or ethanol and hexane.",
          title="Positive deviation"),
        D(r"**Negative deviation:** the vapour pressure is **lower** than Raoult's law predicts. The A-B attractions are **stronger** than A-A and B-B, so molecules escape less easily. Mixing is **exothermic** ($\Delta H_{mix} < 0$) and the volume decreases slightly. Example: nitric acid and water, or hydrochloric acid and water.",
          title="Negative deviation"),
        H("Azeotropes"),
        D(r"An **azeotrope** (constant-boiling mixture) is a mixture of definite composition that boils at a constant temperature and gives a vapour with the **same composition** as the liquid. It cannot be separated by distillation.", title="Azeotrope"),
        IMG("al-chl2-tx-azeotrope.svg", alt="Boiling-point diagram with a minimum. The liquid and vapour curves touch at a single point (the azeotrope) below the boiling points of both pure A and pure B.",
            caption="Figure 2. A minimum-boiling azeotrope (positive deviation), drawn with a simple model; the composition here is illustrative."),
        T(r"**Minimum-boiling azeotrope (positive deviation).** The boiling point passes through a minimum. Ethanol and water form such an azeotrope containing about 95.6% ethanol by mass, boiling at about 78.2 degrees C (check your textbook; pure ethanol boils at 78.4 degrees C). "
          r"Fractional distillation of dilute aqueous ethanol gives the azeotrope as distillate (it boils at the lowest temperature) and leaves water in the flask. **Pure ethanol cannot be obtained** from it by distillation."),
        T(r"**Maximum-boiling azeotrope (negative deviation).** The boiling point passes through a maximum. Nitric acid and water form an azeotrope of about 68% nitric acid by mass, boiling near 121 degrees C; hydrochloric acid and water give about 20% HCl by mass at about 110 degrees C (check your textbook). "
          r"On distillation the azeotrope stays in the flask as the **residue** (it boils at the highest temperature); the distillate is whichever pure component was in excess."),
        CODE("deviation   A-B forces      dH(mix)   boiling-point diagram   distillate          residue\n"
             "ideal       same as A-A/B-B   ~0        no extremum             pure A (lower bp)   pure B\n"
             "positive    weaker            +         minimum (azeotrope)     azeotrope           pure A or pure B\n"
             "negative    stronger          -         maximum (azeotrope)     pure A or pure B    azeotrope", "text", title="Summary"),
        EX("Worked example 2: distilling dilute ethanol", intro=r"A mixture of 30% ethanol and 70% water by mass is fractionally distilled with a long column. What are the distillate and the residue after a long time?", steps=[
            S("Identify the system", text="Ethanol-water shows positive deviation with a minimum-boiling azeotrope at about 95.6% ethanol."),
            S("Which side is the mixture on?", text="30% ethanol is on the water-rich side of the azeotrope."),
            S("Result", text="The distillate approaches the azeotrope (about 95.6% ethanol). The residue becomes pure water. Further enrichment beyond the azeotrope is impossible by distillation."),
        ]),
        EX("Worked example 3: distilling dilute nitric acid", intro=r"A solution of 40% nitric acid by mass is distilled. What are the distillate and the residue?", steps=[
            S("Identify the system", text="Nitric acid and water have negative deviation with a maximum-boiling azeotrope at about 68% HNO3."),
            S("Which side is the mixture on?", text="40% is on the water-rich side of the azeotrope."),
            S("Result", text="The distillate is nearly pure water (the more volatile component on this side). The residue approaches the azeotrope, about 68% HNO3."),
        ]),
        MISTAKE("Thinking distillation can give pure ethanol from any mixture", r"Distillation of ethanol and water stops at the azeotrope. To make 'absolute' ethanol, the last water is removed by another method (for example a drying agent or molecular sieves)."),
        MISTAKE("Mixing up the deviations", r"Positive deviation means higher vapour pressure, weaker A-B attractions, lower boiling-point minimum. Negative deviation means lower vapour pressure, stronger A-B attractions, a maximum."),
        TIP(r"Draw the T-x diagram and mark the starting composition. Questions on azeotropes in Paper 2 ask for the distillate and the residue at the end of the fractional distillation."),
        QUIZ(r"Which pair of statements describes a mixture that shows **positive** deviation from Raoult's law?", [
            "A-B forces weaker than A-A and B-B; boiling-point diagram has a minimum", "A-B forces weaker than A-A and B-B; boiling-point diagram has a maximum",
            "A-B forces stronger than A-A and B-B; boiling-point diagram has a minimum", "A-B forces stronger than A-A and B-B; boiling-point diagram has a maximum"], 0,
             r"Weaker A-B forces raise the vapour pressure, lower the boiling temperature and give a minimum-boiling azeotrope.", hint="Higher vapour pressure means a lower boiling point.",
             feedback=["", "Weak forces would give a minimum, not a maximum.", "Strong forces give a maximum.", "This describes negative deviation."]),
        QUIZ(r"Fractional distillation of a mixture that forms a minimum-boiling azeotrope, starting on the A-rich side of the azeotrope, gives as the final distillate", [
            "pure A", "pure B", "the azeotrope", "an equal mixture of A and B"], 2,
             r"The azeotrope has the lowest boiling point, so it distils first and the distillate approaches the azeotrope; the excess component remains.", hint="Which has the lowest boiling point on the diagram?",
             feedback=["Pure A cannot be obtained as distillate because the azeotrope boils lower.", "Pure B is not a distillate on this side.", "", "There is no special 1:1 composition."]),
        PQ(r"Explain, in terms of intermolecular forces, why ethanol and water show a positive deviation from Raoult's law.",
           r"Pure ethanol and pure water both have hydrogen bonding. In the mixture, the hydrogen bonds between ethanol and water are weaker overall than the average of the strong water-water hydrogen-bond network and the ethanol-ethanol attractions, and the ethyl groups disrupt the water structure. Molecules therefore escape more easily than in an ideal mixture and the vapour pressure is higher than Raoult's law predicts."),
        PQ(r"Describe what is collected when a 60% by mass solution of nitric acid (azeotrope about 68%) is fractionally distilled, and explain why the process cannot give pure nitric acid.",
           r"The mixture lies on the water-rich side of the maximum-boiling azeotrope, so the distillate is water-rich and the residue approaches the azeotrope. Further distillation of the azeotrope gives a vapour with the same composition as the liquid, so no further separation occurs and pure nitric acid cannot be obtained by this method."),
        PQ(r"Use the repeated-enrichment idea of worked example 1 to find how many theoretical plates are needed to raise the vapour mole fraction of A above 0.95, starting from $x_A = 0.40$ and with $p_A^\circ/p_B^\circ = 2.5$.",
           r"After plates 1 to 4 the vapour mole fractions are 0.625, 0.806, 0.912 and 0.963. The value first exceeds 0.95 at the fourth cycle, so four theoretical plates are needed."),
        SUM(r"A T-x diagram has a liquid line and a vapour line; the vapour is richer in the more volatile component, and repeated cycles in a fractionating column enrich it further.",
            r"Positive deviation: weaker A-B forces, higher vapour pressure, minimum-boiling azeotrope. Negative deviation: stronger A-B forces, lower vapour pressure, maximum-boiling azeotrope.",
            r"An azeotrope boils at constant temperature with vapour of the same composition as the liquid and cannot be separated by distillation.",
            r"Ethanol-water (minimum, about 95.6% ethanol) and nitric acid-water (maximum, about 68%) are the standard examples."),
    ],
))

# ------------------------------------------------------------------ 17. Steam distillation and partition
LESSONS.append(lesson(
    module=M6,
    topic="Steam distillation and the partition coefficient",
    title="Steam distillation and the partition coefficient",
    slug="chl2-steam-distillation-partition",
    minutes=24,
    summary="How immiscible liquids distil together in steam distillation, how to calculate the mass ratio of the distillate, and how the partition coefficient governs solvent extraction.",
    objectives=[
        "Explain steam distillation and when it is used",
        "Calculate the composition of the distillate from vapour pressures and molar masses",
        "Define the partition coefficient and calculate its value from concentrations",
        "Calculate the amount extracted by one or several portions of solvent, and explain why several small portions are better",
    ],
    key_concepts=["Immiscible liquids", "Steam distillation", "Partition coefficient", "Solvent extraction", "Distribution law", "Association and dissociation"],
    blocks=[
        H("Introduction"),
        T(r"Lemongrass and eucalyptus oils are extracted by passing steam through the leaves. The oil is damaged if heated directly to its own high boiling point, yet it comes over with steam below 100 degrees C. "
          r"Another everyday method, shaking a plant extract with a solvent to pull out a chemical, relies on how the chemical is shared between two liquids. In this lesson you study both ideas."),
        H("Steam distillation"),
        T(r"Two liquids that are **immiscible** (do not mix) each exert their own vapour pressure, as if the other were absent. The total vapour pressure of the mixture is simply the sum of the vapour pressures of the pure liquids. "
          r"The mixture boils when this total equals the external pressure. Because the sum is larger than either alone, it boils at a temperature **below the boiling point of either liquid**."),
        D(r"In **steam distillation** steam is passed through a mixture containing an organic compound that is immiscible with water. The organic compound distils with the steam below 100 degrees C and is collected from the condensate, where it separates from the water.",
          title="Steam distillation", formula=r"P_{total} = p_{water}^{\circ} + p_{organic}^{\circ}"),
        T(r"Steam distillation is used for substances that are immiscible with water, volatile in steam and may **decompose** at their normal boiling point, such as phenylamine, natural essential oils, and some oils from plants. The substance must not react with water."),
        D(r"In the vapour the ratio of the amounts of the two substances is the ratio of their vapour pressures. Using $n = m/M$:", title="Composition of the distillate",
          formula=r"\dfrac{n_{organic}}{n_{water}} = \dfrac{p_{organic}}{p_{water}} \Rightarrow \dfrac{m_{organic}}{m_{water}} = \dfrac{p_{organic} \times M_{organic}}{p_{water} \times M_{water}}"),
        EX("Worked example 1: steam distillation of phenylamine", intro=r"Phenylamine ($M = 93.0$) and water distil together at 98 degrees C, where the vapour pressures of the pure liquids are 7.0 kPa for phenylamine and 94.3 kPa for water (illustrative values; external pressure 101.3 kPa). Calculate the mass of phenylamine collected per 100 g of water in the distillate.", steps=[
            S("Check the boiling condition", math=r"7.0 + 94.3 = 101.3\ \text{kPa}", text="Total vapour pressure equals the external pressure, so the mixture boils."),
            S("Mass ratio", math=r"\dfrac{m_{ph}}{m_{water}} = \dfrac{7.0 \times 93.0}{94.3 \times 18.0} = \dfrac{651}{1697} = 0.384"),
            S("Mass per 100 g of water", math=r"0.384 \times 100 = 38.4\ \text{g}", text="Although phenylamine boils at about 184 degrees C, 38 g come over with every 100 g of water at about 98 degrees C."),
        ]),
        H("The partition coefficient"),
        D(r"When a solute dissolves in two immiscible solvents in contact, it distributes between them so that, at a fixed temperature, the ratio of its concentrations in the two layers is constant. This ratio is the **partition coefficient** $K_D$ (it is a kind of equilibrium constant).",
          title="Partition coefficient", formula=r"K_D = \dfrac{[\text{X}]_{organic}}{[\text{X}]_{aqueous}}"),
        T(r"The law holds when the solute is in the **same molecular form** in both layers and does not react with either solvent. If it dimerises in one layer (ethanoic acid in a non-polar solvent) or ionises in the other, the simple ratio is not constant (check your textbook)."),
        EX("Worked example 2: finding KD", intro=r"At equilibrium, an organic layer holds $0.040\ \mathrm{mol\,dm^{-3}}$ of a solute and the aqueous layer holds $0.0050\ \mathrm{mol\,dm^{-3}}$. Calculate $K_D$ (organic over aqueous).", steps=[
            S("Substitute", math=r"K_D = \dfrac{0.040}{0.0050} = 8.0", text="No units, because both concentrations have the same units. The solute is eight times more concentrated in the organic layer."),
        ]),
        H("Solvent extraction"),
        T(r"To extract a solute from water, shake the aqueous solution with an immiscible organic solvent in a separating funnel, then run off the layers. Suppose the aqueous solution has volume $V_{aq}$ and the solvent used has volume $V_{org}$. The fraction of the solute left in the water after one extraction is:"),
        F(r"\text{fraction left} = \dfrac{V_{aq}}{V_{aq} + K_D\,V_{org}}", title="One extraction"),
        EX("Worked example 3: one big portion against two small ones", intro=r"100 cm$^3$ of aqueous solution contain 5.00 g of solute. $K_D = 8.0$ (organic over aqueous). Compare (a) one extraction with 50 cm$^3$ of solvent and (b) two extractions with 25 cm$^3$ each (50 cm$^3$ in total).", steps=[
            S("(a) Fraction left after one 50 cm3 portion", math=r"\dfrac{100}{100 + 8.0 \times 50} = \dfrac{100}{500} = 0.20"),
            S("(a) Mass left", math=r"0.20 \times 5.00 = 1.00\ \text{g left}, \quad 4.00\ \text{g extracted}"),
            S("(b) Fraction left after one 25 cm3 portion", math=r"\dfrac{100}{100 + 8.0 \times 25} = \dfrac{100}{300} = 0.333"),
            S("(b) After two portions", math=r"(0.333)^2 \times 5.00 = 0.556\ \text{g left}, \quad 4.44\ \text{g extracted}"),
            S("Conclusion", text="The same total volume of solvent removes 4.44 g in two portions but only 4.00 g in one. **Several small extractions are more efficient than one large one.**"),
        ]),
        MISTAKE("Mixing up which layer is the numerator", r"State clearly which solvent is on top. $K_D = [\text{organic}]/[\text{aqueous}]$ is the convention here; the reverse ratio is the reciprocal. Always check the definition in the question."),
        MISTAKE("Adding the portions of solvent in the fraction formula", r"Each portion multiplies the remaining fraction by $V_{aq}/(V_{aq} + K_DV_{org})$ **separately**. Do not use the total volume in one step for several extractions."),
        TIP(r"Steam distillation and the partition coefficient can both appear in Paper 2. State the assumptions: immiscible liquids, no reaction, the same molecular species in both layers and constant temperature."),
        QUIZ(r"Why does a mixture of two immiscible liquids boil below the boiling point of either liquid?", [
            "Each liquid reacts with the other", "The total vapour pressure is the sum of the two vapour pressures, so it reaches atmospheric pressure at a lower temperature",
            "Mixing is exothermic", "The liquids have lower densities in a mixture"], 1,
             r"Each liquid exerts its own vapour pressure; the sum reaches the external pressure at a temperature below either liquid's own boiling point.",
             hint="What must the total vapour pressure equal at the boiling point?",
             feedback=["Immiscible liquids do not mix or react.", "", "They do not mix, so there is no heat of mixing.", "Density is not involved."]),
        QUIZ(r"A solute has $K_D = 8.0$ between ether and water. A student extracts 100 cm$^3$ of aqueous solution. Which is the most efficient use of 60 cm$^3$ of ether?", [
            "One extraction with 60 cm3", "Two extractions with 30 cm3", "Three extractions with 20 cm3", "It makes no difference"], 2,
             r"More portions of smaller volume leave less solute behind: fractions left are $0.172$, $0.0865$ and $0.0569$ (for 1, 2 and 3 portions). Three portions is the best of these.", hint="Compare the amounts left in each case.",
             feedback=["The least efficient of the three.", "Better than one portion but not the best.", "", "The number of portions matters."]),
        PQ(r"An organic compound of molar mass 128 steam distils with water at a temperature where the pure vapour pressures are 2.00 kPa (organic) and 99.3 kPa (water). Calculate the mass of organic compound collected with 50.0 g of water.",
           r"Ratio $m_{org}/m_{water} = (2.00 \times 128)/(99.3 \times 18.0) = 256/1787 = 0.143$. Mass $= 0.143 \times 50.0 = 7.16$ g."),
        PQ(r"The partition coefficient of a solute between ether and water is 8.0 (ether over water). Calculate the mass extracted from 100 cm$^3$ of aqueous solution containing 5.00 g by (a) one 100 cm$^3$ portion of ether, (b) three 33.3 cm$^3$ portions.",
           r"(a) Fraction left $= 100/(100 + 800) = 0.111$; extracted $= 5.00 \times 0.889 = 4.44$ g. (b) Each portion: $100/(100 + 8.0 \times 33.3) = 100/366.7 = 0.273$; after three, $0.273^3 = 0.0203$; extracted $= 5.00 \times 0.980 = 4.90$ g."),
        PQ(r"State the conditions under which the partition law holds, and explain why it fails for ethanoic acid between water and benzene.",
           r"The law holds at constant temperature for a solute that is in the same molecular form in both solvents and does not react with either. Ethanoic acid dimerises in benzene (two molecules form hydrogen-bonded pairs) but is mainly monomeric (and partly ionised) in water, so the ratio of total concentrations is not constant."),
        SUM(r"Immiscible liquids boil when the sum of their vapour pressures equals the external pressure: below the boiling point of either liquid.",
            r"Steam distillation distils heat-sensitive, water-immiscible compounds; $m_{org}/m_{water} = p_{org}M_{org}/(p_{water}M_{water})$.",
            r"$K_D = [\text{X}]_{org}/[\text{X}]_{aq}$ at a fixed temperature for the same molecular species in both layers.",
            r"Several small solvent extractions remove more solute than one large one."),
    ],
))
