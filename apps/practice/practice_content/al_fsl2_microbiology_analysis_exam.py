"""A Level Food Science and Nutrition (0740), Lower Sixth: practice sets for Food Microbiology & Food Safety, Sensory Evaluation & Food Analysis and the Examination module.

One 8-question set per lesson (7 topic lessons, 3 examination lessons), plus 'Paper 1 mock exam A' (50 multiple-choice questions
across all five Lower Sixth modules in proportion to their topic counts: 12, 12, 9, 10 and 7) and 'Paper 2 practice paper A'
(25 auto-markable parts in 8 numbered questions). Exam facts are only those of the Board's 2023 subject report (Paper 1 = 50
multiple-choice questions, 35 percent, 1 h 30; Paper 2 = essay type, 40 percent, 3 h; Paper 3 = practical, 25 percent, 2 h). The timings
of the mock papers (90 and 150 minutes) are KKEVO practice settings. Essays cannot be marked automatically, so the Paper 2 practice paper is a
structured version with multiple-choice and numeric parts. Numerical answers (growth, fermentation yield, sensory significance,
Kjeldahl, Soxhlet, titratable acidity, moisture, Karl Fischer, energy) were checked by script. Teaching figures are invented for practice.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("food-and-nutrition", "lower-sixth")

M_CHE = "Food Chemistry of Macronutrients"
M_MIC = "Food Microbiology & Food Safety"
M_SEN = "Sensory Evaluation & Food Analysis"
M_EXAM = "Examination"

T_WAT = "Water activity"
T_CHO = "Carbohydrate functional properties"
T_LIP = "Lipid chemistry"
T_PROT = "Protein structure and functional properties"
T_MAI = "Maillard browning"
T_VIT = "Vitamins and processing"
T_MIN = "Minerals and anti-nutritional factors"
T_PIG = "Food pigments"
T_ENZ = "Enzymatic browning"
T_COL = "Colloidal food systems"
T_DIG = "Digestion and absorption"
T_MET = "Metabolic pathways"
T_BMR = "Energy expenditure and BMR"
T_ENR = "Energy requirement calculations"
T_FAC = "Factors affecting microbial growth"
T_FER = "Beneficial fermentation"
T_INF = "Foodborne infections and intoxications"
T_AFL = "Aflatoxins and mycotoxins"
T_SEN = "Sensory evaluation methods"
T_PRO = "Proximate analysis"
T_TIT = "Titratable acidity and moisture determination"
T_P1 = "Paper 1"
T_P2 = "Paper 2"
T_P3 = "Paper 3"

SETS = []


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


# ------------------------------------------------------------------ 1. Factors affecting microbial growth
X = [
    Q("Which is an INTRINSIC factor affecting microbial growth in a food?", "Water activity of the food",
      [("The temperature of the store", "Storage temperature is an extrinsic factor (outside the food)."), ("The relative humidity of the air", "Humidity of the surroundings is extrinsic."), ("The gas in the package", "The atmosphere around the food is extrinsic.")],
      [("Intrinsic", "Intrinsic factors are properties of the food: pH, a_w, nutrients, Eh and antimicrobials.")], T_FAC, "Recall", "Is the factor part of the food or part of its surroundings?"),
    Q("Which phase of the bacterial growth curve shows the fastest rate of increase in cell number?", "The log (exponential) phase",
      [("The lag phase", "In lag the cells are adjusting and divide little."), ("The stationary phase", "In stationary births equal deaths, so the number is steady."), ("The death phase", "In death the number falls.")],
      [("Growth curve", "The straight steep part of the log graph is the log phase.")], T_FAC, "Recall", "Where is the line steepest?"),
    N("A food starts with 500 bacterial cells. The generation time is 30 minutes. How many cells are there after 3 hours? (No lag phase.)", 32000,
      [("Generations", "180 min ÷ 30 min = 6 generations."), ("Growth rule", "N = 500 × 2^6 = 500 × 64 = 32 000.")], T_FAC, "Calculation", "Find the number of generations first.", tol=1, unit="cells"),
    Q("Salted dried fish keeps for months without refrigeration. The main reason is that it has", "A low water activity",
      [("A very low pH", "Salted fish is not acid; its pH is near neutral."), ("A high redox potential", "Redox potential is not the main control in dried fish."), ("A high temperature", "It is stored at ordinary temperature, not a high one.")],
      [("Water activity", "Salt and drying bind water so that microbes cannot use it.")], T_FAC, "Application", "What have salt and drying done to available water?"),
    Q("The graph shows the growth of bacteria in a closed culture. Which letter shows the stationary phase?", "C",
      [("A", "A is the lag phase, where the cells adjust and the number hardly changes."), ("B", "B is the log phase, where the number rises fastest."), ("D", "D is the death phase, where the number falls.")],
      [("Reading the graph", "In the stationary phase the line is flat at the top because nutrients run out and wastes build up.")], T_FAC, "Interpretation", "Look for the flat part at the highest level.",
      diagram="alfsl2-growth-curve-q.svg", alt="A growth curve with four regions labelled A, B, C and D in order from left to right; no phase names are given"),
    Q("A bottle of fruit juice (pH 3.5) goes off in a warm room. Which organisms are most likely to spoil it?", "Yeasts and moulds",
      [("Most pathogenic bacteria such as Salmonella", "Most bacteria do not grow well at pH 3.5."), ("Clostridium botulinum", "It needs a pH above about 4.6."), ("Viruses", "Viruses do not multiply in food, only in living host cells.")],
      [("pH", "Yeasts and moulds tolerate acid; most bacteria do not.")], T_FAC, "Application", "Which group tolerates low pH?"),
    Q("Why is cooked rice left for six hours in a warm kitchen more dangerous than cooked rice kept in a refrigerator?", "In a warm kitchen the temperature is in the danger zone, so bacteria multiply to large numbers",
      [("Rice grows bacteria only when cold", "Growth is slower in the cold, not faster."), ("Cooking adds bacteria to the rice", "Cooking kills most vegetative cells; the danger comes from growth afterwards."), ("Warm rice has no water activity", "Cooked rice has a high a_w.")],
      [("Temperature", "Between about 5 and 60 degrees C the generation time is short, so numbers rise quickly.")], T_FAC, "Reasoning", "Think about generation time at different temperatures."),
    Q("Which statement best describes hurdle technology?", "Combining several mild barriers, such as low pH, reduced a_w and cooling, to keep food safe",
      [("Using one very strong preservative", "Hurdle technology uses several barriers, not one."), ("Heating all food to above 100 degrees C", "That is thermal processing, not the combination of hurdles."), ("Packing food in the light", "Light is not a hurdle used in this way.")],
      [("Hurdles", "Each hurdle stops some microbes; together they stop all, with less damage to the food.")], T_FAC, "Concept", "The word 'hurdle' is plural in the idea."),
]
SETS.append(practice_set(module=M_MIC, topic=T_FAC, title="Growth curves, pH, a_w and temperature", lesson="fsl2-factors-microbial-growth", questions=build(X, 201)))

# ------------------------------------------------------------------ 2. Beneficial fermentation
X = [
    Q("Which organism makes bread dough rise?", "Saccharomyces cerevisiae (yeast)",
      [("Lactobacillus bulgaricus", "It makes lactic acid in yoghurt, not the gas that raises bread."), ("Aspergillus flavus", "It makes aflatoxin on groundnuts and maize."), ("Clostridium botulinum", "It is a pathogen that makes a neurotoxin.")],
      [("Yeast", "Yeast ferments sugar to ethanol and carbon dioxide; the gas raises the dough.")], T_FER, "Recall", "Which fungus makes carbon dioxide?"),
    Q("What is the main product of homofermentative lactic acid bacteria growing on glucose?", "Lactic acid",
      [("Ethanol and carbon dioxide", "That is alcoholic fermentation by yeast, or part of the heterofermentative pathway."), ("Acetic acid only", "Acetic acid is the product of acetic acid bacteria acting on ethanol."), ("Citric acid", "Citric acid is made by Aspergillus niger, not by lactic acid bacteria.")],
      [("Homolactic", "Glucose gives two molecules of lactic acid.")], T_FER, "Recall", "What does the name 'lactic acid bacteria' tell you?"),
    N("A yeast ferments 450 g of glucose completely to ethanol and carbon dioxide. What mass of ethanol is formed in theory? (Mr: glucose 180, ethanol 46.)", 230,
      [("Moles of glucose", "450 ÷ 180 = 2.5 mol."), ("Moles of ethanol", "C6H12O6 gives 2 ethanol, so 5.0 mol."), ("Mass", "5.0 × 46 = 230 g.")], T_FER, "Calculation", "Each glucose gives two ethanol.", tol=0.5, unit="g"),
    Q("In yoghurt, why does the milk thicken during fermentation?", "Lactic acid lowers the pH and the casein coagulates to form a gel",
      [("The yeast makes carbon dioxide that foams the milk", "Yoghurt is made by bacteria, and the thickening is not a foam."), ("The bacteria remove all the water", "Water is not removed; the milk protein sets."), ("The fat turns to protein", "Fat does not turn into protein.")],
      [("Yoghurt", "Acid brings casein to its isoelectric point and the protein network traps the water.")], T_FER, "Concept", "What does acid do to casein?"),
    Q("Which is NOT a way in which fermentation helps preserve food?", "It adds oxygen to the food",
      [("It lowers the pH", "Acid production is a preserving effect."), ("It makes bacteriocins that stop other bacteria", "Bacteriocins such as nisin are an antimicrobial effect."), ("It uses up nutrients, so spoilage organisms compete poorly", "Competition for nutrients is a real effect.")],
      [("Preservation", "Fermentation works by acid, antimicrobials and competition; it does not add oxygen.")], T_FER, "Concept", "Pick the statement that is false."),
    Q("A fermented cassava product has fewer cyanogenic glycosides than the raw root. This benefit of fermentation is best described as", "Detoxification",
      [("Pasteurisation", "Pasteurisation is a mild heat treatment, not a microbial process."), ("Hydrogenation", "Hydrogenation is the addition of hydrogen to fats."), ("Retrogradation", "Retrogradation is the re-association of starch chains.")],
      [("Detoxification", "Microbial enzymes break down the glycosides, which lowers the cyanide released.")], T_FER, "Application", "Which word means 'making less toxic'?"),
    Q("Which statement about starter cultures is correct?", "They give a faster, more reliable and safer fermentation than natural fermentation alone",
      [("They are used only for alcoholic drinks", "They are used in yoghurt, cheese, bread, sausages and many others."), ("They are always killed before they work", "The live culture does the fermentation."), ("They are chemical preservatives", "They are living microbes, not chemicals.")],
      [("Starters", "Selected strains reduce the risk that unwanted microbes dominate.")], T_FER, "Concept", "Why would a producer add a chosen culture?"),
    Q("Palm wine is fermented sap that turns sour within a day or two. A main reason is that", "Yeasts make alcohol and bacteria continue to make acids as the fermentation goes on",
      [("Palm sap has no sugar", "Palm sap is rich in sugar, which is why it ferments."), ("Heat makes the sugar disappear", "The sugar is used by microbes, not lost by heat."), ("Only moulds can grow in sap", "Yeasts and bacteria dominate sap, not moulds.")],
      [("Palm wine", "Mixed yeasts and bacteria in the open sap: alcohol first, then acids (acetic and lactic).")], T_FER, "Application", "Think of sugar, yeast and later bacteria."),
]
SETS.append(practice_set(module=M_MIC, topic=T_FER, title="Lactic acid bacteria, yeasts and fermented foods", lesson="fsl2-beneficial-fermentation", questions=build(X, 202)))

# ------------------------------------------------------------------ 3. Foodborne infections and intoxications
X = [
    Q("A foodborne INTOXICATION is caused by", "A toxin already formed in the food",
      [("Living pathogens that invade the gut", "That is an infection."), ("A chemical added by the cook", "Intoxication here means toxin from microbial growth, not added chemicals."), ("Viruses in water", "Viruses are not the cause of intoxication.")],
      [("Definition", "In an intoxication the bacteria grew earlier and released toxin in the food; they need not be alive when eaten.")], T_INF, "Recall", "Where was the toxin made?"),
    Q("Which organism is the usual cause of food poisoning from raw or undercooked eggs and poultry?", "Salmonella",
      [("Clostridium botulinum", "It is found in low-acid canned food, soil and fish, not typically eggs."), ("Aspergillus flavus", "It is a mould that makes aflatoxin."), ("Lactobacillus", "It is a useful lactic acid bacterium.")],
      [("Salmonella", "It lives in the gut of poultry and contaminates eggs and meat.")], T_INF, "Recall", "Which pathogen lives in poultry?"),
    Q("A food handler with an infected finger prepares sandwiches that are not refrigerated. Guests vomit 3 hours later, without fever. The likely cause is", "Staphylococcus aureus enterotoxin",
      [("Salmonella infection", "Salmonella usually causes fever and diarrhoea after a longer time."), ("Clostridium botulinum", "Botulism shows paralysis after 12 to 36 hours."), ("Aflatoxin", "Aflatoxin causes long-term liver disease.")],
      [("Staphylococcus", "A skin source, short onset (1 to 6 hours) and vomiting without fever point to the toxin.")], T_INF, "Application", "Think of the short onset time."),
    Q("Why can reheating NOT make food safe after Staphylococcus aureus has grown in it?", "The enterotoxin is heat stable",
      [("The bacteria become more numerous when heated", "Heat kills the living cells; the problem is the toxin."), ("The toxin is a spore", "A toxin is a protein, not a spore."), ("Heat makes the toxin more poisonous", "Heat does not change it in this way.")],
      [("Heat stability", "The toxin survives normal cooking temperatures.")], T_INF, "Reasoning", "What survives after the cells are dead?"),
    Q("Which statement about Clostridium botulinum is correct?", "Its spores resist boiling but its toxin is destroyed by boiling for about 10 minutes",
      [("Its toxin resists boiling but its spores are killed at 60 degrees C", "That is the reverse of the facts."), ("It needs oxygen to grow", "It is an anaerobe."), ("It grows best in acidic fruit juice", "It does not grow below about pH 4.6.")],
      [("Botulism", "Spores are heat resistant; the neurotoxin is heat labile.")], T_INF, "Concept", "Spores and toxin behave differently to heat."),
    N("A cooked dish has 10 Salmonella cells and the generation time at room temperature is 20 minutes with no lag. How many hours does it take to reach 100 000 cells? Give your answer to one decimal place.", 4.4,
      [("Generations", "n = log2(100 000 ÷ 10) = log2(10 000) = 13.3."), ("Time", "13.3 × 20 = 266 minutes = 4.4 hours.")], T_INF, "Calculation", "How many doublings are needed to multiply by 10 000?", tol=0.1, unit="hours"),
    Q("Which control is most useful against cross-contamination in a kitchen?", "Separate boards and knives for raw meat and ready-to-eat food, and wash hands",
      [("Boiling all the water used to wash the floor", "Floor water is not the main route."), ("Keeping the kitchen warm", "Warmth helps bacteria grow."), ("Using a bigger refrigerator", "Cold helps with growth but does not stop transfer from raw to cooked food.")],
      [("Cross-contamination", "Transfer of microbes from raw food or hands to cooked food is stopped by separation and washing.")], T_INF, "Application", "How do microbes move from raw to cooked food?"),
    Q("Clostridium perfringens food poisoning occurs when large numbers of living cells are eaten and then produce toxin in the gut. This type of illness is called", "A toxico-infection",
      [("A pure intoxication", "In an intoxication the toxin is already in the food."), ("A pure infection by invasion", "The illness is due to toxin, not to invasion alone."), ("A mycotoxicosis", "A mycotoxicosis is caused by a mould toxin.")],
      [("Toxico-infection", "Living cells are eaten and toxin is released in the gut.")], T_INF, "Concept", "Both cells and toxin are involved."),
]
SETS.append(practice_set(module=M_MIC, topic=T_INF, title="Infection, intoxication and control", lesson="fsl2-foodborne-infections-intoxications", questions=build(X, 203)))

# ------------------------------------------------------------------ 4. Aflatoxins and mycotoxins
X = [
    Q("Which fungus is the main producer of aflatoxin?", "Aspergillus flavus",
      [("Saccharomyces cerevisiae", "It is baker's yeast and not a toxin producer in food."), ("Penicillium camemberti", "It is a cheese mould, not an aflatoxin producer."), ("Rhizopus", "It is a bread and tempeh mould, not the aflatoxin species.")],
      [("Aflatoxin", "Aspergillus flavus and A. parasiticus make the aflatoxins.")], T_AFL, "Recall", "The first letters 'afla' give a clue."),
    Q("Which pair of foods is most often contaminated with aflatoxin?", "Groundnuts and maize",
      [("Fresh tomatoes and lettuce", "Fresh moist vegetables spoil by other organisms."), ("Fresh fish and milk", "Fish and milk are spoiled by bacteria; milk can contain M1 only through contaminated feed."), ("Sugar and salt", "These have a very low a_w and are not a medium for mould.")],
      [("Crops", "Groundnuts and maize stored warm and damp are the classic examples.")], T_AFL, "Recall", "Think of stored crops in warm, humid areas."),
    Q("Which set of conditions most favours aflatoxin formation in stored maize?", "Warm, humid store, grain moisture above the safe level and insect damage",
      [("Cold, dry store with sealed bags", "These conditions stop mould growth."), ("Boiled grain in a closed pot", "The mould is killed and not growing."), ("Dry grain on a clean rack in the sun", "Rapid drying is a control, not a cause.")],
      [("Conditions", "Moisture, warmth, humidity and damaged grain allow Aspergillus to grow.")], T_AFL, "Application", "What does a mould need?"),
    Q("Why is boiling contaminated groundnut sauce not a solution?", "Aflatoxin is heat stable and survives normal cooking",
      [("Boiling makes the toxin more poisonous", "Cooking does not increase toxicity."), ("The toxin is a living spore", "A mycotoxin is a chemical compound, not a living cell."), ("Boiling dissolves the toxin into the air", "It is not volatile.")],
      [("Stability", "Mycotoxins are small stable molecules not destroyed at cooking temperatures.")], T_AFL, "Reasoning", "What is left after the mould is killed?"),
    Q("Which is the main chronic health risk linked to long-term exposure to aflatoxin B1?", "Liver cancer",
      [("Scurvy", "Scurvy is due to a lack of vitamin C."), ("Rickets", "Rickets is due to a lack of vitamin D or calcium."), ("Goitre", "Goitre is due to iodine deficiency.")],
      [("Health effects", "Aflatoxin B1 is a liver carcinogen, especially where hepatitis B is common.")], T_AFL, "Recall", "Which organ does aflatoxin damage?"),
    N("A maize meal sample contains 12 µg/kg of aflatoxin (a figure invented for practice). A child eats 250 g of it. How many µg of aflatoxin are eaten?", 3,
      [("Convert mass", "250 g = 0.250 kg."), ("Multiply", "12 µg/kg × 0.250 kg = 3.0 µg.")], T_AFL, "Calculation", "Convert grams to kilograms first.", tol=0.05, unit="µg"),
    Q("Which practice best reduces aflatoxin risk after harvesting groundnuts?", "Dry quickly to the safe moisture, sort out mouldy nuts and store dry off the floor",
      [("Leave the pods on the ground in the rain", "Moisture allows mould growth."), ("Store them damp in closed plastic to keep them fresh", "Damp, closed storage promotes growth."), ("Feed the mouldy nuts to animals", "Animals can be harmed and the toxin can pass into milk and meat.")],
      [("Control", "Quick drying, sorting and dry storage are the key controls.")], T_AFL, "Application", "Which step removes water and bad nuts?"),
    Q("Ochratoxin A, fumonisins and patulin are all examples of", "Mycotoxins",
      [("Bacterial endotoxins", "These three are produced by moulds."), ("Heat-labile toxins", "Most are stable."), ("Vitamins", "They are toxic compounds, not vitamins.")],
      [("Mycotoxins", "Mould toxins include aflatoxins, ochratoxin A, fumonisins, patulin and zearalenone.")], T_AFL, "Concept", "Which organisms make these compounds?"),
]
SETS.append(practice_set(module=M_MIC, topic=T_AFL, title="Aflatoxin conditions, effects and control", lesson="fsl2-aflatoxins-mycotoxins", questions=build(X, 204)))

# ------------------------------------------------------------------ 5. Sensory evaluation methods
X = [
    Q("In a triangle test, a judge receives", "Three coded samples, two the same and one different",
      [("Two samples and must say which is better", "That is a paired comparison."), ("A reference and two samples", "That is a duo-trio test."), ("Five samples to rank", "That is a ranking test.")],
      [("Triangle test", "The judge picks the odd one out of three.")], T_SEN, "Recall", "The name tells you the number of samples."),
    Q("What is the chance of choosing correctly by guessing in a duo-trio test?", "1 in 2",
      [("1 in 3", "That is the chance for a triangle test."), ("1 in 6", "6 is the number of possible serving orders in a triangle test, not a chance."), ("1 in 4", "There are only two samples to choose between.")],
      [("Chance", "The judge chooses between two coded samples.")], T_SEN, "Recall", "How many samples does the judge choose between?"),
    Q("Why are samples labelled with random three-digit codes?", "So that names, brands or position do not bias the judges",
      [("To make the samples last longer", "Codes do not affect keeping quality."), ("To show the cook who made them", "Codes hide the identity."), ("To save space on the label", "The reason is to control bias.")],
      [("Control", "Coded samples remove prejudice about names.")], T_SEN, "Concept", "Think of a famous brand."),
    Q("A company wants to know which of two biscuits consumers like better. The best test is", "A hedonic test with a consumer panel",
      [("A triangle test with a trained panel", "That tests whether the biscuits can be told apart, not which is liked."), ("Kjeldahl analysis", "That measures protein."), ("Soxhlet extraction", "That measures fat.")],
      [("Choosing a test", "Liking is measured by a hedonic or preference test on a consumer panel.")], T_SEN, "Application", "Is the question about difference or liking?"),
    Q("In a triangle test with 12 judges, 8 pick the odd sample correctly. The minimum for significance at the 5 percent level is 8 (one-sided). What is the conclusion?", "A difference between the samples is detected",
      [("There is no way to decide", "The table gives the decision rule."), ("The samples are the same", "More than the minimum identified the odd sample, so a difference is shown."), ("The test must be repeated with 9 judges", "The number of judges is already enough to use the table.")],
      [("Using the table", "8 meets the minimum of 8, so the result is significant at 5 percent.")], T_SEN, "Interpretation", "Compare 8 with the minimum from the table."),
    N("In a triangle test 12 judges are used. How many correct answers are expected by chance alone?", 4,
      [("Chance", "The chance for each judge is 1/3."), ("Expected number", "12 × 1/3 = 4.")], T_SEN, "Calculation", "Multiply the number of judges by the chance for each.", tol=0.01, unit="judges"),
    N("Ten consumers score a biscuit on the 9-point hedonic scale: 7, 8, 6, 9, 7, 8, 7, 6, 8, 7. Find the mean score.", 7.3,
      [("Total", "7+8+6+9+7+8+7+6+8+7 = 73."), ("Mean", "73 ÷ 10 = 7.3.")], T_SEN, "Calculation", "Add the scores and divide by the number of judges.", tol=0.05, unit="points"),
    Q("Five judges rank three samples for crispness (1 = crispest). The rank totals are A = 7, B = 14 and C = 9. Which statement is correct?", "A was ranked crispest overall",
      [("B was ranked crispest overall", "B has the highest total, so it was the least crisp."), ("C was ranked crispest overall", "C is in the middle."), ("The totals show an error because they are not equal", "Totals need not be equal; they must add to 30 for 5 judges.")],
      [("Rank totals", "The lowest total means the best overall rank.")], T_SEN, "Interpretation", "With 1 as the best rank, which total is smallest?"),
]
SETS.append(practice_set(module=M_SEN, topic=T_SEN, title="Difference, ranking and hedonic tests", lesson="fsl2-sensory-evaluation-methods", questions=build(X, 205)))

# ------------------------------------------------------------------ 6. Proximate analysis
X = [
    Q("Which method is used to measure the crude protein in a food?", "The Kjeldahl method",
      [("Soxhlet extraction", "That measures fat."), ("Oven drying", "That measures moisture."), ("Ashing at 550 degrees C", "That measures minerals.")],
      [("Kjeldahl", "It measures total nitrogen, which is converted to protein.")], T_PRO, "Recall", "Which method measures nitrogen?"),
    Q("What is the role of boric acid in the Kjeldahl distillation?", "It traps the ammonia that is released",
      [("It digests the sample", "Concentrated sulphuric acid digests the sample."), ("It dissolves the fat", "Fat is dissolved by solvent in Soxhlet extraction."), ("It is the indicator at the end point", "The receiving boric acid holds the ammonia; an indicator is added separately to show the end point.")],
      [("Distillation", "The ammonia is carried over and trapped in boric acid as borate, which is then titrated.")], T_PRO, "Concept", "What happens to the ammonia?"),
    N("A 1.000 g sample needs 12.40 cm³ of 0.100 M HCl and the blank needs 0.40 cm³. Calculate the percentage nitrogen (A(N) = 14.007). Give your answer to two decimal places.", 1.68,
      [("Corrected titre", "12.40 − 0.40 = 12.00 cm³."), ("Moles of N", "12.00 × 0.100 ÷ 1000 = 1.200 × 10^-3 mol."), ("Mass of N and percentage", "1.200 × 10^-3 × 14.007 = 0.01681 g; ÷ 1.000 × 100 = 1.68 percent.")], T_PRO, "Calculation", "Subtract the blank, then find moles of nitrogen.", tol=0.01, unit="%"),
    N("A food contains 2.0 percent nitrogen. Calculate the crude protein content using the factor 6.25.", 12.5,
      [("Factor", "6.25 = 100 ÷ 16, since protein is about 16 percent nitrogen."), ("Protein", "2.0 × 6.25 = 12.5 percent.")], T_PRO, "Calculation", "Multiply nitrogen percentage by the factor.", tol=0.05, unit="%"),
    Q("Why is the protein value from the Kjeldahl method called 'crude' protein?", "It measures all nitrogen, including non-protein nitrogen, and uses an average factor",
      [("It is measured on unwashed samples", "Washing is not the issue."), ("It is accurate only for plants", "The method is used on all foods."), ("It is calculated by difference", "That is how carbohydrate is found, not protein.")],
      [("Crude protein", "Urea, free amino acids and other nitrogen compounds are counted, and the 6.25 factor is an average.")], T_PRO, "Concept", "What does Kjeldahl measure directly?"),
    N("A 2.500 g sample gives a fat mass of 0.4400 g after Soxhlet extraction. What is the percentage of fat?", 17.6,
      [("Percentage", "0.4400 ÷ 2.500 × 100 = 17.6 percent.")], T_PRO, "Calculation", "Divide the mass of fat by the mass of sample.", tol=0.05, unit="%"),
    Q("A food contains moisture 10.0, ash 2.0, protein 12.0, fat 3.0 and fibre 3.0 percent. What is the carbohydrate by difference?", "70.0 percent",
      [("30.0 percent", "30.0 is the sum of the other five components, not the carbohydrate."), ("100.0 percent", "100 is the total; the others must be subtracted."), ("40.0 percent", "This does not follow from the data.")],
      [("By difference", "100 − (10 + 2 + 12 + 3 + 3) = 70 percent.")], T_PRO, "Calculation", "Subtract the sum of the other components from 100."),
    Q("Which solvent set-up is correct for Soxhlet extraction of fat?", "Heat a non-polar solvent such as petroleum ether in a flask using a water bath or mantle, not a naked flame",
      [("Boil water in the flask and extract with steam", "Fat is not soluble in water; a solvent is needed."), ("Heat concentrated sulphuric acid with the sample", "That is the digestion step of Kjeldahl."), ("Burn the sample at 550 degrees C", "That is the ash determination.")],
      [("Soxhlet", "The solvent is flammable, so heat safely and work in a ventilated place.")], T_PRO, "Application", "Which solvent dissolves fat, and how do you heat it safely?"),
]
SETS.append(practice_set(module=M_SEN, topic=T_PRO, title="Kjeldahl, Soxhlet and the proximate scheme", lesson="fsl2-proximate-analysis", questions=build(X, 206)))

# ------------------------------------------------------------------ 7. Titratable acidity and moisture determination
X = [
    Q("Titratable acidity is usually measured by titrating the food with", "Standard sodium hydroxide, to the end point of phenolphthalein (about pH 8.2)",
      [("Standard hydrochloric acid", "Acid would not neutralise the acids in the food."), ("Iodine solution", "Iodine is used in the starch test."), ("Benedict's solution", "That is used for reducing sugars.")],
      [("Method", "A standard alkali neutralises all the acid; the pink colour marks the end point.")], T_TIT, "Recall", "Food acids need an alkali."),
    Q("Two fruit juices have the same pH, but one needs much more alkali to neutralise. What does this show?", "It has a higher titratable acidity because it holds more total acid",
      [("It has a lower total acid", "More alkali means more acid present."), ("It has no weak acids", "Weak acids are exactly what the titration finds."), ("pH and titratable acidity are the same thing", "They measure different things.")],
      [("TA and pH", "pH counts free H+; TA counts all the neutralisable acid.")], T_TIT, "Reasoning", "Which measurement shows the total amount of acid?"),
    N("25.0 cm³ of orange juice needs 14.2 cm³ of 0.100 M NaOH. Express the acidity as g citric acid per 100 cm³ (equivalent mass 64.04). Give your answer to two decimal places.", 0.36,
      [("Moles", "14.2 × 0.100 ÷ 1000 = 1.42 × 10^-3 mol."), ("Mass of acid", "1.42 × 10^-3 × 64.04 = 0.0909 g."), ("Per 100 cm³", "0.0909 ÷ 25.0 × 100 = 0.364, which is 0.36 g per 100 cm³.")], T_TIT, "Calculation", "Moles of NaOH equal moles of acidic hydrogen.", tol=0.01, unit="g per 100 cm³"),
    N("10.0 cm³ of milk needs 1.60 cm³ of 0.100 M NaOH. Express the acidity as lactic acid (equivalent mass 90.08) in percent. Give your answer to two decimal places.", 0.14,
      [("Mass of acid", "1.60 × 0.100 ÷ 1000 × 90.08 = 0.01441 g."), ("Percent", "0.01441 ÷ 10.0 × 100 = 0.144, about 0.14 percent.")], T_TIT, "Calculation", "Use the equivalent mass of lactic acid.", tol=0.01, unit="%"),
    N("A 5.00 g sample of grain weighs 3.80 g after drying to constant mass. What is the moisture content (wet basis)?", 24,
      [("Mass lost", "5.00 − 3.80 = 1.20 g."), ("Moisture", "1.20 ÷ 5.00 × 100 = 24.0 percent.")], T_TIT, "Calculation", "Divide the mass lost by the starting mass.", tol=0.1, unit="%"),
    Q("Why must a dried sample be cooled in a desiccator before weighing?", "It would take up moisture from the air and the result would be wrong",
      [("The balance cannot weigh hot objects, but the sample has no other change", "Hot air currents matter, but the main reason is moisture uptake."), ("Cooling removes the ash", "Cooling does not affect ash."), ("Cooling makes the sample heavier because it is dense", "Mass does not increase on cooling except by absorbing moisture.")],
      [("Desiccator", "A dried food is hygroscopic and gains water from humid air.")], T_TIT, "Application", "What does a dry food do in humid air?"),
    Q("The Karl Fischer titration is preferred to oven drying for chocolate powder because", "It reacts only with water and does not need heating that can drive off other volatile substances",
      [("It measures protein", "KF measures water only."), ("It is faster than weighing", "Speed is not the main reason."), ("It needs no reagents", "It needs the KF reagent.")],
      [("Karl Fischer", "KF is specific to water and suits dry or heat-sensitive foods.")], T_TIT, "Concept", "What is the problem with heating chocolate powder?"),
    N("25.0 mg of water takes 5.00 cm³ of Karl Fischer reagent. A 500 mg sample takes 3.20 cm³. What is the water content of the sample in percent?", 3.2,
      [("Factor", "F = 25.0 ÷ 5.00 = 5.00 mg per cm³."), ("Water in the sample", "3.20 × 5.00 = 16.0 mg."), ("Percentage", "16.0 ÷ 500 × 100 = 3.2 percent.")], T_TIT, "Calculation", "Find the mg of water per cm³ of reagent first.", tol=0.05, unit="%"),
]
SETS.append(practice_set(module=M_SEN, topic=T_TIT, title="Titratable acidity, drying and Karl Fischer", lesson="fsl2-titratable-acidity-moisture", questions=build(X, 207)))

# ------------------------------------------------------------------ 8. Examination: Paper 1
X = [
    Q("How many multiple-choice questions are in Paper 1, according to the Board's 2023 report?", "50",
      [("25", "Paper 1 has 50 questions, not 25."), ("100", "100 is the total marks of the Paper 2 essay paper in the report."), ("40", "The report gives 50 questions.")],
      [("Paper 1", "The paper has 50 multiple-choice questions and carries 35 percent.")], T_P1, "Recall", "State the number given in the report."),
    N("A paper has 50 questions in 90 minutes. What is the average time per question in minutes?", 1.8,
      [("Divide", "90 ÷ 50 = 1.8 minutes.")], T_P1, "Calculation", "Divide the time by the number of questions.", tol=0.01, unit="minutes"),
    Q("A stem says 'Which of the following is NOT a cause of rancidity?' What is the best first step?", "Underline NOT and find the three true causes, so that the option left over is the answer",
      [("Choose the first true statement", "With NOT, the true statements are the wrong answers."), ("Ignore the word NOT", "Missing a negative is a common cause of errors."), ("Choose the longest option", "Length is not a guide.")],
      [("Negatives", "Mark the negative and reverse your search.")], T_P1, "Application", "What does NOT change about what you look for?"),
    Q("A student finds 12.0 percent nitrogen in a sample and chooses 12.0 percent as the protein. Which type of distractor was chosen?", "An unfinished calculation",
      [("An absolute word", "There is no 'always' or 'never' here."), ("A reversed answer", "The direction was not reversed."), ("A true statement for the wrong question", "The number is not true for any other question here.")],
      [("Distractors", "The nitrogen value must be multiplied by 6.25 to give protein.")], T_P1, "Reasoning", "Which step was missing?"),
    Q("Two options are almost the same. What should you do?", "Compare them word by word to find the one detail that makes one false",
      [("Choose the one that sounds more scientific", "That is not reliable."), ("Choose the shorter one", "Length is not a guide."), ("Leave it blank", "A blank earns nothing.")],
      [("Close options", "The small difference often is the fact being tested.")], T_P1, "Application", "Where is the difference between them?"),
    Q("Which pair of terms describes two DIFFERENT food poisoning mechanisms that candidates often confuse?", "Infection and intoxication",
      [("Moisture and water content", "These mean the same thing in food analysis."), ("Kjeldahl method and nitrogen determination", "These are the same method described in two ways."), ("Sensory and organoleptic evaluation", "These are two names for the same thing.")],
      [("Confusable pairs", "Infection versus intoxication is a pair that candidates mix up.")], T_P1, "Recall", "Which pair describes two different disease mechanisms?"),
    N("A food has 20 g protein, 10 g fat and 50 g carbohydrate per 100 g. Using 17, 37 and 17 kJ per gram, find the energy per 100 g in kJ.", 1560,
      [("Protein", "20 × 17 = 340."), ("Fat", "10 × 37 = 370."), ("Carbohydrate and total", "50 × 17 = 850; 340 + 370 + 850 = 1560 kJ.")], T_P1, "Calculation", "Multiply each nutrient mass by its factor and add.", tol=1, unit="kJ"),
    Q("What should you do if you cannot answer a question in about two minutes?", "Choose your best guess, mark it and return if time allows",
      [("Spend ten minutes until you find the answer", "One question can cost the time of several easy ones."), ("Stop answering the paper", "Other questions earn marks."), ("Change all your other answers", "That is not sensible.")],
      [("Time", "A paper of 50 questions needs about 1.8 minutes per question on average.")], T_P1, "Application", "Think of the marks that remain."),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Multiple-choice technique and calculations", lesson="fsl2-paper1-multiple-choice", questions=build(X, 208)))

# ------------------------------------------------------------------ 9. Examination: Paper 2
X = [
    Q("What does the command word 'differentiate' ask for?", "The differences between two or more things",
      [("A list of examples only", "That is 'list' or 'give examples'."), ("A step-by-step process", "That is 'describe'."), ("A calculation", "No calculation is required.")],
      [("Command word", "Differentiate means state how they differ, point by point.")], T_P2, "Recall", "Think of the word 'difference'."),
    Q("According to the Board's 2023 report, how many marks was each question of Paper 2 scored out of?", "25",
      [("10", "The report shows scores out of 25."), ("50", "50 is not the score for one question."), ("100", "100 is the total marks the report gives for the paper.")],
      [("Paper 2", "The highest and lowest scores in the report are given out of 25.")], T_P2, "Recall", "The highest score for a question was given as ?/25."),
    Q("Which answer correctly defines a food taboo?", "A food that a group forbids or avoids for cultural, social or religious reasons",
      [("A short-lived enthusiasm for a food or diet", "That is a food fad."), ("A false belief about the health effect of a food", "That is a food fallacy."), ("A food that is unsafe because of bacteria", "That is a food safety hazard, not a taboo.")],
      [("Food habits", "Fad, taboo and fallacy are different ideas that candidates mixed up.")], T_P2, "Concept", "Taboo means forbidden."),
    Q("Which weakness in answers on fats and oils does the Board's 2023 report record for Paper 2?", "Candidates did not define rancidity or propose prevention, and mixed up the margarine and cheese flow diagrams",
      [("Candidates calculated iodine values wrongly", "The report does not mention iodine values."), ("Candidates confused hydrogenation with fermentation", "The report does not give this confusion."), ("Nobody attempted the question", "The report says it was the least popular, not that nobody attempted it.")],
      [("Report", "The report notes weak definitions and prevention of rancidity and a mix-up of flow diagrams.")], T_P2, "Recall", "Think of the question on Section C."),
    Q("A 25-mark question has four parts. How should you share your time?", "Give each part time in line with its marks and attempt all parts",
      [("Answer only part (a) in detail", "Missing parts gives no marks."), ("Write the same length for every part", "Marks are not equal across parts."), ("Spend the whole time on the part you find hardest", "That is risky and gives up easy marks.")],
      [("Time", "Allocate time by marks and try every part.")], T_P2, "Application", "How are marks shared across parts?"),
    Q("The rubric says to answer ONE question from each section. A candidate answers two from Section B and none from Section D. What is the likely result?", "Marks are lost, because the instruction was not followed",
      [("Full marks, since the extra answer is a bonus", "Rubric rules are applied by examiners."), ("The Section D marks are given automatically", "No answer, no marks."), ("There is no effect", "The report warns candidates about this.")],
      [("Rubric", "The report advises strict adherence to instructions.")], T_P2, "Reasoning", "What did the report say about answering two from one section?"),
    Q("Which sequence best answers 'Explain how insulin and glucagon regulate blood glucose'?", "Rise in glucose: insulin makes cells take up glucose and store it as glycogen; fall: glucagon makes the liver release glucose",
      [("Insulin raises blood glucose and glucagon lowers it", "This reverses the roles."), ("Both hormones are made in the liver and raise glucose", "Both are made in the pancreas, and insulin lowers glucose."), ("They affect only the heart", "They regulate blood glucose through liver, muscle and fat cells.")],
      [("Hormones", "Insulin lowers blood glucose; glucagon raises it; both come from the pancreas.")], T_P2, "Application", "Which hormone lowers glucose?"),
    Q("Which opening best answers 'Define rancidity'?", "The development of unpleasant tastes and smells in fats and oils, mainly through oxidation or hydrolysis",
      [("The hardening of oils by adding hydrogen", "That is hydrogenation."), ("The browning of cut fruit", "That is enzymatic browning."), ("The setting of egg protein", "That is coagulation.")],
      [("Definition", "Rancidity is the spoilage of fat by oxidation or hydrolysis.")], T_P2, "Recall", "Which process spoils fats?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Command words, sections and planning", lesson="fsl2-paper2-essay", questions=build(X, 209)))

# ------------------------------------------------------------------ 10. Examination: Paper 3
X = [
    Q("According to the Board's 2023 report, Paper 3 has two parts. They are", "Food tests and cookery",
      [("Titration and microscopy", "These are not the parts named in the report."), ("Sensory evaluation and diet surveys", "The report names food tests and cookery."), ("Essays and multiple choice", "Those are Papers 2 and 1.")],
      [("Paper 3", "Part 1 is food tests and Part 2 is cookery.")], T_P3, "Recall", "Recall the title of each part."),
    Q("A sample stays blue when heated with Benedict's solution. The correct report is", "The colour stayed blue: reducing sugar absent (a negative result)",
      [("No result, so nothing is written", "The report says that negative results must be reported."), ("Reducing sugar present in a large amount", "A large amount gives brick red."), ("Starch present", "Starch is tested with iodine.")],
      [("Negative result", "Write the observation and the conclusion.")], T_P3, "Application", "What does no colour change mean?"),
    Q("Which result with iodine solution shows starch?", "Blue-black colour",
      [("Brick-red precipitate", "That is a strong positive with Benedict's solution."), ("Violet colour", "That is the biuret test for protein."), ("Cloudy white emulsion", "That is the ethanol test for fat.")],
      [("Iodine test", "Starch gives a blue-black complex with iodine.")], T_P3, "Recall", "Which colour shows starch?"),
    Q("What is the result of the biuret test on a protein-rich food?", "Blue changes to violet or purple",
      [("Orange-red precipitate", "That is a Benedict's result for a reducing sugar."), ("Blue-black", "That is the iodine test for starch."), ("The DCPIP is decolourised", "That is the test for vitamin C.")],
      [("Biuret", "Peptide bonds form a violet complex with copper in alkali.")], T_P3, "Recall", "Which test uses sodium hydroxide and copper sulphate?"),
    Q("To test for a non-reducing sugar such as sucrose you should", "Boil with dilute hydrochloric acid, neutralise, and then test with Benedict's solution",
      [("Add iodine solution", "Iodine tests for starch."), ("Add ethanol and water", "That is the fat test."), ("Add Benedict's solution at once and expect brick red", "Sucrose does not react until it has been hydrolysed.")],
      [("Hydrolysis", "Acid splits sucrose into reducing sugars; then Benedict's is positive.")], T_P3, "Concept", "The sugar must be hydrolysed first."),
    N("A meal contains 150 g of cooked rice. The practice FCT gives 2.7 g protein per 100 g of cooked rice (a value invented for practice). How many g of protein are in 150 g?", 4.05,
      [("Scale", "150 × 2.7 ÷ 100 = 4.05 g.")], T_P3, "Calculation", "Multiply the value per 100 g by the mass ÷ 100.", tol=0.01, unit="g"),
    N("A recipe uses 200 g of a vegetable with 20 percent waste. The practice FCT gives 3.0 g protein per 100 g edible portion. How many g of protein are in the recipe?", 4.8,
      [("Edible mass", "200 × 0.80 = 160 g."), ("Protein", "160 × 3.0 ÷ 100 = 4.8 g.")], T_P3, "Calculation", "Remove the waste before scaling.", tol=0.01, unit="g"),
    Q("Which statement about the cookery part is supported by the Board's report?", "Teachers should explain the science involved in the cookery practical",
      [("Candidates need not plan", "Planning is part of the task."), ("Any food composition table may be used", "The report says to use only the FCT supplied by the Board."), ("Practical sessions are optional", "The report advises students to attend all practical sessions.")],
      [("Report", "The report recommends that teachers teach the science of cookery.")], T_P3, "Recall", "Think of the advice to teachers."),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Food tests, calculations and cookery planning", lesson="fsl2-paper3-practical-skills", questions=build(X, 210)))

# ------------------------------------------------------------------ Paper 1 mock exam A (50 MC; 12/12/9/10/7 by module)
P1 = [
    # ---- Food Chemistry of Macronutrients (12): water activity 3, carbohydrates 3, lipids 2, proteins 2, Maillard 2
    Q("The water activity of a food is defined as", "The vapour pressure of water in the food divided by that of pure water at the same temperature",
      [("The percentage of water in the food", "That is the moisture content, not the water activity."), ("The mass of water in 100 g of the food", "That is a moisture measure."), ("The boiling point of the food", "Boiling point is not water activity.")],
      [("Definition", "a_w = p / p0, a ratio between 0 and 1.")], T_WAT, "Recall", "Is it a percentage or a ratio of vapour pressures?"),
    Q("A food in equilibrium with air of 75 percent relative humidity has a water activity of", "0.75",
      [("75", "Water activity is on a scale 0 to 1, not 0 to 100."), ("0.25", "This takes 1 minus the humidity."), ("7.5", "This is a power-of-ten error.")],
      [("ERH", "a_w equals the equilibrium relative humidity divided by 100.")], T_WAT, "Calculation", "Divide the percentage by 100."),
    Q("Adding salt or sugar to a food preserves it mainly because it", "Lowers the water activity so that microbes cannot use the water",
      [("Raises the pH", "Salt and sugar do not mainly act by raising pH."), ("Kills all bacteria at once", "They slow or stop growth; they do not sterilise."), ("Adds oxygen", "Oxygen is not added.")],
      [("Preservation", "Dissolved solutes bind water and lower a_w.")], T_WAT, "Application", "What happens to available water?"),
    Q("Heating a starch suspension in water until the granules swell and the mixture thickens is called", "Gelatinisation",
      [("Retrogradation", "Retrogradation is the re-association of starch chains on cooling and ageing."), ("Dextrinisation", "Dextrinisation is the breakdown of starch by dry heat."), ("Caramelisation", "Caramelisation is the browning of sugars.")],
      [("Gelatinisation", "Granules take up water, swell and thicken the sauce.")], T_CHO, "Recall", "Which term describes swelling of granules in hot water?"),
    Q("The staling of bread on storage is mainly due to", "Retrogradation of starch",
      [("Gelatinisation of starch", "That happens during baking."), ("Caramelisation of sucrose", "That needs high dry heat and gives colour, not staling."), ("Pectin gel formation", "Pectin gels are in jams, not in bread.")],
      [("Retrogradation", "Starch chains re-associate and crystallise, making the crumb firm.")], T_CHO, "Application", "Think of what happens to cooked starch on cooling."),
    Q("Which set of conditions is needed for a good pectin gel in jam?", "Pectin, sufficient sugar and an acid pH",
      [("Pectin, salt and an alkaline pH", "Alkali weakens pectin gels and salt is not the second need."), ("Starch, fat and a neutral pH", "These are not the requirements for pectin gels."), ("Protein, water and cooling only", "Protein gels are a different system.")],
      [("Pectin gel", "Sugar competes for water and acid reduces the charge on pectin, so chains join.")], T_CHO, "Concept", "Think about the ingredients of jam."),
    Q("Autoxidation of unsaturated fatty acids in oils produces", "Hydroperoxides that break down to give rancid flavours",
      [("Glycerol and soap only", "This is hydrolysis in alkaline conditions, not autoxidation."), ("A harder fat with no flavour change", "Hydrogenation, not oxidation, hardens fat."), ("Starch", "Starch is not a product of fat oxidation.")],
      [("Rancidity", "Free-radical oxidation gives hydroperoxides and then aldehydes and ketones.")], T_LIP, "Concept", "Which process gives off-flavours in fats?"),
    Q("Hydrogenation of vegetable oil is carried out to", "Make a liquid oil more solid and more stable by adding hydrogen to double bonds",
      [("Remove all water from the oil", "Hydrogenation is not drying."), ("Increase the number of double bonds", "It removes double bonds."), ("Make the oil more soluble in water", "Oil stays non-polar.")],
      [("Hydrogenation", "Hydrogen is added to the double bonds with a nickel catalyst, raising the melting point.")], T_LIP, "Recall", "Hydrogen is added to what?"),
    Q("Denaturation of an egg white protein on heating involves", "Unfolding of the protein structure without breaking the peptide bonds",
      [("Breaking of peptide bonds into amino acids", "That is hydrolysis, not denaturation."), ("Formation of new peptide bonds", "Peptide bonds are not formed by heating."), ("Loss of all nitrogen", "Nitrogen is not lost.")],
      [("Denaturation", "Weak bonds break and the chain unfolds; the primary structure is unchanged.")], T_PROT, "Concept", "Which bonds are broken?"),
    Q("A protein has its lowest solubility at its", "Isoelectric point",
      [("Highest temperature", "Temperature affects denaturation, not the isoelectric solubility effect."), ("Highest pH", "Alkaline pH raises solubility of most food proteins."), ("Boiling point", "Boiling is unrelated to the isoelectric point.")],
      [("Isoelectric point", "At the pI the net charge is zero, so molecules aggregate and precipitate (for example casein in yoghurt).")], T_PROT, "Concept", "At which pH is the net charge zero?"),
    Q("Maillard browning is a reaction between", "A reducing sugar and an amino group",
      [("Phenols and oxygen with an enzyme", "That is enzymatic browning."), ("A sugar heated alone", "That is caramelisation."), ("Two amino acids only", "A reducing sugar is also needed.")],
      [("Maillard", "Reducing sugars react with amino groups on heating, giving brown pigments and flavour.")], T_MAI, "Recall", "It needs both a sugar and an amine."),
    Q("Which nutritional loss is associated with the Maillard reaction?", "Loss of available lysine",
      [("Gain of vitamin C", "Maillard does not raise vitamin C."), ("Loss of all minerals", "Minerals are not lost by the reaction."), ("Gain of omega-3 fatty acids", "Fatty acids are not formed.")],
      [("Lysine", "The free amino group of lysine reacts with sugars and becomes unavailable.")], T_MAI, "Application", "Which essential amino acid has a free side-chain amino group?"),

    # ---- Micronutrients, Pigments, Enzymes & Dispersions (12): vitamins 3, minerals 3, pigments 2, enzymatic browning 2, colloids 2
    Q("Which vitamin is most easily lost when vegetables are boiled in a large volume of water?", "Vitamin C",
      [("Vitamin A", "It is fat soluble and fairly stable in water."), ("Vitamin D", "It is fat soluble and stable to boiling."), ("Vitamin K", "It is fat soluble and stable to boiling.")],
      [("Vitamin C", "It is water soluble and sensitive to heat and oxidation.")], T_VIT, "Recall", "Which vitamin is water soluble and heat labile?"),
    Q("Blanching vegetables before freezing helps to", "Inactivate enzymes that would cause loss of colour, flavour and vitamins",
      [("Increase the water activity", "Blanching does not raise a_w for that purpose."), ("Sterilise the food completely", "Blanching is a mild heat treatment."), ("Add fat-soluble vitamins", "It does not add vitamins.")],
      [("Blanching", "A short heat treatment inactivates enzymes such as peroxidase.")], T_VIT, "Application", "Think of what enzymes still do in frozen vegetables."),
    Q("Adding bicarbonate of soda (an alkali) to cooking vegetables to keep them green causes a loss of", "Thiamin (vitamin B1) and a softer texture",
      [("Vitamin A only", "Thiamin is the vitamin affected by alkali."), ("All the minerals", "Minerals are not destroyed."), ("Fat", "Vegetables contain little fat and it is not destroyed.")],
      [("Alkali", "Thiamin is unstable in alkali; the pectin is also weakened.")], T_VIT, "Concept", "Which B vitamin is unstable in alkaline conditions?"),
    Q("Which compound in cereals and legumes binds iron, zinc and calcium and lowers their absorption?", "Phytate",
      [("Lactose", "Lactose can help calcium absorption."), ("Vitamin C", "It increases the absorption of non-haem iron."), ("Starch", "Starch is a carbohydrate, not a mineral binder.")],
      [("Phytate", "Phytic acid forms insoluble complexes with minerals.")], T_MIN, "Recall", "Which anti-nutrient is found in whole grains?"),
    Q("Which treatment reduces the phytate content of cereals and beans?", "Soaking, germination or fermentation",
      [("Freezing", "Freezing does not reduce phytate."), ("Adding more salt", "Salt does not reduce phytate."), ("Drying in the sun", "Drying does not reduce phytate by itself.")],
      [("Processing", "Phytase enzymes become active during soaking, germination and fermentation.")], T_MIN, "Application", "Which processes activate phytase?"),
    Q("Oxalate in spinach reduces the availability of", "Calcium",
      [("Vitamin C", "Oxalate does not bind vitamin C."), ("Iodine", "Oxalate does not mainly bind iodine."), ("Protein", "Oxalate is a mineral binder, not a protein binder.")],
      [("Oxalate", "Calcium oxalate is insoluble and is not absorbed.")], T_MIN, "Concept", "Which mineral forms an insoluble salt with oxalate?"),
    Q("When green vegetables are boiled with acid (for example vinegar), chlorophyll changes to", "Olive-brown pheophytin",
      [("Bright green chlorophyllin", "Alkali, not acid, gives chlorophyllin."), ("Red anthocyanin", "Anthocyanins are separate pigments."), ("Orange carotene", "Carotene is already present and not formed from chlorophyll.")],
      [("Chlorophyll", "Acid replaces the magnesium and gives pheophytin, which is olive brown.")], T_PIG, "Concept", "What does acid do to the magnesium in chlorophyll?"),
    Q("Which pigment is orange, fat soluble and a precursor of vitamin A?", "Beta-carotene",
      [("Anthocyanin", "It is a water-soluble pigment that is not a vitamin A precursor."), ("Chlorophyll", "It is green and not a vitamin A precursor."), ("Myoglobin", "It is the red pigment of muscle.")],
      [("Carotenoids", "Beta-carotene is converted to retinol in the body.")], T_PIG, "Recall", "Which pigment is in carrots?"),
    Q("Cut apple slices turn brown in air because", "Polyphenol oxidase oxidises phenols in the presence of oxygen",
      [("The Maillard reaction occurs at room temperature", "Maillard needs sugars and amines and usually heat."), ("Starch is retrograded", "Retrogradation is about starch ageing."), ("Pectin gels", "Gelling does not cause browning.")],
      [("Enzymatic browning", "The enzyme needs a phenolic substrate and oxygen.")], T_ENZ, "Concept", "Which enzyme is involved?"),
    Q("Which treatment best prevents enzymatic browning of cut fruit?", "Dipping in lemon juice",
      [("Leaving it in warm air", "Warm air with oxygen speeds browning."), ("Adding a pinch of copper sulphate", "Copper is a cofactor of the enzyme and promotes browning."), ("Adding more oxygen", "Oxygen is a requirement for browning.")],
      [("Prevention", "Acid and ascorbic acid lower the pH and act as antioxidants.")], T_ENZ, "Application", "Which treatment lowers pH and gives an antioxidant?"),
    Q("Milk is an example of which colloidal system?", "An oil-in-water emulsion",
      [("A water-in-oil emulsion", "Butter and margarine are water-in-oil."), ("A gas-in-liquid foam", "Whipped cream is a foam."), ("A solid sol", "Milk is not a solid dispersion.")],
      [("Emulsion", "Fat globules are dispersed in water with protein stabilisers.")], T_COL, "Recall", "Which phase is continuous in milk?"),
    Q("An emulsifier such as lecithin works because its molecules", "Have a water-loving end and an oil-loving end and sit at the oil-water boundary",
      [("Are very small and dissolve in oil only", "An emulsifier needs both ends."), ("React with water to make gas", "That describes a raising agent."), ("Remove the oil from the mixture", "It keeps oil dispersed; it does not remove it.")],
      [("Emulsifier", "Amphiphilic molecules lower interfacial tension and stop droplets joining.")], T_COL, "Concept", "Why does it need two kinds of ends?"),

    # ---- Human Physiology, Metabolism & Energy Balance (9): digestion 3, metabolic pathways 2, BMR 2, energy requirement 2
    Q("Where does most chemical digestion and absorption of nutrients take place?", "The small intestine",
      [("The stomach", "The stomach starts protein digestion but absorbs little."), ("The large intestine", "The colon mainly absorbs water and salts."), ("The mouth", "Only starch digestion begins there.")],
      [("Small intestine", "Enzymes from the pancreas and the intestinal wall act there and villi give a large surface.")], T_DIG, "Recall", "Where are the villi?"),
    Q("Bile helps the digestion of fats by", "Emulsifying the fat into small droplets, giving a larger surface for lipase",
      [("Digesting fat to fatty acids", "Lipase digests the fat; bile is not an enzyme."), ("Acting as a protease", "Bile contains no protease."), ("Absorbing the fat", "Absorption is by the cells of the villi.")],
      [("Bile", "Bile salts emulsify fat; they do not digest it.")], T_DIG, "Concept", "Is bile an enzyme?"),
    Q("Glucose is absorbed across the intestinal wall mainly by", "Active transport linked to sodium (co-transport)",
      [("Simple osmosis", "Osmosis is the movement of water."), ("Phagocytosis", "That is the engulfing of particles."), ("Passive diffusion only", "Absorption of glucose against a gradient needs active transport.")],
      [("Absorption", "Sodium-glucose co-transporters use the sodium gradient set by the sodium pump.")], T_DIG, "Concept", "Which process needs energy and carriers?"),
    Q("Glycolysis takes place in the", "Cytoplasm, and gives a net gain of 2 ATP per glucose",
      [("Mitochondrial matrix, with a net gain of 38 ATP", "The mitochondria are the site of the Krebs cycle."), ("Nucleus, with no ATP gain", "Glycolysis is not in the nucleus."), ("Ribosomes, with a net gain of 4 ATP", "Four ATP are made but two are used, so the net is 2, and ribosomes are not the site.")],
      [("Glycolysis", "Glucose is split to two pyruvate in the cytoplasm; net 2 ATP and 2 NADH.")], T_MET, "Recall", "Is oxygen needed for glycolysis?"),
    Q("Deamination of amino acids in the liver produces", "Ammonia (converted to urea) and a keto acid",
      [("Glucose and glycogen only", "Glucose may be made from the keto acid, but the first products are ammonia and keto acid."), ("Fatty acids and glycerol", "These are products of lipid breakdown."), ("Lactic acid", "Lactic acid is a product of anaerobic glycolysis.")],
      [("Deamination", "The amino group is removed; the nitrogen is excreted as urea.")], T_MET, "Concept", "What happens to the amino group?"),
    Q("Which statement about the basal metabolic rate (BMR) is correct?", "It is the energy used at rest to maintain basic body functions and is the largest part of daily energy expenditure for most people",
      [("It is the energy used for digesting a meal", "That is the thermic effect of food."), ("It is the energy used in physical activity", "That is the activity component."), ("It is the same for all people regardless of body size", "BMR depends on size, age, sex and lean mass.")],
      [("BMR", "BMR is measured at rest and typically accounts for more than half of daily energy use.")], T_BMR, "Concept", "Which part of expenditure is at rest?"),
    Q("About what fraction of the energy in a mixed meal is used in its digestion and metabolism (the thermic effect of food)?", "About 10 percent",
      [("About 50 percent", "That is far above the typical value."), ("About 1 percent", "That is below the typical value."), ("About 90 percent", "Nearly all energy is not used in digestion.")],
      [("TEF", "A usual teaching value is about 10 percent of the energy intake (check your textbook).")], T_BMR, "Recall", "It is a small part of the intake."),
    Q("A person has a BMR of 7000 kJ per day and a physical activity level (PAL) of 1.6. What is the estimated total daily energy requirement?", "11 200 kJ",
      [("17 920 kJ", "This applies the PAL twice."), ("4 375 kJ", "This divides by the PAL instead of multiplying."), ("7 000 kJ", "This is the BMR only.")],
      [("TEE", "TEE = BMR × PAL = 7000 × 1.6 = 11 200 kJ.")], T_ENR, "Calculation", "Multiply BMR by PAL."),
    Q("A food contains 10 g protein, 20 g fat and 60 g carbohydrate per 100 g. Using 17, 37 and 17 kJ per gram, its energy per 100 g is", "1930 kJ",
      [("1 530 kJ", "This uses 17 kJ per gram for fat instead of 37."), ("2 130 kJ", "This uses 37 kJ per gram for protein as well as for fat."), ("1 190 kJ", "This is the energy of protein and carbohydrate only, with the fat left out.")],
      [("Energy", "170 + 740 + 1020 = 1930 kJ.")], T_ENR, "Calculation", "Multiply each nutrient by its factor and add."),

    # ---- Food Microbiology & Food Safety (10): factors 3, fermentation 3, infections 2, aflatoxins 2
    Q("The usual shape of the bacterial growth curve shows, in order,", "Lag, log (exponential), stationary and death phases",
      [("Log, lag, death and stationary phases", "The log phase follows the lag phase and the stationary phase comes before death."), ("Stationary, lag, log and death phases", "The population cannot reach stationary before it grows."), ("Death, log, lag and stationary phases", "Death is the last phase in a closed culture.")],
      [("Growth curve", "Cells adjust, then multiply, then run out of nutrients, then die.")], T_FAC, "Recall", "Where does the population grow fastest?"),
    Q("A food starts with 2 000 bacterial cells and has 16 000 cells 90 minutes later. What is the generation time during growth?", "30 minutes",
      [("45 minutes", "This divides 90 by 2, not by the number of doublings."), ("15 minutes", "This is based on 6 generations."), ("90 minutes", "That is the whole period, not the time for one doubling.")],
      [("Calculation", "16 000/2 000 = 8 = 2^3, so 3 generations in 90 minutes: 30 min each.")], T_FAC, "Calculation", "How many doublings take a number to eight times its size?"),
    Q("The danger zone for the growth of most food poisoning bacteria is roughly", "5 to 60 degrees C",
      [("-18 to 0 degrees C", "That is the range of freezing."), ("70 to 100 degrees C", "That is the range of cooking."), ("0 to 5 degrees C", "This is the range of refrigerators, which slows growth.")],
      [("Danger zone", "Teaching values are about 5 to 60 degrees C (check your textbook).")], T_FAC, "Recall", "Between the fridge and hot holding."),
    Q("In lactic acid fermentation of glucose by a homofermentative bacterium, one mole of glucose gives", "Two moles of lactic acid",
      [("Two moles of ethanol and two of carbon dioxide", "This is alcoholic fermentation."), ("One mole of lactic acid", "Two molecules are formed per glucose."), ("Six moles of carbon dioxide", "This is complete aerobic respiration.")],
      [("Equation", "C6H12O6 gives 2 CH3CH(OH)COOH.")], T_FER, "Recall", "Count the carbon atoms."),
    Q("A yeast ferments 90 g of glucose (Mr 180) to ethanol (Mr 46) and carbon dioxide. The theoretical mass of ethanol is", "46 g",
      [("92 g", "This is the ethanol from 180 g of glucose."), ("23 g", "This forgets that each glucose gives two ethanol."), ("90 g", "This assumes ethanol equals the mass of glucose.")],
      [("Yield", "90/180 = 0.5 mol; 1.0 mol ethanol = 46 g.")], T_FER, "Calculation", "Each glucose gives two ethanol."),
    Q("Which fermented food is made by Lactobacillus bulgaricus and Streptococcus thermophilus acting on milk?", "Yoghurt",
      [("Bread", "Bread is raised by yeast."), ("Palm wine", "Palm wine is fermented by yeasts and bacteria in sap."), ("Soy sauce", "That uses moulds and other microbes.")],
      [("Yoghurt", "The two bacteria together convert lactose to lactic acid.")], T_FER, "Recall", "Which milk product is thick and sour?"),
    Q("Staphylococcus aureus food poisoning is usually described as", "An intoxication with a short onset, caused by a heat-stable enterotoxin",
      [("An infection with onset after several days", "Salmonella is slower; S. aureus acts in hours."), ("A mycotoxicosis", "That is caused by moulds."), ("A toxin destroyed by boiling for 10 minutes", "That describes the botulinum toxin.")],
      [("S. aureus", "The preformed toxin acts within 1 to 6 hours and survives boiling.")], T_INF, "Concept", "Think of the toxin and the onset."),
    Q("Which statement about Clostridium botulinum is correct?", "It is an anaerobic spore-former that can grow in low-acid canned foods with too little heat treatment",
      [("It needs oxygen and grows on bread", "It is an anaerobe."), ("Its toxin is stable to boiling but the spores are not", "The spores are the heat-resistant stage; the toxin is labile."), ("It is a mould", "It is a bacterium.")],
      [("C. botulinum", "Spores survive weak heating; in the sealed can they germinate and make toxin.")], T_INF, "Concept", "Spores and low-oxygen cans."),
    Q("Aflatoxins are produced by", "Aspergillus flavus growing on stored groundnuts and maize",
      [("Salmonella on poultry", "Salmonella is a bacterium and does not make aflatoxin."), ("Yeast on grape juice", "Yeast makes alcohol."), ("Lactobacillus in milk", "Lactobacillus makes lactic acid.")],
      [("Aflatoxin", "The mould grows on damp stored crops.")], T_AFL, "Recall", "A mould, not a bacterium."),
    Q("Which measure best reduces aflatoxin contamination in stored grain?", "Dry the grain quickly to the safe moisture level and store it dry",
      [("Boil the grain before storing it", "Boiling would wet it and cooking does not remove existing toxin."), ("Store it in a warm damp place to ferment", "Warm damp conditions promote the mould."), ("Mix good and mouldy grain to dilute the toxin", "Mixing spreads the contamination and is unsafe.")],
      [("Control", "Low moisture stops mould growth.")], T_AFL, "Application", "Which factor does the mould need most?"),

    # ---- Sensory Evaluation & Food Analysis (7): sensory 3, proximate 2, titratable acidity and moisture 2
    Q("In a triangle test there are", "Three coded samples, of which two are identical",
      [("Two samples and a reference", "That is a duo-trio test."), ("Three different samples to rank", "That is a ranking test."), ("One sample scored on a scale", "That is a scoring or hedonic test.")],
      [("Triangle test", "The judge picks the odd one.")], T_SEN, "Recall", "How many identical samples are there?"),
    Q("Which control is essential in a sensory test?", "Random three-digit codes and a random order of presentation",
      [("Telling judges which brand is which", "This creates bias."), ("Letting judges discuss their answers", "This lets them influence each other."), ("Always serving the best sample first", "This biases the result.")],
      [("Controls", "Coding and randomisation remove bias.")], T_SEN, "Concept", "How do you avoid prejudice?"),
    Q("A hedonic test is used to find out", "How much consumers like a food",
      [("Whether two foods can be distinguished", "That is a difference test."), ("The nitrogen content of the food", "That is Kjeldahl analysis."), ("The pH of the food", "That is measured with a pH meter.")],
      [("Hedonic", "The judges score liking on a scale such as the 9-point scale.")], T_SEN, "Recall", "The word 'hedonic' relates to pleasure."),
    Q("The Kjeldahl method measures the total", "Nitrogen of a food, which is multiplied by a factor to estimate crude protein",
      [("Fat, which is multiplied by 9", "Fat is measured by Soxhlet extraction."), ("Moisture, by loss in mass", "Moisture is measured by drying or KF."), ("Ash, by burning at 550 degrees C", "Ash is a separate method.")],
      [("Kjeldahl", "Digest, distil, titrate: nitrogen × 6.25 estimates protein.")], T_PRO, "Recall", "Which element does Kjeldahl measure?"),
    Q("In the Soxhlet method, fat is determined from", "The mass of fat extracted by a solvent divided by the mass of sample",
      [("The loss in mass on heating at 105 degrees C", "That measures moisture."), ("The titre of standard hydrochloric acid", "That is the Kjeldahl titration."), ("The mass of ash left after burning", "That measures minerals.")],
      [("Soxhlet", "Petroleum ether dissolves the fat, which is weighed after evaporation.")], T_PRO, "Concept", "Which solvent step is involved?"),
    Q("Titratable acidity of a fruit juice is measured by titrating with standard", "Sodium hydroxide, to the colour change of phenolphthalein",
      [("Hydrochloric acid, to methyl orange", "The acids in the juice need an alkali."), ("Silver nitrate, to a precipitate", "That is a test for chloride."), ("Iodine, to a blue-black colour", "That is a test for starch.")],
      [("Method", "NaOH neutralises the food acids; the end point is about pH 8.2.")], T_TIT, "Recall", "Neutralising an acid needs what?"),
    Q("A 5.00 g sample of flour is dried to constant mass and weighs 4.40 g. The moisture content is", "12 percent",
      [("8.8 percent", "This is the dry matter in grams divided by 50, a power-of-ten slip."), ("88 percent", "This is the dry matter percentage."), ("0.6 percent", "This is the mass lost in grams, not a percentage.")],
      [("Moisture", "(5.00 − 4.40) ÷ 5.00 × 100 = 12 percent.")], T_TIT, "Calculation", "Divide the mass lost by the original mass."),
]
assert len(P1) == 50, len(P1)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="fsl2-paper1-multiple-choice",
    mock=True, time_limit_minutes=90, questions=build(P1, 31)))

# ------------------------------------------------------------------ Paper 2 practice paper A (structured, auto-markable parts)
# 8 numbered questions, 25 parts; the concept of each part is the topic title it tests. A KKEVO practice setting (150 minutes).
P2 = [
    # Question 1: water activity and carbohydrates
    Q("Question 1(a). A dried fruit sample is in equilibrium with air at 70 percent relative humidity. What is its water activity, and what does this tell you about moulds?", "0.70; many moulds can grow slowly, so it must be kept drier or sealed",
      [("70; no microbe can grow", "Water activity is on a 0 to 1 scale, and moulds can grow at about 0.70 to 0.80."), ("0.30; the food is safe", "The ERH divided by 100 gives 0.70, not its complement."), ("0.70; no microbe at all can grow", "Some specialised moulds and yeasts can grow near this value.")],
      [("a_w", "a_w = ERH ÷ 100 = 0.70, within the range of many moulds.")], T_WAT, "Application", "Divide the percentage by 100."),
    Q("Question 1(b). A cook mixes starch with water and heats the mixture; it thickens. After cooling overnight, the sauce becomes firm and water separates. Which two terms describe these changes in order?", "Gelatinisation then retrogradation",
      [("Retrogradation then gelatinisation", "Retrogradation happens after gelatinisation, on cooling."), ("Dextrinisation then caramelisation", "These need dry heat."), ("Denaturation then coagulation", "These describe protein changes.")],
      [("Starch", "Hot water swells the granules; on cooling the chains re-associate and squeeze out water.")], T_CHO, "Application", "Which comes on heating and which on cooling?"),
    Q("Question 1(c). Why does jam need acid as well as sugar and pectin?", "Acid reduces the negative charge on pectin so that the chains can join into a gel",
      [("Acid makes the pectin dissolve completely", "Acid helps gel formation; it does not just dissolve the pectin."), ("Acid replaces the sugar", "Sugar is still needed to bind water."), ("Acid kills the fruit enzymes only", "That is not the main reason for acid in a pectin gel.")],
      [("Pectin gel", "Low pH reduces the repulsion between pectin chains.")], T_CHO, "Concept", "What does acid do to the charges on pectin?"),
    # Question 2: lipids and proteins
    Q("Question 2(a). Which is the best definition of rancidity?", "The development of unpleasant tastes and smells in fats and oils through oxidation or hydrolysis",
      [("The hardening of oil by adding hydrogen", "That is hydrogenation."), ("The browning of cut vegetables", "That is enzymatic browning."), ("The setting of a protein gel", "That is coagulation.")],
      [("Rancidity", "Oxidative rancidity gives aldehydes and ketones; hydrolytic rancidity frees fatty acids.")], T_LIP, "Recall", "Which process spoils fats?"),
    Q("Question 2(b). Which measures best prevent oxidative rancidity in cooking oil?", "Store in a cool, dark, airtight container and use an antioxidant",
      [("Store in a clear bottle in the sun to kill microbes", "Light and heat speed oxidation."), ("Heat the oil repeatedly and keep it open", "Repeated heating and oxygen speed oxidation."), ("Add a small piece of copper wire", "Copper acts as a catalyst for oxidation.")],
      [("Prevention", "Exclude oxygen, light, heat and metals; antioxidants stop the chain reaction.")], T_LIP, "Application", "What speeds up oxidation, and how do you reverse it?"),
    Q("Question 2(c). Egg white is whisked to a stable foam. Which protein change explains the stability of the foam?", "Surface denaturation of the proteins, which form a film around the air bubbles",
      [("Hydrolysis of the proteins to amino acids", "That would destroy the film."), ("Retrogradation of the proteins", "Retrogradation is a starch change."), ("Caramelisation of protein", "Caramelisation is a sugar change.")],
      [("Foaming", "Whisking unfolds proteins at the air-liquid interface where they form a network.")], T_PROT, "Concept", "What happens to the proteins at the bubble surface?"),
    # Question 3: Maillard and vitamins
    Q("Question 3(a). Which set of conditions most favours the Maillard reaction in a baked product?", "A reducing sugar with an amino group, heat, and an intermediate water activity",
      [("Sucrose heated alone with no protein", "That is caramelisation."), ("Raw fruit with oxygen and an enzyme", "That is enzymatic browning."), ("Frozen food at a very low a_w", "At a very low a_w and temperature the rate is very low.")],
      [("Maillard", "Needs reducing sugar, amino groups, heat and moderate a_w.")], T_MAI, "Concept", "Which reaction is NOT caramelisation or enzymatic?"),
    Q("Question 3(b). Which cooking method retains the MOST vitamin C in green vegetables?", "Steaming or boiling briefly in a small volume of water",
      [("Boiling for a long time in a large volume of water", "Vitamin C leaches into water and is destroyed by heat."), ("Adding bicarbonate of soda and boiling", "Alkali destroys vitamin C and thiamin."), ("Keeping cooked vegetables warm for hours", "Heat and oxygen destroy vitamin C.")],
      [("Vitamin C", "Short time and little water limit leaching and heat damage.")], T_VIT, "Application", "Which factors destroy vitamin C?"),
    # Question 4: minerals, pigments, enzymes, colloids
    Q("Question 4(a). A child's diet is based on unrefined maize and beans with little meat. Which compound mainly reduces the absorption of iron and zinc?", "Phytate",
      [("Vitamin C", "Vitamin C improves non-haem iron absorption."), ("Haem iron", "Haem iron is well absorbed and is found in meat."), ("Lactose", "Lactose does not bind iron and zinc.")],
      [("Phytate", "Phytic acid binds minerals; soaking and fermenting reduce it.")], T_MIN, "Application", "Which anti-nutrient is in whole cereals and beans?"),
    Q("Question 4(b). Red cabbage is cooked with vinegar. The anthocyanin pigment will turn", "Redder (more red or pink)",
      [("Blue-green", "Blue-green colours appear in alkaline conditions."), ("Colourless", "It is not bleached by acid."), ("Brown", "Brown suggests enzymatic or Maillard browning.")],
      [("Anthocyanins", "Red in acid, purple near neutral, blue or green in alkali.")], T_PIG, "Application", "Is vinegar an acid or an alkali?"),
    Q("Question 4(c). Which enzyme causes the browning of cut yam and plantain in air?", "Polyphenol oxidase",
      [("Amylase", "Amylase hydrolyses starch."), ("Lipase", "Lipase hydrolyses fats."), ("Catalase", "Catalase breaks down hydrogen peroxide.")],
      [("Enzymatic browning", "Polyphenol oxidase oxidises phenols with oxygen.")], T_ENZ, "Recall", "Name the oxidase of phenols."),
    Q("Question 4(d). In mayonnaise, the egg yolk acts as", "An emulsifier that keeps oil droplets dispersed in water",
      [("A raising agent", "Egg yolk does not produce gas in mayonnaise."), ("A preservative that kills bacteria", "Yolk is not a preservative."), ("A thickener that gelatinises", "Mayonnaise thickens through emulsion, not starch gelatinisation.")],
      [("Emulsifier", "Lecithin has water-loving and oil-loving ends.")], T_COL, "Concept", "What is the role of lecithin?"),
    # Question 5: physiology and energy
    Q("Question 5(a). Which enzyme starts protein digestion and where does it act?", "Pepsin in the acid stomach",
      [("Amylase in the mouth", "Amylase starts starch digestion."), ("Lipase in the colon", "Lipase acts in the small intestine."), ("Trypsin in the stomach", "Trypsin acts in the small intestine at a higher pH.")],
      [("Digestion", "Pepsin works in the acid of the stomach.")], T_DIG, "Recall", "Which enzyme needs acid?"),
    Q("Question 5(b). Which of the following is the BEST description of gluconeogenesis?", "The making of glucose from non-carbohydrate substances such as amino acids and glycerol",
      [("The breakdown of glucose to pyruvate", "That is glycolysis."), ("The breakdown of fatty acids to acetyl CoA", "That is beta-oxidation."), ("The removal of the amino group from amino acids", "That is deamination.")],
      [("Gluconeogenesis", "It keeps blood glucose up in fasting, mainly in the liver.")], T_MET, "Concept", "Neo means new."),
    N("Question 5(c). A man has a BMR of 7000 kJ per day and a PAL of 1.6. Calculate his estimated total energy requirement in kJ per day.", 11200,
      [("Formula", "TEE = BMR × PAL."), ("Calculate", "7000 × 1.6 = 11 200 kJ.")], T_BMR, "Calculation", "Multiply BMR by the activity factor.", tol=1, unit="kJ"),
    N("Question 5(d). A food contains 10 g protein, 20 g fat and 60 g carbohydrate per 100 g. Calculate its energy in kJ per 100 g using 17, 37 and 17 kJ per gram.", 1930,
      [("Protein", "10 × 17 = 170 kJ."), ("Fat", "20 × 37 = 740 kJ."), ("Carbohydrate and total", "60 × 17 = 1020; 170 + 740 + 1020 = 1930 kJ.")], T_ENR, "Calculation", "Multiply each mass by its factor and add.", tol=1, unit="kJ"),
    # Question 6: microbiology
    N("Question 6(a). A food has 2 000 bacteria. After 90 minutes of growth in the log phase it has 16 000. Calculate the generation time in minutes.", 30,
      [("Generations", "16 000 ÷ 2 000 = 8 = 2^3, so 3 generations."), ("Generation time", "90 ÷ 3 = 30 minutes.")], T_FAC, "Calculation", "How many doublings give a factor of eight?", tol=0.1, unit="minutes"),
    Q("Question 6(b). Which description matches the fermentation of one mole of glucose by yeast?", "Two moles of ethanol and two moles of carbon dioxide",
      [("Two moles of lactic acid", "That is homolactic fermentation."), ("Six moles of carbon dioxide and six of water", "That is complete aerobic respiration."), ("One mole of ethanol and one of carbon dioxide", "The equation gives two of each.")],
      [("Equation", "C6H12O6 gives 2 C2H5OH + 2 CO2.")], T_FER, "Recall", "Count the carbons on each side."),
    Q("Question 6(c). A cream cake handled by a food worker with an infected finger causes vomiting 3 hours after eating, with no fever. Which organism and type of illness fit best?", "Staphylococcus aureus; an intoxication",
      [("Salmonella; an infection", "Salmonella gives fever and diarrhoea after a longer time."), ("Clostridium botulinum; an infection", "Botulism is an intoxication with paralysis."), ("Aspergillus flavus; an infection", "Aspergillus is a mould that makes aflatoxin.")],
      [("Food poisoning", "Short onset and a skin source indicate preformed enterotoxin.")], T_INF, "Application", "Which organism is on skin, and which is a toxin?"),
    Q("Question 6(d). Why is cooking NOT a reliable way to make aflatoxin-contaminated groundnuts safe?", "Aflatoxin is heat stable and persists after the mould is killed",
      [("Cooking increases the number of mould spores", "Cooking kills the mould."), ("Aflatoxin is a protein that cooks", "Aflatoxin is a stable small molecule, not a protein."), ("Aflatoxin is destroyed only at 30 degrees C", "It is not destroyed at that temperature, nor is the statement true.")],
      [("Aflatoxin", "Prevention is the only control.")], T_AFL, "Reasoning", "What survives?"),
    # Question 7: sensory
    Q("Question 7(a). In a triangle test with 18 judges, the minimum number of correct answers for significance at the 5 percent level (one-sided) is 10. If 9 judges choose correctly, the conclusion is", "No significant difference has been shown",
      [("The samples are significantly different", "9 is below the minimum of 10."), ("The samples are identical", "A non-significant result does not prove they are identical."), ("The test is invalid", "The result is usable; it is just not significant.")],
      [("Interpretation", "9 is less than 10, so luck cannot be excluded.")], T_SEN, "Interpretation", "Compare 9 with 10."),
    N("Question 7(b). Five consumers score a drink on the 9-point hedonic scale: 6, 7, 8, 5, 9. Calculate the mean score.", 7,
      [("Total", "6 + 7 + 8 + 5 + 9 = 35."), ("Mean", "35 ÷ 5 = 7.")], T_SEN, "Calculation", "Add the scores and divide by 5.", tol=0.01, unit="points"),
    # Question 8: analysis
    N("Question 8(a). A 0.500 g sample needs 18.60 cm³ of 0.100 M HCl and the blank needs 0.20 cm³. Calculate the percentage nitrogen (A(N) = 14.007) to two decimal places.", 5.15,
      [("Corrected titre", "18.60 − 0.20 = 18.40 cm³."), ("Moles of N", "18.40 × 0.100 ÷ 1000 = 1.840 × 10^-3 mol."), ("Percentage", "1.840 × 10^-3 × 14.007 = 0.02577 g; ÷ 0.500 × 100 = 5.15 percent.")], T_PRO, "Calculation", "Subtract the blank first.", tol=0.01, unit="%"),
    N("Question 8(b). 25.0 cm³ of wine needs 18.4 cm³ of 0.100 M NaOH. Calculate the titratable acidity as tartaric acid (equivalent mass 75.04) in g per 100 cm³, to two decimal places.", 0.55,
      [("Moles", "18.4 × 0.100 ÷ 1000 = 1.84 × 10^-3 mol."), ("Mass of acid", "1.84 × 10^-3 × 75.04 = 0.1381 g."), ("Per 100 cm³", "0.1381 ÷ 25.0 × 100 = 0.552, about 0.55 g per 100 cm³.")], T_TIT, "Calculation", "Moles of NaOH equal moles of acidic hydrogen.", tol=0.01, unit="g per 100 cm³"),
    N("Question 8(c). A 10.0 g sample of a food weighs 8.7 g after drying to constant mass. Calculate its moisture content (wet basis) in percent.", 13,
      [("Mass lost", "10.0 − 8.7 = 1.3 g."), ("Percentage", "1.3 ÷ 10.0 × 100 = 13 percent.")], T_TIT, "Calculation", "Divide the mass lost by the starting mass.", tol=0.1, unit="%"),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="fsl2-paper2-essay",
    mock=True, time_limit_minutes=150, questions=build(P2, 32)))

