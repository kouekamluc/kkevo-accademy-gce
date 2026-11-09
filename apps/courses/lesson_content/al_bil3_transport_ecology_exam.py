"""A Level Biology (0710), Lower Sixth: Gaseous Exchange & Mass Transport Systems, Ecology, Population Dynamics & Conservation, and the Examination module.

13 topic lessons (bil3-) and 3 examination lessons (bixl-), one practice set each (see the practice file of the same name).
Content follows KKEVO's master curriculum blueprint (module lines for L6M6 and L6M7) and the Board's 2023 subject report for
exam structure and common errors; it is not a Board syllabus booklet. Curves, cardiac traces, population curves and the
succession diagram are teaching models drawn from the stated teaching data (invented or typical values, labelled as such).
Calculations (saturation values, cardiac output, potometer volumes, productivity, diversity indices, capture-recapture,
statistics) were checked by script.
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "lower-sixth")

M_GAS = "Gaseous Exchange & Mass Transport Systems"
M_ECO = "Ecology, Population Dynamics & Conservation"
M_EXAM = "Examination"

LESSONS = []

# ------------------------------------------------------------------ 1. Ventilation and gaseous exchange
LESSONS.append(lesson(
    module=M_GAS,
    topic="Ventilation and gaseous exchange",
    title="Ventilation of the lungs and gaseous exchange in the alveoli",
    slug="bil3-ventilation-gas-exchange",
    minutes=24,
    summary="How pressure changes move air in and out of the mammalian lungs, how the alveolus is built for rapid diffusion, and how lung volumes and ventilation rates are measured and calculated.",
    objectives=[
        "Explain inspiration and expiration in terms of muscles, thorax volume and pressure",
        "Relate the structure of the alveolus to Fick's law of diffusion",
        "Define tidal volume, vital capacity, residual volume and pulmonary ventilation, and read them from a spirometer trace",
        "Calculate pulmonary and alveolar ventilation and explain how breathing is controlled",
    ],
    key_concepts=["Ventilation", "Alveolus", "Fick's law", "Tidal volume", "Vital capacity", "Residual volume", "Dead space", "Surfactant"],
    blocks=[
        H("Introduction"),
        T("A footballer in Garoua finishes a hard match and breathes fast and deep for several minutes. His body is "
          "paying back an oxygen debt, and getting rid of extra carbon dioxide. Two different processes work together here. "
          "**Ventilation** (breathing) moves fresh air into the lungs and stale air out. **Gaseous exchange** is the diffusion of oxygen "
          "into the blood and carbon dioxide out of it across the alveolar surface. This lesson explains both."),
        H("The alveolus as an exchange surface"),
        D("The rate of diffusion across a surface is directly proportional to the surface area and the concentration "
          "(partial pressure) difference, and inversely proportional to the thickness of the barrier.",
          title="Fick's law (in words)", formula=r"\text{rate of diffusion} \propto \frac{\text{surface area} \times \text{concentration difference}}{\text{diffusion distance}}"),
        T("Each human lung holds hundreds of millions of tiny air sacs called **alveoli** (singular: alveolus). Together they give a "
          "total surface area of roughly the size of a tennis court (check your textbook for the exact figure). "
          "Every feature of the alveolus can be linked to Fick's law."),
        KEY("Adaptations of the alveolus", "Match each feature to a term in Fick's law.", cards=[
            ["Large surface area", "Millions of alveoli, each rounded and wrapped in a network of capillaries."],
            ["Short diffusion distance", "The wall is a single layer of flattened (squamous) epithelial cells, touching a capillary wall that is also one cell thick."],
            ["Steep concentration gradient", "Ventilation brings fresh air and the blood flow carries oxygen away, so the gradient is maintained."],
            ["Moist and stretchy", "A thin film of water lets gases dissolve. Elastic fibres let the alveolus stretch and recoil."],
        ]),
        T("The alveolar cells also make **surfactant**, a mixture of phospholipids and proteins. It lowers the surface tension of the water film. "
          "Without it the walls of the alveoli would stick together when you breathe out, and the lungs would be very hard to inflate. "
          "Babies born very early may lack enough surfactant and struggle to breathe."),
        H("Ventilation: pressure and volume"),
        T("Air always moves from a region of higher pressure to one of lower pressure. The lungs have no muscle of their own. "
          "Instead, muscles change the volume of the **thorax** (chest cavity), which changes the pressure inside the lungs. "
          "The lungs are held against the chest wall by a thin film of pleural fluid, so they follow its movements."),
        KEY("Inspiration and expiration at rest", "Compare the two stages.", cards=[
            ["Inspiration (active)", "The external intercostal muscles contract and raise the ribs up and out. The diaphragm contracts and flattens. Thorax volume rises, so lung pressure falls below atmospheric pressure and air flows in."],
            ["Expiration (usually passive)", "The muscles relax. The ribs fall and the diaphragm domes upwards. The elastic lungs recoil. Thorax volume falls, pressure rises above atmospheric and air flows out."],
            ["Forced expiration", "In exercise the internal intercostal muscles contract and pull the ribs down. The abdominal muscles contract and push the diaphragm up. Expiration becomes active."],
        ]),
        H("Lung volumes and ventilation rates"),
        D("**Tidal volume (TV)**: the volume of air breathed in or out in one normal breath. **Vital capacity (VC)**: the largest volume that can be breathed out after the deepest possible breath in. "
          "**Residual volume (RV)**: the air left in the lungs after the deepest possible breath out. **Inspiratory reserve volume (IRV)** and **expiratory reserve volume (ERV)**: "
          "the extra air that can be breathed in or out beyond a normal breath.", title="Lung volumes"),
        IMG("al-bil3-spirometer.svg", alt="Spirometer trace showing three normal breaths, one deepest breath in and one deepest breath out, with brackets for inspiratory reserve volume, tidal volume, expiratory reserve volume, residual volume and vital capacity",
            caption="Figure 1. A spirometer trace (typical teaching values for a young adult: IRV 3.0, TV 0.5, ERV 1.0, RV 1.2 dm³). Vital capacity = IRV + TV + ERV."),
        F(r"\text{VC} = \text{IRV} + \text{TV} + \text{ERV} \qquad \text{TLC} = \text{VC} + \text{RV}", title="Capacities"),
        F(r"\text{pulmonary ventilation} = \text{tidal volume} \times \text{breathing rate}", title="Pulmonary (minute) ventilation"),
        T("Not all the air in a breath reaches the alveoli. The air in the trachea and bronchi (about 0.15 dm³ in an adult) is the **dead space**. "
          "It takes no part in gaseous exchange. A spirometer uses a chamber of oxygen floating on water. As you breathe, the chamber rises and falls "
          "and a pen records the trace on a rotating drum. A chemical (soda lime) absorbs the carbon dioxide so that the oxygen used can be measured."),
        EX("Worked example 1: ventilation rates", intro="Using the trace in Figure 1, a student breathes at 12 breaths per minute. Calculate (a) the pulmonary ventilation and (b) the alveolar ventilation, if the dead space is 0.15 dm³.", steps=[
            S("Pulmonary ventilation", math=r"0.5 \times 12 = 6.0 \text{ dm}^3 \text{ min}^{-1}"),
            S("Air reaching the alveoli in one breath", math=r"0.5 - 0.15 = 0.35 \text{ dm}^3"),
            S("Alveolar ventilation", math=r"0.35 \times 12 = 4.2 \text{ dm}^3 \text{ min}^{-1}", text="Only 4.2 of the 6.0 dm³ per minute takes part in gaseous exchange."),
        ], check=r"4.2 < 6.0"),
        EX("Worked example 2: reading the trace", intro="From Figure 1, find the vital capacity and the total lung capacity.", steps=[
            S("Vital capacity", math=r"3.0 + 0.5 + 1.0 = 4.5 \text{ dm}^3"),
            S("Total lung capacity", math=r"4.5 + 1.2 = 5.7 \text{ dm}^3", text="The residual volume cannot be breathed out, so it is not part of vital capacity."),
        ]),
        H("Control of breathing"),
        T("Breathing is controlled by the **ventilation centre** in the medulla oblongata of the brain. Chemoreceptors in the medulla, and in the carotid and aortic bodies, detect a rise in blood carbon dioxide. "
          "Carbon dioxide forms carbonic acid, which lowers blood pH, and it is this fall in pH that the receptors detect. "
          "Nerve impulses then go to the intercostal muscles and the diaphragm, so breathing becomes faster and deeper. This is negative feedback. "
          "Stretch receptors in the lungs stop over-inflation."),
        MISTAKE("Saying the lungs suck air in", "The lungs are passive. The muscles increase the volume of the thorax, the pressure inside falls, and air is pushed in by the higher atmospheric pressure outside. Always describe the sequence: muscles, volume, pressure, air movement."),
        MISTAKE("Mixing gaseous exchange with breathing", "Breathing (ventilation) is the movement of air. Gaseous exchange is diffusion across the alveolar wall. Respiration is the release of energy in cells. Use each term only for its own meaning."),
        QUIZ("During inspiration at rest, which row is correct?", ["Diaphragm relaxes; thorax volume falls; pressure rises", "Diaphragm contracts; thorax volume rises; pressure falls", "Diaphragm contracts; thorax volume falls; pressure rises", "Diaphragm relaxes; thorax volume rises; pressure falls"], 1,
             "Contraction of the diaphragm and external intercostals raises thorax volume, which lowers the pressure below atmospheric.",
             hint="Which way does the pressure need to change for air to enter?",
             feedback=["That describes expiration.", "", "A contracting diaphragm flattens, so volume cannot fall.", "A relaxed diaphragm cannot raise the volume."]),
        QUIZ("A person has a tidal volume of 0.4 dm³, a dead space of 0.15 dm³ and breathes 15 times per minute. What is the alveolar ventilation?", ["6.0 dm³ per minute", "2.25 dm³ per minute", "3.75 dm³ per minute", "0.25 dm³ per minute"], 2,
             "(0.4 − 0.15) × 15 = 3.75 dm³ per minute.", hint="Subtract the dead space from each breath before multiplying.",
             feedback=["That is the pulmonary ventilation (0.4 × 15) with no allowance for dead space.", "That is 0.15 × 15, the volume that only ventilates the dead space.", "", "That is the air reaching the alveoli in one breath, not in one minute."]),
        TIP("Ventilation and the alveolus appear in Paper 1 (volumes, calculations and the order of events) and in Paper 2 explanations. When asked to explain, link structure to function through Fick's law, and always state the three links in the order muscle, volume, pressure.", title="Exam link"),
        PQ("(a) State three features of the alveolus that make it efficient for gaseous exchange. (b) Explain how inspiration happens in a resting person.",
           "(a) Any three, each with its reason: very large total surface area from millions of alveoli (more diffusion); wall one cell thick (short diffusion distance); rich capillary network and ventilation maintain a steep concentration gradient; moist surface so gases dissolve; surfactant keeps the alveoli open. (b) The external intercostal muscles contract, raising the ribs up and out. The diaphragm contracts and flattens. The volume of the thorax increases, so the pressure in the lungs falls below atmospheric pressure. Air flows in down the pressure gradient."),
        PQ("A spirometer trace shows a tidal volume of 0.55 dm³ at 14 breaths per minute. The vital capacity is 4.8 dm³ and the residual volume 1.3 dm³. Calculate the pulmonary ventilation and the total lung capacity.",
           "Pulmonary ventilation = 0.55 × 14 = 7.7 dm³ per minute. Total lung capacity = vital capacity + residual volume = 4.8 + 1.3 = 6.1 dm³."),
        PQ("Explain why a person who has taken a slow, deep breath has a lower breathing rate than usual, but the same pulmonary ventilation could be maintained.",
           "Pulmonary ventilation = tidal volume × breathing rate. A deeper breath increases the tidal volume, so fewer breaths per minute give the same product. A deeper breath is also more efficient because the dead space is a smaller fraction of each breath, so more air reaches the alveoli."),
        SUM("Ventilation moves air by changing thorax volume and pressure: muscles contract, volume rises, pressure falls, air flows in.",
            "The alveolus follows Fick's law: large area, short distance and a steep gradient maintained by ventilation and blood flow.",
            "Surfactant lowers surface tension and keeps the alveoli open.",
            "VC = IRV + TV + ERV; TLC = VC + RV; pulmonary ventilation = tidal volume × rate; alveolar ventilation uses TV minus dead space.",
            "Chemoreceptors detect a fall in blood pH from carbon dioxide and the medulla raises the breathing rate (negative feedback)."),
    ],
))

# ------------------------------------------------------------------ 2. Oxygen dissociation curves
LESSONS.append(lesson(
    module=M_GAS,
    topic="Oxygen dissociation curves",
    title="Haemoglobin, oxygen dissociation curves and the Bohr and chloride shifts",
    slug="bil3-oxygen-dissociation-curves",
    minutes=25,
    summary="Why the oxygen dissociation curve is S-shaped, how carbon dioxide shifts it (the Bohr shift), how fetal haemoglobin differs, and how carbon dioxide is carried with the chloride shift.",
    objectives=[
        "Describe haemoglobin and explain the S-shape of the curve through cooperative binding",
        "Explain the Bohr shift and the advantage of the curve shifting right in respiring tissues",
        "Compare adult haemoglobin with fetal haemoglobin and with myoglobin",
        "Describe how carbon dioxide is transported and the role of the chloride shift",
    ],
    key_concepts=["Haemoglobin", "Partial pressure", "Cooperative binding", "Oxyhaemoglobin", "Bohr shift", "Chloride shift", "Carbonic anhydrase", "Fetal haemoglobin"],
    blocks=[
        H("Introduction"),
        T("A farmer in Bamenda climbs a steep hill carrying a load and gets out of breath. At higher altitude the air has a lower partial pressure of oxygen. "
          "How does the body still carry enough oxygen? The answer lies in **haemoglobin**, the red pigment of red blood cells, and in the special shape of its oxygen dissociation curve."),
        H("Haemoglobin"),
        D("**Haemoglobin (Hb)** is a protein with quaternary structure: four polypeptide chains (two α and two β in adults), each holding a haem group with one iron(II) ion, Fe²⁺. Each haem can bind one oxygen molecule, so one haemoglobin carries up to four.",
          title="Definition: haemoglobin"),
        F(r"\text{Hb} + 4\text{O}_2 \rightleftharpoons \text{Hb(O}_2)_4", title="Loading and unloading"),
        T("The **partial pressure of oxygen** (pO₂, in kPa) is the share of the total gas pressure that is due to oxygen. Haemoglobin **loads** (combines with) oxygen where pO₂ is high, as in the lungs. "
          "It **unloads** (releases) oxygen where pO₂ is low, as in respiring muscle. **Percentage saturation** is the share of haem groups that carry oxygen."),
        H("The S-shaped curve"),
        IMG("al-bil3-odc.svg", alt="Three S-shaped oxygen dissociation curves: fetal haemoglobin to the left, adult haemoglobin in the middle and adult haemoglobin at high carbon dioxide to the right",
            caption="Figure 1. Oxygen dissociation curves (model curves for teaching; textbooks give slightly different exact values)."),
        T("The curve is S-shaped (sigmoid) because of **cooperative binding**. At low pO₂ the first oxygen molecule binds with difficulty, because the haem groups are buried. "
          "Once it has bound, the shape of the molecule changes slightly and the other haem groups become easier to reach, so the next oxygen binds much more easily. "
          "The curve therefore rises steeply. The last haem group is hard to fill, as there are few free sites left, so the curve levels off near 100%."),
        D("The **Bohr shift (effect)** is the movement of the oxygen dissociation curve to the right when the carbon dioxide concentration rises (and pH falls). Haemoglobin then has a lower affinity for oxygen and releases it more readily at a given pO₂.", title="Definition: Bohr shift"),
        T("Here are teaching values read from the model curves (percentage saturation).\n\nAt pO₂ 2 kPa: fetal Hb 38, adult 18, adult at high CO₂ 10. At 4 kPa: fetal 80, adult 59, adult at high CO₂ 41. At 8 kPa: fetal 96, adult 90, adult at high CO₂ 82. At 13 kPa (lungs): fetal 99, adult 97, adult at high CO₂ 94."),
        EX("Worked example 1: oxygen delivered to a muscle", intro="Using the values above, how much more oxygen (in percentage points of saturation) does haemoglobin release in an exercising muscle with pO₂ 4 kPa and high CO₂ than in a resting tissue at 4 kPa with normal CO₂? Haemoglobin leaves the lungs at 97% saturation.", steps=[
            S("Resting tissue (normal curve)", math=r"97 - 59 = 38 \text{ percentage points released}"),
            S("Exercising muscle (curve shifted right)", math=r"97 - 41 = 56 \text{ percentage points released}"),
            S("Difference", math=r"56 - 38 = 18", text="So 18 more percentage points of saturation are released. The right shift delivers about 47% more oxygen than the normal curve (18 ÷ 38) at the same pO₂."),
        ], check=r"18/38 = 0.47"),
        H("Why the Bohr shift happens"),
        T("In respiring tissue, carbon dioxide diffuses into the red blood cell. The enzyme **carbonic anhydrase** speeds up its reaction with water to form carbonic acid, which splits into hydrogen ions and hydrogencarbonate ions. "
          "The hydrogen ions bind to haemoglobin (it acts as a buffer) and change its shape, so it releases oxygen more easily. Where the tissue is most active, the most oxygen is delivered."),
        F(r"\text{CO}_2 + \text{H}_2\text{O} \xrightarrow{\text{carbonic anhydrase}} \text{H}_2\text{CO}_3 \rightleftharpoons \text{H}^+ + \text{HCO}_3^-"),
        H("Carbon dioxide transport and the chloride shift"),
        T("Carbon dioxide travels in three ways: most as **hydrogencarbonate ions** in the plasma, some bound to haemoglobin as **carbaminohaemoglobin**, and some dissolved in plasma. The exact percentages differ between textbooks (check your textbook), but hydrogencarbonate is always the largest share."),
        T("Hydrogencarbonate ions diffuse out of the red blood cell into the plasma. Positive charge would then build up inside the cell, so chloride ions (Cl⁻) move in from the plasma to keep the charge balanced. "
          "This is the **chloride shift**. In the lungs the processes reverse: hydrogencarbonate re-enters the cell, carbon dioxide is released and diffuses into the alveoli."),
        H("Other haemoglobins"),
        KEY("Curves to the left", "A curve to the left means higher affinity: it loads oxygen at lower pO₂ and unloads less readily.", cards=[
            ["Fetal haemoglobin", "Curve to the left of adult Hb. At the placenta, where pO₂ is low, fetal blood takes oxygen from the mother's blood."],
            ["Myoglobin", "One haem group per molecule, so the curve is hyperbolic (not S-shaped). It holds oxygen in muscle and releases it only when pO₂ is very low, as in hard exercise."],
            ["Animals in low-oxygen places", "Their haemoglobin tends to have a curve to the left (check your textbook for examples such as animals at high altitude)."],
        ]),
        MISTAKE("Shifting the curve the wrong way", "A higher CO₂ concentration moves the curve to the RIGHT. Think of it this way: right means the curve is lower at a given pO₂, so more oxygen is unloaded. Left means the haemoglobin holds on."),
        MISTAKE("Calling the shift a change in the amount of haemoglobin", "The Bohr shift changes the affinity (how tightly oxygen is held), not the number of haemoglobin molecules or the total oxygen capacity."),
        QUIZ("In an actively respiring muscle, which change in the oxygen dissociation curve of haemoglobin is expected?", ["A shift to the left, so more oxygen is released", "A shift to the right, so more oxygen is released", "A shift to the right, so less oxygen is released", "No shift, because pO₂ alone decides unloading"], 1,
             "More CO₂ and a lower pH lower the affinity for oxygen, shifting the curve right, so haemoglobin unloads more oxygen at a given pO₂.",
             hint="Which direction means a lower affinity?",
             feedback=["A left shift raises the affinity, so less oxygen is released.", "", "A right shift releases more oxygen, not less.", "CO₂ and pH change the affinity, which is the Bohr effect."]),
        QUIZ("What is the purpose of the chloride shift?", ["To move chloride ions into the lungs", "To balance the charge when hydrogencarbonate ions leave the red blood cell", "To carry oxygen as chloride salt", "To make carbonic anhydrase work"], 1,
             "Hydrogencarbonate leaves the cell; chloride ions enter so that the charge inside the cell stays balanced.", hint="What would happen to the charge inside the cell if a negative ion left?",
             feedback=["The shift happens in red blood cells, not in the lungs.", "", "Oxygen is not carried as a chloride compound.", "Carbonic anhydrase is an enzyme and is not driven by chloride movement."]),
        TIP("The curve and the Bohr shift are among the most examined ideas in this module. Practise drawing the curve with a labelled axis (pO₂ in kPa, percentage saturation) and sketching the shifted curve to the right. Quote a value from the graph when asked to compare.", title="Exam link"),
        PQ("(a) Explain why the oxygen dissociation curve of adult haemoglobin is S-shaped. (b) Explain the advantage of the Bohr shift in an exercising muscle.",
           "(a) Haemoglobin has four haem groups. At low pO₂ the first oxygen binds slowly. Binding changes the shape of the molecule, which makes it easier for the next oxygens to bind (cooperative binding), so the curve steepens. Near saturation few sites are left, so the curve flattens. (b) The muscle makes carbon dioxide, which forms H⁺ in the red cell. The H⁺ lowers the affinity of haemoglobin for oxygen, so the curve shifts right and more oxygen is released at the same pO₂, in the tissue that needs it most."),
        PQ("Explain why fetal haemoglobin must have a curve to the left of adult haemoglobin.",
           "At the placenta the mother's blood has a low pO₂, which unloads oxygen. For oxygen to move to the fetus, the fetal haemoglobin must have a higher affinity than the maternal haemoglobin, so that it can load oxygen at the same pO₂. A curve to the left shows a higher percentage saturation at any pO₂."),
        PQ("Describe how carbon dioxide is carried from respiring tissues to the lungs, including the part played by the chloride shift.",
           "CO₂ diffuses into red blood cells. Carbonic anhydrase catalyses CO₂ + H₂O into H₂CO₃, which dissociates into H⁺ and HCO₃⁻. H⁺ binds to haemoglobin. HCO₃⁻ diffuses out into the plasma, and Cl⁻ moves in to keep the charge balanced (chloride shift). Most CO₂ is carried as HCO₃⁻ in plasma; some binds to haemoglobin as carbaminohaemoglobin and some dissolves in the plasma. In the lungs the reactions reverse and CO₂ diffuses into the alveoli."),
        SUM("Haemoglobin has four haem groups and loads up to four O₂; the S-shaped curve results from cooperative binding.",
            "A curve to the right means lower affinity and more oxygen unloaded; a curve to the left means higher affinity.",
            "The Bohr shift is caused by CO₂ and H⁺, produced in respiring tissue by carbonic anhydrase, lowering haemoglobin's affinity for oxygen.",
            "Fetal haemoglobin is to the left of adult haemoglobin; myoglobin has a hyperbolic curve and stores oxygen.",
            "CO₂ is carried mainly as hydrogencarbonate; the chloride shift keeps the charge in red cells balanced."),
    ],
))

# ------------------------------------------------------------------ 3. Cardiac cycle
LESSONS.append(lesson(
    module=M_GAS,
    topic="The cardiac cycle and its control",
    title="The cardiac cycle: pressure, volume and valves",
    slug="bil3-cardiac-cycle",
    minutes=24,
    summary="The phases of systole and diastole, how pressure changes open and close the valves, and how stroke volume, heart rate and cardiac output are calculated.",
    objectives=[
        "Define systole, diastole and the cardiac cycle",
        "Describe the sequence of events of one cycle in terms of pressure changes and valve movements",
        "Read a pressure trace for the left atrium, left ventricle and aorta",
        "Calculate cycle length, stroke volume, cardiac output and ejection fraction",
    ],
    key_concepts=["Cardiac cycle", "Systole", "Diastole", "Atrioventricular valve", "Semilunar valve", "Stroke volume", "Cardiac output", "Isovolumetric"],
    blocks=[
        H("Introduction"),
        T("A nurse at a health centre in Maroua places two fingers on a patient's wrist and counts the pulse for one minute: 75 beats. Each beat is one turn of a repeating sequence in the heart. "
          "In the Board's 2023 report, candidates who were asked to describe the cardiac cycle often described the path of blood through the heart instead. The question is about **contraction and relaxation, pressure and valves**. This lesson shows how to answer it."),
        H("The structure you need"),
        T("The heart is a double pump. The right side sends blood to the lungs. The left side sends blood to the body. Each side has an upper **atrium** and a lower **ventricle**. "
          "**Atrioventricular (AV) valves** (tricuspid on the right, bicuspid on the left) lie between atrium and ventricle. **Semilunar valves** (pulmonary and aortic) lie at the exits of the ventricles. "
          "Valves are one-way and have no muscle: they open and close only because of **pressure differences**. The left ventricle has a much thicker wall than the right because it pumps blood round the whole body."),
        D("The **cardiac cycle** is the sequence of events (contraction and relaxation of the chambers, with changes in pressure and valve movements) that makes up one heartbeat. **Systole** is contraction; **diastole** is relaxation.", title="Definitions"),
        H("The events of one cycle"),
        T("At 75 beats per minute one cycle lasts 60 ÷ 75 = 0.8 s. The figure shows the model cycle used in this lesson (typical teaching values; textbooks give slightly different timings)."),
        IMG("al-bil3-cardiac.svg", alt="Pressure in the aorta, left ventricle and left atrium over one 0.8 second cycle, with shaded bands for atrial systole, ventricular systole and diastole and four numbered valve events",
            caption="Figure 1. Pressures during one cycle. Valve events: 1 AV valve closes, 2 aortic valve opens, 3 aortic valve closes, 4 AV valve opens. A = atrial systole."),
        KEY("Phases of the cycle", "Follow the numbers in Figure 1.", cards=[
            ["Atrial systole (0 to 0.1 s)", "The atria contract and top up the ventricles. Atrial pressure rises slightly. The AV valves are open; the semilunar valves are shut."],
            ["Start of ventricular systole (0.1 s)", "The ventricles begin to contract. Ventricular pressure rises above atrial pressure, so the AV valves shut (event 1: the first heart sound, 'lub'). For a short time all valves are closed, and the volume does not change (isovolumetric contraction)."],
            ["Ejection (about 0.2 to 0.4 s)", "Ventricular pressure rises above aortic pressure, so the semilunar valve opens (event 2). Blood is forced out into the aorta. Aortic pressure rises to its peak."],
            ["Start of diastole (about 0.4 s)", "The ventricle relaxes. Its pressure falls below aortic pressure, so the semilunar valve shuts (event 3: the second heart sound, 'dup'). Elastic recoil of the aorta causes a small dip and rise in aortic pressure (the dicrotic notch)."],
            ["Ventricular filling (0.45 to 0.8 s)", "Ventricular pressure falls below atrial pressure, so the AV valve opens (event 4). Blood flows from atrium to ventricle, partly before the atria contract. All chambers are relaxed (diastole)."],
        ]),
        T("The left atrium has a thin wall and produces a small pressure rise. The ventricle produces a very high pressure because it has thick muscle. The aorta pressure never falls to zero, thanks to the elasticity of its wall, so blood flow is smooth."),
        H("Cardiac output"),
        D("**Stroke volume (SV)** is the volume of blood pumped out of one ventricle in one beat. **Cardiac output (CO)** is the volume pumped out of one ventricle in one minute.", title="Definitions"),
        F(r"\text{CO} = \text{SV} \times \text{heart rate} \qquad \text{ejection fraction} = \frac{\text{SV}}{\text{end-diastolic volume}} \times 100"),
        EX("Worked example 1: cardiac output", intro="At rest, the left ventricle holds 120 cm³ at the end of diastole and 50 cm³ at the end of systole. The heart rate is 75 beats per minute. Find the stroke volume, the cardiac output and the ejection fraction.", steps=[
            S("Stroke volume", math=r"120 - 50 = 70 \text{ cm}^3"),
            S("Cardiac output", math=r"70 \times 75 = 5250 \text{ cm}^3 \text{ min}^{-1} = 5.25 \text{ dm}^3 \text{ min}^{-1}"),
            S("Ejection fraction", math=r"\frac{70}{120} \times 100 = 58\%"),
        ], check=r"70 \times 75 = 5250"),
        EX("Worked example 2: effect of exercise", intro="During exercise the heart rate rises to 150 beats per minute and the stroke volume to 100 cm³. By what factor does the cardiac output increase?", steps=[
            S("New cardiac output", math=r"100 \times 150 = 15\,000 \text{ cm}^3 \text{ min}^{-1}"),
            S("Factor", math=r"\frac{15\,000}{5250} = 2.86", text="The cardiac output rises to about 2.9 times its resting value."),
        ]),
        MISTAKE("Describing blood flow instead of the cycle", "A cardiac cycle answer must name systole and diastole, give the pressure relationships and say which valves are open or shut at each stage. A list of chambers the blood passes through earns few marks."),
        MISTAKE("Saying valves are opened by muscle", "Valves open and close passively. A valve opens when the pressure behind it exceeds the pressure in front, and shuts when the pressure in front is higher. Always state the two pressures."),
        QUIZ("Which event closes the atrioventricular valves?", ["Atrial pressure rises above ventricular pressure", "Ventricular pressure rises above atrial pressure at the start of systole", "Aortic pressure rises above ventricular pressure", "The atrial muscle relaxes"], 1,
             "When the ventricle starts to contract, its pressure rises above atrial pressure and pushes the AV valve shut.", hint="Which way does the blood try to flow at the start of ventricular systole?",
             feedback=["That would open the AV valves.", "", "That closes the semilunar (aortic) valve.", "Relaxation of the atrium does not by itself shut the valve."]),
        QUIZ("A ventricle has end-diastolic volume 130 cm³ and stroke volume 65 cm³. What is the ejection fraction?", ["65%", "50%", "2%", "195%"], 1,
             "65 ÷ 130 × 100 = 50%.", hint="Ejection fraction = stroke volume divided by end-diastolic volume.",
             feedback=["That is the stroke volume value, not a percentage.", "", "That inverts the fraction: 130 ÷ 65 = 2.", "That adds the two volumes, 130 + 65."]),
        TIP("The cardiac cycle is a favourite for Paper 2 (with a pressure graph) and appears in Paper 1 as valve and pressure questions. Use the words systole, diastole, pressure and valve in each sentence, and quote times and pressures from any graph supplied.", title="Exam link"),
        PQ("Describe the events that occur in the left side of the heart during ventricular systole.",
           "The ventricle contracts and its pressure rises above the pressure in the left atrium, so the bicuspid (AV) valve shuts. For a short time the ventricle is a closed chamber and pressure rises rapidly (isovolumetric contraction). When ventricular pressure exceeds aortic pressure the semilunar valve opens and blood is ejected into the aorta. The aortic pressure reaches its maximum. At the end of systole the ventricular pressure falls below aortic pressure and the semilunar valve shuts."),
        PQ("The heart rate of an athlete is 60 beats per minute and the stroke volume is 95 cm³. Calculate (a) the length of one cardiac cycle and (b) the cardiac output.",
           "(a) 60 ÷ 60 = 1.0 s. (b) 95 × 60 = 5700 cm³ per minute (5.7 dm³ per minute)."),
        PQ("Explain why the pressure in the aorta does not fall to zero between beats.",
           "During systole the aorta stretches as blood is forced in. During diastole the elastic wall recoils, squeezing the blood onward and keeping the pressure high. The semilunar valve is shut, so blood cannot flow back into the ventricle."),
        SUM("One cycle at 75 beats per minute lasts 0.8 s: atrial systole, ventricular systole, then diastole.",
            "Valves are passive: they open and close because of pressure differences between chambers and arteries.",
            "AV valves close at the start of ventricular systole; semilunar valves open when ventricular pressure exceeds aortic pressure.",
            "Semilunar valves close at the start of diastole, causing the dicrotic notch.",
            "CO = SV × heart rate; ejection fraction = SV ÷ end-diastolic volume × 100."),
    ],
))

# ------------------------------------------------------------------ 4. Control of the heartbeat
LESSONS.append(lesson(
    module=M_GAS,
    topic="The cardiac cycle and its control",
    title="Control of the heartbeat: the sinoatrial node, the ECG and nervous and hormonal control",
    slug="bil3-cardiac-control-sa-node-ecg",
    minutes=23,
    summary="How the heart beats on its own (myogenic) from the SAN, how the wave of excitation is delayed at the AVN and spreads through the ventricles, how to read an ECG, and how the brain and adrenaline change the heart rate.",
    objectives=[
        "Explain why cardiac muscle is described as myogenic",
        "Describe the pathway of excitation from the SAN to the ventricle walls and the reason for the delay at the AVN",
        "Identify the P wave, QRS complex and T wave on an ECG and calculate heart rate from it",
        "Explain how the medulla, the autonomic nerves and adrenaline alter the heart rate",
    ],
    key_concepts=["Myogenic", "Sinoatrial node", "Atrioventricular node", "Bundle of His", "Purkyne fibres", "ECG", "Vagus nerve", "Adrenaline"],
    blocks=[
        H("Introduction"),
        T("A heart removed from a body for a transplant can go on beating for a time if it is kept supplied with oxygen. It does not need a nerve impulse to start each beat. "
          "This is because the heart is **myogenic**: its contraction is started by the cardiac muscle itself. Nerves and hormones only change the speed of a beat the heart is already making."),
        D("Cardiac muscle is **myogenic** if it can contract and relax rhythmically without any external stimulus from nerves.", title="Definition: myogenic"),
        H("The pathway of excitation"),
        T("A small patch of specialised muscle in the wall of the right atrium, the **sinoatrial node (SAN)**, acts as the **pacemaker**. Its cells depolarise spontaneously and set the rate of the heart."),
        KEY("The sequence", "Follow the wave from the SAN to the apex.", cards=[
            ["1. SAN fires", "A wave of electrical excitation spreads over the walls of both atria. The atria contract (atrial systole)."],
            ["2. Fibrous barrier", "A layer of non-conducting fibrous tissue between atria and ventricles stops the wave from going straight to the ventricles."],
            ["3. AVN delay", "The wave reaches the **atrioventricular node (AVN)** in the septum. It is delayed for about 0.1 s, which gives the atria time to empty before the ventricles contract."],
            ["4. Bundle of His", "The wave passes down the **bundle of His** (in the septum) to the apex of the heart."],
            ["5. Purkyne fibres", "**Purkyne fibres** carry the wave up the walls of the ventricles. The ventricles contract from the apex upwards, pushing blood towards the arteries."],
        ]),
        T("Contracting from the apex up makes sure the blood is squeezed out towards the arteries at the top, instead of being trapped at the bottom. "
          "The cells of cardiac muscle are joined by intercalated discs, which let the wave pass quickly from cell to cell."),
        H("The ECG"),
        D("An **electrocardiogram (ECG)** is a recording of the electrical activity of the heart made by electrodes on the skin. It shows the waves of excitation as they spread, not the blood pressure.", title="Definition"),
        KEY("Parts of an ECG", "One normal beat gives three main features.", cards=[
            ["P wave", "Excitation spreading over the atria (atrial depolarisation); the atria then contract."],
            ["QRS complex", "Excitation spreading through the ventricles (ventricular depolarisation); the ventricles then contract. It is tall because the ventricle muscle mass is large."],
            ["T wave", "Recovery (repolarisation) of the ventricles."],
        ]),
        T("The time between two R peaks gives the length of one cycle. A doctor can then calculate the heart rate: **heart rate = 60 ÷ time between R peaks in seconds**."),
        EX("Worked example 1: heart rate from an ECG", intro="On an ECG, the time between two successive R peaks is 0.80 s. A second patient has an R-to-R time of 0.60 s. Find each heart rate.", steps=[
            S("First patient", math=r"\frac{60}{0.80} = 75 \text{ beats per minute}"),
            S("Second patient", math=r"\frac{60}{0.60} = 100 \text{ beats per minute}", text="A resting rate above 100 beats per minute is called tachycardia. Below 60 is bradycardia (check your textbook for exact limits)."),
        ], check=r"60/0.8 = 75"),
        EX("Worked example 2: paper speed", intro="An ECG is printed at a paper speed of 25 mm per second. Two R peaks are 20 mm apart. Find the heart rate.", steps=[
            S("Time between R peaks", math=r"\frac{20}{25} = 0.80 \text{ s}"),
            S("Heart rate", math=r"\frac{60}{0.80} = 75 \text{ beats per minute}"),
        ]),
        T("An ECG can show problems. An irregular spacing of the R peaks suggests an irregular heartbeat (arrhythmia). If a P wave is not followed by a QRS complex, the wave has failed to cross from atria to ventricles (heart block)."),
        H("Nervous and hormonal control"),
        T("The SAN sets a resting rate of about 100 beats per minute if left alone, but the brain normally slows it to about 70 (check your textbook). The **cardiac centre** in the medulla oblongata controls the rate through the autonomic nervous system. "
          "**Baroreceptors** (pressure sensors) in the aorta and carotid arteries and **chemoreceptors** (sensitive to CO₂ and pH) feed back to this centre."),
        KEY("How the rate is changed", "Two nerves and one hormone.", cards=[
            ["Sympathetic nerve (speeds up)", "Releases noradrenaline at the SAN. The heart rate and the force of contraction increase. It acts when blood CO₂ rises (as in exercise) or blood pressure falls."],
            ["Vagus nerve (slows down)", "Part of the parasympathetic system. Releases acetylcholine at the SAN. The heart rate decreases. It acts when blood pressure is too high."],
            ["Adrenaline", "A hormone from the adrenal glands in fear or stress. It acts on the SAN and raises heart rate and stroke volume."],
        ]),
        T("This is **negative feedback**. If blood pressure rises, baroreceptors send more impulses to the cardiac centre, which sends more impulses along the vagus nerve, and the heart slows."),
        MISTAKE("Saying nerves start the heartbeat", "The heartbeat starts in the SAN. Nerves and hormones only change the rate. If the nerves to the heart are cut, the heart continues to beat."),
        MISTAKE("Mixing up the AVN delay with a block", "The AVN delay is normal and useful. It lets the atria finish emptying before the ventricles contract. A heart block is an abnormal failure of the wave to cross."),
        QUIZ("Why is there a short delay at the atrioventricular node?", ["To let the atria empty into the ventricles before the ventricles contract", "To let the ventricles fill the aorta", "To let the SAN recover", "To make the heart rate faster"], 0,
             "The delay makes the ventricles contract after the atria have emptied into them.", hint="What must be completed before ventricular systole starts?",
             feedback=["", "Blood leaves the ventricles only after they contract.", "The SAN recovers by itself; the delay is not for that.", "The delay does not change the rate of the SAN."]),
        QUIZ("Which nerve slows the heart, and which chemical does it release at the SAN?", ["Sympathetic nerve; noradrenaline", "Vagus nerve; acetylcholine", "Vagus nerve; noradrenaline", "Sympathetic nerve; acetylcholine"], 1,
             "The vagus (parasympathetic) nerve releases acetylcholine and slows the heart.", hint="Parasympathetic nerves release acetylcholine.",
             feedback=["The sympathetic nerve speeds the heart.", "", "The vagus does not release noradrenaline.", "The sympathetic nerve releases noradrenaline."]),
        TIP("In Paper 2, link each ECG feature to a chamber and a pressure event. In Paper 1, expect order questions (SAN, AVN, bundle of His, Purkyne) and heart-rate calculations from R-to-R times.", title="Exam link"),
        PQ("(a) Explain what is meant by saying the heart is myogenic. (b) Describe how excitation spreads from the SAN to the apex of the heart.",
           "(a) The cardiac muscle itself starts each contraction without a stimulus from nerves. (b) The SAN in the right atrium starts a wave of excitation which spreads over both atria, causing atrial systole. A layer of fibrous tissue stops the wave crossing directly to the ventricles. The wave reaches the AVN, which delays it by about 0.1 s. It then passes down the bundle of His to the apex and up through the walls of the ventricles by the Purkyne fibres. The ventricles contract from the apex upwards."),
        PQ("An ECG has R peaks 0.5 s apart. Calculate the heart rate and suggest the condition.",
           "Heart rate = 60 ÷ 0.5 = 120 beats per minute. A resting rate over 100 is tachycardia (although a rate of 120 is normal in vigorous exercise)."),
        PQ("Explain how the body raises the heart rate when exercise starts.",
           "Muscles produce more CO₂ and lactate, so blood pH falls. Chemoreceptors in the carotid arteries and aorta detect this and send impulses to the cardiac centre in the medulla. The centre sends more impulses along the sympathetic nerve, which releases noradrenaline at the SAN, so the SAN fires faster. Adrenaline from the adrenal glands has the same effect. The higher heart rate raises cardiac output and delivers oxygen faster."),
        SUM("Cardiac muscle is myogenic: the SAN, in the right atrium, starts each beat and acts as the pacemaker.",
            "Excitation spreads over the atria, is delayed at the AVN, then passes via the bundle of His and Purkyne fibres to the ventricles, which contract from the apex upwards.",
            "On the ECG, P = atrial depolarisation, QRS = ventricular depolarisation, T = ventricular repolarisation. Heart rate = 60 ÷ R-to-R time in seconds.",
            "The cardiac centre in the medulla changes the rate: sympathetic nerve (noradrenaline) speeds up, vagus (acetylcholine) slows down.",
            "Adrenaline also increases heart rate and stroke volume."),
    ],
))

# ------------------------------------------------------------------ 5. Tissue fluid
LESSONS.append(lesson(
    module=M_GAS,
    topic="Tissue fluid formation",
    title="Tissue fluid: Starling's hypothesis, lymph and oedema",
    slug="bil3-tissue-fluid-starling",
    minutes=22,
    summary="How hydrostatic and oncotic pressures decide whether fluid leaves or enters a capillary, how lymph returns the excess, and why oedema occurs.",
    objectives=[
        "Describe the composition of tissue fluid and how it differs from blood plasma and lymph",
        "Explain Starling's hypothesis using hydrostatic and oncotic pressures along a capillary",
        "Calculate net filtration pressure from stated pressures",
        "Explain the role of the lymphatic system and at least three causes of oedema",
    ],
    key_concepts=["Tissue fluid", "Hydrostatic pressure", "Oncotic pressure", "Net filtration", "Lymph", "Oedema", "Plasma proteins", "Starling's hypothesis"],
    blocks=[
        H("Introduction"),
        T("Children in a village in the Far North with severe protein shortage (kwashiorkor) often have swollen bellies and legs. The swelling is not fat. It is fluid that has built up outside the capillaries. "
          "To understand why, we need to see how fluid normally leaves and returns to the blood."),
        H("What tissue fluid is"),
        D("**Tissue fluid** is the watery fluid that surrounds the cells of the body. It comes from blood plasma that has been filtered out through the capillary walls. It contains water, glucose, amino acids, oxygen, ions and some small proteins, but no red blood cells and few large plasma proteins.", title="Definition"),
        T("Cells exchange substances with the blood through the tissue fluid. Oxygen and nutrients pass from capillary to fluid to cell. Carbon dioxide and waste pass the other way. Capillary walls are one cell thick and have tiny gaps between the cells, so small molecules can leave but large proteins stay."),
        H("Starling's hypothesis"),
        T("Two opposing pressures decide the movement of fluid. **Hydrostatic pressure** is the pressure of the blood pushing against the capillary wall (it is produced by the heart). It pushes fluid OUT. "
          "**Oncotic pressure** is the effect of the plasma proteins in the blood: they lower the water potential of the plasma, so water tends to move into the capillary by osmosis. It pulls fluid IN. (Some textbooks write this as the water potential of the blood; check your textbook.)"),
        D("**Starling's hypothesis**: at the arteriole end of a capillary the hydrostatic pressure is greater than the oncotic pressure, so fluid is forced out. At the venule end the hydrostatic pressure has fallen below the oncotic pressure, so fluid returns by osmosis.", title="Starling's hypothesis"),
        F(r"\text{net filtration pressure} = \text{hydrostatic pressure} - \text{oncotic pressure}"),
        IMG("al-bil3-starling.svg", alt="Graph of hydrostatic pressure falling from 4.5 to 2.0 kilopascals along a capillary and a constant oncotic pressure of 3.0 kilopascals, with net outward movement near the arteriole end and net inward movement near the venule end",
            caption="Figure 1. Pressures along a capillary (teaching values: hydrostatic 4.5 to 2.0 kPa, oncotic 3.0 kPa; real values vary between tissues)."),
        EX("Worked example 1: net pressure at each end", intro="Use the values in Figure 1. Find the net filtration pressure at the arteriole end (hydrostatic 4.5 kPa) and the venule end (2.0 kPa), and state the direction of fluid movement.", steps=[
            S("Arteriole end", math=r"4.5 - 3.0 = +1.5 \text{ kPa}", text="Positive: fluid leaves the capillary."),
            S("Venule end", math=r"2.0 - 3.0 = -1.0 \text{ kPa}", text="Negative: fluid enters the capillary."),
        ]),
        EX("Worked example 2: where the movement reverses", intro="If the hydrostatic pressure falls in a straight line from 4.5 to 2.0 kPa along the capillary, how far along (as a fraction of its length) does the net movement change direction?", steps=[
            S("Pressure change over the full length", math=r"4.5 - 2.0 = 2.5 \text{ kPa}"),
            S("The pressure must fall from 4.5 to 3.0", math=r"4.5 - 3.0 = 1.5 \text{ kPa}"),
            S("Fraction of the length", math=r"\frac{1.5}{2.5} = 0.60", text="The movement changes direction 0.6 (60%) of the way along the capillary."),
        ]),
        H("The lymphatic system"),
        T("More fluid leaves the capillaries than returns by osmosis (in Figure 1 the outward region is larger than the inward region). The extra fluid (a few litres a day in a person; check your textbook for the figure) drains into **lymph capillaries**. "
          "Once inside, the fluid is called **lymph**. Lymph vessels join to form larger vessels with one-way valves. Lymph is moved by squeezing from nearby muscles and body movements, and it returns to the blood near the heart at the subclavian veins."),
        T("Lymph is like tissue fluid but it contains more fats (from the intestine) and many lymphocytes. Lymph nodes along the vessels filter bacteria and make lymphocytes."),
        H("Oedema"),
        D("**Oedema** is a build-up of excess tissue fluid causing swelling.", title="Definition"),
        KEY("Causes of oedema", "Each cause upsets the Starling balance or blocks the drainage.", cards=[
            ["Low plasma protein", "Starvation (kwashiorkor) or liver disease means less plasma protein, so oncotic pressure falls. Less fluid returns to the capillary."],
            ["High blood pressure or heart failure", "Hydrostatic pressure rises (the venous pressure backs up), so more fluid is pushed out."],
            ["Blocked lymph vessels", "Fluid cannot drain away. In lymphatic filariasis, parasitic worms block lymph vessels and cause gross swelling of the legs."],
            ["Inflammation", "Capillary walls become more leaky, so proteins and fluid escape (swelling in an infected cut)."],
        ]),
        MISTAKE("Saying that osmosis pushes fluid out of the capillary", "Fluid leaves by pressure filtration, driven by hydrostatic pressure. Osmosis (the oncotic pressure) draws it back in. Do not swap the two."),
        MISTAKE("Forgetting that the pressure falls along the capillary", "Hydrostatic pressure drops because of friction and because fluid has left, which is why the balance changes between the two ends. Oncotic pressure stays almost the same."),
        QUIZ("Which row correctly describes events at the venule end of a capillary?", ["Hydrostatic pressure is higher than oncotic pressure; fluid leaves", "Hydrostatic pressure is lower than oncotic pressure; fluid enters", "Hydrostatic pressure equals zero; fluid is unaffected", "Oncotic pressure is lower; fluid enters"], 1,
             "At the venule end the hydrostatic pressure has fallen below the oncotic pressure, so water returns by osmosis.", hint="Which pressure falls along the capillary?",
             feedback=["That describes the arteriole end.", "", "Hydrostatic pressure does not fall to zero in a capillary.", "Oncotic pressure stays roughly constant and it is higher than the hydrostatic pressure at the venule end."]),
        QUIZ("A person has a very low concentration of plasma protein. What is the most likely result?", ["Less tissue fluid forms and the person is dehydrated", "More tissue fluid stays outside the capillary, causing oedema", "Blood pressure rises", "Lymph flow stops"], 1,
             "Low plasma protein reduces the oncotic pressure, so less fluid is drawn back into the capillary and it accumulates.", hint="Which pressure draws fluid into the capillary?",
             feedback=["Less oncotic pressure would let more fluid stay out, not form less.", "", "Low plasma protein does not cause a rise in pressure in the main arteries.", "Lymph flow would, if anything, increase."]),
        TIP("Starling's hypothesis appears as a Paper 1 reasoning question and as a part of a Paper 2 question. A graph of two pressures is common: compare the lines at each end of the capillary and state the net direction of fluid, with the values.", title="Exam link"),
        PQ("Explain how tissue fluid is formed and how most of it returns to the circulation.",
           "At the arteriole end the hydrostatic pressure of blood is higher than the oncotic pressure of the plasma proteins, so water and small molecules are forced out through the capillary wall, forming tissue fluid. Large proteins and cells stay in. At the venule end the hydrostatic pressure has fallen below the oncotic pressure, so water returns by osmosis. The excess that does not return drains into lymph capillaries and is returned to the blood through the lymph vessels near the heart."),
        PQ("A capillary has a hydrostatic pressure of 3.6 kPa and an oncotic pressure of 3.0 kPa at one point. Calculate the net filtration pressure and state what happens to fluid there.",
           "Net filtration pressure = 3.6 − 3.0 = +0.6 kPa. Positive, so there is net movement of fluid out of the capillary."),
        PQ("Suggest why a child with kwashiorkor has a swollen abdomen.",
           "The diet lacks protein, so the liver makes less plasma protein. The oncotic pressure of the blood falls. Less water is drawn back into the capillaries at the venule end, so tissue fluid accumulates and fluid collects in the abdomen as oedema."),
        SUM("Tissue fluid is plasma minus the large proteins and cells, filtered through capillary walls.",
            "Net filtration pressure = hydrostatic pressure − oncotic pressure. Fluid leaves at the arteriole end and re-enters at the venule end.",
            "Excess fluid drains into lymph capillaries and returns to the blood near the heart.",
            "Oedema results from low plasma protein, high capillary pressure, blocked lymph vessels or leaky capillaries."),
    ],
))

# ------------------------------------------------------------------ 6. Water transport in plants
LESSONS.append(lesson(
    module=M_GAS,
    topic="Water transport in plants",
    title="Water transport in plants: apoplast, symplast and the cohesion-tension theory",
    slug="bil3-water-transport-plants",
    minutes=25,
    summary="How water crosses the root by the apoplast and symplast pathways, how it rises in the xylem by cohesion and tension, and how transpiration is measured with a potometer.",
    objectives=[
        "Use water potential (Ψ = Ψs + Ψp) to predict the direction of water movement between cells",
        "Describe the apoplast, symplast and vacuolar pathways and the role of the endodermis and Casparian strip",
        "Explain the cohesion-tension theory and give evidence for it",
        "Explain how environmental factors affect transpiration and calculate transpiration rate from potometer data",
    ],
    key_concepts=["Water potential", "Apoplast", "Symplast", "Casparian strip", "Xylem", "Cohesion", "Adhesion", "Transpiration", "Potometer"],
    blocks=[
        H("Introduction"),
        T("A cocoa tree in the forest near Ebolowa lifts hundreds of litres of water from the soil to its leaves in a year, with no pump and no heart. The tallest trees lift water 100 m or more. "
          "This lesson explains how, in three stages: across the root, up the xylem, and out of the leaf."),
        H("Water potential in cells"),
        D("**Water potential (Ψ)** is a measure of the tendency of water molecules to move from one place to another. It is measured in kilopascals (kPa) or megapascals (MPa). Pure water at standard conditions has the highest value, 0. Solutions and cell sap have negative values.", title="Definition: water potential"),
        F(r"\Psi = \Psi_s + \Psi_p"),
        T("**Solute potential (Ψs)** is always negative: dissolved solutes reduce the water potential. **Pressure potential (Ψp)** is the pressure exerted by the cell wall on the contents of a turgid cell; it is positive. "
          "Water always moves from a region of **higher** (less negative) water potential to one of **lower** (more negative) water potential, by osmosis, down the water potential gradient."),
        EX("Worked example 1: direction of water movement", intro="Cell X has Ψs = −0.9 MPa and Ψp = +0.4 MPa. Cell Y next to it has Ψs = −1.1 MPa and Ψp = +0.2 MPa. In which direction does water move?", steps=[
            S("Water potential of X", math=r"\Psi_X = -0.9 + 0.4 = -0.5 \text{ MPa}"),
            S("Water potential of Y", math=r"\Psi_Y = -1.1 + 0.2 = -0.9 \text{ MPa}"),
            S("Compare", text="Ψ of X (−0.5) is higher than Ψ of Y (−0.9), so water moves from X to Y."),
        ], check=r"-0.5 > -0.9"),
        H("Across the root: three pathways"),
        T("Root hair cells absorb water from the soil by osmosis. Their huge number, and the extensive root system, give a large surface area. The water then crosses the **cortex** to the **xylem** in the centre by three routes."),
        KEY("Pathways across the cortex", "The first two are the main routes.", cards=[
            ["Apoplast pathway", "Water moves through the cell walls and the spaces between the cells. Cellulose walls are porous and water moves by mass flow and capillary action. It does not cross a membrane."],
            ["Symplast pathway", "Water moves through the cytoplasm of the cells, which are linked by strands called plasmodesmata. It crosses the cell surface membrane once, by osmosis."],
            ["Vacuolar pathway", "Water passes from vacuole to vacuole, crossing membranes (tonoplast and cell membrane) each time. It is slower."],
        ]),
        T("At the inner edge of the cortex, the **endodermis** is a ring of cells. The walls of its cells contain a waterproof band of **suberin**, the **Casparian strip**. The strip blocks the apoplast pathway. Water must enter the cytoplasm of the endodermal cells and continue by the symplast route. "
          "This gives the plant control over which substances enter the xylem, because the membrane of the endodermis can select. It also lets the root actively pump mineral ions into the xylem, lowering its water potential. Water then follows by osmosis. This is the origin of **root pressure**."),
        IMG("al-bil3-water-potential.svg", alt="Staircase of boxes showing water potential falling from soil water at -0.3 to root hair -0.6, root cortex -0.9, root xylem -1.2, leaf cells -1.5 and outside air at -30 megapascals",
            caption="Figure 1. A water potential gradient from soil to air (invented teaching values; the drop into dry air is far larger than the others)."),
        H("Up the xylem: the cohesion-tension theory"),
        T("Xylem vessels are dead, hollow tubes with no end walls, and their walls are strengthened with lignin. Water moves up them by mass flow. Root pressure is small and works mainly when transpiration is low (for example at night), so it cannot be the main force. The main force is at the top of the plant."),
        KEY("Cohesion-tension theory", "Follow the chain from the leaf to the root.", cards=[
            ["1. Transpiration", "Water evaporates from the surface of the mesophyll cell walls in the leaf into the air spaces. Vapour diffuses out through the open stomata."],
            ["2. Pull (tension)", "The loss lowers the water potential of the leaf cells, so water is drawn from the xylem. This produces tension (negative pressure) in the xylem, pulling the water column up."],
            ["3. Cohesion", "Water molecules are hydrogen-bonded to each other (cohesion), so the column does not break and is pulled up as one."],
            ["4. Adhesion", "Water molecules are attracted to the lignin and cellulose of the xylem walls (adhesion), which helps to hold the column up and enables capillary action."],
        ]),
        D("**Transpiration** is the loss of water vapour from the aerial parts of a plant, mainly through the stomata. The continuous flow from root to leaf is the **transpiration stream**.", title="Definition: transpiration"),
        T("**Evidence for the theory.** The diameter of a tree trunk shrinks slightly in the day when transpiration is high, because the xylem is under tension. If a xylem vessel is cut, air is sucked in rather than water leaking out. "
          "A cut stem sealed in a dye solution draws the dye upward. Water does not rise if the leaf is covered by grease (stomata blocked)."),
        H("Factors affecting transpiration"),
        T("**Light** opens the stomata, so transpiration rises. **Temperature** raises the kinetic energy of the water molecules and lowers the humidity of the air, so evaporation rises. "
          "**Humidity**: in humid air the gradient is smaller, so transpiration falls. **Wind** removes the humid layer near the leaf, so transpiration rises. A lack of soil water makes the guard cells lose turgor, and the stomata close. "
          "Plants adapted to dry places (xerophytes) reduce water loss by thick cuticles, sunken stomata, hairs and rolled leaves."),
        H("Measuring water uptake: the potometer"),
        T("A **potometer** measures how fast a cut shoot takes up water. An air bubble in a capillary tube moves as the shoot takes up water. Because most water taken up is lost by transpiration, uptake is used as an estimate of transpiration. "
          "The volume taken up equals the cross-sectional area of the tube times the distance moved by the bubble: **V = πr²d**."),
        EX("Worked example 2: transpiration rate", intro="In a potometer with a capillary tube of radius 0.5 mm, the bubble moves 36 mm in 10 minutes. Calculate the rate of water uptake in mm³ per minute.", steps=[
            S("Volume taken up", math=r"V = \pi r^2 d = \pi \times 0.5^2 \times 36 = 28.3 \text{ mm}^3"),
            S("Rate", math=r"\frac{28.3}{10} = 2.8 \text{ mm}^3 \text{ min}^{-1}"),
        ], check=r"\pi (0.5)^2 (36) = 28.27"),
        MISTAKE("Saying water is pushed up from the roots", "Root pressure is small and cannot raise water in a tall tree. The main force is the pull (tension) from transpiration, using the cohesion of water molecules. State the chain: transpiration, tension, cohesion."),
        QUIZ("In which pathway does water move through cell walls without crossing a membrane?", ["Symplast", "Vacuolar", "Apoplast", "Plasmodesmata"], 2,
             "The apoplast pathway is through the cell walls and the spaces between cells.", hint="Which pathway is blocked by the Casparian strip?",
             feedback=["The symplast pathway goes through the cytoplasm, crossing the cell membrane.", "The vacuolar pathway crosses membranes each time.", "", "Plasmodesmata are the strands that link the cytoplasm of cells in the symplast route."]),
        QUIZ("Which statement about the cohesion-tension theory is correct?", ["Water molecules are pushed up by the roots", "Hydrogen bonds between water molecules help to keep the water column unbroken", "Phloem sap is pulled by the xylem", "Xylem vessels are living cells that pump water"], 1,
             "Cohesion between hydrogen-bonded water molecules lets the column be pulled up without breaking.", hint="What attracts water molecules to each other?",
             feedback=["That describes root pressure, which is minor.", "", "Phloem and xylem carry different substances.", "Xylem vessels are dead."]),
        TIP("Water transport is common in Paper 1 (pathways, potometer calculations) and Paper 2 (cohesion-tension explanation). Paper 3 practical work often uses a potometer or a simple transpiration experiment, so know the precautions: cut the shoot under water, keep the apparatus airtight and keep conditions constant.", title="Exam link"),
        PQ("Explain how water moves from the soil to the xylem in a root and why the endodermis is important.",
           "Root hair cells have a lower water potential than the soil water, so water enters by osmosis. It crosses the cortex by the apoplast pathway (cell walls), the symplast pathway (cytoplasm through plasmodesmata) and the vacuolar pathway. At the endodermis the Casparian strip (suberin) blocks the apoplast route, so all the water must pass through the cytoplasm and membrane of the endodermal cells. This lets the plant control what enters the xylem and allows ions to be actively pumped in, lowering the water potential of the xylem so water follows by osmosis."),
        PQ("A cell has Ψs = −1.2 MPa and Ψp = +0.5 MPa. A neighbouring cell has Ψ = −0.5 MPa. State the direction in which water moves and explain.",
           "Ψ of the first cell = −1.2 + 0.5 = −0.7 MPa. The second cell has Ψ = −0.5 MPa, which is higher (less negative). Water moves from the second cell to the first, down the water potential gradient."),
        PQ("Describe the cohesion-tension theory and give one piece of evidence for it.",
           "Water evaporates from the mesophyll cell walls and diffuses out through the stomata (transpiration). This lowers the water potential of the leaf cells and draws water from the xylem, producing tension. Hydrogen bonds between water molecules (cohesion) keep the water column continuous, and adhesion to the xylem walls helps to support it. The whole column is pulled up. Evidence: the diameter of a tree trunk decreases when transpiration is high; air enters instead of water if a xylem vessel is cut."),
        SUM("Water moves from higher (less negative) to lower (more negative) water potential; Ψ = Ψs + Ψp.",
            "Across the root, water uses the apoplast, symplast and vacuolar pathways; the Casparian strip blocks the apoplast route at the endodermis.",
            "In the xylem water rises by transpiration pull, with tension, cohesion (hydrogen bonds) and adhesion.",
            "Light, temperature, wind and low humidity increase transpiration.",
            "A potometer measures uptake: V = πr²d, divided by time for a rate."),
    ],
))

# ------------------------------------------------------------------ 7. Phloem transport
LESSONS.append(lesson(
    module=M_GAS,
    topic="Phloem transport",
    title="Phloem transport: translocation and the mass flow hypothesis",
    slug="bil3-phloem-mass-flow",
    minutes=22,
    summary="How sucrose is loaded into sieve tubes, how pressure drives mass flow from source to sink, and what experiments show about translocation.",
    objectives=[
        "Describe the structure of sieve tube elements and companion cells",
        "Explain the mass flow (pressure flow) hypothesis, including active loading and unloading",
        "Define source and sink and give examples",
        "Evaluate the evidence for and against mass flow and calculate a rate of translocation",
    ],
    key_concepts=["Phloem", "Sieve tube element", "Companion cell", "Translocation", "Source", "Sink", "Mass flow", "Sucrose"],
    blocks=[
        H("Introduction"),
        T("A sugar cane farmer near Mbandjock knows that the sweet juice collects in the stem. The sugars are made in the leaves by photosynthesis, but they are stored in the stem. "
          "**Translocation** is the movement of organic substances (mainly sucrose and amino acids) in the phloem. It is different from the movement of water in the xylem."),
        H("Structure of the phloem"),
        KEY("Two cell types", "They work as a pair.", cards=[
            ["Sieve tube elements", "Long living cells joined end to end. The end walls are perforated sieve plates. They have very little cytoplasm and no nucleus, so there is little to block the flow."],
            ["Companion cells", "Each sieve tube element is beside a companion cell with a nucleus, many mitochondria and dense cytoplasm. It carries out the metabolism for the sieve tube element, makes ATP and loads sucrose. Plasmodesmata link the two cells."],
        ]),
        D("A **source** is a region where sucrose is loaded into the phloem (such as a mature leaf, or a storage organ releasing sugars). A **sink** is a region where sucrose is removed and used or stored (such as roots, growing shoots, fruits and seeds).", title="Source and sink"),
        T("The direction of flow is from source to sink. It can change: a tuber is a sink while it fills with starch in the growing season, but a source when it sprouts."),
        H("The mass flow hypothesis"),
        T("The hypothesis, proposed by Münch, explains translocation as a flow driven by a **hydrostatic pressure gradient** between source and sink."),
        KEY("Mass flow in five steps", "Link each step to water potential.", cards=[
            ["1. Loading at the source", "Sucrose is actively loaded into the companion cell and then the sieve tube. In many plants hydrogen ions are pumped out of the companion cell using ATP, and sucrose re-enters with hydrogen ions through a co-transporter protein (co-transport)."],
            ["2. Water enters", "The sucrose lowers the water potential of the sieve tube. Water enters from the nearby xylem by osmosis. Hydrostatic pressure at the source end rises."],
            ["3. Mass flow", "Pressure at the source is higher than at the sink, so sap flows along the sieve tube down the pressure gradient (mass flow)."],
            ["4. Unloading at the sink", "Sucrose is removed (actively or by diffusion) and used in respiration or converted to starch. The water potential of the sieve tube rises, and water leaves by osmosis, lowering the pressure."],
            ["5. Water returns", "Water leaving at the sink goes back to the xylem and is carried to the leaves again."],
        ]),
        T("Mass flow carries everything dissolved in the sap together in one direction. It is much faster than diffusion, which is far too slow over the distance from a leaf to a root. "
          "Active loading needs ATP, so translocation stops if the companion cells are poisoned with a respiratory inhibitor or if the temperature drops very low."),
        H("Evidence from experiments"),
        KEY("Experiments", "Each supports a different part of the hypothesis.", cards=[
            ["Ringing (girdling)", "If a ring of bark (with phloem) is removed from a stem, sugars build up above the ring and the swelling shows downward flow. The xylem is unharmed so the tree continues to take up water for a time."],
            ["Aphid stylets", "An aphid inserts its mouthpart (stylet) into a sieve tube. If the aphid is cut away, sap flows out of the stylet under pressure, showing a positive hydrostatic pressure. The sap is rich in sucrose."],
            ["Radioactive tracer", "A leaf is given CO₂ containing radioactive carbon-14. Autoradiography then shows the carbon-14 in the phloem, and the speed can be measured."],
            ["Metabolic inhibitors", "Chemicals that stop ATP production in the companion cells stop translocation, showing that active steps are needed."],
        ]),
        T("**Evidence against or difficulties.** Sieve plates would resist flow, and it is not clear how the sap passes them. Different substances in the same tube sometimes move at different speeds, which mass flow does not predict. "
          "Not all sieve tubes show a pressure difference. Some textbooks stress these points; check your textbook."),
        EX("Worked example 1: rate of translocation", intro="Carbon-14 supplied to a leaf is detected 60 cm lower down the stem 40 minutes later. Calculate the rate in cm per hour and in metres per hour.", steps=[
            S("Rate in cm per minute", math=r"\frac{60}{40} = 1.5 \text{ cm min}^{-1}"),
            S("Rate in cm per hour", math=r"1.5 \times 60 = 90 \text{ cm h}^{-1}"),
            S("In metres per hour", math=r"\frac{90}{100} = 0.9 \text{ m h}^{-1}", text="This is of the order of the speeds in the textbooks (about 0.5 to 1 m per hour in many plants), much faster than diffusion could achieve."),
        ], check=r"1.5 \times 60 = 90"),
        EX("Worked example 2: predicting a result", intro="A ring of bark is removed from the stem of a young plant below the lowest leaf. The leaves above are in the light. Predict what happens above and below the ring after several days, and explain.", steps=[
            S("Above the ring", text="The stem swells and sugar content rises. Sucrose arriving from the leaves cannot pass the ring, because the phloem has been removed."),
            S("Below the ring", text="Sugar supply stops. The roots below the ring are starved and the tissue below shrinks and eventually dies."),
            S("Conclusion", text="The phloem carries sucrose downward from the leaves. The xylem is intact, so the shoot above stays supplied with water for some time."),
        ]),
        MISTAKE("Mixing up phloem and xylem", "Xylem moves water and minerals upward in dead cells, driven by transpiration pull. Phloem moves organic solutes in living cells from source to sink, driven by pressure from active loading. They are different mechanisms."),
        MISTAKE("Saying that sucrose moves by osmosis", "Sucrose enters by active loading (co-transport). It is the WATER that moves by osmosis, which builds up the pressure that drives mass flow."),
        QUIZ("Which of the following best describes a sink?", ["A leaf making sucrose in bright light", "A growing root tip using sucrose in respiration", "The xylem vessel carrying water to the leaf", "A stoma losing water vapour"], 1,
             "A sink is any region that removes sucrose from the phloem for use or storage.", hint="Where does sucrose leave the phloem?",
             feedback=["A leaf making sucrose is a source.", "", "The xylem carries water, not sucrose.", "A stoma is not a sugar sink."]),
        QUIZ("Why does translocation stop if the companion cells are poisoned with a respiratory inhibitor?", ["Sucrose is no longer made in the leaf", "The cells cannot make ATP for active loading of sucrose", "Xylem vessels collapse", "Sieve plates become blocked by starch"], 1,
             "Active loading of sucrose needs ATP made by the companion cells, so mass flow stops without it.", hint="What does the proton pump need?",
             feedback=["Photosynthesis is not affected by a respiratory inhibitor.", "", "Xylem is not affected by an inhibitor of the companion cells.", "Nothing blocks sieve plates in this experiment."]),
        TIP("Phloem questions often give an experiment (ringing, aphids or radioactive carbon) and ask for an interpretation. Link every observation back to source, sink, pressure and active loading, and name the structure that carries the substance.", title="Exam link"),
        PQ("Describe the structure of a sieve tube element and explain how the companion cell helps it.",
           "A sieve tube element is a living cell with end walls perforated to form sieve plates. It has little cytoplasm, no nucleus and few organelles, so flow is not obstructed. The companion cell next to it has a nucleus and many mitochondria. It provides ATP and proteins, and loads sucrose into the sieve tube. The two are linked by plasmodesmata."),
        PQ("Explain the mass flow hypothesis for the movement of sucrose from a leaf to a root.",
           "Sucrose is actively loaded into the sieve tube at the leaf (the source), lowering its water potential. Water enters from the xylem by osmosis, so the hydrostatic pressure is high. At the root (the sink) sucrose is removed and used or stored, so water potential rises and water leaves, lowering the pressure. The sap flows down the pressure gradient from leaf to root in mass flow."),
        PQ("An aphid stylet is cut from the aphid and sap flows out of it. Explain what this suggests.",
           "The stylet is in a sieve tube. Sap flows out because it is under pressure, which supports the idea that the sieve tube contains positive hydrostatic pressure, as the mass flow hypothesis says. The sap contains sucrose."),
        SUM("Phloem sieve tube elements are living cells with sieve plates; companion cells supply ATP and load sucrose.",
            "Translocation is the movement of sucrose and other organic solutes from sources to sinks.",
            "Mass flow: active loading lowers water potential, water enters by osmosis, pressure builds, sap flows to the sink, and unloading releases pressure.",
            "Evidence: ringing, aphid stylets, radioactive tracers and metabolic inhibitors; difficulties include the sieve plates and different speeds of solutes.",
            "Rates are calculated as distance ÷ time."),
    ],
))

# ------------------------------------------------------------------ 8. Energy flow and productivity
LESSONS.append(lesson(
    module=M_ECO,
    topic="Energy flow and productivity",
    title="Energy flow, gross and net primary productivity and ecological efficiency",
    slug="bil3-energy-flow-productivity",
    minutes=24,
    summary="How energy enters and leaves an ecosystem, how GPP, respiration and NPP are related, why only about a tenth passes between trophic levels, and how efficiencies are calculated.",
    objectives=[
        "Trace the flow of energy from the Sun to decomposers in a named ecosystem",
        "Define and calculate gross primary productivity, net primary productivity and net production of consumers",
        "Calculate the efficiency of energy transfer between trophic levels and give reasons for energy loss",
        "Interpret pyramids of number, biomass and energy",
    ],
    key_concepts=["Trophic level", "Gross primary productivity", "Net primary productivity", "Respiration loss", "Ecological efficiency", "Pyramid of energy", "Decomposer", "Assimilation"],
    blocks=[
        H("Introduction"),
        T("In the Board's 2023 report, candidates who were asked to trace the flow of energy in a named ecosystem often drew only a bare food chain starting with the Sun. "
          "They lost marks because they named no ecosystem, gave no organisms that really live there, and did not say where energy is lost. "
          "This lesson gives you the vocabulary and the calculations to do it properly."),
        H("Energy enters and leaves, matter cycles"),
        T("Energy flows through an ecosystem in one direction: from the Sun, into producers, along food chains and out as heat. It is not recycled. Matter (such as carbon and nitrogen) is recycled. "
          "Producers capture only a small fraction of the light that falls on them (a few percent at most; check your textbook), because most light is reflected, passes through the leaf, is the wrong wavelength or falls on non-photosynthetic parts."),
        D("A **trophic level** is the position of an organism in a food chain, counted by the number of feeding steps from the producer: producers, primary consumers, secondary consumers and so on. **Decomposers** (bacteria and fungi) feed on dead material and waste at every level.", title="Definition: trophic level"),
        H("Productivity"),
        D("**Gross primary productivity (GPP)** is the total energy fixed by photosynthesis in producers, per unit area per unit time. **Net primary productivity (NPP)** is the energy that remains after the producers have used some in their own respiration (R). It is the energy available to consumers and decomposers.", title="Definitions"),
        F(r"\text{NPP} = \text{GPP} - R"),
        T("Productivity is given in kJ m⁻² year⁻¹ (energy per area per time) or g m⁻² year⁻¹ (dry mass). The word **productivity** always involves time. **Biomass** is the dry mass of living material at one moment, with no time."),
        IMG("al-bil3-energy-flow.svg", alt="Energy flow diagram: GPP 25000 loses 10000 to respiration leaving net primary productivity 15000, 10 percent passes to primary consumers (1500), 10 percent of that to secondary consumers (150), and dead material passes to decomposers",
            caption="Figure 1. Energy flow in a food chain, kJ m⁻² year⁻¹ (invented teaching data)."),
        T("For consumers the equivalent equation is **net production = assimilation − respiration**. The energy a consumer eats (ingestion) is not all assimilated: the part that is not digested leaves in the faeces."),
        D("**Efficiency of energy transfer** between trophic levels = (energy in the higher level ÷ energy in the lower level) × 100. In many food chains it is around 10% (it varies between about 5% and 20%; check your textbook).", title="Ecological efficiency"),
        EX("Worked example 1: productivity and transfer", intro="A grassland has GPP of 25 000 kJ m⁻² year⁻¹ and plant respiration of 10 000. Primary consumers gain 1 500 and secondary consumers gain 150. Calculate (a) the NPP, (b) the percentage of GPP that is NPP and (c) the efficiency of transfer from producers to primary consumers and from primary to secondary consumers.", steps=[
            S("NPP", math=r"25\,000 - 10\,000 = 15\,000 \text{ kJ m}^{-2}\text{ year}^{-1}"),
            S("NPP as % of GPP", math=r"\frac{15\,000}{25\,000} \times 100 = 60\%"),
            S("Producers to primary consumers", math=r"\frac{1500}{15\,000} \times 100 = 10\%"),
            S("Primary to secondary", math=r"\frac{150}{1500} \times 100 = 10\%"),
        ], check=r"15000 \times 0.1 = 1500"),
        EX("Worked example 2: a herd of goats", intro="A herd of goats eats grass containing 600 kJ per unit area. They lose 200 kJ in faeces and 320 kJ in respiration. Calculate the assimilation, the net production and the net production efficiency (net production ÷ assimilation × 100). (Invented data.)", steps=[
            S("Assimilation", math=r"600 - 200 = 400 \text{ kJ}"),
            S("Net production", math=r"400 - 320 = 80 \text{ kJ}"),
            S("Net production efficiency", math=r"\frac{80}{400} \times 100 = 20\%"),
        ]),
        H("Why is so much energy lost?"),
        KEY("Reasons for loss at each level", "A good answer gives at least three, with the destination of the energy.", cards=[
            ["Not eaten", "Roots, bones, wood or fur are not eaten. They pass to decomposers when the organism dies."],
            ["Not digested", "Part of the food is egested in the faeces, which go to decomposers."],
            ["Respiration", "Much of the assimilated energy is used for movement, keeping warm, active transport and other life processes, and is lost as heat."],
            ["Excretion", "Energy remains in urea and other waste."],
        ]),
        T("Because of these losses, food chains are short, usually four or five links. Warm-blooded animals (birds and mammals) lose more energy as heat, so they convert a smaller share of their food into growth than cold-blooded animals do. "
          "Eating plants (for example maize or cassava) takes advantage of the first trophic level, where the energy is highest, so a given area of land can feed more people on crops than on meat."),
        H("Ecological pyramids"),
        T("A **pyramid of numbers** counts organisms at each level. It can be an odd shape: one large tree supporting thousands of insects gives an inverted pyramid. "
          "A **pyramid of biomass** uses the dry mass of each level at one time. It can be inverted in the sea, where tiny algae grow and are eaten rapidly. "
          "A **pyramid of energy** shows the energy passing through each level per unit area per year. It is always a true pyramid, because energy is lost at each step and a level cannot hold more energy than the one below it passes on."),
        MISTAKE("Drawing a food chain and calling it energy flow", "A food chain shows who eats whom. Energy flow shows how much energy enters each level and where it goes: into growth, into respiration (lost as heat), into faeces and dead material (decomposers). Name the ecosystem and organisms, and show losses with figures."),
        MISTAKE("Giving energy as a percentage with no area and time", "Productivity has units such as kJ m⁻² year⁻¹. Biomass has no time. Efficiency is a percentage with no unit."),
        QUIZ("A forest has GPP of 40 000 kJ m⁻² year⁻¹ and respiration of 24 000 kJ m⁻² year⁻¹. What is the NPP?", ["64 000", "16 000", "24 000", "1.67"], 1,
             "NPP = GPP − R = 40 000 − 24 000 = 16 000.", hint="Which quantity is left after the producers' own respiration?",
             feedback=["That adds the two quantities.", "", "That is the respiration loss, not the NPP.", "That is GPP ÷ R."]),
        QUIZ("Why is a pyramid of energy never inverted?", ["Because large organisms live at the top", "Because energy is lost at every transfer, so each level has less than the one below", "Because decomposers recycle energy", "Because biomass is always greatest at the top"], 1,
             "Energy is lost as heat, faeces and waste at each step, so a level cannot pass on more than it received.", hint="What happens to energy at each transfer?",
             feedback=["Size is irrelevant to the energy pyramid.", "", "Energy is not recycled; matter is.", "Biomass has nothing to do with this and is usually greatest at the base."]),
        TIP("Energy flow appears in Paper 1 as a calculation or a pyramid, and in Paper 2 as a narrative: trace the energy from the Sun in a named ecosystem, say how much is lost at each level and why, and finish with the decomposers.", title="Exam link"),
        PQ("Trace the flow of energy in a named ecosystem (for example a savanna in the north of Cameroon) from sunlight to decomposers.",
           "Sunlight energy is captured by the grasses (producers) by photosynthesis and stored as chemical energy; a small fraction of the light is used. Some of this GPP is lost as heat in respiration by the grasses; the rest is NPP. Grasshoppers or cattle (primary consumers) eat the grass. Some energy is lost in faeces, in respiration and in the parts that are not eaten. Lions or hawks (secondary consumers) eat the herbivores and again lose energy in respiration, faeces and uneaten parts. About 10% of the energy is passed to the next level, so there are few top predators. Dead organisms, faeces and wastes of all levels are used by decomposers (bacteria and fungi), which release the energy as heat by respiration."),
        PQ("In a lake the NPP of the algae is 9 000 kJ m⁻² year⁻¹. The small fish gain 810 and the large fish gain 90 kJ m⁻² year⁻¹. Calculate the efficiency of transfer at each step.",
           "Algae to small fish: 810 ÷ 9 000 × 100 = 9%. Small fish to large fish: 90 ÷ 810 × 100 = 11% (11.1%)."),
        PQ("Explain why a pyramid of biomass for a sea can be inverted but a pyramid of energy cannot.",
           "A biomass pyramid shows the mass at one moment. In the sea, tiny algae reproduce and are eaten very quickly, so their standing mass at any time can be less than the mass of the zooplankton that eat them. An energy pyramid shows the energy passing through each level over a year; the zooplankton cannot receive more energy than the algae produce, so the pyramid of energy is always wider at the base."),
        SUM("Energy flows one way through ecosystems (Sun, producers, consumers, heat); matter is recycled.",
            "NPP = GPP − R; for consumers, net production = assimilation − respiration.",
            "Efficiency of transfer = energy in the higher level ÷ energy in the lower level × 100; it is about 10% in many food chains.",
            "Energy is lost by uneaten parts, egestion, respiration and excretion, so food chains are short.",
            "Pyramids of energy are always upright; pyramids of numbers and biomass can be inverted."),
    ],
))

# ------------------------------------------------------------------ 9. Biogeochemical cycles
LESSONS.append(lesson(
    module=M_ECO,
    topic="Biogeochemical cycles",
    title="The carbon, nitrogen and phosphorus cycles",
    slug="bil3-biogeochemical-cycles",
    minutes=24,
    summary="How carbon, nitrogen and phosphorus move between air, soil, water and living things, the bacteria that carry out each step of the nitrogen cycle, and the effects of human activity.",
    objectives=[
        "Describe the carbon cycle and the processes that add or remove carbon dioxide",
        "Name and distinguish nitrogen fixation, ammonification, nitrification and denitrification, with the organisms involved",
        "Describe the phosphorus cycle and explain why it has no gas stage",
        "Explain the effects of human activity, such as deforestation, fertilisers and burning, on these cycles",
    ],
    key_concepts=["Carbon cycle", "Nitrogen fixation", "Ammonification", "Nitrification", "Denitrification", "Phosphorus cycle", "Decomposers", "Fertiliser"],
    blocks=[
        H("Introduction"),
        T("A farmer near Bafia grows groundnuts one year and maize the next. The maize that follows groundnuts grows better, without any added fertiliser. "
          "The reason is that groundnut roots carry bacteria that add nitrogen to the soil. **Biogeochemical cycles** describe how elements such as carbon, nitrogen and phosphorus pass between living things (bio), the air, water and rocks (geo) in chemical forms."),
        H("The carbon cycle"),
        T("The air contains about 0.04% carbon dioxide. Carbon moves between the air, living things and the oceans in these main processes."),
        KEY("Processes in the carbon cycle", "Learn which ones add and which remove CO₂.", cards=[
            ["Photosynthesis (removes CO₂)", "Producers (plants, algae, cyanobacteria) fix CO₂ into carbohydrates."],
            ["Feeding", "Carbon in organic compounds passes along food chains as consumers eat producers."],
            ["Respiration (adds CO₂)", "All living things, including decomposers, release CO₂ by respiration."],
            ["Decomposition", "Saprophytic bacteria and fungi break down dead matter and waste and release CO₂."],
            ["Combustion (adds CO₂)", "Burning wood and fossil fuels releases CO₂. Fossil fuels formed from dead organisms that did not decompose."],
            ["Dissolving in water", "CO₂ dissolves in oceans and lakes, and is used by aquatic producers or locked in the shells of marine organisms and in limestone."],
        ]),
        T("Human activity has increased the amount of CO₂ in the air by burning fossil fuels and by deforestation (burning and clearing forest reduces photosynthesis). The Congo Basin forest in the south and east of Cameroon is a large store of carbon. "
          "Carbon dioxide traps heat in the atmosphere (it is a greenhouse gas), which contributes to global warming."),
        H("The nitrogen cycle"),
        T("Nitrogen is part of proteins, nucleic acids and ATP. The air is 78% nitrogen gas (N₂), but plants and animals cannot use it, because the triple bond between the atoms is very strong. It must first be converted into ammonium or nitrate. Four processes, all done by bacteria, are involved. In the Board's 2023 report, candidates confused them, so learn each name with its change."),
        IMG("al-bil3-nitrogen-cycle.svg", alt="Nitrogen cycle diagram: nitrogen gas to organic nitrogen by fixation, organic nitrogen to ammonium by ammonification, ammonium to nitrite to nitrate by nitrification, nitrate to nitrogen gas by denitrification and nitrate taken up by roots to organic nitrogen",
            caption="Figure 1. The nitrogen cycle, with the main bacteria."),
        CODE("Process           Change                      Bacteria (examples)\n"
             "Fixation          N2 -> ammonium (NH4+)       Rhizobium (root nodules of legumes),\n"
             "                                              Azotobacter (free-living), Anabaena\n"
             "Ammonification    proteins/urea -> NH4+       Saprophytic bacteria and fungi\n"
             "Nitrification 1   NH4+ -> nitrite (NO2-)      Nitrosomonas\n"
             "Nitrification 2   nitrite -> nitrate (NO3-)   Nitrobacter\n"
             "Denitrification   nitrate -> N2 gas           Pseudomonas denitrificans\n"
             "                  (waterlogged soil, no oxygen)", "text", title="Table 1. Processes in the nitrogen cycle"),
        T("**Nitrogen fixation** by *Rhizobium* occurs in swellings (nodules) on the roots of legumes such as groundnut, cowpea and bean. The bacteria obtain carbohydrate from the plant, and the plant obtains ammonium: a mutualistic relationship. "
          "**Nitrification** needs oxygen, so it happens in well-aerated soil. **Denitrification** happens when soil is waterlogged and has little oxygen, and it wastes nitrate that farmers would like to keep. "
          "Plants absorb nitrate (and ammonium) through their roots and use it to make amino acids. Lightning and the Haber process in fertiliser factories also fix nitrogen."),
        H("The phosphorus cycle"),
        T("Phosphorus is in DNA, ATP and phospholipids. Unlike carbon and nitrogen it has **no gas stage**: it moves in the form of phosphate ions. Rocks slowly weather and release phosphate into the soil. Plants absorb phosphate and animals get it by eating plants. "
          "Decomposers return phosphate to the soil when organisms die. Some phosphate is washed into the sea and forms sediments, which take millions of years to become rock again. Because of this slow return, phosphate is often a limiting nutrient and farmers add phosphate fertilisers."),
        H("Human effects"),
        T("Heavy use of nitrogen and phosphorus fertilisers allows crops to grow better, but excess nitrate and phosphate are washed by rain into rivers and lakes, leading to **eutrophication** (see the later lesson on pollution). Planting legumes in rotation, or leaving land fallow, restores soil nitrogen without chemical fertilisers. "
          "Burning vegetation at the end of the dry season releases carbon dioxide and nitrogen oxides and removes the nutrients held in the plants."),
        EX("Worked example 1: matching bacteria to processes", intro="A soil sample is kept waterlogged for several weeks. The nitrate concentration falls and nitrogen gas is released. Name the process and the type of bacteria, and explain why it happens in waterlogged soil.", steps=[
            S("Process", text="Denitrification: nitrate is converted to nitrogen gas."),
            S("Bacteria", text="Denitrifying bacteria such as Pseudomonas denitrificans."),
            S("Why in waterlogged soil", text="Water fills the soil spaces, so there is little oxygen. These bacteria use nitrate instead of oxygen as an electron acceptor in respiration."),
        ]),
        EX("Worked example 2: crop rotation", intro="Explain how growing groundnuts one year increases the yield of maize in the following year.", steps=[
            S("Nitrogen fixation", text="Rhizobium in the root nodules of groundnut converts N₂ to ammonium, and the plant uses it."),
            S("After harvest", text="Roots and leaves left in the soil are decomposed (ammonification) and nitrified by Nitrosomonas and Nitrobacter, producing nitrate."),
            S("Result", text="The maize roots absorb nitrate and use it to make amino acids and proteins, so growth and yield improve."),
        ]),
        MISTAKE("Saying nitrogen fixation is the conversion of ammonia to nitrate", "That is nitrification. Fixation is the conversion of nitrogen gas (N₂) to ammonium (or ammonia). Learn each name with its starting and ending substance."),
        MISTAKE("Drawing the cycle with no annotation", "A diagram without the names of the bacteria and the changes earns very little. Label each arrow with the process, the organism and the chemical change."),
        QUIZ("Which bacteria convert nitrite to nitrate?", ["Nitrosomonas", "Nitrobacter", "Rhizobium", "Pseudomonas denitrificans"], 1,
             "Nitrobacter oxidises nitrite to nitrate; this is the second step of nitrification.", hint="Nitrosomonas does the first step of nitrification.",
             feedback=["Nitrosomonas converts ammonium to nitrite.", "", "Rhizobium fixes nitrogen gas in root nodules.", "Pseudomonas denitrificans converts nitrate to nitrogen gas."]),
        QUIZ("Why is the phosphorus cycle described as having no atmospheric stage?", ["Phosphorus is not used by plants", "Phosphorus compounds do not form a gas that is in significant amounts in air, so it moves through rock, soil, water and living things", "Phosphorus is only found in animals", "Phosphorus is fixed by bacteria from the air"], 1,
             "Phosphorus occurs as phosphate in rocks, soil and water rather than as a common atmospheric gas.", hint="Which two cycles in this lesson have a gas stage?",
             feedback=["Plants need it for DNA, ATP and membranes.", "", "It is found in plants as well, in DNA and membranes.", "Bacteria fix nitrogen, not phosphorus."]),
        TIP("The nitrogen cycle is a frequent Paper 2 question. Draw a labelled diagram, then add a sentence for each process naming the bacteria and the starting and ending compounds. Paper 1 tests the order of the processes and the conditions each needs (oxygen for nitrification, none for denitrification).", title="Exam link"),
        PQ("Describe the roles of bacteria in the nitrogen cycle.",
           "Nitrogen-fixing bacteria (Rhizobium in legume root nodules, Azotobacter free-living) convert nitrogen gas into ammonium. Saprophytic bacteria decompose proteins and urea in dead organisms and waste to ammonium (ammonification). Nitrifying bacteria oxidise ammonium to nitrite (Nitrosomonas) and nitrite to nitrate (Nitrobacter), in aerobic soil. Denitrifying bacteria (Pseudomonas denitrificans) convert nitrate to nitrogen gas in waterlogged anaerobic soil."),
        PQ("Explain how the carbon in a molecule of glucose in a leaf can return to the atmosphere. Give two different routes.",
           "Route 1: the glucose is used in respiration in the leaf cells, releasing CO₂. Route 2: the leaf is eaten by an animal, whose respiration releases CO₂; or the leaf dies and decomposers respire it and release CO₂; or the plant material is burned, releasing CO₂ by combustion."),
        PQ("Suggest why waterlogging of a field reduces its fertility for maize.",
           "Waterlogging removes oxygen from the soil. Nitrification stops, so less nitrate forms. Denitrifying bacteria convert the nitrate that is present to nitrogen gas, which escapes. The soil loses nitrate, and roots also receive less oxygen for respiration, so the crop yield falls."),
        SUM("Carbon enters living things by photosynthesis and returns by respiration, decomposition and combustion.",
            "Nitrogen cycle: fixation (N₂ to ammonium), ammonification, nitrification (ammonium to nitrite to nitrate) and denitrification (nitrate to N₂).",
            "Name the bacteria: Rhizobium and Azotobacter, Nitrosomonas, Nitrobacter, Pseudomonas denitrificans.",
            "Phosphorus has no gas stage; it moves as phosphate through rock, soil, water and living things.",
            "Deforestation, burning, fertilisers and drainage alter all three cycles."),
    ],
))

# ------------------------------------------------------------------ 10. Succession
LESSONS.append(lesson(
    module=M_ECO,
    topic="Ecological succession",
    title="Ecological succession: from pioneers to a climax community",
    slug="bil3-ecological-succession",
    minutes=22,
    summary="How communities change over time from pioneer species to a stable climax, the differences between primary and secondary succession, and how biomass, biodiversity and soil change.",
    objectives=[
        "Define succession, pioneer species, seral stage and climax community",
        "Distinguish primary from secondary succession with examples",
        "Describe the changes in the environment and community during succession",
        "Interpret data on species number and biomass during succession and explain how human activity can hold a community at a stage",
    ],
    key_concepts=["Succession", "Pioneer species", "Seral stage", "Climax community", "Primary succession", "Secondary succession", "Humus", "Plagioclimax"],
    blocks=[
        H("Introduction"),
        T("When a farmer near Mamfe leaves a maize field to rest, within weeks grasses and herbs invade it. After several years there are shrubs and young trees, and after decades the plot looks like the surrounding forest. "
          "This slow, predictable change in the community over time is called **succession**."),
        D("**Ecological succession** is the gradual, directional change in the species that make up a community over time, as one community modifies its environment and is replaced by another. Each stage is a **seral stage**. The final, relatively stable community is the **climax community**.", title="Definition: succession"),
        H("Primary and secondary succession"),
        KEY("Two kinds", "They differ in the starting point.", cards=[
            ["Primary succession", "Starts on a bare surface with no soil and no seeds, such as new volcanic rock, a lava flow or a newly exposed sand bank. Lava flows from eruptions of Mount Cameroon are a local example. It takes hundreds of years."],
            ["Secondary succession", "Starts where a community has been removed but soil, seeds and roots remain: an abandoned farm, a cleared forest or a burnt field. It is much faster, because the soil already exists."],
        ]),
        H("A typical sequence"),
        T("**Pioneer species** are the first to colonise. On bare rock they are lichens and mosses, and in water they are algae and floating plants. They have features such as small, light, wind-blown spores or seeds, tolerance to harsh conditions and fast growth. "
          "Lichens (a partnership between a fungus and an alga) release acids that weather rock. As they die and decompose, they form a thin layer of **humus** (organic matter) and a first soil. "
          "Mosses and then small herbs grow in it. Their roots hold the soil, and as they die the soil deepens and holds more water and minerals. Larger herbs and grasses follow, then shrubs, then trees. "
          "Each stage changes the environment in a way that suits the next community better than itself (**facilitation**) and the first species are shaded out and replaced."),
        IMG("al-bil3-succession.svg", alt="Graph over 200 years: the number of plant species rises from 0 to about 50 and levels off, while biomass rises more slowly at first and then steeply to 100 percent of the climax, with shaded bands for pioneer, herb and shrub, and woody and climax stages",
            caption="Figure 1. Changes in species number and biomass during a succession (invented teaching data)."),
        KEY("What changes during succession", "Most of these increase, but not all.", cards=[
            ["Soil", "Deeper, richer in humus, nutrients and water, with a larger number of decomposers."],
            ["Biodiversity", "Species number rises then levels off (it may fall slightly in the climax as a few dominant species shade the others)."],
            ["Biomass and structure", "Biomass increases; the community becomes layered (herbs, shrubs, canopy), giving more niches and habitats."],
            ["Productivity", "NPP is high in the middle stages. At the climax, GPP is about equal to respiration, so NPP is near zero and biomass stops increasing."],
            ["Stability", "Food webs become longer and more complex, so the community resists change better."],
        ]),
        T("The **climax community** depends on the climate and soil. In the wet southern region of Cameroon it is evergreen rainforest; in the savanna of the north it is grassland with scattered trees. It is more or less stable until the climate or soil changes."),
        H("Human influence"),
        T("When people hold a community at an earlier stage by repeated disturbance, it never reaches the natural climax. Grazing, cutting, burning and ploughing do this. The result is a **plagioclimax**. "
          "Much of the savanna in northern Cameroon is held by burning and grazing. If the fires stopped, many areas would develop more trees and shrubs (check your textbook for the regional details). Clearing forest for farming followed by fallow lets secondary succession restart."),
        EX("Worked example 1: reading the graph", intro="Use Figure 1. (a) At what time do the number of species and the biomass percentage have the same value on the graph? (b) Calculate the average rate of increase in species number between years 10 and 30.", steps=[
            S("Compare the values", text="At year 60 the species number is 35 and biomass is 35 (the curves cross). After that, the biomass value is greater."),
            S("Increase in species", math=r"20 - 5 = 15 \text{ species}"),
            S("Average rate", math=r"\frac{15}{30 - 10} = 0.75 \text{ species per year}"),
        ], check=r"15/20 = 0.75"),
        EX("Worked example 2: explaining the slow start", intro="Using Figure 1, explain why biomass increases slowly in the first 30 years but rapidly between years 30 and 100.", steps=[
            S("Early stages", text="The pioneer and herb stages have small plants and thin soil, so they hold little biomass."),
            S("Later stages", text="Deeper soil and more nutrients let shrubs and trees grow. Trees are large, woody and long-lived, so biomass rises steeply."),
            S("Calculation", math=r"\frac{70 - 10}{100 - 30} = 0.86 \text{ percentage points per year}", text="The average increase between years 30 and 100 is 0.86 percentage points of climax biomass per year, compared with only (10 − 0) ÷ 30 = 0.33 in the first 30 years."),
        ]),
        MISTAKE("Saying that the climax has no change", "The climax is relatively stable, but species still come and go and individual trees die and are replaced. There is no net directional change in the type of community."),
        MISTAKE("Saying that biodiversity always peaks at the climax", "Species number often peaks at an intermediate stage or levels off. Many textbooks note a slight decline in the final stage because a few large trees dominate. Answer from the data you are given."),
        QUIZ("Which of the following starts a PRIMARY succession?", ["A field abandoned after farming", "A forest cleared by felling", "A fresh lava flow", "A garden left unweeded"], 2,
             "Only a lava flow starts with no soil, so it begins as primary succession.", hint="Where is there no soil to start with?",
             feedback=["The soil, seeds and roots remain, so this is secondary succession.", "Soil remains, so it is secondary succession.", "", "Soil remains, so it is secondary succession."]),
        QUIZ("What is a pioneer species?", ["A species of the climax community", "The first species to colonise a bare area", "A species that eats the others", "A species that lives in the soil only"], 1,
             "Pioneers are the first colonisers; they tolerate harsh conditions and start to build soil.", hint="Think about the first lichens on a bare rock.",
             feedback=["That describes a climax species.", "", "Feeding relationships do not define a pioneer.", "Pioneers are not limited to soil."]),
        TIP("Succession appears in Paper 1 (definitions, primary or secondary) and Paper 2 (graphs of species and biomass). Practise describing a change with data: give the values and the time, and link each change to the soil or shading.", title="Exam link"),
        PQ("Describe and explain the changes that occur during the primary succession on bare rock.",
           "Lichens and mosses (pioneers) colonise first. They weather the rock and, when they die, are decomposed to form a thin layer of humus and soil. The soil retains water and minerals, so small herbs and grasses can grow. As they die the soil deepens and richer, so shrubs and then trees can grow and shade the earlier species out. The number of species and biomass increase. Soil, structure and food webs become more complex until a stable climax community forms."),
        PQ("Explain why secondary succession is faster than primary succession.",
           "In secondary succession the soil is already present, with nutrients, humus, seeds, roots and soil organisms. In primary succession the soil has to be formed first, from rock, by pioneer species, which takes a very long time."),
        PQ("A savanna is burned every year. Explain why trees do not become established.",
           "Annual fire kills tree seedlings and young shrubs, while grasses regrow from underground parts. This holds the community at the grassland stage (a plagioclimax), and prevents succession to woodland."),
        SUM("Succession is the directional change in a community over time, ending in a stable climax community.",
            "Primary succession starts on bare rock without soil; secondary succession starts where soil remains and is faster.",
            "Pioneers change the environment (soil, shade) and are replaced; soil depth, biomass and complexity increase.",
            "At the climax, GPP is about equal to respiration and NPP is near zero.",
            "Burning, grazing and cutting can hold a community at a plagioclimax."),
    ],
))

# ------------------------------------------------------------------ 11. Population dynamics
LESSONS.append(lesson(
    module=M_ECO,
    topic="Population dynamics",
    title="Population dynamics: growth curves, carrying capacity and predator-prey cycles",
    slug="bil3-population-dynamics",
    minutes=25,
    summary="What makes a population grow or shrink, the logistic growth curve and carrying capacity, density-dependent and independent factors, predator-prey oscillations, and capture-recapture estimates.",
    objectives=[
        "Define population, carrying capacity and the factors that change population size",
        "Describe and explain the stages of a population growth curve",
        "Distinguish density-dependent from density-independent factors, and r- from K-strategists",
        "Explain predator-prey oscillations and estimate a population by capture-recapture",
    ],
    key_concepts=["Population", "Carrying capacity", "Exponential growth", "Logistic growth", "Density-dependent factor", "Density-independent factor", "Predator-prey cycle", "Capture-recapture"],
    blocks=[
        H("Introduction"),
        T("In the dry season, an area of grass in the Waza region supports a certain number of antelopes. In a good rainy season, their numbers rise. In a drought, they fall. "
          "**Population dynamics** is the study of how and why the size of a population changes."),
        D("A **population** is a group of organisms of the same species living in the same place at the same time. The **carrying capacity (K)** is the maximum population size that an environment can support over a long time, given its resources (food, water, space).", title="Definitions"),
        F(r"\text{change in population} = (\text{births} + \text{immigration}) - (\text{deaths} + \text{emigration})"),
        H("Population growth curves"),
        IMG("al-bil3-logistic.svg", alt="S-shaped logistic population growth curve levelling off at a carrying capacity of 1000, with a dashed exponential curve that rises far above it",
            caption="Figure 1. Logistic growth (solid) compared with exponential growth (dashed). Teaching values: N0 = 50, r = 0.5, K = 1000."),
        T("When a few individuals enter a new habitat with plenty of food, space and no predators, the population grows slowly at first (few parents), then faster and faster. The growth is **exponential**, because each generation is larger than the last. "
          "In real life it cannot go on for ever. Food, space, water and light run short, and disease and predators increase. This is called **environmental resistance**. Growth slows and the population levels off around the carrying capacity K."),
        KEY("Phases of the S-shaped (sigmoid) curve", "Each phase has a reason.", cards=[
            ["Slow growth", "A small number of breeding individuals, and time to adjust to the new habitat."],
            ["Exponential growth", "Resources are plentiful. Births exceed deaths. The rate rises as the population rises."],
            ["Slowing", "Resources become limiting. Competition, predation and disease reduce birth rate and raise death rate."],
            ["Stationary phase", "Births plus immigration equal deaths plus emigration. The population fluctuates around K."],
        ]),
        F(r"\frac{dN}{dt} = rN\,\frac{K - N}{K}", title="Logistic growth model (the rate of change of population size N)"),
        T("Here **r** is the maximum rate of increase per individual per unit time. The rate is largest at about K ÷ 2, where the population is half the carrying capacity, and it is zero at K."),
        EX("Worked example 1: growth rates on the logistic curve", intro="A population has r = 0.5 per generation and K = 1000. Calculate the growth rate dN/dt when N = 100, N = 500 and N = 900.", steps=[
            S("N = 100", math=r"0.5 \times 100 \times \frac{1000 - 100}{1000} = 45"),
            S("N = 500", math=r"0.5 \times 500 \times \frac{1000 - 500}{1000} = 125"),
            S("N = 900", math=r"0.5 \times 900 \times \frac{1000 - 900}{1000} = 45", text="The growth rate is greatest at N = K ÷ 2 = 500 and is the same at 100 and 900, as the curve is symmetric."),
        ], check=r"0.5(500)(0.5) = 125"),
        H("Limiting factors"),
        KEY("Two kinds of limiting factor", "The effect depends on whether it changes with the density of the population.", cards=[
            ["Density-dependent", "The effect rises as the population gets denser: competition for food, space and mates, predation, parasitism and disease, and build-up of waste. They give negative feedback and keep the population near K."],
            ["Density-independent", "The effect does not depend on the population size: floods, fire, drought, frost, cyclones or a cut in a river by a dam. They can cause sudden crashes."],
        ]),
        T("Species follow different strategies. **r-strategists** (many insects, weeds, bacteria) are small, mature early, produce many offspring with little care, and thrive in unstable habitats. "
          "**K-strategists** (elephants, gorillas, large trees) are large, mature slowly, produce few young with a lot of parental care, and live close to carrying capacity in stable habitats. K-strategists recover slowly from hunting."),
        H("Predator and prey"),
        IMG("al-bil3-predprey.svg", alt="Two oscillating curves over time: the prey population (blue) peaks first and the predator population (orange) peaks a little later",
            caption="Figure 2. A model of predator-prey cycles (computed from a Lotka-Volterra model with stated teaching parameters)."),
        T("In many systems the numbers of predators and prey rise and fall in repeating cycles, with the **predator peak lagging behind the prey peak**. "
          "(i) Prey numbers rise, so there is more food for predators. (ii) Predator numbers rise a little later and eat more prey. (iii) Prey numbers fall, so predators starve and their numbers fall. (iv) With fewer predators, the prey recover and the cycle starts again. "
          "A well-known example is the snowshoe hare and lynx in Canada. Real cycles also depend on food supply, disease and weather, and a predator with other food sources may not show the cycle. Check your textbook for the cases you are expected to know. "
          "Two species that need the same limited resource also compete. **Gause's competitive exclusion principle** says two species with identical niches cannot live together for long: one will exclude the other. Gause showed this with two species of Paramecium (single-celled organisms) grown in one culture tube."),
        H("Estimating population size"),
        T("To estimate the size of a mobile animal population, the **capture-recapture** (mark-release-recapture) method is used. Animals are caught, marked in a harmless way and released. After they have mixed with the rest, a second sample is taken."),
        F(r"N = \frac{M \times C}{R}", title="Lincoln index"),
        T("M is the number marked in the first sample, C is the number caught in the second sample, and R is the number of marked animals in the second sample. "
          "It assumes that marking does not harm or change the behaviour of the animals, that marked animals mix at random, and that there is no immigration, emigration, birth or death during the study."),
        EX("Worked example 2: capture-recapture", intro="Forty fish in a pond are caught, marked and released. A week later, 50 fish are caught, and 10 of them have marks. Estimate the population size.", steps=[
            S("Substitute", math=r"N = \frac{40 \times 50}{10}"),
            S("Calculate", math=r"N = 200 \text{ fish}", text="One fifth of the second sample is marked, so the 40 marked fish are about one fifth of the whole population."),
        ], check=r"40 \times 50 / 10 = 200"),
        MISTAKE("Calling every limiting factor density-dependent", "A flood kills the same share of a population whether it is dense or sparse, so it is density-independent. Only factors whose effect changes with density (competition, disease, predation) are density-dependent."),
        QUIZ("Which of the following is a density-dependent factor?", ["A forest fire", "A cyclone", "Competition for food", "A very cold night"], 2,
             "The effect of competition becomes stronger as the population gets more crowded.", hint="Which factor gets worse when there are more individuals?",
             feedback=["Fire kills regardless of density.", "A cyclone kills regardless of density.", "", "Frost affects all individuals regardless of density."]),
        QUIZ("In a capture-recapture study, 60 animals were marked. A later sample of 45 contained 9 marked animals. What is the estimated population?", ["300", "12", "540", "2700"], 0,
             "N = (60 × 45) ÷ 9 = 300.", hint="Use N = M × C ÷ R.",
             feedback=["", "That inverts the formula: M × R ÷ C.", "That multiplies M × R, which is not part of the formula.", "That is M × C with no division by R."]),
        TIP("Population dynamics is a Paper 1 and Paper 2 topic: be ready to label the phases of a growth curve and explain each, to calculate a Lincoln index, and to explain why the predator peak follows the prey peak.", title="Exam link"),
        PQ("Describe and explain the shape of the growth curve of a population of bacteria placed in a flask of broth.",
           "At first growth is slow because there are few cells and they must adjust to the medium (lag). Then growth is exponential: food is plentiful and the number doubles at regular intervals. Later nutrients run out and waste (toxins, acid) builds up, so growth slows. In the stationary phase deaths equal births and the population stays near the carrying capacity. Finally the population may decline as nutrients are exhausted and toxins accumulate."),
        PQ("In a study of a beetle population, 80 beetles were marked. In a second sample of 60 beetles, 12 were marked. Estimate the population and state two assumptions.",
           "N = (80 × 60) ÷ 12 = 400 beetles. Assumptions: marking does not affect the survival or behaviour of the beetles; marked beetles mix randomly with the others; no beetles are born, die, enter or leave the area during the study."),
        PQ("Explain why the numbers of a predator rise and fall after those of its prey.",
           "When prey numbers rise, predators have more food, so they survive and breed, and their numbers rise after a delay. The larger predator population eats more prey, so prey numbers fall. With less food, predators starve and their numbers fall. With fewer predators, the prey population recovers. The delay is the time needed for the predator to reproduce."),
        SUM("Population change = (births + immigration) − (deaths + emigration).",
            "Growth is slow, exponential and then levels off at the carrying capacity: the S-shaped (logistic) curve.",
            "Density-dependent factors (competition, predation, disease) regulate numbers; density-independent factors (fire, floods, frost) do not depend on density.",
            "Predator numbers peak after prey numbers; the cycles are a negative feedback with a time lag.",
            "Capture-recapture: N = M × C ÷ R."),
    ],
))

# ------------------------------------------------------------------ 12. Biodiversity: diversity indices
LESSONS.append(lesson(
    module=M_ECO,
    topic="Biodiversity, pollution and conservation",
    title="Measuring biodiversity: richness, evenness and Simpson's index",
    slug="bil3-biodiversity-indices",
    minutes=23,
    summary="What biodiversity is, how species richness and evenness differ, how to sample a habitat, and how to calculate and interpret Simpson's index of diversity.",
    objectives=[
        "Distinguish genetic, species and ecosystem diversity, and species richness from evenness",
        "Describe how to sample a habitat using random quadrats and transects",
        "Calculate Simpson's index of diversity and interpret it",
        "Explain why biodiversity matters and what threatens it",
    ],
    key_concepts=["Biodiversity", "Species richness", "Evenness", "Simpson's index", "Quadrat", "Transect", "Indicator species", "Habitat loss"],
    blocks=[
        H("Introduction"),
        T("A cocoa farm and a patch of natural forest can both hold plants and animals. The forest has many different species, each with only a few individuals. The farm has a few species, and one of them (cocoa) is very common. "
          "Which is more diverse? To compare them fairly, we need a number. This lesson shows how to get one."),
        D("**Biodiversity** is the variety of life. It has three levels: **genetic diversity** (the variety of alleles within a species), **species diversity** (the number of species and how common each is) and **ecosystem diversity** (the variety of habitats and communities).", title="Definition: biodiversity"),
        KEY("Two parts of species diversity", "Both are needed.", cards=[
            ["Species richness", "The number of different species in a community. It ignores how many individuals there are of each."],
            ["Evenness", "How equal the numbers of individuals of each species are. A community dominated by one species has low evenness."],
        ]),
        H("Sampling a habitat"),
        T("It is impossible to count every organism, so we take samples. To avoid bias the samples must be **random**. A **quadrat** is a square frame (often 1 m × 1 m) placed at coordinates chosen with random numbers. "
          "A **transect** is a line across a habitat along which quadrats are placed at regular intervals, to show change across a gradient such as from the edge of a forest. "
          "Mobile animals can be collected with pitfall traps, sweep nets or kick sampling in a stream. Larger samples give more reliable results, and the same effort must be used in each site."),
        H("Simpson's index of diversity"),
        D("**Simpson's index (D)** takes into account both richness and evenness. For N the total number of individuals of all species and n the number of individuals of each species, the form used in many A Level courses is:", title="Simpson's index", formula=r"D = \frac{N(N-1)}{\sum n(n-1)}"),
        T("The higher the value, the greater the diversity. The lowest possible value is 1, when there is only one species. Some textbooks use a different form, 1 − Σ(n ÷ N)², which gives a value between 0 and 1. Both rank sites in the same order; check which form your textbook uses and show your working."),
        EX("Worked example 1: comparing two sites", intro="Site A has five species with 20, 15, 10, 3 and 2 individuals. Site B has five species with 44, 3, 1, 1 and 1 individuals. Calculate D for each.", steps=[
            S("Site A: N and Σ n(n−1)", math=r"N = 50 \quad \sum n(n-1) = 380 + 210 + 90 + 6 + 2 = 688"),
            S("Site A: D", math=r"D = \frac{50 \times 49}{688} = 3.56"),
            S("Site B: N and Σ n(n−1)", math=r"N = 50 \quad \sum n(n-1) = 1892 + 6 + 0 + 0 + 0 = 1898"),
            S("Site B: D", math=r"D = \frac{50 \times 49}{1898} = 1.29", text="Both sites have five species and 50 individuals, but site A is far more diverse because the individuals are spread more evenly."),
        ], check=r"2450/688 = 3.56"),
        EX("Worked example 2: effect of richness", intro="A third site C has 50 individuals evenly shared among 10 species (5 each). Calculate D and compare it with site A.", steps=[
            S("Σ n(n−1)", math=r"10 \times (5 \times 4) = 200"),
            S("D", math=r"D = \frac{50 \times 49}{200} = 12.25", text="Site C is the most diverse: it has more species and perfect evenness."),
        ]),
        T("A high index suggests a stable ecosystem with many food webs and niches. A low index suggests a simple ecosystem, which a single disturbance can damage. "
          "A low index in a river can show pollution, because only a few tolerant species survive. **Indicator species** show conditions: for example the larvae of stoneflies and mayflies need clean, oxygen-rich water, whereas bloodworms and sludge worms tolerate polluted water. Lichens on trees are sensitive to air pollution."),
        H("Why biodiversity matters and what threatens it"),
        KEY("Reasons to conserve", "Ecological, economic and ethical.", cards=[
            ["Ecological", "Species depend on each other (pollination, food webs, nutrient cycling). A diverse community resists disturbance and recovers better."],
            ["Economic", "Food, timber, fish, fuel and medicines (many drugs have come from plants). Tourism brings income to forest and park regions."],
            ["Ethical and cultural", "Every species has a right to exist, and many species are part of local culture and traditions."],
        ]),
        T("The main threats are **habitat loss** and fragmentation (farming, logging, towns, roads), **overexploitation** (bushmeat hunting, overfishing, the timber trade), **invasive species** that outcompete native ones, **pollution** and **climate change**. These threats are the subject of the next lesson."),
        MISTAKE("Using richness alone", "Two sites with the same number of species can differ greatly in diversity if one is dominated by a single species. Always use an index that includes the numbers in each species."),
        MISTAKE("Forgetting n(n−1)", "The formula uses n(n−1) for each species, not n². A species with only one individual contributes 0 to the sum. Show the sum in a table with columns n and n(n−1)."),
        QUIZ("A sample contains 4 species with 10 individuals each. What is Simpson's index D = N(N−1) ÷ Σn(n−1)?", ["4.33", "1.00", "40.0", "0.75"], 0,
             "N = 40, Σ n(n−1) = 4 × 90 = 360, D = 40 × 39 ÷ 360 = 4.33.", hint="Work out Σ n(n−1) first.",
             feedback=["", "1 is the value for one species only.", "That is N, not D.", "That is 1 − Σ(n/N)² for this sample, a different form of the index."]),
        QUIZ("Why must quadrats be placed at random?", ["So that the sample is not biased by the investigator's choice", "So that more species are found", "So that the quadrats cover the whole area", "So the numbers of organisms are the same in each quadrat"], 0,
             "Random placement avoids bias from placing quadrats where there are more interesting organisms.", hint="Think about where a student would put the quadrat if they were choosing.",
             feedback=["", "Random sampling does not increase the number of species found.", "A random sample covers part of the area, not all of it.", "Numbers will vary between quadrats; that is natural."]),
        TIP("Diversity indices are a Paper 1 and Paper 2 calculation, and the practical Paper 3 often uses random sampling. Show the working in a table, give the answer to 2 decimal places, and compare two sites using the numbers.", title="Exam link"),
        PQ("Explain why species richness alone is a poor measure of the biodiversity of a site.",
           "Richness counts only the number of species and ignores how many individuals there are of each. A site with five species may have 96% of the individuals in one species. It is much less diverse and less stable than a site with five species in equal numbers. An index such as Simpson's index includes both the number of species and the evenness."),
        PQ("A sample from a stream gives the following counts: mayfly larvae 6, stonefly larvae 4, freshwater shrimp 5, bloodworm 5. Calculate Simpson's index D and suggest what it shows.",
           "N = 20. Σ n(n−1) = 30 + 12 + 20 + 20 = 82. D = 20 × 19 ÷ 82 = 4.63. The index is fairly high and the sample includes mayfly and stonefly larvae, which need clean oxygen-rich water, so the stream is probably not heavily polluted."),
        PQ("Describe how you would use random quadrats to compare the plant diversity of two fields.",
           "Mark out each field as a grid using tape measures. Use random numbers (from a calculator or table) as coordinates for 20 or more placements of a 1 m² quadrat in each field. In each quadrat identify the plants and count the number of each species. Add up the totals for each field and calculate Simpson's index for each. Use the same number and size of quadrats and the same time of year in both fields."),
        SUM("Biodiversity includes genetic, species and ecosystem diversity; species diversity combines richness and evenness.",
            "Samples must be random and large enough: quadrats, transects and traps.",
            "Simpson's index D = N(N−1) ÷ Σ n(n−1): the higher, the more diverse.",
            "Indicator species such as stoneflies show water quality.",
            "Threats include habitat loss, overexploitation, invasive species, pollution and climate change."),
    ],
))

# ------------------------------------------------------------------ 13. Pollution and conservation
LESSONS.append(lesson(
    module=M_ECO,
    topic="Biodiversity, pollution and conservation",
    title="Pollution and conservation: eutrophication, biomagnification and sustainable management",
    slug="bil3-pollution-conservation",
    minutes=24,
    summary="The causes and effects of eutrophication, biomagnification of pesticides, noise and other pollution, and how in-situ and ex-situ conservation and sustainable use protect species.",
    objectives=[
        "Explain eutrophication step by step, including the role of biochemical oxygen demand",
        "Explain bioaccumulation and biomagnification, and calculate a magnification factor",
        "Describe the effects of air pollution, plastic and excessive noise on living things",
        "Distinguish in-situ from ex-situ conservation and evaluate sustainable use of resources",
    ],
    key_concepts=["Eutrophication", "BOD", "Biomagnification", "Acid rain", "Noise pollution", "In-situ conservation", "Ex-situ conservation", "Sustainable use"],
    blocks=[
        H("Introduction"),
        T("Water in a village stream turns green in the dry season, and fish die in large numbers. A farm upstream has been heavily fertilised and the village latrine drains into the stream. "
          "This is a typical case of **pollution**: the release by humans of substances or energy that harm living things. We look at the main kinds, then at how species and habitats can be protected."),
        H("Eutrophication"),
        D("**Eutrophication** is the enrichment of a water body with nutrients (mainly nitrate and phosphate), which leads to excessive growth of algae and the loss of oxygen and wildlife.", title="Definition: eutrophication"),
        KEY("Sequence of events", "Write the steps in order in an exam.", cards=[
            ["1. Nutrients enter", "Nitrate and phosphate from fertilisers, sewage and detergents are washed into the water by rain (run-off)."],
            ["2. Algal bloom", "Algae and cyanobacteria grow rapidly at the surface and form a thick green layer."],
            ["3. Light blocked", "The bloom shades the plants below. They cannot photosynthesise and die."],
            ["4. Decomposition", "Dead algae and plants are decomposed by aerobic bacteria, which multiply and use up the dissolved oxygen. The **biochemical oxygen demand (BOD)** rises."],
            ["5. Death of animals", "Fish and other animals with high oxygen needs die of suffocation. Anaerobic bacteria release toxic gases. Biodiversity falls."],
        ]),
        D("**Biochemical oxygen demand (BOD)** is the amount of oxygen taken up by microorganisms in a sample of water, kept in the dark for a set time (often 5 days). A higher BOD means more organic pollution.", title="Definition: BOD"),
        T("Raw sewage causes a similar effect because it is organic matter for decomposers. Controls include treating sewage, reducing the use of fertilisers, planting buffer strips of vegetation by the water, and using fertilisers only at the right time."),
        H("Pesticides and biomagnification"),
        D("**Bioaccumulation** is the build-up of a persistent substance in the body of one organism over time. **Biomagnification** is the increase in concentration of the substance at each higher trophic level of a food chain.", title="Definitions"),
        T("Persistent pesticides such as DDT and some heavy metals (mercury, lead) are not broken down, and they are stored in fat or tissues, so they are not excreted. A predator eats many prey and accumulates all of their stored poison. "
          "The concentration therefore rises at each step, and top predators such as fish-eating birds suffer the most (for example thin eggshells and population falls). The effect can be shown by a table of concentrations."),
        CODE("Organism               Concentration (ppm, invented)\n"
             "Water                  0.00003\n"
             "Plankton               0.04\n"
             "Small fish             0.5\n"
             "Large fish             2\n"
             "Fish-eating bird       25", "text", title="Table 1. A teaching example of biomagnification"),
        EX("Worked example 1: magnification factors", intro="Use Table 1. By what factor is the concentration in the fish-eating bird greater than in (a) the large fish and (b) the water?", steps=[
            S("(a) Bird to large fish", math=r"\frac{25}{2} = 12.5"),
            S("(b) Bird to water", math=r"\frac{25}{0.00003} = 8.3 \times 10^{5}", text="The bird has about 830 000 times the concentration in the water. Water pollution that seems harmless can still kill top predators."),
        ], check=r"25/0.00003 = 833333"),
        H("Other pollutants"),
        KEY("More types", "Cause, effect and control.", cards=[
            ["Acid rain", "Sulphur dioxide and nitrogen oxides (from burning fuel and vehicle exhausts) dissolve in rain, lowering its pH. It damages leaves, acidifies lakes and soil and releases toxic aluminium. Controlled by cleaner fuels and filters."],
            ["Greenhouse gases", "Carbon dioxide and methane absorb heat radiated from the Earth. Their increase raises global temperature, changes rainfall and shifts the ranges of species."],
            ["Plastics", "Plastic bags and bottles block drains, trap animals and break into tiny pieces eaten by organisms. They persist for many years."],
            ["Oil", "Oil spills coat birds and block the gills of fish and the pores of plants in swamps and mangroves."],
            ["Noise", "Excess noise in large towns causes hearing loss, stress, raised blood pressure, disturbed sleep and poor concentration, and affects animals' communication. The question usually asks for the EFFECTS, not the sources."],
        ]),
        H("Conservation"),
        D("**Conservation** is the protection and sustainable management of species, habitats and ecosystems to maintain biodiversity.", title="Definition"),
        KEY("Two approaches", "In-situ keeps the animals in their home; ex-situ takes them out for protection.", cards=[
            ["In-situ (in the natural habitat)", "National parks and reserves, such as Korup National Park and Waza National Park in Cameroon, laws against poaching and logging, and community forests. It protects the whole ecosystem and food webs, and species keep their natural behaviour. It needs patrols and funds."],
            ["Ex-situ (outside the habitat)", "Zoos, wildlife sanctuaries, botanic gardens, captive breeding, seed banks and gene banks. It can rescue species whose habitat is lost, and allows research and release back into the wild. It protects only a few species and animals may lose natural behaviour."],
        ]),
        T("International agreements (such as the Convention on International Trade in Endangered Species, CITES) regulate trade in rare species. "
          "**Sustainable use** means using a resource at a rate at which it can be replaced: selective logging and replanting, catch quotas and mesh sizes in fishing, rotating crops and agroforestry. "
          "People who live near protected areas need benefits such as jobs in tourism, a share of the income and alternative sources of protein, or they will continue to hunt and clear land. Education and community management help conservation to succeed."),
        MISTAKE("Giving sources when asked for effects", "In the Board's 2023 report, many candidates described where noise comes from (bars, markets) when the question asked about the effects on people. Read the command words: effects, causes, sources, control."),
        MISTAKE("Saying that fertiliser kills fish directly", "Fish die because of the oxygen shortage that follows the algal bloom and decay. Describe the sequence of events: nutrients, bloom, light blocked, death of plants, decomposition, BOD, oxygen shortage."),
        QUIZ("What is the main reason fish die in a eutrophic lake?", ["The nitrate is poisonous to fish", "Decomposers use up the dissolved oxygen", "The water becomes too warm", "Algae eat the fish"], 1,
             "After the algae die, aerobic bacteria use much of the dissolved oxygen, so the fish suffocate.", hint="Think about what the bacteria do to the dead algae.",
             feedback=["Nitrate at normal levels is not the direct cause.", "", "Temperature is not the main cause.", "Algae do not feed on fish."]),
        QUIZ("Which of the following is an example of ex-situ conservation?", ["A national park", "A seed bank", "A community forest", "A law against hunting"], 1,
             "A seed bank stores seeds outside their natural habitat.", hint="Ex-situ means off-site.",
             feedback=["A park protects species in their habitat (in-situ).", "", "A forest protects species in their habitat (in-situ).", "A law protects species in the wild (in-situ)."]),
        TIP("Pollution and conservation are favourite Paper 2 topics, often with a stated place or species. Name the pollutant, give the sequence of events with the correct vocabulary (BOD, magnification), and evaluate the control measure, mentioning both benefits and limits.", title="Exam link"),
        PQ("Describe how eutrophication of a lake can kill fish.",
           "Nitrates and phosphates from fertilisers and sewage run into the lake. Algae multiply rapidly, forming a bloom that blocks light, so submerged plants cannot photosynthesise and die. Dead algae and plants are decomposed by aerobic bacteria, whose population rises and uses up the dissolved oxygen (high BOD). Fish and other aerobic organisms suffocate and die."),
        PQ("Explain why a fish-eating bird contains a higher concentration of a persistent pesticide than the plankton in the lake.",
           "The pesticide is persistent and is stored in the fat of organisms, so it is not broken down or excreted. Plankton absorb it from the water. Each small fish eats many plankton and keeps their pesticide, so its concentration is higher. Large fish eat many small fish and the concentration rises again. The bird eats many large fish. The concentration therefore increases at each trophic level (biomagnification)."),
        PQ("Compare in-situ and ex-situ conservation, with one advantage and one disadvantage of each.",
           "In-situ conservation protects species in their natural habitat, as in a national park. Advantage: whole ecosystems and food webs are protected and species keep their natural behaviour. Disadvantage: it is difficult to control poaching or logging and costs a lot of patrolling. Ex-situ conservation protects species away from their habitat, as in a zoo, botanic garden or seed bank. Advantage: it can save a species whose habitat is destroyed and allows captive breeding. Disadvantage: only a few species can be kept, genetic diversity may be small and animals may lose natural behaviour."),
        SUM("Eutrophication: nutrients, algal bloom, light blocked, death of plants, decomposition, high BOD, oxygen shortage, death of fish.",
            "Persistent pesticides biomagnify up food chains and affect top predators most.",
            "Pollution includes acid rain, greenhouse gases, plastics, oil and noise; learn effects, causes and controls.",
            "In-situ conservation protects habitats; ex-situ conservation protects species outside them.",
            "Sustainable use and community involvement are needed for long-term success."),
    ],
))

# ------------------------------------------------------------------ Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: working through 50 multiple-choice questions",
    slug="bixl-paper1-multiple-choice",
    minutes=24,
    summary="How to approach the 50 multiple-choice questions of Paper 1: reading stems, predicting answers, eliminating options, handling data, calculations and diagrams, and a map of the seven Lower Sixth modules.",
    objectives=[
        "Use a repeatable routine to answer a multiple-choice question: read, predict, eliminate, check",
        "Handle calculation, graph and diagram questions quickly and accurately",
        "Recognise the common traps that wrong options are built on",
        "Plan revision using a map of the seven Lower Sixth modules",
    ],
    key_concepts=["Stem", "Distractor", "Elimination", "Command word", "Data interpretation", "Time per question", "Revision map"],
    blocks=[
        H("Introduction"),
        T("Paper 1 of the Advanced Level Biology examination is made up of 50 multiple-choice questions. Each has a stem (the question) and four options, and only one is correct. "
          "The Board's 2023 subject report says the paper tests a wide scope of the syllabus, and the MCQ answer sheets are marked by the Board's technical team. A multiple-choice answer is either right or wrong: there is no credit for a partly correct idea, so you must choose the right letter. "
          "In the KKEVO mock paper that goes with this lesson, we set 90 minutes for 50 questions (a KKEVO practice setting). That is under two minutes for each question."),
        H("A routine for every question"),
        KEY("Four steps", "Do them in order and quickly.", cards=[
            ["1. Read the stem", "Underline the command: which is correct, which is NOT, calculate, identify. Note units and any numbers."],
            ["2. Predict", "Before reading the options, say the answer in your head. This protects you from attractive wrong options."],
            ["3. Eliminate", "Cross out options that you know are wrong. Each is built on a real misconception. Why is it wrong?"],
            ["4. Check", "Re-read the stem against your chosen option. For calculations, check the units and the order of magnitude."],
        ]),
        T("If you cannot decide in about two minutes, mark your best guess, put a mark by the question, and move on. Come back later. Never leave a question unanswered: a blank cannot score, but a sensible guess can. (In the KKEVO mock a wrong answer simply scores no mark; follow your teacher's guidance for the real paper.)"),
        H("Kinds of question and how to handle them"),
        T("**Recall** questions test a fact, such as the enzyme that speeds the reaction of carbon dioxide and water in red blood cells. Answer from memory, then check the options. "
          "**Process** questions ask for the order or the correct step (the path of excitation in the heart; the nitrogen cycle). Draw the sequence in the margin of the question. "
          "**Calculation** questions ask for a number: magnification, ventilation rate, cardiac output, efficiency, Simpson's index. Write the formula, substitute with units, and check against the options. "
          "**Data and diagram** questions give a graph, table or drawing: read it carefully first, then use the stem. "
          "**Experiment** questions ask which control, variable or conclusion is correct."),
        EX("Worked example 1: a calculation", intro="A heart has an end-diastolic volume of 130 cm³ and an end-systolic volume of 55 cm³. The heart rate is 80 beats per minute. What is the cardiac output? A 6.0 dm³ per min, B 10.4 dm³ per min, C 75 cm³ per min, D 4.4 dm³ per min.", steps=[
            S("Predict", text="Stroke volume is the difference between the two volumes. Cardiac output is stroke volume multiplied by heart rate."),
            S("Calculate", math=r"(130 - 55) \times 80 = 75 \times 80 = 6000 \text{ cm}^3 \text{ min}^{-1} = 6.0 \text{ dm}^3 \text{ min}^{-1}"),
            S("Eliminate", text="B is 130 × 80. C is the stroke volume (no rate). D is 55 × 80. The answer is A."),
        ], check=r"75 \times 80 = 6000"),
        EX("Worked example 2: reading a graph", intro="Look at the oxygen dissociation curves in the lesson on haemoglobin. At a pO₂ of 4 kPa the adult curve shows 59% saturation, and the curve at high CO₂ shows 41%. A student says: 'The haemoglobin at high CO₂ has a higher affinity for oxygen.' Is this correct?", steps=[
            S("Predict", text="A curve lower and to the right has a lower affinity."),
            S("Use the data", text="At the same pO₂ (4 kPa) the high-CO₂ curve is less saturated (41% against 59%)."),
            S("Conclusion", text="The statement is wrong. The haemoglobin has a lower affinity, so more oxygen is released to the tissues."),
        ]),
        H("Traps built into wrong options"),
        KEY("Common distractors", "Recognise them and do not be caught.", cards=[
            ["The reversed answer", "Left for right, increase for decrease, source for sink. Re-check the direction in the stem."],
            ["The half-right answer", "Correct for one part of the stem but not for the other, such as the correct enzyme at the wrong place."],
            ["The unfinished calculation", "The result of the first step only (stroke volume, not cardiac output)."],
            ["The related fact", "True, but it answers a different question: for example 'the lungs are elastic' in a question about the diaphragm."],
            ["The absolute word", "Options with 'always', 'only' or 'never' are rarely correct in biology."],
        ]),
        H("A map of the seven Lower Sixth modules"),
        T("Paper 1 samples every module, roughly in proportion to the number of topics. Use this map to plan revision."),
        CODE("Module                                         Ideas to be ready for\n"
             "Cytology & Membrane Physiology                 prokaryote/eukaryote, fluid mosaic, water\n"
             "                                               potential, osmosis, active transport\n"
             "Biological Molecules & Enzymology              sugars, lipids, protein structure, Vmax and\n"
             "                                               Km, inhibition, allosteric regulation\n"
             "Nucleic Acids, Protein Synthesis, Cell Division DNA/RNA, replication, genetic code,\n"
             "                                               mitosis, meiosis\n"
             "Biodiversity & Systematic Taxonomy             domains, kingdoms, keys, phyla\n"
             "Autotrophic & Heterotrophic Nutrition          chloroplast, light reactions, Calvin cycle,\n"
             "                                               C3/C4/CAM, gut histology and hormones\n"
             "Gaseous Exchange & Mass Transport              ventilation, ODC, cardiac cycle, tissue fluid,\n"
             "                                               xylem and phloem\n"
             "Ecology, Population Dynamics, Conservation     energy, cycles, succession, populations,\n"
             "                                               diversity, pollution", "text", title="Table 1. Revision map"),
        MISTAKE("Changing a correct answer without a reason", "Your first choice is usually right if you read the stem carefully. Change an answer only if you find a clear error in your reasoning, not because of a feeling."),
        MISTAKE("Spending too long on one calculation", "If a calculation needs more than two or three minutes, make a note and return to it. An easier question later is worth the same."),
        QUIZ("A question asks: 'Which statement about the cardiac cycle is NOT correct?' Which approach is best?", ["Choose the first option that seems true", "Check each option and choose the one that is false", "Choose the longest option", "Choose the option that contains the word 'always'"], 1,
             "A NOT question asks for the false statement, so test each option for truth and pick the false one.", hint="What are you looking for in a NOT question?",
             feedback=["The first true option is the wrong choice here.", "", "Length does not show falsehood.", "'Always' may suggest falsehood but you must check the facts, not guess from a word."]),
        QUIZ("A pipette is marked ±0.1 cm³ and used to measure 5.0 cm³. What is the percentage uncertainty?", ["0.1%", "2%", "5%", "0.5%"], 1,
             "0.1 ÷ 5.0 × 100 = 2%.", hint="Percentage uncertainty = uncertainty ÷ measurement × 100.",
             feedback=["That is the uncertainty value written as a percentage without the division.", "", "That is 5.0 itself written as a percentage.", "That is 0.1 ÷ 20."]),
        TIP("Work through the paper once quickly, answering what you know, then use the time left for the marked questions. Leave 5 to 10 minutes at the end to check that every question has an answer.", title="Exam link"),
        PQ("A student breathes with a tidal volume of 0.60 dm³ at 15 breaths per minute. The dead space is 0.15 dm³. What is the alveolar ventilation? A 9.0, B 6.75, C 2.25, D 0.45 (all in dm³ per minute).",
           "Alveolar ventilation = (0.60 − 0.15) × 15 = 0.45 × 15 = 6.75 dm³ per minute, so B. A is 0.60 × 15 (no dead space). C is 0.15 × 15 (the dead space volume only). D is the volume per breath."),
        PQ("In a food chain, the net primary productivity is 12 000 kJ m⁻² year⁻¹ and the primary consumers gain 1 200. The efficiency of transfer is: A 1%, B 10%, C 90%, D 100%.",
           "1 200 ÷ 12 000 × 100 = 10%, so B."),
        PQ("List four steps you would use to answer a multiple-choice question.",
           "Read the stem and note the command word; predict the answer before reading the options; eliminate options that are wrong, thinking about why each is wrong; check the answer against the stem, including units for a calculation."),
        SUM("Paper 1 is 50 multiple-choice questions; there is no partial credit, so choose the best option for each.",
            "Use the routine: read, predict, eliminate, check. Never leave a question blank.",
            "Wrong options are built on reversed ideas, half-right ideas, unfinished calculations and related facts.",
            "Practise calculations, graph reading and diagrams with units; budget about two minutes a question in the KKEVO mock.",
            "Revise all seven modules, as the paper samples every one."),
    ],
))

# ------------------------------------------------------------------ Examination 2. Paper 2
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: answering structured and essay questions",
    slug="bixl-paper2-theory-essay",
    minutes=25,
    summary="How to read command words, answer exactly what is asked, plan essays, use labelled diagrams and annotation, handle data, and avoid the errors the Board's 2023 report describes.",
    objectives=[
        "Interpret command words such as describe, explain, outline, state, compare and suggest",
        "Plan and write a structured essay answer with accurate terminology",
        "Draw and annotate a diagram so it earns marks, and answer data questions with figures",
        "Avoid the typical errors reported by the Board in 2023, such as answering a different question",
    ],
    key_concepts=["Command word", "Essay plan", "Annotation", "Data response", "Terminology", "Relevance", "Synthesis", "Mark allocation"],
    blocks=[
        H("Introduction"),
        T("Paper 2 is the written theory paper, with structured and essay questions. The Board's 2023 report describes a paper of eight questions and says that performance was poor on most of them, especially on questions that needed ideas from different parts of the course to be put together, such as protein synthesis or the nerve impulse. "
          "Its most frequent comment was that candidates answered the question they hoped to see, not the one on the paper. This lesson trains you to answer the question that is asked. "
          "Paper 2 cannot be marked automatically, so the KKEVO practice paper that goes with this lesson uses multiple-choice and numeric parts that follow the style of the paper; practise full written answers on paper as well."),
        H("Command words"),
        KEY("What each word asks for", "Learn to answer the word, not the topic.", cards=[
            ["State, name, give", "A short fact or term. No explanation."],
            ["Define", "A precise meaning, in a sentence."],
            ["Describe", "Say what happens or what you see, in order. No reasons."],
            ["Explain", "Give reasons: how and why. Use 'because' and 'so'."],
            ["Outline", "The main points only, briefly."],
            ["Compare, distinguish", "Similarities and differences, each with both sides stated. A table or paired sentences work well."],
            ["Suggest", "Apply your knowledge to an unfamiliar situation. There may be several acceptable answers."],
            ["Annotate", "Label a diagram with a short description of structure AND function, not the name only."],
        ]),
        H("Answer what is asked: errors from the Board's report"),
        T("The Board's 2023 report for this subject lists many examples, which we paraphrase here. Each is a different way of answering the wrong question."),
        KEY("Errors to avoid", "Each is a lost mark that is easy to keep.", cards=[
            ["Define when asked for a role", "Asked for the role of metamorphosis, candidates defined and described its types. The role is the problem it solves: separate stages can use different food and habitats."],
            ["Credit the gland, not the secretion", "Asked for functions of saliva and hydrochloric acid, candidates gave the functions of the glands. Name the secretion and say what it does."],
            ["Food chain instead of energy flow", "Asked to trace energy in a named ecosystem, candidates drew an unlabelled food chain. Name the ecosystem, use organisms that live there and show energy losses."],
            ["Sources instead of effects", "Asked for effects of noise on people, candidates listed sources. Read the word 'effects'."],
            ["Blood flow instead of the cycle", "Asked to describe the cardiac cycle, candidates traced the path of blood. Describe systole and diastole and the valves."],
            ["Structure OR function in an annotation", "An annotation should say both what the part looks like and what it does."],
        ]),
        H("Planning an essay"),
        T("For a question worth many marks, spend two minutes on a plan. Write the headings in the margin: for the nitrogen cycle, for example, the headings are fixation, ammonification, nitrification, denitrification and human effects. "
          "Then write one paragraph per heading, each with a topic sentence, the process, the organism and the chemical change. Use the exact scientific terms. Finish with a sentence that answers the question directly."),
        EX("Worked example 1: a structured answer", intro="Describe how the structure of the alveolus is related to its function in gaseous exchange. (A model answer plan with marks.)", steps=[
            S("Point 1: surface area", text="Millions of alveoli give a large surface area, so more oxygen and carbon dioxide can diffuse per second."),
            S("Point 2: diffusion distance", text="The wall is one cell thick (squamous epithelium) next to a one-cell thick capillary, so the diffusion path is very short."),
            S("Point 3: gradient", text="Ventilation brings in air with a high oxygen concentration and the blood flow removes oxygen, so the concentration gradient is steep."),
            S("Point 4: moist and elastic", text="A moist surface lets gases dissolve. Elastic fibres allow stretching and recoil. Surfactant stops the alveoli sticking together."),
            S("Link", text="Each feature is connected to Fick's law: rate of diffusion is proportional to surface area × concentration difference ÷ distance."),
        ]),
        H("Diagrams and annotation"),
        T("Draw a single, clear diagram where the question asks for one, using a sharp pencil, with a title and ruled label lines that do not cross each other. "
          "In the Board's practical examination, candidates who drew several diagrams of different systems separately lost time and marks; one diagram showing all systems asked for is better. "
          "When you annotate, write the structure (what it looks like or where it is) and the function (what it does) on one line."),
        H("Data questions"),
        T("When a graph or table is given, follow four steps. (1) State the overall trend with the variables and units. (2) Quote at least two data points with their units. (3) Do any calculation asked for, with working. (4) Give a biological explanation using the right terms. "
          "Never describe a graph without quoting values, and never explain without referring to the data."),
        EX("Worked example 2: describing and explaining data", intro="A table (invented data) shows that, as the partial pressure of CO₂ rises from 2 to 8 kPa, the percentage saturation of haemoglobin at pO₂ = 4 kPa falls from 70% to 45%. Describe and explain the change.", steps=[
            S("Describe with data", text="As the CO₂ pressure rises from 2 kPa to 8 kPa, the haemoglobin saturation at 4 kPa oxygen falls from 70% to 45%, a fall of 25 percentage points."),
            S("Explain", text="More CO₂ forms more carbonic acid and H⁺ in the red blood cell. H⁺ binds to haemoglobin, lowering its affinity for oxygen (the Bohr shift), so it releases more oxygen to the tissues."),
        ], check=r"70 - 45 = 25"),
        MISTAKE("Writing everything you know on the topic", "Marks are only for points that answer the question. A long answer full of irrelevant facts can lose the marker's attention and wastes time you need for the other questions."),
        MISTAKE("Using everyday words", "Write 'water potential gradient', not 'water goes to where there is less water'. Write 'the semilunar valve closes', not 'the door shuts'. Use correct terms, spelled correctly."),
        QUIZ("A question says: 'Explain why the aorta pressure does not fall to zero between beats.' Which answer is best?", ["The aorta is a large vessel with a thick wall", "The elastic wall recoils in diastole, squeezing the blood on, and the semilunar valve prevents backflow", "The aorta carries blood to the whole body", "The pressure falls to zero when the person is asleep"], 1,
             "An explanation gives the mechanism: elastic recoil and the closed valve.", hint="Which answer gives a reason?",
             feedback=["It is a description of the vessel, not an explanation.", "", "It is a fact about the aorta but it is not a reason.", "It is false."]),
        QUIZ("What does 'annotate' require on a labelled diagram?", ["The names of the parts only", "A short note on the structure and function of each labelled part", "A different diagram for each part", "A longer answer on a separate page"], 1,
             "Annotation adds a description of the structure and function beside each label.", hint="Think about the word note.",
             feedback=["That is labelling, not annotating.", "", "One diagram is better than several.", "Annotations go on the diagram, in short form."]),
        TIP("Paper 2 contains topics from all seven modules, including questions that combine them (for example, the Bohr shift needs both haemoglobin structure and the carbonic anhydrase reaction). Revise by linking topics, not only by topic.", title="Exam link"),
        PQ("(a) State the meaning of the command words 'describe' and 'explain'. (b) Rewrite this answer so that it answers the question 'Explain why a very tall tree has a negative pressure in its xylem': 'Water goes up the tree.'",
           "(a) Describe: say what happens, in sequence, without reasons. Explain: give reasons, saying how and why. (b) 'Water evaporates from the leaf cells and diffuses out of the stomata (transpiration). This lowers the water potential of the leaf cells, which pull water from the xylem. The water molecules are held together by hydrogen bonds (cohesion), so the whole column is pulled up and is under tension, which is a negative pressure.'"),
        PQ("Annotate the structure of the ileum wall and explain how it is adapted for absorption (three features).",
           "Villi: finger-like projections with a thin epithelium, which give a large surface area for absorption. Epithelial cells with microvilli: increase surface area further and contain carrier proteins for active transport. A rich capillary network and a lacteal in each villus: remove absorbed substances so the concentration gradient is maintained. Each annotation names the structure and states its function."),
        PQ("Plan, in note form, an answer to 'Describe how humans have affected the carbon cycle'.",
           "Heading 1: burning fossil fuels releases CO₂ stored for millions of years. Heading 2: deforestation and burning reduce photosynthesis and release CO₂. Heading 3: intensive farming (cattle, rice fields) releases methane. Heading 4: consequence: more CO₂ and methane in the atmosphere, enhanced greenhouse effect, global warming. Heading 5: reduction measures (reforestation, renewable energy)."),
        SUM("Read the command word first: state, define, describe, explain, outline, compare, suggest, annotate each ask for something different.",
            "Answer the question asked: role, not definition; secretion, not gland; effects, not sources; cycle, not blood flow.",
            "Plan essays with headings; use exact terminology; give both structure and function in annotations.",
            "For data, state the trend, quote values with units, calculate if asked, then explain.",
            "Link topics across modules; practise written answers on paper."),
    ],
))

# ------------------------------------------------------------------ Examination 3. Paper 3
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: practical skills - microscopy, dissection, biochemical tests, keys, graphs and statistics",
    slug="bixl-paper3-practical-skills",
    minutes=25,
    summary="The practical skills for Paper 3: drawing and magnification, dissection and annotation, food tests, taxonomic keys, tables, graphs, simple statistics, planning and evaluation, in a Cameroonian school laboratory.",
    objectives=[
        "Calculate magnification and actual size, and draw and label a specimen correctly",
        "Carry out and interpret the biochemical tests for starch, sugars, protein and lipid",
        "Construct a dichotomous key from visible external features and classify a specimen",
        "Record results in a table, plot a graph, calculate a mean and standard deviation, and plan and evaluate an experiment",
    ],
    key_concepts=["Magnification", "Scale bar", "Annotation", "Benedict's test", "Dichotomous key", "Independent variable", "Standard deviation", "Percentage error"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is the practical paper. The Board's 2023 report shows groups of questions with identification and classification of specimens, drawing, dissection, biochemical tests, microscopy, experiments on osmosis, enzymes and food tests, and the use of dichotomous keys. "
          "It also shows that candidates lost marks for poor drawings, for annotating with functions only, for keys that used features that cannot be seen, and for not knowing the exact quantities and conditions of the food tests. "
          "Practical marks are earned by doing, so practise in the laboratory. This lesson tells you what the examiner looks for."),
        H("Microscopy and drawing"),
        D("**Magnification** = size of the image ÷ actual size of the object (both in the same units). A **scale bar** is a line on a drawing that represents a known real length.", title="Magnification", formula=r"\text{magnification} = \frac{\text{image size}}{\text{actual size}}"),
        EX("Worked example 1: magnification and actual size", intro="(a) A drawing of a cell is 45 mm long. The cell is actually 30 µm long. Find the magnification. (b) Another drawing of a cell is 60 mm long at a magnification of ×400. Find the actual length in µm.", steps=[
            S("Convert to the same units", math=r"45 \text{ mm} = 45\,000 \,\mu\text{m}"),
            S("(a) Magnification", math=r"\frac{45\,000}{30} = \times 1500"),
            S("(b) Actual length", math=r"\frac{60 \text{ mm}}{400} = 0.15 \text{ mm} = 150 \,\mu\text{m}"),
        ], check=r"1500 \times 30 = 45000"),
        KEY("Rules for a biological drawing", "Examiners check each one.", cards=[
            ["Size and position", "Use a large part of the space. Draw what you see, not what a textbook shows."],
            ["Lines", "Sharp, single, continuous pencil lines. No shading, no sketching, no colouring."],
            ["Proportion", "Show the true proportions and the right number of parts. Draw outlines of tissues and a few cells, not every cell."],
            ["Labels", "Ruled label lines that touch the part and do not cross each other. Labels written horizontally, outside the drawing."],
            ["Title and magnification", "Give a title (name of specimen and the view) and the magnification or a scale bar."],
        ]),
        H("Dissection"),
        T("In a dissection, such as of a fish, a bird or a rat, the Board's report says to display the systems asked for on a single diagram. Cut carefully, pin the animal in the dissecting tray and keep tissues moist. "
          "Draw in pencil what you see after displaying the system. **Annotate** by writing both the structure (for example 'long, coiled tube with many folds') and the function (for example 'absorbs digested food into the blood'). "
          "The report says that candidates must draw specimens themselves in the presence of the teacher, not copy from books. Wash hands and dispose of the specimen as the teacher instructs."),
        H("Biochemical tests"),
        CODE("Test for       Method                                        Positive result\n"
             "Starch         add iodine solution (yellow-brown)            blue-black\n"
             "Reducing       add Benedict's solution, heat in a water      blue -> green -> yellow ->\n"
             "sugar          bath at about 80 C for 2-3 minutes            orange -> brick red\n"
             "Non-reducing   heat with dilute HCl, cool, neutralise with   brick-red precipitate\n"
             "sugar          sodium hydrogencarbonate, then Benedict's     (only after the acid step)\n"
             "Protein        add NaOH then drops of dilute copper(II)      blue -> violet/purple\n"
             "               sulphate (biuret test)\n"
             "Lipid          shake with ethanol, then pour into water      cloudy white emulsion\n"
             "               (emulsion test)\n"
             "Vitamin C      add food extract to DCPIP (blue) drop by     DCPIP is decolourised\n"
             "               drop                                          (the more it takes, the less vitamin C)", "text", title="Table 1. Biochemical tests"),
        T("State quantities (for example 2 cm³ of sample and 2 cm³ of Benedict's solution) and say when heating is needed. Include a control: repeat the test with water in place of the sample, to show that the reagent alone does not give the positive colour. "
          "Test for reducing sugar first. If it is negative, then do the non-reducing test: if it turns positive only after the acid and neutralising steps, a non-reducing sugar (such as sucrose) is present."),
        H("Taxonomy and dichotomous keys"),
        T("To **identify and classify** a specimen, note its external features and place it in a phylum and class using these (for example, an animal with jointed legs and a hard exoskeleton is in the phylum Arthropoda). "
          "A **dichotomous key** is a series of paired statements that each lead to a name or to the next pair. "
          "The Board's report says that many candidates used features that were not external and visible, such as 'lays eggs' or 'cold-blooded'. Use only features you can see on the specimen: colour, number of legs, wings, shape, presence of a shell. "
          "When asked for a habitat, name the specific place (for example 'under damp leaf litter'), not 'terrestrial'."),
        CODE("1a  Has wings ................................ go to 2\n"
             "1b  No wings ................................. go to 3\n"
             "2a  One pair of wings ........................ housefly\n"
             "2b  Two pairs of wings ....................... dragonfly\n"
             "3a  Six legs ................................. ant\n"
             "3b  Eight legs ............................... spider", "text", title="Listing 1. A dichotomous key (invented example)"),
        H("Recording results, graphs and statistics"),
        KEY("Tables and graphs", "Presentation marks are easy marks.", cards=[
            ["Table", "Independent variable in the first column. Units in the column heading, not in the body. Same number of decimal places in each column. Include repeats and a mean."],
            ["Graph", "Independent variable on the x-axis, dependent on the y-axis. Label axes with the quantity and unit. Scales that use more than half of the grid, in equal steps. Plot points exactly as small crosses. Use a line of best fit, or join points with straight lines if a trend is unknown."],
            ["Type", "A line graph for two continuous variables, a bar chart for categories, a histogram for continuous classes."],
        ]),
        EX("Worked example 2: mean and standard deviation", intro="Six seedlings have heights of 12, 14, 11, 15, 13 and 16 mm. Calculate the mean and the sample standard deviation.", steps=[
            S("Mean", math=r"\bar{x} = \frac{12 + 14 + 11 + 15 + 13 + 16}{6} = 13.5 \text{ mm}"),
            S("Deviations squared", math=r"(-1.5)^2 + (0.5)^2 + (-2.5)^2 + (1.5)^2 + (-0.5)^2 + (2.5)^2 = 17.5"),
            S("Sample standard deviation", math=r"s = \sqrt{\frac{17.5}{6 - 1}} = \sqrt{3.5} = 1.87 \text{ mm}", text="Standard deviation shows how much the values spread around the mean. A small value means the results are consistent (precise)."),
        ], check=r"\sqrt{3.5} = 1.87"),
        T("To decide whether the difference between two means is real, you can use the **t-test**. It compares the means, taking the spread into account. If the probability p is less than 0.05 the difference is said to be statistically significant. "
          "A **correlation** (for example the Spearman rank test) tests whether two variables change together, but a correlation does not prove one causes the other. The details of each test are in your textbook; know when to use each one and how to state the null hypothesis."),
        H("Planning, errors and evaluation"),
        T("In a plan, state the **independent variable** (what you change), the **dependent variable** (what you measure) and the **controlled variables** (what you keep the same). Give the range of values, the apparatus, the number of repeats and how you will reduce error. "
          "For an osmosis experiment with carrot strips, for example, the strips should have the same length and surface area, the same volume of solution and the same time. Dry each strip gently before weighing."),
        EX("Worked example 3: percentage change and percentage error", intro="A carrot strip has a mass of 10.0 g. After 30 minutes in a solution its mass is 12.0 g. A second strip falls from 10.0 g to 8.8 g in a stronger solution. (a) Calculate the percentage change in each. (b) A measuring cylinder with an uncertainty of ±0.5 cm³ is used to measure 10 cm³. What is the percentage error?", steps=[
            S("(a) First strip", math=r"\frac{12.0 - 10.0}{10.0} \times 100 = +20\%", text="The strip gains water by osmosis, so the solution had a higher water potential than the carrot cells."),
            S("(a) Second strip", math=r"\frac{8.8 - 10.0}{10.0} \times 100 = -12\%", text="The strip loses water, so the solution had a lower water potential than the cells."),
            S("(b) Percentage error", math=r"\frac{0.5}{10} \times 100 = 5\%", text="A burette or pipette would give a smaller percentage error."),
        ], check=r"(8.8-10)/10 = -0.12"),
        T("When you evaluate, discuss reliability (repeat results close together), accuracy (close to the true value), the main sources of error and how to improve them. "
          "Report the experiment in the past tense and reported speech where the paper asks for it, as the Board's report advises: 'The strips were weighed' rather than 'We weigh the strips'. "
          "Many Cameroonian school laboratories are short of apparatus. You can still earn full marks if you adapt safely. A kerosene or gas stove and a beaker of water give a water bath. A thermometer shows the temperature. A kitchen scale can replace a balance for rough work. "
          "Never taste or smell chemicals, wear eye protection when heating and keep flames away from alcohol. Leave the laboratory clean. If a reagent is missing, tell the examiner: a practical paper rewards honest reporting of what was done."),
        MISTAKE("Labelling with a function and no structure", "'Absorbs food' is a function. 'Long coiled tube with folded wall' is a structure. Annotate with both."),
        QUIZ("A food sample gives a blue colour with Benedict's reagent on heating. After heating with dilute acid, neutralising and heating with Benedict's reagent, it gives a brick-red precipitate. What does the sample contain?", ["A reducing sugar", "A non-reducing sugar", "Starch", "Protein"], 1,
             "No colour change at first shows no reducing sugar. The positive result after hydrolysis shows a non-reducing sugar, such as sucrose.", hint="What does the acid step do to a non-reducing sugar?",
             feedback=["A reducing sugar would give the colour change at the first test.", "", "Starch is tested with iodine.", "Protein is tested with the biuret test."]),
        QUIZ("An image of a cell on a photograph is 50 mm long and the magnification is ×2000. What is the actual length?", ["100 000 mm", "25 µm", "0.25 µm", "2.5 mm"], 1,
             "Actual length = 50 mm ÷ 2000 = 0.025 mm = 25 µm.", hint="Divide the image size by the magnification, then convert units.",
             feedback=["That multiplies by 2000 instead of dividing.", "", "That divides incorrectly by 200 000.", "That divides by 20, not by 2000."]),
        TIP("Paper 3 is a practical paper in which you carry out tasks, identify and classify specimens, draw, record results and interpret them. Practise each skill in this lesson in the laboratory with a timer, and keep your drawings and notes tidy.", title="Exam link"),
        PQ("Describe how you would test a solution for the presence of a reducing sugar and for a non-reducing sugar.",
           "Reducing sugar: place 2 cm³ of the solution in a test tube, add 2 cm³ of Benedict's solution, heat in a water bath at about 80 degrees Celsius for 2 to 3 minutes. An orange or brick-red precipitate shows reducing sugar; the colour sequence is blue, green, yellow, orange, brick red. Non-reducing sugar: if the first test is negative, heat a fresh 2 cm³ sample with 1 cm³ of dilute hydrochloric acid in a water bath, cool, neutralise with sodium hydrogencarbonate until it stops fizzing, then add Benedict's solution and heat. A brick-red precipitate shows a non-reducing sugar. A control with water should give blue."),
        PQ("A drawing of a cell is 72 mm wide. The scale bar on the drawing, 10 mm long, represents 5 µm. Find the actual width of the cell and the magnification.",
           "Actual width = 72 ÷ 10 × 5 = 36 µm. Magnification = 10 mm ÷ 5 µm = 10 000 µm ÷ 5 µm = ×2000. Check: 72 mm = 72 000 µm; 72 000 ÷ 36 = 2000."),
        PQ("Write a dichotomous key for three specimens: a millipede (many pairs of legs), a spider (eight legs and no antennae) and a grasshopper (six legs and antennae). Use only visible features.",
           "1a Body has more than 8 legs: millipede. 1b Body has 8 legs or fewer: go to 2. 2a Eight legs: spider. 2b Six legs: grasshopper. Each statement uses a feature that can be seen and counted."),
        SUM("Magnification = image size ÷ actual size, in the same units; draw with clear single lines, label lines ruled, and give a title and magnification.",
            "Annotate with structure and function; show the systems asked for on a single dissection diagram.",
            "Learn the exact method for each biochemical test and include a control; test for reducing sugar before non-reducing sugar.",
            "Keys use only visible external features; give specific habitats.",
            "Tables have units in headings; graphs have labelled axes and best-fit lines; use mean, standard deviation and percentage error; plan variables carefully."),
    ],
))

