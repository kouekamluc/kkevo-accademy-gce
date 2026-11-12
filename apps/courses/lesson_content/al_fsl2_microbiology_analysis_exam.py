"""A Level Food Science and Nutrition (0740), Lower Sixth: Food Microbiology & Food Safety, Sensory Evaluation & Food Analysis, and the Examination module.

7 topic lessons (fsl2-) and 3 examination lessons (fsl2-paper...), one practice set each (see the practice file of the same name).
Content follows KKEVO's master curriculum blueprint (L6M4 and L6M5) and the Board's 2023 subject report for exam structure and common
errors; it is not a Board syllabus booklet. Growth, fermentation yield, sensory significance tables, Kjeldahl, Soxhlet, titratable
acidity, moisture and Karl Fischer calculations were checked by script. Teaching figures are labelled as invented for practice.
"""

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "lower-sixth")

M_MIC = "Food Microbiology & Food Safety"
M_SEN = "Sensory Evaluation & Food Analysis"
M_EXAM = "Examination"

LESSONS = []

# ------------------------------------------------------------------ 1. Factors affecting microbial growth
LESSONS.append(lesson(
    module=M_MIC,
    topic="Factors affecting microbial growth",
    title="What makes microbes grow in food: intrinsic and extrinsic factors",
    slug="fsl2-factors-microbial-growth",
    minutes=24,
    summary="The growth curve of bacteria and the intrinsic factors (pH, water activity, nutrients, redox potential, antimicrobials) and extrinsic factors (temperature, humidity, gases) that decide whether food spoils, stays safe or becomes dangerous.",
    objectives=[
        "Describe the four phases of a bacterial growth curve and calculate generations and generation time",
        "Explain how pH, water activity, nutrients, redox potential (Eh) and natural antimicrobials control growth",
        "Explain how storage temperature, humidity and gas composition control growth",
        "Use the hurdle idea to explain why combining several mild controls keeps food safe",
    ],
    key_concepts=["Growth curve", "Generation time", "pH", "Water activity", "Redox potential (Eh)", "Mesophile", "Danger zone", "Hurdle technology"],
    blocks=[
        H("Introduction"),
        T("A woman in Bafoussam cooks a pot of rice and leaves it on the table all afternoon. By evening it smells wrong, or worse, it "
          "smells normal but makes the family ill. Cooked rice, moist and full of starch, is an ideal home for microbes. Dry "
          "garri in a sealed bag, by contrast, can be kept for months. The difference is not luck. It is the set of conditions that each "
          "food provides, and they can be named, measured and controlled. This is the basis of food preservation and of food safety."),
        H("How bacteria multiply"),
        T("Most bacteria reproduce by **binary fission**: one cell becomes two, two become four, and so on. The population "
          "doubles every **generation time** (also called doubling time). If a cell divides every 20 minutes, one cell becomes about a "
          "billion cells in 10 hours. The number of cells after $n$ generations is given by the rule below."),
        F(r"N = N_0 \times 2^{n} \qquad n = \frac{\log N - \log N_0}{\log 2} = \frac{\text{time}}{\text{generation time}}", title="Bacterial growth"),
        D("In a closed culture (a batch of food or broth) the number of living bacteria follows four phases: **lag** (cells adjust, little "
          "division), **log or exponential** (fastest division, straight line on a log scale), **stationary** (nutrients run low and wastes build up, so "
          "births equal deaths) and **death** (more cells die than divide).", title="The growth curve"),
        IMG("alfsl2-growth-curve.svg", alt="Graph of the log of living cells against time showing the lag phase, the rising log phase, the flat stationary phase and the falling death phase",
            caption="Figure 1. The four phases of growth of bacteria in a closed culture."),
        T("Food safety aims to keep bacteria in the lag phase for as long as possible, or to stop them growing at all. "
          "Good hygiene keeps the starting number $N_0$ low. Cold storage lengthens the lag phase and the generation time. "
          "Everything in the rest of the lesson is a way of lengthening lag, slowing the log phase, or making conditions impossible."),
        EX("Worked example 1: growth calculation", intro="A cooked sauce is contaminated with 1 000 bacterial cells. The generation time at the room temperature of the kitchen is 20 minutes. How many cells are there after 2 hours? (Assume no lag phase; this is a teaching model.)", steps=[
            S("Number of generations", math=r"n = \frac{120}{20} = 6"),
            S("Apply the growth rule", math=r"N = 1000 \times 2^{6} = 64\,000", text="The cells multiplied 64 times in only two hours."),
        ], check=r"1000 \times 64 = 64\,000"),
        EX("Worked example 2: finding the generation time", intro="A broth contains 1 000 cells per cm³. Five hours later, during the log phase, it contains 1 000 000 cells per cm³. Find the number of generations and the generation time.", steps=[
            S("Number of generations", math=r"n = \frac{\log 10^{6} - \log 10^{3}}{\log 2} = \frac{3}{0.301} = 9.97 \approx 10"),
            S("Generation time", math=r"\frac{300 \text{ min}}{9.97} = 30 \text{ minutes}", text="Each doubling takes about 30 minutes."),
        ]),
        H("Intrinsic factors: properties of the food"),
        T("**Intrinsic factors** belong to the food itself. Each factor has a range in which a given microbe can grow, with a minimum, an optimum and a maximum."),
        KEY("The intrinsic factors", "Five properties of the food decide who can grow.", cards=[
            ["pH", "Most bacteria grow best near neutral (about pH 6.5 to 7.5) and few grow below about pH 4.5 (check your textbook for exact limits). Yeasts and moulds tolerate acid foods such as fruit juice. This is why spoiled juice is usually yeast or mould, and spoiled meat is bacterial."],
            ["Water activity (a_w)", "The water that microbes can use, on a scale from 0 to 1. Most spoilage bacteria need about 0.90 or more, most yeasts about 0.88, many moulds about 0.80, and a few specialised moulds and yeasts below 0.70 (typical teaching values; check your textbook)."],
            ["Nutrients", "Microbes need carbon, nitrogen, minerals and vitamins. Rich foods (meat, milk, eggs, cooked rice) support almost everyone. Fruits are low in protein and favour yeasts and moulds."],
            ["Redox potential (Eh)", "How much oxygen is available. Aerobes need oxygen, anaerobes are harmed by it, and facultative organisms grow either way. The inside of a thick stew or a can is low in oxygen, which suits Clostridium."],
            ["Natural antimicrobials and structure", "Egg white lysozyme, lactoferrin in milk, and compounds in spices and garlic slow growth. Shells, skins and rinds are physical barriers; grinding or cutting breaks them."],
        ]),
        T("Water activity links to the lesson on water activity in Food Chemistry. Salting, sugaring and drying work by lowering a_w, not by adding poison. "
          "Dried fish, groundnuts and smoked meat survive because a_w is low, but if they take up moisture the moulds start again."),
        H("Extrinsic factors: the storage environment"),
        T("**Extrinsic factors** are conditions around the food. Temperature is the most important. By their preferred temperature, microbes fall into groups."),
        KEY("Groups by temperature", "Cardinal temperatures differ.", cards=[
            ["Psychrophiles and psychrotrophs", "Grow in the cold, from about 0 to 20 degrees C. They spoil food slowly in a refrigerator. Some pathogens, such as Listeria, can still multiply at refrigerator temperatures."],
            ["Mesophiles", "Grow best from about 20 to 45 degrees C, with an optimum near 37 degrees C. Nearly all human pathogens are mesophiles, because they are adapted to the human body."],
            ["Thermophiles", "Grow best from about 45 to 70 degrees C. They matter in hot-held food, canned food stored in hot places, and some spore-formers."],
        ]),
        IMG("alfsl2-temperature-scale.svg", alt="Vertical temperature scale from minus 18 to 100 degrees Celsius with the danger zone between 5 and 60 degrees shaded",
            caption="Figure 2. Safe and unsafe temperatures (teaching values). Exact limits differ by textbook and by country: check your textbook."),
        T("Food kept between about 5 and 60 degrees C is in the **danger zone**, where the common pathogens multiply fastest. "
          "A refrigerator (0 to 5 degrees C) slows growth. A freezer at -18 degrees C stops it, but does not kill all the microbes; they restart when food thaws. "
          "Cooking to a core temperature of about 70 degrees C or more (check the rule your teacher uses) kills most vegetative cells, but not heat-resistant spores or heat-stable toxins."),
        T("**Relative humidity** of the air decides whether the surface of a food gains or loses water, so it changes a_w. Dried goods in humid air take up water and spoil. "
          "**Gases** matter too: vacuum packing and modified atmospheres (more carbon dioxide, less oxygen) stop aerobic spoilers, although they may favour anaerobes."),
        H("Hurdles together"),
        D("**Hurdle technology** combines several mild barriers (for example low pH, reduced a_w, cooling and a preservative) so that each one stops microbes "
          "from growing, and together they give food that is safe and keeps its taste and nutrients.", title="Hurdle technology"),
        T("A single strong treatment, like very heavy salting, can ruin taste. Several small hurdles work together: smoked, salted fish that is also dried and kept in a dry store is safer than any one step alone."),
        MISTAKE("Saying that freezing kills bacteria", "Freezing stops growth because liquid water is unavailable and enzymes slow down, but many cells survive. After thawing, growth restarts, sometimes within hours. Use the words 'stops or slows growth' unless the question is about heat."),
        MISTAKE("Mixing up pH and a_w", "Low pH means acid. Low water activity means little available water. A salted fish has low a_w and neutral pH; a lemon juice has low pH and high a_w. Name the correct factor."),
        TIP("Exam link: Paper 1 asks for factors and typical limits, and calculations of generation time. Paper 2 essays on food spoilage and preservation expect both intrinsic and extrinsic factors with an example food for each. Use 'because' sentences: low a_w, so the microbe cannot take water."),
        QUIZ("Which food is most likely to support the growth of bacteria if left in a warm kitchen?", ["Dry groundnuts in a sealed jar", "Cooked rice and fish stew", "Lemon juice", "Salted dried fish"], 1,
             "Cooked rice and fish stew has a high a_w, a near neutral pH and plenty of nutrients, so it supports bacterial growth.",
             hint="Look for high water, near neutral pH and protein.",
             feedback=["Low a_w stops growth.", "", "Its low pH limits most bacteria.", "Salt has lowered the a_w."]),
        QUIZ("Bacteria in a closed culture stop increasing in number although some cells still divide. Which phase is this?", ["Lag phase", "Log phase", "Stationary phase", "Death phase"], 2,
             "In the stationary phase new cells are balanced by dying cells because nutrients run out and wastes build up.",
             hint="Births equal deaths.",
             feedback=["In lag the cells adjust to the new food and divide little.", "In log the number rises fastest.", "", "In death the number falls."]),
        PQ("(a) State two intrinsic and two extrinsic factors affecting microbial growth. (b) A starting population of 500 cells has a generation time of 30 minutes. Calculate the number after 3 hours.",
           "(a) Intrinsic: pH, water activity (also nutrients, Eh, antimicrobials). Extrinsic: temperature, relative humidity (also gases). (b) 3 hours = 180 minutes, n = 180/30 = 6. N = 500 × 2^6 = 500 × 64 = 32 000 cells."),
        PQ("Explain why moist cooked rice kept at 30 degrees C for six hours is a food safety risk, but dry uncooked rice in a sealed bag is not.",
           "Cooked rice has a high a_w and a neutral pH, plenty of starch and the temperature is within the danger zone and near the mesophile optimum, so bacteria (and any surviving spores) grow and may form toxins. Dry rice has a very low a_w, so no microbe can take up water to grow, and the sealed bag keeps humidity out."),
        PQ("Describe two hurdles that can be combined to preserve smoked fish and say why combining them is better than one hurdle.",
           "Examples: drying (low a_w), salting (low a_w and some direct effect on cells), smoking (antimicrobial chemicals and surface drying), low temperature storage, packaging that keeps out moisture. Each hurdle alone lets some microbes grow; together they block every group while keeping taste and nutrients, so milder treatments can be used."),
        SUM("Bacteria grow in four phases: lag, log, stationary and death; N = N0 × 2^n.",
            "Intrinsic factors are pH, water activity, nutrients, redox potential and natural antimicrobials.",
            "Extrinsic factors are temperature, relative humidity and gases; the danger zone is about 5 to 60 degrees C.",
            "Most pathogens are mesophiles; refrigeration slows growth and freezing stops it but does not kill all cells.",
            "Hurdle technology combines several mild barriers to keep food safe."),
    ],
))

# ------------------------------------------------------------------ 2. Beneficial fermentation
LESSONS.append(lesson(
    module=M_MIC,
    topic="Beneficial fermentation",
    title="Useful microbes: lactic acid bacteria, yeasts and fermented foods",
    slug="fsl2-beneficial-fermentation",
    minutes=23,
    summary="How lactic acid bacteria and yeasts make food safer, tastier and more nutritious by fermentation, with the balanced equations, yield calculations and examples such as yoghurt, bread, palm wine and fermented cassava.",
    objectives=[
        "Define fermentation and distinguish lactic acid fermentation from alcoholic fermentation",
        "Write and use the equations for both fermentations, including theoretical yield",
        "Explain how fermentation preserves food and improves its nutrition, flavour and texture",
        "Describe examples of fermented foods and the role of starter cultures",
    ],
    key_concepts=["Fermentation", "Lactic acid bacteria", "Homofermentative", "Heterofermentative", "Yeast", "Starter culture", "Probiotic", "Bacteriocin"],
    blocks=[
        H("Introduction"),
        T("Not all microbes in food are enemies. Bread rises, yoghurt thickens, palm wine foams and cassava sticks (bobolo, baton de manioc) become soft and safe because of microbes doing useful work. "
          "People used these methods thousands of years before microbes were discovered. At A Level you must explain the chemistry and the reasons that fermented foods are safer and keep longer."),
        D("**Fermentation** in food technology is the controlled use of microbes to change a food by breaking down its carbohydrates (and sometimes proteins and fats) without a full supply of oxygen, "
          "making acids, alcohol, gases and flavour compounds.", title="Fermentation"),
        H("Lactic acid bacteria"),
        T("**Lactic acid bacteria (LAB)** are Gram-positive bacteria that make lactic acid as the main product of sugar breakdown. The common genera are Lactobacillus, Lactococcus, Streptococcus (thermophilus) and Leuconostoc. "
          "They tolerate acid, need rich media and grow without oxygen, though they are not harmed by it."),
        KEY("Two kinds of lactic fermentation", "Compare the pathways.", cards=[
            ["Homofermentative", "Glucose gives almost only lactic acid. One mole of glucose gives two moles of lactic acid. Examples: Lactococcus lactis, Streptococcus thermophilus."],
            ["Heterofermentative", "Glucose gives lactic acid plus ethanol (or acetic acid) and carbon dioxide. This gives gas, flavour and the holes in some cheeses. Example: Leuconostoc."],
        ]),
        F(r"\mathrm{C_6H_{12}O_6 \;\longrightarrow\; 2\,CH_3CH(OH)COOH}", title="Homolactic fermentation of glucose"),
        T("Acid production is the main preservative effect. The pH falls (often to about 4 to 4.5), which stops growth of most spoilage and pathogenic bacteria. LAB also make hydrogen peroxide and "
          "small proteins called **bacteriocins** (nisin is a well-known one) that kill related bacteria. In addition, LAB use up the nutrients so that other microbes cannot compete."),
        T("In **yoghurt**, two bacteria work together: Lactobacillus delbrueckii subsp. bulgaricus and Streptococcus thermophilus. They convert lactose to lactic acid. The acid lowers the pH to about the isoelectric point of casein, "
          "so the milk proteins coagulate and form the gel. In **cheese**, LAB make acid, then rennet enzymes complete the curd; in **fermented cassava** and cereal porridges, LAB sour the food and help reduce natural toxins and some anti-nutrients."),
        H("Yeasts and alcoholic fermentation"),
        T("**Yeasts** are single-celled fungi. Saccharomyces cerevisiae ferments sugars in the absence of oxygen to ethanol and carbon dioxide. In bread, the carbon dioxide makes the dough rise and the ethanol evaporates in the oven. In palm wine, sugar-rich sap is fermented by wild yeasts (often with lactic and acetic bacteria, so it turns sour in a day); in beer and wine, the ethanol is the product wanted."),
        F(r"\mathrm{C_6H_{12}O_6 \;\longrightarrow\; 2\,C_2H_5OH + 2\,CO_2}", title="Alcoholic fermentation of glucose"),
        EX("Worked example 1: theoretical yield", intro="A yeast ferments 180 g of glucose completely to ethanol and carbon dioxide. Calculate the theoretical masses of ethanol and carbon dioxide. (Relative molecular masses: glucose 180, ethanol 46, carbon dioxide 44.)", steps=[
            S("Moles of glucose", math=r"\frac{180}{180} = 1 \text{ mol}"),
            S("Ethanol", math=r"2 \times 46 = 92 \text{ g}"),
            S("Carbon dioxide", math=r"2 \times 44 = 88 \text{ g}", text="Mass is conserved: 92 + 88 = 180 g. Ethanol is 51 percent of the glucose mass, the theoretical maximum. Real yeast makes less, because some sugar goes into new cells."),
        ], check=r"92 + 88 = 180"),
        EX("Worked example 2: lactic acid", intro="A homofermentative culture converts 90 g of glucose to lactic acid (relative molecular mass 90). How much lactic acid is formed in theory?", steps=[
            S("Moles of glucose", math=r"\frac{90}{180} = 0.5 \text{ mol}"),
            S("Moles of lactic acid", math=r"2 \times 0.5 = 1.0 \text{ mol}"),
            S("Mass", math=r"1.0 \times 90 = 90 \text{ g}", text="The mass of lactic acid equals the mass of glucose, because the reaction is an isomerisation (same formula, one glucose gives two lactic acids)."),
        ]),
        H("Why fermented foods matter"),
        KEY("Benefits of fermentation", "Fermented foods help in five ways.", cards=[
            ["Safety and preservation", "Acid (and sometimes alcohol) stops pathogens. Fermented foods keep longer without a fridge."],
            ["Flavour and texture", "Acids, esters, diacetyl and gas give sour taste, aroma and soft, thick or open textures."],
            ["Nutrition", "Fermentation can raise B vitamins, break down phytates and starch, and release minerals and amino acids. Cassava fermentation also lowers cyanogenic glycosides."],
            ["Digestibility", "Lactose is partly broken down in yoghurt, so many people with lactose intolerance tolerate it better."],
            ["Probiotic effect", "Some live cultures survive in the gut and may support gut health (research continues; use the word 'may')."],
        ]),
        T("**Starter cultures** are selected strains added on purpose (for yoghurt, bread and cheese) to give a fast, reliable and safe fermentation. **Spontaneous** (natural) fermentations rely on microbes already in the raw material, as with many traditional foods. "
          "The risk of spontaneous fermentation is that the wrong microbes win; keeping salt, temperature and clean equipment right is the control."),
        MISTAKE("Calling every microbe in food harmful", "Fermented foods rely on live microbes. The point is control: the right microbe, the right conditions. A question about 'beneficial' microbes wants the product, the organism and the benefit."),
        MISTAKE("Writing the equation with the wrong ratio", "One glucose gives TWO lactic acid, or TWO ethanol plus TWO carbon dioxide. A missing 2 is a common loss of marks. Check the atoms: C6 on the left, C2 times 2 plus C1 times 2 on the right."),
        TIP("Exam link: Paper 1 asks for organisms and products of fermentation; Paper 2 asks for explanation of how fermentation preserves food and the steps in making a fermented product. Use an example from your own region where you can (check your textbook)."),
        QUIZ("Which organism and process are used to make dough rise?", ["Lactobacillus making lactic acid", "Saccharomyces cerevisiae making ethanol and carbon dioxide", "Aspergillus making aflatoxin", "Streptococcus making diacetyl only"], 1,
             "Yeast ferments sugars to ethanol and carbon dioxide; the gas expands in the dough.",
             hint="Which product is a gas?",
             feedback=["Lactic acid is a liquid and is the product in yoghurt, not bread.", "", "Aflatoxin is a toxin from a mould.", "Diacetyl is a flavour; it does not raise bread."]),
        QUIZ("Why does fermentation by lactic acid bacteria help preserve food?", ["It removes all water", "It lowers the pH and makes antimicrobial compounds", "It raises the temperature above 100 degrees C", "It adds oxygen"], 1,
             "Acid, bacteriocins and nutrient competition all stop other microbes.",
             hint="Think about the product.",
             feedback=["Fermentation does not dry food.", "", "Fermentation does not heat food to that level.", "LAB grow without oxygen."]),
        PQ("(a) Define fermentation. (b) Write the equation for alcoholic fermentation of glucose. (c) Calculate the mass of ethanol from 450 g glucose, assuming complete conversion (Mr: glucose 180, ethanol 46).",
           "(a) Controlled breakdown of food carbohydrates by microbes, usually in low oxygen, giving acids, alcohol, gas and flavours. (b) C6H12O6 gives 2 C2H5OH + 2 CO2. (c) 450/180 = 2.5 mol; ethanol = 5.0 mol × 46 = 230 g."),
        PQ("Explain how yoghurt is made and why it keeps longer than fresh milk.",
           "Milk is heated, cooled to about the warm temperature of the culture and Lactobacillus bulgaricus and Streptococcus thermophilus are added. They ferment lactose to lactic acid. The pH falls, the casein coagulates to give a gel and flavour compounds form. The low pH and the competition stop most spoilage and pathogenic bacteria, so it keeps longer (refrigeration still needed)."),
        PQ("Discuss the benefits and the risks of a traditional spontaneous fermentation such as palm wine or fermented cassava.",
           "Benefits: low cost, acids preserve, flavour, improved nutrition and detoxification (cassava). Risks: no control of which microbes grow, contamination from water or utensils, variation in quality, possible spoilage organisms or toxins if conditions are wrong, ethanol content in palm wine. Control by clean equipment, safe water, sound raw material and, where possible, starter cultures."),
        SUM("Fermentation uses controlled microbial action; the main groups are lactic acid bacteria and yeasts.",
            "Homolactic: C6H12O6 gives 2 lactic acid. Alcoholic: C6H12O6 gives 2 ethanol + 2 CO2.",
            "Acid, bacteriocins and competition preserve fermented foods; nutrition, flavour and digestibility may improve.",
            "Starter cultures give control; spontaneous fermentations are cheap but variable."),
    ],
))

# ------------------------------------------------------------------ 3. Foodborne infections and intoxications
LESSONS.append(lesson(
    module=M_MIC,
    topic="Foodborne infections and intoxications",
    title="Foodborne illness: Salmonella, Staphylococcus aureus and Clostridium botulinum",
    slug="fsl2-foodborne-infections-intoxications",
    minutes=25,
    summary="The difference between foodborne infection, intoxication and toxico-infection, the main pathogens (Salmonella, Staphylococcus aureus, Clostridium botulinum and others), their sources, symptoms, and the controls that prevent outbreaks.",
    objectives=[
        "Distinguish infection, intoxication and toxico-infection with an organism for each",
        "Describe the source, symptoms, onset and control of Salmonella, Staphylococcus aureus and Clostridium botulinum",
        "Explain why heat kills some pathogens but not their spores or toxins",
        "Apply the five keys to safer food and calculate pathogen growth towards an infective dose",
    ],
    key_concepts=["Infection", "Intoxication", "Toxico-infection", "Incubation period", "Enterotoxin", "Spore", "Cross-contamination", "Infective dose"],
    blocks=[
        H("Introduction"),
        T("After a wedding in a town in the Centre Region, dozens of guests fall ill within hours. Some vomit heavily after about three hours. Others have fever and diarrhoea after a day. Another group of cases, much rarer, starts with blurred vision and weakness. The same meal caused three different diseases because three different mechanisms were at work. "
          "Understanding the mechanism tells you the cause, the time to onset, and the right control."),
        KEY("Three ways food makes people ill", "The mechanism is what the exam asks for.", cards=[
            ["Foodborne infection", "The person eats living pathogens that multiply in the gut and invade it. Onset is slower (usually many hours to days) and fever is common. Example: Salmonella."],
            ["Food intoxication", "The person eats a toxin already formed in the food by bacteria growing earlier. The bacteria need not be alive when eaten. Onset is fast (hours) and fever is usually absent. Examples: Staphylococcus aureus, Clostridium botulinum."],
            ["Toxico-infection", "The person eats many living cells that then make a toxin in the gut. Example: Clostridium perfringens."],
        ]),
        D("The **incubation period** is the time between eating contaminated food and the first symptom. The **infective dose** is the number of cells needed to cause illness; it varies with the organism and the health of the person.", title="Two terms"),
        H("Salmonella (infection)"),
        T("**Salmonella** are Gram-negative rods that live in the intestines of animals, especially poultry, pigs and reptiles. Raw eggs, poultry, meat and unwashed vegetables carry them. They are killed by proper cooking, so illness comes from undercooked food, or from cross-contamination to ready-to-eat food. "
          "Symptoms are diarrhoea, abdominal pain, fever, nausea and vomiting, usually 12 to 36 hours after eating (the range is wider: check your textbook). Typhoid is caused by a different Salmonella (S. Typhi), spread by water and food contaminated with human faeces."),
        IMG("alfsl2-growth-curve.svg", alt="Growth curve with lag, log, stationary and death phases", caption="Figure 1. Pathogens in the log phase in warm food rapidly reach an infective dose (see worked example 1)."),
        EX("Worked example 1: reaching an infective dose", intro="A cooked chicken dish carries 10 Salmonella cells when it is left to stand. Assume a generation time of 20 minutes and no lag (a pessimistic teaching model). How long does it take to reach 100 000 cells?", steps=[
            S("Number of generations", math=r"n = \log_2\!\left(\frac{100\,000}{10}\right) = \log_2 10^{4} = 13.3"),
            S("Time", math=r"13.3 \times 20 = 266 \text{ min} \approx 4.4 \text{ hours}", text="Food left out for half a day easily reaches this number. Keeping food hot (above 60 degrees C) or cold stops it."),
        ]),
        H("Staphylococcus aureus (intoxication)"),
        T("**Staphylococcus aureus** lives on the skin, in noses, and in cuts and boils of food handlers. If it gets into food that is then left warm, it multiplies and releases **enterotoxins**. These toxins are **heat stable**: they survive boiling for the time of normal cooking, so reheating a contaminated dish does not make it safe. "
          "Symptoms start fast, about 1 to 6 hours after eating: nausea, violent vomiting, cramps, usually with little or no fever. Recovery normally takes a day or two. Common foods are cooked meat, cream, cheese, and handled foods that are not reheated."),
        T("Control: hygienic handling (wash hands, cover cuts, do not handle food when ill), and keep prepared food hot or cold, because the toxin cannot be removed once it has formed."),
        H("Clostridium botulinum (intoxication)"),
        T("**Clostridium botulinum** is a Gram-positive, anaerobic, spore-forming rod found in soil and water. The spores are very heat resistant. In an environment with no oxygen, low acidity (pH above about 4.6), enough moisture and warmth, the spores germinate and the cells produce **botulinum neurotoxin**, one of the most poisonous substances known. "
          "It blocks nerve signals to muscles and causes paralysis, blurred vision, difficulty swallowing and breathing, and can be fatal. Onset is typically 12 to 36 hours but can be shorter or longer (check your textbook). Unlike the staphylococcal toxin, this toxin is **heat labile**: it is destroyed by boiling for about 10 minutes, which is why home-preserved foods should be boiled before eating."),
        T("Sources: inadequately processed low-acid canned foods, home-bottled vegetables, smoked or fermented fish and meat, and honey for infants under one year (spores can grow in the infant gut). Control: correct commercial canning that gives a sufficient heat treatment to destroy spores, acidity below pH 4.6, low a_w, refrigeration, and discarding swollen cans."),
        KEY("Compare the three", "A summary of the exam favourites.", cards=[
            ["Salmonella", "Type: infection. Onset 12 to 36 h. Source: poultry, eggs, meat. Killed by cooking."],
            ["Staphylococcus aureus", "Type: intoxication. Onset 1 to 6 h. Source: human skin and nose. Toxin survives cooking."],
            ["Clostridium botulinum", "Type: intoxication. Onset 12 to 36 h. Source: soil, low-acid canned food. Spores survive boiling, toxin destroyed by boiling."],
        ]),
        T("Other organisms you may meet in a textbook: **Clostridium perfringens** (toxico-infection from large pots of meat dishes cooled slowly), **Bacillus cereus** (reheated rice; an emetic toxin or a diarrhoeal toxin), **Escherichia coli** (some strains cause serious illness), **Listeria monocytogenes** (grows in the refrigerator, dangerous in pregnancy), **Campylobacter** (poultry) and **Vibrio cholerae** (contaminated water and shellfish)."),
        H("Control: five keys to safer food"),
        T("The World Health Organization teaches five keys: keep clean, separate raw and cooked, cook thoroughly, keep food at safe temperatures, and use safe water and raw materials. "
          "**Cross-contamination** is the transfer of microbes from raw food, hands or equipment to ready-to-eat food. Use separate boards and knives, wash hands with soap, cook to a core temperature of about 70 degrees C or above, cool leftovers quickly, and reheat them until steaming hot."),
        MISTAKE("Saying that reheating always makes food safe", "Reheating kills living cells but not heat-stable toxins (S. aureus, and B. cereus emetic toxin) or spores. Safety depends on stopping growth before the food is cooked and eaten."),
        MISTAKE("Confusing the toxins of S. aureus and C. botulinum", "Staphylococcal enterotoxin resists boiling and causes vomiting. Botulinum toxin is destroyed by boiling for about 10 minutes and causes paralysis. Learn the pairs, not just the names."),
        TIP("Exam link: Paper 2 (Section B, food consumption and health) and Paper 1 ask for the organism, source, symptoms and prevention, and for the difference between infection and intoxication. Write 'onset' with units, and name the type of illness."),
        QUIZ("A person has violent vomiting 3 hours after eating a cream cake handled by someone with a septic finger. What is the most likely cause?", ["Salmonella infection", "Staphylococcus aureus enterotoxin", "Clostridium botulinum neurotoxin", "Aflatoxin"], 1,
             "A short onset, vomiting without fever and a handler with a skin infection point to staphylococcal enterotoxin.",
             hint="Think about onset time and the source on the skin.",
             feedback=["Salmonella usually causes diarrhoea and fever after a longer period.", "", "Botulism causes paralysis, not violent vomiting after 3 hours.", "Aflatoxin is a mould toxin with long-term effects."]),
        QUIZ("Which is TRUE of a toxico-infection?", ["It is caused by a toxin already in the food and living cells are not needed", "Large numbers of living cells are eaten and produce toxin in the gut", "It is caused only by moulds", "It is always fatal"], 1,
             "Toxico-infection needs living cells that make toxin in the gut, as with Clostridium perfringens.",
             hint="Which part is 'infection' and which part is 'toxin'?",
             feedback=["That describes an intoxication.", "", "Toxico-infection is caused by bacteria.", "Most cases are mild."]),
        PQ("(a) Distinguish a foodborne infection from a food intoxication. (b) Name one organism for each.",
           "(a) In an infection, living pathogens eaten with the food multiply in and invade the gut; in an intoxication, a toxin already made by bacteria in the food causes the illness and the bacteria need not be alive. (b) Infection: Salmonella. Intoxication: Staphylococcus aureus or Clostridium botulinum."),
        PQ("Explain why botulism is associated with home-canned low-acid vegetables, and state two ways to prevent it.",
           "Spores in the soil survive weak heat treatments. Inside a sealed jar there is no oxygen, the pH is above about 4.6 and the water is plentiful, so spores germinate and release neurotoxin. Prevention: a pressure-cooker or adequate heat process that kills spores; acidification (pH below 4.6); boiling home-preserved food for about 10 minutes before eating (destroys the toxin); refrigeration; discard swollen cans."),
        PQ("A school canteen serves rice and sauce prepared at 7 am and kept on a table until 1 pm. Use your knowledge of microbial growth to explain how illness could occur and how it can be prevented.",
           "The food spends six hours in the danger zone at the mesophile optimum, so any bacteria that survived cooking or came from handlers multiply to reach an infective dose or produce toxins (B. cereus spores in rice, S. aureus from hands). Prevention: cook shortly before serving; keep hot above about 60 degrees C or cool quickly and refrigerate; reheat until steaming hot; wash hands; separate raw and cooked foods; discard leftovers after a safe time."),
        SUM("Infection: living pathogens eaten (Salmonella). Intoxication: preformed toxin (S. aureus, C. botulinum). Toxico-infection: toxin made in the gut (C. perfringens).",
            "S. aureus toxin resists boiling; botulinum toxin is destroyed by boiling, but its spores survive normal boiling.",
            "Onset: about 1 to 6 hours for S. aureus, 12 to 36 hours for Salmonella (typical values; check your textbook).",
            "Prevention follows the five keys: clean, separate, cook, safe temperature, safe water and materials."),
    ],
))

# ------------------------------------------------------------------ 4. Aflatoxins and mycotoxins
LESSONS.append(lesson(
    module=M_MIC,
    topic="Aflatoxins and mycotoxins",
    title="Mould poisons in stored crops: aflatoxins and other mycotoxins",
    slug="fsl2-aflatoxins-mycotoxins",
    minutes=22,
    summary="What mycotoxins are, how Aspergillus flavus makes aflatoxins in groundnuts and maize, why they matter for health and trade, and how to prevent them in the field, in drying and in storage.",
    objectives=[
        "Define mycotoxin and name the main groups with the fungi and crops involved",
        "Explain the conditions that allow Aspergillus flavus to grow and make aflatoxin",
        "Describe the health effects of aflatoxin and why cooking does not remove it",
        "Describe control measures before harvest, in drying and in storage, and the idea of limits in food",
    ],
    key_concepts=["Mycotoxin", "Aflatoxin B1", "Aspergillus flavus", "Ochratoxin A", "Fumonisin", "Water activity", "Safe moisture", "Aflatoxicosis"],
    blocks=[
        H("Introduction"),
        T("A farmer stores freshly harvested groundnuts in a bag in a warm, humid room. A few weeks later, some nuts are shrivelled, discoloured or covered with a green-yellow mould. "
          "The mould may be gone from the cooked sauce, but the poison it made is not. This poison is called aflatoxin, and it is one of the most important food safety problems in warm tropical countries."),
        D("A **mycotoxin** is a toxic secondary metabolite made by some moulds (filamentous fungi) that grow on crops and foods. Mycotoxins are not proteins: they are small, stable molecules that are not removed by washing or normal cooking.", title="Mycotoxin"),
        H("Aflatoxins"),
        T("**Aflatoxins** are made mainly by **Aspergillus flavus** and **Aspergillus parasiticus**. The main types are B1, B2, G1 and G2, named from the colour of their fluorescence under ultraviolet light (B for blue, G for green). "
          "**Aflatoxin B1** is the most poisonous and is classified by the International Agency for Research on Cancer as a human carcinogen. In the cow, aflatoxin B1 in feed is converted to aflatoxin M1, which can appear in milk."),
        KEY("Where aflatoxin is found", "Crops that mould easily in warm, humid places.", cards=[
            ["Cereals and oilseeds", "Groundnuts and maize are the best-known examples. Cottonseed, tree nuts, some spices and dried foods are also reported."],
            ["Products", "Groundnut paste and sauces, maize flour and milled products, animal feeds, and milk from animals eating contaminated feed."],
            ["Conditions", "Warm temperature (about 25 to 35 degrees C), high humidity, grain moisture above the safe level, insect damage, drought stress before harvest, damaged shells and slow drying."],
        ]),
        T("Water is the key. Moulds can grow when the water activity of the stored crop is above about 0.70 to 0.80 (check your textbook). Safe storage moisture for grain is usually around 13 to 14 percent for maize and lower for groundnuts; teachers and the Board's practical manual give the figures to use. "
          "Contamination can start in the **field** (a drought-stressed plant is more easily invaded, insects and cracks open the way) and increases after harvest if drying is slow or storage is damp."),
        H("Health effects"),
        KEY("What aflatoxin does", "Effects depend on dose and time.", cards=[
            ["Acute aflatoxicosis", "A very large dose causes liver failure, with vomiting, jaundice and sometimes death. Outbreaks have been recorded from badly contaminated maize in Africa."],
            ["Chronic exposure", "Small amounts over years damage the liver and raise the risk of liver cancer, especially in people also infected with hepatitis B."],
            ["Other concerns", "Studies link chronic exposure to poor growth in children and to weakened immunity; research continues and the strength of the evidence is debated (check your textbook)."],
            ["Animals and trade", "Contaminated feed harms livestock and puts toxin in milk. Exports of groundnuts, maize, cocoa and coffee can be rejected if they exceed the legal limits of the importing country."],
        ]),
        T("Aflatoxins are very stable. They survive roasting, boiling and frying with only a limited reduction, so the only effective approach is to prevent their formation and to remove contaminated grain before it is eaten. Because there is no entirely safe level for a carcinogen, rules set **maximum limits** in micrograms per kilogram of food (µg/kg). Limits differ between countries and for different foods: check the current rules of the Cameroon standards body ANOR and of the importing countries."),
        EX("Worked example 1: exposure", intro="A maize meal sample contains 12 µg/kg of total aflatoxin (a figure invented for practice). A child eats 200 g of the meal in a day. How much aflatoxin does the child take in?", steps=[
            S("Convert the mass", math=r"200 \text{ g} = 0.200 \text{ kg}"),
            S("Multiply", math=r"12 \mu\text{g/kg} \times 0.200 \text{ kg} = 2.4 \mu\text{g}", text="Small as it looks, this repeated daily over years is the chronic exposure that is of concern, especially for a small child."),
        ]),
        EX("Worked example 2: sorting", intro="A lot of 40 kg of groundnuts contains 2 kg of visibly mouldy or shrivelled nuts that are removed by hand sorting. What percentage is removed, and why is the rest not automatically safe? (Teaching figures.)", steps=[
            S("Percentage removed", math=r"\frac{2}{40} \times 100 = 5\%"),
            S("Explain the rest", text="Toxin can be present in nuts that look normal, and it is concentrated in a few badly contaminated nuts. Sorting removes much of the toxin, but the lot should still be tested or the nuts should come from a reliable stored source."),
        ]),
        H("Other mycotoxins"),
        KEY("Other important mycotoxins", "Learn one organism and one food for each.", cards=[
            ["Ochratoxin A", "Aspergillus ochraceus and Penicillium species. Found in stored cereals, coffee, cocoa and dried fruits. Harms the kidney."],
            ["Fumonisins", "Fusarium species. Found mainly in maize. Linked to disease in animals and to oesophageal cancer in humans."],
            ["Patulin", "Penicillium expansum. Found in rotten apples and apple juice."],
            ["Zearalenone and trichothecenes", "Fusarium species in cereals; affect reproduction in animals and cause vomiting and feed refusal."],
        ]),
        H("Prevention"),
        KEY("Control at three stages", "Think: field, drying, storage.", cards=[
            ["Before harvest", "Use good seed and crop rotation, irrigate in drought if possible, control insects, harvest at maturity and avoid damaging the pods and ears."],
            ["Drying", "Dry quickly to the safe moisture on clean tarpaulins or drying racks, not on bare soil; sort out mouldy, damaged and discoloured grain."],
            ["Storage", "Use clean dry stores with good ventilation and pest control, sealed or hermetic bags where available, keep off the floor, and keep humidity low. Do not feed rejected grain to livestock or reuse it in food."],
        ]),
        T("Detection uses sampling (many small portions from a lot, since toxin is unevenly spread), ultraviolet light as a screening tool, rapid test strips and ELISA kits, and HPLC in the laboratory. Biological control with non-toxin-producing strains of A. flavus is used in some African countries (check current practice)."),
        MISTAKE("Saying that cooking destroys aflatoxin", "Cooking kills living mould but not aflatoxin, which is heat stable. Answers must say 'prevent the mould growing and remove contaminated grain'."),
        MISTAKE("Confusing mycotoxin with bacterial toxin", "Mycotoxins come from moulds (fungi), not bacteria. The foods are different (grains, nuts) and the effects are long-term as well as acute."),
        TIP("Exam link: Paper 2 questions on food safety and storage can ask for conditions, effects and prevention. Paper 1 asks for the organism, the food, the heat stability and the preventive step. Always state 'moisture' or 'a_w' in the prevention."),
        QUIZ("Which fungus is the main producer of aflatoxin?", ["Saccharomyces cerevisiae", "Aspergillus flavus", "Clostridium botulinum", "Penicillium roqueforti"], 1,
             "Aspergillus flavus (with A. parasiticus) makes aflatoxins on groundnuts and maize.",
             hint="Think of the name 'afla': A. fla-vus.",
             feedback=["That is baker's yeast, used in bread.", "", "That is a bacterium that makes a neurotoxin.", "That mould is used in making blue cheese."]),
        QUIZ("Why does boiling groundnut sauce NOT make contaminated groundnuts safe?", ["The mould needs a longer time to die", "Aflatoxin is heat stable and is not destroyed by normal cooking", "Boiling increases the toxin", "Aflatoxin is a protein that cooks"], 1,
             "Aflatoxin is a small heat-stable molecule that survives normal cooking temperatures.",
             hint="What do cooks do to heat-labile toxins?",
             feedback=["Killing the mould does not remove the toxin.", "", "Cooking does not make more toxin.", "It is not a protein."]),
        PQ("(a) Name two crops commonly contaminated with aflatoxin. (b) State three conditions that favour growth of Aspergillus flavus on stored grain.",
           "(a) Groundnuts and maize (also cottonseed, tree nuts, spices). (b) High moisture (a_w above about 0.7 to 0.8), warm temperature (25 to 35 degrees C), humid storage; also insect damage and slow drying."),
        PQ("Describe the control of aflatoxin in groundnuts from harvest to storage.",
           "Harvest mature pods without damage, dry quickly to safe moisture on clean racks or tarpaulins, sort out mouldy, shrivelled and discoloured nuts, store in clean, dry, ventilated, pest-proof stores or hermetic bags off the floor, and keep humidity and temperature low. Use only sound nuts for food, never feed the rejects to animals, and test where possible."),
        PQ("Evaluate the statement: 'If aflatoxin-contaminated maize is cooked well, it is safe to eat.'",
           "The statement is false. Cooking kills mould but aflatoxin is stable at normal cooking temperatures and persists. Long-term exposure raises the risk of liver cancer and can cause acute poisoning at high doses. Safety depends on preventing mould growth, drying and sorting grain before it is cooked."),
        SUM("Mycotoxins are stable toxic compounds made by moulds on crops; aflatoxin B1 from Aspergillus flavus is a human carcinogen.",
            "Warm, humid conditions, high moisture, insect damage and drought stress favour toxin formation.",
            "Cooking does not remove aflatoxin; prevention (drying, sorting, dry storage) is the control, and legal limits are in µg/kg.",
            "Other mycotoxins: ochratoxin A, fumonisins, patulin, zearalenone."),
    ],
))

# ------------------------------------------------------------------ 5. Sensory evaluation methods
LESSONS.append(lesson(
    module=M_SEN,
    topic="Sensory evaluation methods",
    title="Judging food with the senses: difference, ranking and hedonic tests",
    slug="fsl2-sensory-evaluation-methods",
    minutes=24,
    summary="How trained and untrained panels judge appearance, aroma, flavour and texture, how to control a sensory test, and how to run and interpret triangle, duo-trio, paired comparison, ranking and hedonic tests.",
    objectives=[
        "Name the sensory attributes of food and the senses used to judge each",
        "Describe the controls needed so a sensory test is fair",
        "Choose between difference tests, ranking, scoring and hedonic (acceptance) tests",
        "Interpret triangle and duo-trio results with the chance probability, and summarise hedonic and ranking data",
    ],
    key_concepts=["Organoleptic", "Panel", "Triangle test", "Duo-trio test", "Paired comparison", "Ranking test", "Hedonic scale", "Randomisation"],
    blocks=[
        H("Introduction"),
        T("A bakery in Douala changes its recipe to use a cheaper flour. Will customers notice? Will they like it less? Instruments can measure moisture or fat, but only people can say whether a food tastes good. "
          "**Sensory evaluation** (organoleptic testing) is the scientific use of the senses of sight, smell, taste, touch and hearing to measure and interpret a food. It is used to develop new products, to check quality, to compare brands and to test the effect of a change in ingredients or processing."),
        KEY("What is judged", "Each attribute uses particular senses.", cards=[
            ["Appearance", "Sight: colour, shape, size, gloss, surface and clarity."],
            ["Aroma and flavour", "Smell (volatile compounds reach the nose) and taste (sweet, sour, salty, bitter and umami on the tongue). Flavour is smell and taste together, which is why food tastes flat when you have a blocked nose."],
            ["Texture and mouthfeel", "Touch and pressure in the mouth and on the hand: crisp, soft, tough, creamy, gritty, juicy."],
            ["Sound", "Hearing: the crunch of a biscuit or the crackle of a crisp."],
        ]),
        H("Panels"),
        T("A **trained panel** (or expert panel) has people chosen for sensitivity and trained to describe and score attributes in a consistent way. A small trained panel (about 8 to 12 people) is used for difference and descriptive tests. A **consumer panel** has untrained people who represent buyers, and gives opinions about liking. It needs many more people (often 50 or more) because individuals differ."),
        H("Controlling the test"),
        D("A sensory test must reduce **bias**, so that the result comes from the food, not from the surroundings or the order.", title="Why control matters"),
        KEY("Good practice", "Six controls to quote in an answer.", cards=[
            ["Samples", "Same size, temperature, serving dish and amount; present each sample at its normal serving temperature."],
            ["Coding", "Label with random three-digit codes, so that names or brands cannot influence the judge."],
            ["Order", "Randomise or balance the order of presentation, since the first sample is often rated differently from the last."],
            ["Palate", "Give water or plain crackers between samples. Judges should not smoke or eat strong food before the test."],
            ["Place", "Quiet, odour-free booths or separate places, with no talking so that judges do not influence each other. Coloured light may hide differences in appearance when only flavour is to be judged."],
            ["Judges", "Not ill, not hungry or just after a meal, not tired; volunteers; replicate testing on different days where possible."],
        ]),
        H("Difference tests"),
        T("A **difference test** asks whether two samples can be told apart. It does not ask which is better."),
        KEY("Common difference tests", "Chance level decides how to read the results.", cards=[
            ["Triangle test", "Three coded samples: two are the same and one is different. The judge picks the odd one. Chance of a correct guess = 1 in 3. There are 6 possible arrangements, which are shared out across the judges."],
            ["Duo-trio test", "A reference sample is given, then two coded samples, one matching the reference. The judge picks the one that matches. Chance = 1 in 2."],
            ["Paired comparison", "Two samples; the judge chooses the sweeter, the saltier or the one preferred. Chance = 1 in 2. If the question is about a given attribute it is a difference test; if it is about liking it is a preference test."],
        ]),
        T("The answer to a triangle test is read by comparing the number of correct choices with the number you would expect by chance. Statisticians use the binomial distribution; the table below shows the smallest number of correct answers that is significant at the 5 percent level for a one-sided test (the test asks whether more than chance can pick the odd sample). "
          "Your school will probably give you a table of this kind in the practical manual; use it."),
        CODE("""Judges   Triangle (chance 1/3)   Duo-trio (chance 1/2)
         correct needed          correct needed
   9            6                       8
  12            8                      10
  15            9                      12
  18           10                      13
  24           13                      17""", "text", title="Minimum correct answers for significance at 5 percent (one-sided)", caption="Values computed from the binomial distribution; check them against the table in your textbook."),
        EX("Worked example 1: triangle test", intro="A bakery trains 12 judges. In a triangle test comparing the old recipe and the new recipe, 7 judges pick the odd sample correctly. What does this show?", steps=[
            S("Chance expectation", math=r"12 \times \tfrac{1}{3} = 4 \text{ correct by guessing}"),
            S("Compare with the table", text="12 judges need 8 correct for a significant difference at 5 percent. 7 is below 8."),
            S("Conclusion", text="The panel cannot show that the new flour is detectably different. The recipe change is not noticed at this level of evidence. (Seven correct is more than the 4 expected by chance, but not enough to rule out luck.)"),
        ]),
        H("Ranking, scoring and hedonic tests"),
        T("A **ranking test** asks judges to put several samples in order of an attribute (for example sweetness) or of preference, from 1 (best) to the number of samples. Rank totals are added up; the lowest total is the most preferred (or the highest total is the most intense, depending on how the ranks were assigned). "
          "A **hedonic test** measures how much a person likes a food. The **9-point hedonic scale** runs from 1 'dislike extremely' to 9 'like extremely', with 5 as 'neither like nor dislike'. The mean score of a consumer panel is compared for different samples. "
          "A **scoring test** (rating) uses a numeric scale for the intensity of an attribute. A **descriptive test** lists and scores all the attributes of one food."),
        EX("Worked example 2: ranking", intro="Five judges rank three plantain chip samples A, B, C for crispness (1 = crispest). The ranks for A are 1, 2, 1, 1, 2; for B they are 3, 3, 2, 3, 3; for C they are 2, 1, 3, 2, 1. Find the rank totals and give the result.", steps=[
            S("Add the ranks", math=r"A = 7,\; B = 14,\; C = 9"),
            S("Interpret", text="Check: the totals add to 30, which is 5 judges times (1 + 2 + 3) = 30. A has the lowest total, so A is the crispest. Whether the difference is significant needs a rank table; with only five judges, treat the result as a guide."),
        ], check=r"7 + 14 + 9 = 30"),
        EX("Worked example 3: hedonic data", intro="Ten consumers score a new biscuit (A) and the old biscuit (B) on the 9-point scale. A: 7, 8, 6, 9, 7, 8, 7, 6, 8, 7. B: 6, 7, 5, 7, 6, 8, 6, 5, 7, 6. Find the means.", steps=[
            S("Add the scores of A", math=r"7+8+6+9+7+8+7+6+8+7 = 73 \Rightarrow \bar{x}_A = 7.3"),
            S("Add the scores of B", math=r"6+7+5+7+6+8+6+5+7+6 = 63 \Rightarrow \bar{x}_B = 6.3"),
            S("Conclude", text="A is 'liked moderately' on average (7 is 'like moderately'), and one mark higher than B. A statistical test would show whether this is significant; in an exam say the sample and the scale."),
        ]),
        MISTAKE("Using a difference test to answer a preference question", "A triangle test says whether people can tell two foods apart, not which they prefer. Preference needs a hedonic or paired preference test."),
        MISTAKE("Forgetting the controls", "Examiners expect coded samples, random order, palate cleansing and separation of judges. Writing 'taste them' without controls earns very little."),
        TIP("Exam link: Paper 1 asks for the right test for a purpose and the chance levels. Paper 2 (food science, quality) may ask you to describe how you would design a test. Paper 3 may ask you to run a triangle or a ranking test with your own panel."),
        QUIZ("In a triangle test, what is the probability that a judge picks the odd sample by chance alone?", ["1/2", "1/3", "1/6", "1/9"], 1,
             "There are three samples and one is the odd one, so the chance is 1 in 3.",
             hint="How many samples does the judge choose among?",
             feedback=["That is the chance in a duo-trio or paired test.", "", "There are 6 arrangements of the three samples, but the judge still chooses one out of three.", "This is not a probability for this task."]),
        QUIZ("Why are samples given random three-digit codes?", ["To save space on the label", "So that names, brands or position do not influence the judges", "To make the food keep longer", "To show the sample is cooked"], 1,
             "Coding removes bias caused by known names or labels.",
             hint="Think about prejudice about a famous brand.",
             feedback=["The reason is scientific, not space.", "", "Codes have no effect on keeping quality.", "Codes say nothing about cooking."]),
        PQ("(a) Name three controls in a sensory test. (b) State the difference between a triangle test and a hedonic test.",
           "(a) Coded samples; randomised order; water or plain cracker between samples; separate booths with no talking; equal portions at the same temperature. (b) A triangle test finds out whether two products can be distinguished (difference test), using three samples; a hedonic test measures how much consumers like a product on a scale."),
        PQ("In a duo-trio test with 15 judges, 11 identify the sample that matches the reference. Using the table, what is your conclusion?",
           "15 judges need 12 correct for significance at 5 percent. 11 is below the minimum, so the evidence is not enough to say that the two samples are different. (11 out of 15 is more than the 7.5 expected by chance, but not enough to rule out luck.)"),
        PQ("A company wants to know which of three new drinks teenagers like best. Describe a suitable sensory test and the controls you would use.",
           "Use a consumer panel of untrained teenagers (50 or more) and a hedonic test on a 9-point scale, possibly with a ranking of the three drinks. Serve equal portions at the same temperature in identical cups with random three-digit codes, rotate the order across judges, give water between samples, keep judges apart, and compare the mean scores or rank totals. A statistical test is needed to say whether the differences are real."),
        SUM("Sensory evaluation uses sight, smell, taste, touch and hearing to measure appearance, aroma, flavour and texture.",
            "Controls: coded samples, random order, equal portions, palate cleansing, separate judges.",
            "Difference tests: triangle (chance 1/3), duo-trio (1/2) and paired comparison; hedonic tests measure liking; ranking orders samples.",
            "Compare correct answers with the number needed for significance; compare mean hedonic scores or rank totals."),
    ],
))

# ------------------------------------------------------------------ 6. Proximate analysis
LESSONS.append(lesson(
    module=M_SEN,
    topic="Proximate analysis",
    title="Proximate analysis: moisture, ash, protein (Kjeldahl), fat (Soxhlet), fibre and carbohydrate",
    slug="fsl2-proximate-analysis",
    minutes=25,
    summary="The six proximate components of a food, how each is determined (including Kjeldahl nitrogen and Soxhlet fat extraction), the calculations and how proximate results give an energy value.",
    objectives=[
        "List the proximate components and the principle of each method",
        "Explain the steps of the Kjeldahl method and calculate protein from a titration",
        "Explain Soxhlet extraction and calculate fat content",
        "Calculate carbohydrate by difference and energy value with Atwater factors, and state the limits of proximate analysis",
    ],
    key_concepts=["Proximate analysis", "Kjeldahl method", "Nitrogen factor", "Crude protein", "Soxhlet extraction", "Ash", "Crude fibre", "Carbohydrate by difference", "Atwater factors"],
    blocks=[
        H("Introduction"),
        T("A school in Buea wants to know how much protein and fat is in a locally made groundnut flour. A food composition table gives average values, but a sample from this producer may differ. Chemical analysis gives the answer. "
          "The Board's report asks candidates to know how to use the food composition table (FCT) supplied by the Board and warns that this is often poorly done. In this lesson you learn how the table values are obtained."),
        D("**Proximate analysis** (the Weende scheme) divides a food into six groups of components that are measured by simple, standard methods: **moisture, ash, crude protein, crude fat (ether extract), crude fibre** and **nitrogen-free extract (carbohydrate by difference)**. 'Crude' means the group is measured by a method that is not perfectly specific.", title="Proximate analysis"),
        KEY("The six components", "Principle of each method.", cards=[
            ["Moisture", "Dry the sample at about 105 degrees C to constant mass; loss in mass is water (next lesson)."],
            ["Ash", "Burn the dry sample in a furnace at about 550 degrees C until only white or grey mineral residue remains. Ash is a measure of total minerals."],
            ["Crude protein", "Kjeldahl method: total nitrogen is measured, and multiplied by a factor."],
            ["Crude fat", "Soxhlet extraction with a non-polar solvent (petroleum ether or hexane); the mass of fat removed is weighed after the solvent evaporates."],
            ["Crude fibre", "Boil the fat-free sample in dilute acid then dilute alkali; the insoluble residue is dried, weighed, ashed and the loss gives fibre."],
            ["Carbohydrate (NFE)", "Calculated by difference: 100 minus the sum of moisture, ash, protein, fat and fibre."],
        ]),
        H("The Kjeldahl method for protein"),
        IMG("alfsl2-kjeldahl-flow.svg", alt="Four boxes in a row: digest, distil, titrate and calculate", caption="Figure 1. The four stages of the Kjeldahl method."),
        T("**Digestion**: the sample is heated with concentrated sulphuric acid and a catalyst (for example a copper or selenium salt and potassium sulphate to raise the boiling point). The organic nitrogen becomes ammonium sulphate. "
          "**Distillation**: excess sodium hydroxide is added to the digest and the mixture is heated; ammonia is released and carried into receiving boric acid. "
          "**Titration**: the ammonia in the boric acid forms borate, which is titrated with standard hydrochloric acid to the end point. A **blank** (no sample) is also run and its titre is subtracted."),
        F(r"\%\,N = \frac{(V_{\text{sample}} - V_{\text{blank}}) \times M_{\text{HCl}} \times 14.007}{\text{mass of sample (g)} \times 1000} \times 100", title="Percentage nitrogen"),
        F(r"\text{crude protein (\%)} = \%\,N \times F", title="Protein from nitrogen"),
        T("Proteins contain about 16 percent nitrogen, which gives the common **nitrogen factor** F = 100/16 = 6.25. Some foods use other factors (for example 5.7 for wheat and 6.38 for milk; check your textbook for the factors you must use). "
          "Kjeldahl measures **total nitrogen**, so non-protein nitrogen (urea, free amino acids, some vitamins) is counted too. This is why the result is called 'crude' protein."),
        EX("Worked example 1: Kjeldahl calculation", intro="A 1.000 g sample of a food is digested and distilled. The titre of 0.100 M HCl is 12.40 cm³ and the blank titre is 0.40 cm³. Calculate the percentage nitrogen and the crude protein (F = 6.25).", steps=[
            S("Corrected titre", math=r"12.40 - 0.40 = 12.00 \text{ cm}^3"),
            S("Moles of HCl, which equal moles of N", math=r"\frac{12.00 \times 0.100}{1000} = 1.200 \times 10^{-3} \text{ mol}"),
            S("Mass of nitrogen", math=r"1.200 \times 10^{-3} \times 14.007 = 0.01681 \text{ g}"),
            S("Percentage nitrogen", math=r"\frac{0.01681}{1.000} \times 100 = 1.68\%"),
            S("Crude protein", math=r"1.68 \times 6.25 = 10.5\%"),
        ]),
        H("Soxhlet extraction for fat"),
        T("A dried, weighed sample is placed in a porous **thimble** in the Soxhlet apparatus. Solvent boils in a flask, condenses above the sample, floods the thimble and siphons back, again and again, carrying fat into the flask. After several hours the solvent is evaporated, and the flask containing the fat is dried and weighed again. "
          "The solvent is flammable: heat with a water bath or an electric mantle, never a naked flame, and work in a ventilated place."),
        F(r"\text{crude fat (\%)} = \frac{\text{mass of flask with fat} - \text{mass of empty flask}}{\text{mass of sample}} \times 100", title="Fat content"),
        EX("Worked example 2: fat and carbohydrate by difference", intro="A 2.500 g sample gives an empty flask mass of 77.9900 g and a flask mass of 78.4300 g after extraction. The other results per 100 g of the sample are moisture 12.0, ash 3.5, protein 9.2 and fibre 2.8. Calculate the fat content and the carbohydrate (NFE) by difference.", steps=[
            S("Mass of fat", math=r"78.4300 - 77.9900 = 0.4400 \text{ g}"),
            S("Percentage fat", math=r"\frac{0.4400}{2.500} \times 100 = 17.6\%"),
            S("Add the other components", math=r"12.0 + 3.5 + 9.2 + 17.6 + 2.8 = 45.1\%"),
            S("Carbohydrate (NFE)", math=r"100 - 45.1 = 54.9\%", text="Errors in any other component add up in the carbohydrate value, which is why it is only an estimate."),
        ]),
        H("Fibre, ash and energy"),
        T("Crude fibre is the part of the plant cell wall that is not dissolved by hot dilute acid and alkali. It underestimates dietary fibre, since some soluble fibre is lost, so modern work uses dietary fibre methods; the Weende value is still used in school. "
          "**Ash** is a total mineral measure; individual minerals need further methods."),
        T("The energy value is calculated from the results with **Atwater factors**: about 17 kJ per gram for protein, 37 kJ for fat and 17 kJ for carbohydrate (4, 9 and 4 kilocalories per gram). Fibre, ash and water give no energy in the simple school calculation."),
        EX("Worked example 3: energy", intro="A food contains 13 g protein, 5 g fat and 70 g carbohydrate per 100 g. Calculate its energy value in kJ and kcal per 100 g.", steps=[
            S("Energy in kJ", math=r"13 \times 17 + 5 \times 37 + 70 \times 17 = 221 + 185 + 1190 = 1596 \text{ kJ}"),
            S("Energy in kcal", math=r"13 \times 4 + 5 \times 9 + 70 \times 4 = 52 + 45 + 280 = 377 \text{ kcal}"),
        ]),
        MISTAKE("Forgetting the blank titration", "The blank is subtracted from the sample titre. Leaving it out makes the nitrogen too high."),
        MISTAKE("Calling Kjeldahl protein exact", "Kjeldahl measures nitrogen, not protein. The factor and the non-protein nitrogen make the result an estimate. Use 'crude protein' in answers."),
        TIP("Exam link: the Board's report says candidates struggle with calculations involving the food composition table and with food composition in general. Practise: use per 100 g values from the table supplied by your teacher, then scale to the portion. Paper 1 asks for method principles; Paper 3 may include a calculation."),
        QUIZ("What is the purpose of concentrated sulphuric acid in the Kjeldahl digestion?", ["To extract the fat", "To convert organic nitrogen to ammonium sulphate", "To neutralise the ammonia in the receiver", "To dissolve the fibre"], 1,
             "The hot concentrated acid breaks down the organic matter and traps the nitrogen as ammonium sulphate.",
             hint="Which step comes first and what happens to nitrogen?",
             feedback=["Fat is extracted by a solvent, in a different method.", "", "Boric acid receives the ammonia in distillation.", "Fibre is a separate method with dilute acid and alkali."]),
        QUIZ("A food has 2.0 percent nitrogen. Using the usual factor, what is its crude protein?", ["8.0 percent", "10.0 percent", "12.5 percent", "16.0 percent"], 2,
             "2.0 × 6.25 = 12.5 percent.",
             hint="The usual factor is 100 divided by 16.",
             feedback=["That uses a factor of 4.", "That uses a factor of 5.", "", "16 is the percentage of nitrogen in protein, not the factor."]),
        PQ("In a Kjeldahl test 0.500 g of a sample needs 18.60 cm³ of 0.100 M HCl and the blank needs 0.20 cm³. Calculate the percentage nitrogen and the crude protein with a factor of 6.25.",
           "Corrected titre 18.40 cm³. Moles N = 18.40 × 0.100 / 1000 = 1.840 × 10^-3 mol. Mass N = 1.840 × 10^-3 × 14.007 = 0.02577 g. %N = 0.02577/0.500 × 100 = 5.15 percent. Protein = 5.15 × 6.25 = 32.2 percent."),
        PQ("Describe how the fat content of a dried food is determined by Soxhlet extraction.",
           "Weigh a dried sample in a thimble and a clean dry flask. Boil petroleum ether in the flask; the vapour condenses and floods the thimble, dissolving fat, then siphons back to the flask. Repeat for several hours. Evaporate the solvent, dry the flask and weigh it. Fat percentage = increase in flask mass divided by sample mass times 100. Use a water bath, not a naked flame."),
        PQ("Explain why 'carbohydrate by difference' is only an estimate and give the value for a food with moisture 10.0, ash 2.0, protein 12.0, fat 3.0 and fibre 3.0 percent.",
           "It is found by subtracting every other measured component from 100, so all errors and the non-protein or unmeasured components are included in the result. NFE = 100 − (10.0 + 2.0 + 12.0 + 3.0 + 3.0) = 70.0 percent."),
        SUM("Proximate analysis measures moisture, ash, crude protein, crude fat, crude fibre and carbohydrate (by difference).",
            "Kjeldahl: digest, distil into boric acid, titrate with standard acid, subtract the blank; protein = %N × 6.25 (or the correct factor).",
            "Soxhlet: solvent extracts fat; fat % = mass of fat ÷ mass of sample × 100.",
            "Energy: 17, 37 and 17 kJ per gram for protein, fat and carbohydrate; all values are estimates, and the FCT gives averages."),
    ],
))

# ------------------------------------------------------------------ 7. Titratable acidity and moisture determination
LESSONS.append(lesson(
    module=M_SEN,
    topic="Titratable acidity and moisture determination",
    title="Measuring acidity and moisture: titration, oven drying and Karl Fischer",
    slug="fsl2-titratable-acidity-moisture",
    minutes=23,
    summary="How titratable acidity is found by titration with sodium hydroxide and expressed as a percentage of a named acid, how it differs from pH, and how moisture is measured by oven drying and by Karl Fischer titration.",
    objectives=[
        "Explain titratable acidity and how it differs from pH",
        "Calculate titratable acidity as percent of citric, malic, tartaric or lactic acid",
        "Describe moisture determination by oven drying and calculate wet-basis moisture and dry matter",
        "Explain the principle of Karl Fischer titration and when it is preferred to drying",
    ],
    key_concepts=["Titratable acidity", "End point", "Phenolphthalein", "Equivalent mass", "Oven drying", "Constant mass", "Moisture content", "Karl Fischer titration"],
    blocks=[
        H("Introduction"),
        T("Two fruit juices may both have a pH of 3.5, yet one tastes much sharper. A dairy buying milk must know whether it is already souring. A baker needs flour that is dry enough to store. "
          "The first question is about acidity and the second about water. Both are measured by simple laboratory methods that a school laboratory can carry out."),
        H("Titratable acidity"),
        D("**pH** measures the concentration of free hydrogen ions at the moment of measurement. **Titratable acidity (TA)** measures the total amount of acid present, both free and not yet dissociated, by titrating with a standard alkali to a fixed end point (usually about pH 8.2, the colour change of phenolphthalein).", title="pH and titratable acidity"),
        T("Weak acids in foods (citric, malic, tartaric, lactic and acetic) dissociate only partly, so the pH does not tell how much acid is present. As the alkali neutralises the free hydrogen ions, more molecules dissociate and are also neutralised, until all the acid is used up. "
          "That is why TA correlates better with sourness than pH does. Buffering by proteins and salts also changes the relation between pH and TA."),
        T("Result: TA is reported as grams of the **predominant acid** per 100 cm³ (or per 100 g) of the sample. The predominant acid depends on the food: citric acid in citrus fruits, malic in apples, tartaric in grapes, lactic in milk and fermented products, acetic in vinegar. "
          "Divide the molar mass by the number of acidic hydrogens (basicity) to get the **equivalent mass**."),
        CODE("""Acid       Formula     Mr      Acidic H   Equivalent mass
Citric     C6H8O7     192.12      3          64.04
Malic      C4H6O5     134.09      2          67.04
Tartaric   C4H6O6     150.09      2          75.04
Lactic     C3H6O3      90.08      1          90.08
Acetic     C2H4O2      60.05      1          60.05""", "text", title="Acids used to express acidity"),
        F(r"\text{TA (g per 100 cm}^3\text{)} = \frac{V_{\text{NaOH}} \times M_{\text{NaOH}} \times E}{1000 \times V_{\text{sample}}} \times 100", title="Titratable acidity"),
        T("In the formula, V is the titre in cm³, M is the molarity of the NaOH, E is the equivalent mass of the named acid and V of the sample is the volume titrated. Procedure: pipette the sample (diluted if it is dark or very acid), add a few drops of phenolphthalein, titrate with standard 0.1 M NaOH from the burette to the first permanent faint pink, and repeat until two titres agree (concordant). Coloured juices may need a pH meter to find pH 8.2."),
        EX("Worked example 1: orange juice", intro="25.0 cm³ of orange juice needs 14.2 cm³ of 0.100 M NaOH to reach the end point. Express the acidity as citric acid (E = 64.04).", steps=[
            S("Moles of NaOH", math=r"\frac{14.2 \times 0.100}{1000} = 1.42 \times 10^{-3} \text{ mol}"),
            S("Mass of acid", math=r"1.42 \times 10^{-3} \times 64.04 = 0.0909 \text{ g}"),
            S("Per 100 cm³", math=r"\frac{0.0909}{25.0} \times 100 = 0.364 \text{ g per 100 cm}^3", text="So the juice contains about 0.36 percent citric acid."),
        ], check=r"\frac{14.2 \times 0.1 \times 64.04}{1000 \times 25} \times 100 = 0.364"),
        EX("Worked example 2: milk", intro="10.0 cm³ of fresh milk needs 1.60 cm³ of 0.100 M NaOH. Express the acidity as lactic acid (E = 90.08).", steps=[
            S("Moles of NaOH", math=r"\frac{1.60 \times 0.100}{1000} = 1.60 \times 10^{-4} \text{ mol}"),
            S("Mass of lactic acid", math=r"1.60 \times 10^{-4} \times 90.08 = 0.01441 \text{ g}"),
            S("Per 100 cm³", math=r"\frac{0.01441}{10.0} \times 100 = 0.144\%", text="Fresh milk has a small natural acidity from proteins and phosphates (commonly about 0.13 to 0.17 percent as lactic acid; check your textbook). A higher value suggests bacterial souring."),
        ]),
        H("Moisture content"),
        D("**Moisture content** is the mass of water in a food as a percentage of the mass of the food (the wet basis). **Dry matter** is what is left after the water is removed.", title="Moisture content"),
        T("**Oven drying**: weigh about 5 g of sample in a dish, heat in an oven at about 105 degrees C, cool in a desiccator and weigh; repeat until the mass is constant (two weighings within a small tolerance). Always cool in a desiccator so that the dried sample does not take up moisture again. "
          "Foods rich in sugar or fat, or containing volatile compounds, can lose other volatiles or can burn or oxidise, so a vacuum oven at a lower temperature may be used."),
        F(r"\text{moisture (\%)} = \frac{\text{mass lost on drying}}{\text{mass of sample}} \times 100 \qquad \text{dry matter (\%)} = 100 - \text{moisture}", title="Wet-basis moisture"),
        EX("Worked example 3: oven drying", intro="A 5.00 g sample of grain is heated to constant mass and weighs 3.80 g after drying. Calculate the moisture and dry matter.", steps=[
            S("Mass lost", math=r"5.00 - 3.80 = 1.20 \text{ g}"),
            S("Moisture", math=r"\frac{1.20}{5.00} \times 100 = 24.0\%"),
            S("Dry matter", math=r"100 - 24.0 = 76.0\%", text="On a dry-basis the water is 1.20/3.80 = 31.6 percent of the dry mass. Wet basis (24.0 percent) is the usual way of reporting."),
        ]),
        H("Karl Fischer titration"),
        T("The **Karl Fischer (KF) titration** is a chemical method specific to water. The reagent contains iodine, sulphur dioxide, a base and an alcohol. Iodine is used up in a reaction that needs exactly one molecule of water per molecule of iodine. When all the water is used, excess iodine is detected electrically at the end point. "
          "The reagent is first standardised against a known mass of water to get its **water equivalence factor** (mg of water per cm³ of reagent)."),
        F(r"\text{water (mg)} = V_{\text{KF}} \times F \qquad F = \frac{\text{mass of water standard (mg)}}{V_{\text{standard}}}", title="Karl Fischer"),
        EX("Worked example 4: Karl Fischer", intro="25.0 mg of pure water takes 5.00 cm³ of KF reagent. A 500 mg sample of dried powder takes 3.20 cm³. Find the water content.", steps=[
            S("Water equivalence factor", math=r"F = \frac{25.0}{5.00} = 5.00 \text{ mg cm}^{-3}"),
            S("Water in the sample", math=r"3.20 \times 5.00 = 16.0 \text{ mg}"),
            S("Percentage", math=r"\frac{16.0}{500} \times 100 = 3.2\%"),
        ]),
        T("KF is preferred for foods with very little water (powders, oils, chocolate, dried fruit and sugars), for foods that decompose or lose other volatiles when heated, and when high accuracy is needed. Its limits are the cost of reagents, the need to exclude air moisture and the difficulty of releasing water from some solids (a solvent or heating may be needed). Moisture can also be measured by distillation with toluene and by rapid infrared moisture balances."),
        MISTAKE("Saying TA and pH are the same", "pH is the activity of free hydrogen ions now; TA is the total acid that neutralises a base. A buffered food can have a high TA and a moderate pH. Use both words correctly."),
        MISTAKE("Not cooling in a desiccator", "A hot dry sample takes up water from the air, so the mass is too high and the moisture too low. Cool in a desiccator and weigh quickly."),
        TIP("Exam link: Paper 1 asks for the principle of each method; Paper 2 may ask for the use of these tests in quality control; Paper 3 may give titration or drying data. State the acid in your answer, the units, and the working."),
        QUIZ("Why is phenolphthalein used for titratable acidity of a food?", ["It turns pink near pH 8.2, the end point for a weak acid titrated with NaOH", "It turns pink in acid", "It measures moisture", "It removes colour from the sample"], 0,
             "The pink end point (about pH 8.2) marks complete neutralisation of weak food acids.",
             hint="What is the pH at the equivalence point of a weak acid and a strong base?",
             feedback=["", "In acid, phenolphthalein is colourless.", "Moisture is measured by drying or KF.", "It is an indicator, not a bleach."]),
        QUIZ("A sample loses 0.90 g on drying from 6.00 g. What is its wet-basis moisture content?", ["10 percent", "15 percent", "18 percent", "85 percent"], 1,
             "0.90/6.00 × 100 = 15 percent.",
             hint="Divide the mass lost by the original mass.",
             feedback=["That divides by 9, not by 6.", "", "That divides by the dry mass 5.10.", "That is the dry matter."]),
        PQ("20.0 cm³ of apple juice needs 11.8 cm³ of 0.100 M NaOH. Calculate the acidity as malic acid (E = 67.04), in g per 100 cm³.",
           "Moles NaOH = 11.8 × 0.100/1000 = 1.18 × 10^-3. Mass = 1.18 × 10^-3 × 67.04 = 0.0791 g. Per 100 cm³ = 0.0791/20.0 × 100 = 0.395 g, about 0.40 g per 100 cm³."),
        PQ("Describe how you would find the moisture content of maize flour by oven drying and give two precautions.",
           "Weigh a clean, dry dish; add about 5 g of flour and weigh; dry at about 105 degrees C; cool in a desiccator; weigh; repeat drying until the mass is constant. Moisture % = mass lost ÷ sample mass × 100. Precautions: cool in a desiccator, handle with tongs, avoid overheating, and weigh quickly."),
        PQ("State two reasons why the Karl Fischer method may be chosen to find the moisture of chocolate powder instead of oven drying.",
           "Oven drying can also remove other volatile substances and the fat and sugar may change at 105 degrees C, so the loss is not only water. KF reacts only with water, is accurate at low moisture, and can be done on small samples without heating."),
        SUM("pH measures free hydrogen ions; titratable acidity measures total acid by titration to about pH 8.2.",
            "TA = V × M × E ÷ (1000 × sample volume) × 100, expressed as the predominant acid.",
            "Moisture by oven drying: loss on drying to constant mass, cooled in a desiccator; dry matter = 100 − moisture.",
            "Karl Fischer is a specific titration for water, used for dry or heat-sensitive foods."),
    ],
))

# ------------------------------------------------------------------ 8-10. Examination
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: multiple-choice strategy across the whole syllabus",
    slug="fsl2-paper1-multiple-choice",
    minutes=20,
    summary="How to approach the 50 multiple-choice questions of Paper 1, covering the whole syllabus: planning time, reading stems, eliminating distractors, handling calculations and revising by module.",
    objectives=[
        "State the structure and weighting of Paper 1 from the Board's 2023 report",
        "Use a step-by-step method for reading a stem, predicting the answer and eliminating options",
        "Recognise typical distractors in food science and nutrition questions",
        "Plan time and revision across the five Lower Sixth modules",
    ],
    key_concepts=["Paper 1", "Stem", "Distractor", "Elimination", "Time per question", "Revision by module", "Calculation questions"],
    blocks=[
        H("What the paper is"),
        D("According to the Board's 2023 Advanced Level report, Paper 1 for Food Science and Nutrition (0740) has **50 multiple-choice questions**, carries **35 percent** of the examination and lasts **1 hour 30 minutes**. It is marked electronically and covers the **entire syllabus**.", title="Paper 1 in the Board's report"),
        T("The report says that the table of specification gave about 15 questions to knowledge and comprehension, 15 to application, 10 to analysis and 10 to synthesis and evaluation. These are the figures in the report; the balance may change between years, so treat them as a guide. "
          "That means that only about a third of Paper 1 is recall. The rest asks you to apply a rule to a case, read data or reason. Because Paper 1 covers the whole syllabus, a gap in one module costs marks that cannot be recovered by essay skill."),
        T("The platform's Paper 1 mock exam A for this course has 50 questions across the five Lower Sixth modules and gives you 90 minutes. That timing is a KKEVO practice setting, which is the same length as the real paper. It gives an average of 1.8 minutes a question."),
        H("A method for each question"),
        KEY("Read, predict, eliminate, check", "Four habits that raise scores.", cards=[
            ["Read the stem first", "Cover the options. Underline the key words: 'which', 'NOT', 'best', 'most likely', 'first'. Many errors come from missing a negative."],
            ["Predict an answer", "Decide what the answer should be before looking at the options, so a clever wrong option cannot lead you."],
            ["Eliminate", "Cross out options that are wrong and say why. If two options are similar, look for the one word that makes one of them false."],
            ["Check units and sense", "In calculation questions check the unit, the power of ten, and whether the answer is realistic (a protein value above 100 percent is impossible)."],
        ]),
        H("Common distractors in this subject"),
        KEY("Typical wrong options", "Name the trap so you can avoid it.", cards=[
            ["Opposite effect", "For example 'a lower a_w increases microbial growth'. Check the direction of change."],
            ["Right fact, wrong question", "A true statement about glucose when the question asks about fructose, or about the infection when the stem asks about the toxin."],
            ["Confusable pairs", "Infection versus intoxication; pH versus titratable acidity; Maillard browning versus enzymatic browning; HBV versus LBV protein; denaturation versus coagulation; food fad, taboo and fallacy."],
            ["Unfinished calculation", "The option equal to the value before the last step, such as nitrogen percentage instead of protein percentage."],
            ["Absolute words", "'Always' and 'never' are often wrong in biology and food science, but not every time. Judge the content."],
        ]),
        H("Calculation questions"),
        T("Calculation questions are usually short: generation numbers, energy from composition, nitrogen to protein, percentage moisture, titratable acidity, BMR or energy requirements. Write the formula, put in numbers with units, and compute once. If the numbers are awkward, round at the end."),
        EX("Worked example 1: a calculation question", intro="A food contains 20 g protein, 10 g fat and 50 g carbohydrate per 100 g. Using 17, 37 and 17 kJ per gram, what is its energy per 100 g?", steps=[
            S("Protein", math=r"20 \times 17 = 340 \text{ kJ}"),
            S("Fat", math=r"10 \times 37 = 370 \text{ kJ}"),
            S("Carbohydrate", math=r"50 \times 17 = 850 \text{ kJ}"),
            S("Total", math=r"340 + 370 + 850 = 1560 \text{ kJ}", text="Distractors would be 340 (protein only), 1190 (forgetting the fat factor of 37), or 1710 (using 17 for fat as well)."),
        ]),
        EX("Worked example 2: elimination", intro="Which of the following food poisoning bacteria forms a toxin that is destroyed by boiling for 10 minutes? A Staphylococcus aureus  B Clostridium botulinum  C Salmonella  D Bacillus cereus emetic toxin.", steps=[
            S("Predict", text="The heat-labile toxin is the botulinum neurotoxin."),
            S("Eliminate", text="A: the S. aureus enterotoxin survives boiling. C: Salmonella causes infection, not a preformed toxin. D: the emetic toxin is heat stable."),
            S("Choose", text="B is correct."),
        ]),
        H("Timing and revision"),
        T("Aim for 1 minute on easy recall questions and up to 3 minutes on a calculation. Mark an answer, leave a very hard question and come back; never leave a blank, since there is no penalty to guessing in most multiple-choice papers (check the instructions on your paper). "
          "In the last 5 minutes, check that each answer is on the correct line."),
        T("Revise by module. For the five Lower Sixth modules use the mock to find the weak one: macronutrient chemistry, micronutrients and pigments, physiology and energy, microbiology and food safety, sensory evaluation and analysis. Then use the lesson and set for that topic."),
        MISTAKE("Spending too long on one question", "A single hard question can cost the time of three easy ones. Mark a best guess and move on."),
        MISTAKE("Answering the question you expected", "The stem may ask for 'NOT' or for 'the first step'. Read the whole stem again before choosing."),
        TIP("Exam link: the report says candidates must follow the instructions. Fill in the answer sheet exactly as told, one answer per question."),
        QUIZ("A multiple-choice question has two options that look nearly the same. What is the best next step?", ["Choose the longer one", "Look for the single word or number that makes one of them false", "Skip every such question", "Choose the first one"], 1,
             "The difference between two similar options is the part that tests whether you know the fact.",
             hint="Compare them word by word.",
             feedback=["Length is not a reliable guide.", "", "These questions are often the easiest to settle by careful reading.", "Position is not a guide."]),
        QUIZ("Paper 1 has 50 questions in 90 minutes. What is the average time per question?", ["1.2 minutes", "1.5 minutes", "1.8 minutes", "2.0 minutes"], 2,
             "90 ÷ 50 = 1.8 minutes.",
             hint="Divide the time by the number of questions.",
             feedback=["That would be 60 minutes.", "That would be 75 minutes.", "", "That would be 100 minutes."]),
        PQ("List the four steps you would follow for every multiple-choice question and say what each prevents.",
           "Read the stem and underline key words (prevents missing 'NOT' or 'best'); predict an answer first (prevents being led by a clever wrong option); eliminate wrong options with reasons (reduces guessing); check units and sense for calculations (prevents unit and power-of-ten errors)."),
        PQ("A student finds 12.0 percent nitrogen in a food and answers 'protein = 12.0 percent'. Explain the error and give the correct value.",
           "The nitrogen percentage was given as the protein percentage; the last step (multiplying by the nitrogen factor 6.25) was left out. Protein = 12.0 × 6.25 = 75 percent (a teaching value). The wrong option is the typical unfinished calculation distractor."),
        SUM("Paper 1 has 50 multiple-choice questions, 35 percent of the marks, 1 hour 30 minutes, whole syllabus (Board's 2023 report).",
            "Read the stem, predict, eliminate, check units.",
            "Know the confusable pairs and the unfinished-calculation trap.",
            "Revise by module and use the mock to find weak topics."),
    ],
))

LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: essay-type questions, command words and planning",
    slug="fsl2-paper2-essay",
    minutes=22,
    summary="How Paper 2 is built (eight essay-type questions in four sections), what the Board's report says candidates did well and badly, and how to read command words, plan answers and use the marks as a guide to length.",
    objectives=[
        "Describe Paper 2 as the report describes it and follow the rubric about sections",
        "Interpret command words such as define, state, explain, assess, differentiate and discuss",
        "Plan a structured answer with a short plan, headings and examples",
        "Avoid the errors that the Board's report identifies",
    ],
    key_concepts=["Paper 2", "Section", "Command word", "Differentiate", "Assess", "Flow diagram", "Match answer to marks", "Food composition table"],
    blocks=[
        H("What the paper is"),
        D("The Board's 2023 report describes Paper 2 as an **essay-type** paper that carries **40 percent** of the examination and lasts **3 hours**. It covers the whole syllabus. The report lists **eight questions in four sections**: Section A (application of nutritional science), Section B (food consumption and health), Section C (food science) and Section D (community health and nutrition), with two questions in each, and scores for each question are given out of 25.", title="Paper 2 in the Board's report"),
        T("The report also says that some candidates answered two questions from one section when they should have answered one, and it advises students to follow instructions on the question paper strictly. "
          "Read the rubric on your paper carefully: it tells you how many questions to answer and from which sections. The tables in the report show that the most attempted questions were the enzyme question in Section C and the community nutrition question in Section D (question 8); the least attempted were the question on fats (rancidity and margarine) and the food habits question in Section D."),
        KEY("What the report says went wrong", "Paraphrased from the Board's comments on candidates.", cards=[
            ["Energy and composition", "Basal metabolic rate was not understood, and candidates did not know the parts of a food composition table or how to use it."],
            ["Protein quality", "Candidates could not tell high biological value (HBV) proteins from low biological value (LBV) proteins."],
            ["Hormones and blood sugar", "The roles of insulin and glucagon in regulating blood glucose were weak, and so was the explanation of the four dimensions of food security."],
            ["Blood vessels", "Atherosclerosis and arteriosclerosis were not told apart."],
            ["Fats", "Rancidity was not defined and its prevention was not proposed, and the flow diagram for margarine was mixed up with the one for cheese."],
            ["Enzymes", "Selectivity (specificity) was confused with catalytic function."],
            ["Food habits", "Food fads, food taboos and food fallacies were mixed up."],
        ]),
        T("The common cause the report gives is incomplete coverage of the syllabus. The remedy is simple: learn the definitions of the pairs that are mixed up, and learn the flow diagrams (margarine, cheese, bread) separately."),
        H("Command words"),
        KEY("What the verbs ask", "Do what the word asks and no more.", cards=[
            ["State, name, list", "Give the facts briefly. No reason is needed."],
            ["Define", "Give the exact meaning in a short sentence and, if helpful, an example."],
            ["Differentiate or distinguish", "Give the difference between two things, using a point for each. A table or 'whereas' sentences work well."],
            ["Describe", "Say what it looks like or what happens, in order. A flow diagram of a process is a description."],
            ["Explain", "Give reasons: how and why. Use 'because' or 'so'."],
            ["Assess or evaluate", "Weigh up the importance or the strengths and weaknesses and reach a judgement, with reasons."],
            ["Discuss", "Give several points of view or effects, with evidence, and a short conclusion."],
        ]),
        H("Planning an answer"),
        T("Match the length to the marks: roughly one clear point (a fact with its reason or example) per mark. A part worth 4 marks needs four points, not a page. Spend 2 minutes on a plan: write the headings, then add one example for each. "
          "With 3 hours for four 25-mark answers, you have about 40 to 45 minutes for each question, leaving time to read and check."),
        EX("Worked example 1: differentiate", intro="Differentiate between a food fad, a food taboo and a food fallacy.", steps=[
            S("Food fad", text="A temporary enthusiasm for a particular food or diet, usually followed by many people for a short time, often without scientific basis."),
            S("Food taboo", text="A food that a group forbids or avoids for religious, cultural or social reasons, usually for a long time."),
            S("Food fallacy", text="A false belief about a food or its effects on health, such as the claim that a certain food cures a disease or makes a person lose a stated weight overnight."),
            S("Add an example of each", text="Give one example you are sure of, in your own region or textbook. Do not mix up the definitions."),
        ]),
        EX("Worked example 2: plan for an explain question", intro="Explain how Staphylococcus aureus causes food poisoning and how it can be prevented (8 marks).", steps=[
            S("Cause", text="S. aureus lives on the skin and in the nose of handlers and gets onto food by handling (1 to 2 marks)."),
            S("Growth and toxin", text="In warm, moist, protein-rich food the cells multiply and release heat-stable enterotoxin (2 marks)."),
            S("Effect", text="The toxin causes vomiting and cramps within hours; cooking does not destroy it (2 marks)."),
            S("Prevention", text="Hand washing, covering cuts, not handling food when ill, rapid cooling and holding hot or cold (2 to 3 marks)."),
        ]),
        H("Diagrams and flow charts"),
        T("The report says that the margarine flow diagram was mixed up with the cheese diagram, so learn the sequence and the purpose of each stage. Draw flow diagrams as a neat vertical list of boxes joined by arrows, with a short note on what happens at each stage. Label with a ruler, not freehand."),
        MISTAKE("Answering two questions from the same section when the rubric says one", "Examiners may mark only the first or the best, depending on the rule. Read the rubric twice."),
        MISTAKE("Writing everything you know on the topic", "A question on rancidity prevention wants the causes and the steps that stop them; do not add a lecture on all fats. Answer what is asked."),
        TIP("Exam link: Paper 2 covers 100 percent of the syllabus. Choose the questions by the parts you can answer, not by the first part only. Do all parts of the question you choose; the marks per part are given on the paper."),
        QUIZ("What does the command word 'differentiate' require?", ["A long description of one thing", "The differences between two or more things", "A list of examples", "A calculation only"], 1,
             "Differentiate means give the differences, point by point.",
             hint="Think of 'difference'.",
             feedback=["That is 'describe'.", "", "That is 'list' or 'give examples'.", "A calculation is not asked for."]),
        QUIZ("A 25-mark Paper 2 question has four parts. What is the best use of time?", ["Spend all the time on the first part", "Plan briefly and give each part the time and length that its marks suggest", "Answer only the parts you like", "Write the longest answer you can for part (a)"], 1,
             "The marks per part guide how long each answer should be, and every part must be tried.",
             hint="How do you earn the marks across the whole question?",
             feedback=["Later parts will lose marks.", "", "Unanswered parts get no marks.", "A long answer to one part cannot make up for blanks elsewhere."]),
        PQ("Define rancidity and propose three measures to prevent it in a fat or oil.",
           "Rancidity is the development of unpleasant tastes and smells in fats and oils, caused by oxidation of unsaturated fatty acids (oxidative rancidity) or by hydrolysis of the fat by lipase (hydrolytic rancidity). Measures: store in airtight, dark, cool containers; add antioxidants such as vitamin E or permitted synthetic antioxidants; avoid contact with metals such as copper and iron; keep the fat dry; heat to inactivate lipase."),
        PQ("Differentiate between high biological value (HBV) and low biological value (LBV) proteins and give an example of each.",
           "HBV proteins supply all the essential amino acids in proportions close to human needs and are used well by the body; examples are egg, milk, meat and fish. LBV proteins lack, or are low in, one or more essential amino acids; examples are many plant proteins such as maize or cassava. LBV proteins can be combined (complementary proteins, for example cereal with legume) to give a better mixture."),
        PQ("Explain how insulin and glucagon regulate blood glucose.",
           "After a meal, blood glucose rises; the beta cells of the pancreas release insulin, which makes liver, muscle and fat cells take up glucose and store it as glycogen (and fat), so blood glucose falls. When blood glucose falls, alpha cells release glucagon, which makes the liver break down glycogen and make glucose, so blood glucose rises. They are an example of negative feedback."),
        SUM("Paper 2: essay-type, 40 percent, 3 hours, covers the whole syllabus; eight questions in four sections, scored out of 25 each in the report.",
            "Follow the rubric about how many questions to answer from each section.",
            "Obey the command word, match the length to the marks and plan briefly.",
            "Learn the pairs and diagrams that candidates mixed up in 2023."),
    ],
))

LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: practical skills, food tests, cookery and sensory work",
    slug="fsl2-paper3-practical-skills",
    minutes=24,
    summary="What the practical paper tests (food tests and cookery), how to carry out and report the standard tests including negative results, how to use the food composition table, how to plan a cookery practical, and how to cope with a school laboratory.",
    objectives=[
        "State the structure of Paper 3 from the Board's report",
        "Carry out and report the standard food tests, including negative results",
        "Use the food composition table to calculate nutrients in a portion",
        "Plan and justify a cookery practical with a time plan and the science of each step",
    ],
    key_concepts=["Paper 3", "Food test", "Negative result", "Control", "Food composition table", "Time plan", "Cookery science", "Sensory evaluation"],
    blocks=[
        H("What the paper is"),
        D("The Board's 2023 report says Paper 3 is a **practical** paper that carries **25 percent** and lasts **2 hours**, in two parts: **Part 1, food tests** and **Part 2, cookery**. Part 2 has three groups of cookery tasks. Candidates are asked to identify food samples with reagents, report results, use the food composition table for calculations, and cook and present dishes.", title="Paper 3 in the Board's report"),
        T("The report says that in Part 1 most candidates could identify the samples with the reagents given, but many did not report their **negative results**, and many were weak in calculations that need the **food composition table** (FCT). In Part 2 the report says performance was above average. "
          "It also advises teachers to cover the practical manual, to explain the science behind cookery, and to use only the FCT supplied by the Board. Students are advised to attend all practical sessions."),
        H("Part 1: food tests"),
        IMG("alfsl2-food-tests.svg", alt="Table of six food tests: starch with iodine, reducing sugar with Benedict, non-reducing sugar with acid hydrolysis then Benedict, protein with biuret, fat with ethanol emulsion, vitamin C with DCPIP", caption="Figure 1. Standard food tests and positive results (check your practical manual for the exact reagents and quantities)."),
        T("Take a small amount of the food (grind and dissolve solids in water, or use as a paste), add the reagent, and observe. Record **what you did, what you saw** and **what you conclude**. A test that does not give the positive colour is a **negative result**, and it must be reported: 'no change from blue; reducing sugar absent'. A negative result is also evidence."),
        CODE("""Sample  Test            Observation                  Conclusion
A       Iodine          stays yellow-brown           starch absent
A       Benedict's      blue stays blue after heat   reducing sugar absent
A       Biuret          turns violet                 protein present
B       Iodine          turns blue-black             starch present
B       Benedict's      green then yellow            small reducing sugar present""", "text", title="A model table for recording results"),
        KEY("Good practice in food tests", "These details gain marks.", cards=[
            ["Safety", "Use test tubes in a rack, heat in a water bath (not directly in a flame, no pointing at faces), wear a lab coat, and handle copper sulphate, sodium hydroxide and acids with care."],
            ["Controls", "Use water as a negative control and a known positive food as a positive control, if allowed, to check the reagent."],
            ["Quantities", "Use the amounts in your manual, and add reagents drop by drop where it says so."],
            ["Reporting", "Report all observations including negative results, state the reagent, and draw conclusions that match the evidence: a faint change is a small amount, not a large one."],
        ]),
        T("Semi-quantitative reading of Benedict's: blue (none), green (trace), yellow, orange, brick-red (large amount). To test for **non-reducing sugars** such as sucrose, first do Benedict's (negative), then boil a fresh sample with dilute hydrochloric acid to hydrolyse it, neutralise with sodium hydrogencarbonate until it stops fizzing, and repeat Benedict's: a positive result now shows a non-reducing sugar. The **vitamin C test** with DCPIP: the blue dye is decolourised by vitamin C (a reducing agent); the more vitamin C, the fewer drops of juice needed."),
        H("Using the food composition table"),
        T("A **food composition table (FCT)** lists the nutrients in 100 g of the edible portion of a food. Calculations scale these values to the portion eaten or cooked. The report advises that only the FCT supplied by the Board should be used, because its values and layout are the ones the questions are set on. The values in the example below are **invented for practice** and are not from any real table."),
        CODE("""Food (per 100 g edible portion)   Energy kJ   Protein g   Fat g   Iron mg
Rice, cooked (practice value)        500         2.7        0.3     0.2
Beans, cooked (practice value)       500         8.0        0.5     2.0
Fish, grilled (practice value)       700        22.0        5.0     1.0""", "text", title="A practice FCT extract (invented for practice)"),
        EX("Worked example 1: portion calculation", intro="A meal contains 150 g cooked rice and 100 g cooked beans (edible portions). Using the practice table, calculate the protein and the energy in the meal.", steps=[
            S("Scale the rice", math=r"150 \times \frac{2.7}{100} = 4.05 \text{ g protein};\quad 150 \times \frac{500}{100} = 750 \text{ kJ}"),
            S("Scale the beans", math=r"100 \times \frac{8.0}{100} = 8.0 \text{ g protein};\quad 100 \times \frac{500}{100} = 500 \text{ kJ}"),
            S("Add", math=r"\text{protein} = 4.05 + 8.0 = 12.05 \text{ g};\quad \text{energy} = 750 + 500 = 1250 \text{ kJ}"),
        ], check=r"12.05\ \text{g protein and } 1250\ \text{kJ}"),
        EX("Worked example 2: from raw weight to edible portion", intro="A recipe uses 200 g of a vegetable with 20 percent waste (peel and stalks). The edible portion has 3.0 g of protein per 100 g (practice value). How much protein is in the recipe?", steps=[
            S("Edible mass", math=r"200 \times (1 - 0.20) = 160 \text{ g}"),
            S("Protein", math=r"160 \times \frac{3.0}{100} = 4.8 \text{ g}", text="Using the raw weight instead of the edible weight is a common error."),
        ]),
        H("Part 2: cookery"),
        T("In cookery you are given a task (for example a dish for a family, a child or a person with a stated need), usually with a limited time. The marks reward the **plan**, the **hygiene and organisation**, the **method and the final dish**, and the **explanation of the science**. "
          "The report advises teachers to teach the science behind cookery, so be ready to say why each method is used."),
        KEY("Cookery science to quote", "Link a step to a reason.", cards=[
            ["Gelatinisation", "Starch granules swell and thicken a sauce or porridge when heated in water."],
            ["Maillard browning", "Amino acids and reducing sugars give a brown colour and flavour on frying and baking."],
            ["Coagulation", "Egg and milk proteins set when heated (denaturation then aggregation); gentle heat stops curdling."],
            ["Emulsification", "Egg yolk lecithin holds oil and water together in mayonnaise."],
            ["Enzymatic browning", "Cut apple or plantain browns as polyphenol oxidase acts in air; lemon juice (acid) and quick cooking slow it."],
            ["Raising agents", "Yeast or baking powder make carbon dioxide; steam and air also expand in the oven."],
            ["Vitamin retention", "Water-soluble vitamins leach into cooking water and some are heat labile; cook in a small amount of water, for a short time."],
        ]),
        CODE("""Time    Task
0:00    Wash hands, put on apron, wash and prepare vegetables
0:10    Start the longest-cooking item (beans) in a covered pot
0:25    Prepare sauce ingredients, heat oil
0:40    Cook sauce; rice on to boil
1:00    Check seasoning, taste with a clean spoon
1:10    Serve hot, garnish, clean the work area""", "text", title="An outline time plan for a 1 hour 20 minute meal"),
        T("Always show a plan with a menu, a list of ingredients with quantities, a time plan, and a short note of the nutritional value (for example 'beans give protein and iron; vegetables give vitamins and fibre'). Present the dish neatly, and clear the working area."),
        H("School laboratory realities"),
        T("Equipment may be shared, fuel and water limited and the power supply uncertain. Prepare for this: practise at home with the same methods, write the method down so that you can follow it when stressed, and use a rack, a water bath or a kettle if the burner is busy. Wash and dry equipment before you start, bring a clean towel, and keep reagents labelled. Attending every practical session is the best preparation: the report says so for students."),
        MISTAKE("Not reporting negative results", "Writing only the positive tests loses marks in the report. Every test done should appear in the table with its result."),
        MISTAKE("Using raw weight with an edible-portion table", "FCT values are for the edible portion. Remove waste before you scale."),
        TIP("Exam link: the report records that Part 1 identification was done well but reporting and calculations were weak, and that cookery was above average and balanced. Do not skip the written plan and the explanations."),
        QUIZ("A solution turns blue-black when iodine solution is added. What does this show?", ["Reducing sugar", "Starch", "Protein", "Fat"], 1,
             "A blue-black colour with iodine shows starch.",
             hint="Recall the iodine test.",
             feedback=["Reducing sugars are shown by Benedict's test.", "", "Protein gives a violet colour with biuret.", "Fat gives an emulsion with ethanol and water."]),
        QUIZ("In a food test, no colour change is observed. What should you do?", ["Leave it out of the report", "Record it as a negative result and state the conclusion", "Repeat until you get a colour", "Write the opposite result"], 1,
             "A negative result is an observation and must be reported, with the conclusion that the nutrient is absent (or below detection).",
             hint="Think about what the report says.",
             feedback=["The report says that candidates lost marks by leaving these out.", "", "Repeating is fine for checking, but you must report what you observed.", "That would be false."]),
        PQ("Describe how you would test a food sample for reducing sugar and for protein, and say how you would report negative results.",
           "Reducing sugar: add Benedict's solution to the sample in a test tube and heat in a boiling water bath for a few minutes; green, yellow, orange or brick-red shows reducing sugar; no change from blue is negative. Protein: add sodium hydroxide and a few drops of dilute copper sulphate; violet or purple is positive, blue stays negative. Report each test in a table (test, observation, conclusion), including negative results such as 'remains blue: reducing sugar absent'."),
        PQ("Using the practice FCT in this lesson, find the protein in 120 g of grilled fish.",
           "Protein = 120 × 22.0/100 = 26.4 g (the table value is invented for practice)."),
        PQ("Plan a two-course lunch for a family of four using a staple, a protein food and a vegetable. Give the menu, the time plan, two cookery-science points and the nutritional value.",
           "Example: rice, bean stew with vegetables and fruit. Time plan with the longest-cooking beans first, then the stew sauce, then rice, then the fruit, ending with serving hot and clearing up. Science: gelatinisation of rice starch; vegetables cooked briefly in little water to keep vitamin C. Nutrition: rice gives energy, beans give protein and iron, vegetables and fruit give vitamins, fibre and minerals; the cereal with legume gives complementary protein. (Use your own examples and the quantities in the question.)"),
        SUM("Paper 3 is practical, 25 percent, 2 hours, with food tests and cookery (Board's 2023 report).",
            "Report every food test, including negative results; show the observation and the conclusion.",
            "Use the Board's FCT, the edible portion and the correct scaling from 100 g.",
            "In cookery, plan, organise, keep hygiene and explain the science of each method."),
    ],
))

