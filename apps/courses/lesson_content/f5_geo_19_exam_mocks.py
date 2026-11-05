"""Form 5 Geography (O Level 0550): the Examination module, Paper 1 and Paper 2 (four lessons).

Draft content. The only exam facts stated are those of the Board's revised 0550 syllabus (see
docs/curriculum/GEOGRAPHY_0550_SOURCE.md): Paper 1 is 50 multiple-choice questions (map skills 5, physical 23,
human 22) in 1 hour 30 minutes for 35% of the marks, with no multiple-choice question on pure case studies except
on Cameroon; Paper 2 has seven essay and problem-solving questions, four answered, in 2 hours 30 minutes for 65%
(90 marks): Section A map reading (compulsory, 25% of the marks for the whole examination), B physical,
C human (examples from LICs, NICs and AICs), D Cameroon (one question answered from each of B, C and D).
Time plans, checklists and paragraph methods are KKEVO study advice, not official mark schemes. All maps
are fictitious. A reviewer must check the examples against the syllabus and textbooks.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

M_EXAM = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ 1. Paper 1 strategies
    lesson(
        module=M_EXAM, topic="Paper 1",
        title="Paper 1: multiple-choice strategies",
        slug="geoexam-paper-1-multiple-choice-strategies",
        minutes=22,
        summary="How Paper 1 is organised (50 questions: 5 map skills, 23 physical, 22 human), a time plan of about 1.8 "
                "minutes a question, the two-pass method, elimination, absolute words and the traps in similar terms.",
        objectives=[
            "Outline how Paper 1 is organised: number of questions, time, and the split between map skills, physical and human geography",
            "Explain the two-pass method and calculate the average time available for each question",
            "Describe how to eliminate wrong options and how to deal with words such as only, always and NOT",
            "Identify pairs of similar geographical terms that cause errors, such as weather and climate or weathering and erosion",
        ],
        key_concepts=["Paper 1", "Two-pass method", "Elimination", "Absolute words", "Distractor", "Map skills questions"],
        blocks=[
            H("Introduction"),
            T("Imagine a student in a school hall in Bafoussam. The invigilator says, \"You may begin.\" There are 50 "
              "multiple-choice questions on the paper and 90 minutes on the clock. Some questions look at a map. Some ask "
              "about the atmosphere or rocks. Some ask about farms, towns and Cameroon.\n\n"
              "Knowing geography is the first half of success. The second half is knowing how the paper is built and how to "
              "read its questions. This lesson teaches the second half."),
            D("Paper 1 has **50 multiple-choice questions**, and **all** of them are answered. The time allowed is "
              "**1 hour 30 minutes**. Paper 1 carries **35%** of the marks for the whole examination.",
              title="Paper 1: the official facts"),
            IMG("f5g-exam-paper1-split.svg",
                alt="A bar showing Paper 1: 5 questions on map skills, 23 on physical geography and 22 on human geography.",
                caption="Figure 1. The 50 questions of Paper 1, as set out in the Board's syllabus."),
            T("The syllabus says how the 50 questions are shared. **Map skills** has 5 questions. **Physical geography** has 23. "
              "**Human geography** has 22.\n\n"
              "There is one more rule. **No multiple-choice question is set on pure case studies, except on Cameroon.** "
              "So a question will not ask you for the details of a farm in another continent. But it can ask you for "
              "facts about Cameroon, such as a regional capital, a river or a port. Revise the Cameroon facts."),
            TIP("**Exam link.** This lesson is about Paper 1 (multiple choice). The map skills questions use the same skills as "
                "Paper 2 Section A, so practise reading grid references, bearings and scale in both papers.",
                title="Where this appears"),
            H("Time: about 1.8 minutes a question"),
            T("90 minutes divided by 50 questions is **1.8 minutes** for each question, a little less than two minutes. "
              "Some questions take 20 seconds. A calculation or a map question may take three minutes. The aim is to "
              "keep to the average and never to get stuck."),
            IMG("f5g-exam-twopass.svg",
                alt="A timeline of 90 minutes divided into Pass 1 up to 55 minutes, Pass 2 up to 80 minutes and a final check.",
                caption="Figure 2. A suggested plan for the 90 minutes (KKEVO study advice, not an official rule)."),
            KEY("The two-pass method",
                "Go through the paper twice. The first pass collects the marks that are easy to get. The second pass uses the "
                "time that is left for the hard questions.",
                cards=[["Pass 1 (about 55 minutes)", "Answer every question you can do quickly. If you are not sure after about a minute, mark it with a tick and move on."],
                       ["Pass 2 (about 25 minutes)", "Go back to the ticked questions. Use elimination. Choose the best answer."],
                       ["Check (about 10 minutes)", "Make sure every question has an answer. Re-read questions with NOT, only or always."]]),
            H("Reading a question and eliminating options"),
            D("The **stem** is the question or the unfinished sentence. The **key** is the one correct option. "
              "The **distractors** are the wrong options. A good distractor looks attractive because it contains a "
              "true fact, or a common mistake, but it does not answer this question.",
              title="Stem, key and distractors"),
            T("Do not look for the right answer straight away. First read the stem slowly and cover the options. "
              "Say the answer in your head. Then look at the options and find the one that matches.\n\n"
              "If you cannot say the answer, use **elimination**. Cross out options that you can prove wrong. Often only two "
              "are left. Then ask which of the two answers the stem better."),
            EX("Worked example 1: elimination", intro="Which of these is the best definition of weathering?  "
               "A. The wearing away of rock by a moving river.  B. The breaking down of rock where it lies, with little "
               "or no movement.  C. The carrying of rock fragments by wind.  D. The dropping of sediment when a river slows down.",
               steps=[
                   S("Say the answer first", text="Weathering means the breaking down of rock in place. Rock is cracked or rotted where it lies."),
                   S("Cross out distractors", text="A says 'wearing away by a river': that is erosion, and it involves movement. C says 'carrying': that is transport. D says 'dropping': that is deposition."),
                   S("Choose", text="Only B says 'where it lies, with little or no movement'. The answer is B."),
               ]),
            H("Absolute words, NOT and diagrams"),
            KEY("Words that need care",
                "A few small words can change the whole meaning of a question or an option.",
                cards=[["Absolute words", "Only, always, never, all, none, every: an option with one of these is often too strong. Ask: can I think of one exception?"],
                       ["NOT and EXCEPT", "Underline the word. You are looking for the one false statement, not the true ones."],
                       ["Superlatives", "Largest, highest, main, best: check that your choice is truly the most, not just a big one."],
                       ["Maps and diagrams", "Read the title, key and scale before the options. Check units (km or m) and where north is. Use the figure, not memory."]]),
            EX("Worked example 2: a scale question",
               intro="On a map of scale 1 : 50 000 the distance between two villages measures 6 cm. What is the real distance?  "
                     "A. 0.3 km   B. 3 km   C. 30 km   D. 300 km",
               steps=[
                   S("Meaning of the scale", text="1 : 50 000 means that 1 cm on the map stands for 50 000 cm on the ground."),
                   S("Multiply", math=r"6 \times 50\,000 = 300\,000 \text{ cm}"),
                   S("Change units", text="100 000 cm make 1 km, so 300 000 cm is 3 km. The answer is B."),
                   S("Check with the wrong options", text="A, C and D are wrong by a factor of 10 or more. Estimate: 6 cm is a short distance, and 2 cm on this map is 1 km, so 6 cm is 3 km."),
               ]),
            H("Traps in similar terms"),
            CODE("Term                What it means\n"
                 "weather             the state of the air now or today\n"
                 "climate             the average weather over many years\n"
                 "weathering          rock breaks down where it lies\n"
                 "erosion             rock is worn away and carried\n"
                 "rotation            the Earth spins on its axis (one day)\n"
                 "revolution          the Earth orbits the Sun (one year)\n"
                 "latitude            distance north or south of the equator\n"
                 "longitude           distance east or west of Greenwich\n"
                 "site                the land a settlement stands on\n"
                 "situation           where it is in relation to other places",
                 "text", title="Pairs to learn: a distractor often uses the other word of the pair"),
            QUIZ("Which word describes the average weather of a place over many years?",
                 ["Weather", "Climate", "Weathering", "Season"], 1,
                 "Climate is the average of the weather over a long time.",
                 hint="One of these words is about the state of the air today; another is about many years.",
                 feedback=["Weather is the state of the air at a time, such as rain today.", "",
                           "Weathering is the breaking down of rock, not an atmosphere word.",
                           "A season is a part of the year, not the long-term average."]),
            MISTAKE("Choosing an option because it is true",
                    "An option can be a true fact and still be wrong for this question. Always ask: does this option answer the "
                    "stem? A distractor often states something that is correct, but about a different topic."),
            QUIZ("An option says 'Rainforest soils are always very fertile.' What is the best first reaction?",
                 ["Choose it because it is about rainforests", "Be careful: the word 'always' may make it too strong", "Cross out the stem", "Choose it because it is long"], 1,
                 "Absolute words such as always and never are often too strong. Check if you can think of an exception.",
                 hint="Look at the single word 'always'.",
                 feedback=["The topic matching is not enough. Check every word.", "",
                           "The stem is the question. Keep it and use it.", "The length of an option does not make it right."]),
            PQ("Paper 1 is 50 questions in 90 minutes. Calculate the average time for each question, and say how many minutes remain "
               "for the last 20 questions if you finish the first 30 in 50 minutes.",
               "Average: 90 divided by 50 = 1.8 minutes. After 30 questions in 50 minutes, 40 minutes remain (90 minus 50) for 20 "
               "questions, which is 2 minutes for each. You have gained time on the first part."),
            PQ("State the three groups of questions in Paper 1 and the number of questions in each.",
               "Map skills: 5. Physical geography: 23. Human geography: 22. The total is 50."),
            PQ("A stem reads 'Which of the following is NOT a renewable source of power?' Explain how you would answer it.",
               "Underline NOT. Test each option as a source and decide if it is renewable (for example solar, wind, hydro) or not (for "
               "example coal, oil, natural gas). Three options will be renewable. The one that is not renewable is the answer."),
            PQ("Rotation and revolution are often mixed up. State the difference and one effect of each.",
               "Rotation is the Earth spinning on its axis in about 24 hours; it causes day and night. Revolution is the Earth moving "
               "round the Sun in about a year; with the tilt of the axis it causes the seasons."),
            SUM("Paper 1: 50 multiple-choice questions, all answered, 1 hour 30 minutes, 35% of the marks. Split: map skills 5, physical 23, human 22.",
                "No multiple-choice question is set on pure case studies, except on Cameroon, so revise Cameroon facts.",
                "About 1.8 minutes a question. Use two passes: easy marks first, ticked questions second, then a check.",
                "Say the answer before reading the options. Eliminate options you can prove wrong.",
                "Watch absolute words, NOT, and pairs of similar terms such as weather and climate or weathering and erosion."),
        ],
    ),

    # ------------------------------------------------------------------ 2. The map reading question
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2: the compulsory map reading question",
        slug="geoexam-paper-2-the-map-reading-question",
        minutes=25,
        summary="Section A of Paper 2 is compulsory and carries 25% of the marks for the whole examination. Learn a six-step "
                "method with grid references, scale, bearings, describing relief and drainage, and linking nature to people.",
        objectives=[
            "Outline the six steps for answering the compulsory map reading question",
            "Calculate distances from a scale and measure bearings between places on a map",
            "Describe relief and drainage using contours, spot heights and grid references as evidence",
            "Explain how physical features influence settlement and land use, using the map as evidence",
        ],
        key_concepts=["Section A", "Grid reference", "Scale", "Bearing", "Relief", "Drainage", "Land use", "Evidence from the map"],
        blocks=[
            H("Introduction"),
            T("In Paper 2 you must answer **one question that nobody can skip**: the map reading and interpretation question. "
              "Whatever other questions you choose, you must answer this one.\n\n"
              "Think of a student from Kumba holding a map of an unfamiliar district. She must find places, measure distances, "
              "describe the hills and rivers, and explain why a town stands where it does. All of that is on the map. "
              "This lesson shows a method for getting the marks."),
            D("Paper 2 has seven essay and problem-solving questions. Four are answered. **Section A, Map Reading and "
              "Interpretation**, has one question and it is **compulsory**. It carries **25% of the total marks for the whole "
              "examination**. You then answer one question from each of Sections B, C and D.",
              title="Section A: the official facts"),
            IMG("f5g-exam-paper2-structure.svg",
                alt="Four boxes: Section A map reading (one question, compulsory) and Sections B, C and D (two questions each, answer one).",
                caption="Figure 1. The structure of Paper 2, as set out in the Board's syllabus."),
            TIP("**Exam link.** Section A is the map reading question of Paper 2. The same skills are tested in the 5 map skills "
                "questions of Paper 1. A strong Section A is worth a quarter of all the marks, so practise it every week.",
                title="Where this appears"),
            H("Six steps"),
            IMG("f5g-exam-map-steps.svg",
                alt="Six boxes in order: read the whole question, study the key scale and grid, locate, measure, describe, link.",
                caption="Figure 2. A six-step method (KKEVO study advice)."),
            T("**Step 1.** Read the whole question before you start. Later parts may help you with earlier ones.\n\n"
              "**Step 2.** Study the key, the scale and the grid lines. Find north.\n\n"
              "**Step 3.** Locate places with grid references. **Step 4.** Measure distances and bearings.\n\n"
              "**Step 5.** Describe relief, drainage, settlement and land use. **Step 6.** Link nature to people: explain "
              "how the physical features affect what people do."),
            H("The skills you need"),
            D("A **grid reference** gives the position of a place. Read **eastings first** (the numbers along the top or "
              "bottom), then **northings** (the numbers up the side). A four-figure reference names a square. In a "
              "six-figure reference the third and sixth digits are tenths of a square.",
              title="Grid references", note="Remember: along the corridor, then up the stairs."),
            KEY("Distance, bearing and direction",
                "Three skills that you will use in nearly every map question.",
                cards=[["Distance", "Measure with the edge of a paper strip and compare it with the scale bar. Or use ground distance = map distance times the scale."],
                       ["Bearing", "A bearing is an angle measured clockwise from north, written with three figures, such as 062 degrees. The bearing back is 180 degrees different."],
                       ["Direction", "Use eight points: N, NE, E, SE, S, SW, W, NW. Write 'south-west' as the direction of the river's flow, never just 'down'."]]),
            CODE("Direction   Bearing\n"
                 "North       000\n"
                 "North-east  045\n"
                 "East        090\n"
                 "South-east  135\n"
                 "South       180\n"
                 "South-west  225\n"
                 "West        270\n"
                 "North-west  315",
                 "text", title="The eight points and their bearings"),
            T("Figure 3 is a **fictitious** map of Kuma district. It is not a real place. It has a grid with squares of 1 km, "
              "contour lines in metres, a river and its tributary, a road, forest, swamp and farmland. We shall use it for "
              "two model answers."),
            IMG("f5g-exam-kuma-map.svg",
                alt="Fictitious map of Kuma district: a hill in the north-east, the River Kuma flowing south-west, a road through Kuma town, forest in the north-west and a swamp in the south-west.",
                caption="Figure 3. Fictitious map of Kuma district. 1 grid square = 1 km. Summit 412 m at 152 240."),
            EX("Model answer 1: describe the relief and drainage",
               intro="Question: Using Figure 3, describe the relief and the drainage of Kuma district. (Write about three points, each with evidence from the map.)",
               steps=[
                   S("Point 1: high land in the north-east, low land in the south-west",
                     text="The land is highest in the north-east, where the summit is 412 m at grid reference 152 240 and the contours of 400, 300, 200 and 100 m ring the hill. It is lowest in the south-west, where the spot height is only 64 m, near 106 207. So the land slopes down from north-east to south-west."),
                   S("Point 2: slopes are steep on one side and gentle on the other",
                     text="The slopes are steep on the east side of the hill, where the 300 m and 200 m contours are only about 0.3 km apart. They are gentle on the west side, where the same contours are about 0.9 km apart. Contours that are close together mean a steep slope; contours far apart mean a gentle slope."),
                   S("Point 3: drainage follows the slope",
                     text="The River Kuma rises on the lower slopes of the hill near 145 233 and flows south-west across the map to leave at the western edge. A tributary flows south from near the northern edge and joins the river at 115 214. The streams join like branches of a tree, the start of a dendritic pattern. They flow towards the lowest ground, where there is a swamp in the south-west."),
               ]),
            EX("Model answer 2: locate, measure and explain",
               intro="Question: (a) Give the six-figure grid reference of the church. (b) Find the distance and the bearing from the church to the summit (the 412 m height). (c) Explain why Kuma town has grown where it stands.",
               steps=[
                   S("(a) Grid reference",
                     text="The church is between the lines 12 and 13 across, six tenths along, so the easting is 126. It is between the lines 22 and 23 up, six tenths up, so the northing is 226. The reference is 126 226."),
                   S("(b) Distance and bearing",
                     text="The summit is at 152 240, so it is 2.6 km east and 1.4 km north of the church. Pythagoras gives the distance: the square root of (2.6 squared plus 1.4 squared) is about 2.95, so about 3.0 km. The angle from north is the inverse tangent of 2.6 divided by 1.4, about 62 degrees. The bearing is 062 degrees."),
                   S("(c) Explanation: point, evidence, explain",
                     text="Kuma stands on flat, low land between the River Kuma and its tributary. This gives a water supply and farmland, and the farmland on the map lies beside the town. The main road passes through the town and crosses both streams by bridges, so it is easy to reach. It is well away from the steep slopes of the hill and from the swamp in the south-west, where building would be difficult."),
               ]),
            EX("Worked example 3: scale and a measured distance",
               intro="On a map of scale 1 : 50 000 a road measures 4.6 cm between two bridges. What is the ground distance in kilometres?",
               steps=[
                   S("Multiply by the scale", math=r"4.6 \times 50\,000 = 230\,000 \text{ cm}"),
                   S("Change to kilometres", math=r"230\,000 \div 100\,000 = 2.3 \text{ km}"),
                   S("State the answer with the unit", text="The ground distance is 2.3 km."),
               ]),
            H("Linking physical features to human activity"),
            KEY("Three links to look for",
                "Examiners ask you to go beyond 'what is where' to 'why it is there'. Use these links, always with a map reference.",
                cards=[["Water and flat land", "Villages and towns often stand on flat land near a river or a stream. The water is used for drinking and farming."],
                       ["Slope and farming", "Farms and fields are on gentle slopes and plains. Steep slopes are often left under forest, because they are hard to farm and soil is easily washed away."],
                       ["Routes and crossing points", "Roads follow gentle ground. Bridges appear where roads cross rivers, and towns often grow at such crossing points."]]),
            MISTAKE("Reading the northing first",
                    "A grid reference is easting first, then northing. 126 226 and 226 126 are two different places. Say to yourself: along the corridor, then up the stairs."),
            QUIZ("A feature has the grid reference 140 225. Which statement is correct?",
                 ["It is 14 squares up and 225 across", "Its easting is 14.0 and its northing is 22.5", "Its northing is 14.0 and its easting is 22.5", "It is in square 22 across and 14 up"], 1,
                 "Eastings come first: easting 14.0 (the first three digits) and northing 22.5 (the last three).",
                 hint="Split the six digits into two groups of three. Which group is read first?",
                 feedback=["The digits are tenths of a km, not counts of squares.", "",
                           "The order is reversed. The first three digits are the easting.",
                           "The reference is not in squares of 22 and 14, because the digits are read as 14.0 and 22.5."]),
            QUIZ("The bearing of B from A is 062 degrees. What is the bearing of A from B?",
                 ["062 degrees", "118 degrees", "242 degrees", "298 degrees"], 2,
                 "The bearing back is 180 degrees different: 062 plus 180 is 242 degrees.",
                 hint="The direction back is the opposite direction. How many degrees is the opposite?",
                 feedback=["That is the same direction, not the way back.", "180 minus 62 is not the bearing back.", "",
                           "360 minus 62 would measure the angle the other way round and is not the bearing back."]),
            PQ("Look at Figure 3. Give the four-figure grid reference of the square that contains the school (the S symbol), and the six-figure reference of the hospital.",
               "The school is at 11.9 across and 21.9 up, so it lies in the square 1121 (easting 11, northing 21). The hospital is at 13.9 across and 21.9 up, so its six-figure reference is 139 219."),
            PQ("Using Figure 3, find the straight-line distance from the school to the hospital and give the bearing of the hospital from the school.",
               "The school (119 219) and the hospital (139 219) are on the same northing. The hospital is 2 squares east, so the distance is 2.0 km. The direction is due east, so the bearing is 090 degrees."),
            PQ("Describe the land in the south-west of Figure 3 and say how it differs from the land near the summit.",
               "The south-west is low and flat: the spot height is only 64 m near 106 207, the river leaves the map there and there is a swamp. Near the summit the land is high (412 m at 152 240) with closely spaced contours on the east side. So the south-west is low and gentle, the north-east is high and steeper."),
            PQ("Using Figure 3, explain why the village of Ebo (148 215) is where it is. Use evidence from the map.",
               "Ebo is on lower ground south of the hill, outside the steep slopes. A track runs from the main road to the village, so it is linked to Kuma and to the hospital. It is on land that is flatter than the hill slopes and is not in the swamp."),
            SUM("Section A of Paper 2 is compulsory and carries 25% of the marks for the whole examination.",
                "Follow six steps: read the whole question, study key, scale and grid, locate, measure, describe, link.",
                "Grid references: eastings first, then northings. Bearings: clockwise from north, three figures; the bearing back differs by 180.",
                "Describe relief with heights and contour spacing: close together is steep, far apart is gentle. Describe drainage with the flow direction and joins.",
                "Always give evidence from the map and link physical features to settlement, farming and routes."),
        ],
    ),

    # ------------------------------------------------------------------ 3. Physical and human questions
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2: answering physical and human geography questions",
        slug="geoexam-paper-2-answering-physical-and-human-questions",
        minutes=24,
        summary="How to answer the essay questions of Sections B and C: read the command word, plan in two minutes, write "
                "point-evidence-explain paragraphs, add a labelled sketch and use examples from LICs, NICs and AICs.",
        objectives=[
            "Identify the command word in a question and describe what it asks you to do",
            "Outline a two-minute plan and write point, evidence and explain paragraphs",
            "Draw and label a simple sketch diagram that supports an answer",
            "Illustrate human geography answers with examples from LICs, NICs and AICs without inventing facts",
        ],
        key_concepts=["Command word", "Plan", "Point, evidence, explain", "Labelled sketch", "LIC, NIC and AIC examples", "Section B", "Section C"],
        blocks=[
            H("Introduction"),
            T("In Paper 2 you answer **one question from Section B (physical geography)** and **one from Section C (human "
              "geography, with examples from LICs, NICs and AICs)**. You choose from two questions in each section. "
              "Remember that these answers are written in sentences and paragraphs, with diagrams, not just ticked.\n\n"
              "A student in Limbe may know a lot about rainfall. But a long list of facts about rainfall does not answer "
              "'Explain how relief rainfall is formed'. Marks go to the answer that does what the question asks. "
              "This lesson shows how."),
            TIP("**Exam link.** These skills are for Paper 2 Section B (physical geography) and Section C (human geography with "
                "examples from LICs, NICs and AICs). The same ideas help in Section D, the Cameroon question. The Board's "
                "assessment objectives are knowledge, comprehension, application and analysis, so show that you understand, "
                "not only that you remember.",
                title="Where this appears"),
            H("Command words"),
            T("The **command word** is the word in the question that tells you what to do. The Board's syllabus uses verbs "
              "such as define, illustrate, describe, explain, outline, identify, calculate and draw. Other words, such as "
              "state, compare or suggest, are also common. Always read the instruction on your own paper."),
            CODE("Command word    What to do\n"
                 "define          give the exact meaning in one sentence\n"
                 "identify/state  give a short answer; no explanation needed\n"
                 "describe        say what it is like or what happens: features, pattern, numbers\n"
                 "outline         give the main points briefly\n"
                 "explain         give reasons: say how and why\n"
                 "illustrate      show with an example or a diagram\n"
                 "draw            make a neat labelled sketch or diagram\n"
                 "calculate       work out a number; show working and give the unit\n"
                 "compare         say how two things are alike and how they differ",
                 "text", title="What command words ask for"),
            QUIZ("A question says 'Explain why Douala receives heavy rain.' What must your answer contain?",
                 ["A list of towns with heavy rain", "Reasons that say how and why the rain falls", "A definition of rain only", "A drawing with no writing"], 1,
                 "Explain asks for reasons, with how and why, linked to the place.",
                 hint="Which command word is it? What does that word ask for?",
                 feedback=["A list does not give reasons.", "",
                           "A definition alone does not say why.", "A sketch helps, but the answer still needs written reasons."]),
            H("Plan in two minutes"),
            KEY("A two-minute plan",
                "Four questions in 150 minutes means that you cannot write without thinking. Use the first two minutes of each question to plan (KKEVO study advice, not an official rule), on a spare line of your answer book, and cross it out neatly.",
                cards=[["1. Underline", "The command word and the topic words. For example: Explain / relief rainfall."],
                       ["2. List points", "Write three or four key points, in a sensible order, in a few words each."],
                       ["3. Choose a sketch", "Decide which labelled diagram would help. Draw it first or last, but not by accident."],
                       ["4. Check the time", "Each of four questions has a share of the 150 minutes. A guide: about 45 minutes for Section A and 35 for each of the other three."]]),
            H("Point, evidence, explain"),
            IMG("f5g-exam-pee.svg",
                alt="Three boxes: Point, Evidence, Explain, with an example paragraph about relief rain on Mount Cameroon.",
                caption="Figure 1. One paragraph = point + evidence + explanation."),
            T("A good paragraph has three parts. The **point** says what. The **evidence** gives a fact, a number or a place. "
              "The **explanation** says how or why, and links back to the question.\n\n"
              "For three or four main points, write three or four paragraphs. This is easy for an examiner to follow."),
            H("Labelled sketch diagrams"),
            T("A sketch is a quick, neat drawing, not a work of art. In geography it earns marks because it shows that you "
              "understand the process. A good sketch has:\n\n"
              "a title; a large, clear size (at least a third of a page); labels written with a pencil and ruler lines "
              "pointing to the right part; and short notes (annotations) that say what is happening, such as 'air rises and cools'.\n\n"
              "Draw with a sharp pencil. Do not colour heavily. Put arrows on the paths of air or water."),
            EX("Model answer plan 1: a physical question (Section B)",
               intro="Question: Explain how relief rainfall is formed. Use a labelled sketch.",
               steps=[
                   S("Sketch", text="Draw the cross-section in Figure 2: sea on the left, a mountain on the right. Add arrows for moist air rising on the windward side and sinking on the leeward side. Label: Atlantic Ocean, moist air, windward side, heavy rain, leeward side, little rain. Give it a title."),
                   S("Paragraph 1: moist air meets a mountain", text="Point: relief rainfall begins when moist air from the sea meets high land. Evidence: Mount Cameroon rises close to the Atlantic coast near Limbe. Explain: the mountain blocks the air, so the air is forced to rise."),
                   S("Paragraph 2: cooling and condensation", text="Point: rising air cools. Evidence: air gets colder as it goes up (the troposphere is cooler at height). Explain: cool air holds less water vapour, so the vapour condenses into cloud and falls as rain."),
                   S("Paragraph 3: wet and dry sides", text="Point: the windward side is wet and the leeward side is dry. Evidence: the slopes facing the sea receive the heavy rain (check your textbook for figures for Mount Cameroon). Explain: on the leeward side the air sinks and warms, so it takes up water vapour and little rain falls."),
               ]),
            IMG("f5g-exam-sketch-relief-rain.svg",
                alt="A labelled sketch of moist air rising over a mountain near the sea, with heavy rain on the windward side and little rain on the leeward side.",
                caption="Figure 2. A model labelled sketch for the question on relief rainfall."),
            H("Examples from LICs, NICs and AICs"),
            T("Section C asks for **examples from LICs, NICs and AICs**. An example is a place or a country with a fact "
              "that supports your point. The Board's note says that case studies are not required for agriculture and resources: "
              "well-chosen examples are enough."),
            KEY("Typical examples to know",
                "Use the examples that your teacher and textbook gave you. These are common ones, not a fixed list.",
                cards=[["LIC (low-income country)", "For example Chad or Niger: low incomes, much of the work in farming, high birth rates."],
                       ["NIC (newly industrialising country)", "For example South Korea or Brazil: fast growth of manufacturing and rising incomes."],
                       ["AIC (advanced industrial country)", "For example Japan or the USA: high incomes, services and industry, low birth rates."]]),
            T("**Do not invent facts or numbers.** If you are not sure of a figure, describe it in words, such as 'high', 'about "
              "half' or 'one of the highest in the world'. A true general statement scores better than a false exact number. "
              "Name the country or place, give one true fact, then link it to the question."),
            EX("Model answer plan 2: a human question (Section C)",
               intro="Question: Explain why the population of many low-income countries is growing fast.",
               steps=[
                   S("Paragraph 1: high birth rates", text="Point: birth rates are high. Evidence: countries such as Niger have some of the highest numbers of births per woman in the world (check current data). Explain: children help on farms, many families have little access to family planning, and parents want children to care for them in old age."),
                   S("Paragraph 2: falling death rates", text="Point: death rates have fallen. Evidence: more children now receive vaccines and clinics and clean water are more common. Explain: more people survive, so birth rate minus death rate, the natural increase, is large."),
                   S("Paragraph 3: a young population", text="Point: many people are young. Evidence: the age-sex pyramid of an LIC has a wide base. Explain: the many young people will soon become parents, so the population keeps growing even if families become smaller."),
                   S("Paragraph 4: contrast and conclusion", text="Evidence: in an AIC such as Japan, birth rates are low and the population is ageing, so growth is slow. Conclusion: high births and falling deaths, with a young population, explain fast growth in many LICs."),
               ]),
            MISTAKE("Answering a different question",
                    "Writing everything you know about rainfall when the question is about one type of rainfall. Read the command word and the topic words, and answer only that."),
            PQ("Explain the difference between 'describe' and 'explain'. Use the River Benue as an example.",
               "Describe: say what it is like. The River Benue flows west from the Adamawa area through Garoua into Nigeria. Explain: give reasons, for example why its flow is low in the dry season (little rain) and high in the rainy season. Describe tells what; explain tells why."),
            PQ("Write one point-evidence-explain paragraph to answer: 'Why do farmers build terraces on steep slopes?'",
               "Point: terraces reduce soil loss on steep slopes. Evidence: in hilly farming areas in Africa and Asia, farmers cut steps into the hillside. Explain: each flat step slows the water running down the slope, so less soil is washed away and the crops can use the water."),
            PQ("List four things that a good labelled sketch diagram must have.",
               "A title; a clear, fairly large drawing; labels with lines pointing to the correct parts; and short notes or arrows that say what is happening, such as 'air rises and cools'."),
            PQ("Plan three points for: 'Explain why desertification is a problem in the Sahel.'",
               "Point 1: land loses its plant cover through overgrazing, tree cutting and drought. Point 2: the soil is blown or washed away, so crops fail and wells dry up. Point 3: people lose farmland and may migrate. Evidence for each: Lake Chad has become much smaller than it was in the 1960s, and many families around it have lost fishing and farming (check your textbook for details)."),
            SUM("Read the command word first: describe tells what, explain tells why, calculate needs working and a unit, draw needs a labelled sketch.",
                "Plan for two minutes: underline, list three or four points, choose a sketch, check the time.",
                "Write point, evidence, explain paragraphs. The evidence must be a true fact or place.",
                "A good sketch has a title, a large clear drawing, labels with lines and short notes.",
                "In Section C, use examples from LICs, NICs and AICs. Never invent numbers; use words if you are unsure."),
        ],
    ),

    # ------------------------------------------------------------------ 4. The Cameroon question
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2: the Cameroon question (Section D)",
        slug="geoexam-paper-2-the-cameroon-question",
        minutes=24,
        summary="Section D of Paper 2 is the Geography of Cameroon: two questions, one answered. Learn to use safe Cameroon facts, "
                "locate features on a sketch map, plan an answer and check it against a study checklist.",
        objectives=[
            "Outline what Section D covers: background, physical and human characteristics and economic development potentials of Cameroon",
            "Identify the ten regions and their capitals and the main relief units, rivers, climate zones and ports of Cameroon",
            "Draw and label a simple sketch map of Cameroon to locate features",
            "Explain physical and economic features of Cameroon in point, evidence, explain paragraphs",
        ],
        key_concepts=["Section D", "Regions and capitals", "Relief units", "Climate zones", "Sketch map", "Rivers and ports", "Cameroon facts"],
        blocks=[
            H("Introduction"),
            T("Section D is the question closest to home. It asks about **your own country**: where the regions are, "
              "how high and wet the land is, where people live and how Cameroon earns its living.\n\n"
              "A student from Maroua knows the heat of the Far North. A student from Buea knows the rain on the slopes "
              "of Mount Cameroon. Section D rewards that knowledge, written with care and with true facts."),
            D("In Paper 2, **Section D (Geography of Cameroon)** has **two questions and you answer one**. Paper 1 also "
              "has multiple-choice questions on Cameroon. It sets no multiple-choice question on pure case studies, except on Cameroon.",
              title="Section D: the official facts"),
            TIP("**Exam link.** Section D is Paper 2. Cameroon facts also appear in Paper 1, which sets no multiple-choice "
                "question on pure case studies except on Cameroon. Learning the facts on this page helps in both papers.",
                title="Where this appears"),
            H("What the Cameroon topics cover"),
            KEY("The four Cameroon topics in the syllabus",
                "Any Section D question comes from one of these four topics.",
                cards=[["Background of Cameroon", "Location in Africa; the administrative map and the regional headquarters."],
                       ["Physical characteristics", "Relief units, drainage systems and watersheds, climatic types, vegetation and soils."],
                       ["Human characteristics", "Population growth, structure, distribution and migration; settlement and urbanisation; town and countryside."],
                       ["Economic development potentials", "Agriculture; forest, fish, mineral and energy resources; river development; manufacturing; the informal sector; transport; tourism; growth and constraints."]]),
            H("A fact bank to learn"),
            CODE("Region        Capital\n"
                 "Adamawa       Ngaoundere\n"
                 "Centre        Yaounde\n"
                 "East          Bertoua\n"
                 "Far North     Maroua\n"
                 "Littoral      Douala\n"
                 "North         Garoua\n"
                 "North-West    Bamenda\n"
                 "South         Ebolowa\n"
                 "South-West    Buea\n"
                 "West          Bafoussam",
                 "text", title="The ten regions and their capitals"),
            KEY("Other facts to know",
                "These facts are widely taught. For figures such as heights, areas and tonnes, check your textbook.",
                cards=[["Relief units", "Coastal plain; southern plateau; Adamawa plateau; western highlands; Benue and Chad lowlands; Mandara mountains."],
                       ["Mount Cameroon", "The highest peak in Cameroon and an active volcano near the coast."],
                       ["Main rivers", "Sanaga, Wouri, Nyong, Benue, Logone, Cross River and Mungo."],
                       ["Climate zones", "Equatorial (Guinean), Cameroonian-type monsoon, Sudanian and Sahelian."],
                       ["Ports and works", "The ports of Douala and Kribi; the Lagdo dam on the Benue; Lake Chad in the far north."]]),
            H("Locating on a sketch map"),
            T("Examiners like answers that locate things. A simple sketch map of Cameroon can earn marks and make your "
              "explanation clear. Cameroon is wide in the south and narrow in the north, with the Atlantic coast in the "
              "south-west and Lake Chad at the northern tip. Practise drawing this shape until it takes one minute."),
            IMG("f5g-exam-cameroon-sketch.svg",
                alt="A simplified sketch map of Cameroon with towns, rivers Benue and Sanaga, Mount Cameroon, Lake Chad, the Adamawa plateau and the Mandara mountains.",
                caption="Figure 1. A simplified sketch map of Cameroon (not to scale; check the shape in an atlas)."),
            T("Add only what the question needs. For a question on relief, mark the six relief units. For a question on "
              "climate, mark the zones. Use a key or direct labels and give the sketch a title."),
            EX("Model answer plan 1: relief (Physical characteristics)",
               intro="Question: Describe the main relief regions of Cameroon. Show them on a sketch map.",
               steps=[
                   S("Sketch", text="Draw the outline as in Figure 1 and label: Atlantic Ocean, coastal plain, Mount Cameroon, southern plateau, Adamawa plateau, western highlands, Mandara mountains, Benue and Chad lowlands."),
                   S("Paragraph 1: south and west", text="Point: the south-west has a low coastal plain with a high volcano. Evidence: Mount Cameroon, the highest peak in the country, rises near the coast. Behind the plain is the southern plateau and, to the north-west, the western highlands, near Bamenda and Bafoussam."),
                   S("Paragraph 2: the centre", text="Point: the middle of the country is a plateau. Evidence: the Adamawa plateau lies in the middle of the country, near Ngaoundere. It separates the forested south from the drier north."),
                   S("Paragraph 3: the north", text="Point: the north is lower, with a few mountains. Evidence: the Benue and Chad lowlands lie around Garoua and towards Lake Chad, and the Mandara mountains stand in the Far North near Maroua. (Check your textbook for heights.)"),
               ]),
            EX("Model answer plan 2: climate (Physical characteristics)",
               intro="Question: Compare the climate of the Far North with the climate of the south, and explain the differences.",
               steps=[
                   S("Paragraph 1: the south", text="Point: the south has a warm, wet equatorial climate. Evidence: places such as Yaounde and Douala have rain in most months (check your textbook for the months and totals). Explain: the south lies near the equator and near the Atlantic, so warm moist air gives frequent rain."),
                   S("Paragraph 2: the Far North", text="Point: the Far North is hot and dry for much of the year. Evidence: it has a Sahelian climate, with a short rainy season and a long dry season, near Maroua and Lake Chad. Explain: it is far from the sea and close to the Sahara, so moist air reaches it only for a short time."),
                   S("Paragraph 3: the contrast", text="Point: the two regions differ in the length of the rainy season. Evidence: the south has a long wet period; the Far North has a long dry season. Explain: rainfall decreases from south to north as the distance from the sea increases. In between, the Sudanian and Cameroonian-type monsoon climates have an intermediate pattern."),
               ]),
            EX("Model answer plan 3: economy (Economic development potentials)",
               intro="Question: Explain why Douala is the main port of Cameroon.",
               steps=[
                   S("Paragraph 1: site", text="Point: Douala is on the coast, on the Wouri estuary. Evidence: it lies in the Littoral region, on the Gulf of Guinea. Explain: the estuary provides a sheltered harbour for ships."),
                   S("Paragraph 2: routes inland", text="Point: it is linked to the interior. Evidence: roads and a railway lead inland to Yaounde and beyond (check your textbook for the railway). Explain: goods can be moved easily between the port and the rest of the country."),
                   S("Paragraph 3: wider market", text="Point: it also serves neighbouring countries. Evidence: goods for landlocked countries such as Chad and the Central African Republic have used the port (check your textbook). Explain: this brings extra trade and jobs. Kribi is a second port."),
               ]),
            KEY("A study checklist for Section D (not an official mark scheme)",
                "After you write, check your answer against these six questions.",
                cards=[["Cameroon places", "Did I name real regions, towns, rivers or relief units?"],
                       ["Location", "Did I locate things on a sketch map or in words (north, south-west, near the coast)?"],
                       ["True facts", "Does every point have one true fact? Did I avoid inventing numbers?"],
                       ["Explain", "Did I say why, not only what?"],
                       ["Link", "Did I link to people and development: farming, towns, trade, energy?"],
                       ["Command word", "Did I do what describe, explain or compare asked?"]]),
            MISTAKE("Being vague about Cameroon",
                    "'Cameroon is hot and has rivers' earns little. Name the region, the climate zone or the river, and give a true fact about it."),
            MISTAKE("Confusing regions and capitals",
                    "Buea (South-West) and Bamenda (North-West) are often swapped, as are Bafoussam (West) and Garoua (North). Learn the table of ten regions and say it aloud."),
            QUIZ("Which town is the capital of the South-West Region?",
                 ["Bamenda", "Bafoussam", "Buea", "Ebolowa"], 2,
                 "Buea is the capital of the South-West Region. It stands on the slopes of Mount Cameroon.",
                 hint="Think of the town on the slopes of the highest peak in the country.",
                 feedback=["Bamenda is the capital of the North-West.", "Bafoussam is the capital of the West.", "",
                           "Ebolowa is the capital of the South."]),
            QUIZ("In which part of Cameroon is the Sahelian climate found?",
                 ["The coast near Douala", "The Far North near Lake Chad", "The south near Ebolowa", "The western highlands"], 1,
                 "The Sahelian climate, with a short rainy season and a long dry season, is found in the far north.",
                 hint="Which part of Cameroon is nearest to the Sahara and Lake Chad?",
                 feedback=["The coast is wet, with a long rainy period.", "",
                           "The south has an equatorial climate with rain in most months.", "The highlands have cooler, wetter weather because of height."]),
            PQ("State the capitals of the Far North, the North and the Adamawa regions.",
               "Far North: Maroua. North: Garoua. Adamawa: Ngaoundere."),
            PQ("State two facts about Mount Cameroon.",
               "It is the highest peak in Cameroon. It is an active volcano near the coast, in the south-west of the country."),
            PQ("Name the four climate zones of Cameroon and say which one is found in the Far North.",
               "Equatorial (Guinean), Cameroonian-type monsoon, Sudanian and Sahelian. The Sahelian zone is found in the Far North."),
            PQ("Describe how you would show these on a quick sketch map: the Atlantic coast, Mount Cameroon, Douala, Yaounde and Lake Chad.",
               "Draw a simple outline that is wide in the south and narrow in the north. Write Atlantic Ocean on the south-west side of the outline. Mark Mount Cameroon with a triangle on the coast and Douala by a dot near it. Mark Yaounde by a dot inland to the east of Douala. Draw Lake Chad as a small lake at the northern tip. Add a title."),
            SUM("Section D (Geography of Cameroon) has two questions; you answer one. Cameroon facts also appear in Paper 1.",
                "Learn the ten regions and their capitals, the relief units, the main rivers, the climate zones and the ports.",
                "Practise a simple sketch map and use it to locate features.",
                "Write point, evidence, explain paragraphs with one true fact for each point.",
                "Use the checklist after you write. For figures, check your textbook and never invent numbers."),
        ],
    ),
]
