"""Practice sets for Form 5 Geography: Map interpretation (one per lesson, 8 questions each).

All figures show KUMA DISTRICT, a fictitious place drawn for teaching.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Map Reading and Interpretation"
TOPIC = "Map interpretation"

SETS = []

REL = "f5g-mapint-kuma-relief.svg"
REL_ALT = ("Relief map of Kuma District with contours at 50 metre interval, spot heights, two trig stations, a bench mark and lettered points A, D, E, F and G")
CQ = "f5g-mapint-contour-quiz.svg"
CQ_ALT = "Six contour patterns lettered A to F with heights in metres"
DRN = "f5g-mapint-kuma-drainage.svg"
DRN_ALT = ("Drainage map of Kuma District with the R. Kuma, four tributaries, a seasonal stream, Lake Bimbi, a swamp and lettered points P, Q, R, S and V")
MAPQ = "f5g-mapint-kuma-map-q.svg"
MAPQ_ALT = ("Topographic map of Kuma District with forest, plantation, farmland, grassland, swamp, roads, railway and settlements, and lettered points P, Q, R and S")
MAP = "f5g-mapint-kuma-map.svg"
MAP_ALT = ("Topographic map of Kuma District with contours, rivers, vegetation, roads, a railway, the market town of Tabeng and the villages Njomi, Mbolo, Ekum, Bimbi and Fundi")

# ------------------------------------------------------------------ 1. Relief and contour lines
SETS.append(practice_set(
    module=MODULE, topic=TOPIC, title="Relief and contour lines", lesson="mapint-relief-and-contour-lines",
    questions=[
        MC("A contour line on a map joins places that have the same:", [
            C("distance from the sea", why="Distance from the sea is not what contours measure. They measure height."),
            C("slope", why="Two places on one contour can have different slopes. A contour joins places of equal height."),
            C("height above sea level", correct=True),
            C("kind of vegetation", why="Vegetation is shown by other signs, not by contours."),
        ], steps=[S("Recall the definition", text="A contour line joins points of equal height above sea level.")],
            concept="Definition of a contour line", skill="Recall",
            hint="Think about what the numbers on a contour line tell you.",
            feedback="Every point on one contour is at the same height above sea level."),
        MC("A triangle with a dot inside it, with a number beside it, is the sign for a:", [
            C("trigonometrical station", correct=True),
            C("bench mark", why="A bench mark is shown by a cross with the letters BM."),
            C("spot height", why="A spot height is a plain dot with a number."),
            C("village", why="Villages are shown by small black squares."),
        ], steps=[S("Recall the signs", text="A trig station is a triangle with a dot. A bench mark is a cross marked BM. A spot height is a dot.")],
            concept="Height signs on maps", skill="Recall",
            hint="Which of the height signs has three sides?",
            feedback="The triangle with a dot is a trigonometrical (trig) station, a fixed survey point."),
        NUM("In the figure, the thick contour lines are labelled 400 and 500 metres, and one thin line lies between them. "
            "What is the contour interval, in metres?", 50, unit="m",
            steps=[S("Find the height difference", math=r"500 - 400 = 100", text="The two thick lines are 100 metres apart."),
                   S("Share it between the gaps", math=r"100 \div 2 = 50", text="There are two gaps (400 to 450, and 450 to 500), so the interval is 50 metres.")],
            concept="Contour interval", skill="Calculation",
            hint="Count the gaps between the 400 and the 500 metre lines.", diagram=REL, diagram_alt=REL_ALT,
            feedback="Interval is the height difference between neighbouring contours: 50 metres."),
        MC("On a contour map, contour lines that are far apart show:", [
            C("a steep slope", why="A steep slope has close contours, because the land rises quickly."),
            C("a gentle slope", correct=True),
            C("a waterfall", why="A waterfall would show contours almost touching, not far apart."),
            C("the top of a hill", why="A hilltop is a small closed ring, not wide spacing."),
        ], steps=[S("Link spacing to slope", text="Wide spacing means the land rises slowly over a long distance, so the slope is gentle.")],
            concept="Spacing and slope", skill="Concept",
            hint="Think about how far you must walk to climb 50 metres.",
            feedback="Wide contours mean a gentle slope. Close contours mean a steep slope."),
        MC("In the figure, which lettered pattern shows a valley?", [
            C("Pattern A", why="Pattern A has the V pointing down towards lower heights (the numbers rise on each side). That is a spur, not a valley."),
            C("Pattern B", why="Pattern B shows two hills with a dip between them, which is a saddle."),
            C("Pattern C", why="Pattern C is a set of closed rings with the highest number in the middle, which is a hill."),
            C("Pattern D", correct=True),
        ], steps=[S("Read the numbers", text="In pattern D the contours bend into a V and the V points towards higher numbers (350 is higher than 150). A V pointing uphill is a valley.")],
            concept="Valley contour pattern", skill="Interpretation",
            hint="Check which way the point of each V faces, and compare it with the heights.",
            diagram=CQ, diagram_alt=CQ_ALT,
            feedback="A V that points uphill, towards the higher numbers, is a valley."),
        MC("In the figure, which lettered pattern shows a spur?", [
            C("Pattern F", why="Pattern F is a set of long narrow closed rings, which is a ridge."),
            C("Pattern D", why="Pattern D is the valley, because its V points uphill."),
            C("Pattern A", correct=True),
            C("Pattern E", why="Pattern E has very close lines on one side of a band, which is an escarpment."),
        ], steps=[S("Read the numbers", text="In pattern A the V bends point downhill, towards the lower numbers (250 is lower than 400). That is a spur, high ground that sticks out from a hill.")],
            concept="Spur contour pattern", skill="Interpretation",
            hint="A spur is the opposite of a valley. Which way does the V point?",
            diagram=CQ, diagram_alt=CQ_ALT,
            feedback="A V pointing downhill is a spur."),
        NUM("The trig station on Kuma Hill is 706 metres high and the bench mark near Tabeng is 330 metres. "
            "How many metres higher is the trig station?", 376, unit="m",
            steps=[S("Subtract the lower height", math=r"706 - 330 = 376")],
            concept="Height difference between two points", skill="Calculation",
            hint="Find the two heights on the map, then subtract.", diagram=REL, diagram_alt=REL_ALT,
            feedback="706 minus 330 is 376 metres."),
        MC("In the figure, at which letter is the slope steepest?", [
            C("D", correct=True),
            C("E", why="E is on low flat land with almost no contours, so the slope there is the gentlest."),
            C("G", why="G is the flat top of the plateau, with no contours."),
            C("A", why="A is a saddle. The contours around it are fairly wide apart."),
        ], steps=[S("Compare contour spacing", text="At D the contours (400, 450 and 500 metres) are crowded very close together on the edge of the plateau. "
                    "The closest contours show the steepest slope.")],
            concept="Comparing slopes", skill="Reasoning",
            hint="Where are the contour lines most crowded?",
            diagram=REL, diagram_alt=REL_ALT,
            feedback="Close contours mean a steep slope. At D the escarpment contours are crowded."),
    ]))

# ------------------------------------------------------------------ 2. Drainage on maps
SETS.append(practice_set(
    module=MODULE, topic=TOPIC, title="Drainage on maps", lesson="mapint-drainage-on-maps",
    questions=[
        MC("The place where a river begins is called its:", [
            C("mouth", why="The mouth is where a river ends."),
            C("source", correct=True),
            C("confluence", why="A confluence is where two streams join."),
            C("tributary", why="A tributary is a smaller stream that joins a larger one."),
        ], steps=[S("Recall the term", text="A river begins at its source and ends at its mouth.")],
            concept="Source of a river", skill="Recall",
            hint="Which word means the start of a river?", feedback="The source is where a river begins."),
        MC("The place where two rivers join is called a:", [
            C("source", why="A source is where a river begins."),
            C("delta", why="A delta is a landform at a river mouth, not a place where two streams meet."),
            C("lake", why="A lake is an area of water, not a joining point."),
            C("confluence", correct=True),
        ], steps=[S("Recall the term", text="A confluence is the meeting point of two streams.")],
            concept="Confluence", skill="Recall",
            hint="The word begins with 'con', as in 'come together'.", feedback="A confluence is where two streams join."),
        MC("In the figure, which letter marks the source of the R. Kuma?", [
            C("Q", correct=True),
            C("P", why="P is a confluence, where the R. Ewe joins the R. Kuma."),
            C("R", why="R is where the river meets Lake Bimbi, its mouth."),
            C("V", why="V is in the swamp, near the end of the river."),
        ], steps=[S("Find the start of the river", text="The R. Kuma begins at Q, in the north, at about 480 metres. It is the highest end of the river.")],
            concept="Source on a map", skill="Interpretation",
            hint="Which end of the river is highest?", diagram=DRN, diagram_alt=DRN_ALT,
            feedback="Q is at the highest end of the river. That is its source."),
        MC("Look at the figure. The R. Kuma has its source at about 480 metres and its mouth in Lake Bimbi at 300 metres. The river flows generally towards the:", [
            C("north-west", why="The source is in the north and the lake is in the south-east, so the river does not flow north-west."),
            C("north-east", why="The lake is south of the source, so the flow cannot be north-east."),
            C("south-east", correct=True),
            C("south-west", why="The lake is east of the source as well as south, so the flow is not south-west."),
        ], steps=[S("Compare the heights", text="The river flows downhill from 480 metres to 300 metres."),
                  S("Find the position of the mouth", text="Lake Bimbi lies to the south and east of the source, so the flow is south-east.")],
            concept="Direction of flow", skill="Reasoning",
            hint="Rivers flow downhill. Where is the low end?", diagram=DRN, diagram_alt=DRN_ALT,
            feedback="The flow is from the high source in the north towards the lake in the south-east."),
        NUM("A river has its source at 480 metres above sea level and its mouth in a lake at 300 metres. "
            "By how many metres does the river fall from source to mouth?", 180, unit="m",
            steps=[S("Subtract", math=r"480 - 300 = 180")],
            concept="Height drop of a river", skill="Calculation",
            hint="Subtract the lower height from the higher one.",
            feedback="480 minus 300 is 180 metres."),
        MC("In the figure, the R. Kuma and its tributaries branch like the limbs of a tree. This drainage pattern is:", [
            C("radial", why="In a radial pattern streams flow outwards from one high point, not branch like a tree."),
            C("dendritic", correct=True),
            C("trellised", why="A trellised pattern has parallel streams with right-angle joins."),
            C("seasonal", why="Seasonal describes a stream that dries up. It is not a pattern."),
        ], steps=[S("Name the pattern", text="Tributaries join the main river at acute angles, like the branches of a tree. That is a dendritic pattern.")],
            concept="Dendritic pattern", skill="Interpretation",
            hint="Think of the branches of a tree.", diagram=DRN, diagram_alt=DRN_ALT,
            feedback="Tree-like branching is a dendritic pattern."),
        MC("A trellised drainage pattern develops where:", [
            C("streams flow outwards from a volcano", why="That is a radial pattern."),
            C("the land is flat and rain is very light", why="Light rain on flat land does not explain a pattern with right-angle joins."),
            C("the land is a swamp", why="A swamp is a wet area and does not form this pattern."),
            C("long parallel ridges and valleys alternate", correct=True),
        ], steps=[S("Link pattern to relief", text="In a trellised pattern, the main streams follow the valleys and the tributaries join them at right angles across the ridges.")],
            concept="Trellised pattern", skill="Concept",
            hint="Which landscape has long straight parallel features?",
            feedback="Alternating parallel ridges and valleys produce trellised drainage."),
        MC("In the figure, which lettered feature carries water only in the rainy season?", [
            C("S", correct=True),
            C("V", why="V is a swamp. It is wet most of the year because it is low and flat."),
            C("P", why="P is a confluence on the main river, which flows all year."),
            C("R", why="R is the mouth of the permanent R. Kuma at the lake."),
        ], steps=[S("Read the symbol", text="S is on a broken blue line. The key says a broken line is a seasonal stream, which flows only in the rainy season.")],
            concept="Seasonal streams", skill="Application",
            hint="Which symbol on the map is a broken line?", diagram=DRN, diagram_alt=DRN_ALT,
            feedback="A broken blue line is a seasonal stream."),
    ]))

# ------------------------------------------------------------------ 3. Vegetation and land use
SETS.append(practice_set(
    module=MODULE, topic=TOPIC, title="Vegetation and land use", lesson="mapint-vegetation-and-land-use",
    questions=[
        MC("Land use means:", [
            C("the way people use the land", correct=True),
            C("the kind of rock under the land", why="Rock type is geology, not land use."),
            C("the height of the land", why="Height is relief, not land use."),
            C("the amount of rain on the land", why="Rainfall is climate, not land use."),
        ], steps=[S("Recall the definition", text="Land use is what people do with the land, for example farming, grazing or building.")],
            concept="Definition of land use", skill="Recall",
            hint="Think about what people do on the land.", feedback="Land use is the way in which people use the land."),
        MC("A large farm with neat rows of a single tree crop, such as oil palm, is called a:", [
            C("swamp", why="A swamp is a wet area, not a farm."),
            C("hamlet", why="A hamlet is a very small settlement."),
            C("plantation", correct=True),
            C("savanna", why="Savanna is a natural grassland with scattered trees."),
        ], steps=[S("Recall the term", text="A plantation is a large commercial farm that grows one crop in rows.")],
            concept="Plantation", skill="Recall",
            hint="The word describes a large commercial tree-crop farm.", feedback="A plantation grows one crop in rows."),
        MC("In the figure, the area marked P shows:", [
            C("farmland", why="Farmland is yellow with crop signs. P has green tree signs."),
            C("swamp", why="Swamp has blue lines and grass tufts. P has tree rings."),
            C("grassland", why="Grassland has tufts on a white background. P is in the hills."),
            C("forest", correct=True),
        ], steps=[S("Use the key", text="P is on the high land in the north-west. The key shows green rings for forest.")],
            concept="Reading the key", skill="Interpretation",
            hint="Check the key for the sign that matches the pattern at P.", diagram=MAPQ, diagram_alt=MAPQ_ALT,
            feedback="P is forest, shown by green rings on high land."),
        MC("In the figure, the area marked R is probably used for:", [
            C("fishing", why="R is on high land, not by the water."),
            C("grazing", correct=True),
            C("plantation farming", why="A plantation needs flat land with a transport link. R has no road or railway."),
            C("a town", why="R is open grass with no buildings or roads."),
        ], steps=[S("Use the key and the relief", text="R is on the plateau in the north-east, covered with grass. Open grass on high flat land is usually used for grazing.")],
            concept="Grazing land", skill="Interpretation",
            hint="What sign covers the plateau?", diagram=MAPQ, diagram_alt=MAPQ_ALT,
            feedback="Grass on the plateau suits cattle, so R is grazing land."),
        MC("In the figure, which is the best reason why forest covers Kuma Hill (P)?", [
            C("The hill is on flat land", why="The contours on Kuma Hill are close together, which means steep slopes, not flat land."),
            C("The hill has a railway", why="The railway is far to the south."),
            C("The slopes are steep and hard to farm", correct=True),
            C("The hill is in the swamp", why="The swamp is beside the lake in the south-east."),
        ], steps=[S("Read the contours", text="The contours on Kuma Hill are crowded, which shows steep slopes. Steep slopes are hard to plough and soil is easily washed away."),
                  S("Give the link", text="So the slopes are left under forest.")],
            concept="Relief and forest", skill="Reasoning",
            hint="Look at the spacing of the contour lines on the hill.", diagram=MAPQ, diagram_alt=MAPQ_ALT,
            feedback="Steep slopes are hard to farm, so they stay forested."),
        MC("In the figure, the plantation marked Q is on low flat land close to the railway. Which statement is a good explanation of its location?", [
            C("Flat land is easy to work and the railway takes the crop to market", correct=True),
            C("The land is too steep for other crops", why="The land at Q is flat, not steep."),
            C("The area is too wet for any other use", why="Q is on dry land, not in the swamp."),
            C("There are no roads or railways nearby", why="There is a railway and an estate road. Plantations need transport."),
        ], steps=[S("Link land and access", text="A plantation needs a large flat area and an easy way to move crops, so the flat land beside the railway suits it.")],
            concept="Location of a plantation", skill="Application",
            hint="Think about what a large commercial farm needs.", diagram=MAPQ, diagram_alt=MAPQ_ALT,
            feedback="Plantations need flat land and transport."),
        MC("Which statement correctly describes the distribution of farmland in Kuma District?", [
            C("It covers the whole of the north-west highlands", why="The north-west highlands are under forest."),
            C("It covers the whole plateau", why="The plateau is grassland."),
            C("It forms a single block in the south-east", why="The south-east has the lake and swamp."),
            C("It is found in small patches near villages and on gentle slopes", correct=True),
        ], steps=[S("Check the map", text="The yellow farmland symbols appear in small separate patches near Ekum, Tabeng and Bimbi, all on gentle slopes.")],
            concept="Describing distribution", skill="Interpretation",
            hint="Look for where the yellow farmland signs are.", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="Farmland is in small patches near settlements, on gentle slopes."),
        MC("Which sentence EXPLAINS the land use rather than only describing it?", [
            C("There is a swamp around Lake Bimbi.", why="This only describes where the swamp is."),
            C("The swamp is not farmed because the wet, flat ground is waterlogged.", correct=True),
            C("The swamp is in the south-east of the map.", why="This only gives a location."),
            C("The swamp is blue and green on the map.", why="This describes the symbol only."),
        ], steps=[S("Look for the reason", text="An explanation says WHY. The second sentence gives a reason: the ground is waterlogged, so crops cannot grow.")],
            concept="Describe versus explain", skill="Reasoning",
            hint="Which sentence contains a reason (a word like 'because')?", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="An explanation gives a reason."),
    ]))

# ------------------------------------------------------------------ 4. Settlement, communication and economic activity
SETS.append(practice_set(
    module=MODULE, topic=TOPIC, title="Settlement, communication and economic activity", lesson="mapint-settlement-communication-and-economic-activity",
    questions=[
        MC("A nucleated settlement is one in which the buildings are:", [
            C("in a line along a road", why="That is a linear settlement."),
            C("scattered far apart", why="That is a dispersed settlement."),
            C("found only on hills", why="This describes a location, not a pattern."),
            C("grouped closely around a centre", correct=True),
        ], steps=[S("Recall the pattern", text="Nucleated means clustered around a centre.")],
            concept="Nucleated settlement", skill="Recall",
            hint="The word 'nucleus' means centre.", feedback="Nucleated means grouped around a centre."),
        MC("The position of a settlement in relation to the hills, rivers and routes around it is called its:", [
            C("site", why="Site is the actual ground on which the settlement is built."),
            C("situation", correct=True),
            C("function", why="Function is the settlement's main job."),
            C("pattern", why="Pattern is the arrangement of the buildings."),
        ], steps=[S("Recall the terms", text="Site is the ground. Situation is the position in relation to the surroundings.")],
            concept="Site and situation", skill="Concept",
            hint="Which word is about the relationship to the surroundings?", feedback="Situation is the position in relation to the surroundings."),
        MC("In the figure, the village of Njomi has its houses in a line along the main road. Its pattern is:", [
            C("nucleated", why="Njomi's houses are not grouped around a centre."),
            C("dispersed", why="The houses are close together in a line, not scattered."),
            C("linear", correct=True),
            C("radial", why="Radial is a drainage pattern."),
        ], steps=[S("Look at the shape", text="The houses of Njomi follow the main road in a line, so it is a linear settlement.")],
            concept="Linear settlement", skill="Interpretation",
            hint="What shape do the buildings make?", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="Houses along a road form a linear settlement."),
        MC("In the figure, the main function of Tabeng is:", [
            C("market town and route centre", correct=True),
            C("farming village", why="Tabeng is a large town with a market and a station, not a farming village."),
            C("fishing village", why="Tabeng is not on the lake."),
            C("forest camp", why="Tabeng is on flat land far from the forest."),
        ], steps=[S("Use the evidence", text="Tabeng has a market, a railway station and roads that meet there, so it is a market town and a route centre.")],
            concept="Function of a town", skill="Interpretation",
            hint="Look at the signs next to Tabeng.", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="A market, a station and meeting roads make Tabeng a market town and route centre."),
        NUM("Count the named villages (not the town) in the figure. How many are there?", 5,
            steps=[S("Read the names", text="The villages are Njomi, Mbolo, Ekum, Bimbi and Fundi. Tabeng is the town, so it is not counted.")],
            concept="Counting settlements", skill="Interpretation",
            hint="List every settlement name, then remove the town.", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="There are five named villages."),
        MC("In the figure, the tarred road from the north crosses the hills at the saddle. The best reason is that:", [
            C("saddles are always flat and wide", why="A saddle is a dip, but it is not always flat or wide."),
            C("the saddle is the steepest point", why="The saddle is a dip in the ridge, not the steepest place."),
            C("roads cannot be built in valleys", why="Roads are often built in valleys. This does not explain the saddle."),
            C("the saddle is the lowest point on the high ground", correct=True),
        ], steps=[S("Compare routes", text="A road climbs less through the saddle (about 564 metres) than over either hill. So the saddle is the easiest crossing.")],
            concept="Roads and relief", skill="Reasoning",
            hint="Think about how much a road would climb over each choice.", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="Roads use saddles because they are the lowest crossing of high ground."),
        MC("In the figure, why does the railway run across the southern lowland?", [
            C("Trains need a gentle gradient, so the flat lowland is the easiest route", correct=True),
            C("There is no land in the north", why="There is land in the north, but it is high and steep."),
            C("Railways must cross lakes", why="Railways avoid lakes and swamps. This one passes north of them."),
            C("The plateau is too low for a railway", why="The plateau is high, not low."),
        ], steps=[S("Link railway and relief", text="Railways need a very gentle gradient. The southern lowland is almost flat, so building is easy and cheap.")],
            concept="Railways and gradient", skill="Application",
            hint="What kind of slope can a train climb?", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="Trains need gentle gradients, so railways follow flat land."),
        MC("In the figure, a footpath climbs the escarpment to the hamlets on the plateau, but there is no road. The best explanation is that:", [
            C("people on the plateau never travel", why="The footpath shows that they do travel."),
            C("the escarpment is too steep for a road, but people can climb it on foot", correct=True),
            C("the plateau has no settlements", why="Fundi hamlets are on the plateau."),
            C("a footpath is faster than a railway", why="Speed is not the reason. Steepness is."),
        ], steps=[S("Read the contours", text="The escarpment has contours close together, so it is very steep. A road must have an easy gradient, but a footpath can climb steeply.")],
            concept="Footpaths on steep slopes", skill="Reasoning",
            hint="What does the spacing of the contours tell you about the escarpment?", diagram=MAP, diagram_alt=MAP_ALT,
            feedback="Steep slopes block roads, but paths can climb them."),
    ]))

# ------------------------------------------------------------------ 5. Sketch maps and linking features
SKT = "f5g-mapint-sketch-example.svg"
SKT_ALT = "A model sketch map of Kuma District with frame, title, north arrow, scale, key and labels numbered one to six"
SETS.append(practice_set(
    module=MODULE, topic=TOPIC, title="Sketch maps and linking features", lesson="mapint-sketch-maps-and-linking-features",
    questions=[
        MC("A sketch map is best described as:", [
            C("an exact copy of the whole map", why="A sketch map is not an exact copy and it does not include everything."),
            C("a simple drawing of part of a map showing only the features asked for", correct=True),
            C("a drawing of the relief only", why="A sketch map can show any features the question asks for."),
            C("a photograph of the area", why="A sketch map is drawn, not photographed."),
        ], steps=[S("Recall the definition", text="A sketch map is a simple drawing of part of a map with only the requested features.")],
            concept="Definition of a sketch map", skill="Recall",
            hint="Think about the word 'only'.", feedback="A sketch map shows only the features asked for."),
        MC("Which of these should NOT be on a sketch map that asks for the river and the lake only?", [
            C("a title", why="A title is needed."),
            C("a key", why="A key is needed."),
            C("a north arrow", why="A north arrow is needed."),
            C("the railway and the villages", correct=True),
        ], steps=[S("Check the question", text="The question asks for the river and the lake only. The railway and villages were not asked for, so leave them out.")],
            concept="Only the features asked for", skill="Application",
            hint="Which item is not part of the question?",
            feedback="Draw only what the question asks for."),
        MC("What should you draw first when you start a sketch map?", [
            C("the frame", correct=True),
            C("the key", why="The key comes after the features, once you know which symbols you used."),
            C("the labels", why="Labels come last, after the features are drawn."),
            C("the railway", why="Features are drawn after the frame."),
        ], steps=[S("Order of work", text="Frame, title, north and scale, features, key, labels. The frame is first because it sets the shape and size.")],
            concept="Order of drawing", skill="Concept",
            hint="What gives the sketch its shape and size?", feedback="Start with the frame."),
        MC("A good key on a sketch map:", [
            C("lists only the features you did not draw", why="The key must explain the features you did draw."),
            C("is optional if the labels are clear", why="The key is required as part of the sketch map."),
            C("has a symbol and a name for every feature you drew", correct=True),
            C("has the scale of the map", why="Scale is shown separately, not in the key."),
        ], steps=[S("Use of a key", text="The key explains each symbol. Every feature drawn needs a symbol and a name in the key.")],
            concept="Key on a sketch map", skill="Concept",
            hint="Think about what a key explains.", feedback="Every symbol you draw must appear in the key."),
        NUM("Kuma District is 9 km wide and 6 km high. You draw a frame 12 centimetres wide. "
            "What height, in centimetres, keeps the same shape?", 8, unit="cm",
            steps=[S("Find the ratio", math=r"\frac{6}{9} = \frac{2}{3}"),
                   S("Apply to the width", math=r"12 \times \frac{2}{3} = 8")],
            concept="Proportion of the frame", skill="Calculation",
            hint="The height is two thirds of the width.",
            feedback="The frame is 12 cm by 8 cm."),
        MC("In the figure, the circle numbered 4 marks the:", [
            C("title", why="The title is marked 2."),
            C("scale", correct=True),
            C("key", why="The key is marked 5."),
            C("frame", why="The frame is marked 1."),
        ], steps=[S("Read the checklist", text="The checklist beside the figure shows 1 frame, 2 title, 3 north arrow, 4 scale, 5 key, 6 labels.")],
            concept="Parts of a sketch map", skill="Interpretation",
            hint="Read the checklist beside the sketch.", diagram=SKT, diagram_alt=SKT_ALT,
            feedback="Number 4 marks the scale line."),
        MC("Which sentence correctly links a physical feature to a human activity?", [
            C("The R. Kuma flows into Lake Bimbi.", why="This only describes a physical feature."),
            C("Tabeng has a market.", why="This only describes a human feature."),
            C("Kuma Hill is 706 metres high.", why="This only gives a height."),
            C("The railway crosses the flat lowland because trains need gentle slopes.", correct=True),
        ], steps=[S("Check for a link", text="The correct sentence names a human feature (the railway), a physical feature (flat lowland) and gives a reason.")],
            concept="Linking physical and human features", skill="Application",
            hint="Which sentence has both a land feature, an activity and a reason?",
            feedback="A link joins the land to the human activity with a reason."),
        MC("Which answer to 'Explain why there are few houses around Lake Bimbi' scores best?", [
            C("The land beside the lake is low, flat and swampy (evidence), so it is too wet to build or farm (explanation).", correct=True),
            C("There are few houses there.", why="This repeats the question without a reason."),
            C("The lake is blue.", why="This is a description of the symbol and gives no reason."),
            C("There is a swamp.", why="This gives some evidence but no explanation of why it matters."),
        ], steps=[S("Check for the three parts", text="A full answer gives the point, the evidence from the map and the explanation. Only one option has all three.")],
            concept="Point, evidence, explanation", skill="Reasoning",
            hint="Look for the answer that gives a reason as well as a fact.",
            feedback="The best answer gives evidence and an explanation."),
    ]))
