"""A Level Food Science and Nutrition (0740), Upper Sixth: practice sets for Clinical Dietetics & Therapeutic Nutrition,
Community Nutrition, Epidemiology & Food Security and the Examination module.

One 8-question set per lesson (8 topic lessons, 3 examination lessons), plus 'Paper 1 mock exam A' (50 multiple-choice
questions across all five Upper Sixth modules in proportion to their topic counts: 5, 6, 3, 5 and 3 topics give 11, 14,
7, 11 and 7 questions) and 'Paper 2 practice paper A' (25 auto-markable parts in 8 numbered questions, one section A to D
pair each). Food Science has no Paper 3 mock: the Paper 3 lesson and its set cover practical skills. Exam facts are only
those of the Board's 2023 subject report. Mock timings (90 and 150 minutes) are KKEVO practice settings, not Board
settings. Teaching data are labelled invented. Numerical answers were checked by script.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "upper-sixth")

M_ENG = "Food Engineering & Preservation Technology"
M_POST = "Post-Harvest Commodity Technology"
M_QA = "Food Quality Assurance & Legislation"
M_CLIN = "Clinical Dietetics & Therapeutic Nutrition"
M_COMM = "Community Nutrition, Epidemiology & Food Security"
M_EXAM = "Examination"

# Exact topic titles (used as mock concepts)
T_THERM = "Thermal processing kinetics"
T_PAST = "Pasteurization and canning"
T_LOWT = "Low-temperature preservation"
T_DEHY = "Dehydration"
T_IRR = "Irradiation, modified atmosphere packaging and additives"
T_PHYS = "Post-harvest physiology"
T_CER = "Cereals, milling and baking"
T_ROOT = "Roots, tubers and plantain"
T_OIL = "Oilseeds and oils"
T_MEAT = "Meat and dairy"
T_BEV = "Beverages"
T_HACCP = "HACCP"
T_GMP = "GMP and ISO 22000"
T_CODEX = "Codex Alimentarius and Cameroonian food standards"
T_PEM = "Protein-energy malnutrition and obesity"
T_DIAB = "Diabetes mellitus"
T_HYP = "Hypertension and atherosclerosis"
T_RENAL = "Renal and gastrointestinal disorders"
T_CELI = "Celiac disease and lactose intolerance"
T_STATUS = "Nutritional status assessment"
T_FORT = "Fortification and nutrition programmes"
T_FSEC = "Food security policy"


def Q(prompt, correct, wrongs, steps, concept, skill, hint, diagram="", alt=""):
    """Four-option MC spec. `wrongs` = [(text, why)] x3. The position of the correct option is balanced by build()."""
    assert len(wrongs) == 3, prompt
    return {"k": "mc", "prompt": prompt, "correct": correct, "wrongs": wrongs, "steps": steps, "concept": concept,
            "skill": skill, "hint": hint, "diagram": diagram, "alt": alt}


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit="", diagram="", alt=""):
    return {"k": "num", "prompt": prompt, "answer": answer, "steps": steps, "concept": concept, "skill": skill,
            "hint": hint, "tol": tol, "unit": unit, "diagram": diagram, "alt": alt}


def build(specs, seed):
    """Turn specs into MC/NUM questions with the correct option spread evenly over A-D."""
    rng = random.Random(seed)
    counts = [0, 0, 0, 0]
    out = []
    for s in specs:
        st = [S(a, text=b) for a, b in s["steps"]]
        assert s["concept"] and len(s["concept"]) <= 80, s["concept"]
        assert s["hint"] and s["skill"], s["prompt"]
        if s["k"] == "num":
            out.append(NUM(s["prompt"], s["answer"], steps=st, tolerance=s["tol"], unit=s["unit"], concept=s["concept"],
                           skill=s["skill"], hint=s["hint"], diagram=s["diagram"], diagram_alt=s["alt"]))
            continue
        m = min(counts)
        pos = rng.choice([i for i in range(4) if counts[i] == m])
        counts[pos] += 1
        ch = [C(t, why=w) for t, w in s["wrongs"]]
        ch.insert(pos, C(s["correct"], correct=True))
        out.append(MC(s["prompt"], ch, steps=st, concept=s["concept"], skill=s["skill"], hint=s["hint"],
                      diagram=s["diagram"], diagram_alt=s["alt"]))
    return out


SETS = []

ZQ = "alfsu2-zscore-q.svg"
ZQ_ALT = "Normal curve of a reference population with dashed lines at Z of minus 3, minus 2, 0 and plus 2; four regions marked P (below minus 3), Q (between minus 3 and minus 2), R (between minus 2 and 0) and S (at the median)"

# ------------------------------------------------------------------ 1. PEM and obesity
V1 = [
    Q("Which sign best separates kwashiorkor from marasmus?", "Oedema of the feet and legs",
      [("Severe wasting of muscle", "Wasting is present in marasmus and may also be present in kwashiorkor."), ("Low weight for age", "Both forms are underweight."), ("A history of infection", "Infection is a common trigger of both forms.")],
      [("Key sign", "Oedema from low blood albumin is characteristic of kwashiorkor and absent in marasmus.")], T_PEM, "Recall", "Look for fluid in the tissues."),
    Q("A 10-month-old infant is very thin with a wizened face, no oedema and a good appetite. The most likely form of PEM is:", "Marasmus",
      [("Kwashiorkor", "Kwashiorkor has oedema."), ("Marasmic kwashiorkor", "That mixed form also has oedema."), ("Obesity with hidden hunger", "The infant is severely wasted, not overweight.")],
      [("Reasoning", "Severe wasting without oedema points to marasmus: a mainly energy-deficient diet.")], T_PEM, "Application", "Is there oedema?"),
    Q("Why is a starved child given small frequent feeds of a low-energy therapeutic milk in the first stage of treatment?", "Organs such as the heart, kidney and gut work at a reduced level and a large feed can overload them",
      [("The child cannot digest any food at all", "Digestion is reduced, not absent."), ("Therapeutic milk kills the infection", "Feeds do not treat infection; medicines do."), ("Large feeds make the oedema worse in every case", "The reason is metabolic overload, not oedema alone.")],
      [("Stage 1", "Stabilize first, then catch-up growth with F-100 or RUTF.")], T_PEM, "Concept", "Think of the heart and kidneys of a starved child."),
    Q("Ready-to-use therapeutic food (RUTF) is suitable for treatment at home because it:", "Needs no water or cooking and resists bacterial growth",
      [("Is a liquid that needs boiling first", "RUTF is a paste that needs no preparation."), ("Contains only protein", "It contains energy, protein, vitamins and minerals."), ("Is given only in hospital", "Its use at home is a major advantage.")],
      [("Properties", "A peanut-milk-oil-sugar paste with a vitamin and mineral mix, low in water.")], T_PEM, "Concept", "Think of a paste with little water."),
    N("Calculate the BMI of an adult of mass 72 kg and height 1.80 m (to 1 decimal place).", 22.2,
      [("Formula", "BMI = mass ÷ height squared."), ("Calculate", "72 ÷ (1.80 × 1.80) = 72 ÷ 3.24 = 22.2.")], T_PEM, "Calculation", "Square the height first.", tol=0.1, unit="kg/m²"),
    Q("A man has a BMI of 31.5. According to the WHO adult classes he is:", "Obese",
      [("Overweight", "Overweight is 25.0 to 29.9."), ("Normal", "Normal is 18.5 to 24.9."), ("Underweight", "Underweight is below 18.5.")],
      [("Classes", "30.0 or more is obese.")], T_PEM, "Application", "Compare with 30."),
    N("Mifflin-St Jeor: BMR = 10 × mass(kg) + 6.25 × height(cm) − 5 × age + 5 for men. Find the BMR of a man aged 30, 70 kg and 175 cm (kcal per day, nearest whole number).", 1649,
      [("Substitute", "10(70) + 6.25(175) − 5(30) + 5 = 700 + 1093.75 − 150 + 5."), ("Total", "1 648.75, which is 1 649 kcal a day.")], T_PEM, "Calculation", "Compute each term then add.", tol=1, unit="kcal/day"),
    Q("A daily energy deficit of 500 kcal is kept for a week. Using 7 700 kcal per kg of body fat, the expected loss is about:", "0.45 kg",
      [("3.5 kg", "3 500 is the weekly deficit in kcal, not kilograms."), ("4.5 kg", "That divides the wrong way and slips a decimal point."), ("0.045 kg", "That is ten times too small.")],
      [("Weekly deficit", "500 × 7 = 3 500 kcal."), ("Loss", "3 500 ÷ 7 700 = 0.45 kg.")], T_PEM, "Calculation", "Divide the weekly deficit by the energy in 1 kg of fat."),
]
SETS.append(practice_set(module=M_CLIN, topic=T_PEM, title="PEM forms, treatment, BMI and energy deficit", lesson="fsu2-pem-obesity", questions=build(V1, 301)))

# ------------------------------------------------------------------ 2. Diabetes mellitus
V2 = [
    Q("Which hormone is released when blood glucose is low, and where does it act mainly?", "Glucagon, on the liver",
      [("Insulin, on the liver", "Insulin is released when glucose is high."), ("Glucagon, on the muscles only", "Glucagon acts mainly on the liver."), ("Insulin, on the pancreas", "Insulin comes from the pancreas and acts on target cells.")],
      [("Role", "Alpha cells release glucagon, which breaks liver glycogen and makes new glucose.")], T_DIAB, "Recall", "Which hormone raises glucose?"),
    Q("Which cells of the pancreas make insulin?", "Beta cells of the islets of Langerhans",
      [("Alpha cells of the islets", "Alpha cells make glucagon."), ("Acinar cells", "Acinar cells make digestive enzymes."), ("Liver cells", "The liver stores glycogen but does not make insulin.")],
      [("Source", "Beta cells release insulin when blood glucose rises.")], T_DIAB, "Recall", "Alpha, beta: which one lowers glucose?"),
    Q("Which statement is correct for type 1 diabetes?", "It is caused by autoimmune destruction of beta cells and needs insulin injections",
      [("It is mainly caused by obesity and responds to diet alone", "That describes type 2."), ("It is caused by too much insulin", "Insulin is lacking, not excessive."), ("It usually begins in old age", "Type 1 usually begins in children and young people.")],
      [("Type 1", "Little or no insulin is made, so insulin must be injected.")], T_DIAB, "Concept", "Think of the beta cells."),
    Q("Which of these is a feature of type 2 diabetes?", "Insulin resistance in muscle, fat and liver cells",
      [("Immediate and total loss of insulin production", "That describes type 1."), ("Always diagnosed before the age of 15", "Type 2 usually occurs in adults, although it is now seen in young people."), ("Caused by a virus alone", "Type 2 is linked to obesity, inactivity and genetics.")],
      [("Mechanism", "Cells respond poorly to insulin and the pancreas cannot compensate.")], T_DIAB, "Concept", "Think of resistance."),
    N("A diet of 2 000 kcal a day has 50 per cent of energy from carbohydrate (4 kcal per g). How many grams of carbohydrate is that?", 250,
      [("Energy from carbohydrate", "0.50 × 2 000 = 1 000 kcal."), ("Convert", "1 000 ÷ 4 = 250 g.")], T_DIAB, "Calculation", "Convert energy to grams using 4 kcal per gram.", tol=0, unit="g"),
    N("Glycaemic load = GI × carbohydrate (g) ÷ 100. Find the GL of a portion with GI 60 and 25 g of carbohydrate.", 15,
      [("Formula", "GL = 60 × 25 ÷ 100."), ("Calculate", "1 500 ÷ 100 = 15.")], T_DIAB, "Calculation", "Multiply then divide by 100.", tol=0, unit=""),
    Q("A person on insulin is shaking, sweating and confused but can swallow. The first action is:", "Give about 15 g of fast-acting carbohydrate such as sugar in water",
      [("Give a fatty meal", "Fat is absorbed slowly."), ("Give extra insulin", "That would lower glucose further."), ("Do nothing until the symptoms pass", "Untreated hypoglycaemia can lead to loss of consciousness.")],
      [("Hypoglycaemia", "Treat with 15 g of fast carbohydrate, recheck after 15 minutes, then give a snack.")], T_DIAB, "Application", "Which food raises glucose fastest?"),
    Q("Which is the best dietary advice for a person with type 2 diabetes?", "Spread measured, low-GI carbohydrate through the day, add fibre and control weight",
      [("Remove all carbohydrate from the diet", "Carbohydrate is the main energy source; quality and quantity are managed."), ("Eat one very large meal daily", "Large meals cause large glucose peaks."), ("Drink fruit juice instead of eating whole fruit", "Juice lacks fibre and raises glucose faster.")],
      [("Principles", "Regular meals, low GI, fibre, healthy fats, less salt, weight loss and activity.")], T_DIAB, "Application", "Which advice keeps glucose steady?"),
]
SETS.append(practice_set(module=M_CLIN, topic=T_DIAB, title="Insulin, glucagon, diabetes types and glycaemic load", lesson="fsu2-diabetes-mellitus", questions=build(V2, 302)))

# ------------------------------------------------------------------ 3. Hypertension and atherosclerosis
V3 = [
    Q("Hypertension in adults is commonly defined as repeated blood pressure readings of:", "140/90 mmHg or above",
      [("120/80 mmHg or above", "120/80 is a normal reading."), ("100/60 mmHg or below", "That describes low pressure."), ("160/110 mmHg only", "That is severe hypertension; the threshold is lower.")],
      [("Definition", "Persistent 140/90 mmHg or above.")], T_HYP, "Recall", "What is the usual cut-off?"),
    Q("Which of the following is the main difference between atherosclerosis and arteriosclerosis?", "Atherosclerosis is a type of arteriosclerosis caused by plaque of fat and cholesterol in the artery wall",
      [("Atherosclerosis affects veins only", "Both affect arteries."), ("Arteriosclerosis is caused only by plaque", "Plaque is the cause in atherosclerosis; arteriosclerosis is the general term for hardening."), ("They are exactly the same condition", "Atherosclerosis is one type within arteriosclerosis.")],
      [("Distinction", "Arteriosclerosis = hardening and loss of elasticity; atherosclerosis = plaque type.")], T_HYP, "Concept", "Which term is the wider one?"),
    Q("Which lipoprotein carries cholesterol back from tissues to the liver?", "HDL",
      [("LDL", "LDL carries cholesterol to the tissues."), ("Chylomicron", "Chylomicrons carry dietary fat from the gut."), ("Albumin", "Albumin is a plasma protein, not a lipoprotein.")],
      [("HDL", "High-density lipoprotein removes cholesterol from the tissues.")], T_HYP, "Recall", "Which one is called good cholesterol?"),
    Q("Which dietary change is most likely to lower LDL cholesterol?", "Replacing saturated fat with unsaturated fat and adding soluble fibre",
      [("Eating more fried foods cooked in partially hydrogenated oil", "Trans fat raises LDL."), ("Eating more salty processed foods", "Salt raises blood pressure but does not lower LDL."), ("Replacing vegetables with refined starch", "That lowers fibre and does not help.")],
      [("Mechanism", "Unsaturated fat and soluble fibre both lower LDL.")], T_HYP, "Application", "Which change swaps the type of fat?"),
    N("The WHO advises under 2 g of sodium a day. Salt is 39.3 per cent sodium. How many grams of salt contain 2 g of sodium (nearest 0.1 g)?", 5.1,
      [("Relation", "salt = sodium ÷ 0.393."), ("Calculate", "2 ÷ 0.393 = 5.09, about 5.1 g.")], T_HYP, "Calculation", "Divide by the fraction of sodium.", tol=0.1, unit="g"),
    N("A lipid profile gives total cholesterol 5.8, HDL 1.2 and triglycerides 2.2 mmol/L. Estimate LDL = TC − HDL − TG ÷ 2.2 (mmol/L).", 3.6,
      [("Substitute", "5.8 − 1.2 − 2.2 ÷ 2.2."), ("Calculate", "5.8 − 1.2 − 1.0 = 3.6 mmol/L.")], T_HYP, "Calculation", "TG ÷ 2.2 gives 1.0.", tol=0.05, unit="mmol/L"),
    Q("Which is the correct order in the development of an atherosclerotic plaque?", "Damage to the lining, entry of LDL, foam cell and fatty streak, fibrous plaque, clot",
      [("Clot, fatty streak, damage to the lining, plaque", "A clot forms at the end, on a plaque."), ("Plaque, foam cell, damage to the lining, clot", "Plaque is built after the fatty streak."), ("Fatty streak, clot, plaque, damage to the lining", "Damage to the lining comes first.")],
      [("Sequence", "Injury, LDL entry and oxidation, foam cells, fatty streak, plaque, rupture and clot.")], T_HYP, "Reasoning", "What starts the process?"),
    Q("Which advice is part of a DASH-type diet for hypertension?", "Eat more vegetables, fruit and legumes and use less salt",
      [("Add stock cubes to every meal for flavour", "Stock cubes are high in sodium."), ("Replace fish with fatty red meat", "That raises saturated fat."), ("Avoid all fruit and vegetables because they contain sugar", "They supply potassium and fibre and lower blood pressure.")],
      [("DASH", "Vegetables, fruit, legumes, whole grains, fish, little salt and saturated fat.")], T_HYP, "Application", "Which advice lowers sodium and adds potassium?"),
]
SETS.append(practice_set(module=M_CLIN, topic=T_HYP, title="Blood pressure, plaque, lipids and salt calculations", lesson="fsu2-hypertension-atherosclerosis", questions=build(V3, 303)))

# ------------------------------------------------------------------ 4. Renal and gastrointestinal disorders
V4 = [
    Q("Which pair of changes occurs when the kidneys fail?", "Raised blood urea and raised blood potassium",
      [("Raised blood urea and lowered blood phosphate", "Phosphate rises when the kidneys cannot excrete it."), ("Lowered blood urea and raised blood pressure", "Urea builds up in kidney failure."), ("Lowered blood potassium and increased urine output", "Potassium rises and urine output usually falls.")],
      [("Kidney function", "Filtration of urea, potassium and phosphate falls, so they accumulate.")], T_RENAL, "Concept", "What can the kidney no longer excrete?"),
    Q("Why is the protein allowance usually raised when a patient with kidney failure starts dialysis?", "Dialysis removes amino acids and patients are often under-nourished",
      [("Dialysis makes the kidney work harder", "Dialysis replaces part of kidney function."), ("Protein lowers blood potassium", "That is not the reason."), ("Protein is needed to raise blood pressure", "The aim is not to raise blood pressure.")],
      [("Reason", "Before dialysis protein is limited to reduce urea; on dialysis it is raised.")], T_RENAL, "Concept", "What does the dialysis machine remove besides waste?"),
    N("A patient on haemodialysis, ideal body mass 65 kg, is advised 1.2 g of protein per kg. How many grams of protein a day is that?", 78,
      [("Multiply", "65 × 1.2 = 78 g.")], T_RENAL, "Calculation", "Multiply mass by the allowance per kg.", tol=0, unit="g"),
    Q("A patient with kidney failure and high blood potassium should limit which food?", "Large amounts of banana and tomato",
      [("Cooked rice", "Rice is low in potassium."), ("White bread", "Bread is not high in potassium."), ("Boiled egg white", "Egg white is low in potassium.")],
      [("Potassium", "Bananas, tomatoes, oranges and leafy vegetables are potassium-rich.")], T_RENAL, "Application", "Which foods are rich in potassium?"),
    Q("The two most important causes of peptic ulcer are:", "Helicobacter pylori infection and long use of NSAIDs such as aspirin",
      [("Eating spicy food and drinking water", "Spicy food does not cause ulcers."), ("Vitamin C excess and salt", "These are not causes."), ("Gluten and lactose", "These relate to celiac disease and lactose intolerance.")],
      [("Causes", "The bacterium damages the mucus layer; NSAIDs reduce protective mucus.")], T_RENAL, "Recall", "One is a bacterium, one is a type of medicine."),
    Q("In the WHO low-osmolarity oral rehydration solution, glucose is included because:", "Sodium is absorbed together with glucose and water follows",
      [("Glucose kills diarrhoea bacteria", "ORS replaces fluid, it does not kill organisms."), ("Glucose prevents vomiting", "It does not."), ("Glucose lowers the osmolarity below that of blood", "Glucose adds to osmolarity; the amounts are balanced.")],
      [("Co-transport", "Sodium-glucose carriers work even in diarrhoea.")], T_RENAL, "Concept", "Think of the carrier in the intestinal wall."),
    N("The particles in a litre of ORS are sodium 75, chloride 65, glucose 75, potassium 20 and citrate 10 mmol. What is the total osmolarity in mOsm/L?", 245,
      [("Add", "75 + 65 + 75 + 20 + 10 = 245 mOsm/L.")], T_RENAL, "Calculation", "Add every particle.", tol=0, unit="mOsm/L"),
    Q("A child with watery diarrhoea is bright and drinking. The best dietary advice is:", "Give ORS and continue breastfeeding and normal feeding",
      [("Stop all food for 24 hours", "Fasting worsens malnutrition."), ("Give only sweet fizzy drinks", "These are hypertonic and worsen diarrhoea."), ("Give plain boiled water only", "Water does not replace the salts lost.")],
      [("Management", "ORS to replace losses, zinc, continued feeding and clean water.")], T_RENAL, "Application", "What replaces water and salt together?"),
]
SETS.append(practice_set(module=M_CLIN, topic=T_RENAL, title="Kidney diets, peptic ulcer and oral rehydration", lesson="fsu2-renal-gastro", questions=build(V4, 304)))

# ------------------------------------------------------------------ 5. Celiac disease and lactose intolerance
V5 = [
    Q("Celiac disease is best described as:", "An autoimmune disease triggered by gluten that damages the villi of the small intestine",
      [("A shortage of lactase", "That is lactose intolerance."), ("A food allergy to milk protein", "That is a milk allergy."), ("An infection of the large intestine", "Celiac disease is not an infection.")],
      [("Definition", "Gluten triggers an immune attack on the intestinal lining.")], T_CELI, "Recall", "Is it infection, allergy or autoimmunity?"),
    Q("Which cereals contain gluten?", "Wheat, barley and rye",
      [("Maize, rice and millet", "These are gluten-free."), ("Sorghum, oats and rice", "Sorghum and rice are gluten-free and oats are usually avoided only because of contamination."), ("Cassava, yam and plantain", "These are roots and fruit, naturally gluten-free.")],
      [("Sources", "Gluten proteins occur in wheat, barley and rye.")], T_CELI, "Recall", "Which three grains must be avoided?"),
    Q("A person with celiac disease can safely eat:", "Boiled yam with fish and vegetable sauce",
      [("Wheat bread with eggs", "Bread contains wheat gluten."), ("Beer", "Beer is made from barley and contains gluten."), ("Spaghetti made from wheat", "Wheat pasta contains gluten.")],
      [("Gluten-free choice", "Yam, fish and vegetables contain no gluten.")], T_CELI, "Application", "Pick the meal without wheat, barley or rye."),
    Q("Why does untreated celiac disease often cause iron-deficiency anaemia?", "Villous atrophy reduces the surface for absorbing iron",
      [("Gluten destroys iron in the blood", "The problem is absorption, not destruction in the blood."), ("Gluten blocks the liver from making iron", "The liver does not make iron."), ("Celiac patients eat no meat", "Diet is not the main cause.")],
      [("Mechanism", "Flattened villi absorb nutrients poorly.")], T_CELI, "Reasoning", "Where is iron absorbed?"),
    Q("Lactose is a:", "Disaccharide of glucose and galactose",
      [("Disaccharide of two glucose units", "That is maltose."), ("Monosaccharide", "Lactose is a double sugar."), ("Protein of milk", "Casein and whey are milk proteins.")],
      [("Structure", "Lactase splits lactose into glucose and galactose.")], T_CELI, "Recall", "Which two sugars are joined?"),
    Q("Why do some lactose-intolerant people tolerate yoghurt better than milk?", "Bacteria in yoghurt have digested part of the lactose",
      [("Yoghurt contains no carbohydrate", "It contains some lactose."), ("Yoghurt contains extra lactase made by the body", "The body does not make extra lactase."), ("Yoghurt contains more lactose", "It has less lactose than milk.")],
      [("Fermentation", "Lactic acid bacteria use lactose.")], T_CELI, "Concept", "What do the starter bacteria do to lactose?"),
    N("Milk contains 4.7 g of lactose per 100 mL. How many grams of lactose are in 400 mL (1 decimal place)?", 18.8,
      [("Scale", "4.7 × 4 = 18.8 g.")], T_CELI, "Calculation", "400 mL is four lots of 100 mL.", tol=0.1, unit="g"),
    Q("A person who avoids all dairy foods should especially make sure of enough:", "Calcium, from foods such as small bony fish, leafy vegetables and beans",
      [("Gluten", "Gluten is not needed."), ("Lactose", "Lactose is not essential."), ("Vitamin C only", "The main loss with dairy is calcium.")],
      [("Replacement", "Dairy is a main calcium source, so other sources are needed.")], T_CELI, "Application", "What does milk provide in large amounts besides protein?"),
]
SETS.append(practice_set(module=M_CLIN, topic=T_CELI, title="Gluten-free and lactose-reduced diets", lesson="fsu2-celiac-lactose", questions=build(V5, 305)))

# ------------------------------------------------------------------ 6. Nutritional status assessment
V6 = [
    Q("The four groups of methods for assessing nutritional status are summarized as ABCD. Which list is correct?", "Anthropometric, biochemical, clinical, dietary",
      [("Anthropometric, biological, chemical, dietary", "Biological and chemical are not the standard groups."), ("Appetite, blood, calories, diet", "These are not the standard groups."), ("Age, body, chemistry, diet", "These are not the standard groups.")],
      [("ABCD", "Anthropometric, Biochemical, Clinical and Dietary.")], T_STATUS, "Recall", "Match each letter."),
    Q("A child of 30 months has a height-for-age Z-score of −2.4. The child is:", "Stunted",
      [("Wasted", "Wasting is low weight-for-height."), ("Overweight", "A negative Z-score cannot indicate overweight."), ("Normal", "A Z-score below −2 is outside the normal range.")],
      [("Cut-off", "HAZ below −2 means stunting.")], T_STATUS, "Application", "Which index is height-for-age?"),
    N("A child's mass is 8.4 kg. The reference median for age and sex is 10.0 kg with SD 1.0 kg. Find the weight-for-age Z-score.", -1.6,
      [("Formula", "Z = (observed − median) ÷ SD."), ("Calculate", "(8.4 − 10.0) ÷ 1.0 = −1.6.")], T_STATUS, "Calculation", "Observed minus median, divided by SD.", tol=0.05, unit=""),
    Q("A child of 24 months has a MUAC of 118 mm. According to the WHO cut-offs this is:", "Moderate acute malnutrition",
      [("Severe acute malnutrition", "That is below 115 mm."), ("Normal", "Normal is 125 mm or more."), ("Stunting", "MUAC does not measure stunting.")],
      [("MUAC bands", "Under 115 severe, 115 to under 125 moderate, 125 or more normal.")], T_STATUS, "Application", "Compare with 115 and 125 mm."),
    Q("In the diagram, which region contains children with a Z-score between −3 and −2?", "Q",
      [("P", "P is below −3."), ("R", "R is between −2 and 0."), ("S", "S is at the median.")],
      [("Read the axis", "Region Q lies between the lines at −3 and −2: moderate.")], T_STATUS, "Interpretation", "Read the numbers on the axis.", diagram=ZQ, alt=ZQ_ALT),
    Q("Which limitation applies to a single 24-hour dietary recall?", "It may not represent a person's usual intake",
      [("It cannot be used with illiterate people", "A recall is spoken and suits illiterate respondents."), ("It needs a blood sample", "It is based on an interview."), ("It measures only the weight of the person", "It records foods and amounts eaten.")],
      [("Limit", "One day varies from usual intake; repeat it on several days.")], T_STATUS, "Concept", "Think of day-to-day variation."),
    N("A person eats 250 g of plantain as bought. The peel makes up 30 per cent of the mass. Energy of the edible portion is 122 kcal per 100 g (teaching value). Find the energy eaten (kcal, nearest whole number).", 213,
      [("Edible portion", "250 × 0.70 = 175 g."), ("Energy", "122 × 1.75 = 213.5 kcal; the answer is 213 or 214.")], T_STATUS, "Calculation", "Remove the peel before scaling.", tol=1, unit="kcal"),
    Q("A haemoglobin of 10.5 g/dL in a non-pregnant woman is:", "Below the WHO cut-off for anaemia of 12 g/dL",
      [("Above the cut-off for anaemia", "12 g/dL is the cut-off for non-pregnant women."), ("Normal for a woman", "It is below 12."), ("Exactly the same as the cut-off for men", "The cut-off for men is 13 g/dL.")],
      [("Cut-offs", "Women (non-pregnant) 12, men 13, pregnant women and young children 11 g/dL.")], T_STATUS, "Application", "Compare with 12 g/dL."),
]
SETS.append(practice_set(module=M_COMM, topic=T_STATUS, title="ABCD methods, Z-scores, MUAC and recalls", lesson="fsu2-nutritional-status", questions=build(V6, 306)))

# ------------------------------------------------------------------ 7. Fortification and nutrition programmes
V7 = [
    Q("Adding iodine to the salt eaten by the whole population is an example of:", "Mass (universal) fortification",
      [("Biofortification", "Biofortification uses plant breeding."), ("Targeted fortification", "Targeted fortification is for a specific group."), ("Enrichment of refined flour", "Enrichment restores nutrients lost in processing.")],
      [("Type", "A staple eaten by nearly everyone carries the nutrient.")], T_FORT, "Concept", "Who eats the salt?"),
    Q("Which is the best definition of enrichment?", "Restoring nutrients lost during processing, for example B vitamins and iron in refined flour",
      [("Adding a nutrient never found in the food", "That is fortification."), ("Breeding crops with more nutrients", "That is biofortification."), ("Giving capsules to a target group", "That is supplementation.")],
      [("Definition", "Enrichment puts back what processing removed.")], T_FORT, "Recall", "Think of refined flour."),
    Q("Which is a characteristic of a good food vehicle?", "It is eaten regularly in fairly constant amounts and processed centrally",
      [("It is eaten only at festivals", "Regular consumption is needed."), ("It is made in thousands of home kitchens", "Central processing allows quality control."), ("It changes colour when the nutrient is added", "Fortification should not change sensory quality.")],
      [("Vehicle", "Wide, regular, steady intake and central mixing.")], T_FORT, "Concept", "Who eats it, how often and where is it made?"),
    N("Salt is to be iodized to give 30 mg of iodine per kg. How many micrograms of iodine are in 4 g of this salt?", 120,
      [("Per gram", "30 mg per kg = 30 µg per g."), ("4 g", "4 × 30 = 120 µg.")], T_FORT, "Calculation", "30 mg per kg equals 30 µg per g.", tol=0, unit="µg"),
    N("Flour is to carry 40 mg of iron per kg. How many grams of an iron compound containing 20 per cent iron are needed for 500 kg of flour?", 100,
      [("Iron needed", "40 × 500 = 20 000 mg = 20 g."), ("Compound", "20 ÷ 0.20 = 100 g.")], T_FORT, "Calculation", "Find the mass of iron, then divide by the iron fraction.", tol=0, unit="g"),
    Q("Vitamin A capsules are given to children aged 6 to 59 months every four to six months. This is:", "Supplementation",
      [("Fortification", "Fortification adds nutrients to foods."), ("Biofortification", "That is plant breeding."), ("Dietary diversification", "That is a change of foods eaten.")],
      [("Type", "Capsules, tablets or syrups are supplements.")], T_FORT, "Concept", "Is the nutrient added to a food?"),
    Q("A community teaches that pregnant women should not eat eggs. This rule, forbidden by custom, is a:", "Food taboo",
      [("Food fad", "A fad is a short-lived fashion."), ("Food fallacy", "A fallacy is a false belief; the question describes a prohibition."), ("Food fortification", "No nutrient is added.")],
      [("Taboo", "A food forbidden by custom or religion.")], T_FORT, "Concept", "Is it a prohibition or just a belief?"),
    Q("Which is the best way to deal with a taboo that bans eggs for children?", "Learn the reason and offer other protein foods such as fish, beans and groundnuts",
      [("Ignore the culture and force the change", "Education works best when it respects culture."), ("Ban the community from growing eggs", "This does not address nutrition."), ("Replace all local foods with imported ones", "Local foods are cheaper and acceptable.")],
      [("Approach", "Respect culture and use local alternatives.")], T_FORT, "Application", "How would you win the community's trust?"),
]
SETS.append(practice_set(module=M_COMM, topic=T_FORT, title="Fortification amounts, programmes and food habits", lesson="fsu2-fortification-programmes", questions=build(V7, 307)))

# ------------------------------------------------------------------ 8. Food security policy
V8 = [
    Q("Which list gives the four dimensions of food security?", "Availability, access, utilization and stability",
      [("Production, price, processing and packaging", "These are stages of the food chain, not the dimensions."), ("Availability, affordability, advertising and aid", "Advertising and aid are not dimensions."), ("Supply, storage, sale and safety", "These are not the standard dimensions.")],
      [("Four dimensions", "Availability, access, utilization and stability.")], T_FSEC, "Recall", "A-A-U-S."),
    Q("A family lives near a market full of food but cannot afford it. Which dimension is mainly affected?", "Access",
      [("Availability", "Food is available in the market."), ("Utilization", "That concerns how the body uses food."), ("Stability only", "The problem is the lack of purchasing power now.")],
      [("Access", "Income and prices decide whether households can obtain food.")], T_FSEC, "Application", "Is the food missing or out of reach?"),
    Q("Frequent diarrhoea caused by unsafe water reduces which dimension of food security most directly?", "Utilization",
      [("Availability", "The food supply is not directly changed."), ("Access", "Income and prices are unchanged."), ("Production", "Production is not a dimension.")],
      [("Utilization", "Safe water, sanitation and health let the body use food.")], T_FSEC, "Reasoning", "Think of the body using the nutrients."),
    Q("Seasonal hunger before the harvest each year is mainly a problem of:", "Stability",
      [("Utilization", "That concerns water and health."), ("Availability across the whole year only", "It is the change over time that defines stability."), ("Biofortification", "That is a method, not a dimension.")],
      [("Stability", "Food security must hold at all times.")], T_FSEC, "Concept", "Which dimension has 'at all times'?"),
    Q("Which measure mainly improves food availability?", "Reducing post-harvest losses through better drying and storage",
      [("Cash transfers to poor households", "These improve access."), ("Hand-washing campaigns", "These improve utilization."), ("Early warning of drought", "That supports stability.")],
      [("Availability", "Less loss means more food reaches consumers.")], T_FSEC, "Application", "Which one adds to supply?"),
    N("A region produces 40 000 t, imports 10 000 t and exports 2 000 t of food. Losses are 10 per cent of the net supply. How many tonnes remain available?", 43200,
      [("Net supply", "40 000 + 10 000 − 2 000 = 48 000 t."), ("After losses", "48 000 × 0.90 = 43 200 t.")], T_FSEC, "Calculation", "Find the net supply first.", tol=0, unit="t"),
    N("Using 43 200 t of food at 3 500 kcal per kg for 200 000 people, estimate the energy per person per day in kcal (nearest whole number; use 365 days).", 2071,
      [("Total energy", "43 200 000 kg × 3 500 = 1.512 × 10^11 kcal."), ("Per person per day", "1.512 × 10^11 ÷ (200 000 × 365) = 2 071 kcal.")], T_FSEC, "Calculation", "Divide by population and days.", tol=2, unit="kcal"),
    Q("Why can a national food balance sheet fail to show that some households are hungry?", "It gives an average and does not show access, sharing or seasons",
      [("It counts only imported food", "It includes production and imports."), ("It measures the weight of children", "It does not measure bodies."), ("It is always accurate for every household", "It is a national average.")],
      [("Limit", "Averages hide inequality and seasonal gaps.")], T_FSEC, "Interpretation", "What does an average hide?"),
]
SETS.append(practice_set(module=M_COMM, topic=T_FSEC, title="Four dimensions, causes and policy for food security", lesson="fsu2-food-security-policy", questions=build(V8, 308)))

# ------------------------------------------------------------------ 9. Paper 1 lesson set
V9 = [
    Q("According to the Board's 2023 report, Paper 1 of Food Science and Nutrition is:", "50 multiple-choice questions on the whole syllabus, 35 per cent, 1 hour 30 minutes",
      [("50 multiple-choice questions, 40 per cent, 3 hours", "That is the weighting and time of Paper 2."), ("Essay type, 35 per cent, 1 hour 30 minutes", "Paper 1 is multiple choice."), ("A practical paper of 25 per cent", "That is Paper 3.")],
      [("Facts", "Paper 1 is multiple choice, 35 per cent and 1 hour 30 minutes.")], "Paper 1", "Recall", "Recall the table in the report."),
    N("At an even pace, how many seconds are available per question for 50 questions in 90 minutes?", 108,
      [("Total time", "90 × 60 = 5 400 s."), ("Per question", "5 400 ÷ 50 = 108 s.")], "Paper 1", "Calculation", "Convert minutes to seconds first.", tol=0, unit="s"),
    Q("A stem says 'Which of the following is NOT a feature of marasmus?' The best first step is to:", "Mark NOT and look for the option that does not fit marasmus",
      [("Ignore NOT and choose a feature of marasmus", "That answers the opposite question."), ("Choose the longest option", "Length is not reliable."), ("Choose the first option", "That is guessing.")],
      [("Key word", "NOT reverses the task.")], "Paper 1", "Reasoning", "What does the word NOT do?"),
    Q("Which option is a typical distractor pattern in a nutrition question?", "Swapping the roles of insulin and glucagon",
      [("Using the correct fact for the question asked", "That is the right answer, not a distractor."), ("Giving the answer in the stem", "That is not a distractor pattern."), ("Repeating the question as an option", "That is not typical.")],
      [("Pattern", "Reversed pairs are common distractors.")], "Paper 1", "Concept", "Which pair is commonly reversed?"),
    N("The report's table of specification for Paper 1 lists knowledge and comprehension 15, application 15, analysis 10, synthesis 5 and evaluation 5. How many of the 50 questions need more than recall and comprehension?", 35,
      [("Add", "15 + 10 + 5 + 5 = 35.")], "Paper 1", "Interpretation", "Add all rows except knowledge and comprehension.", tol=0, unit="questions"),
    N("A man's mass is 81 kg and his height is 1.80 m. What is his BMI?", 25,
      [("Square the height", "1.80² = 3.24."), ("Divide", "81 ÷ 3.24 = 25.")], "Paper 1", "Calculation", "Square the height first.", tol=0.1, unit="kg/m²"),
    Q("If a question has taken about 3 minutes with no answer, the best action is to:", "Mark it, give a best guess and move on, returning if time allows",
      [("Spend ten more minutes on it", "Each question carries the same mark."), ("Leave all later questions blank", "Time would be lost for easier questions."), ("Change all your earlier answers", "Without a reason this is unhelpful.")],
      [("Pacing", "A first pass then a second pass with the marked questions.")], "Paper 1", "Application", "Each question is worth the same."),
    Q("A calculation asks for the energy eaten from 200 g of food as bought, of which 30 per cent is waste. Which method is correct?", "Find the edible portion (140 g), then scale the table value per 100 g",
      [("Use 200 g directly with the table value", "That ignores the refuse."), ("Use 30 g only", "30 per cent is the waste, not the edible portion."), ("Divide the table value by 200", "That does not scale correctly.")],
      [("Method", "Tables give values per 100 g of edible portion.")], "Paper 1", "Application", "What does the table use as its basis?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 structure, pacing and distractors", lesson="fsu2-exam-paper-1-multiple-choice", questions=build(V9, 309)))

# ------------------------------------------------------------------ 10. Paper 2 lesson set
V10 = [
    Q("According to the Board's report, Paper 2 is:", "Essay type, 40 per cent, 3 hours",
      [("Multiple choice, 35 per cent, 1 hour 30 minutes", "That is Paper 1."), ("Essay type, 25 per cent, 2 hours", "That is the weighting and time of Paper 3."), ("A practical paper of 40 per cent", "Paper 3 is the practical paper.")],
      [("Facts", "Paper 2: essay type, 40 per cent, 3 hours.")], "Paper 2", "Recall", "Recall the table in the report."),
    Q("The report says some candidates lost marks by:", "Answering two questions from one section instead of one",
      [("Answering all questions from Section D", "That is not reported."), ("Drawing diagrams", "Diagrams are encouraged."), ("Writing in short paragraphs", "Short paragraphs are good practice.")],
      [("Instructions", "Follow the section instruction on the paper.")], "Paper 2", "Recall", "Recall the students' recommendations in the report."),
    Q("The command word 'differentiate' means:", "Give differences between two things, side by side",
      [("List without explanation", "That is state or list."), ("Give a reason for something", "That is explain."), ("Draw a diagram only", "That is a different instruction.")],
      [("Command word", "Differentiate means state differences.")], "Paper 2", "Concept", "Think of 'difference'."),
    Q("A part carries 6 marks. The best length of answer is:", "About six clear points, matched to the marks",
      [("One sentence", "Too short for 6 marks."), ("Three pages of unrelated facts", "Marks are lost for irrelevant material."), ("A single diagram without labels", "Unlabelled diagrams earn little.")],
      [("Mark matching", "Count points against marks.")], "Paper 2", "Application", "How many points make 6 marks?"),
    Q("High biological value (HBV) protein is protein that:", "Contains all the essential amino acids in proportions close to human needs",
      [("Is found only in cereals", "Cereals are usually low in lysine."), ("Contains no essential amino acids", "That would be of no value."), ("Is always cheaper", "Cost is not the definition.")],
      [("Definition", "HBV protein has a well-balanced amino acid pattern, as in eggs, milk, meat and fish.")], "Paper 2", "Recall", "Which amino acids must be present?"),
    Q("Which sequence belongs to margarine manufacture and not to cheese?", "Oil hydrogenation or blending, emulsifying with an aqueous phase, chilling and kneading",
      [("Milk, starter and rennet, curd cutting and whey draining", "That is cheese."), ("Washing, peeling, slicing and frying", "That describes making chips."), ("Mashing, fermenting, boiling with hops and cooling", "That is brewing.")],
      [("Margarine", "Fat phase plus aqueous phase, emulsified, chilled and worked.")], "Paper 2", "Application", "Margarine is a fat emulsion."),
    Q("Enzyme selectivity (specificity) means:", "Each enzyme acts only on a particular substrate because of the shape of its active site",
      [("Enzymes lower activation energy", "That is the catalytic function."), ("Enzymes are used up in the reaction", "Enzymes are not used up."), ("Enzymes work at any temperature", "Enzymes are sensitive to temperature and pH.")],
      [("Distinction", "Selectivity = choice of substrate; catalysis = lower activation energy.")], "Paper 2", "Concept", "Which idea is about choosing the substrate?"),
    Q("A statement 'a pregnant woman should eat less so that the baby is small' is best called a:", "Food fallacy",
      [("Food fad", "Fads are short-lived fashions."), ("Food taboo", "A taboo is a prohibition by custom."), ("Fortification", "No nutrient is added.")],
      [("Term", "A false belief with no scientific support is a fallacy.")], "Paper 2", "Concept", "Is it a belief, a custom or a fashion?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 structure, command words and flagged topics", lesson="fsu2-exam-paper-2-essays", questions=build(V10, 310)))

# ------------------------------------------------------------------ 11. Paper 3 lesson set
V11 = [
    Q("According to the Board's report, Paper 3 is:", "A practical paper with food tests and cookery, 25 per cent, 2 hours",
      [("Essay type, 40 per cent, 3 hours", "That is Paper 2."), ("Multiple choice, 35 per cent", "That is Paper 1."), ("A written paper on cookery only", "It has both food tests and cookery, and it is practical.")],
      [("Facts", "Two parts: food test and cookery.")], "Paper 3", "Recall", "Recall the table in the report."),
    Q("A food extract turns blue-black with iodine solution. This shows:", "Starch is present",
      [("Reducing sugar is present", "That is shown by Benedict's test."), ("Protein is present", "That is shown by the biuret test."), ("Fat is present", "That is shown by the ethanol emulsion test.")],
      [("Test", "Iodine reacts with starch to give blue-black.")], "Paper 3", "Recall", "Which nutrient does iodine test for?"),
    Q("Benedict's test stays blue after heating in a water bath. The correct conclusion is:", "Reducing sugar is not present",
      [("Reducing sugar is present", "A positive test turns green, yellow, orange or brick-red."), ("The test is invalid", "A blue result is a valid negative."), ("Starch is present", "This test does not detect starch.")],
      [("Negative result", "Report absence as well as presence.")], "Paper 3", "Interpretation", "Does blue mean a colour change?"),
    Q("What does the biuret test detect, and what is the positive colour?", "Protein; violet or purple",
      [("Starch; blue-black", "That is the iodine test."), ("Reducing sugar; brick-red", "That is Benedict's test."), ("Fat; cloudy white", "That is the ethanol emulsion test.")],
      [("Biuret", "Sodium hydroxide and dilute copper sulfate give violet with protein.")], "Paper 3", "Recall", "Name the nutrient detected by copper(II) ions in alkali."),
    Q("A sucrose solution gives no colour change with Benedict's test, but after boiling with dilute acid, neutralizing and re-testing it gives brick-red. Why?", "Acid hydrolyses sucrose to glucose and fructose, which are reducing sugars",
      [("Sucrose is a reducing sugar", "Sucrose is a non-reducing sugar."), ("The acid is a reducing sugar", "The acid is not a sugar."), ("Boiling creates starch", "Boiling does not create starch.")],
      [("Hydrolysis", "Sucrose gives glucose and fructose on hydrolysis.")], "Paper 3", "Reasoning", "What does acid do to a disaccharide?"),
    N("2.0 cm³ of DCPIP is decolourised by 1.6 cm³ of ascorbic acid solution of concentration 1.0 mg per cm³. The same volume of DCPIP is decolourised by 4.0 cm³ of a juice. What is the vitamin C concentration of the juice (mg per cm³)?", 0.4,
      [("Ascorbic acid used", "1.6 cm³ × 1.0 mg/cm³ = 1.6 mg."), ("Juice", "1.6 mg ÷ 4.0 cm³ = 0.40 mg per cm³.")], "Paper 3", "Calculation", "Find the mass that decolourises 2.0 cm³ of DCPIP.", tol=0.01, unit="mg/cm³"),
    N("Using teaching values, 90 g of uncooked rice with 360 kcal per 100 g of edible portion gives how many kcal?", 324,
      [("Scale", "360 × 0.90 = 324 kcal.")], "Paper 3", "Calculation", "Scale the value per 100 g.", tol=0, unit="kcal"),
    Q("Which is the best order of items in a cookery time plan?", "Longest-cooking items first, items needed hot at serving last",
      [("Serving first, then washing", "Time plans move forward to serving."), ("Items in alphabetical order", "Order depends on timing."), ("The quickest items first", "Slow items need the earliest start.")],
      [("Planning", "Work back from the serving time.")], "Paper 3", "Application", "Work backwards from serving."),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Paper 3 food tests, calculations and cookery planning", lesson="fsu2-exam-paper-3-practicals", questions=build(V11, 311)))

# ------------------------------------------------------------------ Paper 1 mock exam A (50 questions)
P1 = [
    # ---- Food Engineering & Preservation Technology (11)
    Q("The D-value of a micro-organism is the time at a given temperature needed to:", "Reduce the number of viable cells by 90 per cent (one log cycle)",
      [("Kill every cell in the food", "Heat kills in a first-order way and never reaches exactly zero."), ("Raise the temperature by 10 degrees Celsius", "That describes the z-value."), ("Double the number of cells", "D concerns destruction, not growth.")],
      [("Definition", "D is the decimal reduction time: one tenfold fall in the population.")], T_THERM, "Recall", "Think of one log cycle."),
    Q("A spore population falls from 10^6 to 10^2 per gram in 8 minutes at 121 °C. What is the D-value?", "2 minutes",
      [("8 minutes", "That is the total time, not the time per log cycle."), ("4 minutes", "The reduction is 4 log cycles; 4 is the number of cycles, not the time per cycle."), ("0.5 minutes", "That divides 4 by 8, the wrong way round.")],
      [("Log cycles", "From 10^6 to 10^2 is 4 log cycles."), ("D-value", "8 ÷ 4 = 2 minutes.")], T_THERM, "Calculation", "Count the log cycles first."),
    Q("The z-value of an organism is 10 °C and its D-value at 111 °C is 2.0 min. What is the D-value at 121 °C?", "0.2 min",
      [("20 min", "A higher temperature lowers D; it does not raise it."), ("2.0 min", "D changes by a factor of 10 for each z degrees."), ("0.02 min", "That is two log cycles; only one (10 °C) is crossed.")],
      [("Rule", "A rise of z degrees divides D by 10."), ("Apply", "Rise of 10 °C: D = 2.0 ÷ 10 = 0.2 min.")], T_THERM, "Calculation", "How many z-values lie between 111 and 121 °C?"),
    Q("The main reason for blanching vegetables before freezing is to:", "Inactivate enzymes that cause off-flavours and colour change in storage",
      [("Sterilize the vegetables completely", "Blanching only reduces microbial load slightly."), ("Increase the vitamin C content", "Some vitamin C is lost in blanching."), ("Raise the water activity", "Blanching is not used to change water activity.")],
      [("Purpose", "Heat inactivates enzymes such as peroxidase, and also expels air and fixes colour.")], T_THERM, "Concept", "What would enzymes do during frozen storage?"),
    Q("A milk sample is held at 72 °C for 15 seconds and then cooled quickly. This treatment is:", "High-temperature short-time (HTST) pasteurization",
      [("Ultra-high temperature (UHT) sterilization", "UHT uses about 135 °C or more for a few seconds."), ("Canning at 121 °C", "Canning uses much higher temperatures in sealed containers."), ("Blanching", "Blanching is used for vegetables before other processes.")],
      [("Time and temperature", "HTST is about 72 °C for 15 s; the low-temperature long-time method is about 63 °C for 30 min.")], T_PAST, "Recall", "Match the time and temperature."),
    Q("Why are foods with a pH above 4.6 given a heat process of about 121 °C in a retort?", "To destroy spores of Clostridium botulinum, which can grow in low-acid foods",
      [("To raise the pH to 7", "Heat does not neutralize the food."), ("Because acid foods cannot be heated", "Acid foods are heated at lower temperatures."), ("To freeze the water in the food", "Retort processing is heating, not freezing.")],
      [("pH 4.6 rule", "Low-acid foods allow growth and toxin formation by C. botulinum spores.")], T_PAST, "Concept", "Which spore-former matters in low-acid canned food?"),
    Q("A banana stored at 5 °C develops black skin and does not ripen properly. This damage is called:", "Chilling injury",
      [("Freezer burn", "Freezer burn is surface dehydration of frozen food."), ("Enzymatic blanching", "Not a process that causes this."), ("Case hardening", "Case hardening is a drying defect.")],
      [("Chilling injury", "Tropical fruits are damaged above freezing, usually below about 12 °C.")], T_LOWT, "Application", "Is the temperature below zero?"),
    Q("Quick freezing is preferred to slow freezing because it:", "Forms small ice crystals that cause less damage to the cells",
      [("Forms large crystals that rupture the cell walls", "That is the problem of slow freezing."), ("Raises the water activity", "Freezing lowers the amount of available water."), ("Kills all micro-organisms", "Freezing stops growth but does not sterilize.")],
      [("Crystal size", "Fast freezing gives many small crystals, with less drip loss on thawing.")], T_LOWT, "Concept", "Think of crystal size and cell damage."),
    Q("In freeze-drying, water is removed by:", "Sublimation of ice under vacuum",
      [("Evaporation in hot air", "That is hot-air drying."), ("Boiling at atmospheric pressure", "Boiling would cook the food."), ("Spraying onto hot rollers", "That is drum drying.")],
      [("Mechanism", "The food is frozen and the ice turns directly to vapour under low pressure.")], T_DEHY, "Recall", "Ice to vapour without becoming liquid."),
    Q("100 kg of fruit with 80 per cent moisture is dried to 20 per cent moisture. How much water is removed?", "75 kg",
      [("60 kg", "That subtracts the percentages (80 − 20) as if they were kilograms of the original mass."), ("80 kg", "That is the original water, not the water removed."), ("25 kg", "That is the mass of dried product.")],
      [("Dry solids", "100 × 0.20 = 20 kg."), ("Final mass", "20 ÷ 0.80 = 25 kg."), ("Water removed", "100 − 25 = 75 kg.")], T_DEHY, "Calculation", "The dry solids do not change."),
    Q("Modified atmosphere packaging usually extends shelf life of fresh produce by:", "Lowering oxygen and raising carbon dioxide, which slows respiration and spoilage",
      [("Raising oxygen to speed ripening", "That would shorten shelf life."), ("Adding live yeast to the pack", "Yeast would cause spoilage."), ("Removing all nitrogen", "Nitrogen is a common inert filler gas.")],
      [("MAP", "Gas mixture with less O2 and more CO2 and N2 slows respiration and aerobic organisms.")], T_IRR, "Concept", "Think of respiration."),
    # ---- Post-Harvest Commodity Technology (14)
    Q("Which fruit is climacteric, ripening with a burst of ethylene and respiration after harvest?", "Banana",
      [("Orange", "Citrus is non-climacteric."), ("Pineapple", "Pineapple is non-climacteric and does not ripen further after harvest."), ("Grape", "Grapes are non-climacteric.")],
      [("Climacteric fruit", "Banana, mango, tomato, avocado and papaya.")], T_PHYS, "Recall", "Which fruit can be ripened off the plant?"),
    Q("Which storage change is most likely to slow the respiration and ripening of fruit?", "A lower temperature, above the chilling limit, and removal of ethylene",
      [("A higher temperature", "That speeds respiration."), ("Adding ripe fruit to the store", "Ripe fruit releases ethylene."), ("Sealing in a bag with no ventilation", "Without ventilation, gases and heat build up.")],
      [("Control", "Cool storage and ethylene control slow ripening.")], T_PHYS, "Application", "Which change slows chemical reactions?"),
    Q("Which change occurs when a banana ripens?", "Starch is converted to sugars and the skin turns from green to yellow as chlorophyll is lost",
      [("Sugars are converted to starch", "The reverse occurs."), ("Pectin becomes harder", "Pectin is broken down and the fruit softens."), ("Acidity and chlorophyll increase", "Chlorophyll is lost.")],
      [("Ripening", "Starch hydrolysis, chlorophyll loss, softening and aroma formation.")], T_PHYS, "Concept", "Think of how ripe fruit tastes."),
    Q("Wheat flour is suited to bread making because its proteins:", "Form elastic gluten that holds the gas produced by yeast",
      [("Dissolve completely in water", "Gluten proteins hydrate to form a network."), ("Contain no amino acids", "All proteins contain amino acids."), ("Are destroyed in the oven before the dough rises", "They coagulate and set the structure.")],
      [("Gluten", "Gliadin and glutenin form an elastic network.")], T_CER, "Concept", "Why does dough stretch?"),
    Q("The extraction rate of flour is the:", "Percentage of the cleaned grain that is obtained as flour",
      [("Percentage of water removed from the flour", "That is moisture loss."), ("Number of times grain is milled", "It is a percentage."), ("Protein content of the flour", "Protein content is a different measure.")],
      [("Definition", "For example, 75 kg of flour from 100 kg of grain is 75 per cent.")], T_CER, "Recall", "Flour as a share of grain."),
    Q("In bread making, yeast raises the dough mainly by:", "Fermenting sugar to carbon dioxide and ethanol",
      [("Producing oxygen", "Yeast produces carbon dioxide."), ("Hydrolysing gluten", "Gluten is needed to hold the gas."), ("Dissolving the starch", "Starch is not dissolved to raise the dough.")],
      [("Fermentation", "CO2 expands the dough and the ethanol evaporates in the oven.")], T_CER, "Concept", "Which gas inflates the dough?"),
    Q("Fresh bitter cassava is made safe to eat by processes such as grating, soaking, fermenting and cooking, because they:", "Remove or break down cyanogenic glucosides, which release hydrogen cyanide",
      [("Add vitamin A", "These steps do not add vitamin A."), ("Convert protein to starch", "Cassava is mainly starch already."), ("Raise the water activity to 1", "That is not their purpose.")],
      [("Detoxification", "Linamarin is broken down by linamarase and the cyanide is lost as gas or washed away.")], T_ROOT, "Application", "What toxic compound is in cassava?"),
    Q("As a plantain ripens, its starch content:", "Falls as starch is converted to sugars",
      [("Rises as sugars are converted to starch", "The reverse is true."), ("Stays unchanged until it rots", "Ripening changes the composition."), ("Is converted to protein", "Starch is not converted to protein.")],
      [("Composition", "Green plantain is starchy; ripe plantain is sweeter.")], T_ROOT, "Concept", "Compare a green and a ripe plantain."),
    Q("In oil refining, the step that removes free fatty acids using alkali is called:", "Neutralization",
      [("Degumming", "Degumming removes phospholipids."), ("Bleaching", "Bleaching removes pigments with clay."), ("Deodorization", "Deodorization removes volatile odours with steam under vacuum.")],
      [("Order", "Degumming, neutralization, bleaching, deodorization.")], T_OIL, "Recall", "Alkali reacts with acids."),
    Q("Which statement about solvent extraction of oilseeds is correct?", "A solvent such as hexane dissolves the oil from flaked seed and is then removed by evaporation",
      [("Water is used to wash out the oil", "Oil does not dissolve in water."), ("It yields less oil than hand pounding", "It extracts a high proportion of the oil."), ("It works only for palm fruit", "It is used for oilseeds such as soya and cottonseed.")],
      [("Solvent extraction", "Hexane dissolves the oil; the solvent is distilled off and recycled.")], T_OIL, "Concept", "Fat dissolves in non-polar solvents."),
    Q("The development of rigor mortis in meat is mainly due to:", "Loss of ATP, which lets actin and myosin stay locked together, with a fall in pH",
      [("Gain of ATP and a rise in pH", "ATP falls after death."), ("Growth of Salmonella", "Rigor is a muscle change, not an infection."), ("Dissolving of collagen", "Collagen is not dissolved in rigor.")],
      [("Rigor", "After death glycogen is converted to lactic acid, the pH falls and ATP is lost.")], T_MEAT, "Concept", "What fuels muscle relaxation?"),
    Q("In the manufacture of yoghurt, milk sets because:", "Lactic acid from bacteria lowers the pH and causes casein to coagulate",
      [("Rennet is added to every batch", "Cheese uses rennet; yoghurt relies on acid."), ("Water is evaporated off", "That is condensed milk."), ("Lactose is converted to starch", "Lactose is converted to lactic acid.")],
      [("Yoghurt", "Streptococcus and Lactobacillus ferment lactose to lactic acid, pH about 4.6, and casein coagulates.")], T_MEAT, "Concept", "What do the starter bacteria produce?"),
    Q("The fermentation of fresh cocoa beans before drying is important because it:", "Develops chocolate flavour precursors and reduces bitterness",
      [("Roasts the beans", "Roasting is a later step."), ("Adds fat to the beans", "Fat is already present."), ("Sterilizes the bean completely", "It is a microbial and enzymatic process, not sterilization.")],
      [("Cocoa", "Pulp is fermented for several days, then beans are dried and later roasted.")], T_BEV, "Concept", "Which step makes flavour precursors?"),
    Q("In brewing, malting is carried out to:", "Germinate the grain so that enzymes convert starch to fermentable sugars",
      [("Kill the yeast", "Yeast is added later for fermentation."), ("Add the hops", "Hops are added in boiling the wort."), ("Remove the husk completely", "The aim is enzyme development.")],
      [("Malting", "Germination develops amylases that act in mashing.")], T_BEV, "Concept", "Which compound is converted to sugar?"),
    # ---- Food Quality Assurance & Legislation (7)
    Q("How many principles does HACCP have?", "Seven",
      [("Five", "There are seven principles."), ("Nine", "Nine is not the number of principles."), ("Twelve", "Twelve is the number of steps in the Codex application sequence, not the principles.")],
      [("Principles", "Hazard analysis, CCPs, critical limits, monitoring, corrective actions, verification, records.")], T_HACCP, "Recall", "Count the principles."),
    Q("A critical control point (CCP) is a step at which:", "Control can be applied and is essential to prevent, remove or reduce a hazard to an acceptable level",
      [("Any hazard is recorded but never controlled", "A CCP is where control is applied."), ("The product is packed", "Packing may or may not be a CCP."), ("The plant manager is replaced", "It is a step in the process, not a personnel event.")],
      [("Definition", "Essential control at a process step.")], T_HACCP, "Concept", "Where must you act?"),
    Q("In pasteurization of milk, '72 °C for 15 seconds' is an example of a:", "Critical limit",
      [("Corrective action", "A corrective action is what is done when a limit is missed."), ("Hazard", "A hazard is an agent such as a pathogen."), ("Verification record", "Verification confirms that the system works.")],
      [("Critical limit", "A measurable limit that separates safe from unsafe at a CCP.")], T_HACCP, "Application", "Which term is a measurable boundary?"),
    Q("Good Manufacturing Practice (GMP) is best described as:", "Basic hygiene and operating conditions that make food production safe and consistent",
      [("A tax paid by food factories", "GMP is not a tax."), ("A method of freezing food", "GMP is not a preservation method."), ("An advertising code", "It concerns production.")],
      [("GMP", "Premises, hygiene, pest control, training and cleaning are prerequisites for HACCP.")], T_GMP, "Concept", "Think of prerequisites."),
    Q("ISO 22000 is:", "An international food safety management system standard that includes HACCP principles and prerequisite programmes",
      [("A law that bans all additives", "It is a voluntary standard, not a ban."), ("A method of milling", "It is a management standard."), ("A listing of vitamin recommendations", "It does not list vitamins.")],
      [("ISO 22000", "Management system for any organization in the food chain.")], T_GMP, "Recall", "Is it a law, a method or a system?"),
    Q("The Codex Alimentarius is:", "A collection of international food standards, guidelines and codes of practice developed under FAO and WHO",
      [("A Cameroonian law on markets", "Codex is international."), ("A list of foods banned in Africa", "It is not a list of bans."), ("A school curriculum", "It is a standards collection.")],
      [("Codex", "The Codex Alimentarius Commission is an FAO and WHO body.")], T_CODEX, "Recall", "Which UN agencies are involved?"),
    Q("In Cameroon, the national standards and quality agency whose standards a food producer should check is:", "ANOR (check the current rules)",
      [("FIFA", "FIFA is a football body."), ("BEAC", "BEAC is the central bank of the CEMAC region."), ("CEMAC alone", "CEMAC is a regional community, not the standards agency.")],
      [("ANOR", "The standards and quality agency; check the current rules on which standards are mandatory.")], T_CODEX, "Recall", "Which acronym relates to standards?"),
    # ---- Clinical Dietetics & Therapeutic Nutrition (11)
    Q("A child has swollen feet, a swollen belly, thin pale hair and a diet of thin cassava porridge. The most likely diagnosis is:", "Kwashiorkor",
      [("Marasmus", "Marasmus has no oedema."), ("Rickets", "Rickets affects the bones and is due to vitamin D and calcium lack."), ("Scurvy", "Scurvy is due to vitamin C lack.")],
      [("Signs", "Oedema, fatty liver, hair change and low protein diet.")], T_PEM, "Application", "Which form has oedema?"),
    Q("An adult has a mass of 63 kg and a height of 1.50 m. His BMI is:", "28.0 kg/m²",
      [("42.0 kg/m²", "That divides by the height without squaring it."), ("21.0 kg/m²", "That divides by 3.0, a wrong squaring of 1.5."), ("94.5 kg/m²", "That multiplies mass by height.")],
      [("Square the height", "1.50² = 2.25."), ("BMI", "63 ÷ 2.25 = 28.0.")], T_PEM, "Calculation", "Square the height first."),
    Q("Insulin lowers blood glucose mainly by:", "Helping glucose enter cells and stimulating storage as glycogen",
      [("Breaking down glycogen in the liver", "That is the action of glucagon."), ("Making new glucose from amino acids", "That is gluconeogenesis, stimulated by glucagon."), ("Increasing the kidney's release of glucose", "That would raise blood glucose.")],
      [("Insulin", "Uptake into liver, muscle and fat and glycogen formation.")], T_DIAB, "Concept", "Which hormone lowers blood glucose?"),
    Q("Which statement about type 2 diabetes is correct?", "It involves insulin resistance and is strongly linked to obesity and inactivity",
      [("It is always autoimmune", "Type 1 is autoimmune."), ("It can only be treated with insulin", "Diet, activity and tablets are also used."), ("It affects only children", "It mostly affects adults.")],
      [("Type 2", "Insulin resistance, weight and inactivity.")], T_DIAB, "Concept", "Which type is linked to obesity?"),
    Q("A 'salt' intake of 5 g a day corresponds to a sodium intake of about:", "2 g",
      [("5 g", "Salt is not all sodium."), ("12 g", "Sodium is less than the salt mass."), ("0.5 g", "That is only 10 per cent; sodium is about 39 per cent of salt.")],
      [("Conversion", "5 × 0.393 = 1.97 g.")], T_HYP, "Calculation", "Sodium is about 39 per cent of salt."),
    Q("Which pair of fats most clearly raises LDL cholesterol?", "Saturated fat and trans fat",
      [("Monounsaturated and polyunsaturated fat", "These tend to lower LDL."), ("Omega-3 fat and fibre", "These do not raise LDL."), ("Water and vitamin C", "These do not affect LDL.")],
      [("Fats", "Saturated and trans fats raise LDL; trans fat also lowers HDL.")], T_HYP, "Concept", "Which fats are 'bad'?"),
    Q("A patient with chronic kidney disease and high blood potassium is best advised to:", "Limit potassium-rich foods and leach vegetables and tubers before cooking",
      [("Eat as many bananas as possible", "Bananas are rich in potassium."), ("Drink unlimited fluids", "Fluid is often restricted."), ("Increase salt for flavour", "Salt is restricted.")],
      [("Potassium control", "Avoid large amounts of high-potassium foods; soaking and boiling reduces potassium.")], T_RENAL, "Application", "What can the kidney no longer excrete?"),
    Q("The sodium-glucose co-transport mechanism is the basis of:", "Oral rehydration solution",
      [("Pasteurization", "That is a heat treatment."), ("Blanching", "That is a heat treatment."), ("Food irradiation", "That uses ionizing radiation.")],
      [("ORS", "Glucose helps sodium and water to be absorbed in the small intestine.")], T_RENAL, "Concept", "Which treatment for diarrhoea is it?"),
    Q("Which food is safe for a person with celiac disease?", "Boiled cassava",
      [("Wheat bread", "Wheat contains gluten."), ("Barley malt drink", "Barley contains gluten."), ("Wheat semolina", "Semolina is wheat.")],
      [("Gluten-free", "Cassava is a root and contains no gluten.")], T_CELI, "Application", "Avoid wheat, barley and rye."),
    Q("The enzyme that is deficient in lactose intolerance is:", "Lactase",
      [("Amylase", "Amylase digests starch."), ("Lipase", "Lipase digests fats."), ("Pepsin", "Pepsin digests protein.")],
      [("Lactase", "It splits lactose into glucose and galactose.")], T_CELI, "Recall", "Name the enzyme that acts on lactose."),
    Q("Villous atrophy in celiac disease leads to malabsorption because:", "The absorptive surface of the small intestine is reduced",
      [("The stomach stops making acid", "The villi are in the small intestine."), ("The liver makes too much bile", "That is not the mechanism."), ("The colon absorbs too much water", "The problem is in the small intestine.")],
      [("Mechanism", "Flattened villi have less surface area.")], T_CELI, "Reasoning", "What do villi do?"),
    # ---- Community Nutrition, Epidemiology & Food Security (7)
    Q("A height-for-age Z-score below −2 in a child indicates:", "Stunting",
      [("Wasting", "Wasting is low weight-for-height."), ("Overweight", "Overweight is a high weight-for-height."), ("Normal growth", "Normal growth lies between −2 and +2.")],
      [("Cut-off", "HAZ below −2 is stunting.")], T_STATUS, "Recall", "Which index is based on height?"),
    Q("A child's weight is 7.8 kg. The reference median is 9.0 kg and the SD is 0.8 kg. The weight-for-age Z-score is:", "−1.5",
      [("+1.5", "The child is below the median, so Z is negative."), ("−1.2", "That is the difference in kg, not divided by the SD."), ("−0.15", "That divides by 8 instead of 0.8.")],
      [("Formula", "Z = (7.8 − 9.0) ÷ 0.8 = −1.5.")], T_STATUS, "Calculation", "Observed minus median, over SD."),
    Q("MUAC below 115 mm in a child aged 6 to 59 months is classed as:", "Severe acute malnutrition",
      [("Moderate acute malnutrition", "That is 115 to under 125 mm."), ("Normal", "Normal is 125 mm or more."), ("Overweight", "MUAC under 115 mm is not overweight.")],
      [("MUAC", "Under 115 mm severe.")], T_STATUS, "Recall", "Compare with 115 mm."),
    Q("Iodization of salt is an example of:", "Mass fortification to prevent goitre and brain damage",
      [("Biofortification", "That uses plant breeding."), ("Dietary diversification", "That changes the foods eaten."), ("Supplementation with capsules", "That uses capsules or tablets.")],
      [("Fortification", "A staple food carries the nutrient.")], T_FORT, "Concept", "What vehicle carries the iodine?"),
    Q("Which of these is a food fad?", "A short-lived craze for a single 'superfood' diet",
      [("A custom that forbids certain meats to women", "That is a taboo."), ("A belief that pregnant women should eat less", "That is a fallacy."), ("Iodized salt", "That is fortification.")],
      [("Fad", "Short-lived fashion.")], T_FORT, "Concept", "Which term means a short-lived fashion?"),
    Q("A family has enough food in the market but poor sanitation, and the children have frequent diarrhoea. Which dimension of food security is mainly weak?", "Utilization",
      [("Availability", "Food is available."), ("Access", "The family can obtain the food."), ("Production", "Production is not a dimension.")],
      [("Utilization", "Safe water, sanitation and health let the body use food.")], T_FSEC, "Application", "Is the problem supply, income or use of food?"),
    Q("Which action protects the stability dimension of food security?", "Early warning systems and grain reserves for droughts",
      [("Hand-washing campaigns", "These improve utilization."), ("Cash transfers only", "These help access in the short term."), ("Fortifying salt", "That improves nutrient utilization.")],
      [("Stability", "Reserves and early warning limit the effect of shocks.")], T_FSEC, "Application", "Which action prepares for shocks?"),
]
assert len(P1) == 50, len(P1)
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="fsu2-exam-paper-1-multiple-choice",
                         questions=build(P1, 331), mock=True, time_limit_minutes=90))

# ------------------------------------------------------------------ Paper 2 practice paper A (26 parts)
P2 = [
    # Question 1 (Section A, application of nutritional science): energy and BMR (3)
    Q("Question 1(a). Basal Metabolic Rate (BMR) is best defined as the energy the body uses:", "At complete rest, awake, fasting and in a comfortable temperature, to keep vital functions going",
      [("During hard physical work", "That is part of total energy expenditure, not the basal rate."), ("To digest and absorb a meal", "That is the thermic effect of food."), ("While asleep only", "BMR is measured awake and at rest.")],
      [("Definition", "BMR is the minimum energy for vital functions.")], T_STATUS, "Recall", "Think of the body at complete rest."),
    Q("Question 1(b). Which of the following raises BMR?", "Fever and a greater proportion of lean body mass",
      [("Fasting for several weeks", "Prolonged under-nutrition lowers BMR."), ("Advancing age", "BMR falls with age."), ("A cold-weather coat", "A coat does not change the basal rate in this way.")],
      [("Factors", "Fever, lean mass, thyroxine, growth and pregnancy raise BMR.")], T_STATUS, "Concept", "Which factor involves more active tissue?"),
    N("Question 1(c). A woman aged 25, 60 kg and 160 cm: BMR = 10 × mass + 6.25 × height − 5 × age − 161 (kcal/day). Her total energy expenditure is BMR × 1.5. What is it in kcal per day?", 1971,
      [("BMR", "10(60) + 6.25(160) − 5(25) − 161 = 600 + 1000 − 125 − 161 = 1 314."), ("TEE", "1 314 × 1.5 = 1 971 kcal.")], T_STATUS, "Calculation", "Find the BMR first, then apply the activity factor.", tol=1, unit="kcal/day"),
    # Question 2 (Section A): protein quality and food composition table (3)
    Q("Question 2(a). Which food is a high biological value (HBV) protein?", "Egg",
      [("Maize", "Cereals are limited in lysine."), ("Cassava", "Cassava is low in protein."), ("Plantain", "Plantain is low in protein.")],
      [("HBV", "Contains all the essential amino acids in proportions close to needs.")], T_PEM, "Recall", "Which food has a balanced amino acid pattern?"),
    Q("Question 2(b). A meal of maize and beans has a better protein value than maize alone because:", "Each food supplies the essential amino acid that the other lacks",
      [("Beans contain no protein", "Beans are rich in protein."), ("Maize contains all essential amino acids in large amounts", "Maize is low in lysine."), ("The two foods cancel out each other's amino acids", "They complement each other.")],
      [("Complementation", "Cereals are low in lysine, legumes in methionine.")], T_PEM, "Reasoning", "Think of limiting amino acids."),
    N("Question 2(c). Using a teaching value (invented): dried beans contain 335 kcal per 100 g. How many kcal are in 150 g?", 502.5,
      [("Scale", "335 × 1.5 = 502.5 kcal.")], T_STATUS, "Calculation", "Scale the value per 100 g.", tol=0.5, unit="kcal"),
    # Question 3 (Section B, food consumption and health): blood glucose regulation (4)
    Q("Question 3(a). After a meal, rising blood glucose stimulates:", "Beta cells of the pancreas to release insulin",
      [("Alpha cells to release insulin", "Alpha cells release glucagon."), ("Beta cells to release glucagon", "Beta cells release insulin."), ("The liver to release adrenaline", "The liver does not release adrenaline in this response.")],
      [("Stimulus", "High glucose triggers insulin from beta cells.")], T_DIAB, "Recall", "Which cells respond to high glucose?"),
    Q("Question 3(b). Which action by the liver is stimulated by glucagon?", "Conversion of glycogen to glucose",
      [("Conversion of glucose to glycogen", "That is stimulated by insulin."), ("Conversion of glucose to fat", "Also an insulin effect."), ("Removal of insulin from the blood", "Not the action of glucagon.")],
      [("Glucagon", "Glycogenolysis and gluconeogenesis raise blood glucose.")], T_DIAB, "Concept", "Which process raises glucose?"),
    N("Question 3(c). A portion of a food has GI 55 and contains 40 g of carbohydrate (teaching values). What is its glycaemic load?", 22,
      [("Formula", "GL = GI × carbohydrate ÷ 100."), ("Calculate", "55 × 40 ÷ 100 = 22.")], T_DIAB, "Calculation", "Multiply, then divide by 100.", tol=0.1, unit=""),
    Q("Question 3(d). The diet of a patient with type 2 diabetes should:", "Provide measured, low-GI carbohydrate spread through the day with fibre and weight control",
      [("Exclude all carbohydrate", "Carbohydrate is the main energy source."), ("Include one large meal at night", "Large meals give large glucose peaks."), ("Use sweet drinks to prevent low sugar at every meal", "These raise glucose too fast.")],
      [("Principles", "Quality, quantity and timing of carbohydrate.")], T_DIAB, "Application", "Which advice steadies blood glucose?"),
    # Question 4 (Section B): atherosclerosis and hypertension (3)
    Q("Question 4(a). Atherosclerosis differs from arteriosclerosis in that atherosclerosis:", "Is a type of arteriosclerosis caused by plaque of cholesterol and fat in the artery wall",
      [("Is a hardening of veins", "Both affect arteries."), ("Has no link to cholesterol", "Cholesterol is central to atheroma."), ("Is the general term for all artery hardening", "That is arteriosclerosis.")],
      [("Distinction", "Arteriosclerosis is the general term; atherosclerosis is the plaque type.")], T_HYP, "Concept", "Which term is the wider term?"),
    N("Question 4(b). Total cholesterol 6.4, HDL 1.4 and triglycerides 1.6 mmol/L. Estimate LDL = TC − HDL − TG ÷ 2.2 (mmol/L, 1 decimal place).", 4.3,
      [("Substitute", "6.4 − 1.4 − 1.6 ÷ 2.2."), ("Calculate", "6.4 − 1.4 − 0.73 = 4.27, about 4.3 mmol/L.")], T_HYP, "Calculation", "Divide TG by 2.2 first.", tol=0.05, unit="mmol/L"),
    Q("Question 4(c). Which dietary advice best lowers blood pressure?", "Reduce salt and increase fruit, vegetables and legumes",
      [("Add stock cubes to meals", "They are high in sodium."), ("Replace fish with smoked, salted fish", "Salted fish raises sodium intake."), ("Eat more fatty meat", "That raises saturated fat.")],
      [("DASH", "Less sodium and more potassium-rich foods.")], T_HYP, "Application", "Which change lowers sodium?"),
    # Question 5 (Section C, food science): rancidity, margarine, thermal processing (4)
    Q("Question 5(a). Oxidative rancidity is caused by:", "Reaction of unsaturated fatty acids with oxygen, producing peroxides and then volatile aldehydes and ketones",
      [("Growth of yeast in water", "That is fermentation."), ("Absorption of water by starch", "That is not rancidity."), ("Enzymatic browning of fruit", "That involves phenols, not fats.")],
      [("Mechanism", "Auto-oxidation of unsaturated fat gives the rancid odour.")], T_OIL, "Concept", "Which reaction involves oxygen and fat?"),
    Q("Question 5(b). Which measure helps prevent rancidity in cooking oil?", "Store it airtight, cool and dark, and add an antioxidant",
      [("Leave it in an open pan in the sun", "Heat, light and air speed oxidation."), ("Add copper utensils", "Copper catalyses oxidation."), ("Re-use it for deep frying many times", "Repeated heating speeds spoilage.")],
      [("Prevention", "Exclude oxygen, light and metals; add antioxidants.")], T_OIL, "Application", "Remove oxygen, light and heat."),
    Q("Question 5(c). Which sequence correctly outlines margarine manufacture?", "Refined oil, hydrogenation or blending, mixing with the aqueous phase, emulsifying, chilling and working, packing",
      [("Milk, starter and rennet, curd cutting, whey draining, pressing and ripening", "That is cheese manufacture."), ("Grain, malting, mashing, boiling with hops and fermentation", "That is brewing."), ("Fresh fruit, washing, crushing, pasteurizing and filling", "That is fruit juice.")],
      [("Margarine", "Fat phase plus aqueous phase, emulsified, chilled and worked.")], T_OIL, "Recall", "Which process makes a water-in-oil emulsion?"),
    N("Question 5(d). A process of 8 minutes at 115 °C is equivalent to how many minutes at 121 °C when z = 10 °C? (1 decimal place.)", 2.0,
      [("Rule", "Equivalent time = t × 10^((T − 121) ÷ z)."), ("Calculate", "8 × 10^(−0.6) = 8 × 0.251 = 2.0 min.")], T_THERM, "Calculation", "Each 10 °C lower multiplies the lethal rate by 1/10.", tol=0.1, unit="min"),
    # Question 6 (Section C): enzymes, dehydration, dairy (3)
    Q("Question 6(a). Enzyme selectivity (specificity) is shown when:", "Amylase acts on starch but not on protein, because of the shape of its active site",
      [("Amylase speeds up the digestion of starch", "That shows catalytic function."), ("Amylase is not changed by the reaction", "That is another catalytic property."), ("Amylase is destroyed at a high temperature", "That is denaturation.")],
      [("Selectivity", "Each enzyme fits a particular substrate.")], T_CER, "Concept", "Which statement is about substrate choice?"),
    N("Question 6(b). 200 kg of fruit with 75 per cent moisture is dried to 15 per cent moisture. How many kilograms of water are removed (1 decimal place)?", 141.2,
      [("Dry solids", "200 × 0.25 = 50 kg."), ("Final mass", "50 ÷ 0.85 = 58.8 kg."), ("Water removed", "200 − 58.8 = 141.2 kg.")], T_DEHY, "Calculation", "Dry solids are unchanged.", tol=0.2, unit="kg"),
    Q("Question 6(c). In cheese making, milk is made to set mainly by:", "Rennet (chymosin) acting on casein, with acid from starter bacteria",
      [("Sublimation of water under vacuum", "That is freeze-drying."), ("Addition of hexane", "Hexane is used to extract oil."), ("Heating to 121 °C in a can", "That is canning.")],
      [("Cheese", "Rennet and acid coagulate casein into curd.")], T_MEAT, "Concept", "Which enzyme clots milk?"),
    # Question 7 (Section D, community health and nutrition): food habits and fortification (3)
    Q("Question 7(a). A community forbids children to eat eggs. This is a:", "Food taboo",
      [("Food fad", "A fad is a short-lived fashion."), ("Food fallacy", "A fallacy is a false belief."), ("Food additive", "No additive is involved.")],
      [("Taboo", "Prohibition by custom.")], T_FORT, "Concept", "Is it a custom of prohibition?"),
    N("Question 7(b). Flour is to carry 30 mg of iron per kg. How many grams of iron compound containing 20 per cent iron are needed for 250 kg of flour?", 37.5,
      [("Iron needed", "30 × 250 = 7 500 mg = 7.5 g."), ("Compound", "7.5 ÷ 0.20 = 37.5 g.")], T_FORT, "Calculation", "Find iron first, then divide by the iron fraction.", tol=0.1, unit="g"),
    Q("Question 7(c). A suitable food vehicle for mass fortification is one that is:", "Eaten regularly by most people and processed in a few central plants",
      [("Eaten rarely by a few people", "Coverage would be poor."), ("Made at home in many different ways", "Control would be difficult."), ("Changed in taste by the added nutrient", "Taste must not change.")],
      [("Vehicle", "Wide, regular, central.")], T_FORT, "Concept", "Think about reach and control."),
    # Question 8 (Section D): assessment and food security (3)
    N("Question 8(a). A child's weight is 8.1 kg. The reference median is 10.0 kg and SD is 0.9 kg. What is the weight-for-age Z-score (2 decimal places)?", -2.11,
      [("Formula", "Z = (8.1 − 10.0) ÷ 0.9."), ("Calculate", "−1.9 ÷ 0.9 = −2.11, so the child is underweight (below −2).")], T_STATUS, "Calculation", "Observed minus median, divided by SD.", tol=0.02, unit=""),
    Q("Question 8(b). Which dimension of food security refers to whether the body can use the food eaten?", "Utilization",
      [("Availability", "That is supply."), ("Access", "That is obtaining food."), ("Stability", "That is security over time.")],
      [("Utilization", "Safe food, clean water, health and care.")], T_FSEC, "Recall", "Which dimension involves health and water?"),
    Q("Question 8(c). Which measure addresses access to food for poor households in the lean season?", "Cash transfers or public works programmes",
      [("Hand-washing campaigns", "That addresses utilization."), ("Raising export of staple crops", "That could reduce local supply."), ("Banning all food imports", "That could raise prices.")],
      [("Access", "Income support helps households to buy food.")], T_FSEC, "Application", "Which measure raises household income?"),
]
assert len(P2) == 26, len(P2)
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="fsu2-exam-paper-2-essays",
                         questions=build(P2, 332), mock=True, time_limit_minutes=150))
