"""Upper Sixth Biology (A Level, 0710): Plant Growth Regulators & Reproduction, Classical, Molecular & Population Genetics,
Biotechnology, Genetic Engineering & Immunology, and the Examination module.

Topic lessons use the slug prefix biu2- and the examination lessons bixu-. Content follows KKEVO's master curriculum blueprint and the
Board's 2023 subject report for exam structure and common errors; it is not a Board syllabus booklet. Every genetic cross, ratio,
chi-squared value, map distance and Hardy-Weinberg calculation was checked by script. Data labelled "invented" are teaching data.
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "upper-sixth")

M_PGR = "Plant Growth Regulators & Reproduction"
M_GEN = "Classical, Molecular & Population Genetics"
M_BIO = "Biotechnology, Genetic Engineering & Immunology"
M_EXAM = "Examination"

LESSONS = []


# ------------------------------------------------------------------ 1. Plant hormones
LESSONS.append(lesson(
    module=M_PGR,
    topic="Plant hormones",
    title="Plant growth regulators: auxins, gibberellins, cytokinins, abscisic acid and ethene",
    slug="biu2-plant-growth-regulators",
    minutes=25,
    summary="What the five plant growth regulators are made for, how auxin makes cells elongate and bend a shoot towards light, and how the regulators work together and against each other.",
    objectives=[
        "Define a plant growth regulator and say how it differs from an animal hormone",
        "Explain phototropism, gravitropism and apical dominance in terms of auxin",
        "State the main effects of gibberellins, cytokinins, abscisic acid and ethene, with uses in farming",
        "Interpret experiments on plant growth regulators and deduce what each result shows",
    ],
    key_concepts=["Plant growth regulator", "Auxin (IAA)", "Phototropism", "Apical dominance", "Gibberellin", "Cytokinin", "Abscisic acid", "Ethene"],
    blocks=[
        H("Introduction"),
        T("A trader in Mbouda wants her green bananas to turn yellow before market day. She puts them in a closed sack with a few ripe ones. "
          "Two days later they are ready. She has used a plant chemical without knowing its name. The ripe fruit gave off a gas called **ethene**, "
          "and the gas ripened the rest.\n\nPlants do not have nerves, but they still coordinate growth, flowering, ripening and leaf fall. "
          "They do this with chemical messengers. In this lesson we meet five groups of them and see how farmers use them."),
        H("What is a plant growth regulator?"),
        D("A **plant growth regulator** (plant hormone) is an organic chemical made in small amounts in one part of a plant. "
          "It affects the growth or development of the same cell, or of cells elsewhere in the plant, at very low concentration.",
          title="Definition: plant growth regulator"),
        T("Plant regulators differ from animal hormones in three ways. They are not made in special glands; many ordinary tissues make them. "
          "They are not carried round in a blood system, but move from cell to cell, through the xylem and phloem, or as a gas. "
          "And one regulator can have several different effects, depending on its **concentration** and on **which tissue** receives it."),
        H("Auxins"),
        T("The main natural auxin is **indole acetic acid (IAA)**. It is made in the **shoot tip** (apical meristem), in young leaves and in developing seeds. "
          "It is moved from cell to cell by carrier proteins, mainly downwards from the tip."),
        D("**Acid growth hypothesis.** Auxin binds to a receptor on the cell surface membrane. This activates proton pumps that move H+ ions into the cell wall. "
          "The pH of the wall falls. The acid activates wall proteins (expansins) that loosen the links between cellulose microfibrils. "
          "The wall becomes more stretchable. Water enters by osmosis, the vacuole swells and the cell **elongates**.",
          title="How auxin makes cells elongate"),
        T("**Phototropism.** A shoot grows towards one-sided light. Light causes auxin to move sideways across the tip, from the lit side to the shaded side. "
          "More auxin reaches the cells on the shaded side. They elongate more than the cells on the lit side, so the shoot bends towards the light. "
          "This brings the leaves to the light for photosynthesis."),
        T("**Gravitropism.** In a horizontal root, auxin collects on the lower side. Shoot cells are stimulated by this concentration, but root cells are **inhibited** by it. "
          "So in a root the lower side grows more slowly than the upper side and the root curves downwards. In a horizontal shoot the lower side grows faster and the shoot curves upwards. "
          "The same regulator has opposite effects on the two organs because roots are much more sensitive to auxin."),
        T("**Apical dominance.** While the apical bud is growing, auxin from it flows down the stem and prevents the lateral buds from growing. "
          "If the tip is cut off, the lateral buds grow and the plant becomes bushy. This is why farmers prune coffee, cocoa and tea bushes, and hedges."),
        T("**Uses.** A cut stem dipped in rooting powder (synthetic auxin) forms roots sooner. Spraying auxin on flowers helps fruit to set. "
          "The synthetic auxin 2,4-D kills broad-leaved weeds in cereal fields at a dose that does not harm the narrow-leaved crop."),
        IMG("al-biu2-phototropism.svg", alt="A shoot lit from the right: auxin moves across the tip to the shaded left side, the left side elongates more, and the shoot bends towards the light",
            caption="Figure 1. Phototropism. Auxin moves to the shaded side, which elongates faster."),
        H("Gibberellins, cytokinins, abscisic acid and ethene"),
        KEY("Four more regulators", "Learn each one as: where made, main effects.", cards=[
            ["Gibberellins (GA)", "Made in young leaves, shoot tips, root tips and seeds. Stimulate stem elongation, so dwarf plants treated with GA grow tall. Break seed dormancy and start germination. Stimulate flowering in some plants. Make grapes larger when sprayed on the bunches."],
            ["Cytokinins", "Made mainly in root tips and developing seeds. Stimulate cell division. Make lateral buds grow, so they oppose apical dominance. Delay the ageing (senescence) of leaves, which is why cut leaves stay green longer when sprayed."],
            ["Abscisic acid (ABA)", "Made in leaves, stems and seeds, and made faster when the plant lacks water. Causes stomata to close in water stress. Keeps seeds dormant. Generally inhibits growth."],
            ["Ethene", "A gas made by ripening fruit, ageing leaves and damaged tissue. Stimulates fruit ripening and leaf fall (abscission). Spreads from cell to cell and between plants."],
        ]),
        T("**Gibberellin and germination.** When a barley or maize seed absorbs water, the embryo releases gibberellin. The gibberellin reaches the outer layer of the endosperm (the aleurone layer) "
          "and switches on the gene for **amylase**. Amylase breaks down the starch store to sugars that feed the growing embryo. "
          "ABA has the opposite effect: it keeps the seed dormant until conditions are suitable. The balance between GA and ABA decides when a seed germinates."),
        T("**ABA and stomata.** In a drought, root cells make ABA and it travels to the leaves. ABA makes guard cells lose potassium ions. "
          "The water potential of the guard cells rises, water leaves by osmosis, the guard cells become flaccid and the stomata close. "
          "Less water is lost by transpiration, but less carbon dioxide enters as well."),
        T("**Ethene and ripening.** Ripening fruit makes ethene, and ethene stimulates more ethene production. This is a **positive feedback**, so one ripe fruit starts the process in the others. "
          "Ethene switches on enzymes that turn starch to sugar, break down pectin in cell walls (the fruit goes soft) and break down chlorophyll (green to yellow). "
          "Fruit companies pick bananas green so that they are firm in transport, then expose them to ethene in a ripening room. "
          "Ethene also activates the cells at the base of a leaf stalk (the abscission zone) so that the leaf drops. Growers also use ethene-releasing chemicals to make pineapple plants flower at the same time."),
        T("**Working together.** A high cytokinin to auxin ratio makes lateral buds grow, and a high auxin to cytokinin ratio keeps them inhibited. "
          "In tissue culture (growing plants from a few cells in sterile jelly), a high auxin to cytokinin ratio makes roots form, a high cytokinin to auxin ratio makes shoots form, "
          "and a balanced ratio makes an undifferentiated mass of cells called a **callus**. This is how farms produce thousands of identical banana, plantain and pineapple plants."),
        CODE("""Regulator       Where made            Main effects
Auxin (IAA)     shoot tip, young      cell elongation, phototropism,
                leaves                gravitropism, apical dominance
Gibberellin     young leaves, seeds   stem elongation, germination,
                                      breaks dormancy
Cytokinin       root tips, seeds      cell division, lateral buds,
                                      delays senescence
Abscisic acid   leaves, seeds         closes stomata, dormancy
Ethene          ripe fruit, old       ripening, leaf fall
                leaves (gas)""", "text", title="Summary of the five regulators"),
        EX("Worked example 1: what does the coleoptile experiment show?", intro="Oat seedlings have a protective sheath called a coleoptile. Five groups were lit from one side. "
           "(A) intact coleoptile; (B) tip cut off; (C) tip covered with an opaque cap; (D) a thin plate of mica pushed into the tip on the shaded side only; "
           "(E) a mica plate pushed into the tip on the lit side only. Predict what happens and say what each result shows.", steps=[
            S("A: intact", text="It bends towards the light. This is the normal response."),
            S("B: tip removed", text="No bending, and growth nearly stops. The tip makes something needed for growth."),
            S("C: tip covered", text="No bending. The tip must detect the light, but the bending happens lower down."),
            S("D: mica on the shaded side", text="No bending. Mica blocks movement of substances. The chemical must pass down the shaded side to cause bending."),
            S("E: mica on the lit side", text="Bending still occurs. The chemical was moving down the shaded side, which was not blocked."),
            S("Conclusion", text="The tip detects light and makes a growth-promoting chemical (auxin). The chemical moves to the shaded side and passes down it, making the shaded cells elongate more."),
        ]),
        EX("Worked example 2: apical dominance", intro="Bean plants were grown for 10 days. The mean length of the lateral bud on the first leaf node is in the table (invented teaching data). "
           "Group 1: tip left on, 2 mm. Group 2: tip cut off, 38 mm. Group 3: tip cut off and a paste containing auxin placed on the cut surface, 3 mm. "
           "Group 4: tip cut off and auxin paste on the cut, plus a drop of cytokinin placed directly on the lateral bud, 25 mm. Explain the results.", steps=[
            S("Group 1 against group 2", text="Removing the tip allows the lateral bud to grow (2 mm to 38 mm). The tip was inhibiting it."),
            S("Group 3", text="Auxin paste in place of the tip restores the inhibition (3 mm). So auxin from the tip is the inhibiting substance."),
            S("Group 4", text="Cytokinin applied to the bud overcomes the inhibition even with auxin present (25 mm). Cytokinin promotes lateral bud growth and opposes auxin."),
            S("Conclusion", text="Apical dominance is controlled by the balance of auxin from the apical bud and cytokinin. Auxin inhibits and cytokinin promotes growth of the lateral bud."),
        ]),
        TIP("In the Board's Paper 2 you may meet plant regulators in a question on coordination or on an experiment. Always say **which** regulator, **where** it is made, and **what it does to which cells**. "
            "In Paper 1, plant regulators are tested by short statements; learn the table above."),
        MISTAKE("Saying that auxin makes cells divide", "Auxin makes cells **elongate** (and gibberellin does so in stems). **Cytokinin** stimulates cell division. "
                "Write 'elongation' for auxin, 'division' for cytokinin."),
        MISTAKE("Saying auxin builds up on the lit side", "Auxin moves **away** from the light, to the **shaded** side. The shaded side then grows faster. "
                "Remember that the plant bends towards the light because the side away from the light is longer."),
        QUIZ("A farmer cuts the top off a young coffee plant. Which statement best explains why the plant becomes bushier?",
             ["Cutting the tip lets more light reach the leaves.",
              "Auxin from the tip no longer inhibits the lateral buds, so they grow.",
              "Gibberellin is stored in the tip and is released when it is cut.",
              "Ethene from the cut surface stimulates the lateral buds."], 1,
             "The apical bud supplies auxin that inhibits the lateral buds. Removing it ends the inhibition.",
             hint="Which regulator comes from the shoot tip and travels down the stem?",
             feedback=["The effect is hormonal, not about light.", "", "Gibberellin is not stored in the tip for this purpose.", "Ethene is made at wounds, but it is not what ends apical dominance."]),
        QUIZ("Which regulator would a farmer use to delay the ageing of cut leaves for sale?",
             ["Ethene", "Abscisic acid", "Cytokinin", "Auxin at high concentration"], 2,
             "Cytokinin delays senescence (ageing) of leaves.",
             hint="Which regulator is linked with cell division and keeps tissues young?",
             feedback=["Ethene speeds ageing and leaf fall.", "ABA promotes closing of stomata and dormancy, not delay of ageing.", "", "A high dose of auxin acts as a herbicide, not as a preservative."]),
        PQ("(a) Describe how auxin causes a shoot to bend towards light. (b) Explain why a horizontal root bends downwards even though auxin collects on its lower side.",
           "(a) Light on one side causes auxin to move across the tip to the shaded side. The cells on the shaded side receive more auxin. Auxin activates proton pumps that acidify the cell walls, the walls loosen, water enters by osmosis and the cells elongate. "
           "The shaded side grows faster than the lit side, so the shoot bends towards the light. "
           "(b) Auxin collects on the lower side, but root cells are very sensitive and high auxin concentrations inhibit their elongation. The lower side therefore grows more slowly than the upper side, so the root curves down."),
        PQ("Explain how gibberellin and abscisic acid together control the germination of a seed.",
           "ABA maintains dormancy. When the seed takes up water in suitable conditions the embryo releases gibberellin, and the ratio of GA to ABA rises. Gibberellin diffuses to the aleurone layer and switches on genes for amylase. "
           "Amylase hydrolyses starch in the endosperm to sugars, which are respired by the embryo for energy and used for growth. Germination begins."),
        PQ("Describe two ways in which a farmer uses ethene and two ways in which a farmer uses auxin.",
           "Ethene: ripening of bananas picked green by exposing them to ethene in a ripening room; and causing pineapple plants to flower at the same time so that the crop can be harvested together. "
           "Auxin: rooting powder on stem cuttings; selective herbicide such as 2,4-D against broad-leaved weeds in cereals; spray on flowers to help fruit set. (Any two of each.)"),
        PQ("In plant tissue culture, how would you change the ratio of cytokinin to auxin in the jelly to produce (i) roots (ii) shoots (iii) a callus?",
           "(i) A high auxin to cytokinin ratio gives roots. (ii) A high cytokinin to auxin ratio gives shoots. (iii) A roughly balanced ratio gives a callus, an undifferentiated mass of cells. The exact amounts depend on the species."),
        SUM("Plant growth regulators are made in small amounts, in many tissues, and act at low concentration; their effect depends on concentration and tissue.",
            "Auxin (IAA) makes cells elongate by acidifying the wall; it controls phototropism, gravitropism and apical dominance. Auxin moves to the shaded side of a shoot.",
            "Gibberellins promote stem growth and germination (amylase). Cytokinins promote cell division and lateral buds and delay senescence.",
            "ABA closes stomata and maintains dormancy. Ethene ripens fruit and causes leaf fall, with positive feedback.",
            "The balance of regulators, such as auxin to cytokinin, decides the outcome."),
    ],
))

# ------------------------------------------------------------------ 2. Photoperiodism
LESSONS.append(lesson(
    module=M_PGR,
    topic="Photoperiodism",
    title="Photoperiodism and phytochrome",
    slug="biu2-photoperiodism-phytochrome",
    minutes=22,
    summary="How plants measure the length of the night, the difference between short-day, long-day and day-neutral plants, and how phytochrome switches between two forms in red and far-red light.",
    objectives=[
        "Define photoperiodism and classify plants as short-day, long-day or day-neutral",
        "Explain that the length of the dark period is what the plant measures, using night-break experiments",
        "Describe phytochrome Pr and Pfr and the effect of red and far-red light",
        "Interpret tables of flowering results under different light and dark treatments",
    ],
    key_concepts=["Photoperiodism", "Short-day plant", "Long-day plant", "Critical night length", "Phytochrome", "Pr and Pfr", "Night break"],
    blocks=[
        H("Introduction"),
        T("Cameroon lies close to the equator, so the length of day hardly changes through the year: about 12 hours, all year. "
          "Farther from the equator, days are long in summer and short in winter. Many plants use this change as a calendar to decide when to flower. "
          "A plant flowering at the right time is able to set seed when pollinators are active and the weather suits it."),
        D("**Photoperiodism** is the response of an organism, such as flowering in a plant, to the relative lengths of day and night (the **photoperiod**).", title="Definition: photoperiodism"),
        H("Three kinds of plant"),
        KEY("Flowering and day length", "Plants are classified by how their flowering depends on the photoperiod.", cards=[
            ["Short-day plants (SDP)", "Flower when the night is **longer** than a critical length. Examples: chrysanthemum, poinsettia, rice varieties and soya bean varieties."],
            ["Long-day plants (LDP)", "Flower when the night is **shorter** than a critical length. Examples: spinach, lettuce, barley, some wheat varieties."],
            ["Day-neutral plants (DNP)", "Flowering does not depend on day length. Examples: tomato, cucumber, maize and sunflower in many varieties."],
        ]),
        T("The names are misleading. Experiments show that the plant is really measuring the **length of the uninterrupted dark period**. "
          "A short-day plant needs a night **longer** than its critical length, and a long-day plant needs a night **shorter** than its critical length."),
        T("Take a short-day plant with a critical night length of 10 hours. In a cycle of 14 hours of light and 10 hours of dark it flowers. "
          "In a cycle of 16 hours of light and 8 hours of dark it does not flower, because the night is too short. "
          "A long-day plant with the same critical length behaves the opposite way."),
        H("The night-break experiments"),
        T("If the dark period is broken by a short flash of light, the plant behaves as though the night were short. "
          "A flash of light in the middle of a long night stops a short-day plant from flowering. The same flash causes a long-day plant to flower. "
          "Interrupting the **day** with a short dark period has no effect. So it is the unbroken night that counts."),
        CODE("""Treatment (light : dark)        Short-day plant     Long-day plant
8 h : 16 h  (long night)       flowers             no flowers
16 h : 8 h  (short night)      no flowers          flowers
8 h : 7 h : 1 h flash : 8 h    no flowers          flowers
 (night broken by light)""", "text", title="Typical results (the critical night length is 10 hours for both)"),
        H("Phytochrome: the light detector"),
        D("**Phytochrome** is a blue-green pigment protein. It exists in two forms that convert into each other. **Pr** absorbs red light (about 660 nm). "
          "**Pfr** absorbs far-red light (about 730 nm). Absorbing red light changes Pr into Pfr. Absorbing far-red light changes Pfr back to Pr.",
          title="Definition: phytochrome"),
        IMG("al-biu2-phytochrome.svg", alt="Two boxes Pr and Pfr. An arrow from Pr to Pfr labelled red light 660 nm. An arrow from Pfr to Pr labelled far-red light 730 nm and darkness (slow)",
            caption="Figure 1. The two forms of phytochrome."),
        T("Pfr is the **active form**. Daylight contains much more red than far-red light, so during the day most phytochrome becomes Pfr. "
          "In darkness, Pfr slowly changes back to Pr (and some is broken down). At the end of a long night little Pfr remains. "
          "A short night leaves a lot of Pfr at dawn.\n\nA short-day plant needs a **low Pfr level** at the end of the night to flower: Pfr inhibits flowering in it. "
          "A long-day plant needs a **higher Pfr level**: Pfr promotes flowering in it. This explains the night-break: a flash of red light changes Pr to Pfr at once, so the plant 'sees' a short night."),
        T("A flash of red light followed immediately by a flash of far-red light has no effect at all. The far-red light turns Pfr back to Pr and cancels the red. "
          "The effect of the last flash is the one that counts. This reversibility is the evidence that phytochrome is the pigment involved."),
        T("**Florigen.** The leaves detect the photoperiod, but the flowers form in the buds. So a signal must move from the leaves to the buds. "
          "This hypothetical flowering hormone was called florigen, and a protein called FT is now believed to be the signal (textbooks differ on how they present this; check your textbook). "
          "Grafting experiments show it: if a leaf from a flowering plant is grafted onto a plant that is not flowering, the second plant also flowers."),
        T("Phytochrome has other roles. Lettuce seeds need red light to germinate, which is why small seeds buried deep do not sprout. "
          "In shade under other plants, light is rich in far-red because leaves absorb red. Pfr is low, and the stems stretch quickly to find light."),
        EX("Worked example 1: classify the plant", intro="A plant is exposed to four cycles. Cycle 1: 9 h light, 15 h dark. Cycle 2: 15 h light, 9 h dark. "
           "Cycle 3: 9 h light, 7 h dark, 1 min red light, 8 h dark. Cycle 4: 9 h light, 7 h dark, 1 min red light then 1 min far-red light, 8 h dark. "
           "It flowers only in cycles 1 and 4. Classify the plant and explain each result.", steps=[
            S("Cycles 1 and 2", text="It flowers with a 15 h night but not with a 9 h night. It needs a long night, so it is a short-day plant."),
            S("Cycle 3", text="The red flash converts Pr to Pfr and breaks the night into periods of 7 h and 8 h. Both are shorter than the critical length, so the plant does not flower."),
            S("Cycle 4", text="The far-red flash straight after the red converts Pfr back to Pr. The effect of the red flash is cancelled, so the 15 h night counts as unbroken and the plant flowers."),
            S("Conclusion", text="A short-day plant; the last flash given decides the result, which shows that phytochrome is involved."),
        ]),
        EX("Worked example 2: a consistent experiment", intro="A short-day plant has a critical night length of 11 hours. Predict whether it flowers: (i) 12 h light, 12 h dark (ii) 14 h light, 10 h dark (iii) 10 h light, 14 h dark with a 5 min red flash in the middle of the night (iv) as (iii), but the red flash is followed at once by a far-red flash.", steps=[
            S("Rule", text="A short-day plant flowers only if the **uninterrupted** dark period is longer than 11 h."),
            S("(i)", text="Dark period 12 h is more than 11 h, so it flowers."),
            S("(ii)", text="Dark period 10 h is less than 11 h, so it does not flower."),
            S("(iii)", text="The red flash converts Pr to Pfr, which breaks the night into two periods of about 7 h. Neither is longer than 11 h. It does not flower."),
            S("(iv)", text="Far-red light converts Pfr back to Pr and cancels the flash. The night is effectively unbroken at 14 h. It flowers."),
        ]),
        TIP("Paper 2 questions ask for a result **and** the reason. Write the reason in terms of the dark period and the level of Pfr. Do not write only 'it needs short days'."),
        MISTAKE("Thinking the plant measures day length", "The experiments with night-breaks show that the plant measures the length of the **uninterrupted night**. A flash of light in the day does nothing; a flash in the night changes the response."),
        MISTAKE("Mixing up Pr and Pfr", "Pr absorbs **r**ed light and becomes Pfr. Pfr absorbs **f**ar-red light and becomes Pr. Pfr is the active form."),
        QUIZ("A short-day plant is kept with 16 hours of dark each night. Halfway through the dark a flash of red light is given. What is the likely result?",
             ["It flowers, because the night is still long.", "It does not flower, because the long night has been broken into two short ones.",
              "It flowers, because red light promotes Pfr.", "It does not flower, because red light destroys phytochrome."], 1,
             "The flash converts Pr to Pfr and the plant reads two short nights of about 8 h each, below its critical length.",
             hint="What does the plant measure, and what does a flash do to the night?",
             feedback=["The night has been interrupted; it is not the total dark time that matters.", "", "Pfr inhibits flowering in a short-day plant.", "Red light does not destroy phytochrome; it converts Pr to Pfr."]),
        QUIZ("Which form of phytochrome is active, and which light converts it to the inactive form?",
             ["Pr is active; red light converts it to Pfr.", "Pfr is active; far-red light converts it to Pr.", "Pfr is active; red light converts it to Pr.", "Pr is active; far-red light converts it to Pfr."], 1,
             "Pfr is the active form. Far-red light (730 nm) changes Pfr back to Pr.",
             hint="Red makes the active one. Far-red reverses it.",
             feedback=["Pr is the inactive form.", "", "Red light converts Pr to Pfr.", "Pr is inactive and far-red converts Pfr to Pr."]),
        PQ("Explain why a short flash of light in the middle of the night prevents a short-day plant from flowering but a flash in the middle of the day has no effect.",
           "A short-day plant flowers only if the uninterrupted dark period is longer than its critical length. A flash in the night converts Pr to Pfr, which breaks the dark period into two periods each shorter than the critical length, so the plant reacts as if the night were short. "
           "A flash during the day adds light to a period that is already light, so the dark period is unchanged."),
        PQ("Describe the evidence that phytochrome is the pigment that detects the night break.",
           "Red light (about 660 nm) is the most effective at breaking the night. If a flash of far-red light (about 730 nm) is given immediately after the red flash, the effect is cancelled. This reversibility matches the interconversion of Pr and Pfr by red and far-red light, which is a property of phytochrome."),
        PQ("A garden in Buea is lit by a street lamp all night. Chrysanthemums (short-day plants) nearby fail to flower at the usual time. Explain.",
           "The lamp breaks the dark period or removes it. Light converts Pr to Pfr in the leaves, so Pfr remains high at the end of the night and the dark period is shorter than the critical length. Pfr inhibits flowering in a short-day plant, so no flowering signal is made."),
        SUM("Photoperiodism is the response to the lengths of day and night. Plants are short-day, long-day or day-neutral.",
            "The plant measures the uninterrupted dark period. Short-day plants need a night longer than a critical length, long-day plants a night shorter than it.",
            "Phytochrome has two forms: Pr changes to Pfr in red light, Pfr to Pr in far-red light and slowly in darkness. Pfr is the active form.",
            "A red flash in the night converts Pr to Pfr; a far-red flash cancels it. The last flash decides the result.",
            "A signal, florigen (now thought to be the FT protein), is made in the leaves and moves to the buds."),
    ],
))


# ------------------------------------------------------------------ 3. Reproduction in flowering plants
LESSONS.append(lesson(
    module=M_PGR,
    topic="Reproduction in flowering plants",
    title="Pollen, embryo sac and double fertilisation",
    slug="biu2-flowering-plant-reproduction",
    minutes=24,
    summary="How pollen grains and the embryo sac are made by meiosis and mitosis, what the eight nuclei of the embryo sac become, and why fertilisation in flowering plants is double.",
    objectives=[
        "Describe microsporogenesis and the structure of a mature pollen grain",
        "Describe megasporogenesis and the structure of the embryo sac",
        "Explain double fertilisation and state the chromosome number of each product",
        "Describe how the ovule becomes the seed and the ovary the fruit",
    ],
    key_concepts=["Microsporogenesis", "Megasporogenesis", "Pollen grain", "Embryo sac", "Double fertilisation", "Endosperm", "Triploid"],
    blocks=[
        H("Introduction"),
        T("A maize field near Bamenda is in flower. The tassels at the top shed yellow dust, which is pollen. The silks on the young cobs catch it. "
          "Each grain of maize on the cob is the result of one successful pollen grain reaching one ovule. Each grain formed from **two** fusions, not one. "
          "To follow this, we must see how pollen and the ovule's egg cell are made."),
        H("Alternation of generations in flowering plants"),
        T("A flowering plant is the diploid **sporophyte** (2n). It makes haploid spores by meiosis. These grow by mitosis into very small haploid structures, the **gametophytes**, "
          "which make the gametes. In flowering plants the male gametophyte is the **pollen grain** and the female gametophyte is the **embryo sac**. Both are tiny and live inside the flower."),
        H("Microsporogenesis: making pollen"),
        T("An anther has four pollen sacs. Each sac contains many diploid **pollen mother cells** (microspore mother cells). Each pollen mother cell divides by **meiosis** to give "
          "four haploid **microspores**. The nucleus of each microspore then divides once by **mitosis**, to give a **tube nucleus** and a **generative nucleus**. "
          "The microspore develops a tough wall to become a pollen grain. The outer layer (exine) is made of sporopollenin, a very resistant chemical, with patterns and pores."),
        D("**Microsporogenesis** is the production of haploid microspores from diploid pollen mother cells by meiosis, followed by the development of pollen grains. "
          "A mature pollen grain contains a tube nucleus and a generative nucleus (or two male gametes).", title="Definition: microsporogenesis"),
        T("When the grain lands on the stigma of the same species, it absorbs sugar solution and germinates. A **pollen tube** grows down through the style, controlled by the tube nucleus. "
          "The generative nucleus divides by mitosis to give **two male gametes** (haploid nuclei), either before pollination or in the tube. The tube grows toward the ovule, "
          "attracted by chemicals, enters through a small hole in the ovule, the **micropyle**, and releases the two male gametes into the embryo sac."),
        H("Megasporogenesis: making the embryo sac"),
        T("Inside the ovule, a tissue called the **nucellus** contains one diploid **megaspore mother cell**. It divides by **meiosis** to give four haploid megaspores in a row. "
          "Three degenerate. Only the one farthest from the micropyle survives. This is the **functional megaspore**. Its nucleus divides by mitosis three times without the cell dividing in between: "
          "1 nucleus, then 2, then 4, then 8. The 8 nuclei are arranged and then separated by cell walls into the **embryo sac** (female gametophyte), which has 7 cells."),
        KEY("The embryo sac", "Eight nuclei, seven cells. All are haploid.", cards=[
            ["Micropyle end", "The **egg cell** with a **synergid** on each side. The synergids help guide the pollen tube."],
            ["Centre", "One large **central cell** containing **two polar nuclei**."],
            ["Opposite end", "Three **antipodal cells**. They degenerate soon after fertilisation."],
        ]),
        IMG("al-biu2-embryo-sac.svg", alt="An ovule containing an embryo sac: egg cell and two synergids at the micropyle, two polar nuclei in the centre, three antipodal cells at the other end; a pollen tube entering the micropyle",
            caption="Figure 1. The mature embryo sac and the entry of the pollen tube."),
        H("Double fertilisation"),
        D("**Double fertilisation** is the process found only in flowering plants in which the two male gametes from one pollen tube each fuse with a different female nucleus: one with the egg cell, and one with the two polar nuclei.", title="Definition: double fertilisation"),
        T("One male gamete fuses with the egg cell to form the diploid **zygote** (n + n = 2n). This will become the embryo. "
          "The other male gamete fuses with the **two polar nuclei** to form a **triploid** (3n) nucleus. This becomes the **endosperm**, a food store of starch, oil or protein that feeds the embryo. "
          "The antipodals and synergids soon degenerate."),
        CODE("""Event                              Chromosome number (maize, 2n = 20)
Pollen mother cell                 20
Microspore (after meiosis)         10
Male gamete                        10
Megaspore mother cell              20
Functional megaspore               10
Egg cell / each polar nucleus      10
Zygote (10 + 10)                   20
Endosperm nucleus (10 + 10 + 10)   30""", "text", title="Chromosome numbers in maize"),
        H("From ovule to seed and ovary to fruit"),
        T("After fertilisation the zygote divides by mitosis to form the embryo (with a plumule, a radicle and one or two cotyledons). The endosperm nucleus divides to form the food store; "
          "in some seeds, such as the bean, the cotyledons absorb the endosperm, and in cereals like maize it is kept. The **integuments** (outer layers of the ovule) harden into the **testa** (seed coat). "
          "The ovule becomes the **seed**. The ovary wall becomes the **fruit wall** (pericarp). Other parts of the flower, such as petals and stamens, usually wither. "
          "Auxin and gibberellin from the developing seeds stimulate the ovary to grow into fruit."),
        EX("Worked example 1: chromosome counts in a plant with 2n = 14", intro="Pea has 2n = 14. Give the number of chromosomes in (a) a pollen mother cell, (b) a microspore, (c) a male gamete, (d) the zygote, (e) the endosperm nucleus.", steps=[
            S("Pollen mother cell", text="It is diploid: 14."),
            S("Microspore and male gamete", text="Meiosis halves the number: 7. Mitosis keeps it at 7, so each male gamete has 7."),
            S("Zygote", text="7 (male) + 7 (egg) = 14."),
            S("Endosperm", text="One male gamete (7) + two polar nuclei (7 + 7) = 21, which is triploid, 3n."),
        ]),
        EX("Worked example 2: counting nuclei", intro="How many mitotic divisions turn one functional megaspore into the embryo sac nuclei, and why does the embryo sac have 8 nuclei but only 7 cells?", steps=[
            S("Divisions of the nucleus", text="One nucleus becomes 2, then 4, then 8: three rounds of mitosis. The number of separate nuclear divisions is 1 + 2 + 4 = 7."),
            S("Number of cells", text="Three antipodals, two synergids and one egg cell make six cells. The central cell holds the other two nuclei (the polar nuclei) in one cell. 6 + 1 = 7 cells, 8 nuclei."),
            S("Haploid", text="All 8 nuclei came from one haploid megaspore by mitosis, so all are haploid."),
        ]),
        TIP("The Board's report notes that candidates are asked to explain, not just define. For double fertilisation write who fuses with whom, the chromosome number of each product and its fate (zygote, embryo; triploid, endosperm)."),
        MISTAKE("Saying the pollen grain is the male gamete", "The pollen grain is a **gametophyte** with a few nuclei. The male gametes are the two haploid nuclei, carried by the pollen tube."),
        MISTAKE("Giving the endosperm as 2n", "The endosperm is **triploid** (3n), because it comes from two polar nuclei plus one male gamete."),
        QUIZ("In the embryo sac, which cells or nuclei fuse with the male gametes?",
             ["The egg cell and the antipodal cells", "The egg cell and the two polar nuclei", "The synergids and the polar nuclei", "The egg cell and the synergids"], 1,
             "One male gamete fuses with the egg cell, the other with the two polar nuclei.",
             hint="One fusion makes the embryo and the other makes the food store.",
             feedback=["The antipodals degenerate and take no part.", "", "The synergids guide the pollen tube; they are not fertilised.", "Synergids are helper cells and do not fuse."]),
        QUIZ("A mature embryo sac contains",
             ["4 haploid nuclei", "8 haploid nuclei", "8 diploid nuclei", "7 haploid nuclei"], 1,
             "Three mitoses of the haploid megaspore nucleus give 8 haploid nuclei in 7 cells.",
             hint="1, 2, 4, ...",
             feedback=["Only two rounds of mitosis would give 4.", "", "They come from a haploid megaspore, so none is diploid.", "There are 7 cells, but 8 nuclei."]),
        PQ("Outline how a mature pollen grain is formed from a pollen mother cell and state the chromosome number at each stage in a plant with 2n = 20.",
           "A diploid pollen mother cell (20) divides by meiosis to form four haploid microspores (10). Each microspore nucleus divides once by mitosis to form a tube nucleus and a generative nucleus (each 10). A tough wall forms round it, and the grain is released from the anther. The generative nucleus later divides again to give two male gametes (10 each)."),
        PQ("Describe the structure of the embryo sac and explain how it forms.",
           "A diploid megaspore mother cell in the nucellus divides by meiosis to give four haploid megaspores. Three degenerate. The survivor's nucleus divides three times by mitosis to give 8 nuclei, which are enclosed in 7 cells: an egg cell and two synergids at the micropyle, a central cell with two polar nuclei, and three antipodal cells at the other end."),
        PQ("Explain the importance of double fertilisation and what happens to the ovule and ovary afterwards.",
           "One male gamete fuses with the egg to make the diploid zygote that grows into the embryo; the other fuses with the two polar nuclei to make triploid endosperm. Endosperm is only made if fertilisation has happened, so the plant does not waste food on unfertilised ovules. Afterwards the ovule becomes the seed (integuments form the testa) and the ovary becomes the fruit."),
        SUM("A pollen mother cell makes four haploid microspores by meiosis; mitosis gives a grain with a tube and a generative nucleus, which gives two male gametes.",
            "A megaspore mother cell makes four megaspores; one survives and divides by mitosis three times to give 8 haploid nuclei in 7 cells.",
            "Double fertilisation: one male gamete + egg = zygote (2n); another + two polar nuclei = endosperm (3n).",
            "The ovule becomes the seed; the integuments become the testa; the ovary becomes the fruit."),
    ],
))

# ------------------------------------------------------------------ 4. Human gametogenesis and the menstrual cycle
LESSONS.append(lesson(
    module=M_PGR,
    topic="Human gametogenesis and the menstrual cycle",
    title="Gametogenesis and the hormonal control of the menstrual cycle",
    slug="biu2-gametogenesis-menstrual-cycle",
    minutes=25,
    summary="How sperm and egg cells are made, how they differ, and how FSH, LH, oestrogen and progesterone control the ovarian and uterine cycles through feedback.",
    objectives=[
        "Describe spermatogenesis and oogenesis and state the chromosome number at each stage",
        "Compare the two processes (number of gametes, timing, polar bodies)",
        "Explain the roles of FSH, LH, oestrogen and progesterone in the menstrual cycle",
        "Interpret hormone graphs and explain how the contraceptive pill works",
    ],
    key_concepts=["Spermatogenesis", "Oogenesis", "Polar body", "FSH and LH", "Oestrogen and progesterone", "Follicle and corpus luteum", "Negative and positive feedback"],
    blocks=[
        H("Introduction"),
        T("Every month in a healthy adult woman the lining of the uterus is built up, and, if no pregnancy occurs, shed. This takes about four weeks, and it happens in step with changes in the ovary. "
          "One organ helps another because hormones link them. This lesson shows how gametes are made and how the hormones set the timing."),
        H("Spermatogenesis"),
        T("Sperm are made in the **seminiferous tubules** of the testes from puberty onwards, continuously. The stages are:"),
        CODE("""Stage                       Cell                      Chromosomes
Multiplication (mitosis)    Spermatogonium             46 (2n)
Growth                      Primary spermatocyte       46 (2n)
Meiosis I                   2 secondary spermatocytes  23 (n)
Meiosis II                  4 spermatids               23 (n)
Differentiation             4 sperm                    23 (n)""", "text", title="Spermatogenesis"),
        T("Spermatids change into sperm with a head (nucleus and **acrosome** full of enzymes), a middle piece with many mitochondria and a tail (flagellum). "
          "Sertoli cells in the tubule wall nourish the developing sperm. Leydig cells between the tubules make testosterone."),
        H("Oogenesis"),
        T("Oogenesis happens in the ovary. Compared with spermatogenesis it has three striking differences: it begins before birth, it pauses for years, and each primary oocyte gives one ovum, not four."),
        CODE("""Stage                           Cell                          When
Multiplication (mitosis)        Oogonia -> primary oocyte     before birth
Meiosis I begins, then stops    Primary oocyte (46)           stays in prophase I
                                                              until puberty
Meiosis I completes             Secondary oocyte (23) +       just before
                                first polar body (23)         ovulation
Meiosis II                      Ovum (23) + second polar      only after sperm
                                body                          has entered
Polar bodies                    Small, die                    ----""", "text", title="Oogenesis"),
        T("The cytoplasm divides unequally, so the secondary oocyte keeps almost all the cytoplasm and food reserves, and the polar bodies are tiny and degenerate. "
          "This is an advantage: the one egg that is made is large and well supplied for the early embryo. A woman is born with all the primary oocytes she will have, "
          "and only a few hundred will ever be released as secondary oocytes."),
        D("The **menstrual cycle** is the cycle of about 28 days in which an egg develops in the ovary and is released, the lining of the uterus (the **endometrium**) thickens to receive an embryo, "
          "and, if no embryo implants, the lining is shed in **menstruation**. The length of the cycle varies from woman to woman; 28 days is the textbook average, with ovulation about day 14.", title="Definition: menstrual cycle"),
        H("Hormones in the cycle"),
        KEY("Four hormones to know", "Where each is made and what it does.", cards=[
            ["FSH (follicle-stimulating hormone)", "From the anterior pituitary. Stimulates growth of follicles in the ovary and stimulates the follicle cells to make oestrogen."],
            ["LH (luteinising hormone)", "From the anterior pituitary. A surge triggers ovulation and the change of the burst follicle into the corpus luteum."],
            ["Oestrogen", "From the follicle (and the corpus luteum). Repairs and thickens the endometrium. In low amounts it inhibits FSH. At a high level it stimulates the LH surge."],
            ["Progesterone", "From the corpus luteum. Maintains the endometrium and makes it secretory and rich in blood vessels. Inhibits FSH and LH (negative feedback)."],
        ]),
        IMG("al-biu2-menstrual-cycle.svg", alt="Graph over 28 days with four curves: FSH with a small peak around day 13, LH with a sharp peak at day 14, oestrogen with a peak just before day 14 and a smaller peak around day 21, progesterone rising after day 14 and falling at day 26; ovulation marked at day 14 and menstruation on days 1 to 4",
            caption="Figure 1. An idealised menstrual cycle (hormone levels are drawn qualitatively)."),
        T("**Days 1 to 5 (menstruation).** Levels of oestrogen and progesterone are low. Low progesterone and oestrogen no longer inhibit the pituitary, so **FSH** rises. The endometrium breaks down and is shed.\n\n"
          "**Days 6 to 13 (follicular phase).** FSH stimulates several follicles to grow, and one becomes dominant. The follicle makes **oestrogen**, which rises. Oestrogen repairs and thickens the endometrium. "
          "Early on, a low level of oestrogen inhibits FSH (negative feedback), so only one follicle goes on.\n\n"
          "**Around day 13.** Oestrogen reaches a high level for a few days. At this high level it has a **positive feedback** effect on the pituitary and causes a surge of **LH** and a smaller rise of FSH.\n\n"
          "**Day 14 (ovulation).** The LH surge makes the follicle wall burst and the secondary oocyte is released.\n\n"
          "**Days 15 to 28 (luteal phase).** Under LH, the burst follicle becomes the **corpus luteum**, which makes **progesterone** and some oestrogen. Progesterone prepares and maintains the endometrium. "
          "High progesterone and oestrogen inhibit the pituitary, so FSH and LH levels fall and no new follicle develops.\n\n"
          "**If there is no pregnancy,** the corpus luteum degenerates after about 10 to 12 days. Progesterone and oestrogen fall. The endometrium cannot be maintained and menstruation starts a new cycle. "
          "**If there is a pregnancy,** the embryo makes a hormone that rescues the corpus luteum (next lesson)."),
        H("Contraception and the pill"),
        T("The combined contraceptive pill contains synthetic oestrogen and progesterone. Taken every day, it keeps these hormones at a steady level that inhibits FSH and LH release by negative feedback. "
          "With no FSH, follicles do not develop. With no LH surge, there is no ovulation. The pill also thickens the mucus in the cervix. "
          "Like any medicine, it has benefits and risks. A health worker or doctor should advise on its use."),
        EX("Worked example 1: oogenesis and chromosome numbers", intro="A primary oocyte has 46 chromosomes. State the number of chromosomes and the number of chromatids per chromosome after (a) ovulation (b) fertilisation, and explain why a woman can have a first polar body without a second.", steps=[
            S("At ovulation", text="Meiosis I has just finished. The secondary oocyte has 23 chromosomes, each made of two chromatids. (The first polar body has 23 as well.)"),
            S("Fertilisation", text="Entry of the sperm triggers meiosis II. The chromatids separate. The ovum has 23 single chromatid chromosomes and the second polar body gets the other 23. The sperm nucleus (23) then fuses with the ovum nucleus (23) to give 46."),
            S("Polar bodies", text="The first polar body forms at the end of meiosis I, just before ovulation. The second only forms if meiosis II is triggered by a sperm, so an unfertilised egg has only the first."),
        ]),
        EX("Worked example 2: reading the graph", intro="Using the cycle in Figure 1, explain (a) why LH peaks on day 14 (b) why menstruation begins at about day 28 (c) why the pill prevents ovulation.", steps=[
            S("(a) LH peak", text="Oestrogen from the large follicle reaches a high level for a few days. At this level its effect on the pituitary is positive, producing the LH surge."),
            S("(b) Menstruation", text="With no pregnancy the corpus luteum degenerates. Progesterone and oestrogen fall. The endometrium loses its support and breaks down."),
            S("(c) The pill", text="Steady synthetic hormones inhibit FSH and LH by negative feedback. Without FSH, follicles do not mature; without an LH surge, there is no ovulation."),
        ]),
        TIP("Graph questions: say what rises or falls, name the hormone and its source, then link the cause to the effect. Words such as 'because' show that you explain."),
        MISTAKE("Saying the corpus luteum makes LH", "The corpus luteum is **made by** LH and **makes progesterone**. FSH and LH come from the anterior pituitary, not the ovary."),
        MISTAKE("Saying four eggs come from one oocyte", "Oogenesis produces one ovum and two or three polar bodies. Spermatogenesis makes four sperm."),
        QUIZ("Which hormone causes ovulation?",
             ["FSH", "Progesterone", "LH", "Oestrogen at a low level"], 2,
             "A surge of LH triggers ovulation (it follows a high level of oestrogen that has positive feedback on the pituitary).",
             hint="Which pituitary hormone peaks sharply at the middle of the cycle?",
             feedback=["FSH stimulates follicle growth.", "Progesterone is made after ovulation.", "", "A low level of oestrogen inhibits the pituitary; a high level stimulates it."]),
        QUIZ("Which statement about spermatogenesis and oogenesis is correct?",
             ["Both produce four gametes from each primary cell.", "Oogenesis starts before birth; spermatogenesis starts at puberty.", "Both continue without a pause from puberty.", "Both produce polar bodies."], 1,
             "Oogonia multiply and begin meiosis before birth; sperm formation begins at puberty.",
             hint="Think about timing.",
             feedback=["Oogenesis gives one ovum.", "", "Primary oocytes pause in prophase I for years.", "Only oogenesis makes polar bodies."]),
        PQ("Compare spermatogenesis and oogenesis. Give three differences.",
           "(1) Spermatogenesis makes four equal-sized gametes from one primary spermatocyte; oogenesis makes one large ovum and polar bodies. (2) Spermatogenesis starts at puberty and continues; oogenesis begins before birth, pauses in prophase I and resumes at puberty, one oocyte per cycle. (3) Spermatids must change shape into sperm; the oocyte is not changed in shape but is large and has food reserves. (4) Meiosis II of the oocyte completes only after fertilisation."),
        PQ("Explain how the level of oestrogen controls the secretion of FSH and LH during the first half of the cycle.",
           "At the start, FSH stimulates the follicle to grow and make oestrogen. A low to moderate oestrogen level inhibits FSH (negative feedback), so FSH falls and only the best follicle continues. When oestrogen reaches a high level near day 13 it has positive feedback on the pituitary, causing a surge of LH (and a smaller rise of FSH) that triggers ovulation."),
        PQ("Describe the roles of the corpus luteum in the cycle and explain what happens to it if the egg is not fertilised.",
           "The corpus luteum forms from the burst follicle under LH. It makes progesterone and some oestrogen, which maintain the thickened, vascular endometrium and inhibit FSH and LH. If no embryo implants it degenerates in about 10 to 12 days. Progesterone falls, the endometrium breaks down and menstruation starts. The fall in hormones releases the pituitary from inhibition and FSH rises."),
        PQ("Explain how the combined pill stops a woman from becoming pregnant.",
           "The synthetic oestrogen and progesterone keep blood levels of these hormones steady and high. They inhibit the pituitary by negative feedback so FSH and LH are low. Follicles do not mature and there is no LH surge, so there is no ovulation. No egg means no fertilisation. The pill also makes cervical mucus thick, which hinders sperm."),
        SUM("Spermatogenesis: one primary spermatocyte makes four sperm. Oogenesis: one primary oocyte makes one ovum and polar bodies; meiosis I pauses until puberty and II ends after fertilisation.",
            "FSH grows the follicle; the follicle makes oestrogen; a high oestrogen level causes the LH surge; LH causes ovulation and forms the corpus luteum.",
            "The corpus luteum makes progesterone, which maintains the endometrium and inhibits FSH and LH.",
            "If no pregnancy, the corpus luteum degenerates, hormone levels fall and menstruation follows.",
            "The pill uses steady hormones to inhibit FSH and LH so that ovulation does not occur."),
    ],
))

# ------------------------------------------------------------------ 5. Pregnancy and birth
LESSONS.append(lesson(
    module=M_PGR,
    topic="Pregnancy and birth",
    title="Fertilisation, implantation, the placenta, birth and lactation",
    slug="biu2-pregnancy-birth-lactation",
    minutes=24,
    summary="What happens from fertilisation to implantation, what the placenta does, how positive feedback and oxytocin drive birth, and how prolactin and oxytocin control milk.",
    objectives=[
        "Describe fertilisation, the acrosome reaction and early development to implantation",
        "Explain how hCG maintains the corpus luteum and how the placenta takes over hormone production",
        "Describe the functions of the placenta and the amnion",
        "Explain parturition as positive feedback and describe the hormonal control of lactation",
    ],
    key_concepts=["Acrosome reaction", "Implantation", "hCG", "Placenta", "Oxytocin", "Positive feedback", "Prolactin", "Lactation"],
    blocks=[
        H("Introduction"),
        T("A nurse at a health centre in Garoua explains to a young woman that a pregnancy test measures a hormone made by the embryo. "
          "The same visit may cover how the baby is fed and when labour starts. All of these stages are controlled by chemical signals. "
          "In this lesson we follow them from fertilisation to feeding."),
        H("Fertilisation and early development"),
        T("Fertilisation usually occurs in the upper part of the **oviduct** (fallopian tube). Many sperm reach the egg but only one fertilises it. "
          "The sperm head releases enzymes from its **acrosome** that digest the jelly-like layer round the oocyte (the **acrosome reaction**). The sperm membrane fuses with the egg membrane. "
          "This triggers the **cortical reaction**: granules just under the egg surface release substances that harden the outer layer, so no further sperm can enter. "
          "The oocyte completes meiosis II, and the sperm and egg nuclei fuse to form the diploid **zygote**."),
        T("The zygote divides by mitosis as it travels down the oviduct (cleavage). After about four days it is a solid ball of cells, the **morula**; then a hollow ball, the **blastocyst**, with an outer layer, the **trophoblast**, and an inner cell mass that will form the embryo. "
          "About six to seven days after fertilisation the blastocyst sticks to the endometrium and sinks into it. This is **implantation**. The exact days vary slightly between textbooks; check yours."),
        H("Hormones of early pregnancy"),
        T("After implantation, the trophoblast cells secrete **human chorionic gonadotrophin (hCG)**. hCG acts like LH and keeps the **corpus luteum** alive. "
          "The corpus luteum continues to make progesterone and oestrogen, so the endometrium is not shed and menstruation does not occur. "
          "hCG is excreted in urine. Home pregnancy tests detect it using antibodies, as the next topics show."),
        T("From about the 10th to 12th week the **placenta** itself makes large amounts of progesterone and oestrogen, and the corpus luteum degenerates. Progesterone maintains the uterus lining and inhibits contraction of the uterine muscle during pregnancy."),
        H("The placenta and the membranes"),
        D("The **placenta** is a disc-shaped organ formed from the embryo's tissue (the chorion, with finger-like **chorionic villi**) and the mother's endometrium. It exchanges materials between mother and fetus without the two bloodstreams mixing.", title="Definition: placenta"),
        KEY("Functions of the placenta", "The villi give a large surface area, and the barrier is very thin.", cards=[
            ["Exchange", "Oxygen, glucose, amino acids, vitamins, minerals and water pass from mother to fetus. Carbon dioxide and urea pass from fetus to mother. Fetal haemoglobin has a higher affinity for oxygen than adult haemoglobin, so oxygen moves to the fetus."],
            ["Hormones", "Makes progesterone and oestrogen from the third month, and also hCG."],
            ["Protection", "Acts as a barrier to many bacteria and to the mother's blood pressure. IgG antibodies cross it, giving the baby passive immunity. Some viruses, alcohol and some drugs can cross, so a pregnant woman should take medicine only on advice."],
        ]),
        T("The fetus is surrounded by the **amnion**, a membrane enclosing **amniotic fluid**. The fluid cushions the fetus against knocks, keeps temperature constant, allows the fetus to move, and helps the lungs to develop. "
          "The fetus is connected to the placenta by the **umbilical cord**, with two umbilical arteries (carrying deoxygenated blood to the placenta) and one umbilical vein (carrying oxygenated blood to the fetus)."),
        H("Parturition (birth)"),
        T("Birth takes place about 38 weeks after fertilisation (40 weeks after the last period). Several changes prepare the uterus. "
          "The level of progesterone falls compared with oestrogen, so the uterus muscle (myometrium) becomes more sensitive. The fetus and placenta make prostaglandins. "
          "Oxytocin, a hormone made in the hypothalamus and released from the **posterior pituitary**, causes strong contractions of the myometrium. "
          "The first contractions push the baby's head against the cervix. Stretch receptors in the cervix send impulses to the hypothalamus, and more oxytocin is released. "
          "More oxytocin causes stronger contractions, which push the head harder against the cervix, and so on."),
        D("**Positive feedback** is a process in which a change causes further change in the same direction. Birth is a positive feedback loop: contractions stretch the cervix, stretch stimulates oxytocin release, and oxytocin increases contractions. The loop ends when the baby is born and the stretch stops.", title="Definition: positive feedback"),
        T("After the baby is born the placenta (afterbirth) is expelled, and the uterus contracts to its normal size under oxytocin, which reduces bleeding."),
        H("Lactation"),
        T("During pregnancy, oestrogen and progesterone build up the milk-secreting tissue of the breasts but prevent milk release. After birth, their levels fall. "
          "**Prolactin**, from the anterior pituitary, stimulates the alveolar cells to **make milk**. "
          "When the baby suckles, receptors in the nipple send impulses to the hypothalamus, which stimulates **oxytocin** release from the posterior pituitary. Oxytocin makes the muscle cells round the alveoli contract and **eject milk** (the let-down reflex). "
          "Suckling also stimulates more prolactin secretion, so the more the baby feeds, the more milk is made. "
          "The first milk, **colostrum**, is rich in antibodies and protein. Breast milk supplies the baby's nutrients and gives passive immunity; the World Health Organisation recommends exclusive breastfeeding for the first six months for most babies."),
        EX("Worked example 1: why does the pregnancy test work?", intro="A pregnancy test detects hCG in urine. Explain why it is positive from about the second week after fertilisation and why the level of hCG in a woman is useful for the first three months only.", steps=[
            S("Source", text="hCG is made by the trophoblast cells of the embryo after implantation, about a week after fertilisation. It appears in the blood and then the urine."),
            S("Why it is needed", text="hCG keeps the corpus luteum alive so progesterone is still made and the endometrium is retained."),
            S("Fall in level", text="After about 10 to 12 weeks the placenta makes enough progesterone itself. The corpus luteum is no longer needed and hCG falls."),
        ]),
        EX("Worked example 2: trace the positive feedback in labour", intro="Write the steps of the loop in order and say how the loop ends.", steps=[
            S("Start", text="The fetal head presses on the cervix and stretches it."),
            S("Signal", text="Stretch receptors send nerve impulses to the hypothalamus."),
            S("Hormone", text="The hypothalamus makes the posterior pituitary release more oxytocin."),
            S("Effect", text="Oxytocin makes the myometrium contract more strongly, which pushes the head harder against the cervix."),
            S("End", text="The loop continues until the baby is born; then the stretch stops and so does the oxytocin surge."),
        ]),
        TIP("When a question says 'explain' for birth, the marks are for the **loop** (stretch, oxytocin, stronger contractions, more stretch), not only for naming oxytocin."),
        MISTAKE("Saying oxytocin is made by the pituitary", "Oxytocin is made by neurosecretory cells in the hypothalamus and **released** from the posterior pituitary. Prolactin is made in the anterior pituitary."),
        MISTAKE("Saying mother and baby blood mix in the placenta", "The bloodstreams are separate. Materials cross by diffusion, facilitated diffusion and active transport through the thin barrier."),
        QUIZ("What is the function of hCG in early pregnancy?",
             ["It stimulates contractions of the uterus.", "It maintains the corpus luteum so that progesterone production continues.", "It stimulates the production of milk.", "It triggers ovulation."], 1,
             "hCG, made by the trophoblast, acts like LH and keeps the corpus luteum making progesterone.",
             hint="Which structure would otherwise break down at the end of the cycle?",
             feedback=["That is oxytocin.", "", "That is prolactin.", "That is the LH surge before pregnancy."]),
        QUIZ("Why is the control of birth an example of positive feedback?",
             ["Because contractions reduce the amount of oxytocin.", "Because stretching the cervix causes oxytocin release, which causes stronger contractions that stretch the cervix more.", "Because oxytocin is stopped when levels are too high.", "Because progesterone rises in labour."], 1,
             "The output (contractions) increases the input (stretch) that triggered it.",
             hint="Positive feedback amplifies the original change.",
             feedback=["Contractions increase oxytocin release, not reduce it.", "", "That would be negative feedback.", "Progesterone relative to oestrogen falls near birth."]),
        PQ("Describe what happens from the moment a sperm touches the egg to the formation of the zygote.",
           "The acrosome releases enzymes that digest the layer round the oocyte. The sperm membrane fuses with the oocyte membrane and the sperm nucleus enters. This triggers the cortical reaction, in which granules release substances that harden the outer layer so no other sperm can enter. The oocyte completes meiosis II, producing the ovum and a second polar body. The nuclei of sperm and ovum fuse to form the diploid zygote."),
        PQ("State four functions of the placenta.",
           "Exchange of oxygen, nutrients, carbon dioxide and urea between maternal and fetal blood by diffusion and active transport; secretion of progesterone and oestrogen (and hCG); barrier that keeps maternal and fetal blood separate and filters many pathogens; allows IgG antibodies to pass to give passive immunity; attaches the fetus to the uterus wall."),
        PQ("Describe the hormonal control of lactation, including the roles of prolactin and oxytocin.",
           "During pregnancy, high oestrogen and progesterone develop the milk glands but prevent milk release. After birth these fall and prolactin from the anterior pituitary stimulates milk production in the alveoli. Suckling stimulates sensory nerves, impulses reach the hypothalamus and oxytocin is released from the posterior pituitary, causing the muscle cells round the alveoli to contract and eject milk. Suckling also increases prolactin, so supply matches demand."),
        PQ("Explain why a woman who is pregnant does not have a menstrual period.",
           "After implantation, hCG from the trophoblast keeps the corpus luteum alive, and later the placenta itself makes progesterone and oestrogen. These hormones maintain the endometrium and inhibit the pituitary release of FSH and LH, so there is no new follicle, no ovulation and no loss of the endometrium."),
        SUM("Fertilisation: acrosome reaction, cortical reaction, fusion of nuclei. The zygote becomes a blastocyst that implants after about a week.",
            "hCG from the trophoblast keeps the corpus luteum making progesterone; later the placenta makes progesterone and oestrogen.",
            "The placenta exchanges materials, makes hormones and protects the fetus; the amnion holds fluid that cushions it.",
            "Birth is positive feedback: stretch, oxytocin, stronger contractions, more stretch.",
            "Prolactin makes milk; oxytocin ejects it; suckling stimulates both."),
    ],
))


# ------------------------------------------------------------------ 6. Monohybrid crosses, codominance, multiple alleles, sex linkage
LESSONS.append(lesson(
    module=M_GEN,
    topic="Monohybrid and dihybrid crosses",
    title="Monohybrid crosses, codominance, multiple alleles and sex linkage",
    slug="biu2-monohybrid-codominance-sex-linkage",
    minutes=25,
    summary="Working through monohybrid crosses with correct symbols, and extending them to codominance (sickle cell), multiple alleles (ABO blood groups) and X-linked inheritance (colour blindness).",
    objectives=[
        "Use genetic terms and symbols correctly and set out a monohybrid cross with gametes and a Punnett square",
        "Work out genotypes and probabilities for crosses involving codominance and multiple alleles",
        "Explain sex linkage and predict the outcomes of X-linked crosses",
        "Use a test cross and a family tree to deduce unknown genotypes",
    ],
    key_concepts=["Allele", "Genotype and phenotype", "Homozygous and heterozygous", "Codominance", "Multiple alleles", "Sex linkage", "Test cross"],
    blocks=[
        H("Introduction"),
        T("A couple in Yaounde learn that both are carriers of the sickle cell allele. A health worker explains that each child has a one in four chance of the disease. "
          "This answer comes from the rules of inheritance that Gregor Mendel found in pea plants in the 1860s. "
          "In this lesson we use the rules for ordinary dominance, and then for codominance, multiple alleles and genes on the X chromosome."),
        H("Terms and symbols"),
        D("An **allele** is one of the alternative forms of a gene. A person with two identical alleles is **homozygous**; a person with two different alleles is **heterozygous**. "
          "The **genotype** is the combination of alleles. The **phenotype** is the visible or measurable result, produced by the genotype together with the environment.", title="Key terms"),
        T("Use **one letter** for each gene: a capital for the dominant allele and the same letter in lower case for the recessive. For tallness in peas, write T and t, not T and D. "
          "The Board's examiners note that candidates lose marks by using four different letters for two genes. "
          "Show every cross in the same order: parents' phenotypes, parents' genotypes, gametes, offspring genotypes, offspring phenotypes and ratio."),
        H("Monohybrid inheritance"),
        T("A cross between heterozygous parents (Tt × Tt) gives gametes T and t from each parent. The Punnett square joins them at random:"),
        CODE("""             Gametes from pollen parent
               T        t
Gametes   T    TT       Tt
from      t    Tt       tt
egg parent

Genotypes: 1 TT : 2 Tt : 1 tt
Phenotypes: 3 tall : 1 dwarf""", "text", title="Tt x Tt"),
        T("The ratio 3 : 1 only appears in large numbers, because each fertilisation is a separate chance event. "
          "A family of four children does not have to contain exactly one affected child."),
        D("A **test cross** crosses an individual of dominant phenotype but unknown genotype with a homozygous recessive. If the unknown is TT, all offspring are tall. If it is Tt, half are tall and half are dwarf (1 : 1).", title="Definition: test cross"),
        H("Codominance"),
        D("Alleles are **codominant** when both are fully expressed in the heterozygote. Neither hides the other.", title="Definition: codominance"),
        T("The gene for the beta chain of haemoglobin has two common alleles in West and Central Africa: HbA (normal) and HbS (sickle). "
          "HbA HbA people are normal. HbS HbS people have sickle cell disease. HbA HbS people (carriers, sickle cell trait) make **both** kinds of haemoglobin. "
          "Because both are made, the alleles are codominant. Textbooks write them as Hb^A and Hb^S; in the examples below we write them as A and S for brevity."),
        CODE("""Carrier x carrier (AS x AS)

        A     S
  A    AA    AS
  S    AS    SS

1 AA : 2 AS : 1 SS
Probability of a child with the disease (SS) = 1/4
Probability of a carrier = 1/2""", "text", title="Sickle cell cross"),
        T("The sickle cell allele is common in parts of Africa because carriers are less likely to die from severe malaria. This is called **heterozygote advantage**."),
        H("Multiple alleles: the ABO blood groups"),
        T("A gene can have more than two alleles in a population, although each person has only two. The ABO blood group gene has three alleles: I^A, I^B and i. "
          "I^A and I^B are both dominant to i, and are codominant with each other."),
        CODE("""Phenotype (blood group)   Possible genotypes
A                        IA IA   or   IA i
B                        IB IB   or   IB i
AB                       IA IB
O                        i i""", "text", title="ABO genotypes"),
        T("Compare the cross between a group A parent (I^A i) and a group B parent (I^B i). The gametes are I^A or i, and I^B or i. The four combinations are I^A I^B, I^A i, I^B i and i i. "
          "So the children are AB, A, B and O in the ratio 1 : 1 : 1 : 1. A pair of parents with groups A and B can have a child of **any** blood group."),
        H("Sex linkage"),
        T("In humans, females are XX and males XY. The X chromosome is much larger than the Y and carries many genes with no matching gene on the Y. "
          "Genes on the X chromosome are **sex-linked**. Because a male has only one X, a recessive allele on it is expressed, even if there is only one copy."),
        D("**Sex linkage** is the inheritance of a gene that lies on a sex chromosome (here the X). Characteristics determined by recessive X-linked alleles appear more often in males than in females.", title="Definition: sex linkage"),
        T("Red-green colour blindness and haemophilia are X-linked recessive. Use X^B for normal vision and X^b for colour blindness. A man's genotype is X^B Y (normal) or X^b Y (colour-blind). "
          "A woman is X^B X^B (normal), X^B X^b (carrier, normal) or X^b X^b (colour-blind)."),
        CODE("""Carrier woman x normal man  (XB Xb  x  XB Y)

          XB       Y
  XB    XB XB    XB Y
  Xb    XB Xb    Xb Y

Daughters: all normal (1/2 normal, 1/2 carrier)
Sons: 1/2 normal, 1/2 colour-blind
Overall: 1/4 colour-blind (all of them boys)""", "text", title="X-linked cross"),
        T("A colour-blind father cannot pass the allele to his son, because the son gets his Y from his father. He passes it to **all his daughters**, who become carriers if their mother is homozygous normal."),
        EX("Worked example 1: sickle cell probabilities", intro="Two carriers (AS) plan to have two children. Find (a) the probability that a child has sickle cell disease, (b) the probability that both children have the disease, (c) the probability that a healthy-looking child (not SS) is a carrier.", steps=[
            S("(a)", math=r"P(SS) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}"),
            S("(b)", math=r"P(\text{both SS}) = \frac{1}{4} \times \frac{1}{4} = \frac{1}{16}"),
            S("(c)", text="A healthy-looking child is AA (1/4) or AS (2/4), so three outcomes out of four are possible. The probability that such a child is a carrier:", math=r"\frac{2/4}{3/4} = \frac{2}{3}"),
        ]),
        EX("Worked example 2: blood groups and a doubtful father", intro="A mother is group A. Her child is group O. A man of group AB is named as the father. Can he be the father?", steps=[
            S("Child's genotype", text="Group O is i i. The child got one i from the mother and one from the father."),
            S("Mother", text="She is group A and gave an i, so her genotype is I^A i."),
            S("Father", text="The father must also have given an i. A group AB man is I^A I^B and has no i allele."),
            S("Conclusion", text="He **cannot** be the father. Blood groups can exclude a man but cannot prove he is the father, since many men share the same group."),
        ]),
        EX("Worked example 3: X-linked cross", intro="A colour-blind man marries a woman who is a carrier. What fraction of their daughters will be colour-blind?", steps=[
            S("Parents", text="Man X^b Y; woman X^B X^b."),
            S("Gametes", text="Man: X^b or Y. Woman: X^B or X^b."),
            S("Daughters", text="A daughter gets X^b from her father. From her mother she gets X^B (carrier) or X^b (colour-blind). So half of the daughters are colour-blind and half are carriers."),
            S("Answer", math=r"\frac{1}{2}"),
        ]),
        TIP("In Paper 2 genetics questions, state the key to your symbols first, for example 'T = tall, t = dwarf', then follow the sequence parents, gametes, offspring, ratio. Show gametes as single letters in circles or a list, not as pairs."),
        MISTAKE("Using different letters for the same gene", "Use the **same letter** in capital and lower case. Writing G, S, R and T for two genes is a common error noted by the Board."),
        MISTAKE("Giving sons the X from the father", "A son gets his Y from his father and his X from his mother. So an X-linked recessive allele in a son comes from his **mother**."),
        QUIZ("A man with sickle cell trait (AS) has children with a woman who is also AS. What is the probability that their child is a carrier like them?",
             ["1/4", "1/2", "3/4", "1"], 1,
             "Of the four combinations, AS arises twice (A from father with S from mother, and S from father with A from mother).",
             hint="Draw the Punnett square.",
             feedback=["1/4 is the probability of SS (or of AA).", "", "3/4 is the probability the child does not have the disease.", "Not all children are carriers."]),
        QUIZ("Which cross could produce a colour-blind daughter?",
             ["X^B X^B  ×  X^b Y", "X^B X^b  ×  X^B Y", "X^B X^b  ×  X^b Y", "X^B X^B  ×  X^B Y"], 2,
             "A daughter must receive an X^b from each parent. The father must be X^b Y, and the mother must carry X^b.",
             hint="A daughter needs a recessive allele from both parents.",
             feedback=["All daughters would be carriers; the father's X^b is not matched by a second allele.", "The father is normal and gives only X^B, so no daughter can be colour-blind.", "", "No recessive allele present."]),
        PQ("A man of blood group B and a woman of blood group A have a child of group O. Give the genotypes of the parents and state the probability that their next child is group AB.",
           "Group O child is i i, so each parent has an i. Father group B with an i is I^B i. Mother group A with an i is I^A i. Gametes I^A, i from mother and I^B, i from father. Offspring: I^A I^B (AB), I^A i (A), I^B i (B), i i (O), each 1/4. The probability of group AB is 1/4."),
        PQ("Haemophilia is caused by an X-linked recessive allele (X^h). A woman who is not affected has a haemophilic father. She marries an unaffected man. Show the probability that a son will be haemophilic.",
           "Her father is X^h Y, and he gave her his X, so she is X^H X^h (a carrier). Her husband is X^H Y. Gametes: mother X^H or X^h; father X^H or Y. Sons are X^H Y or X^h Y, each with probability 1/2 among the sons. So the probability that a son is haemophilic is 1/2 (and the probability that a given child is a haemophilic boy is 1/4)."),
        PQ("In cattle, red coat (R) and white coat (W) are codominant: the heterozygote has a roan coat. Predict the offspring of a roan bull and a roan cow, and explain how this differs from complete dominance.",
           "Roan RW × roan RW gives gametes R or W from each parent. Offspring: 1 RR (red) : 2 RW (roan) : 1 WW (white). There are three phenotypes in the ratio 1 : 2 : 1, matching the genotypes. With complete dominance the heterozygote would look the same as one homozygote and give 3 : 1. In codominance both alleles are expressed in the heterozygote."),
        PQ("Explain why more men than women are colour-blind.",
           "The allele is recessive and on the X chromosome. A man has one X, so a single copy of the allele makes him colour-blind. A woman has two X chromosomes and needs two copies, one from each parent, to be colour-blind. One copy only makes her a carrier. The recessive allele is rare, so the chance of having two copies is far smaller than the chance of having one."),
        SUM("Use one letter for each gene: capital for dominant, lower case for recessive. Set out each cross in order: parents, gametes, offspring, ratio.",
            "A test cross with a homozygous recessive shows whether an individual with dominant phenotype is homozygous or heterozygous.",
            "Codominant alleles are both expressed in the heterozygote (sickle cell haemoglobin, roan cattle). Heterozygote advantage maintains the sickle allele where malaria is common.",
            "Multiple alleles: ABO has I^A, I^B and i; any person has two. Blood groups can exclude but not prove fatherhood.",
            "X-linked recessive traits appear more often in males. A son's X comes from his mother; a father passes his X to all his daughters."),
    ],
))

# ------------------------------------------------------------------ 7. Dihybrid crosses
LESSONS.append(lesson(
    module=M_GEN,
    topic="Monohybrid and dihybrid crosses",
    title="Dihybrid crosses and independent assortment",
    slug="biu2-dihybrid-crosses",
    minutes=24,
    summary="Two genes on different chromosomes, the 9:3:3:1 and 1:1:1:1 ratios, how to find gametes and offspring quickly, and how to deduce parental genotypes from offspring ratios.",
    objectives=[
        "State Mendel's law of independent assortment and explain it with meiosis",
        "Work out gametes and offspring of a dihybrid cross, including the 9:3:3:1 ratio",
        "Use the multiplication rule to find the probability of a genotype or phenotype",
        "Deduce parental genotypes from offspring ratios such as 3:3:1:1",
    ],
    key_concepts=["Dihybrid cross", "Independent assortment", "9:3:3:1", "Test cross 1:1:1:1", "Multiplication rule"],
    blocks=[
        H("Introduction"),
        T("A maize breeder near Dschang wants plants that are both tall and resistant to a leaf disease. Height and resistance are controlled by two different genes. "
          "To plan crosses, the breeder must know how the two genes are passed on together. A **dihybrid cross** follows two genes at once."),
        H("Independent assortment"),
        D("**Law of independent assortment:** when gametes form, the alleles of one gene separate into the gametes independently of the alleles of another gene, provided the genes are on **different chromosomes** (or far apart on one chromosome).",
          title="Mendel's second law"),
        T("The reason is the behaviour of chromosomes in meiosis I. The two homologous pairs line up at the equator at random. "
          "The maternal chromosome of one pair may go to the same pole as the maternal or the paternal chromosome of the other pair. "
          "Each possible arrangement is equally likely."),
        H("The 9:3:3:1 ratio"),
        T("Mendel crossed pea plants with round yellow seeds (RRYY) and wrinkled green seeds (rryy). R is round (dominant) and Y is yellow (dominant). The F1 are all RrYy: round and yellow. "
          "Each F1 plant makes four types of gamete in equal numbers: RY, Ry, rY and ry. Crossing two F1 plants gives a 4 × 4 Punnett square of 16 boxes."),
        CODE("""            RY      Ry      rY      ry
    RY    RRYY    RRYy    RrYY    RrYy
    Ry    RRYy    RRyy    RrYy    Rryy
    rY    RrYY    RrYy    rrYY    rrYy
    ry    RrYy    Rryy    rrYy    rryy

Round yellow     9  (R- Y-)
Round green      3  (R- yy)
Wrinkled yellow  3  (rr Y-)
Wrinkled green   1  (rr yy)""", "text", title="RrYy x RrYy"),
        T("The ratio 9 : 3 : 3 : 1 is really two 3 : 1 ratios combined. Round to wrinkled is 3 : 1 and yellow to green is 3 : 1. "
          "(3 round + 1 wrinkled) × (3 yellow + 1 green) = 9 : 3 : 3 : 1. This is the **multiplication rule**: the probability of two independent events together is the product of their separate probabilities."),
        KEY("Finding the gametes", "A quick rule.", cards=[
            ["Each gamete", "Gets one allele of each gene. RrYy gives RY, Ry, rY, ry (2 × 2 = 4 types)."],
            ["Homozygous genes", "RRYy gives RY and Ry only (2 types). rryy gives only ry."],
            ["Number of types", "With n heterozygous genes on different chromosomes, 2 to the power n gamete types."],
        ]),
        H("The test cross for two genes"),
        T("A test cross of a double heterozygote RrYy with the double recessive rryy gives gametes RY, Ry, rY, ry from one parent and only ry from the other. "
          "The offspring are RrYy, Rryy, rrYy and rryy in the ratio **1 : 1 : 1 : 1**. This ratio shows that the two genes assort independently."),
        EX("Worked example 1: probability using the multiplication rule", intro="Two pea plants RrYy are crossed. Find the probability that an offspring is wrinkled and yellow (rr Y-).", steps=[
            S("Wrinkled", math=r"P(rr) = \frac{1}{4}"),
            S("Yellow (YY or Yy)", math=r"P(Y\text{-}) = \frac{3}{4}"),
            S("Multiply", math=r"\frac{1}{4} \times \frac{3}{4} = \frac{3}{16}"),
            S("Check with the Punnett square", text="Three of the 16 boxes are rrYY, rrYy, rrYy. Matches the 3 in the ratio 9 : 3 : 3 : 1."),
        ]),
        EX("Worked example 2: deducing a genotype", intro="A round yellow plant is crossed with a round green plant (RrYy x ? ). Of 160 offspring, about 60 are round yellow, 60 round green, 20 wrinkled yellow and 20 wrinkled green. Deduce the genotype of the green parent.", steps=[
            S("Round : wrinkled", text="(60 + 60) : (20 + 20) = 120 : 40 = 3 : 1. Both parents are Rr."),
            S("Yellow : green", text="(60 + 20) : (60 + 20) = 80 : 80 = 1 : 1. A 1 : 1 ratio comes from a heterozygote crossed with a recessive, so the green parent is yy."),
            S("Genotype of green parent", text="Round and green: **Rryy**."),
            S("Check", text="Rr × Rr gives 3 : 1. Yy × yy gives 1 : 1. Combined: (3 : 1) × (1 : 1) = 3 : 3 : 1 : 1, which matches 60 : 60 : 20 : 20."),
        ]),
        EX("Worked example 3: how many gamete types?", intro="How many different gametes can a plant of genotype AaBbCcDD form?", steps=[
            S("Heterozygous genes", text="Aa, Bb, Cc are heterozygous (3 genes). DD is homozygous and gives only D."),
            S("Count", math=r"2^3 = 8", text="The 8 types are ABCD, ABcD, AbCD, AbcD, aBCD, aBcD, abCD and abcD."),
        ]),
        TIP("When asked to 'explain' a result, link the ratio to meiosis: independent assortment of homologous pairs in meiosis I, followed by random fusion of gametes. A 9 : 3 : 3 : 1 ratio is the sign of two independent genes, each showing complete dominance."),
        MISTAKE("Putting both alleles of one gene in a gamete", "A gamete carries **one** allele of each gene. RrYy cannot form 'Rr' or 'Yy' gametes. It forms RY, Ry, rY and ry."),
        MISTAKE("Stating 9 : 3 : 3 : 1 for every dihybrid cross", "The ratio only applies when both parents are double heterozygotes, the genes are on different chromosomes and dominance is complete. If genes are linked, or there is epistasis, the ratios differ."),
        QUIZ("A plant of genotype AaBb is crossed with aabb. What is the expected ratio of phenotypes if the genes are on different chromosomes?",
             ["9 : 3 : 3 : 1", "1 : 1 : 1 : 1", "3 : 1", "1 : 1"], 1,
             "AaBb makes four gamete types in equal numbers; aabb makes only ab. So four offspring types, 1 : 1 : 1 : 1.",
             hint="How many gamete types does each parent make?",
             feedback=["That is the ratio when both parents are AaBb.", "", "3 : 1 would need a monohybrid cross of two heterozygotes.", "1 : 1 is a monohybrid test cross."]),
        QUIZ("Two plants RrYy are crossed. What is the probability of a round green offspring (R- yy)?",
             ["1/16", "3/16", "9/16", "3/4"], 1,
             "3/4 (round) × 1/4 (green) = 3/16.",
             hint="Multiply the probability of R- by the probability of yy.",
             feedback=["1/16 is wrinkled green.", "", "9/16 is round yellow.", "3/4 is the probability of round alone."]),
        PQ("Pea plants heterozygous for seed shape (R/r) and seed colour (Y/y) are crossed. Draw a Punnett square for the cross, and give the phenotype ratio of the offspring. Explain why the gametes are in equal numbers.",
           "Parents RrYy × RrYy. Gametes from each: RY, Ry, rY, ry. The Punnett square has 16 boxes (see the lesson). Offspring: 9 round yellow : 3 round green : 3 wrinkled yellow : 1 wrinkled green. The four gamete types are equal because the two pairs of homologous chromosomes line up at random in meiosis I, so each combination of alleles is equally likely."),
        PQ("In tomato plants, tall (T) is dominant to dwarf (t) and purple stem (P) is dominant to green stem (p). A tall purple plant crossed with a dwarf green plant gave 52 tall purple, 48 tall green, 50 dwarf purple, 51 dwarf green. Give the genotype of the tall purple parent and say what the ratio shows.",
           "The offspring ratio is about 1 : 1 : 1 : 1. A cross with the double recessive (ttpp) giving four equal classes shows that the tall purple parent is TtPp and that the two genes assort independently."),
        PQ("A plant AaBb is self-fertilised. What proportion of the offspring will be homozygous for both genes (AABB, AAbb, aaBB or aabb)?",
           "Each gene gives a homozygote (AA or aa) with probability 1/4 + 1/4 = 1/2, and the two genes are independent, so both together: 1/2 × 1/2 = 1/4. Check with the 16 boxes: AABB, AAbb, aaBB and aabb each occur once in 16, which is 4/16 = 1/4."),
        PQ("A cross between a plant AaBb and a plant Aabb gives offspring in the ratio 3 : 3 : 1 : 1. Explain how this arises.",
           "Aa × Aa gives 3 dominant : 1 recessive for A. Bb × bb gives 1 : 1 for B. The two sets of probabilities combine: (3 : 1) × (1 : 1) = 3 : 3 : 1 : 1 (A- B-, A- bb, aa B-, aa bb)."),
        SUM("Independent assortment: alleles of genes on different chromosomes separate independently in meiosis I.",
            "A double heterozygote makes four gamete types in equal numbers; two such parents give 9 : 3 : 3 : 1.",
            "A dihybrid test cross gives 1 : 1 : 1 : 1.",
            "The multiplication rule combines independent probabilities; separate ratios combine in the same way.",
            "Work out unknown genotypes by taking each gene separately and reading its own ratio (3 : 1 or 1 : 1)."),
    ],
))

# ------------------------------------------------------------------ 8. Linkage and crossing over
LESSONS.append(lesson(
    module=M_GEN,
    topic="Linkage and crossing over",
    title="Linkage, crossing over and chromosome mapping",
    slug="biu2-linkage-crossing-over-maps",
    minutes=26,
    summary="Why linked genes break the 9:3:3:1 rule, how crossing over produces recombinants, how to calculate the recombinant frequency and how to build a simple chromosome map.",
    objectives=[
        "Explain autosomal linkage and write linked genotypes with the correct symbols",
        "Describe how crossing over at a chiasma produces recombinant gametes",
        "Calculate the recombinant frequency (cross-over value) from test cross results",
        "Use recombinant frequencies to place genes in order on a chromosome map",
    ],
    key_concepts=["Linkage", "Chiasma", "Crossing over", "Parental and recombinant types", "Recombinant frequency", "Map unit", "Chromosome map"],
    blocks=[
        H("Introduction"),
        T("There are far more genes than chromosomes. A human has about 20 000 genes on 23 pairs of chromosomes, so each chromosome carries hundreds. "
          "Genes on the same chromosome cannot assort independently, because they travel together. "
          "In 2023 the Board's examiners noted that many candidates drew linked genes as if they were on separate chromosomes. This lesson shows the correct method."),
        D("**Linkage** is the inheritance together of genes on the same chromosome. A group of linked genes forms a **linkage group**. Their loci (positions) are on one chromosome and tend to be inherited together, unless crossing over separates them.", title="Definition: linkage"),
        H("Writing linked genotypes"),
        T("Show each chromosome as a line with the alleles on it. A double heterozygote AaBb with A and B on the same chromosome (and a and b on the other) is written **AB / ab**. "
          "This is called the **coupling** arrangement. If the dominant allele of one gene is on the same chromosome as the recessive of the other (Ab / aB), the arrangement is **repulsion**. "
          "Never write AaBb alone for a linked cross, because it does not show which alleles are on which chromosome."),
        H("Without crossing over"),
        T("If there were no crossing over, an AB / ab individual would make only two kinds of gamete, AB and ab. A test cross with ab / ab gives 1 : 1 only (AB / ab and ab / ab). "
          "This is **complete linkage**. In practice, the test cross usually gives all four kinds of offspring, but not in equal numbers."),
        H("Crossing over"),
        D("**Crossing over** is the exchange of segments between non-sister chromatids of homologous chromosomes at a **chiasma** during prophase I of meiosis. It produces new combinations of alleles on a chromatid.", title="Definition: crossing over"),
        IMG("al-biu2-linkage-crossover.svg", alt="A chiasma between homologous chromosomes carrying A and B (blue) and a and b (amber); four chromatids result: AB, Ab, aB and ab, with Ab and aB marked recombinant",
            caption="Figure 1. A crossover between the loci of A and B gives two recombinant and two parental chromatids."),
        T("Gametes that have the same combination as the parents' chromosomes (AB and ab) are **parental types**. Those with new combinations (Ab and aB) are **recombinants**. "
          "A crossover between the two genes in a cell gives two parental and two recombinant chromatids. "
          "The further apart two genes are, the more likely a chiasma forms between them. So the **recombinant frequency** is a measure of distance."),
        F(r"\text{Recombinant frequency} = \frac{\text{number of recombinant offspring}}{\text{total number of offspring}} \times 100\%", title="Recombinant frequency (cross-over value)"),
        T("One percent recombination is called one **map unit** (also one centimorgan). The recombinant frequency cannot exceed 50%, because even if genes are very far apart on a chromosome and always cross over, only half of the gametes are recombinant. A value near 50% looks the same as independent assortment. The Board uses the term cross-over value (COV) for the same quantity."),
        EX("Worked example 1: a test cross", intro="A heterozygous plant (AB / ab) was test-crossed with ab / ab. Offspring (invented teaching data): 440 AaBb, 440 aabb, 60 Aabb, 60 aaBb. Calculate the recombinant frequency and explain the results.", steps=[
            S("Parental types", text="AaBb and aabb were produced from the parental gametes AB and ab: 440 + 440 = 880."),
            S("Recombinant types", text="Aabb and aaBb came from recombinant gametes Ab and aB: 60 + 60 = 120."),
            S("Total", math=r"880 + 120 = 1000"),
            S("Recombinant frequency", math=r"\frac{120}{1000} \times 100\% = 12\%", text="The genes are 12 map units apart."),
            S("Explanation", text="The parental types are far more common than recombinants, and the numbers within each pair are equal. The genes are linked, and crossing over between them occurs in about 12% of gametes."),
        ]),
        EX("Worked example 2: is it linkage or independent assortment?", intro="Use the data above. If the genes assorted independently, 250 of each class would be expected. Test the difference with the chi-squared test (you will learn this fully in the next lessons).", steps=[
            S("Calculate", math=r"\chi^2 = \sum \frac{(O - E)^2}{E} = 2 \times \frac{(440-250)^2}{250} + 2 \times \frac{(60-250)^2}{250}"),
            S("Value", math=r"\chi^2 = 2(144.4) + 2(144.4) = 577.6"),
            S("Compare", text="With 3 degrees of freedom, the critical value at the 5% level is 7.82. Our value is far larger, so the difference from 1 : 1 : 1 : 1 is significant. The genes are linked."),
        ]),
        H("Chromosome maps"),
        T("Recombinant frequencies for pairs of genes can be used to place the genes on a map, in order and at relative distances. "
          "Suppose genes A, B and C are in one linkage group. The recombinant frequencies between the pairs are A to B 12%, B to C 8% and A to C 20%."),
        EX("Worked example 3: the order of three genes", intro="Use the recombinant frequencies A to B = 12%, B to C = 8% and A to C = 20% to find the order of the genes and draw the map.", steps=[
            S("Find the largest distance", text="A to C is the largest, 20%, so A and C are at the ends and B is in between."),
            S("Check", math=r"12 + 8 = 20", text="The two shorter distances add up to the longer one. This confirms B lies between A and C."),
            S("Map", text="A ---- 12 ---- B -- 8 -- C. The map is 20 units long. (Map distances over long stretches tend to be slightly underestimated because of double crossovers, so the sum of short distances can be a little greater than the long one.)"),
        ]),
        CODE("""A |------------| B |--------| C
       12 units       8 units
|----------------------------------|
              20 units (A to C)""", "text", title="Chromosome map of three genes"),
        T("The map shows **order** and **relative distance**, not exact physical distance. Maps were first made for the fruit fly (Drosophila) and for maize. "
          "Mapping is used to find the position of genes for diseases and to find marker genes close to a gene wanted by a breeder."),
        TIP("In a linkage question, check the offspring numbers. If there are two big equal classes and two small equal classes, the genes are linked. The big classes are the parental types; the small classes are the recombinants. The recombinant frequency is always less than 50%."),
        MISTAKE("Using the wrong total", "Recombinant frequency is recombinants divided by the **total** offspring, not by the number of parental types."),
        MISTAKE("Writing linked genes as separate pairs", "Write AB / ab, with a line for each chromosome, not AaBb. In a Paper 2 answer show the chromosomes, the chiasma and the four gamete types."),
        QUIZ("A test cross of AB / ab with ab / ab gave 45 AaBb, 45 aabb, 5 Aabb and 5 aaBb. What is the recombinant frequency?",
             ["5%", "10%", "50%", "90%"], 1,
             "Recombinants: 5 + 5 = 10 out of 100 = 10%.",
             hint="Recombinants are the two smaller classes.",
             feedback=["5 is the size of one recombinant class; add both.", "", "50% would mean independent assortment.", "90 is the number of parental types."]),
        QUIZ("Which observation suggests that two genes are NOT linked?",
             ["Two large equal classes and two small equal classes", "Four equal classes in a test cross", "Recombinant frequency of 12%", "Only two classes of offspring"], 1,
             "Four equal classes is the 1 : 1 : 1 : 1 ratio of independent assortment, with a recombinant frequency of 50%.",
             hint="Which result is the ratio for independent assortment?",
             feedback=["That pattern is typical of linkage with crossing over.", "", "12% is less than 50%, so linked.", "Only two classes means complete linkage."]),
        PQ("In maize, the gene for coloured seeds (C) is dominant to colourless (c) and the gene for full seeds (S) is dominant to shrunken (s). A plant CS / cs was test-crossed with cs / cs. The offspring were: 4032 coloured full, 149 coloured shrunken, 152 colourless full, 4035 colourless shrunken (these figures follow a classic maize experiment; check your textbook). Calculate the recombinant frequency and state the map distance.",
           "Parental types: 4032 + 4035 = 8067. Recombinants: 149 + 152 = 301. Total: 8368. Recombinant frequency = 301 / 8368 × 100% = 3.6%. The genes are about 3.6 map units apart, and linked."),
        PQ("Explain, with a labelled diagram, how crossing over produces recombinant gametes.",
           "Homologous chromosomes pair in prophase I of meiosis. A chiasma forms between a chromatid from each chromosome and the two non-sister chromatids break and rejoin, swapping segments. If the break is between the loci of two genes AB / ab, the chromatids become Ab and aB. After meiosis there are four haploid cells: two with the parental combinations AB and ab, and two with the recombinant combinations Ab and aB. (A diagram should show two chromosomes, the chiasma, the four chromatids and the four alleles.)"),
        PQ("The recombinant frequencies for genes P, Q and R are P to Q 6%, Q to R 14%, P to R 8%. Give the order of the genes on the chromosome.",
           "The largest distance is Q to R (14%), so Q and R are at the ends. P is between them: 6 + 8 = 14. Order: Q, P, R."),
        PQ("Give two reasons why the recombinant frequency for two linked genes cannot be more than 50%.",
           "A crossover at a chiasma involves only two of the four chromatids, so even if a chiasma forms between the genes in every cell, half of the gametes carry parental combinations. Also, when the genes are very far apart, two or more crossovers can cancel each other, so the observed recombinant frequency never goes above 50% and is indistinguishable from independent assortment."),
        SUM("Linked genes are on the same chromosome and are inherited together. Write them as AB / ab.",
            "Crossing over at a chiasma in prophase I swaps pieces between non-sister chromatids and makes recombinant gametes.",
            "Recombinant frequency (cross-over value) = recombinants / total × 100%. One percent is one map unit. It is never more than 50%.",
            "A test cross with linkage gives two large equal classes (parental) and two small equal classes (recombinant).",
            "Recombinant frequencies place genes in order on a chromosome map."),
    ],
))


# ------------------------------------------------------------------ 9. Epistasis
LESSONS.append(lesson(
    module=M_GEN,
    topic="Epistasis and the chi-squared test",
    title="Epistasis: when one gene masks another",
    slug="biu2-epistasis",
    minutes=24,
    summary="How genes in the same pathway interact, the modified dihybrid ratios 9:3:4, 12:3:1 and 9:7, and how to recognise epistasis in a question and work out genotypes.",
    objectives=[
        "Define epistasis and distinguish it from dominance",
        "Explain epistasis using a gene-enzyme-product pathway",
        "Predict offspring ratios for recessive epistasis, dominant epistasis and complementary genes",
        "Use a modified ratio to decide which type of gene interaction is present",
    ],
    key_concepts=["Epistasis", "Recessive epistasis (9:3:4)", "Dominant epistasis (12:3:1)", "Complementary genes (9:7)", "Gene pathway"],
    blocks=[
        H("Introduction"),
        T("Labrador dogs come in three coat colours: black, chocolate (brown) and yellow (golden). A breeder who crosses two black Labradors may be surprised by a yellow puppy. "
          "The yellow colour is not caused by a third allele of the colour gene. It comes from a second gene that acts on the first. This is **epistasis**."),
        D("**Epistasis** is the interaction between two genes at different loci in which the alleles of one gene (the epistatic gene) mask or modify the expression of the alleles of the other gene (the hypostatic gene).", title="Definition: epistasis"),
        T("Epistasis is not the same as dominance. **Dominance** is about two alleles of the **same** gene. **Epistasis** is about two **different** genes. "
          "Epistasis changes the 9 : 3 : 3 : 1 ratio of a dihybrid cross, because some of the phenotype classes become hidden or combined. "
          "The total is still 16 parts, which shows two genes are involved."),
        H("A pathway explains it"),
        T("Genes code for enzymes. Often several enzymes work in a chain, so one gene's product decides whether another enzyme has anything to work on. "
          "In Labradors, gene **E** controls whether pigment can be deposited in the hair at all. Gene **B** controls the colour of the pigment: B gives black and b gives brown."),
        CODE("""Gene E enzyme                Gene B enzyme
precursor ----------> brown pigment ----------> black pigment

E_ (EE or Ee): pigment is deposited in the hair
ee           : no pigment deposited -> yellow, whatever the B genes are
B_           : brown pigment converted to black
bb           : pigment stays brown""", "text", title="Pathway for Labrador coat colour"),
        H("Recessive epistasis: 9 : 3 : 4"),
        T("Cross two black dogs of genotype BbEe. The Punnett square is the same as for any dihybrid, but the phenotypes are combined differently."),
        CODE("""Genotype            Phenotype    Number (out of 16)
B_ E_  (9)          black        9
bb E_  (3)          brown        3
B_ ee  (3) and
bb ee  (1)          yellow       4

Ratio: 9 black : 3 brown : 4 yellow""", "text", title="BbEe x BbEe"),
        T("The ee genotype is **epistatic** to B because the dog is yellow whether it carries B or b. The effect of gene E hides the effect of gene B. Because ee is recessive, this is **recessive epistasis**."),
        T("A test cross of BbEe with bbee gives 1 black : 1 brown : 2 yellow. In 16 boxes you cannot see this, so use the gametes: BbEe gives BE, Be, bE, be; bbee gives be. Offspring: BbEe (black), Bbee (yellow), bbEe (brown), bbee (yellow). So 1 black : 1 brown : 2 yellow."),
        H("Other types of gene interaction"),
        KEY("Three modified ratios from AaBb x AaBb", "Learn the pattern in each case.", cards=[
            ["Recessive epistasis 9 : 3 : 4", "Homozygous recessive of one gene masks the other gene. Example: Labrador coat colour (ee gives yellow)."],
            ["Dominant epistasis 12 : 3 : 1", "A dominant allele of one gene masks the other gene. Example: fruit colour in summer squash, where the dominant W gives white fruit whatever the second gene is; yellow needs ww and a dominant allele of the second gene, green is ww and recessive."],
            ["Complementary genes 9 : 7", "A dominant allele of **both** genes is needed to make the product. Example: purple flower colour in sweet pea. Anything else is white."],
        ]),
        T("In every case the 16 boxes are the same. Only the grouping of phenotypes changes. A practical rule: if the F2 of a dihybrid cross gives a ratio that adds up to 16 but is not 9 : 3 : 3 : 1, look for epistasis."),
        EX("Worked example 1: the labrador cross", intro="Two black Labradors (BbEe) have 16 puppies. How many of each colour are expected?", steps=[
            S("Gametes", text="Each parent makes BE, Be, bE, be."),
            S("Offspring classes", text="9 B_E_ (black), 3 bbE_ (brown), 3 B_ee and 1 bbee (yellow)."),
            S("Expected numbers", text="9 black, 3 brown, 4 yellow. (Calculated by script from all 16 combinations.)"),
        ]),
        EX("Worked example 2: deducing the parents", intro="A yellow Labrador (homozygous eeBB) is crossed with a brown Labrador (homozygous bbEE). What are the colours of the F1, and of the F2 when two F1 are crossed?", steps=[
            S("Gametes", text="Yellow eeBB makes eB only. Brown bbEE makes bE only."),
            S("F1", text="All BbEe, which are black (the combination of B and E)."),
            S("F2", text="F1 × F1 is BbEe × BbEe, as in the table above: 9 black : 3 brown : 4 yellow."),
        ]),
        EX("Worked example 3: sweet pea", intro="Two white-flowered sweet pea plants, CCpp and ccPP, are crossed. All the F1 are purple. Explain this and predict the F2 ratio.", steps=[
            S("F1 genotype", text="CCpp makes Cp; ccPP makes cP. All F1 are CcPp."),
            S("Why purple", text="Purple pigment needs a dominant allele of both genes. Each parent lacks one, so both are white. The F1 has C and P, so it is purple. The two genes **complement** each other."),
            S("F2", text="CcPp × CcPp gives 9 C_P_ (purple) and 3 C_pp + 3 ccP_ + 1 ccpp = 7 (white). Ratio 9 purple : 7 white. (Calculated from all 16 combinations.)"),
        ]),
        TIP("Count the total first. If the numbers add to 16 and the ratio is 9 : 3 : 4, 12 : 3 : 1 or 9 : 7, it is epistasis. Then say which genotype is epistatic and **why** (use the pathway)."),
        MISTAKE("Calling epistasis dominance", "Dominance is between alleles of the same gene. Epistasis is between **different genes**. Do not write 'the allele e is dominant to B'."),
        MISTAKE("Thinking the ratio is no longer Mendelian", "The alleles still assort independently and the genotype classes are unchanged (9 : 3 : 3 : 1). Epistasis changes only how the **phenotypes** are grouped."),
        QUIZ("A cross between two plants AaBb gives offspring in the ratio 9 : 7. Which type of interaction is this?",
             ["Recessive epistasis", "Dominant epistasis", "Complementary genes", "Independent assortment without interaction"], 2,
             "A 9 : 7 ratio means a dominant allele of both genes is needed for the product; all other genotypes have the same phenotype.",
             hint="Which ratio has only two classes?",
             feedback=["Recessive epistasis gives 9 : 3 : 4.", "Dominant epistasis gives 12 : 3 : 1.", "", "Without interaction the ratio is 9 : 3 : 3 : 1."]),
        QUIZ("In Labradors, a black dog BbEe is test-crossed with a yellow dog bbee. What proportion of puppies are yellow?",
             ["1/4", "1/2", "3/4", "1/16"], 1,
             "Yellow puppies are Bbee and bbee: 1/4 + 1/4 = 1/2. (Black 1/4, brown 1/4.)",
             hint="List the four offspring genotypes and their colours.",
             feedback=["1/4 would be black or brown alone.", "", "3/4 would be non-yellow.", "1/16 is the fraction of ee bb in a dihybrid F2."]),
        PQ("Two black Labradors produce 3 black, 1 brown and 2 yellow puppies. Suggest their genotypes and explain how yellow puppies are possible.",
           "Each parent must be heterozygous for E (a yellow puppy is ee and each parent contributed an e) and for B (a brown puppy bb), so the parents are BbEe. Yellow puppies, ee, have no pigment deposited in the hair, so the colour gene B is hidden. This is recessive epistasis."),
        PQ("In summer squash, W (white) is dominant epistatic to the colour gene Y (yellow, dominant to green y). Two heterozygous plants WwYy are crossed. Give the phenotype ratio.",
           "W_ (any Y): 12 of 16 white. ww Y_: 3 of 16 yellow. ww yy: 1 of 16 green. The ratio is 12 white : 3 yellow : 1 green."),
        PQ("Explain, using the idea of enzymes, why a plant that lacks a dominant allele of either of two complementary genes has white flowers.",
           "Each gene codes for an enzyme in a pathway that makes the purple pigment. A dominant allele makes a working enzyme. If either gene is homozygous recessive that enzyme is missing, the pathway is blocked, and no pigment is made, so the flowers are white. Only plants with at least one dominant allele of both genes make working enzymes at both steps and are purple."),
        PQ("A breeder crosses a yellow Labrador with a chocolate (brown) Labrador, and all 8 puppies are black. Give the genotypes of the parents.",
           "Black puppies need a dominant allele of both genes (B_ E_). The yellow parent is ee, so it cannot supply E: the E comes from the brown parent, which is bb and therefore must carry E. The brown parent cannot supply B, so B comes from the yellow parent. Because all 8 puppies are alike, each parent is probably homozygous: yellow eeBB and brown bbEE. Every puppy is BbEe, which is black."),
        SUM("Epistasis is the masking of one gene's expression by another gene at a different locus; it is not dominance.",
            "Genes work in pathways; a block at one step hides the effect of genes later in the pathway.",
            "Dihybrid F2 ratios: 9 : 3 : 4 (recessive epistasis), 12 : 3 : 1 (dominant epistasis), 9 : 7 (complementary genes). Each totals 16.",
            "Genotype classes are the same as in a normal dihybrid; only the phenotype grouping differs."),
    ],
))

# ------------------------------------------------------------------ 10. Chi-squared
LESSONS.append(lesson(
    module=M_GEN,
    topic="Epistasis and the chi-squared test",
    title="The chi-squared test in genetics",
    slug="biu2-chi-squared-test",
    minutes=26,
    summary="How to test whether observed offspring numbers fit an expected ratio: the null hypothesis, calculating chi-squared, degrees of freedom, critical values and correct conclusions.",
    objectives=[
        "State a null hypothesis for a genetic cross and calculate expected numbers",
        "Calculate chi-squared and the degrees of freedom",
        "Compare the value with the critical value at the 5% level and draw a correct conclusion",
        "Explain the limits of the test",
    ],
    key_concepts=["Null hypothesis", "Observed and expected", "Chi-squared", "Degrees of freedom", "Critical value", "Significance level 5%"],
    blocks=[
        H("Introduction"),
        T("A cross should give a 3 : 1 ratio, but the real numbers are never exactly 3 : 1. If a farm gets 152 tall and 48 dwarf plants, is that close enough to 3 : 1? "
          "A few extra dwarf plants could be chance, because fertilisation is random. The **chi-squared test** helps us decide whether the difference is just chance, or too large to be chance."),
        H("The method"),
        KEY("Five steps", "Always follow them in this order.", cards=[
            ["1 Null hypothesis", "State what you expect. For example: there is no significant difference between the observed numbers and a 3 : 1 ratio."],
            ["2 Expected numbers", "Calculate the numbers you would expect from the ratio and the total."],
            ["3 Chi-squared", "Add up (O − E)² / E for every class."],
            ["4 Degrees of freedom", "Number of classes minus 1."],
            ["5 Compare and conclude", "Compare with the critical value at p = 0.05 in the table."],
        ]),
        F(r"\chi^2 = \sum \frac{(O - E)^2}{E}", title="Chi-squared"),
        T("O is the **observed** number in a class and E is the **expected** number. Use **actual numbers of offspring**, not percentages or ratios. The sum is over all classes."),
        CODE("""Degrees of    Critical value      Critical value
freedom       at p = 0.05 (5%)    at p = 0.01 (1%)
1             3.84                6.63
2             5.99                9.21
3             7.82                11.34
4             9.49                13.28
5             11.07               15.09""", "text", title="Critical values of chi-squared (standard table; use the table in your own exam paper)"),
        D("If the calculated value is **smaller than** the critical value at p = 0.05, the difference between observed and expected is **not significant**: it could be due to chance, and we do not reject the null hypothesis. "
          "If it is **equal to or larger than** the critical value, the difference is **significant** (the probability of getting it by chance is less than 5%), and we reject the null hypothesis.", title="The decision"),
        T("The 5% level means that if the null hypothesis is true, we would still wrongly reject it in about 1 test out of 20."),
        EX("Worked example 1: a monohybrid cross", intro="Two heterozygous tall plants are crossed. The offspring are 152 tall and 48 dwarf (invented data). Test the fit to 3 : 1.", steps=[
            S("Null hypothesis", text="There is no significant difference between the observed numbers and the expected 3 : 1 ratio."),
            S("Expected numbers", math=r"E_{tall} = \frac{3}{4} \times 200 = 150, \qquad E_{dwarf} = \frac{1}{4} \times 200 = 50"),
            S("Chi-squared", math=r"\chi^2 = \frac{(152-150)^2}{150} + \frac{(48-50)^2}{50} = 0.0267 + 0.08 = 0.107"),
            S("Degrees of freedom", math=r"2 - 1 = 1", text="Critical value at 5%: 3.84."),
            S("Conclusion", text="0.107 is much less than 3.84. The difference is not significant and could be due to chance. The data fit a 3 : 1 ratio."),
        ]),
        EX("Worked example 2: a dihybrid cross", intro="From a cross of two RrYy pea plants, the counts were 315 round yellow, 108 round green, 101 wrinkled yellow and 32 wrinkled green (total 556; these are Mendel's published counts). Test the fit to 9 : 3 : 3 : 1.", steps=[
            S("Expected", math=r"556 \times \frac{9}{16} = 312.75, \quad 556 \times \frac{3}{16} = 104.25, \quad 104.25, \quad 556 \times \frac{1}{16} = 34.75"),
            S("Chi-squared", math=r"\chi^2 = \frac{(315-312.75)^2}{312.75} + \frac{(108-104.25)^2}{104.25} + \frac{(101-104.25)^2}{104.25} + \frac{(32-34.75)^2}{34.75} = 0.47"),
            S("Degrees of freedom", math=r"4 - 1 = 3", text="Critical value at 5%: 7.82."),
            S("Conclusion", text="0.47 < 7.82. Not significant, so the results are consistent with a 9 : 3 : 3 : 1 ratio, and the two genes assort independently."),
        ]),
        EX("Worked example 3: a significant difference", intro="Of 100 offspring of a monohybrid test cross, 62 were male and 38 female. Test the fit to an expected 1 : 1 sex ratio.", steps=[
            S("Expected", text="50 and 50."),
            S("Chi-squared", math=r"\chi^2 = \frac{(62-50)^2}{50} + \frac{(38-50)^2}{50} = 2.88 + 2.88 = 5.76"),
            S("Degrees of freedom and critical value", text="1 degree of freedom: 3.84."),
            S("Conclusion", text="5.76 is larger than 3.84. The difference is significant at the 5% level. Chance alone is unlikely to explain it (the probability is less than 5%), so reject the null hypothesis. It is still not proof of a particular cause: something may bias the sex ratio, or the 5% risk of a false alarm may have occurred."),
        ]),
        H("Limits and good practice"),
        T("Use the test on **counts**, not on percentages. Use large samples; an expected number below about 5 in any class makes the test unreliable. "
          "The test does not show that the null hypothesis is true. It only shows that the data **do not contradict** it. "
          "The test cannot say why a result is significant: linkage, epistasis, lethal alleles or poor sampling could all cause a difference. "
          "A value of chi-squared that is very small (data too good to be true) can also be worth questioning."),
        TIP("When writing the conclusion, state three things: the calculated value, the critical value with the degrees of freedom, and the decision in words (for example, 'not significant, so the difference is due to chance and the results fit 3 : 1')."),
        MISTAKE("Using percentages instead of numbers", "Chi-squared depends on the total sample size. Use the real numbers of offspring. 15.2 tall out of 20 percent gives nonsense."),
        MISTAKE("Wrong degrees of freedom", "It is the number of classes minus 1, **not** the sample size minus 1. For 4 classes, the value is 3."),
        MISTAKE("Saying the hypothesis is proved", "If chi-squared is less than the critical value, say the null hypothesis is **not rejected**. Do not say it is proved."),
        QUIZ("A dihybrid cross gives 4 classes in a 9 : 3 : 3 : 1 test. A student calculates chi-squared = 6.1. What is the correct conclusion at the 5% level?",
             ["Significant, since 6.1 is more than 3.84", "Not significant, since 6.1 is less than 7.82", "Significant, since 6.1 is more than 5.99", "Cannot be decided without knowing the sample size"], 1,
             "Four classes give 3 degrees of freedom, with critical value 7.82. 6.1 is below it, so the difference is not significant.",
             hint="First find the degrees of freedom. How many classes are there?",
             feedback=["3.84 is for 1 degree of freedom.", "", "5.99 is the value for 2 degrees of freedom.", "Sample size is already built into the calculation of chi-squared. The degrees of freedom depend on the number of classes."]),
        QUIZ("What does a significant value of chi-squared tell you?",
             ["The null hypothesis is certainly false.", "The null hypothesis is probably not correct, because there is less than a 5% probability of the difference being due to chance.", "The sample is too small.", "The ratio expected is correct."], 1,
             "Significant means less than a 5% probability of getting such a difference by chance if the null hypothesis were true.",
             hint="Think about probability, not certainty.",
             feedback=["The test gives a probability, not a certainty.", "", "Sample size is a separate issue.", "A significant value means the expected ratio does not fit."]),
        PQ("In a cross of two heterozygous pea plants, the offspring were 290 tall and 110 dwarf. Test whether these results fit 3 : 1.",
           "Expected: 300 tall and 100 dwarf. Chi-squared = (290 − 300)²/300 + (110 − 100)²/100 = 0.333 + 1.0 = 1.33. Degrees of freedom = 1; the critical value is 3.84. 1.33 < 3.84, so the difference is not significant and the data fit a 3 : 1 ratio."),
        PQ("A cross of two black Labradors gave 90 black, 25 brown and 45 yellow puppies, which was compared with the expected 9 : 3 : 4 ratio. Calculate chi-squared and state the conclusion.",
           "Total 160. Expected: 90 black, 30 brown, 40 yellow. Chi-squared = (90 − 90)²/90 + (25 − 30)²/30 + (45 − 40)²/40 = 0 + 0.833 + 0.625 = 1.46. Degrees of freedom = 3 − 1 = 2; critical value 5.99. 1.46 < 5.99: not significant; the results fit 9 : 3 : 4, consistent with recessive epistasis."),
        PQ("A test cross is expected to give 1 : 1 : 1 : 1. The observed numbers were 61 : 59 : 20 : 20 (total 160, invented). Show that the difference is significant and suggest an explanation.",
           "Expected 40 each. Chi-squared = (61−40)²/40 + (59−40)²/40 + (20−40)²/40 + (20−40)²/40 = 11.03 + 9.03 + 10 + 10 = 40.05. Degrees of freedom = 3; critical value 7.82. 40.05 > 7.82: significant, so reject the null hypothesis. The two large classes and two small classes suggest the genes are linked, with a recombinant frequency of 40/160 = 25%."),
        PQ("Give two reasons why a significant chi-squared value does not prove that a particular genetic explanation is correct.",
           "The test only shows that observed numbers differ from expected by more than chance would normally cause; it does not identify the cause. A significant result could be caused by linkage, epistasis, a lethal genotype, a biased sample or poor classification of phenotypes. There is also a 5% chance of a significant result occurring by chance even if the hypothesis is correct."),
        SUM("State a null hypothesis, calculate expected numbers from the ratio and the total, then calculate chi-squared = sum of (O − E)² / E.",
            "Degrees of freedom = number of classes − 1. Compare with the critical value at p = 0.05: 3.84 (1), 5.99 (2), 7.82 (3).",
            "Calculated value below the critical value: not significant, the difference could be chance. At or above: significant, reject the null hypothesis.",
            "Use numbers, not percentages. The test does not prove a hypothesis or give the cause of a difference."),
    ],
))

# ------------------------------------------------------------------ 11. Mutations
LESSONS.append(lesson(
    module=M_GEN,
    topic="Mutations",
    title="Gene and chromosome mutations",
    slug="biu2-gene-chromosomal-mutations",
    minutes=25,
    summary="Substitution, insertion and deletion mutations and their effects on the protein, chromosome structure changes, non-disjunction and polyploidy, and what causes mutations.",
    objectives=[
        "Define mutation and name the types of gene mutation",
        "Work out the effect of a substitution, insertion or deletion on a protein using the genetic code",
        "Describe chromosome mutations and non-disjunction, with the chromosome numbers in Down syndrome",
        "Explain causes of mutation and why mutations may be harmful, neutral or beneficial",
    ],
    key_concepts=["Mutation", "Point mutation", "Frameshift", "Silent, missense, nonsense", "Non-disjunction", "Polyploidy", "Mutagen"],
    blocks=[
        H("Introduction"),
        T("In one letter of the DNA code in a gene for haemoglobin, a single base is changed. A child who inherits two copies of this change has sickle cell disease. "
          "A different change, in a different place, can be harmless, and another can even help. "
          "Mutations are the source of all new alleles. Without them there would be no variation for natural selection to act on."),
        D("A **mutation** is a random, unpredictable change in the amount, arrangement or base sequence of the genetic material of a cell.", title="Definition: mutation"),
        T("A mutation that happens in a **body cell** (somatic mutation) cannot be passed to children, though it may cause cancer. A mutation in a **gamete or its precursor** (germ-line mutation) can be inherited."),
        H("Gene (point) mutations"),
        T("A gene mutation is a change in the sequence of bases in a gene. There are three kinds."),
        KEY("Types of gene mutation", "Study the effects.", cards=[
            ["Substitution", "One base is replaced by another. Only one codon changes. The result may be silent, missense or nonsense."],
            ["Insertion", "One or more extra bases are added. If the number is not a multiple of 3 it causes a frameshift."],
            ["Deletion", "One or more bases are lost. If the number is not a multiple of 3 it causes a frameshift."],
        ]),
        KEY("Effects of a substitution", "Because the genetic code is degenerate (more than one codon can code for the same amino acid), the effect depends on the change.", cards=[
            ["Silent", "The new codon codes for the same amino acid. No effect on the protein. Example: GAA to GAG, both code for glutamic acid (Glu)."],
            ["Missense", "The new codon codes for a different amino acid. The protein may change. Example: GAG to GUG (Glu to Val), as in sickle cell haemoglobin."],
            ["Nonsense", "The new codon is a stop codon. The protein is cut short. Example: GAG to UAG."],
        ]),
        T("In sickle cell disease the DNA triplet that codes for the sixth amino acid in the beta chain of haemoglobin is changed from CTC to CAC on the template strand. The mRNA codon changes from GAG (glutamic acid) to GUG (valine). "
          "Valine is non-polar and glutamic acid is charged. The haemoglobin molecules stick together when oxygen is low, and the red cells take a sickle shape."),
        T("**Frameshift.** The ribosome reads mRNA in triplets. If one base is inserted or deleted, every codon after the change is read in a different frame. "
          "Almost every amino acid after it changes, and often a stop codon appears early. This usually has a more severe effect than a substitution. "
          "Insertion or deletion of exactly three bases (or a multiple of three) removes or adds amino acids but does not shift the frame."),
        CODE("""mRNA                AUG GAA CCU UUG AAC CUU UGA
Protein             Met-Glu-Pro-Leu-Asn-Leu-stop

Substitution GAA->GAG    AUG GAG CCU UUG AAC CUU UGA
                         Met-Glu-Pro-Leu-Asn-Leu-stop      (silent)
Substitution GAA->GUA    AUG GUA CCU UUG AAC CUU UGA
                         Met-Val-Pro-Leu-Asn-Leu-stop      (missense)
Substitution GAA->UAA    AUG UAA ...
                         Met-stop                          (nonsense)
Deletion of first G      AUG AAC CUU UGA
 of GAA                  Met-Asn-Leu-stop                  (frameshift)
Deletion of GAA          AUG CCU UUG AAC CUU UGA
 (3 bases)               Met-Pro-Leu-Asn-Leu-stop          (one amino acid lost)""", "text", title="Effects of mutations on one short invented mRNA"),
        H("Chromosome mutations"),
        T("**Changes in structure** involve whole sections of a chromosome. A **deletion** removes a segment. A **duplication** repeats a segment. An **inversion** turns a segment round by 180 degrees. "
          "A **translocation** moves a segment to a non-homologous chromosome. These can break up genes or change their number."),
        T("**Changes in number.** Sometimes homologous chromosomes or chromatids fail to separate in meiosis. This is **non-disjunction**. One gamete receives both chromosomes of a pair (n + 1 = 24 in humans) and another receives none (n − 1 = 22). "
          "When a gamete with 24 is fertilised by a normal gamete (23) the zygote has 47 chromosomes. If the extra chromosome is number 21, the child has **Down syndrome** (trisomy 21). "
          "A zygote with 22 + 23 = 45 chromosomes has a missing chromosome; in humans, one X chromosome only (45, X) gives Turner syndrome. The risk of non-disjunction rises with the age of the mother."),
        T("**Polyploidy** is the presence of more than two sets of chromosomes (3n, 4n, 6n). It is common in plants and rare in animals. Bread wheat is hexaploid (6n = 42). "
          "Seedless bananas are triploid (3n), so they cannot make normal gametes and do not form seeds, but are propagated by suckers. Polyploid crops are often bigger and give bigger yields."),
        H("Causes and effects"),
        T("Mutations occur spontaneously, for example from errors in DNA replication, at a low and constant rate. The rate is raised by **mutagens**: ionising radiation (X-rays, gamma rays), ultraviolet light, and chemicals (for example some components of tobacco smoke and some food moulds). "
          "Mutations are random: they are not caused by need, and they are not predictable."),
        T("Most mutations are harmful or neutral. A few are beneficial. A mutation that is harmful in one environment may be useful in another. "
          "The sickle cell allele is harmful in homozygotes, but in people who have one copy it protects against severe malaria, and so the allele stays common in malaria regions. "
          "Mutations in genes that control cell division (such as tumour suppressor genes) can lead to cancer."),
        EX("Worked example 1: effects of base changes", intro="The example mRNA is AUG GAA CCU UUG AAC CUU UGA (Met-Glu-Pro-Leu-Asn-Leu-stop). Say what happens to the protein if (a) the first G of GAA is deleted, (b) an A is inserted after AUG.", steps=[
            S("(a) Deletion of one base", text="AUG AAC CUU UGA: Met-Asn-Leu-stop. The frame has moved, three amino acids changed, and a stop codon appears early. The protein is much shorter."),
            S("(b) Insertion of one base", text="AUG AGA ACC UUU GAA CCU UUG A: Met-Arg-Thr-Phe-Glu-Pro-Leu, then an incomplete codon. Every amino acid after the first has changed, so this is a frameshift."),
            S("Compare", text="A single-base insertion or deletion shifts the reading frame. Many amino acids change. This is why frameshifts are usually more serious than substitutions."),
        ]),
        EX("Worked example 2: counting chromosomes after non-disjunction", intro="Non-disjunction of chromosome 21 occurs in meiosis I in a woman. (a) How many chromosomes can the egg cells have? (b) If an abnormal egg is fertilised by a normal sperm, how many chromosomes has the zygote?", steps=[
            S("(a) Eggs", text="One egg gets both chromosomes 21: 22 + 2 = 24. Another gets none: 22. (Normal is 23.)"),
            S("(b) Zygote", text="24 + 23 = 47 (three copies of chromosome 21: Down syndrome). The 22-chromosome egg gives 22 + 23 = 45, which is usually lethal for chromosome 21."),
        ]),
        TIP("When asked about the effect of a mutation on the protein, write the old and new codon and amino acid, then say if the change is silent, missense, nonsense or frameshift. Then link to the **function**."),
        MISTAKE("Saying mutations are caused by the need of the organism", "Mutations are random. The environment may select for a mutation that already exists, but it does not cause the useful one to appear."),
        MISTAKE("Calling every deletion a frameshift", "A deletion of **three** bases (or a multiple of 3) removes whole amino acids and the frame is kept. Only deletions or insertions that are **not** a multiple of 3 cause a frameshift."),
        QUIZ("A single base is deleted near the start of a gene. Which statement is most likely?",
             ["The protein has one amino acid changed.", "All amino acids after the deletion are likely to be changed.", "There is no effect because the code is degenerate.", "The protein is unchanged but the mRNA is longer."], 1,
             "A one-base deletion shifts the reading frame for the rest of the gene.",
             hint="What happens to the triplets after the deletion?",
             feedback=["That describes a missense substitution.", "", "Degeneracy helps with substitutions, not frameshifts.", "The mRNA would be shorter, not longer."]),
        QUIZ("The mRNA codon GAG is changed to GAA. This is an example of",
             ["a nonsense mutation", "a missense mutation", "a silent mutation", "a frameshift mutation"], 2,
             "Both GAG and GAA code for glutamic acid, so the protein is unchanged.",
             hint="Look up the amino acid for both codons.",
             feedback=["Nonsense creates a stop codon.", "Missense changes the amino acid; here it does not.", "", "Only one base is replaced; the frame is unchanged."]),
        PQ("Explain how a single base substitution can lead to sickle cell disease.",
           "A base in the DNA triplet for the sixth amino acid of the beta chain changes (CTC to CAC), so the mRNA codon changes from GAG to GUG. The amino acid glutamic acid is replaced by valine. This alters the shape of the haemoglobin, especially at low oxygen, and the molecules form long fibres that distort the red blood cell into a sickle shape, which blocks capillaries and carries less oxygen."),
        PQ("Distinguish between a gene mutation and a chromosome mutation and give an example of each.",
           "A gene mutation is a change in the base sequence of a gene, for example a substitution that causes sickle cell disease. A chromosome mutation is a change in the structure or the number of chromosomes, for example trisomy 21 (Down syndrome), caused by non-disjunction, or a translocation."),
        PQ("A woman's egg has 24 chromosomes because of non-disjunction. State how it arises and the number of chromosomes in the zygote if it is fertilised by a normal sperm.",
           "In meiosis I, a pair of homologous chromosomes fails to separate (or in meiosis II, sister chromatids fail to separate), so both go to one cell. That egg has 23 + 1 = 24 chromosomes. A normal sperm has 23, so the zygote has 47."),
        PQ("Suggest why polyploid plants are used in agriculture, and why a triploid banana is seedless.",
           "Polyploid plants often have bigger cells and organs and may give higher yields or bigger fruits. A triploid has three sets of chromosomes; in meiosis they cannot pair into twos, so they are shared unevenly and viable gametes are not formed. No fertilisation occurs, so no seeds form, and the plant is propagated vegetatively."),
        SUM("A mutation is a random change in the genetic material. Somatic mutations are not inherited; germ-line mutations are.",
            "Gene mutations: substitution (silent, missense or nonsense), insertion and deletion (frameshift unless a multiple of 3).",
            "Chromosome mutations: deletion, duplication, inversion, translocation; non-disjunction (Down syndrome 47) and polyploidy.",
            "Mutagens such as radiation and some chemicals increase mutation rates. Most mutations are harmful or neutral; some are beneficial, as with the sickle allele where malaria occurs."),
    ],
))

# ------------------------------------------------------------------ 12. Gene regulation
LESSONS.append(lesson(
    module=M_GEN,
    topic="Gene regulation",
    title="Gene regulation: the lac operon",
    slug="biu2-lac-operon-gene-regulation",
    minutes=25,
    summary="How bacteria switch genes on and off with the lac operon (induction) and the trp operon (repression), the parts of an operon, and how to predict the effect of mutations.",
    objectives=[
        "Explain why not all genes are expressed all the time",
        "Name the parts of the lac operon and describe how it is switched on and off",
        "Explain enzyme induction and enzyme repression in the Jacob-Monod model",
        "Predict enzyme production in mutants of the lac operon",
    ],
    key_concepts=["Operon", "Regulator gene", "Promoter and operator", "Repressor", "Induction", "Repression", "Structural genes"],
    blocks=[
        H("Introduction"),
        T("A bacterium such as *E. coli* in the gut of a baby faces a changing diet. When the baby drinks milk, the bacterium finds lactose. "
          "It needs enzymes to break lactose down. It would be wasteful to make these enzymes all the time, when there is no lactose. "
          "In 1961 François Jacob and Jacques Monod proposed how bacteria avoid this waste. The Board's 2023 report states that candidates found this topic hard. This lesson sets it out step by step."),
        D("An **operon** is a group of genes on a bacterial chromosome, next to each other, that are controlled together and transcribed as one mRNA. It consists of a **promoter**, an **operator** and the **structural genes**.", title="Definition: operon"),
        H("Parts of the lac operon"),
        KEY("The lac operon", "Six parts to learn.", cards=[
            ["Regulator gene (lacI)", "Lies some distance away, with its own promoter. Always makes the **repressor protein**."],
            ["Promoter (P)", "The site where RNA polymerase attaches to begin transcription."],
            ["Operator (O)", "A short DNA sequence next to the structural genes. The repressor can bind to it."],
            ["Structural genes", "lacZ codes for beta-galactosidase (breaks lactose into glucose and galactose). lacY codes for permease (lets lactose into the cell). lacA codes for transacetylase (its role is less clear)."],
        ]),
        IMG("al-biu2-lac-operon.svg", alt="Top: operon with a repressor sitting on the operator and RNA polymerase blocked at the promoter. Bottom: lactose bound to the repressor, which leaves the operator, and RNA polymerase moving along the structural genes making mRNA",
            caption="Figure 1. The lac operon when lactose is absent (top) and present (bottom)."),
        H("No lactose: switched off"),
        T("The repressor protein has a shape that fits the operator. It binds to the operator and covers part of the promoter, so RNA polymerase cannot move along the structural genes. "
          "No mRNA is made and no enzymes are produced. (A very small amount of leakage occurs, enough for the first lactose to enter.)"),
        H("Lactose present: switched on (induction)"),
        T("Lactose (or its isomer allolactose) enters the cell and binds to the repressor at a second binding site. This changes the shape of the repressor, so it can no longer bind to the operator. "
          "RNA polymerase moves along the structural genes and makes mRNA. Ribosomes translate it, and beta-galactosidase and permease are made. "
          "When the lactose has been used up, the repressor returns to the operator and the operon is switched off."),
        D("**Induction** is the switching on of genes by a substance (the inducer, here lactose) that binds to the repressor and stops it binding to the operator. An **inducible** enzyme is made only when its substrate is present.", title="Definition: enzyme induction"),
        H("Enzyme repression: the trp operon"),
        T("Some operons work in the opposite way. The trp operon codes for enzymes that make the amino acid tryptophan. When tryptophan is scarce the operon is on. "
          "When tryptophan is plentiful, it binds to the repressor (here it is called a **corepressor**). The repressor then changes shape so that it **can** bind to the operator and switch the operon off. "
          "The cell stops making an amino acid that it does not need. This is **enzyme repression**."),
        CODE("""                      lac operon (induction)       trp operon (repression)
Normal state          OFF (repressor on operator)  ON (repressor inactive)
Signal molecule       lactose                      tryptophan
Effect on repressor   made INACTIVE (cannot bind)  made ACTIVE (can bind)
Result of signal      operon switched ON           operon switched OFF
Function              breaks down a nutrient       makes an amino acid""", "text", title="Induction and repression compared"),
        T("In eukaryotes the regulation is more complex: transcription factors bind to promoters and enhancers, and hormones such as oestrogen or gibberellin can act by affecting transcription factors. The ideas of switching on and off are the same. "
          "(Some textbooks also describe the effect of glucose through a molecule called cAMP; the lac operon is on at its highest only when lactose is present and glucose is low. Check your textbook for how far to go.)"),
        EX("Worked example 1: predicting enzyme production in mutants", intro="State whether beta-galactosidase is made in each strain, with and without lactose. (a) Normal. (b) A mutant with a faulty repressor that cannot bind to the operator. (c) A mutant with a faulty lacZ gene. (d) A mutant with an operator that the repressor cannot recognise.", steps=[
            S("(a) Normal", text="Without lactose: not made. With lactose: made."),
            S("(b) Faulty repressor", text="Nothing blocks the operator, so the enzyme is made all the time, with or without lactose (constitutive)."),
            S("(c) Faulty lacZ", text="The structural gene for the enzyme is faulty. Active enzyme is never made, whatever the lactose level."),
            S("(d) Operator mutation", text="The repressor cannot bind, so the operon is always on. The enzyme is made all the time."),
        ]),
        EX("Worked example 2: explaining induction in sentences", intro="Explain how the presence of lactose leads to production of beta-galactosidase. Give the answer as a sequence.", steps=[
            S("1", text="Lactose enters the cell (small amounts, through permease already present) and binds to the repressor."),
            S("2", text="The repressor changes shape and cannot bind to the operator."),
            S("3", text="RNA polymerase can bind to the promoter and move along the structural genes."),
            S("4", text="mRNA for lacZ, lacY and lacA is transcribed."),
            S("5", text="Translation at ribosomes makes beta-galactosidase, permease and transacetylase."),
        ]),
        TIP("In exam answers on the operon, always name the **repressor**, the **operator** and **RNA polymerase** and say where each is. The mark is usually for the action: lactose binds repressor, the repressor cannot bind the operator, RNA polymerase can transcribe."),
        MISTAKE("Saying lactose binds to the operator", "Lactose binds to the **repressor**, not to the DNA. The repressor is what binds the operator."),
        MISTAKE("Thinking the repressor is made only when there is no lactose", "The regulator gene is expressed all the time at a low rate. The repressor is always present. Lactose changes whether it can bind."),
        QUIZ("In the lac operon, what happens when lactose is present?",
             ["Lactose binds to the operator so RNA polymerase can attach.", "Lactose binds to the repressor, which no longer binds to the operator.", "Lactose binds to RNA polymerase and activates it.", "Lactose destroys the repressor."], 1,
             "Lactose changes the shape of the repressor so it cannot bind to the operator. RNA polymerase can then transcribe.",
             hint="What does the inducer attach to?",
             feedback=["The operator is a DNA sequence; lactose does not bind it.", "", "RNA polymerase is not the target.", "The repressor is not destroyed; it is changed."]),
        QUIZ("A bacterium has a mutation in the lacI gene so that no repressor is made. What is the effect?",
             ["The enzymes are never made.", "The enzymes are made only when lactose is present.", "The enzymes are made all the time.", "The enzymes are made only when glucose is present."], 2,
             "With no repressor, nothing blocks the operator, so the structural genes are always transcribed.",
             hint="Which part stops transcription in the absence of lactose?",
             feedback=["That would happen if the repressor never released the operator.", "That is the normal pattern.", "", "Glucose is not part of this question."]),
        PQ("Describe the roles of the regulator gene, the operator and the structural genes in the lac operon.",
           "The regulator gene codes for the repressor protein. The operator is the DNA sequence that the repressor binds to; when bound it blocks RNA polymerase. The structural genes (lacZ, lacY, lacA) code for the enzymes and proteins needed to take up and break down lactose, and are transcribed together as one mRNA when the repressor is not on the operator."),
        PQ("Explain how the lac operon is switched off again when all the lactose has been used.",
           "As lactose is broken down, the concentration of lactose in the cell falls. Lactose molecules leave the repressor, so the repressor returns to its original shape and binds to the operator again. RNA polymerase is blocked, no more mRNA is made, and the enzymes are not made. The enzymes already made are gradually degraded."),
        PQ("Compare the control of the lac operon and the trp operon.",
           "In the lac operon the repressor is active on its own and is made inactive by lactose, so the operon is switched on by lactose (induction). In the trp operon the repressor is inactive alone; tryptophan binds and activates it, so the operon is switched off when tryptophan is plentiful (repression). Lac controls enzymes for breaking down a nutrient; trp controls enzymes for making an amino acid."),
        PQ("Why is it an advantage to a bacterium to control the lac operon like this?",
           "It saves energy and amino acids, because the enzymes are not made unless lactose is present to be broken down. When lactose is present the cell quickly makes the enzymes it needs, so it can use the new source of food."),
        SUM("An operon is a group of structural genes under one promoter and operator. A regulator gene makes the repressor.",
            "Lac operon: the repressor binds the operator, blocking transcription. Lactose binds the repressor, which leaves the operator, and RNA polymerase transcribes the structural genes (induction).",
            "Trp operon: tryptophan activates the repressor, which switches the operon off (repression).",
            "A faulty repressor or operator makes the enzymes constitutive; a faulty structural gene makes no enzyme."),
    ],
))

# ------------------------------------------------------------------ 13. Hardy-Weinberg
LESSONS.append(lesson(
    module=M_GEN,
    topic="Hardy-Weinberg equilibrium",
    title="The Hardy-Weinberg principle, allele frequencies and speciation",
    slug="biu2-hardy-weinberg-speciation",
    minutes=26,
    summary="Using p + q = 1 and p squared + 2pq + q squared = 1 to find allele and genotype frequencies, the conditions of the equilibrium, what changes allele frequencies, and how new species arise.",
    objectives=[
        "Define allele frequency and gene pool and state the Hardy-Weinberg equations",
        "Calculate allele and genotype frequencies, including carrier frequency from disease frequency",
        "State the conditions needed for equilibrium and name the factors that change allele frequencies",
        "Describe allopatric and sympatric speciation and reproductive isolation",
    ],
    key_concepts=["Gene pool", "Allele frequency", "p and q", "Hardy-Weinberg equilibrium", "Natural selection", "Genetic drift", "Speciation"],
    blocks=[
        H("Introduction"),
        T("In many parts of Cameroon about one in a few hundred children is born with sickle cell disease, while many more people carry the allele without being ill. "
          "A health planner who wants to know how many carriers live in a district cannot test everyone. "
          "A simple mathematical model, the Hardy-Weinberg principle, lets us estimate the frequency of carriers from the frequency of the disease."),
        D("The **gene pool** is all the alleles of all the genes in a breeding population. The **allele frequency** is the proportion of all the copies of a gene that are a particular allele. The **genotype frequency** is the proportion of individuals with a particular genotype.", title="Key terms"),
        H("The equations"),
        T("Take a gene with two alleles. Let the frequency of the dominant allele A be **p** and the frequency of the recessive allele a be **q**. Together they make up all the alleles, so"),
        F(r"p + q = 1"),
        T("When gametes combine at random, the genotype frequencies are given by (p + q)², that is"),
        F(r"p^2 + 2pq + q^2 = 1"),
        T("**p²** is the frequency of AA, **2pq** is the frequency of Aa (carriers) and **q²** is the frequency of aa. Frequencies are proportions between 0 and 1, so 0.25 is 25%."),
        D("The **Hardy-Weinberg principle** states that in a large, randomly mating population with no migration, no mutation and no selection, allele frequencies and genotype frequencies stay constant from generation to generation. "
          "After one generation of random mating the genotype frequencies are p², 2pq and q².", title="Hardy-Weinberg principle"),
        KEY("Conditions for equilibrium", "All must hold. They never do perfectly, so the principle is a model for comparison.", cards=[
            ["Population", "Very large (so chance has no effect), mating at random."],
            ["No change in alleles", "No mutation and no migration (no gene flow)."],
            ["No selection", "All genotypes survive and reproduce equally well."],
        ]),
        EX("Worked example 1: from the frequency of the disease to carriers", intro="In a town, 1 child in 400 is born with a recessive condition (aa). (This is a teaching figure, not a real survey.) Calculate the frequency of the allele a, of A, and the percentage of carriers.", steps=[
            S("q squared", math=r"q^2 = \frac{1}{400} = 0.0025"),
            S("q", math=r"q = \sqrt{0.0025} = 0.05"),
            S("p", math=r"p = 1 - q = 0.95"),
            S("Carriers", math=r"2pq = 2 \times 0.95 \times 0.05 = 0.095", text="About 9.5% of the population, or about 1 person in 10.5, are carriers."),
            S("Check", math=r"p^2 + 2pq + q^2 = 0.9025 + 0.095 + 0.0025 = 1"),
        ]),
        EX("Worked example 2: from genotype counts to allele frequencies", intro="In a sample of 500 people, 320 are AA, 160 are Aa and 20 are aa (invented). (a) Find p and q. (b) Is the sample in Hardy-Weinberg equilibrium?", steps=[
            S("Count the alleles", text="500 people have 1000 alleles. A alleles: 2 × 320 + 160 = 800. a alleles: 2 × 20 + 160 = 200."),
            S("Frequencies", math=r"p = \frac{800}{1000} = 0.8, \qquad q = \frac{200}{1000} = 0.2"),
            S("Expected genotypes", math=r"p^2 \times 500 = 0.64 \times 500 = 320, \quad 2pq \times 500 = 0.32 \times 500 = 160, \quad q^2 \times 500 = 0.04 \times 500 = 20"),
            S("Compare", text="The expected numbers equal the observed ones, so the sample is in Hardy-Weinberg equilibrium."),
        ]),
        EX("Worked example 3: a population that is not in equilibrium", intro="A sample of 500 has 200 AA, 200 Aa and 100 aa (invented). Find the allele frequencies and test with chi-squared whether the genotypes fit Hardy-Weinberg.", steps=[
            S("Allele frequencies", math=r"p = \frac{2 \times 200 + 200}{1000} = 0.6, \qquad q = 0.4"),
            S("Expected", math=r"p^2 N = 180, \quad 2pq N = 240, \quad q^2 N = 80"),
            S("Chi-squared", math=r"\chi^2 = \frac{(200-180)^2}{180} + \frac{(200-240)^2}{240} + \frac{(100-80)^2}{80} = 2.22 + 6.67 + 5.00 = 13.89"),
            S("Degrees of freedom", text="3 classes, minus 1, minus 1 because the allele frequency was estimated from the data: 1 degree of freedom. Critical value at 5%: 3.84."),
            S("Conclusion", text="13.89 > 3.84, so the population is **not** in equilibrium. There are too few heterozygotes and too many homozygotes; this may be due to non-random mating (inbreeding) or selection. Some textbooks use fewer steps; check your syllabus."),
        ]),
        H("What changes allele frequencies?"),
        T("Real populations seldom meet all the conditions. Allele frequencies change by:"),
        KEY("Causes of change", "Evolution is a change in allele frequencies in a population.", cards=[
            ["Natural selection", "Individuals with better-adapted alleles survive and breed more. For example, the sickle cell allele is kept at a high frequency in malaria regions by heterozygote advantage."],
            ["Genetic drift", "Chance changes in allele frequencies, strong in small populations (for example, a founder effect when a few individuals start a new colony)."],
            ["Gene flow", "Migration of individuals or movement of gametes (pollen) between populations brings new alleles."],
            ["Mutation", "Creates new alleles. The rate is low, but it is the source of all new variation."],
            ["Non-random mating", "Inbreeding or choosing mates changes the genotype frequencies but not the allele frequencies by itself."],
        ]),
        H("Speciation"),
        D("A **species** is a group of organisms that can interbreed to produce **fertile** offspring and that is reproductively isolated from other such groups. (This definition does not work well for organisms that reproduce asexually or for fossils. Textbooks give other definitions; check yours.)", title="Definition: species"),
        D("**Speciation** is the formation of new species, when populations of one species become **reproductively isolated** and so cannot exchange genes.", title="Definition: speciation"),
        T("**Allopatric speciation** (allo = different, patria = country) begins with a **geographical barrier**, such as a mountain range, a river or the sea, which splits a population in two. "
          "The two populations have no gene flow. Mutation, drift and natural selection, in different habitats, change their gene pools. "
          "Over time they become so different that, if they meet again, they cannot interbreed to produce fertile offspring."),
        T("**Sympatric speciation** (sym = same) occurs **within the same area**, with no geographical barrier. Reproductive isolation arises in another way: "
          "polyploidy in plants (a tetraploid plant cannot breed with its diploid relatives), or differences in food or breeding behaviour between groups in the same habitat. "
          "Many scientists think that the small cichlid fish of Lake Barombi Mbo, a crater lake in south-west Cameroon, formed in this way, though the evidence is debated."),
        T("**Reproductive isolating mechanisms** keep species apart. Before fertilisation: different habitats, different breeding seasons, different courtship behaviour, different flower shape or pollinators, and incompatible gametes. "
          "After fertilisation: hybrids that are weak or infertile (a mule, from a horse and a donkey, is sterile)."),
        TIP("In calculations, always say what p and q stand for. Start from the figure you are given: q² if you know the frequency of the recessive phenotype, or count alleles if you have genotype numbers. Convert to a proportion, not a percentage, before using the equation."),
        MISTAKE("Taking the frequency of the disease as q", "The frequency of **affected people** is q², not q. You must take the square root to get q. The carrier frequency is 2pq."),
        MISTAKE("Treating p + q as the genotype frequencies", "p + q = 1 is for **alleles**. p², 2pq and q² are for **genotypes**."),
        QUIZ("The frequency of the recessive allele q is 0.3. What is the frequency of heterozygotes?",
             ["0.09", "0.21", "0.42", "0.49"], 2,
             "p = 0.7. 2pq = 2 × 0.7 × 0.3 = 0.42.",
             hint="First find p.",
             feedback=["0.09 is q squared.", "0.21 is p times q (without the 2).", "", "0.49 is p squared."]),
        QUIZ("Which of the following is needed for a population to be in Hardy-Weinberg equilibrium?",
             ["Natural selection acting on the alleles", "A small population", "Random mating", "Migration into the population"], 2,
             "Random mating is one of the conditions. Selection, small size and migration all disturb the equilibrium.",
             hint="Which of these is a condition and not a disturbance?",
             feedback=["Selection changes allele frequencies.", "Small populations are affected by chance (drift).", "", "Migration (gene flow) changes allele frequencies."]),
        PQ("Cystic fibrosis is caused by a recessive allele. In a European population the frequency of the disease is about 1 in 2500. Calculate the carrier frequency. (Use the 1 in 2500 figure as a teaching value.)",
           "q² = 1/2500 = 0.0004. q = 0.02. p = 0.98. 2pq = 2 × 0.98 × 0.02 = 0.0392, which is about 3.9%, or about 1 person in 25."),
        PQ("In a population of 1000 plants the frequency of the recessive allele for white flowers (w) is 0.4. Calculate the expected numbers of RR, Rw and ww plants.",
           "q = 0.4 so p = 0.6. RR: p² = 0.36, 360 plants. Rw: 2pq = 0.48, 480 plants. ww: q² = 0.16, 160 plants. Total 1000."),
        PQ("Explain how a mountain range can lead to the formation of two species from one.",
           "The mountain range separates a population into two populations, and prevents gene flow. Mutation produces different alleles in each, and different environments favour different alleles by natural selection, with genetic drift as well. Over many generations the gene pools become so different that, even if the barrier is removed, the two cannot interbreed to produce fertile offspring. They are reproductively isolated, so they are separate species (allopatric speciation)."),
        PQ("Give three conditions that must be true for the Hardy-Weinberg equation to apply and say why each is rarely true.",
           "Random mating: many animals choose mates and people marry by choice or within communities. No selection: some genotypes always survive better. No migration or mutation: populations are rarely isolated and mutations always occur. Large population: small populations show drift. So the equation is a model to compare real populations with, not an exact description."),
        SUM("p + q = 1 for alleles; p² + 2pq + q² = 1 for genotypes. The frequency of recessive homozygotes is q², so q is its square root.",
            "The principle applies only in a large, randomly mating population without mutation, migration or selection.",
            "Selection, drift, gene flow and mutation change allele frequencies; evolution is a change in allele frequency.",
            "Speciation needs reproductive isolation: allopatric (a geographical barrier) or sympatric (no barrier, for example polyploidy)."),
    ],
))


# ------------------------------------------------------------------ 14. Recombinant DNA techniques
LESSONS.append(lesson(
    module=M_BIO,
    topic="Recombinant DNA techniques",
    title="Recombinant DNA: restriction enzymes, ligase and vectors",
    slug="biu2-recombinant-dna-techniques",
    minutes=25,
    summary="How a gene is cut out with restriction endonucleases, joined into a plasmid with DNA ligase, put into bacteria and selected, using the production of human insulin as the example.",
    objectives=[
        "Describe how restriction endonucleases cut DNA and leave sticky ends",
        "Explain the roles of DNA ligase, plasmid vectors and marker genes",
        "Explain why reverse transcriptase is used to make cDNA",
        "Describe how transformed bacteria are identified and calculate fragment sizes after a digest",
    ],
    key_concepts=["Restriction endonuclease", "Sticky ends", "DNA ligase", "Plasmid vector", "cDNA and reverse transcriptase", "Transformation", "Marker gene"],
    blocks=[
        H("Introduction"),
        T("A person with type 1 diabetes in Douala needs insulin every day. Until the 1980s, insulin came only from the pancreas of pigs and cattle. "
          "Today most insulin is human insulin made by bacteria or yeast that carry the human gene. This is an example of **genetic engineering**, the transfer of a gene from one organism to another."),
        D("**Recombinant DNA** is DNA made by joining together pieces from two or more different sources, so that it contains a combination of genes that does not exist in nature. **Genetic engineering** is the use of such techniques to change the genes of an organism.", title="Definition: recombinant DNA"),
        T("The genetic code is universal: the same codons code for the same amino acids in bacteria and in humans. This is why a human gene can work in a bacterium. "
          "The steps are: obtain the gene, cut the vector, join the gene into the vector, put the vector into a host cell, and select the cells that took it up."),
        IMG("al-biu2-recombinant-dna.svg", alt="Three steps: cut the plasmid and gene with the same enzyme, mix and join with ligase to make a recombinant plasmid, and put the plasmid into a bacterium",
            caption="Figure 1. The main steps in making recombinant DNA."),
        H("Step 1: Obtaining the gene"),
        T("There are three main ways. The gene can be **cut out** of the genome with restriction enzymes. It can be **made from mRNA** using reverse transcriptase. Or it can be **synthesised** chemically if the base sequence is known."),
        T("In human cells, a gene has non-coding sections (introns) that are removed from the pre-mRNA. Bacteria cannot remove introns. So a gene taken from human DNA would not give a working protein in a bacterium. "
          "Instead, mRNA for insulin is taken from pancreatic beta cells, which make a lot of it. The enzyme **reverse transcriptase** makes a single strand of **complementary DNA (cDNA)** from the mRNA. DNA polymerase then makes the second strand. The cDNA has no introns."),
        H("Step 2: Cutting DNA with restriction endonucleases"),
        D("A **restriction endonuclease** (restriction enzyme) is an enzyme from bacteria that cuts DNA at a specific base sequence called a **recognition site**. In bacteria it is a defence against invading viruses.", title="Definition: restriction endonuclease"),
        T("Recognition sites are usually 4 to 8 base pairs long and are **palindromic**: the sequence reads the same 5' to 3' on both strands. "
          "For example, the enzyme **EcoRI** recognises GAATTC. The opposite strand, read 5' to 3', is also GAATTC. "
          "EcoRI cuts each strand between G and A. The cuts are staggered, so each end has a short single-stranded overhang, AATT. These are **sticky ends** because they can form hydrogen bonds with complementary bases on any other DNA cut with the same enzyme. "
          "Some enzymes cut straight across, leaving **blunt ends**, which are harder to join."),
        CODE("""5'-G AATT C-3'          cut           5'-G        AATT C-3'
3'-C TTAA G-5'      ---------->      3'-C TTAA        G-5'

Each fragment has an overhang (sticky end).""", "text", title="EcoRI cuts GAATTC"),
        T("To join a gene into a plasmid, **both** the gene and the plasmid are cut with the **same enzyme**, so their sticky ends match."),
        H("Step 3: Joining with DNA ligase"),
        T("When the cut plasmid and the gene are mixed, the sticky ends pair by hydrogen bonds between complementary bases. But the sugar-phosphate backbone still has breaks. "
          "**DNA ligase** makes the phosphodiester bonds that seal them, to give a continuous recombinant molecule."),
        H("Vectors"),
        D("A **vector** is a DNA molecule used to carry a gene into a host cell. The commonest vector for bacteria is a **plasmid**: a small, circular DNA molecule found in bacteria, separate from the main chromosome.", title="Definition: vector"),
        T("A good plasmid vector has an **origin of replication** (so it copies itself in the host), a **single** recognition site for the restriction enzyme (so it is cut only once), and **marker genes** that make it easy to find cells that have it. "
          "Marker genes are often genes for antibiotic resistance. Other vectors are viruses (bacteriophages for bacteria, others for animal cells) and the Ti plasmid of the soil bacterium *Agrobacterium* for plants."),
        H("Step 4: Putting the vector in the host: transformation"),
        T("Bacteria are made more permeable to DNA by treating them with calcium chloride and then a short heat shock, or with a brief electric pulse (electroporation). "
          "Only a small proportion of the cells take up a plasmid. **Transformation** is the uptake and expression of foreign DNA by a host cell."),
        H("Step 5: Selection with marker genes"),
        T("Suppose the plasmid has two resistance genes: ampR (resistance to ampicillin) and tetR (resistance to tetracycline). The gene of interest is inserted **inside the tetR gene**, which stops it working (insertional inactivation). "
          "Bacteria are grown on agar with ampicillin. Only cells with a plasmid (recombinant or not) survive. Colonies are then copied to a plate with tetracycline (replica plating). "
          "Colonies that grow on ampicillin but **not** on tetracycline contain **recombinant** plasmids, because tetR was disrupted."),
        CODE("""Cells                          Ampicillin     Ampicillin + tetracycline
No plasmid                     die            die
Plasmid with no insert         grow           grow
Recombinant plasmid (insert    grow           die
 inside tetR)                                 (select these)""", "text", title="Selecting recombinant bacteria"),
        T("Selected cells are grown in large fermenters. The bacteria make human insulin, which is purified for medicine. Other products of this kind include human growth hormone and factor VIII for haemophilia."),
        EX("Worked example 1: restriction fragments of a linear DNA", intro="A linear DNA fragment of 5000 base pairs has EcoRI sites at 1000 bp and at 3500 bp from one end. How many fragments result and how long are they?", steps=[
            S("Number of fragments", text="A linear molecule cut at 2 sites gives 2 + 1 = 3 fragments."),
            S("Lengths", math=r"1000, \quad 3500 - 1000 = 2500, \quad 5000 - 3500 = 1500"),
            S("Check", math=r"1000 + 2500 + 1500 = 5000"),
        ]),
        EX("Worked example 2: a circular plasmid", intro="A circular plasmid of 4000 bp has two EcoRI sites, 1200 bp apart (measured along the shorter arc). Give the fragment sizes after digestion, and after digestion with an enzyme that cuts the plasmid only once.", steps=[
            S("Two sites on a circle", text="Two cuts on a circular molecule give two fragments: 1200 bp and 4000 − 1200 = 2800 bp."),
            S("One site", text="One cut opens the circle into one linear molecule of 4000 bp. This is why a vector should have a single site for the enzyme."),
        ]),
        EX("Worked example 3: interpreting selection", intro="A recombinant plasmid has the insulin gene inserted into the middle of tetR. Predict growth on ampicillin and on tetracycline for (a) a recombinant colony and (b) a colony that took up a plasmid that closed without the gene.", steps=[
            S("(a) Recombinant", text="ampR is working, so it grows on ampicillin. tetR is disrupted, so it does **not** grow on tetracycline."),
            S("(b) Plasmid with no insert", text="Both resistance genes work. It grows on both."),
            S("Use", text="We select the colonies that grow on ampicillin only."),
        ]),
        TIP("In Paper 2, a description of genetic engineering has a fixed order: obtain gene (reverse transcriptase), cut with restriction enzyme, vector cut with the same enzyme, ligase, put into host, select with marker. Name the enzyme at each step."),
        MISTAKE("Saying ligase joins the sticky ends by hydrogen bonds", "The sticky ends pair by hydrogen bonds between bases (this is not an enzyme action). Ligase forms **phosphodiester bonds** in the backbone."),
        MISTAKE("Saying restriction enzymes cut DNA at random", "Each enzyme recognises one specific base sequence and cuts only there."),
        QUIZ("Why is mRNA, and not the gene from the genome, used as the starting point for making a human gene for insulin in bacteria?",
             ["Bacteria cannot read DNA.", "mRNA has had the introns removed, which bacteria cannot do.", "Insulin mRNA is smaller than the gene and travels faster.", "Restriction enzymes cannot cut human DNA."], 1,
             "cDNA made from mRNA has no introns, so a bacterium can express it.",
             hint="What does a bacterium lack that a human cell has when making mRNA?",
             feedback=["Bacteria read DNA by transcription as usual.", "", "Size is not the reason.", "Restriction enzymes cut any DNA that has the recognition site."]),
        QUIZ("Which enzyme seals the gap between the DNA of the gene and the DNA of the plasmid?",
             ["Restriction endonuclease", "DNA polymerase", "DNA ligase", "Reverse transcriptase"], 2,
             "DNA ligase forms phosphodiester bonds between the nucleotides.",
             hint="Which enzyme joins and which one cuts?",
             feedback=["It cuts DNA.", "It adds new nucleotides to a growing strand using a template.", "", "It makes DNA from RNA."]),
        PQ("Describe how a human gene can be inserted into a bacterial plasmid.",
           "The plasmid and the gene (or cDNA) are cut with the same restriction endonuclease, which leaves sticky ends with complementary bases. The cut gene and plasmid are mixed so that the sticky ends pair by hydrogen bonds. DNA ligase seals the sugar-phosphate backbone, giving a recombinant plasmid. The plasmid is put into bacteria (for example with calcium chloride and heat shock)."),
        PQ("A plasmid carries genes for resistance to ampicillin and tetracycline. A gene is inserted into the tetracycline resistance gene. Explain how you could identify the bacteria that contain the recombinant plasmid.",
           "Grow the bacteria on agar with ampicillin. Only bacteria with a plasmid survive. Make a replica of the colonies onto agar with tetracycline. Colonies that grew on ampicillin but are missing from the tetracycline plate contain plasmids in which tetR has been disrupted by the inserted gene. Pick these colonies from the original plate."),
        PQ("A linear DNA molecule of 6000 base pairs is cut by a restriction enzyme at positions 1500 and 4000 from one end. Give the sizes of the fragments. If a second enzyme cuts at 2500 only, what are the sizes with the second enzyme?",
           "First enzyme: 1500, 4000 − 1500 = 2500 and 6000 − 4000 = 2000 bp, which add to 6000. Second enzyme: 2500 and 6000 − 2500 = 3500 bp."),
        PQ("State three features of a good plasmid vector and explain why each is needed.",
           "An origin of replication, so the plasmid copies itself when the host divides. A single recognition site for the restriction enzyme, so that the plasmid is cut once and the gene can be inserted without breaking up the plasmid. A marker gene, such as antibiotic resistance, so that cells that have taken up the plasmid can be identified. (Also small size, which makes it easy to enter cells.)"),
        SUM("Genetic engineering moves a gene into another organism; the universal code lets the gene work.",
            "A restriction endonuclease cuts at a palindromic recognition site, often leaving sticky ends. The gene and plasmid are cut with the same enzyme.",
            "DNA ligase seals the backbone. cDNA, made with reverse transcriptase, has no introns.",
            "Plasmid vectors enter bacteria by transformation. Marker genes, such as antibiotic resistance, identify the transformed (recombinant) cells."),
    ],
))

# ------------------------------------------------------------------ 15. PCR, electrophoresis and sequencing
LESSONS.append(lesson(
    module=M_BIO,
    topic="PCR, electrophoresis and sequencing",
    title="PCR, gel electrophoresis, DNA sequencing and DNA profiling",
    slug="biu2-pcr-electrophoresis-sequencing",
    minutes=26,
    summary="How the polymerase chain reaction copies DNA, how gel electrophoresis separates fragments by size, how the Sanger method reads a sequence, and how DNA profiles are used.",
    objectives=[
        "Describe the three stages of a PCR cycle and the role of Taq polymerase and primers",
        "Calculate the number of copies after n cycles",
        "Explain how gel electrophoresis separates DNA and estimate a fragment size from a calibration",
        "Outline the Sanger chain-termination method and uses of DNA profiling",
    ],
    key_concepts=["PCR", "Primers", "Taq polymerase", "Gel electrophoresis", "Calibration with a ladder", "Chain-terminating nucleotides", "DNA profile"],
    blocks=[
        H("Introduction"),
        T("A laboratory in Yaounde needs to detect a virus in a blood sample. There are only a few viral genomes in a small drop. To see them, the lab first makes millions of copies of a small part of the genome. "
          "The same technique is used to analyse DNA from a hair left at a crime scene. The technique is the **polymerase chain reaction (PCR)**."),
        H("PCR"),
        D("The **polymerase chain reaction** is a technique that makes millions of copies of a chosen section of DNA in a few hours, in a machine called a thermal cycler.", title="Definition: PCR"),
        T("The tube contains: the **template DNA**; two short single-stranded **primers** (about 20 nucleotides each) complementary to the two ends of the target sequence; free **nucleotides** (dNTPs); "
          "a heat-stable DNA polymerase, **Taq polymerase** (from the bacterium *Thermus aquaticus*, which lives in hot springs); and a buffer with magnesium ions."),
        IMG("al-biu2-pcr-cycle.svg", alt="Three boxes showing denature at 95 degrees where strands separate, anneal at 55 degrees where primers bind, and extend at 72 degrees where Taq polymerase copies the strands",
            caption="Figure 1. One cycle of PCR."),
        KEY("One cycle has three steps", "The temperatures are typical values.", cards=[
            ["1 Denaturation, about 95 degrees C", "The hydrogen bonds between the two strands break, so the DNA becomes single-stranded."],
            ["2 Annealing, about 50 to 65 degrees C", "The mixture is cooled. The primers bind (anneal) to complementary sequences on each strand."],
            ["3 Extension, about 72 degrees C", "Taq polymerase adds nucleotides to the 3' end of each primer, making a complementary strand."],
        ]),
        T("Taq polymerase is used because it is not destroyed at 95 degrees C. An ordinary enzyme would be denatured in the first cycle. Each cycle doubles the number of copies of the target (ideally). "
          "After n cycles there are 2 to the power n copies of a single starting molecule."),
        F(r"\text{copies after } n \text{ cycles} = N_0 \times 2^n", title="Ideal copy number"),
        EX("Worked example 1: copies after 30 cycles", intro="A sample has 1 molecule of target DNA. How many copies are present after 30 cycles of ideal PCR?", steps=[
            S("Use the formula", math=r"2^{30} = 1\,073\,741\,824"),
            S("Say it in words", text="More than a thousand million copies. In practice the reaction is less than 100% efficient, so the real number is lower, and it levels off when the reagents are used up."),
        ]),
        T("PCR is used to detect pathogens, diagnose genetic disease, make DNA for sequencing and cloning, and in forensic science. It needs a very clean method, because stray DNA (contamination) will also be copied."),
        H("Gel electrophoresis"),
        D("**Gel electrophoresis** separates charged molecules in an electric field according to their size. DNA fragments are placed in wells at one end of a gel (agarose) in a buffer solution. A voltage is applied.", title="Definition: gel electrophoresis"),
        T("DNA is **negatively charged** because of its phosphate groups. In an electric field it moves towards the **positive electrode (anode)**. The gel is a mesh. **Small fragments move farther** and **large fragments move less** in the same time. "
          "After the run, the DNA is made visible with a dye that binds to DNA and fluoresces under ultraviolet light, or with a labelled probe."),
        IMG("al-biu2-gel.svg", alt="A gel with three lanes: a ladder of known sizes 2000, 1000, 500, 250 and 100 base pairs, and two sample lanes with bands, with an arrow showing DNA moving towards the positive end",
            caption="Figure 2. Gel electrophoresis with a size ladder. Smaller fragments travel farther from the wells."),
        T("A **ladder** is a mixture of fragments of known sizes in one lane. A graph of distance moved against the logarithm of fragment size is close to a straight line. "
          "You can read the size of an unknown fragment from the graph."),
        EX("Worked example 2: size of an unknown fragment", intro="A gel was run with a ladder. Distances moved from the well (mm): 2000 bp, 15 mm; 1000 bp, 27 mm; 500 bp, 39 mm; 250 bp, 51 mm. An unknown fragment moved 33 mm. Estimate its size.", steps=[
            S("Pattern", text="Each halving of the size (2000 to 1000 to 500 to 250) adds 12 mm. So distance is a straight-line function of log size."),
            S("Position", text="33 mm lies between 27 mm (1000 bp) and 39 mm (500 bp), exactly half way (6 mm of 12 mm)."),
            S("Estimate", math=r"\log_{10} s = 3 - \frac{6}{12} \times 0.301 = 2.85 \Rightarrow s \approx 708", text="So the fragment is about 700 bp. Half way on the log scale means the geometric mean of 1000 and 500, which is 707."),
        ]),
        H("DNA sequencing: the Sanger method"),
        T("The Sanger (chain-termination) method makes copies of a template with DNA polymerase, a primer and the four normal nucleotides. "
          "A small proportion of special **dideoxynucleotides (ddNTPs)** is added, each labelled with a different fluorescent dye. A ddNTP has no 3'-OH group. "
          "When it is added to a growing chain, no further nucleotide can be joined, so the chain **stops**. "
          "The reaction gives a mixture of fragments of every possible length, each ending with a labelled ddNTP of the base at that point."),
        T("The fragments are separated by size (electrophoresis in a very thin capillary), and a detector reads the colour of the last base in each fragment, from the shortest to the longest. "
          "The order of colours is the sequence of the **new** strand. The template sequence is its complement."),
        CODE("""Fragments, shortest to longest, with last base (ddNTP):
length  1  2  3  4  5  6  7
last    T  A  C  G  G  A  T

New strand (5' to 3'):      T A C G G A T
Template (complement):      A T G C C T A   (3' to 5')""", "text", title="Reading a Sanger result (invented)"),
        T("Modern methods (next-generation sequencing) read millions of short fragments at the same time, and have greatly lowered the cost, which allowed whole genomes to be sequenced, including the human genome."),
        H("DNA profiling"),
        T("Human DNA contains short sequences repeated one after the other, called short tandem repeats (STRs). The number of repeats at each place (locus) varies between people. "
          "The STR loci are copied by PCR and the fragments separated by electrophoresis. The band pattern is a **DNA profile**. "
          "Two people (except identical twins) have different profiles. A child gets half of the bands from the mother and half from the father. "
          "Profiles are used in forensic science to match suspects to samples, to establish paternity, to identify remains after disasters and to study biodiversity. "
          "A match gives a statistical probability, not absolute certainty, and the results depend on correct handling of samples."),
        TIP("In a Paper 2 question about PCR, name each ingredient and say why Taq is used. In a gel question, give the direction (towards the positive electrode), explain why (DNA is negatively charged) and say that smaller pieces move faster and farther."),
        MISTAKE("Saying DNA moves towards the negative electrode", "DNA has a net **negative** charge, so it is attracted to the **positive** electrode."),
        MISTAKE("Saying PCR copies the whole genome", "PCR copies only the section between the two primers."),
        QUIZ("After 10 cycles of ideal PCR, how many copies are there from one starting molecule?",
             ["20", "100", "1024", "10 000"], 2,
             "2 to the power 10 = 1024.",
             hint="Each cycle doubles.",
             feedback=["That would be adding 2 each cycle.", "Not 10 squared; each cycle doubles.", "", "That would be 10 to the 4th power."]),
        QUIZ("Why do smaller DNA fragments move farther in a gel?",
             ["They have a greater charge per base.", "They pass through the pores of the gel more easily.", "They are more strongly attracted to the electrodes.", "They contain no phosphate."], 1,
             "All DNA has about the same charge per unit length, so the speed depends on how easily the molecule moves through the gel mesh. Small ones move more easily.",
             hint="Think of a mesh.",
             feedback=["The charge per base is roughly the same.", "", "The force per unit length is the same.", "All DNA has phosphate groups."]),
        PQ("Explain why heat-stable DNA polymerase is used in PCR, and describe what happens at 95, 55 and 72 degrees C.",
           "The mixture is heated to about 95 degrees C each cycle; an ordinary DNA polymerase would denature, whereas Taq polymerase from a heat-loving bacterium survives. At about 95 degrees C the hydrogen bonds between the strands break (denaturation). At about 55 degrees C the primers bind (anneal) to complementary sequences at the ends of the target. At about 72 degrees C Taq polymerase extends the primers by adding complementary nucleotides to make two double-stranded copies."),
        PQ("A gel is run with DNA fragments of 800, 300 and 150 bp. Describe where each is found and explain.",
           "DNA moves towards the positive electrode, because it is negatively charged. The smallest fragment, 150 bp, moves farthest from the well; the 300 bp fragment is next; the largest, 800 bp, is nearest the well, because large molecules move through the gel mesh more slowly."),
        PQ("A mother, her child and two men (X and Y) each have a DNA profile of three bands: Mother bands at 12, 18, 25; Child 12, 21, 25; Man X 14, 21, 30; Man Y 14, 17, 31 (all invented). Which man could be the father, and what can you say about the result?",
           "The child's bands at 12 and 25 are also found in the mother, so the band at 21 must come from the father. Man X has a band at 21 and could be the father. Man Y has no band at 21 and is excluded. A match with X does not prove paternity; more loci are needed to make the probability high."),
        PQ("Describe how dideoxynucleotides are used in the Sanger method to find the base sequence of DNA.",
           "DNA polymerase copies the template using normal nucleotides and a small proportion of fluorescently labelled ddNTPs, which have no 3'-OH and so stop the chain when incorporated. This produces fragments of all lengths, each ending in a ddNTP of a known base. The fragments are separated by size and the colour of the last base is read in order of size to give the sequence of the new strand."),
        SUM("PCR makes copies of a target region by repeated cycles of denaturing (about 95 degrees C), annealing of primers (about 55) and extension by Taq polymerase (about 72). Copies = 2 to the power n.",
            "Gel electrophoresis separates DNA by size: negative DNA moves to the positive electrode, small fragments move farther. A ladder gives sizes.",
            "Sanger sequencing uses chain-terminating ddNTPs to make fragments ending at each base.",
            "DNA profiles from STRs are used in forensic science, paternity and identification, with results given as probabilities."),
    ],
))

# ------------------------------------------------------------------ 16. GMOs and gene therapy
LESSONS.append(lesson(
    module=M_BIO,
    topic="GMOs and gene therapy",
    title="Genetically modified organisms and gene therapy: benefits, risks and ethics",
    slug="biu2-gmos-gene-therapy",
    minutes=25,
    summary="How GM crops and animals are made and used, how somatic gene therapy works, and how to weigh benefits, risks and ethical questions in a balanced way.",
    objectives=[
        "Define a GMO and give examples of GM crops, GM microorganisms and their uses",
        "Describe how somatic gene therapy is carried out and its limits",
        "Distinguish somatic and germ-line gene therapy",
        "Evaluate benefits, risks and ethical issues in a balanced answer",
    ],
    key_concepts=["Genetically modified organism", "Bt crops", "Golden rice", "Gene therapy", "Somatic and germ-line", "Viral vectors", "Ethical evaluation"],
    blocks=[
        H("Introduction"),
        T("Cotton farmers in northern Cameroon lose part of their crop to caterpillars (bollworms). Some farmers in other countries grow cotton with a gene that makes the plant produce a protein toxic to those caterpillars. "
          "Other people worry about what such crops do to the environment, to seed prices and to health. "
          "Biology can supply evidence, but the decision also involves farmers, consumers and governments. In this lesson we examine the science and the arguments on both sides."),
        D("A **genetically modified organism (GMO)** is an organism whose genome has been changed by genetic engineering, usually by adding a gene from another species (a **transgene**). A **transgenic** organism has a gene from another species.", title="Definition: GMO"),
        H("How GM crops are made"),
        T("The gene is cut out or synthesised and inserted into a vector. For plants the vector is often the **Ti plasmid** of the bacterium *Agrobacterium tumefaciens*, which naturally transfers DNA into plant cells. "
          "Another method shoots tiny gold particles coated with DNA into plant cells (a gene gun). A marker gene is included. Single cells that take up the gene are grown in tissue culture (with plant growth regulators) into whole plants."),
        H("Examples and uses"),
        KEY("Examples of GMOs", "Each has been developed for a particular purpose.", cards=[
            ["Bt crops", "A gene from the soil bacterium *Bacillus thuringiensis* codes for a toxin (Bt toxin) that kills certain insects when they eat the plant. Used in cotton and maize in several countries. Aim: less crop loss and less spraying of insecticide."],
            ["Golden rice", "Rice with genes added so that the grain makes beta-carotene, which the body turns into vitamin A. Aim: reduce vitamin A deficiency, which causes blindness and increases deaths from infections."],
            ["Herbicide-tolerant crops", "Crops that survive a particular weedkiller, so that weeds can be killed without killing the crop."],
            ["Microorganisms", "Bacteria and yeast that make human insulin, growth hormone and enzymes for detergents and cheese making (rennet)."],
            ["Animals", "For example, goats that make a human protein in their milk; fish that grow faster. Few reach commercial use."],
        ]),
        H("Weighing benefits and risks"),
        T("The same technology can be assessed under several headings. Here is a balanced list. A good answer gives points on both sides and says that each case should be judged on its own evidence."),
        CODE("""Possible benefits                      Concerns and uncertainties
Higher yield, less crop loss           Pests may evolve resistance to Bt toxin
Less insecticide sprayed               Transgenes may spread to wild relatives
Added nutrients (golden rice)          Effects on non-target insects (debated)
Crops that tolerate drought or salt    Possible allergens must be tested
Cheaper medicines from microbes        Seeds protected by patents; cost to farmers
                                       Consumers want labelling and choice""", "text", title="GM crops: a balanced view"),
        T("Many scientific bodies, including the World Health Organization, say that GM foods that have passed safety assessment are no more likely to harm health than their conventional equivalents, and also say that each product must be assessed separately. "
          "Environmental effects are studied by field trials. Farmers using Bt crops are advised to plant a **refuge** of non-Bt plants, so that resistant pests mate with susceptible ones and resistance spreads more slowly. "
          "Whether to allow GM crops is also a matter of national law. Many countries have biosafety laws; students should check the current rules in Cameroon."),
        H("Gene therapy"),
        D("**Gene therapy** is the treatment of a genetic disease by putting a normal copy of a gene into the cells of a patient, to replace or make up for a faulty allele.", title="Definition: gene therapy"),
        T("In **somatic gene therapy**, the new gene is put into body cells. The change affects only the patient and is **not inherited**. "
          "In **germ-line gene therapy**, the change is made in gametes or an early embryo and would be passed to all later generations. Germ-line therapy in humans is prohibited or not permitted in most countries, because of the unknown long-term effects and ethical concerns."),
        T("**How it works (ex vivo).** Cells are taken from the patient (for example blood stem cells). A vector, often a modified virus that cannot cause disease, carries a working copy of the gene into the cells in the laboratory. "
          "The modified cells are returned to the patient. **In vivo** therapy puts the vector straight into the patient, for example by injection into the eye or the blood."),
        T("The first successful use was in severe combined immunodeficiency caused by lack of the enzyme adenosine deaminase (ADA-SCID), where children are born with almost no working immune system. "
          "Modified blood stem cells gave many patients a working immune system. In the later years, therapies have been developed for some inherited blood disorders, including sickle cell disease, using gene editing (check the current status in your textbook)."),
        KEY("Gene therapy: limits and risks", "A balanced view.", cards=[
            ["Technical limits", "The new gene may not be taken up by enough cells, may not stay active, or may only work for a time, so treatment may need repeating."],
            ["Safety", "The immune system may react to the vector. A vector that inserts into the genome can disrupt other genes: in some early trials this led to leukaemia."],
            ["Cost and access", "Treatments can cost very much, so most patients in poorer countries cannot reach them."],
            ["Ethics", "Should germ-line changes ever be allowed? Where is the line between treating disease and enhancing normal traits? Who decides?"],
        ]),
        EX("Worked example 1: how is a Bt cotton plant made?", intro="Outline the steps in making a Bt cotton plant.", steps=[
            S("Gene", text="The Bt toxin gene is isolated from the bacterium Bacillus thuringiensis."),
            S("Vector", text="It is inserted into the Ti plasmid of Agrobacterium (with a marker gene) using restriction enzymes and ligase."),
            S("Transfer", text="Cotton cells are infected with the bacterium, which transfers the DNA into the plant cells."),
            S("Select and grow", text="Cells that took up the gene are selected with the marker and grown in tissue culture into whole plants."),
        ]),
        EX("Worked example 2: a balanced evaluation", intro="Evaluate the statement: 'Golden rice should be grown in countries with a high level of vitamin A deficiency.'", steps=[
            S("For", text="It provides beta-carotene in a staple food, so people who eat rice every day would get a source of vitamin A. Vitamin A deficiency is a major cause of preventable blindness and increases child mortality."),
            S("Against or uncertain", text="Other ways exist: supplements, a varied diet, and food that is already rich in vitamin A. The amount of beta-carotene must be shown to be enough, and rice varieties adapted to local conditions are needed. Some people object to the technology itself, and regulation takes time."),
            S("Conclusion", text="The decision should be based on evidence of how well it works in a real community compared with other options. It need not replace them."),
        ]),
        TIP("A question that asks you to 'discuss' or 'evaluate' needs both sides and a reasoned conclusion. Do not simply praise or condemn. Use evidence words: 'may', 'in some cases', 'depends on'."),
        MISTAKE("Saying all GM foods are unsafe, or all are safe", "Safety is assessed product by product. A single sentence for all GMOs is not a scientific answer."),
        MISTAKE("Mixing up somatic and germ-line therapy", "Somatic therapy treats body cells and is **not inherited**. Germ-line therapy would alter gametes or embryos and **would** be inherited."),
        QUIZ("Why is somatic gene therapy not passed on to the patient's children?",
             ["The new gene is destroyed by the immune system.", "Only body cells are changed, not the gametes.", "The gene is always recessive.", "Children cannot inherit viral vectors."], 1,
             "Gametes are not altered, so the change is not inherited.",
             hint="Which cells make the next generation?",
             feedback=["That can be a problem, but it is not the reason.", "", "Dominance is not relevant.", "The vector is not the issue; the gene is in body cells only."]),
        QUIZ("In a Bt crop, which statement about resistance is correct?",
             ["Pests cannot become resistant because the gene is in the plant.", "Pests may evolve resistance, so refuges of non-Bt plants are recommended.", "Bt toxin is a hormone that stops pests breeding.", "Resistance is only a problem for non-GM crops."], 1,
             "Selection by the toxin favours resistant pests; a refuge slows the spread of resistance.",
             hint="What does natural selection do when the toxin is always present?",
             feedback=["Any control method puts selection pressure on pests.", "", "It is a protein toxin that damages the insect gut.", "Resistance can occur with any pest control."]),
        PQ("Describe how a gene for resistance to an insect pest could be inserted into a crop plant.",
           "The gene is cut out with a restriction enzyme and joined, using ligase, into the Ti plasmid of Agrobacterium tumefaciens together with a marker gene. Plant cells are infected with the bacterium, which transfers the DNA into the plant cell genome. Transformed cells are selected using the marker and grown in tissue culture with plant growth regulators into whole plants, which are tested and then bred."),
        PQ("Discuss the advantages and disadvantages of genetically modified crops.",
           "Advantages: increased yield or reduced loss to pests, less insecticide, added nutrients, tolerance of stress, longer storage. Disadvantages or concerns: pests may evolve resistance; transgenes may spread to wild relatives; possible effects on non-target organisms; allergenicity must be tested; patents and the cost of seed for small farmers; consumer wishes for labelling and choice. Each GM crop should be judged separately on its evidence, and the benefits weighed against alternatives."),
        PQ("Explain the difference between somatic and germ-line gene therapy and state why germ-line therapy is controversial.",
           "Somatic therapy puts a normal gene into body cells; the change affects only the patient and is not inherited. Germ-line therapy changes gametes or early embryos so that every cell, including gametes, carries the change, which passes to future generations. It is controversial because long-term effects are unknown, future generations cannot consent, errors could be permanent, and there are fears it could lead to selecting or enhancing traits."),
        PQ("Outline how ex vivo gene therapy could treat a child with ADA-SCID, and give one risk.",
           "Blood stem cells are removed from the child. A harmless modified virus carrying a working ADA gene is used to put the gene into the cells in the laboratory. The modified cells are returned to the child, where they divide and give cells that make the enzyme and a working immune system. Risks: the vector may insert next to a gene that controls cell division and cause leukaemia; the immune system may react; the effect may not last."),
        SUM("A GMO has a gene from another species added by genetic engineering. Bt crops, golden rice and microbes making insulin are examples.",
            "Benefits include yield, nutrition and cheaper medicines; concerns include resistance, gene flow, allergenicity, cost and choice. Judge each case on its evidence.",
            "Somatic gene therapy adds a working gene to body cells (ex vivo or in vivo) and is not inherited; germ-line therapy would be inherited and is widely not allowed.",
            "Gene therapy faces technical, safety, cost and ethical limits. Balanced evaluation gives both sides and a reasoned conclusion."),
    ],
))

# ------------------------------------------------------------------ 17. Monoclonal antibodies and fermentation
LESSONS.append(lesson(
    module=M_BIO,
    topic="Monoclonal antibodies and fermentation",
    title="Monoclonal antibodies and fermentation (batch and continuous culture)",
    slug="biu2-monoclonal-antibodies-fermentation",
    minutes=26,
    summary="How hybridoma cells make monoclonal antibodies and what they are used for, and how microorganisms are grown in fermenters in batch and continuous culture to make products such as penicillin and beer.",
    objectives=[
        "Describe how monoclonal antibodies are produced and list their uses",
        "Explain how a pregnancy test works",
        "Distinguish a culture from a culture medium, and batch from continuous culture",
        "Describe the growth curve of a bacterial culture and calculate population growth",
    ],
    key_concepts=["Monoclonal antibody", "Hybridoma", "Culture and culture medium", "Fermenter", "Batch culture", "Continuous culture", "Growth curve"],
    blocks=[
        H("Introduction"),
        T("A home pregnancy test gives a result in minutes. The test strip contains antibodies that bind to a single hormone in urine. "
          "The antibodies are made by cells grown in tanks. The same kind of tank, a fermenter, is used to make penicillin and, in a much older tradition, the local brews of Cameroon such as bili-bili. "
          "This lesson covers both topics: monoclonal antibodies and fermentation."),
        H("Monoclonal antibodies"),
        D("**Monoclonal antibodies** are identical antibodies, all made by one clone of cells, that bind to one specific antigen.", title="Definition: monoclonal antibody"),
        T("A single B lymphocyte makes only one kind of antibody, but it cannot be grown in the laboratory for long. A cancer cell (a **myeloma** cell) can divide again and again, but does not make the wanted antibody. "
          "A **hybridoma** combines the two."),
        KEY("Making monoclonal antibodies", "Follow the steps in order.", cards=[
            ["1 Immunise", "Inject a mouse with the antigen, so that its spleen makes B lymphocytes that make the antibody."],
            ["2 Fuse", "Take B lymphocytes from the spleen and fuse them with myeloma cells, using polyethylene glycol or a virus. The fused cells are **hybridoma** cells."],
            ["3 Select", "Grow the mixture in a medium that kills unfused cells. Test the hybridomas and keep those that make the wanted antibody."],
            ["4 Grow", "Culture the selected hybridoma in fermenters. The cells divide indefinitely, and each makes the same antibody."],
            ["5 Purify", "Collect and purify the antibody from the medium."],
        ]),
        T("**Uses.** Diagnosis: pregnancy tests (antibody to hCG) and tests for infections, including malaria and HIV rapid tests. Treatment: antibodies that bind to cancer cells (for example, the drug trastuzumab for some breast cancers) and block them or deliver a drug. Purification: antibody fixed to a column removes one protein from a mixture. Research: labelling a protein in a cell. "
          "**Limits:** antibodies from mice can be seen as foreign by the human immune system, so they are changed to \"humanised\" forms. Production is expensive."),
        T("**A pregnancy test.** Urine moves along a strip. The first zone has mobile antibodies against hCG, joined to coloured particles. If hCG is present, it binds to these antibodies. "
          "The complex moves on to the test line, where a second, fixed antibody against hCG binds it, and the line becomes coloured. A control line holds antibodies that bind the mobile antibody whether or not hCG is present; it shows the test has worked."),
        H("Fermentation and microbial culture"),
        D("A **culture** is the growing of cells, tissues or microorganisms under controlled conditions. A **culture medium** is the mixture of nutrients and the conditions in which they grow: a carbon source (e.g. glucose), a nitrogen source, minerals, vitamins and water.", title="Culture and culture medium"),
        T("**Fermentation**, in industry, means the large-scale culture of microorganisms (bacteria, yeast, fungi) to make a product. It is done in a **fermenter** (bioreactor)."),
        KEY("Features of a fermenter", "Each solves a problem.", cards=[
            ["Sterility", "The vessel and medium are sterilised with steam, to prevent contaminants from competing with the culture."],
            ["Stirrer (paddles)", "Mixes the cells and nutrients and spreads the oxygen, and spreads the heat."],
            ["Air inlet (sparger)", "Bubbles in sterile air for aerobic cultures, such as those of fungi."],
            ["Cooling jacket", "Removes the heat made by the microbes' metabolism, so the temperature is kept at the optimum."],
            ["Probes and pH control", "Measure temperature and pH. Acid or alkali is added to keep the pH constant."],
        ]),
        T("**Batch culture.** The sterile medium is placed in the fermenter and inoculated with the microorganism. The culture grows, then the **whole contents** are harvested and the fermenter is emptied, cleaned and restarted. "
          "In a closed batch the growth shows a pattern:"),
        CODE("""Phase         What happens
Lag           Cells adjust and make enzymes; little division
Log           Rapid exponential growth; nutrients plentiful
Stationary    Growth rate = death rate; nutrients run low, waste builds up
Death         Cells die faster than new ones are made""", "text", title="Growth curve of a batch culture"),
        T("**Secondary metabolites**, such as the antibiotic **penicillin**, are made mainly in the **stationary phase**, when growth slows. They are not needed for growth. "
          "Penicillin comes from the fungus *Penicillium chrysogenum*. It is often produced in a **fed-batch** culture: nutrients are added slowly during the run, to keep the fungus making penicillin for longer. "
          "The product is extracted and purified (downstream processing)."),
        T("**Continuous culture.** Fresh medium is added at a steady rate and culture liquid is removed at the same rate. The volume stays constant. "
          "The culture is held in the log phase and a steady state is reached. It is used for products made during growth (**primary metabolites**) such as ethanol, single-cell protein and mycoprotein. "
          "It saves the time needed to empty, clean and restart, but contamination is a risk because the run is long and the equipment is in use for weeks."),
        CODE("""                       Batch culture               Continuous culture
Medium                 added once                  added all the time
Product                collected at the end        collected all the time
Growth phase           all phases                  held in log phase
Best for               secondary metabolites       primary metabolites
                       (penicillin)                (ethanol, mycoprotein)
Contamination          one batch lost              long run, higher risk
Down time              cleaning between batches    little""", "text", title="Batch and continuous culture compared"),
        T("**Traditional fermentation.** Local drinks such as bili-bili, sha'a (sorghum or maize beer) and palm wine are made by yeasts that ferment sugars to ethanol and carbon dioxide. "
          "In bili-bili, grain is malted (germinated, so that amylase makes sugar), cooked, cooled and fermented by yeast. Cassava is fermented by bacteria and yeasts to make foods such as bobolo and to reduce the cyanide in the root. "
          "Lactic acid bacteria ferment milk to make yoghurt. These are batch processes controlled by experience rather than by instruments."),
        F(r"N = N_0 \times 2^{t/g}", title="Population growth during the log phase"),
        T("Here N0 is the starting number, t is the time and g is the generation (doubling) time."),
        EX("Worked example 1: bacterial numbers", intro="A culture starts with 1000 cells. The generation time is 30 minutes. How many cells after 5 hours of log growth?", steps=[
            S("Number of generations", math=r"\frac{5 \times 60}{30} = 10"),
            S("Cells", math=r"N = 1000 \times 2^{10} = 1\,024\,000"),
            S("Remark", text="Real cultures do not keep growing like this: nutrients run out, and the stationary phase begins."),
        ]),
        EX("Worked example 2: choosing batch or continuous culture", intro="A company wants to make (a) penicillin and (b) fungal protein for human food (mycoprotein). Suggest the type of culture for each and give a reason.", steps=[
            S("(a) Penicillin", text="Fed-batch (a type of batch) culture. Penicillin is a secondary metabolite made in the stationary phase, so the culture should be taken beyond the phase of rapid growth."),
            S("(b) Mycoprotein", text="Continuous culture. The product is the biomass itself, made during growth, so the culture is kept in the log phase and harvested all the time."),
        ]),
        EX("Worked example 3: reading a growth curve", intro="A bacterium in batch culture has these counts (invented, in millions per cm3) at hours 0, 2, 4, 6, 8, 10, 12, 14: 1, 1, 4, 32, 256, 300, 300, 120. Name the phase from 0 to 2 h, from 4 to 8 h, from 10 to 12 h and at 14 h, and explain each.", steps=[
            S("0 to 2 h", text="Lag phase: the count does not rise. The bacteria are adjusting to the medium and making enzymes."),
            S("4 to 8 h", text="Log phase: the count rises 8-fold every 2 hours (4, 32, 256). This is steady exponential growth with plenty of nutrients."),
            S("10 to 12 h", text="Stationary phase: the count stays at 300. Division and death are balanced because nutrients are running low and waste is building up."),
            S("At 14 h", text="Death phase: the count has fallen to 120 because cells die faster than new ones form."),
        ]),
        TIP("The Board's report notes that candidates often did not state the **conditions** of the fermenter (temperature, pH, oxygen, carbon and nitrogen sources). Always give them when you describe a fermentation process."),
        MISTAKE("Mixing up culture and culture medium", "A **culture** is the growing of cells under controlled conditions (or the cells so grown). The **culture medium** is the nutrient mixture and conditions they are grown in."),
        MISTAKE("Saying penicillin is made in the log phase", "Penicillin is a secondary metabolite, produced mainly in the **stationary phase**."),
        QUIZ("In a pregnancy test strip, what is the purpose of the control line?",
             ["It detects hCG in the urine.", "It shows that the urine has flowed through and the test has worked.", "It shows that the woman is not pregnant.", "It detects LH."], 1,
             "The control line binds the mobile antibody whether or not hCG is present, so it appears whenever the test has worked.",
             hint="Think about what binds at the control line.",
             feedback=["The test line detects hCG.", "", "A missing control line means an invalid test.", "The test uses antibodies to hCG."]),
        QUIZ("Which of the following is a feature of continuous culture?",
             ["Whole contents harvested at the end", "Medium added and product removed at the same rate", "Growth held in the death phase", "Used mainly to make secondary metabolites"], 1,
             "In continuous culture the volume stays constant, with medium in and culture out at the same rate.",
             hint="Which one never stops?",
             feedback=["That is batch culture.", "", "It is held in the log phase.", "Secondary metabolites are made in batch culture."]),
        PQ("Describe how monoclonal antibodies are produced.",
           "A mouse is injected with the antigen so that B lymphocytes make antibodies to it. B lymphocytes are taken from the spleen and fused with myeloma (cancer) cells to make hybridoma cells. Hybridomas that make the required antibody are selected and cultured in fermenters. They divide indefinitely and each makes the same antibody, which is collected and purified."),
        PQ("Give three uses of monoclonal antibodies.",
           "Diagnosis, for example detecting hCG in pregnancy tests, or detecting infection; treatment, for example antibodies that bind to receptors on cancer cells, or deliver drugs to them; purification of a specific protein from a mixture; labelling and locating molecules in research."),
        PQ("Describe the main features of a fermenter and explain why each is needed.",
           "The vessel is sterile, so that unwanted microbes do not compete. A stirrer mixes the contents and spreads oxygen and heat. A sparger supplies sterile air for aerobic organisms. A cooling jacket removes the heat released by metabolism to keep the optimum temperature. Probes monitor pH, temperature and oxygen, and acid or alkali is added to keep pH constant. The medium supplies carbon, nitrogen, minerals and vitamins."),
        PQ("Distinguish between batch and continuous culture and explain why penicillin is made in a batch process.",
           "In batch culture, the medium is added once, the organism grows through lag, log, stationary and death phases, and the whole culture is harvested at the end. In continuous culture, medium is added and culture removed at the same rate, so the culture stays in log phase. Penicillin is a secondary metabolite made in the stationary phase when growth slows, so a batch (or fed-batch) process that allows the culture to reach this stage is used."),
        SUM("Monoclonal antibodies come from hybridoma cells (B lymphocyte fused with a myeloma cell) and bind one antigen. Uses: diagnosis (pregnancy tests), treatment, purification.",
            "A culture is the growing of cells under controlled conditions; the culture medium supplies nutrients. A fermenter controls sterility, mixing, aeration, temperature and pH.",
            "Batch culture goes through lag, log, stationary and death phases and suits secondary metabolites such as penicillin. Continuous culture holds the log phase and suits primary metabolites and biomass.",
            "Growth in log phase: N = N0 × 2 to the power t/g."),
    ],
))

# ------------------------------------------------------------------ 18. Immunity
LESSONS.append(lesson(
    module=M_BIO,
    topic="Immunity",
    title="Immunity: non-specific defence, B and T lymphocytes, antibodies and vaccination",
    slug="biu2-immunity-lymphocytes-vaccination",
    minutes=27,
    summary="The body's first and second lines of defence, how B lymphocytes and T lymphocytes work in humoral and cell-mediated immunity, antibody structure, primary and secondary responses, and how vaccines work.",
    objectives=[
        "Describe non-specific defences: barriers, phagocytosis, inflammation and interferons",
        "Distinguish humoral (B cell) and cell-mediated (T cell) immunity and the roles of each cell type",
        "Describe clonal selection, antibody structure and the primary and secondary responses",
        "Explain active and passive immunity, vaccination and herd immunity, and the effect of HIV",
    ],
    key_concepts=["Phagocytosis", "Antigen and antibody", "B lymphocyte and plasma cell", "T helper and T cytotoxic cells", "Memory cells", "Clonal selection", "Vaccination", "Herd immunity"],
    blocks=[
        H("Introduction"),
        T("A child in a village near Maroua is given a vaccine at the health centre and does not catch measles during an outbreak. "
          "The child's body has learnt to recognise the virus without being ill. "
          "The Board's report notes that many candidates cannot match the types of lymphocyte to their roles. Learn it carefully: each cell has its own job."),
        H("Non-specific defence"),
        T("The first line of defence is non-specific: it acts in the same way against any pathogen."),
        KEY("Non-specific defences", "Barriers keep pathogens out; cells and chemicals deal with those that get in.", cards=[
            ["Physical and chemical barriers", "Skin (tough keratin layer), mucus and cilia in the airways trap and move out microbes, lysozyme in tears and saliva digests bacterial walls, stomach acid kills many microbes that are swallowed."],
            ["Phagocytosis", "Phagocytes (neutrophils and macrophages) bind to a pathogen, engulf it in a vesicle (a phagosome), and fuse with lysosomes. Lysozyme and other enzymes digest the pathogen."],
            ["Inflammation", "Damaged cells and mast cells release histamine. Blood vessels widen and become leaky, so more blood and phagocytes reach the site. The area is red, hot and swollen."],
            ["Fever and interferons", "A raised temperature slows many pathogens and speeds the immune response. Cells infected by viruses release interferons, which make neighbouring cells resist the virus."],
        ]),
        H("Specific immunity: antigens and lymphocytes"),
        D("An **antigen** is a molecule, usually a protein or carbohydrate on the surface of a pathogen or a foreign cell, that causes the immune system to make a specific response. An **antibody** is a protein made by a plasma cell that binds to a specific antigen.", title="Antigen and antibody"),
        T("Self antigens are not attacked because the immune system learns not to respond to them. **Lymphocytes** are white blood cells made in the bone marrow. **B lymphocytes** mature in the bone marrow. **T lymphocytes** mature in the **thymus**. "
          "There are millions of different lymphocytes, each with receptors for one specific antigen."),
        H("Humoral immunity: B lymphocytes"),
        T("The word **humoral** refers to body fluids, because antibodies work in blood and tissue fluid. The steps:"),
        IMG("al-biu2-clonal-selection.svg", alt="B cells with different receptors; an antigen selects one B cell with the matching receptor; T helper cell releases cytokines; the selected cell divides by mitosis into plasma cells that secrete antibodies and memory cells",
            caption="Figure 1. Clonal selection of a B lymphocyte."),
        KEY("Humoral response", "In order.", cards=[
            ["1 Selection", "An antigen binds to the receptor of one B cell that has a complementary shape. This **selects** the cell."],
            ["2 Activation", "A T helper cell that recognises the same antigen releases **cytokines**, which activate the B cell."],
            ["3 Clonal expansion", "The B cell divides repeatedly by mitosis to make a **clone** of identical cells."],
            ["4 Differentiation", "Most of the clone become **plasma cells**, which make and secrete large numbers of antibodies. Some become **memory B cells**."],
        ]),
        T("**Antibody structure.** An antibody (immunoglobulin) is a Y-shaped protein made of four polypeptide chains: two long (heavy) and two short (light), joined by disulphide bridges. "
          "At the tips of the Y are the **variable regions**, whose shape is different in each antibody and forms the antigen-binding site. The rest is the **constant region**."),
        T("**How antibodies work.** They bind to antigens on pathogens, and can: cause bacteria to clump (agglutination), which makes phagocytosis easier; coat the pathogen so phagocytes recognise it (opsonisation); "
          "neutralise toxins and block viruses from entering cells; and activate a group of proteins (complement) that make holes in the pathogen cell."),
        H("Cell-mediated immunity: T lymphocytes"),
        T("Viruses hide inside body cells, where antibodies cannot reach them. **Cell-mediated immunity** deals with such cells, with cancer cells and with transplants. "
          "A macrophage or an infected cell shows pieces of the antigen on its surface. A T cell with a matching receptor binds to it."),
        KEY("Types of T lymphocyte", "Learn the job of each.", cards=[
            ["T helper cells", "Recognise the antigen presented. Release cytokines that activate B cells, T cytotoxic cells and macrophages. They are the 'managers' of the response. HIV attacks these cells."],
            ["T cytotoxic (killer) cells", "Bind to infected cells and kill them by releasing perforin, a protein that makes holes in the cell, and other enzymes that trigger the cell to die."],
            ["T memory cells", "Long-lived cells that remain after the infection, ready to respond quickly if the antigen returns."],
            ["T regulatory cells", "Reduce the immune response when the infection is over, and help to prevent attack on the body's own cells."],
        ]),
        H("Primary and secondary responses"),
        T("The first time a pathogen enters, there is a delay while the right B and T cells are selected and multiply. Antibody levels rise slowly to a modest peak. This is the **primary response**. "
          "Memory cells stay in the body. On a second infection by the same antigen, memory cells divide and differentiate rapidly. Antibody levels rise **faster** and to a **much higher** level and stay high longer. This is the **secondary response**. The person is usually not ill."),
        H("Active and passive immunity; vaccination"),
        CODE("""                  Active                          Passive
Antibodies made   by the person's own cells      received ready-made
Memory cells      yes                             no
Onset             slow (days to weeks)            immediate
Duration          long-lasting                    short (weeks to months)
Natural           infection                       antibodies across the placenta, in milk
Artificial        vaccination                     injection of antibodies (e.g. anti-venom)""", "text", title="Types of immunity"),
        D("**Vaccination** is the introduction of a harmless form of an antigen (a dead or weakened pathogen, a toxoid, a part of a pathogen or the genetic instructions for an antigen) to stimulate the primary immune response and the production of memory cells, without causing the disease.", title="Definition: vaccination"),
        T("A **booster** is a later dose that stimulates the secondary response and builds up higher, longer-lasting immunity. "
          "If enough people in a population are immune, a pathogen cannot spread easily and those who are not immune are indirectly protected. This is **herd immunity**. "
          "The proportion that must be immune depends on how infectious the disease is. If R0 is the number of people one case infects in a fully susceptible population, the minimum immune proportion is 1 minus 1 / R0."),
        T("**HIV** infects T helper cells and destroys them. Without enough T helper cells, B cells and cytotoxic T cells are not properly activated. The person develops acquired immune deficiency syndrome (AIDS) and is open to infections and cancers that a healthy immune system would control. "
          "Antiretroviral drugs reduce the amount of virus and allow a long and healthy life."),
        EX("Worked example 1: match the cell and the role", intro="State which cell is responsible for each: (a) secreting antibodies (b) killing a virus-infected cell (c) activating B cells with cytokines (d) responding fast on second infection.", steps=[
            S("(a)", text="Plasma cell (a differentiated B cell)."),
            S("(b)", text="T cytotoxic cell."),
            S("(c)", text="T helper cell."),
            S("(d)", text="Memory B and T cells."),
        ]),
        EX("Worked example 2: interpreting antibody levels", intro="A person is injected with an antigen on day 0 and again on day 28. Antibody level (arbitrary units) was 0 on day 0; 2 on day 7; 10 on day 14; 6 on day 28; 15 on day 31; 100 on day 35. Explain the shapes of the two peaks.", steps=[
            S("First dose", text="A slow rise to a low peak of 10 by day 14. Selection and clonal expansion of the few B cells with matching receptors take time."),
            S("Second dose (day 28)", text="Antibodies rise quickly (15 by day 31) and reach 100 by day 35, ten times the first peak. Memory B cells, already present in large numbers, divide and differentiate into plasma cells at once."),
            S("Conclusion", text="This is the secondary response, which is faster, bigger and longer lasting. It is the basis of booster vaccines."),
        ]),
        EX("Worked example 3: the herd immunity threshold", intro="A disease has R0 = 4 (invented). What proportion of the population needs to be immune to stop an epidemic?", steps=[
            S("Formula", math=r"1 - \frac{1}{R_0} = 1 - \frac{1}{4} = 0.75"),
            S("Answer", text="75% of the population must be immune. A more infectious disease (higher R0) needs a higher proportion."),
        ]),
        TIP("Link each cell to the **correct type of immunity**: B cells and plasma cells are humoral; T cytotoxic cells are cell-mediated; T helper cells assist both. The Board's examiners found that this is where most marks are lost."),
        MISTAKE("Saying that T cells make antibodies", "Only plasma cells (from B cells) make antibodies. T cells have receptors on their membranes, but they do not secrete antibodies."),
        MISTAKE("Saying that vaccines give passive immunity", "A vaccine makes the person produce their own antibodies and memory cells, so it is **active** immunity. Passive immunity is the supply of antibodies from outside."),
        QUIZ("Which cell directly kills a body cell that is infected with a virus?",
             ["Plasma cell", "T helper cell", "T cytotoxic cell", "Macrophage"], 2,
             "T cytotoxic cells bind to infected cells and kill them with perforin.",
             hint="Which cells act on infected cells?",
             feedback=["Plasma cells secrete antibodies.", "T helper cells release cytokines to activate other cells.", "", "Macrophages engulf pathogens and present antigens; they do not kill infected cells in this way."]),
        QUIZ("Why is the secondary response faster than the primary response?",
             ["Antibodies from the first response are still at the same level.", "Memory cells are present and respond rapidly.", "The pathogen is weaker the second time.", "Phagocytes make the antibodies."], 1,
             "Memory B and T cells are ready; no time is spent on selecting and building up a clone.",
             hint="What is left in the body after the first infection?",
             feedback=["Antibody levels fall after the first response.", "", "The pathogen has not changed.", "Only plasma cells make antibodies."]),
        PQ("Describe how a B lymphocyte produces antibodies after the first entry of a bacterium into the body.",
           "A B cell with a receptor that matches an antigen on the bacterium binds to it. The cell is activated by cytokines from a T helper cell. It divides by mitosis to form a clone of identical cells (clonal expansion). Most of these become plasma cells with much rough endoplasmic reticulum, which secrete large amounts of the antibody. Some become memory cells."),
        PQ("Explain the difference between the roles of B lymphocytes and T lymphocytes in immunity.",
           "B lymphocytes are responsible for humoral immunity: they differentiate into plasma cells that secrete antibodies in the blood and tissue fluid, and into memory B cells. T lymphocytes are responsible for cell-mediated immunity: T helper cells release cytokines that activate B cells and other cells; T cytotoxic cells kill infected cells; and T memory cells remain for later infections. B cells mature in the bone marrow and T cells in the thymus."),
        PQ("Explain how vaccination gives long-term protection against a disease, and why a booster dose may be given.",
           "The vaccine contains a harmless form of the antigen. It is recognised by B and T cells, and the primary response gives plasma cells, antibodies and memory cells, without the disease. If the real pathogen arrives, memory cells quickly give a secondary response, with a rapid, large production of antibodies. A booster dose boosts the secondary response and gives a higher and longer-lasting level of memory cells and antibody."),
        PQ("Explain why people with HIV infection are more likely to get other infections.",
           "HIV infects and destroys T helper cells. These cells release the cytokines that activate B cells and T cytotoxic cells, and macrophages. With fewer T helper cells, antibody production and killing of infected cells are reduced, so the immune system cannot control other pathogens or cancers."),
        SUM("Non-specific defences: barriers, phagocytosis, inflammation, fever and interferons. They act against any pathogen.",
            "B lymphocytes: humoral immunity. Selection, clonal expansion, plasma cells (antibodies) and memory cells. T helper cells activate; T cytotoxic cells kill infected cells.",
            "An antibody is a Y-shaped protein with variable regions that bind a specific antigen. The secondary response is faster and bigger than the primary one.",
            "Active immunity makes memory cells (infection or vaccination); passive immunity is short-lived. Herd immunity protects those who are not immune. HIV destroys T helper cells."),
    ],
))


# ------------------------------------------------------------------ 19. Examination: Paper 1
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: multiple-choice technique for Upper Sixth Biology",
    slug="bixu-paper1-multiple-choice-technique",
    minutes=22,
    summary="How to approach the 50 multiple-choice questions: reading stems, eliminating options, handling data and calculation questions, and managing time across the six Upper Sixth modules.",
    objectives=[
        "Describe the structure of Paper 1 and plan your time",
        "Use a systematic method to answer recall, application and data questions",
        "Eliminate wrong options by recognising the common misconceptions",
        "Avoid the typical traps: absolute words, near-identical options and unit errors",
    ],
    key_concepts=["Paper 1 structure", "Stem and options", "Elimination", "Distractors", "Data questions", "Time management"],
    blocks=[
        H("Introduction"),
        T("Paper 1 of A Level Biology (0710) is **50 multiple-choice questions**. Each question has a stem and four options, one correct. "
          "The Board's 2023 report says that the answer sheets are marked by the technical department, and that the paper tests a wide scope of the syllabus. "
          "In the Upper Sixth you must also remember the Lower Sixth work: the paper does not stop at this year's modules."),
        T("Our Paper 1 mock exam A uses 50 questions across all six Upper Sixth modules, in proportion to their number of topics, with a time limit of 90 minutes. "
          "That time limit is a **KKEVO practice setting**, not an official one. It gives you about 1.8 minutes per question."),
        H("A method for every question"),
        KEY("Five steps", "Do them fast.", cards=[
            ["1 Cover the options", "Read the stem and try to answer before you look at A to D. Options are written to tempt you."],
            ["2 Underline key words", "NOT, ONLY, FIRST, BEST, ALL, and units. Many wrong answers come from misreading."],
            ["3 Compare with the options", "If your own answer is there, check it against the others before choosing."],
            ["4 Eliminate", "Cross out options that are clearly false. Each wrong option is usually a real misconception."],
            ["5 Choose, move on", "If stuck after about two minutes, mark the question and return. Unless the paper says otherwise, answer every question."],
        ]),
        T("Each wrong option in this course has a reason written for it in the practice sets. When you review your mistakes, learn the reason: it is often the real misconception you must fix."),
        H("Types of question"),
        T("**Recall.** The question asks for a fact: which hormone causes the LH surge, which enzyme seals the sugar-phosphate backbone. The key is accurate knowledge and careful reading."),
        T("**Application.** You use a principle in a new situation. For example: a cross, a Hardy-Weinberg calculation, the effect of a mutation on a protein, the result of a night break in a short-day plant."),
        T("**Data and experiments.** You read a graph or table and choose the conclusion that the data support. Check axes, units and the direction of change; make sure the conclusion is stated by the data and not by your outside knowledge."),
        T("**Multiple statements.** You are given several statements and asked which are correct. Judge each statement on its own, then match your list with the options."),
        EX("Worked example 1: an application question", intro="Two plants AaBb are crossed. Genes A and B are on different chromosomes. What fraction of the offspring is expected to be aabb? (A: 1/16, B: 1/8, C: 1/4, D: 9/16)", steps=[
            S("Cover the options", text="Each parent makes ab gametes with probability 1/4. So aabb has probability 1/4 × 1/4 = 1/16."),
            S("Check", text="Equivalent: aa has probability 1/4, bb has probability 1/4, product 1/16. Answer A."),
            S("Why the others tempt", text="1/4 forgets that each parent makes ab gametes only one time in four. 9/16 is the A_B_ class. 1/8 comes from slipping 1/2 × 1/4."),
        ]),
        EX("Worked example 2: a data question", intro="A student measured the percentage change in mass of potato cylinders in sucrose solutions: 0.0 M, +10%; 0.2 M, +4%; 0.4 M, -4%; 0.6 M, -10% (invented). Which concentration is closest to the water potential of the potato cells? (A: 0.1 M, B: 0.2 M, C: 0.3 M, D: 0.4 M)", steps=[
            S("Idea", text="At the concentration with no change in mass, the water potential of the solution equals that of the cells."),
            S("Interpolate", text="Between 0.2 M (+4%) and 0.4 M (−4%) the change passes through zero half-way, at 0.3 M."),
            S("Answer", text="C. Options B and D are the nearest data points, but neither gives zero change."),
        ]),
        EX("Worked example 3: eliminating options", intro="Which statement about the placenta is correct? (A: Fetal and maternal blood mix freely. B: It secretes hCG, progesterone and oestrogen. C: It is formed only from the mother's tissue. D: It prevents all antibodies crossing.)", steps=[
            S("A", text="False. The bloodstreams are separate; exchange is across a thin barrier."),
            S("C", text="False. The placenta contains tissue of the embryo (chorion) and of the mother (endometrium)."),
            S("D", text="False. IgG antibodies cross the placenta and give passive immunity."),
            S("Answer", text="B is correct. The elimination of A, C and D confirms it."),
        ]),
        H("Common traps"),
        KEY("Traps in Paper 1", "Watch for them.", cards=[
            ["Absolute words", "'Always', 'never', 'all' and 'only' are usually wrong in biology, but not always. Test them."],
            ["Near-identical options", "Options that differ by one word (for example 'mitosis' or 'meiosis', 'anterior' or 'posterior', 'Pr' or 'Pfr') test careful reading."],
            ["Units and scale", "Micrometres, millimetres, per cent and fractions. Convert before comparing."],
            ["True but irrelevant", "An option can be a true biological fact but not answer the question asked."],
            ["Calculations", "Check the formula (for example, q² or q?), then check that the answer is a sensible size."],
        ]),
        T("**Time plan for 50 questions.** Do the first pass in about 60 to 65 minutes, answering every question you can, and marking those that need more time. Use the remaining time for the marked questions, then check any calculation. "
          "If you are not sure, choose the option left after eliminating two."),
        T("**Topics to revise from the Upper Sixth.** Respiration (ATP yield, location of each stage), homeostasis (feedback, kidney, hormones), nerves and muscle, plant growth regulators and reproduction, genetics (crosses, ratios, chi-squared, Hardy-Weinberg), and biotechnology and immunity. "
          "Plan a revision schedule that covers each module at least twice before the examination."),
        TIP("After each practice paper, sort your wrong answers into four groups: did not know, misread, calculation slip and careless. Each group has a different cure."),
        MISTAKE("Choosing the first true statement", "Read all four options. A second option may be more complete or may be the only one that answers the actual question."),
        MISTAKE("Changing a correct answer without a reason", "Change an answer only if you can name the fact or the step that you got wrong."),
        QUIZ("Why is it useful to cover the options and answer the stem first?",
             ["It is faster to guess.", "It stops the wrong options from steering your thinking.", "It is not allowed to look at the options.", "It makes the stem easier to read."], 1,
             "The distractors are designed to tempt; forming your own answer first lets you test it against the options.",
             hint="Think about the purpose of the distractors.",
             feedback=["It is not about guessing.", "", "You may of course read the options.", "The stem is not changed by covering the options."]),
        QUIZ("A stem reads: 'Which of the following is NOT a function of the placenta?' What is the best first step?",
             ["Choose the first option that is a function of the placenta.", "Underline NOT and look for the one false statement among the four.", "Choose the longest option.", "Skip the question; it is a trick."], 1,
             "NOT reverses the question. Three options will be true functions and one will be false; you must pick the false one.",
             hint="What does the word NOT change about the task?",
             feedback=["That would choose a true function, which is the opposite of what is asked.", "", "Length does not show correctness.", "It is an ordinary question; reading it carefully is enough."]),
        PQ("Explain how you would answer this question without looking at the options first: 'A short-day plant with a critical night length of 10 hours is exposed to 14 hours of light and 10 hours of dark with a flash of red light in the middle of the dark period. Does it flower?'",
           "The plant needs an uninterrupted dark period at least as long as the critical length. A red flash converts Pr to Pfr and splits the 10 hours into two periods of about 5 hours, both shorter than the critical length, so the plant does not flower. After working this out, find the option that says 'does not flower because the long night is broken'."),
        PQ("List three habits that improve a student's score in a 50-question multiple-choice paper.",
           "Read the stem carefully and underline words such as NOT and ONLY; eliminate wrong options by finding the misconception behind each; manage time by moving on from a hard question and returning to it; check calculations for units and size; never leave a question blank."),
        PQ("A student is asked which is the correct genotype ratio for Tt × Tt and chooses 3 : 1. Explain what is wrong with the answer and what the stem asked for.",
           "3 : 1 is the phenotype ratio. The question asked for the genotype ratio, which is 1 TT : 2 Tt : 1 tt. The mistake was reading 'genotype' as 'phenotype', a typical misreading that underlining key words would prevent."),
        SUM("Paper 1 is 50 multiple-choice questions across the whole syllabus. The KKEVO practice mock gives 90 minutes (a practice setting).",
            "Cover the options, underline key words, compare, eliminate, then choose. Do not leave blanks.",
            "Question types: recall, application, data and multiple statements. Data questions must be answered from the data.",
            "Watch absolute words, near-identical options, units and true-but-irrelevant options."),
    ],
))

# ------------------------------------------------------------------ 20. Examination: Paper 2
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: structured questions, essays and common errors",
    slug="bixu-paper2-theory-structured-essay",
    minutes=24,
    summary="How to answer the theory paper: reading command words, giving the function of a secretion rather than a gland, relating structure to function, writing genetic crosses correctly, and planning an essay.",
    objectives=[
        "Interpret command words such as state, describe, explain, compare and discuss",
        "Avoid the errors that the Board's 2023 report records in theory answers",
        "Set out genetics, biotechnology and physiology answers in the expected form",
        "Plan and write a short essay answer with a clear structure",
    ],
    key_concepts=["Command words", "Structure and function", "Genetic cross layout", "Annotated diagrams", "Essay plan", "Use of terms"],
    blocks=[
        H("Introduction"),
        T("Paper 2 is the theory paper, with structured and essay-type questions. The Board's 2023 report describes its questions as testing application, analysis and synthesis, and says that candidates' answers were weak where they needed to explain processes rather than recall facts. "
          "Candidates' scripts also showed that popular questions were not always well answered: choosing a question because it looks familiar is not the same as being able to answer it fully. "
          "This lesson shows how to turn your knowledge into the answers examiners reward."),
        T("Our Paper 2 practice paper A is a **KKEVO practice setting** with about 25 multiple-choice and numeric parts in numbered questions, with a time limit of 150 minutes. Essays cannot be marked automatically, so practise those on paper and compare with the model answers in the lessons."),
        H("Command words"),
        KEY("What the words ask for", "Answer what is asked, no more and no less.", cards=[
            ["State, name, give", "A short answer, a word or phrase. No explanation needed."],
            ["Describe", "Say what happens or what something looks like, in order. For a graph, describe the trend using figures."],
            ["Explain", "Give reasons: because. You must link cause and effect. 'Describe' without 'because' will not earn explanation marks."],
            ["Compare, distinguish", "Give similarities and/or differences, point by point (use both sides in each sentence)."],
            ["Discuss, evaluate", "Give arguments on both sides, with evidence, and a reasoned conclusion."],
            ["Outline", "The main points only, briefly."],
        ]),
        H("Errors that the Board's report records"),
        T("The report on the 2023 papers contains many patterns. These are paraphrased here, with the way to avoid each."),
        KEY("Six common errors", "Learn the corrected form.", cards=[
            ["Function given to the gland, not the secretion", "In a question on salivary glands and oxyntic cells, the answer must say what saliva and hydrochloric acid do. Write: 'saliva contains amylase, which digests starch', not 'the gland digests starch'."],
            ["Structure listed without function", "For 'how is the ileum suited to absorption', state each structure and link it: villi and microvilli give a large surface area; thin epithelium gives a short diffusion path; a capillary network and lacteal carry products away."],
            ["Wrong symbols in genetics", "Use two letters for two genes (G, g, S, s). Show linked genes on a line for each chromosome with the chiasma, not as unlinked pairs. Calculate recombinant frequency as a percentage of the **total**."],
            ["Process drawn, not explained", "A bare diagram of the nitrogen cycle or a food chain earns little. Annotate each arrow with the organism and the process, and name the ecosystem."],
            ["Defining the wrong thing", "When asked for the role of metamorphosis, explain **why** the stages exist (separate habitats and feeding), not just define it or list its types."],
            ["Missing conditions in industrial processes", "For fermentation, state the culture medium, the pH, the temperature, the oxygen supply and the carbon and nitrogen sources, and the stages from screening to downstream processing."],
        ]),
        T("The report also says that candidates found three topics hard: how information in DNA is used to make a protein and how its synthesis is regulated by enzyme induction and repression; the formation of a nerve impulse and the way the hypothalamus controls the pituitary; "
          "and the roles of the different B and T lymphocytes. These all appear in the Upper Sixth course, so treat them as priorities."),
        H("The layout of a genetics answer"),
        CODE("""Key:         T = tall (dominant), t = dwarf (recessive)
Parents:     tall (Tt)        x     dwarf (tt)
Gametes:     T    t                 t    t
Offspring:   Tt, Tt, tt, tt
Phenotypes:  2 tall : 2 dwarf  =  1 : 1""", "text", title="Layout"),
        T("Write the key first, then parents, gametes, the cross (a Punnett square or list), offspring genotypes, phenotypes and the ratio. A chi-squared answer has: null hypothesis, expected numbers, the calculation, degrees of freedom, the critical value and the conclusion."),
        H("Structured questions and essays"),
        T("In a structured question, each part has a mark. The number of marks and the number of lines show how many points are needed. Write one clear point per mark. "
          "In an essay, spend a few minutes on a plan: list the main headings, then the key terms for each. Begin with a short statement of the answer, keep to the title, use labelled diagrams, and end with a conclusion or summary."),
        EX("Worked example 1: a plan for a short essay", intro="Question: 'Describe how the information in DNA is used to make a protein, and explain how the production of an enzyme can be regulated.' Give a plan.", steps=[
            S("Part 1: protein synthesis", text="Transcription (RNA polymerase, template strand, mRNA), processing in eukaryotes, translation (ribosome, tRNA anticodon, codon, peptide bond), and the role of the genetic code."),
            S("Part 2: regulation", text="Operon: promoter, operator, repressor. Induction (lactose binds repressor, operon on). Repression (corepressor, e.g. tryptophan). Link: regulation controls transcription."),
            S("Close", text="A closing statement: gene expression is controlled so that proteins are made only when they are needed."),
        ]),
        EX("Worked example 2: a model answer in the right form", intro="Question: 'Explain how the structure of the ileum is suited to absorption.' Give a model answer.", steps=[
            S("Structure and function pairs", text="The wall has villi and the cells have microvilli, so the surface area is large. The epithelium is one cell thick, so the diffusion distance is short. Each villus has a network of blood capillaries and a lacteal that carry absorbed substances away, which keeps a steep concentration gradient. Many mitochondria in the epithelial cells give ATP for active transport of glucose and amino acids."),
            S("Why it earns marks", text="Every structure is linked to a function with a reason."),
        ]),
        EX("Worked example 3: explaining the nerve impulse and synapse (outline)", intro="Question: 'Outline the formation of a nerve impulse.' Give a model outline.", steps=[
            S("Resting potential", text="Sodium-potassium pumps move 3 Na+ out and 2 K+ in; K+ leaks out more than Na+ leaks in; the inside is about -70 mV."),
            S("Action potential", text="A stimulus opens sodium channels, Na+ enters, and the membrane depolarises; at the threshold more channels open (all-or-nothing). Then sodium channels close and potassium channels open, K+ leaves, and the membrane repolarises."),
            S("Link to a synapse", text="At the synapse the impulse causes calcium entry, vesicles release neurotransmitter, and it binds to receptors on the next neurone."),
        ]),
        TIP("Use the correct scientific terms: 'concentration gradient' not 'high to low'; 'water potential' not 'water concentration'; 'hydrolysis' for digestion; 'secretion' for what a gland releases."),
        MISTAKE("Writing everything you know on a topic", "Marks are for the points the question asks for. Extra, correct material does not make up for a missing point, and time spent on it is lost for other questions."),
        MISTAKE("Unlabelled or unannotated diagrams", "A diagram must be labelled and annotated with the function or the process. Use one diagram for a dissection that shows more than one system, as the report asks."),
        QUIZ("The question says 'Explain why the secondary immune response is faster than the primary response'. Which answer best fits the command word?",
             ["The secondary response is faster.", "Memory cells from the first infection divide and differentiate rapidly, so more plasma cells and antibodies are made sooner.", "There are more antibodies in the secondary response.", "Memory cells are present."], 1,
             "'Explain' needs a reason with 'because' logic.",
             hint="Look for the answer that has cause and effect.",
             feedback=["This restates the question.", "", "This describes, but does not give the reason.", "This is a fact that supports the reason but does not link it to the speed."]),
        QUIZ("What should an answer on the role of salivary glands in digestion say?",
             ["The glands digest starch.", "Saliva contains amylase, which digests starch, mucus lubricates food and lysozyme kills bacteria.", "The glands are found in the mouth.", "The glands break down proteins."], 1,
             "The functions belong to the secretion, which should be named with its contents and action.",
             hint="What does the gland release, and what does that do?",
             feedback=["A gland does not itself digest.", "", "That locates the glands and does not answer the question.", "Salivary amylase acts on starch, not proteins."]),
        PQ("Distinguish between 'describe' and 'explain' using the example of the lac operon.",
           "Describe: when lactose is present, the operon is switched on and the enzymes are made. Explain: lactose binds to the repressor and changes its shape, so it cannot bind to the operator. RNA polymerase can then transcribe the structural genes, so the enzymes needed to use lactose are made. The explanation gives the cause at each step."),
        PQ("A student answers a linkage question with the genotype AaBb x aabb and a 9 : 3 : 3 : 1 Punnett square. List three things that are wrong with this for a linked pair of genes.",
           "(1) Linked genes should be written on lines for each chromosome, AB / ab, not as AaBb, so that the arrangement is clear. (2) The gametes include parental and recombinant types in unequal numbers; a 16-box 9 : 3 : 3 : 1 square assumes independent assortment. (3) A test cross of linked genes gives two large and two small classes, and the recombinant frequency should be calculated as a percentage of the total offspring."),
        PQ("Plan, in six lines, a short essay on 'The role of hormones in the control of the menstrual cycle'.",
           "1 Introduction: cycle of about 28 days; ovary and uterus coordinated. 2 FSH: follicle growth, oestrogen. 3 Oestrogen: repairs the endometrium; negative feedback on FSH; at a high level, positive feedback causing the LH surge. 4 LH: ovulation and corpus luteum. 5 Progesterone: maintains the endometrium, inhibits FSH and LH. 6 If no pregnancy, the corpus luteum degenerates, hormones fall, menstruation; summary of feedback."),
        PQ("Explain why 'the ileum has villi' is not a complete answer to a question on how the ileum is suited to absorption.",
           "It states a structure but not its function. The answer should say that the villi (and microvilli) increase the surface area for absorption, then add other adaptations with their functions: thin walls give short diffusion distances, the capillaries and lacteal remove absorbed products to keep a steep gradient, and mitochondria supply ATP for active transport."),
        SUM("Paper 2 is the theory paper (structured and essay). Our practice paper is a KKEVO practice setting with auto-markable parts; practise essays on paper.",
            "Read command words: state, describe, explain (with reasons), compare, discuss (both sides).",
            "Give functions of secretions, link structures to functions, use two letters for two genes, annotate diagrams, give the conditions of industrial processes.",
            "Plan essays, keep to the question, use the correct scientific terms."),
    ],
))

# ------------------------------------------------------------------ 21. Examination: Paper 3
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: practical skills, planning, data and errors",
    slug="bixu-paper3-practical-skills",
    minutes=26,
    summary="Practical skills for the biology practical paper: planning a fair test, using apparatus, tables and graphs, drawing and magnification, errors, and writing conclusions, with advice for school laboratories with limited equipment.",
    objectives=[
        "Plan an investigation with independent, dependent and controlled variables and replicates",
        "Present results in a correct table and graph and calculate means and percentage change",
        "Calculate magnification and percentage uncertainty",
        "Write conclusions that are supported by the data, and report experiments in the past tense",
    ],
    key_concepts=["Variables and controls", "Replicates", "Tables and graphs", "Magnification", "Uncertainty", "Conclusion", "Biological drawing"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is the **practical paper**. It also includes a **school-based assessment (SBA)** mark, which comes from your practical workbook. "
          "The Board's 2023 report says that the practical groups include identifying and classifying specimens, making labelled drawings, dissection, and experiments such as the effect of solutions on strips of carrot and the action of catalase. "
          "It also says that candidates were often good at following a procedure, but weaker at explaining what the results show. "
          "Practical skills are not learned by reading, so use this lesson to guide practice in your school laboratory."),
        H("Planning an investigation"),
        KEY("A plan answers five questions", "Write each of these.", cards=[
            ["What is changed?", "The **independent variable**, with the values you will use (for example sucrose 0, 0.2, 0.4, 0.6 and 0.8 mol per dm3)."],
            ["What is measured?", "The **dependent variable**, with the method (for example change in mass of potato cylinders after 30 minutes)."],
            ["What is kept constant?", "The **controlled variables**: same size and type of tissue, same volume, same temperature, same time."],
            ["How is it made reliable?", "**Replicates** (at least three), take a mean, and a **control** (for example water alone)."],
            ["How is it safe?", "Name any hazard and how to reduce it (hot water bath, sharp blade, chemicals)."],
        ]),
        T("Write the plan as a numbered method in the **past tense and passive voice** if you are reporting an experiment already done ('The potato was cut into cylinders'), because the Board's examiners noted that candidates should be drilled in reporting experiments in this way. "
          "In a plan for the future, use the imperative or the future tense."),
        H("Apparatus and school laboratory realities"),
        T("Many schools have limited equipment: shared microscopes, one balance, few thermometers. You can still score well if you show good method and think about the quality of measurements. Some points:"),
        CODE("""Measurement        Suitable apparatus                  Smallest division / uncertainty
Mass               balance (0.1 g or 0.01 g)           half of smallest division
Volume             measuring cylinder, syringe,        1 cm3 cylinder: +/- 0.5 cm3
                   burette, pipette                    burette: +/- 0.05 cm3
Temperature        thermometer, water bath             1 degree C: +/- 0.5 degree C
Time               stopwatch or watch with seconds     +/- 0.5 s (plus reaction time)
Length             ruler, in mm                        +/- 0.5 mm
Cell size          eyepiece graticule and stage        calibrated with the stage micrometer
                   micrometer""", "text", title="Apparatus and uncertainty"),
        T("If equipment is not available, improvise carefully: a phone stopwatch for timing, a syringe for small volumes, a ruler for lengths, boiled and cooled water for a control, local plant material such as yam, cassava or fresh pawpaw (a source of protease) in place of imported material. "
          "State any change and say why it is valid."),
        H("Tables and graphs"),
        T("A results table has the independent variable in the **first column**, with headings that name the quantity and give the **units** (for example 'Sucrose concentration / mol dm-3'), no units in the body, and numbers with the same number of decimal places as the precision of the instrument. "
          "Include repeats and the mean. Do not leave out failed readings without comment."),
        T("A graph has the independent variable on the x-axis, the dependent variable on the y-axis, labelled axes with units, a scale that uses more than half the grid, points plotted accurately (small crosses or dots) and a line of best fit (a smooth curve or a straight line, not dot to dot) unless the data call for joining points. "
          "For a rate, draw a tangent. A bar chart is used when the independent variable is a category (for example different foods); a line graph when it is continuous."),
        EX("Worked example 1: percentage change in mass", intro="Potato cylinders started with mass 2.50 g in each solution. After 30 minutes the masses were: water 2.75 g; 0.2 M 2.60 g; 0.4 M 2.40 g; 0.6 M 2.25 g. Calculate the percentage change in mass for each, and estimate the concentration at which there is no change.", steps=[
            S("Formula", math=r"\text{percentage change} = \frac{\text{final} - \text{initial}}{\text{initial}} \times 100"),
            S("Values", text="Water: +10.0%. 0.2 M: +4.0%. 0.4 M: −4.0%. 0.6 M: −10.0%."),
            S("No change", text="Between 0.2 M (+4%) and 0.4 M (−4%), a straight line gives zero change at 0.3 M, so the potato cells have the same water potential as a 0.3 M sucrose solution."),
            S("Interpretation", text="In solutions weaker than 0.3 M, water enters the cells by osmosis and the mass rises; in stronger solutions, water leaves and the mass falls."),
        ]),
        EX("Worked example 2: magnification", intro="A student draws a plant cell. The drawing is 36 mm long. The actual cell is 60 micrometres long. Calculate the magnification. A scale bar of 20 mm represents 50 micrometres; what magnification does this show?", steps=[
            S("Convert units", math=r"60\ \mu\text{m} = 0.060\ \text{mm}"),
            S("Magnification", math=r"\text{magnification} = \frac{\text{drawing length}}{\text{actual length}} = \frac{36}{0.060} = 600"),
            S("Scale bar", math=r"\frac{20\ \text{mm}}{0.050\ \text{mm}} = 400", text="So a drawing with that scale bar has a magnification of ×400. Both lengths must be in the same unit."),
        ]),
        EX("Worked example 3: percentage uncertainty", intro="A 100 cm3 measuring cylinder is marked in 1 cm3 divisions. A student measures 40 cm3. A thermometer marked in 1 degree C divisions reads 20 degrees C. Compare the percentage uncertainty of the two readings.", steps=[
            S("Cylinder", math=r"\frac{0.5}{40} \times 100 = 1.25\%"),
            S("Thermometer", math=r"\frac{0.5}{20} \times 100 = 2.5\%", text="The thermometer reading has the greater percentage uncertainty."),
            S("Improvement", text="Use a larger volume or a more precise instrument (a burette for volume) or make a larger change in the measured quantity, to reduce the percentage uncertainty."),
        ]),
        H("Biological drawing, specimens and keys"),
        T("A drawing is made in pencil, large (at least half the page), with clear continuous lines, no shading, and a title that names the specimen and the view. Labels are in ruled lines that do not cross, written horizontally. "
          "**Annotate** (add notes) with the **structure and its function or adaptation**, because the Board's report records that candidates lost marks for stating functions only, without the structure. "
          "When dissecting an animal, display the systems asked for and draw them **in one diagram**."),
        T("In classification, write the phylum, class, common name and scientific name correctly; do not confuse the features of the class with those of the phylum. "
          "A **dichotomous key** uses a pair of contrasting, **visible external features** at each step, leading to a name or to the next pair. Do not use internal features or features you cannot see."),
        H("Errors, conclusions and evaluation"),
        T("**Random errors** make repeated readings scatter (for example, reaction time in stopwatch use). They are reduced by repeating and taking a mean. "
          "**Systematic errors** shift all readings the same way (for example, a balance that reads 0.2 g too much). They are reduced by calibrating or using a better method. "
          "A **conclusion** states what the results show, uses figures from the data, and gives a biological explanation. It should not go beyond the data. "
          "An **evaluation** states limitations (few replicates, temperature not controlled, imprecise apparatus) and an improvement for each."),
        T("**A short test for catalase.** Fresh liver or yam, cut into pieces, added to hydrogen peroxide produces oxygen bubbles (effervescence). To show that an **enzyme** is involved, boil a sample first: no effervescence with the boiled tissue shows that the enzyme is denatured. That control is the logic the Board looks for."),
        TIP("Always give a **numerical comparison** in a conclusion: 'The mass increased by 10% in water and decreased by 10% in 0.6 M sucrose' is better than 'the potato changed'."),
        MISTAKE("Joining points dot-to-dot on a graph of continuous data", "Draw a line or curve of best fit through the trend unless the question says to join the points."),
        MISTAKE("Putting units in every cell of the table", "Give the unit once in the column heading, not in each cell."),
        QUIZ("A student reports that the potato lost mass in a strong sucrose solution but forgets to say why. Which explanation is correct?",
             ["Water moved by osmosis from the cells, which have a higher water potential, into the solution, which has a lower water potential.", "Sucrose entered the cells and made them lighter.", "Water moved by active transport out of the cells.", "The solution evaporated."], 0,
             "Water moves by osmosis down the water potential gradient, from the cells to the more concentrated solution.",
             hint="Which has the higher water potential, the cell or a strong solution?",
             feedback=["", "Sucrose would increase the mass if it entered.", "Osmosis is passive; it needs no ATP.", "Evaporation is not involved."]),
        QUIZ("What is the magnification of a drawing 45 mm long of a specimen 0.15 mm long?",
             ["x 30", "x 300", "x 3000", "x 0.003"], 1,
             "45 / 0.15 = 300.",
             hint="Divide drawing length by actual length, in the same units.",
             feedback=["That would be 4.5 / 0.15.", "", "That would be 450 / 0.15.", "That inverts the ratio."]),
        PQ("Plan an investigation to find the effect of temperature on the activity of catalase in yam or liver, using school equipment.",
           "Independent variable: temperature (for example 10, 20, 30, 40, 50 and 60 degrees C, using water baths and a thermometer). Dependent variable: volume of oxygen collected in 60 seconds in a syringe, or height of froth in a tube. Controlled: same mass of tissue cut to the same size, same volume and concentration of hydrogen peroxide, same time, same pH or buffer. Replicates: three at each temperature and a mean. Control: boiled tissue. Safety: care with hot water and with hydrogen peroxide."),
        PQ("A student measured the diameter of a cell image as 24 mm and the actual size as 0.04 mm. Calculate the magnification and the actual size of a structure that measures 6 mm in the image.",
           "Magnification = 24 / 0.04 = 600. Actual size of the structure = 6 / 600 = 0.01 mm = 10 micrometres."),
        PQ("In an experiment the volume of oxygen in 60 seconds was 8, 9 and 7 cm3 at 30 degrees C. Calculate the mean and the rate, and suggest one source of error.",
           "Mean = (8 + 9 + 7) / 3 = 8.0 cm3. Rate = 8.0 / 60 = 0.13 cm3 per second (to two significant figures). Possible error: reaction time at the stopwatch, or loss of gas before the syringe was fixed. Repeat more times to reduce random error."),
        PQ("State two ways of improving the reliability and two ways of improving the validity of the investigation on potato cylinders.",
           "Reliability: repeat each concentration at least three times and calculate a mean; use more cylinders. Validity: control the variables, such as the same size, same potato and same time; use the same temperature; blot the cylinders in the same way before weighing; use a control in water."),
        SUM("Plan with independent, dependent and controlled variables, replicates, a control and safety.",
            "Tables: independent variable first, headings with units. Graphs: labelled axes, scale, best-fit line.",
            "Magnification = drawing length / actual length in the same units. Percentage uncertainty = half the smallest division divided by the reading × 100.",
            "Conclusions use figures and give a biological explanation; evaluations give limitations and improvements. Draw large, labelled and annotated diagrams."),
    ],
))
