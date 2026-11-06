"""Form 5 Chemistry (O Level 0515): Organic Chemistry & Qualitative Analysis (8 topics) and the Examination module.

Draft content built from KKEVO's master curriculum blueprint, not from a Board syllabus booklet; a reviewer must check
it against the Board's syllabus and textbooks. Exam facts are only those of the Board's 2023 subject report: Paper 1 is
50 multiple-choice questions in 1 hour 30 minutes; Paper 2 has ten questions in Sections A, B (Alternative to Practical,
two compulsory questions on experimental skills) and C. Study plans and checklists are KKEVO advice, not mark schemes.

Notation used in this file (converted by fx() at the bottom): [[CH4]] is a formula or equation in running text,
<<2H2 + O2 -> 2H2O>> is the same as bare LaTeX for a math= field; ^ gives a charge, e.g. Cu^2+, and n is an italic n.
Relative atomic masses used: H 1, C 12, N 14, O 16, Na 23, Mg 24, S 32, Cl 35.5, K 39, Ca 40, Cu 63.5, Zn 65.
"""

import re

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "form-5")

M_ORG = "Organic Chemistry & Qualitative Analysis"
M_EXAM = "Examination"

_ARROWS = {"->": r"\rightarrow ", "<=>": r"\rightleftharpoons ", "+": "+", "=": "="}


def _tok(t):
    """One token of a chemical formula or equation -> LaTeX (see the notation note above)."""
    if t in _ARROWS:
        return _ARROWS[t]
    if re.fullmatch(r"[\d.]+|n", t):
        return t
    coef = ""
    m = re.match(r"^(\d+)(?=[A-Z(\[e])", t)
    if m:
        coef, t = m.group(1) + r"\,", t[m.end():]
    ch = ""
    if "^" in t:
        t, ch = t.split("^", 1)
        ch = "^{" + ch + "}"
    t = re.sub(r"(?<=[A-Za-z)\]])(\d+)", r"_{\1}", t).replace(".", r"\cdot ")
    return coef + r"\mathrm{" + t + ch + "}"


def _eq(s):
    return " ".join(_tok(t) for t in s.split())


def fx(s):
    """[[CH4]] -> inline maths; <<2H2 + O2 -> 2H2O>> -> bare LaTeX for a math= field."""
    s = re.sub(r"\[\[(.+?)\]\]", lambda m: "$" + _eq(m.group(1)) + "$", s)
    return re.sub(r"<<(.+?)>>", lambda m: _eq(m.group(1)), s)


def _walk(x):
    if isinstance(x, str):
        return fx(x)
    if isinstance(x, list):
        return [_walk(i) for i in x]
    if isinstance(x, dict):
        return {k: _walk(v) for k, v in x.items()}
    return x


LESSONS = []

# ============================================================================================
# 1. Homologous series and nomenclature (lesson 1 of 2)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Homologous series and nomenclature",
    title="Homologous series and functional groups",
    slug="che-homologous-series-functional-groups", minutes=22,
    summary="Organic compounds are carbon compounds. A homologous series is a family with the same functional group and general formula, each member differing by CH2 from the next.",
    objectives=[
        "Define a hydrocarbon and a homologous series and list the features of a series",
        "Write the general formula of alkanes, alkenes, alkynes, alcohols and carboxylic acids",
        "Name the functional group of each family and distinguish saturated from unsaturated compounds",
        "Use a general formula to find the molecular formula or relative molecular mass of a member of a series",
    ],
    key_concepts=["Organic compound", "Hydrocarbon", "Homologous series", "General formula", "Functional group", "Saturated and unsaturated"],
    blocks=[
        H("Introduction"),
        T("In a kitchen in Douala, the cooking gas in the cylinder is mainly butane. The hand sanitiser on the table contains ethanol. "
          "The vinegar in the salad is ethanoic acid. The plastic bowl is made of poly(ethene). All of these are **organic compounds**: compounds of carbon.\n\n"
          "There are millions of organic compounds. To avoid learning them one by one, chemists sort them into families. Members of a family behave in a similar way. "
          "This lesson shows how the families are built."),
        D("**Organic chemistry** is the study of carbon compounds (except a few simple ones such as carbonates, carbon monoxide and carbon dioxide, which are usually studied with inorganic chemistry). "
          "A **hydrocarbon** is a compound that contains **only carbon and hydrogen**.", title="Definitions"),
        T("Carbon atoms can join to each other in long chains and rings, and each carbon atom forms **four** covalent bonds. This is why there are so many carbon compounds."),
        H("Homologous series"),
        D("A **homologous series** is a family of organic compounds that have the **same functional group**, the **same general formula**, and **similar chemical properties**. "
          "Each member differs from the next by a [[CH2]] group.", title="Homologous series"),
        KEY("Four features of a homologous series", "Learn these four. They are asked often.",
            cards=[["Same general formula", "One formula with the letter n fits every member, for example CnH2n+2 for alkanes."],
                   ["Same functional group", "All members have the same atom or group of atoms that decides how they react."],
                   ["Successive members differ by CH2", "The relative molecular mass rises by 14 from one member to the next (12 + 2 = 14)."],
                   ["Gradual change in physical properties", "Melting point, boiling point and density change steadily as the chain gets longer."]]),
        T("The first eight alkanes show the pattern. Each formula is the one before it plus [[CH2]]. The boiling points rise because longer molecules have stronger attractions between them. The values are approximate."),
        CODE("Name      Formula   Boiling point (approx.)\n"
             "methane   CH4       -162 C\n"
             "ethane    C2H6       -89 C\n"
             "propane   C3H8       -42 C\n"
             "butane    C4H10       -1 C\n"
             "pentane   C5H12       36 C\n"
             "hexane    C6H14       69 C\n"
             "heptane   C7H16       98 C\n"
             "octane    C8H18      126 °C", "text", title="The first eight alkanes"),
        T("This is why butane is a gas that can be liquefied in a cylinder and pentane is a liquid at room temperature."),
        H("General formulae and functional groups"),
        D("A **functional group** is the atom or group of atoms in a molecule that is mainly responsible for its chemical reactions.", title="Functional group"),
        CODE("Family           Functional group   General formula    Example\n"
             "alkanes          C-C single bonds   CnH2n+2            CH4\n"
             "alkenes          C=C double bond    CnH2n              C2H4\n"
             "alkynes          C=-C triple bond   CnH2n-2            C2H2\n"
             "alcohols         -OH                CnH2n+1OH          C2H5OH\n"
             "carboxylic acids -COOH              CnH2n+1COOH        CH3COOH\n"
             "esters           -COO-              CnH2n+1COOCmH2m+1  CH3COOC2H5", "text", title="Families you must know"),
        D("A **saturated** hydrocarbon has only single bonds between carbon atoms (the alkanes). An **unsaturated** hydrocarbon has at least one double or triple bond between carbon atoms (alkenes and alkynes).",
          title="Saturated and unsaturated"),
        EX("Worked example 1: a formula from the general formula", intro="An alkane has 12 carbon atoms in each molecule. Write its molecular formula and find its relative molecular mass.",
           steps=[
               S("Write the general formula", math=r"\text{C}_n\text{H}_{2n+2}"),
               S("Put n = 12", math=r"\text{C}_{12}\text{H}_{2(12)+2} = \text{C}_{12}\text{H}_{26}"),
               S("Add the atomic masses (C = 12, H = 1)", math=r"12 \times 12 + 26 \times 1 = 144 + 26 = 170"),
               S("State the answer", text="The formula is [[C12H26]] and its relative molecular mass is 170."),
           ]),
        EX("Worked example 2: finding n from a mass", intro="A member of the alkene series has relative molecular mass 84. Find its molecular formula.",
           steps=[
               S("General formula of alkenes", math=r"\text{C}_n\text{H}_{2n}"),
               S("Each CH2 unit has mass 14", math=r"12n + 2n = 14n"),
               S("Solve", math=r"14n = 84 \;\Rightarrow\; n = 6"),
               S("Write the formula", text="The alkene is [[C6H12]]. Check: 6 x 12 + 12 = 84."),
           ]),
        MISTAKE("Using the alkane formula for every hydrocarbon", "CnH2n+2 is only for alkanes. Alkenes are CnH2n and alkynes are CnH2n-2. A hydrocarbon with formula C4H8 cannot be an alkane: it has two hydrogen atoms fewer than the alkane C4H10, so it has a double bond."),
        MISTAKE("Saying members of a series have the same physical properties", "They have **similar chemical** properties, because they share a functional group. Their **physical** properties change steadily with chain length."),
        TIP("Homologous series, general formulae and functional groups are tested in Paper 1 (multiple choice) and in the structured questions of Paper 2. The Board's report says candidates need to be clear that the -OH group is the functional group in alcohols.", title="Exam link"),
        QUIZ("Which is the general formula of the alkenes?", [r"$\text{C}_n\text{H}_{2n+2}$", r"$\text{C}_n\text{H}_{2n}$", r"$\text{C}_n\text{H}_{2n-2}$", r"$\text{C}_n\text{H}_{2n+1}\text{OH}$"], 1,
             "Alkenes have one C=C bond, so they have two hydrogen atoms fewer than the alkane with the same number of carbon atoms: CnH2n.",
             hint="Compare with the alkane formula and remove the hydrogen atoms that make room for the double bond.",
             feedback=["This is the formula of the alkanes.", "", "This is the formula of the alkynes.", "This is the formula of the alcohols."]),
        QUIZ("Which two compounds are in the same homologous series?", ["C2H4 and C2H6", "CH3OH and CH3COOH", "C3H8 and C5H12", "C2H5OH and C2H6"], 2,
             "C3H8 and C5H12 both fit CnH2n+2 (n = 3 and n = 5), so both are alkanes. Members of a series with n = 3 and n = 5 differ by two CH2 groups.",
             hint="Test each pair against the general formulae.",
             feedback=["C2H4 is an alkene and C2H6 is an alkane: different functional groups.", "CH3OH is an alcohol (-OH) and CH3COOH is a carboxylic acid (-COOH).", "", "C2H5OH is an alcohol and C2H6 is an alkane."]),
        PQ("Define the term *homologous series* and give two features of a homologous series.",
           "A homologous series is a family of organic compounds with the same functional group and the same general formula. Features: successive members differ by CH2; they have similar chemical properties; their physical properties change gradually (any two)."),
        PQ("An alkane has 8 carbon atoms. Write its formula and calculate its relative molecular mass. (C = 12, H = 1)",
           "General formula CnH2n+2 with n = 8 gives C8H18. Mr = 8 x 12 + 18 x 1 = 96 + 18 = 114."),
        PQ("Explain why the boiling point of the alkanes increases from methane to octane.",
           "As the chain gets longer the molecules are bigger, so the attractions between molecules are stronger. More energy is needed to separate them, so the boiling point rises."),
        PQ("Name the functional group in (a) [[CH3CH2OH]] and (b) [[CH3COOH]].",
           "(a) The hydroxyl group, -OH (an alcohol). (b) The carboxyl group, -COOH (a carboxylic acid)."),
        SUM("Organic compounds are compounds of carbon; hydrocarbons contain only carbon and hydrogen.",
            "A homologous series has the same functional group, the same general formula and similar chemical properties; neighbours differ by CH2 (14 mass units).",
            "General formulae: alkanes CnH2n+2, alkenes CnH2n, alkynes CnH2n-2, alcohols CnH2n+1OH, carboxylic acids CnH2n+1COOH.",
            "Functional groups: C=C, C=-C, -OH and -COOH decide how each family reacts.",
            "Saturated compounds have only single bonds; unsaturated compounds have a double or triple bond."),
    ])]

# ============================================================================================
# 2. Homologous series and nomenclature (lesson 2 of 2)
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Homologous series and nomenclature",
    title="Naming organic compounds and isomers",
    slug="che-naming-organic-compounds-isomers", minutes=24,
    summary="IUPAC names come from the longest chain (stem), the family ending and the numbered branches. Isomers share a molecular formula but differ in structure or in arrangement about a double bond.",
    objectives=[
        "Name straight-chain and simply branched alkanes, alkenes and alcohols using IUPAC rules",
        "Define structural isomers and draw the isomers of butane, pentane and butene",
        "Explain geometric (cis-trans) isomerism and say when a compound can show it",
        "Check that two structures have the same molecular formula by counting atoms",
    ],
    key_concepts=["IUPAC name", "Stem", "Alkyl group", "Structural isomers", "Geometric isomers", "Cis and trans"],
    blocks=[
        H("Introduction"),
        T("Two bottles on a shelf both contain a compound with the molecular formula [[C4H10]]. One boils at about -1 °C. The other boils at about -12 °C. They are different substances with the same formula. "
          "To talk about them clearly, chemists give every compound a systematic name. The rules are set by IUPAC, the International Union of Pure and Applied Chemistry."),
        KEY("Four steps to name a compound", "Follow the steps in order.",
            cards=[["1. Find the longest chain", "Count the carbon atoms in the longest unbroken chain that contains the functional group. This gives the stem."],
                   ["2. Add the family ending", "-ane for alkanes, -ene for alkenes, -yne for alkynes, -ol for alcohols, -oic acid for carboxylic acids."],
                   ["3. Name the branches", "A branch is an alkyl group: methyl, CH3, or ethyl, C2H5. Put its name in front."],
                   ["4. Number the carbons", "Number from the end that gives the **lowest numbers** to the functional group first, then the branches. Use di- for two identical branches."]]),
        CODE("Carbons  Stem      Alkyl group\n"
             "1        meth-     methyl  CH3-\n"
             "2        eth-      ethyl   C2H5-\n"
             "3        prop-\n"
             "4        but-\n"
             "5        pent-\n"
             "6        hex-\n"
             "7        hept-\n"
             "8        oct-", "text", title="Stems and alkyl groups"),
        EX("Worked example 1: naming a branched alkane", intro="Name CH3-CH(CH3)-CH2-CH3, which has a CH3 branch on the second carbon atom of the chain.",
           steps=[
               S("Longest chain", text="Going CH3, CH, CH2, CH3 gives 4 carbon atoms: the stem is but-."),
               S("Family ending", text="All bonds are single, so the ending is -ane: butane."),
               S("Branch", text="One CH3 group is a methyl branch."),
               S("Number", text="Number from the end that gives the branch the lower number: the branch is on carbon 2. The name is **2-methylbutane**."),
               S("Check the formula", text="C: 1 + 1 + 1 + 1 + 1 = 5. H: 3 + 1 + 3 + 2 + 3 = 12. The formula is [[C5H12]], so it is an isomer of pentane."),
           ]),
        H("Structural isomers"),
        D("**Structural isomers** are compounds with the **same molecular formula** but **different structural formulae** (the atoms are joined in a different order). Their physical properties differ, and sometimes their chemical properties do too.", title="Structural isomers"),
        T("[[C4H10]] has two isomers. One has a straight chain and one has a branch."),
        CODE("butane           CH3-CH2-CH2-CH3\n"
             "2-methylpropane  CH3-CH(CH3)-CH3\n\n"
             "Both are C4H10. Butane boils at about -1 C;\n"
             "2-methylpropane boils at about -12 °C.", "text", title="The isomers of C4H10"),
        T("[[C5H12]] has **three** isomers. [[C6H14]] has **five**. The number of isomers grows quickly with chain length."),
        CODE("pentane              CH3-CH2-CH2-CH2-CH3\n"
             "2-methylbutane       CH3-CH(CH3)-CH2-CH3\n"
             "2,2-dimethylpropane  C(CH3)4   (a carbon with four CH3 groups)", "text", title="The three isomers of C5H12"),
        EX("Worked example 2: positions of a double bond and an -OH group", intro="Write the names of the compounds CH2=CH-CH2-CH3, CH3-CH=CH-CH3, CH3-CH2-CH2-OH and CH3-CH(OH)-CH3.",
           steps=[
               S("Alkenes: number so the double bond gets the lowest number", text="CH2=CH-CH2-CH3 has the double bond after carbon 1: **but-1-ene**. CH3-CH=CH-CH3 has it after carbon 2: **but-2-ene**."),
               S("Alcohols: number so the -OH gets the lowest number", text="CH3-CH2-CH2-OH has -OH on carbon 1: **propan-1-ol**. CH3-CH(OH)-CH3 has -OH on carbon 2: **propan-2-ol**."),
               S("Notice", text="Each pair has the same molecular formula ([[C4H8]] and [[C3H8O]]), so each pair are structural isomers."),
           ]),
        H("Geometric (cis-trans) isomerism"),
        T("Rotation about a C=C double bond is not possible, so the groups on each carbon atom stay fixed in space. This gives a second kind of isomerism."),
        D("**Geometric isomers** have the same structural formula but the groups are arranged differently in space about a C=C bond. In the **cis** form the two matching groups are on the **same side**. In the **trans** form they are on **opposite sides**.", title="Geometric isomerism"),
        CODE("   H3C     CH3          H3C     H\n"
             "      \\   /                \\   /\n"
             "       C=C                  C=C\n"
             "      /   \\                /   \\\n"
             "     H     H              H     CH3\n"
             "  cis-but-2-ene        trans-but-2-ene", "text", title="Geometric isomers of but-2-ene"),
        KEY("When is cis-trans isomerism possible?", "Each of the two carbon atoms of the C=C bond must have two **different** groups attached.",
            cards=[["But-2-ene: yes", "Each double-bond carbon carries H and CH3: two different groups."],
                   ["But-1-ene: no", "One double-bond carbon is CH2=, with two identical hydrogen atoms, so the two arrangements are the same molecule."],
                   ["Ethene: no", "Each carbon has two hydrogen atoms."]]),
        MISTAKE("Choosing a chain that is drawn straight, not the longest", "A chain can bend on the page. Count the longest run of carbon atoms, even if it turns corners. In the structure CH3-CH2-CH(CH3)-CH2-CH3 the longest chain has 5 carbons (pentane), with a methyl branch on carbon 3. It is **3-methylpentane**, not a hexane."),
        MISTAKE("Numbering from the wrong end", "The rule is the lowest number for the functional group first. Write butan-2-ol, never butan-3-ol: numbering from the other end gives 2."),
        TIP("Isomers, names and structures appear in Paper 1 (for example, which of these is an isomer of butane) and in Paper 2 structured questions. When asked to show isomers, write the full structural formula and then count atoms to check the molecular formula.", title="Exam link"),
        QUIZ("Which of these is an isomer of butane, [[C4H10]]?", ["Butene, C4H8", "2-methylpropane", "Propane, C3H8", "Butan-1-ol, C4H9OH"], 1,
             "2-methylpropane has the formula C4H10 with a branched chain, so it is a structural isomer of butane.",
             hint="An isomer must have the same molecular formula.",
             feedback=["Butene has two fewer hydrogen atoms.", "", "Propane has three carbon atoms, not four.", "Butan-1-ol contains oxygen, so the molecular formula differs."]),
        QUIZ("Which compound shows cis-trans isomerism?", ["Ethene", "But-1-ene", "But-2-ene", "Butane"], 2,
             "In but-2-ene each double-bond carbon has an H and a CH3 group. These are different, so the cis and trans forms exist.",
             hint="Look for a C=C bond with two different groups on each carbon atom.",
             feedback=["Each carbon of ethene has two identical hydrogen atoms.", "One end is CH2=, with two hydrogen atoms: the two forms are the same.", "", "Butane has no C=C bond, so groups can rotate."]),
        PQ("Draw and name the three isomers of [[C5H12]].",
           "Pentane CH3-CH2-CH2-CH2-CH3; 2-methylbutane CH3-CH(CH3)-CH2-CH3; 2,2-dimethylpropane C(CH3)4."),
        PQ("Name [[CH3CH2CH(CH3)CH2CH3]] and write its molecular formula.",
           "The longest chain has 5 carbons (pentane) with a methyl branch on carbon 3: 3-methylpentane. It has 5 + 1 = 6 carbon atoms and 3 + 2 + 1 + 3 + 2 + 3 = 14 hydrogen atoms, so the formula is C6H14."),
        PQ("Explain why but-2-ene has cis and trans forms but but-1-ene does not.",
           "There is no rotation about the C=C bond. In but-2-ene each double-bond carbon has two different groups (H and CH3), so the groups can be on the same side (cis) or opposite sides (trans). In but-1-ene one carbon has two identical H atoms, so only one arrangement exists."),
        PQ("Give the names of the two alcohols with molecular formula [[C3H8O]].",
           "Propan-1-ol, CH3CH2CH2OH, and propan-2-ol, CH3CH(OH)CH3. They are structural isomers (position of the -OH group)."),
        SUM("IUPAC names come from the longest chain (stem), the family ending, then the branches with the lowest possible numbers.",
            "Structural isomers have the same molecular formula but different structures: C4H10 has 2, C5H12 has 3 and C6H14 has 5.",
            "Isomers can also differ in the position of a double bond or an -OH group.",
            "Geometric isomers (cis and trans) occur when rotation about C=C is blocked and each carbon has two different groups.",
            "Always check isomers by counting atoms."),
    ])]

# ============================================================================================
# 3. Crude oil and cracking
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Crude oil and cracking",
    title="Crude oil, fractional distillation and cracking",
    slug="che-crude-oil-fractional-distillation-cracking", minutes=24,
    summary="Crude oil is a mixture of hydrocarbons separated by fractional distillation according to boiling point. Cracking breaks long alkanes into shorter alkanes and alkenes.",
    objectives=[
        "Describe how crude oil formed and why it is a mixture of hydrocarbons",
        "Explain fractional distillation and how the properties of fractions change down the column",
        "State the main fractions and their uses",
        "Explain why cracking is done, name the conditions and write balanced cracking equations",
    ],
    key_concepts=["Crude oil", "Fractional distillation", "Fraction", "Cracking", "Catalytic cracking", "Alkene from alkane"],
    blocks=[
        H("Introduction"),
        T("Petrol for a taxi in Yaounde, kerosene for a lamp in a village, diesel for a generator, tar for a new road: all of these come from **crude oil**. "
          "Cameroon produces crude oil offshore and has a refinery at Limbe. A refinery does not make new substances at first. It separates a mixture into useful parts."),
        D("**Crude oil** is a thick, dark liquid found underground. It is a **mixture of many hydrocarbons**, mostly alkanes. It formed over millions of years from the remains of tiny sea plants and animals that were buried under mud and sand and changed by heat and pressure. Because it is a mixture, its substances keep their own boiling points, and **fractional distillation** uses this difference.", title="Crude oil"),
        H("Fractional distillation"),
        D("**Fractional distillation** is the separation of a liquid mixture into parts called **fractions**, using the different boiling points of the components. Each fraction is still a mixture of hydrocarbons with similar boiling points.", title="Fractional distillation"),
        IMG("f5ch-e-fractionating-column.svg", alt="A tall fractionating column. Crude oil enters near the bottom. Refinery gas leaves at the top, then petrol, kerosene, diesel, fuel oil and bitumen at the bottom. An arrow shows temperature falling upwards.",
            caption="Figure 1. A fractionating column. The column is hot at the bottom and cooler at the top."),
        KEY("How the column works", "Follow the steps from the bottom to the top.",
            cards=[["1. Heat", "Crude oil is heated in a furnace to about 350 °C. Most of it turns to vapour."],
                   ["2. Enter", "The hot vapour enters near the bottom of the tall column."],
                   ["3. Rise and cool", "The vapour rises. The temperature falls steadily up the column."],
                   ["4. Condense", "Each hydrocarbon condenses where the column is cooler than its boiling point and is tapped off as a fraction."]]),
        T("Long molecules have high boiling points, so they condense low in the column. Short molecules have low boiling points and rise to the top. "
          "This is why the bottom fractions are thick, dark and slow to burn, and the top fractions are thin, pale and catch fire easily."),
        CODE("Fraction          Carbon atoms (approx.)  Main use\n"
             "refinery gas      1 to 4                  cooking gas (LPG), heating\n"
             "petrol            5 to 10                 fuel for cars and motorbikes\n"
             "kerosene          10 to 16                jet fuel, lamps and stoves\n"
             "diesel            15 to 20                lorries, buses, generators\n"
             "fuel oil          20 to 30                ships, power stations\n"
             "bitumen           above 35                road surfaces, roofing", "text",
             title="Main fractions, top to bottom (carbon numbers differ between textbooks)"),
        KEY("Trends down the column", "From refinery gas to bitumen:",
            cards=[["Longer molecules", "More carbon atoms in each molecule."],
                   ["Higher boiling point", "Stronger attractions between the bigger molecules."],
                   ["More viscous", "Thicker and slower to flow."],
                   ["Less flammable", "Harder to ignite, and they burn with a smokier flame."]]),
        H("Cracking"),
        T("There is a problem. Crude oil contains more long-chain hydrocarbons than we need and fewer short ones than we want. Petrol is in great demand. Cracking solves the problem."),
        D("**Cracking** is the breaking down of large alkane molecules into smaller, more useful molecules, one of which is an **alkene**. It is a decomposition reaction done at high temperature, with or without a catalyst.", title="Cracking"),
        KEY("Conditions for catalytic cracking", "These are the usual conditions in textbooks; check your textbook for the exact values.",
            cards=[["Temperature", "About 500 °C for catalytic cracking. Thermal cracking uses a much higher temperature (700 °C or more)."],
                   ["Catalyst", "A zeolite (a hard aluminium silicate), or aluminium oxide or silica."]]),
        T("The alkanes made are shorter alkanes, which are used in petrol. The alkenes made are the raw materials for plastics and for making ethanol. So cracking gives both fuel and chemical raw materials."),
        EX("Worked example 1: balancing a cracking equation", intro="Decane, [[C10H22]], is cracked into octane, [[C8H18]], and one other product. Write the equation.",
           steps=[
               S("Subtract the atoms", math=r"\text{C}_{10}\text{H}_{22} - \text{C}_8\text{H}_{18} = \text{C}_2\text{H}_4"),
               S("Identify the other product", text="[[C2H4]] fits the formula CnH2n, so it is ethene, an alkene."),
               S("Write the equation", math=r"<<C10H22 -> C8H18 + C2H4>>"),
               S("Check atoms", text="Carbon: 10 on the left, 8 + 2 = 10 on the right. Hydrogen: 22 on the left, 18 + 4 = 22 on the right. Balanced."),
           ]),
        EX("Worked example 2: two molecules of alkene", intro="Tetradecane, [[C14H30]], cracks into decane, [[C10H22]], and ethene only. How many molecules of ethene form from one molecule of tetradecane?",
           steps=[
               S("Carbon left over", math=r"14 - 10 = 4 \text{ carbon atoms}"),
               S("Each ethene has 2 carbon atoms", math=r"4 \div 2 = 2 \text{ molecules}"),
               S("Equation", math=r"<<C14H30 -> C10H22 + 2C2H4>>"),
               S("Check hydrogen", text="22 + 2 x 4 = 30. Balanced."),
           ]),
        H("Cracking in the laboratory and the test for the alkene"),
        IMG("f5ch-e-cracking-apparatus.svg", alt="A hard-glass tube holds mineral wool soaked in liquid paraffin at one end and broken porcelain in the middle. The porcelain is heated strongly. A delivery tube carries gas into a test tube over water in a trough.",
            caption="Figure 2. Cracking in the laboratory. The gas is collected over water."),
        T("Liquid paraffin (a mixture of alkanes) is warmed so that its vapour passes over strongly heated broken porcelain, which acts as the catalyst. The gases that form are collected over water. "
          "To show that an alkene is present, shake the gas with **bromine water**. It changes from orange-brown to colourless."),
        MISTAKE("Mixing up the two processes", "Fractional distillation is a **physical** separation: no molecules are changed. Cracking is a **chemical** change: big molecules are broken into smaller ones."),
        MISTAKE("Saying fractions are pure compounds", "A fraction is a mixture of hydrocarbons with boiling points close together. Petrol, for example, contains many different compounds."),
        TIP("Crude oil and cracking come up in Paper 1 (fractions, uses, trends) and in Paper 2 structured questions (equations for cracking, why it is done). Alkenes made by cracking lead into the lessons on alkenes and polymers.", title="Exam link"),
        QUIZ("Which fraction condenses nearest the top of the fractionating column?", ["Bitumen", "Diesel", "Refinery gas", "Fuel oil"], 2,
             "Refinery gas has the smallest molecules and the lowest boiling points, so it stays as a gas to the top of the column.",
             hint="Short molecules have low boiling points.",
             feedback=["Bitumen has the largest molecules and leaves at the bottom.", "Diesel is in the middle of the column.", "", "Fuel oil is low in the column."]),
        QUIZ("Why is cracking carried out in oil refineries?", ["To separate crude oil into fractions", "To change long alkanes into shorter, more useful alkanes and alkenes", "To remove sulfur from petrol", "To join small molecules into polymers"], 1,
             "Cracking breaks long-chain molecules, which are in surplus, into shorter alkanes for petrol and alkenes for plastics.",
             hint="Think about what we want more of: petrol or bitumen?",
             feedback=["That is fractional distillation.", "", "Removing sulfur is a different process.", "Joining small molecules is polymerization, the opposite of cracking."]),
        PQ("Explain why the molecules in the bitumen fraction have higher boiling points than those in refinery gas.",
           "Bitumen molecules are much longer (more than 35 carbon atoms) than refinery gas molecules (1 to 4 carbon atoms). Longer molecules have stronger attractions between them, so more energy is needed to separate them: a higher boiling point."),
        PQ("Write a balanced equation for the cracking of [[C12H26]] into ethene and one alkane. Name the alkane.",
           "C12H26 -> C10H22 + C2H4. The alkane is decane. Check: carbon 12 = 10 + 2; hydrogen 26 = 22 + 4."),
        PQ("Describe a test to show that a gas from cracking is unsaturated.",
           "Shake the gas with bromine water. If it is unsaturated (an alkene), the orange-brown colour disappears and the liquid becomes colourless."),
        PQ("Give two reasons why cracking is important.",
           "It turns surplus long-chain hydrocarbons into smaller alkanes that are in high demand for petrol, and it produces alkenes, which are raw materials for making plastics and other chemicals."),
        SUM("Crude oil is a mixture of hydrocarbons formed from ancient sea life over millions of years.",
            "Fractional distillation separates it by boiling point: small molecules rise to the top, big molecules stay low.",
            "Down the column: longer molecules, higher boiling points, more viscous, less flammable.",
            "Cracking breaks long alkanes into shorter alkanes and alkenes, using heat and a catalyst such as a zeolite.",
            "Bromine water changes from orange-brown to colourless with an alkene."),
    ])]

# ============================================================================================
# 4. Alkanes
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alkanes",
    title="Alkanes: combustion and substitution",
    slug="che-alkanes-combustion-substitution", minutes=24,
    summary="Alkanes are saturated hydrocarbons, CnH2n+2. Methane and ethane burn in oxygen (complete or incomplete combustion) and react with chlorine in sunlight by free-radical substitution.",
    objectives=[
        "Describe the structure and general properties of methane and ethane",
        "Write equations for complete and incomplete combustion and explain the danger of carbon monoxide",
        "Explain substitution with chlorine in sunlight and write the equations step by step",
        "Explain why alkanes do not react with bromine water, acids or alkalis",
    ],
    key_concepts=["Alkane", "Saturated", "Complete combustion", "Incomplete combustion", "Substitution", "Free radical"],
    blocks=[
        H("Introduction"),
        T("When a family in a village in the Grassfields feeds cow dung and farm waste to a biogas digester, the gas that burns on the stove is mostly **methane**. "
          "Natural gas from the ground, and the gas that bubbles from a swamp, are also mostly methane. Methane is the first member of the alkane family. Its neighbour is **ethane**."),
        D("**Alkanes** are saturated hydrocarbons with the general formula [[CnH2n+2]]. All the bonds between carbon atoms are single covalent bonds. Methane is [[CH4]]. Ethane is [[C2H6]].", title="Alkanes"),
        CODE("Methane CH4            Ethane C2H6\n\n"
             "      H                   H   H\n"
             "      |                   |   |\n"
             "  H - C - H           H - C - C - H\n"
             "      |                   |   |\n"
             "      H                   H   H", "text", title="Structures of methane and ethane"),
        T("Methane and ethane are colourless gases with little smell, and they are insoluble in water. Alkanes are **not very reactive**: all their bonds are strong single bonds, so they do not react with acids, alkalis, or bromine water. "
          "They do react in two important ways: **combustion** and **substitution**."),
        H("Combustion"),
        D("**Complete combustion** is burning in plenty of oxygen. The products are carbon dioxide and water. The reaction gives out a lot of heat, so alkanes are good fuels.", title="Complete combustion"),
        CODE("methane:  CH4 + 2O2  ->  CO2 + 2H2O\n"
             "ethane:   2C2H6 + 7O2  ->  4CO2 + 6H2O", "text", title="Complete combustion equations"),
        D("**Incomplete combustion** is burning in a limited supply of air. The products are carbon monoxide (or carbon, called soot) and water.", title="Incomplete combustion"),
        T("Examples of the equations for methane:\n\n[[2CH4 + 3O2 -> 2CO + 4H2O]]  (carbon monoxide)\n\n[[CH4 + O2 -> C + 2H2O]]  (carbon, as soot)"),
        MISTAKE("Ignoring carbon monoxide", "Carbon monoxide is a colourless, odourless, poisonous gas. It stops the blood from carrying oxygen. Never burn charcoal, a gas cooker or a generator in a closed room. Make sure there is fresh air."),
        EX("Worked example 1: mass of carbon dioxide", intro="Calculate the mass of carbon dioxide produced when 8.0 g of methane burns completely. (C = 12, H = 1, O = 16)",
           steps=[
               S("Equation", math=r"<<CH4 + 2O2 -> CO2 + 2H2O>>"),
               S("Moles of methane", math=r"M_r(\text{CH}_4) = 16;\quad n = \frac{8.0}{16} = 0.50\ \text{mol}"),
               S("Mole ratio CH4 : CO2 = 1 : 1", math=r"n(\text{CO}_2) = 0.50\ \text{mol}"),
               S("Mass of CO2", math=r"M_r(\text{CO}_2) = 44;\quad m = 0.50 \times 44 = 22\ \text{g}"),
           ]),
        EX("Worked example 2: volumes of gases", intro="What volume of oxygen is needed to burn completely 30 cm³ of ethane, and what volume of carbon dioxide forms? All gases are measured at the same temperature and pressure.",
           steps=[
               S("Equation", math=r"<<2C2H6 + 7O2 -> 4CO2 + 6H2O>>"),
               S("Gas volumes are in the same ratio as moles", text="2 volumes of ethane need 7 volumes of oxygen and give 4 volumes of carbon dioxide."),
               S("Oxygen", math=r"\frac{7}{2} \times 30 = 105\ \text{cm}^3"),
               S("Carbon dioxide", math=r"\frac{4}{2} \times 30 = 60\ \text{cm}^3"),
           ]),
        H("Substitution with chlorine"),
        D("A **substitution reaction** is one in which an atom or group in a molecule is replaced by another atom or group. In alkanes, hydrogen atoms are replaced by halogen atoms. It needs **ultraviolet light** (sunlight).", title="Substitution"),
        T("The first step makes a one-chlorine compound, chloromethane, and hydrogen chloride:"),
        T("[[CH4 + Cl2 -> CH3Cl + HCl]]"),
        T("With excess chlorine, more hydrogen atoms are replaced one by one: [[CH3Cl]] (chloromethane), [[CH2Cl2]] (dichloromethane), [[CHCl3]] (trichloromethane) and [[CCl4]] (tetrachloromethane)."),
        KEY("The free-radical mechanism", "A **free radical** is an atom or group with an unpaired electron. It is very reactive. The reaction is a chain reaction in three stages.",
            cards=[["1. Initiation", "Ultraviolet light splits the chlorine molecule into two chlorine atoms (radicals): Cl2 gives Cl• + Cl•"],
                   ["2. Propagation", "Cl• + CH4 gives HCl + CH3• then CH3• + Cl2 gives CH3Cl + Cl•. The new Cl• continues the chain."],
                   ["3. Termination", "Two radicals meet and join: Cl• + Cl• gives Cl2, or CH3• + Cl• gives CH3Cl. The chain stops."]]),
        T("In the dark, methane and chlorine do not react at room temperature. Light supplies the energy to start the chain."),
        MISTAKE("Calling it an addition reaction", "Substitution **replaces** a hydrogen atom and gives **two** products (for example CH3Cl and HCl). Addition joins molecules together and gives **one** product. Alkanes cannot undergo addition because they have no double bond."),
        TIP("Alkanes appear in Paper 1 (combustion, products, substitution) and in Paper 2 structured and essay questions on types of reactions. The Board's report says short notes on reaction types should give a definition and an equation as an example.", title="Exam link"),
        QUIZ("What are the products of the **incomplete** combustion of methane?", ["Carbon dioxide and water only", "Carbon monoxide (or carbon) and water", "Methane and oxygen", "Hydrogen and carbon dioxide"], 1,
             "In a limited supply of oxygen, carbon is only partly oxidised, so carbon monoxide or carbon (soot) forms, together with water.",
             hint="Which product shows that the carbon has not been fully oxidised?",
             feedback=["That is complete combustion.", "", "These are not products.", "Burning does not release hydrogen gas."]),
        QUIZ("What type of reaction occurs between methane and chlorine in sunlight?", ["Addition", "Neutralisation", "Substitution", "Polymerization"], 2,
             "A hydrogen atom of methane is replaced by a chlorine atom, so it is a substitution reaction.",
             hint="Count the products. Is one atom swapped for another?",
             feedback=["Addition needs a double bond and gives one product.", "Neutralisation is acid with base.", "", "Polymerization joins many small molecules together."]),
        PQ("Write a balanced equation for the complete combustion of ethane and name the products.",
           "2C2H6 + 7O2 -> 4CO2 + 6H2O. The products are carbon dioxide and water."),
        PQ("Calculate the mass of carbon dioxide formed when 6.0 g of ethane burns completely. (C = 12, H = 1, O = 16)",
           "Mr of C2H6 = 30, so n = 6.0 / 30 = 0.20 mol. 2 mol C2H6 give 4 mol CO2, so n(CO2) = 0.40 mol. Mr of CO2 = 44, so mass = 0.40 x 44 = 17.6 g."),
        PQ("Explain why a gas heater in a closed room can be dangerous.",
           "The oxygen supply is limited, so incomplete combustion occurs and carbon monoxide forms. Carbon monoxide is poisonous because it stops the blood from carrying oxygen, and it has no smell or colour."),
        PQ("Explain why methane does not decolourise bromine water in the dark but reacts with chlorine in sunlight.",
           "Methane is saturated, with strong single bonds, so it cannot take part in addition reactions with bromine water. Ultraviolet light supplies the energy to split chlorine molecules into radicals, which start a substitution chain reaction."),
        SUM("Alkanes are saturated hydrocarbons, CnH2n+2, with only single bonds; they are fairly unreactive.",
            "Complete combustion gives carbon dioxide and water; incomplete combustion gives carbon monoxide or soot and water.",
            "Carbon monoxide is a poisonous gas: always have fresh air when burning fuels.",
            "In sunlight, alkanes react with chlorine by free-radical substitution: CH4 + Cl2 gives CH3Cl + HCl.",
            "Substitution gives two products; it is different from addition."),
    ])]

# ============================================================================================
# 5. Alkenes and alkynes (lesson 1 of 2): ethene
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alkenes and alkynes",
    title="Ethene and the alkenes: addition reactions",
    slug="che-alkenes-ethene-addition", minutes=24,
    summary="Alkenes have a C=C double bond, CnH2n. They undergo addition with hydrogen, bromine, steam and hydrogen halides, and bromine water is the test for unsaturation.",
    objectives=[
        "Describe the structure of ethene and where alkenes come from",
        "Write equations for the addition of hydrogen, bromine, steam and hydrogen bromide to ethene",
        "Describe the test that distinguishes alkenes from alkanes",
        "Explain why alkenes burn with a smokier flame than alkanes, using percentage of carbon",
    ],
    key_concepts=["Alkene", "Double bond", "Addition reaction", "Hydrogenation", "Test for unsaturation", "Ethene"],
    blocks=[
        H("Introduction"),
        T("Green bananas from the plantations of Njombe and Penja ripen faster if they are put near a ripe banana. A gas called **ethene** is released by the ripe fruit and speeds up ripening in the others. "
          "Ethene, [[C2H4]], is the first alkene. It is also the most important raw material of the plastics industry."),
        D("**Alkenes** are unsaturated hydrocarbons that contain a **carbon-carbon double bond**, C=C. Their general formula is [[CnH2n]]. The first member is ethene, [[C2H4]], then propene, [[C3H6]].", title="Alkenes"),
        CODE("      H       H\n"
             "       \\     /\n"
             "        C = C          ethene, C2H4\n"
             "       /     \\\n"
             "      H       H", "text", title="Structure of ethene"),
        T("Alkenes are made by **cracking** alkanes (see the lesson on crude oil). Ethene can also be made by heating ethanol with a catalyst, which you will see in the lesson on ethanol."),
        D("An **addition reaction** is a reaction in which two molecules join to form **one** product. The double bond breaks and each carbon atom gains a new atom or group. Only unsaturated compounds can do this.", title="Addition reaction"),
        H("Addition reactions of ethene"),
        CODE("Reagent           Conditions                      Product\n"
             "hydrogen          nickel catalyst, about 150 °C    ethane\n"
             "bromine           room temperature, no catalyst    1,2-dibromoethane\n"
             "steam             phosphoric acid catalyst,        ethanol\n"
             "                  about 300 °C, 60-70 atm\n"
             "hydrogen bromide  room temperature (gas)           bromoethane", "text", title="Addition reactions of ethene (conditions are approximate; check your textbook)"),
        CODE("C2H4 + H2   -> C2H6          (hydrogenation)\n"
             "C2H4 + Br2  -> C2H4Br2       (1,2-dibromoethane)\n"
             "C2H4 + H2O  -> C2H5OH        (hydration, gives ethanol)\n"
             "C2H4 + HBr  -> C2H5Br        (bromoethane)", "text", title="Equations"),
        T("Look at the first equation. The two reactants join to make one product, and no atoms are lost. That is addition. Hydrogenation is used in industry to turn liquid vegetable oils, which are unsaturated, into solid fat for making margarine."),
        H("The test for unsaturation"),
        D("To test whether a hydrocarbon is unsaturated, shake it with **bromine water** (orange-brown). If it is an alkene (or alkyne) the colour **disappears quickly**: the bromine adds across the double bond. A saturated alkane does not change the colour in the dark.", title="Test for an alkene"),
        T("Acidified potassium manganate(VII) (purple) is also decolourised by alkenes, but it is also decolourised by other reducing substances, so bromine water is the preferred test. Check your textbook for the version your teacher uses."),
        EX("Worked example 1: mass from an addition reaction", intro="Calculate the mass of 1,2-dibromoethane formed when 14 g of ethene reacts completely with bromine. (C = 12, H = 1, Br = 80)",
           steps=[
               S("Equation", math=r"<<C2H4 + Br2 -> C2H4Br2>>"),
               S("Moles of ethene", math=r"M_r(\text{C}_2\text{H}_4) = 28;\quad n = \frac{14}{28} = 0.50\ \text{mol}"),
               S("Mole ratio 1 : 1", math=r"n(\text{C}_2\text{H}_4\text{Br}_2) = 0.50\ \text{mol}"),
               S("Mass", math=r"M_r = 24 + 4 + 160 = 188;\quad m = 0.50 \times 188 = 94\ \text{g}"),
           ]),
        EX("Worked example 2: why alkenes burn with a smokier flame", intro="Calculate the percentage of carbon by mass in ethane and in ethene and explain which burns with the sootier flame.",
           steps=[
               S("Ethane, C2H6 (Mr = 30)", math=r"\frac{24}{30} \times 100 = 80\%"),
               S("Ethene, C2H4 (Mr = 28)", math=r"\frac{24}{28} \times 100 = 85.7\%"),
               S("Conclusion", text="Ethene has a higher percentage of carbon, so in air there is not enough oxygen to burn all the carbon. Some carbon forms as soot, giving a smoky yellow flame."),
           ]),
        MISTAKE("Saying the bromine 'burns' or 'dissolves'", "Bromine water is decolourised because the bromine **reacts** with the double bond and forms a colourless compound. Write 'orange-brown to colourless'. Do not write 'clear': a clear solution can still be orange."),
        MISTAKE("Writing the product of addition with a double bond left", "After addition the double bond becomes a single bond. The product of ethene and hydrogen is ethane, not ethene with extra hydrogen."),
        TIP("Alkenes are examined in Paper 1 (products of addition, test for unsaturation) and in Paper 2 (equations and conditions; the Board's report advises learning the reagent, the condition and the products of each reaction). Learn the table in this lesson as a set.", title="Exam link"),
        QUIZ("Which observation shows that a gas is an alkene?", ["It burns with a blue flame", "It turns limewater milky", "It decolourises bromine water", "It turns red litmus blue"], 2,
             "Alkenes undergo addition with bromine, so orange-brown bromine water turns colourless.",
             hint="Which test works for a double bond?",
             feedback=["A blue flame suggests clean burning, not a double bond.", "Limewater tests for carbon dioxide.", "", "That tests for ammonia, an alkaline gas."]),
        QUIZ("What is the product when ethene reacts with steam in the presence of a catalyst?", ["Ethane", "Ethanol", "Ethanoic acid", "Poly(ethene)"], 1,
             "Water adds across the double bond: C2H4 + H2O gives C2H5OH, ethanol.",
             hint="Which atoms are added?",
             feedback=["Ethane needs hydrogen, not steam.", "", "Ethanoic acid needs oxidation of ethanol.", "Polymerization needs many ethene molecules, not steam."]),
        PQ("Write the equation for the reaction of ethene with bromine and state what is seen.",
           "C2H4 + Br2 -> C2H4Br2 (1,2-dibromoethane). The orange-brown bromine colour disappears and the mixture becomes colourless."),
        PQ("Explain why ethane does not decolourise bromine water but ethene does.",
           "Ethane is saturated: it has only single bonds, so it cannot undergo addition. Ethene has a C=C double bond, which breaks open so that bromine adds on."),
        PQ("Calculate the percentage of carbon in propene, [[C3H6]]. (C = 12, H = 1)",
           "Mr = 3 x 12 + 6 = 42. Percentage C = 36 / 42 x 100 = 85.7%."),
        PQ("Why are vegetable oils hardened with hydrogen to make margarine?",
           "The oils have C=C double bonds. Hydrogen adds across them (hydrogenation, with a nickel catalyst), making the molecules more saturated, so the oil changes from a liquid to a solid fat."),
        SUM("Alkenes are unsaturated hydrocarbons with a C=C double bond; general formula CnH2n; first member ethene, C2H4.",
            "Addition: two molecules join to give one product; ethene adds hydrogen, bromine, steam and hydrogen bromide.",
            "Test for unsaturation: bromine water goes from orange-brown to colourless.",
            "Alkenes burn with a smokier flame than alkanes because they have a higher percentage of carbon.",
            "Hydrogenation of vegetable oils makes margarine; alkenes are raw materials for plastics."),
    ])]

# ============================================================================================
# 6. Alkenes and alkynes (lesson 2 of 2): ethyne
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alkenes and alkynes",
    title="Ethyne and the alkynes",
    slug="che-alkynes-ethyne", minutes=20,
    summary="Alkynes have a C=-C triple bond, CnH2n-2. Ethyne is made from calcium carbide and water, burns with a very hot sooty flame and adds hydrogen, bromine and hydrogen chloride in two stages.",
    objectives=[
        "State the structure and general formula of the alkynes",
        "Describe the laboratory preparation of ethyne and write the equation",
        "Describe combustion of ethyne and the uses of the flame",
        "Write equations for the addition of hydrogen and bromine to ethyne and compare ethane, ethene and ethyne",
    ],
    key_concepts=["Alkyne", "Triple bond", "Ethyne", "Calcium carbide", "Two-stage addition", "Oxy-acetylene flame"],
    blocks=[
        H("Introduction"),
        T("A welder in a garage in Bafoussam joins two pieces of metal with a very bright, very hot flame. The gas in that flame is **ethyne** (also called acetylene), burned in pure oxygen. "
          "The flame is hotter than 3000 °C. Ethyne is the first member of the alkynes."),
        D("**Alkynes** are unsaturated hydrocarbons containing a **carbon-carbon triple bond**, C=-C (written with three lines). Their general formula is [[CnH2n-2]]. The first member is ethyne, [[C2H2]], then propyne, [[C3H4]].", title="Alkynes"),
        CODE("H - C = C - H      ethyne, C2H2   (the three lines between the carbons\n"
             "                  are a triple bond; the molecule is a straight line)", "text", title="Structure of ethyne"),
        H("Laboratory preparation"),
        D("Ethyne is prepared by adding **water** to **calcium carbide**, [[CaC2]]. The reaction is fast and gives off heat.", title="Preparation"),
        T("[[CaC2 + 2H2O -> Ca(OH)2 + C2H2]]"),
        T("Water is dripped slowly onto lumps of calcium carbide in a flask, and the gas is collected over water because ethyne is almost insoluble in water."),
        H("Combustion"),
        T("[[2C2H2 + 5O2 -> 4CO2 + 2H2O]]"),
        T("In air, ethyne burns with a very sooty, bright flame. Its percentage of carbon is the highest of the three hydrocarbons in the table below, so there is not enough oxygen in air to burn all of it. "
          "In pure oxygen the flame is much hotter and clean: the **oxy-acetylene torch** used for cutting and welding steel."),
        CODE("             ethane     ethene      ethyne\n"
             "formula      C2H6       C2H4        C2H2\n"
             "bond C-C     single     double      triple\n"
             "% carbon     80.0       85.7        92.3\n"
             "flame in air faint      smoky       very sooty\n"
             "bromine water  no       decolourised decolourised\n"
             "H2 it can add 0          1           2", "text", title="Ethane, ethene and ethyne compared"),
        H("Addition reactions"),
        T("The triple bond can add **two** molecules of a reagent, one after another. Each addition turns the triple bond to a double bond and then to a single bond."),
        CODE("C2H2 + H2    -> C2H4      (first stage, nickel catalyst)\n"
             "C2H4 + H2    -> C2H6      (second stage)\n"
             "overall:  C2H2 + 2H2 -> C2H6\n\n"
             "C2H2 + Br2   -> C2H2Br2     (1,2-dibromoethene)\n"
             "C2H2Br2 + Br2 -> C2H2Br4    (1,1,2,2-tetrabromoethane)\n"
             "overall:  C2H2 + 2Br2 -> C2H2Br4\n\n"
             "C2H2 + HCl   -> C2H3Cl      (chloroethene, used to make PVC)", "text", title="Addition reactions of ethyne"),
        T("Ethyne decolourises bromine water, like ethene, but takes up **twice** as much bromine."),
        EX("Worked example 1: mass of bromine", intro="Calculate the mass of bromine needed to convert 13 g of ethyne completely into 1,1,2,2-tetrabromoethane. (C = 12, H = 1, Br = 80)",
           steps=[
               S("Equation", math=r"<<C2H2 + 2Br2 -> C2H2Br4>>"),
               S("Moles of ethyne", math=r"M_r = 26;\quad n = \frac{13}{26} = 0.50\ \text{mol}"),
               S("Moles of bromine (ratio 1 : 2)", math=r"n(\text{Br}_2) = 2 \times 0.50 = 1.0\ \text{mol}"),
               S("Mass of bromine", math=r"M_r(\text{Br}_2) = 160;\quad m = 1.0 \times 160 = 160\ \text{g}"),
           ]),
        EX("Worked example 2: volume of oxygen", intro="What volume of oxygen is needed to burn 100 cm³ of ethyne completely, at the same temperature and pressure?",
           steps=[
               S("Equation", math=r"<<2C2H2 + 5O2 -> 4CO2 + 2H2O>>"),
               S("Ratio of volumes of gas C2H2 : O2 = 2 : 5", math=r"V(\text{O}_2) = \frac{5}{2} \times 100 = 250\ \text{cm}^3"),
           ]),
        MISTAKE("Forgetting that two stages are possible", "If the question says 'excess hydrogen' or 'excess bromine', ethyne takes up **two** molecules. If only one molecule is available, you stop at the alkene stage."),
        MISTAKE("Using the wrong test", "Both ethene and ethyne decolourise bromine water, so this test does not tell them apart. A smokier, sootier flame and the amount of bromine used are the clues."),
        TIP("Ethyne appears in Paper 1 (preparation, flame, the test) and Paper 2 structured and essay answers on reaction types. Safety: ethyne forms explosive mixtures with air. Never light the gas as it comes from the flask until the air is driven out.", title="Exam link"),
        QUIZ("What is the general formula of the alkynes?", [r"$\text{C}_n\text{H}_{2n-2}$", r"$\text{C}_n\text{H}_{2n}$", r"$\text{C}_n\text{H}_{2n+2}$", r"$\text{C}_n\text{H}_{n}$"], 0,
             "Alkynes have two hydrogen atoms fewer than alkenes: CnH2n-2. For n = 2 it gives C2H2.",
             hint="Take the alkene formula and remove two more hydrogen atoms for the extra bond.",
             feedback=["", "This is the alkene formula.", "This is the alkane formula.", "Not a general formula for alkynes: ethyne fits, but propyne C3H4 does not."]),
        QUIZ("Which pair of substances is used to prepare ethyne in the laboratory?", ["Calcium carbonate and hydrochloric acid", "Calcium carbide and water", "Ethanol and concentrated sulfuric acid", "Zinc and dilute sulfuric acid"], 1,
             "CaC2 + 2H2O gives Ca(OH)2 + C2H2.",
             hint="The name of the gas, acetylene, comes from the carbide.",
             feedback=["That gives carbon dioxide.", "", "That gives ethene.", "That gives hydrogen."]),
        PQ("Write the equation for the preparation of ethyne from calcium carbide.",
           "CaC2 + 2H2O -> Ca(OH)2 + C2H2."),
        PQ("Why does ethyne burn with a sooty flame in air but give a very hot, clean flame in pure oxygen?",
           "Ethyne has a very high percentage of carbon (92.3%), so there is not enough oxygen in air for complete combustion and soot (carbon) forms. In pure oxygen the combustion is complete, and the reaction releases much heat."),
        PQ("Write two equations to show the stepwise addition of hydrogen to ethyne.",
           "C2H2 + H2 -> C2H4 (ethene), then C2H4 + H2 -> C2H6 (ethane), using a nickel catalyst."),
        PQ("Ethyne reacts with hydrogen chloride to give a compound used to make PVC. Write the equation and name the product.",
           "C2H2 + HCl -> C2H3Cl. The product is chloroethene (vinyl chloride), the monomer of PVC."),
        SUM("Alkynes have a C=-C triple bond; general formula CnH2n-2; first member ethyne, C2H2.",
            "Ethyne is made from calcium carbide and water: CaC2 + 2H2O gives Ca(OH)2 + C2H2.",
            "It burns with a very sooty flame in air and a very hot flame in oxygen (welding).",
            "Ethyne adds two molecules of hydrogen, bromine or other reagents, in two stages.",
            "Bromine water is decolourised by both alkenes and alkynes."),
    ])]

# ============================================================================================
# 7. Alcohols (lesson 1 of 2): making ethanol
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alcohols",
    title="Alcohols and the fermentation of ethanol",
    slug="che-alcohols-ethanol-fermentation", minutes=22,
    summary="Alcohols contain the -OH group, CnH2n+1OH. Ethanol is made by fermentation of sugar with yeast (anaerobic, 25 to 35 °C) or by hydrating ethene with steam.",
    objectives=[
        "Name the first four alcohols, state their general formula and identify the -OH functional group",
        "Describe fermentation: raw materials, conditions, equation and the test for the gas",
        "Describe how ethanol is concentrated by fractional distillation",
        "Compare fermentation with the hydration of ethene and state uses and dangers of alcohols",
    ],
    key_concepts=["Alcohol", "Hydroxyl group", "Fermentation", "Yeast and enzymes", "Anaerobic", "Hydration of ethene"],
    blocks=[
        H("Introduction"),
        T("In the Western Highlands, sap tapped from raffia palms is left in a calabash. In a few hours it bubbles and becomes palm wine. In the north, sorghum is brewed to make local beer. "
          "In each case the sweet liquid has become an alcoholic drink. The key substance is **ethanol**, the best known member of the alcohol family."),
        D("**Alcohols** are organic compounds that contain the **hydroxyl group, -OH**. They form a homologous series with the general formula [[CnH2n+1OH]].", title="Alcohols"),
        CODE("Name         Formula    Structural formula\n"
             "methanol     CH3OH      CH3-OH\n"
             "ethanol      C2H5OH     CH3-CH2-OH\n"
             "propan-1-ol  C3H7OH     CH3-CH2-CH2-OH\n"
             "butan-1-ol   C4H9OH     CH3-CH2-CH2-CH2-OH", "text", title="The first four alcohols"),
        T("Alcohols with short chains mix completely with water. Ethanol is a colourless liquid that boils at 78 °C. It is a neutral liquid: it does not change the colour of litmus."),
        H("Fermentation"),
        D("**Fermentation** is the breaking down of sugar into ethanol and carbon dioxide by the enzymes in **yeast**, in the absence of air. An **enzyme** is a biological catalyst.", title="Fermentation"),
        T("[[C6H12O6 -> 2C2H5OH + 2CO2]]"),
        T("Glucose, [[C6H12O6]], comes from sugar cane, fruit juice, palm sap, or starch (such as cassava or maize) that has been broken down into sugar."),
        KEY("Conditions for fermentation", "Each condition has a reason. Examiners ask for the reason.",
            cards=[["Yeast", "Yeast contains the enzymes (zymase) that change glucose into ethanol."],
                   ["Warm, about 25 to 35 °C", "Too cold and the reaction is slow. Too hot and the enzymes are destroyed (denatured)."],
                   ["No air (anaerobic)", "With air, the ethanol is oxidised further to ethanoic acid and the drink turns sour."],
                   ["Dissolved sugar", "The reaction happens in a solution of sugar in water."]]),
        T("The carbon dioxide can be seen as bubbles. It turns **limewater milky**, which shows the fermentation is working. The fermentation stops when the ethanol reaches about 15% of the liquid, because ethanol at that concentration kills the yeast."),
        H("Concentrating ethanol"),
        T("To make a stronger drink or a fuel, the ethanol must be separated from the water. Ethanol boils at 78 °C and water boils at 100 °C. When the mixture is heated gently, ethanol vapour rises first. This is **fractional distillation**: the ethanol vapour condenses higher in the column and is collected."),
        H("Another route: hydrating ethene"),
        T("Ethanol can also be made from ethene and steam: [[C2H4 + H2O -> C2H5OH]], with a phosphoric acid catalyst at about 300 °C and 60 to 70 atmospheres."),
        CODE("                 Fermentation              Hydration of ethene\n"
             "raw material     sugar or starch           ethene from crude oil\n"
             "                 (renewable)               (not renewable)\n"
             "speed            slow (days)               fast\n"
             "type of process  batch                     continuous\n"
             "product          dilute, impure            very pure ethanol\n"
             "temperature      25 to 35 °C               about 300 °C", "text", title="Two ways to make ethanol"),
        EX("Worked example 1: mass of ethanol from glucose", intro="Calculate the mass of ethanol that can form from 180 g of glucose. (C = 12, H = 1, O = 16)",
           steps=[
               S("Equation", math=r"<<C6H12O6 -> 2C2H5OH + 2CO2>>"),
               S("Moles of glucose", math=r"M_r = 6(12) + 12 + 6(16) = 180;\quad n = \frac{180}{180} = 1.0\ \text{mol}"),
               S("Mole ratio glucose : ethanol = 1 : 2", math=r"n(\text{ethanol}) = 2.0\ \text{mol}"),
               S("Mass of ethanol", math=r"M_r(\text{C}_2\text{H}_5\text{OH}) = 46;\quad m = 2.0 \times 46 = 92\ \text{g}"),
           ]),
        EX("Worked example 2: percentage yield", intro="A brewer ferments 450 g of glucose and collects 184 g of ethanol. What is the percentage yield?",
           steps=[
               S("Maximum (theoretical) mass", math=r"n(\text{glucose}) = \frac{450}{180} = 2.5\ \text{mol};\quad n(\text{ethanol}) = 5.0\ \text{mol};\quad m = 5.0 \times 46 = 230\ \text{g}"),
               S("Percentage yield", math=r"\frac{184}{230} \times 100 = 80\%"),
           ]),
        H("Uses and dangers"),
        T("Ethanol is used as a solvent (in perfumes and medicines), as a fuel (bioethanol, often mixed with petrol), in hand sanitiser and antiseptics, and in alcoholic drinks. "
          "Alcohol harms the liver and brain, makes drivers dangerous, and is a risk for young people. **Methanol** is poisonous. Methylated spirit is ethanol made unfit to drink, so never drink it."),
        MISTAKE("Saying fermentation needs oxygen", "Fermentation is **anaerobic**: it needs no air. If air gets in, bacteria oxidise the ethanol to ethanoic acid and the drink becomes vinegar."),
        MISTAKE("Saying alcohols are bases because they contain OH", "The -OH in an alcohol is joined by a covalent bond to the carbon chain. It does not release hydroxide ions, so alcohols are neutral to litmus."),
        TIP("The Board's report says candidates were good at identifying alcohols and their uses but weaker on the reactivity of alcohols, and that the -OH group should be taught as the functional group. This lesson covers making and uses; the next lesson covers the reactions. Alcohols appear in Paper 1 and in Paper 2 structured questions.", title="Exam link"),
        QUIZ("Which condition is needed for the fermentation of glucose to ethanol?", ["A temperature of 300 °C", "A plentiful supply of air", "Yeast and a temperature of about 30 °C", "Concentrated sulfuric acid"], 2,
             "Yeast supplies the enzymes, and about 25 to 35 °C is warm enough for them to work without being destroyed.",
             hint="Enzymes work best at a mild temperature.",
             feedback=["300 °C is the temperature for hydrating ethene.", "Air would oxidise the ethanol to ethanoic acid.", "", "Concentrated sulfuric acid is used for other reactions, such as esterification."]),
        QUIZ("What is the formula of the functional group in alcohols?", ["-COOH", "C=C", "-OH", "-CHO"], 2,
             "The -OH (hydroxyl) group is the functional group of alcohols.",
             hint="Alcohols end in -ol.",
             feedback=["-COOH is the carboxyl group of acids.", "C=C is the group in alkenes.", "", "-CHO is the group in aldehydes, not in this lesson."]),
        PQ("Write the equation for the fermentation of glucose and name the two products.",
           "C6H12O6 -> 2C2H5OH + 2CO2. The products are ethanol and carbon dioxide."),
        PQ("State two conditions needed for fermentation and give the reason for each.",
           "Yeast, because it contains the enzymes that catalyse the reaction. A temperature of about 25 to 35 °C: lower is too slow and higher destroys the enzymes. (Absence of air, to prevent oxidation to ethanoic acid, is another.)"),
        PQ("Explain how ethanol can be separated from a fermented mixture of ethanol and water.",
           "By fractional distillation. Ethanol boils at 78 °C, water at 100 °C. On heating, ethanol vapour leaves first, and is condensed and collected."),
        PQ("Give one advantage of making ethanol by fermentation and one advantage of making it from ethene.",
           "Fermentation: it uses renewable raw materials (sugar or starch) and mild conditions. Hydration of ethene: it is fast, continuous and gives very pure ethanol."),
        SUM("Alcohols have the -OH group and the general formula CnH2n+1OH; the first four are methanol, ethanol, propan-1-ol and butan-1-ol.",
            "Fermentation: glucose gives ethanol and carbon dioxide, using yeast, about 25 to 35 °C and no air.",
            "Fractional distillation concentrates ethanol because it boils at 78 °C, lower than water.",
            "Ethanol can also be made by hydrating ethene with steam at about 300 °C and a catalyst.",
            "Ethanol is used as a solvent, a fuel and in drinks; methanol is poisonous."),
    ])]

# ============================================================================================
# 8. Alcohols (lesson 2 of 2): reactions
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Alcohols",
    title="Reactions of ethanol: oxidation, esterification and dehydration",
    slug="che-ethanol-reactions", minutes=24,
    summary="Ethanol burns, reacts with sodium, is oxidised to ethanoic acid, forms an ester with a carboxylic acid and is dehydrated to ethene. For each reaction learn the reagent, condition and product.",
    objectives=[
        "Write equations for the combustion of ethanol and its reaction with sodium",
        "Describe the oxidation of ethanol and the colour changes of the oxidising agents",
        "Describe esterification, name esters and write the equation",
        "Describe dehydration of ethanol to ethene with the conditions",
    ],
    key_concepts=["Oxidation of ethanol", "Acidified potassium dichromate", "Esterification", "Ester", "Dehydration", "Reaction with sodium"],
    blocks=[
        H("Introduction"),
        T("Palm wine left for two days in an open calabash tastes sour. Air has oxidised the ethanol in it into ethanoic acid, the acid in vinegar. "
          "That is one reaction of ethanol. This lesson covers the main ones. For each reaction, learn three things: the **reagent**, the **condition**, and the **products**."),
        CODE("Reaction        Reagent and condition                        Product\n"
             "combustion      oxygen, lit                                  CO2 and H2O\n"
             "with sodium     sodium metal                                 sodium ethoxide + H2\n"
             "oxidation       acidified K2Cr2O7 or KMnO4, warm             ethanoic acid\n"
             "esterification  ethanoic acid + conc. H2SO4 catalyst, warm   ethyl ethanoate + water\n"
             "dehydration     conc. H2SO4 at about 170 °C, or hot Al2O3    ethene + water", "text", title="Summary of the reactions of ethanol"),
        H("Combustion and reaction with sodium"),
        T("Ethanol burns with a clean, pale blue flame:\n\n[[C2H5OH + 3O2 -> 2CO2 + 3H2O]]"),
        T("Sodium reacts with ethanol, giving off hydrogen. The fizzing is gentler than with water. The hydrogen gives a squeaky pop with a lighted splint.\n\n[[2C2H5OH + 2Na -> 2C2H5ONa + H2]]\n\nThe product, [[C2H5ONa]], is sodium ethoxide. This reaction shows that the -OH group has a hydrogen atom that can be replaced."),
        H("Oxidation"),
        D("**Oxidation** of ethanol is its conversion into ethanoic acid (through ethanal) by an **oxidising agent**, which supplies oxygen, written [O].", title="Oxidation of ethanol"),
        T("[[C2H5OH + 2[O] -> CH3COOH + H2O]]"),
        CODE("Oxidising agent                       Colour change when ethanol is oxidised\n"
             "acidified potassium dichromate(VI)    orange to green\n"
             "acidified potassium manganate(VII)    purple to colourless", "text", title="Colour changes"),
        T("The colour change shows that an alcohol is present, because the oxidising agent has been reduced. Heat gently. In nature, bacteria in air do the same job and change palm wine or wine into vinegar."),
        H("Esterification"),
        D("**Esterification** is the reaction of an alcohol with a carboxylic acid to make an **ester** and water. Concentrated sulfuric acid is the catalyst, and the mixture is warmed. It is a **reversible** reaction.", title="Esterification"),
        T("[[C2H5OH + CH3COOH <=> CH3COOC2H5 + H2O]]"),
        T("The ester made here is **ethyl ethanoate**. To name an ester, write the alcohol part first (ethyl, from ethanol), then the acid part (ethanoate, from ethanoic acid). Esters have sweet, fruity smells. They are used in perfumes, food flavours and as solvents."),
        H("Dehydration"),
        D("**Dehydration** of ethanol is the removal of water from its molecule to form **ethene**. The conditions are concentrated sulfuric acid at about 170 °C (some books say 170 to 180 °C; check your textbook), or ethanol vapour passed over hot aluminium oxide.", title="Dehydration of ethanol"),
        T("[[C2H5OH -> C2H4 + H2O]]"),
        EX("Worked example 1: naming an ester", intro="Name the ester made from methanol and propanoic acid and give its molecular formula.",
           steps=[
               S("Alcohol part", text="Methanol gives **methyl**."),
               S("Acid part", text="Propanoic acid gives **propanoate**."),
               S("Name", text="The ester is **methyl propanoate**, CH3CH2COOCH3."),
               S("Molecular formula and mass", math=r"\text{C}_4\text{H}_8\text{O}_2;\quad M_r = 4(12) + 8 + 2(16) = 88"),
           ]),
        EX("Worked example 2: mass of ester with a percentage yield", intro="23 g of ethanol reacts with excess ethanoic acid. The percentage yield of ethyl ethanoate is 60%. Calculate the mass of ester obtained. (C = 12, H = 1, O = 16)",
           steps=[
               S("Moles of ethanol", math=r"M_r(\text{C}_2\text{H}_5\text{OH}) = 46;\quad n = \frac{23}{46} = 0.50\ \text{mol}"),
               S("Maximum ester (ratio 1 : 1)", math=r"M_r(\text{CH}_3\text{COOC}_2\text{H}_5) = 88;\quad 0.50 \times 88 = 44\ \text{g}"),
               S("Actual mass", math=r"44 \times \frac{60}{100} = 26.4\ \text{g}"),
           ]),
        MISTAKE("Saying the dichromate turns blue or colourless", "Acidified potassium dichromate(VI) changes from **orange to green**. Acidified potassium manganate(VII) changes from **purple to colourless**. Do not swap them."),
        MISTAKE("Naming the ester the wrong way round", "Ethanol and ethanoic acid make **ethyl ethanoate**, not 'ethanoyl ethanol'. Alcohol part first, acid part second, ending -oate."),
        TIP("The Board's report says candidates struggled with the reactivity of alcohols, and suggests learning the reagent, condition and products of each reaction. Ethanol reactions appear in Paper 1 (colour changes, products) and Paper 2, where an equation and conditions are often asked.", title="Exam link"),
        QUIZ("What colour change is seen when ethanol is warmed with acidified potassium dichromate(VI)?", ["Green to orange", "Orange to green", "Purple to colourless", "Colourless to blue"], 1,
             "The dichromate is reduced as the alcohol is oxidised: orange to green.",
             hint="Dichromate starts orange.",
             feedback=["The change is the other way round.", "", "That is potassium manganate(VII).", "Neither oxidising agent gives this change."]),
        QUIZ("Which are the products of the reaction of ethanol with ethanoic acid and a little concentrated sulfuric acid?", ["Ethene and water", "Ethyl ethanoate and water", "Sodium ethoxide and hydrogen", "Carbon dioxide and water"], 1,
             "This is esterification: alcohol + acid gives ester + water.",
             hint="Name the reaction first.",
             feedback=["That is dehydration, with sulfuric acid alone.", "", "That is the reaction with sodium.", "These are the products of burning."]),
        PQ("Describe what you would see when a small piece of sodium is added to ethanol and name the gas given off.",
           "The sodium fizzes (more slowly than with water) and dissolves, and a gas is given off that gives a squeaky pop with a lighted splint. The gas is hydrogen."),
        PQ("Write the equation for the dehydration of ethanol and state the conditions.",
           "C2H5OH -> C2H4 + H2O. Conditions: concentrated sulfuric acid at about 170 °C, or the vapour passed over heated aluminium oxide."),
        PQ("Write the equation for the preparation of ethyl ethanoate and state the catalyst.",
           "C2H5OH + CH3COOH <=> CH3COOC2H5 + H2O. The catalyst is concentrated sulfuric acid."),
        PQ("Calculate the maximum mass of ethyl ethanoate that can be made from 69 g of ethanol and excess ethanoic acid. (C = 12, H = 1, O = 16)",
           "Mr of ethanol = 46; n = 69/46 = 1.5 mol. Ratio 1 : 1, so n(ester) = 1.5 mol. Mr of ester = 88, so mass = 1.5 x 88 = 132 g."),
        SUM("Ethanol burns to give carbon dioxide and water, and reacts with sodium to give hydrogen and sodium ethoxide.",
            "Oxidation (acidified dichromate or permanganate, warm) gives ethanoic acid: orange to green, or purple to colourless.",
            "Esterification: ethanol + ethanoic acid with concentrated sulfuric acid gives ethyl ethanoate + water (reversible).",
            "Dehydration: concentrated sulfuric acid at about 170 °C, or hot aluminium oxide, gives ethene.",
            "For every reaction learn: reagent, condition, product."),
    ])]

# ============================================================================================
# 9. Carboxylic acids
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Carboxylic acids, soaps and detergents",
    title="Ethanoic acid and the carboxylic acids",
    slug="che-ethanoic-acid-carboxylic-acids", minutes=22,
    summary="Carboxylic acids contain -COOH and are weak acids. Ethanoic acid reacts with metals, carbonates and bases like other acids, and forms esters with alcohols.",
    objectives=[
        "Name the first three carboxylic acids and state their general formula",
        "Describe how ethanoic acid is made by oxidation of ethanol",
        "Explain why ethanoic acid is a weak acid and write the equilibrium for its ionization",
        "Write equations for reactions of ethanoic acid with a metal, a carbonate, a base and an alcohol",
    ],
    key_concepts=["Carboxylic acid", "Carboxyl group", "Weak acid", "Partial ionization", "Salt of ethanoic acid", "Vinegar"],
    blocks=[
        H("Introduction"),
        T("Vinegar on a salad, the sting of a red ant (methanoic acid), the sour taste of spoiled palm wine: all of these involve **carboxylic acids**. "
          "Vinegar is a solution containing about 5% ethanoic acid. Carboxylic acids are the organic acids."),
        D("**Carboxylic acids** are organic compounds that contain the **carboxyl group, -COOH**. The general formula is [[CnH2n+1COOH]].", title="Carboxylic acids"),
        CODE("Name        Formula    Notes\n"
             "methanoic   HCOOH      in ant stings\n"
             "ethanoic    CH3COOH    in vinegar\n"
             "propanoic   C2H5COOH   used to preserve food", "text", title="The first three carboxylic acids"),
        T("Note the name: the carbon of the -COOH group is counted in the chain. Ethanoic acid has **two** carbon atoms."),
        H("Making ethanoic acid"),
        T("Ethanoic acid is made by **oxidising ethanol**, using acidified potassium dichromate(VI) or by bacteria and air:"),
        T("[[C2H5OH + 2[O] -> CH3COOH + H2O]]"),
        H("A weak acid"),
        D("A **weak acid** is an acid that ionizes **only partly** in water. A **strong acid** (such as hydrochloric acid) ionizes completely.", title="Weak acid"),
        T("In ethanoic acid solution, only a small fraction of the molecules ionize. Most remain as molecules. The reaction is reversible:"),
        T("[[CH3COOH <=> CH3COO^- + H^+]]"),
        T("Because few hydrogen ions are present, a solution of ethanoic acid has a higher pH than a hydrochloric acid solution of the same concentration, and it reacts less vigorously with magnesium."),
        H("Reactions of ethanoic acid"),
        CODE("with a metal:      2CH3COOH + Mg -> (CH3COO)2Mg + H2\n"
             "with a carbonate: 2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2\n"
             "with an alkali:   CH3COOH + NaOH -> CH3COONa + H2O\n"
             "with an alcohol:  CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O", "text", title="Typical acid reactions"),
        T("The salts made have names ending in **-oate**: magnesium ethanoate, sodium ethanoate. The carbonate reaction gives **effervescence** (bubbles of carbon dioxide). It turns litmus red but does not turn it as strongly red as a strong acid."),
        EX("Worked example 1: the concentration of vinegar", intro="25.0 cm³ of diluted vinegar is neutralised by 20.0 cm³ of 0.500 mol/dm³ sodium hydroxide. Find the concentration of ethanoic acid in the diluted vinegar.",
           steps=[
               S("Equation", math=r"<<CH3COOH + NaOH -> CH3COONa + H2O>>"),
               S("Moles of NaOH", math=r"n = 0.500 \times \frac{20.0}{1000} = 0.0100\ \text{mol}"),
               S("Moles of acid (ratio 1 : 1)", math=r"n(\text{CH}_3\text{COOH}) = 0.0100\ \text{mol}"),
               S("Concentration", math=r"c = \frac{0.0100}{25.0/1000} = 0.400\ \text{mol/dm}^3"),
           ]),
        EX("Worked example 2: gas from a carbonate", intro="What mass of sodium carbonate is needed to react completely with ethanoic acid to give 0.10 mol of carbon dioxide? (Na = 23, C = 12, O = 16)",
           steps=[
               S("Equation", math=r"<<2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2>>"),
               S("Mole ratio Na2CO3 : CO2 = 1 : 1", math=r"n(\text{Na}_2\text{CO}_3) = 0.10\ \text{mol}"),
               S("Mass", math=r"M_r = 2(23) + 12 + 3(16) = 106;\quad m = 0.10 \times 106 = 10.6\ \text{g}"),
           ]),
        T("Uses of ethanoic acid: vinegar for cooking and preserving, making esters, making plastics and artificial fibres, and as a solvent."),
        MISTAKE("Confusing strong with concentrated", "**Weak** and **strong** tell how much an acid ionizes. **Concentrated** and **dilute** tell how much acid is dissolved. You can have a dilute solution of a strong acid or a concentrated solution of a weak acid."),
        MISTAKE("Counting the carbon atoms wrongly", "In ethanoic acid, CH3COOH, the -COOH carbon is one of the two carbon atoms. Propanoic acid has three carbon atoms, C2H5COOH."),
        TIP("Carboxylic acids appear in Paper 1 (names, formulae, weak acid) and Paper 2 (equations for the acid reactions and esterification; titration calculations with vinegar are common in practical-type questions).", title="Exam link"),
        QUIZ("Which equation shows ethanoic acid acting as a weak acid?", ["CH3COOH -> CH3COO- + H+ (goes to completion)", "CH3COOH <=> CH3COO- + H+ (only slightly ionized)", "CH3COOH + H2 -> C2H5OH", "CH3COOH -> CO2 + H2O"], 1,
             "The reversible arrow shows that ionization is partial, and that is what makes it a weak acid.",
             hint="Look for the two-way arrow.",
             feedback=["That would be a strong acid.", "", "This is not ionization.", "This is not ionization."]),
        QUIZ("What are the products of ethanoic acid and sodium carbonate?", ["Sodium ethanoate, water and carbon dioxide", "Sodium ethanoate and hydrogen", "Ethyl ethanoate and water", "Sodium hydroxide and ethanol"], 0,
             "Like other acids, ethanoic acid reacts with a carbonate to give a salt, water and carbon dioxide.",
             hint="An acid plus a carbonate gives a salt, water and carbon dioxide.",
             feedback=["", "Hydrogen is given off with metals, not carbonates.", "That is esterification, which needs an alcohol.", "No such reaction."]),
        PQ("Write the formula of propanoic acid and the equation for its reaction with sodium hydroxide.",
           "Propanoic acid is C2H5COOH. C2H5COOH + NaOH -> C2H5COONa + H2O (sodium propanoate and water)."),
        PQ("Explain why ethanoic acid is a weak acid.",
           "It ionizes only partly in water: CH3COOH <=> CH3COO- + H+. Most molecules stay un-ionized, so the concentration of H+ is low."),
        PQ("State what is seen when magnesium ribbon is added to ethanoic acid and name the gas.",
           "The magnesium fizzes and dissolves, more slowly than in hydrochloric acid of the same concentration. The gas is hydrogen (squeaky pop)."),
        PQ("A titration needs 15.0 cm³ of 0.100 mol/dm³ sodium hydroxide to neutralise 25.0 cm³ of ethanoic acid. Calculate the concentration of the acid.",
           "n(NaOH) = 0.100 x 15.0/1000 = 0.00150 mol. The ratio is 1 : 1, so n(acid) = 0.00150 mol. c = 0.00150 / 0.0250 = 0.0600 mol/dm³."),
        SUM("Carboxylic acids contain -COOH; general formula CnH2n+1COOH; methanoic, ethanoic and propanoic acid are the first three.",
            "Ethanoic acid is made by oxidising ethanol.",
            "It is a weak acid: partial ionization, CH3COOH <=> CH3COO- + H+.",
            "It reacts with metals (hydrogen), carbonates (carbon dioxide), alkalis (salt + water) and alcohols (ester + water).",
            "The salts have names ending in -oate."),
    ])]

# ============================================================================================
# 10. Soaps and detergents
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Carboxylic acids, soaps and detergents",
    title="Soaps, saponification and detergents",
    slug="che-soaps-saponification-detergents", minutes=24,
    summary="Soap is made by heating a fat or oil with sodium hydroxide (saponification). Soap and detergent molecules have a water-loving head and a grease-loving tail, but soap forms scum in hard water.",
    objectives=[
        "State that fats and oils are esters of glycerol and long-chain fatty acids",
        "Describe saponification and write the equation",
        "Explain the cleaning action of soap using the head and tail of the molecule",
        "Compare soap and soapless detergents, including hard water and the environment",
    ],
    key_concepts=["Fat and oil", "Saponification", "Soap", "Glycerol", "Hydrophilic and hydrophobic", "Soapless detergent", "Scum"],
    blocks=[
        H("Introduction"),
        T("In many villages, soap is made at home from palm oil or palm kernel oil mixed with caustic soda, or with a strong solution of ash from burnt plantain peels. "
          "The mixture is stirred and heated until it thickens. The substance that forms is soap. This lesson explains the chemistry."),
        D("**Fats and oils** are esters made from **glycerol** (propane-1,2,3-triol) and three **fatty acids**, which are long-chain carboxylic acids. Fats are solid at room temperature. Oils are liquid.", title="Fats and oils"),
        H("Saponification"),
        D("**Saponification** is the hydrolysis of a fat or oil by a hot alkali (such as sodium hydroxide) to give **soap** and **glycerol**. Soap is the **sodium salt of a long-chain fatty acid**. (Potassium hydroxide gives potassium soaps, which are softer.)", title="Saponification"),
        CODE("fat or oil + 3NaOH(aq)  ->  3 soap + glycerol\n\n"
             "(C17H35COO)3C3H5 + 3NaOH -> 3C17H35COONa + C3H5(OH)3\n"
             "  tristearin                  sodium stearate   glycerol", "text", title="Making soap from tristearin"),
        T("After heating, common salt is added. Soap is less soluble in salty water, so it floats as a solid layer. This is called **salting out**. The glycerol stays in the solution. The soap is then pressed into bars."),
        EX("Worked example 1: mass of soap", intro="Calculate the mass of sodium stearate formed when 89 g of tristearin is completely saponified. (C = 12, H = 1, O = 16, Na = 23)",
           steps=[
               S("Masses", math=r"M_r(\text{tristearin}) = 57(12) + 110 + 6(16) = 890;\quad M_r(\text{C}_{17}\text{H}_{35}\text{COONa}) = 306"),
               S("Moles of tristearin", math=r"n = \frac{89}{890} = 0.10\ \text{mol}"),
               S("Mole ratio 1 : 3", math=r"n(\text{soap}) = 0.30\ \text{mol}"),
               S("Mass of soap", math=r"m = 0.30 \times 306 = 91.8\ \text{g}"),
           ]),
        H("How soap cleans"),
        IMG("f5ch-e-soap-micelle.svg", alt="Left: one soap molecule drawn as a round head with a zigzag tail. Right: a grease droplet surrounded by soap molecules with their tails in the grease and their heads pointing out into the water.",
            caption="Figure 1. A soap molecule (left) and how soap molecules surround a drop of grease (right)."),
        KEY("Two ends, two jobs", "A soap molecule has two parts.",
            cards=[["Head: hydrophilic", "The charged -COO-Na+ end is attracted to water. 'Hydrophilic' means water-loving."],
                   ["Tail: hydrophobic", "The long hydrocarbon chain is not attracted to water but dissolves in grease and oil. 'Hydrophobic' means water-hating."]]),
        T("Grease does not mix with water, so water alone does not remove oily dirt. The tails of soap molecules dissolve in the grease. The heads stay in the water. "
          "Rubbing breaks the grease into small drops, each surrounded by soap molecules, with heads outwards. The drops are kept apart and are washed away with the water. This mixture of tiny droplets in water is an **emulsion**."),
        H("Hard water and detergents"),
        T("**Hard water** contains calcium or magnesium ions, [[Ca^2+]] and [[Mg^2+]]. These ions combine with soap anions to form an insoluble solid called **scum**:"),
        T("[[Ca^2+ + 2C17H35COO^- -> (C17H35COO)2Ca]]"),
        T("Scum wastes soap, and it makes a grey layer on clothes and in basins. More soap is needed before lather forms."),
        D("**Soapless detergents** are cleaning agents made from petroleum, not from fats. A common one is a sodium alkylbenzenesulfonate. Its molecule has a long hydrocarbon tail and a sulfonate head, [[-SO3^- Na^+]]. Their calcium and magnesium salts are **soluble**, so they do not form scum in hard water.", title="Soapless detergents"),
        CODE("                    Soap                        Soapless detergent\n"
             "made from           fats or oils + alkali       petroleum products\n"
             "in hard water       forms scum                  no scum\n"
             "in acidic water     forms insoluble fatty acid  still works\n"
             "environment         biodegradable               branched chains do not rot;\n"
             "                                                straight chains do", "text", title="Soap and detergent compared"),
        T("A **biodegradable** substance is broken down by bacteria. Old detergents with branched chains were not, and made foam in rivers. Modern detergents use straight chains that bacteria can break down. "
          "Some detergents contain phosphates. These feed algae in rivers and ponds and cause the water to turn green and lose oxygen."),
        MISTAKE("Saying the soap and the glycerol are the same", "Saponification gives two products. **Soap** is the sodium salt of the fatty acid. **Glycerol** is the alcohol. They are separated by salting out."),
        MISTAKE("Saying detergents are better because they are 'stronger'", "Detergents are better in hard water because their calcium salts are soluble. In soft water soap is as effective, and it is biodegradable."),
        TIP("Soaps and detergents appear in Paper 1 (saponification, hard water, cleaning action) and in Paper 2. A good answer names the reagent and conditions (a fat or oil with hot sodium hydroxide) and the two products.", title="Exam link"),
        QUIZ("What are the two products of the saponification of a fat with sodium hydroxide?", ["Soap and glycerol", "Soap and ethanol", "Detergent and water", "A fatty acid and carbon dioxide"], 0,
             "Hydrolysis of the fat by alkali gives the sodium salt of the fatty acid (soap) and glycerol.",
             hint="One is a salt and the other is an alcohol with three -OH groups.",
             feedback=["", "The alcohol part of a fat is glycerol, not ethanol.", "Detergent is not made by this reaction.", "These are not made by saponification."]),
        QUIZ("Why does soap form scum in hard water?", ["The soap anions react with calcium or magnesium ions to form an insoluble compound", "Hard water is acidic", "Hard water is too cold", "Soap is too concentrated"], 0,
             "Ca2+ or Mg2+ ions combine with the soap anions to make insoluble calcium or magnesium salts.",
             hint="Think of the ions that make water hard.",
             feedback=["", "Hardness is caused by calcium and magnesium ions, not acid.", "Temperature does not cause scum.", "Scum is a chemical reaction, not a matter of quantity."]),
        PQ("Write the equation for the saponification of tristearin with sodium hydroxide.",
           "(C17H35COO)3C3H5 + 3NaOH -> 3C17H35COONa + C3H5(OH)3."),
        PQ("Describe how the soap molecule removes grease from a dirty plate.",
           "The hydrophobic tails dissolve in the grease; the hydrophilic heads stay in the water. The grease is broken into droplets surrounded by soap molecules with heads outwards, so the droplets stay in the water and are rinsed away."),
        PQ("Why is a soapless detergent better than soap in hard water?",
           "Its calcium and magnesium salts are soluble, so no scum forms, and it lathers and cleans in hard water."),
        PQ("Give one environmental problem caused by detergents and one way to reduce it.",
           "Branched-chain detergents are not biodegradable and cause foam in rivers; phosphates cause algae to grow. Use biodegradable straight-chain detergents and phosphate-free products."),
        SUM("Fats and oils are esters of glycerol and fatty acids; saponification with hot sodium hydroxide gives soap and glycerol.",
            "Soap is the sodium salt of a long-chain fatty acid; salting out separates it.",
            "A soap molecule has a hydrophilic head and a hydrophobic tail; the tail dissolves in grease and the head in water.",
            "In hard water soap forms scum with Ca2+ and Mg2+; soapless detergents do not.",
            "Biodegradable detergents with straight chains are better for the environment."),
    ])]

# ============================================================================================
# 11. Polymers
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Natural and synthetic polymers",
    title="Addition and condensation polymers",
    slug="che-polymers-addition-condensation", minutes=26,
    summary="Polymers are long molecules built from many monomers. Addition polymers form from alkenes with no loss of atoms; condensation polymers lose a small molecule such as water at each link.",
    objectives=[
        "Define monomer, polymer and polymerization",
        "Describe addition polymerization, name common addition polymers and draw the repeat unit",
        "Describe condensation polymerization, with nylon and polyesters as examples",
        "Name natural polymers (starch, cellulose, protein, rubber) and discuss plastic waste",
    ],
    key_concepts=["Monomer", "Polymer", "Addition polymerization", "Condensation polymerization", "Repeat unit", "Natural polymer", "Biodegradable"],
    blocks=[
        H("Introduction"),
        T("A plastic bucket in a market in Douala, a nylon rope on a fishing boat at Kribi, a cotton shirt, a cassava root and the protein in a piece of fish are all made of **polymers**. "
          "The word means 'many parts'. Some polymers are made by nature, others by chemists."),
        D("A **monomer** is a small molecule that can join with many others. A **polymer** is a very long molecule made of many monomer units joined together. **Polymerization** is the reaction that joins the monomers.", title="Definitions"),
        H("Addition polymers"),
        D("In **addition polymerization**, many unsaturated monomers (usually alkenes) join by opening their double bonds. **No atom is lost**, so the polymer has the same empirical formula as the monomer.", title="Addition polymerization"),
        CODE("   H   H                 H   H\n"
             "   |   |                 |   |\n"
             "n  C = C      ->      ( - C - C - )n\n"
             "   |   |                 |   |\n"
             "   H   H                 H   H\n"
             "  ethene               poly(ethene)\n\n"
             "n CH2=CH2  ->  (-CH2-CH2-)n", "text", title="Addition polymerization of ethene"),
        T("The part in the bracket is the **repeat unit**. The letter n is a very large number, often thousands. Conditions: high pressure and a catalyst (check your textbook for the exact values)."),
        CODE("Monomer                  Polymer          Uses\n"
             "ethene                   poly(ethene)     bags, bowls, bottles\n"
             "propene                  poly(propene)    ropes, crates\n"
             "chloroethene             PVC              water pipes, cable insulation\n"
             "tetrafluoroethene        PTFE             non-stick pans\n"
             "phenylethene (styrene)   polystyrene      packaging, food boxes", "text", title="Common addition polymers"),
        EX("Worked example 1: drawing a repeat unit", intro="Chloroethene is CH2=CHCl. Write the repeat unit of PVC and calculate the relative mass of a PVC molecule with 800 repeat units. (C = 12, H = 1, Cl = 35.5)",
           steps=[
               S("Open the double bond", text="Each monomer becomes -CH2-CHCl- in the chain: the repeat unit is [[CH2CHCl]] (the same atoms as the monomer, C2H3Cl)."),
               S("Mass of one repeat unit", math=r"M_r = 2(12) + 3(1) + 35.5 = 62.5"),
               S("Mass of the polymer", math=r"800 \times 62.5 = 50\,000"),
           ]),
        H("Condensation polymers"),
        D("In **condensation polymerization**, monomers with **two functional groups** each join and a **small molecule** (usually water) is **lost** at each link. The polymer has less mass than the monomers.", title="Condensation polymerization"),
        CODE("Nylon (a polyamide):  diamine + dicarboxylic acid\n"
             "  H2N-(CH2)6-NH2  +  HOOC-(CH2)4-COOH\n"
             "  -> -NH-(CH2)6-NH-CO-(CH2)4-CO-  + H2O  (repeated many times)\n"
             "  link: -CONH-  (the amide link)\n\n"
             "Polyester:  diol + dicarboxylic acid\n"
             "  link: -COO-  (the ester link)", "text", title="Condensation polymers"),
        T("Nylon makes ropes, fishing nets and clothes. The polyester called PET makes drink bottles and fibres for clothes. The links in these polymers are like the links in natural proteins and fats."),
        EX("Worked example 2: mass lost on joining", intro="One molecule of hexane-1,6-diamine ([[C6H16N2]]) joins one molecule of hexanedioic acid ([[C6H10O4]]) with the loss of one water molecule. Find the relative mass of the product. (C = 12, H = 1, N = 14, O = 16)",
           steps=[
               S("Masses of the monomers", math=r"M_r(\text{diamine}) = 116;\quad M_r(\text{diacid}) = 146"),
               S("Add and subtract water (18)", math=r"116 + 146 - 18 = 244"),
               S("Check the formula", text="The product has formula [[C12H24N2O3]]: 12 x 12 + 24 + 2 x 14 + 3 x 16 = 244."),
           ]),
        H("Natural polymers"),
        CODE("Natural polymer   Monomer             Type          Where\n"
             "starch            glucose             condensation  cassava, plantain, maize\n"
             "cellulose         glucose             condensation  wood, cotton\n"
             "protein           amino acids         condensation  meat, fish, beans\n"
             "natural rubber    isoprene            addition      rubber trees", "text", title="Natural polymers"),
        T("In the body, enzymes break starch into glucose and proteins into amino acids. This is the reverse of condensation and is called **hydrolysis**. In a protein the link between amino acids is the **peptide link**, -CONH-, the same as the amide link in nylon."),
        H("Plastic waste"),
        T("Most synthetic polymers are **not biodegradable**. Plastic bags block drains and cause floods in towns. Burning plastics gives toxic gases (PVC gives hydrogen chloride). Cameroon has laws that limit non-biodegradable plastic packaging. "
          "Better choices are to reuse and recycle plastics, and to use biodegradable plastics where possible."),
        MISTAKE("Saying a condensation polymer has no other product", "A condensation polymer is always formed together with a small molecule such as water. An addition polymer is the only product."),
        MISTAKE("Forgetting to keep the bracket and n", "The formula of a polymer is the repeat unit in a bracket with n outside. Do not write the monomer alone, and do not leave the bonds at the ends of the bracket out."),
        TIP("Polymers appear in Paper 1 (monomers, repeat units, types) and in Paper 2 essays on types of reactions. The Board's report asks for a definition and an equation as an example when writing short notes.", title="Exam link"),
        QUIZ("What is the monomer of poly(ethene)?", ["Ethane", "Ethene", "Ethanol", "Ethanoic acid"], 1,
             "Poly(ethene) is made by joining many ethene molecules, CH2=CH2.",
             hint="The name tells you: poly + the monomer.",
             feedback=["Ethane is saturated and cannot polymerize by addition.", "", "Ethanol is an alcohol.", "Ethanoic acid is a carboxylic acid."]),
        QUIZ("Which statement describes condensation polymerization?", ["Alkenes join and no atoms are lost", "Monomers join and a small molecule such as water is lost", "A polymer breaks into monomers", "A polymer is dissolved in water"], 1,
             "In condensation polymerization a small molecule is lost at each link.",
             hint="What does 'condensation' mean in the water cycle?",
             feedback=["That is addition polymerization.", "", "That is hydrolysis.", "Dissolving is not a reaction."]),
        PQ("Write the equation for the polymerization of propene.",
           "n CH3CH=CH2 -> (-CH(CH3)-CH2-)n. The product is poly(propene)."),
        PQ("Explain the difference between addition and condensation polymerization.",
           "In addition polymerization alkene monomers with a C=C bond join, the double bond opens, and there is only one product. In condensation polymerization monomers with two functional groups join and a small molecule such as water is lost at each link."),
        PQ("Name two natural polymers and the monomers they are made from.",
           "Starch and cellulose are made from glucose; proteins are made from amino acids; natural rubber is made from isoprene (any two)."),
        PQ("Give two environmental problems caused by plastics and one way to reduce them.",
           "They are not biodegradable, so they build up and block drains; burning them gives toxic gases (for example hydrogen chloride from PVC). Reduce by reusing, recycling and using biodegradable materials."),
        SUM("A polymer is a long molecule made of many monomers joined by polymerization.",
            "Addition polymers (poly(ethene), PVC) come from alkenes; the double bond opens and no atom is lost.",
            "Condensation polymers (nylon, polyesters) lose a small molecule such as water at each link.",
            "Natural polymers: starch and cellulose (glucose), proteins (amino acids), rubber (isoprene).",
            "Most plastics are not biodegradable: reuse, recycle and reduce."),
    ])]

# ============================================================================================
# 12. Qualitative analysis (lesson 1 of 2): cations
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Qualitative analysis",
    title="Identifying cations with sodium hydroxide and ammonia",
    slug="che-qualitative-analysis-cations", minutes=24,
    summary="Add sodium hydroxide, then ammonia solution, a little at a time and then in excess. The colour of the precipitate and whether it dissolves identify NH4+, Ca2+, Zn2+, Pb2+, Cu2+, Fe2+ and Fe3+.",
    objectives=[
        "Explain what qualitative analysis is and record observations and inferences correctly",
        "Carry out the tests for cations with dilute sodium hydroxide and ammonia solution, dropwise and in excess",
        "Use a table of results to identify NH4+, Ca2+, Zn2+, Pb2+, Cu2+, Fe2+ and Fe3+",
        "Write ionic equations for the formation of the hydroxide precipitates",
    ],
    key_concepts=["Qualitative analysis", "Precipitate", "Excess", "Observation and inference", "Cation tests", "Ionic equation"],
    blocks=[
        H("Introduction"),
        T("A farmer near Mount Cameroon notices that the water of a spring leaves a rusty-brown stain on rocks. A school laboratory can find out which metal ion is in it, without any machine. "
          "The method is **qualitative analysis**: finding out *what* is present, not *how much*."),
        D("**Qualitative analysis** is the identification of the ions or compounds present in a sample by carrying out chemical tests and observing the results. A **precipitate** is an insoluble solid that forms when two solutions are mixed.", title="Qualitative analysis"),
        KEY("How to carry out the test", "The Board's report says candidates must show good laboratory procedure. Follow these steps:",
            cards=[["1. Look first", "Note the colour of the solid or solution. Cu2+ salts are blue. Fe2+ is pale green. Fe3+ is yellow-brown. The rest are colourless."],
                   ["2. Add dropwise", "Put about 2 cm of the solution in a test tube. Add dilute sodium hydroxide **a few drops at a time** and note any precipitate and its colour."],
                   ["3. Add in excess", "Keep adding until the tube is about half full. Does the precipitate dissolve? Note the colour of the solution."],
                   ["4. Repeat with ammonia", "Use a new sample with ammonia solution, again dropwise, then in excess."]]),
        T("Always write **what you see** (the observation), such as 'a pale blue precipitate that does not dissolve in excess'. Then write **what you deduce** (the inference), such as 'Cu2+ is present'. Do not write the inference in place of the observation."),
        CODE("Ion     Sodium hydroxide, a little then excess       Ammonia solution, a little then excess\n"
             "Ca2+    white ppt, insoluble in excess               no ppt, or a very slight white ppt\n"
             "Zn2+    white ppt, dissolves in excess               white ppt, dissolves in excess\n"
             "Pb2+    white ppt, dissolves in excess               white ppt, insoluble in excess\n"
             "Cu2+    light blue ppt, insoluble in excess          light blue ppt, dissolves in excess\n"
             "                                                     to give a deep blue solution\n"
             "Fe2+    green ppt, insoluble in excess               green ppt, insoluble in excess\n"
             "        (turns brown on standing in air)\n"
             "Fe3+    red-brown ppt, insoluble in excess           red-brown ppt, insoluble in excess\n"
             "NH4+    no ppt; on warming, ammonia gas is given     (ammonia solution is not used for\n"
             "        off (turns damp red litmus paper blue)        this ion)", "text",
             title="Tests for cations (ppt = precipitate). Check the shade of colours against your textbook."),
        T("The ionic equation for each precipitate shows the metal ion joining with hydroxide ions from the alkali."),
        T("[[Cu^2+ + 2OH^- -> Cu(OH)2]]   (light blue)"),
        T("[[Fe^2+ + 2OH^- -> Fe(OH)2]]   (green)"),
        T("[[Fe^3+ + 3OH^- -> Fe(OH)3]]   (red-brown)"),
        T("[[Ca^2+ + 2OH^- -> Ca(OH)2]]   (white)"),
        T("Zinc hydroxide and lead(II) hydroxide are **amphoteric**: they dissolve in excess alkali. For zinc, [[Zn(OH)2 + 2OH^- -> [Zn(OH)4]^2-]] gives a colourless solution. "
          "Ammonia solution dissolves the precipitates of zinc hydroxide and copper(II) hydroxide by making soluble complex ions, but not lead(II) hydroxide."),
        T("For ammonium ions the reaction is [[NH4^+ + OH^- -> NH3 + H2O]]. The ammonia gas has a sharp smell and turns damp red litmus paper blue."),
        KEY("Telling the white precipitates apart", "Three ions give a white precipitate with sodium hydroxide: Ca2+, Zn2+ and Pb2+. Use excess reagents.",
            cards=[["Insoluble in excess NaOH", "Calcium, Ca2+."],
                   ["Dissolves in excess NaOH; dissolves in excess ammonia", "Zinc, Zn2+."],
                   ["Dissolves in excess NaOH; insoluble in excess ammonia", "Lead(II), Pb2+. Confirm: potassium iodide gives a bright yellow precipitate."]]),
        EX("Worked example 1: a blue solution", intro="Solution P is blue. It gives a light blue precipitate with a few drops of sodium hydroxide. The precipitate does not dissolve in excess. With ammonia solution, a light blue precipitate forms, and it dissolves in excess to give a deep blue solution. Identify the cation.",
           steps=[
               S("Colour of the solution", text="Blue points to Cu2+."),
               S("Sodium hydroxide", text="A light blue precipitate, insoluble in excess, matches Cu(OH)2."),
               S("Ammonia", text="A light blue precipitate that dissolves to a deep blue solution is the special result for Cu2+."),
               S("Conclusion", text="The cation in P is copper(II), Cu2+. The precipitate is [[Cu(OH)2]]."),
           ]),
        EX("Worked example 2: a colourless solution", intro="Solution Q is colourless. Sodium hydroxide gives a white precipitate that dissolves in excess. Ammonia gives a white precipitate that does not dissolve in excess. Potassium iodide gives a yellow precipitate. Identify the cation.",
           steps=[
               S("Eliminate coloured ions", text="Colourless, so not Cu2+, Fe2+ or Fe3+."),
               S("White precipitate soluble in excess NaOH", text="The ion is Zn2+ or Pb2+."),
               S("Ammonia insoluble in excess", text="This rules out Zn2+. The ion is Pb2+."),
               S("Confirm", text="Potassium iodide gives yellow lead(II) iodide. The cation is lead(II), Pb2+."),
           ]),
        MISTAKE("Writing the inference instead of the observation", "Write 'a green precipitate formed'. Do not write only 'Fe2+ is present'. Marks are given for the observation and then for the conclusion."),
        MISTAKE("Adding too much too fast", "Add the alkali drop by drop at first. If you pour in excess at once you will not see the precipitate form, and you cannot tell whether it dissolves."),
        MISTAKE("Mixing up 'no reaction' and 'insoluble in excess'", "'Insoluble in excess' means a precipitate formed and then did not dissolve. 'No precipitate' means nothing formed at all."),
        TIP("The Board's report says Section B of Paper 2 (Alternative to Practical) tests analysis of salts with a series of tests, and that learners should be able to describe simple laboratory procedures, observe and interpret results. Cation tests are also asked in Paper 1. Where textbooks give slightly different colours (for example for iron(II) hydroxide), check your textbook.", title="Exam link"),
        QUIZ("A solution gives a red-brown precipitate with sodium hydroxide which is insoluble in excess. Which ion is present?", ["Cu2+", "Fe2+", "Fe3+", "Zn2+"], 2,
             "Red-brown precipitate of iron(III) hydroxide, insoluble in excess: Fe3+.",
             hint="Which iron ion gives a red-brown colour?",
             feedback=["Copper(II) gives a light blue precipitate.", "Iron(II) gives a green precipitate.", "", "Zinc gives a white precipitate."]),
        QUIZ("A white precipitate formed with sodium hydroxide dissolves in excess. With ammonia a white precipitate forms and it dissolves in excess. The ion is:", ["Pb2+", "Ca2+", "Zn2+", "NH4+"], 2,
             "Zinc hydroxide dissolves in both excess sodium hydroxide and excess ammonia.",
             hint="Lead dissolves only in one of the two reagents in excess.",
             feedback=["Lead(II) hydroxide does not dissolve in excess ammonia.", "Calcium hydroxide does not dissolve in excess sodium hydroxide.", "", "Ammonium ions give no precipitate."]),
        PQ("Describe a test to show that a solution contains ammonium ions.",
           "Add sodium hydroxide solution and warm gently. Ammonia gas is given off. It has a sharp smell and turns damp red litmus paper blue."),
        PQ("Describe what you would see when sodium hydroxide is added slowly, and then in excess, to a solution containing Fe2+ ions.",
           "A green precipitate forms. It does not dissolve in excess. On standing it turns brown (it is oxidised by air)."),
        PQ("Write the ionic equation for the formation of the precipitate when sodium hydroxide is added to copper(II) sulfate solution.",
           "Cu2+ + 2OH- -> Cu(OH)2."),
        PQ("Two colourless solutions both give a white precipitate with sodium hydroxide that dissolves in excess. Explain how ammonia solution distinguishes between zinc and lead(II) ions.",
           "Add ammonia solution dropwise, then in excess. Zinc: a white precipitate that dissolves in excess. Lead(II): a white precipitate that does not dissolve in excess."),
        SUM("Qualitative analysis finds out what is present. Record observations first, then inferences.",
            "Add NaOH and ammonia solution dropwise, then in excess, to a fresh sample each time.",
            "Colours of hydroxides: Cu(OH)2 light blue, Fe(OH)2 green, Fe(OH)3 red-brown, others white.",
            "Excess NaOH dissolves Zn and Pb hydroxides; excess ammonia dissolves Zn and Cu hydroxides (deep blue for Cu).",
            "Ammonium ions: warm with NaOH to give ammonia gas, which turns damp red litmus paper blue."),
    ])]

# ============================================================================================
# 13. Qualitative analysis (lesson 2 of 2): anions and gases
# ============================================================================================
LESSONS += [lesson(
    module=M_ORG, topic="Qualitative analysis",
    title="Identifying anions and gases",
    slug="che-qualitative-analysis-anions-gases", minutes=26,
    summary="Anions are identified by tests with acid, barium chloride, silver nitrate or aluminium with alkali, and gases by simple tests such as limewater, litmus and a lighted splint.",
    objectives=[
        "Carry out and describe the tests for CO3 2-, SO4 2-, SO3 2-, NO3-, Cl-, Br- and I-",
        "Explain why some tests need the solution to be acidified first",
        "State the tests for hydrogen, oxygen, carbon dioxide, ammonia, chlorine, sulfur dioxide, hydrogen chloride and water",
        "Combine anion and cation tests to identify an unknown salt",
    ],
    key_concepts=["Anion tests", "Acidifying first", "Halide ions", "Gas tests", "Limewater", "Salt analysis"],
    blocks=[
        H("Introduction"),
        T("A cook in Maroua wonders why a white powder fizzes when vinegar is added. The fizzing is carbon dioxide, and it is the first clue that the powder is a carbonate. "
          "Anion tests work the same way. You add a reagent and watch for a gas or a precipitate. You also need quick tests for the gases themselves."),
        H("Tests for anions"),
        CODE("Anion            Test                                         Positive result\n"
             "carbonate CO3 2-  add dilute acid                              fizzing; gas turns limewater milky\n"
             "sulfate SO4 2-    add dilute HCl (or HNO3), then BaCl2(aq)      white precipitate (BaSO4)\n"
             "sulfite SO3 2-    add dilute acid, warm                        SO2 gas: sharp smell; turns acidified\n"
             "                                                               dichromate orange to green\n"
             "nitrate NO3-      add NaOH(aq) and aluminium foil, warm        ammonia gas; turns damp red litmus blue\n"
             "chloride Cl-      add dilute HNO3, then AgNO3(aq)              white ppt, dissolves in dilute NH3(aq)\n"
             "bromide Br-       add dilute HNO3, then AgNO3(aq)              cream ppt, dissolves in concentrated NH3(aq)\n"
             "iodide I-         add dilute HNO3, then AgNO3(aq)              yellow ppt, insoluble in NH3(aq)", "text",
             title="Tests for anions (check your textbook for ammonia concentrations)"),
        T("Why acidify first? Carbonates and sulfites also give a white precipitate with barium chloride, and carbonates, sulfites and hydroxides can give a precipitate with silver nitrate. "
          "Adding acid first removes them (carbonate gives off carbon dioxide). Then only the ion you are testing for gives the precipitate."),
        T("Ionic equations for the precipitates:"),
        T("[[Ba^2+ + SO4^2- -> BaSO4]]   (white)"),
        T("[[Ag^+ + Cl^- -> AgCl]]   (white)"),
        T("[[Ag^+ + Br^- -> AgBr]]   (cream)"),
        T("[[Ag^+ + I^- -> AgI]]   (yellow)"),
        T("For nitrate, the aluminium reduces the nitrate in alkali and gives ammonia gas. The test is also given by nitrite ions, which your syllabus may or may not require; check your textbook."),
        H("Tests for gases"),
        CODE("Gas                Test                                    Result\n"
             "hydrogen H2        lighted splint                          squeaky pop\n"
             "oxygen O2          glowing splint                          relights\n"
             "carbon dioxide CO2 bubble through limewater                turns milky (cloudy)\n"
             "ammonia NH3        damp red litmus paper                   turns blue; sharp smell\n"
             "chlorine Cl2       damp blue litmus paper                  turns red, then bleached white;\n"
             "                                                           yellow-green gas\n"
             "sulfur dioxide SO2 acidified potassium dichromate paper    orange to green; sharp smell\n"
             "hydrogen chloride  rod dipped in ammonia solution          dense white fumes (NH4Cl)\n"
             "water vapour       anhydrous copper(II) sulfate            white to blue", "text", title="Tests for gases"),
        T("The equations for the limewater test and the ammonia/hydrogen chloride test:"),
        T("[[CO2 + Ca(OH)2 -> CaCO3 + H2O]]   (milky, because calcium carbonate is insoluble)"),
        T("[[NH3 + HCl -> NH4Cl]]   (white fumes of ammonium chloride)"),
        KEY("Two gases that look alike", "Carbon dioxide and sulfur dioxide both turn limewater milky. Use the second test:",
            cards=[["Carbon dioxide", "No smell. Does not change acidified dichromate."],
                   ["Sulfur dioxide", "Sharp, choking smell. Turns acidified potassium dichromate from orange to green."]]),
        EX("Worked example 1: identify a salt", intro="Salt R is a blue crystalline solid. It dissolves in water to give a blue solution. A light blue precipitate forms with sodium hydroxide, and it does not dissolve in excess. When dilute hydrochloric acid and then barium chloride solution are added to the solution, a white precipitate forms. Name the salt.",
           steps=[
               S("Cation", text="Blue solution and a light blue precipitate, insoluble in excess: Cu2+."),
               S("Anion", text="Acid then barium chloride gives a white precipitate: SO4 2-."),
               S("Conclusion", text="Salt R is copper(II) sulfate, [[CuSO4]]."),
           ]),
        EX("Worked example 2: a colourless salt", intro="Salt S is white and dissolves in water to give a colourless solution. Sodium hydroxide gives a white precipitate that dissolves in excess. Ammonia gives a white precipitate that dissolves in excess. With dilute nitric acid then silver nitrate, a white precipitate forms that dissolves in dilute ammonia. Name the salt.",
           steps=[
               S("Cation", text="White precipitate soluble in excess of both reagents: Zn2+."),
               S("Anion", text="White precipitate with silver nitrate, soluble in dilute ammonia: Cl-."),
               S("Conclusion", text="Salt S is zinc chloride, [[ZnCl2]]."),
           ]),
        MISTAKE("Forgetting to acidify", "To test for sulfate or a halide, add dilute acid **first**. Without it, carbonate or sulfite ions can give a precipitate and give a false positive."),
        MISTAKE("Using the wrong acid", "For the sulfate test do not use sulfuric acid to acidify (it contains sulfate). For the halide tests do not use hydrochloric acid (it contains chloride). Use dilute nitric acid for the silver nitrate tests."),
        MISTAKE("Saying limewater 'turns white'", "Write that limewater turns **milky** or cloudy. With a lot of carbon dioxide the milkiness goes away, because soluble calcium hydrogencarbonate forms."),
        TIP("The Board's report says Section B of Paper 2 (Alternative to Practical) includes salt analysis: candidates must find the anion and the cation with a series of tests, and describe, observe and interpret. These tests are also tested in Paper 1. Learn each test as a trio: reagent, observation, ion.", title="Exam link"),
        QUIZ("A white solid fizzes when dilute hydrochloric acid is added and the gas turns limewater milky. The solid contains which anion?", ["Sulfate", "Chloride", "Carbonate", "Nitrate"], 2,
             "Carbonates and acids give off carbon dioxide, which turns limewater milky.",
             hint="Which anion releases carbon dioxide with acid?",
             feedback=["Sulfates do not fizz with acid.", "Chlorides do not fizz with acid.", "", "Nitrates do not fizz with dilute acid."]),
        QUIZ("A solution gives a yellow precipitate with dilute nitric acid followed by silver nitrate. The precipitate is insoluble in ammonia. Which anion is present?", ["Chloride", "Bromide", "Iodide", "Sulfate"], 2,
             "AgI is yellow and does not dissolve in ammonia.",
             hint="White, cream, yellow: chloride, bromide, ...",
             feedback=["Silver chloride is white and dissolves in dilute ammonia.", "Silver bromide is cream.", "", "Sulfate is tested with barium chloride."]),
        PQ("Describe the test for a sulfate and give the ionic equation.",
           "Add dilute hydrochloric acid (or nitric acid), then barium chloride solution. A white precipitate shows sulfate. Ba2+ + SO4 2- -> BaSO4."),
        PQ("A gas turns damp red litmus paper blue and forms white fumes with hydrogen chloride. Name the gas and write the equation for the reaction with hydrogen chloride.",
           "The gas is ammonia. NH3 + HCl -> NH4Cl."),
        PQ("Describe how you could distinguish carbon dioxide from sulfur dioxide.",
           "Both turn limewater milky. Sulfur dioxide has a sharp smell and turns acidified potassium dichromate paper from orange to green. Carbon dioxide has no smell and does not change it."),
        PQ("A salt dissolves to give a pale green solution. Sodium hydroxide gives a green precipitate that turns brown. Barium chloride in acid gives a white precipitate. Name the salt.",
           "The green precipitate that turns brown shows Fe2+. The white precipitate with acid and barium chloride shows sulfate. The salt is iron(II) sulfate."),
        SUM("Anions: carbonate (acid gives CO2), sulfate (acid then BaCl2), halides (nitric acid then AgNO3: white, cream, yellow), nitrate (NaOH and Al, ammonia).",
            "Acidify first so that carbonate and sulfite do not give a false positive.",
            "Gases: H2 pops, O2 relights, CO2 turns limewater milky, NH3 turns damp red litmus blue, Cl2 bleaches damp litmus, SO2 turns dichromate green.",
            "Combine one cation test and one anion test to name a salt.",
            "Record the observation first, then the inference."),
    ])]

# ============================================================================================
# 14. Examination: Paper 1
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1: multiple-choice strategies for Chemistry",
    slug="chx-paper-1-multiple-choice-strategy", minutes=22,
    summary="Paper 1 has 50 multiple-choice questions in 1 hour 30 minutes drawn from the whole syllabus. Use about 1.8 minutes a question, the two-pass method, elimination and a fixed method for calculations.",
    objectives=[
        "State the official facts about Paper 1: 50 questions, 1 hour 30 minutes, whole syllabus, and the mix of knowledge, comprehension, application and analysis",
        "Plan the time with the two-pass method and calculate the average time per question",
        "Use elimination, and watch for NOT, only and always, in chemistry questions",
        "Use a four-step routine for mole calculations and avoid unit traps",
    ],
    key_concepts=["Paper 1", "Two-pass method", "Elimination", "Distractor", "Mole routine", "Unit traps"],
    blocks=[
        H("Introduction"),
        T("It is 8 a.m. in an exam hall in Buea. The paper has 50 multiple-choice questions on chemistry, and you have 90 minutes. Some questions ask for a fact. Some ask you to read a table. "
          "Some ask for a calculation. Knowing chemistry is the first half of success. Knowing how the paper works is the second half, and this lesson covers it."),
        D("According to the Board's 2023 report, Paper 1 has **50 multiple-choice questions** drawn from the **whole syllabus**, and the time is **1 hour 30 minutes**. It is marked electronically. "
          "The questions test knowledge (30%), comprehension (40%), application (19%) and analysis (11%).", title="Paper 1: the official facts"),
        T("Because only 30% of the questions are pure recall, learning definitions is not enough. Most questions ask you to **understand** an idea, to **use** it in a new situation, or to **analyse** data. "
          "Practise with new examples, not only the ones in your notes."),
        T("Since the questions come from the whole syllabus, all seven modules matter: matter and bonding, formulae and moles, acids, bases and redox, energetics and rates, electrochemistry, inorganic chemistry, and organic chemistry with qualitative analysis."),
        H("Time: about 1.8 minutes a question"),
        T("90 minutes divided by 50 questions is **1.8 minutes** each. A fact question can take 20 seconds. A mole calculation can take three minutes. The aim is to keep to the average."),
        KEY("The two-pass method (KKEVO study advice)", "Go through the paper twice.",
            cards=[["Pass 1 (about 55 minutes)", "Answer everything you can do at once. If you are stuck after about a minute, tick the question and move on."],
                   ["Pass 2 (about 25 minutes)", "Go back to the ticked questions. Use elimination and calculation."],
                   ["Final check (about 10 minutes)", "Make sure every question has an answer. Re-read questions with NOT, only or always."]]),
        H("Reading questions and eliminating options"),
        D("The **stem** is the question. The **key** is the correct option. The **distractors** are the wrong options. A good distractor is a true statement about something else, or the result of a common mistake.", title="Stem, key, distractors"),
        T("First read the stem and cover the options. Decide what the answer should be. Then find the matching option. If you cannot, **eliminate** options you can prove wrong, then choose between those left."),
        EX("Worked example 1: elimination", intro="Which statement about alkenes is correct?  A. They are saturated hydrocarbons.  B. They decolourise bromine water.  C. Their general formula is CnH2n+2.  D. They react with chlorine only by substitution.",
           steps=[
               S("Say the answer first", text="Alkenes have a C=C double bond. They are unsaturated and undergo addition. Their test is bromine water."),
               S("Cross out", text="A is wrong: alkenes are unsaturated. C is wrong: CnH2n+2 is the alkane formula; alkenes are CnH2n. D is wrong: alkenes undergo addition."),
               S("Choose", text="B is the only correct statement."),
           ]),
        H("Words that change the meaning"),
        KEY("Watch for these", "A small word can change the whole question.",
            cards=[["NOT, EXCEPT", "Underline them. You are looking for the one false statement."],
                   ["Only, always, never, all", "Options with these words are often too strong. Ask: can I think of an exception?"],
                   ["Most, best, largest", "Check that your answer is truly the most or best, not just a good one."],
                   ["Tables, graphs, diagrams", "Read the title, units and labels before the options. Use the data in the question, not memory."]]),
        H("Chemistry traps"),
        CODE("Pair of terms                        The difference\n"
             "strong / concentrated acid           strong = ionizes completely; concentrated = a lot of acid dissolved\n"
             "oxidation / reduction                OIL RIG: Oxidation Is Loss of electrons; Reduction Is Gain\n"
             "atom / ion / molecule                ion has a charge; molecule is atoms joined by covalent bonds\n"
             "exothermic / endothermic             exothermic: heat given out, temperature rises\n"
             "element / compound / mixture         element: one kind of atom; compound: bonded; mixture: not bonded\n"
             "yield / rate                         yield is how much; rate is how fast\n"
             "saturated / unsaturated              saturated: only single bonds between carbon atoms", "text", title="Pairs that cause mistakes"),
        H("A routine for calculations"),
        KEY("Four steps for any mole calculation", "Do the steps in order and the numbers rarely go wrong.",
            cards=[["1. Equation", "Write the balanced equation."],
                   ["2. Moles of the known substance", "Moles = mass / molar mass, or concentration x volume in dm³."],
                   ["3. Mole ratio", "Use the numbers in front of the formulae to find the moles of the wanted substance."],
                   ["4. Convert", "Change moles into mass, volume or concentration. Check the unit."]]),
        EX("Worked example 2: a mole question", intro="How many moles are there in 5.3 g of sodium carbonate, [[Na2CO3]]? (Na = 23, C = 12, O = 16)  A. 20  B. 0.5  C. 0.05  D. 5.0",
           steps=[
               S("Molar mass", math=r"2(23) + 12 + 3(16) = 106\ \text{g/mol}"),
               S("Moles", math=r"n = \frac{5.3}{106} = 0.050\ \text{mol}"),
               S("Check the distractors", text="A (20) comes from dividing the wrong way round: 106 / 5.3. B (0.5) and D (5.0) are decimal slips. The answer is C."),
           ]),
        MISTAKE("Spending five minutes on one question", "At 1.8 minutes a question, one hard question can cost the time of three easy ones. Tick it and come back."),
        MISTAKE("Forgetting to change cm³ into dm³", "Concentration in mol/dm³ needs the volume in dm³. Divide cm³ by 1000. The options often include the answer you get if you forget."),
        TIP("This lesson is about Paper 1. The Board's own description says the 50 items come from the whole syllabus, so use the mock paper in this module and revise by topic from the results page. Whether a wrong answer loses marks is something to confirm with your teacher; the safest habit is to answer every question.", title="Exam link"),
        QUIZ("The Paper 1 time is 90 minutes for 50 questions. What is the average time for each question?", ["0.9 minutes", "1.8 minutes", "2.5 minutes", "5 minutes"], 1,
             "90 divided by 50 = 1.8 minutes.",
             hint="Divide the time by the number of questions.",
             feedback=["That is 45 divided by 50.", "", "That would take 125 minutes in all.", "That would take 250 minutes in all."]),
        QUIZ("A question asks: 'Which of these is NOT an alkane?' What should you look for?", ["The only unsaturated hydrocarbon among the options", "The first option that is an alkane", "The longest formula", "The formula that ends in -OH"], 0,
             "NOT reverses the question: you need the one option that is not an alkane, for example an alkene with a double bond.",
             hint="Underline NOT and say the question again in your own words.",
             feedback=["", "That is an alkane, so it is wrong.", "Length has nothing to do with the type of compound.", "That is an alcohol, but it may not be the option asked about."]),
        PQ("List the three passes of the two-pass method and say what you do in each.",
           "Pass 1: answer all the questions you can do quickly and tick the others. Pass 2: return to the ticked questions and use elimination or calculation. Final check: make sure every question is answered and re-read questions with NOT, only or always."),
        PQ("Explain what a distractor is and how elimination helps.",
           "A distractor is a wrong option that looks attractive. Elimination removes the options that you can show are wrong, leaving fewer choices, so a correct answer is more likely."),
        PQ("Calculate the number of moles in 11 g of carbon dioxide, [[CO2]]. (C = 12, O = 16)",
           "Molar mass = 12 + 2 x 16 = 44 g/mol. Moles = 11 / 44 = 0.25 mol."),
        PQ("A student reads a 25 cm³ volume as 25 dm³ in a concentration calculation. What is the effect on the answer?",
           "The volume is 1000 times too big, so the concentration calculated will be 1000 times too small. Always convert cm³ into dm³ by dividing by 1000."),
        SUM("Paper 1 has 50 multiple-choice questions from the whole syllabus in 1 hour 30 minutes: knowledge 30%, comprehension 40%, application 19%, analysis 11%.",
            "Use about 1.8 minutes a question; use the two-pass method.",
            "Say the answer first, then eliminate wrong options; watch NOT, only and always.",
            "Learn the pairs of terms that cause errors (strong and concentrated, oxidation and reduction).",
            "For calculations: equation, moles, ratio, convert; check units."),
    ])]

# ============================================================================================
# 15. Examination: Paper 2 (structured questions and essays)
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2: answering structured and essay questions",
    slug="chx-paper-2-structured-questions", minutes=26,
    summary="Paper 2 has ten questions in three sections: structured questions, Alternative to Practical, and essays. Learn the command words, what the examiners say candidates get wrong, and model answers.",
    objectives=[
        "Describe the structure of Paper 2 (Sections A, B and C) as given in the Board's 2023 report",
        "Respond correctly to command words such as state, describe, explain and calculate",
        "Avoid the common errors named in the Board's report: yield and equilibrium position, the role of a catalyst, ionic equations at electrodes",
        "Plan a short-note essay with a definition, an example and an equation",
    ],
    key_concepts=["Paper 2", "Command words", "Yield and position of equilibrium", "Catalyst", "Ionic equation", "Short notes"],
    blocks=[
        H("Introduction"),
        T("In Paper 2 you write your own answers. The Board's 2023 report says that Paper 2 has **ten questions in three sections**. **Section A** and **Section C** mainly test knowledge, understanding, application and analysis. "
          "**Section B** is **Alternative to Practical**: two compulsory questions on experimental skills (the next lesson). KKEVO's blueprint gives the time as 2 hours 30 minutes. Check the exact format with your teacher."),
        D("The report says Paper 2 was a little harder than the year before, and that a candidate needs **more than knowledge**: most questions ask you to understand, apply and analyse. Section A was where candidates did best, and Section B contributed most to poor performance.", title="What the Board says"),
        H("Command words"),
        CODE("Command word   What the examiner wants\n"
             "State / name   a short answer, no explanation\n"
             "Define         the exact meaning, in one precise sentence\n"
             "Describe       what happens or what you see, in order\n"
             "Explain        the reason: use 'because' and the chemistry\n"
             "Calculate      working, answer, and the unit\n"
             "Deduce         work out an answer from the information given\n"
             "Suggest        apply your knowledge to a situation you have not seen\n"
             "Compare        similarities and differences, both sides", "text", title="Command words"),
        KEY("Habits that protect your marks", "These habits cost nothing.",
            cards=[["Equations", "Write correct formulae first, then balance. Add state symbols if asked."],
                   ["Units", "Write the unit with every numerical answer. Convert cm³ into dm³ first."],
                   ["Working", "Show every step of a calculation."],
                   ["Reagent, condition, product", "For any reaction, give all three."]]),
        H("Mistakes the Board's report names"),
        T("The report lists areas in which candidates lost marks. Learn the correct ideas."),
        KEY("Yield and position of equilibrium", "Candidates mixed up *yield* and *equilibrium position*, and did not know what a catalyst does in a reversible reaction.",
            cards=[["A catalyst", "Speeds up the forward and the backward reaction **equally**. Equilibrium is reached faster, but the yield and the equilibrium position do **not** change."],
                   ["Yield and position", "Changing temperature or pressure can move the position of equilibrium and so change the yield of product."],
                   ["Rate", "The factors that change the position also change the rate, but they are explained differently: rate uses collision theory; position uses Le Chatelier's principle."]]),
        EX("Worked example 1: the Haber process", intro="The Haber process is [[N2 + 3H2 <=> 2NH3]], exothermic. (a) Explain why high pressure increases the yield of ammonia. (b) State and explain the effect of the iron catalyst on the yield.",
           steps=[
               S("(a) Count molecules of gas", text="There are 4 moles of gas on the left (1 + 3) and 2 on the right."),
               S("(a) Apply Le Chatelier", text="High pressure moves the equilibrium to the side with fewer moles of gas, the right. So the yield of ammonia increases."),
               S("(b) Catalyst", text="The iron catalyst speeds up the forward and the backward reactions equally. Equilibrium is reached faster, but the yield is **unchanged**."),
           ]),
        KEY("Electrolysis answers", "The report says electrolysis of an aqueous salt solution gave the poorest results in Section A. Know the ions, the electrode equations and the observations.",
            cards=[["Ionize first", "The electrolyte and water ionize, so more than one ion goes to each electrode."],
                   ["Write half-equations", "Cathode: gain of electrons (reduction). Anode: loss of electrons (oxidation)."],
                   ["Observation", "Say what you see at each electrode and in the solution."]]),
        EX("Worked example 2: electrolysis of copper(II) sulfate with inert electrodes", intro="Write the electrode reactions and state what is seen. Then calculate the mass of copper deposited by a current of 2.0 A for 965 s. (Cu = 63.5; F = 96 500 C/mol)",
           steps=[
               S("Cathode", math=r"<<Cu^2+ + 2e^- -> Cu>>", text="A pink-brown solid (copper) is deposited."),
               S("Anode", math=r"<<4OH^- -> 2H2O + O2 + 4e^->>", text="Bubbles of colourless gas (oxygen). The blue colour of the solution fades as copper ions are used up."),
               S("Charge", math=r"Q = It = 2.0 \times 965 = 1930\ \text{C}"),
               S("Moles of electrons", math=r"n(e^-) = \frac{1930}{96\,500} = 0.0200\ \text{mol}"),
               S("Copper (2 electrons per Cu)", math=r"n(\text{Cu}) = 0.0100\ \text{mol};\quad m = 0.0100 \times 63.5 = 0.635\ \text{g}"),
           ]),
        KEY("Carbon and its forms", "The report says candidates could not tell crystalline from non-crystalline forms of carbon.",
            cards=[["Crystalline (allotropes)", "Diamond and graphite have regular structures."],
                   ["Non-crystalline", "Charcoal, coke and soot have no regular crystal structure."]]),
        H("Section C: short notes and essays"),
        T("Section C tests the ability to organise your material logically, and to use diagrams. For **short notes on types of reactions** the report says to give a **definition** and to use **examples or equations**. For an experiment, report it in the standard order: materials, procedure, results, analysis of results."),
        EX("Worked example 3: a short note on addition reactions", intro="Write short notes on addition reactions.",
           steps=[
               S("Definition", text="An addition reaction is one in which two or more molecules join to form one product, and the double bond of an unsaturated molecule opens."),
               S("Example and equation", text="Ethene with bromine: [[C2H4 + Br2 -> C2H4Br2]]. The orange-brown colour of bromine water disappears."),
               S("Second example", text="Ethene with hydrogen (nickel catalyst, about 150 °C): [[C2H4 + H2 -> C2H6]]."),
               S("Use or link", text="Addition polymerization of ethene makes poly(ethene)."),
           ]),
        MISTAKE("Saying a catalyst increases the yield", "A catalyst changes the rate only. In a reversible reaction it does not change the position of equilibrium or the yield."),
        MISTAKE("Writing the answer to 'explain' as a statement", "'Explain' needs a reason. Do not only say what happens. Add 'because' and the chemistry."),
        TIP("This lesson is about Paper 2. The marks per question are not stated here because the Board's report does not give them. Write complete answers, with units and equations.", title="Exam link"),
        QUIZ("What effect does a catalyst have on the equilibrium position of a reversible reaction?", ["It moves it to the right", "It moves it to the left", "It has no effect on the position", "It doubles the yield"], 2,
             "A catalyst speeds up both directions equally, so it does not change the position or the yield.",
             hint="Think about what happens to the forward and the backward rates.",
             feedback=["It speeds up both directions equally.", "It speeds up both directions equally.", "", "The yield stays the same."]),
        QUIZ("In an answer to 'Explain why', what must you include?", ["Only the name of the reaction", "A reason, introduced by 'because'", "A drawing", "A long list of facts"], 1,
             "'Explain' requires the reason, using the chemistry.",
             hint="What does 'explain' ask for that 'state' does not?",
             feedback=["That is not an explanation.", "", "A drawing may help but it is not required.", "More facts do not give a reason."]),
        PQ("State the difference between *yield* and *rate* of reaction.",
           "Yield is the amount of product obtained. Rate is how fast the product forms."),
        PQ("Write the half-equation at the cathode when copper(II) sulfate solution is electrolysed with inert electrodes, and say what is seen.",
           "Cu2+ + 2e- -> Cu. A pink-brown solid (copper) forms on the cathode."),
        PQ("Calculate the mass of copper deposited when a current of 0.50 A flows for 1930 s through copper(II) sulfate solution. (Cu = 63.5; F = 96 500 C/mol)",
           "Q = 0.50 x 1930 = 965 C. n(e-) = 965 / 96 500 = 0.0100 mol. Two electrons deposit one copper atom, so n(Cu) = 0.0050 mol. m = 0.0050 x 63.5 = 0.3175 g, about 0.32 g."),
        PQ("Write a short note on esterification: definition, equation and one use.",
           "Esterification is the reaction of an alcohol with a carboxylic acid to give an ester and water, catalysed by concentrated sulfuric acid; it is reversible. C2H5OH + CH3COOH <=> CH3COOC2H5 + H2O. Esters are used as flavours and perfumes."),
        SUM("Paper 2 has ten questions in Sections A, B (Alternative to Practical) and C, testing more than recall.",
            "Answer the command word: state, describe, explain, calculate.",
            "A catalyst changes the rate, not the yield or position of equilibrium; yield and position change with temperature and pressure.",
            "For electrolysis write the half-equations and the observations.",
            "For short notes: definition, example and equation; for experiments: materials, procedure, results, analysis."),
    ])]

# ============================================================================================
# 16. Examination: Paper 2 Alternative to Practical
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2 Section B: Alternative to Practical",
    slug="chx-paper-2-alternative-to-practical", minutes=28,
    summary="Section B tests experimental skills on paper: apparatus, gas collection, tests for ions and gases, titration tables, observations and inferences, and safe, fair experiments.",
    objectives=[
        "Name common laboratory apparatus and state what each is used for",
        "Choose a method of collecting a gas and explain the choice",
        "Record titration results in a table, choose concordant titres and calculate a concentration",
        "Write observations and inferences for tests on salts and organic compounds, and plan a fair and safe test",
    ],
    key_concepts=["Alternative to Practical", "Apparatus", "Gas collection", "Titration", "Concordant titres", "Observation and inference", "Fair test"],
    blocks=[
        H("Introduction"),
        T("Not every school has a full laboratory. The Board therefore sets **Alternative to Practical** questions: you answer on paper as if you had done the experiment. "
          "The Board's 2023 report says Section B has **two compulsory questions**, and that it tests reading, recording, manipulating and reporting skills, inference, problem solving and simple calculations from results. "
          "It also tests experimental design and safety. The report says this section gave the weakest results in the paper, so it is worth practising."),
        H("Apparatus"),
        CODE("Apparatus              Use\n"
             "burette                delivers measured, variable volumes of liquid (titrations)\n"
             "pipette (25.0 cm³)     delivers one fixed, accurate volume\n"
             "volumetric flask       makes up an exact volume of solution\n"
             "measuring cylinder     measures volumes less accurately\n"
             "conical flask          holds the solution being titrated; can be swirled\n"
             "filter funnel          holds filter paper to separate a solid from a liquid\n"
             "thermometer            measures temperature\n"
             "balance                measures mass\n"
             "gas syringe            measures the volume of gas given off\n"
             "condenser              cools vapour back to a liquid in distillation\n"
             "separating funnel      separates liquids that do not mix\n"
             "evaporating dish       evaporates a solution\n"
             "stopwatch              measures time", "text", title="Common apparatus"),
        H("Collecting gases"),
        IMG("f5ch-e-gas-collection.svg", alt="Three ways of collecting a gas: over water in an inverted jar, by downward delivery into an upright jar, and by upward delivery into an inverted jar.",
            caption="Figure 1. Three ways to collect a gas."),
        CODE("Method                       Use when the gas is                   Examples\n"
             "over water                   insoluble (or slightly soluble)       hydrogen, oxygen\n"
             "downward delivery            denser than air                       carbon dioxide, chlorine, hydrogen chloride\n"
             "upward delivery              less dense than air and soluble       ammonia", "text", title="Choosing a method (carbon dioxide is also collected over water in some books; check your textbook)"),
        H("Titration"),
        IMG("f5ch-e-titration-setup.svg", alt="A burette held in a stand above a conical flask that stands on a white tile. The flask contains alkali and indicator. Labels show the burette, tap, flask and white tile.",
            caption="Figure 2. Titration apparatus. The white tile helps you see the colour change."),
        KEY("Method", "The report says most candidates did well on titration questions, but a few were weak on the calculations. Follow this method.",
            cards=[["1. Fill", "Rinse the burette with the solution it will hold. Fill it and read the starting volume at the bottom of the meniscus."],
                   ["2. Pipette", "Use the pipette to put 25.0 cm³ of the other solution into the flask. Add 2 or 3 drops of indicator."],
                   ["3. Titrate", "Add from the burette, swirling. Do a rough titration first, then slow down near the end point."],
                   ["4. Repeat", "Repeat until you have two or three results that agree within 0.10 cm³ (concordant results)."]]),
        CODE("Indicator          In acid         In alkali       End point (acid-alkali)\n"
             "methyl orange      red             yellow          orange\n"
             "phenolphthalein    colourless      pink            colour just changes", "text", title="Indicators"),
        CODE("                       Rough    1        2        3\n"
             "Final burette / cm³   25.30    25.85    26.30    25.95\n"
             "Initial burette / cm³  0.00     1.00     1.50     1.10\n"
             "Titre / cm³           25.30    24.85    24.80    24.85", "text", title="Example results"),
        EX("Worked example 1: a titration calculation", intro="25.0 cm³ of 0.100 mol/dm³ sodium hydroxide is neutralised by hydrochloric acid from the burette. Use the table above to find the concentration of the acid. Equation: NaOH + HCl gives NaCl + H2O.",
           steps=[
               S("Titre of each run", text="Titre = final - initial. The values are 25.30 (rough), 24.85, 24.80 and 24.85."),
               S("Choose concordant results", text="Ignore the rough titre. The three accurate titres are within 0.10 cm³ of each other, so use all three."),
               S("Mean titre", math=r"\frac{24.85 + 24.80 + 24.85}{3} = 24.83\ \text{cm}^3"),
               S("Moles of NaOH", math=r"n = 0.100 \times \frac{25.0}{1000} = 0.00250\ \text{mol}"),
               S("Moles of HCl (ratio 1 : 1) and its concentration", math=r"c = \frac{0.00250}{24.83/1000} = 0.101\ \text{mol/dm}^3"),
           ]),
        H("Observation and inference"),
        T("Most Section B questions on salt analysis give you a list of tests and results. Write **observation** and **inference** in separate columns."),
        CODE("Test                                       Observation                    Inference\n"
             "add sodium hydroxide, then excess          light blue ppt, not soluble    Cu2+ present\n"
             "add dilute acid                            fizzing, gas turns limewater   a carbonate\n"
             "                                           milky\n"
             "add bromine water to a liquid              orange-brown to colourless     unsaturated compound\n"
             "                                                                          (C=C bond)\n"
             "add acidified K2Cr2O7 and warm             orange to green                an alcohol (oxidised)\n"
             "add sodium carbonate solution              fizzing                        carboxylic acid (-COOH)", "text", title="Observation and inference"),
        EX("Worked example 2: planning a fair test", intro="Plan an experiment to show how the concentration of hydrochloric acid affects the rate of reaction with marble chips.",
           steps=[
               S("Variable you change", text="The concentration of the acid, for example 0.5, 1.0 and 2.0 mol/dm³."),
               S("Variable you measure", text="The volume of carbon dioxide collected in a gas syringe every 30 seconds, using a stopwatch."),
               S("Keep constant", text="The mass and size of the marble chips, the volume of acid and the temperature."),
               S("Result", text="Plot volume of gas against time. The steepest curve belongs to the fastest reaction. Safety: wear eye protection."),
           ]),
        H("Safety"),
        T("Wear eye protection. Do not taste or smell chemicals directly (waft the gas gently towards your nose if told to). Add acid to water, not water to acid. Heat test tubes pointing away from people. Keep flames away from flammable liquids such as ethanol."),
        MISTAKE("Recording only the inference", "Write 'a blue solution' or 'a green precipitate', not just 'copper' or 'iron'. The observation earns marks of its own."),
        MISTAKE("Averaging a rough titre", "The rough titre is only a guide. Average only the concordant, accurate readings."),
        MISTAKE("Wrong number of decimal places", "A burette is read to 0.05 cm³, so titres are written to two decimal places, for example 24.85 cm³. Do not write 24.8 for one reading and 24.85 for another."),
        TIP("Section B (Alternative to Practical) has two compulsory questions. Practise with real apparatus if you can, and with a drawing if you cannot. Where textbooks differ on details such as ammonia strength or end-point colours, check your textbook.", title="Exam link"),
        QUIZ("Which method is used to collect ammonia gas?", ["Over water", "Downward delivery", "Upward delivery", "Gas syringe only"], 2,
             "Ammonia is very soluble in water and less dense than air, so it is collected by upward delivery.",
             hint="Is the gas soluble? Is it lighter or heavier than air?",
             feedback=["Ammonia dissolves in water.", "Ammonia is lighter than air, so it would escape.", "", "A gas syringe measures volume; it does not collect a dry sample of the gas in a jar."]),
        QUIZ("In a titration the results (in cm³) are 25.20 (rough), 24.60, 24.65 and 24.60. Which are used to calculate the mean titre?", ["All four", "Only the first", "The last three", "Only 24.60 and 24.65"], 2,
             "The rough titre is not used. The three accurate readings are within 0.10 cm³ of each other.",
             hint="Which result is only a guide?",
             feedback=["The rough reading is not accurate enough.", "The rough reading is excluded.", "", "The second 24.60 is also concordant and should be used."]),
        PQ("Name the apparatus used to measure exactly 25.0 cm³ of a solution, and the apparatus used to add acid slowly to it.",
           "A pipette (with a pipette filler) measures 25.0 cm³. A burette adds the acid slowly."),
        PQ("A student adds bromine water to an organic liquid. The orange-brown colour disappears. State the observation, the inference, and one more test that gives the same kind of result.",
           "Observation: the bromine water changes from orange-brown to colourless. Inference: the liquid is unsaturated (it has a C=C bond). Acidified potassium manganate(VII) also changes from purple to colourless."),
        PQ("In a titration, 25.0 cm³ of sodium hydroxide of concentration 0.200 mol/dm³ needs 20.00 cm³ of sulfuric acid, H2SO4, for neutralisation. Find the concentration of the acid. (2NaOH + H2SO4 gives Na2SO4 + 2H2O)",
           "n(NaOH) = 0.200 x 0.0250 = 0.00500 mol. The ratio NaOH : H2SO4 is 2 : 1, so n(H2SO4) = 0.00250 mol. c = 0.00250 / 0.02000 = 0.125 mol/dm³."),
        PQ("Give two safety precautions for heating a test tube of liquid.",
           "Wear eye protection; point the mouth of the tube away from yourself and others; heat gently and shake; use a holder."),
        SUM("Section B is Alternative to Practical: two compulsory questions on experimental skills.",
            "Know the apparatus and what each is used for.",
            "Collect gases over water (insoluble), by downward delivery (denser than air) or upward delivery (less dense).",
            "In titration, use concordant results (within 0.10 cm³), write titres to two decimal places and show the mole calculation.",
            "Write observations first and inferences second; plan fair tests and state safety rules."),
    ])]

# @@END@@
LESSONS = _walk(LESSONS)
