"""Practice sets for Form 5 Food and Nutrition: nutrients, digestion, the kitchen, equipment and hygiene (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "form-5")

M1 = "Basic Nutrition & Digestion"
M2 = "The Kitchen, Equipment & Hygiene"


def q(prompt, right, wrongs, pos, step, concept, skill, hint, diagram="", diagram_alt=""):
    """4-option MC: the correct option is placed at index `pos`; `wrongs` is three (text, why) pairs."""
    opts = [C(t, why=w) for t, w in wrongs]
    opts.insert(pos, C(right, correct=True))
    return MC(prompt, opts, steps=[S("Work it out", text=step)], concept=concept, skill=skill, hint=hint,
              diagram=diagram, diagram_alt=diagram_alt)


SETS = []

# ------------------------------------------------------------------ 1. Proteins
SETS.append(practice_set(
    module=M1, topic="Proteins", title="Proteins and protein deficiency", lesson="fdn1-proteins",
    questions=[
        q("Which nutrient contains nitrogen?", "Protein", [
            ("Carbohydrate", "Carbohydrates contain only carbon, hydrogen and oxygen."),
            ("Fat", "Fats contain only carbon, hydrogen and oxygen."),
            ("Water", "Water is hydrogen and oxygen only.")], 0,
          "Proteins are made of amino acids, which contain nitrogen.", "Protein chemistry", "Recall", "Which nutrient is made of amino acids?"),
        q("What is the main function of protein in the body?", "Growth and repair of body cells", [
            ("Providing the main fuel for the body", "Carbohydrate is the main fuel; protein is used for energy only when the others are short."),
            ("Carrying fat-soluble vitamins", "Fat carries vitamins A, D, E and K."),
            ("Adding bulk to the faeces", "That is the job of dietary fibre.")], 1,
          "Protein builds new cells and repairs worn or damaged ones.", "Functions of protein", "Recall", "It is called a body-building nutrient."),
        q("Which food is a good source of protein of high biological value?", "Eggs", [
            ("Boiled cassava", "Cassava is mostly starch with very little protein."),
            ("Palm oil", "Palm oil is a fat."),
            ("Ripe plantain", "Plantain is mainly carbohydrate.")], 2,
          "Eggs contain all the essential amino acids in good amounts.", "Sources of protein", "Recall", "Look for the animal food."),
        q("Beans and maize are eaten together to give better-quality protein. This is called", "protein complementation", [
            ("protein denaturation", "Denaturation means that heat or acid changes the shape of a protein."),
            ("protein deficiency", "Deficiency means too little protein."),
            ("emulsification", "Emulsification is the breaking of fat into droplets by bile.")], 3,
          "Each food supplies the amino acids that the other lacks, so the mixture is better.", "Protein complementation", "Concept", "What does each food add to the other?"),
        q("A young child has a swollen stomach, swollen feet and thin, pale hair. The likely cause is", "a diet very low in protein", [
            ("a diet very low in vitamin C", "That causes scurvy, with bleeding gums."),
            ("lack of iodine", "That causes goitre, a swollen neck."),
            ("eating too much fat", "That causes obesity, not swelling with poor hair.")], 0,
          "Oedema and poor hair are signs of kwashiorkor, a protein deficiency.", "Kwashiorkor", "Application", "Swelling (oedema) is a key clue."),
        q("How does marasmus differ from kwashiorkor?", "Marasmus shows severe wasting from lack of food overall, with no oedema", [
            ("Marasmus shows oedema and kwashiorkor shows wasting", "It is the other way round."),
            ("Marasmus is caused by too much protein", "Marasmus comes from too little food, including protein."),
            ("Marasmus affects only adults", "It mainly affects infants and young children.")], 1,
          "Marasmus is severe wasting from too little energy and protein; kwashiorkor shows oedema.", "Kwashiorkor and marasmus", "Concept", "One shows swelling and one shows wasting."),
        NUM("A child needs a protein supplement. Using 17 kJ per gram, how many kilojoules does 25 g of protein give?", 425,
            steps=[S("Multiply mass by energy value", math=r"25 \times 17 = 425 \text{ kJ}")], unit="kJ",
            concept="Energy from protein", skill="Calculation", hint="Energy = mass in grams times 17."),
        q("A family cannot afford meat. Which meal gives the best protein quality for the lowest cost?", "Beans with maize and a little dried fish", [
            ("Boiled cassava alone", "Cassava has little protein, so the meal is poor in it."),
            ("Fried plantain with palm oil", "This is mostly carbohydrate and fat."),
            ("Rice with a lot of oil", "This gives plenty of energy but little protein.")], 2,
          "Beans and maize complement each other and a small amount of fish improves the mixture further.", "Planning protein meals", "Application", "Combine plant foods and add a little animal food."),
    ]))

# ------------------------------------------------------------------ 2. Carbohydrates
SETS.append(practice_set(
    module=M1, topic="Carbohydrates", title="Carbohydrates: sugars, starch and energy", lesson="fdn1-carbohydrates",
    questions=[
        q("The main function of carbohydrate is to", "supply energy", [
            ("build and repair cells", "That is protein's main job."),
            ("carry vitamins A and D", "Fats carry fat-soluble vitamins."),
            ("make haemoglobin", "Haemoglobin needs iron and protein.")], 1,
          "Carbohydrates are the body's main source of energy.", "Function of carbohydrate", "Recall", "Think of staple foods such as rice and cassava."),
        q("Which of these is a monosaccharide?", "Glucose", [
            ("Sucrose", "Sucrose is a disaccharide (glucose plus fructose)."),
            ("Starch", "Starch is a polysaccharide."),
            ("Lactose", "Lactose is a disaccharide (milk sugar).")], 0,
          "Glucose is a single sugar.", "Classification", "Recall", "The prefix mono- means one."),
        q("Which food is rich in starch?", "Boiled cocoyam", [
            ("Egg white", "Egg white is protein."),
            ("Cooking oil", "Cooking oil is pure fat."),
            ("Tomato juice", "Tomato juice is mostly water with vitamin C.")], 3,
          "Cocoyam is a starchy staple.", "Sources of starch", "Recall", "Look for a staple root."),
        q("Iodine solution is added to a sample of food. It turns blue-black. The food contains", "starch", [
            ("protein", "Protein is tested for with a different reagent."),
            ("glucose", "Glucose is tested with Benedict's solution (brick-red)."),
            ("fat", "Fat is tested with an emulsion or grease-spot test.")], 2,
          "Iodine turns blue-black in the presence of starch.", "Test for starch", "Concept", "Think about the name of the reagent."),
        NUM("A meal contains 80 g of carbohydrate. Using 17 kJ per gram, calculate the energy from carbohydrate in kilojoules.", 1360,
            steps=[S("Multiply", math=r"80 \times 17 = 1\,360 \text{ kJ}")], unit="kJ",
            concept="Energy from carbohydrate", skill="Calculation", hint="Mass in grams times 17."),
        q("Why can too much sugar cause tooth decay?", "Mouth bacteria change sugar into acid that attacks the enamel", [
            ("Sugar contains fluoride", "Fluoride protects teeth. It is not found in sugar."),
            ("Sugar makes the teeth soft by itself", "Sugar does not soften teeth directly; acid from bacteria does."),
            ("Sugar kills useful bacteria", "The problem is the acid made by bacteria feeding on sugar.")], 0,
          "Bacteria feed on the sugar and produce acid.", "Effects of sugar", "Concept", "What do bacteria in the mouth produce from sugar?"),
        q("A girl eats a lot of sweets and does little exercise. Which is the most likely result over time?", "Obesity", [
            ("Marasmus", "Marasmus comes from too little food."),
            ("Rickets", "Rickets comes from lack of vitamin D."),
            ("Anaemia", "Anaemia comes from lack of iron.")], 1,
          "Extra carbohydrate is stored as fat.", "Excess carbohydrate", "Application", "What happens to energy that is not used?"),
        q("Which choice gives the best snack for a student who wants slow-release energy and some protein?", "Roasted plantain with groundnuts", [
            ("A bottle of sweet soft drink", "It gives sugar only, with no protein."),
            ("A spoon of sugar", "It is a quick burst of sugar with no other nutrients."),
            ("A cup of plain oil", "It is pure fat and does not give a balanced snack.")], 2,
          "Plantain supplies starch and groundnuts add protein.", "Choosing snacks", "Application", "Combine a starchy food with a protein food."),
    ]))

# ------------------------------------------------------------------ 3. Fats and oils
SETS.append(practice_set(
    module=M1, topic="Fats and oils", title="Fats, oils and energy calculations", lesson="fdn1-fats-and-oils",
    questions=[
        q("Which nutrient gives the most energy per gram?", "Fat", [
            ("Protein", "Protein gives about 17 kJ per gram."),
            ("Carbohydrate", "Carbohydrate gives about 17 kJ per gram."),
            ("Fibre", "Fibre is not digested and gives no energy.")], 0,
          "Fat gives about 37 kJ per gram.", "Energy value of fat", "Recall", "It is the most concentrated source."),
        q("Fats are made of", "glycerol and fatty acids", [
            ("amino acids", "Amino acids make protein."),
            ("glucose units", "Glucose units make starch."),
            ("minerals", "Minerals are inorganic nutrients.")], 2,
          "A fat molecule is one glycerol joined to three fatty acids.", "Composition of fat", "Recall", "Think about the chemistry of lipids."),
        q("Which vitamins are fat-soluble?", "A, D, E and K", [
            ("B and C", "These are water-soluble."),
            ("A and C", "Vitamin C is water-soluble."),
            ("B12 and K", "B12 is water-soluble.")], 1,
          "Vitamins A, D, E and K dissolve in fat.", "Fat-soluble vitamins", "Recall", "There are four of them."),
        q("Which of these is a rich source of saturated fat?", "Butter", [
            ("Groundnut oil", "Groundnut oil is mainly unsaturated."),
            ("Boiled beans", "Beans are low in fat."),
            ("Fresh lemon", "Lemon contains almost no fat.")], 3,
          "Butter is animal fat that is solid and high in saturated fat.", "Saturated fat", "Concept", "Think of solid animal fats."),
        NUM("A food contains 10 g of fat. Using 37 kJ per gram, how much energy does the fat give?", 370,
            steps=[S("Multiply", math=r"10 \times 37 = 370 \text{ kJ}")], unit="kJ",
            concept="Energy from fat", skill="Calculation", hint="Mass of fat times 37."),
        NUM("A snack has 10 g of protein, 30 g of carbohydrate and 12 g of fat (invented for practice). Using protein 17, carbohydrate 17 and fat 37 kJ per gram, find the total energy in kJ.", 1124,
            steps=[S("Protein", math=r"10 \times 17 = 170"), S("Carbohydrate", math=r"30 \times 17 = 510"), S("Fat", math=r"12 \times 37 = 444"),
                   S("Add", math=r"170 + 510 + 444 = 1\,124 \text{ kJ}")], unit="kJ",
            concept="Total energy of a food", skill="Calculation", hint="Work out each nutrient separately, then add."),
        q("Why should a person with high blood cholesterol reduce saturated fat?", "It can raise cholesterol and block the arteries", [
            ("It makes the blood too thin", "It does not thin the blood; it is more likely to block arteries."),
            ("It destroys vitamin C", "Fat does not destroy vitamin C."),
            ("It prevents the body from absorbing water", "Fat does not stop water absorption.")], 2,
          "Too much saturated fat raises cholesterol and risks heart disease.", "Health effects of fat", "Application", "Think about the arteries."),
        q("A student says, 'I eat little fat, so I will have no problem with my eyes.' What is wrong with this thought?", "Too little fat can cause a lack of vitamin A, which is fat-soluble", [
            ("Fat has nothing to do with eyes", "Fat helps carry vitamin A, which the eyes need."),
            ("Fat is the only source of iron", "Fat does not supply iron."),
            ("Vitamin A is water-soluble", "Vitamin A is fat-soluble.")], 1,
          "Very low fat intake reduces absorption of fat-soluble vitamins, including A.", "Fat and vitamin absorption", "Reasoning", "Which vitamin protects sight, and what carries it?"),
    ]))

# ------------------------------------------------------------------ 4. Vitamins
SETS.append(practice_set(
    module=M1, topic="Vitamins", title="Vitamins and deficiency diseases", lesson="fdn1-vitamins",
    questions=[
        q("A lack of vitamin C causes", "scurvy", [
            ("rickets", "Rickets is caused by lack of vitamin D."),
            ("beriberi", "Beriberi is caused by lack of vitamin B1."),
            ("night blindness", "Night blindness is caused by lack of vitamin A.")], 0,
          "Vitamin C deficiency causes scurvy, with bleeding gums.", "Vitamin C", "Recall", "Think of bleeding gums."),
        q("Which vitamin is needed for sight in dim light?", "Vitamin A", [
            ("Vitamin B12", "B12 is for blood and nerves."),
            ("Vitamin D", "Vitamin D is for bones."),
            ("Vitamin K", "Vitamin K is for blood clotting.")], 1,
          "Vitamin A is needed for seeing in dim light.", "Vitamin A", "Recall", "Which vitamin do carrots supply?"),
        q("Which food is the best source of vitamin D?", "Oily fish", [
            ("Boiled yam", "Yam is starch with almost no vitamin D."),
            ("Fresh pineapple", "Pineapple is a source of vitamin C."),
            ("Groundnut", "Groundnuts have vitamins E and B but little D.")], 2,
          "Oily fish, eggs and liver contain vitamin D.", "Vitamin D sources", "Recall", "Which foods come from the sea or the hen?"),
        q("Vitamin B12 is found only in", "animal foods", [
            ("citrus fruits", "Citrus fruits provide vitamin C."),
            ("green leaves", "Leaves provide vitamins A, C and K, but no B12."),
            ("vegetable oils", "Vegetable oils provide vitamin E.")], 3,
          "B12 is found only in animal foods such as meat, fish, eggs and milk.", "Vitamin B12", "Concept", "Think of people who eat no animal foods."),
        q("Which vitamin helps the body to absorb iron from plant foods?", "Vitamin C", [
            ("Vitamin D", "Vitamin D helps absorb calcium."),
            ("Vitamin K", "Vitamin K helps blood clot."),
            ("Vitamin E", "Vitamin E is an antioxidant.")], 0,
          "Vitamin C improves iron absorption.", "Vitamin C and iron", "Concept", "Eat leaves with a fruit."),
        q("Which method best saves vitamin C when cooking vegetables?", "Cook briefly in a little water with the lid on", [
            ("Cut them early and soak in water", "Soaking in water washes vitamin C out."),
            ("Boil them for a long time", "Heat destroys vitamin C."),
            ("Add bicarbonate of soda", "Soda destroys vitamin C.")], 1,
          "Short, covered cooking in little water loses the least vitamin C.", "Saving vitamins", "Application", "Water, heat and air destroy vitamin C."),
        q("A diet based almost entirely on polished rice may cause", "beriberi", [
            ("scurvy", "Scurvy comes from lack of vitamin C."),
            ("rickets", "Rickets comes from lack of vitamin D."),
            ("goitre", "Goitre comes from lack of iodine.")], 2,
          "Polishing removes the outer layers of rice, which contain vitamin B1.", "Vitamin B1", "Application", "Which vitamin is lost with the rice husk?"),
        q("A child eats mostly maize. Their skin is rough and they have diarrhoea. The likely deficiency is", "vitamin B3 (niacin)", [
            ("vitamin A", "Vitamin A deficiency affects the eyes."),
            ("vitamin C", "Lack of C affects the gums and healing."),
            ("vitamin K", "Lack of K affects blood clotting.")], 3,
          "Niacin deficiency causes pellagra, linked with maize-based diets.", "Vitamin B3", "Reasoning", "Pellagra gives skin, gut and nerve signs."),
    ]))

# ------------------------------------------------------------------ 5. Minerals
SETS.append(practice_set(
    module=M1, topic="Minerals", title="Minerals and deficiency", lesson="fdn1-minerals",
    questions=[
        q("The mineral needed to make haemoglobin is", "iron", [
            ("calcium", "Calcium builds bones and teeth."),
            ("iodine", "Iodine is for thyroxine."),
            ("sodium", "Sodium balances body fluids.")], 0,
          "Iron is part of haemoglobin.", "Iron function", "Recall", "Anaemia is its deficiency disease."),
        q("A lack of iodine causes", "goitre", [
            ("anaemia", "Anaemia is lack of iron."),
            ("scurvy", "Scurvy is lack of vitamin C."),
            ("rickets", "Rickets is lack of vitamin D or calcium.")], 1,
          "Iodine is needed for the thyroid gland, and its absence causes goitre.", "Iodine", "Recall", "Look at the neck."),
        q("Which is a good source of calcium?", "Milk", [
            ("Palm oil", "Palm oil is a fat."),
            ("Boiled cassava", "Cassava is low in calcium."),
            ("Sugar", "Sugar has no minerals.")], 2,
          "Milk, cheese and small fish with bones provide calcium.", "Calcium sources", "Recall", "Think about foods for strong bones."),
        q("Which pair of nutrients work together for strong bones?", "Calcium and vitamin D", [
            ("Iron and vitamin C", "These work together for blood."),
            ("Sodium and vitamin A", "These do not combine for bones."),
            ("Fluoride and vitamin K", "Fluoride helps teeth; vitamin K helps clotting.")], 0,
          "Vitamin D helps the body to absorb calcium for bone growth.", "Calcium and vitamin D", "Concept", "One is a mineral, one is a vitamin."),
        q("Which mineral protects tooth enamel from decay?", "Fluoride", [
            ("Iron", "Iron is for blood."),
            ("Sodium", "Sodium balances body fluids."),
            ("Iodine", "Iodine is for the thyroid.")], 3,
          "Fluoride makes enamel stronger.", "Fluoride", "Recall", "It is added to some toothpastes."),
        q("A worker sweats heavily and then gets muscle cramps. Which mineral was lost?", "Sodium", [
            ("Iron", "Sweat does not lose much iron."),
            ("Iodine", "Iodine loss does not cause cramps."),
            ("Phosphorus", "Phosphorus is not mainly lost in sweat.")], 1,
          "Sweat contains salt (sodium chloride), and its loss can cause cramps.", "Sodium", "Application", "Salt is in sweat."),
        q("Which meal best helps a girl with anaemia?", "Beans and dark green leaves with a fresh orange", [
            ("White bread and sweet tea", "Little iron, and tea reduces its absorption."),
            ("Fried plantain and soft drink", "Mostly starch and sugar."),
            ("Rice with a lot of oil", "Mainly carbohydrate and fat.")], 0,
          "Beans and leaves supply iron and orange supplies vitamin C, which helps its absorption.", "Preventing anaemia", "Application", "Combine iron foods with vitamin C."),
        q("Why is it unwise to add stock cubes and salt to every dish?", "Too much sodium over a long time can raise blood pressure", [
            ("Salt destroys the proteins in food", "Salt does not destroy protein nutritionally."),
            ("Salt causes goitre", "Goitre is caused by lack of iodine."),
            ("Salt cannot be digested", "Salt dissolves and is absorbed.")], 2,
          "A high sodium intake is linked with high blood pressure.", "Excess sodium", "Reasoning", "Think of long-term health."),
    ]))

# ------------------------------------------------------------------ 6. Water and dietary fibre
SETS.append(practice_set(
    module=M1, topic="Water and dietary fibre", title="Water and dietary fibre", lesson="fdn1-water-and-fibre",
    questions=[
        q("Dietary fibre is mainly made of", "cellulose", [
            ("starch", "Starch is digestible."),
            ("glycogen", "Glycogen is an animal energy store."),
            ("protein", "Protein is a different nutrient.")], 0,
          "Fibre (NSP) is mostly cellulose from plant cell walls.", "What fibre is", "Recall", "It is the material of plant cell walls."),
        q("Which function belongs to dietary fibre?", "It prevents constipation", [
            ("It supplies much energy", "Fibre is not digested, so it gives no energy."),
            ("It builds bones", "Calcium and vitamin D build bones."),
            ("It makes haemoglobin", "Iron makes haemoglobin.")], 1,
          "Fibre adds bulk and keeps the bowel working.", "Fibre functions", "Recall", "Think of the large intestine."),
        q("Which food is the richest source of fibre?", "Beans", [
            ("Sugar", "Sugar contains no fibre."),
            ("Cooking oil", "Oil is pure fat."),
            ("Boiled egg", "Eggs have protein and fat but no fibre.")], 2,
          "Beans are rich in fibre.", "Sources of fibre", "Recall", "Pick the plant food."),
        q("About what fraction of an adult's body is water?", "About two-thirds", [
            ("About one-tenth", "Water makes a much bigger part."),
            ("About one-fifth", "Water makes a much bigger part."),
            ("Almost all of it", "Water is large but not almost all; solids make a third.")], 3,
          "Water is roughly 60 per cent of an adult's body.", "Water in the body", "Recall", "More than half, less than three-quarters."),
        q("Which is NOT a function of water in the body?", "Providing energy", [
            ("Carrying dissolved nutrients in the blood", "This is a real function."),
            ("Cooling the body by sweating", "This is a real function."),
            ("Acting as a lubricant in the joints", "This is a real function.")], 0,
          "Water has no energy value.", "Functions of water", "Concept", "Water is not a fuel."),
        q("A child has severe diarrhoea. Which first step is most helpful at home?", "Give oral rehydration solution (ORS) and seek a health worker if no better", [
            ("Stop giving all fluids", "This worsens dehydration."),
            ("Give only sweet soft drinks", "Too much sugar may make diarrhoea worse; ORS has the right mix."),
            ("Wait and give nothing", "A child can become dehydrated quickly.")], 1,
          "ORS replaces the water and salts lost in diarrhoea.", "Dehydration", "Application", "The child is losing water and salts."),
        q("Which change to a family's diet will best prevent constipation?", "Add vegetables, beans and whole grains and drink enough water", [
            ("Eat only white rice and fish", "These have little fibre."),
            ("Eat fewer vegetables and more sweets", "Sweets have no fibre."),
            ("Drink only tea", "Tea does not supply fibre.")], 2,
          "Fibre adds bulk and water helps it work.", "Preventing constipation", "Application", "Which foods have more cellulose?"),
        q("Why do people who work in the hot sun need more water?", "They lose more water as sweat to keep cool", [
            ("Sweat is mostly fat", "Sweat is mostly water."),
            ("The sun destroys the water in the body", "The body loses it as sweat, not by sunlight directly."),
            ("Heat makes the body store more water", "The opposite happens: more is lost.")], 0,
          "Sweating cools the body, but it loses water, so water must be replaced.", "Water loss", "Reasoning", "What does sweat do for the body?"),
    ]))

# ------------------------------------------------------------------ 7. Digestion and absorption
SETS.append(practice_set(
    module=M1, topic="Digestion and absorption", title="Digestion, enzymes and absorption", lesson="fdn1-digestion-absorption",
    questions=[
        q("The enzyme in saliva that begins the digestion of starch is", "amylase", [
            ("pepsin", "Pepsin acts on protein in the stomach."),
            ("lipase", "Lipase acts on fats."),
            ("trypsin", "Trypsin acts on protein in the small intestine.")], 0,
          "Salivary amylase changes starch to maltose.", "Salivary amylase", "Recall", "It works in the mouth."),
        q("Where does most absorption of digested food take place?", "In the small intestine", [
            ("In the mouth", "Food is only chewed and mixed there."),
            ("In the stomach", "Only a little, such as alcohol, is absorbed in the stomach."),
            ("In the large intestine", "The large intestine absorbs mainly water.")], 1,
          "The ileum has villi and a rich blood supply.", "Site of absorption", "Recall", "Look at the diagram for the longest part."),
        q("The end products of protein digestion are", "amino acids", [
            ("fatty acids", "Fatty acids come from fats."),
            ("glucose", "Glucose comes from carbohydrates."),
            ("glycerol", "Glycerol comes from fats.")], 2,
          "Proteins are split into amino acids.", "End products", "Recall", "Proteins are made of these units."),
        q("Study the figure. Which letter shows the organ that makes bile?", "S", [
            ("P", "P is the mouth."),
            ("R", "R is the stomach, which makes gastric juice."),
            ("U", "U is the small intestine.")], 2,
          "S is the liver, which makes bile.", "Organs of digestion", "Interpretation", "Bile is made by a large organ on the left of the figure.",
          diagram="f5fdn1-digestive-system-lettered.svg",
          diagram_alt="Schematic of the digestive system with the organs marked by letters P to W."),
        q("In the lettered figure, in which structure is most water absorbed from the waste?", "V", [
            ("R", "R is the stomach, which does not mainly absorb water."),
            ("T", "T is the pancreas, which makes juices."),
            ("U", "U is the small intestine, which absorbs digested food.")], 3,
          "V is the large intestine, which absorbs water and forms faeces.", "Large intestine", "Interpretation", "Look for the wide tube at the bottom.",
          diagram="f5fdn1-digestive-system-lettered.svg",
          diagram_alt="Schematic of the digestive system with the organs marked by letters P to W."),
        q("What is the role of bile in digestion?", "It emulsifies fat into small droplets", [
            ("It digests protein", "Bile has no protein enzymes."),
            ("It changes starch to glucose", "That is done by amylase and other enzymes."),
            ("It kills germs in the stomach", "That is the role of stomach acid.")], 1,
          "Bile contains no enzyme. It breaks fat into droplets.", "Bile", "Concept", "Bile makes the surface larger for lipase."),
        q("How do villi help absorption?", "They greatly increase the surface area and have a rich blood supply", [
            ("They make enzymes that digest starch", "Villi absorb; enzymes come from glands and the gut wall."),
            ("They churn the food", "Churning is done by the stomach muscles."),
            ("They store bile", "Bile is stored in the gall bladder.")], 2,
          "A large surface and many blood capillaries make absorption quick.", "Villi", "Concept", "Think of surface area."),
        q("Which sequence correctly lists the path of food through the alimentary canal?", "Mouth, gullet, stomach, small intestine, large intestine, anus", [
            ("Mouth, stomach, gullet, small intestine, large intestine, anus", "The gullet comes before the stomach."),
            ("Mouth, gullet, small intestine, stomach, large intestine, anus", "The stomach comes before the small intestine."),
            ("Mouth, gullet, stomach, large intestine, small intestine, anus", "The small intestine comes before the large intestine.")], 0,
          "Food passes in this order along the tube.", "Path of food", "Reasoning", "Follow the figure from top to bottom."),
    ]))

# ------------------------------------------------------------------ 8. Kitchen layout
SETS.append(practice_set(
    module=M2, topic="Kitchen layout and design", title="Kitchen layouts and design", lesson="fdn1-kitchen-layout",
    questions=[
        q("The three points of the work triangle are", "sink, cooker and refrigerator", [
            ("door, window and table", "These are not the work centres."),
            ("cooker, table and cupboard", "The table and cupboard are not points of the work triangle."),
            ("sink, floor and cupboard", "The floor and cupboard are not the work triangle points.")], 0,
          "The cook moves among storage, preparation and cooking.", "Work triangle", "Recall", "Storage, washing and cooking."),
        q("Look at the figure. Which letter shows a U-shaped kitchen?", "C", [
            ("A", "A is the single-wall layout."),
            ("B", "B has units along two adjacent walls (L shape)."),
            ("D", "D has two facing rows (parallel).")], 2,
          "A U shape has units on three walls.", "Recognise layouts", "Interpretation", "Count the walls with units.",
          diagram="f5fdn1-kitchen-layouts-blank.svg",
          diagram_alt="Four kitchen plans marked A, B, C and D showing a refrigerator F, sink S and cooker C in different arrangements."),
        q("In the figure, which letter shows the parallel (galley) layout?", "D", [
            ("A", "A has units on one wall only."),
            ("B", "B has two adjacent walls."),
            ("C", "C has units on three walls.")], 3,
          "Parallel kitchens have two facing rows with a passage between.", "Recognise layouts", "Interpretation", "Look for two facing rows.",
          diagram="f5fdn1-kitchen-layouts-blank.svg",
          diagram_alt="Four kitchen plans marked A, B, C and D showing a refrigerator F, sink S and cooker C in different arrangements."),
        q("Which layout is most suitable for a very small room with one cook?", "Single-wall", [
            ("U-shaped", "A U shape needs more room."),
            ("Parallel with doors at both ends", "This invites traffic through the work area."),
            ("Island layout", "An island needs a large room.")], 3,
          "All units sit along one wall, so it fits narrow rooms.", "Choosing a layout", "Application", "Think about the space needed."),
        q("Which is the best reason for good ventilation in a kitchen?", "To remove heat, steam, smoke and fumes", [
            ("To make food cook faster", "Ventilation does not change cooking time."),
            ("To keep the floor dry only", "Floors are kept dry by cleaning, not by ventilation."),
            ("To keep insects inside", "Ventilation does not keep insects in.")], 0,
          "Moving air takes away what cooking releases.", "Ventilation", "Concept", "Think of what you smell when frying."),
        q("Which floor covering is the most suitable for a kitchen?", "Non-slip ceramic tiles", [
            ("Polished smooth tiles", "They become slippery when wet."),
            ("Loose carpet", "It absorbs spills and holds germs."),
            ("Untreated wood", "It absorbs water and is hard to clean.")], 1,
          "A kitchen floor should be non-slip, easy to clean and waterproof.", "Flooring", "Application", "Think of wet and greasy floors."),
        q("Artificial lights in a kitchen are best placed", "above the sink, cooker and worktops", [
            ("only in the centre of the ceiling", "Shadows fall on the work areas."),
            ("behind the cook", "The cook's body casts shadows on the work."),
            ("only near the door", "This leaves work areas dark.")], 2,
          "Lights over the work areas avoid shadows and accidents.", "Lighting", "Application", "Where is the work done?"),
        q("A cook walks a long way between the sink and the cooker. What is the best improvement?", "Bring the sink, cooker and refrigerator closer into a compact triangle", [
            ("Move the cooker to the other room", "This makes it worse."),
            ("Add more tables in the middle", "This blocks movement."),
            ("Remove the window", "This does not shorten the walk.")], 0,
          "A compact triangle saves time and effort.", "Planning the triangle", "Reasoning", "Reduce the distance between work centres."),
    ]))

# ------------------------------------------------------------------ 9. Cookers, refrigerators and appliances
SETS.append(practice_set(
    module=M2, topic="Cookers, refrigerators and appliances", title="Cookers, refrigerators and appliances", lesson="fdn1-cookers-fridges-appliances",
    questions=[
        q("Which is the correct way to check a gas hose for a leak?", "Brush soapy water on the joints and look for bubbles", [
            ("Light a match near the joints", "A flame could ignite the leaking gas."),
            ("Switch on the electric light", "A switch can spark and ignite gas."),
            ("Smell the cylinder from close up", "Smelling is a warning but not a safe test; use soapy water.")], 1,
          "Bubbles show where gas is escaping.", "Gas safety", "Concept", "Use a safe liquid, not a flame."),
        q("A refrigerator keeps food cool to", "slow the growth of bacteria", [
            ("kill all bacteria in the food", "Cold does not kill most bacteria."),
            ("cook the food slowly", "Cold does not cook food."),
            ("add vitamins to the food", "A refrigerator adds no nutrients.")], 1,
          "Low temperature slows bacterial growth.", "Purpose of refrigeration", "Recall", "Think of food poisoning."),
        q("Which is the best place for raw meat in a refrigerator?", "The bottom shelf", [
            ("The top shelf above cooked food", "Drips may fall onto the food below."),
            ("Next to the milk on the door", "The door is the warmest place."),
            ("On a plate beside cooked rice", "This risks cross-contamination.")], 3,
          "Drips from raw meat then fall on nothing else.", "Using a refrigerator", "Application", "Think about drips."),
        q("A pressure cooker saves", "time and fuel", [
            ("water and salt only", "It mainly saves time and fuel."),
            ("labour in washing up", "It does not reduce washing up."),
            ("vitamins in all foods", "Vitamins are not saved by it as a rule.")], 0,
          "Steam under pressure raises the boiling temperature, so cooking is faster.", "Pressure cooker", "Concept", "Higher temperature means shorter cooking."),
        q("Which of these should be considered first when buying a refrigerator for a family of eight in a town with frequent power cuts?", "Size, running cost and how it copes with power cuts", [
            ("Only its colour", "Colour has no effect on performance."),
            ("Only the brand name", "A brand does not guarantee suitability."),
            ("How many shelves are painted", "Paint has no effect on performance.")], 2,
          "The family's size and the electricity supply decide the choice.", "Choosing a fridge", "Application", "Which factors affect how well it will serve this family?"),
        q("Which care rule applies to a non-stick pan?", "Use wooden or plastic spoons", [
            ("Scrub it with a metal pad", "Metal scratches the coating."),
            ("Heat it empty on high flame", "Overheating damages the coating."),
            ("Leave it to soak for days", "Soaking is unnecessary and can damage it.")], 2,
          "Soft tools protect the coating.", "Care of utensils", "Recall", "Protect the coating."),
        q("Why are two chopping boards kept in many kitchens, one for raw meat and one for vegetables?", "To prevent cross-contamination", [
            ("To make cutting faster", "Speed is not the reason."),
            ("To use the knives less", "Knives are still used."),
            ("Because boards wear out quickly", "Wear is not the reason.")], 0,
          "Germs from raw meat must not reach ready-to-eat foods.", "Hygiene and equipment", "Reasoning", "Think about germs."),
        q("A family wants a cooker that works during power cuts, heats quickly and is easy to control. The best choice is", "a gas cooker", [
            ("an electric cooker", "It will not work in a power cut."),
            ("an open three-stone fire", "It is slow to control and smoky."),
            ("a microwave oven", "It also needs electricity.")], 3,
          "Gas is independent of electricity and gives instant, controllable heat.", "Choosing a cooker", "Application", "Which fuel does not depend on the power supply?"),
    ]))

# ------------------------------------------------------------------ 10. Hygiene
SETS.append(practice_set(
    module=M2, topic="Personal, food and kitchen hygiene", title="Personal, food and kitchen hygiene", lesson="fdn1-hygiene",
    questions=[
        q("Which is the most important rule of personal hygiene before cooking?", "Wash hands with soap and clean water", [
            ("Wear perfume", "Perfume does not remove germs."),
            ("Wear rings", "Rings trap germs."),
            ("Wipe hands on the apron", "The apron holds germs.")], 1,
          "Handwashing removes germs from the hands.", "Handwashing", "Recall", "Think of soap and water."),
        q("Food poisoning is caused by", "eating food contaminated with harmful germs or poisons", [
            ("eating too much protein", "Excess protein does not cause food poisoning."),
            ("lack of vitamin C", "That causes scurvy."),
            ("eating cold foods", "Cold food is not the cause.")], 2,
          "Contaminated food carries germs or toxins.", "Food poisoning", "Concept", "Think of germs in food."),
        q("Cross-contamination happens when", "germs spread from raw food to cooked food", [
            ("food is cooked for too long", "That is overcooking."),
            ("food is stored in the refrigerator", "A refrigerator slows germs."),
            ("food is washed in clean water", "Washing reduces germs.")], 0,
          "Germs are carried by hands, boards or drips.", "Cross-contamination", "Concept", "Cross means from one thing to another."),
        q("Why should long hair be tied back or covered when cooking?", "So that hairs and germs do not fall into the food", [
            ("To make the cook look smart", "Appearance is not the reason."),
            ("To keep the cook cool", "Heat is not the reason."),
            ("To make cooking faster", "Speed is not the reason.")], 3,
          "Hair carries dirt and germs.", "Personal hygiene", "Application", "Think of what could fall into the pot."),
        q("A cook has a cut on her finger. What should she do before preparing food?", "Cover the cut with a clean waterproof dressing", [
            ("Leave it uncovered so that it dries", "Germs from an open cut can reach the food."),
            ("Cook as normal and wash afterwards", "Germs could already have reached the food."),
            ("Put oil on the cut", "Oil does not protect the food.")], 1,
          "A waterproof dressing stops germs getting into the food.", "Cuts and food handling", "Application", "Protect the wound and the food."),
        q("Cooked rice is left in a pot at room temperature all afternoon. What is the main danger?", "Bacteria multiply to harmful numbers", [
            ("The rice loses all its starch", "Starch is not lost."),
            ("The rice turns into protein", "A food does not change into another nutrient."),
            ("The rice becomes too heavy", "Weight is not the danger.")], 3,
          "Warm, moist food allows bacteria to grow quickly.", "Food storage", "Reasoning", "What do bacteria like?"),
        q("Which is the best way to deal with kitchen waste?", "Put it in a covered bin and empty it daily", [
            ("Leave it open in the corner", "It attracts flies and rats."),
            ("Throw it in the drain", "It blocks the drain and attracts pests."),
            ("Keep it under the sink for a week", "It will rot and smell.")], 1,
          "A lid keeps pests out and daily emptying prevents rot.", "Kitchen hygiene", "Application", "Think about flies and rats."),
        q("Which is the best advice when reheating leftover stew?", "Heat it until steaming hot all through, and do it only once", [
            ("Warm it slightly so that it keeps its taste", "Slight warming may not kill germs."),
            ("Reheat it again and again to be safe", "Repeated reheating gives bacteria more chances to grow."),
            ("Leave it at room temperature to cool slowly", "Slow cooling gives bacteria time to grow.")], 0,
          "Heating until steaming hot kills most bacteria.", "Reheating", "Application", "Think of killing germs without giving them time to regrow."),
    ]))

# ------------------------------------------------------------------ 11. Safety and first aid
SETS.append(practice_set(
    module=M2, topic="Safety and first aid in the kitchen", title="Kitchen safety and first aid", lesson="fdn1-safety-first-aid",
    questions=[
        q("A scald is an injury caused by", "hot liquid or steam", [
            ("dry heat or flame", "That is a burn."),
            ("a sharp knife", "That is a cut."),
            ("electricity", "That is an electric shock.")], 2,
          "A scald comes from hot liquid or steam.", "Scald", "Recall", "Think of boiling water."),
        q("The correct first aid for a minor burn is to", "hold it under cool running water for at least 10 minutes", [
            ("rub butter on it", "Butter traps heat and can cause infection."),
            ("burst the blisters", "This opens the skin to infection."),
            ("cover it with toothpaste", "Toothpaste is not safe on a burn.")], 3,
          "Cooling reduces damage and pain.", "First aid for burns", "Recall", "The treatment starts with cooling."),
        q("Why should pot handles be turned inwards?", "So that nobody knocks them and spills hot contents", [
            ("To heat the pot faster", "It does not affect heating."),
            ("To save gas", "It does not affect gas use."),
            ("To keep the handles clean", "Cleanliness is not the reason.")], 1,
          "Handles that stick out can be knocked or grabbed by a child.", "Preventing scalds", "Concept", "Who might pass by?"),
        q("A pan of cooking oil catches fire. What is the safest action?", "Turn off the heat if safe and cover the pan with a lid or damp cloth", [
            ("Pour water on it", "Water makes burning oil spatter and spread."),
            ("Carry it outside quickly", "Moving it risks burns and spreading the fire."),
            ("Fan the flames", "Air feeds the fire.")], 2,
          "Cutting off the air puts out the fire.", "Fire safety", "Application", "Fires need air."),
        q("What should you do first if someone gets an electric shock from a faulty appliance?", "Switch off the power or unplug it before touching the person", [
            ("Pull the person away with bare hands", "You could be shocked too."),
            ("Pour water on the appliance", "Water conducts electricity and is dangerous."),
            ("Leave the person and wait", "Help is needed, but first make it safe.")], 0,
          "The current must be off before helping.", "Electric shock", "Application", "Make the scene safe first."),
        q("A cut is bleeding. Which action is correct?", "Press on it with a clean cloth and raise the injured part", [
            ("Wash it with strong bleach", "Bleach damages tissue."),
            ("Leave it open to the air", "Open cuts can become infected."),
            ("Pack it with soil", "Soil carries tetanus bacteria.")], 1,
          "Firm pressure with a clean cloth stops bleeding.", "First aid for cuts", "Application", "Press and raise."),
        q("In which case should a burn be seen by a health worker?", "A large burn, or a burn on a child's face", [
            ("A small red patch that cools quickly", "A very minor burn can be treated with cool water."),
            ("A mark that fades in minutes", "This is superficial."),
            ("A dry patch from sunlight", "This is not a kitchen burn.")], 2,
          "Large, deep or facial burns and burns in young children need professional care.", "When to seek help", "Reasoning", "Consider size, place and age."),
        q("Which action is MOST likely to prevent a fall in the kitchen?", "Wiping up spills at once", [
            ("Leaving water on the floor to dry", "Wet floors are slippery."),
            ("Polishing the floor with oil", "Oil makes floors slippery."),
            ("Placing loose mats on wet tiles", "Loose mats can slip.")], 0,
          "A dry floor is not slippery.", "Preventing falls", "Concept", "What makes floors slip?"),
    ]))
