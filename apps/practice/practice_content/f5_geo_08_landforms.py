"""Practice sets for Form 5 Geography, Geomorphology: Denudational processes and landforms (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Geomorphology"
TOPIC = "Denudational processes and landforms"

SETS = []

# ------------------------------------------------------------------ 1. Weathering
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Weathering: types, landforms and factors",
    lesson="land-weathering",
    questions=[
        MC("Weathering is best defined as the", [
            C("carrying away of rock by a river", why="This describes erosion and transportation, not weathering."),
            C("breaking down of rock where it lies", correct=True),
            C("building up of new land by deposits", why="This is deposition."),
            C("movement of rock down a slope", why="This is mass movement, such as a landslide."),
        ], steps=[S("Recall", text="Weathering breaks or rots rock in place. The pieces are not carried away while the rock is being weathered.")],
           concept="Definition of weathering", skill="Recall", hint="Think of what happens to the rock: does it move?"),
        MC("Which of these is a type of physical weathering that is common in the tropics?", [
            C("Freeze-thaw", why="Freeze-thaw needs temperatures below zero, which are rare in tropical lowlands."),
            C("Hydrolysis", why="Hydrolysis is a chemical process."),
            C("Oxidation", why="Oxidation is a chemical process in which iron rusts."),
            C("Exfoliation by temperature change", correct=True),
        ], steps=[S("Sort the processes", text="Hydrolysis and oxidation are chemical. Freeze-thaw is physical but rare in the tropics. Exfoliation is physical and common.")],
           concept="Physical weathering in the tropics", skill="Recall", hint="Which physical process does not need frost?"),
        MC("Rusting of the iron in a rock, which makes many tropical soils red, is called", [
            C("oxidation", correct=True),
            C("hydrolysis", why="Hydrolysis changes minerals such as feldspar into clay."),
            C("exfoliation", why="Exfoliation is the peeling of rock sheets by heat and cold."),
            C("salt crystallisation", why="This is a physical process in which salt crystals widen cracks."),
        ], steps=[S("Match process and result", text="Oxygen reacts with iron to make rust. This is oxidation.")],
           concept="Chemical weathering processes", skill="Concept", hint="Rust forms when iron meets oxygen."),
        MC("Which statement about a tor is correct?", [
            C("It forms when a river cuts down into rock.", why="Tors are made by weathering and then removal of the regolith, not by river down-cutting."),
            C("It is a pile of rounded blocks left after the regolith around them is removed.", correct=True),
            C("It is a lake cut off from a river.", why="This describes an ox-bow lake."),
            C("It is a ridge of sand built by waves.", why="This describes a spit or a bar."),
        ], steps=[S("Stages", text="Joints let water in, chemical weathering makes rounded blocks in the regolith, and erosion removes the regolith so the blocks stand out.")],
           concept="Tors", skill="Concept", hint="Which landform is a weathering landform?"),
        MC("Why is freeze-thaw rare in the lowlands of southern Cameroon?", [
            C("The rocks there are very hard.", why="Rock hardness does not stop frost action; temperature does."),
            C("There is no water in the cracks.", why="The region is humid, so water is plentiful."),
            C("The temperature seldom falls to freezing point.", correct=True),
            C("Plants cover all the rock.", why="Plant cover is not the main reason."),
        ], steps=[S("Condition needed", text="Freeze-thaw needs water to freeze and expand in cracks. That needs temperatures below 0 degrees Celsius, which hardly happen in tropical lowlands.")],
           concept="Freeze-thaw and climate", skill="Reasoning", hint="What temperature does water need to reach to freeze?"),
        MC("A bare granite dome in a hot dry area shows curved sheets peeling from its surface. The most likely cause is", [
            C("rapid chemical weathering by heavy rain", why="The area is dry, so chemical weathering is weak."),
            C("deposition by a river", why="Deposition builds landforms; it does not peel rock."),
            C("roots of large trees", why="A bare dome in a dry area has few or no trees."),
            C("heating by day and cooling by night", correct=True),
        ], steps=[S("Match evidence to process", text="Bare rock, a hot dry area and curved sheets point to exfoliation caused by daily temperature change.")],
           concept="Exfoliation", skill="Application", hint="Think of the climate: is water or temperature change the main agent?"),
        MC("Which feature of a forest area helps to explain why weathering is deep there?", [
            C("Bare rock in the sun", why="Bare rock is typical of dry lands and speeds only temperature-change weathering."),
            C("Very low rainfall", why="Low rainfall slows chemical weathering."),
            C("Heavy rain, high temperature and organic acids from plants", correct=True),
            C("Frequent frost at night", why="Frost is not common in tropical forest lowlands."),
        ], steps=[S("Combine the factors", text="Water, heat and acids from rotting leaves all speed chemical weathering, giving a deep regolith.")],
           concept="Weathering in the humid tropics", skill="Reasoning", hint="What does chemical weathering need most?"),
        MC("Two rocks lie side by side in the same forest. One weathers much faster. The best explanation is a difference in", [
            C("rock type", correct=True),
            C("latitude", why="Both rocks are at the same place, so latitude is the same."),
            C("rainfall", why="Both rocks are in the same forest, so rainfall is the same."),
            C("air temperature", why="Both rocks have the same climate."),
        ], steps=[S("Spot the only difference", text="Climate and vegetation are the same, so rock type (hardness, joints, minerals) must explain the difference.")],
           concept="Factors of weathering", skill="Reasoning", hint="Which factor is NOT the same for the two rocks?"),
    ]))

# ------------------------------------------------------------------ 2. Erosion, transportation and deposition
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Erosion, transportation and deposition: processes and methods",
    lesson="land-erosion-transportation-and-deposition",
    questions=[
        MC("The dropping of a load by a river when it loses energy is called", [
            C("erosion", why="Erosion is the wearing away of land."),
            C("transportation", why="Transportation is the carrying of the load."),
            C("weathering", why="Weathering breaks rock in place and needs no moving agent."),
            C("deposition", correct=True),
        ], steps=[S("Match", text="Deposition is the dropping of load when the agent loses energy.")],
           concept="Definition of deposition", skill="Recall", hint="Which stage comes last in the chain?"),
        MC("Which list contains only agents of erosion?", [
            C("Rivers, wind and waves", correct=True),
            C("Rivers, soil and rocks", why="Soil and rocks are materials, not agents."),
            C("Wind, rainfall and clay", why="Clay is a load, not an agent."),
            C("Waves, sand and cliffs", why="Sand and cliffs are not agents."),
        ], steps=[S("Agents move and carry", text="Rivers, wind and waves are the three agents named in the syllabus.")],
           concept="Agents of erosion", skill="Recall", hint="An agent is something that moves and carries material."),
        MC("The scraping of a river bed by stones carried in the water is", [
            C("hydraulic action", why="Hydraulic action is the force of the water alone."),
            C("attrition", why="Attrition wears the load, not the bed."),
            C("abrasion", correct=True),
            C("solution", why="Solution is dissolving of minerals."),
        ], steps=[S("Match", text="Abrasion (corrasion) is the wearing of the bed and banks by the load.")],
           concept="Abrasion", skill="Recall", hint="Think of sandpaper."),
        MC("Pebbles found far downstream are small and round mainly because of", [
            C("deposition", why="Deposition drops material; it does not make it round."),
            C("attrition", correct=True),
            C("suspension", why="Suspension is a way of carrying fine particles."),
            C("hydraulic action", why="Hydraulic action loosens material from banks; it does not round pebbles."),
        ], steps=[S("Reason", text="Stones knock against each other during transport (attrition) and become smaller and rounder.")],
           concept="Attrition", skill="Concept", hint="Which process wears the load itself?"),
        MC("The brown colour of a river in flood comes mainly from material carried by", [
            C("traction", why="Traction rolls large stones along the bed; they do not colour the water."),
            C("saltation", why="Saltation moves small stones along the bed."),
            C("suspension", correct=True),
            C("solution", why="Dissolved minerals cannot be seen and do not make water muddy."),
        ], steps=[S("Link colour to method", text="Fine clay and silt float in the water in suspension and make it look muddy.")],
           concept="Suspension", skill="Application", hint="Which load is so fine that it floats in the water?"),
        MC("A river carries a large boulder only during a flood. The boulder most likely moves by", [
            C("solution", why="A boulder cannot be dissolved and carried."),
            C("suspension", why="A boulder is too heavy to float in the water."),
            C("saltation", why="Saltation moves small stones; a boulder is too heavy to bounce."),
            C("traction", correct=True),
        ], steps=[S("Match size to method", text="The largest pieces are rolled or dragged along the bed. This is traction and needs a lot of energy.")],
           concept="Traction", skill="Application", hint="The heavier the load, the nearer the bed it travels."),
        MC("A river slows down as it enters a lake and its brown water clears. This is because the river", [
            C("deposits its load as it loses energy", correct=True),
            C("erodes the lake bed more strongly", why="A slow river has less energy, so erosion is weaker, not stronger."),
            C("begins to carry more load in solution", why="Solution does not depend on slowing down in this way and would not clear the water."),
            C("starts attrition of the pebbles", why="Attrition does not clear muddy water."),
        ], steps=[S("Energy and load", text="When a river slows, it cannot carry as much. The load is dropped and the water clears.")],
           concept="Causes of deposition", skill="Reasoning", hint="What happens to a river's energy when it slows?"),
        MC("Which statement correctly differentiates erosion from weathering?", [
            C("Erosion happens only in deserts.", why="Erosion happens everywhere there is a moving agent."),
            C("Erosion needs a moving agent that carries material away; weathering does not.", correct=True),
            C("Weathering needs a moving agent; erosion does not.", why="This is the wrong way round."),
            C("Erosion is chemical and weathering is physical.", why="Both weathering and erosion have physical and chemical processes; the difference is the moving agent."),
        ], steps=[S("Key difference", text="Weathering breaks rock in place. Erosion uses a moving agent such as a river, wind or waves to wear away and carry material.")],
           concept="Erosion and weathering compared", skill="Concept", hint="Which one needs something to carry the material away?"),
    ]))

# ------------------------------------------------------------------ 3. Rivers: erosional landforms
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="River courses and erosional landforms",
    lesson="land-rivers-erosional-landforms",
    questions=[
        MC("The place where a smaller stream joins a larger river is called a", [
            C("source", why="The source is where a river begins."),
            C("mouth", why="The mouth is where a river enters the sea or a lake."),
            C("confluence", correct=True),
            C("watershed", why="A watershed is the high ground between two river basins."),
        ], steps=[S("Match", text="A tributary joins the main river at a confluence.")],
           concept="Parts of a river", skill="Recall", hint="Think of two rivers flowing together."),
        MC("The main work of a river in its upper course is", [
            C("deposition of silt", why="Deposition is typical of the lower course."),
            C("vertical erosion", correct=True),
            C("building of a delta", why="Deltas form at the mouth."),
            C("formation of ox-bow lakes", why="Ox-bow lakes form in the middle and lower courses."),
        ], steps=[S("Upper course", text="The river is steep and has a stony load, so it cuts down into its bed.")],
           concept="Upper course processes", skill="Recall", hint="Which direction does the river cut when the slope is steep?"),
        MC("A narrow valley with steep sides, cut by a river in its upper course, is a", [
            C("flood plain", why="A flood plain is flat and wide, in the lower course."),
            C("delta", why="A delta is a depositional feature at the mouth."),
            C("V-shaped valley", correct=True),
            C("lagoon", why="A lagoon is a coastal water body."),
        ], steps=[S("Match", text="Vertical erosion produces a deep, narrow, V-shaped valley.")],
           concept="V-shaped valley", skill="Recall", hint="Think of the letter whose shape the valley has."),
        MC("Interlocking spurs are formed because", [
            C("the river winds around ridges that it is too weak to cut through", correct=True),
            C("the river deposits silt on both banks", why="Deposition does not make spurs; it makes flood plains and levees."),
            C("waves cut notches into a cliff", why="This describes coastal erosion."),
            C("the wind blows sand into ridges", why="This describes dunes."),
        ], steps=[S("Explain", text="In the upper course the river lacks energy to erode sideways, so it flows around spurs.")],
           concept="Interlocking spurs", skill="Concept", hint="What does a weak river do when it meets a ridge?"),
        MC("Which condition is most important for the formation of a waterfall?", [
            C("A very gentle slope", why="A waterfall needs a sudden step, not a gentle slope."),
            C("A layer of hard rock over softer rock", correct=True),
            C("A wide flood plain", why="A flood plain is flat and has no steps."),
            C("A large amount of silt", why="Silt is deposited by slow rivers; it does not make steps."),
        ], steps=[S("Why", text="The soft rock wears away faster, leaving an overhang of hard rock and a vertical drop.")],
           concept="Waterfall formation", skill="Concept", hint="What does the river wear away faster: hard or soft rock?"),
        MC("A deep, narrow valley left behind by a waterfall that has moved upstream is a", [
            C("gorge", correct=True),
            C("meander", why="A meander is a bend in the river."),
            C("levee", why="A levee is a bank of silt."),
            C("tor", why="A tor is a weathering landform."),
        ], steps=[S("Result of retreat", text="As the fall retreats it leaves a steep-sided gorge downstream.")],
           concept="Gorge", skill="Concept", hint="What does a retreating fall leave behind it?"),
        MC("A river flows fast over a rough bed made of alternating bands of hard and soft rock, forming many small white-water steps. This feature is", [
            C("a gorge", why="A gorge is a deep valley, not a series of steps."),
            C("a delta", why="A delta is at the river mouth."),
            C("a waterfall", why="A waterfall is a single large drop, but here the steps are many and small."),
            C("rapids", correct=True),
        ], steps=[S("Decide", text="Many small steps over a rough bed are rapids. One large vertical drop is a waterfall.")],
           concept="Rapids", skill="Application", hint="Count the drops: one big or many small?"),
        MC("A field team finds a steep, narrow valley with a fast, stony stream, interlocking spurs and a small waterfall. The stream is probably in its", [
            C("lower course", why="The lower course is flat and wide with deposition."),
            C("middle course", why="The middle course has meanders and a wider valley."),
            C("delta", why="A delta is at the mouth."),
            C("upper course", correct=True),
        ], steps=[S("Collect the clues", text="Steep slope, V-shape, interlocking spurs and waterfalls all belong to the upper course.")],
           concept="Identifying river courses", skill="Interpretation", hint="Which course has the steepest gradient?"),
    ]))

# ------------------------------------------------------------------ 4. Rivers: depositional landforms
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Meanders, flood plains, deltas and alluvial fans",
    lesson="land-rivers-depositional-landforms",
    questions=[
        MC("A large bend in the middle or lower course of a river is a", [
            C("meander", correct=True),
            C("gorge", why="A gorge is a deep narrow valley."),
            C("waterfall", why="A waterfall is a vertical drop."),
            C("tor", why="A tor is a weathering landform made of blocks of rock."),
        ], steps=[S("Match", text="A meander is a bend in a river.")],
           concept="Meander", skill="Recall", hint="Think of the word 'bend'."),
        MC("The curved lake left when a river cuts off a meander is called an", [
            C("alluvial lake", why="This is not a standard landform name."),
            C("ox-bow lake", correct=True),
            C("delta lake", why="A delta is at the river mouth and is not a cut-off bend."),
            C("lagoon", why="A lagoon is separated from the sea by a spit or bar."),
        ], steps=[S("Match", text="The abandoned bend is an ox-bow lake.")],
           concept="Ox-bow lake", skill="Recall", hint="It is named after a U-shaped part of a yoke."),
        MC("The fine, fertile silt left on a flood plain after a flood is called", [
            C("regolith", why="Regolith is weathered rock and soil formed in place."),
            C("scree", why="Scree is loose rock at the foot of a cliff."),
            C("alluvium", correct=True),
            C("laterite", why="Laterite is a hard iron-rich soil layer, not river silt."),
        ], steps=[S("Match", text="River-deposited material is alluvium.")],
           concept="Flood plain deposits", skill="Recall", hint="Alluvial fans are made of the same kind of material."),
        MC("The steep bank on the outside of a meander is known as a", [
            C("slip-off slope", why="This is the gentle bank on the inside of the bend."),
            C("levee", why="A levee is a raised bank made by flood deposits."),
            C("river cliff", correct=True),
            C("distributary", why="A distributary is a channel in a delta."),
        ], steps=[S("Where the water is fastest", text="Fast water erodes the outside of the bend and undercuts it to form a river cliff.")],
           concept="River cliff", skill="Concept", hint="Which side of the bend has the fastest water?"),
        MC("Natural levees consist mainly of coarse material because", [
            C("the river carries only coarse material", why="Rivers carry coarse and fine material together."),
            C("the heaviest material is dropped first when floodwater slows at the banks", correct=True),
            C("levees are built by waves", why="Waves have no role in river levees."),
            C("wind blows sand to the river banks", why="Levees are made by water, not wind."),
        ], steps=[S("Order of deposition", text="Floodwater slows suddenly at the bank. Heavy, coarse material is dropped first, near the channel. Fine silt is carried further.")],
           concept="Formation of levees", skill="Concept", hint="Which particles settle first when water slows?"),
        MC("Which condition does NOT favour the formation of a large delta?", [
            C("A river with a large load", why="This favours a delta."),
            C("Shallow and sheltered water at the mouth", why="This favours a delta."),
            C("Strong waves and tides that remove the load", correct=True),
            C("A river that splits into distributaries", why="Splitting channels are part of how a delta grows."),
        ], steps=[S("Spot the unfavourable condition", text="Strong waves and tides would sweep the silt away, so deposits could not build up.")],
           concept="Conditions for a delta", skill="Reasoning", hint="What must the sea NOT do to the river's load?"),
        MC("A mountain stream emerges onto a flat dry plain and drops its load in a fan shape, boulders first. This is", [
            C("a levee", why="A levee is a long bank beside a river channel."),
            C("a delta", why="A delta forms where a river enters a sea or lake."),
            C("a meander", why="A meander is a bend in a river."),
            C("an alluvial fan", correct=True),
        ], steps=[S("Clues", text="Mountain front, sudden change to a flat plain and a fan-shaped deposit with coarse material at the apex point to an alluvial fan.")],
           concept="Alluvial fan", skill="Application", hint="Where does the stream suddenly lose its steep slope?"),
        MC("The inside of a meander bend is gently sloping and covered with sand. The most likely reason is that", [
            C("the water there is slow and deposits its load", correct=True),
            C("the water there is fast and erodes the bank", why="Fast erosion happens on the outside of the bend."),
            C("a waterfall has retreated there", why="Waterfalls are features of the upper course."),
            C("waves have built a beach", why="This is a river bend, not a coast."),
        ], steps=[S("Link speed and deposition", text="On the inside of a bend the water is slow, so it drops sand and gravel to build a slip-off slope.")],
           concept="Slip-off slope", skill="Reasoning", hint="Is the inside of a bend faster or slower than the outside?"),
    ]))

# ------------------------------------------------------------------ 5. Wind and water in deserts
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Desert landforms made by wind and water",
    lesson="land-wind-and-water-in-deserts",
    questions=[
        MC("The blowing away of loose, fine particles by the wind is called", [
            C("abrasion", why="Abrasion is the wearing of rock by wind-blown sand."),
            C("attrition", why="Attrition is the wearing down of the load itself."),
            C("deflation", correct=True),
            C("saltation", why="Saltation is a way sand grains are transported."),
        ], steps=[S("Match", text="Deflation lifts and removes loose material.")],
           concept="Deflation", skill="Recall", hint="It lowers the land by blowing material away."),
        MC("A crescent-shaped sand dune with its horns pointing downwind is a", [
            C("seif", why="A seif is a long ridge along the wind direction."),
            C("barchan", correct=True),
            C("wadi", why="A wadi is a dry river valley."),
            C("playa", why="A playa is a flat dry basin."),
        ], steps=[S("Match", text="Barchans are crescent dunes with horns pointing downwind.")],
           concept="Barchan", skill="Recall", hint="Think of a crescent moon."),
        MC("A dry valley in a desert that carries water only after rain is a", [
            C("wadi", correct=True),
            C("salt pan", why="A salt pan is a salty crust in a basin."),
            C("inselberg", why="An inselberg is an isolated hill."),
            C("playa", why="A playa is a flat basin, not a valley."),
        ], steps=[S("Match", text="A wadi is a channel that is dry most of the time and floods briefly.")],
           concept="Wadi", skill="Recall", hint="Think of a river that is nearly always dry."),
        MC("An isolated, steep-sided hill of hard rock on a flat plain is called a", [
            C("tor", why="A tor is a pile of rounded blocks formed by weathering, not a large hill."),
            C("barchan", why="A barchan is a dune."),
            C("inselberg", correct=True),
            C("levee", why="A levee is a river-bank embankment."),
        ], steps=[S("Match", text="The softer land around is worn away and the hard rock remains as an inselberg.")],
           concept="Inselberg", skill="Recall", hint="The name means 'island mountain'."),
        MC("Why is the base of a mushroom rock narrower than its top?", [
            C("Wind-blown sand is carried close to the ground and wears the base most", correct=True),
            C("Rain washes away the base", why="Deserts have very little rain, and rain does not make this shape."),
            C("The top is made of softer rock", why="The shape is explained by where the sand strikes, not by softer rock at the top."),
            C("Salt crystals grow at the top", why="Salt crystals widen cracks but do not make this shape."),
        ], steps=[S("Explain", text="Sand grains are heavy and bounce near the ground. Abrasion is strongest at the base, leaving a wide top.")],
           concept="Mushroom rock", skill="Concept", hint="Where do the sand grains hit the rock most?"),
        MC("Which statement about a barchan is correct?", [
            C("Its steep slip face faces the wind.", why="The slip face is on the sheltered (downwind) side."),
            C("Its gentle slope faces the wind.", correct=True),
            C("It is a long ridge parallel to the wind.", why="That describes a seif dune."),
            C("Its horns point into the wind.", why="The horns are carried ahead and point downwind."),
        ], steps=[S("Profile of a dune", text="Sand is blown up the gentle windward slope and falls down the steep slip face on the far side.")],
           concept="Barchan structure", skill="Concept", hint="Which side is the sand blown up?"),
        MC("A desert basin has no outlet. After heavy rain it fills with water. In the dry season the water evaporates and leaves a white crust. The crust is", [
            C("alluvium", why="Alluvium is river silt, not a salt crust."),
            C("regolith", why="Regolith is weathered rock and soil."),
            C("a salt pan", correct=True),
            C("loess", why="Loess is wind-blown silt and is not described here."),
        ], steps=[S("Follow the process", text="Rain fills the playa. Evaporation leaves the dissolved salt behind as a crust, called a salt pan.")],
           concept="Playa and salt pan", skill="Application", hint="What stays behind when salty water evaporates?"),
        MC("A hunter in a desert says, 'The wadi was empty at midday but full of fast, muddy water an hour after a storm in the hills.' This best shows that", [
            C("deserts never have flowing water", why="This is the opposite of the observation."),
            C("flash floods give deserts short but powerful water action", correct=True),
            C("wind is the only agent in deserts", why="The observation shows water at work."),
            C("salt pans form in wadis", why="Salt pans form in basins where lakes evaporate, not in the wadi channel."),
        ], steps=[S("Interpret", text="Water is rare, but a storm on bare ground makes a sudden flash flood that is strong enough to carry a lot of material.")],
           concept="Desert flash floods", skill="Interpretation", hint="Compare the wadi before and after the storm."),
    ]))

# ------------------------------------------------------------------ 6. Waves and coastal landforms
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Wave erosion and coastal landforms",
    lesson="land-waves-and-coastal-landforms",
    questions=[
        MC("The water that runs back down a beach after a wave breaks is called the", [
            C("swash", why="Swash is the water that runs up the beach."),
            C("fetch", why="Fetch is the length of open water the wind blows over."),
            C("backwash", correct=True),
            C("drift", why="Drift is the movement of the load along the coast."),
        ], steps=[S("Match", text="Swash goes up the beach. Backwash returns down it.")],
           concept="Swash and backwash", skill="Recall", hint="It goes back down the slope."),
        MC("The gently sloping rock shelf at the foot of a retreating cliff is a", [
            C("wave-cut platform", correct=True),
            C("spit", why="A spit is a ridge of deposited sand."),
            C("stack", why="A stack is an isolated pillar of rock."),
            C("lagoon", why="A lagoon is a body of water behind a bar."),
        ], steps=[S("Match", text="As the cliff retreats, the cut-back leaves a platform.")],
           concept="Wave-cut platform", skill="Recall", hint="It is cut by waves."),
        MC("A pillar of rock standing separately in the sea near a cliff is a", [
            C("tombolo", why="A tombolo is a bar of sand joining an island to the land."),
            C("bar", why="A bar is a ridge of sand across a bay."),
            C("cave", why="A cave is a hollow in a cliff or headland."),
            C("stack", correct=True),
        ], steps=[S("Match", text="When the arch roof collapses, an isolated pillar remains: the stack.")],
           concept="Stack", skill="Recall", hint="It was once joined to the headland."),
        MC("Which is the correct order of the features produced on a headland?", [
            C("Cave, crack, arch, stack", why="A crack must exist before it becomes a cave."),
            C("Crack, arch, cave, stack", why="A cave forms before it is cut through to make an arch."),
            C("Crack, cave, arch, stack", correct=True),
            C("Stack, arch, cave, crack", why="This is the reverse order."),
        ], steps=[S("Follow the erosion", text="Waves widen a crack into a cave, break through to make an arch, and the arch roof collapses to leave a stack.")],
           concept="Headland features", skill="Concept", hint="Start with the smallest feature."),
        MC("Longshore drift moves sand along a beach because", [
            C("swash goes up at an angle and backwash goes straight down", correct=True),
            C("tides push sand along the cliff", why="Tides are not the cause; waves hitting at an angle are."),
            C("rivers carry sand along the coast", why="Rivers bring sand to the sea but do not move it along the shore."),
            C("wind blows sand across the sea", why="Wind makes the waves, but the drift itself is made by swash and backwash."),
        ], steps=[S("Zigzag", text="Swash carries material up at the angle of the waves. Backwash returns it straight down. Repeated, this moves the load along the coast.")],
           concept="Longshore drift", skill="Concept", hint="Compare the paths of swash and backwash."),
        MC("A spit grows where", [
            C("a cliff is undercut by waves", why="Undercutting makes a notch and a platform, not a spit."),
            C("the coast changes direction and longshore drift continues straight on", correct=True),
            C("a river forms a delta", why="A delta is made by a river, not by longshore drift."),
            C("a headland has a crack", why="A crack in a headland starts the sequence to a cave, arch and stack."),
        ], steps=[S("Explain", text="At a bend the drift keeps moving the load straight on and drops it in calmer water, building a ridge.")],
           concept="Spit formation", skill="Reasoning", hint="What does the drift do when the coast turns away?"),
        MC("A beach of dark sand is found at the foot of a volcano on the coast. The dark colour is best explained by", [
            C("coral fragments", why="Coral gives pale sand."),
            C("volcanic rock broken down into sand", correct=True),
            C("salt left by evaporation", why="Salt is white and does not make sand dark."),
            C("mangrove roots", why="Mangroves live in muddy water and do not make the sand dark."),
        ], steps=[S("Link material to source", text="Beach sand comes from the rock that is eroded nearby. Dark volcanic rock gives dark sand, as at Limbe.")],
           concept="Source of beach sand", skill="Application", hint="Where does beach sand come from?"),
        MC("The sketch of a cliff shows a deep notch at the foot, with a wide rock platform at low tide. What will happen to this cliff?", [
            C("It will grow seaward", why="Cliffs do not grow seaward when a notch is being cut."),
            C("It will turn into a spit", why="A spit is a sand ridge, not a cliff."),
            C("It will slowly retreat inland as the notch collapses", correct=True),
            C("It will become a delta", why="A delta forms at a river mouth."),
        ], steps=[S("Predict", text="A notch weakens the cliff above. The rock collapses, the cliff retreats and the platform widens.")],
           concept="Cliff retreat", skill="Interpretation", hint="What happens to the rock above a deep notch?"),
    ]))

# ------------------------------------------------------------------ 7. Drainage patterns
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Recognising dendritic, trellised and radial drainage",
    lesson="land-drainage-patterns",
    questions=[
        MC("A drainage pattern is", [
            C("the arrangement of a river and its tributaries on a map", correct=True),
            C("the speed at which a river flows", why="This describes river velocity."),
            C("the amount of water carried by a river", why="This describes river discharge."),
            C("the slope of a river valley", why="This describes the gradient."),
        ], steps=[S("Recall", text="A drainage pattern is the shape formed by a river and its tributaries.")],
           concept="Definition of drainage pattern", skill="Recall", hint="It is something you can see from above."),
        MC("The word 'dendritic' means", [
            C("like the spokes of a wheel", why="This describes a radial pattern."),
            C("like a garden trellis", why="This describes a trellised pattern."),
            C("like a staircase", why="This does not describe any of the three patterns."),
            C("like a tree", correct=True),
        ], steps=[S("Meaning", text="Dendritic comes from the Greek word for tree.")],
           concept="Dendritic pattern", skill="Recall", hint="Think of a trunk and branches."),
        MC("Which pattern has rivers that flow outwards from a central high point?", [
            C("Dendritic", why="Dendritic rivers join to form a trunk, they do not spread from a point."),
            C("Trellised", why="Trellised rivers run in parallel lines."),
            C("Radial", correct=True),
            C("Parallel", why="This is not one of the three syllabus patterns."),
        ], steps=[S("Match", text="Radial means spokes of a wheel, from a centre.")],
           concept="Radial pattern", skill="Recall", hint="Think of the spokes of a bicycle wheel."),
        MC("Which type of rock structure best produces a trellised drainage pattern?", [
            C("The same rock over a wide area", why="This produces dendritic drainage."),
            C("Parallel bands of hard and soft rock", correct=True),
            C("A volcanic cone", why="This produces radial drainage."),
            C("A flat plain of sand", why="No guiding structure exists, so dendritic or no clear pattern forms."),
        ], steps=[S("Reason", text="Rivers cut valleys in soft rock and leave hard rock as ridges, so the rivers and their tributaries follow the bands at right angles.")],
           concept="Conditions for trellised drainage", skill="Concept", hint="Which structure has long parallel ridges and valleys?"),
        MC("Tributaries that join the main river at acute angles in a branching form show", [
            C("a radial pattern", why="Radial streams start from a centre and do not join to make a trunk."),
            C("no pattern", why="A pattern is clearly visible."),
            C("a trellised pattern", why="Trellised tributaries join at right angles."),
            C("a dendritic pattern", correct=True),
        ], steps=[S("Use the angle clue", text="Acute angles in a tree-like form mean dendritic. Right angles in a grid mean trellised.")],
           concept="Recognising dendritic drainage", skill="Concept", hint="Look at the angle where tributaries join."),
        MC("Look at Map A. Which pattern do the rivers show?", [
            C("Dendritic", why="Dendritic rivers join to form a single trunk; here they spread out."),
            C("Trellised", why="Trellised rivers run in parallel lines with right-angle joins."),
            C("Radial, around a dome", correct=True),
            C("None of the three", why="A clear pattern is visible: rivers spread from a central high point."),
        ], steps=[S("Read the map", text="The contours are circles with the highest value (500) in the centre, and the streams flow outwards in all directions. This is radial drainage around a hill or dome.")],
           concept="Interpreting a radial pattern", skill="Interpretation", hint="Where do the streams start, and which way do they flow?",
           diagram="f5g-land-quiz-map-a.svg", diagram_alt="Fictitious map of Bakoko district with circular contours 200 to 500 and streams flowing outwards in all directions from the centre"),
        MC("Look at Map B. The rivers run in long parallel lines and tributaries join them at right angles. The likely reason is", [
            C("bands of hard and soft rock", correct=True),
            C("uniform rock and a gentle slope", why="This gives a tree-like dendritic pattern."),
            C("a volcanic cone in the centre", why="A volcano gives radial drainage, with streams spreading from a centre."),
            C("a river delta", why="A delta is at the mouth and has distributaries, not parallel rivers."),
        ], steps=[S("Read the map", text="Parallel main rivers with right-angle tributaries form a trellised pattern. The reason is alternating bands of hard and soft rock.")],
           concept="Interpreting a trellised pattern", skill="Interpretation", hint="Which pattern has right-angle junctions?",
           diagram="f5g-land-quiz-map-b.svg", diagram_alt="Fictitious map of Njoke district with two long parallel rivers and short tributaries joining them at right angles"),
        MC("Look at Map C. Which statement about the pattern is correct?", [
            C("It is trellised because the rivers are straight.", why="Straightness is not the clue; the angle of the junctions and the tree-like form are."),
            C("It is dendritic, so the rock is likely to be similar over the area.", correct=True),
            C("It is radial because rivers flow towards the sea.", why="Radial streams spread out from a centre; here they join a trunk."),
            C("It is trellised because it has many tributaries.", why="Having many tributaries does not make a pattern trellised; right angles do."),
        ], steps=[S("Read the map", text="Many branches join the main river at acute angles in a tree-like form. This is dendritic, which forms on uniform rock with a gentle slope.")],
           concept="Interpreting a dendritic pattern", skill="Interpretation", hint="Does it look like a tree or a grid?",
           diagram="f5g-land-quiz-map-c.svg", diagram_alt="Fictitious map of Mbanga district with a main river and many branching tributaries joining at acute angles like a tree"),
    ]))

# ------------------------------------------------------------------ 8. Denudational hazards
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Landslides, rockfall, mudflow and gas explosions",
    lesson="land-denudational-hazards",
    questions=[
        MC("The rapid downhill movement of a mass of soil and rock on a slope is a", [
            C("landslide", correct=True),
            C("deflation", why="Deflation is the blowing away of loose particles by wind."),
            C("longshore drift", why="Longshore drift is the movement of sand along a coast."),
            C("weathering", why="Weathering is the breaking down of rock in place."),
        ], steps=[S("Match", text="A landslide is a mass of soil and rock sliding downhill.")],
           concept="Definition of landslide", skill="Recall", hint="Think of a slope giving way."),
        MC("The fall of single rocks from a steep cliff face is called", [
            C("mudflow", why="Mudflow is the flow of water-soaked soil."),
            C("rockfall", correct=True),
            C("exfoliation", why="Exfoliation is the peeling of sheets from a rock surface by heat and cold."),
            C("abrasion", why="Abrasion is wearing by a moving load."),
        ], steps=[S("Match", text="Rockfall is the fall of blocks from a rock face.")],
           concept="Rockfall", skill="Recall", hint="The name says what falls."),
        MC("Natural gas is mainly", [
            C("carbon dioxide", why="Carbon dioxide does not burn."),
            C("oxygen", why="Oxygen helps fire but is not natural gas."),
            C("nitrogen", why="Nitrogen does not burn."),
            C("methane", correct=True),
        ], steps=[S("Recall", text="Natural gas is mainly methane, which burns easily.")],
           concept="Natural gas", skill="Recall", hint="It is the gas that burns."),
        MC("Which is a human cause of landslides?", [
            C("Heavy rainfall", why="Rainfall is a natural cause."),
            C("Removing forest from steep slopes", correct=True),
            C("A steep natural slope", why="This is a natural cause."),
            C("An earthquake", why="This is a natural cause."),
        ], steps=[S("Sort the causes", text="Rain, natural steep slopes and earthquakes are natural. Clearing forest is done by people.")],
           concept="Causes of landslides", skill="Concept", hint="Which cause is done by people?"),
        MC("Why do roots help to prevent landslides?", [
            C("They add weight to the slope", why="Adding weight makes slopes less stable, not more."),
            C("They bind the soil and hold it in place", correct=True),
            C("They make the rain fall faster", why="Roots do not change the rain."),
            C("They dissolve the rock below", why="Roots do not protect slopes by dissolving rock."),
        ], steps=[S("Role of roots", text="Roots hold soil particles together, and the plant cover slows the rain.")],
           concept="Prevention of landslides", skill="Concept", hint="What do roots do to the soil?"),
        MC("A hillside suddenly slides during a long period of heavy rain. The best explanation is that", [
            C("the rain made the soil heavy and slippery over the solid rock beneath", correct=True),
            C("the rain dissolved the entire hillside", why="Rain does not dissolve a whole hill; it saturates the regolith."),
            C("wind blew the soil away", why="The movement is downhill under gravity, not by wind."),
            C("waves cut the foot of the hill", why="This describes coastal cliffs, not an inland hillside."),
        ], steps=[S("Explain", text="Rain soaks the loose regolith, adding weight and reducing friction, so it slides over the impermeable rock.")],
           concept="Rain and landslides", skill="Reasoning", hint="What does water do to loose soil?"),
        MC("Which of these is an example of mitigation rather than prevention?", [
            C("Planting trees on a bare slope", why="This helps to prevent the hazard from happening."),
            C("Building terraces on a slope", why="This helps to prevent the hazard from happening."),
            C("Digging drains along the road", why="This helps to prevent the hazard by removing water."),
            C("Warning people and moving them to safe places", correct=True),
        ], steps=[S("Decide", text="Mitigation reduces harm once the hazard threatens. A warning and evacuation protect people but do not stop the landslide.")],
           concept="Prevention and mitigation", skill="Reasoning", hint="Which action does not stop the hazard but protects people?"),
        MC("A village below a steep, bare hillside in the West Region plans to protect itself from landslides. Which package is best?", [
            C("Plant trees, build terraces and drains and keep houses away from the slope foot", correct=True),
            C("Cut more trees for building space", why="Removing trees makes landslides more likely."),
            C("Dig a deep hole at the foot of the slope for new houses", why="Cutting into the foot of a slope makes it less stable."),
            C("Block all drains to keep the water on the hill", why="Water trapped in the soil makes the slope slide."),
        ], steps=[S("Match measures to the problem", text="Roots hold the soil, terraces and drains reduce the water, and keeping houses away from the foot lowers the risk to people.")],
           concept="Planning slope protection", skill="Application", hint="Which measures hold soil and remove water?"),
    ]))
