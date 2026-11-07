"""Upper Sixth Chemistry (A Level 0715): practice sets for Inorganic Periodic Chemistry (s & p blocks), Transition Metal &
Coordination Chemistry, Advanced Organic Synthesis & Spectroscopy and the Examination module.

Draft content built from KKEVO's master curriculum blueprint, not a Board syllabus booklet. The only exam facts used are
those of the Board's 2023 report (Paper 1: 50 multiple-choice questions; Paper 2: six compulsory questions in sections
A physical/general, B inorganic, C organic; Paper 3: quantitative and qualitative analysis plus school-based assessment).
The two mock papers use KKEVO practice settings: Paper 1 mock A has exactly 50 four-option questions spread over all six
Upper Sixth modules in proportion to their topic counts; Paper 2 practice paper A has auto-markable parts only (essays and
mechanisms cannot be marked automatically). Numbers were checked by script.
Atomic masses: H 1, C 12, N 14, O 16, Na 23, Mg 24, Al 27, Si 28, P 31, S 32, Cl 35.5, K 39, Ca 40, Cr 52, Mn 55, Fe 56,
Cu 63.5, Zn 65, Br 80, Ag 108, I 127. Notation: [[CH4]] is a formula in running text (see fx() at the bottom of the file).
"""

import random
import re

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "upper-sixth")

M_P = "Inorganic Periodic Chemistry: s & p Blocks"
M_T = "Transition Metal & Coordination Chemistry"
M_O = "Advanced Organic Synthesis & Spectroscopy"
M_EXAM = "Examination"
M_K = "Reaction Kinetics"
M_I = "Ionic Equilibria"
M_E = "Electrochemistry"

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


class _Bag:
    """Gives the position of the correct option so that A-D are used evenly."""

    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.items = []

    def next(self):
        if not self.items:
            self.items = [0, 1, 2, 3]
            self.rng.shuffle(self.items)
        return self.items.pop()


BAG = _Bag(1)


def use(seed):
    global BAG
    BAG = _Bag(seed)


def Q(prompt, correct, wrongs, steps, concept, skill, hint, pos=None):
    """Four-option MC. `wrongs` = [(text, why)] x3; the correct option goes to a balanced position."""
    assert len(wrongs) == 3
    pos = BAG.next() if pos is None else pos
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(correct, correct=True))
    return MC(prompt, choices, steps=[S(a, text=b) for a, b in steps], concept=concept, skill=skill, hint=hint)


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit=""):
    return NUM(prompt, answer, steps=[S(a, text=b) for a, b in steps], tolerance=tol, unit=unit, concept=concept,
               skill=skill, hint=hint)


SETS = []

# ============================================================================================
# 1. Periodicity across Period 3
# ============================================================================================
use(201)
T1 = "Periodicity across Period 3"
SET1 = [
    Q("What happens to the atomic radius across Period 3 from sodium to chlorine?",
      "It decreases, because the nuclear charge increases while the outer electrons stay in the same shell",
      [("It increases, because more electrons are added", "The extra electrons go into the same shell (n = 3), so they do not add a new shell."),
       ("It stays constant, because the shell is the same", "The nuclear charge rises, pulling the electrons in; the radius does not stay constant."),
       ("It decreases, because the shielding increases strongly", "Shielding by inner shells stays almost the same across a period; the rising nuclear charge is the reason.")],
      [("Compare nuclear charge and shielding", "Protons rise from 11 to 17 but the shielding by inner shells is almost unchanged, so the effective nuclear charge grows and the radius falls.")],
      T1, "Concept", "Think about what changes and what stays the same across the period."),
    Q("Which Period 3 oxide dissolves in water to give a solution of pH 14?",
      "[[Na2O]]", [("[[MgO]]", "MgO is only slightly soluble and gives about pH 9-10."), ("[[Al2O3]]", "Al2O3 is insoluble in water."), ("[[SO2]]", "SO2 gives an acidic solution (H2SO3).")],
      [("Identify the basic soluble oxide", "Na2O is ionic and reacts completely with water: Na2O + H2O -> 2NaOH, a strong alkali.")],
      T1, "Recall", "Which oxide is most ionic?"),
    Q("Which equation shows the amphoteric nature of aluminium oxide?",
      "[[Al2O3 + 2NaOH + 3H2O -> 2Na[Al(OH)4] ]]",
      [("[[Al2O3 + 3H2O -> 2Al(OH)3]]", "Aluminium oxide is insoluble in water; this reaction does not occur."),
       ("[[SiO2 + 2NaOH -> Na2SiO3 + H2O]]", "This shows that silicon dioxide is acidic, not that Al2O3 is amphoteric."),
       ("[[MgO + 2HCl -> MgCl2 + H2O]]", "This shows only that magnesium oxide is basic.")],
      [("Amphoteric means acid and base behaviour", "Al2O3 reacts with acids (forming Al^3+) and with alkali (forming the aluminate ion).")],
      T1, "Concept", "An amphoteric oxide reacts with an alkali as well as an acid."),
    N("Sodium oxide (6.2 g) is added to water. Find the mass of sodium hydroxide formed. (Na = 23, O = 16, H = 1)", 8.0,
      [("Moles of Na2O", "Mr = 62, so n = 6.2 / 62 = 0.10 mol."), ("Ratio", "Na2O + H2O -> 2NaOH, so n(NaOH) = 0.20 mol."), ("Mass", "Mr(NaOH) = 40, so mass = 0.20 x 40 = 8.0 g.")],
      T1, "Calculation", "Find moles of the oxide first, then use the 1 : 2 ratio.", tol=0.05, unit="g"),
    Q("Which statement explains why the melting point of silicon is much higher than that of phosphorus?",
      "Silicon has a giant covalent structure, whereas phosphorus consists of simple [[P4]] molecules held by weak forces",
      [("Silicon has stronger London forces between its atoms", "London forces act between simple molecules; silicon has a network of covalent bonds instead."),
       ("Silicon atoms have more delocalized electrons than phosphorus atoms", "Silicon has no sea of delocalized electrons; it is a semiconductor with covalent bonds."),
       ("Silicon has a larger atomic radius than phosphorus", "The size is not the reason; the type of structure and bonding decides the melting point.")],
      [("Compare structures", "Melting Si breaks strong covalent bonds throughout a giant lattice. Melting white phosphorus only overcomes weak London forces between P4 molecules.")],
      T1, "Reasoning", "What must be broken in each substance when it melts?"),
    Q("Which pair of statements about the first ionization energies of Period 3 is correct?",
      "Al is lower than Mg because its outer electron is in a 3p orbital; S is lower than P because of electron pair repulsion in a 3p orbital",
      [("Al is lower than Mg because Al has a larger atomic radius; S is lower than P because S has more shells", "Al is smaller than Mg and S is in the same shell as P."),
       ("Al is lower than Mg because its nuclear charge is smaller; S is lower than P for the same reason", "The nuclear charge of Al and S is larger, not smaller."),
       ("Both are lower because the outer electrons are in a new shell", "No new shell is started within the period.")],
      [("Recall the two dips", "Mg to Al: 3p is higher in energy than 3s. P to S: the paired 3p electron is repelled by its partner.")],
      T1, "Reasoning", "Look at which sub-shell and which orbital the removed electron comes from."),
    Q("Solid X reacts violently with water, giving white fumes of a gas that turns blue litmus red and leaves a solution of about pH 1. Which chloride is X?",
      "[[PCl5]]", [("[[NaCl]]", "NaCl dissolves to give a neutral solution and does not fume."), ("[[MgCl2]]", "MgCl2 dissolves with a pH of about 6.5 and no fumes."), ("[[CCl4]]", "CCl4 is not a Period 3 chloride and is not hydrolysed by water.")],
      [("Match observations", "PCl5 + 4H2O -> H3PO4 + 5HCl: HCl gives the fumes and the acid solution (the equation is complete hydrolysis).")],
      T1, "Application", "Which chloride is covalent and hydrolysed?"),
    Q("Aluminium chloride exists as [[Al2Cl6]] in the vapour. What does this show?",
      "AlCl3 is covalent: it forms dative bonds from chlorine lone pairs to aluminium to complete the octet",
      [("AlCl3 is a fully ionic lattice", "An ionic lattice would not give dimer molecules in the vapour."),
       ("Aluminium has a valency of 6", "Aluminium forms three bonds; the dimer arises from dative bonds."),
       ("Chlorine atoms are bonded to each other by a double bond", "The bridge is formed by chlorine lone pairs donated to a neighbouring Al, not Cl=Cl bonds.")],
      [("Electron deficiency", "In AlCl3 the Al atom has only six outer electrons. A Cl lone pair on another molecule fills the gap, giving the dimer.")],
      T1, "Interpretation", "Count the electrons around Al in AlCl3."),
]
SETS += [practice_set(module=M_P, topic=T1, title="Period 3 trends practice", lesson="chu2-periodicity-period-3", questions=SET1)]

# ============================================================================================
# 2. Groups I and II
# ============================================================================================
use(202)
T2 = "Groups I and II"
SET2 = [
    Q("Which metal gives a lilac flame in a flame test?",
      "Potassium", [("Sodium", "Sodium gives a golden-yellow flame."), ("Lithium", "Lithium gives a crimson-red flame."), ("Calcium", "Calcium gives a brick-red flame.")],
      [("Recall", "The lilac colour is characteristic of potassium ions.")], T2, "Recall", "Think of the three Group I flame colours: red, yellow, lilac."),
    Q("Why does reactivity increase down Group I?",
      "The outer electron is further from the nucleus and better shielded, so it is lost more easily",
      [("The nuclear charge decreases down the group", "The nuclear charge increases down the group."),
       ("The atoms have more outer electrons", "All Group I atoms have one outer electron."),
       ("The ions are smaller", "The ions become larger down the group.")],
      [("Link to ionization energy", "Down the group the radius and shielding increase, the first ionization energy falls and the metals react more readily.")],
      T2, "Concept", "Think about the first ionization energy."),
    Q("Which statement about the Group II hydroxides is correct?",
      "Solubility increases from magnesium hydroxide to barium hydroxide",
      [("Solubility decreases from magnesium hydroxide to barium hydroxide", "This is the trend for the sulfates, not the hydroxides."),
       ("All the Group II hydroxides are insoluble", "Barium hydroxide is fairly soluble and gives a strongly alkaline solution."),
       ("The solubility is the same for all Group II hydroxides", "There is a clear trend down the group.")],
      [("Recall the trend", "Hydroxides: solubility rises down the group. Sulfates: solubility falls.")],
      T2, "Recall", "Hydroxides and sulfates have opposite trends."),
    Q("Which compound decomposes at the lowest temperature?",
      "[[MgCO3]]", [("[[CaCO3]]", "CaCO3 is more stable than MgCO3."), ("[[SrCO3]]", "SrCO3 is more stable than CaCO3."), ("[[BaCO3]]", "BaCO3 is the most stable carbonate in the group.")],
      [("Apply the trend", "Thermal stability of the carbonates rises down the group, so MgCO3 (smallest cation, highest polarizing power) decomposes first.")],
      T2, "Application", "Which cation polarizes the carbonate ion most?"),
    N("Calcium carbonate (5.00 g) is heated until it decomposes completely. What volume of carbon dioxide forms at room temperature and pressure (24 dm³/mol)? (Ca = 40, C = 12, O = 16)", 1.2,
      [("Moles of CaCO3", "Mr = 100, so n = 5.00 / 100 = 0.0500 mol."), ("Moles of CO2", "[[CaCO3 -> CaO + CO2]] is a 1 : 1 ratio: 0.0500 mol."), ("Volume", "0.0500 x 24 = 1.20 dm³.")],
      T2, "Calculation", "Use the 1 : 1 ratio and the molar volume at rtp.", tol=0.01, unit="dm³"),
    Q("Which equation correctly shows the products of heating magnesium nitrate?",
      "[[2Mg(NO3)2 -> 2MgO + 4NO2 + O2]]",
      [("[[Mg(NO3)2 -> Mg(NO2)2 + O2]]", "The nitrite is the product for sodium and potassium nitrates only."),
       ("[[Mg(NO3)2 -> Mg + 2NO2 + O2]]", "The metal is not produced; the oxide forms."),
       ("[[2Mg(NO3)2 -> 2MgO + 2NO2 + O2]]", "Not balanced for nitrogen and oxygen: 2 NO3 groups per formula need 4 NO2 in total from two formula units.")],
      [("Group II pattern", "Group II nitrates give the oxide, nitrogen dioxide (brown gas) and oxygen. The equation balances with 4NO2: N 4 = 4, O 12 = 2 + 8 + 2.")],
      T2, "Application", "Which pattern do Group II nitrates follow: nitrite or oxide?"),
    Q("Lithium carbonate decomposes at a Bunsen burner temperature but sodium carbonate does not. What is the best explanation?",
      "The Li^+ ion is small and has a high charge density, so it polarizes the carbonate ion more strongly",
      [("Lithium is less reactive than sodium", "Lithium is a reactive metal; the explanation lies in cation size, not reactivity."),
       ("Lithium has a higher relative atomic mass than sodium", "Li (7) has a lower relative atomic mass than Na (23)."),
       ("The carbonate ion in lithium carbonate is larger", "The carbonate ion is the same in both compounds.")],
      [("Diagonal relationship", "Li^+ is small, so its charge density is large (like Mg^2+). It distorts the CO3^2- ion, which then breaks into the oxide and CO2.")],
      T2, "Reasoning", "Compare the sizes of Li^+ and Na^+."),
    Q("Which pair of elements shows a diagonal relationship?",
      "Beryllium and aluminium", [("Sodium and magnesium", "These are neighbours in a period, not a diagonal pair."), ("Lithium and sodium", "These are in the same group."), ("Beryllium and calcium", "These are in the same group.")],
      [("Identify the diagonal", "A diagonal pair is the first element of one group and the second element of the next: Li-Mg and Be-Al. Both Be and Al form amphoteric oxides.")],
      T2, "Recall", "Look one group to the right and one period down."),
]
SETS += [practice_set(module=M_P, topic=T2, title="Groups I and II trends practice", lesson="chu2-groups-i-and-ii", questions=SET2)]

# ============================================================================================
# 3. Group IV
# ============================================================================================
use(203)
T3 = "Group IV"
SET3 = [
    Q("Which element in Group IV is a typical metal?",
      "Lead", [("Carbon", "Carbon is a non-metal."), ("Silicon", "Silicon is a metalloid (semiconductor)."), ("Germanium", "Germanium is a metalloid.")],
      [("Recall the trend", "Metallic character increases down the group: C non-metal, Si and Ge metalloids, Sn and Pb metals.")],
      T3, "Recall", "Metallic character rises down a group."),
    Q("Which oxidation state becomes more stable down Group IV?",
      "+2", [("+4", "The +4 state becomes less stable down the group."), ("0", "Zero is the oxidation state of the element itself."), ("-4", "-4 occurs in carbides and silicides but is not the trend described by the inert pair effect.")],
      [("Inert pair effect", "The ns2 electrons are increasingly reluctant to take part in bonding, so +2 (the pair retained) is favoured by Sn and Pb.")],
      T3, "Concept", "Which state keeps the ns2 pair?"),
    Q("Which compound is the strongest oxidizing agent?",
      "[[PbO2]]", [("[[SnO2]]", "Sn(IV) is fairly stable and is not strongly oxidizing."), ("[[CO2]]", "CO2 is not an oxidizing agent under normal conditions."), ("[[SiO2]]", "SiO2 is very stable and unreactive.")],
      [("Apply the inert pair effect", "Pb(IV) readily gains two electrons to become the stable Pb(II).")],
      T3, "Application", "Which element's +4 state is least stable?"),
    Q("What is the correct equation for the reaction of lead(IV) oxide with concentrated hydrochloric acid?",
      "[[PbO2 + 4HCl -> PbCl2 + Cl2 + 2H2O]]",
      [("[[PbO2 + 4HCl -> PbCl4 + 2H2O]]", "PbCl4 is unstable; Pb(IV) is reduced to Pb(II) and chloride is oxidized."),
       ("[[PbO2 + 2HCl -> PbCl2 + H2O2]]", "H2O2 is not formed; chlorine is the oxidation product."),
       ("[[PbO2 + 2HCl -> Pb + Cl2 + H2O2]]", "Lead metal is not formed.")],
      [("Check the redox", "Pb: +4 to +2 (reduced); Cl: -1 to 0 (oxidized). Atoms: Pb 1, O 2, H 4, Cl 4 on both sides.")],
      T3, "Application", "Pb(IV) is reduced; what is oxidized?"),
    Q("Why is silicon tetrachloride hydrolysed by water but carbon tetrachloride is not?",
      "Silicon has accessible 3d orbitals that can accept a lone pair from water; carbon has no suitable orbitals",
      [("The Si-Cl bond is non-polar", "The Si-Cl bond is more polar than C-Cl, which helps hydrolysis."),
       ("SiCl4 has a lower molar mass than CCl4", "SiCl4 (Mr 170) is heavier than CCl4 (Mr 154), and molar mass does not decide whether water can attack the molecule."),
       ("Carbon is more electronegative than chlorine", "Chlorine is more electronegative than carbon.")],
      [("Explain with orbitals", "Water donates a lone pair to silicon's empty 3d orbitals. Carbon cannot expand its octet because it has no d orbitals in the second shell.")],
      T3, "Reasoning", "Think about what water needs to attack the central atom."),
    N("What is the oxidation state of lead in [[PbO2]]?", 4,
      [("Oxygen is -2", "In PbO2, 2 x (-2) = -4."), ("Balance", "Pb + 2(-2) = 0 gives Pb = +4.")],
      T3, "Calculation", "Oxygen is -2 and the compound is neutral."),
    Q("Which statement about the Group IV elements is correct?",
      "The melting point of tin is much lower than that of silicon because tin is held by weaker metallic bonding, whereas silicon is held by strong covalent bonds",
      [("Tin has a higher melting point than silicon because it is more metallic", "Giant covalent silicon has a much higher melting point than tin."),
       ("Diamond conducts because it has delocalized electrons", "Diamond has none; graphite conducts."),
       ("All Group IV elements form stable +4 chlorides", "PbCl4 is unstable.")],
      [("Compare bonding", "Silicon: strong covalent bonds throughout. Tin: metallic bonding with large ions and few delocalized electrons per atom.")],
      T3, "Interpretation", "Compare the strengths of the bonds that are broken on melting."),
    Q("Lead(II) hydroxide dissolves in excess sodium hydroxide solution. What does this show?",
      "Lead(II) hydroxide is amphoteric", [("Lead(II) hydroxide is acidic only", "It also reacts with acids to give Pb^2+ salts."), ("Lead(II) hydroxide is basic only", "It also dissolves in excess alkali, so it is not basic only."), ("Lead is oxidized to Pb(IV)", "The oxidation state of lead stays at +2 in the plumbate(II) ion.")],
      [("Interpret", "A hydroxide that reacts with both acid and alkali is amphoteric: Pb(OH)2 + 2OH^- gives [Pb(OH)4]^2-.")],
      T3, "Interpretation", "What type of hydroxide dissolves in both acid and alkali?"),
]
SETS += [practice_set(module=M_P, topic=T3, title="Group IV trends and the inert pair effect practice", lesson="chu2-group-iv", questions=SET3)]

# ============================================================================================
# 4. Group VII
# ============================================================================================
use(204)
T4 = "Group VII"
SET4 = [
    Q("What is the colour of iodine vapour?",
      "Purple", [("Pale yellow", "Pale yellow is the colour of fluorine gas."), ("Greenish-yellow", "Greenish-yellow is chlorine gas."), ("Red-brown", "Red-brown is liquid bromine (its vapour is orange-brown).")],
      [("Recall", "Solid iodine is grey-black and sublimes to a purple vapour.")], T4, "Recall", "Think of iodine on gentle heating."),
    Q("Which trend is correct down Group VII from chlorine to iodine?",
      "The oxidizing power decreases", [("The oxidizing power increases", "Iodine is the weakest oxidizing agent of the three."), ("The boiling point decreases", "The boiling point increases as London forces strengthen."), ("The electronegativity increases", "Electronegativity decreases as the atoms get bigger.")],
      [("Recall", "Standard electrode potentials: Cl2 +1.36 V, Br2 +1.07 V, I2 +0.54 V; boiling point rises; electronegativity falls.")],
      T4, "Recall", "Compare the electrode potentials."),
    Q("Chlorine water is added to potassium bromide solution. What is observed and what is the reason?",
      "The solution turns orange-brown because chlorine oxidizes bromide ions to bromine",
      [("The solution turns purple because iodine is formed", "No iodine is present; bromide ions are oxidized."),
       ("There is no change because chlorine is less reactive than bromine", "Chlorine is the stronger oxidizing agent and displaces bromine."),
       ("A white precipitate forms because silver chloride is made", "No silver ions are present.")],
      [("Displacement", "Cl2 + 2Br^- -> 2Cl^- + Br2; the more reactive halogen displaces the less reactive from its salt.")],
      T4, "Application", "Which halogen is the stronger oxidizing agent?"),
    Q("A white solid reacts with concentrated sulfuric acid to give steamy white fumes only, with no coloured vapour. Which anion is present?",
      "Chloride", [("Bromide", "Bromide would also give red-brown bromine and SO2."), ("Iodide", "Iodide would give purple vapour, a yellow solid and H2S."), ("Carbonate", "Carbonate would give colourless, odourless carbon dioxide (effervescence), not steamy fumes of an acidic gas.")],
      [("Match the observation", "Cl^- is too weak a reducing agent to reduce H2SO4, so HCl fumes form alone.")],
      T4, "Application", "Which halide is the weakest reducing agent?"),
    N("25.0 cm³ of 0.200 mol/dm³ sodium bromide is treated with excess silver nitrate. Find the mass in grams of silver bromide formed. (Ag = 108, Br = 80)", 0.94,
      [("Moles of Br^-", "0.200 x 0.0250 = 0.00500 mol."), ("Moles of AgBr", "Ratio 1 : 1, so 0.00500 mol."), ("Mass", "Mr(AgBr) = 188, so mass = 0.00500 x 188 = 0.940 g.")],
      T4, "Calculation", "Find the moles of bromide, then use the 1 : 1 ratio.", tol=0.01, unit="g"),
    Q("Which silver halide dissolves in dilute ammonia solution?",
      "[[AgCl]]", [("[[AgBr]]", "AgBr needs concentrated ammonia."), ("[[AgI]]", "AgI does not dissolve even in concentrated ammonia."), ("All three dissolve", "Only AgCl dissolves in dilute ammonia solution.")],
      [("Recall", "AgCl dissolves in dilute NH3; AgBr in concentrated NH3; AgI in neither.")], T4, "Recall", "The solubility falls from Cl to I."),
    Q("In which reaction does chlorine undergo disproportionation?",
      "[[3Cl2 + 6KOH -> 5KCl + KClO3 + 3H2O]]",
      [("[[Cl2 + 2KI -> 2KCl + I2]]", "Here chlorine is only reduced (0 to -1); it is not also oxidized."),
       ("[[H2 + Cl2 -> 2HCl]]", "Chlorine is reduced only; hydrogen is oxidized."),
       ("[[2Na + Cl2 -> 2NaCl]]", "Chlorine is reduced only.")],
      [("Look for one element going up and down", "In the first equation Cl goes from 0 to -1 (in KCl) and from 0 to +5 (in KClO3).")],
      T4, "Concept", "Find the equation where chlorine ends in two different oxidation states."),
    Q("Why is hydrofluoric acid a weaker acid than hydrochloric acid?",
      "The H-F bond is very strong and hydrogen bonding makes dissociation less favourable",
      [("Fluorine is less electronegative than chlorine", "Fluorine is the most electronegative element."),
       ("The H-F bond is longer than the H-Cl bond", "H-F is shorter than H-Cl, which makes it stronger."),
       ("Fluoride ions are larger than chloride ions", "Fluoride is smaller than chloride.")],
      [("Compare bond strength", "The H-F bond enthalpy (about 562 kJ/mol) is much greater than that of H-Cl (about 431 kJ/mol); hydrogen bonding in solution also opposes dissociation.")],
      T4, "Reasoning", "Compare the bond enthalpies."),
]
SETS += [practice_set(module=M_P, topic=T4, title="Halogens, halides and chlorine oxoacids practice", lesson="chu2-group-vii", questions=SET4)]

# ============================================================================================
# 5. Properties of the 3d elements
# ============================================================================================
use(205)
T5 = "Properties of the 3d elements"
SET5 = [
    Q("Which statement defines a transition element?",
      "A d-block element that forms at least one ion with a partially filled d sub-shell",
      [("Any element in the d block", "Zinc and scandium are d-block elements but their ions have empty or full d sub-shells."),
       ("An element that forms coloured compounds", "Colour is a property, not the definition; the definition is based on the electrons."),
       ("A metal with a high melting point", "Many non-transition metals also have high melting points.")],
      [("Recall", "The definition is based on the electronic structure of the ion.")], T5, "Recall", "Look at the d sub-shell of the ion."),
    Q("What is the electronic configuration of the [[Fe^2+]] ion? (Fe: atomic number 26)",
      "[Ar] 3d6", [("[Ar] 3d4 4s2", "The 4s electrons are lost first when ions form."), ("[Ar] 3d5 4s1", "Electrons are removed from 4s before 3d."), ("[Ar] 3d8", "Two electrons are removed, not added.")],
      [("Remove 4s first", "Fe: [Ar] 3d6 4s2. Remove the two 4s electrons to give Fe^2+: [Ar] 3d6.")],
      T5, "Concept", "Which electrons leave the atom first?"),
    Q("Which ion is colourless in solution?",
      "[[Zn^2+]]", [("[[Cu^2+]]", "Cu^2+ is blue."), ("[[Fe^3+]]", "Fe^3+ is yellow-brown."), ("[[Ni^2+]]", "Ni^2+ is green.")],
      [("Check the d sub-shell", "Zn^2+ is 3d10, a full sub-shell, so there are no d-d transitions and the ion is colourless.")],
      T5, "Recall", "Which ion has a full 3d sub-shell?"),
    Q("Why is [[Mn^2+]] much harder to oxidize to [[Mn^3+]] than [[Fe^2+]] is to [[Fe^3+]]?",
      "Mn^2+ has a half-filled 3d5 sub-shell, which is extra stable",
      [("Mn^2+ has a full 3d sub-shell", "Mn^2+ is 3d5, which is half-filled, not full."),
       ("Mn is a non-metal", "Manganese is a transition metal."),
       ("Mn^2+ has no d electrons", "Mn^2+ has five 3d electrons.")],
      [("Compare configurations", "Fe^2+ (3d6) loses an electron to become 3d5; Mn^2+ is already 3d5 and would lose that stability.")],
      T5, "Reasoning", "Write down the 3d configurations of both ions."),
    N("In a titration, 25.0 cm³ of Fe^2+ solution needs 22.50 cm³ of 0.0200 mol/dm³ KMnO4. What is the concentration of Fe^2+ in mol/dm³? (MnO4^- reacts with Fe^2+ in the ratio 1 : 5)", 0.09,
      [("Moles of MnO4^-", "0.0200 x 0.02250 = 4.50 x 10^-4 mol."), ("Moles of Fe^2+", "5 x 4.50 x 10^-4 = 2.25 x 10^-3 mol."), ("Concentration", "2.25 x 10^-3 / 0.0250 = 0.0900 mol/dm³.")],
      T5, "Calculation", "Use the 1 : 5 ratio to convert the manganate(VII) moles.", tol=0.001, unit="mol/dm³"),
    Q("Which metal and use are correctly paired as a catalyst?",
      "Iron in the Haber process", [("Copper in the Contact process", "The Contact process uses vanadium(V) oxide."), ("Vanadium in the hydrogenation of oils", "Hydrogenation uses nickel."), ("Nickel in the Haber process", "The Haber process uses iron.")],
      [("Recall", "Haber: Fe. Contact: V2O5. Hydrogenation: Ni.")], T5, "Recall", "Match each catalyst to its process."),
    Q("Which ion is paramagnetic?",
      "[[Fe^3+]]", [("[[Zn^2+]]", "Zn^2+ is 3d10: all electrons are paired."), ("[[Cu^+]]", "Cu^+ is 3d10: all electrons are paired."), ("[[Sc^3+]]", "Sc^3+ is 3d0: it has no d electrons.")],
      [("Count unpaired electrons", "Fe^3+ is 3d5 with five unpaired electrons, so it is strongly paramagnetic.")],
      T5, "Application", "Which ion has unpaired d electrons?"),
    Q("What is the oxidation number of manganese in [[MnO4^-]]?",
      "+7", [("+4", "+4 is the oxidation state in MnO2."), ("+6", "+6 is the oxidation state in the manganate(VI) ion, MnO4^2-."), ("+2", "+2 is Mn^2+, the product of reduction in acid.")],
      [("Balance charge", "Mn + 4(-2) = -1, so Mn = +7.")], T5, "Calculation", "Oxygen is -2; the total charge is -1."),
]
SETS += [practice_set(module=M_T, topic=T5, title="Properties of the 3d elements practice", lesson="chu2-3d-elements-properties", questions=SET5)]

# ============================================================================================
# 6. Complex ions and ligands
# ============================================================================================
use(206)
T6 = "Complex ions and ligands"
SET6 = [
    Q("What is a ligand?",
      "A molecule or ion that donates a lone pair of electrons to a central metal ion",
      [("A molecule or ion that accepts a lone pair from a metal ion", "That describes the metal ion (a Lewis acid), not the ligand."),
       ("A transition metal ion at the centre of a complex", "That is the central metal ion."),
       ("Any negative ion in a complex", "Ligands may be neutral (H2O, NH3); what matters is that they donate a lone pair.")],
      [("Recall", "Ligands are Lewis bases that form dative covalent bonds to the metal ion.")], T6, "Recall", "Think about who gives the electron pair."),
    Q("What is the coordination number of the metal in [[ [Fe(CN)6]^4- ]]?",
      "6", [("4", "There are six cyanide ligands, not four."), ("2", "Two is the charge of the metal ion, not the number of bonds."), ("4-", "4- is the charge of the complex, not a coordination number.")],
      [("Count the bonds", "Six monodentate cyanide ligands give six dative bonds.")], T6, "Recall", "Each cyanide ligand forms one bond."),
    Q("What is the oxidation number of iron in [[ [Fe(CN)6]^4- ]]?",
      "+2", [("+3", "Check: +3 with six CN^- (-6) would give a charge of -3."), ("+4", "The charge on the complex is -4, not the oxidation number of the metal."), ("-2", "The metal ion is positive here.")],
      [("Use the charges", "x + 6(-1) = -4 gives x = +2.")], T6, "Calculation", "Charge of complex = metal + ligand charges."),
    Q("What is the name of [[ [Cu(NH3)4(H2O)2]^2+ ]]?",
      "Tetraamminediaquacopper(II)", [("Diaquatetraamminecopper(II)", "Ligands are named in alphabetical order, so ammine comes before aqua."), ("Tetraamminediaquacuprate(II)", "-ate is used only for negative complexes; this one is a cation."), ("Tetraamminediaquacopper(IV)", "The oxidation number of copper is +2.")],
      [("Apply the naming rules", "Ligands alphabetically (ammine, aqua), then the metal and its oxidation number, +2 for copper here.")],
      T6, "Application", "Alphabetical order of ligand names, ignoring prefixes."),
    Q("Which ligand is bidentate?",
      "Ethane-1,2-diamine", [("Ammonia", "Ammonia has one donor atom (monodentate)."), ("Chloride ion", "Chloride is monodentate."), ("Water", "Water is monodentate here.")],
      [("Count the donor atoms", "H2NCH2CH2NH2 has two nitrogen atoms, each with a lone pair, so it forms two bonds to the same metal ion.")],
      T6, "Concept", "Look for two atoms each with a lone pair."),
    Q("What is the coordination number of nickel in [[ [Ni(en)3]^2+ ]] where en is ethane-1,2-diamine?",
      "6", [("3", "Three ligands, but each bonds twice."), ("2", "2 is the charge on the ion."), ("9", "The ligand has two donor atoms, not three.")],
      [("Count dative bonds", "Three en ligands x two donor atoms each = 6.")], T6, "Application", "Multiply the number of ligands by the number of donor atoms."),
    Q("Which complex is tetrahedral?",
      "[[ [CoCl4]^2- ]]", [("[[ [Cu(H2O)6]^2+ ]]", "Coordination number 6: octahedral."), ("[[ [Ag(NH3)2]^+ ]]", "Coordination number 2: linear."), ("[[ [Fe(CN)6]^3- ]]", "Coordination number 6: octahedral.")],
      [("Link number to shape", "Four large chloride ligands give a tetrahedral complex with bond angles of about 109.5 degrees.")],
      T6, "Application", "Which complex has four ligands?"),
    Q("Excess dilute ammonia solution is added to copper(II) sulfate solution. What is observed at the end?",
      "A deep blue solution", [("A pale blue precipitate that does not dissolve", "The precipitate dissolves in excess ammonia to form a complex."), ("A green precipitate", "Green precipitates are characteristic of Fe^2+ or Ni^2+."), ("A colourless solution", "Colourless solutions are given by Zn^2+ in excess ammonia, not Cu^2+.")],
      [("Recall", "A pale blue precipitate of Cu(OH)2 forms first, then dissolves in excess ammonia to form deep blue [Cu(NH3)4(H2O)2]^2+.")],
      T6, "Recall", "Ammonia replaces water ligands."),
]
SETS += [practice_set(module=M_T, topic=T6, title="Complex ions, ligands and naming practice", lesson="chu2-complex-ions-ligands", questions=SET6)]

# ============================================================================================
# 7. Isomerism and colour in complexes
# ============================================================================================
use(207)
T7 = "Isomerism and colour in complexes"
SET7 = [
    Q("Which type of isomerism is shown by [[ [Pt(NH3)2Cl2] ]] (square planar)?",
      "Cis-trans (geometric) isomerism", [("Optical isomerism", "The square planar complex has a plane of symmetry, so it is not chiral."), ("Structural (chain) isomerism", "The ligands are all the same atoms in the same chains; only the arrangement in space differs."), ("It shows no isomerism", "Two isomers exist: cisplatin and transplatin.")],
      [("Identify the arrangements", "The two Cl may be adjacent (cis) or opposite (trans).")], T7, "Concept", "Where can the two chloride ligands sit?"),
    Q("What happens to the five 3d orbitals of a transition metal ion in an octahedral complex?",
      "They split into a lower set of three and a higher set of two", [("They split into a lower set of two and a higher set of three", "The three orbitals between the axes (t2g) are lower; the two pointing at the ligands (eg) are higher."), ("They all rise equally in energy", "That is true of a spherical field; ligands on axes cause a split."), ("They remain at the same energy", "That is the case only for the free ion.")],
      [("Repulsion by ligands", "Orbitals pointing at the ligands are repelled more and rise (eg); the others (t2g) are lower.")],
      T7, "Recall", "Which orbitals point directly at the ligands on the axes?"),
    Q("A solution absorbs blue light and transmits the rest. What colour does it appear?",
      "Yellow-orange", [("Blue", "Blue light is absorbed, not seen."), ("Red-violet", "Violet is not complementary to blue."), ("Colourless", "A solution that absorbs visible light is coloured.")],
      [("Use the complementary colour", "Blue light is absorbed, so the colour seen is the complementary colour, orange-yellow.")], T7, "Application", "The colour seen is opposite the absorbed colour on the wheel."),
    N("A complex has an energy gap of 3.00 x 10^-19 J between its d orbitals. Calculate the wavelength of light absorbed in nm. (h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m/s)", 663,
      [("Use lambda = hc / E", "lambda = (6.63 x 10^-34 x 3.00 x 10^8) / (3.00 x 10^-19)."), ("Calculate", "lambda = 6.63 x 10^-7 m = 663 nm (red region).")],
      T7, "Calculation", "Rearrange E = hc/lambda.", tol=1, unit="nm"),
    Q("Which ion is colourless in aqueous solution?",
      "[[Sc^3+]]", [("[[Ti^3+]]", "Ti^3+ is 3d1 and is purple."), ("[[Cr^3+]]", "Cr^3+ is 3d3 and is green or violet."), ("[[Ni^2+]]", "Ni^2+ is 3d8 and is green.")],
      [("Check for d electrons", "Sc^3+ has no d electrons (3d0), so no d-d transition occurs.")], T7, "Application", "Which ion has an empty d sub-shell?"),
    Q("Why does adding excess ammonia to aqueous copper(II) ions change the colour from pale blue to deep blue?",
      "Ammonia is a stronger-field ligand, so the d orbital splitting increases and a shorter wavelength is absorbed",
      [("Copper is reduced to copper(I)", "The oxidation state does not change; ligands are exchanged."),
       ("Ammonia is a coloured substance", "Ammonia is colourless; the colour arises from the change in the complex."),
       ("The d electrons are removed by ammonia", "The d electrons stay in the ion; the gap between orbitals changes.")],
      [("Ligand field strength", "NH3 is above H2O in the spectrochemical series, so ΔE rises and the absorbed light moves to higher energy.")],
      T7, "Reasoning", "Think about the size of the d orbital energy gap."),
    Q("Which complex shows optical isomerism?",
      "[[ [Ni(en)3]^2+ ]] (en = ethane-1,2-diamine)", [("[[ [Ni(H2O)6]^2+ ]]", "All six ligands are identical and the complex is symmetrical."), ("[[ [Pt(NH3)2Cl2] ]] (square planar)", "The square planar complex is planar and has a mirror plane."), ("[[ [Ag(NH3)2]^+ ]]", "The linear complex has a mirror plane.")],
      [("Look for chirality", "Three bidentate ligands arranged in a propeller shape give two non-superimposable mirror images.")], T7, "Concept", "Which complex has no plane of symmetry?"),
    Q("What is the energy gap in kJ/mol for a complex absorbing 500 nm light? (hc/lambda per ion = 3.98 x 10^-19 J; L = 6.02 x 10^23 /mol)",
      "240 kJ/mol", [("2.4 kJ/mol", "A factor of 100 is missing: the product 3.98 x 10^-19 x 6.02 x 10^23 is 2.4 x 10^5 J = 240 kJ."), ("0.24 kJ/mol", "The unit conversion J to kJ was applied twice."), ("3.98 x 10^-19 kJ/mol", "This is the energy per ion in J, not per mole in kJ.")],
      [("Multiply by L", "3.98 x 10^-19 x 6.02 x 10^23 = 2.40 x 10^5 J/mol."), ("Convert", "2.40 x 10^5 J / 1000 = 240 kJ/mol.")],
      T7, "Calculation", "Multiply by the Avogadro constant and convert joules to kilojoules."),
]
SETS += [practice_set(module=M_T, topic=T7, title="Isomerism and colour in complexes practice", lesson="chu2-complex-isomerism-colour", questions=SET7)]

# ============================================================================================
# 8. Ligand exchange and stability constants
# ============================================================================================
use(208)
T8 = "Ligand exchange and stability constants"
SET8 = [
    Q("What is a ligand exchange reaction?",
      "A reaction in which one or more ligands in a complex are replaced by others", [("A reaction in which the metal ion is replaced by another metal ion", "That is a displacement of the metal; ligand exchange keeps the metal and changes ligands."), ("A reaction in which electrons are transferred between ligands", "That would be a redox reaction."), ("A reaction in which the complex loses its charge", "The charge may change or stay the same; the key is that ligands are replaced.")],
      [("Recall", "[Cu(H2O)6]^2+ + 4NH3 -> [Cu(NH3)4(H2O)2]^2+ + 4H2O is an example.")], T8, "Recall", "Which part of the complex is replaced?"),
    Q("Concentrated hydrochloric acid is added to pink aqueous cobalt(II) chloride. What is observed and why?",
      "The solution turns blue because [[ [CoCl4]^2- ]] forms", [("The solution turns green because cobalt is reduced", "No redox occurs; chloride replaces water as ligand."), ("The solution stays pink because chloride cannot be a ligand", "Chloride is a ligand and forms the tetrahedral blue complex."), ("A white precipitate of CoCl2 forms", "Cobalt(II) chloride is soluble in concentrated hydrochloric acid.")],
      [("Ligand exchange", "[Co(H2O)6]^2+ (pink, octahedral) + 4Cl^- <=> [CoCl4]^2- (blue, tetrahedral) + 6H2O.")], T8, "Application", "Which ligand has replaced water?"),
    Q("What is the expression for K_stab of [[Ag^+ + 2NH3 <=> [Ag(NH3)2]^+]]?",
      "[[ [Ag(NH3)2]^+ ]] divided by ([[Ag^+]] times [[NH3]] squared), all concentrations", [("([[Ag^+]] times [[NH3]] squared) divided by [[ [Ag(NH3)2]^+ ]]", "This is the inverse, a dissociation constant."), ("[[ [Ag(NH3)2]^+ ]] divided by ([[Ag^+]] times [[NH3]])", "The ammonia concentration must be squared because two molecules react."), ("[[ [Ag(NH3)2]^+ ]] times [[Ag^+]] divided by [[NH3]] squared", "Product and reactant terms are mixed up.")],
      [("Write the expression", "K_stab = [complex] / ([metal ion][ligand]^2).")], T8, "Concept", "Products over reactants, with the ligand raised to a power equal to its coefficient."),
    N("At equilibrium, [Ag(NH3)2]^+ = 0.030 mol/dm³, Ag^+ = 2.0 x 10^-10 mol/dm³ and NH3 = 0.40 mol/dm³. Calculate log10 of K_stab (to 2 decimal places).", 8.97,
      [("Substitute", "K = 0.030 / (2.0 x 10^-10 x 0.40^2)."), ("Evaluate", "0.40^2 = 0.16; denominator = 3.2 x 10^-11; K = 9.4 x 10^8 mol^-2 dm^6."), ("Logarithm", "log10 (9.375 x 10^8) = 8.97.")],
      T8, "Calculation", "Square the ammonia concentration before dividing.", tol=0.02),
    Q("Complex A has K_stab = 1.6 x 10^7 and complex B has K_stab = 1.0 x 10^20 (same type). What does this show?",
      "Complex B is more stable and its ligands would replace those of A", [("Complex A is more stable because its K_stab is smaller", "A larger K_stab means a more stable complex."), ("The two are equally stable", "K_stab differs by a factor of about 10^13."), ("Complex B dissociates more", "A larger K_stab means less dissociation.")],
      [("Interpret", "A higher K_stab means the equilibrium lies further to the complex; the better ligand displaces the weaker one.")], T8, "Interpretation", "Which constant is larger?"),
    Q("Why does the replacement of six ammonia ligands by three ethane-1,2-diamine molecules around nickel(II) occur readily?",
      "The number of free particles rises from 4 to 7, so the entropy increases", [("The Ni-N bonds formed are far stronger", "The bonds are similar; the enthalpy change is close to zero."), ("Ethane-1,2-diamine is a stronger oxidizing agent", "No oxidation occurs."), ("The reaction is endothermic and so favoured at high temperature", "The enthalpy change is near zero; the driving force is the entropy rise.")],
      [("Count particles", "Left: 1 complex + 3 en = 4. Right: 1 complex + 6 NH3 = 7. More disorder gives positive delta S and a negative delta G.")], T8, "Reasoning", "Count the number of separate species on each side."),
    Q("Which statement explains why AgI does not dissolve in aqueous ammonia although AgCl does?",
      "AgI has a much lower solubility, so too few silver ions are available to form the complex", [("Iodide ions are better ligands than ammonia", "Iodide is a weak ligand for silver in this context; the explanation lies in the very low solubility of AgI."), ("Ammonia cannot form a complex with silver", "It does: [Ag(NH3)2]^+ forms from AgCl."), ("Silver iodide is amphoteric", "Silver iodide is not amphoteric.")],
      [("Solubility product", "Ksp falls from AgCl to AgI, so [Ag^+] in contact with AgI is too low for NH3 to capture it.")], T8, "Reasoning", "Think about the supply of free silver ions."),
    N("25.0 cm³ of hard water needs 15.00 cm³ of 0.0200 mol/dm³ EDTA (reacts 1 : 1 with the metal ions). What is the concentration of metal ions in mol/dm³?", 0.012,
      [("Moles of EDTA", "0.0200 x 0.01500 = 3.00 x 10^-4 mol."), ("Moles of metal ions", "1 : 1, so 3.00 x 10^-4 mol."), ("Concentration", "3.00 x 10^-4 / 0.0250 = 0.0120 mol/dm³.")],
      T8, "Calculation", "Use the 1 : 1 ratio.", tol=0.0005, unit="mol/dm³"),
]
SETS += [practice_set(module=M_T, topic=T8, title="Ligand exchange and stability constants practice", lesson="chu2-ligand-exchange-stability", questions=SET8)]

# ============================================================================================
# 9. Benzene and electrophilic substitution
# ============================================================================================
use(209)
T9 = "Benzene and electrophilic substitution"
SET9 = [
    Q("What is the length of each carbon-carbon bond in benzene?",
      "All equal, about 0.139 nm, between single and double bond lengths", [("Alternating 0.154 nm and 0.134 nm", "That would be the Kekule structure; the real bonds are all equal."), ("All 0.154 nm, as in alkanes", "That is the length of a C-C single bond."), ("All 0.134 nm, as in alkenes", "That is the length of a C=C double bond.")],
      [("Recall", "Equal bond lengths show delocalization of the pi electrons.")], T9, "Recall", "Are the bonds all alike or alternating?"),
    Q("Which type of reaction is characteristic of benzene?",
      "Electrophilic substitution", [("Electrophilic addition", "Addition would destroy the delocalized ring."), ("Nucleophilic substitution", "The electron-rich ring attracts electrophiles, not nucleophiles."), ("Free radical addition at room temperature", "This happens only in UV light and slowly.")],
      [("Recall", "Substitution preserves the stable ring.")], T9, "Recall", "Is the ring electron-rich or electron-poor?"),
    Q("What is the electrophile in the nitration of benzene?",
      "[[NO2^+]]", [("[[NO3^-]]", "Nitrate is a negative ion; it is not an electrophile."), ("[[NH2^-]]", "This is a nucleophile and unrelated to the reaction."), ("[[H^+]]", "H^+ is lost from the ring; it is not the attacking group.")],
      [("Recall", "HNO3 + 2H2SO4 -> NO2^+ + H3O^+ + 2HSO4^-")], T9, "Recall", "Which species is made by sulfuric acid and nitric acid?"),
    Q("Which reagents are needed to convert benzene into bromobenzene?",
      "[[Br2]] with anhydrous [[FeBr3]], in the dark", [("Bromine water at room temperature", "Benzene does not react with bromine water."), ("Bromine and UV light", "UV light gives free-radical addition."), ("Hydrogen bromide and heat", "HBr does not substitute onto the benzene ring.")],
      [("Apply", "A halogen carrier is needed to make Br^+ (or polarized Br2).")], T9, "Application", "A catalyst is needed to make bromine electrophilic."),
    N("5.00 g of benzene (Mr = 78) is converted to nitrobenzene (Mr = 123) with a 60.0% yield. What mass of nitrobenzene is obtained in grams?", 4.73,
      [("Moles of benzene", "5.00 / 78 = 0.06410 mol."), ("Theoretical mass", "0.06410 x 123 = 7.885 g."), ("Actual mass", "60.0% of 7.885 = 4.73 g.")],
      T9, "Calculation", "Find the theoretical mass first, then apply the yield.", tol=0.02, unit="g"),
    Q("Which compound will react fastest with the nitrating mixture?",
      "Methylbenzene", [("Benzene", "Benzene is less reactive than methylbenzene because it lacks an activating group."), ("Nitrobenzene", "The nitro group deactivates the ring."), ("Benzoic acid", "The carboxyl group deactivates the ring.")],
      [("Directing and activating effects", "The CH3 group donates electrons and activates the ring.")], T9, "Reasoning", "Which has an electron-donating group?"),
    Q("Nitration of benzoic acid with the nitrating mixture gives mainly which product?",
      "3-nitrobenzoic acid", [("2-nitrobenzoic acid", "The COOH group is deactivating and 3-directing."), ("4-nitrobenzoic acid", "The COOH group directs to the 3-position, not to the 4-position."), ("2,4-dinitrobenzoic acid", "Only one nitro group enters under mild conditions, and the position is the 3-position.")],
      [("Directing effect", "-COOH withdraws electrons, so substitution takes place at the 3-position.")], T9, "Application", "COOH is a meta director."),
    Q("The enthalpy of hydrogenation of benzene is -208 kJ/mol and that of cyclohexene is -120 kJ/mol. What is the stabilization energy of benzene?",
      "152 kJ/mol", [("88 kJ/mol", "This is 208 - 120, which compares benzene with one C=C, not three."), ("360 kJ/mol", "This is the expected value for three C=C bonds, not the stabilization energy."), ("208 kJ/mol", "This is the actual enthalpy of hydrogenation of benzene.")],
      [("Calculate", "Expected for three C=C: 3 x (-120) = -360. Actual: -208. Difference: 152 kJ/mol.")], T9, "Calculation", "Compare the observed value with three times the cyclohexene value."),
]
SETS += [practice_set(module=M_O, topic=T9, title="Benzene and electrophilic substitution practice", lesson="chu2-benzene-electrophilic-substitution", questions=SET9)]

# ============================================================================================
# 10. Phenols
# ============================================================================================
use(210)
T10 = "Phenols"
SET10 = [
    Q("Which functional group is present in phenol?",
      "A hydroxyl group bonded directly to a benzene ring", [("A hydroxyl group on a saturated carbon chain", "That describes an alcohol."), ("A carbonyl group on a benzene ring", "That would be an aldehyde or ketone."), ("A carboxyl group on a benzene ring", "That is benzoic acid.")],
      [("Recall", "Phenol is C6H5OH: the OH is attached directly to the ring.")], T10, "Recall", "What is the -OH attached to?"),
    Q("Arrange ethanol, phenol and ethanoic acid in order of increasing acid strength.",
      "Ethanol < phenol < ethanoic acid", [("Phenol < ethanol < ethanoic acid", "Ethanol is a weaker acid than phenol."), ("Ethanoic acid < phenol < ethanol", "This reverses the order."), ("Ethanol < ethanoic acid < phenol", "Ethanoic acid is stronger than phenol.")],
      [("Recall the pKa values", "Ethanol 16, phenol 10, ethanoic acid 4.8.")], T10, "Recall", "Smaller pKa means stronger acid."),
    Q("Which reagent distinguishes phenol from ethanol by giving a violet colour?",
      "Neutral iron(III) chloride solution", [("Sodium carbonate solution", "Neither gives effervescence."), ("Acidified potassium dichromate(VI)", "Ethanol is oxidized to a green solution; phenol gives a mixture. It does not give a clean violet colour."), ("Bromine water", "Bromine water gives a white precipitate with phenol, not a violet colour.")],
      [("Recall", "Phenols form a violet complex with Fe^3+ ions.")], T10, "Recall", "Which metal ion forms a coloured complex with phenol?"),
    Q("What is observed when bromine water is added to aqueous phenol?",
      "The orange colour disappears and a white precipitate forms", [("No change", "The activated ring reacts readily."), ("A violet colour forms", "That is the FeCl3 test."), ("A brown solution with a pungent smell forms", "Bromine would stay unchanged without reaction; here the colour disappears.")],
      [("Observation", "C6H5OH + 3Br2 -> C6H2Br3OH + 3HBr; 2,4,6-tribromophenol is a white solid.")], T10, "Application", "Is a catalyst needed?"),
    Q("Why is phenol more reactive than benzene towards electrophiles?",
      "A lone pair on oxygen is delocalized into the ring, increasing its electron density", [("The -OH group withdraws electrons from the ring", "The group donates electrons by delocalization."), ("Phenol is non-polar", "Phenol is polar; this does not explain the ring reactivity."), ("Phenol has more carbon atoms in the ring", "The ring is the same size.")],
      [("Activation", "The oxygen lone pair joins the pi system, so the ring is more electron-rich.")], T10, "Concept", "Does -OH donate or withdraw electrons into the ring?"),
    N("Phenol (1.88 g, Mr = 94) reacts with excess bromine water. Calculate the maximum mass in grams of 2,4,6-tribromophenol (Mr = 331) formed.", 6.62,
      [("Moles of phenol", "1.88 / 94 = 0.0200 mol."), ("Ratio 1 : 1", "n(product) = 0.0200 mol."), ("Mass", "0.0200 x 331 = 6.62 g.")],
      T10, "Calculation", "Use the 1 : 1 ratio.", tol=0.02, unit="g"),
    Q("Phenol is added to sodium carbonate solution. What is observed?",
      "No reaction", [("Effervescence of carbon dioxide", "Phenol is too weak an acid to release CO2 from carbonates."), ("A white precipitate", "No precipitate forms."), ("A violet colour", "That needs iron(III) chloride.")],
      [("Compare acid strength", "Phenol (pKa 10) is weaker than carbonic acid (pKa about 6.4), so it cannot decompose carbonates.")], T10, "Application", "Compare phenol with carbonic acid."),
    Q("Which compound is formed when phenol reacts with ethanoyl chloride?",
      "Phenyl ethanoate", [("Ethyl benzoate", "That has a different arrangement of the groups."), ("Ethanoic acid and benzene", "Phenol is not cleaved into these."), ("Cyclohexanol", "The ring is not reduced.")],
      [("Esterification via acyl chloride", "C6H5OH + CH3COCl -> CH3COOC6H5 + HCl")], T10, "Application", "Acyl chlorides form esters with phenols."),
]
SETS += [practice_set(module=M_O, topic=T10, title="Phenols practice", lesson="chu2-phenols", questions=SET10)]

# ============================================================================================
# 11. Aldehydes and ketones
# ============================================================================================
use(211)
T11 = "Aldehydes and ketones"
SET11 = [
    Q("Which type of reaction occurs when HCN reacts with ethanal?",
      "Nucleophilic addition", [("Electrophilic addition", "The attacking species CN^- is a nucleophile, not an electrophile."), ("Nucleophilic substitution", "Nothing is replaced; HCN adds across C=O."), ("Free radical substitution", "No radicals are involved.")],
      [("Identify the attacker", "CN^- attacks the delta-positive carbon of C=O, and the pi bond opens: nucleophilic addition.")], T11, "Concept", "Is the attacking species electron-rich or electron-poor?"),
    Q("Which compound is an aldehyde?",
      "[[CH3CH2CHO]]", [("[[CH3COCH3]]", "This is propanone, a ketone."), ("[[CH3CH2OH]]", "This is ethanol, an alcohol."), ("[[CH3COOH]]", "This is ethanoic acid, a carboxylic acid.")],
      [("Look for the CHO group", "An aldehyde has a carbonyl carbon bonded to at least one hydrogen, written -CHO.")], T11, "Recall", "Which compound ends in -CHO?"),
    Q("What is observed when propanone is warmed with Tollens' reagent?",
      "No change", [("A silver mirror forms", "That requires an aldehyde."), ("A red-brown precipitate forms", "That is the Fehling's result for an aldehyde."), ("The solution turns green", "That is the dichromate result for an aldehyde or alcohol.")],
      [("Ketones resist oxidation", "A ketone has no hydrogen on the carbonyl carbon and is not oxidized by Tollens' reagent.")], T11, "Application", "Is propanone an aldehyde or a ketone?"),
    Q("Which reagent gives an orange precipitate with both propanal and propanone?",
      "2,4-dinitrophenylhydrazine", [("Tollens' reagent", "It reacts with the aldehyde only."), ("Sodium carbonate", "No reaction with either."), ("Neutral iron(III) chloride", "That is the test for phenols.")],
      [("Recall", "2,4-DNPH reacts with the C=O group in aldehydes and ketones.")], T11, "Recall", "Which test is for the carbonyl group itself?"),
    Q("Which product forms when butanone is reduced with NaBH4?",
      "Butan-2-ol", [("Butan-1-ol", "Reduction of a ketone gives a secondary alcohol, not a primary alcohol."), ("Butanal", "Butanal is an aldehyde and is not formed by reduction."), ("Butanoic acid", "Reduction does not produce an acid.")],
      [("Reduce C=O", "CH3COCH2CH3 + 2[H] -> CH3CH(OH)CH2CH3, a secondary alcohol.")], T11, "Application", "A ketone is reduced to which class of alcohol?"),
    Q("Which compound gives a yellow precipitate with iodine and sodium hydroxide?",
      "Propan-2-ol", [("Propan-1-ol", "It has no CH3CH(OH)- group."), ("Propanal", "It has no CH3CO group."), ("Propanoic acid", "It has no CH3CO or CH3CH(OH) group.")],
      [("Look for CH3CH(OH)- or CH3CO-", "Propan-2-ol, CH3CH(OH)CH3, is oxidized in situ to propanone and gives CHI3.")], T11, "Application", "Which compound has CH3CH(OH)-?"),
    Q("Why is the product of HCN addition to butanone a racemic mixture?",
      "CN^- attacks the planar C=O group from either face with equal probability, giving equal amounts of both enantiomers",
      [("CN^- attacks only from above, giving one enantiomer", "Attack from either face is equally likely."),
       ("The product has no chiral centre", "The carbon that carried the C=O now has four different groups (CH3, C2H5, OH, CN), so it is chiral."),
       ("The product is optically inactive because it is a polymer", "No polymer forms; the product is a single small molecule.")],
      [("Check the structure and the attack", "The new chiral carbon is formed by attack on a flat C=O group from the two faces equally, so the two enantiomers form in equal amounts and their rotations cancel.")],
      T11, "Reasoning", "Think about the shape of the carbonyl group."),
    N("How many degrees of unsaturation does C4H8O have?", 1,
      [("Formula", "DBE = (2C + 2 - H) / 2, ignoring O."), ("Calculate", "(2 x 4 + 2 - 8) / 2 = 1.")],
      T11, "Calculation", "Use (2C + 2 - H) / 2.", tol=0),
]
SETS += [practice_set(module=M_O, topic=T11, title="Aldehydes and ketones practice", lesson="chu2-aldehydes-ketones", questions=SET11)]

# ============================================================================================
# 12. Carboxylic acids and derivatives
# ============================================================================================
use(212)
T12 = "Carboxylic acids and derivatives"
SET12 = [
    Q("What is the functional group of a carboxylic acid?",
      "-COOH", [("-CHO", "This is the aldehyde group."), ("-CO-", "This is the ketone group."), ("-COOR", "This is the ester group.")],
      [("Recall", "The carboxyl group is a carbonyl group with a hydroxyl group on the same carbon.")], T12, "Recall", "The name comes from carbonyl and hydroxyl."),
    Q("Which reagent converts a carboxylic acid into an acyl chloride?",
      "Thionyl chloride, [[SOCl2]]", [("Sodium chloride", "NaCl does not replace the -OH group."), ("Dilute hydrochloric acid", "It does not make an acyl chloride from a carboxylic acid."), ("Chlorine gas", "It would substitute on the alkyl group in light, not on the carboxyl group.")],
      [("Recall", "SOCl2 or PCl5 replaces OH with Cl.")], T12, "Recall", "Which reagent has S, O and Cl?"),
    Q("Which compound is formed when ethanoyl chloride reacts with ammonia?",
      "Ethanamide", [("Ethylamine", "That would need a Hofmann degradation or reduction."), ("Ammonium ethanoate", "That forms from ethanoic acid and ammonia, not from the acyl chloride."), ("Ethanenitrile", "A nitrile would need a dehydrating agent.")],
      [("Nucleophilic addition-elimination", "NH3 replaces Cl: CH3COCl + 2NH3 -> CH3CONH2 + NH4Cl.")], T12, "Application", "Which atom or group does ammonia replace?"),
    Q("What are the products of heating ethyl ethanoate under reflux with aqueous sodium hydroxide?",
      "Sodium ethanoate and ethanol", [("Ethanoic acid and ethanol", "These are the products of acid hydrolysis; in alkali the acid is neutralized to its salt."), ("Sodium ethoxide and ethanoic acid", "The ester is cleaved into the alcohol and the carboxylate, not these."), ("Ethanal and sodium hydroxide", "The ester is not oxidized or reduced here.")],
      [("Alkaline hydrolysis", "CH3COOC2H5 + NaOH -> CH3COONa + C2H5OH.")], T12, "Application", "NaOH neutralizes the acid that forms."),
    N("8.80 g of ethyl ethanoate (Mr = 88) is hydrolysed completely by excess sodium hydroxide solution. What mass in grams of sodium ethanoate (Mr = 82) forms?", 8.2,
      [("Moles of ester", "8.80 / 88 = 0.100 mol."), ("Mole ratio 1 : 1", "n(salt) = 0.100 mol."), ("Mass", "0.100 x 82 = 8.20 g.")],
      T12, "Calculation", "Use the 1 : 1 mole ratio.", tol=0.05, unit="g"),
    Q("Why is chloroethanoic acid a stronger acid than ethanoic acid?",
      "The electronegative chlorine withdraws electrons and stabilizes the anion", [("Chlorine donates electrons to the carboxyl group", "Chlorine is electron-withdrawing in this case."), ("Chloroethanoic acid has a larger molar mass", "Mass is not the reason."), ("Chloroethanoic acid has a stronger O-H bond", "A weaker O-H bond is not the explanation; the stability of the anion is.")],
      [("Inductive effect", "Cl pulls electron density, spreading the negative charge of the carboxylate ion and stabilizing it.")], T12, "Reasoning", "Does chlorine pull or push electrons?"),
    Q("An amide is warmed with bromine and aqueous sodium hydroxide and gives methylamine. What is the amide?",
      "Ethanamide", [("Methanamide", "Hofmann degradation removes one carbon; methanamide would give ammonia."), ("Propanamide", "Propanamide would give ethylamine."), ("N-methylmethanamide", "The reaction applies to primary amides, RCONH2.")],
      [("Remove one carbon", "The amine has one carbon fewer than the amide, so a 2-carbon amide gives methylamine: CH3CONH2 -> CH3NH2.")], T12, "Application", "How many carbon atoms does the amine have?"),
    N("0.500 mol of ethanoic acid and 0.500 mol of ethanol reach equilibrium with Kc = 4.0. How many moles of ester are present at equilibrium? (Give your answer to 2 decimal places.)", 0.33,
      [("Let ester = x", "Acid = ethanol = 0.500 - x; water = x."), ("Kc", "x^2 / (0.500 - x)^2 = 4.0, so x / (0.500 - x) = 2.0."), ("Solve", "x = 1.0 - 2.0x, so x = 0.333 mol.")],
      T12, "Calculation", "Take the square root of both sides first.", tol=0.01, unit="mol"),
]
SETS += [practice_set(module=M_O, topic=T12, title="Carboxylic acids and derivatives practice", lesson="chu2-carboxylic-acids-derivatives", questions=SET12)]

# ============================================================================================
# 13. Amines and diazonium salts
# ============================================================================================
use(213)
T13 = "Amines and diazonium salts"
SET13 = [
    Q("Which compound is a primary amine?",
      "[[CH3CH2NH2]]", [("[[(CH3)2NH]]", "This is a secondary amine (two alkyl groups on N)."), ("[[(CH3)3N]]", "This is a tertiary amine."), ("[[CH3CONH2]]", "This is an amide, not an amine.")],
      [("Count alkyl groups on N", "A primary amine has one alkyl or aryl group on nitrogen, RNH2.")], T13, "Recall", "How many carbon groups are attached to nitrogen?"),
    Q("Which is the correct order of base strength, strongest first?",
      "Ethylamine > ammonia > phenylamine", [("Phenylamine > ammonia > ethylamine", "The order is reversed: phenylamine is the weakest base."), ("Ammonia > ethylamine > phenylamine", "Ethylamine is stronger than ammonia because of the electron-donating ethyl group."), ("Ethylamine > phenylamine > ammonia", "The lone pair of phenylamine is delocalized, making it weaker than ammonia.")],
      [("Compare lone-pair availability", "Alkyl groups donate electrons (stronger base); the benzene ring withdraws the lone pair by delocalization (weaker base).")], T13, "Concept", "Which group pushes electrons to N and which one pulls them?"),
    Q("Which reagents convert nitrobenzene to phenylamine?",
      "Tin and concentrated hydrochloric acid, heat under reflux, then sodium hydroxide", [("Sodium nitrite and hydrochloric acid at 0-5 °C", "That makes a diazonium salt from phenylamine."), ("Concentrated nitric and sulfuric acids", "That nitrates the ring."), ("Bromine and iron(III) bromide", "That brominates the ring.")],
      [("Reduction", "Sn / conc. HCl reduces -NO2 to -NH3^+; NaOH frees the amine.")], T13, "Recall", "The nitro group must be reduced."),
    Q("Phenylamine is treated with sodium nitrite and hydrochloric acid at 0-5 °C. What is formed?",
      "Benzenediazonium chloride", [("Nitrobenzene", "Nitrobenzene needs the nitrating mixture."), ("Phenol", "Phenol forms if the diazonium salt is warmed."), ("Benzene", "No hydrogenolysis occurs.")],
      [("Diazotization", "C6H5NH2 + HNO2 + HCl -> C6H5N2^+ Cl^- + 2H2O")], T13, "Recall", "What type of salt forms at low temperature?"),
    Q("Why must the diazotization of phenylamine be carried out below 5 °C?",
      "The benzenediazonium ion decomposes at higher temperatures, forming phenol and nitrogen", [("The reaction does not start at higher temperatures", "It does start; the problem is the stability of the product."), ("Nitrous acid is a gas at higher temperatures", "It is nitrous acid's own instability, but the main reason is the diazonium ion decomposing."), ("Phenylamine boils at higher temperatures", "The boiling point of phenylamine is 184 °C.")],
      [("Stability", "At higher temperatures C6H5N2^+ + H2O -> C6H5OH + N2 + H^+.")], T13, "Reasoning", "What is lost as bubbles on warming?"),
    N("12.3 g of nitrobenzene (Mr = 123) is reduced to phenylamine (Mr = 93) in 75.0% yield. What mass in grams of phenylamine forms?", 6.98,
      [("Moles", "12.3 / 123 = 0.100 mol."), ("Theoretical mass", "0.100 x 93 = 9.30 g."), ("Actual mass", "0.750 x 9.30 = 6.975, which is 6.98 g.")],
      T13, "Calculation", "Find the theoretical mass, then apply the percentage.", tol=0.02, unit="g"),
    Q("Which product forms when a cold solution of benzenediazonium chloride is added to an alkaline solution of phenol?",
      "A yellow-orange azo dye", [("Phenol and nitrogen", "That occurs if the diazonium solution is warmed in water."), ("Nitrobenzene", "No nitro compound forms."), ("A colourless solution of sodium phenoxide", "The diazonium ion couples with phenoxide and a coloured azo compound forms.")],
      [("Coupling", "The diazonium ion attacks the activated 4-position of the phenoxide ion, forming -N=N-.")], T13, "Application", "What type of compound has the -N=N- group?"),
    Q("What forms when benzenediazonium chloride is warmed with aqueous potassium iodide?",
      "Iodobenzene and nitrogen", [("Iodobenzene only, with no gas released", "Nitrogen is always released when the diazonium group is replaced; bubbles are seen."), ("Phenylamine and iodine", "No reduction of the diazonium group to an amine occurs."), ("Benzene and iodine", "The iodide ion replaces N2; the ring is not reduced.")],
      [("Substitution", "C6H5N2^+ + I^- -> C6H5I + N2")], T13, "Application", "Which group replaces the N2?"),
]
SETS += [practice_set(module=M_O, topic=T13, title="Amines and diazonium salts practice", lesson="chu2-amines-diazonium", questions=SET13)]

# ============================================================================================
# 14. Amino acids, proteins and polymers
# ============================================================================================
use(214)
T14 = "Amino acids, proteins and polymers"
SET14 = [
    Q("Which amino acid does NOT have optical isomers?",
      "Glycine", [("Alanine", "The alpha carbon of alanine carries H, NH2, COOH and CH3: chiral."), ("Serine", "The alpha carbon of serine carries four different groups: chiral."), ("Cysteine", "The alpha carbon of cysteine carries four different groups: chiral.")],
      [("Check for four different groups", "In glycine R = H, so the alpha carbon has two identical H atoms and is not chiral.")], T14, "Recall", "Which amino acid has R = H?"),
    Q("What type of link joins amino acids in a protein?",
      "Peptide (amide) bond, -CO-NH-", [("Ester link, -CO-O-", "Esters join carboxylic acids to alcohols."), ("Glycosidic link", "Glycosidic links join sugar units in carbohydrates."), ("Ionic bond", "Ionic bonds contribute to tertiary structure but do not join the chain.")],
      [("Recall", "The carboxyl group of one amino acid condenses with the amino group of the next, losing water.")], T14, "Recall", "Proteins are polyamides."),
    Q("In strongly acidic solution (pH 1), what is the form of glycine?",
      "[[ +H3N-CH2-COOH ]] (a cation)", [("[[ H2N-CH2-COO^- ]] (an anion)", "That is the form in strongly alkaline solution."), ("[[ +H3N-CH2-COO^- ]] (a zwitterion)", "That is the form at the isoelectric point (about pH 6)."), ("[[ H2N-CH2-COOH ]] (neutral)", "The uncharged form is very minor in water.")],
      [("Add a proton", "In acid, the carboxylate COO^- of the zwitterion is protonated to COOH, leaving a cation.")], T14, "Concept", "Does acid add or remove H^+?"),
    N("Calculate the relative molecular mass of the dipeptide Gly-Gly formed from two molecules of glycine (Mr = 75) with loss of one molecule of water (Mr = 18).", 132,
      [("Sum of the amino acids", "2 x 75 = 150."), ("Subtract water", "150 - 18 = 132.")],
      T14, "Calculation", "One molecule of water is lost for each peptide bond.", tol=0),
    Q("Which pair of monomers forms nylon-6,6?",
      "Hexanedioic acid (or its acyl chloride) and hexane-1,6-diamine", [("Hexanedioic acid and hexane-1,6-diol", "That would form a polyester."), ("Hexane-1,6-diamine and hexane-1,6-diol", "No diacid is present to form an amide or ester link."), ("Hexene and hexane", "Addition polymerization of alkenes does not give nylon.")],
      [("Match the links", "Diacid plus diamine gives amide links: nylon-6,6.")], T14, "Recall", "Nylon is a polyamide."),
    Q("The repeat unit of a polymer is -CH2-CH(CH3)-. What is the monomer?",
      "Propene, CH2=CHCH3", [("Ethene", "Ethene would give -CH2-CH2-."), ("Propane", "Propane is saturated and cannot polymerize by addition."), ("Propan-1-ol", "An alcohol is not an addition monomer.")],
      [("Restore the double bond", "Add C=C between the two chain carbons: CH2=CH(CH3).")], T14, "Application", "Put back the double bond."),
    Q("Which statement about condensation polymers is correct?",
      "A small molecule such as water or HCl is lost each time a monomer joins", [("They are formed from alkene monomers", "That describes addition polymers."), ("The repeat unit has the same formula as the monomer", "That is true for addition polymers; here the small molecule lost changes the formula."), ("They always contain a carbon-only backbone", "Polyesters and polyamides have ester or amide links in the chain.")],
      [("Compare with addition", "Condensation loses a small molecule each time; addition does not.")], T14, "Concept", "What is released in condensation polymerization?"),
    Q("A tripeptide is made from three different amino acids, each used once. How many different tripeptides are possible?",
      "6", [("3", "Order matters; there are more than 3 arrangements."), ("9", "This is 3 x 3, which would allow repeats."), ("27", "This is 3 x 3 x 3, which would allow repeats of the same amino acid.")],
      [("Count arrangements", "3 x 2 x 1 = 6 different sequences.")], T14, "Application", "Arrange three different units in a row."),
]
SETS += [practice_set(module=M_O, topic=T14, title="Amino acids, proteins and polymers practice", lesson="chu2-amino-acids-proteins-polymers", questions=SET14)]

# ============================================================================================
# 15. Structure elucidation by IR, NMR and mass spectrometry
# ============================================================================================
use(215)
T15 = "Structure elucidation by IR, NMR and mass spectrometry"
SET15 = [
    Q("What does the peak at the highest m/z (the molecular ion) in a mass spectrum tell you?",
      "The relative molecular mass of the compound", [("The number of hydrogen environments", "That comes from NMR spectroscopy."), ("The functional groups present", "That comes mainly from infrared spectroscopy."), ("The purity of the sample", "Purity is not found from a single peak.")],
      [("Recall", "M^+ is the molecule that has lost one electron, so its m/z equals the relative molecular mass.")], T15, "Recall", "The molecule has lost only an electron."),
    Q("A strong sharp absorption at 1710 cm⁻¹ in an IR spectrum indicates which bond?",
      "C=O", [("O-H", "O-H absorbs at 3200-3550 cm⁻¹."), ("C≡N", "C≡N absorbs at 2200-2260 cm⁻¹."), ("C-H", "C-H absorbs at 2850-3100 cm⁻¹.")],
      [("Use the table", "The carbonyl stretch is strong and sharp between 1680 and 1750 cm⁻¹.")], T15, "Recall", "Which bond absorbs strongly near 1700?"),
    N("How many degrees of unsaturation are there in C7H6O2 (benzoic acid)?", 5,
      [("Formula", "(2C + 2 - H) / 2."), ("Calculate", "(14 + 2 - 6) / 2 = 5 (a benzene ring is 4 and the C=O is 1).")],
      T15, "Calculation", "Oxygen does not change the count.", tol=0),
    Q("How many signals does the 1H NMR spectrum of ethanol, CH3CH2OH, contain?",
      "3", [("2", "The CH3, the CH2 and the OH are three different environments."), ("5", "That counts hydrogens, not environments."), ("6", "That is the number of hydrogens, not environments.")],
      [("Count environments", "CH3 (triplet), CH2 (quartet) and OH (singlet).")], T15, "Application", "Count the different types of hydrogen."),
    Q("In the 1H NMR spectrum of ethyl ethanoate, what is the signal for the -OCH2- hydrogens at about 4.1 ppm?",
      "A quartet, because there are 3 hydrogens on the adjacent carbon", [("A triplet, because there are 2 hydrogens on the adjacent carbon", "The adjacent carbon is the CH3 with 3 hydrogens, giving a quartet."), ("A singlet, because the oxygen blocks coupling", "Splitting arises from adjacent carbons; the oxygen atom does not remove the CH3 coupling."), ("A doublet, because there is 1 adjacent hydrogen", "There are 3 adjacent hydrogens.")],
      [("n + 1 rule", "n = 3 neighbouring hydrogens gives 3 + 1 = 4 lines.")], T15, "Application", "How many hydrogens are on the neighbouring carbon?"),
    Q("A compound has molecular formula C3H8O. Its 1H NMR spectrum shows a doublet (6H), a septet (1H) and a singlet (1H). What is the compound?",
      "Propan-2-ol", [("Propan-1-ol", "Propan-1-ol would show a triplet, a sextet, another triplet and a singlet."), ("Methoxyethane", "Methoxyethane would show a triplet, a quartet and a singlet (3H) for OCH3."), ("Propanal", "Propanal has a different formula (C3H6O).")],
      [("Match the pattern", "Two equivalent CH3 groups (6H, doublet) next to one CH (septet) means (CH3)2CH-, so (CH3)2CHOH.")], T15, "Reasoning", "A 6H doublet means two equivalent CH3 groups next to a CH."),
    N("In the mass spectrum of an alkane the M peak has height 100 and the M+1 peak has height 5.5. How many carbon atoms are in the molecule?", 5,
      [("Carbons from the ratio", "Number of C = (5.5 / 100) x 100 / 1.1."), ("Calculate", "5.5 / 1.1 = 5 carbon atoms.")],
      T15, "Calculation", "About 1.1% of carbon atoms are 13C.", tol=0),
    Q("The mass spectrum of a compound shows peaks at m/z 108 and 110 of about equal height. Which element is present?",
      "Bromine", [("Chlorine", "Chlorine gives M and M+2 peaks in the ratio 3 : 1."), ("Sulfur", "Sulfur gives a small M+2 peak (about 4% of M), not an equal one."), ("Nitrogen", "Nitrogen has no significant heavy isotope peak.")],
      [("Isotope pattern", "79Br and 81Br are present in nearly equal amounts, so M and M+2 are equal in height.")], T15, "Interpretation", "Which halogen has two isotopes in a 1 : 1 ratio?"),
]
SETS += [practice_set(module=M_O, topic=T15, title="Structure elucidation by IR, NMR and mass spectrometry practice", lesson="chu2-structure-elucidation-spectroscopy", questions=SET15)]

# ============================================================================================
# 16. Examination: Paper 1 strategy
# ============================================================================================
use(216)
TP1 = "Paper 1"
SET16 = [
    Q("According to the Board's 2023 report, how many multiple-choice questions are in Chemistry Paper 1?",
      "50", [("30", "The paper has 50 questions, not 30."), ("40", "The paper has 50 questions, not 40."), ("60", "The paper has 50 questions, not 60.")],
      [("Recall", "Paper 1 consists of 50 multiple-choice questions covering the whole syllabus.")], TP1, "Recall", "A round number between 40 and 60."),
    Q("What is the best first step in a multiple-selection question?",
      "Judge each statement as true or false on its own", [("Read the answer combinations first", "This can bias your judgement of the statements."), ("Choose the combination with the most statements", "The number of statements is not related to correctness."), ("Guess the answer and move on", "A systematic check is quick and much more reliable.")],
      [("Method", "Decide on each statement, then match your verdicts to a combination.")], TP1, "Concept", "Decide on the statements before looking at the options."),
    Q("In an assertion-reason question, both statements are true and the reason correctly explains the assertion. Which answer is correct in the common key?",
      "A", [("B", "B would mean the reason does not explain the assertion."), ("C", "C means the reason is false."), ("D", "D means the assertion is false.")],
      [("Apply the key", "A: both true and the reason is the explanation.")], TP1, "Application", "Which letter is the 'best' combination?"),
    Q("A question asks which of four species is NOT a reducing agent. What should you do first?",
      "Underline NOT and test each option as a reducing agent", [("Choose the species with the highest oxidation number", "This ignores the specific species; you must test each."), ("Choose the first option", "Guessing wastes the chance to eliminate options."), ("Choose the species with the lowest atomic number", "Atomic number does not decide redox behaviour.")],
      [("Read carefully", "Questions with NOT, EXCEPT or LEAST need each option tested against the stated criterion.")], TP1, "Reasoning", "The negative word reverses the question."),
    N("Using E(Cu^2+/Cu) = +0.34 V and E(Zn^2+/Zn) = -0.76 V, calculate the standard cell potential in volts for the Zn/Cu cell.", 1.1,
      [("Cathode and anode", "Cu^2+/Cu is more positive, so it is the cathode; Zn is the anode."), ("Formula", "E cell = E(cathode) - E(anode) = +0.34 - (-0.76)."), ("Result", "E cell = +1.10 V.")],
      TP1, "Calculation", "Subtract the anode value from the cathode value.", tol=0.01, unit="V"),
    N("What is the pH of 0.0050 mol/dm³ hydrochloric acid? Give your answer to 2 decimal places.", 2.3,
      [("Strong monoprotic acid", "[H^+] = 0.0050 mol/dm³."), ("pH", "pH = -log10(0.0050) = 2.30.")],
      TP1, "Calculation", "pH = -log10[H^+].", tol=0.01),
    Q("You find an answer that is not among the options. What should you do?",
      "Check your working for common slips such as the mole ratio, a missing factor of 2, units or the sign", [("Choose the option nearest to your answer", "Distractors are designed to be near answers from common errors."), ("Leave the question blank at once", "You may find the slip quickly and score the mark."), ("Change the question in your head", "The question must be answered as written.")],
      [("Recheck", "The option set normally contains the right answer; a mismatch signals an error in your method.")], TP1, "Reasoning", "The right answer is always among the options."),
    Q("Which approach to a 90-minute, 50-question KKEVO mock is most sensible?",
      "Answer the quick ones first, mark the long ones, and use the remaining time on the marked ones and a final check", [("Start at question 1 and refuse to move on until it is solved", "One hard item can cost the time of several easy ones."), ("Spend 3 minutes on every question", "That would need 150 minutes."), ("Answer only the calculations", "All questions carry the same mark; easy factual items give quicker marks.")],
      [("Time plan", "About 1 min 48 s per question on average; quick items first.")], TP1, "Application", "How much time is there per question on average?"),
]
SETS += [practice_set(module=M_EXAM, topic=TP1, title="Paper 1 strategy practice", lesson="chxu-paper-1-multiple-choice-strategy", questions=SET16)]

# ============================================================================================
# 17. Examination: Paper 2 skills
# ============================================================================================
use(217)
TP2 = "Paper 2"
SET17 = [
    Q("How is Paper 2 organized, according to the Board's 2023 report?",
      "Six compulsory questions in three sections: physical and general, inorganic, organic", [("Ten questions, of which five are chosen", "The Board's report describes six compulsory questions."), ("Fifty multiple-choice questions", "That describes Paper 1."), ("Two practical tasks", "That describes Paper 3.")],
      [("Recall", "Two questions in each of the three sections.")], TP2, "Recall", "Count the sections and the questions in each."),
    Q("What does the command word 'explain' require?",
      "A reason, using the correct chemical idea", [("A one-word answer", "That is for 'state' or 'name'."), ("A list of observations only", "Observations alone answer 'describe'."), ("A calculation with units", "That is for 'calculate'.")],
      [("Command words", "Explain: give the reason for a fact or trend.")], TP2, "Concept", "Think about the word 'because'."),
    Q("Which is a balanced equation for chlorine reacting with hot concentrated potassium hydroxide?",
      "[[3Cl2 + 6KOH -> 5KCl + KClO3 + 3H2O]]", [("[[Cl2 + 2KOH -> KCl + KClO + H2O]]", "That is the equation for cold, dilute alkali."), ("[[Cl2 + KOH -> KCl + KClO3 + H2O]]", "This is not balanced."), ("[[2Cl2 + 4KOH -> 3KCl + KClO3 + 2H2O]]", "This is not balanced: the oxygen and hydrogen atoms do not balance.")],
      [("Hot alkali gives chlorate(V)", "Check: Cl 6 = 5 + 1; K 6 = 5 + 1; O 6 = 3 + 3; H 6 = 6.")], TP2, "Application", "Which equation gives ClO3^- and is balanced?"),
    Q("What are the reagent and conditions needed to convert ethanol to ethanal?",
      "Acidified potassium dichromate(VI), heat and distil the product as it forms", [("Acidified potassium dichromate(VI), heat under reflux with excess oxidant", "Reflux with excess oxidant gives ethanoic acid."), ("Sodium borohydride at room temperature", "NaBH4 reduces; it does not oxidize."), ("Concentrated sulfuric acid, 170 C", "That dehydrates ethanol to ethene.")],
      [("Controlled oxidation", "Distilling the aldehyde as it forms prevents further oxidation.")], TP2, "Application", "Which technique prevents over-oxidation?"),
    Q("A compound X, C3H8O, reacts with sodium to give hydrogen and is oxidized to a product that does not form a silver mirror but gives a yellow precipitate with iodine and NaOH. What is X?",
      "Propan-2-ol", [("Propan-1-ol", "Oxidation gives propanal, which forms a silver mirror."), ("Methoxyethane", "An ether does not react with sodium."), ("Propanal", "Propanal has formula C3H6O, not C3H8O.")],
      [("Deduce step by step", "Alcohol (reacts with Na); oxidation gives propanone (no silver mirror, iodoform positive); so X is the secondary alcohol propan-2-ol.")], TP2, "Reasoning", "Which alcohol gives a ketone on oxidation?"),
    Q("Which statement is the best explanation of why the solubility of Group II sulfates falls down the group?",
      "The lattice energy changes little but the hydration enthalpy of the cation becomes less exothermic", [("The sulfate ion becomes smaller", "The anion is the same in every sulfate."), ("The cations become more strongly hydrated", "Hydration becomes weaker as the cations get larger."), ("The lattice energy increases greatly", "For large anions the lattice energy changes only slightly.")],
      [("Energy cycle", "Enthalpy of solution = - lattice energy + hydration enthalpy; the hydration term falls most.")], TP2, "Reasoning", "Which of the two energy terms changes more?"),
    N("A volatile liquid of mass 0.250 g is vaporized and occupies 96.0 cm³ at room temperature and pressure (24.0 dm³/mol). Calculate its relative molar mass in g/mol.", 62.5,
      [("Moles", "96.0 cm³ = 0.0960 dm³; n = 0.0960 / 24.0 = 0.00400 mol."), ("Molar mass", "M = mass / moles = 0.250 / 0.00400 = 62.5 g/mol.")],
      TP2, "Calculation", "Convert the volume to dm³ first.", tol=0.1, unit="g/mol"),
    Q("In a curly-arrow mechanism for hydroxide attacking bromoethane, where does the first arrow start and end?",
      "From the lone pair on oxygen of OH^- to the carbon atom of the C-Br bond", [("From the C-Br bond to the oxygen of OH^-", "The arrow direction is reversed."), ("From the hydrogen of OH^- to bromine", "The hydrogen is not the electron source."), ("From the bromine atom to the carbon", "The electrons of the C-Br bond move onto bromine, not from it.")],
      [("Electron flow", "Nucleophile's lone pair moves to the electron-poor carbon; the C-Br bond pair moves to Br.")], TP2, "Application", "The tail starts at the electron source."),
]
SETS += [practice_set(module=M_EXAM, topic=TP2, title="Paper 2 structured questions practice", lesson="chxu-paper-2-theory-skills", questions=SET17)]

# ============================================================================================
# 18. Examination: Paper 3 practical skills
# ============================================================================================
use(218)
TP3 = "Paper 3"
SET18 = [
    Q("According to the Board's 2023 report, what are the two questions of Chemistry Paper 3?",
      "Quantitative analysis and qualitative analysis", [("Planning and graph plotting", "These skills are useful but are not the two questions named in the report."), ("Organic synthesis and spectroscopy", "These are theory topics, not the practical questions."), ("Titration only, with no qualitative work", "Paper 3 includes a qualitative analysis question as well.")],
      [("Recall", "Question 1: quantitative analysis. Question 2: qualitative analysis.")], TP3, "Recall", "One measures amounts; one identifies substances."),
    Q("A burette is read as 24.50 cm³ at the end and 1.00 cm³ at the start. What is the titre, and to what precision should burette readings be recorded?",
      "23.50 cm³; to the nearest 0.05 cm³ (two decimal places)", [("23.5 cm³; to the nearest 1 cm³", "A burette is read much more precisely than 1 cm³."), ("25.50 cm³; to 0.01 cm³", "The titre is the difference between the readings, not their sum."), ("23.50 cm³; to 0.5 cm³", "Burettes are read to 0.05 cm³, not 0.5 cm³.")],
      [("Subtract readings", "24.50 - 1.00 = 23.50 cm³; the readings are recorded to 0.05 cm³.")], TP3, "Application", "Titre = final - initial."),
    Q("Titres of 24.10 (rough), 23.55, 23.50 and 23.45 cm³ are obtained. What mean titre should be used?",
      "23.50 cm³", [("23.65 cm³", "That includes the rough titre; it should not be averaged."), ("23.55 cm³", "The mean of the concordant titres is 23.50 cm³."), ("24.10 cm³", "The rough titration is used only to estimate the endpoint.")],
      [("Average the concordant ones", "(23.55 + 23.50 + 23.45) / 3 = 23.50 cm³.")], TP3, "Calculation", "Leave out the rough titre."),
    Q("Why is dilute sulfuric acid, and not hydrochloric acid, used to acidify potassium manganate(VII) titrations?",
      "Chloride ions would be oxidized by manganate(VII), giving a titre that is too high", [("Hydrochloric acid is not strong enough", "It is a strong acid; the problem is the chloride ion."), ("Sulfuric acid is the indicator", "Manganate(VII) is its own indicator."), ("Hydrochloric acid reduces the Fe^2+", "HCl does not change the Fe^2+; the problem is the chloride.")],
      [("Side reaction", "2MnO4^- + 10Cl^- + 16H^+ -> 2Mn^2+ + 5Cl2 + 8H2O wastes manganate(VII).")], TP3, "Reasoning", "Which ion in HCl can be oxidized?"),
    N("25.0 cm³ of Fe^2+ solution needs a mean titre of 23.50 cm³ of 0.0200 mol/dm³ KMnO4. What is the concentration of Fe^2+ in mol/dm³ (3 decimal places)?", 0.094,
      [("Moles of MnO4^-", "0.0200 x 0.02350 = 4.70 x 10^-4 mol."), ("Moles of Fe^2+", "x 5 = 2.35 x 10^-3 mol."), ("Concentration", "2.35 x 10^-3 / 0.0250 = 0.0940 mol/dm³.")],
      TP3, "Calculation", "1 mol of MnO4^- reacts with 5 mol of Fe^2+.", tol=0.001, unit="mol/dm³"),
    Q("Solution X gives a white precipitate with NaOH that dissolves in excess, and a white precipitate with ammonia that does NOT dissolve in excess. Which cation is present?",
      "Al^3+ (or Pb^2+)", [("Zn^2+", "Its hydroxide would dissolve in excess ammonia."), ("Mg^2+", "Its precipitate does not dissolve in excess NaOH."), ("Cu^2+", "It gives a pale blue precipitate, not a white one.")],
      [("Use both tests", "Dissolves in excess NaOH: Al, Zn or Pb. Insoluble in excess NH3: Al or Pb.")], TP3, "Application", "Zinc is the one that dissolves in excess ammonia."),
    Q("Which pair is the correct observation and inference for adding acidified barium chloride to solution Y?",
      "Observation: a white precipitate forms. Inference: sulfate ions are present", [("Observation: sulfate ions form. Inference: a white precipitate", "The terms are reversed: an observation is what is seen."), ("Observation: sulfate is present. Inference: a white precipitate forms", "The inference is the conclusion about the ion."), ("Observation: barium sulfate. Inference: Y is acidic", "Naming the compound is an inference, and acidity is not shown by the test.")],
      [("Separate what is seen from what it means", "Write the observation first; the inference gives the ion.")], TP3, "Interpretation", "Which part can you see with your eyes?"),
    Q("A colourless liquid fizzes with sodium carbonate, decolourizes bromine water and gives no silver mirror. Which compound is it likely to be?",
      "Maleic acid (cis-butenedioic acid) in solution", [("Methanoic acid", "Methanoic acid would give a silver mirror with Tollens' reagent."), ("Ethanol", "Ethanol does not fizz with carbonate."), ("Benzoic acid", "Benzoic acid does not decolourize bromine water.")],
      [("Combine tests", "Fizzing: carboxylic acid. Decolourizing bromine water: C=C. No silver mirror: not methanoic acid.")], TP3, "Reasoning", "Which acid contains C=C?"),
]
SETS += [practice_set(module=M_EXAM, topic=TP3, title="Paper 3 practical skills practice", lesson="chxu-paper-3-practical-skills", questions=SET18)]

# ============================================================================================
# 19. Paper 1 mock exam A: exactly 50 four-option questions across the six Upper Sixth modules
#     (Kinetics 8, Ionic Equilibria 10, Electrochemistry 8, s and p blocks 6, Transition metals 6, Organic 12)
# ============================================================================================
use(301)
KRO = "Rate equations and order of reaction"
KIR = "Initial rates and half-life"
KMR = "Mechanisms and the rate-determining step"
KAR = "The Arrhenius equation"
KCA = "Catalysis"
IAB = "Acid-base theories and pH"
IKA = "Ka, Kb and Kw"
IBU = "Buffer solutions"
ITI = "Titration curves and indicators"
ISH = "Salt hydrolysis"
IKS = "Solubility product and the common ion effect"
ESE = "Standard electrode potentials"
ECE = "Cell EMF and spontaneity"
ENE = "The Nernst equation"
EFU = "Fuel cells"
EQE = "Quantitative electrolysis"
PP3 = "Periodicity across Period 3"
PG12 = "Groups I and II"
PG4 = "Group IV"
PG7 = "Group VII"
TPR = "Properties of the 3d elements"
TCX = "Complex ions and ligands"
TIC = "Isomerism and colour in complexes"
TLE = "Ligand exchange and stability constants"
OBE = "Benzene and electrophilic substitution"
OPH = "Phenols"
OAK = "Aldehydes and ketones"
OCA = "Carboxylic acids and derivatives"
OAM = "Amines and diazonium salts"
OAA = "Amino acids, proteins and polymers"
OST = "Structure elucidation by IR, NMR and mass spectrometry"

P1 = [
    # ---- Reaction Kinetics (8)
    Q("A reaction has the rate equation: rate = k[A]²[B]. The concentration of A is doubled and the concentration of B is tripled. By what factor does the rate change?",
      "12", [("6", "This multiplies 2 by 3 and ignores that A is second order."), ("5", "The factors multiply; they do not add."), ("36", "B is first order, so tripling B triples the rate; only A is squared.")],
      [("Apply each order", "A is second order: 2² = 4. B is first order: 3¹ = 3."), ("Multiply", "Overall factor = 4 x 3 = 12.")],
      KRO, "Calculation", "Raise each concentration factor to the power of its order."),
    Q("A reaction has the rate equation: rate = k[A][B], with rate in mol dm⁻³ s⁻¹. What are the units of k?",
      "mol⁻¹ dm³ s⁻¹", [("s⁻¹", "That is the unit of k for a first-order reaction."), ("mol⁻² dm⁶ s⁻¹", "That is the unit for a third-order reaction."), ("mol dm⁻³ s⁻¹", "That is the unit of the rate itself.")],
      [("Rearrange", "k = rate / ([A][B]) = (mol dm⁻³ s⁻¹) / (mol² dm⁻⁶) = mol⁻¹ dm³ s⁻¹.")],
      KRO, "Calculation", "Divide the units of the rate by the units of the concentration terms."),
    Q("Initial rates for the reaction A + B → products were measured.\nExperiment 1: [A] = 0.10, [B] = 0.10 mol/dm³, rate = 2.0 x 10⁻³ mol dm⁻³ s⁻¹\nExperiment 2: [A] = 0.20, [B] = 0.10 mol/dm³, rate = 8.0 x 10⁻³\nExperiment 3: [A] = 0.10, [B] = 0.20 mol/dm³, rate = 4.0 x 10⁻³\nWhat is the value of k with its units?",
      "2.0 mol⁻² dm⁶ s⁻¹", [("0.20 mol⁻¹ dm³ s⁻¹", "This assumes the reaction is first order in A; doubling [A] quadruples the rate, so A is second order."), ("2.0 x 10⁻³ mol dm⁻³ s⁻¹", "This is the rate in Experiment 1, not k."), ("20 mol⁻² dm⁶ s⁻¹", "This treats B as second order; doubling [B] only doubles the rate.")],
      [("Orders", "Experiments 1 and 2: [A] x 2 gives rate x 4, so order in A = 2. Experiments 1 and 3: [B] x 2 gives rate x 2, so order in B = 1."), ("Rate equation", "rate = k[A]²[B]."), ("k", "k = 2.0 x 10⁻³ / (0.10² x 0.10) = 2.0 mol⁻² dm⁶ s⁻¹.")],
      KIR, "Calculation", "Find each order by comparing two experiments in which only one concentration changes."),
    Q("A first-order reaction has a half-life of 20 minutes. What fraction of the reactant remains after 1 hour?",
      "1/8", [("1/3", "This assumes a steady decrease; first-order decay halves the amount each half-life."), ("1/4", "That is the fraction after two half-lives (40 minutes)."), ("1/6", "This divides by 6; the fraction halves three times, not six.")],
      [("Count half-lives", "60 / 20 = 3 half-lives."), ("Fraction", "(1/2)³ = 1/8.")],
      KIR, "Calculation", "How many half-lives are there in 60 minutes?"),
    Q("The reaction 2NO₂ + F₂ → 2NO₂F has the rate equation: rate = k[NO₂][F₂]. Which mechanism is consistent with this?",
      "Slow: NO₂ + F₂ → NO₂F + F; fast: NO₂ + F → NO₂F", [("Fast: F₂ → 2F; slow: 2NO₂ + 2F → 2NO₂F", "The slow step would then involve NO₂ and F in the rate equation, giving a different form."), ("Slow: 2NO₂ + F₂ → 2NO₂F in one step", "A one-step termolecular reaction would give rate = k[NO₂]²[F₂]."), ("Slow: F₂ → 2F; fast: NO₂ + F → NO₂F", "The slow step involves only F₂, giving rate = k[F₂].")],
      [("The rate-determining step", "The rate equation matches the species in the slow step: one NO₂ and one F₂."), ("Check the sum", "Adding the two steps gives 2NO₂ + F₂ → 2NO₂F.")],
      KMR, "Reasoning", "The slow step must contain exactly the species in the rate equation."),
    Q("A graph of ln k against 1/T for a reaction is a straight line of gradient -6000 K. What is the activation energy? (R = 8.31 J K⁻¹ mol⁻¹)",
      "+49.9 kJ mol⁻¹", [("-49.9 kJ mol⁻¹", "The gradient is -Ea/R, so Ea itself is positive."), ("722 kJ mol⁻¹", "This divides 6000 by R; Ea = -gradient x R."), ("6.00 kJ mol⁻¹", "This ignores R in the calculation.")],
      [("Arrhenius gradient", "ln k = ln A - Ea/RT, so the gradient = -Ea/R."), ("Calculate", "Ea = 6000 x 8.31 = 49 860 J mol⁻¹ = 49.9 kJ mol⁻¹.")],
      KAR, "Calculation", "The gradient equals -Ea/R."),
    Q("Why does a rise in temperature of 10 K often roughly double the rate of a reaction?",
      "The fraction of molecules with energy equal to or greater than the activation energy increases", [("The collision frequency doubles", "Collision frequency rises only by a few per cent for a 10 K rise."), ("The activation energy is halved", "Activation energy is unchanged by temperature."), ("The number of molecules doubles", "The amount of reactant does not change.")],
      [("Maxwell-Boltzmann distribution", "The tail of the distribution above Ea grows rapidly with temperature, so more collisions are successful.")],
      KAR, "Concept", "Think about the energy distribution of the molecules."),
    Q("Which statement about a catalyst is correct?",
      "It provides an alternative reaction pathway with a lower activation energy", [("It makes the reaction more exothermic", "A catalyst does not change the enthalpy change."), ("It increases the equilibrium yield of the products", "A catalyst changes the rate, not the position of equilibrium."), ("It raises the temperature of the reaction", "A catalyst does not change the temperature.")],
      [("Role of a catalyst", "It lowers the activation energy and speeds up both forward and reverse reactions; it is regenerated.")],
      KCA, "Concept", "A catalyst changes the route, not the starting and finishing energies."),
    # ---- Ionic Equilibria (10)
    Q("Which species is a Lewis acid?",
      "[[BF3]]", [("[[NH3]]", "NH3 donates a lone pair, so it is a Lewis base."), ("[[H2O]]", "Water has lone pairs to donate (a Lewis base)."), ("[[Cl^-]]", "Chloride donates a lone pair and is a Lewis base.")],
      [("Definition", "A Lewis acid accepts a lone pair of electrons. BF3 has an incomplete octet on boron.")],
      IAB, "Concept", "Which one has an empty orbital?"),
    Q("What is the conjugate base of the dihydrogenphosphate ion, [[H2PO4^-]]?",
      "[[HPO4^2-]]", [("[[H3PO4]]", "H3PO4 is the conjugate acid of H2PO4^-."), ("[[PO4^3-]]", "PO4^3- is two proton losses away."), ("[[H3O^+]]", "H3O^+ is the conjugate acid of water.")],
      [("Remove one proton", "The conjugate base is formed by loss of one H^+: H2PO4^- gives HPO4^2-.")],
      IAB, "Concept", "A conjugate base has one H^+ fewer."),
    Q("What is the pH of a 0.10 mol/dm³ solution of a weak acid HA with Ka = 1.8 x 10⁻⁵ mol/dm³?",
      "2.87", [("1.00", "This treats the acid as strong and fully ionized."), ("4.74", "This is the pKa, not the pH."), ("5.74", "This omits the square root: [H⁺] = √(Ka x c).")],
      [("Weak acid approximation", "[H⁺] = √(1.8 x 10⁻⁵ x 0.10) = 1.34 x 10⁻³ mol/dm³."), ("pH", "pH = -log10(1.34 x 10⁻³) = 2.87.")],
      IKA, "Calculation", "Use [H⁺] = √(Ka x c) for a weak acid."),
    Q("What is the pH of 0.010 mol/dm³ sodium hydroxide at 25 °C? (Kw = 1.0 x 10⁻¹⁴)",
      "12.00", [("2.00", "This is the pOH, not the pH."), ("12.30", "This counts two hydroxide ions per formula unit; NaOH gives only one."), ("10.00", "This is a slip in subtracting the pOH from 14.")],
      [("pOH", "[OH⁻] = 0.010, so pOH = 2.00."), ("pH", "pH = 14.00 - 2.00 = 12.00.")],
      IKA, "Calculation", "Find pOH first."),
    Q("A buffer contains 0.20 mol/dm³ ethanoic acid and 0.10 mol/dm³ sodium ethanoate. pKa of ethanoic acid = 4.76. What is its pH?",
      "4.46", [("4.76", "This ignores the ratio of salt to acid."), ("5.06", "The ratio has been inverted: it is [salt]/[acid] = 0.10/0.20."), ("3.76", "This subtracts 1 (log 0.1) instead of log 0.5.")],
      [("Henderson-Hasselbalch", "pH = pKa + log([salt]/[acid])."), ("Calculate", "pH = 4.76 + log(0.10/0.20) = 4.76 - 0.30 = 4.46.")],
      IBU, "Calculation", "The salt is the conjugate base in the numerator."),
    Q("Why does an ethanoic acid / sodium ethanoate buffer resist a pH change when a little hydrochloric acid is added?",
      "The ethanoate ions react with the added H⁺ to form ethanoic acid", [("The ethanoic acid reacts with the added H⁺", "The weak acid cannot react with H⁺; the conjugate base does."), ("All the added acid is neutralized completely", "The pH changes slightly, because the buffer capacity is limited."), ("The sodium ions react with the added H⁺", "Sodium ions are spectators.")],
      [("Buffer action", "CH3COO⁻ + H⁺ → CH3COOH: the added acid is converted into the weak acid, so [H⁺] barely changes.")],
      IBU, "Concept", "Which component removes H⁺?"),
    Q("A solution of ethanoic acid is titrated with sodium hydroxide solution. Which indicator is suitable?",
      "Phenolphthalein (range 8.3-10.0)", [("Methyl orange (range 3.1-4.4)", "It changes colour well below the equivalence pH of about 8.7."), ("Methyl red (range 4.2-6.3)", "It also changes colour before the equivalence point."), ("Bromocresol green (range 3.8-5.4)", "It changes colour in an acidic range and is unsuitable for a weak acid with a strong base.")],
      [("Equivalence point", "The salt formed (sodium ethanoate) is basic, so the equivalence point is at pH above 7; phenolphthalein changes in that range.")],
      ITI, "Application", "The equivalence point of a weak acid / strong base titration is above pH 7."),
    Q("Why is an aqueous solution of ammonium chloride acidic?",
      "The ammonium ion donates a proton to water, forming H₃O⁺", [("The chloride ion accepts a proton from water", "Chloride is the conjugate base of a strong acid and does not hydrolyse."), ("Ammonia is a stronger base than water", "That is true but does not explain the acidic solution; it is NH4⁺ that is the weak acid."), ("Ammonium chloride is an acid salt containing H⁺", "It contains no free H⁺; the proton is donated by NH4⁺.")],
      [("Salt hydrolysis", "NH4⁺ + H2O ⇌ NH3 + H3O⁺; the solution has more H3O⁺ than OH⁻.")],
      ISH, "Concept", "Which ion is the conjugate acid of a weak base?"),
    Q("The solubility product of silver chloride is Ksp = 1.8 x 10⁻¹⁰ mol² dm⁻⁶ at 25 °C. What is its solubility in pure water?",
      "1.3 x 10⁻⁵ mol/dm³", [("1.8 x 10⁻¹⁰ mol/dm³", "This is the value of Ksp itself, not the solubility."), ("9.0 x 10⁻¹¹ mol/dm³", "This divides Ksp by 2 instead of taking the square root."), ("1.8 x 10⁻⁵ mol/dm³", "This takes the wrong power of ten in the square root.")],
      [("Ksp expression", "Ksp = [Ag⁺][Cl⁻] = s²."), ("Solve", "s = √(1.8 x 10⁻¹⁰) = 1.34 x 10⁻⁵ mol/dm³.")],
      IKS, "Calculation", "For a 1 : 1 salt, solubility is the square root of Ksp."),
    Q("Using Ksp(AgCl) = 1.8 x 10⁻¹⁰ mol² dm⁻⁶, what is the solubility of silver chloride in 0.10 mol/dm³ sodium chloride?",
      "1.8 x 10⁻⁹ mol/dm³", [("1.3 x 10⁻⁵ mol/dm³", "This is the solubility in pure water; the common ion reduces it."), ("1.8 x 10⁻¹¹ mol/dm³", "This divides by 0.10 twice."), ("0.10 mol/dm³", "This is the chloride concentration, not the solubility of AgCl.")],
      [("Common ion effect", "[Cl⁻] is about 0.10, so [Ag⁺] = Ksp / [Cl⁻] = 1.8 x 10⁻¹⁰ / 0.10 = 1.8 x 10⁻⁹ mol/dm³.")],
      IKS, "Calculation", "Use the chloride from the salt as the dominant [Cl⁻]."),
    # ---- Electrochemistry (8)
    Q("What are the standard conditions of the standard hydrogen electrode?",
      "Hydrogen gas at 100 kPa (1 atm), [H⁺] = 1.00 mol/dm³, 298 K, platinum electrode", [("Hydrogen gas at 100 kPa, [H⁺] = 0.10 mol/dm³, 298 K", "The concentration of H⁺ must be 1.00 mol/dm³."), ("Hydrogen gas at 100 kPa, [H⁺] = 1.00 mol/dm³, 373 K", "The standard temperature is 298 K."), ("Hydrogen gas at 10 kPa, [H⁺] = 1.00 mol/dm³, 298 K", "The standard pressure is 100 kPa (1 atm).")],
      [("Recall", "The SHE has H₂ at 1 atm bubbling over platinum in 1.00 mol/dm³ H⁺ at 298 K, and is assigned E° = 0.00 V.")],
      ESE, "Recall", "Standard conditions: 1 mol/dm³, 100 kPa, 298 K."),
    Q("E° values: Zn²⁺/Zn = -0.76 V, Fe²⁺/Fe = -0.44 V, Cu²⁺/Cu = +0.34 V, Ag⁺/Ag = +0.80 V. Which metal is the strongest reducing agent?",
      "Zn", [("Fe", "Fe is a weaker reducing agent than Zn because its E° is less negative."), ("Cu", "Cu has a positive E°, so it is a weak reducing agent."), ("Ag", "Ag has the most positive E° and is the weakest reducing agent of the four metals.")],
      [("Rule", "The more negative the E°, the more readily the metal gives up electrons.")],
      ESE, "Interpretation", "Which E° is most negative?"),
    Q("E°(Fe³⁺/Fe²⁺) = +0.77 V and E°(Sn⁴⁺/Sn²⁺) = +0.15 V. What is E°cell for 2Fe³⁺ + Sn²⁺ → 2Fe²⁺ + Sn⁴⁺?",
      "+0.62 V", [("+0.92 V", "This adds the two values instead of subtracting."), ("+1.39 V", "E° values are not multiplied by the stoichiometric coefficients."), ("-0.62 V", "The sign is wrong: the Fe³⁺ half-cell is the more positive one (cathode).")],
      [("Use the formula", "E°cell = E°(cathode) - E°(anode) = +0.77 - (+0.15) = +0.62 V."), ("Spontaneity", "A positive E°cell shows the reaction is feasible.")],
      ECE, "Calculation", "The more positive half-cell is the cathode."),
    Q("What is ΔG° for a cell with E°cell = +1.10 V and 2 electrons transferred? (F = 96 500 C/mol)",
      "-212 kJ/mol", [("+212 kJ/mol", "A positive E°cell gives a negative ΔG°."), ("-106 kJ/mol", "This uses n = 1 instead of 2."), ("-0.212 kJ/mol", "This has a unit error; 212 300 J is 212 kJ.")],
      [("Formula", "ΔG° = -nFE°."), ("Calculate", "-2 x 96 500 x 1.10 = -212 300 J/mol = -212 kJ/mol.")],
      ECE, "Calculation", "Use ΔG = -nFE and convert to kJ."),
    Q("For Zn + Cu²⁺ → Zn²⁺ + Cu at 298 K, E°cell = 1.10 V. What is the cell potential when [Zn²⁺] = 1.0 mol/dm³ and [Cu²⁺] = 0.010 mol/dm³? (E = E° - (0.0592/n) log Q)",
      "1.04 V", [("1.10 V", "The Nernst correction has been ignored; the non-standard concentrations change E."), ("1.16 V", "Q has been inverted: Q = [Zn²⁺]/[Cu²⁺] = 100."), ("0.98 V", "n has been taken as 1, but two electrons are transferred.")],
      [("Reaction quotient", "Q = [Zn²⁺]/[Cu²⁺] = 1.0/0.010 = 100."), ("Nernst equation", "E = 1.10 - (0.0592/2) x log 100 = 1.10 - 0.0592 = 1.04 V.")],
      ENE, "Calculation", "Write Q as products over reactants."),
    Q("Which half-equation occurs at the cathode of an acidic hydrogen-oxygen fuel cell?",
      "[[O2 + 4H^+ + 4e^- -> 2H2O]]", [("[[H2 -> 2H^+ + 2e^-]]", "This is the oxidation at the anode."), ("[[O2 + 2H2O + 4e^- -> 4OH^-]]", "This is the cathode reaction of an alkaline fuel cell."), ("[[2H2O -> O2 + 4H^+ + 4e^-]]", "This is oxidation of water, which occurs during electrolysis, not at the fuel-cell cathode.")],
      [("Reduction of oxygen", "In acid, O₂ is reduced: O₂ + 4H⁺ + 4e⁻ → 2H₂O.")],
      EFU, "Concept", "Oxygen is reduced at the cathode."),
    Q("A current of 2.00 A passes through copper(II) sulfate solution for 30.0 minutes using copper electrodes. What mass of copper is deposited at the cathode? (F = 96 500 C/mol; Cu = 63.5)",
      "1.18 g", [("2.37 g", "This uses one electron per copper atom; Cu²⁺ needs two."), ("0.592 g", "This divides by four electrons per copper atom."), ("0.0197 g", "The time was not converted to seconds (30 instead of 1800).")],
      [("Charge", "Q = It = 2.00 x 1800 = 3600 C."), ("Moles of electrons", "3600 / 96 500 = 0.0373 mol."), ("Mass", "Cu²⁺ + 2e⁻ → Cu, so n(Cu) = 0.01865 mol and mass = 0.01865 x 63.5 = 1.18 g.")],
      EQE, "Calculation", "Convert minutes to seconds before using Q = It."),
    Q("How long does it take a current of 0.500 A to deposit 1.08 g of silver? (Ag⁺ + e⁻ → Ag; Ag = 108; F = 96 500 C/mol)",
      "1930 s", [("965 s", "This is the charge in coulombs, not the time in seconds."), ("3860 s", "This uses two electrons per silver atom."), ("482 s", "This divides by 4 when the charge is already found by one electron.")],
      [("Moles of silver", "1.08 / 108 = 0.0100 mol."), ("Charge", "Q = 0.0100 x 96 500 = 965 C."), ("Time", "t = Q / I = 965 / 0.500 = 1930 s.")],
      EQE, "Calculation", "Find the charge first, then divide by the current."),
    # ---- Inorganic Periodic Chemistry (6)
    Q("Which Period 3 oxide reacts with both dilute hydrochloric acid and aqueous sodium hydroxide?",
      "[[Al2O3]]", [("[[MgO]]", "MgO is basic and reacts only with acids."), ("[[SiO2]]", "SiO2 is acidic and reacts only with hot concentrated alkali."), ("[[P4O10]]", "P4O10 is acidic and reacts with water and alkali.")],
      [("Amphoteric oxide", "Aluminium oxide reacts with both acids and alkalis.")],
      PP3, "Recall", "Which oxide is amphoteric?"),
    Q("Why is the melting point of silicon much higher than that of sulfur?",
      "Silicon has a giant covalent structure, whereas sulfur consists of simple molecules with weak intermolecular forces", [("Silicon has a metallic structure", "Silicon is a semiconductor with a covalent network, not a metallic lattice."), ("Silicon atoms have a greater mass", "Mass is not the reason; the structure is."), ("Sulfur has weaker covalent bonds", "The covalent bonds in S₈ are strong; they are not broken on melting.")],
      [("Structure and bonding", "Melting silicon breaks strong covalent bonds throughout the lattice; melting sulfur breaks only London forces.")],
      PP3, "Reasoning", "What must be overcome when each substance melts?"),
    Q("Which statement about the Group II carbonates is correct?",
      "Thermal stability increases down the group because the polarizing power of the cation decreases", [("Thermal stability decreases down the group because the cations become larger", "The larger cations polarize the carbonate ion less, so stability increases."), ("All Group II carbonates are soluble in water", "They are sparingly soluble or insoluble."), ("Thermal stability is the same for all Group II carbonates", "There is a clear trend down the group.")],
      [("Polarization", "Bigger cation, lower charge density, less distortion of CO₃²⁻: more heat is needed to decompose.")],
      PG12, "Concept", "Think about charge density of the cation."),
    Q("Which Group II sulfate is the least soluble in water?",
      "[[BaSO4]]", [("[[MgSO4]]", "MgSO4 is the most soluble."), ("[[CaSO4]]", "CaSO4 is sparingly soluble but more soluble than BaSO4."), ("[[SrSO4]]", "SrSO4 is less soluble than CaSO4 but more soluble than BaSO4.")],
      [("Trend", "Solubility of the sulfates falls down the group; BaSO4 is the basis of the test for sulfate ions.")],
      PG12, "Recall", "Sulfate solubility decreases down the group."),
    Q("Which statement about lead compounds is correct?",
      "Lead(IV) oxide is a strong oxidizing agent because the +2 state is the more stable one", [("Lead(II) is a strong oxidizing agent", "Pb(II) is the stable state and is not strongly oxidizing."), ("Lead(IV) chloride is the most stable chloride of lead", "PbCl₄ is unstable and decomposes to PbCl₂ and Cl₂."), ("Lead behaves exactly like carbon in its oxidation states", "Carbon prefers +4; lead prefers +2 because of the inert pair effect.")],
      [("Inert pair effect", "The +2 state becomes more stable down Group IV, so Pb(IV) is easily reduced.")],
      PG4, "Concept", "Which oxidation state is favoured by lead?"),
    Q("Which sodium halide reacts with concentrated sulfuric acid to give iodine, sulfur and hydrogen sulfide?",
      "[[NaI]]", [("[[NaCl]]", "NaCl gives only steamy HCl fumes."), ("[[NaBr]]", "NaBr gives bromine and sulfur dioxide."), ("[[NaF]]", "NaF gives hydrogen fluoride only.")],
      [("Reducing power", "Iodide is the strongest reducing agent of the halides and reduces H₂SO₄ as far as H₂S.")],
      PG7, "Recall", "Which halide is the strongest reducing agent?"),
    # ---- Transition Metal & Coordination Chemistry (6)
    Q("What is the electronic configuration of the Fe³⁺ ion? (Fe: atomic number 26)",
      "[Ar] 3d⁵", [("[Ar] 3d³ 4s²", "The 4s electrons are lost first."), ("[Ar] 3d⁶", "That is the configuration of Fe²⁺."), ("[Ar] 3d⁴ 4s¹", "No 4s electron remains in the ion.")],
      [("Remove 4s first", "Fe: [Ar] 3d⁶ 4s². Remove two 4s electrons and one 3d electron: [Ar] 3d⁵.")],
      TPR, "Concept", "Remove the 4s electrons before the 3d electrons."),
    Q("Which of these ions is colourless in aqueous solution?",
      "[[Zn^2+]]", [("[[Cu^2+]]", "Cu^2+ is blue."), ("[[Fe^3+]]", "Fe^3+ is yellow-brown."), ("[[Ni^2+]]", "Ni^2+ is green.")],
      [("Check d electrons", "Zn^2+ is 3d10, so no d-d transition is possible.")],
      TPR, "Application", "Which ion has a full 3d sub-shell?"),
    Q("What are the oxidation number of cobalt and the coordination number in [[ [Co(NH3)5Cl]^2+ ]]?",
      "+3 and 6", [("+2 and 6", "+2 is the charge on the whole ion; the Cl^- ligand must be included in the oxidation number calculation."), ("+3 and 2", "There are six donor atoms, not two kinds of ligand."), ("+2 and 5", "Five NH3 ligands plus one Cl^- ligand make six.")],
      [("Oxidation number", "x + 5(0) + 1(-1) = +2, so x = +3."), ("Coordination number", "5 NH3 + 1 Cl^- = 6.")],
      TCX, "Calculation", "Charge of complex = metal + ligand charges."),
    Q("What is the name of the complex ion [[ [Fe(CN)6]^3- ]]?",
      "Hexacyanidoferrate(III)", [("Hexacyanidoiron(III)", "A complex anion takes the -ate ending: ferrate."), ("Hexacyanidoferrate(II)", "The oxidation number of Fe is +3: x + 6(-1) = -3."), ("Hexacyanidoferrate(VI)", "The Roman numeral is the oxidation number, not the number of ligands.")],
      [("Apply the naming rules", "Six cyanide ligands, a negative complex so ferrate, oxidation number +3.")],
      TCX, "Application", "Is the complex a cation or an anion?"),
    Q("Why does replacing the water ligands in [[ [Cu(H2O)6]^2+ ]] by ammonia change the colour of the solution?",
      "The ligand field strength changes the d orbital splitting, so a different wavelength of light is absorbed", [("The oxidation state of copper changes", "Copper remains Cu(II) in both complexes."), ("Ammonia is a coloured ligand", "Ammonia is colourless; the colour comes from the metal complex."), ("The coordination number falls to 2", "The coordination number stays 6 here.")],
      [("Crystal field", "NH3 is a stronger-field ligand than H2O, so ΔE increases and the absorbed light shifts to shorter wavelength.")],
      TIC, "Reasoning", "What property of the d orbitals depends on the ligand?"),
    Q("Which complex ion is the most stable?",
      "[[ [Ni(en)3]^2+ ]] because the chelate effect increases the entropy", [("[[ [Ni(NH3)6]^2+ ]] because ammonia is bidentate", "Ammonia is monodentate."), ("[[ [Ni(H2O)6]^2+ ]] because water is the best ligand", "Water is a weaker ligand than ammonia or en."), ("All three are equally stable", "The K_stab values differ widely.")],
      [("Chelate effect", "Three bidentate en ligands replace six monodentate ligands, increasing the number of free particles from 4 to 7.")],
      TLE, "Concept", "Which ligand is polydentate?"),
    # ---- Advanced Organic Synthesis & Spectroscopy (12)
    Q("Which reagents and conditions convert benzene into nitrobenzene?",
      "Concentrated nitric acid and concentrated sulfuric acid at 50-55 °C", [("Dilute nitric acid at room temperature", "Dilute acid does not give enough NO₂⁺; nitrates phenol but not benzene."), ("Nitrogen dioxide and UV light", "UV light favours radical reactions, not electrophilic substitution."), ("Concentrated hydrochloric acid and sodium nitrite at 0-5 °C", "These reagents make a diazonium salt from an amine.")],
      [("Nitrating mixture", "HNO₃ + 2H₂SO₄ → NO₂⁺ + H₃O⁺ + 2HSO₄⁻; NO₂⁺ is the electrophile.")],
      OBE, "Recall", "Which two acids generate the nitronium ion?"),
    Q("Nitrobenzene is brominated using bromine and iron(III) bromide. What is the main product?",
      "3-bromonitrobenzene", [("2-bromonitrobenzene", "The nitro group is 3-directing, so substitution is not at the 2-position."), ("4-bromonitrobenzene", "The nitro group is 3-directing, not 4-directing."), ("2,4-dibromonitrobenzene", "Only one bromine enters under these conditions, and at the 3-position.")],
      [("Directing effects", "NO₂ is deactivating and 3-directing, so Br enters at the 3-position.")],
      OBE, "Application", "NO₂ is a meta-director."),
    Q("Which reagent gives a violet colour with phenol but not with ethanol?",
      "Neutral iron(III) chloride solution", [("Acidified potassium dichromate(VI)", "It oxidizes ethanol (orange to green) and gives no violet with phenol."), ("Sodium carbonate solution", "Neither compound produces carbon dioxide."), ("2,4-dinitrophenylhydrazine", "Neither contains a carbonyl group.")],
      [("Test for a phenol", "Phenols form a violet complex with Fe³⁺ ions.")],
      OPH, "Recall", "Which metal ion gives a coloured complex with phenols?"),
    Q("Which compound gives both a silver mirror with Tollens' reagent and a yellow precipitate with iodine and aqueous sodium hydroxide?",
      "Ethanal", [("Propanone", "Propanone gives the iodoform test but no silver mirror."), ("Propanal", "Propanal gives a silver mirror but has no CH₃CO group."), ("Ethanol", "Ethanol gives the iodoform test but no silver mirror.")],
      [("Two tests", "Ethanal, CH₃CHO, is an aldehyde (silver mirror) and contains CH₃CO- (iodoform).")],
      OAK, "Application", "You need an aldehyde with a CH₃CO group."),
    Q("What is the main product when butanone is treated with sodium tetrahydridoborate(III), NaBH₄?",
      "Butan-2-ol", [("Butan-1-ol", "Reduction of a ketone gives a secondary alcohol, not a primary alcohol."), ("Butanoic acid", "Reduction does not give an acid."), ("Butanal", "Butanal is an aldehyde, an isomer of butanone, not a reduction product.")],
      [("Reduction", "CH₃COCH₂CH₃ + 2[H] → CH₃CH(OH)CH₂CH₃, a secondary alcohol.")],
      OAK, "Application", "A ketone is reduced to a secondary alcohol."),
    Q("Ethanoyl chloride is added to excess concentrated ammonia solution. What are the products?",
      "Ethanamide and ammonium chloride", [("Ethylamine and hydrogen chloride", "The product keeps the C=O group; it is an amide."), ("Ammonium ethanoate only", "That would form from ethanoic acid, not from the acyl chloride."), ("Ethanoic acid and ammonia", "This is the hydrolysis product with water, not with ammonia.")],
      [("Addition-elimination", "CH₃COCl + 2NH₃ → CH₃CONH₂ + NH₄Cl")],
      OCA, "Application", "The nucleophile replaces Cl."),
    Q("Methyl propanoate is heated under reflux with aqueous sodium hydroxide. What are the products?",
      "Sodium propanoate and methanol", [("Propanoic acid and methanol", "In alkali the acid is neutralized to its sodium salt."), ("Sodium methanoate and propan-1-ol", "The groups are swapped: the acid part is propanoate and the alcohol part is methanol."), ("Propanal and methanol", "Hydrolysis does not reduce the acid portion.")],
      [("Alkaline hydrolysis", "CH₃CH₂COOCH₃ + NaOH → CH₃CH₂COONa + CH₃OH")],
      OCA, "Application", "Name the ester from the acid and the alcohol parts."),
    Q("Which is the correct order of basic strength, strongest first?",
      "Ethylamine > ammonia > phenylamine", [("Phenylamine > ammonia > ethylamine", "Phenylamine is the weakest because its lone pair is delocalized."), ("Ammonia > ethylamine > phenylamine", "The ethyl group makes ethylamine a stronger base than ammonia."), ("Ethylamine > phenylamine > ammonia", "Phenylamine is weaker than ammonia.")],
      [("Lone-pair availability", "Alkyl groups donate electrons; the benzene ring withdraws the lone pair by delocalization.")],
      OAM, "Concept", "Which group makes the lone pair more available?"),
    Q("What reagent and conditions are used to convert phenylamine into benzenediazonium chloride?",
      "Sodium nitrite and hydrochloric acid at 0-5 °C", [("Sodium nitrite and hydrochloric acid at 50 °C", "At 50 °C the diazonium salt decomposes to phenol and nitrogen."), ("Tin and concentrated hydrochloric acid under reflux", "This reduces nitrobenzene to phenylamine."), ("Concentrated nitric acid and sulfuric acid at 50-55 °C", "This nitrates the ring.")],
      [("Diazotization", "NaNO₂ + HCl give HNO₂ in situ; the temperature is kept below 5 °C.")],
      OAM, "Recall", "The temperature is critical."),
    Q("Nylon-6,6 is made from which pair of monomers?",
      "Hexanedioic acid (or its acyl chloride) and hexane-1,6-diamine", [("Hexanedioic acid and hexane-1,6-diol", "This pair makes a polyester."), ("Hexene and ethene", "This would be an addition polymer."), ("Hexane-1,6-diamine and hexane-1,6-diol", "No acid group is present to form amide or ester links.")],
      [("Polyamide", "A diacid and a diamine form amide links with loss of water or HCl.")],
      OAA, "Recall", "Nylon is a polyamide."),
    Q("How many signals appear in the 1H NMR spectrum of 2-methylpropan-2-ol, (CH₃)₃COH?",
      "2", [("1", "The OH hydrogen is in a different environment from the nine CH₃ hydrogens."), ("3", "The three CH₃ groups are equivalent, so they give one signal."), ("10", "This counts hydrogen atoms, not environments.")],
      [("Count environments", "Nine equivalent CH₃ hydrogens give one singlet and the OH hydrogen gives another singlet.")],
      OST, "Application", "Equivalent hydrogens give one signal."),
    Q("The mass spectrum of a compound has molecular ion peaks at m/z 64 and 66 in the ratio 3 : 1. Which element is present?",
      "Chlorine", [("Bromine", "Bromine gives M and M+2 peaks in the ratio 1 : 1."), ("Sulfur", "Sulfur gives a small M+2 peak (about 4%)."), ("Nitrogen", "Nitrogen has no significant M+2 peak.")],
      [("Isotope pattern", "35Cl : 37Cl is 3 : 1, so the M and M+2 peaks are in a 3 : 1 ratio (chloroethane).")],
      OST, "Interpretation", "Which halogen has isotopes in a 3 : 1 ratio?"),
]
assert len(P1) == 50, len(P1)
SETS += [practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="chxu-paper-1-multiple-choice-strategy",
                      mock=True, time_limit_minutes=90, questions=P1)]

# ============================================================================================
# 20. Paper 2 practice paper A: 26 auto-markable parts in six numbered questions (A: 1-2, B: 3-4, C: 5-6)
# ============================================================================================
use(302)
P2 = [
    # ---- Question 1 (Section A): kinetics
    Q("Question 1 (a). Initial rates were measured for the reaction P + Q → products at constant temperature.\nExperiment 1: [P] = 0.20, [Q] = 0.10 mol/dm³, rate = 3.0 x 10⁻⁴ mol dm⁻³ s⁻¹\nExperiment 2: [P] = 0.40, [Q] = 0.10 mol/dm³, rate = 6.0 x 10⁻⁴\nExperiment 3: [P] = 0.20, [Q] = 0.30 mol/dm³, rate = 2.7 x 10⁻³\nWhat is the order of reaction with respect to Q?",
      "Second order", [("Zero order", "The rate changes when [Q] changes, so the order is not zero."), ("First order", "Tripling [Q] would then triple the rate; here the rate increases ninefold."), ("Third order", "Tripling [Q] raises the rate by 3² = 9, not by 3³ = 27.")],
      [("Compare experiments 1 and 3", "[Q] is multiplied by 3 and the rate is multiplied by 2.7 x 10⁻³ / 3.0 x 10⁻⁴ = 9."), ("Order", "3ⁿ = 9 so n = 2.")],
      KRO, "Calculation", "Compare two experiments in which only [Q] changes."),
    N("Question 1 (b). Using the data of Question 1 (a) (P is first order and Q is second order), calculate the rate constant k. Give the value only, in mol⁻² dm⁶ s⁻¹.", 0.15,
      [("Rate equation", "rate = k[P][Q]²."), ("Substitute experiment 1", "3.0 x 10⁻⁴ = k x 0.20 x 0.10² = k x 2.0 x 10⁻³."), ("Solve", "k = 0.15 mol⁻² dm⁶ s⁻¹.")],
      KIR, "Calculation", "Rearrange the rate equation for k.", tol=0.005, unit="mol⁻² dm⁶ s⁻¹"),
    N("Question 1 (c). The rate constant of a first-order reaction is 2.0 x 10⁻³ s⁻¹ at 300 K and 8.0 x 10⁻³ s⁻¹ at 320 K. Calculate the activation energy in kJ/mol. (R = 8.314 J K⁻¹ mol⁻¹; ln(k₂/k₁) = Ea/R x (1/T₁ - 1/T₂))", 55.3,
      [("ln(k2/k1)", "ln(4.0) = 1.386."), ("1/T1 - 1/T2", "1/300 - 1/320 = 2.083 x 10⁻⁴ K⁻¹."), ("Ea", "Ea = 8.314 x 1.386 / 2.083 x 10⁻⁴ = 55 300 J/mol = 55.3 kJ/mol.")],
      KAR, "Calculation", "Use the two-temperature form of the Arrhenius equation.", tol=0.4, unit="kJ/mol"),
    Q("Question 1 (d). Adding a catalyst to a reversible exothermic reaction at constant temperature does which of the following?",
      "It increases the rates of the forward and reverse reactions equally and leaves ΔH unchanged", [("It increases the equilibrium yield of products", "A catalyst does not change the equilibrium position."), ("It makes ΔH more negative", "The enthalpy change depends only on reactants and products."), ("It increases the activation energy of the reverse reaction only", "The activation energies of both directions are lowered by the same amount.")],
      [("Role of a catalyst", "It provides a pathway with a lower Ea for both directions, so equilibrium is reached sooner but not shifted.")],
      KCA, "Concept", "What does a catalyst change and what does it leave unchanged?"),
    # ---- Question 2 (Section A): ionic equilibria and electrochemistry
    N("Question 2 (a). Calculate the pH of 0.020 mol/dm³ of a weak acid HA, Ka = 1.8 x 10⁻⁵ mol/dm³. Give your answer to 2 decimal places.", 3.22,
      [("Weak acid approximation", "[H⁺] = √(Ka x c) = √(1.8 x 10⁻⁵ x 0.020) = 6.0 x 10⁻⁴ mol/dm³."), ("pH", "pH = -log10(6.0 x 10⁻⁴) = 3.22.")],
      IKA, "Calculation", "Use [H⁺] = √(Ka x c).", tol=0.01),
    N("Question 2 (b). A buffer is made from 0.30 mol/dm³ ethanoic acid and 0.15 mol/dm³ sodium ethanoate (pKa = 4.76). Calculate its pH to 2 decimal places.", 4.46,
      [("Henderson-Hasselbalch", "pH = pKa + log([salt]/[acid])."), ("Calculate", "pH = 4.76 + log(0.15/0.30) = 4.76 - 0.30 = 4.46.")],
      IBU, "Calculation", "Salt over acid, inside the logarithm.", tol=0.01),
    N("Question 2 (c). E°(Ag⁺/Ag) = +0.80 V and E°(Zn²⁺/Zn) = -0.76 V. Calculate E°cell for the cell formed from these two half-cells, in volts.", 1.56,
      [("Cathode and anode", "Ag⁺/Ag is more positive, so it is the cathode; Zn is the anode."), ("E°cell", "+0.80 - (-0.76) = +1.56 V.")],
      ECE, "Calculation", "E°cell = E°(cathode) - E°(anode).", tol=0.01, unit="V"),
    N("Question 2 (d). A current of 2.00 A passes for 30.0 minutes through copper(II) sulfate solution. Calculate the mass of copper deposited in grams. (F = 96 500 C/mol; Cu = 63.5)", 1.18,
      [("Charge", "Q = 2.00 x 1800 = 3600 C."), ("Moles of electrons", "3600 / 96 500 = 0.0373 mol."), ("Mass", "n(Cu) = 0.0373 / 2 = 0.01865 mol; mass = 0.01865 x 63.5 = 1.18 g.")],
      EQE, "Calculation", "Convert the time into seconds.", tol=0.02, unit="g"),
    N("Question 2 (e). The solubility product of silver chloride is 1.8 x 10⁻¹⁰ mol² dm⁻⁶. Calculate its solubility in pure water, in units of 10⁻⁵ mol/dm³ (give the number only, to 2 decimal places).", 1.34,
      [("Ksp expression", "Ksp = [Ag⁺][Cl⁻] = s²."), ("Solve", "s = √(1.8 x 10⁻¹⁰) = 1.34 x 10⁻⁵ mol/dm³.")],
      IKS, "Calculation", "For a 1 : 1 salt, s = √Ksp.", tol=0.02),
    # ---- Question 3 (Section B): s- and p-block
    Q("Question 3 (a). Phosphorus(V) oxide, P₄O₁₀, is added to water. What is the approximate pH of the solution and the main product?",
      "pH about 0-1; phosphoric acid", [("pH about 13-14; phosphoric acid", "P4O10 is acidic; the solution is strongly acidic."), ("pH 7; no reaction", "P4O10 reacts vigorously with water."), ("pH about 13; sodium phosphate", "No sodium is present.")],
      [("Acidic oxide", "P₄O₁₀ + 6H₂O → 4H₃PO₄, a strong acid solution.")],
      PP3, "Recall", "Is P4O10 a metal or non-metal oxide?"),
    Q("Question 3 (b). Which statement best explains why the solubility of the Group II sulfates decreases down the group?",
      "The hydration enthalpy of the cation becomes less exothermic while the lattice energy changes little", [("The lattice energy of the sulfates increases greatly down the group", "The lattice energy changes only slightly because the sulfate ion is large."), ("The sulfate ion becomes more polarized", "The sulfate ion is the same in each compound."), ("The cations become more strongly hydrated", "Larger cations are less strongly hydrated.")],
      [("Energy terms", "Dissolving is less favourable when the hydration enthalpy decreases faster than the lattice energy.")],
      PG12, "Reasoning", "Which energy term changes little for a large anion?"),
    N("Question 3 (c). Calcium carbonate (10.0 g) is heated strongly until it has fully decomposed. Calculate the mass of calcium oxide formed in grams. (Ca = 40, C = 12, O = 16)", 5.6,
      [("Moles of CaCO3", "10.0 / 100 = 0.100 mol."), ("Ratio 1 : 1", "n(CaO) = 0.100 mol."), ("Mass", "0.100 x 56 = 5.60 g.")],
      PG12, "Calculation", "Use the 1 : 1 ratio.", tol=0.02, unit="g"),
    Q("Question 3 (d). Lead(IV) chloride is unstable at room temperature but carbon tetrachloride is stable. What explains this?",
      "The +2 oxidation state is more stable than +4 for lead because of the inert pair effect", [("Lead is a non-metal", "Lead is a metal."), ("The Pb-Cl bond is stronger than the C-Cl bond", "Pb-Cl is weaker; the cause is the stability of Pb(II)."), ("Carbon has d orbitals", "Carbon has no d orbitals in its second shell.")],
      [("Inert pair effect", "PbCl₄ → PbCl₂ + Cl₂; the 6s² pair of lead is reluctant to be used in bonding.")],
      PG4, "Concept", "Think about the stability of Pb(II)."),
    # ---- Question 4 (Section B): halogens and transition metals
    N("Question 4 (a). Chlorine reacts with hot concentrated potassium hydroxide: 3Cl₂ + 6KOH → 5KCl + KClO₃ + 3H₂O. How many moles of KCl are produced per mole of KClO₃?", 5,
      [("Read the equation", "5 mol of KCl and 1 mol of KClO3 are formed.")],
      PG7, "Application", "Read the coefficients in the balanced equation.", tol=0),
    N("Question 4 (b). 25.0 cm³ of 0.200 mol/dm³ sodium iodide solution is treated with excess silver nitrate solution. Calculate the mass of silver iodide formed in grams. (Ag = 108, I = 127)", 1.18,
      [("Moles of I⁻", "0.200 x 0.0250 = 0.00500 mol."), ("Ratio 1 : 1", "n(AgI) = 0.00500 mol; Mr = 235."), ("Mass", "0.00500 x 235 = 1.175 g, which is 1.18 g.")],
      PG7, "Calculation", "Find the moles of iodide first.", tol=0.01, unit="g"),
    Q("Question 4 (c). What are the oxidation number of chromium and the coordination number in [Cr(H₂O)₄Cl₂]⁺?",
      "+3 and 6", [("+1 and 6", "+1 is the charge on the whole ion; the two chloride ligands must be allowed for."), ("+3 and 2", "There are six ligands, so the coordination number is 6."), ("+2 and 4", "Four water ligands plus two chloride ligands give coordination number 6, and Cr is +3.")],
      [("Oxidation number", "x + 4(0) + 2(-1) = +1, so x = +3."), ("Coordination number", "4 + 2 = 6.")],
      TCX, "Calculation", "Include the charge of each ligand."),
    N("Question 4 (d). A complex absorbs light of wavelength 450 nm. Calculate the energy gap between the d orbitals in kJ/mol. (h = 6.63 x 10⁻³⁴ J s; c = 3.00 x 10⁸ m/s; L = 6.02 x 10²³ mol⁻¹)", 266,
      [("Energy per ion", "E = hc/λ = (6.63 x 10⁻³⁴ x 3.00 x 10⁸) / (4.50 x 10⁻⁷) = 4.42 x 10⁻¹⁹ J."), ("Per mole", "4.42 x 10⁻¹⁹ x 6.02 x 10²³ = 2.66 x 10⁵ J/mol = 266 kJ/mol.")],
      TIC, "Calculation", "Convert nm to m; multiply by L and divide by 1000.", tol=2, unit="kJ/mol"),
    # ---- Question 5 (Section C): organic
    Q("Question 5 (a). Compound A, C₄H₈O₂ (Mr 88), has an IR peak at 1740 cm⁻¹ and no broad peak above 2500 cm⁻¹. Its 1H NMR spectrum has a triplet (3H, 1.2 ppm), a singlet (3H, 2.0 ppm) and a quartet (2H, 4.1 ppm). What is A?",
      "Ethyl ethanoate", [("Butanoic acid", "A carboxylic acid would show a broad O-H absorption and a 10-12 ppm signal."), ("Methyl propanoate", "That would show a CH₃ singlet near 3.7 ppm (OCH₃), a quartet near 2.3 ppm and a triplet near 1.1 ppm; the quartet in this spectrum is at 4.1 ppm."), ("Propyl methanoate", "That would show a methanoate CH signal near 8 ppm.")],
      [("Match the data", "1740 cm⁻¹ is an ester C=O. The CH₃CO singlet at 2.0 and the OCH₂CH₃ pattern fit ethyl ethanoate.")],
      OST, "Reasoning", "Identify the ester from the splitting pattern."),
    Q("Question 5 (b). What is the electrophile in the nitration of benzene?",
      "The nitronium ion, NO₂⁺", [("The nitrate ion, NO₃⁻", "Nitrate is a nucleophile, not an electrophile."), ("The hydronium ion, H₃O⁺", "H₃O⁺ is a by-product."), ("The nitrite ion, NO₂⁻", "Nitrite is not formed in the nitrating mixture.")],
      [("Generating the electrophile", "HNO₃ + 2H₂SO₄ → NO₂⁺ + H₃O⁺ + 2HSO₄⁻")],
      OBE, "Recall", "A positive ion attacks the electron-rich ring."),
    Q("Question 5 (c). Which test distinguishes pentan-2-one from pentan-3-one?",
      "Warm with iodine and aqueous sodium hydroxide: pentan-2-one gives a yellow precipitate", [("Add Tollens' reagent: pentan-2-one gives a silver mirror", "Neither is an aldehyde; neither gives a silver mirror."), ("Add 2,4-DNPH: only pentan-2-one gives an orange precipitate", "Both ketones give an orange precipitate."), ("Add Fehling's solution: pentan-2-one gives a red precipitate", "Ketones do not react with Fehling's solution.")],
      [("Iodoform test", "Pentan-2-one has CH₃CO-; pentan-3-one does not, so only the first gives CHI₃.")],
      OAK, "Application", "Which ketone contains a methyl group on the carbonyl carbon?"),
    N("Question 5 (d). 0.500 mol ethanoic acid and 0.500 mol ethanol reach equilibrium with Kc = 4.0. Calculate the amount in mol of ethyl ethanoate at equilibrium, to 2 decimal places.", 0.33,
      [("Let x = ester", "Acid = ethanol = 0.500 - x; ester = water = x."), ("Kc", "x²/(0.500 - x)² = 4.0, so x/(0.500 - x) = 2.0."), ("Solve", "x = 1.00 - 2.0x; x = 0.333 mol.")],
      OCA, "Calculation", "The volume cancels in this equilibrium.", tol=0.01, unit="mol"),
    Q("Question 5 (e). A polymer has the repeat unit -CH₂-CHCl-. Which statement is correct?",
      "The monomer is chloroethene and the polymer is an addition polymer", [("The monomer is chloroethane and the polymer is a condensation polymer", "Chloroethane is saturated and cannot polymerize by addition."), ("The monomer is 1,2-dichloroethane", "Two chlorines would give a different repeat unit."), ("The polymer is formed by loss of HCl at each link", "No small molecule is lost in addition polymerization.")],
      [("Restore the C=C", "Repeat unit -CH₂-CHCl- comes from CH₂=CHCl by addition polymerization.")],
      OAA, "Application", "Put the double bond back between the chain carbons."),
    # ---- Question 6 (Section C): organic
    Q("Question 6 (a). Compound X, C₃H₈O, reacts with sodium to give hydrogen. When oxidized with warm acidified potassium dichromate(VI) and distilled, the product gives a silver mirror with Tollens' reagent. What is X?",
      "Propan-1-ol", [("Propan-2-ol", "Oxidation gives propanone, which gives no silver mirror."), ("Methoxyethane", "An ether does not react with sodium."), ("Propanal", "Propanal has the formula C₃H₆O.")],
      [("Deduce", "Reacts with Na: an alcohol. Oxidation product is an aldehyde: X is a primary alcohol, propan-1-ol.")],
      OAK, "Reasoning", "A silver mirror needs an aldehyde."),
    Q("Question 6 (b). Which observation shows that a liquid is phenol and not ethanol?",
      "A white precipitate forms with bromine water", [("Bubbles of hydrogen form with sodium", "Both phenol and ethanol react with sodium."), ("The liquid turns acidified dichromate(VI) green", "Ethanol does this; phenol is oxidized to a messy mixture."), ("The liquid dissolves in water", "Ethanol is miscible with water; solubility does not distinguish.")],
      [("Distinguish", "Phenol gives 2,4,6-tribromophenol, a white precipitate, with bromine water.")],
      OPH, "Application", "Which reaction depends on the activated ring?"),
    Q("Question 6 (c). Which reagent and condition convert nitrobenzene into phenylamine?",
      "Tin and concentrated hydrochloric acid, heat under reflux, then add sodium hydroxide", [("Sodium nitrite and hydrochloric acid at 0-5 °C", "That forms a diazonium salt from phenylamine."), ("Concentrated nitric acid and concentrated sulfuric acid", "That introduces more nitro groups."), ("Lithium tetrahydridoaluminate(III) in dry ether", "With aromatic nitro compounds it gives azo compounds rather than the amine, so it is not used for this step.")],
      [("Reduction", "Sn / conc. HCl reduces -NO₂ to -NH₃⁺; NaOH frees the amine.")],
      OAM, "Recall", "Which metal in acid reduces a nitro group?"),
    N("Question 6 (d). How many degrees of unsaturation does C₈H₈O (phenylethanone) have?", 5,
      [("Formula", "(2C + 2 - H) / 2."), ("Calculate", "(16 + 2 - 8) / 2 = 5: benzene ring (4) plus C=O (1).")],
      OST, "Calculation", "Oxygen does not affect the count.", tol=0),
]
assert len(P2) == 26, len(P2)
SETS += [practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="chxu-paper-2-theory-skills",
                      mock=True, time_limit_minutes=150, questions=P2)]

SETS = _walk(SETS)
