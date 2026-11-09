"""Form 5 Human Biology: Human Nutrition & the Digestive System and Respiration, Circulation & Excretion. 13 lessons, one practice set each.

Content source: KKEVO master curriculum blueprint (modules HBI-0565-M3 and M4) and the Board's 2023 Ordinary Level
subject report (Paper 1 has 50 multiple-choice questions, Paper 2 has essay-type questions).
Numbers in tables and calculations are simple teaching data. Diagrams are schematic.
"""

from .dsl import *  # noqa: F403

COURSE = ("human-biology", "form-5")

NUT = "Human Nutrition & the Digestive System"
RES = "Respiration, Circulation & Excretion"

LESSONS = []

# ------------------------------------------------------------------ 1. A balanced diet and food tests
LESSONS.append(lesson(
    module=NUT,
    topic="A balanced diet and food tests",
    title="A balanced diet and the food tests",
    slug="hbi2-balanced-diet-and-food-tests",
    minutes=22,
    summary="What a balanced diet is, why people need different amounts of energy, and how to test a food for starch, reducing sugar, protein, lipid and vitamin C, with the colour changes to expect.",
    objectives=[
        "Define a balanced diet and explain why energy needs differ between people",
        "Carry out and describe the iodine, Benedict's, biuret, ethanol emulsion and DCPIP tests",
        "State the positive and negative colour result of each food test",
        "Draw a conclusion about a food from a table of test results",
    ],
    key_concepts=["Balanced diet", "Energy value", "Iodine test", "Benedict's test", "Biuret test", "Ethanol emulsion test", "DCPIP test"],
    blocks=[
        H("Introduction"),
        T("A farmer who walks to his field every morning and a student who sits in a classroom all day do not need the same amount of food. "
          "A good meal for one is too much for the other. In this lesson you will learn what makes a diet balanced, and how a laboratory "
          "can show which nutrients a food contains."),
        D("A **balanced diet** contains all the nutrients (carbohydrates, proteins, lipids, vitamins, mineral salts, water and fibre) in the right "
          "proportions for the person's age, sex and activity, and gives the right amount of energy.",
          title="Definition: balanced diet"),
        T("The functions of each nutrient were studied in the module on cells and food biochemistry. Here we use them to plan meals and to test foods."),
        H("What decides how much energy you need"),
        KEY("Energy needs change", "The energy in food is measured in kilojoules (kJ). A person needs more when:", cards=[
            ["Growing", "Children and teenagers need extra protein, calcium and energy to build new tissue."],
            ["Very active", "A builder, a farmer or an athlete uses much more energy than an office worker."],
            ["Pregnant or breast-feeding", "A mother needs extra energy, protein, iron and calcium for her baby."],
            ["Bigger body", "Adults with a large body mass use more energy than small adults. Men on average need more than women."],
        ]),
        T("The energy values below are rounded numbers used for teaching. Textbooks differ a little, so check your textbook."),
        CODE("""Nutrient        Energy released (approximate)
Carbohydrate    17 kJ per gram
Protein         17 kJ per gram
Lipid           37 kJ per gram""", "text", title="Approximate energy values"),
        EX("Worked example 1: energy in a meal", intro="A meal of rice and beans contains 60 g of carbohydrate, 10 g of protein and 5 g of lipid. Find its energy value.", steps=[
            S("Carbohydrate", math=r"60 \times 17 = 1020 \text{ kJ}"),
            S("Protein", math=r"10 \times 17 = 170 \text{ kJ}"),
            S("Lipid", math=r"5 \times 37 = 185 \text{ kJ}"),
            S("Add", math=r"1020 + 170 + 185 = 1375 \text{ kJ}"),
        ]),
        TIP("Lipid gives more than twice the energy of carbohydrate or protein for the same mass. That is why a small amount of palm oil or fried food adds a lot of energy."),
        H("Testing foods"),
        T("To find which nutrients are in a food, we crush or mix a small sample with water and add a **reagent** (a chemical that changes colour "
          "if a certain nutrient is present). Always wear eye protection, and never taste anything in a laboratory."),
        CODE("""Test             Reagent and method                         Negative       Positive
Starch           Add a few drops of iodine solution         yellow-brown   blue-black
Reducing sugar   Benedict's solution, heat in a hot        blue           green, yellow, orange
                 water bath for a few minutes                              then brick-red
Protein          Biuret test: add sodium hydroxide then     blue           purple (violet)
                 a few drops of dilute copper sulphate
Lipid            Ethanol emulsion test: shake the food      clear          cloudy white
                 with ethanol, then pour into water                        emulsion
Vitamin C        DCPIP solution (blue): add drops of the    stays blue     DCPIP turns
                 food juice                                                colourless""", "text", title="Summary of the food tests"),
        T("For the **Benedict's test** the colour depends on how much reducing sugar there is. A little sugar gives green, more gives yellow "
          "or orange, and a lot gives a brick-red precipitate (solid particles in the liquid). Glucose and maltose are reducing sugars. "
          "Ordinary table sugar (sucrose) is not a reducing sugar and gives no change unless it is first broken down by boiling with acid."),
        T("For the **ethanol emulsion test** the lipid dissolves in ethanol. When this mixture is poured into water, the lipid forms tiny droplets "
          "that make the water look cloudy and white. A simple test with no chemicals is to rub the food on paper: a lipid leaves a "
          "see-through (translucent) greasy mark."),
        T("The **DCPIP test** shows vitamin C. DCPIP is a blue dye that loses its colour when vitamin C is added. The more vitamin C a juice has, the "
          "fewer drops are needed to make the dye colourless."),
        EX("Worked example 2: reading test results", intro="A food sample gives these results. Which nutrients does it contain?", steps=[
            S("Iodine test", text="The sample turns blue-black. Starch is present."),
            S("Benedict's test", text="It stays blue after heating. There is no reducing sugar."),
            S("Biuret test", text="It turns purple. Protein is present."),
            S("Ethanol emulsion", text="The water stays clear. There is no lipid."),
            S("Conclusion", text="The sample contains starch and protein, but no reducing sugar and no lipid. A food such as a cooked bean paste could give this pattern."),
        ]),
        EX("Worked example 3: planning a balanced meal", intro="A Form 5 student eats only boiled yam with palm oil. Suggest two changes to make the meal balanced.", steps=[
            S("Find what the meal has", text="Yam gives carbohydrate and palm oil gives lipid. Almost no protein, vitamins or fibre."),
            S("Add protein", text="Add fish, beans, eggs or groundnuts."),
            S("Add vitamins, minerals and fibre", text="Add green leaves such as njama njama and a fruit. Drink clean water."),
        ]),
        MISTAKE("Wrong colour for Benedict's", "Benedict's solution starts blue and the negative result is blue. A student who writes 'no colour change' needs to say which colour it stayed. The positive result is a range from green to brick-red, not 'red' only."),
        MISTAKE("Forgetting to heat Benedict's", "The Benedict's test needs heating in a hot water bath. Starch, protein and lipid tests do not need heat. Mixing up the reagents (iodine for sugar) is a very common error."),
        MISTAKE("Calling a diet balanced because it is large", "Eating a lot of one nutrient is not balanced. A balanced diet has the right proportions of all seven parts."),
        TIP("In Paper 1 multiple choice, food tests are often given as a table of colours that you must match to a nutrient. In Paper 2 you may be asked to describe how you would test a food, so learn the reagent, the method and both colours."),
        QUIZ("A food is mixed with iodine solution and turns blue-black. Which nutrient is present?",
             ["Protein", "Reducing sugar", "Starch", "Lipid"], 2,
             "Iodine solution turns blue-black with starch.",
             hint="Which test uses iodine solution?",
             feedback=["Protein is tested with biuret reagent and gives purple.", "Reducing sugar is tested with Benedict's solution and heat.", "", "Lipid is tested with ethanol and water, giving a cloudy white emulsion."]),
        QUIZ("Which test needs a hot water bath?",
             ["Iodine test for starch", "Benedict's test for reducing sugar", "Biuret test for protein", "DCPIP test for vitamin C"], 1,
             "Benedict's solution must be heated for the colour to change.",
             hint="Only one reagent needs heat.",
             feedback=["Iodine is added at room temperature.", "", "Biuret is also done without heating.", "DCPIP is added drop by drop with no heating."],
             title="Quick check 2"),
        PQ("Describe how you would test a sample of food for protein. State the colour for a positive result.",
           "Place a little of the food, crushed and mixed with water, in a test tube. Add sodium hydroxide solution, then add a few drops of dilute copper sulphate solution and shake. If protein is present the mixture turns purple (violet). If there is no protein it stays blue."),
        PQ("A juice is tested with DCPIP. Juice X decolourises 1 cm3 of DCPIP with 4 drops. Juice Y needs 12 drops. Which juice has more vitamin C and why?",
           "Juice X. Vitamin C makes DCPIP colourless. Juice X needed fewer drops to do this, so it contains more vitamin C per drop."),
        PQ("Explain why a plantain farmer and a secondary school student need different amounts of energy.",
           "The farmer does heavy physical work, so his muscles use more energy, and he needs more carbohydrate and lipid. The student is much less active, so needs less. Energy needs depend on activity, age, sex, body size and whether a person is growing or pregnant."),
        PQ("Calculate the energy in a snack containing 40 g of carbohydrate, 15 g of protein and 20 g of lipid, using 17, 17 and 37 kJ per gram.",
           "Carbohydrate 40 x 17 = 680 kJ. Protein 15 x 17 = 255 kJ. Lipid 20 x 37 = 740 kJ. Total 680 + 255 + 740 = 1675 kJ."),
        SUM("A balanced diet has all seven nutrients in the right proportions for a person's age, sex and activity.",
            "Energy is measured in kilojoules. Carbohydrate and protein give about 17 kJ per gram and lipid about 37 kJ per gram (check your textbook).",
            "Iodine turns blue-black for starch. Benedict's goes from blue to green, yellow, orange or brick-red when heated with reducing sugar.",
            "Biuret turns purple for protein. Ethanol with water gives a cloudy white emulsion for lipid. DCPIP loses its blue colour for vitamin C."),
    ],
))

# ------------------------------------------------------------------ 2. Malnutrition
LESSONS.append(lesson(
    module=NUT,
    topic="Malnutrition",
    title="Malnutrition: too little, too much or the wrong mix",
    slug="hbi2-malnutrition",
    minutes=20,
    summary="Malnutrition means a diet that is not balanced: kwashiorkor, marasmus, obesity and vitamin and mineral deficiencies, with their signs, causes and prevention.",
    objectives=[
        "Define malnutrition and give examples of undernutrition and overnutrition",
        "Compare kwashiorkor and marasmus in cause and signs",
        "Explain the causes and risks of obesity",
        "Name the main vitamin and mineral deficiency diseases and how to prevent them",
    ],
    key_concepts=["Malnutrition", "Kwashiorkor", "Marasmus", "Obesity", "Deficiency disease", "Anaemia", "Goitre", "Rickets"],
    blocks=[
        H("Introduction"),
        T("When we hear the word 'malnutrition' we usually think of a thin, hungry child. But a person who eats too much of the wrong food can also "
          "be malnourished. Both problems are found in Cameroon, in villages and in cities."),
        D("**Malnutrition** is a condition caused by a diet that does not have the right amount or the right mix of nutrients. It includes too little "
          "of some nutrients (**undernutrition** and deficiency) and too much of others (**overnutrition**).",
          title="Definition: malnutrition"),
        H("Kwashiorkor and marasmus"),
        T("These two diseases are the main forms of protein-energy malnutrition in young children. They usually appear after a child is weaned "
          "(taken off breast milk) and given food that is poor in protein or too small in amount."),
        KEY("Kwashiorkor and marasmus compared", "Both come from poor diets, but the diet and the signs are different.", cards=[
            ["Kwashiorkor: cause", "Not enough protein. The child may still get some energy from starchy food such as cassava or maize porridge."],
            ["Kwashiorkor: signs", "Swollen belly and swollen (oedema) legs and feet from fluid, thin muscles, poor growth, thin hair that may change colour, apathy and sadness."],
            ["Marasmus: cause", "Not enough food of all kinds: too little energy and protein together."],
            ["Marasmus: signs", "Severe wasting. The child is very thin, with visible ribs and wrinkled skin like an 'old person', weak and very small for his or her age. No swelling."],
        ]),
        T("Prevention is the same for both: breast-feed babies, then give a mixed diet containing protein foods (beans, groundnuts, soya, eggs, fish, "
          "milk) as well as energy foods. Treat infections early, because diarrhoea and other illnesses make malnutrition worse. A malnourished "
          "child needs a clinic or hospital: do not treat it only at home."),
        H("Obesity"),
        D("**Obesity** means having so much body fat that health is harmed. It is a form of overnutrition. It happens when the energy taken in "
          "from food is greater than the energy used up, over a long time. The extra is stored as fat.",
          title="Definition: obesity"),
        T("Causes include eating a lot of fatty and sugary foods, drinking sugary soft drinks, little exercise, and in some people inherited "
          "tendencies. The risks include high blood pressure, heart disease, a type of diabetes in adults, and strain on joints. Prevention: "
          "eat less fat and sugar, more vegetables and fruit, watch portion sizes and stay active, such as by walking and playing sport."),
        H("Vitamin and mineral deficiency diseases"),
        CODE("""Missing nutrient   Disease           Signs                           Foods that help
Vitamin A          Night blindness   Cannot see well in dim light    Carrot, red palm oil, liver, green leaves
Vitamin C          Scurvy            Bleeding gums, slow healing     Orange, guava, pawpaw, lemon
Vitamin D          Rickets           Soft, bent leg bones (children) Eggs, oily fish; sunlight on skin
Iron               Anaemia           Pale, tired, short of breath    Liver, beans, dark green leaves, meat
Iodine             Goitre            Swollen neck (thyroid gland)    Iodised salt, sea fish
Calcium            Weak bones/teeth  Brittle bones, tooth decay      Milk, small fish eaten whole, beans""", "text", title="Deficiency diseases"),
        T("**Anaemia** happens when the blood has too little haemoglobin to carry oxygen. Iron is needed to make haemoglobin, so a diet low in iron is a "
          "common cause, but anaemia can also have other causes such as infection or blood loss, so see a health worker. **Goitre** is a swelling "
          "of the thyroid gland because it needs iodine to make its hormone; using iodised salt prevents it."),
        EX("Worked example 1: identify the disease", intro="A two-year-old child has a swollen belly, swollen feet, thin arms and thin hair. The family eats mostly cassava. Name the disease, the nutrient lacking and one way to prevent it.", steps=[
            S("Match the signs", text="Swollen belly and feet with thin arms point to kwashiorkor, not marasmus (which has no swelling)."),
            S("Name the nutrient", text="Cassava is mostly carbohydrate, so the diet lacks protein."),
            S("Prevent it", text="Add beans, eggs, fish or groundnuts to the child's meals, and keep breast-feeding until the age recommended by the health centre."),
        ]),
        EX("Worked example 2: compare two children", intro="Child A is very thin, wrinkled and weak with no swelling. Child B has a swollen belly and thin limbs. Which child has marasmus?", steps=[
            S("Look for swelling", text="Swelling (oedema) is a sign of kwashiorkor. Child B has it."),
            S("Look for wasting", text="Child A is severely wasted without swelling. This is marasmus."),
            S("Answer", text="Child A has marasmus; child B has kwashiorkor."),
        ]),
        MISTAKE("Saying kwashiorkor is 'lack of food'", "Marasmus is lack of food in general. Kwashiorkor is specifically too little protein. Examiners expect the word protein."),
        MISTAKE("Forgetting that malnutrition includes obesity", "Malnutrition does not only mean being thin. Eating too much of the wrong food is also malnutrition."),
        MISTAKE("Mixing the vitamin and the disease", "Learn pairs: vitamin C with scurvy, vitamin D with rickets, vitamin A with night blindness, iron with anaemia, iodine with goitre."),
        TIP("Paper 1 often asks you to match a sign (swollen neck, bleeding gums, bent legs) with a deficiency. Paper 2 may ask for the causes and prevention of kwashiorkor or obesity. Use the words cause, sign and prevention in your answers. This lesson gives general information, not medical diagnosis."),
        QUIZ("Which sign is found in kwashiorkor but not in marasmus?",
             ["Very thin body", "Swollen belly and feet", "Weakness", "Slow growth"], 1,
             "Swelling from fluid (oedema) is typical of kwashiorkor.",
             hint="Which sign is linked to fluid collecting in tissues?",
             feedback=["Both conditions give a thin body, though in kwashiorkor it is the arms and legs.", "", "Weakness is found in both.", "Both slow growth."]),
        QUIZ("Which food best helps prevent goitre?", ["Iodised salt", "Orange", "Rice", "Palm oil"], 0,
             "Iodine is needed by the thyroid gland, and iodised salt supplies it.",
             hint="Goitre is a swelling of the neck.",
             feedback=["", "Orange gives vitamin C, which prevents scurvy.", "Rice is mainly carbohydrate.", "Palm oil gives lipid and vitamin A, not iodine."],
             title="Quick check 2"),
        PQ("State two differences between kwashiorkor and marasmus.",
           "Kwashiorkor is caused by too little protein, marasmus by too little food of all kinds (energy and protein). Kwashiorkor shows swelling of the belly and legs; marasmus shows severe wasting with no swelling."),
        PQ("Explain how obesity can develop.",
           "Obesity develops when a person eats more energy than the body uses, for a long period. The extra energy from fat and sugar is stored as body fat. Little exercise makes this worse."),
        PQ("Name the deficiency disease caused by too little vitamin D and describe its effect on the body.",
           "Rickets. Vitamin D helps the body take in calcium for bones, so in a child the bones stay soft and the legs bend under the body weight."),
        PQ("Suggest a day's meals that would help prevent anaemia in a teenage girl.",
           "Include iron-rich foods such as beans, liver or meat and dark green leaves like njama njama, with a fruit for vitamin C (which helps iron be absorbed). Avoid skipping meals. If she often looks pale or tired she should see a health worker."),
        SUM("Malnutrition means a diet that is wrong in amount or mix: too little (undernutrition) or too much (overnutrition).",
            "Kwashiorkor is due to protein lack and shows swelling; marasmus is due to lack of all food and shows severe wasting.",
            "Obesity comes from taking in more energy than is used; it raises the risk of heart disease and high blood pressure.",
            "Know the pairs: vitamin A and night blindness, C and scurvy, D and rickets, iron and anaemia, iodine and goitre."),
    ],
))

# ------------------------------------------------------------------ 3. Teeth and dental decay
LESSONS.append(lesson(
    module=NUT,
    topic="Teeth and dental decay",
    title="Teeth: structure, types and dental decay",
    slug="hbi2-teeth-and-dental-decay",
    minutes=20,
    summary="The structure of a tooth, the four types of human teeth and their jobs, the dental formula, and how sugar and bacteria cause decay and how to prevent it.",
    objectives=[
        "Name and describe the parts of a tooth in a vertical section",
        "Name the four types of teeth and state the function of each",
        "Interpret the dental formula of an adult",
        "Explain how dental decay happens and how it is prevented",
    ],
    key_concepts=["Enamel", "Dentine", "Pulp cavity", "Cement", "Incisor, canine, premolar, molar", "Dental formula", "Plaque", "Dental decay"],
    blocks=[
        H("Introduction"),
        T("Teeth are the first part of the digestive system to work on food. Chewing breaks food into small pieces so that enzymes can reach more "
          "of its surface. A person with bad teeth often cannot chew well and may suffer pain. In this lesson you will study the structure of a "
          "tooth, the kinds of teeth, and how to protect them."),
        H("Structure of a tooth"),
        IMG("f5hbi2-tooth.svg", alt="Vertical section of a tooth showing enamel, dentine, pulp cavity with nerve and blood vessels, cement, gum and jawbone",
            caption="Figure 1. A vertical section of a tooth (schematic)."),
        KEY("Parts of a tooth", "A tooth has a crown above the gum and a root held in the jawbone.", cards=[
            ["Enamel", "The hard white covering of the crown. It is the hardest substance in the body and protects the tooth. It has no living cells."],
            ["Dentine", "A bone-like, living tissue under the enamel. It forms most of the tooth and is softer than enamel."],
            ["Pulp cavity", "The space in the middle. It holds the nerve and blood vessels, which bring food and oxygen and give feeling."],
            ["Cement", "A thin bony layer on the root that fixes the tooth in the jawbone with fibres."],
            ["Gum", "Soft tissue around the neck of the tooth that seals the gap between tooth and bone."],
        ]),
        H("Types of teeth"),
        CODE("""Type       Shape                  Function
Incisor    Flat, chisel-shaped    Cut and bite food
Canine     Pointed                Tear and hold food
Premolar   Flat top with 2 cusps  Crush and grind food
Molar      Large, many cusps      Crush and grind food""", "text", title="The four types of human teeth"),
        T("Humans are **omnivores**, so they have all four types. Premolars and molars have wide tops with bumps called **cusps**, good for grinding. "
          "Molars have more than one root, while incisors and canines have one root."),
        H("Two sets of teeth and the dental formula"),
        T("A child first grows **milk (deciduous) teeth**, 20 in all. They are replaced from about the age of six by **permanent teeth**, 32 in an "
          "adult, though the last four molars (the wisdom teeth) may come late or not at all. Exact ages differ from child to child."),
        T("The **dental formula** shows how many teeth of each type there are in one half of the upper jaw (top line) and one half of the lower jaw (bottom line), in the order incisors, canines, premolars, molars."),
        CODE("""Adult:  I 2/2  C 1/1  PM 2/2  M 3/3
Teeth in one half of both jaws: 2+1+2+3 = 8 above and 8 below = 16
Whole mouth: 16 x 2 = 32 teeth

Child:  I 2/2  C 1/1  PM 0/0  M 2/2
One half: 2+1+0+2 = 5 above and 5 below = 10; whole mouth 20 teeth""", "text", title="Dental formula"),
        EX("Worked example 1: use the dental formula", intro="A person's dental formula is I 2/2, C 1/1, PM 2/2, M 3/3. How many teeth does the mouth have? How many are molars?", steps=[
            S("Count one half of the upper jaw", text="2 + 1 + 2 + 3 = 8."),
            S("Count one half of the lower jaw", text="2 + 1 + 2 + 3 = 8."),
            S("Double for the left and right halves", text="(8 + 8) x 2 = 32 teeth."),
            S("Molars", text="3 above and 3 below on each side: (3 + 3) x 2 = 12 molars."),
        ]),
        H("Dental decay"),
        D("**Dental decay** (caries) is the gradual destruction of the tooth by acid made by bacteria in the mouth.", title="Definition: dental decay"),
        T("Bacteria live in the mouth. They gather with food remains and saliva on the teeth as a sticky film called **plaque**. The bacteria feed on sugar "
          "from food and drink and release acid. The acid dissolves the calcium salts of the enamel, making a hole (a cavity). If the hole is not treated, bacteria "
          "reach the dentine and then the pulp cavity, where they irritate the nerve and cause toothache. The tooth may be lost, and infection can spread."),
        KEY("How decay happens", "Follow the chain from sugar to cavity.", cards=[
            ["1. Plaque forms", "Bacteria, saliva and food remains stick to the teeth."],
            ["2. Bacteria use sugar", "They feed on sugar and starch left in the mouth and make acid."],
            ["3. Enamel dissolves", "The acid removes calcium salts, making a cavity."],
            ["4. Pulp is reached", "The nerve is exposed: toothache, infection, possible tooth loss."],
        ]),
        H("Preventing decay"),
        T("Clean the teeth well with a brush or a chewing stick at least twice a day, and especially before sleeping. Use a toothpaste with fluoride "
          "(fluoride makes enamel stronger). Eat fewer sugary sweets and drinks, and do not snack all day. Eat foods with calcium and vitamin D. See a dentist or health worker "
          "if you have pain or dark holes, and for regular check-ups. Rinsing the mouth with clean water after eating also helps. Gum disease is also caused by "
          "plaque, so cleaning along the gum line matters too."),
        EX("Worked example 2: explain a toothache", intro="Explain why a child who often drinks sugary drinks and rarely brushes may get toothache.", steps=[
            S("Plaque", text="Without brushing, plaque stays on the teeth."),
            S("Acid", text="The bacteria in plaque change the sugar into acid."),
            S("Damage", text="Acid dissolves the enamel and forms a cavity which reaches the dentine and pulp. The nerve in the pulp sends pain signals."),
        ]),
        MISTAKE("Saying bacteria eat the tooth", "The bacteria do not chew the tooth. They make **acid** from sugar, and the acid dissolves the enamel."),
        MISTAKE("Putting the nerve in the dentine", "The nerve and blood vessels are in the pulp cavity at the centre. Dentine is hard tissue around it."),
        MISTAKE("Mixing the dental formula", "The numbers are for one side only, top over bottom. Remember to double the total for the whole mouth."),
        TIP("Paper 1 may give a labelled tooth and ask you to name enamel, dentine or pulp; Paper 2 may ask for the cause and prevention of dental decay. This lesson gives general oral health advice and is not a diagnosis."),
        QUIZ("Which part of the tooth contains the nerve and blood vessels?", ["Enamel", "Dentine", "Pulp cavity", "Cement"], 2,
             "The pulp cavity in the centre holds the nerve and blood vessels.",
             hint="It is the hollow space in the centre.",
             feedback=["Enamel is the hard outer covering.", "Dentine surrounds the pulp.", "", "Cement fixes the root to the jawbone."]),
        QUIZ("Which type of tooth is used to tear food?", ["Incisor", "Canine", "Molar", "Premolar"], 1,
             "Canines are pointed and tear and hold food.",
             hint="Think of the pointed teeth beside the incisors.",
             feedback=["Incisors cut and bite.", "", "Molars crush and grind.", "Premolars crush and grind."], title="Quick check 2"),
        PQ("Name the four types of teeth and give the function of each.",
           "Incisors cut and bite, canines tear and hold, premolars and molars crush and grind food."),
        PQ("State two functions of the enamel of a tooth.",
           "It is very hard, so it protects the softer dentine and pulp from wear, and it resists the acid in the mouth for a long time before it is dissolved."),
        PQ("Explain how eating sweets and not brushing may lead to dental decay.",
           "Plaque forms, bacteria in it use the sugar and make acid, the acid dissolves calcium salts in enamel, and a cavity forms. Without treatment it reaches the pulp and causes toothache."),
        PQ("Give three ways of caring for the teeth.",
           "Brush or use a chewing stick after meals and before bed, use fluoride toothpaste, eat fewer sweets and sugary drinks, and visit a dentist for check-ups."),
        SUM("A tooth has enamel on the crown, dentine below it, a pulp cavity with nerves and vessels, cement on the root, held in the jawbone and gum.",
            "Incisors cut, canines tear, premolars and molars grind. The adult dental formula is I 2/2, C 1/1, PM 2/2, M 3/3, giving 32 teeth.",
            "Bacteria in plaque change sugar into acid, which dissolves enamel and causes decay.",
            "Prevent decay by cleaning the teeth well, using fluoride, cutting down on sugar and seeing a dentist."),
    ],
))

# ------------------------------------------------------------------ 4. Digestion
LESSONS.append(lesson(
    module=NUT,
    topic="Digestion",
    title="Digestion: peristalsis and the enzymes of the gut",
    slug="hbi2-digestion",
    minutes=24,
    summary="How food moves along the gut by peristalsis and is broken down by amylase, proteases and lipase, with the roles of stomach acid, bile and the pancreas, region by region.",
    objectives=[
        "Name the parts of the digestive system and state what happens in each",
        "Describe peristalsis and explain why it is needed",
        "State the enzyme, substrate, product and site for starch, protein and fat digestion",
        "Explain the roles of hydrochloric acid, bile and pancreatic juice",
    ],
    key_concepts=["Ingestion", "Digestion", "Peristalsis", "Amylase", "Protease", "Lipase", "Bile", "Hydrochloric acid", "Pancreatic juice"],
    blocks=[
        H("Introduction"),
        T("When you eat a plate of rice and fish, the food is far too big and too complex to pass into the blood. It has to be broken into "
          "small, soluble molecules first. This is **digestion**. It happens in a long tube, the **alimentary canal** (gut), helped by organs such as the liver and pancreas."),
        D("**Digestion** is the breakdown of large insoluble food molecules into small soluble molecules that can be absorbed into the blood.", title="Definition: digestion"),
        T("There are two kinds. **Mechanical digestion** is physical: chewing and the churning of the stomach cut food into small pieces. **Chemical digestion** "
          "uses **enzymes**, which are biological catalysts (they speed up reactions without being used up). Enzymes were studied in a previous module."),
        IMG("f5hbi2-digestive-system.svg", alt="Labelled diagram of the human digestive system from mouth to anus including liver, gall bladder, stomach, pancreas, small and large intestine",
            caption="Figure 1. The digestive system (schematic, not to scale)."),
        H("The journey of food"),
        KEY("From mouth to anus", "The main stages of feeding are:", cards=[
            ["Ingestion", "Taking food into the mouth."],
            ["Digestion", "Breakdown of food by chewing and enzymes."],
            ["Absorption", "Digested food passes into the blood and lymph (next lesson)."],
            ["Assimilation", "Cells use the absorbed food to build tissues or release energy."],
            ["Egestion", "Undigested food leaves the body as faeces through the anus."],
        ]),
        H("Peristalsis"),
        D("**Peristalsis** is a wave of muscle contraction along the wall of the gut that pushes food forward.", title="Definition: peristalsis"),
        T("The wall of the oesophagus and intestine has two layers of muscle. Circular muscles go around the tube, and longitudinal muscles run along it. "
          "Circular muscles behind the food contract and squeeze the tube, while the muscles in front relax. A wave of this movement pushes the food along. "
          "This is why a person can swallow food even when standing on his head. It also mixes the food with enzymes."),
        H("Enzymes at work"),
        T("Digestive enzymes work on one kind of food each. Carbohydrases digest carbohydrates, proteases digest proteins and lipases digest lipids. "
          "Digestion starts in the mouth and stomach and is finished in the small intestine."),
        CODE("""Region           Secretion (made by)        What happens
Mouth            Saliva (salivary glands)   Amylase: starch -> maltose.  Chewing: mechanical.
Oesophagus       Mucus                      Peristalsis moves food to the stomach.
Stomach          Gastric juice: pepsin,     Pepsin digests protein to shorter chains (peptides).
                 hydrochloric acid, mucus   Acid kills bacteria and gives the pH pepsin needs.
Duodenum         Bile (liver), pancreatic   Bile emulsifies fat and neutralises acid.
                 juice (pancreas)           Pancreatic amylase, protease and lipase act.
Ileum            Intestinal juice           Maltase: maltose -> glucose. Peptidases: peptides ->
                                            amino acids. Lipase: fats -> fatty acids + glycerol.""", "text", title="Digestion region by region"),
        CODE("""Enzyme      Food (substrate)   Products
Amylase     Starch             Maltose
Maltase     Maltose            Glucose
Protease    Protein            Peptides then amino acids
Lipase      Lipid (fat)        Fatty acids and glycerol""", "text", title="Main enzymes"),
        T("**Pepsin** works best in the acid conditions of the stomach (about pH 2). **Pancreatic and intestinal enzymes** work best in the slightly alkaline "
          "conditions of the small intestine. The stomach makes **hydrochloric acid** to kill harmful microbes in the food and to provide the correct pH for pepsin. "
          "The stomach wall is protected from the acid by a layer of mucus."),
        H("Bile and the pancreas"),
        T("**Bile** is a green liquid made in the liver and stored in the gall bladder. It flows into the duodenum through the bile duct. Bile is **not an enzyme**. "
          "It has two jobs: it neutralises the acid from the stomach so the enzymes of the small intestine can work, and it **emulsifies** fat, "
          "breaking large fat droplets into tiny ones. Small droplets have a large surface area, so lipase can digest them quickly."),
        T("The **pancreas** makes pancreatic juice with amylase, protease (such as trypsin) and lipase, and releases it into the duodenum."),
        EX("Worked example 1: follow a meal of boiled yam and egg", intro="Describe where the starch of the yam and the protein of the egg are digested and what they become.", steps=[
            S("Starch in the mouth", text="Salivary amylase begins to change starch into maltose while the yam is chewed."),
            S("Starch in the small intestine", text="Pancreatic amylase continues the work, and maltase in the ileum changes maltose into glucose."),
            S("Protein in the stomach", text="Pepsin in acid changes the egg protein into shorter peptides."),
            S("Protein in the small intestine", text="Pancreatic protease and then peptidases change peptides into amino acids."),
        ]),
        EX("Worked example 2: why does a fatty meal need bile?", intro="Explain how bile helps in the digestion of the fat in fried plantain chips.", steps=[
            S("Neutralise", text="Bile makes the contents of the duodenum slightly alkaline, which suits the enzymes."),
            S("Emulsify", text="Bile breaks the fat into tiny droplets without changing it chemically."),
            S("Surface area", text="Tiny droplets have a much larger total surface area for lipase to act on."),
            S("Products", text="Lipase changes fat into fatty acids and glycerol."),
        ]),
        MISTAKE("Calling bile an enzyme", "Bile contains no enzymes. It emulsifies fat (physical change) and neutralises acid. The enzyme for fat is lipase."),
        MISTAKE("Saying digestion and absorption are the same", "Digestion breaks food down into small molecules. Absorption is the passage of these molecules into the blood. Egestion removes undigested waste."),
        MISTAKE("Confusing egestion and excretion", "Egestion is getting rid of undigested food (faeces) that has never been inside body cells. Excretion is getting rid of waste made by cells, such as urea and carbon dioxide."),
        TIP("Paper 1 often asks you to match an enzyme to its substrate or site, or to say what bile does. Learn the table of enzymes and products. For Paper 2, name the gland, the juice, the enzyme and the products in order."),
        QUIZ("Which enzyme digests protein in the stomach?", ["Amylase", "Pepsin", "Lipase", "Maltase"], 1,
             "Pepsin is the protease of the stomach and works in acid.",
             hint="Which enzyme works best at about pH 2?",
             feedback=["Amylase digests starch.", "", "Lipase digests fats.", "Maltase digests maltose to glucose."]),
        QUIZ("What is the main function of bile?", ["To digest protein", "To digest starch", "To emulsify fats and neutralise acid", "To kill bacteria with acid"], 2,
             "Bile emulsifies fat and neutralises stomach acid. It has no enzymes.",
             hint="Bile is not an enzyme.",
             feedback=["Protein is digested by protease.", "Starch is digested by amylase.", "", "Hydrochloric acid in the stomach kills bacteria."], title="Quick check 2"),
        PQ("Define peristalsis and explain why it is necessary.",
           "Peristalsis is a wave of contractions of the circular and longitudinal muscles of the gut wall that pushes food along. It moves food through the gut and mixes it with digestive juices."),
        PQ("State two functions of the hydrochloric acid in the stomach.",
           "It kills bacteria in the food, and it gives the acid pH at which pepsin works best."),
        PQ("Complete: starch is changed to ____ by the enzyme ____ in the mouth, and then to ____ by maltase in the small intestine.",
           "Starch is changed to maltose by amylase, and then to glucose."),
        PQ("Explain why the small intestine is where most digestion is completed.",
           "Bile and pancreatic juice enter the duodenum, and the walls of the ileum also make enzymes. Together they digest starch, protein and fat completely into glucose, amino acids, fatty acids and glycerol, in a slightly alkaline medium."),
        SUM("Digestion breaks large insoluble molecules into small soluble ones, by mechanical and chemical (enzyme) action.",
            "Peristalsis is the wave of muscle contraction that moves food along the gut.",
            "Amylase makes starch into maltose, protease makes protein into amino acids, lipase makes fats into fatty acids and glycerol.",
            "Stomach acid kills germs; bile (from the liver) emulsifies fat and neutralises acid; the pancreas makes enzymes."),
    ],
))

# ------------------------------------------------------------------ 5. Absorption and the liver
LESSONS.append(lesson(
    module=NUT,
    topic="Absorption and the liver",
    title="Absorption in the ileum and the functions of the liver",
    slug="hbi2-absorption-and-the-liver",
    minutes=22,
    summary="How the ileum is adapted for absorption with villi, where absorbed food goes (hepatic portal vein and lacteals), water absorption in the colon, and the main functions of the liver.",
    objectives=[
        "Define absorption and state where it happens",
        "Explain how villi and the ileum are adapted for absorption",
        "Trace the route of glucose and amino acids, and of fatty acids and glycerol, after absorption",
        "State six functions of the liver",
    ],
    key_concepts=["Absorption", "Villus", "Lacteal", "Hepatic portal vein", "Assimilation", "Deamination", "Urea", "Glycogen"],
    blocks=[
        H("Introduction"),
        T("After a meal at the table, the food that was on your plate has been broken into glucose, amino acids, fatty acids, glycerol, vitamins, minerals "
          "and water. These small molecules must now cross the wall of the gut into the blood. This is **absorption**. "
          "The liver then receives the blood and works on what has been absorbed."),
        D("**Absorption** is the movement of digested food molecules (and water, minerals and vitamins) from the gut into the blood or lymph.", title="Definition: absorption"),
        T("Most absorption takes place in the **ileum**, the last part of the small intestine. About 6 to 7 metres is a common figure for the "
          "length of the whole small intestine in an adult, but textbooks differ, so check yours."),
        H("Adaptations of the ileum"),
        IMG("f5hbi2-villus.svg", alt="Diagram of one villus showing epithelium one cell thick, a network of capillaries and a central lacteal",
            caption="Figure 1. A villus: the finger-like fold of the ileum wall (schematic)."),
        KEY("Why the ileum is good at absorbing", "Each feature increases the speed of absorption.", cards=[
            ["Very long", "Gives food a long time and a large area for absorption."],
            ["Folds and villi", "The wall is folded and covered with millions of tiny finger-like **villi**. This gives a huge surface area."],
            ["Thin wall", "The epithelium covering a villus is one cell thick, so molecules have a very short distance to move."],
            ["Rich blood supply", "A network of capillaries in each villus carries away absorbed food quickly. This keeps a steep concentration gradient."],
            ["Lacteal", "A lymph vessel in the centre of each villus absorbs fats."],
        ]),
        T("Absorption uses **diffusion** (movement from a high to a low concentration) and also **active transport** (movement against the gradient, using "
          "energy from respiration). Glucose and amino acids are mostly absorbed by active transport when their concentration in the gut is low. "
          "This is why the cells in the villi have many mitochondria."),
        H("Where the food goes"),
        CODE("""Digested food               Absorbed into               Then goes to
Glucose, amino acids        Capillaries of the villus   Hepatic portal vein -> liver
Vitamins, minerals          Capillaries of the villus   Hepatic portal vein -> liver
Fatty acids and glycerol    Lacteal (lymph vessel)      Lymph -> joins the blood near the heart
Water                       Blood (ileum and colon)     Blood""", "text", title="Route of absorbed food"),
        T("**Fatty acids and glycerol** pass into epithelial cells, are rebuilt into small fat droplets, and enter the lacteal. They travel in the lymph and "
          "join the blood near the heart, so fat reaches the body without going through the liver first."),
        T("**Water** is absorbed both in the small intestine and, mostly what remains, in the **colon** (large intestine). The colon takes back water so that "
          "faeces become semi-solid. If food passes through too quickly, as in diarrhoea, too little water is absorbed and the body can become dried out. "
          "Dehydration from diarrhoea is dangerous for small children, so give oral rehydration solution and seek care."),
        T("After absorption, cells take the nutrients from blood and use them for energy or to build new tissue. This is **assimilation**. Undigested "
          "fibre and dead cells form faeces, stored in the rectum and **egested** through the anus."),
        H("The liver"),
        T("The **liver** is the largest organ inside the body. Blood from the gut arrives in the **hepatic portal vein**, so the liver can control what "
          "reaches the rest of the body. It has many jobs."),
        KEY("Main functions of the liver", "Learn at least six.", cards=[
            ["Regulates blood glucose", "Extra glucose is changed to **glycogen** and stored (under the control of insulin). When glucose is low, glycogen is changed back to glucose."],
            ["Deamination", "Extra amino acids cannot be stored. The liver removes the amino part (the nitrogen) and makes **urea**. The urea goes to the kidneys. The rest is used for energy."],
            ["Makes bile", "Bile is stored in the gall bladder and helps fat digestion."],
            ["Detoxification", "It breaks down alcohol, drugs and many poisons into less harmful substances."],
            ["Stores substances", "Iron and vitamins A and D (and B12) are stored."],
            ["Breaks down old red blood cells", "It makes bile pigments from haemoglobin of worn-out red cells, and stores the iron."],
            ["Makes plasma proteins", "For example, fibrinogen, which is needed for blood clotting."],
        ]),
        EX("Worked example 1: follow a glucose molecule", intro="Describe the route of a glucose molecule from the ileum to a muscle cell.", steps=[
            S("Absorption", text="Glucose is absorbed into a capillary in a villus."),
            S("Hepatic portal vein", text="The blood carries it in the hepatic portal vein to the liver."),
            S("Liver", text="The liver may store some as glycogen, or release it to the blood to keep the level steady."),
            S("To the muscle", text="Blood leaves in the hepatic vein, goes to the heart, and is pumped round the body to the muscle, where glucose is used in respiration."),
        ]),
        EX("Worked example 2: why do we make urea?", intro="A student eats a lot of beans and meat. Explain what the liver does with the extra amino acids.", steps=[
            S("No storage", text="The body cannot store amino acids."),
            S("Deamination", text="The liver removes the nitrogen part (the amine group) from them."),
            S("Result", text="This forms urea, a waste that the blood carries to the kidneys to be excreted in urine. The remaining part is used to give energy or is changed to fat or carbohydrate."),
        ]),
        MISTAKE("Sending all fat to the liver", "Fatty acids and glycerol go into the lacteals and the lymph first, not the hepatic portal vein."),
        MISTAKE("Saying villi 'digest' food", "Villi absorb food. Digestion is done by enzymes in the gut."),
        MISTAKE("Saying the liver stores glucose", "The liver stores glucose as **glycogen**. Glycogen is changed back to glucose when needed."),
        TIP("In Paper 1 expect questions on the adaptations of a villus and on liver functions. In Paper 2 essays, link structure to function: 'thin wall, so short diffusion distance'. This lesson gives general facts about the body and is not medical advice."),
        QUIZ("Which food molecules enter the lacteal?", ["Glucose and amino acids", "Fatty acids and glycerol", "Vitamin C and water", "Urea"], 1,
             "Fats are absorbed into lacteals, the lymph vessels in the villi.",
             hint="Lacteal means 'milky'. Think of the fat droplets.",
             feedback=["Glucose and amino acids go into the capillaries.", "", "Vitamin C goes into the capillaries.", "Urea is a waste made in the liver, not a digested food."]),
        QUIZ("Which is a function of the liver?", ["Making urea from excess amino acids", "Digesting protein with pepsin", "Absorbing glucose", "Making saliva"], 0,
             "The liver changes excess amino acids into urea (deamination).",
             hint="The liver does not make enzymes for digestion.",
             feedback=["", "Pepsin is made in the stomach.", "Absorption is done by the ileum.", "Saliva comes from the salivary glands."], title="Quick check 2"),
        PQ("State three ways in which the villi are adapted for absorption.",
           "They give a very large surface area; the wall is one cell thick for a short diffusion distance; and a network of capillaries removes absorbed food to keep a steep concentration gradient. They also have a lacteal for fats."),
        PQ("Explain what deamination is and why it is needed.",
           "Deamination is the removal of the nitrogen-containing (amino) group from excess amino acids in the liver, forming urea. It is needed because amino acids cannot be stored and the nitrogen must be removed from the body as urea in urine."),
        PQ("Name the blood vessel that carries absorbed glucose to the liver.",
           "The hepatic portal vein."),
        PQ("Give four functions of the liver.",
           "Regulation of blood glucose (storage as glycogen), deamination and making urea, making bile, detoxifying alcohol and drugs, storing iron and vitamins, making plasma proteins, and breaking down old red blood cells (any four)."),
        SUM("Absorption is the passage of digested food into the blood or lymph, mainly in the ileum.",
            "The ileum is long, folded into villi with a thin wall, a rich blood supply and a lacteal.",
            "Glucose and amino acids go by the hepatic portal vein to the liver; fats go into the lacteals.",
            "The liver regulates glucose, makes urea by deamination, makes bile, detoxifies and stores substances."),
    ],
))

# ------------------------------------------------------------------ 6. Breathing and gaseous exchange
LESSONS.append(lesson(
    module=RES,
    topic="Breathing and gaseous exchange",
    title="Breathing and gaseous exchange in the lungs",
    slug="hbi2-breathing-and-gaseous-exchange",
    minutes=24,
    summary="The difference between breathing (moving air in and out by the ribs and diaphragm) and gaseous exchange (diffusion of oxygen and carbon dioxide at the alveoli), with the adaptations of the alveoli.",
    objectives=[
        "Describe the path of air to the alveoli and name the parts of the breathing system",
        "Explain the mechanism of inspiration and expiration using the ribs, intercostal muscles and diaphragm",
        "Explain gaseous exchange at the alveolus and the adaptations that make it efficient",
        "Distinguish clearly between breathing, gaseous exchange and respiration",
    ],
    key_concepts=["Breathing", "Gaseous exchange", "Alveolus", "Diaphragm", "Intercostal muscles", "Diffusion", "Respiration", "Trachea"],
    blocks=[
        H("Introduction"),
        T("Run for a short distance in the school yard and you notice that you breathe faster and deeper. Your muscles need more oxygen, "
          "and your body has to get rid of more carbon dioxide. Two things are happening at once: air is moving in and out of the lungs, and gases are "
          "moving between the air and the blood. Many candidates mix these two ideas. This lesson separates them."),
        D("**Breathing** (ventilation) is the movement of air into and out of the lungs by the action of the ribs, rib muscles and diaphragm.", title="Definition: breathing"),
        D("**Gaseous exchange** is the diffusion of oxygen from the air in the alveoli into the blood, and of carbon dioxide from the blood into the air in the alveoli.", title="Definition: gaseous exchange"),
        D("**Respiration** is the chemical release of energy from food (usually glucose) in cells. It happens in every living cell and is quite different from breathing.", title="Definition: respiration"),
        H("The breathing system"),
        T("Air enters through the nose (or mouth), where hairs and mucus trap dust and germs, and the air is warmed and moistened. It passes down the **trachea** "
          "(windpipe), which is kept open by rings of cartilage. The trachea divides into two **bronchi** (one **bronchus** for each lung). Each bronchus divides into "
          "many small **bronchioles**, which end in tiny air sacs called **alveoli**. The lungs are in the thorax (chest), protected by the ribs. "
          "The **diaphragm** is a sheet of muscle below the lungs, separating the thorax from the abdomen."),
        T("The lining of the trachea and bronchi has **goblet cells** that make sticky mucus, and **cilia** (tiny hairs) that sweep the mucus, with trapped dust and bacteria, up to the throat "
          "to be swallowed or coughed out."),
        H("The breathing mechanism"),
        CODE("""                         INSPIRATION (breathing in)      EXPIRATION (breathing out)
External intercostal     contract                         relax
muscles (between ribs)
Ribs                     move up and out                  move down and in
Diaphragm                contracts and flattens           relaxes and returns to a dome shape
Volume of thorax         increases                        decreases
Pressure in lungs        falls below air pressure         rises above air pressure
Air                      flows in                         is forced out""", "text", title="The breathing mechanism"),
        T("The key idea is pressure. When the volume of the thorax gets bigger, the pressure inside the lungs falls below the pressure of the "
          "air outside, so air is pushed in. When the volume gets smaller, the pressure rises above the outside pressure and air is pushed out. "
          "Air does not flow in because the lungs 'pull' it. It flows in because of the difference in pressure."),
        T("In quiet breathing expiration is passive: the muscles simply relax. In hard exercise, the internal intercostal muscles and abdominal muscles can also contract "
          "to force more air out."),
        H("Gaseous exchange at the alveoli"),
        IMG("f5hbi2-alveolus.svg", alt="An alveolus surrounded by a capillary, with oxygen moving from the air into the blood and carbon dioxide moving the other way",
            caption="Figure 1. Gaseous exchange at an alveolus (schematic)."),
        T("Blood arriving at the lungs from the heart contains little oxygen and a lot of carbon dioxide. The air in the alveoli has more oxygen "
          "and less carbon dioxide than this blood. Gases move by **diffusion**, from high to low concentration. So oxygen diffuses from the alveolus into the "
          "blood, where it is picked up by haemoglobin, and carbon dioxide diffuses from the blood into the alveolus, to be breathed out."),
        KEY("Adaptations of the alveoli", "Each feature makes diffusion faster.", cards=[
            ["Enormous number", "There are millions of alveoli, so the surface area is very large."],
            ["Thin walls", "The wall of an alveolus and the wall of a capillary are each one cell thick, so the diffusion distance is very short."],
            ["Moist lining", "Oxygen dissolves in the thin film of moisture before it diffuses."],
            ["Rich blood supply", "A dense network of capillaries takes oxygen away and brings carbon dioxide, keeping a steep concentration gradient."],
            ["Ventilation", "Breathing constantly replaces the air in the alveoli so the oxygen level stays high."],
        ]),
        CODE("""Gas             Inhaled air (about)   Exhaled air (about)
Nitrogen        78%                   78%
Oxygen          21%                   16%
Carbon dioxide  0.04%                 4%
Water vapour    variable              more (saturated)""", "text", title="Composition of air (rounded teaching values: check your textbook)"),
        T("To show that exhaled air has more carbon dioxide, blow through a straw into **limewater**. It turns cloudy (milky). Limewater stays clear in "
          "air from outside for much longer, because inhaled air has very little carbon dioxide."),
        EX("Worked example 1: explain inspiration", intro="Describe how air enters the lungs when a person breathes in.", steps=[
            S("Muscles", text="The external intercostal muscles contract and the diaphragm contracts and flattens."),
            S("Ribs", text="The ribs move up and out."),
            S("Volume and pressure", text="The volume of the thorax increases, so the pressure in the lungs falls below the air pressure outside."),
            S("Result", text="Air flows into the lungs from the higher pressure outside."),
        ]),
        EX("Worked example 2: why is a heavy runner's breathing fast?", intro="Explain why breathing becomes faster and deeper during exercise.", steps=[
            S("Muscles need more energy", text="Exercising muscles respire faster, using more oxygen and producing more carbon dioxide."),
            S("Carbon dioxide level rises", text="The extra carbon dioxide in the blood is detected by the brain."),
            S("Response", text="The brain sends signals so the breathing muscles work faster and harder. More air moves in and out, so more oxygen is supplied and more carbon dioxide removed."),
        ]),
        MISTAKE("Mixing breathing and gaseous exchange", "Breathing is the movement of air by the ribs and diaphragm. Gaseous exchange is diffusion of gases at the alveoli. Examiners find that many candidates describe breathing when the question asks for gaseous exchange."),
        MISTAKE("Saying we breathe in oxygen only", "Inhaled air is mostly nitrogen. Oxygen is about a fifth of it. Exhaled air still contains much oxygen, about 16 percent."),
        MISTAKE("Mixing respiration with breathing", "Respiration is a chemical process in cells that releases energy. Breathing is a physical movement of air."),
        TIP("For Paper 2, a question on gaseous exchange expects diffusion, a large surface area, thin walls and the blood supply. A question on breathing expects muscles, ribs, volume and pressure in order. Read the question word carefully."),
        QUIZ("What happens to the diaphragm during inspiration?", ["It relaxes and domes upward", "It contracts and flattens", "It moves up with the ribs", "It stays still"], 1,
             "The diaphragm contracts and flattens, which increases the volume of the thorax.",
             hint="Think of what increases the volume of the chest.",
             feedback=["That is what happens during expiration.", "", "The ribs move up and out, but the diaphragm moves down as it flattens.", "The diaphragm is the main muscle of breathing."]),
        QUIZ("By what process does oxygen move from the alveolus into the blood?", ["Peristalsis", "Diffusion", "Digestion", "Respiration"], 1,
             "Oxygen moves from a higher concentration in the alveolus to a lower concentration in the blood by diffusion.",
             hint="It is the movement of particles from high to low concentration.",
             feedback=["Peristalsis is a wave of muscle contraction in the gut.", "", "Digestion is the breakdown of food.", "Respiration releases energy in cells; it is not a movement of gas."], title="Quick check 2"),
        PQ("State three adaptations of the alveoli for gaseous exchange.",
           "A very large surface area from millions of alveoli; walls one cell thick, so the diffusion distance is short; a moist surface; a rich capillary network that keeps a steep concentration gradient."),
        PQ("Describe what happens to the intercostal muscles, ribs and diaphragm during expiration.",
           "The external intercostal muscles relax so the ribs move down and in. The diaphragm relaxes and returns to its dome shape. The volume of the thorax decreases, the pressure rises and air is forced out."),
        PQ("Explain the difference between breathing and gaseous exchange.",
           "Breathing is the movement of air in and out of the lungs using the ribs, intercostal muscles and diaphragm. Gaseous exchange is the diffusion of oxygen into the blood and of carbon dioxide out of the blood across the walls of the alveoli and capillaries."),
        PQ("Describe a simple test that shows exhaled air has more carbon dioxide than inhaled air.",
           "Bubble exhaled air through limewater in one tube and ordinary air through limewater in another. The limewater in the exhaled-air tube turns milky much faster."),
        SUM("Breathing moves air by the action of the intercostal muscles, ribs and diaphragm; it changes the volume and pressure of the thorax.",
            "Gaseous exchange is diffusion of oxygen into the blood and carbon dioxide out of it across the thin walls of the alveoli and capillaries.",
            "Alveoli are adapted by a large surface area, thin walls, moisture and a rich blood supply.",
            "Respiration is the release of energy from food in cells; it is not the same as breathing."),
    ],
))

# ------------------------------------------------------------------ 7. Smoking and carbon monoxide
LESSONS.append(lesson(
    module=RES,
    topic="Smoking and carbon monoxide",
    title="Smoking, tar and carbon monoxide",
    slug="hbi2-smoking-and-carbon-monoxide",
    minutes=20,
    summary="The harmful substances in tobacco smoke (tar, nicotine, carbon monoxide), how they damage the lungs and blood, and the other sources and dangers of carbon monoxide.",
    objectives=[
        "Name the harmful substances in tobacco smoke and state the effect of each",
        "Explain how carbon monoxide reduces the oxygen carried by the blood",
        "Describe the diseases linked with smoking: bronchitis, emphysema, lung cancer and heart disease",
        "Describe how to avoid carbon monoxide poisoning at home and how to reduce harm from smoke",
    ],
    key_concepts=["Tar", "Nicotine", "Carbon monoxide", "Carboxyhaemoglobin", "Bronchitis", "Emphysema", "Lung cancer", "Passive smoking"],
    blocks=[
        H("Introduction"),
        T("Cigarettes are sold in small shops and kiosks in towns all over Cameroon. A cigarette burns tobacco and sends a mixture of hot gases and tiny "
          "particles into the lungs. Some of these substances damage the breathing system and the blood. This lesson explains how, so that you can make healthy choices "
          "and explain the facts in an examination."),
        H("What is in tobacco smoke?"),
        KEY("The three main harmful substances", "Smoke contains thousands of chemicals. Three are the most important at this level.", cards=[
            ["Tar", "A sticky black mixture. It coats the lining of the airways and contains chemicals that can cause **cancer**. It also paralyses and destroys cilia."],
            ["Nicotine", "A drug that is **addictive**, so smokers find it very hard to stop. It makes the heart beat faster and narrows blood vessels, which raises blood pressure."],
            ["Carbon monoxide (CO)", "A poisonous gas. It joins to haemoglobin and reduces the oxygen the blood can carry."],
        ]),
        H("Effects on the lungs"),
        T("In a healthy airway, goblet cells make mucus that traps dust and microbes, and cilia sweep the mucus upward. Tar damages and stops the cilia. "
          "Mucus and trapped germs then stay in the airway and cause infection and coughing (the 'smoker's cough'). Over time the following can develop."),
        CODE("""Disease          What happens
Bronchitis       The bronchi are inflamed and full of mucus. Long coughing. Repeated infection.
Emphysema        The walls of the alveoli break down. Fewer alveoli means a smaller surface
                 for gaseous exchange, so the person is short of breath.
Lung cancer      Chemicals in tar make cells in the lungs divide out of control and form a tumour.
Heart disease    Nicotine and CO raise blood pressure and damage artery walls, helping fat to
                 build up in arteries (see the lesson on atherosclerosis).""", "text", title="Diseases linked with smoking"),
        T("Smoking also harms a pregnant woman and her baby. Carbon monoxide reduces the oxygen reaching the baby, and smoking in pregnancy is linked with a baby of low birth weight."),
        H("How carbon monoxide works"),
        D("**Carboxyhaemoglobin** is the compound formed when carbon monoxide binds to haemoglobin. It does not release the gas easily, so the haemoglobin cannot carry oxygen.", title="Definition: carboxyhaemoglobin"),
        T("Haemoglobin in red blood cells normally joins with oxygen in the lungs to make oxyhaemoglobin. Carbon monoxide joins to haemoglobin much more strongly than oxygen does. "
          "So some of the haemoglobin is blocked, the blood carries less oxygen, and cells receive less oxygen. The smoker may feel tired and breathless, and the heart has "
          "to work harder to supply the body."),
        T("Carbon monoxide has no colour and no smell, so people cannot tell it is there. It is made whenever a fuel such as charcoal, wood, kerosene or petrol "
          "burns with too little oxygen. Cooking on a charcoal stove or running a generator inside a closed room can build up the gas to a dangerous level. "
          "Always cook and run engines in open, ventilated places, and never sleep in a closed room with a burning charcoal stove. In case of dizziness, headache or "
          "confusion, move to fresh air and get medical help. This is general safety advice."),
        H("Passive smoking and giving up"),
        T("**Passive smoking** means breathing in smoke from other people's cigarettes. Children and adults near smokers can have more coughs, chest infections "
          "and asthma attacks. Smoke from tobacco is harmful even for non-smokers. Giving up smoking is hard because of nicotine, but the risks of lung disease, "
          "heart disease and cancer begin to fall once a person stops. A doctor or health centre can help."),
        EX("Worked example 1: why does a heavy smoker get breathless on stairs?", intro="Explain two reasons why a smoker may become short of breath when climbing stairs.", steps=[
            S("Carbon monoxide", text="Some haemoglobin has joined with carbon monoxide, so the blood carries less oxygen to the muscles."),
            S("Damaged lungs", text="If emphysema has developed, there are fewer alveoli, so less oxygen can diffuse into the blood."),
            S("Answer", text="Muscles get less oxygen than they need for the extra effort, so the person breathes harder and feels breathless."),
        ]),
        EX("Worked example 2: why do smokers cough?", intro="Explain how tobacco smoke causes a persistent cough.", steps=[
            S("Cilia", text="Tar paralyses and destroys the cilia that sweep mucus up the airways."),
            S("Mucus builds up", text="The sticky mucus, with dust and bacteria, collects in the bronchi."),
            S("Cough", text="The smoker coughs to clear the mucus, and the airway becomes inflamed and infected."),
        ]),
        MISTAKE("Saying carbon monoxide is carbon dioxide", "They are different gases. Carbon dioxide is made by respiration and carried away in the blood. Carbon monoxide is poisonous and blocks haemoglobin."),
        MISTAKE("Saying nicotine causes cancer", "Tar contains the main cancer-causing chemicals. Nicotine is the addictive drug that raises heart rate and blood pressure."),
        MISTAKE("Thinking only smokers are at risk", "Passive smokers who breathe in the smoke also face risks, and carbon monoxide from stoves and generators can harm anyone."),
        TIP("Paper 1 often asks which substance does which harm (tar, nicotine, carbon monoxide), and Paper 2 may ask you to explain how smoking affects the lungs and blood. Use the words cilia, mucus, alveoli, haemoglobin and oxygen in your answer."),
        QUIZ("Which substance in tobacco smoke combines with haemoglobin and reduces the oxygen it carries?",
             ["Tar", "Nicotine", "Carbon monoxide", "Carbon dioxide"], 2,
             "Carbon monoxide forms carboxyhaemoglobin and blocks oxygen transport.",
             hint="It is a poisonous gas with no smell.",
             feedback=["Tar coats the airways and contains cancer-causing chemicals.", "Nicotine is the addictive drug.", "", "Carbon dioxide is normally carried by the blood and does not block haemoglobin in this way."]),
        QUIZ("Which disease is caused by the breaking down of the walls of the alveoli?",
             ["Bronchitis", "Emphysema", "Asthma", "Tuberculosis"], 1,
             "Emphysema destroys alveolar walls and reduces the surface area for gaseous exchange.",
             hint="Which disease reduces the surface area of the alveoli?",
             feedback=["Bronchitis is inflammation of the bronchi.", "", "Asthma is a narrowing of the airways, often by allergy.", "Tuberculosis is a bacterial infection of the lungs."], title="Quick check 2"),
        PQ("State the effect of tar on the cilia lining the airways and explain what follows.",
           "Tar paralyses and destroys the cilia. Mucus with dust and germs is no longer swept out, so it collects in the airways, causes coughing and infections such as bronchitis."),
        PQ("Explain how carbon monoxide reduces the supply of oxygen to the body.",
           "Carbon monoxide joins to haemoglobin in red blood cells more strongly than oxygen does, forming carboxyhaemoglobin. Less haemoglobin is free to carry oxygen, so cells receive less oxygen."),
        PQ("Give two sources of carbon monoxide in a home and one safety measure.",
           "Burning charcoal, wood or kerosene in a poorly ventilated room, and a petrol generator running indoors. Always cook and use generators outside or in open, ventilated places."),
        PQ("Why is it difficult for a smoker to give up smoking?",
           "Tobacco contains nicotine, an addictive drug. The smoker becomes dependent, so stopping causes cravings."),
        SUM("Tobacco smoke contains tar (cancer, cilia damage), nicotine (addiction, raised heart rate and blood pressure) and carbon monoxide.",
            "Carbon monoxide forms carboxyhaemoglobin and so reduces the oxygen carried by the blood.",
            "Smoking is linked with bronchitis, emphysema, lung cancer, heart disease and low birth weight.",
            "Carbon monoxide can also come from badly ventilated stoves and generators: use them in the open air."),
    ],
))

# ------------------------------------------------------------------ 8. Blood
LESSONS.append(lesson(
    module=RES,
    topic="Blood",
    title="Blood: plasma, cells and clotting",
    slug="hbi2-blood",
    minutes=20,
    summary="The four components of blood (plasma, red cells, white cells, platelets), how each is adapted to its function, and how a clot seals a wound.",
    objectives=[
        "Name the components of blood and give the function of each",
        "Explain how red blood cells are adapted to carry oxygen",
        "Describe how white blood cells defend the body",
        "Describe how blood clots and why clotting matters",
    ],
    key_concepts=["Plasma", "Red blood cell", "Haemoglobin", "White blood cell", "Phagocyte", "Lymphocyte", "Platelet", "Clotting"],
    blocks=[
        H("Introduction"),
        T("A small cut on a finger bleeds for a short time and then stops. A scab forms. In that small event the blood has carried food and oxygen, "
          "fought germs, and sealed a hole. An adult has about five litres of blood. In this lesson you will study what it is made of and what each part does."),
        D("**Blood** is a red liquid tissue that circulates in the blood vessels. It consists of a liquid called **plasma** in which red cells, white cells and platelets are suspended.", title="Definition: blood"),
        KEY("The four components", "If blood is left to stand with a chemical that stops clotting, it separates into layers: plasma on top, then a thin layer of white cells and platelets, then red cells.", cards=[
            ["Plasma", "A pale yellow liquid, a little more than half of the blood volume, mostly water. It carries dissolved substances."],
            ["Red blood cells", "The most numerous cells. They carry oxygen."],
            ["White blood cells", "Fewer in number. They defend the body against disease."],
            ["Platelets", "Small fragments of cells that help blood to clot."],
        ]),
        H("Plasma"),
        T("Plasma is about 90 percent water. It carries many substances: dissolved food (glucose, amino acids), mineral salts, hormones, urea (waste from the liver to the kidneys), "
          "carbon dioxide (mostly as hydrogencarbonate ions), and proteins such as **fibrinogen** (needed for clotting) and antibodies. It also carries heat from warm organs such as the liver and muscles to the rest of the body."),
        H("Red blood cells"),
        T("A red blood cell (erythrocyte) is a small, flexible disc with a dent on each side, a shape called **biconcave**. It has **no nucleus** when mature. "
          "It contains **haemoglobin**, a red protein that has iron. In the lungs, where there is a lot of oxygen, haemoglobin joins with oxygen to form **oxyhaemoglobin**. "
          "In the tissues, where oxygen is low, oxyhaemoglobin releases oxygen to the cells."),
        CODE("""Feature of the red cell      How it helps
Biconcave disc               Large surface area for taking up oxygen
No nucleus                   More room for haemoglobin
Haemoglobin (contains iron)  Joins with oxygen and carries it
Small and flexible           Can squeeze through narrow capillaries
Very many                    Millions in each drop of blood, so much oxygen is carried""", "text", title="Adaptations of the red blood cell"),
        T("Red blood cells are made in the **red bone marrow** (for example in the ribs, sternum, vertebrae and the ends of long bones) and live for roughly four months. "
          "Old cells are broken down in the liver and spleen, and the iron is kept for making new haemoglobin."),
        H("White blood cells"),
        T("White blood cells (leucocytes) have a nucleus and no haemoglobin. They are able to leave the capillaries and move through tissues. There are two main groups."),
        KEY("Two jobs of white cells", "Both protect against microbes.", cards=[
            ["Phagocytes", "They surround bacteria, take them in and digest them. This is called **phagocytosis**. They have a lobed nucleus and can change shape."],
            ["Lymphocytes", "They make **antibodies**, proteins that stick to a specific germ and help to destroy it. Some remain as memory cells, which is why we are protected after an illness or a vaccine."],
        ]),
        H("Platelets and clotting"),
        T("Platelets are fragments of cells with no nucleus. When a blood vessel is cut, platelets collect at the wound and release chemicals. These cause the "
          "soluble plasma protein **fibrinogen** to change to insoluble strands of **fibrin**. The fibrin forms a net across the wound, traps red cells, and "
          "hardens into a **clot**, and then a scab."),
        T("Clotting stops loss of blood and stops germs from entering the wound. People with a clotting disorder such as haemophilia may bleed for much longer. "
          "(Haemophilia is studied in the genetics module.) In the case of severe bleeding, press firmly on the wound with a clean cloth and get medical help."),
        EX("Worked example 1: explain the role of haemoglobin", intro="Explain how haemoglobin helps to supply oxygen to the muscles.", steps=[
            S("In the lungs", text="Oxygen is plentiful, so haemoglobin combines with it to form oxyhaemoglobin (bright red)."),
            S("Transport", text="Red blood cells carry oxyhaemoglobin in the arteries to the muscles."),
            S("In the muscles", text="Oxygen concentration is low, so oxyhaemoglobin releases oxygen, which diffuses into muscle cells for respiration."),
        ]),
        EX("Worked example 2: what happens when a person has a cut on the knee?", intro="Describe how the bleeding stops and how the body defends itself against infection.", steps=[
            S("Platelets", text="Platelets collect at the wound and release chemicals."),
            S("Fibrin", text="Soluble fibrinogen changes to insoluble fibrin threads, which form a net and a clot, and then a scab."),
            S("Defence", text="Phagocytes move to the wound and take in bacteria. Lymphocytes make antibodies against germs that enter."),
        ]),
        MISTAKE("Saying red blood cells have a nucleus", "Mature mammalian red blood cells have no nucleus. White blood cells do."),
        MISTAKE("Saying blood clots because of red cells", "Clotting depends on platelets and the plasma protein fibrinogen changing into fibrin."),
        MISTAKE("Saying plasma is a cell", "Plasma is the liquid part. The cells are the red cells, white cells and platelets (fragments)."),
        TIP("Paper 1 often asks you to match each component of blood to its function or to say which feature of the red blood cell helps it to carry oxygen. In Paper 2 you may be asked to compare red and white cells in a table, so learn shape, nucleus, function and where each is made."),
        QUIZ("Which part of the blood carries oxygen?", ["Plasma", "Red blood cells", "White blood cells", "Platelets"], 1,
             "Haemoglobin in red blood cells carries oxygen as oxyhaemoglobin.",
             hint="Which cells contain haemoglobin?",
             feedback=["Plasma carries dissolved substances such as glucose and urea, and most carbon dioxide.", "", "White blood cells fight germs.", "Platelets help blood to clot."]),
        QUIZ("What do lymphocytes do?", ["Take in bacteria by phagocytosis", "Make antibodies", "Carry oxygen", "Form a clot"], 1,
             "Lymphocytes make antibodies against particular germs.",
             hint="Phagocytes and lymphocytes have different jobs.",
             feedback=["That is the work of phagocytes.", "", "Red blood cells carry oxygen.", "Platelets and fibrin form the clot."], title="Quick check 2"),
        PQ("State two ways in which a red blood cell is adapted to carry oxygen.",
           "It is biconcave, which gives a large surface area; it has no nucleus, giving more room for haemoglobin; it contains haemoglobin which combines with oxygen."),
        PQ("Describe how white blood cells protect the body against disease.",
           "Phagocytes take in and digest bacteria (phagocytosis). Lymphocytes make antibodies that attach to germs and help destroy them."),
        PQ("Explain why blood clotting is important.",
           "It prevents too much blood being lost from a wound, and the clot seals the wound so that bacteria cannot enter."),
        PQ("List four substances carried in the plasma and give one place where each is going.",
           "Glucose from the gut to cells; urea from the liver to the kidneys; carbon dioxide from the tissues to the lungs; hormones from glands to target organs; heat from the liver and muscles to other parts."),
        SUM("Blood has plasma, red cells, white cells and platelets.",
            "Red cells are biconcave with no nucleus and are full of haemoglobin, which carries oxygen as oxyhaemoglobin.",
            "Phagocytes digest germs and lymphocytes make antibodies.",
            "Platelets help fibrinogen change to fibrin, which forms the clot."),
    ],
))

# ------------------------------------------------------------------ 9. Blood groups and transfusion
LESSONS.append(lesson(
    module=RES,
    topic="Blood groups and transfusion",
    title="Blood groups, inheritance and transfusion",
    slug="hbi2-blood-groups-and-transfusion",
    minutes=24,
    summary="The ABO blood groups and Rhesus factor, which groups can safely give blood to which, and how blood groups are inherited from parents.",
    objectives=[
        "Name the antigens and antibodies of the four ABO groups",
        "Work out which donors and recipients are compatible for a transfusion",
        "Explain why the wrong blood causes clumping (agglutination)",
        "Work out the possible blood groups of children from the parents' genotypes",
    ],
    key_concepts=["Antigen", "Antibody", "Agglutination", "ABO system", "Rhesus factor", "Universal donor", "Universal recipient", "Transfusion"],
    blocks=[
        H("Introduction"),
        T("After a road accident or during childbirth, a person may lose so much blood that doctors must replace it. This is a **blood transfusion**. "
          "But blood from one person cannot be given safely to every other person. Blood has to be matched. In this lesson you will learn the rules."),
        D("A **blood group** is a classification of blood based on the presence of certain chemicals (antigens) on the surface of the red blood cells. "
          "A **transfusion** is the transfer of blood from a donor to a recipient.", title="Definitions"),
        H("The ABO system"),
        T("In the ABO system there are four groups: A, B, AB and O. Two substances matter. **Antigens** are proteins on the surface of red blood cells. "
          "**Antibodies** are proteins in the plasma that attach to foreign antigens. A person never has antibodies against his own antigens."),
        CODE("""Blood group   Antigens on red cells   Antibodies in plasma
A             A                      anti-B
B             B                      anti-A
AB            A and B                none
O             none                   anti-A and anti-B""", "text", title="The ABO blood groups"),
        T("If the recipient has an antibody that matches an antigen on the donor's red cells, the antibody joins the cells together in clumps. This is **agglutination**. "
          "The clumps block small blood vessels and can be fatal. So a donor's red cells must not carry an antigen that the recipient has an antibody against."),
        CODE("""Donor group      Can safely give red cells to
O                O, A, B and AB   (universal donor)
A                A and AB
B                B and AB
AB               AB only

Recipient group  Can safely receive red cells from
AB               AB, A, B and O   (universal recipient)
A                A and O
B                B and O
O                O only""", "text", title="Compatibility for transfusion of red cells"),
        T("Group O red cells have no A or B antigens, so no recipient has an antibody against them. Group O is therefore called the **universal donor**. "
          "Group AB people have no anti-A or anti-B antibodies, so they can receive red cells of any group and are called **universal recipients**. In real hospitals, the blood "
          "of the donor and patient is always tested and matched, and donated blood is screened for infections such as HIV and hepatitis."),
        H("The Rhesus factor"),
        T("Another antigen on red cells is the **Rhesus (Rh) factor**. People who have it are **Rhesus positive (Rh+)** and those without it are **Rhesus negative (Rh-)**. "
          "An Rh- person does not naturally have anti-Rh antibodies, but may make them if Rh+ blood is given. So Rh- patients should receive Rh- blood. "
          "Rhesus differences between a mother and her baby also need care in pregnancy; antenatal clinics test for this."),
        H("Inheritance of blood groups"),
        T("The ABO group is controlled by one gene with three alleles: I-A, I-B and i (written here as A, B and O to keep things simple). "
          "A and B are **codominant** (both show when together), and O is **recessive**. Each person has two alleles, one from each parent."),
        CODE("""Phenotype (group)   Possible genotypes
A                   AA or AO
B                   BB or BO
AB                  AB
O                   OO""", "text", title="ABO genotypes"),
        EX("Worked example 1: a cross between AO and BO", intro="A father is group A (genotype AO) and a mother is group B (genotype BO). What groups can their children have?", steps=[
            S("Gametes", text="Father: A or O. Mother: B or O."),
            S("Combine", text="A with B gives AB. A with O gives AO (group A). O with B gives BO (group B). O with O gives OO (group O)."),
            S("Answer", text="All four groups are possible: AB, A, B and O, each with a chance of 1 in 4."),
        ]),
        EX("Worked example 2: a group AB parent and a group O parent", intro="One parent is AB and the other is O. Can they have a child with group AB or O?", steps=[
            S("Gametes", text="AB parent: A or B. O parent: O only."),
            S("Combine", text="A with O gives AO (group A). B with O gives BO (group B)."),
            S("Answer", text="Their children can only be group A or group B. A child of group AB or O is not possible."),
        ]),
        EX("Worked example 3: choose a donor", intro="A patient in a hospital in Bafoussam is group B. A relative with group A offers to give blood. Is this safe? Which groups could give?", steps=[
            S("Patient's antibodies", text="Group B has anti-A antibodies."),
            S("Donor's antigens", text="Group A red cells carry the A antigen, so the patient's anti-A antibodies would make them clump."),
            S("Answer", text="It is not safe. Group B or group O red cells could be given (and the hospital will still test and match the blood)."),
        ]),
        MISTAKE("Mixing up antigens and antibodies", "Antigens are on the red cells. Antibodies are in the plasma. Group A has A antigens and anti-B antibodies, not anti-A."),
        MISTAKE("Saying group O can receive any blood", "Group O has both antibodies, so it can only receive group O. It is group AB that can receive red cells of any group."),
        MISTAKE("Forgetting O is recessive", "A person of group A may be AA or AO. Two parents of group A can have a child of group O if both are AO."),
        TIP("Paper 1 often asks which blood group is the universal donor, or who can donate to a patient of a given group. Paper 2 questions use genetic crosses: write the parents' genotypes, the gametes, then combine them in a Punnett square. This lesson is for learning; in real life a hospital always matches blood by test."),
        QUIZ("Which blood group is called the universal donor?", ["A", "B", "AB", "O"], 3,
             "Group O red cells have no A or B antigens, so they do not meet a matching antibody.",
             hint="Which group has no antigens on its red cells?",
             feedback=["Group A cells have the A antigen, so group B and O recipients would clump them.", "Group B cells carry the B antigen.", "Group AB has both antigens and can only give to AB.", ""]),
        QUIZ("A person has blood group AB. Which antibodies are in the plasma?", ["Anti-A only", "Anti-B only", "Both anti-A and anti-B", "None"], 3,
             "Group AB has both antigens, so the plasma has no antibody against A or B.",
             hint="A person does not make antibodies against his own antigens.",
             feedback=["Anti-A would clump the person's own A cells.", "Anti-B would clump the person's own B cells.", "That is group O.", ""], title="Quick check 2"),
        PQ("Explain why a patient of group A must not be given blood of group B.",
           "Group A plasma contains anti-B antibodies. Group B red cells carry B antigens, so the anti-B antibodies would make them stick together (agglutination), blocking blood vessels."),
        PQ("Two parents are both group A with genotype AO. Show the possible blood groups of their children.",
           "Gametes: A or O from each parent. Children: AA (A), AO (A), AO (A), OO (O). So three out of four are group A and one out of four is group O."),
        PQ("A child has blood group O. Give the possible genotypes of a group B parent and a group A parent.",
           "The child is OO so each parent gave an O allele. The group B parent must be BO and the group A parent must be AO."),
        PQ("Why is group AB called the universal recipient?",
           "Its plasma has neither anti-A nor anti-B antibodies, so it can receive red cells of any ABO group without agglutination."),
        SUM("Group A has A antigens and anti-B antibodies; B has B antigens and anti-A; AB has both antigens and no antibodies; O has no antigens and both antibodies.",
            "Wrong transfusion makes red cells clump (agglutination). O is the universal donor and AB is the universal recipient.",
            "A and B are codominant; O is recessive. A child of an AB and an O parent can only be A or B.",
            "Hospitals always test and match blood, check the Rhesus factor and screen donated blood for infections."),
    ],
))

# ------------------------------------------------------------------ 10. The heart and double circulation
LESSONS.append(lesson(
    module=RES,
    topic="The heart and double circulation",
    title="The heart and the double circulation",
    slug="hbi2-heart-and-double-circulation",
    minutes=25,
    summary="The four chambers, valves and vessels of the heart, the path of blood through the lungs and the body (double circulation), and how arteries, veins and capillaries differ.",
    objectives=[
        "Name and locate the chambers, valves and main vessels of the heart in a diagram",
        "Trace the path of blood through the heart, lungs and body in the correct order",
        "Explain why the heart is described as a double pump and why the left ventricle wall is thicker",
        "Compare the structure and function of arteries, veins and capillaries",
    ],
    key_concepts=["Atrium", "Ventricle", "Valve", "Aorta", "Vena cava", "Pulmonary artery", "Pulmonary vein", "Double circulation", "Coronary artery"],
    blocks=[
        H("Introduction"),
        T("Put two fingers on your wrist or neck and you feel your pulse: one beat for each time the heart pumps. The heart is a muscular organ about the "
          "size of your fist, behind the ribs. It beats without rest all through your life and pushes blood round a network of tubes."),
        D("The **circulatory system** is made of the heart, the blood vessels and the blood. It transports oxygen, food, waste and heat around the body.", title="Definition: circulatory system"),
        H("Structure of the heart"),
        IMG("f5hbi2-heart.svg", alt="Vertical section of the heart showing the right and left atria and ventricles, valves, septum and the main vessels",
            caption="Figure 1. The heart seen from the front (schematic). The right side of the body is on the left of the picture."),
        T("The heart has **four chambers**. The two upper chambers are the **atria** (singular **atrium**), which receive blood. The two lower chambers are the "
          "**ventricles**, which pump blood out. A wall of muscle, the **septum**, separates the right side from the left side so that blood with and without oxygen "
          "does not mix."),
        CODE("""Part                Blood vessel connected         Carries
Right atrium        Vena cava (in)                 Deoxygenated blood from the body
Right ventricle     Pulmonary artery (out)         Deoxygenated blood to the lungs
Left atrium         Pulmonary veins (in)           Oxygenated blood from the lungs
Left ventricle      Aorta (out)                    Oxygenated blood to the body""", "text", title="Chambers and vessels"),
        KEY("Valves and why they matter", "Valves make sure blood flows only one way.", cards=[
            ["Tricuspid valve", "Between the right atrium and right ventricle (it has three flaps)."],
            ["Bicuspid (mitral) valve", "Between the left atrium and left ventricle (two flaps)."],
            ["Semilunar valves", "At the start of the aorta and the pulmonary artery. They stop blood from falling back into the ventricles."],
            ["Tendons", "Strong cords that hold the flaps of the atrioventricular valves so they do not turn inside out."],
        ]),
        T("The wall of the **left ventricle** is much thicker than the right. The left ventricle pumps blood to the whole body, a long way and against a high resistance. "
          "The right ventricle only pumps to the nearby lungs, so it needs less force. The heart muscle has its own blood supply, the **coronary arteries**, "
          "which branch from the aorta. If a coronary artery is blocked, part of the heart muscle is short of oxygen."),
        H("Double circulation"),
        IMG("f5hbi2-double-circulation.svg", alt="Scheme of double circulation: the right side of the heart pumps blood to the lungs and the left side pumps it to the body",
            caption="Figure 2. Double circulation (schematic)."),
        D("**Double circulation** means that blood passes through the heart twice in each complete circuit of the body: once in the **pulmonary circulation** (heart to lungs and back) and once in the **systemic circulation** (heart to body and back).", title="Definition: double circulation"),
        KEY("The path of one drop of blood", "Starting at the vena cava:", cards=[
            ["1. Right atrium", "Deoxygenated blood from the body enters from the vena cava."],
            ["2. Right ventricle", "It is pumped through the tricuspid valve and then out through the pulmonary artery."],
            ["3. Lungs", "Gaseous exchange: blood loses carbon dioxide and gains oxygen."],
            ["4. Left atrium", "Oxygenated blood returns by the pulmonary veins."],
            ["5. Left ventricle", "It passes through the bicuspid valve and is pumped out into the aorta."],
            ["6. Body", "Blood supplies the organs, then returns to the vena cava."],
        ]),
        T("Double circulation lets oxygenated blood return to the heart and be pumped again at high pressure to the body. In a single circulation, as in a fish, the blood loses pressure after the gills. "
          "Mammals need a fast supply of oxygen to keep their bodies warm and active."),
        H("Blood vessels"),
        CODE("""Vessel      Carries                         Wall                         Other features
Artery      Blood away from the heart       Thick, muscular, elastic     Narrow lumen; high pressure; pulse
Vein        Blood towards the heart         Thin                         Wide lumen; low pressure; valves
Capillary   Blood between arteries & veins  One cell thick              Very narrow; exchange with cells""", "text", title="Arteries, veins and capillaries"),
        T("Arteries carry blood at high pressure, so their walls are thick and elastic to stand the pressure. Most arteries carry oxygenated blood, but the "
          "**pulmonary artery** carries deoxygenated blood. Most veins carry deoxygenated blood, but the **pulmonary vein** carries oxygenated blood. "
          "So you must use the direction of flow (away from or towards the heart) to define them, not the colour or the oxygen level."),
        T("Capillaries have walls one cell thick, so substances can pass through into the tissue fluid and cells. Veins have valves that stop blood from flowing backwards, "
          "because the blood pressure in them is low."),
        EX("Worked example 1: trace the blood", intro="Name in order the chambers and vessels through which blood flows from the lungs to the muscles of the arm.", steps=[
            S("Back from the lungs", text="Pulmonary vein."),
            S("Chambers", text="Left atrium, bicuspid valve, left ventricle."),
            S("Out", text="Aorta, then arteries branching to the arm, then capillaries in the muscle."),
        ]),
        EX("Worked example 2: why is the wall of the left ventricle thicker?", intro="Explain the difference.", steps=[
            S("Compare the destinations", text="The left ventricle sends blood to the whole body. The right ventricle sends blood only to the nearby lungs."),
            S("Link to force", text="Pushing blood a long way against more resistance needs a more powerful contraction."),
            S("Link to structure", text="A thicker muscle wall gives a stronger contraction, so the left ventricle wall is thicker."),
        ]),
        MISTAKE("Labelling left and right as seen by the viewer", "In a diagram the right atrium and ventricle are drawn on the left of the page because the heart is seen as if looking at a person facing you."),
        MISTAKE("Saying all arteries carry oxygenated blood", "The pulmonary artery carries deoxygenated blood to the lungs. Define arteries as vessels leaving the heart."),
        MISTAKE("Saying blood goes straight from the right to the left side", "The septum prevents this. Blood must go through the lungs first."),
        TIP("Examiners like labelled diagrams of the heart in Paper 2 and flow-of-blood questions in Paper 1. Practise tracing the path from the vena cava until you can do it without looking. Add the valves in the right places."),
        QUIZ("Which chamber of the heart pumps blood into the aorta?", ["Right atrium", "Right ventricle", "Left atrium", "Left ventricle"], 3,
             "The left ventricle pumps oxygenated blood into the aorta and round the body.",
             hint="The aorta carries blood to the whole body.",
             feedback=["The right atrium receives blood from the vena cava.", "The right ventricle pumps to the lungs through the pulmonary artery.", "The left atrium receives blood from the lungs.", ""]),
        QUIZ("Which vessel carries oxygenated blood from the lungs to the heart?", ["Pulmonary artery", "Pulmonary vein", "Vena cava", "Aorta"], 1,
             "The pulmonary vein takes oxygenated blood from the lungs to the left atrium.",
             hint="It is a vein, because it goes toward the heart.",
             feedback=["The pulmonary artery carries blood from the heart to the lungs.", "", "The vena cava brings deoxygenated blood from the body.", "The aorta carries blood from the heart to the body."], title="Quick check 2"),
        PQ("State two differences between an artery and a vein.",
           "An artery carries blood away from the heart at high pressure and has a thick, muscular and elastic wall with no valves. A vein carries blood towards the heart at low pressure, with a thin wall, a wide lumen and valves."),
        PQ("Explain why the heart has valves.",
           "The valves allow blood to flow in one direction only and stop it from flowing backwards, for example from the ventricles into the atria or from the arteries into the ventricles."),
        PQ("Describe the path of blood from the right atrium to the left atrium.",
           "Right atrium, tricuspid valve, right ventricle, pulmonary artery, lungs (capillaries of the alveoli), pulmonary veins, left atrium."),
        PQ("Why is double circulation more efficient than single circulation?",
           "Blood returns to the heart after the lungs and is pumped again, so it reaches the body at high pressure and quickly. Oxygenated and deoxygenated blood are kept separate by the septum."),
        SUM("The heart has four chambers: two atria that receive blood and two ventricles that pump it out. The septum separates right from left.",
            "Right side: vena cava, right atrium, tricuspid valve, right ventricle, pulmonary artery. Left side: pulmonary veins, left atrium, bicuspid valve, left ventricle, aorta.",
            "Double circulation means blood goes through the heart twice per circuit: lungs and body.",
            "Arteries (thick walls, high pressure), veins (valves, low pressure) and capillaries (one cell thick, exchange)."),
    ],
))

# ------------------------------------------------------------------ 11. Hypertension and atherosclerosis
LESSONS.append(lesson(
    module=RES,
    topic="Hypertension and atherosclerosis",
    title="Hypertension and atherosclerosis",
    slug="hbi2-hypertension-and-atherosclerosis",
    minutes=20,
    summary="What blood pressure is, what high blood pressure (hypertension) and fatty deposits in arteries (atherosclerosis) are, their risk factors and the consequences, and healthy ways to prevent them.",
    objectives=[
        "Define blood pressure, hypertension and atherosclerosis",
        "Explain how fatty deposits narrow arteries and lead to a heart attack or stroke",
        "List the risk factors that can be changed and those that cannot",
        "Suggest general ways of lowering the risk",
    ],
    key_concepts=["Blood pressure", "Hypertension", "Atherosclerosis", "Cholesterol", "Thrombosis", "Heart attack", "Stroke", "Risk factor"],
    blocks=[
        H("Introduction"),
        T("A health worker at a clinic wraps a cuff round your arm and pumps it up. She reads two numbers, for example 120 over 80. These numbers are your **blood pressure**. "
          "High blood pressure is common in many countries, including ours, and people often have it without feeling ill. Knowing the facts helps people to protect themselves. "
          "This lesson gives general information, not diagnosis or treatment: always see a health worker for your own health."),
        D("**Blood pressure** is the force with which blood pushes against the walls of the arteries as the heart pumps. It is measured in millimetres of mercury (mmHg) with two numbers.", title="Definition: blood pressure"),
        T("The first (higher) number is the **systolic** pressure, when the ventricles contract. The second (lower) number is the **diastolic** pressure, when the heart relaxes between beats. "
          "A healthy young adult at rest is often near 120/80 mmHg."),
        H("Hypertension"),
        D("**Hypertension** is a condition in which the blood pressure stays higher than normal over time. Doctors often use readings that stay at or above about 140/90 mmHg, but the exact limits are set by health guidelines, so check the current rules.", title="Definition: hypertension"),
        T("Hypertension often has no signs, so it is called a silent condition. Over many years it makes the heart work harder and damages the walls of arteries. It can lead to "
          "a **stroke**, a **heart attack**, heart failure and kidney damage. For most people no single cause is found. Risk factors include too much salt in the diet, being overweight, lack of exercise, smoking, heavy drinking, long-term stress, and a family history of the disease. "
          "Because it has no signs, adults should have their pressure checked at a clinic from time to time."),
        H("Atherosclerosis"),
        D("**Atherosclerosis** is the build-up of fatty deposits (plaques) containing **cholesterol** in the walls of arteries. The artery becomes narrow and less elastic.", title="Definition: atherosclerosis"),
        KEY("How it develops", "The process takes many years.", cards=[
            ["1. Damage", "The lining of an artery is injured, for example by high blood pressure, smoking or too much fat in the blood."],
            ["2. Deposit", "Cholesterol and fat collect in the damaged wall and form a plaque."],
            ["3. Narrowing", "The plaque makes the lumen narrower, so less blood passes. The wall becomes harder."],
            ["4. Clot", "A clot (**thrombus**) may form on a rough plaque and block the artery completely. This is **thrombosis**."],
        ]),
        T("The harm depends on which artery is blocked. If a **coronary artery** is blocked, part of the heart muscle gets no oxygen and may die. This is a **heart attack** (coronary thrombosis). "
          "If an artery in the brain is blocked, or bursts, it causes a **stroke**. In the legs, it may cause pain when walking."),
        T("The risk of atherosclerosis rises with a diet high in saturated fat (such as fatty meat and some fried foods), smoking, high blood pressure, obesity, lack of exercise, stress, and age. "
          "Family history and sex are risk factors you cannot change. Many others you can change."),
        H("Reducing the risk"),
        CODE("""Risk factor                   What a person can do
Too much salt                 Add less salt; use fewer salty stock cubes and salted fish
Too much saturated fat        Eat less fatty meat and deep-fried food; use less oil
Smoking                       Do not smoke; avoid smoke from others
Overweight / little exercise  Walk, cycle or play sport; control portion size
Stress                        Rest, enough sleep, talk to someone
Alcohol (large amounts)       Drink little or none
Unknown pressure              Have blood pressure checked at a health centre""", "text", title="Lowering the risk"),
        EX("Worked example 1: read a blood pressure", intro="A clinic records a blood pressure of 150/95 mmHg for a man at rest on three separate visits. State the systolic and diastolic values and say what this suggests.", steps=[
            S("Identify the values", text="Systolic 150 mmHg (first number). Diastolic 95 mmHg (second number)."),
            S("Compare", text="Both are above the usual healthy figures near 120/80, and above the 140/90 level commonly used for concern."),
            S("Conclusion", text="The readings suggest hypertension. He should see a doctor, who can confirm it and advise. A student cannot diagnose it from a single reading."),
        ]),
        EX("Worked example 2: how does atherosclerosis lead to a heart attack?", intro="Explain the link between fatty deposits and a heart attack.", steps=[
            S("Narrowed artery", text="Cholesterol forms plaques in the coronary arteries and narrows them."),
            S("Clot", text="A clot forms on a plaque and blocks the artery."),
            S("Heart muscle", text="Part of the heart muscle gets no oxygen or glucose, cannot respire, and the muscle is damaged. This is a heart attack."),
        ]),
        MISTAKE("Saying that hypertension means a fast pulse", "Hypertension is high blood pressure in the arteries, not just a fast heartbeat. A person can have it without any signs."),
        MISTAKE("Saying cholesterol is always bad", "Cholesterol is used to make cell membranes and some hormones. Too much of it in the blood is the problem."),
        MISTAKE("Mixing 'atherosclerosis' and 'thrombosis'", "Atherosclerosis is the fatty build-up in the artery wall. Thrombosis is the blood clot that may then block the artery."),
        TIP("Paper 1 often asks for a cause or a risk factor for heart disease; Paper 2 may ask you to explain how a diet and lifestyle affect the heart. Always link the cause to the effect in steps: fat, plaque, narrowing, clot, heart muscle."),
        QUIZ("What is atherosclerosis?", ["An infection of the heart valves", "A build-up of fatty deposits in artery walls", "A shortage of red blood cells", "A leak between the atria"], 1,
             "Fatty deposits narrow arteries and make them harder.",
             hint="Look at the word 'artery' in the name: it concerns the artery wall.",
             feedback=["That is a different heart problem.", "", "A shortage of red cells or haemoglobin is anaemia.", "A hole between the heart chambers is a heart defect."]),
        QUIZ("Which is a risk factor for hypertension that a person can change?", ["Family history", "Age", "Too much salt in the diet", "Sex"], 2,
             "Diet can be changed. Age, sex and family history cannot be changed.",
             hint="Which one depends on your own choices?",
             feedback=["You cannot change your family history.", "You cannot change your age.", "", "You cannot change your sex."], title="Quick check 2"),
        PQ("Define hypertension and state two possible effects on the body.",
           "Hypertension is blood pressure that stays higher than normal. It can lead to a stroke, a heart attack, heart failure or kidney damage."),
        PQ("Describe how a heart attack can happen.",
           "Cholesterol plaques narrow a coronary artery (atherosclerosis). A clot forms and blocks the artery. The heart muscle beyond the clot receives no oxygen and is damaged."),
        PQ("Give three ways in which a person can reduce the risk of heart disease.",
           "Eat less saturated fat and salt, do not smoke, take regular exercise, avoid being overweight, and have blood pressure checked."),
        PQ("Explain why smoking increases the risk of atherosclerosis.",
           "Nicotine raises blood pressure and carbon monoxide and other chemicals damage the lining of the arteries, so fat is deposited more easily."),
        SUM("Blood pressure is the force of blood on artery walls, measured as systolic over diastolic in mmHg.",
            "Hypertension is blood pressure that stays too high. It is often silent and can cause stroke, heart attack and kidney damage.",
            "Atherosclerosis is a build-up of fatty deposits (cholesterol) in artery walls; a clot (thrombus) can then block the artery.",
            "Lower the risk: less salt and saturated fat, no smoking, exercise, healthy weight, regular blood pressure checks."),
    ],
))

# ------------------------------------------------------------------ 12. The kidney and urine formation
LESSONS.append(lesson(
    module=RES,
    topic="The kidney and urine formation",
    title="The kidney and the formation of urine",
    slug="hbi2-kidney-and-urine-formation",
    minutes=25,
    summary="Excretion and the organs that carry it out, the structure of the urinary system and the nephron, and how urine is made by ultrafiltration and selective reabsorption.",
    objectives=[
        "Define excretion and name the excretory organs and what each removes",
        "Name the parts of the urinary system and of a nephron",
        "Describe ultrafiltration in the glomerulus and selective reabsorption in the tubule",
        "State what urine contains and why glucose and protein are normally absent",
    ],
    key_concepts=["Excretion", "Kidney", "Nephron", "Glomerulus", "Bowman's capsule", "Ultrafiltration", "Selective reabsorption", "Urea", "Urine"],
    blocks=[
        H("Introduction"),
        T("On a hot day after football you drink water and later pass dark yellow urine. After a rainy day with little exercise you pass pale urine. The kidneys are changing the "
          "amount of water and waste that leaves the body. They clean the blood, which is why they are so important."),
        D("**Excretion** is the removal from the body of the waste products of metabolism (the chemical reactions in cells), and of substances in excess.", title="Definition: excretion"),
        CODE("""Organ      Waste removed
Lungs      Carbon dioxide (and water vapour)
Kidneys    Urea, excess water and excess salts, in urine
Skin       Water, a little urea and salts, in sweat
Liver      Makes urea and bile pigments (excreted by kidneys and gut)""", "text", title="Excretory organs"),
        T("Remember: removing undigested food as faeces is **egestion**, not excretion, because the food was never part of the body's cells."),
        H("The urinary system"),
        T("The body has two bean-shaped **kidneys** at the back of the abdomen, one on each side of the backbone. Blood reaches each kidney by the **renal artery** and leaves by the **renal vein**. "
          "Urine leaves the kidney in a tube called the **ureter** and is stored in the **bladder**. When the bladder is full it empties through the **urethra**."),
        T("In a vertical section a kidney has an outer **cortex**, an inner **medulla** and a space called the **pelvis** which collects urine and leads to the ureter. "
          "Each kidney contains about a million tiny filtering tubes called **nephrons** (an approximate figure; check your textbook)."),
        H("The nephron"),
        IMG("f5hbi2-nephron.svg", alt="Diagram of one nephron: Bowman's capsule with the glomerulus, proximal tubule, loop of Henle, distal tubule and collecting duct",
            caption="Figure 1. One nephron (schematic, not to scale)."),
        KEY("Parts of a nephron in order", "The filtrate flows through these parts.", cards=[
            ["Bowman's capsule and glomerulus", "A cup-shaped capsule that surrounds a knot of capillaries (the glomerulus). Blood is filtered here."],
            ["Proximal convoluted tubule", "A coiled tube next to the capsule. Most reabsorption happens here."],
            ["Loop of Henle", "A U-shaped loop that dips into the medulla and helps to reabsorb water."],
            ["Distal convoluted tubule", "A second coiled tube where salts and water are adjusted."],
            ["Collecting duct", "Takes the fluid (urine) from many nephrons to the pelvis."],
        ]),
        H("Stage 1: ultrafiltration"),
        T("Blood enters the glomerulus from the **afferent arteriole**, which is wider than the **efferent arteriole** that carries blood away. "
          "This narrowing makes the blood pressure in the glomerulus very high. The pressure squeezes small molecules out of the blood, through the thin capillary wall and the "
          "capsule lining, into the capsule. This is **ultrafiltration**."),
        CODE("""Passes into the capsule (filtrate)      Stays in the blood
Water                                   Red blood cells
Glucose                                 White blood cells
Amino acids                             Platelets
Urea                                    Large proteins
Mineral salts (e.g. sodium chloride)""", "text", title="What is filtered and what is not"),
        T("Only small molecules can pass. Blood cells and large protein molecules are too big, so they stay in the blood. About a fifth of the plasma is filtered. "
          "The filtrate contains useful substances (glucose, amino acids, salts, much water) as well as urea."),
        H("Stage 2: selective reabsorption"),
        T("The filtrate then flows along the tubule. Useful substances are taken back into the blood in the capillaries that surround the tubule. This is **selective reabsorption**."),
        KEY("Where each substance is taken back", "Reabsorption is selective: the body takes back what it needs.", cards=[
            ["Glucose and amino acids", "All are reabsorbed in the proximal tubule by active transport, which uses energy. The urine of a healthy person has no glucose."],
            ["Water", "Most of the water is reabsorbed in the proximal tubule and the loop of Henle (by osmosis). The amount in the collecting duct is controlled by the hormone ADH."],
            ["Mineral salts", "Reabsorbed as the body needs; the extra goes into urine."],
            ["Urea", "Mostly stays in the tubule, so its concentration in the urine is high."],
        ]),
        T("The fluid that is left, with water, urea and extra salts, flows into the collecting duct and then the ureter. It is **urine**. Urine is about 95 percent water. "
          "The tubule cells have many mitochondria to supply the energy for active transport. They also have microvilli to increase surface area."),
        T("If the kidneys fail, urea and water build up in the blood. A **kidney machine** (dialysis) can do the work of the filter for a patient, or a healthy kidney can be transplanted. "
          "Protein or glucose in urine, found by a health worker's test, can be a sign that something is wrong and needs medical advice."),
        EX("Worked example 1: follow glucose", intro="A healthy person eats a sweet meal. Explain why there is no glucose in the urine although glucose is in the blood.", steps=[
            S("Filtration", text="Glucose is a small molecule, so it is filtered out of the blood into the capsule."),
            S("Reabsorption", text="All of it is taken back into the blood in the proximal tubule by active transport."),
            S("Urine", text="So no glucose is left in the filtrate to leave in the urine."),
        ]),
        EX("Worked example 2: why is there no blood protein in healthy urine?", intro="A health worker finds a lot of protein in a person's urine. Explain why this is unusual.", steps=[
            S("Size", text="Plasma proteins are large molecules. They cannot pass through the filter in the glomerulus."),
            S("Result", text="Protein normally stays in the blood, so healthy urine has none (or only a trace)."),
            S("Meaning", text="Protein in urine suggests the filter may be damaged, so the person should see a doctor."),
        ]),
        MISTAKE("Saying the kidney filters out only waste", "Ultrafiltration is not selective. Useful substances such as glucose are filtered out too. Selective reabsorption brings them back."),
        MISTAKE("Mixing ureter and urethra", "Ureters connect the kidneys to the bladder (two of them). The urethra takes urine from the bladder to the outside (one)."),
        MISTAKE("Confusing urea and urine", "Urea is a waste chemical made in the liver. Urine is the liquid containing urea, water and salts."),
        TIP("Candidates are often asked to label a nephron or to state what is filtered and what is reabsorbed. Learn the order: capsule, proximal tubule, loop of Henle, distal tubule, collecting duct. Link each structure to its function."),
        QUIZ("Which substance is normally NOT found in the filtrate in Bowman's capsule?", ["Glucose", "Urea", "Red blood cells", "Water"], 2,
             "Red blood cells are too big to pass through the filter.",
             hint="Which of these is a cell, not a dissolved substance?",
             feedback=["Glucose is small and is filtered.", "Urea is small and is filtered.", "", "Water is filtered."]),
        QUIZ("Where does most selective reabsorption take place?", ["Glomerulus", "Proximal convoluted tubule", "Ureter", "Bladder"], 1,
             "All the glucose and amino acids and much water are reabsorbed in the proximal tubule.",
             hint="It happens in the tube after the capsule.",
             feedback=["Filtration, not reabsorption, takes place in the glomerulus.", "", "The ureter only carries urine.", "The bladder stores urine."], title="Quick check 2"),
        PQ("Explain how ultrafiltration happens in the glomerulus.",
           "Blood enters through a wide afferent arteriole and leaves through a narrower efferent one, so the pressure in the glomerulus is high. This forces water, glucose, amino acids, urea and salts through the thin capillary wall into Bowman's capsule. Cells and big proteins stay behind."),
        PQ("State what is meant by selective reabsorption and name two substances that are reabsorbed.",
           "It is the taking back into the blood of useful substances from the filtrate in the tubule. Glucose, amino acids, water and salts are reabsorbed."),
        PQ("Name three substances found in urine.",
           "Water, urea and mineral salts."),
        PQ("Why do the cells of the proximal tubule contain many mitochondria?",
           "They carry out active transport to reabsorb glucose and amino acids, which needs energy from respiration, released in mitochondria."),
        SUM("Excretion is the removal of metabolic waste. The kidneys remove urea, excess water and salts as urine.",
            "A nephron has the Bowman's capsule with glomerulus, the proximal tubule, the loop of Henle, the distal tubule and the collecting duct.",
            "Ultrafiltration forces small molecules out of the blood under high pressure; blood cells and proteins stay.",
            "Selective reabsorption returns all the glucose, amino acids and much water and salts to the blood; urine is the rest."),
    ],
))

# ------------------------------------------------------------------ 13. Osmoregulation and thermoregulation
LESSONS.append(lesson(
    module=RES,
    topic="Osmoregulation and thermoregulation",
    title="Osmoregulation, ADH and temperature control by the skin",
    slug="hbi2-osmoregulation-and-thermoregulation",
    minutes=24,
    summary="How the body keeps its water balance (osmoregulation, ADH) and its temperature near 37 degrees C (thermoregulation by the skin), as examples of homeostasis and negative feedback.",
    objectives=[
        "Define homeostasis, osmoregulation and thermoregulation",
        "Explain how ADH controls the concentration of the urine",
        "Describe the structure of the skin and its roles in temperature control",
        "Explain the body's responses to being too hot and too cold",
    ],
    key_concepts=["Homeostasis", "Negative feedback", "Osmoregulation", "ADH", "Hypothalamus", "Thermoregulation", "Sweating", "Vasodilation", "Vasoconstriction"],
    blocks=[
        H("Introduction"),
        T("Whether you spend the day in the cool highlands of Bamenda or in the heat of Maroua, your body temperature stays close to 37 degrees C, and the water content of your blood "
          "stays nearly constant. Keeping the internal conditions steady is called homeostasis. This lesson looks at two examples: water balance and temperature."),
        D("**Homeostasis** is the maintenance of a constant internal environment (such as temperature, water content and blood glucose) in the body.", title="Definition: homeostasis"),
        D("**Negative feedback** is a control system in which a change from the normal level is detected and a response is started that brings the level back to normal.", title="Definition: negative feedback"),
        KEY("Parts of a control system", "Every homeostatic control has the same pattern:", cards=[
            ["Receptor", "Detects the change (for example, temperature or water concentration of the blood)."],
            ["Control centre", "The brain (hypothalamus) compares the level with the normal value."],
            ["Effector", "A muscle or gland that carries out the response (for example, sweat glands or the kidney)."],
            ["Result", "The level returns to normal and the response stops."],
        ]),
        H("Osmoregulation"),
        D("**Osmoregulation** is the control of the water content and the concentration of salts in the blood and body fluids.", title="Definition: osmoregulation"),
        T("If you sweat a lot and drink little, your blood becomes too concentrated (it has too little water). If you drink a large amount of water, it becomes too dilute. "
          "The **hypothalamus**, a part of the brain, contains cells that detect the concentration of the blood. They signal the **pituitary gland** at the base of the brain, "
          "which releases **ADH** (antidiuretic hormone) into the blood."),
        CODE("""                      BLOOD TOO CONCENTRATED            BLOOD TOO DILUTE
                      (not enough water)                (too much water)
Hypothalamus detects  Low water content                 High water content
ADH from pituitary    More ADH released                 Less ADH released
Collecting duct       Becomes more permeable to water   Becomes less permeable to water
Water reabsorbed      More                              Less
Urine                 Small volume, concentrated        Large volume, dilute and pale
Result                Blood water level rises           Blood water level falls""", "text", title="Control of water balance by ADH"),
        T("ADH works on the walls of the **collecting ducts** in the kidney. More ADH makes them more permeable to water, so more water is reabsorbed into the blood. "
          "The urine is then dark and concentrated. When there is plenty of water in the body, little ADH is released and the urine is pale and plentiful. "
          "This is negative feedback, because the response (changing the water reabsorbed) corrects the original change."),
        H("Thermoregulation and the skin"),
        D("**Thermoregulation** is the control of the body's core temperature, which in humans is kept at about 37 degrees C.", title="Definition: thermoregulation"),
        T("The skin has two layers. The outer **epidermis** has a dead surface layer that protects against germs and water loss. The inner **dermis** contains blood capillaries, "
          "sweat glands, hair follicles with tiny **hair erector muscles**, sensory nerve endings and **fat** (in a layer under the skin) which insulates. "
          "The skin's temperature receptors send messages to the hypothalamus, which is also sensitive to the temperature of the blood passing through it."),
        CODE("""                      WHEN TOO HOT                       WHEN TOO COLD
Sweat glands          Make more sweat. Its evaporation   Make little or no sweat
                      takes heat from the skin
Blood vessels (skin)  Vasodilation: widen, more blood    Vasoconstriction: narrow, less blood
                      near the surface, more heat lost   near the surface, less heat lost
Hair erector muscles  Relax: hairs lie flat              Contract: hairs stand up and trap air
Muscles               No shivering                       Shivering: muscles contract and make heat
Behaviour             Seek shade, drink, remove clothes  Put on clothes, move about""", "text", title="Responses of the skin to temperature"),
        T("**Sweating** cools the body because water needs heat to evaporate and takes that heat from the skin. Because sweat contains water and salts, we must drink when we sweat. "
          "**Vasodilation** and **vasoconstriction** are changes in the width of the arterioles that supply the skin capillaries. The capillaries themselves do not move; "
          "it is the arterioles that widen or narrow. Hairs standing on end are more useful in animals with fur than in humans, where the effect is small."),
        EX("Worked example 1: a long walk in the sun", intro="Explain how the body prevents its temperature from rising during a long walk in the heat.", steps=[
            S("Detect", text="The hypothalamus detects the rise in blood temperature, and skin receptors detect heat."),
            S("Sweat glands", text="They make more sweat, and its evaporation cools the skin."),
            S("Blood vessels", text="Skin arterioles widen (vasodilation), so more blood flows near the surface and loses heat by radiation."),
            S("Result", text="The body temperature falls back toward 37 degrees C (negative feedback)."),
        ]),
        EX("Worked example 2: a person drinks very little all day", intro="Describe how the kidney responds and what the urine will be like.", steps=[
            S("Blood concentration", text="The blood becomes too concentrated. The hypothalamus detects this."),
            S("ADH", text="The pituitary releases more ADH. It makes the collecting ducts more permeable to water."),
            S("Urine", text="More water is reabsorbed, so a small volume of dark, concentrated urine is passed. The person should drink more clean water."),
        ]),
        MISTAKE("Saying sweat cools because it is cold", "Sweat is at body temperature. It cools the skin because evaporation takes heat energy from the skin."),
        MISTAKE("Saying capillaries move closer to the surface", "Capillaries do not move. The arterioles that supply them widen (vasodilation) so more blood flows through them, or narrow (vasoconstriction) so less blood flows."),
        MISTAKE("Mixing ADH with insulin or other hormones", "ADH controls water reabsorption in the kidney. It is made by the pituitary gland, not the pancreas."),
        TIP("In Paper 1, look out for questions on what ADH does or which blood vessel change cools the body. In Paper 2, a good answer on temperature control names the receptor (hypothalamus), the effector (sweat glands, skin arterioles, muscles) and the result. Draw a table if the question asks for 'hot' and 'cold' conditions."),
        QUIZ("Which hormone controls how much water is reabsorbed in the collecting ducts?", ["Insulin", "ADH", "Adrenaline", "Thyroxine"], 1,
             "ADH makes the collecting ducts more permeable to water.",
             hint="Its name means 'against urine production'.",
             feedback=["Insulin controls blood glucose.", "", "Adrenaline prepares the body for action.", "Thyroxine controls the metabolic rate."]),
        QUIZ("What happens to the skin arterioles when the body is too hot?", ["Vasoconstriction", "Vasodilation", "They disappear", "They make sweat"], 1,
             "They widen (vasodilation), so more blood flows near the surface and more heat is lost.",
             hint="More heat must be lost, so which way does blood flow change?",
             feedback=["Vasoconstriction conserves heat in cold conditions.", "", "Blood vessels do not disappear.", "Sweat is made by sweat glands."], title="Quick check 2"),
        PQ("Explain how the body responds when the blood becomes too concentrated.",
           "The hypothalamus detects this and the pituitary releases more ADH. The collecting ducts become more permeable, more water is reabsorbed, and a small volume of concentrated urine is produced. The blood becomes less concentrated."),
        PQ("Describe two ways in which the body conserves heat when it is cold.",
           "Vasoconstriction of skin arterioles reduces blood flow near the surface, hairs stand up and trap air, sweating stops, and the muscles shiver to produce heat."),
        PQ("State two functions of the skin other than temperature control.",
           "It protects against germs, injury and water loss; it contains sense organs for touch, pressure, pain and temperature; it excretes some water and salts in sweat; and it makes vitamin D in sunlight."),
        PQ("Why is homeostasis important for the body?",
           "Enzymes and cells work properly only in a narrow range of temperature and water content. Keeping the internal environment constant allows the body to work efficiently."),
        SUM("Homeostasis keeps the internal environment steady by negative feedback.",
            "ADH from the pituitary makes the collecting ducts reabsorb more water when the blood is too concentrated, so urine is small and dark; with plenty of water, less ADH gives plenty of pale urine.",
            "The hypothalamus controls temperature. When hot: sweating and vasodilation. When cold: vasoconstriction, shivering and no sweat.",
            "The skin has the epidermis, dermis with sweat glands, blood capillaries, hair and nerve endings, and a layer of fat."),
    ],
))
