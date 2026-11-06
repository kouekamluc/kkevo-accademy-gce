"""Form 5 Chemistry: Acids, Bases, Salts & Redox; Energetics, Kinetics & Equilibria (13 lessons, one practice set each).

Draft content: check against the official syllabus and your textbook. Numbers were verified by script.
"""

from .dsl import *  # noqa: F403

COURSE = ("chemistry", "form-5")

M3 = "Acids, Bases, Salts & Redox"
M4 = "Energetics, Kinetics & Equilibria"

LESSONS = []

# ------------------------------------------------------------------ 1. Acids, bases and electrolytes
LESSONS.append(lesson(
    module=M3,
    topic="Acids, bases and electrolytes",
    title="Acids, bases and strong and weak electrolytes",
    slug="chc-acids-bases-electrolytes",
    minutes=22,
    summary="The Arrhenius and Bronsted-Lowry definitions of acids and bases, conjugate pairs, alkalis, and the difference between strong and weak acids, bases and electrolytes.",
    objectives=[
        "State the Arrhenius definitions of an acid and a base",
        "Use the Bronsted-Lowry idea of proton donors and proton acceptors, and name conjugate acid-base pairs",
        "Explain the difference between strong and weak acids and bases in terms of ionization",
        "Distinguish strong, weak and non-electrolytes and give examples",
    ],
    key_concepts=["Arrhenius acid", "Arrhenius base", "Alkali", "Bronsted-Lowry acid", "Bronsted-Lowry base",
                  "Conjugate pair", "Ionization", "Strong electrolyte", "Weak electrolyte"],
    blocks=[
        H("Introduction"),
        T("In a Cameroonian kitchen you meet acids and bases every day. Lemon and tomato taste sour because they contain acids. "
          "Soap and wood-ash water feel slippery because they are alkaline. Car-battery liquid is a strong acid and can burn the skin. "
          "Vinegar is also an acid, yet we eat it on salad. So what exactly makes something an acid, and why are some acids dangerous while others are safe?"),
        T("In this lesson you learn two scientific definitions of acids and bases, and the idea of **strong** and **weak**. "
          "These ideas come back in pH, salt preparation and equilibrium."),
        H("Arrhenius acids and bases"),
        D("An **Arrhenius acid** is a substance that produces hydrogen ions, $\\mathrm{H^+}$, when it dissolves in water. "
          "An **Arrhenius base** is a substance that produces hydroxide ions, $\\mathrm{OH^-}$, in water.", title="Arrhenius definitions"),
        CODE("HCl(g)  --water-->  H+(aq) + Cl-(aq)        acid: gives H+\n"
             "NaOH(s) --water-->  Na+(aq) + OH-(aq)      base: gives OH-", "text", title="Two examples"),
        D("An **alkali** is a base that dissolves in water. Sodium hydroxide, potassium hydroxide and ammonia solution are alkalis. "
          "Copper(II) oxide is a base but not an alkali, because it does not dissolve.", title="Alkali"),
        T("Note that a free $\\mathrm{H^+}$ ion is just a proton and does not stay alone. In water it joins a water molecule to make the "
          "**oxonium ion**, $\\mathrm{H_3O^+}$. Many books still write $\\mathrm{H^+(aq)}$ as a short form."),
        H("Bronsted-Lowry acids and bases"),
        T("The Arrhenius idea works only in water. Bronsted and Lowry gave a wider idea based on the **proton**, which is a hydrogen ion."),
        D("A **Bronsted-Lowry acid** is a proton donor. A **Bronsted-Lowry base** is a proton acceptor.", title="Bronsted-Lowry definitions"),
        CODE("HCl + NH3  ->  NH4+ + Cl-\n"
             "HCl gives a proton (acid).  NH3 receives it (base).", "text", title="Proton transfer"),
        T("In this reaction no water is needed, so the Arrhenius idea cannot explain it. The Bronsted-Lowry idea can."),
        D("When an acid gives away a proton, what is left is its **conjugate base**. When a base accepts a proton, it becomes its "
          "**conjugate acid**. An acid and its conjugate base differ by one proton: a **conjugate pair**.", title="Conjugate pairs"),
        CODE("NH3 + H2O  <->  NH4+ + OH-\n"
             "base 1  acid 2   acid 1  base 2\n"
             "Pairs: NH3 / NH4+   and   H2O / OH-", "text", title="Ammonia in water"),
        TIP("Water can act as an acid or as a base, depending on its partner. With HCl it accepts a proton (base). With ammonia it gives a proton (acid)."),
        H("Strong and weak"),
        D("A **strong acid** ionizes almost completely in water. A **weak acid** ionizes only slightly, so most of its molecules stay whole. "
          "The same idea applies to bases.", title="Strong and weak"),
        KEY("Examples to learn", "Strength is about how much a substance ionizes. It is not about concentration.", cards=[
            ["Strong acids", "Hydrochloric acid HCl, sulfuric acid H2SO4, nitric acid HNO3."],
            ["Weak acids", "Ethanoic acid CH3COOH (in vinegar), carbonic acid H2CO3, citric acid (in lemon)."],
            ["Strong bases (alkalis)", "Sodium hydroxide NaOH, potassium hydroxide KOH."],
            ["Weak base", "Ammonia solution NH3. Many metal hydroxides are only slightly soluble."],
        ]),
        CODE("Strong:  HCl  ->  H+ + Cl-                  (one-way arrow, nearly all ionized)\n"
             "Weak:    CH3COOH <-> H+ + CH3COO-           (double arrow, only a few ionized)", "text", title="Two arrows"),
        H("Electrolytes"),
        D("An **electrolyte** is a substance that conducts electricity when molten or in solution because it contains free ions. "
          "A **strong electrolyte** is almost completely ionized. A **weak electrolyte** is only slightly ionized. "
          "A **non-electrolyte** has no ions and does not conduct.", title="Electrolytes"),
        KEY("Three kinds", "Conductivity depends on how many ions are free to move.", cards=[
            ["Strong electrolytes", "HCl(aq), NaOH(aq), NaCl(aq). The bulb shines brightly."],
            ["Weak electrolytes", "CH3COOH(aq), NH3(aq). The bulb glows dimly."],
            ["Non-electrolytes", "Sugar solution, ethanol, pure water. The bulb does not light."],
        ]),
        EX("Worked example 1: conjugate pairs", intro="In the reaction $\\mathrm{HNO_3 + H_2O \\rightarrow H_3O^+ + NO_3^-}$, identify the acid, the base and the conjugate pairs.", steps=[
            S("Find who gives the proton", text="HNO3 loses H+ and becomes NO3-. So HNO3 is the acid."),
            S("Find who receives the proton", text="H2O gains H+ and becomes H3O+. So H2O is the base."),
            S("Write the pairs", text="HNO3 / NO3- is one pair. H2O / H3O+ is the other pair."),
        ]),
        EX("Worked example 2: comparing two acids", intro="Hydrochloric acid and ethanoic acid both have concentration 0.1 mol per dm3. Which conducts better, and why?", steps=[
            S("Compare ionization", text="HCl is strong, so almost every molecule gives H+ and Cl-. Ethanoic acid is weak, so only a few molecules ionize."),
            S("Link to conductivity", text="More ions free to move means better conduction. So HCl(aq) is the better conductor."),
            S("Link to concentration", text="They have the same concentration, so the difference is only due to strength."),
        ]),
        MISTAKE("Strong does not mean concentrated", "Strength is how far a substance ionizes. Concentration is how much substance is dissolved. "
                "You can have a dilute strong acid or a concentrated weak acid."),
        MISTAKE("Calling every base an alkali", "Only a base that dissolves in water is an alkali. Copper(II) oxide and magnesium oxide are bases but not alkalis."),
        QUIZ("In the reaction $\\mathrm{NH_3 + HCl \\rightarrow NH_4^+ + Cl^-}$, what does NH3 do?",
             ["It donates a proton", "It accepts a proton", "It donates a hydroxide ion", "It accepts an electron"], 1,
             "NH3 gains H+ to become NH4+, so it is a proton acceptor, which is a Bronsted-Lowry base.",
             hint="Compare the H atoms in NH3 and in NH4+.",
             feedback=["If NH3 donated a proton it would lose hydrogen, but it gains one.", "",
                       "No OH- is transferred in this reaction.", "Electron transfer is redox, not acid-base."]),
        QUIZ("Which solution is the best conductor of electricity, if all have the same concentration?",
             ["Sugar solution", "Ethanoic acid", "Ammonia solution", "Sodium hydroxide solution"], 3,
             "NaOH is a strong electrolyte, completely ionized. It has the most free ions.",
             hint="Look for a strong electrolyte.",
             feedback=["Sugar is a non-electrolyte.", "Ethanoic acid is weak and little ionized.", "Ammonia is a weak base, little ionized.", ""]),
        TIP("Exam link: definitions, conjugate pairs and strong versus weak appear in Paper 1 multiple choice and in the structured questions of Paper 2. "
            "Write definitions in full: a Bronsted-Lowry acid is a proton donor.", title="Exam link"),
        PQ("Define a Bronsted-Lowry acid and give one example of a reaction in which water acts as an acid.",
           "A Bronsted-Lowry acid is a proton donor. In $\\mathrm{NH_3 + H_2O \\rightleftharpoons NH_4^+ + OH^-}$, water gives a proton to ammonia, so water is the acid."),
        PQ("Explain why ethanoic acid is called a weak acid although it can be concentrated.",
           "A weak acid ionizes only slightly in water, so most molecules stay as CH3COOH. Strength depends on the extent of ionization, not on the amount dissolved."),
        PQ("Write the conjugate base of $\\mathrm{H_2SO_4}$ and of $\\mathrm{H_2O}$ (as an acid).",
           "Remove one proton: $\\mathrm{H_2SO_4}$ gives $\\mathrm{HSO_4^-}$, and $\\mathrm{H_2O}$ gives $\\mathrm{OH^-}$."),
        PQ("A student tests three solutions with a bulb: one is bright, one is dim, one does not light. Suggest one possible substance for each.",
           "Bright: HCl or NaOH solution (strong electrolytes). Dim: ethanoic acid or ammonia solution (weak electrolytes). No light: sugar solution (non-electrolyte)."),
        SUM("An Arrhenius acid gives H+ in water; an Arrhenius base gives OH- in water; an alkali is a soluble base.",
            "A Bronsted-Lowry acid donates a proton; a base accepts a proton. An acid and its conjugate base differ by one proton.",
            "Strong acids and bases are almost completely ionized; weak ones only slightly. Strength is not concentration.",
            "Strong electrolytes have many free ions and conduct well; weak ones conduct poorly; non-electrolytes do not conduct.",
            "In Paper 1, expect questions on conjugate pairs and on comparing conductivity or strength."),
    ],
))

# ------------------------------------------------------------------ 2. pH, indicators and neutralization
LESSONS.append(lesson(
    module=M3,
    topic="The pH scale, indicators and neutralization",
    title="pH, indicators and neutralization",
    slug="chc-ph-indicators-neutralization",
    minutes=24,
    summary="The pH scale from 0 to 14, calculating pH from the hydrogen ion concentration, common indicators and their colours, and neutralization reactions with their ionic equation and everyday uses.",
    objectives=[
        "Describe the pH scale and relate pH to acidity and alkalinity",
        "Calculate the pH of a strong acid or strong alkali from its concentration",
        "Name the colours of litmus, methyl orange, phenolphthalein and universal indicator in acid and alkali",
        "Write word, full and ionic equations for neutralization and give everyday uses",
    ],
    key_concepts=["pH", "Indicator", "Universal indicator", "Neutralization", "Salt", "Ionic equation"],
    blocks=[
        H("Introduction"),
        T("A farmer near Buea notices that maize grows badly in one field. A simple test shows that the soil is too acidic. "
          "She spreads wood ash or agricultural lime on the soil. The soil improves because an alkali **neutralizes** the extra acid. "
          "To know how acidic the soil is, chemists use a number called **pH**."),
        H("The pH scale"),
        D("The **pH** is a number that tells how acidic or alkaline a solution is. A neutral solution has pH 7 at 25 degrees C. "
          "Acids have pH less than 7. Alkalis have pH greater than 7. The usual scale runs from 0 to 14.", title="pH"),
        IMG("f5ch-c-ph-scale.svg", alt="pH scale from 0 to 14 coloured red to violet, with examples of common substances",
            caption="Figure 1. The pH scale. Universal indicator turns red in strong acid, green at pH 7 and violet in strong alkali."),
        T("The scale is **logarithmic**. A solution of pH 3 has ten times more hydrogen ions than a solution of pH 4. "
          "A solution of pH 2 has one hundred times more hydrogen ions than a solution of pH 4."),
        D("For a solution, $\\mathrm{pH} = -\\log_{10}[\\mathrm{H^+}]$, where $[\\mathrm{H^+}]$ is the concentration of hydrogen ions in mol per dm3.",
          title="Calculating pH", formula=r"\mathrm{pH} = -\log_{10}[\mathrm{H^+}]"),
        D("In water at 25 degrees C, $[\\mathrm{H^+}] \\times [\\mathrm{OH^-}] = 1 \\times 10^{-14}$. So for an alkali, find $[\\mathrm{OH^-}]$, then "
          "$\\mathrm{pOH} = -\\log_{10}[\\mathrm{OH^-}]$ and $\\mathrm{pH} = 14 - \\mathrm{pOH}$.", title="Alkalis", formula=r"\mathrm{pH} + \mathrm{pOH} = 14"),
        EX("Worked example 1: pH of a strong acid", intro="Find the pH of 0.020 mol per dm3 hydrochloric acid.", steps=[
            S("HCl is strong, so it ionizes completely", text="$[\\mathrm{H^+}]$ equals the acid concentration."),
            S("Write the value", math=r"[\mathrm{H^+}] = 0.020 = 2.0 \times 10^{-2}\ \mathrm{mol/dm^3}"),
            S("Apply the formula", math=r"\mathrm{pH} = -\log_{10}(0.020) = 1.70"),
        ], check=r"10^{-1.70} = 0.020"),
        EX("Worked example 2: pH of a strong alkali", intro="Find the pH of 0.0050 mol per dm3 sodium hydroxide at 25 degrees C.", steps=[
            S("NaOH is strong, so $[\\mathrm{OH^-}]$ equals the concentration", math=r"[\mathrm{OH^-}] = 0.0050"),
            S("Find pOH", math=r"\mathrm{pOH} = -\log_{10}(0.0050) = 2.30"),
            S("Find pH", math=r"\mathrm{pH} = 14 - 2.30 = 11.70"),
        ]),
        TIP("When the concentration is an exact power of ten, such as 0.001, the pH is just the power: $0.001 = 10^{-3}$, so the pH is 3."),
        H("Indicators"),
        D("An **indicator** is a substance that changes colour depending on the acidity of a solution. "
          "**Universal indicator** is a mixture that gives a range of colours and so shows the pH.", title="Indicator"),
        CODE("Indicator            In acid          In alkali\n"
             "Litmus               red              blue\n"
             "Methyl orange        red              yellow\n"
             "Phenolphthalein      colourless       pink\n"
             "Universal indicator  red/orange       blue/violet (green at pH 7)", "text", title="Common indicators"),
        MISTAKE("Mixing up the colours", "Litmus: red in acid, blue in alkali. Phenolphthalein is the opposite way round from what many expect: colourless in acid, pink in alkali. "
                "Methyl orange is red in acid and yellow in alkali."),
        H("Neutralization"),
        D("**Neutralization** is the reaction of an acid with a base to form a salt and water only.", title="Neutralization"),
        CODE("acid + alkali          ->  salt + water\n"
             "acid + metal oxide    ->  salt + water\n"
             "acid + metal carbonate ->  salt + water + carbon dioxide\n\n"
             "HCl + NaOH        ->  NaCl + H2O\n"
             "2NaOH + H2SO4     ->  Na2SO4 + 2H2O\n"
             "CaCO3 + 2HCl      ->  CaCl2 + H2O + CO2", "text", title="General and specific equations"),
        T("Look at the ions. In $\\mathrm{HCl + NaOH}$, the ions $\\mathrm{Na^+}$ and $\\mathrm{Cl^-}$ do not change. They are **spectator ions**. "
          "Only $\\mathrm{H^+}$ and $\\mathrm{OH^-}$ react. This is true for every strong acid and strong alkali."),
        D("The **ionic equation for neutralization** is $\\mathrm{H^+(aq) + OH^-(aq) \\rightarrow H_2O(l)}$.", title="Ionic equation",
          formula=r"\mathrm{H^+(aq) + OH^-(aq) \rightarrow H_2O(l)}"),
        KEY("Uses of neutralization", "Everyday uses all rely on adding a base to an acid or the reverse.", cards=[
            ["Farming", "Lime or wood ash is spread on acidic soil to raise its pH."],
            ["Indigestion", "Antacid tablets contain bases such as magnesium hydroxide to neutralize extra stomach acid."],
            ["Factory waste", "Acidic waste water is treated with lime before it is released into rivers."],
            ["Toothpaste", "Toothpaste is mildly alkaline and neutralizes acids made by bacteria on teeth."],
        ]),
        EX("Worked example 3: dilution and pH", intro="10 cm3 of a strong acid of pH 2 is diluted with water to 100 cm3. Find the new pH.", steps=[
            S("Find the dilution factor", text="100 cm3 divided by 10 cm3 gives a factor of 10."),
            S("Find the new concentration", math=r"[\mathrm{H^+}] = 10^{-2} \div 10 = 10^{-3}\ \mathrm{mol/dm^3}"),
            S("Find the pH", math=r"\mathrm{pH} = 3"),
        ]),
        QUIZ("Solution X has pH 3 and solution Y has pH 5. Which statement is correct?",
             ["Y has 2 times more H+ ions than X", "X has 100 times more H+ ions than Y", "X is less acidic than Y", "X has 10 times more H+ ions than Y"], 1,
             "Each pH unit is a factor of 10. Two units give $10 \\times 10 = 100$. X has the lower pH, so it has the higher H+ concentration.",
             hint="Count how many pH units separate 3 and 5.",
             feedback=["The relationship is not additive but a factor of 10 per unit, and X is the one with more.", "",
                       "A lower pH means more acidic, so X is the more acidic.", "That would be a difference of one pH unit, not two."]),
        QUIZ("A few drops of phenolphthalein are added to a solution and it turns pink. The solution is...",
             ["acidic", "neutral", "alkaline", "a salt solution of pH 1"], 2,
             "Phenolphthalein is pink in alkali.", hint="Think of pink as the alkali colour for this indicator.",
             feedback=["In acid it stays colourless.", "In neutral solution it stays colourless.", "", "At pH 1 it would be colourless."]),
        TIP("Exam link: pH, indicator colours and neutralization appear in Paper 1 multiple choice and in Paper 2 structured questions, including the alternative to practical section. "
            "When you are asked for an equation, balance it and give state symbols if asked.", title="Exam link"),
        PQ("Calculate the pH of 0.0010 mol per dm3 nitric acid (a strong acid).", "$[\\mathrm{H^+}] = 0.0010 = 10^{-3}$, so $\\mathrm{pH} = 3$."),
        PQ("Write the balanced equation for the neutralization of sulfuric acid by potassium hydroxide.",
           "$\\mathrm{H_2SO_4 + 2KOH \\rightarrow K_2SO_4 + 2H_2O}$."),
        PQ("Calculate the pH of 0.10 mol per dm3 NaOH at 25 degrees C.",
           "$[\\mathrm{OH^-}] = 0.10$, so $\\mathrm{pOH} = 1$ and $\\mathrm{pH} = 14 - 1 = 13$."),
        PQ("A farmer's soil has pH 5. Name a substance to add and explain how it helps.",
           "Add lime (calcium oxide or calcium hydroxide) or wood ash. It is a base. It reacts with the acid in the soil by neutralization, so the pH rises towards 7."),
        SUM("pH measures acidity: below 7 acid, 7 neutral, above 7 alkaline. Each unit is a factor of 10.",
            "For a strong acid, $\\mathrm{pH} = -\\log_{10}[\\mathrm{H^+}]$. For a strong alkali, find pOH first and subtract from 14.",
            "Litmus: red/blue. Methyl orange: red/yellow. Phenolphthalein: colourless/pink. Universal indicator gives the full colour range.",
            "Neutralization: acid + base gives a salt and water. The ionic equation is $\\mathrm{H^+ + OH^- \\rightarrow H_2O}$.",
            "Neutralization is used in farming, in medicine, in industry and in toothpaste."),
    ],
))

# ------------------------------------------------------------------ 3. Preparing soluble salts
LESSONS.append(lesson(
    module=M3,
    topic="Preparation of salts and solubility",
    title="Preparing soluble salts",
    slug="chc-preparing-soluble-salts",
    minutes=24,
    summary="How to choose a method for a soluble salt: acid with a reactive metal, an insoluble base or a carbonate, or titration for sodium, potassium and ammonium salts, with the steps, equations and percentage yield.",
    objectives=[
        "Define a salt and state the three common routes to a soluble salt",
        "Choose the correct method for a given salt using the flowchart",
        "Describe the practical steps: react, filter, evaporate, crystallise, dry",
        "Calculate the theoretical mass and the percentage yield of a salt",
    ],
    key_concepts=["Salt", "Excess", "Filtrate", "Crystallization", "Titration method", "Percentage yield"],
    blocks=[
        H("Introduction"),
        T("Salt is not only the white powder in the kitchen. In chemistry, a **salt** is a compound formed when the hydrogen of an acid is replaced by a metal or by the ammonium ion. "
          "Common table salt, sodium chloride, is one example. Others are copper(II) sulfate, used in blue crystals to spray cocoa farms against fungus, and potassium nitrate, used in fertilizers."),
        T("Many salts are made in the laboratory. The method depends on whether the salt is soluble or insoluble in water, and on the substances available. "
          "In this lesson you learn the methods for **soluble** salts. The next lesson covers insoluble salts."),
        D("A **salt** is an ionic compound made when the hydrogen ions of an acid are replaced by metal ions or by ammonium ions.", title="Salt"),
        KEY("Names of salts", "The first part of the name comes from the base or metal. The second part comes from the acid.", cards=[
            ["Hydrochloric acid", "gives chlorides, for example zinc chloride"],
            ["Sulfuric acid", "gives sulfates, for example copper(II) sulfate"],
            ["Nitric acid", "gives nitrates, for example magnesium nitrate"],
            ["Ethanoic acid", "gives ethanoates, for example sodium ethanoate"],
        ]),
        H("Choosing a method"),
        IMG("f5ch-c-salt-flow-soluble.svg", alt="Flowchart: salts of sodium, potassium or ammonium are made by titration; other soluble salts by adding an excess of a solid to the acid, then filtering",
            caption="Figure 1. Choosing a method for a soluble salt."),
        T("Sodium, potassium and ammonium bases are all **soluble**. You cannot add an \"excess\" of a dissolved alkali and filter it away. So these salts are made by **titration**. "
          "Other soluble salts are made by adding an excess of an insoluble solid to the acid."),
        H("Method 1: acid with an insoluble solid in excess"),
        D("The solid can be a **reactive metal** (such as magnesium or zinc), a **metal oxide or hydroxide** (such as copper(II) oxide), or a **carbonate** (such as copper(II) carbonate).", title="Three solids"),
        CODE("Zn      + H2SO4  ->  ZnSO4  + H2              metal gives hydrogen\n"
             "CuO     + H2SO4  ->  CuSO4  + H2O             oxide gives water\n"
             "CuCO3   + H2SO4  ->  CuSO4  + H2O + CO2       carbonate gives water and CO2", "text", title="Three reactions"),
        T("Follow these steps."),
        T("1. Warm a fixed volume of dilute acid in a beaker.\n\n2. Add the solid a little at a time, stirring. Keep adding until no more reacts. Some solid is left at the bottom. This is the **excess**. "
          "Using excess makes sure that all the acid has reacted."),
        T("3. **Filter** to remove the excess solid. The solution that passes through is the **filtrate**.\n\n4. Heat the filtrate gently to evaporate some water until it is **saturated**. "
          "You can test by dipping a glass rod in and seeing crystals form as it cools.\n\n5. Leave the solution to cool slowly. Crystals form. Filter them, wash with a little cold distilled water and dry between filter papers."),
        MISTAKE("Evaporating to dryness", "Do not heat until all the water has gone. Many salts hold water in their crystals and would be damaged, and impurities would be left in the solid. Stop when the solution is saturated and let crystals grow on cooling."),
        TIP("Why do copper and dilute acid not give copper(II) sulfate? Copper is below hydrogen in the reactivity series, so it does not react with dilute acids. Use copper(II) oxide or carbonate instead. Sodium and potassium are too violent with acid, so use titration."),
        H("Method 2: titration for sodium, potassium and ammonium salts"),
        T("To make sodium sulfate, you react sodium hydroxide solution with sulfuric acid. Both are solutions, so you must add exact amounts."),
        T("1. Use a pipette to put 25.0 cm3 of the alkali in a flask and add a few drops of an indicator such as methyl orange.\n\n2. Add the acid from a burette until the indicator just changes colour. Note the volume.\n\n"
          "3. Repeat with the same volumes but **no indicator**, because the indicator would contaminate the salt. 4. Evaporate the solution to the crystallization point, cool, filter and dry the crystals."),
        CODE("2NaOH + H2SO4  ->  Na2SO4 + 2H2O\n"
             "KOH  + HNO3   ->  KNO3  + H2O\n"
             "NH3  + HCl    ->  NH4Cl", "text", title="Examples made by titration"),
        H("Percentage yield"),
        D("The **percentage yield** compares what you actually collected with the greatest mass the equation allows.", title="Percentage yield",
          formula=r"\text{percentage yield} = \frac{\text{actual mass}}{\text{theoretical mass}} \times 100"),
        EX("Worked example 1: copper(II) sulfate crystals",
           intro="4.0 g of copper(II) oxide is reacted with excess dilute sulfuric acid. After crystallization, 9.4 g of copper(II) sulfate-5-water, $\\mathrm{CuSO_4 \\cdot 5H_2O}$, is collected. Find the percentage yield. ($A_r$: Cu = 63.5, O = 16, S = 32, H = 1.)",
           steps=[
               S("Write the equation", math=r"\mathrm{CuO + H_2SO_4 \rightarrow CuSO_4 + H_2O}"),
               S("Moles of CuO", math=r"M_r = 63.5 + 16 = 79.5,\quad n = \frac{4.0}{79.5} = 0.0503\ \mathrm{mol}"),
               S("The mole ratio is 1 : 1, then hydrated crystals form", text="So 0.0503 mol of $\\mathrm{CuSO_4 \\cdot 5H_2O}$ is possible."),
               S("Theoretical mass", math=r"M_r = 159.5 + 90 = 249.5,\quad m = 0.0503 \times 249.5 = 12.55\ \mathrm{g}"),
               S("Percentage yield", math=r"\frac{9.4}{12.55} \times 100 = 74.9\% \approx 75\%"),
           ]),
        EX("Worked example 2: choose the method", intro="Suggest how to make (a) magnesium sulfate, (b) potassium sulfate, (c) copper(II) chloride.", steps=[
            S("(a) Magnesium is a reactive metal", text="Add excess magnesium (or magnesium oxide or carbonate) to dilute sulfuric acid, filter, crystallise."),
            S("(b) Potassium salts need titration", text="React potassium hydroxide solution with dilute sulfuric acid by titration, then evaporate and crystallise."),
            S("(c) Copper does not react with acid", text="Add excess copper(II) oxide or carbonate to dilute hydrochloric acid, filter, evaporate and crystallise."),
        ]),
        QUIZ("Why is an excess of the insoluble solid added to the acid?",
             ["To make the reaction faster", "To make sure all the acid has reacted", "To make the salt insoluble", "To make the crystals larger"], 1,
             "Excess solid means that every acid particle has reacted. The unreacted solid is then removed by filtration, so the salt is not contaminated with acid.",
             hint="What would be left in the solution if you had too little solid?",
             feedback=["Excess changes the amount, not the speed in a useful way.", "", "The salt is soluble and stays in solution.", "Crystal size depends on how it cools."]),
        QUIZ("Which pair of reactants can be used to prepare sodium nitrate?",
             ["Sodium and nitric acid in excess", "Sodium hydroxide solution and dilute nitric acid by titration", "Sodium oxide in excess and nitric acid", "Sodium carbonate in excess, filtered"], 1,
             "Sodium compounds are soluble. You cannot filter an excess, so you use titration with a pipette and burette.",
             hint="Remember the flowchart: Na, K or NH4.",
             feedback=["Sodium is too reactive with acid: the reaction is dangerous.", "", "Sodium oxide dissolves, so it cannot be filtered off as an excess.", "Sodium carbonate dissolves, so no excess can be filtered off."]),
        TIP("Exam link: the preparation of salts is tested in Paper 1 multiple choice (choosing a method) and in the structured questions and the alternative to practical section of Paper 2 (apparatus, steps and equations).", title="Exam link"),
        PQ("Describe how you would prepare crystals of zinc sulfate starting with zinc and dilute sulfuric acid.",
           "Add excess zinc to warm dilute sulfuric acid until no more bubbles. Filter to remove excess zinc. Evaporate the filtrate until it is saturated, leave to cool so crystals form, filter them, wash with a little cold water and dry. Equation: $\\mathrm{Zn + H_2SO_4 \\rightarrow ZnSO_4 + H_2}$."),
        PQ("Why is the titration repeated without indicator when making sodium sulfate crystals?",
           "The indicator would dissolve in the solution and contaminate the crystals. Once the exact volumes are known, the same volumes are mixed without it."),
        PQ("Calculate the theoretical mass of $\\mathrm{ZnSO_4}$ (anhydrous) from 6.5 g of zinc. ($A_r$: Zn = 65, S = 32, O = 16.)",
           "$n(\\mathrm{Zn}) = 6.5/65 = 0.10$ mol. Ratio 1 : 1, so $n(\\mathrm{ZnSO_4}) = 0.10$ mol. $M_r = 161$, so mass $= 0.10 \\times 161 = 16.1$ g."),
        PQ("Give one reason why a percentage yield is always less than 100 percent in practice.",
           "Some salt is lost on filter paper and glassware, remains in solution when it crystallises, or the crystals are not completely dry or pure."),
        SUM("A salt is formed when the hydrogen of an acid is replaced by a metal or ammonium ion.",
            "For soluble salts of metals other than Na, K and NH4: add an excess of metal, oxide, hydroxide or carbonate to the acid, filter, evaporate to saturation, crystallise.",
            "For sodium, potassium and ammonium salts, use titration, then repeat without indicator.",
            "Never evaporate to dryness. Crystallise from a saturated solution.",
            "Percentage yield = actual mass divided by theoretical mass, times 100."),
    ],
))

# ------------------------------------------------------------------ 4. Insoluble salts, solubility rules and curves
LESSONS.append(lesson(
    module=M3,
    topic="Preparation of salts and solubility",
    title="Insoluble salts, solubility rules and solubility curves",
    slug="chc-insoluble-salts-solubility",
    minutes=25,
    summary="The solubility rules for common salts, preparing an insoluble salt by precipitation, writing ionic equations, and defining and using solubility and solubility curves.",
    objectives=[
        "Use the solubility rules to predict whether a salt is soluble or insoluble",
        "Describe how to prepare an insoluble salt by precipitation and write the ionic equation",
        "Define solubility and a saturated solution",
        "Read a solubility curve and calculate how much solid crystallises on cooling",
    ],
    key_concepts=["Solubility", "Saturated solution", "Precipitate", "Spectator ion", "Solubility curve"],
    blocks=[
        H("Introduction"),
        T("When hard water from a borehole is boiled in a kettle, a white scale forms inside. It is an insoluble salt, calcium carbonate. "
          "When you stir salt into water for cooking, the salt disappears. It is soluble. "
          "How can we know in advance which salts dissolve and which do not? Chemists use a short set of **solubility rules**."),
        H("Solubility rules"),
        CODE("SOLUBLE\n"
             "All salts of sodium, potassium and ammonium\n"
             "All nitrates\n"
             "Chlorides, except silver chloride and lead(II) chloride\n"
             "Sulfates, except barium sulfate, lead(II) sulfate (calcium sulfate is slightly soluble)\n\n"
             "INSOLUBLE\n"
             "Carbonates, except those of sodium, potassium and ammonium\n"
             "Hydroxides, except those of sodium, potassium and (slightly) calcium\n"
             "Oxides, except those of sodium and potassium (which react with water)", "text", title="Rules for common salts"),
        TIP("Learn the rules in two groups. Nearly everything with Na, K, NH4 or nitrate is soluble. Then remember the few insoluble chlorides (Ag, Pb) and sulfates (Ba, Pb, Ca)."),
        MISTAKE("Calling PbCl2 soluble", "Lead(II) chloride is insoluble in cold water, although it dissolves in hot water. Always remember that Ag and Pb are exceptions among chlorides."),
        H("Preparing an insoluble salt: precipitation"),
        D("A **precipitate** is an insoluble solid that forms when two solutions are mixed. The process is called **precipitation**.", title="Precipitate"),
        IMG("f5ch-c-salt-flow-insoluble.svg", alt="Flowchart: mix two solutions, a precipitate forms, filter, wash with distilled water, dry",
            caption="Figure 1. Making an insoluble salt."),
        T("To make an insoluble salt, choose **two soluble salts**. One contains the positive ion wanted and the other contains the negative ion wanted. "
          "Their other ions combine to stay dissolved as a soluble salt."),
        CODE("Pb(NO3)2(aq) + 2KI(aq)  ->  PbI2(s) + 2KNO3(aq)\n"
             "lead nitrate + potassium iodide -> yellow solid + potassium nitrate (stays dissolved)", "text", title="Example: lead(II) iodide"),
        D("An **ionic equation** shows only the ions that react. **Spectator ions** are ions that are present but do not change, so they are left out.", title="Ionic equation"),
        CODE("Full:   Pb(NO3)2 + 2KI -> PbI2 + 2KNO3\n"
             "Ionic:  Pb2+(aq) + 2I-(aq) -> PbI2(s)\n"
             "Spectators: K+ and NO3-", "text", title="Writing the ionic equation"),
        T("The steps for the practical are: (1) mix the solutions; (2) **filter** to separate the solid from the solution; "
          "(3) **wash** the residue with distilled water to remove the soluble salt that sticks to it; (4) dry the solid between filter papers or in a warm oven."),
        EX("Worked example 1: choose the reagents", intro="Suggest solutions to make solid barium sulfate, and write the ionic equation.", steps=[
            S("Barium sulfate contains Ba2+ and SO4 2-", text="Use a soluble barium salt and a soluble sulfate."),
            S("Pick soluble salts", text="Barium chloride solution and sodium sulfate solution."),
            S("Full equation", math=r"\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}"),
            S("Ionic equation", math=r"\mathrm{Ba^{2+}(aq) + SO_4^{2-}(aq) \rightarrow BaSO_4(s)}"),
        ]),
        EX("Worked example 2: will a precipitate form?", intro="Will a precipitate form when silver nitrate solution is added to sodium chloride solution?", steps=[
            S("List the possible products", text="Silver chloride and sodium nitrate."),
            S("Check the rules", text="All nitrates are soluble. Silver chloride is an exception: it is insoluble."),
            S("Conclusion", math=r"\mathrm{AgNO_3 + NaCl \rightarrow AgCl(s) + NaNO_3}", text="A white precipitate of silver chloride forms."),
        ]),
        H("Solubility and solubility curves"),
        D("The **solubility** of a substance is the maximum mass of it that dissolves in 100 g of water at a stated temperature. "
          "A solution that holds this maximum amount is called **saturated**.", title="Solubility"),
        T("For most solids, solubility rises with temperature. Hot water dissolves more salt than cold water. "
          "For gases such as oxygen, the opposite is true. Warm water holds less dissolved oxygen, which is why fish in hot ponds may struggle."),
        IMG("f5ch-c-solubility-curve.svg", alt="Solubility curve of salt X rising from 20 g per 100 g water at 20 degrees C to 80 g per 100 g at 80 degrees C",
            caption="Figure 2. A solubility curve. The data are for teaching, not for a real salt."),
        T("A **solubility curve** is a graph of solubility against temperature. A point on the curve is a saturated solution. "
          "A point below the curve is unsaturated. If you cool a saturated solution, the solubility falls and the extra solute comes out as **crystals**."),
        EX("Worked example 3: crystals on cooling", intro="Using Figure 2, 50 g of water is saturated with salt X at 60 degrees C. It is then cooled to 20 degrees C. What mass of crystals forms?", steps=[
            S("Read the solubility at 60 degrees C", text="55 g per 100 g of water."),
            S("Scale to 50 g of water", math=r"55 \times \frac{50}{100} = 27.5\ \mathrm{g\ dissolved}"),
            S("Read the solubility at 20 degrees C and scale", math=r"20 \times \frac{50}{100} = 10\ \mathrm{g\ can\ stay\ dissolved}"),
            S("Subtract", math=r"27.5 - 10 = 17.5\ \mathrm{g\ of\ crystals}"),
        ]),
        QUIZ("Which of these salts is insoluble in water?",
             ["Potassium carbonate", "Ammonium chloride", "Lead(II) sulfate", "Magnesium nitrate"], 2,
             "Most sulfates are soluble, but those of barium and lead(II) are not.",
             hint="Remember the exceptions among sulfates.",
             feedback=["Carbonates of potassium, sodium and ammonium are soluble.", "All ammonium salts are soluble.", "", "All nitrates are soluble."]),
        QUIZ("Why is the precipitate washed with distilled water?",
             ["To make it dissolve", "To remove soluble salt left on the solid", "To cool it", "To make it saturated"], 1,
             "The solution that wets the precipitate contains the soluble salt (such as potassium nitrate). Washing removes it.",
             hint="What other substance is in the mixture besides the precipitate?",
             feedback=["The precipitate is insoluble, so it will stay as a solid.", "", "Cooling is not the purpose.", "A solid cannot be saturated; solutions are."]),
        TIP("Exam link: solubility rules and precipitation are tested in Paper 1 multiple choice. Solubility curves and preparation of salts also come up in Paper 2 structured questions and in the alternative to practical section, where you may be asked for steps, observations and ionic equations.", title="Exam link"),
        PQ("Write the ionic equation for the reaction between aqueous silver nitrate and aqueous sodium chloride.",
           "$\\mathrm{Ag^+(aq) + Cl^-(aq) \\rightarrow AgCl(s)}$. The spectator ions are $\\mathrm{Na^+}$ and $\\mathrm{NO_3^-}$."),
        PQ("Suggest a method to prepare insoluble calcium carbonate from calcium chloride.",
           "Mix calcium chloride solution with sodium carbonate solution. White calcium carbonate precipitates. Filter, wash with distilled water, dry. $\\mathrm{CaCl_2 + Na_2CO_3 \\rightarrow CaCO_3 + 2NaCl}$."),
        PQ("Define solubility.",
           "Solubility is the maximum mass of a solute that dissolves in 100 g of water at a stated temperature to form a saturated solution."),
        PQ("Use Figure 2. What mass of salt X is needed to saturate 200 g of water at 80 degrees C?",
           "At 80 degrees C, 80 g dissolve in 100 g of water. For 200 g of water: $80 \\times 2 = 160$ g."),
        SUM("Learn the rules: all nitrates and all Na, K and NH4 salts are soluble; carbonates and hydroxides are mostly insoluble; chlorides and sulfates have a few exceptions.",
            "To make an insoluble salt, mix two soluble salts that supply the right ions, filter, wash with distilled water and dry.",
            "Ionic equations show only the reacting ions; spectator ions are left out.",
            "Solubility is the maximum mass dissolving in 100 g of water at a stated temperature.",
            "On cooling a saturated solution, the difference in solubility appears as crystals."),
    ],
))

# ------------------------------------------------------------------ 5. Water of crystallization
LESSONS.append(lesson(
    module=M3,
    topic="Water of crystallization and related terms",
    title="Water of crystallization, efflorescence, deliquescence and hygroscopy",
    slug="chc-water-of-crystallization",
    minutes=22,
    summary="Hydrated and anhydrous salts, tests for water, the terms efflorescence, deliquescence and hygroscopic, and calculating the percentage of water or the number of water molecules in a hydrate.",
    objectives=[
        "Define water of crystallization and distinguish hydrated and anhydrous salts",
        "Describe the colour changes used to test for water",
        "Define and give examples of efflorescence, deliquescence and hygroscopy",
        "Calculate the percentage of water in a hydrate and the value of x in a formula such as CuSO4.xH2O",
    ],
    key_concepts=["Water of crystallization", "Hydrated", "Anhydrous", "Efflorescence", "Deliquescence", "Hygroscopic"],
    blocks=[
        H("Introduction"),
        T("In Douala, table salt left in an open dish often turns damp and sticks together in the humid air. "
          "In a dry classroom cupboard, white powder may cover old washing soda crystals. Both are examples of salts reacting with water vapour in the air, in different ways. "
          "In this lesson you learn the names for these behaviours and how to calculate the water inside a crystal."),
        H("Hydrated and anhydrous salts"),
        D("**Water of crystallization** is the fixed number of water molecules that are chemically joined to the ions inside the crystals of some salts. "
          "A salt with water of crystallization is **hydrated**. One without is **anhydrous**.", title="Water of crystallization"),
        CODE("Hydrated salt                 Formula             Colour\n"
             "Copper(II) sulfate-5-water    CuSO4.5H2O          blue\n"
             "Washing soda                  Na2CO3.10H2O        colourless\n"
             "Epsom salt                    MgSO4.7H2O          colourless\n"
             "Iron(II) sulfate-7-water      FeSO4.7H2O          pale green\n"
             "Cobalt(II) chloride-6-water   CoCl2.6H2O          pink", "text", title="Examples"),
        T("The water molecules are part of the crystal structure. When they are removed, the crystal falls apart into a powder and often changes colour."),
        CODE("CuSO4.5H2O  <->  CuSO4  +  5H2O\n"
             "blue crystals     white powder", "text", title="Heating a hydrate"),
        T("The change is **reversible**. If you add water to white anhydrous copper(II) sulfate it turns blue again, and gets warm. "
          "This is a simple **test for water**. Cobalt(II) chloride paper is blue when dry and pink when water touches it."),
        TIP("These tests show that water is present. They do not prove that the liquid is pure water. Use the boiling point (100 degrees C) for purity."),
        H("Efflorescence, deliquescence and hygroscopy"),
        D("**Efflorescence** is the loss of water of crystallization from hydrated crystals to the air, so that they become a dry powder. "
          "It happens when the air is drier than the crystal. Example: washing soda, $\\mathrm{Na_2CO_3 \\cdot 10H_2O}$.", title="Efflorescence"),
        D("**Deliquescence** is when a solid absorbs so much water vapour from the air that it dissolves in it and forms a solution. "
          "Examples: sodium hydroxide, anhydrous calcium chloride, iron(III) chloride.", title="Deliquescence"),
        D("A **hygroscopic** substance absorbs water vapour from the air. It may become damp or swell but does not always dissolve. "
          "Examples: concentrated sulfuric acid, silica gel, anhydrous copper(II) sulfate, quicklime.", title="Hygroscopy"),
        TIP("Some textbooks use \"hygroscopic\" for all substances that take in water, including deliquescent ones. Check your textbook and follow your teacher's definition."),
        KEY("Using these properties", "These properties are put to work in everyday life and in the laboratory.", cards=[
            ["Drying agents", "Silica gel packets in new shoes or electronics, and calcium chloride in a desiccator, absorb moisture."],
            ["Storage", "Sodium hydroxide must be kept in a tightly closed bottle because it is deliquescent."],
            ["Test for water", "Anhydrous copper(II) sulfate turns from white to blue; cobalt chloride paper from blue to pink."],
            ["Table salt", "Impure salt contains substances that absorb moisture, so it cakes. Adding a drying agent keeps it free-flowing."],
        ]),
        H("Calculations with hydrates"),
        D("Percentage of water in a hydrate = mass of water in one formula unit divided by the relative formula mass of the hydrate, times 100.", title="Percentage of water",
          formula=r"\% \text{ water} = \frac{x \times 18}{M_r \text{ of hydrate}} \times 100"),
        EX("Worked example 1: percentage of water", intro="Calculate the percentage of water in washing soda, $\\mathrm{Na_2CO_3 \\cdot 10H_2O}$. ($A_r$: Na = 23, C = 12, O = 16, H = 1.)", steps=[
            S("Relative mass of $\\mathrm{Na_2CO_3}$", math=r"46 + 12 + 48 = 106"),
            S("Relative mass of $10\\mathrm{H_2O}$", math=r"10 \times 18 = 180"),
            S("Relative mass of the hydrate", math=r"106 + 180 = 286"),
            S("Percentage of water", math=r"\frac{180}{286} \times 100 = 62.9\%"),
        ]),
        EX("Worked example 2: finding x", intro="2.495 g of hydrated copper(II) sulfate, $\\mathrm{CuSO_4 \\cdot xH_2O}$, is heated until all the water has gone. 1.595 g of white anhydrous salt remains. Find x. ($M_r$ of $\\mathrm{CuSO_4}$ = 159.5.)", steps=[
            S("Mass of water lost", math=r"2.495 - 1.595 = 0.900\ \mathrm{g}"),
            S("Moles of water", math=r"0.900 \div 18 = 0.050\ \mathrm{mol}"),
            S("Moles of anhydrous salt", math=r"1.595 \div 159.5 = 0.010\ \mathrm{mol}"),
            S("Divide to find the ratio", math=r"x = 0.050 \div 0.010 = 5"),
        ], check=r"\mathrm{CuSO_4 \cdot 5H_2O}"),
        MISTAKE("Using the mass of the hydrate as the mass of the salt", "After heating, the mass left is the anhydrous salt. The mass lost is the water. Use these two masses separately when finding moles."),
        QUIZ("A white powder forms on old washing soda crystals kept in a dry cupboard. This is an example of...",
             ["Deliquescence", "Efflorescence", "Hygroscopy", "Neutralization"], 1,
             "Hydrated crystals have lost water of crystallization to the dry air, leaving a powder. This is efflorescence.",
             hint="Did the crystal gain water or lose water?",
             feedback=["Deliquescence means absorbing water until the solid dissolves.", "", "Hygroscopic substances absorb water; here water was lost.", "No acid and base have reacted."]),
        QUIZ("Pellets of sodium hydroxide left in an open dish become wet and then form a liquid. This property is called...",
             ["Efflorescence", "Crystallization", "Deliquescence", "Dehydration"], 2,
             "The solid takes in water vapour and dissolves in it.", hint="The solid takes in so much water that it dissolves.",
             feedback=["Efflorescence is a loss of water.", "Crystallization is forming crystals from solution.", "", "Dehydration is removing water."]),
        TIP("Exam link: these terms and the percentage-of-water calculation appear in Paper 1 multiple choice and in Paper 2 structured questions. Define each term carefully and give an example.", title="Exam link"),
        PQ("Define water of crystallization and give one example of a hydrated salt with its formula.",
           "It is the fixed number of water molecules chemically bonded in crystals of a salt. Example: $\\mathrm{CuSO_4 \\cdot 5H_2O}$."),
        PQ("Describe a chemical test for water.",
           "Add the liquid to white anhydrous copper(II) sulfate. It turns blue if water is present. Or test with blue cobalt(II) chloride paper, which turns pink."),
        PQ("Calculate the percentage of water in $\\mathrm{MgSO_4 \\cdot 7H_2O}$. ($A_r$: Mg = 24, S = 32, O = 16, H = 1.)",
           "$M_r = 120 + 126 = 246$. Water: $7 \\times 18 = 126$. $126/246 \\times 100 = 51.2\\%$."),
        PQ("Explain why anhydrous calcium chloride is used in a desiccator.",
           "It is hygroscopic and deliquescent. It absorbs water vapour from the air, so the air and the stored substances stay dry."),
        SUM("Hydrated salts contain water of crystallization; anhydrous salts do not.",
            "White anhydrous copper(II) sulfate turns blue with water; blue cobalt(II) chloride paper turns pink.",
            "Efflorescence loses water to the air. Deliquescence absorbs so much water that the solid dissolves. Hygroscopic substances absorb water vapour.",
            "Percentage of water = (x times 18) divided by the relative mass of the hydrate, times 100.",
            "To find x, divide moles of water by moles of anhydrous salt."),
    ],
))

# ------------------------------------------------------------------ 6. Oxidation and reduction I
LESSONS.append(lesson(
    module=M3,
    topic="Oxidation and reduction",
    title="Oxidation and reduction: oxygen, hydrogen and electron transfer",
    slug="chc-redox-transfer",
    minutes=23,
    summary="Oxidation and reduction as gain or loss of oxygen, loss or gain of hydrogen and, most generally, loss or gain of electrons, with half-equations and oxidising and reducing agents.",
    objectives=[
        "Define oxidation and reduction in terms of oxygen, hydrogen and electrons",
        "Identify what is oxidised and what is reduced in a reaction",
        "Write ionic half-equations for oxidation and reduction",
        "Define oxidising agent and reducing agent and name examples",
    ],
    key_concepts=["Oxidation", "Reduction", "Redox", "Half-equation", "Oxidising agent", "Reducing agent"],
    blocks=[
        H("Introduction"),
        T("A roof of corrugated iron sheet in Bamenda turns red-brown after a few rainy seasons. Charcoal glows and gives heat in a cooking stove. "
          "A car battery stores energy. All of these involve **oxidation and reduction**. "
          "Chemists often shorten the two names together to **redox**."),
        H("Three ways to define oxidation and reduction"),
        T("The first ideas were about oxygen. Later, chemists saw that hydrogen could be used, and finally that **electrons** explain every case."),
        KEY("The three definitions", "Learn all three. Electron transfer is the most general.", cards=[
            ["Oxygen", "Oxidation is gain of oxygen. Reduction is loss of oxygen."],
            ["Hydrogen", "Oxidation is loss of hydrogen. Reduction is gain of hydrogen."],
            ["Electrons", "Oxidation is loss of electrons. Reduction is gain of electrons."],
        ]),
        TIP("Memory aid: **OIL RIG**. Oxidation Is Loss (of electrons). Reduction Is Gain (of electrons)."),
        H("Oxygen and hydrogen transfer"),
        CODE("2Mg + O2  ->  2MgO         Mg gains oxygen: Mg is oxidised\n"
             "CuO + H2 ->  Cu + H2O      CuO loses oxygen: CuO is reduced\n"
             "                           H2 gains oxygen: H2 is oxidised\n"
             "H2S + Cl2 -> 2HCl + S      H2S loses hydrogen: H2S is oxidised\n"
             "                           Cl2 gains hydrogen: Cl2 is reduced", "text", title="Examples"),
        T("In every example, oxidation and reduction happen **together**. If something loses oxygen, something else gains it. That is why the reactions are called redox reactions."),
        H("Electron transfer and half-equations"),
        T("A **half-equation** shows only the oxidation or only the reduction. It includes the electrons, written $e^-$. Both atoms and charges must balance."),
        CODE("Oxidation:   Mg  ->  Mg2+ + 2e-        (loses 2 electrons)\n"
             "Reduction:   Cu2+ + 2e-  ->  Cu       (gains 2 electrons)\n"
             "Overall:     Mg + Cu2+  ->  Mg2+ + Cu\n\n"
             "In the overall equation the electrons cancel.", "text", title="Magnesium and copper(II) sulfate"),
        D("An **oxidising agent** takes electrons from another substance. It is itself **reduced**. A **reducing agent** gives electrons to another substance. It is itself **oxidised**.", title="Agents"),
        KEY("Typical agents", "Oxidising agents are often reactive non-metals or substances rich in oxygen. Reducing agents are often metals or hydrogen.", cards=[
            ["Oxidising agents", "Oxygen, chlorine, hydrogen peroxide, acidified potassium manganate(VII), acidified potassium dichromate(VI), concentrated nitric acid."],
            ["Reducing agents", "Reactive metals, hydrogen, carbon, carbon monoxide, sulfur dioxide, iron(II) ions, iodide ions."],
        ]),
        EX("Worked example 1: iron and copper(II) sulfate", intro="Iron nails are dipped in copper(II) sulfate solution and become coated with copper. Show what is oxidised and what is reduced.", steps=[
            S("Full equation", math=r"\mathrm{Fe + CuSO_4 \rightarrow FeSO_4 + Cu}"),
            S("Ionic equation (remove spectator $\\mathrm{SO_4^{2-}}$)", math=r"\mathrm{Fe + Cu^{2+} \rightarrow Fe^{2+} + Cu}"),
            S("Oxidation half-equation", math=r"\mathrm{Fe \rightarrow Fe^{2+} + 2e^-}", text="Iron loses electrons, so it is oxidised and is the reducing agent."),
            S("Reduction half-equation", math=r"\mathrm{Cu^{2+} + 2e^- \rightarrow Cu}", text="Copper(II) ions gain electrons, so they are reduced. $\\mathrm{Cu^{2+}}$ is the oxidising agent."),
        ]),
        EX("Worked example 2: chlorine and potassium bromide", intro="Chlorine gas is bubbled into potassium bromide solution. The solution turns orange-brown because bromine forms. Write the half-equations.", steps=[
            S("Equation", math=r"\mathrm{Cl_2 + 2KBr \rightarrow 2KCl + Br_2}"),
            S("Oxidation (bromide loses electrons)", math=r"\mathrm{2Br^- \rightarrow Br_2 + 2e^-}"),
            S("Reduction (chlorine gains electrons)", math=r"\mathrm{Cl_2 + 2e^- \rightarrow 2Cl^-}"),
            S("Agents", text="Chlorine is the oxidising agent. Bromide ions are the reducing agent."),
        ]),
        EX("Worked example 3: rusting", intro="Iron rusts: $\\mathrm{4Fe + 3O_2 \\rightarrow 2Fe_2O_3}$. Explain why this is redox.", steps=[
            S("Iron gains oxygen", text="Fe is oxidised (gain of oxygen). In electrons: $\\mathrm{Fe \\rightarrow Fe^{3+} + 3e^-}$."),
            S("Oxygen is reduced", text="Oxygen gains electrons to form oxide ions: $\\mathrm{O_2 + 4e^- \\rightarrow 2O^{2-}}$."),
            S("Conclusion", text="Oxidation and reduction occur together, so rusting is a redox reaction. Rust is really hydrated iron(III) oxide, formed when iron meets oxygen and water."),
        ]),
        MISTAKE("Thinking the agent is the one oxidised", "The **oxidising agent** is the substance that is **reduced**. The **reducing agent** is the one that is **oxidised**. "
                "Check by asking: who takes electrons (oxidising agent), who gives them (reducing agent)?"),
        MISTAKE("Forgetting the electrons in half-equations", "Half-equations must balance both atoms and charge. Electrons appear on the right in oxidation and on the left in reduction."),
        QUIZ("Which change is an example of reduction?",
             ["$\\mathrm{Mg \\rightarrow Mg^{2+} + 2e^-}$", "$\\mathrm{Cu^{2+} + 2e^- \\rightarrow Cu}$", "$\\mathrm{2Br^- \\rightarrow Br_2 + 2e^-}$", "$\\mathrm{Fe^{2+} \\rightarrow Fe^{3+} + e^-}$"], 1,
             "Reduction is gain of electrons. Only the second equation has electrons on the left side (gained).",
             hint="Look for electrons on the left side of the arrow.",
             feedback=["Electrons are lost, so this is oxidation.", "", "Electrons are lost, so this is oxidation.", "Electrons are lost, so this is oxidation."]),
        QUIZ("In $\\mathrm{CuO + H_2 \\rightarrow Cu + H_2O}$, hydrogen acts as...",
             ["an oxidising agent", "a catalyst", "a reducing agent", "a spectator"], 2,
             "Hydrogen takes oxygen from copper(II) oxide, so it is oxidised and acts as the reducing agent.",
             hint="Which substance gains oxygen?",
             feedback=["The oxidising agent is the one reduced: CuO.", "A catalyst is not used up.", "", "It takes part in the change."]),
        TIP("Exam link: redox definitions, half-equations and agents appear in Paper 1 multiple choice and in Paper 2 structured questions, often linked with displacement reactions and electrolysis.", title="Exam link"),
        PQ("State the meaning of oxidation in terms of electrons and give a half-equation.",
           "Oxidation is loss of electrons. Example: $\\mathrm{Zn \\rightarrow Zn^{2+} + 2e^-}$."),
        PQ("In $\\mathrm{Zn + 2HCl \\rightarrow ZnCl_2 + H_2}$, name the substance oxidised and the substance reduced.",
           "Zinc is oxidised: $\\mathrm{Zn \\rightarrow Zn^{2+} + 2e^-}$. Hydrogen ions are reduced: $\\mathrm{2H^+ + 2e^- \\rightarrow H_2}$."),
        PQ("Define a reducing agent and give one example.",
           "A reducing agent gives electrons to another substance and is itself oxidised. Example: magnesium, or hydrogen, or iron(II) ions."),
        PQ("Is $\\mathrm{NaOH + HCl \\rightarrow NaCl + H_2O}$ a redox reaction? Explain.",
           "No. No electrons are transferred. The ions only recombine: $\\mathrm{H^+ + OH^- \\rightarrow H_2O}$. It is neutralization."),
        SUM("Oxidation: gain of oxygen, loss of hydrogen or loss of electrons. Reduction: loss of oxygen, gain of hydrogen or gain of electrons.",
            "OIL RIG: Oxidation Is Loss, Reduction Is Gain of electrons.",
            "Oxidation and reduction always happen together in a redox reaction.",
            "An oxidising agent is reduced. A reducing agent is oxidised.",
            "Half-equations show electrons and must balance atoms and charge."),
    ],
))

# ------------------------------------------------------------------ 7. Oxidation numbers and tests for agents
LESSONS.append(lesson(
    module=M3,
    topic="Oxidation and reduction",
    title="Oxidation numbers and tests for oxidising and reducing agents",
    slug="chc-oxidation-numbers-tests",
    minutes=25,
    summary="Rules for working out oxidation numbers, using changes in oxidation number to spot oxidation and reduction, naming with Roman numerals, and laboratory tests for oxidising and reducing agents.",
    objectives=[
        "Apply the rules to work out oxidation numbers of elements in compounds and ions",
        "Identify oxidation and reduction from a change in oxidation number",
        "Use Roman numerals in names such as iron(III) oxide and manganate(VII)",
        "Describe tests for oxidising agents (potassium iodide) and reducing agents (acidified manganate(VII) and dichromate(VI))",
    ],
    key_concepts=["Oxidation number", "Roman numeral", "Increase and decrease", "Potassium iodide test", "Acidified potassium manganate(VII)", "Acidified potassium dichromate(VI)"],
    blocks=[
        H("Introduction"),
        T("In the last lesson you followed electrons in simple reactions. But in many compounds, such as $\\mathrm{KMnO_4}$ or $\\mathrm{H_2SO_4}$, it is hard to see which atom gains or loses electrons. "
          "Chemists use **oxidation numbers**, a bookkeeping system that shows where electrons have moved. "
          "Iron rust, for example, contains iron with oxidation number +3. Iron in green iron(II) sulfate crystals has +2."),
        H("Rules for oxidation numbers"),
        D("The **oxidation number** of an atom is the charge it would have if all the bonds in the substance were ionic.", title="Oxidation number"),
        CODE("1. Atoms in an element on its own: 0          (Mg, O2, Cl2, S8)\n"
             "2. A simple ion: its charge                   (Na+ is +1, Cl- is -1, Fe3+ is +3)\n"
             "3. Total for a neutral compound: 0            (H2O: 2(+1) + (-2) = 0)\n"
             "4. Total for an ion: equals the ion's charge  (SO4 2-: S + 4(-2) = -2)\n"
             "5. Group 1 metals: +1.  Group 2 metals: +2.  Aluminium: +3\n"
             "6. Hydrogen: +1 (except in metal hydrides, -1)\n"
             "7. Oxygen: -2 (except in peroxides, -1)\n"
             "8. Chlorine in chlorides: -1", "text", title="The rules"),
        EX("Worked example 1: oxidation numbers", intro="Find the oxidation number of (a) S in $\\mathrm{H_2SO_4}$, (b) Mn in $\\mathrm{KMnO_4}$, (c) Cr in $\\mathrm{K_2Cr_2O_7}$.", steps=[
            S("(a) $\\mathrm{H_2SO_4}$ is neutral", math=r"2(+1) + S + 4(-2) = 0 \Rightarrow S = +6"),
            S("(b) $\\mathrm{KMnO_4}$ is neutral", math=r"(+1) + Mn + 4(-2) = 0 \Rightarrow Mn = +7"),
            S("(c) $\\mathrm{K_2Cr_2O_7}$ is neutral", math=r"2(+1) + 2Cr + 7(-2) = 0 \Rightarrow 2Cr = +12 \Rightarrow Cr = +6"),
        ]),
        EX("Worked example 2: more examples", intro="Find the oxidation number of nitrogen in $\\mathrm{NH_3}$, $\\mathrm{NO_2}$ and $\\mathrm{HNO_3}$, and of iron in $\\mathrm{Fe_2O_3}$.", steps=[
            S("$\\mathrm{NH_3}$", math=r"N + 3(+1) = 0 \Rightarrow N = -3"),
            S("$\\mathrm{NO_2}$", math=r"N + 2(-2) = 0 \Rightarrow N = +4"),
            S("$\\mathrm{HNO_3}$", math=r"(+1) + N + 3(-2) = 0 \Rightarrow N = +5"),
            S("$\\mathrm{Fe_2O_3}$", math=r"2Fe + 3(-2) = 0 \Rightarrow Fe = +3"),
        ]),
        H("Using oxidation numbers"),
        D("**Oxidation** is an **increase** in oxidation number. **Reduction** is a **decrease** in oxidation number. "
          "A reaction in which no oxidation number changes is **not** redox.", title="Redox by oxidation number"),
        CODE("Mg + CuSO4 -> MgSO4 + Cu\n"
             "Mg:  0 -> +2     increase: oxidised\n"
             "Cu: +2 ->  0     decrease: reduced\n\n"
             "NaOH + HCl -> NaCl + H2O\n"
             "Na +1, O -2, H +1, Cl -1 all stay the same: not redox", "text", title="Two examples"),
        T("**Roman numerals** in names give the oxidation number of the metal. Iron(II) oxide is FeO and iron(III) oxide is $\\mathrm{Fe_2O_3}$. "
          "Potassium manganate(VII) is $\\mathrm{KMnO_4}$ with Mn at +7. Potassium dichromate(VI) is $\\mathrm{K_2Cr_2O_7}$ with Cr at +6."),
        H("Tests for oxidising and reducing agents"),
        CODE("Test for a reducing agent\n"
             "  Acidified potassium manganate(VII): purple -> colourless\n"
             "  Acidified potassium dichromate(VI): orange -> green\n\n"
             "Test for an oxidising agent\n"
             "  Potassium iodide solution: colourless -> brown (iodine)\n"
             "  (with starch, blue-black)", "text", title="Laboratory tests"),
        T("**Reducing agents** such as sulfur dioxide, hydrogen sulfide and iron(II) ions give electrons. The manganate(VII) ion $\\mathrm{MnO_4^-}$ (Mn +7) is reduced to nearly colourless $\\mathrm{Mn^{2+}}$ (Mn +2), "
          "so the purple colour disappears. The dichromate(VI) ion is reduced from orange $\\mathrm{Cr_2O_7^{2-}}$ to green $\\mathrm{Cr^{3+}}$."),
        T("**Oxidising agents** such as chlorine or hydrogen peroxide take electrons from iodide ions. Iodide is oxidised to iodine, which is brown in solution."),
        CODE("5Fe2+ + MnO4- + 8H+  ->  5Fe3+ + Mn2+ + 4H2O\n"
             "Fe: +2 -> +3 (oxidised)     Mn: +7 -> +2 (reduced)\n\n"
             "Cl2 + 2I-  ->  2Cl- + I2\n"
             "Cl: 0 -> -1 (reduced)       I: -1 -> 0 (oxidised)", "text", title="Two ionic equations"),
        TIP("In the manganate(VII) test, the solution must be acidified (with dilute sulfuric acid). Do not use hydrochloric acid, because it is itself slowly oxidised by manganate(VII)."),
        MISTAKE("Wrong sign convention", "Write the sign: +6, not 6, and -2, not 2-. An ion charge is written as $\\mathrm{2-}$ with the number first, but an oxidation number is written with the sign first."),
        QUIZ("What is the oxidation number of nitrogen in $\\mathrm{HNO_3}$?",
             ["+3", "+5", "-3", "+1"], 1,
             "H is +1 and three O atoms are -6. So $1 + N - 6 = 0$, giving $N = +5$.",
             hint="Add up the oxidation numbers of H and O first.",
             feedback=["Check: +1 and +3 would not cancel -6.", "", "That is nitrogen in ammonia, NH3.", "Hydrogen is +1; nitrogen is not."]),
        QUIZ("A few drops of acidified potassium manganate(VII) are added to a solution. The purple colour disappears. What does this show?",
             ["The solution contains an oxidising agent", "The solution contains a reducing agent", "The solution is alkaline", "The solution contains water"], 1,
             "Manganate(VII) is reduced to Mn2+, which is almost colourless. Something in the solution reduced it, so the solution contains a reducing agent.",
             hint="The purple ion is the oxidising agent here.",
             feedback=["The oxidising agent is the manganate(VII) itself.", "", "The test is done in acid, not for alkalinity.", "Water is always present and does not cause the colour change."]),
        TIP("Exam link: oxidation numbers and the tests for oxidising and reducing agents appear in Paper 1 multiple choice and in the structured questions and alternative to practical section of Paper 2, where you describe the colour changes.", title="Exam link"),
        PQ("Find the oxidation number of sulfur in $\\mathrm{SO_2}$ and in $\\mathrm{H_2S}$.",
           "$\\mathrm{SO_2}$: $S + 2(-2) = 0$, so S = +4. $\\mathrm{H_2S}$: $2(+1) + S = 0$, so S = -2."),
        PQ("In $\\mathrm{Cl_2 + 2KI \\rightarrow 2KCl + I_2}$, state the change in oxidation number of chlorine and of iodine and name what is oxidised.",
           "Chlorine goes from 0 to -1 (reduced). Iodine goes from -1 to 0 (oxidised). Iodide ions are oxidised."),
        PQ("Describe what you would see when acidified potassium dichromate(VI) is warmed with a solution containing sulfur dioxide, and explain.",
           "The orange solution turns green. Dichromate(VI) (Cr +6) is reduced to chromium(III) (Cr +3) by sulfur dioxide, which is a reducing agent."),
        PQ("Name the compound $\\mathrm{FeSO_4}$ and state the oxidation number of iron in it.",
           "Iron(II) sulfate. The sulfate ion is $\\mathrm{SO_4^{2-}}$, so iron is +2."),
        SUM("Oxidation number rules: element 0; simple ion = its charge; compounds add up to 0; ions add up to the charge; H is +1, O is -2, Group 1 +1, Group 2 +2.",
            "Oxidation is an increase in oxidation number. Reduction is a decrease.",
            "Roman numerals give the oxidation number: iron(III) is +3, manganate(VII) has Mn +7.",
            "Reducing agent test: acidified manganate(VII) turns purple to colourless; acidified dichromate(VI) turns orange to green.",
            "Oxidising agent test: potassium iodide solution turns brown because iodine forms."),
    ],
))

# ------------------------------------------------------------------ 8. Exothermic and endothermic reactions
LESSONS.append(lesson(
    module=M4,
    topic="Exothermic and endothermic reactions",
    title="Exothermic and endothermic reactions and energy profile diagrams",
    slug="chc-exothermic-endothermic-profiles",
    minutes=23,
    summary="Reactions that release heat (exothermic) and absorb heat (endothermic), the sign of delta H, bond breaking and making, and how to read and draw energy profile diagrams with activation energy and a catalyst.",
    objectives=[
        "Define exothermic and endothermic reactions and give examples of each",
        "State the sign of delta H for each type and relate it to the temperature change",
        "Explain energy changes in terms of bond breaking and bond making",
        "Read and draw energy profile diagrams, labelling reactants, products, activation energy and delta H",
    ],
    key_concepts=["Exothermic", "Endothermic", "Enthalpy change (delta H)", "Activation energy", "Energy profile diagram", "Catalyst"],
    blocks=[
        H("Introduction"),
        T("When a bottle-gas stove burns, the flame heats the pot. When a farmer slakes quicklime with water to make lime for building, the mixture becomes too hot to touch. "
          "On the other hand, a cold pack used for a sports injury feels icy when it is activated. "
          "In each case a chemical or physical change moves **energy** between the substances and their surroundings."),
        H("Exothermic and endothermic"),
        D("An **exothermic reaction** gives out energy, usually as heat, to the surroundings. The temperature of the surroundings **rises**.", title="Exothermic"),
        D("An **endothermic reaction** takes in energy, usually as heat, from the surroundings. The temperature of the surroundings **falls**.", title="Endothermic"),
        KEY("Examples", "Learn at least three of each.", cards=[
            ["Exothermic", "Burning fuels (charcoal, gas, wood). Respiration in our cells. Neutralization of acid by alkali. Dissolving sodium hydroxide in water. Quicklime with water."],
            ["Endothermic", "Photosynthesis (energy from sunlight). Thermal decomposition of calcium carbonate (limestone) into lime. Dissolving ammonium nitrate in water. Citric acid with sodium hydrogencarbonate."],
        ]),
        T("The **enthalpy change**, written $\\Delta H$ (delta H), is the heat energy change of a reaction at constant pressure. Its unit is kilojoules per mole, kJ per mol."),
        D("$\\Delta H = H_{\\text{products}} - H_{\\text{reactants}}$. For an exothermic reaction $\\Delta H$ is **negative**. For an endothermic reaction $\\Delta H$ is **positive**.", title="Sign of delta H",
          formula=r"\Delta H = H_{\text{products}} - H_{\text{reactants}}"),
        TIP("Link the sign to what happens to the substances. Exothermic: the products have **less** energy than the reactants because energy leaves, so $\\Delta H$ is negative. Endothermic: the products have **more** energy, so $\\Delta H$ is positive."),
        H("Bond breaking and bond making"),
        T("Every reaction breaks old bonds and makes new bonds. **Breaking** bonds needs energy, so it is endothermic. **Making** bonds gives out energy, so it is exothermic."),
        CODE("Energy to break bonds  >  energy released making bonds   ->  endothermic overall\n"
             "Energy to break bonds  <  energy released making bonds   ->  exothermic overall", "text", title="Which side wins"),
        H("Energy profile diagrams"),
        T("An **energy profile diagram** plots the energy of the substances against the progress of the reaction. It shows the energy level of the reactants, the energy level of the products and a hump in between."),
        D("The **activation energy**, $E_a$, is the minimum energy that colliding particles must have to react. On the diagram it is the height from the reactants to the top of the hump.", title="Activation energy"),
        IMG("f5ch-c-profile-exo.svg", alt="Energy profile diagram for an exothermic reaction: products lower than reactants, with activation energy hump and a downward delta H arrow",
            caption="Figure 1. Exothermic reaction: products are lower than reactants."),
        IMG("f5ch-c-profile-endo.svg", alt="Energy profile diagram for an endothermic reaction: products higher than reactants, with activation energy hump and an upward delta H arrow",
            caption="Figure 2. Endothermic reaction: products are higher than reactants."),
        T("Even exothermic reactions need a start. A candle does not burn until a match gives it the activation energy. Once it burns, the heat released keeps the reaction going."),
        H("Effect of a catalyst"),
        D("A **catalyst** is a substance that speeds up a reaction without being used up. It provides a different route with a **lower activation energy**. It does **not** change $\\Delta H$.", title="Catalyst"),
        IMG("f5ch-c-profile-catalyst.svg", alt="Two energy profile humps with the same start and end: the black one is higher, the green one with a catalyst is lower",
            caption="Figure 3. A catalyst lowers the hump but reactants and products stay at the same levels."),
        EX("Worked example 1: reading an exothermic profile", intro="A reaction has reactants at 250 kJ per mol, the top of the hump at 340 kJ per mol and products at 180 kJ per mol. Find $E_a$, $\\Delta H$ and the activation energy of the reverse reaction.", steps=[
            S("Activation energy", math=r"E_a = 340 - 250 = 90\ \mathrm{kJ/mol}"),
            S("Enthalpy change", math=r"\Delta H = 180 - 250 = -70\ \mathrm{kJ/mol}", text="Negative, so exothermic."),
            S("Reverse reaction", math=r"E_a(\text{reverse}) = 340 - 180 = 160\ \mathrm{kJ/mol}", text="The reverse reaction has $\\Delta H = +70$ kJ per mol."),
        ]),
        EX("Worked example 2: an endothermic reaction", intro="Reactants are at 40 kJ per mol, products at 110 kJ per mol and the top of the hump at 170 kJ per mol. Find $E_a$ and $\\Delta H$.", steps=[
            S("Activation energy", math=r"E_a = 170 - 40 = 130\ \mathrm{kJ/mol}"),
            S("Enthalpy change", math=r"\Delta H = 110 - 40 = +70\ \mathrm{kJ/mol}"),
            S("Conclusion", text="$\\Delta H$ is positive, so the reaction is endothermic. The surroundings cool down."),
        ]),
        MISTAKE("Mixing up Ea and delta H", "$E_a$ is measured from the reactants **up to the top of the hump**. $\\Delta H$ is measured from the reactants **to the products**. They are different arrows."),
        MISTAKE("\"It needs heat to start, so it is endothermic\"", "Many exothermic reactions need a spark or a flame to start. Judge by the overall energy change: do the products have less energy than the reactants?"),
        QUIZ("A student mixes two solids in a beaker and the temperature falls from 28 degrees C to 21 degrees C. The reaction is...",
             ["exothermic, with a negative $\\Delta H$", "endothermic, with a positive $\\Delta H$", "exothermic, with a positive $\\Delta H$", "endothermic, with a negative $\\Delta H$"], 1,
             "Energy is taken from the surroundings, so the surroundings cool down. That is endothermic, and $\\Delta H$ is positive.",
             hint="Falling temperature means the reaction took in heat.",
             feedback=["Exothermic reactions warm the surroundings.", "", "The two signs are never paired like that.", "Endothermic reactions always have a positive $\\Delta H$."]),
        QUIZ("What is the effect of a catalyst on an energy profile?",
             ["It raises the activation energy", "It makes $\\Delta H$ more negative", "It lowers the activation energy", "It raises the products"], 2,
             "A catalyst provides an alternative route with a lower hump. The start and end levels do not change.",
             hint="Think of a tunnel through a hill instead of climbing over it.",
             feedback=["That would slow the reaction.", "$\\Delta H$ does not change with a catalyst.", "", "The product level is fixed by the chemistry, not by the catalyst."]),
        TIP("Exam link: energy profile diagrams, signs of $\\Delta H$ and the effect of a catalyst appear in Paper 1 multiple choice. Paper 2 can ask you to draw and label a profile for a given reaction.", title="Exam link"),
        PQ("Define an endothermic reaction and give one example.",
           "It takes in heat from the surroundings, so the temperature falls and $\\Delta H$ is positive. Example: thermal decomposition of calcium carbonate."),
        PQ("Sketch and label an energy profile diagram for an exothermic reaction.",
           "Draw reactants at a high level and products at a lower level, joined by a hump. Label the reactants, the products, the activation energy $E_a$ (reactants up to the top of the hump) and $\\Delta H$ (a downward arrow from reactants to products)."),
        PQ("Explain, using bonds, why burning methane is exothermic.",
           "Breaking the bonds in methane and oxygen takes in energy. Making the bonds in carbon dioxide and water gives out more energy. Since more energy is released than absorbed, the reaction is exothermic."),
        PQ("A reaction has $E_a$ = 60 kJ per mol and $\\Delta H$ = -70 kJ per mol. What is the activation energy of the reverse reaction?",
           "The products are 70 kJ per mol lower than the reactants. The hump is 60 kJ above the reactants, so it is 130 kJ above the products. $E_a(\\text{reverse}) = 60 + 70 = 130$ kJ per mol."),
        SUM("Exothermic reactions release heat: temperature rises, $\\Delta H$ is negative, products are lower in energy.",
            "Endothermic reactions absorb heat: temperature falls, $\\Delta H$ is positive, products are higher in energy.",
            "Bond breaking absorbs energy; bond making releases energy.",
            "Activation energy is the height of the hump from the reactants. $\\Delta H$ is the difference between products and reactants.",
            "A catalyst lowers the activation energy but does not change $\\Delta H$."),
    ],
))

# ------------------------------------------------------------------ 9. Enthalpy changes defined
LESSONS.append(lesson(
    module=M4,
    topic="Enthalpy changes",
    title="Enthalpy changes: combustion, neutralization, formation and solution",
    slug="chc-enthalpy-changes-defined",
    minutes=24,
    summary="Definitions of the standard enthalpy changes of combustion, neutralization, formation and solution, with their equations, typical values, and calculations of heat from moles and moles from heat.",
    objectives=[
        "Define enthalpy change of combustion, neutralization, formation and solution",
        "Write the equation that matches each definition",
        "Use heat = moles x enthalpy change to find the heat released or absorbed",
        "Compare fuels by the heat released per mole and per gram",
    ],
    key_concepts=["Enthalpy of combustion", "Enthalpy of neutralization", "Enthalpy of formation", "Enthalpy of solution", "Standard conditions", "Heat per mole"],
    blocks=[
        H("Introduction"),
        T("A household in Yaounde buys a 12.5 kg cylinder of cooking gas. How much heat is stored in it? Which fuel gives the most heat for its weight? "
          "To answer questions like these we use **enthalpy changes** per mole. They tell us how much heat a reaction releases or absorbs for a fixed amount of substance."),
        D("**Standard conditions** are a temperature of 298 K (25 degrees C) and a pressure of 100 kPa (about 1 atmosphere), with substances in their normal physical states. "
          "The symbol $\\Delta H^{\\ominus}$ marks a standard enthalpy change. Some books use 101 kPa; check your textbook.", title="Standard conditions"),
        H("Four enthalpy changes"),
        D("The **enthalpy change of combustion**, $\\Delta H_c$, is the heat change when **1 mol** of a substance burns **completely in oxygen**. It is always negative.", title="Combustion"),
        CODE("CH4(g) + 2O2(g)  ->  CO2(g) + 2H2O(l)        dHc = -890 kJ/mol\n"
             "C2H5OH(l) + 3O2(g) -> 2CO2(g) + 3H2O(l)     dHc = -1367 kJ/mol", "text", title="Examples (approximate values)"),
        D("The **enthalpy change of neutralization**, $\\Delta H_n$, is the heat change when an acid and an alkali react to form **1 mol of water**. "
          "For a strong acid and a strong alkali it is about -57 kJ per mol, because the reaction is always $\\mathrm{H^+ + OH^- \\rightarrow H_2O}$.", title="Neutralization"),
        CODE("H+(aq) + OH-(aq)  ->  H2O(l)        dHn = -57 kJ/mol", "text", title="The ionic equation"),
        D("The **enthalpy change of formation**, $\\Delta H_f$, is the heat change when **1 mol of a compound** is formed from its **elements** in their standard states.", title="Formation"),
        CODE("C(s) + O2(g)  ->  CO2(g)                dHf = -394 kJ/mol\n"
             "H2(g) + 1/2 O2(g)  ->  H2O(l)           dHf = -286 kJ/mol\n"
             "C(s) + 2H2(g)  ->  CH4(g)               dHf = -75 kJ/mol", "text", title="Examples (approximate values)"),
        T("The enthalpy of formation of an **element** in its standard state is **zero**, because nothing is formed. Fractions such as 1/2 $\\mathrm{O_2}$ are allowed in these equations, because the equation must show exactly 1 mol of product."),
        D("The **enthalpy change of solution**, $\\Delta H_{soln}$, is the heat change when **1 mol** of a substance dissolves in **so much water** that more water would make no further heat change.", title="Solution"),
        CODE("NaOH(s) -> Na+(aq) + OH-(aq)             dHsoln = about -44 kJ/mol   (warms)\n"
             "NH4NO3(s) -> NH4+(aq) + NO3-(aq)       dHsoln = about +26 kJ/mol   (cools)", "text", title="Examples (approximate values)"),
        TIP("The values in this lesson are rounded textbook values. Your textbook may give slightly different numbers. Use the numbers your question gives you."),
        H("Using enthalpy changes"),
        D("Heat released or absorbed = number of moles $\\times$ enthalpy change per mole.", title="Heat from moles",
          formula=r"\text{heat} = n \times |\Delta H|"),
        EX("Worked example 1: heat from burning methane", intro="How much heat is released when 3.2 g of methane burns completely? ($\\Delta H_c = -890$ kJ per mol; $A_r$: C = 12, H = 1.)", steps=[
            S("Relative molecular mass", math=r"M_r(\mathrm{CH_4}) = 12 + 4 = 16"),
            S("Moles", math=r"n = \frac{3.2}{16} = 0.20\ \mathrm{mol}"),
            S("Heat released", math=r"0.20 \times 890 = 178\ \mathrm{kJ}"),
        ]),
        EX("Worked example 2: the cooking gas cylinder", intro="Cooking gas is mainly butane, $\\mathrm{C_4H_{10}}$ ($\\Delta H_c = -2877$ kJ per mol). Estimate the heat released when the 12.5 kg of butane in a full cylinder is burned. ($A_r$: C = 12, H = 1.)", steps=[
            S("Relative molecular mass", math=r"M_r = 48 + 10 = 58"),
            S("Moles in 12 500 g", math=r"n = \frac{12\,500}{58} = 215.5\ \mathrm{mol}"),
            S("Heat", math=r"215.5 \times 2877 = 6.2 \times 10^5\ \mathrm{kJ}"),
        ]),
        EX("Worked example 3: which fuel gives more heat per gram?", intro="Compare hydrogen ($\\Delta H_c = -286$ kJ per mol, $M_r = 2$) with ethanol ($\\Delta H_c = -1367$ kJ per mol, $M_r = 46$).", steps=[
            S("Hydrogen per gram", math=r"\frac{286}{2} = 143\ \mathrm{kJ/g}"),
            S("Ethanol per gram", math=r"\frac{1367}{46} = 29.7\ \mathrm{kJ/g}"),
            S("Conclusion", text="Hydrogen gives about five times more heat per gram than ethanol. Ethanol has the larger value per mole only because each mole has more mass."),
        ]),
        H("Finding a reaction enthalpy from formation values (extension)"),
        T("Some courses use this idea. Check your syllabus. The enthalpy change of a reaction can be found from enthalpies of formation:"),
        F(r"\Delta H_{\text{reaction}} = \sum \Delta H_f(\text{products}) - \sum \Delta H_f(\text{reactants})"),
        CODE("CH4 + 2O2 -> CO2 + 2H2O\n"
             "dH = [(-394) + 2(-286)] - [(-75) + 2(0)]\n"
             "   = -966 - (-75) = -891 kJ/mol", "text", title="Check: burning methane"),
        T("The answer, $-891$ kJ per mol, is within rounding of the value $-890$ kJ per mol above."),
        MISTAKE("Forgetting \"1 mol\" in the definition", "Each definition fixes the amount: 1 mol burned, 1 mol of water formed, 1 mol of compound formed or 1 mol dissolved. Without it, the value changes with the amount used."),
        MISTAKE("Wrong equation for formation", "A formation equation must have the **elements** on the left and exactly **1 mol of the compound** on the right. $\\mathrm{2C + 4H_2 \\rightarrow 2CH_4}$ is not a formation equation."),
        QUIZ("Which equation represents the enthalpy change of formation of carbon dioxide?",
             ["$\\mathrm{CO + 1/2\\,O_2 \\rightarrow CO_2}$", "$\\mathrm{C(s) + O_2(g) \\rightarrow CO_2(g)}$", "$\\mathrm{CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O}$", "$\\mathrm{2C + 2O_2 \\rightarrow 2CO_2}$"], 1,
             "Formation: 1 mol of the compound from its elements in standard states. Carbon and oxygen are the elements.",
             hint="The left side must be elements only.",
             feedback=["CO is a compound, not an element.", "", "That is the combustion of methane.", "That makes 2 mol of the product, not 1."]),
        QUIZ("0.50 mol of ethanol is burned completely. $\\Delta H_c = -1367$ kJ per mol. How much heat is released?",
             ["2734 kJ", "1367 kJ", "683.5 kJ", "0.00037 kJ"], 2,
             "Heat = moles x $|\\Delta H_c|$ = $0.50 \\times 1367 = 683.5$ kJ.",
             hint="Multiply moles by the value per mole.",
             feedback=["That is for 2 mol.", "That is for 1 mol.", "", "You divided instead of multiplying."]),
        TIP("Exam link: definitions of the four enthalpy changes appear in Paper 1 multiple choice and in Paper 2 structured and essay questions, where you may need to write the matching equation and calculate heat. Learn the definitions word for word, including \"1 mol\".", title="Exam link"),
        PQ("Define the standard enthalpy change of formation of water.",
           "It is the heat change when 1 mol of water is formed from hydrogen and oxygen in their standard states. $\\mathrm{H_2(g) + 1/2\\,O_2(g) \\rightarrow H_2O(l)}$."),
        PQ("Calculate the heat released when 11.6 g of butane burns completely. ($\\Delta H_c = -2877$ kJ per mol; $M_r = 58$.)",
           "$n = 11.6 \\div 58 = 0.20$ mol. Heat $= 0.20 \\times 2877 = 575.4$ kJ."),
        PQ("What mass of ethanol must burn to release 683.5 kJ? ($\\Delta H_c = -1367$ kJ per mol; $M_r = 46$.)",
           "$n = 683.5 \\div 1367 = 0.50$ mol. Mass $= 0.50 \\times 46 = 23$ g."),
        PQ("Why is the enthalpy of neutralization about the same for any strong acid and any strong alkali?",
           "In every case the reaction is $\\mathrm{H^+ + OH^- \\rightarrow H_2O}$. Spectator ions do not take part, so the heat per mole of water is nearly the same."),
        SUM("The four standard enthalpy changes each refer to a fixed amount: 1 mol burned, 1 mol of water formed, 1 mol of compound formed, 1 mol dissolved.",
            "Combustion and neutralization are always negative. Formation and solution can be negative or positive.",
            "Heat released or absorbed = moles x enthalpy change per mole.",
            "Divide the enthalpy change per mole by $M_r$ to compare fuels per gram.",
            "The enthalpy of formation of an element in its standard state is zero."),
    ],
))

# ------------------------------------------------------------------ 10. Measuring enthalpy changes
LESSONS.append(lesson(
    module=M4,
    topic="Enthalpy changes",
    title="Measuring enthalpy changes with Q = mcΔT",
    slug="chc-measuring-enthalpy-calorimetry",
    minutes=25,
    summary="How to measure heat changes with a simple calorimeter using Q = mc delta T, calculate delta H for neutralization, solution and combustion experiments, explain sources of error and report an experiment.",
    objectives=[
        "Use Q = m c delta T to calculate the heat gained or lost by water or a solution",
        "Convert Q to delta H in kJ per mole and give the correct sign",
        "Describe how to measure the enthalpy change of neutralization, solution and combustion",
        "Explain sources of error and how to reduce them",
    ],
    key_concepts=["Calorimeter", "Specific heat capacity", "Q = mcΔT", "Heat loss", "Temperature change", "Experimental report"],
    blocks=[
        H("Introduction"),
        T("In the last lesson you used given values of $\\Delta H$. But where do those values come from? "
          "Chemists measure them. In a school laboratory you can do this with a polystyrene cup, a thermometer and a balance. "
          "The idea is simple: the heat given out by a reaction warms the water, and the heat taken in cools it. We measure the temperature change and calculate."),
        H("The heat equation"),
        D("The heat energy $Q$ gained or lost by a solution is found from its mass $m$, its specific heat capacity $c$ and its temperature change $\\Delta T$.", title="Q = mcΔT",
          formula=r"Q = m\,c\,\Delta T"),
        KEY("What each symbol means", "Use these values and units in your calculations.", cards=[
            ["Q", "Heat energy in joules (J). Divide by 1000 for kJ."],
            ["m", "Mass of the water or solution in grams. For dilute solutions use 1 cm3 = 1 g."],
            ["c", "Specific heat capacity: 4.2 joules per gram per kelvin (J per g per K) for water and dilute solutions. Some books use 4.18."],
            ["delta T", "Temperature change in kelvin or degrees C (the same size). Always final minus initial."],
        ]),
        IMG("f5ch-c-calorimeter.svg", alt="Insulated cup with a lid and thermometer containing a solution, with the formula Q = m c delta T",
            caption="Figure 1. A simple calorimeter."),
        T("After finding $Q$, find the **number of moles** of the substance that gave this heat. Then divide."),
        D("Enthalpy change per mole: $\\Delta H = -\\dfrac{Q}{n}$ if the temperature **rises** (exothermic, $\\Delta H$ negative). "
          "$\\Delta H = +\\dfrac{Q}{n}$ if the temperature **falls** (endothermic, $\\Delta H$ positive). Convert $Q$ to kJ.", title="From Q to delta H",
          formula=r"\Delta H = \pm \frac{Q}{n}"),
        H("Measuring neutralization"),
        T("Put a measured volume of acid in a polystyrene cup and record its temperature. Add the same volume of alkali of the same concentration, stir, and record the highest temperature."),
        EX("Worked example 1: enthalpy of neutralization", intro="25.0 cm3 of 2.00 mol per dm3 hydrochloric acid is mixed with 25.0 cm3 of 2.00 mol per dm3 sodium hydroxide. The temperature rises by 13.5 K. Calculate $\\Delta H_n$. (Assume $c$ = 4.2 J per g per K and 1 cm3 = 1 g.)", steps=[
            S("Mass of solution", math=r"m = 25.0 + 25.0 = 50.0\ \mathrm{g}"),
            S("Heat released", math=r"Q = 50.0 \times 4.2 \times 13.5 = 2835\ \mathrm{J} = 2.835\ \mathrm{kJ}"),
            S("Moles of water formed", math=r"n = 0.0250 \times 2.00 = 0.0500\ \mathrm{mol}"),
            S("Divide and give the sign", math=r"\Delta H = -\frac{2.835}{0.0500} = -56.7\ \mathrm{kJ/mol}", text="The sign is negative because the temperature rose."),
        ]),
        H("Measuring enthalpy of solution"),
        EX("Worked example 2: dissolving ammonium nitrate", intro="8.0 g of ammonium nitrate ($M_r = 80$) is dissolved in 100 g of water. The temperature falls by 6.2 K. Calculate $\\Delta H_{soln}$. (Use the mass of water as $m$.)", steps=[
            S("Heat absorbed", math=r"Q = 100 \times 4.2 \times 6.2 = 2604\ \mathrm{J} = 2.604\ \mathrm{kJ}"),
            S("Moles dissolved", math=r"n = \frac{8.0}{80} = 0.10\ \mathrm{mol}"),
            S("Divide and give the sign", math=r"\Delta H_{soln} = +\frac{2.604}{0.10} = +26.0\ \mathrm{kJ/mol}", text="The sign is positive because the temperature fell."),
        ]),
        H("Measuring enthalpy of combustion"),
        T("For a fuel, burn it in a spirit burner under a metal can of water. Weigh the burner before and after, to find the mass of fuel burned, and measure the temperature rise of the water."),
        EX("Worked example 3: burning ethanol", intro="A spirit burner burns 0.46 g of ethanol ($M_r = 46$). The heat warms 200 g of water by 9.0 K. Find $\\Delta H_c$ and compare it with the data book value of -1367 kJ per mol.", steps=[
            S("Heat gained by water", math=r"Q = 200 \times 4.2 \times 9.0 = 7560\ \mathrm{J} = 7.56\ \mathrm{kJ}"),
            S("Moles of ethanol burned", math=r"n = \frac{0.46}{46} = 0.010\ \mathrm{mol}"),
            S("Enthalpy change", math=r"\Delta H_c = -\frac{7.56}{0.010} = -756\ \mathrm{kJ/mol}"),
            S("Compare", text="The measured value is only about 55 percent of the data value. Much heat escaped to the air and the can."),
        ]),
        H("Errors and improvements"),
        KEY("Why experimental values differ", "Experimental values are usually smaller in size than data book values. Learn the causes and the fixes.", cards=[
            ["Heat loss to the surroundings", "Use a polystyrene cup with a lid. For combustion, use a draught shield and put the can close to the flame."],
            ["Heat taken by the container and thermometer", "Cannot be removed easily. Use a small mass of cup or allow for it."],
            ["Incomplete combustion of the fuel", "Soot on the can shows it. Use plenty of air and a clean flame."],
            ["Temperature reading error", "Stir well and read the maximum (or minimum) temperature. Use a thermometer with 0.1 degree divisions."],
            ["Assumptions", "We assume the solution has the density and heat capacity of water."],
        ]),
        KEY("How to report an experiment", "The Board's report notes that some candidates lack reporting skills. Use this order.", cards=[
            ["Aim and materials", "What you measure, and the apparatus and chemicals."],
            ["Procedure", "Numbered steps in the past tense or as clear instructions."],
            ["Results", "A table of masses, volumes and temperatures with units."],
            ["Calculation", "$Q$, then $n$, then $\\Delta H$ with sign and units."],
            ["Conclusion and errors", "State $\\Delta H$, compare with the data value and explain differences."],
        ]),
        MISTAKE("Using the mass of the solid in Q = mcΔT", "The heat goes into the **water or solution**, so $m$ is the mass of the solution (or water). Use the mass of the solid only to find moles."),
        MISTAKE("Wrong sign or unit", "Temperature up means $\\Delta H$ is negative. Convert joules to kilojoules before dividing by moles. State kJ per mol."),
        QUIZ("The temperature of 100 g of water rises by 5.0 K. What is $Q$? ($c$ = 4.2 J per g per K)",
             ["2100 J", "21 J", "84 J", "500 J"], 0,
             "$Q = 100 \\times 4.2 \\times 5.0 = 2100$ J.", hint="Multiply the three numbers.",
             feedback=["", "You forgot the 100 g.", "You divided instead of multiplying.", "You left out $c$."]),
        QUIZ("Why is a lid put on the cup in a neutralization experiment?",
             ["To stop heat escaping and make the measured temperature change more accurate", "To make the reaction faster", "To keep the acid from being spoiled", "To increase the volume"], 0,
             "Heat lost to the air makes the temperature rise look smaller, so a lid reduces this error.", hint="Where could the heat go?",
             feedback=["", "The lid does not change the rate noticeably.", "No spoiling happens.", "A lid does not add volume."]),
        TIP("Exam link: the Board's report on Chemistry Paper 2 notes questions on determining enthalpy changes and the related calculation, and says some candidates lack reporting skills. Practise calculations in the order Q, n, $\\Delta H$ and report with clear steps. This content also appears in Paper 1 multiple choice.", title="Exam link"),
        PQ("50 g of water is warmed by 8.0 K. Calculate the heat gained. ($c$ = 4.2 J per g per K.)",
           "$Q = 50 \\times 4.2 \\times 8.0 = 1680$ J."),
        PQ("100 cm3 of 1.0 mol per dm3 HCl is mixed with 100 cm3 of 1.0 mol per dm3 NaOH. The temperature rises by 6.8 K. Calculate $\\Delta H_n$.",
           "Mass $= 200$ g. $Q = 200 \\times 4.2 \\times 6.8 = 5712$ J $= 5.712$ kJ. Moles of water $= 0.100 \\times 1.0 = 0.10$ mol. $\\Delta H = -5.712/0.10 = -57.1$ kJ per mol."),
        PQ("4.0 g of sodium hydroxide ($M_r = 40$) dissolves in 50 g of water and the temperature rises by 21.0 K. Calculate $\\Delta H_{soln}$.",
           "$Q = 50 \\times 4.2 \\times 21.0 = 4410$ J $= 4.41$ kJ. $n = 4.0/40 = 0.10$ mol. $\\Delta H = -4.41/0.10 = -44.1$ kJ per mol."),
        PQ("Give two reasons why an experimental enthalpy of combustion is smaller in size than the data book value.",
           "Heat is lost to the surroundings (the air, the can and the burner). The fuel may burn incompletely, so less heat is released."),
        SUM("$Q = m c \\Delta T$ with $c$ = 4.2 J per g per K for water. $m$ is the mass of water or solution.",
            "$\\Delta H = \\pm Q/n$ in kJ per mol. Negative if the temperature rises, positive if it falls.",
            "Use equal volumes and concentrations in neutralization; the moles of water formed equal the moles of acid used.",
            "Heat loss and incomplete combustion make experimental combustion values smaller than data values.",
            "Report an experiment with aim, procedure, results table, calculation and conclusion."),
    ],
))

# ------------------------------------------------------------------ 11. Rate of reaction and collision theory
LESSONS.append(lesson(
    module=M4,
    topic="Rate of reaction and collision theory",
    title="Rate of reaction, collision theory and the factors that change rate",
    slug="chc-rate-collision-theory",
    minutes=25,
    summary="What rate of reaction means, how collision theory explains it, and how concentration, pressure, temperature, surface area, a catalyst and light change the rate, with choice of the right factor for a given reaction.",
    objectives=[
        "Define rate of reaction and calculate a mean rate from experimental data",
        "State and use the collision theory: collisions, activation energy and orientation",
        "Explain how concentration, pressure, temperature, surface area, catalysts and light change rate",
        "Choose the relevant factors for a given reaction",
    ],
    key_concepts=["Rate of reaction", "Collision theory", "Activation energy", "Effective collision", "Catalyst", "Surface area"],
    blocks=[
        H("Introduction"),
        T("In a village kitchen, a cook cuts yam into small pieces so that it cooks faster. Firewood is split into thin sticks to light a fire quickly. "
          "A fridge keeps tomatoes fresh for days. A firework explodes in a fraction of a second but an iron roof takes years to rust. "
          "Some reactions are fast and some are slow. The **rate of reaction** tells us how fast."),
        D("The **rate of reaction** is the change in the amount of a reactant or product per unit time. For a mean rate: "
          "$\\text{rate} = \\dfrac{\\text{change in amount}}{\\text{time taken}}$. Units may be cm3 per s (gas produced), g per s (mass lost) or mol per dm3 per s.", title="Rate of reaction",
          formula=r"\text{mean rate} = \frac{\text{change in amount}}{\text{time taken}}"),
        EX("Worked example 1: a mean rate", intro="48 cm3 of hydrogen is collected in the first 120 s of a reaction between magnesium and acid. Find the mean rate.", steps=[
            S("Use the formula", math=r"\text{mean rate} = \frac{48\ \mathrm{cm^3}}{120\ \mathrm{s}}"),
            S("Calculate", math=r"= 0.40\ \mathrm{cm^3/s}"),
        ]),
        H("Collision theory"),
        D("**Collision theory** says that a reaction can happen only when particles **collide**. A collision leads to reaction only if the particles have **at least the activation energy** and meet with the **right orientation**. "
          "Such a collision is called an **effective** (successful) collision.", title="Collision theory"),
        T("Most collisions are not effective. The particles just bounce apart. Anything that makes **more effective collisions per second** speeds up the reaction."),
        H("Factors that change the rate"),
        KEY("Concentration (and gas pressure)", "More particles in the same volume.", cards=[
            ["Higher concentration", "More particles per cm3, so collisions are more frequent, so more effective collisions per second."],
            ["Higher pressure (gases only)", "Gas particles are pushed closer together. This works like a higher concentration."],
        ]),
        KEY("Temperature", "Two effects at once.", cards=[
            ["Particles move faster", "They collide more often."],
            ["More particles have enough energy", "A larger fraction has energy at least equal to $E_a$. This is the main effect."],
        ]),
        IMG("f5ch-c-energy-distribution.svg", alt="Two curves of particle energy at a lower and a higher temperature, with a dashed line for the activation energy; the area to the right is larger for the higher temperature",
            caption="Figure 1. At a higher temperature, more particles have energy of at least $E_a$."),
        KEY("Surface area", "Matters when a solid reacts.", cards=[
            ["Smaller pieces", "A powder has many more particles at the surface than one lump of the same mass."],
            ["Effect", "More surface particles are exposed to collisions, so the rate rises. Example: powdered marble reacts faster with acid than marble chips."],
        ]),
        KEY("Catalyst", "A substance that speeds up a reaction without being used up.", cards=[
            ["How", "It gives an alternative route with a **lower activation energy**. More collisions are effective."],
            ["Examples", "Manganese(IV) oxide for hydrogen peroxide; iron in the Haber process; enzymes in living cells."],
        ]),
        KEY("Light", "Some reactions are started by light.", cards=[
            ["Photochemical reactions", "Light gives energy to particles. Examples: photosynthesis, silver salts darkening in photographic film, methane with chlorine."],
        ]),
        TIP("A catalyst does not change $\\Delta H$ or the amount of product. It only changes how fast the reaction reaches the same end point. Many reactions roughly double their rate for each 10 K rise in temperature, but this is only a rough rule. Check your textbook."),
        H("Choosing the right factor"),
        T("The Board's report on Chemistry Paper 2 notes that many candidates could not pick the right factor for a given reaction. Ask yourself what is reacting."),
        CODE("Reaction type                              Factors that matter\n"
             "Solid + solution (marble + acid)           surface area, concentration, temperature, catalyst\n"
             "Reaction between solutions only            concentration, temperature, catalyst (pressure has almost no effect)\n"
             "Reaction between gases                     pressure, concentration, temperature, catalyst\n"
             "Reaction started by light                  light intensity, as well as the above", "text", title="Which factors apply"),
        EX("Worked example 2: surface area", intro="Explain why powdered marble reacts faster with dilute hydrochloric acid than marble chips of the same mass.", steps=[
            S("Compare the surface", text="The powder has a much greater surface area. More marble particles are in contact with the acid."),
            S("Link to collisions", text="Acid particles collide with marble particles more frequently."),
            S("Link to rate", text="More effective collisions per second means a higher rate. The total amount of gas formed is the same, because the same mass of marble is used."),
        ]),
        EX("Worked example 3: temperature", intro="A reaction takes 120 s at 20 degrees C. Assuming the rate doubles for every 10 K rise, how long does it take at 50 degrees C?", steps=[
            S("Number of 10 K steps", math=r"(50 - 20) \div 10 = 3"),
            S("Rate factor", math=r"2^3 = 8\ \text{times faster}"),
            S("New time", math=r"120 \div 8 = 15\ \mathrm{s}"),
        ]),
        MISTAKE("Saying heat \"gives more collisions\" only", "Higher temperature does increase the number of collisions a little, but the main reason is that many **more particles have energy of at least $E_a$**. Always mention activation energy."),
        MISTAKE("Saying a catalyst gives particles more energy", "A catalyst does not add energy. It **lowers the activation energy**, so a larger fraction of the particles already have enough energy."),
        QUIZ("Which change would NOT speed up the reaction $\\mathrm{Mg(s) + 2HCl(aq) \\rightarrow MgCl_2(aq) + H_2(g)}$?",
             ["Using magnesium powder", "Using more concentrated acid", "Warming the acid", "Using a larger piece of magnesium ribbon of the same mass"], 3,
             "A bigger lump has less surface area for its mass, so the rate would not increase (it would fall).",
             hint="Which option makes the solid less finely divided?",
             feedback=["Powder has more surface area, so it is faster.", "More concentrated acid has more particles per volume.", "Heating gives more energy.", ""]),
        QUIZ("Why does increasing the temperature increase the rate of reaction?",
             ["It lowers the activation energy", "More particles have energy of at least the activation energy", "It increases the volume of the solution", "It changes the products"], 1,
             "At higher temperature, a much larger fraction of particles reach the activation energy, and they also collide more often.",
             hint="The activation energy stays the same. What changes?",
             feedback=["Only a catalyst lowers the activation energy.", "", "Heating does not increase the number of particles.", "The products stay the same."]),
        TIP("Exam link: collision theory and the factors affecting rate are tested in Paper 1 multiple choice. In Paper 2 the Board's report notes a question on factors that affect rate where candidates must choose the factors that suit a specific reaction, so practise explaining with collision theory.", title="Exam link"),
        PQ("State two conditions needed for particles to react when they collide.",
           "They must collide with at least the activation energy, and they must have the correct orientation."),
        PQ("Explain, using collision theory, why increasing the concentration of an acid increases the rate.",
           "There are more acid particles in each cm3. Collisions between particles are more frequent. So there are more effective collisions per second, and the rate increases."),
        PQ("Name three ways to speed up the reaction between zinc granules and dilute sulfuric acid.",
           "Use zinc powder (bigger surface area), use more concentrated acid, warm the acid. A catalyst such as a few drops of copper(II) sulfate solution also works."),
        PQ("Why does pressure not change the rate of a reaction between two aqueous solutions?",
           "Liquids and solids cannot be squeezed much. Changing pressure does not change their concentration, so it has almost no effect. Pressure matters for gases."),
        SUM("Rate = change in amount divided by time taken.",
            "Reaction needs effective collisions: enough energy ($\\geq E_a$) and the right orientation.",
            "Higher concentration, pressure (gases), surface area and temperature give more effective collisions per second.",
            "A catalyst lowers $E_a$; it is not used up and does not change $\\Delta H$ or the yield.",
            "Match the factor to the reaction: pressure only for gases, surface area only for solids."),
    ],
))

# ------------------------------------------------------------------ 12. Following rate: curves and experiments
LESSONS.append(lesson(
    module=M4,
    topic="Rate of reaction and collision theory",
    title="Following a reaction: rate curves and rate experiments",
    slug="chc-rate-curves-experiments",
    minutes=24,
    summary="How to measure reaction rate by gas volume or loss of mass, read the shape of a rate curve, find mean and initial rates, and compare curves for changes in conditions and in the amount of reactant.",
    objectives=[
        "Describe three ways of following the progress of a reaction",
        "Explain the shape of a volume-time or mass-time graph",
        "Calculate a mean rate between two times and an initial rate from a tangent",
        "Predict how a curve changes when concentration, temperature, surface area, a catalyst or the amount of reactant changes",
    ],
    key_concepts=["Rate curve", "Gradient", "Mean rate", "Initial rate", "Limiting reactant", "Final volume"],
    blocks=[
        H("Introduction"),
        T("A student at a school in Bafoussam wants to know how fast marble chips react with acid. She cannot watch the particles. "
          "But she can collect the gas that comes off and note the volume every few seconds. A graph of those readings is a **rate curve**. "
          "In this lesson you learn to read these curves and to explain them with collision theory."),
        H("Ways to follow a reaction"),
        KEY("Three common methods", "Choose the method that suits what changes during the reaction.", cards=[
            ["Volume of gas", "Collect the gas in a gas syringe or an upturned measuring cylinder. Record the volume at fixed times. Good for a metal with acid, or hydrogen peroxide with a catalyst."],
            ["Loss of mass", "Put the flask on a balance. If a gas escapes, the mass falls. Use cotton wool in the neck to stop spray leaving. Good for marble with acid (carbon dioxide escapes)."],
            ["Time for a colour or cloudiness change", "Time how long a mark under the flask takes to disappear when a solid forms, such as sulfur from sodium thiosulfate with acid. A shorter time means a faster rate."],
        ]),
        H("The shape of the curve"),
        T("Look at this typical set of results for the volume of gas made when excess acid reacts with a fixed mass of magnesium."),
        CODE("Time (s)           0    10    20    30    40    60   120\n"
             "Volume (cm3)       0    24    38    47    52    57    60", "text", title="Results"),
        IMG("f5ch-c-rate-curves.svg", alt="Four curves of gas volume against time: A rises fastest to 60 cm3, B is slower, C slowest, and D ends at 30 cm3",
            caption="Figure 1. Volume of gas against time for four experiments."),
        T("Three things to notice on every curve."),
        T("1. The curve is **steepest at the start**. At the start the reactants are at their highest concentration, so collisions are most frequent.\n\n"
          "2. The curve gets **less steep** as time passes. Reactant particles are used up, so the concentration falls and collisions become less frequent.\n\n"
          "3. The curve becomes **flat**. A flat line means the reaction has stopped because one reactant has run out. The volume at this point is the total volume of gas."),
        D("The **gradient** of a rate curve is the rate of reaction at that moment. A steeper line means a faster reaction.", title="Gradient and rate"),
        EX("Worked example 1: mean rates from the table", intro="Use the results above to find the mean rate between 0 and 10 s, and between 20 and 30 s.", steps=[
            S("0 to 10 s", math=r"\frac{24 - 0}{10} = 2.4\ \mathrm{cm^3/s}"),
            S("20 to 30 s", math=r"\frac{47 - 38}{10} = 0.9\ \mathrm{cm^3/s}"),
            S("Compare", text="The rate falls as the reactant is used up."),
        ]),
        EX("Worked example 2: initial rate from a tangent", intro="A tangent drawn to the curve at time zero passes through (0 s, 0 cm3) and reaches the 60 cm3 level at 20 s. Find the initial rate.", steps=[
            S("Gradient of the tangent", math=r"\frac{60 - 0}{20 - 0} = 3.0\ \mathrm{cm^3/s}"),
            S("Meaning", text="The rate at the start is 3.0 cm3 per s. It is bigger than any of the mean rates in the table."),
        ]),
        H("Comparing curves"),
        T("In Figure 1, curve B is the original experiment. How do the others differ?"),
        CODE("Curve A: steeper, same final volume   -> faster: higher concentration, higher temperature,\n"
             "                                          powder instead of lumps, or a catalyst\n"
             "Curve C: less steep, same final volume -> slower: lower concentration, lower temperature,\n"
             "                                          or larger lumps\n"
             "Curve D: lower final volume            -> less of the limiting reactant was used", "text", title="Reading the curves"),
        D("The **limiting reactant** is the reactant that is used up first. It decides the total amount of product. "
          "Changing only the **rate** (temperature, surface area, catalyst) does **not** change the final volume. Changing the **amount** of the limiting reactant does.", title="Limiting reactant"),
        EX("Worked example 3: hydrogen peroxide and a catalyst", intro="20 cm3 of 0.20 mol per dm3 hydrogen peroxide decomposes with a manganese(IV) oxide catalyst: $\\mathrm{2H_2O_2 \\rightarrow 2H_2O + O_2}$. What total volume of oxygen is collected at room temperature and pressure? (1 mol of gas occupies 24 000 cm3.)", steps=[
            S("Moles of hydrogen peroxide", math=r"n = 0.020 \times 0.20 = 0.0040\ \mathrm{mol}"),
            S("Moles of oxygen (ratio 2 : 1)", math=r"0.0040 \div 2 = 0.0020\ \mathrm{mol}"),
            S("Volume of oxygen", math=r"0.0020 \times 24\,000 = 48\ \mathrm{cm^3}"),
            S("Effect of the catalyst", text="With the catalyst the 48 cm3 is reached much sooner, but the final volume is still 48 cm3."),
        ]),
        MISTAKE("Saying a faster reaction gives more product", "Rate and yield are different. Warming the acid makes the reaction faster, but with the same mass of the limiting reactant the final volume is the **same**. The curve is steeper but ends at the same height."),
        MISTAKE("Drawing curves that start at different places", "All volume-time curves start at the origin (0, 0). The curves differ in how steeply they rise and in where they flatten."),
        QUIZ("On a volume-time graph, what does a flat horizontal part of the curve show?",
             ["The reaction is at its fastest", "The reaction has stopped because a reactant is used up", "A catalyst has been added", "The temperature has fallen"], 1,
             "No more gas is being made, so the reaction has finished.",
             hint="What does a gradient of zero mean for the rate?",
             feedback=["The fastest reaction is where the curve is steepest.", "", "A catalyst changes the steepness, not the flatness.", "A fall in temperature would only slow the curve."]),
        QUIZ("Experiment 1 uses 1.0 g of magnesium ribbon with excess acid. Experiment 2 uses 1.0 g of magnesium powder with the same excess acid. Compared with experiment 1, the curve for experiment 2...",
             ["is steeper and ends at the same volume", "is steeper and ends at a higher volume", "is less steep and ends at the same volume", "is the same"], 0,
             "Powder has more surface area, so the rate is higher. The mass of magnesium is the same, so the total volume is the same.",
             hint="Surface area changes the rate. What decides the final volume?",
             feedback=["", "The same mass of magnesium gives the same total gas.", "Powder reacts faster, not slower.", "The surface area differs, so the curves differ."]),
        TIP("Exam link: rate graphs appear in Paper 1 multiple choice and in Paper 2 structured and alternative-to-practical questions, where you may draw curves, calculate rates and name apparatus. When you draw a second curve, label which experiment it belongs to.", title="Exam link"),
        PQ("Why does the gradient of a gas-volume graph decrease with time?",
           "The reactants are used up, so their concentration falls. There are fewer effective collisions per second and the rate decreases."),
        PQ("Use the table in this lesson to find the mean rate between 40 s and 60 s.",
           "$(57 - 52) \\div (60 - 40) = 5 \\div 20 = 0.25$ cm3 per s."),
        PQ("Describe how you could follow the reaction between marble chips and dilute hydrochloric acid by loss of mass. Why is cotton wool used?",
           "Put the flask with the acid and chips on a balance. Plug the neck with cotton wool. Record the mass at fixed times. The mass falls as carbon dioxide escapes. The cotton wool lets the gas out but stops acid spray leaving."),
        PQ("Sketch how the curve changes if the experiment is repeated with half the volume of the same acid, which is the limiting reactant.",
           "The curve starts at the origin with about the same initial gradient, but it flattens at half the original final volume."),
        SUM("Rate can be followed by volume of gas, loss of mass or time for a colour or cloudiness change.",
            "On a rate curve the gradient is the rate: steepest at the start, flat when a reactant is used up.",
            "Mean rate = change in volume divided by change in time. Initial rate = gradient of the tangent at time zero.",
            "Rate changes (temperature, surface area, catalyst) alter the steepness. Changes in the amount of limiting reactant alter the final volume.",
            "Always start curves at the origin and label them."),
    ],
))

# ------------------------------------------------------------------ 13. Reversible reactions and equilibrium
LESSONS.append(lesson(
    module=M4,
    topic="Reversible reactions and equilibrium",
    title="Reversible reactions, dynamic equilibrium and Le Chatelier's principle",
    slug="chc-reversible-equilibrium-le-chatelier",
    minutes=26,
    summary="Reversible reactions, what dynamic equilibrium means, and how Le Chatelier's principle predicts the effect of concentration, pressure, temperature and a catalyst on the position of equilibrium and the yield.",
    objectives=[
        "Explain what a reversible reaction and a dynamic equilibrium are",
        "State Le Chatelier's principle",
        "Predict the effect of changing concentration, pressure and temperature on the position of equilibrium",
        "Explain why a catalyst does not change the position of equilibrium and distinguish yield from rate",
    ],
    key_concepts=["Reversible reaction", "Dynamic equilibrium", "Position of equilibrium", "Le Chatelier's principle", "Yield", "Closed system"],
    blocks=[
        H("Introduction"),
        T("Most reactions you have met go in one direction: wood burns to ash and gases, and ash does not turn back into wood. "
          "But some reactions can go **both ways**. Blue crystals of copper(II) sulfate lose water when heated and turn white. Add water and they turn blue again. "
          "Ammonia, which is used to make fertilizers for farms, is made in a reaction that goes both ways. Understanding this helps chemists get more product."),
        D("A **reversible reaction** is a reaction in which the products can react to form the reactants again. It is shown with the sign $\\rightleftharpoons$.", title="Reversible reaction"),
        CODE("CuSO4.5H2O  <=>  CuSO4 + 5H2O\n"
             "2NO2  <=>  N2O4                 (brown gas <=> colourless gas)\n"
             "N2 + 3H2  <=>  2NH3             (the Haber process)\n"
             "H2 + I2  <=>  2HI", "text", title="Examples of reversible reactions"),
        H("Dynamic equilibrium"),
        T("Put reactants in a **closed system**, where nothing can escape. At first only the forward reaction takes place and its rate is high. Products form and start to react backwards. "
          "The forward rate falls and the reverse rate rises, until they become **equal**."),
        D("**Dynamic equilibrium** is the state of a reversible reaction in a closed system when the rate of the forward reaction equals the rate of the reverse reaction. "
          "The concentrations of reactants and products stay constant, but both reactions are still going on.", title="Dynamic equilibrium"),
        IMG("f5ch-c-equilibrium-rates.svg", alt="Graph of reaction rate against time: the forward rate falls and the reverse rate rises until they meet and stay equal",
            caption="Figure 1. At equilibrium the forward and reverse rates are equal."),
        TIP("\"Dynamic\" means that the particles keep reacting in both directions. The reaction has not stopped. It looks still only because the amounts do not change."),
        D("The **position of equilibrium** tells us how much product and reactant are present. If it lies **to the right**, there is more product (a high **yield**). If it lies **to the left**, there is more reactant.", title="Position of equilibrium"),
        H("Le Chatelier's principle"),
        D("**Le Chatelier's principle**: if a change is made to a system at equilibrium, the position of equilibrium shifts so as to **oppose** (reduce) the change.", title="Le Chatelier's principle"),
        KEY("Four changes", "Apply each rule to a reaction you are given.", cards=[
            ["Concentration", "Add a reactant, or remove a product: the position shifts to the **right** (more product). Add a product: it shifts to the left."],
            ["Pressure (gases only)", "Higher pressure shifts the position to the side with **fewer moles of gas**. Lower pressure shifts it to the side with more moles. If the moles are equal, there is no shift."],
            ["Temperature", "Raising the temperature shifts the position in the **endothermic** direction. Lowering it shifts the position in the **exothermic** direction."],
            ["Catalyst", "No effect on the position. It speeds up the forward and reverse reactions equally, so equilibrium is reached sooner."],
        ]),
        T("These are the same factors that affect the rate, but the effects are explained differently. For rate, we use collision theory. For the position of equilibrium, we use Le Chatelier's principle."),
        H("Worked applications"),
        EX("Worked example 1: the Haber process", intro="$\\mathrm{N_2(g) + 3H_2(g) \\rightleftharpoons 2NH_3(g)}$, $\\Delta H = -92$ kJ per mol (forward reaction exothermic). Predict the effect on the yield of ammonia of (a) a higher pressure, (b) a higher temperature, (c) removing ammonia as it forms.", steps=[
            S("(a) Pressure", text="Left side: 1 + 3 = 4 mol of gas. Right side: 2 mol. Higher pressure shifts the position to the right, so the yield of ammonia increases."),
            S("(b) Temperature", text="The forward reaction is exothermic. A higher temperature favours the endothermic (reverse) direction, so the position shifts to the left and the yield decreases."),
            S("(c) Removing ammonia", text="Removing a product shifts the position to the right to replace it, so more ammonia forms."),
        ]),
        T("In the real Haber process, a compromise is used: about 450 degrees C and about 200 atmospheres, with an iron catalyst. A lower temperature would give a higher yield but would be too slow. The catalyst makes the reaction fast enough. You will meet this again in the lessons on nitrogen."),
        EX("Worked example 2: nitrogen dioxide", intro="$\\mathrm{2NO_2(g) \\rightleftharpoons N_2O_4(g)}$, $\\Delta H = -57$ kJ per mol. $\\mathrm{NO_2}$ is brown and $\\mathrm{N_2O_4}$ is colourless. What is seen when a sealed tube of the mixture is (a) cooled in ice water, (b) compressed?", steps=[
            S("(a) Cooling", text="The forward reaction is exothermic. Cooling favours the exothermic direction, so more $\\mathrm{N_2O_4}$ forms and the mixture becomes paler."),
            S("(b) Compressing", text="Left side: 2 mol of gas. Right side: 1 mol. Higher pressure shifts to the right. Note that the tube first looks darker, because the same gas is squeezed into a smaller space, and then becomes paler as equilibrium shifts."),
        ]),
        EX("Worked example 3: no effect of pressure", intro="$\\mathrm{H_2(g) + I_2(g) \\rightleftharpoons 2HI(g)}$. What is the effect of increasing the pressure?", steps=[
            S("Count moles of gas", text="Left: 1 + 1 = 2 mol. Right: 2 mol."),
            S("Conclusion", text="Both sides have the same number of moles of gas, so a change in pressure does not shift the position of equilibrium."),
        ]),
        MISTAKE("Mixing up yield and rate", "The Board's report notes that candidates confused the yield with the position of equilibrium and with the effect of a catalyst. "
                "**Yield** depends on the position of equilibrium. **Rate** depends on how fast equilibrium is reached. A catalyst changes the rate but not the position or the yield at equilibrium."),
        MISTAKE("Saying a catalyst increases the yield", "A catalyst speeds up both directions equally. The equilibrium mixture is the same, but it is reached faster."),
        MISTAKE("Ignoring state symbols for pressure", "Only **gases** count when you compare moles for pressure changes. Count the moles of gas on each side, not solids or liquids."),
        QUIZ("In $\\mathrm{2SO_2(g) + O_2(g) \\rightleftharpoons 2SO_3(g)}$, increasing the pressure will...",
             ["shift the position to the left", "have no effect on the position", "shift the position to the right", "lower the rate"], 2,
             "Left: 3 mol of gas. Right: 2 mol of gas. High pressure favours the side with fewer moles, so the position shifts to the right and the yield of $\\mathrm{SO_3}$ increases.",
             hint="Count the moles of gas on each side.",
             feedback=["That would be the side with more moles of gas.", "That is true only when the moles are equal on both sides.", "", "Higher pressure increases the rate."]),
        QUIZ("What is the effect of a catalyst on a reaction at equilibrium?",
             ["It shifts the position to the right", "It shifts the position to the left", "It does not change the position of equilibrium", "It stops the reverse reaction"], 2,
             "A catalyst speeds up both directions equally. The equilibrium position is the same, but it is reached sooner.",
             hint="A catalyst changes the route, not the energy levels of reactants and products.",
             feedback=["Only changes in concentration, pressure or temperature can shift the position.", "Only changes in concentration, pressure or temperature can shift the position.", "", "It speeds up the reverse reaction too."]),
        TIP("Exam link: the Board's report on Paper 2 records a question on reversibility and its use in industrial processes, where candidates could not separate yield from equilibrium position and misjudged the role of a catalyst. Reversible reactions and Le Chatelier's principle also appear in Paper 1 multiple choice. Explain every answer with Le Chatelier's principle, not just a bare statement.", title="Exam link"),
        PQ("Define dynamic equilibrium.",
           "It is the state in a closed system when the forward and reverse reactions occur at the same rate, so the concentrations of reactants and products stay constant."),
        PQ("For $\\mathrm{N_2 + 3H_2 \\rightleftharpoons 2NH_3}$ ($\\Delta H = -92$ kJ per mol), state and explain the effect of lowering the temperature on the yield at equilibrium.",
           "Lowering the temperature favours the exothermic (forward) direction, so the position shifts to the right and the yield of ammonia increases. (The rate, however, becomes slower.)"),
        PQ("Why is a catalyst used in the Haber process if it does not change the yield at equilibrium?",
           "It makes the equilibrium be reached much faster, so the process can be run at a temperature low enough for a good yield but with a reasonable rate."),
        PQ("Use Le Chatelier's principle to say what happens to $\\mathrm{2NO_2 \\rightleftharpoons N_2O_4}$ ($\\Delta H = -57$ kJ per mol) when the mixture is heated.",
           "Heating favours the endothermic (reverse) direction, so the position shifts to the left. More brown $\\mathrm{NO_2}$ forms and the colour darkens."),
        SUM("A reversible reaction can go in both directions ($\\rightleftharpoons$). Equilibrium is reached in a closed system when the forward and reverse rates are equal.",
            "At dynamic equilibrium the concentrations stay constant, but the reactions have not stopped.",
            "Le Chatelier: the position shifts to oppose any change made to the system.",
            "More reactant or less product shifts right. Higher pressure favours fewer moles of gas. Higher temperature favours the endothermic direction.",
            "A catalyst does not change the position or the yield. It only makes equilibrium arrive sooner."),
    ],
))
