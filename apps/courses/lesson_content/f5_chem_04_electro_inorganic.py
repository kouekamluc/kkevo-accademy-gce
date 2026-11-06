"""Form 5 Chemistry: Electrochemistry, and Inorganic Chemistry (Non-Metals & Metals).

Chemical formulae are written between double square brackets in text, and between double curly brackets in maths.
A small helper at the bottom turns them into LaTeX (subscripts, charges, arrows).
"""

import re

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "form-5")

M_EL = "Electrochemistry"
M_IN = "Inorganic Chemistry (Non-Metals & Metals)"

LESSONS = []

# ===================================================================== ELECTROCHEMISTRY
# ------------------------------------------------------------------ 1. Electrolytes and ionic theory
LESSONS.append(lesson(
    module=M_EL, topic="Electrolytes and ionic theory",
    title="Electrolytes, non-electrolytes and ions",
    slug="chd-electrolytes-ionic-theory", minutes=18,
    summary="An electrolyte conducts electricity when molten or dissolved because it contains free ions; a non-electrolyte has no free ions. Metals conduct with electrons and are not electrolytes.",
    objectives=["Define electrolyte and non-electrolyte and classify common substances",
                "Use the ionic theory to explain why ionic solids do not conduct but molten or dissolved ones do",
                "Write equations showing how an electrolyte forms ions",
                "Tell strong electrolytes from weak ones"],
    key_concepts=["Electrolyte", "Non-electrolyte", "Ion", "Ionic theory", "Strong and weak electrolytes"],
    blocks=[
        H("Why does salty water carry current?"),
        T("You are told never to touch an electric wire with wet hands. Yet pure water hardly carries current at all. Add a spoon of salt and the water becomes dangerous. Something in the salt must carry the charge."),
        T("This lesson explains what that something is. It is the key to the whole topic of electrolysis, so take your time with it."),
        H("Definitions"),
        D("An **electrolyte** is a compound that conducts electricity when it is **molten** or **dissolved in water**, and is **chemically changed (decomposed)** by the current.",
          title="Electrolyte"),
        D("A **non-electrolyte** is a compound that does not conduct electricity either when molten or when dissolved in water.",
          title="Non-electrolyte"),
        T("Test a liquid with the circuit below. If the bulb lights, the liquid conducts. If the bulb stays off, it does not. For a solid, you first have to melt it or dissolve it."),
        IMG("f5ch-d-conductivity-test.svg", alt="A circuit with a bulb and a battery joined to two electrodes dipping in a beaker of liquid",
            caption="Figure 1. A simple test for conduction. Two electrodes dip into the liquid; the bulb shows whether current flows."),
        H("The ionic theory"),
        D("An **ion** is an atom or group of atoms that has lost or gained electrons, so it carries an electric charge. Positive ions are **cations**. Negative ions are **anions**.",
          title="Ion"),
        KEY("The ionic theory in three points", "", cards=[
            ["1. Ions are already there", "Ionic compounds such as sodium chloride are made of ions. Electricity does not create them."],
            ["2. Solid: ions are fixed", "In a solid crystal the ions are held in a lattice and cannot move, so a solid ionic compound does not conduct."],
            ["3. Molten or dissolved: ions are free", "Melting or dissolving frees the ions. They move and carry the charge, so the liquid conducts."]]),
        T("So the electricity in an electrolyte is carried by **moving ions**. In a metal wire it is carried by **moving electrons**. This is the big difference between the two kinds of conductor."),
        CODE("""Substance          Solid   Molten   Dissolved in water
Sodium chloride    No      Yes      Yes
Lead(II) bromide   No      Yes      (insoluble)
Copper (metal)     Yes     Yes      (insoluble)
Sugar              No      (burns)  No
Ethanol            -       No       No""", "text", title="Which substances conduct?"),
        T("Copper conducts as a solid because of its free electrons. It is **not** an electrolyte, because it is an element, not a compound, and no chemical change happens inside it. Graphite also conducts as a solid for the same reason, but it is not an electrolyte either."),
        H("How an electrolyte makes ions"),
        T("When an ionic compound dissolves or melts, the lattice breaks up. We show this with an equation:"),
        F(r"{{NaCl -> Na^+ + Cl^-}}", title="Sodium chloride"),
        F(r"{{CuSO4 -> Cu^2+ + SO4^2-}}", title="Copper(II) sulfate"),
        T("Some covalent compounds are not made of ions, but they react with water and **form** ions. Acids are the best examples. Hydrogen chloride gas is a non-electrolyte by itself, but in water it gives an electrolyte:"),
        F(r"{{HCl -> H^+ + Cl^-}}", title="Hydrochloric acid"),
        F(r"{{H2SO4 -> 2H^+ + SO4^2-}}", title="Sulfuric acid"),
        D("A **strong electrolyte** is fully ionized in solution, so it has many ions and conducts well (hydrochloric acid, sulfuric acid, sodium hydroxide, sodium chloride). A **weak electrolyte** is only partly ionized, so it has few ions and conducts poorly (ethanoic acid, ammonia solution, and pure water). A reversible arrow shows partial ionization:",
          title="Strong and weak electrolytes", formula=r"{{CH3COOH <=> H^+ + CH3COO^-}}"),
        EX("Worked example 1: classify", intro="A student tests five liquids with the circuit in Figure 1. Classify each as strong electrolyte, weak electrolyte or non-electrolyte: dilute hydrochloric acid (bulb very bright), sugar solution (bulb off), dilute ethanoic acid of the same concentration (bulb dim), molten lead(II) bromide (bulb bright), ethanol (bulb off).", steps=[
            S("Bright bulb means many ions", text="Hydrochloric acid and molten lead(II) bromide are strong electrolytes."),
            S("Dim bulb means few ions", text="Ethanoic acid is a weak electrolyte."),
            S("Bulb off means no ions", text="Sugar solution and ethanol are non-electrolytes. Their molecules stay whole and carry no charge."),
        ]),
        EX("Worked example 2: counting ions", intro="How many moles of ions are present when 0.20 mol of aluminium sulfate dissolves completely?", steps=[
            S("Write the ionization", math=r"{{Al2(SO4)3 -> 2Al^3+ + 3SO4^2-}}"),
            S("Count ions per formula unit", text="2 aluminium ions + 3 sulfate ions = 5 ions."),
            S("Multiply by the moles", math=r"0.20 \times 5 = 1.0 \text{ mol of ions}"),
        ], check=r"2(+3) + 3(-2) = 0 \text{ (charge balances)}"),
        MISTAKE("Thinking electricity makes the ions", "Ions are already present in ionic solids. Heat or water only sets them free, and the battery only makes them move in one direction."),
        MISTAKE("Calling a metal an electrolyte", "Metals conduct by electrons and are not decomposed. An electrolyte must be a compound that is decomposed by the current."),
        MISTAKE("Saying solid sodium chloride has no ions", "It is full of ions. The correct reason it does not conduct is that its ions cannot move."),
        QUIZ("Why does solid sodium chloride not conduct electricity, but molten sodium chloride does?",
             ["Solid sodium chloride has no ions", "Its ions are held in fixed positions in the solid but are free to move when molten", "Its electrons are free only when molten", "Melting turns it into a metal"], 1,
             "In the solid the ions are fixed in the lattice. When molten they are free to move and carry charge.",
             hint="Are the ions absent from the solid, or just unable to move?",
             feedback=["The ions are there in the solid; they simply cannot move.", "", "Ionic compounds conduct with ions, not free electrons.", "Melting does not change a compound into a metal."]),
        QUIZ("Which of these is an electrolyte?", ["Copper wire", "Sugar solution", "Dilute sulfuric acid", "Graphite"], 2,
             "Dilute sulfuric acid is a compound that contains free ions and is decomposed by current.",
             hint="Look for a compound that gives ions in water. Metals and graphite conduct differently.",
             feedback=["Copper conducts with electrons and is an element, so it is not an electrolyte.", "Sugar dissolves as whole molecules, with no ions.", "", "Graphite conducts with electrons and is an element."]),
        TIP("Exam link: this idea appears in Paper 1 multiple-choice questions on which substances conduct, and as the first marks of a Paper 2 electrolysis question, where you must name the ions present."),
        PQ("Define an electrolyte and give one example of a solid and one of a liquid that is not an electrolyte.",
           "An electrolyte is a compound that conducts electricity when molten or dissolved in water and is decomposed by the current. A non-electrolyte solid: sugar. A non-electrolyte liquid: ethanol (or pure tetrachloromethane)."),
        PQ("Explain why copper sulfate solution conducts but solid copper sulfate does not.",
           "Solid copper sulfate has its ions held in fixed positions in the lattice. In solution the ions are free to move, so they carry the charge."),
        PQ("Write equations to show the ions formed when (a) potassium chloride dissolves; (b) nitric acid dissolves.",
           r"(a) [[KCl -> K^+ + Cl^-]]   (b) [[HNO3 -> H^+ + NO3^-]]"),
        SUM("An electrolyte is a compound that conducts when molten or dissolved and is decomposed by the current.",
            "A non-electrolyte has no free ions, so it does not conduct in either state.",
            "Ionic theory: ions are fixed in the solid and free when molten or dissolved. Ions, not electrons, carry the current in an electrolyte.",
            "Metals and graphite conduct with electrons and are not electrolytes.",
            "Strong electrolytes are fully ionized; weak ones are only partly ionized."),
    ]))

# ------------------------------------------------------------------ 2. Mechanism of electrolysis
LESSONS.append(lesson(
    module=M_EL, topic="Mechanism of electrolysis",
    title="How electrolysis works: electrodes, half-equations and preferential discharge",
    slug="chd-mechanism-of-electrolysis", minutes=24,
    summary="In electrolysis, cations go to the cathode and gain electrons (reduction); anions go to the anode and lose electrons (oxidation). Which ion is discharged depends on the electrochemical series, concentration and the electrode.",
    objectives=["Define electrolysis, anode, cathode and inert and active electrodes",
                "Describe the movement of ions and electrons in an electrolytic cell",
                "Write half-equations for the discharge of ions",
                "Predict which ion is discharged using the three factors of preferential discharge"],
    key_concepts=["Electrolysis", "Anode and cathode", "Oxidation and reduction", "Half-equation", "Preferential discharge"],
    blocks=[
        H("Using electricity to force a change"),
        T("Some chemical changes will not happen by themselves. You cannot just heat common salt and get sodium metal. But if you pass an electric current through molten salt, you can. This is **electrolysis**."),
        D("**Electrolysis** is the decomposition of an electrolyte, molten or in solution, by passing a **direct current** (d.c.) through it.", title="Electrolysis"),
        T("The cell has a d.c. supply (battery), two **electrodes** that dip into the electrolyte, and the electrolyte itself."),
        D("The **anode** is the electrode joined to the **positive** terminal of the battery. The **cathode** is the electrode joined to the **negative** terminal. **Inert** electrodes (graphite or platinum) do not take part in the reaction. **Active** electrodes (such as copper) can react or dissolve.", title="Electrodes"),
        TIP("Memory aid: Positive Anode, Negative Is Cathode (PANIC). Anions go to the Anode. Cations go to the Cathode (cat-ions to the cat-hode)."),
        IMG("f5ch-d-electrolysis-cell.svg", alt="Cell with anode and cathode in molten lead(II) bromide. Bromide ions move to the anode and lead ions to the cathode.",
            caption="Figure 1. Electrolysis of molten lead(II) bromide. Bromide ions go to the anode, lead ions go to the cathode."),
        H("What happens inside the cell"),
        KEY("Four steps", "", cards=[
            ["1. Ions are free", "The molten or dissolved electrolyte contains free cations and anions."],
            ["2. The battery pushes electrons", "It pulls electrons out of the anode and pushes them onto the cathode, through the wire."],
            ["3. Cathode: reduction", "Cations are attracted to the negative cathode and **gain** electrons."],
            ["4. Anode: oxidation", "Anions are attracted to the positive anode and **lose** electrons."]]),
        T("Notice two kinds of current. In the wires, **electrons** flow, from the anode to the battery and from the battery to the cathode. In the electrolyte, **ions** move. Electrons never travel through the electrolyte."),
        D("**Oxidation** is the loss of electrons and **reduction** is the gain of electrons (OIL RIG: Oxidation Is Loss, Reduction Is Gain). Oxidation takes place at the anode and reduction at the cathode.", title="OIL RIG"),
        T("We describe what happens at each electrode with a **half-equation**. For molten lead(II) bromide:"),
        F(r"\text{Cathode: } {{Pb^2+ + 2e^- -> Pb}}"),
        F(r"\text{Anode: } {{2Br^- -> Br2 + 2e^-}}"),
        T("The electrons gained at the cathode equal the electrons lost at the anode. Each half-equation must balance in **atoms and in charge**."),
        H("Preferential discharge"),
        T("A solution in water holds more than one kind of cation and anion. Besides the ions of the salt, water gives a very small number of [[H^+]] and [[OH^-]] ions. Usually only one ion at each electrode is discharged. Three factors decide which one."),
        D("**Preferential (selective) discharge** is the discharge of one ion in preference to others at an electrode. It depends on (1) the position of the ion in the electrochemical series, (2) the concentration of the ion, and (3) the nature of the electrode.", title="Preferential discharge"),
        CODE("""Cations (cathode): easiest to discharge at the right
  K+  Na+  Ca2+  Mg2+  Al3+  Zn2+  H+  Cu2+  Ag+

Anions (anode): easiest to discharge at the left
  I-  Br-  Cl-  OH-  SO4 2-  NO3-""", "text", title="Order of discharge in aqueous solutions"),
        T("**Cathode.** Silver and copper ions come after hydrogen in the list, so the metal is deposited. Ions of more reactive metals, such as sodium, potassium, calcium, magnesium and aluminium, stay in solution. [[H^+]] from water is discharged instead and hydrogen gas is released. (Some textbooks let zinc or iron be deposited from concentrated solutions; check your textbook.)"),
        T("**Anode.** Iodide, bromide and chloride ions are discharged before hydroxide ions if the halide solution is concentrated. If it is very dilute, hydroxide is discharged and oxygen forms. Sulfate and nitrate ions are **never** discharged from aqueous solution: [[OH^-]] goes instead."),
        T("**Concentration:** a concentrated chloride solution gives chlorine; a very dilute one gives mostly oxygen. **Electrode:** an active copper anode dissolves instead of any anion being discharged. We study these cases in the next lessons."),
        F(r"{{2H^+ + 2e^- -> H2}} \qquad {{4OH^- -> 2H2O + O2 + 4e^-}}", title="Two half-equations from water"),
        CODE("""Product   Test
Hydrogen  Lighted splint: squeaky pop
Oxygen    Glowing splint relights
Chlorine  Damp blue litmus turns red, then is bleached white
Bromine   Red-brown vapour or liquid
Copper    Pink-brown solid coats the cathode""", "text", title="Tests for the products"),
        EX("Worked example 1: molten zinc chloride", intro="Predict the products when molten zinc chloride is electrolysed with inert electrodes and write the half-equations.", steps=[
            S("List the ions", text="Only [[Zn^2+]] and [[Cl^-]] are present. There is no water, so there is no choice to make."),
            S("Cathode (reduction)", math=r"{{Zn^2+ + 2e^- -> Zn}}"),
            S("Anode (oxidation)", math=r"{{2Cl^- -> Cl2 + 2e^-}}"),
            S("Products", text="Zinc metal at the cathode and chlorine gas at the anode."),
        ]),
        EX("Worked example 2: aqueous sodium sulfate", intro="Predict the products when dilute sodium sulfate solution is electrolysed with inert electrodes.", steps=[
            S("List all the ions", text="[[Na^+]] and [[SO4^2-]] from the salt; [[H^+]] and [[OH^-]] from water."),
            S("Cathode: choose between Na+ and H+", text="Sodium is high in the series, so H+ is discharged.", math=r"{{2H^+ + 2e^- -> H2}}"),
            S("Anode: choose between sulfate and OH-", text="Sulfate is never discharged, so OH- is.", math=r"{{4OH^- -> 2H2O + O2 + 4e^-}}"),
            S("Products", text="Hydrogen at the cathode and oxygen at the anode. In effect, water is decomposed and sodium sulfate only carries the current."),
        ]),
        MISTAKE("Mixing up anode and cathode", "In electrolysis the anode is positive and the cathode is negative. Do not copy the sign rule from a simple cell (in the last lesson of this module), where it is the other way round."),
        MISTAKE("Sending electrons through the solution", "Electrons flow only in the wires. In the electrolyte the current is carried by ions."),
        MISTAKE("Unbalanced half-equations", "Write [[2Cl^- -> Cl2 + 2e^-]], not [[Cl^- -> Cl2 + e^-]]. Check atoms, then check charge."),
        QUIZ("Dilute sulfuric acid is electrolysed with inert electrodes. What is formed at the anode?", ["Hydrogen", "Sulfur dioxide", "Oxygen", "Sulfate ions are discharged"], 2,
             "Sulfate is not discharged. Hydroxide ions from water are, and they give oxygen.",
             hint="Which anion gets discharged, sulfate or hydroxide?",
             feedback=["Hydrogen is formed at the cathode, because H+ is a cation.", "Sulfate ions stay in solution.", "", "Sulfate and nitrate ions are not discharged from aqueous solution."]),
        QUIZ("Which half-equation is balanced and correct for a copper(II) ion at the cathode?", [r"[[Cu^2+ -> Cu + 2e^-]]", r"[[Cu^2+ + 2e^- -> Cu]]", r"[[Cu^2+ + e^- -> Cu]]", r"[[Cu -> Cu^2+ + 2e^-]]"], 1,
             "Cations gain electrons at the cathode. The charge 2+ needs two electrons to become neutral.",
             hint="At the cathode there is reduction, so electrons appear on the left.",
             feedback=["This shows loss of electrons, which is oxidation at the anode.", "", "Charge does not balance: 2+ plus 1- is not 0.", "This is oxidation, which happens at the anode."]),
        TIP("Exam link: this topic appears in Paper 1 (which ion is discharged, which gas forms) and in Paper 2 structured questions, where you write half-equations and name products. Always give the sign and the name of each electrode."),
        PQ("Define (a) the anode, (b) the cathode.", "(a) The anode is the electrode connected to the positive terminal of the battery, where oxidation occurs. (b) The cathode is the electrode connected to the negative terminal, where reduction occurs."),
        PQ("Molten lead(II) bromide is electrolysed with graphite electrodes. Name the products at each electrode and write the half-equations.", r"Cathode: lead, [[Pb^2+ + 2e^- -> Pb]]. Anode: bromine, [[2Br^- -> Br2 + 2e^-]]."),
        PQ("Why is hydrogen, not sodium, formed at the cathode when sodium chloride solution is electrolysed?", "Sodium is high in the electrochemical series, so its ions are hard to discharge. Hydrogen ions from water are lower in the series, so they are discharged instead."),
        SUM("Electrolysis is the decomposition of an electrolyte by d.c. The anode is positive, the cathode is negative.",
            "Cations go to the cathode and are reduced; anions go to the anode and are oxidized (OIL RIG).",
            "Electrons flow through the wires. Ions carry charge through the electrolyte.",
            "Half-equations must balance in atoms and charge.",
            "Preferential discharge depends on the series, the concentration and the electrode. Sulfate and nitrate ions are never discharged from solution."),
    ]))

# ------------------------------------------------------------------ 3. Electrolysis: molten salts, acidified water, brine
LESSONS.append(lesson(
    module=M_EL, topic="Electrolysis of common electrolytes",
    title="Electrolysis of molten salts, acidified water and brine",
    slug="chd-electrolysis-molten-water-brine", minutes=24,
    summary="Molten salts give a metal and a non-metal; acidified water gives hydrogen and oxygen in a 2 to 1 volume ratio; concentrated brine gives hydrogen, chlorine and sodium hydroxide solution.",
    objectives=["Predict and explain the products of electrolysis of molten salts",
                "Describe and explain the electrolysis of acidified water, including the 2 to 1 gas ratio",
                "Describe and explain the electrolysis of concentrated brine and name its three products",
                "Write the half-equations and overall equations for each case"],
    key_concepts=["Molten salt", "Acidified water", "Brine", "Chlor-alkali", "Overall equation"],
    blocks=[
        H("Salt, soap and clean water"),
        T("Common salt from the coast is cheap. When its solution is electrolysed we get three useful things at once: chlorine to make water safe to drink, sodium hydroxide to make soap, and hydrogen as a fuel and raw material. This lesson shows how."),
        T("We use the rules from the last lesson: cations go to the cathode, anions go to the anode, and in a solution in water we must decide which ion is discharged."),
        H("Case 1: molten salts"),
        T("A molten salt has only two kinds of ion, so there is no choice. The metal ion goes to the cathode and the non-metal ion goes to the anode. For molten sodium chloride (the way sodium is made):"),
        F(r"\text{Cathode: } {{Na^+ + e^- -> Na}} \qquad \text{Anode: } {{2Cl^- -> Cl2 + 2e^-}}"),
        F(r"{{2NaCl -> 2Na + Cl2}}", title="Overall equation"),
        T("Molten lead(II) bromide gives lead at the cathode and red-brown bromine vapour at the anode. Do this only in a fume cupboard."),
        H("Case 2: acidified water"),
        T("Pure water has too few ions to conduct well. A little dilute sulfuric acid is added to give plenty of ions. The electrolyte is called **acidified water**. The ions present are [[H^+]], [[SO4^2-]] and [[OH^-]]."),
        IMG("f5ch-d-water-voltameter.svg", alt="Two inverted test tubes over electrodes in dilute sulfuric acid; the cathode tube holds twice as much gas as the anode tube",
            caption="Figure 1. Electrolysis of acidified water. Hydrogen collects at the cathode (2 volumes) and oxygen at the anode (1 volume)."),
        F(r"\text{Cathode: } {{4H^+ + 4e^- -> 2H2}}"),
        F(r"\text{Anode: } {{4OH^- -> 2H2O + O2 + 4e^-}}"),
        F(r"{{2H2O -> 2H2 + O2}}", title="Overall equation"),
        T("Two moles of hydrogen form for every one mole of oxygen. At the same temperature and pressure, gas volumes follow mole ratios, so the volume ratio is **hydrogen : oxygen = 2 : 1**. The acid is not used up. Water is, so the acid becomes slightly more concentrated."),
        H("Case 3: concentrated sodium chloride solution (brine)"),
        T("Brine contains [[Na^+]] and [[Cl^-]] from the salt, and [[H^+]] and [[OH^-]] from water. Sodium is high in the series, so hydrogen ions are discharged at the cathode. Chloride is concentrated, so it is discharged before hydroxide at the anode."),
        F(r"\text{Cathode: } {{2H^+ + 2e^- -> H2}}"),
        F(r"\text{Anode: } {{2Cl^- -> Cl2 + 2e^-}}"),
        T("What is left behind? The [[Na^+]] ions stayed in solution. Hydrogen ions were removed, so the [[OH^-]] ions from water are left over. The solution turns into **sodium hydroxide solution**, which is strongly alkaline."),
        F(r"{{2NaCl + 2H2O -> 2NaOH + H2 + Cl2}}", title="Overall equation"),
        T("If the sodium chloride solution is very dilute, hydroxide ions compete and mostly oxygen forms at the anode instead of chlorine. Industry keeps chlorine and sodium hydroxide apart (with a diaphragm or membrane) because they react together."),
        CODE("""Electrolyte (inert electrodes)  Cathode    Anode     Left in solution
Molten lead(II) bromide        lead       bromine   -
Molten sodium chloride         sodium     chlorine  -
Acidified water                hydrogen   oxygen    acid, more concentrated
Concentrated brine             hydrogen   chlorine  sodium hydroxide solution""", "text", title="Summary of products"),
        KEY("Uses of the three products", "", cards=[
            ["Chlorine", "Sterilizing drinking water and swimming pools, bleach, making plastics such as PVC."],
            ["Sodium hydroxide", "Making soap and detergents, paper, and purifying bauxite for aluminium."],
            ["Hydrogen", "Making ammonia (Haber process), hardening vegetable oils into margarine, and as a fuel."]]),
        EX("Worked example 1: brine", intro="Explain why the solution near the cathode becomes alkaline when brine is electrolysed.", steps=[
            S("Which ion is discharged at the cathode?", text="Hydrogen ions, not sodium ions.", math=r"{{2H^+ + 2e^- -> H2}}"),
            S("Where do the hydrogen ions come from?", text="From water, which ionizes slightly: [[H2O <=> H^+ + OH^-]]."),
            S("What is left?", text="Taking away H+ leaves extra OH- ions. With the Na+ ions that stayed, we have sodium hydroxide. A solution with excess OH- is alkaline."),
        ]),
        EX("Worked example 2: gas volumes", intro="In the electrolysis of acidified water, 40 cm3 of hydrogen is collected. What volume of oxygen is collected at the same conditions, and what is the total gas volume?", steps=[
            S("Use the overall equation", math=r"{{2H2O -> 2H2 + O2}} \quad \text{so } V(\mathrm{H_2}) : V(\mathrm{O_2}) = 2 : 1"),
            S("Oxygen", math=r"V(\mathrm{O_2}) = \dfrac{40}{2} = 20 \text{ cm}^3"),
            S("Total", math=r"40 + 20 = 60 \text{ cm}^3"),
        ]),
        MISTAKE("Saying sodium is made from brine", "Sodium metal reacts with water, and its ion is not discharged from solution. Sodium is made only by electrolysing the molten salt."),
        MISTAKE("Saying the acid is used up in acidified water", "The acid only provides ions. Water is the substance decomposed, so the acid is not used up."),
        MISTAKE("Forgetting what stays in solution", "In brine the solution left behind is sodium hydroxide, not sodium chloride. State it."),
        QUIZ("Concentrated sodium chloride solution is electrolysed using inert electrodes. Which row is correct?",
             ["Cathode: sodium; anode: chlorine", "Cathode: hydrogen; anode: oxygen", "Cathode: hydrogen; anode: chlorine", "Cathode: chlorine; anode: hydrogen"], 2,
             "Hydrogen ions are discharged at the cathode, and chloride ions (concentrated) at the anode.",
             hint="Which is easier to discharge at the cathode, sodium or hydrogen ions?",
             feedback=["Sodium ions are not discharged from aqueous solution.", "Oxygen would form only if the solution were very dilute.", "", "This has the electrodes the wrong way round: chlorine forms from chloride ions at the anode, and hydrogen forms at the cathode."]),
        QUIZ("In the electrolysis of acidified water, 12 cm3 of oxygen is collected. What volume of hydrogen forms?", ["6 cm3", "12 cm3", "24 cm3", "36 cm3"], 2,
             "The ratio hydrogen : oxygen is 2 : 1, so hydrogen is 2 x 12 = 24 cm3.",
             hint="Which gas has twice the volume of the other?",
             feedback=["This halves the oxygen volume instead of doubling it.", "The two gases are not formed in equal volumes.", "", "This is three times the oxygen volume; the ratio is 2 : 1."]),
        TIP("Exam link: electrolysis of brine and of acidified water is a favourite in Paper 2 structured questions, where marks go for correct products, half-equations and what is left in the solution. Paper 1 asks for the products or the gas ratio."),
        PQ("Dilute sulfuric acid is electrolysed using platinum electrodes. Name the gas at each electrode and give a test for each.", "Cathode: hydrogen, which burns with a squeaky pop. Anode: oxygen, which relights a glowing splint."),
        PQ("Name the three products of electrolysing concentrated brine and give one use of each.", "Hydrogen (making ammonia or margarine), chlorine (sterilizing water or bleach), sodium hydroxide solution (making soap)."),
        PQ("Write the equation for the reaction at the cathode and at the anode when molten sodium chloride is electrolysed.", r"Cathode: [[Na^+ + e^- -> Na]]. Anode: [[2Cl^- -> Cl2 + 2e^-]]."),
        SUM("Molten salts give the metal at the cathode and the non-metal at the anode.",
            "Acidified water gives hydrogen and oxygen in a 2 : 1 volume ratio: [[2H2O -> 2H2 + O2]].",
            "Concentrated brine gives hydrogen at the cathode, chlorine at the anode, and sodium hydroxide solution is left.",
            "Very dilute chloride solutions give oxygen, not chlorine, at the anode.",
            "Always say which ion is discharged and why."),
    ]))

# ------------------------------------------------------------------ 4. Copper(II) sulfate, inert and active electrodes
LESSONS.append(lesson(
    module=M_EL, topic="Electrolysis of common electrolytes",
    title="Electrolysis of copper(II) sulfate: inert and active electrodes, refining copper",
    slug="chd-electrolysis-copper-sulfate", minutes=22,
    summary="With inert electrodes copper(II) sulfate gives copper and oxygen and becomes acidic; with copper electrodes the anode dissolves and the cathode grows, which is how copper is refined.",
    objectives=["Describe and explain electrolysis of copper(II) sulfate with inert (graphite) electrodes",
                "Describe and explain what changes when copper electrodes are used",
                "Explain how impure copper is refined by electrolysis",
                "Compare the two cases with half-equations and observations"],
    key_concepts=["Inert electrode", "Active electrode", "Copper refining", "Anode sludge", "Colour of the electrolyte"],
    blocks=[
        H("The same solution, two different results"),
        T("A copper wire in a house in Douala must be very pure copper, or it will heat up and waste electricity. Pure copper is made by electrolysis. Yet the same blue copper(II) sulfate solution behaves differently depending on the **electrodes**. This lesson explains the difference."),
        H("Inert electrodes (graphite or platinum)"),
        T("The ions present are [[Cu^2+]] and [[SO4^2-]] from the salt, and [[H^+]] and [[OH^-]] from water."),
        T("At the cathode, copper ions come after hydrogen ions in the order of discharge, so copper is deposited, not hydrogen. At the anode, sulfate is never discharged, so hydroxide ions are, and oxygen forms."),
        F(r"\text{Cathode: } {{Cu^2+ + 2e^- -> Cu}}"),
        F(r"\text{Anode: } {{4OH^- -> 2H2O + O2 + 4e^-}}"),
        F(r"{{2CuSO4 + 2H2O -> 2Cu + O2 + 2H2SO4}}", title="Overall equation"),
        KEY("Observations with inert electrodes", "", cards=[
            ["Cathode", "A pink-brown solid (copper) coats the electrode."],
            ["Anode", "Bubbles of oxygen, which relights a glowing splint."],
            ["Solution", "The blue colour fades because copper ions are used up. The solution becomes acidic because hydrogen ions and sulfate ions are left, which is dilute sulfuric acid."]]),
        H("Copper electrodes (active)"),
        T("Now the anode is made of copper. Copper atoms lose electrons more easily than hydroxide ions do. So the anode itself dissolves."),
        F(r"\text{Anode (+): } {{Cu -> Cu^2+ + 2e^-}}"),
        F(r"\text{Cathode (-): } {{Cu^2+ + 2e^- -> Cu}}"),
        T("Every copper ion removed from the solution at the cathode is replaced by one that enters at the anode. So the blue colour does **not** change, and the solution stays neutral. The anode **loses mass** and the cathode **gains the same mass**. Copper is simply moved from one electrode to the other."),
        IMG("f5ch-d-copper-refining.svg", alt="Impure copper anode and pure copper cathode in copper sulfate solution, with sludge under the anode",
            caption="Figure 1. Refining copper. The impure anode dissolves; pure copper is deposited on the cathode."),
        CODE("""                 Graphite electrodes        Copper electrodes
Cathode          copper deposited           copper deposited
Anode            oxygen given off           anode dissolves
Blue colour      fades                      stays the same
Solution         becomes acidic             stays neutral
Mass of anode    no change                  decreases
Mass of cathode  increases                  increases (same amount)""", "text", title="Inert electrodes against copper electrodes"),
        H("Refining copper"),
        T("Copper made by heating its ore (see the lessons on extraction of metals) is about 99% pure. That is not pure enough for cables. So it is refined:"),
        T("The **anode** is a thick block of impure copper. The **cathode** is a thin sheet of pure copper. The **electrolyte** is copper(II) sulfate solution, acidified with sulfuric acid. As the current flows, the anode dissolves and pure copper builds up on the cathode."),
        T("What happens to the impurities? Unreactive metals such as silver and gold do not dissolve. They fall to the bottom as **anode sludge**, which is worth collecting. More reactive impurities such as zinc and iron dissolve, but they stay in solution because copper ions are discharged first."),
        EX("Worked example 1: predicting observations", intro="Copper(II) sulfate solution is electrolysed using graphite electrodes. State what you see at each electrode and what happens to the solution. Then say what changes if the graphite anode is replaced by copper.", steps=[
            S("Cathode", text="Pink-brown copper is deposited."),
            S("Anode (graphite)", text="Colourless bubbles of oxygen form. The blue colour fades and the solution becomes acidic."),
            S("Replace the anode by copper", text="The anode now dissolves, there are no bubbles, and the solution stays blue. The anode loses mass and the cathode gains mass."),
        ]),
        EX("Worked example 2: mass change", intro="Two pure copper electrodes are used in copper(II) sulfate solution. The cathode gains 1.20 g. What is the change in the mass of the anode, and the change in the mass of the electrolyte?", steps=[
            S("Copper moved to the cathode", text="1.20 g of copper left the solution as ions."),
            S("Copper entered at the anode", text="The same amount of copper dissolved from the anode, as [[Cu^2+]] ions, to replace it."),
            S("Answer", text="Anode decreases by 1.20 g. The mass of electrolyte does not change, because the copper ions removed are replaced."),
        ]),
        MISTAKE("Saying the solution fades with copper electrodes", "The Cu2+ ions removed at the cathode are replaced at the anode, so the concentration and colour stay the same."),
        MISTAKE("Forgetting the acid that forms", "With inert electrodes the solution becomes acidic because H+ and sulfate ions are left. Name the acid: sulfuric acid."),
        MISTAKE("Writing the anode product as sulfate or sulfur dioxide", "Sulfate ions stay in solution. At an inert anode, oxygen forms."),
        QUIZ("Copper(II) sulfate solution is electrolysed using copper electrodes. Which statement is correct?",
             ["Oxygen is formed at the anode", "The blue colour of the solution fades", "The anode decreases in mass and the cathode increases in mass", "Hydrogen is formed at the cathode"], 2,
             "The copper anode dissolves and copper is deposited on the cathode, so the anode loses mass and the cathode gains it.",
             hint="Which is easier to oxidise at the anode: copper atoms or hydroxide ions?",
             feedback=["Copper dissolves in preference to hydroxide ions being discharged.", "Copper ions are replaced as fast as they are removed, so the colour stays.", "", "Copper ions are discharged at the cathode, not hydrogen ions."]),
        QUIZ("Which of these ends up in the anode sludge during the refining of copper?", ["Zinc", "Iron", "Silver", "Copper sulfate"], 2,
             "Silver is less reactive than copper, so it does not dissolve and falls as sludge.",
             hint="Which metal is less reactive than copper?",
             feedback=["Zinc is more reactive, so it dissolves and stays in the solution.", "Iron is more reactive, so it dissolves and stays in the solution.", "", "Copper sulfate is the electrolyte, dissolved in water."]),
        TIP("Exam link: electrolysis of copper(II) sulfate with the two kinds of electrodes is one of the most common electrolysis questions in Paper 2, and the observations (colour, mass, gas) are often examined in Paper 1."),
        PQ("Describe two changes you would observe at the electrodes and one change in the solution when copper(II) sulfate solution is electrolysed with platinum electrodes.", "Cathode: pink-brown copper deposited. Anode: bubbles of oxygen. Solution: the blue colour fades and it becomes acidic."),
        PQ("Why does the blue colour remain when copper electrodes are used?", "At the anode copper atoms dissolve as copper ions at the same rate as copper ions are discharged at the cathode, so the concentration of copper ions stays constant."),
        PQ("Describe how impure copper is refined. Name the anode, the cathode and the electrolyte, and say what happens to the impurities.", "The anode is impure copper, the cathode is pure copper, and the electrolyte is copper(II) sulfate solution. The anode dissolves and pure copper deposits on the cathode. Unreactive impurities such as silver and gold fall off as sludge; more reactive ones dissolve and stay in solution."),
        SUM("With inert electrodes, copper(II) sulfate gives copper at the cathode and oxygen at the anode; the blue colour fades and the solution becomes acidic.",
            "With copper electrodes, the anode dissolves and the cathode gains copper; the solution stays blue and neutral.",
            "The anode loses the same mass that the cathode gains.",
            "Copper is refined with an impure anode, a pure cathode and copper(II) sulfate solution; unreactive impurities form anode sludge."),
    ]))

# ------------------------------------------------------------------ 5. Faraday's first law
LESSONS.append(lesson(
    module=M_EL, topic="Faraday's laws of electrolysis",
    title="Faraday's first law: charge, current and mass deposited",
    slug="chd-faraday-first-law", minutes=22,
    summary="The mass liberated at an electrode is proportional to the charge passed. Use Q = It, then moles of electrons = Q / 96500, then divide by the electrons per ion to get moles of substance.",
    objectives=["State Faraday's first law and the meaning of Q = It",
                "Define the Faraday constant, F = 96 500 C per mole of electrons",
                "Calculate the mass of a substance deposited from current and time",
                "Calculate the time or current needed to deposit a given mass"],
    key_concepts=["Quantity of electricity (charge)", "Coulomb", "Faraday constant", "Electrons per ion", "m = ItM / zF"],
    blocks=[
        H("How much metal in one hour?"),
        T("A workshop in Douala silver-plates spoons. The owner wants to know how much silver is put on a spoon in 40 minutes, and what current to use. The answer comes from Michael Faraday's work on electrolysis, which links **electricity** to **amount of substance**."),
        H("Charge, current and time"),
        D("**Faraday's first law:** the mass of a substance liberated at an electrode during electrolysis is directly proportional to the quantity of electricity (charge) that passes through the electrolyte.",
          title="Faraday's first law", formula=r"m \propto Q"),
        D("The quantity of electricity (charge) is the current multiplied by the time. Charge is in **coulombs** (C), current in **amperes** (A) and time in **seconds** (s).",
          title="Charge", formula=r"Q = I \times t"),
        TIP("Always change minutes and hours to seconds first. 30 minutes is 1800 s, and 1 hour is 3600 s."),
        H("Moles of electrons: the Faraday constant"),
        D("The **Faraday constant**, $F$, is the charge carried by one mole of electrons. It is the same for every element.",
          title="Faraday constant", formula=r"F = 96\,500 \text{ C mol}^{-1}"),
        T("So if a charge $Q$ passes, the moles of electrons are:"),
        F(r"n(\mathrm{e^-}) = \dfrac{Q}{F}"),
        T("Next, use the **half-equation** to see how many electrons each ion needs. Let $z$ be the number of electrons per ion (per atom deposited)."),
        CODE("""Half-equation             electrons per atom (z)
Ag+  + e-      -> Ag            1
Cu2+ + 2e-     -> Cu            2
Al3+ + 3e-     -> Al            3
2H+  + 2e-     -> H2            2  (per H2 molecule)
2Cl- -> Cl2 + 2e-               2  (per Cl2 molecule)
4OH- -> 2H2O + O2 + 4e-         4  (per O2 molecule)""", "text", title="Electrons per atom or molecule"),
        KEY("Four-step plan for every Faraday calculation", "", cards=[
            ["1. Charge", "Q = I x t (time in seconds)"],
            ["2. Moles of electrons", "n(e) = Q / 96 500"],
            ["3. Moles of substance", "n = n(e) / z, using the half-equation"],
            ["4. Mass or volume", "mass = n x M, or volume = n x 24 dm3 at room temperature and pressure"]]),
        F(r"m = \dfrac{I \, t \, M}{z \, F}", title="All four steps together"),
        EX("Worked example 1: mass from current and time", intro="A current of 2.0 A flows for 30 minutes through copper(II) sulfate solution with copper electrodes. What mass of copper is deposited? (Cu = 63.5, F = 96 500 C/mol)", steps=[
            S("Charge", math=r"Q = It = 2.0 \times (30 \times 60) = 3600 \text{ C}"),
            S("Moles of electrons", math=r"n(\mathrm{e^-}) = \dfrac{3600}{96\,500} = 0.0373 \text{ mol}"),
            S("Moles of copper", text="The half-equation is [[Cu^2+ + 2e^- -> Cu]], so z = 2.", math=r"n(\mathrm{Cu}) = \dfrac{0.0373}{2} = 0.01865 \text{ mol}"),
            S("Mass", math=r"m = 0.01865 \times 63.5 = 1.18 \text{ g}"),
        ], check=r"m = \dfrac{2.0 \times 1800 \times 63.5}{2 \times 96\,500} = 1.18 \text{ g}"),
        EX("Worked example 2: time needed", intro="How long must a current of 0.50 A flow to deposit 1.08 g of silver from silver nitrate solution? (Ag = 108)", steps=[
            S("Moles of silver", math=r"n(\mathrm{Ag}) = \dfrac{1.08}{108} = 0.0100 \text{ mol}"),
            S("Moles of electrons", text="[[Ag^+ + e^- -> Ag]], so z = 1.", math=r"n(\mathrm{e^-}) = 0.0100 \text{ mol}"),
            S("Charge", math=r"Q = 0.0100 \times 96\,500 = 965 \text{ C}"),
            S("Time", math=r"t = \dfrac{Q}{I} = \dfrac{965}{0.50} = 1930 \text{ s} = 32 \text{ min } 10 \text{ s}"),
        ]),
        EX("Worked example 3: charge for one mole", intro="What charge is needed to deposit 0.10 mol of copper from copper(II) ions?", steps=[
            S("Electrons per copper atom", text="z = 2, so 0.10 mol of Cu needs 0.20 mol of electrons."),
            S("Charge", math=r"Q = 0.20 \times 96\,500 = 19\,300 \text{ C}"),
        ]),
        MISTAKE("Using minutes in Q = It", "The unit of time must be seconds. A current of 2 A for 30 minutes is 2 x 1800 = 3600 C, not 2 x 30."),
        MISTAKE("Forgetting the number of electrons per ion", "Copper needs 2 mol of electrons per mole, aluminium needs 3. Write the half-equation first."),
        MISTAKE("Giving a mass with no unit", "Write grams (g). Examiners penalize missing or wrong units."),
        QUIZ("A current of 5.0 A flows for 20 minutes. What charge passes?", ["100 C", "1200 C", "6000 C", "100 000 C"], 2,
             "Time = 20 x 60 = 1200 s, so Q = 5.0 x 1200 = 6000 C.",
             hint="Convert the time to seconds first.",
             feedback=["This is 5 x 20: minutes were used instead of seconds.", "This is the time in seconds only; you still need to multiply by the current.", "", "This is not the right size; recheck the multiplication."]),
        QUIZ("If the same current flows for twice as long, the mass deposited will be", ["half as much", "the same", "twice as much", "four times as much"], 2,
             "Mass is directly proportional to charge, and charge is proportional to time.",
             hint="Which quantity is mass proportional to?",
             feedback=["A longer time passes more charge, so more is deposited.", "Mass depends on charge, and the charge doubles.", "", "Mass is proportional to charge, not to its square."]),
        TIP("Exam link: Faraday calculations are part of Paper 2 structured questions on electrolysis. The Board's 2023 report names a question on electrolysis of an aqueous salt with Faraday's first law as the worst answered in its Section A, and asks for ionic equations at each electrode. Practise both."),
        PQ("Calculate the mass of copper deposited when a current of 5.0 A passes through copper(II) sulfate solution for 20 minutes. (Cu = 63.5, F = 96 500 C/mol)", "Q = 5.0 x 1200 = 6000 C. n(e) = 6000/96500 = 0.0622 mol. n(Cu) = 0.0311 mol. Mass = 0.0311 x 63.5 = 1.97 g."),
        PQ("How long will a current of 3.0 A take to deposit 3.0 g of zinc from zinc ions? (Zn = 65)", "n(Zn) = 3.0/65 = 0.04615 mol. n(e) = 0.0923 mol (z = 2). Q = 0.0923 x 96500 = 8908 C. t = 8908/3.0 = 2970 s, about 49.5 minutes."),
        PQ("State Faraday's first law and define the Faraday constant.", "The mass of a substance liberated at an electrode is directly proportional to the quantity of electricity passed. The Faraday constant is the charge carried by one mole of electrons, 96 500 C per mol."),
        SUM("Faraday's first law: mass liberated is directly proportional to the charge passed.",
            "Q = It, with time in seconds. One mole of electrons carries F = 96 500 C.",
            "Moles of electrons = Q / F. Divide by the electrons per ion (z) to find moles of substance.",
            "Mass = moles x molar mass. Write the half-equation first to find z.",
            "Check units and give answers in g, s, C or dm3."),
    ]))

# ------------------------------------------------------------------ 6. Faraday's second law
LESSONS.append(lesson(
    module=M_EL, topic="Faraday's laws of electrolysis",
    title="Faraday's second law: cells in series, gas volumes and the charge on an ion",
    slug="chd-faraday-second-law", minutes=22,
    summary="The same charge liberates amounts of different substances in the ratio of their moles of electrons: 1 F liberates 1 mol of Ag but only half a mole of Cu. Use it for cells in series and for gas volumes.",
    objectives=["State Faraday's second law",
                "Compare masses liberated by the same charge in different electrolytes",
                "Calculate gas volumes at the electrodes from the charge",
                "Find the charge on an ion from electrolysis data"],
    key_concepts=["Cells in series", "Equivalent mass", "Gas volume from charge", "Charge on an ion"],
    blocks=[
        H("One current, several cells"),
        T("When cells are connected one after another in a circuit (in series), the same current flows through all of them for the same time. So the **same quantity of electricity** passes through each electrolyte. But the masses liberated are not equal. Why? Because different ions need different numbers of electrons."),
        D("**Faraday's second law:** when the same quantity of electricity passes through different electrolytes, the masses of the substances liberated are proportional to their equivalent masses. The **equivalent mass** is the relative atomic mass divided by the charge on the ion (A divided by z).",
          title="Faraday's second law", formula=r"\text{equivalent mass} = \dfrac{A_r}{z}"),
        T("In moles it is even simpler. One mole of electrons (1 F = 96 500 C) liberates **one mole** of a metal that needs one electron per ion, **half a mole** if it needs two, and **one third** of a mole if it needs three."),
        CODE("""One mole of electrons (96 500 C) liberates

Ag   (Ag+)    1 mol    108 g
Na   (Na+)    1 mol     23 g
Cu   (Cu2+)   0.5 mol  31.75 g
Al   (Al3+)   1/3 mol    9 g
H2   at the cathode   0.5 mol   12 dm3 at room temperature and pressure
Cl2  at the anode     0.5 mol   12 dm3
O2   at the anode     0.25 mol   6 dm3""", "text", title="What one Faraday liberates"),
        TIP("This course uses a molar gas volume of 24 dm3 per mole at room temperature and pressure. Some books use 22.4 dm3 per mole at s.t.p. Use the value the question gives you."),
        H("Gas volumes from charge"),
        F(r"n(\mathrm{H_2}) = \dfrac{n(\mathrm{e^-})}{2} \qquad n(\mathrm{Cl_2}) = \dfrac{n(\mathrm{e^-})}{2} \qquad n(\mathrm{O_2}) = \dfrac{n(\mathrm{e^-})}{4}", title="Moles of each gas"),
        T("These come from the half-equations: two electrons per [[H2]] or [[Cl2]] molecule, and four per [[O2]] molecule. Multiply moles of gas by 24 dm3 to get the volume."),
        EX("Worked example 1: cells in series", intro="Copper(II) sulfate solution and silver nitrate solution are electrolysed in series, with the same current. 0.635 g of copper is deposited. What mass of silver is deposited in the other cell? (Cu = 63.5, Ag = 108)", steps=[
            S("Moles of copper", math=r"n(\mathrm{Cu}) = \dfrac{0.635}{63.5} = 0.0100 \text{ mol}"),
            S("Moles of electrons passed", text="Copper needs 2 electrons per atom.", math=r"n(\mathrm{e^-}) = 2 \times 0.0100 = 0.0200 \text{ mol}"),
            S("Moles of silver", text="Silver needs 1 electron per atom, and the same electrons passed.", math=r"n(\mathrm{Ag}) = 0.0200 \text{ mol}"),
            S("Mass of silver", math=r"0.0200 \times 108 = 2.16 \text{ g}"),
        ]),
        EX("Worked example 2: volumes of gas", intro="A current of 0.50 A flows for 1930 s through dilute sulfuric acid with inert electrodes. Find the volume of hydrogen and of oxygen collected at room temperature and pressure (24 dm3 per mole).", steps=[
            S("Charge", math=r"Q = 0.50 \times 1930 = 965 \text{ C}"),
            S("Moles of electrons", math=r"\dfrac{965}{96\,500} = 0.0100 \text{ mol}"),
            S("Hydrogen", math=r"n(\mathrm{H_2}) = 0.0050 \text{ mol}, \quad V = 0.0050 \times 24 = 0.12 \text{ dm}^3 = 120 \text{ cm}^3"),
            S("Oxygen", math=r"n(\mathrm{O_2}) = 0.0025 \text{ mol}, \quad V = 0.0025 \times 24 = 0.060 \text{ dm}^3 = 60 \text{ cm}^3"),
        ], check=r"120 : 60 = 2 : 1"),
        EX("Worked example 3: the charge on an ion", intro="A charge of 2895 C deposits 0.27 g of a metal M (relative atomic mass 27). What is the charge on its ion?", steps=[
            S("Moles of electrons", math=r"\dfrac{2895}{96\,500} = 0.030 \text{ mol}"),
            S("Moles of metal", math=r"\dfrac{0.27}{27} = 0.010 \text{ mol}"),
            S("Electrons per atom", math=r"\dfrac{0.030}{0.010} = 3"),
            S("Conclusion", text="Each atom needs 3 electrons, so the ion is [[M^3+]]."),
        ]),
        MISTAKE("Assuming equal moles of every substance", "The same charge gives equal moles only if z is the same. Copper gives half as many moles as silver."),
        MISTAKE("Using 2 electrons for oxygen", "Oxygen needs 4 electrons per [[O2]] molecule, so one mole of electrons gives only a quarter of a mole of oxygen."),
        MISTAKE("Mixing mass and moles", "Work in moles through the electrons, and convert to mass or volume only at the end."),
        QUIZ("The same charge is passed through molten sodium chloride and molten aluminium oxide. Which statement is true about the moles of metal formed?",
             ["Equal moles of sodium and aluminium", "Three times as many moles of aluminium as sodium", "Three times as many moles of sodium as aluminium", "Twice as many moles of sodium as aluminium"], 2,
             "Sodium needs 1 electron per atom, aluminium needs 3, so the same electrons give three times as many moles of sodium.",
             hint="Compare the electrons needed per atom.",
             feedback=["Equal moles would need equal electrons per atom.", "This is the reverse: aluminium needs more electrons per atom.", "", "The ratio of electrons per atom is 1 to 3, not 1 to 2."]),
        QUIZ("What volume of hydrogen forms at room temperature and pressure when 0.020 mol of electrons passes through dilute acid? (24 dm3 per mole)", ["0.24 dm3", "0.48 dm3", "0.12 dm3", "0.96 dm3"], 0,
             "n(H2) = 0.020/2 = 0.010 mol; V = 0.010 x 24 = 0.24 dm3.",
             hint="Two electrons make one molecule of hydrogen.",
             feedback=["", "This treats each electron as making one molecule of H2.", "This divides by 4, which is the number for oxygen.", "This is far too large."]),
        TIP("Exam link: these calculations, with gas volumes and cells in series, are typical Paper 2 questions on Faraday's laws. Set the working out in the four steps from the last lesson and state your units."),
        PQ("A current of 2.0 A flows for 965 s through molten sodium chloride. Calculate the volume of chlorine formed at the anode at room temperature and pressure (24 dm3 per mole).", "Q = 2.0 x 965 = 1930 C. n(e) = 0.020 mol. n(Cl2) = 0.010 mol. V = 0.010 x 24 = 0.24 dm3 (240 cm3)."),
        PQ("The same current flows through silver nitrate and copper(II) sulfate solutions in series. 5.4 g of silver is deposited. Calculate the mass of copper deposited. (Ag = 108, Cu = 63.5)", "n(Ag) = 5.4/108 = 0.050 mol, so 0.050 mol of electrons passed. n(Cu) = 0.025 mol. Mass = 0.025 x 63.5 = 1.59 g."),
        PQ("State Faraday's second law.", "When the same quantity of electricity passes through different electrolytes, the masses of substances liberated are proportional to their equivalent masses (relative atomic mass divided by the charge on the ion)."),
        SUM("Faraday's second law: the same charge liberates masses in the ratio of their equivalent masses, A / z.",
            "One mole of electrons liberates 1 mol of Ag, 0.5 mol of Cu, 1/3 mol of Al.",
            "Gases: n(H2) = n(e)/2, n(Cl2) = n(e)/2, n(O2) = n(e)/4. Multiply by 24 dm3 at room temperature and pressure.",
            "Moles of electrons divided by moles of metal gives the charge on the ion.",
            "For cells in series, find the moles of electrons from one cell and use them in the others."),
    ]))

# ------------------------------------------------------------------ 7. Electrochemical series, cells, electroplating
LESSONS.append(lesson(
    module=M_EL, topic="Electrochemical series, cells and electroplating",
    title="The electrochemical series, simple cells and electroplating",
    slug="chd-series-cells-electroplating", minutes=24,
    summary="Metals are ranked by their tendency to form positive ions. In a simple cell the more reactive metal is the negative electrode; in electroplating the object is the cathode and the plating metal is the anode.",
    objectives=["Use the electrochemical series to compare metals as electron donors",
                "Explain how a simple cell works and which electrode is negative",
                "Predict the relative voltage of cells made with different pairs of metals",
                "Describe electroplating and its purposes, and calculate a mass plated"],
    key_concepts=["Electrochemical series", "Simple cell", "Negative and positive electrode", "Electroplating", "Electrolytic cell and simple cell compared"],
    blocks=[
        H("From a torch battery to a silver spoon"),
        T("The battery in a torch makes electricity from chemicals. A silver spoon is made by using electricity to put silver on a cheaper metal. These two ideas are opposites, and both depend on one list: the **electrochemical series**."),
        H("The electrochemical series"),
        D("The **electrochemical series** ranks metals (with hydrogen) in order of their tendency to lose electrons and form positive ions in solution. For the common metals it has the same order as the reactivity series.", title="Electrochemical series"),
        CODE("""Most ready to lose electrons (strongest reducing agents)
  Potassium   K
  Sodium      Na
  Calcium     Ca
  Magnesium   Mg
  Aluminium   Al
  Zinc        Zn
  Iron        Fe
  Tin         Sn
  Lead        Pb
  Hydrogen    H
  Copper      Cu
  Silver      Ag
  Gold        Au
Least ready to lose electrons""", "text", title="The series"),
        T("A metal higher in the series loses electrons more easily. Its ions gain electrons less easily. That is why the ions of copper and silver are discharged at a cathode before hydrogen ions, and sodium ions are not."),
        H("Simple cells"),
        D("A **simple cell** (electrochemical cell) is made of two different metals dipping in an electrolyte and joined by a wire. It changes **chemical energy** into **electrical energy**.", title="Simple cell"),
        IMG("f5ch-d-simple-cell.svg", alt="Zinc and copper plates in dilute sulfuric acid connected through a voltmeter; electrons flow from zinc to copper",
            caption="Figure 1. A zinc and copper cell. Electrons flow in the wire from the zinc (negative) to the copper (positive)."),
        T("In the cell in Figure 1, zinc is higher in the series than copper, so zinc loses electrons more readily."),
        F(r"\text{Zinc (negative): } {{Zn -> Zn^2+ + 2e^-}}"),
        F(r"\text{Copper (positive): } {{2H^+ + 2e^- -> H2}}"),
        T("The electrons leave the zinc, flow through the wire (and the voltmeter) to the copper, and are picked up there by hydrogen ions. Bubbles of hydrogen form on the copper. The zinc slowly dissolves. When the zinc is used up the cell stops."),
        KEY("Rules for a simple cell", "", cards=[
            ["More reactive metal", "It is the **negative** electrode. It loses electrons (oxidation)."],
            ["Less reactive metal", "It is the **positive** electrode. Ions gain electrons here (reduction)."],
            ["Voltage", "The further apart the two metals are in the series, the greater the voltage. Two identical metals give none."]]),
        CODE("""                   Electrolytic cell        Simple (chemical) cell
Energy change      electrical -> chemical   chemical -> electrical
Needs a battery?   yes                      no, it is the battery
Anode              positive                 negative
Cathode            negative                 positive
Oxidation at       anode                    anode
Reduction at       cathode                  cathode""", "text", title="Two kinds of cell compared"),
        H("Electroplating"),
        D("**Electroplating** is the coating of one metal on the surface of another by electrolysis.", title="Electroplating"),
        IMG("f5ch-d-electroplating.svg", alt="A silver anode and an object cathode in silver nitrate solution",
            caption="Figure 2. Silver-plating an object. The object is the cathode, the silver bar is the anode."),
        KEY("How to electroplate", "", cards=[
            ["Cathode (negative)", "The object to be plated."],
            ["Anode (positive)", "A bar of the plating metal."],
            ["Electrolyte", "A solution containing ions of the plating metal, such as silver nitrate for silver."]]),
        T("At the anode, silver atoms become ions and enter the solution. At the cathode, silver ions become atoms and coat the object. The concentration of the solution stays about the same. A clean, grease-free surface and a small current give a smooth, strongly attached layer."),
        T("**Why plate?** To protect from corrosion (tin-plated food cans, chromium-plated taps), to give a good appearance (silver-plated cutlery, gold-plated jewellery) and to make a surface harder-wearing (chromium on car parts)."),
        EX("Worked example 1: voltage and polarity", intro="Three cells are made, each with a copper plate and one other metal in dilute acid: magnesium, zinc and iron. Which gives the greatest voltage, and which metal is the negative electrode in each?", steps=[
            S("Compare positions in the series", text="Magnesium is furthest above copper, then zinc, then iron."),
            S("Voltage", text="The cell with the greatest gap gives the greatest voltage: magnesium and copper."),
            S("Polarity", text="In each cell the more reactive metal (magnesium, zinc, iron) is negative and copper is positive."),
        ]),
        EX("Worked example 2: electroplating calculation", intro="A spoon is silver-plated using a current of 0.50 A for 40 minutes. What mass of silver is deposited? (Ag = 108, F = 96 500 C/mol)", steps=[
            S("Charge", math=r"Q = 0.50 \times 40 \times 60 = 1200 \text{ C}"),
            S("Moles of electrons", math=r"\dfrac{1200}{96\,500} = 0.01244 \text{ mol}"),
            S("Moles of silver", text="[[Ag^+ + e^- -> Ag]], one electron per atom: 0.01244 mol."),
            S("Mass", math=r"0.01244 \times 108 = 1.34 \text{ g}"),
        ]),
        MISTAKE("Using the wrong signs for a simple cell", "In a simple cell the more reactive metal is the negative electrode. This is the opposite of the anode sign in an electrolytic cell. Remember that oxidation is always at the anode."),
        MISTAKE("Putting the object at the anode", "In electroplating the object must be the cathode, because metal ions are reduced there."),
        MISTAKE("Using the wrong electrolyte", "The electrolyte must contain ions of the plating metal. For nickel plating use a nickel salt solution, not copper sulfate."),
        QUIZ("A cell is made with a magnesium plate and a copper plate in dilute acid. Which statement is correct?",
             ["Copper is the negative electrode", "Electrons flow from copper to magnesium through the wire", "Magnesium is the negative electrode", "No voltage is produced"], 2,
             "Magnesium is higher in the series, so it loses electrons and is the negative electrode. Electrons flow from magnesium to copper.",
             hint="Which metal is higher in the series?",
             feedback=["Copper is less reactive, so it is the positive electrode.", "Electrons flow from the negative to the positive electrode: magnesium to copper.", "", "Two different metals always give a voltage."]),
        QUIZ("A key is to be nickel-plated. Which set-up is correct?",
             ["Key as anode, nickel as cathode, copper sulfate solution", "Key as cathode, nickel as anode, nickel salt solution", "Key as cathode, copper as anode, nickel salt solution", "Key as anode, nickel as cathode, nickel salt solution"], 1,
             "The object is the cathode, the plating metal is the anode, and the electrolyte contains the plating metal's ions.",
             hint="Which electrode must the object be?",
             feedback=["The object must be the cathode and the electrolyte must contain nickel ions.", "", "The anode must be made of the plating metal, nickel.", "The object would not be plated if it were the anode."]),
        TIP("Exam link: Paper 1 asks which metal is the negative electrode in a cell and how to set up electroplating; Paper 2 asks you to draw and label the plating cell and write the electrode equations."),
        PQ("Draw (describe) the apparatus to copper-plate an iron spoon. State the anode, cathode and electrolyte.", "Anode: a bar of copper. Cathode: the iron spoon. Electrolyte: copper(II) sulfate solution. Join them to a d.c. supply (anode to positive). Copper is deposited on the spoon."),
        PQ("Explain why a zinc-copper cell stops producing current after a long time.", "The zinc loses electrons and dissolves as zinc ions. When all the zinc has reacted there is no more zinc to supply electrons, so the cell stops."),
        PQ("Give two reasons why metals are electroplated.", "To protect the metal from corrosion and to improve its appearance. (Also to make the surface harder wearing.)"),
        SUM("The electrochemical series ranks metals by their tendency to lose electrons.",
            "In a simple cell the more reactive metal is negative and electrons flow from it to the other metal.",
            "The further apart two metals are in the series, the greater the voltage.",
            "Electroplating: object as cathode, plating metal as anode, solution of the plating metal's ions.",
            "Electrolytic cells use electricity to cause change; simple cells make electricity from chemical change."),
    ]))

# ===================================================================== INORGANIC CHEMISTRY
# ------------------------------------------------------------------ 8. Hydrogen, oxygen and air
LESSONS.append(lesson(
    module=M_IN, topic="Hydrogen, oxygen, air and water",
    title="Hydrogen, oxygen and the air",
    slug="chd-hydrogen-oxygen-air", minutes=22,
    summary="Hydrogen is made from zinc and dilute acid and burns with a pop; oxygen is made from hydrogen peroxide and relights a glowing splint; air is about 78% nitrogen and 21% oxygen and is separated by fractional distillation.",
    objectives=["Describe the laboratory preparation, test, properties and uses of hydrogen",
                "Describe the laboratory preparation, test, properties and uses of oxygen",
                "State the composition of clean air and how its gases are separated industrially",
                "Calculate the percentage of oxygen in air from an experiment"],
    key_concepts=["Hydrogen", "Oxygen", "Composition of air", "Fractional distillation of liquid air", "Air pollutants"],
    blocks=[
        H("The gases around you"),
        T("When you light a charcoal stove in a market in Bafoussam, the fire needs air. When you pump a bicycle tyre you are squeezing air. Air is a mixture of gases, and two of them, oxygen and nitrogen, make up nearly all of it. Hydrogen is a gas you will not find free in air, but it is the lightest gas there is."),
        H("Hydrogen"),
        T("**Laboratory preparation:** add dilute hydrochloric acid to zinc granules."),
        F(r"{{Zn + 2HCl -> ZnCl2 + H2}}"),
        T("Hydrogen is almost insoluble in water and is lighter than air. It can be collected **over water** or by **upward delivery** (air is pushed out of an upturned jar)."),
        D("**Test for hydrogen:** hold a lighted splint at the mouth of the test tube. Hydrogen burns with a **squeaky pop**.", title="Test for hydrogen"),
        T("**Properties:** colourless, odourless, the least dense gas, insoluble in water, neutral. It burns in air or oxygen to form water. It is also a **reducing agent**: it takes oxygen from hot copper(II) oxide, which turns from black to pink-brown."),
        F(r"{{2H2 + O2 -> 2H2O}} \qquad {{CuO + H2 -> Cu + H2O}}"),
        T("**Industrial manufacture:** hydrogen is made from natural gas (methane) and steam at high temperature with a nickel catalyst, and is also a by-product of the electrolysis of brine."),
        F(r"{{CH4 + H2O -> CO + 3H2}}"),
        T("**Uses:** making ammonia (Haber process), hardening vegetable oils into margarine, and as a rocket fuel. Hydrogen mixed with air explodes, so it is never ignited until you are sure all the air is out of the apparatus."),
        H("Oxygen"),
        T("**Laboratory preparation:** add manganese(IV) oxide, a catalyst, to hydrogen peroxide solution. The oxide is not used up."),
        F(r"{{2H2O2 -> 2H2O + O2}}"),
        T("Oxygen is slightly soluble in water, so it is collected **over water**."),
        D("**Test for oxygen:** a **glowing splint** held in the gas **relights**.", title="Test for oxygen"),
        T("**Properties:** colourless, odourless, slightly denser than air, only slightly soluble in water, neutral. It **supports combustion** but does not burn itself. Many elements burn in it to form oxides."),
        F(r"{{2Mg + O2 -> 2MgO}} \qquad {{C + O2 -> CO2}} \qquad {{S + O2 -> SO2}}"),
        T("**Industrial manufacture:** by fractional distillation of liquid air (see below). **Uses:** breathing in hospitals, high-altitude flying and diving, steel making, and cutting and welding metals with ethyne."),
        H("The composition of air"),
        CODE("""Gas                  Percentage by volume (clean dry air)
Nitrogen             78
Oxygen               21
Argon                about 0.9
Carbon dioxide       about 0.04
Water vapour         varies with the weather
Other noble gases    very small amounts""", "text", title="Clean air"),
        T("**Fractional distillation of liquid air.** The air is filtered to remove dust. Carbon dioxide and water vapour are removed, because they would freeze and block the pipes. The air is then compressed and cooled until it becomes a liquid at about -200 degrees Celsius. The liquid air is warmed slowly in a tall column. Each gas boils off at its own boiling point: nitrogen first (-196 degrees Celsius), then argon (-186), then oxygen (-183)."),
        T("**Finding the percentage of oxygen.** A fixed volume of air is passed over heated copper in a syringe. The copper takes oxygen from the air and turns black: [[2Cu + O2 -> 2CuO]]. The gas volume falls and then stays constant. Nitrogen and the other gases remain."),
        EX("Worked example 1: percentage of oxygen", intro="100 cm3 of air is passed backwards and forwards over heated copper until the volume stops changing. The final volume, cooled to the starting temperature, is 79 cm3. Find the percentage of oxygen in the air.", steps=[
            S("Volume lost", math=r"100 - 79 = 21 \text{ cm}^3"),
            S("This is the oxygen used", text="Copper only takes oxygen, so the loss is the volume of oxygen."),
            S("Percentage", math=r"\dfrac{21}{100} \times 100 = 21\%"),
        ]),
        EX("Worked example 2: volume of hydrogen", intro="6.5 g of zinc reacts completely with excess dilute hydrochloric acid. What volume of hydrogen forms at room temperature and pressure? (Zn = 65; 24 dm3 per mole)", steps=[
            S("Moles of zinc", math=r"\dfrac{6.5}{65} = 0.10 \text{ mol}"),
            S("Mole ratio", text="From [[Zn + 2HCl -> ZnCl2 + H2]], 1 mol of Zn gives 1 mol of H2, so 0.10 mol of H2."),
            S("Volume", math=r"0.10 \times 24 = 2.4 \text{ dm}^3"),
        ]),
        KEY("Common air pollutants", "", cards=[
            ["Carbon monoxide", "From incomplete burning of fuel. Poisonous: it stops blood carrying oxygen."],
            ["Sulfur dioxide", "From burning fuels that contain sulfur. Causes acid rain."],
            ["Oxides of nitrogen", "Formed in hot engines. Cause acid rain and breathing problems."],
            ["Soot (particles)", "From smoky fires and diesel engines. Harm the lungs."]]),
        MISTAKE("Saying air is a compound", "Air is a mixture. Its gases are not chemically joined and can be separated by physical means."),
        MISTAKE("Saying oxygen burns", "Oxygen **supports** burning. It does not burn itself."),
        MISTAKE("Mixing up the two splint tests", "Lighted splint, squeaky pop: hydrogen. Glowing splint relights: oxygen."),
        QUIZ("A gas relights a glowing splint. The gas is", ["hydrogen", "oxygen", "carbon dioxide", "nitrogen"], 1,
             "A glowing splint relights only in oxygen, which supports combustion.",
             hint="Which gas makes things burn better?",
             feedback=["Hydrogen gives a squeaky pop with a lighted splint.", "", "Carbon dioxide puts a splint out.", "Nitrogen does not support burning; it puts a splint out."]),
        QUIZ("Which gas is boiled off first when liquid air is warmed slowly?", ["Oxygen", "Argon", "Nitrogen", "Carbon dioxide"], 2,
             "Nitrogen has the lowest boiling point (-196 degrees Celsius) of the main gases, so it boils off first.",
             hint="Compare the boiling points: -196, -186, -183.",
             feedback=["Oxygen boils at the highest of the three, so it comes off last.", "Argon boils between nitrogen and oxygen.", "", "Carbon dioxide is removed from the air before it is liquefied."]),
        TIP("Exam link: preparation, tests and uses of hydrogen and oxygen, and the composition of air, appear in Paper 1 multiple-choice questions, and in Paper 2 as drawing and description of the apparatus. Give the test and the observation together."),
        PQ("Describe how hydrogen is prepared in the laboratory and how you would test the gas.", "Add dilute hydrochloric acid to zinc granules in a flask. Collect the gas over water or by upward delivery. Test: a lighted splint gives a squeaky pop. Equation: [[Zn + 2HCl -> ZnCl2 + H2]]."),
        PQ("State the percentage of nitrogen and of oxygen in clean air and explain how they are separated on a large scale.", "Nitrogen 78%, oxygen 21%. Air is cooled to a liquid, then fractionally distilled: the gases boil off at different temperatures, nitrogen first and oxygen last."),
        PQ("Give two uses of oxygen and two uses of hydrogen.", "Oxygen: breathing in hospitals, steel making (or welding). Hydrogen: making ammonia, hardening oils to make margarine (or rocket fuel)."),
        SUM("Hydrogen: Zn + dilute acid; lighted splint, squeaky pop; least dense; reducing agent; used in ammonia and margarine.",
            "Oxygen: manganese(IV) oxide and hydrogen peroxide; relights a glowing splint; supports combustion.",
            "Air is a mixture: 78% nitrogen, 21% oxygen, about 1% argon, 0.04% carbon dioxide, and water vapour.",
            "Liquid air is separated by fractional distillation: nitrogen, argon, oxygen come off in turn.",
            "Main pollutants: carbon monoxide, sulfur dioxide, oxides of nitrogen and soot."),
    ]))

# ------------------------------------------------------------------ 9. Water, hardness and treatment
LESSONS.append(lesson(
    module=M_IN, topic="Hydrogen, oxygen, air and water",
    title="Water: tests, hardness and water treatment",
    slug="chd-water-hardness-treatment", minutes=22,
    summary="Water is tested with anhydrous copper(II) sulfate or cobalt chloride paper. Hard water contains calcium and magnesium ions; temporary hardness is removed by boiling, permanent hardness by washing soda or ion exchange.",
    objectives=["Describe chemical tests for water",
                "Distinguish soft, temporary hard and permanent hard water",
                "Explain how each kind of hardness is removed and its effects",
                "Describe the steps in treating water for a town supply"],
    key_concepts=["Test for water", "Hard and soft water", "Temporary hardness", "Permanent hardness", "Water treatment"],
    blocks=[
        H("Water that will not lather"),
        T("In many villages, water from a borehole leaves a white crust in the kettle and soap makes a grey scum instead of foam. People call the water 'hard'. Meanwhile the tap water in the city is treated to make it safe to drink. This lesson explains both."),
        H("Testing for water"),
        D("**Chemical tests for water:** anhydrous (white) copper(II) sulfate turns **blue**; blue cobalt chloride paper turns **pink**. Both tests show that water is present but not that it is pure. Pure water boils at exactly 100 degrees Celsius and freezes at 0 degrees Celsius.", title="Tests for water"),
        F(r"{{CuSO4 + 5H2O -> CuSO4~5H2O}}", title="White to blue"),
        H("Hard and soft water"),
        D("**Hard water** is water that does not easily form a lather with soap but forms a scum instead. It contains dissolved **calcium** and **magnesium** ions. **Soft water** forms a lather easily.", title="Hard water"),
        T("To test, shake the same volume of each water sample with a few drops of soap solution. Soft water lathers at once. Hard water forms a scum and needs more soap before it lathers. The scum is calcium or magnesium compounds of soap:"),
        F(r"{{Ca^2+ + 2C17H35COO^- -> (C17H35COO)2Ca}}", title="Soap scum"),
        T("Rainwater is slightly acidic because it dissolves carbon dioxide. When it runs through limestone or chalk, it dissolves calcium carbonate and forms calcium hydrogencarbonate."),
        F(r"{{CaCO3 + H2O + CO2 -> Ca(HCO3)2}}"),
        CODE("""                  Temporary hardness            Permanent hardness
Caused by         calcium (or magnesium)        calcium (or magnesium)
                  hydrogencarbonate             sulfate or chloride
Removed by        boiling                       NOT removed by boiling
Also removed by   washing soda, ion exchange    washing soda, ion exchange,
                                                distillation""", "text", title="Two kinds of hardness"),
        T("**Boiling** removes temporary hardness. The hydrogencarbonate breaks down and calcium carbonate settles. This is the white scale (fur) in kettles."),
        F(r"{{Ca(HCO3)2 -> CaCO3 + H2O + CO2}}", title="Boiling temporary hard water"),
        T("**Washing soda** (sodium carbonate) removes both kinds. The carbonate ions combine with the calcium ions and form insoluble calcium carbonate."),
        F(r"{{Na2CO3 + CaSO4 -> CaCO3 + Na2SO4}} \qquad {{Ca^2+ + CO3^2- -> CaCO3}}"),
        T("**Ion exchange** passes the water through a resin that holds sodium ions. The resin swaps its sodium ions for the calcium and magnesium ions, so soft water comes out. **Distillation** also gives pure water but costs too much for large amounts."),
        KEY("Good and bad of hard water", "", cards=[
            ["Disadvantages", "Wastes soap and leaves scum. Scale in kettles, boilers and pipes wastes fuel and can block pipes."],
            ["Advantages", "The calcium helps build teeth and bones. It gives a pleasant taste. It is not harmful to drink."]]),
        H("Treating water for a town supply"),
        IMG("f5ch-d-water-treatment.svg", alt="Flow chart: river, screen, settling tank with alum, sand filter, chlorine added, storage and supply",
            caption="Figure 1. Steps in treating water. Each step removes something different."),
        T("**1. Screening** removes large objects such as sticks and plastic. **2. Sedimentation:** aluminium sulfate (alum) is added. It makes tiny suspended particles clump together and sink. **3. Filtration** through beds of sand and gravel removes the remaining solids. **4. Chlorination:** a little chlorine is added to kill disease germs. The treated water goes into storage tanks and is piped to homes."),
        T("The water is made safe to drink. It is **not** softened by these steps, and it is not distilled."),
        EX("Worked example 1: identify the hardness", intro="Two water samples A and B each form a scum with soap. After boiling for several minutes and cooling, A lathers well, but B still forms a scum. What kind of hardness has each sample?", steps=[
            S("Sample A", text="Boiling removed its hardness, so it was temporary hard water (calcium hydrogencarbonate)."),
            S("Sample B", text="Boiling did not help, so it was permanent hard water (for example calcium sulfate)."),
            S("How to soften B", text="Add washing soda (sodium carbonate) or pass it through an ion-exchange resin."),
        ]),
        EX("Worked example 2: why treat water", intro="Explain the purpose of the alum, sand filter and chlorine in water treatment.", steps=[
            S("Alum", text="It makes small particles clump together so that they settle out."),
            S("Sand filter", text="It traps the solids that did not settle."),
            S("Chlorine", text="It kills bacteria and other germs that cause disease."),
        ]),
        MISTAKE("Thinking boiling softens all hard water", "Boiling removes only temporary hardness. Permanent hardness stays."),
        MISTAKE("Saying hard water is dangerous to drink", "Hard water is safe. It is a nuisance with soap and scale, not a health risk."),
        MISTAKE("Saying treated tap water is distilled or soft", "Treatment removes particles and germs. The hardness of the water is not changed."),
        QUIZ("Which substance removes both temporary and permanent hardness?", ["Boiling", "Sodium carbonate", "Chlorine", "Alum"], 1,
             "Carbonate ions precipitate calcium ions as calcium carbonate, whatever the source of the hardness.",
             hint="Which one gives carbonate ions?",
             feedback=["Boiling removes only temporary hardness.", "", "Chlorine kills germs; it does not remove calcium ions.", "Alum makes particles clump together; it does not remove calcium ions."]),
        QUIZ("What is the white solid that forms inside a kettle used with hard water?", ["Calcium carbonate", "Calcium chloride", "Sodium carbonate", "Calcium oxide"], 0,
             "Heating temporary hard water breaks down calcium hydrogencarbonate to calcium carbonate, which is insoluble.",
             hint="What is formed when calcium hydrogencarbonate is heated?",
             feedback=["", "Calcium chloride is soluble and stays dissolved.", "Sodium carbonate is not found in hard water.", "Calcium oxide is made at very high temperature, not in a kettle."]),
        TIP("Exam link: hardness and water treatment are tested in Paper 1 (which method removes which hardness) and in Paper 2 as an experimental or descriptive question. Always name the substance that causes the hardness."),
        PQ("Describe a chemical test for water and state what you observe.", "Add the liquid to anhydrous copper(II) sulfate: it turns from white to blue. (Or blue cobalt chloride paper turns pink.)"),
        PQ("Explain, with an equation, why boiling softens temporary hard water but not permanent hard water.", "Temporary hardness is calcium hydrogencarbonate, which decomposes on boiling: [[Ca(HCO3)2 -> CaCO3 + H2O + CO2]], leaving insoluble calcium carbonate. Permanent hardness is caused by calcium sulfate or chloride, which do not decompose on heating."),
        PQ("List the stages in the treatment of river water for a town and give the purpose of each.", "Screening (removes large objects), sedimentation with alum (makes particles settle), filtration through sand (removes fine particles), chlorination (kills germs)."),
        SUM("Water turns white copper(II) sulfate blue and blue cobalt chloride paper pink.",
            "Hard water contains calcium or magnesium ions, does not lather with soap and forms scum.",
            "Temporary hardness (hydrogencarbonates) is removed by boiling. Permanent hardness (sulfates, chlorides) is not.",
            "Washing soda and ion exchange remove both kinds.",
            "Water treatment: screening, sedimentation with alum, filtration, chlorination."),
    ]))

# ------------------------------------------------------------------ 10. Carbon and its compounds
LESSONS.append(lesson(
    module=M_IN, topic="Carbon and its compounds",
    title="Carbon: allotropes, carbon monoxide, carbon dioxide and carbonates",
    slug="chd-carbon-and-compounds", minutes=22,
    summary="Diamond and graphite are allotropes of carbon with different structures and properties. Carbon monoxide is poisonous; carbon dioxide turns limewater milky; carbonates give carbon dioxide with acids and many decompose on heating.",
    objectives=["Explain the properties and uses of diamond and graphite from their structures",
                "State the properties, preparation and dangers of carbon monoxide",
                "Prepare and test carbon dioxide and state its properties and uses",
                "Describe reactions of carbonates with acids and heat"],
    key_concepts=["Allotropes", "Diamond", "Graphite", "Carbon monoxide", "Carbon dioxide", "Carbonates"],
    blocks=[
        H("The same element, very different materials"),
        T("A pencil lead and a diamond ring are both made only of carbon. One is soft and grey, the other is the hardest natural material. The difference lies in how the atoms are joined."),
        D("**Allotropes** are different forms of the same element in the same physical state, with different arrangements of atoms and so different physical properties.", title="Allotropes"),
        H("Diamond and graphite"),
        KEY("Two allotropes of carbon", "", cards=[
            ["Diamond", "Each carbon atom is joined by strong covalent bonds to four others in a rigid, three-dimensional giant structure. Very hard. Very high melting point. No free electrons, so it does not conduct. Used for cutting and drilling tools and jewellery."],
            ["Graphite", "Each carbon atom is joined to three others in flat layers of hexagonal rings. Weak forces hold the layers together, so they slide: soft and slippery. The fourth electron of each atom is free to move, so graphite conducts. Used in pencils, lubricants and electrodes."]]),
        T("Both burn in oxygen to give carbon dioxide only. This shows that both are pure carbon. Other forms include charcoal, coke and soot, whose atoms are not in a regular pattern, and the ball-shaped molecules called fullerenes."),
        H("Carbon monoxide, CO"),
        T("Carbon monoxide forms when carbon or a carbon compound burns in **too little oxygen** (incomplete combustion)."),
        F(r"{{2C + O2 -> 2CO}}"),
        T("It is colourless and has no smell, which makes it very dangerous. It is **poisonous** because it combines with haemoglobin in the blood and stops the blood carrying oxygen. Every year people die from burning charcoal in closed rooms. Always ventilate a room where charcoal, a gas cooker or a generator is used."),
        T("Carbon monoxide is a neutral oxide. It burns with a blue flame and is a good **reducing agent**, used in the blast furnace to reduce iron ore."),
        F(r"{{2CO + O2 -> 2CO2}}"),
        H("Carbon dioxide, CO2"),
        T("**Laboratory preparation:** add dilute hydrochloric acid to marble chips (calcium carbonate). Dilute sulfuric acid is not used because the calcium sulfate it forms coats the marble and stops the reaction."),
        F(r"{{CaCO3 + 2HCl -> CaCl2 + H2O + CO2}}"),
        T("Carbon dioxide is denser than air, so it is collected by **downward delivery** (or in a gas syringe). It is slightly soluble in water."),
        D("**Test for carbon dioxide:** bubble the gas through **limewater** (calcium hydroxide solution). It turns **milky** because insoluble calcium carbonate forms. In excess carbon dioxide the milkiness disappears, because soluble calcium hydrogencarbonate forms.", title="Test for carbon dioxide"),
        F(r"{{Ca(OH)2 + CO2 -> CaCO3 + H2O}} \qquad {{CaCO3 + H2O + CO2 -> Ca(HCO3)2}}"),
        T("**Properties:** colourless, odourless, denser than air, does not support burning. It is an **acidic oxide**: it dissolves in water to form a weak acid (carbonic acid) and reacts with alkalis."),
        F(r"{{2NaOH + CO2 -> Na2CO3 + H2O}}"),
        T("**Uses:** fire extinguishers, because it is dense and does not burn; fizzy drinks; solid carbon dioxide ('dry ice') for cooling, which turns straight to gas; and plants use it in photosynthesis. It is also a **greenhouse gas**: more of it in the air adds to global warming."),
        H("Carbonates"),
        T("**With acids:** every carbonate gives carbon dioxide, a salt and water. This is also the test for a carbonate: add dilute acid and pass the gas into limewater."),
        T("**On heating:** many carbonates decompose to a metal oxide and carbon dioxide."),
        F(r"{{CaCO3 -> CaO + CO2}} \qquad {{CuCO3 -> CuO + CO2}}"),
        T("Copper carbonate changes from green to black. Zinc carbonate is white and gives an oxide that is yellow when hot and white when cold. Sodium and potassium carbonates are not decomposed by an ordinary Bunsen flame: the more reactive the metal, the more stable its carbonate. Heating limestone gives **quicklime** (calcium oxide), used in making cement and to neutralize acid soil. Adding water gives **slaked lime**: [[CaO + H2O -> Ca(OH)2]]."),
        EX("Worked example 1: heating limestone", intro="10.0 g of calcium carbonate is heated strongly until it has all decomposed. Find the mass of calcium oxide and the volume of carbon dioxide at room temperature and pressure. (Ca = 40, C = 12, O = 16; 24 dm3 per mole)", steps=[
            S("Moles of calcium carbonate", math=r"M_r(\mathrm{CaCO_3}) = 100 \qquad \dfrac{10.0}{100} = 0.100 \text{ mol}"),
            S("Mole ratio", text="[[CaCO3 -> CaO + CO2]] is 1 : 1 : 1, so 0.100 mol of each product."),
            S("Mass of calcium oxide", math=r"0.100 \times 56 = 5.60 \text{ g}"),
            S("Volume of carbon dioxide", math=r"0.100 \times 24 = 2.4 \text{ dm}^3"),
        ], check=r"5.60 + 0.100 \times 44 = 10.0 \text{ g (mass is conserved)}"),
        EX("Worked example 2: identify the solid", intro="A green solid X fizzes with dilute acid, giving a gas that turns limewater milky. When X is heated it turns black and the same gas is given off. Name X.", steps=[
            S("Fizzing with acid and the limewater test", text="The gas is carbon dioxide, so X is a carbonate."),
            S("Green changing to black on heating", text="Copper carbonate decomposes to black copper(II) oxide."),
            S("Answer", text="X is copper(II) carbonate."),
        ]),
        MISTAKE("Mixing crystalline and non-crystalline carbon", "Diamond and graphite are the crystalline forms (allotropes with a regular lattice). Charcoal, coke and soot are non-crystalline forms with no regular pattern."),
        MISTAKE("Saying carbon dioxide supports burning", "It does not. A burning splint goes out in it. Oxygen supports burning."),
        MISTAKE("Saying graphite conducts because it has ions", "Graphite has no ions. It conducts because of free (delocalized) electrons between its layers."),
        MISTAKE("Using sulfuric acid to make carbon dioxide from marble", "The insoluble calcium sulfate coats the marble and stops the reaction. Use hydrochloric acid."),
        QUIZ("Why is graphite soft and slippery?", ["Its atoms are joined by weak ionic bonds", "Its layers are held together by weak forces and can slide over each other", "Each atom is joined to four others", "It has no free electrons"], 1,
             "Strong bonds act within each layer, but only weak forces act between layers, so the layers slide.",
             hint="Think about forces between the layers.",
             feedback=["Graphite is covalent, not ionic.", "", "Four bonds per atom is diamond; graphite atoms have three bonds.", "Graphite has free electrons, which is why it conducts."]),
        QUIZ("Carbon dioxide is bubbled into limewater for a long time. What is seen?", ["It stays clear", "It turns milky and stays milky", "It turns milky and then becomes clear again", "A brown solid forms"], 2,
             "Insoluble calcium carbonate forms first, then dissolves as soluble calcium hydrogencarbonate in excess carbon dioxide.",
             hint="What happens in excess carbon dioxide?",
             feedback=["Limewater changes as soon as the gas dissolves.", "In excess the precipitate dissolves.", "", "The product is white calcium carbonate."]),
        TIP("Exam link: Paper 1 asks about allotropes, the test for carbon dioxide and the thermal decomposition of carbonates. The Board's 2023 report says many candidates could not tell the crystalline forms of carbon (diamond, graphite) from the non-crystalline forms (charcoal, coke, soot), so learn which is which and explain each property from the structure."),
        PQ("Explain why diamond is very hard but graphite conducts electricity.", "In diamond each carbon atom is held by four strong covalent bonds in a rigid giant structure, so it is very hard. In graphite each carbon is bonded to three others, leaving one electron per atom free to move between the layers, so graphite conducts."),
        PQ("Describe how you would prepare and collect a sample of carbon dioxide, and how you would test it.", "Add dilute hydrochloric acid to marble chips. Collect the gas by downward delivery because it is denser than air. Test: it turns limewater milky."),
        PQ("Why is carbon monoxide dangerous? Name a situation where it may form in the home.", "It is colourless and odourless and combines with haemoglobin, so the blood cannot carry oxygen. It forms when charcoal, gas or petrol burns with too little oxygen, such as in a closed room with a charcoal stove."),
        SUM("Diamond and graphite are allotropes of carbon. Diamond is hard and does not conduct; graphite is soft and conducts.",
            "Carbon monoxide forms in incomplete combustion; it is poisonous and a reducing agent.",
            "Carbon dioxide: marble and dilute hydrochloric acid; downward delivery; limewater turns milky; acidic oxide.",
            "Carbonates give carbon dioxide with acid and decompose on heating to an oxide (except sodium and potassium carbonates).",
            "Carbon dioxide is a greenhouse gas."),
    ]))

# ------------------------------------------------------------------ 11. Nitrogen and its compounds
LESSONS.append(lesson(
    module=M_IN, topic="Nitrogen and its compounds",
    title="Nitrogen, ammonia, the Haber process, nitric acid and the nitrogen cycle",
    slug="chd-nitrogen-ammonia-haber", minutes=25,
    summary="Ammonia is made industrially by the Haber process, N2 + 3H2 reversible 2NH3, with an iron catalyst at about 450 degrees Celsius and 200 atm. It is used for fertilizers and nitric acid. Nitrogen cycles through air, soil and living things.",
    objectives=["State the properties and uses of nitrogen",
                "Prepare and test ammonia in the laboratory and state its properties and uses",
                "Describe the Haber process and explain the conditions used",
                "Describe the manufacture of nitric acid, and the uses of nitrogen fertilizers",
                "Describe the main steps of the nitrogen cycle"],
    key_concepts=["Nitrogen", "Ammonia", "Haber process", "Equilibrium and yield", "Nitric acid", "Fertilizers", "Nitrogen cycle"],
    blocks=[
        H("Feeding the crops"),
        T("A farmer in the Western Highlands adds fertilizer to maize or vegetables. The fertilizer gives the plants nitrogen, which they need to make proteins. Yet the air is 78% nitrogen. The problem is that nitrogen gas is very unreactive, so plants cannot use it. The Haber process changes it into ammonia, from which fertilizers are made."),
        H("Nitrogen"),
        T("Nitrogen is a colourless, odourless gas, a little less dense than air, almost insoluble in water, and **unreactive** because the two atoms are joined by a very strong triple bond. It is obtained by fractional distillation of liquid air. Uses: to make ammonia, as a liquid for freezing and storing blood and food, and to fill food packets because it prevents the food going bad."),
        H("Ammonia, NH3"),
        T("**Laboratory preparation:** heat a mixture of ammonium chloride and calcium hydroxide."),
        F(r"{{2NH4Cl + Ca(OH)2 -> CaCl2 + 2NH3 + 2H2O}}"),
        T("Ammonia is **less dense than air**, so it is collected by **upward delivery** (an upturned jar). It is very soluble in water, so it cannot be collected over water. It is dried with **quicklime** (calcium oxide). Concentrated sulfuric acid and calcium chloride cannot be used, because they react with ammonia."),
        D("**Test for ammonia:** it turns **damp red litmus paper blue**, and makes **dense white fumes** of ammonium chloride with hydrogen chloride gas.", title="Test for ammonia", formula=r"{{NH3 + HCl -> NH4Cl}}"),
        T("**Properties:** colourless gas with a sharp, choking smell. Very soluble in water. Its solution is weakly alkaline because it forms a few hydroxide ions."),
        F(r"{{NH3 + H2O <=> NH4^+ + OH^-}}"),
        T("**Uses:** making fertilizers and nitric acid, and in household cleaning liquids and refrigeration."),
        H("The Haber process"),
        D("The **Haber process** makes ammonia from nitrogen and hydrogen. The reaction is **reversible** and exothermic.", title="Haber process", formula=r"{{N2 + 3H2 <=> 2NH3}} \qquad \Delta H = -92 \text{ kJ per mole of reaction}"),
        T("Nitrogen comes from the air. Hydrogen comes from natural gas and steam. The gases, in the ratio 1 : 3, are compressed and passed over an **iron catalyst** at about **450 degrees Celsius** and about **200 atmospheres**. (Textbooks give slightly different values, such as 400 to 500 degrees Celsius and 150 to 300 atm: check your textbook.) The mixture leaving the reactor is cooled, the ammonia becomes a liquid and is drawn off, and the unreacted nitrogen and hydrogen are **recycled**."),
        IMG("f5ch-d-haber-flow.svg", alt="Flow diagram of the Haber process: nitrogen and hydrogen compressed, converter with iron catalyst, cooler where ammonia condenses, recycle of unreacted gases",
            caption="Figure 1. The Haber process. Ammonia is condensed and removed; unreacted gases return to the converter."),
        KEY("Why these conditions? (Le Chatelier)", "", cards=[
            ["High pressure", "4 moles of gas make 2 moles of gas. High pressure pushes the equilibrium to the side with fewer gas molecules, so the yield of ammonia rises. Very high pressure is costly and needs strong equipment, so about 200 atm is a compromise."],
            ["Moderate temperature", "The forward reaction is exothermic, so a low temperature gives a higher yield, but the reaction is then too slow. About 450 degrees Celsius is a compromise between yield and rate."],
            ["Iron catalyst", "It speeds up the forward and the backward reactions equally. It gets to equilibrium faster but does **not** change the equilibrium position or the yield."]]),
        H("Nitric acid and fertilizers"),
        T("**Nitric acid** is made from ammonia in three steps. Ammonia and air pass over a hot platinum catalyst, and nitrogen monoxide forms. It is then oxidized to nitrogen dioxide, which is dissolved in water in the presence of more air."),
        F(r"{{4NH3 + 5O2 -> 4NO + 6H2O}} \qquad {{2NO + O2 -> 2NO2}} \qquad {{4NO2 + O2 + 2H2O -> 4HNO3}}"),
        T("Nitric acid is a strong acid used to make **ammonium nitrate** fertilizer, explosives and dyes. Reacting ammonia with acid gives ammonium salts, which are fertilizers:"),
        F(r"{{NH3 + HNO3 -> NH4NO3}} \qquad {{2NH3 + H2SO4 -> (NH4)2SO4}}"),
        T("A good fertilizer has a high percentage of nitrogen. Compounds of nitrogen, phosphorus and potassium (NPK) feed crops. Too much fertilizer washed into rivers causes pollution."),
        H("The nitrogen cycle"),
        IMG("f5ch-d-nitrogen-cycle.svg", alt="The nitrogen cycle: nitrogen from the air becomes nitrates in soil by lightning and bacteria, plants make proteins, animals eat plants, decay gives ammonium compounds, bacteria return nitrogen to the air",
            caption="Figure 2. The nitrogen cycle."),
        T("**Fixation** turns nitrogen gas into compounds. Lightning makes nitrogen oxides ([[N2 + O2 -> 2NO]]) that reach the soil as nitrates in rain. Bacteria in the root nodules of beans, groundnuts and other legumes fix nitrogen directly. Factories fix it in the Haber process. **Plants** take up nitrates and make proteins, and **animals** get nitrogen by eating plants. When plants and animals die, and in animal waste, **decay** returns nitrogen as ammonium compounds. **Nitrifying bacteria** change ammonium compounds to nitrates. **Denitrifying bacteria** return nitrogen gas to the air."),
        EX("Worked example 1: percentage of nitrogen", intro="Which fertilizer has the higher percentage of nitrogen by mass, ammonium nitrate or ammonium sulfate? (H = 1, N = 14, O = 16, S = 32)", steps=[
            S("Ammonium nitrate", math=r"M_r(\mathrm{NH_4NO_3}) = 14 + 4 + 14 + 48 = 80 \qquad \dfrac{28}{80} \times 100 = 35\%"),
            S("Ammonium sulfate", math=r"M_r((\mathrm{NH_4})_2\mathrm{SO_4}) = 36 + 32 + 64 = 132 \qquad \dfrac{28}{132} \times 100 = 21.2\%"),
            S("Compare", text="Ammonium nitrate has the higher percentage of nitrogen (35% against 21.2%)."),
        ]),
        EX("Worked example 2: Haber process calculations", intro="(a) What volume of ammonia forms from 30 dm3 of hydrogen, with excess nitrogen, at the same temperature and pressure? (b) What mass of ammonia forms from 56 g of nitrogen with excess hydrogen? (N = 14, H = 1)", steps=[
            S("(a) Gas volumes follow mole ratios", text="From [[N2 + 3H2 <=> 2NH3]], 3 volumes of H2 give 2 volumes of NH3.", math=r"30 \times \dfrac{2}{3} = 20 \text{ dm}^3"),
            S("(b) Moles of nitrogen", math=r"\dfrac{56}{28} = 2.0 \text{ mol}"),
            S("(b) Moles and mass of ammonia", text="1 mol of N2 gives 2 mol of NH3, so 4.0 mol.", math=r"4.0 \times 17 = 68 \text{ g}"),
        ]),
        MISTAKE("Saying the catalyst increases the yield", "A catalyst speeds up the forward and backward reactions equally. The equilibrium position and the yield do not change; the equilibrium is reached sooner."),
        MISTAKE("Mixing up yield and rate", "Pressure and temperature change both the rate and the yield, but for different reasons. Explain them separately."),
        MISTAKE("Collecting ammonia over water or drying it with sulfuric acid", "Ammonia is very soluble and reacts with the acid. Dry it with quicklime and collect it by upward delivery."),
        QUIZ("Which is the best way to dry ammonia gas?", ["Concentrated sulfuric acid", "Anhydrous calcium chloride", "Quicklime (calcium oxide)", "Phosphorus(V) oxide"], 2,
             "Ammonia is alkaline, so it is dried with a basic drying agent, quicklime.",
             hint="Ammonia is a base. Which drying agents are acidic?",
             feedback=["The acid would react with ammonia to make ammonium sulfate.", "Calcium chloride reacts with ammonia and cannot be used.", "", "Phosphorus(V) oxide is acidic and would react."]),
        QUIZ("In the Haber process, what is the effect of using an iron catalyst?", ["The yield of ammonia is increased", "The reaction reaches equilibrium faster", "The reaction becomes endothermic", "The equilibrium position moves to the right"], 1,
             "A catalyst speeds up both directions equally, so equilibrium is reached sooner, with the same yield.",
             hint="Does a catalyst change the position of equilibrium?",
             feedback=["The yield stays the same at a given temperature and pressure.", "", "A catalyst does not change the energy change of the reaction.", "A catalyst does not shift the equilibrium."]),
        TIP("Exam link: the Haber process is a regular topic in Paper 2, where marks are for the equation, the catalyst, the temperature and pressure and, most of all, your explanation of why. The Board's 2023 report says candidates confused yield with equilibrium position and wrongly thought a catalyst changes the yield. Paper 1 asks about ammonia tests, preparation and fertilizers."),
        PQ("Write the equation for the Haber process and state the temperature, pressure and catalyst used.", "[[N2 + 3H2 <=> 2NH3]]. About 450 degrees Celsius, about 200 atmospheres, iron catalyst."),
        PQ("Explain why a very high temperature is not used in the Haber process, although it makes the reaction faster.", "The forward reaction is exothermic. A high temperature moves the equilibrium to the left and lowers the yield of ammonia. A moderate temperature is a compromise between a fast rate and a good yield."),
        PQ("Describe how bacteria help to return nitrogen to the soil. Name two types.", "Nitrogen-fixing bacteria (for example in legume root nodules) change nitrogen gas into nitrogen compounds. Nitrifying bacteria change ammonium compounds into nitrates that plants can take up."),
        SUM("Nitrogen is unreactive and is obtained from liquid air.",
            "Ammonia: from ammonium chloride and calcium hydroxide; upward delivery; dried with quicklime; turns damp red litmus blue.",
            "Haber process: [[N2 + 3H2 <=> 2NH3]], iron catalyst, about 450 degrees Celsius, about 200 atm, unreacted gases recycled.",
            "A catalyst does not change the yield; high pressure raises it; a high temperature lowers it.",
            "Nitric acid is made from ammonia; ammonium salts are fertilizers.",
            "The nitrogen cycle: fixation, uptake by plants, decay, nitrification and denitrification."),
    ]))

# ------------------------------------------------------------------ 12. Sulfur and its compounds
LESSONS.append(lesson(
    module=M_IN, topic="Sulfur and its compounds",
    title="Sulfur, sulfur dioxide and sulfuric acid: the Contact process",
    slug="chd-sulfur-contact-process", minutes=24,
    summary="Sulfur has two allotropes. Sulfur dioxide is an acidic, bleaching gas and a cause of acid rain. Sulfuric acid is made by the Contact process, using vanadium(V) oxide, and the concentrated acid is a dehydrating agent.",
    objectives=["Name the allotropes of sulfur and state its uses",
                "State the preparation, test, properties and uses of sulfur dioxide",
                "Describe the Contact process and explain its conditions",
                "State the properties and uses of dilute and concentrated sulfuric acid"],
    key_concepts=["Rhombic and monoclinic sulfur", "Sulfur dioxide", "Acid rain", "Contact process", "Dehydrating agent", "Oleum"],
    blocks=[
        H("The most useful acid"),
        T("Sulfuric acid is made in larger amounts than any other chemical. It is in car batteries, it helps to make fertilizers, and it is used in making soaps and paints. It begins with a yellow solid: sulfur."),
        H("Sulfur"),
        T("Sulfur is a yellow, brittle solid that does not dissolve in water. It occurs as the free element in volcanic regions, in crude oil and natural gas, and in metal sulfide ores."),
        D("Sulfur has two crystalline **allotropes**. **Rhombic sulfur** is stable below about 96 degrees Celsius and forms diamond-shaped crystals. **Monoclinic sulfur** is stable above about 96 degrees Celsius and forms needle-shaped crystals. Both are made of rings of eight atoms, [[S8]]. They change into one another at about 96 degrees Celsius, the **transition temperature**.", title="Allotropes of sulfur"),
        T("If molten sulfur is poured into cold water it forms a rubbery solid called **plastic sulfur**, which slowly changes back to rhombic sulfur. Uses of sulfur: making sulfuric acid (most of it), vulcanizing rubber, matches, and fungicides."),
        H("Sulfur dioxide, SO2"),
        T("Sulfur dioxide forms when sulfur or sulfur compounds burn in air, and when metal sulfide ores are roasted."),
        F(r"{{S + O2 -> SO2}} \qquad {{2ZnS + 3O2 -> 2ZnO + 2SO2}}"),
        T("**Laboratory preparation:** add dilute hydrochloric acid to sodium sulfite."),
        F(r"{{Na2SO3 + 2HCl -> 2NaCl + H2O + SO2}}"),
        T("Sulfur dioxide is a colourless, poisonous gas with a choking smell. It is denser than air and very soluble in water, forming an acidic solution (sulfurous acid), so it is an **acidic oxide**. It is a **reducing agent** and a bleach."),
        D("**Test for sulfur dioxide:** it turns **acidified potassium dichromate(VI) solution from orange to green**. It also decolourizes acidified potassium manganate(VII), which is purple.", title="Test for sulfur dioxide"),
        T("**Uses:** making sulfuric acid, bleaching wood pulp and paper, and preserving dried fruits and drinks. **Harm:** it causes **acid rain**, which damages buildings, kills trees and harms life in rivers. It comes from burning fuels that contain sulfur and from smelting sulfide ores."),
        H("The Contact process"),
        IMG("f5ch-d-contact-flow.svg", alt="Flow diagram of the Contact process: burn sulfur, purify, converter with vanadium(V) oxide, absorb in sulfuric acid to make oleum, add water, sulfuric acid",
            caption="Figure 1. The Contact process."),
        KEY("Three stages", "", cards=[
            ["1. Make sulfur dioxide", "Burn sulfur in dry air (or roast a sulfide ore). The gas is purified and dried so that impurities do not poison the catalyst."],
            ["2. Convert to sulfur trioxide", "[[2SO2 + O2 <=> 2SO3]] over a vanadium(V) oxide catalyst, [[V2O5]], at about 450 degrees Celsius and 1 to 2 atmospheres. The reaction is exothermic and reversible."],
            ["3. Absorb and dilute", "Sulfur trioxide is dissolved in concentrated sulfuric acid to make **oleum**. Water is then added to oleum to make sulfuric acid."]]),
        F(r"{{SO3 + H2SO4 -> H2S2O7}} \qquad {{H2S2O7 + H2O -> 2H2SO4}}", title="Absorption stage"),
        T("Sulfur trioxide is not added to water directly, because the reaction is so violent that it forms a fine mist of acid that is hard to condense. A moderate temperature gives a good yield and a fast enough reaction. High pressure is not needed, because the yield is already high at low pressure, and it would be costly. Unreacted gases are recycled."),
        H("Sulfuric acid"),
        T("**Dilute sulfuric acid** is a typical strong acid. It reacts with metals above hydrogen, bases and carbonates. For example: [[Mg + H2SO4 -> MgSO4 + H2]]."),
        T("**Concentrated sulfuric acid** has special properties. It is a **dehydrating agent**: it removes water from substances. It turns blue copper(II) sulfate crystals white, and turns sugar to black carbon."),
        F(r"{{C12H22O11 -> 12C + 11H2O}} \quad \text{(with concentrated } {{H2SO4}} \text{)}"),
        T("Hot concentrated sulfuric acid is also an **oxidizing agent**: [[Cu + 2H2SO4 -> CuSO4 + SO2 + 2H2O]]. Diluting it gives out a lot of heat, so always add **acid to water**, slowly, never water to the acid."),
        T("**Uses:** making fertilizers (ammonium sulfate, superphosphate), car batteries, detergents, paints, and cleaning metals."),
        EX("Worked example 1: mass of acid", intro="What mass of sulfuric acid can be made from 16 tonnes of sulfur, if every atom of sulfur ends up in sulfuric acid? (S = 32, H = 1, O = 16)", steps=[
            S("Link sulfur to the acid", text="Each S atom becomes one [[H2SO4]] molecule, so 1 mol of S gives 1 mol of [[H2SO4]]."),
            S("Molar masses", math=r"S = 32 \text{ g/mol} \qquad M_r(\mathrm{H_2SO_4}) = 98"),
            S("Scale", math=r"16 \times \dfrac{98}{32} = 49 \text{ tonnes}"),
        ]),
        EX("Worked example 2: gas volumes in the converter", intro="20 dm3 of sulfur dioxide reacts completely with oxygen to form sulfur trioxide, all gases measured at the same temperature and pressure. What volume of oxygen is needed and what volume of sulfur trioxide forms?", steps=[
            S("Use the equation", math=r"{{2SO2 + O2 -> 2SO3}} \quad (2 : 1 : 2 \text{ by volume})"),
            S("Oxygen", math=r"\dfrac{20}{2} = 10 \text{ dm}^3"),
            S("Sulfur trioxide", text="Same volume as sulfur dioxide.", math=r"20 \text{ dm}^3"),
        ]),
        MISTAKE("Dissolving sulfur trioxide directly in water", "In industry, it is dissolved in concentrated sulfuric acid to give oleum. The oleum is then diluted."),
        MISTAKE("Saying the catalyst is iron or platinum", "The Contact process uses vanadium(V) oxide. Iron is the Haber process catalyst."),
        MISTAKE("Pouring water into concentrated acid", "This can make the mixture boil and spit. Add the acid to water, a little at a time."),
        QUIZ("What is the catalyst in the Contact process?", ["Iron", "Nickel", "Vanadium(V) oxide", "Manganese(IV) oxide"], 2,
             "Vanadium(V) oxide, V2O5, catalyzes the conversion of sulfur dioxide to sulfur trioxide.",
             hint="Which catalyst belongs to the Haber process, and which to the Contact process?",
             feedback=["Iron is the catalyst in the Haber process.", "Nickel is used when hydrogen is made from methane and when oils are hardened.", "", "Manganese(IV) oxide is used in making oxygen from hydrogen peroxide."]),
        QUIZ("Concentrated sulfuric acid is added to sugar. The sugar turns black. This shows that the acid is", ["an oxidizing agent only", "a dehydrating agent", "a reducing agent", "a weak acid"], 1,
             "The acid removes water from the sugar, leaving black carbon.",
             hint="What is taken away from the sugar?",
             feedback=["It can oxidize, but the black carbon shows removal of water.", "", "Sulfuric acid does not act as a reducing agent here.", "Sulfuric acid is a strong acid, and the colour change does not show weakness."]),
        TIP("Exam link: the Contact process, with its equations, catalyst and conditions, appears in Paper 2. Paper 1 asks for the catalyst, the tests for sulfur dioxide and properties of concentrated acid. Explain the conditions in terms of yield and rate, as with the Haber process."),
        PQ("Describe the three stages of the Contact process. Give the catalyst and temperature.", "Sulfur burns in air to form sulfur dioxide. Sulfur dioxide and oxygen react over vanadium(V) oxide at about 450 degrees Celsius: [[2SO2 + O2 <=> 2SO3]]. Sulfur trioxide is dissolved in concentrated sulfuric acid to make oleum, which is diluted with water to give sulfuric acid."),
        PQ("State the test for sulfur dioxide and one environmental problem that it causes.", "It turns acidified potassium dichromate(VI) from orange to green. It causes acid rain."),
        PQ("Give two uses of concentrated sulfuric acid and name the property shown in each.", "Drying gases or turning sugar black (dehydrating agent); making fertilizers such as ammonium sulfate (acid reacting with ammonia); reacting with copper when hot (oxidizing agent)."),
        SUM("Sulfur has rhombic and monoclinic allotropes (transition at about 96 degrees Celsius).",
            "Sulfur dioxide is an acidic, bleaching gas; the test is orange to green with acidified dichromate(VI); it causes acid rain.",
            "Contact process: sulfur, then sulfur dioxide, then over vanadium(V) oxide at about 450 degrees Celsius to sulfur trioxide, then oleum, then sulfuric acid.",
            "Concentrated sulfuric acid dehydrates and, when hot, oxidizes.",
            "Always add acid to water."),
    ]))

# ------------------------------------------------------------------ 13. Chlorine and hydrogen chloride
LESSONS.append(lesson(
    module=M_IN, topic="Chlorine and hydrogen chloride",
    title="Chlorine and hydrogen chloride: preparation, tests and reactions",
    slug="chd-chlorine-hydrogen-chloride", minutes=22,
    summary="Chlorine is a yellow-green poisonous gas that bleaches damp litmus, displaces bromine and iodine and forms iron(III) chloride. Hydrogen chloride is a very soluble gas made from salt and concentrated sulfuric acid.",
    objectives=["Describe the laboratory preparation and collection of chlorine",
                "State the test for chlorine and its main reactions and uses",
                "Describe the laboratory preparation of hydrogen chloride",
                "Describe the properties and tests of hydrogen chloride and hydrochloric acid"],
    key_concepts=["Chlorine", "Bleaching", "Displacement of halogens", "Hydrogen chloride", "Hydrochloric acid"],
    blocks=[
        H("The gas that makes water safe"),
        T("Tap water in towns is made safe with a little chlorine. The same gas, in strong amounts, is poisonous. You met chlorine in the electrolysis of brine. Here we see how it is made in the laboratory and what it does."),
        H("Chlorine, Cl2"),
        T("**Laboratory preparation:** warm manganese(IV) oxide with concentrated hydrochloric acid."),
        F(r"{{MnO2 + 4HCl -> MnCl2 + Cl2 + 2H2O}}"),
        IMG("f5ch-d-chlorine-prep.svg", alt="Apparatus: flask with manganese oxide and concentrated hydrochloric acid, wash bottle with water, wash bottle with concentrated sulfuric acid, gas jar",
            caption="Figure 1. Preparing dry chlorine. Water removes hydrogen chloride; concentrated sulfuric acid dries the gas."),
        T("The gas first passes through **water**, which removes hydrogen chloride fumes, then through **concentrated sulfuric acid**, which dries it. Chlorine is denser than air, so it is collected by **downward delivery**. It is poisonous, so everything is done in a fume cupboard."),
        D("**Test for chlorine:** it **bleaches damp litmus paper** (first turning it red, then white). It also turns moist starch-iodide paper blue-black.", title="Test for chlorine"),
        T("**Properties:** yellow-green gas with a choking smell. Poisonous. Denser than air. Fairly soluble in water."),
        KEY("Reactions of chlorine", "", cards=[
            ["With metals", "Forms chlorides. [[2Na + Cl2 -> 2NaCl]]. With hot iron it forms iron(III) chloride, a brown solid: [[2Fe + 3Cl2 -> 2FeCl3]]."],
            ["With hydrogen", "[[H2 + Cl2 -> 2HCl]]. It burns, giving hydrogen chloride."],
            ["With water", "Gives a mixture of hydrochloric acid and chloric(I) acid, which bleaches: [[Cl2 + H2O <=> HCl + HOCl]]. Dry chlorine does not bleach dry litmus; water is needed."],
            ["With cold dilute sodium hydroxide", "Makes bleach (sodium chlorate(I)): [[Cl2 + 2NaOH -> NaCl + NaOCl + H2O]]."]]),
        T("**Displacement.** Chlorine is a more reactive halogen than bromine and iodine. It displaces them from their salts. Potassium bromide solution turns orange-brown. Potassium iodide solution turns brown (iodine)."),
        F(r"{{Cl2 + 2KBr -> 2KCl + Br2}} \qquad {{Cl2 + 2KI -> 2KCl + I2}}"),
        T("**Uses:** killing germs in drinking water and swimming pools, making bleach and disinfectants, plastics such as PVC, and hydrochloric acid. Chlorine is made industrially by electrolysis of brine."),
        H("Hydrogen chloride, HCl"),
        T("**Laboratory preparation:** warm sodium chloride with concentrated sulfuric acid."),
        F(r"{{NaCl + H2SO4 -> NaHSO4 + HCl}}"),
        T("The gas is dried with **concentrated sulfuric acid** and collected by **downward delivery**, because it is denser than air. It is **extremely soluble** in water. To dissolve it safely, an inverted funnel just touches the water, so the water cannot be sucked back into the apparatus."),
        D("**Test for hydrogen chloride:** it forms **dense white fumes** with ammonia gas. Dissolved in water it gives a **white precipitate with silver nitrate solution** after adding dilute nitric acid.", title="Test for hydrogen chloride"),
        F(r"{{NH3 + HCl -> NH4Cl}} \qquad {{Ag^+ + Cl^- -> AgCl}}"),
        T("**Dry hydrogen chloride and hydrochloric acid.** Dry hydrogen chloride gas (or HCl in a non-aqueous solvent such as methylbenzene) has molecules, no ions, and does not act as an acid: it does not change dry litmus and does not react with dry magnesium. When it dissolves in water, it ionizes to give hydrochloric acid, a strong acid."),
        F(r"{{HCl -> H^+ + Cl^-}} \quad \text{(in water)}"),
        T("Hydrochloric acid has all the usual reactions of a strong acid with metals, bases and carbonates. **Uses:** cleaning metal surfaces before plating or painting ('pickling'), making chlorides, and as a laboratory reagent."),
        EX("Worked example 1: chlorine volume", intro="8.7 g of manganese(IV) oxide reacts with excess concentrated hydrochloric acid. What volume of chlorine forms at room temperature and pressure? (Mn = 55, O = 16; 24 dm3 per mole)", steps=[
            S("Moles of manganese(IV) oxide", math=r"M_r(\mathrm{MnO_2}) = 87 \qquad \dfrac{8.7}{87} = 0.10 \text{ mol}"),
            S("Mole ratio", text="From [[MnO2 + 4HCl -> MnCl2 + Cl2 + 2H2O]], 1 mol of MnO2 gives 1 mol of Cl2."),
            S("Volume", math=r"0.10 \times 24 = 2.4 \text{ dm}^3"),
        ]),
        EX("Worked example 2: displacement", intro="Chlorine gas is bubbled into colourless potassium iodide solution. What do you see, and what is the equation?", steps=[
            S("Observation", text="The solution turns brown as iodine forms."),
            S("Why", text="Chlorine is more reactive than iodine, so it takes the potassium and displaces iodine."),
            S("Equation", math=r"{{Cl2 + 2KI -> 2KCl + I2}}"),
        ], check=r"\text{ionic: } {{Cl2 + 2I^- -> 2Cl^- + I2}}"),
        MISTAKE("Saying dry chlorine bleaches dry litmus", "It does not. Bleaching needs water to make chloric(I) acid. Use damp litmus."),
        MISTAKE("Saying iron burns in chlorine to give iron(II) chloride", "Chlorine is a strong oxidizing agent and gives iron(III) chloride, [[FeCl3]]."),
        MISTAKE("Writing that dry HCl gas is an acid", "Dry hydrogen chloride has no hydrogen ions. It becomes an acid only in water."),
        QUIZ("Which observation shows that a gas is chlorine?", ["It relights a glowing splint", "It turns damp litmus paper white", "It turns limewater milky", "It turns damp red litmus blue"], 1,
             "Chlorine bleaches damp litmus paper.",
             hint="Which gas is a bleach?",
             feedback=["This is oxygen.", "", "This is carbon dioxide.", "This is ammonia, which is alkaline."]),
        QUIZ("Why is concentrated sulfuric acid used in the preparation of dry chlorine?", ["To make the gas denser", "To remove water vapour", "To react with hydrogen chloride", "To increase the yield of chlorine"], 1,
             "Concentrated sulfuric acid is a drying agent. It takes water vapour from the gas.",
             hint="What property of concentrated sulfuric acid do we use?",
             feedback=["Drying does not change the density of chlorine.", "", "Water in the first wash bottle removes the hydrogen chloride.", "Drying does not change how much chlorine is made."]),
        TIP("Exam link: Paper 1 asks for tests and properties of chlorine and hydrogen chloride; Paper 2 asks you to draw or label the apparatus for preparing a dry gas and explain each bottle. Practise naming what each wash bottle does."),
        PQ("Describe how you would prepare a dry sample of chlorine. Name the reagents and the drying agent.", "Warm manganese(IV) oxide with concentrated hydrochloric acid. Pass the gas through water to remove hydrogen chloride, then through concentrated sulfuric acid to dry it. Collect it by downward delivery in a fume cupboard."),
        PQ("State two reactions of chlorine, with equations.", "With iron: [[2Fe + 3Cl2 -> 2FeCl3]]. With potassium bromide solution: [[Cl2 + 2KBr -> 2KCl + Br2]]. (Also with sodium: [[2Na + Cl2 -> 2NaCl]].)"),
        PQ("Explain why hydrogen chloride dissolved in water conducts electricity but hydrogen chloride in methylbenzene does not.", "In water, hydrogen chloride ionizes to give H+ and Cl- ions which carry current. In methylbenzene it stays as molecules, so there are no ions to carry current."),
        SUM("Chlorine: MnO2 + conc. HCl; dried with conc. H2SO4; downward delivery; bleaches damp litmus.",
            "Chlorine displaces bromine and iodine and forms FeCl3 with iron.",
            "Hydrogen chloride: NaCl + conc. H2SO4; very soluble; white fumes with ammonia; white precipitate with silver nitrate.",
            "Dry HCl is not an acid; hydrochloric acid is a strong acid.",
            "Uses of chlorine: water sterilization, bleach, PVC."),
    ]))

# ------------------------------------------------------------------ 14. Reactivity series
LESSONS.append(lesson(
    module=M_IN, topic="Reactivity series and extraction of metals",
    title="The reactivity series: reactions, displacement and protection from rusting",
    slug="chd-reactivity-series", minutes=22,
    summary="Metals are ranked by how vigorously they react with water, acids and oxygen. A more reactive metal displaces a less reactive one from its salt, and zinc protects iron by being more reactive.",
    objectives=["Write the reactivity series and use it to compare metals",
                "Describe the reactions of metals with water, steam, dilute acid and oxygen",
                "Predict and explain displacement reactions with equations",
                "Explain sacrificial protection and galvanizing"],
    key_concepts=["Reactivity series", "Displacement reaction", "Reaction with water and acid", "Thermite reaction", "Sacrificial protection"],
    blocks=[
        H("Why is iron roofing coated with zinc?"),
        T("Roofs in many Cameroonian towns are corrugated iron sheets. A new sheet shines silver, because it has a zinc coating. Why zinc, and why do old sheets rust? To answer, we need the order of reactivity of metals."),
        D("The **reactivity series** is a list of metals in order of how readily they react, from the most reactive to the least reactive.", title="Reactivity series"),
        CODE("""Most reactive
  Potassium    K
  Sodium       Na
  Calcium      Ca
  Magnesium    Mg
  Aluminium    Al
  (Carbon      C)
  Zinc         Zn
  Iron         Fe
  Tin          Sn
  Lead         Pb
  (Hydrogen    H)
  Copper       Cu
  Silver       Ag
  Gold         Au
Least reactive""", "text", title="The reactivity series (carbon and hydrogen shown for comparison)"),
        T("A more reactive metal loses electrons more easily to form its positive ion. The order is the same as in the electrochemical series."),
        H("Reactions with water, steam, acid and oxygen"),
        CODE("""Metal       With cold water              With steam / dilute acid
K, Na       violent: H2 and hydroxide    explosive
Ca          steady fizzing: H2           fast
Mg          very slow                    burns in steam; fast with acid
Zn, Fe      no reaction                  react with steam; Zn fast and Fe
                                         slowly with dilute acid
Cu, Ag, Au  no reaction                  no reaction""", "text", title="How metals react"),
        F(r"{{2Na + 2H2O -> 2NaOH + H2}} \qquad {{Ca + 2H2O -> Ca(OH)2 + H2}}"),
        F(r"{{Mg + H2O -> MgO + H2}} \quad \text{(steam)} \qquad {{3Fe + 4H2O <=> Fe3O4 + 4H2}} \quad \text{(steam)}"),
        F(r"{{Mg + 2HCl -> MgCl2 + H2}} \qquad {{Fe + 2HCl -> FeCl2 + H2}}", title="With dilute acids"),
        T("Metals above hydrogen react with dilute acids and give hydrogen. Copper, silver and gold do not. **With oxygen**, the reactive metals burn: [[2Mg + O2 -> 2MgO]]. Aluminium seems unreactive because a thin, tough layer of aluminium oxide forms on its surface and protects it. Sodium is stored under oil because it reacts with air and water."),
        H("Displacement reactions"),
        D("In a **displacement reaction** a more reactive metal takes the place of a less reactive metal in a solution of its salt. The more reactive metal gives electrons to the ions of the less reactive metal.", title="Displacement"),
        F(r"{{Zn + CuSO4 -> ZnSO4 + Cu}} \qquad {{Zn + Cu^2+ -> Zn^2+ + Cu}}"),
        T("In this reaction zinc is **oxidized** (it loses electrons) and copper ions are **reduced** (they gain electrons). The blue colour of the solution fades and pink-brown copper appears. With an iron nail in copper(II) sulfate solution, the nail is coated with copper and the blue solution turns pale green, as iron(II) sulfate forms: [[Fe + CuSO4 -> FeSO4 + Cu]]. Copper displaces silver: [[Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag]]."),
        T("**Displacing a metal from its oxide.** A more reactive metal can take oxygen from the oxide of a less reactive metal. In the thermite reaction, aluminium reduces iron(III) oxide and makes molten iron, used to weld railway lines."),
        F(r"{{2Al + Fe2O3 -> Al2O3 + 2Fe}}"),
        T("**Heating compounds.** Carbonates of metals high in the series, such as sodium and potassium, are not decomposed by heat. Those lower in the series decompose easily, as with copper carbonate. The less reactive the metal, the less stable its carbonate."),
        H("Using the series to protect iron"),
        T("Iron rusts when it is in contact with **both air (oxygen) and water**. Zinc is more reactive than iron. In **galvanizing**, iron is coated with zinc. Even if the coating is scratched, zinc, being more reactive, corrodes first and the iron beneath does not rust. This is called **sacrificial protection**. Blocks of magnesium or zinc fixed to ships' hulls and buried pipes do the same job. Tin is less reactive than iron, so a tin coat protects only while it is unbroken: once scratched, the iron rusts faster."),
        EX("Worked example 1: predicting", intro="Which of these will react? (a) iron with zinc sulfate solution; (b) zinc with iron(II) sulfate solution; (c) copper with dilute hydrochloric acid.", steps=[
            S("(a) Iron and zinc sulfate", text="Iron is less reactive than zinc, so it cannot displace zinc. No reaction."),
            S("(b) Zinc and iron(II) sulfate", text="Zinc is more reactive, so it displaces iron.", math=r"{{Zn + FeSO4 -> ZnSO4 + Fe}}"),
            S("(c) Copper and dilute acid", text="Copper is below hydrogen, so there is no reaction."),
        ]),
        EX("Worked example 2: mass of copper", intro="Excess zinc is added to copper(II) sulfate solution containing 0.10 mol of copper(II) ions. What mass of copper forms? (Cu = 63.5)", steps=[
            S("Use the equation", math=r"{{Zn + Cu^2+ -> Zn^2+ + Cu}}"),
            S("Mole ratio", text="1 mol of copper ions gives 1 mol of copper, so 0.10 mol."),
            S("Mass", math=r"0.10 \times 63.5 = 6.35 \text{ g}"),
        ]),
        MISTAKE("Writing a displacement the wrong way round", "Only the **more reactive** metal displaces the less reactive one. Check the series first."),
        MISTAKE("Saying aluminium is less reactive than iron", "Aluminium is higher in the series. It only seems unreactive because of its oxide layer."),
        MISTAKE("Forgetting that rust needs both air and water", "Iron in dry air or in water without air does not rust easily. Both oxygen and water are needed."),
        QUIZ("A piece of magnesium ribbon is placed in copper(II) sulfate solution. What is observed?", ["No reaction", "Blue colour fades and pink-brown solid forms", "Blue colour deepens", "A white solid forms and the solution stays blue"], 1,
             "Magnesium is more reactive and displaces copper: the blue copper ions are used up and copper metal forms.",
             hint="Compare magnesium and copper in the series.",
             feedback=["Magnesium is higher than copper, so it displaces it.", "", "The colour fades as copper ions are removed.", "Copper, not a white solid, forms."]),
        QUIZ("Why does zinc protect an iron roof even where the coating is scratched?", ["Zinc is less reactive than iron", "Zinc is more reactive than iron and corrodes first", "Zinc keeps the iron dry", "Zinc stops oxygen reaching the scratch"], 1,
             "Zinc is above iron, so it loses electrons more readily and corrodes in preference to iron.",
             hint="Which metal is higher in the series?",
             feedback=["Zinc is more reactive than iron.", "", "Zinc does not keep the iron dry; it corrodes instead.", "Oxygen can reach the scratch; the protection is from zinc's reactivity."]),
        TIP("Exam link: the reactivity series appears in Paper 1 (predict which reaction occurs) and in Paper 2 (experiments with metals and solutions, and extraction). You will be asked to write equations for displacement, so practise them."),
        PQ("Arrange these metals in order of reactivity, most reactive first: copper, magnesium, iron, sodium.", "Sodium, magnesium, iron, copper."),
        PQ("A strip of copper is put into silver nitrate solution. State what you see and write the equation.", "Silver crystals form on the copper and the solution slowly turns blue. [[Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag]]."),
        PQ("Explain, in terms of reactivity, why a tin-plated can rusts quickly when scratched but a zinc-coated sheet does not.", "Tin is less reactive than iron, so once the coating is broken the iron corrodes in preference to tin. Zinc is more reactive than iron, so the zinc corrodes first and protects the iron."),
        SUM("The reactivity series ranks metals: K, Na, Ca, Mg, Al, Zn, Fe, Sn, Pb, (H), Cu, Ag, Au.",
            "Reactive metals react with water, steam and dilute acid to give hydrogen; copper, silver and gold do not.",
            "A more reactive metal displaces a less reactive one from its salt solution.",
            "Aluminium is protected by its oxide layer.",
            "Zinc protects iron by sacrificial protection."),
    ]))

# ------------------------------------------------------------------ 15. Extraction of metals
LESSONS.append(lesson(
    module=M_IN, topic="Reactivity series and extraction of metals",
    title="Extracting sodium, aluminium, iron and copper",
    slug="chd-extraction-of-metals", minutes=25,
    summary="The method of extraction depends on the metal's place in the reactivity series: sodium and aluminium by electrolysis of the molten compound, iron by reduction with carbon monoxide in the blast furnace, copper by roasting its ore and refining by electrolysis.",
    objectives=["Link the method of extraction to the position of the metal in the series",
                "Describe the extraction of sodium and aluminium by electrolysis",
                "Describe the blast furnace, with equations, and the making of steel",
                "State the properties and uses of sodium, aluminium, iron and copper"],
    key_concepts=["Ore", "Electrolysis of molten compounds", "Downs cell", "Cryolite", "Blast furnace", "Slag", "Steel"],
    blocks=[
        H("From rock to metal"),
        T("The metals in your cooking pot, in the electric cables over your head and in the steel bars of a building were all once in rocks. Most metals are found as compounds. A rock that holds enough of a metal compound to be worth mining is called an **ore**. The metal must be **extracted**, and the method depends on how reactive the metal is."),
        D("An **ore** is a rock that contains a metal or metal compound in an amount large enough to make extraction worthwhile.", title="Ore"),
        CODE("""Metal        Main ore                 Method of extraction
Sodium       rock salt (NaCl)         electrolysis of molten NaCl
Aluminium    bauxite (Al2O3)          electrolysis of Al2O3 in molten cryolite
Iron         haematite (Fe2O3)        reduction by carbon monoxide
Copper       sulfide ores, e.g.       roasting, then refining by electrolysis
             copper pyrites
Silver, Gold found as the metal       physical separation""", "text", title="Extraction methods"),
        T("**Rule:** the most reactive metals (above carbon: potassium, sodium, calcium, magnesium, aluminium) hold on to their oxygen or chlorine too strongly for carbon to remove it. They need **electrolysis** of the molten compound, which costs a lot of electricity. Metals below carbon, such as zinc, iron and lead, can be reduced by heating with carbon. Very unreactive metals such as gold are found uncombined."),
        H("Sodium: electrolysis of molten sodium chloride"),
        T("Sodium is made in a **Downs cell**. Sodium chloride is melted. It melts at a high temperature, so a little calcium chloride is mixed with it to lower the melting point and save energy. A graphite anode and a steel cathode are used."),
        F(r"\text{Cathode: } {{Na^+ + e^- -> Na}} \qquad \text{Anode: } {{2Cl^- -> Cl2 + 2e^-}}"),
        T("Molten sodium floats up and is collected. The chlorine gas is a useful by-product. **Properties:** sodium is a soft, silvery metal that floats on water and reacts violently with it: [[2Na + 2H2O -> 2NaOH + H2]]. It is stored under oil. **Uses:** a coolant in some nuclear reactors, street lamps and making other sodium compounds."),
        H("Aluminium: electrolysis of aluminium oxide"),
        T("The ore is **bauxite**. It is purified to give pure aluminium oxide (alumina), which has a very high melting point. It is dissolved in molten **cryolite**, which lowers the working temperature to about 950 degrees Celsius and makes a good conducting liquid. The cell is a steel tank lined with graphite, which is the cathode. Graphite blocks dipping in the liquid are the anodes."),
        F(r"\text{Cathode: } {{Al^3+ + 3e^- -> Al}} \qquad \text{Anode: } {{2O^2- -> O2 + 4e^-}}"),
        F(r"{{2Al2O3 -> 4Al + 3O2}}", title="Overall equation"),
        T("Molten aluminium sinks to the bottom and is tapped off. The oxygen formed at the anodes reacts with the hot graphite to give carbon dioxide, so the anodes slowly burn away and must be replaced: [[C + O2 -> CO2]]. Aluminium smelting uses a huge amount of electricity, so smelters are built where electricity is cheap. Cameroon's aluminium smelter at Edea uses hydroelectric power from the Sanaga river."),
        T("**Properties:** low density, good conductor of heat and electricity, resists corrosion because of its oxide layer, easy to shape. **Uses:** overhead cables, aircraft, cooking pots, roofing sheets and drink cans."),
        H("Iron: the blast furnace"),
        T("The raw materials are **iron ore** (haematite, [[Fe2O3]]), **coke** (carbon), **limestone** (calcium carbonate) and hot **air**. They are fed in at the top. Hot air is blown in near the bottom."),
        IMG("f5ch-d-blast-furnace.svg", alt="Blast furnace sketch with raw materials at the top, hot air blast near the bottom, molten slag and molten iron tapped at the base, and the main equations",
            caption="Figure 1. The blast furnace. Iron ore is reduced by carbon monoxide; limestone removes sand as slag."),
        KEY("Reactions in the blast furnace", "", cards=[
            ["1. Coke burns", "[[C + O2 -> CO2]]. This gives out heat to raise the furnace temperature."],
            ["2. Carbon monoxide forms", "[[CO2 + C -> 2CO]]. Carbon monoxide is the reducing agent."],
            ["3. Iron ore is reduced", "[[Fe2O3 + 3CO -> 2Fe + 3CO2]]. Molten iron runs to the bottom."],
            ["4. Limestone removes sand", "[[CaCO3 -> CaO + CO2]], then [[CaO + SiO2 -> CaSiO3]]. The calcium silicate is slag."]]),
        T("**Slag** is molten and less dense than iron, so it floats on top of the iron. Both are tapped off separately. The slag is used for road making. The waste gases leaving the top are mainly nitrogen, carbon dioxide and some carbon monoxide."),
        T("**Cast iron** from the furnace is hard but brittle, because it contains about 4% carbon. To make **steel**, much of the carbon is burnt off by blowing oxygen through the molten iron: [[C + O2 -> CO2]]. Steel is strong and is used in buildings, bridges, vehicles and tools. Adding other metals, such as chromium and nickel, gives stainless steel. Pure iron is soft and rusts easily."),
        H("Copper: roasting and refining"),
        T("Copper is often found as sulfide ores. The ore is concentrated and heated in air (roasted), which gives copper and sulfur dioxide, in a simplified equation: [[Cu2S + O2 -> 2Cu + SO2]]. The sulfur dioxide must be collected and made into sulfuric acid, or it would cause acid rain. The copper is then refined by electrolysis, as in the earlier lesson, to give copper that is 99.9% pure or more."),
        T("**Properties:** a reddish-brown metal, a very good conductor of heat and electricity, malleable and ductile, does not react with water or dilute acids. **Uses:** electrical wires, water pipes, cooking utensils, and alloys such as brass (copper and zinc) and bronze (copper and tin)."),
        EX("Worked example 1: mass of iron", intro="What mass of iron can be made from 160 tonnes of iron(III) oxide, assuming complete reduction? (Fe = 56, O = 16)", steps=[
            S("Molar mass of the oxide", math=r"M_r(\mathrm{Fe_2O_3}) = 2 \times 56 + 3 \times 16 = 160"),
            S("Equation", math=r"{{Fe2O3 + 3CO -> 2Fe + 3CO2}} \quad (1 \text{ mol oxide} \rightarrow 2 \text{ mol Fe})"),
            S("Mass of iron", math=r"160 \times \dfrac{2 \times 56}{160} = 112 \text{ tonnes}"),
        ]),
        EX("Worked example 2: mass of aluminium", intro="What mass of aluminium can be obtained from 102 tonnes of aluminium oxide? (Al = 27, O = 16)", steps=[
            S("Molar mass", math=r"M_r(\mathrm{Al_2O_3}) = 2 \times 27 + 3 \times 16 = 102"),
            S("Ratio from 2Al2O3 -> 4Al + 3O2", math=r"1 \text{ mol Al}_2\mathrm{O}_3 \rightarrow 2 \text{ mol Al}"),
            S("Mass", math=r"102 \times \dfrac{2 \times 27}{102} = 54 \text{ tonnes}"),
        ]),
        MISTAKE("Saying that carbon reduces aluminium oxide", "Aluminium is above carbon in the series. Carbon cannot reduce its oxide, so electrolysis is used."),
        MISTAKE("Naming the wrong reducing agent in the blast furnace", "The main reducing agent is carbon monoxide made from coke, not the coke itself or the limestone."),
        MISTAKE("Saying limestone is added to give iron", "Limestone removes sand (silicon dioxide) as slag. It does not help the iron form."),
        QUIZ("What is the purpose of cryolite in the extraction of aluminium?", ["It reduces aluminium oxide", "It lowers the melting point of the electrolyte", "It forms the anodes", "It reacts with oxygen"], 1,
             "Cryolite dissolves aluminium oxide and lets the electrolysis work at about 950 degrees Celsius instead of over 2000 degrees Celsius.",
             hint="Aluminium oxide melts at a very high temperature.",
             feedback=["Reduction is by electrons at the cathode, not by cryolite.", "", "The anodes are graphite.", "The oxygen reacts with the graphite anodes."]),
        QUIZ("In the blast furnace, what is formed when limestone reacts with silicon dioxide?", ["Iron", "Carbon monoxide", "Calcium silicate (slag)", "Calcium carbonate"], 2,
             "Calcium oxide from the limestone combines with silicon dioxide to make calcium silicate, the slag.",
             hint="What does the limestone remove?",
             feedback=["Iron comes from the reduction of its oxide.", "Carbon monoxide comes from carbon dioxide and coke.", "", "Calcium carbonate is the limestone itself."]),
        TIP("Exam link: extraction of metals appears in Paper 1 (which method for which metal) and often as a Paper 2 question on the blast furnace or aluminium cell, with equations and reasons. Link the method to the position in the reactivity series."),
        PQ("Name the raw materials used in the blast furnace and state the purpose of each.", "Iron ore (source of iron), coke (fuel and source of carbon monoxide), limestone (removes sand as slag), hot air (oxygen to burn the coke)."),
        PQ("Write equations for the formation of carbon monoxide and for its reaction with iron(III) oxide in the blast furnace.", "[[C + O2 -> CO2]] then [[CO2 + C -> 2CO]], and [[Fe2O3 + 3CO -> 2Fe + 3CO2]]."),
        PQ("Explain why aluminium is extracted by electrolysis but iron by reduction with carbon monoxide.", "Aluminium is more reactive than carbon, so carbon cannot remove oxygen from its oxide, and electrolysis of the molten compound is needed. Iron is less reactive than carbon, so carbon monoxide can reduce iron oxide."),
        SUM("Method of extraction depends on the position in the reactivity series.",
            "Sodium: electrolysis of molten sodium chloride (Downs cell). Aluminium: aluminium oxide in molten cryolite with graphite electrodes.",
            "Iron: blast furnace; coke, limestone, ore and hot air; carbon monoxide reduces the ore; limestone forms slag with sand.",
            "Steel is made by removing carbon from cast iron with oxygen.",
            "Copper: roast the sulfide ore, then refine by electrolysis."),
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


LESSONS = _fix(LESSONS)
