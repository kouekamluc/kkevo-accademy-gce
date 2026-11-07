"""A Level Chemistry, Lower Sixth: the mole concept and titrations; atomic structure; chemical bonding (18 lessons, one practice set each).

Relative atomic masses used (state them in every question): H 1, C 12, N 14, O 16, F 19, Na 23, Mg 24, Al 27, P 31, S 32, Cl 35.5,
K 39, Ca 40, Mn 55, Fe 56, Cu 63.5, Zn 65, Br 80, I 127, Ag 108. Avogadro constant L = 6.02 x 10^23 per mole.
Gas constant R = 8.31 J per mole per kelvin. Molar gas volume: 24 dm3 at room temperature and pressure (rtp, 20 C and 1 atm);
22.4 dm3 at standard temperature and pressure (stp, 0 C and 1 atm). Ionisation energies and radii are rounded teaching data:
check your textbook for small differences.
"""

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "lower-sixth")

M1 = "The Mole Concept, Stoichiometry & Redox Titrations"
M2 = "Atomic Structure, Mass Spectrometry & Electronic Structure"
M3 = "Chemical Bonding, Molecular Geometry & Intermolecular Forces"

LESSONS = []

# ------------------------------------------------------------------ 1. The mole and the Avogadro constant
LESSONS.append(lesson(
    module=M1,
    topic="Avogadro constant and the ideal gas equation",
    title="The mole, the Avogadro constant and molar mass",
    slug="chl1-mole-avogadro-molar-mass",
    minutes=22,
    summary="Count particles in moles with the Avogadro constant, link moles to mass through molar mass, and count atoms, molecules and ions in a sample.",
    objectives=[
        "Define the mole and the Avogadro constant and say which kind of particle is being counted",
        "Convert between mass, amount in moles and number of particles",
        "Count the atoms or ions inside a given number of moles of a compound",
        "Avoid the usual slips with molecules versus atoms and with formula units",
    ],
    key_concepts=["Mole", "Avogadro constant", "Molar mass", "Formula unit", "Amount of substance"],
    blocks=[
        H("Introduction"),
        T("A seller in a Douala market counts tomatoes in heaps of five and sells salt by the cupful. Chemists cannot count atoms one by one, "
          "because an atom is far too small, so they count them in one very large heap called the **mole**. The mole links the mass you weigh "
          "on a balance to the number of particles you cannot see. Every titration and gas calculation in this course starts here."),
        H("The mole and the Avogadro constant"),
        D(r"The **mole** (symbol mol) is the amount of substance that contains as many elementary particles as there are atoms in exactly 12 g of carbon-12. "
          r"The particles can be atoms, molecules, ions or electrons, so you must always say which one you are counting.",
          title="Definition: the mole"),
        D(r"The **Avogadro constant**, $L$, is the number of particles in one mole of any substance.", title="Definition: Avogadro constant",
          formula=r"L = 6.02 \times 10^{23}\ \mathrm{mol^{-1}}",
          note="In some books the symbol is N_A. Value used in this course: 6.02 × 10^23 per mole."),
        T(r"The **molar mass**, $M$, is the mass of one mole of a substance, in $\mathrm{g\,mol^{-1}}$. It has the same number as the relative atomic mass "
          r"$A_r$ (for an element) or relative formula mass $M_r$ (for a compound). In this lesson: H 1, C 12, N 14, O 16, Na 23, Cl 35.5, Ca 40, Cu 63.5."),
        KEY("Three conversions to know", "Two formulae move you between the three quantities. The mole is the bridge.", cards=[
            [r"Mass and moles", r"$n = \dfrac{m}{M}$ with $m$ in g and $M$ in g/mol"],
            [r"Moles and particles", r"$N = n \times L$, where $N$ is the number of particles"],
            [r"Mass and particles", r"Go through moles: mass $\to n \to N$ (or back)"],
        ]),
        H("Worked examples"),
        EX("Worked example 1: molecules in a sample", intro=r"How many water molecules are in 3.6 g of water? ($A_r$: H 1, O 16)", steps=[
            S("Find the molar mass", math=r"M(\mathrm{H_2O}) = 2(1) + 16 = 18\ \mathrm{g\,mol^{-1}}"),
            S("Find the moles", math=r"n = \frac{3.6}{18} = 0.20\ \mathrm{mol}"),
            S("Multiply by the Avogadro constant", math=r"N = 0.20 \times 6.02\times 10^{23} = 1.2\times 10^{23}\ \text{molecules}"),
        ], check=r"\frac{1.204\times 10^{23}}{6.02\times 10^{23}} \times 18 = 3.6\ \mathrm{g}"),
        EX("Worked example 2: counting ions", intro=r"How many ions are in 5.85 g of sodium chloride? ($A_r$: Na 23, Cl 35.5)", steps=[
            S("Molar mass of NaCl", math=r"M = 23 + 35.5 = 58.5\ \mathrm{g\,mol^{-1}}"),
            S("Moles of formula units", math=r"n = \frac{5.85}{58.5} = 0.100\ \mathrm{mol}"),
            S(r"Each formula unit gives two ions (one $\mathrm{Na^+}$ and one $\mathrm{Cl^-}$)", math=r"n(\text{ions}) = 2 \times 0.100 = 0.200\ \mathrm{mol}"),
            S("Number of ions", math=r"N = 0.200 \times 6.02\times 10^{23} = 1.20\times 10^{23}"),
        ]),
        EX("Worked example 3: the mass of a single atom", intro=r"Find the mass of one copper atom in grams. ($A_r$ of Cu = 63.5)", steps=[
            S(r"One mole of copper has mass 63.5 g and holds $6.02\times10^{23}$ atoms", math=r"\text{mass of one atom} = \frac{63.5\ \mathrm{g}}{6.02\times 10^{23}}"),
            S("Divide", math=r"= 1.05\times 10^{-22}\ \mathrm{g}"),
        ]),
        MISTAKE("Counting molecules when you need atoms", r"In 0.50 mol of $\mathrm{NH_3}$ there are 0.50 mol of molecules but $0.50 \times 4 = 2.0$ mol of atoms. "
                "Always ask: which particle does the question want, and how many of them are in each formula unit?"),
        MISTAKE("Using mass in kilograms or mixing units", "The molar mass is in g/mol, so the mass must be in grams. If a question gives 0.0036 kg, convert it to 3.6 g first."),
        QUIZ(r"How many oxygen atoms are in 0.25 mol of $\mathrm{CO_2}$?",
             [r"$1.5\times 10^{23}$", r"$3.0\times 10^{23}$", r"$6.02\times 10^{23}$", r"$1.5\times 10^{24}$"], 1,
             r"Each molecule has 2 O atoms, so 0.50 mol of O atoms, and $0.50 \times 6.02\times 10^{23} = 3.0\times 10^{23}$.",
             hint="First find the moles of oxygen atoms, then convert to a number.",
             feedback=[r"This is the number of CO$_2$ molecules ($0.25 \times 6.02\times10^{23}$); you forgot that each molecule has two O atoms.", "",
                       "This is the number in one whole mole of anything, not 0.25 mol of CO2.",
                       "This is ten times too big: the powers of ten were mishandled."]),
        TIP("Mole calculations appear in Paper 1 multiple choice and in Paper 2 structured questions, usually as the first step of a longer problem. Write the particle you are counting next to every number."),
        PQ(r"How many atoms are in 0.250 mol of methane, $\mathrm{CH_4}$?",
           r"Each molecule has 5 atoms (1 C and 4 H). Moles of atoms = $0.250 \times 5 = 1.25$ mol. Number = $1.25 \times 6.02\times10^{23} = 7.53\times 10^{23}$ atoms."),
        PQ(r"What is the mass of $3.01\times10^{23}$ molecules of carbon dioxide? ($A_r$: C 12, O 16)",
           r"$n = \dfrac{3.01\times10^{23}}{6.02\times10^{23}} = 0.500$ mol. $M(\mathrm{CO_2}) = 44$ g/mol. Mass $= 0.500 \times 44 = 22.0$ g."),
        PQ(r"Calculate the number of hydroxide ions in 10.0 g of calcium hydroxide, $\mathrm{Ca(OH)_2}$. ($A_r$: Ca 40, O 16, H 1)",
           r"$M = 40 + 2(17) = 74$ g/mol. $n = 10.0/74 = 0.135$ mol. Each formula unit has 2 $\mathrm{OH^-}$ ions, so $n(\mathrm{OH^-}) = 0.270$ mol. "
           r"Number $= 0.270 \times 6.02\times10^{23} = 1.63\times10^{23}$ ions."),
        PQ(r"Find the mass of one molecule of water in grams.",
           r"$M = 18$ g/mol, so mass of one molecule $= \dfrac{18}{6.02\times10^{23}} = 2.99\times10^{-23}$ g."),
        SUM(r"The mole is the amount of substance containing $6.02\times10^{23}$ particles (the Avogadro constant, $L$).",
            r"$n = m/M$ and $N = nL$: use them to link mass, moles and number of particles.",
            "Always name the particle: atoms, molecules or ions. Use the formula to count how many of each are in one formula unit.",
            "Molar mass is in g/mol and numerically equal to the relative atomic or formula mass."),
    ],
))

# ------------------------------------------------------------------ 2. Ideal gas equation
LESSONS.append(lesson(
    module=M1,
    topic="Avogadro constant and the ideal gas equation",
    title="The ideal gas equation PV = nRT",
    slug="chl1-ideal-gas-equation",
    minutes=24,
    summary="Use PV = nRT with correct SI units to find moles, volume, pressure, temperature and molar mass of gases, and explain why the molar gas volume depends on conditions.",
    objectives=[
        "State the ideal gas equation and the SI units of each term",
        "Convert dm3, cm3, kPa and degrees Celsius into m3, Pa and kelvin",
        "Calculate gas volumes, pressures and molar masses from experimental data",
        "Relate PV = nRT to the molar gas volumes 24 dm3 (rtp) and 22.4 dm3 (stp)",
    ],
    key_concepts=["Ideal gas", "PV = nRT", "Gas constant R", "SI units", "Molar gas volume", "Relative molecular mass from gas data"],
    blocks=[
        H("Introduction"),
        T("A 12.5 kg cooking-gas cylinder in a Yaounde kitchen holds liquid butane under pressure. When the valve opens, the liquid turns to gas and fills "
          "the room's air space at a much lower pressure. How much gas is that, and how does it change on a hot day? The ideal gas equation answers such questions, "
          "and in the laboratory it lets us find the molar mass of an unknown gas by weighing it."),
        H("The equation"),
        T("Experiments show three things for a fixed mass of gas. Volume is inversely proportional to pressure at constant temperature (Boyle). Volume is proportional to the "
          "kelvin temperature at constant pressure (Charles). Equal volumes of gases at the same temperature and pressure contain equal numbers of molecules (Avogadro). "
          "Combining all three gives one equation."),
        D(r"For $n$ moles of an **ideal gas** (one whose particles have negligible volume and no attractions):", title="The ideal gas equation",
          formula=r"PV = nRT",
          note="P pressure in Pa, V volume in m3, n moles, T temperature in K, R = 8.31 J per mole per K."),
        CODE("""Quantity      SI unit       Convert from
pressure P    pascal, Pa    1 kPa = 1000 Pa ; 1 atm = 101 325 Pa
volume V      m3            1 dm3 = 0.001 m3 ; 1 cm3 = 0.000001 m3
temperature   kelvin, K     T(K) = t(deg C) + 273
amount n      mol           n = mass / molar mass
R             8.31 J/(mol K)  (1 J = 1 Pa m3)""", "text", title="Units: convert before you substitute"),
        TIP("Check the units first. Most lost marks come from using dm3 or kPa straight in the equation, or from forgetting to add 273 to the temperature."),
        KEY("Where the molar gas volume comes from", r"At 293 K and 101 325 Pa, one mole occupies $V = \dfrac{nRT}{P} = \dfrac{8.31 \times 293}{101\,325} = 0.0240\ \mathrm{m^3} = 24.0\ \mathrm{dm^3}$ "
            r"(room temperature and pressure, rtp). At 273 K the same pressure gives $22.4\ \mathrm{dm^3}$ (standard temperature and pressure, stp). The molar volume is not a constant of nature: it depends on $T$ and $P$.", cards=[]),
        H("Worked examples"),
        EX("Worked example 1: molar mass of a gas", intro=r"0.200 g of a gas occupies 120 cm$^3$ at 100 kPa and 27 °C. Find its molar mass and suggest what the gas could be.", steps=[
            S("Convert units", math=r"P = 1.00\times10^{5}\ \mathrm{Pa},\quad V = 120\times10^{-6} = 1.20\times10^{-4}\ \mathrm{m^3},\quad T = 300\ \mathrm{K}"),
            S("Moles from the equation", math=r"n = \frac{PV}{RT} = \frac{1.00\times10^{5} \times 1.20\times10^{-4}}{8.31\times 300} = 4.81\times10^{-3}\ \mathrm{mol}"),
            S("Molar mass", math=r"M = \frac{m}{n} = \frac{0.200}{4.81\times10^{-3}} = 41.6\ \mathrm{g\,mol^{-1}}"),
            S("Interpret", text="About 42 g/mol. Propene, C3H6 (M = 42), fits. Other gases could also have this value, so more evidence is needed to be sure."),
        ]),
        EX("Worked example 2: volume of gas produced", intro=r"1.00 g of calcium carbonate reacts with excess dilute hydrochloric acid. What volume of $\mathrm{CO_2}$ is collected at 25 °C and 100 kPa? ($A_r$: Ca 40, C 12, O 16)", steps=[
            S("Equation", math=r"\mathrm{CaCO_3 + 2HCl \rightarrow CaCl_2 + H_2O + CO_2}"),
            S("Moles of CaCO3 (1 : 1 with CO2)", math=r"n = \frac{1.00}{100} = 0.0100\ \mathrm{mol}"),
            S(r"Apply PV = nRT with $T = 298$ K, $P = 1.00\times10^{5}$ Pa", math=r"V = \frac{nRT}{P} = \frac{0.0100 \times 8.31 \times 298}{1.00\times10^{5}} = 2.48\times10^{-4}\ \mathrm{m^3}"),
            S("Convert to cm3", math=r"2.48\times10^{-4}\ \mathrm{m^3} = 248\ \mathrm{cm^3}"),
        ]),
        EX("Worked example 3: molar mass from a density", intro=r"A gas has density 1.80 g/dm$^3$ at 25 °C and 100 kPa. Find its molar mass.", steps=[
            S(r"Use 1 dm3 as the sample: mass 1.80 g, volume $1.00\times10^{-3}\ \mathrm{m^3}$", math=r"n = \frac{PV}{RT} = \frac{1.00\times10^{5}\times 1.00\times10^{-3}}{8.31\times 298} = 0.0404\ \mathrm{mol}"),
            S("Divide mass by moles", math=r"M = \frac{1.80}{0.0404} = 44.6\ \mathrm{g\,mol^{-1}}"),
            S("Interpret", text="About 44.6 g/mol, consistent with CO2 or propane (M = 44) within the accuracy of the data."),
        ]),
        MISTAKE("Using 24 dm3 at any temperature", "24 dm3 is only right at rtp. At 25 °C and 100 kPa one mole occupies 24.8 dm3, and at stp it is 22.4 dm3. If a question gives T and P, use PV = nRT."),
        MISTAKE("Forgetting the kelvin conversion", "A temperature of 27 °C is 300 K, not 27 K. Using the Celsius number makes a volume or moles answer wrong by a factor of about 11."),
        QUIZ(r"Which volume is correct for 0.0100 mol of gas at 27 °C and 200 kPa?",
             [r"$1.25\times10^{-4}\ \mathrm{m^3}$", r"$1.12\times10^{-5}\ \mathrm{m^3}$", r"$0.125\ \mathrm{m^3}$", r"$0.802\ \mathrm{m^3}$"], 0,
             r"Convert first: $T = 300$ K and $P = 2.00\times10^{5}$ Pa. Then $V = nRT/P = (0.0100 \times 8.31 \times 300)/(2.00\times10^{5}) = 1.25\times10^{-4}\ \mathrm{m^3}$, which is 125 cm3.",
             hint="Rearrange to V = nRT/P and keep SI units throughout.",
             feedback=["", "This uses 27 as the temperature, so the Celsius-to-kelvin step was missed.",
                       "The pressure was entered as 200 instead of 200 000: kPa was not converted to Pa.",
                       "This turns the equation upside down (nP/RT), so the volume is far too big."]),
        TIP("Gas-law numerical questions appear in Paper 2 (often with a mass of gas or a displaced volume) and sometimes in Paper 1. Always show the unit conversions line."),
        PQ(r"Calculate the volume of 0.200 mol of an ideal gas at 300 K and 150 kPa. Give the answer in dm$^3$.",
           r"$V = \dfrac{nRT}{P} = \dfrac{0.200 \times 8.31\times 300}{1.50\times10^{5}} = 3.32\times10^{-3}\ \mathrm{m^3} = 3.32\ \mathrm{dm^3}$."),
        PQ(r"A 5.00 dm$^3$ vessel holds argon at 200 kPa and 27 °C. What mass of argon is present? ($A_r$ of Ar = 40)",
           r"$n = \dfrac{PV}{RT} = \dfrac{2.00\times10^{5}\times 5.00\times10^{-3}}{8.31 \times 300} = 0.401$ mol. Mass $= 0.401 \times 40 = 16.0$ g."),
        PQ(r"What is the pressure of 2.00 g of hydrogen gas ($\mathrm{H_2}$) in a 10.0 dm$^3$ container at 25 °C? ($A_r$ of H = 1)",
           r"$n = 2.00/2 = 1.00$ mol. $P = \dfrac{nRT}{V} = \dfrac{1.00 \times 8.31 \times 298}{1.00\times10^{-2}} = 2.48\times10^{5}$ Pa, about 248 kPa."),
        PQ(r"0.150 g of a volatile liquid vaporises completely to give 62.0 cm$^3$ of vapour at 100 °C and 101 kPa. Find the relative molecular mass.",
           r"$T = 373$ K, $V = 6.20\times10^{-5}\ \mathrm{m^3}$, $P = 1.01\times10^{5}$ Pa. $n = \dfrac{PV}{RT} = \dfrac{1.01\times10^{5}\times6.20\times10^{-5}}{8.31\times373} = 2.02\times10^{-3}$ mol. "
           r"$M = 0.150/2.02\times10^{-3} = 74$ g/mol, so $M_r \approx 74$."),
        SUM(r"$PV = nRT$ with $P$ in Pa, $V$ in m$^3$, $T$ in K and $R = 8.31\ \mathrm{J\,mol^{-1}K^{-1}}$.",
            "Convert kPa to Pa, dm3 and cm3 to m3, and degrees Celsius to kelvin before substituting.",
            "To find a molar mass, find moles from PV = nRT and divide the mass by the moles.",
            "24 dm3 per mole holds only at rtp and 22.4 dm3 only at stp; otherwise use the equation."),
    ],
))


# ------------------------------------------------------------------ 3. Formulae from combustion data
LESSONS.append(lesson(
    module=M1,
    topic="Formulae from combustion data",
    title="Empirical and molecular formulae from combustion data",
    slug="chl1-formulae-from-combustion",
    minutes=24,
    summary="Find empirical and molecular formulae from masses of carbon dioxide and water, from percentage composition, and from gas volumes before and after combustion.",
    objectives=[
        "Calculate the masses of C, H and O in a compound from the masses of CO2 and H2O it gives on burning",
        "Turn masses into a mole ratio and then into an empirical formula",
        "Use the relative molecular mass to find the molecular formula",
        "Work out the formula of a hydrocarbon from gas volumes measured before and after combustion",
    ],
    key_concepts=["Empirical formula", "Molecular formula", "Combustion analysis", "Mole ratio", "Gas-volume (eudiometry) analysis"],
    blocks=[
        H("Introduction"),
        T("Suppose a chemist at a petroleum laboratory in Limbe has a new organic liquid and wants to know its formula. She burns a small, weighed sample in "
          "excess oxygen. All the carbon in it turns into carbon dioxide and all the hydrogen into water. By weighing the two products she can work backwards to "
          "the formula. This method, **combustion analysis**, is how many organic formulae were first found."),
        D("The **empirical formula** is the simplest whole-number ratio of the atoms of each element in a compound. The **molecular formula** is the actual number of atoms of each "
          "element in one molecule, and it is a whole-number multiple of the empirical formula.", title="Definitions"),
        KEY("The method in five steps", "Use the same steps every time. Each step has one job.", cards=[
            ["1. Masses of elements", r"C from CO$_2$: $m_{CO_2}\times\dfrac{12}{44}$. H from water: $m_{H_2O}\times\dfrac{2}{18}$. O by difference."],
            ["2. Moles", r"Divide each mass by $A_r$."],
            ["3. Ratio", "Divide all by the smallest number of moles."],
            ["4. Whole numbers", "If a ratio is like 1.5, multiply all by 2 (or by 3 for 1.33)."],
            ["5. Molecular formula", r"Compare the empirical mass with $M_r$: multiplier $= M_r / M_{\text{empirical}}$."],
        ]),
        T("The fractions in step 1 come from the formulae. In 44 g of CO2 there are 12 g of carbon. In 18 g of water there are 2 g of hydrogen. Oxygen in the "
          "compound is found by subtracting carbon and hydrogen from the sample mass, because some of the oxygen in the products came from the air."),
        H("Worked examples"),
        EX("Worked example 1: carbon, hydrogen and oxygen", intro=r"0.580 g of an organic compound containing C, H and O burns completely to give 1.32 g of carbon dioxide and 0.540 g of water. "
           r"Its relative molecular mass is 58. Find the empirical and molecular formulae. ($A_r$: C 12, H 1, O 16)", steps=[
            S("Mass of carbon", math=r"m(\mathrm{C}) = 1.32\times\frac{12}{44} = 0.360\ \mathrm{g}"),
            S("Mass of hydrogen", math=r"m(\mathrm{H}) = 0.540\times\frac{2}{18} = 0.0600\ \mathrm{g}"),
            S("Mass of oxygen by difference", math=r"m(\mathrm{O}) = 0.580 - 0.360 - 0.0600 = 0.160\ \mathrm{g}"),
            S("Moles", math=r"n(\mathrm{C}) = 0.0300,\quad n(\mathrm{H}) = 0.0600,\quad n(\mathrm{O}) = 0.0100"),
            S("Divide by the smallest (0.0100)", math=r"\mathrm{C : H : O} = 3 : 6 : 1 \;\Rightarrow\; \text{empirical formula } \mathrm{C_3H_6O}"),
            S("Compare masses", math=r"M(\mathrm{C_3H_6O}) = 36 + 6 + 16 = 58 = M_r \;\Rightarrow\; \text{molecular formula } \mathrm{C_3H_6O}"),
        ], check=r"\mathrm{C_3H_6O + 4O_2 \rightarrow 3CO_2 + 3H_2O}\ \ (\text{balanced: } 3\,\mathrm{C},\ 6\,\mathrm{H},\ 9\,\mathrm{O} \text{ on each side})"),
        EX("Worked example 2: a hydrocarbon and the multiplier", intro=r"0.350 g of a hydrocarbon gives 1.10 g of $\mathrm{CO_2}$ and 0.450 g of $\mathrm{H_2O}$ on complete combustion. "
           r"A mass spectrum shows its molecular ion at $m/z = 70$. Find the molecular formula.", steps=[
            S("Carbon and hydrogen", math=r"m(\mathrm{C}) = 1.10\times\tfrac{12}{44} = 0.300\ \mathrm{g},\qquad m(\mathrm{H}) = 0.450\times\tfrac{2}{18} = 0.0500\ \mathrm{g}"),
            S("Check there is no oxygen", text="0.300 + 0.0500 = 0.350 g, which equals the sample mass, so the compound is a hydrocarbon."),
            S("Moles", math=r"n(\mathrm{C}) = \frac{0.300}{12} = 0.0250,\qquad n(\mathrm{H}) = \frac{0.0500}{1} = 0.0500"),
            S("Ratio", math=r"\mathrm{C : H} = 1 : 2 \;\Rightarrow\; \text{empirical formula } \mathrm{CH_2}\ (M = 14)"),
            S("Multiplier", math=r"\frac{70}{14} = 5 \;\Rightarrow\; \text{molecular formula } \mathrm{C_5H_{10}}"),
        ]),
        H("Gas volumes: burning a hydrocarbon"),
        T(r"For a gaseous hydrocarbon $\mathrm{C_xH_y}$, volumes of gases measured at the same temperature and pressure are in the same ratio as moles (Avogadro). "
          "The usual experiment mixes the hydrocarbon with excess oxygen, ignites it, then cools the gases to room temperature so that the water condenses to a liquid "
          "and takes up no gas volume. Potassium hydroxide solution then absorbs the carbon dioxide."),
        F(r"\mathrm{C_xH_y} + \left(x + \tfrac{y}{4}\right)\mathrm{O_2} \rightarrow x\,\mathrm{CO_2} + \tfrac{y}{2}\,\mathrm{H_2O(l)}"),
        EX("Worked example 3: from volumes to a formula", intro=r"10.0 cm$^3$ of a gaseous hydrocarbon is mixed with 50.0 cm$^3$ of oxygen (excess) and sparked. After cooling to the starting temperature "
           r"the gas volume is 35.0 cm$^3$. Shaking with potassium hydroxide solution leaves 15.0 cm$^3$. Find the formula.", steps=[
            S("Volume of CO2 is the volume absorbed by KOH", math=r"V(\mathrm{CO_2}) = 35.0 - 15.0 = 20.0\ \mathrm{cm^3}"),
            S("So each volume of hydrocarbon gives 2 volumes of CO2", math=r"x = \frac{20.0}{10.0} = 2"),
            S("Oxygen used = start minus what is left (the 15.0 cm3 is unused oxygen)", math=r"V(\mathrm{O_2}) = 50.0 - 15.0 = 35.0\ \mathrm{cm^3}"),
            S("Oxygen per volume of hydrocarbon", math=r"x + \frac{y}{4} = \frac{35.0}{10.0} = 3.5 \;\Rightarrow\; \frac{y}{4} = 1.5 \;\Rightarrow\; y = 6"),
            S("Formula", math=r"\mathrm{C_2H_6}\quad (\text{ethane})"),
        ], check=r"\mathrm{2C_2H_6 + 7O_2 \rightarrow 4CO_2 + 6H_2O}:\ 10\ \text{cm}^3 \text{ ethane uses } 35\ \text{cm}^3\ \mathrm{O_2} \text{ and forms } 20\ \text{cm}^3\ \mathrm{CO_2}"),
        MISTAKE("Counting oxygen from the air as oxygen in the compound", "The oxygen in CO2 and H2O comes partly from the sample and partly from the oxygen supply. "
                "Find oxygen in the sample by difference (sample mass minus C minus H), never from the products."),
        MISTAKE("Rounding a ratio such as 1.5 down to 1 or up to 2", "A ratio of 1.5 : 1 means multiply everything by 2 to get 3 : 2. A ratio of 1.33 means multiply by 3. Only round when the number is within about 0.05 of a whole number."),
        QUIZ(r"A compound has empirical formula $\mathrm{CH_2O}$ and $M_r = 180$. What is its molecular formula?",
             [r"$\mathrm{CH_2O}$", r"$\mathrm{C_3H_6O_3}$", r"$\mathrm{C_6H_{12}O_6}$", r"$\mathrm{C_{12}H_{24}O_{12}}$"], 2,
             r"The empirical mass is $12 + 2 + 16 = 30$. The multiplier is $180/30 = 6$, so the molecular formula is $\mathrm{C_6H_{12}O_6}$.",
             hint="Find the mass of the empirical formula and divide it into 180.",
             feedback=["This is the empirical formula itself, with M = 30, not 180.", "This is a multiplier of 3 (M = 90), too small.", "",
                       "This is a multiplier of 12 (M = 360); the multiplier is 180/30 = 6."]),
        TIP("Combustion data questions are standard Paper 2 material and often appear in Paper 1 as a quick ratio. Show each mass and each mole ratio in a clear line: the method marks are usually separate from the final formula."),
        PQ(r"1.50 g of a compound of C, H and O gives 2.20 g of $\mathrm{CO_2}$ and 0.900 g of $\mathrm{H_2O}$ on burning. $M_r = 60$. Find the molecular formula.",
           r"C: $2.20\times12/44 = 0.600$ g. H: $0.900\times2/18 = 0.100$ g. O: $1.50 - 0.600 - 0.100 = 0.800$ g. Moles: C 0.0500, H 0.100, O 0.0500. Ratio 1 : 2 : 1, so empirical formula $\mathrm{CH_2O}$ ($M = 30$). "
           r"$60/30 = 2$, so the molecular formula is $\mathrm{C_2H_4O_2}$."),
        PQ(r"20.0 cm$^3$ of a gaseous hydrocarbon is burnt in excess oxygen. After cooling, the volume of gas has decreased by 50.0 cm$^3$ and 40.0 cm$^3$ of carbon dioxide is formed. Find the formula.",
           r"$x = 40.0/20.0 = 2$. The contraction is $V(1 + y/4) = 20.0(1 + y/4) = 50.0$, so $1 + y/4 = 2.5$ and $y = 6$. The formula is $\mathrm{C_2H_6}$. (Check: 20 cm3 of ethane uses 70 cm3 of oxygen and gives 40 cm3 of CO2; "
           r"$20 + 70 - 40 = 50$.)"),
        PQ(r"0.292 g of a compound of C, H and O gives 0.528 g of $\mathrm{CO_2}$ and 0.180 g of $\mathrm{H_2O}$; $M_r = 146$. Find the molecular formula.",
           r"C: $0.528\times12/44 = 0.144$ g. H: $0.180\times2/18 = 0.0200$ g. O: $0.292 - 0.144 - 0.0200 = 0.128$ g. Moles: C 0.0120, H 0.0200, O 0.00800. Dividing by 0.00400: C 3, H 5, O 2. Empirical formula $\mathrm{C_3H_5O_2}$ ($M = 73$). "
           r"$146/73 = 2$, so the molecular formula is $\mathrm{C_6H_{10}O_4}$."),
        PQ(r"A compound contains 40.0% carbon, 6.7% hydrogen and 53.3% oxygen by mass, and has $M_r = 180$. Find the empirical and molecular formulae.",
           r"In 100 g: C 40.0 g (3.33 mol), H 6.7 g (6.7 mol), O 53.3 g (3.33 mol). Dividing by 3.33 gives 1 : 2 : 1, so the empirical formula is $\mathrm{CH_2O}$ ($M = 30$). $180/30 = 6$, so the molecular formula is $\mathrm{C_6H_{12}O_6}$."),
        SUM("Convert the masses of CO2 and H2O into masses of C (×12/44) and H (×2/18); find oxygen by difference.",
            "Divide each mass by Ar, then divide by the smallest number of moles to get the ratio, and clear any fractions.",
            r"The molecular formula is the empirical formula times $M_r / M_{\text{empirical}}$.",
            r"For gas volumes: $V(\mathrm{CO_2})$ gives $x$, and oxygen used gives $x + y/4$, so $y$ follows."),
    ],
))


# ------------------------------------------------------------------ 4. Acid-base titration calculations
LESSONS.append(lesson(
    module=M1,
    topic="Acid-base and back titrations",
    title="Acid-base titrations: method and calculations",
    slug="chl1-acid-base-titrations",
    minutes=25,
    summary="Carry out an acid-base titration with a pipette, burette and indicator, choose the indicator, and calculate concentrations and percentage purity.",
    objectives=[
        "Describe a titration and explain the role of the standard solution, the burette, the pipette and the indicator",
        "Choose between methyl orange and phenolphthalein for a given acid and base",
        "Calculate the concentration of an unknown solution and report concentration in mol/dm3 and g/dm3",
        "Calculate the percentage purity of a solid from titration data",
    ],
    key_concepts=["Titration", "Standard solution", "Primary standard", "Indicator", "End-point", "Concordant titres", "Percentage purity"],
    blocks=[
        H("Introduction"),
        T("A quality-control technician at a drinks company in Douala checks the acid in a batch of concentrated juice by titration. A water-supply laboratory in Bamenda checks "
          "the alkalinity of a borehole sample the same way. A **titration** finds the concentration of an unknown solution by measuring the volume of a solution of known concentration "
          "needed to react exactly with it."),
        IMG("al-chl1-titration-setup.svg", alt="Titration set-up: a clamped burette with tap above a conical flask standing on a white tile",
            caption="Figure 1. The set-up: standard solution in the burette, a measured volume of the other solution and the indicator in the flask."),
        D("A **standard solution** is a solution whose concentration is accurately known. A **primary standard** is a solid pure enough, stable enough and with a high enough molar mass to be "
          "weighed accurately to make a standard solution directly; anhydrous sodium carbonate is one. The **end-point** is the volume at which the indicator changes colour; it should "
          "match the **equivalence point**, where the reactants are in the exact ratio of the equation.", title="Definitions"),
        H("The method"),
        KEY("Good technique", "These details are marked in the practical paper and affect your accuracy.", cards=[
            ["Pipette", "Rinse with the solution it will hold. Fill to the mark at eye level. Let it drain; do not blow out the last drop."],
            ["Burette", "Rinse with the solution it will hold, fill above zero, run some through the tap to remove air, read the bottom of the meniscus."],
            ["Flask", "Rinse with distilled water only. Add 2 or 3 drops of indicator and swirl as you add the solution."],
            ["Titres", "Do a rough run, then repeat until two or more titres agree within 0.10 cm3 (concordant). Average only the concordant ones."],
        ]),
        CODE("""Indicator          Acid colour   Alkali colour   Use with
methyl orange      red           yellow          strong acid + strong or weak base
phenolphthalein    colourless    pink            strong base + strong or weak acid
(no common indicator suits a weak acid with a weak base)""", "text", title="Choosing an indicator"),
        T("The indicator must change colour in the steep part of the pH change at the equivalence point. For a strong acid with a strong base either indicator works. "
          "For a weak acid (such as ethanoic acid) with a strong base the equivalence solution is slightly alkaline, so phenolphthalein is used. For a strong acid with a weak base "
          "(such as sodium carbonate or ammonia) the equivalence solution is slightly acidic, so methyl orange is used. Titration curves are treated in Upper Sixth."),
        H("The calculation"),
        KEY("Four steps", "The same four steps solve every titration.", cards=[
            ["1", "Write the balanced equation."],
            ["2", r"Moles of the known solution: $n = c \times V$ with $V$ in dm$^3$ (cm$^3 \div 1000$)."],
            ["3", "Use the mole ratio from the equation to find moles of the unknown."],
            ["4", r"Concentration of the unknown $= n \div V$. Convert to g/dm$^3$ by multiplying by the molar mass."],
        ]),
        EX("Worked example 1: concentration of an alkali", intro=r"25.0 cm$^3$ portions of sodium hydroxide solution were titrated against 0.100 mol/dm$^3$ hydrochloric acid. "
           r"Titres: rough 23.10, then 22.50, 22.45, 22.55 cm$^3$. Find the concentration of the sodium hydroxide.", steps=[
            S("Choose the concordant titres and average them (the rough value is not used)", math=r"\frac{22.50 + 22.45 + 22.55}{3} = 22.50\ \mathrm{cm^3}"),
            S("Equation", math=r"\mathrm{NaOH + HCl \rightarrow NaCl + H_2O}\quad(1:1)"),
            S("Moles of HCl", math=r"n = 0.100 \times \frac{22.50}{1000} = 2.25\times10^{-3}\ \mathrm{mol}"),
            S("Moles of NaOH in the 25.0 cm3 portion are equal", math=r"n(\mathrm{NaOH}) = 2.25\times10^{-3}\ \mathrm{mol}"),
            S("Concentration", math=r"c = \frac{2.25\times10^{-3}}{0.0250} = 0.0900\ \mathrm{mol\,dm^{-3}}"),
        ], check=r"0.0900 \times 25.0 = 2.25 = 0.100 \times 22.50"),
        EX("Worked example 2: a 1 : 2 reaction, and g/dm3", intro=r"25.0 cm$^3$ of dilute sulfuric acid is neutralised by 22.40 cm$^3$ of 0.100 mol/dm$^3$ sodium hydroxide. Find the concentration of the acid in mol/dm$^3$ and in g/dm$^3$. ($A_r$: H 1, S 32, O 16)", steps=[
            S("Equation", math=r"\mathrm{H_2SO_4 + 2NaOH \rightarrow Na_2SO_4 + 2H_2O}\quad(1:2)"),
            S("Moles of NaOH", math=r"n = 0.100\times\frac{22.40}{1000} = 2.24\times10^{-3}\ \mathrm{mol}"),
            S("Moles of acid are half of that", math=r"n(\mathrm{H_2SO_4}) = 1.12\times10^{-3}\ \mathrm{mol}"),
            S("Concentration", math=r"c = \frac{1.12\times10^{-3}}{0.0250} = 0.0448\ \mathrm{mol\,dm^{-3}}"),
            S("Mass concentration ($M = 98$)", math=r"0.0448\times98 = 4.39\ \mathrm{g\,dm^{-3}}"),
        ]),
        EX("Worked example 3: percentage purity", intro=r"1.40 g of impure sodium carbonate was dissolved and made up to 250 cm$^3$. 25.0 cm$^3$ portions needed 24.0 cm$^3$ of 0.100 mol/dm$^3$ hydrochloric acid "
           r"(methyl orange indicator). Find the percentage of $\mathrm{Na_2CO_3}$ in the sample. ($A_r$: Na 23, C 12, O 16)", steps=[
            S("Equation", math=r"\mathrm{Na_2CO_3 + 2HCl \rightarrow 2NaCl + H_2O + CO_2}\quad(1:2)"),
            S("Moles of HCl", math=r"n = 0.100\times0.0240 = 2.40\times10^{-3}\ \mathrm{mol}"),
            S("Moles of Na2CO3 in 25.0 cm3", math=r"\frac{2.40\times10^{-3}}{2} = 1.20\times10^{-3}\ \mathrm{mol}"),
            S("Scale up to 250 cm3 (ten times)", math=r"1.20\times10^{-2}\ \mathrm{mol}"),
            S("Mass of Na2CO3 ($M = 106$)", math=r"1.20\times10^{-2}\times106 = 1.272\ \mathrm{g}"),
            S("Percentage purity", math=r"\frac{1.272}{1.40}\times100 = 90.9\%"),
        ]),
        MISTAKE("Forgetting the scale-up from the aliquot", "If you titrate 25.0 cm3 taken from a 250 cm3 solution, your answer is for the 25.0 cm3 only. Multiply by 10 to get the moles in the whole solution."),
        MISTAKE("Using the rough titre or averaging non-concordant values", "Average only titres within 0.10 cm3 of each other. A rough titre is a trial to find the approximate end-point and is not part of the mean."),
        QUIZ("Which indicator is best for titrating ethanoic acid (a weak acid) with sodium hydroxide solution?",
             ["Methyl orange, because it changes from red to yellow", "Phenolphthalein, because the equivalence point is slightly alkaline", "Either, because all acid-base indicators work for all titrations", "Neither, because ethanoic acid is too weak to titrate"], 1,
             "At the equivalence point sodium ethanoate is present, which hydrolyses to give a slightly alkaline solution (pH above 7). Phenolphthalein changes colour in that range.",
             hint="Think about the pH of the salt formed at the equivalence point.",
             feedback=["Methyl orange changes colour on the acid side (around pH 3 to 4.5), well before the equivalence point of this titration.", "",
                       "Indicators have different colour-change ranges, so the choice matters for weak-acid or weak-base titrations.",
                       "Weak acids can be titrated with a strong base; only weak acid with weak base is unsuitable."]),
        TIP("Titration calculations are set every year in the practical paper and as structured questions in Paper 2. Quote titres to 0.05 cm3 (two decimal places), give concordant results, and write the unit of concentration in your answer."),
        PQ(r"25.0 cm$^3$ of 0.0800 mol/dm$^3$ sodium hydroxide needs 20.0 cm$^3$ of hydrochloric acid for neutralisation. Calculate the concentration of the acid.",
           r"$n(\mathrm{NaOH}) = 0.0800\times0.0250 = 2.00\times10^{-3}$ mol. The ratio is 1 : 1, so $n(\mathrm{HCl}) = 2.00\times10^{-3}$ mol. $c = 2.00\times10^{-3}/0.0200 = 0.100$ mol/dm$^3$."),
        PQ(r"10.0 cm$^3$ of vinegar was diluted to 250 cm$^3$. 25.0 cm$^3$ of the diluted solution needed 10.0 cm$^3$ of 0.100 mol/dm$^3$ NaOH. "
           r"Find the concentration of ethanoic acid in the vinegar in g/dm$^3$. ($\mathrm{CH_3COOH + NaOH \rightarrow CH_3COONa + H_2O}$; $M = 60$)",
           r"$n(\mathrm{NaOH}) = 0.100\times0.0100 = 1.00\times10^{-3}$ mol, so 1.00 × 10$^{-3}$ mol of acid in 25.0 cm$^3$. In 250 cm$^3$: $1.00\times10^{-2}$ mol, which came from 10.0 cm$^3$ of vinegar. "
           r"$c = 1.00\times10^{-2}/0.0100 = 1.00$ mol/dm$^3$. Mass concentration $= 1.00\times60 = 60$ g/dm$^3$."),
        PQ(r"3.00 g of washing soda crystals, $\mathrm{Na_2CO_3\cdot xH_2O}$, were dissolved to make 250 cm$^3$ of solution. 25.0 cm$^3$ needed 20.98 cm$^3$ of 0.100 mol/dm$^3$ HCl. Find $x$. ($A_r$: Na 23, C 12, O 16, H 1)",
           r"$n(\mathrm{HCl}) = 0.100\times0.02098 = 2.098\times10^{-3}$ mol. $n(\mathrm{Na_2CO_3}) = 1.049\times10^{-3}$ mol in 25.0 cm$^3$, so $1.049\times10^{-2}$ mol in 250 cm$^3$. "
           r"$M = 3.00/1.049\times10^{-2} = 286$ g/mol. $M(\mathrm{Na_2CO_3}) = 106$, so $18x = 286 - 106 = 180$ and $x = 10$."),
        PQ(r"What volume of 0.100 mol/dm$^3$ hydrochloric acid is needed to neutralise 25.0 cm$^3$ of 0.0500 mol/dm$^3$ barium hydroxide, $\mathrm{Ba(OH)_2}$?",
           r"$\mathrm{Ba(OH)_2 + 2HCl \rightarrow BaCl_2 + 2H_2O}$. $n(\mathrm{Ba(OH)_2}) = 0.0500\times0.0250 = 1.25\times10^{-3}$ mol, so $n(\mathrm{HCl}) = 2.50\times10^{-3}$ mol. "
           r"$V = 2.50\times10^{-3}/0.100 = 0.0250$ dm$^3 = 25.0$ cm$^3$."),
        SUM("A titration finds an unknown concentration from the volume of a standard solution that reacts exactly with it.",
            "Use pipette, burette, indicator and white tile carefully; average only concordant titres (within 0.10 cm3).",
            "Four steps: balanced equation, moles of the known, mole ratio, concentration of the unknown (and scale up any aliquot).",
            "Methyl orange suits strong acid with weak base; phenolphthalein suits weak acid with strong base."),
    ],
))


# ------------------------------------------------------------------ 5. Back titrations
LESSONS.append(lesson(
    module=M1,
    topic="Acid-base and back titrations",
    title="Back titrations",
    slug="chl1-back-titrations",
    minutes=24,
    summary="Use a back titration when a substance is insoluble or reacts slowly: add a known excess of reagent, titrate what is left, and subtract to find what reacted.",
    objectives=[
        "Explain when and why a back titration is used instead of a direct titration",
        "Describe the steps of a back titration",
        "Calculate the amount of a substance from the excess reagent measured by titration",
        "Apply the method to limestone, antacid tablets and ammonium salts",
    ],
    key_concepts=["Back titration", "Excess reagent", "Moles that reacted", "Percentage composition from titration"],
    blocks=[
        H("Introduction"),
        T("Calcium carbonate in limestone and in eggshell does not dissolve in water. You cannot pipette a solution of it, and it reacts with acid too slowly for a sharp end-point if you add acid "
          "drop by drop from a burette. The same problem arises with antacid tablets and with ammonium salts in fertiliser. A **back titration** solves it by adding a known amount of reagent in excess, "
          "letting it react completely, and then titrating the **leftover** reagent."),
        IMG("al-chl1-back-titration-flow.svg", alt="Flow chart: sample plus known excess reagent, reaction, leftover reagent titrated with a standard solution",
            caption="Figure 1. A back titration measures what is left over, then subtracts."),
        D("In a **back titration** a known excess of one reagent is added to the sample; after the reaction is complete, the unreacted excess is found by titration. "
          "The amount that reacted with the sample is the amount added minus the amount left over.", title="Definition: back titration"),
        KEY("When to use a back titration", "Any one of these is a good reason.", cards=[
            ["Insoluble solid", "The sample cannot be dissolved, so it cannot go in the flask as a solution (CaCO3 in limestone)."],
            ["Slow reaction", "The reaction takes time, so the direct end-point is not sharp."],
            ["Volatile product or reagent", "Gas is lost or the end-point is hard to see (ammonia from an ammonium salt)."],
            ["No suitable indicator", "A direct titration has no clear colour change, but the excess can be titrated cleanly."],
        ]),
        KEY("The calculation in four lines", "Always write these four quantities.", cards=[
            ["A", "Moles of reagent added (known concentration times volume)."],
            ["B", "Moles of reagent left over (from the titration, using the second equation)."],
            ["C", "Moles that reacted with the sample = A minus B."],
            ["D", "Use the first equation to turn C into moles of the sample, then mass and percentage."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: calcium carbonate in limestone", intro=r"0.500 g of limestone was warmed with 50.0 cm$^3$ of 0.200 mol/dm$^3$ hydrochloric acid (excess). The mixture was filtered into a flask and the excess acid "
           r"needed 24.0 cm$^3$ of 0.100 mol/dm$^3$ sodium hydroxide. Find the percentage of $\mathrm{CaCO_3}$. ($A_r$: Ca 40, C 12, O 16)", steps=[
            S("Equations", math=r"\mathrm{CaCO_3 + 2HCl \rightarrow CaCl_2 + H_2O + CO_2}\qquad \mathrm{HCl + NaOH \rightarrow NaCl + H_2O}"),
            S("A: moles of HCl added", math=r"0.200\times0.0500 = 1.00\times10^{-2}\ \mathrm{mol}"),
            S("B: moles of HCl left over (equal to moles of NaOH)", math=r"0.100\times0.0240 = 2.40\times10^{-3}\ \mathrm{mol}"),
            S("C: moles of HCl that reacted", math=r"1.00\times10^{-2} - 2.40\times10^{-3} = 7.60\times10^{-3}\ \mathrm{mol}"),
            S("D: moles of CaCO3 (2 HCl per CaCO3)", math=r"\frac{7.60\times10^{-3}}{2} = 3.80\times10^{-3}\ \mathrm{mol}"),
            S("Mass and percentage ($M = 100$)", math=r"3.80\times10^{-3}\times100 = 0.380\ \mathrm{g}\;\Rightarrow\;\frac{0.380}{0.500}\times100 = 76.0\%"),
        ]),
        EX("Worked example 2: an antacid tablet", intro=r"One antacid tablet of mass 1.25 g containing magnesium hydroxide was added to 50.0 cm$^3$ of 0.500 mol/dm$^3$ hydrochloric acid. The excess acid needed 30.0 cm$^3$ of 0.250 mol/dm$^3$ NaOH. "
           r"Find the percentage of $\mathrm{Mg(OH)_2}$ by mass in the tablet, assuming no other substance in the tablet reacts. ($A_r$: Mg 24, O 16, H 1)", steps=[
            S("Equation", math=r"\mathrm{Mg(OH)_2 + 2HCl \rightarrow MgCl_2 + 2H_2O}"),
            S("A: HCl added", math=r"0.500\times0.0500 = 2.50\times10^{-2}\ \mathrm{mol}"),
            S("B: HCl left over", math=r"0.250\times0.0300 = 7.50\times10^{-3}\ \mathrm{mol}"),
            S("C: HCl that reacted", math=r"2.50\times10^{-2} - 7.50\times10^{-3} = 1.75\times10^{-2}\ \mathrm{mol}"),
            S("D: moles of Mg(OH)2", math=r"\frac{1.75\times10^{-2}}{2} = 8.75\times10^{-3}\ \mathrm{mol}"),
            S("Mass and percentage ($M = 58$)", math=r"8.75\times10^{-3}\times58 = 0.5075\ \mathrm{g}\;\Rightarrow\;\frac{0.5075}{1.25}\times100 = 40.6\%"),
        ]),
        EX("Worked example 3: ammonium sulfate in a fertiliser", intro=r"1.00 g of a fertiliser containing ammonium sulfate was boiled with 50.0 cm$^3$ of 0.500 mol/dm$^3$ NaOH until all the ammonia had escaped. "
           r"The remaining NaOH needed 28.0 cm$^3$ of 0.500 mol/dm$^3$ HCl. Find the percentage of $\mathrm{(NH_4)_2SO_4}$. ($A_r$: N 14, H 1, S 32, O 16)", steps=[
            S("Equation for the ammonium salt", math=r"\mathrm{(NH_4)_2SO_4 + 2NaOH \rightarrow Na_2SO_4 + 2NH_3 + 2H_2O}"),
            S("A: NaOH added", math=r"0.500\times0.0500 = 2.50\times10^{-2}\ \mathrm{mol}"),
            S("B: NaOH left over (equal to moles of HCl)", math=r"0.500\times0.0280 = 1.40\times10^{-2}\ \mathrm{mol}"),
            S("C: NaOH that reacted", math=r"2.50\times10^{-2} - 1.40\times10^{-2} = 1.10\times10^{-2}\ \mathrm{mol}"),
            S("D: moles of ammonium sulfate (2 NaOH each)", math=r"\frac{1.10\times10^{-2}}{2} = 5.50\times10^{-3}\ \mathrm{mol}"),
            S("Mass and percentage ($M = 132$)", math=r"5.50\times10^{-3}\times132 = 0.726\ \mathrm{g}\;\Rightarrow\;72.6\%"),
        ]),
        MISTAKE("Using the leftover as the answer", "The titre tells you how much reagent was left over, not how much reacted with your sample. Subtract it from the amount you added first."),
        MISTAKE("Using the wrong mole ratio at each stage", "Two different equations are involved: one between the sample and the excess reagent, and one between the excess reagent and the titrant. Write both equations and use each one only for its own step."),
        QUIZ("In a back titration, 10.0 mmol of acid was added to a sample and 3.0 mmol was found left over. How much acid reacted with the sample?",
             ["3.0 mmol", "7.0 mmol", "10.0 mmol", "13.0 mmol"], 1,
             "Acid that reacted = acid added minus acid left over = 10.0 - 3.0 = 7.0 mmol.",
             hint="What was used up is what was added minus what remains.",
             feedback=["This is the amount left over, which the titration measured directly. It did not react.", "",
                       "This is all the acid that was added, before subtracting the leftover.", "Adding the two gives a number larger than what was put in."]),
        TIP("Back titrations are a favourite for Paper 2 structured questions on percentage composition, and the Paper 3 practical may include a limestone or antacid analysis. Write 'A, B, C, D' lines to keep the logic visible to the examiner."),
        PQ(r"0.800 g of impure calcium carbonate was heated with 40.0 cm$^3$ of 0.500 mol/dm$^3$ HCl. The excess acid needed 18.0 cm$^3$ of 0.250 mol/dm$^3$ NaOH. Find the percentage of $\mathrm{CaCO_3}$.",
           r"A: $0.500\times0.0400 = 2.00\times10^{-2}$ mol HCl. B: $0.250\times0.0180 = 4.50\times10^{-3}$ mol. C: $2.00\times10^{-2} - 4.50\times10^{-3} = 1.55\times10^{-2}$ mol. "
           r"D: $\mathrm{CaCO_3}$ = $1.55\times10^{-2}/2 = 7.75\times10^{-3}$ mol; mass $= 0.775$ g; percentage $= 0.775/0.800\times100 = 96.9\%$."),
        PQ(r"1.00 g of powdered eggshell was added to 50.0 cm$^3$ of 0.400 mol/dm$^3$ HCl. The excess acid needed 15.0 cm$^3$ of 0.200 mol/dm$^3$ NaOH. Find the percentage of $\mathrm{CaCO_3}$ in the eggshell.",
           r"A: $0.400\times0.0500 = 2.00\times10^{-2}$ mol. B: $0.200\times0.0150 = 3.00\times10^{-3}$ mol. C: $1.70\times10^{-2}$ mol. D: $\mathrm{CaCO_3}$ $= 8.50\times10^{-3}$ mol, mass $0.850$ g, so $85.0\%$."),
        PQ(r"2.00 g of impure ammonium chloride was boiled with 40.0 cm$^3$ of 1.00 mol/dm$^3$ NaOH. The excess NaOH needed 12.0 cm$^3$ of 1.00 mol/dm$^3$ HCl. Find the percentage of $\mathrm{NH_4Cl}$. ($A_r$: N 14, H 1, Cl 35.5)",
           r"$\mathrm{NH_4Cl + NaOH \rightarrow NaCl + NH_3 + H_2O}$ (1 : 1). NaOH added $= 4.00\times10^{-2}$ mol; left $= 1.20\times10^{-2}$ mol; reacted $= 2.80\times10^{-2}$ mol $= n(\mathrm{NH_4Cl})$. "
           r"Mass $= 2.80\times10^{-2}\times53.5 = 1.498$ g. Percentage $= 1.498/2.00\times100 = 74.9\%$."),
        PQ("A student wants the percentage of calcium carbonate in a lump of chalk. Explain why a direct titration is unsuitable and a back titration is used.",
           "Chalk (calcium carbonate) is insoluble in water, so it cannot be pipetted as a solution, and it reacts slowly with acid so a burette end-point would not be sharp. "
           "In a back titration a known excess of acid is added, the reaction is allowed to finish, and the leftover acid is titrated with standard alkali. The acid that reacted is the acid added minus the leftover."),
        SUM("A back titration adds a known excess of reagent, then titrates what is left over.",
            "Moles that reacted = moles added minus moles left over. Use each equation for its own step.",
            "Use it for insoluble solids, slow reactions, and volatile products such as ammonia.",
            "Finish by converting to moles of the sample, then mass, then percentage."),
    ],
))


# ------------------------------------------------------------------ 6. Redox titrations: manganate(VII)
LESSONS.append(lesson(
    module=M1,
    topic="Redox titrations",
    title="Redox titrations with potassium manganate(VII)",
    slug="chl1-redox-titration-manganate",
    minutes=25,
    summary="Build half-equations for manganate(VII) with iron(II), ethanedioate and hydrogen peroxide, and use the mole ratios to analyse iron tablets and peroxide solutions.",
    objectives=[
        "Write and combine half-equations for manganate(VII) reduced in acid solution",
        "Explain why dilute sulfuric acid is used and why no indicator is needed",
        "Use the 1:5, 2:5 and 2:5 mole ratios to find concentrations and percentage purity",
        "Report burette readings and end-points for a dark solution correctly",
    ],
    key_concepts=["Oxidation and reduction", "Oxidation number", "Half-equation", "Manganate(VII)", "Self-indicator", "Mole ratio in redox titrations"],
    blocks=[
        H("Introduction"),
        T("Iron tablets sold in pharmacies in Yaounde and Garoua contain iron(II) sulfate, because the body absorbs iron(II) well. How much iron(II) is really in a tablet? "
          "Potassium manganate(VII), KMnO4, answers the question: it oxidises iron(II) to iron(III), and the dark purple of its solution gives its own end-point. "
          "This is a **redox titration**."),
        D("**Oxidation** is loss of electrons (oxidation number increases); **reduction** is gain of electrons (oxidation number decreases). "
          "An **oxidising agent** is reduced and a **reducing agent** is oxidised. In a redox equation the electrons lost equal the electrons gained.", title="Definitions: redox"),
        H("Building the equation from half-equations"),
        T(r"In acid solution the purple $\mathrm{MnO_4^-}$ ion (Mn has oxidation number +7) is reduced to almost colourless $\mathrm{Mn^{2+}}$ (+2): five electrons are gained by each Mn."),
        F(r"\mathrm{MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O}"),
        F(r"\mathrm{Fe^{2+} \rightarrow Fe^{3+} + e^-}"),
        T("To combine them, multiply the iron half-equation by 5 so that the electrons cancel, then add."),
        F(r"\mathrm{MnO_4^- + 5Fe^{2+} + 8H^+ \rightarrow Mn^{2+} + 5Fe^{3+} + 4H_2O}"),
        CODE("""Reducing agent          Half-equation                         Ratio MnO4- : reductant
Fe2+                    Fe2+ -> Fe3+ + e-                      1 : 5
C2O4 2- (ethanedioate)  C2O4 2- -> 2CO2 + 2e-                   2 : 5
H2O2                    H2O2 -> O2 + 2H+ + 2e-                  2 : 5""", "text", title="Three reducing agents to know"),
        KEY("Practical points", "These are examined in Paper 3 and in structured questions.", cards=[
            ["Acid", "Dilute sulfuric acid is added to the flask. Hydrochloric acid is not used because manganate(VII) would oxidise chloride ions to chlorine. Nitric acid is not used because it is itself an oxidising agent."],
            ["No indicator", "Manganate(VII) is its own indicator: the purple decolourises as it reacts; the first permanent pale pink in the flask marks the end-point."],
            ["Burette reading", "The solution is so dark that the bottom of the meniscus is hard to see. Read the top of the meniscus, and do so each time."],
            ["Ethanedioate", "Reacts slowly when cold. Warm to about 60 degrees Celsius; the Mn2+ formed then acts as a catalyst."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: iron(II) concentration", intro=r"25.0 cm$^3$ of an iron(II) sulfate solution, acidified, needed 21.40 cm$^3$ of 0.0200 mol/dm$^3$ $\mathrm{KMnO_4}$. Find the concentration of $\mathrm{Fe^{2+}}$.", steps=[
            S("Moles of manganate(VII)", math=r"n(\mathrm{MnO_4^-}) = 0.0200\times0.02140 = 4.28\times10^{-4}\ \mathrm{mol}"),
            S("Ratio 1 : 5", math=r"n(\mathrm{Fe^{2+}}) = 5\times4.28\times10^{-4} = 2.14\times10^{-3}\ \mathrm{mol}"),
            S("Concentration", math=r"c = \frac{2.14\times10^{-3}}{0.0250} = 0.0856\ \mathrm{mol\,dm^{-3}}"),
        ]),
        EX("Worked example 2: purity of iron tablets", intro=r"3.00 g of crushed iron tablets (containing $\mathrm{FeSO_4\cdot7H_2O}$) was dissolved in dilute sulfuric acid and made up to 250 cm$^3$. 25.0 cm$^3$ portions needed 19.40 cm$^3$ of 0.0100 mol/dm$^3$ "
           r"$\mathrm{KMnO_4}$. Find the percentage of $\mathrm{FeSO_4\cdot7H_2O}$ in the sample. ($A_r$: Fe 56, S 32, O 16, H 1; $M = 278$)", steps=[
            S("Moles of MnO4-", math=r"0.0100\times0.01940 = 1.94\times10^{-4}\ \mathrm{mol}"),
            S("Moles of Fe2+ in 25.0 cm3", math=r"5\times1.94\times10^{-4} = 9.70\times10^{-4}\ \mathrm{mol}"),
            S("Moles in 250 cm3", math=r"9.70\times10^{-3}\ \mathrm{mol}"),
            S("Mass of hydrated salt", math=r"9.70\times10^{-3}\times278 = 2.70\ \mathrm{g}"),
            S("Percentage purity", math=r"\frac{2.70}{3.00}\times100 = 89.9\%"),
        ]),
        EX("Worked example 3: hydrogen peroxide", intro=r"10.0 cm$^3$ of hydrogen peroxide solution was diluted to 250 cm$^3$. 25.0 cm$^3$ of the dilute solution, acidified, needed 20.00 cm$^3$ of 0.0200 mol/dm$^3$ $\mathrm{KMnO_4}$. "
           r"Find the concentration of the original solution.", steps=[
            S(r"Equation (from the half-equations $\mathrm{MnO_4^-}$ ×2 and $\mathrm{H_2O_2}$ ×5)", math=r"\mathrm{2MnO_4^- + 5H_2O_2 + 6H^+ \rightarrow 2Mn^{2+} + 5O_2 + 8H_2O}"),
            S("Moles of MnO4-", math=r"0.0200\times0.02000 = 4.00\times10^{-4}\ \mathrm{mol}"),
            S("Ratio 2 : 5", math=r"n(\mathrm{H_2O_2}) = 4.00\times10^{-4}\times\frac{5}{2} = 1.00\times10^{-3}\ \mathrm{mol\ in\ 25.0\ cm^3}"),
            S("In the 250 cm3 of diluted solution", math=r"1.00\times10^{-2}\ \mathrm{mol}"),
            S("This came from 10.0 cm3 of the original", math=r"c = \frac{1.00\times10^{-2}}{0.0100} = 1.00\ \mathrm{mol\,dm^{-3}}"),
        ]),
        MISTAKE("Using a 1 : 1 ratio", "Never assume 1 : 1 for a redox titration. The ratio comes from balancing the electrons: 1 MnO4- takes 5 electrons, so it reacts with 5 Fe2+, each of which gives 1 electron."),
        MISTAKE("Acidifying with hydrochloric acid", "Chloride ions are oxidised by manganate(VII), so some of the titrant is used up on the acid and the titre is too big. Use dilute sulfuric acid."),
        QUIZ(r"In the reaction between $\mathrm{MnO_4^-}$ and $\mathrm{Fe^{2+}}$, how many moles of $\mathrm{Fe^{2+}}$ react with 0.0010 mol of $\mathrm{MnO_4^-}$?",
             ["0.0010 mol", "0.0020 mol", "0.0050 mol", "0.0250 mol"], 2,
             r"Each $\mathrm{MnO_4^-}$ accepts 5 electrons and each $\mathrm{Fe^{2+}}$ gives 1, so the ratio is 1 : 5 and $5 \times 0.0010 = 0.0050$ mol.",
             hint="Count the electrons gained by one MnO4- and lost by one Fe2+.",
             feedback=["This assumes a 1 : 1 ratio, which ignores the five electrons Mn gains.", "This uses a ratio of 1 : 2, which does not balance the electrons.", "",
                       "This multiplies by 25, which is not a ratio in the equation."]),
        TIP("Redox titrations appear in Paper 2 and in the practical Paper 3. Examiners expect the full ionic equation or the stated mole ratio, and the end-point colour: first permanent pale pink."),
        PQ(r"25.0 cm$^3$ of 0.0500 mol/dm$^3$ sodium ethanedioate, $\mathrm{Na_2C_2O_4}$, is warmed with dilute sulfuric acid and titrated with 0.0200 mol/dm$^3$ $\mathrm{KMnO_4}$. What titre is expected?",
           r"$n(\mathrm{C_2O_4^{2-}}) = 0.0500\times0.0250 = 1.25\times10^{-3}$ mol. Ratio $\mathrm{MnO_4^-} : \mathrm{C_2O_4^{2-}} = 2 : 5$, so $n(\mathrm{MnO_4^-}) = 1.25\times10^{-3}\times2/5 = 5.00\times10^{-4}$ mol. "
           r"Volume $= 5.00\times10^{-4}/0.0200 = 0.0250$ dm$^3 = 25.0$ cm$^3$."),
        PQ(r"1.00 g of iron wire was dissolved in dilute sulfuric acid to give $\mathrm{Fe^{2+}}$ and made up to 100 cm$^3$. 10.0 cm$^3$ portions needed 17.0 cm$^3$ of 0.0200 mol/dm$^3$ $\mathrm{KMnO_4}$. Find the percentage of iron in the wire. ($A_r$ of Fe = 56)",
           r"$n(\mathrm{MnO_4^-}) = 0.0200\times0.0170 = 3.40\times10^{-4}$ mol. $n(\mathrm{Fe^{2+}})$ in 10.0 cm$^3$ $= 5\times3.40\times10^{-4} = 1.70\times10^{-3}$ mol; in 100 cm$^3$: $1.70\times10^{-2}$ mol. "
           r"Mass $= 1.70\times10^{-2}\times56 = 0.952$ g. Percentage $= 95.2\%$."),
        PQ(r"Write the two half-equations and the overall ionic equation for the oxidation of ethanedioate ions, $\mathrm{C_2O_4^{2-}}$, to carbon dioxide by acidified manganate(VII) ions.",
           r"Reduction: $\mathrm{MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O}$. Oxidation: $\mathrm{C_2O_4^{2-} \rightarrow 2CO_2 + 2e^-}$. Multiply the first by 2 and the second by 5 (10 electrons each), then add: "
           r"$\mathrm{2MnO_4^- + 5C_2O_4^{2-} + 16H^+ \rightarrow 2Mn^{2+} + 10CO_2 + 8H_2O}$."),
        PQ(r"25.0 cm$^3$ of a solution containing $\mathrm{Fe^{2+}}$ and $\mathrm{Fe^{3+}}$ needed 20.00 cm$^3$ of 0.0200 mol/dm$^3$ $\mathrm{KMnO_4}$. A second 25.0 cm$^3$ portion was treated with zinc to reduce all the $\mathrm{Fe^{3+}}$ to $\mathrm{Fe^{2+}}$, and then needed 30.00 cm$^3$ of the same $\mathrm{KMnO_4}$. Find the concentration of each ion.",
           r"First portion (Fe$^{2+}$ only): $n = 5\times0.0200\times0.02000 = 2.00\times10^{-3}$ mol, so $c(\mathrm{Fe^{2+}}) = 2.00\times10^{-3}/0.0250 = 0.0800$ mol/dm$^3$. "
           r"Second portion (total iron): $n = 5\times0.0200\times0.03000 = 3.00\times10^{-3}$ mol, so $c(\text{total}) = 0.120$ mol/dm$^3$. $c(\mathrm{Fe^{3+}}) = 0.120 - 0.0800 = 0.0400$ mol/dm$^3$."),
        SUM(r"In acid: $\mathrm{MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O}$; build the full equation by balancing electrons.",
            r"Mole ratios $\mathrm{MnO_4^-}$ : $\mathrm{Fe^{2+}}$ = 1 : 5, : $\mathrm{C_2O_4^{2-}}$ = 2 : 5, : $\mathrm{H_2O_2}$ = 2 : 5.",
            "Use dilute sulfuric acid; manganate(VII) is its own indicator (first permanent pale pink); read the top of the meniscus.",
            "Scale up from the aliquot and convert moles to mass or percentage as the question asks."),
    ],
))


# ------------------------------------------------------------------ 7. Iodometric titrations
LESSONS.append(lesson(
    module=M1,
    topic="Redox titrations",
    title="Iodine and thiosulfate (iodometric) titrations",
    slug="chl1-redox-titration-iodometric",
    minutes=24,
    summary="Find copper(II) and hypochlorite (bleach) by adding excess iodide, then titrating the iodine released with sodium thiosulfate using starch near the end-point.",
    objectives=[
        "Explain how excess iodide converts an oxidising agent into an equivalent amount of iodine",
        "Write the equations for iodine with thiosulfate, copper(II) with iodide, and hypochlorite with iodide",
        "Use the mole chain oxidant to iodine to thiosulfate in calculations",
        "Describe when and why starch is added and what the end-point colour change is",
    ],
    key_concepts=["Iodometric titration", "Thiosulfate", "Starch indicator", "Mole chain", "Oxidation number of sulfur in S4O6 2-"],
    blocks=[
        H("Introduction"),
        T("Household bleach is sold in many Cameroonian towns in unlabelled bottles, and the amount of active chlorine in it varies. Many oxidising agents, such as copper(II) ions and hypochlorite "
          "in bleach, cannot be titrated directly. But each one oxidises iodide ions to iodine, and the iodine can be titrated with sodium thiosulfate. This is an **iodometric titration**: "
          "you measure the oxidising agent by the iodine it releases."),
        KEY("The two-stage idea", "Always two reactions, one chain of moles.", cards=[
            ["Stage 1", "Add excess acidified potassium iodide to the oxidising agent. It releases iodine, I2, in an amount equivalent to the oxidising agent."],
            ["Stage 2", r"Titrate the iodine with sodium thiosulfate solution: $\mathrm{I_2 + 2S_2O_3^{2-} \rightarrow 2I^- + S_4O_6^{2-}}$ (1 : 2)."],
        ]),
        F(r"\mathrm{I_2 + 2S_2O_3^{2-} \rightarrow 2I^- + S_4O_6^{2-}}"),
        T("Thiosulfate is a reducing agent: each sulfur goes from +2 in thiosulfate to +2.5 on average in tetrathionate, and iodine goes from 0 to -1. "
          "The iodine solution is brown. As thiosulfate is added the brown fades to pale yellow. At that stage add a few drops of **starch**: a deep blue-black starch-iodine complex forms. "
          "Continue until the blue colour disappears completely (end-point: blue to colourless). Starch is added late because it would hold on to iodine if added when there is a lot of iodine."),
        CODE("""Oxidising agent     Reaction with excess iodide                Chain (moles)
Cu2+                2Cu2+ + 4I- -> 2CuI + I2                   2 Cu2+ -> 1 I2 -> 2 S2O3 2-   so Cu2+ : S2O3 2- = 1 : 1
OCl- (bleach)       OCl- + 2I- + 2H+ -> Cl- + I2 + H2O         1 OCl- -> 1 I2 -> 2 S2O3 2-   so OCl- : S2O3 2- = 1 : 2
MnO4- / Cr2O7 2-    similar, in acid                            (taught with other redox systems)""", "text", title="Chains to learn"),
        TIP("In the copper reaction a cream-white precipitate of copper(I) iodide forms. It can hide the end-point colour; the colour changes from blue-black to cream. Always note the change you actually see."),
        H("Worked examples"),
        EX("Worked example 1: copper(II) solution", intro=r"Excess potassium iodide was added to 25.0 cm$^3$ of copper(II) sulfate solution. The iodine released needed 20.0 cm$^3$ of 0.100 mol/dm$^3$ sodium thiosulfate. Find the concentration of the copper(II) ions.", steps=[
            S("Equations", math=r"\mathrm{2Cu^{2+} + 4I^- \rightarrow 2CuI + I_2}\qquad \mathrm{I_2 + 2S_2O_3^{2-} \rightarrow 2I^- + S_4O_6^{2-}}"),
            S("Moles of thiosulfate", math=r"0.100\times0.0200 = 2.00\times10^{-3}\ \mathrm{mol}"),
            S("Moles of I2 (ratio 1 : 2)", math=r"1.00\times10^{-3}\ \mathrm{mol}"),
            S("Moles of Cu2+ (ratio 2 : 1 with I2)", math=r"2.00\times10^{-3}\ \mathrm{mol}"),
            S("Concentration", math=r"c = \frac{2.00\times10^{-3}}{0.0250} = 0.0800\ \mathrm{mol\,dm^{-3}}"),
        ]),
        EX("Worked example 2: bleach", intro=r"10.0 cm$^3$ of household bleach was diluted to 250 cm$^3$. 25.0 cm$^3$ of the dilute solution was acidified and treated with excess potassium iodide. "
           r"The iodine released needed 12.0 cm$^3$ of 0.100 mol/dm$^3$ thiosulfate. Find the concentration of sodium hypochlorite, $\mathrm{NaOCl}$, in the bleach in mol/dm$^3$ and g/dm$^3$. ($A_r$: Na 23, O 16, Cl 35.5)", steps=[
            S("Equation", math=r"\mathrm{OCl^- + 2I^- + 2H^+ \rightarrow Cl^- + I_2 + H_2O}"),
            S("Moles of thiosulfate", math=r"0.100\times0.0120 = 1.20\times10^{-3}\ \mathrm{mol}"),
            S("Moles of I2 (1 : 2)", math=r"6.00\times10^{-4}\ \mathrm{mol}"),
            S("Moles of OCl- in 25.0 cm3 (1 : 1 with I2)", math=r"6.00\times10^{-4}\ \mathrm{mol}"),
            S("In 250 cm3, which came from 10.0 cm3 of bleach", math=r"6.00\times10^{-3}\ \mathrm{mol}\;\Rightarrow\; c = \frac{6.00\times10^{-3}}{0.0100} = 0.600\ \mathrm{mol\,dm^{-3}}"),
            S(r"Mass concentration ($M(\mathrm{NaOCl}) = 74.5$)", math=r"0.600\times74.5 = 44.7\ \mathrm{g\,dm^{-3}}"),
        ]),
        EX("Worked example 3: copper in brass", intro=r"1.20 g of brass (an alloy of copper and zinc) was dissolved in acid and the solution made up to 250 cm$^3$. 25.0 cm$^3$ of it, with excess iodide, released iodine that needed 12.3 cm$^3$ of 0.100 mol/dm$^3$ thiosulfate. "
           r"Find the percentage of copper in the brass. ($A_r$ of Cu = 63.5)", steps=[
            S("Moles of thiosulfate", math=r"0.100\times0.0123 = 1.23\times10^{-3}\ \mathrm{mol}"),
            S("Cu2+ : thiosulfate = 1 : 1", math=r"n(\mathrm{Cu^{2+}}) = 1.23\times10^{-3}\ \mathrm{mol\ in\ 25.0\ cm^3}"),
            S("Scale up to 250 cm3", math=r"1.23\times10^{-2}\ \mathrm{mol}"),
            S("Mass of copper", math=r"1.23\times10^{-2}\times63.5 = 0.781\ \mathrm{g}"),
            S("Percentage", math=r"\frac{0.781}{1.20}\times100 = 65.1\%"),
        ]),
        MISTAKE("Adding starch at the start", "With a lot of iodine present, the starch-iodine complex forms strongly and releases iodine slowly, which makes the end-point late and unclear. Wait until the solution is pale yellow, then add starch."),
        MISTAKE("Forgetting the 1 : 2 step", r"One $\mathrm{I_2}$ reacts with two $\mathrm{S_2O_3^{2-}}$. Halving the thiosulfate moles is needed to get moles of iodine, and sometimes a further factor to get moles of the oxidising agent. Write the chain before you calculate."),
        QUIZ(r"In the chain $\mathrm{OCl^-} \rightarrow \mathrm{I_2} \rightarrow \mathrm{S_2O_3^{2-}}$, how many moles of thiosulfate are needed per mole of hypochlorite?",
             ["0.5", "1", "2", "4"], 2,
             r"One mole of $\mathrm{OCl^-}$ releases one mole of $\mathrm{I_2}$, and one mole of $\mathrm{I_2}$ reacts with two moles of thiosulfate.",
             hint="Follow the chain with two equations: OCl- to I2, then I2 to S2O3 2-.",
             feedback=["This halves where it should double: iodine needs two thiosulfate ions, not half of one.", "This ignores the 1 : 2 ratio between I2 and thiosulfate.", "",
                       "This doubles twice. The first step is 1 : 1, so only one factor of 2 applies."]),
        TIP("The iodine-thiosulfate titration is a standard practical in Paper 3 and a frequent Paper 2 calculation. State the colours: brown to pale yellow, add starch, blue-black to colourless."),
        PQ(r"25.0 cm$^3$ of an iodine solution needed 20.0 cm$^3$ of 0.100 mol/dm$^3$ sodium thiosulfate. Find the concentration of the iodine.",
           r"$n(\mathrm{S_2O_3^{2-}}) = 0.100\times0.0200 = 2.00\times10^{-3}$ mol. $n(\mathrm{I_2}) = 1.00\times10^{-3}$ mol. $c = 1.00\times10^{-3}/0.0250 = 0.0400$ mol/dm$^3$."),
        PQ(r"10.0 cm$^3$ of bleach was diluted to 250 cm$^3$. 25.0 cm$^3$ of the dilute solution with excess acidified iodide released iodine that needed 9.0 cm$^3$ of 0.100 mol/dm$^3$ thiosulfate. Find the concentration of NaOCl in the bleach in g/dm$^3$. ($M(\mathrm{NaOCl}) = 74.5$)",
           r"$n(\mathrm{S_2O_3^{2-}}) = 0.100\times0.0090 = 9.0\times10^{-4}$ mol; $n(\mathrm{I_2}) = 4.5\times10^{-4}$ mol $= n(\mathrm{OCl^-})$ in 25.0 cm$^3$. In 250 cm$^3$: $4.5\times10^{-3}$ mol, from 10.0 cm$^3$ of bleach. "
           r"$c = 0.450$ mol/dm$^3$; mass concentration $= 0.450\times74.5 = 33.5$ g/dm$^3$."),
        PQ(r"1.00 g of copper(II) sulfate crystals, $\mathrm{CuSO_4\cdot5H_2O}$ ($M = 249.5$), was dissolved to make 100 cm$^3$. 10.0 cm$^3$ with excess iodide needed 10.0 cm$^3$ of 0.0400 mol/dm$^3$ thiosulfate. Find the percentage purity of the crystals.",
           r"$n(\mathrm{S_2O_3^{2-}}) = 0.0400\times0.0100 = 4.00\times10^{-4}$ mol. $n(\mathrm{Cu^{2+}}) = 4.00\times10^{-4}$ mol in 10.0 cm$^3$, so $4.00\times10^{-3}$ mol in 100 cm$^3$. "
           r"Mass $= 4.00\times10^{-3}\times249.5 = 0.998$ g. Purity $= 99.8\%$."),
        PQ(r"Show, using oxidation numbers, that the reaction between iodine and thiosulfate ions is a redox reaction and say which species is oxidised.",
           r"Iodine: 0 in $\mathrm{I_2}$ goes to $-1$ in $\mathrm{I^-}$ (reduced, gains electrons). Sulfur: +2 in $\mathrm{S_2O_3^{2-}}$ goes to an average of +2.5 in $\mathrm{S_4O_6^{2-}}$ (oxidised, loses electrons). "
           r"Thiosulfate is the reducing agent: $\mathrm{2S_2O_3^{2-} \rightarrow S_4O_6^{2-} + 2e^-}$; iodine is the oxidising agent: $\mathrm{I_2 + 2e^- \rightarrow 2I^-}$."),
        SUM("An oxidising agent plus excess iodide releases iodine; the iodine is titrated with sodium thiosulfate.",
            r"$\mathrm{I_2 + 2S_2O_3^{2-} \rightarrow 2I^- + S_4O_6^{2-}}$: moles of thiosulfate are twice moles of iodine.",
            r"Chains: $\mathrm{Cu^{2+}}$ : thiosulfate = 1 : 1; $\mathrm{OCl^-}$ : thiosulfate = 1 : 2.",
            "Add starch only near the end, when the solution is pale yellow; the end-point is blue-black to colourless."),
    ],
))


# ------------------------------------------------------------------ 8. Subatomic particles
LESSONS.append(lesson(
    module=M2,
    topic="Subatomic particles",
    title="Subatomic particles and how they were discovered",
    slug="chl1-subatomic-particles",
    minutes=22,
    summary="Name the evidence for the electron, nucleus and neutron, give the relative mass and charge of each particle, and work out the particles in atoms, ions and isotopes.",
    objectives=[
        "Describe how cathode rays, the gold-foil experiment and the neutron showed the structure of the atom",
        "State the relative mass and charge of protons, neutrons and electrons",
        "Find the numbers of protons, neutrons and electrons in atoms and ions from the nuclide symbol",
        "Explain why charged particles are deflected in electric fields by an amount that depends on charge and mass",
    ],
    key_concepts=["Electron", "Nucleus", "Proton", "Neutron", "Atomic number", "Mass number", "Isotope", "Charge-to-mass ratio"],
    blocks=[
        H("Introduction"),
        T("Atoms are far too small to see, so how do we know what is inside one? Chemists built the picture from experiments, one clue at a time. Each experiment in this lesson "
          "changed the model of the atom, and the numbers they produced are still used in mass spectrometry and in calculations about isotopes."),
        H("Three experiments"),
        D("In the 1890s J. J. Thomson showed that the rays in a vacuum discharge tube (cathode rays) are streams of negatively charged particles, because they bend towards a positive plate in an electric field. "
          "By measuring the bending he found the ratio of charge to mass. The particles are the **electrons**, and they come from every kind of atom. "
          "Later experiments (Millikan's oil drops) gave the charge of one electron, $1.60\\times10^{-19}$ C, so its mass could be calculated.", title="1. The electron"),
        D("In about 1909 Geiger and Marsden fired alpha particles (positively charged helium nuclei) at thin gold foil. Most passed straight through, a few were deflected, and about one in many thousands "
          "bounced back. Rutherford explained this: the atom is mostly empty space, and all the positive charge and almost all the mass are in a tiny, dense **nucleus**.", title="2. The nucleus"),
        IMG("al-chl1-rutherford.svg", alt="Alpha particles fired at gold foil: most go straight through, a few are deflected and a very few rebound",
            caption="Figure 1. Alpha scattering: the pattern showed a small, dense, positive nucleus."),
        D("The nucleus has less mass than the number of protons suggested. In 1932 Chadwick identified an uncharged particle with nearly the same mass as the proton, the **neutron**. "
          "Isotopes of an element have the same number of protons but different numbers of neutrons.", title="3. The neutron"),
        H("The particles"),
        CODE("""Particle   Symbol   Relative charge   Relative mass     Actual mass (kg)
proton     p        +1                1                 1.673 x 10^-27
neutron    n        0                 1                 1.675 x 10^-27
electron   e        -1                1/1836            9.11  x 10^-31
(charge of a proton = 1.60 x 10^-19 C)""", "text", title="Properties of subatomic particles"),
        KEY("Reading a nuclide symbol", r"For the nuclide $^{A}_{Z}\mathrm{X}^{q}$:", cards=[
            [r"Atomic number $Z$", "Number of protons. It defines the element."],
            [r"Mass number $A$", r"Protons plus neutrons. Number of neutrons $= A - Z$."],
            [r"Charge $q$", r"Number of electrons $= Z - q$ (for a positive ion $q > 0$ fewer electrons)."],
        ]),
        T("The nucleus is about $10^{-15}$ m across; the whole atom is about $10^{-10}$ m. The atom's diameter is therefore about 100 000 times that of its nucleus. Nearly all the mass is in the nucleus, because a proton is about 1836 times as heavy as an electron."),
        EX("Worked example 1: particles in atoms and ions", intro=r"Give the numbers of protons, neutrons and electrons in (a) $^{56}_{26}\mathrm{Fe}^{3+}$, (b) $^{35}_{17}\mathrm{Cl}^{-}$, (c) $^{27}_{13}\mathrm{Al}^{3+}$.", steps=[
            S(r"(a) Fe$^{3+}$", math=r"p = 26;\ n = 56 - 26 = 30;\ e = 26 - 3 = 23"),
            S(r"(b) Cl$^-$", math=r"p = 17;\ n = 35 - 17 = 18;\ e = 17 + 1 = 18"),
            S(r"(c) Al$^{3+}$", math=r"p = 13;\ n = 27 - 13 = 14;\ e = 13 - 3 = 10"),
        ]),
        EX("Worked example 2: how much heavier is a proton?", intro=r"Using the masses in the table, find the ratio of the mass of a proton to that of an electron, and the charge in coulombs on one mole of electrons ($L = 6.02\times10^{23}\ \mathrm{mol^{-1}}$).", steps=[
            S("Ratio of masses", math=r"\frac{1.673\times10^{-27}}{9.11\times10^{-31}} = 1.84\times10^{3} \approx 1836"),
            S("Charge on one mole of electrons", math=r"1.60\times10^{-19}\times6.02\times10^{23} = 9.63\times10^{4}\ \mathrm{C\,mol^{-1}}"),
            S("Link", text="This is the Faraday constant (about 96 500 C per mole), used in Upper Sixth electrolysis."),
        ]),
        EX("Worked example 3: deflection in an electric field", intro=r"A beam of $^{1}\mathrm{H}^{+}$, $^{2}\mathrm{H}^{+}$ and $^{4}\mathrm{He}^{2+}$ ions passes between two charged plates. Compare how much each beam is deflected.", steps=[
            S("The deflection of an ion is proportional to its charge-to-mass ratio, $q/m$", text="A larger charge gives a larger force; a larger mass resists it."),
            S("Calculate $q/m$ in units of $e$ per mass number", math=r"^{1}\mathrm{H}^{+}: \frac{1}{1} = 1;\quad {}^{2}\mathrm{H}^{+}: \frac{1}{2} = 0.5;\quad {}^{4}\mathrm{He}^{2+}: \frac{2}{4} = 0.5"),
            S("Conclude", text="1H+ is deflected most (twice as much). 2H+ and 4He2+ are deflected by the same amount and cannot be separated by an electric field alone."),
        ]),
        MISTAKE("Using the wrong number for electrons in an ion", "A positive ion has lost electrons, so there are fewer electrons than protons. Fe3+ has 26 protons but only 23 electrons. A negative ion has gained electrons."),
        MISTAKE("Thinking isotopes differ in protons", "Isotopes of an element have the same atomic number (same protons and electrons, so the same chemical behaviour) and differ only in neutrons, hence in mass."),
        QUIZ(r"What do the particles $^{35}\mathrm{Cl}^{-}$ and $^{37}\mathrm{Cl}^{-}$ have in common?",
             ["The same number of neutrons", "The same number of protons and electrons", "The same mass number", "The same number of protons but a different number of electrons"], 1,
             "They are isotopes of chlorine with the same charge: 17 protons and 18 electrons each. They differ only in neutrons (18 and 20).",
             hint="Isotopes differ in only one of the three particle numbers.",
             feedback=["The neutron numbers are 18 and 20.", "", "The mass numbers are 35 and 37, so they differ.",
                       "Both have the same charge, so the electron numbers are equal (18)."]),
        TIP("Questions on subatomic particles appear in Paper 1 as short recall or numerical items and in Paper 2 as the start of mass-spectrometry questions. Always show protons, neutrons and electrons separately."),
        PQ(r"Give the numbers of protons, neutrons and electrons in $^{31}_{15}\mathrm{P}^{3-}$.",
           r"Protons $= 15$. Neutrons $= 31 - 15 = 16$. Electrons $= 15 + 3 = 18$."),
        PQ(r"What fraction of the mass of a hydrogen-1 atom is due to its electron? ($m_p = 1.673\times10^{-27}$ kg, $m_e = 9.11\times10^{-31}$ kg)",
           r"Mass of atom $\approx 1.673\times10^{-27} + 9.11\times10^{-31} = 1.6739\times10^{-27}$ kg. Fraction $= 9.11\times10^{-31}/1.6739\times10^{-27} = 5.44\times10^{-4}$, about 0.054%."),
        PQ("Explain how the results of the alpha-particle scattering experiment led to the nuclear model of the atom.",
           "Most alpha particles went straight through, so most of the atom is empty space. A few were deflected through large angles, so there is a small region of positive charge repelling them. "
           "A very few bounced almost straight back, so that positive region is very dense and holds most of the atom's mass. This is the nucleus."),
        PQ(r"A beam of $^{12}\mathrm{C}^{+}$ and $^{12}\mathrm{C}^{2+}$ ions passes through an electric field. Which is deflected more, and by what factor?",
           r"Deflection is proportional to $q/m$. $^{12}\mathrm{C}^{+}$: $1/12$. $^{12}\mathrm{C}^{2+}$: $2/12$. The 2+ ion has twice the charge-to-mass ratio, so it is deflected twice as much."),
        SUM("Cathode rays gave electrons, gold-foil scattering gave the small dense nucleus, and Chadwick found the neutron.",
            "Proton: relative mass 1, charge +1. Neutron: mass 1, charge 0. Electron: mass 1/1836, charge -1.",
            r"For $^{A}_{Z}\mathrm{X}^{q}$: protons $= Z$, neutrons $= A - Z$, electrons $= Z - q$.",
            "Deflection of an ion in an electric or magnetic field depends on its charge-to-mass ratio, which is the basis of mass spectrometry."),
    ],
))

# ------------------------------------------------------------------ 9. Mass spectrometer and relative atomic mass
LESSONS.append(lesson(
    module=M2,
    topic="Mass spectrometry",
    title="The mass spectrometer and relative atomic mass",
    slug="chl1-mass-spectrometer-ar",
    minutes=23,
    summary="Describe the four stages of a mass spectrometer and use isotope abundances from a mass spectrum to calculate relative atomic mass, or the reverse.",
    objectives=[
        "Describe ionisation, acceleration, deflection and detection in a mass spectrometer",
        "Explain why a vacuum is used and why only positive ions are detected",
        "Calculate relative atomic mass from isotope masses and abundances",
        "Find isotope abundances from a known relative atomic mass",
    ],
    key_concepts=["Mass spectrometer", "m/z", "Relative isotopic mass", "Isotope abundance", "Relative atomic mass"],
    blocks=[
        H("Introduction"),
        T("The relative atomic mass of chlorine on the periodic table is 35.5, yet no chlorine atom has that mass. Every atom of chlorine has a mass number of 35 or 37. "
          "A **mass spectrometer** separates ions of different mass and measures how many of each kind there are, which explains the average. It is also the machine used in forensic and food laboratories "
          "to identify unknown substances."),
        IMG("al-chl1-mass-spectrometer.svg", alt="Schematic of a mass spectrometer: ionisation chamber, accelerating plates, magnetic field bending ion paths, and a detector",
            caption="Figure 1. The four stages. Only ions of the right m/z follow the path that reaches the detector."),
        KEY("Four stages", "In the order the sample meets them.", cards=[
            ["1. Ionisation", "The sample is vaporised and bombarded by high-energy electrons, which knock out an electron to form positive ions: X(g) gives X+(g) + e-."],
            ["2. Acceleration", "An electric field accelerates the positive ions to a high speed."],
            ["3. Deflection", "A magnetic field bends the ion paths. Lighter ions (or ions with higher charge) bend more. Changing the field strength brings ions of each m/z in turn to the detector."],
            ["4. Detection", "Ions hitting the detector produce a current that is proportional to how many arrive. The computer plots a mass spectrum."],
        ]),
        T("The whole instrument is under high vacuum so that ions do not collide with air molecules. Only positive ions are accelerated and bent in the usual set-up. "
          "The horizontal axis of a spectrum is the **mass-to-charge ratio**, $m/z$. For singly charged ions ($z = 1$) it equals the mass number. A 2+ ion appears at half its mass number, so $^{24}\\mathrm{Mg}^{2+}$ gives a small peak at $m/z = 12$."),
        D(r"The **relative atomic mass**, $A_r$, of an element is the weighted mean of the masses of its atoms, compared with one twelfth of the mass of a carbon-12 atom. For an element with isotopes of masses $m_1, m_2, \dots$ and abundances $a_1, a_2, \dots$ (in per cent):",
          title="Definition: relative atomic mass", formula=r"A_r = \frac{m_1 a_1 + m_2 a_2 + \cdots}{a_1 + a_2 + \cdots}"),
        H("Worked examples"),
        EX("Worked example 1: boron", intro=r"A mass spectrum of boron shows peaks at $m/z = 10$ (19.9%) and $m/z = 11$ (80.1%). Calculate the relative atomic mass.", steps=[
            S("Multiply each mass by its abundance", math=r"10\times19.9 = 199.0;\qquad 11\times80.1 = 881.1"),
            S("Add and divide by the total abundance (100)", math=r"A_r = \frac{199.0 + 881.1}{100} = 10.8"),
        ], check=r"10.8 \text{ lies between 10 and 11, nearer to 11 because }{}^{11}\mathrm{B}\text{ is more abundant}"),
        EX("Worked example 2: chlorine from peak heights", intro=r"The peaks for $^{35}\mathrm{Cl}^+$ and $^{37}\mathrm{Cl}^+$ are in the height ratio 3 : 1. Find the relative atomic mass of chlorine.", steps=[
            S("Abundances are 75% and 25%", math=r"\frac{3}{3+1} = 75\%,\qquad \frac{1}{3+1} = 25\%"),
            S("Weighted mean", math=r"A_r = \frac{35\times75 + 37\times25}{100} = \frac{2625 + 925}{100} = 35.5"),
        ]),
        EX("Worked example 3: abundance from a known Ar", intro=r"Copper has two isotopes, $^{63}\mathrm{Cu}$ and $^{65}\mathrm{Cu}$. Its relative atomic mass is 63.5. Find the percentage abundance of each.", steps=[
            S("Let the abundance of 63Cu be $x$ per cent", math=r"\frac{63x + 65(100 - x)}{100} = 63.5"),
            S("Expand and solve", math=r"63x + 6500 - 65x = 6350 \;\Rightarrow\; -2x = -150 \;\Rightarrow\; x = 75"),
            S("Answer", text="63Cu is 75% and 65Cu is 25%."),
        ], check=r"\frac{63\times75 + 65\times25}{100} = 63.5"),
        MISTAKE("Averaging the mass numbers without weighting", "Taking (10 + 11)/2 = 10.5 for boron ignores that the isotopes are not equally abundant. Always weight by abundance."),
        MISTAKE("Forgetting the 2+ peaks", "A small peak at half a mass number usually belongs to a doubly charged ion with m/z = mass/2. Do not count it as another isotope."),
        QUIZ("Why must the inside of a mass spectrometer be kept under a high vacuum?",
             ["So that the sample stays liquid", "So that ions do not collide with air particles on their way to the detector", "So that neutral atoms are also detected", "To increase the charge on the ions"], 1,
             "Collisions with air molecules would scatter or neutralise the ions, so they would not follow the intended path.",
             hint="Think about what would happen to a moving ion in air.",
             feedback=["A vacuum has nothing to do with the state of the sample; the sample is vaporised.", "",
                       "Only ions are accelerated and deflected; neutral atoms are not detected.", "The charge is set by ionisation, not by the vacuum."]),
        TIP("Relative atomic mass from a spectrum is a regular Paper 2 calculation, and the method also appears in Paper 1. Give the answer to the number of decimal places the data allow, usually one."),
        PQ(r"Neon has three isotopes: $^{20}\mathrm{Ne}$ (90.48%), $^{21}\mathrm{Ne}$ (0.27%) and $^{22}\mathrm{Ne}$ (9.25%). Calculate the relative atomic mass.",
           r"$A_r = \dfrac{20(90.48) + 21(0.27) + 22(9.25)}{100} = \dfrac{1809.6 + 5.67 + 203.5}{100} = 20.19 \approx 20.2$."),
        PQ(r"Lithium has isotopes $^{6}\mathrm{Li}$ (7.6%) and $^{7}\mathrm{Li}$ (92.4%). Calculate its relative atomic mass.",
           r"$A_r = \dfrac{6(7.6) + 7(92.4)}{100} = \dfrac{45.6 + 646.8}{100} = 6.92$."),
        PQ(r"Silver has two isotopes, $^{107}\mathrm{Ag}$ (51.8%) and $^{109}\mathrm{Ag}$ (48.2%). Calculate $A_r$ and explain why 107.96 is not a whole number.",
           r"$A_r = \dfrac{107(51.8) + 109(48.2)}{100} = \dfrac{5542.6 + 5253.8}{100} = 107.96$. It is a weighted average of two isotopes with different masses; no individual atom has that mass."),
        PQ("Describe what happens to the sample in each of the four stages of a mass spectrometer, and why the ions must be deflected before detection.",
           "Ionisation: vaporised atoms are hit by fast electrons and become positive ions. Acceleration: an electric field gives all ions the same kinetic energy. Deflection: a magnetic field bends the paths; lighter ions bend more, "
           "so ions with different m/z are separated. Detection: ions arriving at the detector produce a current proportional to their number. Deflection separates the isotopes before they are counted."),
        SUM("A mass spectrometer ionises, accelerates, deflects (by m/z) and detects ions in a vacuum.",
            r"The x-axis is $m/z$; for 1+ ions it equals the mass number, and a 2+ ion appears at half its mass.",
            r"$A_r = \sum (\text{mass} \times \text{abundance}) / \sum (\text{abundance})$.",
            "To find abundances from a known Ar, call one abundance x and the other (100 - x) and solve."),
    ],
))


# ------------------------------------------------------------------ 10. Mass spectra of compounds
LESSONS.append(lesson(
    module=M2,
    topic="Mass spectrometry",
    title="Interpreting mass spectra of molecules",
    slug="chl1-mass-spectra-molecules",
    minutes=24,
    summary="Read the molecular ion, the M+1 and M+2 peaks and common fragments in the mass spectrum of a molecule to find its relative molecular mass, its number of carbon atoms and whether it contains chlorine or bromine.",
    objectives=[
        "Identify the molecular ion peak and use it for the relative molecular mass",
        "Use the M+1 peak to estimate the number of carbon atoms",
        "Recognise the M and M+2 patterns of chlorine (3 : 1) and bromine (1 : 1) and the patterns for Cl2 and Br2",
        "Assign common fragment ions from the mass lost",
    ],
    key_concepts=["Molecular ion", "Fragmentation", "M+1 peak and carbon-13", "Isotope patterns of Cl and Br", "Base peak"],
    blocks=[
        H("Introduction"),
        T("A food-safety laboratory in Douala receives an unknown solvent. A mass spectrum can show its relative molecular mass, whether it contains chlorine or bromine, and, from its fragments, "
          "which groups it contains. In this lesson you read these clues in the same order an examiner expects."),
        D("In electron-impact ionisation a molecule M loses one electron and becomes the **molecular ion**, $\\mathrm{M^{+}}$ (written $\\mathrm{M^{\\cdot+}}$ in some books). "
          "Its $m/z$ equals the relative molecular mass $M_r$ when only the most common isotopes are present. The molecular ion often breaks into smaller **fragment ions**, and the tallest peak is called the **base peak**.", title="Molecular ion and fragments"),
        KEY("Four clues in a spectrum", "Check them in this order.", cards=[
            ["Right-most main peak", "The molecular ion: its m/z is the relative molecular mass (ignore small M+1 and M+2 peaks for now)."],
            ["M+1 peak", "A small peak one unit above M, caused by molecules that contain one carbon-13 atom (1.1% of carbon). Number of C atoms is about (height of M+1 / height of M) x 100 / 1.1."],
            ["M+2 peak", "A peak two units above M signals chlorine (M : M+2 = 3 : 1) or bromine (M : M+2 = 1 : 1)."],
            ["Fragments", "The difference between M and a fragment is the mass lost, which points to the group lost (15 = CH3, 17 = OH, 29 = C2H5 or CHO)."],
        ]),
        IMG("al-chl1-ms-chlorine.svg", alt="Mass spectrum of chlorine gas: peaks at 35 and 37 in the ratio 3 to 1, and at 70, 72 and 74 in the ratio 9 to 6 to 1",
            caption="Figure 1. Chlorine, Cl2. Each atom is 35Cl (75%) or 37Cl (25%), so molecules combine in the ratio 9 : 6 : 1."),
        T(r"The 9 : 6 : 1 pattern comes from probabilities. The chance of a $^{35}\mathrm{Cl}$ atom is $\frac{3}{4}$, of $^{37}\mathrm{Cl}$ it is $\frac{1}{4}$. For $\mathrm{Cl_2}$: $^{35}\mathrm{Cl}{-}^{35}\mathrm{Cl}$ (m/z 70) has probability $\left(\frac{3}{4}\right)^2 = \frac{9}{16}$; "
          r"one of each (m/z 72) has probability $2\times\frac{3}{4}\times\frac{1}{4} = \frac{6}{16}$; $^{37}\mathrm{Cl}{-}^{37}\mathrm{Cl}$ (m/z 74) has probability $\left(\frac{1}{4}\right)^2 = \frac{1}{16}$. "
          r"Bromine is about half $^{79}\mathrm{Br}$ and half $^{81}\mathrm{Br}$, so $\mathrm{Br_2}$ gives peaks at 158, 160 and 162 in the ratio 1 : 2 : 1."),
        H("Worked examples"),
        EX("Worked example 1: a chloroalkane", intro=r"The mass spectrum of a compound $\mathrm{C_2H_5Cl}$ has peaks at $m/z = 64$ and $66$ in the height ratio 3 : 1, and a base peak at $m/z = 29$. Explain these peaks. ($A_r$: C 12, H 1; use $^{35}\mathrm{Cl}$ and $^{37}\mathrm{Cl}$)", steps=[
            S("Molecular ions", math=r"\mathrm{C_2H_5{}^{35}Cl}: 24 + 5 + 35 = 64;\qquad \mathrm{C_2H_5{}^{37}Cl}: 24 + 5 + 37 = 66"),
            S("Ratio 3 : 1", text="This matches the natural ratio of 35Cl to 37Cl, so the compound contains one chlorine atom."),
            S("Base peak at 29", math=r"64 - 35 = 29 = \mathrm{C_2H_5^+}\quad(24 + 5)"),
            S("Why only one peak at 29", text="The fragment no longer contains chlorine, so it has no 37Cl partner."),
        ]),
        EX("Worked example 2: how many carbon atoms?", intro=r"In the mass spectrum of a hydrocarbon the molecular-ion peak has height 100 units and the M+1 peak has height 5.5 units. How many carbon atoms does a molecule contain?", steps=[
            S("Each carbon contributes 1.1% to M+1", text="The probability that a given carbon atom is carbon-13 is 1.1%."),
            S("Carbon atoms", math=r"\frac{5.5}{100}\times100\div1.1 = 5"),
            S("Conclusion", text="Five carbon atoms. With $M_r = 70$ the compound could be $\\mathrm{C_5H_{10}}$ (check: $60 + 10 = 70$)."),
        ]),
        EX("Worked example 3: propanone", intro=r"The mass spectrum of propanone, $\mathrm{CH_3COCH_3}$, has peaks at $m/z = 58$, 43 and 15. Suggest the ions responsible. ($A_r$: C 12, H 1, O 16)", steps=[
            S("m/z 58", math=r"[\mathrm{CH_3COCH_3}]^{+}:\ 36 + 6 + 16 = 58\quad(\text{molecular ion})"),
            S("m/z 43 is 15 less than M", math=r"58 - 15 = 43:\ \mathrm{CH_3CO^+}\quad(24 + 3 + 16 = 43)"),
            S("m/z 15", math=r"\mathrm{CH_3^+}\quad(12 + 3 = 15)"),
            S("Conclusion", text="The base peak at 43 shows the C-C bond next to the C=O breaks easily, losing a CH3 group (mass 15)."),
        ]),
        MISTAKE("Calling the tallest peak the molecular ion", "The tallest peak is the base peak and is often a fragment. The molecular ion is the peak with the highest m/z in the main group (ignoring the small M+1 and M+2 peaks)."),
        MISTAKE("Missing that Cl and Br patterns need different ratios", "Chlorine gives M : M+2 = 3 : 1; bromine gives 1 : 1. A compound with two chlorine atoms gives M, M+2, M+4 in the ratio 9 : 6 : 1."),
        QUIZ(r"A compound's spectrum shows two peaks of almost equal height at $m/z = 94$ and $m/z = 96$. Which atom is present?",
             ["One chlorine atom", "One bromine atom", "One iodine atom", "Two chlorine atoms"], 1,
             r"Peaks two units apart in a 1 : 1 ratio show one bromine atom ($^{79}\mathrm{Br}$ and $^{81}\mathrm{Br}$ in about equal amounts). $\mathrm{CH_3Br}$ gives 94 and 96.",
             hint="Which halogen has two isotopes in roughly equal amounts?",
             feedback=["One chlorine gives a 3 : 1 ratio of the M and M+2 peaks.", "", "Iodine has only one stable isotope, so there is no M+2 peak.",
                       "Two chlorines give three peaks at M, M+2 and M+4 in the ratio 9 : 6 : 1."]),
        TIP("Spectra of molecules appear in Paper 2 structure-elucidation questions and, in simple form, in Paper 1. Say which peak is M, show the subtraction for each fragment, and state the isotope pattern in words."),
        PQ(r"Predict the $m/z$ values and relative heights of the molecular-ion peaks for $\mathrm{Br_2}$. ($A_r$: $^{79}\mathrm{Br}$ and $^{81}\mathrm{Br}$ in equal amounts)",
           r"Combinations: $^{79}\mathrm{Br}{-}^{79}\mathrm{Br}$ gives $m/z = 158$ (probability $\frac{1}{4}$); $^{79}\mathrm{Br}{-}^{81}\mathrm{Br}$ gives 160 (probability $\frac{1}{2}$); $^{81}\mathrm{Br}{-}^{81}\mathrm{Br}$ gives 162 ($\frac{1}{4}$). Height ratio 1 : 2 : 1."),
        PQ(r"The spectrum of a hydrocarbon has M at height 100 and M+1 at height 3.3. How many carbon atoms are present?",
           r"$\dfrac{3.3}{100}\times100 \div 1.1 = 3$ carbon atoms."),
        PQ(r"Calculate the heights of the peaks for $\mathrm{Cl_2}$ at $m/z = 70, 72, 74$, given that the ratio of $^{35}\mathrm{Cl}$ to $^{37}\mathrm{Cl}$ is 3 : 1, and state the ratio.",
           r"70: $\left(\frac{3}{4}\right)^2 = 0.5625$. 72: $2\times\frac{3}{4}\times\frac{1}{4} = 0.375$. 74: $\left(\frac{1}{4}\right)^2 = 0.0625$. Ratio $9 : 6 : 1$."),
        PQ(r"Bromomethane, $\mathrm{CH_3Br}$, gives a spectrum with peaks at $m/z = 94$ and 96, and strong peaks at 15 and at 79 and 81. Assign these four peaks. ($A_r$: C 12, H 1)",
           r"94 and 96: molecular ions $\mathrm{CH_3{}^{79}Br^+}$ ($12 + 3 + 79 = 94$) and $\mathrm{CH_3{}^{81}Br^+}$ (96), in a 1 : 1 ratio. 15: $\mathrm{CH_3^+}$ ($12 + 3$), after loss of Br. 79 and 81: $\mathrm{{}^{79}Br^+}$ and $\mathrm{{}^{81}Br^+}$."),
        SUM("The molecular ion peak (highest m/z of the main group) gives the relative molecular mass.",
            "The M+1 peak gives the number of carbon atoms: height ratio (as a percentage) divided by 1.1.",
            "M : M+2 = 3 : 1 means one Cl; 1 : 1 means one Br. Cl2 gives 9 : 6 : 1 and Br2 gives 1 : 2 : 1.",
            "Subtract a fragment's m/z from M to find the mass lost and name the group."),
    ],
))


# ------------------------------------------------------------------ 11. Ionisation energy trends
LESSONS.append(lesson(
    module=M2,
    topic="Ionization energy trends",
    title="Ionisation energy: definitions, trends and evidence",
    slug="chl1-ionisation-energy-trends",
    minutes=24,
    summary="Define first and successive ionisation energies, explain trends down groups and across Period 2, and use successive values to find the group of an element.",
    objectives=[
        "Define first ionisation energy and write equations for first, second and third ionisation",
        "Explain trends down a group and across a period, including the dips at Group 3 and Group 6",
        "Use successive ionisation energies to deduce the group of an element",
        "Link ionisation energy to nuclear charge, distance, shielding and electron repulsion",
    ],
    key_concepts=["First ionisation energy", "Successive ionisation energy", "Shielding", "Nuclear charge", "Sub-shell energy", "Spin-pair repulsion"],
    blocks=[
        H("Introduction"),
        T("Why does sodium react vigorously with water but neon does not react at all? Part of the answer is how easily each atom gives up an electron. "
          "**Ionisation energy** measures that, and the pattern across the periodic table gives direct evidence for the shells and sub-shells you meet in the next two lessons."),
        D(r"The **first ionisation energy** of an element is the energy needed to remove one electron from each atom in one mole of gaseous atoms, to form one mole of gaseous 1+ ions.", title="Definition",
          formula=r"\mathrm{X(g) \rightarrow X^+(g) + e^-}\qquad \Delta H = +\ \mathrm{kJ\,mol^{-1}}",
          note="The second ionisation energy refers to X+(g) -> X2+(g) + e-, and so on. All ionisation energies are positive (endothermic)."),
        CODE("""First :  Mg(g)    -> Mg+(g)  + e-
Second:  Mg+(g)   -> Mg2+(g) + e-
Third :  Mg2+(g)  -> Mg3+(g) + e-
(state symbols (g) are part of the definition)""", "text", title="Equations for successive ionisation of magnesium"),
        KEY("Four factors", "Explain every trend with these, in this order.", cards=[
            ["Nuclear charge", "More protons pull the electrons harder: ionisation energy rises."],
            ["Distance", "The farther the outer electron is from the nucleus, the weaker the pull."],
            ["Shielding", "Inner shells repel the outer electron and cancel part of the nuclear charge."],
            ["Sub-shell and pairing", "Electrons in a higher-energy sub-shell, or paired in the same orbital, are easier to remove."],
        ]),
        H("Trends"),
        T("**Down a group** the first ionisation energy falls: the outer electron is in a shell farther from the nucleus and more shielded, and this outweighs the extra protons."),
        CODE("""Group 1 (kJ/mol)          Group 2 (kJ/mol)
Li   520                  Be   900
Na   496                  Mg   738
K    419                  Ca   590
Rb   403                  Sr   550
Cs   376                  Ba   503
(rounded teaching values: check your textbook)""", "text", title="Down Groups 1 and 2"),
        T("**Across Period 2** the general rise comes from increasing nuclear charge with the electrons going into the same shell, so shielding hardly changes. There are two dips:"),
        IMG("al-chl1-ie-period2.svg", alt="Graph of first ionisation energy from lithium to neon with dips at boron and oxygen",
            caption="Figure 1. Period 2 first ionisation energies: general rise with dips at B and O."),
        KEY("Two dips to explain", "These are the classic evidence for sub-shells and for electron pairing.", cards=[
            ["Be to B (dip)", r"B has its outer electron in a 2p sub-shell. A 2p electron is on average farther out and higher in energy than a 2s electron, and is shielded by the 2s electrons, so it is easier to remove."],
            ["N to O (dip)", r"In O ($2p^4$) two electrons share one 2p orbital. They repel each other, so one is removed more easily than from N ($2p^3$), where each 2p orbital has one electron."],
        ]),
        T("The same two reasons explain the dips from Mg to Al (3s to 3p) and from P to S in Period 3."),
        H("Successive ionisation energies"),
        T("Removing a second electron from a positive ion is harder than removing the first, because the ion has the same nuclear charge but fewer electrons. "
          "The big evidence for shells comes when electrons start to be removed from a **new, inner shell**: there is a very large jump."),
        EX("Worked example 1: which group?", intro=r"The first five ionisation energies of element W (in kJ/mol) are 496, 4562, 6910, 9543 and 13 354. Deduce the group of W.", steps=[
            S("Look for the biggest jump", math=r"496 \rightarrow 4562\ \text{(a jump of about nine times)}"),
            S("Interpret", text="The first electron comes from the outer shell. The second comes from the inner shell, which is much closer to the nucleus and less shielded."),
            S("Conclusion", text="One outer electron: W is in Group 1. The data match sodium."),
        ]),
        EX("Worked example 2: Mg and Al", intro=r"The first ionisation energy of aluminium (578 kJ/mol) is lower than that of magnesium (738 kJ/mol). Explain.", steps=[
            S("Electron configurations", math=r"\mathrm{Mg}: 1s^2 2s^2 2p^6 3s^2;\qquad \mathrm{Al}: 1s^2 2s^2 2p^6 3s^2 3p^1"),
            S("Where the electron comes from", text="Mg loses a 3s electron. Al loses a 3p electron."),
            S("Explain", text="A 3p electron is higher in energy and farther from the nucleus on average. It is also shielded by the 3s electrons. These effects outweigh the extra proton in Al."),
        ]),
        EX("Worked example 3: nitrogen and oxygen", intro=r"Explain why oxygen (1314 kJ/mol) has a lower first ionisation energy than nitrogen (1402 kJ/mol).", steps=[
            S("Configurations", math=r"\mathrm{N}: 2p^3\ (\uparrow\ \uparrow\ \uparrow);\qquad \mathrm{O}: 2p^4\ (\uparrow\downarrow\ \uparrow\ \uparrow)"),
            S("Explain", text="In O two electrons occupy the same 2p orbital and repel each other. Removing one relieves this repulsion, so less energy is needed than for nitrogen, whose 2p orbitals each hold one electron."),
        ]),
        MISTAKE("Saying 'full shells are stable' without the factors", "Always give nuclear charge, distance, shielding and, where relevant, sub-shell or electron-pair repulsion. 'It likes a full shell' scores no marks in an A Level explanation."),
        MISTAKE("Omitting state symbols in the equation", "An ionisation equation must show gaseous states: Mg(g) goes to Mg+(g) + e-. Without (g) the equation does not match the definition."),
        QUIZ("The first four ionisation energies of an element X are 738, 1451, 7733 and 10 540 kJ/mol. In which group is X?",
             ["Group 1", "Group 2", "Group 3", "Group 4"], 1,
             "The big jump comes between the second and third values (1451 to 7733), so two electrons are in the outer shell. X is in Group 2 (it is magnesium).",
             hint="Where is the first very large jump?",
             feedback=["A Group 1 element would show the big jump after the first value.", "", "A Group 3 element would show the big jump after the third value.",
                       "The jump here is after the second value, not the fourth."]),
        TIP("Ionisation energy appears in Paper 1 (graph interpretation and group identification) and Paper 2 (equations, explanations of dips). Learn the equations with state symbols."),
        PQ(r"Write equations, with state symbols, for the second ionisation energy of magnesium and the third ionisation energy of aluminium.",
           r"$\mathrm{Mg^+(g) \rightarrow Mg^{2+}(g) + e^-}$ and $\mathrm{Al^{2+}(g) \rightarrow Al^{3+}(g) + e^-}$. (Charge check: $+1 = +2 - 1$ and $+2 = +3 - 1$.)"),
        PQ(r"The first five ionisation energies of an element (kJ/mol) are 590, 1145, 4912, 6491 and 8153. State the group of the element and explain.",
           r"The first very large increase is from 1145 to 4912, after two electrons are removed. Two electrons are in the outer shell, so the element is in Group 2 (it is calcium)."),
        PQ("Explain why the first ionisation energy of the Group 1 elements decreases from lithium (520 kJ/mol) to caesium (376 kJ/mol).",
           "Down the group the outer electron is in a shell farther from the nucleus and is shielded by more inner shells. These effects outweigh the increase in nuclear charge, so the attraction on the outer electron falls and it is easier to remove."),
        PQ("Explain why sulfur (1000 kJ/mol) has a lower first ionisation energy than phosphorus (1012 kJ/mol).",
           r"Phosphorus ($3p^3$) has one electron in each 3p orbital. In sulfur ($3p^4$) two electrons share one 3p orbital and repel each other, so one is removed slightly more easily despite sulfur's larger nuclear charge."),
        SUM("First ionisation energy: X(g) to X+(g) + e-, per mole, always endothermic.",
            "Trends depend on nuclear charge, distance, shielding, sub-shell and electron-pair repulsion.",
            "Down a group it falls; across a period it rises, with dips at Group 3 (new p sub-shell) and Group 6 (paired electrons).",
            "A very large jump in successive ionisation energies shows that the next electron comes from an inner shell, so it identifies the group."),
    ],
))


# ------------------------------------------------------------------ 12. Atomic orbitals and quantum numbers
LESSONS.append(lesson(
    module=M2,
    topic="Atomic orbitals and quantum numbers",
    title="Atomic orbitals and the four quantum numbers",
    slug="chl1-orbitals-quantum-numbers",
    minutes=24,
    summary="Describe s, p and d orbitals, state the allowed values of the four quantum numbers, and count orbitals and electrons in shells and sub-shells.",
    objectives=[
        "Define an atomic orbital and describe the shapes of s and p orbitals and the d orbital cloverleaf",
        "State the meaning and allowed values of n, l, ml and ms",
        "Show that shell n has n squared orbitals and holds 2n squared electrons",
        "Decide whether a set of quantum numbers is allowed",
    ],
    key_concepts=["Atomic orbital", "Principal quantum number n", "Orbital quantum number l", "Magnetic quantum number ml", "Spin quantum number ms", "Sub-shell"],
    blocks=[
        H("Introduction"),
        T("In the early atomic models electrons circled the nucleus like planets. Quantum theory replaced that picture. We cannot say exactly where an electron is; we can only say where it is likely to be found. "
          "Each electron in an atom is described by four numbers, a kind of address: the shell, the sub-shell, the orbital and the spin. This lesson explains what each number means and how many addresses there are."),
        D("An **atomic orbital** is a region of space around the nucleus in which there is a high probability (usually taken as 90%) of finding an electron. Each orbital holds a maximum of two electrons, with opposite spins.", title="Definition: atomic orbital"),
        IMG("al-chl1-orbitals.svg", alt="Shapes of s, p and d orbitals: a sphere, three dumbbells along x, y and z, and a cloverleaf",
            caption="Figure 1. An s orbital is a sphere; a p orbital is a dumbbell along one axis (px, py, pz); most d orbitals are cloverleaf shaped."),
        H("The four quantum numbers"),
        CODE("""Number   Name                 Allowed values               What it tells you
n        principal            1, 2, 3, ...                 the shell (energy and size)
l        orbital (angular)    0 to n-1                     the sub-shell and shape: l = 0 s, 1 p, 2 d, 3 f
ml       magnetic             -l, ..., 0, ..., +l          which orbital in the sub-shell (2l + 1 values)
ms       spin                 +1/2 or -1/2                 the spin direction of the electron""", "text", title="Quantum numbers"),
        KEY("Counting rules", "Everything follows from the allowed values.", cards=[
            ["Orbitals in a sub-shell", "2l + 1: one s orbital, three p, five d, seven f."],
            ["Electrons in a sub-shell", "2(2l + 1): 2 in s, 6 in p, 10 in d, 14 in f."],
            ["Orbitals in shell n", r"$n^2$ (add up the sub-shells)."],
            ["Electrons in shell n", r"$2n^2$: 2, 8, 18, 32 for $n = 1, 2, 3, 4$."],
        ]),
        T("The Pauli exclusion principle says no two electrons in an atom can have the same set of all four quantum numbers. Two electrons in one orbital share $n$, $l$ and $m_l$, so they must differ in $m_s$: this is why an orbital holds at most two electrons."),
        T("Orbitals in the same sub-shell, such as the three 2p orbitals, have the same energy in an isolated atom; we say they are **degenerate**. "
          "A p orbital has a node (a plane where the probability of finding the electron is zero) at the nucleus. The three p orbitals are at right angles along the x, y and z axes."),
        H("Worked examples"),
        EX("Worked example 1: the third shell", intro=r"For $n = 3$, list the sub-shells and give the number of orbitals and the maximum number of electrons.", steps=[
            S(r"Allowed $l$ values", math=r"l = 0, 1, 2 \;\Rightarrow\; 3s,\ 3p,\ 3d"),
            S("Orbitals in each", math=r"3s: 1;\quad 3p: 3;\quad 3d: 5"),
            S("Total orbitals and electrons", math=r"1 + 3 + 5 = 9 = 3^2 \text{ orbitals};\qquad 2 \times 9 = 18 = 2(3)^2 \text{ electrons}"),
        ]),
        EX("Worked example 2: is this set allowed?", intro=r"Decide whether each set of quantum numbers $(n, l, m_l, m_s)$ is allowed. (a) $(2, 2, 0, +\tfrac12)$ (b) $(3, 1, -2, -\tfrac12)$ (c) $(3, 2, +2, +\tfrac12)$ (d) $(1, 0, 0, -\tfrac12)$", steps=[
            S("(a) Check $l \\le n - 1$", text="For n = 2, l can only be 0 or 1. l = 2 is not allowed."),
            S("(b) Check |ml| <= l", text="For l = 1, ml can only be -1, 0 or +1. ml = -2 is not allowed."),
            S("(c) All rules satisfied", text="n = 3, l = 2 (a 3d sub-shell), ml = +2 is within -2 to +2, ms = +1/2 is allowed. Allowed."),
            S("(d) All rules satisfied", text="n = 1, l = 0 (1s), ml = 0, ms = -1/2. Allowed."),
        ]),
        EX("Worked example 3: counting a special case", intro=r"How many electrons in the shell $n = 4$ can have $m_l = 0$?", steps=[
            S(r"List the sub-shells of $n = 4$", math=r"l = 0, 1, 2, 3 \;\Rightarrow\; 4s, 4p, 4d, 4f"),
            S("Each sub-shell has exactly one orbital with ml = 0", text="So there are 4 orbitals with ml = 0 in this shell."),
            S("Each orbital holds 2 electrons", math=r"4 \times 2 = 8\ \text{electrons}"),
        ]),
        MISTAKE("Mixing up n and l", "The sub-shell letter depends on l, not n. The 3d sub-shell has n = 3 and l = 2. There is no 2d sub-shell because l cannot be as large as n."),
        MISTAKE("Saying an orbital is an orbit", "An orbit is a path; an orbital is a region of probability. Electrons do not follow circular paths around the nucleus."),
        QUIZ(r"How many orbitals are in the $4d$ sub-shell and how many electrons can it hold?",
             ["1 orbital, 2 electrons", "3 orbitals, 6 electrons", "5 orbitals, 10 electrons", "7 orbitals, 14 electrons"], 2,
             r"For d, $l = 2$, so there are $2l + 1 = 5$ orbitals, holding $5 \times 2 = 10$ electrons.",
             hint="Use 2l + 1 with l = 2.",
             feedback=["This is an s sub-shell (l = 0).", "This is a p sub-shell (l = 1).", "", "This is an f sub-shell (l = 3)."]),
        TIP("Quantum numbers appear in Paper 1 as 'which set is not allowed' items, and in Paper 2 as counting questions. Check each rule in the order l less than n, ml between -l and +l, ms = plus or minus half."),
        PQ(r"State the quantum numbers $n$ and $l$ for the 4p sub-shell, and the number of electrons it holds.",
           r"4p: $n = 4$, $l = 1$. It has $2l + 1 = 3$ orbitals, so it holds 6 electrons."),
        PQ(r"Which of the following sets $(n, l, m_l, m_s)$ is not allowed? (A) $(1, 0, 0, +\tfrac12)$ (B) $(2, 1, -1, -\tfrac12)$ (C) $(3, 3, 0, +\tfrac12)$ (D) $(4, 3, +3, -\tfrac12)$",
           r"(C) is not allowed. For $n = 3$ the largest $l$ is 2, but here $l = 3$. The others satisfy $l \le n - 1$, $|m_l| \le l$ and $m_s = \pm\tfrac12$."),
        PQ(r"Show that the number of orbitals in shell $n = 4$ is $4^2$, and find the maximum number of electrons.",
           r"Sub-shells: 4s (1 orbital), 4p (3), 4d (5), 4f (7). Total $= 1 + 3 + 5 + 7 = 16 = 4^2$. Electrons $= 2 \times 16 = 32 = 2(4)^2$."),
        PQ("Explain in terms of quantum numbers why an orbital cannot hold more than two electrons.",
           "Two electrons in the same orbital have the same n, l and ml. The Pauli exclusion principle forbids two electrons having all four quantum numbers the same, so they must differ in ms. "
           "ms has only two values (+1/2 and -1/2), so a maximum of two electrons can be in one orbital."),
        SUM(r"An orbital is a region of high probability of finding an electron, holding at most 2 electrons of opposite spin.",
            r"$n = 1, 2, 3, \dots$; $l = 0$ to $n - 1$; $m_l = -l$ to $+l$; $m_s = \pm\tfrac12$.",
            r"A sub-shell has $2l + 1$ orbitals (s 1, p 3, d 5, f 7); a shell has $n^2$ orbitals and $2n^2$ electrons.",
            "s orbitals are spherical, p orbitals are dumbbells along x, y and z, and d orbitals are mostly cloverleaf shaped."),
    ],
))

# ------------------------------------------------------------------ 13. Aufbau, Hund, Pauli
LESSONS.append(lesson(
    module=M2,
    topic="Aufbau principle, Hund's rule and the Pauli exclusion principle",
    title="Electronic configurations: Aufbau, Hund and Pauli",
    slug="chl1-aufbau-hund-pauli",
    minutes=25,
    summary="Write electronic configurations and orbital box diagrams for atoms and ions up to krypton, including the chromium and copper exceptions, and count unpaired electrons.",
    objectives=[
        "State the Aufbau principle, Hund's rule and the Pauli exclusion principle",
        "Write full and shorthand configurations of atoms and ions up to Z = 36",
        "Explain the configurations of chromium and copper",
        "Draw orbital box diagrams and count unpaired electrons",
    ],
    key_concepts=["Aufbau principle", "Hund's rule", "Pauli exclusion principle", "Orbital box diagram", "Unpaired electrons", "4s fills before 3d but empties first"],
    blocks=[
        H("Introduction"),
        T("An iron tablet from a pharmacy in Yaounde and the iron roofing sheets of a house in Bamenda both depend on the same fact: iron atoms have four unpaired electrons, which makes iron magnetic and gives its ions their coloured compounds. "
          "Electronic configurations explain such properties. Three rules tell us how to fill the orbitals."),
        KEY("The three rules", "Apply all three every time.", cards=[
            ["Aufbau principle", "Electrons go into the lowest-energy empty orbital first. Order: 1s 2s 2p 3s 3p 4s 3d 4p 5s ..."],
            ["Pauli exclusion principle", "An orbital holds at most two electrons, and they must have opposite spins."],
            ["Hund's rule", "In orbitals of equal energy (such as three p orbitals), electrons occupy them singly with parallel spins before any pairing."],
        ]),
        IMG("al-chl1-box-iron.svg", alt="Orbital box diagram of iron showing paired electrons in 1s to 4s and four unpaired electrons in the 3d boxes",
            caption="Figure 1. Iron: 1s2 2s2 2p6 3s2 3p6 4s2 3d6. The 4s sub-shell is filled first but the 3d boxes sit higher in energy."),
        CODE("""Atom    Z    Configuration                          Shorthand
N       7    1s2 2s2 2p3                            [He] 2s2 2p3
O       8    1s2 2s2 2p4                            [He] 2s2 2p4
K      19    1s2 2s2 2p6 3s2 3p6 4s1                [Ar] 4s1
Fe     26    1s2 2s2 2p6 3s2 3p6 3d6 4s2            [Ar] 3d6 4s2
Cr     24    1s2 2s2 2p6 3s2 3p6 3d5 4s1            [Ar] 3d5 4s1   (exception)
Cu     29    1s2 2s2 2p6 3s2 3p6 3d10 4s1           [Ar] 3d10 4s1  (exception)""", "text", title="Examples (written in shell order; check your textbook for the order your course uses)"),
        T("**Two exceptions.** Chromium has $3d^5 4s^1$, not $3d^4 4s^2$, and copper has $3d^{10} 4s^1$, not $3d^9 4s^2$. A half-filled and a completely filled 3d sub-shell have extra stability because the 3d and 4s energies are very close and electron-electron repulsion is reduced when electrons are spread over more orbitals. "
          "This is an explanation by energy balance; some textbooks give slightly different wording, so check your textbook."),
        KEY("Making ions", "Remove electrons from the highest shell first. For a transition metal, the 4s electrons are lost before the 3d electrons, even though 4s was filled first.", cards=[
            [r"$\mathrm{Fe^{2+}}$", r"$[\mathrm{Ar}]\,3d^6$ (the two 4s electrons go)"],
            [r"$\mathrm{Fe^{3+}}$", r"$[\mathrm{Ar}]\,3d^5$ (half-filled, five unpaired electrons)"],
            [r"$\mathrm{Cu^{2+}}$", r"$[\mathrm{Ar}]\,3d^9$"],
        ]),
        H("Worked examples"),
        EX("Worked example 1: iron and its ions", intro=r"Write the electronic configurations of Fe, Fe$^{2+}$ and Fe$^{3+}$ and give the number of unpaired electrons in each.", steps=[
            S("Fe ($Z = 26$)", math=r"1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,3d^6\,4s^2 = [\mathrm{Ar}]\,3d^6\,4s^2"),
            S("3d box diagram of Fe: six electrons in five boxes", text="One electron in each box first (five unpaired), then the sixth pairs up with one: four unpaired electrons."),
            S(r"Fe$^{2+}$ (lose the two 4s electrons)", math=r"[\mathrm{Ar}]\,3d^6:\ 4\ \text{unpaired}"),
            S(r"Fe$^{3+}$ (lose one more, from 3d)", math=r"[\mathrm{Ar}]\,3d^5:\ 5\ \text{unpaired}"),
        ]),
        EX("Worked example 2: Cr and Cu", intro=r"Write the electronic configuration of chromium ($Z = 24$) and copper ($Z = 29$) and state how many unpaired electrons each has.", steps=[
            S("Chromium", math=r"[\mathrm{Ar}]\,3d^5\,4s^1:\ \text{six unpaired electrons (five in 3d, one in 4s)}"),
            S("Copper", math=r"[\mathrm{Ar}]\,3d^{10}\,4s^1:\ \text{one unpaired electron (the 4s electron)}"),
            S("Why these differ from the pattern", text="A half-filled (3d5) or filled (3d10) sub-shell is lower in energy overall, so one electron moves from 4s to 3d."),
        ]),
        EX("Worked example 3: oxygen and Hund's rule", intro=r"Draw the 2p box diagram of oxygen and explain why oxygen has two unpaired electrons.", steps=[
            S(r"Oxygen has 8 electrons: $1s^2\,2s^2\,2p^4$", text="Four electrons go into three 2p boxes."),
            S("Hund's rule: singly first", text="The first three electrons go one to each of the three 2p orbitals, all with the same spin."),
            S("The fourth pairs up with one of them (opposite spin)", text="Box diagram: (up, down) (up) (up). Unpaired electrons: 2."),
        ]),
        MISTAKE("Removing 3d electrons first from a transition-metal ion", "Although 4s fills before 3d, it is the 4s electrons that are lost first when an ion forms. Fe2+ is [Ar] 3d6, not [Ar] 3d4 4s2."),
        MISTAKE("Pairing electrons too soon", "In a box diagram, put one electron in every orbital of a sub-shell, all pointing the same way, before you pair any. Pairing early breaks Hund's rule."),
        QUIZ(r"Which is the electronic configuration of the $\mathrm{Cu^{2+}}$ ion ($Z = 29$)?",
             [r"$[\mathrm{Ar}]\,3d^{9}$", r"$[\mathrm{Ar}]\,3d^{10}\,4s^{1}$", r"$[\mathrm{Ar}]\,3d^{8}\,4s^{1}$", r"$[\mathrm{Ar}]\,3d^{7}\,4s^{2}$"], 0,
             r"Copper is $[\mathrm{Ar}]\,3d^{10}\,4s^1$. To form 2+, remove the 4s electron first, then one 3d electron, leaving $[\mathrm{Ar}]\,3d^9$.",
             hint="Start with the copper atom, then remove electrons from 4s first.",
             feedback=["", "This is the copper atom (or the Cu+ ion if the 4s electron is removed); Cu2+ has lost two electrons.",
                       "This keeps a 4s electron and removes two from 3d; the 4s electron is lost first.", "This keeps the 4s pair and removes two from 3d, the wrong order: the 4s electrons go first."]),
        TIP("Configurations come up in Paper 1 (count unpaired electrons, pick the correct ion) and Paper 2 (write the configuration and explain Cr, Cu). Keep the 4s-before-3d filling order but lose the 4s first."),
        PQ(r"Write the electronic configurations of (a) $\mathrm{Cl^-}$ and (b) $\mathrm{K}$, in the form 1s2 ... ",
           r"(a) $\mathrm{Cl}$ has 17 electrons; $\mathrm{Cl^-}$ has 18: $1s^2\,2s^2\,2p^6\,3s^2\,3p^6$. (b) $\mathrm{K}$ has 19 electrons: $1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^1$. Note that $\mathrm{Cl^-}$ and K+ have the same configuration as argon."),
        PQ(r"How many unpaired electrons are in (a) $\mathrm{Mn^{2+}}$ and (b) $\mathrm{Ni^{2+}}$? ($Z$: Mn 25, Ni 28)",
           r"(a) Mn is $[\mathrm{Ar}]\,3d^5\,4s^2$; Mn$^{2+}$ loses the 4s pair: $3d^5$, five unpaired electrons. (b) Ni is $[\mathrm{Ar}]\,3d^8\,4s^2$; Ni$^{2+}$ is $3d^8$: three 3d orbitals are paired and two have a single electron, so two unpaired."),
        PQ("State the three rules used to build an electronic configuration, and say which one is broken if two electrons in the same p orbital have the same spin.",
           "Aufbau: lowest-energy orbitals first. Pauli: at most two electrons per orbital, with opposite spins. Hund: singly occupy equal-energy orbitals with parallel spins before pairing. Two electrons in one orbital with the same spin break the Pauli exclusion principle."),
        PQ(r"Explain why chromium is $[\mathrm{Ar}]\,3d^5\,4s^1$ rather than $[\mathrm{Ar}]\,3d^4\,4s^2$.",
           r"The 3d and 4s energies are very close. With $3d^5\,4s^1$ each of the six outer orbitals has a single electron, which minimises electron-electron repulsion and gives a half-filled 3d sub-shell. This arrangement is lower in energy overall, so one 4s electron moves into 3d."),
        SUM("Aufbau: fill lowest energy first (1s 2s 2p 3s 3p 4s 3d 4p). Pauli: maximum two electrons per orbital, opposite spins. Hund: single occupancy first, parallel spins.",
            "Cr is 3d5 4s1 and Cu is 3d10 4s1 because half-filled and filled 3d sub-shells are favoured.",
            "In ions of transition metals, the 4s electrons are lost before the 3d electrons.",
            "Unpaired electrons are counted from the box diagram: they cause paramagnetism and coloured compounds."),
    ],
))


# ------------------------------------------------------------------ 14. Ionic bonding and polarisation
LESSONS.append(lesson(
    module=M3,
    topic="Ionic bonding and polarization",
    title="Ionic bonding and polarisation (Fajans' rules)",
    slug="chl1-ionic-bonding-polarisation",
    minutes=23,
    summary="Describe ionic lattices and their properties, and use Fajans' rules and the charge density of the cation to predict when an ionic bond has covalent character.",
    objectives=[
        "Describe ionic bonding and the properties that follow from the giant ionic lattice",
        "Define polarisation and polarising power and state Fajans' rules",
        "Rank cations by charge density and anions by polarisability",
        "Use polarisation to explain differences in melting point, solubility and thermal stability",
    ],
    key_concepts=["Ionic bond", "Giant ionic lattice", "Polarising power", "Polarisability", "Fajans' rules", "Covalent character"],
    blocks=[
        H("Introduction"),
        T("Kitchen salt, sodium chloride, melts at 801 degrees Celsius. Aluminium chloride, made from a metal and the same chlorine, turns to vapour at about 180 degrees Celsius. "
          "Both are compounds of a metal and chlorine, so why do they behave so differently? The answer is that no ionic bond is 100% ionic. The size and charge of the ions decide how far the "
          "bond is shifted towards covalent."),
        D("An **ionic bond** is the electrostatic attraction between oppositely charged ions. In a **giant ionic lattice** each ion is surrounded by ions of the opposite charge in all directions, so the attraction acts throughout the crystal.", title="Definition: ionic bonding"),
        KEY("Properties that follow from the lattice", "Each property is explained by the strong, long-range attraction.", cards=[
            ["High melting point", "A lot of energy is needed to overcome the strong attractions in all directions."],
            ["Hard but brittle", "A blow slides one layer so that like charges meet and repel, and the crystal cleaves."],
            ["Conducts when molten or dissolved", "The ions are free to move. In the solid they are held in fixed positions."],
            ["Often soluble in water", "Polar water molecules attract the ions and pull them out of the lattice (see the hydration of ions)."],
        ]),
        H("Polarisation of ions"),
        T("A small, highly charged cation attracts the electron cloud of a neighbouring anion. The cloud is pulled towards the cation, so some electron density is shared in the region between the two nuclei: the bond acquires **covalent character**."),
        IMG("al-chl1-polarisation.svg", alt="Two panels: a small distortion of a large anion by a low-charge cation, and a large distortion by a small highly charged cation",
            caption="Figure 1. Polarisation: a small 3+ cation pulls the large anion's cloud towards it."),
        D("**Polarising power** is the ability of a cation to distort the electron cloud of an anion. **Polarisability** is the ease with which an anion's electron cloud can be distorted.", title="Definitions"),
        KEY("Fajans' rules: covalent character increases when", "These are the usual statements; textbooks list them in slightly different orders.", cards=[
            ["1. Cation", r"is small (small radius) and has a high charge, so it has a high charge density ($\text{charge} / \text{radius}$)."],
            ["2. Anion", "is large (the outer electrons are far from the nucleus and held loosely) and has a high charge."],
            ["3. Cation type", "has a non-noble-gas electron configuration (for example Ag+ or Cu+ polarise more than Na+ of similar size). Check your textbook."],
        ]),
        CODE("""Ion     Charge   Radius (pm)   Charge/radius (e per nm)
Na+     1+       102           9.8
Mg2+    2+       72            27.8
Al3+    3+       54            55.6
Li+     1+       76            13.2
K+      1+       138           7.3
(rounded teaching values: check your textbook)
Anion radii (pm): F- 133, Cl- 181, Br- 196, I- 220""", "text", title="Charge density of cations"),
        H("Worked examples"),
        EX("Worked example 1: ranking cations", intro=r"Arrange $\mathrm{Na^+}$, $\mathrm{Mg^{2+}}$ and $\mathrm{Al^{3+}}$ in order of polarising power, and say what this does to the bonding in their chlorides.", steps=[
            S("Charge density from the table", math=r"\mathrm{Na^+}: \frac{1}{0.102} = 9.8;\quad \mathrm{Mg^{2+}}: \frac{2}{0.072} = 27.8;\quad \mathrm{Al^{3+}}: \frac{3}{0.054} = 55.6\ \text{(e per nm)}"),
            S("Order", text="Al3+ > Mg2+ > Na+. The ions are isoelectronic (10 electrons), so size and charge alone decide it."),
            S("Effect on the chlorides", text="NaCl is ionic (mp 801 C), MgCl2 is mainly ionic (mp 714 C), and AlCl3 has strong covalent character and sublimes at about 180 C (it forms Al2Cl6 molecules in the vapour)."),
        ]),
        EX("Worked example 2: anions", intro=r"Which has the greater covalent character, lithium chloride or lithium iodide? Explain.", steps=[
            S("The cation is the same (Li+)", text="So the difference comes from the anion."),
            S("Compare the anions", text="I- (220 pm) is larger than Cl- (181 pm). Its outer electrons are farther from the nucleus and more shielded, so its cloud is more easily pulled out of shape."),
            S("Conclusion", text="LiI has more covalent character than LiCl. The same trend is seen in the silver halides, where AgI is the least ionic and the least soluble."),
        ]),
        EX("Worked example 3: thermal stability of carbonates", intro=r"Magnesium carbonate decomposes at a much lower temperature than barium carbonate. Use polarisation to explain.", steps=[
            S("Equation", math=r"\mathrm{MgCO_3(s) \rightarrow MgO(s) + CO_2(g)}"),
            S("Cation size", text="Mg2+ (72 pm) is much smaller than Ba2+ (135 pm), so its charge density is higher."),
            S("Effect on the carbonate ion", text="Mg2+ polarises the carbonate ion strongly, distorting one C-O bond so it breaks easily to release CO2. Ba2+ polarises it much less, so more heat is needed."),
        ]),
        MISTAKE("Saying 'smaller anion means more polarisation'", "It is the cation that polarises and the anion that is polarised. The larger the anion, the easier its cloud is distorted. Learn which ion is which in each statement."),
        MISTAKE("Using only ionic radius", "Charge matters as much as size. Al3+ is smaller than Mg2+ and also has a higher charge, so it is the most polarising of the three, not Na+."),
        QUIZ("Which compound is likely to have the most covalent character?",
             ["NaF", "NaCl", "AlCl3", "MgO"], 2,
             "Al3+ has the highest charge density, and chloride is larger and more polarisable than fluoride or oxide, so AlCl3 shows the most covalent character. MgO is strongly ionic because both ions are small and not easily distorted.",
             hint="Look for the smallest, most highly charged cation, bonded to a large anion.",
             feedback=["Na+ has low charge density and F- is small and hard to polarise.", "Na+ is a weakly polarising cation, so NaCl is mainly ionic.", "",
                       "Both Mg2+ and O2- are small, and MgO has a very high melting point typical of a strongly ionic lattice."]),
        TIP("Polarisation is used in Paper 2 to explain melting points, solubility and the thermal stability of Group 2 carbonates and nitrates, and it appears in Paper 1 as comparison items. Use the words 'charge density' and 'distorts the electron cloud'."),
        PQ(r"Calculate the charge-to-radius ratio of $\mathrm{K^+}$ (138 pm) and $\mathrm{Ca^{2+}}$ (100 pm) in e per nm and say which polarises more.",
           r"$\mathrm{K^+}$: $1/0.138 = 7.25$ e per nm. $\mathrm{Ca^{2+}}$: $2/0.100 = 20.0$ e per nm. $\mathrm{Ca^{2+}}$ has the higher ratio, so it is the stronger polarising cation."),
        PQ("Explain why the melting point of aluminium chloride (it sublimes at about 180 C) is much lower than that of sodium chloride (801 C).",
           "Al3+ is small and highly charged, so it polarises the chloride ion and the bonding has considerable covalent character; AlCl3 forms simple molecules (Al2Cl6) with weak forces between them. "
           "Na+ is larger with a 1+ charge, so NaCl is a giant ionic lattice with strong electrostatic attractions in all directions."),
        PQ("Arrange the lithium halides LiF, LiCl, LiBr and LiI in order of increasing covalent character and explain.",
           "LiF < LiCl < LiBr < LiI. The cation is the same, so the trend depends on the anion: the larger the halide ion, the more polarisable its electron cloud, and the more covalent character the bond has."),
        PQ("Explain why an ionic solid does not conduct electricity but its melt does.",
           "In the solid, ions are fixed in the lattice and cannot move. When molten the ions are free to move and carry charge, so the liquid conducts."),
        SUM("An ionic lattice gives high melting points, brittleness, and conduction only when ions can move (molten or dissolved).",
            "Polarising power depends on cation charge density (charge / radius); polarisability is greatest for large, highly charged anions.",
            "More polarisation means more covalent character, e.g. AlCl3, LiI and AgI.",
            "Polarisation explains the lower thermal stability of MgCO3 than BaCO3."),
    ],
))

# ------------------------------------------------------------------ 15. Covalent bonding and VSEPR
LESSONS.append(lesson(
    module=M3,
    topic="Covalent bonding and VSEPR shapes",
    title="Covalent bonding and VSEPR shapes",
    slug="chl1-covalent-bonding-vsepr",
    minutes=26,
    summary="Use dot-and-cross ideas, dative bonds and electron-pair repulsion theory to predict the shapes and bond angles of molecules and ions with two to six electron pairs.",
    objectives=[
        "Describe a covalent bond, a dative covalent bond and the exceptions to the octet rule",
        "State the VSEPR rules, including the order of repulsion between lone pairs and bond pairs",
        "Predict the shapes and bond angles of molecules and ions with up to six electron pairs",
        "Explain why bond angles in CH4, NH3 and H2O decrease",
    ],
    key_concepts=["Covalent bond", "Dative bond", "Expanded octet", "VSEPR theory", "Lone pair", "Bond angle", "Molecular shape"],
    blocks=[
        H("Introduction"),
        T("The cooking gas used in many Cameroonian homes is mainly butane, a covalent molecule. Water, ammonia in fertiliser and carbon dioxide from fermentation are all covalent too. "
          "Their properties depend on their shapes: water is bent, which makes it polar and a good solvent; carbon dioxide is linear, which makes it non-polar. "
          "The VSEPR model predicts these shapes from simple counting."),
        D("A **covalent bond** is the electrostatic attraction between the nuclei of two atoms and a shared pair of electrons between them. A **dative covalent bond** is a covalent bond in which both shared electrons come from one atom (the donor), as in the ammonium ion, $\\mathrm{NH_4^+}$, formed when $\\mathrm{NH_3}$ donates its lone pair to $\\mathrm{H^+}$.", title="Definitions"),
        KEY("Exceptions to the octet rule", "The octet rule works for many molecules but there are three kinds of exception.", cards=[
            ["Fewer than 8", "BeCl2 (4 electrons around Be) and BF3 (6 around B) are electron deficient."],
            ["More than 8 (expanded octet)", "Atoms in Period 3 and below can hold more: PCl5 (10 around P), SF6 (12 around S)."],
            ["Odd number of electrons", "NO has 11 valence electrons, so one atom cannot have an octet."],
        ]),
        H("VSEPR theory"),
        D("**Valence shell electron-pair repulsion (VSEPR) theory**: pairs of electrons in the outer shell of the central atom repel each other and take positions as far apart as possible. "
          "The shape is named from the arrangement of the **atoms**, not the lone pairs.", title="VSEPR theory"),
        KEY("Order of repulsion", "This explains why angles shrink when lone pairs are present.", cards=[
            ["Strongest", "lone pair - lone pair"],
            ["Middle", "lone pair - bond pair"],
            ["Weakest", "bond pair - bond pair"],
        ]),
        T(r"A multiple bond (double or triple) counts as **one region** of electron density in VSEPR. To find the number of electron pairs on the central atom: add the central atom's valence electrons to one for every single-bonded atom (zero for a doubly bonded atom such as O), "
          r"subtract the charge for a positive ion or add it for a negative ion, then divide by 2."),
        IMG("al-chl1-vsepr-tetrahedral.svg", alt="Methane, ammonia and water drawn with wedge and dashed bonds and lone pairs, showing tetrahedral, pyramidal and bent shapes",
            caption="Figure 1. Four electron pairs: the arrangement is tetrahedral, but the shape depends on how many pairs are lone pairs."),
        CODE("""Pairs  Lone  Shape                  Ideal angle      Examples
2      0     linear                 180              BeCl2, CO2
3      0     trigonal planar        120              BF3, NO3-
3      1     bent                   about 119        SO2
4      0     tetrahedral            109.5            CH4, NH4+, SO4 2-
4      1     trigonal pyramidal     107 (NH3)        NH3, H3O+, PCl3
4      2     bent (V-shaped)        104.5 (H2O)      H2O, SCl2
5      0     trigonal bipyramidal   90 and 120       PCl5
5      1     see-saw                about 90 and 120 SF4
5      2     T-shaped               about 90         ClF3
5      3     linear                 180              XeF2
6      0     octahedral             90               SF6
6      1     square pyramidal       about 90         BrF5
6      2     square planar          90               XeF4, ICl4-""", "text", title="Shapes from two to six electron pairs"),
        IMG("al-chl1-vsepr-5-pairs.svg", alt="Trigonal bipyramidal PCl5, see-saw SF4, T-shaped ClF3 and linear XeF2",
            caption="Figure 2. Five electron pairs: lone pairs occupy equatorial positions, where there is more room."),
        IMG("al-chl1-vsepr-6-pairs.svg", alt="Octahedral SF6, square pyramidal BrF5 and square planar XeF4",
            caption="Figure 3. Six electron pairs: lone pairs go opposite each other, giving the square planar shape for XeF4."),
        H("Worked examples"),
        EX("Worked example 1: ammonia and water", intro=r"Predict the shape and bond angle of $\mathrm{NH_3}$ and $\mathrm{H_2O}$.", steps=[
            S("NH3: five valence electrons on N plus three H", math=r"\frac{5 + 3}{2} = 4\ \text{pairs: 3 bond pairs and 1 lone pair}"),
            S("Shape and angle", text="Tetrahedral arrangement, trigonal pyramidal shape, bond angle about 107 degrees (less than 109.5 because the lone pair repels more than a bond pair)."),
            S("H2O: six valence electrons on O plus two H", math=r"\frac{6 + 2}{2} = 4\ \text{pairs: 2 bond pairs and 2 lone pairs}"),
            S("Shape and angle", text="Bent (V-shaped), about 104.5 degrees. Two lone pairs push the bond pairs closer than one does in NH3."),
        ]),
        EX("Worked example 2: SF4 and XeF4", intro=r"Predict the shapes of $\mathrm{SF_4}$ and $\mathrm{XeF_4}$.", steps=[
            S("SF4: S has 6 valence electrons, four F", math=r"\frac{6 + 4}{2} = 5\ \text{pairs: 4 bond pairs, 1 lone pair}"),
            S("Place the lone pair equatorial", text="Trigonal bipyramidal arrangement; the shape is see-saw."),
            S("XeF4: Xe has 8 valence electrons, four F", math=r"\frac{8 + 4}{2} = 6\ \text{pairs: 4 bond pairs, 2 lone pairs}"),
            S("Put the lone pairs opposite each other", text="Octahedral arrangement; the shape is square planar, with 90 degree F-Xe-F angles."),
        ]),
        EX("Worked example 3: ammonium ion and a dative bond", intro=r"Describe the bonding and shape of the ammonium ion, $\mathrm{NH_4^+}$.", steps=[
            S("Formation", math=r"\mathrm{NH_3 + H^+ \rightarrow NH_4^+}"),
            S("Dative bond", text="The N atom donates its lone pair to the empty 1s orbital of H+. Once formed, all four N-H bonds are identical."),
            S("Electron pairs", math=r"\frac{5 + 4 - 1}{2} = 4\ \text{pairs, all bonding}"),
            S("Shape", text="Tetrahedral, with H-N-H angles of 109.5 degrees."),
        ], check=r"\mathrm{NH_3 + H^+ \rightarrow NH_4^+}:\ \text{N: 1 on each side; H: 4 on each side; charge: +1 on each side}"),
        MISTAKE("Naming the shape from the electron pairs", "Water has four electron pairs (tetrahedral arrangement) but its shape is bent, because only the positions of atoms count in the name. NH3 is pyramidal, not tetrahedral."),
        MISTAKE("Using 109.5 degrees for NH3 and H2O", "Lone pairs repel more than bond pairs, so the angles close up: 107 degrees in NH3 and 104.5 degrees in H2O. State the reason when you give a value."),
        QUIZ(r"What is the shape of the $\mathrm{ICl_4^-}$ ion? (I has 7 valence electrons)",
             ["Tetrahedral", "See-saw", "Square planar", "Octahedral"], 2,
             r"$\frac{7 + 4 + 1}{2} = 6$ pairs: 4 bond pairs and 2 lone pairs. The lone pairs sit opposite each other, so the shape is square planar.",
             hint="Add the charge for a negative ion before halving.",
             feedback=["This would need four pairs; ICl4- has six.", "This is for five pairs with one lone pair (such as SF4).", "",
                       "An octahedral molecule has six bond pairs and no lone pairs (such as SF6); here two of the six are lone pairs."]),
        TIP("VSEPR questions are among the most predictable parts of Papers 1 and 2: state the number of bond pairs and lone pairs, name the shape, give the angle and give one reason. Draw 3D shapes with wedge and dash bonds."),
        PQ(r"Predict the shape and approximate bond angle of (a) $\mathrm{BF_3}$ and (b) $\mathrm{PCl_3}$.",
           r"(a) B: $\frac{3 + 3}{2} = 3$ pairs, all bonding: trigonal planar, $120^{\circ}$. (b) P: $\frac{5 + 3}{2} = 4$ pairs: 3 bond pairs and 1 lone pair, trigonal pyramidal, a little under $109.5^{\circ}$ because the lone pair repels the bond pairs."),
        PQ("Explain why the bond angles in CH4, NH3 and H2O are 109.5, 107 and 104.5 degrees respectively.",
           "All three have four pairs of electrons around the central atom, arranged tetrahedrally. In CH4 all four are bond pairs, which repel equally, so the angle is 109.5 degrees. In NH3 one pair is a lone pair, which repels the bond pairs more strongly than they repel each other, closing the angle to 107 degrees. "
           "In H2O there are two lone pairs, which squeeze the bond pairs further, to 104.5 degrees."),
        PQ(r"Predict the shapes of $\mathrm{CO_2}$ and $\mathrm{SO_2}$ and explain the difference. (C has 4 valence electrons, S has 6; treat each O as doubly bonded)",
           r"$\mathrm{CO_2}$: $\frac{4 + 0}{2} = 2$ regions, no lone pairs: linear, $180^{\circ}$. $\mathrm{SO_2}$: $\frac{6 + 0}{2} = 3$ regions: 2 bond regions and 1 lone pair, so bent (about $119^{\circ}$). Sulfur has a lone pair; carbon does not."),
        PQ(r"Draw or describe the dative bond that forms when ammonia reacts with boron trifluoride, $\mathrm{NH_3 + BF_3 \rightarrow H_3N{\rightarrow}BF_3}$, and say why it forms.",
           r"BF3 has only six electrons around B, so it has an empty orbital. The N atom of NH3 donates its lone pair into this empty orbital, forming a dative covalent bond (shown by an arrow from N to B). The product has four pairs around each of N and B, so each is tetrahedral."),
        SUM("A covalent bond is a shared pair of electrons; in a dative bond both electrons come from one atom.",
            "VSEPR: electron pairs repel and spread out; lone pair - lone pair repulsion is greater than lone pair - bond pair, which is greater than bond pair - bond pair.",
            r"Number of pairs on the central atom = (valence electrons + single-bonded atoms - charge) / 2; shape is named from the atoms only.",
            "Shapes: 2 linear, 3 trigonal planar, 4 tetrahedral (pyramidal, bent), 5 trigonal bipyramid (see-saw, T-shape, linear), 6 octahedral (square pyramid, square planar)."),
    ],
))


# ------------------------------------------------------------------ 16. Sigma and pi bonds, hybridisation
LESSONS.append(lesson(
    module=M3,
    topic="Sigma and pi bonds and hybridization",
    title="Sigma and pi bonds, and sp3, sp2 and sp hybridisation",
    slug="chl1-sigma-pi-hybridisation",
    minutes=25,
    summary="Describe sigma and pi bonds as end-on and sideways overlap of orbitals, count them in molecules, and use sp3, sp2 and sp hybridisation to explain shapes and bond angles.",
    objectives=[
        "Distinguish sigma and pi bonds by the way orbitals overlap",
        "Count sigma and pi bonds in single, double and triple bonds and in molecules",
        "Explain sp3, sp2 and sp hybridisation and the resulting angles",
        "Deduce the hybridisation of an atom from its sigma bonds and lone pairs",
    ],
    key_concepts=["Sigma bond", "Pi bond", "Hybridisation", "sp3, sp2 and sp orbitals", "Restricted rotation", "Bond length and strength"],
    blocks=[
        H("Introduction"),
        T("Ethene, made by ripening fruit, is the plant hormone that turns green plantains and bananas yellow in a market stall in Limbe. Ethane, a different gas from natural gas, does not do that. "
          "The reason lies in the bonds between the carbon atoms: ethene has a double bond and ethane a single bond. This lesson explains what a double bond really is, "
          "and why carbon can make bonds at 109.5, 120 and 180 degrees."),
        D("A **sigma ($\\sigma$) bond** is formed by the end-on (head-on) overlap of two orbitals along the line joining the two nuclei. The electron density is concentrated between the nuclei and the bond is cylindrically symmetrical about the bond axis.", title="Definition: sigma bond"),
        D("A **pi ($\\pi$) bond** is formed by the sideways overlap of two parallel p orbitals. The electron density is in two regions, above and below the line joining the nuclei, with a node in the plane of the nuclei.", title="Definition: pi bond"),
        IMG("al-chl1-sigma-pi-ethene.svg", alt="Ethene with a sigma bond along the C-C axis and a pi bond as two lobes above and below the molecular plane",
            caption="Figure 1. Ethene: one sigma bond and one pi bond between the carbons. The molecule is flat."),
        KEY("Counting rules", "Every bond contains exactly one sigma bond. Extra bonds are pi bonds.", cards=[
            ["Single bond", "1 sigma"],
            ["Double bond", "1 sigma + 1 pi"],
            ["Triple bond", "1 sigma + 2 pi"],
        ]),
        T("A pi bond is weaker than a sigma bond because the sideways overlap is less effective, but a double bond is stronger and shorter than a single bond. "
          "Typical values: C-C 154 pm and about 347 kJ/mol; C=C 134 pm and about 614 kJ/mol; C-C triple 120 pm and about 839 kJ/mol (check your textbook for exact figures)."),
        T("Pi bonds also explain **restricted rotation**. Turning one end of a C=C bond would break the sideways overlap, so it cannot rotate freely at room temperature. This is why alkenes can have cis and trans (geometric) isomers, which you will meet in organic chemistry."),
        H("Hybridisation"),
        D("**Hybridisation** is the mixing of atomic orbitals of one atom to form the same number of new, equivalent hybrid orbitals, which then overlap with other atoms' orbitals. "
          "It is a model that explains why the bonds of carbon in methane are all equal and point at 109.5 degrees.", title="Definition: hybridisation"),
        CODE("""Hybrid  Orbitals mixed   Number   Angle      Shape           Example
sp3     one s + three p  4        109.5      tetrahedral     CH4, C2H6, NH3, H2O
sp2     one s + two p    3        120        trigonal planar C2H4, BF3, C6H6, HCHO
sp      one s + one p    2        180        linear          C2H2, CO2, HCN, BeCl2""", "text", title="The three common types"),
        KEY("Finding the hybridisation quickly", "Count the regions of electron density on the atom: the number of sigma bonds plus the number of lone pairs.", cards=[
            ["4 regions", "sp3"],
            ["3 regions", "sp2"],
            ["2 regions", "sp"],
        ]),
        T(r"In methane the carbon atom promotes one 2s electron into a 2p orbital to give four unpaired electrons, then mixes one 2s and three 2p orbitals into four equivalent $sp^3$ hybrids. "
          r"In ethene each carbon mixes one 2s and two 2p orbitals into three $sp^2$ hybrids (in one plane, at 120 degrees) leaving one unmixed p orbital at right angles to the plane. "
          r"In ethyne each carbon mixes one 2s and one 2p orbital into two $sp$ hybrids (180 degrees) leaving two unmixed p orbitals, which form the two pi bonds."),
        H("Worked examples"),
        EX("Worked example 1: counting sigma and pi bonds", intro=r"Count the sigma and pi bonds in (a) propene, $\mathrm{CH_3CH{=}CH_2}$, (b) hydrogen cyanide, $\mathrm{H{-}C{\equiv}N}$, (c) ethanal, $\mathrm{CH_3CHO}$.", steps=[
            S("(a) Propene", math=r"\text{C-H: 6};\ \text{C-C: 1};\ \text{C=C: 1 sigma + 1 pi} \;\Rightarrow\; 8\ \sigma,\ 1\ \pi"),
            S("(b) HCN", math=r"\text{H-C: 1 sigma};\ \text{C}{\equiv}\text{N: 1 sigma + 2 pi} \;\Rightarrow\; 2\ \sigma,\ 2\ \pi"),
            S("(c) Ethanal", math=r"\text{C-H: 4};\ \text{C-C: 1};\ \text{C=O: 1 sigma + 1 pi} \;\Rightarrow\; 6\ \sigma,\ 1\ \pi"),
        ]),
        EX("Worked example 2: hybridisation of each atom", intro=r"State the hybridisation of the underlined atom: (a) C in $\mathrm{CO_2}$, (b) B in $\mathrm{BF_3}$, (c) N in $\mathrm{NH_3}$, (d) O in $\mathrm{H_2O}$, (e) the carbonyl C in $\mathrm{CH_3COCH_3}$.", steps=[
            S("(a) C in CO2", text="Two sigma bonds, no lone pairs: 2 regions, sp (linear)."),
            S("(b) B in BF3", text="Three sigma bonds, no lone pairs: 3 regions, sp2 (trigonal planar)."),
            S("(c) N in NH3", text="Three sigma bonds + one lone pair: 4 regions, sp3."),
            S("(d) O in H2O", text="Two sigma bonds + two lone pairs: 4 regions, sp3."),
            S("(e) C=O carbon in propanone", text="Two C-C sigma bonds + one C=O sigma bond: 3 regions, sp2 (the pi bond is not counted)."),
        ]),
        EX("Worked example 3: shape and bond angles of ethyne", intro=r"Describe the bonding in ethyne, $\mathrm{C_2H_2}$, and state its shape.", steps=[
            S("Each carbon has two sigma bonds (one to H, one to the other C)", text="So each carbon is sp hybridised (2 regions)."),
            S("The two unmixed p orbitals on each carbon", text="They overlap sideways in two perpendicular planes to give two pi bonds."),
            S("Bond count and shape", math=r"3\ \sigma\ (\text{C-H} \times 2,\ \text{C-C}\times1)\ \text{and}\ 2\ \pi;\quad \text{linear, H-C-C angle } 180^{\circ}"),
        ]),
        MISTAKE("Counting a double bond as two sigma bonds", "A double bond is one sigma and one pi. When you work out hybridisation, count only the sigma bonds and lone pairs, so a C=C carbon with three sigma bonds is sp2."),
        MISTAKE("Saying pi bonds are formed from hybrid orbitals", "Pi bonds are formed from the unhybridised p orbitals left over. Hybrid orbitals make the sigma framework."),
        QUIZ("How many sigma and pi bonds are in a molecule of ethene, C2H4?",
             ["4 sigma, 2 pi", "5 sigma, 1 pi", "6 sigma, 0 pi", "3 sigma, 2 pi"], 1,
             "Four C-H bonds (4 sigma) plus a C=C double bond (1 sigma and 1 pi) give 5 sigma and 1 pi.",
             hint="Count the C-H bonds first, then the C=C bond.",
             feedback=["This counts only four bonds from the hydrogens and treats the double bond as two pi bonds.", "",
                       "This treats every bond as sigma; the second bond in a double bond is pi.", "This is the count for ethyne, C2H2."]),
        TIP("Hybridisation, sigma and pi bonds feature in Paper 1 (counting, matching) and Paper 2 (explaining shapes and restricted rotation). Always count sigma bonds and lone pairs to state the hybridisation."),
        PQ(r"Count the sigma and pi bonds in acrylonitrile, $\mathrm{CH_2{=}CH{-}C{\equiv}N}$.",
           r"C-H: 3 sigma. C=C: 1 sigma + 1 pi. C-C: 1 sigma. C$\equiv$N: 1 sigma + 2 pi. Total: 6 sigma and 3 pi."),
        PQ(r"State the hybridisation of each carbon in propanone, $\mathrm{CH_3COCH_3}$, and the C-C-C bond angle.",
           r"The two methyl carbons each have four sigma bonds: $sp^3$. The carbonyl carbon has three sigma bonds (two C-C, one C=O) and one pi bond: $sp^2$. The C-C-C angle is about $120^{\circ}$ (trigonal planar at the carbonyl carbon)."),
        PQ("Explain why ethene is a planar molecule and why there is no free rotation about its C=C bond.",
           "Each carbon is sp2 hybridised, so its three sigma bonds lie in one plane at about 120 degrees. The unhybridised p orbitals overlap sideways above and below this plane to form the pi bond. "
           "Rotating one carbon about the C=C axis would twist the p orbitals out of alignment and break the pi bond, so rotation does not occur at room temperature."),
        PQ("Why is the C-C bond in ethyne (120 pm) shorter and stronger than that in ethane (154 pm)?",
           "The triple bond has one sigma and two pi bonds, so more electron density between the nuclei pulls them closer and holds them more strongly. In addition, sp hybrid orbitals have more s character, so they are held closer to the nucleus than sp3 orbitals."),
        SUM("Sigma bonds form by end-on overlap; pi bonds form by sideways overlap of parallel p orbitals. Double = 1 sigma + 1 pi; triple = 1 sigma + 2 pi.",
            "Hybridisation mixes atomic orbitals into equal hybrid orbitals: sp3 (109.5), sp2 (120) and sp (180).",
            "Hybridisation = number of sigma bonds + lone pairs on the atom (4 sp3, 3 sp2, 2 sp).",
            "Pi bonds restrict rotation, which is the origin of cis-trans isomerism."),
    ],
))

# ------------------------------------------------------------------ 17. Metallic bonding
LESSONS.append(lesson(
    module=M3,
    topic="Metallic bonding",
    title="Metallic bonding and the properties of metals",
    slug="chl1-metallic-bonding",
    minutes=21,
    summary="Describe metallic bonding as positive ions in a sea of delocalised electrons and use it to explain conduction, malleability, melting points and the strengthening effect of alloying.",
    objectives=[
        "Describe metallic bonding and draw the model",
        "Explain electrical and thermal conductivity, malleability and ductility",
        "Explain trends in melting point using ion charge, ion size and number of delocalised electrons",
        "Explain why alloys are harder than pure metals",
    ],
    key_concepts=["Metallic bond", "Delocalised electrons", "Malleability", "Metallic melting point trends", "Alloy"],
    blocks=[
        H("Introduction"),
        T("A copper wire carries electricity into a house in Garoua, and an aluminium pot sits on a cooking-gas flame in Douala. Both metals conduct, both can be shaped without breaking, "
          "and neither is brittle like salt. Metallic bonding explains all of these facts with one model."),
        D("A **metallic bond** is the electrostatic attraction between the positive metal ions in a lattice and the delocalised (free-moving) outer electrons that surround them.", title="Definition: metallic bonding"),
        IMG("al-chl1-metallic-bonding.svg", alt="Regular lattice of positive ions with amber dots for delocalised electrons moving between them",
            caption="Figure 1. Metallic bonding: a lattice of positive ions in a sea of delocalised electrons."),
        KEY("Properties explained", "Each one follows from the model.", cards=[
            ["Electrical conduction", "Delocalised electrons are free to move through the lattice when a potential difference is applied."],
            ["Thermal conduction", "Mobile electrons and vibrating ions pass kinetic energy quickly through the metal."],
            ["Malleable and ductile", "Layers of ions slide over one another and the electron sea keeps the lattice bonded, so the metal changes shape without breaking."],
            ["High melting point and boiling point", "Strong attraction between the ions and the electron sea must be overcome (and the larger the attraction, the higher the melting point)."],
            ["Lustre", "Free electrons absorb and re-emit light at the surface."],
        ]),
        H("What makes a metallic bond stronger?"),
        T("Three factors increase the strength of metallic bonding. A higher **charge** on the ion (more delocalised electrons per atom), a **smaller ionic radius** (the electrons are closer to the nuclei), and a larger number of delocalised electrons per unit volume."),
        CODE("""Metal   Outer electrons (delocalised)   Ion    Radius (pm)   Melting point (C)
Na      1                              Na+    102           98
Mg      2                              Mg2+   72            650
Al      3                              Al3+   54            660
Li      1                              Li+    76            181
K       1                              K+     138           63
Cs      1                              Cs+    167           28.5
(rounded teaching values: check your textbook)""", "text", title="Melting points and ion data"),
        T("Transition metals have very high melting points because the 3d and 4s electrons are all available for bonding. Mercury is a liquid at room temperature because of weak metallic bonding in its atoms. "
          "Textbooks differ in how they explain this, so check your textbook."),
        H("Worked examples"),
        EX("Worked example 1: Na, Mg and Al", intro=r"Explain why the melting point rises from sodium (98 C) to magnesium (650 C) and aluminium (660 C).", steps=[
            S("Delocalised electrons per atom", math=r"\mathrm{Na}: 1;\quad \mathrm{Mg}: 2;\quad \mathrm{Al}: 3"),
            S("Ionic radius", math=r"\mathrm{Na^+}\ 102\ \mathrm{pm} > \mathrm{Mg^{2+}}\ 72\ \mathrm{pm} > \mathrm{Al^{3+}}\ 54\ \mathrm{pm}"),
            S("Explain", text="From Na to Al the ion has a higher charge, is smaller, and there are more delocalised electrons. So the attraction between ions and the electron sea grows, and more energy is needed to melt the metal."),
        ]),
        EX("Worked example 2: Group 1", intro=r"Explain why the melting point falls from lithium (181 C) to caesium (28.5 C).", steps=[
            S("Same charge, same number of delocalised electrons", text="Each atom provides one delocalised electron and forms a 1+ ion."),
            S("Radius increases", text="Down the group the ions are larger (76 pm to 167 pm), so the delocalised electrons are farther from the positive nuclei."),
            S("Explain", text="The attraction weakens, so the metallic bond is weaker and the melting point is lower."),
        ]),
        EX("Worked example 3: counting delocalised electrons", intro=r"How many delocalised electrons are contributed by 2.7 g of aluminium? ($A_r$ of Al = 27; $L = 6.02\times10^{23}\ \mathrm{mol^{-1}}$)", steps=[
            S("Moles of Al", math=r"\frac{2.7}{27} = 0.10\ \mathrm{mol}"),
            S("Each atom gives 3 electrons", math=r"0.10\times3 = 0.30\ \mathrm{mol\ of\ electrons}"),
            S("Number", math=r"0.30\times6.02\times10^{23} = 1.8\times10^{23}"),
        ]),
        H("Alloys"),
        T("An **alloy** is a mixture of a metal with other elements, usually other metals. Brass is copper with zinc, and bronze is copper with tin. Bronze and brass castings made by craftspeople in the Grassfields and elsewhere are alloys. "
          "Atoms of a different size disturb the regular layers, so the layers cannot slide as easily, and the alloy is harder and stronger than the pure metal."),
        MISTAKE("Saying metals contain free electrons from the ions", "The positive ions stay in the lattice; the delocalised electrons come from the outer shells of the metal atoms. The metal as a whole is neutral."),
        MISTAKE("Saying the bonding between metal atoms is 'ionic'", "There are no negative ions in a pure metal. The bond is between the positive ions and the sea of electrons, and it is not the same as the ionic bond between oppositely charged ions."),
        QUIZ("Why does sodium have a lower melting point than magnesium?",
             ["Sodium atoms are heavier than magnesium atoms", "Sodium has one delocalised electron per atom and larger ions, so the metallic bonding is weaker", "Sodium has covalent bonding", "Sodium atoms are smaller and have a higher charge"], 1,
             "Na gives one delocalised electron and forms a larger 1+ ion; Mg gives two electrons and forms a smaller 2+ ion, so Mg has the stronger attraction.",
             hint="Compare the charge on the ion, the ion radius and the number of delocalised electrons.",
             feedback=["The mass of the atom has little effect on the strength of the bonding.", "",
                       "Metals do not have covalent bonding between atoms; the model is a lattice of ions in an electron sea.", "This describes magnesium, which has the higher melting point."]),
        TIP("Metallic bonding appears in Paper 1 and Paper 2 as short explanations. Always name the ions and the delocalised electrons, and say how charge and size change the strength."),
        PQ(r"Explain why metals conduct electricity but ionic solids do not.",
           "In a metal the delocalised electrons are free to move through the lattice when a potential difference is applied. In an ionic solid the ions are held in fixed positions in the lattice and there are no free electrons, so no charge carriers can move."),
        PQ(r"Explain why copper can be drawn into wire but sodium chloride crystals shatter when hit.",
           "In copper, layers of positive ions can slide over each other while the delocalised electrons keep the lattice bonded. In sodium chloride, sliding moves like-charged ions next to each other, so repulsion breaks the crystal."),
        PQ("Explain why brass is harder than pure copper.",
           "Brass contains zinc atoms, which are a different size from copper atoms. They disrupt the regular layers of copper ions, so the layers cannot slide over each other as easily, making the alloy harder."),
        PQ(r"Compare the melting points of potassium (63 C) and calcium (842 C) and explain the difference.",
           r"Calcium atoms give two delocalised electrons and form a 2+ ion (100 pm), which is smaller and higher in charge than $\mathrm{K^+}$ (138 pm, 1 electron). The attraction between ions and electrons is therefore much stronger in calcium, so it has the higher melting point."),
        SUM("A metal is a lattice of positive ions surrounded by delocalised electrons.",
            "Conduction depends on mobile electrons; malleability on layers of ions sliding without breaking the bonding.",
            "Metallic bond strength increases with ion charge, smaller ion size and more delocalised electrons, so Na < Mg < Al in melting point.",
            "Alloys are harder because different-sized atoms disrupt the layers of the pure metal."),
    ],
))


# ------------------------------------------------------------------ 18. Dipole moments and hydrogen bonding
LESSONS.append(lesson(
    module=M3,
    topic="Dipole moments and hydrogen bonding",
    title="Dipole moments, intermolecular forces and hydrogen bonding",
    slug="chl1-dipoles-hydrogen-bonding",
    minutes=26,
    summary="Decide whether a molecule is polar from its bonds and shape, describe London, permanent dipole and hydrogen-bond forces, and explain boiling-point trends and the anomalous properties of water.",
    objectives=[
        "Use electronegativity to decide whether a bond is polar and add bond dipoles as vectors",
        "Predict whether a molecule has a net dipole moment from its shape",
        "Describe London (instantaneous dipole) forces, permanent dipole-dipole forces and hydrogen bonds",
        "Explain boiling-point trends and the high boiling point and low-density ice of water",
    ],
    key_concepts=["Electronegativity", "Polar bond", "Dipole moment", "London dispersion forces", "Permanent dipole-dipole forces", "Hydrogen bond"],
    blocks=[
        H("Introduction"),
        T("Water boils at 100 degrees Celsius. Hydrogen sulfide, H2S, a larger molecule from the same group, boils at about minus 60 degrees. If water followed the trend of its group it would boil far below zero "
          "and the oceans, the rivers of Cameroon and the water in a cooking pot would not exist as liquids at room temperature. The reason is a special intermolecular force, the hydrogen bond."),
        D("**Electronegativity** is the ability of an atom in a covalent bond to attract the bonding pair of electrons towards itself. Pauling values: H 2.2, C 2.5, N 3.0, O 3.5, F 4.0, Cl 3.0, Br 2.8, I 2.5. "
          "When two bonded atoms differ in electronegativity, the bond is **polar**: the more electronegative atom carries a small negative charge ($\\delta-$) and the other a small positive charge ($\\delta+$).", title="Electronegativity and bond polarity"),
        D("The **dipole moment**, $\\mu$, of a bond is the product of the size of the partial charge and the distance between the charges. It is a vector pointing towards the more electronegative atom. "
          "The dipole moment of a molecule is the vector sum of the bond dipoles. It is measured in debye (D); for water it is about 1.85 D.", title="Dipole moment"),
        IMG("al-chl1-dipoles.svg", alt="Carbon dioxide with two opposite bond dipoles that cancel, and bent water with bond dipoles that add to a net dipole",
            caption="Figure 1. A molecule with polar bonds is non-polar overall if its shape makes the dipoles cancel."),
        KEY("Polar or non-polar molecule?", "Two questions decide it.", cards=[
            ["1. Are the bonds polar?", "If every bond is non-polar (H2, Cl2, O2), the molecule is non-polar."],
            ["2. Does the shape cancel the dipoles?", "Symmetrical shapes with identical polar bonds cancel: CO2 (linear), BF3 (trigonal planar), CH4 and CCl4 (tetrahedral). Unsymmetrical shapes do not: H2O, NH3, CHCl3, SO2."],
        ]),
        H("Intermolecular forces"),
        T("Intermolecular forces are the forces **between** molecules. They are much weaker than covalent bonds (which are inside molecules). They decide melting points, boiling points and solubility."),
        CODE("""Force                              Occurs between                       Strength (typical)
London (instantaneous dipole-      all molecules and atoms,             0.1 to 40 kJ/mol; grows with the
induced dipole, dispersion)        even noble gases                     number of electrons in the molecule
Permanent dipole-dipole            polar molecules                      5 to 25 kJ/mol
Hydrogen bond                      H bonded to N, O or F, and a lone    10 to 40 kJ/mol (water about 20)
                                   pair on N, O or F of another molecule""", "text", title="Types of intermolecular force"),
        T("**London forces** arise because electrons are always moving, so at any instant one side of a molecule has slightly more electron density. This instantaneous dipole induces a dipole in a neighbour, and the two attract. "
          "More electrons and a larger surface area give stronger London forces, so boiling points rise down group 17 and with chain length in alkanes."),
        D("A **hydrogen bond** is a strong dipole-dipole attraction between a hydrogen atom bonded to a very electronegative atom (N, O or F) and a lone pair on a different N, O or F atom. "
          "It is shown as a dotted line and is roughly a tenth of the strength of a covalent bond.", title="Definition: hydrogen bond"),
        IMG("al-chl1-hbond-water.svg", alt="Three water molecules joined by dashed hydrogen bonds",
            caption="Figure 2. Hydrogen bonding in water: each molecule can form up to four hydrogen bonds."),
        IMG("al-chl1-bp-trends.svg", alt="Graph of boiling points of hydrides of groups 14, 15, 16 and 17 showing high values for NH3, H2O and HF",
            caption="Figure 3. Boiling points of hydrides: NH3, H2O and HF are anomalously high because of hydrogen bonding."),
        H("Worked examples"),
        EX("Worked example 1: polar or not?", intro=r"State whether each molecule has a net dipole moment: $\mathrm{CCl_4}$, $\mathrm{CHCl_3}$, $\mathrm{BF_3}$, $\mathrm{NH_3}$, $\mathrm{CO_2}$.", steps=[
            S(r"$\mathrm{CCl_4}$", text="Tetrahedral with four identical C-Cl dipoles: they cancel. Non-polar."),
            S(r"$\mathrm{CHCl_3}$", text="Tetrahedral, but one bond is C-H and three are C-Cl, so the dipoles do not cancel. Polar."),
            S(r"$\mathrm{BF_3}$", text="Trigonal planar with three identical B-F dipoles at 120 degrees: cancel. Non-polar."),
            S(r"$\mathrm{NH_3}$", text="Pyramidal with a lone pair: the dipoles add up. Polar."),
            S(r"$\mathrm{CO_2}$", text="Linear with two equal and opposite C=O dipoles: cancel. Non-polar."),
        ]),
        EX("Worked example 2: boiling points of hydrogen halides", intro=r"The boiling points of HF, HCl, HBr and HI are 20, -85, -67 and -35 degrees Celsius. Explain the pattern.", steps=[
            S("HCl, HBr, HI", text="Boiling point rises as the molecules get larger and have more electrons, so the London forces get stronger."),
            S("HF is out of line", text="F is so electronegative that HF molecules form hydrogen bonds, which are much stronger than the London and dipole forces in HCl, so HF has the highest boiling point."),
        ]),
        EX("Worked example 3: same relative mass, different boiling point", intro=r"Ethanol, $\mathrm{CH_3CH_2OH}$ (boiling point 78 C), and methoxymethane, $\mathrm{CH_3OCH_3}$ (boiling point -24 C), both have $M_r = 46$. Explain the difference.", steps=[
            S("Same formula mass and electrons", text="The London forces are similar."),
            S("Ethanol has an O-H bond", text="So its molecules form hydrogen bonds with each other."),
            S("Methoxymethane has no O-H", text="Its molecules are only polar (weaker permanent dipole-dipole forces). Less energy is needed to separate them, so the boiling point is much lower."),
        ]),
        H("Water: the effects of hydrogen bonding"),
        KEY("Unusual properties", "Each is explained by hydrogen bonds.", cards=[
            ["High boiling point", "Many hydrogen bonds must be broken to vaporise water."],
            ["Ice floats", "In ice each molecule forms four hydrogen bonds in an open hexagonal lattice, which holds molecules farther apart than in liquid water. Ice is less dense, so lakes freeze from the top and life survives below."],
            ["Good solvent", "Water forms hydrogen bonds with ethanol, sugars and ammonia, and attracts ions through the polarity of its molecules."],
            ["High surface tension", "Molecules at the surface are pulled inwards by hydrogen bonds."],
        ]),
        MISTAKE("Saying hydrogen bonds are bonds within the molecule", "A hydrogen bond is an intermolecular force. When water boils, the covalent O-H bonds stay intact and the hydrogen bonds between molecules break."),
        MISTAKE("Giving hydrogen bonding for any molecule containing hydrogen", "Hydrogen bonds need H bonded directly to N, O or F, plus a lone pair on N, O or F in another molecule. CH4 and H2S do not form hydrogen bonds in the liquid."),
        QUIZ("Which molecule forms hydrogen bonds with other molecules of itself?",
             ["CH4", "CH3F", "CH3OH", "CH3OCH3"], 2,
             "Methanol has an O-H bond, so H is attached directly to oxygen and it can form hydrogen bonds. CH3F has no H bonded to F; CH3OCH3 has no O-H; CH4 has no N, O or F.",
             hint="Look for H directly bonded to N, O or F.",
             feedback=["CH4 has no N, O or F, so no hydrogen bonds.", "The F is bonded to carbon, and the H atoms are bonded to carbon, not to F.", "",
                       "The oxygen is bonded to two carbons, so there is no O-H to donate a hydrogen bond between its own molecules."]),
        TIP("This topic is tested in Paper 1 (rank boiling points, spot hydrogen bonding) and Paper 2 (explain with the type of force). Name the force, say between which atoms, and compare strengths."),
        PQ("Explain why the boiling point of water (100 C) is much higher than that of hydrogen sulfide (about -60 C).",
           "Water molecules form hydrogen bonds because H is bonded to the very electronegative O, which also has lone pairs. Hydrogen bonds are much stronger than the weak dipole and London forces in H2S, so much more energy is needed to separate water molecules."),
        PQ("Put CH4, SiH4, GeH4 in order of increasing boiling point and explain.",
           "CH4 < SiH4 < GeH4 (about -162, -112 and -88 degrees Celsius). All are non-polar and use only London forces. The molecules have more electrons down the group, so the London forces grow stronger."),
        PQ("Explain why ice is less dense than liquid water.",
           "In ice each water molecule forms four hydrogen bonds in a regular open lattice, with large spaces. When ice melts some hydrogen bonds break and the molecules move closer together, so liquid water is denser."),
        PQ("Explain why ethanol is soluble in water but hexane is not.",
           "Ethanol has an O-H group that forms hydrogen bonds with water molecules, which are about as strong as those in the pure liquids. Hexane is non-polar and can only form London forces with water, which are weaker than the hydrogen bonds between water molecules, so it does not dissolve."),
        SUM("A polar bond has unequal sharing; a molecule is polar only if its dipoles do not cancel (shape matters).",
            "London forces act between all molecules and increase with the number of electrons; permanent dipole forces act between polar molecules.",
            "A hydrogen bond needs H bonded to N, O or F and a lone pair on N, O or F of another molecule.",
            "Hydrogen bonds explain the high boiling points of NH3, H2O and HF, ice floating, and the solubility of alcohols."),
    ],
))

