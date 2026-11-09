"""Form 5 Geology (O Level 0555): practice sets for modules 4 to 6 and the Examination module, with two mock papers.

Draft content. Exam facts are only those of the Board's 2023 report: Paper 1 is 50 multiple-choice questions, all
answered; Paper 2 has seven structural questions, five answered (two from Section A, two from Section B and compulsory
school-based Question 7). The mock papers use KKEVO practice settings (90 and 150 minutes), not official settings.
Essays cannot be marked automatically, so the Paper 2 practice paper tests definitions, diagram and map reading and
calculations through multiple-choice and numeric parts. Numerical answers were verified by script; teaching figures
are invented for practice.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("geology", "form-5")

M4 = "Geomorphology & Surface Processes"
M5 = "Structural Geology, Stratigraphy & Paleontology"
M6 = "Hydrogeology, Economic & Environmental Geology"
M7 = "Examination"


class _Bag:
    """Gives the position of the correct option so that A-D are used evenly."""

    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.items = []

    def next(self):
        if not self.items:
            self.items = [0, 1, 2, 3]
            self.rng.shuffle(self.items)
        return self.items.pop()


BAG = _Bag(1)


def use(seed):
    global BAG
    BAG = _Bag(seed)


def Q(prompt, correct, wrongs, steps, concept, skill, hint, diagram="", alt=""):
    """Four-option MC. `wrongs` = [(text, why)] x3; the correct option goes to a balanced position."""
    pos = BAG.next()
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(correct, correct=True))
    return MC(prompt, choices, steps=[S(a, text=b) for a, b in steps], concept=concept, skill=skill, hint=hint,
              diagram=diagram, diagram_alt=alt)


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit="", diagram="", alt=""):
    return NUM(prompt, answer, steps=[S(a, text=b) for a, b in steps], tolerance=tol, unit=unit, concept=concept,
               skill=skill, hint=hint, diagram=diagram, diagram_alt=alt)


# Exact topic titles of the Geology outline (apps/academics/gce_curriculum.py).
T_BR = "Geology and its branches"
T_SOL = "The solar system"
T_SEI = "Seismic waves and the Earth's interior"
T_PLA = "Plate tectonics"
T_CRY = "Crystals and symmetry"
T_SIX = "The six crystal systems"
T_PHY = "Physical properties of minerals"
T_RFM = "Rock-forming minerals"
T_CYC = "The rock cycle"
T_IGN = "Igneous rocks"
T_VOL = "Volcanism and the Cameroon Volcanic Line"
T_SED = "Sedimentary rocks"
T_MET = "Metamorphic rocks"
T_WEA = "Weathering"
T_SOI = "Soil formation"
T_MAS = "Mass wasting"
T_RIV = "Rivers and their landforms"
T_WIS = "Wind, ice and the sea"
T_SSD = "Stress, strain, strike and dip"
T_FOL = "Folds"
T_FJU = "Faults, joints and unconformities"
T_STR = "Principles of stratigraphy"
T_TIM = "The geological time scale"
T_FOS = "Fossils"
T_HYD = "The hydrologic cycle and groundwater"
T_AQU = "Aquifers, springs and wells"
T_PET = "Petroleum, natural gas and coal"
T_ORE = "Ore deposits and mineral resources of Cameroon"
T_GEO = "Geohazards"

SETS = []

# ------------------------------------------------------------------ 1. Weathering
use(11)
SETS.append(practice_set(
    module=M4, topic=T_WEA, title="Weathering: processes and definitions",
    lesson="gly2-weathering-physical-chemical-biological",
    questions=[
        Q("Which statement correctly separates weathering from erosion?",
          "Weathering breaks rock down where it is; erosion removes and carries the pieces away",
          [("Weathering carries rock away; erosion breaks it down in place", "The two are swapped: weathering is breakdown in place."),
           ("Weathering needs water; erosion never does", "Erosion is often done by water. The difference is movement, not water."),
           ("Weathering happens underground only; erosion happens on hills only", "Both happen at the surface and neither is limited to one place.")],
          [("Recall", "Weathering is breakdown in place. Erosion is removal and transport.")],
          "Weathering and erosion", "Recall", "One of them involves movement of the pieces."),
        Q("A rock surface peels off in thin sheets after hot days and cold nights. This is mainly", "Physical weathering by thermal expansion",
          [("Chemical weathering by hydration", "Hydration adds water to minerals. Peeling from heating and cooling does not change the minerals."),
           ("Biological weathering by lichens", "No living organism is involved in this case."),
           ("Deposition by wind", "Deposition is the dropping of material, not breakdown of a rock.")],
          [("Cause", "Repeated heating and cooling makes the outer layer expand and contract."), ("Type", "The rock is split but the minerals do not change: physical weathering.")],
          "Thermal expansion and exfoliation", "Concept", "Is the mineral composition changing?"),
        Q("The addition of water to a mineral, causing a change in its chemical composition, is called", "Hydration",
          [("Oxidation", "Oxidation involves oxygen, not just water."), ("Carbonation", "Carbonation involves carbonic acid from carbon dioxide and water."), ("Exfoliation", "Exfoliation is a physical peeling process.")],
          [("Match the definition", "Water added to a mineral: hydration.")],
          "Hydration", "Recall", "The prefix 'hydro' means water."),
        Q("Limestone reacts with rainwater containing dissolved carbon dioxide. The soluble product is", "Calcium hydrogencarbonate",
          [("Calcium oxide", "Calcium oxide (quicklime) is not made by cold rainwater."), ("Silicon dioxide", "That is quartz and is not produced here."), ("Iron oxide", "Iron oxide forms by oxidation of iron minerals, not from limestone.")],
          [("Write the reaction", "CaCO3 + H2O + CO2 gives Ca(HCO3)2."), ("Name", "Ca(HCO3)2 is calcium hydrogencarbonate, which is soluble in water.")],
          "Carbonation of limestone", "Concept", "Think of the carbonic acid the rain contains."),
        Q("A rock containing iron minerals develops a red-brown crust like rust. The process is", "Oxidation",
          [("Hydrolysis of silica", "Hydrolysis of feldspar makes clay, not a rusty crust."), ("Frost wedging", "Frost wedging is the splitting of rock by freezing water."), ("Abrasion", "Abrasion is wearing by rock fragments carried by wind or water.")],
          [("Clue", "A red-brown rusty crust forms when iron combines with oxygen."), ("Process", "That is oxidation.")],
          "Oxidation", "Application", "What makes a nail rusty?"),
        Q("A fig tree grows in a crack of a wall and splits it. This is", "Biological weathering",
          [("Chemical weathering only", "The main effect is the splitting force of roots, which is physical, and a living organism causes it."), ("Erosion", "Erosion is transport; the wall is split in place."), ("Mass wasting", "Mass wasting is movement downslope under gravity.")],
          [("Agent", "A living plant is the agent."), ("Type", "A living organism helping rock to break is biological weathering.")],
          "Biological weathering", "Application", "Who or what is doing the breaking?"),
        N("A cube of rock with sides of 1 cm is split into 1 000 equal small cubes with sides of 0.1 cm. By what factor does the total surface area increase?", 10,
          [("Original area", "6 faces x 1 cm x 1 cm = 6 cm squared."), ("Small cubes", "One cube: 6 x 0.1 x 0.1 = 0.06 cm squared. 1 000 cubes: 60 cm squared."), ("Factor", "60 / 6 = 10.")],
          "Surface area and weathering", "Calculation", "Find the area of one cube before and after.", unit="times"),
        Q("Why is chemical weathering faster in the forest of southern Cameroon than in a cold dry region?",
          "Heat and plentiful water speed up chemical reactions, and plant acids add to the attack",
          [("There are no joints in tropical rocks", "Tropical rocks do have joints."), ("Wind removes all the rock at once", "Wind is not the main reason and wind transport is erosion."), ("Tropical rocks are always softer", "Rock type matters, but the climate is the main difference here.")],
          [("Factors", "Chemical reactions go faster in warm conditions with plenty of water."), ("Add organisms", "Plants release acids that attack minerals as well.")],
          "Climate and rate of weathering", "Reasoning", "Think about temperature and rainfall."),
    ]))

# ------------------------------------------------------------------ 2. Soil formation
SOILQ = "f5gly2-soil-q.svg"
SOILQ_A = "A soil profile with five horizontal layers labelled P at the top, then Q, R, S and T at the bottom, with a depth arrow on the left; the layers have no names"
use(12)
SETS.append(practice_set(
    module=M4, topic=T_SOI, title="Soil: components, factors and horizons",
    lesson="gly2-soil-formation-profile",
    questions=[
        Q("Which list gives all four components of a soil?", "Mineral particles, humus, water and air",
          [("Mineral particles, rock salt, oil and air", "Salt and oil are not general soil components."), ("Humus, water, gold and air", "Gold is not a normal component of soil."), ("Mineral particles, humus and bedrock only", "Soil also contains water and air, and bedrock is not a component.")],
          [("Recall", "Soil = weathered mineral particles + humus + water + air.")], "Components of soil", "Recall", "Think of what is in a handful of garden soil."),
        Q("In the profile shown, which layer is the topsoil (A horizon)?", "Q",
          [("P", "P is the surface layer of leaf litter and humus (O horizon)."), ("R", "R is the subsoil (B horizon)."), ("T", "T is the bedrock.")],
          [("Order", "From the top: O (P), A (Q), B (R), C (S), bedrock (T)."), ("Answer", "The topsoil is Q.")],
          "Soil horizons", "Interpretation", "Count down from the top: O first, then A.", diagram=SOILQ, alt=SOILQ_A),
        Q("In the same profile, which layer is solid, unweathered bedrock?", "T",
          [("S", "S is the C horizon of partly weathered rock fragments."), ("R", "R is the B horizon, which is soil."), ("P", "P is the organic layer at the surface.")],
          [("Bottom layer", "The lowest layer in a full profile is the bedrock, T.")], "Soil horizons", "Interpretation", "Where would the unbroken rock lie?", diagram=SOILQ, alt=SOILQ_A),
        Q("Which of these is NOT one of the factors that control soil formation?", "The colour of the sky",
          [("Parent material", "Parent material is a factor."), ("Climate", "Climate is a factor."), ("Time", "Time is a factor.")],
          [("Five factors", "Parent material, climate, relief, organisms and time."), ("Answer", "The colour of the sky is not a factor.")],
          "Factors of soil formation", "Recall", "Pick the option that has no effect on weathering or humus."),
        Q("Washing of dissolved minerals downwards by rain is called", "Leaching",
          [("Exfoliation", "Exfoliation is peeling of rock sheets."), ("Deflation", "Deflation is wind removal of loose material."), ("Attrition", "Attrition is the wearing down of fragments by collision.")],
          [("Definition", "Leaching is the downward washing of dissolved minerals by rainwater.")], "Leaching", "Recall", "It involves water moving down through soil."),
        Q("A tropical forest soil is red and poor in nutrients. The red colour is mainly due to", "Iron and aluminium oxides left after leaching",
          [("A high content of humus", "Humus makes soil dark, not red."), ("Fresh volcanic ash", "Fresh volcanic ash is usually grey and rich in nutrients."), ("Fossil shells", "Shells would give a pale, lime-rich soil.")],
          [("Heavy rain", "It leaches soluble nutrients and silica."), ("What stays", "Iron and aluminium oxides remain and colour the soil red.")],
          "Tropical soils", "Concept", "What stays behind when the soluble materials are washed away?"),
        N("A soil core has a volume of 400 cm3. The solid grains occupy 240 cm3. What percentage of the core is pore space?", 40,
          [("Pore volume", "400 - 240 = 160 cm3."), ("Percentage", "160 / 400 x 100 = 40 per cent.")],
          "Pore space of soil", "Calculation", "Subtract the solid volume from the total, then divide.", unit="%"),
        Q("On a steep slope the soil is usually thin because", "It is removed by erosion and mass wasting faster than it forms",
          [("Parent rock cannot weather on slopes", "Rock weathers on slopes too."), ("Time has no effect on steep land", "Time matters everywhere."), ("Plants cannot grow on steep ground at all", "Some plants do grow on slopes. The key point is loss of material.")],
          [("Relief", "Slope is a factor in soil formation."), ("Reason", "On steep slopes material moves downhill, so a thick soil cannot build up.")],
          "Relief and soil", "Reasoning", "What happens to loose material on a steep slope?"),
    ]))

# ------------------------------------------------------------------ 3. Mass wasting
use(13)
SETS.append(practice_set(
    module=M4, topic=T_MAS, title="Mass wasting: types, causes and control",
    lesson="gly2-mass-wasting",
    questions=[
        Q("The main force that causes mass wasting is", "Gravity",
          [("Wind", "Wind causes aeolian processes, not mass wasting."), ("Magnetism", "Magnetism plays no part."), ("Ocean currents", "Currents work in the sea, not on hillslopes.")],
          [("Definition", "Mass wasting is movement of material downslope under gravity.")], "Mass wasting", "Recall", "What pulls things down a slope?"),
        Q("Very slow downslope movement of soil, shown by leaning fence posts and curved tree trunks, is", "Creep",
          [("Rockfall", "Rockfall is sudden free fall of rock."), ("Mudflow", "A mudflow is a fast flow of wet soil."), ("Slump", "Slump is a sudden movement of a block on a curved surface.")],
          [("Clue", "Leaning posts and trees mean a slow movement."), ("Name", "That is creep.")], "Creep", "Recall", "Which type is too slow to see?"),
        Q("A block of soil slips down along a curved surface and leaves a curved scar at the top. This is a", "Slump",
          [("Creep", "Creep is slow with no scar."), ("Rockfall", "Rockfall is falling rock from a cliff."), ("Mudflow", "A mudflow flows as a wet mass and does not move as a rotated block.")],
          [("Clue", "A curved scar and a rotated block are the signs of slump.")], "Slump", "Concept", "Think about the curved surface."),
        Q("A fast flow of soil saturated with water moves down a valley after heavy rain. It is a", "Mudflow",
          [("Creep", "Creep is very slow."), ("Slump", "Slump is a block movement."), ("Deflation", "Deflation is a wind process.")],
          [("Clue", "Very wet, fast, flowing: mudflow.")], "Mudflow", "Recall", "What do you call a flow of mud?"),
        Q("Which change is most likely to make a slope fail?", "Heavy rain that saturates the soil",
          [("A dry spell", "Dry conditions make the soil stronger."), ("Planting deep-rooted trees", "Roots bind the soil and make it stable."), ("Building a drain to take water away", "Drainage reduces water in the slope and helps stability.")],
          [("Water", "Water adds weight and reduces friction between grains.")], "Causes of slope failure", "Application", "Which option adds water to the slope?"),
        Q("A road cutting removes the bottom of a hillside. Why does this make landslides more likely?", "The slope is steeper and the toe that supported it has gone",
          [("The soil becomes more fertile", "Fertility is not the issue."), ("The rock above becomes colder", "Temperature is not the cause."), ("Gravity becomes stronger", "Gravity does not change.")],
          [("Effect of cutting", "It makes the slope steeper and removes support at its base."), ("Result", "The downslope pull exceeds the strength more easily.")], "Slope stability", "Reasoning", "What holds the top of a slope up?"),
        Q("Which pair is correctly matched?", "Rockfall and talus at the foot of a cliff",
          [("Creep and a curved scar", "A curved scar belongs to slump."), ("Mudflow and leaning telephone poles", "Leaning poles are a sign of creep."), ("Slump and heap of boulders under a cliff", "Boulders under a cliff are from rockfall.")],
          [("Match each", "Rockfall makes talus; creep tilts poles; slump leaves a scar.")], "Types of mass wasting", "Concept", "Match each sign to the type."),
        Q("Which action would best reduce landslide risk on a farmed hillside?", "Plant trees and build drainage channels",
          [("Clear all vegetation to plant crops", "Roots hold the soil, so removal weakens it."), ("Cut a flat shelf into the base of the slope", "Cutting at the toe removes support."), ("Pile heavy waste at the top of the slope", "Extra weight increases the downslope pull.")],
          [("Strengthen the slope", "Roots bind soil and drains remove water.")], "Reducing landslide risk", "Application", "Which action makes the slope stronger and drier?"),
    ]))

# ------------------------------------------------------------------ 4. Rivers
RIVQ = "f5gly2-river-q.svg"
RIVQ_A = "Plan view of a meandering river on a floodplain. Letter A marks the outside of a bend at the bottom, B the inside of the same bend, C a separate curved lake beside the river and D the flat land around the river"
use(14)
SETS.append(practice_set(
    module=M4, topic=T_RIV, title="Rivers: erosion, load and landforms",
    lesson="gly2-rivers-erosion-transport-deposition",
    questions=[
        Q("The wearing of the river bed and banks by the stones and sand that the river carries is", "Abrasion",
          [("Attrition", "Attrition is the wearing of the stones themselves as they hit each other."), ("Solution", "Solution is dissolving of rock."), ("Deposition", "Deposition is dropping of the load.")],
          [("Definition", "Abrasion (corrasion) is the scraping of the bed and banks by the load.")], "River erosion", "Recall", "Think of sandpaper."),
        Q("Fine clay and silt carried floating in the water are moved by", "Suspension",
          [("Traction", "Traction moves large stones along the bed."), ("Saltation", "Saltation is the bouncing of sand grains."), ("Solution", "Solution is for dissolved material.")],
          [("Match", "Very fine particles floating in the water move in suspension.")], "River transport", "Recall", "Fine particles stay up in the water."),
        Q("In the figure, which letter marks the oxbow lake?", "C",
          [("A", "A marks the outer bank of the bend."), ("B", "B marks the inner bank of the bend."), ("D", "D marks the flat land around the river.")],
          [("Shape", "An oxbow lake is a curved lake separate from the river, cut off from an old meander."), ("Answer", "C.")],
          "Oxbow lakes", "Interpretation", "Look for a lake that is not part of the river channel.", diagram=RIVQ, alt=RIVQ_A),
        Q("In the figure, at A (outside of the bend) the river mainly", "Erodes to make a steep river cliff",
          [("Deposits sand to make a slip-off slope", "Slip-off slopes form on the inner bank, B."), ("Forms a delta", "Deltas form at the river mouth."), ("Builds a levee", "Levees form beside the channel in a flood.")],
          [("Fast water", "The current is fastest on the outer bank, so it erodes.")],
          "Meander processes", "Concept", "Is the water faster or slower on the outer bank?", diagram=RIVQ, alt=RIVQ_A),
        Q("At B (the inside of the bend) the river mainly", "Deposits sand and gravel to form a slip-off slope",
          [("Erodes a river cliff", "The cliff is on the outside, A."), ("Plunges over a waterfall", "Waterfalls occur where hard rock overlies soft rock."), ("Dissolves limestone", "That is solution, not the process on this bank.")],
          [("Slow water", "The water on the inside is slow, so it drops its load.")],
          "Meander processes", "Concept", "Is the current weaker or stronger on the inside?", diagram=RIVQ, alt=RIVQ_A),
        Q("A waterfall forms where", "A band of hard rock lies over softer rock",
          [("The river enters the sea", "That is where a delta forms."), ("The river meanders across a floodplain", "That produces meanders, not a step."), ("A glacier melts", "That is not needed for a waterfall.")],
          [("Differential erosion", "The soft rock below wears faster, leaving a step over which the water falls.")],
          "Waterfalls", "Concept", "One rock resists erosion better than the other."),
        N("A river channel is 10 m wide and 2 m deep on average. The water flows at 0.6 m per second. What is the discharge?", 12,
          [("Formula", "Discharge = width x depth x velocity."), ("Substitute", "10 x 2 x 0.6 = 12.")],
          "River discharge", "Calculation", "Find the area of the cross-section and multiply by speed.", unit="cubic metres per second"),
        Q("A delta forms where a river enters a sea because", "The river slows and drops its load",
          [("The river speeds up and erodes the sea bed", "Entering the sea makes the river slow down."), ("The river stops flowing in the sea", "It still flows, but loses energy."), ("The salt water dissolves the river's sand", "Salt water does not dissolve sand.")],
          [("Loss of energy", "On meeting still water the river's speed drops."), ("Deposition", "The load is dropped and builds up into low land.")],
          "Deltas", "Reasoning", "What happens to speed when moving water meets a larger water body?"),
    ]))

# ------------------------------------------------------------------ 5. Wind, ice and the sea
use(15)
SETS.append(practice_set(
    module=M4, topic=T_WIS, title="Wind, ice and the sea: processes and landforms",
    lesson="gly2-wind-ice-sea-landforms",
    questions=[
        Q("Removal of loose fine particles by wind, which lowers the ground surface, is", "Deflation",
          [("Abrasion", "Abrasion is the wearing of rock by wind-blown sand."), ("Plucking", "Plucking is a glacial process."), ("Attrition", "Attrition is the wearing of fragments by collision.")],
          [("Definition", "Deflation is wind removal of loose particles.")], "Wind erosion", "Recall", "Think 'deflate' means lower."),
        Q("A mound of wind-blown sand with a gentle windward slope and a steep slip face is a", "Dune",
          [("Moraine", "A moraine is made of debris left by ice."), ("Spit", "A spit is made by waves and longshore drift."), ("Arête", "An arête is a knife-edge ridge cut by glaciers.")],
          [("Shape", "A gentle windward slope and steep slip face describe a dune.")], "Dunes", "Recall", "Which landform is made of sand blown by wind?"),
        Q("An armchair-shaped hollow high on a mountain where a glacier began is a", "Cirque",
          [("Stack", "A stack is a rock column left in the sea."), ("Oxbow lake", "An oxbow lake is a river feature."), ("Loess", "Loess is wind-blown dust.")],
          [("Match", "A cirque (corrie) is the glacier's starting hollow.")], "Glacial landforms", "Recall", "It looks like an armchair."),
        Q("Which landform is made by glaciers?", "U-shaped valley",
          [("V-shaped valley", "V-shaped valleys are cut by rivers."), ("Wave-cut platform", "Made by waves."), ("Barchan dune", "Made by wind.")],
          [("Shape", "A glacier widens and deepens a river valley into a U shape.")], "Glacial landforms", "Concept", "Which letter-shape describes the glaciated valley?"),
        Q("A rock column left standing in the sea after the roof of an arch collapses is a", "Stack",
          [("Spit", "A spit is a ridge of deposited sand or shingle."), ("Cirque", "A cirque is a glacial hollow."), ("Levee", "A levee is a river bank feature.")],
          [("Sequence", "Crack, cave, arch, then stack when the arch falls.")], "Coastal erosion", "Recall", "It comes after the arch."),
        Q("A long ridge of sand attached to the land at one end and built by longshore drift is a", "Spit",
          [("Stack", "A stack is a rock pillar."), ("Moraine", "A moraine is made by ice."), ("Loess", "Loess is wind-blown silt.")],
          [("Deposition by the sea", "Longshore drift moves sediment past a bend, building a spit.")], "Coastal deposition", "Concept", "It is a depositional feature."),
        Q("Which statement about Cameroon is the most accurate?", "It has no glaciers today, so glacial landforms are studied from other regions",
          [("Glaciers cover the coastal region", "There are no glaciers on the coast."), ("Glaciers made the Wouri estuary", "The Wouri estuary is not a glacial landform."), ("Cameroon has more glaciers than Europe", "There are no glaciers in Cameroon.")],
          [("Fact", "Cameroon has no glaciers now.")], "Glaciers", "Application", "Is Cameroon cold enough for permanent ice at the surface?"),
        Q("Wind-blown sand wearing away a rock surface like sandpaper is", "Abrasion",
          [("Deflation", "Deflation removes loose particles."), ("Hydration", "Hydration is a chemical process."), ("Plucking", "Plucking is by glaciers.")],
          [("Mechanism", "Sand grains hit the rock and wear it down: abrasion.")], "Wind erosion", "Concept", "The moving sand acts like sandpaper."),
    ]))

# ------------------------------------------------------------------ 6. Stress, strain, strike and dip
SDQ = "f5gly2-strike-dip-q.svg"
SDQ_A = "A map square with a north arrow. A long vertical line is the strike line, with a short tick at its middle pointing to the right (east) and the number 40 beside the tick"
use(16)
SETS.append(practice_set(
    module=M5, topic=T_SSD, title="Stress, strain, strike and dip",
    lesson="gly2-stress-strain-strike-dip",
    questions=[
        Q("Stress is best defined as", "A force acting on a rock per unit area",
          [("The change in shape of a rock", "That is strain, the result of stress."), ("The breaking of a rock along a plane", "That describes a fault."), ("The heat inside a rock", "Heat is not stress.")],
          [("Definition", "Stress = force / area. Strain is the change produced.")], "Stress and strain", "Recall", "It is a force, not a change."),
        Q("Which kind of stress squeezes rock and mainly produces folds and reverse faults?", "Compression",
          [("Tension", "Tension pulls rock apart."), ("Shear", "Shear causes sideways sliding."), ("Gravity", "Gravity is a force, not a type of tectonic stress named here.")],
          [("Direction", "Squeezing is compression.")], "Types of stress", "Recall", "Think of two plates colliding."),
        Q("A rock that bends and flows without breaking is showing", "Ductile (plastic) behaviour",
          [("Brittle behaviour", "Brittle rocks break."), ("Elastic behaviour only", "Elastic rocks return to their shape when stress is removed."), ("Weathering", "Weathering is surface breakdown.")],
          [("Match", "Permanent bending without breaking is ductile deformation.")], "Rock behaviour", "Concept", "The rock keeps the new shape."),
        Q("In the figure, in which direction do the beds dip?", "East",
          [("West", "The tick points the opposite way."), ("North", "North is along the strike line, not at right angles."), ("South", "South is along the strike line.")],
          [("Reading the symbol", "The short tick shows the dip direction. It points to the east.")], "Dip direction", "Interpretation", "Which way does the short tick point?", diagram=SDQ, alt=SDQ_A),
        N("In the figure, what is the dip angle in degrees?", 40,
          [("Reading the number", "The number beside the tick is the dip angle: 40 degrees.")], "Dip angle", "Interpretation", "Look for the number on the symbol.", unit="degrees", diagram=SDQ, alt=SDQ_A),
        Q("A bed has a strike of east-west. Its dip direction could be", "North or south",
          [("East or west", "These are along the strike."), ("North-east only", "Dip direction is at 90 degrees to strike."), ("Vertically upwards", "Dip direction is a horizontal direction.")],
          [("Right angles", "The dip direction is at 90 degrees to the strike.")], "Strike and dip", "Concept", "Draw the strike line and then a line at right angles."),
        N("A bed dips at 30 degrees and its outcrop on flat ground is 300 m wide. Find its true thickness in metres.", 150,
          [("Formula", "True thickness = width x sin(dip)."), ("Substitute", "300 x sin 30 degrees = 300 x 0.5 = 150 m.")],
          "True thickness", "Calculation", "Use sin of the dip angle.", tol=0.5, unit="m"),
        N("A bed dips at 45 degrees and its outcrop is 80 m wide on flat ground. Find the true thickness to one decimal place (in metres).", 56.6,
          [("Formula", "True thickness = width x sin(dip)."), ("Substitute", "80 x sin 45 degrees = 80 x 0.7071 = 56.6 m.")],
          "True thickness", "Calculation", "sin 45 degrees is about 0.707.", tol=0.1, unit="m"),
    ]))

# ------------------------------------------------------------------ 7. Folds
FOLQ = "f5gly2-folds-q.svg"
FOLQ_A = "Cross-section of folded layers with an upward arch on the left and a downward trough on the right, dashed vertical axial planes through each, and three circled letters: P above the arch, Q above the trough and R above the sloping side between them"
use(17)
SETS.append(practice_set(
    module=M5, topic=T_FOL, title="Folds: anticlines, synclines and parts",
    lesson="gly2-folds-anticline-syncline",
    questions=[
        Q("A fold in which the limbs dip away from the axis is an", "Anticline",
          [("Syncline", "Syncline limbs dip towards the axis."), ("Horst", "A horst is a fault block."), ("Unconformity", "An unconformity is a gap in the rock record.")],
          [("Definition", "Limbs dipping away from the axis make an upfold: an anticline.")], "Anticline", "Recall", "The limbs go down on both sides of the crest."),
        Q("In an eroded anticline with beds in their original order, the rocks in the core are the", "Oldest",
          [("Youngest", "The youngest rocks are in the core of a syncline."), ("Igneous only", "The core can be any rock, and age is the point of the rule."), ("Same age as the limbs", "The limbs are younger than the core.")],
          [("Rule", "Anticline: oldest in the core.")], "Age in folds", "Recall", "Think of an arch cut off at the top."),
        Q("In the figure, which letter marks the syncline?", "Q",
          [("P", "P is on the arch, the anticline."), ("R", "R marks the side (limb) between the folds."), ("None of them", "The trough on the right is a syncline, marked Q.")],
          [("Shape", "A downfold is a syncline, marked Q.")], "Identify folds", "Interpretation", "Which part sags downwards?", diagram=FOLQ, alt=FOLQ_A),
        Q("In the figure, the part marked R, between the anticline and syncline, is called the", "Limb",
          [("Hinge", "The hinge is at the crest or trough."), ("Axial plane", "The axial plane is the dashed line."), ("Fault plane", "There is no fault in this figure.")],
          [("Parts of a fold", "The side of a fold between two hinges is a limb.")], "Parts of a fold", "Interpretation", "R is on the side of the fold.", diagram=FOLQ, alt=FOLQ_A),
        Q("The dashed lines in the figure show the", "Axial planes",
          [("Fault planes", "Fault planes show displacement of beds, which is not seen here."), ("Joints", "Joints are fractures, not drawn here."), ("Bedding planes", "Bedding planes follow the layers, not cut across them.")],
          [("Position", "The dashed line divides each fold into two limbs: the axial plane.")], "Axial plane", "Interpretation", "It divides each fold into two limbs.", diagram=FOLQ, alt=FOLQ_A),
        Q("A fold with an almost horizontal axial plane is called", "Recumbent",
          [("Symmetrical", "A symmetrical fold has a vertical axial plane."), ("Plunging", "Plunging describes a tilted axis."), ("Anticlinal", "That describes the shape, not the tilt of the axial plane.")],
          [("Meaning", "Recumbent means lying down: the axial plane is nearly horizontal.")], "Types of fold", "Concept", "Recumbent means lying down."),
        Q("What type of stress mostly forms folds?", "Compression",
          [("Tension", "Tension pulls rock apart."), ("Shear only", "Shear produces strike-slip faults."), ("No stress at all", "Folding needs stress.")],
          [("Cause", "Squeezing makes rock layers fold.")], "Cause of folds", "Concept", "Folds shorten the crust."),
        N("A bed 30 km long is folded so that it now spans 24 km. What is the percentage shortening?", 20,
          [("Difference", "30 - 24 = 6 km."), ("Percentage", "6 / 30 x 100 = 20 per cent.")],
          "Shortening by folding", "Calculation", "Divide the change by the original length.", unit="%"),
    ]))

# ------------------------------------------------------------------ 8. Faults, joints and unconformities
FAQ = "f5gly2-faults-q.svg"
FAQ_A = "Two cross-sections of layered rock cut by a steep blue fault line dipping to the right. In fault X an arrow on the right block points down; in fault Y an arrow on the right block points up"
HOQ = "f5gly2-horst-q.svg"
HOQ_A = "Two cross-sections with layered rock cut by two blue fault lines. In the left picture the middle block P is higher than its neighbours; in the right picture the middle block Q is lower than its neighbours"
UNQ = "f5gly2-uncon-q.svg"
UNQ_A = "Three cross-sections labelled Figure X, Y and Z, each with an amber wavy line as the old erosion surface. In X tilted beds lie under flat beds, in Y flat beds lie under and over the line, in Z a grey igneous-looking rock with crosses lies under flat beds"
use(18)
SETS.append(practice_set(
    module=M5, topic=T_FJU, title="Faults, horst and graben, and unconformities",
    lesson="gly2-faults-joints-unconformities",
    questions=[
        Q("A joint differs from a fault because along a joint", "There has been no noticeable movement",
          [("There has been a large displacement", "Displacement defines a fault."), ("The rock is always igneous", "Joints occur in all rock types."), ("The rock has been folded", "Folding is a different structure.")],
          [("Definition", "A joint is a fracture with no noticeable movement.")], "Fault and joint", "Recall", "Fault means movement."),
        Q("In fault X in the figure, the hanging wall (the right block, which lies above the fault plane) has moved down. The fault is", "A normal fault",
          [("A reverse fault", "In a reverse fault the hanging wall moves up."), ("A strike-slip fault", "Strike-slip movement is sideways."), ("A joint", "A joint has no displacement.")],
          [("Hanging wall", "The fault plane dips to the right, so the right block is the hanging wall."), ("Movement", "It moved down: normal fault.")], "Normal fault", "Interpretation", "Compare the movement arrow with the dip of the fault plane.", diagram=FAQ, alt=FAQ_A),
        Q("Fault Y in the figure was formed mainly by", "Compression",
          [("Tension", "Tension produces normal faults."), ("Folding only", "Folding is not a cause of faulting by itself."), ("Deposition", "Deposition is not a stress.")],
          [("Movement", "The hanging wall moved up: reverse fault."), ("Cause", "Reverse faults are caused by compression.")], "Reverse fault", "Interpretation", "Which type of fault shows the hanging wall rising?", diagram=FAQ, alt=FAQ_A),
        Q("In the figure, block P, higher than its neighbours between two faults, is a", "Horst",
          [("Graben", "A graben is the dropped block."), ("Syncline", "A syncline is a fold."), ("Dyke", "A dyke is an igneous intrusion.")],
          [("Shape", "A block pushed up between two parallel faults is a horst.")], "Horst", "Interpretation", "Is P higher or lower than its neighbours?", diagram=HOQ, alt=HOQ_A),
        Q("In the figure, block Q, lower than its neighbours between two faults, is a", "Graben",
          [("Horst", "A horst is the raised block."), ("Anticline", "An anticline is an upfold."), ("Joint set", "A joint set is a group of fractures without movement.")],
          [("Shape", "A dropped block between two faults is a graben.")], "Graben", "Interpretation", "Is Q higher or lower than its neighbours?", diagram=HOQ, alt=HOQ_A),
        Q("Which figure shows an angular unconformity?", "Figure X",
          [("Figure Y", "In Figure Y both sets of beds are horizontal: a parallel unconformity."), ("Figure Z", "In Figure Z igneous or metamorphic rock lies below: a heterolithic unconformity."), ("None of the figures", "Figure X is an angular unconformity.")],
          [("Look", "Flat beds above tilted beds: angular unconformity (X).")], "Angular unconformity", "Interpretation", "Which figure has tilted beds below the line?", diagram=UNQ, alt=UNQ_A),
        Q("Figure Z shows sedimentary beds lying on igneous or metamorphic rock across an erosion surface. This is a", "Heterolithic unconformity",
          [("Parallel unconformity", "Both sets of beds are horizontal in a parallel unconformity."), ("Angular unconformity", "Tilted beds lie below an angular unconformity."), ("Normal fault", "No fault is shown.")],
          [("Match", "Older igneous or metamorphic rock below, younger sediments above: heterolithic.")], "Heterolithic unconformity", "Interpretation", "What type of rock lies below the amber line?", diagram=UNQ, alt=UNQ_A),
        Q("Which sequence correctly lists the formation of an angular unconformity?", "Deposition, tilting and uplift, erosion, new deposition",
          [("Erosion, tilting, deposition, uplift", "Rock must exist before it can be tilted or eroded."), ("Deposition, erosion, new deposition, tilting", "Tilting happens before the new beds, otherwise they would be tilted too."), ("Tilting, deposition, erosion, uplift", "Beds cannot tilt before they are deposited.")],
          [("Order", "Beds are laid down, tilted and uplifted, eroded and then buried by new horizontal beds.")], "Formation of an unconformity", "Reasoning", "The new beds are flat, so they came last."),
    ]))

# ------------------------------------------------------------------ 9. Principles of stratigraphy
STR = "f5gly2-strata.svg"
STR_A = "A cross-section with five horizontal layers A at the bottom, then B, C, D and E at the top, all labelled with circled letters. A vertical grey body F cuts through layers A, B, C and D but does not enter E. An amber wavy line lies between D and E"
use(19)
SETS.append(practice_set(
    module=M5, topic=T_STR, title="Relative age and the principles of stratigraphy",
    lesson="gly2-stratigraphy-principles-relative-age",
    questions=[
        Q("The principle of superposition states that in an undisturbed sequence of sedimentary layers", "The oldest layer is at the bottom",
          [("The oldest layer is at the top", "That reverses the principle."), ("All layers are the same age", "Layers form one after another, so they have different ages."), ("Layers are always vertical", "Layers are laid down nearly horizontally.")],
          [("Principle", "Each layer is deposited on top of an earlier one.")], "Superposition", "Recall", "Think of a pile of newspapers."),
        Q("Sediments are first laid down", "In nearly horizontal layers",
          [("As vertical sheets", "Gravity makes sediments settle flat."), ("As folded layers", "Folds form later, by compression."), ("As faults", "Faults form later, by stress.")],
          [("Principle", "Original horizontality: layers begin flat, so tilting happened later.")], "Original horizontality", "Concept", "Think of mud settling in a lake."),
        Q("In the figure, which layer is the oldest of the layered rocks?", "A",
          [("B", "B is above A."), ("D", "D is near the top."), ("E", "E is the youngest layer.")],
          [("Superposition", "The lowest layer is the oldest, so A.")], "Superposition", "Interpretation", "Look at the bottom layer.", diagram=STR, alt=STR_A),
        Q("In the figure, which layer is the youngest?", "E",
          [("A", "A is the oldest."), ("D", "E lies above D."), ("F", "F is an intrusion that cuts A to D, and E lies on top of it.")],
          [("Order", "E lies on top of everything, including the eroded top of F, so it is the youngest.")], "Superposition", "Interpretation", "Which body is on top of the others?", diagram=STR, alt=STR_A),
        Q("In the figure, the igneous body F is", "Younger than layers A to D and older than layer E",
          [("Older than layer A", "F cuts through A, so it must be younger than A."), ("Older than layers A to D", "A body that cuts across a layer is younger than it."), ("The same age as E", "E lies over the eroded top of F, so F is older.")],
          [("Cross-cutting", "F cuts A to D, so it is younger than them."), ("Not cutting E", "E lies above F and is not cut, so F is older than E.")], "Cross-cutting relationships", "Reasoning", "F stops at the amber surface.", diagram=STR, alt=STR_A),
        Q("A pebble of granite lies inside a sandstone bed. The granite is", "Older than the sandstone",
          [("Younger than the sandstone", "A fragment must exist before it can be enclosed."), ("Exactly the same age as the sandstone", "The two formed at different times."), ("Impossible to date relatively", "The principle of inclusions gives the relationship.")],
          [("Inclusions", "A fragment is older than the rock that contains it.")], "Inclusions", "Application", "The pebble had to exist first."),
        Q("Faunal succession allows geologists to", "Match rocks of the same age in different places using their fossils",
          [("Measure the age of rocks in years directly", "That needs radiometric dating."), ("Find the thickness of beds", "Fossils do not measure thickness."), ("Tell whether a rock is igneous", "Fossils are found in sedimentary rocks.")],
          [("Principle", "Fossils follow each other in a known order, so the same fossils mean the same age.")], "Faunal succession", "Concept", "Think of correlation."),
        N("A sandstone bed 18 m thick was deposited at an average rate of 0.3 mm per year. How many years did it take? (Invented figures for practice.)", 60000,
          [("Convert", "18 m = 18 000 mm."), ("Divide", "18 000 / 0.3 = 60 000 years.")], "Rate of deposition", "Calculation", "Convert to millimetres first.", unit="years"),
    ]))

# ------------------------------------------------------------------ 10. The geological time scale
use(20)
SETS.append(practice_set(
    module=M5, topic=T_TIM, title="The time scale and half-life calculations",
    lesson="gly2-geological-time-scale-half-life",
    questions=[
        Q("The age of the Earth is about", "4.6 billion years",
          [("4.6 million years", "That is far too young: it is a thousand times too small."), ("46 000 years", "That is far too young."), ("100 billion years", "That is older than the universe is thought to be.")],
          [("Fact", "The Earth is about 4.6 billion years old.")], "Age of the Earth", "Recall", "Billions, not millions."),
        Q("Which is the correct order of the eras, oldest to youngest?", "Palaeozoic, Mesozoic, Cenozoic",
          [("Mesozoic, Palaeozoic, Cenozoic", "The Palaeozoic is older than the Mesozoic."), ("Cenozoic, Mesozoic, Palaeozoic", "That is youngest to oldest."), ("Palaeozoic, Cenozoic, Mesozoic", "The Mesozoic comes before the Cenozoic.")],
          [("Memory aid", "Palaeo (old), Meso (middle), Ceno (recent).")], "Eras", "Recall", "Old, middle, recent."),
        Q("Which period is the oldest?", "Cambrian",
          [("Jurassic", "The Jurassic is in the Mesozoic, which is younger."), ("Permian", "The Permian is the last period of the Palaeozoic."), ("Quaternary", "The Quaternary is the youngest.")],
          [("Order", "The Palaeozoic begins with the Cambrian.")], "Periods", "Recall", "Which period begins the Palaeozoic?"),
        Q("Dinosaurs lived mainly in the", "Mesozoic era",
          [("Palaeozoic era", "The Palaeozoic is the age of trilobites and early fish."), ("Cenozoic era", "The Cenozoic is the age of mammals."), ("Precambrian", "There were no dinosaurs in the Precambrian.")],
          [("Fact", "The Mesozoic is often called the age of reptiles.")], "Eras", "Recall", "Mesozoic means middle life."),
        N("A charcoal sample has one eighth of the carbon-14 of a living tree. The half-life of carbon-14 is 5 730 years. How old is the sample in years?", 17190,
          [("Number of half-lives", "1/8 = (1/2)^3, so 3 half-lives."), ("Age", "3 x 5 730 = 17 190 years.")], "Radiometric dating", "Calculation", "Halve three times to reach one eighth.", unit="years"),
        N("A mineral has one sixteenth of its parent atoms left. The (invented) isotope has a half-life of 20 million years. How old is the mineral in millions of years?", 80,
          [("Number of half-lives", "1/16 = (1/2)^4, so 4 half-lives."), ("Age", "4 x 20 = 80 million years.")], "Radiometric dating", "Calculation", "How many halvings make 1/16?", unit="million years"),
        Q("Which isotope is best for dating a 30 000-year-old piece of wood?", "Carbon-14",
          [("Uranium-238", "Its half-life of 4.5 billion years is far too long to show change in 30 000 years."), ("Potassium-40", "Its half-life is 1.25 billion years, also too long."), ("None of them", "Carbon-14 is suitable for organic remains younger than about 50 000 years.")],
          [("Match half-life to age", "Choose an isotope with a half-life close to the age: carbon-14 (5 730 years).")], "Choosing an isotope", "Application", "The half-life should be a similar size to the age."),
        N("The Precambrian lasted from about 4 600 to 539 million years ago. What percentage of Earth's history is it, to the nearest whole number?", 88,
          [("Length", "4 600 - 539 = 4 061 million years."), ("Percentage", "4 061 / 4 600 x 100 = 88.3, so 88 per cent.")], "Length of the Precambrian", "Calculation", "Divide its length by 4 600.", tol=0.5, unit="%"),
    ]))

# ------------------------------------------------------------------ 11. Fossils
use(21)
SETS.append(practice_set(
    module=M5, topic=T_FOS, title="Fossils: formation and the invertebrate groups",
    lesson="gly2-fossils-invertebrate-groups",
    questions=[
        Q("A fossil is best defined as", "The preserved remains or traces of an organism that lived in the geological past",
          [("Any very old rock", "A fossil is evidence of life, not just old rock."), ("A mineral that grows in cracks", "Minerals in cracks are not life remains."), ("A living animal from an old species", "A fossil is not alive.")],
          [("Definition", "A fossil is preserved evidence of ancient life found in rock.")], "Definition of a fossil", "Recall", "It is evidence of life."),
        Q("Which conditions favour fossilization?", "Hard parts and rapid burial in a low-oxygen setting",
          [("Soft body and slow burial in open air", "Such remains decay or are eaten."), ("Burial in hot flowing lava", "Lava would destroy the remains."), ("Fast erosion of the sea bed", "Erosion exposes remains to decay.")],
          [("Protection", "Hard parts last longer and quick burial protects them from scavengers and decay.")], "Conditions for fossilization", "Concept", "What stops remains from rotting or being eaten?"),
        Q("A shell dissolves and leaves a hollow in the rock with the shape of its outside. This is a", "Mould",
          [("Cast", "A cast is formed when minerals fill the mould."), ("Trace fossil", "A trace fossil is a footprint or burrow."), ("Carbonised film", "Carbonisation leaves a black carbon film.")],
          [("Definition", "The hollow is the mould. A filled mould is a cast.")], "Preservation", "Concept", "A hollow impression."),
        Q("A fossil shows a head shield, a segmented thorax and a tail shield. It is a", "Trilobite",
          [("Ammonite", "Ammonites are coiled shells."), ("Graptolite", "Graptolites are thin saw-blade colonies."), ("Gastropod", "Gastropods are single spiral shells.")],
          [("Features", "Three body parts and a segmented body: a trilobite.")], "Trilobites", "Recall", "Three parts lengthways."),
        Q("A coiled shell with chambers separated by walls showing wavy sutures is an", "Ammonite",
          [("Brachiopod", "Brachiopods have two valves."), ("Coral", "Corals have radial septa and are not coiled."), ("Trilobite", "Trilobites have segmented bodies.")],
          [("Features", "Coiled, chambered shell with suture lines: ammonite.")], "Ammonites", "Recall", "Look for the wavy sutures."),
        Q("Which feature distinguishes a bivalve from a brachiopod?", "The two valves are equal and are mirror images of each other",
          [("It has two valves", "Both groups have two valves."), ("It lived in the sea", "Both groups are marine."), ("It has a hard shell", "Both have hard shells.")],
          [("Key difference", "A bivalve has equal left and right valves; a brachiopod's valves are of different sizes.")], "Bivalve and brachiopod", "Concept", "Compare the valves in size."),
        Q("A rock contains graptolites. These fossils are mainly useful for dating rocks from the", "Ordovician and Silurian",
          [("Jurassic and Cretaceous", "Ammonites are the useful index fossils of those periods."), ("Quaternary", "Graptolites became extinct long before the Quaternary."), ("Precambrian", "Graptolites appeared after the Precambrian.")],
          [("Range", "Graptolites are best known as index fossils of the Ordovician and Silurian (check your textbook for exact ranges).")], "Graptolites", "Application", "They are Early Palaeozoic fossils."),
        Q("A layer contains both trilobites (Cambrian to Permian) and ammonites (Devonian to Cretaceous). The layer could be from the", "Devonian, Carboniferous or Permian",
          [("Cambrian or Ordovician", "Ammonites had not yet appeared."), ("Jurassic or Cretaceous", "Trilobites were extinct by then."), ("Triassic only", "Trilobites were extinct by the Triassic.")],
          [("Overlap", "Cambrian-Permian overlaps Devonian-Cretaceous from the Devonian to the Permian.")], "Using fossil ranges", "Reasoning", "Find the time when both groups existed."),
    ]))

# ------------------------------------------------------------------ 12. Hydrologic cycle and groundwater
CYQ = "f5gly2-cycle-q.svg"
CYQ_A = "Water cycle diagram: sea on the left, hill on the right, cloud above. A is the arrow rising from the sea, B the cloud, C the rain, D the arrow down the slope on the surface, E the arrow down into the ground, F the arrow along the underground dashed line"
use(22)
SETS.append(practice_set(
    module=M6, topic=T_HYD, title="The water cycle, porosity and the water table",
    lesson="gly2-hydrologic-cycle-groundwater",
    questions=[
        Q("Hydrogeology is the study of", "Groundwater",
          [("All the water on Earth", "That is too wide: hydrogeology concerns water below the ground."), ("Rainfall only", "Rainfall is part of meteorology and the water cycle."), ("Rivers and lakes only", "Surface water is studied in hydrology.")],
          [("Definition", "Hydrogeology is the study of groundwater: its occurrence, movement and quality.")], "Hydrogeology", "Recall", "It is about water underground."),
        Q("In the figure, the process marked A, from the sea to the air, is", "Evaporation",
          [("Condensation", "Condensation makes clouds from vapour."), ("Infiltration", "Infiltration is entry into the ground."), ("Precipitation", "Precipitation is rain, hail or snow falling.")],
          [("Direction", "Liquid water becoming vapour and rising: evaporation.")], "Hydrologic cycle", "Interpretation", "Water is rising from the sea.", diagram=CYQ, alt=CYQ_A),
        Q("In the figure, the process marked E, water going down into the ground, is", "Infiltration",
          [("Runoff", "Runoff is flow over the ground surface."), ("Evaporation", "Evaporation is upward."), ("Condensation", "Condensation happens in the air.")],
          [("Direction", "Water soaking into soil and rock is infiltration.")], "Hydrologic cycle", "Interpretation", "The arrow points into the ground.", diagram=CYQ, alt=CYQ_A),
        Q("In the figure, the arrow D down the surface of the slope shows", "Runoff",
          [("Infiltration", "Infiltration goes downward into the soil."), ("Condensation", "Condensation is in the air."), ("Groundwater flow", "Groundwater flows below the surface.")],
          [("Position", "Flow over the surface towards the sea is runoff.")], "Hydrologic cycle", "Interpretation", "It flows over the ground surface.", diagram=CYQ, alt=CYQ_A),
        Q("Porosity is", "The percentage of a rock that is empty space",
          [("How fast water flows through a rock", "That is permeability."), ("The depth of the water table", "That is a different measurement."), ("The hardness of a rock", "Hardness is a mineral property.")],
          [("Definition", "Porosity = volume of pores / total volume x 100.")], "Porosity", "Recall", "It measures space, not speed."),
        N("A 500 cm3 sample of sand has pore spaces totalling 175 cm3. What is its porosity?", 35,
          [("Formula", "Porosity = pore volume / total volume x 100."), ("Substitute", "175 / 500 x 100 = 35 per cent.")], "Calculating porosity", "Calculation", "Divide the pore volume by the total volume.", unit="%"),
        Q("Clay can hold a lot of water but a well in clay yields little, because clay is", "Porous but not permeable",
          [("Permeable but not porous", "Clay's pores are tiny, so water cannot flow quickly."), ("Neither porous nor permeable", "Clay does have many small pores."), ("Both highly porous and highly permeable", "Clay has very low permeability.")],
          [("Storage and flow", "Clay stores water in tiny pores but they are poorly connected, so water cannot move quickly.")], "Porosity and permeability", "Concept", "Separate storage from flow."),
        Q("The water table is", "The top of the zone in which all pores are full of water",
          [("The bottom of the zone in which all pores are full of water", "That is the lower boundary at the impermeable layer."), ("The ground surface", "The water table is usually below the surface."), ("The level of the nearest river bed always", "It may be above or below that.")],
          [("Definition", "Below the water table is the zone of saturation.")], "Water table", "Concept", "Think of the upper surface of the saturated zone."),
    ]))

# ------------------------------------------------------------------ 13. Aquifers, springs and wells
UNQ2 = "f5gly2-unconfined-q.svg"
UNQ2_A = "Cross-section of ground with a dashed blue water table, a vertical well shaft, a place where water flows out at the ground surface and a blue saturated zone above a clay layer. Letter A is on the dashed line, B at the place where water flows out, C on the well and D in the saturated zone"
ARQ = "f5gly2-artesian-q.svg"
ARQ_A = "Cross-section: a blue layer dipping between two grey clay layers under sloping ground, rain on high ground at left, a dashed line above the ground on the right and a well. B is on the clay above, C on the blue layer, D on the dashed line, E at the well"
use(23)
SETS.append(practice_set(
    module=M6, topic=T_AQU, title="Aquifers, springs, wells and artesian water",
    lesson="gly2-aquifers-springs-wells",
    questions=[
        Q("An aquifer is a rock that is", "Porous and permeable so that it stores and yields water",
          [("Porous but impermeable", "Such a rock stores water but does not yield it."), ("Impermeable and non-porous", "That would be a barrier to water."), ("Igneous and dense", "Rock type alone does not define an aquifer.")],
          [("Definition", "An aquifer both stores and transmits water.")], "Aquifer", "Recall", "It must hold water and let it flow."),
        Q("In the figure, the dashed line marked A is the", "Water table",
          [("Fault plane", "A fault plane is a fracture surface."), ("Bedding plane", "A bedding plane separates layers."), ("Pressure surface of an artesian well", "That belongs to a confined aquifer.")],
          [("Position", "The top of the saturated zone is the water table.")], "Water table", "Interpretation", "The dashed line is the top of the water-filled zone.", diagram=UNQ2, alt=UNQ2_A),
        Q("In the figure, a spring appears at B because", "The water table meets the ground surface there",
          [("The clay layer is permeable", "Clay is impermeable."), ("The well is pumping", "A spring flows naturally."), ("The rock is dry", "A dry rock could not release water.")],
          [("Cause", "Where the water table reaches the surface, groundwater flows out as a spring.")], "Springs", "Interpretation", "Where does the water table cut the surface?", diagram=UNQ2, alt=UNQ2_A),
        Q("The clay layer under the saturated zone in the same figure is useful because it", "Does not let the water drain downwards",
          [("Is very porous and permeable", "Clay is impermeable."), ("Heats the water", "Clay does not heat water."), ("Adds oxygen", "Clay does not add oxygen.")],
          [("Impermeable layer", "It blocks downward flow so water collects above it.")], "Impermeable layers", "Concept", "Think of a floor that holds water."),
        Q("In the artesian figure, the layer marked C is the", "Aquifer",
          [("Confining layer", "That is B, the clay above."), ("Pressure surface", "That is the dashed line D."), ("Recharge area", "Recharge area is where rain enters at the high end.")],
          [("Position", "The porous, permeable layer between the clays is the aquifer, C.")], "Artesian aquifer", "Interpretation", "It is the water-filled layer between the clay layers.", diagram=ARQ, alt=ARQ_A),
        Q("In the artesian figure, the dashed line D shows", "The level to which the water in the confined aquifer would rise",
          [("The water table of an unconfined aquifer", "A confined aquifer does not have a free water table."), ("The ground surface", "The ground is the solid black line."), ("The top of the clay layer", "The clay is the shaded layer.")],
          [("Pressure surface", "The dashed line is the potentiometric (pressure) surface.")], "Pressure surface", "Interpretation", "It slopes above the ground on the right.", diagram=ARQ, alt=ARQ_A),
        Q("Why does water flow out of the artesian well at E without pumping?", "The pressure surface lies above the ground at the well",
          [("The well is very deep", "Depth does not cause flow."), ("The clay layer is permeable", "Clay is impermeable and confines the water."), ("Rain falls on the well", "Rain is not the cause here.")],
          [("Pressure", "Water at depth is under the pressure of the water column from the recharge area, so it rises to the pressure surface and spills out.")], "Artesian well", "Reasoning", "Compare the dashed line to the ground at the well.", diagram=ARQ, alt=ARQ_A),
        N("A borehole yields 1.5 cubic metres of water per hour and is pumped for 8 hours a day. Each person uses 25 litres a day (1 cubic metre = 1 000 litres). How many people can it supply?", 480,
          [("Daily volume", "1.5 x 8 = 12 cubic metres = 12 000 litres."), ("People", "12 000 / 25 = 480.")], "Borehole supply", "Calculation", "Convert cubic metres to litres.", unit="people"),
    ]))

# ------------------------------------------------------------------ 14. Petroleum, natural gas and coal
TRQ = "f5gly2-trap-q.svg"
TRQ_A = "Cross-section of an arched rock structure with a well at the crest. A is on the grey top layer, B on the pale yellow layer holding fluids, C on the dark layer at the bottom, D on the green fluid at the very top of the arch and E on the orange fluid below it"
use(24)
SETS.append(practice_set(
    module=M6, topic=T_PET, title="Petroleum, natural gas and coal",
    lesson="gly2-petroleum-gas-coal",
    questions=[
        Q("Petroleum forms mainly from", "The remains of tiny marine organisms buried in mud",
          [("Fragments of granite", "Granite is igneous rock with no organic matter."), ("Volcanic ash", "Ash is not a source of hydrocarbons."), ("Pure quartz sand", "Quartz sand has no organic matter.")],
          [("Origin", "Plankton and algae buried in oxygen-poor mud are changed by heat and pressure into oil and gas.")], "Origin of petroleum", "Recall", "It is a fossil fuel."),
        Q("In the figure, the layer marked A, which stops the oil from escaping upwards, is the", "Cap rock",
          [("Reservoir rock", "The reservoir rock holds the fluids and is B."), ("Source rock", "The source rock is C, the layer where the oil forms."), ("Bedrock only", "A cap rock is defined by its function.")],
          [("Function", "An impermeable seal on top of the reservoir is the cap rock.")], "Cap rock", "Interpretation", "Which layer is impermeable and on top?", diagram=TRQ, alt=TRQ_A),
        Q("In the figure, the layer marked B, which is porous and permeable and holds the oil, is the", "Reservoir rock",
          [("Cap rock", "That is the grey top layer, A."), ("Source rock", "The source rock is C."), ("Gangue", "Gangue is waste mineral in an ore.")],
          [("Function", "Porous, permeable rock that stores oil is the reservoir rock.")], "Reservoir rock", "Interpretation", "It holds the fluids.", diagram=TRQ, alt=TRQ_A),
        Q("In the figure, the fluid marked D at the very top of the arch is", "Natural gas",
          [("Water", "Water, the densest fluid, is at the bottom."), ("Crude oil", "Oil lies below the gas; it is E."), ("Brine from the sea", "Brine is water, which lies at the bottom.")],
          [("Density", "Gas is the lightest fluid and collects at the top, above the oil.")], "Fluids in a trap", "Interpretation", "Which fluid is lightest?", diagram=TRQ, alt=TRQ_A),
        Q("In the figure, the fluid E, below the gas, is", "Oil",
          [("Gas", "Gas is the lightest and lies above."), ("Granite", "Granite is a rock, not a fluid."), ("Coal", "Coal is a solid.")],
          [("Order", "From the top: gas, oil, water.")], "Fluids in a trap", "Interpretation", "It lies between the gas and the water.", diagram=TRQ, alt=TRQ_A),
        Q("Which is the correct order of coal types from lowest to highest rank?", "Peat, lignite, bituminous coal, anthracite",
          [("Anthracite, bituminous coal, lignite, peat", "That is from highest to lowest."), ("Lignite, peat, anthracite, bituminous coal", "Peat is the first stage."), ("Peat, bituminous coal, lignite, anthracite", "Lignite comes before bituminous coal.")],
          [("Process", "More burial, heat and pressure raise the rank.")], "Coal formation", "Recall", "Start from unaltered plants."),
        N("A reservoir covers 1 square kilometre and is 20 m thick. Its porosity is 25% and 80% of the pores hold oil. How many cubic metres of oil are there? (Invented figures.)", 4000000,
          [("Rock volume", "1 000 000 m2 x 20 m = 20 000 000 m3."), ("Pore volume", "20 000 000 x 0.25 = 5 000 000 m3."), ("Oil", "5 000 000 x 0.80 = 4 000 000 m3.")], "Reservoir volume", "Calculation", "Multiply rock volume by porosity, then by the oil fraction.", unit="m3"),
        Q("Cameroon's offshore oil is associated with which sedimentary basin? (Check your textbook for details.)", "Rio del Rey basin",
          [("Lake Chad basin", "Check your textbook: this is not the one named for Cameroon's offshore oil."), ("Congo Basin only", "The Congo Basin is not the main offshore oil basin."), ("Sahara basin", "That is not a Cameroonian oil basin.")],
          [("Basin", "The Rio del Rey basin in the south-west is a producing offshore basin, named in the blueprint with the Douala basin.")], "Cameroon's petroleum basins", "Recall", "It is named in the blueprint with the Douala basin."),
    ]))

# ------------------------------------------------------------------ 15. Ore deposits and mineral resources of Cameroon
use(25)
SETS.append(practice_set(
    module=M6, topic=T_ORE, title="Ore, gangue and tenor: Cameroon's mineral resources",
    lesson="gly2-ore-deposits-cameroon-resources",
    questions=[
        Q("Gangue is", "The unwanted mineral found in an ore",
          [("The metal content of an ore", "That is the tenor."), ("The mineral that contains the metal", "That is the ore mineral."), ("The rock above an ore body", "That is overburden.")],
          [("Definition", "Gangue is the worthless mineral that occurs with the ore mineral.")], "Gangue", "Recall", "It is waste."),
        Q("Mineral tenor means", "The metal content of an ore",
          [("The size of the ore body", "Tenor is about concentration, not size."), ("The hardness of the ore", "Hardness is a physical property."), ("The depth of the ore", "Depth is a different factor.")],
          [("Definition", "Tenor is the metal content, for example grams of metal per tonne.")], "Tenor", "Recall", "It tells you how rich the ore is."),
        Q("An ore mineral is a mineral deposit that", "Contains a metal and can be mined at a profit",
          [("Contains any metal at all", "It must be profitable to mine."), ("Is made only of gold", "Many metals have ore minerals."), ("Is found only in igneous rock", "Ores occur in all kinds of rock.")],
          [("Definition", "A metal-bearing deposit that can be mined at a profit.")], "Ore mineral", "Recall", "It must pay."),
        Q("Bauxite, the ore of aluminium, forms mainly by", "Deep weathering and leaching in a hot, wet climate",
          [("Cooling of lava in the sea", "That makes basalt, not bauxite."), ("Metamorphism of limestone", "Limestone gives marble."), ("Glacial erosion", "Glaciers do not form bauxite.")],
          [("Process", "Rain leaches other material away and leaves an aluminium-rich residue.")], "Bauxite", "Concept", "Think of tropical weathering."),
        Q("Gold and rutile are often found in river sands and gravels because they are", "Dense, hard and resistant to weathering",
          [("Light and soluble", "If they were soluble they would dissolve."), ("Formed only in the sea", "They come from weathered rock."), ("Always found in limestone", "They are not typical of limestone.")],
          [("Placer process", "Dense, resistant minerals settle in river gravels where the flow slows.")], "Placer deposits", "Concept", "They are heavy."),
        Q("Which resource is the raw material for cement?", "Limestone",
          [("Rutile", "Rutile is an ore of titanium."), ("Gold", "Gold is a precious metal."), ("Bauxite", "Bauxite is an ore of aluminium.")],
          [("Use", "Cement is made from limestone, a calcium carbonate rock.")], "Limestone", "Recall", "It is made from calcium carbonate."),
        N("An ore has a tenor of 4 grams of gold per tonne. How many grams of gold are in 500 tonnes of this ore?", 2000,
          [("Multiply", "500 x 4 = 2 000 grams.")], "Tenor calculation", "Calculation", "Multiply tonnes by grams per tonne.", unit="g"),
        Q("A deposit has a tenor of 4 g/t. Gold is worth FCFA 30 000 per gram (an invented price), and mining and processing cost FCFA 150 000 per tonne. Is it an ore?", "No, the value of a tonne (FCFA 120 000) is below the cost",
          [("Yes, because it contains gold", "To be an ore it must be mined at a profit."), ("Yes, the value is FCFA 600 000 per tonne", "The value is 4 x 30 000 = 120 000, not 600 000."), ("Cannot be decided without the age of the rock", "Age is not needed: compare value and cost.")],
          [("Value", "4 x 30 000 = FCFA 120 000 per tonne."), ("Compare", "120 000 is less than the cost of 150 000, so there would be a loss: not an ore at that price.")], "Is it an ore?", "Reasoning", "Compare the value of one tonne with its cost."),
    ]))

# ------------------------------------------------------------------ 16. Geohazards
use(26)
SETS.append(practice_set(
    module=M6, topic=T_GEO, title="Geohazards and the Lake Nyos and Monoun disasters",
    lesson="gly2-geohazards-earthquakes-volcanoes-lakes",
    questions=[
        Q("The point on the Earth's surface directly above the focus of an earthquake is the", "Epicentre",
          [("Focus", "The focus is the point underground where the rock breaks."), ("Fault plane", "The fault plane is the fracture surface."), ("Magnitude", "Magnitude measures the energy released.")],
          [("Definition", "Focus is below; epicentre is on the surface above it.")], "Earthquake terms", "Recall", "It is on the surface."),
        Q("The gas that killed people at Lake Nyos in 1986 was mainly", "Carbon dioxide",
          [("Methane burning in air", "No fire was involved."), ("Chlorine", "Chlorine was not involved."), ("Oxygen", "Oxygen is not harmful; the gas displaced it.")],
          [("Cause", "A cloud of carbon dioxide released from the lake suffocated people and animals.")], "Lake Nyos", "Recall", "It is the gas we breathe out."),
        Q("Carbon dioxide from the lake was so deadly because it is", "Heavier than air, colourless and without smell",
          [("Lighter than air and rises away", "It would then have blown away from the villages."), ("Hot enough to burn", "The cloud was not a fire."), ("Radioactive", "It is not radioactive.")],
          [("Properties", "It flowed down valleys, filled low ground and gave no warning.")], "Why the gas was deadly", "Concept", "It flowed into valleys."),
        Q("Which pair of lake and year is correct?", "Lake Monoun 1984 and Lake Nyos 1986",
          [("Lake Monoun 1986 and Lake Nyos 1984", "The years are swapped."), ("Lake Monoun 1990 and Lake Nyos 1994", "Both dates are wrong."), ("Lake Nyos 1950 and Lake Monoun 1960", "There were no disasters in those years.")],
          [("Dates", "Monoun, August 1984; Nyos, August 1986.")], "Lake Monoun and Nyos", "Recall", "Monoun was first."),
        Q("Which action reduces the danger of gas release from a crater lake?", "Installing degassing pipes",
          [("Building houses beside the lake", "That increases the risk."), ("Adding more rock to the lake bottom", "That does not remove the gas."), ("Closing off all warnings", "Warnings reduce risk.")],
          [("Engineering", "Pipes let dissolved gas escape slowly and safely.")], "Reducing risk", "Application", "Which action takes the gas out slowly?"),
        Q("Which volcanic hazard is a hot, fast-moving cloud of gas and ash?", "A pyroclastic flow",
          [("A lava flow", "Lava flows are slow-moving streams of molten rock."), ("A lahar", "A lahar is a mudflow of ash and water."), ("An ash fall", "Ash fall is settling of ash from the air.")],
          [("Definition", "Fast, hot clouds of gas and ash are pyroclastic flows.")], "Volcanic hazards", "Recall", "It is hot and very fast."),
        N("How many times more energy is released by a magnitude 8 earthquake than by a magnitude 6? Use 10 to the power 1.5 (about 31.6) per magnitude unit and give the answer to the nearest 100.", 1000,
          [("Difference", "8 - 6 = 2 units."), ("Energy ratio", "31.6 x 31.6 = 1 000 (exactly 10 to the power 3).")], "Magnitude and energy", "Calculation", "Raise the factor to the number of units of difference.", tol=100, unit="times"),
        N("A seismograph records the S wave 15 s after the P wave. P waves travel at 6.0 km/s and S waves at 3.5 km/s (invented values). How far is the epicentre in km?", 126,
          [("Equation", "d/3.5 - d/6.0 = 15."), ("Solve", "d x 0.119 = 15, so d = 126 km.")], "Distance from S-P lag", "Calculation", "The difference in travel times equals the lag.", tol=1, unit="km"),
    ]))

# ------------------------------------------------------------------ 17. Examination: Paper 1 strategies
use(27)
SETS.append(practice_set(
    module=M7, topic="Paper 1", title="Paper 1 strategies: structure, time and definitions",
    lesson="gly2-exam-paper-1-multiple-choice-strategies",
    questions=[
        Q("According to the Board's 2023 report, Geology Paper 1 consists of", "50 multiple-choice questions, all to be answered",
          [("7 structural questions, 5 to be answered", "That describes Paper 2."), ("25 essay questions", "Paper 1 is multiple choice."), ("A school-based project", "The school-based assessment is Question 7 of Paper 2, not Paper 1.")],
          [("Fact", "Paper 1: 50 MCQs, all answered.")], "Paper 1 structure", "Recall", "Paper 1 is the multiple-choice paper."),
        N("In KKEVO's practice mock, Paper 1 has 50 questions in 90 minutes. What is the average number of minutes for each question?", 1.8,
          [("Divide", "90 / 50 = 1.8 minutes.")], "Time per question", "Calculation", "Divide the total time by the number of questions.", tol=0.01, unit="minutes"),
        Q("In the two-pass method, what do you do in the first pass?", "Answer the questions you can do quickly and tick the others",
          [("Spend five minutes on each hard question", "That wastes time that easy questions need."), ("Guess every question at once", "Guessing everything is not a plan."), ("Read only the last question", "You need to see all questions.")],
          [("Plan", "First pass: easy marks. Second pass: ticked questions. Then check.")], "Two-pass method", "Application", "Easy marks first."),
        Q("A question says: 'Which of these is NOT a physical property of a mineral?' Options: streak, lustre, cleavage, oxidation. The best method is to", "Find the three properties and choose the odd one out",
          [("Choose the first property you recognise", "That is a true property, so it cannot be the answer."), ("Choose the longest option", "Length does not decide anything."), ("Skip all questions with NOT", "You would lose easy marks.")],
          [("Elimination", "Three options are properties. Oxidation is a weathering process, so it is the answer.")], "Elimination", "Reasoning", "Cross out the options that are true."),
        Q("Streak is", "The colour of the powder of a mineral",
          [("The powder of a mineral", "Streak is the colour of the powder, not the powder itself."), ("The way a mineral breaks", "That is cleavage or fracture."), ("The appearance of a mineral in reflected light", "That is lustre.")],
          [("Definition", "Streak is the colour of a mineral in powder form.")], "Precise definitions", "Recall", "It is a colour."),
        Q("A plane of symmetry in a crystal is", "A surface dividing the crystal into two mirror-image halves",
          [("An imaginary line about which the crystal rotates", "That is an axis of symmetry."), ("A point at the middle of the crystal", "That is the centre of symmetry."), ("A flat crystal face", "A face is not a plane of symmetry.")],
          [("Definition", "A plane is a surface; an axis is a line.")], "Precise definitions", "Recall", "Plane means surface."),
        N("On a map, 4 cm on the scale bar represents 10 km. Find the denominator of the numerical scale 1 : n.", 250000,
          [("Convert", "10 km = 1 000 000 cm."), ("Divide", "1 000 000 / 4 = 250 000.")], "Scale conversion", "Calculation", "Convert 10 km to centimetres first.", unit=""),
        Q("A sample has 25% of its parent isotope left. How many half-lives have passed?", "2",
          [("1", "One half-life leaves 50%."), ("3", "Three half-lives leave 12.5%."), ("4", "Four half-lives leave 6.25%.")],
          [("Halve", "100% to 50% to 25%: two halvings.")], "Calculation checks", "Calculation", "Halve the amount until you reach 25%."),
    ]))

# ------------------------------------------------------------------ 18. Examination: Paper 2 strategies
use(28)
SETS.append(practice_set(
    module=M7, topic="Paper 2", title="Paper 2 strategies: choice, definitions and map work",
    lesson="gly2-exam-paper-2-structured-questions-maps",
    questions=[
        Q("According to the Board's 2023 report, Paper 2 of Geology has seven structural questions. A candidate must answer", "Five: two from Section A, two from Section B and compulsory Question 7",
          [("All seven", "Only five are answered."), ("Three from each section", "The rule is two from each of A and B plus Question 7."), ("Two from Section A and Question 7 only", "Two from Section B are also required.")],
          [("Rule", "2 + 2 + 1 = 5.")], "Paper 2 structure", "Recall", "Add the numbers from each part."),
        Q("Question 7 of Paper 2 is", "A compulsory school-based assessment question",
          [("An optional essay in Section A", "It is compulsory and not in Section A."), ("A multiple-choice question", "Paper 2 questions are structural."), ("A question that is dropped when you have answered four others", "It must be answered.")],
          [("Fact", "Q7 is school-based assessment and compulsory; ask your teacher what it involves in your school.")], "School-based assessment", "Recall", "It is the compulsory one."),
        Q("Which definition would earn the mark for hydrogeology?", "The study of groundwater",
          [("The study of water", "This is too general: examiners reported it as a common error."), ("The study of rocks beneath the sea", "That describes marine geology."), ("The study of rainfall", "That is meteorology.")],
          [("Exact wording", "Hydrogeology is the study of groundwater.")], "Exact definitions", "Recall", "It is about water underground."),
        Q("On a map, all the boundaries between beds run parallel to the contour lines. The beds are", "Horizontal",
          [("Vertical", "Vertical beds give straight boundaries that cross contours."), ("Folded into a dome", "A dome shows circular outcrop patterns that cross contours."), ("Overturned", "No such evidence is given.")],
          [("Reason", "A bed that is horizontal has the same height everywhere, so its boundary follows a contour.")], "Reading beds on a map", "Concept", "A contour joins points of equal height."),
        Q("When drawing a profile along line A to B, the ground surface should", "Follow the heights where the line crosses the contours",
          [("Be a straight horizontal line", "Examiners reported this as a common error."), ("Be drawn as a straight slope from A to B", "The surface rises and falls with the land."), ("Not be drawn", "The ground surface is the first part of the profile.")],
          [("Method", "Plot the heights read at each contour crossing and join them smoothly.")], "Drawing a profile", "Application", "Use the heights along the line."),
        N("The horizontal scale of a profile is 1 : 50 000 and the vertical scale is 1 : 10 000. What is the vertical exaggeration?", 5,
          [("Formula", "Vertical exaggeration = horizontal denominator / vertical denominator."), ("Calculate", "50 000 / 10 000 = 5.")], "Vertical exaggeration", "Calculation", "Divide the larger denominator by the smaller.", unit="times"),
        N("On a graphical scale, 5 cm represents 20 km. Find the real distance, in km, represented by 7 cm.", 28,
          [("Find km per cm", "20 / 5 = 4 km per cm."), ("Multiply", "7 x 4 = 28 km.")], "Using a graphical scale", "Calculation", "Find how many kilometres 1 cm stands for.", unit="km"),
        N("The ground rises by 120 m over a horizontal distance of 2.4 km. The gradient is 1 in n. Find n.", 20,
          [("Convert", "2.4 km = 2 400 m."), ("Divide", "2 400 / 120 = 20, so the gradient is 1 in 20.")], "Gradient", "Calculation", "Use the same units, then divide distance by height.", unit=""),
    ]))

# ------------------------------------------------------------------ 19. Paper 1 mock exam A (50 questions)
use(29)
P1 = [
    # Module 1: Introduction, Solar System & Global Tectonics (6)
    Q("Which branch of geology is the study of fossils?", "Palaeontology",
      [("Mineralogy", "Mineralogy is the study of minerals."), ("Petrology", "Petrology is the study of rocks."), ("Seismology", "Seismology is the study of earthquakes.")],
      [("Branches", "Palaeontology deals with fossils.")], T_BR, "Recall", "Palaeo means ancient."),
    Q("The asteroid belt lies between the orbits of", "Mars and Jupiter",
      [("Earth and Mars", "Mars follows Earth directly; the belt is further out."), ("Jupiter and Saturn", "The belt is nearer the Sun."), ("Venus and Earth", "These are inner planets with no belt between them.")],
      [("Position", "The main asteroid belt is between Mars and Jupiter.")], T_SOL, "Recall", "Think of the order of the planets from the Sun."),
    Q("Which type of seismic wave cannot travel through a liquid?", "S waves",
      [("P waves", "P waves travel through solids and liquids."), ("Both P and S waves", "P waves can pass through liquids."), ("Neither of them", "P waves do pass through liquids.")],
      [("Evidence", "S waves stop at the liquid outer core.")], T_SEI, "Recall", "One type is shear waves."),
    Q("The boundary between the crust and the mantle is called the", "Mohorovicic discontinuity (Moho)",
      [("Gutenberg discontinuity", "That is the core-mantle boundary."), ("Lehmann discontinuity", "That is between the outer and inner core."), ("Plimsoll line", "That is a mark on ships.")],
      [("Boundary", "The Moho separates the crust from the mantle.")], T_SEI, "Recall", "It is named after a Croatian seismologist."),
    Q("Which observation supports continental drift?", "The coastlines of South America and Africa fit together like jigsaw pieces",
      [("All oceans have the same depth", "Ocean depth varies."), ("Volcanoes occur only on land", "Many volcanoes occur on the sea floor."), ("All rocks are the same age", "Rocks vary in age.")],
      [("Evidence", "Matching coastlines, rocks and fossils across the Atlantic support the idea.")], T_PLA, "Concept", "Look at a world map."),
    Q("At a convergent boundary where oceanic crust meets continental crust, the oceanic plate", "Is subducted beneath the continental plate",
      [("Rises above the continental plate", "Oceanic crust is denser, so it sinks."), ("Stays level with it", "One plate is forced beneath the other."), ("Splits into two new plates", "That happens at divergent boundaries.")],
      [("Density", "Oceanic crust is denser, so it descends into the mantle.")], T_PLA, "Concept", "Which crust is denser?"),
    # Module 2: Crystallography & Mineralogy (6)
    Q("An axis of symmetry in a crystal is", "An imaginary line about which the crystal can be rotated through 360 degrees so that a face appears more than once",
      [("A surface dividing the crystal into mirror-image halves", "That is a plane of symmetry."), ("The point at the centre of the crystal", "That is the centre of symmetry."), ("The edge where two faces meet", "That is a crystal edge.")],
      [("Definition", "An axis is a line, a plane is a surface.")], T_CRY, "Recall", "An axis is a line."),
    Q("A crystal with a plane of symmetry can be divided into", "Two halves, one the mirror image of the other",
      [("Two identical halves that are rotated copies", "That describes rotational symmetry."), ("Three unequal parts", "Planes divide into two halves."), ("Two halves of different shapes", "The halves are mirror images.")],
      [("Definition", "A plane of symmetry gives mirror-image halves.")], T_CRY, "Concept", "Think of a mirror."),
    Q("Which crystal system has three axes of equal length at right angles to one another?", "Cubic",
      [("Hexagonal", "Hexagonal has three equal axes in one plane at 120 degrees and a fourth axis at right angles."), ("Monoclinic", "Monoclinic axes are of unequal length."), ("Triclinic", "Triclinic axes are unequal and not at right angles.")],
      [("Definition", "Cubic (isometric): three equal axes at 90 degrees.")], T_SIX, "Recall", "Think of a cube."),
    Q("The colour of the powder of a mineral is its", "Streak",
      [("Lustre", "Lustre is the appearance in reflected light."), ("Cleavage", "Cleavage is the tendency to split along planes."), ("Fracture", "Fracture is the nature of a freshly broken surface.")],
      [("Definition", "Streak is the colour of the powdered mineral.")], T_PHY, "Recall", "A mineral is rubbed on a plate."),
    Q("Quartz has a Mohs hardness of 7 and calcite 3. Which statement is correct?", "Quartz can scratch calcite",
      [("Calcite can scratch quartz", "The harder mineral scratches the softer one."), ("They are equally hard", "7 and 3 are different."), ("Neither scratches the other", "Quartz scratches calcite.")],
      [("Rule", "A mineral scratches any mineral with a lower hardness number.")], T_PHY, "Application", "Higher number means harder."),
    Q("Which group of minerals is the most abundant in the Earth's crust?", "Silicates",
      [("Carbonates", "Carbonates are common but less abundant."), ("Sulphides", "Sulphides are mostly in ore deposits."), ("Native elements", "Native elements are rare.")],
      [("Fact", "Silicate minerals, such as feldspar and quartz, make up most of the crust.")], T_RFM, "Recall", "Think of quartz and feldspar."),
    # Module 3: Petrology (8)
    Q("In the rock cycle, a sedimentary rock that is heated and squeezed deep in the crust may become a", "Metamorphic rock",
      [("Igneous rock directly without melting", "Igneous rock forms from melt."), ("Loose sediment", "That needs weathering and erosion."), ("Fossil", "A fossil is not a rock type.")],
      [("Process", "Heat and pressure without melting give metamorphic rock.")], T_CYC, "Concept", "No melting is involved."),
    Q("Granite is coarse-grained because it", "Cooled slowly deep underground",
      [("Cooled quickly at the surface", "Fast cooling gives fine grains."), ("Was formed from sand", "Granite is igneous, not sedimentary."), ("Was formed from shells", "Granite is not organic.")],
      [("Cooling rate", "Slow cooling allows large crystals to grow.")], T_IGN, "Concept", "Larger crystals need more time."),
    Q("An igneous intrusion that cuts across the bedding of the surrounding rock is a", "Dyke",
      [("Sill", "A sill lies parallel to the bedding."), ("Lava flow", "A lava flow lies on the surface."), ("Ash layer", "Ash falls on the surface.")],
      [("Definition", "A dyke is discordant; a sill is concordant.")], T_IGN, "Recall", "A sill is parallel to the beds."),
    Q("Mount Cameroon is part of a chain of volcanoes and crater lakes called the", "Cameroon Volcanic Line",
      [("Mid-Atlantic Ridge", "That is an underwater ridge in the Atlantic."), ("East African Rift", "That is a rift valley in East Africa."), ("Andes", "The Andes are in South America.")],
      [("Fact", "Mount Cameroon lies on the Cameroon Volcanic Line.")], T_VOL, "Recall", "The name includes the country."),
    Q("Sandstone is classified as a", "Clastic sedimentary rock",
      [("Chemical sedimentary rock", "Chemical rocks form from dissolved material."), ("Foliated metamorphic rock", "Sandstone is not metamorphic."), ("Extrusive igneous rock", "Sandstone is not igneous.")],
      [("Type", "Sandstone is made of grains of sand cemented together.")], T_SED, "Recall", "It is made of grains."),
    Q("A bed in which grain size changes gradually, coarse at the bottom and fine at the top, shows", "Graded bedding",
      [("Ripple marks", "Ripple marks are undulations on the bed surface."), ("Cross-bedding", "Cross-bedding shows inclined layers inside a bed."), ("Mud cracks", "Mud cracks show drying.")],
      [("Definition", "Graded bedding: coarse at the bottom, fine at the top.")], T_SED, "Recall", "Look at the grain size."),
    Q("Limestone changes into marble by", "Heat and pressure that recrystallise the calcite",
      [("Cooling of lava", "Lava makes igneous rocks."), ("Compaction of sand", "Compaction makes sandstone."), ("Evaporation of sea water", "That makes salt rocks.")],
      [("Metamorphism", "Limestone is recrystallised to marble.")], T_MET, "Concept", "A metamorphic change."),
    Q("Contact metamorphism occurs", "Around an igneous intrusion",
      [("Across a whole mountain belt", "That is regional metamorphism."), ("Along a fault plane only", "That is dynamic metamorphism."), ("On the sea floor surface", "It needs a heat source in contact.")],
      [("Cause", "Heat from a nearby intrusion bakes the surrounding rock.")], T_MET, "Concept", "Think of contact with hot magma."),
    # Module 4: Geomorphology (8)
    Q("The reaction of carbon dioxide and water, forming weak carbonic acid that breaks down minerals, is", "Carbonation",
      [("Hydration", "Hydration is the addition of water to a mineral."), ("Oxidation", "Oxidation involves oxygen."), ("Exfoliation", "Exfoliation is peeling of rock sheets.")],
      [("Definition", "Carbonation uses carbonic acid.")], T_WEA, "Recall", "Carbon dioxide plus water."),
    Q("Which of these is a form of physical weathering?", "Thermal expansion and contraction of rock",
      [("Oxidation of iron minerals", "That is chemical weathering."), ("Carbonation of limestone", "That is chemical weathering."), ("Hydrolysis of feldspar", "That is chemical weathering.")],
      [("Classification", "Heating and cooling split rock without changing its minerals.")], T_WEA, "Concept", "No new minerals are produced."),
    Q("The top layer of soil, rich in humus and roots, is the", "A horizon",
      [("B horizon", "The B horizon is subsoil."), ("C horizon", "The C horizon is weathered rock."), ("R horizon", "R is bedrock.")],
      [("Order", "O, A, B, C, R from the top.")], T_SOI, "Recall", "Topsoil."),
    Q("Very slow downslope movement of soil is called", "Creep",
      [("Mudflow", "Mudflow is fast."), ("Rockfall", "Rockfall is sudden."), ("Slump", "Slump is a block movement.")],
      [("Speed", "Creep is the slowest type.")], T_MAS, "Recall", "Leaning posts are a sign."),
    Q("Sand grains that bounce along a river bed are moved by", "Saltation",
      [("Traction", "Traction rolls large stones."), ("Solution", "Solution carries dissolved material."), ("Suspension", "Suspension carries fine particles in the water.")],
      [("Definition", "Saltation is bouncing of sand grains.")], T_RIV, "Recall", "It begins with the same letter as sand."),
    Q("On the inside of a river bend, the river mainly", "Deposits sand and gravel",
      [("Erodes a steep cliff", "That happens on the outside of the bend."), ("Forms a waterfall", "Waterfalls need a hard rock step."), ("Dissolves rock", "That is solution and does not describe the inner bend.")],
      [("Slow water", "On the inside the water is slow and drops its load.")], T_RIV, "Concept", "Is the current slower or faster?"),
    Q("A ridge of sand or shingle attached to land at one end and built by longshore drift is a", "Spit",
      [("Stack", "A stack is a rock column."), ("Cirque", "A cirque is a glacial hollow."), ("Loess", "Loess is wind-blown silt.")],
      [("Deposition", "Longshore drift builds a spit.")], T_WIS, "Recall", "A depositional coastal feature."),
    Q("A knife-edge ridge between two glacial hollows is an", "Arête",
      [("Oxbow", "An oxbow is a river feature."), ("Dune", "A dune is made by wind."), ("Delta", "A delta is made by a river.")],
      [("Landform", "Cirques cut back-to-back leave an arête.")], T_WIS, "Recall", "It is a ridge."),
    # Module 5: Structure, stratigraphy, palaeontology (12)
    Q("Stress is", "Force per unit area acting on a rock",
      [("The change in shape of a rock", "That is strain."), ("A break in a rock", "That is a fracture or fault."), ("The temperature of a rock", "Temperature is not stress.")],
      [("Definition", "Stress = force / area.")], T_SSD, "Recall", "Strain is the result."),
    Q("A bed strikes north-south and dips at 30 degrees. The dip direction is", "East or west",
      [("North or south", "That is along the strike."), ("North-east only", "The dip direction is at right angles to the strike."), ("Vertical", "Dip direction is horizontal.")],
      [("Right angles", "At 90 degrees to the strike.")], T_SSD, "Concept", "Draw a line at right angles to the strike."),
    Q("In an anticline with beds in their original order, the rocks in the core are the", "Oldest",
      [("Youngest", "That applies to a syncline."), ("Igneous", "Age, not rock type, is the point."), ("The same age as the limbs", "The limbs are younger.")],
      [("Rule", "Anticline: oldest in the core.")], T_FOL, "Recall", "An arch."),
    Q("A fold whose axial plane is nearly horizontal is", "Recumbent",
      [("Symmetrical", "A symmetrical fold has a vertical axial plane."), ("Plunging", "Plunging describes a tilted axis."), ("A monocline", "A monocline is a single bend.")],
      [("Meaning", "Recumbent means lying down.")], T_FOL, "Recall", "Lying down."),
    Q("A normal fault is caused mainly by", "Tension",
      [("Compression", "Compression forms reverse faults."), ("Shear only", "Shear forms strike-slip faults."), ("Weathering", "Weathering is not a stress.")],
      [("Cause", "Tension stretches the crust and the hanging wall moves down.")], T_FJU, "Concept", "Hanging wall down."),
    Q("Younger horizontal beds lying on older tilted beds form a", "Angular unconformity",
      [("Parallel unconformity", "In a parallel unconformity both sets are horizontal."), ("Heterolithic unconformity", "That needs igneous or metamorphic rock below."), ("Graben", "A graben is a dropped fault block.")],
      [("Definition", "Flat on tilted: angular.")], T_FJU, "Recall", "Look at the angle."),
    Q("A feature that cuts across a rock is", "Younger than the rock it cuts",
      [("Older than the rock it cuts", "It could not cut something that did not exist."), ("The same age", "Cutting happens after the rock exists."), ("Impossible to compare", "The cross-cutting principle gives the order.")],
      [("Principle", "Cross-cutting relationships.")], T_STR, "Concept", "The cutter must come later."),
    Q("The principle of faunal succession is used mainly to", "Correlate rocks of the same age using fossils",
      [("Measure the dip of beds", "Fossils do not measure dip."), ("Find the porosity of rocks", "Fossils do not measure porosity."), ("Date igneous rocks in years", "That needs radiometric dating.")],
      [("Use", "Fossils follow a known order, so they match rocks of the same age.")], T_STR, "Concept", "Fossils change with time."),
    Q("The correct order of eras from oldest to youngest is", "Palaeozoic, Mesozoic, Cenozoic",
      [("Cenozoic, Mesozoic, Palaeozoic", "That is youngest to oldest."), ("Mesozoic, Palaeozoic, Cenozoic", "The Palaeozoic is the oldest."), ("Palaeozoic, Cenozoic, Mesozoic", "The Mesozoic comes before the Cenozoic.")],
      [("Order", "Palaeo, Meso, Ceno.")], T_TIM, "Recall", "Old, middle, recent."),
    N("A rock contains one eighth of its original parent isotope. The half-life is 40 million years. How old is the rock in millions of years?", 120,
      [("Half-lives", "1/8 = (1/2)^3, so 3 half-lives."), ("Age", "3 x 40 = 120 million years.")], T_TIM, "Calculation", "How many halvings give one eighth?", unit="million years"),
    Q("Which fossil group has left and right valves of equal size and an umbo on each valve?", "Bivalves",
      [("Brachiopods", "Brachiopod valves are unequal."), ("Trilobites", "Trilobites have a segmented body."), ("Graptolites", "Graptolites are thin colonies.")],
      [("Features", "Equal valves and umbones belong to bivalves.")], T_FOS, "Recall", "Equal valves."),
    Q("Which fossil is an index fossil of the Mesozoic era?", "Ammonite",
      [("Trilobite", "Trilobites are Palaeozoic."), ("Graptolite", "Graptolites are Early Palaeozoic."), ("Brachiopod of the Cambrian", "Not a Mesozoic index fossil.")],
      [("Range", "Ammonites flourished in the Mesozoic and are used as index fossils.")], T_FOS, "Application", "Which group ends at the Cretaceous?"),
    # Module 6: Hydrogeology, economic and environmental (10)
    Q("Hydrogeology is the study of", "Groundwater",
      [("Rainfall", "Rainfall belongs to meteorology."), ("All water on Earth", "That is too broad."), ("Rivers", "That is surface hydrology.")],
      [("Definition", "Hydrogeology is the study of groundwater.")], T_HYD, "Recall", "Think underground."),
    N("A rock sample of volume 200 cm3 has pore spaces of 50 cm3. What is its porosity?", 25,
      [("Formula", "Porosity = pore volume / total volume x 100."), ("Substitute", "50 / 200 x 100 = 25 per cent.")], T_HYD, "Calculation", "Divide pore volume by total volume.", unit="%"),
    Q("An aquifer must be", "Both porous and permeable",
      [("Porous but impermeable", "It would not yield water."), ("Impermeable but non-porous", "It would hold no water."), ("Only permeable and dry", "It must store water.")],
      [("Definition", "It stores and yields water.")], T_AQU, "Recall", "Storage and flow."),
    Q("An artesian well flows without pumping because the water", "Is under pressure in a confined aquifer",
      [("Is very deep", "Depth alone does not cause flow."), ("Is hot", "Heat is not the cause."), ("Comes from a river", "It comes from the aquifer.")],
      [("Pressure", "A confined aquifer fed from higher ground is under pressure.")], T_AQU, "Concept", "Think about the recharge area."),
    Q("In a petroleum trap, the layer that prevents the oil from escaping upwards is the", "Cap rock",
      [("Source rock", "The source rock is where oil forms."), ("Reservoir rock", "The reservoir holds the oil."), ("Gangue", "Gangue is waste mineral in an ore.")],
      [("Function", "An impermeable seal on top.")], T_PET, "Recall", "A seal."),
    Q("Which is the highest rank of coal?", "Anthracite",
      [("Peat", "Peat is the first stage."), ("Lignite", "Lignite is low rank."), ("Bituminous coal", "Bituminous coal is below anthracite.")],
      [("Order", "Peat, lignite, bituminous coal, anthracite.")], T_PET, "Recall", "Hardest and highest in carbon."),
    Q("The unwanted mineral found together with the ore mineral is", "Gangue",
      [("Tenor", "Tenor is metal content."), ("Cap rock", "That is related to petroleum traps."), ("Placer", "A placer is a type of deposit.")],
      [("Definition", "Gangue is the worthless mineral in an ore.")], T_ORE, "Recall", "It is waste."),
    Q("Bauxite, the ore of aluminium, forms by", "Intense weathering and leaching in a hot, wet climate",
      [("Cooling of granite", "Granite does not make bauxite."), ("Glacial deposition", "Glaciers do not make bauxite."), ("Wind erosion", "Wind does not make bauxite.")],
      [("Residual deposit", "Leaching leaves aluminium-rich residue.")], T_ORE, "Concept", "Tropical weathering."),
    Q("The 1986 gas disaster at Lake Nyos was caused by the release of", "Carbon dioxide",
      [("Lava", "No lava was erupted."), ("Methane gas explosion", "Carbon dioxide was the gas released."), ("Steam only", "The killer gas was carbon dioxide.")],
      [("Cause", "Dissolved carbon dioxide came out of the lake water.")], T_GEO, "Recall", "A heavy, invisible gas."),
    Q("The point on the surface directly above the focus of an earthquake is the", "Epicentre",
      [("Hypocentre", "That is another word for the focus."), ("Fault scarp", "That is a ground step."), ("Magnitude point", "No such term.")],
      [("Definition", "Focus underground, epicentre above.")], T_GEO, "Recall", "On the surface."),
]
# Module 4 extra items to reach 50 are already included above; replace nothing.

# ------------------------------------------------------------------ 20. Paper 2 practice paper A (28 parts)
MAP = "f5gly2-map.svg"
MAP_A = ("Geological map of a flat area: vertical bands A to E from west to east, a dashed line X to Y across them, a north arrow, a strike and dip symbol on bed C (north-south line, tick pointing east, 30) and a scale bar 0 to 10 km")
STRQ = "f5gly2-strata.svg"
STRQ_A = STR_A
use(30)
P2 = [
    # Part A: the map (Q1-Q10). Beds A-E, flat country, beds in their original order.
    Q("Map section. Bed boundaries on the map run north-south. What is the strike of the beds?", "North-south",
      [("East-west", "The boundaries run north-south, and strike is the direction of the boundary lines on flat ground."), ("North-east", "The boundaries are not diagonal."), ("There is no strike", "Strike exists for any inclined bed.")],
      [("Definition", "On flat ground, the strike runs along the bed boundaries: north-south.")], T_SSD, "Interpretation", "Strike runs along the boundary lines.", diagram=MAP, alt=MAP_A),
    Q("The short tick on the dip symbol points east. In which direction do the beds dip?", "East",
      [("West", "The tick points the other way."), ("North", "North is along the strike."), ("South", "South is along the strike.")],
      [("Symbol", "The tick shows the direction of dip.")], T_SSD, "Interpretation", "Look where the tick points.", diagram=MAP, alt=MAP_A),
    N("Read the dip angle from the symbol, in degrees.", 30,
      [("Number", "The number by the tick is 30, so the dip is 30 degrees.")], T_SSD, "Interpretation", "Look for the number beside the symbol.", unit="degrees", diagram=MAP, alt=MAP_A),
    Q("Assume the country is flat and the beds are the right way up. The beds dip east. Which bed is the oldest?", "A",
      [("B", "B is overlain by C and is younger than A."), ("D", "D is younger than A, B and C."), ("E", "E is the youngest.")],
      [("Dip", "Walking east you go on to younger beds when beds dip east on flat ground."), ("Answer", "A is the oldest.")], T_STR, "Reasoning", "Which way do you go to cross older beds?", diagram=MAP, alt=MAP_A),
    Q("Which bed is the youngest?", "E",
      [("A", "A is the oldest."), ("C", "C is in the middle."), ("D", "E lies east of D, so is younger.")],
      [("Order", "Oldest to youngest from west to east: A, B, C, D, E.")], T_STR, "Reasoning", "Go to the other end from the oldest.", diagram=MAP, alt=MAP_A),
    N("On the printed paper, the 10 km bar of the scale is 4 cm long. Convert the scale to a numerical scale 1 : n. Give n.", 250000,
      [("Convert", "10 km = 1 000 000 cm."), ("Divide", "1 000 000 / 4 = 250 000. The scale is 1 : 250 000.")], T_SSD, "Calculation", "Convert 10 km to centimetres first.", unit="", diagram=MAP, alt=MAP_A),
    N("The line X to Y measures 8 cm on the printed map where 4 cm represents 10 km. How long is XY on the ground, in km?", 20,
      [("Scale", "4 cm is 10 km, so 1 cm is 2.5 km."), ("Distance", "8 x 2.5 = 20 km.")], T_SSD, "Calculation", "Find the kilometres for 1 cm.", unit="km", diagram=MAP, alt=MAP_A),
    N("The outcrop of bed B is 3.0 km wide on the flat ground. The dip is 30 degrees. What is the true thickness of bed B in km?", 1.5,
      [("Formula", "True thickness = width x sin(dip)."), ("Substitute", "3.0 x sin 30 degrees = 3.0 x 0.5 = 1.5 km.")], T_SSD, "Calculation", "Use sin of the dip.", tol=0.05, unit="km", diagram=MAP, alt=MAP_A),
    Q("Which bed has the widest outcrop on the map?", "D",
      [("A", "A is 5 km wide."), ("B", "B is 3 km wide."), ("E", "E is the narrowest at 2 km.")],
      [("Compare", "From the scale bar, D is about 6 km wide, wider than A (5), B (3), C (4) and E (2).")], T_SSD, "Interpretation", "Compare the band widths using the scale bar.", diagram=MAP, alt=MAP_A),
    Q("On a different map, all the bed boundaries run parallel to the contour lines. The beds there are", "Horizontal",
      [("Vertical", "Vertical beds give straight lines that cross the contours."), ("Dipping steeply", "Dipping beds cross the contours."), ("Folded into an anticline", "A fold gives outcrops that cross the contours.")],
      [("Reason", "Beds at the same height everywhere have boundaries that follow contour lines.")], T_SSD, "Concept", "A contour joins points of equal height."),
    # Part B: figures
    Q("Folds. In the folds figure, which letter marks the syncline?", "Q",
      [("P", "P marks the anticline."), ("R", "R marks a limb."), ("None", "Q marks the downfold.")],
      [("Shape", "A downfold is a syncline.")], T_FOL, "Interpretation", "Which part sags downward?", diagram=FOLQ, alt=FOLQ_A),
    Q("In the same figure, what is the part marked R?", "A limb",
      [("The hinge", "The hinge is at the crest or trough."), ("The axial plane", "That is the dashed line."), ("A fault", "No fault is shown.")],
      [("Parts", "R is the side of a fold, a limb.")], T_FOL, "Interpretation", "R is on the side.", diagram=FOLQ, alt=FOLQ_A),
    Q("Faults. In the horst and graben figure, block P is a", "Horst",
      [("Graben", "A graben is the lower block."), ("Syncline", "A syncline is a fold."), ("Dyke", "A dyke is an igneous intrusion.")],
      [("Shape", "P is raised between two faults.")], T_FJU, "Interpretation", "P is higher than its neighbours.", diagram=HOQ, alt=HOQ_A),
    Q("In the same figure, block Q is a", "Graben",
      [("Horst", "A horst is the raised block."), ("Anticline", "An anticline is a fold."), ("Joint", "A joint has no displacement.")],
      [("Shape", "Q has dropped between two faults.")], T_FJU, "Interpretation", "Q is lower than its neighbours.", diagram=HOQ, alt=HOQ_A),
    Q("Unconformities. Figure X shows flat beds on tilted beds. This is a", "Angular unconformity",
      [("Parallel unconformity", "Both sets of beds would be horizontal."), ("Heterolithic unconformity", "Igneous or metamorphic rock would lie below."), ("Normal fault", "No fault is shown.")],
      [("Match", "Flat on tilted: angular.")], T_FJU, "Interpretation", "Compare the angle of the beds above and below.", diagram=UNQ, alt=UNQ_A),
    Q("In the same figure, which figure shows sedimentary beds on igneous or metamorphic rock?", "Figure Z",
      [("Figure X", "X shows tilted beds, not igneous rock."), ("Figure Y", "Y shows horizontal beds on horizontal beds."), ("All three", "Only one shows this.")],
      [("Match", "The crosses mark crystalline rock under the erosion surface: heterolithic.")], T_FJU, "Interpretation", "Look for the rock with crosses.", diagram=UNQ, alt=UNQ_A),
    Q("Relative age. In the strata figure, which is the youngest rock?", "E",
      [("A", "A is the oldest layer."), ("D", "E lies above D."), ("F", "F is cut off by the erosion surface below E.")],
      [("Order", "A, B, C, D, F, E from oldest to youngest.")], T_STR, "Reasoning", "E lies on top of all the others.", diagram=STRQ, alt=STRQ_A),
    Q("In the same figure, the igneous body F is", "Younger than D and older than E",
      [("Older than A", "F cuts A, so it is younger than A."), ("The same age as D", "F cuts D, so it is younger."), ("Younger than E", "E lies above F and is not cut by it.")],
      [("Cross-cutting", "F cuts A to D but not E.")], T_STR, "Reasoning", "F stops at the erosion surface.", diagram=STRQ, alt=STRQ_A),
    Q("Soils. In the soil figure, the layer marked R (third from the top) is the", "Subsoil (B horizon)",
      [("Topsoil (A horizon)", "The topsoil is the second layer, Q."), ("Bedrock", "Bedrock is the bottom layer, T."), ("Leaf litter (O horizon)", "That is the top layer, P.")],
      [("Order", "P is O, Q is A, R is B, S is C, T is bedrock.")], T_SOI, "Interpretation", "Count down: O, A, B.", diagram=SOILQ, alt=SOILQ_A),
    Q("Rivers. In the river figure, the landform marked B on the inside of the bend is the", "Slip-off slope",
      [("River cliff", "The river cliff is on the outer bank, A."), ("Oxbow lake", "That is C."), ("Waterfall", "No waterfall is shown.")],
      [("Process", "Slow water deposits sand on the inner bank.")], T_RIV, "Interpretation", "Which bank is the inner one?", diagram=RIVQ, alt=RIVQ_A),
    Q("Petroleum. In the trap figure, the layer marked B that holds the oil is the", "Reservoir rock",
      [("Cap rock", "The cap rock is A at the top."), ("Source rock", "The source rock is C at the base."), ("Soil horizon", "This is a deep rock structure.")],
      [("Function", "A porous, permeable rock stores the oil.")], T_PET, "Interpretation", "It is the layer that stores the fluids.", diagram=TRQ, alt=TRQ_A),
    Q("Groundwater. In the artesian figure, the layer marked C is the", "Aquifer",
      [("Confining layer", "That is B."), ("Pressure surface", "That is the dashed line D."), ("Water table", "A confined aquifer has no free water table.")],
      [("Position", "The porous, water-filled layer between the clays.")], T_AQU, "Interpretation", "It is the water-filled layer.", diagram=ARQ, alt=ARQ_A),
    # Part C: calculations and definitions
    N("A charcoal sample contains one eighth of its original carbon-14. The half-life is 5 730 years. How old is it in years?", 17190,
      [("Half-lives", "1/8 = (1/2)^3, so 3 half-lives."), ("Age", "3 x 5 730 = 17 190 years.")], T_TIM, "Calculation", "How many halvings give one eighth?", unit="years"),
    N("A 500 cm3 rock sample has pore spaces totalling 150 cm3. What is its porosity?", 30,
      [("Formula", "150 / 500 x 100 = 30 per cent.")], T_HYD, "Calculation", "Divide pore volume by total volume.", unit="%"),
    N("A stream is 6 m wide and 1.5 m deep and flows at 0.8 m per second. What is the discharge?", 7.2,
      [("Formula", "Discharge = width x depth x velocity."), ("Calculate", "6 x 1.5 x 0.8 = 7.2.")], T_RIV, "Calculation", "Multiply the three values.", tol=0.05, unit="cubic metres per second"),
    Q("Which statement correctly defines streak and fracture?", "Streak is the colour of the powder of a mineral; fracture is the nature of its freshly broken surface",
      [("Streak is the powder of a mineral; fracture is its ability to break", "These are the errors the examiners reported."), ("Streak is the appearance in reflected light; fracture is its hardness", "Streak is not lustre, and fracture is not hardness."), ("Streak is the colour of the mineral; fracture is the colour of its powder", "The two are swapped and confused.")],
      [("Definitions", "Streak: colour of powder. Fracture: nature of a freshly broken surface.")], T_PHY, "Recall", "One is a colour, the other is a surface."),
    Q("Which list gives characteristics of a bivalve?", "Equal left and right valves, an umbo, muscle scars joined by a pallial line, teeth on the hinge",
      [("Unequal valves and a stalk opening", "That describes a brachiopod."), ("A coiled chambered shell with sutures", "That describes an ammonite."), ("A segmented body with a head and tail shield", "That describes a trilobite.")],
      [("Features", "Bivalves have equal valves, umbones, muscle scars with a pallial line and dentition.")], T_FOS, "Recall", "Think of a mussel shell."),
    Q("Which statement correctly defines hydration, carbonation and oxidation?", "Addition of water to minerals; reaction with carbonic acid; reaction with oxygen",
      [("Reaction with oxygen; addition of water; reaction with carbonic acid", "The first two definitions are swapped around."), ("Reaction with carbonic acid; reaction with oxygen; addition of water", "The definitions are in the wrong order for the three terms."), ("Loss of water; reaction with nitrogen; heating", "None of these is a correct definition.")],
      [("Definitions", "Hydration adds water. Carbonation uses carbonic acid. Oxidation uses oxygen.")], T_WEA, "Recall", "Hydro means water."),
]

SETS.append(practice_set(
    module=M7, topic="Paper 1", title="Paper 1 mock exam A",
    lesson="gly2-exam-paper-1-multiple-choice-strategies", mock=True, time_limit_minutes=90, questions=P1))
SETS.append(practice_set(
    module=M7, topic="Paper 2", title="Paper 2 practice paper A",
    lesson="gly2-exam-paper-2-structured-questions-maps", mock=True, time_limit_minutes=150, questions=P2))
