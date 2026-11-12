"""Upper Sixth Geology (A Level 0755): practice sets for Sedimentology & Sedimentary Petrology and Structural
Geology & Geological Map Work (one 8-question set per lesson).

Draft content. Numerical answers were verified by script; map extracts and data are invented for practice.
Correct options are placed by a seeded bag so that A-D are used evenly.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("geology", "upper-sixth")

M1 = "Sedimentology & Sedimentary Petrology"
M2 = "Structural Geology & Geological Map Work"


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


SETS = []

# ------------------------------------------------------------------ 1. Hjulstrom
HJQ = "algyu1-hjulstrom-q.svg"
HJQ_A = ("Log-log graph of mean velocity (0.1 to 1000 cm/s) against grain diameter (0.001 to 1000 mm). Solid curve P "
         "has a minimum near 0.3 mm; dashed curve Q lies below it. Point X: 0.01 mm at 30 cm/s. Point Y: 0.3 mm at "
         "60 cm/s. Point Z: 10 mm at 20 cm/s. Field names are not shown.")
use(101)
SETS.append(practice_set(
    module=M1, topic="Sediment transport and the Hjulström diagram",
    title="Flow, settling and the Hjulström diagram", lesson="gyu1-sediment-transport-hjulstrom",
    questions=[
        Q("Sand grains that are lifted from the bed, carried a short distance and dropped again are moving by", "Saltation",
          [("Traction", "Traction is rolling and sliding in constant contact with the bed, typical of pebbles."),
           ("Suspension", "Suspended grains are held up by eddies for long distances; they do not hop."),
           ("Attrition", "Attrition is an erosion process (grains knocking each other smaller), not a mode of transport.")],
          [("Recall the modes", "Traction, saltation, suspension and solution."), ("Match", "Short hops along the bed describe saltation.")],
          "Modes of sediment transport", "Recall", "Which mode describes a bouncing movement?"),
        Q("On the diagram, curve P is the", "Critical erosion velocity curve",
          [("Settling (deposition) curve", "The settling curve is the lower, dashed curve Q, which rises steadily with grain size."),
           ("Line of laminar flow", "The diagram does not show flow regime lines."),
           ("Line of equal Reynolds number", "Reynolds number is not plotted on the Hjulström diagram.")],
          [("Shape", "P has a minimum for fine sand and rises for finer and coarser grains."), ("Identify", "That U-shape is the erosion curve.")],
          "Hjulström diagram curves", "Interpretation", "Which curve rises again for very fine grains?", diagram=HJQ, alt=HJQ_A),
        Q("Point Y (0.3 mm sand, 60 cm/s) describes a grain lying on the bed. What happens to it?", "It is eroded and carried away",
          [("It stays at rest on the bed", "Y is above curve P, the erosion curve, so the grain is picked up."),
           ("It is deposited", "Deposition happens below the dashed curve Q; Y is far above it."),
           ("It is dissolved", "The diagram describes mechanical movement of grains, not solution.")],
          [("Locate", "At 0.3 mm the erosion curve is about 20 cm/s."), ("Compare", "60 cm/s is above it, so the grain is eroded.")],
          "Reading the Hjulström diagram", "Interpretation", "Is the point above or below curve P?", diagram=HJQ, alt=HJQ_A),
        Q("Point Z is a 10 mm pebble moving in a flow that has slowed to 20 cm/s. What happens to it?", "It is deposited",
          [("It is eroded from the bed", "Z is far below the erosion curve for 10 mm (about 100 cm/s)."),
           ("It stays in suspension", "A 10 mm pebble is never in suspension in a river; and Z is below the settling curve."),
           ("It keeps moving by traction indefinitely", "Below the settling curve moving grains stop.")],
          [("Locate", "For 10 mm the dashed settling curve is at about 70 cm/s."), ("Compare", "20 cm/s is below it, so the pebble is dropped.")],
          "Reading the Hjulström diagram", "Interpretation", "Compare 20 cm/s with curve Q at 10 mm.", diagram=HJQ, alt=HJQ_A),
        Q("Point X is fine silt (0.01 mm) at 30 cm/s. Which statement is correct?", "Silt already in suspension stays moving, but silt resting on a consolidated bed is not eroded",
          [("All silt in the river is eroded", "X is below the erosion curve P (about 70 cm/s for 0.01 mm), so silt at rest is not picked up."),
           ("All silt is deposited at once", "X is far above the settling curve Q, so moving silt is not dropped."),
           ("Silt behaves exactly like 0.3 mm sand at this velocity", "Sand of 0.3 mm would be eroded at 30 cm/s; fine silt would not, because of cohesion.")],
          [("Locate", "X lies between P and Q."), ("Meaning", "Between the curves: transport of grains already moving, no erosion of grains at rest.")],
          "Transport field and cohesion", "Interpretation", "X lies between the two curves.", diagram=HJQ, alt=HJQ_A),
        N("Use Stokes' law to find the settling velocity, in mm/s, of a 0.02 mm quartz grain in still water (grain density 2 650 kg/m3, water 1 000 kg/m3, viscosity 0.001 Pa s, g = 9.81 m/s2). Give 2 significant figures.", 0.36,
          [("Formula", r"$v = (\rho_s - \rho_f) g d^2 / 18\mu$."), ("Substitute", r"$v = 1650 \times 9.81 \times (2\times10^{-5})^2 / 0.018 = 3.6\times10^{-4}$ m/s."), ("Convert", "0.36 mm/s.")],
          "Stokes' law", "Calculation", "Convert 0.02 mm to metres before squaring.", tol=0.02, unit="mm/s"),
        N("By Stokes' law, how many times more slowly does a 0.002 mm clay particle settle than a 0.01 mm silt grain of the same density?", 25,
          [("Ratio", r"$v \propto d^2$, so the ratio is $(0.01/0.002)^2$."), ("Calculate", r"$5^2 = 25$.")],
          "Settling velocity depends on d squared", "Reasoning", "Velocity depends on the square of the diameter.", tol=0, unit="times"),
        Q("Which is the strongest criticism of using the Hjulström diagram for a deep, fast river carrying flaky mica and dense magnetite grains?", "It uses mean velocity for about 1 m depth and uniform quartz grains, so it ignores depth, grain shape and grain density",
          [("It uses logarithmic axes", "Log axes are a strength: they let very different sizes and velocities fit one graph."),
           ("It cannot show deposition", "The settling curve does show deposition."),
           ("It applies only to wind", "It was drawn for water; the problem is depth, shape and density, not the fluid.")],
          [("Assumptions", "Mean velocity, about 1 m depth, quartz spheres of one size."), ("Mismatch", "Mica is flaky and magnetite is dense, and depth changes bed shear stress.")],
          "Evaluating the Hjulström diagram", "Reasoning", "List the conditions the diagram was drawn for."),
    ]))

# ------------------------------------------------------------------ 2. Grain size
use(102)
SETS.append(practice_set(
    module=M1, topic="Grain size analysis",
    title="Phi units, sieve data and Folk and Ward statistics", lesson="gyu1-grain-size-analysis-phi-statistics",
    questions=[
        N("Convert a grain diameter of 0.125 mm to phi units.", 3,
          [("Formula", r"$\phi = -\log_2 d$."), ("Power of 2", r"$0.125 = 2^{-3}$, so $\phi = 3$.")],
          "Phi scale", "Calculation", "Write 0.125 as a power of 2.", tol=0.01, unit="phi"),
        Q("A grain measures 2.5 phi. Its diameter and Wentworth class are", "About 0.18 mm, fine sand",
          [("About 5.7 mm, pebble", r"That uses $d = 2^{+\phi}$; the formula is $d = 2^{-\phi}$."),
           ("2.5 mm, granule", "Phi is not the diameter in millimetres."),
           ("About 0.018 mm, silt", "The decimal place is wrong: 2 to the power -2.5 is 0.177 mm.")],
          [("Convert", r"$d = 2^{-2.5} = 0.177$ mm."), ("Class", "0.125 to 0.25 mm is fine sand.")],
          "Phi to millimetres", "Calculation", "Use d = 2 to the power minus phi."),
        N("A sample of 80 g leaves 1.6, 6.4, 20, 32 and 16 g on the 0, 1, 2, 3 and 4 phi sieves, and 4 g in the pan. What percentage of the sample is coarser than 3 phi?", 75,
          [("Add the coarser sieves", "1.6 + 6.4 + 20 + 32 = 60 g."), ("Percentage", "60/80 x 100 = 75 per cent.")],
          "Cumulative percentage from sieve data", "Calculation", "Add the weights on the 0 to 3 phi sieves.", tol=0.5, unit="%"),
        N("A sand gives phi16 = 1.2, phi50 = 1.8 and phi84 = 2.2. Calculate the Folk and Ward graphic mean in phi (2 decimal places).", 1.73,
          [("Formula", r"$M_z = (\phi_{16} + \phi_{50} + \phi_{84})/3$."), ("Substitute", "(1.2 + 1.8 + 2.2)/3 = 5.2/3 = 1.73 phi.")],
          "Graphic mean", "Calculation", "Average three of the percentiles.", tol=0.01, unit="phi"),
        Q("The same sand has phi5 = 0.5 and phi95 = 2.6. Its inclusive graphic standard deviation is 0.57. It is", "Moderately well sorted",
          [("Very well sorted", "Very well sorted is below 0.35."),
           ("Poorly sorted", "Poorly sorted is 1.00 to 2.00."),
           ("Extremely poorly sorted", "That class is above 4.00.")],
          [("Calculate", "(2.2 - 1.2)/4 + (2.6 - 0.5)/6.6 = 0.25 + 0.32 = 0.57."), ("Class", "0.50 to 0.71: moderately well sorted.")],
          "Folk and Ward sorting classes", "Application", "Compare 0.57 with the class limits 0.35, 0.50, 0.71 and 1.00."),
        Q("For the same sand the inclusive graphic skewness is -0.22. Which interpretation fits best?", "Coarse-skewed: fines were winnowed out, as often happens on beaches",
          [("Fine-skewed: fine grains were added from suspension", "A negative skewness in phi means a tail of coarse grains, not fine grains."),
           ("Perfectly symmetrical: the energy never varied", "Nearly symmetrical is between -0.1 and +0.1."),
           ("Skewness cannot be used for interpretation", "Skewness is useful, though not decisive, for interpreting winnowing.")],
          [("Sign", "Negative skewness in phi units means a tail towards coarse sizes."), ("Process", "Waves wash out fines, leaving the coarse tail.")],
          "Skewness and winnowing", "Interpretation", "Which side of the distribution has the long tail when skewness is negative?"),
        Q("Which method is most suitable for measuring the grain size distribution of a clay-rich mudstone after disaggregation?", "A pipette or hydrometer settling method based on Stokes' law",
          [("Dry sieving at whole phi intervals", "Sieves finer than about 4 phi clog; clay must be measured by settling or laser."),
           ("Measuring clasts with a ruler", "Clay particles are far too small to measure individually by hand."),
           ("Counting fossils in thin section", "Fossil counts do not give grain size.")],
          [("Size", "Clay is finer than 1/256 mm."), ("Method", "Fine particles are sized by their settling velocity, using Stokes' law.")],
          "Methods of grain size analysis", "Application", "Which law links fall velocity to diameter?"),
        Q("A geologist claims that a sorting-skewness plot proves an ancient sandstone was a beach deposit. The best evaluation is that", "The fields overlap and source and diagenesis affect sizes, so other evidence such as structures and fossils is needed",
          [("The claim is always correct because statistics are objective", "Objective numbers can still fall where environments overlap."),
           ("Grain size cannot vary between environments", "Grain size does vary with energy; the problem is overlap, not lack of variation."),
           ("Only the mean size matters, so the plot is useless", "Sorting and skewness add information; they are not useless, just not decisive.")],
          [("Strength", "The plot often separates modern sands in one region."), ("Limits", "Overlapping fields, source control and diagenetic change.")],
          "Evaluating grain size statistics", "Reasoning", "Think about what else controls the sizes in a rock."),
    ]))

# ------------------------------------------------------------------ 3. Sedimentary structures
STQ = "algyu1-structures-q.svg"
STQ_A = ("Four unlabelled panels. P: inclined laminae curving down to the east (E right, W left), tangential to the base. "
         "Q: two beds, large grains at the base, small at the top. R: profile 1 asymmetrical, 2 symmetrical. "
         "S: cracks narrowing downward.")
use(103)
SETS.append(practice_set(
    module=M1, topic="Sedimentary structures",
    title="Bedforms, way-up criteria and palaeocurrents", lesson="gyu1-sedimentary-structures-way-up",
    questions=[
        Q("Flute casts and tool marks preserved on the base of a sandstone bed are best classified as", "Erosional structures preserved as sole marks",
          [("Biogenic structures", "They are made by the current and the objects it carries, not by organisms."),
           ("Chemical structures formed during diagenesis", "They form at the sediment surface before the sand is deposited."),
           ("Depositional structures formed inside the bed", "They are cut into the mud below and cast by the sand above, so they are erosional.")],
          [("Timing", "The current scoured the mud before the sand was laid down."), ("Preservation", "The sand filled the scours, so casts hang from the bed base: sole marks.")],
          "Classification of sedimentary structures", "Recall", "When did the scour form compared with the sand?"),
        Q("In panel P, towards which direction did the current flow?", "East",
          [("West", "Foresets dip downstream; they dip towards the east, so west is upstream."),
           ("North", "The section runs west to east; nothing indicates north."),
           ("It cannot be told from cross-bedding", "Cross-bedding gives a direction because foresets dip downstream.")],
          [("Foresets", "They dip down towards E."), ("Rule", "Foresets dip downstream, so the current flowed east.")],
          "Palaeocurrent from cross-bedding", "Interpretation", "Which way do the inclined laminae slope down?", diagram=STQ, alt=STQ_A),
        Q("In panel R, which profile records a one-way current, and why?", "Profile 1, because it is asymmetrical with a steep lee side",
          [("Profile 2, because it is symmetrical", "Symmetrical ripples with sharp crests are made by to-and-fro wave motion."),
           ("Both, because all ripples need a current", "Wave ripples form under oscillating water, not a one-way current."),
           ("Neither, because ripples form only in wind", "Ripples form under water and wind.")],
          [("Shape", "Current ripples have a gentle stoss side and a steep lee side."), ("Identify", "Profile 1 is asymmetrical.")],
          "Current and wave ripples", "Interpretation", "Compare the two sides of each ripple.", diagram=STQ, alt=STQ_A),
        Q("What does panel S show about the beds?", "They are the right way up, because the cracks narrow downward",
          [("They are overturned, because the cracks narrow downward", "Desiccation cracks open at the drying surface and narrow downward in beds that are the right way up."),
           ("Nothing, because mud cracks are not way-up criteria", "They are a useful way-up criterion."),
           ("The mud was deposited in deep water", "Cracks need the mud to dry out in air, so the water was shallow or absent.")],
          [("Formation", "Mud dries and shrinks from the top, opening cracks that narrow downward."), ("Apply", "Narrowing downward means the beds are upright.")],
          "Desiccation cracks as a way-up criterion", "Interpretation", "Where does mud start to crack as it dries?", diagram=STQ, alt=STQ_A),
        Q("Panel Q shows beds that fine upward from a sharp base. The most likely origin is", "Deposition from a waning current such as a turbidity current",
          [("Gradual strengthening of the current", "A strengthening current would leave coarser grains on top (coarsening upward)."),
           ("Desiccation in a desert", "Drying produces cracks, not grading."),
           ("Burrowing animals mixing the bed", "Bioturbation destroys grading rather than making it.")],
          [("Settling", "When a flow slows, larger grains settle first (Stokes' law)."), ("Origin", "A waning flow, typically a turbidity current, makes normal grading.")],
          "Graded bedding", "Concept", "Which grains settle first when a flow slows?", diagram=STQ, alt=STQ_A),
        Q("As a current over fine sand gets steadily stronger, the bed forms appear in the order", "Ripples, dunes, plane bed, antidunes",
          [("Antidunes, dunes, ripples, plane bed", "Antidunes are the highest-energy bedform, so they come last."),
           ("Plane bed, ripples, antidunes, dunes", "Dunes belong to the lower flow regime and come before the upper plane bed."),
           ("Dunes, ripples, antidunes, plane bed", "Ripples form at lower velocity than dunes.")],
          [("Lower flow regime", "Ripples, then dunes."), ("Upper flow regime", "Plane bed, then antidunes.")],
          "Bedforms and flow regime", "Recall", "Start with the smallest bedform at the lowest velocity."),
        N("Calculate the vector mean palaeocurrent direction, in degrees, of the foreset dip directions 350, 010, 030 and 020 degrees.", 12.6,
          [("Sine sum", "-0.174 + 0.174 + 0.500 + 0.342 = 0.842."), ("Cosine sum", "0.985 + 0.985 + 0.866 + 0.940 = 3.775."),
           ("Angle", r"$\tan^{-1}(0.842/3.775) = 12.6^\circ$, in the north-east quadrant.")],
          "Vector mean of palaeocurrents", "Calculation", "Add the sines and the cosines separately.", tol=1, unit="degrees"),
        Q("On one limb of a fold the cross-bed foresets meet the upper bedding surface tangentially and are truncated at the lower surface. The limb is", "Overturned (inverted)",
          [("The right way up", "In an upright bed the tangential part of a foreset is at the base."),
           ("Horizontal", "Way-up criteria do not give the dip angle."),
           ("Faulted", "Inversion of cross-beds shows overturning, not faulting.")],
          [("Normal geometry", "Foresets are truncated at the top and tangential at the base."), ("Here", "The geometry is upside down, so the limb is overturned.")],
          "Way-up in folded beds", "Reasoning", "Where is the tangential end of a foreset in an upright bed?"),
    ]))

# ------------------------------------------------------------------ 4. Diagenesis
use(104)
SETS.append(practice_set(
    module=M1, topic="Diagenesis",
    title="Compaction, cementation and porosity at depth", lesson="gyu1-diagenesis-compaction-cementation",
    questions=[
        Q("Diagenesis is best defined as", "All changes to a sediment after deposition at low temperature and pressure, before metamorphism",
          [("The breakdown of rock at the Earth's surface", "That is weathering, which happens before transport and deposition."),
           ("Recrystallization of rock under high temperature and pressure to form new textures", "That describes metamorphism."),
           ("The transport of grains by water, wind and ice", "Transport comes before deposition; diagenesis follows it.")],
          [("Timing", "After deposition."), ("Conditions", "Low temperature and pressure of shallow burial, below the metamorphic range.")],
          "Definition of diagenesis", "Recall", "When does diagenesis start?"),
        Q("Sutured and concavo-convex grain contacts in a sandstone are evidence of", "Pressure solution (chemical compaction)",
          [("Dissolution creating secondary porosity", "Secondary porosity shows as open, oversized pores, not interlocking contacts."),
           ("Early calcite cementation", "Early cement holds grains apart, preventing such contacts."),
           ("Desiccation", "Desiccation is drying of mud at the surface.")],
          [("Observation", "Grains interpenetrate along their contacts."), ("Process", "High stress at contacts dissolves the mineral: pressure solution.")],
          "Pressure solution", "Concept", "What happens to a mineral where stress is concentrated?"),
        N("A 10 m layer of mud with porosity 0.60 compacts to porosity 0.20. Calculate its new thickness in metres.", 5.0,
          [("Solid thickness", "10 x (1 - 0.60) = 4.0 m."), ("New thickness", "4.0 / (1 - 0.20) = 5.0 m.")],
          "Compaction and solid volume", "Calculation", "The solid volume does not change.", tol=0.05, unit="m"),
        N("A 20 m sand layer with porosity 0.40 is compacted and cemented to porosity 0.25. What is its new thickness in metres?", 16,
          [("Solid thickness", "20 x 0.60 = 12 m."), ("New thickness", "12 / 0.75 = 16 m.")],
          "Compaction and solid volume", "Calculation", "Find the thickness of solid grains first.", tol=0.1, unit="m"),
        N("A shale has surface porosity 0.60 and c = 0.0005 per metre in the relation porosity = 0.60 e^(-cz). What is its porosity (as a fraction) at 2 000 m? Give 2 decimal places.", 0.22,
          [("Exponent", "cz = 0.0005 x 2000 = 1."), ("Porosity", r"$0.60\,e^{-1} = 0.221$.")],
          "Exponential porosity-depth relation", "Calculation", "Work out c times z first.", tol=0.01, unit=""),
        Q("A sandstone reservoir has large irregular pores lined by remnants of partly dissolved feldspar. This porosity is", "Secondary porosity created by dissolution",
          [("Primary porosity between original grains", "Primary pores are regular spaces between grains, not moulds of dissolved grains."),
           ("Fracture porosity from faulting", "Fractures are planar cracks, not grain-shaped pores."),
           ("Porosity created by quartz cementation", "Cementation fills pores; it never creates them.")],
          [("Clue", "Remnants of dissolved feldspar line the pores."), ("Name", "Pores made by later dissolution are secondary porosity.")],
          "Secondary porosity", "Interpretation", "What has been removed to make the pore?"),
        Q("A red sandstone owes its colour mainly to", "A haematite (iron oxide) cement or grain coating",
          [("Abundant red feldspar grains only", "Pink feldspar can tint an arkose, but red sandstones are coloured by iron oxide coatings and cement."),
           ("Organic matter", "Organic matter makes rocks grey or black."),
           ("Glauconite", "Glauconite is green.")],
          [("Recall", "Red sandstones have iron oxide (haematite) cement and grain coatings."), ("Setting", "Iron oxidizes in well-aerated settings such as deserts and piedmonts.")],
          "Cements", "Recall", "Which mineral gives a red streak?"),
        Q("Why do many limestones lose porosity faster than quartz sandstones during burial?", "Calcite dissolves and reprecipitates more readily, so pressure solution and cementation work at shallower depths",
          [("Calcite is harder than quartz", "Calcite (hardness 3) is softer than quartz (7)."),
           ("Limestones are never compacted", "Limestones do compact, and form stylolites."),
           ("Quartz is more soluble than calcite in pore water", "Calcite is the more reactive mineral in most pore waters.")],
          [("Reactivity", "Calcite is far more soluble and reactive than quartz."), ("Result", "Early cementation and pressure solution reduce porosity quickly.")],
          "Diagenesis of carbonates and sandstones", "Reasoning", "Compare how readily calcite and quartz dissolve."),
    ]))

# ------------------------------------------------------------------ 5. Siliciclastic rocks
use(105)
SETS.append(practice_set(
    module=M1, topic="Siliciclastic rocks",
    title="Naming and describing siliciclastic rocks", lesson="gyu1-siliciclastic-rocks-classification",
    questions=[
        Q("A rock is made of angular fragments 5 to 40 mm across of several rock types in a fine matrix. It is a", "Breccia",
          [("Oligomict conglomerate", "Conglomerates have rounded clasts, and oligomict means one clast type."),
           ("Arkose", "Arkose is a sandstone, with grains under 2 mm."),
           ("Greywacke", "Greywacke is a matrix-rich sandstone, not a rudite.")],
          [("Size", "Clasts over 2 mm: a rudite."), ("Shape", "Angular clasts: breccia.")],
          "Classification of rudites", "Recall", "Rounded or angular clasts?"),
        N("A point count of 200 points gives quartz 120, feldspar 54, rock fragments 18 and matrix 8. What is the quartz percentage of the framework (QFL recalculated to 100)? Give 1 decimal place.", 62.5,
          [("Framework", "120 + 54 + 18 = 192."), ("Quartz", "120/192 x 100 = 62.5 per cent.")],
          "QFL recalculation", "Calculation", "Leave out the matrix before calculating percentages.", tol=0.1, unit="%"),
        Q("Using the same count (Q 62.5, F 28.1, L 9.4 per cent, matrix 4 per cent), the rock is", "Arkose",
          [("Greywacke", "Matrix is only 4 per cent, under the 15 per cent needed for a wacke."),
           ("Quartz arenite", "Quartz arenite needs at least 95 per cent quartz."),
           ("Lithic arenite", "Feldspar (28.1) exceeds rock fragments (9.4).")],
          [("Matrix", "4 per cent: an arenite."), ("QFL", "Q under 75 per cent and F greater than L: arkose.")],
          "Naming a sandstone", "Application", "Check the matrix first, then compare F with L."),
        Q("A count gives quartz 100, feldspar 20, rock fragments 40 and matrix 40 (200 points). The rock is a", "Lithic wacke (lithic greywacke)",
          [("Lithic arenite", "Matrix is 20 per cent, over the 15 per cent limit for arenites."),
           ("Arkose", "Feldspar (12.5 per cent of framework) is less than rock fragments (25 per cent) and matrix exceeds 15 per cent."),
           ("Sublitharenite", "Quartz is only 62.5 per cent of the framework and the rock is matrix-rich.")],
          [("Matrix", "40/200 = 20 per cent: a wacke."), ("Framework", "Q 62.5, F 12.5, L 25: L exceeds F, so lithic.")],
          "Arenites and wackes", "Application", "Is the matrix above or below 15 per cent?"),
        Q("Which description best fits an orthoquartzite of a transgressive shoreline?", "Over 95 per cent quartz, medium grained, well rounded, well sorted, supermature, cross-bedded",
          [("Quartz, feldspar and rock fragments in clay matrix, angular, poorly sorted, graded", "That is a greywacke from turbidity currents."),
           ("Angular clasts of many rocks, poorly sorted, massive", "That is a breccia or polymict deposit near its source."),
           ("Clay minerals, organic matter and pyrite, laminated", "That is a black shale.")],
          [("Setting", "Waves rework sand for a long time as the sea advances."), ("Result", "Only quartz survives; grains are well rounded and well sorted.")],
          "Quartz arenite", "Recall", "What survives long reworking by waves?"),
        Q("Why does an arkose usually indicate rapid erosion of granite in an arid or cold climate?", "Feldspar survives only if chemical weathering is weak and burial is quick",
          [("Feldspar forms during transport", "Feldspar comes from the source rock; it does not grow during transport."),
           ("Arid climates create feldspar from quartz", "Quartz does not turn into feldspar at the surface."),
           ("Feldspar is more resistant than quartz", "Feldspar is less stable and turns to clay by hydrolysis.")],
          [("Stability", "Feldspar is destroyed by hydrolysis in warm, wet conditions."), ("Inference", "Plenty of feldspar means little chemical weathering and short transport.")],
          "Provenance and climate", "Reasoning", "What normally happens to feldspar in a hot, wet climate?"),
        N("A sandstone contains quartz 180, feldspar 15 and rock fragments 5 grains. Calculate the maturity index Q/(F + L).", 9,
          [("F + L", "15 + 5 = 20."), ("Index", "180/20 = 9.")],
          "Mineralogical maturity", "Calculation", "Add feldspar and rock fragments first.", tol=0.05, unit=""),
        Q("A candidate describes a piedmont rock as 'muscovite, porphyritic, coarse grain'. The best correction is", "Name a rock such as arkose and describe it as coarse grained, subangular, moderately sorted and submature",
          [("Keep muscovite but add 'phaneritic'", "Muscovite is a mineral, and phaneritic is an igneous term."),
           ("Replace it with granite", "Granite is igneous; the question asks for a sedimentary rock of the piedmont."),
           ("Add 'vesicular' to describe the pores", "Vesicular is a volcanic texture.")],
          [("Rock, not mineral", "Name a rock: arkose, breccia or polymict conglomerate."), ("Sedimentary texture", "Use grain size with 'grained', shape, sorting and maturity.")],
          "Describing sedimentary rocks", "Reasoning", "Is muscovite a rock?"),
    ]))

# ------------------------------------------------------------------ 6. Carbonate rocks
DUQ = "algyu1-dunham-q.svg"
DUQ_A = ("Five sketched limestone thin sections lettered P to T. P: a few grains in grey mud. Q: more grains floating "
         "in grey mud. R: touching grains with grey mud between. S: touching grains with clear (white) spaces. "
         "T: curved layers built by organisms.")
use(106)
SETS.append(practice_set(
    module=M1, topic="Carbonate rocks",
    title="Folk and Dunham names and carbonate environments", lesson="gyu1-carbonate-rocks-folk-dunham",
    questions=[
        Q("Clear, coarse calcite crystals that fill the spaces between grains in a limestone are called", "Sparite",
          [("Micrite", "Micrite is microcrystalline mud, dull and fine, not clear coarse crystals."),
           ("Peloids", "Peloids are small grains of micrite, a type of allochem."),
           ("Ooids", "Ooids are concentrically layered grains.")],
          [("Definition", "Sparite is a pore-filling cement of coarse, clear calcite.")],
          "Components of limestones", "Recall", "Is it a grain, a mud or a cement?"),
        Q("In the figure, which thin section is a wackestone?", "Q",
          [("P", "P has fewer than 10 per cent grains in mud: a (lime) mudstone."),
           ("R", "R is grain-supported with mud between grains: a packstone."),
           ("S", "S is grain-supported without mud: a grainstone.")],
          [("Rule", "Wackestone: mud-supported, over 10 per cent grains."), ("Apply", "Q has grains floating in mud, more than in P.")],
          "Dunham classification", "Interpretation", "Look for grains that float in mud but are not rare.", diagram=DUQ, alt=DUQ_A),
        Q("Thin section S would be named in Dunham's scheme as a", "Grainstone",
          [("Packstone", "A packstone has mud between touching grains; S has clear cement instead."),
           ("Wackestone", "In a wackestone the grains float in mud."),
           ("Boundstone", "Boundstone is bound by organisms, like T.")],
          [("Support", "The grains touch: grain-supported."), ("Mud", "The spaces are clear (no mud): grainstone.")],
          "Dunham classification", "Interpretation", "Do the grains touch, and what fills the spaces?", diagram=DUQ, alt=DUQ_A),
        Q("A limestone of ooids cemented by sparite has the Folk name", "Oosparite",
          [("Oomicrite", "Micrite means carbonate mud, but this rock has sparite cement."),
           ("Biosparite", "Bio- refers to fossils, not ooids."),
           ("Pelsparite", "Pel- refers to peloids.")],
          [("Prefix", "Ooids: oo-."), ("Root", "Sparite cement: -sparite.")],
          "Folk classification", "Application", "Prefix for the grain, root for what lies between."),
        Q("An oosparite is best interpreted as forming in", "Warm, shallow, agitated water on a shoal or tidal bar",
          [("A quiet lagoon below wave base", "Quiet water would let mud settle, giving micrite."),
           ("The deep ocean below the carbonate compensation depth", "Below the CCD carbonate dissolves; ooids need very shallow water."),
           ("A freshwater swamp", "Ooids of this kind form in warm, carbonate-saturated sea water.")],
          [("Ooids", "Need agitation in warm, saturated shallow water."), ("Sparite", "No mud: energetic water washed it out.")],
          "Carbonate environments", "Interpretation", "What do both ooids and the lack of mud tell you about energy?"),
        N("A 5.00 g limestone sample leaves 0.40 g of insoluble residue after excess dilute acid. What is its carbonate content in per cent?", 92,
          [("Carbonate mass", "5.00 - 0.40 = 4.60 g."), ("Percentage", "4.60/5.00 x 100 = 92 per cent.")],
          "Carbonate content by acid digestion", "Calculation", "Subtract the residue from the sample mass.", tol=0.5, unit="%"),
        N("A 6.00 g limestone loses 2.20 g of carbon dioxide when dissolved in acid. Assuming all the carbonate is calcite (CaCO3 = 100, CO2 = 44), what percentage of the sample is calcite? Give 1 decimal place.", 83.3,
          [("Mass of calcite", "2.20 x 100/44 = 5.00 g."), ("Percentage", "5.00/6.00 x 100 = 83.3 per cent.")],
          "Carbonate content from CO2 loss", "Calculation", "Each 44 g of CO2 comes from 100 g of CaCO3.", tol=0.2, unit="%"),
        Q("A buff, sugary carbonate rock fizzes only when powdered and does not stain with alizarin red S. It is most likely", "Dolostone (dolomite rock)",
          [("Oolitic limestone", "Calcite limestones fizz strongly in cold dilute acid and stain red."),
           ("Chalk", "Chalk is soft calcite that fizzes strongly."),
           ("Marble", "Marble is metamorphosed limestone, mostly calcite, which fizzes and stains.")],
          [("Acid test", "Weak reaction unless powdered: dolomite."), ("Stain", "Alizarin red S stains calcite, not dolomite.")],
          "Distinguishing dolomite", "Application", "Which carbonate mineral reacts weakly with cold acid?"),
    ]))

# ------------------------------------------------------------------ 7. Evaporites and carbonaceous rocks
EVQ = "algyu1-evaporite-q.svg"
EVQ_A = ("Cross-section of a basin cut off from the open sea by a sill. Sea water flows in over the sill; evaporation "
         "arrows rise from the basin; brine gets saltier away from the sill. Four zones on the basin floor are "
         "numbered 1 (next to the sill) to 4 (farthest away), with no mineral names.")
use(107)
SETS.append(practice_set(
    module=M1, topic="Evaporites and carbonaceous rocks",
    title="Evaporite sequences and coal formation", lesson="gyu1-evaporites-coal-carbonaceous-rocks",
    questions=[
        Q("Which sequence shows the order in which minerals crystallize from evaporating sea water?", "Calcite, gypsum, halite, potash salts",
          [("Halite, gypsum, calcite, potash salts", "Halite is very soluble, so it crystallizes after gypsum and calcite."),
           ("Gypsum, calcite, potash salts, halite", "Calcite is the least soluble and comes first; potash salts come last."),
           ("Potash salts, halite, gypsum, calcite", "This is the reverse order, most soluble first.")],
          [("Rule", "The least soluble mineral saturates first."), ("Order", "Carbonate, gypsum or anhydrite, halite, potash and magnesium salts.")],
          "Evaporite precipitation order", "Recall", "Least soluble first."),
        Q("In the figure, zone 3 is most likely made of", "Halite",
          [("Calcite", "Carbonate forms first, near the sill (zone 1)."),
           ("Gypsum", "Gypsum forms in zone 2, before halite."),
           ("Sylvite", "Potash salts such as sylvite need the most concentrated brine, farthest away (zone 4).")],
          [("Salinity", "Brine concentrates with distance from the sill."), ("Zone 3", "Third mineral in the order: halite.")],
          "Barred basin zonation", "Interpretation", "Count the zones in order of precipitation.", diagram=EVQ, alt=EVQ_A),
        Q("Why do the zones in the figure change away from the sill?", "Brine becomes more concentrated as it flows in and evaporates",
          [("The water gets deeper away from the sill", "Depth alone does not decide which salt crystallizes; concentration does."),
           ("Rivers bring different salts to each zone", "The supply is sea water over the sill."),
           ("The temperature falls away from the sill", "The pattern is caused by rising salinity, not falling temperature.")],
          [("Process", "Water evaporates as it moves into the basin."), ("Result", "More soluble salts saturate farther from the inlet.")],
          "Barred basin model", "Reasoning", "What happens to the salinity of water that keeps evaporating?", diagram=EVQ, alt=EVQ_A),
        N("A column of sea water 1 000 m deep evaporates completely. With 35 kg of salt per cubic metre and a salt density of 2 200 kg per cubic metre, what thickness of salt (m) forms? Give 1 decimal place.", 15.9,
          [("Mass per m2", "1 000 x 35 = 35 000 kg."), ("Thickness", "35 000 / 2 200 = 15.9 m.")],
          "Evaporite thickness from sea water", "Calculation", "Find the mass of salt under 1 m2, then its volume.", tol=0.2, unit="m"),
        Q("Nodular 'chicken-wire' anhydrite growing within tidal-flat sediment with microbial mats indicates", "A sabkha on a hot, arid coast",
          [("A deep barred basin floor", "Deep basin evaporites are laminated precipitates, not nodules grown within tidal-flat sediment."),
           ("A freshwater swamp", "Swamps produce peat, not anhydrite."),
           ("A deep-sea turbidite fan", "Turbidites contain graded sands, not evaporite nodules.")],
          [("Clue", "Nodules grow inside sediment just above high tide with microbial mats."), ("Setting", "A coastal sabkha in an arid climate.")],
          "Sabkha evaporites", "Interpretation", "Where do salts grow inside coastal sediment?"),
        N("Peat compacts to bituminous coal in a ratio of 10 to 1. What thickness of peat (m) formed a 2.4 m coal seam?", 24,
          [("Ratio", "Peat thickness = coal thickness x 10."), ("Answer", "2.4 x 10 = 24 m.")],
          "Compaction of peat to coal", "Calculation", "Multiply by the compaction ratio.", tol=0.1, unit="m"),
        Q("Which coal has the highest rank?", "Anthracite",
          [("Lignite", "Lignite is a low-rank brown coal with high moisture."),
           ("Peat", "Peat is not yet coal; it is the starting material."),
           ("Sub-bituminous coal", "It lies between lignite and bituminous coal.")],
          [("Series", "Peat, lignite, sub-bituminous, bituminous, anthracite."), ("Highest", "Anthracite: most carbon, least volatile matter.")],
          "Coal rank", "Recall", "Which coal has the most carbon?"),
        Q("Why are thick halite layers important to petroleum geologists?", "Halite flows upward into salt domes that deform overlying beds and seal traps",
          [("Halite is a petroleum source rock", "Source rocks are organic-rich shales; halite contains no kerogen."),
           ("Halite is a very porous reservoir", "Halite is almost impermeable, so it seals rather than stores oil."),
           ("Halite turns into oil on heating", "Halite is an inorganic salt and cannot make oil.")],
          [("Property", "Salt is weak and less dense than buried sediment, so it rises as diapirs."), ("Result", "Domes arch beds into traps and salt seals them.")],
          "Salt domes", "Reasoning", "Think about how salt behaves under load and how permeable it is."),
    ]))

# ------------------------------------------------------------------ 8. Stress and strain
use(108)
SETS.append(practice_set(
    module=M2, topic="Stress and strain",
    title="Principal stresses, Mohr circle and strain ellipse", lesson="gyu1-stress-strain-mohr-circle",
    questions=[
        Q("The principal stresses at a point are the stresses that act", "On three mutually perpendicular planes that carry no shear stress",
          [("Only on horizontal planes", "Principal planes may have any orientation; they are defined by zero shear stress."),
           ("On planes at 45 degrees to each other", "Planes of greatest shear stress are at 45 degrees to sigma1; principal planes are perpendicular to each other."),
           ("Only during earthquakes", "Principal stresses exist at every point in a stressed body at all times.")],
          [("Definition", "Principal planes have zero shear stress."), ("Geometry", "There are three, mutually perpendicular: sigma1, sigma2, sigma3.")],
          "Principal stresses", "Recall", "What is missing on a principal plane?"),
        N("Calculate the lithostatic stress (MPa) at 2 km depth under rock of density 2 500 kg/m3 (g = 9.81 m/s2). Give 1 decimal place.", 49.1,
          [("Formula", r"$\sigma = \rho g h$."), ("Substitute", "2 500 x 9.81 x 2 000 = 49 050 000 Pa = 49.1 MPa.")],
          "Lithostatic stress", "Calculation", "Use sigma = rho g h with h in metres.", tol=0.1, unit="MPa"),
        N("sigma1 = 100 MPa and sigma3 = 40 MPa. Calculate the normal stress (MPa) on a plane whose normal is at 30 degrees to sigma1.", 85,
          [("Centre and radius", "Centre 70 MPa, radius 30 MPa."), ("Normal stress", r"$70 + 30\cos 60^\circ = 85$ MPa.")],
          "Normal stress on a plane", "Calculation", "Use 2 theta, not theta, in the cosine.", tol=0.5, unit="MPa"),
        N("For the same stresses and plane (sigma1 = 100 MPa, sigma3 = 40 MPa, theta = 30 degrees), calculate the shear stress in MPa.", 26.0,
          [("Formula", r"$\tau = \frac{\sigma_1 - \sigma_3}{2}\sin 2\theta$."), ("Substitute", r"$30 \sin 60^\circ = 25.98$ MPa.")],
          "Shear stress on a plane", "Calculation", "The radius of the Mohr circle times sin 2 theta.", tol=0.3, unit="MPa"),
        Q("On which planes is the shear stress greatest?", "Planes at 45 degrees to sigma1",
          [("Planes perpendicular to sigma1", "Planes perpendicular to sigma1 are principal planes with zero shear stress."),
           ("Planes parallel to sigma1 and sigma2", "These are principal planes (perpendicular to sigma3), also with zero shear stress."),
           ("Planes at 30 degrees to sigma1", "Shear stress there is high but not the maximum; the maximum is at 2 theta = 90 degrees.")],
          [("Mohr circle", "tau is greatest at the top of the circle, 2 theta = 90 degrees."), ("Angle", "theta = 45 degrees.")],
          "Maximum shear stress", "Concept", "Where is the top of the Mohr circle?"),
        Q("A fossil line 12 cm long is stretched to 15 cm. Its extension and stretch are", "e = +0.25 and S = 1.25",
          [("e = +0.20 and S = 1.20", "That divides the change by the new length (15) instead of the original (12)."),
           ("e = +3 and S = 15", "Extension is the change divided by the original length, not the change in centimetres."),
           ("e = -0.25 and S = 0.75", "The line got longer, so the extension is positive.")],
          [("Extension", "(15 - 12)/12 = +0.25."), ("Stretch", "S = 15/12 = 1.25 = 1 + e.")],
          "Extension and stretch", "Calculation", "Divide the change by the original length."),
        N("A marker line originally perpendicular to a shear zone is rotated through an angular shear of 60 degrees. Calculate the shear strain gamma (2 decimal places).", 1.73,
          [("Formula", r"$\gamma = \tan\psi$."), ("Substitute", r"$\tan 60^\circ = 1.73$.")],
          "Shear strain", "Calculation", "Shear strain is the tangent of the angular shear.", tol=0.01, unit=""),
        Q("Pebbles in a deformed conglomerate give a strain ratio of 2, while ooids in an interbedded limestone give 4. The best explanation is", "The stiff pebbles deformed less than their matrix, so they underestimate the strain",
          [("The limestone was deformed in a different event", "Interbedded rocks in one outcrop normally share the same deformation; competence contrast is the simpler explanation."),
           ("Ooids are always larger than pebbles", "Size does not set the strain ratio."),
           ("Strain cannot be measured from deformed objects", "It can, if the markers deformed like the rock around them.")],
          [("Assumption", "Markers must deform with the rock."), ("Problem", "Competent pebbles resist deformation, giving low values.")],
          "Strain markers and their limits", "Reasoning", "Do strong pebbles and soft ooids behave alike?"),
    ]))

# ------------------------------------------------------------------ 9. Brittle and ductile deformation
SSQ = "algyu1-stressstrain-q.svg"
SSQ_A = ("Stress against strain. Curve 1 (orange) rises steeply in a straight line and ends at a cross X. Curve 2 (blue) "
         "rises in a straight line to a point Y, then bends over and continues to large strain at nearly constant stress.")
use(109)
SETS.append(practice_set(
    module=M2, topic="Brittle and ductile deformation",
    title="Controls on brittle and ductile behaviour and Coulomb failure", lesson="gyu1-brittle-ductile-deformation",
    questions=[
        Q("On the graph, point Y on curve 2 marks", "The yield point (elastic limit), after which strain is permanent",
          [("The point of brittle fracture", "Fracture is marked by the cross X at the end of curve 1."),
           ("The start of elastic deformation", "Elastic deformation starts at the origin and ends at Y."),
           ("The greatest strain the rock can reach", "Curve 2 continues to much larger strains after Y.")],
          [("Shape", "The line is straight (elastic) up to Y, then curves."), ("Meaning", "Y is the yield point; beyond it the rock flows permanently.")],
          "Stress-strain curves", "Interpretation", "Where does the straight part of curve 2 end?", diagram=SSQ, alt=SSQ_A),
        Q("Curve 1 most likely represents a rock deformed", "Cold, at low confining pressure and a fast strain rate",
          [("Hot, at high confining pressure and a slow strain rate", "Those conditions give ductile behaviour like curve 2."),
           ("Under lithostatic stress only", "Lithostatic stress alone changes volume, not shape, and causes no fracture."),
           ("In a shear zone at 25 km depth", "Deep shear zones deform in a ductile way.")],
          [("Shape", "Curve 1 is elastic up to sudden fracture: brittle."), ("Conditions", "Brittle failure is favoured by low temperature, low confining pressure and fast loading.")],
          "Brittle behaviour", "Interpretation", "Curve 1 ends with a fracture.", diagram=SSQ, alt=SSQ_A),
        N("A limestone shortens elastically by a strain of 0.0005 under a stress of 30 MPa. Calculate Young's modulus in GPa.", 60,
          [("Formula", r"$E = \sigma/\varepsilon$."), ("Substitute", "30 000 000 / 0.0005 = 60 000 000 000 Pa = 60 GPa.")],
          "Young's modulus", "Calculation", "Divide stress by strain, then convert to GPa.", tol=0.5, unit="GPa"),
        Q("Which factor makes brittle failure MORE likely?", "An increase in pore-fluid pressure",
          [("An increase in temperature", "Higher temperature favours ductile flow."),
           ("An increase in confining pressure", "Confining pressure suppresses cracks and favours ductile behaviour."),
           ("A decrease in strain rate", "Slower loading favours creep and ductile flow.")],
          [("Effective stress", "Pore pressure is subtracted from the normal stress."), ("Result", "Lower effective stress means less frictional resistance: brittle failure is easier.")],
          "Controls on deformation", "Concept", "Which factor reduces the effective normal stress?"),
        N("With a surface temperature of 25 degrees C and a geothermal gradient of 25 degrees C per km, at what depth (km) is the 300 degrees C brittle-ductile transition?", 11,
          [("Temperature rise", "300 - 25 = 275 degrees C."), ("Depth", "275 / 25 = 11 km.")],
          "Brittle-ductile transition", "Calculation", "Subtract the surface temperature first.", tol=0.1, unit="km"),
        N("A fault has cohesion 10 MPa and coefficient of friction 0.6. The normal stress is 50 MPa and pore-fluid pressure 20 MPa. What shear stress (MPa) is needed for slip?", 28,
          [("Effective normal stress", "50 - 20 = 30 MPa."), ("Coulomb", "10 + 0.6 x 30 = 28 MPa.")],
          "Mohr-Coulomb criterion with pore pressure", "Calculation", "Subtract the pore pressure before using tau = C + mu sigma_n.", tol=0.2, unit="MPa"),
        N("A rock has a coefficient of internal friction of 0.6. At what angle (degrees) to sigma1 do shear fractures form? Give 1 decimal place.", 29.5,
          [("Friction angle", r"$\phi = \tan^{-1} 0.6 = 31.0^\circ$."), ("Fracture angle", "45 - 31.0/2 = 29.5 degrees.")],
          "Orientation of shear fractures", "Calculation", "Find phi from mu, then use 45 - phi/2.", tol=0.3, unit="degrees"),
        Q("A quartz vein in a mica schist has been stretched into a chain of sausage-shaped pieces. This structure and its cause are", "Boudinage, caused by extension of a competent layer in weaker rock",
          [("Cross-bedding, caused by a current", "Cross-bedding is a sedimentary structure, not a deformation structure."),
           ("Graded bedding, caused by a waning flow", "Grading is sedimentary and has nothing to do with stretching."),
           ("Columnar jointing, caused by cooling", "Columnar joints form in cooling lava or sills, not in stretched veins.")],
          [("Competence", "The quartz vein is stronger than the schist."), ("Result", "Stretching breaks or necks the strong layer into boudins.")],
          "Competence and boudinage", "Application", "Which layer is stronger, and what happens when it is stretched?"),
    ]))

# ------------------------------------------------------------------ 10. Folds
FMQ = "algyu1-foldmap-q.svg"
FMQ_A = ("Schematic map, eastings 40-48, northings 60-66. Strips west to east: C, B, A, B, C (wide), B. All dips are 30 "
         "degrees; dip symbols point away from strip A and towards the middle of wide strip C. Line X-Y at northing 63.")
use(110)
SETS.append(practice_set(
    module=M2, topic="Folds",
    title="Fold description, Ramsay classes and map evidence", lesson="gyu1-folds-classification-map-evidence",
    questions=[
        Q("On the map, the structure centred on strip A (easting 43) is", "An anticline, because the oldest bed is in the core and the beds dip away",
          [("A syncline, because beds B are on both sides", "Beds repeating on both sides do not decide it: the core age and dip directions do. A has the oldest rock and dips are away."),
           ("A dome, because the strips are symmetrical", "A dome would show closed, circular outcrops; here the strips run straight north to south."),
           ("A normal fault, because the strips are straight", "Straight strips show beds of constant strike; no displacement is shown.")],
          [("Core", "A is the oldest bed."), ("Dips", "Dip symbols point away from the axis.")],
          "Anticline on a map", "Interpretation", "Which bed is oldest and which way do the dip symbols point?", diagram=FMQ, alt=FMQ_A),
        Q("The core bed of the structure at easting 46 is", "C, the youngest bed",
          [("A, the oldest bed", "A lies in the core of the anticline at easting 43."),
           ("B, the middle bed", "B lies on both limbs of both structures but is not at the core of either."),
           ("There is no core bed", "Every fold has a bed that outcrops along its axis.")],
          [("Pattern", "C is in the middle with older B on both sides."), ("Rule", "Youngest in the core of a syncline.")],
          "Core beds of folds", "Interpretation", "Which bed lies on the axis at easting 46?", diagram=FMQ, alt=FMQ_A),
        Q("Which six-figure grid reference gives the position where the anticline axis crosses northing 64.5?", "430645",
          [("645430", "The northing has been written first; the easting always comes first."),
           ("4306", "That is a four-figure reference, not precise enough for a point."),
           ("460645", "Easting 46.0 is the syncline axis, not the anticline axis.")],
          [("Easting", "Axis at 43.0: digits 430."), ("Northing", "64.5: digits 645, so 430645.")],
          "Six-figure grid references", "Application", "Easting first, three digits each.", diagram=FMQ, alt=FMQ_A),
        N("Bed B outcrops west of the anticline as a strip 0.80 km wide on flat ground and dips at 30 degrees. What is its true thickness in metres?", 400,
          [("Formula", r"$t = w \sin\delta$."), ("Calculate", "0.80 x sin 30 = 0.40 km = 400 m.")],
          "True thickness from outcrop width", "Calculation", "Multiply the outcrop width by the sine of the dip.", tol=2, unit="m", diagram=FMQ, alt=FMQ_A),
        N("A symmetrical fold has both limbs dipping at 40 degrees. Find its interlimb angle in degrees.", 100,
          [("Rule", "Interlimb angle = 180 - (sum of the two limb dips)."), ("Answer", "180 - 80 = 100 degrees (an open fold).")],
          "Interlimb angle", "Calculation", "Subtract the limb dips from 180 degrees.", tol=0.5, unit="degrees"),
        N("A layer is 10 m thick at the hinge of a Class 2 fold. What is its thickness in metres at right angles to the layer where it dips at 60 degrees?", 5,
          [("Class 2", r"$t' = \cos\alpha = 0.5$."), ("Thickness", "10 x 0.5 = 5 m.")],
          "Ramsay thickness ratio", "Calculation", "For similar folds t-prime equals cos of the dip.", tol=0.05, unit="m"),
        Q("Which of these is a MAJOR structure associated with folds, as opposed to a fold type?", "A salt dome",
          [("An anticline", "That is itself a type of fold, not a structure associated with folds."),
           ("A tension gash", "Tension gashes are minor structures."),
           ("A desiccation crack", "That is a sedimentary structure formed by drying.")],
          [("Major structures", "Salt domes, gravity collapse structures, nappes, valley bulges and cambering, periclines."), ("Choice", "Only the salt dome is on the list.")],
          "Structures associated with folds", "Recall", "Think of structures on a larger scale than a single fold."),
        Q("A competent sandstone bed keeps the same thickness, measured at right angles to the bed, all round a fold. Its Ramsay class is", "Class 1B (parallel fold)",
          [("Class 2 (similar fold)", "In a Class 2 fold the layer thins on the limbs (t' = cos alpha)."),
           ("Class 3", "In Class 3 the layer is thickest on the limbs."),
           ("It cannot be classified without a map", "Classification uses the profile of the layer and its dip isogons.")],
          [("Constant thickness", "Orthogonal thickness constant means t' = 1."), ("Class", "Dip isogons converge towards the core: Class 1B.")],
          "Ramsay classification", "Concept", "Which class has t-prime equal to 1?"),
    ]))

# ------------------------------------------------------------------ 11. Faults and shear zones
FLQ = "algyu1-fault-q.svg"
FLQ_A = ("Cross-section of a fault dipping steeply to the right. A marker bed on the left (P) is lower on the right (Q). "
         "R is the fault plane, S the vertical offset of the bed, T the horizontal offset. No fault type is stated.")
use(111)
SETS.append(practice_set(
    module=M2, topic="Faults and shear zones",
    title="Fault types, throw, heave and shear zones", lesson="gyu1-faults-shear-zones-kinematics",
    questions=[
        Q("In the figure, block Q (right of the fault plane R) is the", "Hanging wall",
          [("Footwall", "The footwall is the block below the fault plane, here P, on the left."),
           ("Horst", "A horst is a raised block between two faults."),
           ("Graben", "A graben is a down-dropped block between two faults.")],
          [("Geometry", "R dips down to the right, so the block above the plane is on the right."), ("Name", "The block above an inclined fault plane is the hanging wall.")],
          "Hanging wall and footwall", "Interpretation", "Which block lies above the inclined plane?", diagram=FLQ, alt=FLQ_A),
        Q("The marker bed is lower on the hanging wall side. The fault is a", "Normal fault",
          [("Reverse fault", "In a reverse fault the hanging wall moves up relative to the footwall."),
           ("Dextral strike-slip fault", "Strike-slip faults show horizontal, not vertical, offset in section."),
           ("Thrust", "A thrust is a gently dipping reverse fault; the hanging wall would be higher.")],
          [("Movement", "The hanging wall has moved down relative to the footwall."), ("Type", "That is a normal fault.")],
          "Fault classification", "Application", "Which way has the hanging wall moved?", diagram=FLQ, alt=FLQ_A),
        Q("Which letter marks the throw?", "S",
          [("T", "T is the horizontal offset, the heave."), ("R", "R is the fault plane itself."), ("P", "P is the footwall block.")],
          [("Definition", "Throw is the vertical component of the displacement."), ("Figure", "S is the vertical offset of the bed.")],
          "Throw and heave", "Interpretation", "Throw is vertical, heave horizontal.", diagram=FLQ, alt=FLQ_A),
        N("A normal fault dips at 60 degrees and a bed is offset by a throw of 120 m. Calculate the heave in metres (1 decimal place).", 69.3,
          [("Formula", r"heave = throw / tan(dip)."), ("Calculate", "120 / 1.732 = 69.3 m.")],
          "Heave from throw", "Calculation", "Divide the throw by the tangent of the dip.", tol=0.3, unit="m"),
        N("For the same fault (dip 60 degrees, throw 120 m), calculate the net slip in metres (1 decimal place).", 138.6,
          [("Formula", r"net slip = throw / sin(dip)."), ("Calculate", "120 / 0.866 = 138.6 m.")],
          "Net slip", "Calculation", "Use the sine of the dip to go from throw to slip.", tol=0.5, unit="m"),
        N("A rock has a coefficient of internal friction of 0.6. Predict the dip (degrees, 1 decimal place) of a normal fault, where sigma1 is vertical.", 60.5,
          [("Friction angle", r"$\phi = \tan^{-1} 0.6 = 31.0^\circ$."), ("Fault angle to sigma1", "45 - 15.5 = 29.5 degrees."), ("Dip", "90 - 29.5 = 60.5 degrees.")],
          "Anderson and Coulomb", "Calculation", "The fault makes about 30 degrees with the vertical sigma1.", tol=0.3, unit="degrees"),
        N("Across a ductile shear zone 10 m wide, markers are displaced by 50 m. What is the shear strain?", 5,
          [("Formula", r"$\gamma$ = displacement / width."), ("Calculate", "50 / 10 = 5.")],
          "Shear strain in a shear zone", "Calculation", "Divide displacement by the width of the zone.", tol=0.05, unit=""),
        Q("A candidate describes a fault on a map as running 'S-N'. The best correction is", "Write the trend as north to south (or south to north) with the location given by grid reference or cardinal points",
          [("No correction is needed because abbreviations are accepted", "The Board's report notes that candidates should not use short-hand and should write directions in full."),
           ("Describe it as a fold instead", "A fault is not a fold; candidates lost marks by describing folds when asked for faults."),
           ("State only its dip angle", "The question asks for location and trend, and a map gives no dip angle for a fault plane.")],
          [("Requirement", "Location and trend in full, with the correct direction pair."), ("Avoid", "Short-hand and mixing the fault with a fold.")],
          "Describing faults on maps", "Reasoning", "What did the Board's examiners say about abbreviations and directions?"),
    ]))

# ------------------------------------------------------------------ 12. Cleavage and foliation
CLQ = "algyu1-cleavage-q.svg"
CLQ_A = ("Cross-section of three folded layers Q (blue curves) with a vertical dashed line P through the crest and thin "
         "orange lines R, nearly vertical and fanning slightly, cutting the layers. H is a point on the crest.")
use(112)
SETS.append(practice_set(
    module=M2, topic="Cleavage and foliation",
    title="Cleavage, foliation and bedding-cleavage relationships", lesson="gyu1-cleavage-foliation",
    questions=[
        Q("In the figure, the thin lines R are best described as", "Axial planar cleavage, parallel to the axial plane P",
          [("Bedding, parallel to the layers Q", "Bedding is the folded layering Q, not the straight lines R."),
           ("Joints formed by cooling", "Cooling joints form in igneous rocks, not in folded sedimentary layers."),
           ("Faults, because they cut the layers", "Faults would offset the layers; none of the layers is displaced.")],
          [("Orientation", "R is nearly parallel to the vertical axial plane P."), ("Name", "Cleavage parallel to the axial plane is axial planar cleavage.")],
          "Axial planar cleavage", "Interpretation", "Compare the direction of R with the dashed line P.", diagram=CLQ, alt=CLQ_A),
        Q("At point H, near the crest, the angle between bedding Q and cleavage R is", "About 90 degrees",
          [("About 0 degrees", "They would be parallel only on the limbs of a tight fold; at the crest the layers are flat and the cleavage is vertical."),
           ("About 45 degrees", "At the crest the layers are horizontal and the cleavage vertical, so the angle is not 45."),
           ("It cannot be measured", "It can be measured on a section like this.")],
          [("Orientation", "Layers are roughly horizontal at the crest and cleavage is near vertical."), ("Angle", "About 90 degrees.")],
          "Bedding-cleavage angle at the hinge", "Interpretation", "Compare the direction of the crest with the lines R.", diagram=CLQ, alt=CLQ_A),
        Q("Cleavage forms perpendicular to the", "Greatest compressive stress (sigma1)",
          [("Least compressive stress (sigma3)", "Cleavage lies parallel to the plane containing the intermediate and long axes of strain, perpendicular to sigma1."),
           ("Original bedding", "Cleavage may cut bedding at any angle and is not defined by it."),
           ("Direction of gravity", "The orientation of cleavage is set by tectonic stress, not gravity alone.")],
          [("Mechanism", "Platy minerals rotate and grow in the plane of flattening."), ("Orientation", "Plane of flattening is perpendicular to sigma1.")],
          "Orientation of cleavage", "Concept", "Think of flattening a ball of clay."),
        N("Spherical reduction spots in a slate are now ellipses with axial ratio 9:1 (no area change). What percentage shortening is there perpendicular to the cleavage? Give a whole number.", 67,
          [("Original diameter", "Square root of (9 x 1) = 3."), ("Shortening", "(3 - 1)/3 = 0.667, so about 67 per cent.")],
          "Strain from deformed spots", "Calculation", "Find the original circle diameter from the area.", tol=1, unit="%"),
        Q("In an outcrop, bedding dips 60 degrees east and cleavage dips 35 degrees east, with the same strike. The beds are", "Overturned, because the cleavage is less steep than the bedding",
          [("Upright, because the cleavage dips east too", "The direction of dip is the same, but the cleavage is LESS steep than bedding, which indicates overturning."),
           ("Upright, because the cleavage is steeper", "The cleavage is gentler, not steeper."),
           ("In a fold hinge, because both dip east", "Both planes dip in the same direction on a limb; the hinge would show them nearly perpendicular.")],
          [("Rule", "Same dip direction: cleavage steeper = upright, gentler = overturned."), ("Here", "35 is less than 60: overturned.")],
          "Bedding-cleavage way-up rule", "Reasoning", "Compare 35 and 60 degrees."),
        Q("Which sequence lists rocks formed from shale in order of increasing metamorphic grade?", "Slate, phyllite, schist, gneiss",
          [("Gneiss, schist, phyllite, slate", "This is the reverse: grade falls along it."),
           ("Schist, slate, gneiss, phyllite", "Slate is lower grade than schist."),
           ("Phyllite, gneiss, slate, schist", "The order is not by grade.")],
          [("Grain size", "Grows with temperature and pressure."), ("Order", "Slate, phyllite, schist, gneiss.")],
          "Metamorphic grade series", "Recall", "Which rock is the finest grained?"),
        Q("A candidate lists granite as a foliated metamorphic rock. The best correction is", "Granite is igneous; a foliated rock with banding of quartz-feldspar and biotite-hornblende is gneiss",
          [("Granite is metamorphic when it is coarse grained", "Grain size does not make a rock metamorphic: granite crystallizes from magma."),
           ("Granite is sedimentary because it contains quartz", "Quartz is common in igneous rocks as well."),
           ("The statement is right because granite can be strongly banded", "Strongly banded rocks of that composition are gneisses, not granites.")],
          [("Origin", "Granite cools from magma."), ("Equivalent", "Gneiss is the banded, foliated metamorphic rock of similar composition.")],
          "Foliated metamorphic rocks", "Reasoning", "How did granite form?"),
        Q("A mica schist contains garnet and kyanite and visible aligned micas. It indicates", "Medium-grade regional metamorphism of a pelitic (shale) parent",
          [("Low-grade metamorphism of limestone", "Limestone gives marble, and garnet and kyanite need medium grade."),
           ("Contact metamorphism of sandstone", "Contact metamorphism gives non-foliated hornfels or quartzite."),
           ("Cooling of granitic magma", "Schist is metamorphic, not igneous.")],
          [("Minerals", "Garnet and kyanite are medium-grade minerals of pelitic rocks."), ("Texture", "Aligned micas: foliation from regional metamorphism.")],
          "Schist and grade", "Application", "Which parent rock produces micas, garnet and kyanite?"),
    ]))

# ------------------------------------------------------------------ 13. Stratum contours and three-point problems
TPQ = "algyu1-threepoint-q.svg"
TPQ_A = ("Map with east and north axes in metres. Borehole A at (0, 0) with the top of a coal seam at 300 m, B at "
         "(1000, 0) at 180 m and C at (0, 500) at 220 m. No contours are drawn.")
use(113)
SETS.append(practice_set(
    module=M2, topic="Stratum contours and three-point problems",
    title="Strike, dip, depth and thickness from stratum contours", lesson="gyu1-stratum-contours-three-point",
    questions=[
        Q("A stratum contour on a bed is", "A line joining points of equal height on the surface of the bed",
          [("A line joining points of equal thickness of the bed", "That would be an isopach line, not a stratum contour."),
           ("A line drawn in the direction of dip", "Dip direction is at right angles to a stratum contour."),
           ("A line joining beds of the same age", "That describes a time line or correlation, not a structure contour.")],
          [("Definition", "Equal height above sea level on the bedding surface."), ("Property", "It is a strike line.")],
          "Stratum contours", "Recall", "Think of the horizontal line on a tilted bed."),
        Q("In the map, the point on line AB where the top of the seam is at 220 m (the height of C) is", "Two thirds of the way from A to B, at 667 m east",
          [("Half way, at 500 m east", "Half way would be 240 m, the mean of 300 and 180."),
           ("One third of the way, at 333 m east", "One third would be 260 m."),
           ("At B, 1 000 m east", "B is at 180 m, not 220 m.")],
          [("Fraction", "(300 - 220)/(300 - 180) = 80/120 = 2/3."), ("Position", "2/3 of 1 000 m is 667 m.")],
          "Three-point problem: interpolation", "Calculation", "Find what fraction of the 120 m drop has occurred by 220 m.", diagram=TPQ, alt=TPQ_A),
        Q("The strike line joins C to the point on AB at 667 m east. Its bearing is", "127 degrees (south-east to north-west)",
          [("037 degrees", "037 degrees is the dip direction, at right angles to strike."),
           ("090 degrees", "A due east-west strike would need C and the point on AB to have the same northing."),
           ("000 degrees", "A north-south strike would need them to have the same easting.")],
          [("Vector", "From C (0, 500) to (667, 0): 667 east and 500 south."), ("Bearing", "arctan(667/-500): 127 degrees, in the south-east direction.")],
          "Strike from three points", "Calculation", "Draw the line and measure its direction from north.", diagram=TPQ, alt=TPQ_A),
        N("The perpendicular distance between the 300 m contour (through A) and the 220 m contour is 400 m. Calculate the dip of the bed in degrees (1 decimal place).", 11.3,
          [("Formula", r"$\tan(\text{dip}) = $ vertical interval / horizontal distance."), ("Calculate", "tan(dip) = 80/400 = 0.20, so dip = 11.3 degrees.")],
          "Dip from contour spacing", "Calculation", "Use the 80 m drop between the contours.", tol=0.1, unit="degrees", diagram=TPQ, alt=TPQ_A),
        Q("The dip direction of the bed is", "037 degrees (north-east)",
          [("217 degrees (south-west)", "This points up the dip, towards higher contours."),
           ("127 degrees (south-east)", "That is the strike direction."),
           ("307 degrees (north-west)", "That is the other end of the strike line.")],
          [("Rule", "Dip direction is at right angles to strike, towards lower heights."), ("Here", "Heights fall to the north-east (C is lower than A): 037 degrees.")],
          "Dip direction", "Application", "At right angles to strike, which way do heights fall?", diagram=TPQ, alt=TPQ_A),
        N("The seam top is 140 m above sea level at a point where the ground is 232 m. How deep (m) must a borehole go to reach it?", 92,
          [("Formula", "Depth = ground height - bed height."), ("Calculate", "232 - 140 = 92 m.")],
          "Depth to a bed", "Calculation", "Subtract the bed height from the ground height.", tol=0.5, unit="m"),
        N("A coal seam is 25 m thick measured vertically and dips at 11.3 degrees. What is its true thickness in metres (1 decimal place)?", 24.5,
          [("Formula", "True thickness = vertical thickness x cos(dip)."), ("Calculate", "25 x cos 11.3 = 24.5 m.")],
          "True thickness", "Calculation", "True thickness is measured at right angles to the bed.", tol=0.1, unit="m"),
        N("A bed has a true dip of 11.3 degrees (tan 0.20) towards 037 degrees. Calculate its apparent dip in degrees (1 decimal place) on a section running west to east (bearing 090).", 6.8,
          [("Angle beta", "90 - 37 = 53 degrees between the section and the dip direction."), ("Formula", "tan(app) = 0.20 x cos 53 = 0.12, so app = 6.8 degrees.")],
          "Apparent dip", "Calculation", "Use tan(app) = tan(dip) x cos(beta).", tol=0.1, unit="degrees"),
    ]))

# ------------------------------------------------------------------ 14. Geological cross-sections
use(114)
SETS.append(practice_set(
    module=M2, topic="Geological cross-sections",
    title="Drawing and reading sections: apparent dip and exaggeration", lesson="gyu1-geological-cross-sections",
    questions=[
        Q("Which of these is NOT a required part of a geological cross-section?", "A copy of the whole geological map",
          [("The end points X and Y with directions", "Section ends and compass directions must be shown."),
           ("The horizontal scale and vertical exaggeration", "Scales and VE must be stated."),
           ("Fold axes and core beds", "These must be inserted on the section, as the Board's examiners expected.")],
          [("Required", "Title, ends, scales, VE, units, axes, core beds."), ("Not required", "Redrawing the map: a section is a vertical slice.")],
          "Contents of a cross-section", "Recall", "A section is not a plan view."),
        Q("A candidate draws only the ground surface along XY and labels the beds along it. The main weakness is that", "It is a topographic profile; it does not show the beds, fold axes and core beds below the surface",
          [("The profile should be curved instead of straight", "Straight or curved depends on the topography, not on the answer's quality."),
           ("The beds should be coloured red", "Colour is not the issue."),
           ("It should show the map symbols instead", "Map symbols belong on the map; the section shows structure below ground.")],
          [("Task", "A section shows the beds underground."), ("Fault in answer", "A profile alone does not show structure.")],
          "Cross-section vs topographic profile", "Reasoning", "What lies below the line of the ground?"),
        N("Beds strike 000 degrees and dip 30 degrees. A section runs at 060 degrees (VE = 1). Calculate the apparent dip in degrees (1 decimal place).", 26.6,
          [("Angle to strike", "Beta = 60 degrees."), ("Formula", "tan(app) = tan 30 x sin 60 = 0.5774 x 0.8660 = 0.5, so app = 26.6 degrees.")],
          "Apparent dip", "Calculation", "Use tan(app) = tan(dip) x sin(beta).", tol=0.1, unit="degrees"),
        N("Beds dip at 50 degrees and strike 000 degrees. What is the apparent dip in degrees (1 decimal place) on a section at 045 degrees?", 40.1,
          [("Beta", "45 degrees to strike."), ("Calculate", "tan(app) = tan 50 x sin 45 = 0.8427, so app = 40.1 degrees.")],
          "Apparent dip", "Calculation", "The section is 45 degrees from strike.", tol=0.1, unit="degrees"),
        N("A section has horizontal scale 1:50 000 and vertical scale 1:25 000. What is the vertical exaggeration?", 2,
          [("Formula", "VE = horizontal scale / vertical scale."), ("Calculate", "50 000 / 25 000 = 2.")],
          "Vertical exaggeration", "Calculation", "Divide the scale denominators: horizontal over vertical.", tol=0, unit=""),
        N("Beds dip at 30 degrees and the section has VE = 2. At what angle (degrees, 1 decimal place) are the beds drawn?", 49.1,
          [("Formula", "tan(drawn) = VE x tan(dip)."), ("Calculate", "2 x 0.5774 = 1.155, so drawn dip = 49.1 degrees.")],
          "Dip drawn with exaggeration", "Calculation", "Multiply tan(dip) by VE.", tol=0.1, unit="degrees"),
        N("On the map of the Folds lesson the beds dip at 30 degrees and the anticline axis (E43) and syncline axis (E46) are 3 km apart. If the top of bed A is 0.30 km above the flat ground at the anticline axis, how deep (m) is it below ground at the syncline axis? Give a whole number.", 1432,
          [("Drop", "3 x tan 30 = 1.732 km."), ("Height", "0.30 - 1.732 = -1.432 km."), ("Depth", "1.432 km = 1 432 m.")],
          "Depth from a section", "Calculation", "Find the fall in height over 3 km and subtract from 0.30 km.", tol=5, unit="m"),
        Q("A small patch of limestone (the youngest bed) is completely surrounded by older sandstone. It is best described as", "An outlier, preserved by folding and left by erosion",
          [("An inlier, formed by deposition", "An inlier is older rock surrounded by younger rock, and erosion, not deposition, explains the shape."),
           ("An angular unconformity, formed by faulting", "An angular unconformity is a surface between tilted older beds and younger beds, not a patch of rock."),
           ("A dyke, formed by volcanic eruption", "A dyke is a vertical sheet of intrusive rock cutting the beds.")],
          [("Evidence", "Younger rock entirely surrounded by older rock."), ("Formation", "Folding or faulting preserved it and erosion removed the rest.")],
          "Outliers and inliers", "Concept", "Is the surrounding rock older or younger than the patch?"),
    ]))

# ==== END OF SETS ====
