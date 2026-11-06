"""Form 5 Biology: Reproduction, Growth & Genetics, Ecology & Community Health, and the Examination module.

16 topic lessons (bid-) and 3 examination lessons (bix-), one practice set each (see the practice file of the same name).
Content follows KKEVO's master curriculum blueprint and the Board's 2023 subject report for exam structure; it is not a
Board syllabus booklet. Genetics ratios and probabilities were checked by script (itertools).
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "form-5")

M_REP = "Reproduction, Growth & Genetics"
M_ECO = "Ecology & Community Health"
M_EXAM = "Examination"

LESSONS = []

# ------------------------------------------------------------------ 1. Cell division
LESSONS.append(lesson(
    module=M_REP,
    topic="Cell division",
    title="Cell division: mitosis and meiosis",
    slug="bid-mitosis-and-meiosis",
    minutes=24,
    summary="Chromosomes, the diploid and haploid numbers, the four stages of mitosis, why meiosis halves the chromosome number, and how the two kinds of division differ.",
    objectives=[
        "Define chromosome, diploid and haploid, and give the human numbers",
        "Describe the stages of mitosis and state where and why it happens",
        "Describe meiosis and explain how it makes gametes that differ from each other",
        "Compare mitosis and meiosis and work out chromosome numbers and cell numbers",
    ],
    key_concepts=["Chromosome", "Diploid and haploid", "Mitosis", "Meiosis", "Crossing over", "Gamete"],
    blocks=[
        H("Introduction"),
        T('A boy in Bafoussam grazes his knee while playing football. A week later the wound has closed and the '
             'skin is new. The same boy is also taller than he was last year. Both things happen because his cells '
             'keep dividing.\n\nThere are two kinds of cell division. **Mitosis** makes new body cells. **Meiosis** '
             'makes the sex cells (gametes) that pass on life to the next generation. First we need to know what '
             'is being shared out when a cell divides.'),
        H("Chromosomes and chromosome numbers"),
        D("A **chromosome** is a thread-like structure in the nucleus, made of DNA and protein. It carries genes. "
          "Chromosomes can only be seen clearly when a cell is dividing.", title="Definition: chromosome"),
        T("In body cells, chromosomes come in pairs. One chromosome of each pair came from the mother and one from the father. "
          "The two chromosomes of a pair are called **homologous chromosomes**. They carry the same genes in the same order."),
        D("A cell with two sets of chromosomes (pairs) is **diploid**, written $2n$. A cell with one set (one from each pair) is **haploid**, written $n$.",
          title="Diploid and haploid"),
        KEY("Human numbers", "Learn these two numbers.", cards=[
            ["Body cell (diploid)", "46 chromosomes, which is 23 pairs. Written 2n = 46."],
            ["Gamete (haploid)", "23 chromosomes: one from each pair. Written n = 23."],
        ]),
        T("When a sperm (n = 23) fuses with an egg (n = 23), the zygote has 23 + 23 = 46 chromosomes. The diploid number is restored."),
        H("Mitosis"),
        D("**Mitosis** is cell division in which one cell divides to form two daughter cells that have the same number of "
          "chromosomes as the parent cell and are genetically identical to it.", title="Definition: mitosis"),
        T("Before a cell divides it is in **interphase**. During interphase the cell grows and the DNA is copied. "
          "Each chromosome then consists of two identical **chromatids** joined at a point called the **centromere**. "
          "Then mitosis begins. It has four stages."),
        IMG("f5bi-d-mitosis-stages.svg", alt="Four cells showing prophase with chromosomes visible, metaphase with chromosomes on the equator, anaphase with chromatids at opposite poles and telophase with two nuclei forming",
            caption="Figure 1. The four stages of mitosis in a cell with four chromosomes."),
        KEY("The stages of mitosis", "Remember the order: PMAT.", cards=[
            ["Prophase", "Chromosomes shorten and become visible as two chromatids. The nuclear membrane breaks down. Spindle fibres form."],
            ["Metaphase", "The chromosomes line up across the middle (equator) of the cell, attached to spindle fibres."],
            ["Anaphase", "The centromeres split. The chromatids are pulled apart to opposite poles."],
            ["Telophase", "A nuclear membrane forms round each group of chromosomes. The cytoplasm divides, giving two daughter cells."],
        ]),
        T("**Where and why does mitosis happen?** It makes new cells for growth and to repair damaged tissue (such as a cut). "
          "It replaces worn-out cells (such as skin and red blood cells). In single-celled and some other organisms it is used for asexual reproduction. "
          "In plants it happens mostly in growing regions called meristems, for example the tips of roots and shoots."),
        H("Meiosis"),
        D("**Meiosis** is cell division in which one diploid cell divides twice to form four haploid cells (gametes in animals), "
          "each with half the chromosome number of the parent cell and each genetically different.", title="Definition: meiosis"),
        T("Meiosis happens in the sex organs: the testes and ovaries in animals, and the anthers and ovules in flowering plants. "
          "It has two divisions."),
        IMG("f5bi-d-chromosome-flow.svg", alt="Flow diagram: a cell with 4 chromosomes makes two identical cells by mitosis, or two cells with 2 chromosomes and then four cells with 2 chromosomes by meiosis",
            caption="Figure 2. Chromosome numbers after mitosis and after meiosis."),
        T('In **meiosis I**, the homologous chromosomes pair up. Pieces may be swapped between them (**crossing '
             'over**). Then the two chromosomes of each pair are pulled apart into two cells, each with half the '
             'chromosomes. In **meiosis II**, the chromatids of each chromosome are pulled apart, as in mitosis. '
             'The result is four cells, each haploid.\n\nMeiosis makes gametes **different from each other**. There '
             'are two reasons. Crossing over mixes genes between homologous chromosomes. And the pairs separate at '
             'random, so each gamete gets a different mixture of the chromosomes from the mother and father. This '
             'is the first source of variation.'),
        CODE("""Feature              Mitosis               Meiosis
Where                body cells            sex organs
Divisions            one                   two
Cells made           2                     4
Chromosome number    same as parent (2n)   half of parent (n)
Daughter cells       identical             different from each other
Used for             growth, repair,       making gametes
                     asexual reproduction""", "text", title="Mitosis compared with meiosis"),
        EX("Worked example 1: how many cells?", intro="One cell in a root tip divides by mitosis. Each daughter cell also divides, and this happens 5 times in all. How many cells are there at the end?", steps=[
            S("Each division doubles the number of cells", text="1 cell becomes 2, then 4, then 8, then 16, then 32."),
            S("Use the rule", math=r"\text{number of cells} = 2^n = 2^5"),
            S("Calculate", math=r"2^5 = 32 \text{ cells}"),
        ]),
        EX("Worked example 2: chromosome numbers", intro="A body cell of a certain animal has 8 chromosomes. How many chromosomes are in (a) a cell made by mitosis, (b) a gamete, (c) a zygote?", steps=[
            S("(a) Mitosis keeps the number", text="The new cell has 8 chromosomes, the same as the parent."),
            S("(b) Meiosis halves the number", math=r"8 \div 2 = 4 \text{ chromosomes}"),
            S("(c) Fertilization joins two gametes", math=r"4 + 4 = 8 \text{ chromosomes}"),
        ]),
        MISTAKE('Two common mistakes',
             'Saying mitosis makes gametes: Gametes are made by meiosis. Mitosis makes identical body cells. Write '
             'the chromosome numbers to show you understand: mitosis 2n to 2n, meiosis 2n to n. Spelling and '
             'mixing words: Chromosome (the whole thread), chromatid (one half of a copied chromosome) and '
             "centromere (the joining point) are different words. The Board's reports list wrong spellings of "
             'biological terms, so learn to spell each one.'),
        QUIZ("A cell with 14 chromosomes divides by meiosis. How many chromosomes are in each daughter cell?",
             ["14", "28", "7", "3.5"], 2,
             "Meiosis halves the chromosome number: 14 divided by 2 is 7.", hint="Meiosis makes haploid cells.",
             feedback=["14 is the number after mitosis, not meiosis.", "Doubling happens at fertilization, not in meiosis.", "", "Chromosome numbers are whole numbers: 7 is half of 14."]),
        QUIZ("During which stage of mitosis are chromatids pulled to opposite ends of the cell?",
             ["Prophase", "Metaphase", "Anaphase", "Telophase"], 2,
             "In anaphase the centromeres split and the chromatids move to the poles.", hint="'Ana' means apart.",
             feedback=["In prophase the chromosomes only become visible.", "In metaphase they line up on the equator.", "", "In telophase the nuclei re-form."]),
        TIP("Exam link: Paper 1 (multiple choice) often shows a cell in a stage of mitosis or asks for a chromosome number. Paper 2 essays may ask you to compare mitosis and meiosis or to describe a stage. Use the correct terms, and say 'identical' for mitosis and 'different' for meiosis.", title="Exam link"),
        PQ("Define mitosis and state two reasons why it is important.",
           "Mitosis is cell division in which a cell divides to give two daughter cells with the same number of chromosomes and genetically identical to the parent. It is important for growth and for repair or replacement of cells. (It also gives asexual reproduction in some organisms.)"),
        PQ("Describe what happens to the chromosomes in anaphase of mitosis.",
           "The centromeres divide. The two chromatids of each chromosome are pulled apart by the spindle fibres to opposite poles of the cell."),
        PQ("Give three differences between mitosis and meiosis.",
           "Mitosis has one division and meiosis has two. Mitosis makes two cells and meiosis makes four. Mitosis keeps the chromosome number (diploid) and meiosis halves it (haploid). Mitosis makes identical cells and meiosis makes cells that differ. Mitosis happens in body cells and meiosis in sex organs."),
        SUM("Chromosomes are in pairs in body cells (diploid, 46 in humans) and single in gametes (haploid, 23).",
            "Mitosis (PMAT) makes two identical diploid cells for growth, repair and replacement.",
            "Meiosis has two divisions and makes four different haploid cells in the sex organs.",
            "Crossing over and random separation of chromosomes cause variation.",
            "Fertilization joins two haploid gametes and restores the diploid number."),
    ],
))

# ------------------------------------------------------------------ 2. Asexual reproduction
LESSONS.append(lesson(
    module=M_REP,
    topic="Asexual reproduction and vegetative propagation",
    title="Asexual reproduction and vegetative propagation",
    slug="bid-asexual-reproduction-and-vegetative-propagation",
    minutes=22,
    summary="How one parent can make offspring without gametes (fission, budding, spores), and how farmers use runners, tubers, suckers, cuttings and grafting to propagate plants.",
    objectives=[
        "Define asexual reproduction and name its main forms",
        "Describe binary fission, budding and spore formation with examples",
        "Distinguish natural from artificial vegetative propagation using plants such as yam, plantain and cassava",
        "State advantages and disadvantages of asexual reproduction",
    ],
    key_concepts=["Asexual reproduction", "Clone", "Binary fission", "Budding", "Spores", "Vegetative propagation", "Cutting", "Grafting"],
    blocks=[
        H("Introduction"),
        T("A farmer near Kumba plants pieces of cassava stem in the ground. A few weeks later each piece has roots and shoots and "
          "is a new cassava plant. No seeds were used and no flowers were needed. This is **vegetative propagation**, a kind of **asexual reproduction**."),
        D("**Asexual reproduction** is reproduction that involves only one parent, with no gametes and no fertilization. The offspring are "
          "genetically identical to the parent.", title="Definition: asexual reproduction"),
        D("A **clone** is a group of organisms that are genetically identical because they came from one parent by asexual reproduction.", title="Definition: clone"),
        T("Asexual offspring are made by mitosis, so they have the same genes as the parent. They differ only if a mutation happens."),
        H("Asexual reproduction in lower organisms"),
        IMG("f5bi-d-fission-budding.svg", alt="Bacterium dividing into two by binary fission and a yeast cell producing a bud that breaks off",
            caption="Figure 1. Binary fission in a bacterium and budding in yeast."),
        KEY("Three forms to know", "Each is found in different organisms.", cards=[
            ["Binary fission", "The cell copies its DNA and splits into two equal cells. Examples: bacteria, Amoeba."],
            ["Budding", "A small outgrowth (bud) forms on the parent, grows, and breaks off as a new individual. Examples: yeast, Hydra."],
            ["Spore formation", "The parent makes many tiny spores. Each spore can grow into a new organism. Examples: Rhizopus (bread mould), mushrooms, ferns."],
        ]),
        T("Bacteria can divide as often as every 20 minutes or so in good conditions. This is why food left in the sun, or infected wounds, can become dangerous fast."),
        H("Vegetative propagation in flowering plants"),
        D("**Vegetative propagation** is the production of new plants from a part of the parent plant (a root, stem or leaf), without seeds or gametes.", title="Definition: vegetative propagation"),
        T("**Natural** vegetative propagation happens without help from humans. The plant has a special organ that can grow into a new plant."),
        KEY("Natural methods", "Organ, how it works, and an example.", cards=[
            ["Runner (stolon)", "A long side stem grows along the ground and forms roots and new shoots at nodes. Example: strawberry, sweet potato vine."],
            ["Rhizome", "An underground horizontal stem with buds. Example: ginger, spear grass."],
            ["Stem tuber", "A swollen underground stem storing food, with buds ('eyes'). Example: yam, Irish potato."],
            ["Bulb", "Fleshy leaf bases storing food around a short stem. Example: onion."],
            ["Corm", "A short, swollen underground stem. Example: cocoyam (check your textbook for local names)."],
            ["Sucker", "A new shoot that grows from the base or roots of the parent. Example: plantain and banana."],
        ]),
        T("**Artificial** vegetative propagation is done by people. A farmer chooses a good parent plant and copies it."),
        KEY("Artificial methods", "Used on farms and in nurseries.", cards=[
            ["Cutting", "A piece of stem, leaf or root is cut off and planted. It grows roots. Example: cassava stems, sugar cane."],
            ["Grafting", "A shoot (scion) from one plant is joined to the stem or root (stock) of another so that they grow as one plant. Example: citrus, mango, cocoa."],
            ["Budding (in plants)", "A bud from one plant is inserted under the bark of another. Example: rubber, citrus."],
            ["Layering", "A branch is bent to the soil and covered while still attached. It makes roots, then is cut off. Example: some fruit trees and shrubs."],
        ]),
        T("The yam farmer who cuts a tuber into pieces, each with an eye, and plants them is using artificial propagation with a natural organ."),
        H("Advantages and disadvantages"),
        CODE("""Advantages                          Disadvantages
One parent is enough                No variation: all clones
Fast; no need to find a mate        A disease can kill all the plants
Good qualities (high yield) kept    No new combinations of genes,
Plants grow faster than from seed   so little ability to adapt
Works where seeds do not form       Overcrowding near the parent""", "text", title="Asexual reproduction"),
        EX("Worked example: choose a method", intro="A cocoa farmer has one tree that gives very large pods. How can she get more trees with the same large pods? Give the method and one reason.", steps=[
            S("Choose a vegetative method", text="Grafting (or budding) a shoot from the good tree onto young rootstocks."),
            S("Explain why", text="The new plants are clones of the good tree, so they will have the same large pods. Seeds would give variable trees because seeds come from sexual reproduction."),
            S("Give a drawback", text="All the trees are genetically the same, so a disease could attack all of them."),
        ]),
        MISTAKE("Calling a tuber or a bulb a root", "A yam tuber and an onion bulb are underground parts of the stem system. A tuber is a swollen stem; a bulb is a short stem with fleshy leaf bases. Learn which plant part each is."),
        MISTAKE("Saying offspring from asexual reproduction are 'similar'", "Write 'genetically identical'. Mutation is the only reason a small difference could appear."),
        QUIZ("Which is an example of natural vegetative propagation?",
             ["Planting a cassava stem", "Grafting a mango shoot", "A strawberry runner rooting at a node", "Sowing maize seeds"], 2,
             "A runner is a stem that grows along the ground and roots by itself, without any help.", hint="'Natural' means the plant does it unaided.",
             feedback=["A cassava cutting is artificial: a person cuts and plants it.", "Grafting is done by a person.", "", "Seeds come from sexual reproduction."]),
        QUIZ("Why are plants grown from cuttings genetically identical to the parent?",
             ["Because they come from seeds", "Because they are made by mitosis from one parent", "Because they are made by meiosis", "Because pollination is not needed"], 1,
             "The cutting grows by mitosis, which copies the parent's genes exactly.", hint="Which cell division keeps the genes the same?",
             feedback=["Cuttings do not come from seeds.", "", "Meiosis makes different cells.", "That is true but does not explain why the genes are the same."]),
        TIP("Exam link: Paper 1 asks you to identify an organ (tuber, bulb, runner) or a method (fission, budding). Paper 2 may ask you to define asexual reproduction, give advantages and disadvantages, or describe how a farmer propagates a crop.", title="Exam link"),
        PQ("Define asexual reproduction and name three of its forms.",
           "Asexual reproduction is reproduction involving one parent only, with no gametes, giving offspring that are genetically identical to the parent. Forms are binary fission, budding, spore formation and vegetative propagation."),
        PQ("Describe how yeast reproduces by budding.",
           "A small bulge (bud) grows out of the parent yeast cell. The nucleus divides and one nucleus moves into the bud. The bud grows and then breaks off as a new yeast cell."),
        PQ("Give two advantages and two disadvantages of vegetative propagation for a farmer.",
           "Advantages: the plants keep the good qualities of the parent and they grow and mature faster than plants from seed. Disadvantages: there is no variation, so a disease can destroy all the plants, and the plants may crowd each other."),
        PQ("Name the part of the plant used and the method for propagating (a) yam, (b) plantain, (c) cassava.",
           "(a) Yam: a piece of stem tuber with an eye is planted. (b) Plantain: a sucker growing from the base is separated and planted. (c) Cassava: a cutting of the stem is planted."),
        SUM("Asexual reproduction uses one parent and makes genetically identical offspring (clones).",
            "Forms: binary fission, budding, spore formation and vegetative propagation.",
            "Natural vegetative organs: runners, rhizomes, tubers, bulbs, corms, suckers.",
            "Artificial methods: cuttings, grafting, budding and layering.",
            "It is fast and keeps good qualities, but there is no variation and disease can spread."),
    ],
))

# ------------------------------------------------------------------ 3. Flower structure and pollination
LESSONS.append(lesson(
    module=M_REP,
    topic="Sexual reproduction in flowering plants",
    title="Flower structure and pollination",
    slug="bid-flower-structure-and-pollination",
    minutes=22,
    summary="The parts of a flower and their jobs, how self- and cross-pollination differ, and how insect-pollinated and wind-pollinated flowers are adapted.",
    objectives=[
        "Name and state the function of the main parts of a flower",
        "Distinguish self-pollination from cross-pollination",
        "Compare insect-pollinated and wind-pollinated flowers",
        "Draw and label a flower in longitudinal section",
    ],
    key_concepts=["Sepal and petal", "Stamen", "Carpel", "Pollen grain", "Pollination", "Insect-pollinated", "Wind-pollinated"],
    blocks=[
        H("Introduction"),
        T("In a cocoa farm in the Centre Region, tiny flowers grow straight out of the trunk. Small midges visit them and carry pollen from one flower "
          "to another. Without this, there would be few pods and no chocolate. Flowers are the **reproductive organs** of flowering plants."),
        H("Parts of a flower"),
        IMG("f5bi-d-flower-ls.svg", alt="Longitudinal section of a flower labelling stigma, anther, style, ovary, ovule, filament, petal, sepal and receptacle",
            caption="Figure 1. A flower cut in half lengthways."),
        KEY("What each part does", "Learn the parts and their jobs.", cards=[
            ["Sepals", "Small, usually green. They protect the flower when it is a bud."],
            ["Petals", "Often large and coloured. They attract insects."],
            ["Stamen (male part)", "Has an anther, which makes pollen grains (male gametes inside), held up by a filament."],
            ["Carpel (female part)", "Has a stigma (receives pollen), a style (holds the stigma up) and an ovary containing one or more ovules."],
            ["Ovule", "Inside the ovary. It contains the female gamete (egg cell). After fertilization it becomes a seed."],
            ["Receptacle", "The tip of the flower stalk that holds all the flower parts."],
        ]),
        T("Some flowers have nectaries, which make a sweet liquid called **nectar** that attracts insects. A flower with both stamens and carpels is a bisexual flower."),
        H("Pollination"),
        D("**Pollination** is the transfer of pollen grains from an anther to a stigma of a flower of the same species.", title="Definition: pollination"),
        T("**Self-pollination** is the transfer of pollen from an anther to a stigma of the same flower or another flower on the same plant. "
          "**Cross-pollination** is the transfer of pollen to a flower on a different plant of the same species."),
        CODE("""                Self-pollination        Cross-pollination
Pollen goes to  same plant              different plant
Variation       little                  more
Needs agent     not always              yes (insect, wind, ...)
Disease         spreads to all          some plants may survive
Seedlings       less able to adapt      more able to adapt""", "text", title="Self- and cross-pollination"),
        T("Pollen is carried by agents such as insects, wind, water or small animals. Most flowers have ways of encouraging cross-pollination, "
          "for example when the anthers and stigmas ripen at different times."),
        H("Insect-pollinated and wind-pollinated flowers"),
        CODE("""Feature        Insect-pollinated          Wind-pollinated
Petals         large, bright, scented     small, dull or absent
Nectar         present                    none
Pollen         sticky or spiny, less      light, dry, smooth, plenty
Anthers        inside the flower          hang outside on long filaments
Stigma         small, sticky, inside      large, feathery, outside
Example        hibiscus, beans            maize, grasses""", "text", title="Two types of flower"),
        EX("Worked example 1: explain the adaptations", intro="Explain why the stigma of a grass flower is large and feathery.", steps=[
            S("State the job of the stigma", text="It must catch pollen that is carried by the wind."),
            S("Link structure to function", text="A large, feathery surface has a big area, so it has a better chance of catching the pollen grains blown past."),
        ]),
        EX("Worked example 2: model answer for a diagram question", intro="Draw and label a flower in longitudinal section. (State what to include.)", steps=[
            S("Draw the outline", text="Use a pencil, a clear outline, and no shading. Draw the receptacle at the base."),
            S("Add the female parts", text="Draw the ovary with ovules, then the style and the stigma."),
            S("Add the male parts and others", text="Draw the stamens with filament and anther, then the petals and sepals."),
            S("Label", text="Use straight label lines that touch the part. Write the title and the name of each part with correct spelling."),
        ]),
        MISTAKE("Mixing up the male and female parts", "Stamen = male = anther (makes pollen). Carpel = female = stigma, style and ovary. Learn the pairs together. The Board's reports note wrong spellings such as 'anta' for anther, 'stickma' for stigma and 'polline' for pollen."),
        MISTAKE("Confusing pollination with fertilization", "Pollination is the arrival of pollen on the stigma. Fertilization is the fusion of the male and female gametes. It happens later, in the ovule."),
        QUIZ("Which part of a flower makes pollen grains?",
             ["Stigma", "Ovary", "Anther", "Sepal"], 2,
             "The anther is the part of the stamen that makes pollen.", hint="It sits on top of a filament.",
             feedback=["The stigma receives pollen.", "The ovary contains the ovules.", "", "Sepals protect the bud."]),
        QUIZ("A flower has small green petals, long hanging anthers and a feathery stigma. How is it most likely pollinated?",
             ["By insects", "By wind", "By birds", "By itself only"], 1,
             "Small dull petals, hanging anthers and a large feathery stigma are signs of wind pollination.", hint="No bright petals or scent to attract insects.",
             feedback=["Insect-pollinated flowers have large, bright petals.", "", "Bird-pollinated flowers have bright petals and nectar.", "The long anthers and feathery stigma are for catching wind-blown pollen."]),
        TIP("Exam link: Paper 1 shows a flower diagram with letters and asks for a part, or a flower description and asks how it is pollinated. Paper 2 can ask you to compare insect- and wind-pollinated flowers.", title="Exam link"),
        PQ("Define pollination and state the difference between self-pollination and cross-pollination.",
           "Pollination is the transfer of pollen from an anther to a stigma of the same species. In self-pollination the pollen goes to a flower on the same plant. In cross-pollination it goes to a flower on a different plant."),
        PQ("State the functions of (a) the petals, (b) the stigma, (c) the ovule.",
           "(a) Petals attract insects (in insect-pollinated flowers). (b) The stigma receives pollen grains. (c) The ovule contains the female gamete and becomes a seed after fertilization."),
        PQ("Give three differences between an insect-pollinated flower and a wind-pollinated flower.",
           "Insect-pollinated flowers have large, bright, scented petals and nectar, sticky pollen and small stigmas inside the flower. Wind-pollinated flowers have small dull petals, no nectar, light dry pollen in large amounts, and hanging anthers and large feathery stigmas outside the flower."),
        PQ("Explain why cross-pollination is an advantage to a species.",
           "It mixes the genes from two different plants, so the offspring show more variation. Some may be better able to survive changes or disease, so the species can adapt more easily."),
        SUM("A flower has sepals, petals, stamens (anther and filament) and carpels (stigma, style, ovary with ovules).",
            "Pollination is the transfer of pollen from anther to stigma; it is not fertilization.",
            "Self-pollination uses one plant; cross-pollination uses two and gives more variation.",
            "Insect-pollinated flowers are bright and scented; wind-pollinated flowers have hanging anthers and feathery stigmas."),
    ],
))

# ------------------------------------------------------------------ 4. Fertilization, dispersal, germination
LESSONS.append(lesson(
    module=M_REP,
    topic="Sexual reproduction in flowering plants",
    title="Fertilization, dispersal and germination in flowering plants",
    slug="bid-fertilization-dispersal-and-germination",
    minutes=24,
    summary="How a pollen tube reaches the ovule and double fertilization happens, how the ovary becomes a fruit and the ovule a seed, how seeds are dispersed, and what a seed needs to germinate.",
    objectives=[
        "Describe fertilization in a flowering plant, including double fertilization",
        "State what the ovule and ovary become after fertilization",
        "Describe four methods of seed and fruit dispersal and the adaptations for each",
        "State the conditions needed for germination and interpret a germination experiment",
    ],
    key_concepts=["Pollen tube", "Double fertilization", "Fruit and seed", "Dispersal", "Germination", "Cotyledon", "Hypogeal and epigeal"],
    blocks=[
        H("Introduction"),
        T("A farmer in Dschang buys maize seed. The seed is dry and looks dead, but a few days after sowing in moist warm soil it sprouts. "
          "Where did the seed come from? It came from a flower that was pollinated and fertilized. This lesson follows the journey from pollen to seedling."),
        H("Fertilization"),
        T("When a pollen grain lands on a compatible stigma, it grows a **pollen tube**. The tube grows down through the style, guided by chemicals, "
          "and enters the ovary. It then enters an ovule through a small opening called the **micropyle**. The tube carries two male nuclei."),
        D("**Fertilization** is the fusion of a male gamete (nucleus) with a female gamete (the egg cell) to form a zygote.", title="Definition: fertilization"),
        D("**Double fertilization** is the process in flowering plants in which one male nucleus fuses with the egg cell to make the zygote (2n), and the "
          "second male nucleus fuses with two polar nuclei in the embryo sac to make the endosperm nucleus (3n).", title="Definition: double fertilization"),
        T("The zygote divides by mitosis and grows into the **embryo**. The endosperm becomes a food store in some seeds (for example maize). "
          "In others the food is stored in the cotyledons (for example beans)."),
        H("From flower to fruit and seed"),
        KEY("After fertilization", "Each part of the flower changes.", cards=[
            ["Ovule", "Becomes the seed."],
            ["Ovary", "Becomes the fruit."],
            ["Zygote", "Becomes the embryo inside the seed."],
            ["Ovary wall", "Becomes the fruit wall (pericarp)."],
            ["Petals, stamens, stigma and style", "Wither and fall off in most flowers."],
        ]),
        T("A mature seed has a protective coat (**testa**), a small hole (micropyle), an embryo with a **radicle** (young root) and a **plumule** (young shoot), "
          "and one or two seed leaves (**cotyledons**). Monocotyledons such as maize have one cotyledon and dicotyledons such as beans have two."),
        H("Dispersal of fruits and seeds"),
        D("**Dispersal** is the scattering of seeds or fruits away from the parent plant.", title="Definition: dispersal"),
        T("Dispersal reduces competition for water, light and nutrients between the offspring and the parent, and helps the species colonise new places."),
        KEY("Four methods", "Look at the adaptation to match each method.", cards=[
            ["Wind", "Light fruits or seeds with wings or hairs (parachutes). Example: silk cotton (kapok) seeds, some tree fruits with wings."],
            ["Animals", "Fleshy, brightly coloured, tasty fruits are eaten and the seeds pass out in the droppings. Or dry fruits with hooks stick to fur or clothing."],
            ["Water", "Fruits that float because they are light or have a waterproof, fibrous husk. Example: coconut."],
            ["Explosive (self-dispersal)", "A dry fruit dries and twists, then splits suddenly and throws the seeds out. Example: many bean and pea pods."],
        ]),
        H("Germination"),
        D("**Germination** is the growth of an embryo in a seed into a young plant (seedling) when the conditions are right.", title="Definition: germination"),
        KEY("Conditions needed", "Three things are needed.", cards=[
            ["Water", "Softens the testa, activates enzymes and lets the stored food be digested and moved."],
            ["Oxygen", "For aerobic respiration, which releases energy for growth."],
            ["A suitable temperature", "Warm enough for enzymes to work well (not too cold, not too hot)."],
        ]),
        T("Light is not needed by most seeds, because the food store supplies everything until the first leaves open. "
          "During germination, enzymes (for example amylase) digest the stored starch into sugar, which is used for respiration and to build new cells."),
        IMG("f5bi-d-germination-tubes.svg", alt="Four test tubes A to D with seeds on moist or dry cotton wool, under boiled water covered with oil, or in a fridge",
            caption="Figure 1. A germination experiment. Each tube differs from tube A in one condition only."),
        T("In **epigeal** germination (for example the common bean), the cotyledons are carried above the ground. In **hypogeal** germination (for example maize), the cotyledons stay below the ground. Textbooks differ on which examples they use, so check yours."),
        IMG("f5bi-d-germination-dry-mass.svg", alt="Graph of the dry mass of a germinating seedling, falling for about one week and then rising",
            caption="Figure 2. The dry mass of a seedling falls first, then rises."),
        T("Look at Figure 2. At first the seedling cannot make food, so it uses the food store in respiration. Its **dry mass** falls. "
          "When the first green leaves open, photosynthesis makes new food and the dry mass rises. (Fresh mass rises from the start because the seed takes in water, so dry mass is the better measure.)"),
        EX("Worked example 1: read the experiment", intro="Use Figure 1. In which tube do you expect the seeds to germinate? Explain why the other tubes do not.", steps=[
            S("Find the tube with all three conditions", text="Tube A has water (moist cotton wool), air and warmth (25 degrees Celsius). Seeds germinate."),
            S("Tube B", text="No water. Germination needs water."),
            S("Tube C", text="Boiled water holds no dissolved oxygen and the oil stops air entering. No oxygen."),
            S("Tube D", text="Too cold for enzymes to work. The seeds do not germinate (or only very slowly)."),
        ]),
        EX("Worked example 2: link the seed to the flower", intro="A mango flower is pollinated and fertilized. Name the part of the flower that becomes (a) the fruit, (b) the seed.", steps=[
            S("(a) Fruit", text="The ovary becomes the fruit."),
            S("(b) Seed", text="The ovule becomes the seed."),
        ]),
        MISTAKE('Two common mistakes',
             "Saying 'the seed needs sunlight to germinate': Most seeds need only water, oxygen and warmth. Light "
             'is needed later, by the seedling, for photosynthesis. Controlling too many things in an experiment: '
             'A fair test changes one factor and keeps the others the same. In Figure 1 each tube changes one '
             'condition from tube A.'),
        QUIZ("What does the ovule become after fertilization?",
             ["The fruit", "The seed", "The embryo", "The cotyledon"], 1,
             "The ovule becomes the seed. The ovary becomes the fruit.", hint="Which part contains the egg?",
             feedback=["The ovary becomes the fruit.", "", "The zygote becomes the embryo inside the seed.", "A cotyledon is a seed leaf inside the seed."]),
        QUIZ("Why does the dry mass of a germinating seedling fall at first?",
             ["It loses water", "It uses its food store in respiration before it can photosynthesise", "Its roots die", "The leaves fall off"], 1,
             "The seedling respires the food store to get energy. It cannot photosynthesise until it has leaves.", hint="Dry mass does not include water.",
             feedback=["Dry mass does not include water.", "", "The roots grow.", "There are no leaves yet."]),
        TIP("Exam link: Paper 1 often has a germination experiment (situations and experiments) or a dispersal question. Paper 2 can ask you to describe fertilization, dispersal methods or the conditions for germination.", title="Exam link"),
        PQ("Describe how fertilization takes place in a flowering plant.",
           "A pollen grain lands on the stigma and grows a pollen tube down the style to the ovule, entering through the micropyle. The tube carries two male nuclei. One fuses with the egg cell to form the zygote. The other fuses with the polar nuclei to form the endosperm. This is double fertilization."),
        PQ("State two ways in which a fruit is adapted for dispersal by wind and two for dispersal by animals.",
           "Wind: it is light and has wings or hairs. Animals: it is fleshy, brightly coloured and tasty so that the seeds are eaten and passed out, or it has hooks that cling to fur."),
        PQ("Why is it an advantage for seeds to be dispersed?",
           "The young plants do not compete with the parent or with each other for water, light and nutrients. The species can also spread to new places."),
        SUM("A pollen tube carries two male nuclei into the ovule. In double fertilization one makes the zygote and the other the endosperm.",
            "The ovule becomes the seed and the ovary becomes the fruit.",
            "Seeds are dispersed by wind, animals, water or explosive pods to reduce competition.",
            "Germination needs water, oxygen and warmth, but not light.",
            "Dry mass falls at first as the food store is used, then rises when photosynthesis starts."),
    ],
))

# ------------------------------------------------------------------ 5. Human reproductive systems
LESSONS.append(lesson(
    module=M_REP,
    topic="Human reproduction",
    title="The human reproductive systems and the menstrual cycle",
    slug="bid-human-reproductive-systems-and-menstrual-cycle",
    minutes=24,
    summary="The parts of the male and female reproductive systems, how sperm and eggs are made and adapted, and what happens in the menstrual cycle.",
    objectives=[
        "Name the parts of the male and female reproductive systems and state their functions",
        "Describe how sperm and egg cells are adapted to their functions",
        "Describe the main events of the menstrual cycle and the hormones involved",
        "Interpret a graph of the uterus lining over one cycle",
    ],
    key_concepts=["Testis", "Ovary", "Gamete", "Sperm and egg", "Ovulation", "Menstrual cycle", "Oestrogen and progesterone"],
    blocks=[
        H("Introduction"),
        T("At a health talk in a school in Bertoua, a nurse explains that the human body has special organs to make new life. "
          "Understanding these organs helps young people to look after their health and to make informed choices as adults. "
          "In this lesson we use correct scientific names and keep the language simple."),
        H("The male reproductive system"),
        IMG("f5bi-d-male-system.svg", alt="Male reproductive system labelling bladder, seminal vesicle, prostate gland, urethra, sperm duct, testis, epididymis and scrotum",
            caption="Figure 1. The male reproductive system (front view, simplified)."),
        KEY("Parts and functions", "Follow the path of a sperm.", cards=[
            ["Testis (plural testes)", "Makes sperm (and the hormone testosterone). Hangs in the scrotum, which is slightly cooler than the body."],
            ["Epididymis", "A coiled tube on each testis where sperm are stored and mature."],
            ["Sperm duct", "Carries sperm from the epididymis to the urethra."],
            ["Seminal vesicle and prostate gland", "Add a fluid that feeds and carries the sperm. Sperm plus fluid is called semen."],
            ["Urethra", "A tube through the penis that carries semen (and urine, but never at the same time)."],
            ["Penis", "Places semen inside the vagina during sexual intercourse."],
        ]),
        H("The female reproductive system"),
        IMG("f5bi-d-female-system.svg", alt="Female reproductive system labelling ovary, oviduct, uterus, cervix and vagina",
            caption="Figure 2. The female reproductive system (front view, simplified)."),
        KEY("Parts and functions", "Follow the path of an egg.", cards=[
            ["Ovary", "Makes egg cells (ova) and the hormones oestrogen and progesterone. There are two."],
            ["Oviduct (fallopian tube)", "Catches the egg and carries it to the uterus. Fertilization usually happens here."],
            ["Uterus (womb)", "A muscular organ with a soft lining where the embryo implants and the fetus grows."],
            ["Cervix", "A ring of muscle at the lower end of the uterus. It keeps the fetus in during pregnancy."],
            ["Vagina", "Receives the penis and semen. It is also the birth canal."],
        ]),
        H("Gametes: sperm and egg"),
        D("A **gamete** is a sex cell. It is haploid, made by meiosis, and fuses with another gamete at fertilization.", title="Definition: gamete"),
        KEY("How they are adapted", "Structure matches function.", cards=[
            ["Sperm", "Small, with a tail to swim. Many mitochondria in the middle section release energy. The head holds the nucleus and an acrosome with enzymes that digest the egg's outer layer. Millions are made."],
            ["Egg (ovum)", "Large, with a food store in the cytoplasm for the early embryo. A jelly-like coat. It cannot move by itself, so it is carried along the oviduct. One is released at a time."],
        ]),
        T("Sperm are made all the time from puberty onward. In a female, each month one egg (usually) is released from an ovary. This is called **ovulation**."),
        H("The menstrual cycle"),
        T("The **menstrual cycle** is a series of changes in the ovary and uterus that repeats about every 28 days. Cycles vary from person to person. "
          "Four hormones control it. FSH (from the pituitary gland) makes a follicle in the ovary grow. The follicle makes **oestrogen**. "
          "LH (also from the pituitary) triggers ovulation. The empty follicle becomes the corpus luteum, which makes **progesterone**."),
        IMG("f5bi-d-menstrual-lining.svg", alt="Graph of uterus lining thickness over 28 days: thin at the period on days 1 to 5, rising steadily to day 24 and falling by day 28",
            caption="Figure 3. The uterus lining over one cycle."),
        KEY("The main events", "Days are approximate.", cards=[
            ["Days 1 to 5: menstruation", "The lining breaks down and leaves the body through the vagina with some blood (a period)."],
            ["Days 5 to 13", "A follicle grows. Oestrogen makes the lining rebuild and thicken."],
            ["About day 14: ovulation", "LH triggers the release of an egg from the ovary into the oviduct."],
            ["Days 15 to 28", "Progesterone keeps the lining thick and full of blood vessels, ready for an embryo."],
            ["If the egg is not fertilized", "The corpus luteum breaks down, progesterone falls, the lining breaks down and a new period starts."],
        ]),
        T("If the egg is fertilized and implants, the corpus luteum and then the placenta keep making progesterone, so the lining is kept and there is no period."),
        EX("Worked example 1: read the graph", intro="Use Figure 3. On which day is the lining at its thickest, and what is happening in the ovary around day 14?", steps=[
            S("Find the highest point", text="The peak is at about day 24."),
            S("Link day 14 to the ovary", text="At about day 14 ovulation takes place: an egg is released from the ovary."),
        ]),
        EX("Worked example 2: follow the path", intro="Write the path taken by a sperm from where it is made to where it fertilizes an egg.", steps=[
            S("From the testis", text="Testis, then epididymis, then sperm duct."),
            S("Into the female", text="Urethra, then vagina, through the cervix and uterus."),
            S("To the egg", text="Up the oviduct, where fertilization takes place."),
        ]),
        MISTAKE("Mixing up the oviduct and the ureter or urethra", "The oviduct carries eggs. The ureter carries urine from the kidney. The urethra carries urine (and semen in males). Spell each carefully."),
        MISTAKE("Saying ovulation is the same as menstruation", "Ovulation is the release of an egg (about day 14). Menstruation is the loss of the uterus lining (days 1 to 5)."),
        QUIZ("Where in the female system does fertilization usually happen?",
             ["Uterus", "Ovary", "Oviduct", "Vagina"], 2,
             "The egg is met by sperm in the oviduct.", hint="The egg travels along this tube after ovulation.",
             feedback=["The embryo implants in the uterus, but fertilization comes earlier.", "The ovary makes and releases the egg.", "", "The vagina receives the semen."]),
        QUIZ("Which feature of a sperm cell helps it to swim?",
             ["The acrosome", "A large food store", "A tail with many mitochondria nearby", "A jelly coat"], 2,
             "The tail moves the sperm along, and mitochondria release the energy it needs.", hint="Think of movement and energy.",
             feedback=["The acrosome holds enzymes to enter the egg.", "A large food store belongs to the egg.", "", "A jelly coat belongs to the egg."]),
        TIP("Exam link: Paper 1 shows the male or female system with letters and asks you to name a part, or shows the lining graph. Paper 2 can ask you to describe the cycle or compare sperm and egg.", title="Exam link"),
        PQ("State the functions of (a) the testis, (b) the oviduct, (c) the uterus.",
           "(a) The testis makes sperm and testosterone. (b) The oviduct carries the egg to the uterus and is where fertilization happens. (c) The uterus holds the embryo in its lining and the fetus grows there."),
        PQ("Give three ways in which a sperm cell is adapted for its function.",
           "It has a tail to swim. It has many mitochondria to release energy. It has an acrosome with enzymes to break through the egg's outer layer. It is small and made in very large numbers."),
        PQ("Describe what happens in the menstrual cycle on days 1 to 5 and around day 14.",
           "On days 1 to 5 the uterus lining breaks down and leaves the body (menstruation). Around day 14 an egg is released from the ovary (ovulation)."),
        PQ("Explain why there is no menstruation during pregnancy.",
           "After implantation the corpus luteum, and later the placenta, keep making progesterone. This keeps the lining of the uterus thick, so it does not break down."),
        SUM("Male system: testis, epididymis, sperm duct, seminal vesicle, prostate gland, urethra, penis.",
            "Female system: ovary, oviduct, uterus, cervix, vagina.",
            "Sperm have a tail, mitochondria and an acrosome; the egg is large with a food store.",
            "The cycle lasts about 28 days: period, lining rebuilds, ovulation near day 14, lining kept thick or lost."),
    ],
))

# ------------------------------------------------------------------ 6. Fertilization, pregnancy, birth, contraception
LESSONS.append(lesson(
    module=M_REP,
    topic="Human reproduction",
    title="Fertilization, pregnancy, birth and contraception",
    slug="bid-pregnancy-birth-and-contraception",
    minutes=23,
    summary="How fertilization and implantation lead to an embryo, the role of the placenta, how birth happens, and the main methods of contraception and how they work.",
    objectives=[
        "Describe fertilization, early development and implantation",
        "Explain the functions of the placenta, umbilical cord and amniotic fluid",
        "Outline the stages of birth",
        "Describe the main methods of contraception and how each works",
    ],
    key_concepts=["Fertilization", "Implantation", "Placenta", "Umbilical cord", "Amnion", "Gestation", "Contraception"],
    blocks=[
        H("Introduction"),
        T("At a clinic in Limbe, a mother attends an antenatal visit. The nurse checks her blood pressure and explains why good food, rest and "
          "clean water matter during pregnancy. Everything the baby needs, it gets through the mother. How does that work?"),
        H("From fertilization to implantation"),
        T('**Fertilization** happens in the oviduct. The head of one sperm enters the egg and the two nuclei '
             "fuse. The zygote (2n = 46) is formed. At once the egg's outer layer changes so that no other sperm "
             'can enter.\n\nThe zygote divides by mitosis as it moves down the oviduct, forming a ball of cells '
             'called an **embryo**. About a week after fertilization the embryo reaches the uterus and sinks into '
             'the soft lining. This is **implantation**. If implantation does not happen, there is no pregnancy.'),
        D("**Gestation** (pregnancy) is the time from fertilization to birth, about 9 months (about 40 weeks from the last period).", title="Definition: gestation"),
        D("A **fetus** is the name given to the developing baby after the first weeks, when the main organs have formed.", title="Definition: fetus"),
        H("Protection and feeding of the fetus"),
        IMG("f5bi-d-placenta.svg", alt="A fetus inside the uterus joined to the placenta by the umbilical cord and surrounded by amniotic fluid and the amnion",
            caption="Figure 1. The fetus, placenta, umbilical cord and amniotic fluid."),
        KEY("Structures and jobs", "Each protects or feeds the fetus.", cards=[
            ["Placenta", "A disc of tissue on the uterus wall. The mother's blood and the fetus's blood flow very close together but do not mix. Food, oxygen and antibodies pass to the fetus; carbon dioxide and urea pass to the mother. It also makes progesterone."],
            ["Umbilical cord", "Joins the fetus to the placenta. It has an umbilical vein (carries oxygen- and food-rich blood to the fetus) and umbilical arteries (carry waste blood away)."],
            ["Amnion and amniotic fluid", "The amnion is a bag around the fetus filled with amniotic fluid. The fluid cushions against knocks, keeps the temperature steady and lets the fetus move."],
        ]),
        T("The placenta has a very large surface area and a thin barrier. This lets substances diffuse across quickly. It is not a perfect filter: "
          "alcohol, nicotine, some drugs and some pathogens (for example HIV and the rubella virus) can cross it. This is why a pregnant woman should avoid alcohol and tobacco and should attend antenatal clinics."),
        H("Birth"),
        KEY("Stages of birth", "Labour has three stages.", cards=[
            ["1. Contractions", "The muscle of the uterus wall contracts. The cervix widens. The amnion breaks and the amniotic fluid flows out (the waters break)."],
            ["2. Delivery", "Strong contractions push the baby out through the cervix and vagina. The umbilical cord is clamped and cut."],
            ["3. Afterbirth", "The placenta separates from the uterus wall and is pushed out."],
        ]),
        T("After birth, breast milk gives the baby food and antibodies. The first milk, colostrum, is especially rich in antibodies. "
          "Health workers advise that babies are breastfed (with the exceptions that a health worker will explain, for example when the mother is HIV positive and needs special advice)."),
        H("Contraception"),
        D("**Contraception** is the prevention of pregnancy by stopping fertilization or implantation.", title="Definition: contraception"),
        T("People use contraception to space their children and to plan their families. It is a personal and family decision. Health centres give advice and many methods are available."),
        KEY("Main methods", "Group them by how they work.", cards=[
            ["Barrier methods", "A condom (male or female) stops sperm reaching the egg. Condoms also protect against sexually transmitted infections, including HIV."],
            ["Hormonal methods", "The pill, implants or injections contain hormones that stop ovulation or thicken mucus at the cervix."],
            ["Intra-uterine device (IUD)", "A small device placed in the uterus by a trained health worker. It stops fertilization or implantation."],
            ["Natural methods", "Avoiding intercourse around ovulation (the calendar method). Less reliable because cycles vary."],
            ["Surgical methods", "Vasectomy (cutting the sperm ducts) or female sterilization (blocking the oviducts). Intended to be permanent."],
        ]),
        TIP("Only a condom protects against both pregnancy and sexually transmitted infections. Abstinence (not having sex) is also a method that is fully effective.", title="Good to know"),
        EX("Worked example 1: explain the placenta", intro="Explain how the placenta is adapted for exchange between mother and fetus.", steps=[
            S("Large surface area", text="The tissue is folded into many finger-like projections (villi), which gives a large area for diffusion."),
            S("Thin barrier", text="Only a few cells separate the blood supplies, so substances diffuse over a short distance."),
            S("Good blood supply", text="Many blood vessels bring a constant supply of oxygen and food and take away waste."),
        ]),
        EX("Worked example 2: describe a contraception method", intro="Explain how a condom works and give one advantage over the pill.", steps=[
            S("How it works", text="It is a barrier. It catches semen, so sperm cannot enter the vagina and reach the egg."),
            S("Advantage", text="It also protects against sexually transmitted infections, which the pill does not."),
        ]),
        MISTAKE("Saying the mother's blood flows into the fetus", "The two blood supplies do not mix. Substances pass across the placenta by diffusion and other transport. This avoids problems with different blood groups and high blood pressure."),
        MISTAKE("Saying the umbilical artery carries oxygen to the fetus", "In the cord, the vein brings oxygen-rich blood to the fetus. The arteries carry blood poor in oxygen away from the fetus."),
        QUIZ("Which of these is NOT a function of the placenta?",
             ["Passing oxygen to the fetus", "Passing urea to the mother's blood", "Making the baby's blood cells", "Making progesterone"], 2,
             "Blood cells of the fetus are made in the fetus's own tissues (liver, then bone marrow). The placenta exchanges substances and makes progesterone.", hint="Look for a job the placenta does not do.",
             feedback=["The placenta does pass oxygen to the fetus.", "Urea passes from the fetus to the mother.", "", "The placenta does make progesterone."]),
        QUIZ("Which method of contraception also protects against HIV?",
             ["The pill", "A condom", "Vasectomy", "The calendar method"], 1,
             "A condom is a barrier that prevents contact with infected body fluids.", hint="Look for a barrier method.",
             feedback=["The pill stops ovulation but gives no barrier.", "", "Vasectomy stops sperm but does not stop infections.", "The calendar method does not protect against infections."]),
        TIP("Exam link: Paper 1 may show a diagram of the fetus and ask for a part's function. Paper 2 can ask about the placenta, birth or the types of contraception. Use correct terms and describe how each method works.", title="Exam link"),
        PQ("Describe what happens between fertilization and implantation.",
           "The zygote divides by mitosis as it travels down the oviduct and forms a ball of cells (the embryo). About a week later it reaches the uterus and embeds in the soft lining."),
        PQ("State the functions of (a) the amniotic fluid, (b) the umbilical cord.",
           "(a) The amniotic fluid cushions and protects the fetus from shock and keeps the temperature steady. (b) The umbilical cord connects the fetus to the placenta and carries blood to and from it."),
        PQ("Explain why a pregnant woman should not smoke or drink alcohol.",
           "Harmful substances can pass across the placenta into the fetus's blood. They can damage the fetus and slow its growth."),
        PQ("Describe three methods of contraception and say how each works.",
           "A condom is a barrier that stops sperm reaching the egg. The pill contains hormones that stop ovulation. An IUD placed in the uterus prevents fertilization or implantation. (A vasectomy cuts the sperm ducts so that sperm cannot reach the semen.)"),
        SUM("Fertilization happens in the oviduct; the embryo implants in the uterus lining about a week later.",
            "The placenta exchanges food, oxygen and waste; mother's and fetus's blood do not mix.",
            "The amnion and fluid protect the fetus; the umbilical cord links it to the placenta.",
            "Birth: contractions and waters break, delivery, afterbirth.",
            "Contraception prevents pregnancy by barriers, hormones, devices, natural or surgical methods."),
    ],
))

# ------------------------------------------------------------------ 7. DNA and monohybrid inheritance
LESSONS.append(lesson(
    module=M_REP,
    topic="DNA and inheritance",
    title="DNA, genes and monohybrid inheritance",
    slug="bid-dna-genes-and-monohybrid-inheritance",
    minutes=25,
    summary="The structure of DNA, what genes and alleles are, the vocabulary of genetics, and how to work out a monohybrid cross with a Punnett square.",
    objectives=[
        "Describe the structure of DNA and the base-pairing rule",
        "Define gene, allele, genotype, phenotype, dominant, recessive, homozygous and heterozygous",
        "Carry out a monohybrid cross with a Punnett square and state the ratios and probabilities",
        "Use correct symbols and explain Mendel's results",
    ],
    key_concepts=["DNA", "Gene", "Allele", "Genotype and phenotype", "Dominant and recessive", "Punnett square", "Monohybrid cross"],
    blocks=[
        H("Introduction"),
        T("A family in Garoua sees that the first child is tall and the second is short, though both parents are tall. "
          "People ask how this can happen. The answer is in the instructions that parents pass on in their gametes. Those instructions are stored in **DNA**."),
        H("DNA and genes"),
        IMG("f5bi-d-dna-structure.svg", alt="A double helix of DNA with two backbones joined by base pairs, with the rule that A pairs with T and C pairs with G",
            caption="Figure 1. A short length of the DNA double helix."),
        D("**DNA** (deoxyribonucleic acid) is the molecule that stores genetic information. It is a double helix (a twisted ladder) made of two strands. "
          "Each strand has a backbone of sugar and phosphate units and a row of bases. The bases are adenine (A), thymine (T), cytosine (C) and guanine (G).", title="Definition: DNA"),
        KEY("The base-pairing rule", "This rule is always true.", cards=[
            ["A pairs with T", "Adenine joins thymine."],
            ["C pairs with G", "Cytosine joins guanine."],
        ]),
        T("The order of the bases is a code. If one strand reads A T T G C, the other strand reads T A A C G. "
          "When a cell divides, the strands separate and each is used as a pattern to build a new partner strand. Two identical molecules of DNA are made."),
        D("A **gene** is a length of DNA that codes for one protein, and so controls a characteristic (for example the shape of a seed).", title="Definition: gene"),
        T("A chromosome is one very long DNA molecule wound up with protein. A human cell has 23 pairs of chromosomes (46 in all)."),
        H("Genetics vocabulary"),
        D("An **allele** is one of the different forms of the same gene (for example the allele for tall and the allele for short).", title="Definition: allele"),
        KEY("Words to learn", "These words appear in every genetics question.", cards=[
            ["Genotype", "The alleles an organism has, for example Tt."],
            ["Phenotype", "What the organism looks like or does, for example tall."],
            ["Dominant allele", "Shows its effect even when there is only one copy. Written with a capital letter (T)."],
            ["Recessive allele", "Shows its effect only when there are two copies. Written with a small letter (t)."],
            ["Homozygous", "Two identical alleles (TT or tt)."],
            ["Heterozygous", "Two different alleles (Tt)."],
        ]),
        H("A monohybrid cross"),
        T("Gregor Mendel studied garden peas. He crossed plants that differ in **one** characteristic, such as height. This is a **monohybrid** cross. "
          "In peas, the allele for tall (T) is dominant to the allele for short (t)."),
        T("Each parent has two alleles for the gene, but a gamete gets only one, because gametes are haploid. A tall plant with genotype Tt makes two kinds of gamete, T and t, in equal numbers."),
        EX("Worked example 1: Tt crossed with Tt", intro="Two heterozygous tall plants are crossed (Tt x Tt). Find the genotypes and phenotypes of the offspring.", steps=[
            S("Write the gametes", text="Each parent makes gametes T and t."),
            S("Draw a Punnett square", text="Put one parent's gametes along the top and the other's down the side. Join them in the boxes."),
            S("Read the genotypes", text="TT, Tt, Tt, tt. This is 1 TT : 2 Tt : 1 tt."),
            S("Read the phenotypes", math=r"\text{3 tall} : \text{1 short}"),
            S("State probabilities", math=r"P(\text{short}) = \tfrac{1}{4}, \qquad P(\text{tall}) = \tfrac{3}{4}"),
        ]),
        CODE("""            Gametes from parent 2
              T        t
Gametes   T   TT       Tt
from
parent 1  t   Tt       tt

Genotypes: 1 TT : 2 Tt : 1 tt
Phenotypes: 3 tall : 1 short""", "text", title="Punnett square for Tt x Tt"),
        EX("Worked example 2: homozygous parents", intro="A pure-breeding tall plant (TT) is crossed with a pure-breeding short plant (tt). What are the offspring (F1), and what happens if two F1 plants are crossed (F2)?", steps=[
            S("F1 cross", text="TT makes only T gametes. tt makes only t gametes. Every offspring is Tt."),
            S("F1 phenotype", text="All the F1 plants are tall, because T is dominant."),
            S("F2 cross", text="Tt x Tt gives 1 TT : 2 Tt : 1 tt."),
            S("F2 phenotype", math=r"\text{3 tall} : \text{1 short}"),
        ]),
        T("A ratio such as 3 : 1 is what we expect from a large number of offspring. In a small family the numbers can differ, because each fertilization is a matter of chance. "
          "Mendel counted thousands of plants, so his results came close to 3 : 1."),
        MISTAKE("Writing gametes with two alleles", "A gamete carries one allele of each gene. Write T and t, not Tt, as the gametes."),
        MISTAKE("Mixing genotype and phenotype", "Tt is a genotype. 'Tall' is a phenotype. Say which one the question asks for. Use the same letter in capital and small form for the two alleles."),
        QUIZ("Two heterozygous parents (Tt x Tt) have many offspring. What fraction are expected to be short (tt)?",
             ["1/2", "1/4", "3/4", "All"], 1,
             "The Punnett square gives 1 tt out of 4 boxes.", hint="Draw the square: how many boxes are tt?",
             feedback=["1/2 would be the fraction that are heterozygous, Tt.", "", "3/4 are tall, not short.", "All short is impossible: T is dominant and appears in most offspring."]),
        QUIZ("Which pair of alleles is homozygous recessive?",
             ["TT", "Tt", "tt", "tT"], 2,
             "Two identical small letters show two copies of the recessive allele.", hint="'Homo' means the same.",
             feedback=["TT is homozygous dominant.", "Tt is heterozygous.", "", "tT is the same as Tt: heterozygous."]),
        TIP("Exam link: Paper 1 gives a cross and asks for the expected ratio or the genotype of the parents. Paper 2 may ask for a full genetic diagram. Always show the parents' genotypes, the gametes, the offspring genotypes and the phenotypes, and state the symbols used.", title="Exam link"),
        PQ("Define gene and allele.",
           "A gene is a length of DNA that codes for a protein and controls a characteristic. An allele is one of the different forms of a gene."),
        PQ("Write the base sequence of the strand complementary to A A C T G.",
           "T T G A C. A pairs with T and C pairs with G."),
        PQ("In peas, round seed (R) is dominant to wrinkled seed (r). Show the offspring of Rr x rr.",
           "Gametes: R and r from one parent, r from the other. Offspring: Rr, Rr, rr, rr. That is 1 Rr : 1 rr, or 1 round : 1 wrinkled. The probability of a wrinkled seed is 1/2."),
        PQ("Two tall parents have a short child. What are the genotypes of the parents? Explain.",
           "Both are Tt. The child is tt, so each parent must have given one t. As both parents are tall, each also has the dominant allele T."),
        SUM("DNA is a double helix; A pairs with T and C with G; the order of bases is the genetic code.",
            "A gene is a length of DNA that codes for a protein; alleles are different forms of a gene.",
            "Dominant alleles show with one copy; recessive alleles need two copies.",
            "Tt x Tt gives 1 TT : 2 Tt : 1 tt and 3 : 1 in phenotype."),
    ],
))

# ------------------------------------------------------------------ 8. Test cross, codominance, sex-linkage
LESSONS.append(lesson(
    module=M_REP,
    topic="DNA and inheritance",
    title="Test cross, codominance, sex determination and sex linkage",
    slug="bid-test-cross-codominance-and-sex-linkage",
    minutes=25,
    summary="How a test cross shows an unknown genotype, how incomplete dominance and codominance differ from complete dominance (with ABO and sickle-cell examples), how sex is determined, and how sex-linked traits are inherited.",
    objectives=[
        "Use a test cross to find an unknown genotype",
        "Explain incomplete dominance and codominance, including the ABO blood groups and sickle-cell trait",
        "Explain how sex is determined and show that the chance of a boy or a girl is equal",
        "Work out the inheritance of a sex-linked trait such as colour blindness",
    ],
    key_concepts=["Test cross", "Incomplete dominance", "Codominance", "ABO blood groups", "Sex chromosomes", "Sex linkage", "Carrier"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian families the same questions are asked at every birth: will it be a boy or a girl? Will the baby have the blood group of the mother or the father? "
          "Genetics can answer both questions. It also explains why some conditions, such as colour blindness, are more common in men."),
        H("The test cross"),
        T("A tall pea plant could be TT or Tt. You cannot tell from its looks. To find out, cross it with a plant that is **homozygous recessive** (tt). This is a **test cross**."),
        D("A **test cross** is a cross between an organism of unknown genotype (showing the dominant phenotype) and a homozygous recessive organism, used to find the unknown genotype.", title="Definition: test cross"),
        KEY("Reading the result", "Look at the offspring.", cards=[
            ["All offspring tall", "The unknown parent was TT (it gave only T gametes)."],
            ["About half tall, half short", "The unknown parent was Tt (it gave T and t gametes in equal numbers). The ratio is 1 : 1."],
        ]),
        H("Incomplete dominance and codominance"),
        T("In **complete dominance**, the dominant allele hides the recessive allele. Sometimes the heterozygote is different from both parents."),
        D("**Incomplete dominance** is when neither allele is fully dominant, so the heterozygote has a phenotype between the two homozygotes. "
          "Example: red-flowered (RR) crossed with white-flowered (WW) snapdragon or four o'clock plants gives pink (RW).", title="Definition: incomplete dominance"),
        D("**Codominance** is when both alleles are fully expressed in the heterozygote.", title="Definition: codominance"),
        T("The ABO blood group is controlled by one gene with three alleles: $I^A$, $I^B$ and $i$ (also written $I^O$). "
          "$I^A$ and $I^B$ are codominant, and both are dominant to $i$. People with $I^A I^B$ have group AB: both A and B markers appear on their red blood cells."),
        CODE("""Genotype       Blood group
IA IA or IA i    A
IB IB or IB i    B
IA IB            AB
i i              O""", "text", title="ABO blood groups"),
        EX("Worked example 1: blood groups of children", intro="A mother is group A (genotype IA i) and the father is group B (genotype IB i). Which blood groups are possible in their children?", steps=[
            S("Gametes", text="Mother: IA or i. Father: IB or i."),
            S("Combine", text="IA IB, IA i, IB i, i i."),
            S("Blood groups", text="AB, A, B and O. All four groups are possible, each with probability 1/4."),
        ]),
        T("**Sickle-cell** is another example. The allele $Hb^S$ makes abnormal haemoglobin. A person with two $Hb^S$ alleles has sickle-cell disease. "
          "A person with one $Hb^A$ and one $Hb^S$ has the sickle-cell trait and is usually healthy. Where malaria is common, the trait gives some protection against malaria, which keeps the allele in the population. "
          "If two carriers ($Hb^A Hb^S$) have a child, the chance that the child has sickle-cell disease is 1/4."),
        H("Sex determination"),
        T("Humans have 23 pairs of chromosomes. Twenty-two pairs are the same in males and females. The 23rd pair is the **sex chromosomes**. "
          "A female has two X chromosomes (XX). A male has one X and one Y chromosome (XY). Every egg carries an X. Half of the sperm carry X and half carry Y."),
        CODE("""            Sperm
             X       Y
Egg   X     XX      XY
      X     XX      XY

Girls (XX) : boys (XY) = 1 : 1""", "text", title="Sex determination"),
        T("It is the **sperm** that decides the sex of the baby: an X sperm makes a girl and a Y sperm makes a boy. At each birth the chance of a girl is 1/2 and of a boy is 1/2. "
          "The chance of two girls in a row is 1/2 x 1/2 = 1/4. A family with two girls has the same 1/2 chance of a boy next time, because every fertilization is separate."),
        H("Sex linkage"),
        D("A **sex-linked** gene is a gene located on a sex chromosome (usually the X chromosome). Its inheritance is linked to the sex of the person.", title="Definition: sex linkage"),
        T("The X chromosome carries many genes that the short Y chromosome does not carry. Red-green colour blindness and haemophilia are caused by recessive alleles on the X chromosome. "
          "Use $X^B$ for normal vision and $X^b$ for colour blindness."),
        KEY("Genotypes for colour blindness", "Males have only one X.", cards=[
            ["Female", "$X^B X^B$ normal. $X^B X^b$ normal but a carrier. $X^b X^b$ colour-blind."],
            ["Male", "$X^B Y$ normal. $X^b Y$ colour-blind."],
        ]),
        T("A **carrier** has one copy of the recessive allele but does not show the condition. A male with $X^b Y$ is colour-blind, because he has no second X to cover the recessive allele. "
          "This is why the condition is more common in males."),
        EX("Worked example 2: carrier mother", intro="A woman who is a carrier for colour blindness ($X^B X^b$) has children with a man with normal vision ($X^B Y$). Find the chance that a child is colour-blind.", steps=[
            S("Gametes", text="Mother: $X^B$ or $X^b$. Father: $X^B$ or Y."),
            S("Combine", text="$X^B X^B$ (normal daughter), $X^B X^b$ (carrier daughter), $X^B Y$ (normal son), $X^b Y$ (colour-blind son)."),
            S("Answer", math=r"P(\text{colour-blind child}) = \tfrac{1}{4}"),
            S("Per sex", text="No daughter is colour-blind. Half of the sons are colour-blind."),
        ]),
        MISTAKE('Two common mistakes',
             "Saying the mother decides the sex: All eggs carry an X. The father's sperm carries X or Y, so the "
             "father's sperm decides. Using a test cross with a heterozygote: The test partner must be homozygous "
             'recessive (tt). Using Tt would not show the genotype clearly.'),
        QUIZ("A test cross between a tall plant and a short plant gives about half tall and half short offspring. What is the genotype of the tall parent?",
             ["TT", "Tt", "tt", "Cannot be known"], 1,
             "Half short offspring (tt) means the tall parent gave a t gamete as well as T. So it is Tt.", hint="Short offspring must get a recessive allele from both parents.",
             feedback=["A TT parent would give all tall offspring.", "", "A tt parent would be short.", "The test cross is designed to tell us."]),
        QUIZ("A colour-blind man marries a woman with normal vision who is not a carrier ($X^B X^B$). What is the colour vision of their sons?",
             ["All colour-blind", "Half colour-blind", "All normal", "It cannot be worked out"], 2,
             "Sons get their X from the mother ($X^B$) and a Y from the father. So all sons are normal.", hint="Where does a son get his X from?",
             feedback=["The son's X comes from his mother, who has no colour-blind allele.", "That would need a carrier mother.", "", "It can be worked out."]),
        TIP("Exam link: Paper 1 asks for a test cross result, blood group genotypes, the chance of a boy or girl, or a sex-linked inheritance. Paper 2 may ask for a full genetic diagram with a key. Always define your symbols.", title="Exam link"),
        PQ("Explain what a test cross is and what it shows.",
           "A test cross is a cross between an organism showing the dominant trait but with an unknown genotype and a homozygous recessive organism. If all offspring show the dominant trait, the unknown parent is homozygous dominant. If about half show the recessive trait, it is heterozygous."),
        PQ("Red snapdragons (RR) are crossed with white (WW). Give the phenotype of the offspring and explain the result.",
           "All the offspring are RW and pink. This is incomplete dominance: neither allele is fully dominant, so the heterozygote shows an intermediate colour."),
        PQ("Show how the sex of a child is determined and give the chance of a boy.",
           "The mother's gametes are all X. The father makes X sperm and Y sperm in equal numbers. An X sperm gives XX (girl). A Y sperm gives XY (boy). The chance of a boy is 1/2."),
        SUM("A test cross with a homozygous recessive shows an unknown genotype: all dominant means TT; half and half means Tt.",
            "Incomplete dominance gives an intermediate phenotype; codominance shows both alleles (ABO group AB).",
            "The father's sperm decides the sex: XX is female, XY is male, and the chance of each is 1/2.",
            "Sex-linked recessive conditions such as colour blindness are more common in males because males have only one X."),
    ],
))

# ------------------------------------------------------------------ 9. Variation, mutation, evolution
LESSONS.append(lesson(
    module=M_REP,
    topic="Variation, mutation and evolution",
    title="Variation, mutation and natural selection",
    slug="bid-variation-mutation-and-evolution",
    minutes=24,
    summary="The two kinds of variation, how mutation and meiosis cause it, how natural selection changes populations over time, and how Darwin's and Lamarck's ideas differ.",
    objectives=[
        "Distinguish continuous from discontinuous variation and name its causes",
        "Define mutation and give causes and examples",
        "Explain natural selection step by step using examples such as insecticide-resistant mosquitoes",
        "Compare Darwin's theory with Lamarck's theory and explain artificial selection",
    ],
    key_concepts=["Variation", "Continuous and discontinuous variation", "Mutation", "Natural selection", "Adaptation", "Evolution", "Artificial selection"],
    blocks=[
        H("Introduction"),
        T("Look at the students in your class. No two are exactly alike: they differ in height, skin colour, blood group, and in many other ways. "
          "This is **variation**. It is the raw material of evolution."),
        D("**Variation** is the differences between individuals of the same species.", title="Definition: variation"),
        H("Two kinds of variation"),
        IMG("f5bi-d-variation-graphs.svg", alt="Graph P is a bell-shaped histogram of heights. Graph Q is a bar chart of four blood groups with separate bars",
            caption="Figure 1. Graph P shows continuous variation. Graph Q shows discontinuous variation."),
        KEY("Continuous and discontinuous variation", "Look at the shape of the graph.", cards=[
            ["Continuous variation", "A whole range of values with no clear groups. Examples: height, mass, skin colour. The graph is a bell shape. Caused by genes (many genes) and the environment."],
            ["Discontinuous variation", "A few clear groups with nothing in between. Examples: blood group (A, B, AB, O), ability to roll the tongue. The graph is a bar chart. Mainly caused by genes."],
        ]),
        T("The **environment** also affects some features. A maize plant given plenty of water and fertiliser grows taller than one of the same seed with poor soil. A person's mass changes with diet. "
          "Differences caused only by the environment are not passed to the next generation."),
        H("Causes of genetic variation"),
        T("Genetic variation has three main sources. First, meiosis: crossing over and the random separation of chromosomes. "
          "With 23 pairs of chromosomes, one person can make $2^{23}$ = 8 388 608 different combinations of chromosomes in gametes, even before crossing over. "
          "Second, random fertilization: any sperm can fuse with any egg. Third, **mutation**."),
        D("A **mutation** is a sudden change in the DNA of a cell: a change in a gene (gene mutation) or in the number or structure of chromosomes (chromosome mutation).", title="Definition: mutation"),
        KEY("Facts about mutation", "Most mutations are harmful or have no effect.", cards=[
            ["Causes", "Mistakes when DNA is copied. Ionising radiation (X-rays, gamma rays), ultraviolet light and some chemicals (for example in tobacco smoke) increase the rate of mutation."],
            ["Examples", "Sickle-cell disease (a gene mutation). Albinism (a gene mutation). Down syndrome: a person has three copies of chromosome 21, so 47 chromosomes (a chromosome mutation)."],
            ["Effect", "A mutation in a body cell may cause cancer. A mutation in a gamete can be inherited. Occasionally a mutation is useful and gives an advantage."],
        ]),
        H("Natural selection"),
        T("Charles Darwin and Alfred Wallace explained how species change over time. Their idea is called **natural selection**."),
        D("**Natural selection** is the process by which organisms best suited to their environment survive, reproduce and pass on their alleles, so that these alleles become more common in the population.", title="Definition: natural selection"),
        KEY("Steps in natural selection", "Learn the steps in order.", cards=[
            ["1. Variation", "Individuals of a species are not all the same."],
            ["2. Overproduction", "More offspring are born than can survive."],
            ["3. Struggle for survival", "They compete for food, space and mates, and face predators and disease."],
            ["4. Survival of the fittest", "Those with useful features survive and reproduce more."],
            ["5. Inheritance", "They pass the useful alleles to their offspring. Over many generations the population changes."],
        ]),
        T("**Example: insecticide resistance.** When insecticide is sprayed to kill mosquitoes, nearly all die. By chance, a few have a mutation that makes them resistant. These survive and breed. "
          "Their offspring inherit the resistance allele. After some generations, most of the mosquitoes are resistant. The same happens when bacteria become resistant to an antibiotic."),
        IMG("f5bi-d-natural-selection.svg", alt="Graph of the percentage of light moths falling from 90 to 20 and dark moths rising from 10 to 80 over four generations on dark trees",
            caption="Figure 2. In the classic peppered-moth example, dark moths become more common on soot-darkened trees. The figures are illustrative."),
        T("An **adaptation** is a feature that helps an organism to survive in its environment. Over a very long time, natural selection can lead to **evolution**: the gradual change in the features of a species. "
          "Fossils, similar bone structures in different animals and DNA comparisons support evolution."),
        H("Other ideas"),
        T("**Lamarck's theory** said that features gained in life (acquired characteristics), such as the long "
             'neck of a giraffe stretching for leaves, are passed to offspring. Experiments show that acquired '
             'characteristics are not inherited. A man who loses a finger does not have children without fingers. '
             'Only changes in DNA in the gametes are inherited.\n\n**Artificial selection** (selective breeding) is '
             'when people choose which individuals breed. A farmer keeps the cows that give most milk and breeds '
             'them. Over generations, the herd gives more milk. It is the same as natural selection except that '
             'humans, not the environment, do the selecting.'),
        EX("Worked example 1: explain with natural selection", intro="Explain how a population of bacteria can become resistant to an antibiotic.", steps=[
            S("Variation", text="By mutation, a few bacteria are resistant."),
            S("Selection", text="The antibiotic kills the non-resistant bacteria. The resistant ones survive."),
            S("Inheritance", text="They reproduce and pass the resistance to their offspring."),
            S("Result", text="After some time most bacteria in the population are resistant."),
        ]),
        EX("Worked example 2: classify the variation", intro="State whether each is continuous or discontinuous: (a) mass of students; (b) blood group; (c) length of leaves on a tree.", steps=[
            S("(a) Mass", text="Continuous: a whole range of values."),
            S("(b) Blood group", text="Discontinuous: clear groups."),
            S("(c) Length of leaves", text="Continuous: a range of lengths."),
        ]),
        MISTAKE('Two common mistakes',
             "Saying 'the animal changed because it needed to': Individuals do not change because of need. "
             'Variation exists first. The environment selects the individuals that happen to be suited. Write '
             "'those with the useful feature survived and reproduced'. Thinking all mutations are harmful: Many "
             "have no effect and a few are useful. Say 'mutations are random changes; most are harmful or "
             "neutral'."),
        QUIZ("Which of these shows discontinuous variation?",
             ["Height", "Body mass", "Blood group", "Leaf length"], 2,
             "Blood group has clear categories with no in-between.", hint="Which feature can be put in distinct groups?",
             feedback=["Height shows a range of values.", "Mass shows a range of values.", "", "Leaf length shows a range of values."]),
        QUIZ("Which statement best describes natural selection?",
             ["Organisms change because they need to", "Organisms with useful features survive and pass them on", "Acquired features are passed to offspring", "Humans choose which animals breed"], 1,
             "Individuals with useful features are more likely to survive and reproduce, so their alleles become more common.", hint="It depends on variation which already exists.",
             feedback=["Need does not cause changes.", "", "That was Lamarck's idea, which has been rejected.", "That is artificial selection."]),
        TIP("Exam link: Paper 1 shows a graph of variation or a story about resistance and asks what happens. Paper 2 may ask for a description of natural selection, a comparison with Lamarck's idea or examples of mutation.", title="Exam link"),
        PQ("Distinguish continuous from discontinuous variation, giving one example of each.",
           "Continuous variation shows a whole range of values with no clear groups (for example height). Discontinuous variation shows distinct groups with no in-between values (for example blood group)."),
        PQ("Define mutation and give two things that can cause it.",
           "A mutation is a sudden change in the DNA of a cell (in a gene or in the chromosomes). Radiation such as X-rays and ultraviolet light, and some chemicals can cause it."),
        PQ("Describe how natural selection could cause mosquitoes to become resistant to an insecticide.",
           "There is variation, so some mosquitoes have an allele for resistance. The insecticide kills most, but the resistant ones survive and breed. They pass the allele to their offspring. After many generations most mosquitoes are resistant."),
        SUM("Variation is continuous (a range, bell-shaped) or discontinuous (clear groups).",
            "Mutation is a sudden change in DNA; radiation and some chemicals raise its rate.",
            "Natural selection: variation, overproduction, struggle, survival of the fittest, inheritance.",
            "Lamarck's idea of inheriting acquired features has been rejected; artificial selection is breeding chosen by people."),
    ],
))

# ------------------------------------------------------------------ 10. Ecological concepts and food webs
LESSONS.append(lesson(
    module=M_ECO,
    topic="Ecological concepts and food webs",
    title="Ecology: habitats, food chains, food webs and pyramids",
    slug="bid-ecological-concepts-and-food-webs",
    minutes=24,
    summary="Ecology vocabulary (habitat, population, community, ecosystem, niche), producers, consumers and decomposers, trophic levels, food chains and webs, and pyramids of numbers.",
    objectives=[
        "Define habitat, population, community, ecosystem and niche",
        "Classify organisms as producers, consumers or decomposers and state their trophic level",
        "Construct food chains and read a food web, predicting the effect of removing an organism",
        "Interpret pyramids of numbers, including an inverted pyramid",
    ],
    key_concepts=["Habitat", "Ecosystem", "Biotic and abiotic factors", "Trophic level", "Food chain", "Food web", "Pyramid of numbers"],
    blocks=[
        H("Introduction"),
        T("In Waza National Park, grass grows after the rains, antelopes eat the grass, and lions hunt the antelopes. When the lions die, their bodies are broken down by bacteria and fungi. "
          "Every living thing in the park depends on others and on the non-living world. **Ecology** is the study of these relationships."),
        D("**Ecology** is the study of the relationships between living organisms and their environment.", title="Definition: ecology"),
        H("Ecology vocabulary"),
        KEY("Learn these words", "Say them with an example.", cards=[
            ["Habitat", "The place where an organism lives. Example: a pond, a forest floor, a termite mound."],
            ["Population", "All the organisms of one species living in the same place. Example: all the tilapia in a pond."],
            ["Community", "All the populations of different species living in the same place."],
            ["Ecosystem", "A community together with its non-living environment and the way they interact. Example: a lake, a savanna."],
            ["Niche", "The role of an organism in its habitat: what it eats, where it lives, and what it does."],
        ]),
        T("An ecosystem has **biotic factors** (living things: predators, competitors, disease) and **abiotic factors** (non-living things: temperature, rainfall, light, soil, pH, wind)."),
        H("Producers, consumers and decomposers"),
        KEY("Feeding groups", "Who gets energy from where.", cards=[
            ["Producers", "Green plants and algae. They make food by photosynthesis, using light energy."],
            ["Consumers", "Animals that eat other organisms. Primary consumers eat plants (herbivores). Secondary consumers eat primary consumers. Tertiary consumers eat secondary consumers."],
            ["Decomposers", "Bacteria and fungi. They break down dead organisms and waste and return nutrients to the soil."],
        ]),
        D("A **trophic level** is the position of an organism in a food chain. Producers are the first trophic level, primary consumers the second, and so on.", title="Definition: trophic level"),
        H("Food chains and food webs"),
        D("A **food chain** shows the transfer of energy from one organism to the next, by feeding. Each arrow means 'is eaten by' or 'passes energy to'.", title="Definition: food chain"),
        CODE("grass  ->  grasshopper  ->  frog  ->  snake  ->  hawk", "text", title="A food chain"),
        T("Here grass is the producer. The grasshopper is the primary consumer, the frog the secondary consumer, the snake the tertiary consumer, and the hawk the quaternary consumer. "
          "The arrow always points to the organism that does the eating."),
        D("A **food web** is a set of food chains that are linked together, because most organisms eat more than one kind of food.", title="Definition: food web"),
        IMG("f5bi-d-food-web.svg", alt="Food web with grass eaten by grasshopper and mouse, the grasshopper eaten by a frog, the frog and mouse eaten by a snake, and the snake and mouse eaten by a hawk",
            caption="Figure 1. A food web in a grassland. Arrows point to the feeder."),
        T("Look at Figure 1. The mouse is eaten by both the snake and the hawk. The snake eats the frog and the mouse. Many food chains run through this web. "
          "If the snake were removed, the number of frogs and mice would rise (less predation), and the hawk would depend more on the mice."),
        H("Pyramids of numbers"),
        IMG("f5bi-d-pyramid-numbers.svg", alt="Two pyramids of numbers: a normal pyramid of grass, grasshoppers, frogs and a snake, and an inverted one with one tree, many caterpillars and few birds",
            caption="Figure 2. A normal pyramid of numbers and one that is not pyramid-shaped."),
        T("A **pyramid of numbers** shows the number of organisms at each trophic level. The producers are at the base. In most pyramids the number falls at each level up, because energy is lost at each level. "
          "But if the producer is very large (a tree), the pyramid looks different: one tree feeds hundreds of caterpillars. A **pyramid of biomass** uses the total dry mass of each level and is almost always a true pyramid."),
        EX("Worked example 1: read the food web", intro="Using Figure 1, (a) name all the producers, (b) write a food chain with four organisms, (c) name a tertiary consumer.", steps=[
            S("(a) Producers", text="Grass is the only producer."),
            S("(b) A four-organism chain", text="grass, grasshopper, frog, snake."),
            S("(c) Tertiary consumer", text="The snake eats the frog, which ate the grasshopper, which ate the grass. So the snake is a tertiary consumer (fourth trophic level)."),
        ]),
        EX("Worked example 2: predict the effect", intro="What happens to the number of grasshoppers if the frogs are killed by a disease? Explain.", steps=[
            S("Link the organisms", text="Frogs eat grasshoppers."),
            S("Predict", text="With fewer frogs, fewer grasshoppers are eaten, so the number of grasshoppers rises at first."),
            S("Think further", text="More grasshoppers will eat more grass, so the grass may decrease. The snakes may eat more mice."),
        ]),
        MISTAKE("Pointing the arrows the wrong way", "The arrow shows the movement of energy, so it points to the feeder: grass to grasshopper. Never draw it from the eater to the food."),
        MISTAKE("Putting the Sun or decomposers inside the food chain", "A food chain starts with the producer. The Sun is the source of energy but is not part of the chain. Decomposers act on dead organisms at every level."),
        QUIZ("In the food chain: maize -> weevil -> lizard -> hawk, which organism is the secondary consumer?",
             ["Maize", "Weevil", "Lizard", "Hawk"], 2,
             "The weevil is the primary consumer, so the lizard that eats it is the secondary consumer.", hint="Count from the producer: producer, primary, secondary.",
             feedback=["Maize is the producer.", "The weevil eats the maize, so it is the primary consumer.", "", "The hawk is the tertiary consumer."]),
        QUIZ("Why is the pyramid of numbers for one large tree, many caterpillars and a few birds not a normal pyramid?",
             ["Because trees are consumers", "Because one very large producer supports many small consumers", "Because birds eat the tree", "Because caterpillars are producers"], 1,
             "One big tree feeds hundreds of small caterpillars, so the base is narrow and the middle is wide.", hint="Think about the size of one tree.",
             feedback=["Trees are producers.", "", "Birds eat caterpillars, not the tree.", "Caterpillars eat the leaves and are consumers."]),
        TIP("Exam link: Paper 1 often shows a food web and asks about trophic levels or the effect of removing an organism. Paper 2 may ask you to define ecological terms or construct food chains.", title="Exam link"),
        PQ("Define habitat, community and ecosystem.",
           "A habitat is the place where an organism lives. A community is all the populations of different species living in the same place. An ecosystem is a community together with its non-living environment."),
        PQ("Explain the roles of producers and decomposers in an ecosystem.",
           "Producers make food by photosynthesis, which is the source of energy for all the other organisms. Decomposers break down dead organisms and waste, releasing nutrients back to the soil for plants."),
        PQ("Use Figure 1 to explain what would happen to the mice if the hawks were removed.",
           "There would be fewer predators of mice, so the number of mice would rise at first. More mice would eat more grass. The snakes might eat more mice and fewer frogs."),
        SUM("Habitat, population, community, ecosystem and niche have precise meanings.",
            "Producers make food, consumers eat, and decomposers break down the dead.",
            "Arrows in food chains and webs point to the feeder and show the flow of energy.",
            "Pyramids of numbers usually narrow upward; one large producer can give an inverted shape."),
    ],
))

# ------------------------------------------------------------------ 11. Energy flow and populations
LESSONS.append(lesson(
    module=M_ECO,
    topic="Energy flow, populations and cycles",
    title="Energy flow and estimating population size",
    slug="bid-energy-flow-and-population-estimation",
    minutes=24,
    summary="How energy flows through an ecosystem and is lost at each level, what controls population growth, and how to estimate a population with quadrats and capture-recapture.",
    objectives=[
        "Explain how energy flows through an ecosystem and why only about 10% passes to the next level",
        "Describe a population growth curve and the factors that limit growth",
        "Estimate population size with quadrats and calculate it",
        "Estimate population size by capture-recapture and state its assumptions",
    ],
    key_concepts=["Energy flow", "10% rule", "Population growth", "Limiting factor", "Quadrat", "Capture-recapture"],
    blocks=[
        H("Introduction"),
        T("A farmer in Nkambe wants to know how many pests are in his field. A national park warden wants to know how many elephants live in the forest. "
          "Neither can count every animal or plant. Ecologists use sampling to estimate numbers. First, we look at the energy that supports a population."),
        H("Energy flow"),
        T("The Sun is the source of energy for nearly all ecosystems. Producers capture a small part of the light energy and store it in food by photosynthesis. "
          "When a consumer eats a producer, some energy passes along the food chain. This is **energy flow**."),
        IMG("f5bi-d-energy-flow.svg", alt="Boxes for grass, grasshopper, frog and snake with 10 000, 1 000, 100 and 10 kilojoules, with arrows showing energy lost at each level",
            caption="Figure 1. Energy passed along a food chain."),
        D("**Energy flow** is the one-way movement of energy through an ecosystem, from the Sun to producers, to consumers, and finally lost as heat.", title="Definition: energy flow"),
        T("At each level, only about **10%** of the energy passes to the next level. The rest is lost: as heat from respiration, in waste (faeces and urine), "
          "in parts not eaten (bones, roots) or used for movement. This is why food chains are short (usually four or five levels) and why there are fewer animals at the top."),
        EX("Worked example 1: the 10% rule", intro="A field of grass receives 10 000 kJ of energy that is stored in the grass. Assume 10% passes to each level. How much energy reaches the snake at the end of the chain grass, grasshopper, frog, snake?", steps=[
            S("Grass to grasshopper", math=r"10\,000 \times \tfrac{10}{100} = 1\,000 \text{ kJ}"),
            S("Grasshopper to frog", math=r"1\,000 \times \tfrac{10}{100} = 100 \text{ kJ}"),
            S("Frog to snake", math=r"100 \times \tfrac{10}{100} = 10 \text{ kJ}"),
            S("Answer", text="The snake receives 10 kJ."),
        ]),
        T("Energy does not recycle. It enters as light and leaves as heat. By contrast, matter such as carbon and nitrogen is recycled (the next lesson)."),
        H("Populations"),
        D("The **population size** is the number of individuals of one species in a given area at a given time. The **population density** is the number per unit area.", title="Definition: population"),
        T("A population changes because of four things. It rises with **births** and **immigration** (arrival of individuals). It falls with **deaths** and **emigration** (leaving)."),
        IMG("f5bi-d-population-curve.svg", alt="S-shaped curve of a population growing slowly, then rapidly, then levelling off at a dotted line called the carrying capacity",
            caption="Figure 2. The growth of a population in a new habitat."),
        T("When a few individuals enter a new habitat, growth is slow at first. Then it speeds up because there is plenty of food and space. "
          "Finally the population levels off. The limit is the **carrying capacity**: the largest population the environment can support. "
          "Factors that limit growth include food supply, space, water, disease, predators and competition."),
        H("Estimating population size"),
        T("**Quadrats** are used for plants and slow-moving animals. A quadrat is a square frame, often 1 m by 1 m. Place it at random places in the area (for example by throwing it over your shoulder), and count the organisms in each."),
        F(r"\text{estimated population} = \text{mean number per quadrat} \times \frac{\text{total area}}{\text{area of one quadrat}}", title="Quadrat method"),
        IMG("f5bi-d-quadrat.svg", alt="Five square quadrats with dots showing 3, 5, 4, 6 and 2 plants",
            caption="Figure 3. Plant counts in five quadrats of 1 square metre."),
        EX("Worked example 2: quadrats", intro="Using Figure 3, in a field of 20 m by 10 m, estimate the number of plants of species X.", steps=[
            S("Count the plants in each quadrat", text="3, 5, 4, 6 and 2."),
            S("Find the mean", math=r"\frac{3+5+4+6+2}{5} = \frac{20}{5} = 4 \text{ per m}^2"),
            S("Find the area of the field", math=r"20 \times 10 = 200 \text{ m}^2"),
            S("Estimate the population", math=r"4 \times \frac{200}{1} = 800 \text{ plants}"),
        ]),
        T("**Capture-recapture** is used for moving animals. Catch a sample, mark each animal harmlessly, and release it. Later catch a second sample. Count how many are marked."),
        F(r"N = \frac{M \times n}{m}", title="Capture-recapture (Lincoln index)"),
        T("Here $N$ is the population size, $M$ is the number marked in the first sample, $n$ is the number in the second sample, and $m$ is the number of marked animals in the second sample."),
        EX("Worked example 3: capture-recapture", intro="50 tilapia in a pond are caught, marked and released. The next day 40 fish are caught and 8 are marked. Estimate the number of fish in the pond.", steps=[
            S("Identify the values", text="M = 50, n = 40, m = 8."),
            S("Substitute", math=r"N = \frac{50 \times 40}{8}"),
            S("Calculate", math=r"N = \frac{2000}{8} = 250 \text{ fish}"),
        ]),
        TIP("For capture-recapture to be reliable: the marked animals must mix evenly with the others, the marking must not harm them or make them easier to catch, there must be no births, deaths or movement in and out during the study, and the sample must be large enough.", title="Assumptions"),
        MISTAKE('Two common mistakes',
             'Forgetting to multiply by the area ratio: The mean per quadrat is not the population. Multiply by '
             'the number of quadrats that would fit in the whole area (total area divided by quadrat area). Mixing '
             'up m and n in capture-recapture: m is the number marked in the second sample, n is the total in the '
             "second sample. Mark the second sample's total and the marked count carefully."),
        QUIZ("A food chain starts with 5 000 kJ in the producers. Assuming 10% transfer, how much energy reaches the secondary consumer?",
             ["500 kJ", "50 kJ", "5 kJ", "250 kJ"], 1,
             "Producer to primary: 500 kJ. Primary to secondary: 50 kJ.", hint="Apply 10% twice.",
             feedback=["500 kJ reaches the primary consumer only.", "", "5 kJ would reach the tertiary consumer.", "250 kJ is 5% and not the 10% rule."]),
        QUIZ("A capture-recapture study: 30 marked, second sample 30, of which 6 are marked. What is the population estimate?",
             ["6", "30", "150", "180"], 2,
             "N = (30 x 30) / 6 = 150.", hint="N = M x n / m.",
             feedback=["6 is the number of recaptured marked animals.", "30 is the sample size.", "", "That would be 30 x 6."]),
        TIP("Exam link: Paper 1 includes energy-transfer calculations, quadrat or capture-recapture calculations and growth curves. Paper 2 may ask you to describe how to estimate a population. Show the formula and the units.", title="Exam link"),
        PQ("State the 10% rule and give two reasons why energy is lost between trophic levels.",
           "Only about 10% of the energy at one trophic level passes to the next. Energy is lost as heat from respiration, in waste such as faeces and urine, and in parts that are not eaten or digested."),
        PQ("Describe how to use a quadrat to estimate the number of dandelions in a school field.",
           "Place the quadrat at random positions, count the dandelions in each quadrat, and find the mean per quadrat. Multiply by the area of the field divided by the area of one quadrat. Use many quadrats for better accuracy."),
        PQ("In a lake 80 fish were caught, marked and released. A later sample of 60 fish had 12 marked. Estimate the population.",
           "N = (80 x 60) / 12 = 4800 / 12 = 400 fish."),
        SUM("Energy flows one way: Sun to producers to consumers, and is lost as heat. About 10% passes to the next level.",
            "A population grows in an S-shaped curve and levels off at the carrying capacity.",
            "Quadrat estimate = mean per quadrat x (total area / quadrat area).",
            "Capture-recapture: N = M x n / m, with assumptions."),
    ],
))

# ------------------------------------------------------------------ 12. Cycles
LESSONS.append(lesson(
    module=M_ECO,
    topic="Energy flow, populations and cycles",
    title="Biogeochemical cycles: carbon, nitrogen and water",
    slug="bid-carbon-nitrogen-and-water-cycles",
    minutes=24,
    summary="How carbon, nitrogen and water move between living things and the environment, and the roles of photosynthesis, respiration, decomposers and bacteria in the cycles.",
    objectives=[
        "Describe the carbon cycle and the processes that remove and add carbon dioxide",
        "Describe the nitrogen cycle, naming fixation, nitrification, uptake, decay and denitrification",
        "Describe the water cycle",
        "Draw and annotate a cycle correctly",
    ],
    key_concepts=["Carbon cycle", "Nitrogen fixation", "Nitrification", "Denitrification", "Decomposers", "Water cycle"],
    blocks=[
        H("Introduction"),
        T("A farmer in Ngaoundéré grows beans between rows of maize. The next year the maize grows better where the beans grew. "
          "Bacteria living in the roots of the bean plants have added nitrogen to the soil. Nutrients are used again and again. They move in **cycles**."),
        D("A **biogeochemical cycle** is the movement of an element such as carbon, nitrogen or water between living things (bio) and the non-living environment (geo).", title="Definition: nutrient cycle"),
        H("The carbon cycle"),
        IMG("f5bi-d-carbon-cycle.svg", alt="The carbon cycle: CO2 in the air is taken in by plants by photosynthesis, passes to animals by feeding, returns by respiration and decay, and is also released by burning fossil fuels",
            caption="Figure 1. The carbon cycle."),
        KEY("Processes", "Some remove carbon dioxide from the air, some add it.", cards=[
            ["Photosynthesis", "Removes carbon dioxide from the air. Green plants use it to make glucose and other carbon compounds."],
            ["Feeding", "Carbon compounds pass from plants to animals."],
            ["Respiration", "All living things (plants, animals, decomposers) release carbon dioxide."],
            ["Death and decay", "Decomposers break down dead matter and waste, and release carbon dioxide by respiration."],
            ["Combustion", "Burning wood and fossil fuels (coal, oil, gas) releases carbon dioxide."],
        ]),
        T("Fossil fuels were formed from remains of living things millions of years ago. Burning them returns that carbon to the air faster than plants can remove it, so the amount of carbon dioxide in the air is rising. We study this in the lesson on human impact."),
        H("The nitrogen cycle"),
        T("Air is about 78% nitrogen gas, but plants and animals cannot use it directly. Plants need nitrogen compounds, called **nitrates**, to make proteins. Bacteria change nitrogen between its forms."),
        IMG("f5bi-d-nitrogen-cycle.svg", alt="The nitrogen cycle: nitrogen gas is fixed into nitrates, absorbed by plants, passed to animals, returned as dead matter, changed to ammonium by decomposers and back to nitrates, and some is returned to the air",
            caption="Figure 2. The nitrogen cycle."),
        KEY("Processes", "Each involves different microbes.", cards=[
            ["Nitrogen fixation", "Nitrogen gas is changed into nitrogen compounds. Done by nitrogen-fixing bacteria (for example Rhizobium in the root nodules of beans and other legumes) and by lightning."],
            ["Absorption", "Plants take up nitrates through their roots and use them to make proteins."],
            ["Feeding", "Animals eat plants and use the protein."],
            ["Decay (ammonification)", "Decomposers break down dead organisms and waste (urea) and release ammonium compounds."],
            ["Nitrification", "Nitrifying bacteria change ammonium into nitrites and then into nitrates."],
            ["Denitrification", "In waterlogged soil, denitrifying bacteria change nitrates back into nitrogen gas, which returns to the air."],
        ]),
        T("Farmers add nitrates in fertilisers or grow legumes such as beans and groundnuts to improve the soil. Draining waterlogged fields helps keep nitrates in the soil, by reducing denitrification."),
        H("The water cycle"),
        T("The Sun's heat makes water **evaporate** from seas, lakes and rivers. Plants lose water by **transpiration**. Water vapour rises, cools and **condenses** to form clouds. "
          "It falls as **precipitation** (rain, hail). Some runs off the land into rivers (run-off) and some soaks into the soil (infiltration) and is taken up by plant roots. Rivers carry water back to the sea."),
        CODE("sea, lakes, soil  -> (evaporation, transpiration) ->  water vapour in air\nwater vapour  -> (condensation) ->  clouds\nclouds  -> (precipitation) ->  rain on land\nrain on land -> (run-off, infiltration) -> rivers, soil, sea", "text", title="The water cycle in one chain"),
        EX("Worked example 1: trace a carbon atom", intro="Describe how a carbon atom in the carbon dioxide of the air can become part of a lion and then return to the air.", steps=[
            S("Into the plant", text="Photosynthesis in grass turns carbon dioxide into glucose and other compounds."),
            S("To the animal", text="An antelope eats the grass. A lion eats the antelope."),
            S("Back to the air", text="The lion releases CO2 by respiration. When it dies, decomposers release CO2 by respiration."),
        ]),
        EX("Worked example 2: explain the effect of waterlogging", intro="Why do crops grow poorly in a waterlogged field with little oxygen?", steps=[
            S("Identify the bacteria", text="Denitrifying bacteria thrive where there is no oxygen."),
            S("Link to nitrates", text="They change nitrates into nitrogen gas, which escapes."),
            S("Effect", text="Plants then have less nitrate to make proteins, so growth is poor."),
        ]),
        MISTAKE("Mixing up nitrification and nitrogen fixation", "Fixation changes nitrogen gas into compounds. Nitrification changes ammonium into nitrates. Name the bacteria for each if you can."),
        MISTAKE("Saying that decomposers only break down plants", "They act on all dead organisms, faeces and urine, and release nutrients as ammonium and carbon dioxide."),
        QUIZ("Which process removes carbon dioxide from the air?",
             ["Respiration", "Combustion", "Photosynthesis", "Decay"], 2,
             "Photosynthesis uses carbon dioxide to make glucose.", hint="Green plants.",
             feedback=["Respiration releases carbon dioxide.", "Burning releases carbon dioxide.", "", "Decomposers release carbon dioxide."]),
        QUIZ("Which group of organisms changes ammonium compounds into nitrates?",
             ["Nitrifying bacteria", "Denitrifying bacteria", "Nitrogen-fixing bacteria", "Fungi only"], 0,
             "Nitrifying bacteria carry out nitrification: ammonium to nitrite to nitrate.", hint="The word nitrification gives a clue.",
             feedback=["", "Denitrifying bacteria change nitrates to nitrogen gas.", "Fixing bacteria change nitrogen gas into compounds.", "Fungi help in decay, but nitrification is done by bacteria."]),
        TIP("Exam link: the Board's report asks teachers to drill students on annotated nutrient cycles. Paper 2 often asks you to draw and annotate the carbon or nitrogen cycle; Paper 1 shows a cycle with letters. Practise drawing each cycle from memory.", title="Exam link"),
        PQ("Name three processes that put carbon dioxide into the air and one that removes it.",
           "Respiration, combustion (burning) and decay add carbon dioxide. Photosynthesis removes it."),
        PQ("Describe the role of Rhizobium bacteria.",
           "Rhizobium lives in root nodules of legumes such as beans. It fixes nitrogen gas from the air into nitrogen compounds that the plant can use. The plant gives the bacteria sugars in return."),
        PQ("Explain how nitrates in the soil can be lost from the nitrogen cycle.",
           "Denitrifying bacteria change nitrates into nitrogen gas in waterlogged soil. Nitrates can also be washed away by rain (leaching) or removed in harvested crops."),
        PQ("Describe the water cycle.",
           "Water evaporates from seas and lakes and is lost from plants by transpiration. The vapour condenses to form clouds, and falls as rain. Some runs off into rivers and the sea; some soaks into the soil."),
        SUM("Carbon: photosynthesis removes CO2; respiration, decay and burning add it.",
            "Nitrogen: fixation, absorption, feeding, decay, nitrification and denitrification.",
            "Bacteria and fungi are essential in recycling nutrients.",
            "Water: evaporation, transpiration, condensation, precipitation, run-off and infiltration."),
    ],
))

# ------------------------------------------------------------------ 13. Biological associations
LESSONS.append(lesson(
    module=M_ECO,
    topic="Biological associations",
    title="Biological associations: parasitism, mutualism, commensalism and predation",
    slug="bid-biological-associations",
    minutes=22,
    summary="The four kinds of close relationship between organisms, with examples from Cameroon, and how predator and prey numbers rise and fall together.",
    objectives=[
        "Define parasitism, mutualism, commensalism and predation and give an example of each",
        "Distinguish ectoparasites from endoparasites and host from parasite",
        "Explain the benefit to each partner in a named association",
        "Interpret a graph of predator and prey numbers",
    ],
    key_concepts=["Parasitism", "Host", "Mutualism", "Commensalism", "Predation", "Predator-prey cycle"],
    blocks=[
        H("Introduction"),
        T("On a farm near Bafia, the maize is attacked by a plant called witchweed (Striga) that grows on its roots. "
          "Beans growing nearby have root nodules full of bacteria that help the beans to grow. An egret follows the cattle in the same field and eats the insects that the cattle disturb. "
          "These are three different kinds of relationship. Biologists call them biological associations."),
        D("A **biological association** is a close, long-term relationship between two organisms of different species.", title="Definition: association"),
        H("Parasitism"),
        D("**Parasitism** is an association in which one organism (the **parasite**) lives on or in another organism (the **host**) and feeds on it, and the host is harmed.", title="Definition: parasitism"),
        T("The parasite benefits and the host is harmed (though usually not killed quickly). **Ectoparasites** live on the outside of the host, for example ticks, lice and fleas. "
          "**Endoparasites** live inside the host, for example the tapeworm in the intestine and the malaria parasite (Plasmodium) in the blood. Witchweed (Striga) is a parasitic plant that takes water and food from maize and sorghum roots."),
        H("Mutualism"),
        D("**Mutualism** is an association in which both organisms benefit.", title="Definition: mutualism"),
        KEY("Examples", "Name the benefit to each.", cards=[
            ["Legume and Rhizobium", "The bacteria in the root nodules fix nitrogen for the plant. The plant gives the bacteria sugars and a home."],
            ["Lichen", "A fungus and an alga live together. The alga makes food by photosynthesis. The fungus gives support, water and protection."],
            ["Cattle and gut bacteria", "Bacteria in the stomach of a cow digest cellulose. The cow gives the bacteria food and a warm home."],
        ]),
        H("Commensalism"),
        D("**Commensalism** is an association in which one organism benefits and the other is neither helped nor harmed.", title="Definition: commensalism"),
        T("Examples are epiphytes such as some orchids and ferns that grow on tree branches and use the tree only for support and light, and the cattle egret that feeds on insects disturbed by grazing cattle. "
          "Textbooks differ on a few examples (the egret is sometimes counted as mutualism if it also removes ticks), so check yours."),
        H("Predation"),
        D("**Predation** is feeding in which one animal (the **predator**) kills and eats another animal (the **prey**).", title="Definition: predation"),
        T("Examples: a lion and a zebra, a hawk and a chick, a spider and a fly. Predators have adaptations such as speed, sharp claws and good eyesight. Prey have adaptations such as camouflage, speed, warning colours or spines."),
        IMG("f5bi-d-predator-prey.svg", alt="Two wave-like curves of prey and predator numbers over time; the predator curve rises after the prey curve and falls after it",
            caption="Figure 1. The numbers of predators and prey rise and fall in cycles."),
        T("Look at Figure 1. When prey are plentiful, the number of predators rises. More predators eat more prey, so the number of prey falls. "
          "Then the predators have less food and their number falls. Then the prey recover. The predator curve always follows the prey curve."),
        CODE("""Association    Organism 1    Organism 2    Example
Parasitism     gains         harmed        tick on a cow
Mutualism      gains         gains         Rhizobium in beans
Commensalism   gains         no effect     orchid on a tree
Predation      gains         killed        lion and zebra""", "text", title="Four associations"),
        EX("Worked example 1: classify", intro="Name the association and give a reason: (a) a tapeworm in a human intestine; (b) lichens; (c) a hawk and a mouse.", steps=[
            S("(a) Tapeworm", text="Parasitism. The tapeworm feeds on the host's digested food and the host is harmed."),
            S("(b) Lichen", text="Mutualism. The alga makes food and the fungus gives protection; both benefit."),
            S("(c) Hawk and mouse", text="Predation. The hawk kills and eats the mouse."),
        ]),
        EX("Worked example 2: read the predator-prey graph", intro="Use Figure 1. Explain why the predator numbers peak after the prey numbers.", steps=[
            S("When prey rise", text="There is more food for predators, so they breed and survive better."),
            S("Time lag", text="It takes time for predators to reproduce, so their peak comes after the prey peak."),
            S("Then", text="More predators eat more prey and the prey fall; the predators then fall too."),
        ]),
        MISTAKE("Calling every feeding relationship parasitism", "A parasite lives on or in the host for a long time and does not usually kill it. A predator kills and eats its prey."),
        MISTAKE("Writing that both partners always gain in commensalism", "In commensalism only one gains. The other is not affected. If both gain it is mutualism."),
        QUIZ("A tick attaches to a cow and feeds on its blood. What is this association?",
             ["Mutualism", "Commensalism", "Parasitism", "Predation"], 2,
             "The tick is an ectoparasite. It lives on the host and feeds on it, and the host is harmed.", hint="One organism feeds on a living host without killing it quickly.",
             feedback=["The cow does not gain.", "The cow is not unaffected: it is harmed.", "", "The tick does not kill and eat the cow."]),
        QUIZ("Which association benefits both organisms?",
             ["Legumes and Rhizobium", "Tick and cow", "Orchid and tree", "Hawk and mouse"], 0,
             "Rhizobium gets food and a home and the legume gets nitrogen compounds.", hint="Which one is mutualism?",
             feedback=["", "A tick harms the cow.", "The orchid gains but the tree is not affected.", "The mouse is killed."]),
        TIP("Exam link: Paper 1 usually gives a description and asks which association it is, or a predator-prey graph. Paper 2 may ask for definitions with examples. Always say who benefits and who is harmed.", title="Exam link"),
        PQ("Define parasitism and name one ectoparasite and one endoparasite.",
           "Parasitism is an association in which a parasite lives on or in a host and feeds on it, harming the host. A tick (or louse) is an ectoparasite. A tapeworm (or Plasmodium) is an endoparasite."),
        PQ("Describe the association between a legume and Rhizobium bacteria.",
           "It is mutualism. The bacteria live in the root nodules and fix nitrogen into compounds the plant can use. The plant gives the bacteria sugars for energy and a protected home."),
        PQ("Distinguish commensalism from mutualism.",
           "In commensalism one organism benefits and the other is not affected. In mutualism both organisms benefit."),
        PQ("Explain why the numbers of a predator rise and fall with the numbers of its prey.",
           "More prey means more food, so predators increase. They then eat more prey and the prey decrease. With less food the predators decrease, and the prey can recover. The cycle repeats."),
        SUM("Parasitism: parasite gains, host harmed. Mutualism: both gain.",
            "Commensalism: one gains, the other is unaffected. Predation: predator kills prey.",
            "Examples: tick, tapeworm, Rhizobium, lichen, orchid, lion and zebra.",
            "Predator and prey numbers cycle, with the predators peaking after the prey."),
    ],
))

# ------------------------------------------------------------------ 14. Human impact
LESSONS.append(lesson(
    module=M_ECO,
    topic="Human impact on the environment",
    title="Human impact: pollution, deforestation, eutrophication and conservation",
    slug="bid-human-impact-on-the-environment",
    minutes=25,
    summary="The main kinds of pollution and their effects, why forests are cleared and what follows, how eutrophication kills fish, and how we conserve resources and wildlife.",
    objectives=[
        "Describe the causes and effects of air, water and land pollution",
        "Explain the causes and effects of deforestation",
        "Explain eutrophication as a sequence of events",
        "Describe conservation methods and give examples from Cameroon",
    ],
    key_concepts=["Pollution", "Greenhouse effect", "Acid rain", "Deforestation", "Eutrophication", "Conservation"],
    blocks=[
        H("Introduction"),
        T("In Douala, plastic bottles block the drains in the rainy season and cause floods. Smoke from old vehicles and burning rubbish hangs over the roads. "
          "Many people depend on rivers and forests that are being damaged. Human activities can harm the environment. Understanding how helps us to protect it."),
        H("Pollution"),
        D("**Pollution** is the addition of harmful substances to the environment, in amounts that damage living things or the environment.", title="Definition: pollution"),
        KEY("Air pollution", "Look at the pollutant and what it does.", cards=[
            ["Carbon dioxide and methane", "From burning fuel and wood, forest clearing, livestock and rubbish. They trap heat in the atmosphere: the greenhouse effect, which leads to global warming."],
            ["Carbon monoxide", "From incomplete burning in engines and fires. It combines with haemoglobin and stops red blood cells carrying oxygen. It is poisonous."],
            ["Sulphur dioxide and oxides of nitrogen", "From burning fuels in industry and vehicles. They dissolve in rain to form acid rain, which damages trees, buildings and lakes."],
            ["CFCs", "Chemicals once used in fridges and sprays. They damage the ozone layer, which shields us from harmful ultraviolet light."],
            ["Smoke and dust", "Cause breathing problems and reduce light."],
        ]),
        KEY("Water pollution", "Sources and effects.", cards=[
            ["Sewage", "Spreads disease (cholera, typhoid) and uses up oxygen when bacteria decompose it."],
            ["Fertiliser run-off", "Nitrates and phosphates cause eutrophication (below)."],
            ["Oil spills", "Coat the surface, stop oxygen entering the water and kill sea birds and fish."],
            ["Industrial and mining waste", "Poisonous chemicals (such as mercury) get into food chains."],
            ["Plastic", "Fish and animals eat or get caught in it. It does not rot."],
        ]),
        KEY("Land pollution", "Waste on the land.", cards=[
            ["Non-biodegradable waste", "Plastics and metals do not rot. They stay for a long time."],
            ["Pesticides and herbicides", "Can poison useful animals. Some build up along food chains (bioaccumulation), harming animals at the top, such as birds of prey."],
            ["Waste dumps", "Attract pests, spread disease and can leak chemicals into groundwater."],
        ]),
        H("Deforestation"),
        D("**Deforestation** is the clearing of forests, so that the land can be used for other purposes.", title="Definition: deforestation"),
        T("Forests are cleared for farming (including large plantations), for timber, for firewood and charcoal, for roads and building, and for mining. "
          "Cameroon's rainforests in the South and East are home to many species, and conservation groups work to protect them."),
        KEY("Effects of deforestation", "Think soil, water, air and wildlife.", cards=[
            ["Soil erosion", "Without roots to hold the soil, rain washes it away. Soil becomes poor and rivers get muddy."],
            ["Flooding", "Without trees, rain runs off quickly."],
            ["Loss of habitat", "Animals and plants lose their homes. Some species become extinct and biodiversity falls."],
            ["Climate", "Fewer trees to take up carbon dioxide, so more stays in the air. Less water enters the air by transpiration, which can reduce rainfall."],
        ]),
        H("Eutrophication"),
        IMG("f5bi-d-eutrophication.svg", alt="Flow chart: fertiliser and sewage wash into a lake, algae grow fast, light cannot reach plants which die, bacteria use up oxygen, and fish die",
            caption="Figure 1. The steps of eutrophication."),
        D("**Eutrophication** is the enrichment of water with nutrients (nitrates and phosphates), which leads to excessive growth of algae and the death of other life.", title="Definition: eutrophication"),
        T("Look at Figure 1 and learn the steps in order. Fertiliser and sewage add nitrates and phosphates. Algae grow fast and cover the surface (an algal bloom). "
          "Plants below the surface die because they get no light. Bacteria feed on the dead matter and multiply. The bacteria use up the oxygen in the water by respiration. Fish and other animals die from lack of oxygen."),
        H("Conservation"),
        D("**Conservation** is the protection and wise use of natural resources and wildlife so that they are available for the future.", title="Definition: conservation"),
        KEY("Methods", "Match the method to the problem.", cards=[
            ["Protected areas", "National parks and reserves, such as Waza, Korup and the Dja Faunal Reserve. Hunting and clearing are controlled."],
            ["Reforestation", "Planting trees where forests have been cut."],
            ["Laws and education", "Laws on hunting, logging and dumping, and teaching people why conservation matters."],
            ["Sustainable farming and fishing", "Crop rotation, using manure, limiting net sizes and fish catches so that populations can recover."],
            ["Reduce, reuse, recycle", "Less waste goes to the dump and fewer resources are used."],
            ["Clean energy", "Use of hydroelectric and solar energy instead of burning wood or fossil fuels."],
        ]),
        EX("Worked example 1: eutrophication", intro="Explain why fish die in a pond after fertiliser from a nearby farm is washed into it.", steps=[
            S("Fertiliser adds nutrients", text="Nitrates and phosphates make algae grow quickly."),
            S("Light is blocked", text="The algae cover the surface and the plants beneath die for lack of light."),
            S("Oxygen runs out", text="Bacteria that feed on the dead matter multiply and use up the oxygen."),
            S("Fish die", text="Fish cannot get enough oxygen for respiration."),
        ]),
        EX("Worked example 2: effects of deforestation", intro="Explain two ways in which clearing a forest on a hillside can lead to flooding downstream.", steps=[
            S("Less interception and uptake", text="Without trees, less rain is held on leaves and taken up by roots."),
            S("More run-off and silt", text="Rain runs off quickly into rivers. Eroded soil fills the river bed, so the river overflows more easily."),
        ]),
        MISTAKE("Saying eutrophication is caused by 'too many fish' or 'too much water'", "It is caused by too many nutrients, especially nitrates and phosphates, usually from fertiliser and sewage."),
        MISTAKE("Missing the step about bacteria", "Algae do not use up the oxygen by themselves. Examiners expect you to say that the bacteria that decompose the dead plants and algae use up the oxygen."),
        QUIZ("Which gas from burning fuels is the main cause of acid rain?",
             ["Oxygen", "Sulphur dioxide", "Nitrogen", "Helium"], 1,
             "Sulphur dioxide (and oxides of nitrogen) dissolve in rain to make acid.", hint="It contains sulphur.",
             feedback=["Oxygen does not cause acid rain.", "", "Nitrogen gas is not the cause; oxides of nitrogen are.", "Helium is an inert gas."]),
        QUIZ("What happens first in eutrophication?",
             ["Fish die", "Algae grow rapidly after nutrients enter the water", "Bacteria use up oxygen", "Plants die"], 1,
             "The nutrients cause the algae to grow rapidly. The other events follow.", hint="Nutrients come first.",
             feedback=["Fish die at the end.", "", "That happens after plants die.", "Plants die after the algae block the light."]),
        TIP("Exam link: Paper 1 shows a flow chart or a story about a lake, and asks for a stage or an effect. Paper 2 can ask for the causes and effects of pollution or deforestation and for conservation methods in Cameroon.", title="Exam link"),
        PQ("State two effects of deforestation on the environment.",
           "Soil erosion (and flooding) and loss of habitat for animals and plants. Also less carbon dioxide taken up, which adds to global warming."),
        PQ("Describe how the burning of fossil fuels may cause global warming.",
           "Burning fossil fuels releases carbon dioxide. Carbon dioxide traps heat in the atmosphere (the greenhouse effect), so the Earth's average temperature rises."),
        PQ("Describe the stages of eutrophication in a lake.",
           "Fertiliser and sewage wash in. Nitrates and phosphates make algae grow quickly. The algae block light, so plants under the surface die. Bacteria decompose the dead matter and use up the oxygen. Fish and other animals die from lack of oxygen."),
        PQ("Suggest three ways in which a community can conserve its forest.",
           "Plant new trees to replace those cut. Make laws and enforce them to limit logging and hunting. Teach people about the value of the forest. Set up a protected reserve. Use alternative fuels instead of firewood."),
        SUM("Pollution includes air (CO2, CO, SO2, CFCs), water (sewage, fertiliser, oil) and land (plastic, pesticides).",
            "Deforestation causes soil erosion, flooding, loss of habitat and more carbon dioxide in the air.",
            "Eutrophication: nutrients, algal bloom, light blocked, plants die, bacteria use oxygen, fish die.",
            "Conservation: protected areas, reforestation, laws, education, sustainable use."),
    ],
))

# ------------------------------------------------------------------ 15. Pathogens and immunity
LESSONS.append(lesson(
    module=M_ECO,
    topic="Pathogens, immunity and disease control",
    title="Pathogens, the body's defences and immunity",
    slug="bid-pathogens-and-immunity",
    minutes=24,
    summary="What pathogens are and how they spread, the body's barriers and white blood cells, how antibodies work, and the difference between active and passive, natural and artificial immunity.",
    objectives=[
        "Define pathogen, disease and transmissible disease, and name four types of pathogen",
        "Describe the ways in which pathogens are transmitted",
        "Describe the body's defences, including phagocytes and lymphocytes",
        "Distinguish active from passive immunity and explain how a vaccine works",
    ],
    key_concepts=["Pathogen", "Transmission", "Antigen and antibody", "Phagocyte", "Lymphocyte", "Vaccination", "Active and passive immunity"],
    blocks=[
        H("Introduction"),
        T("In a school in Maroua, a child comes to class with a cough and fever. Within a week, several others are ill. "
          "Something small is spreading from person to person. The germs that cause such diseases are called pathogens."),
        D("A **pathogen** is an organism that causes disease. A **transmissible (infectious) disease** is one that can pass from one person to another.", title="Definition: pathogen"),
        KEY("Types of pathogen", "Examples of the diseases they cause.", cards=[
            ["Bacteria", "Cholera, typhoid, tuberculosis, gonorrhoea, syphilis."],
            ["Viruses", "HIV/AIDS, influenza, measles, polio, the common cold."],
            ["Protoctists", "Malaria (Plasmodium), amoebic dysentery."],
            ["Fungi", "Athlete's foot and ringworm."],
        ]),
        H("How pathogens spread"),
        KEY("Routes of transmission", "Many diseases use more than one route.", cards=[
            ["Direct contact", "Touching, or sexual contact. Example: gonorrhoea, syphilis, ringworm."],
            ["Droplets in the air", "Coughing and sneezing. Example: tuberculosis, influenza."],
            ["Contaminated food and water", "Example: cholera and typhoid (the faecal-oral route)."],
            ["Vectors", "Animals that carry the pathogen from one host to another. Example: female Anopheles mosquito (malaria)."],
            ["Blood and body fluids", "Example: HIV through unscreened blood, shared needles, from mother to child."],
        ]),
        T("A **vector** is an organism that carries a pathogen from one host to another without usually being harmed itself."),
        H("The body's defences"),
        KEY("First barriers", "These stop pathogens entering.", cards=[
            ["Skin", "A tough barrier. A cut is sealed by a blood clot."],
            ["Mucus and cilia", "In the nose and windpipe they trap microbes and sweep them away."],
            ["Stomach acid", "Kills most microbes in food."],
            ["Tears and saliva", "Contain lysozyme, an enzyme that kills bacteria."],
        ]),
        T("If pathogens get past the barriers, white blood cells attack them. **Phagocytes** engulf and digest pathogens (phagocytosis). "
          "**Lymphocytes** make **antibodies**."),
        D("An **antigen** is a molecule (usually on the surface of a pathogen) that causes the body to make antibodies. An **antibody** is a protein made by lymphocytes that is specific to one antigen and helps to destroy the pathogen.", title="Definition: antigen and antibody"),
        T("Antibodies clump the pathogens together, or burst them, or mark them so that phagocytes can eat them. Antibodies are **specific**: an antibody for the measles virus cannot attack the cholera bacterium. "
          "After an infection, some lymphocytes remain as **memory cells**, so that a second infection by the same pathogen is destroyed quickly. That is **immunity**."),
        IMG("f5bi-d-antibody-response.svg", alt="Graph of antibody level: a small slow rise after the first exposure and a much faster and higher rise after the second exposure",
            caption="Figure 1. The first exposure gives a slow, small response. The second is fast and large."),
        H("Types of immunity"),
        KEY("Four kinds", "Active: your body makes antibodies. Passive: you receive antibodies.", cards=[
            ["Natural active", "You catch the disease and your body makes antibodies and memory cells."],
            ["Artificial active", "A vaccine gives a harmless form of the pathogen. Your body makes antibodies and memory cells."],
            ["Natural passive", "A baby gets antibodies from the mother across the placenta and in breast milk (colostrum)."],
            ["Artificial passive", "An injection of antibodies (an antiserum, for example for snake bite or tetanus). Protection is fast but short-lived."],
        ]),
        D("A **vaccine** contains dead or weakened pathogens, or parts of them (antigens). It does not cause the disease, but makes the body produce antibodies and memory cells.", title="Definition: vaccine"),
        T("When many people in a community are vaccinated, the pathogen finds it hard to spread, so even unvaccinated people are partly protected. "
          "Vaccines such as BCG (tuberculosis), polio, measles and others are part of the national vaccination programme in many countries. "
          "Antibiotics, such as penicillin, kill bacteria but do not work on viruses. Overuse leads to resistant bacteria (see the lesson on natural selection)."),
        EX("Worked example 1: explain a booster", intro="Why is a second dose of some vaccines given later?", steps=[
            S("First dose", text="Lymphocytes make a small amount of antibodies and some memory cells."),
            S("Second dose", text="Memory cells respond quickly. They make more antibodies faster and the level lasts longer, as in Figure 1."),
        ]),
        EX("Worked example 2: classify the immunity", intro="Name the type of immunity: (a) a baby protected by breast milk; (b) a child given the measles vaccine; (c) a man given an antiserum after a snake bite.", steps=[
            S("(a) Breast milk", text="Natural passive: the baby receives antibodies made by the mother."),
            S("(b) Measles vaccine", text="Artificial active: the child's own body makes antibodies."),
            S("(c) Antiserum", text="Artificial passive: ready-made antibodies are injected."),
        ]),
        MISTAKE("Saying a vaccine contains antibodies", "A vaccine contains antigens (a weak or dead pathogen). The body then makes its own antibodies. An antiserum contains antibodies."),
        MISTAKE("Using antibiotics for viral diseases", "Antibiotics kill bacteria. They do not work on viruses such as flu or HIV."),
        QUIZ("Which cells make antibodies?",
             ["Red blood cells", "Phagocytes", "Lymphocytes", "Platelets"], 2,
             "Lymphocytes (white blood cells) make antibodies.", hint="Phagocytes engulf. Which white cell makes proteins?",
             feedback=["Red blood cells carry oxygen.", "Phagocytes engulf and digest pathogens.", "", "Platelets help blood to clot."]),
        QUIZ("A baby receives antibodies from its mother's breast milk. This is:",
             ["Natural active immunity", "Artificial active immunity", "Natural passive immunity", "Artificial passive immunity"], 2,
             "The baby gets ready-made antibodies naturally, so it is passive and natural.", hint="Does the baby make the antibodies?",
             feedback=["Active means the person makes the antibodies.", "A vaccine is not involved.", "", "No injection is involved."]),
        TIP("Exam link: Paper 1 asks about pathogens, vectors, antibodies and types of immunity, and sometimes shows the antibody graph. Paper 2 can ask for how the body defends itself or how a vaccine works.", title="Exam link"),
        PQ("Define pathogen and name the type of pathogen that causes (a) malaria, (b) cholera, (c) HIV/AIDS.",
           "A pathogen is an organism that causes disease. (a) Malaria is caused by a protoctist (Plasmodium). (b) Cholera is caused by a bacterium. (c) HIV/AIDS is caused by a virus."),
        PQ("Describe how white blood cells defend the body against pathogens.",
           "Phagocytes engulf and digest pathogens. Lymphocytes make antibodies that are specific to the antigens of the pathogens and help to destroy them. Memory cells remain after the infection."),
        PQ("Explain how a vaccine gives protection against a disease.",
           "The vaccine contains a dead or weakened pathogen or its antigens. The body makes antibodies and memory cells without suffering the disease. If the real pathogen enters later, the memory cells make antibodies quickly."),
        PQ("Distinguish between active and passive immunity, giving one example of each.",
           "In active immunity the body makes its own antibodies, for example after a vaccination. In passive immunity the antibodies are given ready-made, for example from the mother's milk."),
        SUM("Pathogens (bacteria, viruses, protoctists, fungi) spread by contact, air, food and water, vectors and body fluids.",
            "Barriers, phagocytes and lymphocytes protect us; lymphocytes make specific antibodies and memory cells.",
            "Vaccines contain antigens and give artificial active immunity; antiserum gives passive immunity.",
            "Antibiotics kill bacteria but not viruses."),
    ],
))

# ------------------------------------------------------------------ 16. Common diseases
LESSONS.append(lesson(
    module=M_ECO,
    topic="Pathogens, immunity and disease control",
    title="Common diseases: malaria, cholera, typhoid, tuberculosis and sexually transmitted infections",
    slug="bid-common-diseases-and-their-control",
    minutes=25,
    summary="The cause, transmission, symptoms and control of malaria, cholera, typhoid, tuberculosis, gonorrhoea, syphilis and HIV/AIDS, with a clear list of how HIV is and is not spread.",
    objectives=[
        "State the pathogen and the way of transmission of each disease",
        "Describe the main symptoms of each disease",
        "Describe ways of preventing and controlling each disease",
        "Explain how HIV affects the immune system and how it is and is not transmitted",
    ],
    key_concepts=["Malaria", "Cholera", "Typhoid", "Tuberculosis", "Gonorrhoea and syphilis", "HIV/AIDS", "Prevention"],
    blocks=[
        H("Introduction"),
        T("Health workers in Cameroon fight many infections. Some are carried by mosquitoes (malaria). Some spread through dirty water (cholera and typhoid). One spreads through the air (tuberculosis). "
          "Some are passed on during sex (gonorrhoea, syphilis and HIV). Knowing the cause and the route of each disease tells us how to prevent it. Only well-established facts are given here."),
        H("Malaria"),
        T("**Cause:** the protoctist *Plasmodium*. **Transmission:** by the bite of an infected female *Anopheles* mosquito (the vector). It can also pass by blood transfusion or from mother to baby. "
          "**Symptoms:** repeated fever with chills and sweating, headache, tiredness and anaemia, because the parasite destroys red blood cells."),
        KEY("Control of malaria", "Break the cycle at each stage.", cards=[
            ["Stop mosquito bites", "Sleep under insecticide-treated nets, use screens and repellents, and wear long sleeves in the evening."],
            ["Kill the mosquito and its larvae", "Drain or cover standing water, put oil or larvicide on ponds, clear gutters, and spray insecticide indoors."],
            ["Treat the sick and protect the vulnerable", "Prompt treatment with antimalarial drugs. Some people at high risk, such as pregnant women, receive preventive medicine."],
        ]),
        H("Cholera and typhoid"),
        T("**Cholera** is caused by a bacterium (*Vibrio cholerae*). **Typhoid** is caused by a bacterium (*Salmonella Typhi*). Both spread through food and water contaminated with the faeces of an infected person. "
          "**Symptoms of cholera:** severe watery diarrhoea and vomiting, leading to dehydration. **Symptoms of typhoid:** a long fever, headache, stomach pain."),
        IMG("f5bi-d-disease-transmission.svg", alt="Flow chart: faeces of a sick person reach water, soil, flies and hands, then food and drink, then the mouth of a healthy person, who becomes ill",
            caption="Figure 1. How cholera and typhoid spread, and how to break the chain."),
        KEY("Control", "Clean water and clean hands.", cards=[
            ["Safe water", "Boil, filter or treat drinking water. Protect wells and springs from sewage."],
            ["Sanitation", "Use latrines. Dispose of sewage safely."],
            ["Hygiene", "Wash hands with soap after the toilet and before eating. Cover food and wash fruit and vegetables. Control flies."],
            ["Treatment and vaccines", "For cholera, oral rehydration solution (clean water with salts and sugar) replaces lost water. Antibiotics treat typhoid. Vaccines exist for both."],
        ]),
        H("Tuberculosis"),
        T("**Cause:** the bacterium *Mycobacterium tuberculosis*. **Transmission:** by droplets in the air when a person with TB of the lungs coughs or sneezes. "
          "**Symptoms:** a cough that lasts weeks, chest pain, weight loss, night sweats and tiredness, sometimes blood in the sputum. "
          "**Control:** the BCG vaccine in childhood, good ventilation, covering the mouth when coughing, and treatment with several antibiotics for at least six months. It is important to finish the whole course, or the bacteria may become resistant."),
        H("Sexually transmitted infections"),
        T("Some pathogens pass from one person to another through sexual contact. The best protection is to abstain, to be faithful to one uninfected partner, or to use condoms correctly."),
        KEY("Gonorrhoea and syphilis", "Both are bacterial.", cards=[
            ["Gonorrhoea", "Caused by the bacterium Neisseria gonorrhoeae. Spread by sexual contact. Symptoms: a discharge from the penis or vagina and pain when urinating (some people have no symptoms). Untreated, it can cause infertility. Treated with antibiotics."],
            ["Syphilis", "Caused by the bacterium Treponema pallidum. Spread by sexual contact and from mother to baby across the placenta. Symptoms: a painless sore at first, then a rash, and later serious damage to the body. Treated with antibiotics such as penicillin."],
        ]),
        H("HIV and AIDS"),
        T("**HIV** (human immunodeficiency virus) is a virus. It infects and destroys a type of lymphocyte (T helper cells) that is needed to fight infections. "
          "Over years, the immune system is weakened. **AIDS** (acquired immune deficiency syndrome) is the stage at which the body can no longer defend itself and gets serious infections."),
        KEY("HIV spreads by", "Contact with body fluids that contain the virus.", cards=[
            ["Unprotected sex", "With an infected person."],
            ["Infected blood", "Unscreened blood transfusions, shared needles or razors."],
            ["Mother to child", "During pregnancy, birth or breastfeeding."],
        ]),
        KEY("HIV does NOT spread by", "This helps to stop stigma.", cards=[
            ["Everyday contact", "Hugging, shaking hands, sharing food or plates, using the same toilet."],
            ["Insects", "Mosquito bites do not pass on HIV."],
            ["Coughing and sneezing", "It is not an airborne disease."],
        ]),
        T("There is no cure and no vaccine for HIV at present, but antiretroviral drugs (ART) keep the amount of virus low, let people live long and healthy lives, and greatly reduce the chance of passing it on. "
          "Testing is important so that treatment can start early. Control: condoms, abstinence, safe blood, clean needles and treatment of pregnant women to protect their babies."),
        CODE("""Disease       Pathogen            Spread by                    One control measure
Malaria       Plasmodium          female Anopheles mosquito    treated nets, drain water
Cholera       bacterium           contaminated food, water     clean water, sanitation
Typhoid       bacterium           contaminated food, water     hygiene, vaccine
Tuberculosis  bacterium           droplets in air              BCG, full drug course
Gonorrhoea    bacterium           sexual contact               condoms, antibiotics
Syphilis      bacterium           sexual contact, mother-baby  condoms, antibiotics
HIV/AIDS      virus               sex, blood, mother-child     condoms, safe blood, ART""", "text", title="Summary table"),
        EX("Worked example 1: suggest control measures", intro="A village has an outbreak of cholera. Suggest four measures to stop it spreading.", steps=[
            S("Clean water", text="Boil or treat all drinking water."),
            S("Hygiene", text="Wash hands with soap after the toilet and before preparing food."),
            S("Sanitation", text="Use latrines, keep them away from wells, and dispose of waste safely."),
            S("Treatment", text="Give oral rehydration solution to those who are sick and take severe cases to the health centre."),
        ]),
        EX("Worked example 2: why can HIV lead to AIDS?", intro="Explain how HIV weakens the body's defences.", steps=[
            S("Target", text="HIV infects and destroys T helper lymphocytes."),
            S("Effect", text="With fewer of these cells, the body cannot make antibodies well."),
            S("Result", text="Infections that a healthy person could fight off become serious. This stage is called AIDS."),
        ]),
        MISTAKE('Two common mistakes',
             'Saying mosquitoes spread HIV: Mosquitoes spread malaria (and some other diseases) but not HIV. Give '
             "the correct routes of transmission. Saying 'malaria is caused by a mosquito': Malaria is caused by "
             'the protoctist Plasmodium. The mosquito is the vector that carries it.'),
        QUIZ("Which disease is spread by droplets in the air when an infected person coughs?",
             ["Cholera", "Malaria", "Tuberculosis", "Syphilis"], 2,
             "TB is spread by droplets from the lungs of an infected person.", hint="Think of a long cough.",
             feedback=["Cholera spreads by water and food.", "Malaria is spread by a mosquito.", "", "Syphilis spreads by sexual contact."]),
        QUIZ("Which of the following does NOT spread HIV?",
             ["Unprotected sex", "Shared needles", "Mosquito bites", "Infected blood transfusion"], 2,
             "HIV is not spread by mosquito bites or by everyday contact.", hint="Choose the route that does not involve body fluids.",
             feedback=["It does spread HIV.", "Needles can carry infected blood.", "", "Infected blood passes on the virus."]),
        TIP("Exam link: the Board lists these diseases among the common ones. Paper 1 asks for the pathogen, vector, or the control of a disease. Paper 2 can ask you to describe how one disease is transmitted and controlled. Write the correct type of pathogen and the exact route.", title="Exam link"),
        PQ("Name the pathogen, the vector and two control measures for malaria.",
           "The pathogen is Plasmodium (a protoctist). The vector is the female Anopheles mosquito. Control: sleep under treated mosquito nets and drain standing water where mosquitoes breed."),
        PQ("Describe how cholera is spread and how it can be prevented.",
           "Cholera bacteria in the faeces of an infected person contaminate water and food. A person who swallows them gets ill. It can be prevented by boiling water, using latrines, washing hands and covering food."),
        PQ("Explain why it is important to finish a full course of antibiotics for tuberculosis.",
           "If treatment stops early, some bacteria survive. They may become resistant and spread, which makes the disease harder to treat."),
        SUM("Malaria: Plasmodium, female Anopheles; nets, drain water, treatment.",
            "Cholera and typhoid: bacteria in contaminated water and food; clean water, sanitation and hygiene.",
            "Tuberculosis: bacterium, droplets; BCG, ventilation, full drug course.",
            "Gonorrhoea and syphilis: bacteria, sexual contact; condoms, antibiotics.",
            "HIV: virus attacking T helper lymphocytes; spread by sex, blood, mother to child; ART keeps the virus low."),
    ],
))

# ------------------------------------------------------------------ 17. Paper 1 strategy
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: the six types of multiple-choice question",
    slug="bix-paper1-six-question-types",
    minutes=24,
    summary="The layout of Biology Paper 1 (50 multiple-choice questions in six sections) and a method for each type: simple, diagram, multiple-response, assertion-and-reasoning, biological terms, and situations and experiments.",
    objectives=[
        "Describe the structure of Paper 1 and the six sections",
        "Apply a method to each of the six question types",
        "Manage time and answer carefully on an electronically marked paper",
        "Eliminate wrong options by recognising common traps",
    ],
    key_concepts=["Paper 1 structure", "Diagram questions", "Multiple response", "Assertion and reasoning", "Biological terms", "Experiments and situations"],
    blocks=[
        H("Introduction"),
        T("Paper 1 is the same every year in its shape: 50 multiple-choice questions to be answered in 1 hour 30 minutes. That is less than two minutes per question. "
          "The paper covers the whole syllabus, from Form 1 to Form 5, and it is marked electronically. This lesson shows what the six sections ask and how to approach each one."),
        KEY("The six sections", "As described in the Board's report on the 2023 examination.", cards=[
            ["Section 1: 7 simple questions", "Direct questions on facts and definitions."],
            ["Section 2: 13 diagram questions", "Questions that use a biological diagram, drawing or graph."],
            ["Section 3: 5 multiple-response questions", "Several statements; you choose which are correct."],
            ["Section 4: 5 assertion-and-reasoning questions", "An assertion and a reason; you judge both."],
            ["Section 5: 10 biological terms questions", "Matching a term, a definition or a description."],
            ["Section 6: 10 situations and experiments questions", "A short story, table or experiment to interpret."],
        ]),
        T("Because the paper is marked electronically, follow the instructions exactly: use the pencil and shading style the paper asks for, fill in one answer only, and make sure the answer number matches the question number."),
        H("Section 1: simple questions"),
        T("These are recall questions. Read all four options before choosing, because two options often look right. Cover the options, think of the answer, then look."),
        EX("Worked example: a simple question", intro="Which part of a flower becomes the fruit after fertilization? A. Ovule B. Ovary C. Stigma D. Anther", steps=[
            S("Think of the answer first", text="After fertilization the ovary becomes the fruit and the ovule becomes the seed."),
            S("Find it and check the others", text="B is correct. Ovule is the seed (a common trap); stigma and anther do not form fruit."),
        ]),
        H("Section 2: diagram questions"),
        T("Look at the whole diagram, the title, the labels and any scale or key. Do not rely on a quick glance. Identify the structure the letter points to, not what is next to it. "
          "In graphs, read the axes and units first, then the shape."),
        EX("Worked example: a graph", intro="A graph shows enzyme activity rising to a peak at 40 degrees Celsius, then falling to zero at 60. What is the likely reason for the fall above 40?", steps=[
            S("Read the graph", text="The rate rises, peaks and then falls."),
            S("Link to biology", text="High temperatures change the shape of the enzyme's active site (denaturation), so it cannot bind the substrate."),
        ]),
        H("Section 3: multiple-response questions"),
        T("A question gives several statements, numbered 1, 2 and 3 (or more), and the options are combinations such as '1 and 2 only', '1 and 3 only', '2 and 3 only' or 'all of them'. "
          "Judge each statement separately as true or false. Then pick the option that matches your list. Do not choose by guessing from the first statement. "
          "The exact wording of the options may differ in the real paper, so read the instructions."),
        EX("Worked example: multiple response", intro="Which of these are features of wind-pollinated flowers? 1. Large feathery stigma 2. Brightly coloured petals 3. Light, dry pollen. Options: A. 1 and 2 only  B. 1 and 3 only  C. 2 and 3 only  D. 1, 2 and 3.", steps=[
            S("Judge each statement", text="1 is true. 2 is false (that is for insect-pollinated flowers). 3 is true."),
            S("Match", text="Statements 1 and 3 are true, so the answer is B."),
        ]),
        H("Section 4: assertion and reasoning"),
        T("You are given an **assertion** (a statement) and a **reason** (another statement). Follow these steps. First decide if the assertion is true. Then decide if the reason is true. "
          "If both are true, ask: does the reason explain the assertion? The Board's option wording may vary, so read the options carefully. A typical set of options is: both true and the reason explains the assertion; both true but the reason does not explain it; assertion true and reason false; assertion false and reason true."),
        EX("Worked example: assertion and reasoning", intro="Assertion: Plants kept in the dark lose mass in their dry matter. Reason: Respiration continues in the dark but photosynthesis does not.", steps=[
            S("Assertion", text="True. In the dark, plants respire and use up stored food."),
            S("Reason", text="True. Photosynthesis needs light; respiration does not."),
            S("Link", text="The reason explains the assertion, so the answer is 'both true and the reason explains the assertion'."),
        ]),
        MISTAKE('Two common mistakes',
             "Choosing 'reason explains' just because both statements are true: Two true statements may be "
             "unrelated. For example: 'Water is a liquid' and 'Plants need water' are both true, but the second "
             'does not explain the first. Reading the question too fast: Words such as NOT, ONLY, EXCEPT and FIRST '
             'change the answer. Underline them in your head.'),
        H("Section 5: biological terms"),
        T("These questions test precise vocabulary: a definition to match to a term, a word that completes a sentence, or the right term for a process. Learn each term with its definition and its spelling. "
          "The Board's reports note that candidates confuse terms such as fission and fusion, and mis-spell terms such as pollen, gamete, ovary and habitat."),
        EX("Worked example: a terms question", intro="The fusion of the nucleus of a male gamete with the nucleus of a female gamete is called: A. pollination B. fertilization C. germination D. dispersal.", steps=[
            S("Define each option", text="Pollination: pollen reaches the stigma. Germination: a seed grows. Dispersal: seeds spread."),
            S("Answer", text="B, fertilization, is the fusion of gametes."),
        ]),
        H("Section 6: situations and experiments"),
        T("A short passage, table or experiment is given. Identify what is being tested (the independent variable), what is measured (the dependent variable) and what must be kept the same (control variables). "
          "Then work out what the result shows. Do not use your own beliefs: use the information given."),
        EX("Worked example: an experiment", intro="Four tubes of seeds: A moist and warm, B dry and warm, C moist and cold, D under oil with no oxygen. Only A germinates. Which factors are needed?", steps=[
            S("Compare tubes with A", text="B lacks water, C lacks warmth, D lacks oxygen."),
            S("Conclusion", text="Water, warmth and oxygen are all needed for germination."),
        ]),
        H("Time and technique"),
        KEY("A simple plan", "For a 90-minute paper.", cards=[
            ["First pass", "Answer the questions you know at once. Spend no more than 2 minutes on a question."],
            ["Mark and return", "Mark hard questions lightly and come back at the end."],
            ["Check", "Keep 5 to 10 minutes to check that each answer is in the right place."],
            ["Do not leave blanks", "Eliminate options you know are wrong, then choose. A guess is better than a blank."],
        ]),
        QUIZ("How many questions are in Biology Paper 1, and how long do you have?",
             ["40 questions in 1 hour", "50 questions in 1 hour 30 minutes", "50 questions in 2 hours 30 minutes", "60 questions in 1 hour 30 minutes"], 1,
             "Paper 1 has 50 multiple-choice questions in 1 hour 30 minutes.", hint="It is less than two minutes per question.",
             feedback=["The paper has 50 questions and lasts longer.", "", "2 hours 30 minutes is the length of Paper 2.", "There are 50 questions, not 60."]),
        QUIZ("In an assertion-and-reasoning question, both statements are true. What must you check next?",
             ["Whether the options are in order", "Whether the reason explains the assertion", "Whether the sentence is long", "Nothing; choose the first option"], 1,
             "Both true is not enough. The reason must explain the assertion.", hint="Think of 'because'.",
             feedback=["Option order does not matter.", "", "Length is irrelevant.", "The first option is not always correct."]),
        TIP("Take the Paper 1 mock exam under timed conditions, then review each wrong answer. The results page lists your score by topic, so you can revise the weakest ones first.", title="Practice"),
        PQ("List the six sections of Biology Paper 1 and the number of questions in each.",
           "Section 1: 7 simple questions. Section 2: 13 diagram questions. Section 3: 5 multiple-response questions. Section 4: 5 assertion-and-reasoning questions. Section 5: 10 biological terms questions. Section 6: 10 situations and experiments questions."),
        PQ("Explain how to answer a multiple-response question.",
           "Judge each numbered statement separately as true or false. Then choose the option that lists exactly the true statements."),
        PQ("An assertion and a reason are both true. How do you decide between the two options that say both are true?",
           "Ask whether the reason explains the assertion. If it does, choose 'reason explains'. If it is a true but separate fact, choose 'does not explain'."),
        SUM("Paper 1: 50 multiple-choice questions, 1 hour 30 minutes, six sections, marked electronically.",
            "Diagrams: read titles, labels and axes. Multiple response: judge each statement.",
            "Assertion and reasoning: assertion, reason, then whether the reason explains.",
            "Terms: learn definitions and spelling. Experiments: variables, controls and conclusion.",
            "Manage time: first pass, mark and return, and check."),
    ],
))

# ------------------------------------------------------------------ 18. Paper 2 strategy
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: Section A, Section B and planning an essay",
    slug="bix-paper2-sections-and-essay-planning",
    minutes=24,
    summary="The layout of Paper 2 (three compulsory questions and a choice of two from four), how to read command words, how to plan and write an essay-type answer, and how to draw and label diagrams.",
    objectives=[
        "State the layout of Paper 2: Section A compulsory, Section B choose two",
        "Choose Section B questions wisely and manage the 2 hours 30 minutes",
        "Interpret command words such as define, state, describe, explain, compare and distinguish",
        "Plan and write a clear answer and draw a labelled biological diagram",
    ],
    key_concepts=["Paper 2 layout", "Command words", "Planning an answer", "Definitions", "Labelled diagrams", "Spelling of biological terms"],
    blocks=[
        H("Introduction"),
        T("Paper 2 is written in your own words. According to the Board's report on the 2023 examination, it has seven essay-type questions in two sections. "
          "Section A has three compulsory questions. Section B has four questions, and you answer any two. The paper lasts 2 hours 30 minutes. "
          "The report says that many candidates found it hard to define terms, describe experiments, interpret data and draw labelled diagrams, so this lesson trains those skills. "
          "Check the exact format with your teacher, because it can change."),
        KEY("Layout", "Know before you enter the room.", cards=[
            ["Section A", "Three questions, all compulsory. Answer every question and every part, even the ones you find hard."],
            ["Section B", "Four questions, of which you answer any two. Read all four before choosing."],
            ["Time", "2 hours 30 minutes in all. Divide your time between the questions and keep a few minutes to check."],
        ]),
        T("The report noted that one compulsory question had a very low average and that some candidates did not attempt every part of Section A. Never leave a compulsory part blank: write what you know, because marks are given for correct points."),
        H("Choosing Section B questions"),
        T("Read the four questions. For each one, ask: can I define the key terms, can I draw the diagram, and can I give at least five clear points? Choose the two questions where you can answer yes. "
          "Do not choose a question just because the topic looks familiar; check what the question actually asks."),
        H("Command words"),
        CODE("""Word          What to do
Define        Give the exact meaning of a term.
State         Give a short answer; no explanation needed.
List          Give a number of items, one after another.
Name          Give the correct term (a single word or phrase).
Describe      Say what happens, step by step, or what it looks like.
Explain       Give reasons: say why or how, using 'because'.
Compare       Give similarities AND differences (use 'whereas').
Distinguish   Give differences between two things.
Draw/label    Use a pencil, large clear drawing, label lines touching.
Suggest       Apply what you know to a new situation.""", "text", title="Command words"),
        MISTAKE("Describing when asked to explain", "'Describe' says what happens. 'Explain' says why. Use 'because' or 'so that' in explanations."),
        MISTAKE("Giving only the differences in a 'compare' question", "Compare asks for both similarities and differences. When you compare, name both things in the same sentence: 'Mitosis makes two cells, whereas meiosis makes four.'"),
        H("Planning an answer"),
        T("Spend 2 minutes on a plan for any longer answer. Write key words in the margin. Then answer in short, clear sentences. Each point should be one fact. "
          "Use correct biological terms and spell them correctly. Examiners cannot award a mark for a wrong term, for example 'polline' for pollen."),
        EX("Worked example 1: plan an answer", intro="Describe how a named transmissible disease is spread and controlled. (Choose malaria.)", steps=[
            S("Cause and vector", text="Plasmodium (a protoctist), carried by the female Anopheles mosquito."),
            S("Transmission", text="The infected mosquito bites a person and passes the parasite into the blood."),
            S("Symptoms", text="Repeated fever, chills, headache, anaemia."),
            S("Control", text="Sleep under treated nets; drain standing water; kill larvae; use antimalarial drugs."),
            S("Write in order", text="Start with the cause, then spread, then control. Use paragraphs or numbered points."),
        ]),
        EX("Worked example 2: a diagram question", intro="Draw a labelled diagram of the female reproductive system.", steps=[
            S("Draw large and clear", text="Use a sharp pencil. Do not use colour or shading. Make the outline continuous."),
            S("Draw the main parts", text="Two ovaries, two oviducts, the uterus, the cervix and the vagina."),
            S("Label", text="Draw straight lines with no arrowheads that touch each part. Write the label in horizontal text with correct spelling."),
            S("Title", text="Add a heading such as 'The female reproductive system'."),
        ]),
        H("Words the Board's report says are misspelt"),
        T("Learn to spell these: pollen, fusion, gamete, clotting, anther, stigma, epididymis, ovary, pseudopodium, pyrenoid, septum, semilunar valve, cytoplasmic strand, dull, acetylcholine, habitat, nucleus and scent. "
          "Write each one three times from memory."),
        TIP("Use the marks (shown on the paper) as a guide to how many points to give. A part worth several marks needs several different points, not one point repeated.", title="Marks"),
        QUIZ("A question says 'Distinguish between mitosis and meiosis.' What should you write?",
             ["Only what mitosis is", "The differences between them", "The similarities between them", "A diagram"], 1,
             "Distinguish means to give the differences.", hint="Think of 'to tell apart'.",
             feedback=["That is not enough.", "", "Compare asks for similarities and differences.", "A diagram is not requested."]),
        QUIZ("Which Section B strategy is best?",
             ["Answer the first two questions", "Read all four and choose the two you can answer best", "Answer three questions", "Answer none"], 1,
             "Read all four questions, then choose the two where you know the terms and can give enough points.", hint="You have a choice.",
             feedback=["The first two may be the harder ones for you.", "", "Only two are needed; a third wastes time.", "You must answer two."]),
        PQ("State the structure of Paper 2.",
           "Paper 2 has seven essay-type questions. Section A has three compulsory questions. Section B has four questions from which any two are answered. The paper lasts 2 hours 30 minutes."),
        PQ("Explain the difference between 'describe' and 'explain'.",
           "Describe asks what happens or what something looks like. Explain asks for the reasons why it happens, usually using 'because'."),
        PQ("List four rules for a good labelled biological diagram.",
           "Use a pencil. Draw a large, clear outline with no shading. Use straight label lines that touch the parts and do not cross. Give a title and spell each label correctly."),
        PQ("Why should you not leave a compulsory question part blank?",
           "Marks are awarded for each correct point. Writing what you know can earn marks, but a blank earns none."),
        SUM("Paper 2: seven questions; Section A three compulsory; Section B choose two of four; 2 hours 30 minutes.",
            "Read command words: define, state, describe, explain, compare, distinguish.",
            "Plan for two minutes, write short clear points with correct terms and spellings.",
            "Draw labelled diagrams large, in pencil, with correct labels."),
    ],
))

# ------------------------------------------------------------------ 19. Interpreting experiments and data
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Interpreting experiments, tables and graphs",
    slug="bix-interpreting-experiments-and-data",
    minutes=24,
    summary="How to identify variables and controls, describe a method, read tables and graphs, calculate means and percentages, draw a graph, and write a conclusion supported by the data.",
    objectives=[
        "Identify the independent, dependent and control variables in an experiment",
        "Describe a fair-test method and say how to make results reliable",
        "Calculate a mean and a percentage from a table",
        "Draw and interpret a line graph and write a conclusion that quotes the data",
    ],
    key_concepts=["Independent variable", "Dependent variable", "Control", "Reliability", "Mean and percentage", "Graph plotting", "Conclusion"],
    blocks=[
        H("Introduction"),
        T("A student in Bamenda wants to know whether temperature affects how fast seeds germinate. She sets up five dishes at different temperatures and counts the seeds that germinate. "
          "Biology exam questions often give you results like these and ask you to describe, calculate and explain. "
          "The Board's report says that candidates are weak at analysing and interpreting data, and need basic skills in plotting and interpreting graphs. This lesson builds those skills."),
        H("Variables and controls"),
        KEY("Three kinds of variable", "Every experiment has these.", cards=[
            ["Independent variable", "The factor that you change on purpose. Example: the temperature."],
            ["Dependent variable", "The factor that you measure to see the effect. Example: the number of seeds that germinate."],
            ["Control variables", "Factors that you keep the same so that the test is fair. Example: the type of seed, the number of seeds, the amount of water, the time."],
        ]),
        D("A **control experiment** is a set-up that is the same as the test in every way except for the factor being tested. It shows that the factor, and not something else, caused the result.", title="Definition: control experiment"),
        T("A **fair test** changes one factor only. To make results **reliable**, repeat the experiment several times and use a large sample (many seeds, not two). Then find the mean."),
        H("Reading a table"),
        T("The student placed 50 seeds in each dish and counted the seeds that germinated after 5 days."),
        CODE("""Temperature (C)    Seeds that germinated (out of 50)
10                  5
20                  28
30                  45
40                  12
50                  0""", "text", title="Results"),
        T("To compare the results fairly, turn them into percentages. A percentage is the part divided by the whole, times 100."),
        F(r"\text{percentage} = \frac{\text{part}}{\text{whole}} \times 100", title="Percentage"),
        EX("Worked example 1: percentage germination", intro="Find the percentage of seeds that germinated at 30 degrees Celsius and at 40 degrees Celsius.", steps=[
            S("At 30", math=r"\frac{45}{50} \times 100 = 90\%"),
            S("At 40", math=r"\frac{12}{50} \times 100 = 24\%"),
            S("Describe", text="Germination was highest at 30 degrees (90%) and fell to 24% at 40 degrees."),
        ]),
        EX("Worked example 2: the mean", intro="Three repeats at 20 degrees Celsius gave 27, 28 and 29 seeds. Find the mean number germinated.", steps=[
            S("Add the values", math=r"27 + 28 + 29 = 84"),
            S("Divide by the number of values", math=r"\frac{84}{3} = 28"),
            S("Answer", text="The mean is 28 seeds."),
        ]),
        H("Drawing and describing a graph"),
        KEY("Rules for plotting a line graph", "Marks are given for each of these.", cards=[
            ["Axes", "Put the independent variable on the horizontal (x) axis and the dependent variable on the vertical (y) axis."],
            ["Labels and units", "Write the name and the unit of each axis, for example 'Temperature (degrees Celsius)'."],
            ["Scale", "Choose a scale that uses more than half of the graph paper. Make the steps equal."],
            ["Plot", "Mark each point accurately with a small cross or dot."],
            ["Join", "Join the points with a smooth curve or straight lines as the data suggest. Use a sharp pencil."],
        ]),
        T("To **describe a trend**, say how the dependent variable changes as the independent variable changes, and **quote values** from the table or graph. "
          "For our data: 'As the temperature rises from 10 to 30 degrees Celsius, the percentage of seeds that germinate rises from 10% to 90%. Above 30 degrees it falls to 24% at 40 degrees and to 0% at 50 degrees.'"),
        H("Writing a conclusion"),
        T("A conclusion answers the question that the experiment asked. It must be supported by the results. For our data: 'Seeds germinate best at about 30 degrees Celsius. Germination is poor at low temperatures and at temperatures above 40 degrees. "
          "This is because enzymes work best at a moderate temperature and are damaged at high temperature.' Do not claim more than the data show. The data do not show, for example, that 31 degrees is worse than 30 degrees."),
        EX("Worked example 3: improving the experiment", intro="Suggest two ways to improve the reliability of the investigation.", steps=[
            S("Repeat", text="Repeat each temperature three times and calculate the mean."),
            S("Larger sample and narrower steps", text="Use more seeds per dish. Test more temperatures between 20 and 40 degrees to find the best temperature more exactly."),
        ]),
        MISTAKE("Putting the variables on the wrong axes", "Time or the factor you control goes on the horizontal axis. What you measure goes on the vertical axis."),
        MISTAKE("Describing a graph without numbers", "'It goes up and then down' earns little. Quote values from the axes: 'It rises from 10% at 10 degrees to 90% at 30 degrees.'"),
        MISTAKE("Missing units", "Always write units (degrees Celsius, g, cm3, minutes). Missing units cost marks in calculations and on graph axes."),
        QUIZ("In an experiment, the number of seeds germinating at different temperatures is measured. Which is the dependent variable?",
             ["The temperature", "The type of seed", "The number of seeds that germinate", "The amount of water"], 2,
             "The dependent variable is what you measure: the number that germinate.", hint="Which factor is measured, not changed?",
             feedback=["Temperature is the independent variable.", "The seed type is kept the same.", "", "The water is kept the same."]),
        QUIZ("Out of 50 seeds, 28 germinate. What is the percentage?",
             ["28%", "56%", "22%", "50%"], 1,
             "28 divided by 50, times 100, is 56%.", hint="part divided by whole, times 100.",
             feedback=["28% treats 28 as a percentage without dividing by 50.", "", "22 is the number that did not germinate.", "50% would be 25 seeds."]),
        TIP("Exam link: Paper 1 Section 6 gives short experiments and tables. Paper 2 often gives a table or graph and asks you to describe it, calculate, plot or explain. Practise with each experiment in your textbook.", title="Exam link"),
        PQ("State the difference between an independent variable and a dependent variable.",
           "The independent variable is the factor that is changed by the experimenter. The dependent variable is the factor that is measured to see the effect."),
        PQ("Calculate the mean of 12, 14 and 13 and the percentage germination if 36 of 40 seeds germinate.",
           "Mean = (12 + 14 + 13) / 3 = 39 / 3 = 13. Percentage = 36 / 40 x 100 = 90%."),
        PQ("List five things that must be shown on a line graph to earn full marks.",
           "Labelled axes with units, a sensible even scale, accurate plotting of all points, the independent variable on the x-axis and a neat line joining the points."),
        PQ("Why is a control experiment useful?",
           "A control is the same as the test in every way except the factor tested. It shows that the result is due to that factor and not to something else."),
        SUM("Independent variable: changed. Dependent variable: measured. Control variables: kept the same.",
            "Reliable results: repeat, large sample, calculate a mean.",
            "Percentage = part / whole x 100; mean = total / number of values.",
            "Graphs: independent variable on the x-axis, labels with units, even scale, accurate points.",
            "Describe trends with values and write conclusions that the data support."),
    ],
))
