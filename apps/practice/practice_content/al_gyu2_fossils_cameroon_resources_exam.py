"""A Level Geology (0755), Upper Sixth: practice sets for Systematic Palaeontology, Stratigraphy & Regional Geology
of Cameroon, Economic, Petroleum, Hydro- & Engineering Geology and the Examination module.

One 8-question set per lesson (15 topic lessons, 3 examination lessons), plus 'Paper 1 mock exam A' (50 multiple-choice
questions across all five Upper Sixth modules in proportion to their topic counts: 7, 7, 6, 5 and 4 topics give 12,
12, 10, 9 and 7 questions) and 'Paper 2 practice paper A' (25 auto-markable parts in 8 numbered questions). Geology has
no Paper 3 mock: the Paper 3 lesson and its set cover practical skills. Exam facts are only those of the Board's 2023
subject report. Mock timings (90 and 150 minutes) are KKEVO practice settings, not Board settings. Facts about the
geology of Cameroon are hedged as in the lessons. Numerical answers were checked by script.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("geology", "upper-sixth")

M_SED = "Sedimentology & Sedimentary Petrology"
M_STRU = "Structural Geology & Geological Map Work"
M_PAL = "Systematic Palaeontology"
M_STR = "Stratigraphy & Regional Geology of Cameroon"
M_ECO = "Economic, Petroleum, Hydro- & Engineering Geology"
M_EXAM = "Examination"

T_TAPH = "Fossilization and taphonomy"
T_TRIL = "Trilobites and graptolites"
T_BRAC = "Brachiopods and bivalves"
T_GAST = "Gastropods and cephalopods"
T_ECHI = "Echinoids and corals"
T_MICR = "Microfossils, plants and vertebrates"
T_PRIN = "Principles of stratigraphy"
T_PREC = "The Precambrian basement of Cameroon"
T_PANA = "The Pan-African fold belt"
T_BASN = "Sedimentary basins of Cameroon"
T_CVL = "The Cameroon Volcanic Line"
T_ORE = "Ore deposits"
T_PET = "Petroleum geology"
T_HYD = "Hydrogeology"
T_ENG = "Engineering geology"

# Topics of the other writer's modules (exact titles, used as mock concepts)
T_HJUL = "Sediment transport and the Hjulström diagram"
T_GRAIN = "Grain size analysis"
T_SSTR = "Sedimentary structures"
T_DIAG = "Diagenesis"
T_SILI = "Siliciclastic rocks"
T_CARB = "Carbonate rocks"
T_EVAP = "Evaporites and carbonaceous rocks"
T_STRS = "Stress and strain"
T_BRIT = "Brittle and ductile deformation"
T_FOLD = "Folds"
T_FALT = "Faults and shear zones"
T_CLEA = "Cleavage and foliation"
T_STRC = "Stratum contours and three-point problems"
T_XSEC = "Geological cross-sections"


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

TRIL_Q = "algyu2-trilobite-q.svg"
TRIL_ALT = "Dorsal view of a trilobite with eight parts marked P to W: P head shield, Q raised centre of the head, R oval on the cheek, S dashed line across the cheek, T spine at the head corner, U side of a thorax segment, V centre of the thorax, W tail shield"
SUT_Q = "algyu2-sutures-q.svg"
SUT_ALT = "Four cephalopod suture lines labelled A to D: A is gently curved, B is an angular zigzag with smooth sides, C has smooth rounded saddles and finely toothed lobes, D is finely frilled throughout"
RANGE = "algyu2-rangechart.svg"
RANGE_ALT = "Range chart: beds 1 (oldest) to 10 (youngest) with the ranges of five species. A from bed 1 to 6, B from 4 to 9, C from 2 to 4, D from 7 to 10, E from 5 to 7"
SUP_Q = "algyu2-supergene-q.svg"
SUP_ALT = "Vertical profile through a weathered copper deposit divided into zones 1 to 5 from top to bottom, with downward arrows in zones 2 and 3 and a dashed water table between zones 3 and 4"
TRAP_Q = "algyu2-traps-q.svg"
TRAP_ALT = "Four petroleum traps A to D, oil in green: A oil at the crest of an arched sandstone under shale; B tilted sandstone cut by a fault; C upturned beds against a column of salt; D sandstone wedge thinning out within shale"

# ------------------------------------------------------------------ 1. Fossilization and taphonomy
V1 = [
    Q("What is taphonomy?", "The study of what happens to an organism from death until it is found as a fossil",
      [("The classification and naming of fossil organisms", "That is taxonomy."), ("The use of fossils to date and correlate rocks", "That is biostratigraphy."), ("The study of fossil tracks and burrows only", "That is ichnology, the study of trace fossils.")],
      [("Definition", "Taphonomy covers decay, disarticulation, transport, burial and diagenesis.")], "Definition of taphonomy", "Recall", "Think of the path from death to fossil."),
    Q("Which mode of preservation keeps the original material but fills its pores with new minerals?", "Permineralization",
      [("Replacement", "In replacement the original material is dissolved and replaced."), ("Carbonization", "Carbonization leaves only a carbon film."), ("An external mould", "A mould is an impression; the original material has gone.")],
      [("Petrified wood", "Silica fills the cells of the wood while the cell walls remain: permineralization.")], "Modes of preservation", "Recall", "Is the original material still there?"),
    Q("A shale contains thin black films in the shape of leaves. How are they preserved?", "By carbonization",
      [("By pyritization", "Pyritization would give brassy pyrite, not black films of carbon."), ("As casts", "A cast is a three-dimensional filling of a hollow."), ("As unaltered remains", "The leaf tissue has lost its volatile parts.")],
      [("Carbon film", "Volatile parts were driven off, leaving a thin carbon residue.")], "Modes of preservation", "Application", "What colour is carbon?"),
    Q("Which organism has the HIGHEST preservation potential?", "A thick-shelled oyster living on a muddy shallow sea floor",
      [("A worm living in sand on a beach", "It has no hard parts."), ("An insect living in a forest", "Land organisms are rarely buried and insects decay fast."), ("A jellyfish drifting in the open sea", "It has no hard parts and lives where little sediment accumulates.")],
      [("Factors", "Hard calcite shell, abundant, in a place where sediment accumulates.")], "Preservation potential", "Reasoning", "Combine hard parts with habitat."),
    Q("A bed contains bivalves with both valves joined, in burrowing position, with all sizes present. This is:", "A life assemblage preserved where the animals lived",
      [("A death assemblage transported by currents", "Transport separates valves and sorts sizes."), ("A Lagerstätte of soft-bodied animals", "Bivalve shells are hard parts; nothing suggests soft-part preservation."), ("A trace-fossil assemblage", "These are body fossils.")],
      [("Evidence", "Articulated valves, life position and mixed sizes show no transport.")], "Life and death assemblages", "Interpretation", "Were the shells moved?"),
    Q("Why do Lagerstätten such as the Burgess Shale matter to palaeontologists?", "They preserve soft-bodied organisms, showing how much of past life is normally lost",
      [("They are the main source of zone fossils", "Zone fossils come from ordinary rocks with common hard-shelled fossils."), ("They contain only unaltered shells", "Their special feature is soft-part preservation."), ("They show that all organisms fossilize easily", "They show the opposite: preservation of soft parts is exceptional.")],
      [("Exceptional preservation", "Rapid burial in anoxic conditions stopped decay and scavenging.")], "Lagerstätten", "Concept", "What is unusual about them?"),
    Q("Pyritized fossils are found in a black shale. What does this suggest about the environment?", "Reducing (oxygen-poor) bottom conditions",
      [("A warm, clear, shallow reef", "Reefs are well oxygenated."), ("A desert with wind-blown sand", "Pyrite forms in reducing, water-saturated sediment."), ("A glacial environment", "Pyrite says nothing about cold.")],
      [("Pyrite", "Iron sulphide forms where sulphate-reducing bacteria work in the absence of oxygen.")], "Fossils as environmental indicators", "Interpretation", "Pyrite forms without oxygen."),
    Q("Which rank lies between order and genus in the Linnaean hierarchy?", "Family",
      [("Class", "Class lies above order."), ("Species", "Species lies below genus."), ("Phylum", "Phylum lies above class.")],
      [("Order", "Kingdom, phylum, class, order, family, genus, species.")], "Taxonomy", "Recall", "Recite the ranks in order."),
]
SETS.append(practice_set(module=M_PAL, topic=T_TAPH, title="Taphonomy, preservation and assemblages", lesson="gyu2-fossilization-taphonomy", questions=build(V1, 201)))

# ------------------------------------------------------------------ 2. Trilobites and graptolites
V2 = [
    Q("In the diagram, which letter marks the glabella?", "Q",
      [("P", "P marks the head shield as a whole (cephalon)."), ("R", "R marks the eye."), ("W", "W marks the tail shield (pygidium).")],
      [("Glabella", "The raised central part of the cephalon, over the stomach.")], "Trilobite morphology", "Recall", "Look for the raised central part of the head.", diagram=TRIL_Q, alt=TRIL_ALT),
    Q("In the diagram, the dashed line S was a line of weakness. What was its function?", "It split during moulting so the animal could leave its exoskeleton",
      [("It carried the nerves to the eyes", "It is a suture in the exoskeleton, not a nerve."), ("It allowed the animal to enrol", "Enrolment used the joints of the thorax."), ("It marked the edge of the gut", "The gut lay under the glabella.")],
      [("Facial suture", "Moulting split the cephalon along the facial suture.")], "Trilobite morphology", "Concept", "What did a growing arthropod have to do?", diagram=TRIL_Q, alt=TRIL_ALT),
    Q("A trilobite is blind, has a smooth convex shield and a broad pitted fringe. Its most likely mode of life is:", "Burrowing or sitting on soft mud as a deposit feeder",
      [("Active swimming predator", "Predators had large eyes."), ("Pelagic drifting in surface waters", "Pelagic forms usually had large eyes and spiny bodies."), ("Attached to rock by a stalk", "Trilobites were not attached.")],
      [("Functional morphology", "No eyes and a smooth shield suit life in mud; the fringe spread the weight.")], "Trilobite modes of life", "Application", "What does the lack of eyes suggest?"),
    Q("What is the range of the trilobites?", "Cambrian to Permian",
      [("Ordovician to Silurian", "That is the main range of graptoloids."), ("Cambrian to Recent", "Trilobites became extinct at the end of the Permian."), ("Devonian to Cretaceous", "That is the range of the ammonoids.")],
      [("Range", "They appear early in the Cambrian and die out in the end-Permian extinction.")], "Trilobite range", "Recall", "They disappeared in the greatest mass extinction."),
    Q("Graptolites belong to which phylum?", "Hemichordata",
      [("Cnidaria", "Corals are cnidarians; graptolites are not corals."), ("Arthropoda", "Trilobites are arthropods."), ("Bryophyta", "Graptolites are animals, not mosses.")],
      [("Affinity", "Graptolites were colonial hemichordates related to living pterobranchs.")], "Graptolite morphology", "Recall", "They are related to living pterobranchs."),
    Q("Which order of graptolite forms is correct, from oldest to youngest?", "Many-stiped dendroid, four-stiped, two-stiped, biserial, uniserial",
      [("Uniserial, biserial, two-stiped, four-stiped, dendroid", "That is youngest to oldest."), ("Two-stiped, dendroid, uniserial, four-stiped, biserial", "The trend is a reduction in stipe number."), ("Biserial, uniserial, dendroid, two-stiped, four-stiped", "Uniserial monograptids are Silurian, the latest.")],
      [("Trend", "Stipe number fell through the Ordovician; biserial then uniserial forms followed.")], "Graptolite evolution", "Recall", "Stipe number decreased through time."),
    Q("A black shale contains abundant uniserial graptolites with thecae on one side. What is its most likely age?", "Silurian",
      [("Cambrian", "Graptoloids appear at the start of the Ordovician."), ("Carboniferous", "Graptoloids were extinct by then."), ("Jurassic", "Graptolites were long extinct.")],
      [("Monograptids", "Uniserial Monograptus-type graptolites are typical of the Silurian.")], "Graptolites as zone fossils", "Application", "Which forms are the youngest graptoloids?"),
    Q("Why are graptolites rarely found in limestones and sandstones?", "Their organic skeletons are preserved mainly as carbon films in quiet, anoxic muds",
      [("They lived only in fresh water", "They were marine and planktonic."), ("They had heavy calcite skeletons that dissolved", "Their skeleton was organic, not calcite."), ("They lived only on land", "They were marine.")],
      [("Preservation", "Oxygenated, high-energy settings destroyed the organic colonies.")], "Graptolite preservation", "Reasoning", "What were they made of?"),
]
SETS.append(practice_set(module=M_PAL, topic=T_TRIL, title="Trilobite and graptolite morphology and dating", lesson="gyu2-trilobites-graptolites", questions=build(V2, 202)))

# ------------------------------------------------------------------ 3. Brachiopods and bivalves
V3 = [
    Q("Where is the plane of symmetry in a brachiopod?", "Through each valve, from the beak to the front margin",
      [("Between the two valves along the hinge", "That is the bivalve plane."), ("There is no plane of symmetry", "Brachiopods are bilaterally symmetrical."), ("Parallel to the commissure", "The plane cuts through both valves at right angles to the commissure.")],
      [("Symmetry", "Each brachiopod valve is symmetrical; the two valves differ.")], "Brachiopod vs bivalve symmetry", "Recall", "Is each valve symmetrical on its own?"),
    Q("Which structure fixed most brachiopods to the sea floor?", "The pedicle, passing through the foramen",
      [("The byssus", "Byssal threads attach some bivalves such as mussels."), ("The lophophore", "The lophophore is the feeding organ."), ("The adductor muscle", "Adductor muscles close the shell.")],
      [("Pedicle", "A fleshy stalk through a hole in the pedicle valve.")], "Brachiopod morphology", "Recall", "Which valve has the hole?"),
    Q("A bivalve shows a deep pallial sinus and a posterior gape. It was most likely:", "A deep burrower with long siphons",
      [("A cemented oyster", "Oysters have no siphons and no sinus."), ("A free-swimming scallop", "Scallops have no deep sinus."), ("A byssally attached mussel", "Mussels lack a deep pallial sinus.")],
      [("Pallial sinus", "The sinus marks the muscles that withdrew long siphons; the gape let them stay out.")], "Bivalve modes of life", "Application", "What do siphons allow a buried animal to do?"),
    Q("Which feature is found in articulate brachiopods but not in inarticulate ones?", "Teeth and sockets forming a hinge",
      [("A shell of two valves", "All brachiopods have two valves."), ("A lophophore", "All brachiopods feed with a lophophore."), ("A pedicle", "Many inarticulates, such as Lingula, have a pedicle.")],
      [("Articulation", "Articulates hinge with teeth and sockets; inarticulates are held only by muscles.")], "Brachiopod morphology", "Recall", "What does 'articulate' mean?"),
    Q("A thin, flat bivalve with 'ears' beside the hinge most probably:", "Swam by clapping its valves",
      [("Burrowed deeply in mud", "Deep burrowers are elongated with a pallial sinus."), ("Was cemented to rock", "Cemented forms are thick and irregular."), ("Bored into wood", "Borers have rasping ridges.")],
      [("Pecten", "Scallops are light and flat for swimming.")], "Bivalve modes of life", "Application", "Light and flat shells suit which activity?"),
    Q("Why is a folded (zigzag) commissure an advantage to a brachiopod in muddy water?", "It separates inflowing and outflowing currents and screens out sediment grains",
      [("It makes the shell heavier so it sinks", "The fold is about feeding currents, not weight."), ("It lets the animal swim", "Brachiopods did not swim."), ("It is where the pedicle emerges", "The pedicle passes through the foramen near the beak.")],
      [("Function", "A long narrow zigzag gape filters out grains while letting water in.")], "Brachiopod functional morphology", "Reasoning", "Think about water entering the shell."),
    Q("What change in shelf faunas followed the end-Permian mass extinction?", "Bivalves replaced brachiopods as the dominant shelled animals",
      [("Brachiopods became more diverse than ever", "Most brachiopod groups were lost."), ("Trilobites recovered and dominated", "Trilobites became extinct."), ("Graptolites replaced bivalves", "Graptoloids had died out in the Devonian.")],
      [("Change of the guard", "Brachiopods dominated the Palaeozoic; bivalves the Mesozoic and Cenozoic.")], "Brachiopod and bivalve history", "Recall", "Which group dominates modern shelves?"),
    Q("Which statement about Lingula is correct?", "It is an inarticulate brachiopod that burrows in mud and has existed since the Cambrian",
      [("It is a bivalve that swims", "Lingula is a brachiopod."), ("It is an articulate brachiopod of the Carboniferous only", "It is inarticulate and lives today."), ("It is a cemented oyster", "It is a brachiopod.")],
      [("Living fossil", "Lingula has changed little since the Cambrian.")], "Brachiopod examples", "Recall", "It is called a living fossil."),
]
SETS.append(practice_set(module=M_PAL, topic=T_BRAC, title="Brachiopod and bivalve symmetry and modes of life", lesson="gyu2-brachiopods-bivalves", questions=build(V3, 203)))

# ------------------------------------------------------------------ 4. Gastropods and cephalopods
V4 = [
    Q("In the diagram, which suture is ceratitic?", "C",
      [("A", "A is a gently curved nautiloid suture."), ("B", "B is an angular goniatitic suture with smooth sides."), ("D", "D is frilled throughout: ammonitic.")],
      [("Ceratitic", "Smooth rounded saddles with finely toothed lobes.")], "Suture types", "Interpretation", "Which line has smooth saddles but frilled lobes?", diagram=SUT_Q, alt=SUT_ALT),
    Q("A fossil shows suture D of the diagram. What is its most likely age?", "Jurassic or Cretaceous",
      [("Cambrian", "Ammonoids appear in the Devonian."), ("Devonian to Permian only", "That range fits goniatitic sutures."), ("Eocene", "Ammonoids died out at the end of the Cretaceous.")],
      [("Ammonitic suture", "Fully frilled sutures are typical of Jurassic and Cretaceous ammonites.")], "Suture types", "Application", "Which group has the most complex sutures?", diagram=SUT_Q, alt=SUT_ALT),
    Q("What is the function of the siphuncle?", "To control the gas and liquid in the chambers and so the buoyancy",
      [("To carry food to the mouth", "Food was taken by the tentacles."), ("To attach the shell to the sea floor", "Cephalopods swam."), ("To hold the gills", "The gills were in the body chamber.")],
      [("Buoyancy", "Liquid was removed or added through the siphuncle.")], "Cephalopod morphology", "Recall", "Why does the shell have chambers?"),
    Q("Where is the siphuncle in an ammonoid?", "Along the outer (ventral) margin of the whorl",
      [("At the centre of the septa", "A central siphuncle is typical of nautiloids."), ("Inside the body chamber only", "It passes through all the chambers."), ("In the aperture", "The aperture is the opening of the body chamber.")],
      [("Position", "A marginal (ventral) siphuncle separates ammonoids from most nautiloids.")], "Nautiloids vs ammonoids", "Recall", "Central or marginal?"),
    Q("A gastropod has a long siphonal canal at the base of its aperture. This suggests:", "A carnivore or scavenger that used a siphon to sense prey",
      [("A herbivore grazing algae on rocks", "Grazers usually have an entire aperture."), ("A filter feeder attached by a stalk", "Gastropods are not attached by stalks."), ("A swimming cephalopod", "Gastropods have no chambered shell.")],
      [("Siphonal canal", "The canal held a siphon that drew water over a chemical sense organ.")], "Gastropod morphology", "Application", "What did the siphon do?"),
    Q("Which feature distinguishes a coiled ammonite from a coiled gastropod?", "The ammonite is coiled in one plane and divided into chambers by septa",
      [("The ammonite has an aperture", "Both have an aperture."), ("The gastropod is made of calcium carbonate", "Both are calcium carbonate."), ("The gastropod has septa", "Gastropods have no internal septa.")],
      [("Coiling and septa", "Gastropods coil helically and are undivided; ammonites are planispiral and chambered.")], "Gastropods vs cephalopods", "Concept", "Section the shell: what do you see?"),
    Q("What part of a belemnite is most often found as a fossil?", "The solid calcite guard (rostrum)",
      [("The ink sac", "Soft parts are rarely preserved."), ("The external coiled shell", "Belemnites had an internal skeleton and were not coiled."), ("The tentacle hooks only", "Hooks are rare finds; the guard is common.")],
      [("Guard", "Dense, radiating calcite fibres give it a high preservation potential.")], "Belemnites", "Recall", "Which part is dense calcite?"),
    Q("Why are ammonites excellent zone fossils?", "They evolved rapidly, were widespread swimmers, abundant and easy to identify",
      [("They lived for a very long time unchanged", "Long-ranging fossils are poor zone fossils."), ("They lived only in one small sea", "They were widespread."), ("They are found in all continental rocks", "They are marine.")],
      [("Criteria", "Short ranges plus wide distribution give fine, correlatable zones.")], "Ammonites as zone fossils", "Reasoning", "List the qualities of a good zone fossil."),
]
SETS.append(practice_set(module=M_PAL, topic=T_GAST, title="Gastropod shells, cephalopod sutures and belemnites", lesson="gyu2-gastropods-cephalopods", questions=build(V4, 204)))

# ------------------------------------------------------------------ 5. Echinoids and corals
V5 = [
    Q("Which statement describes a regular echinoid?", "Five-fold symmetry with the periproct inside the apical system",
      [("Bilateral symmetry with the periproct at the back", "That describes an irregular echinoid."), ("Septa arranged in multiples of six", "Septa belong to corals."), ("A pedicle valve and a brachial valve", "That describes a brachiopod.")],
      [("Regular echinoid", "Pentameral symmetry, periproct on top in the apical system, mouth central below.")], "Regular and irregular echinoids", "Recall", "Where is the anus?"),
    Q("Why did irregular echinoids such as Micraster develop petaloid ambulacra and move the periproct to the back?", "As adaptations to burrowing in sediment",
      [("As adaptations to grazing on rocks", "Grazers are regular echinoids."), ("To attach to the sea floor", "Echinoids are not attached."), ("To swim in open water", "Irregular echinoids burrowed.")],
      [("Infaunal life", "Waste is left behind as the animal moves forward; petals serve respiration in the burrow.")], "Echinoid adaptations", "Reasoning", "Where did heart urchins live?"),
    Q("Which coral order is always colonial, with prominent tabulae and reduced or absent septa?", "Tabulate",
      [("Rugose", "Rugose corals have well-developed septa and may be solitary."), ("Scleractinian", "Scleractinians have hexameral septa."), ("Hermatypic", "That describes reef-building corals, not an order.")],
      [("Tabulate", "For example Favosites and Halysites.")], "Coral orders", "Recall", "The name comes from the tabulae."),
    Q("What is the range of scleractinian corals?", "Middle Triassic to Recent",
      [("Ordovician to Permian", "That is the range of rugose and tabulate corals."), ("Cambrian to Silurian", "No coral order has this range."), ("Cretaceous only", "They live today.")],
      [("Range", "Scleractinians appear after the end-Permian extinction.")], "Coral orders", "Recall", "Modern reef corals belong here."),
    Q("A fossil reef of colonial corals indicates which environment?", "Warm, clear, shallow marine water of normal salinity",
      [("Shallow marine water of any temperature", "Reef corals need warm water; 'shallow marine' alone is incomplete."), ("Deep, cold, dark water", "Reef corals need light for their algae."), ("Fresh-water lakes", "Corals are marine.")],
      [("Conditions", "Symbiotic algae need light; corals need warmth, clear water and normal salinity.")], "Corals as environmental indicators", "Application", "Give all the adjectives."),
    N("A Devonian coral shows 2 000 daily growth ridges in 5 annual bands (invented teaching figures). How many days were there in the year?", 400,
      [("Divide", "2 000 ÷ 5 = 400 days.")], "Coral growth lines", "Calculation", "Divide the ridges by the number of years.", tol=0.5, unit="days"),
    N("Using 400 days in a year and a year of 8 766 hours, calculate the length of a Devonian day in hours.", 21.9,
      [("Divide", "8 766 ÷ 400 = 21.9 hours.")], "Coral growth lines", "Calculation", "Share the hours of a year among the days.", tol=0.1, unit="hours"),
    Q("How are the septa inserted in a rugose coral?", "In four places, giving a bilateral arrangement",
      [("In cycles of six, giving radial symmetry", "That is scleractinian."), ("They are absent", "That is typical of tabulate corals."), ("In pairs across a single plane", "Rugose insertion is in four quadrants.")],
      [("Rugose", "After six protosepta, new septa are added in four places.")], "Coral orders", "Recall", "Rugose corals are also called tetracorals."),
]
SETS.append(practice_set(module=M_PAL, topic=T_ECHI, title="Echinoids, coral orders and coral clocks", lesson="gyu2-echinoids-corals", questions=build(V5, 205)))

# ------------------------------------------------------------------ 6. Microfossils, plants and vertebrates
V6 = [
    Q("Why are microfossils used to date rocks in oil wells?", "They survive whole in drill cuttings and are abundant",
      [("They are larger than macrofossils", "They are microscopic."), ("They are found only in oil", "They are found in sedimentary rocks, not in the oil itself."), ("They never change through time", "They evolved quickly, which is why they date rocks.")],
      [("Cuttings", "A drill bit grinds rock into chips; only tiny fossils survive intact.")], "Microfossils in the oil industry", "Reasoning", "What happens to a large fossil during drilling?"),
    Q("Which microfossils have siliceous skeletons?", "Radiolaria and diatoms",
      [("Foraminifera and coccoliths", "These are mainly calcareous."), ("Conodonts and ostracods", "Conodonts are phosphatic; ostracods calcareous."), ("Spores and pollen", "These have organic walls.")],
      [("Silica", "Radiolaria and diatoms form siliceous oozes and cherts.")], "Microfossil groups", "Recall", "Which form cherts?"),
    Q("Most of the Cretaceous Chalk is made of:", "Coccoliths",
      [("Radiolaria", "Radiolaria are siliceous."), ("Conodonts", "Conodonts are rare phosphatic elements."), ("Nummulites", "Nummulites are Eocene larger forams.")],
      [("Chalk", "Chalk is a fine limestone of coccolith plates.")], "Microfossil groups", "Recall", "Tiny calcite plates of algae."),
    Q("Why is the colour of conodonts and spores useful to petroleum geologists?", "It darkens with heating and shows whether the rock reached the oil window",
      [("It shows the salinity of the water", "Salinity comes from ostracods and forams."), ("It gives the absolute age in years", "Colour shows heating, not age."), ("It shows the direction of current flow", "Colour has nothing to do with currents.")],
      [("Thermal maturity", "Colour change records the maximum temperature reached.")], "Microfossils in the oil industry", "Concept", "What changes their colour?"),
    Q("Which plant has diamond-shaped leaf scars in a spiral and formed Carboniferous coal swamps?", "Lepidodendron",
      [("Calamites", "Calamites has a jointed, ribbed stem."), ("Glossopteris", "Glossopteris is a Permian seed fern with tongue-shaped leaves."), ("Sigillaria", "Sigillaria has leaf scars in vertical rows.")],
      [("Lepidodendron", "A giant lycopod with spiral diamond leaf scars.")], "Plant fossils", "Recall", "Diamond and spiral."),
    Q("The distribution of Glossopteris in Permian rocks of South America, Africa, India, Antarctica and Australia is evidence for:", "The former union of these continents in Gondwana",
      [("Global cooling at the end of the Cretaceous", "Wrong age and topic."), ("The evolution of flowering plants", "Glossopteris is a seed fern."), ("Marine transgression", "It is a land plant.")],
      [("Distribution", "Its seeds could not cross oceans.")], "Plant fossils", "Application", "How could one plant reach five continents?"),
    Q("Which fossil is usually given as a transitional form between reptiles and birds?", "Archaeopteryx",
      [("Glossopteris", "A plant."), ("Micraster", "An echinoid."), ("Paradoxides", "A trilobite.")],
      [("Archaeopteryx", "Late Jurassic, with feathers and also teeth, claws and a bony tail.")], "Vertebrate fossils", "Recall", "Late Jurassic, feathered."),
    Q("Long periods of no change broken by rapid change in small isolated populations describes:", "Punctuated equilibrium",
      [("Phyletic gradualism", "Gradualism expects slow continuous change."), ("Uniformitarianism", "That is a principle about present processes explaining the past."), ("Faunal succession", "That is the order of fossils in rocks.")],
      [("Model", "Proposed by Eldredge and Gould in 1972.")], "Evolution in the fossil record", "Recall", "Stasis then a burst."),
]
SETS.append(practice_set(module=M_PAL, topic=T_MICR, title="Microfossils, plants, vertebrates and evolution", lesson="gyu2-microfossils-plants-vertebrates", questions=build(V6, 206)))

# ------------------------------------------------------------------ 7. Principles of stratigraphy
V7 = [
    Q("Which of these is a lithostratigraphic unit?", "A formation",
      [("A stage", "A stage is a chronostratigraphic unit."), ("A biozone", "A biozone is biostratigraphic."), ("An epoch", "An epoch is a unit of time.")],
      [("Lithostratigraphy", "Group, formation, member and bed are defined by rock type.")], "Kinds of stratigraphic unit", "Recall", "Which is defined by rock type?"),
    Q("The rock deposited during the Jurassic Period is called the Jurassic:", "System",
      [("Era", "An era is a unit of time larger than a period."), ("Epoch", "An epoch is a time unit within a period."), ("Formation", "A formation is lithostratigraphic.")],
      [("Matching units", "Period (time) matches system (rock).")], "Chronostratigraphy and geochronology", "Recall", "Period is to time as ... is to rock."),
    Q("In the range chart, which beds form the concurrent-range zone of species A and B?", "Beds 4 to 6",
      [("Beds 1 to 9", "That is the combined range, not the overlap."), ("Beds 7 to 9", "A is absent above bed 6."), ("Beds 1 to 3", "B is absent below bed 4.")],
      [("Overlap", "A: 1 to 6; B: 4 to 9; overlap 4 to 6.")], "Biozones and range charts", "Interpretation", "Find where both bars are present.", diagram=RANGE, alt=RANGE_ALT),
    Q("Using the range chart, a sample contains species D and E only. Which bed did it come from?", "Bed 7",
      [("Bed 5", "Bed 5 would also contain A and B."), ("Bed 9", "E is absent above bed 7."), ("Bed 10", "E is absent in bed 10.")],
      [("D", "7 to 10."), ("E", "5 to 7."), ("Both", "Only bed 7 contains both; B also ranges into bed 7, so a sample with only D and E suggests B was not preserved, but bed 7 is the only possible bed.")], "Biozones and range charts", "Interpretation", "Where do the D and E bars overlap?", diagram=RANGE, alt=RANGE_ALT),
    Q("A vertical sequence passes upward from beach sandstone to offshore shale to shelf limestone. Using Walther's law, this records:", "A marine transgression",
      [("A marine regression", "A regression would place nearshore facies over offshore ones."), ("An angular unconformity", "The beds are a conformable facies succession."), ("Folding of the beds", "Facies changes do not show folding.")],
      [("Walther's law", "Deeper-water facies on top of shallower ones means the sea advanced.")], "Facies and Walther's law", "Interpretation", "Is the water getting deeper upwards?"),
    N("A mineral has a daughter-to-parent ratio of 7. How many half-lives have passed?", 3,
      [("Fraction left", "Parent = 1/(1 + 7) = 1/8 of the original."), ("Half-lives", "(1/2)³ = 1/8, so 3 half-lives.")], "Radiometric dating", "Calculation", "What fraction of the parent is left?"),
    N("A zircon has a Pb-206 to U-238 ratio of 0.5. Using a half-life of 4 470 million years, calculate its age in millions of years.", 2615,
      [("Formula", "t = (4 470 ÷ 0.693) × ln(1.5)."), ("Evaluate", "6 449 × 0.405 ≈ 2 615 million years.")], "Radiometric dating", "Calculation", "Use t = (t½ ÷ ln 2) × ln(1 + D/P).", tol=15, unit="million years"),
    Q("Why can K-Ar ages of a reheated granite be too young?", "Argon is a gas and escapes when the mineral is heated, resetting the clock",
      [("Potassium is added by weathering", "Weathering usually removes potassium."), ("The half-life of K-40 changes with temperature", "Half-lives are constant."), ("Calcium-40 is too rare to measure", "The problem is argon loss; calcium is too common, not rare.")],
      [("Argon loss", "Losing daughter atoms lowers D/P, giving a younger age.")], "Radiometric dating", "Reasoning", "What kind of element is argon?"),
]
SETS.append(practice_set(module=M_STR, topic=T_PRIN, title="Stratigraphic units, biozones and radiometric ages", lesson="gyu2-stratigraphy-principles", questions=build(V7, 207)))

# ------------------------------------------------------------------ 8. The Precambrian basement of Cameroon
V8 = [
    Q("What is a craton?", "An old, thick, stable part of a continent not strongly deformed for a very long time",
      [("A young mountain belt at a plate boundary", "That is an orogenic (mobile) belt."), ("A sedimentary basin of the Cretaceous", "Basins are younger and subsiding."), ("A chain of intraplate volcanoes", "That describes the Cameroon Volcanic Line.")],
      [("Craton", "Stable since the Precambrian; exposed parts are shields.")], "Craton, shield and mobile belt", "Recall", "Think stable and old."),
    Q("The Ntem Complex of southern Cameroon is part of which craton?", "The Congo Craton",
      [("The West African Craton", "That lies to the north-west, in West Africa."), ("The Kaapvaal Craton", "That is in southern Africa."), ("The São Francisco Craton", "That is in Brazil.")],
      [("Location", "The Ntem Complex is the north-western part of the Congo Craton.")], "The Ntem Complex", "Recall", "It continues into Gabon and the Congo."),
    Q("What is a charnockite?", "A granitic rock containing orthopyroxene, formed at granulite-facies temperatures",
      [("A sedimentary iron formation", "That is a BIF."), ("A low-grade green volcanic schist", "That describes greenstone rocks."), ("A dolerite dyke", "Dolerite is a basic igneous rock.")],
      [("Charnockite", "Orthopyroxene (hypersthene) is the key mineral.")], "Archaean rock types", "Recall", "Which mineral makes it special?"),
    Q("TTG gneisses are typical of Archaean crust. What do the letters stand for?", "Tonalite, trondhjemite and granodiorite",
      [("Tuff, tillite and greywacke", "These are not the TTG suite."), ("Trachyte, tephrite and gabbro", "These are volcanic and basic rocks."), ("Talc, tremolite and garnet", "These are minerals.")],
      [("TTG", "Sodium-rich granitoid gneisses formed by melting of hydrated basaltic crust.")], "Archaean rock types", "Recall", "They are sodic granitoids."),
    Q("Why are banded iron formations mostly older than about 1.8 billion years?", "Iron could stay dissolved only in oxygen-poor oceans",
      [("Iron did not exist before then", "Iron has existed since the Earth formed."), ("They formed only by volcanic eruptions", "BIFs are chemical sediments."), ("Later BIFs were all eroded", "The change reflects ocean and atmosphere chemistry.")],
      [("Oxygen", "Once oceans contained free oxygen, iron precipitated quickly and could not build BIFs widely.")], "Banded iron formations", "Reasoning", "What happens to Fe2+ in oxygenated water?"),
    Q("Which iron ore prospect of south-eastern Cameroon is commonly cited in banded iron formations of the craton?", "Mbalam",
      [("Minim-Martap", "That is commonly cited for bauxite."), ("Figuil", "That is commonly cited for limestone."), ("Bétaré-Oya", "That is commonly cited for gold.")],
      [("Hedged fact", "Mbalam is the commonly cited iron prospect; check your textbook.")], "Resources of the basement", "Recall", "Iron, not aluminium or gold."),
    Q("The Nyong unit at the north-west margin of the Ntem Complex is best described as:", "Archaean crust reworked with Palaeoproterozoic rocks in the Eburnean orogeny",
      [("Cretaceous rift sediments", "The Nyong unit is Precambrian."), ("Cenozoic alkaline volcanoes", "That describes the Cameroon Volcanic Line."), ("Undeformed Archaean charnockites", "It was deformed and metamorphosed again.")],
      [("Eburnean", "About 2 billion years ago (check your textbook).")], "The Nyong unit", "Recall", "When was it reworked?"),
    Q("A greenstone belt is mainly made of:", "Metamorphosed volcanic rocks (basaltic and ultramafic) and sediments at low grade",
      [("Fresh granite", "Granite is not green and is not volcanic."), ("Cretaceous sandstones", "Greenstone belts are Precambrian."), ("Coal and evaporites", "These are sedimentary rocks of younger basins.")],
      [("Colour", "Chlorite, epidote and actinolite give the green colour.")], "Archaean rock types", "Recall", "Why are they green?"),
]
SETS.append(practice_set(module=M_STR, topic=T_PREC, title="The Congo Craton, Ntem Complex and Nyong unit", lesson="gyu2-precambrian-basement-cameroon", questions=build(V8, 208)))

# ------------------------------------------------------------------ 9. The Pan-African fold belt
V9 = [
    Q("Which supercontinent was assembled during the Pan-African orogeny?", "Gondwana",
      [("Pangaea", "Pangaea was assembled later, in the late Palaeozoic."), ("Rodinia", "Rodinia broke up before the Pan-African collisions."), ("Laurasia", "Laurasia was the northern part of Pangaea.")],
      [("Gondwana", "Pan-African collisions joined Africa, South America and other blocks.")], "The Pan-African orogeny", "Recall", "Africa and South America were joined in it."),
    Q("Roughly when did the Pan-African orogeny take place?", "About 650 to 550 million years ago",
      [("About 3 billion years ago", "That is the age of the Ntem Complex."), ("About 2 billion years ago", "That is the Eburnean orogeny."), ("About 100 million years ago", "That is the Cretaceous rifting.")],
      [("Age", "Late Neoproterozoic to Early Cambrian; check your textbook for exact values.")], "The Pan-African orogeny", "Recall", "Late Neoproterozoic."),
    Q("In which direction were the Yaoundé nappes thrust?", "Southward, onto the Congo Craton",
      [("Northward, onto the West African Craton", "They were thrust towards the craton to the south."), ("Westward into the Atlantic", "The Atlantic did not exist then."), ("They were not thrust", "They are nappes, moved on thrusts.")],
      [("Foreland", "The rigid craton acted as the foreland; nappes moved over it.")], "Nappes of the Yaoundé domain", "Recall", "Where is the craton?"),
    Q("What does the presence of garnet-kyanite gneisses and granulites in the Yaoundé domain indicate?", "Burial to great depth at high pressure during collision",
      [("Shallow contact metamorphism near a lava flow", "Kyanite indicates high pressure."), ("Deposition in a desert", "These are metamorphic rocks."), ("Low-grade burial metamorphism", "Granulites are high grade.")],
      [("Index minerals", "Kyanite and granulite assemblages need high pressure and temperature.")], "Nappes of the Yaoundé domain", "Interpretation", "Kyanite is a high-pressure mineral."),
    Q("What kind of movement is usually given for the Central Cameroon Shear Zone?", "Dextral (right-lateral) strike-slip",
      [("Normal faulting with downthrow to the south", "It is mainly strike-slip."), ("Sinistral reverse faulting", "It is usually described as dextral."), ("No movement; it is a bedding plane", "It is a major shear zone.")],
      [("CCSZ", "Roughly ENE-WSW (about N70°E), mainly dextral; check your textbook.")], "Shear zones", "Recall", "Right-lateral."),
    Q("Which rock forms in the core of a ductile shear zone?", "Mylonite",
      [("Fault breccia", "Breccia forms by brittle faulting near the surface."), ("Hornfels", "Hornfels forms by contact metamorphism."), ("Tillite", "Tillite is a glacial sediment.")],
      [("Mylonite", "Fine-grained, strongly foliated and lineated, from ductile grain-size reduction.")], "Shear zones", "Recall", "Ductile, not brittle."),
    Q("A granite cuts across the foliation of a gneiss and contains foliated gneiss xenoliths, but is itself unfoliated. It is:", "Post-tectonic",
      [("Syn-tectonic", "A syn-tectonic granite would share the foliation."), ("Pre-tectonic", "A pre-tectonic granite would be deformed and foliated."), ("Archaean basement", "Its relationships show it is younger than the deformation.")],
      [("Relative age", "Cross-cutting and inclusions show it is younger than the fabric.")], "Syn- and post-tectonic granites", "Reasoning", "Is the granite deformed?"),
    Q("Why was the Congo Craton not strongly deformed by the Pan-African orogeny?", "It was old, cold, thick and strong, so it acted as a rigid foreland",
      [("It had not yet formed", "It is Archaean, much older."), ("It was under the ocean", "Being under water would not protect it from collision."), ("It was made of soft sediment", "Cratons are crystalline and strong.")],
      [("Rheology", "A thick, cold lithospheric root resists deformation.")], "The Pan-African orogeny", "Reasoning", "Old crust is strong crust."),
]
SETS.append(practice_set(module=M_STR, topic=T_PANA, title="Pan-African collision, nappes and shear zones", lesson="gyu2-pan-african-fold-belt", questions=build(V9, 209)))

# ------------------------------------------------------------------ 10. Sedimentary basins of Cameroon
V10 = [
    Q("What event formed the Cretaceous sedimentary basins of Cameroon?", "The break-up of Gondwana and the opening of the South Atlantic",
      [("The Pan-African collision", "That was Neoproterozoic and built a fold belt."), ("The Eburnean orogeny", "That was Palaeoproterozoic."), ("The eruption of Mount Cameroon", "Volcanism did not create the basins.")],
      [("Rifting", "Stretching of the lithosphere created rift and passive-margin basins.")], "Origin of the basins", "Recall", "Which ocean opened in the Cretaceous?"),
    Q("Which basin lies next to Nigeria and has produced most of Cameroon's oil?", "Rio del Rey basin",
      [("Mamfe basin", "Mamfe is an inland continental rift."), ("Garoua basin", "Garoua is an inland rift in the North."), ("Lake Chad basin", "It lies in the Far North.")],
      [("Rio del Rey", "The eastern edge of the Niger Delta system.")], "The basins of Cameroon", "Recall", "Coastal, in the far west."),
    Q("The Garoua and Mamfe basins are best described as:", "Inland Cretaceous rifts linked to the Benue Trough, with mainly continental fill",
      [("Passive margins with thick marine fill", "That describes the coastal basins."), ("Precambrian greenstone belts", "They are Cretaceous."), ("Volcanic calderas", "They are sedimentary basins.")],
      [("Failed rifts", "They never became oceans.")], "The basins of Cameroon", "Recall", "Inland and continental."),
    Q("Wedge-shaped units that thicken towards normal faults were deposited:", "While the faults were active (syn-rift)",
      [("After faulting stopped (post-rift)", "Post-rift units drape the faults with even thickness."), ("Before any faulting (pre-rift)", "Pre-rift units have even thickness cut by the faults."), ("During the Pan-African orogeny", "The basins are Cretaceous.")],
      [("Growth", "Faster subsidence next to the fault gave thicker sediment there.")], "Syn-rift and post-rift fill", "Interpretation", "Why would a unit thicken towards a fault?"),
    Q("What causes the slow subsidence of a passive margin after rifting stops?", "Cooling and contraction of the stretched lithosphere",
      [("Subduction of the ocean floor", "There is no subduction at a passive margin."), ("Uplift by a mantle plume", "That would cause uplift, not subsidence."), ("Folding by collision", "Passive margins are not in collision.")],
      [("Thermal subsidence", "Cooling makes the lithosphere denser, so it sinks.")], "Passive margins", "Concept", "What happens to hot rock as it cools?"),
    N("A post-rift sequence 2 400 m thick accumulated over 40 million years (invented figures). Calculate the average sedimentation rate in m per million years.", 60,
      [("Divide", "2 400 ÷ 40 = 60 m per million years.")], "Sedimentation rates", "Calculation", "Thickness ÷ time.", tol=0.5, unit="m per million years"),
    Q("Why is a calculated sedimentation rate from a modern thickness an underestimate of the true rate of deposition?", "Compaction has thinned the sediment and gaps in deposition are included in the time",
      [("Sediment expands after burial", "Sediment compacts, it does not expand."), ("Radiometric ages are always too old", "That is not the reason."), ("Erosion adds thickness", "Erosion removes thickness.")],
      [("Compaction and gaps", "Original thickness was greater, and pauses lengthen the time.")], "Sedimentation rates", "Reasoning", "What happens to mud when it is buried?"),
    Q("Old Pan-African shear zones influenced the Cretaceous rifts because:", "They were zones of weakness that were reactivated when the lithosphere was stretched",
      [("They contained oil", "Shear zones are crystalline basement structures."), ("They were volcanic vents", "They are deformation zones."), ("They were younger than the rifts", "They are much older.")],
      [("Reactivation", "Rifts often follow pre-existing weaknesses.")], "Origin of the basins", "Reasoning", "Old structures are weak."),
]
SETS.append(practice_set(module=M_STR, topic=T_BASN, title="Rifts, passive margins and Cameroon's basins", lesson="gyu2-sedimentary-basins-cameroon", questions=build(V10, 210)))

# ------------------------------------------------------------------ 11. The Cameroon Volcanic Line
V11 = [
    Q("What is the approximate length and trend of the Cameroon Volcanic Line?", "About 1 600 km, trending about N30°E",
      [("About 160 km, trending east-west", "It is ten times longer and trends north-east."), ("About 1 600 km, trending north-west", "It trends north-east."), ("About 6 000 km, trending north-south", "Too long, and the wrong trend.")],
      [("Facts", "From Annobón to the Lake Chad area, roughly N30°E.")], "Extent and trend of the CVL", "Recall", "From the Gulf of Guinea towards Lake Chad."),
    Q("What makes the CVL unusual among volcanic chains?", "It crosses the continent-ocean boundary with the same kind of volcanism on both",
      [("It lies on a subduction zone", "It is intraplate."), ("It is a mid-ocean ridge", "It is not a spreading centre."), ("Its volcanoes are all extinct", "Mount Cameroon is active.")],
      [("Setting", "Similar alkaline volcanism on oceanic and continental lithosphere.")], "Extent and trend of the CVL", "Concept", "Where does it lie relative to the coast?"),
    Q("Which rock suite is typical of the CVL?", "Alkali basalts, basanites, trachytes and phonolites",
      [("Calc-alkaline andesites and dacites", "These are typical of subduction zones."), ("Tholeiitic mid-ocean ridge basalts only", "The CVL is alkaline."), ("Komatiites and greenstones", "These are Archaean.")],
      [("Alkaline", "Rich in sodium and potassium; evolved by fractional crystallization.")], "Rocks of the CVL", "Recall", "Rich in alkalis."),
    Q("Mantle peridotite xenoliths in CVL basalts show that:", "The magma rose quickly from the mantle",
      [("The magma formed in the crust", "Mantle xenoliths come from the mantle."), ("The basalt cooled slowly at depth", "They indicate rapid ascent."), ("The volcano is a subduction volcano", "They do not indicate subduction.")],
      [("Rapid ascent", "Dense xenoliths would sink in a slow-rising magma.")], "Rocks of the CVL", "Reasoning", "Dense fragments in a rising liquid."),
    N("A plate moves at 3 cm per year over a fixed plume for 20 million years. How long, in km, would the hotspot track be?", 600,
      [("Convert", "0.03 m per year × 20 000 000 years = 600 000 m."), ("km", "600 km.")], "Origin of the CVL", "Calculation", "Distance = speed × time; watch the units.", tol=1, unit="km"),
    Q("Which observation is the strongest argument against a simple hotspot origin for the CVL?", "There is no steady age progression along the line",
      [("Its lavas are alkaline", "Many hotspot lavas are alkaline."), ("It contains crater lakes", "Crater lakes do not test the model."), ("It contains trachytes", "Trachytes form by fractionation at many hotspots.")],
      [("Age pattern", "A plate moving over a plume should give ages increasing in one direction.")], "Origin of the CVL", "Reasoning", "What does a hotspot track look like?"),
    Q("What killed about 1 700 people near Lake Nyos in 1986?", "A sudden release of carbon dioxide from the lake's deep water",
      [("A lava flow from Mount Cameroon", "Mount Cameroon is far from Lake Nyos and no lava was involved."), ("An earthquake that collapsed houses", "The deaths were by suffocation."), ("Volcanic ash that buried villages", "There was no ash fall.")],
      [("Limnic eruption", "Dense CO2 flowed down valleys and suffocated people and animals.")], "Hazards of the CVL", "Recall", "Which gas is denser than air?"),
    Q("Which measure has been used since 2001 to reduce the risk at Lake Nyos?", "Pipes that degas the bottom water slowly",
      [("Filling the lake with soil", "That is not the method used."), ("Building a lava barrier", "There is no lava hazard at the lake."), ("Adding lime to neutralize the water", "The method is controlled degassing.")],
      [("Degassing", "Gas-rich water is brought up in a pipe and the gas escapes gradually.")], "Hazards of the CVL", "Recall", "Remove the gas before it builds up."),
]
SETS.append(practice_set(module=M_STR, topic=T_CVL, title="CVL extent, rocks, origin and hazards", lesson="gyu2-cameroon-volcanic-line", questions=build(V11, 211)))

# ------------------------------------------------------------------ 12. Ore deposits
V12 = [
    Q("What is the cut-off grade of an ore deposit?", "The lowest grade that can be mined at a profit",
      [("The highest grade found in the deposit", "The cut-off is a minimum, not a maximum."), ("The average crustal abundance of the metal", "That is the denominator of the concentration factor."), ("The percentage of metal recovered in the plant", "That is the recovery.")],
      [("Definition", "Below the cut-off grade, mining costs more than the metal is worth.")], "Ore, grade and cut-off grade", "Recall", "Think about profit."),
    N("Average crustal abundance of copper is 0.005%. An ore contains 0.6% copper. Calculate the concentration factor.", 120,
      [("Formula", "Concentration factor = ore grade ÷ crustal abundance."), ("Calculate", "0.6 ÷ 0.005 = 120.")], "Concentration factor", "Calculation", "Divide the ore grade by the crustal abundance.", tol=0.5),
    N("A deposit holds 3 million tonnes of ore at 2% copper. The plant recovers 90% of the copper. How many tonnes of copper are produced?", 54000,
      [("Metal in ore", "3 000 000 × 0.02 = 60 000 t."), ("Recovered", "60 000 × 0.90 = 54 000 t.")], "Grade and tonnage", "Calculation", "Find the metal in the ore first, then apply the recovery.", tol=10, unit="tonnes"),
    Q("Layers of chromite at the base of an ultrabasic intrusion are an example of:", "Magmatic segregation by crystal settling",
      [("A hydrothermal vein deposit", "Veins form from hot fluids in fractures."), ("A placer deposit", "Placers form in rivers and on beaches."), ("Supergene enrichment", "That is a weathering process.")],
      [("Settling", "Dense early crystals sink and accumulate in layers.")], "Magmatic ore deposits", "Recall", "Which process happens inside the magma?"),
    Q("Tin and tungsten minerals in altered granite, produced by fluorine-rich fluids, are typical of:", "Greisen deposits",
      [("Porphyry copper deposits", "Porphyry deposits are mainly copper and molybdenum."), ("Banded iron formations", "BIFs are iron-rich chemical sediments."), ("Bauxite", "Bauxite is a residual aluminium deposit.")],
      [("Greisen", "Fluorine- and boron-rich fluids alter granite and deposit cassiterite and wolframite.")], "Hydrothermal ore deposits", "Recall", "Which deposit is altered granite?"),
    Q("In the profile, which zone is the zone of supergene enrichment?", "Zone 4",
      [("Zone 1", "Zone 1 is the gossan, a leached iron-oxide cap."), ("Zone 3", "Zone 3 is above the water table, where copper is removed."), ("Zone 5", "Zone 5 is the unaltered primary ore.")],
      [("Position", "Copper is redeposited at and just below the water table.")], "Supergene enrichment", "Interpretation", "Where does the dissolved copper stop moving down?", diagram=SUP_Q, alt=SUP_ALT),
    Q("Why does a gossan have a red-brown colour?", "It is made of iron oxides left behind after copper and sulphur were leached out",
      [("It is made of copper sulphides", "Copper sulphides are in the enriched zone."), ("It is made of bauxite", "Bauxite is an aluminium ore."), ("It is a lava flow", "A gossan is a weathered cap.")],
      [("Residue", "Oxidation of pyrite and chalcopyrite leaves iron oxides at the surface.")], "Supergene enrichment", "Concept", "What stays behind when copper is carried away?"),
    Q("Gold is concentrated in river gravels because it is:", "Dense and chemically unreactive, so it survives weathering and settles quickly",
      [("Light, so it floats to the surface", "Gold is very dense."), ("Soluble, so it precipitates in the river", "Gold is chemically inert."), ("Magnetic, so it sticks to iron minerals", "Gold is not magnetic.")],
      [("Placer", "Heavy, resistant minerals settle first where the flow slows.")], "Placer deposits", "Reasoning", "Why does a gold pan work?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_ORE, title="Ore processes, grade and supergene enrichment", lesson="gyu2-ore-deposits", questions=build(V12, 212)))

# ------------------------------------------------------------------ 13. Petroleum geology
V13 = [
    Q("Which rock is the typical source rock for petroleum?", "An organic-rich dark shale deposited in anoxic conditions",
      [("A clean, well-sorted sandstone", "That is a typical reservoir rock."), ("A massive granite", "Granite has no organic matter."), ("A rock salt bed", "Salt is a seal, not a source.")],
      [("Source rock", "Fine sediment with preserved organic matter becomes kerogen.")], "Source rocks", "Recall", "Where does the organic matter come from?"),
    Q("Which kerogen type is derived mainly from woody land plants and yields mainly gas?", "Type III",
      [("Type I", "Type I comes from algae and gives oil."), ("Type II", "Type II comes from marine plankton and gives oil."), ("Type IV", "Type IV is inert and gives neither.")],
      [("Kerogen types", "Hydrogen-poor woody material gives gas and coal.")], "Kerogen and maturation", "Recall", "Land plants, low hydrogen."),
    N("The surface temperature is 20 °C and the geothermal gradient is 25 °C per km. At what depth, in km, is the base of the oil window (120 °C)?", 4,
      [("Formula", "depth = (T − surface T) ÷ gradient."), ("Calculate", "(120 − 20) ÷ 25 = 4 km.")], "Oil window", "Calculation", "Subtract the surface temperature before dividing.", tol=0.05, unit="km"),
    N("Using the same figures, at what depth, in km, is the top of the oil window (60 °C)?", 1.6,
      [("Calculate", "(60 − 20) ÷ 25 = 1.6 km.")], "Oil window", "Calculation", "Use the same formula with 60 °C.", tol=0.05, unit="km"),
    Q("A sandstone core of volume 200 cm³ contains 45 cm³ of connected pore space. What is its porosity?", "22.5%",
      [("4.4%", "That is 200 ÷ 45 turned round."), ("45%", "That is the pore volume, not a percentage of the total."), ("77.5%", "That is the percentage of solid grains.")],
      [("Porosity", "45 ÷ 200 × 100 = 22.5%.")], "Reservoir rocks", "Calculation", "Pore volume divided by total volume.", ),
    Q("In which trap is oil held where a reservoir sandstone thins out within shale?", "Trap D, a stratigraphic pinch-out",
      [("Trap A, an anticline", "In trap A the oil is at the crest of a fold."), ("Trap B, a fault trap", "In trap B the oil is held against a fault."), ("Trap C, a salt dome", "In trap C beds are upturned against salt.")],
      [("Pinch-out", "A sand wedge that thins to nothing in shale forms a stratigraphic trap.")], "Traps", "Interpretation", "Which trap needs no fold or fault?", diagram=TRAP_Q, alt=TRAP_ALT),
    Q("In an anticlinal trap, which sequence of fluids is found from the crest downwards?", "Gas, oil, water",
      [("Oil, gas, water", "Gas is lighter than oil."), ("Water, oil, gas", "Water is the densest, so it is lowest."), ("Oil, water, gas", "Gas rises above both.")],
      [("Density", "The fluids sort by density: lightest at the top.")], "Traps", "Concept", "Order by density."),
    Q("Why must a trap form before, or while, oil migrates?", "Otherwise the oil would pass through and escape with nothing to hold it",
      [("Because oil forms inside the trap", "Oil forms in the source rock and migrates."), ("Because traps make kerogen mature", "Maturation depends on temperature."), ("Because traps are made of salt", "Traps can be many kinds.")],
      [("Timing", "A trap formed late may find the oil already gone or dispersed.")], "Petroleum system", "Reasoning", "What does the oil need when it arrives?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_PET, title="Source, maturation, reservoir and trap", lesson="gyu2-petroleum-geology", questions=build(V13, 213)))

# ------------------------------------------------------------------ 14. Hydrogeology
V14 = [
    Q("What is specific yield?", "The fraction of a rock's volume of water that drains out under gravity",
      [("The total pore space as a percentage", "That is porosity."), ("The water held back by surface tension", "That is specific retention."), ("The rate of flow through a unit area", "That is a flux or velocity.")],
      [("Storage", "Porosity = specific yield + specific retention.")], "Aquifers and storage", "Recall", "Gravity drainage only."),
    Q("Why does clay yield very little water although its porosity is high?", "Its tiny pores hold water by surface tension, so specific yield is very low",
      [("Its pores are very large", "Clay pores are tiny."), ("Clay has no pore space", "Clay has high porosity."), ("Clay repels water", "Clay holds water strongly.")],
      [("Retention", "Most of the water is held and cannot drain.")], "Aquifers and storage", "Reasoning", "Think of specific retention."),
    N("An aquifer has K = 20 m per day, a cross-section of 40 m² and a hydraulic gradient of 0.01. Calculate the discharge in m³ per day.", 8,
      [("Darcy's law", "Q = KAi."), ("Calculate", "20 × 40 × 0.01 = 8 m³ per day.")], "Darcy's law", "Calculation", "Multiply K by area by gradient.", tol=0.05, unit="m³ per day"),
    N("For the same aquifer with an effective porosity of 0.2, calculate the seepage velocity in m per day.", 1,
      [("Formula", "v = Ki ÷ n_e."), ("Calculate", "20 × 0.01 ÷ 0.2 = 1 m per day.")], "Darcy's law", "Calculation", "Divide the Darcy velocity by the effective porosity.", tol=0.01, unit="m per day"),
    N("How many days would a pollutant take to travel 150 m at that seepage velocity?", 150,
      [("Divide", "150 ÷ 1 = 150 days.")], "Groundwater flow and pollution", "Calculation", "Time = distance ÷ velocity.", tol=0.5, unit="days"),
    N("A sandstone aquifer has K = 12 m per day and thickness 25 m. Calculate its transmissivity in m² per day.", 300,
      [("Formula", "T = Kb."), ("Calculate", "12 × 25 = 300 m² per day.")], "Transmissivity", "Calculation", "Multiply conductivity by thickness.", tol=0.5, unit="m² per day"),
    Q("Water rises above the top of a confined aquifer in a well because:", "The water is under pressure from the higher recharge area",
      [("The aquifer is open to the atmosphere", "A confined aquifer is sealed above by an aquitard."), ("Capillary action lifts it many metres", "Capillary rise is small."), ("The water is warmer and lighter", "Temperature is not the cause.")],
      [("Head", "The potentiometric surface lies above the top of the aquifer.")], "Confined aquifers", "Concept", "Where is the recharge area?"),
    Q("What is a cone of depression?", "The funnel-shaped lowering of the water table or potentiometric surface around a pumped well",
      [("A hill of sediment around a spring", "That is not a cone of depression."), ("A sinkhole in limestone", "A sinkhole is a collapse feature."), ("The zone where seawater enters an aquifer", "That is saline intrusion.")],
      [("Drawdown", "The water level is lowest at the well and rises with distance.")], "Pumping and drawdown", "Recall", "Pumping lowers the water level."),
]
SETS.append(practice_set(module=M_ECO, topic=T_HYD, title="Darcy's law, aquifers and groundwater flow", lesson="gyu2-hydrogeology-darcy", questions=build(V14, 214)))

# ------------------------------------------------------------------ 15. Engineering geology
V15 = [
    Q("What does RQD measure?", "The percentage of a core run made of intact pieces 10 cm or longer",
      [("The compressive strength of the core", "That is UCS."), ("The water content of a clay", "That is a moisture content or Atterberg limit."), ("The porosity of the rock", "RQD is about fracturing.")],
      [("RQD", "A guide to the degree of fracturing of the rock mass.")], "Rock mass properties", "Recall", "It is a percentage of core."),
    N("A 200 cm core run contains pieces 10 cm or longer of 30, 20, 45, 15 and 25 cm. Calculate the RQD as a percentage.", 67.5,
      [("Add", "30 + 20 + 45 + 15 + 25 = 135 cm."), ("RQD", "135 ÷ 200 × 100 = 67.5%.")], "Rock mass properties", "Calculation", "Add only pieces of 10 cm or more.", tol=0.1, unit="%"),
    N("A clay has a liquid limit of 55% and a plastic limit of 25%. Calculate the plasticity index.", 30,
      [("Formula", "PI = LL − PL."), ("Calculate", "55 − 25 = 30.")], "Soil properties", "Calculation", "Subtract the plastic limit from the liquid limit.", tol=0.05),
    Q("Which clay property makes it a poor foundation in a seasonal climate?", "Swelling and shrinking with changes in water content",
      [("High compressive strength", "Strong rocks are good foundations."), ("Very high permeability", "Clays have low permeability."), ("Very low porosity", "Clays are porous but this is not the problem.")],
      [("Swelling clays", "Smectite expands when wet and shrinks when dry, cracking structures.")], "Soil properties", "Concept", "What happens to montmorillonite when it is wetted?"),
    Q("For a dam, which orientation of the bedding is most favourable?", "Beds dipping upstream",
      [("Beds dipping downstream", "That favours sliding and leakage under the dam."), ("Beds dipping parallel to a fault along the valley", "A fault is a weakness and a leakage path."), ("Horizontal beds of cavernous limestone", "Caves allow reservoir leakage.")],
      [("Dip", "Upstream dips resist sliding and make seepage paths longer.")], "Dam sites", "Application", "Which way would water have to flow to escape?"),
    N("A dry sand slope of 20° has an angle of internal friction of 30°. Calculate the factor of safety, FS = tan φ ÷ tan β.", 1.59,
      [("Tangents", "tan 30° = 0.577; tan 20° = 0.364."), ("Divide", "0.577 ÷ 0.364 = 1.59.")], "Slope stability", "Calculation", "Use FS = tan φ ÷ tan β.", tol=0.02),
    Q("Heavy rain lowers the effective friction angle of the slope to 18°. What happens to the slope of 20°?", "FS falls below 1 (about 0.89) and the slope fails",
      [("FS rises above 1.5 and the slope is safer", "Water lowers the resistance."), ("FS stays at 1.59", "The friction angle has changed."), ("FS becomes exactly 1", "tan 18° ÷ tan 20° is about 0.89.")],
      [("Calculation", "tan 18° = 0.325; 0.325 ÷ 0.364 = 0.89, so the slope is unstable.")], "Slope stability", "Application", "Recalculate with φ = 18°."),
    Q("Which factor is NOT a factor for the siting of a quarry?", "The number of people employed in the quarry after it opens",
      [("The quality of the rock", "Quality is a siting factor."), ("The thickness of overburden", "Thin overburden lowers cost."), ("The distance to the market and roads", "Transport cost is a siting factor.")],
      [("Read the command", "Siting factors are about where the quarry should be, not its effects once open.")], "Quarries", "Reasoning", "Is it a cause of location or a result of it?"),
]
SETS.append(practice_set(module=M_ECO, topic=T_ENG, title="Rock mass, soil, dams, slopes and quarries", lesson="gyu2-engineering-geology", questions=build(V15, 215)))

# ------------------------------------------------------------------ Examination: Paper 1
X1 = [
    Q("According to the Board's 2023 report, how many questions are in Geology Paper 1?", "50 multiple-choice questions",
      [("25 multiple-choice questions", "The report gives 50."), ("6 essay questions", "That is Paper 2."), ("5 compulsory practical questions", "That is Paper 3.")],
      [("Format", "Paper 1 is 50 multiple-choice questions, 30% of the examination.")], "Paper 1 format", "Recall", "Recall the structure in the report."),
    Q("In a stem such as 'Which of the following is NOT a feature of irregular echinoids?', you should:", "Test each option and choose the false statement",
      [("Choose the first true statement", "In a NOT question the key is the false one."), ("Choose the longest option", "Length proves nothing."), ("Leave it blank", "A blank cannot score.")],
      [("Negative stem", "Three options are true; you want the one that is not.")], "Multiple-choice routine", "Concept", "What are you hunting for?"),
    Q("What is the best first step on reading a multiple-choice item?", "Read the stem and predict the answer before looking at the options",
      [("Read the four options first", "A familiar wrong option may pull you in."), ("Pick the option with 'always' in it", "Absolute words are often wrong but must be checked."), ("Skip all calculations", "Calculation items are worth the same one mark.")],
      [("Routine", "Read, predict, eliminate, check.")], "Multiple-choice routine", "Concept", "Protect yourself from distractors."),
    N("A mineral has a daughter-to-parent ratio of 3. How many half-lives have passed?", 2,
      [("Fraction left", "Parent = 1 ÷ (1 + 3) = 1/4."), ("Half-lives", "(1/2)² = 1/4: 2 half-lives.")], "Calculation items", "Calculation", "Work out the fraction of parent left.", tol=0),
    N("Water flows through an aquifer with K = 8 m per day, area 100 m² and gradient 0.01. Calculate the discharge in m³ per day.", 8,
      [("Darcy", "Q = KAi = 8 × 100 × 0.01 = 8.")], "Calculation items", "Calculation", "Use Q = KAi.", tol=0.05, unit="m³ per day"),
    Q("A calculation question has the options 0.8, 8, 80 and 800. You work out 8. Why are the others there?", "They are distractors from slips such as misplaced decimal points or a missing factor",
      [("They are all correct", "Only one option is correct."), ("They show the units are wrong", "They are numbers from common slips."), ("They give extra marks", "Each item scores one mark.")],
      [("Distractors", "Wrong options are built from typical slips.")], "Distractors", "Concept", "How are wrong options written?"),
    N("The KKEVO Paper 1 mock has 50 questions in 90 minutes (a practice setting). How many minutes per question on average?", 1.8,
      [("Divide", "90 ÷ 50 = 1.8 minutes.")], "Time per question", "Calculation", "Divide the time by the number of questions.", tol=0.01, unit="minutes"),
    Q("Which approach to revision does the Board's 2023 report advise against?", "Speculative preparation that leaves out parts of the syllabus",
      [("Practising the whole syllabus", "The report encourages wide coverage."), ("Owning the recommended textbooks", "The report recommends this."), ("Learning the correct spelling of terms", "The report advises this.")],
      [("Report", "Paper 1 covers the entire syllabus, so skipped topics cost marks.")], "Revision planning", "Recall", "Paper 1 covers everything."),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Multiple-choice routine, calculations and timing", lesson="gyu2-exam-paper-1-multiple-choice", questions=build(X1, 221)))

# ------------------------------------------------------------------ Examination: Paper 2
X2 = [
    Q("According to the Board's 2023 report, how is Geology Paper 2 organized?", "Six essay questions, of which candidates answer four",
      [("Fifty multiple-choice questions", "That is Paper 1."), ("Five compulsory practical questions", "That is Paper 3."), ("Two essays, both compulsory", "The report gives six questions.")],
      [("Format", "Six questions, any four, weighted 35%.")], "Paper 2 format", "Recall", "Recall the report."),
    Q("What does the command word 'explain' ask you to do?", "Give reasons: how and why something happens",
      [("List facts without reasons", "That is state or list."), ("Say what happens without reasons", "That is describe."), ("Give only the names of things", "That is name.")],
      [("Command words", "Explain needs reasons, often using because or so.")], "Command words", "Recall", "Which word needs reasons?"),
    Q("A question asks for the FACTORS that influence the location of a quarry. Which answer earns the marks?", "Quality of rock, thin overburden, distance to market, distance from homes and water supplies",
      [("Dust, noise and landslides near the quarry", "These are effects."), ("The jobs the quarry provides", "This is an economic effect."), ("The disadvantages of quarrying", "The question asks about location.")],
      [("Read the question", "The Board's report notes candidates gave effects instead of factors of location.")], "Answer what is asked", "Application", "Is it a reason for the site or a result?"),
    Q("A question asks candidates to explain how palaeomagnetic stripes support sea-floor spreading. Which answer is best?", "Symmetrical stripes of normal and reversed polarity on both sides of the ridge, older away from it, show new crust forming at the ridge and moving outwards",
      [("A description of the theory of sea-floor spreading", "The report notes this is the error: the theory is described, the evidence is not."), ("A list of past reversals of the field", "A list does not show spreading."), ("A description of the evidence for continental drift", "That is different evidence.")],
      [("Evidence to conclusion", "Link the stripes to the conclusion.")], "Linking evidence to theory", "Application", "The question asks how the evidence supports the idea."),
    Q("Which is the best use of the first five minutes on an essay?", "Write a plan of key terms, points, examples and a labelled diagram",
      [("Start writing everything you know", "This leads to irrelevant answers."), ("Draw the rock cycle as a warm-up", "The report notes candidates drew the wrong diagram."), ("Write a long introduction about geology", "Introductions should be short and relevant.")],
      [("Planning", "A plan keeps the answer on the question.")], "Essay planning", "Application", "What protects you from irrelevance?"),
    Q("Which diagram feature earns credit in a Paper 2 answer?", "Large, neat labels naming the features you discuss",
      [("Colouring and shading only", "Labels, not decoration, earn credit."), ("A copy of a diagram unrelated to the question", "Irrelevant diagrams earn nothing."), ("No labels, to save time", "Unlabelled diagrams earn little.")],
      [("Labelled diagram", "Draw large and label every feature you refer to.")], "Diagrams", "Concept", "A diagram must be readable."),
    N("You have 150 minutes (a KKEVO practice setting) for a practice paper of 25 parts. How many minutes per part on average?", 6,
      [("Divide", "150 ÷ 25 = 6 minutes.")], "Time management", "Calculation", "Divide the time by the number of parts.", tol=0.01, unit="minutes"),
    Q("Why should abbreviations and short-hand be avoided in written answers?", "The Board's report asks candidates not to use them and notes misspellings of key terms",
      [("They are always scientifically wrong", "The reason is clarity and marking."), ("They lengthen the paper", "They shorten it but lose credit."), ("They are banned by law", "It is the Board's advice.")],
      [("Report", "Write terms in full and spell them correctly.")], "Writing technical terms", "Recall", "Recall the report's advice to students."),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Command words, answers and essay planning", lesson="gyu2-exam-paper-2-essays", questions=build(X2, 222)))

# ------------------------------------------------------------------ Examination: Paper 3
X3 = [
    Q("According to the Board's 2023 report, Geology Paper 3 is:", "A practical paper of five compulsory questions",
      [("Fifty multiple-choice questions", "That is Paper 1."), ("An essay paper of six questions", "That is Paper 2."), ("A fieldwork report of 5 000 words", "The report does not describe it so.")],
      [("Format", "Five compulsory questions; SBA and fieldwork count 5% each.")], "Paper 3 format", "Recall", "Practical and compulsory."),
    Q("How should a grid reference be written on a geological map?", "Six figures, eastings first and then northings",
      [("Four figures, northings first", "The report notes this error."), ("Six figures, northings first", "Eastings come first."), ("Four figures, eastings first", "Six figures are needed to locate a feature accurately.")],
      [("Grid reference", "Along the corridor then up the stairs: eastings, then northings.")], "Grid references", "Recall", "Eastings are read first."),
    Q("What is the evidence on a map that a fold is an anticline?", "Dip arrows point away from the axis and the oldest bed is in the core",
      [("The beds move away on both sides", "Beds do not move; the dip arrows give the evidence."), ("Dip arrows point towards the axis", "That is a syncline."), ("The youngest bed lies in the core", "That is a syncline.")],
      [("Anticline", "Oldest rocks in the core; dips away from the axis.")], "Folds on maps", "Application", "Which way do the dip arrows point?"),
    Q("A small patch of a younger rock is completely surrounded by older rock. What is it?", "An outlier, formed by erosion",
      [("An inlier", "An inlier is older rock surrounded by younger."), ("An angular unconformity", "That is a surface, not an isolated outcrop."), ("A sill", "A sill is an intrusion.")],
      [("Outlier", "Younger rock isolated by erosion.")], "Maps: outliers and inliers", "Interpretation", "Younger inside, older around."),
    Q("How should the positive crystallographic axes be labelled in a crystal drawing?", "+a, +b and +c",
      [("a+, b+ and c+", "The report notes the sign comes first."), ("A, B and C in capital letters", "Axes are lower-case."), ("x, y and z", "Crystal axes are a, b, c.")],
      [("Convention", "Sign first, then the letter.")], "Crystal models", "Recall", "Recall the convention."),
    Q("A fossil has a siphonal canal on its shell. What mode of life should you give, with the reason?", "A burrower or ploughing animal, because of the siphonal canal",
      [("A borrower, because of the siphonal canal", "The report notes candidates confused burrower with borrower."), ("Attached to rock by a pedicle", "A pedicle is a brachiopod feature."), ("A swimmer, because of its ears", "Ears are a scallop feature.")],
      [("Mode of life", "State the mode and the evidence; spell burrower correctly.")], "Fossil identification", "Application", "Give mode and evidence."),
    Q("A coral specimen is a reef-building form. What is its full environmental significance?", "A warm, clear, shallow marine environment",
      [("A shallow marine environment", "The report notes 'warm' was omitted."), ("A deep, cold ocean", "Reef corals need light and warmth."), ("A desert", "Corals are marine.")],
      [("Corals", "Give all three adjectives.")], "Fossil identification", "Application", "Include the temperature."),
    Q("A hand specimen is granular and sugary, composed of calcite and reacts with dilute HCl. What is the relationship between it and limestone?", "It is marble, formed by metamorphism of limestone, which is the parent rock",
      [("It is limestone, the parent of marble", "Marble is the metamorphic rock formed from limestone."), ("It is a plutonic equivalent of limestone", "Plutonic equivalents belong to igneous rocks."), ("It has no relationship to limestone", "They share calcite and reaction with acid.")],
      [("Protolith", "Limestone is the protolith of marble.")], "Hand specimens", "Reasoning", "Which came first?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Maps, crystals, fossils and specimens: practical method", lesson="gyu2-exam-paper-3-practical", questions=build(X3, 223)))

# ------------------------------------------------------------------ Paper 1 mock exam A (50 MC across the five modules)
# Allocation by topic count (7, 7, 6, 5, 4): 12 + 12 + 10 + 9 + 7 = 50.
P1 = [
    # ---- Sedimentology & Sedimentary Petrology (12)
    Q("Which grains need the lowest flow velocity to be eroded from a bed, according to the Hjulström diagram?", "Fine to medium sand",
      [("Clay", "Clay is cohesive, so it needs a higher velocity than sand to be eroded."), ("Pebbles", "Pebbles are heavy and need a high velocity."), ("Boulders", "Boulders need the highest velocity of all.")],
      [("Diagram", "The erosion curve has its minimum near fine to medium sand.")], T_HJUL, "Recall", "Which grains are not cohesive and not heavy?"),
    Q("According to Stokes' law, what happens to the settling velocity of a small sphere if its diameter doubles?", "It increases four times",
      [("It doubles", "Velocity depends on the square of the diameter."), ("It increases eight times", "That would be a cube law."), ("It stays the same", "Velocity depends on diameter.")],
      [("Stokes", "v is proportional to d², so doubling d gives four times the velocity.")], T_HJUL, "Calculation", "v depends on d squared."),
    Q("What is the grain diameter 0.25 mm in phi units (phi = −log₂ d, d in mm)?", "2",
      [("−2", "That would be a grain of 4 mm."), ("0.25", "That is the diameter in mm, not phi."), ("4", "That is 1 ÷ 0.25, not −log₂ 0.25.")],
      [("Formula", "φ = −log₂(0.25)."), ("Calculate", "0.25 = 2⁻², so φ = 2.")], T_GRAIN, "Calculation", "Write 0.25 as a power of 2."),
    Q("A sediment is described as well sorted. This means that:", "Its grains are all of similar size",
      [("Its grains are all well rounded", "That describes roundness."), ("Its grains are all large", "Sorting is about uniformity, not size."), ("It contains no clay", "A well-sorted clay is possible.")],
      [("Sorting", "A low standard deviation of grain size.")], T_GRAIN, "Concept", "Think of a spread of sizes."),
    Q("In cross-bedding, the foresets dip:", "In the direction in which the current was flowing",
      [("Against the current direction", "Foresets form on the lee side and dip downstream."), ("Vertically downwards", "They are inclined layers."), ("Parallel to the top of the bed", "They are inclined to the bedding.")],
      [("Lee side", "Grains avalanche down the downstream face.")], T_SSTR, "Concept", "Where do grains accumulate on a dune?"),
    Q("Graded bedding that is coarse at the base and fines upward is typical of:", "Turbidity current deposits",
      [("Wind-blown dunes", "Dunes show large cross-bedding."), ("Evaporite basins", "Evaporites form by chemical precipitation."), ("Glacial striations", "Striations are erosional marks.")],
      [("Turbidites", "The current slows and drops its largest grains first.")], T_SSTR, "Recall", "Which current deposits graded beds?"),
    Q("Which process reduces porosity during diagenesis?", "Compaction and cementation",
      [("Dissolution of unstable grains", "Dissolution can increase porosity."), ("Fracturing by tectonic stress", "Fracturing increases permeability."), ("Weathering at the surface", "Weathering is not diagenesis.")],
      [("Diagenesis", "Grains are pressed together and pores are filled with cement.")], T_DIAG, "Recall", "Which processes pack and fill?"),
    Q("A sandstone with abundant feldspar and little rounding, derived from nearby granite, is:", "An arkose",
      [("An orthoquartzite", "Orthoquartzite is nearly pure quartz and well rounded."), ("A greywacke", "Greywacke has a clay matrix and rock fragments."), ("A micrite", "Micrite is a carbonate mud.")],
      [("Arkose", "Feldspar-rich and immature.")], T_SILI, "Recall", "Which sandstone is feldspar-rich?"),
    Q("Which rock is a poorly sorted sandstone with a clay-rich matrix, deposited by turbidity currents?", "Greywacke",
      [("Orthoquartzite", "That is clean, well sorted quartz sandstone."), ("Breccia", "Breccia is a coarse rock of angular fragments."), ("Oolitic limestone", "That is a carbonate.")],
      [("Greywacke", "Immature, with graded bedding and sole marks.")], T_SILI, "Recall", "Which is poorly sorted with a clay matrix?"),
    Q("In Dunham's classification, a grain-supported carbonate rock with no mud is a:", "Grainstone",
      [("Mudstone", "Mudstone is mud-supported with few grains."), ("Packstone", "Packstone is grain-supported with mud between."), ("Boundstone", "Boundstone is bound by organisms.")],
      [("Dunham", "Grain-supported with no mud: grainstone.")], T_CARB, "Recall", "Look for grain support and no mud."),
    Q("A carbonate rock made mainly of shell fragments set in lime mud is a:", "Biomicrite",
      [("Oosparite", "Oosparite has ooids in sparry cement."), ("Pelsparite", "Pelsparite has pellets in sparry cement."), ("Biosparite", "Biosparite has shell fragments in sparry cement, not mud.")],
      [("Folk", "Bio- prefix for fossils; -micrite for the mud matrix.")], T_CARB, "Application", "Fossils plus mud."),
    Q("From evaporating sea water, which mineral precipitates before halite?", "Gypsum",
      [("Sylvite", "Potassium salts precipitate last."), ("Carnallite", "Magnesium and potassium salts come late."), ("Quartz", "Quartz is not an evaporite.")],
      [("Sequence", "Calcite, then gypsum or anhydrite, then halite, then potassium and magnesium salts.")], T_EVAP, "Recall", "Order of evaporation."),
    # ---- Structural Geology & Geological Map Work (12)
    Q("What is plotted on the axes of a Mohr circle?", "Normal stress and shear stress",
      [("Strain and time", "Those are not the axes of the Mohr circle."), ("Depth and temperature", "Those are for a geotherm."), ("Dip and strike", "Those are map measurements.")],
      [("Mohr circle", "It shows stresses on all planes through a point.")], T_STRS, "Recall", "Which two stress components act on a plane?"),
    Q("A rock layer 10 cm long is stretched to 12 cm. What is the extension e = (l − l₀) ÷ l₀?", "0.2",
      [("1.2", "That is the stretch l ÷ l₀, not the extension."), ("2", "That is the change in length in cm, not a ratio."), ("−0.2", "A negative value means shortening.")],
      [("Formula", "e = (12 − 10) ÷ 10 = 0.2.")], T_STRS, "Calculation", "Change in length divided by original length."),
    Q("Which condition favours ductile rather than brittle deformation?", "High temperature, high confining pressure and a slow strain rate",
      [("Low temperature and a high strain rate", "These favour brittle failure."), ("Low confining pressure near the surface", "That favours brittle failure."), ("Very cold, dry rock", "Cold rock is brittle.")],
      [("Ductile", "Rocks flow when hot, deeply buried and slowly strained.")], T_BRIT, "Concept", "Think of the deep crust."),
    Q("In an unoverturned fold, the oldest rocks are found in the core of:", "An anticline",
      [("A syncline", "The youngest rocks lie in the core of a syncline."), ("A monocline", "A monocline is a single step."), ("A dome with the beds inverted", "Beds are not inverted in a normal dome.")],
      [("Anticline", "Beds dip away from the axis; the core is the oldest.")], T_FOLD, "Recall", "Which fold has the oldest beds in the core?"),
    Q("A fold with an interlimb angle of 20° is described as:", "Tight",
      [("Gentle", "Gentle folds have interlimb angles of 120° to 180°."), ("Open", "Open folds have interlimb angles of 70° to 120°."), ("Isoclinal", "Isoclinal folds have an interlimb angle of 0°.")],
      [("Classification", "Tight folds have interlimb angles of about 30° to 70° or less.")], T_FOLD, "Application", "A smaller angle means a tighter fold."),
    Q("In a normal fault the hanging wall:", "Moves down relative to the footwall",
      [("Moves up relative to the footwall", "That is a reverse fault."), ("Moves sideways only", "That is a strike-slip fault."), ("Does not move", "A fault is a surface of relative movement.")],
      [("Normal fault", "Extension: the hanging wall slides down.")], T_FALT, "Recall", "Normal faults form by extension."),
    Q("A low-angle reverse fault that carries older rocks over younger is a:", "Thrust",
      [("Normal fault", "Normal faults dip steeply and cause extension."), ("Tear fault", "A tear fault is a strike-slip fault."), ("Joint", "A joint has no displacement.")],
      [("Thrust", "Shortening on a gently dipping fault.")], T_FALT, "Recall", "Reverse and low angle."),
    Q("Slaty cleavage usually forms:", "At right angles to the direction of maximum compression",
      [("Parallel to the direction of maximum compression", "Cleavage is perpendicular to it."), ("Parallel to bedding in every case", "It can cut across bedding."), ("Only by cooling of magma", "Cleavage is a deformation fabric.")],
      [("Cleavage", "Platy minerals rotate or grow perpendicular to the compression.")], T_CLEA, "Concept", "Think of flattening."),
    Q("On a map, a stratum contour joins points at the same height on a bed. Its direction gives the bed's:", "Strike",
      [("Dip direction", "Dip is at right angles to strike."), ("True thickness", "Thickness needs two surfaces."), ("Age", "Contours do not give age.")],
      [("Strike", "Strike is the direction of a horizontal line on the bed.")], T_STRC, "Concept", "A horizontal line on a bed."),
    Q("Three points on a bed have heights 100 m, 100 m and 60 m. In what direction is the strike?", "Along the line joining the two 100 m points",
      [("Along the line joining the 100 m and the 60 m points", "That line is not horizontal on the bed."), ("At right angles to the line joining the two 100 m points", "That is the dip direction."), ("It cannot be found", "Two points of equal height fix the strike.")],
      [("Three-point problem", "Equal heights lie on a stratum contour.")], T_STRC, "Application", "Which points are at the same height?"),
    Q("A cross-section has a horizontal scale of 1 : 10 000 and a vertical scale of 1 : 2 000. What is the vertical exaggeration?", "5",
      [("0.2", "That is the inverse: it would make the vertical scale smaller."), ("8", "That is 10 000 − 2 000 turned into thousands, not a ratio."), ("20", "That is 10 000 ÷ 500.")],
      [("Formula", "VE = horizontal scale denominator ÷ vertical scale denominator."), ("Calculate", "10 000 ÷ 2 000 = 5.")], T_XSEC, "Calculation", "Compare the scales."),
    Q("On a cross-section drawn along a line that is oblique to the dip direction, the dip shown is:", "An apparent dip, less than the true dip",
      [("The true dip", "True dip is shown only in a section along the dip direction."), ("An apparent dip, greater than the true dip", "Apparent dips never exceed the true dip."), ("Zero in every case", "It is zero only along the strike.")],
      [("Apparent dip", "Always less than or equal to the true dip.")], T_XSEC, "Concept", "Which section shows true dip?"),
    # ---- Systematic Palaeontology (10)
    Q("A bed contains single bivalve valves of similar size, mostly broken and convex up. This is a:", "Death assemblage transported by currents",
      [("Life assemblage", "Life assemblages have articulated shells in life position."), ("Lagerstätte", "No soft-part preservation is described."), ("Trace fossil assemblage", "These are shells.")],
      [("Evidence", "Sorting, breakage and orientation show transport.")], T_TAPH, "Interpretation", "Were the shells moved?"),
    Q("Which organism has the highest preservation potential?", "A thick-shelled bivalve in a shallow sea",
      [("A jellyfish", "No hard parts."), ("A worm in a beach", "No hard parts."), ("An insect on land", "Rapid decay and little burial.")],
      [("Factors", "Hard parts, abundance and a habitat with rapid burial.")], T_TAPH, "Reasoning", "Combine skeleton and habitat."),
    Q("The facial suture of a trilobite functioned during:", "Moulting",
      [("Enrolment", "Enrolment used the thoracic joints."), ("Feeding", "It was not a feeding structure."), ("Reproduction", "It was a line of weakness for moulting.")],
      [("Moulting", "The cephalon split along the suture.")], T_TRIL, "Recall", "What do arthropods do as they grow?"),
    Q("Graptoloids are excellent zone fossils of the Ordovician and Silurian mainly because they:", "Evolved rapidly and were planktonic and widespread",
      [("Were fixed to the sea floor", "That limits distribution."), ("Had thick calcite skeletons", "Their skeleton was organic."), ("Lived on land", "They were marine.")],
      [("Criteria", "Short ranges and wide distribution.")], T_TRIL, "Reasoning", "What two qualities does a zone fossil need?"),
    Q("What is the plane of symmetry in a bivalve?", "Between the two valves, along the hinge line",
      [("Through the middle of each valve", "That is the brachiopod plane."), ("There is none", "Bivalves are bilaterally symmetrical."), ("Parallel to the growth lines", "The plane lies between the valves.")],
      [("Symmetry", "Valves are mirror images of each other.")], T_BRAC, "Recall", "Brachiopods differ."),
    Q("A deep pallial sinus in a bivalve shows that the animal:", "Had long siphons and lived buried in sediment",
      [("Was cemented to rock", "Cemented forms have no sinus."), ("Swam by clapping its valves", "Swimmers lack a deep sinus."), ("Was attached by a pedicle", "Pedicles belong to brachiopods.")],
      [("Pallial sinus", "It marks the siphon-retracting muscles.")], T_BRAC, "Application", "Siphons imply burial."),
    Q("Which suture type is typical of Jurassic and Cretaceous ammonites?", "Ammonitic, with frilled saddles and lobes",
      [("Nautiloid, straight or gently curved", "That is the simplest."), ("Goniatitic, angular and smooth", "That is Devonian to Permian."), ("Ceratitic, with frilled lobes only", "That is mainly Triassic.")],
      [("Complexity", "Suture complexity increased through time.")], T_GAST, "Recall", "The most complex suture."),
    Q("Reef-building corals are used to indicate:", "Warm, clear, shallow marine water",
      [("Cold deep sea", "They need light and warmth."), ("Fresh-water lakes", "Corals are marine."), ("Arid deserts", "Corals cannot live there.")],
      [("Indicator", "Symbiotic algae require light and warm water.")], T_ECHI, "Application", "Give all the adjectives."),
    Q("Why are microfossils preferred to large fossils in oil wells?", "They survive drilling and are abundant in cuttings",
      [("They are easier to see in the field", "They are microscopic."), ("They are always older", "Age is not the reason."), ("They are made of oil", "They are not.")],
      [("Cuttings", "Large fossils are crushed by the drill bit.")], T_MICR, "Reasoning", "What does a drill bit do?"),
    Q("The distribution of Glossopteris on several southern continents is evidence for:", "The former union of those continents in Gondwana",
      [("A global ocean", "It is a land plant."), ("A mass extinction", "Distribution says nothing about extinction."), ("The origin of flowering plants", "Glossopteris was a seed fern.")],
      [("Distribution", "Its seeds could not cross oceans.")], T_MICR, "Application", "How did it reach five continents?"),
    # ---- Stratigraphy & Regional Geology of Cameroon (9)
    Q("The Jurassic System is a:", "Chronostratigraphic unit of rock",
      [("Lithostratigraphic unit", "That is defined by rock type."), ("Biostratigraphic unit", "That is defined by fossils."), ("Unit of time", "The unit of time is the Period.")],
      [("Units", "System, series and stage are rock units of time.")], T_PRIN, "Recall", "Period is to time as system is to what?"),
    Q("A mineral has one eighth of its original parent isotope. The half-life is 704 million years. What is its age?", "2 112 million years",
      [("704 million years", "That is one half-life, which leaves half."), ("1 408 million years", "That is two half-lives, which leaves a quarter."), ("5 632 million years", "That is eight half-lives; the parent fraction is 1/8, not 8 half-lives.")],
      [("Half-lives", "(1/2)³ = 1/8, so 3 half-lives."), ("Age", "3 × 704 = 2 112 million years.")], T_PRIN, "Calculation", "Count how many halvings."),
    Q("The Ntem Complex is part of the:", "Congo Craton",
      [("West African Craton", "That lies in West Africa."), ("Pan-African fold belt", "That lies to the north."), ("Cameroon Volcanic Line", "That is Cenozoic volcanism.")],
      [("Location", "Archaean craton of southern Cameroon.")], T_PREC, "Recall", "Which craton underlies the south?"),
    Q("Banded iron formations are important because they are:", "A major source of iron ore",
      [("A source of aluminium", "Bauxite is the aluminium ore."), ("The main reservoir of oil", "They are not oil reservoirs."), ("Active volcanic rocks", "They are chemical sediments.")],
      [("BIF", "Alternating iron oxide and chert bands.")], T_PREC, "Recall", "Iron in the name."),
    Q("The Pan-African orogeny is associated with the assembly of:", "Gondwana",
      [("Pangaea", "Pangaea formed later."), ("Rodinia", "Rodinia broke up before."), ("Laurasia", "That is the northern half of Pangaea.")],
      [("Gondwana", "Neoproterozoic collisions.")], T_PANA, "Recall", "Africa and South America."),
    Q("The Central Cameroon Shear Zone is usually described as:", "A major dextral strike-slip shear zone",
      [("A thrust that carried nappes south", "That describes the Yaoundé nappes."), ("A rift basin", "The Cretaceous basins are rifts."), ("A volcanic crater", "It is a deformation zone.")],
      [("CCSZ", "Check your textbook for the trend and sense of shear.")], T_PANA, "Recall", "Strike-slip."),
    Q("Which Cretaceous basin next to Nigeria has produced most of Cameroon's oil?", "Rio del Rey basin",
      [("Mamfe basin", "Inland continental rift."), ("Garoua basin", "Inland rift in the North."), ("Lake Chad basin", "Far North.")],
      [("Rio del Rey", "Coastal basin at the eastern edge of the Niger Delta system.")], T_BASN, "Recall", "Coastal, in the west."),
    Q("The Cameroon Volcanic Line is described as intraplate because:", "It lies within the African plate, with no plate boundary",
      [("It lies on a subduction zone", "There is no subduction zone."), ("It is a spreading ridge", "It is not a ridge."), ("It is made of sediments", "It is volcanic.")],
      [("Intraplate", "Alkaline volcanism within a plate.")], T_CVL, "Concept", "No plate boundary."),
    Q("The 1986 disaster at Lake Nyos was caused by:", "A sudden release of carbon dioxide from deep lake water",
      [("A lava flow", "No lava was involved."), ("An explosive ash eruption", "No ash fall occurred."), ("A mudflow from Mount Cameroon", "Wrong volcano and wrong process.")],
      [("Limnic eruption", "Dense CO2 suffocated people.")], T_CVL, "Recall", "Which gas?"),
    # ---- Economic, Petroleum, Hydro- & Engineering Geology (7)
    Q("An ore contains 0.5% copper; the average crustal abundance is 0.005%. What is the concentration factor?", "100",
      [("10", "That divides 0.05 by 0.005."), ("0.01", "That divides the abundance by the grade."), ("1 000", "That divides by 0.0005.")],
      [("Divide", "0.5 ÷ 0.005 = 100.")], T_ORE, "Calculation", "Ore grade divided by crustal abundance."),
    Q("Where is copper redeposited in supergene enrichment?", "At and below the water table",
      [("In the gossan at the surface", "Copper has been leached from there."), ("In the leached zone", "Copper is removed from it."), ("Only in the deepest primary ore", "It replaces primary sulphides near the water table.")],
      [("Supergene", "Reducing conditions below the water table precipitate secondary sulphides.")], T_ORE, "Recall", "Where does oxygen run out?"),
    Q("Which kerogen type yields mainly oil and comes from marine plankton?", "Type II",
      [("Type III", "That gives mainly gas."), ("Type IV", "That gives nothing."), ("Type I only", "Type I comes from lake algae.")],
      [("Type II", "The commonest oil-prone kerogen.")], T_PET, "Recall", "Marine plankton."),
    Q("Which of these is a stratigraphic trap?", "A sandstone that thins out within shale",
      [("An anticline", "A fold is a structural trap."), ("A fault trap", "Faults are structural."), ("A salt dome", "Salt domes are structural.")],
      [("Stratigraphic", "Caused by a change in the rocks.")], T_PET, "Recall", "No fold or fault."),
    Q("A sand aquifer has K = 5 m per day, area 20 m² and gradient 0.02. What is the discharge?", "2 m³ per day",
      [("100 m³ per day", "That leaves out the gradient."), ("0.2 m³ per day", "That divides by 10: a slip in the decimal point."), ("20 m³ per day", "That uses a gradient of 0.2.")],
      [("Darcy", "5 × 20 × 0.02 = 2 m³ per day.")], T_HYD, "Calculation", "Q = KAi."),
    Q("Which aquifer has water under pressure that rises above the top of the aquifer in a well?", "A confined aquifer",
      [("An unconfined aquifer", "Unconfined aquifers have a free water table."), ("A perched aquifer", "Perched lenses are small and unconfined."), ("An aquitard", "An aquitard transmits water slowly.")],
      [("Confined", "Sealed between aquitards; recharged at higher ground.")], T_HYD, "Concept", "Where does the pressure come from?"),
    Q("For a dam, beds that dip upstream are favourable because they:", "Resist sliding and make seepage paths longer",
      [("Allow water to escape quickly", "That would be unfavourable."), ("Make the foundation weak", "They improve stability."), ("Reduce the need for a core", "They do not remove the need for good design.")],
      [("Dip", "Water would have to flow up the bedding to escape.")], T_ENG, "Application", "Which way would leakage travel?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="gyu2-exam-paper-1-multiple-choice",
                         questions=build(P1, 231), mock=True, time_limit_minutes=90))

# ------------------------------------------------------------------ Paper 2 practice paper A (25 auto-markable parts in 8 questions)
P2 = [
    # Question 1: taphonomy and fossils as environmental indicators (3)
    Q("Question 1(a). A candidate is asked to discuss the preservation potential of Cardium. Which opening is best?", "Cardium has a high preservation potential, because it has a calcareous shell, is abundant and lived where sediment was deposited quickly",
      [("Cardium is a bivalve with two valves", "This describes the animal but gives no verdict."), ("Cardium is preserved because it dies", "No reasons are given."), ("Cardium lived in the sea and had a shell", "No verdict on high or low preservation potential.")],
      [("Verdict first", "The report notes candidates gave reasons without saying whether the potential was high or low.")], T_TAPH, "Application", "Start with the verdict."),
    Q("Question 1(b). Which fossil indicates a warm, shallow, clear marine environment?", "A colony of reef-building corals",
      [("A pyritized ammonite", "Pyrite indicates reducing conditions."), ("A mammoth", "A mammoth indicates a glacial environment."), ("A fossil lungfish", "Lungfish indicate seasonal drought.")],
      [("Indicator", "Corals need light, warmth and clear water.")], T_TAPH, "Interpretation", "Which fossil needs algae and light?"),
    Q("Question 1(c). A bed contains articulated bivalves in life position. This indicates:", "A life assemblage with little or no transport",
      [("A death assemblage", "Transport would separate valves."), ("A turbidite", "Turbidites show graded bedding and transport."), ("A trace fossil", "These are body fossils.")],
      [("Evidence", "Intact pairs in burrowing position were buried in place.")], T_TAPH, "Interpretation", "Was the assemblage moved?"),
    # Question 2: invertebrates (4)
    Q("Question 2(a). Which feature shows that a two-valved fossil is a brachiopod?", "Each valve is symmetrical about a plane through the beak",
      [("The two valves are mirror images", "That is the bivalve pattern."), ("It has a pallial sinus", "That is a bivalve feature."), ("It has a siphuncle", "That is a cephalopod feature.")],
      [("Symmetry", "Brachiopod valves are unequal and each is symmetrical.")], T_BRAC, "Concept", "Where is the plane of symmetry?"),
    Q("Question 2(b). A trilobite with huge eyes, long spines and a narrow body probably lived:", "As a swimming or pelagic animal",
      [("As a burrower in mud", "Burrowers are often blind."), ("Cemented to rock", "Trilobites were not cemented."), ("As a filter feeder on a stalk", "That is not a trilobite habit.")],
      [("Functional morphology", "Large eyes and spines suggest an active swimmer.")], T_TRIL, "Application", "What do large eyes suggest?"),
    Q("Question 2(c). A coiled fossil is divided into chambers and has frilled sutures. It is a:", "Ammonite",
      [("Gastropod", "Gastropods are not chambered."), ("Nautiloid", "Nautiloids have simple sutures."), ("Belemnite", "Belemnites have an internal guard.")],
      [("Sutures", "Frilled sutures identify ammonites.")], T_GAST, "Application", "Chambers plus frilled sutures."),
    N("Question 2(d). A coral shows 1 950 daily growth ridges in 5 annual bands (invented). Calculate the number of days in one year.", 390,
      [("Divide", "1 950 ÷ 5 = 390 days.")], T_ECHI, "Calculation", "Divide the ridges by the bands.", tol=0.5, unit="days"),
    # Question 3: stratigraphy (3)
    Q("Question 3(a). Which statement describes a lithostratigraphic unit?", "A formation defined by its rock type",
      [("A zone defined by a fossil", "That is biostratigraphy."), ("A system defined by time", "That is chronostratigraphy."), ("An epoch of geological time", "That is geochronology.")],
      [("Units", "Formation, member and bed are defined by lithology.")], T_PRIN, "Recall", "Which is defined by rock?"),
    N("Question 3(b). A zircon has a Pb-206 to U-238 ratio of 0.25. Using a half-life of 4 470 million years, calculate its age in millions of years.", 1439,
      [("Formula", "t = (4 470 ÷ 0.693) × ln 1.25."), ("Calculate", "6 449 × 0.2231 ≈ 1 439 million years.")], T_PRIN, "Calculation", "Use t = (t½ ÷ ln 2) × ln(1 + D/P).", tol=15, unit="million years"),
    Q("Question 3(c). In a conformable section, beach sand is overlain by offshore shale. Walther's law shows that:", "The sea deepened as the section was deposited (a transgression)",
      [("The sea became shallower", "That would put shallower facies on deeper ones."), ("There is an unconformity", "The succession is conformable."), ("The beds were folded", "Facies changes do not show folding.")],
      [("Walther", "Vertical order equals lateral order of environments.")], T_PRIN, "Interpretation", "Is the water getting deeper?"),
    # Question 4: basement and Pan-African (3)
    Q("Question 4(a). Which rock association is typical of the Archaean Ntem Complex?", "TTG gneisses, charnockites and greenstone belts with banded iron formations",
      [("Cretaceous sandstones and shales", "These fill sedimentary basins."), ("Alkali basalts and trachytes", "These are Cenozoic volcanic rocks."), ("Coal measures", "These are Carboniferous sediments.")],
      [("Ntem", "Archaean craton rocks.")], T_PREC, "Recall", "Think of an old craton."),
    Q("Question 4(b). Nappes of the Yaoundé domain were thrust:", "Southward onto the Congo Craton",
      [("Northward onto the Sahara", "They moved towards the craton."), ("Eastward into the sea", "No sea lay there."), ("Downward into the mantle", "Thrusts move rocks up and over.")],
      [("Foreland", "The craton acted as a rigid foreland.")], T_PANA, "Recall", "Where is the craton?"),
    Q("Question 4(c). A granite that cuts the foliation of the surrounding gneiss and is itself unfoliated is:", "Post-tectonic",
      [("Syn-tectonic", "Syn-tectonic granites share the foliation."), ("Pre-tectonic", "Pre-tectonic granites would be deformed."), ("Part of the craton floor", "Its relations show it is younger than the deformation.")],
      [("Cross-cutting", "It is younger than the fabric.")], T_PANA, "Reasoning", "Is it deformed?"),
    # Question 5: basins and CVL (3)
    Q("Question 5(a). Wedge-shaped units that thicken into normal faults are:", "Syn-rift deposits",
      [("Post-rift deposits", "They drape faults with even thickness."), ("Basement rocks", "Basement is crystalline."), ("Volcanic plugs", "Plugs are not wedge-shaped sediments.")],
      [("Growth strata", "Deposited while the faults were active.")], T_BASN, "Interpretation", "When were the faults active?"),
    N("Question 5(b). A basin fill 2 000 m thick accumulated in 50 million years (invented). Calculate the average sedimentation rate in m per million years.", 40,
      [("Divide", "2 000 ÷ 50 = 40 m per million years.")], T_BASN, "Calculation", "Thickness ÷ time.", tol=0.5, unit="m per million years"),
    Q("Question 5(c). Which observation is the best evidence against a simple hotspot origin of the Cameroon Volcanic Line?", "There is no steady age progression along the line",
      [("The lavas are alkaline", "Hotspots also produce alkaline lavas."), ("It crosses the coast", "That does not test the hotspot model."), ("It has crater lakes", "Crater lakes are not relevant.")],
      [("Age pattern", "A moving plate over a fixed plume gives a steady age trend.")], T_CVL, "Reasoning", "What should a hotspot track show?"),
    # Question 6: petroleum and ores (4)
    N("Question 6(a). The surface temperature is 25 °C and the geothermal gradient 30 °C per km. At what depth (km) is 115 °C reached?", 3,
      [("Formula", "(115 − 25) ÷ 30 = 3 km.")], T_PET, "Calculation", "Subtract the surface temperature first.", tol=0.05, unit="km"),
    Q("Question 6(b). Which sequence of fluids is found from the crest of an anticlinal trap downwards?", "Gas, oil, water",
      [("Oil, gas, water", "Gas is lighter."), ("Water, oil, gas", "Water is lowest."), ("Gas, water, oil", "Oil is lighter than water.")],
      [("Density", "Order by density.")], T_PET, "Concept", "Lightest on top."),
    N("Question 6(c). A reservoir covers 3 km² with 10 m of net thickness, porosity 0.20 and oil saturation 0.75. Calculate the volume of oil in place in millions of m³.", 4.5,
      [("Rock volume", "3 × 10⁶ m² × 10 m = 3 × 10⁷ m³."), ("Oil", "3 × 10⁷ × 0.20 × 0.75 = 4.5 × 10⁶ m³ = 4.5 million m³.")], T_PET, "Calculation", "Multiply rock volume by porosity and saturation.", tol=0.05, unit="million m³"),
    Q("Question 6(d). Gossan is the:", "Iron-oxide cap left above a leached sulphide ore body",
      [("Zone where copper sulphides are redeposited", "That is the enriched zone."), ("Unaltered primary ore", "That is the hypogene zone."), ("Bauxite", "Bauxite is an aluminium ore.")],
      [("Gossan", "Iron oxides remain after copper and sulphur are leached.")], T_ORE, "Recall", "A red-brown cap."),
    # Question 7: hydrogeology and engineering (3)
    N("Question 7(a). An aquifer has K = 15 m per day, area 30 m² and gradient 0.02. Calculate the discharge in m³ per day.", 9,
      [("Darcy", "15 × 30 × 0.02 = 9 m³ per day.")], T_HYD, "Calculation", "Q = KAi.", tol=0.05, unit="m³ per day"),
    N("Question 7(b). A 100 cm core run has pieces of 10 cm or longer of 20, 15 and 30 cm. Calculate the RQD as a percentage.", 65,
      [("Add", "20 + 15 + 30 = 65 cm."), ("RQD", "65 ÷ 100 × 100 = 65%.")], T_ENG, "Calculation", "Add the pieces of 10 cm or more.", tol=0.1, unit="%"),
    Q("Question 7(c). Which is a factor in choosing the location of a quarry?", "Quality of rock and a thin overburden",
      [("Dust and noise produced after opening", "These are effects."), ("Landslides caused by blasting", "These are hazards."), ("Jobs created in the town", "This is an economic effect.")],
      [("Siting", "Factors of location, not effects of the quarry.")], T_ENG, "Application", "Which factor determines where to dig?"),
    # Question 8: sedimentology and structure (2)
    Q("Question 8(a). A graded bed fining upward from a coarse base, with sole marks, is typical of:", "A turbidity current deposit",
      [("A desert dune", "Dunes show large cross-bedding."), ("A lagoon evaporite", "Evaporites are chemical."), ("A glacial till", "Till is unsorted.")],
      [("Turbidite", "Graded bedding and sole marks.")], T_SSTR, "Interpretation", "Which current deposits graded beds?"),
    Q("Question 8(b). On a geological map, dip arrows point away from the axis and the oldest bed is in the core. The structure is:", "An anticline",
      [("A syncline", "Dips point towards the axis in a syncline."), ("A normal fault", "A fault offsets beds."), ("An outlier", "An outlier is a patch of younger rock surrounded by older rock.")],
      [("Evidence", "The report asks for dip-arrow evidence and the core bed.")], T_FOLD, "Interpretation", "Which way do the dips point?"),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="gyu2-exam-paper-2-essays",
                         questions=build(P2, 232), mock=True, time_limit_minutes=150))
