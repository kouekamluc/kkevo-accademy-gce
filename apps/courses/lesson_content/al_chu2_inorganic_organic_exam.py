"""Upper Sixth Chemistry (A Level 0715): Inorganic Periodic Chemistry (s & p blocks), Transition Metal & Coordination
Chemistry, Advanced Organic Synthesis & Spectroscopy, and the Examination module (15 topic lessons + 3 exam lessons).

Draft content built from KKEVO's master curriculum blueprint, not from a Board syllabus booklet; a reviewer must check
it against the Board's syllabus and textbooks. Exam facts are only those of the Board's 2023 report: Paper 1 = 50
multiple-choice questions, Paper 2 = six compulsory questions (Section A physical and general, B inorganic, C organic),
Paper 3 = practical (Question 1 quantitative analysis, Question 2 qualitative analysis, plus a school-based assessment).
Study plans and checklists are KKEVO advice, not mark schemes.

Notation (converted by fx() at the bottom): [[CH4]] is a formula in running text, <<2H2 + O2 -> 2H2O>> is bare LaTeX for
math= fields; ^ gives a charge (Cu^2+). Relative atomic masses: H 1, C 12, N 14, O 16, Na 23, Mg 24, Al 27, Si 28,
P 31, S 32, Cl 35.5, K 39, Ca 40, Cr 52, Mn 55, Fe 56, Cu 63.5, Zn 65, Br 80, Ag 108, I 127.
"""

import re

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "upper-sixth")

M_P = "Inorganic Periodic Chemistry: s & p Blocks"
M_T = "Transition Metal & Coordination Chemistry"
M_O = "Advanced Organic Synthesis & Spectroscopy"
M_EXAM = "Examination"

_ARROWS = {"->": r"\rightarrow ", "<=>": r"\rightleftharpoons ", "+": "+", "=": "="}


def _tok(t):
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


_ION = re.compile(r"(?<![A-Za-z$\{^])((?:\[[^\]\s$]+\]|(?:[A-Z][a-z]?\d*|\((?:[A-Z][a-z]?\d*)+\)\d*)+))\^(\d*[+-])(?![\w{])")


def fx(s):
    s = re.sub(r"\[\[(.+?)\]\]", lambda m: "$" + _eq(m.group(1)) + "$", s)
    s = re.sub(r"<<(.+?)>>", lambda m: _eq(m.group(1)), s)
    parts = s.split("$")
    for i in range(0, len(parts), 2):
        parts[i] = _ION.sub(lambda m: "$" + _tok(m.group(1) + "^" + m.group(2)) + "$", parts[i])
        parts[i] = re.sub(r"(\d(?:\.\d+)?) x 10\^(-?\d+)", lambda m: "$" + m.group(1) + r" \times 10^{" + m.group(2) + "}$", parts[i])
        parts[i] = re.sub(r"(?<![\w$])10\^(-?\d+)", lambda m: "$10^{" + m.group(1) + "}$", parts[i])
        parts[i] = re.sub(r"\^(-?\d+)", lambda m: "${}^{" + m.group(1) + "}$", parts[i])
        parts[i] = re.sub(r"\bK_(stab|sp|c|p|w|a|b)\b", lambda m: "$K_{" + m.group(1) + "}$", parts[i])
        parts[i] = parts[i].replace("<=>", "⇌").replace("->", "→")
    return "$".join(parts)


def fxm(s):
    """Maths fields (math=, check=, formula bodies): only the <<...>> chemistry shorthand is converted."""
    s = re.sub(r"\[\[(.+?)\]\]", lambda m: "$" + _eq(m.group(1)) + "$", s)
    return re.sub(r"<<(.+?)>>", lambda m: _eq(m.group(1)), s)


_MATH_KEYS = ("math", "check", "formula")


def _walk(x):
    if isinstance(x, dict):
        if x.get("block_type") == "code":
            return x
        out = {}
        for k, v in x.items():
            if isinstance(v, str) and (k in _MATH_KEYS or (k == "body" and x.get("block_type") == "formula")):
                out[k] = fxm(v)
            else:
                out[k] = _walk(v)
        return out
    if isinstance(x, str):
        return fx(x)
    if isinstance(x, list):
        return [_walk(i) for i in x]
    return x


LESSONS = []
# ============================================================================================
# 1. Periodicity across Period 3
# ============================================================================================
LESSONS += [lesson(
    module=M_P, topic="Periodicity across Period 3",
    title="Period 3: trends from sodium to argon",
    slug="chu2-periodicity-period-3", minutes=24,
    summary="Across Period 3 the structure and bonding change from metallic to giant covalent to simple molecular, and the oxides and chlorides change from basic and ionic to acidic and covalent.",
    objectives=[
        "Describe and explain the trends in atomic radius, first ionization energy, melting point and conductivity from Na to Ar",
        "Link the structure and bonding of the elements to their melting points",
        "Describe the reactions of the Period 3 oxides with water, acids and bases, with equations",
        "Describe the structure of the chlorides and their reactions with water",
    ],
    key_concepts=["Periodicity", "Giant metallic, giant covalent and simple molecular", "Amphoteric oxide", "Hydrolysis of chlorides", "Ionization energy dips"],
    blocks=[
        H("Introduction"),
        T("Aluminium cooking pots, sand (silicon dioxide) on a Limbe beach, phosphate fertilizer for a cocoa farm, sulfur from volcanic gases at Mount Cameroon and table salt all come from the same row of the Periodic Table: Period 3. "
          "The eight elements from sodium to argon show **periodicity**, a repeating pattern of properties. In Period 3 you can watch bonding and structure change step by step."),
        D("**Periodicity** is the repeating pattern of physical and chemical properties of the elements when they are arranged by proton number. Across a period, the number of protons rises by one each step while the outer electrons stay in the same shell (n = 3).", title="Periodicity"),
        H("Atomic radius, ionization energy and electronegativity"),
        T("Across Period 3 the nuclear charge rises from +11 to +18, but the new electrons go into the same shell and the shielding by inner shells hardly changes. The outer electrons are pulled in harder. So the **atomic radius decreases**, the **first ionization energy generally increases** and the **electronegativity increases** (argon is not given a value because it forms no bonds)."),
        CODE("Element       Na    Mg    Al    Si    P     S     Cl    Ar\n"
             "1st IE kJ/mol 496   738   578   786   1012  1000  1251  1521\n"
             "Melting pt C  98    650   660   1410  44    115   -101  -189\n"
             "Structure     metal metal metal giant giant simple simple simple\n"
             "                               cov.  --- molecules (P4, S8, Cl2, Ar) ---", "text",
             title="Period 3 data (approximate values)"),
        IMG("al-chu2-period3-melting.svg", alt="Bar chart of the approximate melting points of sodium to argon: low for sodium, rising to magnesium and aluminium, highest for silicon at 1410 degrees C, then low for the molecular elements and below zero for chlorine and argon.",
            caption="Figure 1. Melting points across Period 3 (approximate values)."),
        KEY("Two dips in ionization energy", "The rise is not smooth. Learn both dips and their explanations.",
            cards=[["Mg to Al (dip)", "The outer electron of Al is in a 3p orbital. A 3p electron is higher in energy and is better shielded by the 3s electrons, so it is removed more easily than a 3s electron of Mg."],
                   ["P to S (dip)", "In S the fourth 3p electron must share an orbital with another electron. Electron-electron repulsion in the pair makes it easier to remove than the unpaired 3p electron of P."]]),
        H("Structure, bonding and melting point"),
        T("Melting point depends on the **structure** and on the strength of the forces that must be broken, so it does not rise smoothly."),
        KEY("Three types of structure in Period 3", "",
            cards=[["Na, Mg, Al: giant metallic", "Positive ions in a sea of delocalized electrons. Melting point rises Na < Mg < Al because the ion charge rises (1+, 2+, 3+), more electrons are delocalized and the ions are smaller, so the metallic bond is stronger."],
                   ["Si: giant covalent", "Every Si atom is joined to four others by strong covalent bonds, as in diamond. Many strong bonds must be broken, so the melting point is the highest. Si is a semiconductor."],
                   ["P4, S8, Cl2, Ar: simple molecular", "Only weak London forces act between molecules and covalent bonds do not break on melting. Melting points are low and depend on molecule size: S8 is larger than P4, so S melts higher than P; Cl2 and Ar are small, so they are gases."]]),
        T("Electrical conductivity follows the same pattern: Na, Mg and Al conduct well (delocalized electrons; Al is best because it has three per atom), Si is a semiconductor, and P, S, Cl2 and Ar do not conduct."),
        H("Oxides"),
        T("Burning each element in oxygen gives an oxide. Moving across the period the oxide changes from ionic and basic, through amphoteric, to covalent and acidic. This follows the rise in electronegativity: oxygen is much more electronegative than Na, so Na2O is ionic, but silicon and the non-metals share electrons."),
        CODE("Oxide     Bonding/structure     Reaction with water              pH of solution\n"
             "Na2O      ionic                 forms NaOH                       13-14\n"
             "MgO       ionic                 slightly soluble, Mg(OH)2        about 9-10\n"
             "Al2O3     ionic with covalent   insoluble                        7 (no reaction)\n"
             "SiO2      giant covalent        insoluble                        7 (no reaction)\n"
             "P4O10     simple molecular      forms H3PO4                      about 0-1\n"
             "SO2       simple molecular      forms H2SO3                      about 1-2\n"
             "SO3       simple molecular      forms H2SO4                      about 0-1\n"
             "Cl2O7     simple molecular      forms HClO4                      about 0", "text",
             title="Oxides of Period 3 (pH values approximate; check your textbook)"),
        T("Equations for the water reactions:"),
        F(r"\mathrm{Na_2O + H_2O \rightarrow 2NaOH}"),
        F(r"\mathrm{P_4O_{10} + 6H_2O \rightarrow 4H_3PO_4}"),
        F(r"\mathrm{SO_3 + H_2O \rightarrow H_2SO_4}"),
        D("An **amphoteric** oxide reacts with both acids and bases to form salts. Aluminium oxide is the example for Period 3.", title="Amphoteric oxide"),
        F(r"\mathrm{Al_2O_3 + 6HCl \rightarrow 2AlCl_3 + 3H_2O}"),
        F(r"\mathrm{Al_2O_3 + 2NaOH + 3H_2O \rightarrow 2Na[Al(OH)_4]}"),
        T("Silicon dioxide is acidic but does not dissolve in water. It reacts with hot concentrated alkali: [[SiO2 + 2NaOH -> Na2SiO3 + H2O]] (sodium silicate). Magnesium oxide, being basic, reacts with acids only: [[MgO + 2HCl -> MgCl2 + H2O]]."),
        H("Chlorides"),
        T("The chlorides show the same change from ionic to covalent. NaCl and MgCl2 are ionic solids with high melting points; they conduct when molten and dissolve in water to give neutral or very slightly acidic solutions (MgCl2 about pH 6.5, because Mg^2+ polarizes the water molecules a little). "
          "Anhydrous aluminium chloride is covalent: it exists as dimers, [[Al2Cl6]], which sublime at about 180 °C and conduct poorly when molten. SiCl4 and PCl5 are simple covalent molecules."),
        D("**Hydrolysis** of a covalent chloride is its reaction with water, producing the hydroxide or oxoacid and hydrogen chloride. Ionic chlorides (NaCl, MgCl2) only dissolve; they do not hydrolyse extensively.", title="Hydrolysis"),
        F(r"\mathrm{AlCl_3 + 3H_2O \rightarrow Al(OH)_3 + 3HCl}"),
        F(r"\mathrm{SiCl_4 + 2H_2O \rightarrow SiO_2 + 4HCl}"),
        F(r"\mathrm{PCl_5 + 4H_2O \rightarrow H_3PO_4 + 5HCl}"),
        T("White fumes of hydrogen chloride appear when these chlorides meet moist air, and the resulting solutions are strongly acidic (about pH 1 for SiCl4 and PCl5). Aluminium chloride solution is acidic (about pH 3) because the hydrated ion [[ [Al(H2O)6]^3+ ]] donates protons."),
        EX("Worked example 1: oxides and pH", intro="Oxide X is added to water and gives a solution of pH 14. Oxide Y does not dissolve in water but dissolves in both dilute hydrochloric acid and sodium hydroxide solution. Identify X and Y from Period 3 and write one equation for X.",
           steps=[
               S("Identify X", text="A strongly alkaline solution means a basic ionic oxide that dissolves: Na2O. (MgO is only slightly soluble, about pH 9-10.)"),
               S("Equation for X", math=r"\mathrm{Na_2O + H_2O \rightarrow 2NaOH}"),
               S("Identify Y", text="An insoluble oxide that reacts with both acids and bases is amphoteric: Al2O3."),
               S("State the answer", text="X is sodium oxide and Y is aluminium oxide."),
           ]),
        EX("Worked example 2: explaining a trend", intro="Explain why the first ionization energy of sulfur (1000 kJ/mol) is lower than that of phosphorus (1012 kJ/mol).",
           steps=[
               S("Write the outer configurations", text="P: 3s2 3p3 (three unpaired 3p electrons). S: 3s2 3p4 (one 3p orbital holds a pair)."),
               S("Compare the electron removed", text="In S, the electron removed comes from a doubly occupied 3p orbital."),
               S("Explain", text="Repulsion between the two electrons in the same orbital makes this electron easier to remove than the unpaired electron in P, even though the nuclear charge of S is greater."),
           ]),
        MISTAKE("Saying SiO2 is a simple molecule", "SiO2 is a giant covalent structure like diamond, so it has a very high melting point. CO2 is the simple molecule. Silicon dioxide is insoluble in water; do not give it a pH of 1."),
        MISTAKE("Saying all chlorides dissolve to a neutral solution", "Only the ionic chlorides (NaCl, MgCl2) do. Covalent chlorides such as AlCl3, SiCl4 and PCl5 react with water (hydrolysis) and give acidic solutions with white fumes of HCl."),
        TIP("Period 3 oxides and chlorides, and the melting-point and ionization-energy trends, are tested in Paper 1 and in the inorganic questions of Paper 2. The Board's 2023 report lists the acid-base character of period 2 and 3 oxides among its multiple-choice concepts. Always link a property to structure and bonding.", title="Exam link"),
        QUIZ("Which Period 3 oxide is amphoteric?", [r"$\mathrm{MgO}$", r"$\mathrm{Al_2O_3}$", r"$\mathrm{SiO_2}$", r"$\mathrm{P_4O_{10}}$"], 1,
             "Al2O3 reacts with acids to form Al^3+ salts and with alkalis to form aluminates.",
             hint="Which oxide dissolves in both HCl and NaOH?",
             feedback=["MgO is basic: it reacts with acids only.", "", "SiO2 is acidic (it needs hot, concentrated alkali).", "P4O10 is acidic and reacts with water to give phosphoric acid."]),
        QUIZ("Why does silicon have a much higher melting point than sulfur?", ["Silicon atoms are heavier", "Silicon has a giant covalent structure but sulfur is made of weakly attracted S8 molecules", "Silicon has delocalized electrons", "Sulfur has weaker covalent bonds"], 1,
             "Melting silicon means breaking strong covalent bonds throughout a giant structure; melting sulfur only overcomes London forces between S8 molecules.",
             hint="What has to be broken when each melts?",
             feedback=["Mass is not the reason; the type of bonding decides.", "", "Silicon is a semiconductor, but its high melting point comes from its covalent network.", "The covalent bonds in S8 are strong; they are not broken on melting."]),
        PQ("(a) State and explain the trend in melting point from sodium to aluminium. (b) Explain why the melting point of silicon is the highest in the period.",
           "(a) It rises: Na < Mg < Al. The metal ions have charges 1+, 2+ and 3+, the number of delocalized electrons per atom rises (1, 2, 3) and the ionic radius falls, so the attraction between the ions and the electron sea becomes stronger and more energy is needed to melt the metal. (b) Silicon has a giant covalent lattice in which each atom is bonded to four others by strong covalent bonds; a large amount of energy is needed to break these bonds."),
        PQ("Write equations for the reaction of (a) phosphorus(V) oxide with water and (b) aluminium oxide with sodium hydroxide solution. State what the second reaction shows.",
           "(a) P4O10 + 6H2O → 4H3PO4. (b) Al2O3 + 2NaOH + 3H2O → 2Na[Al(OH)4]. Because aluminium oxide also reacts with acids (Al2O3 + 6HCl → 2AlCl3 + 3H2O), it is amphoteric."),
        PQ("Anhydrous aluminium chloride fumes in moist air and gives an acidic solution with water. Explain these observations with an equation.",
           "Anhydrous AlCl3 is covalent and is hydrolysed by the moisture in the air: AlCl3 + 3H2O → Al(OH)3 + 3HCl. The hydrogen chloride gas forms white fumes with moist air and dissolves to give hydrochloric acid, so the solution is acidic. (In water the hydrated ion [Al(H2O)6]^3+ also donates protons.)"),
        PQ("Explain why the first ionization energy of aluminium is lower than that of magnesium.",
           "The outer electron removed from aluminium is in a 3p orbital, which is higher in energy than the 3s orbital of magnesium and is partly shielded by the 3s electrons. It is therefore less strongly held and easier to remove, despite aluminium having one more proton."),
        SUM("Across Period 3: atomic radius falls, first ionization energy generally rises (dips at Al and S) and electronegativity rises.",
            "Melting point: giant metallic (Na, Mg, Al) rises with charge; giant covalent Si is highest; simple molecular P4, S8, Cl2, Ar are low.",
            "Oxides change from basic (Na2O, MgO) to amphoteric (Al2O3) to acidic (SiO2, P4O10, SO2, SO3, Cl2O7).",
            "Chlorides change from ionic (NaCl, MgCl2) to covalent (Al2Cl6, SiCl4, PCl5); covalent chlorides are hydrolysed to give HCl and acidic solutions."),
    ])]

# ============================================================================================
# 2. Groups I and II
# ============================================================================================
LESSONS += [lesson(
    module=M_P, topic="Groups I and II",
    title="Groups I and II: reactivity, solubility and thermal stability",
    slug="chu2-groups-i-and-ii", minutes=24,
    summary="Group I and II metals become more reactive down the group; hydroxide solubility rises, sulfate solubility falls and carbonates and nitrates become more stable to heat, all explained by ion size, lattice energy and polarization.",
    objectives=[
        "Explain the trend in reactivity and the reactions of the metals with water and oxygen",
        "Explain the trends in solubility of Group II hydroxides and sulfates",
        "Explain the trend in thermal stability of carbonates and nitrates using polarization, and write the equations",
        "Describe the diagonal relationships Li-Mg and Be-Al and the flame test colours",
    ],
    key_concepts=["Reactivity trend", "Flame tests", "Polarizing power", "Thermal decomposition", "Lattice energy and hydration enthalpy", "Diagonal relationship"],
    blocks=[
        H("Introduction"),
        T("Wood ash used for making soap at home contains potassium carbonate. Lime (calcium oxide) is spread on soil and added to cement; milk of magnesia contains magnesium hydroxide; the red colour of fireworks comes from strontium salts. "
          "These are the **s-block** metals. Their outer electrons are in an s orbital: one in Group I (the alkali metals) and two in Group II (the alkaline earth metals). Their chemistry is a clean example of how ion size controls properties."),
        H("Reactivity and reactions of the metals"),
        T("Going down a group the atoms get larger, the outer electron(s) are further from the nucleus and better shielded, so the **ionization energy falls** and the metals lose electrons more easily. **Reactivity increases down both groups.** Group I metals are more reactive than the Group II metal in the same period because they need only one electron to be removed."),
        CODE("Metal   With cold water                            Flame colour\n"
             "Li      steady fizzing, floats, slow                crimson-red\n"
             "Na      vigorous, melts into a ball, fizzes        golden-yellow\n"
             "K       violent, burns with a lilac flame           lilac\n"
             "Mg      very slow with cold water; burns in steam  none (white flame in air)\n"
             "Ca      steady fizzing, cloudy white suspension    brick-red\n"
             "Sr      faster                                     crimson\n"
             "Ba      vigorous                                   apple-green", "text",
             title="Observations (standard textbook values; check your textbook for exact wording)"),
        F(r"<<2Na + 2H2O -> 2NaOH + H2>>"),
        F(r"<<Ca + 2H2O -> Ca(OH)2 + H2>>"),
        F(r"<<Mg + H2O -> MgO + H2>>"),
        T("The last equation is for magnesium in steam. All the reactions give hydrogen; the Group I solutions are strongly alkaline. Metals burn in oxygen: [[2Mg + O2 -> 2MgO]] with a bright white flame, and lithium gives the normal oxide [[4Li + O2 -> 2Li2O]]. Sodium forms mainly the peroxide [[2Na + O2 -> Na2O2]] in excess oxygen and potassium forms a superoxide, [[KO2]] (check your textbook)."),
        T("In a **flame test**, electrons are excited by the heat and then fall back to lower energy levels, emitting light of a characteristic colour. The colours are used to identify the cation in qualitative analysis."),
        H("Solubility of Group II compounds"),
        KEY("Two opposite trends", "Dissolving needs energy to break the lattice (the **lattice energy**) and releases energy as ions are surrounded by water (the **hydration enthalpy**). Both fall as the cation gets bigger. Which falls faster decides the trend.",
            cards=[["Hydroxides: solubility increases down", "The OH^- ion is small, so the lattice energy falls steeply as the cation gets bigger. This drop is larger than the fall in hydration enthalpy, so dissolving becomes easier. Mg(OH)2 is almost insoluble; Ba(OH)2 is fairly soluble."],
                   ["Sulfates: solubility decreases down", "The SO4^2- ion is large, so the lattice energy changes very little as the cation grows. The hydration enthalpy of the cation falls significantly, so dissolving becomes less favourable. MgSO4 is soluble; BaSO4 is insoluble."]]),
        T("The insolubility of barium sulfate is the basis of the test for sulfate ions: acidified barium chloride (or barium nitrate) gives a white precipitate, [[Ba^2+ + SO4^2- -> BaSO4]]. The acid removes carbonate and sulfite, which would also give white precipitates with barium ions."),
        H("Thermal stability of carbonates and nitrates"),
        D("**Polarizing power** is the ability of a small, highly charged cation to distort the electron cloud of a nearby anion. The larger and more polarized the anion, the weaker its bonds, so the compound decomposes more easily on heating.", title="Polarization"),
        T("Down Group II the cation radius increases, so its charge density and polarizing power decrease. The carbonate ion is distorted less, so more heat is needed to decompose the carbonate. **Thermal stability of carbonates and nitrates increases down Group II.**"),
        F(r"<<CaCO3 -> CaO + CO2>>"),
        F(r"<<2Mg(NO3)2 -> 2MgO + 4NO2 + O2>>"),
        T("Group I carbonates (except lithium carbonate) do not decompose in a Bunsen flame because the cations have a lower charge and a larger radius. Group I nitrates also decompose less: sodium and potassium nitrates give the nitrite and oxygen, but lithium nitrate behaves like the Group II nitrates."),
        F(r"<<2NaNO3 -> 2NaNO2 + O2>>"),
        F(r"<<4LiNO3 -> 2Li2O + 4NO2 + O2>>"),
        F(r"<<Li2CO3 -> Li2O + CO2>>"),
        H("Diagonal relationships"),
        T("The first element of a group resembles the second element of the *next* group. Lithium is small with a high charge density, close to magnesium. Both form a normal oxide, a nitride ([[Li3N]], [[Mg3N2]]) when heated in nitrogen, carbonates that decompose on heating and poorly soluble carbonates, phosphates and fluorides. "
          "Beryllium resembles aluminium: BeO and Al2O3 are amphoteric, and both chlorides are covalent. Beryllium oxide reacts with acid and with alkali."),
        F(r"<<BeO + 2HCl -> BeCl2 + H2O>>"),
        F(r"<<BeO + 2NaOH + H2O -> Na2[Be(OH)4]>>"),
        EX("Worked example 1: heating calcium carbonate", intro="2.00 g of calcium carbonate is heated strongly until it has decomposed completely. Find the mass of calcium oxide formed and the volume of carbon dioxide at room temperature and pressure (24 dm³/mol). (Ca = 40, C = 12, O = 16)",
           steps=[
               S("Equation", math=r"<<CaCO3 -> CaO + CO2>>"),
               S("Moles of CaCO3", math=r"\dfrac{2.00}{100} = 0.0200\ \text{mol}"),
               S("Moles of CaO and CO2", text="Ratio 1 : 1 : 1, so 0.0200 mol of each."),
               S("Mass of CaO", math=r"0.0200 \times 56 = 1.12\ \text{g}"),
               S("Volume of CO2 at rtp", math=r"0.0200 \times 24 = 0.480\ \text{dm}^3"),
           ]),
        EX("Worked example 2: explaining a trend", intro="Explain why barium carbonate needs a higher temperature than magnesium carbonate to decompose.",
           steps=[
               S("Compare the cations", text="Ba^2+ is much larger than Mg^2+ with the same charge, so Ba^2+ has a lower charge density."),
               S("Polarization", text="Ba^2+ polarizes the carbonate ion less, so the C-O bond in carbonate that must break is distorted less."),
               S("Conclude", text="BaCO3 is more thermally stable, so more energy (a higher temperature) is needed to give BaO and CO2."),
           ]),
        MISTAKE("Mixing up the two solubility trends", "Hydroxides get more soluble down Group II; sulfates get less soluble. Learn them as a pair. The explanation uses the anion size: small OH^- (lattice energy changes more), large SO4^2- (lattice energy changes little)."),
        MISTAKE("Explaining thermal stability by ionization energy", "Decomposition of a carbonate or nitrate is explained by polarization of the anion by the cation (charge density), not by the ionization energy of the metal."),
        TIP("The Board's 2023 report listed the action of heat on sodium nitrate, the diagonal relationship of lithium and magnesium, and the solubility of Group II sulfates among the concepts tested; candidates found the sulfate explanation difficult. Write: the lattice energy hardly changes, the hydration enthalpy falls, so dissolving is less favourable.", title="Exam link"),
        QUIZ("Which equation describes what happens when sodium nitrate is heated?", [r"$\mathrm{2NaNO_3 \rightarrow 2NaNO_2 + O_2}$", r"$\mathrm{2NaNO_3 \rightarrow Na_2O + 2NO_2 + \tfrac{1}{2}O_2}$", r"$\mathrm{NaNO_3 \rightarrow Na + NO_3}$", r"$\mathrm{NaNO_3 \rightarrow NaO + NO_2}$"], 0,
             "Group I nitrates (except lithium) give the nitrite and oxygen only.",
             hint="Do the Group I nitrates make a brown gas?",
             feedback=["", "This would be an oxide, as for lithium nitrate and the Group II nitrates; sodium nitrate stops at the nitrite.", "The nitrate does not simply separate into its elements on heating.", "NaO is not a stable formula for any oxide, and the equation is not balanced."]),
        QUIZ("Why is barium sulfate less soluble than magnesium sulfate?", ["Ba^2+ has a higher charge", "The hydration enthalpy of the cation falls more than the lattice energy changes", "Ba^2+ is smaller", "The lattice energy of barium sulfate is much larger than that of magnesium sulfate"], 1,
             "The large sulfate ion keeps the lattice energy almost constant while the hydration enthalpy of the cation falls down the group, so dissolving is less favourable.",
             hint="Which energy term changes little for a large anion?",
             feedback=["Both ions have a 2+ charge.", "", "Ba^2+ is larger than Mg^2+.", "The lattice energy of sulfates changes only slightly down the group; the main change is in the hydration enthalpy."]),
        PQ("(a) State the trend in thermal stability of the Group II carbonates. (b) Explain it. (c) Write an equation for the decomposition of magnesium carbonate.",
           "(a) Stability increases down the group (MgCO3 decomposes at a lower temperature than BaCO3). (b) The cation radius increases down the group, so the charge density and polarizing power fall; the carbonate ion is polarized (distorted) less, so the compound resists decomposition more. (c) MgCO3 → MgO + CO2."),
        PQ("Describe what you would see when a small piece of potassium is added to water, and write an equation. Why is the reaction more violent than that of sodium?",
           "It floats, melts into a ball, moves on the surface and fizzes (hydrogen), and burns with a lilac flame; the solution is alkaline. 2K + 2H2O → 2KOH + H2. Potassium is more reactive because its outer electron is further from the nucleus and better shielded, so its first ionization energy is lower."),
        PQ("Write equations for the thermal decomposition of (a) lithium carbonate and (b) calcium nitrate, and explain why lithium carbonate decomposes although sodium carbonate does not.",
           "(a) Li2CO3 → Li2O + CO2. (b) 2Ca(NO3)2 → 2CaO + 4NO2 + O2. Li+ is very small so its charge density is high, much like Mg^2+. It polarizes the carbonate ion enough for decomposition; Na+ is larger and polarizes the carbonate ion much less."),
        PQ("Beryllium oxide reacts with both hydrochloric acid and sodium hydroxide solution. State what this shows and write the two equations. Which Period 3 element does beryllium resemble?",
           "BeO is amphoteric. BeO + 2HCl → BeCl2 + H2O; BeO + 2NaOH + H2O → Na2[Be(OH)4]. Beryllium resembles aluminium (a diagonal relationship)."),
        SUM("Reactivity increases down Groups I and II because ionization energy falls; Group I is more reactive than Group II in the same period.",
            "Flame test colours: Li crimson, Na golden-yellow, K lilac, Ca brick-red, Sr crimson, Ba apple-green.",
            "Group II hydroxides get more soluble down the group; sulfates get less soluble.",
            "Carbonates and nitrates of Group II get more thermally stable down the group because the polarizing power of the cation falls.",
            "Li resembles Mg and Be resembles Al (diagonal relationship); BeO is amphoteric."),
    ])]

# ============================================================================================
# 3. Group IV
# ============================================================================================
LESSONS += [lesson(
    module=M_P, topic="Group IV",
    title="Group IV: carbon to lead and the inert pair effect",
    slug="chu2-group-iv", minutes=22,
    summary="Down Group IV the elements change from non-metal to metal, the +2 oxidation state becomes more stable than +4 (the inert pair effect), and the oxides and chlorides change character accordingly.",
    objectives=[
        "Describe the variation in physical properties and metallic character from C to Pb",
        "Explain the inert pair effect and the stability of the +2 and +4 states",
        "Describe the oxides, chlorides and acid-base character of the Group IV elements",
        "Explain why carbon is different from the rest of the group",
    ],
    key_concepts=["Metallic character", "Inert pair effect", "Oxidation states +2 and +4", "Amphoteric oxides", "Hydrolysis of tetrachlorides", "Catenation"],
    blocks=[
        H("Introduction"),
        T("The pencil lead in your bag is graphite, a form of carbon. The sand on the beach and the glass in a window are silicon dioxide. The solder in electronics contains tin and lead, and the old car batteries used in many Cameroonian towns contain lead and lead(IV) oxide. "
          "These are all **Group IV** elements: carbon, silicon, germanium, tin and lead, each with the outer configuration ns2 np2. Going down the group you move from a non-metal to a metal."),
        H("Physical properties"),
        CODE("Element   Type         Structure              Melting point (approx., C)   Conductivity\n"
             "C         non-metal    giant covalent         3500 (diamond, sublimes)     diamond none; graphite good\n"
             "Si        metalloid    giant covalent         1410                         semiconductor\n"
             "Ge        metalloid    giant covalent         940                          semiconductor\n"
             "Sn        metal        giant metallic         232                          good\n"
             "Pb        metal        giant metallic         327                          good", "text",
             title="Group IV elements (approximate values)"),
        T("The melting points fall from carbon to tin because the bonds in the structure get weaker as the atoms get bigger and the bond lengths longer. The pattern is not perfectly smooth: lead melts a little higher than tin. "
          "The change from covalent to metallic bonding explains the rise in electrical conductivity from carbon (diamond) to tin and lead."),
        H("The inert pair effect"),
        D("The **inert pair effect** is the increasing reluctance of the ns2 electrons to take part in bonding as you go down a group, so that the oxidation state two less than the group number becomes more stable. In Group IV, the **+2 state becomes more stable than +4 down the group**.", title="Inert pair effect"),
        T("The ns2 electrons of the heavy atoms are held more strongly (poor shielding by the filled d and f sub-shells, so the effective nuclear charge is high). The energy needed to use them for bonding is not recovered by the extra bonds. The result:"),
        KEY("Stability of oxidation states", "",
            cards=[["Carbon and silicon", "Almost always +4 (CO2, SiO2, CCl4, SiCl4). Carbon monoxide (+2) is easily oxidized to CO2."],
                   ["Tin", "Both +2 and +4 occur. Sn(II) is a reducing agent: Sn^2+ is easily oxidized to Sn^4+."],
                   ["Lead", "+2 is the stable state (PbCl2, PbO, Pb^2+ salts). Lead(IV) compounds are strong oxidizing agents: PbO2 is reduced easily to Pb(II)."]]),
        F(r"<<PbO2 + 4HCl -> PbCl2 + Cl2 + 2H2O>>"),
        F(r"<<Sn^2+ + 2Fe^3+ -> Sn^4+ + 2Fe^2+>>"),
        T("Lead(IV) chloride, PbCl4, is unstable and decomposes at room temperature: [[PbCl4 -> PbCl2 + Cl2]]. Compare this with CCl4, SiCl4 and SnCl4, which are stable."),
        H("Oxides and chlorides"),
        T("The oxides show the change from acidic to amphoteric as the metallic character grows. **CO2** and **SiO2** are acidic. **GeO2**, **SnO2** and **PbO2** are amphoteric (check your textbook for GeO2). The +2 oxides **SnO** and **PbO** are amphoteric; **CO** is neutral."),
        F(r"<<PbO + 2HNO3 -> Pb(NO3)2 + H2O>>"),
        F(r"<<PbO + 2NaOH + H2O -> Na2[Pb(OH)4]>>"),
        T("Lead(II) and tin(II) hydroxides likewise dissolve in excess sodium hydroxide, which is used in qualitative analysis: a white precipitate that dissolves in excess alkali suggests Pb^2+ (or Sn^2+, Al^3+ or Zn^2+, which must be separated by further tests)."),
        KEY("Tetrachlorides and water", "",
            cards=[["CCl4: no reaction", "Carbon has no low-lying empty orbitals in its second shell, so it cannot accept a lone pair from water; the C-Cl bond is also strong and CCl4 is non-polar overall."],
                   ["SiCl4: violent hydrolysis", "Silicon has empty 3d orbitals that can accept a lone pair from a water molecule, so SiCl4 fumes in moist air: SiCl4 + 2H2O gives SiO2 and 4HCl."]]),
        F(r"<<SiCl4 + 2H2O -> SiO2 + 4HCl>>"),
        H("What makes carbon special"),
        T("Carbon differs from the rest of the group in several ways, a favourite theme of the examiners. It forms strong C-C bonds and long chains and rings (**catenation**, which explains organic chemistry), it forms stable multiple bonds (C=C, C≡C, C=O) because its atoms are small, it cannot expand its octet because it has no d orbitals in its second shell, and its oxide CO2 is a gas made of simple molecules while SiO2 is a giant covalent solid. "
          "Silicon-silicon bonds are weaker, so silicon hydrides (silanes) are less stable than alkanes and are readily attacked by water, while methane is not."),
        EX("Worked example 1: oxidation states", intro="Lead forms PbCl2 but not a stable PbCl4, whereas carbon forms CCl4 but not a stable CCl2. Explain the difference.",
           steps=[
               S("State the effect", text="The inert pair effect: the 6s2 electrons of lead are reluctant to take part in bonding."),
               S("Apply to lead", text="Lead uses only its 6p electrons to form Pb(II). The +4 state needs the 6s electrons too and is therefore a strong oxidizing state: Pb(IV) tends to gain two electrons to become Pb(II)."),
               S("Apply to carbon", text="For carbon the 2s electrons are close to the nucleus and well used in bonding. Four strong covalent bonds, giving +4, release more energy than two bonds."),
           ]),
        EX("Worked example 2: identifying a compound", intro="A dark brown solid A reacts with warm concentrated hydrochloric acid to give a greenish-yellow gas, which bleaches damp litmus paper, and a white solid that dissolves in hot water. Identify A and the white solid.",
           steps=[
               S("The gas", text="A greenish-yellow gas that bleaches damp litmus is chlorine: A is an oxidizing agent."),
               S("The solid", text="PbO2 is a dark brown strong oxidizing agent of Pb(IV). It oxidizes chloride ions to chlorine and is reduced to Pb(II)."),
               S("Write the equation", math=r"<<PbO2 + 4HCl -> PbCl2 + Cl2 + 2H2O>>"),
               S("Conclude", text="A is lead(IV) oxide and the white solid is lead(II) chloride, which is soluble in hot water."),
           ]),
        MISTAKE("Saying carbon has no +2 state", "Carbon forms CO (+2). The inert pair effect makes +2 stable only for the heavy elements; CO is a reducing agent that is easily oxidized to CO2."),
        MISTAKE("Explaining CCl4 stability with bond energy only", "The usual full answer is that carbon has no available d orbitals, so a water molecule cannot attack the carbon by donating a lone pair. Silicon has accessible 3d orbitals."),
        TIP("The Board's 2023 report lists the variation of physical properties down Group IV, the acid-base character of the oxides and the unique properties of carbon among its multiple-choice concepts, and Paper 2 on the inorganic section had difficulty with explanations. Always name the effect (inert pair, polarization or d orbitals) before you give the detail.", title="Exam link"),
        QUIZ("Which Group IV chloride does NOT exist as a stable compound at room temperature?", [r"$\mathrm{CCl_4}$", r"$\mathrm{SiCl_4}$", r"$\mathrm{SnCl_4}$", r"$\mathrm{PbCl_4}$"], 3,
             "Lead(IV) chloride decomposes to lead(II) chloride and chlorine because of the inert pair effect.",
             hint="Which element has the most stable +2 state?",
             feedback=["CCl4 is stable (but not hydrolysed).", "SiCl4 is stable in dry conditions; it is hydrolysed by water.", "SnCl4 is stable.", ""]),
        QUIZ("What is the acid-base nature of lead(IV) oxide?", ["Acidic only", "Basic only", "Amphoteric", "Neutral"], 2,
             "PbO2 reacts with concentrated alkali to form plumbate(IV) ions and with acids, so it is amphoteric (with the extra feature of being an oxidizing agent).",
             hint="Metallic character is higher for lead than for carbon.",
             feedback=["CO2 and SiO2 are acidic; PbO2 is more metallic.", "Basic oxides belong to strongly metallic elements such as Na or Ca.", "", "CO is the neutral oxide of the group; PbO2 is not neutral."]),
        PQ("Explain the term inert pair effect and use it to explain why tin(II) is a reducing agent but lead(II) is not.",
           "The inert pair effect is the reluctance of the ns2 electrons of the heavier p-block elements to be used in bonding, so the oxidation state two below the group number becomes more stable down the group. For tin, +4 is comparable in stability to +2, so Sn(II) can lose two more electrons and be oxidized to Sn(IV): it is a reducing agent. For lead, +2 is much more stable than +4, so Pb(II) is not easily oxidized."),
        PQ("Silicon tetrachloride fumes in moist air but carbon tetrachloride does not. Explain the difference and write an equation for the reaction of silicon tetrachloride with water.",
           "SiCl4 has empty 3d orbitals, so a water molecule can donate a lone pair to the silicon atom and the molecule is hydrolysed. Carbon has no available d orbitals in its second shell, so CCl4 cannot be attacked this way. SiCl4 + 2H2O → SiO2 + 4HCl (white fumes of HCl)."),
        PQ("Describe and explain how the acid-base character of the oxides changes from CO2 to PbO2, giving one equation.",
           "The oxides change from acidic (CO2, SiO2) to amphoteric (SnO2, PbO2) as the elements become more metallic and the bonding in the oxide becomes more ionic. An example is PbO + 2HNO3 → Pb(NO3)2 + H2O (acting as a base), and PbO + 2NaOH + H2O → Na2[Pb(OH)4] (acting as an acid)."),
        PQ("Give three ways in which carbon differs from the other Group IV elements.",
           "Carbon forms strong C-C bonds and long chains (catenation); it forms stable multiple bonds because it is small; it has no d orbitals in its second shell, so its tetrachloride is not hydrolysed and it cannot expand its octet; CO2 is a simple molecule while SiO2 is a giant covalent solid."),
        SUM("Group IV changes from non-metal (C) through metalloids (Si, Ge) to metals (Sn, Pb).",
            "The inert pair effect makes +2 more stable down the group: Sn(II) is a reducing agent and Pb(IV) is an oxidizing agent.",
            "Oxides change from acidic (CO2, SiO2) to amphoteric (SnO2, PbO2); the +2 oxides SnO and PbO are amphoteric.",
            "SiCl4 is hydrolysed by water, CCl4 is not; PbCl4 is unstable.",
            "Carbon is special: catenation, multiple bonds, no d orbitals, and a gaseous molecular oxide."),
    ])]

# ============================================================================================
# 4. Group VII
# ============================================================================================
LESSONS += [lesson(
    module=M_P, topic="Group VII",
    title="Group VII: the halogens, halides and oxoacids",
    slug="chu2-group-vii", minutes=24,
    summary="Oxidizing power of the halogens falls down Group VII while the reducing power of the halide ions rises; chlorine disproportionates in alkali and the oxoacids of chlorine get stronger as the oxidation state rises.",
    objectives=[
        "Describe the physical properties and the trend in oxidizing power of the halogens",
        "Explain displacement reactions and the reactions of halides with concentrated sulfuric acid",
        "Describe the tests for halide ions and the properties of the hydrogen halides",
        "Define disproportionation and write equations for chlorine with water and with cold and hot alkali; compare the strengths of chlorine oxoacids",
    ],
    key_concepts=["Oxidizing power trend", "Displacement", "Halide reducing power", "Silver halide tests", "Disproportionation", "Strength of oxoacids"],
    blocks=[
        H("Introduction"),
        T("Chlorine is added to water in treatment plants and swimming pools; household bleach contains sodium chlorate(I); iodine is added to table salt in many countries to prevent goitre; silver bromide is the light-sensitive part of photographic film. "
          "The **halogens** (Group VII: fluorine, chlorine, bromine, iodine) are reactive non-metals whose molecules are diatomic. They are a classic example of a group in which the trend in redox behaviour is clear and can be explained."),
        H("Physical properties and oxidizing power"),
        CODE("Halogen   Colour and state at room temperature     Boiling point (approx., C)   E(X2/X-) volts\n"
             "F2        pale yellow gas                            -188                       +2.87\n"
             "Cl2       greenish-yellow gas                        -34                        +1.36\n"
             "Br2       red-brown liquid (orange vapour)           59                         +1.07\n"
             "I2        grey-black solid (purple vapour)           184 (sublimes on warming)  +0.54", "text",
             title="The halogens (approximate values)"),
        T("The boiling point rises down the group because the molecules have more electrons, so the London forces between them are stronger. The **oxidizing power falls** down the group: the atoms are bigger, the electron to be gained is further from the nucleus and better shielded, so the standard electrode potential falls from +2.87 V (F2) to +0.54 V (I2). A halogen oxidizes the halide ions of the halogens below it."),
        H("Displacement reactions"),
        F(r"<<Cl2 + 2Br^- -> 2Cl^- + Br2>>"),
        F(r"<<Cl2 + 2I^- -> 2Cl^- + I2>>"),
        F(r"<<Br2 + 2I^- -> 2Br^- + I2>>"),
        T("Chlorine water added to potassium bromide solution turns it orange or brown (bromine); added to potassium iodide it gives a brown solution or a black solid (iodine). Bromine does not oxidize chloride ions, because Br2 is a weaker oxidizing agent than Cl2. Adding an organic solvent such as hexane or cyclohexane makes the colours clearer: chlorine is almost colourless, bromine orange-red and iodine purple in the organic layer."),
        H("Halides with concentrated sulfuric acid"),
        T("The **reducing power of the halide ions rises down the group** (I^- > Br^- > Cl^-), because the larger ion loses its electron more easily. Concentrated sulfuric acid, itself an oxidizing agent, shows this clearly."),
        CODE("Halide   Products with concentrated H2SO4                     Acid reduced to?\n"
             "NaCl     steamy white fumes of HCl only                      not reduced (no redox)\n"
             "NaBr     HBr, then red-brown Br2 fumes and choking SO2       SO2\n"
             "NaI      HI, then purple I2 vapour, yellow solid S,           SO2, S and H2S\n"
             "         smell of bad eggs (H2S)", "text",
             title="Observations"),
        F(r"<<NaCl + H2SO4 -> NaHSO4 + HCl>>"),
        F(r"<<2HBr + H2SO4 -> Br2 + SO2 + 2H2O>>"),
        F(r"<<8HI + H2SO4 -> 4I2 + H2S + 4H2O>>"),
        H("Tests and hydrogen halides"),
        T("To test for halide ions, add dilute nitric acid and then silver nitrate solution. The acid removes carbonate. Then test the solubility of the precipitate in ammonia solution."),
        CODE("Ion   Precipitate with Ag+     Dilute NH3      Concentrated NH3\n"
             "Cl-   white AgCl              dissolves       dissolves\n"
             "Br-   cream AgBr              insoluble       dissolves\n"
             "I-    yellow AgI              insoluble       insoluble", "text",
             title="Silver halide precipitates"),
        F(r"<<Ag^+ + Cl^- -> AgCl>>"),
        T("The thermal stability of the hydrogen halides falls from HF to HI because the H-X bond gets longer and weaker (bond enthalpies about 562, 431, 366 and 299 kJ/mol). HI decomposes on moderate heating into hydrogen and violet iodine vapour. In water, HCl, HBr and HI are strong acids; HF is a weak acid because the H-F bond is so strong and the fluoride ion is strongly hydrated and hydrogen-bonded."),
        H("Disproportionation of chlorine"),
        D("**Disproportionation** is a redox reaction in which the **same element is simultaneously oxidized and reduced**. Chlorine, oxidation state 0, goes to -1 (reduced) and to +1 or +5 (oxidized).", title="Disproportionation"),
        F(r"<<Cl2 + H2O <=> HCl + HClO>>"),
        F(r"<<Cl2 + 2NaOH -> NaCl + NaClO + H2O>>"),
        F(r"<<3Cl2 + 6KOH -> 5KCl + KClO3 + 3H2O>>"),
        T("With cold dilute alkali the product is the chlorate(I) ion, ClO^- (bleach); with hot concentrated alkali the chlorate(V) ion, ClO3^-, forms. In the last equation chlorine goes from 0 to -1 in 5 Cl^- and from 0 to +5 in one ClO3^-. The 2023 Board report noted that writing the hot-alkali equation caused difficulty. Chlorine in water also gives HClO (chloric(I) acid), which kills germs; this is why water works use chlorine."),
        H("Oxoacids of chlorine"),
        CODE("Acid     Formula   Oxidation state of Cl   Strength\n"
             "chloric(I)   HClO     +1                     weak (pKa about 7.5)\n"
             "chloric(III) HClO2    +3                     weak (pKa about 2)\n"
             "chloric(V)   HClO3    +5                     strong\n"
             "chloric(VII) HClO4    +7                     very strong", "text", title="Chlorine oxoacids (values approximate; check your textbook)"),
        T("The acid strength rises as the number of oxygen atoms increases. The extra electronegative oxygen atoms pull electron density from the O-H bond and spread the negative charge of the anion over more atoms (delocalization), which makes the anion more stable and so the acid is stronger. For the same oxidation state, acid strength falls as the halogen gets larger: HClO > HBrO > HIO."),
        EX("Worked example 1: halide analysis", intro="25.0 cm³ of 0.100 mol/dm³ sodium chloride solution is treated with excess acidified silver nitrate. Find the mass of silver chloride precipitated. (Ag = 108, Cl = 35.5)",
           steps=[
               S("Equation", math=r"<<Ag^+ + Cl^- -> AgCl>>"),
               S("Moles of chloride", math=r"0.100 \times 0.0250 = 2.50 \times 10^{-3}\ \text{mol}"),
               S("Moles of AgCl", text="Ratio 1 : 1, so 2.50 x 10^-3 mol."),
               S("Mass", math=r"2.50 \times 10^{-3} \times 143.5 = 0.359\ \text{g}"),
           ]),
        EX("Worked example 2: oxidation numbers in a disproportionation", intro="Show that the reaction of chlorine with hot concentrated potassium hydroxide is a disproportionation.",
           steps=[
               S("Write the equation", math=r"<<3Cl2 + 6KOH -> 5KCl + KClO3 + 3H2O>>"),
               S("Oxidation numbers of chlorine", text="Cl2: 0. KCl: -1. KClO3: +5 (K +1, O -2 x 3 = -6, so Cl = +5)."),
               S("Interpret", text="Five Cl atoms are reduced from 0 to -1 (gain 5 electrons) and one Cl atom is oxidized from 0 to +5 (loses 5 electrons). The same element is both oxidized and reduced: disproportionation."),
           ]),
        MISTAKE("Saying fluorine is the weakest oxidizing agent", "Fluorine is the strongest oxidizing agent of the group (E = +2.87 V). The trend is that oxidizing power falls from F2 to I2."),
        MISTAKE("Using one equation for both alkali reactions", "Cold dilute alkali gives chlorate(I), ClO^-. Hot concentrated alkali gives chlorate(V), ClO3^-. Check the oxidation number of Cl in your products and balance the equation."),
        TIP("The Board's 2023 report lists properties of the halogens, the acid strength of the oxoacids of the halogens and the disproportionation of chlorine in hot concentrated potassium hydroxide among the items tested in Paper 1 and Paper 2. In qualitative practicals you may be asked to identify a halide from the silver nitrate and ammonia tests.", title="Exam link"),
        QUIZ("Which observation is made when concentrated sulfuric acid is added to solid sodium iodide?", ["Steamy white fumes only", "Red-brown fumes of bromine", "Purple vapour, a yellow solid and a smell of bad eggs", "A colourless solution with no gas"], 2,
             "Iodide is a strong reducing agent and reduces sulfuric acid to SO2, S and H2S, forming iodine (purple vapour).",
             hint="Which halide is the strongest reducing agent?",
             feedback=["That is the result with sodium chloride.", "That is the result with sodium bromide.", "", "A vigorous reaction occurs; iodide is oxidized."]),
        QUIZ("Which acid is the strongest?", [r"$\mathrm{HClO}$", r"$\mathrm{HClO_2}$", r"$\mathrm{HClO_3}$", r"$\mathrm{HClO_4}$"], 3,
             "HClO4 has the most oxygen atoms; its anion is stabilized by delocalization over four oxygen atoms.",
             hint="Count oxygen atoms and the oxidation state of Cl.",
             feedback=["HClO has only one oxygen atom and is a weak acid.", "HClO2 is weak.", "HClO3 is strong but weaker than HClO4.", ""]),
        PQ("Describe what you would observe and write an ionic equation when chlorine water is added to aqueous potassium iodide. What does this show about the oxidizing power of chlorine and iodine?",
           "The colourless solution turns brown (and a black solid may form) because iodine is produced. Cl2 + 2I^- → 2Cl^- + I2. Chlorine is a stronger oxidizing agent than iodine (it oxidizes I^- to I2) because the E value of Cl2/Cl^- (+1.36 V) is more positive than that of I2/I^- (+0.54 V)."),
        PQ("Solid sodium chloride and solid sodium bromide are each treated with concentrated sulfuric acid. Describe the observations and explain the difference.",
           "NaCl gives steamy white fumes of HCl only: NaCl + H2SO4 → NaHSO4 + HCl; chloride is too weak a reducing agent to reduce the acid. NaBr gives HBr, but HBr is oxidized by the acid to red-brown bromine and colourless, choking SO2: 2HBr + H2SO4 → Br2 + SO2 + 2H2O. Bromide is a stronger reducing agent than chloride because the larger ion loses its electron more easily."),
        PQ("(a) Write an equation for the reaction of chlorine with hot concentrated potassium hydroxide solution. (b) Explain why it is a disproportionation.",
           "(a) 3Cl2 + 6KOH → 5KCl + KClO3 + 3H2O. (b) Chlorine (0) is reduced to chloride (-1) in KCl and oxidized to chlorate(V) (+5) in KClO3; the same element is both oxidized and reduced."),
        PQ("Explain why HClO4 is a stronger acid than HClO.",
           "In HClO4 the chlorine is in oxidation state +7 and is bonded to three extra oxygen atoms. They withdraw electron density from the O-H bond and the negative charge of the perchlorate ion is delocalized over four oxygen atoms, making ClO4^- very stable. In HClO the anion has one oxygen atom only, so the charge is not spread out and the acid is weak."),
        SUM("Down Group VII boiling point rises and oxidizing power falls; a halogen displaces halides of the elements below it.",
            "Reducing power of halides rises Cl- < Br- < I-: concentrated H2SO4 gives HCl only, then Br2 and SO2, then I2, S and H2S.",
            "Silver halides: AgCl white (dilute NH3), AgBr cream (conc. NH3), AgI yellow (insoluble).",
            "Disproportionation: Cl2 with cold dilute alkali gives ClO^-; with hot concentrated alkali gives ClO3^- and Cl^-.",
            "Acid strength of chlorine oxoacids rises HClO < HClO2 < HClO3 < HClO4."),
    ])]

# ============================================================================================
# 5. Properties of the 3d elements
# ============================================================================================
LESSONS += [lesson(
    module=M_T, topic="Properties of the 3d elements",
    title="The 3d elements: configurations, oxidation states, colour and catalysis",
    slug="chu2-3d-elements-properties", minutes=24,
    summary="Transition elements have partly filled d sub-shells in at least one ion, giving variable oxidation states, coloured compounds, catalytic activity, complex ions and paramagnetism.",
    objectives=[
        "Write the electronic configurations of the 3d atoms and their ions and define a transition element",
        "Explain variable oxidation states and the relative stability of Fe(II)/Fe(III) and Mn(II)/Mn(III)",
        "Describe the colours of common ions and explain catalytic activity and paramagnetism",
        "Write redox equations for iron(II) with manganate(VII) and dichromate(VI)",
    ],
    key_concepts=["Transition element", "Electronic configuration", "Variable oxidation state", "Paramagnetism", "Catalyst", "Half-filled d sub-shell"],
    blocks=[
        H("Introduction"),
        T("Steel rails, iron nails on a building site, copper wire for electricity, nickel coins and the zinc coating on a corrugated roof are all made from **3d elements**. Cocoa processing and fertilizer factories use iron and vanadium catalysts. "
          "These elements have special properties that the s-block metals do not: they form coloured compounds, have more than one oxidation state and form complex ions."),
        H("Definition and electronic configurations"),
        D("A **transition element** is a d-block element that forms **at least one ion with a partially filled d sub-shell**.", title="Transition element"),
        T("Scandium (Sc^3+ is 3d0) and zinc (Zn^2+ is 3d10) are d-block elements, but they are **not** transition elements by this definition. The 4s orbital fills before the 3d, but **when atoms form positive ions the 4s electrons are lost first**."),
        CODE("Atom   Configuration            Atom   Configuration\n"
             "Ti     [Ar] 3d2 4s2             Fe     [Ar] 3d6 4s2\n"
             "V      [Ar] 3d3 4s2             Co     [Ar] 3d7 4s2\n"
             "Cr     [Ar] 3d5 4s1  (not 3d4)  Ni     [Ar] 3d8 4s2\n"
             "Mn     [Ar] 3d5 4s2             Cu     [Ar] 3d10 4s1  (not 3d9)\n"
             "                                Zn     [Ar] 3d10 4s2\n"
             "\n"
             "Ions: Fe2+ [Ar] 3d6   Fe3+ [Ar] 3d5   Cu+ [Ar] 3d10   Cu2+ [Ar] 3d9   Cr3+ [Ar] 3d3   Mn2+ [Ar] 3d5", "text",
             title="Electronic configurations"),
        T("Chromium and copper are exceptions: a half-filled (3d5) or completely filled (3d10) sub-shell has extra stability, so one 4s electron moves into the 3d sub-shell."),
        H("Variable oxidation states"),
        T("The 4s and 3d energies are very close, so after losing the 4s electrons the atom can lose a variable number of 3d electrons with a modest rise in ionization energy. This gives several oxidation states, usually differing by one."),
        CODE("Element   Common oxidation states (colour of the aqueous species)\n"
             "V         +2 (violet), +3 (green), +4 VO2+ (blue), +5 VO2+ (yellow)\n"
             "Cr        +3 Cr3+ (green/violet), +6 Cr2O7 2- (orange), CrO4 2- (yellow)\n"
             "Mn        +2 (very pale pink), +4 MnO2 (brown solid), +7 MnO4- (purple)\n"
             "Fe        +2 (pale green), +3 (yellow-brown)\n"
             "Co        +2 (pink)\n"
             "Ni        +2 (green)\n"
             "Cu        +1 (colourless/white compounds), +2 (blue)\n"
             "Zn        +2 only (colourless)", "text",
             title="Oxidation states and colours (standard textbook values; check your textbook)"),
        T("In an oxidation reaction the oxidation number rises. Use oxidation numbers to see what changes. In [[MnO4^-]] the oxidation number of Mn is +7 (4 x -2 = -8; -8 + 7 = -1). In [[Cr2O7^2-]] each Cr is +6 (7 x -2 = -14; 2Cr = +12)."),
        F(r"<<MnO4^- + 8H^+ + 5Fe^2+ -> Mn^2+ + 4H2O + 5Fe^3+>>"),
        F(r"<<Cr2O7^2- + 14H^+ + 6Fe^2+ -> 2Cr^3+ + 7H2O + 6Fe^3+>>"),
        KEY("Why Fe(II) is oxidized easily but Mn(II) is not", "The Board's 2023 report noted that candidates could not explain this.",
            cards=[["Fe^2+ is 3d6", "Losing one more electron gives Fe^3+, 3d5, a half-filled and stable sub-shell. So Fe^2+ is readily oxidized to Fe^3+."],
                   ["Mn^2+ is 3d5", "It is already half-filled and extra stable. Removing another electron would destroy this stability, so Mn^2+ is not readily oxidized to Mn^3+ (a large amount of energy is needed)."]]),
        H("Colour, catalysis and magnetism"),
        T("**Colour.** Compounds of transition metal ions with partly filled d sub-shells are usually coloured (Cu^2+ blue, Fe^3+ yellow-brown, MnO4^- purple), whereas Sc^3+ (3d0), Zn^2+ and Cu^+ (3d10) compounds are colourless. The origin of colour is explained in a later lesson."),
        T("**Catalysis.** Transition metals and their compounds are good catalysts because they can change oxidation state and use the d orbitals to adsorb reactants. Examples: iron in the Haber process, vanadium(V) oxide in the Contact process, nickel in the hydrogenation of alkenes, manganese(IV) oxide in the decomposition of hydrogen peroxide."),
        T("In **homogeneous catalysis** the metal ions change oxidation state: Fe^2+/Fe^3+ catalyses the reaction between iodide ions and peroxodisulfate ions, [[S2O8^2- + 2I^- -> 2SO4^2- + I2]], by alternately reacting with each reactant."),
        T("**Magnetism.** Ions with unpaired d electrons are **paramagnetic** (they are weakly attracted into a magnetic field). Ions with no unpaired electrons, such as Zn^2+ and Cu^+, are **diamagnetic**. The more unpaired electrons, the greater the paramagnetism."),
        EX("Worked example 1: configurations", intro="Write the electronic configuration of Fe^3+ and Cu^2+, and state how many unpaired electrons each has. (Fe: atomic number 26; Cu: 29)",
           steps=[
               S("Fe atom", text="[Ar] 3d6 4s2."),
               S("Remove the 4s electrons first, then one 3d", text="Fe^3+: [Ar] 3d5. The five 3d electrons are in separate orbitals (Hund's rule), so there are 5 unpaired electrons."),
               S("Cu atom", text="[Ar] 3d10 4s1. Remove the 4s electron and one 3d electron: Cu^2+ is [Ar] 3d9, with 1 unpaired electron."),
           ]),
        EX("Worked example 2: a manganate(VII) titration", intro="A 25.0 cm³ sample of iron(II) sulfate solution needs 20.0 cm³ of 0.0200 mol/dm³ potassium manganate(VII) in acid. Find the concentration of Fe^2+.",
           steps=[
               S("Equation", math=r"<<MnO4^- + 8H^+ + 5Fe^2+ -> Mn^2+ + 4H2O + 5Fe^3+>>"),
               S("Moles of MnO4^-", math=r"0.0200 \times 0.0200 = 4.00 \times 10^{-4}\ \text{mol}"),
               S("Moles of Fe^2+", math=r"5 \times 4.00 \times 10^{-4} = 2.00 \times 10^{-3}\ \text{mol}"),
               S("Concentration", math=r"\dfrac{2.00 \times 10^{-3}}{0.0250} = 0.0800\ \text{mol/dm}^3"),
           ]),
        MISTAKE("Removing 3d electrons before 4s electrons", "The 4s electrons are lost first when an atom forms a positive ion. Fe^2+ is [Ar] 3d6, not [Ar] 3d4 4s2."),
        MISTAKE("Saying all d-block elements are transition elements", "Zinc forms only Zn^2+ (3d10) and scandium only Sc^3+ (3d0). Neither has a partially filled d sub-shell in its ions, so neither is a transition element."),
        TIP("The 3d elements are tested in Paper 1 (naming complexes, coordination and oxidation numbers) and Paper 2 (explaining oxidation-state stability, configurations, colour). The practical Paper 3 often uses an iron(II) or manganate(VII) titration.", title="Exam link"),
        QUIZ("What is the electronic configuration of the Cr atom?", ["[Ar] 3d4 4s2", "[Ar] 3d5 4s1", "[Ar] 3d6", "[Ar] 4s2 4p4"], 1,
             "Chromium takes one electron from 4s into the 3d sub-shell to give a half-filled, more stable 3d5.",
             hint="Which has extra stability: 3d4 4s2 or 3d5 4s1?",
             feedback=["This is the 'expected' configuration, but it is not the actual one.", "", "The two 4s electrons are not both removed from the atom.", "That is not a transition element configuration."]),
        QUIZ("Which of these is NOT a transition element?", ["Iron", "Copper", "Zinc", "Nickel"], 2,
             "Zinc forms only Zn^2+, 3d10: a full d sub-shell in all its compounds.",
             hint="Which one has a full 3d sub-shell in all its ions?",
             feedback=["Fe^2+ and Fe^3+ have partly filled d sub-shells.", "Cu^2+ is 3d9.", "", "Ni^2+ is 3d8."]),
        PQ("Define a transition element and explain why zinc is not one.",
           "A transition element is a d-block element that forms at least one ion with a partially filled d sub-shell. Zinc forms only Zn^2+, [Ar] 3d10, in which the 3d sub-shell is completely filled, so it does not meet the definition."),
        PQ("Explain why Fe^2+ is readily oxidized to Fe^3+ but Mn^2+ is not readily oxidized to Mn^3+.",
           "Fe^2+ is 3d6; removal of one electron gives Fe^3+, 3d5, with a stable half-filled sub-shell. Mn^2+ is already 3d5, which is stable, so a lot of energy would be needed to remove another electron from it."),
        PQ("Give three characteristic properties of transition elements, with an example of each.",
           "(i) Variable oxidation states, e.g. Mn (+2, +4, +7) or Fe (+2, +3). (ii) Coloured ions, e.g. Cu^2+ blue or MnO4^- purple. (iii) Catalytic activity, e.g. Fe in the Haber process or V2O5 in the Contact process. (Also complex ion formation and paramagnetism.)"),
        PQ("A solution of Fe^2+ ions requires 18.40 cm³ of 0.0200 mol/dm³ KMnO4 in a titration of a 25.0 cm³ sample. Calculate the concentration of Fe^2+ ions.",
           "n(MnO4^-) = 0.0200 x 0.01840 = 3.68 x 10^-4 mol. Ratio MnO4^- : Fe^2+ = 1 : 5, so n(Fe^2+) = 1.84 x 10^-3 mol. c = 1.84 x 10^-3 / 0.0250 = 0.0736 mol/dm³."),
        SUM("A transition element forms at least one ion with a partly filled d sub-shell; Sc and Zn are not transition elements.",
            "Cr is [Ar] 3d5 4s1 and Cu is [Ar] 3d10 4s1; 4s electrons are lost first when ions form.",
            "Variable oxidation states arise because the 4s and 3d energies are close; Fe^2+ (3d6) oxidizes easily, Mn^2+ (3d5) does not.",
            "Transition metal ions are coloured, catalytic and often paramagnetic.",
            "MnO4^- oxidizes Fe^2+ in the ratio 1 : 5; Cr2O7^2- oxidizes Fe^2+ in the ratio 1 : 6."),
    ])]

# ============================================================================================
# 6. Complex ions and ligands
# ============================================================================================
LESSONS += [lesson(
    module=M_T, topic="Complex ions and ligands",
    title="Complex ions, ligands and naming complexes",
    slug="chu2-complex-ions-ligands", minutes=24,
    summary="A complex ion is a central metal ion bonded to ligands by dative bonds; learn to find the coordination number, oxidation number and charge, to name complexes, and to recognise the usual shapes.",
    objectives=[
        "Define complex ion, ligand and coordination number and describe dative bonding",
        "Classify ligands as monodentate, bidentate or polydentate with examples",
        "Calculate the oxidation number of the metal and the charge of a complex, and name complexes by IUPAC rules",
        "Relate coordination number to shape (octahedral, tetrahedral, square planar, linear) and describe the reactions of aqueous ions with NaOH and ammonia",
    ],
    key_concepts=["Complex ion", "Ligand", "Dative covalent bond", "Coordination number", "Monodentate and bidentate", "Naming complexes"],
    blocks=[
        H("Introduction"),
        T("Copper(II) sulfate crystals are blue because of a complex ion. Haemoglobin in your blood carries oxygen because iron sits in a complex. The chlorophyll that makes cocoa leaves green has magnesium in a similar structure, and the cancer drug cisplatin is a platinum complex. "
          "Transition metal ions are small and highly charged and have empty orbitals, so they attract lone pairs strongly. The result is a **complex ion**."),
        D("A **complex ion** is a central metal ion surrounded by **ligands** bonded to it by dative covalent bonds. A **ligand** is a molecule or ion that donates a lone pair of electrons to the metal ion. The **coordination number** is the number of dative bonds from the ligands to the central metal ion.", title="Definitions"),
        T("The metal ion is a Lewis acid (electron pair acceptor) and the ligand is a Lewis base (electron pair donor). The charge on the complex is the sum of the charge on the metal ion and the charges on the ligands."),
        KEY("Types of ligand", "",
            cards=[["Monodentate (one bond)", "H2O, NH3, Cl^-, CN^-, OH^-. Each has one atom with a lone pair that bonds to the metal."],
                   ["Bidentate (two bonds)", "Ethane-1,2-diamine, H2NCH2CH2NH2 (often written en), and the ethanedioate (oxalate) ion, C2O4^2-. Two donor atoms bond to the same metal."],
                   ["Polydentate (many bonds)", "EDTA^4- is hexadentate (six donor atoms). It wraps round a metal ion and forms very stable chelate complexes."]]),
        T("A complex with a bidentate or polydentate ligand is called a **chelate**. Chelates are more stable than similar complexes with monodentate ligands (the chelate effect), explained in the lesson on stability constants."),
        H("Coordination number, charge and oxidation number"),
        F(r"\text{charge of complex} = \text{oxidation number of metal} + \text{sum of ligand charges}"),
        EX("Worked example 1: oxidation number and coordination number", intro="Find the oxidation number of the metal and the coordination number in [[ [Fe(CN)6]^4- ]] and in [[ [CrCl2(H2O)4]^+ ]].",
           steps=[
               S("[Fe(CN)6]^4-: coordination number", text="Six cyanide ligands, each monodentate: coordination number 6."),
               S("[Fe(CN)6]^4-: oxidation number", math=r"x + 6(-1) = -4 \;\Rightarrow\; x = +2"),
               S("[CrCl2(H2O)4]^+: coordination number", text="Two Cl^- and four H2O, all monodentate: coordination number 6."),
               S("[CrCl2(H2O)4]^+: oxidation number", math=r"x + 2(-1) + 4(0) = +1 \;\Rightarrow\; x = +3"),
           ]),
        H("Shapes"),
        CODE("Coordination number   Shape            Examples\n"
             "2                     linear           [Ag(NH3)2]+\n"
             "4                     tetrahedral      [CuCl4]2-, [CoCl4]2-, [Zn(OH)4]2-\n"
             "4                     square planar    [Pt(NH3)2Cl2], [Ni(CN)4]2-\n"
             "6                     octahedral       [Cu(H2O)6]2+, [Fe(CN)6]3-, [Co(NH3)6]3+", "text",
             title="Shapes of complexes"),
        T("Large ligands such as Cl^- tend to give tetrahedral four-coordinate complexes; small ligands such as H2O and NH3 usually give six-coordinate octahedral complexes. Bond angles: 90° and 180° in octahedral and square planar complexes, about 109.5° in tetrahedral complexes."),
        H("Naming complexes (IUPAC)"),
        KEY("Rules", "",
            cards=[["1. Ligands first, in alphabetical order", "Prefix with di-, tri-, tetra-, penta-, hexa- (ignored for alphabetical order). Use bis-, tris- if the ligand name already contains a number."],
                   ["2. Ligand names", "H2O aqua; NH3 ammine; Cl^- chlorido (older: chloro); CN^- cyanido (cyano); OH^- hydroxido (hydroxo); C2O4^2- oxalato; en ethane-1,2-diamine."],
                   ["3. Then the metal with its oxidation number", "Roman numeral in brackets. If the complex is a negative ion the metal name ends in -ate (ferrate for iron, cuprate for copper, argentate for silver)."]]),
        CODE("[Cu(H2O)6]2+        hexaaquacopper(II)\n"
             "[Cu(NH3)4(H2O)2]2+ tetraamminediaquacopper(II)\n"
             "[Ag(NH3)2]+        diamminesilver(I)\n"
             "[Fe(CN)6]4-        hexacyanidoferrate(II)\n"
             "[Fe(CN)6]3-        hexacyanidoferrate(III)\n"
             "[CoCl4]2-          tetrachloridocobaltate(II)\n"
             "[Pt(NH3)2Cl2]      diamminedichloridoplatinum(II)\n"
             "[Ni(en)3]2+        tris(ethane-1,2-diamine)nickel(II)", "text", title="Examples (older names use chloro and cyano; check which your textbook uses)"),
        H("Reactions of aqueous ions with sodium hydroxide and ammonia"),
        T("Solutions of transition metal salts contain hydrated ions such as [[ [Cu(H2O)6]^2+ ]] (blue), [[ [Fe(H2O)6]^2+ ]] (pale green), [[ [Fe(H2O)6]^3+ ]] (yellow-brown), [[ [Ni(H2O)6]^2+ ]] (green) and [[ [Cr(H2O)6]^3+ ]] (green or violet). Adding a little sodium hydroxide or ammonia removes protons from the water ligands and gives an insoluble hydroxide. In excess reagent, some precipitates dissolve because the ligands change."),
        CODE("Ion     Add NaOH(aq)                         In excess NaOH    In excess NH3(aq)\n"
             "Cu2+    pale blue ppt                         insoluble         dissolves: deep blue solution\n"
             "Fe2+    green ppt, turns brown in air         insoluble         insoluble\n"
             "Fe3+    red-brown ppt                         insoluble         insoluble\n"
             "Ni2+    green ppt                             insoluble         dissolves: blue/violet solution\n"
             "Zn2+    white ppt                             dissolves         dissolves (colourless)\n"
             "Cr3+    green ppt                             dissolves: green  slightly soluble (check your textbook)", "text",
             title="Standard textbook observations (Paper 3 skills)"),
        F(r"<<Cu^2+ + 2OH^- -> Cu(OH)2>>"),
        F(r"<<[Cu(H2O)6]^2+ + 4NH3 -> [Cu(NH3)4(H2O)2]^2+ + 4H2O>>"),
        F(r"<<Zn(OH)2 + 2OH^- -> [Zn(OH)4]^2->>"),
        MISTAKE("Counting the number of ligands instead of the number of bonds", "The coordination number counts dative bonds. [Ni(en)3]^2+ has three ligands but coordination number 6, because each en is bidentate."),
        MISTAKE("Forgetting the -ate ending in negative complexes", "[Fe(CN)6]^4- is hexacyanidoferrate(II), not hexacyanidoiron(II). In the formula, write the ligands first, in alphabetical order of their names."),
        TIP("The Board's 2023 report lists determining coordination and oxidation number, naming complexes and complex ion formation among the Paper 1 concepts tested. In Paper 3 the reactions of cations with sodium hydroxide and ammonia are routine.", title="Exam link"),
        QUIZ("What is the coordination number of the metal ion in [[ [Cu(NH3)4(H2O)2]^2+ ]]?", ["2", "4", "6", "8"], 2,
             "Four NH3 and two H2O ligands, all monodentate, give six dative bonds.",
             hint="Add all the monodentate ligands.",
             feedback=["There are more than two ligands.", "Only the ammonia molecules are counted here; the water ligands also bond.", "", "There are six ligands, not eight."]),
        QUIZ("What is the name of [[ [Fe(CN)6]^3- ]]?", ["Hexacyanidoiron(III)", "Hexacyanidoferrate(III)", "Hexacyanidoferrate(II)", "Iron(III) cyanide"], 1,
             "The complex is a negative ion, so the metal name takes -ate. The oxidation number is x + 6(-1) = -3, so x = +3.",
             hint="Work out the oxidation number and decide whether the complex is a cation or an anion.",
             feedback=["A negative complex takes the -ate ending.", "", "Check the charge: iron is +3 here, not +2.", "This is not the IUPAC name of a complex ion."]),
        PQ("Define the terms ligand and coordination number and give the coordination number of [[ [Ni(en)3]^2+ ]] where en is ethane-1,2-diamine.",
           "A ligand is a molecule or ion that donates a lone pair of electrons to a central metal ion to form a dative covalent bond. The coordination number is the number of dative bonds to the central ion. In [Ni(en)3]^2+ each en is bidentate, so the coordination number is 3 x 2 = 6."),
        PQ("Name the complex [[ [Cu(NH3)4(H2O)2]^2+ ]] and state the oxidation number of copper in it.",
           "Tetraamminediaquacopper(II) (ammine before aqua alphabetically). The charge is 2+ and the ligands are neutral, so copper is +2."),
        PQ("Describe what is seen when sodium hydroxide solution is added dropwise to a solution of copper(II) sulfate until in excess, and then ammonia solution is added dropwise to another sample until in excess. Write an ionic equation for the first precipitate.",
           "With NaOH a pale blue precipitate forms that does not dissolve in excess. With ammonia, a pale blue precipitate forms first and then dissolves in excess to give a deep blue solution of [Cu(NH3)4(H2O)2]^2+. Cu^2+ + 2OH^- → Cu(OH)2."),
        PQ("State the shape and approximate bond angle of [[ [CoCl4]^2- ]] and suggest why chloride gives a four-coordinate complex when water gives a six-coordinate one.",
           "Tetrahedral, about 109.5°. Chloride ions are larger than water molecules, so only four can fit round the cobalt ion without too much repulsion between the ligands."),
        SUM("A complex ion has a central metal ion with ligands bonded through dative covalent bonds; the coordination number counts those bonds.",
            "Ligands may be monodentate (H2O, NH3, Cl^-, CN^-), bidentate (en, oxalate) or polydentate (EDTA).",
            "Charge of the complex = oxidation number of the metal + sum of the ligand charges.",
            "Name: ligands (alphabetical) then the metal with its oxidation number; -ate if the complex is negative.",
            "Shapes: 6 octahedral, 4 tetrahedral or square planar, 2 linear."),
    ])]

# ============================================================================================
# 7. Isomerism and colour in complexes
# ============================================================================================
LESSONS += [lesson(
    module=M_T, topic="Isomerism and colour in complexes",
    title="Isomerism in complexes and the origin of colour",
    slug="chu2-complex-isomerism-colour", minutes=24,
    summary="Complexes show cis-trans and optical isomerism; their colours come from d-d transitions between split d orbitals, with the energy gap controlled by the metal ion, its oxidation state, the ligands and the shape.",
    objectives=[
        "Draw and identify cis-trans and optical isomers of octahedral and square planar complexes",
        "Explain the splitting of the 3d orbitals in an octahedral field",
        "Explain why complexes are coloured and use DeltaE = hc/wavelength to link energy gap and colour",
        "Explain how ligand, oxidation state and shape change the colour, and why some ions are colourless",
    ],
    key_concepts=["Cis-trans isomerism", "Optical isomerism in complexes", "d orbital splitting", "d-d transition", "Complementary colour", "Spectrochemical series"],
    blocks=[
        H("Introduction"),
        T("Cisplatin is used in chemotherapy, but its isomer transplatin is not effective. Same atoms, same formula, different arrangement in space, so a different effect on the body. "
          "And why is a solution of copper(II) sulfate blue but zinc sulfate colourless? This lesson answers both questions."),
        H("Geometric (cis-trans) isomerism"),
        D("**Cis-trans isomers** have the same ligands bonded to the same metal ion but arranged differently: the cis isomer has two identical ligands next to each other (90° apart) and the trans isomer has them opposite each other (180° apart).", title="Cis-trans isomerism"),
        CODE("Square planar [Pt(NH3)2Cl2]            Octahedral [Co(NH3)4Cl2]+\n"
             "\n"
             "cis:   H3N     Cl                    cis:  the two Cl are adjacent (90 degrees)\n"
             "         \\   /                       trans: the two Cl are opposite (180 degrees)\n"
             "          Pt\n"
             "         /   \\\n"
             "       H3N     Cl\n"
             "\n"
             "trans: H3N     Cl\n"
             "         \\   /\n"
             "          Pt\n"
             "         /   \\\n"
             "       Cl     NH3", "text", title="Cis and trans isomers"),
        T("The cis isomer has a net dipole (the two Pt-Cl bonds point to the same side) and the trans isomer has none. Tetrahedral complexes do not show cis-trans isomerism, because all the positions are equivalent."),
        H("Optical isomerism"),
        T("A complex shows **optical isomerism** if its mirror image cannot be superimposed on it. Examples are octahedral complexes with three bidentate ligands, such as [[ [Ni(en)3]^2+ ]], and cis-[[ [Co(en)2Cl2]^+ ]] (but not the trans form, which has a plane of symmetry). The two mirror-image forms rotate the plane of polarized light in opposite directions."),
        H("Why complexes are coloured"),
        T("In a free transition metal ion the five 3d orbitals have the same energy. In an octahedral complex the six ligands approach along the x, y and z axes. The two orbitals that point towards the ligands (d_z2 and d_x2-y2, called **e_g**) are repelled more and rise in energy. The three that point between the ligands (d_xy, d_xz, d_yz, called **t_2g**) are repelled less and lie lower. The energy gap is **ΔE** or Δ_oct."),
        IMG("al-chu2-d-splitting.svg", alt="Energy diagram of the five 3d orbitals splitting into three lower t2g orbitals and two higher eg orbitals in an octahedral field, with an electron promoted by absorbing light of energy delta E.",
            caption="Figure 1. Splitting of the 3d orbitals in an octahedral complex and a d-d transition."),
        D("A **d-d transition** occurs when an electron in a lower d orbital absorbs a photon of visible light of energy equal to the gap and moves to a higher d orbital. The light that is **not** absorbed (the complementary colour) is transmitted and is the colour we see.", title="Origin of colour", formula=r"\Delta E = h\nu = \dfrac{hc}{\lambda}"),
        T("Here h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m/s and λ is the wavelength. The complementary colours are opposite on the colour wheel: red absorbed gives blue-green (cyan); orange absorbed gives blue; blue absorbed gives yellow-orange; violet absorbed gives yellow-green."),
        KEY("What changes the colour?", "Anything that changes the size of the gap ΔE changes the wavelength absorbed.",
            cards=[["The ligand", "Strong-field ligands give a larger gap. Spectrochemical series (increasing gap): I^- < Br^- < Cl^- < F^- < OH^- < H2O < NH3 < en < CN^- < CO. Replacing H2O by NH3 in copper(II) shifts the colour from pale blue to deep blue."],
                   ["The oxidation state", "A higher charge on the metal pulls ligands closer, giving a larger gap: Fe^2+ (pale green) and Fe^3+ (yellow-brown) with the same ligands have different colours."],
                   ["The metal ion", "Cr^3+, Mn^2+, Fe^2+ and Cu^2+ have different numbers of d electrons and different gaps."],
                   ["The shape", "Tetrahedral complexes have a smaller gap (about 4/9 of the octahedral value), so [CuCl4]^2- (yellow-green) differs from [Cu(H2O)6]^2+ (blue)."]]),
        T("**Colourless ions.** If the d sub-shell is empty (Sc^3+, 3d0) or full (Zn^2+, Cu^+, 3d10), there is no electron to promote or no empty d orbital to receive it. No d-d transition is possible, so the ions are colourless. The deep purple of MnO4^-, where Mn is +7 (3d0), is not a d-d transition; it arises from charge transfer from oxygen to manganese (check your textbook)."),
        EX("Worked example 1: energy and wavelength", intro="A complex absorbs light of wavelength 600 nm. Calculate the energy gap per ion and per mole. (h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m/s, L = 6.02 x 10^23 /mol)",
           steps=[
               S("Convert the wavelength", math=r"\lambda = 600\ \text{nm} = 6.00 \times 10^{-7}\ \text{m}"),
               S("Energy per ion", math=r"\Delta E = \dfrac{hc}{\lambda} = \dfrac{6.63\times10^{-34} \times 3.00\times10^{8}}{6.00\times10^{-7}} = 3.32 \times 10^{-19}\ \text{J}"),
               S("Energy per mole", math=r"3.32\times10^{-19} \times 6.02\times10^{23} = 2.00 \times 10^{5}\ \text{J/mol} = 200\ \text{kJ/mol}"),
           ]),
        EX("Worked example 2: cis-trans and symmetry", intro="Decide whether [[ [Pt(NH3)2Cl2] ]] and [[ [Pt(NH3)Cl3]^- ]] can each exist as cis-trans isomers.",
           steps=[
               S("[Pt(NH3)2Cl2]", text="Square planar with two NH3 and two Cl. The two Cl can be adjacent (cis) or opposite (trans). Two isomers exist."),
               S("[Pt(NH3)Cl3]^-", text="Square planar with one NH3 and three Cl. Whatever position NH3 takes, the arrangement is the same: NH3 is opposite one Cl and adjacent to the other two. Only one structure exists."),
           ]),
        MISTAKE("Explaining colour as the colour absorbed", "The colour you see is the colour not absorbed, the complementary colour. A complex that absorbs orange-red light looks blue."),
        MISTAKE("Saying the d orbitals split because ligands remove d electrons", "The electrons stay in the metal ion. The ligands' lone pairs repel the electrons in the d orbitals that point at them, raising their energy."),
        TIP("Isomerism of complexes, d-d transitions and the colour of complex ions are Paper 1 and Paper 2 material (the Board's 2023 report lists the identification of geometric isomers and the formation of complex ions). Say: the gap is ΔE, the wavelength absorbed depends on it, and the complementary colour is seen.", title="Exam link"),
        QUIZ("Why is a solution of zinc sulfate colourless?", ["Zinc has no d electrons", "Zn^2+ has a full 3d sub-shell, so no d-d transition is possible", "Zinc ions absorb all light", "Zinc sulfate is not ionic"], 1,
             "A d-d transition needs an empty or half-empty d orbital to receive the promoted electron. Zn^2+ is 3d10.",
             hint="Write the configuration of Zn^2+.",
             feedback=["Zn^2+ has ten d electrons.", "", "If it absorbed all light it would look black, not colourless.", "Zinc sulfate is ionic."]),
        QUIZ("A complex absorbs strongly in the orange-red region. What colour does it appear?", ["Orange", "Red", "Blue-green", "Colourless"], 2,
             "Blue-green is the complementary colour of orange-red.",
             hint="Use the colour wheel: the seen colour is opposite the absorbed one.",
             feedback=["The absorbed colour is not the one seen.", "Red is absorbed.", "", "A complex that absorbs visible light is coloured."]),
        PQ("Explain why [[ [Cu(H2O)6]^2+ ]] is blue.",
           "In the octahedral complex the 3d orbitals split into a lower t2g set and a higher eg set. Cu^2+ is 3d9, so there is a vacancy in the eg set. Orange-red visible light of energy equal to the gap is absorbed and an electron is promoted from t2g to eg (d-d transition). The remaining light, the complementary colour, is blue."),
        PQ("A complex ion absorbs light of wavelength 500 nm. Calculate the energy gap in kJ/mol. (h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m/s, L = 6.02 x 10^23 /mol)",
           "E = hc/λ = (6.63 x 10^-34 x 3.00 x 10^8) / (5.00 x 10^-7) = 3.98 x 10^-19 J per ion. Per mole: 3.98 x 10^-19 x 6.02 x 10^23 = 2.40 x 10^5 J/mol = 240 kJ/mol."),
        PQ("Draw (describe) the cis and trans isomers of [[ [Pt(NH3)2Cl2] ]] and state which is polar.",
           "Both are square planar. In the cis isomer the two NH3 are adjacent and the two Cl are adjacent (90°). In the trans isomer the two NH3 are opposite each other and the two Cl are opposite each other (180°). The cis isomer is polar because the bond dipoles do not cancel; the trans isomer is non-polar."),
        PQ("Suggest why replacing the water ligands in [[ [Cu(H2O)6]^2+ ]] with ammonia changes the colour from pale blue to deep blue.",
           "Ammonia is a stronger-field ligand than water (higher in the spectrochemical series), so the d orbital splitting ΔE is larger. The complex absorbs light of higher energy (shorter wavelength), so the colour seen changes to a deeper blue."),
        SUM("Cis-trans isomerism occurs in square planar and octahedral complexes; optical isomerism occurs in complexes such as [Ni(en)3]^2+ and cis-[Co(en)2Cl2]^+.",
            "In an octahedral field the 3d orbitals split into a lower t2g set (3) and a higher eg set (2).",
            "A d-d transition absorbs light of energy ΔE = hc/λ; the colour seen is the complementary colour.",
            "Ligand, oxidation state, metal ion and shape alter ΔE and hence the colour; spectrochemical series I^- < Cl^- < H2O < NH3 < CN^-.",
            "Ions with 3d0 or 3d10 configurations are colourless."),
    ])]

# ============================================================================================
# 8. Ligand exchange and stability constants
# ============================================================================================
LESSONS += [lesson(
    module=M_T, topic="Ligand exchange and stability constants",
    title="Ligand exchange, stability constants and the chelate effect",
    slug="chu2-ligand-exchange-stability", minutes=24,
    summary="Ligands in a complex can be replaced by others; the stability constant Kstab shows how far the complex forms, and chelate complexes are extra stable because of the entropy increase.",
    objectives=[
        "Describe ligand exchange reactions with their colour changes and write the equations",
        "Write the expression for a stability constant and use it to compare and calculate",
        "Explain the chelate effect in terms of entropy",
        "Apply stability constants to the dissolving of silver halides, EDTA titrations and carbon monoxide poisoning",
    ],
    key_concepts=["Ligand exchange", "Stability constant Kstab", "Chelate effect", "EDTA titration", "Competition between ligands", "Entropy"],
    blocks=[
        H("Introduction"),
        T("Photographers once fixed black-and-white film by dissolving unused silver bromide in a solution called hypo, and some studios in Cameroon still use this method. A water-treatment laboratory in Douala checks hardness by titrating with EDTA. "
          "Doctors treat metal poisoning with chelating agents. All of these use **ligand exchange**: one ligand takes the place of another on a metal ion."),
        H("Ligand exchange"),
        D("**Ligand exchange** (substitution) is a reaction in which one or more ligands in a complex are replaced by other ligands. The coordination number may stay the same or change.", title="Ligand exchange"),
        F(r"<<[Cu(H2O)6]^2+ + 4NH3 <=> [Cu(NH3)4(H2O)2]^2+ + 4H2O>>"),
        F(r"<<[Cu(H2O)6]^2+ + 4Cl^- <=> [CuCl4]^2- + 6H2O>>"),
        F(r"<<[Co(H2O)6]^2+ + 4Cl^- <=> [CoCl4]^2- + 6H2O>>"),
        T("In the second and third reactions the coordination number falls from 6 to 4 because chloride ions are larger than water molecules. [[ [Cu(H2O)6]^2+ ]] is blue and [[ [CuCl4]^2- ]] is yellow-green; adding concentrated hydrochloric acid to copper(II) sulfate gives a green mixture. [[ [Co(H2O)6]^2+ ]] is pink and [[ [CoCl4]^2- ]] is blue. The change is reversible; adding water, or cooling, moves the equilibrium back to the pink complex."),
        T("When water is replaced by ammonia the coordination number and shape stay the same, but the complex changes colour: the ligand is stronger, so the d orbital gap changes (previous lesson)."),
        H("Stability constants"),
        T("The formation of a complex is an equilibrium. For metal ion M^n+ and ligand L forming ML4 (water ligands omitted, because water is the solvent):"),
        F(r"\mathrm{M^{n+} + 4L \rightleftharpoons ML_4^{n+}} \qquad K_{stab} = \dfrac{[\mathrm{ML_4^{n+}}]}{[\mathrm{M^{n+}}][\mathrm{L}]^4}"),
        D("The **stability constant**, K_stab, is the equilibrium constant for the formation of a complex ion from the metal ion and its ligands in solution. **The larger K_stab, the more stable the complex** and the further the equilibrium lies towards the complex. Its units depend on the expression (for the equation above, mol^-4 dm^12).", title="Stability constant"),
        CODE("Complex                   K_stab (approximate)       log K\n"
             "[Ag(NH3)2]+               1.6 x 10^7  mol-2 dm6      7.2\n"
             "[Cu(NH3)4(H2O)2]2+        about 10^13 mol-4 dm12     about 13\n"
             "[Ag(S2O3)2]3-             about 10^13 mol-2 dm6      about 13\n"
             "[Ag(CN)2]-                about 10^20 mol-2 dm6      about 20\n"
             "[Fe(CN)6]4-               very large                 -", "text",
             title="Approximate values (published values differ; check your textbook)"),
        T("When two ligands compete for the same metal ion, the one that forms the complex with the larger K_stab wins. So ammonia can replace water in copper(II), and cyanide will replace ammonia in the silver complex."),
        H("Silver halides and ammonia"),
        T("AgCl dissolves in dilute ammonia because the complex [[ [Ag(NH3)2]^+ ]] forms and removes silver ions from the equilibrium. AgBr needs concentrated ammonia, and AgI does not dissolve in ammonia at all. The reason: the solubility product falls from AgCl to AgI, so fewer silver ions are available for the ligand to capture."),
        F(r"<<AgCl + 2NH3 <=> [Ag(NH3)2]^+ + Cl^->>"),
        F(r"<<AgBr + 2S2O3^2- -> [Ag(S2O3)2]^3- + Br^->>"),
        T("Thiosulfate has a larger K_stab with silver than ammonia has, so it dissolves AgBr: this is the 'fixing' step of black-and-white photography."),
        H("The chelate effect"),
        T("Complexes with bidentate and polydentate ligands are much more stable than similar complexes with monodentate ligands. This is the **chelate effect**. Compare the replacement of ammonia in a nickel complex by ethane-1,2-diamine (en):"),
        F(r"\mathrm{[Ni(NH_3)_6]^{2+} + 3\,en \rightleftharpoons [Ni(en)_3]^{2+} + 6NH_3}"),
        T("On the left there are 4 particles; on the right there are 7. The **entropy increases**, because more particles means more disorder. The enthalpy change is close to zero (six Ni-N bonds are broken and six Ni-N bonds are made), so ΔG = ΔH - TΔS is negative. The reaction goes to the right, which means [Ni(en)3]^2+ has a much larger K_stab than [Ni(NH3)6]^2+."),
        KEY("EDTA", "EDTA^4- is hexadentate and forms 1 : 1 complexes with most metal ions, including Ca^2+ and Mg^2+. Because it binds so strongly, it can be used to titrate hard water: the endpoint is shown by an indicator that changes colour when no free metal ions remain."),
        H("Carbon monoxide poisoning"),
        T("In haemoglobin an iron(II) ion in a haem group binds oxygen as a ligand. Carbon monoxide forms a much more stable complex with the iron than oxygen does, so CO displaces O2 and the blood can no longer carry oxygen. Poorly ventilated charcoal stoves can cause this, which is why cooking indoors with a closed door is dangerous."),
        EX("Worked example 1: calculating K_stab", intro="At equilibrium a solution contains [Ag(NH3)2]^+ at 0.050 mol/dm³, Ag^+ at 1.0 x 10^-9 mol/dm³ and NH3 at 0.20 mol/dm³. Write the expression for K_stab and calculate its value with units.",
           steps=[
               S("Equation", math=r"<<Ag^+ + 2NH3 <=> [Ag(NH3)2]^+>>"),
               S("Expression", math=r"K_{stab} = \dfrac{[\mathrm{[Ag(NH_3)_2]^+}]}{[\mathrm{Ag^+}][\mathrm{NH_3}]^2}"),
               S("Substitute", math=r"K_{stab} = \dfrac{0.050}{(1.0\times10^{-9})(0.20)^2} = 1.25 \times 10^{9}"),
               S("Units", text="mol^-2 dm^6. The large value shows the complex is very stable."),
           ]),
        EX("Worked example 2: EDTA and hard water", intro="25.0 cm³ of hard water needs 12.50 cm³ of 0.0100 mol/dm³ EDTA. EDTA reacts 1 : 1 with Ca^2+. Find the Ca^2+ concentration and express the hardness as g of CaCO3 per dm³ (Mr = 100).",
           steps=[
               S("Moles of EDTA", math=r"0.0100 \times 0.01250 = 1.25 \times 10^{-4}\ \text{mol}"),
               S("Moles of Ca^2+", text="1 : 1, so 1.25 x 10^-4 mol in 25.0 cm³."),
               S("Concentration", math=r"\dfrac{1.25\times10^{-4}}{0.0250} = 5.00 \times 10^{-3}\ \text{mol/dm}^3"),
               S("As CaCO3", math=r"5.00\times10^{-3} \times 100 = 0.500\ \text{g/dm}^3"),
           ]),
        MISTAKE("Including water in the K_stab expression", "Water is the solvent in huge excess and its concentration is constant, so water ligands are left out. Also write the ligand concentration to the power of the number of ligands that react."),
        MISTAKE("Explaining the chelate effect by bond strength", "The metal-nitrogen bonds in the two nickel complexes are very similar. The difference is the increase in entropy as three en molecules displace six NH3 molecules."),
        TIP("Ligand exchange appears in Paper 1 and Paper 2 (the Board's 2023 report lists the formation of complex ions) and in Paper 3 qualitative analysis (observing colour changes). Learn at least three exchange reactions with their colours and write 'reversible' for chloride and ammonia exchange.", title="Exam link"),
        QUIZ("What is the expression for K_stab for [[Cu^2+ + 4NH3 <=> [Cu(NH3)4]^2+]]?", [r"$\dfrac{[\mathrm{Cu^{2+}}][\mathrm{NH_3}]^4}{[\mathrm{[Cu(NH_3)_4]^{2+}}]}$", r"$\dfrac{[\mathrm{[Cu(NH_3)_4]^{2+}}]}{[\mathrm{Cu^{2+}}][\mathrm{NH_3}]^4}$", r"$\dfrac{[\mathrm{[Cu(NH_3)_4]^{2+}}]}{[\mathrm{Cu^{2+}}][\mathrm{NH_3}]}$", r"$\dfrac{[\mathrm{[Cu(NH_3)_4]^{2+}}]}{[\mathrm{Cu^{2+}}][\mathrm{NH_3}]^4[\mathrm{H_2O}]^2}$"], 1,
             "K_stab = [product] / ([metal ion][ligand]^coefficient), water omitted.",
             hint="Products on top, reactants below, with the ligand raised to the power 4.",
             feedback=["This is the inverse (a dissociation constant).", "", "The power of 4 is missing.", "Water is not included."]),
        QUIZ("Why is [[ [Ni(en)3]^2+ ]] more stable than [[ [Ni(NH3)6]^2+ ]]?", ["The Ni-N bonds are much stronger", "The reaction increases the entropy because more particles are formed", "Ethane-1,2-diamine is a stronger acid", "The Ni^2+ ion is smaller in the en complex"], 1,
             "Replacing six NH3 by three en releases more free molecules (4 to 7 particles), so the entropy rises and the reaction is favourable.",
             hint="Count the particles on each side.",
             feedback=["The bonds are nearly identical (Ni-N).", "", "Acidity is not the reason.", "The ion is the same."]),
        PQ("Write the equation and state the colour change when concentrated hydrochloric acid is added to aqueous cobalt(II) chloride, and state what is seen when the mixture is diluted.",
           "[Co(H2O)6]^2+ + 4Cl^- ⇌ [CoCl4]^2- + 6H2O. The pink solution turns blue. On dilution with water the equilibrium moves left and the pink colour returns."),
        PQ("Explain why silver bromide dissolves in concentrated ammonia but silver iodide does not.",
           "AgBr(s) ⇌ Ag^+ + Br^- and Ag^+ + 2NH3 ⇌ [Ag(NH3)2]^+. Ammonia removes Ag^+ and shifts the first equilibrium to the right. AgBr has a larger solubility product, so enough Ag^+ is available to be captured by concentrated ammonia. AgI has a much smaller solubility product; the concentration of Ag^+ is too low for ammonia to remove it."),
        PQ("Explain the chelate effect with reference to [[ [Ni(NH3)6]^2+ ]] being converted to [[ [Ni(en)3]^2+ ]].",
           "Three bidentate en ligands replace six monodentate NH3 ligands, so the number of free particles increases from 4 to 7. The entropy of the system rises (ΔS positive). ΔH is almost zero because the same type and number of bonds (six Ni-N) are broken and made, so ΔG = ΔH - TΔS is negative and the en complex is more stable."),
        PQ("A 50.0 cm³ sample of hard water requires 20.00 cm³ of 0.0100 mol/dm³ EDTA. Calculate the concentration of metal ions (calcium and magnesium combined) in the water in mol/dm³.",
           "n(EDTA) = 0.0100 x 0.02000 = 2.00 x 10^-4 mol. EDTA reacts 1 : 1 with the metal ions, so n(M^2+) = 2.00 x 10^-4 mol. c = 2.00 x 10^-4 / 0.0500 = 4.00 x 10^-3 mol/dm³."),
        SUM("Ligand exchange replaces ligands: H2O by NH3 (deep blue), H2O by Cl^- (coordination number 6 to 4); the changes are often reversible.",
            "K_stab = [complex] / ([metal ion][ligand]^n); a larger K_stab means a more stable complex.",
            "Competition: the ligand that gives the larger K_stab wins; thiosulfate and cyanide dissolve silver halides that ammonia cannot.",
            "The chelate effect: polydentate ligands give more stable complexes because the entropy increases.",
            "EDTA gives 1 : 1 complexes and is used to titrate Ca^2+ and Mg^2+."),
    ])]

# ============================================================================================
# 9. Benzene and electrophilic substitution
# ============================================================================================
LESSONS += [lesson(
    module=M_O, topic="Benzene and electrophilic substitution",
    title="Benzene: structure, stability and electrophilic substitution",
    slug="chu2-benzene-electrophilic-substitution", minutes=25,
    summary="Benzene's delocalized ring makes it unusually stable, so it undergoes electrophilic substitution (nitration, halogenation, Friedel-Crafts) rather than addition, and substituents direct the next group to the 2,4- or 3-position.",
    objectives=[
        "Describe the structure of benzene and use bond length and enthalpy of hydrogenation as evidence for delocalization",
        "Describe and explain the mechanism of electrophilic substitution with the reagents and conditions for nitration, halogenation and Friedel-Crafts reactions",
        "Predict the position of substitution from activating and deactivating groups",
        "Plan short syntheses of substituted benzenes",
    ],
    key_concepts=["Delocalization", "Stabilization energy", "Electrophilic substitution", "Nitrating mixture", "Friedel-Crafts", "Directing effects"],
    blocks=[
        H("Introduction"),
        T("Aspirin, paracetamol, many dyes, the explosive TNT, and plastics such as polystyrene are all made from compounds that contain a benzene ring. Benzene is a liquid with a sweet smell, but it is toxic and a carcinogen, so it is handled only with great care. "
          "Understanding why benzene reacts differently from alkenes is the key to this whole module."),
        H("Structure and stability of benzene"),
        T("Benzene, [[C6H6]], is a **planar** ring of six carbon atoms. Each carbon is bonded to two carbon atoms and one hydrogen by sigma bonds (sp2 hybridization, bond angles 120°). Each carbon has one p orbital left over, perpendicular to the ring. The six p orbitals overlap sideways to form a ring of electron density above and below the plane: a **delocalized pi system** of six electrons."),
        KEY("Evidence for delocalization (not three separate C=C bonds)", "",
            cards=[["Bond length", "All the C-C bonds are equal, 0.139 nm, between the C-C single bond (0.154 nm) and the C=C double bond (0.134 nm). Kekule's structure predicts alternating long and short bonds."],
                   ["Enthalpy of hydrogenation", "Cyclohexene (one C=C) releases about -120 kJ/mol. Three C=C bonds would give 3 x (-120) = -360 kJ/mol. Benzene releases only -208 kJ/mol, so it is 152 kJ/mol more stable than expected. This is the **stabilization energy** (delocalization energy)."],
                   ["Chemical behaviour", "Benzene does not decolourize bromine water and does not react like an alkene; it prefers substitution, which keeps the delocalized ring."]]),
        H("Why substitution and not addition"),
        T("Adding to benzene would destroy the delocalized ring and lose the 152 kJ/mol of stabilization. Substitution keeps the ring. The ring is rich in electrons, so the attacking species is an **electrophile** (an electron-pair acceptor). The reaction is **electrophilic substitution**."),
        D("**Electrophilic substitution** of benzene: (1) The electrophile E^+ attacks the delocalized pi electrons, forming a carbocation intermediate in which the ring is no longer fully delocalized. (2) The intermediate loses H^+ from the carbon that was attacked, restoring the stable aromatic ring.", title="Mechanism"),
        CODE("C6H6 + E+  ->  [C6H6E]+ (intermediate, positive charge spread over 5 carbons)\n"
             "[C6H6E]+  ->  C6H5E + H+       (aromatic ring restored)\n"
             "The catalyst is regenerated when H+ combines with the catalyst anion.", "text", title="Mechanism in outline (draw curly arrows in the exam)"),
        H("Reactions of benzene"),
        KEY("Nitration", "Concentrated nitric acid with concentrated sulfuric acid (the nitrating mixture), at 50-55 °C. The electrophile is the nitronium ion, NO2^+.",
            cards=[["Generating the electrophile", "Sulfuric acid protonates nitric acid: HNO3 + 2H2SO4 -> NO2^+ + H3O^+ + 2HSO4^-."],
                   ["Product", "Nitrobenzene, a pale yellow oily liquid with an almond smell. Above 55 °C more nitro groups enter (1,3-dinitrobenzene)."]]),
        F(r"<<HNO3 + 2H2SO4 -> NO2^+ + H3O^+ + 2HSO4^->>"),
        F(r"<<C6H6 + HNO3 -> C6H5NO2 + H2O>>"),
        KEY("Halogenation", "Chlorine or bromine with a halogen carrier (anhydrous iron(III) bromide or aluminium chloride, or iron filings) at room temperature in the dark. No UV light: UV would cause a free radical addition instead.",
            cards=[["Generating the electrophile", "Br2 + FeBr3 -> Br^+ FeBr4^- (the polarized complex acts as Br^+)."],
                   ["Product", "Bromobenzene and HBr. Benzene does not decolourize bromine water without the catalyst."]]),
        F(r"<<C6H6 + Br2 -> C6H5Br + HBr>>"),
        KEY("Friedel-Crafts reactions", "Anhydrous aluminium chloride as catalyst, under dry conditions.",
            cards=[["Alkylation", "CH3Cl / AlCl3 gives methylbenzene. The electrophile is the carbocation CH3^+ (from CH3Cl + AlCl3)."],
                   ["Acylation", "CH3COCl / AlCl3 gives phenylethanone. The electrophile is the acylium ion, CH3CO^+. This route to ketones is tested in the Board's papers."]]),
        F(r"<<C6H6 + CH3Cl -> C6H5CH3 + HCl>>"),
        F(r"<<C6H6 + CH3COCl -> C6H5COCH3 + HCl>>"),
        T("Benzene can also be hydrogenated with hydrogen and a nickel catalyst at about 150 °C and high pressure: [[C6H6 + 3H2 -> C6H12]] (cyclohexane). This addition needs harsher conditions than for alkenes because the ring must lose its delocalization."),
        H("Directing effects of substituents"),
        T("A group already on the ring decides where the next group enters, and how fast the reaction is."),
        CODE("Group                      Effect on rate        Directs next group to\n"
             "-OH, -NH2, -OCH3, -CH3     activating            2- and 4- positions (ortho/para)\n"
             "-Cl, -Br (halogens)        slightly deactivating  2- and 4-\n"
             "-NO2, -COOH, -CHO, -COR    deactivating          3- position (meta)", "text", title="Directing effects"),
        T("Activating groups push electron density into the ring (by donation of a lone pair or by the inductive effect), stabilizing the carbocation intermediate. Deactivating groups withdraw electrons from the ring. This is why methylbenzene reacts faster than benzene, and nitrobenzene slower. Phenol and phenylamine are so activated that they react with bromine water without a catalyst (next lessons)."),
        H("Planning a synthesis"),
        T("The order of reactions matters because of the directing effects. To make 4-nitrobenzoic acid, nitrate methylbenzene first (the methyl group directs to 2- and 4-; separate the 4-isomer) and then oxidize the CH3 to COOH with hot alkaline potassium manganate(VII). If you oxidize first, the COOH group would direct the nitro group to the 3-position and give 3-nitrobenzoic acid."),
        EX("Worked example 1: yield", intro="7.80 g of benzene (Mr = 78) is nitrated and 8.60 g of nitrobenzene (Mr = 123) is obtained. Calculate the percentage yield.",
           steps=[
               S("Moles of benzene", math=r"\dfrac{7.80}{78} = 0.100\ \text{mol}"),
               S("Theoretical mass of nitrobenzene", text="The ratio is 1 : 1, so 0.100 mol x 123 = 12.3 g."),
               S("Percentage yield", math=r"\dfrac{8.60}{12.3} \times 100 = 69.9\%"),
           ]),
        EX("Worked example 2: predicting the product", intro="Predict the main product(s) of mononitration of methylbenzene and of nitrobenzene, using the nitrating mixture.",
           steps=[
               S("Methylbenzene", text="The methyl group is activating and directs to the 2- and 4-positions: 2-nitromethylbenzene and 4-nitromethylbenzene (and the reaction is faster than for benzene)."),
               S("Nitrobenzene", text="The nitro group is deactivating and directs to the 3-position: 1,3-dinitrobenzene, which needs hotter, stronger conditions."),
           ]),
        MISTAKE("Using UV light for the bromination of benzene", "Substitution in the ring needs a halogen carrier (FeBr3 or Fe) in the dark. UV light makes radicals and gives an addition product or, for methylbenzene, substitution in the side chain."),
        MISTAKE("Saying benzene has alternating single and double bonds", "All six C-C bonds are the same length (0.139 nm). Kekule's drawing is a model only; the pi electrons are delocalized above and below the ring."),
        TIP("The Board's 2023 report lists the bromination of benzene in Paper 1 and the products of phenylethanone in Paper 2, where candidates found structures and mechanisms difficult. Learn the reagents, the conditions and the electrophile for each reaction, and practise drawing the mechanism with curly arrows.", title="Exam link"),
        QUIZ("Which reagents convert benzene to nitrobenzene?", ["Dilute nitric acid at room temperature", "Concentrated nitric acid and concentrated sulfuric acid at 50-55 °C", "Nitrogen dioxide and UV light", "Concentrated nitric acid alone at 100 °C"], 1,
             "The nitrating mixture produces the electrophile NO2^+; the temperature is kept below about 55 °C to prevent more than one nitro group entering.",
             hint="Which acid helps to make the nitronium ion?",
             feedback=["Dilute acid does not give a high enough concentration of NO2^+.", "", "UV light is for free-radical reactions.", "Without sulfuric acid there is not enough NO2^+, and a high temperature gives dinitration."]),
        QUIZ("Which group directs a second substituent to the 3-position?", [r"$-\mathrm{OH}$", r"$-\mathrm{CH_3}$", r"$-\mathrm{NO_2}$", r"$-\mathrm{NH_2}$"], 2,
             "The nitro group withdraws electrons and is 3-directing and deactivating.",
             hint="Which group removes electron density from the ring?",
             feedback=["-OH is activating and 2,4-directing.", "-CH3 is activating and 2,4-directing.", "", "-NH2 is activating and 2,4-directing."]),
        PQ("Use the enthalpy changes of hydrogenation of cyclohexene (-120 kJ/mol) and benzene (-208 kJ/mol) to calculate the stabilization energy of benzene. What does it show?",
           "Three C=C bonds would give 3 x (-120) = -360 kJ/mol. Actual = -208 kJ/mol. Stabilization energy = 360 - 208 = 152 kJ/mol. Benzene is more stable than the Kekule structure with three isolated C=C bonds, because its six pi electrons are delocalized."),
        PQ("Describe the mechanism of the bromination of benzene using bromine and iron(III) bromide. Why is this a substitution and not an addition?",
           "Br2 reacts with FeBr3 to give a polarized complex that behaves as the electrophile Br^+ (Br2 + FeBr3 -> Br^+ FeBr4^-). The Br^+ attacks the pi electrons of the ring to form a carbocation intermediate. The intermediate loses H^+ (which combines with FeBr4^- to give HBr and regenerate FeBr3), restoring the aromatic ring and giving bromobenzene. Substitution keeps the delocalized ring and its 152 kJ/mol stabilization; addition would destroy it."),
        PQ("Starting from benzene, give the reagents and conditions for a three-step synthesis of 3-nitrobenzoic acid: (a) benzene to methylbenzene, (b) methylbenzene to benzoic acid, (c) benzoic acid to 3-nitrobenzoic acid.",
           "(a) CH3Cl with anhydrous AlCl3 (Friedel-Crafts alkylation). (b) Hot alkaline potassium manganate(VII), then acidify (side-chain oxidation). (c) Concentrated HNO3 and concentrated H2SO4 at 50-55 °C; the COOH group is deactivating and 3-directing."),
        PQ("Benzene reacts with ethanoyl chloride in the presence of aluminium chloride. Name the reaction and the product and write an equation.",
           "Friedel-Crafts acylation; the product is phenylethanone. C6H6 + CH3COCl → C6H5COCH3 + HCl (the electrophile is the ethanoylium ion CH3CO^+)."),
        SUM("Benzene is planar with delocalized pi electrons; C-C bonds are 0.139 nm; stabilization energy is 152 kJ/mol.",
            "Benzene undergoes electrophilic substitution to keep the delocalized ring: attack by E^+, carbocation intermediate, loss of H^+.",
            "Nitration: conc. HNO3 / conc. H2SO4, 50-55 °C (NO2^+). Halogenation: Br2 / FeBr3 in the dark. Friedel-Crafts: RCl or RCOCl / AlCl3.",
            "Activating groups (-OH, -NH2, -CH3) direct to the 2,4-positions; deactivating groups (-NO2, -COOH) direct to the 3-position.",
            "The order of steps in a synthesis depends on the directing effects."),
    ])]

# ============================================================================================
# 10. Phenols
# ============================================================================================
LESSONS += [lesson(
    module=M_O, topic="Phenols",
    title="Phenols: acidity, ring reactions and tests",
    slug="chu2-phenols", minutes=22,
    summary="Phenol is a weak acid, stronger than alcohols because its anion is stabilized by delocalization, and its ring is so activated that it reacts with bromine water and dilute nitric acid without a catalyst.",
    objectives=[
        "Compare the acidity of alcohols, phenol and carboxylic acids and explain the order",
        "Describe the reactions of phenol with sodium, sodium hydroxide, acyl chlorides and bromine, with equations",
        "Explain why the ring in phenol is more reactive than in benzene",
        "Distinguish phenols from alcohols and carboxylic acids using chemical tests",
    ],
    key_concepts=["Phenol structure", "Acidity of phenol", "Phenoxide delocalization", "Activated ring", "Neutral iron(III) chloride test", "2,4,6-tribromophenol"],
    blocks=[
        H("Introduction"),
        T("Disinfectants such as TCP, some mouthwashes and the resin in Bakelite handles and electrical fittings all come from phenol, C6H5OH. Phenol was one of the first antiseptics used in surgery. It is a colourless solid that turns pink on standing and burns the skin, so it must be handled with care. "
          "In phenol the -OH group is attached directly to a benzene ring. This one change makes its chemistry quite different from that of alcohols."),
        D("A **phenol** is a compound in which a hydroxyl group is bonded directly to a carbon atom of a benzene ring. The simplest is phenol, [[C6H5OH]].", title="Phenol"),
        H("Acidity of phenol"),
        T("Phenol is a weak acid: it partly ionizes in water to give the phenoxide ion, [[C6H5O^-]]."),
        F(r"<<C6H5OH <=> C6H5O^- + H^+>>"),
        T("The negative charge on the oxygen of the phenoxide ion is **delocalized** into the benzene ring, because a lone pair on oxygen overlaps with the pi system. Spreading the charge makes the ion more stable, so phenol loses H^+ more easily than an alcohol. In an alkoxide ion, [[C2H5O^-]], the charge stays on oxygen and the ethyl group pushes electrons towards it, making it less stable."),
        CODE("Compound         Approximate pKa     Reacts with\n"
             "ethanol          16                  Na only\n"
             "water            15.7                Na\n"
             "phenol           10                  Na and NaOH (not Na2CO3)\n"
             "ethanoic acid    4.8                 Na, NaOH and Na2CO3 (gives CO2)", "text",
             title="Acid strength order (a smaller pKa means a stronger acid)"),
        T("The order of acid strength is **alcohols < phenol < carboxylic acids**. Phenol is too weak to release carbon dioxide from carbonates, which is how it is distinguished from a carboxylic acid. Electron-withdrawing groups on the ring, such as -NO2, increase the acidity (2,4,6-trinitrophenol, picric acid, is a strong acid)."),
        F(r"<<2C6H5OH + 2Na -> 2C6H5ONa + H2>>"),
        F(r"<<C6H5OH + NaOH -> C6H5ONa + H2O>>"),
        T("The first reaction needs sodium metal and releases hydrogen; the second occurs with aqueous sodium hydroxide, where the solid phenol dissolves to give a clear solution of sodium phenoxide. Alcohols do not react with aqueous sodium hydroxide."),
        H("Reactions of the ring"),
        T("The lone pair on the oxygen atom is partly delocalized into the ring, which makes the ring **much more electron-rich** than that of benzene. The -OH group is an activating, 2,4-directing group. Phenol therefore reacts with electrophiles under mild conditions, and without a catalyst."),
        KEY("Bromine water", "Aqueous bromine at room temperature, no catalyst.",
            cards=[["Observation", "The orange bromine water is decolourized and a white precipitate of 2,4,6-tribromophenol forms immediately (with a smell of antiseptic)."],
                   ["Why no catalyst", "The activated ring polarizes bromine strongly enough. All three positions (2, 4 and 6) are substituted."]]),
        F(r"<<C6H5OH + 3Br2 -> C6H2Br3OH + 3HBr>>"),
        KEY("Nitration", "Dilute nitric acid at room temperature gives a mixture of 2-nitrophenol and 4-nitrophenol. Concentrated nitric acid gives 2,4,6-trinitrophenol (picric acid), but violent oxidation can also occur.",
            cards=[["Compare with benzene", "Benzene needs concentrated nitric and sulfuric acids at 50-55 °C. Phenol reacts with dilute nitric acid."]]),
        H("Esters of phenol and azo coupling"),
        T("Phenol does not form an ester with a carboxylic acid directly, because it is a poor nucleophile. It reacts with an **acyl chloride** instead (or an acid anhydride):"),
        F(r"<<C6H5OH + CH3COCl -> CH3COOC6H5 + HCl>>"),
        T("The product is phenyl ethanoate. In the lesson on amines and diazonium salts you will see that phenol, dissolved in sodium hydroxide, couples with a benzenediazonium salt at 0-5 °C to give a bright orange-red **azo dye**."),
        H("Tests for phenol"),
        KEY("Distinguishing phenol, an alcohol and a carboxylic acid", "",
            cards=[["Neutral iron(III) chloride", "A few drops of aqueous FeCl3 give a violet (purple) colour with phenol. Alcohols and carboxylic acids give no violet colour (the carboxylic acid gives a different colour that depends on the acid; check your textbook)."],
                   ["Sodium carbonate", "A carboxylic acid gives carbon dioxide (effervescence); phenol and alcohols do not."],
                   ["Bromine water", "Phenol gives a white precipitate immediately; alcohols do not."]]),
        EX("Worked example 1: mass of product", intro="0.940 g of phenol (Mr = 94) reacts with excess bromine water to form 2,4,6-tribromophenol (Mr = 331). Calculate the maximum mass of product.",
           steps=[
               S("Equation", math=r"<<C6H5OH + 3Br2 -> C6H2Br3OH + 3HBr>>"),
               S("Moles of phenol", math=r"\dfrac{0.940}{94} = 0.0100\ \text{mol}"),
               S("Moles of product", text="1 : 1, so 0.0100 mol."),
               S("Mass", math=r"0.0100 \times 331 = 3.31\ \text{g}"),
           ]),
        EX("Worked example 2: telling three liquids apart", intro="Three colourless liquids in unlabelled bottles are ethanol, phenol (solution) and ethanoic acid. Design a short test scheme.",
           steps=[
               S("Test 1: add sodium carbonate", text="Effervescence means ethanoic acid (CO2 given off)."),
               S("Test 2: add neutral iron(III) chloride to the other two", text="A violet colour means phenol."),
               S("Conclude", text="The remaining liquid, which gives no reaction with either test, is ethanol."),
           ]),
        MISTAKE("Saying phenol reacts like an alcohol with NaOH", "Alcohols are not acidic enough to react with aqueous sodium hydroxide; phenol is. The difference is due to delocalization of charge in the phenoxide ion."),
        MISTAKE("Using a catalyst for the bromination of phenol", "Phenol reacts with bromine water without any catalyst, giving three substitutions at once. Benzene needs FeBr3 and gives only one bromine."),
        TIP("The Board's 2023 report lists the distinguishing test between alcohols and phenols in Paper 1 and the classes of alcohols in Paper 1. Name the reagent, the observation and the inference: 'neutral FeCl3, violet colour, phenol present'.", title="Exam link"),
        QUIZ("Which reagent gives a violet colour with phenol?", ["Acidified potassium dichromate(VI)", "Neutral iron(III) chloride solution", "Sodium carbonate", "2,4-DNPH"], 1,
             "Iron(III) ions form a violet complex with phenol.",
             hint="This is the standard colour test for a phenol.",
             feedback=["That oxidizes alcohols and aldehydes.", "", "That detects acids by effervescence.", "That detects aldehydes and ketones."]),
        QUIZ("Why is phenol a stronger acid than ethanol?", ["Phenol has a higher molar mass", "The phenoxide ion is stabilized by delocalization of its charge into the ring", "Phenol contains oxygen and ethanol does not", "Phenol has a stronger O-H bond"], 1,
             "The negative charge on phenoxide is delocalized into the benzene ring, which stabilizes the anion and favours ionization.",
             hint="Compare the stability of the two anions.",
             feedback=["Molar mass does not decide acidity.", "", "Both contain oxygen.", "A stronger O-H bond would make it less acidic."]),
        PQ("Explain why phenol reacts with aqueous sodium hydroxide but ethanol does not.",
           "Phenol is a stronger acid than ethanol: the phenoxide ion formed on losing H^+ is stabilized because the negative charge is delocalized into the benzene ring. Phenol therefore reacts with NaOH: C6H5OH + NaOH → C6H5ONa + H2O. The ethoxide ion has its charge localized on oxygen (and the electron-releasing ethyl group destabilizes it), so ethanol is too weak an acid to react with aqueous NaOH."),
        PQ("Describe what you would see when excess bromine water is added to aqueous phenol. Write an equation and explain why no catalyst is needed.",
           "The orange colour of the bromine water disappears and a white precipitate of 2,4,6-tribromophenol forms. C6H5OH + 3Br2 → C6H2Br3OH + 3HBr. The lone pair on oxygen is delocalized into the ring, activating it so strongly towards electrophiles that bromine reacts without a halogen carrier."),
        PQ("Compound X, C6H5OH, and compound Y, C6H5CH2OH, are both colourless. Describe two tests to tell them apart and state the results.",
           "(i) Add neutral FeCl3 solution: X gives a violet colour; Y gives none. (ii) Add bromine water: X decolourizes it and gives a white precipitate; Y does not. (Also, X reacts with aqueous NaOH to dissolve; Y does not.)"),
        PQ("Phenol (1.88 g, Mr = 94) is converted to 2,4,6-tribromophenol (Mr = 331). Calculate the mass of product if the yield is 80.0%.",
           "n(phenol) = 1.88 / 94 = 0.0200 mol. Theoretical mass of product = 0.0200 x 331 = 6.62 g. Actual = 0.800 x 6.62 = 5.30 g."),
        SUM("Phenol is a weak acid (pKa about 10): stronger than alcohols, weaker than carboxylic acids; it reacts with Na and NaOH but not with carbonates.",
            "The phenoxide ion is stabilized because its charge is delocalized into the ring.",
            "The -OH group activates the ring: phenol gives 2,4,6-tribromophenol with bromine water and nitrophenols with dilute nitric acid.",
            "Test for a phenol: neutral FeCl3 gives a violet colour.",
            "Phenyl esters are made from acyl chlorides; phenol couples with diazonium salts to make azo dyes."),
    ])]

# ============================================================================================
# 11. Aldehydes and ketones
# ============================================================================================
LESSONS += [lesson(
    module=M_O, topic="Aldehydes and ketones",
    title="Aldehydes and ketones: nucleophilic addition and tests",
    slug="chu2-aldehydes-ketones", minutes=25,
    summary="The polar C=O group is attacked by nucleophiles; aldehydes and ketones add HCN and hydride, form orange precipitates with 2,4-DNPH, and are told apart by Tollens', Fehling's and the iodoform tests.",
    objectives=[
        "Explain the polarity of C=O and why carbonyl compounds undergo nucleophilic addition",
        "Describe and write the mechanism for the addition of HCN, and explain why a racemic mixture forms",
        "Describe the reduction with NaBH4 and the condensation with 2,4-DNPH",
        "Use Tollens', Fehling's, acidified dichromate and iodoform tests to identify aldehydes, ketones and methyl ketones",
    ],
    key_concepts=["Carbonyl group", "Nucleophilic addition", "Cyanohydrin", "Racemic mixture", "2,4-DNPH test", "Tollens' and Fehling's tests", "Iodoform test"],
    blocks=[
        H("Introduction"),
        T("The smell of almonds comes from benzaldehyde, the sharp smell of nail-polish remover comes from propanone, and methanal solution (formalin) is used to preserve biological specimens in school laboratories. "
          "Aldehydes and ketones both contain the **carbonyl group**, C=O. They are the products when alcohols are oxidized."),
        D("An **aldehyde** has the carbonyl group at the end of a carbon chain: R-CHO (at least one H on the carbonyl carbon). A **ketone** has the carbonyl group between two carbon atoms: R-CO-R'. Aldehyde names end in **-al** (ethanal, propanal) and ketone names in **-one** (propanone, butanone).", title="Aldehydes and ketones"),
        T("Aldehydes are made by gentle oxidation of **primary alcohols** (distil the aldehyde out as it forms using acidified potassium dichromate(VI)); ketones are made by oxidation of **secondary alcohols**. Tertiary alcohols are not oxidized this way."),
        H("Nucleophilic addition"),
        T("Oxygen is more electronegative than carbon, so C=O is polar. The carbon is delta-positive and is attacked by **nucleophiles** (electron-pair donors). The pi bond breaks and a new group adds across C=O. This is **nucleophilic addition**. (Compare alkenes, where an electrophile attacks the electron-rich C=C.)"),
        T("Aldehydes are more reactive than ketones: they have only one electron-releasing alkyl group (which reduces the positive charge on carbon) and less steric hindrance round the carbon."),
        KEY("Mechanism: addition of HCN", "Reagents: potassium cyanide (KCN) with dilute sulfuric acid, or HCN with a trace of base, at about room temperature. The cyanide ion, CN^-, is the nucleophile.",
            cards=[["Step 1", "The CN^- ion attacks the delta-positive carbon of C=O. The C=O pi electrons move onto oxygen, giving an alkoxide intermediate."],
                   ["Step 2", "The negative oxygen is protonated by H^+ (from HCN or the acid) to give the hydroxynitrile (cyanohydrin)."]]),
        F(r"<<CH3CHO + HCN -> CH3CH(OH)CN>>"),
        T("The product from ethanal is 2-hydroxypropanenitrile. Its centre carbon has four different groups (H, CH3, OH, CN), so it is a **chiral centre**. The planar C=O group can be attacked by CN^- from above or below with equal probability, so equal amounts of both enantiomers form: a **racemic mixture** that does not rotate plane-polarized light. The nitrile group can then be hydrolysed (reflux with dilute acid) to a carboxylic acid, lengthening the carbon chain by one: this makes 2-hydroxypropanoic acid (lactic acid)."),
        KEY("Reduction", "Sodium tetrahydridoborate(III) (NaBH4) in water or ethanol, or lithium tetrahydridoaluminate(III) (LiAlH4) in dry ether, followed by acid. The nucleophile is the hydride ion, H^-.",
            cards=[["Aldehyde", "RCHO is reduced to a primary alcohol: CH3CHO + 2[H] -> CH3CH2OH."],
                   ["Ketone", "RCOR' is reduced to a secondary alcohol: CH3COCH3 + 2[H] -> CH3CH(OH)CH3."]]),
        H("Condensation with 2,4-DNPH"),
        T("2,4-dinitrophenylhydrazine (Brady's reagent) reacts with both aldehydes and ketones to give a yellow, orange or red crystalline precipitate (a 2,4-dinitrophenylhydrazone). Water is lost in the reaction, so it is called a **condensation** (addition-elimination) reaction. After recrystallization the melting point of the derivative can be compared with tables to identify the original carbonyl compound. The test is positive for aldehydes and ketones only; carboxylic acids, esters and amides do not react."),
        H("Distinguishing aldehydes from ketones"),
        T("Aldehydes are **easily oxidized**; ketones are not. Mild oxidizing agents therefore distinguish them."),
        CODE("Reagent                      Aldehyde                        Ketone\n"
             "Tollens' (ammoniacal AgNO3,  silver mirror (Ag deposited)    no change\n"
             "  warm water bath)\n"
             "Fehling's/Benedict's         blue solution to red-brown       no change\n"
             "  (heat)                     precipitate of Cu2O (aliphatic)\n"
             "Acidified K2Cr2O7, warm      orange to green                  no change", "text",
             title="Distinguishing tests"),
        F(r"<<CH3CHO + 2[Ag(NH3)2]^+ + 3OH^- -> CH3COO^- + 2Ag + 4NH3 + 2H2O>>"),
        F(r"<<CH3CHO + 2Cu^2+ + 5OH^- -> CH3COO^- + Cu2O + 3H2O>>"),
        T("Benzaldehyde gives a silver mirror but does not give a positive Fehling's test (check your textbook)."),
        H("The iodoform test"),
        T("Warming a compound with iodine and aqueous sodium hydroxide gives a pale yellow precipitate of **triiodomethane** (iodoform, CHI3) with an antiseptic smell if the compound contains the group CH3CO- (a methyl ketone or ethanal) or CH3CH(OH)- (ethanol or a secondary alcohol with a methyl group). Propanone, butanone, ethanal, ethanol, propan-2-ol and phenylethanone are positive; propanal, methanal and propan-1-ol are negative."),
        F(r"<<CH3COCH3 + 3I2 + 4NaOH -> CHI3 + CH3COONa + 3NaI + 3H2O>>"),
        F(r"<<C6H5COCH3 + 3I2 + 4NaOH -> C6H5COONa + CHI3 + 3NaI + 3H2O>>"),
        EX("Worked example 1: identify the unknown", intro="Compound P, C3H6O, gives an orange precipitate with 2,4-DNPH, does not give a silver mirror with Tollens' reagent and gives a yellow precipitate with iodine and sodium hydroxide. Identify P.",
           steps=[
               S("Degrees of unsaturation", math=r"\dfrac{2(3)+2-6}{2} = 1"),
               S("2,4-DNPH", text="An orange precipitate shows that P is an aldehyde or a ketone (C=O accounts for the one double-bond equivalent)."),
               S("Tollens'", text="No silver mirror: P is not an aldehyde, so it is a ketone."),
               S("Iodoform", text="A positive iodoform test shows the CH3CO- group. The ketone is propanone, CH3COCH3."),
           ]),
        EX("Worked example 2: HCN with an unsymmetrical ketone", intro="Butanone reacts with KCN and dilute acid. Name the product and explain why it is optically inactive.",
           steps=[
               S("Reaction", math=r"<<CH3COCH2CH3 + HCN -> CH3C(OH)(CN)CH2CH3>>"),
               S("Name", text="2-hydroxy-2-methylbutanenitrile."),
               S("Chirality", text="The central carbon carries four different groups (CH3, C2H5, OH, CN), so it is chiral."),
               S("Racemic mixture", text="The nucleophile CN^- attacks the planar C=O from either side with equal probability, so equal amounts of both enantiomers form. Their rotations cancel and the mixture is optically inactive."),
           ]),
        MISTAKE("Saying 2,4-DNPH distinguishes aldehydes from ketones", "2,4-DNPH gives a precipitate with both. Use Tollens' or Fehling's to tell aldehydes from ketones."),
        MISTAKE("Calling the addition of HCN electrophilic", "The attacking species CN^- is a nucleophile, and it attacks the delta-positive carbon of C=O. Draw the curly arrow from the lone pair on carbon of CN^- to the carbonyl carbon."),
        TIP("The Board's 2023 report lists reactions of aldehydes in Paper 1 and, in Paper 2, the products of phenylethanone with NaOH/I2, 2,4-DNPH and HCN, which candidates found difficult. Remember that phenylethanone gives sodium benzoate and CHI3 with NaOH/I2, a hydrazone with 2,4-DNPH and a hydroxynitrile with HCN.", title="Exam link"),
        QUIZ("Which compound gives a silver mirror with Tollens' reagent?", ["Propanone", "Propanal", "Propan-2-ol", "Phenylethanone"], 1,
             "Propanal is an aldehyde, which is oxidized to propanoate while silver ions are reduced to silver.",
             hint="Which one is an aldehyde?",
             feedback=["Ketones are not oxidized by Tollens' reagent.", "", "A secondary alcohol is not oxidized by Tollens' reagent.", "A ketone: no silver mirror."]),
        QUIZ("Which compound gives a yellow precipitate with iodine and sodium hydroxide?", ["Propanal", "Pentan-3-one", "Butanone", "Methanal"], 2,
             "Butanone contains the CH3CO- group, which is required for the iodoform reaction.",
             hint="Look for the CH3CO group.",
             feedback=["Propanal, CH3CH2CHO, has no CH3CO group.", "Pentan-3-one, CH3CH2COCH2CH3, has no CH3CO group.", "", "Methanal has no methyl group."]),
        PQ("Write the mechanism for the reaction between propanal and KCN/H2SO4 and name the product. Why is the product a racemic mixture?",
           "Step 1: the lone pair on carbon of CN^- attacks the delta-positive carbon of C=O; the C=O pi electrons move onto oxygen to give an alkoxide intermediate CH3CH2CH(O^-)CN. Step 2: the O^- picks up H^+ (from HCN or H2SO4) to give CH3CH2CH(OH)CN, 2-hydroxybutanenitrile. The carbonyl group is planar, so CN^- attacks from either face with equal probability; the chiral carbon forms as equal amounts of both enantiomers, a racemic mixture."),
        PQ("Describe a chemical test to distinguish (a) propanal from propanone, and (b) propanone from pentan-3-one. State the observations.",
           "(a) Warm with Tollens' reagent: propanal gives a silver mirror; propanone gives no change. (Fehling's: propanal gives a red-brown precipitate; propanone gives none.) (b) Warm with iodine and aqueous sodium hydroxide: propanone gives a yellow precipitate (CHI3) with an antiseptic smell because it has the CH3CO group; pentan-3-one does not."),
        PQ("Compound Q has the formula C4H8O. It forms an orange precipitate with 2,4-DNPH and a silver mirror with Tollens' reagent. Give the two possible structures and name them.",
           "Q has one degree of unsaturation (C=O) and is an aldehyde: butanal, CH3CH2CH2CHO, or 2-methylpropanal, (CH3)2CHCHO."),
        PQ("Write equations for the reduction of propanone with NaBH4 and name the type of alcohol formed. Which ion is the nucleophile?",
           "CH3COCH3 + 2[H] → CH3CH(OH)CH3; propan-2-ol, a secondary alcohol. The nucleophile is the hydride ion, H^-, from NaBH4."),
        SUM("Aldehydes (RCHO) and ketones (RCOR') contain the polar C=O group and undergo nucleophilic addition; aldehydes are more reactive.",
            "HCN (KCN/H^+) gives a hydroxynitrile; with unsymmetrical carbonyls the product is a racemic mixture. NaBH4 reduces aldehydes to primary alcohols and ketones to secondary alcohols.",
            "2,4-DNPH gives an orange precipitate with both aldehydes and ketones.",
            "Tollens' (silver mirror) and Fehling's (red-brown Cu2O) are positive for aldehydes only.",
            "The iodoform test (I2/NaOH, yellow CHI3) is positive for CH3CO- and CH3CH(OH)- compounds."),
    ])]

# ============================================================================================
# 12. Carboxylic acids and derivatives
# ============================================================================================
LESSONS += [lesson(
    module=M_O, topic="Carboxylic acids and derivatives",
    title="Carboxylic acids, acyl chlorides, esters and amides",
    slug="chu2-carboxylic-acids-derivatives", minutes=25,
    summary="Carboxylic acids are weak acids made by oxidation or hydrolysis; they form acyl chlorides, esters and amides, whose reactivity and hydrolysis follow nucleophilic addition-elimination.",
    objectives=[
        "Describe the preparation, acidity and reactions of carboxylic acids",
        "Describe the preparation and reactions of acyl chlorides, esters and amides with equations",
        "Compare the relative reactivity of the derivatives and explain acid and alkaline hydrolysis of esters",
        "Use the Hofmann degradation and the equilibrium constant of esterification in calculations",
    ],
    key_concepts=["Carboxyl group", "Acyl chloride", "Esterification", "Ester hydrolysis", "Amide", "Hofmann degradation", "Addition-elimination"],
    blocks=[
        H("Introduction"),
        T("Vinegar contains ethanoic acid; ants and nettles sting with methanoic acid; the smell of pineapples comes from an ester, and soap is made from the sodium salts of long-chain carboxylic acids (found in palm oil from Cameroonian plantations). "
          "Nylon and polyester clothing are built from amides and esters. The family of carboxylic acids and its derivatives is a central part of organic chemistry."),
        D("A **carboxylic acid** contains the carboxyl group, -COOH. Its derivatives replace the -OH of the carboxyl group: **acyl chlorides** (-COCl), **esters** (-COOR), **amides** (-CONH2) and acid anhydrides (-CO-O-CO-).", title="Carboxylic acids and derivatives"),
        H("Preparation of carboxylic acids"),
        KEY("Three routes", "",
            cards=[["Oxidation of primary alcohols and aldehydes", "Heat under reflux with excess acidified potassium dichromate(VI) (orange to green): CH3CH2OH to CH3COOH."],
                   ["Hydrolysis of nitriles", "Reflux the nitrile with dilute hydrochloric acid: RCN + 2H2O + HCl gives RCOOH + NH4Cl. This lengthens the chain by one carbon."],
                   ["Oxidation of the side chain of an arene", "Methylbenzene is heated under reflux with alkaline potassium manganate(VII), then acidified: C6H5CH3 gives C6H5COOH."]]),
        H("Acid properties"),
        T("Carboxylic acids are weak acids (pKa about 4.8 for ethanoic acid). In the carboxylate ion the negative charge is delocalized over both oxygen atoms, which makes the ion stable. They react with active metals, bases and carbonates."),
        F(r"<<2CH3COOH + Mg -> (CH3COO)2Mg + H2>>"),
        F(r"<<CH3COOH + NaOH -> CH3COONa + H2O>>"),
        F(r"<<2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2>>"),
        T("Electron-withdrawing groups increase acid strength: chloroethanoic acid (pKa 2.9) is stronger than ethanoic acid because chlorine pulls electron density away and stabilizes the anion. Electron-releasing alkyl groups weaken the acid: methanoic acid (3.8) is stronger than ethanoic acid (4.8)."),
        H("Acyl chlorides"),
        T("An acyl chloride is made from the carboxylic acid with thionyl chloride, SOCl2 (the by-products SO2 and HCl are gases, so it is easily purified), or with PCl5."),
        F(r"<<CH3COOH + SOCl2 -> CH3COCl + SO2 + HCl>>"),
        F(r"<<CH3COOH + PCl5 -> CH3COCl + POCl3 + HCl>>"),
        T("Acyl chlorides are the **most reactive** derivatives because the carbonyl carbon is attached to two electronegative atoms (O and Cl) and Cl^- is a good leaving group. They react in a cold, vigorous **nucleophilic addition-elimination** reaction: the nucleophile adds to C=O and then Cl^- is lost."),
        CODE("Acyl chloride + water      -> carboxylic acid + HCl      (steamy fumes of HCl)\n"
             "Acyl chloride + alcohol     -> ester + HCl\n"
             "Acyl chloride + phenol      -> phenyl ester + HCl\n"
             "Acyl chloride + ammonia     -> amide + ammonium chloride\n"
             "Acyl chloride + amine       -> N-substituted amide + amine hydrochloride", "text",
             title="Reactions of ethanoyl chloride (the nucleophile attacks C=O)"),
        F(r"<<CH3COCl + H2O -> CH3COOH + HCl>>"),
        F(r"<<CH3COCl + C2H5OH -> CH3COOC2H5 + HCl>>"),
        F(r"<<CH3COCl + 2NH3 -> CH3CONH2 + NH4Cl>>"),
        H("Esters"),
        T("**Esterification** is the reversible reaction of a carboxylic acid with an alcohol, catalyzed by a few drops of concentrated sulfuric acid, with heating under reflux. The ester is named from the alcohol (alkyl) and the acid (-oate): ethyl ethanoate."),
        F(r"<<CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O>>"),
        T("Equilibrium constant: K_c = [ester][water] / [acid][alcohol]; for ethanoic acid and ethanol at room temperature K_c is about 4. To raise the yield, use an excess of one reactant or remove water. Esters are volatile, sweet-smelling liquids used as flavourings, perfumes and solvents."),
        KEY("Hydrolysis of esters", "",
            cards=[["Acid hydrolysis (reversible)", "Reflux with dilute HCl or H2SO4: ester + water gives acid + alcohol. The reverse of esterification, so it never goes to completion."],
                   ["Alkaline hydrolysis (irreversible)", "Reflux with aqueous NaOH: ester + OH^- gives the carboxylate salt + alcohol. The carboxylate ion cannot react with the alcohol, so the reaction goes to completion. Acidify to obtain the free acid. This is saponification when the ester is a fat."]]),
        F(r"<<CH3COOC2H5 + NaOH -> CH3COONa + C2H5OH>>"),
        H("Amides"),
        T("Amides contain -CONH2 and are named from the acid: ethanamide, CH3CONH2 (N-methylethanamide if there is a methyl on nitrogen). They are the least reactive derivatives and are neutral (the nitrogen lone pair is delocalized into C=O, so amides are not basic). They are hydrolysed by refluxing with acid (giving the acid and an ammonium salt) or with alkali (giving the carboxylate and ammonia)."),
        F(r"<<CH3CONH2 + NaOH -> CH3COONa + NH3>>"),
        KEY("Hofmann degradation", "Warm an amide with bromine and aqueous sodium hydroxide. The product is a primary amine with **one carbon fewer** than the amide.",
            cards=[["Equation", "RCONH2 + Br2 + 4NaOH -> RNH2 + 2NaBr + Na2CO3 + 2H2O"],
                   ["Use", "A way to shorten a carbon chain, and an identification tool: the amine has one carbon fewer, so propanamide gives ethylamine."]]),
        F(r"<<RCONH2 + Br2 + 4NaOH -> RNH2 + 2NaBr + Na2CO3 + 2H2O>>"),
        T("Reactivity order of derivatives towards nucleophiles: acyl chloride > acid anhydride > ester > amide."),
        EX("Worked example 1: equilibrium yield of ester", intro="0.500 mol of ethanoic acid and 0.500 mol of ethanol are mixed with a little acid catalyst and left to reach equilibrium. K_c = 4.0. Find the amount of ethyl ethanoate at equilibrium. (The volume cancels because the number of moles is the same on both sides.)",
           steps=[
               S("Let x mol of ester form", text="Then acid = ethanol = (0.500 - x) mol and water = x mol."),
               S("Write K_c", math=r"K_c = \dfrac{x \cdot x}{(0.500 - x)^2} = 4.0"),
               S("Take the square root", math=r"\dfrac{x}{0.500 - x} = 2.0 \;\Rightarrow\; x = 1.0 - 2.0x \;\Rightarrow\; 3x = 1.0"),
               S("Solve", math=r"x = 0.333\ \text{mol of ester}"),
           ]),
        EX("Worked example 2: alkaline hydrolysis", intro="8.80 g of ethyl ethanoate (Mr = 88) is refluxed with excess aqueous sodium hydroxide. Calculate the mass of sodium ethanoate (Mr = 82) formed.",
           steps=[
               S("Equation", math=r"<<CH3COOC2H5 + NaOH -> CH3COONa + C2H5OH>>"),
               S("Moles of ester", math=r"\dfrac{8.80}{88} = 0.100\ \text{mol}"),
               S("Moles of salt", text="1 : 1, so 0.100 mol."),
               S("Mass", math=r"0.100 \times 82 = 8.20\ \text{g}"),
           ]),
        MISTAKE("Using alkali to carry out the reverse of esterification and expecting equilibrium", "Acid hydrolysis is reversible, but alkaline hydrolysis goes to completion because the carboxylate ion cannot react with the alcohol. Say which one is meant."),
        MISTAKE("Saying amides are basic like amines", "In an amide the lone pair on nitrogen is delocalized onto the carbonyl oxygen, so amides are neutral. Amines are basic."),
        TIP("The Board's 2023 report lists hydrolysis of the derivatives, the preparation of carboxylic acids and their derivatives and the naming of amides in Paper 1, and the Hofmann degradation reagent in Paper 2. For every reaction, give the reagent, the condition (reflux, cold) and the equation.", title="Exam link"),
        QUIZ("Which reagent converts ethanoic acid to ethanoyl chloride?", ["Sodium chloride", "Thionyl chloride, SOCl2", "Hydrochloric acid", "Chlorine gas"], 1,
             "SOCl2 (or PCl5) replaces the -OH of the acid by -Cl.",
             hint="The reagent is a chloride of sulfur or phosphorus.",
             feedback=["It does not replace -OH.", "", "HCl does not make an acyl chloride from a carboxylic acid.", "Chlorine would substitute on the alkyl group instead."]),
        QUIZ("Why does alkaline hydrolysis of an ester go to completion?", ["The ester is destroyed by the heat", "The carboxylate ion formed does not react with the alcohol", "Water is removed", "NaOH is a catalyst"], 1,
             "The carboxylate salt is stable and cannot react with the alcohol, so the reverse reaction does not occur.",
             hint="Compare the product with that of acid hydrolysis.",
             feedback=["It is a chemical reaction, not decomposition.", "", "Water is a reactant here.", "NaOH is consumed, so it is a reagent."]),
        PQ("Write equations for the reaction of ethanoyl chloride with (a) water, (b) ethanol and (c) ammonia (excess). Name the organic product in each.",
           "(a) CH3COCl + H2O → CH3COOH + HCl (ethanoic acid). (b) CH3COCl + C2H5OH → CH3COOC2H5 + HCl (ethyl ethanoate). (c) CH3COCl + 2NH3 → CH3CONH2 + NH4Cl (ethanamide). The mechanism in each case is nucleophilic addition-elimination."),
        PQ("Explain why an acyl chloride is more reactive than the carboxylic acid towards nucleophiles.",
           "The carbonyl carbon in an acyl chloride is bonded to two electronegative atoms (O and Cl), so it is more delta-positive and more attractive to nucleophiles. The chloride ion is also a good leaving group. In the acid the OH group donates a lone pair into C=O, reducing the positive charge, and OH^- is a poor leaving group."),
        PQ("Describe how you would prepare a sample of ethyl ethanoate from ethanol and ethanoic acid and state two ways of increasing the yield.",
           "Mix ethanoic acid and ethanol with a few drops of concentrated sulfuric acid, heat under reflux, then distil off the ester. The reaction is reversible: CH3COOH + C2H5OH ⇌ CH3COOC2H5 + H2O. Use an excess of one reactant, or remove the ester or water as it forms (distillation, or concentrated H2SO4 which absorbs water)."),
        PQ("Compound W, C3H7NO, gives ethylamine when warmed with bromine and aqueous sodium hydroxide. Identify W and write an equation.",
           "The product has one carbon fewer than W, so W is propanamide, CH3CH2CONH2 (a Hofmann degradation). CH3CH2CONH2 + Br2 + 4NaOH → CH3CH2NH2 + 2NaBr + Na2CO3 + 2H2O."),
        SUM("Carboxylic acids are made by oxidation of primary alcohols or aldehydes, nitrile hydrolysis or side-chain oxidation; they are weak acids.",
            "SOCl2 or PCl5 converts RCOOH to the very reactive acyl chloride, which reacts with water, alcohols and ammonia/amines by addition-elimination.",
            "Esterification is reversible (conc. H2SO4, reflux); acid hydrolysis is reversible and alkaline hydrolysis goes to completion.",
            "Amides are neutral and the least reactive; hydrolysed by acid or alkali.",
            "Hofmann degradation: amide, Br2 and NaOH give an amine with one carbon fewer."),
    ])]

# ============================================================================================
# 13. Amines and diazonium salts
# ============================================================================================
LESSONS += [lesson(
    module=M_O, topic="Amines and diazonium salts",
    title="Amines, basicity and diazonium salts (azo dyes)",
    slug="chu2-amines-diazonium", minutes=25,
    summary="Amines are bases and nucleophiles because of the nitrogen lone pair; phenylamine forms a benzenediazonium salt at 0-5 °C, which couples with phenols to make azo dyes.",
    objectives=[
        "Classify amines and explain the order of basicity of aliphatic amines, ammonia and phenylamine",
        "Describe the preparation of amines and their reactions with acids, haloalkanes and acyl chlorides",
        "Describe diazotization of phenylamine and the conditions needed",
        "Describe coupling to make azo dyes and the other reactions of diazonium salts",
    ],
    key_concepts=["Primary, secondary, tertiary amine", "Basicity of amines", "Reduction of nitro compounds", "Diazotization", "Azo coupling", "Azo dye"],
    blocks=[
        H("Introduction"),
        T("The bright colours of printed cloth in the markets of Douala, Bamenda and Yaounde are made with synthetic dyes, and many are azo dyes made from phenylamine. "
          "The smell of rotting fish comes from amines, and many drugs and vitamins are amines. Amines are organic derivatives of ammonia, and like ammonia they have a lone pair on nitrogen."),
        D("An **amine** is a compound in which one or more hydrogen atoms of ammonia are replaced by alkyl or aryl groups. **Primary** amines are RNH2, **secondary** amines R2NH and **tertiary** amines R3N. **Phenylamine** (aniline), C6H5NH2, is an aromatic primary amine.", title="Amines"),
        H("Basicity"),
        T("The nitrogen lone pair can accept a proton, so amines are bases (weak bases, partly ionized in water): [[CH3NH2 + H2O <=> CH3NH3^+ + OH^-]]. Amines are also **nucleophiles**."),
        KEY("Order of basicity", "Strongest base on the left.",
            cards=[["Aliphatic amines > ammonia", "Alkyl groups push electrons towards N (positive inductive effect), so the lone pair is more available: (CH3)2NH > CH3NH2 > NH3 (pKb about 3.3 for methylamine and 4.8 for ammonia, approximate)."],
                   ["Phenylamine is the weakest", "The nitrogen lone pair is delocalized into the benzene ring, so it is less available for protons (pKb about 9). Phenylamine does not turn litmus blue."]]),
        F(r"<<CH3NH2 + HCl -> CH3NH3Cl>>"),
        F(r"<<C6H5NH2 + HCl -> C6H5NH3Cl>>"),
        T("Salts of amines are ionic and soluble in water. Adding sodium hydroxide frees the amine again: [[C6H5NH3^+ + OH^- -> C6H5NH2 + H2O]]."),
        H("Preparation"),
        KEY("Methods", "",
            cards=[["From haloalkanes", "Heat a haloalkane with excess ethanolic ammonia in a sealed tube: CH3CH2Br + 2NH3 gives CH3CH2NH2 + NH4Br. Without an excess of ammonia, further substitution gives secondary and tertiary amines."],
                   ["Reduction of nitriles", "Lithium tetrahydridoaluminate(III) in dry ether, or hydrogen with a nickel catalyst: CH3CN + 4[H] gives CH3CH2NH2."],
                   ["Reduction of nitrobenzene (phenylamine)", "Heat under reflux with tin and concentrated hydrochloric acid; then add excess aqueous sodium hydroxide to free the phenylamine from its salt."]]),
        F(r"<<CH3CH2Br + 2NH3 -> CH3CH2NH2 + NH4Br>>"),
        F(r"\mathrm{C_6H_5NO_2 + 6[H] \rightarrow C_6H_5NH_2 + 2H_2O}"),
        H("Reactions of amines"),
        F(r"<<CH3CH2NH2 + CH3COCl -> CH3CONHCH2CH3 + HCl>>"),
        T("The reaction with an acyl chloride gives an N-substituted amide (here N-ethylethanamide). The Board's report lists the reactions of amines among the concepts tested. Phenylamine reacts with bromine water at room temperature to give a white precipitate of 2,4,6-tribromophenylamine, because the -NH2 group activates the ring: [[C6H5NH2 + 3Br2 -> C6H2Br3NH2 + 3HBr]]."),
        H("Diazonium salts and azo dyes"),
        D("**Diazotization** is the reaction of a primary aromatic amine with nitrous acid, HNO2 (made in the mixture from sodium nitrite and hydrochloric acid), at **0-5 °C**, to form a **diazonium salt**.", title="Diazotization"),
        F(r"<<NaNO2 + HCl -> NaCl + HNO2>>"),
        F(r"<<C6H5NH2 + HNO2 + HCl -> C6H5N2^+ Cl^- + 2H2O>>"),
        T("The temperature is critical. Above about 5-10 °C the benzenediazonium ion decomposes, releasing nitrogen and forming phenol: [[C6H5N2^+ + H2O -> C6H5OH + N2 + H^+]]. Aliphatic diazonium salts are so unstable that they decompose at once."),
        KEY("Azo coupling", "The diazonium ion is a weak electrophile. It attacks a highly activated ring (phenol in alkaline solution, or another amine) at the 4-position, giving an **azo compound** with the -N=N- group, which is highly coloured because the delocalized system joins the two rings.",
            cards=[["With phenol dissolved in NaOH, 0-5 °C", "Yellow-orange azo dye, 4-hydroxyphenylazobenzene, that dyes cloth. The alkaline solution gives the phenoxide ion, which is much more reactive than phenol."],
                   ["With naphthalen-2-ol in NaOH, 0-5 °C", "A bright orange-red (scarlet) precipitate, the standard laboratory test for aromatic primary amines (check your textbook)."]]),
        F(r"<<C6H5N2^+ + C6H5O^- -> C6H5N=NC6H4OH>>"),
        T("Other reactions of benzenediazonium salts (replace N2 by another group, releasing nitrogen gas):"),
        CODE("With water, warm             -> phenol (C6H5OH) + N2\n"
             "With KI(aq), room temp.     -> iodobenzene (C6H5I) + N2   (a good way to put iodine on the ring)\n"
             "With CuCl in HCl (Sandmeyer)-> chlorobenzene + N2\n"
             "With CuCN                   -> benzonitrile + N2", "text",
             title="Reactions of C6H5N2+ Cl-"),
        T("Benzenediazonium chloride is the key intermediate in making substituted benzenes from benzene: benzene to nitrobenzene to phenylamine to diazonium salt to many products."),
        EX("Worked example 1: yield", intro="12.3 g of nitrobenzene (Mr = 123) is reduced to phenylamine (Mr = 93) in 75.0% yield. Calculate the mass of phenylamine.",
           steps=[
               S("Moles of nitrobenzene", math=r"\dfrac{12.3}{123} = 0.100\ \text{mol}"),
               S("Theoretical mass of phenylamine", text="1 : 1, so 0.100 mol x 93 = 9.30 g."),
               S("Actual mass", math=r"0.750 \times 9.30 = 6.98\ \text{g}"),
           ]),
        EX("Worked example 2: a synthesis of an azo dye", intro="Outline the synthesis of 4-hydroxyphenylazobenzene starting from benzene.",
           steps=[
               S("Step 1: nitration", text="Concentrated HNO3 and concentrated H2SO4, 50-55 °C: benzene to nitrobenzene."),
               S("Step 2: reduction", text="Sn and concentrated HCl, reflux, then NaOH: nitrobenzene to phenylamine."),
               S("Step 3: diazotization", text="NaNO2 and HCl at 0-5 °C: phenylamine to benzenediazonium chloride."),
               S("Step 4: coupling", text="Add the cold diazonium solution to phenol dissolved in aqueous NaOH at 0-5 °C: orange-yellow azo dye forms."),
           ]),
        MISTAKE("Doing diazotization at room temperature", "Benzenediazonium chloride decomposes above about 10 °C to give phenol and nitrogen. Keep the mixture in an ice bath at 0-5 °C, and use the diazonium solution at once."),
        MISTAKE("Saying phenylamine is a stronger base than ammonia", "The lone pair on nitrogen is delocalized into the ring, so phenylamine is a weaker base than ammonia. Alkylamines are stronger bases than ammonia."),
        TIP("The Board's 2023 report lists the reactions of amines in Paper 1, and in Paper 2 candidates had to state the reagent and conditions for converting phenylamine to benzenediazonium chloride. Learn: NaNO2/HCl (or HNO2) at 0-5 °C.", title="Exam link"),
        QUIZ("What is the temperature range for diazotization of phenylamine?", ["20-25 °C", "50-55 °C", "0-5 °C", "100 °C"], 2,
             "Benzenediazonium chloride is stable only in ice-cold solution.",
             hint="The salt decomposes in warm solution.",
             feedback=["Too warm; the diazonium salt would decompose.", "That is the nitration temperature.", "", "Far too hot."]),
        QUIZ("Which compound is the strongest base?", ["Ammonia", "Phenylamine", "Ethylamine", "Ethanamide"], 2,
             "The electron-donating ethyl group makes the lone pair on N of ethylamine more available than in ammonia.",
             hint="Which has an electron-donating group on N and a localized lone pair?",
             feedback=["Ammonia is weaker than ethylamine.", "The lone pair is delocalized into the ring.", "", "The lone pair of an amide is delocalized onto C=O; amides are neutral."]),
        PQ("Explain why phenylamine is a weaker base than ethylamine.",
           "In phenylamine the lone pair on nitrogen overlaps with the pi system of the benzene ring and is delocalized, so it is less available to accept a proton. In ethylamine the ethyl group pushes electrons towards nitrogen (positive inductive effect) and the lone pair is localized, so it is more available."),
        PQ("Describe how phenylamine can be converted into benzenediazonium chloride and then into a yellow-orange azo dye. Give the reagents and the conditions.",
           "Diazotization: add NaNO2 and HCl (nitrous acid, HNO2) to phenylamine at 0-5 °C to give C6H5N2^+ Cl^-. Coupling: add the cold solution to phenol dissolved in aqueous NaOH, also at 0-5 °C. The 4-hydroxyphenylazobenzene precipitates as a yellow-orange dye."),
        PQ("Give the reagents for each step in the conversion of benzene to phenylamine, and state the colour change or observation you would expect when the final product is treated with bromine water.",
           "Benzene to nitrobenzene: concentrated HNO3 and concentrated H2SO4, 50-55 °C. Nitrobenzene to phenylamine: Sn and concentrated HCl, reflux, then NaOH. Phenylamine decolourizes bromine water and gives a white precipitate of 2,4,6-tribromophenylamine."),
        PQ("Warm benzenediazonium chloride solution slowly to 40 °C. State what is observed and write an equation.",
           "Bubbles of colourless gas (nitrogen) are given off and phenol is formed (an antiseptic smell). C6H5N2^+ + H2O → C6H5OH + N2 + H^+."),
        SUM("Amines are bases and nucleophiles; basicity: alkylamines > ammonia > phenylamine.",
            "Amines are made from haloalkanes and excess ammonia, by reducing nitriles, and (phenylamine) by reducing nitrobenzene with Sn/HCl.",
            "Primary amines react with acyl chlorides to give N-substituted amides.",
            "Diazotization: C6H5NH2 + NaNO2/HCl at 0-5 °C gives C6H5N2^+ Cl^-.",
            "Coupling with phenol in NaOH (0-5 °C) gives an azo dye; warming gives phenol and N2; KI gives iodobenzene."),
    ])]

# ============================================================================================
# 14. Amino acids, proteins and polymers
# ============================================================================================
LESSONS += [lesson(
    module=M_O, topic="Amino acids, proteins and polymers",
    title="Amino acids, proteins and synthetic polymers",
    slug="chu2-amino-acids-proteins-polymers", minutes=25,
    summary="Amino acids are amphoteric zwitterions that join by peptide bonds to make proteins; synthetic polymers are made by addition or by condensation (polyesters, polyamides), and their structure explains their properties.",
    objectives=[
        "Describe the structure, amphoteric behaviour and chirality of amino acids, including the zwitterion and isoelectric point",
        "Form peptides by condensation, describe the levels of protein structure and the biuret test",
        "Draw repeat units of addition polymers and of polyesters and polyamides, and work out the monomers",
        "Compare addition and condensation polymerization and comment on biodegradability",
    ],
    key_concepts=["Zwitterion", "Isoelectric point", "Peptide bond", "Protein structure", "Addition polymer", "Condensation polymer", "Polyamide and polyester"],
    blocks=[
        H("Introduction"),
        T("Beans and groundnuts, fish and eggs, which feed families across Cameroon, supply proteins; the clothes you wear may be polyester or nylon; the plastic bags and bottles in every market are poly(ethene). "
          "Proteins and synthetic polymers are both long chains built from small units, but proteins are built from 20 types of amino acid and synthetic polymers from just one or two monomers."),
        H("Amino acids"),
        D("An **amino acid** contains both an amino group (-NH2) and a carboxyl group (-COOH). In the **2-amino acids** (alpha amino acids) found in proteins, both groups are attached to the same carbon atom: H2N-CH(R)-COOH, where R is the side chain.", title="Amino acids"),
        CODE("Glycine    R = H      H2N-CH2-COOH\n"
             "Alanine    R = CH3    H2N-CH(CH3)-COOH\n"
             "Serine     R = CH2OH  H2N-CH(CH2OH)-COOH\n"
             "Cysteine   R = CH2SH  H2N-CH(CH2SH)-COOH", "text", title="Examples"),
        T("**Optical isomerism.** In every 2-amino acid except glycine the 2-carbon (the alpha carbon) has four different groups (H, NH2, COOH and R), so it is a chiral centre and the molecule has two non-superimposable mirror-image forms. Natural proteins contain only the L form. Glycine (R = H) is not chiral."),
        KEY("Amphoteric behaviour and the zwitterion", "Amino acids are crystalline solids with high melting points and are soluble in water. This is because they exist as **zwitterions**: ions with both a positive and a negative charge.",
            cards=[["Zwitterion (neutral solution)", "The proton moves from COOH to NH2, giving +H3N-CH(R)-COO^-. The strong ionic attractions explain the high melting points and water solubility."],
                   ["In acid", "The COO^- group accepts a proton: +H3N-CH(R)-COOH. The amino acid is a cation."],
                   ["In alkali", "The NH3^+ group loses a proton: H2N-CH(R)-COO^-. The amino acid is an anion."]]),
        D("The **isoelectric point** is the pH at which an amino acid (or protein) has no net charge, existing as the zwitterion. At this pH it does not move in an electric field and its solubility is lowest. For glycine it is about pH 6.", title="Isoelectric point"),
        T("In **electrophoresis** or **chromatography** amino acids are separated by their different charges and sizes; the colourless spots are developed with ninhydrin, which gives a purple or blue-violet colour."),
        H("Peptides and proteins"),
        T("Two amino acids join by a **condensation** reaction between the -COOH of one and the -NH2 of the other, losing water. The new -CO-NH- link is a **peptide bond** (an amide link)."),
        F(r"\mathrm{H_2N{-}CH_2{-}COOH + H_2N{-}CH(CH_3){-}COOH \rightarrow H_2N{-}CH_2{-}CO{-}NH{-}CH(CH_3){-}COOH + H_2O}"),
        T("The product is a dipeptide, glycylalanine (Gly-Ala), with the free -NH2 end named first. Two different amino acids can form two different dipeptides (Gly-Ala and Ala-Gly). Three different amino acids can form 3 x 2 x 1 = 6 different tripeptides. Long chains are **polypeptides** and are **proteins**."),
        KEY("Levels of protein structure", "",
            cards=[["Primary", "The sequence of amino acids joined by peptide bonds."],
                   ["Secondary", "Regular folding held by hydrogen bonds between C=O and N-H groups of the backbone: the alpha helix and the beta pleated sheet."],
                   ["Tertiary", "The overall 3D shape from interactions between R groups: hydrogen bonds, ionic bonds, disulfide bridges (S-S between cysteines) and hydrophobic interactions."],
                   ["Quaternary", "The arrangement of more than one polypeptide chain, as in haemoglobin (four chains)."]]),
        T("**Hydrolysis** of a protein by refluxing with 6 mol/dm³ hydrochloric acid for about 24 hours breaks all the peptide bonds and releases the amino acids, which can be identified by chromatography. The **biuret test** (aqueous NaOH then a few drops of dilute copper(II) sulfate) gives a purple (violet) colour with peptide bonds, i.e. with proteins and polypeptides."),
        H("Addition polymers"),
        D("**Addition polymerization** joins many alkene monomers (unsaturated molecules) without losing any atoms; the C=C bonds open and the chain forms. The **repeat unit** is the smallest unit that repeats along the chain.", title="Addition polymers"),
        CODE("Monomer              Polymer                   Repeat unit\n"
             "ethene CH2=CH2       poly(ethene)              -CH2-CH2-\n"
             "propene CH2=CHCH3    poly(propene)             -CH2-CH(CH3)-\n"
             "chloroethene         poly(chloroethene), PVC   -CH2-CHCl-\n"
             "phenylethene         poly(phenylethene)        -CH2-CH(C6H5)-\n"
             "tetrafluoroethene    PTFE                      -CF2-CF2-", "text", title="Examples"),
        T("To find the monomer from an addition polymer, take the repeat unit and put back the C=C double bond between the two chain carbon atoms. Addition polymers have a carbon-only backbone, so they are non-biodegradable and persist in the environment; this is why plastic waste blocks drains in many cities."),
        H("Condensation polymers"),
        T("In **condensation polymerization** two different functional groups react and a small molecule (water or hydrogen chloride) is lost each time a bond forms. The monomers have two reactive groups, one at each end."),
        KEY("Polyesters and polyamides", "",
            cards=[["Polyester (Terylene, poly(ethylene terephthalate))", "Benzene-1,4-dicarboxylic acid + ethane-1,2-diol. The ester link -CO-O- forms and water is lost."],
                   ["Polyamide (nylon-6,6)", "Hexanedioic acid (or hexanedioyl dichloride, which reacts faster and loses HCl) + hexane-1,6-diamine. The amide link -CO-NH- forms. The two 6s refer to six carbons in each monomer."],
                   ["Proteins", "Natural polyamides made from amino acids."]]),
        F(r"\mathrm{n\,H_2N(CH_2)_6NH_2 + n\,HOOC(CH_2)_4COOH \rightarrow [{-}NH(CH_2)_6NHCO(CH_2)_4CO{-}]_n + 2n\,H_2O}"),
        T("Both polyesters and polyamides can be broken down (hydrolysed) by acids and alkalis, so they are more biodegradable than addition polymers. Polyamides have strong hydrogen bonds between chains, giving strong fibres."),
        EX("Worked example 1: a dipeptide", intro="Write the molecular formulae of glycine (C2H5NO2) and alanine (C3H7NO2), and find the molecular formula and Mr of the dipeptide Gly-Ala. (C = 12, H = 1, N = 14, O = 16)",
           steps=[
               S("Add the two amino acids", text="C2H5NO2 + C3H7NO2 = C5H12N2O4."),
               S("Subtract one water for the peptide bond", text="C5H12N2O4 - H2O = C5H10N2O3."),
               S("Relative molecular mass", math=r"5(12) + 10(1) + 2(14) + 3(16) = 146"),
           ]),
        EX("Worked example 2: finding the monomer", intro="A polymer has the repeat unit -CH2-CHCl-. Name the monomer and the polymer. Then state whether the polymer is biodegradable.",
           steps=[
               S("Restore the double bond", text="Monomer: CH2=CHCl, chloroethene."),
               S("Name the polymer", text="Poly(chloroethene) (PVC)."),
               S("Biodegradability", text="The carbon-carbon backbone is not attacked by micro-organisms, so it is non-biodegradable."),
           ]),
        MISTAKE("Including the water in the repeat unit of a condensation polymer", "Water (or HCl) is lost during bond formation and is not part of the polymer. The repeat unit of nylon-6,6 contains one residue of each monomer joined by two amide links, with no extra water."),
        MISTAKE("Saying amino acids are acidic or basic only", "Amino acids contain both an acidic group and a basic group, so they are amphoteric, and in solution they exist mainly as zwitterions with a pH-dependent charge."),
        TIP("Amino acids and optical isomers appear in Paper 2 (the Board's 2023 report notes that candidates found it difficult to write the optical isomers of an amino acid). Draw the two enantiomers as mirror images about a dotted vertical line, with the chiral carbon in the centre; label the groups NH2, COOH, H, R in the same order.", title="Exam link"),
        QUIZ("What is the product of the condensation of two amino acids?", ["An ester and water", "A dipeptide and water", "An acid anhydride", "An amine and carbon dioxide"], 1,
             "The carboxyl group of one amino acid reacts with the amino group of the other, forming an amide (peptide) link and water.",
             hint="Which functional groups react?",
             feedback=["An ester needs an alcohol.", "", "An anhydride needs two acids.", "No CO2 is lost."]),
        QUIZ("Which polymer is formed by condensation polymerization?", ["Poly(ethene)", "Nylon-6,6", "PVC", "PTFE"], 1,
             "Nylon-6,6 forms from a diacid and a diamine, losing water or HCl.",
             hint="Look for a polymer made from two different monomers with two reactive groups each.",
             feedback=["Addition polymer.", "", "Addition polymer.", "Addition polymer."]),
        PQ("Explain why glycine has a high melting point and dissolves in water, whereas ethanoic acid is a liquid at room temperature.",
           "Glycine exists as a zwitterion, +H3N-CH2-COO^-, so there are strong ionic attractions between the molecules in the solid, giving a high melting point. These ions are also hydrated by water, so glycine dissolves. Ethanoic acid is a simple molecule with only hydrogen bonding and van der Waals forces between molecules."),
        PQ("Draw the two enantiomers of alanine and explain why glycine does not show optical isomerism.",
           "The alpha carbon of alanine has four different groups: H, NH2, COOH and CH3. The two enantiomers are mirror images that cannot be superimposed, so the carbon is a chiral centre. In glycine the alpha carbon has two hydrogen atoms (R = H), so it has no chiral centre and there is a plane of symmetry."),
        PQ("Write the repeat unit of the polyester formed from ethane-1,2-diol and benzene-1,4-dicarboxylic acid. State the small molecule that is lost, and the type of polymerization.",
           "Repeat unit: -O-CH2-CH2-O-CO-C6H4-CO-. Water is lost (one molecule for each ester link). It is condensation polymerization."),
        PQ("Compare addition and condensation polymerization in three ways.",
           "Addition polymerization: monomers contain a C=C bond; no small molecule is lost; the repeat unit has the same formula as the monomer; the backbone is carbon-carbon, so the polymer is non-biodegradable. Condensation polymerization: the monomers have two functional groups; a small molecule such as H2O or HCl is lost for every link; the polymer is a polyester or polyamide, which can be hydrolysed (more biodegradable)."),
        SUM("2-Amino acids have NH2 and COOH on the same carbon; they exist as zwitterions, are amphoteric and (except glycine) are chiral.",
            "Amino acids join by peptide bonds (condensation, losing water); proteins have primary, secondary, tertiary and quaternary structure.",
            "Hydrolysis with 6 mol/dm³ HCl gives amino acids; the biuret test gives a purple colour for peptide bonds.",
            "Addition polymers (poly(ethene), PVC, PTFE) have repeat units from C=C monomers and are non-biodegradable.",
            "Condensation polymers (polyesters, nylon, proteins) lose H2O or HCl and are formed from monomers with two functional groups."),
    ])]

# ============================================================================================
# 15. Structure elucidation by IR, NMR and mass spectrometry
# ============================================================================================
LESSONS += [lesson(
    module=M_O, topic="Structure elucidation by IR, NMR and mass spectrometry",
    title="Structure elucidation: IR, NMR and mass spectra together",
    slug="chu2-structure-elucidation-spectroscopy", minutes=25,
    summary="Combine the molecular ion and fragments from mass spectrometry, functional groups from infrared absorptions and the number, shift, area and splitting of NMR signals to deduce a structure.",
    objectives=[
        "Use the molecular ion, M+1 and M+2 peaks and common fragments to find the relative molecular mass and clues to structure",
        "Identify functional groups from characteristic infrared absorptions",
        "Interpret 1H NMR chemical shifts, integration and the n + 1 splitting rule, and 13C NMR peak counts",
        "Combine the data and the degrees of unsaturation to propose a structure",
    ],
    key_concepts=["Molecular ion", "Fragmentation", "IR absorption", "Chemical shift", "Integration", "n + 1 rule", "Degrees of unsaturation"],
    blocks=[
        H("Introduction"),
        T("A forensic laboratory identifies an unknown white powder in minutes; a food laboratory checks that an edible oil has not been mixed with another oil; a pharmaceutical company confirms that each tablet contains the right drug. All use the same three techniques: mass spectrometry (MS), infrared (IR) spectroscopy and nuclear magnetic resonance (NMR). "
          "Each answers a different question about a molecule. Together, they often give its structure."),
        KEY("What each technique tells you", "",
            cards=[["Mass spectrum", "The molecular ion peak gives the relative molecular mass. Fragment peaks show which pieces the molecule breaks into."],
                   ["Infrared spectrum", "Absorptions show the bonds and functional groups present (O-H, C=O, N-H, C≡N, C=C...)."],
                   ["1H NMR spectrum", "Shows how many different hydrogen environments there are (number of signals), how many hydrogens in each (integration), what type (chemical shift) and how many hydrogens are on neighbouring carbons (splitting)."],
                   ["13C NMR spectrum", "One signal for each different carbon environment; the shift shows C=O, C=C or aromatic, C-O or C-C."]]),
        H("Degrees of unsaturation"),
        F(r"\text{Degrees of unsaturation} = \dfrac{2C + 2 + N - H - X}{2}"),
        T("Count one for each double bond or ring, two for a triple bond and four for a benzene ring. Oxygen does not affect the count. For C4H8O2 the value is (8 + 2 - 8)/2 = 1: one C=O (or ring). For C7H6O2: (14 + 2 - 6)/2 = 5: a benzene ring (4) plus one C=O."),
        H("Mass spectrometry"),
        T("In the spectrometer the molecule loses an electron to form the **molecular ion**, M^+. The peak at the highest m/z (apart from small isotope peaks) gives the relative molecular mass. Weak bonds break to form fragment ions; each fragment peak has m/z equal to the mass of the fragment ion. The base peak is the tallest peak."),
        CODE("m/z   Fragment ion         Typical source\n"
             "15    CH3+                 methyl group\n"
             "29    C2H5+ or CHO+        ethyl group; aldehyde\n"
             "43    CH3CO+ or C3H7+      methyl ketone, ester or propyl group\n"
             "77    C6H5+                phenyl group\n"
             "91    C7H7+                methylbenzene (benzyl group)\n"
             "105   C6H5CO+              benzoyl group (benzoyl compounds)\n"
             "M-17  loss of OH           alcohol or acid\n"
             "M-18  loss of H2O          alcohol\n"
             "M-28  loss of CO or C2H4\n"
             "M-29  loss of C2H5 or CHO", "text", title="Common fragments (whole-number masses)"),
        KEY("Isotope peaks", "",
            cards=[["M+1 peak from 13C", "About 1.1% of carbon atoms are 13C. Number of C atoms = (height of M+1 / height of M) x 100 / 1.1."],
                   ["Chlorine", "35Cl : 37Cl = 3 : 1, so peaks M and M+2 in the ratio 3 : 1 (e.g. chloroethane at 64 and 66)."],
                   ["Bromine", "79Br : 81Br = 1 : 1, so peaks M and M+2 of equal height (bromoethane at 108 and 110)."],
                   ["Nitrogen rule", "A compound with one nitrogen atom (or an odd number) has an odd relative molecular mass, e.g. propanamide, 73."]]),
        H("Infrared spectroscopy"),
        T("Bonds absorb infrared radiation at characteristic wavenumbers (in cm⁻¹) and make them vibrate. Use the table to spot functional groups. The 'fingerprint region' below 1500 cm⁻¹ is unique to each compound and is matched against a library."),
        IMG("al-chu2-ir-regions.svg", alt="A horizontal wavenumber scale from 4000 to 500 per centimetre with coloured bars marking the ranges for O-H, N-H, C-H, C triple bond N, C double bond O and C double bond C absorptions.",
            caption="Figure 1. Where common bonds absorb in the infrared (approximate ranges)."),
        CODE("Bond                 Wavenumber (cm-1)    Appearance\n"
             "O-H alcohol/phenol   3200-3550            broad\n"
             "O-H carboxylic acid  2500-3300            very broad, overlaps C-H\n"
             "N-H amine/amide      3300-3500            medium, sometimes two peaks\n"
             "C-H                  2850-3100            medium to strong\n"
             "C≡N, C≡C             2100-2260            weak to medium\n"
             "C=O                  1680-1750            strong, sharp\n"
             "C=C                  1620-1680            weak to medium\n"
             "C-O                  1000-1300            strong\n"
             "\n"
             "C=O: aldehyde about 1725; ketone about 1715; ester about 1740; acid about 1710; amide about 1650", "text",
             title="Characteristic IR absorptions"),
        H("1H NMR spectroscopy"),
        T("In a strong magnetic field hydrogen nuclei absorb radio waves. The position of the signal is the **chemical shift**, δ, in ppm measured from tetramethylsilane (TMS, δ = 0), which is used as a reference because all its 12 hydrogen atoms are in the same environment and it is inert. Electronegative atoms and double bonds **deshield** hydrogens and move the signal to a higher δ."),
        CODE("Hydrogen environment            Approximate delta (ppm)\n"
             "R-CH3                          0.9\n"
             "R-CH2-R                        1.3\n"
             "CH3-C=O                        2.1\n"
             "CH2-C=O or CH2-Ar              2.2-2.7\n"
             "CH2-O (alcohol or ester)       3.3-4.3\n"
             "C=C-H                          4.5-6.0\n"
             "Ar-H (benzene ring)            6.5-8.0\n"
             "R-CHO                          9.4-10.0\n"
             "R-COOH                         10-12\n"
             "R-OH, R-NH2                    0.5-5.5 (variable, broad)", "text", title="Chemical shifts"),
        KEY("Reading a spectrum", "",
            cards=[["Number of signals", "Equals the number of different hydrogen environments."],
                   ["Integration (area)", "The relative areas give the ratio of hydrogens in each environment, e.g. 3 : 2 : 3."],
                   ["Splitting: n + 1 rule", "A signal split by n hydrogens on adjacent carbons has n + 1 lines: singlet (0 neighbours), doublet (1), triplet (2), quartet (3). Peak areas follow Pascal's triangle: doublet 1:1, triplet 1:2:1, quartet 1:3:3:1."],
                   ["OH and NH protons", "Usually singlets, with no coupling. After shaking with D2O, OH and NH signals disappear because H is exchanged for D."]]),
        IMG("al-chu2-nmr-ethyl.svg", alt="Schematic 1H NMR spectrum of ethyl ethanoate: a triplet near 1.2 ppm for three hydrogens, a singlet near 2.0 ppm for three hydrogens and a quartet near 4.1 ppm for two hydrogens.",
            caption="Figure 2. Schematic 1H NMR spectrum of ethyl ethanoate, CH3COOCH2CH3 (approximate shifts)."),
        T("**13C NMR.** Each different carbon environment gives one signal. Typical shifts: alkyl carbons 5-40 ppm; C-O 50-90; C=C and aromatic carbons 100-150; C=O in esters, acids and amides 160-185; C=O in aldehydes and ketones 190-220. For example, propanone has only 2 signals (CH3 and C=O) and ethyl ethanoate has 4."),
        H("A strategy for combined problems"),
        KEY("Six steps", "",
            cards=[["1", "M^+ gives the relative molecular mass; use the formula if it is given and calculate the degrees of unsaturation."],
                   ["2", "Use IR to list the functional groups: C=O, O-H, N-H, C≡N."],
                   ["3", "Count the NMR signals and the integration to find the fragments."],
                   ["4", "Use the splitting to join the fragments (CH3 triplet with CH2 quartet means an ethyl group)."],
                   ["5", "Check the MS fragments against the proposed structure."],
                   ["6", "Check that the molecular formula and the degrees of unsaturation match."]]),
        EX("Worked example 1: C4H8O2", intro="Compound A has relative molecular mass 88 and formula C4H8O2. IR: strong peak at 1740 cm⁻¹, no broad peak above 2500 cm⁻¹. 1H NMR: triplet at 1.2 (3H), singlet at 2.0 (3H), quartet at 4.1 (2H). MS shows peaks at 43 and 29. Identify A.",
           steps=[
               S("Degrees of unsaturation", math=r"\dfrac{2(4) + 2 - 8}{2} = 1"),
               S("IR", text="1740 cm⁻¹ is C=O of an ester. No broad O-H above 2500 cm⁻¹, so not a carboxylic acid."),
               S("NMR", text="Singlet 2.0 (3H) is CH3-C=O. Quartet 4.1 (2H) with triplet 1.2 (3H) is -OCH2CH3, an ethyl group on oxygen."),
               S("MS", text="43 = CH3CO+ and 29 = C2H5+, consistent with ethyl ethanoate."),
               S("Answer", text="A is CH3COOCH2CH3, ethyl ethanoate (Mr = 88)."),
           ]),
        EX("Worked example 2: C8H8O", intro="Compound B, C8H8O, gives IR peaks at 1685 and 3050 cm⁻¹, 1H NMR signals at 2.6 (singlet, 3H) and 7.4-8.0 (multiplet, 5H), and MS peaks at 120, 105 and 77. B gives a yellow precipitate with iodine and sodium hydroxide. Identify B.",
           steps=[
               S("Degrees of unsaturation", math=r"\dfrac{2(8) + 2 - 8}{2} = 5 \;\Rightarrow\; \text{benzene ring (4)} + \text{C=O (1)}"),
               S("IR", text="1685 cm⁻¹ is C=O of a ketone conjugated with a ring; 3050 cm⁻¹ is aromatic C-H."),
               S("NMR", text="Singlet at 2.6 (3H): CH3-C=O. Multiplet 7.4-8.0 (5H): a monosubstituted benzene ring."),
               S("MS", text="105 = C6H5CO+ (benzoyl) and 77 = C6H5+."),
               S("Answer", text="B is C6H5COCH3, phenylethanone. The CH3CO group explains the positive iodoform test."),
           ]),
        MISTAKE("Reading the number of NMR signals as the number of hydrogens", "Signals count environments, not atoms. The area (integration) gives the number of hydrogens in each environment. Propanone has 6 hydrogens but only one signal."),
        MISTAKE("Using the splitting rule with the wrong neighbours", "The signal is split by hydrogens on **adjacent carbons** only, not by hydrogens on the same carbon and not by an OH hydrogen (usually no coupling). The CH2 of ethyl ethanoate has 3 neighbours on CH3, so it is a quartet."),
        TIP("Deducing a structure from data is a Paper 2 skill: the Board's 2023 report describes organic questions that ask candidates to find a structure from calculations and tests, and says many candidates found this hard. Always show your working: state the molecular formula, the degrees of unsaturation, each IR peak with its meaning, and each NMR signal with its integration, splitting and assignment.", title="Exam link"),
        QUIZ("An IR spectrum has a strong sharp peak at 1715 cm⁻¹ and a broad peak at 3300 cm⁻¹. Which pair of groups is present?", ["C=O and O-H", "C≡N and N-H", "C=C and C-H", "C-O and C-Cl"], 0,
             "1715 cm⁻¹ is a C=O stretch and the broad band near 3300 cm⁻¹ is an O-H stretch (alcohol), so the compound has both groups.",
             hint="Use the table of characteristic absorptions.",
             feedback=["", "C≡N absorbs near 2250 cm⁻¹.", "C=C absorbs near 1650 cm⁻¹, not at 1715.", "These absorb in the fingerprint region."]),
        QUIZ("How many signals are in the 1H NMR spectrum of propanone, CH3COCH3?", ["1", "2", "3", "6"], 0,
             "All six hydrogens are in the same environment (two equivalent CH3 groups), so there is one signal (a singlet).",
             hint="Are the two methyl groups different?",
             feedback=["", "Both CH3 groups are identical.", "There are only two types of carbon, and one type of hydrogen.", "Signals count environments, not hydrogens."]),
        PQ("A compound has Mr = 74 and formula C3H6O2. IR shows a broad band from 2500 to 3300 cm⁻¹ and a peak at 1710 cm⁻¹. 1H NMR: triplet 1.2 (3H), quartet 2.4 (2H), singlet 11.5 (1H). Identify the compound.",
           "Degrees of unsaturation = (6 + 2 - 6)/2 = 1 (C=O). The broad band 2500-3300 and peak at 1710 cm⁻¹ indicate a carboxylic acid, -COOH. NMR: singlet at 11.5 is the COOH proton; quartet (2H) with triplet (3H) is a CH2CH3 group, attached to the C=O (CH2 at 2.4). The compound is propanoic acid, CH3CH2COOH (Mr = 74)."),
        PQ("Distinguish propan-1-ol from propan-2-ol using the number of signals and splitting in their 1H NMR spectra.",
           "Propan-1-ol, CH3CH2CH2OH, has 4 signals: CH3 triplet (3H, about 0.9), middle CH2 sextet (2H, about 1.6), OCH2 triplet (2H, about 3.6) and OH singlet (1H). Propan-2-ol, (CH3)2CHOH, has 3 signals: CH3 doublet (6H, about 1.2), CH septet (1H, about 4.0) and OH singlet (1H)."),
        PQ("State the number of signals in the 13C NMR spectrum of (a) ethyl ethanoate and (b) benzoic acid, with a reason in each case.",
           "(a) 4: the CH3 of the ethyl group, the OCH2, the C=O and the CH3 on the C=O are all different. (b) 5: the C=O carbon, the ring carbon bearing COOH, the two equivalent ortho carbons, the two equivalent meta carbons and the para carbon."),
        PQ("A mass spectrum of a hydrocarbon shows M^+ at m/z 86 with relative height 100 and M+1 with relative height 6.6. How many carbon atoms does it contain? Suggest the molecular formula.",
           "Number of C = (6.6 / 100) x 100 / 1.1 = 6. For six carbon atoms and M = 86 the formula C6H14 (hexane, an alkane) fits (6 x 12 + 14 = 86)."),
        SUM("MS: M^+ gives the relative molecular mass; fragments give pieces (43 CH3CO+, 77 C6H5+, 105 C6H5CO+); Cl gives M : M+2 = 3 : 1 and Br gives 1 : 1.",
            "IR: O-H 3200-3550 (broad), acid O-H 2500-3300, C=O 1680-1750, C≡N 2200-2260, C-H 2850-3100.",
            "1H NMR: signals = environments, area = hydrogens, n + 1 rule for splitting, TMS at 0.",
            "13C NMR: one signal per carbon environment; C=O 160-220 ppm.",
            "Use degrees of unsaturation = (2C + 2 + N - H - X)/2 and check that the final structure fits all the data."),
    ])]

# ============================================================================================
# 16. Examination: Paper 1
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1: multiple-choice strategy for Upper Sixth Chemistry",
    slug="chxu-paper-1-multiple-choice-strategy", minutes=22,
    summary="Paper 1 has 50 multiple-choice questions on the whole syllabus. Learn the three question types, a time plan, a map of the six Upper Sixth modules and how to avoid the traps in calculations and statements.",
    objectives=[
        "Describe the structure of Paper 1 and the question types reported by the Board",
        "Use elimination, independent judging of statements and the assertion-reason method",
        "Plan time and mark a first pass, with a second pass for the long items",
        "Map the six Upper Sixth modules to the kinds of question asked and the common traps",
    ],
    key_concepts=["Paper 1 structure", "Single response", "Multiple selection", "Assertion and reason", "Time plan", "Calculation traps"],
    blocks=[
        H("Introduction"),
        T("Paper 1 is quick to mark but hard to prepare for, because one question can come from anywhere in the two-year course. A student in Maroua who has revised only the topics she likes will meet several she has skipped. "
          "The Board's 2023 report says Paper 1 has 50 multiple-choice questions covering the entire Chemistry syllabus. This lesson shows you how to prepare for that breadth."),
        KEY("What the Board's 2023 report says about Paper 1", "",
            cards=[["Structure", "50 multiple-choice questions on the whole syllabus. In 2023, 36 were single-response, 9 were multiple-selection and 5 were assertion-reason."],
                   ["Balance of content", "About 40% physical and general chemistry, 28% inorganic and 32% organic. Nine questions needed calculations."],
                   ["Concepts in 2023", "They included crystal structure, halogens, standard electrode potentials, radioactivity, tests on alcohols, Group IV, reaction kinetics, complex ions, buffers, pH, enthalpy, naming amides and complexes, and nitrogen oxidation states."]]),
        T("KKEVO's Paper 1 mock A has exactly 50 four-option questions spread across all six Upper Sixth modules in proportion to their topics. Its 90-minute limit is a KKEVO practice setting that gives you about 1 minute 48 seconds per question; follow your own paper's printed instructions in the real examination."),
        H("The three question types"),
        KEY("How to attack each type", "",
            cards=[["Single response", "Cover the options and work out your own answer first, then match. Eliminate options that break a rule (units, charge, atom balance, direction of a trend). Choose the best of the remainder."],
                   ["Multiple selection", "Judge each numbered statement as true or false on its own, without looking at the answer combinations. Then pick the combination that matches your verdicts."],
                   ["Assertion and reason", "Decide whether the assertion is true, whether the reason is true, and, if both, whether the reason explains the assertion. Do the three checks in order."]]),
        CODE("A  Assertion true, reason true, and the reason explains the assertion\n"
             "B  Assertion true, reason true, but the reason does not explain the assertion\n"
             "C  Assertion true, reason false\n"
             "D  Assertion false, reason true\n"
             "E  Both false", "text", title="A common assertion-reason key (follow the key printed on your paper)"),
        H("Time plan"),
        T("In the first pass answer every question that you can finish in about one minute. Put a small mark beside long calculations and anything you doubt. In the second pass, return to the marked items. Leave a few minutes at the end to check that you have an answer for every question and that each answer is in the right place. Do not spend five minutes on one question while four easy ones wait."),
        H("A map of the Upper Sixth modules"),
        CODE("Module                          Typical Paper 1 tasks\n"
             "Reaction kinetics               order from initial rates; rate equation; half-life; Arrhenius; catalyst\n"
             "Ionic equilibria                pH of strong and weak acids; buffer pH; Ksp; indicator choice\n"
             "Electrochemistry                E cell; direction of reaction; Nernst; mass deposited (Q = It)\n"
             "s and p blocks                  Period 3 oxides; Group I, II trends; Group IV; halogens\n"
             "Transition metals               configurations; coordination number; naming; colour; ligand exchange\n"
             "Organic and spectroscopy        reagents and conditions; isomers; tests; polymers; IR, NMR, MS", "text",
             title="Revision map"),
        EX("Worked example 1: a calculation item", intro="Which is the standard cell potential of a cell made of Zn^2+/Zn (-0.76 V) and Cu^2+/Cu (+0.34 V)? A  -1.10 V   B  +0.42 V   C  +1.10 V   D  -0.42 V",
           steps=[
               S("Identify cathode and anode", text="The more positive electrode potential is the cathode (reduction): Cu^2+/Cu. Zinc is the anode."),
               S("Use the formula", math=r"E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} = +0.34 - (-0.76)"),
               S("Calculate", math=r"E^\circ_{cell} = +1.10\ \text{V}"),
               S("Choose", text="The answer is C. A is the wrong sign; B and D come from adding with the wrong signs."),
           ]),
        EX("Worked example 2: assertion and reason", intro="Assertion: Fe^2+ is oxidized to Fe^3+ more easily than Mn^2+ is oxidized to Mn^3+. Reason: Mn^2+ has a half-filled 3d sub-shell.",
           steps=[
               S("Is the assertion true?", text="Yes. Fe^2+ (3d6) loses one electron to give a half-filled 3d5 ion; Mn^2+ would lose its stable 3d5 arrangement."),
               S("Is the reason true?", text="Yes. Mn^2+ is [Ar] 3d5."),
               S("Does the reason explain the assertion?", text="Yes. The stability of the half-filled sub-shell makes Mn^2+ resistant to oxidation. Answer: A."),
           ]),
        MISTAKE("Missing a negative word", "Questions say NOT, EXCEPT or LEAST. Circle the word before you read the options. Many wrong answers are really correct statements that fail the question."),
        MISTAKE("Rounding too early or choosing the nearest option", "Keep full calculator values until the last step. If your answer is not an option, redo the calculation: examiners place distractors that come from common slips (wrong ratio, forgotten 2, wrong sign, wrong unit)."),
        TIP("Paper 1 is machine-marked and each question tests one idea, so read the question twice and match the idea to the topic list in the revision map. After each mock, write a short note on every error: wrong fact, wrong method or wrong reading of the question.", title="Exam link"),
        QUIZ("In a multiple-selection question, what should you do first?", ["Look at the answer combinations", "Decide whether each statement is true or false on its own", "Choose the longest combination", "Skip the question"], 1,
             "If you judge statements one by one first, the combinations cannot mislead you.",
             hint="What does the combination depend on?",
             feedback=["That can push you towards a convenient but wrong combination.", "", "Length is not related to correctness.", "Skipping loses a mark you could have earned."]),
        QUIZ("An assertion is true and the reason is true, but the reason does not explain the assertion. What is the answer in the common key?", ["A", "B", "C", "D"], 1,
             "B means both are true but the reason is not the correct explanation.",
             hint="Look at the key: which letter says the reason does not explain?",
             feedback=["A needs the reason to explain the assertion.", "", "C needs a false reason.", "D needs a false assertion."]),
        PQ("Why is it useful to cover the options and work out your own answer before looking at them in a calculation question?",
           "The options include distractors designed from common errors. If you work out an answer first, you are less likely to be pulled towards a plausible-looking wrong option and you can check the match."),
        PQ("A student finds the pH of 0.0050 mol/dm³ hydrochloric acid to be 2.0 by saying pH = -log(0.01). Find the correct pH and say what went wrong.",
           "[H^+] = 0.0050 mol/dm³ for the strong monoprotic acid; pH = -log10(0.0050) = 2.30. The student used 0.01 instead of 0.0050, a slip in reading the concentration."),
        PQ("Give a plan for using 90 minutes on 50 questions, including how you use your time at the end.",
           "About 60 minutes on a first pass answering everything that can be done in about one minute and marking the long or uncertain items; about 25 minutes on the marked items; the last 5 minutes to check that every question has an answer and that answers are in the right boxes."),
        SUM("Paper 1 has 50 multiple-choice questions on the whole syllabus; in 2023 they were mostly single-response, with some multiple-selection and assertion-reason.",
            "Single response: predict, then match; multiple selection: judge each statement alone; assertion-reason: check the assertion, the reason, then the link.",
            "Plan time: first pass for sure answers, second pass for long calculations, and a final check.",
            "Use the module map to revise: kinetics, ionic equilibria, electrochemistry, s and p blocks, transition metals, organic and spectroscopy.",
            "Read NOT, EXCEPT and LEAST; keep full calculator digits and check units."),
    ])]

# ============================================================================================
# 17. Examination: Paper 2
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2: structured theory questions in physical, inorganic and organic chemistry",
    slug="chxu-paper-2-theory-skills", minutes=24,
    summary="Paper 2 has six compulsory questions in three sections. Score by reading command words, balancing equations, showing calculations, naming reagents with conditions, drawing mechanisms and explaining with the right term.",
    objectives=[
        "Describe the structure of Paper 2 and the weaknesses the Board reported",
        "Respond correctly to command words such as state, define, explain, suggest and deduce",
        "Write balanced equations, mechanisms and reagent-and-condition answers",
        "Apply a method to deduce-the-compound questions and to calculations",
    ],
    key_concepts=["Command words", "Balanced equations", "Reagents and conditions", "Mechanisms with curly arrows", "Deduction questions", "Calculation presentation"],
    blocks=[
        H("Introduction"),
        T("Paper 2 is the written theory paper. According to the Board's 2023 report, it has six compulsory questions in three sections: Section A on physical and general chemistry (two questions), Section B on inorganic chemistry (two questions) and Section C on organic chemistry (two questions). No question can be skipped, so you must prepare in every part of the course. "
          "KKEVO's Paper 2 practice paper uses auto-markable parts only, because essays, drawings and mechanisms cannot be marked by a computer. Practise those parts on paper."),
        KEY("What the Board's 2023 report says candidates found difficult", "These are tasks, not questions, from the report; treat them as a checklist.",
            cards=[["Physical and general", "Calculating molar mass of a volatile liquid, molar gas volume from an equation, partial pressure from mole fraction, energetics, pH of weak acids, naming crystal structures, explaining how an acid buffer works."],
                   ["Inorganic", "Explaining why Fe^2+ is easily oxidized but Mn^2+ is not; equations for the amphoteric nature of beryllium oxide; solubility of Group II sulfates; the equation for chlorine disproportionating in hot concentrated potassium hydroxide."],
                   ["Organic", "Empirical and molecular formulae and a structure from them; Hofmann degradation; nitrogen test; optical isomers of an amino acid; the mechanism of alkaline hydrolysis of a haloalkane; products of phenylethanone with NaOH/I2, 2,4-DNPH and HCN; identifying C3H8O from reagents; hybridization; distinguishing tests; reagent and conditions for converting phenylamine to a diazonium salt."]]),
        H("Command words"),
        CODE("State / Name / Give   a short answer, no explanation\n"
             "Define               an exact statement of the term (learn the key definitions)\n"
             "Describe             say what happens or what you would see, in order\n"
             "Explain              give the reason, using the right chemical idea (because...)\n"
             "Suggest              apply your knowledge to an unfamiliar case\n"
             "Deduce               reach a conclusion from the data given\n"
             "Calculate            show the formula, the substitution and the answer with units\n"
             "Compare              give similarities and differences, with both sides stated", "text", title="Command words"),
        H("Equations"),
        T("Check three things before you leave an equation: (1) the formulae are correct; (2) the atoms balance; (3) the charges balance, in an ionic equation. Add state symbols when asked, and write reagents and conditions above or below the arrow. Equations for redox reactions can be built from half-equations, adding electrons to balance charge."),
        F(r"<<3Cl2 + 6KOH -> 5KCl + KClO3 + 3H2O>>"),
        T("The example above is the hot-alkali disproportionation. Balance chlorine first: 5 Cl^- and 1 ClO3^- need 6 Cl atoms."),
        H("Reagents and conditions"),
        CODE("Conversion                          Reagent                          Conditions\n"
             "alkane to chloroalkane              Cl2                              UV light\n"
             "alkene to dibromoalkane             Br2                              room temperature\n"
             "alkene to alcohol                   steam, H3PO4                     300 C, 60-70 atm\n"
             "haloalkane to alcohol               NaOH(aq)                         reflux\n"
             "haloalkane to alkene                NaOH in ethanol                  reflux\n"
             "haloalkane to nitrile               KCN in ethanol                   reflux\n"
             "nitrile to amine                    LiAlH4                           dry ether\n"
             "primary alcohol to aldehyde         K2Cr2O7 / H2SO4                  heat and distil\n"
             "primary alcohol to acid             K2Cr2O7 / H2SO4 (excess)         reflux\n"
             "secondary alcohol to ketone         K2Cr2O7 / H2SO4                  heat\n"
             "aldehyde/ketone to hydroxynitrile   KCN, dilute H2SO4                room temperature\n"
             "aldehyde/ketone to alcohol          NaBH4                            room temperature\n"
             "carboxylic acid to ester            alcohol, conc. H2SO4             reflux\n"
             "carboxylic acid to acyl chloride    SOCl2                            room temperature\n"
             "benzene to nitrobenzene             conc. HNO3 / conc. H2SO4         50-55 C\n"
             "benzene to bromobenzene             Br2, FeBr3                       room temperature, dark\n"
             "nitrobenzene to phenylamine         Sn / conc. HCl, then NaOH        reflux\n"
             "phenylamine to diazonium salt       NaNO2 / HCl                      0-5 C\n"
             "amide to amine (one C fewer)        Br2 / NaOH(aq)                   warm", "text",
             title="Reagents and conditions to learn"),
        H("Mechanisms"),
        T("A mechanism question needs three things: curly arrows starting at a lone pair or a bond and ending at an atom or a bond; partial charges (delta+, delta-) on polar bonds; and the intermediate or transition state with charges. For the nucleophilic substitution (SN2) of bromoethane by hydroxide:"),
        CODE("Step 1 (one step, SN2):   HO^- approaches the C of C-Br from the side opposite to Br\n"
             "   HO^- ..... CH3CH2 ..... Br     transition state (both HO and Br partly bonded)\n"
             "Result: CH3CH2OH + Br^-\n"
             "Arrow 1: from the lone pair on O of HO^- to the carbon.\n"
             "Arrow 2: from the C-Br bond to the Br atom.", "text", title="Mechanism for the alkaline hydrolysis of bromoethane"),
        T("Primary haloalkanes react mainly by SN2 (one step, rate depends on both reactants). Tertiary haloalkanes react by SN1 (two steps, a carbocation intermediate, rate depends on the haloalkane only). Draw the curly arrows carefully: the tail is on the electron source, the head is on the electron sink."),
        H("Deduce-the-compound questions"),
        EX("Worked example 1: C3H8O", intro="Compound X has the formula C3H8O. It reacts with sodium to give hydrogen. When X is warmed with acidified potassium dichromate(VI) and the product distilled, the product gives a silver mirror with Tollens' reagent. Identify X and write the isomers of C3H8O.",
           steps=[
               S("Isomers", text="Three isomers: propan-1-ol, propan-2-ol and methoxyethane (an ether)."),
               S("Sodium test", text="X gives hydrogen with sodium, so it is an alcohol (not the ether)."),
               S("Oxidation product", text="The distillate gives a silver mirror, so it is an aldehyde, so X is a primary alcohol: propan-1-ol. Propan-2-ol would give propanone, which gives no silver mirror."),
               S("Equation", math=r"\mathrm{CH_3CH_2CH_2OH + [O] \rightarrow CH_3CH_2CHO + H_2O}"),
           ]),
        EX("Worked example 2: model answer to an explanation", intro="Explain why the solubility of the Group II sulfates decreases down the group.",
           steps=[
               S("Name the energy terms", text="Solubility depends on the enthalpy of solution = lattice energy (energy to separate the ions, endothermic) minus the hydration enthalpy of the ions (released)."),
               S("Anion size", text="The sulfate ion is large, so the lattice energy changes little as the cation radius increases."),
               S("Cation trend", text="The hydration enthalpy of the cation falls significantly as the ion becomes larger, because the charge density is lower."),
               S("Conclusion", text="Dissolving becomes less favourable (less exothermic), so solubility falls from MgSO4 to BaSO4."),
           ]),
        MISTAKE("Naming a reagent without its conditions", "Examiners want both. 'Sodium hydroxide' alone does not distinguish hydrolysis (aqueous, reflux) from elimination (ethanolic, reflux). 'Dichromate' needs acid and an instruction to distil or reflux."),
        MISTAKE("Vague explanations", "'It is more reactive' or 'it is stronger' is not enough. State the chemical reason: smaller ionization energy, greater polarizing power, delocalization, weaker bond, larger entropy."),
        TIP("Write your final answer to a calculation with units and with a sensible number of significant figures (usually three). Show each step so that a correct method is rewarded even if you make an arithmetic slip. Follow the instructions printed on your paper about the type of pen.", title="Exam link"),
        QUIZ("A question says 'State the reagent and conditions'. Which answer is complete for converting ethanol to ethanoic acid?", ["Potassium dichromate(VI)", "Acidified potassium dichromate(VI), heat under reflux with excess oxidizing agent", "Sulfuric acid", "Hydrogen, nickel catalyst"], 1,
             "The reagent is acidified K2Cr2O7 and the conditions are reflux with excess oxidant, so the aldehyde is oxidized further to the acid.",
             hint="You need a reagent, an acid medium and a technique.",
             feedback=["No acid and no conditions.", "", "Sulfuric acid alone does not oxidize ethanol.", "Hydrogen with nickel reduces, it does not oxidize."]),
        QUIZ("What should the head of a curly arrow in a nucleophilic attack point to?", ["The leaving group", "The atom bearing a partial positive charge", "The negative charge on the nucleophile", "Any carbon atom"], 1,
             "The electrons move towards the electron-poor atom, here the delta-positive carbon.",
             hint="Where do the electrons go?",
             feedback=["The second arrow points to the leaving group, but the first goes to carbon.", "", "The tail starts on the nucleophile's lone pair.", "It must go to the electron-poor atom."]),
        PQ("(a) Write a balanced equation for the thermal decomposition of magnesium nitrate. (b) State the colour of the gas evolved.",
           "(a) 2Mg(NO3)2 → 2MgO + 4NO2 + O2. (b) Brown nitrogen dioxide (and colourless oxygen)."),
        PQ("Outline a method to convert benzene into 4-bromonitrobenzene, giving the order of the reactions and explaining why that order is used.",
           "Brominate benzene first (Br2, FeBr3, room temperature, dark) to give bromobenzene, then nitrate (conc. HNO3 and conc. H2SO4, 50-55 °C). Bromine is 2,4-directing, so the nitro group enters the 2- and 4-positions and the 4-isomer is separated. If benzene were nitrated first, the nitro group (3-directing) would give 3-bromonitrobenzene on bromination."),
        PQ("Distinguish chemically, with observations, between (a) ethane and ethene and (b) propanal and propanone.",
           "(a) Shake with bromine water (or bubble through it): ethene decolourizes it (orange to colourless); ethane does not. (b) Warm with Tollens' reagent: propanal gives a silver mirror; propanone gives none. (Fehling's: propanal gives a red-brown precipitate; propanone gives none.)"),
        SUM("Paper 2 has six compulsory questions in three sections: physical and general, inorganic and organic; prepare in every part.",
            "Read the command word: state is short, explain needs a reason, calculate needs working and units.",
            "Balance atoms and charges in equations; write reagents and conditions for every organic conversion.",
            "Draw mechanisms with curly arrows from electron sources to electron sinks.",
            "Use the data in deduction questions step by step: formula, degrees of unsaturation, tests, structure."),
    ])]

# ============================================================================================
# 18. Examination: Paper 3 (practical skills)
# ============================================================================================
LESSONS += [lesson(
    module=M_EXAM, topic="Paper 3",
    title="Paper 3: titration, qualitative analysis and practical skills",
    slug="chxu-paper-3-practical-skills", minutes=25,
    summary="Paper 3 tests your hands-on skills: a quantitative task (a titration with calculations) and a qualitative task (identifying inorganic and organic unknowns by their reactions), plus school-based work.",
    objectives=[
        "Carry out and record a titration correctly, calculate concentrations and percentage purity, and estimate uncertainties",
        "Identify common cations, anions and gases from standard tests and record observations separately from inferences",
        "Identify organic functional groups with standard tests, including tests for N, S and halogens",
        "Prepare for the school-based assessment and work well in a school laboratory with limited resources",
    ],
    key_concepts=["Titration technique", "Concordant results", "Percentage uncertainty", "Qualitative analysis", "Observation and inference", "Organic functional group tests", "School-based assessment"],
    blocks=[
        H("Introduction"),
        T("The Board's 2023 report says Paper 3 has two questions: Question 1 on quantitative analysis and Question 2 on qualitative analysis. In 2023 the quantitative question was a redox titration, and in the qualitative question each candidate received two inorganic compounds and one organic compound to identify. Alongside the paper there is a school-based assessment of your laboratory book and a school project or field trip report. "
          "Candidates are assessed on practical skills rather than theory, and the report urges schools to begin practical work in Lower Sixth. This lesson gives you a checklist to practise at every opportunity."),
        H("Quantitative analysis: the titration"),
        KEY("Good technique", "",
            cards=[["Preparing", "Rinse the burette with the solution it will contain, and the pipette with the solution it will measure; rinse the conical flask with distilled water only. Remove the funnel and check that the jet is filled and there is no air bubble."],
                   ["Reading", "Read the bottom of the meniscus at eye level, to the nearest 0.05 cm³ (two decimal places, ending in 0 or 5). Record the initial reading and the final reading before subtracting."],
                   ["Results", "Do a rough titration first, then accurate titrations until two or more titres agree within 0.10 cm³ (concordant). Average only the concordant titres."],
                   ["Endpoint", "Add the titrant dropwise near the end, swirling. Potassium manganate(VII) is its own indicator: the first faint permanent pink. For iodine and thiosulfate add starch solution near the endpoint (pale yellow): blue-black to colourless."]]),
        CODE("Titration            Rough    1       2       3\n"
             "Final reading/cm3    24.10    24.50   23.95   24.05\n"
             "Initial reading/cm3  0.00     1.00    0.50    0.50\n"
             "Titre/cm3            24.10    23.50   23.45   23.55\n"
             "Concordant? no (rough) yes     yes     yes\n"
             "Mean of concordant titres = (23.50 + 23.45 + 23.55) / 3 = 23.50 cm3", "text",
             title="A correctly recorded table (invented data)"),
        EX("Worked example 1: a manganate(VII) titration and percentage purity", intro="9.50 g of impure hydrated iron(II) ammonium sulfate, (NH4)2Fe(SO4)2.6H2O (Mr = 392), is dissolved to make 250 cm³ of solution acidified with dilute sulfuric acid. 25.0 cm³ portions need a mean titre of 23.50 cm³ of 0.0200 mol/dm³ KMnO4. Find the percentage purity of the solid.",
           steps=[
               S("Equation", math=r"<<MnO4^- + 8H^+ + 5Fe^2+ -> Mn^2+ + 4H2O + 5Fe^3+>>"),
               S("Moles of MnO4^-", math=r"0.0200 \times 0.02350 = 4.70 \times 10^{-4}\ \text{mol}"),
               S("Moles of Fe^2+ in 25.0 cm³", math=r"5 \times 4.70 \times 10^{-4} = 2.35 \times 10^{-3}\ \text{mol}"),
               S("Moles in 250 cm³", math=r"10 \times 2.35 \times 10^{-3} = 0.0235\ \text{mol}"),
               S("Mass of pure salt", math=r"0.0235 \times 392 = 9.21\ \text{g}"),
               S("Percentage purity", math=r"\dfrac{9.21}{9.50} \times 100 = 97.0\%"),
           ]),
        T("**Uncertainty.** Each burette reading has an uncertainty of about +/- 0.05 cm³, so the titre has +/- 0.10 cm³. Percentage uncertainty = (uncertainty / reading) x 100 = (0.10 / 23.50) x 100 = 0.43%. Using larger volumes reduces the percentage uncertainty."),
        T("**Why sulfuric acid?** Dilute sulfuric acid supplies the H^+ needed. Hydrochloric acid must not be used for manganate(VII) titrations, because Cl^- would be oxidized to chlorine and give a too-high titre. Nitric acid is itself an oxidizing agent and is also unsuitable."),
        H("Qualitative analysis: inorganic"),
        T("Work systematically: note colour and state of the unknown, then dissolve a little in water; test separately for the cation and the anion with fresh portions; use small amounts. **Observations** say what you see (colour, precipitate, gas, smell, temperature); **inferences** say what it shows. Write observations first and never use the name of an ion as an observation."),
        CODE("Cation   Dilute NaOH(aq)                           Excess NaOH       Dilute NH3(aq), then excess\n"
             "Ca2+     white ppt (slight)                        insoluble         no ppt (or very slight)\n"
             "Mg2+     white ppt                                 insoluble         white ppt, insoluble\n"
             "Al3+     white ppt                                 dissolves         white ppt, insoluble\n"
             "Zn2+     white ppt                                 dissolves         white ppt, dissolves\n"
             "Pb2+     white ppt                                 dissolves         white ppt, insoluble\n"
             "Cu2+     pale blue ppt                             insoluble         pale blue ppt, dissolves: deep blue\n"
             "Fe2+     green ppt, turns brown at the surface     insoluble         green ppt, insoluble\n"
             "Fe3+     red-brown ppt                             insoluble         red-brown ppt, insoluble\n"
             "NH4+     no ppt; warm: NH3 gas turns damp red litmus blue", "text",
             title="Standard cation tests (check your textbook for slight differences)"),
        T("Additional tests: Pb^2+ gives a yellow precipitate with potassium iodide and a white precipitate (soluble in hot water) with chloride; Ca^2+ gives a brick-red flame; Cu^2+ gives a blue-green flame (check your textbook); Fe^2+ turns acidified potassium manganate(VII) from purple to colourless; Fe^3+ gives a blood-red colour with thiocyanate ions."),
        CODE("Anion     Test                                     Result\n"
             "CO3 2-    add dilute acid                          effervescence; CO2 turns limewater milky\n"
             "SO4 2-    add dilute HCl, then BaCl2(aq)           white ppt of BaSO4\n"
             "Cl-       dilute HNO3, then AgNO3(aq)              white ppt, soluble in dilute NH3\n"
             "Br-       dilute HNO3, then AgNO3(aq)              cream ppt, soluble in conc. NH3\n"
             "I-        dilute HNO3, then AgNO3(aq)              yellow ppt, insoluble in NH3\n"
             "NO3 -     NaOH(aq) and Al foil, warm               NH3 gas (turns damp red litmus blue)\n"
             "SO3 2-    add dilute acid, warm                    SO2: turns acidified K2Cr2O7 orange to green\n"
             "S2O3 2-   add dilute acid                          yellow precipitate (sulfur) and SO2\n"
             "CrO4 2-   yellow solution; add dilute acid         turns orange (Cr2O7 2-)", "text",
             title="Standard anion tests"),
        F(r"<<S2O3^2- + 2H^+ -> S + SO2 + H2O>>"),
        F(r"<<CO3^2- + 2H^+ -> CO2 + H2O>>"),
        F(r"<<NH4^+ + OH^- -> NH3 + H2O>>"),
        T("**Gas tests.** Hydrogen: burns with a squeaky pop. Oxygen: relights a glowing splint. Carbon dioxide: turns limewater milky. Ammonia: turns damp red litmus blue and has a sharp smell. Chlorine: bleaches damp litmus; greenish-yellow. Sulfur dioxide: turns acidified potassium dichromate(VI) from orange to green. Hydrogen chloride: steamy fumes, forms white smoke with ammonia."),
        EX("Worked example 2: identify the unknown", intro="Solution U gives a pale blue precipitate with a little sodium hydroxide that does not dissolve in excess. With ammonia, a pale blue precipitate forms that dissolves in excess to give a deep blue solution. U gives a white precipitate with barium chloride in the presence of dilute hydrochloric acid. Identify U and write a record of observations and inferences.",
           steps=[
               S("Cation", text="Observation: pale blue precipitate, insoluble in excess NaOH, deep blue solution in excess NH3. Inference: Cu^2+ is present, forming [Cu(NH3)4(H2O)2]^2+."),
               S("Anion", text="Observation: white precipitate with BaCl2 and HCl. Inference: SO4^2- is present; the precipitate is BaSO4."),
               S("Conclusion", text="U is copper(II) sulfate, CuSO4."),
           ]),
        H("Qualitative analysis: organic"),
        CODE("Functional group      Test                                   Positive result\n"
             "Alkene               bromine water                          orange to colourless\n"
             "Alkene               acidified KMnO4                        purple to colourless\n"
             "Alcohol              sodium                                 bubbles of H2\n"
             "1o/2o alcohol        acidified K2Cr2O7, warm                orange to green\n"
             "Phenol               neutral FeCl3                          violet colour\n"
             "Aldehyde             Tollens', warm                         silver mirror\n"
             "Aldehyde             Fehling's, heat                        red-brown precipitate\n"
             "Aldehyde or ketone   2,4-DNPH                               orange precipitate\n"
             "CH3CO- or CH3CH(OH)- I2 and NaOH, warm                      yellow precipitate (smell of antiseptic)\n"
             "Carboxylic acid      Na2CO3(aq)                             effervescence of CO2\n"
             "Haloalkane           warm with NaOH(aq), acidify with HNO3,  white, cream or yellow ppt\n"
             "                     add AgNO3", "text", title="Organic tests"),
        T("**Sodium fusion (Lassaigne) tests.** Heat the organic solid with sodium and dissolve the fusion extract in water. Nitrogen: add iron(II) sulfate solution, boil, cool, then acidify with dilute sulfuric acid (a drop of iron(III) chloride may be added); a blue colour (Prussian blue) shows nitrogen. Sulfur: add lead(II) ethanoate solution; a black precipitate of lead(II) sulfide shows S. Halogens: acidify with dilute nitric acid and add silver nitrate; white, cream or yellow precipitates show Cl, Br or I."),
        T("**Special acids.** Methanoic acid (HCOOH) is an acid (it fizzes with carbonate) and is also a reducing agent, because it contains an aldehyde-type H-C=O: it decolourizes acidified potassium manganate(VII) and gives a silver mirror with Tollens' reagent, which other carboxylic acids do not. Benzoic acid is a white solid that fizzes with carbonate and does not decolourize bromine water. Maleic acid (cis-butenedioic acid) is a diacid with C=C: it fizzes with carbonate and decolourizes bromine water."),
        H("School-based assessment and school-laboratory realities"),
        T("The school-based assessment is the evaluation of your laboratory book and your school project or field trip report. Keep your laboratory book up to date: date every experiment, write aim, method, results table, calculation and conclusion, and have it checked. Choose a project you can complete and that gives measured data; show your own results, graphs and a conclusion."),
        T("In a school laboratory with limited equipment, you may share a burette or a balance, or have only a few indicators. Plan before you start, label every bottle, avoid contamination (do not return reagents to the stock bottle), use distilled water not tap or rain water for solutions, and keep a clean white tile for seeing the endpoint. If a Bunsen burner is unavailable, a water bath can heat solutions safely. Wear eye protection and follow the teacher's safety rules."),
        MISTAKE("Using the name of an ion as an observation", "Write 'a pale blue precipitate forms' as the observation, then 'Cu^2+ is present' as the inference. Marks are given separately and the observation must be what you could see."),
        MISTAKE("Averaging all titres, including the rough one", "Use only concordant results (within 0.10 cm³ of each other), and not the rough titration. Record burette readings to two decimal places."),
        TIP("The Board's 2023 report says candidates did better in the qualitative question than in the quantitative one, and it lists the skills tested in the quantitative question: weighing, measuring volumes with a burette, pipette and other glassware, seeing the endpoint colour change, reading the glassware, recording data and calculating concentrations. Practise a full titration with a results table at least once a month. Paper 3 is a practical paper: there is no mock for it here, but the practice set tests the skills.", title="Exam link"),
        QUIZ("Which observation for a cation test is written correctly?", ["Contains copper ions", "A pale blue precipitate forms that does not dissolve in excess sodium hydroxide", "Copper(II) hydroxide is formed", "The solution is positive for copper"], 1,
             "An observation records what you can see. The inference (Cu^2+) is written separately.",
             hint="Which one describes only what is seen?",
             feedback=["This is an inference.", "", "This is a conclusion about the product.", "This is not an observation."]),
        QUIZ("Why must hydrochloric acid not be used to acidify a titration with potassium manganate(VII)?", ["It is too weak an acid", "Chloride ions are oxidized by manganate(VII), giving a too-large titre", "It reacts with the burette", "It makes the colour change impossible to see"], 1,
             "MnO4^- oxidizes Cl^- to Cl2, so extra manganate(VII) is used and the titre is too high.",
             hint="Which ion in HCl can be oxidized?",
             feedback=["HCl is a strong acid.", "", "Glass is not attacked by dilute HCl.", "The colour change is still visible."]),
        PQ("A student records burette readings to one decimal place and averages all four titres including the rough one. State two errors and the correct procedure.",
           "(i) Readings should be to two decimal places (to the nearest 0.05 cm³). (ii) The rough titration is not averaged; only concordant titres (within 0.10 cm³ of each other) are averaged. Correct procedure: record initial and final readings to 0.05 cm³, do the rough titration first, repeat until two or three titres agree, and average the concordant ones."),
        PQ("Solution V gives a white precipitate with sodium hydroxide that dissolves in excess, and a white precipitate with ammonia that dissolves in excess. Name the cation and write the ionic equation for the first precipitate.",
           "The cation is Zn^2+ (aluminium and lead precipitates do not dissolve in excess ammonia). Zn^2+ + 2OH^- → Zn(OH)2."),
        PQ("Compound W is a colourless liquid. It fizzes with sodium carbonate, decolourizes acidified potassium manganate(VII) and gives a silver mirror with Tollens' reagent. Identify W and explain.",
           "W is methanoic acid, HCOOH. It is an acid (fizzing with carbonate), and also has an aldehyde-type H-C=O group, so it reduces manganate(VII) and Tollens' reagent."),
        PQ("In a titration 25.0 cm³ of 0.0500 mol/dm³ sodium thiosulfate needs 22.50 cm³ of iodine solution. The equation is I2 + 2S2O3^2- → 2I^- + S4O6^2-. Calculate the concentration of iodine.",
           "n(S2O3^2-) = 0.0500 x 0.0250 = 1.25 x 10^-3 mol. n(I2) = 1.25 x 10^-3 / 2 = 6.25 x 10^-4 mol. c = 6.25 x 10^-4 / 0.02250 = 0.0278 mol/dm³."),
        SUM("Titration: rinse correctly, read to 0.05 cm³, record initial and final readings, rough titre first, average concordant titres within 0.10 cm³.",
            "Use H2SO4 (not HCl) for manganate(VII); add starch near the endpoint in iodine-thiosulfate titrations.",
            "Qualitative analysis: observations first (colour, precipitate, gas), then inferences; learn the NaOH and NH3 table.",
            "Organic tests: bromine water, Tollens', Fehling's, 2,4-DNPH, FeCl3, iodoform, carbonate; Lassaigne for N, S, halogens.",
            "Keep a complete laboratory book and a real project for the school-based assessment."),
    ])]


def _merge(blocks):
    """Join runs of untitled formula blocks into one block and runs of untitled text blocks into one block."""
    out = []
    for b in blocks:
        p = out[-1] if out else None
        if p and b["block_type"] == "formula" and p["block_type"] == "formula" and not b["title"] and not p["title"]:
            if p["body"].startswith(r"\begin{gathered}"):
                p["body"] = p["body"][:-len(r"\end{gathered}")] + r" \\[6pt] " + b["body"] + r"\end{gathered}"
            else:
                p["body"] = r"\begin{gathered}" + p["body"] + r" \\[6pt] " + b["body"] + r"\end{gathered}"
        elif p and b["block_type"] == "text" and p["block_type"] == "text" and not b["title"] and not p["title"]:
            p["body"] = p["body"] + "\n\n" + b["body"]
        else:
            out.append(b)
    return out


LESSONS = _walk(LESSONS)
for _lesson in LESSONS:
    _lesson["blocks"] = _merge(_lesson["blocks"])
