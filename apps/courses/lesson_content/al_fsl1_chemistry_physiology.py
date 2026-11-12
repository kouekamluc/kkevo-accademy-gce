"""A Level Food Science and Nutrition (0740), Lower Sixth: Food Chemistry of Macronutrients; Micronutrients, Pigments,
Enzymes & Dispersions; Human Physiology, Metabolism & Energy Balance. 14 lessons, one practice set each (see the practice
file of the same name).

Scope notes: the outline comes from KKEVO's master curriculum blueprint, not a Board syllabus booklet. Facts are standard
A Level ones; where textbooks differ the lesson says "check your textbook". Numbers in worked data are teaching data and
are labelled; food composition values are invented for practice. Exam comments paraphrase the GCE Board's 2023 Advanced
Level subject report.
"""

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "lower-sixth")

M1 = "Food Chemistry of Macronutrients"
M2 = "Micronutrients, Pigments, Enzymes & Dispersions"
M3 = "Human Physiology, Metabolism & Energy Balance"

LESSONS = []

# ------------------------------------------------------------------ 1. Water activity
LESSONS.append(lesson(
    module=M1,
    topic="Water activity",
    title="Water activity, moisture sorption isotherms and food stability",
    slug="fsl1-water-activity",
    minutes=24,
    summary="Water activity (aw) measures how freely the water in a food can take part in growth and reactions. Learn the definition, the sorption isotherm, how aw controls spoilage and chemical change, and how to calculate it.",
    objectives=[
        "Define water activity and relate it to equilibrium relative humidity",
        "Distinguish water content from water activity and bound water from free water",
        "Read a moisture sorption isotherm, including its three regions and hysteresis",
        "Explain how aw limits microbial growth and affects lipid oxidation, browning and enzyme action, and calculate aw from composition",
    ],
    key_concepts=["Water activity", "Equilibrium relative humidity", "Bound and free water", "Sorption isotherm", "Hysteresis",
                  "Intermediate-moisture foods", "Humectant"],
    blocks=[
        H("Introduction"),
        T("Dried cassava chips, honey, salted fish and jam can all sit on a shelf for months, yet fresh tomatoes, cooked rice and "
          "raw fish spoil in a day. Honey contains around 17 to 20 percent water, far more than a dry biscuit, and still it does not go "
          "mouldy. So the **amount** of water is not what matters most. What matters is how **available** the water is. Food scientists "
          "measure that availability with **water activity**."),
        D(r"The **water activity** of a food is the ratio of the water vapour pressure above the food to the vapour pressure above pure water at the same temperature: $a_w = p/p_0$. It runs from 0 (no available water) to 1 (pure water).",
          title="Water activity (aw)", formula=r"a_w = \frac{p}{p_0} = \frac{\text{ERH}}{100}"),
        T("The **equilibrium relative humidity (ERH)** is the relative humidity of the air that is in balance with the food in a sealed "
          "space, so neither gains nor loses water. A food at $a_w = 0.65$ is in balance with air at 65 percent relative humidity. "
          "In a more humid room it will take up water; in a drier room it will dry out."),
        H("Water content is not water activity"),
        T("**Moisture content** is the total mass of water as a percentage of the food (wet basis) or of the dry solids (dry basis). "
          "Two foods with the same moisture content can have very different water activity, because water is held differently. "
          "**Bound water** is attracted to polar groups on starch, protein and sugar molecules and to dissolved solutes, so it is not free "
          "to evaporate, freeze easily or be used by microbes. **Free water** is held loosely in capillaries and between structures and "
          "behaves almost like pure water."),
        EX("Worked example 1: moisture content on two bases", intro="A grain sample contains 12 percent water on a wet basis. Express this on a dry basis. (Teaching data.)", steps=[
            S("Take 100 g of grain", text="It holds 12 g of water and 88 g of dry solids."),
            S("Divide water by dry solids", math=r"\frac{12}{88} \times 100 = 13.6\%"),
            S("State it", text="Dry-basis moisture is 13.6 percent. Always say which basis is used: the number is larger on the dry basis."),
        ], check=r"13.64\% \text{ of } 88 \approx 12"),
        H("Raoult's law: aw from composition"),
        T("Dissolved solutes lower the vapour pressure because they hold on to water molecules. For a dilute solution that behaves "
          "ideally, **Raoult's law** gives $a_w$ as the mole fraction of water. Real foods are not ideal, so this is a good estimate only "
          "for dilute sugar or salt solutions, and the real aw of concentrated foods is measured."),
        F(r"a_w \approx \frac{n_{\text{water}}}{n_{\text{water}} + n_{\text{solute}}}"),
        T("Salt gives two particles per formula unit (Na+ and Cl-), so a mole of salt lowers aw about twice as much as a mole of sugar. "
          "That is one reason salt preserves fish and meat so well."),
        EX("Worked example 2: aw of a sugar syrup", intro="A syrup contains 34.2 g of sucrose (molar mass 342 g/mol) in 100 g of water (molar mass 18 g/mol). Estimate its water activity.", steps=[
            S("Moles of sucrose", math=r"\frac{34.2}{342} = 0.100 \text{ mol}"),
            S("Moles of water", math=r"\frac{100}{18.015} = 5.55 \text{ mol}"),
            S("Mole fraction of water", math=r"a_w \approx \frac{5.55}{5.55 + 0.100} = 0.982"),
            S("Interpret", text="At 0.98 many bacteria still grow, so a thin syrup is not safe by aw alone. Doubling the sugar lowers aw only slightly, which is why jam needs a very high sugar content (more than 60 percent) to reach about 0.80 to 0.85."),
        ]),
        H("The moisture sorption isotherm"),
        T("A **moisture sorption isotherm** plots equilibrium moisture content (vertical axis) against water activity (horizontal axis) at "
          "one fixed temperature. Most foods give an S-shaped (sigmoid) curve with three regions."),
        IMG("alfsl1-sorption-isotherm.svg", alt="Sigmoid sorption isotherm of moisture content against water activity, with region I (monolayer, about 0 to 0.25), region II (multilayer, about 0.25 to 0.75) and region III (free water, above about 0.75), and a desorption curve above the adsorption curve showing hysteresis",
            caption="Figure 1. A typical moisture sorption isotherm with its three regions and hysteresis."),
        KEY("The three regions (boundaries are approximate; check your textbook)", "Water is held more and more loosely as aw rises.", cards=[
            ["Region I: monolayer water", "Below about aw 0.2 to 0.3. Water forms a single layer on polar sites, is very tightly bound, does not freeze and cannot act as a solvent."],
            ["Region II: multilayer water", "From about 0.3 to 0.7. Water forms further layers, begins to dissolve solutes and allows reactions to speed up."],
            ["Region III: free water", "Above about 0.7 to 0.8. Water is held in capillaries and solutions, behaves like bulk water and supports microbial growth and fast reactions."],
        ]),
        T("**Hysteresis** means that the curve for drying (desorption) lies above the curve for wetting (adsorption): at the same aw "
          "the food holds more water when it is being dried than when it is being rewetted. The loop arises from structural changes "
          "and capillary effects. The practical lesson: you must state whether an isotherm is for adsorption or desorption."),
        H("Why aw controls stability"),
        KEY("Approximate lowest aw for growth (values vary slightly with the source and conditions)", "Microbes need available water.", cards=[
            ["Most spoilage bacteria", "About 0.91. Clostridium botulinum needs about 0.94 or more. Staphylococcus aureus can grow down to about 0.86 in air."],
            ["Most yeasts", "About 0.88. Osmophilic yeasts that spoil syrups and honey can tolerate about 0.60 to 0.65."],
            ["Most moulds", "About 0.80. Xerophilic (dry-loving) moulds can grow near 0.65."],
            ["Halophilic bacteria", "About 0.75, in very salty foods."],
        ]),
        T("Chemical and enzymic change also depend on aw. **Lipid oxidation** is slowest near the monolayer value (about 0.2 to 0.4) and "
          "speeds up both when the food is drier (the protective water film is gone and fat is exposed to oxygen) and when it is wetter "
          "(dissolved catalysts move freely). **Non-enzymic browning** (Maillard) is fastest at intermediate aw, about 0.5 to 0.8. "
          "**Enzyme activity** and hydrolytic reactions rise steadily with aw once water can act as a solvent. Texture changes too: biscuits and "
          "crisps turn soft when aw rises above their critical value, around 0.4 to 0.5."),
        T("**Intermediate-moisture foods** have aw of about 0.6 to 0.9: jam, dried fruit, soft sweets, smoked and salted fish. They are "
          "stabilised by **humectants** (sugar, salt, glycerol, sorbitol), which hold water and lower aw, often combined with acid, "
          "mild heat or preservatives such as sorbic acid. This is the idea of hurdle technology: several small barriers together stop growth."),
        MISTAKE("Using moisture content and aw as if they were the same", "A food can be 17 percent water and still be safe if the water is tied up by sugars (honey), and a food of 60 percent water can have aw above 0.99. Safety limits are written in aw, not in moisture percent. Also remember aw has no units."),
        EX("Worked example 3: choosing a safe storage condition", intro="A dried fish has aw 0.72 at 28 degrees Celsius. Storage air in the market stall is at 85 percent relative humidity. What happens, and why?", steps=[
            S("Compare aw with ERH of the air", text="The food is at ERH 72 percent; the air is at 85 percent."),
            S("Direction of water movement", text="Air is more humid than the food, so the fish absorbs water vapour and its aw rises."),
            S("Consequence", text="As aw passes about 0.75 to 0.80 moulds and halophilic bacteria can grow, and fat oxidation and enzymic change speed up."),
            S("Remedy", text="Store in a sealed, moisture-proof container in a dry place, or dry the fish further, so that its aw stays below about 0.65 to 0.70."),
        ]),
        QUIZ("A snack has aw 0.30 and a biscuit has aw 0.30. Honey has aw about 0.55 to 0.60 but 17 percent water. Which statement is correct?",
             ["Honey is unsafe because it contains more water than the biscuit", "Honey resists spoilage because its water is bound by sugars, so aw, not water content, decides", "Water content and aw always rank foods in the same order", "aw of honey must be above 0.9 because it is liquid"], 1,
             "Honey is a concentrated sugar solution, so much of its water is tied to sugar molecules and its aw is low, which prevents microbes from growing.",
             hint="Which measurement tells you how available the water is?",
             feedback=["Total water content does not decide growth.", "", "Foods with the same water content can have very different aw.", "A liquid can have low aw if solutes hold the water."]),
        QUIZ("Which food would you expect to spoil first by bacterial growth at room temperature?",
             ["Dried cassava chips, aw 0.55", "Strawberry jam, aw 0.82", "Fresh cooked rice, aw 0.98", "Salted dried fish, aw 0.70"], 2,
             "Cooked rice has aw near 0.98, far above the 0.91 limit for most bacteria. The others are below this value.",
             hint="Compare each aw with 0.91.",
             feedback=["At 0.55 no common bacteria can grow.", "At 0.82 bacteria cannot grow, though some moulds could.", "", "At 0.70 only very salt- or dry-tolerant organisms can grow."]),
        H("Practice"),
        PQ("Define water activity and state the relationship between water activity and equilibrium relative humidity.", "Water activity is the ratio of the vapour pressure of water above the food to the vapour pressure of pure water at the same temperature (aw = p/p0). It equals the equilibrium relative humidity divided by 100: a food at aw 0.80 is in balance with air at 80 percent relative humidity. It has no units and runs from 0 to 1."),
        PQ("A syrup contains 0.20 mol of glucose and 100 g of water. Estimate its aw using Raoult's law.", "Moles of water = 100 / 18.015 = 5.55. aw is about 5.55 / (5.55 + 0.20) = 0.965. A thin glucose syrup is still above the limit for most bacteria, so it would need more solute, acid or preservative to be stable."),
        PQ("Explain why the sorption isotherm of a food shows hysteresis and why this matters in food storage.", "At a given aw the food holds more water when it is dried (desorption) than when it is wetted (adsorption), so the desorption curve lies above the adsorption curve. Causes include structural changes of the solids during drying and capillary effects. In storage it means a product dried to a safe moisture content may take up water at a different level if rewetted, so the isotherm direction must be stated and packaging chosen to prevent moisture pick-up."),
        PQ("Essay plan: 'Discuss how water activity influences the shelf life of foods.'", "Introduction: define aw and the isotherm. Point 1: microbial limits (bacteria 0.91, yeasts 0.88, moulds 0.80, with exceptions) and the link to hurdle technology. Point 2: chemical changes (lipid oxidation minimum near the monolayer, Maillard maximum at intermediate aw, enzymes rising with aw). Point 3: physical changes (crispness lost, caking). Point 4: ways to lower aw: drying, salt, sugar, humectants, freezing. Evaluation: aw alone is not enough, since pH, temperature, oxygen and preservatives interact, and some microbes tolerate low aw. Conclusion."),
        TIP("Exam link: water activity appears in Paper 1 multiple choice (definition, limits for growth, reading the isotherm) and in Paper 2 food-science essays on preservation and spoilage. Always say what the isotherm axes are and quote approximate limits with the word 'about'."),
        SUM("Water activity is vapour pressure over the food divided by that over pure water, equal to ERH divided by 100.",
            "Water content is not water activity: bound water is unavailable, free water is available to microbes and reactions.",
            "Sorption isotherms are S-shaped with monolayer, multilayer and free-water regions, and show hysteresis between adsorption and desorption.",
            "Most bacteria need aw above about 0.91, yeasts 0.88 and moulds 0.80; lowering aw with drying, salt or sugar preserves food.",
            "Lipid oxidation, Maillard browning and enzymes each depend on aw in their own way."),
    ],
))

# ------------------------------------------------------------------ 2. Carbohydrate functional properties
LESSONS.append(lesson(
    module=M1,
    topic="Carbohydrate functional properties",
    title="Starch, sugars and pectin: gelatinization, retrogradation, dextrinization, caramelization and gels",
    slug="fsl1-carbohydrate-functional-properties",
    minutes=25,
    summary="Carbohydrates thicken, gel, brown and sweeten. Learn amylose and amylopectin, gelatinization, retrogradation, dextrinization, caramelization and pectin gel formation in jam.",
    objectives=[
        "Describe the structure of amylose and amylopectin and relate it to starch behaviour",
        "Explain gelatinization and retrogradation and the factors that affect them",
        "Distinguish dextrinization from caramelization and from Maillard browning",
        "Explain how high-methoxyl and low-methoxyl pectin form gels and calculate a jam endpoint",
    ],
    key_concepts=["Amylose and amylopectin", "Gelatinization", "Retrogradation", "Syneresis", "Dextrinization", "Caramelization", "Pectin gel"],
    blocks=[
        H("Introduction"),
        T("A pot of pap (ogi) thickens as it heats. Left overnight, cooked yam goes firm and a gel forms on cold porridge. Bread goes "
          "stale in two days. A roux turns nutty brown in the pan. Jam sets in the jar. All of these are the **functional properties** "
          "of carbohydrates: what they do in food beyond supplying energy."),
        H("Starch structure"),
        D("**Starch** is stored by plants as insoluble granules. It contains two polymers of glucose. **Amylose** is a mostly linear chain "
          "of glucose units joined by alpha-1,4 bonds, which coils into a helix. **Amylopectin** is a large branched molecule with alpha-1,4 chains and "
          "alpha-1,6 branch points about every 20 to 30 units.", title="Amylose and amylopectin"),
        T("Most starches have about 20 to 30 percent amylose and the rest amylopectin. Waxy varieties are almost all amylopectin, and "
          "high-amylose varieties exist (exact values vary, check your textbook). Cassava, yam, maize, plantain, rice and potato starches "
          "differ in granule size and in amylose content, which is why they thicken and gel differently."),
        H("Gelatinization"),
        D("**Gelatinization** is the irreversible swelling of starch granules in hot water. The ordered crystalline regions melt, the granules "
          "absorb water and swell many times their size, some amylose leaches out, and the paste becomes viscous and translucent. "
          "The birefringence of the granules under polarised light is lost.", title="Gelatinization"),
        T("Gelatinization needs both water and heat. It occurs over a range of temperature, roughly 55 to 80 degrees Celsius depending on the starch "
          "(check your textbook for individual starches). On heating past this range the swollen granules may rupture and the paste thins. "
          "The following factors alter it:"),
        KEY("Factors affecting gelatinization and paste viscosity", "Think: water, heat, other ingredients, shear.", cards=[
            ["Sugar", "Competes for water, so gelatinization is delayed and the paste is less thick and clear."],
            ["Acid", "Hydrolyses starch chains during long cooking, so the paste thins (lemon in a sauce)."],
            ["Fat and protein", "Coat the granules and delay water uptake."],
            ["Stirring and shear", "Rupture swollen granules and thin the paste. Stir enough to avoid lumps but not too hard."],
        ]),
        T("To prevent lumps, first disperse the starch in cold liquid or mix it with fat or sugar, then heat while stirring."),
        H("Retrogradation and syneresis"),
        D("**Retrogradation** is the slow recrystallisation of starch molecules when a gelatinized paste cools and stands. Amylose chains line up "
          "quickly and form a firm gel; amylopectin recrystallises slowly over days. Water can be squeezed out of the gel; this weeping is called **syneresis**.",
          title="Retrogradation"),
        T("Retrogradation explains why cold porridge sets, why stale bread is firm and crumbly (mostly amylopectin recrystallising, with water "
          "moving from crumb to crust), and why cooked rice is hard when cold. It is fastest at refrigerator temperature (about 0 to 5 degrees Celsius). "
          "Reheating above about 60 to 70 degrees Celsius melts the crystals and refreshes the bread for a time. Waxy starches, "
          "emulsifiers (monoglycerides), sugar and enzymes slow staling."),
        H("Dextrinization and caramelization"),
        D("**Dextrinization** is the breakdown of starch by dry heat (and sometimes acid) into shorter chains called **dextrins**, which are "
          "brown, soluble and have less thickening power. It occurs in toast crust, browned flour in a roux and toasted gari.",
          title="Dextrinization"),
        D("**Caramelization** is the thermal breakdown of sugars on their own, with no amino acids needed, giving brown colours and flavours. "
          "Sucrose first splits into glucose and fructose and then forms brown polymers (caramel) and flavour compounds above about 160 degrees Celsius. "
          "Fructose caramelises at a lower temperature than glucose or sucrose.", title="Caramelization"),
        KEY("Three browning reactions compared", "Know which needs what.", cards=[
            ["Dextrinization", "Starch only, dry heat. Products: dextrins."],
            ["Caramelization", "Sugar only, high heat (above about 160 degrees Celsius for sucrose). Products: caramel, bitter and nutty flavours."],
            ["Maillard", "Reducing sugar plus amino group, lower temperatures. Products: melanoidins. See the Maillard lesson."],
        ]),
        MISTAKE("Calling all browning caramelization", "Bread crust and roast groundnuts brown mainly by the Maillard reaction, which needs protein or amino acids. Caramelization is sugar alone. Use the word that matches the reactants named in the question."),
        H("Pectin gels"),
        T("**Pectin** is a polysaccharide of galacturonic acid units found in the cell walls of fruit (rich in citrus peel, guava, apple skins, "
          "slightly under-ripe fruit). Its carboxyl groups may be esterified with methanol. The **degree of methylation** (the share of methylated groups) "
          "decides how it gels."),
        KEY("High-methoxyl and low-methoxyl pectin", "Pectin gels in two different ways.", cards=[
            ["High-methoxyl (HM, more than about 50 percent methylated)", "Gels when there is a lot of sugar (about 60 to 65 percent soluble solids) and acid (pH about 2.8 to 3.5). Sugar takes water from the pectin, acid removes negative charge, so chains join by hydrogen bonds and hydrophobic links."],
            ["Low-methoxyl (LM)", "Gels with calcium ions bridging chains and needs little or no sugar. Used in low-sugar spreads."],
        ]),
        T("A good traditional jam therefore needs three things in the right balance: enough pectin (about 0.5 to 1.5 percent), enough acid, and "
          "enough sugar. Too little pectin gives a runny syrup; too little acid gives a weak gel; too much sugar gives crystals."),
        EX("Worked example 1: jam endpoint", intro="A cook mixes 1 000 g of guava pulp that contains 10 percent natural sugar with 1 000 g of sugar and boils it until the soluble solids reach 65 percent. What is the final mass and how much water is boiled off? (Teaching data.)", steps=[
            S("Mass of solids", math=r"1000 \times 0.10 + 1000 = 1100 \text{ g}"),
            S("Final mass that makes 65 percent", math=r"\frac{1100}{0.65} = 1692 \text{ g}"),
            S("Water lost", math=r"2000 - 1692 = 308 \text{ g}"),
            S("Interpret", text="The cook must boil off about 308 g of water. A sugar thermometer reading about 104 to 105 degrees Celsius, or the 'wrinkle' test on a cold plate, indicates the endpoint."),
        ], check=r"\frac{1100}{1692} = 0.650"),
        EX("Worked example 2: why porridge sets", intro="Explain why cooked maize porridge becomes firm when cooled, and why the surface may release a little water after storage.", steps=[
            S("Hot paste", text="Heating gelatinized the starch: granules swelled and amylose leached into the water."),
            S("On cooling", text="Amylose chains line up and bind by hydrogen bonds, forming a network that traps water: a gel."),
            S("Storage", text="The network keeps tightening as amylopectin also recrystallises, squeezing out some water: syneresis."),
            S("Prevention", text="Use a waxy starch, add fat or sugar, or freeze quickly. Reheating partly reverses the gel."),
        ]),
        QUIZ("What is the main cause of bread staling?",
             ["Loss of all water from the loaf", "Recrystallisation (retrogradation) of starch, mostly amylopectin, and moisture moving to the crust", "Caramelization of the crumb", "Gelatinization of starch in the oven"], 1,
             "Starch gelatinized in baking recrystallises as the loaf stands, making it firm. A stale loaf has not lost all of its water.",
             hint="Which starch change happens during standing, not heating?",
             feedback=["Stale bread still holds most of its water; the water moves from crumb to crust.", "", "Caramelization needs high temperature and is not a storage change.", "Gelatinization happens in the oven; staling comes later."]),
        QUIZ("A cook boils sugar alone in a dry pan until it turns amber. Which reaction occurs?",
             ["Dextrinization", "Maillard reaction", "Caramelization", "Retrogradation"], 2,
             "Heating a sugar alone, with no starch or amino acids, gives caramelization.",
             hint="What are the only reactants?",
             feedback=["Dextrinization needs starch.", "Maillard needs amino groups.", "", "Retrogradation is a cooling change of starch."]),
        H("Practice"),
        PQ("Explain the difference between gelatinization and retrogradation.", "Gelatinization happens when starch is heated with water: granules swell, amylose leaches and a viscous paste forms. Retrogradation happens when that paste cools and stands: starch chains reassociate and recrystallise, forming a gel or a firm texture and sometimes releasing water (syneresis). Gelatinization is irreversible; retrogradation is partly reversible by reheating."),
        PQ("State three factors that lower the viscosity of a hot starch sauce and explain each.", "Acid hydrolyses starch chains; high stirring or shear breaks swollen granules; and long cooking past the peak ruptures granules. (Fat or sugar delay thickening rather than lowering the final paste.)"),
        PQ("Explain why a jam needs sugar, acid and pectin to set.", "Pectin provides the gel network. Acid lowers pH and removes the negative charge on pectin, so chains can approach each other. Sugar binds water, lowering the water available and encouraging pectin chains to join. If any of the three is missing in the right amount, the gel is weak or fails."),
        PQ("Essay plan: 'Discuss the role of heat in changing the properties of carbohydrates in cooking.'", "Introduction: carbohydrate types. Point 1: gelatinization and thickening of starch. Point 2: dextrinization in dry heat. Point 3: caramelization of sugars. Point 4: pectin extraction and gel setting in jam. Point 5: effects of heat on nutritive value (starch becomes digestible, some sugar loss in the Maillard reaction). Evaluation: the reaction depends on moisture, pH and other ingredients; each reaction brings both benefits (flavour, texture) and drawbacks (loss of thickening, bitterness, acrylamide when starchy foods are fried at high temperature). Conclusion."),
        TIP("Exam link: carbohydrate properties appear in Paper 1 and Paper 2 and as practical tests (iodine test for starch, effect of heat on starch paste, jam making) in Paper 3. Name the reaction, state the conditions and give a food example."),
        SUM("Starch granules contain linear amylose and branched amylopectin; the ratio affects thickening and gel strength.",
            "Gelatinization is irreversible swelling of starch with heat and water; retrogradation is slow recrystallisation on cooling, causing staling and syneresis.",
            "Dextrinization is starch broken by dry heat; caramelization is sugar alone at high temperature; Maillard needs amino groups.",
            "High-methoxyl pectin gels with about 60 to 65 percent sugar and acid; low-methoxyl pectin gels with calcium.",
            "Jam endpoint is calculated from the mass of solids divided by the target solids fraction."),
    ],
))

# ------------------------------------------------------------------ 3. Lipid chemistry
LESSONS.append(lesson(
    module=M1,
    topic="Lipid chemistry",
    title="Lipid chemistry: saturation, hydrogenation, rancidity and polymorphism",
    slug="fsl1-lipid-chemistry",
    minutes=26,
    summary="Fats and oils are triglycerides whose properties depend on their fatty acids. Learn saturation, hydrogenation and margarine manufacture, auto-oxidation and rancidity (and how to prevent it), and fat crystal polymorphism.",
    objectives=[
        "Relate fatty acid chain length, saturation and cis or trans form to melting point and properties",
        "Explain hydrogenation and outline margarine manufacture with a flow diagram",
        "Describe the stages of auto-oxidation and hydrolytic rancidity and propose measures to prevent rancidity",
        "Explain polymorphism and calculate iodine value, saponification value, peroxide value and free fatty acid",
    ],
    key_concepts=["Triglyceride", "Saturated and unsaturated", "Iodine value", "Hydrogenation", "Trans fat", "Auto-oxidation",
                  "Rancidity", "Antioxidant", "Polymorphism"],
    blocks=[
        H("Introduction"),
        T("Red palm oil is liquid in the morning and cloudy in a cool room, while shea butter and cocoa butter are firm. Groundnut oil "
          "left open in a hot kitchen turns smelly in weeks. These behaviours come from the chemistry of **lipids**."),
        D("A **triglyceride** (triacylglycerol) is a glycerol molecule esterified with three fatty acids. Each fatty acid is a carboxylic acid with a "
          "hydrocarbon chain. A saturated fatty acid has only single bonds in the chain; an unsaturated one has one (monounsaturated) or more (polyunsaturated) C=C double bonds.",
          title="Triglyceride"),
        H("How structure sets properties"),
        KEY("Melting point and structure", "Straight chains pack closely and melt at higher temperatures.", cards=[
            ["Chain length", "Longer chains have more attraction between molecules, so the melting point rises."],
            ["Saturation", "Saturated chains are straight and pack closely: solid fats (butter, coconut fat, palm stearin)."],
            ["Cis double bond", "Puts a kink in the chain, so packing is loose and the melting point is low: liquid oils (olive, groundnut, sunflower)."],
            ["Trans double bond", "Chain stays nearly straight, so trans fatty acids behave more like saturated fat. They are made by partial hydrogenation and occur in small amounts in ruminant fat."],
        ]),
        T("Natural fats are mixtures of many triglycerides, so they melt over a range rather than at a point. The more unsaturated the fat, the "
          "more susceptible it is to oxidation. Palm oil is about half saturated, which is why it is semi-solid in cool weather (check your textbook for exact composition)."),
        D(r"The **iodine value** is the mass of iodine (in grams) that reacts with 100 g of fat: it measures the number of C=C double bonds. High iodine value = highly unsaturated. The **saponification value** is the mass of potassium hydroxide in mg needed to saponify 1 g of fat and tells you the average chain length: short chains give a higher value.",
          title="Iodine value and saponification value"),
        EX("Worked example 1: iodine value of oleic acid", intro="Oleic acid (C18H34O2, relative molecular mass 282.5) has one double bond. Each double bond takes up one molecule of iodine (I2, 253.8). Calculate its iodine value.", steps=[
            S("Iodine per mole", text="1 mol oleic acid (282.5 g) absorbs 1 mol I2 (253.8 g)."),
            S("Scale to 100 g", math=r"\text{IV} = \frac{253.8}{282.5} \times 100 = 89.9"),
            S("Linoleic acid for comparison", text="Linoleic acid (C18H32O2, 280.5) has two double bonds, so IV = 2 x 253.8 / 280.5 x 100 = 181.0. More double bonds give a higher IV."),
        ]),
        EX("Worked example 2: saponification value of triolein", intro="Triolein (relative molecular mass 885.5) reacts with three KOH per molecule (KOH = 56.1). Find its saponification value.", steps=[
            S("Moles of KOH per gram", math=r"\frac{3}{885.5} = 3.388 \times 10^{-3} \text{ mol}"),
            S("Mass of KOH in mg", math=r"3.388 \times 10^{-3} \times 56.1 \times 1000 = 190.1"),
            S("Interpret", text="A saponification value near 190 is typical of long-chain oils. Coconut oil, with shorter chains, has a higher value (around 250, check your textbook)."),
        ]),
        H("Hydrogenation and margarine"),
        D("**Hydrogenation** adds hydrogen across C=C double bonds, in the presence of a finely divided nickel catalyst at elevated temperature "
          "and pressure, turning liquid oils into semi-solid fats. **Partial hydrogenation** saturates some bonds and may convert some cis bonds to trans; "
          "full hydrogenation gives a hard fat.", title="Hydrogenation"),
        T("Hydrogenation raises the melting point and also improves oxidative stability, because fewer double bonds remain. Its drawbacks: partial "
          "hydrogenation creates trans fats, which raise LDL cholesterol and are linked to heart disease, so many countries limit them, and "
          "producers now prefer blending, fractionation or interesterification (rearranging fatty acids on glycerol)."),
        EX("Worked example 3: hydrogen needed", intro="One tonne (1 000 kg) of oil with iodine value 120 is partially hydrogenated until the iodine value is 70. How much hydrogen is used? (Teaching data.)", steps=[
            S("Iodine value drop per 100 g", text="120 - 70 = 50 g of iodine equivalent per 100 g oil."),
            S("Moles of double bonds hydrogenated per 100 g", math=r"\frac{50}{253.8} = 0.197 \text{ mol}"),
            S("Mass of hydrogen per 100 g", math=r"0.197 \times 2.016 = 0.397 \text{ g}"),
            S("Scale to 1 000 kg", text="1 000 kg is 10 000 lots of 100 g, so hydrogen = 0.397 g x 10 000 = 3.97 kg, about 4 kg."),
        ]),
        IMG("alfsl1-margarine-flow.svg", alt="Flow diagram of margarine manufacture: refined oils and fats blended, fat phase with emulsifier and fat-soluble vitamins, aqueous phase of water, salt and milk, pre-emulsification, chilling and crystallising in a scraped-surface cooler, working, packing and tempering",
            caption="Figure 1. Manufacture of margarine (a water-in-oil emulsion). Do not confuse it with cheese making."),
        T("Margarine is a **water-in-oil emulsion**, typically about 80 percent fat and about 16 percent water phase (check your textbook). The fat phase is a blend "
          "of liquid oil and hydrogenated or interesterified fat, mixed with an emulsifier (lecithin, mono- and diglycerides), vitamins A and D, colour (carotene) "
          "and flavour. The water phase contains water, salt and milk solids. The two phases are emulsified, chilled quickly in a scraped-surface heat exchanger "
          "so that small fat crystals form, worked to give a plastic texture, packed and often stored briefly at a set temperature (tempering)."),
        H("Rancidity"),
        D("**Rancidity** is the development of unpleasant tastes and smells in fats and fatty foods. There are two main types: "
          "**oxidative rancidity** (auto-oxidation) by oxygen and **hydrolytic rancidity** by water and lipase enzymes.", title="Rancidity"),
        KEY("Auto-oxidation in three stages", "A free-radical chain reaction.", cards=[
            ["Initiation", "Heat, light, or a metal ion (iron, copper) removes a hydrogen atom next to a double bond, forming a lipid free radical (R•)."],
            ["Propagation", "R• reacts with oxygen to give a peroxyl radical, which takes a hydrogen from another fatty acid, forming a hydroperoxide and a new R•. The chain keeps going."],
            ["Termination", "Two radicals combine to form non-radical products. Hydroperoxides break down into aldehydes, ketones and short acids that smell rancid."],
        ]),
        T("**Hydrolytic rancidity** occurs when lipase (from the food, mould or bacteria) or heat and water split triglycerides into glycerol and "
          "free fatty acids. In butter the short-chain butyric acid has a sharp, sour smell. In frying, water from food hydrolyses the oil and "
          "raises free fatty acids, which makes the oil smoke at a lower temperature."),
        KEY("Preventing rancidity", "Remove one of the three drivers: oxygen, catalysts, heat and light.", cards=[
            ["Exclude oxygen", "Airtight containers, vacuum or nitrogen packing, keep jars full."],
            ["Avoid light, heat and metals", "Store in dark, cool places; use stainless steel, not copper or iron; refined oils with metals removed."],
            ["Add antioxidants", "Natural tocopherols (vitamin E), ascorbyl palmitate; synthetic BHA, BHT, TBHQ and propyl gallate. They donate hydrogen to radicals and stop the chain."],
            ["Control water and enzymes", "Use dry fat, heat to destroy lipase, refrigerate, do not reuse frying oil excessively."],
        ]),
        T("Rancidity is measured by the **peroxide value** (milliequivalents of peroxide per kilogram of fat, which tracks early oxidation) and by "
          "**free fatty acid** content (a percentage expressed as oleic acid, which tracks hydrolysis)."),
        EX("Worked example 4: peroxide value and free fatty acid", intro="A 5.0 g oil sample needs 4.2 mL of 0.01 mol/L sodium thiosulphate; a blank needs 0.2 mL. Calculate the peroxide value (meq/kg). Separately, 10 g of oil is neutralised by 3.5 mL of 0.1 mol/L NaOH; calculate % free fatty acid as oleic acid (M = 282.5). (Teaching data.)", steps=[
            S("Peroxide value", math=r"\text{PV} = \frac{(4.2 - 0.2) \times 0.01 \times 1000}{5.0} = 8.0 \text{ meq/kg}"),
            S("Free fatty acid", math=r"\%\text{FFA} = \frac{3.5 \times 0.1 \times 282.5}{10 \times 10} = 0.99\%"),
            S("Interpret", text="A fresh refined oil has a peroxide value well below 10 meq/kg; limits are set by food standards (check the current rules). About 1 percent free fatty acid is a sign that the oil is ageing."),
        ]),
        H("Polymorphism"),
        D("**Polymorphism** is the ability of a fat to crystallise in more than one crystal form with different melting points and packing. The "
          "main forms are **alpha** (unstable, loose, lowest melting point), **beta prime** (intermediate, small fine crystals) and **beta** (most stable, large dense crystals, highest melting point).",
          title="Polymorphism"),
        T("The form matters for texture. Margarine and shortening should stay in the beta prime form: small crystals give a smooth, glossy spread and good creaming and aeration. "
          "If they change to beta on storage the product becomes grainy (sandy). Lard tends to crystallise in the beta form, so it is grainy unless interesterified. "
          "**Cocoa butter** has six forms (I to VI in one numbering system). Form V melts just below body temperature, giving a shiny, snapping chocolate "
          "that melts in the mouth. Chocolate makers use **tempering** (controlled melting, cooling and stirring) to seed form V. Without tempering, chocolate may show white **fat bloom** from migration of a more stable form."),
        MISTAKE("Mixing up the margarine flow with cheese making", "The Board's 2023 report notes that some candidates confused the flow diagram for margarine with one for cheese. Margarine begins with oils and fats and an aqueous phase and an emulsifier; cheese begins with milk, starter culture and rennet. Learn the margarine steps in order."),
        MISTAKE("Defining rancidity without prevention", "The report adds that candidates struggled to define rancidity and give preventive measures. Give a definition, name the two types, then list measures that match each type."),
        QUIZ("Which change lowers the melting point of a fat?",
             ["Converting cis double bonds to single bonds by hydrogenation", "Shortening the fatty acid chain", "Converting a cis bond to a trans bond", "Increasing the number of saturated chains"], 1,
             "Shorter chains have weaker attractions between molecules and melt at lower temperatures. Hydrogenation, trans bonds and more saturated chains raise the melting point.",
             hint="Which change reduces the attraction between chains?",
             feedback=["Hydrogenation straightens the chains and raises the melting point.", "", "Trans bonds are straighter, so they raise the melting point.", "More saturated chains pack closer and melt higher."]),
        QUIZ("Which is the correct order of events in oxidative rancidity?",
             ["Termination, propagation, initiation", "Propagation, initiation, termination", "Initiation, propagation, termination", "Hydrolysis, initiation, propagation"], 2,
             "A free radical forms (initiation), the chain reaction builds hydroperoxides (propagation) and radicals finally combine (termination).",
             hint="A chain reaction must first begin.",
             feedback=["That reverses the sequence.", "Initiation cannot come after propagation.", "", "Hydrolysis belongs to hydrolytic rancidity, a different process."]),
        H("Practice"),
        PQ("Define rancidity and propose four measures that prevent it.", "Rancidity is the development of off-flavours and odours in fats through oxidation (auto-oxidation) or hydrolysis (lipase and water). Prevention: store in airtight, opaque containers; keep cool; exclude copper and iron; add antioxidants such as tocopherol, BHA or BHT; heat to inactivate lipase; keep the fat dry; avoid reusing frying oil too often."),
        PQ("Draw and describe a flow diagram for margarine manufacture.", "Refined oils and fats are blended and mixed with oil-soluble emulsifier, vitamins A and D and colour to form the fat phase. The water phase (water, salt, milk solids) is mixed separately. The phases are emulsified, pasteurised, then chilled and crystallised rapidly in a scraped-surface cooler, worked in a resting tube, packed and tempered. Include hydrogenation or interesterification earlier if a hard fat component is made."),
        PQ("Calculate the iodine value of a fat if 0.50 g of it absorbs 0.45 g of iodine.", "Iodine value is grams of iodine per 100 g of fat. 0.45 g per 0.50 g = 0.90 g per g, so 90 g per 100 g. The iodine value is 90, similar to an oil rich in oleic acid."),
        PQ("Essay plan: 'Explain how the chemical structure of fats influences their use in food.'", "Introduction: triglyceride structure. Point 1: chain length, saturation and cis or trans form control the melting point and so solid or liquid state. Point 2: unsaturation increases susceptibility to oxidation; hydrogenation improves stability but may form trans fats. Point 3: polymorphism controls texture in margarine and chocolate. Point 4: uses, for example frying oils, shortening, spreads. Evaluation: nutritional trade-offs (saturated and trans fats versus essential polyunsaturated fatty acids). Conclusion."),
        TIP("Exam link: lipid chemistry appears in Paper 1 (definitions, iodine value, rancidity) and in Paper 2 food-science essays; the Board's report notes that rancidity and the margarine flow diagram were poorly answered, so practise both. Paper 3 may include fat tests. Always give the stage names and the preventive measures."),
        SUM("Fats are triglycerides; chain length, saturation and cis or trans form determine melting point and stability.",
            "Iodine value measures unsaturation; saponification value measures average chain length.",
            "Hydrogenation with nickel saturates double bonds, hardens oils and improves stability, but partial hydrogenation can create trans fats; margarine is a water-in-oil emulsion.",
            "Oxidative rancidity runs by initiation, propagation and termination; hydrolytic rancidity is lipase and water; prevent by excluding oxygen, light, heat, metals and water and by adding antioxidants.",
            "Polymorphs (alpha, beta prime, beta) set the texture of margarine and chocolate; tempering seeds the desired form."),
    ],
))

# ------------------------------------------------------------------ 4. Protein structure and functional properties
LESSONS.append(lesson(
    module=M1,
    topic="Protein structure and functional properties",
    title="Protein structure, denaturation, coagulation, foaming and protein quality",
    slug="fsl1-protein-structure-functional",
    minutes=26,
    summary="Protein behaviour in food follows from its four levels of structure. Learn denaturation and coagulation, foaming, gluten and gelation, and how biological value separates high and low biological value proteins.",
    objectives=[
        "Describe primary, secondary, tertiary and quaternary protein structure and the bonds that hold them",
        "Explain denaturation, coagulation and what causes them in cooking and processing",
        "Explain how proteins form foams and gels and why gluten and caseins behave as they do",
        "Distinguish high and low biological value proteins and calculate digestibility and biological value",
    ],
    key_concepts=["Peptide bond", "Primary to quaternary structure", "Denaturation", "Coagulation", "Isoelectric point", "Foam", "Gluten",
                  "Biological value", "Protein complementation"],
    blocks=[
        H("Introduction"),
        T("An egg white turns from clear liquid to firm white when it is poached. Milk curdles when lemon juice is added. Dough made from wheat flour "
          "stretches and traps gas, but dough from cassava flour does not. All of this is **protein functionality**: what proteins do in foods because of their shape and chemistry."),
        H("Four levels of structure"),
        D("A **protein** is a polymer of amino acids joined by **peptide bonds** (a condensation reaction between the carboxyl group of one amino acid and the amino group of the next, releasing water). "
          "A chain of n amino acids has n - 1 peptide bonds.", title="Peptide bond"),
        KEY("Levels of protein structure", "Each level depends on the one before it.", cards=[
            ["Primary", "The sequence of amino acids, held by peptide bonds. This is set by the gene."],
            ["Secondary", "Local folding into alpha-helices and beta-pleated sheets, held by hydrogen bonds between backbone groups."],
            ["Tertiary", "The full 3D fold of one chain, held by hydrogen bonds, ionic bonds, hydrophobic interactions and disulphide bridges (S-S) between cysteine residues."],
            ["Quaternary", "Several chains associated into one functional protein (haemoglobin has four)."],
        ]),
        T("Amino acids have an amino group, a carboxyl group and a side chain (R). The side chain decides whether the residue is hydrophobic, polar or charged. "
          "Nine of the twenty amino acids are **essential** for adults (histidine, isoleucine, leucine, lysine, methionine, phenylalanine, threonine, tryptophan and valine) "
          "because the body cannot make them in sufficient amounts."),
        H("Denaturation and coagulation"),
        D("**Denaturation** is the loss of the secondary, tertiary and quaternary structure of a protein, without breaking peptide bonds. The primary structure is unchanged. "
          "The protein unfolds and loses its biological activity and often its solubility.", title="Denaturation"),
        D("**Coagulation** is the clumping together of denatured protein molecules into a solid or semi-solid mass (as egg white sets or milk curdles).",
          title="Coagulation"),
        KEY("What causes denaturation", "Anything that breaks the weak bonds holding the fold.", cards=[
            ["Heat", "Increases vibration and breaks hydrogen bonds. Egg white begins to set at about 60 to 65 degrees Celsius, yolk a little higher."],
            ["Acid or alkali", "Changes the charge on side chains. Lemon juice curdles milk; vinegar helps egg white set (poaching)."],
            ["Mechanical action", "Whisking or kneading unfolds proteins at air interfaces or aligns them."],
            ["Salt, solvents, enzymes", "Salt in cheese making, alcohol, and proteolytic enzymes such as papain used as tenderizers."],
        ]),
        T("Denaturation can improve digestibility (cooked egg is more digestible than raw) and destroys harmful proteins such as trypsin inhibitors in beans and avidin in raw egg white. "
          "Over-heating makes proteins tough and rubbery because they squeeze out water: this is why overcooked egg and meat are hard."),
        T("Every protein has an **isoelectric point (pI)**, the pH at which its net charge is zero. There the protein is least soluble because chains do not repel one another and aggregate. "
          "Casein has a pI of about 4.6, which is the pH at which milk curdles in yoghurt and in acid cheeses. For this reason fermented milk sets as lactic acid bacteria lower the pH. "
          "In cheese making rennet (the enzyme chymosin) clips kappa-casein, which allows the casein micelles to clump into curd."),
        H("Foams and gels"),
        T("**Foaming** happens when a protein solution is whisked: the protein unfolds at the air-liquid interface, exposing hydrophobic groups to the air and hydrophilic groups to water, "
          "and forms a film around each bubble. Partial denaturation and then coagulation of this film (for example when meringue or sponge is baked) sets the foam. "
          "Factors: sugar added gradually stabilises egg white foam by thickening the liquid and slowing drainage; a pinch of acid (cream of tartar) helps stability; "
          "any trace of fat or egg yolk spoils the foam because fat competes for the interface; over-whipping makes the foam dry and grainy as films break."),
        T("**Gelation** occurs when denatured proteins link into a three-dimensional network that holds water. Examples: set custard, cooked egg, gelatin dessert, "
          "yoghurt, cheese and tofu. **Gluten** forms when wheat flour proteins gliadin (gives extensibility) and glutenin (gives elasticity) are hydrated and kneaded: disulphide and hydrogen bonds "
          "form a stretchy network which traps carbon dioxide during bread making."),
        H("Protein quality: HBV and LBV"),
        T("Proteins differ in how well they supply essential amino acids. **High biological value (HBV) proteins** contain all essential amino acids in "
          "proportions close to human need (animal proteins such as egg, milk, meat and fish; soya is a plant example that is nearly complete). "
          "**Low biological value (LBV) proteins** are low in one or more essential amino acids, called **limiting amino acids** (cereals are low in lysine; legumes low in methionine). "
          "The Board's 2023 report notes that some candidates could not distinguish HBV from LBV proteins, so learn both definitions and examples."),
        F(r"\text{BV} = \frac{\text{nitrogen retained}}{\text{nitrogen absorbed}} \times 100"),
        T("**Protein complementation** means eating proteins whose limiting amino acids differ, so each makes up for the other: rice with beans, maize pap with groundnuts, "
          "or bread with milk. Together they supply an HBV-like mixture."),
        EX("Worked example 1: digestibility and biological value", intro="A volunteer eats 10 g of nitrogen in a protein food in a day. Faecal nitrogen from the food is 2 g and urinary nitrogen from the food is 3 g. Calculate true digestibility, biological value and net protein utilisation. (Teaching data; endogenous losses are ignored.)", steps=[
            S("Nitrogen absorbed", math=r"10 - 2 = 8 \text{ g}"),
            S("Digestibility", math=r"\frac{8}{10} \times 100 = 80\%"),
            S("Nitrogen retained", math=r"8 - 3 = 5 \text{ g}"),
            S("Biological value", math=r"\frac{5}{8} \times 100 = 62.5\%"),
            S("Net protein utilisation", math=r"\frac{5}{10} \times 100 = 50\%", text="NPU = BV x digestibility = 0.625 x 0.80 = 50 percent."),
        ]),
        EX("Worked example 2: chemical score", intro="A cereal protein contains 3.6 g lysine per 100 g protein. A reference protein has 5.8 g per 100 g. Find the lysine score and name the limiting amino acid. (Teaching data.)", steps=[
            S("Ratio", math=r"\frac{3.6}{5.8} \times 100 = 62\%"),
            S("State", text="Lysine is the limiting amino acid if every other essential amino acid scores higher than 62 percent."),
            S("Improve", text="Adding legumes (rich in lysine) raises the mixture's score."),
        ]),
        MISTAKE("Saying denaturation breaks peptide bonds", "Denaturation breaks the weaker bonds that hold the fold, not the peptide bonds. Hydrolysis by acid, strong alkali or protease enzymes breaks peptide bonds, and that is a different change."),
        QUIZ("Which bonds are broken first when egg white is heated?",
             ["Peptide bonds", "Hydrogen bonds and other weak bonds that maintain the fold", "Covalent bonds in the amino acids themselves", "Phosphodiester bonds"], 1,
             "Heat breaks the weak bonds holding secondary and tertiary structure; the primary sequence stays intact.",
             hint="Which bonds are weakest?",
             feedback=["Peptide bonds survive normal cooking.", "", "Bonds inside amino acids are strong and are not broken in cooking.", "Phosphodiester bonds belong to nucleic acids."]),
        QUIZ("Why does a trace of egg yolk stop egg white from whisking into a stable foam?",
             ["Yolk is more acidic", "Yolk fat competes with proteins at the bubble surface and weakens the film", "Yolk has more water", "Yolk raises the temperature"], 1,
             "Fat and phospholipids sit at the interface in place of protein, so the protein film cannot form properly.",
             hint="What does a foam need at the bubble surface?",
             feedback=["The effect is not due to acidity.", "", "Water content is not the cause.", "Temperature is not changed."]),
        H("Practice"),
        PQ("Distinguish between high biological value and low biological value proteins, with an example of each.", "HBV proteins contain all the essential amino acids in proportions close to human needs and are well used by the body, for example egg and milk. LBV proteins lack or are low in one or more essential amino acids, the limiting amino acids, for example maize (low in lysine and tryptophan) or most legumes (low in methionine)."),
        PQ("Explain why mixing cereal and legumes improves protein quality.", "Cereal proteins are limited in lysine but adequate in methionine; legume proteins are rich in lysine but limited in methionine. The two limiting amino acids differ, so each makes up for the other and the combined protein is nutritionally close to HBV. Example: rice and beans or maize and groundnuts."),
        PQ("Explain what happens to protein structure when egg white is poached, and why overcooking is undesirable.", "Heat breaks hydrogen bonds and other weak bonds, so the protein unfolds (denaturation) and the unfolded chains bond to each other to form a network that sets (coagulation). If heated too long the network tightens and squeezes water out, making the white tough and rubbery."),
        PQ("Essay plan: 'Describe the functional properties of proteins in food preparation.'", "Introduction: four levels of structure. Point 1: denaturation and coagulation (eggs, meat). Point 2: foaming (whisked egg whites, meringue) with conditions. Point 3: gelation (custard, gelatin, cheese). Point 4: gluten formation in bread. Point 5: solubility and isoelectric precipitation (yoghurt, cheese). Point 6: nutritive effects: digestibility, loss of availability. Evaluation: correct handling depends on temperature, pH and time. Conclusion."),
        TIP("Exam link: protein structure and HBV or LBV protein appear in Paper 1 and Paper 2; the Board's report says that many candidates could not separate HBV from LBV proteins. Give a definition and an example of each and name limiting amino acids."),
        SUM("Proteins are amino acid chains held by peptide bonds; structure runs from primary to quaternary with weak bonds holding the fold.",
            "Denaturation unfolds protein without breaking peptide bonds; coagulation is the clumping of denatured protein.",
            "Heat, acid, whisking, salt and enzymes denature proteins; each protein is least soluble at its isoelectric point.",
            "Proteins foam by unfolding at interfaces, gel by forming networks, and form gluten from gliadin and glutenin in wheat.",
            "HBV proteins have all essential amino acids; LBV proteins lack some; complementation mixes proteins whose limiting amino acids differ."),
    ],
))

# ------------------------------------------------------------------ 5. Maillard browning
LESSONS.append(lesson(
    module=M1,
    topic="Maillard browning",
    title="Maillard non-enzymatic browning: chemistry, control, flavour and acrylamide",
    slug="fsl1-maillard-browning",
    minutes=22,
    summary="The Maillard reaction joins reducing sugars to amino groups and gives crust colour, roast flavour and some losses in protein quality. Learn the stages, the conditions that control it and how to encourage or limit it.",
    objectives=[
        "State the reactants and the main stages of the Maillard reaction",
        "Explain the effect of temperature, pH, water activity and reactant type on its rate",
        "Distinguish Maillard browning from caramelization and enzymic browning",
        "Evaluate its benefits and its drawbacks (flavour, colour, lysine loss, acrylamide) and describe control measures",
    ],
    key_concepts=["Reducing sugar", "Amino group", "Schiff base and Amadori product", "Melanoidins", "Strecker degradation", "Lysine availability", "Acrylamide"],
    blocks=[
        H("Introduction"),
        T("The golden crust of bread, roasted groundnuts, grilled fish, roasted cocoa and coffee beans, fried plantain and the brown skin of roast chicken share one cause. "
          "They are products of the **Maillard reaction**, named after the French chemist Louis-Camille Maillard, who described it in the early 1900s. "
          "It is called **non-enzymatic browning** because no enzyme is needed."),
        D("The **Maillard reaction** is a series of reactions between the carbonyl group of a **reducing sugar** and a free **amino group** of an amino acid, peptide or protein, "
          "which on heating produces brown polymers (melanoidins) and many flavour compounds.", title="Maillard reaction"),
        T("A **reducing sugar** has a free aldehyde or ketone group that can react: glucose, fructose, lactose and maltose. Sucrose is **not** reducing, so it only takes part after it has been split by acid or heat. "
          "The amino group usually comes from lysine, whose side chain has a spare amino group, which is why lysine is the amino acid most affected."),
        H("The main stages"),
        KEY("Three broad stages (simplified)", "The details vary with conditions.", cards=[
            ["Early stage: condensation", "The carbonyl of the sugar reacts with the amino group to give a Schiff base, which rearranges to an Amadori product (or Heyns product with ketoses). Nothing coloured yet and no flavour."],
            ["Intermediate stage", "Amadori products break down to reactive dicarbonyl compounds and furfurals. Strecker degradation of amino acids by dicarbonyls gives aldehydes with strong aromas and carbon dioxide."],
            ["Final stage", "Reactive intermediates condense and polymerise into brown nitrogen-containing polymers, melanoidins, with the colour and roast flavour."],
        ]),
        T("The type of flavour depends on the amino acid and sugar: proline gives bread-like notes, cysteine contributes meaty flavours, and the temperature matters. "
          "This is why roast, toasted, grilled and fried foods smell as they do."),
        H("What controls the rate"),
        KEY("Factors", "Think: conditions that bring reactants together fast.", cards=[
            ["Temperature", "The rate rises steeply with temperature, roughly doubling or tripling for each 10 degrees Celsius rise. It happens slowly even at room temperature over months of storage."],
            ["Water activity", "Fastest at intermediate aw (about 0.5 to 0.8). Too dry: molecules cannot move. Too wet: reactants are diluted."],
            ["pH", "Faster in neutral to alkaline conditions (above pH 6) because amino groups are unprotonated and free to react. Acid slows it."],
            ["Type of sugar", "Pentoses react faster than hexoses; glucose and fructose are more reactive than lactose or maltose."],
            ["Amino acid", "Lysine reacts most readily; free amino acids react faster than amino groups bound in proteins."],
        ]),
        EX("Worked example 1: effect of temperature", intro="Assume the browning rate triples for each 10 degrees Celsius rise (Q10 = 3). By what factor does the rate rise when the pan temperature increases from 130 to 150 degrees Celsius? (Teaching assumption.)", steps=[
            S("Number of 10-degree steps", math=r"\frac{150 - 130}{10} = 2"),
            S("Factor", math=r"3^2 = 9"),
            S("Interpret", text="The browning is nine times faster, so a few extra minutes at a hotter pan can turn golden into burnt. Real Q10 values depend on the food and the stage."),
        ]),
        H("Maillard compared with other browning"),
        KEY("Three browning mechanisms", "A very common examination comparison.", cards=[
            ["Maillard", "Sugar plus amino group, 100 to 180 degrees Celsius or slow in storage; needs no enzyme."],
            ["Caramelization", "Sugar alone, above about 160 degrees Celsius for sucrose."],
            ["Enzymic browning", "Phenolic compounds plus oxygen catalysed by polyphenol oxidase, at room temperature in cut fruits."],
        ]),
        H("Benefits and drawbacks"),
        T("**Benefits:** desirable colour and flavour in bread, biscuits, coffee, cocoa, roast meat, malt and beer; attractive brown skin on fried foods; "
          "melanoidins have antioxidant properties. **Drawbacks:**"),
        KEY("Undesirable effects", "Evaluate both sides.", cards=[
            ["Loss of nutritive value", "Lysine's amino group becomes chemically bound and is no longer available to the body. Milk powder, toasted breakfast cereals and long-stored dried foods can lose a large share of available lysine."],
            ["Unwanted browning", "Dried milk, dried egg, dehydrated fruit and concentrated juices darken in store and develop off-flavours."],
            ["Acrylamide", "When foods rich in the amino acid asparagine and in reducing sugars (potato, some cereal foods, coffee) are fried, baked or roasted above about 120 degrees Celsius, acrylamide, a probable human carcinogen, can form."],
        ]),
        T("Control measures: lower the temperature and shorten the time; lower the pH a little (acid); control aw; remove or reduce reducing sugars (store potatoes warm, not cold, to avoid sugar build-up, and blanch cut potatoes); "
          "use the enzyme asparaginase to reduce asparagine; use sulphites in some dried products; use non-reducing sugar (sucrose) in place of glucose where browning is not wanted; store dried foods cool and dry."),
        EX("Worked example 2: lysine availability", intro="A toasted cereal contains 3.0 g lysine per 100 g protein before toasting and the available fraction after toasting is 65 percent. Calculate the available lysine and the fall in lysine score against a reference value of 5.8 g per 100 g. (Teaching data.)", steps=[
            S("Available lysine", math=r"3.0 \times 0.65 = 1.95 \text{ g per 100 g protein}"),
            S("Score before", math=r"\frac{3.0}{5.8} \times 100 = 52\%"),
            S("Score after", math=r"\frac{1.95}{5.8} \times 100 = 34\%"),
            S("Interpret", text="Toasting reduced the protein quality a great deal. In a diet that is already low in lysine, this matters."),
        ]),
        MISTAKE("Thinking Maillard browning needs an enzyme or only sugar", "Maillard is non-enzymic and needs both a reducing sugar and an amino group. Sugar alone gives caramel; phenols and polyphenol oxidase give enzymic browning."),
        QUIZ("Which food would be least likely to show Maillard browning when heated?",
             ["Milk, with lactose and protein", "Bread dough, with reducing sugars and protein", "Pure sucrose solution at 100 degrees Celsius", "Roasted groundnuts"], 2,
             "Pure sucrose is not a reducing sugar and there is no amino group, so there is no Maillard reaction at that temperature.",
             hint="Which choice lacks one of the two reactants?",
             feedback=["Milk contains both lactose and amino acids and browns when heated.", "Dough has both reactants.", "", "Groundnuts contain both reducing sugars and protein."]),
        QUIZ("Why does adding lemon juice slow the browning of a fried food?",
             ["It increases the temperature", "Acid lowers pH so amino groups are protonated and less reactive", "It supplies more reducing sugar", "It removes oxygen"], 1,
             "At low pH amino groups carry a positive charge and are not available to attack the sugar.",
             hint="What does pH do to the amino group?",
             feedback=["Acid does not raise temperature.", "", "Acid does not add reducing sugar.", "The reaction does not need oxygen."]),
        H("Practice"),
        PQ("State two conditions that increase the rate of the Maillard reaction.", "Higher temperature (and longer heating time) and a pH nearer neutral or alkaline; also intermediate water activity (0.5 to 0.8) and the presence of reactive reducing sugars and lysine."),
        PQ("Explain why the Maillard reaction lowers the protein quality of a toasted food.", "The amino group on the lysine side chain reacts with the sugar to form compounds that the digestive enzymes cannot break and the body cannot use. The lysine is therefore unavailable, so the protein, which is already limited in lysine in cereals, has a lower biological value."),
        PQ("A chip producer finds that fried potato slices turn too dark. Suggest three causes and a remedy for each.", "Too much reducing sugar in tubers stored in the cold: store warm or choose low-sugar varieties and blanch to leach sugar. Oil temperature too high: reduce frying temperature. Fry time too long or the oil old: shorten the time and renew oil. A small amount of acid dip can also slow browning."),
        PQ("Essay plan: 'Discuss the importance of non-enzymic browning in food processing.'", "Introduction: define Maillard, reactants and stages. Point 1: desirable roles in bread, coffee, cocoa, meats. Point 2: undesirable roles in dried milk, juice concentrates, lysine loss, acrylamide. Point 3: control through temperature, pH, aw and ingredient choice. Point 4: compare with caramelization and enzymic browning. Evaluation: balance flavour and safety; processing choices depend on the product. Conclusion."),
        TIP("Exam link: Maillard browning is in Paper 1 (reactants, conditions) and Paper 2 essays on cooking and processing. Always name both reactants and say whether an enzyme is involved."),
        SUM("Maillard browning needs a reducing sugar and an amino group, no enzyme; it makes melanoidins and flavour.",
            "Stages: condensation to Amadori product, breakdown with Strecker degradation, then polymerisation to melanoidins.",
            "Rate rises with temperature, intermediate aw and higher pH; lysine and reducing sugars are most reactive.",
            "It gives crust colour and roast flavour but can lower available lysine, spoil dried foods and form acrylamide.",
            "Control by temperature, time, pH, aw, raw material choice and asparaginase."),
    ],
))

# ------------------------------------------------------------------ 6. Vitamins and processing
LESSONS.append(lesson(
    module=M2,
    topic="Vitamins and processing",
    title="Stability of fat-soluble and water-soluble vitamins during processing",
    slug="fsl1-vitamins-processing",
    minutes=24,
    summary="Vitamins differ widely in how well they survive heat, light, oxygen, pH and water. Learn the stability of each group, where losses occur in preparation and processing, and how to calculate retention.",
    objectives=[
        "Contrast the stability of fat-soluble (A, D, E, K) and water-soluble (B group, C) vitamins",
        "Name the factors that destroy each of the main vitamins",
        "Locate the main points of vitamin loss in preparation, cooking, drying, freezing and canning",
        "Apply first-order loss and combined retention calculations and suggest ways to protect vitamins",
    ],
    key_concepts=["Fat-soluble vitamins", "Water-soluble vitamins", "Leaching", "Thermal destruction", "Oxidation", "Retention", "First-order loss"],
    blocks=[
        H("Introduction"),
        T("A bowl of leaves such as bitterleaf or cassava leaves that has been boiled for an hour and its water thrown away has lost much of its vitamin C and folate, "
          "while the same leaves lightly steamed keep more. A bottle of milk left in sunshine loses riboflavin. Vitamins are present in tiny amounts and are fragile, so "
          "**how** food is stored, prepared and processed decides how much the eater really receives."),
        D("**Water-soluble vitamins** (the B vitamins and vitamin C) dissolve in water, are not stored in large amounts, and are easily lost by leaching and heat. "
          "**Fat-soluble vitamins** (A, D, E and K) dissolve in fat and oil, are stored in the body and are lost mainly by oxidation and light, not by leaching.",
          title="Two groups"),
        H("Stability of the main vitamins"),
        KEY("Water-soluble vitamins", "Summary of what destroys them (qualitative; severity differs with conditions).", cards=[
            ["Vitamin C (ascorbic acid)", "The least stable. Destroyed by heat, oxygen, light, alkali, and traces of copper and iron; lost by leaching into cooking water; ascorbic acid oxidase in cut plants acts on it. Better kept in acid conditions."],
            ["Thiamin (B1)", "Heat-labile and destroyed in alkaline conditions (bicarbonate of soda in cooking), destroyed by sulphite; soluble in water. Thiaminase in raw fish and some plants breaks it down."],
            ["Riboflavin (B2)", "Stable to heat and acid, but destroyed by light (milk in clear glass or plastic) and alkali."],
            ["Niacin (B3)", "Very stable to heat, light and oxidation, but lost by leaching. In maize it is bound and unavailable unless treated with alkali (nixtamalisation); this link explains pellagra in maize-dependent diets."],
            ["Folate and B12", "Folate is lost by heat, light, oxidation and leaching. B12 is fairly heat-stable but lost in high-temperature, long cooking and by light."],
        ]),
        KEY("Fat-soluble vitamins and provitamin A", "Stable to leaching, vulnerable to oxidation.", cards=[
            ["Vitamin A and carotenoids", "Fairly stable to heat in normal cooking, but oxidised by oxygen, light and metals, especially in dried foods and in oil that is old or heated for long. Red palm oil keeps its carotenoids well if protected from light and not over-heated or stored long."],
            ["Vitamin D", "Quite stable in cooking and storage."],
            ["Vitamin E (tocopherols)", "Acts as a natural antioxidant and is itself used up as it protects fat; lost in frying and in rancid fats."],
            ["Vitamin K", "Stable to heat but destroyed by light and alkali."],
        ]),
        H("Where the losses occur"),
        T("Losses happen at every stage from farm to plate: harvest and storage (respiration and enzymes), preparation (peeling, cutting, soaking and washing), cooking "
          "(heat and leaching) and holding (keeping food hot for hours)."),
        KEY("Processing and vitamin losses", "Think: leaching, heat, oxidation, light.", cards=[
            ["Preparation", "Cutting leaves before washing, peeling thickly and soaking in water increase leaching and enzymic oxidation. Wash then cut."],
            ["Boiling", "Water-soluble vitamins leach out into the water and heat destroys some. Use a small volume of water and use the cooking liquid in a soup or sauce."],
            ["Steaming and microwave", "Less leaching, so higher retention than boiling."],
            ["Frying", "Little leaching; heat and oxidation affect vitamins E and A, and the oil itself can be damaged."],
            ["Blanching", "Brief heating before freezing or drying inactivates enzymes. Some water-soluble vitamin loss, but far less than the loss that enzymes would cause in storage."],
            ["Drying and canning", "Sun drying in light destroys carotene and vitamin C; heat sterilisation destroys heat-labile vitamins; vitamin A and C in canned food keep falling slowly in store."],
            ["Freezing", "Little loss during freezing; most loss occurs at blanching and at thawing and cooking."],
        ]),
        H("Calculating losses"),
        D(r"Many vitamin losses follow **first-order kinetics**: the rate of loss is proportional to the amount present. The amount remaining after time $t$ is $C = C_0 e^{-kt}$, where $k$ is the rate constant. The **half-life** is $t_{1/2} = \ln 2 / k$.",
          title="First-order loss", formula=r"C = C_0 e^{-kt}, \quad t_{1/2} = \frac{\ln 2}{k}"),
        EX("Worked example 1: vitamin C in boiling", intro="Vitamin C in a leafy vegetable is lost in boiling water with a rate constant of 0.020 per minute. If the raw leaves contain 100 mg per 100 g, how much remains after 15 minutes, and what is the half-life? (Teaching data.)", steps=[
            S("Apply the equation", math=r"C = 100 \, e^{-0.020 \times 15} = 100 \, e^{-0.30}"),
            S("Compute", math=r"C = 74.1 \text{ mg}"),
            S("Half-life", math=r"t_{1/2} = \frac{0.693}{0.020} = 34.7 \text{ min}"),
            S("Interpret", text="About 26 percent is destroyed in 15 minutes by heat alone, before counting the vitamin that leaches into the water. Shorter cooking saves vitamin."),
        ], check=r"100 e^{-0.30} = 74.08"),
        EX("Worked example 2: combined retention", intro="Vegetables lose 25 percent of vitamin C when blanched and then retain 70 percent of what is left after cooking. Find the overall retention. (Teaching data.)", steps=[
            S("After blanching", math=r"100 - 25 = 75\% \text{ remains}"),
            S("After cooking", math=r"0.75 \times 0.70 = 0.525"),
            S("State", text="Overall retention is 52.5 percent. Retentions at successive steps are multiplied, not added."),
        ]),
        EX("Worked example 3: planning to protect vitamins", intro="Advise a school canteen on cooking a leaf vegetable to keep as much vitamin C and folate as possible.", steps=[
            S("Before cooking", text="Wash first, then cut into large pieces just before cooking; avoid long soaking."),
            S("During cooking", text="Use a small amount of boiling water, lid on, cook for a short time or steam; do not add bicarbonate of soda."),
            S("After cooking", text="Serve at once; use the cooking liquid in the stew; keep food hot for the least time possible."),
            S("Storage", text="Buy fresh, store cool and dark, and use quickly."),
        ]),
        MISTAKE("Saying fat-soluble vitamins are never lost", "They resist leaching, but oxidation, light and long heating in oil destroy vitamins A, E and K. Dried, stored or frying-oil foods can lose a lot."),
        QUIZ("Which vitamin is most likely to be destroyed by adding bicarbonate of soda to cooking water?",
             ["Vitamin D", "Niacin", "Thiamin", "Vitamin A"], 2,
             "Thiamin is unstable in alkaline conditions; bicarbonate of soda raises the pH and speeds its destruction.",
             hint="Which vitamin is unstable in alkali and heat?",
             feedback=["Vitamin D is quite stable in cooking.", "Niacin is very stable to heat and pH.", "", "Vitamin A is not destroyed by alkali in normal cooking."]),
        QUIZ("Why is steaming usually better than boiling for retaining vitamin C?",
             ["Steam is hotter than boiling water", "There is less leaching into cooking water", "Steam adds vitamin C", "Steaming destroys ascorbic acid oxidase only"], 1,
             "The vegetable is not immersed in water, so less vitamin leaches out.",
             hint="Which process removes dissolved vitamins?",
             feedback=["Steam is at the same temperature as boiling water.", "", "Steam adds nothing.", "That is a side effect, but the major benefit is reduced leaching."]),
        H("Practice"),
        PQ("Explain why water-soluble vitamins are lost in greater amounts than fat-soluble vitamins when vegetables are boiled.", "Water-soluble vitamins dissolve in the cooking water and leach out of the cut surfaces, and heat destroys some of them. Fat-soluble vitamins do not dissolve in water and are mostly retained in the food, apart from oxidation and light damage."),
        PQ("Vitamin C in a juice is lost with a rate constant of 0.010 per day on storage. How much of 40 mg per 100 mL remains after 30 days?", "C = 40 e^(-0.010 x 30) = 40 e^(-0.30) = 40 x 0.7408 = 29.6 mg per 100 mL, a loss of about 26 percent."),
        PQ("State four ways of reducing vitamin losses when cooking green vegetables.", "Wash before cutting; use a small volume of water or steam; keep the cooking time short and the lid on; do not add bicarbonate of soda; serve immediately and use the cooking liquid."),
        PQ("Essay plan: 'Discuss the effects of food processing on the vitamin content of foods.'", "Introduction: vitamin groups and stability. Point 1: losses in preparation and cooking by leaching, heat, oxidation. Point 2: effects of drying, freezing, canning and blanching with examples. Point 3: light and packaging, especially riboflavin and carotene. Point 4: protective measures and fortification or enrichment. Evaluation: processing can also improve nutritional quality (niacin release in maize, destruction of thiaminase) and preserve food for the lean season. Conclusion."),
        TIP("Exam link: vitamin stability appears in Paper 1 and in Paper 2 (nutrition and food-science questions) and in practical cookery planning. Always give the cause of loss with the vitamin: leaching, heat, light, oxygen or alkali."),
        SUM("Water-soluble vitamins are lost by leaching and heat; fat-soluble vitamins are lost mainly by oxidation and light.",
            "Vitamin C and thiamin are the most fragile; niacin and vitamin D are among the most stable.",
            "Cut after washing, use little water, short time and no soda, and serve quickly.",
            "First-order loss: C = C0 e^(-kt); retentions at successive steps are multiplied.",
            "Processing can both lose and, in some cases (niacin, thiaminase), improve vitamin availability."),
    ],
))

# ------------------------------------------------------------------ 7. Minerals and anti-nutritional factors
LESSONS.append(lesson(
    module=M2,
    topic="Minerals and anti-nutritional factors",
    title="Mineral bioavailability and anti-nutritional factors: phytates, oxalates, tannins and others",
    slug="fsl1-minerals-antinutritional-factors",
    minutes=24,
    summary="Eating a mineral is not the same as absorbing it. Learn bioavailability, enhancers and inhibitors, and the main anti-nutritional factors in plant foods (phytates, oxalates, tannins, cyanogenic glycosides and enzyme inhibitors) and how processing reduces them.",
    objectives=[
        "Define bioavailability and name factors that enhance or inhibit mineral absorption",
        "Distinguish haem from non-haem iron",
        "Explain how phytates, oxalates and tannins bind minerals and how soaking, germination, fermentation and cooking reduce them",
        "Describe other anti-nutritional factors in tropical staples and calculate phytate to zinc ratios",
    ],
    key_concepts=["Bioavailability", "Haem and non-haem iron", "Phytate", "Oxalate", "Tannin", "Cyanogenic glycoside", "Protease inhibitor", "Phytate:zinc ratio"],
    blocks=[
        H("Introduction"),
        T("A child eating a maize-and-bean meal may be given the same amount of iron on paper as another child eating liver and bread, but absorb far less. "
          "Food tables give the **total** mineral content. The body only uses the part it can absorb: the **bioavailable** part."),
        D("**Bioavailability** is the fraction of a nutrient in food that is absorbed and used by the body. It depends on the form of the mineral, the other foods eaten with it, "
          "food processing and the body's own needs and state (for example iron deficiency increases absorption).", title="Bioavailability"),
        H("Iron: haem and non-haem"),
        T("**Haem iron** is part of haemoglobin and myoglobin in meat, fish and poultry. It is absorbed intact, mainly unaffected by inhibitors; roughly 15 to 35 percent may be absorbed "
          "(values vary by source and iron status; check your textbook). **Non-haem iron** is the inorganic form in plant foods, eggs and dairy; "
          "it is absorbed poorly (often 2 to 20 percent) and strongly affected by what is eaten at the same meal."),
        KEY("Enhancers and inhibitors", "Learn the typical examples.", cards=[
            ["Enhancers", "Vitamin C reduces ferric to ferrous iron and keeps it soluble; meat, fish and poultry factor increases non-haem iron absorption; organic acids (citric, lactic); fermentation."],
            ["Inhibitors", "Phytates (cereals, legumes), polyphenols and tannins (tea, coffee, some sorghum and beans), oxalates (spinach, cocoyam leaves), calcium (competes with iron), and excess fibre."],
        ]),
        T("Practical advice: in the diet of a low-income household, add a source of vitamin C (lemon, guava, orange, fresh peppers) to the meal and drink tea or coffee **between** meals rather than with them."),
        H("Phytates"),
        D("**Phytic acid** (and its salt, **phytate**) is the main storage form of phosphorus in seeds, cereals and legumes. Its six phosphate groups bind iron, zinc, calcium and magnesium "
          "into insoluble complexes that the intestine cannot absorb.", title="Phytate"),
        T("Whole grains, bran, maize, sorghum, millet and legumes are rich in phytate. It can reduce absorption of iron and especially zinc. "
          "The **phytate to zinc molar ratio** is used to judge zinc availability: a ratio above about 15 is commonly taken as a sign of low zinc availability (some authors use 15 and others 18; check your textbook)."),
        EX("Worked example 1: phytate to zinc ratio", intro="A portion of a diet supplies 600 mg of phytic acid (molar mass 660) and 4.0 mg of zinc (atomic mass 65.4). Calculate the molar ratio. Then find the ratio if soaking and fermentation remove 50 percent of the phytate. (Teaching data.)", steps=[
            S("Moles of phytate", math=r"\frac{600}{660} = 0.909 \text{ mmol}"),
            S("Moles of zinc", math=r"\frac{4.0}{65.4} = 0.0612 \text{ mmol}"),
            S("Ratio", math=r"\frac{0.909}{0.0612} = 14.9"),
            S("After 50 percent removal", math=r"\frac{0.455}{0.0612} = 7.4"),
            S("Interpret", text="The meal is just below the commonly used threshold of 15 and reducing phytate halves the ratio, improving zinc availability."),
        ]),
        T("**Reducing phytate:** soaking (water dissolves some and activates natural phytase), germination or malting (sprouting activates phytase), fermentation (microbial phytase; for example ogi, "
          "fermented maize and sourdough), cooking in some cases, and milling (removes bran but also lowers minerals, so check the trade-off)."),
        H("Oxalates, tannins and others"),
        T("**Oxalic acid** forms insoluble calcium oxalate, so calcium in the same food is not absorbed (spinach, sorrel and cocoyam leaves are high in oxalate). "
          "Calcium oxalate can also form kidney stones in susceptible people. Boiling and discarding the water removes part of the soluble oxalate."),
        EX("Worked example 2: oxalate and calcium", intro="A serving of leaves contains 300 mg of oxalic acid (molar mass 90) and 120 mg of calcium (atomic mass 40.1). Assuming 1 mole of oxalate binds 1 mole of calcium, how much calcium could be bound? (Teaching data.)", steps=[
            S("Moles of oxalate", math=r"\frac{300}{90.03} = 3.33 \text{ mmol}"),
            S("Moles of calcium", math=r"\frac{120}{40.08} = 2.99 \text{ mmol}"),
            S("Compare", text="Oxalate (3.33 mmol) exceeds calcium (2.99 mmol), so in theory all 120 mg of calcium could be bound and unavailable."),
            S("Interpret", text="This is why leafy vegetables high in oxalate are poor calcium sources despite their high calcium content. In real digestion not all binds, so absorption is reduced rather than zero."),
        ]),
        T("**Tannins** are polyphenols (in tea, coffee, red sorghum, some beans and unripe fruit) that bind protein and iron, lowering digestibility and absorption; they also make foods astringent. "
          "Milk protein binds tannin, which is why milk in tea reduces its effect on iron a little. **Other anti-nutritional factors** in tropical foods:"),
        KEY("Other anti-nutritional factors", "Know the food, the harm and the processing remedy.", cards=[
            ["Cyanogenic glycosides", "In bitter cassava (linamarin). When the plant cells are damaged, an enzyme releases hydrogen cyanide. Remedy: peeling, grating, soaking, fermenting, drying and thorough cooking (as in making gari, fufu and bobolo)."],
            ["Protease (trypsin) inhibitors and lectins", "In raw soya, beans and other legumes: reduce protein digestion; lectins can cause illness. Destroyed by thorough soaking and boiling; they are not destroyed by under-cooking."],
            ["Goitrogens", "In cassava, cabbage and millet: interfere with iodine use by the thyroid. Risk is greatest when iodine intake is low."],
            ["Saponins and gossypol", "Saponins give bitterness and foaming in legumes; gossypol in cottonseed is toxic to simple-stomached animals. Removed by processing or breeding."],
        ]),
        MISTAKE("Calling every anti-nutritional factor harmful in all cases", "At normal intakes, some (phytate, tannins, saponins) have possible benefits such as antioxidant activity. The aim is to reduce them to levels that do not limit mineral absorption, not to eliminate them. Raw beans and poorly processed bitter cassava, however, are truly dangerous."),
        QUIZ("Which meal pairing improves non-haem iron absorption?",
             ["Beans with a cup of strong tea", "Beans with fresh orange or pepper", "Beans with a calcium supplement", "Cereal porridge with extra bran"], 1,
             "Vitamin C keeps iron in the soluble ferrous form and counters inhibitors.",
             hint="Which choice adds vitamin C?",
             feedback=["Tea tannins bind iron.", "", "Calcium competes with iron absorption.", "Extra bran adds more phytate and fibre."]),
        QUIZ("Which processing step best reduces the phytate in a maize and bean mixture?",
             ["Frying in oil at a high temperature", "Soaking and fermenting", "Grinding into flour only", "Adding salt after cooking"], 1,
             "Soaking dissolves some phytate and activates phytase; fermentation by microbes with phytase breaks it down.",
             hint="Which steps give enzymes time to act?",
             feedback=["Dry heat does not break down phytate much.", "", "Grinding alone leaves phytate unchanged.", "Salt has no effect on phytate."]),
        H("Practice"),
        PQ("Distinguish between haem and non-haem iron.", "Haem iron is part of haemoglobin and myoglobin found in meat, fish and poultry; it is well absorbed and little affected by other foods. Non-haem iron is the inorganic iron in plant foods, eggs and dairy; it is poorly absorbed and strongly affected by enhancers (vitamin C, meat factor) and inhibitors (phytate, tannins, calcium)."),
        PQ("A diet supplies 450 mg phytic acid (M = 660) and 3.0 mg zinc (A = 65.4). Calculate the phytate to zinc molar ratio and say what it suggests.", "Phytate = 450 / 660 = 0.682 mmol; zinc = 3.0 / 65.4 = 0.0459 mmol; ratio = 14.9. This is just under the commonly used 15, so zinc availability is borderline."),
        PQ("Explain how phytates reduce mineral absorption and give three ways to lower phytate in a cereal diet.", "Phytate has six phosphate groups that bind Fe, Zn, Ca and Mg, forming insoluble salts that cannot be absorbed. Reduce it by soaking, germination or malting (which activate phytase) and fermentation (microbial phytase); also by milling to remove bran if the mineral trade-off is acceptable."),
        PQ("Essay plan: 'Discuss the factors that affect the bioavailability of minerals in a plant-based diet.'", "Introduction: bioavailability versus total content. Point 1: inhibitors: phytate, oxalate, tannin, fibre, competition between minerals. Point 2: enhancers: vitamin C, meat factor, fermentation. Point 3: processing: soaking, germination, fermentation, cooking, and fortification. Point 4: body factors: deficiency, age, pregnancy. Evaluation: whole grains also give benefits, so balance. Conclusion."),
        TIP("Exam link: mineral absorption and anti-nutritional factors appear in Paper 1 and Paper 2 nutrition essays, and practical menu planning. Give the mechanism (bind, insoluble) and a processing remedy."),
        SUM("Bioavailability is the fraction of a nutrient that is absorbed and used; food table totals do not show it.",
            "Haem iron is well absorbed; non-haem iron is poorly absorbed and depends on enhancers such as vitamin C.",
            "Phytates, oxalates and tannins bind minerals; the phytate to zinc ratio helps judge zinc availability.",
            "Soaking, germination, fermentation and proper cooking reduce phytate, oxalate, cyanogenic glycosides and enzyme inhibitors.",
            "Other factors include cyanogenic glycosides, protease inhibitors and goitrogens in tropical staples."),
    ],
))

# ------------------------------------------------------------------ 8. Food pigments
LESSONS.append(lesson(
    module=M2,
    topic="Food pigments",
    title="Food pigments: chlorophylls, carotenoids, anthocyanins and myoglobin",
    slug="fsl1-food-pigments",
    minutes=24,
    summary="Colour tells us about freshness and quality. Learn the structure, colour and stability of chlorophylls, carotenoids, anthocyanins and myoglobin, and how pH, heat, oxygen and metals change them.",
    objectives=[
        "Describe the structure and solubility of chlorophylls, carotenoids, anthocyanins and myoglobin",
        "Explain the colour changes caused by heat, acid, alkali, oxygen and metal ions",
        "Apply the knowledge to cooking green vegetables, red palm oil, hibiscus drinks and fresh and cooked meat",
        "Use the colour difference formula to describe a colour change",
    ],
    key_concepts=["Chlorophyll and pheophytin", "Carotenoids (carotenes and xanthophylls)", "Anthocyanins", "Myoglobin, oxymyoglobin, metmyoglobin", "Colour difference"],
    blocks=[
        H("Introduction"),
        T("Buyers choose food by colour: bright green leaves, red palm oil, a ripe red tomato, a deep red bissap drink, fresh red meat. Colour changes tell us about freshness, ripeness and cooking, "
          "and the changes follow chemistry. This lesson covers the four pigment groups named in the syllabus."),
        H("Chlorophylls"),
        D("**Chlorophylls** are the green pigments of leaves. Each molecule has a porphyrin ring (four linked nitrogen-containing rings) with a central magnesium ion and a long fat-soluble phytol tail. "
          "Chlorophyll a is blue-green and chlorophyll b is yellow-green.", title="Chlorophyll"),
        KEY("What changes chlorophyll", "Green vegetables go olive in the pot.", cards=[
            ["Heat and acid", "Acid in the cell sap (released on heating) replaces the central magnesium by two hydrogen atoms, giving **pheophytin**, an olive-brown pigment. Pheophytin is the dull colour of overcooked green vegetables and of vegetables cooked with lemon or vinegar."],
            ["Alkali", "Hydrolyses the phytol tail, giving bright green **chlorophyllin** (water soluble), but also softens the tissue and destroys thiamin, so bicarbonate is not recommended."],
            ["Metal ions", "Copper or zinc can replace the magnesium to give stable bright green complexes; used in some canned peas and sometimes regulated (check the current rules)."],
            ["Enzymes", "Chlorophyllase removes the phytol tail; blanching inactivates it."],
        ]),
        T("To keep colour: cook in a little boiling water with the lid off for a short time (the volatile acids escape), or blanch and cool quickly; do not add acid or use bicarbonate."),
        EX("Worked example 1: mass change of pheophytin", intro="Chlorophyll a (C55H72MgN4O5, 893.5) forms pheophytin a (C55H74N4O5, 871.2) when magnesium is replaced by two hydrogen. What is the change in molar mass and the percentage of Mg in chlorophyll a?", steps=[
            S("Change in molar mass", math=r"893.5 - 871.2 = 22.3 \text{ g/mol}"),
            S("Magnesium share", math=r"\frac{24.3}{893.5} \times 100 = 2.7\%"),
            S("Interpret", text="Replacing only 2.7 percent of the molecule's mass (one Mg for two H) is enough to turn bright green into olive brown, because the electronic structure of the ring changes."),
        ]),
        H("Carotenoids"),
        D("**Carotenoids** are yellow, orange and red pigments built from long chains of conjugated double bonds (forty carbon atoms, tetraterpenes). **Carotenes** (beta-carotene, lycopene) are pure hydrocarbons; "
          "**xanthophylls** (lutein, zeaxanthin) have oxygen groups. They are fat soluble and not soluble in water.", title="Carotenoids"),
        T("Beta-carotene (carrot, red palm oil, sweet potato, mango, papaya) is a **provitamin A**, so it can be converted to retinol. Lycopene (tomato, watermelon) is red and has no vitamin A activity. "
          "Carotenoids are stable to heat and to pH changes in normal cooking, so carrots stay orange when boiled. They are destroyed by oxidation, light and long exposure to heat, and by lipoxygenase enzymes that act in dried foods. Cooking breaks cell walls and "
          "**raises** the availability of carotenoids, especially with a little fat. Colour loss is a sign of vitamin A loss."),
        H("Anthocyanins"),
        D("**Anthocyanins** are water-soluble flavonoid pigments in the vacuoles of plant cells, giving red, purple and blue colours to berries, red cabbage, purple sweet potato, hibiscus calyces (used for the bissap drink), "
          "red grapes and aubergine skin. Their colour depends strongly on pH.", title="Anthocyanins"),
        KEY("Anthocyanin colour with pH", "A natural pH indicator.", cards=[
            ["Acid (pH below about 3)", "Red (flavylium cation form). A little lemon keeps hibiscus drink bright red."],
            ["Near neutral (pH about 4 to 6)", "Colourless or pale, or purple, depending on the compound."],
            ["Alkaline (pH above about 7)", "Blue or green; bicarbonate turns red cabbage or hibiscus juice bluish. Unstable at high pH."],
        ]),
        T("Anthocyanins also form blue complexes with iron, aluminium and tin ions, which is why purple cabbage and berries can turn blue-grey in metal pans or cans. Heat, light, sulphur dioxide, ascorbic acid in some systems, "
          "oxygen and polyphenol oxidase destroy anthocyanins, and they leach into cooking water because they are water soluble."),
        H("Myoglobin and meat colour"),
        D("**Myoglobin** is the iron-containing protein that stores oxygen in muscle. It consists of a globin protein and a haem group with iron at the centre. Its colour depends on the oxidation state of the iron and "
          "on what is bound to it.", title="Myoglobin"),
        KEY("Meat colour changes", "Three forms of myoglobin.", cards=[
            ["Deoxymyoglobin", "Purple-red. Found in the interior of fresh meat and in vacuum-packed meat (no oxygen). Iron is Fe2+."],
            ["Oxymyoglobin", "Bright cherry red. Forms when meat surface is exposed to air (oxygen binds the Fe2+); this is the colour customers like."],
            ["Metmyoglobin", "Brown-grey. Fe2+ is oxidised to Fe3+ after a day or so in air, or at low oxygen levels. A sign of ageing."],
            ["Cooked meat", "Heat denatures the globin and oxidises the iron, giving a grey-brown haemichrome. Curing with nitrite gives pink nitrosomyoglobin, which becomes stable pink nitrosohaemochrome on cooking (ham, sausages)."],
        ]),
        T("Fresh meat should be bright red on the surface, but dark red inside. Packaging in oxygen-permeable film keeps meat red; vacuum packaging gives a purple colour that turns red when opened (blooming). "
          "Cooked colour is not a good safety test: some well-cooked meats stay pink, and some safe meats turn brown; use a thermometer where possible."),
        H("Measuring colour change"),
        F(r"\Delta E = \sqrt{(\Delta L)^2 + (\Delta a)^2 + (\Delta b)^2}", title="Colour difference in the CIE Lab system"),
        T("In the Lab system L is lightness (0 black, 100 white), a runs from green (negative) to red (positive) and b from blue (negative) to yellow (positive). A decrease in negative a for green vegetables "
          "shows loss of green. A larger $\\Delta E$ means a more visible change."),
        EX("Worked example 2: colour change on boiling", intro="Fresh beans measure L = 52, a = -18, b = 30. After 15 minutes of boiling with the lid on they measure L = 45, a = -9, b = 22. Calculate delta E and describe the change. (Teaching data.)", steps=[
            S("Differences", math=r"\Delta L = -7, \quad \Delta a = +9, \quad \Delta b = -8"),
            S("Square and add", math=r"49 + 81 + 64 = 194"),
            S("Square root", math=r"\Delta E = \sqrt{194} = 13.9"),
            S("Interpret", text="The beans are darker (lower L), less green (a moves toward zero) and less yellow (b falls): a visible change, consistent with chlorophyll turning to pheophytin."),
        ]),
        MISTAKE("Saying carrots lose colour in boiling water because carotene dissolves", "Carotenes are fat soluble and do not dissolve in water. Little carotene is lost in boiling; anthocyanins (water soluble) leach, and chlorophyll turns olive from acid, not from dissolving."),
        QUIZ("Why does a green vegetable cooked with vinegar become olive-brown?",
             ["Vinegar oxidises carotene", "Acid replaces magnesium in chlorophyll to give pheophytin", "Vinegar dissolves chlorophyll", "Vinegar destroys the cell walls only"], 1,
             "In an acid medium the central magnesium of chlorophyll is replaced by hydrogen and the pigment becomes olive-brown pheophytin.",
             hint="What happens to the central metal ion?",
             feedback=["Carotenoids are not responsible for the green colour.", "", "Chlorophyll is fat soluble and does not dissolve in vinegar.", "The colour change is chemical, not just physical."]),
        QUIZ("A cook adds bicarbonate of soda to hibiscus drink. What will happen to the colour?",
             ["It becomes brighter red", "It turns blue or purple, since anthocyanins change colour with pH", "It turns yellow because carotenoids form", "It does not change"], 1,
             "Anthocyanins are red in acid and shift toward purple and blue as pH rises.",
             hint="Which pigment group responds to pH like an indicator?",
             feedback=["Acid, not alkali, keeps it red.", "", "Carotenoids are not formed.", "Anthocyanins respond strongly to pH."]),
        H("Practice"),
        PQ("Distinguish between carotenes and xanthophylls, giving one example of each.", "Both are carotenoid pigments. Carotenes are pure hydrocarbons, for example beta-carotene and lycopene. Xanthophylls contain oxygen groups, for example lutein and zeaxanthin."),
        PQ("Explain the changes in colour of fresh meat during storage in air.", "Purple-red deoxymyoglobin in the interior meets oxygen at the surface and becomes bright red oxymyoglobin (blooming). After longer exposure the iron is oxidised from Fe2+ to Fe3+ and the surface turns brown as metmyoglobin."),
        PQ("Describe how to cook green leaves so that they stay green and keep nutrients.", "Use a small amount of boiling water or steam; cook briefly with the lid off at first so volatile acids escape; do not add acid or bicarbonate; cool or serve quickly. Blanching inactivates chlorophyllase; avoid over-cooking, which gives pheophytin."),
        PQ("Essay plan: 'Discuss the stability of natural food pigments during processing.'", "Introduction: four groups, solubility. Point 1: chlorophyll: acid, heat, alkali, metals. Point 2: carotenoids: stable to heat and pH, but oxidised by light and air. Point 3: anthocyanins: pH, metals, leaching, enzymes. Point 4: myoglobin: oxidation state, packaging, curing. Evaluation: colour is often used as a proxy for quality, but safety and nutrition need other checks. Conclusion."),
        TIP("Exam link: pigments appear in Paper 1 and Paper 2 (food science) and in practical cookery on vegetable colour. Always give the pigment, the cause (heat, acid, alkali, oxygen) and the result (the new compound or colour)."),
        SUM("Chlorophyll is a Mg porphyrin: acid gives olive pheophytin, alkali gives bright chlorophyllin but softens food.",
            "Carotenoids are fat soluble, heat stable and provide provitamin A; oxidation and light destroy them.",
            "Anthocyanins are water-soluble pH indicators: red in acid, purple near neutral, blue in alkali.",
            "Myoglobin is purple (deoxy), red (oxy) or brown (met), and grey-brown when cooked; nitrite cures pink.",
            "Colour difference delta E = sqrt(dL squared + da squared + db squared) quantifies a change."),
    ],
))

# ------------------------------------------------------------------ 9. Enzymatic browning
LESSONS.append(lesson(
    module=M2,
    topic="Enzymatic browning",
    title="Enzymatic browning: polyphenol oxidase, enzyme selectivity and control",
    slug="fsl1-enzymatic-browning",
    minutes=23,
    summary="Cut fruit and tubers turn brown when polyphenol oxidase, oxygen and phenolic compounds meet. Learn the reaction, how enzymes work (catalysis and selectivity are different), and the ways to prevent or use browning.",
    objectives=[
        "Describe the reaction of polyphenol oxidase (PPO) with phenolic substrates and oxygen",
        "Explain how enzymes catalyse reactions and show selectivity, and distinguish the two ideas",
        "Name the factors that affect PPO activity (temperature, pH, substrate, inhibitors)",
        "Evaluate control methods and the foods where enzymic browning is wanted, and calculate rate and percentage inhibition",
    ],
    key_concepts=["Polyphenol oxidase", "Phenolic substrate", "o-Quinone and melanin", "Catalysis", "Enzyme selectivity (specificity)", "Active site", "Inhibitor"],
    blocks=[
        H("Introduction"),
        T("A sliced banana, an apple, a cut avocado or peeled yam turns brown within minutes of exposure to air. A cut mango does not do so as fast, and a freshly cut tomato barely does. "
          "Black tea owes its colour and flavour to the same chemistry, as does fermented cocoa. This is **enzymic browning**."),
        D("**Enzymic browning** is the brown discoloration caused by **polyphenol oxidase (PPO)**, an enzyme (also called tyrosinase or catechol oxidase) that contains copper. "
          "In the presence of oxygen it oxidises phenolic compounds to o-quinones, which then polymerise into brown pigments (melanins).",
          title="Enzymic browning"),
        H("The reaction"),
        KEY("Three things must meet", "Remove any one and browning stops.", cards=[
            ["Enzyme", "PPO, normally held in plastids and kept apart from phenols in the vacuole in an intact cell."],
            ["Substrate", "Phenolic compounds such as catechol, chlorogenic acid, catechins and dopamine (banana)."],
            ["Oxygen", "From the air; PPO uses oxygen to oxidise the phenol."],
        ]),
        T("Cutting, bruising or peeling breaks the cell compartments, so enzyme, phenol and oxygen mix. In the first step PPO oxidises **o-diphenols** (two adjacent OH groups on a benzene ring) to **o-quinones**. "
          "The o-quinones are unstable and highly reactive; they react with each other and with amino acids and proteins and polymerise into dark brown **melanins**. "
          "Some PPO enzymes also hydroxylate monophenols (such as tyrosine) to o-diphenols first."),
        F(r"\text{o-diphenol} + \tfrac{1}{2}\,\text{O}_2 \xrightarrow{\text{PPO}} \text{o-quinone} + \text{H}_2\text{O} \;\longrightarrow\; \text{melanins (brown)}"),
        H("Enzymes: catalysis and selectivity"),
        T("The Board's 2023 report says that candidates asked to explain enzyme **selectivity** wrote instead about the enzyme's **catalytic function**. These are two different properties. Learn both clearly."),
        KEY("Catalysis and selectivity are different", "Two separate ideas.", cards=[
            ["Catalytic function", "An enzyme is a biological catalyst: it speeds up a reaction by providing an alternative path with a lower activation energy, without being used up and without changing the equilibrium."],
            ["Selectivity (specificity)", "Each enzyme acts on one substrate or a small group of similar substrates and one type of reaction. This is due to the shape and chemistry of the **active site**, which fits only the right substrate (lock-and-key model, refined as induced fit). PPO attacks o-diphenols but not most other compounds; amylase acts on starch but not on protein; lipase on fats."],
        ]),
        T("In food science, selectivity matters: it explains why an enzyme can be used to change one component only (rennet clots milk, pectinase clears juice, papain tenderises meat) and why, to stop an enzyme, we can remove its **substrate** or "
          "block its active site with an **inhibitor**. Factors that change the shape of the active site (temperature, pH, heavy metals) change both activity and selectivity."),
        H("Factors affecting PPO"),
        KEY("Factors affecting enzyme activity", "General to all enzymes.", cards=[
            ["Temperature", "Rate roughly doubles for each 10 degrees Celsius rise until the enzyme starts to denature. PPO is inactivated by heating to about 70 to 90 degrees Celsius for a short time, in blanching."],
            ["pH", "PPO has an optimum around pH 5 to 7 and is strongly slowed below pH 3 (extreme acid denatures it)."],
            ["Substrate and oxygen concentration", "More phenol or oxygen increases the rate until the enzyme is saturated."],
            ["Inhibitors", "Ascorbic acid, sulphite, citric acid (chelates copper), salt and some thiols, and certain chemicals bind or remove oxidation products."],
        ]),
        EX("Worked example 1: rate and inhibition", intro="A cut apple extract shows an increase in absorbance (a measure of brown colour) from 0.10 to 0.60 in 5 minutes. With 0.5 percent ascorbic acid added, it rises from 0.10 to 0.20 in the same time. Calculate each rate and the percentage inhibition. (Teaching data.)", steps=[
            S("Control rate", math=r"\frac{0.60 - 0.10}{5} = 0.10 \text{ units per minute}"),
            S("Treated rate", math=r"\frac{0.20 - 0.10}{5} = 0.02 \text{ units per minute}"),
            S("Percentage inhibition", math=r"\frac{0.10 - 0.02}{0.10} \times 100 = 80\%"),
            S("Interpret", text="Ascorbic acid reduced browning by 80 percent. It works by reducing o-quinones back to phenols before they polymerise, so the colour is not formed until the ascorbic acid is used up."),
        ]),
        H("Controlling enzymic browning"),
        T("Control by attacking each of the three requirements, or by reducing the enzyme's activity:"),
        KEY("Methods of control", "Match each method to the part of the reaction it blocks.", cards=[
            ["Heat (blanching)", "Denatures PPO. Used before freezing, canning or drying vegetables."],
            ["Acid", "Lemon juice or citric acid lowers pH below the optimum and chelates copper."],
            ["Antioxidants and reducing agents", "Ascorbic acid and sulphite reduce quinones; sulphite also inhibits the enzyme."],
            ["Exclude oxygen", "Submerge in water or syrup, vacuum pack, edible coatings, modified atmosphere."],
            ["Low temperature", "Chilling slows the enzyme (but does not stop it); freezing stops it."],
            ["Remove or change substrate", "Select low-phenol varieties; peel and wash off phenols; genetic or breeding approaches."],
        ]),
        T("Do not forget that enzymic browning is **desirable** in some foods. In black tea, withered tea leaves are rolled to break cells and oxidised by PPO to give theaflavins and thearubigins "
          "(the colour and taste). It also contributes to the colour of raisins, dates, cocoa, and fermented tea. Cocoa beans also darken through other enzymic changes during fermentation."),
        EX("Worked example 2: choosing a treatment", intro="A street vendor wants to keep sliced avocados and peeled yam looking fresh for two hours. Suggest treatments and justify them.", steps=[
            S("Identify the cause", text="Cut surfaces expose PPO, phenols and air, so browning begins."),
            S("Avocado", text="Squeeze lemon or lime over the cut surface (acid and vitamin C), and cover tightly to exclude air."),
            S("Peeled yam", text="Keep the pieces under clean cold water with a little salt or citric acid until cooking; cooking denatures the enzyme."),
            S("Evaluate", text="These methods slow browning but do not stop it for long, and they must follow hygienic rules. Blanching is best if the food will be cooked, frozen or dried."),
        ]),
        MISTAKE("Confusing catalysis with selectivity, and enzymic browning with Maillard", "The report notes that answers on enzyme selectivity often described only catalysis. Selectivity = fits one substrate (active site shape). Catalysis = lower activation energy. Also, enzymic browning needs PPO, phenols and oxygen at room temperature; Maillard needs sugar and amino groups with heat."),
        QUIZ("Which treatment would NOT slow browning in cut apple slices?",
             ["Dipping in lemon juice", "Blanching in hot water", "Leaving the slices in air at room temperature", "Placing slices in a solution of ascorbic acid"], 2,
             "Air and room temperature give the enzyme everything it needs. The other treatments inhibit it or reduce quinones.",
             hint="Which choice supplies oxygen and keeps the enzyme working?",
             feedback=["Acid slows PPO and chelates copper.", "Heat denatures PPO.", "", "Ascorbic acid reduces quinones back to phenols."]),
        QUIZ("Which statement describes enzyme selectivity?",
             ["The enzyme lowers the activation energy of the reaction", "The enzyme acts on a specific substrate because its active site has a matching shape", "The enzyme is destroyed during the reaction", "The enzyme works equally well at all temperatures"], 1,
             "Selectivity (specificity) arises from the shape and chemistry of the active site, which fits particular substrates.",
             hint="Which statement is about which molecule it acts on?",
             feedback=["That is catalytic function, a different property.", "", "Enzymes are not used up.", "Enzymes have temperature optima."]),
        H("Practice"),
        PQ("Distinguish between enzyme selectivity and the catalytic function of an enzyme.", "Catalytic function is the speeding up of a reaction by lowering the activation energy, with the enzyme itself unchanged. Selectivity (specificity) is the ability of an enzyme to act only on a particular substrate or group of similar substrates, because the substrate fits the shape of the active site. For example amylase acts on starch but not on protein."),
        PQ("Explain why a banana slice turns brown but the same slice dipped in lemon juice stays pale for longer.", "Cutting brings polyphenol oxidase, phenols and oxygen together, producing o-quinones that polymerise to brown melanins. Lemon juice lowers the pH below the optimum of PPO, citric acid chelates the copper in the enzyme, and its vitamin C reduces quinones back to phenols, so browning is slowed."),
        PQ("In an experiment the rate of browning is 0.08 units per minute without treatment and 0.03 units per minute with sulphite. Calculate the percentage inhibition.", "(0.08 - 0.03) / 0.08 x 100 = 62.5 percent."),
        PQ("Essay plan: 'Discuss enzymic browning in fruits and vegetables and the ways of preventing it.'", "Introduction: define PPO, substrate, oxygen. Point 1: the reaction pathway to melanins. Point 2: factors affecting the enzyme (temperature, pH, inhibitors). Point 3: control methods with the principle of each. Point 4: foods where browning is wanted (tea, cocoa, raisins). Evaluation: the sulphites cause allergic reactions in some people and have to be declared on labels, heat changes texture and flavour, and acid changes taste. Conclusion."),
        TIP("Exam link: enzymes and browning are in Paper 1, in the Paper 2 food-science section (Question 6 was the most popular question in the Board's 2023 paper and many candidates mixed up selectivity and catalysis) and in practical work. Give definitions in two parts and use food examples."),
        SUM("Polyphenol oxidase uses oxygen to oxidise o-diphenols to o-quinones, which polymerise into brown melanins.",
            "Browning needs enzyme, phenolic substrate and oxygen; removing any one prevents it.",
            "Catalysis lowers activation energy; selectivity means the active site fits particular substrates: different ideas.",
            "Control by blanching, acid, ascorbic acid, sulphite, excluding oxygen and cooling.",
            "In tea and cocoa the same reaction produces wanted colour and flavour."),
    ],
))

# ------------------------------------------------------------------ 10. Colloidal food systems
LESSONS.append(lesson(
    module=M2,
    topic="Colloidal food systems",
    title="Colloidal food systems: emulsions, foams, sols and gels",
    slug="fsl1-colloidal-food-systems",
    minutes=25,
    summary="Many foods are colloids, one phase finely dispersed in another. Learn the types (sols, gels, emulsions, foams), what keeps them stable, how emulsifiers and HLB work, and how Stokes' law explains creaming.",
    objectives=[
        "Define colloid, dispersed phase and continuous phase and classify foods as sol, gel, emulsion or foam",
        "Explain how emulsifiers and stabilisers work and apply the idea of HLB",
        "Describe the instabilities of emulsions and foams: creaming, flocculation, coalescence and drainage",
        "Use Stokes' law to explain creaming and the effect of homogenisation, and calculate a blend HLB",
    ],
    key_concepts=["Colloid", "Dispersed and continuous phase", "Emulsion (O/W and W/O)", "Emulsifier and HLB", "Foam", "Sol and gel", "Stokes' law"],
    blocks=[
        H("Introduction"),
        T("Milk, mayonnaise, butter, whipped cream, bread, jelly, soup thickened with starch and groundnut paste are all dispersions. None is a true solution and none is a coarse mixture that separates at once. "
          "They are **colloidal systems**, which sit between the two. Many texture problems (curdled sauce, watery yoghurt, collapsed foam) are colloid problems."),
        D("A **colloid** is a system in which particles or droplets of one substance (the **dispersed phase**, about 1 nanometre to 1 micrometre or a little larger in size) are spread through another (the **continuous phase**). "
          "They do not settle quickly and scatter light (the Tyndall effect), which is why milk looks white.", title="Colloid"),
        H("Types of food colloid"),
        KEY("Classification by phases", "Name the dispersed phase first.", cards=[
            ["Sol", "Solid dispersed in liquid: starch paste (pap), chocolate drink, some soups and juices."],
            ["Gel", "Liquid trapped in a solid network: jelly, set custard, yoghurt, jam, cooked egg white, cheese."],
            ["Emulsion", "Liquid in liquid. **Oil-in-water (O/W)**: milk, mayonnaise, cream, salad dressings, soup stocks. **Water-in-oil (W/O)**: butter, margarine."],
            ["Foam", "Gas in liquid: whipped cream, whisked egg white, beer head. Gas in solid (solid foam): bread, cake, meringue, ice cream (partly)."],
            ["Aerosol and solid suspension", "Gas in gas or liquid droplets in gas (spray); dispersed solid in solid (some chocolate)."],
        ]),
        T("**Sols** are fluids that may thicken to **gels** as the dispersed particles link into a network: gelatine sol sets to a gel on cooling; pectin sol sets in jam (see the carbohydrate lesson); "
          "milk protein sol sets to a gel in yoghurt when acid reaches the isoelectric point."),
        H("Emulsions and emulsifiers"),
        T("Oil and water do not mix, and shaking only gives temporary droplets that join (coalesce) and separate. To keep an emulsion we need an **emulsifier**."),
        D("An **emulsifier** is an amphiphilic (amphipathic) molecule with a **hydrophilic** (water-loving) head and a **lipophilic** (oil-loving) tail. It sits at the oil-water interface, lowers interfacial tension, and "
          "makes a protective film around droplets that prevents them from coalescing. Examples: lecithin (egg yolk, soya), mono- and diglycerides, proteins (casein), and polysorbates.", title="Emulsifier"),
        T("**Bancroft's rule** says that the phase in which the emulsifier is more soluble tends to be the continuous phase: water-soluble emulsifiers give O/W emulsions; oil-soluble ones give W/O emulsions. "
          "The **hydrophile-lipophile balance (HLB)** scale numbers this balance. Low HLB (about 3 to 6) favours W/O; high HLB (about 8 to 18) favours O/W. HLB values of mixed emulsifiers are the weighted average of their components."),
        F(r"\text{HLB}_{\text{blend}} = x_A \,\text{HLB}_A + (1 - x_A)\,\text{HLB}_B"),
        EX("Worked example 1: HLB blend", intro="Polysorbate 80 has HLB 15.0 and sorbitan monooleate has HLB 4.3. What fraction of the blend must be polysorbate 80 to give HLB 10 for an O/W emulsion? (Values are from standard tables; check your textbook.)", steps=[
            S("Write the equation", math=r"15.0x + 4.3(1 - x) = 10"),
            S("Expand", math=r"10.7x + 4.3 = 10"),
            S("Solve", math=r"x = \frac{5.7}{10.7} = 0.533"),
            S("State", text="The blend is 53 percent polysorbate 80 and 47 percent sorbitan monooleate."),
        ], check=r"15.0(0.533) + 4.3(0.467) = 10.0"),
        T("**Stabilisers** (gums such as xanthan, guar and gum arabic, starch, pectin, carrageenan, gelatin) do not sit at the interface; they thicken the continuous phase and slow droplet movement."),
        H("Why colloids break down"),
        KEY("Instabilities", "Learn the term and what causes it.", cards=[
            ["Creaming or sedimentation", "Droplets rise (oil lighter than water) or sink because of density difference; reversible by shaking. Raw milk cream rises."],
            ["Flocculation", "Droplets clump without merging; often reversible."],
            ["Coalescence", "Droplets merge into larger ones: irreversible and leads to oil separation (curdled mayonnaise, broken sauce)."],
            ["Foam drainage and collapse", "Liquid drains from the films between bubbles; bubbles merge or the gas diffuses between bubbles (disproportionation)."],
            ["Syneresis", "A gel contracts and squeezes out liquid."],
        ]),
        T("The rate of creaming or settling of a spherical droplet is given by **Stokes' law**. It shows what we can do to slow it down."),
        F(r"v = \frac{2 r^2 (\rho_d - \rho_c)\, g}{9 \eta}", title="Stokes' law"),
        T("Here $r$ is the droplet radius, $\\rho_d$ and $\\rho_c$ are the densities of dispersed and continuous phases, $g$ is gravity and $\\eta$ the viscosity of the continuous phase. "
          "The velocity depends on the **square** of the radius, so smaller droplets are far more stable. It falls with a smaller density difference and with a higher viscosity (thickeners). Negative v means the droplet rises."),
        EX("Worked example 2: creaming velocity", intro="Oil droplets of radius 1.0 micrometre (density 920 kg per cubic metre) in water (density 1000, viscosity 0.001 Pa s). Find the creaming speed in millimetres per hour. By what factor does it change if the radius is 10 times as large? (g = 9.81.)", steps=[
            S("Substitute (SI units)", math=r"v = \frac{2 (1.0 \times 10^{-6})^2 (920 - 1000)(9.81)}{9 (0.001)}"),
            S("Compute", math=r"v = -1.74 \times 10^{-7} \text{ m/s (upwards)}"),
            S("Convert", math=r"1.74 \times 10^{-7} \times 3600 \times 1000 = 0.63 \text{ mm per hour}"),
            S("Radius 10 times as large", text="Velocity depends on r squared, so it is 100 times as large: 63 mm per hour, so the cream layer forms in a few hours."),
        ]),
        T("**Homogenisation** forces milk through a narrow valve at high pressure and breaks fat globules from about 3 to 10 micrometres in diameter to about 1 micrometre or less. "
          "A tenfold fall in radius reduces creaming rate a hundredfold (Stokes), so homogenised milk does not form a cream layer in practice."),
        MISTAKE("Saying an emulsifier works by changing the density of the oil", "An emulsifier works at the interface by lowering interfacial tension and forming a film. It does not change density. Thickeners work by raising the viscosity of the continuous phase."),
        QUIZ("Mayonnaise is best described as...",
             ["A water-in-oil emulsion stabilised by sugar", "An oil-in-water emulsion stabilised by lecithin from egg yolk", "A foam of air in oil", "A true solution of oil in vinegar"], 1,
             "Mayonnaise is a high-oil O/W emulsion; the lecithin and proteins of egg yolk are the emulsifiers.",
             hint="What is the continuous phase in mayonnaise?",
             feedback=["Butter and margarine are W/O, not mayonnaise.", "", "Mayonnaise has no gas phase.", "Oil does not dissolve in vinegar."]),
        QUIZ("Which change would most reduce the creaming speed of an oil-in-water emulsion?",
             ["Doubling the droplet radius", "Halving the droplet radius", "Warming the emulsion so that the water becomes less viscous", "Adding more oil without changing the droplet size"], 1,
             "Velocity is proportional to the square of the radius, so halving it cuts the speed to a quarter.",
             hint="Which factor is squared in Stokes' law?",
             feedback=["A larger radius makes creaming faster.", "", "Lower viscosity makes creaming faster.", "The speed of one droplet depends on its own radius, densities and viscosity, not on how many droplets there are."]),
        H("Practice"),
        PQ("Define an emulsion and distinguish an oil-in-water from a water-in-oil emulsion, with a food example of each.", "An emulsion is a colloid of one liquid dispersed as droplets in another liquid in which it is not soluble. In oil-in-water (O/W) emulsions oil droplets are in water, for example milk and mayonnaise. In water-in-oil (W/O) emulsions, water droplets are in oil, for example butter and margarine."),
        PQ("Explain how an emulsifier stabilises an emulsion.", "The emulsifier molecule has a hydrophilic head and a lipophilic tail. It adsorbs at the oil-water interface with each end in its own phase, lowers interfacial tension and makes a film (often charged) around each droplet that prevents coalescence."),
        PQ("Calculate the percentage of polysorbate 80 (HLB 15) needed in a blend with sorbitan monooleate (HLB 4.3) to give HLB 12.", "x = (12 - 4.3)/(15 - 4.3) = 7.7/10.7 = 0.72, so 72 percent polysorbate 80 and 28 percent sorbitan monooleate."),
        PQ("Essay plan: 'Discuss the importance of colloidal systems in food preparation.'", "Introduction: definition and types. Point 1: emulsions (mayonnaise, margarine, milk) and emulsifiers. Point 2: foams (egg white, whipped cream, bread). Point 3: gels (jam, yoghurt, jelly). Point 4: sols (starch pastes). Point 5: stability and breakdown (creaming, coalescence, collapse) and how to prevent it. Evaluation: texture and shelf life depend on controlling droplet size, viscosity and interface; additives help but natural ingredients are possible. Conclusion."),
        TIP("Exam link: colloids feature in Paper 1 and in Paper 2 food-science essays; make sure you can classify a food into the correct type and name the phases. Use Stokes' law only where a question gives numbers."),
        SUM("A colloid has a dispersed phase spread through a continuous phase; types are sol, gel, emulsion and foam.",
            "Emulsifiers have hydrophilic and lipophilic parts and sit at the interface; HLB guides the choice; stabilisers thicken the continuous phase.",
            "Colloids fail by creaming, flocculation, coalescence, drainage and syneresis.",
            "Stokes' law: creaming speed is proportional to r squared and density difference and inversely proportional to viscosity.",
            "Homogenisation shrinks droplets and so greatly slows creaming."),
    ],
))

# ------------------------------------------------------------------ 11. Digestion and absorption
LESSONS.append(lesson(
    module=M3,
    topic="Digestion and absorption",
    title="Gastrointestinal digestion and absorption: enzymes, transport mechanisms and routes",
    slug="fsl1-digestion-absorption",
    minutes=25,
    summary="Follow food through the gut: where each nutrient is digested, the enzymes and secretions involved, and how glucose, amino acids, fats and minerals cross into the body by diffusion, facilitated and active transport.",
    objectives=[
        "State the site, enzyme, substrate and product for digestion of carbohydrate, protein and fat",
        "Describe the roles of bile, pancreatic juice, intestinal secretions and gut hormones",
        "Explain passive, facilitated and active transport and how they absorb glucose, amino acids and fats",
        "Describe the absorption routes (portal blood and lymph) and the role of the large intestine, and calculate digestibility",
    ],
    key_concepts=["Hydrolysis", "Amylase, pepsin, trypsin, lipase", "Bile and micelles", "Villus and microvilli", "Active transport (sodium-glucose)", "Chylomicron", "Hepatic portal vein", "Lacteal"],
    blocks=[
        H("Introduction"),
        T("A meal of rice, beans and fish is a mixture of large molecules: starch, protein and fat. The body can only absorb small ones. **Digestion** breaks the big molecules down by hydrolysis; "
          "**absorption** carries the small products across the gut wall into blood or lymph. Digestibility affects how much of the food a person really gets, and so why cooking and processing matter."),
        D("**Digestion** is the breakdown of food into molecules small enough to be absorbed, by mechanical action (chewing, churning) and by chemical action (enzymes and acid). "
          "Most chemical digestion is **hydrolysis**: water is added across a bond to split it.", title="Digestion"),
        H("Step by step along the gut"),
        KEY("Mouth and stomach", "Start of carbohydrate and protein digestion.", cards=[
            ["Mouth", "Chewing increases surface area. Salivary amylase (works at about pH 6.8) starts to break starch into dextrins and maltose. Lingual lipase begins fat digestion in some species and in infants."],
            ["Stomach", "Churning mixes food with gastric juice into chyme. Hydrochloric acid (pH about 1.5 to 3) kills many microbes, denatures protein and activates pepsinogen to **pepsin**, which hydrolyses proteins into shorter polypeptides. Mucus protects the stomach wall. Intrinsic factor (needed for vitamin B12 absorption) is also secreted here. Salivary amylase is stopped by the acid."],
        ]),
        KEY("Small intestine: where most digestion happens", "Neutral to slightly alkaline pH.", cards=[
            ["Bile (made in the liver, stored in the gall bladder)", "Contains bile salts, which **emulsify** fat into tiny droplets and so give lipase a large surface area. It also neutralises acid and carries away waste products such as bile pigments. It contains no enzymes."],
            ["Pancreatic juice", "Bicarbonate neutralises the acid chyme. Enzymes: **pancreatic amylase** (starch to maltose), **trypsin and chymotrypsin** (proteins to peptides, secreted as inactive precursors), **carboxypeptidase**, **pancreatic lipase** (triglycerides to fatty acids and 2-monoglycerides), nucleases."],
            ["Brush-border enzymes", "On the surface of the microvilli: **maltase, sucrase and lactase** (disaccharides to monosaccharides) and peptidases (peptides to amino acids, dipeptides, tripeptides)."],
            ["Hormones", "Secretin (from the duodenum) stimulates bicarbonate release; cholecystokinin (CCK) stimulates enzyme release and gall bladder contraction; gastrin in the stomach stimulates acid."],
        ]),
        KEY("Summary of main enzymes", "Learn substrate, product and site.", cards=[
            ["Carbohydrate", "Starch to maltose (amylase: mouth and pancreas); maltose to glucose (maltase); sucrose to glucose and fructose (sucrase); lactose to glucose and galactose (lactase)."],
            ["Protein", "Proteins to polypeptides (pepsin, trypsin, chymotrypsin); polypeptides to dipeptides and amino acids (carboxypeptidase and peptidases)."],
            ["Fat", "Triglycerides to fatty acids and monoglycerides (pancreatic lipase), helped by bile salts."],
        ]),
        T("Lactase is produced in large amounts in infants. In many adults worldwide, production falls with age (lactase non-persistence). Undigested lactose is then fermented by gut bacteria, causing "
          "bloating and diarrhoea, which is called lactose intolerance (see the clinical dietetics lessons in Upper Sixth). Cellulose and other fibre are not digested by human enzymes at all."),
        H("Absorption in the small intestine"),
        T("The small intestine is built for absorption: it is long, and its lining is folded into **villi**, each covered with cells that have **microvilli** (the brush border). "
          "This hugely increases the surface area (check your textbook for figures). Each villus has a capillary network and a lymph vessel (**lacteal**), and the cell layer is one cell thick, so distances are short."),
        KEY("Transport across the cell layer", "Three mechanisms.", cards=[
            ["Simple (passive) diffusion", "Small, lipid-soluble molecules (fatty acids, glycerol in part, water by osmosis, fat-soluble vitamins) move down a concentration gradient, no energy needed."],
            ["Facilitated diffusion", "Carrier proteins move molecules down a gradient with no ATP. Fructose is absorbed this way by the transporter GLUT5."],
            ["Active transport", "Carrier proteins move molecules against a gradient using energy. Glucose and galactose enter with sodium ions through the SGLT1 co-transporter (secondary active transport); the sodium gradient is kept by the sodium-potassium pump using ATP. Amino acids enter with sodium; di- and tripeptides enter with hydrogen ions."],
        ]),
        T("This is why glucose absorption is so efficient even when the gut contains little glucose: the active, sodium-linked system pulls it in. It is also the reason oral rehydration solution contains both glucose and salt: "
          "glucose and sodium are absorbed together, and water follows by osmosis."),
        KEY("Routes of absorption", "Water-soluble products go to the liver first.", cards=[
            ["Hepatic portal vein", "Glucose, galactose, fructose, amino acids, short- and medium-chain fatty acids, water-soluble vitamins and most minerals go into the capillaries and then to the liver, which processes them."],
            ["Lymph (lacteal)", "Long-chain fatty acids and monoglycerides form **micelles** with bile salts, are absorbed into the cell, re-formed into triglycerides and packed into **chylomicrons**, which are too large for capillaries and enter the lacteals, then the lymph system and the blood near the heart. Fat-soluble vitamins travel with them."],
        ]),
        H("Large intestine"),
        T("The large intestine absorbs most of the remaining water and electrolytes (sodium, potassium). Gut bacteria ferment undigested carbohydrate and fibre to **short-chain fatty acids**, "
          "which are absorbed and supply some energy (butyrate feeds the colon cells), and some bacteria make vitamin K and some B vitamins. The residue is formed into faeces. Diarrhoea results from too little water absorption and is dangerous for children because of fluid and salt loss."),
        EX("Worked example 1: digestibility", intro="In a feeding trial a volunteer eats 60 g of dry food matter and 6 g of it is recovered in the faeces. Calculate the apparent digestibility of the dry matter. (Teaching data.)", steps=[
            S("Absorbed", math=r"60 - 6 = 54 \text{ g}"),
            S("Digestibility", math=r"\frac{54}{60} \times 100 = 90\%"),
            S("Interpret", text="High-fibre foods and foods with anti-nutritional factors have lower digestibility than refined foods; cooking usually raises digestibility of starch and protein."),
        ]),
        EX("Worked example 2: tracing a fat meal", intro="Trace a mouthful of palm-oil stew from the stomach to the blood, naming the secretions involved.", steps=[
            S("Stomach", text="Fat is churned and partly separated; little digestion occurs."),
            S("Duodenum", text="Bile salts emulsify the fat into droplets. Pancreatic lipase splits triglycerides into fatty acids and monoglycerides."),
            S("Micelles", text="These products join bile salts to form micelles, which carry them to the surface of the epithelial cells."),
            S("Absorption", text="They diffuse into the cell, are rebuilt into triglycerides and packed into chylomicrons, which enter the lacteal and then the lymph and bloodstream."),
        ]),
        MISTAKE("Saying bile digests fat", "Bile contains no enzymes. It emulsifies fat to a large surface area; the enzyme that hydrolyses it is lipase."),
        QUIZ("Which process absorbs glucose from the gut lumen into the cell against its concentration gradient?",
             ["Simple diffusion", "Osmosis", "Sodium-linked active transport (SGLT1)", "Endocytosis of micelles"], 2,
             "Glucose enters with sodium ions through the SGLT1 co-transporter, powered by the sodium gradient set up by the sodium-potassium pump.",
             hint="Which mechanism can move a molecule uphill?",
             feedback=["Simple diffusion only works down a gradient.", "Osmosis is movement of water.", "", "Fat absorption involves micelles; glucose does not."]),
        QUIZ("Where do chylomicrons enter the body?",
             ["Capillaries of the villus then the hepatic portal vein", "Lacteals of the villus, then the lymph system", "The stomach wall", "The bile duct"], 1,
             "Chylomicrons are too large to cross the capillary walls, so they enter the lacteals.",
             hint="Which vessel carries fats?",
             feedback=["Water-soluble products take that route.", "", "The stomach does not absorb fat.", "The bile duct carries bile into the duodenum."]),
        H("Practice"),
        PQ("State the site of secretion, the substrate and the product of pancreatic amylase.", "Pancreatic amylase is made in the pancreas and works in the duodenum. Its substrate is starch (and dextrins) and its main product is maltose."),
        PQ("Explain how the structure of the small intestine is adapted for absorption.", "Its length, the folds, the villi and the microvilli of the epithelial cells give a very large surface area. Each villus has a thin one-cell layer, a dense capillary network and a lacteal, so diffusion distances are short and the concentration gradient is kept steep by blood flow. Cells contain many mitochondria to supply energy for active transport."),
        PQ("Explain why oral rehydration solutions contain both glucose and salt.", "Glucose is absorbed together with sodium ions by the SGLT1 co-transporter. The absorbed solutes increase osmotic pressure in the cell layer and blood, so water follows by osmosis, which rehydrates the patient faster than water alone."),
        PQ("Essay plan: 'Describe the digestion and absorption of fats.'", "Introduction: fat is a triglyceride. Point 1: mechanical digestion and bile emulsification. Point 2: pancreatic lipase and the products. Point 3: micelle formation and absorption. Point 4: re-esterification, chylomicrons, lacteals, lymph. Point 5: short- and medium-chain fatty acids go directly to the portal vein. Evaluation: fat digestion depends on bile and pancreatic function; liver or pancreas disease causes fatty stools. Conclusion."),
        TIP("Exam link: digestion and absorption appear in Paper 1 (enzyme, substrate, product, site) and in Paper 2 (Section A application of nutritional science). Use tables with the site, enzyme, substrate and product for every nutrient."),
        SUM("Digestion is mainly hydrolysis by enzymes: amylase for starch, pepsin, trypsin and peptidases for protein, lipase (helped by bile) for fat.",
            "Most digestion and absorption happens in the small intestine, whose villi and microvilli give a huge surface area.",
            "Glucose, galactose and amino acids are absorbed by sodium-linked active transport; fructose by facilitated diffusion; fats by diffusion after micelle formation.",
            "Water-soluble products go to the liver by the hepatic portal vein; long-chain fats go by chylomicrons in the lymph.",
            "The large intestine absorbs water and salts and ferments fibre to short-chain fatty acids."),
    ],
))

# ------------------------------------------------------------------ 12. Metabolic pathways
LESSONS.append(lesson(
    module=M3,
    topic="Metabolic pathways",
    title="Metabolic pathways: glycolysis, gluconeogenesis, beta-oxidation, deamination and blood glucose control",
    slug="fsl1-metabolic-pathways",
    minutes=27,
    summary="Follow carbohydrate, fat and protein inside the cell. Learn glycolysis, the link to the Krebs cycle, gluconeogenesis, beta-oxidation and ketones, deamination and urea, and how insulin and glucagon keep blood glucose steady.",
    objectives=[
        "Outline glycolysis, its yield and its fate under aerobic and anaerobic conditions",
        "Explain gluconeogenesis, beta-oxidation and deamination and where they happen",
        "Assess how insulin and glucagon regulate blood glucose by negative feedback",
        "Calculate ATP yields for glucose and palmitic acid and connect them to diet and fasting",
    ],
    key_concepts=["Glycolysis", "Krebs cycle and oxidative phosphorylation", "Gluconeogenesis", "Beta-oxidation", "Ketone bodies", "Deamination and urea cycle", "Insulin and glucagon", "Negative feedback"],
    blocks=[
        H("Introduction"),
        T("After a meal of cassava and fish, glucose, amino acids and fatty acids flow into the blood. Hours later, between meals, blood glucose is still about the same. A student walking to school fasting uses fat, "
          "then stored glycogen, without the blood sugar crashing. **Metabolism** is the set of chemical reactions in cells, and the pathways you study here explain how the body keeps energy supply steady."),
        D("**Metabolism** is all the chemical reactions in a living cell. **Catabolism** breaks molecules down and releases energy as **ATP**; **anabolism** builds molecules and uses ATP.", title="Metabolism"),
        IMG("alfsl1-metabolism-map.svg", alt="Map of metabolism: glucose to pyruvate (glycolysis), pyruvate and fatty acids to acetyl CoA, Krebs cycle and electron transport making ATP, amino acid deamination to urea, and gluconeogenesis back to glucose",
            caption="Figure 1. Overview of the main pathways. Cytoplasm: glycolysis, gluconeogenesis. Mitochondrion: Krebs cycle, beta-oxidation, electron transport."),
        H("Glycolysis"),
        D("**Glycolysis** is the pathway in the cytoplasm that splits one glucose (6 carbon atoms) into two pyruvate (3 carbon atoms). No oxygen is needed. "
          "Net yield per glucose: 2 ATP (4 made, 2 used in the early steps) and 2 NADH.", title="Glycolysis", formula=r"\text{glucose} + 2\,\text{ADP} + 2\,\text{P}_i + 2\,\text{NAD}^+ \rightarrow 2\,\text{pyruvate} + 2\,\text{ATP} + 2\,\text{NADH} + 2\,\text{H}^+ + 2\,\text{H}_2\text{O}"),
        T("**With oxygen (aerobic):** pyruvate enters the mitochondrion, is converted to **acetyl-CoA** (by the pyruvate dehydrogenase complex, releasing CO2 and making NADH), and enters the **Krebs cycle**, "
          "which gives CO2, NADH, FADH2 and a little ATP. NADH and FADH2 pass electrons to the **electron transport chain**, where **oxidative phosphorylation** makes most of the ATP. "
          "**Without oxygen (anaerobic):** pyruvate is reduced to **lactate** in muscle (to regenerate NAD+) so glycolysis can continue briefly, giving a small amount of ATP. In yeast, pyruvate becomes ethanol and CO2."),
        T("The full oxidation of glucose gives about 30 to 32 ATP using modern values (2.5 ATP per NADH, 1.5 per FADH2). Older textbooks give 36 to 38 (3 and 2 per NADH and FADH2), so **check your textbook** and say which values you use."),
        EX("Worked example 1: ATP from glucose", intro="Count the ATP from one glucose, using modern values: 2.5 ATP per NADH, 1.5 per FADH2. Glycolysis gives 2 ATP and 2 NADH; pyruvate to acetyl-CoA gives 2 NADH; the Krebs cycle for two acetyl-CoA gives 6 NADH, 2 FADH2 and 2 ATP (as GTP).", steps=[
            S("Substrate-level ATP", math=r"2 + 2 = 4"),
            S("NADH", math=r"(2 + 2 + 6) \times 2.5 = 25"),
            S("FADH2", math=r"2 \times 1.5 = 3"),
            S("Total", math=r"4 + 25 + 3 = 32 \text{ ATP}"),
            S("Older values", text="With 3 ATP per NADH and 2 per FADH2 the total is 4 + 30 + 4 = 38."),
        ]),
        H("Gluconeogenesis"),
        D("**Gluconeogenesis** is the synthesis of glucose from non-carbohydrate sources: lactate, glycerol (from fat), and glucogenic amino acids. It occurs mainly in the liver (and kidney) and keeps blood glucose "
          "supplied during fasting. It reverses glycolysis, bypassing its three irreversible steps with other enzymes, and costs energy.", title="Gluconeogenesis"),
        T("Fatty acids **cannot** be converted to glucose in animals, because the two carbons of acetyl-CoA are lost as CO2 in the Krebs cycle. The brain and red blood cells depend on glucose "
          "(the brain also uses ketones in prolonged fasting), so gluconeogenesis from amino acids is a reason why prolonged fasting breaks down muscle protein. In the **Cori cycle**, "
          "muscle lactate goes to the liver, becomes glucose and returns to muscle."),
        EX("Worked example 2: cost of gluconeogenesis", intro="Making one glucose from two pyruvate needs 4 ATP, 2 GTP and 2 NADH. Using 2.5 ATP per NADH, find the energy cost in ATP equivalents and the net cost of the Cori cycle, where glycolysis in muscle gains 2 ATP. (Teaching values.)", steps=[
            S("Cost", math=r"4 + 2 + 2 \times 2.5 = 11 \text{ ATP-equivalents}"),
            S("Cori cycle", text="The liver spends 6 ATP-equivalents (4 ATP and 2 GTP, ignoring NADH) to make glucose and muscle gains 2 ATP from glycolysis, so the cycle has a net cost of 4 ATP-equivalents, paid by oxidation of other fuels."),
            S("Interpret", text="Gluconeogenesis is expensive, so it happens when carbohydrate is scarce."),
        ]),
        H("Beta-oxidation"),
        D("**Beta-oxidation** is the breakdown of fatty acids in the mitochondrion, two carbon atoms at a time. Each cycle removes an acetyl-CoA and makes one NADH and one FADH2. Acetyl-CoA enters the Krebs cycle.", title="Beta-oxidation"),
        EX("Worked example 3: ATP from palmitic acid", intro="Palmitic acid has 16 carbons. Calculate the ATP yield with modern values (2.5 per NADH, 1.5 per FADH2, 10 per acetyl-CoA through the Krebs cycle), remembering that activation costs 2 ATP-equivalents.", steps=[
            S("Cycles of beta-oxidation", math=r"\frac{16}{2} - 1 = 7"),
            S("Products", text="7 NADH, 7 FADH2 and 8 acetyl-CoA."),
            S("ATP", math=r"7 \times 2.5 + 7 \times 1.5 + 8 \times 10 - 2 = 17.5 + 10.5 + 80 - 2 = 106"),
            S("Compare per gram", math=r"\frac{106}{256.4} = 0.41 \text{ ATP/g} \quad \text{vs glucose } \frac{32}{180.2} = 0.18 \text{ ATP/g}"),
            S("Interpret", text="Fat gives about twice the ATP per gram of glucose, which agrees with 9 kcal/g for fat and about 4 kcal/g for carbohydrate. With older values the yield is 129."),
        ]),
        T("When carbohydrate is very low (fasting, starvation, uncontrolled diabetes, very low carbohydrate diets), the liver makes acetyl-CoA faster than the Krebs cycle can use it (the cycle runs short of oxaloacetate, "
          "which is drawn into gluconeogenesis). The extra acetyl-CoA is turned into **ketone bodies** (acetoacetate, 3-hydroxybutyrate, acetone), used as fuel by heart, muscle and, in long fasts, the brain. Excess ketones make the blood acidic (ketoacidosis), a danger in type 1 diabetes."),
        H("Amino acid metabolism: deamination"),
        D("**Deamination** is the removal of the amino group from an amino acid in the liver, giving a keto acid and ammonia. The ammonia, which is toxic, is converted to **urea** in the urea cycle and excreted by the kidneys. "
          "Often an amino group is first moved to another keto acid by **transamination**.", title="Deamination"),
        T("The remaining keto acid can enter the Krebs cycle for energy, be used in gluconeogenesis (glucogenic amino acids), or be converted into fat. This is why excess protein in the diet is "
          "used as energy or stored as fat and why the urine of someone on a high-protein diet carries more urea. About 16 percent of protein is nitrogen: 75 g of protein carries 12 g of nitrogen, which is excreted mostly as urea."),
        H("Blood glucose regulation: insulin and glucagon"),
        T("The Board's 2023 report notes that many candidates could not state the roles of insulin and glucagon in regulating blood glucose. Learn the loop below."),
        IMG("alfsl1-glucose-feedback.svg", alt="Feedback loop: high blood glucose releases insulin, which lowers it; low blood glucose releases glucagon, which raises it",
            caption="Figure 2. Blood glucose is kept by two opposing hormones (negative feedback)."),
        KEY("Insulin and glucagon", "The pancreas contains the islets of Langerhans.", cards=[
            ["Insulin (beta cells)", "Released when blood glucose is high. It increases glucose uptake into muscle and fat cells (by moving glucose transporters to the cell surface), stimulates the liver and muscle to form **glycogen** (glycogenesis), promotes fat synthesis and slows gluconeogenesis. Result: blood glucose falls."],
            ["Glucagon (alpha cells)", "Released when blood glucose is low. It acts on the liver to break glycogen to glucose (**glycogenolysis**) and to make glucose from amino acids and glycerol (gluconeogenesis), and increases fat breakdown. Result: blood glucose rises."],
            ["Other hormones", "Adrenaline (stress, rapid glycogen breakdown), cortisol and growth hormone also raise blood glucose over time."],
        ]),
        T("In a healthy person fasting blood glucose is kept at about 4 to 6 mmol per litre (check the current reference range with your textbook). In **type 1 diabetes** the beta cells fail, so little insulin is made. In **type 2 diabetes** tissues respond poorly to insulin. In both, glucose stays high; see the Upper Sixth lessons."),
        MISTAKE("Mixing up glycogenesis, glycogenolysis and gluconeogenesis", "Glycogenesis = glucose to glycogen (insulin). Glycogenolysis = glycogen to glucose (glucagon). Gluconeogenesis = new glucose from non-carbohydrate sources (glucagon). Look at the root: lysis = split; genesis = make."),
        QUIZ("Which pathway occurs in the cytoplasm and does NOT need oxygen?",
             ["Krebs cycle", "Beta-oxidation", "Glycolysis", "Electron transport"], 2,
             "Glycolysis takes place in the cytoplasm and needs no oxygen. The other three happen in the mitochondrion.",
             hint="Which pathway comes first for glucose?",
             feedback=["The Krebs cycle is in the mitochondrial matrix.", "Beta-oxidation is mitochondrial.", "", "The electron transport chain is on the inner mitochondrial membrane."]),
        QUIZ("Between meals, blood glucose begins to fall. Which response restores it?",
             ["Insulin release and glycogen synthesis", "Glucagon release, glycogen breakdown and gluconeogenesis in the liver", "Glucose uptake into muscle", "Conversion of glucose into fat"], 1,
             "Low glucose triggers glucagon, which raises blood glucose by glycogenolysis and gluconeogenesis.",
             hint="Which hormone works when glucose is low?",
             feedback=["Insulin lowers blood glucose.", "", "That lowers blood glucose.", "That also lowers blood glucose."]),
        H("Practice"),
        PQ("Outline the fate of pyruvate under aerobic and anaerobic conditions.", "With oxygen, pyruvate enters the mitochondrion, becomes acetyl-CoA, and is oxidised in the Krebs cycle and electron transport chain to CO2 and water with a large ATP yield. Without oxygen, in muscle, pyruvate is reduced to lactate so that NAD+ is regenerated and glycolysis can continue (in yeast, to ethanol and CO2)."),
        PQ("Assess the role of insulin and glucagon in the regulation of blood glucose.", "After a meal blood glucose rises; beta cells release insulin, which increases uptake of glucose by cells, glycogenesis in liver and muscle and fat synthesis, lowering blood glucose. When blood glucose falls, alpha cells release glucagon, which stimulates glycogenolysis and gluconeogenesis in the liver, raising it. This is negative feedback: each hormone reverses the change that triggered it. Evaluation: the system fails in diabetes (lack of insulin or insulin resistance), and other hormones (adrenaline, cortisol) also act."),
        PQ("Calculate the ATP yield from one stearic acid (C18) using modern values (2.5 per NADH, 1.5 per FADH2, 10 per acetyl-CoA, 2 for activation).", "Cycles = 18/2 - 1 = 8, giving 8 NADH, 8 FADH2 and 9 acetyl-CoA. ATP = 8 x 2.5 + 8 x 1.5 + 9 x 10 - 2 = 20 + 12 + 90 - 2 = 120."),
        PQ("Explain why fatty acids cannot be used to make glucose in animals, and why prolonged fasting breaks down muscle.", "In the Krebs cycle two carbon atoms of acetyl-CoA enter and two leave as CO2, so there is no net conversion of acetyl-CoA to oxaloacetate and so no way to build glucose. The brain and red blood cells need glucose, so the liver makes it by gluconeogenesis from glucogenic amino acids taken from muscle protein, and from glycerol."),
        TIP("Exam link: metabolic pathways appear in Paper 1 (site, product, hormone) and in Paper 2 (the Board's 2023 report names the roles of insulin and glucagon as a weak point). State the cells that release each hormone, the action and the effect on blood glucose."),
        SUM("Glycolysis (cytoplasm) turns one glucose into two pyruvate with a net 2 ATP and 2 NADH; aerobic fate is acetyl-CoA, Krebs cycle and electron transport.",
            "Gluconeogenesis makes glucose from lactate, glycerol and amino acids in the liver; fatty acids cannot be converted to glucose.",
            "Beta-oxidation splits fatty acids into acetyl-CoA, NADH and FADH2; excess acetyl-CoA makes ketone bodies when carbohydrate is scarce.",
            "Deamination removes amino groups in the liver; the ammonia becomes urea.",
            "Insulin lowers and glucagon raises blood glucose by negative feedback."),
    ],
))

# ------------------------------------------------------------------ 13. Energy expenditure and BMR
LESSONS.append(lesson(
    module=M3,
    topic="Energy expenditure and BMR",
    title="Components of energy expenditure: basal metabolic rate, thermic effect of food and activity",
    slug="fsl1-energy-expenditure-bmr",
    minutes=24,
    summary="Total energy expenditure has three main parts: BMR, the thermic effect of food and physical activity. Learn what BMR is and how it is defined, measured and changed, and how respiratory quotient reveals the fuel in use.",
    objectives=[
        "Define BMR precisely and state the conditions of its measurement",
        "Name the components of total energy expenditure and their approximate shares",
        "Explain the factors that raise or lower BMR",
        "Describe direct and indirect calorimetry and calculate energy from oxygen consumption and respiratory quotient",
    ],
    key_concepts=["Basal metabolic rate", "Resting metabolic rate", "Thermic effect of food", "Physical activity", "Calorimetry", "Respiratory quotient", "Fat-free mass"],
    blocks=[
        H("Introduction"),
        T("A farmer clearing land in the Western Highlands and a clerk sitting at a desk eat very different amounts. Even asleep, both burn energy to keep the heart beating, lungs working and body warm. "
          "The Board's 2023 report states that many candidates did not understand **Basal Metabolic Rate (BMR)**, so this lesson defines it carefully."),
        D("The **basal metabolic rate (BMR)** is the minimum rate of energy expenditure needed to keep the body alive at rest. It is measured in a person who is lying down, awake, relaxed, "
          "in a warm room (thermoneutral, about 20 to 25 degrees Celsius), 12 to 14 hours after the last meal (post-absorptive) and after a night of rest. "
          "It is expressed in kilocalories (kcal) or kilojoules (kJ) per day (or per hour, or in MJ per day).", title="BMR"),
        T("BMR pays for the heartbeat, breathing, brain and nerve activity, kidney and liver work, cell repair and keeping body temperature. In most adults it accounts for **60 to 75 percent** of total energy expenditure. "
          "The **resting metabolic rate (RMR)** is measured under less strict conditions and is slightly higher (a few percent). Many textbooks use the two terms almost interchangeably, so check how yours defines them."),
        H("Components of total energy expenditure"),
        KEY("Three main parts", "Together: total energy expenditure (TEE).", cards=[
            ["BMR", "About 60 to 75 percent of the total for most people."],
            ["Thermic effect of food (TEF), diet-induced thermogenesis", "Energy used to digest, absorb, transport and store food. About 10 percent of the energy eaten for a mixed diet. By nutrient: protein about 20 to 30 percent of its energy content, carbohydrate about 5 to 10 percent, fat 0 to 3 percent."],
            ["Physical activity", "The most variable part: about 15 to 30 percent in a sedentary person and much higher for farm or manual workers and athletes. Includes exercise and non-exercise activity such as walking, standing and fidgeting."],
            ["Special needs", "Growth in children and adolescents, pregnancy and lactation, and healing add to the total."],
        ]),
        T("A high-protein meal produces more heat than a high-fat meal of the same energy value, which is one of the reasons high-protein diets are popular for weight control; the effect is modest, however, and does not by itself explain weight changes."),
        EX("Worked example 1: share of BMR", intro="A woman's total energy expenditure is 2 700 kcal per day and her BMR is 1 700 kcal per day. Find the share of BMR, and the TEF if it is 10 percent of the energy she eats (assume she is in energy balance). (Teaching data.)", steps=[
            S("BMR share", math=r"\frac{1700}{2700} \times 100 = 63\%"),
            S("TEF", math=r"0.10 \times 2700 = 270 \text{ kcal}"),
            S("Activity and other", math=r"2700 - 1700 - 270 = 730 \text{ kcal}"),
            S("Share", math=r"\frac{730}{2700} \times 100 = 27\%"),
            S("Interpret", text="BMR dominates; activity accounts for about a quarter of the total."),
        ]),
        H("Factors affecting BMR"),
        KEY("What raises or lowers BMR", "Think: body size, body composition, age, sex, hormones, temperature, state of health.", cards=[
            ["Body size and composition", "Larger bodies use more energy. Lean tissue (muscle and organs) is metabolically more active than fat, so a person with more fat-free mass has a higher BMR. This is why BMR is often related to fat-free mass."],
            ["Age", "Highest per kilogram in infants and children (growth), and falls in adults with age as lean mass is lost."],
            ["Sex", "Men have higher BMR than women of the same weight on average, mainly because they have more lean mass."],
            ["Hormones", "Thyroid hormones (thyroxine) set metabolic rate: raised in an overactive thyroid and lowered in an underactive one. Adrenaline raises it briefly."],
            ["Body temperature and climate", "Fever raises BMR (roughly 10 to 13 percent per degree Celsius; check your textbook). Very hot or cold environments raise it slightly."],
            ["Pregnancy, lactation and growth", "Raise BMR."],
            ["Starvation and fasting, prolonged low intake", "Lower BMR through loss of lean tissue and hormonal adaptation, which makes weight loss slow down."],
            ["Genetics and individual variation", "Account for some of the differences between people of similar size."],
        ]),
        H("Measuring energy expenditure"),
        T("**Direct calorimetry** measures the heat released by a person in an insulated chamber. It is accurate but expensive and used only in research. "
          "**Indirect calorimetry** measures the oxygen consumed (and carbon dioxide produced), because energy release is linked to oxygen use: about **4.8 to 5.0 kcal (about 20 kJ) per litre of oxygen**, "
          "depending on the fuel used. Another method is doubly-labelled water for free-living people."),
        D(r"The **respiratory quotient (RQ)** is the volume of carbon dioxide produced divided by the volume of oxygen used. It shows which fuel is being oxidised: about 1.0 for carbohydrate, about 0.7 for fat and about 0.8 to 0.85 for protein (a mixed diet gives about 0.85).",
          title="Respiratory quotient", formula=r"\text{RQ} = \frac{V_{\text{CO}_2}}{V_{\text{O}_2}}"),
        EX("Worked example 2: RQ of glucose and palmitic acid", intro="Glucose: C6H12O6 + 6 O2 gives 6 CO2 + 6 H2O. Palmitic acid: C16H32O2 + 23 O2 gives 16 CO2 + 16 H2O. Find each RQ.", steps=[
            S("Glucose", math=r"\text{RQ} = \frac{6}{6} = 1.0"),
            S("Palmitic acid", math=r"\text{RQ} = \frac{16}{23} = 0.70"),
            S("Interpret", text="A measured RQ of 0.7 shows mainly fat is being burned (fasting); a value near 1.0 shows mainly carbohydrate (after a high-carbohydrate meal)."),
        ]),
        EX("Worked example 3: BMR from oxygen use", intro="A subject at rest uses 250 mL of oxygen per minute and produces 205 mL of carbon dioxide per minute. Find the RQ and estimate BMR in kcal per day using 4.85 kcal per litre of oxygen. (Teaching data.)", steps=[
            S("RQ", math=r"\frac{205}{250} = 0.82"),
            S("Energy per minute", math=r"0.250 \times 4.85 = 1.2125 \text{ kcal/min}"),
            S("Per day", math=r"1.2125 \times 1440 = 1746 \text{ kcal/day}"),
            S("Convert to kJ", math=r"1746 \times 4.184 = 7306 \text{ kJ/day} \approx 7.3 \text{ MJ/day}"),
        ]),
        MISTAKE("Defining BMR as the energy used by sleeping or by 'doing nothing'", "BMR is measured awake, lying at rest, fasted for 12 hours or so in a warm room. Sleeping metabolic rate is a little lower and RMR a little higher. A good answer lists the conditions and the purposes (heartbeat, breathing, temperature)."),
        QUIZ("Which statement about BMR is correct?",
             ["It includes the energy of digesting a meal eaten an hour earlier", "It is the energy needed to maintain life at rest under standard conditions", "It is the same in all adults", "It falls when lean mass rises"], 1,
             "BMR is the minimum expenditure for vital functions in a post-absorptive, rested, warm, relaxed subject.",
             hint="Which statement mentions standard conditions?",
             feedback=["That would be the thermic effect of food, which BMR excludes by fasting.", "", "BMR varies with size, sex, age and more.", "More lean mass raises BMR."]),
        QUIZ("A measurement of RQ gives 0.71. What is the main fuel being burned?",
             ["Carbohydrate", "Fat", "Protein", "Alcohol only"], 1,
             "RQ near 0.7 corresponds to fat oxidation (for example palmitic acid 16/23).",
             hint="Which fuel needs a lot of oxygen per CO2 produced?",
             feedback=["Carbohydrate has RQ 1.0.", "", "Protein is about 0.8.", "Alcohol has an RQ of about 0.67, but is unlikely as the main fuel in a fasting subject."]),
        H("Practice"),
        PQ("Define basal metabolic rate and state three conditions under which it is measured.", "BMR is the minimum rate of energy expenditure needed to keep the body alive at rest. It is measured in a subject who is awake and lying relaxed, in a warm (thermoneutral) room, and fasted for about 12 hours (post-absorptive)."),
        PQ("Explain why two people of the same body weight can have different BMR.", "Body composition: the person with more lean mass (muscle and organs) has a higher BMR because lean tissue is metabolically more active than fat. Age (BMR falls with age), sex (men have more lean mass), thyroid hormones, temperature or illness, and genetics also differ."),
        PQ("Calculate the RQ for stearic acid, C18H36O2 + 26 O2 giving 18 CO2 + 18 H2O.", "RQ = 18 / 26 = 0.69."),
        PQ("Essay plan: 'Discuss the factors that affect the energy needs of an individual.'", "Introduction: components of total energy expenditure. Point 1: BMR and what changes it (size, composition, age, sex, hormones, climate, health). Point 2: thermic effect of food. Point 3: physical activity (occupation, exercise). Point 4: growth, pregnancy and lactation. Evaluation: BMR is the largest, but activity is the most changeable; individual variation. Conclusion."),
        TIP("Exam link: energy expenditure and BMR have been named by the Board as weakly answered. Expect questions in Paper 1 (definition) and in Paper 2 (Section A application of nutritional science, with calculations). State all conditions in the definition."),
        SUM("BMR is the minimum energy for life at rest, measured awake, relaxed, warm and fasted; it is 60 to 75 percent of expenditure.",
            "TEE = BMR + thermic effect of food (about 10 percent) + physical activity (+ growth or pregnancy where relevant).",
            "BMR rises with lean mass, growth, thyroid hormones, fever and pregnancy, and falls with age and starvation.",
            "Indirect calorimetry uses oxygen consumption (about 4.85 kcal per litre) and RQ.",
            "RQ is about 1.0 for carbohydrate, 0.7 for fat and 0.8 for protein."),
    ],
))

# ------------------------------------------------------------------ 14. Energy requirement calculations
LESSONS.append(lesson(
    module=M3,
    topic="Energy requirement calculations",
    title="Calculating energy requirements: BMR equations, PAL, food energy and the food composition table",
    slug="fsl1-energy-requirement-calculations",
    minutes=27,
    summary="Estimate BMR from weight (Schofield, Harris-Benedict or Mifflin-St Jeor), multiply by a physical activity level to find total daily energy, then compare with the energy in food from the Atwater factors and the food composition table.",
    objectives=[
        "Calculate BMR using a prediction equation and convert between kcal, kJ and MJ",
        "Calculate total daily energy expenditure from BMR and PAL, and from a time-and-activity record",
        "Calculate the energy value of foods and meals using Atwater factors and a food composition table",
        "Convert an energy target into grams of carbohydrate, fat and protein and estimate changes in body weight",
    ],
    key_concepts=["Prediction equation", "Physical activity level (PAL)", "Atwater factors", "Food composition table", "kcal, kJ and MJ", "Energy balance"],
    blocks=[
        H("Introduction"),
        T("How much should a 70 kg student eat in a day? How many kilocalories are in a plate of rice, beans, fish and palm oil? In the practical paper the Board's 2023 report found that candidates struggled with "
          "calculations that need the **food composition table (FCT)**, and recommends that the Board's FCT is studied and used in lessons. This lesson gives the full calculating method."),
        T("**Teaching note:** the equations below are widely published (Schofield 1985 in the FAO/WHO/UNU report, Harris-Benedict as revised in 1984, Mifflin-St Jeor 1990). Textbooks may give different versions or round the coefficients differently: "
          "**check your textbook and use the equation your teacher or the Board's booklet supplies**. The food values in this lesson are invented for practice and are not taken from the Board's table."),
        H("Units"),
        F(r"1 \text{ kcal} = 4.184 \text{ kJ}, \qquad 1 \text{ MJ} = 1000 \text{ kJ}"),
        T("A 2 000 kcal diet is $2000 \\times 4.184 = 8368$ kJ, or about 8.4 MJ. Always give the unit and say which one you are using."),
        H("Step 1: BMR from an equation"),
        KEY("Schofield equations (kcal per day, W = body weight in kg)", "From the 1985 FAO/WHO/UNU report; check your textbook.", cards=[
            ["Males 18 to 29 years", "BMR = 15.057 W + 692.2"],
            ["Males 30 to 59 years", "BMR = 11.472 W + 873.1"],
            ["Females 18 to 29 years", "BMR = 14.818 W + 486.6"],
            ["Females 30 to 59 years", "BMR = 8.126 W + 845.6"],
        ]),
        KEY("Other equations (W in kg, H in cm, A in years; kcal per day)", "These use height and age as well.", cards=[
            ["Harris-Benedict (revised 1984), male", "BMR = 88.362 + 13.397 W + 4.799 H - 5.677 A"],
            ["Harris-Benedict (revised 1984), female", "BMR = 447.593 + 9.247 W + 3.098 H - 4.330 A"],
            ["Mifflin-St Jeor, male", "BMR = 10 W + 6.25 H - 5 A + 5"],
            ["Mifflin-St Jeor, female", "BMR = 10 W + 6.25 H - 5 A - 161"],
        ]),
        EX("Worked example 1: BMR of a young man", intro="Find the BMR of a man aged 25, weight 70 kg, height 175 cm, using each equation.", steps=[
            S("Schofield (18 to 29 years)", math=r"15.057 \times 70 + 692.2 = 1746 \text{ kcal}"),
            S("Harris-Benedict", math=r"88.362 + 13.397(70) + 4.799(175) - 5.677(25) = 1724 \text{ kcal}"),
            S("Mifflin-St Jeor", math=r"10(70) + 6.25(175) - 5(25) + 5 = 1674 \text{ kcal}"),
            S("Compare", text="The estimates differ by about 70 kcal (4 percent), which is normal: they are predictions for populations, not measurements of one person."),
        ]),
        H("Step 2: total energy from the physical activity level"),
        D(r"The **physical activity level (PAL)** is total energy expenditure divided by BMR. $\text{TEE} = \text{BMR} \times \text{PAL}$. The FAO/WHO/UNU (2004) classes are: sedentary or light activity 1.40 to 1.69; "
          r"active or moderately active 1.70 to 1.99; vigorous 2.00 to 2.40 (check your textbook).", title="PAL", formula=r"\text{TEE} = \text{BMR} \times \text{PAL}"),
        EX("Worked example 2: a student's daily requirement", intro="The young man above (BMR 1 746 kcal by Schofield) is moderately active with PAL 1.75. Find his estimated energy requirement in kcal, kJ and MJ.", steps=[
            S("TEE", math=r"1746 \times 1.75 = 3056 \text{ kcal}"),
            S("kJ", math=r"3056 \times 4.184 = 12\,786 \text{ kJ}"),
            S("MJ", math=r"\approx 12.8 \text{ MJ per day}"),
        ]),
        EX("Worked example 3: PAL from a time and activity record", intro="A farm worker has a BMR of 1 700 kcal per day. In 24 h: 8 h sleep (1.0 x BMR), 8 h sitting and light tasks (1.5), 5 h walking and light work (2.5), 2 h cooking and housework (2.8) and 1 h vigorous farm work (6.0). Find the PAL and TEE. (Activity ratios are teaching values.)", steps=[
            S("Sum of hours times ratios", math=r"8(1.0) + 8(1.5) + 5(2.5) + 2(2.8) + 1(6.0) = 8 + 12 + 12.5 + 5.6 + 6 = 44.1"),
            S("PAL", math=r"\frac{44.1}{24} = 1.84"),
            S("TEE", math=r"1700 \times 1.84 = 3124 \text{ kcal}"),
            S("Class", text="This PAL is in the active range (1.70 to 1.99), as expected for a farm worker."),
        ]),
        H("Step 3: energy value of food"),
        T("The usual energy factors (**Atwater factors**) are: carbohydrate 4 kcal per g (17 kJ), protein 4 kcal (17 kJ), fat 9 kcal (37 kJ), alcohol 7 kcal (29 kJ); fibre is given a lower value (about 2 kcal, or 8 kJ) in some tables. "
          "A food composition table gives the grams of each nutrient per 100 g of edible food, usually with the energy already calculated."),
        EX("Worked example 4: energy in a meal using a food composition table", intro="Use these invented values per 100 g: cooked rice (carbohydrate 28 g, protein 2.7 g, fat 0.3 g); cooked beans (20 g, 8 g, 0.5 g); palm oil (0, 0, 100 g); fish (0, 20 g, 5 g). Calculate the energy of a meal of 200 g rice, 100 g beans, 15 g palm oil and 80 g fish.", steps=[
            S("Rice, per 100 g", math=r"28(4) + 2.7(4) + 0.3(9) = 125.5 \text{ kcal}, \quad \text{so } 200 \text{ g} = 251.0 \text{ kcal}"),
            S("Beans, 100 g", math=r"20(4) + 8(4) + 0.5(9) = 116.5 \text{ kcal}"),
            S("Palm oil, 15 g", math=r"15 \times 9 = 135.0 \text{ kcal}"),
            S("Fish, 80 g", math=r"(20(4) + 5(9)) \times 0.8 = 125 \times 0.8 = 100.0 \text{ kcal}"),
            S("Total", math=r"251.0 + 116.5 + 135.0 + 100.0 = 602.5 \text{ kcal} = 2521 \text{ kJ}"),
            S("Compare with the requirement", text="602.5 / 2 400 = 25 percent of a 2 400 kcal requirement."),
        ]),
        T("**Using the Board's FCT:** read the right row for the food in its prepared state (raw, boiled, fried), use the column for edible portion, and scale by weight eaten divided by 100. "
          "Do not mix tables: the Board's report asks that only the FCT provided by the Board is used for teaching."),
        H("Step 4: energy balance and body weight, and macronutrient targets"),
        T("If intake equals expenditure, body weight is steady. A daily deficit of 500 kcal for a week is 3 500 kcal, which is only about 0.45 kg of body fat if one kilogram of body fat is taken as roughly 7 700 kcal "
          "(this is a rough rule: real changes vary and metabolism adapts)."),
        EX("Worked example 5: macronutrient grams", intro="A person needs 2 400 kcal. A planner wants 55 percent of energy from carbohydrate, 30 percent from fat and 15 percent from protein. Find the grams of each.", steps=[
            S("Carbohydrate", math=r"\frac{0.55 \times 2400}{4} = 330 \text{ g}"),
            S("Fat", math=r"\frac{0.30 \times 2400}{9} = 80 \text{ g}"),
            S("Protein", math=r"\frac{0.15 \times 2400}{4} = 90 \text{ g}"),
            S("Check", math=r"330(4) + 80(9) + 90(4) = 1320 + 720 + 360 = 2400 \text{ kcal}"),
        ]),
        MISTAKE("Forgetting units, wrong age band, or double counting", "Use the age and sex row that fits; use weight in kg; show kcal and kJ clearly; apply PAL once to the BMR (do not add TEF on top, because PAL already includes it); and remember that equation answers are estimates. For pregnancy, lactation, growth, illness and other special cases, extra energy is added: use the table in your syllabus or the FAO guidance (check the current values)."),
        QUIZ("A woman aged 40 weighs 55 kg. Using Schofield (30 to 59 years: 8.126 W + 845.6), what is her estimated BMR (kcal per day, to the nearest 10)?",
             ["1 290", "1 450", "1 070", "2 000"], 0,
             "8.126 x 55 = 446.9; adding 845.6 gives 1 292.5, about 1 290 kcal.",
             hint="Multiply the weight by 8.126, then add 845.6.",
             feedback=["", "That would use the 18 to 29 years coefficients or an incorrect sum.", "That adds only part of the equation.", "That is closer to TEE with a PAL, not BMR."]),
        QUIZ("Which is the correct order for estimating daily energy needs?",
             ["PAL, then BMR, then add TEF", "BMR from an equation, then multiply by PAL", "Atwater factors, then PAL", "BMR plus PAL"], 1,
             "Estimate BMR first, then multiply by PAL, which already includes activity and the thermic effect of food.",
             hint="PAL is a multiplier.",
             feedback=["PAL includes TEF, and BMR must be found first.", "", "Atwater factors give food energy, not requirements.", "PAL is a multiplier, not an amount to add."]),
        H("Practice"),
        PQ("Calculate the energy requirement in kcal and MJ of a man whose BMR is 1 800 kcal per day and whose PAL is 1.6.", "TEE = 1 800 x 1.6 = 2 880 kcal. In kJ: 2 880 x 4.184 = 12 050 kJ, which is 12.0 MJ."),
        PQ("A food contains 12 g protein, 30 g carbohydrate and 8 g fat per 100 g. Calculate its energy value per 100 g and in a 150 g portion.", "Per 100 g: 12 x 4 + 30 x 4 + 8 x 9 = 48 + 120 + 72 = 240 kcal. For 150 g: 240 x 1.5 = 360 kcal."),
        PQ("Use the Mifflin-St Jeor equation to estimate the BMR of a woman aged 25, weight 60 kg, height 165 cm.", "BMR = 10 x 60 + 6.25 x 165 - 5 x 25 - 161 = 600 + 1031.25 - 125 - 161 = 1 345 kcal per day."),
        PQ("Essay plan: 'Explain how the energy requirement of an adult is estimated and why estimates differ between people.'", "Introduction: energy balance. Point 1: BMR from prediction equations (state one) and what it depends on. Point 2: multiply by PAL, with classes. Point 3: extra needs (growth, pregnancy, lactation, illness). Point 4: check intake using food tables and Atwater factors. Evaluation: equations are population averages; measuring by calorimetry or monitoring weight change gives a better check. Conclusion."),
        TIP("Exam link: energy calculations appear in Paper 2 (Section A) and in the practical paper (the Board's report records difficulty with the calculation that uses the food composition table). Show every step with units, state which table and equation you used, and check that the numbers are reasonable."),
        SUM("Convert units with 1 kcal = 4.184 kJ; 1 MJ = 1 000 kJ.",
            "Estimate BMR with an equation using weight (and sometimes height and age); different equations give slightly different results.",
            "Total energy expenditure = BMR x PAL; PAL comes from tables or a time-and-activity record.",
            "Food energy uses 4 kcal per g for carbohydrate and protein and 9 for fat, or the food composition table values scaled to the portion.",
            "Compare intake with requirement and convert energy shares to grams; a 500 kcal daily deficit is only about 0.45 kg a week."),
    ],
))
