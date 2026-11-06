"""Form 5 Biology: Nutrition in Plants & Animals and Respiration & Gaseous Exchange. 12 lessons, one practice set each.

Content source: KKEVO master curriculum blueprint (modules BIO-0510-M3 and M4) and the Board's 2023 Ordinary Level
subject report (Paper 1 has 50 multiple-choice questions, Paper 2 has essay-type questions).
Numbers drawn on graphs and charts are simple teaching data, not measured results.
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "form-5")

NUT = "Nutrition in Plants & Animals"
RESP = "Respiration & Gaseous Exchange"

LESSONS = []

# ------------------------------------------------------------------ 1. Food nutrients
LESSONS.append(lesson(
    module=NUT,
    topic="Food nutrients",
    title="Food nutrients: what each one does",
    slug="bib-food-nutrients-and-their-functions",
    minutes=22,
    summary="The seven parts of a balanced diet (carbohydrates, proteins, lipids, vitamins, minerals, water and fibre), what each one does in the body, good Cameroonian sources, and the diseases caused by too little of some of them.",
    objectives=[
        "Name the seven components of a balanced diet and give two food sources of each",
        "State the main function of carbohydrates, proteins, lipids, vitamins, minerals, water and fibre",
        "Name the deficiency disease linked with vitamins C and D, iron, iodine and protein",
        "Calculate the energy in a food from the mass of each nutrient",
    ],
    key_concepts=["Nutrient", "Balanced diet", "Carbohydrate", "Protein", "Lipid", "Vitamin", "Mineral", "Fibre (roughage)", "Deficiency disease"],
    blocks=[
        H("Introduction"),
        T("Think about a plate at a Douala market stall: boiled plantain, koki beans, a piece of fish, some njama njama "
          "leaves and a glass of water. Each item gives your body something different. Plantain gives energy. Beans and "
          "fish help you grow. The leaves help your blood and eyes."),
        T("In this lesson you will learn the seven kinds of **nutrient** your body needs, what each one does, and "
          "what goes wrong when one is missing."),
        D("**Food** is any substance that an organism takes in to give energy, for growth and repair, and to keep the body working.",
          title="Definition: food"),
        D("A **nutrient** is a chemical substance in food that the body needs. A **balanced diet** contains all the nutrients in the right amounts.",
          title="Definition: nutrient and balanced diet"),
        KEY("The seven parts of a balanced diet", "Learn the name and the main job of each one.", cards=[
            ["Carbohydrates", "Main source of energy."],
            ["Proteins", "Growth and repair of body cells."],
            ["Lipids (fats and oils)", "Energy store, insulation and protection."],
            ["Vitamins", "Small amounts needed to keep the body healthy."],
            ["Mineral salts", "Build bones, teeth and blood; help many body processes."],
            ["Water", "Solvent and transport; most of every cell."],
            ["Fibre (roughage)", "Keeps food moving through the gut."],
        ]),
        H("Carbohydrates"),
        T("Carbohydrates contain the elements carbon, hydrogen and oxygen. They are the cheapest and quickest source of energy. "
          "Sugars such as glucose are small molecules. **Starch** is a large molecule made of many glucose units joined together. "
          "**Cellulose** is another long chain; humans cannot digest it, so it acts as fibre."),
        T("Cassava, yam, plantain, rice, maize, bread and sugar cane are all rich in carbohydrates. Carbohydrate that the body "
          "does not need at once is changed to fat and stored."),
        H("Proteins"),
        T("Proteins contain carbon, hydrogen, oxygen and **nitrogen** (and sometimes sulphur). They are long chains of small units called "
          "**amino acids**. Your body uses proteins to build muscle, skin, hair and blood, to repair wounds, and to make enzymes and antibodies."),
        T("Good sources are beans, groundnuts, soya, eggs, fish, meat and milk. Children who do not get enough protein may develop "
          "**kwashiorkor**: a swollen belly, thin arms and legs and poor growth."),
        H("Lipids"),
        T("Lipids (fats and oils) contain carbon, hydrogen and oxygen. A lipid is made of **glycerol** and **fatty acids**. "
          "Lipids give more than twice as much energy per gram as carbohydrates. They are stored under the skin, where they keep "
          "the body warm (insulation) and cushion organs such as the kidneys. They are also part of every cell membrane."),
        T("Palm oil, groundnut oil, avocado, safou, butter and fatty fish are rich in lipids."),
        H("Vitamins and mineral salts"),
        T("The body needs only tiny amounts of vitamins and minerals, but it becomes ill without them. A shortage causes a "
          "**deficiency disease**."),
        CODE("""Nutrient     Main use in the body            Deficiency disease      Some sources
Vitamin A    Healthy eyes and skin           Night blindness         Carrot, red palm oil, liver
Vitamin C    Healthy gums and skin, healing  Scurvy (bleeding gums)  Orange, guava, pawpaw
Vitamin D    Takes calcium into bones        Rickets (soft bones)    Sunlight on skin, eggs, fish oil
Calcium      Bones, teeth, blood clotting    Weak bones and teeth    Milk, beans, small fish
Iron         Makes haemoglobin in red cells  Anaemia (pale, tired)   Liver, beans, dark green leaves
Iodine       Makes thyroxine (thyroid)       Goitre (swollen neck)   Iodised salt, sea fish""", "text",
             title="Some vitamins and minerals"),
        T("Rickets is a disease of children. Their leg bones are too soft and bend under the weight of the body. "
          "Vitamin D is made in the skin in sunlight, so it is one vitamin that you can make yourself."),
        H("Water and fibre"),
        T("**Water** is about 60 to 70 percent of the human body. It dissolves substances so they can be carried in blood, "
          "it takes part in chemical reactions such as digestion, and it helps to cool the body as sweat. We lose water in sweat, "
          "urine, faeces and breath, so we must replace it."),
        T("**Fibre** (roughage) is mainly cellulose from plant cell walls. We cannot digest it. It adds bulk to the food and "
          "helps the gut muscles push it along, so it prevents constipation. Vegetables, fruits, beans and whole grains contain fibre."),
        H("Energy in food"),
        T("The energy in food is measured in **kilojoules (kJ)**. Textbooks give slightly different values, so check your "
          "textbook. These are the values used in this lesson:"),
        CODE("""Carbohydrate   about 17 kJ per gram
Protein        about 17 kJ per gram
Lipid          about 38 kJ per gram""", "text", title="Approximate energy values"),
        EX("Worked example 1: energy in a snack", intro="A snack contains 20 g of carbohydrate, 5 g of protein and 10 g of lipid. Find the total energy.", steps=[
            S("Energy from carbohydrate", math=r"20 \times 17 = 340 \text{ kJ}"),
            S("Energy from protein", math=r"5 \times 17 = 85 \text{ kJ}"),
            S("Energy from lipid", math=r"10 \times 38 = 380 \text{ kJ}"),
            S("Add them", math=r"340 + 85 + 380 = 805 \text{ kJ}"),
        ]),
        EX("Worked example 2: choose the nutrient", intro="A child in a village has swollen legs, a swollen belly and poor growth. Her meals are mostly cassava. Which nutrient is she lacking, and what food would help?", steps=[
            S("Match the signs", text="A swollen belly with thin limbs and poor growth is the sign of kwashiorkor."),
            S("Name the nutrient", text="Kwashiorkor is caused by a lack of protein. Cassava is almost all carbohydrate."),
            S("Suggest food", text="Add beans, eggs, fish, groundnuts or milk to the meals."),
        ]),
        MISTAKE("Saying vitamins and minerals give energy", "Only carbohydrates, lipids and proteins release energy. Vitamins, minerals, water and fibre do not."),
        MISTAKE("Spelling the names wrongly", "Examiners see spellings such as 'protine' and 'vitamine'. Learn: protein, carbohydrate, lipid, vitamin, mineral, kwashiorkor, anaemia, rickets."),
        TIP("In Paper 1 multiple choice, nutrient functions and deficiency diseases are common knowledge questions. In Paper 2 essays you may be asked to describe a balanced diet or to explain the function of one nutrient."),
        QUIZ("Which nutrient is the main source of energy for the body?", ["Protein", "Carbohydrate", "Vitamin C", "Fibre"], 1,
             "Carbohydrates are broken down quickly to release energy.",
             hint="Think about cassava, rice and plantain.",
             feedback=["Protein is mainly for growth and repair; it is used for energy only when other foods are short.", "",
                       "Vitamin C is needed in tiny amounts and gives no energy.", "Fibre is not digested, so it gives no energy."]),
        QUIZ("A lack of iron in the diet causes:", ["Rickets", "Scurvy", "Anaemia", "Goitre"], 2,
             "Iron is needed to make haemoglobin. Without enough, the blood carries less oxygen and the person is pale and tired.",
             hint="Which mineral is part of haemoglobin?",
             feedback=["Rickets is caused by too little vitamin D (and calcium).", "Scurvy is caused by too little vitamin C.", "",
                       "Goitre is caused by too little iodine."]),
        PQ("Name the elements present in a protein but not in a carbohydrate.", "Nitrogen (and sometimes sulphur). Carbohydrates contain only carbon, hydrogen and oxygen."),
        PQ("State two uses of lipids in the body.", "Any two: a store of energy; insulation to keep the body warm; protection of organs; part of cell membranes."),
        PQ("A food has 30 g carbohydrate, 10 g protein and 5 g lipid. Calculate the energy using 17 kJ/g for carbohydrate and protein and 38 kJ/g for lipid.", "30 × 17 = 510 kJ; 10 × 17 = 170 kJ; 5 × 38 = 190 kJ. Total = 510 + 170 + 190 = 870 kJ."),
        PQ("Why should a balanced diet contain fibre even though it gives no energy?", "Fibre adds bulk and helps the muscles of the gut push food along (peristalsis). It prevents constipation."),
        SUM("A balanced diet has seven parts: carbohydrates, proteins, lipids, vitamins, mineral salts, water and fibre.",
            "Carbohydrates and lipids give energy; proteins build and repair; vitamins and minerals protect health.",
            "Deficiency diseases: vitamin C scurvy, vitamin D rickets, iron anaemia, iodine goitre, protein kwashiorkor.",
            "Energy in food is about 17 kJ per gram for carbohydrate and protein and about 38 kJ per gram for lipid.",
            "Fibre and water carry no energy but are essential."),
    ],
))

# ------------------------------------------------------------------ 2. Food tests
LESSONS.append(lesson(
    module=NUT,
    topic="Food tests",
    title="Food tests and their colour changes",
    slug="bib-food-tests-and-colour-changes",
    minutes=22,
    summary="How to test a food for starch (iodine), reducing sugar (Benedict's), non-reducing sugar, protein (Biuret), lipid (emulsion) and vitamin C (DCPIP), the exact colour changes, and how to read a table of results.",
    objectives=[
        "Describe the test for starch, reducing sugar, non-reducing sugar, protein, lipid and vitamin C",
        "State the colour change for a positive result in each test",
        "Interpret a table of food-test results and name the nutrients present",
        "Describe safety steps and the use of a control in food tests",
    ],
    key_concepts=["Food test", "Iodine solution", "Benedict's test", "Reducing sugar", "Biuret test", "Emulsion test", "DCPIP", "Control"],
    blocks=[
        H("Introduction"),
        T("A student buys a snack from a roadside seller and wonders what is in it. Is it mostly starch? Does it contain "
          "protein? In the laboratory we find out with **food tests**. Each test uses a reagent (a chemical) that changes "
          "colour when a particular nutrient is present."),
        D("A **food test** is a simple chemical test in which a reagent changes colour (or makes a cloudy liquid) to show that a particular nutrient is in a food.",
          title="Definition: food test"),
        T("Look at the colour chart. You must learn each colour change, because examiners ask for the exact colours."),
        IMG("f5bi-b-food-test-colours.svg", alt="Colour chart: iodine goes from yellow-brown to blue-black; Benedict's goes blue, green, yellow, orange, brick-red; Biuret goes blue to purple; emulsion test goes clear to cloudy white; DCPIP goes blue to colourless",
            caption="Figure 1. The standard colour changes for the food tests."),
        H("Test for starch"),
        T("Put a small piece of food (or a drop of its solution) on a white tile. Add two or three drops of **iodine solution**. "
          "Iodine solution is yellow-brown."),
        D("**Starch** is present if the iodine solution changes from yellow-brown to **blue-black**. If the colour stays yellow-brown, there is no starch.",
          title="Result: starch test"),
        H("Test for reducing sugars"),
        T("**Reducing sugars** are sugars such as glucose, fructose, maltose and lactose. Benedict's solution is blue and contains copper(II) ions."),
        CODE("""1. Crush the food and shake it with a little water in a test tube.
2. Add an equal volume of Benedict's solution (blue).
3. Heat in a boiling water bath for about 5 minutes.
4. Look at the colour.""", "text", title="Benedict's test"),
        D("A reducing sugar is present if the blue solution changes through **green, yellow and orange to a brick-red precipitate**. The more reducing sugar there is, the further the colour goes towards brick-red. If it stays blue, there is no reducing sugar.",
          title="Result: Benedict's test"),
        H("Test for a non-reducing sugar"),
        T("Sucrose (table sugar) is a **non-reducing sugar**. It gives no colour change with Benedict's solution. To test for it, "
          "first break it into reducing sugars."),
        CODE("""1. Do the Benedict's test. It stays blue, so no reducing sugar.
2. Boil a fresh sample with dilute hydrochloric acid for about 2 minutes.
   The acid breaks sucrose into glucose and fructose.
3. Cool, then add sodium hydrogencarbonate until it stops fizzing
   (this neutralises the acid; Benedict's will not work in acid).
4. Do the Benedict's test again.""", "text", title="Test for sucrose"),
        T("A brick-red precipitate now shows that a non-reducing sugar was present."),
        H("Test for protein (Biuret test)"),
        T("Add an equal volume of dilute sodium hydroxide to the food solution. Then add a few drops of dilute copper(II) sulfate "
          "solution, drop by drop, and shake."),
        D("**Protein** is present if the blue solution changes to **purple (violet)**. If it stays blue, there is no protein.",
          title="Result: Biuret test"),
        H("Test for lipids (emulsion test)"),
        T("Crush the food and shake it well with about 2 cm³ of **ethanol**. Allow the solids to settle. Pour the clear liquid into "
          "a test tube of water."),
        D("**Lipid** is present if a **cloudy white emulsion** forms. If the liquid stays clear, there is no lipid. Lipids dissolve in ethanol but not in water, so tiny droplets spread through the water and make it cloudy.",
          title="Result: emulsion test"),
        TIP("A quick extra test for lipid: rub the food on filter paper. A lipid leaves a translucent (see-through) grease spot that does not dry."),
        H("Test for vitamin C"),
        T("**DCPIP** is a blue dye. Put 1 cm³ of DCPIP in a test tube. Add the food juice drop by drop, shaking each time."),
        D("**Vitamin C** is present if the blue DCPIP becomes **colourless**. The fewer drops of juice needed, the more vitamin C the juice contains.",
          title="Result: DCPIP test"),
        H("Safety and a fair test"),
        T("Wear eye protection. Heat tubes in a water bath, not over a flame, and point the tube away from faces. Use a **control**: "
          "do the same test on distilled water. The control shows the colour of a negative result, so you can see whether the food made a real change."),
        EX("Worked example 1: reading a table of results", intro="Food X was tested. Iodine solution stayed yellow-brown. Benedict's solution gave a brick-red precipitate. Biuret reagent stayed blue. The ethanol test stayed clear. Which nutrient is in food X?", steps=[
            S("Starch test", text="Yellow-brown stayed. No starch."),
            S("Benedict's", text="Brick-red precipitate. A reducing sugar is present."),
            S("Biuret and emulsion", text="Blue and clear. No protein and no lipid."),
            S("Conclusion", text="Food X contains a reducing sugar (a lot of it) and none of the other nutrients tested."),
        ]),
        EX("Worked example 2: comparing vitamin C", intro="1 cm³ of DCPIP was decolourised by 1 cm³ of orange juice, 2 cm³ of lemon juice and 4 cm³ of apple juice (teaching data). Which juice has the most vitamin C?", steps=[
            S("Think about the rule", text="A smaller volume of juice to decolourise DCPIP means more vitamin C per cm³."),
            S("Compare", text="Orange needs 1 cm³, lemon needs 2 cm³ and apple needs 4 cm³."),
            S("Order", text="Orange has the most, then lemon, then apple. Orange has twice as much as lemon and four times as much as apple, volume for volume."),
        ]),
        MISTAKE("Saying the iodine test gives 'blue'", "The positive colour is blue-black. The starting colour is yellow-brown, not blue. Write both colours."),
        MISTAKE("Skipping the colours in Benedict's test", "Do not write 'blue to red'. Write the full series: blue, green, yellow, orange, brick-red. Name the precipitate too."),
        MISTAKE("Putting the food in water first for the emulsion test", "The food must be shaken with ethanol first. Only then do you pour the clear liquid into water."),
        TIP("In Paper 1 multiple choice, food tests appear in the 'biological situations and experiments' questions. In Paper 2 you may be asked to describe a test or to read a table of results. Always give the reagent, the method and the colour change."),
        QUIZ("A food is tested with iodine solution and the colour changes to blue-black. The food contains:",
             ["Glucose", "Starch", "Protein", "Lipid"], 1, "Iodine solution turns blue-black with starch.",
             hint="Which nutrient is tested by iodine?",
             feedback=["Glucose is tested with Benedict's solution and heat.", "", "Protein is tested with the Biuret test, which turns purple.", "Lipid is tested with ethanol and water (cloudy white)."]),
        QUIZ("Benedict's solution is added to a food solution and heated in a water bath. The solution stays blue. What does this show?",
             ["The food contains starch", "The food contains no reducing sugar", "The food contains protein", "The test was done at too low a temperature"], 1,
             "A reducing sugar would turn the blue solution to green, yellow, orange or brick-red. Blue means none was found.",
             hint="Blue is the starting colour of Benedict's solution.",
             feedback=["Starch is tested with iodine, and starch does not change Benedict's.", "",
                       "Protein is tested with the Biuret test.", "A water bath at about 100 degrees Celsius is hot enough; the stated result is a true negative."]),
        PQ("State the colour change in a positive Biuret test.", "From blue to purple (violet)."),
        PQ("Describe how you would test a food for lipid.", "Crush the food and shake it with ethanol. Let it settle and pour the clear liquid into water. A cloudy white emulsion shows lipid is present."),
        PQ("A food gives blue with Benedict's solution. After boiling with dilute acid, neutralising and heating with Benedict's again it gives brick-red. What does it contain, and why was the acid needed?", "It contains a non-reducing sugar such as sucrose. The acid breaks the sucrose into reducing sugars (glucose and fructose), which then react with Benedict's solution."),
        PQ("Juice P needs 5 drops and juice Q needs 2 drops to decolourise the same amount of DCPIP. Which has more vitamin C?", "Juice Q, because fewer drops are needed to decolourise the DCPIP."),
        SUM("Starch: iodine solution, yellow-brown to blue-black.",
            "Reducing sugar: Benedict's solution and heat, blue to green, yellow, orange, brick-red.",
            "Non-reducing sugar: boil with dilute acid, neutralise, then Benedict's test.",
            "Protein: Biuret test, blue to purple. Lipid: ethanol then water, cloudy white emulsion.",
            "Vitamin C: DCPIP changes from blue to colourless; fewer drops means more vitamin C. Use a control."),
    ],
))

# ------------------------------------------------------------------ 3. Enzymes: properties and lock-and-key
LESSONS.append(lesson(
    module=NUT,
    topic="Enzymes",
    title="Enzymes: properties and the lock-and-key model",
    slug="bib-enzymes-properties-and-lock-and-key",
    minutes=20,
    summary="Enzymes are protein catalysts that speed up reactions in living things. This lesson covers their properties, the active site and the lock-and-key model, and why a heated enzyme stops working (denaturation).",
    objectives=[
        "Define an enzyme, a catalyst, a substrate and the active site",
        "State the properties of enzymes",
        "Explain how an enzyme works using the lock-and-key model",
        "Explain what denaturation is and why heat stops an enzyme working",
    ],
    key_concepts=["Enzyme", "Catalyst", "Substrate", "Product", "Active site", "Lock-and-key model", "Specificity", "Denaturation"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian homes a cook wraps tough meat in pawpaw leaves, or rubs it with a little raw pawpaw, before "
          "cooking. The meat becomes softer. The leaves contain an **enzyme** called papain that breaks down protein in the meat."),
        T("Without enzymes, the chemical reactions in your body would be far too slow to keep you alive. A starch "
          "meal would take weeks to digest instead of hours. Enzymes make these reactions fast at body temperature."),
        D("A **catalyst** is a substance that speeds up a chemical reaction and is not used up in the reaction.", title="Definition: catalyst"),
        D("An **enzyme** is a protein that acts as a biological catalyst. It speeds up a chemical reaction in a living thing without being changed itself.",
          title="Definition: enzyme"),
        H("Substrate, product and active site"),
        T("The substance that an enzyme acts on is the **substrate**. The new substances formed are the **products**. "
          "Each enzyme has a special-shaped hollow on its surface called the **active site**. The substrate fits into the active site."),
        CODE("""enzyme
substrate  ------------------>  products
(starch)       amylase          (maltose)""", "text", title="Naming the parts"),
        KEY("Properties of enzymes", "These are asked often in examinations.", cards=[
            ["They are proteins", "Made by living cells from amino acids."],
            ["They are catalysts", "They speed up reactions and are not used up, so a small amount does a lot of work."],
            ["They are specific", "Each enzyme works on only one kind of substrate (or a few very similar ones)."],
            ["They work best at one temperature", "Each enzyme has an optimum temperature. Too hot and it is destroyed."],
            ["They work best at one pH", "Each enzyme has an optimum pH."],
            ["They can be reversible", "Many enzymes can speed up a reaction in either direction."],
        ]),
        T("Enzyme names usually end in **-ase**. Amylase acts on starch, protease acts on protein, lipase acts on lipids, "
          "maltase acts on maltose, and catalase acts on hydrogen peroxide."),
        H("The lock-and-key model"),
        T("The **lock-and-key model** explains why enzymes are specific. The active site is like a lock. Only a substrate with the "
          "matching shape, the key, can fit."),
        IMG("f5bi-b-lock-and-key.svg", alt="Four stages: substrate approaches the notch (active site) of the enzyme; substrate fits to form the enzyme-substrate complex; products leave and enzyme is unchanged; a denatured enzyme has a different shaped notch that the substrate does not fit",
            caption="Figure 1. The lock-and-key model. In stage 4 the enzyme has been denatured."),
        KEY("How the enzyme works", "Four steps.", cards=[
            ["1", "The substrate collides with the active site."],
            ["2", "The substrate fits into the active site. They form an enzyme-substrate complex."],
            ["3", "The reaction takes place. The substrate is changed into products."],
            ["4", "The products leave. The enzyme is unchanged and can be used again."],
        ]),
        T("Enzymes lower the amount of energy needed to start a reaction. That is why the reaction goes fast at body temperature."),
        H("Denaturation"),
        D("**Denaturation** is a permanent change in the shape of an enzyme (or other protein), caused by high temperature or a very wrong pH. A denatured enzyme's active site no longer fits the substrate, so the enzyme stops working.",
          title="Definition: denaturation"),
        T("Enzymes are not alive, so we do not say heat 'kills' them. We say they are **denatured**. A denatured enzyme cannot "
          "go back to its original shape. An enzyme that is only cold is not denatured; it simply works slowly and works again when warmed."),
        EX("Worked example 1: name the parts", intro="Amylase breaks down starch to maltose. Name the enzyme, the substrate and the product.", steps=[
            S("Enzyme", text="The name ending in -ase: amylase."),
            S("Substrate", text="The substance acted on: starch."),
            S("Product", text="The substance formed: maltose."),
        ]),
        EX("Worked example 2: catalase and a potato", intro="A student puts a small piece of raw potato into hydrogen peroxide. Bubbles of oxygen appear. A piece of boiled potato gives no bubbles. Explain.", steps=[
            S("Raw potato", text="It contains the enzyme catalase. Catalase breaks hydrogen peroxide into water and oxygen, which bubbles."),
            S("Equation", math=r"2\text{H}_2\text{O}_2 \xrightarrow{\text{catalase}} 2\text{H}_2\text{O} + \text{O}_2"),
            S("Boiled potato", text="Boiling denatured the catalase. Its active site changed shape, so it could not fit the hydrogen peroxide and no oxygen was made."),
        ]),
        EX("Worked example 3: why specific?", intro="Why does a protease not digest starch?", steps=[
            S("Shape of the active site", text="The active site of a protease fits protein molecules only."),
            S("Starch", text="Starch has a different shape, so it cannot fit into the protease active site. No complex forms and no reaction occurs."),
        ]),
        MISTAKE("Saying heat kills enzymes", "Enzymes are not living. Say the enzyme is denatured: its shape changes and the active site no longer fits the substrate."),
        MISTAKE("Saying the enzyme is used up", "The enzyme is not changed and not used up. It leaves the reaction unchanged and works again."),
        MISTAKE("Saying cold denatures an enzyme", "Cold only slows the enzyme down. Denaturation is caused by high temperature or extreme pH."),
        TIP("In Paper 1 multiple choice, enzymes appear in diagram and experiment questions (for example the catalase and potato experiment). In Paper 2 essays you may be asked to explain the lock-and-key model, so practise drawing and labelling it."),
        QUIZ("What is the active site of an enzyme?",
             ["The place where the enzyme is made", "A hollow on the enzyme where the substrate fits", "The product of the reaction", "The part that is destroyed by heat only"], 1,
             "The active site is the special-shaped hollow where the substrate binds and the reaction takes place.",
             hint="Think of the lock in the lock-and-key model.",
             feedback=["Enzymes are made in cells, but that is not called the active site.", "", "The product is what is formed; it leaves the active site.", "Heat changes the whole enzyme's shape, including the active site."]),
        QUIZ("Which statement about enzymes is correct?",
             ["They are used up in the reaction", "They are carbohydrates", "They are not changed by the reaction they speed up", "They work on any substrate"], 2,
             "An enzyme is a catalyst: it takes part in the reaction but comes out unchanged.",
             hint="Recall the definition of a catalyst.",
             feedback=["A catalyst is not used up.", "Enzymes are proteins.", "", "Enzymes are specific, so each works on only one kind of substrate."]),
        PQ("Define an enzyme.", "An enzyme is a protein that acts as a biological catalyst, speeding up a chemical reaction in a living thing without being changed itself."),
        PQ("Explain, using the lock-and-key model, why one enzyme can digest only one kind of food.", "The active site has a particular shape. Only the substrate with a matching shape fits into it to form an enzyme-substrate complex. Other molecules have different shapes and do not fit."),
        PQ("What is denaturation?", "A permanent change in the shape of an enzyme caused by high temperature or a wrong pH, so the active site no longer fits the substrate."),
        PQ("A student boils a sample of amylase for five minutes and then adds it to starch. No digestion occurs. Explain.", "Boiling denatured the amylase. The active site changed shape and could no longer fit the starch, so the enzyme could not catalyse its breakdown."),
        SUM("An enzyme is a protein that acts as a biological catalyst; it speeds up reactions and is not used up.",
            "Enzymes are specific, and work best at an optimum temperature and an optimum pH.",
            "In the lock-and-key model the substrate fits the active site, forms an enzyme-substrate complex, and the products leave.",
            "High temperature or a wrong pH denatures an enzyme: its shape changes permanently and it stops working.",
            "Cold slows an enzyme but does not denature it."),
    ],
))

# ------------------------------------------------------------------ 4. Factors affecting enzyme activity
LESSONS.append(lesson(
    module=NUT,
    topic="Enzymes",
    title="Factors that affect enzyme activity: temperature, pH and concentration",
    slug="bib-factors-affecting-enzyme-activity",
    minutes=24,
    summary="How temperature, pH, substrate concentration and enzyme concentration change the rate of an enzyme-controlled reaction, how to read the graphs, and how to plan a simple amylase experiment.",
    objectives=[
        "Describe and explain the effect of temperature on enzyme activity, including the optimum and denaturation",
        "Describe and explain the effect of pH, giving examples of different optimum values",
        "Explain the effect of substrate and enzyme concentration on the rate of reaction",
        "Read and interpret graphs of enzyme activity and calculate rates",
    ],
    key_concepts=["Rate of reaction", "Optimum temperature", "Optimum pH", "Denaturation", "Substrate concentration", "Enzyme concentration", "Limiting factor"],
    blocks=[
        H("Introduction"),
        T("On a hot day, milk goes sour in a few hours. In a refrigerator it stays fresh for days. The souring is caused by "
          "bacteria whose enzymes work faster when it is warm. The same idea explains how the enzymes in your body behave."),
        T("The **rate of reaction** is how fast the substrate is used up or how fast the product is formed. In this lesson you "
          "will learn four things that change that rate and how to read the graphs."),
        D("The **rate of an enzyme reaction** is the amount of substrate changed, or product made, in a given time. It can be found from 1 divided by the time taken for the reaction to finish.",
          title="Definition: rate"),
        H("Temperature"),
        T("Study Figure 1. The numbers come from a simple teaching data set for a human enzyme."),
        IMG("f5bi-b-enzyme-temperature.svg", alt="Graph of rate of reaction against temperature: rate rises from 0 at 0 degrees to a peak of 16 at 37 degrees, then drops quickly to 2 at 50 degrees and 0 at 60 degrees",
            caption="Figure 1. Effect of temperature on the rate of an enzyme reaction (teaching data)."),
        KEY("Reading the temperature graph", "Three parts.", cards=[
            ["Below the optimum", "As the temperature rises the molecules move faster and collide more often, so the rate rises. At low temperatures it roughly doubles for each 10 degrees Celsius rise."],
            ["At the optimum", "The rate is highest. For human enzymes this is about 37 degrees Celsius."],
            ["Above the optimum", "The enzyme begins to lose its shape. By about 50 to 60 degrees Celsius it is denatured and the rate falls to zero."],
        ]),
        D("The **optimum temperature** is the temperature at which an enzyme works fastest.", title="Definition: optimum temperature"),
        T("The graph rises slowly but falls sharply. This is because a heated enzyme loses its shape and does not come back. "
          "A cooled enzyme can work again, but a denatured one cannot."),
        H("pH"),
        T("**pH** measures how acidic or alkaline a liquid is. pH 7 is neutral, below 7 is acid, above 7 is alkaline. "
          "Each enzyme has an **optimum pH** and the rate falls on either side of it."),
        IMG("f5bi-b-enzyme-ph.svg", alt="Two bell-shaped curves: pepsin has its peak at about pH 2 and amylase has its peak at about pH 7 to 8",
            caption="Figure 2. Effect of pH on the rate of two enzymes (teaching data)."),
        T("Pepsin works in the very acid stomach (optimum about pH 2). Amylase in the mouth works best near neutral pH. "
          "Trypsin, in the small intestine, works best in slightly alkaline conditions (about pH 8). A wrong pH changes "
          "the shape of the active site, so the substrate no longer fits. Pepsin put into an alkaline solution is denatured."),
        H("Substrate concentration"),
        T("If the amount of enzyme is fixed, adding more substrate raises the rate at first. More substrate molecules find an "
          "active site. But after a certain point all the active sites are busy and the rate stops rising. The curve levels off."),
        CODE("""Substrate concentration (units)   0    1    2    3    4    5    6
Rate of reaction (units)         0    5    9   12   14   14.5 14.5""", "text", title="Teaching data: substrate concentration"),
        H("Enzyme concentration"),
        T("If there is plenty of substrate, doubling the enzyme doubles the rate, because there are twice as many active sites. "
          "If the substrate runs short, the rate stops rising. Enzyme concentration and substrate concentration act as "
          "**limiting factors**: whichever is in short supply limits the rate."),
        H("An experiment with amylase"),
        T("Mix amylase with starch in a water bath. Every 30 seconds take a drop and test it with iodine solution on a white tile. "
          "At first it turns blue-black. When the colour stays yellow-brown, all the starch has been digested. Repeat at "
          "different temperatures, keeping the other factors the same. A shorter time means a faster rate."),
        EX("Worked example 1: calculate the rate", intro="Starch disappeared in 240 s at 20 degrees Celsius, 100 s at 30 degrees Celsius and 60 s at 37 degrees Celsius. Calculate the rate in each case as 1000 divided by the time.", steps=[
            S("20 degrees Celsius", math=r"\dfrac{1000}{240} = 4.2"),
            S("30 degrees Celsius", math=r"\dfrac{1000}{100} = 10.0"),
            S("37 degrees Celsius", math=r"\dfrac{1000}{60} = 16.7"),
            S("Conclusion", text="The rate rises as the temperature rises towards 37 degrees Celsius. The faster rate matches the shorter time."),
        ]),
        EX("Worked example 2: read the temperature graph", intro="Use Figure 1. By what percentage does the rate increase between 30 degrees Celsius and 37 degrees Celsius?", steps=[
            S("Read the graph", text="At 30 degrees Celsius the rate is 13 units. At 37 degrees Celsius it is 16 units."),
            S("Change", math=r"16 - 13 = 3 \text{ units}"),
            S("Percentage of the first value", math=r"\dfrac{3}{13} \times 100 = 23\%"),
        ]),
        EX("Worked example 3: explain a plateau", intro="In the substrate table the rate stays at 14.5 units for concentrations 5 and 6. Explain.", steps=[
            S("What has changed", text="More substrate was added but the rate did not rise."),
            S("Reason", text="All the active sites of the enzyme are occupied at one time."),
            S("Limiting factor", text="Enzyme concentration now limits the rate, not substrate. Adding more enzyme would raise the rate."),
        ]),
        MISTAKE("Explaining the fall above the optimum as 'the enzyme moves slower'", "Above the optimum the enzyme is denatured. Its active site changes shape. Slower movement is the explanation for low temperatures only."),
        MISTAKE("Drawing a pH curve that does not start and end near zero", "At very low and very high pH most enzymes are denatured and the rate is near zero. A bell-shaped curve with one peak is expected."),
        MISTAKE("Joining graph points with a ruler", "Enzyme graphs are smooth curves. Draw a smooth curve through the plotted points."),
        TIP("The Board's report says candidates struggle to plot and interpret graphs. Label the axes with units, choose an even scale, plot points exactly, and join with a smooth curve. Graph questions appear in the Paper 1 section on experiments and in Paper 2."),
        QUIZ("At which temperature is the human enzyme in Figure 1 working fastest?",
             ["20 degrees Celsius", "37 degrees Celsius", "50 degrees Celsius", "60 degrees Celsius"], 1,
             "The peak of the curve is at about 37 degrees Celsius, the optimum temperature.",
             hint="Find the highest point on the curve.",
             feedback=["At 20 degrees Celsius the rate is still rising.", "", "At 50 degrees Celsius the enzyme is already being denatured.", "At 60 degrees Celsius the rate is zero because the enzyme is denatured."]),
        QUIZ("Why does the rate stop rising when more substrate is added to a fixed amount of enzyme?",
             ["The enzyme is denatured", "The substrate is used up", "All the active sites are occupied", "The temperature falls"], 2,
             "When every active site is busy, extra substrate cannot be changed any faster.",
             hint="Think about how many active sites there are.",
             feedback=["Denaturation is caused by heat or pH, not by more substrate.", "More substrate was added, so there is more of it, not less.", "", "Nothing in the question changes the temperature."]),
        PQ("State the optimum pH of pepsin and explain why this suits its job.", "About pH 2. Pepsin works in the stomach, which contains hydrochloric acid, so its enzyme works best in acid conditions."),
        PQ("Explain why the rate of an enzyme reaction falls to zero at 60 degrees Celsius.", "The high temperature denatures the enzyme. The shape of the active site changes so the substrate no longer fits."),
        PQ("An enzyme digests starch in 80 s at 30 degrees Celsius. Calculate the rate as 1000 divided by the time.", "1000 ÷ 80 = 12.5 (units per 1000 s)."),
        PQ("Describe how you would find the effect of pH on amylase.", "Mix equal volumes of starch and amylase with buffer solutions of different pH in a water bath at 37 degrees Celsius. Test drops with iodine at regular times and record how long it takes for the blue-black colour to disappear. Keep temperature, volumes and concentrations the same."),
        SUM("Rate of reaction rises with temperature up to the optimum (about 37 degrees Celsius for human enzymes) and then falls steeply as the enzyme is denatured.",
            "Each enzyme has its own optimum pH: pepsin about 2, amylase near neutral, trypsin slightly alkaline.",
            "More substrate increases the rate until all active sites are in use, then the curve levels off.",
            "More enzyme increases the rate while there is enough substrate.",
            "Draw graphs with labelled axes and units and a smooth curve."),
    ],
))

# ------------------------------------------------------------------ 5. Photosynthesis and the leaf
LESSONS.append(lesson(
    module=NUT,
    topic="Photosynthesis and plant nutrition",
    title="Photosynthesis and the structure of a leaf",
    slug="bib-photosynthesis-and-leaf-structure",
    minutes=25,
    summary="Green plants make glucose from carbon dioxide and water using light energy trapped by chlorophyll. This lesson covers the equation, the two stages, the fate of glucose, how the leaf is adapted, and the starch test on a leaf.",
    objectives=[
        "Define photosynthesis and write its word and balanced symbol equation",
        "Outline the light stage and the carbon-fixing stage in the chloroplast",
        "Describe how the layers of a leaf are adapted for photosynthesis",
        "Describe the starch test on a leaf and what it shows",
    ],
    key_concepts=["Photosynthesis", "Chlorophyll", "Chloroplast", "Autotroph", "Palisade mesophyll", "Stoma", "Starch test on a leaf"],
    blocks=[
        H("Introduction"),
        T("A maize plant on a farm in the Grassfields has no mouth and no market. Yet it grows taller every week and "
          "makes cobs full of food. It makes all its own food from air, water and sunlight. This process is called **photosynthesis**."),
        T("Almost all food on Earth starts with photosynthesis. When you eat cassava, plantain or meat, you are using energy that a plant first trapped from sunlight."),
        D("**Photosynthesis** is the process by which green plants make glucose from carbon dioxide and water, using light energy absorbed by chlorophyll, and release oxygen.",
          title="Definition: photosynthesis"),
        D("**Chlorophyll** is the green pigment in chloroplasts that absorbs light energy. A **chloroplast** is the organelle in plant cells where photosynthesis happens. An **autotroph** is an organism that makes its own food.",
          title="Definition: chlorophyll, chloroplast, autotroph"),
        H("The equation"),
        CODE("""Word equation:
carbon dioxide + water  --(light, chlorophyll)-->  glucose + oxygen

Symbol equation:
6CO2 + 6H2O  --(light, chlorophyll)-->  C6H12O6 + 6O2""", "text", title="Photosynthesis"),
        T("Check that the equation balances. On the left there are 6 carbon atoms, 12 hydrogen atoms and 18 oxygen atoms. "
          "On the right, glucose has 6 carbon, 12 hydrogen and 6 oxygen, and six oxygen molecules have 12 oxygen atoms: 6 + 12 = 18. It balances."),
        KEY("What the plant needs and makes", "Four needs, two products.", cards=[
            ["Light", "Gives the energy. The reaction does not go in the dark."],
            ["Chlorophyll", "Absorbs the light energy."],
            ["Carbon dioxide", "Enters the leaf from the air through the stomata."],
            ["Water", "Taken up by the roots and carried to the leaf in xylem."],
            ["Glucose", "The food made, used for energy and building."],
            ["Oxygen", "A by-product released through the stomata."],
        ]),
        H("How it happens in two stages"),
        T("Photosynthesis takes place inside chloroplasts in two stages."),
        KEY("The two stages", "Light needed for the first; chemical reactions in the second.", cards=[
            ["1. Light stage (in the grana)", "Chlorophyll absorbs light. The energy splits water into hydrogen and oxygen. The oxygen is released. Some energy is stored in ATP."],
            ["2. Carbon-fixing stage (in the stroma)", "Carbon dioxide is combined with the hydrogen, using the energy stored in ATP, to make glucose."],
        ]),
        T("You need only this outline for O Level. The important facts are that water is split in the light stage and that oxygen comes from the water."),
        H("What happens to the glucose"),
        T("The plant uses the glucose in several ways. Some is used at once in **respiration** to release energy. Some is turned into "
          "**starch** and stored in leaves, roots and seeds. Some is changed to **sucrose** and carried in the phloem to other parts. "
          "Some is made into **cellulose** for cell walls. With nitrates from the soil, some is turned into amino acids and proteins. "
          "Some is made into oils and fats, for example in groundnuts and palm fruits."),
        H("The structure of a leaf"),
        IMG("f5bi-b-leaf-section.svg", alt="Section through a leaf showing cuticle, upper epidermis, palisade mesophyll with chloroplasts, spongy mesophyll with air spaces, xylem and phloem in a vein, a stoma with two guard cells, and the lower epidermis",
            caption="Figure 1. A section through a leaf."),
        CODE("""Layer                  Adaptation for photosynthesis
Cuticle                Waxy layer; reduces water loss; transparent
Upper epidermis        One cell thick and transparent; lets light through
Palisade mesophyll     Tall cells packed with chloroplasts; most photosynthesis
Spongy mesophyll       Loosely packed with air spaces; carbon dioxide diffuses in
Vein (xylem, phloem)   Xylem brings water; phloem carries sugars away
Lower epidermis        Has stomata; gas exchange
Stoma and guard cells  Open and close; let CO2 in and O2 out""", "text", title="Layers of the leaf"),
        T("The whole leaf is **broad, flat and thin**. A broad flat leaf catches much light. A thin leaf lets light reach all the cells and "
          "keeps the diffusion distance for gases short. Most leaves have more stomata on the lower surface, which is "
          "shaded and cooler, so less water is lost."),
        H("Testing a leaf for starch"),
        T("Starch is the stored product of photosynthesis, so a leaf that contains starch has been photosynthesising."),
        CODE("""1. Destarch the plant: keep it in the dark for 24 to 48 hours.
2. Put it in the light, with one leaf partly covered or part-white (variegated).
3. Pick the leaf. Dip it in boiling water for about 1 minute.
   This kills the cells and softens the leaf.
4. Turn off the flame. Warm the leaf in hot ethanol in a water bath.
   This removes the chlorophyll. Never heat ethanol directly in a flame.
5. Rinse the leaf in warm water to soften it.
6. Spread it on a white tile and add iodine solution.""", "text", title="Starch test on a leaf"),
        T("Blue-black shows starch. If the leaf had a black paper strip, the covered part stays yellow-brown: light is needed. "
          "If the leaf was variegated, only the green parts turn blue-black: chlorophyll is needed."),
        EX("Worked example 1: variegated leaf", intro="A variegated leaf has green and white parts. After 6 hours in sunlight it is tested for starch. Describe and explain the result.", steps=[
            S("Result", text="The green parts turn blue-black. The white parts stay yellow-brown."),
            S("Meaning", text="Starch was made only where there was chlorophyll."),
            S("Conclusion", text="Chlorophyll is needed for photosynthesis."),
        ]),
        EX("Worked example 2: explain a leaf feature", intro="Explain why the palisade cells are found just below the upper epidermis and contain many chloroplasts.", steps=[
            S("Position", text="Light enters through the transparent upper epidermis. Cells just below it receive the most light."),
            S("Chloroplasts", text="Many chloroplasts hold much chlorophyll, so much light energy is trapped."),
            S("Shape", text="The cells are tall and packed together, so many chloroplasts fit near the surface."),
        ]),
        MISTAKE("Saying plants give out oxygen and take in carbon dioxide only", "In the light, photosynthesis takes in CO2 and gives out O2. But the plant also respires all the time. Do not say plants 'do not respire'."),
        MISTAKE("Heating ethanol directly over a flame", "Ethanol is flammable. Always use a hot water bath after turning the flame off."),
        MISTAKE("Writing the oxygen as coming from carbon dioxide", "The oxygen released comes from the splitting of water in the light stage."),
        TIP("Photosynthesis is among the most examined topics. In Paper 1 expect leaf diagrams (labelling the layers) and experiment questions on the starch test. In Paper 2 you may be asked to state the equation, describe the stages, or explain leaf adaptations; draw clear, labelled diagrams and spell chlorophyll correctly."),
        QUIZ("Which layer of the leaf contains the most chloroplasts?",
             ["Upper epidermis", "Palisade mesophyll", "Spongy mesophyll", "Lower epidermis"], 1,
             "The tall palisade cells are packed with chloroplasts and lie just below the upper epidermis where most light arrives.",
             hint="Which layer is directly under the transparent cells at the top?",
             feedback=["The upper epidermis is transparent and mostly has no chloroplasts.", "", "Spongy mesophyll has fewer chloroplasts and many air spaces.", "The lower epidermis has stomata and guard cells; it has no true photosynthetic layer."]),
        QUIZ("In the starch test, why is the leaf placed in hot ethanol?",
             ["To kill the leaf", "To remove chlorophyll so the iodine colour can be seen", "To make starch", "To remove carbon dioxide"], 1,
             "Chlorophyll would hide the blue-black colour. Ethanol removes it and leaves a pale leaf.",
             hint="What colour is the leaf at the start?",
             feedback=["Boiling water kills the cells. Ethanol has a different job.", "", "Starch is made earlier, in the light.", "The test is not about carbon dioxide."]),
        PQ("Write the balanced symbol equation for photosynthesis.", "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ (in the presence of light and chlorophyll)."),
        PQ("State two ways in which a leaf is adapted for photosynthesis.", "Any two: broad and flat, so it catches much light; thin, so gases diffuse quickly and light reaches all cells; palisade cells packed with chloroplasts; transparent epidermis; stomata for gas exchange; air spaces in spongy mesophyll; veins bring water."),
        PQ("Why must a plant be destarched before an experiment on starch?", "To remove starch already in the leaf. Then any starch found afterwards must have been made during the experiment."),
        PQ("Name two substances that the plant makes from the glucose formed in photosynthesis.", "Any two: starch, sucrose, cellulose, proteins (with nitrates), oils and fats."),
        SUM("Photosynthesis makes glucose and oxygen from carbon dioxide and water using light absorbed by chlorophyll: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.",
            "The light stage splits water and releases oxygen; the second stage uses hydrogen and carbon dioxide to make glucose.",
            "Glucose is used in respiration or turned into starch, sucrose, cellulose, proteins and oils.",
            "The leaf is broad, flat and thin. Palisade cells hold most chloroplasts; spongy cells have air spaces; stomata allow gas exchange.",
            "Starch test: destarch, boil, ethanol, rinse, iodine; blue-black means starch."),
    ],
))

# ------------------------------------------------------------------ 6. Limiting factors and mineral requirements
LESSONS.append(lesson(
    module=NUT,
    topic="Photosynthesis and plant nutrition",
    title="Limiting factors in photosynthesis and mineral requirements of plants",
    slug="bib-limiting-factors-and-plant-minerals",
    minutes=24,
    summary="What a limiting factor is, how light, carbon dioxide and temperature limit the rate of photosynthesis, how to read the graphs, and why plants need nitrogen, phosphorus, potassium and magnesium.",
    objectives=[
        "Define a limiting factor and name the factors that limit photosynthesis",
        "Read and explain a graph of photosynthesis rate against light intensity",
        "State why a plant needs nitrate, phosphate, potassium and magnesium",
        "Recognise the symptoms of mineral deficiency in plants",
    ],
    key_concepts=["Limiting factor", "Light intensity", "Carbon dioxide concentration", "Temperature", "Mineral deficiency", "Nitrate", "Phosphate", "Magnesium", "Fertiliser"],
    blocks=[
        H("Introduction"),
        T("A tomato farmer near Foumbot wants bigger harvests. He can give the plants more water, more fertiliser or more "
          "sunlight by cutting nearby shade. But which one helps most? If the plant already has plenty of water, more water "
          "will do nothing. The answer is to find the **limiting factor**."),
        D("A **limiting factor** is the factor in shortest supply, which controls the rate of a process even when the other factors are plentiful.",
          title="Definition: limiting factor"),
        T("The main factors that can limit photosynthesis are **light intensity**, **carbon dioxide concentration** and **temperature**. "
          "Water and chlorophyll can also limit it, but we usually assume they are plentiful."),
        H("Light intensity"),
        T("At low light, photosynthesis is slow because the plant does not have enough energy. Raising the light raises the rate. "
          "Look at Figure 1. The teaching data show two experiments at the same temperature."),
        IMG("f5bi-b-light-rate.svg", alt="Graph of rate of photosynthesis against light intensity. At 0.03 percent carbon dioxide the rate rises to 20 units by light intensity 4 and then levels off. At 0.1 percent carbon dioxide the rate rises further to 36 units by light intensity 6 and then levels off",
            caption="Figure 1. Photosynthesis rate against light intensity at two carbon dioxide concentrations (teaching data)."),
        KEY("How to read the graph", "Three steps.", cards=[
            ["The rising part", "The rate goes up as light goes up. Light is the limiting factor here, and both curves are almost the same."],
            ["The flat part", "Raising the light makes no difference. Some other factor is now limiting, here carbon dioxide."],
            ["The higher curve", "More carbon dioxide gives a higher plateau. This proves carbon dioxide was the limiting factor on the lower curve."],
        ]),
        H("Carbon dioxide and temperature"),
        T("Air has only about 0.03 to 0.04 percent carbon dioxide, so carbon dioxide often limits photosynthesis. "
          "Greenhouse growers sometimes add extra carbon dioxide to raise the rate."),
        T("**Temperature** controls the enzymes of the carbon-fixing stage. As temperature rises the rate rises, until about 35 to 40 degrees Celsius. "
          "Above this, the enzymes are denatured and the rate falls. The temperature curve is similar to the enzyme curve in the last lesson."),
        H("Mineral requirements of plants"),
        T("Plants make carbohydrates from carbon dioxide and water, but they also need **mineral ions** from the soil. They take "
          "them in through the root hairs, dissolved in water."),
        CODE("""Mineral (ion)       Used for                         Deficiency symptoms
Nitrogen (nitrate)  Amino acids, proteins, chlorophyll  Stunted growth; older leaves pale yellow
Phosphorus          DNA, ATP, cell membranes; roots     Poor root growth; small, dull or purplish leaves
(phosphate)
Potassium           Enzyme action; flowers and fruits   Yellow leaf edges and dead spots
Magnesium           Part of chlorophyll                 Yellow leaves with green veins""", "text", title="Minerals needed by plants"),
        T("Symptoms are described slightly differently in different books, so check your textbook for the exact words your teacher expects."),
        T("Farmers add these minerals as **fertilisers**. Manure and compost release minerals slowly as they rot. Artificial "
          "NPK fertiliser contains nitrogen, phosphorus and potassium and acts quickly. Too much fertiliser washes into "
          "streams and can pollute them."),
        H("Showing that a mineral is needed"),
        T("Grow seedlings in water with dissolved minerals (a **water culture**, no soil). Set up one tube with all the minerals "
          "and other tubes each missing one mineral, such as magnesium. After some weeks, the plant with no magnesium has yellow leaves. "
          "The tube with all minerals is the control."),
        EX("Worked example 1: reading the graph", intro="Use Figure 1. At light intensity 4, how much higher is the rate at 0.1 percent carbon dioxide than at 0.03 percent? Give the answer as a percentage of the lower rate.", steps=[
            S("Read the two values", text="At light intensity 4, the rates are 20 units (0.03%) and 30 units (0.1%)."),
            S("Difference", math=r"30 - 20 = 10"),
            S("Percentage of the lower rate", math=r"\dfrac{10}{20} \times 100 = 50\%"),
        ]),
        EX("Worked example 2: what limits the rate?", intro="At light intensity 7 and 0.03 percent carbon dioxide, the rate is 20 units. What is the limiting factor, and how would you raise the rate?", steps=[
            S("Look at the curve", text="At 0.03 percent, the curve is flat between 4 and 8. More light makes no difference."),
            S("Name the limiting factor", text="Light is not limiting. Carbon dioxide is, because raising it to 0.1 percent gives a higher rate."),
            S("Answer", text="Increase the carbon dioxide concentration."),
        ]),
        EX("Worked example 3: diagnose a deficiency", intro="A maize farmer sees that the leaves of her plants are yellow between the veins but the veins stay green. Which mineral may be missing?", steps=[
            S("Think about chlorophyll", text="Yellow leaves mean less chlorophyll."),
            S("Which mineral is in chlorophyll", text="Magnesium is part of chlorophyll."),
            S("Conclusion", text="Probably magnesium deficiency. A soil test would confirm it."),
        ]),
        MISTAKE("Saying 'light is the limiting factor' when the graph is flat", "On the flat part of a light graph, light is NOT limiting. Look for another factor such as carbon dioxide or temperature."),
        MISTAKE("Confusing nitrate with nitrogen gas", "Plants cannot use nitrogen gas from the air. They take in nitrates (nitrate ions) from the soil."),
        MISTAKE("Writing that minerals give energy to plants", "Minerals are building materials and help enzymes work. They do not give energy."),
        TIP("Limiting factor graphs appear often in Paper 1 questions on 'biological situations and experiments' and in Paper 2 data questions. State which factor is limiting and give a reason from the graph."),
        QUIZ("On the flat part of a graph of photosynthesis against light intensity, which statement is correct?",
             ["Light is limiting the rate", "A factor other than light is limiting the rate", "The plant has stopped photosynthesising", "The chlorophyll has been destroyed"], 1,
             "The flat part shows that more light no longer raises the rate, so something else (for example CO2 or temperature) is limiting.",
             hint="What happens when you add more light but nothing changes?",
             feedback=["If light were limiting, more light would raise the rate.", "", "The rate is constant and not zero, so photosynthesis continues.", "Nothing in the graph suggests the chlorophyll is destroyed."]),
        QUIZ("Which mineral is needed to make chlorophyll?",
             ["Potassium", "Phosphate", "Magnesium", "Calcium"], 2,
             "Magnesium is at the centre of the chlorophyll molecule.",
             hint="A lack of this mineral turns leaves yellow between the veins.",
             feedback=["Potassium helps enzymes and flowers and fruits.", "Phosphate is used in DNA, ATP and membranes.", "", "Calcium is not part of chlorophyll."]),
        PQ("Define a limiting factor.", "A factor in short supply that controls the rate of a process even though other factors are plentiful."),
        PQ("Name two factors that can limit the rate of photosynthesis.", "Any two: light intensity, carbon dioxide concentration, temperature (also water and chlorophyll)."),
        PQ("Explain why a plant lacking nitrate grows poorly.", "Nitrate is needed to make amino acids and proteins and chlorophyll. Without it the plant cannot build new cells, so growth is stunted and the leaves are pale yellow."),
        PQ("Describe an experiment to show that a plant needs magnesium.", "Grow seedlings in water culture: one tube with all minerals (control) and one with all minerals except magnesium, in the same light and temperature. After some weeks the seedling without magnesium has yellow leaves, the control stays green."),
        SUM("A limiting factor is the factor in shortest supply that controls the rate of a process.",
            "Light, carbon dioxide and temperature can limit the rate of photosynthesis. On a flat graph line another factor is limiting.",
            "Plants take nitrate, phosphate, potassium and magnesium ions from the soil through root hairs.",
            "Nitrogen makes proteins; phosphorus makes DNA, ATP and membranes; potassium helps enzymes and fruits; magnesium makes chlorophyll.",
            "Fertilisers replace minerals that crops remove from the soil."),
    ],
))

# ------------------------------------------------------------------ 7. Teeth and the alimentary canal
LESSONS.append(lesson(
    module=NUT,
    topic="Nutrition in mammals",
    title="Holozoic nutrition: teeth and the alimentary canal",
    slug="bib-mammal-teeth-and-alimentary-canal",
    minutes=24,
    summary="The five stages of holozoic nutrition, the four types of teeth and their jobs, the structure of a tooth and tooth decay, dental formulae of herbivores and carnivores, and the parts of the alimentary canal.",
    objectives=[
        "Define holozoic nutrition and name its five stages",
        "Name the four types of mammal teeth, state their functions and work out a dental formula",
        "Describe the structure of a tooth and the cause of tooth decay",
        "Name the parts of the alimentary canal and state the function of each",
    ],
    key_concepts=["Holozoic nutrition", "Incisor", "Canine", "Premolar", "Molar", "Dental formula", "Enamel", "Alimentary canal", "Peristalsis"],
    blocks=[
        H("Introduction"),
        T("Look at a goat tied outside a house and at a dog resting beside it. The goat spends the day chewing grass with flat "
          "teeth. The dog tears meat with sharp teeth. Both are mammals, and both feed in the same way: they take in "
          "solid food, break it down and use it. This is called **holozoic nutrition**."),
        D("**Holozoic nutrition** is feeding on solid food that is taken into the body and then digested, absorbed and used. Mammals feed holozoically.",
          title="Definition: holozoic nutrition"),
        KEY("Five stages of holozoic nutrition", "Learn them in order.", cards=[
            ["Ingestion", "Taking food into the mouth."],
            ["Digestion", "Breaking large insoluble food molecules into small soluble ones."],
            ["Absorption", "Taking the small molecules from the gut into the blood."],
            ["Assimilation", "Using the absorbed molecules in the body cells."],
            ["Egestion", "Removing undigested food (faeces) through the anus."],
        ]),
        H("Teeth and their jobs"),
        T("Mammals have teeth of **different types** (heterodont). Teeth start the process of digestion by physically "
          "breaking food into small pieces. This gives the enzymes a larger surface to act on."),
        KEY("Four types of tooth", "Each has a shape that suits its job.", cards=[
            ["Incisors", "Chisel-shaped, at the front. Cut and bite food."],
            ["Canines", "Pointed. Pierce and tear food. Large in meat eaters."],
            ["Premolars", "Broad with ridges. Crush and grind food."],
            ["Molars", "Broad with cusps. Grind food. The biggest at the back."],
        ]),
        H("The dental formula"),
        T("The **dental formula** shows the teeth in half of the upper jaw above the teeth in half of the lower jaw. Use "
          "i for incisors, c for canines, pm for premolars and m for molars. Multiply the sum by 2 to get the total in the mouth."),
        CODE("""Human (adult):  i 2/2   c 1/1   pm 2/2   m 3/3
Goat (herbivore): i 0/3   c 0/1   pm 3/3   m 3/3
Dog (carnivore): i 3/3   c 1/1   pm 4/4   m 2/3""", "text", title="Dental formulae (check your textbook for small differences)"),
        EX("Worked example 1: total number of teeth", intro="An adult human has i 2/2, c 1/1, pm 2/2, m 3/3. How many teeth in total?", steps=[
            S("Add the upper and lower teeth in one half of the mouth", math=r"2 + 2 + 1 + 1 + 2 + 2 + 3 + 3 = 16"),
            S("Multiply by 2 for both halves", math=r"16 \times 2 = 32"),
            S("Answer", text="An adult human has 32 teeth."),
        ]),
        H("Herbivores and carnivores"),
        CODE("""Feature        Herbivore (goat, cow)             Carnivore (dog, lion)
Incisors       Sharp lower incisors cut against   Small, for gripping and scraping
               a hard upper pad
Canines        Small or absent                    Large and pointed; stab and tear
Premolars and  Broad, flat, ridged; grind          Carnassial teeth: sharp, slice flesh
molars         tough plant material               like scissors
Jaw movement   Side to side (grinding)            Up and down (cutting)""", "text", title="Comparing dentition"),
        T("Plant material has cellulose cell walls and takes grinding. Meat is easier to break down and needs piercing and slicing."),
        H("Structure of a tooth"),
        KEY("Parts of a tooth", "Think from outside to inside.", cards=[
            ["Enamel", "The hardest substance in the body. Covers the crown and protects the tooth."],
            ["Dentine", "Bone-like material under the enamel. Less hard, with tiny channels."],
            ["Pulp cavity", "The soft centre with blood vessels (food and oxygen) and nerves (feeling)."],
            ["Cement and root", "The root is fixed in the jawbone by cement. The gum covers the neck."],
        ]),
        H("Tooth decay"),
        T("Bacteria in the mouth form a sticky layer called plaque on the teeth. They feed on sugar and produce **acid**. The acid dissolves "
          "the enamel and makes a hole (cavity). If it reaches the pulp, it causes toothache. To prevent decay, brush after meals, eat less sugary food, "
          "use fluoride toothpaste and visit a dentist regularly."),
        H("The alimentary canal"),
        D("The **alimentary canal** (gut) is the long tube from the mouth to the anus through which food passes and is digested and absorbed.",
          title="Definition: alimentary canal"),
        IMG("f5bi-b-alimentary-canal.svg", alt="Simple diagram of the human gut: mouth, salivary gland, oesophagus, liver, gall bladder, stomach, pancreas, small intestine, large intestine and anus",
            caption="Figure 1. The alimentary canal and its glands (simplified, not to scale)."),
        CODE("""Part               What happens there
Mouth              Chewing; saliva moistens food; salivary amylase starts starch digestion
Oesophagus         Moves food to the stomach by peristalsis
Stomach            Churns food; hydrochloric acid kills bacteria; pepsin digests protein
Small intestine    Duodenum: digestion with bile and pancreatic juice.
                   Ileum: final digestion and absorption of digested food
Large intestine    Absorbs water; forms faeces
Rectum and anus    Rectum stores faeces; the anus egests them""", "text", title="Parts of the canal"),
        D("**Peristalsis** is the wave-like contraction of the muscles in the wall of the gut that pushes food along.", title="Definition: peristalsis"),
        T("The salivary glands, liver, gall bladder and pancreas are not part of the canal. Food does not pass through them, "
          "but they make juices that flow into the canal."),
        EX("Worked example 2: follow a mouthful", intro="Follow a mouthful of boiled yam through the gut and say what happens at each stage.", steps=[
            S("Mouth", text="Incisors and molars break the yam. Saliva makes it soft. Amylase begins to digest starch."),
            S("Oesophagus", text="Peristalsis pushes the ball of food (bolus) down."),
            S("Stomach", text="The stomach churns it. Acid and pepsin act mainly on protein; starch digestion goes on little."),
            S("Small intestine", text="Starch digestion is completed. Glucose is absorbed in the ileum."),
            S("Large intestine", text="Water is absorbed. Fibre remains and forms faeces, which leave through the anus."),
        ]),
        MISTAKE("Calling the liver or pancreas part of the alimentary canal", "Food never enters them. They are associated organs that secrete juices into the canal."),
        MISTAKE("Mixing up egestion and excretion", "Egestion is removal of undigested food that has never entered cells. Excretion is removal of waste made by cells (such as urea and carbon dioxide)."),
        MISTAKE("Saying digestion happens in the large intestine", "Digestion and absorption of nutrients is mostly in the small intestine. The large intestine absorbs water."),
        TIP("In Paper 1 multiple choice, expect labelled diagrams of the gut or a tooth and questions on dental formulae. In Paper 2 essays you may be asked to describe the functions of the parts of the canal. Practise labelling and spell oesophagus, duodenum and ileum."),
        QUIZ("Which type of tooth is large and pointed in carnivores for tearing meat?",
             ["Incisor", "Canine", "Premolar", "Molar"], 1,
             "Canines are pointed teeth that pierce and tear flesh.",
             hint="Think about the long pointed teeth of a dog.",
             feedback=["Incisors are chisel-shaped for cutting.", "", "Premolars crush and grind.", "Molars grind food."]),
        QUIZ("Where is most of the water from digested food absorbed back into the body?",
             ["Stomach", "Large intestine", "Mouth", "Oesophagus"], 1,
             "Some water is absorbed in the small intestine, but the large intestine absorbs most of the remaining water. This makes the faeces more solid.",
             hint="Which part is next to the rectum?",
             feedback=["The stomach absorbs very little water.", "", "Nothing is absorbed from food in the mouth.", "The oesophagus only moves food."]),
        PQ("Name the five stages of holozoic nutrition in order.", "Ingestion, digestion, absorption, assimilation, egestion."),
        PQ("State the functions of the incisors and the molars.", "Incisors cut and bite food. Molars grind food into small pieces."),
        PQ("Explain how sugar in the diet causes tooth decay.", "Bacteria in plaque feed on sugar and make acid. The acid dissolves the enamel and then the dentine, making a cavity."),
        PQ("A dog has i 3/3, c 1/1, pm 4/4, m 2/3. Calculate the total number of teeth.", "3 + 3 + 1 + 1 + 4 + 4 + 2 + 3 = 21. Total = 21 × 2 = 42 teeth."),
        SUM("Holozoic nutrition has five stages: ingestion, digestion, absorption, assimilation and egestion.",
            "Mammals have incisors (cut), canines (tear), premolars and molars (grind). The dental formula shows the teeth in half of each jaw.",
            "A tooth has enamel, dentine, a pulp cavity with blood vessels and nerves, and a root. Acid from bacteria causes decay.",
            "The alimentary canal runs from mouth, oesophagus, stomach, small intestine, large intestine to the anus.",
            "Peristalsis moves food along; the liver, gall bladder and pancreas make juices but are not part of the canal."),
    ],
))

# ------------------------------------------------------------------ 8. Digestion, absorption and assimilation
LESSONS.append(lesson(
    module=NUT,
    topic="Nutrition in mammals",
    title="Digestion, absorption and assimilation",
    slug="bib-digestion-absorption-and-assimilation",
    minutes=25,
    summary="Which enzymes digest starch, protein and lipid and where, the role of bile, how the villus is adapted for absorption in the ileum, and how the liver and body cells assimilate the digested food.",
    objectives=[
        "State the site, enzyme, substrate and products for the digestion of starch, protein and lipid",
        "Explain the roles of hydrochloric acid and bile in digestion",
        "Describe how a villus is adapted for absorption and where each food molecule goes",
        "Explain what is meant by assimilation and the role of the liver",
    ],
    key_concepts=["Digestion", "Amylase", "Protease", "Lipase", "Bile", "Villus", "Lacteal", "Absorption", "Assimilation", "Hepatic portal vein"],
    blocks=[
        H("Introduction"),
        T("A plate of fufu corn and koki beans is a mixture of large, insoluble molecules: starch, protein and some oil. "
          "These are too large to pass through the wall of the gut into the blood. **Digestion** breaks them into "
          "small soluble molecules that can be absorbed."),
        D("**Digestion** is the breakdown of large insoluble food molecules into small soluble molecules by enzymes (chemical digestion) and by chewing and churning (physical digestion).",
          title="Definition: digestion"),
        KEY("What the three food types are broken into", "Learn these end products.", cards=[
            ["Carbohydrate (starch)", "Maltose, then glucose."],
            ["Protein", "Peptides, then amino acids."],
            ["Lipid (fat)", "Fatty acids and glycerol."],
        ]),
        H("Enzymes of digestion"),
        CODE("""Where           Enzyme (made in)             Acts on     Products
Mouth           Salivary amylase (glands)    Starch      Maltose
Stomach         Pepsin (stomach wall)        Protein     Peptides  (acid, about pH 2)
Duodenum        Pancreatic amylase           Starch      Maltose
                Trypsin (pancreas)           Protein     Peptides  (alkaline)
                Lipase (pancreas)            Lipid       Fatty acids + glycerol
Ileum           Maltase (gut wall)           Maltose     Glucose
                Peptidases (gut wall)        Peptides    Amino acids""", "text", title="Digestive enzymes (simplified)"),
        T("Some books use different names, such as erepsin for the peptidases, so check your textbook. The pattern matters most: "
          "each food type has an enzyme, a place and an end product."),
        H("Hydrochloric acid and bile"),
        D("**Hydrochloric acid** in the stomach gives the low pH (about 2) at which pepsin works best, and it kills many bacteria swallowed with food.",
          title="Role of stomach acid"),
        D("**Bile** is a green-yellow liquid made in the liver and stored in the gall bladder. It flows into the duodenum. It contains no enzymes. It **emulsifies** fats and neutralises the acid from the stomach.",
          title="Role of bile"),
        T("Emulsifying means breaking large fat droplets into tiny ones. This gives the lipase a much bigger surface to act on, so "
          "digestion of fat is faster. Bile also makes the contents of the duodenum alkaline, the right pH for the pancreatic enzymes."),
        H("Absorption in the ileum"),
        D("**Absorption** is the movement of digested food molecules from the gut into the blood or lymph.", title="Definition: absorption"),
        T("Most absorption takes place in the **ileum**, the last part of the small intestine. Its wall is covered with thousands of "
          "tiny finger-like projections called **villi** (singular: villus)."),
        IMG("f5bi-b-villus.svg", alt="A villus: finger-like projection with microvilli on its surface, a layer of epithelium one cell thick, a network of capillaries and a central lacteal",
            caption="Figure 1. A villus in the ileum."),
        KEY("How a villus is adapted for absorption", "Each feature has a reason.", cards=[
            ["Many villi and microvilli", "A very large surface area for absorption."],
            ["Wall one cell thick", "A short distance for diffusion."],
            ["Network of capillaries", "A rich blood supply carries glucose and amino acids away, keeping a steep concentration gradient."],
            ["Lacteal", "A lymph vessel that takes in fatty acids and glycerol."],
            ["Mucus and muscle", "Goblet cells make mucus; muscle in the villus keeps it moving."],
        ]),
        T("Glucose and amino acids go into the **blood capillaries**. Fatty acids and glycerol go into the **lacteal**, and then into the lymph, "
          "which joins the blood later. Glucose is absorbed by diffusion and by active transport. Vitamins, minerals and much water are also absorbed here."),
        H("Assimilation"),
        D("**Assimilation** is the use of absorbed food molecules by the body cells to build new materials or to release energy.", title="Definition: assimilation"),
        T("Blood from the ileum goes through the **hepatic portal vein** to the **liver**. The liver controls what reaches the "
          "rest of the body."),
        CODE("""Glucose         Used in respiration for energy. Extra is stored as glycogen in the liver and muscles.
Amino acids     Built into proteins in cells (growth, repair, enzymes). Extra amino acids are changed in
                the liver to urea; this is deamination.
Fatty acids and Used for energy or to build cell membranes. Extra is stored as fat under the skin
glycerol        and around organs.""", "text", title="Fate of absorbed food"),
        H("Egestion"),
        T("The fibre and other undigested material pass into the large intestine. Water is absorbed and the remaining waste forms faeces, which "
          "are stored in the rectum and egested through the anus."),
        EX("Worked example 1: follow starch", intro="Describe the digestion and fate of starch in a mouthful of cooked cassava.", steps=[
            S("Mouth", text="Salivary amylase changes some starch to maltose."),
            S("Duodenum", text="Pancreatic amylase changes more starch to maltose."),
            S("Ileum", text="Maltase changes maltose to glucose."),
            S("Absorption", text="Glucose is absorbed into the blood capillaries of the villi."),
            S("Assimilation", text="The blood goes through the hepatic portal vein to the liver. Glucose is used in respiration or stored as glycogen."),
        ]),
        EX("Worked example 2: why does fat need bile?", intro="Explain why a person with a blocked bile duct digests fat slowly.", steps=[
            S("Without bile", text="Fat stays as large droplets."),
            S("Effect on lipase", text="Lipase can act only on the outside of a drop, so the surface area is small."),
            S("Result", text="Digestion is slow. Also the stomach acid is not neutralised, so enzymes in the duodenum work less well."),
        ]),
        EX("Worked example 3: villus adaptation", intro="Explain why the capillary network inside a villus is an important adaptation.", steps=[
            S("What the blood does", text="It carries glucose and amino acids away quickly."),
            S("Effect on concentration", text="The concentration in the villus stays lower than in the gut, so more diffuses in."),
            S("Result", text="Absorption stays fast."),
        ]),
        MISTAKE("Saying bile digests fat", "Bile contains no enzyme. It emulsifies fat, giving lipase a larger surface. Lipase does the digesting."),
        MISTAKE("Confusing absorption and assimilation", "Absorption is movement into the blood. Assimilation is the use of the molecules by cells."),
        MISTAKE("Saying the enzymes in the stomach work in alkaline conditions", "Pepsin works in acid (about pH 2). The duodenum enzymes need alkaline conditions."),
        TIP("The villus is a favourite Paper 1 diagram. Be ready to label the epithelium, capillary and lacteal and to say why each helps absorption. In Paper 2 essays, give the site, enzyme and products for each food type."),
        QUIZ("Which enzyme digests lipids to fatty acids and glycerol?",
             ["Amylase", "Pepsin", "Lipase", "Maltase"], 2,
             "Lipase acts on lipids and breaks them into fatty acids and glycerol.",
             hint="The name starts with the first letters of 'lipid'.",
             feedback=["Amylase digests starch.", "Pepsin digests protein.", "", "Maltase digests maltose."]),
        QUIZ("Where do fatty acids and glycerol pass after absorption in the villus?",
             ["The blood capillary", "The lacteal", "The stomach", "The pancreas"], 1,
             "The lacteal is the lymph vessel in the middle of the villus that takes in fatty acids and glycerol.",
             hint="Which vessel is separate from the capillaries?",
             feedback=["Glucose and amino acids go into the capillaries.", "", "The stomach is earlier in the gut.", "The pancreas makes enzymes; absorption does not take place there."]),
        PQ("State two functions of bile.", "It emulsifies fats, giving lipase a larger surface area; it neutralises the acid from the stomach, making the pH suitable for the enzymes in the small intestine."),
        PQ("Name the enzyme, the site and the end product of protein digestion in the stomach.", "Pepsin, in the stomach, digests protein to peptides (in acid conditions). Peptidases later change peptides to amino acids in the ileum."),
        PQ("List three ways in which a villus is adapted for absorption.", "Any three: large surface area (villi and microvilli); wall one cell thick; rich blood capillary network; a lacteal; mucus and muscle."),
        PQ("What is assimilation, and what does the liver do with excess amino acids?", "Assimilation is the use of absorbed food molecules by the body cells. The liver changes excess amino acids to urea (deamination)."),
        SUM("Starch is digested to maltose and then glucose; protein to peptides and then amino acids; lipids to fatty acids and glycerol.",
            "Pepsin works in the acid stomach. Bile (no enzymes) emulsifies fat and neutralises acid.",
            "The ileum has villi with microvilli, a thin wall, capillaries and a lacteal for absorption.",
            "Glucose and amino acids go to the blood; fatty acids and glycerol go to the lacteal.",
            "Assimilation uses the molecules: the liver stores glycogen, makes urea from excess amino acids and regulates what reaches the body."),
    ],
))

# ------------------------------------------------------------------ 9. Aerobic and anaerobic respiration
LESSONS.append(lesson(
    module=RESP,
    topic="Aerobic and anaerobic respiration",
    title="Aerobic and anaerobic respiration, oxygen debt and ATP",
    slug="bib-aerobic-and-anaerobic-respiration",
    minutes=25,
    summary="Respiration releases energy from glucose in every living cell. This lesson compares aerobic respiration with anaerobic respiration (alcoholic and lactic acid fermentation), explains oxygen debt and the role of ATP, and describes simple experiments.",
    objectives=[
        "Define respiration and write the word and symbol equations for aerobic respiration",
        "Write the equations for alcoholic and lactic acid fermentation and compare the energy released",
        "Explain oxygen debt and why we breathe hard after exercise",
        "State what ATP is and how it is used by the cell",
    ],
    key_concepts=["Respiration", "Aerobic respiration", "Anaerobic respiration", "Fermentation", "Lactic acid", "Oxygen debt", "ATP", "Mitochondrion"],
    blocks=[
        H("Introduction"),
        T("After a hard football match on a dusty pitch in Bafoussam, a player sits down breathing fast, with tired legs and a "
          "hot body. Her muscle cells have used a lot of energy. That energy came from glucose in a process called **respiration**."),
        T("Every living cell respires, all day and all night. Plants respire too, not only animals."),
        D("**Respiration** is the chemical process in living cells that releases energy from food molecules such as glucose.",
          title="Definition: respiration"),
        T("Do not confuse respiration with **breathing**. Breathing is moving air in and out of the lungs. Respiration is a chemical reaction in cells."),
        H("Aerobic respiration"),
        D("**Aerobic respiration** is the release of a large amount of energy from glucose using oxygen. It takes place mainly in the **mitochondria**.",
          title="Definition: aerobic respiration"),
        CODE("""Word equation:
glucose + oxygen  -->  carbon dioxide + water + energy

Symbol equation:
C6H12O6 + 6O2  -->  6CO2 + 6H2O + energy""", "text", title="Aerobic respiration"),
        T("Check that it balances: 6 carbon, 12 hydrogen and 18 oxygen atoms on each side. The equation is the reverse of the photosynthesis equation, but the two processes are different and use different energy."),
        H("Anaerobic respiration"),
        D("**Anaerobic respiration** is the release of a small amount of energy from glucose without using oxygen. It is also called **fermentation** in yeast and bacteria.",
          title="Definition: anaerobic respiration"),
        T("In **yeast** (alcoholic fermentation), glucose is changed to ethanol and carbon dioxide. This is used to make palm wine, "
          "and to make bread and puff-puff rise, because the carbon dioxide gas forms bubbles in the dough."),
        CODE("""Alcoholic fermentation (yeast):
glucose  -->  ethanol + carbon dioxide + a little energy
C6H12O6  -->  2C2H5OH + 2CO2 + energy""", "text", title="In yeast"),
        T("In **muscle cells** (lactic acid fermentation), when oxygen is short, glucose is changed to lactic acid. No carbon dioxide is made."),
        CODE("""Lactic acid fermentation (muscle):
glucose  -->  lactic acid + a little energy
C6H12O6  -->  2C3H6O3 + energy""", "text", title="In muscle"),
        KEY("Aerobic and anaerobic compared", "Learn the differences.", cards=[
            ["Oxygen", "Aerobic needs oxygen. Anaerobic needs none."],
            ["Products", "Aerobic: carbon dioxide and water. Anaerobic: ethanol and carbon dioxide (yeast) or lactic acid (muscle)."],
            ["Energy", "Aerobic releases much more: about 38 ATP per glucose. Anaerobic releases about 2 ATP per glucose."],
            ["Breakdown", "Aerobic breaks glucose down completely. Anaerobic breaks it down only partly."],
        ]),
        T("The exact ATP numbers differ slightly between books. The key idea is that aerobic respiration releases many times more energy."),
        H("ATP, the energy currency"),
        D("**ATP** (adenosine triphosphate) is a small molecule that stores energy in cells in a form that can be used at once. When a phosphate group is split off, ATP becomes ADP and energy is released.",
          title="Definition: ATP"),
        CODE("""ATP  <-->  ADP + phosphate + energy""", "text"),
        T("Cells use ATP for muscle contraction, active transport, making proteins, nerve impulses and cell division. Some of the energy of respiration is released as heat, which keeps mammals warm."),
        H("Oxygen debt"),
        T("During hard exercise, muscles need energy faster than the blood can bring oxygen. The muscles respire "
          "anaerobically for a while and make **lactic acid**. Lactic acid builds up and can cause tiredness and cramps."),
        D("**Oxygen debt** is the extra oxygen that the body must take in after vigorous exercise to break down the lactic acid made during anaerobic respiration.",
          title="Definition: oxygen debt"),
        T("This is why you keep breathing hard after you stop running. The lactic acid is carried by the blood to the liver, where it is "
          "broken down using oxygen. When the debt is repaid, the breathing rate returns to normal."),
        H("Simple experiments"),
        CODE("""Carbon dioxide from respiration:
Pass air breathed out through limewater. It turns milky.

Anaerobic respiration in yeast:
Boil glucose solution to remove oxygen, cool, add yeast, and pour a layer of oil on top.
Connect to a tube of limewater. The limewater turns milky: carbon dioxide is made.

Heat from respiration:
Put soaked germinating seeds in a vacuum flask with a thermometer. Boiled seeds are the control.
The temperature of the living seeds rises.""", "text", title="Experiments"),
        EX("Worked example 1: after the race", intro="A runner finishes a 400 m race and breathes heavily for several minutes. Explain.", steps=[
            S("During the race", text="The muscles needed more energy than aerobic respiration could supply, so they also respired anaerobically."),
            S("Result", text="Lactic acid built up, giving an oxygen debt."),
            S("After the race", text="Heavy breathing takes in extra oxygen to break down the lactic acid in the liver. When the debt is repaid, breathing slows."),
        ]),
        EX("Worked example 2: dough rises", intro="A baker mixes flour, sugar and yeast and leaves the dough in a warm place. After an hour it has risen. Explain.", steps=[
            S("Yeast respires", text="Yeast uses the sugar by anaerobic respiration (fermentation) inside the dough."),
            S("Gas is made", text="The reaction gives off carbon dioxide."),
            S("Result", text="The gas bubbles are trapped in the dough, so it rises. The ethanol evaporates during baking."),
        ]),
        EX("Worked example 3: limewater", intro="Why does limewater turn milky in the yeast experiment?", steps=[
            S("Carbon dioxide is produced", text="Fermentation makes ethanol and carbon dioxide."),
            S("Test", text="Carbon dioxide reacts with limewater to form a white precipitate, so it turns milky."),
        ]),
        MISTAKE("Saying breathing and respiration are the same thing", "Breathing is the movement of air. Respiration is the chemical release of energy in cells. Write 'cellular respiration' if needed."),
        MISTAKE("Saying lactic acid is made by yeast", "Yeast makes ethanol and carbon dioxide. Lactic acid is made in muscles (and by some bacteria, as in sour milk)."),
        MISTAKE("Saying 'energy is made' in respiration", "Energy is not made or created. It is released from glucose and transferred to ATP and heat."),
        TIP("Respiration appears in Paper 1 as terms, equations and experiment questions (limewater, yeast, vacuum flask). In Paper 2 you may be asked to compare aerobic and anaerobic respiration and explain oxygen debt. Always write both the word and the symbol equation."),
        QUIZ("Which is the product of anaerobic respiration in a human muscle?",
             ["Ethanol", "Lactic acid", "Carbon dioxide and water", "Oxygen"], 1,
             "In muscle, glucose is changed to lactic acid when oxygen is short.",
             hint="Which acid builds up in tired muscles?",
             feedback=["Ethanol is made by yeast.", "", "Carbon dioxide and water are the products of aerobic respiration.", "Oxygen is used in aerobic respiration, not made."]),
        QUIZ("Why does anaerobic respiration release less energy than aerobic respiration?",
             ["It uses more glucose", "Glucose is broken down only partly", "It takes place in the nucleus", "It makes carbon dioxide"], 1,
             "In anaerobic respiration the glucose is not completely broken down, so most of its energy is left in the lactic acid or ethanol.",
             hint="Where does the energy remain?",
             feedback=["It is not the amount of glucose.", "", "Respiration does not occur in the nucleus.", "Aerobic respiration also makes carbon dioxide."]),
        PQ("Write the balanced equation for aerobic respiration.", "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + energy"),
        PQ("Write the word equation for anaerobic respiration in yeast.", "Glucose → ethanol + carbon dioxide + (a little) energy."),
        PQ("Define oxygen debt.", "The extra oxygen taken in after vigorous exercise to break down the lactic acid built up during anaerobic respiration."),
        PQ("State two uses of ATP in cells.", "Any two: muscle contraction, active transport, making proteins, nerve impulses, cell division, keeping warm."),
        SUM("Respiration is the release of energy from glucose in living cells. It is not the same as breathing.",
            "Aerobic: glucose + oxygen → carbon dioxide + water + energy (C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O). It releases much more energy (about 38 ATP).",
            "Anaerobic: yeast makes ethanol and carbon dioxide; muscle makes lactic acid. It releases little energy (about 2 ATP).",
            "Oxygen debt is the extra oxygen needed after hard exercise to remove lactic acid.",
            "ATP carries energy to where the cell needs it; ATP → ADP + phosphate + energy."),
    ],
))

# ------------------------------------------------------------------ 10. Gaseous exchange in plants
LESSONS.append(lesson(
    module=RESP,
    topic="Gaseous exchange in plants",
    title="Gaseous exchange in plants and the stomatal mechanism",
    slug="bib-gaseous-exchange-in-plants",
    minutes=22,
    summary="How oxygen and carbon dioxide enter and leave plants through stomata, lenticels and root surfaces, how day and night change the gas exchange, how guard cells open and close a stoma, and how to use hydrogencarbonate indicator.",
    objectives=[
        "Name the gas exchange surfaces of a plant and the features that suit them",
        "Describe gas exchange in a leaf in daylight and at night",
        "Explain how guard cells open and close a stoma",
        "Interpret a hydrogencarbonate indicator experiment",
    ],
    key_concepts=["Gaseous exchange", "Stoma", "Guard cell", "Lenticel", "Diffusion", "Compensation point", "Hydrogencarbonate indicator"],
    blocks=[
        H("Introduction"),
        T("A cassava farmer knows that if the field is flooded for many days, the roots rot and the plant dies. The roots "
          "have been cut off from air. Roots, stems and leaves all need to take in oxygen for respiration. Leaves also need "
          "carbon dioxide for photosynthesis."),
        D("**Gaseous exchange** is the movement of oxygen and carbon dioxide between an organism and its surroundings, by diffusion.", title="Definition: gaseous exchange"),
        H("A good gas exchange surface"),
        KEY("Features of an exchange surface", "These apply to plants and animals.", cards=[
            ["Large surface area", "More space for gases to diffuse across."],
            ["Thin", "A short distance for diffusion."],
            ["Moist", "Gases dissolve in the film of water before they diffuse."],
            ["Steep concentration gradient", "The gas is used up or carried away on one side, so diffusion continues."],
        ]),
        H("Where plants exchange gases"),
        KEY("Surfaces in a plant", "Three main places.", cards=[
            ["Leaves", "Gases pass through the stomata, mostly in the lower epidermis. Inside, the air spaces in the spongy mesophyll let gases reach every cell."],
            ["Stems", "Woody stems have small pores called lenticels in the bark."],
            ["Roots", "Root hairs take in oxygen from the air spaces in the soil. Flooded soil has no air, so roots can drown."],
        ]),
        T("In a leaf, gases move by diffusion. Carbon dioxide diffuses from the air, through the stoma, through the air spaces and into the "
          "moist surface of the palisade cells. Oxygen diffuses out the other way."),
        H("Gaseous exchange by day and by night"),
        T("**In bright light**, photosynthesis is faster than respiration. The plant uses all the carbon dioxide from respiration and also takes "
          "in carbon dioxide from the air. It gives out the extra oxygen. **At night**, only respiration goes on. The plant takes in oxygen "
          "and gives out carbon dioxide, like an animal."),
        CODE("""                 Photosynthesis   Respiration   Net result
Bright day       fast             slow          CO2 in, O2 out
Dawn or dusk     equal            equal         no net exchange
Night            none             continues     O2 in, CO2 out""", "text", title="Gas exchange in a leaf"),
        D("The **compensation point** is the light intensity at which the rate of photosynthesis equals the rate of respiration, so there is no net gas exchange.",
          title="Definition: compensation point"),
        H("Stomata and guard cells"),
        T("A **stoma** (plural: stomata) is a tiny pore in the epidermis. Each is surrounded by two **guard cells**. Guard cells "
          "have chloroplasts and walls that are thicker on the inner side, next to the pore."),
        IMG("f5bi-b-stomata.svg", alt="Two stomata. In the light the two guard cells are turgid and curved apart leaving an open pore. In the dark they are flaccid, straight and closed",
            caption="Figure 1. A stoma open in the light and closed in the dark."),
        KEY("How a stoma opens", "In the light.", cards=[
            ["1", "In light, the guard cells photosynthesise and their cell sap becomes more concentrated (some books add that potassium ions enter)."],
            ["2", "Water enters by osmosis and the guard cells become turgid."],
            ["3", "The thin outer wall stretches more than the thick inner wall, so the cells curve apart and the pore opens."],
        ]),
        KEY("How a stoma closes", "In the dark or when the plant loses too much water.", cards=[
            ["1", "The sap of the guard cells becomes less concentrated."],
            ["2", "Water leaves by osmosis and the guard cells become flaccid."],
            ["3", "The cells straighten and the pore closes."],
        ]),
        T("Open stomata let carbon dioxide in but also let water vapour out (transpiration). In hot, dry weather the plant closes its stomata to save water, even in the day, and photosynthesis slows down."),
        H("Hydrogencarbonate indicator"),
        T("**Hydrogencarbonate indicator** is red-orange in air. It turns **yellow** when carbon dioxide increases and **purple** when carbon dioxide decreases. We use it to show gas exchange in leaves."),
        CODE("""Tube A: leaf in the light       purple    (CO2 used by photosynthesis faster than made)
Tube B: leaf in the dark        yellow    (only respiration; CO2 made)
Tube C: no leaf, in the light   red       (control, no change)""", "text", title="Typical results"),
        EX("Worked example 1: read the tubes", intro="Three tubes contain hydrogencarbonate indicator. Tube A has a leaf in the light. Tube B has a leaf wrapped in foil. Tube C has no leaf. After two hours A is purple, B is yellow, C is red. Explain each colour.", steps=[
            S("Tube A", text="Photosynthesis used up carbon dioxide faster than respiration made it. Less carbon dioxide gave purple."),
            S("Tube B", text="No light, so no photosynthesis. Respiration added carbon dioxide, so the indicator turned yellow."),
            S("Tube C", text="No leaf, so no change. This is the control."),
        ]),
        EX("Worked example 2: why do stomata close at night?", intro="Explain why most stomata are closed at night.", steps=[
            S("No light", text="Guard cells cannot photosynthesise, so their sap is less concentrated."),
            S("Water movement", text="Water leaves by osmosis and the guard cells become flaccid."),
            S("Result", text="The pore closes, saving water. The leaf does not need carbon dioxide at night."),
        ]),
        EX("Worked example 3: why flooded roots die", intro="Explain why plants in a flooded field may die.", steps=[
            S("Air spaces", text="Water fills the air spaces in the soil. Little oxygen reaches the roots."),
            S("Respiration", text="Root cells cannot respire aerobically. They release little energy."),
            S("Result", text="Roots cannot take in minerals by active transport and may rot."),
        ]),
        MISTAKE("Saying plants only photosynthesise, so they do not need oxygen", "Plants respire all the time, day and night. At night they take in oxygen."),
        MISTAKE("Saying guard cells open because they lose water", "Guard cells open when they gain water and become turgid. They close when they lose water."),
        MISTAKE("Writing 'stomatas' or 'stomas'", "The plural of stoma is stomata. Spell it correctly."),
        TIP("In Paper 1 multiple choice, you may be given a leaf diagram or a hydrogencarbonate indicator experiment. In Paper 2, you may be asked to describe the mechanism of stomatal opening; use the words turgid, flaccid and osmosis."),
        QUIZ("In bright light, a leaf takes in:",
             ["Oxygen and gives out carbon dioxide", "Carbon dioxide and gives out oxygen", "Nitrogen and gives out oxygen", "Only water vapour"], 1,
             "Photosynthesis is faster than respiration in bright light, so the net result is carbon dioxide in and oxygen out.",
             hint="Which process is faster in bright light?",
             feedback=["That is the net exchange at night.", "", "Plants do not use nitrogen gas in gaseous exchange.", "Water vapour leaves, but the main gas exchange is oxygen and carbon dioxide."]),
        QUIZ("What happens to the guard cells when water enters them by osmosis?",
             ["They become flaccid and the stoma closes", "They become turgid and the stoma opens", "They burst", "They stop photosynthesising"], 1,
             "Water makes the guard cells turgid. The uneven walls make them curve apart, so the stoma opens.",
             hint="Which wall of the guard cell is thicker?",
             feedback=["That happens when water leaves.", "", "The cell wall prevents them from bursting.", "Photosynthesis in guard cells occurs in the light."]),
        PQ("State three features of a good gas exchange surface.", "Any three: large surface area, thin, moist, a steep concentration gradient (good supply of gas or carried away)."),
        PQ("Describe how a stoma opens.", "In the light the guard cells accumulate sugars (and some books add potassium ions); water enters by osmosis; the cells become turgid; the thick inner walls curve apart and the pore opens."),
        PQ("Name the tiny pores in the bark of a woody stem through which gases enter.", "Lenticels."),
        PQ("A leaf is placed in hydrogencarbonate indicator in the dark. What colour does the indicator turn, and why?", "Yellow. There is no photosynthesis in the dark. Respiration makes carbon dioxide, which makes the indicator acidic."),
        SUM("Gaseous exchange is the diffusion of oxygen and carbon dioxide across a thin, moist surface with a large area.",
            "Plants exchange gases through the stomata of leaves, lenticels of stems and the root hair surface.",
            "In bright light a leaf takes in carbon dioxide and gives out oxygen; at night it takes in oxygen and gives out carbon dioxide.",
            "Turgid guard cells open the stoma; flaccid guard cells close it.",
            "Hydrogencarbonate indicator turns yellow with more carbon dioxide and purple with less."),
    ],
))

# ------------------------------------------------------------------ 11. Gaseous exchange in animals
LESSONS.append(lesson(
    module=RESP,
    topic="Gaseous exchange in animals",
    title="Gaseous exchange in Amoeba, earthworm, insects and fish",
    slug="bib-gaseous-exchange-in-animals",
    minutes=25,
    summary="How four different animals exchange oxygen and carbon dioxide: diffusion across the surface of Amoeba, the moist skin of the earthworm, the tracheal system of insects, and the gills of fish with their counter-current flow.",
    objectives=[
        "Explain why small organisms can exchange gases through their body surface",
        "Describe gaseous exchange in Amoeba, the earthworm and insects (tracheal system)",
        "Describe how a fish ventilates its gills and how its gills are adapted",
        "Explain the counter-current system and why it is efficient",
    ],
    key_concepts=["Surface area to volume ratio", "Moist skin", "Spiracle", "Trachea", "Tracheole", "Gill filament", "Lamella", "Counter-current flow"],
    blocks=[
        H("Introduction"),
        T("A fish in a pond opens its mouth and closes it again and again. A termite in the soil has no lungs at all. An earthworm "
          "comes out on the surface after heavy rain. All of them need oxygen for respiration, but each takes it in in a "
          "different way. In this lesson you will compare four."),
        T("The idea behind them all is the same. Gases move across a thin, moist surface by diffusion. Larger and more active animals "
          "need special structures to make that surface large."),
        H("Surface area to volume ratio"),
        T("As an organism gets bigger, its volume grows faster than its surface area. Its **surface area to volume ratio** gets smaller. "
          "A very small organism has a large ratio, so diffusion through its surface is enough. A big animal cannot manage."),
        EX("Worked example 1: surface area to volume ratio", intro="Compare a cube of side 1 cm with a cube of side 2 cm.", steps=[
            S("Cube of side 1 cm", math=r"\text{surface area} = 6 \times 1^2 = 6 \text{ cm}^2, \quad \text{volume} = 1 \text{ cm}^3, \quad \text{ratio} = 6"),
            S("Cube of side 2 cm", math=r"\text{surface area} = 6 \times 2^2 = 24 \text{ cm}^2, \quad \text{volume} = 2^3 = 8 \text{ cm}^3, \quad \text{ratio} = 3"),
            S("Conclusion", text="The larger cube has a smaller ratio, 3 compared with 6. Large animals need gills, lungs or tracheae."),
        ]),
        H("Amoeba"),
        T("*Amoeba* is a single-celled organism that lives in fresh water. It is so small that oxygen diffuses straight through "
          "its cell membrane into the cytoplasm. Carbon dioxide diffuses out the same way. No special organ is needed."),
        H("The earthworm"),
        T("The earthworm has no lungs. Gases diffuse through its **moist skin**. The skin is thin and always covered with mucus. "
          "Just below it is a network of capillaries. The blood carries oxygen, dissolved in the plasma and held by haemoglobin, to the rest of the body."),
        KEY("Why an earthworm must stay moist", "Three reasons.", cards=[
            ["Gases dissolve", "Oxygen dissolves in the film of water before diffusing in."],
            ["Mucus", "Mucus keeps the skin wet."],
            ["Burrows", "The worm stays in damp soil. In dry sun its skin dries and it suffocates."],
        ]),
        H("Insects: the tracheal system"),
        T("An insect such as a grasshopper or a cockroach has a hard waterproof outer covering, so it cannot breathe through the skin. "
          "Air enters small openings called **spiracles** along the sides of its thorax and abdomen. The spiracles can open and close to reduce water loss."),
        T("Each spiracle leads into tubes called **tracheae**. Rings of chitin keep them open. The tracheae divide into very thin **tracheolae** "
          "that reach every cell. The ends of the tracheolae are filled with fluid, and oxygen dissolves in it and diffuses into the cells."),
        CODE("""spiracle --> trachea --> tracheole --> body cells
(air in)      (rings keep it open)   (thin, fluid-filled end)

Carbon dioxide leaves by the same route, in the opposite direction.""", "text", title="Air route in an insect"),
        T("Active insects pump their abdomen in and out to push air through the tracheae. The blood of an insect does **not** carry oxygen: the air goes straight to the cells."),
        H("Fish and their gills"),
        T("A fish takes oxygen from the water that flows over its **gills**. Each gill has hundreds of thin **gill filaments**. Each filament has "
          "many tiny folds called **lamellae**. These give a huge surface area. Each lamella is very thin and has a network of blood capillaries."),
        KEY("How a bony fish ventilates its gills", "Water is pumped in a steady flow.", cards=[
            ["Taking in water", "The mouth opens and the floor of the mouth is lowered. The volume of the mouth cavity rises, pressure falls, and water flows in. The operculum (gill cover) is closed."],
            ["Pushing water out", "The mouth closes and the floor of the mouth is raised. The pressure rises. The operculum opens and water flows out over the gills."],
        ]),
        H("Counter-current flow"),
        T("In a gill lamella the blood flows in the **opposite direction** to the water. This is called **counter-current flow**."),
        IMG("f5bi-b-gill-counter-current.svg", alt="Two rows of numbers: in counter-current flow, water goes from 100 to 60 and blood from 50 to 90 in the opposite direction, so blood always meets water with more oxygen; in parallel flow, both reach about 75",
            caption="Figure 1. Counter-current flow compared with parallel flow (illustrative oxygen values)."),
        T("In counter-current flow, the blood always meets water that holds more oxygen than the blood does. So diffusion goes on along the "
          "whole length of the lamella, and the blood leaves almost as rich in oxygen as the water. In the parallel flow, the blood and water would soon "
          "reach the same oxygen level, and diffusion would stop. A fish that uses counter-current flow takes in most of the oxygen from the water."),
        EX("Worked example 2: why counter-current is better", intro="Use Figure 1 to compare the oxygen in the blood leaving the gill in the two systems.", steps=[
            S("Counter-current", text="The blood leaves with 90 units."),
            S("Parallel", text="The blood leaves with about 76 units."),
            S("Difference", math=r"90 - 76 = 14 \text{ units more}"),
            S("Reason", text="In counter-current flow a concentration gradient is kept all along the lamella, so diffusion never stops."),
        ]),
        EX("Worked example 3: fish out of water", intro="Why does a fish die quickly when taken out of water, although the air has more oxygen?", steps=[
            S("Gill structure", text="In water the filaments are held apart by the water."),
            S("In air", text="The filaments stick together, so the surface area drops sharply, and the surface dries."),
            S("Result", text="Too little oxygen can be absorbed and the fish suffocates."),
        ]),
        MISTAKE("Saying insects breathe through lungs or that blood carries their oxygen", "Insects use tracheae. Air goes directly to the cells through tracheoles."),
        MISTAKE("Saying the water and blood flow the same way in gills", "They flow in opposite directions. That is counter-current flow."),
        MISTAKE("Saying earthworms breathe through the mouth", "An earthworm exchanges gases through its moist skin."),
        TIP("In Paper 1 multiple choice you may be asked to match an animal with its gas exchange organ. In Paper 2 essays, draw and label a gill lamella with arrows for water and blood, or describe the tracheal system. Use the words spiracle, trachea, tracheole, lamella and counter-current."),
        QUIZ("Through which structure does air enter the body of an insect?",
             ["Gills", "Lungs", "Spiracles", "Skin"], 2,
             "Air enters through small openings called spiracles along the body.",
             hint="Insects have a hard waterproof outer covering.",
             feedback=["Gills are used by fish.", "Insects have no lungs.", "", "The insect's hard covering does not allow gases to pass."]),
        QUIZ("Why is the counter-current system in a fish gill efficient?",
             ["It keeps the water and blood at the same oxygen level", "It keeps a concentration gradient along the whole length", "It slows down the blood", "It stops water entering the gills"], 1,
             "Blood always meets water with a higher oxygen concentration, so diffusion occurs all along the lamella.",
             hint="What does the blood meet along its journey?",
             feedback=["If the levels became equal, diffusion would stop.", "", "It does not change the speed of blood in this way.", "Water must enter and flow over the gills."]),
        PQ("Why can an Amoeba exchange gases without special organs?", "It is very small, so its surface area to volume ratio is large, and oxygen and carbon dioxide diffuse quickly across the cell membrane."),
        PQ("Describe the route of air through an insect.", "Air enters through a spiracle, then goes into a trachea, then into tracheoles, and diffuses into the body cells. Carbon dioxide goes back the same way."),
        PQ("State two features of a gill lamella that make it good for gas exchange.", "Any two: very thin wall (short diffusion distance); large surface area; rich blood capillary network; water flows over it all the time."),
        PQ("A cube has sides of 3 cm. Calculate its surface area to volume ratio.", "Surface area = 6 × 9 = 54 cm². Volume = 27 cm³. Ratio = 54 ÷ 27 = 2."),
        SUM("Small organisms such as Amoeba exchange gases by diffusion across the surface because their surface area to volume ratio is large.",
            "The earthworm uses its moist skin, which has capillaries below it, and it must stay damp.",
            "Insects have spiracles, tracheae and tracheolae; air goes directly to the cells.",
            "Fish have gills with filaments and lamellae; water is pumped over them by the mouth and operculum.",
            "Counter-current flow keeps a diffusion gradient along the whole lamella and lets the blood take up most of the oxygen."),
    ],
))

# ------------------------------------------------------------------ 12. Human respiratory system
LESSONS.append(lesson(
    module=RESP,
    topic="The human respiratory system",
    title="The human respiratory system, ventilation and lung capacities",
    slug="bib-human-respiratory-system-and-ventilation",
    minutes=25,
    summary="The parts of the human breathing system, how the alveoli are adapted for gas exchange, how the ribs and diaphragm ventilate the lungs, the difference between inhaled and exhaled air, and what tidal volume, vital capacity and residual volume mean.",
    objectives=[
        "Name the parts of the human respiratory system and state the function of each",
        "Explain how the alveolus is adapted for gaseous exchange",
        "Describe the mechanism of inspiration and expiration",
        "Define tidal volume, vital capacity and residual volume and read them from a trace",
    ],
    key_concepts=["Trachea", "Bronchus", "Alveolus", "Diaphragm", "Intercostal muscles", "Inspiration", "Expiration", "Tidal volume", "Vital capacity", "Residual volume"],
    blocks=[
        H("Introduction"),
        T("Climb the stairs to the top of a hostel and you will breathe faster. Run up Mount Cameroon and you will breathe harder still. "
          "Your lungs supply the oxygen your cells need and remove the carbon dioxide they make. In this lesson you will "
          "see how the breathing system does this."),
        H("Parts of the breathing system"),
        IMG("f5bi-b-lungs.svg", alt="Diagram of the chest: the trachea with rings, splitting into two bronchi, branching into bronchioles ending in clusters of alveoli inside the lungs, with ribs around the lungs and the diaphragm below",
            caption="Figure 1. The human respiratory system (front view, simplified)."),
        KEY("Path of air", "From nose to alveoli.", cards=[
            ["Nose", "Hairs and mucus trap dust. The nasal cavity warms and moistens the air."],
            ["Trachea (windpipe)", "A tube held open by C-shaped rings of cartilage. Lined with cilia and mucus-making cells."],
            ["Bronchi", "Two tubes, one into each lung. They also have cartilage."],
            ["Bronchioles", "Narrow branching tubes with no cartilage rings."],
            ["Alveoli", "Tiny air sacs at the ends of the bronchioles. Gas exchange takes place here."],
        ]),
        T("The cilia in the trachea beat upwards and sweep mucus, with trapped dust and bacteria, to the throat to be swallowed. "
          "Smoking damages the cilia. The lungs lie in the chest, protected by the **ribs**. The **diaphragm** is a sheet of muscle that forms the floor of the chest. "
          "Two thin **pleural membranes** surround the lungs, with a little fluid between them. The fluid reduces friction when the lungs move."),
        H("The alveolus"),
        D("An **alveolus** (plural: alveoli) is a tiny air sac in the lungs. Oxygen diffuses from the air in the alveolus into the blood, and carbon dioxide diffuses from the blood into the air.",
          title="Definition: alveolus"),
        KEY("How alveoli are adapted for gas exchange", "Each feature has a reason.", cards=[
            ["Very many alveoli", "Millions of them give a huge surface area."],
            ["Wall one cell thick", "A very short diffusion distance."],
            ["Moist inner surface", "Gases dissolve before they diffuse."],
            ["Dense network of capillaries", "Blood carries oxygen away and brings carbon dioxide, keeping a steep gradient."],
            ["Constant ventilation", "Breathing keeps fresh air in the alveoli."],
        ]),
        T("Oxygen is carried by the red blood cells as oxyhaemoglobin. Carbon dioxide travels mainly in the plasma."),
        H("Inhaled and exhaled air"),
        CODE("""Gas              Inhaled air        Exhaled air
Oxygen           about 21%          about 16%
Carbon dioxide   about 0.04%        about 4%
Nitrogen         about 78%          about 78%
Water vapour     variable           high (saturated)
Temperature      air temperature    warmer (body temperature)""", "text", title="Approximate composition of air"),
        T("Exhaled air has less oxygen because the body used some. It has more carbon dioxide and water vapour because of respiration. The values vary a little between books, so check your textbook."),
        H("Ventilation: breathing in and out"),
        D("**Ventilation** (breathing) is the movement of air into and out of the lungs by changing the volume of the chest cavity.", title="Definition: ventilation"),
        CODE("""                      Breathing in (inspiration)     Breathing out (expiration)
Intercostal muscles   external ones contract         external ones relax
Ribs                  move up and out                move down and in
Diaphragm             contracts, becomes flatter     relaxes, becomes dome-shaped
Chest volume          increases                      decreases
Pressure in lungs     falls below atmospheric        rises above atmospheric
Air movement          flows in                       flows out""", "text", title="Mechanism of breathing"),
        T("Air always moves from a region of higher pressure to a region of lower pressure. When the chest volume increases, the pressure falls "
          "and air is pushed in by the outside air. In forced breathing, such as during exercise, the internal intercostal muscles and the abdominal muscles also help to push air out."),
        H("Lung volumes and capacities"),
        T("A **spirometer** records the volume of air breathed in and out. The trace on the figure is a spirometer-style record. Notice that after the "
          "strongest breath out, some air still remains in the lungs."),
        IMG("f5bi-b-lung-volumes.svg", alt="Trace of lung volume against time: quiet breathing between 2300 and 2800 cubic centimetres, then a deep breath in to 5800 and out to 1200, then quiet breathing again",
            caption="Figure 2. A spirometer trace with the main lung volumes (typical adult teaching values)."),
        KEY("Lung volumes", "Typical adult values; they vary between people and books.", cards=[
            ["Tidal volume", "The volume of air breathed in or out in one quiet breath. About 500 cm³."],
            ["Inspiratory reserve volume (IRV)", "Extra air you can breathe in after a normal breath in. About 3000 cm³."],
            ["Expiratory reserve volume (ERV)", "Extra air you can breathe out after a normal breath out. About 1100 cm³."],
            ["Residual volume", "Air left in the lungs after the strongest breath out. About 1200 cm³. It cannot be breathed out."],
            ["Vital capacity", "The greatest volume you can breathe out after breathing in as deeply as possible: IRV + tidal volume + ERV. About 4600 cm³."],
        ]),
        F(r"\text{Vital capacity} = \text{IRV} + \text{tidal volume} + \text{ERV}", title="Vital capacity"),
        T("During exercise the muscles make more carbon dioxide. The brain detects the rise in carbon dioxide in the blood and makes you breathe faster and deeper."),
        EX("Worked example 1: vital capacity", intro="IRV = 3000 cm³, tidal volume = 500 cm³, ERV = 1100 cm³ and residual volume = 1200 cm³. Find the vital capacity and the total lung capacity.", steps=[
            S("Vital capacity", math=r"3000 + 500 + 1100 = 4600 \text{ cm}^3"),
            S("Total lung capacity", math=r"\text{vital capacity} + \text{residual volume} = 4600 + 1200 = 5800 \text{ cm}^3"),
        ]),
        EX("Worked example 2: air breathed per minute", intro="A student breathes 15 times in one minute with a tidal volume of 500 cm³. How much air is breathed in one minute?", steps=[
            S("Multiply", math=r"15 \times 500 = 7500 \text{ cm}^3"),
            S("Convert to litres", math=r"7500 \text{ cm}^3 = 7.5 \text{ litres}"),
        ]),
        EX("Worked example 3: explain breathing in", intro="Explain how air enters the lungs when you breathe in.", steps=[
            S("Muscles", text="The external intercostal muscles contract, raising the ribs up and out, and the diaphragm contracts and flattens."),
            S("Volume and pressure", text="The volume of the chest increases, so the pressure inside the lungs falls below atmospheric pressure."),
            S("Result", text="Air flows in from outside until the pressures are equal."),
        ]),
        MISTAKE("Saying the lungs push air in and out themselves", "The lungs have no muscle. The ribs and diaphragm change the chest volume and the lungs follow."),
        MISTAKE("Saying the diaphragm relaxes and flattens when breathing in", "Breathing in: the diaphragm contracts and flattens. Breathing out: it relaxes and becomes dome-shaped."),
        MISTAKE("Saying exhaled air has no oxygen", "Exhaled air still has about 16 percent oxygen. Only about 5 percentage points are used."),
        TIP("The respiratory system is a favourite for Paper 1 diagrams (label the trachea, bronchus, alveoli, diaphragm) and for Paper 2 questions on the mechanism of breathing and on air composition. Always give both muscle action and the changes in volume and pressure."),
        QUIZ("What happens to the diaphragm when you breathe in?",
             ["It relaxes and becomes dome-shaped", "It contracts and flattens", "It moves up", "It does not move"], 1,
             "The diaphragm contracts and flattens. The chest volume rises and air flows in.",
             hint="Contracting muscles shorten and flatten.",
             feedback=["That happens when you breathe out.", "", "It moves down when flattened.", "It moves with every breath."]),
        QUIZ("Which feature of the alveolus helps oxygen to diffuse quickly into the blood?",
             ["A thick wall", "A wall one cell thick", "A dry surface", "A lack of capillaries"], 1,
             "A very thin wall makes the diffusion distance short.",
             hint="A short distance means faster diffusion.",
             feedback=["A thick wall would slow diffusion.", "", "The surface must be moist for gases to dissolve.", "Capillaries are needed to carry the oxygen away."]),
        PQ("Name the two sets of muscles used in breathing in.", "The external intercostal muscles and the diaphragm."),
        PQ("State two ways in which the alveoli are adapted for gas exchange.", "Any two: very many, giving a large surface area; wall one cell thick; moist surface; network of capillaries; ventilation keeps the gradient steep."),
        PQ("Compare the amount of carbon dioxide in inhaled and exhaled air.", "Inhaled air has about 0.04 percent; exhaled air has about 4 percent. The extra carbon dioxide comes from respiration in body cells."),
        PQ("A student's vital capacity is 4400 cm³ and the residual volume 1200 cm³. Find the total lung capacity.", "4400 + 1200 = 5600 cm³."),
        SUM("Air passes through the nose, trachea, bronchi and bronchioles to the alveoli, where gas exchange takes place by diffusion.",
            "Alveoli have a large surface area, a thin moist wall and a rich capillary network.",
            "Breathing in: intercostals and diaphragm contract, chest volume rises, pressure falls, air flows in. Breathing out is the reverse.",
            "Exhaled air has less oxygen (about 16 percent) and more carbon dioxide (about 4 percent) and water vapour than inhaled air.",
            "Tidal volume is one quiet breath; vital capacity = IRV + tidal volume + ERV; residual volume stays in the lungs."),
    ],
))
