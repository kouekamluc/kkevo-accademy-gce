"""Practice sets for Form 5 Geography: Map Reading and Interpretation, Map reading (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Map Reading and Interpretation"
TOPIC = "Map reading"

PLAIN = "f5g-map-mbanga-plain.svg"
PLAIN_ALT = ("Fictitious map of Mbanga Plain with numbered eastings 31 to 38 and northings 52 to 58, a river, tarred and murram roads, "
             "a railway, villages, a forest, a plantation, a hill with a trig station, a key, a scale bar and a north arrow")
BEAR = "f5g-map-bearings.svg"
BEAR_ALT = ("Mbanga Plain map with four marked points: P at the church in Mbanga, Q at the trig station on Ngoro Hill, R at Tanjo and S at Nkolo, "
            "with dashed lines from P to each of Q, R and S and a dotted north line at P; the scale is 1:50 000 and the grid squares are 1 km wide")

SETS = []

# ------------------------------------------------------------------ 1. What is a map
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Maps, marginal information, signs and colours",
    lesson="map-what-is-a-map-marginal-information-and-signs",
    questions=[
        MC("Which statement best defines a map?", [
            C("A drawing of the earth's surface seen from above, drawn to scale and using signs and symbols", correct=True),
            C("A photograph of the ground taken from an aircraft", why="That is an aerial photograph. A map is drawn, uses signs and is drawn to scale."),
            C("A list of place names with their heights", why="A list gives names and numbers but does not show where places are in relation to each other."),
            C("A sketch of a place drawn from memory with no scale", why="A map is drawn to scale. A memory sketch with no scale cannot be used to measure."),
        ], steps=[S("Recall the definition", text="A map is a drawing of the whole or part of the earth's surface, seen from above, drawn to scale using signs and symbols.")],
           concept="Definition of a map", skill="Recall", hint="Think of three things a map must have: it is a drawing, it is to scale, and it uses signs."),
        MC("A local council wants to choose a site for a new health centre. How does a map help the council most?", [
            C("It tells the council how much money the health centre will cost", why="A map does not show costs. It shows where things are."),
            C("It shows the number of people living in every house", why="A topographic map shows features such as villages and roads, not the number of people in each house."),
            C("It makes it unnecessary to visit the site", why="A map helps planning, but a planner still has to visit and check the site."),
            C("It shows where villages, roads and rivers are, so a site that people can reach can be chosen", correct=True),
        ], steps=[S("Link the map to the job", text="Planners use maps to see the position of villages, roads and rivers. They can then choose a site that is easy to reach.")],
           concept="Importance of maps", skill="Application", hint="What does a map show about the land that a planner needs to know?"),
        MC("Which of these is NOT marginal information?", [
            C("The title", why="The title is printed in the margin, so it is marginal information."),
            C("The scale", why="The scale is printed in the margin, so it is marginal information."),
            C("The River Mbo drawn across the map", correct=True),
            C("The north arrow", why="The north arrow is printed in the margin, so it is marginal information."),
        ], steps=[S("Separate map and margin", text="Marginal information is printed around the map. The River Mbo is a feature drawn on the map itself.")],
           concept="Marginal information", skill="Concept", hint="Marginal information is found in the margins, outside the picture."),
        MC("The map shows brown rings around Ngoro Hill. What should a student do first to be sure what they stand for?", [
            C("Decide they are rivers because they are curved lines", why="Rivers are blue on this map. Never decide from the shape alone."),
            C("Look in the key, which explains each sign and colour", correct=True),
            C("Measure them with the scale bar", why="The scale bar gives distance. It does not explain what a sign means."),
            C("Read the sheet number", why="The sheet number identifies the map. It does not explain signs."),
        ], steps=[S("Use the key", text="The key lists every sign and colour. Here it shows brown contour lines, which stand for relief.")],
           concept="Purpose of the key", skill="Application", hint="Which part of the marginal information explains the signs?",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
        MC("A map was printed in 1990. A student uses it in 2025 to plan a new road. Which marginal information warns that the map may be out of date?", [
            C("The date", correct=True),
            C("The scale", why="The scale tells how distance is reduced. It does not show how old the map is."),
            C("The north arrow", why="The north arrow gives direction only."),
            C("The title", why="The title names the area but does not give the age."),
        ], steps=[S("Find the age", text="The date shows when the map was made. A map from 1990 may not show roads, villages or farms built since then.")],
           concept="Date and authority", skill="Reasoning", hint="Which item gives a year?"),
        MC("What does the sign for a church look like on the Mbanga Plain map?", [
            C("A circle containing the letter S", why="This is the sign for a school."),
            C("A small black cross", correct=True),
            C("A black triangle with a dot in the middle", why="This is the sign for a trig station."),
            C("A small black rectangle", why="This is the sign for a railway station."),
        ], steps=[S("Check the key", text="The key shows a small black cross for a church. Look at the key before you decide.")],
           concept="Conventional signs", skill="Interpretation", hint="Find 'Church' in the key and compare the sign.",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
        MC("A thin dashed black line runs south from the village of Tanjo. What does it show?", [
            C("A river", why="A river is a blue wavy line."),
            C("A railway", why="A railway is a line with cross ties."),
            C("A murram road", why="A murram road is a solid grey line."),
            C("A track", correct=True),
        ], steps=[S("Compare the line with the key", text="The key shows a dashed black line for a track. A river is blue, a railway has ties, and a murram road is solid grey.")],
           concept="Conventional signs", skill="Interpretation", hint="Compare the style of the line (solid, dashed, with ties) in the key.",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
        MC("The south-west corner of the map has green circles inside a green box. What does this show?", [
            C("Water, because it is near the river", why="Water is shown in blue."),
            C("A plantation", why="A plantation has a dotted border and green dots, not circles."),
            C("Forest, because green stands for vegetation and the key shows circles for forest", correct=True),
            C("A built-up area", why="Built-up areas are shown in grey."),
        ], steps=[S("Colour and key", text="Green stands for vegetation. The key shows circles in a green box for forest. This is Bakoa Forest.")],
           concept="Meaning of colours", skill="Interpretation", hint="Check both the colour and the pattern in the key.",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
    ]))

# ------------------------------------------------------------------ 2. Grid references
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Grid lines and grid references",
    lesson="map-grid-lines-and-grid-references",
    questions=[
        MC("Which statement about eastings is correct?", [
            C("They are horizontal lines, and their numbers rise to the north", why="This describes northings, not eastings."),
            C("They are vertical lines, and their numbers rise to the east", correct=True),
            C("They are the part of the reference that is written last", why="The easting is written first."),
            C("They are curved lines that show height", why="Lines showing height are contours. Eastings are straight grid lines."),
        ], steps=[S("Recall", text="Eastings are the vertical grid lines. Their numbers increase towards the east (right).")],
           concept="Eastings", skill="Recall", hint="Eastings run up and down the map, and 'east' tells you which way the numbers rise."),
        MC("Which rule gives the correct order for a grid reference?", [
            C("Northing first, then easting", why="This reverses the order and gives a different place."),
            C("The bigger number is written first", why="The order does not depend on size."),
            C("The numbers on the side of the map come first", why="The side numbers are northings, which come second."),
            C("Along the corridor, then up the stairs: easting first, then northing", correct=True),
        ], steps=[S("Order", text="Read along the bottom or top first (easting), then up the side (northing).")],
           concept="Order of a grid reference", skill="Recall", hint="Think of the rhyme about a corridor and stairs."),
        MC("What is the four-figure grid reference of the square that contains Nkolo village?", [
            C("5237", why="The numbers are in the wrong order. The easting must come first."),
            C("3852", why="This uses the easting line on the right of the village (38) instead of the one on the left (37)."),
            C("3752", correct=True),
            C("3753", why="This uses the northing line above the village (53) instead of the one below (52)."),
        ], steps=[S("Easting", text="Nkolo lies between easting lines 37 and 38. Use the left line: 37."),
                  S("Northing", text="It lies between northing lines 52 and 53. Use the lower line: 52."),
                  S("Join", math=r"3752")],
           concept="Four-figure grid references", skill="Application", hint="Use the line on the left and the line below the village.",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
        MC("What is the six-figure grid reference of the railway station in Mbanga?", [
            C("360553", correct=True),
            C("553360", why="The northing has been written first. The easting comes first."),
            C("36553", why="The zero tenths figure has been left out. The station is exactly on line 36, so the easting is 360."),
            C("363553", why="The easting has been given 3 tenths, but the station is on the easting line itself, so 0 tenths."),
        ], steps=[S("Easting", text="The station is on easting line 36, so the tenths figure is 0. The easting is 360."),
                  S("Northing", text="It is 3 tenths above northing line 55. The northing is 553."),
                  S("Join", math=r"360553")],
           concept="Six-figure grid references", skill="Application", hint="The station sits exactly on a vertical grid line. What does that make the tenths figure?",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
        MC("What feature is found at grid reference 376551?", [
            C("The school", why="The school is at 364529, in the south of the map."),
            C("The health centre", correct=True),
            C("The market", why="The market is at 346549, in Mbanga town."),
            C("The railway station", why="The railway station is at 360553, on the railway."),
        ], steps=[S("Easting", text="376 means line 37 and 6 tenths along."),
                  S("Northing", text="551 means line 55 and 1 tenth up."),
                  S("Name the feature", text="At this point there is a circle with a cross inside: the health centre.")],
           concept="Finding a feature from a reference", skill="Application", hint="Go along to 37.6, then up to 55.1.",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
        NUM("A bridge is 8 tenths of the way from easting line 52 to line 53, and 3 tenths of the way up from northing line 17 to line 18. Type its six-figure grid reference as one number.", 528173,
            steps=[S("Easting", text="Line 52 and 8 tenths gives 528."),
                   S("Northing", text="Line 17 and 3 tenths gives 173."),
                   S("Join", math=r"528173")],
            concept="Six-figure grid references", skill="Calculation", hint="Write the easting first as the line number followed by the tenths."),
        MC("A four-figure grid reference tells you the position of a feature to within:", [
            C("one grid square (1 km by 1 km on the Mbanga Plain map)", correct=True),
            C("about 100 metres", why="This is the accuracy of a six-figure reference."),
            C("about 1 centimetre", why="A grid reference does not give centimetres."),
            C("the whole map sheet", why="A four-figure reference is more exact than that."),
        ], steps=[S("Accuracy", text="Four figures name a whole grid square. On the practice map each square is 1 km by 1 km.")],
           concept="Accuracy of grid references", skill="Concept", hint="How many tenths does a four-figure reference use?"),
        MC("The trig station on Ngoro Hill is in grid square 3656. A student wrote 5636. What mistake did she make?", [
            C("She used the lines on the right and above the station", why="That would give 3757, not 5636."),
            C("She read the tenths wrongly", why="A four-figure reference has no tenths."),
            C("She used the wrong scale", why="The scale does not affect a grid reference."),
            C("She wrote the northing before the easting", correct=True),
        ], steps=[S("Compare", text="The correct reference is 3656: easting 36, northing 56. She wrote 56 first, then 36. She swapped the order.")],
           concept="Order of a grid reference", skill="Reasoning", hint="Compare the two numbers: where have 36 and 56 moved to?",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
    ]))

# ------------------------------------------------------------------ 3. Directions and bearings
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Directions and bearings",
    lesson="map-directions-and-bearings",
    questions=[
        MC("Which compass point lies halfway between north and north-east?", [
            C("East-north-east (ENE)", why="ENE lies between north-east and east."),
            C("North-north-west (NNW)", why="NNW lies between north and north-west, on the other side of north."),
            C("North-north-east (NNE)", correct=True),
            C("North-east (NE)", why="North-east is itself halfway between north and east."),
        ], steps=[S("Use the 16 points", text="Between N and NE the 16-point compass has NNE.")],
           concept="16 points of the compass", skill="Recall", hint="Say the points in order from north: N, then ...?"),
        MC("Which is the correct way to write a true bearing of 45 degrees?", [
            C("45°", why="A bearing needs three figures, so a zero must be added in front."),
            C("0.45°", why="This changes the size of the angle. 0.45° is almost north."),
            C("450°", why="Bearings go only up to 360°."),
            C("045°", correct=True),
        ], steps=[S("Three figures", text="A bearing is always written with three figures, so 45° is written 045°.")],
           concept="Writing a bearing", skill="Recall", hint="How many figures must a bearing have?"),
        MC("What is the direction of Nkolo (S) from the church (P)?", [
            C("North-east", why="North-east would be above and to the right. Nkolo is below the church."),
            C("South-east", correct=True),
            C("South-west", why="Nkolo is to the right (east) of the church, not the left."),
            C("North-west", why="North-west would be above and to the left."),
        ], steps=[S("Compare positions", text="Nkolo (S) is below and to the right of the church (P) on the map: south and east, so south-east.")],
           concept="Compass direction on a map", skill="Interpretation", hint="Is S above or below P, and to the left or right?",
           diagram=BEAR, diagram_alt=BEAR_ALT),
        MC("What is the bearing of the trig station Q from the church P?", [
            C("060°", correct=True),
            C("030°", why="30° is measured from east instead of from north (90° − 60°)."),
            C("120°", why="120° is 180° − 60°. It is measured from south instead of north."),
            C("240°", why="240° is the bearing of P from Q, the back bearing."),
        ], steps=[S("Draw the north line", text="At P, the north line points straight up."),
                  S("Measure clockwise", text="The angle from the north line to PQ is 60°."),
                  S("Write three figures", math=r"060^\circ")],
           concept="Measuring a bearing", skill="Application", hint="Q is north-east of P, so the bearing is between 000° and 090°.",
           diagram=BEAR, diagram_alt=BEAR_ALT),
        MC("What is the bearing of Tanjo R from the church P?", [
            C("056°", why="56° is the angle measured anticlockwise from north. A bearing is measured clockwise."),
            C("124°", why="124° is the back bearing of R from P, the bearing of P from R."),
            C("304°", correct=True),
            C("236°", why="236° is 180° + 56°. It points south-west, but R is north-west of P."),
        ], steps=[S("Find the quarter", text="R is north-west of P, so the bearing is between 270° and 360°."),
                  S("Convert", math=r"360^\circ - 56^\circ = 304^\circ", text="The angle to the left of north is about 56°.")],
           concept="Bearings greater than 180°", skill="Application", hint="R is north-west of P. Which bearings point north-west?",
           diagram=BEAR, diagram_alt=BEAR_ALT),
        NUM("The bearing of Q from P is 060°. Find the bearing of P from Q (type the number of degrees).", 240, unit="degrees",
            steps=[S("Back bearing", math=r"060^\circ + 180^\circ = 240^\circ", text="The bearing is less than 180°, so add 180°.")],
            concept="Back bearing", skill="Calculation", hint="Is 060 less than 180 or more? What do you do in each case?"),
        MC("The bearing of Y from X is 075°. What is the bearing of X from Y?", [
            C("105°", why="This is 180° − 75°. The rule is to add 180° to a bearing below 180°."),
            C("255°", correct=True),
            C("285°", why="This is 360° − 75°, which is an anticlockwise angle."),
            C("075°", why="A bearing and its back bearing are always 180° apart, so they cannot be equal."),
        ], steps=[S("Back bearing", math=r"075^\circ + 180^\circ = 255^\circ")],
           concept="Back bearing", skill="Reasoning", hint="The bearing is less than 180°, so you must add."),
        NUM("Measure or work out the bearing of Nkolo (S) from the church (P). Give your answer in degrees, as a number.", 136, tolerance=3, unit="degrees",
            steps=[S("Quarter", text="S is south-east of P, so the bearing is between 090° and 180°."),
                   S("Measure", text="S is 2.7 km east and 2.8 km south of P. The angle between the south line and PS is about 44°."),
                   S("Subtract from 180°", math=r"180^\circ - 44^\circ = 136^\circ")],
            concept="Measuring a bearing", skill="Calculation", hint="The bearing is between 090° and 180°. Measure clockwise from the north line at P.",
            diagram=BEAR, diagram_alt=BEAR_ALT),
    ]))

# ------------------------------------------------------------------ 4. Scale, distance and area
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Scale, distance and area",
    lesson="map-scale-distance-and-area",
    questions=[
        MC("Which of these is a representative fraction?", [
            C("1 cm to 5 km", why="This is a statement of scale, written in words."),
            C("1:50 000", correct=True),
            C("A line marked 0, 1, 2, 3 km", why="This is a linear (bar) scale."),
            C("2 cm = 1 km", why="This is a statement of scale."),
        ], steps=[S("Recall", text="A representative fraction is a ratio without units, such as 1:50 000.")],
           concept="Forms of scale", skill="Recall", hint="A representative fraction is a ratio with a colon."),
        NUM("A map has the scale 1:50 000. How many kilometres on the ground does 1 cm on the map represent?", 0.5, unit="km",
            steps=[S("Change centimetres to km", math=r"50\,000 \text{ cm} = 500 \text{ m} = 0.5 \text{ km}")],
            concept="RF to statement", skill="Calculation", hint="1 km is 100 000 cm. Divide 50 000 by 100 000."),
        NUM("A map has the statement of scale '1 cm to 2 km'. Write the representative fraction as 1 : n. Type the value of n.", 200000,
            steps=[S("Kilometres to centimetres", math=r"2 \text{ km} = 2 \times 100\,000 = 200\,000 \text{ cm}"),
                   S("Write the RF", math=r"1 : 200\,000")],
            concept="Statement to RF", skill="Calculation", hint="Change 2 km into centimetres first."),
        NUM("Two villages are 7.4 cm apart on a map of scale 1:50 000. What is the real distance between them in kilometres?", 3.7, tolerance=0.05, unit="km",
            steps=[S("1 cm stands for 0.5 km", text="At 1:50 000, 1 cm = 0.5 km."),
                   S("Multiply", math=r"7.4 \times 0.5 = 3.7 \text{ km}")],
            concept="Measuring distance", skill="Calculation", hint="First work out how many kilometres 1 cm stands for."),
        MC("Using the scale bar, the straight-line distance from P to Q is closest to:", [
            C("2.0 km", why="This is too short: P to Q crosses about three grid squares, each 1 km wide."),
            C("3.9 km", why="3.9 km is the distance from P to S, not from P to Q."),
            C("3.0 km", correct=True),
            C("5.0 km", why="This is too long. The scale bar is 3 km long, and PQ is about as long as the bar."),
        ], steps=[S("Compare with the scale bar", text="The line PQ is about the same length as the 3 km scale bar. Q is 2.6 km east and 1.5 km north of P, so the distance is about 3.0 km.")],
           concept="Distance from a scale bar", skill="Interpretation", hint="Hold a strip of paper against PQ and then against the scale bar.",
           diagram=BEAR, diagram_alt=BEAR_ALT),
        MC("The murram road runs from the junction on the tarred road in Mbanga, with several bends, to Nkolo village. Using the scale, what is the best estimate of its length?", [
            C("3.4 km", why="This is the straight-line distance. The road bends and so is longer."),
            C("5.5 km", why="This is too long. The road is made of four sections of about 1 km each."),
            C("2.0 km", why="This is far too short. The road runs across several grid squares."),
            C("4.0 km", correct=True),
        ], steps=[S("String method", text="The road has four straight sections, each about 1 km long. The string laid straight is 4.0 km at the map scale.")],
           concept="Winding distance", skill="Application", hint="A winding road is longer than the straight line between its ends. Break it into sections.",
           diagram=PLAIN, diagram_alt=PLAIN_ALT),
        NUM("Each grid square on the Mbanga Plain map is 1 km by 1 km. Bakoa Forest Reserve (the green area in the south-west) covers three whole squares and one half square. Find its area in square kilometres.", 3.5, tolerance=0.25, unit="km²",
            steps=[S("Count squares", math=r"3 + 0.5 = 3.5 \text{ squares}"),
                   S("Convert", math=r"3.5 \times 1 \text{ km}^2 = 3.5 \text{ km}^2")],
            concept="Area from grid squares", skill="Calculation", hint="Add the whole squares and the half square, then multiply by the area of one square.",
            diagram=PLAIN, diagram_alt=PLAIN_ALT),
        NUM("A lake covers 12 cm² on a map of scale 1:50 000. Find its real area in square kilometres.", 3, tolerance=0.05, unit="km²",
            steps=[S("Area of 1 cm²", math=r"0.5 \text{ km} \times 0.5 \text{ km} = 0.25 \text{ km}^2"),
                   S("Multiply", math=r"12 \times 0.25 = 3 \text{ km}^2")],
            concept="Area from map measurements", skill="Calculation", hint="First find the real area of 1 cm² on the map, remembering that area is length times width."),
    ]))

# ------------------------------------------------------------------ 5. Copying, reducing, enlarging
SETS.append(practice_set(
    module=MODULE, topic=TOPIC,
    title="Copying, reducing and enlarging maps",
    lesson="map-copying-reducing-and-enlarging",
    questions=[
        MC("In the grid method of enlarging part of a map, the new grid must have:", [
            C("the same number of squares, but each square is larger", correct=True),
            C("more squares, each the same size as before", why="The number of squares stays the same. Only the size changes."),
            C("fewer squares, each larger", why="Using fewer squares changes how features are placed. The number stays the same."),
            C("the same squares, printed in a different colour", why="Colour does not change the size of the map."),
        ], steps=[S("Recall", text="The new grid has the same number of rows and columns. Each square is larger for an enlargement and smaller for a reduction.")],
           concept="Grid method", skill="Recall", hint="Which of the two numbers changes: the number of squares or their size?"),
        NUM("A map of scale 1:50 000 is enlarged so that every length is doubled. The new scale is 1:n. Type the value of n.", 25000,
            steps=[S("Divide by the factor", math=r"50\,000 \div 2 = 25\,000")],
            concept="Change of scale", skill="Calculation", hint="A bigger map has a smaller number after the colon."),
        NUM("A map of scale 1:50 000 is reduced to half size. The new scale is 1:n. Type the value of n.", 100000,
            steps=[S("Multiply by 2", math=r"50\,000 \times 2 = 100\,000")],
            concept="Change of scale", skill="Calculation", hint="A smaller map has a bigger number after the colon."),
        MC("A map of scale 1:50 000 is enlarged so that every length becomes 2.5 times as long. What is the new scale?", [
            C("1:125 000", why="This multiplies by 2.5. That would make the map smaller, not larger."),
            C("1:20 000", correct=True),
            C("1:100 000", why="This would be a reduction to half size."),
            C("1:47 500", why="This subtracts 2500, which is not how scale changes."),
        ], steps=[S("Divide", math=r"50\,000 \div 2.5 = 20\,000")],
           concept="Change of scale", skill="Calculation", hint="When you enlarge, divide the old denominator by the factor."),
        MC("Every length on a map is doubled by an enlargement. The area of a lake on the map becomes:", [
            C("2 times as big", why="This is the factor for lengths. Area depends on two lengths."),
            C("3 times as big", why="This has no link with the factor."),
            C("8 times as big", why="This would be the factor for volume, not area."),
            C("4 times as big", correct=True),
        ], steps=[S("Area factor", math=r"2 \times 2 = 4")],
           concept="Area and enlargement", skill="Concept", hint="Area is length times width. What happens to both?"),
        NUM("A map section measures 8 cm by 6 cm. It is enlarged so that every length is 2.5 times as long. Find the area of the enlarged section in cm².", 300, unit="cm²",
            steps=[S("New sides", math=r"8 \times 2.5 = 20 \text{ cm}, \quad 6 \times 2.5 = 15 \text{ cm}"),
                   S("Area", math=r"20 \times 15 = 300 \text{ cm}^2")],
            concept="Area and enlargement", skill="Calculation", hint="Find the new length and width first."),
        MC("The figure shows a section of the map in a grid with columns A to D and rows 1 to 3. The section is enlarged using a grid with squares twice as big. In which square of the enlarged grid must the church be drawn?", [
            C("B3", why="B3 is the square below the church, where the market is."),
            C("A2", why="A2 is the square to the left of the church. The squares keep their letters and numbers in the copy."),
            C("B2", correct=True),
            C("C2", why="C2 is the square to the right of the church. The squares keep their letters and numbers in the copy."),
        ], steps=[S("Find the square on the original", text="The church is in column B and row 2 of the original."),
                  S("Use the same square", text="The new grid has the same squares in the same order, so the church is drawn in B2 of the enlarged grid.")],
           concept="Grid method", skill="Application", hint="Find the church on the original grid first. The square letter and number do not change.",
           diagram="f5g-map-copy-enlarge.svg",
           diagram_alt="Before and after: a section of Mbanga Plain in a grid of columns A to D and rows 1 to 3 with squares of 2 cm at 1:50 000, and the same section enlarged with squares of 4 cm at 1:25 000"),
        MC("An area 6 km wide and 4 km high must be drawn on a sheet 15 cm wide and 10 cm high. Which is the largest of these scales that fits?", [
            C("1:25 000", why="At 1:25 000 the map would be 24 cm by 16 cm, too big."),
            C("1:50 000", why="This fits (12 cm by 8 cm), but a larger scale also fits."),
            C("1:100 000", why="This fits (6 cm by 4 cm), but a larger scale also fits."),
            C("1:40 000", correct=True),
        ], steps=[S("1:25 000", text="1 cm = 0.25 km: 24 cm by 16 cm. Too big."),
                  S("1:40 000", text="1 cm = 0.4 km: 6 ÷ 0.4 = 15 cm and 4 ÷ 0.4 = 10 cm. It fits exactly."),
                  S("Others", text="1:50 000 gives 12 by 8 cm and 1:100 000 gives 6 by 4 cm. They fit but are smaller. The largest that fits is 1:40 000.")],
           concept="Choosing a scale", skill="Reasoning", hint="Work out the map size at each scale and look for the largest scale that does not go over 15 cm by 10 cm."),
    ]))
