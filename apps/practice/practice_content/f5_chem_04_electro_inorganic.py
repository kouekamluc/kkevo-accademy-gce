"""Practice sets for Form 5 Chemistry: Electrochemistry, and Inorganic Chemistry (Non-Metals & Metals).

Formulae are written in double square brackets in text and double curly brackets in maths; a helper at the bottom
turns them into LaTeX.
"""

import re

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "form-5")

M_EL = "Electrochemistry"
M_IN = "Inorganic Chemistry (Non-Metals & Metals)"

_SEQ = [2, 0, 3, 1, 3, 1, 0, 2, 1, 3, 2, 0, 0, 2, 1, 3]
_N = [0]


def _steps(step):
    out = []
    for st in step:
        if len(st) == 3:
            out.append(S(st[0], text=st[1], math=st[2]))
        else:
            out.append(S(st[0], text=st[1]))
    return out


def Q(prompt, options, ci, whys, step, concept, skill, hint, feedback="", diagram="", diagram_alt=""):
    """MC question: options in the order written, ci = index of the correct one, whys = reasons for the wrong ones
    (in order). The correct option is swapped to a rotating position so answers spread over A-D."""
    whys = list(whys)
    by_index = len(whys) == len(options)
    chs = []
    k = 0
    for i, text in enumerate(options):
        if i == ci:
            chs.append(C(text, correct=True))
        else:
            chs.append(C(text, why=whys[i] if by_index else whys[k]))
            k += 1
    target = _SEQ[_N[0] % len(_SEQ)]
    _N[0] += 1
    chs[ci], chs[target] = chs[target], chs[ci]
    return MC(prompt, chs, steps=_steps(step), concept=concept, skill=skill, hint=hint, feedback=feedback,
              diagram=diagram, diagram_alt=diagram_alt)


def NQ(prompt, answer, step, tol, unit, concept, skill, hint, feedback="", diagram="", diagram_alt=""):
    return NUM(prompt, answer, steps=_steps(step), tolerance=tol, unit=unit, concept=concept, skill=skill, hint=hint,
               feedback=feedback, diagram=diagram, diagram_alt=diagram_alt)


SETS = []

# ===================================================================== 1. Electrolytes and ionic theory
SETS.append(practice_set(
    module=M_EL, topic="Electrolytes and ionic theory",
    title="Electrolytes, non-electrolytes and ions", lesson="chd-electrolytes-ionic-theory",
    questions=[
        Q("The circuit shown is used to test liquids. The bulb lights when the electrodes are placed in which liquid?",
          ["Ethanol", "Sugar solution", "Dilute sulfuric acid", "Tetrachloromethane"], 2,
          ["Ethanol is made of molecules only, so it has no free ions.", "Sugar dissolves as whole molecules and gives no ions.",
           "Tetrachloromethane is a covalent liquid with no ions."],
          [("Look for ions", "A liquid conducts only if it contains free ions."), ("Check each", "Dilute sulfuric acid ionizes to give H+ and sulfate ions, so the bulb lights.")],
          "Which liquids conduct", "Recall", "Which of these liquids contains ions?",
          diagram="f5ch-d-conductivity-test.svg", diagram_alt="Circuit with a bulb, a battery and two electrodes dipping in a beaker of liquid"),
        Q("Which of these is a non-electrolyte?", ["Molten sodium chloride", "Ethanol", "Copper(II) sulfate solution", "Dilute hydrochloric acid"], 1,
          ["Molten sodium chloride has free ions and is decomposed by current, so it is an electrolyte.",
           "Copper(II) sulfate solution contains free ions, so it is an electrolyte.",
           "Hydrochloric acid contains H+ and Cl- ions, so it is an electrolyte."],
          [("Definition", "A non-electrolyte is a compound that does not conduct when molten or in water."), ("Answer", "Ethanol is molecular and does not ionize.")],
          "Non-electrolytes", "Recall", "A non-electrolyte has no free ions in any state."),
        Q("Why does molten lead(II) bromide conduct electricity?", ["Its electrons are free to move", "Its ions are free to move", "Its atoms are free to move", "It contains water"], 1,
          ["Electrons carry current in metals, not in ionic compounds.", "Atoms have no charge, so moving atoms cannot carry current.", "Lead(II) bromide is not a hydrate and there is no water in a molten salt."],
          [("Solid", "In the solid the ions are fixed in the lattice."), ("Molten", "On melting, the ions are free to move and carry the charge.")],
          "Ionic theory", "Concept", "What carries charge in an electrolyte?"),
        Q("Copper wire conducts electricity. The charge is carried by", ["positive ions", "negative ions", "free electrons", "molecules of copper"], 2,
          ["Metals do not contain ions that move.", "Metals have no free anions.", "Copper is a solid metal made of atoms, not molecules."],
          [("Metals", "A metal has a lattice of atoms (positive ions) in a sea of free electrons."), ("Answer", "The free electrons carry the current.")],
          "Conduction in metals", "Concept", "Is copper an electrolyte?"),
        Q("Which equation correctly shows the ionization of sulfuric acid in water?",
          [r"[[H2SO4 -> 2H^+ + SO4^2-]]", r"[[H2SO4 -> H^+ + SO4^2-]]", r"[[H2SO4 -> 2H^+ + SO4^-]]", r"[[H2SO4 -> H2 + SO4]]"], 0,
          ["The charges do not balance: 1+ and 2- do not add to zero.", "Charge is 2+ and 1-, so it does not balance.", "Sulfuric acid does not break into a gas and a radical when dissolved in water."],
          [("Charge balance", "The two H+ ions give 2+. The sulfate ion carries 2- to balance them."), ("Atoms", "2 H, 1 S, 4 O on both sides.")],
          "Ionization equations", "Calculation", "Count the charges on both sides."),
        Q("Solution X and solution Y have the same concentration. The bulb is bright with X and dim with Y. What can you conclude?",
          ["X is a strong electrolyte and Y is a weak electrolyte", "Y is a strong electrolyte and X is a weak electrolyte", "Y is a non-electrolyte", "X and Y have the same number of ions"], 0,
          ["Fewer ions give a dimmer bulb, which is Y, not X.", "A non-electrolyte would not light the bulb at all, but the bulb is dim.", "The brightness is different, so the number of ions is different."],
          [("Brightness", "More ions make a brighter bulb."), ("Conclusion", "X has many ions (strong); Y has few (weak).")],
          "Strong and weak electrolytes", "Reasoning", "Brightness depends on the number of free ions."),
        NQ("How many moles of ions are present when 0.30 mol of magnesium chloride, [[MgCl2]], dissolves completely in water?", 0.90,
           [("Ionization", "", r"{{MgCl2 -> Mg^2+ + 2Cl^-}}"), ("Ions per formula unit", "1 Mg2+ and 2 Cl- make 3 ions."), ("Multiply", "", r"0.30 \times 3 = 0.90 \text{ mol}")],
           0.01, "mol", "Counting ions", "Calculation", "Count the ions in one formula unit."),
        Q("Substance W conducts when solid and when molten, and it is not changed chemically. W is most likely", ["an ionic compound", "a covalent compound", "a metal", "a weak electrolyte"], 2,
          ["Ionic compounds do not conduct when solid.", "Most covalent compounds do not conduct.", "A weak electrolyte conducts only in solution and is changed by the current."],
          [("Solid and molten conduction", "Free electrons carry the current."), ("Not decomposed", "A metal is not decomposed by the current.")],
          "Classifying substances", "Reasoning", "Which type of substance conducts as a solid?"),
    ]))

# ===================================================================== 2. Mechanism of electrolysis
SETS.append(practice_set(
    module=M_EL, topic="Mechanism of electrolysis",
    title="Anode, cathode, half-equations and discharge", lesson="chd-mechanism-of-electrolysis",
    questions=[
        Q("In electrolysis, the cathode is the electrode that is", ["joined to the positive terminal of the battery", "joined to the negative terminal of the battery", "where oxidation takes place", "always made of copper"], 1,
          ["That is the anode.", "Oxidation takes place at the anode.", "Cathodes can be graphite, platinum or any suitable metal."],
          [("Definition", "The cathode is joined to the negative terminal, and reduction occurs there.")],
          "Anode and cathode", "Recall", "Positive anode, negative is cathode."),
        Q("During electrolysis of molten lead(II) bromide, bromide ions move to the", ["cathode and gain electrons", "cathode and lose electrons", "anode and gain electrons", "anode and lose electrons"], 3,
          ["Anions are negative and go to the positive electrode, not the cathode.", "Anions go to the anode and they lose electrons.", "Anions lose electrons, they do not gain them."],
          [("Direction", "Negative ions go to the positive anode."), ("Change", "They lose electrons (oxidation).")],
          "Movement of ions", "Concept", "Opposite charges attract."),
        Q("Which is the correct half-equation for the reaction at the anode when molten zinc chloride is electrolysed?",
          [r"[[Zn^2+ + 2e^- -> Zn]]", r"[[2Cl^- -> Cl2 + 2e^-]]", r"[[Cl^- -> Cl2 + e^-]]", r"[[2Cl^- + 2e^- -> Cl2]]"], 1,
          ["That is the cathode half-equation.", "It is not balanced for atoms: one Cl atom on the left, two on the right.", "Electrons are on the wrong side. Anions lose electrons."],
          [("Anode", "Chloride ions lose electrons."), ("Balance", "2 Cl- give Cl2 and 2 electrons.")],
          "Half-equations", "Calculation", "At the anode electrons appear on the right."),
        Q("Dilute sodium sulfate solution is electrolysed using inert electrodes. The gases formed at the cathode and anode are, respectively,", ["oxygen and hydrogen", "hydrogen and oxygen", "sodium and sulfur dioxide", "hydrogen and sulfur trioxide"], 1,
          ["The gases are the wrong way round. Hydrogen forms at the cathode.", "Sodium is not discharged from solution and sulfate is not discharged.", "Sulfate is not discharged, so no sulfur oxide forms."],
          [("Cathode", "H+ is discharged in preference to Na+, giving hydrogen."), ("Anode", "OH- is discharged in preference to sulfate, giving oxygen.")],
          "Preferential discharge", "Application", "Which ions are discharged, those from the salt or from water?"),
        Q("In which solution would chlorine be the main product at the anode with inert electrodes?", ["Dilute sulfuric acid", "Concentrated sodium chloride solution", "Dilute sodium nitrate solution", "Copper(II) sulfate solution"], 1,
          ["There is no chloride, so oxygen forms.", "Nitrate is never discharged; oxygen forms.", "There is no chloride in copper(II) sulfate, so oxygen forms."],
          [("Need", "Chlorine needs chloride ions in good concentration."), ("Answer", "Only concentrated sodium chloride solution qualifies.")],
          "Concentration effect", "Application", "Which solution contains chloride ions?"),
        Q("Which statement about the current in electrolysis is correct?", ["Electrons flow through the electrolyte", "Ions flow through the wires", "Ions carry the current in the electrolyte and electrons in the wires", "Only positive ions carry the current"], 2,
          ["Electrons do not travel through the electrolyte.", "The wires contain electrons, not ions.", "Both positive and negative ions move and carry current."],
          [("In the wires", "Electrons."), ("In the electrolyte", "Ions, positive towards the cathode and negative towards the anode.")],
          "Charge carriers", "Concept", "What carries the charge in each part of the circuit?"),
        NQ("How many moles of electrons are needed to deposit 0.25 mol of aluminium from [[Al^3+]] ions?", 0.75,
           [("Half-equation", "", r"{{Al^3+ + 3e^- -> Al}}"), ("Electrons per atom", "3 electrons for each atom."), ("Total", "", r"0.25 \times 3 = 0.75 \text{ mol}")],
           0.01, "mol", "Electrons and half-equations", "Calculation", "Look at the number of electrons in the half-equation."),
        Q("A student electrolyses dilute sulfuric acid. A gas that relights a glowing splint is collected at one electrode. Which row is correct?",
          ["Anode: [[4OH^- -> 2H2O + O2 + 4e^-]]", "Cathode: [[4OH^- -> 2H2O + O2 + 4e^-]]", "Anode: [[2H^+ + 2e^- -> H2]]", "Cathode: [[SO4^2- -> SO4 + 2e^-]]"], 0,
          ["Oxidation of hydroxide ions occurs at the anode, not the cathode.", "Hydrogen forms at the cathode and is not oxygen.", "Sulfate is not discharged."],
          [("Gas", "A glowing splint relights in oxygen."), ("Where", "Oxygen forms at the anode, where OH- loses electrons.")],
          "Interpreting observations", "Interpretation", "Which gas relights a glowing splint?"),
    ]))

# ===================================================================== 3. Molten, water, brine
SETS.append(practice_set(
    module=M_EL, topic="Electrolysis of common electrolytes",
    title="Molten salts, acidified water and brine", lesson="chd-electrolysis-molten-water-brine",
    questions=[
        Q("Molten sodium chloride is electrolysed. The products at the cathode and anode are", ["hydrogen and chlorine", "sodium and chlorine", "sodium and oxygen", "chlorine and sodium"], 1,
          ["There is no water, so no hydrogen forms.", "There is no water, so no oxygen forms.", "The products are the wrong way round. Metal forms at the cathode."],
          [("Ions present", "Only Na+ and Cl-."), ("Result", "Sodium at the cathode, chlorine at the anode.")],
          "Molten salts", "Recall", "A molten salt has only two kinds of ion."),
        Q("In the electrolysis of acidified water, the volumes of gases at the cathode and anode are in the ratio", ["1 : 1", "1 : 2", "2 : 1", "4 : 1"], 2,
          ["The ratio would be equal only if both gases needed the same number of electrons.", "This is the wrong way round. Hydrogen is double.", "The equation gives four electrons per O2 and two per H2 for the same charge."],
          [("Equation", "", r"{{2H2O -> 2H2 + O2}}"), ("Ratio", "2 volumes of hydrogen to 1 of oxygen, cathode to anode.")],
          "Water electrolysis", "Recall", "Look at the coefficients of H2 and O2.",),
        Q("What is left in solution after concentrated brine is electrolysed with inert electrodes?", ["Sodium hydroxide solution", "Hydrochloric acid", "Sodium chloride only", "Sulfuric acid"], 0,
          ["No H+ builds up; H+ is removed at the cathode.", "Some NaCl remains but the new product is sodium hydroxide.", "There is no sulfate in the solution."],
          [("Cathode", "H+ is removed, so OH- is left over."), ("Result", "With Na+ this gives sodium hydroxide solution.")],
          "Brine electrolysis", "Concept", "Which ions are not discharged?"),
        Q("Which of these is a use of the chlorine made by electrolysis of brine?", ["Making margarine", "Making soap", "Sterilizing drinking water", "Extracting aluminium"], 2,
          ["Hydrogen is used to harden oils for margarine.", "Sodium hydroxide, not chlorine, is used for making soap.", "Sodium hydroxide, not chlorine, is used in purifying bauxite."],
          [("Chlorine", "Kills germs in water and makes bleach.")],
          "Uses of products", "Recall", "Which product kills germs?"),
        NQ("In the electrolysis of acidified water, 15 cm3 of oxygen is collected at the anode. What volume of hydrogen is collected at the cathode, in cm3, at the same conditions?", 30,
           [("Ratio", "H2 : O2 = 2 : 1 by volume."), ("Hydrogen", "", r"2 \times 15 = 30 \text{ cm}^3")],
           0.5, "cm³", "Gas volumes", "Calculation", "Which gas has the greater volume?"),
        Q("Why is dilute sulfuric acid added when water is electrolysed?", ["To take part in the reaction", "To supply ions so that the water conducts", "To make hydrogen at the anode", "To lower the voltage needed to zero"], 1,
          ["The acid is not used up; water is.", "Hydrogen forms at the cathode, not the anode.", "A voltage is still needed to drive the electrolysis."],
          [("Pure water", "It has very few ions and conducts poorly."), ("Acid", "It supplies H+ and sulfate ions so current flows.")],
          "Role of the acid", "Concept", "What does pure water lack?"),
        Q("Concentrated sodium chloride solution is electrolysed. Which equation shows the reaction at the cathode?", [r"[[Na^+ + e^- -> Na]]", r"[[2H^+ + 2e^- -> H2]]", r"[[2Cl^- -> Cl2 + 2e^-]]", r"[[4OH^- -> 2H2O + O2 + 4e^-]]"], 1,
          ["Sodium is high in the series, so its ions are not discharged from solution.", "Chloride is an anion and reacts at the anode.", "Hydroxide is an anion and reacts at the anode."],
          [("Cathode", "Cations only. H+ is discharged in preference to Na+.")],
          "Cathode reactions", "Calculation", "Choose the equation with electrons on the left."),
        Q("A student electrolyses very dilute sodium chloride solution and finds mostly oxygen at the anode. The best explanation is that", ["chloride ions are not present", "the concentration of chloride ions is low, so hydroxide ions are discharged", "sodium ions react with chlorine", "oxygen is more reactive than chlorine"], 1,
          ["Chloride ions are present, but in low concentration.", "Chlorine, once formed, would not react with sodium ions in that way.", "Reactivity of the gases does not decide which ion is discharged; concentration and position in the series do."],
          [("Rule", "In dilute solution there are far fewer chloride ions than hydroxide ions available."), ("Result", "Hydroxide is discharged, giving oxygen.")],
          "Concentration and discharge", "Reasoning", "Think about the concentration effect."),
    ]))

# ===================================================================== 4. Copper sulfate
SETS.append(practice_set(
    module=M_EL, topic="Electrolysis of common electrolytes",
    title="Copper(II) sulfate with inert and copper electrodes", lesson="chd-electrolysis-copper-sulfate",
    questions=[
        Q("Copper(II) sulfate solution is electrolysed with graphite electrodes, as shown. Which statement is correct?",
          ["Copper is deposited on P and oxygen forms at Q", "Copper is deposited on Q and oxygen forms at P", "Copper is deposited on P and hydrogen forms at Q", "Copper is deposited on Q and hydrogen forms at P"], 1,
          ["P is joined to the positive terminal, so P is the anode. Metal ions are not discharged at the anode.",
           "",
           "P is the anode, so no copper forms there, and hydrogen does not form at the cathode because copper ions are discharged first.",
           "Hydrogen is not formed: at the anode, hydroxide ions are discharged and give oxygen."],
          [("Find the anode", "P is joined to the positive terminal of the battery, so P is the anode and Q is the cathode."), ("Cathode Q", "Cu2+ is discharged: copper is deposited."), ("Anode P", "OH- is discharged: oxygen forms.")],
          "Electrolysis of copper(II) sulfate", "Interpretation", "Which electrode is joined to the positive terminal?",
          diagram="f5ch-d-q-electrolysis-pq.svg", diagram_alt="Two graphite electrodes P and Q in copper(II) sulfate solution; P is joined to the positive terminal of the battery and Q to the negative"),
        Q("With graphite electrodes, the blue colour of copper(II) sulfate solution slowly fades because", ["copper ions are removed from the solution", "water is removed", "sulfate ions are used up", "the graphite dissolves"], 0,
          ["Water is used up too, but this does not cause the blue colour to fade.", "Sulfate ions stay in solution.", "Graphite is inert."],
          [("Colour", "It comes from Cu2+ ions."), ("Effect", "They are discharged at the cathode, so less remains.")],
          "Colour change", "Concept", "What gives the solution its blue colour?"),
        Q("The solution becomes acidic after electrolysis with graphite electrodes. Which acid is formed?", ["Hydrochloric acid", "Nitric acid", "Sulfuric acid", "Carbonic acid"], 2,
          ["There is no chloride in the solution.", "There is no nitrate in the solution.", "Carbonic acid is not formed in this electrolysis."],
          [("Left in solution", "H+ ions (from water) and sulfate ions remain."), ("Result", "This is dilute sulfuric acid.")],
          "Acid formed", "Concept", "Which ions remain once Cu2+ and OH- are discharged?"),
        Q("Copper(II) sulfate solution is electrolysed with copper electrodes. Which observation is correct?",
          ["The solution becomes colourless", "The anode gets smaller and the cathode gets bigger", "Bubbles of oxygen form at the anode", "The cathode loses mass"], 1,
          ["Copper ions are replaced as fast as they are removed, so the solution stays blue.", "Oxygen forms only with an inert anode.", "Copper is deposited on the cathode."],
          [("Anode", "Copper dissolves."), ("Cathode", "Copper is deposited.")],
          "Copper electrodes", "Application", "Which electrode dissolves?"),
        NQ("Two pure copper electrodes are used. The cathode gains 2.54 g. By how many grams does the mass of the anode decrease?", 2.54,
           [("Idea", "Copper dissolved at the anode replaces that deposited at the cathode."), ("Answer", "The anode loses the same mass, 2.54 g.")],
           0.01, "g", "Anode and cathode masses", "Reasoning", "Where does the deposited copper come from?"),
        Q("What happens to silver and gold impurities in the impure copper anode during refining?", ["They dissolve and are deposited on the cathode", "They dissolve and stay in solution", "They fall to the bottom as anode sludge", "They form gas at the anode"], 2,
          ["Silver and gold do not dissolve; copper is easier to oxidize than they are.", "They do not dissolve at all.", "They do not form a gas."],
          [("Rule", "Metals less reactive than copper do not dissolve."), ("Result", "They drop off as sludge.")],
          "Copper refining", "Application", "Are silver and gold more or less reactive than copper?"),
        Q("Which row correctly compares the two kinds of electrode in copper(II) sulfate solution?",
          ["Inert: solution stays blue; Copper: solution fades", "Inert: solution fades and becomes acidic; Copper: solution stays blue", "Inert: anode loses mass; Copper: cathode loses mass", "Inert: copper at the anode; Copper: oxygen at the cathode"], 1,
          ["These are the wrong way round.", "Cathodes gain copper in both cases. Inert anodes do not lose mass.", "Oxygen forms at the anode (inert), not at the cathode."],
          [("Inert", "Cu2+ is removed and acid forms."), ("Copper", "Cu2+ is replaced as fast as it is removed.")],
          "Comparison", "Analysis", "Which set-up replaces the copper ions?"),
        NQ("3.175 g of copper is deposited on a cathode from copper(II) sulfate solution. How many moles of copper(II) ions were removed from the solution? (Cu = 63.5)", 0.05,
           [("Use moles = mass / molar mass", "", r"\dfrac{3.175}{63.5} = 0.050 \text{ mol}")],
           0.001, "mol", "Moles from mass", "Calculation", "Divide the mass by the molar mass."),
    ]))

# ===================================================================== 5. Faraday's first law
SETS.append(practice_set(
    module=M_EL, topic="Faraday's laws of electrolysis",
    title="Faraday's first law and Q = It", lesson="chd-faraday-first-law",
    questions=[
        Q("Faraday's first law states that the mass of a substance liberated at an electrode is", ["proportional to the voltage used", "directly proportional to the quantity of electricity passed", "inversely proportional to the time", "independent of the current"], 1,
          ["The law concerns charge, not voltage.", "More time would give more mass, not less.", "The mass depends on the current and time together (the charge)."],
          [("Law", "m is directly proportional to Q (charge).")],
          "Statement of the law", "Recall", "What is the law linking mass and the amount of electricity?"),
        Q("The Faraday constant is the charge carried by", ["one electron", "one mole of electrons", "one mole of any ion", "one coulomb of electrons"], 1,
          ["One electron carries a tiny charge, not 96 500 C.", "An ion may carry more than one electron's charge, so this changes with the ion.", "One coulomb is just the unit of charge."],
          [("Definition", "F = 96 500 C per mole of electrons.")],
          "Faraday constant", "Recall", "It is a charge per mole of something."),
        NQ("A current of 3.0 A flows for 10 minutes. What quantity of electricity passes, in coulombs?", 1800,
           [("Time in seconds", "", r"10 \times 60 = 600 \text{ s}"), ("Q = It", "", r"3.0 \times 600 = 1800 \text{ C}")],
           1, "C", "Q = It", "Calculation", "Convert the time to seconds first."),
        Q("How many moles of electrons are needed to deposit one mole of copper from [[Cu^2+]]?", ["1", "2", "3", "0.5"], 1,
          ["That is for silver, which needs one electron per ion.", "", "That is for aluminium.", "That would be the moles of copper deposited by 1 mole of electrons."],
          [("Half-equation", "", r"{{Cu^2+ + 2e^- -> Cu}}"), ("Answer", "Two electrons per atom, so 2 mol per mole of copper.")],
          "Electrons per ion", "Concept", "Write the half-equation."),
        NQ("A current of 5.0 A flows for 20 minutes through copper(II) sulfate solution. Calculate the mass of copper deposited, in g. (Cu = 63.5; F = 96 500 C/mol)", 1.97,
           [("Charge", "", r"Q = 5.0 \times 1200 = 6000 \text{ C}"), ("Moles of electrons", "", r"\dfrac{6000}{96\,500} = 0.0622 \text{ mol}"),
            ("Moles of Cu", "z = 2.", r"n(\mathrm{Cu}) = 0.0311 \text{ mol}"), ("Mass", "", r"0.0311 \times 63.5 = 1.97 \text{ g}")],
           0.02, "g", "Mass from current and time", "Calculation", "Use the four-step plan: Q, moles of electrons, moles of copper, mass."),
        Q("If the current is doubled and the time is halved, the mass of metal deposited will", ["double", "halve", "stay the same", "quarter"], 2,
          ["Doubling the current doubles the charge but halving the time halves it.", "The charge is unchanged, not halved.", "The charge does not fall to a quarter."],
          [("Charge", "Q = It. Doubling I and halving t keeps the product the same."), ("Mass", "It depends on Q, so it is unchanged.")],
          "Proportionality", "Reasoning", "Work out what happens to I times t."),
        NQ("How long, in seconds, will a current of 0.50 A take to deposit 1.08 g of silver from silver nitrate solution? (Ag = 108; F = 96 500 C/mol)", 1930,
           [("Moles of Ag", "", r"\dfrac{1.08}{108} = 0.0100 \text{ mol}"), ("Charge", "One electron per atom.", r"0.0100 \times 96\,500 = 965 \text{ C}"), ("Time", "", r"t = \dfrac{965}{0.50} = 1930 \text{ s}")],
           10, "s", "Time from mass", "Calculation", "Find the charge first, then divide by the current."),
        Q("Which quantity of electricity is needed to deposit 0.10 mol of aluminium from [[Al^3+]]? (F = 96 500 C/mol)", ["9650 C", "19 300 C", "28 950 C", "96 500 C"], 2,
          ["This is for 0.10 mol of electrons only.", "This would be for 0.10 mol of copper (2 electrons per atom).", "This is for 1 mol of electrons, not 0.30 mol."],
          [("Electrons", "", r"0.10 \times 3 = 0.30 \text{ mol}"), ("Charge", "", r"0.30 \times 96\,500 = 28\,950 \text{ C}")],
          "Charge for a given amount", "Calculation", "How many electrons does each aluminium ion need?"),
    ]))

# ===================================================================== 6. Faraday's second law
SETS.append(practice_set(
    module=M_EL, topic="Faraday's laws of electrolysis",
    title="Faraday's second law, gas volumes and cells in series", lesson="chd-faraday-second-law",
    questions=[
        Q("Which of these is the equivalent mass of copper in copper(II) ions? (Cu = 63.5)", ["63.5", "127", "31.75", "21.2"], 2,
          ["This is the atomic mass, without dividing by the charge.", "This multiplies by 2 instead of dividing.", "This divides by 3, which is the charge on aluminium."],
          [("Rule", "Equivalent mass = A / z."), ("Copper", "", r"\dfrac{63.5}{2} = 31.75")],
          "Equivalent mass", "Calculation", "Divide by the charge on the ion."),
        Q("The same quantity of electricity is passed through molten sodium chloride and molten aluminium oxide. The moles of sodium formed compared with the moles of aluminium formed will be", ["equal", "one third as many", "three times as many", "twice as many"], 2,
          ["That would need the same number of electrons per atom.", "This is the wrong way round.", "The ratio of electrons needed is 1 to 3, not 1 to 2."],
          [("Sodium", "1 electron per atom."), ("Aluminium", "3 electrons per atom, so 3 times as many moles of sodium.")],
          "Second law in moles", "Concept", "Compare electrons per atom."),
        NQ("The same current flows for the same time through copper(II) sulfate and silver nitrate solutions in series. 0.635 g of copper is deposited. What mass of silver is deposited, in g? (Cu = 63.5, Ag = 108)", 2.16,
           [("Moles of Cu", "", r"\dfrac{0.635}{63.5} = 0.0100 \text{ mol}"), ("Moles of electrons", "", r"2 \times 0.0100 = 0.0200 \text{ mol}"), ("Moles of Ag", "One electron per atom, 0.0200 mol."), ("Mass", "", r"0.0200 \times 108 = 2.16 \text{ g}")],
           0.02, "g", "Cells in series", "Calculation", "The moles of electrons are the same in both cells."),
        Q("How many moles of hydrogen form at the cathode when 0.040 mol of electrons passes through dilute sulfuric acid?", ["0.010 mol", "0.020 mol", "0.040 mol", "0.080 mol"], 1,
          ["This divides by 4, which applies to oxygen.", "", "This assumes one electron per molecule of hydrogen.", "This multiplies by 2 instead of dividing."],
          [("Half-equation", "", r"{{2H^+ + 2e^- -> H2}}"), ("Answer", "2 electrons per H2, so 0.040/2 = 0.020 mol.")],
          "Gas from electrons", "Calculation", "How many electrons make one molecule of hydrogen?"),
        NQ("A current of 2.0 A flows for 965 s through molten sodium chloride. Calculate the volume of chlorine formed, in dm3, at room temperature and pressure (24 dm3 per mole). (F = 96 500 C/mol)", 0.24,
           [("Charge", "", r"Q = 2.0 \times 965 = 1930 \text{ C}"), ("Moles of electrons", "", r"\dfrac{1930}{96\,500} = 0.020 \text{ mol}"), ("Moles of Cl2", "2 electrons per molecule: 0.010 mol."), ("Volume", "", r"0.010 \times 24 = 0.24 \text{ dm}^3")],
           0.005, "dm³", "Gas volume from charge", "Calculation", "Two electrons make one molecule of chlorine."),
        Q("One mole of electrons passes through dilute sulfuric acid. Which statement about the gases at room temperature and pressure is correct?", ["Oxygen has the greatest volume", "Hydrogen has twice the volume of oxygen", "Hydrogen and oxygen have equal volumes", "Oxygen has twice the volume of hydrogen"], 1,
          ["Oxygen needs 4 electrons per molecule, so it has the smaller volume.", "", "Hydrogen needs 2 electrons per molecule and oxygen needs 4, so the volumes are not equal.", "This is the reverse of the true ratio."],
          [("Hydrogen", "0.5 mol, 12 dm3."), ("Oxygen", "0.25 mol, 6 dm3."), ("Answer", "Hydrogen has twice the volume of oxygen.")],
          "Comparing gases", "Reasoning", "Count electrons per molecule of each gas."),
        Q("A charge of 2895 C deposits 0.27 g of a metal M of relative atomic mass 27. What is the charge on the ion of M?", ["1+", "2+", "3+", "4+"], 2,
          ["That would deposit 0.90 g.", "That would deposit 0.405 g.", "", "That would deposit 0.2025 g."],
          [("Moles of electrons", "", r"\dfrac{2895}{96\,500} = 0.030 \text{ mol}"), ("Moles of M", "", r"\dfrac{0.27}{27} = 0.010 \text{ mol}"), ("Ratio", "0.030 / 0.010 = 3, so the ion is M3+.")],
          "Charge on an ion", "Calculation", "Compare the moles of electrons with the moles of metal."),
        Q("Faraday's second law is best stated as: the same quantity of electricity liberates masses that are proportional to", ["the relative atomic masses", "the equivalent masses (A divided by the charge on the ion)", "the densities", "the atomic numbers"], 1,
          ["The charge on the ion also matters.", "", "Density plays no part.", "Atomic number does not appear in the law."],
          [("Law", "Masses are in the ratio of equivalent masses, A divided by z.")],
          "Statement of the law", "Recall", "What combines relative atomic mass and the charge on an ion?"),
    ]))

# ===================================================================== 7. Series, cells, electroplating
SETS.append(practice_set(
    module=M_EL, topic="Electrochemical series, cells and electroplating",
    title="Simple cells, the series and electroplating", lesson="chd-series-cells-electroplating",
    questions=[
        Q("In a simple cell made of zinc and copper in dilute sulfuric acid, the negative electrode is", ["copper, because it is less reactive", "zinc, because it is more reactive", "the electrolyte", "whichever electrode is larger"], 1,
          ["The less reactive metal is the positive electrode.", "The electrolyte is not an electrode.", "Size does not decide polarity."],
          [("Rule", "The more reactive metal loses electrons more easily, so it is negative.")],
          "Polarity of a simple cell", "Recall", "Which metal is higher in the series?"),
        Q("Which pair of metals, with dilute acid as the electrolyte, gives the largest voltage?", ["Zinc and iron", "Magnesium and copper", "Iron and copper", "Zinc and copper"], 1,
          ["These are close together in the series.", "", "Iron and copper are closer together than magnesium and copper.", "Zinc and copper are closer together than magnesium and copper."],
          [("Rule", "The further apart in the series, the larger the voltage."), ("Answer", "Magnesium and copper are furthest apart.")],
          "Voltage and the series", "Application", "Find the pair with the greatest gap."),
        Q("X and Y are two different metals in dilute sulfuric acid in the cell shown. Electrons flow through the wire as shown, and bubbles form on Y. Which statement is correct?",
          ["X is the negative electrode and is more reactive than Y", "Y is the negative electrode and is more reactive than X", "X is the positive electrode and hydrogen forms on X", "X and Y are equally reactive"], 0,
          ["", "Electrons flow from the negative electrode, which is X, not Y.", "Hydrogen forms on Y, the positive electrode.", "Two metals of equal reactivity would give no voltage and no flow."],
          [("Direction", "Electrons leave the negative electrode and flow to the positive one, so X is negative and Y is positive."), ("Reactivity", "The negative electrode is the more reactive metal, so X is more reactive.")],
          "Reading a cell diagram", "Interpretation", "Electrons flow from the negative electrode.",
          diagram="f5ch-d-q-cell-xy.svg", diagram_alt="Two metals X and Y in dilute sulfuric acid joined through a voltmeter; an arrow shows electrons flowing from X to Y and bubbles form on Y"),
        Q("A spoon is to be silver-plated. Which set-up is correct?", ["Spoon as anode, silver as cathode, copper(II) sulfate solution", "Spoon as cathode, silver as anode, silver nitrate solution", "Spoon as anode, silver as cathode, silver nitrate solution", "Spoon as cathode, copper as anode, silver nitrate solution"], 1,
          ["The object must be the cathode, and the solution must contain silver ions.", "", "The object must be the cathode.", "The anode must be silver so that silver ions replace those deposited."],
          [("Rule", "Object is the cathode, plating metal is the anode, solution has ions of the plating metal.")],
          "Electroplating set-up", "Application", "Where must metal ions be reduced?"),
        Q("What happens to the concentration of silver nitrate solution during silver-plating with a silver anode?", ["It falls steadily", "It stays almost the same", "It rises steadily", "It becomes zero"], 1,
          ["The silver ions removed at the cathode are replaced at the anode.", "Silver comes from the anode, not from the solution, so the concentration does not rise.", "Silver ions are replaced, so the solution is not used up."],
          [("Anode", "Ag becomes Ag+ and enters the solution."), ("Cathode", "Ag+ is removed. The two balance.")],
          "Steady concentration", "Reasoning", "Where does the new silver ion come from?"),
        NQ("A spoon is silver-plated using a current of 0.50 A for 40 minutes. What mass of silver is deposited, in g? (Ag = 108; F = 96 500 C/mol)", 1.34,
           [("Charge", "", r"Q = 0.50 \times 2400 = 1200 \text{ C}"), ("Moles of electrons", "", r"\dfrac{1200}{96\,500} = 0.01244 \text{ mol}"), ("Moles and mass of Ag", "One electron per atom.", r"0.01244 \times 108 = 1.34 \text{ g}")],
           0.02, "g", "Plating calculation", "Calculation", "Time in seconds first, then charge, then moles."),
        Q("Which reason does NOT explain why metals are electroplated?", ["To protect against corrosion", "To improve appearance", "To make the surface harder-wearing", "To make the object lighter"], 3,
          ["This is a reason for plating.", "This is a reason for plating.", "This is a reason for plating, for example chromium on car parts."],
          [("Reasons", "Protection, appearance and hardness. A thin coat does not make an object lighter.")],
          "Uses of plating", "Recall", "Which choice is not a reason?"),
        Q("Which statement correctly compares an electrolytic cell with a simple cell?", ["Both change chemical energy to electrical energy", "In both cells, oxidation takes place at the anode", "In both cells, the anode is positive", "Both need a battery"], 1,
          ["An electrolytic cell changes electrical energy into chemical energy.", "", "The anode is positive in an electrolytic cell and negative in a simple cell.", "A simple cell is itself the source of current."],
          [("Comparison", "Oxidation is always at the anode; the sign of the anode differs.")],
          "Cells compared", "Analysis", "What is the same in the two cells?"),
    ]))

# ===================================================================== 8. Hydrogen, oxygen and air
SETS.append(practice_set(
    module=M_IN, topic="Hydrogen, oxygen, air and water",
    title="Hydrogen, oxygen and the composition of air", lesson="chd-hydrogen-oxygen-air",
    questions=[
        Q("Which test shows that a gas is hydrogen?", ["It relights a glowing splint", "It burns with a squeaky pop with a lighted splint", "It turns limewater milky", "It turns damp litmus paper white"], 1,
          ["This is the test for oxygen.", "", "This is the test for carbon dioxide.", "This is the test for chlorine."],
          [("Test", "A lighted splint at the mouth of the tube gives a squeaky pop.")],
          "Test for hydrogen", "Recall", "Which gas burns explosively with a pop?"),
        Q("Which pair of substances is used to make hydrogen in the laboratory?", ["Copper and dilute hydrochloric acid", "Zinc and dilute hydrochloric acid", "Marble and dilute hydrochloric acid", "Zinc and sodium chloride solution"], 1,
          ["Copper is below hydrogen and does not react with dilute acid.", "Marble gives carbon dioxide.", "Zinc does not react with salt solution."],
          [("Rule", "A metal above hydrogen reacts with dilute acid to give hydrogen.")],
          "Preparing hydrogen", "Recall", "The metal must be above hydrogen in the series."),
        Q("The approximate percentage by volume of oxygen in clean dry air is", ["1%", "21%", "78%", "50%"], 1,
          ["This is about the percentage of argon.", "", "This is the percentage of nitrogen.", "Oxygen is a fifth of air, not half."],
          [("Composition", "Nitrogen 78%, oxygen 21%, argon about 1%, carbon dioxide 0.04%.")],
          "Composition of air", "Recall", "Oxygen is about one fifth of air."),
        NQ("In an experiment, 100 cm3 of air is passed over heated copper until the volume stops changing. The final volume of gas, at the original temperature, is 79 cm3. What is the percentage of oxygen in the air?", 21,
           [("Volume of oxygen", "", r"100 - 79 = 21 \text{ cm}^3"), ("Percentage", "", r"\dfrac{21}{100} \times 100 = 21\%")],
           0.5, "%", "Percentage of oxygen", "Calculation", "Copper takes oxygen only."),
        Q("In which order do the gases boil off when liquid air is slowly warmed?", ["Oxygen, argon, nitrogen", "Nitrogen, argon, oxygen", "Argon, nitrogen, oxygen", "Nitrogen, oxygen, argon"], 1,
          ["This is the reverse order of boiling points.", "", "Nitrogen has the lowest boiling point, so it is first.", "Argon boils below oxygen."],
          [("Boiling points", "Nitrogen -196, argon -186, oxygen -183 degrees Celsius."), ("Order", "Lowest boiling point first.")],
          "Fractional distillation of air", "Application", "The gas with the lowest boiling point boils first."),
        Q("Hydrogen is passed over hot black copper(II) oxide. What is observed and what does it show?", ["The oxide turns pink-brown; hydrogen is a reducing agent", "The oxide turns white; hydrogen is an oxidizing agent", "The oxide turns blue; hydrogen is an acid", "There is no change; hydrogen is unreactive"], 0,
          ["Copper oxide is reduced to copper, which is not white.", "Hydrogen does not turn it blue, and hydrogen is not an acid here.", "Hot hydrogen reduces copper oxide."],
          [("Reaction", "", r"{{CuO + H2 -> Cu + H2O}}"), ("Meaning", "Hydrogen takes oxygen, so it is a reducing agent.")],
          "Hydrogen as a reducing agent", "Interpretation", "Copper(II) oxide loses oxygen."),
        NQ("6.5 g of zinc reacts with excess dilute hydrochloric acid. What volume of hydrogen forms at room temperature and pressure, in dm3? (Zn = 65; 24 dm3 per mole)", 2.4,
           [("Moles of zinc", "", r"\dfrac{6.5}{65} = 0.10 \text{ mol}"), ("Moles of hydrogen", "From [[Zn + 2HCl -> ZnCl2 + H2]], 1 : 1: 0.10 mol."), ("Volume", "", r"0.10 \times 24 = 2.4 \text{ dm}^3")],
           0.05, "dm³", "Gas volume from mass", "Calculation", "Find moles of zinc, then use the mole ratio."),
        Q("Which of these is a harmful air pollutant that forms when carbon-containing fuels burn in too little oxygen?", ["Nitrogen", "Carbon monoxide", "Argon", "Oxygen"], 1,
          ["Nitrogen is a harmless main gas of air.", "", "Argon is an unreactive gas in air.", "Oxygen is essential for life."],
          [("Pollutant", "Incomplete combustion gives carbon monoxide, which is poisonous.")],
          "Air pollution", "Application", "What forms in incomplete combustion?"),
    ]))

# ===================================================================== 9. Water, hardness, treatment
SETS.append(practice_set(
    module=M_IN, topic="Hydrogen, oxygen, air and water",
    title="Water tests, hardness and treatment", lesson="chd-water-hardness-treatment",
    questions=[
        Q("A colourless liquid turns anhydrous copper(II) sulfate from white to blue. This shows that the liquid", ["is pure water", "contains water", "is an acid", "contains copper ions"], 1,
          ["The test shows that water is present, but not that it is pure. Pure water has a boiling point of exactly 100 degrees Celsius.", "", "The test does not detect acids.", "The blue colour is the hydrated form of copper(II) sulfate formed with water; it is not caused by copper ions in the liquid."],
          [("Test", "Anhydrous copper(II) sulfate takes up water and becomes blue hydrated crystals."), ("Meaning", "Water is present, whatever else is in the liquid.")],
          "Test for water", "Recall", "Does the test show purity?"),
        Q("Which ions cause the hardness of water?", ["Sodium and potassium ions", "Calcium and magnesium ions", "Chloride and nitrate ions", "Hydrogen and hydroxide ions"], 1,
          ["Compounds of sodium and potassium do not make water hard.", "", "These anions do not cause hardness by themselves.", "These ions are in all water."],
          [("Cause", "Dissolved calcium and magnesium compounds.")],
          "Cause of hardness", "Recall", "Which metal ions react with soap?"),
        Q("Which substance causes temporary hardness of water?", ["Calcium sulfate", "Calcium hydrogencarbonate", "Magnesium chloride", "Sodium carbonate"], 1,
          ["Calcium sulfate causes permanent hardness.", "", "Magnesium chloride causes permanent hardness.", "Sodium carbonate softens water; it does not cause hardness."],
          [("Rule", "Hydrogencarbonates cause temporary hardness. They break down on boiling.")],
          "Temporary hardness", "Recall", "Which compound is removed by boiling?"),
        Q("Four samples of water are tested with soap solution before and after boiling. Sample P: scum before, lather after. Sample Q: scum before, scum after. Sample R: lather before and after. Which sample is permanently hard?", ["P", "Q", "R", "P and Q"], 1,
          ["P is temporary hard water, because boiling removed its hardness.", "", "R is soft water.", "P is temporary hard, not permanently hard."],
          [("P", "Boiling cured it: temporary hardness."), ("Q", "Boiling did not cure it: permanent hardness."), ("R", "Lathers at once: soft.")],
          "Identifying hardness", "Interpretation", "Which sample still forms scum after boiling?"),
        NQ("Boiling temporary hard water decomposes calcium hydrogencarbonate: [[Ca(HCO3)2 -> CaCO3 + H2O + CO2]]. What mass of calcium carbonate forms from 8.1 g of calcium hydrogencarbonate, in g? (Ca = 40, H = 1, C = 12, O = 16)", 5.0,
           [("Molar mass", "", r"M_r(\mathrm{Ca(HCO_3)_2}) = 40 + 2(1 + 12 + 48) = 162"), ("Moles", "", r"\dfrac{8.1}{162} = 0.050 \text{ mol}"), ("Mass of CaCO3", "1 : 1, M of CaCO3 = 100.", r"0.050 \times 100 = 5.0 \text{ g}")],
           0.1, "g", "Mass from equation", "Calculation", "Find moles of the hydrogencarbonate first."),
        Q("Why does washing soda (sodium carbonate) soften both temporary and permanent hard water?", ["It removes sodium ions", "Carbonate ions precipitate calcium ions as calcium carbonate", "It kills bacteria", "It decomposes calcium hydrogencarbonate on heating"], 1,
          ["Sodium ions do not cause hardness, and washing soda adds them.", "", "Killing bacteria is the job of chlorine.", "Washing soda works in cold water by precipitation, not by heating."],
          [("Reaction", "", r"{{Ca^2+ + CO3^2- -> CaCO3}}"), ("Result", "Insoluble calcium carbonate is removed. This works whatever the source of the calcium ions.")],
          "Washing soda", "Concept", "What does carbonate do to calcium ions?"),
        Q("In the treatment of river water for a town supply, which step comes immediately after alum is added in the settling tank?", ["Chlorination", "Filtration through sand", "Screening", "Distillation"], 1,
          ["Chlorine is added at the end, after the water is clear.", "", "Screening is done at the start of the process.", "Distillation is not part of town water treatment."],
          [("Order", "Screening, settling with alum, sand filtration, then chlorination.")],
          "Water treatment order", "Application", "Which step removes the small particles left over?"),
        Q("Which is an advantage of hard water?", ["It saves soap", "It prevents scale in kettles", "It supplies calcium for teeth and bones", "It lathers easily"], 2,
          ["Hard water wastes soap.", "Hard water forms scale.", "Hard water does not lather easily."],
          [("Advantage", "The calcium ions in hard water help to build teeth and bones.")],
          "Effects of hardness", "Recall", "What useful mineral does hard water contain?"),
    ]))

# ===================================================================== 10. Carbon
SETS.append(practice_set(
    module=M_IN, topic="Carbon and its compounds",
    title="Allotropes of carbon, CO, CO2 and carbonates", lesson="chd-carbon-and-compounds",
    questions=[
        Q("Diamond is very hard because", ["its atoms are held by weak forces", "each carbon atom is joined to four others by strong covalent bonds in a giant structure", "it has layers that slide", "it contains free electrons"], 1,
          ["Diamond has strong bonds, not weak ones.", "", "Sliding layers are in graphite.", "Free electrons are in graphite; diamond has none."],
          [("Structure", "Each atom has four strong bonds in a rigid lattice.")],
          "Diamond", "Concept", "Think about the bonds in each direction."),
        Q("Graphite conducts electricity because", ["it contains ions", "each atom has a free (delocalized) electron", "it contains water", "it is a metal"], 1,
          ["Graphite is a non-metal with no ions.", "", "Graphite does not contain water.", "Carbon is a non-metal."],
          [("Bonding", "Each carbon atom uses three electrons for bonding.", ), ("The fourth", "It is free to move between the layers.")],
          "Graphite", "Concept", "Each carbon atom has 4 outer electrons but only 3 bonds."),
        Q("Which of these is a non-crystalline (amorphous) form of carbon?", ["Diamond", "Graphite", "Charcoal", "A fullerene"], 2,
          ["Diamond is a crystalline allotrope.", "Graphite is a crystalline allotrope.", "Fullerenes are crystalline molecular forms."],
          [("Crystalline", "Diamond, graphite and fullerenes have regular structures."), ("Non-crystalline", "Charcoal, coke and soot have no regular pattern.")],
          "Forms of carbon", "Recall", "Which has no regular lattice?"),
        Q("Why is carbon monoxide dangerous to people?", ["It is very acidic", "It combines with haemoglobin and stops blood carrying oxygen", "It makes the air too hot", "It dissolves in blood and forms acid"], 1,
          ["Carbon monoxide is a neutral oxide.", "", "Heating is not the reason.", "It does not form an acid in blood."],
          [("Danger", "It is colourless and odourless and stops oxygen being carried."), ("Safety", "Never burn charcoal in a closed room.")],
          "Carbon monoxide", "Application", "What does it do to the blood?"),
        Q("A gas turns limewater milky and then clear again when bubbled in for a long time. The gas is", ["oxygen", "carbon monoxide", "carbon dioxide", "hydrogen chloride"], 2,
          ["Oxygen does not affect limewater.", "Carbon monoxide does not react with limewater.", "Hydrogen chloride is acidic and would not give the milky precipitate."],
          [("First", "Milky: insoluble calcium carbonate."), ("Then", "Clears: soluble calcium hydrogencarbonate in excess carbon dioxide.")],
          "Test for carbon dioxide", "Interpretation", "Which gas turns limewater milky?"),
        Q("Why is dilute sulfuric acid not used to prepare carbon dioxide from marble chips?", ["It is too weak", "The insoluble calcium sulfate formed stops the reaction", "It makes carbon monoxide", "It makes the gas dissolve"], 1,
          ["Dilute sulfuric acid is a strong acid.", "", "Carbon dioxide forms, not carbon monoxide.", "The gas is only slightly soluble."],
          [("Reaction", "Calcium sulfate is insoluble and coats the marble.")],
          "Preparation of CO2", "Reasoning", "What coats the marble?"),
        NQ("What mass of calcium carbonate must be heated to give 4.8 dm3 of carbon dioxide at room temperature and pressure, in g? (Ca = 40, C = 12, O = 16; 24 dm3 per mole)", 20,
           [("Moles of CO2", "", r"\dfrac{4.8}{24} = 0.20 \text{ mol}"), ("Mole ratio", "From [[CaCO3 -> CaO + CO2]], 1 : 1, so 0.20 mol of CaCO3."), ("Mass", "", r"0.20 \times 100 = 20 \text{ g}")],
           0.5, "g", "Mass from gas volume", "Calculation", "Find the moles of gas first."),
        Q("A white carbonate is heated strongly in a Bunsen flame and does not change. It fizzes with dilute acid. The carbonate is most likely", ["copper(II) carbonate", "calcium carbonate", "zinc carbonate", "sodium carbonate"], 3,
          ["Copper carbonate would turn black.", "Calcium carbonate decomposes in a strong Bunsen flame.", "Zinc carbonate decomposes to an oxide that is yellow when hot."],
          [("Stability", "Carbonates of sodium and potassium resist heating with a Bunsen burner."), ("Acid", "All carbonates fizz.")],
          "Thermal decomposition", "Reasoning", "Which metal is very high in the series?"),
    ]))

# ===================================================================== 11. Nitrogen
SETS.append(practice_set(
    module=M_IN, topic="Nitrogen and its compounds",
    title="Ammonia, the Haber process and the nitrogen cycle", lesson="chd-nitrogen-ammonia-haber",
    questions=[
        Q("Nitrogen is very unreactive because", ["it is a metal", "its two atoms are joined by a very strong triple bond", "it has no electrons", "it is a liquid"], 1,
          ["Nitrogen is a non-metal.", "", "Nitrogen atoms have electrons.", "Nitrogen is a gas at room temperature."],
          [("Bonding", "N2 has a triple covalent bond that needs a lot of energy to break.")],
          "Unreactivity of nitrogen", "Concept", "Think about the bond between the two atoms."),
        Q("Ammonia is collected by upward delivery because it is", ["very soluble in water and denser than air", "less dense than air", "acidic", "poisonous"], 1,
          ["Ammonia is very soluble, but it is not denser than air; it is less dense, and that is why upward delivery works.", "", "Ammonia is alkaline, not acidic.", "Poison does not determine the collection method."],
          [("Density", "Ammonia is less dense than air, so it rises and pushes the air downwards out of the jar.")],
          "Collecting ammonia", "Concept", "Compare its density with that of air."),
        Q("Ammonia gas is identified by", ["turning damp red litmus blue", "turning limewater milky", "relighting a glowing splint", "bleaching damp litmus"], 0,
          ["That is carbon dioxide.", "That is oxygen.", "That is chlorine."],
          [("Test", "Ammonia is alkaline, so it turns damp red litmus blue. It also gives white fumes with hydrogen chloride.")],
          "Test for ammonia", "Recall", "Is ammonia acidic or alkaline?"),
        Q("Which conditions are used in the Haber process?", ["Nickel catalyst, 450 degrees Celsius, 1 atmosphere", "Iron catalyst, 450 degrees Celsius, about 200 atmospheres", "Vanadium(V) oxide, 450 degrees Celsius, 2 atmospheres", "Platinum, 800 degrees Celsius, 200 atmospheres"], 1,
          ["Nickel is used in hardening oils, and 1 atmosphere is too low for a good yield.", "", "Vanadium(V) oxide is the catalyst of the Contact process.", "Platinum is used in making nitric acid from ammonia."],
          [("Haber", "Iron catalyst, about 450 degrees Celsius and about 200 atm.")],
          "Haber conditions", "Recall", "Name the catalyst first."),
        Q("Why does increasing the pressure raise the yield of ammonia?", ["It makes the catalyst work faster", "The forward reaction produces fewer gas molecules (4 to 2)", "It makes the reaction endothermic", "It adds more nitrogen"], 1,
          ["A catalyst's action is not changed by pressure.", "", "The energy change of the reaction does not depend on pressure.", "Pressure does not add reactants."],
          [("Le Chatelier", "A higher pressure favours the side with fewer gas molecules."), ("Count", "4 molecules (N2 and 3 H2) become 2 molecules (2 NH3).")],
          "Pressure and yield", "Reasoning", "Count the molecules of gas on each side."),
        Q("Which process in the nitrogen cycle is carried out by bacteria in the root nodules of beans?", ["Burning of fuel", "Fixation of nitrogen from the air", "Decay of dead plants", "Making of nitric acid in factories"], 1,
          ["Burning is not done by bacteria.", "", "Decay is done by decomposers in the soil, not by nodule bacteria.", "Making nitric acid is an industrial process."],
          [("Role", "Nitrogen-fixing bacteria change nitrogen gas into nitrogen compounds that plants can use.")],
          "Nitrogen cycle", "Application", "What do the nodule bacteria fix?"),
        NQ("Calculate the percentage of nitrogen by mass in urea, [[CO(NH2)2]]. (C = 12, O = 16, N = 14, H = 1)", 46.7,
           [("Molar mass", "", r"12 + 16 + 2(14 + 2) = 60"), ("Nitrogen", "", r"\dfrac{28}{60} \times 100 = 46.7\%")],
           0.2, "%", "Percentage composition", "Calculation", "There are two nitrogen atoms in the formula."),
        NQ("What mass of ammonia forms from 56 g of nitrogen with excess hydrogen, in g? (N = 14, H = 1)", 68,
           [("Moles of N2", "", r"\dfrac{56}{28} = 2.0 \text{ mol}"), ("Mole ratio", "From [[N2 + 3H2 <=> 2NH3]], 1 : 2, so 4.0 mol of NH3."), ("Mass", "", r"4.0 \times 17 = 68 \text{ g}")],
           0.5, "g", "Mass from equation", "Calculation", "Use the mole ratio 1 : 2."),
    ]))

# ===================================================================== 12. Sulfur
SETS.append(practice_set(
    module=M_IN, topic="Sulfur and its compounds",
    title="Sulfur, sulfur dioxide and the Contact process", lesson="chd-sulfur-contact-process",
    questions=[
        Q("The two crystalline allotropes of sulfur are", ["diamond and graphite", "rhombic and monoclinic", "white and red", "plastic and liquid"], 1,
          ["Those are the allotropes of carbon.", "", "White and red are allotropes of phosphorus.", "Plastic sulfur is a non-crystalline form, and liquid is a state, not an allotrope."],
          [("Allotropes", "Rhombic and monoclinic sulfur; both contain rings of eight atoms.")],
          "Allotropes of sulfur", "Recall", "They are named after their crystal shapes."),
        Q("Which test confirms that a gas is sulfur dioxide?", ["It turns acidified potassium dichromate(VI) from orange to green", "It turns damp red litmus blue", "It relights a glowing splint", "It turns limewater milky only"], 0,
          ["That is ammonia.", "That is oxygen.", "Carbon dioxide also turns limewater milky, so this test alone does not identify SO2."],
          [("Test", "Sulfur dioxide is a reducing agent; it changes orange dichromate(VI) to green.")],
          "Test for sulfur dioxide", "Recall", "Look for a colour change with an oxidizing agent."),
        Q("Which environmental problem is caused by sulfur dioxide in the air?", ["Depletion of ozone", "Acid rain", "Global warming by trapping heat", "Hard water"], 1,
          ["Ozone depletion is linked to CFC gases.", "", "Global warming is mainly linked to carbon dioxide and methane.", "Hard water is caused by calcium and magnesium compounds."],
          [("Cause", "Sulfur dioxide dissolves in rain to form acids.")],
          "Acid rain", "Application", "Is sulfur dioxide acidic or neutral?"),
        Q("What is the catalyst in the Contact process?", ["Iron", "Vanadium(V) oxide", "Platinum", "Nickel"], 1,
          ["Iron is the Haber process catalyst.", "", "Platinum is used in nitric acid manufacture.", "Nickel is used to harden oils."],
          [("Contact", "Vanadium(V) oxide catalyzes the oxidation of sulfur dioxide.")],
          "Contact catalyst", "Recall", "Which catalyst belongs to this process?"),
        Q("In the Contact process the sulfur trioxide is first dissolved in", ["water", "concentrated sulfuric acid", "dilute sulfuric acid", "sodium hydroxide solution"], 1,
          ["Dissolving it directly in water makes a fine mist of acid.", "", "Dilute acid would behave like water.", "That would make a salt, not sulfuric acid."],
          [("Stage 3", "Sulfur trioxide in concentrated acid forms oleum; adding water to oleum gives sulfuric acid.")],
          "Absorption stage", "Concept", "Why is water not used directly?"),
        Q("Concentrated sulfuric acid is added to sugar and the sugar turns black. The property of the acid shown is", ["acid properties", "dehydration", "reduction", "weak acidity"], 1,
          ["Acidity would not turn sugar black.", "", "The acid is not acting as a reducing agent here.", "Sulfuric acid is a strong acid."],
          [("Change", "The acid removes water from sugar and leaves black carbon.")],
          "Dehydrating agent", "Application", "What is removed from the sugar?"),
        NQ("20 dm3 of sulfur dioxide reacts with oxygen to form sulfur trioxide. What volume of oxygen is needed, in dm3, at the same temperature and pressure?", 10,
           [("Equation", "", r"{{2SO2 + O2 -> 2SO3}}"), ("Ratio", "2 volumes of SO2 need 1 volume of O2."), ("Oxygen", "", r"\dfrac{20}{2} = 10 \text{ dm}^3")],
           0.1, "dm³", "Gas volumes", "Calculation", "Use the coefficients as volume ratios."),
        NQ("What mass of sulfuric acid, in tonnes, can be made from 16 tonnes of sulfur if all the sulfur ends up as sulfuric acid? (S = 32, H = 1, O = 16)", 49,
           [("Moles are 1 : 1", "Each sulfur atom gives one H2SO4 molecule."), ("Mass ratio", "", r"16 \times \dfrac{98}{32} = 49 \text{ tonnes}")],
           0.5, "tonnes", "Mass from sulfur", "Calculation", "Compare the molar mass of sulfur and sulfuric acid."),
    ]))

# ===================================================================== 13. Chlorine and hydrogen chloride
SETS.append(practice_set(
    module=M_IN, topic="Chlorine and hydrogen chloride",
    title="Chlorine and hydrogen chloride", lesson="chd-chlorine-hydrogen-chloride",
    questions=[
        Q("A gas bleaches damp litmus paper. The gas is", ["ammonia", "carbon dioxide", "chlorine", "hydrogen"], 2,
          ["Ammonia turns damp red litmus blue; it does not bleach.", "Carbon dioxide turns damp blue litmus pink or red; it does not bleach.", "Hydrogen does not affect litmus."],
          [("Test", "Chlorine, with water, forms chloric(I) acid, which bleaches the litmus.")],
          "Test for chlorine", "Recall", "Which gas is a bleach?"),
        Q("Which pair of substances reacts to give chlorine in the laboratory?", ["Manganese(IV) oxide and concentrated hydrochloric acid", "Zinc and dilute hydrochloric acid", "Marble and dilute hydrochloric acid", "Sodium chloride and water"], 0,
          ["That gives hydrogen.", "That gives carbon dioxide.", "Sodium chloride simply dissolves."],
          [("Preparation", "", r"{{MnO2 + 4HCl -> MnCl2 + Cl2 + 2H2O}}")],
          "Preparing chlorine", "Recall", "An oxidizing agent is needed to oxidize chloride ions."),
        Q("In the preparation of dry chlorine, the gas is passed first through water and then through concentrated sulfuric acid. The water", ["dries the gas", "removes hydrogen chloride", "removes oxygen", "makes the gas denser"], 1,
          ["Drying is done by the concentrated sulfuric acid.", "", "Oxygen is not present in large amounts.", "Water does not change the density of chlorine."],
          [("Impurity", "Hydrogen chloride comes over with the chlorine."), ("Washing", "It is very soluble in water, so water removes it. Chlorine is much less soluble.")],
          "Purifying chlorine", "Concept", "What gas comes over with chlorine?"),
        Q("Chlorine gas is bubbled into potassium bromide solution. What is observed?", ["The solution stays colourless", "The solution turns orange-brown", "A white precipitate forms", "The solution turns blue"], 1,
          ["Chlorine displaces bromine, so there is a colour change.", "", "No precipitate forms; bromine stays dissolved.", "Blue would suggest copper ions or starch-iodine."],
          [("Displacement", "", r"{{Cl2 + 2KBr -> 2KCl + Br2}}"), ("Colour", "Bromine is orange-brown in solution.")],
          "Displacement of bromine", "Application", "Which halogen is more reactive?"),
        Q("Hot iron wire is placed in chlorine gas. The product is", ["iron(II) chloride", "iron(III) chloride", "iron oxide", "hydrogen chloride"], 1,
          ["Chlorine, an oxidizing agent, takes iron to the higher oxidation state.", "", "There is no oxygen.", "There is no hydrogen to make hydrogen chloride."],
          [("Equation", "", r"{{2Fe + 3Cl2 -> 2FeCl3}}")],
          "Reaction with iron", "Concept", "Chlorine is a strong oxidizing agent."),
        Q("Hydrogen chloride gas is collected by downward delivery and dissolved in water using an inverted funnel because it is", ["less dense than air and slightly soluble", "denser than air and very soluble", "denser than air and insoluble", "less dense than air and very soluble"], 1,
          ["It is very soluble, not slightly, and denser than air.", "", "It is very soluble; an insoluble gas would not need the funnel.", "It is denser than air, which is why downward delivery is used."],
          [("Density", "Denser than air: downward delivery."), ("Solubility", "Extremely soluble: the funnel stops water being sucked back.")],
          "Handling hydrogen chloride", "Reasoning", "What do the funnel and the collection method tell you?"),
        NQ("8.7 g of manganese(IV) oxide reacts with excess concentrated hydrochloric acid. What volume of chlorine forms at room temperature and pressure, in dm3? (Mn = 55, O = 16; 24 dm3 per mole)", 2.4,
           [("Moles", "", r"M_r(\mathrm{MnO_2}) = 87 \qquad \dfrac{8.7}{87} = 0.10 \text{ mol}"), ("Ratio", "From [[MnO2 + 4HCl -> MnCl2 + Cl2 + 2H2O]], 1 : 1, so 0.10 mol of Cl2."), ("Volume", "", r"0.10 \times 24 = 2.4 \text{ dm}^3")],
           0.05, "dm³", "Gas volume from mass", "Calculation", "Use the mole ratio 1 : 1."),
        Q("Dry hydrogen chloride gas does not turn dry blue litmus paper red, but hydrochloric acid does. This is because", ["hydrogen chloride is a base", "dry hydrogen chloride has molecules but no ions; in water it ionizes to give H+", "hydrochloric acid is a different gas", "litmus only works with liquids"], 1,
          ["Hydrogen chloride is acidic in water, not basic.", "", "Hydrochloric acid is hydrogen chloride dissolved in water.", "Litmus can show the acidity of a gas, but only when water and ions are present; the lack of water here is the point."],
          [("Dry gas", "Only HCl molecules: no H+ ions."), ("In water", "", r"{{HCl -> H^+ + Cl^-}}")],
          "Acid properties need ions", "Reasoning", "What ion makes a solution acidic?"),
    ]))

# ===================================================================== 14. Reactivity series
SETS.append(practice_set(
    module=M_IN, topic="Reactivity series and extraction of metals",
    title="The reactivity series and displacement", lesson="chd-reactivity-series",
    questions=[
        Q("Which list shows the metals in order of reactivity, most reactive first?", ["Copper, iron, magnesium, sodium", "Sodium, magnesium, iron, copper", "Magnesium, sodium, copper, iron", "Iron, copper, sodium, magnesium"], 1,
          ["This is the reverse order.", "", "Sodium is more reactive than magnesium, and iron is more reactive than copper.", "This order is scrambled."],
          [("Series", "K, Na, Ca, Mg, Al, Zn, Fe, Pb, (H), Cu, Ag, Au.")],
          "Reactivity order", "Recall", "Recall the series."),
        Q("Which metal reacts with cold water to give hydrogen?", ["Copper", "Iron", "Zinc", "Sodium"], 3,
          ["Copper does not react with water or steam.", "Iron reacts only with steam, and slowly.", "Zinc reacts only with steam."],
          [("Reaction", "", r"{{2Na + 2H2O -> 2NaOH + H2}}")],
          "Reaction with water", "Recall", "Which is the most reactive?"),
        Q("An iron nail is placed in copper(II) sulfate solution. What is observed?", ["No change", "The nail is coated with pink-brown copper and the solution turns pale green", "The nail dissolves and the solution turns deeper blue", "A white precipitate forms"], 1,
          ["Iron is above copper, so there is a reaction.", "", "The blue colour fades, not deepens.", "No white precipitate forms."],
          [("Reaction", "", r"{{Fe + CuSO4 -> FeSO4 + Cu}}"), ("Observation", "Copper deposits; iron(II) sulfate makes the solution pale green.")],
          "Displacement observations", "Application", "Which metal is more reactive?"),
        Q("In which case will there be NO reaction?", ["Zinc added to copper(II) sulfate solution", "Magnesium added to zinc sulfate solution", "Copper added to zinc sulfate solution", "Iron added to silver nitrate solution"], 2,
          ["Zinc is above copper, so it displaces copper.", "Magnesium is above zinc, so it displaces zinc.", "", "Iron is above silver, so it displaces silver."],
          [("Rule", "A metal displaces only metals below it."), ("Copper and zinc", "Copper is below zinc, so no reaction.")],
          "Predicting displacement", "Reasoning", "Is the added metal above or below the metal in solution?"),
        Q("In the reaction [[Zn + Cu^2+ -> Zn^2+ + Cu]], which statement is correct?", ["Zinc is reduced", "Copper ions are oxidized", "Zinc loses electrons and is oxidized", "Zinc ions are formed by gaining electrons"], 2,
          ["Zinc loses electrons, which is oxidation.", "Copper ions gain electrons: reduction.", "", "Zinc ions form by losing electrons from zinc atoms."],
          [("Zinc", "Zn becomes Zn2+: loss of electrons, oxidation."), ("Copper ions", "Cu2+ becomes Cu: gain of electrons, reduction.")],
          "Redox in displacement", "Concept", "OIL RIG."),
        Q("Blocks of magnesium are attached to the steel hull of a ship to prevent rusting. The reason is that magnesium", ["is less reactive than iron", "is more reactive than iron and corrodes instead", "makes the hull heavier", "stops water touching the steel"], 1,
          ["If magnesium were less reactive it would not protect.", "", "Weight is not the reason.", "The blocks are small, so they do not cover the hull."],
          [("Sacrificial protection", "The more reactive metal loses electrons and corrodes first, protecting the iron.")],
          "Sacrificial protection", "Application", "Which metal corrodes in preference to iron?"),
        NQ("5.6 g of iron is added to excess copper(II) sulfate solution. What mass of copper forms, in g? (Fe = 56, Cu = 63.5)", 6.35,
           [("Equation", "", r"{{Fe + CuSO4 -> FeSO4 + Cu}}"), ("Moles of Fe", "", r"\dfrac{5.6}{56} = 0.10 \text{ mol}"), ("Mass of Cu", "1 : 1.", r"0.10 \times 63.5 = 6.35 \text{ g}")],
           0.05, "g", "Mass from displacement", "Calculation", "The mole ratio is 1 : 1."),
        Q("In the thermite reaction, [[2Al + Fe2O3 -> Al2O3 + 2Fe]], what does the reaction show?", ["Iron is more reactive than aluminium", "Aluminium is more reactive than iron", "Aluminium oxide is easily reduced", "Iron cannot be extracted"], 1,
          ["Iron is the product, so it is displaced from its oxide by aluminium.", "", "Aluminium oxide is formed, not reduced.", "The reaction produces iron."],
          [("Displacement", "Aluminium takes oxygen from iron(III) oxide, so aluminium is more reactive.")],
          "Thermite reaction", "Reasoning", "Which metal ends up with the oxygen?"),
    ]))

# ===================================================================== 15. Extraction of metals
SETS.append(practice_set(
    module=M_IN, topic="Reactivity series and extraction of metals",
    title="Extracting sodium, aluminium, iron and copper", lesson="chd-extraction-of-metals",
    questions=[
        Q("Sodium is extracted by", ["heating its ore with carbon", "electrolysis of molten sodium chloride", "heating its ore in air", "displacement with zinc"], 1,
          ["Sodium is above carbon in the series, so carbon cannot reduce its compounds.", "", "Heating in air would not give the metal.", "Zinc is less reactive than sodium."],
          [("Rule", "Very reactive metals are extracted by electrolysis of the molten compound.")],
          "Extraction of sodium", "Recall", "Sodium is high in the series."),
        Q("Why is aluminium oxide dissolved in molten cryolite for electrolysis?", ["To react with the oxygen", "To lower the operating temperature and improve conduction", "To form the anode", "To make the aluminium less pure"], 1,
          ["Cryolite does not react with the oxygen.", "", "The anodes are made of graphite.", "The purpose is to make the process work, not to change the purity."],
          [("Melting point", "Aluminium oxide melts at over 2000 degrees Celsius."), ("Cryolite", "It lets the cell run at about 950 degrees Celsius and makes a conducting liquid.")],
          "Cryolite", "Concept", "What is the problem with the melting point of aluminium oxide?"),
        Q("In the blast furnace, the main reducing agent is", ["coke", "limestone", "carbon monoxide", "hot air"], 2,
          ["Coke burns to give carbon monoxide, which does the reducing.", "Limestone makes slag.", "", "Hot air supplies oxygen to burn the coke."],
          [("Chain", "Coke burns to carbon dioxide, which reacts with more coke to give carbon monoxide."), ("Reduction", "", r"{{Fe2O3 + 3CO -> 2Fe + 3CO2}}")],
          "Blast furnace reducing agent", "Recall", "Which gas reduces the iron oxide?"),
        Q("What is the purpose of limestone in the blast furnace?", ["To react with iron ore", "To remove sand as slag", "To burn as fuel", "To cool the furnace"], 1,
          ["Limestone does not react with the ore.", "", "Limestone does not burn.", "Limestone is not a coolant."],
          [("Reactions", "", r"{{CaCO3 -> CaO + CO2}}"), ("Slag", "", r"{{CaO + SiO2 -> CaSiO3}}")],
          "Role of limestone", "Concept", "What impurity is in the ore?"),
        Q("Which equation shows the formation of slag in the blast furnace?", [r"[[Fe2O3 + 3CO -> 2Fe + 3CO2]]", r"[[C + O2 -> CO2]]", r"[[CaO + SiO2 -> CaSiO3]]", r"[[CO2 + C -> 2CO]]"], 2,
          ["This is the reduction of iron oxide.", "This is the burning of coke.", "", "This is the formation of carbon monoxide."],
          [("Slag", "Calcium oxide combines with silicon dioxide to make calcium silicate.")],
          "Slag", "Recall", "Slag is a silicate."),
        Q("Steel is made from cast iron by", ["adding more carbon", "blowing oxygen through the molten iron to remove carbon", "cooling it quickly", "adding limestone"], 1,
          ["Cast iron already has too much carbon.", "", "Cooling does not remove carbon.", "Limestone is used in the blast furnace."],
          [("Steel", "Oxygen burns off carbon as carbon dioxide, leaving a small percentage.")],
          "Making steel", "Concept", "Does cast iron have too much or too little carbon?"),
        NQ("What mass of iron can be made from 320 tonnes of iron(III) oxide, in tonnes? (Fe = 56, O = 16)", 224,
           [("Molar mass", "", r"M_r(\mathrm{Fe_2O_3}) = 160"), ("Ratio", "1 mol of oxide gives 2 mol of iron: 160 g gives 112 g."), ("Scale", "", r"320 \times \dfrac{112}{160} = 224 \text{ tonnes}")],
           1, "tonnes", "Mass of iron", "Calculation", "Compare the mass of iron with the mass of oxide."),
        NQ("What mass of aluminium, in tonnes, can be obtained from 5.1 tonnes of aluminium oxide? (Al = 27, O = 16)", 2.7,
           [("Molar mass", "", r"M_r(\mathrm{Al_2O_3}) = 102"), ("Ratio", "1 mol of oxide gives 2 mol of aluminium: 102 g gives 54 g."), ("Scale", "", r"5.1 \times \dfrac{54}{102} = 2.7 \text{ tonnes}")],
           0.05, "tonnes", "Mass of aluminium", "Calculation", "Compare the mass of aluminium with the mass of oxide."),
    ]))



# ===================================================================== formula helper
_SUB = re.compile(r"(?<=[A-Za-z\)])(\d+)")
_CHG = re.compile(r"\^(\d*[+-])")


def _tex(s):
    s = s.replace("<=>", r"\rightleftharpoons ").replace("->", r"\rightarrow ")
    s = _CHG.sub(r"^{\1}", s)
    s = _SUB.sub(r"_{\1}", s)
    return s.replace("~", r"\cdot ")


def _mark(s):
    s = re.sub(r"\[\[(.+?)\]\]", lambda m: "$\\mathrm{" + _tex(m.group(1)) + "}$", s)
    return re.sub(r"\{\{(.+?)\}\}", lambda m: "\\mathrm{" + _tex(m.group(1)) + "}", s)


def _fix(o):
    if isinstance(o, str):
        return _mark(o)
    if isinstance(o, list):
        return [_fix(x) for x in o]
    if isinstance(o, dict):
        return {k: _fix(v) for k, v in o.items()}
    return o


SETS = _fix(SETS)
