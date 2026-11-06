"""Form 5 Biology (O Level 0510), modules 1 and 2: Taxonomy & Variety of Living Organisms, and Cell Biology &
Cellular Transport. 13 lessons, one practice set each (see the practice file of the same name).

Scope notes: the blueprint lists ideas, not a Board syllabus. Facts are the standard O Level ones. Where textbooks
differ the lesson says "check your textbook".
"""

from .dsl import *  # noqa: F403

COURSE = ("biology", "form-5")

M1 = "Taxonomy & Variety of Living Organisms"
M2 = "Cell Biology & Cellular Transport"
T_CHAR = "Characteristics of living things and classification"
T_VIR = "Viruses"
T_BPF = "Bacteria, protoctists and fungi"
T_PLANT = "Kingdom Plantae"
T_INV = "Invertebrate animals"
T_VERT = "Vertebrate animals"
T_MICRO = "Microscopy and magnification"
T_CELL = "Plant and animal cell structure"
T_SPEC = "Cell specialization and organization"
T_TRANS = "Diffusion, osmosis and active transport"

LESSONS = []

# ------------------------------------------------------------------ 1. Characteristics of living things
LESSONS.append(lesson(
    module=M1,
    topic=T_CHAR,
    title="The seven characteristics of living things",
    slug="bia-characteristics-of-living-things",
    minutes=18,
    summary="Biology is the study of living things. Every living organism moves, respires, is sensitive, grows, reproduces, excretes and feeds. Learn the seven characteristics, their definitions and how to use them to decide if something is alive.",
    objectives=[
        "Define biology, organism and the seven characteristics of living things",
        "Give an example of each characteristic from plants and animals you know",
        "Use the characteristics to decide whether something is living or non-living",
        "Distinguish respiration from breathing and excretion from egestion",
    ],
    key_concepts=["Biology", "Organism", "Movement", "Respiration", "Sensitivity", "Growth", "Reproduction", "Excretion", "Nutrition"],
    blocks=[
        H("Introduction"),
        T("In a market in Bafoussam, a trader sells live tilapia from a basin of water. Next to the basin lies a pile of "
          "stones. The fish swim, breathe, react when you touch the water and one day will lay eggs. The stones do none "
          "of this. How do we know that the fish are alive and the stones are not?"),
        T("Biologists answer with a list of seven things that all living things do. In this lesson you will learn the list, "
          "what each word means exactly, and how to use it in the examination."),
        D("**Biology** is the scientific study of living things. An **organism** is a living thing, such as a mango tree, "
          "a mosquito or a human being.", title="Definitions"),
        H("The seven characteristics"),
        T("All living organisms show seven characteristics. Many students remember them with the word **MRS GREN**: "
          "Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, Nutrition."),
        KEY("Seven characteristics of living things", "Each one has an exact meaning. Learn the wording.", cards=[
            ["Movement", "An action by an organism or part of an organism that changes its position or place. A tilapia swims. A plant slowly turns its leaves towards the light."],
            ["Respiration", "The chemical reactions in cells that break down nutrient molecules to release energy."],
            ["Sensitivity", "The ability to detect changes (stimuli) in the surroundings or inside the body and to respond to them. Your eyes close when a bright light shines."],
            ["Growth", "A permanent increase in size and dry mass, by an increase in cell number, cell size, or both."],
            ["Reproduction", "The processes that make more of the same kind of organism. A hen lays eggs that hatch into chicks."],
            ["Excretion", "The removal from the body of toxic waste made by the organism's own chemical reactions, and of substances in excess of what the body needs. Humans excrete carbon dioxide and urea."],
            ["Nutrition", "Taking in materials for energy, growth and repair. Plants make their food by photosynthesis. Animals eat other organisms."],
        ]),
        TIP("Growth means a *permanent* increase. A balloon that gets bigger when you blow into it is not growing. "
            "A cassava plant that stays bigger after the rain has stopped is growing."),
        H("Using the list: living or non-living?"),
        T("Some non-living things look as if they have one or two of the characteristics. A fire spreads (it seems to "
          "grow) and uses oxygen (it seems to respire). A car moves and uses fuel. But neither shows **all seven**. "
          "Living things show all seven, even if some are hard to see, as in a tree."),
        EX("Worked example 1: is a mango tree alive?", intro="A student says that a mango tree is not alive because it never moves. Use the characteristics to answer.", steps=[
            S("Define movement", text="Movement is an action that changes the position of the organism or of a part of it."),
            S("Look for movement in the tree", text="Its leaves turn towards the light and its roots grow down. Plants move parts of the body slowly, even if they do not walk."),
            S("Check the others", text="It respires, responds to light, grows, flowers and makes seeds (reproduces), loses oxygen and water vapour as waste (excretes) and makes food by photosynthesis (nutrition)."),
            S("Conclude", text="The mango tree shows all seven characteristics, so it is a living organism."),
        ]),
        EX("Worked example 2: living or non-living?", intro="Decide whether a goat, a taxi and a seed are living, using the seven characteristics.", steps=[
            S("Goat", text="Moves, respires, senses, grows, reproduces, excretes urea and eats grass. All seven: living."),
            S("Taxi", text="It moves and its engine uses fuel with oxygen to release energy. But it does not grow, reproduce, sense or excrete in the biological way. Not living."),
            S("Seed", text="It looks still, but a living seed respires slowly and, with water, it grows (germinates) into a plant. A seed is living but resting."),
            S("Conclude", text="Goat: living. Taxi: non-living. Seed: living."),
        ]),
        CODE("""Characteristic   Example in a tilapia
Movement         swims using its tail and fins
Respiration      cells release energy from food
Sensitivity      darts away from a shadow
Growth           fry become adult fish
Reproduction     female lays eggs, male fertilises them
Excretion        removes urea and carbon dioxide
Nutrition        eats plants, insects and small animals""", "text", title="Table 1. Characteristics shown by one organism"),
        H("Two words students confuse"),
        MISTAKE("Respiration is not breathing", "Breathing (ventilation) is moving air in and out of the lungs. **Respiration** is the chemical release of energy from food inside every living cell. Plants respire but do not breathe."),
        MISTAKE("Excretion is not egestion", "Excretion removes waste made by the body's own chemical reactions (for example urea). **Egestion** is removal of food that was never absorbed (faeces). Do not write 'excretion is removing faeces'."),
        MISTAKE("Movement does not mean walking", "Plants and sessile animals such as corals also show movement of parts. Always write 'movement of the organism or of part of it'."),
        QUIZ("Which characteristic is described as 'chemical reactions in cells that release energy from nutrients'?",
             ["Excretion", "Nutrition", "Respiration", "Sensitivity"], 2,
             "Respiration is the release of energy from nutrient molecules inside cells.",
             hint="Think about where the energy for movement comes from.",
             feedback=["Excretion is removal of waste.", "Nutrition is taking in materials, not releasing energy from them.", "", "Sensitivity is detecting and responding to stimuli."]),
        QUIZ("A shopkeeper in Kumba notices that a yam left in the dark has grown long pale shoots. Which characteristic does this show?",
             ["Growth", "Excretion", "Movement only", "Egestion"], 0,
             "The shoots are a permanent increase in size and mass, which is growth.",
             hint="Is the increase permanent?",
             feedback=["", "No waste is being removed here.", "Movement changes position and does not describe a permanent increase in size.", "Egestion is removing undigested food."]),
        H("Practice"),
        PQ("State the seven characteristics of living things.", "Movement, respiration, sensitivity, growth, reproduction, excretion and nutrition (MRS GREN)."),
        PQ("Define (a) sensitivity and (b) excretion.", "(a) The ability to detect stimuli in the surroundings or inside the body and to respond to them. (b) The removal from the organism of toxic waste made by its own metabolism and of substances in excess of requirements."),
        PQ("A student says a candle flame is alive because it grows, moves and uses oxygen. Explain why this is wrong.", "A flame does not show all seven characteristics. It does not reproduce, it does not sense and respond, it does not excrete waste made by chemical reactions in cells and it has no cells. Only things that show all seven are living."),
        TIP("Exam link: this topic appears in Paper 1 (multiple choice, often as a biological term or situation) and in Paper 2 essays that ask for definitions. Learn each definition in your own clear wording and spell the words correctly: the Board reports show candidates losing marks for wrong spellings of biological terms."),
        SUM("Biology is the study of living things; an organism is a living thing.",
            "The seven characteristics are movement, respiration, sensitivity, growth, reproduction, excretion and nutrition (MRS GREN).",
            "Respiration is the release of energy in cells, not breathing; excretion is removal of metabolic waste, not egestion.",
            "A thing is alive only if it shows all seven characteristics."),
    ],
))

# ------------------------------------------------------------------ 2. Classification and binomial naming
LESSONS.append(lesson(
    module=M1,
    topic=T_CHAR,
    title="Classification and the binomial system",
    slug="bia-classification-and-binomial-system",
    minutes=22,
    summary="Living things are grouped into kingdoms, phyla, classes, orders, families, genera and species. Each species has a two-part Latin name (genus and species). Learn the ranks, the naming rules and how to use a dichotomous key.",
    objectives=[
        "Explain why organisms are classified and name the seven ranks in order",
        "Define species and list the five kingdoms",
        "Write a binomial name correctly",
        "Use a simple dichotomous key to identify organisms",
    ],
    key_concepts=["Classification", "Taxonomy", "Kingdom", "Genus", "Species", "Binomial name", "Dichotomous key"],
    blocks=[
        H("Introduction"),
        T("In a market in Buea you can ask for 'fish', but the seller needs to know if you want tilapia, catfish or mackerel. "
          "Names that everybody agrees on make life easier. Scientists face the same problem with millions of "
          "organisms. A plant called one name in Bamenda may have another name in Douala and another in England."),
        D("**Classification** is the arrangement of living things into groups according to the features they share. The "
          "study of classification is called **taxonomy**.", title="Definition: classification"),
        T("Classification makes it easier to study the huge variety of organisms. It shows how closely related they are, "
          "and it gives every organism a name that scientists everywhere understand."),
        H("The ranks of classification"),
        T("Organisms are placed in a series of groups. The largest group is a **kingdom**. Each kingdom is divided into "
          "smaller groups, and so on down to the **species**. Organisms in the same small group are very alike."),
        IMG("f5bi-a-classification-ranks.svg", alt="Table of the seven ranks kingdom, phylum, class, order, family, genus and species with the housefly and the human as examples, and an arrow showing groups getting smaller going down",
            caption="Figure 1. The seven ranks for the housefly and for humans. Both are animals, so they share the kingdom, but they differ from the phylum downwards."),
        T("A memory aid for the order: **K**ing **P**hilip **C**ame **O**ver **F**or **G**ood **S**oup (Kingdom, Phylum, Class, Order, "
          "Family, Genus, Species)."),
        D("A **species** is a group of organisms that can breed with one another and produce **fertile** offspring (offspring "
          "that can themselves reproduce).", title="Definition: species"),
        T("Horses and donkeys are different species. A horse and a donkey can produce a mule, but a mule is sterile, "
          "so it cannot start a new line. This shows why 'fertile offspring' is part of the definition."),
        KEY("The five kingdoms", "Most textbooks use five kingdoms. Viruses are not placed in any of them because they are not made of cells.", cards=[
            ["Prokaryotae (bacteria)", "Single cells with no nucleus."],
            ["Protoctista", "Mostly single-celled organisms with a nucleus, such as Amoeba, and simple algae."],
            ["Fungi", "Feed on dead or living matter and have a cell wall. Mushrooms, bread mould, yeast."],
            ["Plantae", "Make food by photosynthesis. Mango, plantain, ferns, moss."],
            ["Animalia", "Many cells, feed on other organisms, usually move. Fish, insects, humans."],
        ]),
        TIP("Some books call the first kingdom Monera and some give the number of kingdoms differently. Check your textbook for the names your teacher uses."),
        H("The binomial system"),
        T("The Swedish scientist **Carl Linnaeus** introduced a way of naming each species with two Latin words. "
          "This is the **binomial system** ('bi' means two, 'nomial' means name)."),
        D("A **binomial name** has two parts. The first is the **genus** and starts with a capital letter. The second is the "
          "**species** and starts with a small letter. The name is written in *italics* or, by hand, underlined.",
          title="Rules for the binomial name"),
        CODE("""Common name     Binomial name
human           Homo sapiens
housefly        Musca domestica
mango           Mangifera indica
Nile tilapia    Oreochromis niloticus
oil palm        Elaeis guineensis
lion            Panthera leo
leopard         Panthera pardus""", "text", title="Table 1. Some binomial names"),
        T("The lion and the leopard share the genus *Panthera*, so they are closely related. Different genera and species can "
          "have the same common name in different languages, but a binomial name belongs to one species only."),
        EX("Worked example 1: writing a binomial name", intro="The housefly belongs to the genus Musca and the species domestica. Write its binomial name correctly in an exam script.", steps=[
            S("Put the genus first", text="Genus: Musca, with a capital M."),
            S("Put the species second", text="Species: domestica, all in small letters."),
            S("Mark it as a scientific name", text="By hand, underline both words separately: Musca domestica. In print it is italic: *Musca domestica*."),
        ]),
        H("Dichotomous keys"),
        T("A **dichotomous key** identifies an organism by a series of questions, each with two answers. ('Dichotomous' means "
          "'divided in two'.) Each answer sends you to another question or to the name of the organism."),
        IMG("f5bi-a-dichotomous-key.svg", alt="Flowchart key: has jointed legs? No leads to has a shell? Yes snail, No earthworm. Yes leads to has six legs? Yes housefly, No spider",
            caption="Figure 2. A dichotomous key to four animals."),
        EX("Worked example 2: using the key", intro="An animal has jointed legs and six of them. Use Figure 2 to identify it.", steps=[
            S("Question 1: jointed legs?", text="Yes, so go to the right-hand branch."),
            S("Question 2: six legs?", text="Yes."),
            S("Identify", text="The key ends at the housefly."),
        ]),
        MISTAKE("Writing the name wrongly", "Do not write 'musca Domestica' or 'Musca Domestica'. The genus has a capital letter and the species does not. Underline or italicise **both** words."),
        MISTAKE("Mixing up species and genus", "A genus can contain many species. *Panthera* is the genus and *leo* alone is not a name; the full binomial is *Panthera leo*."),
        QUIZ("In which order do the ranks run from the largest group to the smallest?",
             ["Kingdom, class, phylum, order, family, genus, species", "Kingdom, phylum, class, order, family, genus, species", "Species, genus, family, order, class, phylum, kingdom", "Kingdom, phylum, order, class, family, genus, species"], 1,
             "The correct order is Kingdom, Phylum, Class, Order, Family, Genus, Species.",
             hint="King Philip Came Over For Good Soup.",
             feedback=["Class comes after phylum, not before.", "", "That list runs from smallest to largest.", "Order comes after class."]),
        QUIZ("Which is a correctly written binomial name?",
             ["Mangifera Indica", "mangifera indica", "Mangifera indica", "MANGIFERA indica"], 2,
             "Capital letter on the genus, small letter on the species, both italic or underlined.",
             hint="Which part gets the capital letter?",
             feedback=["The species name must start with a small letter.", "The genus must start with a capital letter.", "", "Only the first letter of the genus is a capital."]),
        H("Practice"),
        PQ("Define (a) classification and (b) species.", "(a) The arrangement of living things into groups according to the features they share. (b) A group of organisms that can breed together and produce fertile offspring."),
        PQ("List two reasons why scientists classify organisms.", "To make the study of the huge variety of living things easier; to show how closely related organisms are; to give each organism a name understood by scientists everywhere."),
        PQ("A key says: 1(a) has wings: go to 2. 1(b) no wings: go to 3. Explain why this kind of key is called dichotomous.", "Because each question has exactly two possible answers, so the group is divided in two at every step."),
        TIP("Exam link: classification ranks, the binomial rules and keys appear in Paper 1 (terms and diagrams) and may be asked in Paper 2 as a definition or by using a key. Always write the genus with a capital letter and the species with a small letter."),
        SUM("Classification groups organisms by shared features; the ranks run Kingdom, Phylum, Class, Order, Family, Genus, Species.",
            "A species is a group that can breed and produce fertile offspring.",
            "The binomial name is genus (capital) then species (small letter), italic or underlined.",
            "A dichotomous key uses paired choices to identify an organism."),
    ],
))

# ------------------------------------------------------------------ 3. Viruses
LESSONS.append(lesson(
    module=M1,
    topic=T_VIR,
    title="Viruses: structure and replication",
    slug="bia-viruses-structure-and-replication",
    minutes=22,
    summary="Viruses are tiny particles made of genetic material in a protein coat. They have no cells and can reproduce only inside a living host cell. Learn the structure of a virus, how a bacteriophage replicates and how HIV differs.",
    objectives=[
        "Describe the structure of a virus and say why viruses are not placed in a kingdom",
        "Explain why viruses can only reproduce inside host cells",
        "Outline the steps of replication of a bacteriophage",
        "Describe how HIV differs from a bacteriophage",
    ],
    key_concepts=["Virus", "Capsid", "Genetic material", "Host cell", "Bacteriophage", "HIV", "Reverse transcriptase"],
    blocks=[
        H("Introduction"),
        T("Farmers in Cameroon know cassava mosaic disease. The leaves turn yellow and twisted and the harvest is "
          "small. Doctors know measles, influenza and HIV. These very different illnesses have one thing in "
          "common: all are caused by **viruses**."),
        T("A virus is so small that it cannot be seen with a school light microscope. Viruses are usually between about 20 and 300 "
          "nanometres across, much smaller than a bacterium, which is usually a few micrometres long."),
        D("A **virus** is a very small particle made of genetic material (DNA or RNA) inside a protein coat. It has no cell "
          "structure and can reproduce only inside the living cell of another organism, called its **host**.", title="Definition: virus"),
        H("Structure of a virus"),
        T("A virus has no nucleus, no cytoplasm, no cell membrane and no organelles. It has only two basic parts."),
        KEY("Parts of a virus", "All viruses have the first two parts.", cards=[
            ["Genetic material", "DNA or RNA. It carries the instructions for making new viruses. A virus has one type only, never both."],
            ["Capsid", "A coat made of protein that surrounds and protects the genetic material."],
            ["Envelope (some viruses)", "An outer layer taken from the host cell membrane. HIV has one. Many viruses do not."],
        ]),
        T("Viruses do not feed, respire, grow or excrete on their own. They show reproduction and some features of "
          "living things only when inside a host. Biologists therefore place them outside the five kingdoms. "
          "Whether to call them living is an old argument, so say that they are on the border between living and non-living."),
        H("A bacteriophage"),
        T("A **bacteriophage** (phage) is a virus that infects bacteria. It is the standard example because its shape is easy to draw."),
        IMG("f5bi-a-phage.svg", alt="Bacteriophage with a hexagonal head containing DNA, a collar, a tail sheath, a base plate and four tail fibres",
            caption="Figure 1. A bacteriophage. The head holds the DNA. The tail fibres attach to the host."),
        H("How a bacteriophage replicates"),
        T("The steps below are called the **lytic cycle** because the host cell is destroyed ('lysis' means bursting)."),
        KEY("Replication of a phage", "Learn the five steps in order.", cards=[
            ["1. Attachment", "Tail fibres attach to the surface of a bacterium."],
            ["2. Injection", "The tail sheath contracts and the phage's DNA is injected into the bacterium. The empty coat stays outside."],
            ["3. Copying", "The viral DNA takes over the host. The bacterium's own enzymes and ribosomes copy the viral DNA and make viral protein."],
            ["4. Assembly", "New DNA and new protein coats join to form many new phages."],
            ["5. Release", "The bacterium bursts and the new phages escape to infect other bacteria."],
        ]),
        EX("Worked example 1: why can a virus not reproduce alone?", intro="Explain why a virus can reproduce only inside a host cell.", steps=[
            S("What a virus lacks", text="It has no ribosomes, no enzymes for making protein and no energy supply of its own."),
            S("What it needs", text="To make copies of its genetic material and protein coat it needs these from a living cell."),
            S("Conclude", text="So the virus must enter a host cell and use the cell's machinery to make new viruses."),
        ]),
        H("HIV"),
        T("**HIV** (human immunodeficiency virus) is an RNA virus that infects humans. HIV has an envelope with spikes, and it "
          "attaches to a kind of white blood cell, the T helper lymphocyte, which helps the body fight infection."),
        IMG("f5bi-a-hiv.svg", alt="HIV particle with spike proteins on an envelope, a capsid containing two strands of RNA and the enzyme reverse transcriptase",
            caption="Figure 2. HIV. The enzyme reverse transcriptase is carried inside the capsid."),
        T("HIV differs from a phage in an important way. Its genetic material is RNA. Inside the host cell an enzyme called "
          "**reverse transcriptase** copies the RNA into DNA. This DNA joins the host cell's DNA. The cell then makes "
          "new HIV particles, which leave and infect more cells. As the number of T helper cells falls, the body cannot fight infections well. "
          "This is AIDS (acquired immune deficiency syndrome)."),
        T("HIV passes between people through body fluids such as blood and sexual fluids, and from a mother to her baby. It "
          "is not spread by hugging, sharing a plate or mosquito bites. The control of HIV is studied in the ecology and health module."),
        EX("Worked example 2: comparing the two viruses", intro="State two differences between a bacteriophage and HIV.", steps=[
            S("Host", text="A bacteriophage infects bacteria. HIV infects human T helper lymphocytes."),
            S("Genetic material", text="The phage has DNA. HIV has RNA and uses reverse transcriptase to make DNA."),
            S("Other possible answers", text="HIV has an envelope; the phage has a head and tail."),
        ]),
        MISTAKE("Calling a virus a cell", "A virus has no cell structure. A bacterium is a living cell. Antibiotics kill bacteria but do not work on viruses."),
        MISTAKE("Saying viruses divide", "Viruses do not divide. They are made again, as separate parts, by the host cell and then assembled."),
        QUIZ("What is the function of the capsid?",
             ["To make proteins", "To protect the genetic material", "To release energy", "To digest the host cell"], 1,
             "The protein capsid surrounds and protects the DNA or RNA.",
             hint="Think of what a coat does.",
             feedback=["A virus cannot make proteins itself; it uses the host cell.", "", "Viruses do not respire.", "Digesting is not part of the virus's structure."]),
        QUIZ("Which step comes immediately after a phage injects its DNA into a bacterium?",
             ["Release of new phages", "Attachment to the bacterium", "Copying of viral DNA and making of protein", "Assembly of new phages"], 2,
             "After injection the viral DNA takes over the host cell and the host starts to make viral parts.",
             hint="Assembly needs parts to be made first.",
             feedback=["Release is the last step.", "Attachment is the first step.", "", "Assembly comes after the parts are made."]),
        H("Practice"),
        PQ("Define a virus and name its two basic parts.", "A virus is a very small particle with no cell structure that can reproduce only inside a living host cell. Its parts are genetic material (DNA or RNA) and a protein coat (capsid)."),
        PQ("Outline the replication of a bacteriophage.", "The tail fibres attach to the bacterium. The phage injects its DNA. The viral DNA takes over the bacterium, which makes new viral DNA and protein. The new parts assemble into phages. The bacterium bursts (lysis) and releases the new phages."),
        PQ("Why are antibiotics not used to treat HIV or influenza?", "Antibiotics act on bacteria, for example on their cell wall. Viruses are not cells and live inside human cells, so antibiotics do not harm them."),
        TIP("Exam link: viruses appear in Paper 1 multiple choice, often as a diagram of a phage or HIV to label, and in Paper 2 as a description of structure or replication. Spell 'bacteriophage', 'capsid' and 'reverse transcriptase' correctly."),
        SUM("A virus is genetic material in a protein coat with no cell structure.",
            "Viruses reproduce only inside living host cells and are placed outside the five kingdoms.",
            "A phage attaches, injects its DNA, makes copies using the host, assembles and bursts the host.",
            "HIV has RNA, an envelope and reverse transcriptase, and attacks T helper lymphocytes."),
    ],
))

# ------------------------------------------------------------------ 4. Bacteria, protoctists and fungi
LESSONS.append(lesson(
    module=M1,
    topic=T_BPF,
    title="Bacteria, protoctists and fungi",
    slug="bia-bacteria-protoctists-fungi",
    minutes=25,
    summary="Bacteria have cells with no nucleus. Protoctists such as Amoeba, Spirogyra and Plasmodium have a nucleus and are mostly single-celled. Fungi such as Rhizopus and yeast have hyphae or single cells and feed on dead or living matter.",
    objectives=[
        "Describe the structure of a bacterium and list its uses and harm",
        "Describe Amoeba, Spirogyra and Plasmodium and state how each feeds and reproduces",
        "Describe Rhizopus and yeast and the main features of fungi",
        "Compare the three kingdoms in a table",
    ],
    key_concepts=["Prokaryotae", "Binary fission", "Protoctista", "Pseudopodium", "Plasmodium", "Fungi", "Hypha", "Saprophyte", "Budding"],
    blocks=[
        H("Introduction"),
        T("When cooked food is left out in a Douala kitchen for a day, it smells and goes bad. A mould grows on old "
          "bread. Mosquitoes carry the cause of malaria in their saliva. Three different groups of tiny organisms are "
          "involved: bacteria, fungi and protoctists."),
        H("Kingdom Prokaryotae (bacteria)"),
        D("**Bacteria** are single-celled organisms with **no nucleus**. Their DNA lies free in the cytoplasm as a circular "
          "loop. 'Prokaryote' means 'before a nucleus'.", title="Definition: bacteria"),
        IMG("f5bi-a-bacterium.svg", alt="Rod-shaped bacterium with capsule, cell wall, cell membrane, cytoplasm, circular DNA, a plasmid, ribosomes and a flagellum",
            caption="Figure 1. A bacterium. It has no nucleus."),
        T("Bacteria have a cell wall (not made of cellulose), a cell membrane, cytoplasm with small ribosomes, a loop of DNA and, "
          "often, small rings of DNA called plasmids. Some have a slimy capsule and a whip-like flagellum for swimming. "
          "Shapes are round (cocci), rod (bacilli) and spiral or comma-shaped. They reproduce by **binary fission**: each "
          "cell copies its DNA and splits in two, which can happen every twenty minutes or so in good conditions."),
        T("Bacteria are useful: they rot dead plants and animals (decomposers), fix nitrogen in the soil and help make "
          "yoghurt. Others cause disease, such as cholera, typhoid and tuberculosis."),
        H("Kingdom Protoctista"),
        D("**Protoctists** are mostly single-celled organisms whose cells have a nucleus. A few, such as some algae, "
          "are made of many similar cells.", title="Definition: protoctists"),
        T("The three examples to know are Amoeba, Spirogyra and Plasmodium."),
        KEY("Three protoctists", "Know where each one lives and how it feeds.", cards=[
            ["Amoeba", "Lives in pond water. One cell with a nucleus, a contractile vacuole and a changing shape. It moves and feeds using false feet called pseudopodia, which surround food to make a food vacuole. It reproduces by binary fission."],
            ["Spirogyra", "A green alga of ponds. Long threads (filaments) of cells, each with a spiral chloroplast containing pyrenoids (starch stores). It makes food by photosynthesis and can reproduce by conjugation."],
            ["Plasmodium", "A parasite that lives in human red blood cells and liver. It causes malaria and is passed on by the female Anopheles mosquito."],
        ]),
        H("Kingdom Fungi"),
        D("**Fungi** are organisms with cell walls (made of chitin) and no chloroplasts. They do not make their own food. They feed on dead matter "
          "(**saprophytes**) or on living hosts (parasites) and reproduce mainly by spores.", title="Definition: fungi"),
        T("Rhizopus is the black bread mould. Its body is a network of thin threads called **hyphae**, together called a "
          "**mycelium**. Hyphae grow over the bread and release enzymes. The enzymes digest the bread outside the "
          "fungus and the dissolved food is absorbed. Upright hyphae carry a round **sporangium** that holds many spores. "
          "When it bursts, the light spores spread in the air and grow into new moulds where they land."),
        T("**Yeast** is a single-celled fungus used for making bread and alcohol. It reproduces by **budding**: a small "
          "bud grows on the parent cell and then breaks away."),
        CODE("""Feature        Bacteria        Protoctists        Fungi
Nucleus        no              yes                yes
Cell wall      yes             Spirogyra yes,     yes (chitin)
                               Amoeba no
Chloroplasts   no              Spirogyra only     no
Examples       Vibrio cholerae Amoeba, Plasmodium Rhizopus, yeast""", "text", title="Table 1. Comparing three kingdoms"),
        TIP("Textbooks differ on small details, for example how the bacterial cell wall and the protoctist groups are described. Check your textbook for the exact wording your teacher expects."),
        EX("Worked example 1: identify the organism", intro="A student sees a green thread-like organism in pond water. Under the microscope each cell has a spiral chloroplast. Name the organism and its kingdom.", steps=[
            S("Note the features", text="Green, long thread of cells, a spiral chloroplast."),
            S("Match", text="These are the features of Spirogyra."),
            S("Kingdom", text="Spirogyra is an alga in the kingdom Protoctista."),
        ]),
        EX("Worked example 2: how Rhizopus feeds", intro="Explain how Rhizopus gets its food from bread.", steps=[
            S("Hyphae spread", text="The hyphae grow over and into the bread."),
            S("Enzymes", text="They release digestive enzymes onto the bread, which break down starch into soluble sugar."),
            S("Absorption", text="The dissolved sugar is absorbed into the hyphae. This is saprophytic feeding."),
        ]),
        MISTAKE("Giving bacteria a nucleus", "A bacterium has no nucleus: its DNA is a loop in the cytoplasm. Protoctists, fungi, plants and animals have a nucleus."),
        MISTAKE("Writing that fungi photosynthesise", "Fungi have no chloroplasts. They absorb food from dead or living matter."),
        QUIZ("Which organism is a single-celled fungus that reproduces by budding?",
             ["Spirogyra", "Yeast", "Amoeba", "Rhizopus"], 1,
             "Yeast is a single-celled fungus and reproduces by budding.",
             hint="Which one is used to make bread rise?",
             feedback=["Spirogyra is a green alga (protoctist).", "", "Amoeba is a protoctist and divides by binary fission.", "Rhizopus is a fungus made of hyphae, not a single cell."]),
        QUIZ("Plasmodium is spread to people by which organism?",
             ["Female Anopheles mosquito", "Housefly", "Tsetse fly", "Cockroach"], 0,
             "The female Anopheles mosquito carries Plasmodium and passes it on when she bites.",
             hint="Think about which insect transmits malaria.",
             feedback=["", "Houseflies carry germs on their bodies but do not carry Plasmodium.", "The tsetse fly transmits sleeping sickness, a different disease.", "Cockroaches do not spread malaria."]),
        H("Practice"),
        PQ("State three features of a bacterial cell.", "Any three: cell wall; cell membrane; cytoplasm with ribosomes; DNA free in the cytoplasm (no nucleus); sometimes a capsule, plasmids or a flagellum."),
        PQ("Describe how Amoeba feeds.", "It extends pseudopodia round a food particle, enclosing it in a food vacuole. Enzymes digest the food in the vacuole and the digested food is absorbed into the cytoplasm."),
        PQ("Name the parts of Rhizopus: (a) the network of threads, (b) the structure that holds spores.", "(a) Mycelium made of hyphae. (b) Sporangium."),
        TIP("Exam link: this topic appears in Paper 1 multiple choice (diagrams of Amoeba, Spirogyra, Rhizopus or a bacterium) and in Paper 2 essays on differences between organisms. The Board's reports show candidates misspelling words such as 'pseudopodium' and 'pyrenoid': learn the spellings."),
        SUM("Bacteria are single cells with no nucleus and reproduce by binary fission.",
            "Protoctists have a nucleus: Amoeba (pseudopodia), Spirogyra (spiral chloroplast, a green alga), Plasmodium (malaria parasite).",
            "Fungi have chitin walls and no chloroplasts and feed by digesting outside the body and absorbing; Rhizopus has hyphae and a sporangium; yeast reproduces by budding.",
            "Bacteria, protoctists and fungi differ mainly in nucleus, wall and feeding."),
    ],
))

# ------------------------------------------------------------------ 5. Kingdom Plantae
LESSONS.append(lesson(
    module=M1,
    topic=T_PLANT,
    title="Kingdom Plantae: the main plant groups",
    slug="bia-plant-kingdom-groups",
    minutes=22,
    summary="Plants make their own food by photosynthesis. The kingdom is divided into bryophytes (mosses), filicinophytes (ferns), coniferophytes (cone-bearing trees) and flowering plants, which are split into monocots and dicots. Learn the features and examples of each.",
    objectives=[
        "State the features shared by all plants",
        "Describe bryophytes, filicinophytes, coniferophytes and flowering plants with examples",
        "Distinguish monocotyledons from dicotyledons using at least five features",
        "Classify Cameroonian crops as monocots or dicots",
    ],
    key_concepts=["Plantae", "Bryophyte", "Filicinophyte", "Coniferophyte", "Flowering plant", "Cotyledon", "Monocotyledon", "Dicotyledon"],
    blocks=[
        H("Introduction"),
        T("A Cameroonian farm shows great plant variety. Plantains and cocoyams grow beside maize, mango trees shade "
          "the house and moss grows on the wet wall of the well. They look very different, yet all are plants. "
          "In this lesson you will learn how plants are divided into groups."),
        D("**Plants** (kingdom Plantae) are many-celled organisms whose cells have a cell wall made of cellulose and "
          "contain chloroplasts. They make food by photosynthesis, and most do not move from place to place.", title="Definition: plants"),
        H("Four main groups"),
        T("Plants are divided by whether they have true roots, stems and leaves, and by how they reproduce. Some "
          "textbooks give groups different names, so check your textbook."),
        KEY("The plant groups", "Learn one feature and one example for each.", cards=[
            ["Bryophytes (mosses and liverworts)", "Small plants of damp, shady places. No true roots (they have thread-like rhizoids), no vascular (transport) tissue. They reproduce by spores made in a capsule on a stalk."],
            ["Filicinophytes (ferns)", "Have true roots, stems (rhizomes) and leaves called fronds. Have vascular tissue. Reproduce by spores made in sporangia on the underside of fronds. No seeds or flowers."],
            ["Coniferophytes (conifers)", "Mostly trees, such as pine and cypress, with needle-like leaves. They make seeds in cones. The seeds are not enclosed in a fruit ('naked' seeds). No flowers."],
            ["Flowering plants (angiosperms)", "Have flowers. Seeds are enclosed in a fruit that forms from the ovary. The largest group: mango, bean, maize and plantain."],
        ]),
        T("Ferns, conifers and flowering plants all have **vascular tissue**: xylem carries water up from the roots and phloem "
          "carries food made in the leaves. This lets them grow taller than mosses."),
        H("Monocots and dicots"),
        T("Flowering plants are split into two groups according to the number of seed leaves, or **cotyledons**, in the seed."),
        D("A **cotyledon** is a seed leaf that stores food or absorbs it for the embryo plant. A **monocotyledon** (monocot) seed has one "
          "cotyledon. A **dicotyledon** (dicot) seed has two.", title="Definitions: cotyledon, monocot, dicot"),
        CODE("""Feature              Monocotyledon        Dicotyledon
Cotyledons           one                  two
Leaf veins           parallel             net-like (branching)
Roots                fibrous (many equal) tap root with side roots
Vascular bundles     scattered in stem    in a ring in stem
Flower parts         in threes            in fours or fives
Examples             maize, plantain,     mango, bean, groundnut,
                     oil palm, cocoyam    cocoa, orange""", "text", title="Table 1. Monocot and dicot compared"),
        TIP("Cocoyam, plantain, banana, sugar cane and oil palm are monocots. Mango, beans, groundnuts, pawpaw, cocoa and tomato are dicots. Learn two examples of each."),
        EX("Worked example 1: classify a plant", intro="A seed has one cotyledon. The leaves have parallel veins and the roots are fibrous. Name the group and give an example.", steps=[
            S("Count cotyledons", text="One cotyledon means a monocot."),
            S("Check other features", text="Parallel veins and fibrous roots both agree with monocot."),
            S("Example", text="Maize (or plantain, cocoyam, oil palm). The group is monocotyledons within the flowering plants."),
        ]),
        EX("Worked example 2: why moss stays small", intro="Explain why a moss plant cannot grow as tall as a mango tree.", steps=[
            S("Transport tissue", text="Moss has no xylem or phloem, so water and food cannot be carried far."),
            S("Anchorage", text="It has only rhizoids, not true roots, so it cannot hold a tall plant or take water from deep in the soil."),
            S("Conclude", text="It must stay small and live in damp places."),
        ]),
        MISTAKE("Saying ferns have seeds or flowers", "Ferns reproduce by spores. Seeds are made by conifers and flowering plants only."),
        MISTAKE("Mixing up conifers and flowering plants", "Both make seeds, but the seeds of conifers are in cones and are not enclosed in a fruit. Flowering plants have flowers and fruits."),
        QUIZ("Which group of plants has no true roots and reproduces by spores?",
             ["Ferns", "Bryophytes", "Conifers", "Monocots"], 1,
             "Bryophytes (mosses) have only rhizoids and reproduce by spores.",
             hint="Ferns have true roots.",
             feedback=["Ferns have true roots, stems and fronds.", "", "Conifers have true roots and make seeds in cones.", "Monocots are flowering plants with true roots."]),
        QUIZ("A bean seed splits into two halves. A student concludes that the bean is a",
             ["monocot, because it has parallel veins", "dicot, because the seed has two cotyledons", "monocot, because it has fibrous roots", "fern, because it grows in damp soil"], 1,
             "Two seed halves are two cotyledons, so the bean is a dicot.",
             hint="Count the cotyledons.",
             feedback=["Parallel veins are a monocot feature, but the bean has net veins and two cotyledons.", "", "Beans have a tap root.", "Ferns have no seeds at all."]),
        H("Practice"),
        PQ("List three differences between monocotyledons and dicotyledons.", "Any three: monocots have one cotyledon and dicots two; monocot leaves have parallel veins and dicot leaves net veins; monocot roots are fibrous and dicots have a tap root; monocot vascular bundles are scattered and dicot bundles are in a ring; flower parts in threes and in fours or fives."),
        PQ("Name the plant group described: 'has leaves called fronds and reproduces by spores on the underside of the fronds'.", "Filicinophytes (ferns)."),
        PQ("Why do conifers belong with the seed plants but not with the flowering plants?", "They make seeds, but the seeds are in cones and are not enclosed in fruit, and they have no true flowers."),
        TIP("Exam link: plant groups and the monocot or dicot comparison appear in Paper 1 (terms, diagrams of leaves, seeds or roots) and in Paper 2 as a table of differences. Write differences as complete pairs, for example 'one cotyledon / two cotyledons'."),
        SUM("Plants have cellulose cell walls and chloroplasts and make food by photosynthesis.",
            "Bryophytes have no true roots or vascular tissue; ferns have fronds and spores; conifers have seeds in cones; flowering plants have flowers and fruits.",
            "Monocots have one cotyledon, parallel veins, fibrous roots and flower parts in threes.",
            "Dicots have two cotyledons, net veins, a tap root and flower parts in fours or fives."),
    ],
))

# ------------------------------------------------------------------ 6. Invertebrates
LESSONS.append(lesson(
    module=M1,
    topic=T_INV,
    title="Invertebrate animals: the main groups",
    slug="bia-invertebrate-groups",
    minutes=25,
    summary="Invertebrates are animals without a backbone. Learn the main features of cnidarians, flatworms, roundworms, annelids, molluscs and arthropods, and the four classes of arthropod: insects, arachnids, crustaceans and myriapods.",
    objectives=[
        "Define an invertebrate and describe the main features of six phyla",
        "Give an example of each phylum, including some that affect health in Cameroon",
        "Distinguish insects, arachnids, crustaceans and myriapods",
        "Use features to classify an unknown invertebrate",
    ],
    key_concepts=["Invertebrate", "Cnidaria", "Platyhelminthes", "Nematoda", "Annelida", "Mollusca", "Arthropoda", "Exoskeleton", "Segmented"],
    blocks=[
        H("Introduction"),
        T("In a market in Limbe a woman sells giant African land snails. Near the river a child "
          "washes with water where a small snail lives that can carry bilharzia. Earthworms enrich the garden soil "
          "and crabs and prawns are sold from the sea. All these animals have **no backbone**."),
        D("**Invertebrates** are animals that have no backbone (no vertebral column). They make up the large majority of all animal species.", title="Definition: invertebrate"),
        H("Six main phyla"),
        KEY("Phyla of invertebrates", "A phylum is the group below the kingdom.", cards=[
            ["Cnidaria", "Jellyfish, sea anemone, coral and Hydra. Soft body with two layers of cells, tentacles with stinging cells and one opening (mouth) leading to the gut. Radial symmetry."],
            ["Platyhelminthes (flatworms)", "Tapeworm, liver fluke, Schistosoma (bilharzia fluke). Flat, unsegmented body, with one opening to the gut or none. Many are parasites."],
            ["Nematoda (roundworms)", "Ascaris, hookworm and the worm that causes river blindness. Long, thin, round, unsegmented. Gut with a mouth and an anus."],
            ["Annelida (segmented worms)", "Earthworm, leech. Body divided into many rings (segments), moist skin, tiny bristles (chaetae)."],
            ["Mollusca", "Snails, slugs, mussels, octopus. Soft unsegmented body with a muscular foot. Most have a hard shell."],
            ["Arthropoda", "Insects, spiders, crabs, centipedes. Jointed legs, a hard exoskeleton made of chitin and a segmented body. The largest phylum."],
        ]),
        T("Remember the key feature of each: **stinging cells** (cnidarians), **flat** (flatworms), **round** (roundworms), "
          "**segments** (annelids), **muscular foot** (molluscs) and **jointed legs** (arthropods)."),
        H("The four classes of arthropod"),
        T("Arthropods are so numerous that they are divided into classes. Learn the number of legs and body parts."),
        CODE("""Class        Body parts              Legs          Antennae  Examples
Insecta      head, thorax, abdomen   3 pairs       1 pair    housefly, mosquito, bee
Arachnida    head-thorax, abdomen    4 pairs       none      spider, tick, scorpion
Crustacea    head-thorax, abdomen    5 or more     2 pairs   crab, prawn
Myriapoda    head and many segments  many pairs    1 pair    centipede, millipede""", "text", title="Table 1. Classes of arthropod"),
        TIP("Crustaceans vary. Some textbooks describe them as having two body parts, others as three. Check your textbook for the version your teacher uses. The sure tests are two pairs of antennae and five or more pairs of legs."),
        T("Insects are the most successful group. Most adult insects have two pairs of wings, and many are important in "
          "disease (mosquito, tsetse fly, housefly), farming (bees pollinate crops) and food spoilage (cockroach, weevil)."),
        EX("Worked example 1: classify an animal", intro="An animal has a hard shell, a soft unsegmented body and a muscular foot. Name its phylum.", steps=[
            S("List the features", text="Soft unsegmented body, muscular foot, hard shell."),
            S("Compare", text="Segments would mean annelid. Jointed legs would mean arthropod. Soft body with a muscular foot and shell is a mollusc."),
            S("Example", text="A snail. Phylum Mollusca."),
        ]),
        EX("Worked example 2: insect or arachnid?", intro="A student draws an animal with eight legs, two body parts and no antennae. Which class is it?", steps=[
            S("Count the legs", text="Eight legs is four pairs."),
            S("Check antennae and wings", text="No antennae and no wings."),
            S("Conclude", text="This is an arachnid, for example a spider. Insects have six legs and one pair of antennae."),
        ]),
        MISTAKE("Calling a spider an insect", "Spiders have eight legs and two body parts. Insects have six legs, three body parts and antennae."),
        MISTAKE("Thinking all worms are in one group", "Flatworms, roundworms and annelid worms are three different phyla. Look at the shape: flat, round or segmented."),
        QUIZ("Which phylum has a body divided into segments, bristles and a moist skin?",
             ["Platyhelminthes", "Nematoda", "Annelida", "Cnidaria"], 2,
             "Earthworms are annelids: segmented, with bristles.",
             hint="Think of an earthworm.",
             feedback=["Flatworms are not segmented.", "Roundworms are not segmented.", "", "Cnidarians have tentacles with stinging cells."]),
        QUIZ("A crab has five pairs of legs and two pairs of antennae. Which class does it belong to?",
             ["Crustacea", "Insecta", "Arachnida", "Myriapoda"], 0,
             "Five pairs of legs and two pairs of antennae are features of crustaceans.",
             hint="Insects have three pairs of legs.",
             feedback=["", "Insects have three pairs of legs and one pair of antennae.", "Arachnids have four pairs of legs and no antennae.", "Myriapods have many segments and many legs, with one pair of antennae."]),
        H("Practice"),
        PQ("Define an invertebrate and name six phyla.", "An invertebrate is an animal without a backbone. Phyla: Cnidaria, Platyhelminthes, Nematoda, Annelida, Mollusca, Arthropoda."),
        PQ("State three features of arthropods.", "Jointed legs, a hard exoskeleton (made of chitin) and a segmented body."),
        PQ("Compare an insect with an arachnid in two ways.", "Insects have three pairs of legs and arachnids four pairs; insects have antennae and arachnids have none; insects have three body parts (head, thorax, abdomen) and arachnids two."),
        TIP("Exam link: this topic appears in Paper 1 (an unknown animal described by its features, or a diagram to name) and in Paper 2 (a table comparing groups). Give the number of legs and body parts whenever you can."),
        SUM("Invertebrates are animals with no backbone; six phyla to know are Cnidaria, Platyhelminthes, Nematoda, Annelida, Mollusca and Arthropoda.",
            "Cnidarians have stinging cells; flatworms are flat; roundworms are round; annelids are segmented; molluscs have a muscular foot.",
            "Arthropods have jointed legs and a chitin exoskeleton.",
            "Insects have six legs and antennae; arachnids have eight legs and no antennae; crustaceans have five or more pairs of legs and two pairs of antennae; myriapods have many legs."),
    ],
))

# ------------------------------------------------------------------ 7. Insect life cycles
LESSONS.append(lesson(
    module=M1,
    topic=T_INV,
    title="Insect life cycles: mosquito, housefly, cockroach, butterfly and bee",
    slug="bia-insect-life-cycles",
    minutes=24,
    summary="Insects change form as they grow, which is called metamorphosis. Complete metamorphosis has four stages: egg, larva, pupa and adult (mosquito, housefly, butterfly, bee). Incomplete metamorphosis has three stages: egg, nymph and adult (cockroach).",
    objectives=[
        "Define metamorphosis and distinguish complete from incomplete metamorphosis",
        "Describe the life cycles of the mosquito, housefly, butterfly, bee and cockroach",
        "Explain how knowing a life cycle helps to control a pest or disease vector",
        "Recognise a larva, pupa and nymph from a description",
    ],
    key_concepts=["Metamorphosis", "Larva", "Pupa", "Nymph", "Complete metamorphosis", "Incomplete metamorphosis", "Vector"],
    blocks=[
        H("Introduction"),
        T("After heavy rain in Yaounde, small pools of water collect in old tyres and blocked drains. Within days these "
          "pools are full of tiny wriggling creatures. They are the young stages of mosquitoes. Understanding "
          "the life cycle of an insect is the key to controlling pests such as mosquitoes and houseflies."),
        D("**Metamorphosis** is a change in body form that happens as an insect grows from egg to adult. The young "
          "stage often looks very different from the adult.", title="Definition: metamorphosis"),
        H("Two kinds of life cycle"),
        IMG("f5bi-a-life-cycles.svg", alt="Two cycles: complete metamorphosis with four stages egg, larva, pupa, adult; incomplete metamorphosis with three stages egg, nymph, adult",
            caption="Figure 1. Complete metamorphosis (left) and incomplete metamorphosis (right)."),
        KEY("Complete and incomplete metamorphosis", "The test is whether there is a pupa.", cards=[
            ["Complete (four stages)", "Egg, larva, pupa, adult. The larva is very different from the adult. In the pupa the body is rebuilt. Examples: mosquito, housefly, butterfly, bee."],
            ["Incomplete (three stages)", "Egg, nymph, adult. The nymph looks like a small adult without wings and grows by shedding its skin (moulting). No pupa. Example: cockroach."],
        ]),
        T("A **larva** is the feeding stage of an insect with complete metamorphosis. A **pupa** is the stage in which the larva "
          "does not feed and its body changes into the adult. A **nymph** is the young stage of an insect with incomplete metamorphosis."),
        H("The mosquito"),
        T("The female lays her eggs on still water. The egg hatches into a **larva** (a wriggler) that lives in the water, "
          "feeds and comes to the surface to breathe. The larva changes into a comma-shaped **pupa** (a tumbler) that "
          "does not feed but swims. The adult then splits the pupa case and flies away from the water surface. "
          "Egg, larva and pupa are therefore **aquatic**; the adult is aerial."),
        T("Only the female bites, because she needs blood to make her eggs. The female *Anopheles* carries *Plasmodium*, the "
          "cause of malaria. A **vector** is an organism that carries and passes on a disease-causing organism."),
        T("Control: remove still water (empty tins, tyres), cover water tanks, clean drains, stock ponds with fish that eat larvae, "
          "or spread a thin film of oil on the water so that larvae and pupae cannot breathe at the surface. "
          "Insecticide-treated bed nets protect people from adults."),
        H("The housefly"),
        T("A female lays eggs on rotting waste, animal dung or damp food scraps. The eggs hatch into legless, pale **maggots** "
          "(larvae) that feed on the waste. The maggot forms a brown, hard-cased **pupa**, from which the adult fly emerges."),
        T("Houseflies land on waste and on food, so they carry germs on their feet, body hairs and mouthparts. They spread "
          "cholera, typhoid and diarrhoea. They also vomit digestive juices on food before eating it. Control: cover food, "
          "dispose of waste properly, keep latrines closed and use clean refuse bins."),
        H("The cockroach"),
        T("The female cockroach lays eggs in a small case. The **nymphs** that hatch look like small wingless adults. They moult several "
          "times and grow wings at the last moult. There is no pupa, so the cycle has three stages. Cockroaches live in "
          "warm dark places and contaminate food with their saliva and droppings."),
        H("The butterfly and the bee"),
        T("A butterfly lays eggs on a plant. The **caterpillar** (larva) hatches and eats a great deal of leaf, so caterpillars "
          "can damage crops. It then forms a **chrysalis** (pupa), and the adult butterfly emerges. Adult butterflies feed on nectar and help to pollinate flowers."),
        T("The honey bee also shows complete metamorphosis: egg, larva, pupa and adult, in cells of the wax comb. Bees live in "
          "colonies with one queen (who lays the eggs), many workers (females who gather nectar and pollen) and some males (drones). Bees pollinate crops and make honey and wax."),
        TIP("The tsetse fly is also an insect. The female does not lay eggs: she gives birth to a nearly fully grown larva that burrows and quickly forms a pupa. Tsetse flies are vectors of sleeping sickness. Check your textbook before using the tsetse fly as a life-cycle example."),
        EX("Worked example 1: which cycle?", intro="A student finds a legless pale insect on a rubbish heap. It later forms a brown case and an adult fly comes out. Name the larva and the type of metamorphosis.", steps=[
            S("Identify the stages", text="Legless pale creature that feeds: larva (a maggot). Brown case: pupa."),
            S("Check for a pupa", text="There is a pupa, so there are four stages."),
            S("Conclude", text="Complete metamorphosis. The insect is a housefly."),
        ]),
        EX("Worked example 2: control of mosquitoes", intro="Explain why draining stagnant pools helps to control malaria.", steps=[
            S("Where the young live", text="Mosquito eggs, larvae and pupae all develop in still water."),
            S("Effect of draining", text="Without water the life cycle cannot be completed, so fewer adult mosquitoes appear."),
            S("Link to malaria", text="Fewer female Anopheles mosquitoes means fewer bites and less spread of Plasmodium."),
        ]),
        MISTAKE("Saying the pupa feeds and grows", "The pupa is a resting stage. It does not feed while the body is rebuilt into the adult."),
        MISTAKE("Calling a cockroach nymph a larva", "A cockroach has no larva and no pupa. The nymph already looks like a small adult. Use 'nymph' for incomplete metamorphosis."),
        QUIZ("Which insect has incomplete metamorphosis?",
             ["Housefly", "Butterfly", "Mosquito", "Cockroach"], 3,
             "The cockroach goes from egg to nymph to adult with no pupa.",
             hint="Which one has no pupa?",
             feedback=["The housefly has maggot and pupa stages.", "The butterfly has caterpillar and chrysalis stages.", "The mosquito has larva and pupa stages.", ""]),
        QUIZ("In which place do the larva and pupa of a mosquito live?",
             ["On rotting waste", "In still water", "In bee colonies", "Under tree bark"], 1,
             "Mosquito eggs, larvae and pupae develop in still water.",
             hint="Where does a female lay her eggs?",
             feedback=["That is where housefly larvae live.", "", "That is where bees develop.", "Mosquito larvae need water."]),
        H("Practice"),
        PQ("Define metamorphosis and give one example of each type.", "Metamorphosis is a change in body form during the growth of an insect. Complete: mosquito (egg, larva, pupa, adult). Incomplete: cockroach (egg, nymph, adult)."),
        PQ("Describe the life cycle of the housefly and suggest two control measures.", "Eggs laid on rotting waste hatch into maggots (larvae). The maggots feed and form a pupa. The adult fly emerges. Control: cover food and dispose of waste correctly; keep latrines and bins closed."),
        PQ("State the difference between a larva and a nymph.", "A larva looks very different from the adult and changes into a pupa (complete metamorphosis). A nymph looks like a small adult without wings and grows by moulting, with no pupa (incomplete metamorphosis)."),
        TIP("Exam link: insect life cycles appear in Paper 1 (a diagram of stages to name) and in Paper 2 (describe a life cycle and its control). Use the exact stage names: egg, larva, pupa, adult, or egg, nymph, adult."),
        SUM("Metamorphosis is the change of form from egg to adult in an insect.",
            "Complete metamorphosis has egg, larva, pupa and adult: mosquito, housefly, butterfly and bee.",
            "Incomplete metamorphosis has egg, nymph and adult, with no pupa: cockroach.",
            "Knowing where each stage lives shows how to control pests and vectors such as mosquitoes and houseflies."),
    ],
))

# ------------------------------------------------------------------ 8. Vertebrates
LESSONS.append(lesson(
    module=M1,
    topic=T_VERT,
    title="Vertebrate animals: fish, amphibians, reptiles, birds and mammals",
    slug="bia-vertebrate-classes",
    minutes=24,
    summary="Vertebrates have a backbone. The five classes are bony fish, amphibians, reptiles, birds and mammals. Compare their skin covering, breathing organs, limbs, reproduction and body temperature.",
    objectives=[
        "Define a vertebrate and state the main features of the five classes",
        "Give examples of each class known in Cameroon",
        "Distinguish ectotherms from endotherms",
        "Use features to place an unknown vertebrate in its class",
    ],
    key_concepts=["Vertebrate", "Bony fish", "Amphibian", "Reptile", "Bird", "Mammal", "Ectotherm", "Endotherm", "Mammary gland"],
    blocks=[
        H("Introduction"),
        T("A fisherman at Limbe lands tilapia. In the swamp a frog calls. A lizard sits on a wall and a "
          "cockerel crows at dawn. A goat eats grass. All five animals have a backbone, but each belongs to a different "
          "class. Learning the features of the classes helps you to classify any vertebrate."),
        D("A **vertebrate** is an animal with a **backbone** (vertebral column) made of bones called vertebrae. The backbone "
          "protects the spinal cord.", title="Definition: vertebrate"),
        D("An **ectotherm** (cold-blooded animal) gets its body heat from the surroundings, so its body temperature changes "
          "with the temperature outside. An **endotherm** (warm-blooded animal) keeps a constant body temperature using heat made in its own body.",
          title="Definitions: ectotherm and endotherm"),
        H("The five classes"),
        CODE("""Class       Skin             Breathing           Limbs         Reproduction
Bony fish   wet scales       gills               fins          eggs laid in water
Amphibian   moist, no scales skin and lungs;     4 limbs       eggs (jelly) in water;
                             larva has gills                   tadpole -> adult
Reptile     dry, scaly       lungs               4 limbs or    leathery-shelled eggs
                                                 none (snake)  on land
Bird        feathers         lungs               2 wings,      hard-shelled eggs,
                                                 2 legs        laid in a nest
Mammal      hair or fur      lungs               4 limbs       most give birth to live
                                                 (usually)     young; feed on milk""", "text", title="Table 1. The five classes of vertebrate"),
        KEY("Extra features to remember", "These help in answering comparison questions.", cards=[
            ["Bony fish", "Ectotherms. Two-chambered heart. Lateral line senses movement in the water. A swim bladder helps buoyancy. Example: tilapia, catfish."],
            ["Amphibians", "Ectotherms. Metamorphosis from tadpole to adult. Moist skin helps gas exchange, so they live near water. Example: frog, toad."],
            ["Reptiles", "Ectotherms. Fertilisation inside the female. Eggs have leathery shells and do not dry out on land. Example: lizard, snake, crocodile, tortoise."],
            ["Birds", "Endotherms. Feathers, wings, beak with no teeth, light bones with air spaces. Four-chambered heart. Example: chicken, weaver bird."],
            ["Mammals", "Endotherms. Mammary glands, a diaphragm, hair or fur, outer ears (pinna), different types of teeth. Four-chambered heart. Example: goat, human, bat, gorilla."],
        ]),
        TIP("Textbooks differ on a few details: the heart of a reptile has three chambers in most reptiles but four in crocodiles, and a few mammals (the platypus and echidna) lay eggs. Check your textbook for how your teacher wants these exceptions stated."),
        EX("Worked example 1: place an animal in a class", intro="An animal has dry scaly skin, four legs, breathes with lungs and lays leathery eggs on land. Name its class and one example.", steps=[
            S("Skin and breathing", text="Dry scaly skin and lungs rule out fish and amphibians (moist skin)."),
            S("Eggs and legs", text="Leathery-shelled eggs on land match reptiles. Birds have feathers and hard shells."),
            S("Conclude", text="Class: reptile. Example: lizard."),
        ]),
        EX("Worked example 2: amphibian or reptile?", intro="A student says a frog is a reptile. Give two reasons why it is not.", steps=[
            S("Skin", text="A frog's skin is moist and without scales. A reptile's skin is dry and scaly."),
            S("Eggs and young", text="A frog lays jelly-covered eggs in water. The young, tadpoles, have gills and change into adults. Reptiles lay shelled eggs on land and the young look like adults."),
            S("Conclude", text="A frog is an amphibian."),
        ]),
        MISTAKE("Calling all water animals fish", "A crocodile, a frog and a whale live in or near water but are a reptile, an amphibian and a mammal. Use the features, not the habitat."),
        MISTAKE("Saying all vertebrates are warm-blooded", "Fish, amphibians and reptiles are ectotherms. Only birds and mammals are endotherms."),
        QUIZ("Which vertebrate has hair or fur, mammary glands and a diaphragm?",
             ["Bird", "Reptile", "Mammal", "Amphibian"], 2,
             "Hair or fur, milk from mammary glands and a diaphragm are mammal features.",
             hint="Which class feeds young on milk?",
             feedback=["Birds have feathers and no mammary glands.", "Reptiles have dry scales.", "", "Amphibians have moist, bare skin."]),
        QUIZ("The larva of a frog breathes by gills and lives in water. The adult breathes with lungs and skin. The frog is an example of",
             ["an amphibian", "a reptile", "a bony fish", "a mammal"], 0,
             "Amphibians have a water-living larva and a mostly land-living adult.",
             hint="Which class changes form from larva to adult?",
             feedback=["", "Reptiles do not have a tadpole stage.", "Fish keep their gills for life.", "Mammals do not have a larva."]),
        H("Practice"),
        PQ("State two features common to all five classes of vertebrate and one feature that divides them into two groups by body temperature.", "All have a backbone and a skeleton of bone or cartilage (also a brain and a spinal cord). Ectotherms: fish, amphibians and reptiles. Endotherms: birds and mammals."),
        PQ("Give two differences between a bird and a mammal.", "Birds have feathers, wings, a beak and lay hard-shelled eggs. Mammals have hair or fur, mammary glands, a diaphragm and most give birth to live young."),
        PQ("Why can reptile eggs be laid on dry land while amphibian eggs must be laid in water?", "Reptile eggs have a leathery shell that stops them drying out. Amphibian eggs have only a jelly coat and dry out on land."),
        TIP("Exam link: this topic appears in Paper 1 (a described animal to name, or terms such as ectotherm) and in Paper 2 (a table of differences between classes). Always compare in pairs, for example 'wet scales / feathers'."),
        SUM("Vertebrates have a backbone; the five classes are bony fish, amphibians, reptiles, birds and mammals.",
            "Skin: wet scales (fish), moist and bare (amphibians), dry scales (reptiles), feathers (birds), hair (mammals).",
            "Fish, amphibians and reptiles are ectotherms; birds and mammals are endotherms.",
            "Amphibians change from a gill-breathing larva to a lung-breathing adult; reptile and bird eggs have shells for life on land."),
    ],
))

# ------------------------------------------------------------------ 9. Microscopy and magnification
LESSONS.append(lesson(
    module=M2,
    topic=T_MICRO,
    title="Light and electron microscopes, and magnification calculations",
    slug="bia-microscopes-and-magnification",
    minutes=24,
    summary="Cells are too small to see with the naked eye. Compare the light microscope with the electron microscope, learn the difference between magnification and resolution and calculate magnification, actual size and image size with units.",
    objectives=[
        "Name the parts of a light microscope and state what each does",
        "Compare light and electron microscopes",
        "Distinguish magnification from resolution",
        "Calculate magnification, image size and actual size using the right units",
    ],
    key_concepts=["Light microscope", "Electron microscope", "Magnification", "Resolution", "Micrometre", "Scale bar"],
    blocks=[
        H("Introduction"),
        T("In a hospital laboratory in Douala, a technician looks at a drop of blood on a slide. With the naked eye you "
          "see only a red liquid. Through a microscope the technician sees red blood cells and, in a person with malaria, the "
          "parasites inside them. A microscope makes small things look larger and shows more detail."),
        D("**Magnification** is how many times larger the image is than the real object. **Resolution** (resolving power) is the "
          "ability to show two points that are very close together as separate points. A microscope with better resolution shows finer detail.", title="Definitions"),
        T("Magnification and resolution are different. If you enlarge a blurred photograph, it gets bigger but it does not show any "
          "more detail. A good microscope must have both."),
        H("The light microscope"),
        T("A light microscope uses visible light and glass lenses. Light from the lamp or mirror passes through a thin slide. The "
          "objective lens forms a magnified image, and the eyepiece lens magnifies it again."),
        CODE("""Part               Job
Eyepiece lens      magnifies the image again (often x10)
Objective lenses   magnify the specimen (x4, x10, x40)
Stage              holds the slide
Mirror or lamp     sends light through the specimen
Coarse focus       moves the lens quickly to bring the image into focus
Fine focus         makes the image sharp""", "text", title="Table 1. Parts of a light microscope"),
        F(r"\text{total magnification} = \text{eyepiece magnification} \times \text{objective magnification}", title="Total magnification"),
        T("Specimens are cut very thin so that light can pass through. A stain such as iodine or methylene blue can be added "
          "so that the cell parts show up. Light microscopes can show living cells in colour but cannot show very small "
          "structures inside the cell."),
        H("The electron microscope"),
        T("An electron microscope uses a beam of electrons instead of light, and magnets instead of glass lenses. Electrons "
          "have a much shorter wavelength than light, so the image has a far better resolution. It shows the inside of the "
          "cell (the **ultrastructure**) such as mitochondria, ribosomes and the structure of viruses."),
        CODE("""Feature             Light microscope        Electron microscope
Source              visible light           beam of electrons
Lenses              glass                   electromagnets
Maximum useful
magnification       about x1500             hundreds of thousands
Resolution          low (about 0.2 um)      high (about 1000 times better)
Living specimens    yes                     no (kept in a vacuum)
Image colour        coloured (stains)       black and white
Cost and size       cheap, small            very expensive, large""", "text", title="Table 2. Light and electron microscopes"),
        TIP("The figures for maximum magnification and resolution differ slightly between textbooks. Check your textbook and use the values your teacher gives. The idea matters most: the electron microscope has much greater resolution but cannot be used on living cells."),
        H("Units of size"),
        T("Cells are measured in **micrometres** (symbol µm). Parts of cells and viruses are measured in nanometres (nm)."),
        CODE("""1 mm = 1000 um          (1 millimetre = 1000 micrometres)
1 um = 1000 nm          (1 micrometre = 1000 nanometres)
So 0.02 mm = 20 um     and   1 cm = 10 000 um""", "text", title="Table 3. Converting units"),
        H("Calculating magnification"),
        F(r"\text{magnification} = \frac{\text{size of image}}{\text{actual size}}"),
        T("Rearranged, this gives two more forms. Always change both lengths to the **same unit** before you divide, and "
          "write magnification with a multiplication sign, such as ×300. Magnification has no unit."),
        F(r"\text{actual size} = \frac{\text{image size}}{\text{magnification}} \qquad \text{image size} = \text{actual size} \times \text{magnification}"),
        EX("Worked example 1: find the magnification", intro="A drawing of a cell is 45 mm long. The real cell is 150 µm long. Find the magnification.", steps=[
            S("Convert to the same unit", text="45 mm = 45 × 1000 = 45 000 µm."),
            S("Use the formula", math=r"\text{magnification} = \frac{45\,000}{150} = 300"),
            S("Write the answer", text="The magnification is ×300."),
        ], check=r"150 \times 300 = 45\,000\ \mu\text{m} = 45\ \text{mm}"),
        EX("Worked example 2: find the actual size", intro="A student's drawing of a cheek cell is 60 mm across. The drawing is at ×400 magnification. Find the actual width of the cell in micrometres.", steps=[
            S("Use the formula", math=r"\text{actual size} = \frac{60\ \text{mm}}{400} = 0.15\ \text{mm}"),
            S("Change to micrometres", math=r"0.15 \times 1000 = 150\ \mu\text{m}"),
            S("Write the answer", text="The cell is 150 µm wide."),
        ]),
        IMG("f5bi-a-scalebar.svg", alt="A rod-shaped cell with a double arrow above showing its length and a scale bar of 10 micrometres below",
            caption="Figure 1. A scale bar shows a known length. The cell is three times as long as the bar."),
        EX("Worked example 3: use a scale bar", intro="In Figure 1 the scale bar is 80 units long and represents 10 µm. The cell is 240 units long. Find the real length of the cell.", steps=[
            S("Compare with the bar", math=r"\frac{240}{80} = 3"),
            S("Multiply", math=r"3 \times 10\ \mu\text{m} = 30\ \mu\text{m}"),
        ]),
        MISTAKE("Dividing without matching the units", "If the image is in mm and the object is in µm you must convert first. Dividing 45 by 150 gives 0.3, which is wrong by a factor of 1000."),
        MISTAKE("Confusing magnification with resolution", "A higher magnification does not always mean a clearer image. Resolution is the ability to show fine detail. The electron microscope has better resolution, not only more magnification."),
        QUIZ("An eyepiece is ×10 and the objective is ×40. What is the total magnification?",
             ["×50", "×400", "×4", "×4000"], 1,
             "Multiply the two lenses: 10 × 40 = 400, so ×400.",
             hint="Total magnification is a product, not a sum.",
             feedback=["50 is the sum, but the lenses multiply their effects.", "", "That is the objective of ×4 alone.", "That would need a ×100 eyepiece."]),
        QUIZ("Which statement about the electron microscope is correct?",
             ["It can show living cells in colour", "It has a higher resolution than the light microscope", "It uses a beam of light", "It has glass lenses"], 1,
             "The electron microscope has a much higher resolution, so it shows the ultrastructure.",
             hint="Think about what the electron microscope uses instead of light.",
             feedback=["It is used on dead specimens in a vacuum and gives black and white images.", "", "It uses a beam of electrons.", "It uses electromagnets, not glass."]),
        H("Practice"),
        PQ("Give three differences between a light microscope and an electron microscope.", "Light microscope: uses light, glass lenses, can view living specimens, lower resolution. Electron microscope: uses electrons, electromagnets, specimens are dead and in a vacuum, much higher resolution and magnification, image in black and white."),
        PQ("A cell is 25 µm long. In a drawing it is 5 mm long. Calculate the magnification.", "5 mm = 5000 µm. Magnification = 5000 ÷ 25 = 200. The magnification is ×200."),
        PQ("Define magnification and resolution.", "Magnification is the number of times larger an image is than the object. Resolution is the ability of a microscope to show two close points as separate points (the amount of detail it shows)."),
        TIP("Exam link: this topic appears in Paper 1 (an image and a scale bar, or a magnification calculation) and in Paper 2 (calculate magnification of a drawing, state differences between microscopes). Always show your working, convert units and put the units in your answer. The Board's report notes that weak mathematical skills cost candidates marks in calculations."),
        SUM("Total magnification = eyepiece × objective; magnification = image size ÷ actual size.",
            "Convert both sizes to the same unit first: 1 mm = 1000 µm and 1 µm = 1000 nm.",
            "The light microscope can show living cells but has low resolution; the electron microscope shows the ultrastructure with high resolution but only on dead specimens.",
            "Resolution is the ability to show fine detail; it is not the same as magnification."),
    ],
))

# ------------------------------------------------------------------ 10. Plant and animal cell structure
LESSONS.append(lesson(
    module=M2,
    topic=T_CELL,
    title="Plant and animal cells: structure and functions of organelles",
    slug="bia-plant-and-animal-cells",
    minutes=25,
    summary="Both plant and animal cells have a nucleus, cytoplasm, cell membrane, mitochondria and ribosomes. Plant cells also have a cell wall, chloroplasts and a large permanent vacuole. Learn each organelle and its function.",
    objectives=[
        "Name and state the function of the main organelles of a cell",
        "Draw and label a typical plant cell and animal cell",
        "State four differences between plant and animal cells",
        "Link the structure of an organelle to its job",
    ],
    key_concepts=["Cell", "Organelle", "Nucleus", "Cell membrane", "Mitochondrion", "Ribosome", "Chloroplast", "Cell wall", "Vacuole"],
    blocks=[
        H("Introduction"),
        T("Look at a cassava leaf and at your own cheek. Both are made of tiny units called cells. "
          "A plant cell has a firm wall and green chloroplasts. An animal cell, such as a cheek cell, has no wall "
          "and no chloroplasts. In this lesson you will meet the parts of cells and see what each does."),
        D("A **cell** is the basic unit of structure and function of all living organisms. An **organelle** is a small structure "
          "inside a cell that has a particular job.", title="Definitions: cell and organelle"),
        H("A typical plant cell"),
        IMG("f5bi-a-plant-cell.svg", alt="Plant cell showing cell wall, cell membrane, nucleus, cytoplasm, a large vacuole, chloroplasts and mitochondria",
            caption="Figure 1. A plant cell as seen in a diagram. The large vacuole is in the centre."),
        H("A typical animal cell"),
        IMG("f5bi-a-animal-cell.svg", alt="Animal cell showing cell membrane, cytoplasm, nucleus, mitochondria and a small vacuole, and no cell wall",
            caption="Figure 2. An animal cell. It has no cell wall and no chloroplasts."),
        H("Organelles and their functions"),
        KEY("Found in both plant and animal cells", "These are found in nearly all cells.", cards=[
            ["Cell membrane", "A thin layer around the cytoplasm. It is partially permeable, so it controls which substances enter and leave the cell."],
            ["Cytoplasm", "A jelly-like fluid in which the organelles lie. Many chemical reactions of the cell take place here."],
            ["Nucleus", "Contains the DNA in the form of chromosomes. It controls the activities of the cell and is needed for cell division."],
            ["Mitochondria", "Release energy from food by aerobic respiration. Cells that need a lot of energy, such as muscle cells, have many."],
            ["Ribosomes", "Tiny structures that make proteins. Some lie free and some are on the rough endoplasmic reticulum."],
            ["Endoplasmic reticulum", "A network of membranes. The rough type has ribosomes and transports proteins; the smooth type makes lipids."],
            ["Golgi apparatus", "Stacks of flattened sacs that process and package proteins into vesicles for release from the cell."],
        ]),
        KEY("Found mostly in one type of cell", "These help you to tell plant and animal cells apart.", cards=[
            ["Cell wall (plants)", "Made of cellulose outside the cell membrane. It supports the cell and keeps its shape. It is fully permeable."],
            ["Chloroplasts (plants)", "Contain the green pigment chlorophyll. They carry out photosynthesis and store starch."],
            ["Permanent vacuole (plants)", "A large space filled with cell sap (sugars, salts and water) and surrounded by a membrane. It keeps the cell firm."],
            ["Small vacuoles (animals)", "Small, temporary spaces that hold food or water."],
            ["Centrioles (animals)", "Two small tubes near the nucleus that help in cell division."],
            ["Lysosomes (animals)", "Small sacs of digestive enzymes that break down worn-out parts and bacteria."],
        ]),
        TIP("Some textbooks list a few other differences, such as plant cells storing starch while animal cells store glycogen. Check your textbook for the list your teacher uses."),
        CODE("""Feature             Plant cell               Animal cell
Cell wall           present (cellulose)      absent
Chloroplasts        present in green parts   absent
Vacuole             one large, permanent     small and temporary
Shape               fixed, often regular     changes, often round or irregular
Carbohydrate store  starch                   glycogen
Centrioles          absent in most           present""", "text", title="Table 1. Plant and animal cells compared"),
        EX("Worked example 1: identify the cell", intro="A cell seen under the electron microscope has a cell wall, chloroplasts and a large vacuole. Is it a plant or an animal cell? Give two reasons.", steps=[
            S("List the unusual parts", text="Cell wall, chloroplasts and a large permanent vacuole."),
            S("Compare", text="Animal cells have none of these three."),
            S("Conclude", text="It is a plant cell because it has a cell wall and chloroplasts (also the large vacuole)."),
        ]),
        EX("Worked example 2: structure and function", intro="A liver cell, which uses a lot of energy, has many mitochondria. Explain why.", steps=[
            S("What mitochondria do", text="They release energy from food by aerobic respiration."),
            S("Link to the cell", text="A cell with a high energy demand needs more mitochondria to release enough energy."),
            S("Conclude", text="The many mitochondria supply the energy the liver cell needs."),
        ]),
        MISTAKE("Saying that a plant cell 'has a cell wall instead of a cell membrane'", "Plant cells have both. The membrane lies just inside the wall and controls what enters and leaves; the wall is only a support."),
        MISTAKE("Saying that the nucleus is where respiration happens", "Respiration takes place in the cytoplasm and mitochondria. The nucleus controls the cell and holds the DNA."),
        MISTAKE("Mixing up the vacuole and the cell sap", "The cell sap is the liquid; the vacuole is the space that holds it, surrounded by a membrane."),
        QUIZ("Which organelle releases energy from food by aerobic respiration?",
             ["Nucleus", "Chloroplast", "Mitochondrion", "Ribosome"], 2,
             "Mitochondria are the site of aerobic respiration.",
             hint="Think of the 'powerhouse' of the cell.",
             feedback=["The nucleus controls the cell and holds the DNA.", "Chloroplasts carry out photosynthesis.", "", "Ribosomes make proteins."]),
        QUIZ("Which feature is found in an animal cell but NOT in a plant cell?",
             ["Cell wall", "Chloroplast", "Centriole", "Cell membrane"], 2,
             "Centrioles are found in animal cells and are absent from most plant cells.",
             hint="Both cells have a membrane.",
             feedback=["The cell wall is a plant feature.", "Chloroplasts are found only in plants.", "", "Both plant and animal cells have a membrane."]),
        H("Practice"),
        PQ("State the function of (a) the nucleus, (b) ribosomes, (c) chloroplasts.", "(a) Contains DNA and controls the cell's activities. (b) Make proteins. (c) Carry out photosynthesis and contain chlorophyll."),
        PQ("List four differences between a plant cell and an animal cell.", "Plant cells have a cell wall, chloroplasts and a large permanent vacuole, and have a fixed shape; animal cells have none of these (their vacuoles are small) and have centrioles."),
        PQ("Why does the cell wall not control the movement of substances in and out of the cell?", "The cellulose cell wall is fully permeable, so substances pass through freely. The partially permeable cell membrane inside it controls what enters and leaves."),
        TIP("Exam link: cell structure appears in Paper 1 (about 13 questions in the Board's paper deal with biological diagrams, so expect labelled cells) and Paper 2 (draw and label, give functions, differences). Draw large, use sharp lines, label with straight lines that do not cross, and spell the names correctly. The Board's reports list 'nucleus' among words candidates misspell."),
        SUM("Both cells have a membrane, cytoplasm, nucleus, mitochondria and ribosomes.",
            "Functions: nucleus controls the cell; mitochondria release energy; ribosomes make proteins; chloroplasts photosynthesise; the vacuole keeps the cell firm.",
            "Plant cells also have a cellulose cell wall, chloroplasts and a large permanent vacuole.",
            "Animal cells have no wall or chloroplasts; they have small vacuoles and centrioles."),
    ],
))

# ------------------------------------------------------------------ 11. Specialization and organization
LESSONS.append(lesson(
    module=M2,
    topic=T_SPEC,
    title="Specialised cells, tissues, organs and systems",
    slug="bia-specialised-cells-tissues-organs",
    minutes=22,
    summary="Cells become specialised for particular jobs. Similar cells form a tissue, tissues form an organ, organs form an organ system and systems form an organism. Learn the adaptations of the main specialised cells in animals and plants.",
    objectives=[
        "Define cell specialisation, tissue, organ and organ system",
        "Explain how the structure of a red blood cell, sperm cell, root hair cell, palisade cell and xylem vessel suits its function",
        "Arrange the levels of organisation in order with examples",
        "Name the main organ systems and one organ in each",
    ],
    key_concepts=["Specialised cell", "Differentiation", "Tissue", "Organ", "Organ system", "Organism"],
    blocks=[
        H("Introduction"),
        T("A football team has a goalkeeper, defenders and strikers. Each player has a special job and a special skill, "
          "yet together they play one game. The body works in the same way. Your body has many kinds of cell, each "
          "with a special job, and they work together."),
        D("A **specialised cell** has a structure that is suited to one particular function. The process by which a cell "
          "becomes specialised is called **differentiation**.", title="Definition: specialised cell"),
        H("Specialised animal cells"),
        CODE("""Cell                 Function                     Adaptation
Red blood cell       carries oxygen               biconcave disc, no nucleus, full of
                                                  haemoglobin
White blood cell     fights germs                 can change shape to engulf germs
Sperm cell           fertilises the egg           tail to swim, many mitochondria,
                                                  acrosome with enzymes at the head
Egg cell (ovum)      is fertilised, gives food    large, food store in cytoplasm
Nerve cell           carries electrical messages  long fibre, branched ends
Muscle cell          contracts to cause movement  contains fibres that shorten, many
                                                  mitochondria
Ciliated cell        moves mucus in the windpipe  tiny hairs (cilia) that wave""", "text", title="Table 1. Specialised animal cells"),
        H("Specialised plant cells"),
        CODE("""Cell                 Function                     Adaptation
Root hair cell       absorbs water and minerals   long thin extension that increases
                                                  surface area
Palisade cell        photosynthesis               many chloroplasts, tall, near the
                                                  leaf's top surface
Xylem vessel         carries water and supports   long hollow tube with no cross walls,
                                                  walls strengthened with lignin
Phloem sieve tube    carries sugars               holes in the end walls (sieve plates)
Guard cell           opens and closes stomata     kidney shape, can change shape""", "text", title="Table 2. Specialised plant cells"),
        TIP("Always link the structure to the function. 'The red blood cell has no nucleus' is only half an answer. Add 'so there is more room for haemoglobin to carry oxygen'."),
        H("Levels of organisation"),
        D("A **tissue** is a group of similar cells that work together to do the same job. An **organ** is a group of different tissues that work "
          "together to do a particular job. An **organ system** is a group of organs that work together. An **organism** is a living thing made of organ systems working together.", title="Definitions"),
        CODE("""cell  ->  tissue  ->  organ  ->  organ system  ->  organism
Example in a human:
red blood cell -> blood (a tissue) -> heart -> circulatory system -> person
Example in a plant:
palisade cell -> palisade tissue -> leaf -> shoot system -> mango tree""", "text", title="Table 3. Levels of organisation"),
        KEY("Some organ systems of the human body", "Know one organ in each system.", cards=[
            ["Digestive", "Stomach, small intestine, liver."],
            ["Respiratory", "Lungs, windpipe."],
            ["Circulatory", "Heart, blood vessels."],
            ["Excretory", "Kidneys, bladder."],
            ["Nervous", "Brain, spinal cord."],
            ["Reproductive", "Ovaries, testes."],
            ["Skeletal and muscular", "Bones, muscles."],
        ]),
        T("Examples of animal tissues: muscle tissue, nervous tissue, blood and epithelial tissue, which covers surfaces and lines tubes. "
          "Examples of plant tissues: epidermis, palisade tissue, xylem and phloem. Plant organs are the root, stem, leaf and flower."),
        EX("Worked example 1: adaptation of a root hair cell", intro="Explain how a root hair cell is adapted to absorb water and mineral ions.", steps=[
            S("Structure", text="It has a long, thin extension (the root hair) that sticks out into the soil."),
            S("Effect", text="This gives a large surface area for absorbing water and dissolved ions."),
            S("Other feature", text="Its cell is thin-walled, so water enters easily, and it has many mitochondria to supply energy for active uptake of ions."),
        ]),
        EX("Worked example 2: levels of organisation", intro="Put these in order from smallest to largest: heart, cardiac muscle cell, circulatory system, human being, cardiac muscle.", steps=[
            S("Start with the cell", text="Cardiac muscle cell."),
            S("Group the cells", text="Cardiac muscle (a tissue)."),
            S("Group the tissues", text="Heart (an organ)."),
            S("Finish", text="Circulatory system (organ system), then human being (organism)."),
        ]),
        MISTAKE("Mixing up tissue and organ", "A tissue is made of one kind of cell. An organ contains several different tissues. The stomach is an organ with muscle tissue, epithelial tissue and nervous tissue."),
        MISTAKE("Calling blood an organ", "Blood is a tissue: cells in a liquid called plasma."),
        QUIZ("Which feature of a red blood cell helps it carry a lot of oxygen?",
             ["It has a large nucleus", "It contains haemoglobin and has no nucleus", "It has a long tail", "It has many chloroplasts"], 1,
             "No nucleus gives more room for haemoglobin, which carries oxygen.",
             hint="Think of what oxygen binds to.",
             feedback=["Red blood cells have no nucleus.", "", "A tail is a feature of sperm.", "Chloroplasts are found in plants."]),
        QUIZ("A group of similar cells that perform the same function is a",
             ["tissue", "organ", "system", "organism"], 0,
             "A tissue is a group of similar cells working together.",
             hint="An organ has different kinds of tissue.",
             feedback=["", "An organ is made of several tissues.", "A system is made of organs.", "An organism is the whole living thing."]),
        H("Practice"),
        PQ("Define a tissue, an organ and an organ system, with one example of each.", "Tissue: similar cells doing the same job (muscle). Organ: different tissues working together (heart). Organ system: organs working together (circulatory system: heart and blood vessels)."),
        PQ("Explain two ways in which a sperm cell is adapted for its function.", "It has a tail (flagellum) so that it can swim to the egg; many mitochondria release energy for swimming; the acrosome at the head has enzymes to digest the egg's outer layer."),
        PQ("Name two specialised plant cells and state the job of each.", "Root hair cell: absorbs water and mineral ions. Palisade cell: photosynthesis. (Also xylem: carries water and supports; guard cell: opens and closes stomata.)"),
        TIP("Exam link: this topic appears in Paper 1 (cell and organ terms, diagrams of cells) and in Paper 2 (adaptation of cells, with structure linked to function). The Board's reports show that candidates lose marks for weak definitions: learn tissue, organ and system exactly."),
        SUM("Specialised cells have a structure that suits their job; this happens by differentiation.",
            "Cells form tissues, tissues form organs, organs form organ systems and systems form the organism.",
            "Red blood cells (no nucleus, haemoglobin), sperm (tail), root hair (large surface area), palisade (many chloroplasts) and xylem (hollow tubes) are the key examples.",
            "Always link a structure to its function in the answer."),
    ],
))

# ------------------------------------------------------------------ 12. Diffusion and active transport
LESSONS.append(lesson(
    module=M2,
    topic=T_TRANS,
    title="Diffusion and active transport",
    slug="bia-diffusion-and-active-transport",
    minutes=24,
    summary="Substances move in and out of cells by diffusion, osmosis and active transport. Diffusion is the net movement of particles from high to low concentration. Active transport moves particles against the gradient and uses energy from respiration.",
    objectives=[
        "Define diffusion and active transport",
        "Describe factors that affect the rate of diffusion",
        "Calculate the surface area to volume ratio of a cube and explain why it matters",
        "Compare diffusion with active transport",
    ],
    key_concepts=["Diffusion", "Concentration gradient", "Surface area to volume ratio", "Active transport", "Carrier protein", "Partially permeable membrane"],
    blocks=[
        H("Introduction"),
        T("When someone fries fish in a compound in Bamenda, the smell reaches your house in a few minutes even without a wind. "
          "Particles of the smell spread out from the place where they are many to the place where they are few. "
          "This spreading is called **diffusion**, and it happens in living cells all the time."),
        D("**Diffusion** is the net movement of particles (molecules or ions) from a region of higher concentration to a region of "
          "lower concentration, down a concentration gradient, as a result of their random movement.", title="Definition: diffusion"),
        T("Diffusion is a **passive** process: the cell does not need to use energy. The particles have their own energy of movement. "
          "Diffusion goes on until the particles are spread evenly."),
        H("Where diffusion happens in living things"),
        KEY("Examples of diffusion", "Learn three with the direction of movement.", cards=[
            ["Oxygen into red blood cells", "Oxygen diffuses from the air in the lungs, where its concentration is high, into the blood, where it is lower."],
            ["Carbon dioxide into a leaf", "Carbon dioxide diffuses from the air into the leaf through the stomata, because it is used in photosynthesis."],
            ["Digested food in the ileum", "Glucose and amino acids diffuse from the gut into the blood when their concentration is higher in the gut."],
        ]),
        H("Factors affecting the rate of diffusion"),
        KEY("What makes diffusion faster", "A faster rate means more particles cross in a given time.", cards=[
            ["Steeper concentration gradient", "A bigger difference in concentration gives faster diffusion."],
            ["Higher temperature", "Particles move faster."],
            ["Larger surface area", "More space for particles to cross."],
            ["Shorter distance", "A thin membrane or a short path gives faster diffusion."],
            ["Smaller particles", "Small molecules diffuse faster than large ones."],
        ]),
        H("Surface area to volume ratio"),
        T("Small cells exchange substances more quickly than large ones because they have a larger **surface area compared with "
          "their volume**. Use cubes as a model: the surface area of a cube of side $s$ is $6s^2$ and its volume is $s^3$."),
        CODE("""Side of cube   Surface area   Volume   Surface area : volume
1 cm           6 cm2          1 cm3    6 : 1  = 6
2 cm           24 cm2         8 cm3    24 : 8 = 3
3 cm           54 cm2         27 cm3   54 : 27 = 2
4 cm           96 cm2         64 cm3   96 : 64 = 1.5""", "text", title="Table 1. Surface area to volume ratio of cubes"),
        T("As the cube gets bigger its ratio falls. A large cell would find it hard to get enough oxygen to its centre by diffusion. "
          "That is why cells are small, and why large organisms have special gas-exchange surfaces and a transport system."),
        EX("Worked example 1: surface area to volume ratio", intro="Calculate the surface area to volume ratio of a cube of side 5 cm.", steps=[
            S("Surface area", math=r"6 \times 5^2 = 150\ \text{cm}^2"),
            S("Volume", math=r"5^3 = 125\ \text{cm}^3"),
            S("Ratio", math=r"\frac{150}{125} = 1.2"),
        ], check=r"1.2 < 1.5 \text{ so a bigger cube has a smaller ratio}"),
        H("Active transport"),
        D("**Active transport** is the movement of particles through a cell membrane from a region of lower concentration to a "
          "region of higher concentration (against the concentration gradient), using energy from respiration.", title="Definition: active transport"),
        T("The membrane contains **carrier proteins**. A carrier picks up the particle on one side and carries it through, "
          "using energy. Cells that do active transport need many mitochondria to supply this energy."),
        KEY("Examples of active transport", "In each case the substance moves up a concentration gradient.", cards=[
            ["Root hair cells", "Take in mineral ions such as nitrate from the soil, even when the soil has a lower concentration than the cell."],
            ["Ileum", "Absorbs glucose from the gut into the blood when the gut has less glucose than the blood."],
            ["Kidney tubules", "Take glucose back from the filtrate into the blood."],
        ]),
        T("If the cell is short of oxygen, or poisoned so that respiration stops, active transport stops, but diffusion goes on. "
          "This is how scientists show that active transport needs energy."),
        CODE("""Feature              Diffusion               Active transport
Direction            high to low             low to high
Energy from cell     not needed              needed (from respiration)
Carrier proteins     not needed              needed
Stops if respiration no                      yes
is stopped?""", "text", title="Table 2. Diffusion and active transport compared"),
        EX("Worked example 2: choose the process", intro="Nitrate ions are at a concentration of 0.002 units in the soil water and 0.02 units in the root hair cell. The root hair cell still takes in nitrate. Name the process and explain.", steps=[
            S("Compare the concentrations", text="The ions move from low (0.002) to high (0.02): against the gradient."),
            S("Choose the process", text="Movement against the gradient needs energy: active transport."),
            S("Explain", text="Carrier proteins in the membrane use energy from respiration to pull the ions in."),
        ]),
        MISTAKE("Writing that diffusion needs energy from the cell", "Diffusion is passive. The particles move on their own because of their energy of movement."),
        MISTAKE("Forgetting 'net'", "Particles move in both directions. Diffusion is the **net** movement from high to low concentration. Always write 'from high to low concentration'."),
        QUIZ("Which of these is an example of active transport?",
             ["Oxygen entering the blood in the lungs", "Smell of fried fish spreading in a room", "Root hair cells absorbing nitrate ions against a concentration gradient", "Water moving in by osmosis"], 2,
             "Active transport moves ions against the gradient using energy from respiration.",
             hint="Look for movement from low to high concentration.",
             feedback=["That is diffusion down a gradient.", "That is diffusion in air.", "", "Osmosis is the passive movement of water."]),
        QUIZ("What happens to the surface area to volume ratio as a cube gets larger?",
             ["It increases", "It decreases", "It stays the same", "It becomes zero"], 1,
             "Volume grows faster than surface area, so the ratio falls (6, 3, 2, 1.5 ...).",
             hint="Compare the ratios of the 1 cm and 4 cm cubes.",
             feedback=["It decreases as the cube gets bigger.", "", "The ratio changes.", "It never reaches zero."]),
        H("Practice"),
        PQ("Define diffusion and name two factors that affect its rate.", "Diffusion is the net movement of particles from a region of higher to lower concentration, down a concentration gradient. Factors: concentration gradient, temperature, surface area, distance, size of particles."),
        PQ("Give two differences between diffusion and active transport.", "Diffusion goes from high to low concentration, needs no energy and no carriers. Active transport goes from low to high concentration, needs energy from respiration and uses carrier proteins."),
        PQ("Explain why an amoeba does not need a transport system but a large animal does.", "An amoeba is very small, so its surface area to volume ratio is large and substances reach all parts by diffusion. A large animal has a small ratio, so diffusion is too slow and a blood system is needed."),
        TIP("Exam link: diffusion and active transport appear in Paper 1 (terms, experiments, situations) and in Paper 2 (definitions, factors, comparison). Examiners expect the words 'concentration gradient', 'net' and 'energy from respiration'. Give directions: from high to low, or from low to high."),
        SUM("Diffusion is passive net movement from high to low concentration.",
            "Its rate rises with a steeper gradient, higher temperature, larger surface area and shorter distance.",
            "A larger cube has a smaller surface area to volume ratio, so large cells need transport systems.",
            "Active transport moves substances from low to high concentration using energy from respiration and carrier proteins."),
    ],
))

# ------------------------------------------------------------------ 13. Osmosis
LESSONS.append(lesson(
    module=M2,
    topic=T_TRANS,
    title="Osmosis in plant and animal cells",
    slug="bia-osmosis-in-cells",
    minutes=25,
    summary="Osmosis is the movement of water through a partially permeable membrane from a dilute to a concentrated solution. Plant cells become turgid or plasmolysed; red blood cells swell and burst (haemolysis) or shrink (crenation). Calculate percentage change in mass in potato experiments.",
    objectives=[
        "Define osmosis using water potential and a partially permeable membrane",
        "Describe what happens to plant cells and red blood cells in water and in concentrated solutions",
        "Define turgid, flaccid, plasmolysis, haemolysis and crenation",
        "Interpret potato-cylinder results and calculate percentage change in mass",
    ],
    key_concepts=["Osmosis", "Water potential", "Partially permeable membrane", "Turgid", "Flaccid", "Plasmolysis", "Haemolysis", "Crenation"],
    blocks=[
        H("Introduction"),
        T("A cook in Mokolo puts salt on slices of cucumber. After a few minutes the slices are wet and soft, although "
          "no water was added. Where did the water come from? It left the cucumber cells by osmosis."),
        D("**Osmosis** is the net movement of water molecules from a region of higher water potential (a dilute solution) to a region of "
          "lower water potential (a concentrated solution), through a partially permeable membrane.", title="Definition: osmosis"),
        T("**Water potential** is a measure of how freely water molecules can move. Pure water has the highest water potential. "
          "Adding a dissolved substance (a solute) lowers it. So a dilute solution has a higher water potential than a concentrated one. "
          "A **partially permeable membrane** lets small molecules such as water pass but stops larger ones. The cell membrane is one."),
        T("Some textbooks use the words hypotonic (more dilute), isotonic (equal) and hypertonic (more concentrated) for the solutions outside a cell. Check your textbook for the terms your teacher uses."),
        H("Osmosis in plant and animal cells"),
        IMG("f5bi-a-osmosis.svg", alt="A plant cell and a red blood cell in three conditions: water, same concentration and a concentrated solution. Plant cell turgid, flaccid, plasmolysed. Red blood cell swollen, normal, shrunken and spiky",
            caption="Figure 1. Plant cells (top) and red blood cells (bottom) in different solutions."),
        KEY("What happens to a plant cell", "A plant cell has a cellulose wall that does not stretch much.", cards=[
            ["In water or a dilute solution", "Water enters by osmosis. The vacuole swells and pushes the membrane against the wall. The cell is firm and **turgid**. The wall stops the cell bursting."],
            ["In a solution of the same concentration", "There is no net movement of water. The cell is **flaccid** (not firm)."],
            ["In a concentrated solution", "Water leaves by osmosis. The cytoplasm shrinks and the membrane pulls away from the wall. This is **plasmolysis** and the cell is plasmolysed."],
        ]),
        KEY("What happens to a red blood cell", "An animal cell has no cell wall.", cards=[
            ["In water or a dilute solution", "Water enters. The cell swells and may burst, which is called **haemolysis** (lysis)."],
            ["In a solution of the same concentration", "No net movement of water. The cell stays its normal shape."],
            ["In a concentrated solution", "Water leaves. The cell shrinks and the membrane becomes wrinkled or spiky. This is **crenation**."],
        ]),
        T("This is why a drip given to a patient must have the same concentration as the blood. Water or a very concentrated solution "
          "would damage the red blood cells."),
        H("Importance of turgor"),
        T("Turgid cells support soft plants such as young shoots and leaves. When a plant loses water faster than it takes it up, its cells "
          "become flaccid and the plant **wilts**. Watering the plant restores turgor. Stomata (guard cells) also open when their cells are turgid."),
        T("Farmers use osmosis too. Salting fish and meat draws water out of bacteria and the food by osmosis, so it keeps longer. "
          "Too much fertiliser can draw water out of roots and harm the crop."),
        H("An experiment with potato"),
        T("Cylinders of potato of equal size are weighed and placed in solutions of different concentrations. After some time they are "
          "dried gently and weighed again. A gain in mass means water entered by osmosis. A loss means water left."),
        F(r"\text{percentage change in mass} = \frac{\text{final mass} - \text{initial mass}}{\text{initial mass}} \times 100"),
        CODE("""Sucrose (mol/dm3)   Initial mass (g)   Final mass (g)   % change
0.0                 5.0              5.8              +16
0.2                 5.0              5.4              +8
0.4                 5.0              4.8              -4
0.6                 5.0              4.3              -14
0.8                 5.0              4.0              -20""", "text", title="Table 1. Potato cylinders in sucrose solutions"),
        EX("Worked example 1: percentage change", intro="A potato cylinder of mass 5.0 g has mass 4.3 g after 40 minutes in a 0.6 mol/dm3 sucrose solution. Calculate the percentage change in mass.", steps=[
            S("Find the change", math=r"4.3 - 5.0 = -0.7\ \text{g}"),
            S("Divide by the initial mass", math=r"\frac{-0.7}{5.0} = -0.14"),
            S("Multiply by 100", math=r"-0.14 \times 100 = -14\%"),
            S("Explain", text="The cylinder lost mass because water left the cells by osmosis. The sucrose solution had a lower water potential than the cells."),
        ]),
        EX("Worked example 2: estimate the concentration of the cell sap", intro="Use Table 1 to estimate the concentration of sucrose at which a potato cylinder neither gains nor loses mass.", steps=[
            S("Find where the sign changes", text="The change is +8% at 0.2 and -4% at 0.4. So 0% lies between them."),
            S("Use a straight line between the two points", math=r"0.2 + \frac{8}{8+4} \times 0.2 = 0.2 + 0.133 = 0.33\ \text{mol/dm}^3"),
            S("Explain", text="At about 0.33 mol/dm3 there is no net movement of water, so this solution has the same water potential as the potato cells."),
        ]),
        MISTAKE("Saying that water moves from a 'strong' to a 'weak' solution without using water potential", "Say that water moves from a region of higher water potential (dilute) to lower water potential (concentrated). Always mention the partially permeable membrane."),
        MISTAKE("Using 'plasmolysis' for animal cells", "Plasmolysis is for plant cells only. Animal cells in concentrated solutions show crenation, and in water they burst by haemolysis."),
        MISTAKE("Forgetting the sign in percentage change", "A loss of mass must be written with a minus sign, for example -14%."),
        QUIZ("A plant cell is placed in a very concentrated sugar solution. What happens?",
             ["It becomes turgid", "It bursts", "It becomes plasmolysed", "Nothing happens"], 2,
             "Water leaves by osmosis, so the cytoplasm shrinks and pulls away from the wall: plasmolysis.",
             hint="Which way does the water move?",
             feedback=["Turgid cells form in water, not in a concentrated solution.", "A plant cell wall prevents bursting, and water is leaving rather than entering.", "", "There is a difference in water potential, so water moves."]),
        QUIZ("Why does a red blood cell burst in pure water but a plant cell does not?",
             ["The red blood cell has more water", "The plant cell has a strong cellulose wall that resists swelling", "The plant cell has no membrane", "Red blood cells are bigger"], 1,
             "The plant cell wall is strong, so the cell becomes turgid. An animal cell has no wall.",
             hint="Which of the two has a cell wall?",
             feedback=["Water amount is not the reason.", "", "Plant cells have a membrane too.", "Size does not explain it."]),
        H("Practice"),
        PQ("Define osmosis.", "The net movement of water molecules from a region of higher water potential to a region of lower water potential through a partially permeable membrane."),
        PQ("Explain why a lettuce leaf placed in water becomes crisp but a leaf placed in strong salt solution becomes limp.", "In water, water enters the cells by osmosis, so they become turgid and the leaf is firm. In strong salt solution, water leaves the cells by osmosis, the cells become flaccid or plasmolysed and the leaf is limp."),
        PQ("A potato cylinder has an initial mass of 4.0 g and a final mass of 4.6 g. Calculate the percentage change in mass.", "Change = 4.6 - 4.0 = 0.6 g. Percentage change = 0.6 ÷ 4.0 × 100 = +15%."),
        TIP("Exam link: osmosis appears in Paper 1 (diagrams of cells in different solutions, situations and experiments) and in Paper 2 (definitions, describing and explaining experiments, calculations and graphs). The Board's reports note that candidates lose marks for poor use of terms and for weak calculations. Write 'water potential' and 'partially permeable membrane' in your definition."),
        SUM("Osmosis is the net movement of water from higher to lower water potential through a partially permeable membrane.",
            "Plant cells become turgid in water and plasmolysed in concentrated solutions; the wall stops them bursting.",
            "Red blood cells burst (haemolysis) in water and shrink with spiky edges (crenation) in concentrated solutions.",
            "Percentage change in mass = (final - initial) ÷ initial × 100, with a sign."),
    ],
))
