"""A Level Biology (0710), Lower Sixth: practice sets for Gaseous Exchange & Mass Transport Systems, Ecology, Population Dynamics & Conservation and the Examination module.

One 8-question set per lesson (13 topic lessons, 3 examination lessons), plus 'Paper 1 mock exam A' (50 multiple-choice questions
across all seven modules in proportion to their topic counts) and 'Paper 2 practice paper A' (25 auto-markable parts in 8 numbered
questions). Exam facts are only those of the Board's 2023 subject report (Paper 1 = 50 multiple-choice questions, Paper 2 = theory,
Paper 3 = practical). The timings of the mock papers (90 and 150 minutes) are KKEVO practice settings, not Board settings. Essays cannot
be marked automatically, so the Paper 2 practice paper is a structured version with multiple-choice and numeric parts.
Numerical answers (ventilation, cardiac output, potometer, productivity, Simpson's index, capture-recapture, statistics) were checked
by script.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("biology", "lower-sixth")

M_CYT = "Cytology & Membrane Physiology"
M_MOL = "Biological Molecules & Enzymology"
M_NUC = "Nucleic Acids, Protein Synthesis & Cell Division"
M_BIO = "Biodiversity & Systematic Taxonomy"
M_NUT = "Autotrophic & Heterotrophic Nutrition"
M_GAS = "Gaseous Exchange & Mass Transport Systems"
M_ECO = "Ecology, Population Dynamics & Conservation"
M_EXAM = "Examination"


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

# Exact topic titles (apps/academics/gce_curriculum.py, ("biology", "lower-sixth")).
T_PROK = "Prokaryotic and eukaryotic cells"
T_FLUID = "The fluid-mosaic model"
T_WPOT = "Water potential"
T_TRANS = "Transport across membranes"
T_CARB = "Carbohydrates"
T_LIP = "Lipids"
T_PROT = "Amino acids and protein structure"
T_ENZK = "Enzyme kinetics"
T_ENZI = "Enzyme inhibition and regulation"
T_DNA = "DNA and RNA structure"
T_REP = "DNA replication"
T_CODE = "The genetic code, transcription and translation"
T_MITO = "The cell cycle and mitosis"
T_MEI = "Meiosis"
T_DOM = "Domains and kingdoms"
T_KEY = "Dichotomous keys"
T_PROTO = "Protoctista and Fungi"
T_PLANT = "Plantae"
T_ANIM = "Animalia phyla"
T_CHLO = "Chloroplast structure and pigments"
T_LIGHT = "The light-dependent stage"
T_CALV = "The Calvin cycle and photorespiration"
T_C4 = "C3, C4 and CAM plants"
T_DIG = "Digestive histology and control of secretion"
T_VENT = "Ventilation and gaseous exchange"
T_ODC = "Oxygen dissociation curves"
T_CARD = "The cardiac cycle and its control"
T_TISS = "Tissue fluid formation"
T_WATER = "Water transport in plants"
T_PHLO = "Phloem transport"
T_ENER = "Energy flow and productivity"
T_CYC = "Biogeochemical cycles"
T_SUCC = "Ecological succession"
T_POP = "Population dynamics"
T_BDIV = "Biodiversity, pollution and conservation"

# ------------------------------------------------------------------ 1. Ventilation and gaseous exchange
SP = "al-bil3-spirometer.svg"
SP_ALT = "Spirometer trace over 30 seconds: three normal breaths around 2.2 to 2.7 dm3, a deepest breath in reaching 5.7 dm3 and a deepest breath out reaching 1.2 dm3, with brackets for IRV, TV, ERV, RV and VC"
V1 = [
    Q("Which muscles contract during inspiration in a resting person?", "The diaphragm and the external intercostal muscles",
      [("The diaphragm and the internal intercostal muscles", "The internal intercostals contract in forced expiration, pulling the ribs down."),
       ("The abdominal muscles and the internal intercostal muscles", "These are used to force air out during exercise."),
       ("The external intercostal muscles only, while the diaphragm relaxes", "The diaphragm contracts and flattens in inspiration; it does not relax.")],
      [("Recall", "At rest, inspiration is active. The diaphragm contracts and flattens and the external intercostals lift the ribs up and out.")],
      "Muscles of inspiration", "Recall", "Which muscles raise the ribs?"),
    Q("During inspiration, which change in the lungs allows air to flow in?", "The pressure in the lungs falls below atmospheric pressure",
      [("The pressure in the lungs rises above atmospheric pressure", "That would push air out, as in expiration."),
       ("The volume of the thorax decreases", "A decrease in volume raises the pressure and expels air."),
       ("The lungs actively expand because of their own muscle", "The lungs contain no muscle for expansion; they follow the movement of the thorax.")],
      [("Muscles", "Muscle contraction increases the volume of the thorax."), ("Pressure", "A larger volume gives a lower pressure, so air flows from the higher atmospheric pressure into the lungs.")],
      "Pressure changes in ventilation", "Concept", "Air moves from high to low pressure."),
    Q("What is the function of surfactant in the alveoli?", "It lowers the surface tension of the water film, keeping the alveoli open",
      [("It makes the alveolar wall thicker", "A thicker wall would slow diffusion."),
       ("It carries oxygen into the blood", "Haemoglobin carries oxygen; surfactant is not a gas carrier."),
       ("It kills bacteria that enter the lungs", "Phagocytes and mucus do this; surfactant reduces surface tension.")],
      [("Role", "Surfactant, a mixture of phospholipids and proteins, reduces the surface tension and prevents the walls sticking when breathing out.")],
      "Surfactant", "Recall", "Think of what water does to the walls of a wet balloon."),
    N("A student's tidal volume is 0.45 dm³ and she breathes 16 times per minute. Calculate her pulmonary ventilation in dm³ per minute.", 7.2,
      [("Formula", "Pulmonary ventilation = tidal volume × breathing rate."), ("Calculate", "0.45 × 16 = 7.2 dm³ per minute.")],
      "Pulmonary ventilation", "Calculation", "Multiply the volume of one breath by the number of breaths.", tol=0.05, unit="dm³ per minute"),
    N("The spirometer trace shows the deepest breath in reaching 5.7 dm³ and the deepest breath out reaching 1.2 dm³. Calculate the vital capacity in dm³.", 4.5,
      [("Meaning", "Vital capacity is the largest volume that can be breathed out after the deepest breath in."), ("Calculate", "5.7 − 1.2 = 4.5 dm³.")],
      "Vital capacity from a trace", "Interpretation", "Vital capacity is the difference between the highest and lowest points.", tol=0.05, unit="dm³", diagram=SP, alt=SP_ALT),
    Q("A disease causes scarring that thickens the walls of the alveoli. Why does this reduce gaseous exchange?", "The diffusion distance is greater, so the rate of diffusion is lower",
      [("The surface area of the alveoli increases", "Scarring does not increase the surface area."),
       ("The concentration gradient becomes steeper", "A thicker wall does not make the gradient steeper."),
       ("More oxygen is removed by the blood", "Slower diffusion means less oxygen enters.")],
      [("Fick's law", "Rate is inversely proportional to the thickness of the barrier. A thicker wall means a lower rate.")],
      "Fick's law", "Reasoning", "Which term in Fick's law involves thickness?"),
    N("A person has a tidal volume of 0.50 dm³, a dead space of 0.15 dm³ and a breathing rate of 14 per minute. Calculate the alveolar ventilation in dm³ per minute.", 4.9,
      [("Air reaching the alveoli", "0.50 − 0.15 = 0.35 dm³ in each breath."), ("Per minute", "0.35 × 14 = 4.9 dm³ per minute.")],
      "Alveolar ventilation", "Calculation", "Remove the dead space from each breath first.", tol=0.05, unit="dm³ per minute"),
    Q("What is the main stimulus that increases the breathing rate during hard exercise?", "A rise in blood carbon dioxide, lowering the pH, detected by chemoreceptors",
      [("A fall in blood oxygen concentration detected in the lungs", "Oxygen level changes matter less than CO₂ in the normal control of breathing."),
       ("Stretching of the lung tissue", "Stretch receptors prevent over-inflation but do not raise the rate."),
       ("A rise in blood pH detected by baroreceptors", "Exercise lowers the pH, and baroreceptors detect pressure, not pH.")],
      [("Control", "More respiration produces more CO₂, which forms carbonic acid and lowers the blood pH. Chemoreceptors signal the medulla, which increases the rate and depth of breathing.")],
      "Control of breathing", "Application", "Which gas is produced in larger amounts by exercising muscles?"),
]
SETS.append(practice_set(module=M_GAS, topic=T_VENT, title="Ventilation, alveoli and lung volumes", lesson="bil3-ventilation-gas-exchange", questions=build(V1, 101)))

# ------------------------------------------------------------------ 2. Oxygen dissociation curves
OD = "al-bil3-odc-q.svg"
OD_ALT = "Three S-shaped oxygen dissociation curves labelled P (leftmost), Q (middle) and R (rightmost) on axes of haemoglobin saturation against partial pressure of oxygen"
V2 = [
    Q("How many molecules of oxygen can one haemoglobin molecule carry?", "Four",
      [("One", "That is myoglobin, which has one haem group."), ("Two", "Haemoglobin has four haem groups, not two."), ("Eight", "Each haem group binds one oxygen molecule, so four in total.")],
      [("Structure", "Haemoglobin has four polypeptides, each with one haem group, and each haem binds one O₂.")],
      "Haemoglobin structure", "Recall", "Count the haem groups."),
    Q("The figure shows curves for adult haemoglobin at normal CO₂ (Q), adult haemoglobin at high CO₂, and fetal haemoglobin. Which curve is fetal haemoglobin?", "P",
      [("Q", "Q is the adult curve in the middle of the three."), ("R", "R is to the right, so it has the lowest affinity; this is the high-CO₂ curve."), ("It cannot be told from the figure", "Fetal haemoglobin has a higher affinity, so its curve is to the left.")],
      [("Affinity", "Fetal haemoglobin must load oxygen from the mother's blood, so it has a higher affinity: its curve is to the left of the adult curve.")],
      "Fetal haemoglobin", "Interpretation", "Which curve is highest at low pO₂?", diagram=OD, alt=OD_ALT),
    Q("In the same figure, which curve represents adult haemoglobin at a high CO₂ concentration (Bohr shift)?", "R",
      [("P", "P is to the left and shows a higher affinity, as in fetal haemoglobin."), ("Q", "Q is the normal adult curve."), ("P and R are identical", "The curves are different.")],
      [("Bohr shift", "A rise in CO₂ moves the curve to the right, so haemoglobin releases oxygen more readily at a given pO₂.")],
      "Bohr shift", "Interpretation", "Right means a lower affinity.", diagram=OD, alt=OD_ALT),
    Q("Why is the oxygen dissociation curve of haemoglobin S-shaped?", "After the first oxygen binds, the shape of the molecule changes and it becomes easier for the next ones to bind",
      [("Each oxygen molecule binds equally easily to every haem group", "That would give a straight or hyperbolic curve."),
       ("Haemoglobin has only one haem group", "That describes myoglobin, which has a hyperbolic curve."),
       ("Oxygen molecules repel each other on the haem groups", "Binding becomes easier, not harder, after the first oxygen.")],
      [("Cooperative binding", "The first oxygen is hard to bind. It changes the shape of the protein so that the others bind more easily. The last is again harder, which levels the curve.")],
      "Cooperative binding", "Concept", "What happens to the shape of haemoglobin after the first oxygen binds?"),
    Q("What causes the Bohr shift in respiring tissue?", "Hydrogen ions from carbonic acid bind to haemoglobin, lowering its affinity for oxygen",
      [("Hydrogencarbonate ions bind to the haem group", "Hydrogencarbonate is carried in the plasma; hydrogen ions affect the protein."),
       ("Carbonic anhydrase breaks down haemoglobin", "The enzyme acts on CO₂ and water, not on haemoglobin."),
       ("Low pO₂ makes the red blood cell burst", "Haemoglobin loses oxygen at low pO₂ but cells do not burst.")],
      [("Mechanism", "CO₂ + H₂O gives H₂CO₃ (carbonic anhydrase), then H⁺ and HCO₃⁻. The H⁺ binds haemoglobin and alters its shape so that it releases oxygen.")],
      "Cause of the Bohr effect", "Concept", "Which ion lowers the pH?"),
    Q("What is the purpose of the chloride shift in a red blood cell?", "To balance the charge as hydrogencarbonate ions leave the cell",
      [("To carry chloride to the lungs", "The chloride ions move into the red blood cell, not to the lungs."),
       ("To release oxygen from haemoglobin", "Oxygen release is caused by H⁺, the Bohr effect."),
       ("To make carbonic anhydrase work", "The enzyme does not need chloride to work.")],
      [("Charge balance", "HCO₃⁻ diffuses out. Cl⁻ moves in so that the inside of the cell does not become positively charged.")],
      "Chloride shift", "Concept", "Think about the charge on hydrogencarbonate."),
    N("Haemoglobin leaves the lungs 97% saturated with oxygen and, in an exercising muscle on the high-CO₂ curve at 4 kPa, is 41% saturated. By how many percentage points does the saturation fall (the oxygen released)?", 56,
      [("Subtract", "97 − 41 = 56 percentage points of saturation.")],
      "Unloading of oxygen", "Calculation", "Subtract the saturation in the tissue from the saturation leaving the lungs.", tol=0.5, unit="percentage points"),
    Q("Myoglobin has one haem group and a curve to the left of haemoglobin. What is its function in muscle?", "It holds oxygen as a store and releases it only when the pO₂ is very low",
      [("It carries oxygen from the lungs to the muscle", "Haemoglobin does that."),
       ("It carries carbon dioxide to the lungs", "Myoglobin does not carry CO₂."),
       ("It releases oxygen at high pO₂ in the lungs", "It has a high affinity and holds oxygen unless the pO₂ is very low.")],
      [("Affinity", "A curve to the left means a high affinity: it loads at low pO₂ and gives up oxygen only in very active muscle.")],
      "Myoglobin", "Application", "A curve to the left means a higher or lower affinity?"),
]
SETS.append(practice_set(module=M_GAS, topic=T_ODC, title="Oxygen dissociation curves and the Bohr shift", lesson="bil3-oxygen-dissociation-curves", questions=build(V2, 102)))

# ------------------------------------------------------------------ 3. Cardiac cycle (pressure, volume, valves)
CD = "al-bil3-cardiac-q.svg"
CD_ALT = "Graph of pressure against time over 0.8 seconds for the aorta, left ventricle and left atrium, with three shaded phases J, K and L and four marked events W, X, Y and Z along the time axis"
V3 = [
    Q("Which term means the contraction phase of the cardiac cycle?", "Systole",
      [("Diastole", "Diastole is the relaxation phase."), ("Diffusion", "Diffusion is the movement of particles, not a phase of the heart."), ("Stroke volume", "That is the volume of blood pumped out in one beat.")],
      [("Definition", "Systole is contraction; diastole is relaxation.")], "Systole and diastole", "Recall", "It is the opposite of diastole."),
    Q("When does the aortic (semilunar) valve open?", "When the pressure in the left ventricle rises above the pressure in the aorta",
      [("When the left atrium contracts", "Atrial contraction pushes blood into the ventricle through the AV valve."),
       ("When the pressure in the aorta rises above the ventricular pressure", "That closes the valve."),
       ("When the ventricle starts to relax", "Relaxation lowers the ventricular pressure and shuts the valve.")],
      [("Valves are passive", "Blood is pushed through the valve whenever the pressure behind it exceeds the pressure in front.")],
      "Semilunar valve", "Concept", "Which side has the higher pressure when a valve opens?"),
    Q("In the figure, which letter marks the point where the AV valve closes at the start of ventricular systole (the first heart sound)?", "W",
      [("X", "X is where the aortic valve opens, after the pressure rise in the closed ventricle."), ("Y", "Y is where the aortic valve closes."), ("Z", "Z is where the AV valve opens again, in diastole.")],
      [("Read the graph", "The ventricular pressure first rises above the atrial pressure at W. This closes the AV valve. Then the ventricular pressure rises with all valves shut.")],
      "Valve events", "Interpretation", "Look for the first crossing of the ventricular and atrial curves.", diagram=CD, alt=CD_ALT),
    Q("In the figure, which letter marks the closing of the aortic valve, which causes the second heart sound?", "Y",
      [("W", "W is the closing of the AV valve."), ("X", "X is the opening of the aortic valve."), ("Z", "Z is the opening of the AV valve.")],
      [("Read the graph", "The aortic valve closes when the ventricular pressure falls below the aortic pressure, at Y, just before the steep pressure fall in the ventricle.")],
      "Valve events", "Interpretation", "Find where the ventricular curve falls below the aortic curve.", diagram=CD, alt=CD_ALT),
    N("The left ventricle has an end-diastolic volume of 120 cm³ and an end-systolic volume of 50 cm³. The heart rate is 75 beats per minute. Calculate the cardiac output in cm³ per minute.", 5250,
      [("Stroke volume", "120 − 50 = 70 cm³."), ("Cardiac output", "70 × 75 = 5250 cm³ per minute.")],
      "Cardiac output", "Calculation", "First find the stroke volume.", tol=5, unit="cm³ per minute"),
    N("The heart rate of an athlete at rest is 60 beats per minute. How long, in seconds, does one cardiac cycle last?", 1.0,
      [("Calculate", "60 s ÷ 60 beats = 1.0 s per cycle.")],
      "Length of the cardiac cycle", "Calculation", "Divide 60 seconds by the heart rate.", tol=0.01, unit="s"),
    N("A ventricle has an end-diastolic volume of 140 cm³ and an end-systolic volume of 60 cm³. Calculate the ejection fraction as a percentage (to the nearest whole number).", 57,
      [("Stroke volume", "140 − 60 = 80 cm³."), ("Fraction", "80 ÷ 140 × 100 = 57%.")],
      "Ejection fraction", "Calculation", "Ejection fraction = stroke volume ÷ end-diastolic volume × 100.", tol=1, unit="%"),
    Q("Why is the wall of the left ventricle much thicker than the wall of the right ventricle?", "It must generate a much higher pressure to pump blood around the whole body",
      [("It holds more blood than the right ventricle", "Both ventricles pump the same volume."),
       ("It contains more valves", "The number of valves does not explain the thickness."),
       ("It receives blood directly from the body", "It receives blood from the lungs through the left atrium.")],
      [("Pressure", "The left ventricle pumps to the whole body through the aorta, so it needs a thick muscular wall for high pressure. The right pumps only to the nearby lungs.")],
      "Structure of the ventricle", "Application", "Compare the distance the blood must travel from each ventricle."),
]
SETS.append(practice_set(module=M_GAS, topic=T_CARD, title="The cardiac cycle: pressure, volume and valves", lesson="bil3-cardiac-cycle", questions=build(V3, 103)))

# ------------------------------------------------------------------ 4. Control of the heartbeat
V4 = [
    Q("What does it mean to say that the heart is myogenic?", "The heart muscle starts its own contractions without nerve impulses",
      [("The heart can only beat when nerves stimulate it", "That is the opposite of myogenic."), ("The heart is controlled by hormones only", "Hormones change the rate, but the beat is started in the muscle."), ("The heart has no muscle", "The heart is made of cardiac muscle.")],
      [("Definition", "Myogenic muscle contracts rhythmically without a stimulus from nerves.")], "Myogenic", "Recall", "Myo means muscle."),
    Q("Where is the sinoatrial node found?", "In the wall of the right atrium",
      [("In the wall of the left ventricle", "The ventricle wall carries Purkyne fibres, not the pacemaker."), ("In the septum between the ventricles", "That is the bundle of His."), ("In the aorta", "The aorta has baroreceptors but not the pacemaker.")],
      [("Location", "The SAN is a patch of muscle tissue in the wall of the right atrium.")], "Sinoatrial node", "Recall", "It is in the upper right of the heart."),
    Q("What is the function of the delay at the atrioventricular node?", "It lets the atria finish contracting and emptying before the ventricles contract",
      [("It stops the SAN from firing too often", "The delay does not control the SAN."), ("It makes the ventricles contract from the top downwards", "They contract from the apex upwards."), ("It prevents blood entering the atria", "The atria fill during diastole.")],
      [("Timing", "The wave is delayed for about 0.1 s so that the ventricles contract only after the atria have emptied into them.")], "AVN delay", "Concept", "Which chambers should empty first?"),
    Q("What is the role of the Purkyne fibres?", "To carry the wave of excitation up the walls of the ventricles so they contract from the apex",
      [("To start the heartbeat", "That is the role of the SAN."), ("To delay the wave of excitation", "That is the role of the AVN."), ("To conduct the wave from the SAN to the AVN across the atria", "The wave passes across the atria in the muscle walls.")],
      [("Pathway", "Bundle of His to the apex, then Purkyne fibres up through the ventricle walls.")], "Purkyne fibres", "Recall", "They are the last part of the pathway."),
    Q("On an ECG trace, the QRS complex represents:", "Depolarisation of the ventricles, which then contract",
      [("Depolarisation of the atria", "That is the P wave."), ("Recovery (repolarisation) of the ventricles", "That is the T wave."), ("The delay at the AVN", "The delay appears as the flat part between the P wave and the QRS complex.")],
      [("Waves", "P = atrial depolarisation, QRS = ventricular depolarisation, T = ventricular repolarisation.")], "ECG waves", "Recall", "Which chambers have the larger muscle mass?"),
    N("On an ECG, the time between two successive R peaks is 0.75 s. Calculate the heart rate in beats per minute.", 80,
      [("Calculate", "60 ÷ 0.75 = 80 beats per minute.")], "Heart rate from an ECG", "Calculation", "Heart rate = 60 divided by the time of one cycle in seconds.", tol=0.5, unit="beats per minute"),
    Q("Which nerve slows the heart rate, and which chemical does it release?", "The vagus nerve, releasing acetylcholine",
      [("The sympathetic nerve, releasing noradrenaline", "That speeds up the heart."), ("The vagus nerve, releasing noradrenaline", "The vagus releases acetylcholine."), ("The sympathetic nerve, releasing acetylcholine", "The sympathetic nerve releases noradrenaline.")],
      [("Autonomic control", "The parasympathetic vagus nerve slows the heart through acetylcholine at the SAN.")], "Nervous control of the heart", "Recall", "Parasympathetic nerves use acetylcholine."),
    Q("Blood pressure rises in the aorta. What is the most likely response?", "Baroreceptors send more impulses to the cardiac centre, which sends more impulses along the vagus nerve and the heart rate falls",
      [("Chemoreceptors stimulate the sympathetic nerve and the heart rate rises", "A rise in pressure is detected by baroreceptors, and the response is to slow the heart."),
       ("The SAN stops firing completely", "The SAN keeps firing; the rate is reduced."),
       ("Adrenaline is released and the heart rate rises", "Adrenaline raises pressure; it is not the response to a rise in pressure.")],
      [("Negative feedback", "A rise in pressure is detected by baroreceptors. The cardiac centre increases impulses on the vagus nerve, which slows the heart and lowers the pressure.")],
      "Negative feedback on blood pressure", "Application", "Which sensors detect pressure?"),
]
SETS.append(practice_set(module=M_GAS, topic=T_CARD, title="Control of the heartbeat: SAN, ECG and nerves", lesson="bil3-cardiac-control-sa-node-ecg", questions=build(V4, 104)))

# ------------------------------------------------------------------ 5. Tissue fluid formation
ST = "al-bil3-starling-q.svg"
ST_ALT = "Graph of pressure in kilopascals along a capillary: line P falls steadily from 4.5 to 2.0, line Q stays level at 3.0, with points W near the start, X where the lines cross and Y at the end of the capillary"
V5 = [
    Q("Which of the following is found in blood plasma but is normally absent or in very low amounts in tissue fluid?", "Large plasma proteins",
      [("Glucose", "Glucose passes freely out of capillaries into tissue fluid."), ("Oxygen", "Oxygen is carried to cells through the tissue fluid."), ("Water", "Water is the main component of tissue fluid.")],
      [("Composition", "Tissue fluid is plasma that has been filtered, without red blood cells and with very few large proteins.")], "Composition of tissue fluid", "Recall", "Which substances are too large to leave the capillary?"),
    Q("In the figure, which line represents the oncotic pressure of the plasma proteins?", "Line Q, because it stays level along the capillary",
      [("Line P, because it falls along the capillary", "Line P falls because the blood loses pressure; this is the hydrostatic pressure."), ("Line P, because it is the higher line at the start", "A higher value at the start does not identify oncotic pressure; its fall does show hydrostatic pressure."), ("Neither line", "One of them is oncotic pressure.")],
      [("Reasoning", "The plasma proteins stay in the capillary, so their oncotic pressure stays about constant. The hydrostatic pressure falls along the capillary.")],
      "Hydrostatic and oncotic pressure", "Interpretation", "Which pressure depends on the force of the heart?", diagram=ST, alt=ST_ALT),
    Q("In the figure, what happens to fluid at point X, where lines P and Q cross?", "There is no net movement of fluid",
      [("Fluid leaves the capillary rapidly", "Fluid leaves where P is above Q, before X."), ("Fluid enters the capillary rapidly", "Fluid enters where Q is above P, after X."), ("Fluid is destroyed in the capillary", "Fluid is not destroyed; it is just in balance.")],
      [("Balance", "At X the outward and inward pressures are equal, so the net filtration pressure is zero.")],
      "Net filtration pressure", "Interpretation", "What is the difference between the two pressures at X?", diagram=ST, alt=ST_ALT),
    N("At one point along a capillary the hydrostatic pressure is 4.2 kPa and the oncotic pressure is 3.0 kPa. Calculate the net filtration pressure in kPa (positive means fluid leaves).", 1.2,
      [("Subtract", "4.2 − 3.0 = +1.2 kPa. The sign is positive, so the net movement is out of the capillary.")],
      "Net filtration pressure", "Calculation", "Net filtration pressure = hydrostatic pressure − oncotic pressure.", tol=0.05, unit="kPa"),
    Q("Why does the hydrostatic pressure in a capillary fall along its length?", "Fluid has left the blood and friction with the capillary wall resists flow",
      [("Plasma proteins leave the blood", "Plasma proteins stay in the capillary."), ("The heart stops pushing blood", "The heart continues to pump; the pressure falls along the vessels because of resistance."), ("Red blood cells enter the tissue fluid", "Red blood cells do not leave capillaries.")],
      [("Resistance", "Friction and the loss of fluid by filtration lower the pressure along the capillary.")],
      "Pressure along a capillary", "Concept", "What happens to the volume of blood in the capillary as fluid leaves?"),
    Q("Why do children with kwashiorkor often have a swollen abdomen?", "Low plasma protein lowers the oncotic pressure, so less fluid returns to the capillaries",
      [("High plasma protein raises the oncotic pressure", "Kwashiorkor is a lack of protein."), ("The lymph vessels produce too much fluid", "The problem is not in the lymph vessels but in the blood."), ("The hydrostatic pressure of the blood falls", "A lower hydrostatic pressure would reduce fluid leaving, not cause oedema.")],
      [("Oedema", "The diet lacks protein, so plasma protein is low. Less water is drawn back by osmosis, and tissue fluid accumulates.")],
      "Causes of oedema", "Application", "Which pressure draws water back into the capillary?"),
    Q("What is the main function of the lymphatic system in relation to tissue fluid?", "To return excess tissue fluid to the blood",
      [("To carry oxygen to cells", "Blood carries oxygen."), ("To pump blood round the body", "The heart pumps blood; the lymph system has no pump."), ("To make red blood cells", "Red blood cells are made in bone marrow.")],
      [("Drainage", "Tissue fluid that does not return to the capillaries enters lymph capillaries and drains back into the blood near the heart.")],
      "Function of lymph", "Recall", "Where does tissue fluid go if it does not re-enter the capillary?"),
    Q("In lymphatic filariasis, parasitic worms block the lymph vessels of the leg. Why does the leg swell?", "Excess tissue fluid cannot drain away",
      [("Too much blood enters the leg", "The problem is the drainage of tissue fluid."), ("The plasma proteins increase in concentration in the blood", "That would draw more fluid into the capillary."), ("The capillaries absorb too much water", "Capillaries return water at the venule end; the problem is outside them.")],
      [("Blocked drainage", "Tissue fluid forms normally, but when the lymph vessels are blocked it accumulates in the tissues as oedema.")],
      "Oedema and blocked lymph", "Application", "Where does the fluid normally go?"),
]
SETS.append(practice_set(module=M_GAS, topic=T_TISS, title="Tissue fluid, Starling's hypothesis and oedema", lesson="bil3-tissue-fluid-starling", questions=build(V5, 105)))

# ------------------------------------------------------------------ 6. Water transport in plants
V6 = [
    N("A cell has a solute potential of −1.0 MPa and a pressure potential of +0.6 MPa. Calculate its water potential in MPa.", -0.4,
      [("Formula", "Ψ = Ψs + Ψp."), ("Calculate", "−1.0 + 0.6 = −0.4 MPa.")],
      "Water potential of a cell", "Calculation", "Add the two components and keep the signs.", tol=0.01, unit="MPa"),
    Q("Cell X has a water potential of −0.4 MPa and the neighbouring cell Y has −0.7 MPa. In which direction does water move?", "From X to Y",
      [("From Y to X", "Water moves to the lower (more negative) water potential, which is Y."), ("Neither, because both are negative", "A difference in water potential drives movement."), ("From X to Y only if X has a higher pressure potential", "The overall water potential decides direction.")],
      [("Gradient", "Water moves from higher (less negative, −0.4) to lower (more negative, −0.7) water potential, by osmosis.")],
      "Direction of osmosis", "Application", "Which number is higher: −0.4 or −0.7?"),
    Q("What is the effect of the Casparian strip in the endodermis?", "It blocks the apoplast pathway, so water must pass through the cytoplasm of the endodermal cells",
      [("It blocks the symplast pathway", "The symplast pathway is through the cytoplasm and is not blocked."), ("It pumps water into the xylem", "It is a waterproof band of suberin and has no pumping action."), ("It stops all water from entering the xylem", "Water still enters by the symplast route.")],
      [("Selective entry", "The strip of suberin in the walls blocks the movement of water through the cell walls, so the water must cross the membrane, which controls what enters the xylem.")],
      "Casparian strip", "Concept", "In which pathway does the water move through cell walls?"),
    Q("In the apoplast pathway, water moves:", "Through the cell walls and spaces between cells without crossing a membrane",
      [("Through the cytoplasm via plasmodesmata", "That is the symplast pathway."), ("From vacuole to vacuole across membranes", "That is the vacuolar pathway."), ("Only through the xylem vessels", "The xylem carries water up the plant; the apoplast is a route across the root cortex.")],
      [("Pathways", "Apoplast: walls and intercellular spaces. Symplast: cytoplasm connected by plasmodesmata.")], "Apoplast pathway", "Recall", "Apo means outside the cell."),
    Q("Which property of water molecules is most important for the unbroken column of water in the xylem?", "Cohesion between water molecules due to hydrogen bonds",
      [("Water is a good solvent", "A good solvent is useful for transport but does not keep the column unbroken."), ("Water has a high specific heat capacity", "That helps temperature control, not the column."), ("Water is denser than air", "Density is not the cause of the cohesive column.")],
      [("Cohesion", "Hydrogen bonds hold the water molecules together so the column can be pulled up under tension without breaking.")],
      "Cohesion-tension", "Concept", "What holds water molecules together?"),
    Q("Which observation provides evidence that the xylem is under tension?", "The diameter of a tree trunk decreases slightly during the day",
      [("Sugars accumulate above a ring of bark", "That is evidence for phloem transport."), ("Radioactive carbon moves down the stem", "That is evidence for translocation in the phloem."), ("Aphid stylets exude sap", "That shows the pressure in the phloem sieve tubes.")],
      [("Evidence", "In the day the strong pull in the xylem narrows the trunk. At night, when transpiration is low, the trunk widens again.")],
      "Evidence for tension", "Reasoning", "Which tissue is the question about?"),
    N("In a potometer the capillary tube has a radius of 0.4 mm. The air bubble moves 25 mm in 5 minutes. Calculate the rate of water uptake in mm³ per minute (use V = πr²d).", 2.5,
      [("Volume", "π × 0.4² × 25 = 12.57 mm³."), ("Rate", "12.57 ÷ 5 = 2.51 mm³ per minute.")],
      "Potometer calculation", "Calculation", "Volume = πr²d, then divide by the time.", tol=0.05, unit="mm³ per minute"),
    Q("Which change would decrease the rate of transpiration the most?", "An increase in the humidity of the air",
      [("An increase in light intensity", "Light opens stomata and raises transpiration."), ("An increase in wind speed", "Wind removes the humid air next to the leaf and raises transpiration."), ("An increase in air temperature", "A higher temperature increases evaporation.")],
      [("Gradient", "In humid air the water potential gradient between leaf and air is smaller, so less water vapour diffuses out.")],
      "Factors affecting transpiration", "Application", "Which factor makes the air outside the leaf closer to the air inside?"),
]
SETS.append(practice_set(module=M_GAS, topic=T_WATER, title="Water potential, root pathways and transpiration", lesson="bil3-water-transport-plants", questions=build(V6, 106)))

# ------------------------------------------------------------------ 7. Phloem transport
V7 = [
    Q("Which feature of a sieve tube element helps the flow of sap?", "Perforated end walls (sieve plates) and very little cytoplasm",
      [("A large nucleus", "Sieve tube elements have no nucleus."), ("A thick lignified wall", "Lignified walls are found in xylem."), ("Solid cross walls", "Perforated sieve plates allow flow.")],
      [("Structure", "Sieve tube elements have sieve plates and little cytoplasm so that sap flows through with little obstruction.")], "Sieve tube structure", "Recall", "What blocks flow in a pipe?"),
    Q("What is the role of the companion cell?", "It supplies ATP and carries out the metabolism for the sieve tube element, including loading sucrose",
      [("It transports water through the xylem", "Companion cells are in the phloem."), ("It stores starch for the plant", "Starch storage is in other tissues."), ("It makes the sieve plates", "The sieve plates are part of the sieve tube element wall.")],
      [("Partnership", "The sieve tube has no nucleus. The companion cell has a nucleus and many mitochondria, so it provides ATP and the active loading.")], "Companion cell", "Recall", "What does a sieve tube element lack?"),
    Q("Which of the following is a sink for sucrose?", "A growing root tip",
      [("A fully expanded leaf in bright light", "That is a source."), ("A xylem vessel", "The xylem carries water."), ("A guard cell", "A guard cell is not a store or user of sucrose in the way a root or fruit is.")],
      [("Definition", "A sink is where sucrose is removed for use or storage: roots, growing shoots, fruits and seeds.")], "Source and sink", "Concept", "Which tissue uses sugar without making it?"),
    Q("According to the mass flow hypothesis, what drives the flow of sap in the phloem?", "A hydrostatic pressure gradient from source to sink",
      [("Transpiration pull", "That moves water in the xylem."), ("Root pressure", "That affects the xylem, not the movement of sucrose in the phloem."), ("Diffusion of sucrose down a concentration gradient", "Diffusion is far too slow over the distances involved.")],
      [("Mass flow", "Active loading lowers the water potential, water enters, and the high pressure at the source pushes the sap towards the low pressure at the sink.")],
      "Mass flow hypothesis", "Concept", "What do the loading of sucrose and the entry of water create at the source?"),
    Q("A ring of bark is removed from a stem. After some days, what is seen above the ring?", "The stem swells because sucrose from the leaves accumulates",
      [("The stem above the ring shrinks", "The sugar is blocked from moving down and builds up above the ring."), ("Water stops reaching the leaves immediately", "The xylem is intact for some time, so water continues to move."), ("Nothing, as the xylem carries sugar", "The phloem, in the bark, carries sucrose.")],
      [("Ringing", "The phloem in the bark is removed, so sugars accumulate above the cut and the tissues swell.")], "Ringing experiment", "Application", "Which tissue is removed with the bark?"),
    N("Radioactive carbon is detected 45 cm below a leaf 30 minutes after the leaf was supplied with 14CO₂. Calculate the rate of movement in cm per hour.", 90,
      [("Rate per minute", "45 ÷ 30 = 1.5 cm per minute."), ("Per hour", "1.5 × 60 = 90 cm per hour.")],
      "Rate of translocation", "Calculation", "Change 30 minutes to hours.", tol=1, unit="cm per hour"),
    Q("Translocation stops when a respiratory poison is applied to the phloem. What does this suggest?", "Active (ATP-requiring) processes are involved, such as loading sucrose",
      [("Translocation is by diffusion only", "A poison of respiration would not stop diffusion."), ("The xylem is the route for sucrose", "The experiment is about the phloem."), ("Sucrose is made in the roots", "It is made in the leaves by photosynthesis.")],
      [("Inference", "If stopping ATP production stops flow, then ATP is needed, probably for the loading of sucrose into the companion cells and sieve tubes.")],
      "Metabolic inhibitors", "Reasoning", "What does a respiratory poison stop the cells making?"),
    Q("Why does the loading of sucrose into a sieve tube cause water to enter it?", "Sucrose lowers the water potential of the sieve tube, so water enters from the xylem by osmosis",
      [("Sucrose raises the water potential of the sieve tube", "Dissolved solutes lower water potential."), ("Water is pumped into the sieve tube by the companion cell", "Water moves by osmosis, not active transport."), ("Sucrose makes the sieve tube wall more permeable", "The movement of water is the result of the water potential difference.")],
      [("Osmosis", "A solution with more sucrose has a lower (more negative) water potential. Water moves from the xylem, which has a higher water potential, into the sieve tube.")],
      "Loading and water potential", "Reasoning", "Which has a lower water potential: sugary sap or pure water?"),
]
SETS.append(practice_set(module=M_GAS, topic=T_PHLO, title="Phloem structure, translocation and mass flow", lesson="bil3-phloem-mass-flow", questions=build(V7, 107)))

# ------------------------------------------------------------------ 8. Energy flow and productivity
V8 = [
    N("A forest has a gross primary productivity of 18 000 kJ m⁻² year⁻¹ and plant respiration of 7 000 kJ m⁻² year⁻¹. Calculate the net primary productivity in kJ m⁻² year⁻¹.", 11000,
      [("Formula", "NPP = GPP − R."), ("Calculate", "18 000 − 7 000 = 11 000 kJ m⁻² year⁻¹.")],
      "Net primary productivity", "Calculation", "Subtract the plants' own respiration.", tol=10, unit="kJ m⁻² year⁻¹"),
    Q("Which statement about the flow of energy and the cycling of matter in an ecosystem is correct?", "Energy flows in one direction and is lost as heat, while matter such as carbon is recycled",
      [("Energy is recycled between decomposers and producers", "Energy cannot be recycled; it is lost as heat."), ("Matter flows in one direction and is lost as heat", "Heat is energy; matter is recycled."), ("Both energy and matter flow in one direction", "Matter is recycled by decomposers.")],
      [("Contrast", "Energy enters as sunlight and leaves as heat. Atoms of carbon, nitrogen and so on are used again and again.")], "Energy flow and matter cycling", "Concept", "Which of the two can be recycled?"),
    Q("Why are most food chains limited to four or five trophic levels?", "Energy is lost at each level, so too little is left to support more levels",
      [("Predators at the top are too large", "Size is not the cause."), ("Decomposers use all the energy at the base", "Decomposers use dead material from all levels."), ("Producers contain less energy than consumers", "Producers contain the most energy.")],
      [("Losses", "At each transfer only about 10% is passed on. After four or five steps the energy is too small to support another population.")],
      "Length of food chains", "Concept", "How much energy is passed on at each transfer?"),
    N("The net primary productivity of a lake is 9 000 kJ m⁻² year⁻¹. The herbivorous fish gain 810 kJ m⁻² year⁻¹. Calculate the efficiency of energy transfer from producers to herbivores as a percentage.", 9,
      [("Formula", "Efficiency = energy gained by herbivores ÷ NPP × 100."), ("Calculate", "810 ÷ 9 000 × 100 = 9%.")],
      "Efficiency of energy transfer", "Calculation", "Divide the energy in the higher level by the energy in the lower level.", tol=0.1, unit="%"),
    Q("Which of the following is a reason why not all the energy eaten by a herbivore is available to the carnivore that eats it?", "Part of the food is egested in faeces and part is lost as heat in respiration",
      [("The herbivore stores all energy as heat", "Respiration loses heat, but much is also stored in growth and offspring."), ("Carnivores digest only plant material", "Carnivores digest animal tissue."), ("Decomposers prevent the energy from being used", "Decomposers use only the dead matter, faeces and waste.")],
      [("Losses", "Faeces, respiration, excretion and uneaten parts all take energy from the transfer.")], "Energy losses", "Concept", "Where does the energy go that is not stored in the herbivore's body?"),
    N("A cow takes in 600 kJ of grass energy per unit area, loses 200 kJ in faeces and 320 kJ in respiration. Calculate its net production in kJ (assimilation − respiration).", 80,
      [("Assimilation", "600 − 200 = 400 kJ."), ("Net production", "400 − 320 = 80 kJ.")],
      "Net production of a consumer", "Calculation", "First find the energy assimilated.", tol=1, unit="kJ"),
    Q("Why is a pyramid of energy never inverted?", "Energy is lost at each transfer, so each level contains less than the level below",
      [("Large animals need more energy than small animals", "Body size does not affect the shape of the energy pyramid."), ("Producers use up all the energy", "Producers pass on about a tenth of their net production."), ("Decomposers add energy to the top level", "Decomposers do not add energy to the top.")],
      [("Losses", "A level cannot contain more energy than it receives; energy lost as heat is not available to the next level.")], "Pyramids of energy", "Concept", "What happens to energy at every transfer?"),
    Q("Why can a given area of land feed more people if they eat crops rather than meat from animals fed on those crops?", "Less energy is lost, because people feed at a lower trophic level",
      [("Plants contain more protein than meat", "Meat is generally richer in protein; the issue is energy transfer."), ("Animals do not respire", "Animals respire and lose energy as heat."), ("Crops have no cell walls", "Plant cell walls do not explain the difference.")],
      [("Trophic level", "Each trophic level passes on about 10% of the energy. Eating plants directly avoids one transfer and its large losses.")], "Trophic level and food production", "Application", "How many energy transfers occur in each case?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_ENER, title="Energy flow, productivity and efficiency", lesson="bil3-energy-flow-productivity", questions=build(V8, 108)))

# ------------------------------------------------------------------ 9. Biogeochemical cycles
V9 = [
    Q("Which process in the nitrogen cycle converts nitrogen gas into ammonium?", "Nitrogen fixation",
      [("Nitrification", "Nitrification converts ammonium to nitrite and then nitrate."), ("Denitrification", "Denitrification converts nitrate to nitrogen gas, the reverse direction."), ("Ammonification", "Ammonification releases ammonium from dead organic matter.")],
      [("Process", "Fixation turns atmospheric N₂ into ammonium, by bacteria such as Rhizobium and Azotobacter.")], "Nitrogen fixation", "Recall", "N₂ is the starting substance."),
    Q("Where do Rhizobium bacteria live?", "In nodules on the roots of legumes such as groundnut and cowpea",
      [("In the leaves of maize", "Rhizobium nodulates legumes, not maize."), ("In waterlogged soil, converting nitrate to nitrogen gas", "That describes denitrifying bacteria."), ("In the intestines of herbivores", "They are soil bacteria associated with legume roots.")],
      [("Mutualism", "The bacteria get carbohydrate from the plant and give it ammonium.")], "Rhizobium", "Recall", "Which family of plants do farmers rotate with maize?"),
    Q("Which bacteria convert nitrite into nitrate?", "Nitrobacter",
      [("Nitrosomonas", "It converts ammonium to nitrite."), ("Rhizobium", "It fixes nitrogen gas."), ("Pseudomonas denitrificans", "It converts nitrate to nitrogen gas.")],
      [("Two steps", "Nitrosomonas: ammonium to nitrite. Nitrobacter: nitrite to nitrate.")], "Nitrification", "Recall", "It is the second step of nitrification."),
    Q("Under which condition does denitrification occur most?", "In waterlogged soil with little oxygen",
      [("In well-aerated soil", "Nitrification needs oxygen; denitrifying bacteria work without oxygen."), ("In dry sandy soil", "Dry sandy soil is well aerated and not favourable to denitrifying bacteria."), ("In the root nodules of legumes", "Nodules are where nitrogen fixation takes place.")],
      [("Anaerobic", "Denitrifying bacteria use nitrate instead of oxygen in respiration, so they act when oxygen is scarce.")], "Denitrification", "Concept", "Which gas is scarce when soil is waterlogged?"),
    Q("What is the role of decomposers in the nitrogen cycle?", "They convert nitrogen compounds in dead organisms and waste into ammonium",
      [("They convert nitrogen gas into nitrate", "That requires fixation and nitrification."), ("They absorb nitrate through roots", "That is done by plants."), ("They convert nitrate into nitrogen gas", "That is denitrification.")],
      [("Ammonification", "Saprophytic bacteria and fungi break down proteins and urea and release ammonium.")], "Ammonification", "Recall", "What do decomposers feed on?"),
    Q("Which of the following removes carbon dioxide from the atmosphere?", "Photosynthesis in the leaves of plants",
      [("Respiration of decomposers", "Respiration releases CO₂."), ("Burning of wood", "Combustion releases CO₂."), ("Respiration of animals", "That releases CO₂.")],
      [("Carbon cycle", "Photosynthesis uses CO₂ and fixes it into organic compounds.")], "Carbon cycle", "Recall", "Which process uses CO₂?"),
    Q("Why is the phosphorus cycle different from the carbon and nitrogen cycles?", "It has no significant gas phase in the atmosphere",
      [("Phosphorus is not needed by living things", "Phosphorus is in DNA, ATP and cell membranes."), ("Phosphorus is returned to the soil quickly from rock", "The weathering of rock is very slow."), ("Bacteria do not take part", "Decomposers return phosphate from dead matter.")],
      [("Phosphate", "Phosphorus moves as phosphate in rock, soil, water and organisms rather than as a gas.")], "Phosphorus cycle", "Concept", "How does phosphorus pass from rocks to plants?"),
    Q("A farmer grows groundnuts in one season and maize in the next. Which explanation best describes why the maize grows better?", "Rhizobium in the groundnut roots fixed nitrogen, so more nitrate is available to the maize",
      [("Groundnuts add phosphorus to the air", "Phosphorus has no gas stage in the cycle."), ("Groundnut roots remove all the nitrate", "They take up nitrate but the bacteria add more nitrogen than the plant removes."), ("Maize fixes its own nitrogen", "Maize is not a legume and does not fix nitrogen.")],
      [("Rotation", "Rhizobium fixes nitrogen. When the groundnut residues decay, ammonification and nitrification provide nitrate for the maize.")],
      "Crop rotation", "Application", "Which bacteria live in the root nodules?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_CYC, title="The carbon, nitrogen and phosphorus cycles", lesson="bil3-biogeochemical-cycles", questions=build(V9, 109)))

# ------------------------------------------------------------------ 10. Ecological succession
V10 = [
    Q("What is a pioneer species?", "One of the first species to colonise a bare area",
      [("A species that is present in the climax community", "That is a climax species."), ("A predator at the top of a food chain", "Feeding position does not define a pioneer."), ("A species that lives only in soil", "Pioneers may colonise bare rock where there is no soil.")],
      [("Definition", "Pioneers, such as lichens and mosses on rock, are the first colonisers.")], "Pioneer species", "Recall", "Pioneer means first."),
    Q("Which of the following is an example of primary succession?", "Colonisation of a new lava flow on a volcano",
      [("Regrowth of forest on an abandoned farm", "Soil remains, so it is secondary succession."), ("Regrowth on a burnt savanna", "Soil and seeds remain, so it is secondary."), ("Regrowth in a cleared garden", "Soil remains, so it is secondary.")],
      [("Starting point", "Primary succession begins where there is no soil, such as bare rock from a volcano.")], "Primary succession", "Concept", "Where is there no soil to begin with?"),
    Q("Why is secondary succession faster than primary succession?", "Soil, seeds and roots are already present",
      [("There are no herbivores to slow it", "Herbivores are present in both cases."), ("The climate is warmer in secondary succession", "Climate is not the reason."), ("Pioneer species are absent", "Pioneers may still be needed in some cases, but the soil is the main difference.")],
      [("Soil", "In primary succession the soil must first be formed by weathering and the decay of the first colonisers; in secondary succession it exists.")],
      "Rate of succession", "Concept", "What is missing at the start of primary succession?"),
    Q("Which change in the soil occurs as succession proceeds?", "Its depth, humus and water-holding capacity increase",
      [("It becomes shallower", "Soil forms and deepens."), ("It loses all organic matter", "Organic matter increases as plants die and decay."), ("Its mineral content falls to zero", "Minerals are recycled and increase in availability.")],
      [("Soil formation", "Dead plants decay to humus, roots break up the rock and the soil deepens, holding more water and minerals.")], "Changes in soil", "Concept", "What happens when pioneer plants die?"),
    Q("In a climax rainforest, the net primary productivity is close to zero. Why?", "Gross productivity is about equal to the respiration of the community",
      [("The plants no longer photosynthesise", "Photosynthesis continues at a high rate."), ("The soil contains no nutrients", "Soil nutrients are plentiful."), ("The community has no producers", "Producers are the main component.")],
      [("Balance", "NPP = GPP − R. In a climax community GPP is about equal to R, so biomass no longer increases.")], "Productivity in a climax community", "Concept", "NPP = GPP − R."),
    N("A succession has 20 plant species at 30 years and 45 species at 100 years. Calculate the average rate of increase in the number of species per year (to 2 decimal places).", 0.36,
      [("Increase", "45 − 20 = 25 species."), ("Time", "100 − 30 = 70 years."), ("Rate", "25 ÷ 70 = 0.357, or 0.36 species per year.")],
      "Rate of change in a succession", "Calculation", "Divide the change in species by the change in time.", tol=0.01, unit="species per year"),
    Q("A savanna is burned every dry season and never develops into woodland. What term describes the resulting community?", "Plagioclimax",
      [("Climax community", "A natural climax would be woodland in many areas."), ("Pioneer community", "A pioneer community is the first stage after a bare surface formed."), ("Primary succession", "The soil is already present.")],
      [("Disturbance", "A human-maintained stage that stops succession reaching the natural climax is a plagioclimax.")], "Plagioclimax", "Application", "Which term describes a stage held by repeated disturbance?"),
    Q("Which statement about facilitation in succession is correct?", "Each seral stage changes the environment so that it suits the next stage better",
      [("Each stage makes conditions worse for its successors", "That is inhibition, and it is not the general rule."), ("Only the climax species change the environment", "All stages modify the soil and light."), ("It occurs only in primary succession", "It occurs in both.")],
      [("Modification", "Pioneers build soil and add shade and nutrients, allowing larger plants to establish and replace them.")], "Facilitation", "Concept", "How do lichens help mosses?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_SUCC, title="Primary and secondary succession and the climax community", lesson="bil3-ecological-succession", questions=build(V10, 110)))

# ------------------------------------------------------------------ 11. Population dynamics
LG = "al-bil3-logistic.svg"
LG_ALT = "S-shaped logistic population curve levelling off at a carrying capacity of 1000, with a dashed exponential curve rising above it"
V11 = [
    Q("What is the carrying capacity of an environment?", "The maximum population size that the environment can support over a long time",
      [("The number of individuals born in a year", "That is natality."), ("The maximum size a single individual can reach", "It refers to the population, not the individual."), ("The number of species in the area", "That is species richness.")],
      [("Definition", "Carrying capacity depends on the resources: food, water and space.")], "Carrying capacity", "Recall", "It is the limit set by the environment."),
    Q("Which of the following is a density-dependent factor?", "Competition for food",
      [("A flood", "A flood kills regardless of density."), ("A forest fire", "Fire is density-independent."), ("A cold night", "Frost affects all individuals regardless of density.")],
      [("Definition", "Competition, predation and disease have effects that increase as the population becomes denser.")], "Density-dependent factors", "Concept", "Which factor gets worse when there are more individuals?"),
    Q("In the figure, the solid curve shows logistic growth. At about which population size is the growth rate greatest?", "About 500, half of the carrying capacity",
      [("About 50, at the start", "Growth at the start is slow because there are few parents."), ("About 1000, at the carrying capacity", "The growth rate is zero at K."), ("About 900, near the top", "Growth has slowed by then because of resistance.")],
      [("Slope", "The slope of the curve is greatest at the point of inflection, at N = K ÷ 2.")], "Logistic curve", "Interpretation", "Where is the curve steepest?", diagram=LG, alt=LG_ALT),
    N("In a capture-recapture study of fish, 50 were marked and released. A second sample of 40 fish contained 8 marked fish. Estimate the population size.", 250,
      [("Formula", "N = M × C ÷ R."), ("Calculate", "50 × 40 ÷ 8 = 250 fish.")],
      "Capture-recapture", "Calculation", "N = (number marked × second sample) ÷ number recaptured with marks.", tol=1, unit="fish"),
    Q("Which of the following describes an r-strategist?", "A small organism that matures early and produces many offspring with little parental care",
      [("A large organism that produces a few young and cares for them", "That is a K-strategist."), ("An organism that lives close to the carrying capacity in stable habitats", "That is typical of K-strategists."), ("An organism that never reproduces", "Every strategy involves reproduction.")],
      [("Strategies", "r-strategists (such as insects and weeds) reproduce quickly in unstable habitats.")], "r- and K-strategists", "Recall", "Which strategy gives many offspring?"),
    Q("In predator-prey cycles, why does the predator population peak after the prey population?", "The predators need time to reproduce in response to the increase in prey",
      [("Predators are always larger than prey", "Size does not explain the delay."), ("The prey population is always controlled by disease", "The cycle is explained by the predator-prey interaction."), ("Predators eat all the prey at once", "Predators cannot remove all the prey instantly.")],
      [("Time lag", "More prey gives more food, but predators take time to breed. Then the larger predator population reduces the prey again.")], "Predator-prey cycles", "Reasoning", "What delays the rise in the predator numbers?"),
    N("A population has r = 0.4 per generation and a carrying capacity K of 800. Calculate the growth rate dN/dt when N = 200, using dN/dt = rN(K − N)/K.", 60,
      [("Substitute", "0.4 × 200 × (800 − 200) ÷ 800."), ("Calculate", "0.4 × 200 = 80; 80 × 600 ÷ 800 = 60 individuals per generation.")],
      "Logistic growth rate", "Calculation", "Work out (K − N) ÷ K first.", tol=0.5, unit="individuals per generation"),
    Q("Two species of Paramecium grown together in one tube compete for the same food and one species eventually disappears. Which principle does this illustrate?", "The competitive exclusion principle",
      [("The carrying capacity principle", "Carrying capacity is the population limit for one species."), ("Succession", "Succession is a change in the community over time."), ("Biomagnification", "That is the build-up of a toxin in a food chain.")],
      [("Gause", "Two species with identical niches cannot coexist for long: one outcompetes the other.")], "Competitive exclusion", "Concept", "What happens when two species need exactly the same resource?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_POP, title="Population growth, limiting factors and predator-prey cycles", lesson="bil3-population-dynamics", questions=build(V11, 111)))

# ------------------------------------------------------------------ 12. Biodiversity indices
V12 = [
    Q("What does species richness measure?", "The number of different species in a community",
      [("The total number of individuals", "That is abundance."), ("How equally the individuals are spread among the species", "That is evenness."), ("The size of the largest species", "Size is not part of richness.")],
      [("Definition", "Richness is a count of species, ignoring the number of individuals of each.")], "Species richness", "Recall", "It counts only species."),
    N("A sample contains two species with 8 and 2 individuals. Calculate Simpson's index D = N(N − 1) ÷ Σn(n − 1) to 2 decimal places.", 1.55,
      [("N", "N = 8 + 2 = 10, so N(N − 1) = 90."), ("Σn(n−1)", "8 × 7 + 2 × 1 = 56 + 2 = 58."), ("D", "90 ÷ 58 = 1.55.")],
      "Simpson's index", "Calculation", "First work out n(n − 1) for each species.", tol=0.01),
    Q("Why should quadrats be placed at random coordinates?", "To avoid bias from the investigator choosing where to sample",
      [("To find as many species as possible", "Random placement does not aim to find more species."), ("To make sure all quadrats have the same number of plants", "Numbers differ naturally."), ("To cover the whole field", "A sample covers only part of the field.")],
      [("Random sampling", "Random placement gives every part of the area an equal chance of being sampled, so the results are not biased.")], "Random sampling", "Concept", "What does a student tend to do if allowed to choose?"),
    Q("Site P has 5 species and site Q has 5 species. In site P, one species makes up 95% of the individuals. In site Q, the individuals are shared equally. Which statement is correct?", "Site Q has the greater diversity because the evenness is greater",
      [("They have the same diversity because the richness is the same", "Diversity also depends on evenness."), ("Site P has the greater diversity because it has a dominant species", "Dominance by one species lowers diversity."), ("Diversity cannot be compared without a third site", "Two sites can be compared directly.")],
      [("Evenness", "The index takes into account both richness and evenness. Site Q is more even, so its index is higher.")], "Richness and evenness", "Reasoning", "Which site is dominated by one species?"),
    N("A sample has four species with 5 individuals each. Calculate Simpson's index D = N(N − 1) ÷ Σn(n − 1) to 2 decimal places.", 4.75,
      [("N", "N = 20, so N(N − 1) = 380."), ("Σn(n−1)", "4 × (5 × 4) = 80."), ("D", "380 ÷ 80 = 4.75.")],
      "Simpson's index", "Calculation", "Each species gives 5 × 4 = 20.", tol=0.01),
    Q("A river sample contains mainly bloodworms and sludge worms, with no mayfly or stonefly larvae. What does this suggest?", "The river is heavily polluted with organic matter and has low oxygen",
      [("The river is clean and rich in oxygen", "Mayfly and stonefly larvae would be expected in clean water."), ("The river has a high species diversity", "Only a few tolerant species are present."), ("The river is acidic only", "The pattern points to oxygen shortage from organic pollution.")],
      [("Indicator species", "Mayflies and stoneflies need clean, oxygen-rich water. Bloodworms tolerate low oxygen.")], "Indicator species", "Application", "Which animals need clean water?"),
    Q("Which of the following is a threat to biodiversity caused by human activity?", "Clearing forest for farming and fragmenting the habitat",
      [("The natural succession of a field to woodland", "Succession is a natural process."), ("The seasonal growth of grass", "This is a natural cycle."), ("Photosynthesis by plants", "Photosynthesis is not a threat.")],
      [("Threats", "Habitat loss and fragmentation reduce populations and may cause extinctions.")], "Threats to biodiversity", "Concept", "Which option is caused by people?"),
    Q("Why is a high Simpson's index usually taken to indicate a more stable ecosystem?", "It indicates many species with similar numbers, so there are many food webs and niches",
      [("It shows that one species is dominant", "Dominance gives a low index."), ("It shows there are only a few species", "That gives a low index."), ("It shows that the ecosystem is polluted", "Pollution generally lowers the index.")],
      [("Stability", "Many species with balanced numbers provide alternative food sources and functions, so one disturbance is less damaging.")], "Meaning of a high index", "Reasoning", "What does a high index say about richness and evenness?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_BDIV, title="Species richness, evenness and Simpson's index", lesson="bil3-biodiversity-indices", questions=build(V12, 112)))

# ------------------------------------------------------------------ 13. Pollution and conservation
V13 = [
    Q("Which pollutants mainly cause the eutrophication of a lake?", "Nitrates and phosphates from fertilisers and sewage",
      [("Carbon monoxide from vehicles", "Carbon monoxide is an air pollutant and does not cause eutrophication."), ("Sulphur dioxide from factories", "That causes acid rain."), ("Plastic bags", "Plastic harms animals but does not enrich the water with nutrients.")],
      [("Nutrients", "Nitrates and phosphates stimulate the growth of algae.")], "Cause of eutrophication", "Recall", "Which nutrients are in fertiliser?"),
    Q("What does a high biochemical oxygen demand (BOD) in a water sample indicate?", "A large amount of organic matter that microorganisms are decomposing, using up oxygen",
      [("A high concentration of dissolved oxygen", "BOD measures oxygen used, not oxygen available."), ("A very low temperature", "Temperature is not measured by BOD."), ("An absence of microorganisms", "A high BOD means many microorganisms.")],
      [("Definition", "BOD is the oxygen taken up by microbes in a water sample in a set time. More organic matter means a higher BOD.")], "BOD", "Concept", "Think about what bacteria need to decompose organic matter."),
    Q("In a eutrophic lake, why do fish die?", "Bacteria that decompose the dead algae use up the dissolved oxygen",
      [("Algae release poisons that are always lethal", "Some blooms release toxins, but the main cause is oxygen shortage."), ("The water becomes too cold", "Temperature is not the main factor."), ("There is too much light for photosynthesis", "A bloom actually blocks light.")],
      [("Sequence", "Nutrients, bloom, light blocked, plants die, decomposition, high BOD, oxygen shortage, fish die.")], "Eutrophication sequence", "Concept", "What do aerobic decomposers need?"),
    N("In a food chain the concentration of a pesticide is 0.5 ppm in small fish and 25 ppm in a fish-eating bird. By what factor has the concentration increased?", 50,
      [("Divide", "25 ÷ 0.5 = 50, so the concentration in the bird is 50 times higher.")],
      "Biomagnification factor", "Calculation", "Divide the higher concentration by the lower concentration.", tol=0.5),
    Q("The question asks for the EFFECTS of excessive noise on people living in a large town. Which answer is correct?", "Hearing loss, stress, raised blood pressure and disturbed sleep",
      [("Noise from markets, bars and traffic", "These are sources of noise, not effects."), ("Noise from generators and loudspeakers", "These are sources."), ("The decibel scale and its units", "These are about measurement, not effects.")],
      [("Read the command word", "Effects are what the noise does to people, such as hearing loss, stress, high blood pressure and sleeplessness.")], "Effects of noise pollution", "Application", "An effect is something that happens to people."),
    Q("Which of the following is an example of in-situ conservation?", "Protecting forest elephants in a national park",
      [("Storing seeds in a seed bank", "That is ex-situ."), ("Breeding endangered birds in a zoo", "That is ex-situ."), ("Growing rare plants in a botanic garden", "That is ex-situ.")],
      [("In situ", "In-situ conservation protects species in their natural habitat.")], "In-situ conservation", "Recall", "In situ means in place."),
    Q("Which gases are the main cause of acid rain?", "Sulphur dioxide and nitrogen oxides",
      [("Carbon dioxide and methane", "These are the main greenhouse gases."), ("Oxygen and nitrogen", "These are the main gases in air and are not pollutants."), ("Ammonia and phosphate", "These contribute to eutrophication rather than acid rain.")],
      [("Acid rain", "SO₂ and NOₓ dissolve in rain water to form acids, which lowers the pH.")], "Acid rain", "Recall", "Which gases come from burning fuel?"),
    Q("Why is the involvement of local communities important for the success of a protected area?", "People who benefit from the area are more likely to protect it and not hunt or clear it illegally",
      [("It removes the need for any laws", "Laws are still needed."), ("It allows unlimited hunting", "Unlimited hunting would destroy the species."), ("It makes ex-situ conservation unnecessary", "The two approaches complement each other.")],
      [("Sustainability", "If neighbours have jobs, income or resources from the area, they have a reason to conserve it.")], "Sustainable use and communities", "Application", "What do people near a park need to gain?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_BDIV, title="Pollution, biomagnification and conservation", lesson="bil3-pollution-conservation", questions=build(V13, 113)))

# ------------------------------------------------------------------ Examination: Paper 1 technique
X1 = [
    Q("Before looking at the four options of a multiple-choice question, a good candidate should:", "Read the stem and predict the answer",
      [("Choose the longest option", "Length does not show that an option is correct."), ("Look for the options with the word 'always'", "Absolute words are often wrong, but you still have to check the facts."), ("Skip the stem and read the options", "The stem tells you what is being asked.")],
      [("Routine", "Read, predict, eliminate and check: predicting protects you from persuasive wrong options.")], "MCQ routine", "Recall", "What do you do first?"),
    Q("A stem asks: 'Which statement about the cardiac cycle is NOT correct?' You should:", "Test each option and choose the one that is false",
      [("Choose the first true statement", "In a NOT question the answer is the false statement."), ("Choose the statement with the most technical terms", "Technical words do not show falsehood."), ("Leave it blank", "A blank cannot score.")],
      [("Read the command", "In a NOT or EXCEPT question you hunt for the false option.")], "NOT questions", "Concept", "What are you looking for?"),
    N("A heart has an end-diastolic volume of 130 cm³ and an end-systolic volume of 55 cm³, at 80 beats per minute. What is the cardiac output in cm³ per minute?", 6000,
      [("Stroke volume", "130 − 55 = 75 cm³."), ("Output", "75 × 80 = 6000 cm³ per minute.")],
      "Calculation questions", "Calculation", "Find the stroke volume first.", tol=5, unit="cm³ per minute"),
    N("The net primary productivity of a grassland is 4 500 kJ m⁻² year⁻¹ and the primary consumers gain 540 kJ m⁻² year⁻¹. Calculate the efficiency of energy transfer as a percentage.", 12,
      [("Formula", "540 ÷ 4 500 × 100 = 12%.")],
      "Calculation questions", "Calculation", "Efficiency = energy in the higher level ÷ energy in the lower level × 100.", tol=0.2, unit="%"),
    N("A pipette has an uncertainty of ±0.1 cm³ and is used to measure 5.0 cm³. Calculate the percentage uncertainty.", 2,
      [("Formula", "0.1 ÷ 5.0 × 100 = 2%.")],
      "Percentage uncertainty", "Calculation", "Divide the uncertainty by the measured value.", tol=0.05, unit="%"),
    Q("A calculation gives the stroke volume (75 cm³) instead of the cardiac output. Which type of wrong option is this?", "An unfinished calculation",
      [("A reversed answer", "A reversed answer has the opposite direction or sign."), ("An absolute word", "Absolute words are 'always' and 'never'."), ("A correct answer", "The question needs the cardiac output, not the stroke volume.")],
      [("Distractor", "Many wrong options are the result of stopping one step before the end of a calculation.")], "Distractors", "Concept", "Has every step been done?"),
    N("The KKEVO Paper 1 mock has 50 questions in 90 minutes. How many minutes are there for each question on average?", 1.8,
      [("Divide", "90 ÷ 50 = 1.8 minutes (1 minute 48 seconds).")],
      "Time per question", "Calculation", "Divide the total time by the number of questions.", tol=0.01, unit="minutes"),
    Q("Which module of the Lower Sixth course includes the oxygen dissociation curve, the cardiac cycle and the cohesion-tension theory?", "Gaseous Exchange & Mass Transport Systems",
      [("Ecology, Population Dynamics & Conservation", "That module covers energy, cycles, succession and populations."), ("Autotrophic & Heterotrophic Nutrition", "That module covers photosynthesis and digestion."), ("Cytology & Membrane Physiology", "That module covers cells, membranes and water potential.")],
      [("Revision map", "These topics belong to the sixth module, Gaseous Exchange & Mass Transport Systems.")], "Revision map", "Recall", "Which module is about transport in animals and plants?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Multiple-choice technique and calculations", lesson="bixl-paper1-multiple-choice", questions=build(X1, 121)))

# ------------------------------------------------------------------ Examination: Paper 2 technique
X2 = [
    Q("What does the command word 'explain' ask you to do?", "Give reasons: say how and why something happens",
      [("List facts without reasons", "That is 'state' or 'give'."), ("Say what happens, in order, without reasons", "That is 'describe'."), ("Give only the names of structures", "That is 'name' or 'label'.")],
      [("Command words", "Explain needs a reason, usually with 'because' or 'so'.")], "Command words", "Recall", "Which word needs reasons?"),
    Q("What should an annotation on a diagram include?", "A short note on both the structure and the function of the part",
      [("The name of the part only", "That is a label."), ("The function only", "The Board's report notes that candidates lost marks for stating only the function."), ("A second diagram", "One diagram is enough.")],
      [("Annotation", "Describe what the part is like and what it does.")], "Annotation", "Concept", "A label is not an annotation."),
    Q("A question asks for the functions of saliva and of hydrochloric acid in digestion. Which answer is best?", "Saliva moistens food and its amylase begins the digestion of starch; hydrochloric acid kills bacteria and gives the low pH that pepsin needs",
      [("The salivary glands and oxyntic cells digest food", "This describes the glands, not the secretions; the question asks about the secretions."), ("Saliva and acid are secretions of the stomach", "Saliva is not a secretion of the stomach and no function is given."), ("They are produced by the alimentary canal", "This describes the origin, not the function.")],
      [("Secretions", "Name the secretion and state what it does. Do not give the function of the gland.")], "Answer what is asked", "Application", "The question asks about the secretions."),
    Q("A question says: 'Describe the cardiac cycle.' Which opening is best?", "In atrial systole the atria contract; then the ventricles contract (ventricular systole), the AV valves close and the pressure rises until the semilunar valves open",
      [("Blood enters the right atrium from the vena cava and passes to the right ventricle", "This traces blood flow and does not describe the cycle."), ("The heart is a muscular organ with four chambers", "This is a description of the organ, not the cycle."), ("The heart beats about 75 times a minute", "This gives the rate, not the cycle.")],
      [("Systole and diastole", "The Board's 2023 report notes candidates traced blood flow. A good answer names systole and diastole, pressures and valves.")], "Cardiac cycle answer", "Application", "Which answer mentions contraction and valves?"),
    Q("A question asks for the EFFECTS of excessive noise on people in a town. Which answer earns the marks?", "Hearing loss, stress, high blood pressure and loss of sleep",
      [("Loud music from bars and markets", "This is a source."), ("Traffic and generators", "These are sources."), ("Noise measured in decibels", "This is about measurement.")],
      [("Read the question", "Effects are the results for people. Sources are where the noise comes from.")], "Effects, not sources", "Application", "What happens to the people?"),
    Q("A graph shows the haemoglobin saturation falling as CO₂ rises. Which answer to 'describe the trend' is best?", "The saturation falls from 70% to 45% as the CO₂ pressure rises from 2 to 8 kPa",
      [("The graph goes down", "This gives no data."), ("The haemoglobin releases more oxygen because of the Bohr effect", "This explains rather than describes, and quotes no values."), ("The saturation is 70%", "One value does not show a trend.")],
      [("Describe with data", "State the direction of change and quote two values with their units.")], "Describing a graph", "Interpretation", "Which answer has numbers and units?"),
    N("A table shows that haemoglobin saturation falls from 70% to 45% as the CO₂ pressure rises. By how many percentage points does it fall?", 25,
      [("Subtract", "70 − 45 = 25 percentage points.")], "Data calculation", "Calculation", "Subtract the smaller value from the larger.", tol=0.5, unit="percentage points"),
    Q("Which set of headings is the most complete plan for an essay on the nitrogen cycle?", "Fixation, ammonification, nitrification, denitrification and human effects",
      [("Photosynthesis, respiration and decay", "These are headings for the carbon cycle."), ("Eutrophication, acid rain and noise", "These are headings for pollution."), ("Transcription, translation and replication", "These are headings for protein synthesis.")],
      [("Plan", "An essay plan lists the processes in order with the organisms and changes, plus human effects.")], "Essay planning", "Application", "Which headings are the processes of the nitrogen cycle?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Command words, answers and essay planning", lesson="bixl-paper2-theory-essay", questions=build(X2, 122)))

# ------------------------------------------------------------------ Examination: Paper 3 practical skills
X3 = [
    N("A drawing of a cell is 45 mm long. The cell is actually 30 µm long. Calculate the magnification.", 1500,
      [("Convert", "45 mm = 45 000 µm."), ("Calculate", "45 000 ÷ 30 = ×1500.")], "Magnification", "Calculation", "Use the same units for both lengths.", tol=1),
    N("A drawing of a cell is 60 mm long at a magnification of ×400. Calculate the actual length of the cell in µm.", 150,
      [("Divide", "60 mm ÷ 400 = 0.15 mm."), ("Convert", "0.15 mm = 150 µm.")], "Actual size", "Calculation", "Actual size = image size ÷ magnification.", tol=0.5, unit="µm"),
    Q("What is the positive result of the Benedict's test for a reducing sugar?", "A brick-red precipitate after heating, passing through green, yellow and orange",
      [("A blue-black colour", "That is the iodine test for starch."), ("A violet colour", "That is the biuret test for protein."), ("A cloudy white emulsion", "That is the emulsion test for lipid.")],
      [("Colours", "Benedict's reagent is blue and changes to green, yellow, orange and brick red with more reducing sugar.")], "Benedict's test", "Recall", "Which test needs heating?"),
    Q("A sample is negative for reducing sugar. After boiling with dilute acid, neutralising and adding Benedict's reagent, it gives a brick-red colour. What does it contain?", "A non-reducing sugar such as sucrose",
      [("A reducing sugar such as glucose", "It would have given a positive result at the first test."), ("Starch", "Starch gives a blue-black colour with iodine."), ("Protein", "Protein is tested with the biuret test.")],
      [("Hydrolysis", "The acid breaks sucrose into glucose and fructose, which are reducing sugars.")], "Non-reducing sugar test", "Reasoning", "What does the acid do to sucrose?"),
    Q("Which control should be done for the Benedict's test?", "Repeat the test with distilled water instead of the sample",
      [("Repeat it with iodine", "Iodine is a different test."), ("Repeat it with more sample", "A control keeps the reagent but removes the sample."), ("Do the test without heating", "That changes the method.")],
      [("Control", "Water in place of the sample should stay blue, showing that the reagent gives no colour by itself.")], "Controls", "Concept", "A control has no sample in it."),
    Q("Which feature may be used in a dichotomous key for a specimen?", "The number of legs on the specimen",
      [("Whether it lays eggs", "This cannot be seen on a preserved specimen."), ("Whether it is cold-blooded", "This cannot be observed externally."), ("What it eats", "This is not visible on the specimen.")],
      [("Visible features", "The Board's report says keys must use external features that can be seen and counted.")], "Dichotomous keys", "Application", "Which feature can be counted on the specimen?"),
    N("Six seedlings have heights of 12, 14, 11, 15, 13 and 16 mm. Calculate the mean height in mm.", 13.5,
      [("Sum", "12 + 14 + 11 + 15 + 13 + 16 = 81."), ("Mean", "81 ÷ 6 = 13.5 mm.")], "Mean", "Calculation", "Add all the values and divide by the number of values.", tol=0.05, unit="mm"),
    N("A carrot strip falls in mass from 10.0 g to 8.8 g in a concentrated sugar solution. Calculate the percentage change in mass (give a negative value for a decrease).", -12,
      [("Change", "8.8 − 10.0 = −1.2 g."), ("Percentage", "−1.2 ÷ 10.0 × 100 = −12%.")], "Percentage change", "Calculation", "Divide the change by the original mass.", tol=0.2, unit="%"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Practical skills: drawings, tests, keys and data", lesson="bixl-paper3-practical-skills", questions=build(X3, 123)))

# ------------------------------------------------------------------ Paper 1 mock exam A (50 MC across all seven modules)
# Allocation by topic count: Cytology 6, Molecules 7, Nucleic acids 7, Biodiversity 7, Nutrition 7, Transport 9, Ecology 7.
P1 = [
    # ---- Cytology & Membrane Physiology (6)
    Q("Which feature is found in a bacterial cell but not in a typical animal cell?", "A cell wall containing peptidoglycan",
      [("Ribosomes", "Both bacteria and animal cells have ribosomes."), ("A cell surface membrane", "All cells have a surface membrane."), ("Cytoplasm containing enzymes", "All cells have cytoplasm with enzymes.")],
      [("Recall", "Bacteria have a cell wall of peptidoglycan; animal cells have no cell wall.")], T_PROK, "Recall", "Which structure do animal cells lack?"),
    Q("Which statement about ribosomes is correct?", "Prokaryotic ribosomes (70S) are smaller than the ribosomes in the cytoplasm of eukaryotic cells (80S)",
      [("Prokaryotes have no ribosomes", "Prokaryotes make proteins, so they have ribosomes."), ("Eukaryotic ribosomes in the cytoplasm are smaller than prokaryotic ribosomes", "The reverse is true."), ("Both types of cell have ribosomes of the same size", "They differ in size: 70S and 80S.")],
      [("Recall", "Prokaryotes have 70S ribosomes; eukaryotes have 80S ribosomes in the cytoplasm.")], T_PROK, "Recall", "Compare 70S with 80S."),
    Q("What is the role of cholesterol in the cell surface membrane of animal cells?", "It regulates the fluidity of the membrane, making it less fluid at high temperatures and less rigid at low temperatures",
      [("It forms channels for the movement of ions", "Channels are made of proteins."), ("It acts as an enzyme on the surface of the cell", "Cholesterol is a lipid and is not an enzyme."), ("It makes the membrane completely rigid", "It regulates fluidity; it does not make the membrane rigid.")],
      [("Function", "Cholesterol fits between phospholipids. It stops them from moving too much at high temperatures and from packing too tightly at low temperatures.")], T_FLUID, "Recall", "What does it do to the movement of phospholipids?"),
    Q("Why is the cell membrane described as a 'fluid mosaic'?", "Phospholipids and many proteins can move sideways, and the proteins are scattered through the bilayer like a mosaic",
      [("The membrane flows out of the cell", "The word fluid refers to the movement of molecules within the layer."), ("The membrane is a single layer of phospholipids", "It is a bilayer."), ("The proteins are fixed in position in a regular pattern", "The proteins are not fixed; they can move.")],
      [("Model", "Fluid refers to the movement of the phospholipids and proteins; mosaic to the scattered proteins.")], T_FLUID, "Concept", "What does fluid describe?"),
    Q("A plant cell has Ψs = −0.9 MPa and Ψp = +0.3 MPa. It is placed in a solution with Ψ = −0.4 MPa. What happens?", "Water enters the cell by osmosis",
      [("Water leaves the cell by osmosis", "The solution has the higher water potential (−0.4 compared with −0.6), so water enters."), ("There is no net movement of water", "The cell has Ψ = −0.6 MPa, which differs from −0.4 MPa."), ("The cell becomes plasmolysed", "Plasmolysis occurs if water leaves.")],
      [("Cell", "Ψ = −0.9 + 0.3 = −0.6 MPa."), ("Compare", "−0.4 is higher than −0.6, so water moves from the solution into the cell.")], T_WPOT, "Application", "Work out the water potential of the cell first."),
    Q("Which statement describes active transport?", "The movement of a substance against its concentration gradient using ATP and a carrier protein",
      [("The movement of a substance down its concentration gradient through a channel", "That describes facilitated diffusion."), ("The movement of water through a partially permeable membrane", "That describes osmosis."), ("The movement of a substance down a gradient with no protein", "That describes simple diffusion.")],
      [("Definition", "Active transport uses energy from ATP to move a substance against its gradient through a carrier.")], T_TRANS, "Recall", "Which process needs energy?"),
    # ---- Biological Molecules & Enzymology (7)
    Q("Which bond joins two monosaccharides in a disaccharide?", "A glycosidic bond formed by a condensation reaction",
      [("A peptide bond formed by condensation", "Peptide bonds join amino acids."), ("An ester bond formed by hydrolysis", "Ester bonds join fatty acids to glycerol, and hydrolysis breaks bonds."), ("A hydrogen bond formed by condensation", "Hydrogen bonds are weak attractions, not formed by condensation.")],
      [("Recall", "Two sugars join by a condensation reaction that removes water and forms a glycosidic bond.")], T_CARB, "Recall", "Which bond links sugar units?"),
    Q("Which description of cellulose is correct?", "Unbranched chains of β-glucose with alternate units inverted, held together in microfibrils by hydrogen bonds",
      [("Branched chains of α-glucose with 1,4 and 1,6 links", "That describes glycogen."), ("A helical chain of α-glucose", "That describes amylose."), ("A chain of fructose units", "Cellulose is made of glucose.")],
      [("Structure", "Cellulose chains are straight; hydrogen bonds between chains form strong microfibrils.")], T_CARB, "Recall", "Which isomer of glucose forms cellulose?"),
    Q("What is the structure of a triglyceride?", "One glycerol molecule joined to three fatty acids by ester bonds",
      [("Three glycerol molecules joined to one fatty acid", "It is one glycerol and three fatty acids."), ("One glycerol, two fatty acids and a phosphate group", "That is a phospholipid."), ("Three amino acids joined by peptide bonds", "That is a tripeptide.")],
      [("Structure", "A triglyceride is made by three condensation reactions between glycerol and fatty acids.")], T_LIP, "Recall", "What do 'tri' and 'glyceride' tell you?"),
    Q("What is the difference between a saturated and an unsaturated fatty acid?", "A saturated fatty acid has no carbon-carbon double bonds in its hydrocarbon chain",
      [("A saturated fatty acid has one double bond", "That is a monounsaturated fatty acid."), ("A saturated fatty acid contains no hydrogen", "It contains the maximum number of hydrogen atoms."), ("A saturated fatty acid has no carboxyl group", "Every fatty acid has a carboxyl group.")],
      [("Recall", "Saturated means all the carbon atoms are bonded to the maximum number of hydrogens, so there are no double bonds.")], T_LIP, "Recall", "Look at the C=C bonds."),
    Q("Which bonds hold the tertiary structure of a protein?", "Hydrogen bonds, ionic bonds, disulfide bridges and hydrophobic interactions between R groups",
      [("Peptide bonds between neighbouring amino acids", "These form the primary structure."), ("Hydrogen bonds between the C=O and N-H groups of the backbone only", "These give the secondary structure."), ("Glycosidic bonds between the amino acids", "Glycosidic bonds join sugars.")],
      [("Levels", "The tertiary structure is the 3D folding due to interactions between the R groups.")], T_PROT, "Recall", "Which part of an amino acid varies from one to another?"),
    Q("An enzyme has a Vmax of 20 µmol per minute. What is the reaction rate when the substrate concentration equals Km?", "10 µmol per minute",
      [("20 µmol per minute", "That is the maximum rate Vmax, not the rate at Km."), ("5 µmol per minute", "Km is the substrate concentration at half of Vmax, which is 10."), ("40 µmol per minute", "The rate cannot exceed Vmax.")],
      [("Definition", "Km is the substrate concentration at which the rate is Vmax ÷ 2 = 10 µmol per minute.")], T_ENZK, "Application", "Km corresponds to half Vmax."),
    Q("What is the effect of a competitive inhibitor on an enzyme-catalysed reaction?", "It increases the apparent Km and leaves Vmax unchanged",
      [("It decreases Vmax and leaves Km unchanged", "That is a non-competitive inhibitor."), ("It decreases the Km", "A competitive inhibitor makes the enzyme appear to have lower affinity, so Km is higher."), ("It increases Vmax", "Inhibitors do not increase Vmax.")],
      [("Mechanism", "The inhibitor competes with the substrate for the active site. A high substrate concentration overcomes it, so Vmax is the same.")], T_ENZI, "Concept", "Which inhibitor can be overcome by more substrate?"),
    # ---- Nucleic Acids, Protein Synthesis & Cell Division (7)
    Q("Which statement about base pairing in DNA is correct?", "Adenine pairs with thymine by two hydrogen bonds, and guanine pairs with cytosine by three",
      [("Adenine pairs with cytosine by three hydrogen bonds", "A pairs with T, not C."), ("Adenine pairs with guanine by two hydrogen bonds", "Two purines do not pair."), ("Thymine pairs with cytosine by two hydrogen bonds", "T pairs with A.")],
      [("Recall", "A–T has two hydrogen bonds and G–C has three.")], T_DNA, "Recall", "Which bases are complementary?"),
    Q("How does RNA differ from DNA?", "RNA contains ribose and uracil and is usually single-stranded",
      [("RNA contains deoxyribose and thymine", "That describes DNA."), ("RNA is double-stranded and contains uracil", "RNA is usually single-stranded."), ("RNA contains ribose and thymine", "RNA has uracil instead of thymine.")],
      [("Recall", "RNA has ribose sugar, uracil instead of thymine, and usually one strand.")], T_DNA, "Recall", "Which base is in RNA only?"),
    Q("Bacteria are grown for many generations in a medium containing 15N and then moved to a medium with 14N. What does the DNA show after one generation?", "All the DNA has an intermediate density",
      [("All the DNA is heavy", "The new strands are made with 14N, so the DNA cannot be all heavy."), ("All the DNA is light", "Each molecule still contains an old heavy strand."), ("Half of the DNA is heavy and half is light", "Each molecule is a hybrid, so none is fully heavy or fully light.")],
      [("Meselson and Stahl", "Each daughter DNA molecule has one old (15N) and one new (14N) strand, which is the intermediate density. This supports semi-conservative replication.")], T_REP, "Application", "Each molecule keeps one old strand."),
    Q("In the Meselson-Stahl experiment, what is seen after two generations in 14N medium?", "Half of the DNA is of intermediate density and half is light",
      [("All the DNA is of intermediate density", "That is the result after one generation."), ("All the DNA is light", "Half of the molecules still contain an old heavy strand."), ("Half of the DNA is heavy and half is light", "No molecules are fully heavy after the first generation.")],
      [("Second generation", "The intermediate molecules separate, so half the molecules are hybrid and half are fully light.")], T_REP, "Reasoning", "Draw the strands for the second generation."),
    Q("The template strand of a gene has the base sequence TAC GGT. What is the sequence of the mRNA transcribed from it?", "AUG CCA",
      [("ATG CCA", "RNA contains uracil, not thymine."), ("UAC GGU", "This copies the template instead of making the complement."), ("TAC GGT", "This is the template strand itself.")],
      [("Complementary", "T gives A, A gives U, C gives G, G gives C, G gives C, T gives A: AUG CCA.")], T_CODE, "Application", "RNA pairs with uracil in place of thymine."),
    Q("In which phase of the cell cycle is DNA replicated?", "S phase of interphase",
      [("Prophase of mitosis", "The chromosomes condense in prophase, but replication is already complete."), ("Anaphase", "The chromatids separate in anaphase."), ("Cytokinesis", "The cytoplasm divides in cytokinesis.")],
      [("Recall", "G1 growth, S phase DNA synthesis, G2 preparation, then mitosis.")], T_MITO, "Recall", "Which phase is named after synthesis?"),
    Q("Crossing over occurs between:", "Non-sister chromatids of homologous chromosomes in prophase I",
      [("Sister chromatids in prophase II", "Sister chromatids are identical, so crossing over between them would not give new combinations."), ("Non-homologous chromosomes in anaphase", "Crossing over happens between homologous chromosomes in prophase I."), ("Chromosomes in telophase of mitosis", "Crossing over is a feature of meiosis.")],
      [("Recall", "Chiasmata form between non-sister chromatids of a homologous pair, creating new combinations of alleles.")], T_MEI, "Recall", "Which pair of chromosomes lines up in meiosis I?"),
    # ---- Biodiversity & Systematic Taxonomy (7)
    Q("Which of the following lists the three domains of life?", "Bacteria, Archaea and Eukarya",
      [("Plantae, Animalia and Fungi", "These are kingdoms within Eukarya."), ("Prokaryota, Protoctista and Fungi", "These are not the domains."), ("Bacteria, Protoctista and Eukarya", "Protoctista is a kingdom, not a domain.")],
      [("Recall", "The three-domain system divides life into Bacteria, Archaea and Eukarya.")], T_DOM, "Recall", "Name the domains."),
    Q("Which kingdom has cell walls containing chitin and feeds by absorbing nutrients from dead organic matter?", "Fungi",
      [("Plantae", "Plant cell walls contain cellulose."), ("Animalia", "Animal cells have no cell wall."), ("Protoctista", "Protoctists include organisms with different walls and feeding methods.")],
      [("Recall", "Fungi are heterotrophs with chitin walls.")], T_DOM, "Recall", "Which kingdom contains moulds and mushrooms?"),
    Q("Which feature would be suitable for use in a dichotomous key?", "The number of legs on the specimen",
      [("Whether it is cold-blooded", "This cannot be observed on a specimen."), ("What it eats", "Feeding is not a visible feature."), ("How fast it runs", "Behaviour is not a visible feature of the specimen.")],
      [("Rule", "Keys use visible external features that can be counted or seen.")], T_KEY, "Application", "Which feature can you see on the specimen?"),
    Q("Which is the correct way to write the scientific name of the lion?", "Panthera leo (italic or underlined, with a capital letter for the genus)",
      [("panthera Leo", "The genus has the capital letter, not the species."), ("Panthera Leo", "The species name is written with a lowercase letter."), ("panthera leo", "The genus name begins with a capital letter.")],
      [("Binomial", "Genus with a capital, species with a lowercase letter, both italic or underlined.")], T_KEY, "Recall", "Which name has the capital letter?"),
    Q("Which of the following is a fungus?", "Rhizopus, the bread mould",
      [("Amoeba", "Amoeba is a protoctist."), ("Spirogyra", "Spirogyra is an alga, a protoctist."), ("Plasmodium", "Plasmodium is a protoctist that causes malaria.")],
      [("Recall", "Rhizopus has hyphae and reproduces by spores, like other fungi.")], T_PROTO, "Recall", "Which organism has hyphae?"),
    Q("Which statement about mosses (bryophytes) is correct?", "They lack true roots and xylem and need water for the male gametes to swim to the egg",
      [("They have xylem and phloem and produce seeds", "Mosses have no vascular tissue and produce spores."), ("They produce seeds in cones", "That describes conifers."), ("They have true roots to absorb water", "They have rhizoids.")],
      [("Recall", "Mosses are small, have rhizoids and spore capsules and need water for fertilisation.")], T_PLANT, "Recall", "Mosses have no vascular tissue."),
    Q("A worm has a segmented body, bristles (chaetae) on each segment and a closed blood system. To which phylum does it belong?", "Annelida",
      [("Nematoda", "Nematodes are unsegmented roundworms."), ("Platyhelminthes", "Flatworms are flat and unsegmented."), ("Arthropoda", "Arthropods have jointed limbs and an exoskeleton.")],
      [("Recall", "Segmentation with chaetae is characteristic of annelids, such as earthworms.")], T_ANIM, "Application", "Which phylum is segmented worms?"),
    # ---- Autotrophic & Heterotrophic Nutrition (7)
    Q("Where in the chloroplast do the light-dependent reactions occur?", "On the thylakoid membranes in the grana",
      [("In the stroma", "The Calvin cycle occurs in the stroma."), ("In the outer membrane", "The outer membrane is a boundary."), ("In the cytoplasm of the cell", "Photosynthesis occurs within the chloroplast.")],
      [("Recall", "The pigments and electron carriers are on the thylakoid membranes.")], T_CHLO, "Recall", "Where are the photosystems?"),
    Q("What does an action spectrum for photosynthesis show?", "The rate of photosynthesis at different wavelengths of light",
      [("The amount of light absorbed by a pigment at each wavelength", "That is an absorption spectrum."), ("The amount of oxygen in the air at each wavelength", "That is not an action spectrum."), ("The colour of light reflected by a leaf", "This is not the action spectrum.")],
      [("Definition", "An action spectrum plots the rate of photosynthesis against wavelength.")], T_CHLO, "Concept", "Think about the word 'action'."),
    Q("In non-cyclic photophosphorylation, what is the final electron acceptor?", "NADP",
      [("Oxygen", "Oxygen is released from water, not an acceptor."), ("Water", "Water is the electron donor."), ("Chlorophyll a", "Chlorophyll passes electrons on but is not the final acceptor.")],
      [("Pathway", "Electrons from water pass through photosystem II and I to NADP, forming reduced NADP.")], T_LIGHT, "Recall", "Which coenzyme is reduced?"),
    Q("Which products are made in cyclic photophosphorylation?", "ATP only",
      [("ATP and reduced NADP", "That is non-cyclic."), ("Reduced NADP and oxygen", "Neither is made in the cyclic pathway."), ("Oxygen and ATP", "Oxygen comes from the photolysis of water, which is not part of the cyclic pathway.")],
      [("Cyclic", "Electrons return to photosystem I, so only ATP is made.")], T_LIGHT, "Recall", "Which compounds need photolysis?"),
    Q("Which enzyme combines carbon dioxide with RuBP in the Calvin cycle?", "Rubisco",
      [("ATP synthase", "ATP synthase makes ATP."), ("PEP carboxylase", "That fixes CO₂ in C4 plants."), ("Carbonic anhydrase", "That catalyses the reaction of CO₂ and water in red blood cells.")],
      [("Recall", "Rubisco fixes CO₂ to RuBP, giving two molecules of glycerate 3-phosphate (GP).")], T_CALV, "Recall", "Which enzyme fixes carbon dioxide in the Calvin cycle?"),
    Q("How do C4 plants reduce photorespiration?", "They first fix CO₂ in mesophyll cells and release it in the bundle sheath cells, where it is concentrated around rubisco",
      [("They keep their stomata closed all day", "They need CO₂ for photosynthesis."), ("They do not use rubisco", "They use rubisco in the bundle sheath cells."), ("They fix CO₂ only at night", "That describes CAM plants.")],
      [("Mechanism", "PEP carboxylase fixes CO₂ in the mesophyll. The 4-carbon compound moves to the bundle sheath, releasing CO₂ at a high concentration, so rubisco is less likely to react with oxygen.")], T_C4, "Concept", "Where does the Calvin cycle occur in C4 plants?"),
    Q("Which hormone, released from the duodenum when acidic food enters, stimulates the pancreas to secrete a fluid rich in hydrogencarbonate?", "Secretin",
      [("Gastrin", "Gastrin stimulates the secretion of gastric juice in the stomach."), ("Cholecystokinin", "CCK stimulates the release of pancreatic enzymes and bile."), ("Insulin", "Insulin is a pancreatic hormone controlling glucose.")],
      [("Recall", "Secretin neutralises the acid chyme by stimulating alkaline pancreatic juice.")], T_DIG, "Recall", "Which hormone is linked to acid in the duodenum?"),
    # ---- Gaseous Exchange & Mass Transport Systems (9)
    Q("Which sequence of events occurs during inspiration in a resting person?", "The diaphragm contracts and flattens, the thorax volume increases, and the lung pressure falls below atmospheric pressure",
      [("The diaphragm relaxes, the thorax volume decreases and the lung pressure rises", "That describes expiration."), ("The diaphragm contracts, the thorax volume decreases and the pressure falls", "A smaller volume would raise the pressure."), ("The lungs expand by their own muscles and air is sucked in", "The lungs contain no muscle for expansion.")],
      [("Sequence", "Muscle contraction, increased volume, decreased pressure, air flows in.")], T_VENT, "Concept", "Which way does the volume change?"),
    Q("A person has a tidal volume of 0.6 dm³ and breathes 15 times a minute. What is the pulmonary ventilation?", "9.0 dm³ per minute",
      [("0.04 dm³ per minute", "That is 0.6 ÷ 15."), ("25 dm³ per minute", "That is 15 ÷ 0.6."), ("15.6 dm³ per minute", "That adds the two numbers.")],
      [("Calculation", "0.6 × 15 = 9.0 dm³ per minute.")], T_VENT, "Calculation", "Multiply the volume by the rate."),
    Q("What is the effect of a rise in the CO₂ concentration on the oxygen dissociation curve of adult haemoglobin?", "The curve shifts to the right, so more oxygen is released at a given pO₂",
      [("The curve shifts to the left, so more oxygen is released", "A left shift means a higher affinity and less release."), ("The curve shifts to the left, so less oxygen is released", "CO₂ shifts the curve to the right."), ("The curve does not move", "The Bohr effect moves the curve.")],
      [("Bohr shift", "More CO₂ means more H⁺, which lowers the affinity of haemoglobin for oxygen.")], T_ODC, "Concept", "Which direction means a lower affinity?"),
    Q("Why must fetal haemoglobin have a higher affinity for oxygen than adult haemoglobin?", "It must be able to take up oxygen from the mother's blood at the placenta, where the pO₂ is low",
      [("It must release oxygen to the mother", "Oxygen moves from mother to fetus."), ("It has no iron, so it holds oxygen more tightly", "Fetal haemoglobin also contains haem groups with iron."), ("It carries carbon dioxide only", "It carries oxygen.")],
      [("Placenta", "Fetal blood has to load oxygen at a pO₂ at which the mother's haemoglobin is unloading.")], T_ODC, "Application", "Which direction must oxygen move at the placenta?"),
    Q("What closes the atrioventricular valves at the start of ventricular systole?", "The pressure in the ventricle rises above the pressure in the atrium",
      [("The pressure in the aorta rises above that in the ventricle", "That closes the semilunar valve."), ("The atrium relaxes", "Relaxation of the atrium does not close the valve."), ("A nerve impulse from the vagus nerve", "Valves are closed by pressure differences, not by nerves.")],
      [("Valves", "Valves are passive and close when the pressure in front exceeds the pressure behind.")], T_CARD, "Concept", "Which chamber has the higher pressure at the start of systole?"),
    Q("Which structure delays the wave of excitation for about 0.1 s before it passes to the ventricles?", "The atrioventricular node",
      [("The sinoatrial node", "That starts the wave."), ("The Purkyne fibres", "They conduct the wave through the ventricle walls."), ("The vagus nerve", "It controls the heart rate but does not conduct the wave inside the heart.")],
      [("Recall", "The delay lets the atria empty before the ventricles contract.")], T_CARD, "Recall", "Which node is between the atria and ventricles?"),
    Q("At one point along a capillary, the hydrostatic pressure is 3.8 kPa and the oncotic pressure of the plasma is 3.0 kPa. What is the net movement of fluid?", "Net movement out of the capillary, with a net filtration pressure of +0.8 kPa",
      [("Net movement into the capillary, with a net pressure of −0.8 kPa", "The hydrostatic pressure is higher, so fluid leaves."), ("No net movement because both are positive", "Net movement depends on the difference."), ("Net movement out of the capillary, with a net pressure of +6.8 kPa", "That adds the pressures instead of subtracting them.")],
      [("Calculation", "3.8 − 3.0 = +0.8 kPa, so fluid leaves.")], T_TISS, "Calculation", "Subtract the oncotic pressure from the hydrostatic pressure."),
    Q("A plant cell has Ψs = −1.1 MPa and Ψp = +0.5 MPa. What is its water potential?", "−0.6 MPa",
      [("−1.6 MPa", "That subtracts the pressure potential."), ("+0.6 MPa", "Water potential is negative here; the sign matters."), ("−0.5 MPa", "That ignores the solute potential.")],
      [("Formula", "Ψ = Ψs + Ψp = −1.1 + 0.5 = −0.6 MPa.")], T_WATER, "Calculation", "Add the two components, keeping the signs."),
    Q("Which observation supports the mass flow hypothesis for phloem transport?", "Sap flows out under pressure from a severed aphid stylet inserted in a sieve tube",
      [("The diameter of a tree trunk shrinks in the day", "That is evidence for tension in the xylem."), ("Water rises in a cut stem placed in a dye solution", "That relates to xylem transport."), ("Sieve plates have large pores", "Sieve plates may obstruct flow, which is a difficulty for the hypothesis.")],
      [("Evidence", "Sap pushed out of a cut stylet shows a positive hydrostatic pressure in the sieve tubes.")], T_PHLO, "Reasoning", "Which observation involves pressure in the phloem?"),
    # ---- Ecology, Population Dynamics & Conservation (7)
    Q("A forest has a gross primary productivity of 30 000 kJ m⁻² year⁻¹ and plant respiration of 12 000 kJ m⁻² year⁻¹. What is its net primary productivity?", "18 000 kJ m⁻² year⁻¹",
      [("42 000 kJ m⁻² year⁻¹", "That adds GPP and R."), ("12 000 kJ m⁻² year⁻¹", "That is the respiration, not the NPP."), ("2.5 kJ m⁻² year⁻¹", "That is GPP ÷ R.")],
      [("Formula", "NPP = GPP − R = 30 000 − 12 000 = 18 000.")], T_ENER, "Calculation", "Subtract the plants' respiration."),
    Q("The net primary productivity of a grassland is 25 000 kJ m⁻² year⁻¹ and the primary consumers gain 2 000 kJ m⁻² year⁻¹. What is the efficiency of energy transfer?", "8%",
      [("12.5%", "That is 25 000 ÷ 2 000, inverted."), ("1.25%", "That is a misplaced decimal."), ("92%", "That is the percentage lost, not the percentage transferred.")],
      [("Calculation", "2 000 ÷ 25 000 × 100 = 8%.")], T_ENER, "Calculation", "Divide the energy gained by the energy available."),
    Q("Which bacteria convert ammonium ions into nitrite ions?", "Nitrosomonas",
      [("Nitrobacter", "That converts nitrite to nitrate."), ("Rhizobium", "That fixes nitrogen gas."), ("Pseudomonas denitrificans", "That converts nitrate to nitrogen gas.")],
      [("Recall", "Nitrosomonas is the first step of nitrification.")], T_CYC, "Recall", "Which step of nitrification is it?"),
    Q("Which row correctly pairs a process with its change?", "Nitrogen fixation: nitrogen gas to ammonium",
      [("Denitrification: ammonium to nitrate", "That is nitrification; denitrification converts nitrate to nitrogen gas."), ("Nitrification: nitrogen gas to ammonium", "That is fixation."), ("Ammonification: nitrate to nitrite", "Ammonification releases ammonium from organic nitrogen.")],
      [("Recall", "Fixation: N₂ to NH₄⁺.")], T_CYC, "Recall", "Match the name with the starting compound."),
    Q("Which statement about a climax community is correct?", "Gross productivity is about equal to respiration and the species composition is relatively stable",
      [("The net primary productivity is at its highest", "NPP is near zero at the climax."), ("The community contains only pioneer species", "Pioneers are replaced earlier."), ("The soil is at its thinnest", "The soil is deepest at the climax.")],
      [("Recall", "At the climax biomass stops increasing because GPP is about equal to R.")], T_SUCC, "Concept", "NPP = GPP − R."),
    Q("In a capture-recapture study, 30 animals are marked. A second sample of 60 contains 6 marked animals. What is the estimated population?", "300",
      [("3", "That is 30 × 6 ÷ 60."), ("12", "That is 30 × 6 ÷ 15."), ("1 800", "That multiplies 30 × 60 with no division by R.")],
      [("Calculation", "N = 30 × 60 ÷ 6 = 300.")], T_POP, "Calculation", "N = M × C ÷ R."),
    Q("What is biomagnification?", "The increase in the concentration of a persistent toxin at each higher trophic level of a food chain",
      [("The increase in the size of an organism that eats a toxin", "Biomagnification is about concentration, not body size."), ("The growth of algae after the addition of nitrates", "That is an algal bloom as part of eutrophication."), ("The breakdown of a toxin by decomposers", "A persistent toxin is not broken down.")],
      [("Definition", "A persistent substance, stored in the tissues, becomes more concentrated up the food chain because each predator eats many prey.")], T_BDIV, "Recall", "What happens up the food chain?"),
]
assert len(P1) == 50, len(P1)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="bixl-paper1-multiple-choice",
    mock=True, time_limit_minutes=90, questions=build(P1, 31)))

# ------------------------------------------------------------------ Paper 2 practice paper A (structured, auto-markable parts)
# 8 numbered questions, 25 parts; the concept of each part is the topic title it tests. A KKEVO practice setting (150 minutes).
P2 = [
    # Question 1: membranes and water potential
    N("Question 1(a). A potato cell has a solute potential of −0.8 MPa and a pressure potential of +0.3 MPa. Calculate its water potential in MPa.", -0.5,
      [("Formula", "Ψ = Ψs + Ψp."), ("Calculate", "−0.8 + 0.3 = −0.5 MPa.")], T_WPOT, "Calculation", "Add the two potentials, keeping the signs.", tol=0.01, unit="MPa"),
    Q("Question 1(b). Potassium ions enter a root hair cell against their concentration gradient. Which process is responsible?", "Active transport using carrier proteins and ATP",
      [("Simple diffusion through the phospholipid bilayer", "Ions cannot pass through the hydrophobic core, and diffusion is down a gradient."), ("Osmosis through the membrane", "Osmosis is the movement of water."), ("Facilitated diffusion through channel proteins", "That is down the gradient and needs no ATP.")],
      [("Concept", "Movement against a gradient needs energy and carriers: active transport.")], T_TRANS, "Concept", "Which processes need ATP?"),
    Q("Question 1(c). Which component of the cell surface membrane is mainly responsible for cell recognition?", "Glycoproteins and glycolipids",
      [("Cholesterol", "Cholesterol regulates fluidity."), ("The hydrophobic fatty acid tails", "These form the core of the bilayer."), ("The phosphate heads", "They face the water but do not carry the recognition signals.")],
      [("Recall", "Carbohydrate chains attached to proteins and lipids act as markers that identify cells.")], T_FLUID, "Recall", "Which components carry carbohydrate chains?"),
    # Question 2: molecules and enzymes
    N("Question 2(a). An enzyme has a Vmax of 16 µmol per minute. At a substrate concentration of 2 mM the rate is 8 µmol per minute. What is the Km in mM?", 2,
      [("Meaning", "Km is the substrate concentration at which the rate is half of Vmax."), ("Half of Vmax", "Half of 16 is 8 µmol per minute, found at 2 mM, so Km = 2 mM.")], T_ENZK, "Interpretation", "At which concentration is the rate Vmax ÷ 2?", tol=0.05, unit="mM"),
    Q("Question 2(b). Why is starch a good storage molecule in plants?", "It is compact and insoluble, so it does not affect the water potential of the cell",
      [("It is soluble and moves easily to all parts of the cell", "Starch is insoluble."), ("It is made of fatty acids", "Starch is made of glucose."), ("It forms strong fibres around the cell", "That describes cellulose.")],
      [("Application", "Insolubility means starch has no osmotic effect; the spiral and branched shape makes it compact.")], T_CARB, "Application", "What would soluble glucose do to the cell's water potential?"),
    Q("Question 2(c). A non-competitive inhibitor is added to an enzyme-catalysed reaction. What happens to Vmax?", "Vmax decreases and it cannot be restored by adding more substrate",
      [("Vmax increases", "Inhibitors reduce Vmax."), ("Vmax stays the same", "That is the effect of a competitive inhibitor."), ("Vmax decreases, but it is restored by more substrate", "More substrate does not overcome a non-competitive inhibitor.")],
      [("Concept", "A non-competitive inhibitor binds away from the active site and reduces the number of working enzymes, so Vmax falls.")], T_ENZI, "Concept", "Which inhibitor binds away from the active site?"),
    # Question 3: nucleic acids and cell division
    N("Question 3(a). A polypeptide has 150 amino acids. How many nucleotides are there in the coding region of the mRNA (not counting the stop codon)?", 450,
      [("Triplet code", "Each amino acid is coded by three nucleotides."), ("Calculate", "150 × 3 = 450 nucleotides.")], T_CODE, "Calculation", "How many bases code for each amino acid?", tol=0.5),
    Q("Question 3(b). Which enzyme joins the Okazaki fragments on the lagging strand during DNA replication?", "DNA ligase",
      [("DNA helicase", "Helicase unwinds the double helix."), ("RNA polymerase", "RNA polymerase makes RNA in transcription."), ("Amylase", "Amylase digests starch.")],
      [("Recall", "DNA polymerase makes the fragments; DNA ligase joins them.")], T_REP, "Recall", "Which enzyme makes bonds between the fragments?"),
    Q("Question 3(c). An organism has 14 chromosomes in each body cell. How many chromosomes are in each cell at the end of meiosis?", "7",
      [("14", "That is the number in the body cells."), ("28", "That is double the number."), ("3.5", "Chromosomes cannot be shared out in halves.")],
      [("Concept", "Meiosis halves the chromosome number from 14 to 7 in each of four cells.")], T_MEI, "Application", "Meiosis produces haploid cells."),
    # Question 4: taxonomy
    Q("Question 4(a). Which feature identifies an animal as an arthropod?", "Jointed legs and an exoskeleton of chitin",
      [("A backbone and a nerve cord", "That is a feature of vertebrates."), ("A soft body covered by a shell", "This describes molluscs."), ("A body made of many identical rings with bristles", "This describes annelids.")],
      [("Recall", "Arthropods have jointed appendages and a chitin exoskeleton, such as insects and crabs.")], T_ANIM, "Recall", "Think of an insect's legs."),
    Q("Question 4(b). Which pair of statements is correctly written for a dichotomous key?", "1a Has wings, go to 2; 1b Has no wings, go to 3",
      [("1a Has wings, go to 2; 1b Has six legs, go to 3", "The two statements are not opposites."), ("1a Is large, go to 2; 1b Is small, go to 3", "Large and small are not exact features."), ("1a Has wings, go to 2; 1b Lays eggs, go to 3", "The pair must be opposites using the same feature.")],
      [("Rule", "Each pair of statements describes two opposite states of the same visible feature.")], T_KEY, "Application", "What must the two statements of a pair be?"),
    Q("Question 4(c). How do fungi feed?", "They secrete enzymes onto dead organic matter and absorb the digested products",
      [("They make their own food by photosynthesis", "Fungi have no chlorophyll."), ("They engulf food by phagocytosis into a mouth", "Fungi absorb food through their hyphae."), ("They fix nitrogen from the air", "They are not nitrogen fixers.")],
      [("Nutrition", "Fungi are saprophytes with extracellular digestion.")], T_PROTO, "Recall", "Where does fungal digestion take place?"),
    # Question 5: nutrition
    Q("Question 5(a). Which products are released when water is split in the light-dependent stage of photosynthesis?", "Electrons, protons (hydrogen ions) and oxygen",
      [("Carbon dioxide and glucose", "These are not products of water splitting."), ("ATP and NADP", "These are made later by electron transport."), ("Hydrogen gas and carbon", "Hydrogen gas is not released.")],
      [("Photolysis", "Water splits into electrons, H⁺ and O₂. The oxygen is released as a by-product.")], T_LIGHT, "Recall", "What is in a water molecule?"),
    Q("Question 5(b). In the Calvin cycle, glycerate 3-phosphate (GP) is converted to triose phosphate. What does this use?", "ATP and reduced NADP from the light-dependent stage",
      [("Oxygen and water", "Neither is used in the reduction of GP."), ("Light directly", "The Calvin cycle uses the products of the light-dependent stage, not light itself."), ("Carbon dioxide only", "CO₂ is fixed earlier, by rubisco.")],
      [("Reduction", "GP is reduced using energy from ATP and hydrogen from reduced NADP.")], T_CALV, "Recall", "What links the two stages of photosynthesis?"),
    Q("Question 5(c). Which two features of the villus help to maintain a steep concentration gradient for absorption of glucose?", "A rich network of blood capillaries and a thin epithelium",
      [("A thick layer of muscle and a wide lumen", "These do not maintain the gradient."), ("Goblet cells and mucus secretion", "Mucus protects and lubricates; it does not maintain the gradient."), ("Large vacuoles and a thick wall", "A thick wall would slow diffusion.")],
      [("Application", "Blood flowing through the capillaries removes the absorbed glucose, and the thin epithelium gives a short diffusion distance.")], T_DIG, "Application", "What removes the glucose after absorption?"),
    # Question 6: gas exchange, haemoglobin and the heart
    N("Question 6(a). A person has a tidal volume of 0.55 dm³, a dead space of 0.15 dm³ and a breathing rate of 12 per minute. Calculate the alveolar ventilation in dm³ per minute.", 4.8,
      [("Per breath", "0.55 − 0.15 = 0.40 dm³."), ("Per minute", "0.40 × 12 = 4.8 dm³ per minute.")], T_VENT, "Calculation", "Subtract the dead space from each breath.", tol=0.05, unit="dm³ per minute"),
    Q("Question 6(b). What is the advantage of the Bohr shift in an exercising muscle?", "More oxygen is released from haemoglobin where respiration is fastest",
      [("Haemoglobin holds oxygen more tightly", "The Bohr shift lowers the affinity."), ("Less carbon dioxide is produced", "Exercise produces more CO₂."), ("The muscle needs less oxygen", "An exercising muscle needs more oxygen.")],
      [("Application", "More CO₂ and H⁺ lower the affinity of haemoglobin, so more oxygen is unloaded in the tissue that needs it.")], T_ODC, "Application", "Right means a lower affinity."),
    N("Question 6(c). The stroke volume of a ventricle is 80 cm³ and the heart rate is 70 beats per minute. Calculate the cardiac output in cm³ per minute.", 5600,
      [("Formula", "Cardiac output = stroke volume × heart rate."), ("Calculate", "80 × 70 = 5600 cm³ per minute.")], T_CARD, "Calculation", "Multiply the volume of one beat by the beats per minute.", tol=5, unit="cm³ per minute"),
    N("Question 6(d). On an ECG, the time between two R peaks is 0.60 s. Calculate the heart rate in beats per minute.", 100,
      [("Calculate", "60 ÷ 0.60 = 100 beats per minute.")], T_CARD, "Calculation", "Heart rate = 60 ÷ time of one cycle in seconds.", tol=0.5, unit="beats per minute"),
    # Question 7: transport in plants and tissue fluid
    N("Question 7(a). In a potometer, the capillary tube has a radius of 0.5 mm. The air bubble moves 30 mm in 6 minutes. Calculate the rate of water uptake in mm³ per minute.", 3.9,
      [("Volume", "π × 0.5² × 30 = 23.6 mm³."), ("Rate", "23.6 ÷ 6 = 3.9 mm³ per minute.")], T_WATER, "Calculation", "Volume = πr²d.", tol=0.1, unit="mm³ per minute"),
    Q("Question 7(b). What is the function of companion cells in the phloem?", "They load sucrose into the sieve tubes and supply them with ATP",
      [("They carry water up the stem", "That is the function of xylem vessels."), ("They make the sieve plates", "The sieve plates are part of the sieve tube walls."), ("They store starch grains for the sieve tube", "They do not store starch for the sieve tube.")],
      [("Recall", "Companion cells have many mitochondria and carry out the active loading of sucrose.")], T_PHLO, "Recall", "What does a sieve tube element lack?"),
    Q("Question 7(c). A child with very low plasma protein has a swollen abdomen. What is the cause of the swelling?", "The oncotic pressure of the blood is too low to draw tissue fluid back into the capillaries",
      [("The hydrostatic pressure in the capillaries is zero", "Hydrostatic pressure is not zero."), ("The lymph vessels produce too much tissue fluid", "Lymph vessels drain fluid; they do not produce it."), ("The red blood cells leave the capillaries", "Red blood cells normally stay in the capillaries.")],
      [("Oedema", "Less protein means less oncotic pressure, so more fluid stays in the tissues.")], T_TISS, "Application", "Which pressure draws water into the capillary?"),
    # Question 8: ecology
    N("Question 8(a). A savanna has a gross primary productivity of 22 000 kJ m⁻² year⁻¹ and plant respiration of 9 000 kJ m⁻² year⁻¹. Calculate the net primary productivity in kJ m⁻² year⁻¹.", 13000,
      [("Formula", "NPP = GPP − R."), ("Calculate", "22 000 − 9 000 = 13 000 kJ m⁻² year⁻¹.")], T_ENER, "Calculation", "Subtract the respiration.", tol=10, unit="kJ m⁻² year⁻¹"),
    N("Question 8(b). In a capture-recapture study of frogs, 40 were marked and released. A second sample of 50 frogs contained 10 marked frogs. Estimate the population size.", 200,
      [("Formula", "N = M × C ÷ R."), ("Calculate", "40 × 50 ÷ 10 = 200 frogs.")], T_POP, "Calculation", "N = (marked × second sample) ÷ marked in the second sample.", tol=1, unit="frogs"),
    N("Question 8(c). A sample contains three species with 6, 3 and 1 individuals. Calculate Simpson's index D = N(N − 1) ÷ Σn(n − 1) to 1 decimal place.", 2.5,
      [("N", "N = 10, so N(N − 1) = 90."), ("Σn(n−1)", "6 × 5 + 3 × 2 + 1 × 0 = 30 + 6 + 0 = 36."), ("D", "90 ÷ 36 = 2.5.")], T_BDIV, "Calculation", "Work out n(n − 1) for each species.", tol=0.05),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="bixl-paper2-theory-essay",
    mock=True, time_limit_minutes=150, questions=build(P2, 32)))

