"""Form 5 Geography, Map Reading and Interpretation: Map reading (5 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Map Reading and Interpretation"
TOPIC = "Map reading"

LESSONS = []

# ------------------------------------------------------------------ 1. What is a map
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="What is a map? Marginal information, signs and colours",
    slug="map-what-is-a-map-marginal-information-and-signs",
    minutes=20,
    summary="What a map is and why maps matter, the marginal information every map carries and why each item is useful, and how conventional signs and colours show real features.",
    objectives=[
        "Define a map and state why maps are important",
        "State the marginal information found on a map and explain why each item matters",
        "Identify conventional signs and symbols and explain what the main colours stand for",
        "Recognise features on a map by using its key",
    ],
    key_concepts=["Map", "Marginal information", "Key (legend)", "Conventional signs and symbols", "Colour on maps"],
    blocks=[
        H("Introduction"),
        T("A taxi driver leaving Douala for Bamenda needs to know the road. A farmer near the Sanaga wants to know where the river bends. "
          "A council planning a new health centre must know where the villages and roads are. All of them need a **map**."),
        T("In Cameroon's GCE Geography examination, map reading is so important that Paper 2 Section A is a compulsory question. "
          "It carries 25% of the marks for the whole examination. Paper 1 also has five multiple-choice questions on map skills."),
        D("A **map** is a drawing of the whole or part of the earth's surface, seen from above, drawn to scale on a flat sheet "
          "and using signs and symbols to show features.", title="Definition: map"),
        KEY("Why maps are important", "Maps help us in four main ways.", cards=[
            ["Finding the way", "Travellers, drivers, farmers and traders use maps to move between places."],
            ["Planning", "Councils use maps to choose sites for roads, schools, markets and health centres."],
            ["Studying", "Geographers use maps to see where features are and how they are linked."],
            ["Recording", "Maps keep a record of land, boundaries, rivers, forests and other resources."],
        ]),
        H("The practice map: Mbanga Plain"),
        T("In all five lessons we use one practice map. **Mbanga Plain is a fictitious place** made up for teaching. "
          "It has a river, roads, a railway, villages, a forest, a plantation and a hill. Study it carefully, because you will meet it again and again."),
        IMG("f5g-map-mbanga-plain.svg",
            alt="Fictitious topographic map of Mbanga Plain with numbered grid lines, a river, roads, a railway, villages, a forest, a plantation, a hill with a trig station, a key, a scale bar and a north arrow",
            caption="Figure 1. Mbanga Plain (fictitious). Scale 1:50 000. Each grid square is 1 km by 1 km. The map is in the middle; the numbers, key, scale bar and north arrow around it are marginal information."),
        H("Marginal information"),
        D("**Marginal information** is all the information printed in the margins (borders) of a map, outside the picture itself, "
          "that helps you to read and use the map.", title="Definition: marginal information"),
        IMG("f5g-map-marginal-information.svg",
            alt="A map sheet with seven numbered parts: 1 title, 2 sheet number, 3 grid lines, 4 scale, 5 north arrow, 6 key, 7 date and authority",
            caption="Figure 2. The marginal information on a map sheet and what each part is used for."),
        KEY("The seven main items", "Know each item and say why it is useful.", cards=[
            ["Title", "Names the area shown, so you know you have the right map."],
            ["Sheet number", "A map is one sheet of a series. The number helps you find it and its neighbours."],
            ["Grid", "Numbered lines in squares. They give grid references to find places exactly."],
            ["Scale", "Links map distance to real distance, so you can measure distance and area."],
            ["North arrow", "Shows where north is, so you can give directions and bearings."],
            ["Key (legend)", "Explains every sign and colour used on the map."],
            ["Date and authority", "The date shows how up to date the map is. The authority is who made it, which shows how far to trust it."],
        ]),
        EX("Worked example 1: model answer", intro="State three items of marginal information found on a map and explain why each is important.", steps=[
            S("First item: the scale", text="The scale tells us how much real distance one centimetre on the map stands for. Without it we cannot work out the real distance between Mbanga and Nkolo, or the area of the forest."),
            S("Second item: the key", text="The key explains the signs and colours. Without it we would not know whether a black cross is a church or a grave, or whether green means forest or farms."),
            S("Third item: the date", text="The date shows when the map was made. A map printed many years ago may not show new roads or villages, so it may mislead a planner."),
        ]),
        TIP("Exam link: marginal information, signs and colours are tested in Paper 1 (five map-skills multiple-choice questions) and at the start of Paper 2 Section A, the compulsory map question. "
            "Questions often say 'state' or 'name', so short and exact answers earn the marks."),
        H("Conventional signs, symbols and colours"),
        T("A map is much smaller than the land it shows, so there is no room to draw a real church, a real bridge or a real school. "
          "Mapmakers use small pictures instead. They are called conventional signs."),
        D("**Conventional signs and symbols** are small agreed pictures, lines and patterns that stand for real features on a map. "
          "Their meanings are explained in the key.", title="Definition: conventional signs"),
        IMG("f5g-map-signs.svg",
            alt="List of the signs used on Mbanga Plain: roads, track, railway, river, bridge, built-up area, village, church, school, market, health centre, station, trig station, contour, forest and plantation",
            caption="Figure 3. Conventional signs used on the Mbanga Plain map."),
        T("Colour also carries meaning. Most topographic maps use the same colour family for the same kind of feature. "
          "Always check, because some maps change the colours."),
        IMG("f5g-map-colours.svg",
            alt="Six colour swatches: blue for water, green for vegetation, brown for relief, black for man-made features, red for main roads and built-up areas on some maps, white for open land",
            caption="Figure 4. What the main colours usually mean on a map."),
        EX("Worked example 2: reading signs from the key", intro="Look at Figure 1. (a) What is shown by the triangle with a dot on Ngoro Hill, and how high is it? (b) What is the small rectangle where the thick black road crosses the blue line? (c) What do the green circles in the south-west corner show?", steps=[
            S("(a) The triangle with a dot", text="The key shows that this sign is a trig station (a fixed survey point). The number beside it gives its height: 842 metres."),
            S("(b) The small rectangle on the road", text="It is the bridge sign. The tarred road crosses the River Mbo, the blue line, by a bridge."),
            S("(c) The green circles", text="Green stands for vegetation. The key shows that circles in a green box mean forest. This is Bakoa Forest."),
        ]),
        MISTAKE("Guessing signs and skipping the date and scale", "Never decide what a sign means from its colour or shape alone: a green area may be forest or plantation, and a dashed line may be a track or a boundary on other maps. Look in the key every time. Also check the date and scale before you use a map: an old map may miss new roads, and without the scale any distance you measure is meaningless."),
        QUIZ("Which item of marginal information tells you how up to date a map is?", ["The title", "The date", "The key", "The sheet number"], 1,
             "The date shows when the map was surveyed or printed, so it tells you how up to date it is.",
             hint="Think of the item that gives a year.",
             feedback=["The title only names the area.", "", "The key explains the signs and colours.", "The sheet number identifies the map in a series."]),
        QUIZ("A student sees a green area filled with small circles. What should she do first to be sure what it shows?",
             ["Guess that it is forest because green means vegetation", "Look it up in the key", "Measure it with a ruler", "Ignore it, because green is not important"], 1,
             "The key explains every sign and colour. Green means vegetation, but only the key tells you whether it is forest, plantation or farmland.",
             hint="Which part of the marginal information explains signs?",
             feedback=["Green does mean vegetation, but guessing the exact type can be wrong.", "", "Measuring tells you size, not what the sign is.", "The sign matters, because it shows a feature the question may ask about."],
             title="Quick check 2"),
        PQ("Define a map and give two reasons why maps are important.",
           "A map is a drawing of the whole or part of the earth's surface, seen from above, drawn to scale and using signs and symbols. "
           "Maps are important because they help people find the way (for example a driver travelling from Douala to Bamenda) and because planners use them to choose sites for roads, schools and health centres."),
        PQ("State four items of marginal information and say what each is used for.",
           "Title: names the area shown. Scale: lets you change map distance into real distance. North arrow: shows direction. Key: explains the signs and colours. "
           "(Also acceptable: sheet number, which identifies the sheet in a series; grid, which gives locations; date and authority, which show how recent and reliable the map is.)"),
        PQ("Give two conventional signs from the Mbanga Plain map and state the feature each stands for. Then state what the colours blue and green usually mean.",
           "A small black cross stands for a church, and a triangle with a dot stands for a trig station. A thick black line is a tarred road. "
           "Blue stands for water, for example the River Mbo. Green stands for vegetation, for example forest or plantation."),
        SUM("A **map** is a scale drawing of part of the earth's surface seen from above, using signs and symbols. Maps help us find the way, plan, study and record.",
            "**Marginal information** is the information in the margins: title, sheet number, grid, scale, north arrow, key, date and authority. Each helps you use the map.",
            "**Conventional signs** are agreed small pictures for real features, and the **key** explains them. Never guess a sign: check the key.",
            "Colours usually mean blue for water, green for vegetation, brown for relief and black for man-made features. Colours vary between maps, so read the key."),
    ],
))

# ------------------------------------------------------------------ 2. Grid lines and grid references
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Grid lines and grid references",
    slug="map-grid-lines-and-grid-references",
    minutes=20,
    summary="How eastings and northings form the grid, how to give four-figure and six-figure grid references (eastings first), and how to find a feature from its reference.",
    objectives=[
        "Define eastings, northings and a grid square",
        "Give the four-figure grid reference of a grid square",
        "Illustrate the position of a feature with a six-figure grid reference",
        "Identify a feature on the map from a given grid reference",
    ],
    key_concepts=["Grid lines", "Eastings", "Northings", "Grid square", "Four-figure reference", "Six-figure reference"],
    blocks=[
        H("Introduction"),
        T("Suppose a hiker is hurt on Mount Cameroon and the rescue team asks, 'Where are you?' Saying 'near the big rock' is not good enough. "
          "The team needs an exact place that anyone with the same map can find."),
        T("A map solves this with a **grid**: a network of numbered lines drawn over the map. It works like a house address. "
          "The grid reference tells you exactly where a feature is, or lets you find a feature when you are given its reference."),
        D("**Grid lines** are equally spaced, numbered lines drawn on a map at right angles to each other. They form a pattern of **grid squares**. "
          "**Eastings** are the vertical lines, and their numbers rise towards the east (right). "
          "**Northings** are the horizontal lines, and their numbers rise towards the north (up).", title="Definition: grid"),
        IMG("f5g-map-grid-lines.svg",
            alt="A grid with eastings 33 to 38 across the top and northings 54 to 58 down the side, with the grid square 3455 highlighted and arrows marked 1 along and 2 up",
            caption="Figure 1. Eastings run up the map and are read along the edge. Northings run across the map and are read up the edge."),
        KEY("A rhyme to remember", "Always give the easting first.", cards=[
            ["Along the corridor", "Read the easting first: find the vertical line and go along the edge."],
            ["Then up the stairs", "Read the northing second: then go up to find the horizontal line."],
        ]),
        H("Four-figure grid references"),
        T("A **four-figure grid reference** names a whole grid square. The first two figures are the easting. The last two figures are the northing. Use the lines on the **left** and **below** the feature: the line to the left gives the easting, and the line below gives the northing. "
          "On our practice map the squares are 1 km by 1 km, so a four-figure reference points to a square one kilometre wide."),
        IMG("f5g-map-mbanga-plain.svg",
            alt="The fictitious Mbanga Plain map with numbered eastings 31 to 38 and northings 52 to 58, used for the grid reference examples",
            caption="Figure 2. Mbanga Plain again. Use it for the examples and the practice questions."),
        EX("Worked example 1: four-figure reference", intro="Give the four-figure grid reference of the grid square that contains the church in Mbanga (Figure 2).", steps=[
            S("Find the easting", text="The church lies between easting lines 34 and 35. The line on its left is 34. Write 34 first."),
            S("Find the northing", text="The church lies between northing lines 55 and 56. The line below it is 55. Write 55 second."),
            S("Join the two numbers", math=r"\text{Grid reference} = 3455", text="Easting first, then northing."),
        ]),
        H("Six-figure grid references"),
        T("A four-figure reference is not very exact. Many features can lie in the same square. "
          "A **six-figure grid reference** gives the position of a point to within a hundred metres."),
        T("To give one, imagine each side of the square divided into **tenths**. Estimate how many tenths the feature is along from the left line. That is the third figure of the easting. "
          "Then estimate how many tenths it is up from the bottom line. That is the third figure of the northing."),
        D("A **six-figure grid reference** has three figures for the easting (the two-figure line number and the tenths along), followed by three figures for the northing (the two-figure line number and the tenths up).",
          title="Definition: six-figure reference"),
        IMG("f5g-map-six-figure.svg",
            alt="One grid square from easting 34 to 35 and northing 55 to 56 divided into tenths, with the church 3 tenths along and 4 tenths up, giving 343554",
            caption="Figure 3. One grid square divided into tenths. The church is 3 tenths along and 4 tenths up, so its reference is 343554."),
        EX("Worked example 2: six-figure reference", intro="Give the six-figure grid reference of the church in Mbanga.", steps=[
            S("Easting", text="The church is on the left of easting line 35, in the square that starts at 34. It is 3 tenths of the way along. The easting is 343."),
            S("Northing", text="The church is above northing line 55. It is 4 tenths of the way up. The northing is 554."),
            S("Join them", math=r"\text{Grid reference} = 343554"),
        ]),
        EX("Worked example 3: finding a feature from its reference", intro="What feature is at grid reference 369569?", steps=[
            S("Split the reference", text="Easting 369: line 36 and 9 tenths along. Northing 569: line 56 and 9 tenths up."),
            S("Find the point", text="Go along to line 36, then 9 tenths of the way towards 37. Go up from line 56 by 9 tenths."),
            S("Name the feature", text="At this point on Ngoro Hill there is a triangle with a dot: the trig station, 842 metres high."),
        ]),
        T("When a feature sits exactly on a grid line, the tenths figure is zero and you must still write it. The railway station is on easting line 36, so its easting is 360, not 36."),
        TIP("Exam link: Paper 2 Section A can ask 'give the six-figure grid reference of ...' and 'name the feature at grid reference ...'. Paper 1 can ask the same in multiple-choice form. "
            "Estimate the tenths carefully, and never swap the easting and the northing."),
        MISTAKE("Swapping the order", "Writing the northing before the easting gives a different place. Remember: along the corridor, then up the stairs. Easting always comes first."),
        MISTAKE("Using the wrong lines or dropping a zero", "Use the line on the left and the line below the feature, not the ones on the right or above. If the tenths figure is 0, keep it: 360 is correct, 36 is not."),
        QUIZ("A school lies between easting lines 52 and 53 and between northing lines 71 and 72. What is its four-figure grid reference?",
             ["7152", "5271", "5372", "5272"], 1,
             "The easting comes first, using the line on the left (52). The northing comes second, using the line below (71). The reference is 5271.",
             hint="Take the line on the left and the line below. Which number goes first?",
             feedback=["The numbers are in the wrong order: this puts the northing first.", "", "This uses the lines on the right and above (53 and 72).", "The easting is right but the northing uses the line above (72) instead of the line below (71)."]),
        QUIZ("A bridge is 4 tenths of the way from easting line 63 to line 64, and 7 tenths of the way up from northing line 28 to line 29. What is the six-figure reference?",
             ["637284", "428637", "634287", "634278"], 2,
             "Easting: 63 and 4 tenths gives 634. Northing: 28 and 7 tenths gives 287. Write them together: 634287.",
             hint="Write the easting as 63 followed by the tenths, then the northing as 28 followed by the tenths.",
             feedback=["The tenths have been swapped: 3 tenths should be 4, and 4 should be 7.", "The northing has been put first.", "", "The northing is wrong: 28 followed by 7 tenths is 287, not 278."],
             title="Quick check 2"),
        PQ("Define the terms easting and northing. Which one do we write first in a grid reference?",
           "Eastings are the vertical grid lines, numbered so that the numbers rise to the east. Northings are the horizontal grid lines, numbered so that the numbers rise to the north. "
           "The easting is always written first, then the northing."),
        PQ("Using Figure 2, give the four-figure grid reference of the square that contains Nkolo village.",
           "Nkolo lies between easting lines 37 and 38, so the easting is 37. It lies between northing lines 52 and 53, so the northing is 52. The reference is 3752."),
        PQ("Using Figure 2, give the six-figure grid references of (a) the railway station and (b) the health centre.",
           "(a) The railway station is exactly on easting line 36 (0 tenths) and 3 tenths above northing line 55. The reference is 360553. "
           "(b) The health centre is 6 tenths along from line 37 and 1 tenth above line 55. The reference is 376551."),
        PQ("Using Figure 2, name the feature at grid reference 346549. Then explain why a six-figure reference is better than a four-figure reference for finding it.",
           "At 346549 there is the market, a circle with the letter M, in the south of Mbanga town. A four-figure reference (3454) gives a whole square 1 km by 1 km, which could hold many features. "
           "A six-figure reference gives the position to within about 100 metres, so the feature is easy to find."),
        SUM("**Eastings** are vertical grid lines and **northings** are horizontal grid lines. Grid squares are formed where they cross.",
            "A **four-figure reference** names a square. Use the line on the left (easting) and the line below (northing), easting first.",
            "A **six-figure reference** adds tenths: easting line and tenths along, then northing line and tenths up. It is accurate to about 100 m on our map.",
            "To find a feature from a reference, go along to the easting, then up to the northing. Never swap the order, and keep a zero tenths figure."),
    ],
))

# ------------------------------------------------------------------ 3. Directions and bearings
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Directions and bearings",
    slug="map-directions-and-bearings",
    minutes=22,
    summary="The 16 points of the compass, how to measure a true bearing as a three-figure angle clockwise from north, and how to find a back bearing by adding or subtracting 180.",
    objectives=[
        "State the direction of one place from another using the 16 points of the compass",
        "Define a true bearing and write it with three figures",
        "Calculate the bearing of one point from another using a protractor on the map",
        "Calculate a back bearing by adding or subtracting 180 degrees",
    ],
    key_concepts=["Compass points", "True bearing", "North line", "Bearing of B from A", "Back bearing"],
    blocks=[
        H("Introduction"),
        T("A ship leaving the port of Douala is told which course to steer. A pilot flying to Maroua is told which way to point the aircraft. "
          "A surveyor in the Western Highlands has to say exactly where a tower stands from a hill. They all use **directions** and **bearings**. "
          "On a map, **north** is usually at the top, and the north arrow confirms it. From north we can describe every other direction."),
        H("Compass points"),
        T("There are four **cardinal points**: north (N), east (E), south (S) and west (W). Halfway between them are the four **intermediate points**: north-east (NE), south-east (SE), south-west (SW) and north-west (NW). "
          "Splitting again gives the **16 points of the compass**, such as north-north-east (NNE) and east-north-east (ENE)."),
        IMG("f5g-map-compass-16.svg",
            alt="Compass with the 16 points from N, NNE, NE, ENE, E and so on around the circle, with the bearings 000, 045, 090, 135, 180, 225, 270 and 315 marked for the eight main points",
            caption="Figure 1. The 16 points of the compass. Each point is 22.5 degrees from the next."),
        H("True bearings"),
        T("Compass points are not exact enough for surveying and navigation. A **bearing** gives the direction as an angle."),
        D("A **true bearing** is the angle, measured **clockwise from north**, between the north line at the starting point and the line joining the starting point to the other place. "
          "It is written with **three figures**, from 000° to 360°.", title="Definition: true bearing"),
        T("The main points have these bearings: N is 000°, NE is 045°, E is 090°, SE is 135°, S is 180°, SW is 225°, W is 270° and NW is 315°. "
          "Notice that every bearing has three figures, so 45° is written 045°."),
        KEY("Measuring a bearing with a protractor", "Follow these steps in order.", cards=[
            ["1. Join the points", "Draw a straight line from the starting point (A) to the other point (B)."],
            ["2. Draw the north line", "At A, draw or follow a line pointing north, parallel to a grid line (eastings)."],
            ["3. Place the protractor", "Put its centre on A and its zero line along the north line."],
            ["4. Read clockwise", "Read the angle from north, going round clockwise to the line AB. Write three figures."],
        ]),
        IMG("f5g-map-bearings.svg",
            alt="The Mbanga Plain map with four points marked: P at the church in Mbanga, Q at the trig station on Ngoro Hill, R at Tanjo and S at Nkolo, with dashed lines from P to Q, R and S and a dotted north line at P",
            caption="Figure 2. Points P (the church in Mbanga), Q (the trig station), R (Tanjo) and S (Nkolo) on the practice map."),
        EX("Worked example 1: bearing of Q from P", intro="Find the bearing of the trig station Q from the church P (Figure 2).", steps=[
            S("Start at P", text="'The bearing of Q from P' means we stand at P and look at Q. P is the starting point."),
            S("Use the north line at P", text="Q lies to the north-east of P, so the bearing must be between 000° and 090°."),
            S("Measure clockwise", text="Place the protractor at P with zero on the north line. The line PQ crosses the scale at 60°."),
            S("Write three figures", math=r"\text{Bearing of Q from P} = 060^\circ"),
        ]),
        TIP("Check with the grid. Q is 2.6 km east and 1.5 km north of P. If you know trigonometry, the angle from north is the angle whose tangent is 2.6 divided by 1.5. This is 60°, so the measured answer is right."),
        EX("Worked example 2: a bearing larger than 180°", intro="Find the bearing of Tanjo R from the church P.", steps=[
            S("Find the quarter", text="R lies to the north-west of P, so the bearing is between 270° and 360°."),
            S("Measure the small angle", text="The angle between the north line and PR, measured to the left (anticlockwise), is about 56°."),
            S("Convert to a clockwise bearing", math=r"360^\circ - 56^\circ = 304^\circ", text="A bearing is always measured clockwise, so we take the small angle away from 360°."),
            S("Write three figures", math=r"\text{Bearing of R from P} = 304^\circ"),
        ]),
        H("Back bearings"),
        T("Now stand at Q and look back at P. The direction has changed. The bearing of P from Q is called the **back bearing** of the bearing of Q from P."),
        IMG("f5g-map-bearing-back.svg",
            alt="Two points A and B with north lines at each. The bearing of B from A is 060 degrees and the bearing of A from B is 240 degrees",
            caption="Figure 3. The bearing of B from A is 060°. The bearing of A from B is 240°, which is 060 plus 180."),
        D("The **back bearing** is the bearing of the first point from the second. To find it, **add 180°** to the bearing if it is less than 180°, "
          "or **subtract 180°** if it is 180° or more.", title="Rule: back bearing", note="The rule works because the north lines at both points are parallel, so the two directions are exactly opposite, half a turn (180°) apart."),
        EX("Worked example 3: back bearings", intro="Find the bearing of P from each of Q, R and S, given that the bearings of Q, R and S from P are 060°, 304° and 136°.", steps=[
            S("Bearing of P from Q", math=r"060^\circ + 180^\circ = 240^\circ", text="The bearing is below 180°, so add 180°."),
            S("Bearing of P from R", math=r"304^\circ - 180^\circ = 124^\circ", text="The bearing is above 180°, so subtract 180°."),
            S("Bearing of P from S", math=r"136^\circ + 180^\circ = 316^\circ", text="The bearing is below 180°, so add 180°."),
        ]),
        TIP("Exam link: Paper 2 Section A can ask for the bearing of one named place from another, often with a protractor. Paper 1 asks for compass directions and for back bearings in multiple-choice form. "
            "Always draw the north line at the starting point first. A degree or two of measuring error is normal, so be as careful as you can."),
        MISTAKE("Measuring from the wrong end, anticlockwise, or with fewer than three figures", "The bearing of Q from P starts at P. If you measure at Q you get the back bearing, 180° different, so underline the place after 'from' and begin there. Bearings go clockwise from north: if the line is to the left of north, subtract the small angle from 360°. Always write three figures: 45° is wrong, 045° is right."),
        QUIZ("What is the bearing of due south-west?", ["135°", "180°", "225°", "315°"], 2,
             "South is 180° and west is 270°. South-west is halfway between them, which is 225°.",
             hint="South-west lies halfway between 180° and 270°.",
             feedback=["135° is south-east.", "180° is due south.", "", "315° is north-west."]),
        QUIZ("The bearing of Y from X is 075°. What is the bearing of X from Y?", ["105°", "255°", "285°", "075°"], 1,
             "The back bearing is 075° + 180° = 255°.",
             hint="The bearing is below 180°, so you add something.",
             feedback=["105° comes from taking 75° away from 180°, which is not the rule.", "", "285° comes from taking 75° away from 360°. That gives an anticlockwise angle.", "The bearing changes: it cannot be the same."],
             title="Quick check 2"),
        PQ("Name the five compass points that lie between north and east, in order, starting with north.",
           "North (N), north-north-east (NNE), north-east (NE), east-north-east (ENE), east (E)."),
        PQ("Define a true bearing. Give the compass direction and the three-figure bearing of due south-west.",
           "A true bearing is the angle measured clockwise from north, from the north line at the starting point to the line joining the two places, written with three figures. "
           "Due south-west is 225°, because it lies halfway between south (180°) and west (270°)."),
        PQ("Using Figure 2, state the compass direction of Nkolo (S) from the church (P) and the bearing of S from P. Then give the bearing of P from S.",
           "Nkolo lies to the south-east of the church. The bearing of S from P is about 136°. The back bearing is 136° + 180° = 316°."),
        PQ("A ship leaves port on a bearing of 125°. On what bearing must it sail to return to the port in a straight line?",
           "The back bearing is 125° + 180° = 305°."),
        SUM("Direction is described with the **16 points of the compass**. N, NE, E, SE, S, SW, W and NW are 45° apart.",
            "A **true bearing** is measured **clockwise from north** at the starting point and written with three figures (000° to 360°).",
            "For the bearing of B from A, stand at A: draw the north line at A, place the protractor on A and read clockwise to B.",
            "The **back bearing** is the bearing plus or minus 180°: add if less than 180°, subtract if 180° or more."),
    ],
))

# ------------------------------------------------------------------ 4. Scale, distance and area
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Scale, distance and area on a map",
    slug="map-scale-distance-and-area",
    minutes=25,
    summary="The three ways of showing scale, converting between them, measuring straight and winding distances (the string method), and finding area from grid squares and from map areas.",
    objectives=[
        "Identify the statement, representative fraction and linear (bar) forms of scale",
        "Convert a scale from one form to another",
        "Measure straight-line and winding distances on a map and convert them to kilometres",
        "Calculate the area of a feature from grid squares and from its size on the map",
    ],
    key_concepts=["Scale", "Statement of scale", "Representative fraction", "Linear (bar) scale", "String method", "Area from grid squares"],
    blocks=[
        H("Introduction"),
        T("A trader in Bafoussam wants to know how far it is to Bamenda before she hires a lorry. A farmer near Mbanga wants to know how big a field is before he plants. "
          "A map can answer both questions, but only if we understand its **scale**."),
        D("The **scale** of a map is the relationship between a distance on the map and the same distance on the ground.", title="Definition: scale"),
        IMG("f5g-map-scale-forms.svg",
            alt="Three ways to show the same scale: statement, 1 cm on the map is 0.5 km on the ground; representative fraction 1 to 50 000; and a bar scale from 0 to 3 km",
            caption="Figure 1. The same scale shown in three forms (statement, representative fraction and bar scale)."),
        KEY("The three forms of scale", "All three can describe the same map.", cards=[
            ["Statement of scale", "Words: '1 cm on the map represents 0.5 km on the ground', or '2 cm to 1 km'."],
            ["Representative fraction (RF)", "A ratio with no units: 1:50 000 means 1 unit on the map is 50 000 of the same units on the ground."],
            ["Linear (bar) scale", "A line marked in kilometres. You can measure straight against it with a ruler or strip of paper."],
        ], note="A scale such as 1:25 000 is a larger scale than 1:100 000, because its fraction is larger. A larger scale shows a smaller area with more detail. A small scale, such as 1:1 000 000, shows a very large area with little detail."),
        H("Converting between forms"),
        EX("Worked example 1: representative fraction to statement", intro="Express the scale 1:50 000 as a statement of scale.", steps=[
            S("Read the ratio", text="1 cm on the map stands for 50 000 cm on the ground. Remember: 1 m is 100 cm, and 1 km is 1000 m, so 1 km is 100 000 cm."),
            S("Change centimetres to metres", math=r"50\,000 \div 100 = 500 \text{ m}"),
            S("Change metres to kilometres", math=r"500 \div 1000 = 0.5 \text{ km}"),
            S("Write the statement", text="1 cm on the map represents 0.5 km on the ground. This is the same as 2 cm to 1 km."),
        ]),
        EX("Worked example 2: statement to representative fraction", intro="Express the statement '2 cm to 1 km' as a representative fraction.", steps=[
            S("Change the ground distance to centimetres", math=r"1 \text{ km} = 100\,000 \text{ cm}"),
            S("Make the map distance 1 cm", math=r"100\,000 \div 2 = 50\,000", text="2 cm on the map stands for 100 000 cm, so 1 cm stands for 50 000 cm."),
            S("Write the RF", math=r"\text{RF} = 1 : 50\,000"),
        ]),
        H("Measuring distance"),
        T("For a **straight-line distance** use a ruler. Measure in centimetres, then multiply by the number of kilometres that 1 cm stands for. "
          "Or lay a strip of paper along the line, mark its ends and compare it with the bar scale."),
        EX("Worked example 3: a straight-line distance", intro="Two villages are 7.4 cm apart on a map of scale 1:50 000. What is the real distance?", steps=[
            S("Find what 1 cm stands for", text="At 1:50 000, 1 cm stands for 0.5 km."),
            S("Multiply", math=r"7.4 \times 0.5 = 3.7 \text{ km}"),
            S("Write the answer", text="The real distance is 3.7 km."),
        ]),
        T("Roads and rivers bend. For a **winding distance** use the **string method**: lay a piece of thread along the road or river, following every bend. "
          "Mark where it starts and ends, straighten the thread, and measure it with a ruler or against the bar scale."),
        IMG("f5g-map-string-method.svg",
            alt="A winding murram road from A to E on the left and the same road laid out as a straight string of 4 km beside a scale bar on the right; the straight line from A to E is shown dashed and is shorter",
            caption="Figure 2. The string method. The winding road is 4.0 km long. The straight line A to E is only about 3.4 km."),
        EX("Worked example 4: winding and straight distances", intro="The murram road from the junction A in Mbanga to Nkolo village E (Figure 2) measures 8.0 cm when the string is straightened. The straight line from A to E is 6.8 cm. The scale is 1:50 000. Find both distances.", steps=[
            S("Winding distance", math=r"8.0 \times 0.5 = 4.0 \text{ km}", text="This is the distance a traveller drives along the road."),
            S("Straight-line distance", math=r"6.8 \times 0.5 = 3.4 \text{ km}", text="This is the distance 'as the crow flies'."),
            S("Compare", text="The road is 0.6 km longer than the straight line because of its bends."),
        ]),
        H("Measuring area"),
        T("On a map with a grid, the easiest way to find area is to **count grid squares**. The side of each square on the printed practice map is 2 cm. "
          "At 1:50 000, 2 cm stands for 1 km, so each square is 1 km by 1 km. Each square has a real area of **1 km²**."),
        IMG("f5g-map-area-squares.svg",
            alt="Bakoa Forest Reserve drawn over grid squares: three whole squares numbered 1, 2 and 3 and one half square, giving a total of 3.5 squares and an area of 3.5 square kilometres",
            caption="Figure 3. Counting squares: 3 whole squares and 1 half square make 3.5 km²."),
        EX("Worked example 5: area from grid squares", intro="Find the area of Bakoa Forest Reserve on the Mbanga Plain map (Figure 3).", steps=[
            S("Count the whole squares", text="Three whole squares are completely inside the forest."),
            S("Count the part squares", text="One square is cut by a diagonal. Half of it is forest, so it counts as 0.5. (Where pieces are more than half a square count 1, where they are less count 0, or join up pieces to make a whole square.)"),
            S("Add and convert", math=r"3 + 0.5 = 3.5 \text{ squares} \quad 3.5 \times 1 \text{ km}^2 = 3.5 \text{ km}^2"),
        ]),
        EX("Worked example 6: area from measurements", intro="On a map of scale 1:50 000 a rectangular farm measures 3 cm by 2 cm. Find its real area.", steps=[
            S("Change each side to kilometres", math=r"3 \times 0.5 = 1.5 \text{ km} \qquad 2 \times 0.5 = 1.0 \text{ km}"),
            S("Multiply length by width", math=r"1.5 \times 1.0 = 1.5 \text{ km}^2"),
            S("Check with the area shortcut", text="At 1:50 000, 1 cm² on the map is 0.5 km × 0.5 km = 0.25 km². The map area is 6 cm², and 6 × 0.25 = 1.5 km². The answers agree."),
        ]),
        TIP("Exam link: Paper 2 Section A always includes a scale question, such as 'the distance from X to Y' or 'the area of the forest'. Paper 1 asks for scale conversions in multiple-choice form. "
            "Show your working, give the unit (km or km²) and say whether the distance is straight or along a road."),
        MISTAKE("Wrong units, wrong squaring, or a straight line for a winding road", "To change cm to km you must divide by 100 000, not 1000. For area, squares matter: 1 cm² on a 1:50 000 map is 0.25 km² (0.5 × 0.5), not 0.5 km². If a question asks for the distance by road, a ruler along a straight line gives too small an answer, so use the string method for any bent line."),
        QUIZ("A map has the scale 1:100 000. How far on the ground does 1 cm on the map represent?", ["100 000 km", "10 km", "1 km", "100 m"], 2,
             "1 cm stands for 100 000 cm. Divide by 100 to get 1000 m, and that is 1 km.",
             hint="Change 100 000 cm into metres, then into kilometres.",
             feedback=["100 000 km is the number of centimetres, not kilometres.", "Dividing by 10 000 instead of 100 000 gives 10 km.", "", "100 m is only 10 000 cm."]),
        QUIZ("Which of these is the largest scale?", ["1:10 000", "1:50 000", "1:100 000", "1:1 000 000"], 0,
             "The larger the fraction, the larger the scale. 1/10 000 is bigger than the others, so 1:10 000 is the largest scale and shows the most detail.",
             hint="Compare the fractions: a smaller bottom number means a bigger fraction.",
             feedback=["", "1/50 000 is smaller than 1/10 000.", "1/100 000 is smaller still.", "This is the smallest scale of the four."],
             title="Quick check 2"),
        PQ("Express the scale 1:25 000 as a statement of scale.",
           "1 cm on the map stands for 25 000 cm. 25 000 ÷ 100 = 250 m, and 250 m = 0.25 km. So 1 cm on the map represents 0.25 km on the ground."),
        PQ("Express the statement '1 cm to 2 km' as a representative fraction.",
           "2 km = 2 × 100 000 = 200 000 cm. So 1 cm on the map stands for 200 000 cm on the ground. The RF is 1:200 000."),
        PQ("A winding road measures 12.5 cm along the string on a map of scale 1:50 000. Find its real length in kilometres.",
           "At 1:50 000, 1 cm stands for 0.5 km. The length is 12.5 × 0.5 = 6.25 km."),
        PQ("A lake covers an area of 12 cm² on a map of scale 1:50 000. Find its real area in square kilometres.",
           "1 cm² on the map stands for 0.5 km × 0.5 km = 0.25 km². The area is 12 × 0.25 = 3 km²."),
        SUM("**Scale** links map distance to ground distance. It is shown as a statement, a representative fraction (RF) or a linear (bar) scale.",
            "1 km is 100 000 cm. At 1:50 000, 1 cm stands for 0.5 km and 2 cm stands for 1 km. Convert by changing cm to metres, then km.",
            "Measure a straight line with a ruler. Measure a winding road or river with the **string method**, then multiply by km per cm.",
            "Area: count grid squares (each 1 km² on the practice map, whole squares plus halves) or use 1 cm² = 0.25 km² at 1:50 000. Give the unit km²."),
    ],
))

# ------------------------------------------------------------------ 5. Copying, reducing and enlarging
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Copying, reducing and enlarging a map",
    slug="map-copying-reducing-and-enlarging",
    minutes=22,
    summary="How to copy part of a map by the grid method, how to enlarge or reduce it, how the scale, lengths and areas change, and how to choose a new scale.",
    objectives=[
        "Describe the grid method of copying a section of a map",
        "Draw a copy of a map section at a different scale (enlarged or reduced) using a grid",
        "Calculate how scale, lengths and area change when a map is enlarged or reduced",
        "Choose a suitable new scale for a map that must fit a given space",
    ],
    key_concepts=["Copying a map", "Grid method", "Enlargement", "Reduction", "Enlargement factor", "Change of scale"],
    blocks=[
        H("Introduction"),
        T("A teacher in Bamenda wants a big copy of one part of a map for the classroom wall, so that every student can see the roads and the river. "
          "A farmers' cooperative wants a small copy of the same part to carry in a notebook. Both need to copy a section of a map at a different size."),
        D("**Copying** a map means redrawing part of it. **Enlarging** makes the copy bigger than the original. **Reducing** makes the copy smaller. "
          "In both cases the shape and the positions of the features must stay correct.", title="Definition: copy, enlarge, reduce"),
        T("There are several ways to do this. You can trace the map, use a photocopier or scanner, or use a drawing instrument called a pantograph. "
          "The method you need to know well is the **grid method**, which needs only a pencil and a ruler."),
        H("The grid method"),
        KEY("Steps of the grid method", "The key idea: the new grid has the same number of squares, but the squares are a different size.", cards=[
            ["1. Choose the section", "Mark the part of the map to copy, and note its grid squares or draw a grid over it."],
            ["2. Draw the new grid", "Draw a grid with the same number of rows and columns. For an enlargement, make the squares bigger. For a reduction, make them smaller."],
            ["3. Label the squares", "Give the rows and columns the same letters and numbers on both grids."],
            ["4. Copy square by square", "Look at where each line crosses the edge of a square, mark the same place on the new square, then join the marks."],
            ["5. Complete the map", "Add a title, the new scale, a key, a north arrow and the grid numbers."],
        ]),
        IMG("f5g-map-copy-enlarge.svg",
            alt="Before and after: a section of the Mbanga Plain map in a grid of 4 columns A to D and 3 rows 1 to 3 with squares of 2 cm at scale 1:50 000, and the same section enlarged with squares of 4 cm at scale 1:25 000",
            caption="Figure 1. Enlarging. The same 4 by 3 squares, but each square is twice as long and twice as wide. (The figure is not drawn to real size on your screen.)"),
        EX("Worked example 1: enlarging by a factor of 2", intro="A section of a 1:50 000 map is drawn over a grid of 4 columns by 3 rows with squares of 2 cm. It is to be enlarged so that every length is doubled. Describe the copy and give its new scale.", steps=[
            S("Choose the factor", text="Every length is doubled, so the enlargement factor is 2."),
            S("Draw the new grid", text="Use 4 columns and 3 rows again, but each square is 4 cm by 4 cm. The grid is 16 cm wide and 12 cm high."),
            S("Copy the features", text="The church is in square B2 on the original, so it goes in square B2 on the copy, at the same relative position inside the square."),
            S("Find the new scale", math=r"\text{New square} = 4 \text{ cm} = 1 \text{ km}, \quad \text{so } 1 \text{ cm} = 0.25 \text{ km}", text="1 cm on the copy stands for 0.25 km, which is 25 000 cm. The new scale is 1:25 000."),
        ]),
        IMG("f5g-map-copy-reduce.svg",
            alt="Before and after: the same Mbanga Plain section with squares of 2 cm at scale 1:50 000 and reduced to squares of 1 cm at scale 1:100 000",
            caption="Figure 2. Reducing. The same 4 by 3 squares, but each square is half as long and half as wide."),
        EX("Worked example 2: reducing to half size", intro="Reduce the same section so that every length is halved. Give the new grid and the new scale.", steps=[
            S("Choose the factor", text="Every length is halved, so the factor is one half."),
            S("Draw the new grid", text="Use 4 columns and 3 rows, with squares of 1 cm. The grid is 4 cm wide and 3 cm high."),
            S("Find the new scale", math=r"1 \text{ cm} = 1 \text{ km} = 100\,000 \text{ cm}", text="Each 1 cm square is still 1 km on the ground, so 1 cm stands for 1 km. The new scale is 1:100 000."),
        ]),
        H("How scale, length and area change"),
        T("The ground does not change. Only the drawing changes. If every length is multiplied by a number k (the **enlargement factor**), then:"),
        T("The new scale has a denominator that is the old denominator divided by k. A bigger map has a smaller number after the colon. "
          "A length on the map is multiplied by k. An area on the map is multiplied by k × k, which is k squared."),
        CODE("""Change             Lengths   Areas    New scale (from 1:50 000)
Enlarge by 2       x 2       x 4      1:25 000
Reduce to half     x 1/2     x 1/4    1:100 000
Enlarge by 2.5     x 2.5     x 6.25   1:20 000""", "text", title="Table 1. Changes when a map is enlarged or reduced"),
        EX("Worked example 3: the area of a lake", intro="A lake covers 6 cm² on a 1:50 000 map. The map is enlarged by a factor of 2. Find the area of the lake on the copy, and show that its real area has not changed.", steps=[
            S("Area on the copy", math=r"6 \times 2^2 = 6 \times 4 = 24 \text{ cm}^2"),
            S("Real area from the original", math=r"1 \text{ cm}^2 = 0.25 \text{ km}^2, \quad 6 \times 0.25 = 1.5 \text{ km}^2"),
            S("Real area from the copy", math=r"\text{At 1:25 000}, 1 \text{ cm}^2 = 0.0625 \text{ km}^2, \quad 24 \times 0.0625 = 1.5 \text{ km}^2", text="The real area is 1.5 km² on both maps. The copy is bigger, but the lake is the same lake."),
        ]),
        H("Choosing a new scale"),
        T("Sometimes you must fit an area on a page of a given size. Work out how big the area would be at each scale, and choose the **largest scale that still fits**."),
        EX("Worked example 4: choosing a scale", intro="An area 5 km wide and 3 km high must be drawn on a space 16 cm wide and 10 cm high. Which of the scales 1:25 000, 1:40 000, 1:50 000 and 1:100 000 is the largest that fits?", steps=[
            S("Try 1:25 000", text="1 cm stands for 0.25 km. The area is 5 ÷ 0.25 = 20 cm wide and 3 ÷ 0.25 = 12 cm high. It is too big."),
            S("Try 1:40 000", text="1 cm stands for 0.4 km. The area is 5 ÷ 0.4 = 12.5 cm wide and 3 ÷ 0.4 = 7.5 cm high. It fits."),
            S("Try 1:50 000", text="1 cm stands for 0.5 km. The area is 10 cm wide and 6 cm high. It fits, but 1:40 000 is larger and shows more detail."),
            S("Choose", text="The largest scale that fits is 1:40 000."),
        ]),
        TIP("Exam link: Paper 2 Section A may ask you to copy a section of the map, reduce or enlarge it with a given grid, and to include features such as a river, a road and a village. "
            "Mark every feature asked for, label them, and give the new scale and a title. Paper 1 asks about change of scale in multiple-choice form."),
        MISTAKE("Changing the scale the wrong way round", "A bigger map has a smaller scale denominator. Enlarging 1:50 000 by 2 gives 1:25 000, not 1:100 000. Divide the denominator when you enlarge, and multiply it when you reduce."),
        MISTAKE("Forgetting that area changes by the square", "If lengths double, the area becomes four times as big, not twice. Multiply by k × k. Also remember to use the same number of squares on both grids, and to redraw the scale bar and the scale for the copy."),
        QUIZ("A map of scale 1:50 000 is enlarged so that every length is doubled. What is the new scale?", ["1:100 000", "1:50 000", "1:25 000", "1:75 000"], 2,
             "Doubling the lengths makes 1 cm on the copy stand for half as much ground. The denominator is halved: 50 000 ÷ 2 = 25 000, so the scale is 1:25 000.",
             hint="Is a bigger map a larger scale or a smaller scale?",
             feedback=["This doubles the denominator, which would make a reduction.", "The scale changes when the map is enlarged.", "", "This number has no link to doubling."]),
        QUIZ("Every length on a map is made 3 times as long. By what number is the area of a lake on the map multiplied?", ["3", "6", "9", "27"], 2,
             "Area is length times width. Both are multiplied by 3, so the area is multiplied by 3 × 3 = 9.",
             hint="Area depends on two lengths.",
             feedback=["3 is the factor for lengths, not areas.", "6 comes from 3 + 3 or 3 × 2, which is not the rule.", "", "27 would be the factor for volume, not area."],
             title="Quick check 2"),
        PQ("Describe the grid method of enlarging part of a map.",
           "Mark the section to be copied and draw a grid over it, or use the map grid. Draw a new grid with the same number of rows and columns but larger squares. "
           "Label the rows and columns in the same way. Copy the features square by square, marking where each line crosses a square edge, then join the marks. "
           "Finish with a title, the new scale, a key and a north arrow."),
        PQ("A map section is 8 cm by 6 cm at a scale of 1:50 000. It is copied onto a grid with squares twice as long. State the size of the copy, its new scale, and the real size of the area.",
           "Each length is doubled, so the copy is 16 cm by 12 cm. The new scale is 50 000 ÷ 2 = 1:25 000. The real size is the same on both maps: 8 cm × 0.5 = 4 km by 6 cm × 0.5 = 3 km. "
           "Check: 16 cm × 0.25 = 4 km and 12 cm × 0.25 = 3 km."),
        PQ("A road measures 9.6 cm on a map of scale 1:50 000. The map is reduced to a scale of 1:100 000. Find the length of the road on the copy and its real length.",
           "The factor is 50 000 ÷ 100 000 = 1/2, so the road is 9.6 ÷ 2 = 4.8 cm on the copy. The real length is 9.6 × 0.5 = 4.8 km on the original, and 4.8 × 1 = 4.8 km on the copy. They are the same."),
        PQ("An area 4 km wide and 3 km high must be drawn on a space 10 cm wide and 9 cm high. Which of 1:25 000, 1:40 000 and 1:50 000 is the largest scale that fits? Give the size of the map.",
           "At 1:25 000 (0.25 km per cm) the map would be 16 cm by 12 cm, too big. At 1:40 000 (0.4 km per cm) it is 10 cm by 7.5 cm, which fits. At 1:50 000 it is 8 cm by 6 cm, which fits but is smaller. "
           "The largest scale that fits is 1:40 000, and the map is 10 cm by 7.5 cm."),
        SUM("The **grid method** copies a map section square by square. The new grid has the same number of squares, but the squares are bigger (enlargement) or smaller (reduction).",
            "If every length is multiplied by k, the new scale denominator is the old one divided by k. Enlarging 1:50 000 by 2 gives 1:25 000. Reducing to half gives 1:100 000.",
            "Lengths on the map are multiplied by k and areas by k squared, but the **real** distances and areas on the ground do not change.",
            "To fit a space, work out the map size at each scale and choose the largest scale that still fits. Always give a title, the new scale, a key and a north arrow."),
    ],
))
