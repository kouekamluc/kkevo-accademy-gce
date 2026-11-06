"""Form 5 Chemistry: Formulae, Stoichiometry & Mole Concept (10 lessons, one practice set each).

Relative atomic masses used: H 1, C 12, N 14, O 16, Na 23, Mg 24, Al 27, S 32, Cl 35.5, K 39, Ca 40, Fe 56, Cu 64,
Zn 65, Ag 108. Molar gas volume: 24 dm3 at room temperature and pressure (rtp); 22.4 dm3 at stp (stated in each question).
"""

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "form-5")

MODULE = "Formulae, Stoichiometry & Mole Concept"
T1 = "Symbols, valency and balanced equations"
T2 = "Relative formula mass and percentage composition"
T3 = "The mole and Avogadro's constant"
T4 = "Empirical and molecular formulae"
T5 = "Molar gas volume and gas laws"
T6 = "Solution concentration"
T7 = "Reacting masses and titration calculations"

LESSONS = []

# ------------------------------------------------------------------ 1. Symbols, valency, formulae
LESSONS.append(lesson(
    module=MODULE,
    topic=T1,
    title="Symbols, valency and writing formulae",
    slug="chb-symbols-valency-formulae",
    minutes=22,
    summary="Use chemical symbols, valency and radicals to write the correct formula of an ionic or simple covalent compound with the criss-cross method.",
    objectives=[
        "Write the symbols of common elements correctly, using capital and small letters",
        "State the valency of common elements and radicals",
        "Use the criss-cross method to write formulae, using brackets for radicals",
        "Name simple compounds from their formulae",
    ],
    key_concepts=["Chemical symbol", "Valency", "Radical", "Chemical formula", "Criss-cross method"],
    blocks=[
        H("Introduction"),
        T("Look at a bag of fertilizer in a Bamenda or Buea market. It says NPK. N, P and K are chemical symbols, the short "
          "language chemists use all over the world. A cooking gas cylinder, a bag of salt and a sachet of oral rehydration salts "
          "all contain compounds with a fixed formula. In this lesson you will learn how to write that formula correctly."),
        H("Symbols"),
        D("A **chemical symbol** is one capital letter, or one capital letter followed by one small letter, that stands for one element. "
          "The second letter is always small.", title="Definition: symbol"),
        CODE("""Element      Symbol     Element      Symbol
hydrogen     H          calcium      Ca
carbon       C          iron         Fe   (from Latin ferrum)
nitrogen     N          copper       Cu   (cuprum)
oxygen       O          zinc         Zn
sodium       Na         silver       Ag   (argentum)
magnesium    Mg         potassium    K    (kalium)
aluminium    Al         sulfur       S
chlorine     Cl""", "text", title="Symbols to know"),
        MISTAKE("Wrong capital letters", "Co is cobalt but CO is carbon monoxide, a compound. Cl is chlorine but CL means nothing. "
                "Always write a capital first and a small letter second."),
        H("Valency"),
        D("The **valency** of an element is the number of electrons its atom gains, loses or shares when it forms a compound. "
          "It tells us how many bonds an atom can make. Metals lose electrons to form positive ions. Non-metals gain electrons to form negative ions.",
          title="Definition: valency"),
        D("A **radical** is a group of atoms that stays together as one unit and carries a charge. Examples are hydroxide, nitrate, "
          "carbonate and sulfate. Radicals are written in brackets when more than one is needed.", title="Definition: radical"),
        CODE("""Valency 1            Valency 2              Valency 3
H+   hydrogen        Mg2+  magnesium        Al3+   aluminium
Na+  sodium          Ca2+  calcium          Fe3+   iron(III)
K+   potassium       Zn2+  zinc             PO4 3- phosphate
Ag+  silver          Cu2+  copper(II)
NH4+ ammonium        Fe2+  iron(II)
Cl-  chloride        O2-   oxide
OH-  hydroxide       S2-   sulfide
NO3- nitrate         CO3 2- carbonate
HCO3- hydrogencarbonate  SO4 2- sulfate""", "text", title="Common ions and their charges"),
        TIP("Sulfate is also spelt sulphate in some books and papers. Iron and copper can have more than one valency, so the "
            "name carries a Roman numeral: iron(II) and iron(III) differ."),
        H("The criss-cross method"),
        T("A compound has no overall charge. So the positive charges and the negative charges must cancel. "
          "The criss-cross method gives this quickly: swap the charge numbers and write them as small numbers (subscripts) after the symbols."),
        IMG("f5ch-b-crisscross.svg", alt="Criss-cross method for aluminium oxide: Al with charge 3+ and O with charge 2- give Al2O3 after the numbers are swapped",
            caption="Figure 1. Swap the charge numbers: Al³⁺ and O²⁻ give Al₂O₃."),
        KEY("Writing a formula in four steps", "Follow the same steps every time.", cards=[
            ["1. Write the symbols", "Put the positive ion first, then the negative ion."],
            ["2. Write the charges", "For example $\\mathrm{Mg^{2+}}$ and $\\mathrm{Cl^-}$."],
            ["3. Swap the numbers", "The charge number of one ion becomes the subscript of the other. Ignore the signs."],
            ["4. Simplify and check", "Divide by a common factor if there is one. Use brackets round a radical when its subscript is more than 1."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: calcium chloride", steps=[
            S("Write the ions", math=r"\mathrm{Ca^{2+}} \quad \mathrm{Cl^-}"),
            S("Swap the numbers", text="Calcium has charge 2, so chlorine gets subscript 2. Chloride has charge 1, so calcium gets subscript 1 (not written)."),
            S("Write the formula", math=r"\mathrm{CaCl_2}"),
        ], intro="Write the formula of calcium chloride.", check=r"\text{one } 2+ \text{ ion and two } 1- \text{ ions: } +2 - 2 = 0"),
        EX("Worked example 2: aluminium sulfate (a radical)", steps=[
            S("Write the ions", math=r"\mathrm{Al^{3+}} \quad \mathrm{SO_4^{2-}}"),
            S("Swap the numbers", text="Aluminium gets subscript 2 on sulfate. Sulfate gets subscript 3 on aluminium."),
            S("Put the radical in brackets before adding its subscript", math=r"\mathrm{Al_2(SO_4)_3}"),
        ], intro="Write the formula of aluminium sulfate.", check=r"2 \times (+3) + 3 \times (-2) = 0"),
        EX("Worked example 3: when the numbers simplify", steps=[
            S("Write the ions", math=r"\mathrm{Mg^{2+}} \quad \mathrm{O^{2-}}"),
            S("Swap the numbers", math=r"\mathrm{Mg_2O_2}"),
            S("Divide both subscripts by 2", math=r"\mathrm{MgO}"),
        ], intro="Write the formula of magnesium oxide.", check=r"+2 - 2 = 0"),
        EX("Worked example 4: iron with two valencies", steps=[
            S("Read the Roman numeral", text="Iron(III) means $\\mathrm{Fe^{3+}}$."),
            S("Write the ions", math=r"\mathrm{Fe^{3+}} \quad \mathrm{O^{2-}}"),
            S("Swap the numbers", math=r"\mathrm{Fe_2O_3}"),
        ], intro="Write the formula of iron(III) oxide. Then say what iron(II) oxide would be.",
           check=r"\text{Iron(II) oxide is FeO, because } \mathrm{Fe^{2+}} \text{ and } \mathrm{O^{2-}} \text{ cancel}"),
        H("Common mistakes"),
        MISTAKE("Missing brackets", "Calcium hydroxide is $\\mathrm{Ca(OH)_2}$, not $\\mathrm{CaOH_2}$. $\\mathrm{CaOH_2}$ means one oxygen and two hydrogens. "
                "Brackets keep the radical together."),
        MISTAKE("Writing the charges as part of the formula", "The formula of sodium chloride is NaCl, not $\\mathrm{Na^+Cl^-}$. Charges belong to ions; a formula shows the ratio of atoms."),
        MISTAKE("Changing the radical", "In $\\mathrm{(NH_4)_2SO_4}$ the 2 outside the bracket multiplies everything inside. The radical $\\mathrm{NH_4}$ keeps its own 4."),
        QUIZ("What is the formula of magnesium nitrate?",
             [r"$\mathrm{MgNO_3}$", r"$\mathrm{Mg(NO_3)_2}$", r"$\mathrm{Mg_2NO_3}$", r"$\mathrm{Mg_2(NO_3)_2}$"], 1,
             r"Magnesium is $\mathrm{Mg^{2+}}$ and nitrate is $\mathrm{NO_3^-}$. Two nitrate ions are needed, so $\mathrm{Mg(NO_3)_2}$.",
             hint="Nitrate is a radical, so use brackets when it appears more than once.",
             feedback=["One $\\mathrm{Mg^{2+}}$ (+2) and one $\\mathrm{NO_3^-}$ (-1) do not cancel.", "",
                       "The 2 has been put on magnesium. Two magnesium ions (+4) and one nitrate ion (-1) do not cancel.",
                       "Two magnesium ions (+4) and two nitrate ions (-2) do not cancel. Swap the charge numbers instead."]),
        QUIZ("What is the valency of iron in $\\mathrm{Fe_2O_3}$?",
             ["1", "2", "3", "6"], 2,
             r"Three $\mathrm{O^{2-}}$ ions give a total charge of $-6$. Two iron ions must give $+6$, so each is $+3$.",
             hint="Total negative charge from the oxide ions must be cancelled by the two iron ions.",
             feedback=["Valency 1 would not balance two oxide ions.", "Iron(II) would give $\\mathrm{FeO}$.", "", "6 is the total charge on both iron ions, not on one."]),
        TIP("Formula writing appears in Paper 1 multiple choice and in Paper 2 questions on bonding, salts and equations. "
            "The Board's report asks teachers to stress using electron arrangement to work out valency and write formulae, so practise until it is automatic."),
        PQ("Write the formula of (a) zinc carbonate, (b) ammonium sulfate, (c) iron(III) hydroxide.",
           r"(a) $\mathrm{Zn^{2+}}$ and $\mathrm{CO_3^{2-}}$ cancel, so $\mathrm{ZnCO_3}$. (b) $\mathrm{NH_4^+}$ and $\mathrm{SO_4^{2-}}$: two ammonium ions, so $\mathrm{(NH_4)_2SO_4}$. "
           r"(c) $\mathrm{Fe^{3+}}$ and $\mathrm{OH^-}$: three hydroxide ions, so $\mathrm{Fe(OH)_3}$."),
        PQ("Name the compounds (a) $\\mathrm{CuCl_2}$, (b) $\\mathrm{K_2SO_4}$, (c) $\\mathrm{Ca(OH)_2}$.",
           "(a) copper(II) chloride. (b) potassium sulfate. (c) calcium hydroxide."),
        PQ("How many atoms of each element are in one formula unit of $\\mathrm{Ca(NO_3)_2}$?",
           r"Ca: 1. N: 2 (the subscript 2 multiplies the bracket). O: $3 \times 2 = 6$. The formula unit has $1 + 2 + 6 = 9$ atoms."),
        PQ("Aluminium has valency 3 and sulfur (as sulfide) has valency 2. Write the formula of aluminium sulfide.",
           r"Swap the numbers: $\mathrm{Al_2S_3}$. Check: $2 \times 3 = 6$ and $3 \times 2 = 6$."),
        SUM("A symbol is one capital letter or a capital plus a small letter.",
            "Valency is the number of electrons an atom gains, loses or shares; a radical is a charged group that stays together.",
            "Criss-cross: write the ions, swap the charge numbers, simplify, and use brackets for a radical needing a subscript.",
            "A formula shows the ratio of atoms or ions; it has no charges written in it."),
    ],
))

# ------------------------------------------------------------------ 2. Balancing equations
LESSONS.append(lesson(
    module=MODULE,
    topic=T1,
    title="Writing and balancing chemical equations",
    slug="chb-balancing-equations",
    minutes=24,
    summary="Write word and symbol equations, balance them by counting atoms with whole-number coefficients, add state symbols and balance a simple ionic equation.",
    objectives=[
        "Translate a word equation into a formula equation",
        "Balance an equation by changing coefficients, never subscripts",
        "Add state symbols (s), (l), (g) and (aq) correctly",
        "Balance a simple ionic equation for both atoms and charge",
    ],
    key_concepts=["Reactants and products", "Law of conservation of mass", "Coefficient", "State symbol", "Ionic equation"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian kitchens the cooking gas is butane. When it burns, the atoms in butane and in the oxygen of the air rearrange into carbon dioxide and water. "
          "No atom is created and none is lost. A **balanced equation** is the chemist's way of showing this."),
        D("In a chemical reaction the total mass of the products equals the total mass of the reactants. Atoms are only rearranged. "
          "So every equation must have the same number of atoms of each element on both sides.", title="Law of conservation of mass"),
        D("**Reactants** are the substances that react. **Products** are the substances formed. An equation is written reactants → products. "
          "A **coefficient** is the big number in front of a formula. It shows how many units of that substance react or form.", title="Definitions"),
        KEY("State symbols", "Add them after each formula when the question asks for them.", cards=[
            ["(s)", "solid"], ["(l)", "liquid"], ["(g)", "gas"], ["(aq)", "dissolved in water (aqueous)"],
        ]),
        H("How to balance an equation"),
        KEY("The method", "Always follow the same order.", cards=[
            ["1. Write the correct formulae", "Use valency. Never change a formula to help the balancing."],
            ["2. Count atoms", "Count each element on the left and on the right. Treat a radical in brackets as one group if it is unchanged."],
            ["3. Change coefficients", "Start with the element that appears in the fewest places. Leave hydrogen and oxygen until last."],
            ["4. Check", "Count every element again. Reduce to the smallest whole numbers."],
        ]),
        MISTAKE("Changing the subscript", "To balance $\\mathrm{H_2 + O_2 \\rightarrow H_2O}$ do not write $\\mathrm{H_2O_2}$. That is a different substance (hydrogen peroxide). "
                "Only the coefficients can change."),
        H("Worked examples"),
        EX("Worked example 1: magnesium burning", steps=[
            S("Write the formulae", math=r"\mathrm{Mg + O_2 \rightarrow MgO}"),
            S("Count the atoms", text="Left: 1 Mg and 2 O. Right: 1 Mg and 1 O. Oxygen is unbalanced."),
            S("Put 2 in front of MgO", math=r"\mathrm{Mg + O_2 \rightarrow 2MgO}", text="Now Mg is unbalanced: 1 on the left and 2 on the right."),
            S("Put 2 in front of Mg", math=r"\mathrm{2Mg + O_2 \rightarrow 2MgO}"),
            S("Add state symbols", math=r"\mathrm{2Mg(s) + O_2(g) \rightarrow 2MgO(s)}"),
        ], intro="Balance the equation for magnesium burning in oxygen.", check=r"\text{Left: 2 Mg, 2 O. Right: 2 Mg, 2 O.}"),
        EX("Worked example 2: burning cooking gas (butane)", steps=[
            S("Write the formulae", math=r"\mathrm{C_4H_{10} + O_2 \rightarrow CO_2 + H_2O}"),
            S("Balance carbon", math=r"\mathrm{C_4H_{10} + O_2 \rightarrow 4CO_2 + H_2O}"),
            S("Balance hydrogen", math=r"\mathrm{C_4H_{10} + O_2 \rightarrow 4CO_2 + 5H_2O}"),
            S("Count oxygen on the right", text="$4 \\times 2 + 5 = 13$ atoms. $\\mathrm{O_2}$ gives 2 atoms each, so we need 6.5 molecules."),
            S("Double everything to remove the fraction", math=r"\mathrm{2C_4H_{10} + 13O_2 \rightarrow 8CO_2 + 10H_2O}"),
        ], intro="Balance the equation for the complete combustion of butane.", check=r"\text{C: 8 and 8. H: 20 and 20. O: 26 and } 16 + 10 = 26."),
        EX("Worked example 3: extracting iron", steps=[
            S("Write the formulae", math=r"\mathrm{Fe_2O_3 + CO \rightarrow Fe + CO_2}"),
            S("Balance iron", math=r"\mathrm{Fe_2O_3 + CO \rightarrow 2Fe + CO_2}"),
            S("Oxygen: 3 in $\\mathrm{Fe_2O_3}$ and 1 in CO give 4 on the left", text="Each $\\mathrm{CO_2}$ has 2 oxygen atoms and 1 carbon atom. Three CO make three $\\mathrm{CO_2}$: this balances C and O."),
            S("Final equation", math=r"\mathrm{Fe_2O_3 + 3CO \rightarrow 2Fe + 3CO_2}"),
        ], intro="Balance the equation for the reduction of iron(III) oxide by carbon monoxide.", check=r"\text{Fe: 2 and 2. C: 3 and 3. O: } 3 + 3 = 6 \text{ and } 3 \times 2 = 6."),
        EX("Worked example 4: an ionic equation", steps=[
            S("Silver ions meet chloride ions", math=r"\mathrm{Ag^+(aq) + Cl^-(aq) \rightarrow AgCl(s)}"),
            S("Check atoms", text="1 Ag and 1 Cl on each side."),
            S("Check charge", text="Left: $+1 + (-1) = 0$. Right: AgCl has no charge, so 0."),
        ], intro="Silver nitrate solution is added to sodium chloride solution and a white solid forms. Write the ionic equation.",
           check=r"\text{Atoms and charges are both balanced.}"),
        TIP("In an ionic equation the total charge must also be the same on both sides. For example $\\mathrm{Fe^{3+} + 3OH^- \\rightarrow Fe(OH)_3}$: left $+3 - 3 = 0$, right 0. "
            "Ions that do not change (spectator ions) are left out."),
        QUIZ(r"Which equation is balanced?",
             [r"$\mathrm{Al + O_2 \rightarrow Al_2O_3}$", r"$\mathrm{2Al + 3O_2 \rightarrow 2Al_2O_3}$",
              r"$\mathrm{4Al + 3O_2 \rightarrow 2Al_2O_3}$", r"$\mathrm{4Al + 2O_2 \rightarrow 2Al_2O_3}$"], 2,
             r"Left: 4 Al and 6 O. Right: $2 \times 2 = 4$ Al and $2 \times 3 = 6$ O.",
             hint="Count Al and O on each side for every option.",
             feedback=["This is not balanced: Al is 1 and 2, O is 2 and 3.",
                       "Left: 2 Al and 6 O. Right: 4 Al and 6 O. Aluminium does not balance.", "",
                       "Left: 4 Al and 4 O. Right: 4 Al and 6 O. Oxygen does not balance."]),
        QUIZ("A student balances $\\mathrm{H_2 + O_2 \\rightarrow H_2O}$ by writing $\\mathrm{H_2 + O_2 \\rightarrow H_2O_2}$. What is wrong?",
             ["Nothing; the oxygen atoms now balance",
              "She changed a subscript, which changes the substance",
              "She should have written 2O in front of oxygen",
              "Hydrogen should be written as H, not $\\mathrm{H_2}$"], 1,
             r"Changing a subscript makes a different compound. Use coefficients: $\mathrm{2H_2 + O_2 \rightarrow 2H_2O}$.",
             hint="Which numbers is she allowed to change?",
             feedback=["$\\mathrm{H_2O_2}$ is hydrogen peroxide, not water.", "",
                       "Coefficients go in front of whole formulae, and 2O is not oxygen gas.",
                       "Hydrogen gas exists as $\\mathrm{H_2}$ molecules; the formula is correct."]),
        TIP("Balancing appears in nearly every part of Chemistry, in Paper 1 and in Paper 2 questions on reactions, electrolysis and calculations. "
            "The Board's report says candidates need to write equations and ionic equations confidently, so always show the balanced equation first in a calculation."),
        PQ("Balance: $\\mathrm{Na + H_2O \\rightarrow NaOH + H_2}$.",
           r"$\mathrm{2Na + 2H_2O \rightarrow 2NaOH + H_2}$. Check: Na 2 and 2, H $4$ and $2 + 2 = 4$, O 2 and 2."),
        PQ("Balance: $\\mathrm{C_3H_8 + O_2 \\rightarrow CO_2 + H_2O}$.",
           r"$\mathrm{C_3H_8 + 5O_2 \rightarrow 3CO_2 + 4H_2O}$. Check: C 3 and 3, H 8 and 8, O 10 and $6 + 4 = 10$."),
        PQ("Balance: $\\mathrm{Ca(OH)_2 + HCl \\rightarrow CaCl_2 + H_2O}$.",
           r"$\mathrm{Ca(OH)_2 + 2HCl \rightarrow CaCl_2 + 2H_2O}$. Check: Ca 1 and 1, O 2 and 2, H $2 + 2 = 4$ and 4, Cl 2 and 2."),
        PQ("Write a balanced ionic equation, with state symbols, for iron(III) ions reacting with hydroxide ions to give solid iron(III) hydroxide.",
           r"$\mathrm{Fe^{3+}(aq) + 3OH^-(aq) \rightarrow Fe(OH)_3(s)}$. Charge: left $+3 - 3 = 0$; right 0."),
        SUM("An equation shows reactants → products with the same number of each atom on both sides.",
            "Balance by changing coefficients only. Never change a subscript.",
            "Count each element before and after you finish; reduce to the smallest whole numbers.",
            "State symbols are (s), (l), (g) and (aq). Ionic equations must balance in atoms and in charge."),
    ],
))

# ------------------------------------------------------------------ 3. Relative formula mass and percentage composition
LESSONS.append(lesson(
    module=MODULE,
    topic=T2,
    title="Relative formula mass and percentage composition",
    slug="chb-formula-mass-percentage",
    minutes=22,
    summary="Calculate relative formula mass from relative atomic masses and use it to find the percentage by mass of an element in a compound.",
    objectives=[
        "Define relative atomic mass and relative molecular or formula mass",
        "Calculate $M_r$ for compounds, including those with brackets",
        "Calculate the percentage by mass of an element in a compound",
        "Use percentage composition to compare fertilizers and ores",
    ],
    key_concepts=["Relative atomic mass", "Relative formula mass", "Relative molecular mass", "Percentage composition"],
    blocks=[
        H("Introduction"),
        T("A farmer in Dschang can buy urea, ammonium nitrate or ammonium sulfate. All three give the crop nitrogen, but a kilogram of one gives more nitrogen "
          "than a kilogram of another. To compare them fairly we need the **percentage by mass** of nitrogen in each. "
          "First we need the mass of a whole formula, called its relative formula mass."),
        H("Relative masses"),
        D("The **relative atomic mass**, $A_r$, of an element is the average mass of its atoms compared with one twelfth of the mass of a carbon-12 atom. "
          "It has no unit because it is a ratio.", title="Definition: relative atomic mass"),
        D("The **relative molecular mass**, $M_r$, is the sum of the relative atomic masses of all the atoms in a molecule. For an ionic compound, "
          "which has no molecules, we say **relative formula mass**. Both are written $M_r$ and have no unit.", title="Definition: $M_r$",
          formula=r"M_r = \sum A_r \text{ of all atoms in the formula}"),
        CODE("""Use these A_r values:
H 1    C 12   N 14   O 16   Na 23   Mg 24   Al 27
S 32   Cl 35.5   K 39   Ca 40   Fe 56   Cu 64   Zn 65   Ag 108""", "text", title="Relative atomic masses used in this module"),
        KEY("Four steps for $M_r$", "Follow these every time.", cards=[
            ["1. Write the formula", "Check it is correct first."],
            ["2. Count atoms", "Multiply by any subscript. A number outside a bracket multiplies everything inside it."],
            ["3. Multiply by $A_r$", "Use the values in your table."],
            ["4. Add", "Write the answer with no unit."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: calcium hydroxide", steps=[
            S("Count atoms in $\\mathrm{Ca(OH)_2}$", text="Ca: 1. O: 2. H: 2."),
            S("Multiply and add", math=r"M_r = 40 + (2 \times 16) + (2 \times 1)"),
            S("Answer", math=r"M_r = 40 + 32 + 2 = 74"),
        ], intro=r"Calculate $M_r$ of $\mathrm{Ca(OH)_2}$.", check=r"40 + 2(16 + 1) = 74"),
        EX("Worked example 2: aluminium sulfate", steps=[
            S("Count atoms in $\\mathrm{Al_2(SO_4)_3}$", text="Al: 2. S: 3. O: $4 \\times 3 = 12$."),
            S("Multiply and add", math=r"M_r = (2 \times 27) + (3 \times 32) + (12 \times 16)"),
            S("Answer", math=r"M_r = 54 + 96 + 192 = 342"),
        ], intro=r"Calculate $M_r$ of $\mathrm{Al_2(SO_4)_3}$."),
        H("Percentage composition"),
        D("The **percentage composition** by mass of an element in a compound is the part of the formula mass that is that element, written as a percentage.",
          title="Definition: percentage composition",
          formula=r"\%\text{ of element} = \frac{\text{number of atoms} \times A_r}{M_r} \times 100"),
        EX("Worked example 3: nitrogen in a fertilizer", steps=[
            S("Find $M_r$ of $\\mathrm{NH_4NO_3}$", math=r"M_r = 2(14) + 4(1) + 3(16) = 28 + 4 + 48 = 80"),
            S("Mass of nitrogen in one formula", text="There are 2 N atoms: $2 \\times 14 = 28$."),
            S("Divide and multiply by 100", math=r"\frac{28}{80} \times 100 = 35.0\%"),
        ], intro=r"Calculate the percentage by mass of nitrogen in ammonium nitrate, $\mathrm{NH_4NO_3}$.",
           check=r"\text{Check: } 35.0\% \text{ N} + 5.0\% \text{ H} + 60.0\% \text{ O} = 100\%"),
        EX("Worked example 4: iron in an ore", steps=[
            S("Find $M_r$ of $\\mathrm{Fe_2O_3}$", math=r"M_r = 2(56) + 3(16) = 112 + 48 = 160"),
            S("Percentage of iron", math=r"\frac{112}{160} \times 100 = 70.0\%"),
            S("Use it: mass of iron in 5000 kg of pure $\\mathrm{Fe_2O_3}$", math=r"\frac{70}{100} \times 5000 = 3500 \text{ kg}"),
        ], intro=r"Find the percentage of iron in iron(III) oxide, $\mathrm{Fe_2O_3}$, and the mass of iron in 5000 kg of it."),
        EX("Worked example 5: water in a hydrated salt", steps=[
            S("Find $M_r$ of $\\mathrm{CuSO_4 \\cdot 5H_2O}$", text="The dot means five water molecules are attached to each $\\mathrm{CuSO_4}$ unit. You will study this in the lesson on water of crystallization."),
            S("Add", math=r"M_r = 64 + 32 + 64 + 5(18) = 160 + 90 = 250"),
            S("Percentage of water", math=r"\frac{90}{250} \times 100 = 36\%"),
        ], intro=r"Calculate the percentage of water in hydrated copper(II) sulfate, $\mathrm{CuSO_4 \cdot 5H_2O}$."),
        H("Common mistakes"),
        MISTAKE("Ignoring the bracket", r"For $\mathrm{Ca(OH)_2}$ the 2 multiplies both O and H. Writing $40 + 16 + 1 = 57$ is wrong. The answer is 74."),
        MISTAKE("Writing a unit for $M_r$", r"$M_r$ is a relative value, so it has no unit. It is the molar mass (next lesson) that carries g/mol."),
        MISTAKE("Using $A_r$ once for several atoms", r"In $\mathrm{NH_4NO_3}$ there are two N atoms, so use $2 \times 14$. Count every atom, not every element."),
        QUIZ(r"What is $M_r$ of $\mathrm{(NH_4)_2SO_4}$?",
             ["114", "132", "96", "68"], 1,
             r"$2(14) + 8(1) + 32 + 4(16) = 28 + 8 + 32 + 64 = 132$.",
             hint="The 2 outside the bracket multiplies N and H.",
             feedback=["You ignored the 2 outside the bracket and counted one N and four H: $14 + 4 + 32 + 64 = 114$.", "",
                       "You added only the sulfate part, $32 + 64 = 96$, and left out the ammonium.",
                       "You left out the oxygen: $28 + 8 + 32 = 68$. The formula has 4 oxygen atoms."]),
        QUIZ(r"What is the percentage by mass of copper in CuO?",
             ["50%", "75%", "80%", "20%"], 2,
             r"$M_r = 64 + 16 = 80$. Copper is $64/80 \times 100 = 80\%$.",
             hint="Divide the mass of copper by the $M_r$ of the whole formula.",
             feedback=["50% would mean equal masses of Cu and O.", "75% does not match $64/80$. Work out the fraction carefully.", "",
                       "20% is the percentage of oxygen, not copper."]),
        TIP("Percentage composition and $M_r$ questions appear in Paper 1 multiple choice and in the calculation parts of Paper 2. "
            "Give the answer to three significant figures unless the question says otherwise, and show the $M_r$ working."),
        PQ(r"Calculate $M_r$ of (a) $\mathrm{Na_2CO_3}$ and (b) $\mathrm{Mg(NO_3)_2}$.",
           r"(a) $2(23) + 12 + 3(16) = 46 + 12 + 48 = 106$. (b) $24 + 2(14 + 48) = 24 + 124 = 148$."),
        PQ(r"Calculate the percentage by mass of magnesium in magnesium oxide, MgO.",
           r"$M_r = 24 + 16 = 40$. $\frac{24}{40} \times 100 = 60.0\%$."),
        PQ(r"Which gives a farmer more nitrogen per kilogram: urea, $\mathrm{CO(NH_2)_2}$, or potassium nitrate, $\mathrm{KNO_3}$? Show your working.",
           r"Urea: $M_r = 12 + 16 + 2(14 + 2) = 60$, $\%\text{N} = 28/60 \times 100 = 46.7\%$. $\mathrm{KNO_3}$: $M_r = 39 + 14 + 48 = 101$, $\%\text{N} = 14/101 \times 100 = 13.9\%$. Urea gives more."),
        PQ(r"Calculate the mass of calcium in 250 g of calcium carbonate, $\mathrm{CaCO_3}$.",
           r"$M_r = 40 + 12 + 48 = 100$, so calcium is 40.0%. Mass $= 0.40 \times 250 = 100$ g."),
        SUM(r"$M_r$ is the sum of the $A_r$ values of all atoms in the formula and has no unit.",
            "A number outside a bracket multiplies every atom inside it.",
            r"Percentage of an element = (number of atoms $\times A_r$) $\div M_r \times 100$.",
            "The percentages of all elements in a compound add up to 100%."),
    ],
))

# ------------------------------------------------------------------ 4. The mole
LESSONS.append(lesson(
    module=MODULE,
    topic=T3,
    title="The mole, Avogadro's constant and molar mass",
    slug="chb-the-mole",
    minutes=24,
    summary="Define the mole, use Avogadro's constant and molar mass to convert between mass, amount in moles and number of particles.",
    objectives=[
        "State what a mole is and give the value of Avogadro's constant",
        "Calculate the amount in moles from mass and molar mass, and the reverse",
        "Calculate the number of particles from the amount in moles",
        "Tell apart molecules, atoms and moles in a sample",
    ],
    key_concepts=["Mole", "Avogadro's constant", "Molar mass", "Amount of substance"],
    blocks=[
        H("Introduction"),
        T("At Mokolo market eggs are sold by the crate of 30, not one at a time. Atoms are so small that a chemist needs a much bigger counting unit. "
          "That unit is the **mole**. One mole of any substance contains the same number of particles, just as every crate of 30 holds 30 eggs. "
          "The amount of substance is measured in moles, with the symbol $n$."),
        D("The **mole** is the amount of substance that contains $6.02 \\times 10^{23}$ particles (atoms, molecules or ions). "
          "This number is the same as the number of atoms in exactly 12 g of carbon-12.", title="Definition: mole"),
        D("**Avogadro's constant**, $N_A$, is the number of particles in one mole.", title="Definition: Avogadro's constant",
          formula=r"N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}"),
        D("The **molar mass**, $M$, is the mass of one mole of a substance. Its unit is g/mol. "
          "It has the same number as $A_r$ (for an element) or $M_r$ (for a compound).", title="Definition: molar mass"),
        CODE("""Substance   Ar or Mr   Molar mass M
C           12         12 g/mol
H2O         18         18 g/mol
CO2         44         44 g/mol
NaCl        58.5       58.5 g/mol
CaCO3       100        100 g/mol""", "text", title="Same number, different unit"),
        H("Two formulae"),
        F(r"n = \frac{m}{M}", title="Amount from mass"),
        F(r"N = n \times N_A", title="Number of particles from amount"),
        T("Here $n$ is the amount in mol, $m$ is the mass in g, $M$ is the molar mass in g/mol and $N$ is the number of particles. "
          "Rearranged: $m = n \\times M$ and $M = m \\div n$."),
        CODE("""Moles <----- divide by M ------ Mass (g)
Moles ------ multiply by M ----> Mass (g)
Moles ------ multiply by 6.02 x 10^23 ----> Number of particles""", "text", title="Moving between quantities"),
        H("Worked examples"),
        EX("Worked example 1: moles from mass", steps=[
            S("Molar mass of water", math=r"M = 2(1) + 16 = 18 \text{ g/mol}"),
            S("Use $n = m/M$", math=r"n = \frac{36}{18} = 2.0 \text{ mol}"),
        ], intro="How many moles are in 36 g of water?"),
        EX("Worked example 2: mass from moles", steps=[
            S("Molar mass of $\\mathrm{CaCO_3}$", math=r"M = 40 + 12 + 48 = 100 \text{ g/mol}"),
            S("Use $m = n \\times M$", math=r"m = 0.25 \times 100 = 25 \text{ g}"),
        ], intro=r"Find the mass of 0.25 mol of calcium carbonate."),
        EX("Worked example 3: counting molecules", steps=[
            S("Moles of water", math=r"n = \frac{9}{18} = 0.50 \text{ mol}"),
            S("Number of molecules", math=r"N = 0.50 \times 6.02 \times 10^{23} = 3.01 \times 10^{23}"),
        ], intro="How many water molecules are in 9 g of water? Use $N_A = 6.02 \\times 10^{23}$ per mol."),
        EX("Worked example 4: counting atoms", steps=[
            S("Moles of $\\mathrm{CO_2}$", math=r"n = \frac{4.4}{44} = 0.10 \text{ mol}"),
            S("Number of molecules", math=r"0.10 \times 6.02 \times 10^{23} = 6.02 \times 10^{22}"),
            S("Each molecule has 3 atoms (1 C and 2 O)", math=r"3 \times 6.02 \times 10^{22} = 1.81 \times 10^{23} \text{ atoms}"),
        ], intro=r"How many atoms are in 4.4 g of carbon dioxide?",
           check=r"3 \times 6.02 \times 10^{22} = 18.06 \times 10^{22} = 1.806 \times 10^{23} \approx 1.81 \times 10^{23}"),
        H("Common mistakes"),
        MISTAKE("Mixing up atoms and molecules", r"One mole of oxygen gas, $\mathrm{O_2}$, has $6.02 \times 10^{23}$ molecules but twice as many atoms. "
                "Read the question: are you counting molecules or atoms?"),
        MISTAKE("Wrong unit", "Molar mass is in g/mol, mass is in g and amount is in mol. Write the units in each step so that they cancel properly."),
        MISTAKE("Dividing when you should multiply", r"If the amount is given and you want the mass, multiply: $m = n \times M$. Check that the answer is sensible: 0.25 mol cannot weigh more than 1 mol."),
        QUIZ("How many moles are in 5.85 g of sodium chloride, NaCl? ($M = 58.5$ g/mol)",
             ["10 mol", "1.0 mol", "0.10 mol", "0.01 mol"], 2,
             r"$n = 5.85 \div 58.5 = 0.10$ mol.",
             hint="Use $n = m \\div M$.",
             feedback=["You moved the decimal point the wrong way. 5.85 g is a small part of the 58.5 g in one mole, so the answer must be below 1.",
                       "This would need 58.5 g of NaCl.", "", "This is ten times too small; recheck the division."]),
        QUIZ(r"Which contains the same number of molecules as 1 mol of $\mathrm{CO_2}$?",
             [r"1 g of $\mathrm{H_2}$", r"1 mol of $\mathrm{H_2O}$", r"44 mol of $\mathrm{O_2}$", r"44 g of $\mathrm{O_2}$"], 1,
             r"Equal amounts in moles always contain equal numbers of particles, whatever the substance.",
             hint="What does the mole count?",
             feedback=["1 g of $\\mathrm{H_2}$ is 0.5 mol, so only half as many molecules.", "",
                       "44 mol is 44 times more molecules.", "44 g of $\\mathrm{O_2}$ is $44 \\div 32 = 1.375$ mol, which is more than 1 mol. Equal numbers need equal moles, not equal numbers of grams."]),
        TIP("Mole questions are the core of the calculations in Paper 2 and appear in Paper 1 as short numerical items. "
            "Always write the formula first, then the units, then the answer with a unit."),
        PQ("Calculate the mass of 2.5 mol of sodium hydroxide, NaOH.", r"$M = 23 + 16 + 1 = 40$ g/mol. $m = 2.5 \times 40 = 100$ g."),
        PQ(r"How many moles are in 11 g of carbon dioxide?", r"$M = 44$ g/mol. $n = 11 \div 44 = 0.25$ mol."),
        PQ(r"How many atoms are in 0.10 mol of aluminium?", r"$0.10 \times 6.02 \times 10^{23} = 6.02 \times 10^{22}$ atoms."),
        PQ(r"What is the mass of $3.01 \times 10^{23}$ molecules of oxygen gas, $\mathrm{O_2}$?",
           r"$n = (3.01 \times 10^{23}) \div (6.02 \times 10^{23}) = 0.50$ mol. $M = 32$ g/mol. $m = 0.50 \times 32 = 16$ g."),
        SUM("One mole contains $6.02 \\times 10^{23}$ particles (Avogadro's constant).",
            r"Molar mass in g/mol has the same number as $A_r$ or $M_r$.",
            r"$n = m \div M$ and $N = n \times N_A$.",
            "Equal moles mean equal numbers of particles, not equal masses."),
    ],
))

# ------------------------------------------------------------------ 5. Empirical and molecular formulae
LESSONS.append(lesson(
    module=MODULE,
    topic=T4,
    title="Empirical and molecular formulae",
    slug="chb-empirical-molecular-formulae",
    minutes=24,
    summary="Find the empirical formula from masses or percentages by dividing by relative atomic masses, then find the molecular formula from the relative molecular mass.",
    objectives=[
        "Distinguish between an empirical formula and a molecular formula",
        "Find an empirical formula from masses or percentage composition",
        "Deal with ratios such as 1 : 1.5 by multiplying to get whole numbers",
        "Find the molecular formula from the empirical formula and $M_r$",
    ],
    key_concepts=["Empirical formula", "Molecular formula", "Mole ratio", "Percentage composition"],
    blocks=[
        H("Introduction"),
        T("A laboratory technician at the University of Buea analyses a new white powder. The instrument does not give a formula. "
          "It gives the mass or the percentage of each element. The chemist must turn these numbers into a formula. "
          "This is the reverse of the percentage composition calculation you did earlier."),
        D("The **empirical formula** is the formula that shows the simplest whole-number ratio of atoms of each element in a compound.",
          title="Definition: empirical formula"),
        D("The **molecular formula** is the formula that shows the actual number of atoms of each element in one molecule. "
          "It is a whole-number multiple of the empirical formula.", title="Definition: molecular formula"),
        T("Glucose has the molecular formula $\\mathrm{C_6H_{12}O_6}$ and the empirical formula $\\mathrm{CH_2O}$. Ethene, $\\mathrm{C_2H_4}$, has the empirical formula $\\mathrm{CH_2}$. "
          "For ionic compounds such as NaCl the empirical formula is the formula."),
        H("The method"),
        KEY("Five steps for the empirical formula", "Use a table with a column for each element.", cards=[
            ["1. Write the mass of each element", "If you are given percentages, take 100 g of the compound so that % becomes grams."],
            ["2. Divide by $A_r$", "This changes mass into moles of atoms."],
            ["3. Divide by the smallest number", "This gives the ratio, with one element as 1."],
            ["4. Make whole numbers", "If you get 1.5, multiply all by 2. If you get 1.33 or 2.33, multiply all by 3."],
            ["5. Write the formula", "Use the whole numbers as subscripts."],
        ]),
        T("To find the molecular formula, divide the $M_r$ of the compound by the mass of the empirical formula. The answer, $n$, is a whole number. "
          "Multiply every subscript by $n$."),
        F(r"n = \frac{M_r \text{ of the compound}}{\text{mass of the empirical formula}}"),
        H("Worked examples"),
        EX("Worked example 1: from masses", steps=[
            S("Moles of each element", math=r"\text{C: } \frac{2.4}{12} = 0.20 \qquad \text{H: } \frac{0.4}{1} = 0.40"),
            S("Divide by the smallest (0.20)", math=r"\text{C: } 1 \qquad \text{H: } 2"),
            S("Empirical formula", math=r"\mathrm{CH_2}"),
            S("Find $n$", text="The mass of $\\mathrm{CH_2}$ is $12 + 2 = 14$. So $n = 42 \\div 14 = 3$."),
            S("Molecular formula", math=r"\mathrm{C_3H_6}"),
        ], intro=r"A hydrocarbon contains 2.4 g of carbon and 0.4 g of hydrogen. Its $M_r$ is 42. Find its empirical and molecular formulae."),
        EX("Worked example 2: from percentages", steps=[
            S("Take 100 g, so the masses are", text="C 52.2 g, H 13.0 g, O 34.8 g."),
            S("Divide by $A_r$", math=r"\text{C: } \frac{52.2}{12} = 4.35 \quad \text{H: } \frac{13.0}{1} = 13.0 \quad \text{O: } \frac{34.8}{16} = 2.175"),
            S("Divide by the smallest (2.175)", math=r"\text{C: } 2.0 \quad \text{H: } 5.98 \approx 6 \quad \text{O: } 1.0"),
            S("Empirical formula", math=r"\mathrm{C_2H_6O}"),
            S("Molecular formula", text="The mass of $\\mathrm{C_2H_6O}$ is $24 + 6 + 16 = 46$, which equals the given $M_r$. So $n = 1$ and the molecular formula is $\\mathrm{C_2H_6O}$ (ethanol)."),
        ], intro=r"A compound contains 52.2% carbon, 13.0% hydrogen and 34.8% oxygen by mass. Its $M_r$ is 46. Find its formulae."),
        EX("Worked example 3: when the ratio is 1 : 1.5", steps=[
            S("Moles of each element", math=r"\text{Fe: } \frac{5.6}{56} = 0.10 \qquad \text{O: } \frac{2.4}{16} = 0.15"),
            S("Divide by the smallest (0.10)", math=r"\text{Fe: } 1 \qquad \text{O: } 1.5"),
            S("Multiply both by 2 to get whole numbers", math=r"\text{Fe: } 2 \qquad \text{O: } 3"),
            S("Empirical formula", math=r"\mathrm{Fe_2O_3}"),
        ], intro="5.6 g of iron combine with 2.4 g of oxygen. Find the empirical formula of the oxide."),
        EX("Worked example 4: using $M_r$ for a larger molecule", steps=[
            S("Divide by $A_r$", math=r"\text{C: } \frac{92.3}{12} = 7.69 \qquad \text{H: } \frac{7.7}{1} = 7.7"),
            S("Ratio", text="The two numbers are equal, so the ratio is 1 : 1 and the empirical formula is CH."),
            S("Find $n$", text="Mass of CH is 13, so $n = 78 \\div 13 = 6$."),
            S("Molecular formula", math=r"\mathrm{C_6H_6}"),
        ], intro=r"A compound contains 92.3% carbon and 7.7% hydrogen. Its $M_r$ is 78. Find its molecular formula."),
        H("Common mistakes"),
        MISTAKE("Rounding too early", "A ratio of 1 : 1.5 must not be rounded to 1 : 1 or 1 : 2. Multiply by 2. Round only values very close to a whole number, such as 5.98 or 2.02."),
        MISTAKE("Using percentages without taking 100 g", "Write 52.2% as 52.2 g in a 100 g sample before dividing by $A_r$."),
        MISTAKE("Dividing by the atomic number", r"Divide by the relative atomic mass, $A_r$, not by the number of protons."),
        MISTAKE("Giving the empirical formula when the molecular formula is asked", r"Always compare the empirical formula mass with the given $M_r$. If they are equal, $n = 1$."),
        QUIZ("What is the empirical formula of $\\mathrm{C_4H_{10}}$?",
             [r"$\mathrm{CH_2}$", r"$\mathrm{C_2H_5}$", r"$\mathrm{C_4H_{10}}$", r"$\mathrm{CH_3}$"], 1,
             r"Divide both subscripts by their highest common factor, 2: $\mathrm{C_2H_5}$.",
             hint="Divide both subscripts by the same number until they cannot be reduced.",
             feedback=["The ratio of C to H is 4 : 10 = 2 : 5, not 1 : 2.", "",
                       "This is the molecular formula; it can still be simplified.", "The ratio of C to H is 2 : 5, not 1 : 3."]),
        QUIZ("The mole ratio of Mg to N in a compound works out as 1 : 0.67. What should you do next?",
             ["Round to 1 : 1", "Multiply both numbers by 3", "Divide both numbers by 3", "Write the formula as MgN"], 1,
             r"$0.67 \approx 2/3$, so multiply by 3: $3 : 2$, giving $\mathrm{Mg_3N_2}$.",
             hint="A fraction like two thirds needs a multiplier to become whole.",
             feedback=["0.67 is not close to 1; rounding gives the wrong formula.", "",
                       "Dividing would make the numbers smaller and not whole.", "This ignores the 0.67."]),
        TIP("Empirical and molecular formula calculations are typical Paper 2 structured questions and also appear as short Paper 1 items. "
            "Set the working out in a table of mass, $A_r$, moles and ratio so that each step can be marked."),
        PQ(r"A compound contains 40.0% carbon, 6.7% hydrogen and 53.3% oxygen. Find its empirical formula. If $M_r = 180$, find the molecular formula.",
           r"C: $40.0/12 = 3.33$. H: $6.7/1 = 6.7$. O: $53.3/16 = 3.33$. Divide by 3.33: C 1, H 2, O 1. Empirical formula $\mathrm{CH_2O}$ (mass 30). $n = 180/30 = 6$. Molecular formula $\mathrm{C_6H_{12}O_6}$."),
        PQ(r"0.60 g of magnesium combines with 0.40 g of oxygen. Find the empirical formula of magnesium oxide.",
           r"Mg: $0.60/24 = 0.025$. O: $0.40/16 = 0.025$. Ratio 1 : 1. Empirical formula MgO."),
        PQ(r"A hydrocarbon has 85.7% carbon and 14.3% hydrogen and $M_r = 28$. Find its molecular formula.",
           r"C: $85.7/12 = 7.14$. H: $14.3/1 = 14.3$. Ratio 1 : 2, so $\mathrm{CH_2}$ (mass 14). $n = 28/14 = 2$. Molecular formula $\mathrm{C_2H_4}$."),
        PQ(r"A compound has empirical formula $\mathrm{CH_2}$ and $M_r = 56$. Find its molecular formula.",
           r"Mass of $\mathrm{CH_2} = 14$. $n = 56/14 = 4$. Molecular formula $\mathrm{C_4H_8}$."),
        SUM("The empirical formula is the simplest whole-number ratio of atoms; the molecular formula is the actual number.",
            r"Divide the mass (or the percentage, taken as grams in 100 g) of each element by its $A_r$, then divide by the smallest.",
            "Multiply by 2 or 3 if the ratio contains 1.5 or 1.33 so that all numbers are whole.",
            r"$n = M_r \div$ mass of the empirical formula; multiply all subscripts by $n$."),
    ],
))

# ------------------------------------------------------------------ 6. Molar gas volume
LESSONS.append(lesson(
    module=MODULE,
    topic=T5,
    title="Molar gas volume, Avogadro's law and Gay-Lussac's law",
    slug="chb-molar-gas-volume",
    minutes=25,
    summary="Use the molar gas volume (24 dm3 at room temperature, 22.4 dm3 at stp), Avogadro's law and Gay-Lussac's law of combining volumes to solve gas calculations.",
    objectives=[
        "State Avogadro's law and Gay-Lussac's law of combining volumes",
        "Use molar gas volume to convert between moles and gas volume",
        "Use volume ratios from an equation to find volumes of gases that react or form",
        "Convert between cm3 and dm3 and state which molar volume is used",
    ],
    key_concepts=["Avogadro's law", "Molar gas volume", "rtp and stp", "Gay-Lussac's law of combining volumes"],
    blocks=[
        H("Introduction"),
        T("When you pump a bicycle tyre, you push more gas particles into the same space. Gases are easy to measure by volume, so chemists need a way to link "
          "the **volume** of a gas to the **amount** in moles. The key fact is surprising: at the same temperature and pressure, equal volumes of gases have equal numbers of molecules, "
          "whether the gas is light hydrogen or heavy carbon dioxide."),
        D("Equal volumes of all gases, measured at the same temperature and pressure, contain the same number of molecules.", title="Avogadro's law"),
        D("The **molar gas volume** is the volume occupied by one mole of any gas. At room temperature and pressure (**rtp**, about 20 °C and 1 atmosphere) it is **24 dm³**. "
          "At standard temperature and pressure (**stp**, 0 °C and 1 atmosphere) it is **22.4 dm³**.", title="Molar gas volume",
          note="Use 24 dm³ at rtp and 22.4 dm³ at stp. Always read which condition the question states."),
        F(r"n = \frac{V}{24} \quad (V \text{ in dm}^3,\ \text{rtp}) \qquad n = \frac{V}{22.4} \quad (V \text{ in dm}^3,\ \text{stp})"),
        TIP("1 dm³ = 1000 cm³. So $n = V(\\text{cm}^3) \\div 24\\,000$ at rtp. Convert cm³ to dm³ by dividing by 1000."),
        D("When gases react, they do so in volumes that are in a simple whole-number ratio to each other and to the volumes of any gaseous products, "
          "all measured at the same temperature and pressure.", title="Gay-Lussac's law of combining volumes"),
        IMG("f5ch-b-gay-lussac.svg", alt="Bars showing 20 cm3 hydrogen plus 10 cm3 oxygen giving 20 cm3 steam, in the ratio 2 : 1 : 2",
            caption="Figure 1. Volumes of gases in a reaction match the coefficients in the equation (same temperature and pressure)."),
        T("The volume ratio is the same as the mole ratio in the balanced equation. For $\\mathrm{2H_2 + O_2 \\rightarrow 2H_2O}$ the ratio is 2 : 1 : 2, so 20 cm³ of hydrogen needs 10 cm³ of oxygen and gives 20 cm³ of steam. "
          "This works only for gases, and only when all volumes are measured under the same conditions."),
        H("Worked examples"),
        EX("Worked example 1: volume from mass (rtp)", steps=[
            S("Amount of $\\mathrm{CO_2}$", math=r"n = \frac{4.4}{44} = 0.10 \text{ mol}"),
            S("Volume at rtp ($24$ dm³/mol)", math=r"V = 0.10 \times 24 = 2.4 \text{ dm}^3"),
        ], intro=r"Calculate the volume of 4.4 g of carbon dioxide at rtp."),
        EX("Worked example 2: mass from volume (stp)", steps=[
            S("Amount of oxygen at stp", math=r"n = \frac{11.2}{22.4} = 0.50 \text{ mol}"),
            S("Mass", math=r"m = 0.50 \times 32 = 16 \text{ g}"),
        ], intro=r"What is the mass of 11.2 dm³ of oxygen, $\mathrm{O_2}$, at stp? (Use 22.4 dm³/mol.)"),
        EX("Worked example 3: combining volumes", steps=[
            S("Balanced equation", math=r"\mathrm{N_2 + 3H_2 \rightarrow 2NH_3}"),
            S("Volume ratio", text="$\\mathrm{N_2} : \\mathrm{H_2} : \\mathrm{NH_3} = 1 : 3 : 2$."),
            S("Scale up", text="30 cm³ of $\\mathrm{N_2}$ needs $3 \\times 30 = 90$ cm³ of $\\mathrm{H_2}$ and gives $2 \\times 30 = 60$ cm³ of $\\mathrm{NH_3}$."),
        ], intro=r"30 cm³ of nitrogen react completely with hydrogen to form ammonia. What volume of hydrogen is needed and what volume of ammonia forms? (All gases at the same conditions.)"),
        EX("Worked example 4: gas left over", steps=[
            S("Equation", math=r"\mathrm{CH_4(g) + 2O_2(g) \rightarrow CO_2(g) + 2H_2O(l)}"),
            S("Oxygen used", text="10 cm³ of methane needs $2 \\times 10 = 20$ cm³ of oxygen. Oxygen left over: $50 - 20 = 30$ cm³."),
            S("Carbon dioxide formed", text="1 : 1 ratio, so 10 cm³. Water is a liquid at room temperature, so it takes up almost no gas volume."),
            S("Total gas at the end", math=r"10 + 30 = 40 \text{ cm}^3"),
        ], intro=r"10 cm³ of methane are burnt in 50 cm³ of oxygen. After cooling to the starting temperature, what is the total volume of gas?"),
        H("Common mistakes"),
        MISTAKE("Using the wrong molar volume", "Read the conditions. Use 24 dm³ at rtp and 22.4 dm³ at stp. Never mix them in one question."),
        MISTAKE("Forgetting the unit change", "If the volume is in cm³, divide by 1000 to get dm³ before using 24 or 22.4."),
        MISTAKE("Applying gas volumes to solids and liquids", "The molar gas volume works for gases only. 1 mol of water or iron does not occupy 24 dm³."),
        MISTAKE("Assuming equal masses of gases have equal volumes", "Equal volumes have equal numbers of molecules. Because molecules have different masses, equal volumes of different gases have different masses."),
        QUIZ("What is the volume of 0.25 mol of any gas at rtp? (24 dm³/mol)",
             ["0.010 dm³", "6.0 dm³", "96 dm³", "22.4 dm³"], 1,
             r"$V = 0.25 \times 24 = 6.0$ dm³.",
             hint="Multiply the amount by the molar volume.",
             feedback=["You divided $0.25 \\div 24$ instead of multiplying.", "",
                       "You divided 24 by 0.25 instead of multiplying.", "This is the volume of 1 mol at stp, not 0.25 mol at rtp."]),
        QUIZ(r"20 cm³ of $\mathrm{H_2}$ and 20 cm³ of $\mathrm{CO_2}$ are at the same temperature and pressure. Which statement is true?",
             ["The $\\mathrm{CO_2}$ has more molecules because it is heavier", "Both have the same number of molecules",
              "The $\\mathrm{H_2}$ has more molecules because it is lighter", "They have the same mass"], 1,
             r"Avogadro's law: equal volumes at the same temperature and pressure hold equal numbers of molecules.",
             hint="What does Avogadro's law say about volume and number of molecules?",
             feedback=["Mass does not change the number of molecules in a given volume of gas.", "",
                       "Lightness does not change how many molecules fill a given volume.",
                       "The molecules are the same in number but have different masses (2 and 44), so the masses differ."]),
        TIP("Gas volume questions appear in Paper 1 and Paper 2, often with a balanced equation and an experiment (collecting a gas in a syringe or a gas jar). "
            "State the molar volume you use. If the question gives no condition, say which one you are using."),
        PQ(r"Calculate the volume of 0.50 mol of ammonia gas at rtp.", r"$V = 0.50 \times 24 = 12$ dm³."),
        PQ(r"What amount of gas is present in 600 cm³ at rtp?", r"$600 \text{ cm}^3 = 0.600 \text{ dm}^3$. $n = 0.600 \div 24 = 0.025$ mol."),
        PQ(r"5.0 g of calcium carbonate is heated: $\mathrm{CaCO_3 \rightarrow CaO + CO_2}$. What volume of $\mathrm{CO_2}$ forms at stp? (Use 22.4 dm³/mol.)",
           r"$n(\mathrm{CaCO_3}) = 5.0/100 = 0.050$ mol. The mole ratio is 1 : 1, so $n(\mathrm{CO_2}) = 0.050$ mol. $V = 0.050 \times 22.4 = 1.12$ dm³."),
        PQ(r"40 cm³ of carbon monoxide burn in oxygen: $\mathrm{2CO + O_2 \rightarrow 2CO_2}$. What volume of oxygen is needed and what volume of $\mathrm{CO_2}$ forms?",
           r"Ratio 2 : 1 : 2. Oxygen: $40 \div 2 = 20$ cm³. $\mathrm{CO_2}$: 40 cm³."),
        SUM("Avogadro's law: equal volumes of gases at the same temperature and pressure contain equal numbers of molecules.",
            r"Molar gas volume is 24 dm³ at rtp and 22.4 dm³ at stp; $n = V \div$ molar volume, with $V$ in dm³.",
            "Gay-Lussac: gases react in simple whole-number volume ratios, which match the coefficients in the balanced equation.",
            "Convert cm³ to dm³ by dividing by 1000, and use gas volumes for gases only."),
    ],
))

# ------------------------------------------------------------------ 7. Solution concentration
LESSONS.append(lesson(
    module=MODULE,
    topic=T6,
    title="Concentration of solutions: mol/dm³ and g/dm³",
    slug="chb-solution-concentration",
    minutes=24,
    summary="Calculate concentration in mol/dm3 (molarity) and g/dm3, convert between them, find moles and mass in a given volume, and work out simple dilutions.",
    objectives=[
        "Define concentration and give its units, mol/dm³ and g/dm³",
        "Calculate concentration, moles of solute and mass of solute for a given volume",
        "Convert between mol/dm³ and g/dm³ using the molar mass",
        "Calculate the new concentration after dilution",
    ],
    key_concepts=["Solute, solvent and solution", "Concentration", "Molarity", "Mass concentration", "Dilution"],
    blocks=[
        H("Introduction"),
        T("A sachet of oral rehydration salts must be dissolved in exactly the right amount of clean water. Too little water makes the drink too strong; too much makes it too weak. "
          "In chemistry the strength of a solution is its **concentration**: how much solute is dissolved in a fixed volume of the solution."),
        D("A **solute** is the substance that dissolves. A **solvent** is the liquid that dissolves it (usually water). The two together make a **solution**.", title="Solute, solvent, solution"),
        D("The **concentration** of a solution is the amount of solute dissolved in 1 dm³ of solution. "
          "It can be given as an **amount concentration** in mol/dm³ (also called **molarity**, symbol M) or as a **mass concentration** in g/dm³.",
          title="Definition: concentration"),
        KEY("Three formulae to know", "Volume $V$ must be in dm³.", cards=[
            [r"$c = \dfrac{n}{V}$", "Concentration in mol/dm³ = moles ÷ volume in dm³. So $n = c \\times V$."],
            [r"$\text{mass conc.} = c \times M$", "g/dm³ = mol/dm³ × molar mass in g/mol."],
            [r"$1\ \text{dm}^3 = 1000\ \text{cm}^3$", "Divide cm³ by 1000 to get dm³."],
        ]),
        TIP("The volume in the formula is the volume of the **solution**, not the volume of water you started with. "
            "A 0.10 mol/dm³ solution of NaOH means 0.10 mol of NaOH in each 1 dm³ of solution."),
        H("Worked examples"),
        EX("Worked example 1: concentration from mass", steps=[
            S("Molar mass of NaOH", math=r"M = 23 + 16 + 1 = 40 \text{ g/mol}"),
            S("Moles", math=r"n = \frac{4.0}{40} = 0.10 \text{ mol}"),
            S("Volume in dm³", math=r"500 \text{ cm}^3 = 0.500 \text{ dm}^3"),
            S("Concentration", math=r"c = \frac{0.10}{0.500} = 0.20 \text{ mol/dm}^3"),
            S("Mass concentration", math=r"0.20 \times 40 = 8.0 \text{ g/dm}^3"),
        ], intro="4.0 g of sodium hydroxide are dissolved in water to make 500 cm³ of solution. Calculate the concentration in mol/dm³ and in g/dm³."),
        EX("Worked example 2: mass needed", steps=[
            S("Volume in dm³", math=r"250 \text{ cm}^3 = 0.250 \text{ dm}^3"),
            S("Moles needed", math=r"n = c \times V = 0.10 \times 0.250 = 0.025 \text{ mol}"),
            S("Molar mass of $\\mathrm{Na_2CO_3}$", math=r"2(23) + 12 + 3(16) = 106 \text{ g/mol}"),
            S("Mass", math=r"m = 0.025 \times 106 = 2.65 \text{ g}"),
        ], intro=r"What mass of sodium carbonate, $\mathrm{Na_2CO_3}$, is needed to make 250 cm³ of a solution of concentration 0.10 mol/dm³?"),
        EX("Worked example 3: moles in a small volume", steps=[
            S("Volume in dm³", math=r"25.0 \text{ cm}^3 = 0.0250 \text{ dm}^3"),
            S("Moles", math=r"n = 0.20 \times 0.0250 = 0.0050 \text{ mol}"),
        ], intro="How many moles of HCl are in 25.0 cm³ of hydrochloric acid of concentration 0.20 mol/dm³?"),
        EX("Worked example 4: dilution", steps=[
            S("Moles of solute in the first solution", math=r"n = 2.0 \times 0.0250 = 0.050 \text{ mol}"),
            S("Adding water does not change the moles", text="The 0.050 mol is now in 100 cm³ = 0.100 dm³."),
            S("New concentration", math=r"c = \frac{0.050}{0.100} = 0.50 \text{ mol/dm}^3"),
        ], intro="25.0 cm³ of a 2.0 mol/dm³ solution are diluted with water to a total volume of 100 cm³. What is the new concentration?",
           check=r"c_1V_1 = c_2V_2: \ 2.0 \times 25.0 = 0.50 \times 100"),
        EX("Worked example 5: from g/dm³ to mol/dm³", steps=[
            S("Molar mass of $\\mathrm{H_2SO_4}$", math=r"2 + 32 + 64 = 98 \text{ g/mol}"),
            S("Divide by the molar mass", math=r"c = \frac{49}{98} = 0.50 \text{ mol/dm}^3"),
        ], intro=r"A solution of sulfuric acid contains 49 g of $\mathrm{H_2SO_4}$ in each dm³. What is its concentration in mol/dm³?"),
        H("Common mistakes"),
        MISTAKE("Forgetting to convert cm³ to dm³", "A volume of 25.0 cm³ must be written as 0.0250 dm³ before you use $c = n/V$. Otherwise the answer is 1000 times too big."),
        MISTAKE("Mixing mol/dm³ and g/dm³", "A concentration of 8.0 g/dm³ is not 8.0 mol/dm³. Divide by the molar mass to change to mol/dm³."),
        MISTAKE("Using the volume of water, not solution", "If a question gives the final volume of the solution, use that volume."),
        QUIZ("0.50 mol of a solute is dissolved to make 250 cm³ of solution. What is the concentration?",
             ["0.125 mol/dm³", "2.0 mol/dm³", "125 mol/dm³", "0.50 mol/dm³"], 1,
             r"$250 \text{ cm}^3 = 0.250 \text{ dm}^3$. $c = 0.50 \div 0.250 = 2.0$ mol/dm³.",
             hint="Change the volume to dm³ first.",
             feedback=["You multiplied $0.50 \\times 0.250$ instead of dividing.", "",
                       "You multiplied by 250 cm³ instead of dividing by 0.250 dm³.",
                       "You did not take the volume into account."]),
        QUIZ("What mass of NaCl is in 500 cm³ of a 0.20 mol/dm³ solution? (NaCl = 58.5 g/mol)",
             ["5.85 g", "58.5 g", "11.7 g", "0.10 g"], 0,
             r"$n = 0.20 \times 0.500 = 0.10$ mol. $m = 0.10 \times 58.5 = 5.85$ g.",
             hint="First find the moles in 500 cm³, then the mass.",
             feedback=["", "This is the mass of 1 mol, not 0.10 mol.", "This is the mass in 1 dm³ (0.20 mol), not 500 cm³.",
                       "This is the number of moles, not the mass in grams."]),
        TIP("Concentration calculations appear in Paper 2 structured questions and as short numerical items in Paper 1. They lead straight into titration calculations. "
            "Write the unit with every number and always convert cm³ to dm³."),
        PQ(r"2.0 g of sodium hydroxide are dissolved to make 250 cm³ of solution. Calculate the concentration in mol/dm³.",
           r"$n = 2.0 \div 40 = 0.050$ mol. $V = 0.250$ dm³. $c = 0.050 \div 0.250 = 0.20$ mol/dm³."),
        PQ(r"Calculate the mass concentration in g/dm³ of a 0.25 mol/dm³ solution of sulfuric acid, $\mathrm{H_2SO_4}$.",
           r"Mass concentration $= 0.25 \times 98 = 24.5$ g/dm³."),
        PQ(r"50.0 cm³ of a 1.0 mol/dm³ solution are diluted to 250 cm³. What is the new concentration?",
           r"$n = 1.0 \times 0.0500 = 0.050$ mol. $c = 0.050 \div 0.250 = 0.20$ mol/dm³."),
        PQ(r"A solution of magnesium chloride, $\mathrm{MgCl_2}$, has concentration 0.10 mol/dm³. What is the concentration of chloride ions in it?",
           r"Each formula unit $\mathrm{MgCl_2}$ gives 2 chloride ions, so $[\mathrm{Cl^-}] = 2 \times 0.10 = 0.20$ mol/dm³."),
        SUM("Concentration is the amount of solute in 1 dm³ of solution: $c = n \\div V$ in mol/dm³.",
            r"Mass concentration (g/dm³) $= c \times M$.",
            "Always convert cm³ to dm³ by dividing by 1000.",
            r"On dilution the moles of solute stay the same: $c_1V_1 = c_2V_2$."),
    ],
))

# ------------------------------------------------------------------ 8. Reacting masses
LESSONS.append(lesson(
    module=MODULE,
    topic=T7,
    title="Reacting masses and volumes from equations",
    slug="chb-reacting-masses",
    minutes=25,
    summary="Use a balanced equation and the mole ratio to calculate the mass of a product or reactant, or the volume of a gas, from a given mass.",
    objectives=[
        "Explain why a balanced equation gives the mole ratio of reactants and products",
        "Calculate reacting masses in four steps: equation, moles, ratio, answer",
        "Calculate the volume of a gas produced or used in a reaction",
        "Link mass, number of particles, gas volume and solutions through the mole",
    ],
    key_concepts=["Mole ratio", "Reacting mass", "Stoichiometry", "Theoretical amount"],
    blocks=[
        H("Introduction"),
        T("At a lime kiln, limestone (calcium carbonate) is heated to make quicklime for cement and for building. The owner needs to know how much quicklime 1000 kg of limestone will give. "
          "A balanced equation answers this question, because the coefficients are the ratio in **moles**. This is called **stoichiometry**."),
        D("The **mole ratio** is the ratio of the coefficients in a balanced equation. In $\\mathrm{2Mg + O_2 \\rightarrow 2MgO}$ 2 mol of Mg react with 1 mol of $\\mathrm{O_2}$ to form 2 mol of MgO.",
          title="Definition: mole ratio"),
        IMG("f5ch-b-mole-map.svg", alt="Mole map: mass, number of particles, gas volume and solution concentration are all linked through the amount in moles",
            caption="Figure 1. Every quantity connects to the others through moles. (24 dm³/mol at rtp; 22.4 dm³/mol at stp.)"),
        KEY("Four steps for any reacting-mass question", "Never skip step 1.", cards=[
            ["1. Balanced equation", "Write it and check it."],
            ["2. Moles of the known substance", "Use $n = m \\div M$, $n = V \\div 24$ or $n = c \\times V$."],
            ["3. Mole ratio", "Use the coefficients to find moles of the wanted substance."],
            ["4. Convert", "Change moles to mass ($m = n \\times M$) or to gas volume ($V = n \\times 24$)."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: the lime kiln", steps=[
            S("Equation", math=r"\mathrm{CaCO_3 \rightarrow CaO + CO_2}"),
            S("Molar masses", text="$\\mathrm{CaCO_3} = 100$ g/mol and $\\mathrm{CaO} = 40 + 16 = 56$ g/mol."),
            S("Mole ratio is 1 : 1", text="100 g of $\\mathrm{CaCO_3}$ gives 56 g of CaO. The same ratio works in kilograms."),
            S("Scale", math=r"\frac{56}{100} \times 1000 = 560 \text{ kg}"),
        ], intro=r"Calculate the mass of CaO formed when 1000 kg of pure $\mathrm{CaCO_3}$ is heated."),
        EX("Worked example 2: mass of metal to volume of gas", steps=[
            S("Equation", math=r"\mathrm{Mg + 2HCl \rightarrow MgCl_2 + H_2}"),
            S("Moles of Mg", math=r"n = \frac{2.4}{24} = 0.10 \text{ mol}"),
            S("Mole ratio Mg : $\\mathrm{H_2}$ = 1 : 1", text="So 0.10 mol of $\\mathrm{H_2}$ forms."),
            S("Volume of $\\mathrm{H_2}$ at rtp", math=r"V = 0.10 \times 24 = 2.4 \text{ dm}^3"),
            S("Moles of HCl needed (ratio 1 : 2)", math=r"2 \times 0.10 = 0.20 \text{ mol}"),
        ], intro=r"2.4 g of magnesium react completely with dilute hydrochloric acid. Calculate the volume of hydrogen at rtp (24 dm³/mol) and the amount of HCl used."),
        EX("Worked example 3: iron extraction", steps=[
            S("Equation", math=r"\mathrm{Fe_2O_3 + 3CO \rightarrow 2Fe + 3CO_2}"),
            S("Moles of $\\mathrm{Fe_2O_3}$", math=r"n = \frac{80}{160} = 0.50 \text{ mol}"),
            S("Mole ratio $\\mathrm{Fe_2O_3}$ : Fe = 1 : 2", text="So Fe: $2 \\times 0.50 = 1.0$ mol."),
            S("Mass of iron", math=r"m = 1.0 \times 56 = 56 \text{ g}"),
            S("Moles of CO (ratio 1 : 3) and its volume at rtp", math=r"3 \times 0.50 = 1.5 \text{ mol} \quad V = 1.5 \times 24 = 36 \text{ dm}^3"),
        ], intro=r"80 g of iron(III) oxide are reduced by carbon monoxide. Calculate the mass of iron formed and the volume of CO needed at rtp."),
        EX("Worked example 4: precipitation", steps=[
            S("Equation", math=r"\mathrm{AgNO_3 + NaCl \rightarrow AgCl + NaNO_3}"),
            S("Moles of $\\mathrm{AgNO_3}$ ($M = 170$)", math=r"n = \frac{3.4}{170} = 0.020 \text{ mol}"),
            S("Mole ratio 1 : 1, so 0.020 mol of AgCl", text="$M(\\mathrm{AgCl}) = 108 + 35.5 = 143.5$ g/mol."),
            S("Mass of AgCl", math=r"0.020 \times 143.5 = 2.87 \text{ g}"),
        ], intro=r"Excess sodium chloride solution is added to a solution containing 3.4 g of silver nitrate. Calculate the mass of silver chloride precipitate."),
        H("Common mistakes"),
        MISTAKE("Ignoring the mole ratio", "In Example 2 the acid uses 2 mol for every 1 mol of Mg. Do not assume a 1 : 1 ratio; read the coefficients."),
        MISTAKE("Comparing masses directly", "100 g of $\\mathrm{CaCO_3}$ does not give 100 g of CaO. Change to moles, use the ratio, then change back to grams."),
        MISTAKE("Using an unbalanced equation", "A wrong equation gives a wrong ratio. Balance first."),
        QUIZ(r"In $\mathrm{2Mg + O_2 \rightarrow 2MgO}$, what mass of MgO forms when 4.8 g of Mg burns? (Mg 24, O 16)",
             ["4.8 g", "6.4 g", "8.0 g", "16 g"], 2,
             r"$n(\mathrm{Mg}) = 4.8/24 = 0.20$ mol. Ratio 1 : 1, so 0.20 mol MgO. $m = 0.20 \times 40 = 8.0$ g.",
             hint="MgO has molar mass 40 g/mol. How many moles of Mg are there?",
             feedback=["The product is heavier than the magnesium because oxygen joins it; 4.8 g is the mass of magnesium only.", r"This uses the molar mass of $\mathrm{O_2}$ (32): $0.20 \times 32 = 6.4$. The product is MgO, with molar mass 40.", "",
                       "This is 0.40 mol of MgO. The mole ratio Mg : MgO is 1 : 1, so only 0.20 mol forms."]),
        QUIZ(r"In $\mathrm{N_2 + 3H_2 \rightarrow 2NH_3}$, how many moles of $\mathrm{NH_3}$ form from 3 mol of $\mathrm{H_2}$?",
             ["1 mol", "2 mol", "3 mol", "6 mol"], 1,
             r"The ratio $\mathrm{H_2} : \mathrm{NH_3}$ is 3 : 2, so 3 mol of $\mathrm{H_2}$ gives 2 mol of $\mathrm{NH_3}$.",
             hint="Read the coefficients of $\\mathrm{H_2}$ and $\\mathrm{NH_3}$.",
             feedback=["This is the amount of $\\mathrm{N_2}$ that reacts with 3 mol of $\\mathrm{H_2}$, not the $\\mathrm{NH_3}$ formed.", "",
                       "This assumes a 1 : 1 ratio.", "This is double the correct amount."]),
        TIP("Reacting-mass and gas-volume calculations are a main part of the calculation questions in Paper 2, and they are tested in Paper 1 through short numerical items. "
            "Say which molar gas volume you use. Marks are usually given for the balanced equation, the moles and the final answer with a unit."),
        PQ(r"10 g of calcium carbonate react with excess hydrochloric acid: $\mathrm{CaCO_3 + 2HCl \rightarrow CaCl_2 + H_2O + CO_2}$. Calculate the volume of $\mathrm{CO_2}$ at rtp (24 dm³/mol).",
           r"$n(\mathrm{CaCO_3}) = 10/100 = 0.10$ mol. Ratio 1 : 1, so $n(\mathrm{CO_2}) = 0.10$ mol. $V = 0.10 \times 24 = 2.4$ dm³."),
        PQ(r"6.5 g of zinc react with excess acid: $\mathrm{Zn + 2HCl \rightarrow ZnCl_2 + H_2}$. Find the mass of $\mathrm{H_2}$ formed. (Zn 65)",
           r"$n(\mathrm{Zn}) = 6.5/65 = 0.10$ mol. $n(\mathrm{H_2}) = 0.10$ mol. $m = 0.10 \times 2 = 0.20$ g."),
        PQ(r"5.4 g of aluminium burn: $\mathrm{4Al + 3O_2 \rightarrow 2Al_2O_3}$. Calculate the mass of $\mathrm{Al_2O_3}$. (Al 27, O 16)",
           r"$n(\mathrm{Al}) = 5.4/27 = 0.20$ mol. Ratio Al : $\mathrm{Al_2O_3}$ = 4 : 2, so $n = 0.10$ mol. $M = 102$ g/mol. $m = 0.10 \times 102 = 10.2$ g."),
        PQ(r"What mass of HCl reacts with 5.0 g of calcium carbonate in $\mathrm{CaCO_3 + 2HCl \rightarrow CaCl_2 + H_2O + CO_2}$? (HCl = 36.5 g/mol)",
           r"$n(\mathrm{CaCO_3}) = 5.0/100 = 0.050$ mol. $n(\mathrm{HCl}) = 2 \times 0.050 = 0.10$ mol. $m = 0.10 \times 36.5 = 3.65$ g."),
        SUM("A balanced equation gives the mole ratio of the substances.",
            "Four steps: balanced equation, moles of the known substance, mole ratio, convert to mass or volume.",
            "Never compare masses directly; always go through moles.",
            "State the molar gas volume you use: 24 dm³/mol at rtp and 22.4 dm³/mol at stp."),
    ],
))

# ------------------------------------------------------------------ 9. Limiting reagent and percentage yield
LESSONS.append(lesson(
    module=MODULE,
    topic=T7,
    title="Limiting reagents and percentage yield",
    slug="chb-limiting-reagent-yield",
    minutes=24,
    summary="Find the limiting reagent by comparing moles with the mole ratio, calculate the amount of product it gives and work out percentage yield.",
    objectives=[
        "Explain the terms limiting reagent and excess reagent",
        "Find the limiting reagent from the amounts of reactants and the equation",
        "Calculate the product formed and the excess left over",
        "Calculate percentage yield and give reasons why it is below 100%",
    ],
    key_concepts=["Limiting reagent", "Excess reagent", "Theoretical yield", "Actual yield", "Percentage yield"],
    blocks=[
        H("Introduction"),
        T("A tailor in Douala has cloth for 10 shirts, but only 30 buttons. Each shirt needs 6 buttons. The buttons run out after 5 shirts, so the number of buttons decides how many shirts she can finish. "
          "In a reaction the same thing happens. One reactant is used up first and the reaction stops. That reactant is the **limiting reagent**."),
        D("The **limiting reagent** is the reactant that is completely used up first. It decides how much product forms. "
          "A reactant that is left over at the end is in **excess**.", title="Definition: limiting reagent"),
        D("The **theoretical yield** is the mass of product expected from the equation, assuming all the limiting reagent reacts. "
          "The **actual yield** is the mass really obtained.", title="Definition: theoretical and actual yield"),
        F(r"\text{percentage yield} = \frac{\text{actual yield}}{\text{theoretical yield}} \times 100"),
        KEY("How to find the limiting reagent", "Compare moles, not masses.", cards=[
            ["1. Moles of each reactant", "Use $n = m \\div M$."],
            ["2. Divide by the coefficient", "Moles ÷ coefficient in the equation for each reactant."],
            ["3. The smaller value is the limiting reagent", "It runs out first."],
            ["4. Calculate the product from the limiting reagent only", "The excess reagent does not decide the amount of product."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: which reactant runs out?", steps=[
            S("Equation", math=r"\mathrm{Mg + 2HCl \rightarrow MgCl_2 + H_2}"),
            S("Moles of each reactant", math=r"\mathrm{Mg: } \frac{2.4}{24} = 0.10 \text{ mol} \qquad \mathrm{HCl: } \frac{3.65}{36.5} = 0.10 \text{ mol}"),
            S("Divide by the coefficient", text="Mg: $0.10 \\div 1 = 0.10$. HCl: $0.10 \\div 2 = 0.050$. The smaller value is HCl, so **HCl is limiting**."),
            S("Moles of $\\mathrm{H_2}$ from the limiting reagent", text="Ratio HCl : $\\mathrm{H_2}$ = 2 : 1, so $0.10 \\div 2 = 0.050$ mol."),
            S("Volume at rtp (24 dm³/mol)", math=r"0.050 \times 24 = 1.2 \text{ dm}^3"),
            S("Magnesium left over", text="Mg used: 0.050 mol. Left: $0.10 - 0.050 = 0.050$ mol, which is $0.050 \\times 24 = 1.2$ g."),
        ], intro=r"2.4 g of magnesium react with 3.65 g of hydrogen chloride (HCl = 36.5 g/mol). Find the limiting reagent, the volume of hydrogen at rtp and the mass of magnesium left."),
        EX("Worked example 2: hydrogen and oxygen", steps=[
            S("Equation", math=r"\mathrm{2H_2 + O_2 \rightarrow 2H_2O}"),
            S("Moles", math=r"\mathrm{H_2: } \frac{4.0}{2} = 2.0 \text{ mol} \qquad \mathrm{O_2: } \frac{4.0}{32} = 0.125 \text{ mol}"),
            S("Divide by the coefficient", text="$\\mathrm{H_2}$: $2.0 \\div 2 = 1.0$. $\\mathrm{O_2}$: $0.125 \\div 1 = 0.125$. Oxygen is limiting."),
            S("Moles of water", text="Ratio $\\mathrm{O_2} : \\mathrm{H_2O}$ = 1 : 2, so $2 \\times 0.125 = 0.25$ mol."),
            S("Mass of water", math=r"0.25 \times 18 = 4.5 \text{ g}"),
        ], intro=r"4.0 g of hydrogen are mixed with 4.0 g of oxygen and ignited. What mass of water forms?"),
        EX("Worked example 3: percentage yield", steps=[
            S("Equation", math=r"\mathrm{CaCO_3 \rightarrow CaO + CO_2}"),
            S("Theoretical yield", text="10 g is 0.10 mol of $\\mathrm{CaCO_3}$, so 0.10 mol of CaO: $0.10 \\times 56 = 5.6$ g."),
            S("Percentage yield", math=r"\frac{4.2}{5.6} \times 100 = 75\%"),
        ], intro=r"10 g of calcium carbonate are heated. The mass of calcium oxide collected is 4.2 g. Calculate the percentage yield."),
        EX("Worked example 4: using a known yield", steps=[
            S("Theoretical mass of iron", math=r"\frac{112}{160} \times 50 = 35 \text{ g}"),
            S("Actual mass at 80%", math=r"\frac{80}{100} \times 35 = 28 \text{ g}"),
        ], intro=r"In a furnace 50 g of $\mathrm{Fe_2O_3}$ reacts with excess carbon monoxide. The percentage yield of iron is 80%. What mass of iron is obtained? (Fe 56, O 16)"),
        H("Why is the yield below 100%?"),
        T("The yield from a real experiment is almost always less than 100%. Common reasons: some product stays on the filter paper or in the beaker; "
          "the reaction is reversible and does not go to completion; side reactions make other products; or the reactants were not pure. "
          "A percentage yield above 100% means something is wrong, for example the product is still wet or contains impurities."),
        H("Common mistakes"),
        MISTAKE("Comparing masses to find the limiting reagent", "Larger mass does not mean excess. 4.0 g of $\\mathrm{H_2}$ is 2 mol, but 4.0 g of $\\mathrm{O_2}$ is only 0.125 mol. Compare moles divided by the coefficients."),
        MISTAKE("Calculating the product from the excess reagent", "Only the limiting reagent controls how much product forms."),
        MISTAKE("Putting actual yield on the bottom", "Percentage yield is actual ÷ theoretical. It cannot be more than 100% in a correct answer."),
        QUIZ(r"$\mathrm{2Na + Cl_2 \rightarrow 2NaCl}$. 0.40 mol of Na reacts with 0.30 mol of $\mathrm{Cl_2}$. Which is the limiting reagent?",
             ["$\\mathrm{Cl_2}$, because it has fewer moles", "Na, because it needs only 0.20 mol of $\\mathrm{Cl_2}$ and there is more than that",
              "Neither", "$\\mathrm{Cl_2}$, because it is a gas"], 1,
             r"Na: $0.40 \div 2 = 0.20$. $\mathrm{Cl_2}$: $0.30 \div 1 = 0.30$. The smaller value, 0.20, is Na. So Na is limiting and 0.40 mol of NaCl forms.",
             hint="Divide each amount by its coefficient.",
             feedback=["Fewer moles is not enough: you must divide by the coefficient.", "",
                       "The amounts are not in the ratio 2 : 1, so one runs out first.", "The state of a substance does not decide which is limiting."]),
        QUIZ("3.5 g of a product are obtained when the theoretical yield is 5.0 g. What is the percentage yield?",
             ["30%", "70%", "143%", "1.4%"], 1,
             r"$\dfrac{3.5}{5.0} \times 100 = 70\%$.",
             hint="Actual ÷ theoretical × 100.",
             feedback=["30% is the percentage lost, not the percentage obtained.", "",
                       "You divided theoretical by actual. A yield above 100% would not make sense here.", "You did not multiply by 100."]),
        TIP("Limiting reagent and percentage yield questions are standard Paper 2 calculation parts. "
            "Show the moles of both reactants before you decide which is limiting."),
        PQ(r"6.5 g of zinc react with 0.10 mol of HCl: $\mathrm{Zn + 2HCl \rightarrow ZnCl_2 + H_2}$. Which is limiting, and what volume of hydrogen forms at rtp (24 dm³/mol)? (Zn 65)",
           r"Zn: $6.5/65 = 0.10$ mol, divided by 1 = 0.10. HCl: $0.10/2 = 0.050$. HCl is limiting. $n(\mathrm{H_2}) = 0.050$ mol. $V = 0.050 \times 24 = 1.2$ dm³."),
        PQ(r"The theoretical yield of a product is 15 g and 12 g is collected. Calculate the percentage yield.",
           r"$12/15 \times 100 = 80\%$."),
        PQ(r"3.4 g of silver nitrate (170 g/mol) react with 1.17 g of sodium chloride (58.5 g/mol): $\mathrm{AgNO_3 + NaCl \rightarrow AgCl + NaNO_3}$. Calculate the mass of silver chloride formed. (AgCl = 143.5 g/mol)",
           r"$n(\mathrm{AgNO_3}) = 3.4/170 = 0.020$ mol. $n(\mathrm{NaCl}) = 1.17/58.5 = 0.020$ mol. The ratio is 1 : 1, so both are used up and neither is in excess. $n(\mathrm{AgCl}) = 0.020$ mol and $m = 0.020 \times 143.5 = 2.87$ g."),
        PQ("Give two reasons why the actual yield in an experiment is less than the theoretical yield.",
           "Any two of: some product is lost during filtering, washing or transferring; the reaction is reversible so it does not go to completion; side reactions form other products; the reactants are impure."),
        SUM("The limiting reagent is used up first and decides the amount of product; the other reagent is in excess.",
            "Find it by dividing the moles of each reactant by its coefficient: the smaller value is limiting.",
            r"Percentage yield = (actual yield $\div$ theoretical yield) $\times$ 100.",
            "Yields are below 100% because of losses, reversible reactions, side reactions and impurities."),
    ],
))

# ------------------------------------------------------------------ 10. Titration
LESSONS.append(lesson(
    module=MODULE,
    topic=T7,
    title="Volumetric titration calculations",
    slug="chb-titration-calculations",
    minutes=25,
    summary="Describe a titration, find the mean titre and use the equation and the volume and concentration of one solution to find the concentration of the other.",
    objectives=[
        "Describe how a titration is carried out and what end-point means",
        "Calculate the mean titre from concordant results",
        "Calculate the unknown concentration of an acid or an alkali from titration data",
        "Convert the answer to g/dm³ and find the purity of a sample",
    ],
    key_concepts=["Titration", "End-point", "Titre", "Concordant results", "Standard solution"],
    blocks=[
        H("Introduction"),
        T("A water-treatment technician in Yaoundé must check the strength of an acid before using it, and a school laboratory must find the concentration of an unknown alkali. "
          "A **titration** is a careful method that measures exactly how much of one solution reacts with a known volume of another. Then simple mole calculations give the unknown concentration."),
        D("A **titration** is a method of finding the concentration of a solution by adding it slowly from a burette to a known volume of another solution until the reaction is just complete.", title="Definition: titration"),
        D("The **end-point** is the moment the indicator changes colour, showing that the reaction is just complete. "
          "The **titre** is the volume of solution added from the burette to reach the end-point.", title="Definition: end-point and titre"),
        IMG("f5ch-b-titration.svg", alt="Titration apparatus: a burette holding acid is above a conical flask containing 25.0 cm3 of alkali and indicator, standing on a white tile",
            caption="Figure 1. Titration apparatus."),
        KEY("The method", "Follow this order in the practical.", cards=[
            ["1. Measure", "Use a pipette to put 25.0 cm³ of one solution into a conical flask. Add a few drops of indicator."],
            ["2. Fill", "Fill the burette with the other solution and read the starting volume at eye level, at the bottom of the meniscus."],
            ["3. Run in", "Add from the burette, swirling, until the indicator just changes colour. Add drop by drop near the end."],
            ["4. Repeat", "The first run is a rough titration. Repeat until two or three accurate titres agree closely (concordant results). Take the mean of those."],
        ]),
        TIP("Rinsing the conical flask with distilled water does not change the number of moles of solute in it, so it does not matter. "
            "Rinsing the pipette or burette with water would dilute the solution, so rinse them with the solution they will hold."),
        KEY("Calculation steps", "Use the equation for the mole ratio.", cards=[
            ["1. Equation", "Write the balanced equation."],
            ["2. Moles of the known solution", r"$n = c \times V$, with $V$ in dm³ (the mean titre ÷ 1000)."],
            ["3. Mole ratio", "Use the coefficients to find moles of the unknown."],
            ["4. Concentration of the unknown", r"$c = n \div V$, with $V$ = volume in dm³ of that solution."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: 1 : 1 reaction", steps=[
            S("Equation", math=r"\mathrm{HCl + NaOH \rightarrow NaCl + H_2O}"),
            S("Moles of HCl", math=r"n = 0.10 \times \frac{20.0}{1000} = 0.0020 \text{ mol}"),
            S("Mole ratio 1 : 1", text="So 0.0020 mol of NaOH were in the 25.0 cm³."),
            S("Concentration of NaOH", math=r"c = \frac{0.0020}{0.0250} = 0.080 \text{ mol/dm}^3"),
            S("In g/dm³ (NaOH = 40 g/mol)", math=r"0.080 \times 40 = 3.2 \text{ g/dm}^3"),
        ], intro=r"25.0 cm³ of sodium hydroxide solution are neutralized by 20.0 cm³ of 0.10 mol/dm³ hydrochloric acid. Calculate the concentration of the NaOH in mol/dm³ and g/dm³."),
        EX("Worked example 2: 1 : 2 reaction", steps=[
            S("Equation", math=r"\mathrm{H_2SO_4 + 2NaOH \rightarrow Na_2SO_4 + 2H_2O}"),
            S("Moles of NaOH", math=r"n = 0.100 \times \frac{25.0}{1000} = 0.00250 \text{ mol}"),
            S("Mole ratio $\\mathrm{H_2SO_4}$ : NaOH = 1 : 2", math=r"n(\mathrm{H_2SO_4}) = \frac{0.00250}{2} = 0.00125 \text{ mol}"),
            S("Concentration of the acid", math=r"c = \frac{0.00125}{0.0200} = 0.0625 \text{ mol/dm}^3"),
        ], intro=r"25.0 cm³ of 0.100 mol/dm³ sodium hydroxide need 20.0 cm³ of sulfuric acid for neutralization. Calculate the concentration of the acid."),
        EX("Worked example 3: mean titre and sodium carbonate", steps=[
            S("Ignore the rough titre. Use the concordant results", text="20.10, 20.30 and 20.20 cm³ differ by no more than 0.20 cm³."),
            S("Mean titre", math=r"\frac{20.10 + 20.30 + 20.20}{3} = 20.20 \text{ cm}^3"),
            S("Equation", math=r"\mathrm{Na_2CO_3 + 2HCl \rightarrow 2NaCl + H_2O + CO_2}"),
            S("Moles of HCl", math=r"0.100 \times \frac{20.20}{1000} = 0.00202 \text{ mol}"),
            S("Mole ratio $\\mathrm{Na_2CO_3}$ : HCl = 1 : 2", math=r"n(\mathrm{Na_2CO_3}) = \frac{0.00202}{2} = 0.00101 \text{ mol}"),
            S("Concentration", math=r"c = \frac{0.00101}{0.0250} = 0.0404 \text{ mol/dm}^3"),
            S("In g/dm³ ($\\mathrm{Na_2CO_3}$ = 106 g/mol)", math=r"0.0404 \times 106 = 4.28 \text{ g/dm}^3"),
        ], intro=r"In a titration, 25.0 cm³ of sodium carbonate solution were titrated with 0.100 mol/dm³ HCl. The rough titre was 21.80 cm³. The accurate titres were 20.10, 20.30 and 20.20 cm³. Find the concentration of the sodium carbonate in mol/dm³ and g/dm³."),
        TIP("Some books say titres are concordant when they agree within 0.10 cm³, others within 0.20 cm³. Check your textbook and your teacher's instructions."),
        H("Common mistakes"),
        MISTAKE("Using the rough titre", "The rough titre is only a guide. Leave it out when you calculate the mean."),
        MISTAKE("Forgetting the mole ratio", "For $\\mathrm{H_2SO_4}$ with NaOH, one mole of acid reacts with two moles of alkali. Always use the coefficients."),
        MISTAKE("Not converting cm³ to dm³", "A titre of 20.0 cm³ is 0.0200 dm³. If you forget, your answer is 1000 times too large or too small."),
        MISTAKE("Reading the burette from above", "Read at eye level, at the bottom of the meniscus, to avoid reading errors."),
        QUIZ("Which piece of apparatus should be used to measure exactly 25.0 cm³ of the solution into the conical flask?",
             ["A burette", "A pipette", "A beaker", "A measuring cylinder"], 1,
             "A pipette delivers one fixed volume very accurately. A burette is for adding a variable volume, and a beaker or cylinder is less accurate.",
             hint="Which apparatus has a single mark for an accurate fixed volume?",
             feedback=["A burette measures a variable volume and is used to add the second solution.", "",
                       "A beaker has only rough markings.", "A measuring cylinder is not accurate enough for a titration."]),
        QUIZ("25.0 cm³ of NaOH are neutralized by 25.0 cm³ of 0.20 mol/dm³ HCl (a 1 : 1 reaction). What is the concentration of the NaOH?",
             ["0.10 mol/dm³", "0.20 mol/dm³", "0.40 mol/dm³", "1.0 mol/dm³"], 1,
             r"Equal volumes and a 1 : 1 ratio mean equal concentrations: 0.20 mol/dm³.",
             hint="Moles of acid equal moles of alkali. The volumes are the same.",
             feedback=["You halved the concentration; the volumes are equal and the ratio is 1 : 1.", "",
                       "You doubled it; there is no factor 2 in a 1 : 1 reaction.", "This is far too large."]),
        TIP("Titration questions are found in Paper 2, in the Alternative to Practical section. The Board's report notes that some candidates show poor calculation skills there. "
            "Practise writing the equation, the moles of the known solution, the mole ratio and the final concentration with its unit."),
        PQ(r"20.0 cm³ of 0.10 mol/dm³ NaOH are neutralized by 25.0 cm³ of HCl. Calculate the concentration of the HCl.",
           r"$n(\mathrm{NaOH}) = 0.10 \times 0.0200 = 0.0020$ mol. Ratio 1 : 1, so $n(\mathrm{HCl}) = 0.0020$ mol. $c = 0.0020 \div 0.0250 = 0.080$ mol/dm³."),
        PQ(r"25.0 cm³ of 0.050 mol/dm³ sulfuric acid are neutralized by NaOH of concentration 0.10 mol/dm³. What volume of NaOH is needed? ($\mathrm{H_2SO_4 + 2NaOH \rightarrow Na_2SO_4 + 2H_2O}$)",
           r"$n(\mathrm{H_2SO_4}) = 0.050 \times 0.0250 = 0.00125$ mol. $n(\mathrm{NaOH}) = 2 \times 0.00125 = 0.00250$ mol. $V = 0.00250 \div 0.10 = 0.0250$ dm³ $= 25.0$ cm³."),
        PQ(r"The 0.080 mol/dm³ solution of NaOH in Worked example 1 has molar mass 40 g/mol. Give its concentration in g/dm³.",
           r"$0.080 \times 40 = 3.2$ g/dm³."),
        PQ(r"2.0 g of impure sodium hydroxide were dissolved in water and made up to 250 cm³. 25.0 cm³ of this solution needed 22.5 cm³ of 0.10 mol/dm³ HCl. Calculate the percentage of NaOH in the sample. (NaOH = 40 g/mol)",
           r"$n(\mathrm{HCl}) = 0.10 \times 0.0225 = 0.00225$ mol, so $n(\mathrm{NaOH})$ in 25.0 cm³ is 0.00225 mol. In 250 cm³: $0.0225$ mol. Mass $= 0.0225 \times 40 = 0.90$ g. Percentage $= 0.90/2.0 \times 100 = 45\%$."),
        SUM("A titration measures the volume of one solution that reacts exactly with a known volume of another; the end-point is shown by an indicator.",
            "Use a pipette for the fixed volume and a burette for the titre; take the mean of concordant titres and ignore the rough one.",
            "Calculate: equation, moles of the known solution ($c \\times V$), mole ratio, then $c = n \\div V$ for the unknown.",
            "Convert all volumes to dm³ and use the molar mass to change mol/dm³ into g/dm³."),
    ],
))

