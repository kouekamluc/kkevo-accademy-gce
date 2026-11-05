"""Form 5 Computer Science (O Level): Examination - Paper 2 (structured theory) and Paper 3 (practical)."""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")

MODULE = "Examination"
P2 = "Paper 2"
P3 = "Paper 3 (practical)"

LESSONS = []

# ------------------------------------------------------------------ 1. Logic gates and truth tables
LESSONS.append(lesson(
    module=MODULE, topic=P2,
    title="Logic gates and truth tables",
    slug="paper-2-logic-gates-and-truth-tables", minutes=22,
    summary="Learn the six logic gates (AND, OR, NOT, NAND, NOR, XOR), draw their symbols, write their truth tables and read a small circuit with two or three inputs.",
    objectives=[
        "Name the six logic gates and recognise their symbols",
        "Write the truth table of any single gate",
        "Work out how many rows a truth table needs for a given number of inputs",
        "Read a circuit with two or three inputs and complete its truth table step by step",
    ],
    key_concepts=["Logic gate", "Truth table", "Binary input", "AND gate", "OR gate", "NOT gate", "NAND gate", "NOR gate", "XOR gate"],
    blocks=[
        H("Introduction"),
        T("A computer decides things with switches that are either **on** or **off**. A security light outside a shop in Buea is a good example. It must come on only when it is dark **and** someone moves near it."),
        T("A **logic gate** is a tiny circuit that makes this kind of yes or no decision. Computers are built from millions of them. In Paper 2 you draw them, read them and describe what they do."),
        T("The exam description for Paper 2 includes logic circuits, but the syllabus topic list does not teach them. The exam description includes this, so we teach it here from the beginning. For the exact paper format, check the current GCE Board instructions."),
        H("Inputs, outputs and 0 and 1"),
        D("A **logic gate** takes one or two **inputs** and gives one **output**. Every input and output is either **1** (on, true) or **0** (off, false).", title="Logic gate"),
        T("We name inputs with capital letters such as A, B and C. The output is usually called Q. In a computer, 1 may be a high voltage and 0 a low voltage. For the exam you only need the 0 and 1 values."),
        D("A **truth table** lists every possible combination of inputs and shows the output for each one. It is the complete description of what a gate or circuit does.", title="Truth table"),
        H("The six gates"),
        IMG("f5c-logic-gate-symbols.svg", alt="The symbols of the AND, OR, NOT, NAND, NOR and XOR gates with their Boolean statements", caption="Figure 1. The six gate symbols. A small circle on the output means NOT."),
        KEY("Learn these three first", "AND, OR and NOT are the basic gates.", cards=[
            ["AND", "Output is 1 only when A and B are both 1."],
            ["OR", "Output is 1 when A or B or both are 1."],
            ["NOT", "One input. It reverses the input: 0 becomes 1 and 1 becomes 0."],
        ]),
        KEY("Then the three that add a NOT", "These are easy if you know the first three.", cards=[
            ["NAND", "NOT AND. It gives the opposite of AND."],
            ["NOR", "NOT OR. It gives the opposite of OR."],
            ["XOR", "Exclusive OR. Output is 1 when the two inputs are different."],
        ]),
        T("Look at the symbols. NAND is the AND shape with a small circle added. NOR is the OR shape with a small circle. The circle means NOT. XOR is the OR shape with an extra curved line at the input side."),
        CODE("""A B | AND  OR  NAND  NOR  XOR
0 0 |  0    0    1    1    0
0 1 |  0    1    1    0    1
1 0 |  0    1    1    0    1
1 1 |  1    1    0    0    0

A | NOT A
0 |   1
1 |   0""", "text", title="Truth tables of the six gates"),
        TIP("To remember the table: AND needs both inputs on, so it has a single 1 at the bottom. OR has a single 0 at the top. NAND and NOR are the opposites of AND and OR, so flip every value. XOR is 1 only on the two middle rows."),
        H("How many rows?"),
        D("With **n** inputs there are 2 multiplied by itself n times combinations. That is 4 rows for 2 inputs, 8 rows for 3 inputs and 16 rows for 4 inputs.", title="Rows in a truth table"),
        T("Write the rows in counting order, starting with all 0s and ending with all 1s. The right-hand input changes fastest. This order makes sure you never miss or repeat a row."),
        EX("Worked example 1: a security light", intro="The light at a shop is ON (Q = 1) only when it is dark (D = 1) and movement is detected (M = 1). Which gate is this, and what is its truth table?", steps=[
            S("Decide the rule in words", text="Both conditions must be true at the same time."),
            S("Choose the gate", text="Both inputs must be 1 for the output to be 1. That is an AND gate: Q = D AND M."),
            S("Write the four rows", text="D and M can be 00, 01, 10 or 11. Only the last row has both inputs on."),
            S("Truth table", text="Only the row D = 1, M = 1 gives Q = 1. The light stays off in all other rows."),
        ]),
        CODE("""D M | Q
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1""", "text", title="Truth table for the security light"),
        H("Reading a circuit"),
        T("A circuit joins several gates. The output of one gate can feed the input of the next. To read it, work **from the inputs to the output**, one gate at a time. Give each gate output a small label such as X or Y. Then make a column for each label in your truth table."),
        IMG("f5c-logic-circuit-read.svg", alt="Circuit: A and B go into an AND gate giving X. C goes into a NOT gate giving Y. X and Y go into an OR gate giving Q", caption="Figure 2. The circuit for Q = (A AND B) OR (NOT C)."),
        EX("Worked example 2: truth table for a three-input circuit", intro="Complete the truth table for the circuit in Figure 2. How many rows have Q = 1?", steps=[
            S("Count the rows", text="There are 3 inputs, so 8 rows."),
            S("Add a column for each gate output", text="X comes from the AND gate (A AND B). Y comes from the NOT gate (NOT C). Q comes from the OR gate (X OR Y)."),
            S("Fill X, then Y, then Q on every row", text="For row 1 1 0: X = 1 AND 1 = 1, Y = NOT 0 = 1, and Q = 1 OR 1 = 1."),
            S("Count the 1s in the Q column", text="Q is 1 on five rows."),
        ]),
        CODE("""A B C | X Y | Q
0 0 0 | 0 1 | 1
0 0 1 | 0 0 | 0
0 1 0 | 0 1 | 1
0 1 1 | 0 0 | 0
1 0 0 | 0 1 | 1
1 0 1 | 0 0 | 0
1 1 0 | 1 1 | 1
1 1 1 | 1 0 | 1""", "text", title="Truth table for Q = (A AND B) OR (NOT C)"),
        MISTAKE("Missing or repeated rows", "Always write the rows in counting order (000, 001, 010, 011, ...). If you write them in a random order it is easy to miss a combination and lose marks."),
        MISTAKE("Mixing up OR and XOR", "OR gives 1 when both inputs are 1. XOR gives 0 when both inputs are 1. Check the bottom row: that is where they differ."),
        MISTAKE("Skipping the middle columns", "Do not try to find Q in your head for a three-input circuit. Add a column for every gate output. It is slower for one row but faster and safer for eight."),
        QUIZ("Which gate gives an output of 1 only when its two inputs are different?", ["AND", "XOR", "NOR", "OR"], 1,
             "XOR (exclusive OR) is 1 when exactly one input is 1. Rows 01 and 10 give 1; rows 00 and 11 give 0.",
             hint="Look at the two middle rows of the truth table.",
             feedback=["AND gives 1 only when both inputs are 1.", "", "NOR gives 1 only when both inputs are 0.", "OR also gives 1 when both inputs are 1, so it is not limited to different inputs."]),
        QUIZ("A circuit has 4 inputs. How many rows does its full truth table need?", ["8", "12", "16", "4"], 2,
             "Each extra input doubles the number of rows: 2, 4, 8, 16. So 4 inputs need 16 rows.",
             hint="Double the number of rows each time you add an input.",
             feedback=["8 rows is for 3 inputs.", "The number of rows doubles each time; it is not found by adding.", "", "4 rows is for 2 inputs."]),
        PQ("Complete the truth table for a NAND gate with inputs A and B.", "A = 0, B = 0 gives 1. A = 0, B = 1 gives 1. A = 1, B = 0 gives 1. A = 1, B = 1 gives 0. NAND is NOT AND, so it is the opposite of the AND column (0, 0, 0, 1)."),
        PQ("A circuit has the output Q = (NOT (A OR B)) AND C. Complete its truth table and say on which row Q is 1.", "Work out X = A OR B, then Y = NOT X, then Q = Y AND C. Y is 1 only when A = 0 and B = 0. Q needs Y = 1 and C = 1, so Q = 1 only on the row A = 0, B = 0, C = 1. Q is 0 on the other seven rows."),
        PQ("A circuit has 5 inputs. How many rows are in its truth table? Why is it better to draw it as a circuit and test chosen rows than to write every row?", "It has 32 rows (2 multiplied by itself 5 times). Writing 32 rows takes a long time and mistakes are likely. In the exam you are normally given only two or three inputs, but for larger circuits you test chosen rows. The rule 2 to the power n tells you how many rows to expect."),
        PQ("Name the gate: its output is 1 only when both inputs are 0.", "It is a NOR gate. NOR is NOT OR. OR gives 0 only when both inputs are 0, so NOR gives 1 only then."),
        SUM(
            "A logic gate takes inputs of 0 or 1 and gives one output of 0 or 1.",
            "AND needs both inputs 1. OR needs at least one 1. NOT reverses the input.",
            "NAND and NOR are AND and OR with the output reversed. XOR is 1 when the inputs are different.",
            "A truth table has 2 to the power n rows for n inputs, written in counting order.",
            "To read a circuit, go from the inputs to the output and label each gate output with its own column.",
        ),
    ],
))

# ------------------------------------------------------------------ 2. Designing logic circuits
LESSONS.append(lesson(
    module=MODULE, topic=P2,
    title="Designing logic circuits from a problem",
    slug="paper-2-designing-logic-circuits", minutes=24,
    summary="Turn a written problem such as an alarm, a lift or a vote into a Boolean expression, draw the circuit, check it with a truth table and simplify it by inspection.",
    objectives=[
        "Pick out the inputs and the output in a written problem",
        "Write a Boolean expression using AND, OR and NOT",
        "Draw the matching circuit and evaluate it for chosen inputs",
        "Simplify a simple expression by inspection and check it with a truth table",
    ],
    key_concepts=["Boolean expression", "Circuit design", "Evaluating an expression", "Simplification", "Equivalent circuits"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you read circuits that were already drawn. In Paper 2 you may also have to **design** one. You are given a short story, and you must produce the expression and the circuit."),
        T("Think of a shop alarm in Douala. It must ring when a door or window is opened, but only if the owner has switched the alarm on. That sentence already contains a circuit. Your job is to find it."),
        T("The exam description includes circuit synthesis, but the syllabus list does not teach it. So we teach it here. For the exact paper format, check the current GCE Board instructions."),
        H("Boolean expressions"),
        D("A **Boolean expression** describes a circuit using inputs and the words AND, OR and NOT. Brackets show which part is worked out first.", title="Boolean expression"),
        T("Some books write A AND B as A dot B, A OR B as A plus B, and NOT A as A with a bar above it. In this course we write the words, because they are clear and easy to type. Use the style your teacher gives you in the exam."),
        T("Brackets matter. The expression A AND B OR C is unclear. Write (A AND B) OR C or A AND (B OR C). They are different circuits."),
        H("The design method"),
        KEY("Five steps from problem to circuit", "Follow the same steps every time.", cards=[
            ["1. Inputs and output", "List each input with a letter and say what 1 means. Name the output."],
            ["2. Words to operators", "Look for the words and, or, not, both, either, unless, only if."],
            ["3. Expression", "Write the expression with brackets."],
            ["4. Circuit", "Draw one gate per operator, working from the inputs to the output."],
            ["5. Check", "Test the expression with a few rows of a truth table."],
        ]),
        TIP("Words that signal a gate. AND: both, all, and, as well as. OR: either, any, or, at least one. NOT: not, unless, no, without. Read the sentence slowly and underline them."),
        EX("Worked example 1: the shop alarm", intro="An alarm Q must sound if the window sensor W or the door sensor D is triggered, but only when the alarm is switched on (A = 1). Design the circuit.", steps=[
            S("Inputs and output", text="Inputs: W (window open = 1), D (door open = 1), A (alarm on = 1). Output: Q (alarm sounds = 1)."),
            S("Find the operators", text="The window or the door: W OR D. But also the alarm must be on: AND A."),
            S("Write the expression", text="Q = (W OR D) AND A. The bracket is needed so the OR is worked out first."),
            S("Draw the circuit", text="An OR gate for W and D, then an AND gate joining its output to A (Figure 3)."),
        ]),
        IMG("f5c-alarm-circuit.svg", alt="Circuit: W and D go into an OR gate giving X; X and A go into an AND gate giving Q", caption="Figure 3. The alarm circuit Q = (W OR D) AND A."),
        CODE("""W D A | X=W OR D | Q
0 0 0 |    0     | 0
0 0 1 |    0     | 0
0 1 0 |    1     | 0
0 1 1 |    1     | 1
1 0 0 |    1     | 0
1 0 1 |    1     | 1
1 1 0 |    1     | 0
1 1 1 |    1     | 1""", "text", title="Truth table of the alarm"),
        T("Check with the story. The alarm never sounds when A = 0 (switched off). With A = 1 it sounds whenever W or D or both are 1. The table agrees."),
        EX("Worked example 2: a lift", intro="A lift moves (Q = 1) only when the door is closed (D = 1), someone has pressed a call button (B = 1) or a floor button (F = 1), and the lift is not overloaded (O = 1 means overloaded). Write the expression and find on how many rows Q is 1.", steps=[
            S("Inputs and output", text="D, B, F, O. Output Q."),
            S("Find the operators", text="Door closed AND (call button OR floor button) AND NOT overloaded."),
            S("Write the expression", text="Q = D AND (B OR F) AND (NOT O)."),
            S("Count the rows", text="There are 16 rows. Q is 1 when D = 1, O = 0, and at least one of B and F is 1. That is 3 combinations of B and F (01, 10, 11), so Q = 1 on 3 rows."),
        ]),
        CODE("""D B F O | Q          D B F O | Q
0 x x x | 0          1 0 1 0 | 1
1 0 0 0 | 0          1 1 0 0 | 1
1 x x 1 | 0          1 1 1 0 | 1""", "text", title="Lift: the key rows (x means 0 or 1)"),
        EX("Worked example 3: a voting machine", intro="Three judges A, B and C each vote 1 for yes. The result Q is 1 if at least two judges vote yes (a majority). Write the expression and test it.", steps=[
            S("Think in pairs", text="A majority means some pair both said yes: A and B, or B and C, or A and C."),
            S("Write the expression", text="Q = (A AND B) OR (B AND C) OR (A AND C)."),
            S("Test row 1 1 0", text="(1 AND 1) OR (1 AND 0) OR (1 AND 0) = 1 OR 0 OR 0 = 1. Two yes votes give a pass."),
            S("Test row 1 0 0", text="(1 AND 0) OR (0 AND 0) OR (1 AND 0) = 0. One yes vote is not a majority."),
        ]),
        CODE("""A B C | Q
0 0 0 | 0
0 0 1 | 0
0 1 0 | 0
0 1 1 | 1
1 0 0 | 0
1 0 1 | 1
1 1 0 | 1
1 1 1 | 1""", "text", title="Truth table of the majority vote"),
        H("Simplifying by inspection"),
        T("Some circuits use more gates than they need. Fewer gates mean a cheaper and faster circuit. You can often simplify by looking carefully. You do not need long algebra for this exam level."),
        KEY("Rules to look for", "Each rule can be checked with a very small truth table.", cards=[
            ["With 1 and 0", "A AND 1 = A. A AND 0 = 0. A OR 0 = A. A OR 1 = 1."],
            ["Same input twice", "A AND A = A. A OR A = A."],
            ["With its own NOT", "A OR (NOT A) = 1. A AND (NOT A) = 0."],
            ["Double NOT", "NOT (NOT A) = A."],
            ["Common factor", "(A AND B) OR (A AND C) = A AND (B OR C)."],
        ]),
        EX("Worked example 4: simplify", intro="Simplify Q = (A AND B) OR (A AND NOT B) and prove the answer with a truth table.", steps=[
            S("Spot the common factor A", text="Q = A AND (B OR NOT B)."),
            S("Use B OR NOT B = 1", text="Q = A AND 1."),
            S("Use A AND 1 = A", text="Q = A. The whole circuit is just a wire from A to the output."),
            S("Prove it", text="Row by row: A = 0 gives Q = 0 for both B = 0 and B = 1. A = 1 gives Q = 1 for both. So Q always equals A."),
        ]),
        T("The voting circuit can also be shortened by taking out a common factor: Q = (A AND (B OR C)) OR (B AND C). The original needs 3 AND gates and 2 OR gates (5 gates). The shorter form needs 2 AND gates and 2 OR gates (4 gates). Both give the same truth table."),
        MISTAKE("Missing brackets", "(W OR D) AND A and W OR (D AND A) are different circuits. If the alarm sounded whenever the window opened, even with the alarm off, the second form would be wrong for the story."),
        MISTAKE("Reading NOT too late", "In the lift, NOT applies to O only. Write D AND (B OR F) AND (NOT O), not NOT (D AND (B OR F) AND O)."),
        MISTAKE("Simplifying without checking", "If you change an expression, compare the two truth tables. If any row differs, the simplification is wrong."),
        QUIZ("A buzzer must sound if the door is open (D) and the key has not been put in (K = 1 means key in). Which expression is correct?", ["D OR K", "D AND K", "D AND (NOT K)", "(NOT D) AND K"], 2,
             "The buzzer needs the door open (D) and the key not in (NOT K). So Q = D AND (NOT K).",
             hint="Underline the word and, then find which input must be reversed.",
             feedback=["OR would sound the buzzer when only the door is open and the key is in.", "This sounds the buzzer when the key is in, which is the opposite.", "", "This reverses the wrong input."]),
        QUIZ("Which is a simpler form of Q = (A OR B) AND (A OR B)?", ["A AND B", "A OR B", "A", "1"], 1,
             "A rule: X AND X = X. Here X = A OR B, so Q = A OR B.",
             hint="Both brackets are the same. Use the rule for the same input twice.",
             feedback=["The brackets use OR, not AND.", "", "B has disappeared without a reason; A OR B is not the same as A.", "The output is not always 1; try A = 0, B = 0."]),
        PQ("A door-entry system lets a student in (Q = 1) when the card is valid (C = 1) and the time is school hours (H = 1), or when the guard presses the override (G = 1). Write the expression and draw the gates in words.", "Q = (C AND H) OR G. One AND gate has inputs C and H. Its output goes to an OR gate with the second input G. The OR gate output is Q. The override works at any time because OR gives 1 whenever G is 1."),
        PQ("Evaluate Q = (A AND (NOT B)) OR C when A = 1, B = 1 and C = 0.", "NOT B = NOT 1 = 0. A AND 0 = 1 AND 0 = 0. Then 0 OR C = 0 OR 0 = 0. So Q = 0."),
        PQ("Simplify Q = A OR (A AND B). Prove it with a truth table.", "Write A as (A AND 1). Then Q = (A AND 1) OR (A AND B). Take out the common factor A: Q = A AND (1 OR B) = A AND 1 = A. Truth table: A = 0 gives 0 OR 0 = 0 for both B values. A = 1 gives 1 OR B = 1. So Q = A. Q is the same as A on all four rows."),
        PQ("Write the expression for: a water pump runs (Q = 1) when the tank is low (L = 1) and the power is on (P = 1), or when the manual switch (M = 1) is pressed.", "The pump needs low water and power: L AND P. The manual switch adds a second way, so use OR M. Q = (L AND P) OR M. If the story said that the manual switch also needs power, the expression would change to (L OR M) AND P. Read the story to decide."),
        SUM(
            "Find the inputs and the output first, and say what 1 means for each.",
            "Words such as both, and, either, or, not and unless show which gate to use.",
            "Write the expression with brackets, then draw one gate for each operator.",
            "Check the design with a few rows of the truth table against the story.",
            "Simplify by inspection with common factors, A AND 1 = A, and A OR NOT A = 1, and always prove it by truth table.",
        ),
    ],
))

# ------------------------------------------------------------------ 3. Pseudo-code and algorithms
LESSONS.append(lesson(
    module=MODULE, topic=P2,
    title="Pseudo-code and algorithms",
    slug="paper-2-pseudo-code-and-algorithms", minutes=25,
    summary="Learn one clear pseudo-code style: variables, input and output, selection with IF, loops with FOR, WHILE and REPEAT, and simple arrays, then write and read algorithms for everyday problems.",
    objectives=[
        "Explain what an algorithm and pseudo-code are",
        "Write assignment, input and output statements in the course pseudo-code style",
        "Write selection (IF) and the three kinds of loop (FOR, WHILE, REPEAT)",
        "Use a simple array to store a list and process it with a loop",
    ],
    key_concepts=["Algorithm", "Pseudo-code", "Variable", "Assignment", "Selection", "Iteration", "Array", "Flowchart"],
    blocks=[
        H("Introduction"),
        T("Before a programmer writes code, they plan the steps. A trader in Bamenda who gives change follows steps too: take the money, subtract the price, hand back the change. Writing the steps clearly is the skill we practise here."),
        D("An **algorithm** is a finite list of clear steps that solves a problem. **Pseudo-code** is a way of writing an algorithm in plain, structured English that looks like a program but does not belong to any real language.", title="Algorithm and pseudo-code"),
        T("The exam description for Paper 2 includes pseudo-code writing, but the syllabus topic list does not teach it. The exam description includes this, so we teach it here. There is no single pseudo-code style that every paper uses, so we use one consistent style. If your teacher or the exam paper uses a slightly different style, follow it. Check the current GCE Board instructions."),
        H("The pseudo-code style used in this course"),
        T("Keywords are written in capital letters. Each block ends with an END word, and the lines inside a block are indented. Variable names are short and meaningful, such as total, price or count."),
        CODE("""// A line starting with two slashes is a comment
INPUT name                    // read a value into a variable
OUTPUT "Hello ", name         // show text and values
total <- 0                    // assignment: store a value
total <- total + 5            // use the old value to make a new one

Arithmetic:   +  -  *  /  DIV  MOD
              DIV is whole-number division, MOD is the remainder
Comparison:   =  <>  <  >  <=  >=       (<> means not equal)
Logic:        AND  OR  NOT""", "pseudocode", title="Listing 1. Basic statements"),
        T("We type the assignment arrow as the two characters less-than and minus. On paper you may draw a proper arrow. Read it as **becomes** or **is set to**."),
        D("A **variable** is a named place in memory that holds a value that can change. **Assignment** stores a value into a variable. The variable on the left of the arrow receives the value on the right.", title="Variable and assignment"),
        MISTAKE("Mixing assignment and comparison", "total <- 5 stores 5 in total. total = 5 asks whether total is equal to 5. Use the arrow to store and the equals sign to compare."),
        H("Input, process, output"),
        EX("Worked example 1: the average of three marks", intro="Write an algorithm that reads three marks, finds their average and displays it. Check it with the marks 12, 15 and 18.", steps=[
            S("Plan", text="Input three numbers. Process: add them and divide by 3. Output the result."),
            S("Write the pseudo-code", text="See the listing below."),
            S("Test with 12, 15, 18", text="total = 45, and average = 45 / 3 = 15. The output is 15."),
        ]),
        CODE("""INPUT m1, m2, m3
total <- m1 + m2 + m3
average <- total / 3
OUTPUT "Average = ", average""", "pseudocode", title="Average of three marks"),
        H("Selection: making a choice"),
        D("**Selection** lets the algorithm choose between actions, depending on a condition. We use IF ... THEN ... ELSE ... ENDIF.", title="Selection"),
        CODE("""IF mark >= 50 THEN
    OUTPUT "Pass"
ELSE
    OUTPUT "Fail"
ENDIF""", "pseudocode", title="Listing 2. Simple selection"),
        T("When there are more than two outcomes, add ELSE IF lines. The computer takes the first branch whose condition is true and ignores the rest."),
        EX("Worked example 2: a grade", intro="A mark of 70 or more is grade A, 50 to 69 is grade B, and below 50 is grade C. Write the pseudo-code and give the output for a mark of 64.", steps=[
            S("Order the tests", text="Test the highest boundary first. If 70 or more is not true, then a mark of 50 or more must be between 50 and 69."),
            S("Write the pseudo-code", text="See the listing below."),
            S("Test with 64", text="64 >= 70 is false. 64 >= 50 is true. So the output is grade B."),
        ]),
        CODE("""INPUT mark
IF mark >= 70 THEN
    grade <- "A"
ELSE IF mark >= 50 THEN
    grade <- "B"
ELSE
    grade <- "C"
ENDIF
OUTPUT grade""", "pseudocode"),
        H("Iteration: repeating steps"),
        D("**Iteration** (a loop) repeats steps. Use **FOR** when you know how many times, **WHILE** when you test before each repeat, and **REPEAT ... UNTIL** when you test after each repeat.", title="Iteration"),
        KEY("Choosing a loop", "All three can do the same job. Pick the one that matches the story.", cards=[
            ["FOR", "Counted loop. It runs a known number of times: for each of 5 students."],
            ["WHILE", "Tests the condition first. It may run zero times."],
            ["REPEAT ... UNTIL", "Tests the condition at the end. It always runs at least once."],
        ]),
        CODE("""FOR i <- 1 TO 5
    OUTPUT i
NEXT i

count <- 0
WHILE count < 3 DO
    count <- count + 1
ENDWHILE

REPEAT
    INPUT pin
UNTIL pin = 1234""", "pseudocode", title="Listing 3. The three loops"),
        T("WHILE keeps going while the condition is **true**. REPEAT ... UNTIL keeps going until the condition becomes **true**, so it stops when the condition is true. This difference is a common exam trap."),
        H("Arrays: a list under one name"),
        D("An **array** stores a list of values under one name. Each value has a position number called an **index**. In this course the first index is 1, and we write prices[3] for the third value.", title="Array"),
        EX("Worked example 3: shop prices", intro="A shop keeps 5 prices in an array: 1500, 750, 2000, 900 and 1200 FCFA. Write an algorithm that finds the total and counts how many prices are above 1000.", steps=[
            S("Store the prices", text="Set prices[1] to prices[5]. Start total and count at 0."),
            S("Loop over the index", text="FOR i from 1 to 5. Add prices[i] to total. If prices[i] > 1000, add 1 to count."),
            S("Check the result", text="Total = 1500 + 750 + 2000 + 900 + 1200 = 6350. The prices above 1000 are 1500, 2000 and 1200, so count = 3."),
        ]),
        CODE("""prices[1] <- 1500
prices[2] <- 750
prices[3] <- 2000
prices[4] <- 900
prices[5] <- 1200
total <- 0
count <- 0
FOR i <- 1 TO 5
    total <- total + prices[i]
    IF prices[i] > 1000 THEN
        count <- count + 1
    ENDIF
NEXT i
OUTPUT total, count""", "pseudocode"),
        H("Flowcharts"),
        T("A **flowchart** shows an algorithm as a picture. A rounded box is start or end, a parallelogram is input or output, a rectangle is a process step and a diamond is a decision with a YES branch and a NO branch. Figure 4 shows the pass or fail test from Listing 2."),
        IMG("f5c-flowchart-pass-fail.svg", alt="Flowchart: Start, input mark, decision mark at least 50, YES output Pass, NO output Fail, End", caption="Figure 4. Flowchart of the pass or fail test."),
        H("Writing your own algorithms"),
        KEY("A good answer in the exam", "Follow these points.", cards=[
            ["Plan", "Name the inputs, the process and the outputs before you write."],
            ["Layout", "Indent inside IF and loops, and close every block."],
            ["Names", "Use meaningful variable names."],
            ["Test", "Try one example by hand. Does it give the answer you expect?"],
        ]),
        MISTAKE("Forgetting to start a total at zero", "A total or a counter must be set to 0 before the loop. Otherwise it starts with an unknown value."),
        MISTAKE("Off-by-one loops", "FOR i <- 1 TO 5 runs 5 times, not 4 and not 6. Check the first and last index of your array."),
        MISTAKE("Writing real-language code", "Do not write details of a real language, such as colons or print(). Use the pseudo-code style your paper uses."),
        QUIZ("Which loop always runs its steps at least once?", ["WHILE", "FOR", "REPEAT ... UNTIL", "IF"], 2,
             "REPEAT ... UNTIL tests its condition at the end, after the steps have run once.",
             hint="Which loop checks the condition after the body?",
             feedback=["WHILE tests first, so it may not run at all.", "A FOR loop runs a counted number of times, and can run zero times if its range is empty.", "", "IF is a selection, not a loop."]),
        QUIZ("After the lines n <- 4 and then n <- n multiplied by 2, plus 1, what is stored in n? (The second line is n <- n x 2 + 1.)", ["8", "9", "4", "12"], 1,
             "The old value 4 is used first: 4 times 2 is 8, plus 1 is 9. The new value 9 replaces 4 in n.",
             hint="The right-hand side is worked out with the old value of n.",
             feedback=["That ignores the plus 1.", "", "n changes after the second line.", "That would be 4 times (2 + 1), but multiplication comes before addition."]),
        PQ("Write pseudo-code that reads the price of an item and displays 'Discount' if the price is more than 5000 FCFA, otherwise 'No discount'.", "INPUT price. IF price > 5000 THEN OUTPUT 'Discount' ELSE OUTPUT 'No discount' ENDIF. A price of 5000 exactly gives No discount, because 'more than' means greater than."),
        PQ("Write pseudo-code that reads 10 numbers and displays their total.", "total <- 0. FOR i <- 1 TO 10: INPUT number, then total <- total + number. NEXT i. After the loop, OUTPUT total. The counter total must start at zero before the loop."),
        PQ("What does this do? x <- 1, WHILE x < 20 DO, x <- x multiplied by 3, ENDWHILE, OUTPUT x.", "x takes the values 1, 3, 9, 27. When x = 27 the test x < 20 is false, so the loop stops. The output is 27."),
        PQ("Write pseudo-code that keeps asking for a PIN until the user types 4821, then displays 'Welcome'.", "REPEAT, INPUT pin, UNTIL pin = 4821, then OUTPUT 'Welcome'. REPEAT ... UNTIL is the best loop because the PIN must be asked for at least once."),
        SUM(
            "An algorithm is a list of clear steps. Pseudo-code writes it in a structured, language-free style.",
            "Use the arrow to store a value into a variable and the equals sign to compare.",
            "Selection uses IF ... ELSE IF ... ELSE ... ENDIF. Test the highest or most special case first.",
            "FOR counts, WHILE tests first, REPEAT ... UNTIL tests last. Set totals and counters to zero before the loop.",
            "An array stores a list under one name with an index, and a FOR loop is the usual way to process it.",
        ),
    ],
))

# ------------------------------------------------------------------ 4. Trace tables
LESSONS.append(lesson(
    module=MODULE, topic=P2,
    title="Trace tables: following an algorithm step by step",
    slug="paper-2-trace-tables", minutes=24,
    summary="Use a trace table to follow variables through loops and conditions, find the output of an algorithm and spot the error in a faulty one.",
    objectives=[
        "Set up a trace table with one column per variable and one for the output",
        "Trace a FOR loop with an IF, and a WHILE loop, row by row",
        "State the final output of an algorithm from its trace table",
        "Find and correct an error in an algorithm using a trace table",
    ],
    key_concepts=["Trace table", "Dry run", "Variable values", "Loop counter", "Logic error", "Test data"],
    blocks=[
        H("Introduction"),
        T("A mobile-money agent in Limbe checks each customer's total by hand before sending it. A programmer does the same with an algorithm: **walk through it on paper** before trusting it."),
        D("A **trace table** (also called a dry run) records the value of every variable after each step of an algorithm. It shows exactly what the algorithm does with a set of test data.", title="Trace table"),
        T("The exam description for Paper 2 includes algorithm trace tables, but the syllabus topic list does not teach them. The exam description includes this, so we teach it here. In the previous lesson you learned the pseudo-code style. We use it again here. Check the current GCE Board instructions for the exact paper format."),
        H("How to build a trace table"),
        KEY("Four steps", "Follow them in this order.", cards=[
            ["1. Columns", "Make one column for each variable and one for the output."],
            ["2. Start", "Write the starting values: those set before the loop."],
            ["3. One row per pass", "Do each statement in order. Write new values only when a variable changes."],
            ["4. Stop", "Stop when the loop ends. The last row and the output column give the answer."],
        ]),
        TIP("Use your finger or a pencil to follow the line you are on. Never jump ahead. Write the value you get, not the value you expect."),
        EX("Worked example 1: a FOR loop with an IF", intro="Trace Algorithm 1 with marks[1] to marks[5] equal to 45, 62, 50, 38 and 71. What is the output?", steps=[
            S("Set up the columns", text="i, marks[i], the test marks[i] >= 50, and count."),
            S("Fill each row", text="Row i = 1: 45 >= 50 is false, so count stays 0. Row i = 2: 62 >= 50 is true, so count becomes 1. Row i = 3: 50 >= 50 is true, count 2. Row i = 4: 38 is false. Row i = 5: 71 is true, count 3."),
            S("Read the answer", text="The loop ends after i = 5. The output is 3."),
        ]),
        CODE("""count <- 0
FOR i <- 1 TO 5
    IF marks[i] >= 50 THEN
        count <- count + 1
    ENDIF
NEXT i
OUTPUT count""", "pseudocode", title="Algorithm 1. Count the passes"),
        CODE("""i | marks[i] | marks[i] >= 50 | count
- | -        | -              | 0
1 | 45       | false          | 0
2 | 62       | true           | 1
3 | 50       | true           | 2
4 | 38       | false          | 2
5 | 71       | true           | 3

Output: 3""", "text", title="Trace table for Algorithm 1"),
        T("Notice that a mark of exactly 50 passes, because the test is >= (greater than or equal). Watch the boundary carefully. This is where students lose marks."),
        H("Tracing a WHILE loop"),
        T("In a WHILE loop the variable that controls the loop changes inside the loop. Write the condition result each time, and stop the moment it is false."),
        EX("Worked example 2: the digit sum", intro="Trace Algorithm 2 for n = 4837. What does it output, and what does it do?", steps=[
            S("Start", text="n = 4837 and sum = 0. The test n > 0 is true."),
            S("Pass 1", text="digit = 4837 MOD 10 = 7. sum = 7. n = 4837 DIV 10 = 483."),
            S("Pass 2 and 3", text="digit = 3, sum = 10, n = 48. Then digit = 8, sum = 18, n = 4."),
            S("Pass 4 and stop", text="digit = 4, sum = 22, n = 0. The test n > 0 is false, so the loop ends. The output is 22, the sum of the digits."),
        ]),
        CODE("""sum <- 0
WHILE n > 0 DO
    digit <- n MOD 10
    sum <- sum + digit
    n <- n DIV 10
ENDWHILE
OUTPUT sum""", "pseudocode", title="Algorithm 2. Sum of the digits"),
        CODE("""n at start | n > 0 | digit | sum | n at end
4837       | true  | 7     | 7   | 483
483        | true  | 3     | 10  | 48
48         | true  | 8     | 18  | 4
4          | true  | 4     | 22  | 0
0          | false | -     | 22  | -

Output: 22""", "text", title="Trace table for Algorithm 2"),
        H("Finding an error"),
        T("A trace table is also the best way to find a **logic error**: the program runs, but gives the wrong answer. You choose test data where you know the right answer, trace the algorithm, and compare."),
        EX("Worked example 3: the faulty maximum", intro="Algorithm 3 should output the largest of the four numbers 12, 7, 25 and 9 but it does not. Find the error and correct it.", steps=[
            S("Trace it", text="max starts at 12. i = 2: 7 < 12 is true, so max = 7. i = 3: 25 < 7 is false, max stays 7. i = 4: 9 < 7 is false, max stays 7. Output: 7."),
            S("Compare with the expected answer", text="The largest number is 25, but the output is 7. So the algorithm has an error. It actually finds the smallest number."),
            S("Find the line", text="The test uses < (less than). It should use > (greater than)."),
            S("Check the correction", text="With >: i = 2: 7 > 12 is false, max 12. i = 3: 25 > 12 is true, max 25. i = 4: 9 > 25 is false. Output: 25. Correct."),
        ]),
        CODE("""max <- numbers[1]
FOR i <- 2 TO 4
    IF numbers[i] < max THEN        // error: should be >
        max <- numbers[i]
    ENDIF
NEXT i
OUTPUT max""", "pseudocode", title="Algorithm 3. The faulty maximum"),
        CODE("""i | numbers[i] | numbers[i] < max | max
- | -          | -                | 12
2 | 7          | true             | 7
3 | 25         | false            | 7
4 | 9          | false            | 7

Output: 7   (expected 25)""", "text", title="Trace table for the faulty Algorithm 3"),
        H("Common mistakes"),
        MISTAKE("Writing the answer you expect", "Do the steps exactly as the algorithm says. If the algorithm has an error, your trace should show the wrong output."),
        MISTAKE("Wrong loop boundary", "FOR i <- 1 TO 5 gives i = 1, 2, 3, 4, 5. WHILE n > 0 stops when n is 0, not when n is 1. Check the last pass."),
        MISTAKE("Updating variables in the wrong order", "If digit is found before n is changed, use the old n. Always follow the order of the lines."),
        MISTAKE("Forgetting the output column", "Often the output appears on one row only. Write it on the row where OUTPUT is executed."),
        QUIZ("A trace table for a WHILE loop shows the condition becoming false on row 5. What happens next?", ["The loop runs one more time", "The loop stops and the next statement after the loop runs", "The program restarts", "The condition is tested again"], 1,
             "A WHILE loop stops as soon as its condition is false, and the program continues with the line after ENDWHILE.",
             hint="What does a false condition mean for a WHILE loop?",
             feedback=["That would be wrong; the body does not run when the test is false.", "", "Nothing makes the program restart.", "The test was already done; false ends the loop."]),
        QUIZ("Why do we choose test data where we already know the correct answer?", ["To make the program faster", "To compare the trace result with the expected result and find logic errors", "To save memory", "To remove comments"], 1,
             "If you know the right answer, any difference with your trace shows an error and points to the line to check.",
             hint="Think about how you decide whether an output is wrong.",
             feedback=["Test data does not change the speed.", "", "Test data does not change memory use.", "Comments are not affected by test data."]),
        PQ("Trace this: total <- 0; FOR i <- 1 TO 4; total <- total + i multiplied by 2; NEXT i; OUTPUT total. Give each value of total.", "i = 1: total = 2. i = 2: total = 2 + 4 = 6. i = 3: total = 6 + 6 = 12. i = 4: total = 12 + 8 = 20. The output is 20."),
        PQ("Trace: x <- 100, k <- 0; REPEAT x <- x - 30, k <- k + 1 UNTIL x <= 0; OUTPUT k, x. What is the output?", "Pass 1: x = 70, k = 1; 70 <= 0 is false. Pass 2: x = 40, k = 2. Pass 3: x = 10, k = 3. Pass 4: x = -20, k = 4; -20 <= 0 is true, so stop. Output: k = 4 and x = -20."),
        PQ("An algorithm should add the numbers 1 to 5, but it contains total <- 0, FOR i <- 1 TO 4, total <- total + i, NEXT i. Use a trace table to find the output and the error.", "The loop runs for i = 1, 2, 3, 4: total = 1, 3, 6, 10. The output is 10, but the correct answer is 15. The error is the loop limit: it should be TO 5."),
        PQ("Trace Algorithm 2 (sum of the digits) for n = 905. Give the output.", "Pass 1: digit = 5, sum = 5, n = 90. Pass 2: digit = 0, sum = 5, n = 9. Pass 3: digit = 9, sum = 14, n = 0. The loop stops. The output is 14."),
        SUM(
            "A trace table has one column for each variable, plus a column for the output.",
            "Follow the algorithm exactly, one line at a time, and write only what the algorithm does.",
            "Watch the boundaries of >= and >, and where a WHILE or REPEAT loop stops.",
            "To find an error, trace with data whose correct answer you know and compare the output.",
            "The line to fix is usually the test, the loop limit or the starting value.",
        ),
    ],
))

# ------------------------------------------------------------------ 5. Database design
LESSONS.append(lesson(
    module=MODULE, topic=P2,
    title="Database design: tables, keys and relationships",
    slug="paper-2-database-design", minutes=25,
    summary="Design a small database on paper: tables, records, fields, data types, primary and foreign keys and one-to-many relationships, using a school and a shop as examples.",
    objectives=[
        "Define table, record, field, data type, primary key and foreign key",
        "Choose a suitable data type for a field",
        "Explain why one table is split into two linked tables",
        "Design a simple two-table database and show the one-to-many link",
    ],
    key_concepts=["Database", "Table", "Record", "Field", "Data type", "Primary key", "Foreign key", "One-to-many relationship"],
    blocks=[
        H("Introduction"),
        T("A school in Bamenda keeps its student list in an exercise book. Each time a student changes class, the secretary crosses out a line and rewrites it. When the list is long, mistakes creep in. A **database** keeps the same facts in an organised way so they can be searched, sorted and updated safely."),
        D("A **database** is an organised collection of related data stored so it can be searched, sorted and updated. A **relational database** stores data in tables that are linked together.", title="Database"),
        T("The exam description for Paper 2 includes database schema design, but the syllabus topic list does not teach it. The exam description includes this, so we teach it here from the beginning. Check the current GCE Board instructions for the exact paper format."),
        H("Tables, records and fields"),
        D("A **table** stores facts about one kind of thing, for example students. A **record** is one row: all the facts about one student. A **field** is one column: one kind of fact, for example the last name.", title="Table, record and field"),
        CODE("""STUDENT
student_id | first_name | last_name | date_of_birth | class_id
S001       | Amina      | Njoh      | 2009-03-14    | C1
S002       | Paul       | Tabi      | 2008-11-02    | C1
S003       | Grace      | Fon       | 2009-07-21    | C2
S004       | Samuel     | Ndi       | 2009-01-30    | C1
S005       | Linda      | Mbah      | 2008-12-09    | C2""", "text", title="A STUDENT table with 5 records and 5 fields"),
        T("The table has 5 records (5 rows) and 5 fields (5 columns). The first row of names is the **field names**. It is not a record."),
        H("Data types"),
        D("A **data type** tells the database what kind of value a field can hold. This prevents errors, for example a letter typed in a field meant for a price.", title="Data type"),
        KEY("Common data types", "Choose the type that matches the facts and what you will do with them.", cards=[
            ["Text", "Letters, digits and symbols: names, addresses, phone numbers."],
            ["Integer", "Whole numbers: number of copies, age in years."],
            ["Real (decimal)", "Numbers with a fraction: height in metres, a price of 1250.50."],
            ["Date", "A calendar date: date of birth, date of purchase."],
            ["Boolean (yes/no)", "Only two values: paid or not paid."],
        ]),
        TIP("A telephone number is **text**, not a number. You never add phone numbers together, and a number type could remove a leading zero or a plus sign."),
        H("Keys and the one-to-many link"),
        D("A **primary key** is a field whose value is different in every record, so it identifies one record only. Names are not good primary keys because two students may have the same name. An ID such as S001 is better.", title="Primary key"),
        D("A **foreign key** is a field in one table that holds the primary key value of a record in another table. It creates the link between the two tables.", title="Foreign key"),
        T("In the STUDENT table above, class_id is a foreign key. It links each student to a record in a CLASS table. Student S001 has class_id C1, so S001 belongs to class C1."),
        CODE("""CLASS
class_id | class_name | teacher  | room
C1       | Form 5A    | Mrs Ngu  | R12
C2       | Form 5B    | Mr Atem  | R14""", "text", title="The CLASS table (class_id is the primary key)"),
        T("Why not write the teacher's name and the room on every student record? Then the same facts would be repeated many times. If the teacher changes, you would have to correct every student record, and you could forget one. With two tables the teacher is stored **once**."),
        D("In a **one-to-many relationship**, one record in the first table can be linked to many records in the second table, but each record in the second table links to only one in the first. One class has many students. Each student belongs to one class.", title="One-to-many relationship"),
        IMG("f5c-school-er.svg", alt="Two boxes: CLASS with class_id as primary key, STUDENT with student_id as primary key and class_id as foreign key, joined by a line labelled 1 and many", caption="Figure 5. One class has many students. The foreign key class_id joins the two tables."),
        EX("Worked example 1: read the tables", intro="Using the STUDENT and CLASS tables above, how many students are in class C1, and who is the teacher of Grace Fon?", steps=[
            S("Count the foreign key value C1", text="S001, S002 and S004 have class_id C1. That is 3 students."),
            S("Find Grace's class", text="Grace Fon (S003) has class_id C2."),
            S("Look up C2 in the CLASS table", text="C2 is Form 5B and the teacher is Mr Atem."),
        ]),
        EX("Worked example 2: design a shop database", intro="A shop in Douala sells products in categories such as drinks and soap. Design two tables to avoid repeating the category name for every product.", steps=[
            S("Find the two things", text="Products and categories. Each category has many products; each product has one category."),
            S("Write the tables and keys", text="CATEGORY has category_id (primary key) and category_name. PRODUCT has product_id (primary key), product_name, unit_price and category_id (foreign key)."),
            S("Choose data types", text="category_id and product_id: text such as P001. product_name: text. unit_price: integer, because FCFA prices are normally whole numbers. category_id in PRODUCT: the same type as in CATEGORY."),
        ]),
        CODE("""CATEGORY (category_id, category_name)
PRODUCT  (product_id, product_name, unit_price, category_id)

Primary keys: category_id in CATEGORY, product_id in PRODUCT
Foreign key : category_id in PRODUCT
Link        : one category has many products""", "text", title="Schema for the shop"),
        H("What makes a good field"),
        KEY("Good design habits", "Check each field against these points.", cards=[
            ["One fact per field", "Store first_name and last_name separately, not full_name. Then you can sort by last name."],
            ["Store, do not calculate", "Store date_of_birth, not age. Age changes every year; the date does not."],
            ["Right data type", "Dates as date, prices as numbers, phone numbers as text."],
            ["Clear names", "Use one word or words joined by an underscore: first_name, not Name of the child."],
            ["A primary key", "Every table needs one field that identifies each record."],
        ]),
        EX("Worked example 3: choose data types", intro="Choose the best data type for each field: (a) price in FCFA (b) date of enrolment (c) paid_fees (yes or no) (d) phone number.", steps=[
            S("(a) Price", text="Integer, because prices in FCFA are whole numbers. Real (decimal) is needed only if you store fractions."),
            S("(b) Date of enrolment", text="Date."),
            S("(c) paid_fees", text="Boolean (yes/no). There are only two values."),
            S("(d) Phone number", text="Text, because we never calculate with it and it may start with a plus sign or a zero."),
        ]),
        MISTAKE("Using a name as a primary key", "Two people can share a name. Use an ID field that is different in every record."),
        MISTAKE("Putting the foreign key in the wrong table", "In a one-to-many link, the foreign key goes in the table on the many side. The STUDENT table (many) holds class_id, not the CLASS table."),
        MISTAKE("Storing age", "Age changes. Store the date of birth and work out the age when you need it."),
        MISTAKE("Mixing up record and field", "A record is a row (one student). A field is a column (one kind of fact)."),
        QUIZ("In a database of books and the library members who borrowed them, which is the best primary key for the MEMBER table?", ["The member's last name", "The member's date of birth", "A unique member_id", "The member's home town"], 2,
             "A primary key must be different for every record. A unique member_id is guaranteed to be different.",
             hint="Which field can never be the same for two members?",
             feedback=["Two members can share a last name.", "Two members may be born on the same day.", "", "Many members live in the same town."]),
        QUIZ("A SUBJECT table has one record per subject, and a TEACHER table has one record per teacher. Each teacher teaches one subject, but a subject has many teachers. Where does the foreign key go?", ["In SUBJECT, pointing to TEACHER", "In TEACHER, holding the subject_id", "In both tables", "No foreign key is needed"], 1,
             "The foreign key goes on the many side. Many teachers share one subject, so each TEACHER record holds a subject_id.",
             hint="Which table is the many side?",
             feedback=["That would allow only one teacher per subject.", "", "A single foreign key on the many side is enough for a one-to-many link.", "Without a foreign key the two tables would not be linked."]),
        PQ("A library has books and borrowers. Write the field names for two tables, BORROWER and LOAN, where one borrower can have many loans. Name the primary keys and the foreign key.", "BORROWER (borrower_id, first_name, last_name, phone). LOAN (loan_id, book_title, date_borrowed, borrower_id). Primary keys: borrower_id and loan_id. Foreign key: borrower_id in LOAN, because one borrower has many loans."),
        PQ("Explain why a school database stores date_of_birth rather than age.", "Age changes every year, so the stored age would become wrong and would need updating for every student. The date of birth never changes, and the age can always be worked out from it."),
        PQ("State the data type you would use for each field: (a) pass_mark, a whole number out of 100, (b) email_address, (c) date_of_exam.", "(a) Integer. (b) Text. (c) Date."),
        PQ("A table PRODUCT repeats the supplier name and supplier phone on every product record. Explain two problems and a better design.", "Problem 1: the same data is stored many times, which wastes space. Problem 2: if the supplier changes phone, every product record must be changed, and a record may be missed so the data disagree. Better design: a SUPPLIER table (supplier_id, supplier_name, phone) and a PRODUCT table with supplier_id as a foreign key."),
        SUM(
            "A table holds facts about one kind of thing. A record is a row and a field is a column.",
            "A data type fits each field: text, integer, real, date or Boolean. Phone numbers are text.",
            "A primary key identifies each record. A foreign key holds the primary key of another table and creates the link.",
            "In a one-to-many relationship the foreign key goes in the many table.",
            "Good fields hold one fact, are not calculated, have the right type and have a clear name.",
        ),
    ],
))

# ------------------------------------------------------------------ 6. Word processing and spreadsheet tasks
LESSONS.append(lesson(
    module=MODULE, topic=P3,
    title="Word processing and spreadsheet tasks",
    slug="paper-3-word-processing-and-spreadsheet-tasks", minutes=25,
    summary="Plan a timed practical lab, then practise the typical word-processing tasks (formatting, tables, headers, page layout) and spreadsheet tasks (formulas, functions, absolute references, charts) with a checklist.",
    objectives=[
        "Plan a timed practical session: read, save early, name files correctly and check your work",
        "Choose the right word-processing feature for a formatting or layout instruction",
        "Write spreadsheet formulas with SUM, AVERAGE, MAX, MIN, COUNT and IF",
        "Explain relative and absolute references and choose a suitable chart",
    ],
    key_concepts=["Timed practical", "File name", "Formatting", "Header and footer", "Formula", "Function", "Absolute reference", "Chart"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is a hands-on practical in the computer lab. You work on a computer, follow written instructions, save your files and hand them in. It tests what your hands can do, not only what you remember."),
        T("The guide describes Paper 3 as a timed lab covering word processing, spreadsheet modelling, relational database work and basic web design. For the length of the paper, the number of tasks and the software used, check the current GCE Board instructions and ask your teacher. This lesson covers word processing and spreadsheets. The next lesson covers databases and web design."),
        T("Lab programs have different names, such as Microsoft Word and Excel or LibreOffice Writer and Calc. The buttons move around, but the ideas are the same. We describe the feature, and you find it in your own software during lab practice."),
        H("How to work in a timed lab"),
        KEY("Six habits that save marks", "Practise these in every lab session, not only before the exam.", cards=[
            ["Read all the tasks first", "Spend the first few minutes reading the whole paper. Note the file names you must use."],
            ["Plan your time", "Share the time between the tasks. Do not spend half the paper on one table."],
            ["Save early and often", "Save the file with the correct name as soon as you start. Save again after each task."],
            ["Name files exactly", "Use the file name and file type that the instructions give. A wrong name may mean the marker cannot find your work."],
            ["Follow every word", "If the task says 14 point, bold and centred, do all three."],
            ["Check before you finish", "Read each instruction again and compare it with your screen. Spell check your text."],
        ]),
        TIP("If you are stuck on one step, leave it, do the rest, and come back. A half-finished task still earns the marks for the parts you did."),
        H("Word-processing tasks"),
        T("A word-processing task usually gives you some text and asks you to change how it looks or where it sits on the page. Match each instruction to its feature."),
        CODE("""Instruction in the task               Feature to use
-----------------------------------   -------------------------------
Make the title bigger and bold         Font size, bold
Change the font style                  Font (typeface)
Centre the heading                     Alignment: centre
Space between lines                    Line spacing
Margins of 2.5 cm                      Page layout: margins
Print sideways                         Page orientation: landscape
Page numbers at the bottom             Footer with page number field
School name on every page              Header
Show items in a list                   Bullets or numbering
Arrange data in rows and columns       Insert table
Join cells in a table                  Merge cells
Put a picture beside the text          Insert picture, text wrapping
Change every Doualla to Douala         Find and replace
Correct spelling                       Spell check""", "text", title="Word-processing instructions and features"),
        MISTAKE("Spaces instead of formatting", "Do not press the space bar many times to centre text, and do not press Enter at the end of every line. Use alignment, indent and tab settings. Typed spaces break when the text changes."),
        MISTAKE("Typing page numbers by hand", "Use the page-number feature in the header or footer. A number you type shows the same on every page."),
        MISTAKE("Wrong order of steps", "Select the text first, then apply the format. Nothing happens if nothing is selected."),
        H("Spreadsheet tasks"),
        T("A spreadsheet is a grid of cells. Each cell has a name made of its column letter and row number, such as B3. A **formula** starts with an equals sign and calculates a value. When the numbers change, the answer changes automatically."),
        D("A **function** is a ready-made calculation. SUM adds, AVERAGE finds the mean, MAX gives the largest, MIN gives the smallest, COUNT counts numbers, and IF chooses between two results.", title="Common functions"),
        CODE("""=B2*C2              multiply B2 by C2
=SUM(D2:D4)         add the cells D2 to D4
=AVERAGE(B2:B6)     the mean of B2 to B6
=MAX(B2:B6)         the largest value
=MIN(B2:B6)         the smallest value
=COUNT(B2:B6)       how many cells hold numbers
=IF(D2>=5000,"High","Low")    one of two results""", "text", title="Spreadsheet formulas"),
        H("Relative and absolute references"),
        T("When you copy a formula down a column, the cell names in it move with it. This is a **relative reference**. If the formula in row 2 uses B2, the copy in row 3 uses B3. This is usually what you want."),
        T("Sometimes one cell must stay fixed, such as a commission rate stored in G1. Then you write dollar signs before the column letter and the row number. This is an **absolute reference**. It does not change when copied."),
        EX("Worked example 1: formulas for a shop sheet", intro="Cells A2 to C4 hold the item, quantity and unit price. Cell G1 holds a commission rate of 0.05. Write the formulas for total (column D) and commission (column E), and find the sum of the totals.", steps=[
            S("Total in D2", text="Multiply the quantity by the unit price: multiply B2 by C2 (see the formulas under the table). Copy it down to D4."),
            S("Commission in E2", text="Multiply D2 by the fixed rate in G1. G1 must be an absolute reference, with dollar signs before its column letter and its row number. Copy the formula down. If G1 were relative, the copy in row 3 would use G2 and give a wrong result."),
            S("Sum of the totals", text="In D5 use the SUM function on D2 to D4. The totals are 10000, 3600 and 4500, so the sum is 18100. The commissions are 500, 180 and 225."),
        ]),
        CODE("""     A      B         C           D        E
1  Item   Quantity  Unit price  Total    Commission     (G1 holds 0.05)
2  Rice   4         2500        10000    500
3  Oil    2         1800        3600     180
4  Sugar  5         900         4500     225
5                              18100    905

D2: =B2*C2         E2: =D2*$G$1         D5: =SUM(D2:D4)""", "text", title="The shop sheet with its formulas"),
        EX("Worked example 2: an IF formula", intro="In column F, show High if the total is at least 5000 and Low otherwise. What does the sheet show for each row?", steps=[
            S("Write the formula in F2", text='=IF(D2>=5000,"High","Low"). Copy it down.'),
            S("Rice", text="D2 = 10000, which is at least 5000, so High."),
            S("Oil and Sugar", text="3600 and 4500 are less than 5000, so Low and Low."),
        ]),
        H("Formatting and charts"),
        T("Format numbers as the task says: currency, a given number of decimal places, a percentage. Widen columns so no numbers show as hash signs. Keep your headings clear."),
        KEY("Choosing a chart", "Pick the chart that shows what the question asks.", cards=[
            ["Bar or column chart", "Compare separate groups, for example sales of each item."],
            ["Line chart", "Show how something changes over time, for example monthly sales."],
            ["Pie chart", "Show parts of one whole, for example how a budget is shared."],
        ]),
        TIP("A chart needs a title, labels on the axes (or labels on the slices of a pie), and the correct data range. Select the labels and numbers together before you insert it."),
        MISTAKE("Typing numbers instead of formulas", "If the task asks for a total, write =SUM(...). A typed total will not update, and it may score no marks for the method."),
        MISTAKE("A wrong range", "SUM(D2:D3) misses D4. Check the first and last cell of your range on the screen."),
        CODE("""Final checklist before you finish
[ ] Files saved with the exact names and types asked for
[ ] Every formatting instruction done (font, size, alignment, spacing)
[ ] Header, footer and page numbers present where asked
[ ] Tables and charts have the right data and clear headings
[ ] Formulas used, not typed answers; absolute references where needed
[ ] Spell check done; no text hidden or cut off
[ ] Final save""", "text", title="Checklist for word-processing and spreadsheet tasks"),
        QUIZ("D2 holds the formula that multiplies B2 by C2. You copy it down to D3. What does D3 multiply?", ["B2 by C2 again", "B3 by C3", "B2 by C3", "B3 by C2"], 1,
             "Relative references move with the formula. Moving down one row changes B2 to B3 and C2 to C3.",
             hint="Both references change by the same number of rows.",
             feedback=["That would happen only with absolute references.", "", "Only the second reference changed, but both should.", "Only the first reference changed, but both should."]),
        QUIZ("A tax rate is stored in H1 and must stay fixed when a formula is copied down. How do you write the reference to H1?", ["H1 with no change", "H1 with dollar signs before the column letter and the row number", "H plus 1", "A new cell for each row"], 1,
             "Dollar signs before both the column letter and the row number make the reference absolute, so it does not move when copied.",
             hint="What makes a reference absolute?",
             feedback=["A plain H1 is relative and moves to H2 in the next row.", "", "That is not a cell reference.", "That would make the sheet longer and does not fix the reference."]),
        PQ("A task says: put the school name and the page number at the bottom of every page, in 10 point. Name the features you will use.", "Use the footer feature (insert footer). Type the school name in the footer and insert the page-number field, not a typed number. Select the footer text and set the font size to 10 point. Check the footer on the second page."),
        PQ("Write a formula that gives the average of the marks in B2 to B6 and a formula that shows Pass if the average (in C2) is at least 50, otherwise Fail.", "=AVERAGE(B2:B6) gives the average. =IF(C2>=50,\"Pass\",\"Fail\") shows the result. The test uses greater than or equal, so exactly 50 passes."),
        PQ("Which chart suits each: (a) monthly rainfall over a year, (b) how a family budget is shared, (c) the number of students in each class?", "(a) A line chart, because it shows change over time. (b) A pie chart, because the budget is one whole shared into parts. (c) A bar or column chart, because it compares separate groups."),
        PQ("List four checks to make in the last minutes of a practical session.", "Any four of: files saved with the exact names; every instruction read again and done; spell check; formulas used instead of typed answers; header, footer and page numbers present; chart titles and labels; final save."),
        SUM(
            "In a timed lab, read all the tasks, plan your time, save early and often, and use the exact file names.",
            "Match each word-processing instruction to its feature: font, alignment, spacing, margins, orientation, header and footer, table.",
            "A formula starts with an equals sign. Use SUM, AVERAGE, MAX, MIN, COUNT and IF.",
            "Relative references move when copied. Absolute references, with dollar signs, stay fixed.",
            "Choose bar charts to compare groups, line charts for change over time and pie charts for parts of a whole, and label them.",
        ),
    ],
))

# ------------------------------------------------------------------ 7. Database and web design tasks
LESSONS.append(lesson(
    module=MODULE, topic=P3,
    title="Database and web design tasks",
    slug="paper-3-database-and-web-design-tasks", minutes=25,
    summary="Practise the timed database tasks (create a table, enter data, sort and query) and the web tasks (build and style a small page and test it in a browser), with checklists and common slips.",
    objectives=[
        "Create a database table with field names, data types and a primary key",
        "Sort records and write a query with selection criteria",
        "Build and style a small web page with a text editor and test it in a browser",
        "Avoid the common slips in file names, paths and saving",
    ],
    key_concepts=["Table design view", "Data entry", "Sort", "Query", "Criteria", "HTML page", "Internal CSS", "Browser test"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you learned how to work in a timed lab and how to do word-processing and spreadsheet tasks. This lesson covers the other two areas in the guide: relational database work and basic web design."),
        T("The software differs between labs. Many labs use a desktop database program with a design view and a query grid, and a plain text editor with a browser for web pages. Check the current GCE Board instructions and your teacher's notes for what is used in your centre. The ideas below do not change."),
        H("Database tasks"),
        T("A typical task: create a table, enter some records, sort them, and answer a question by writing a query. You learned in the previous topic why tables are designed with keys. Now you do it on the computer."),
        KEY("Steps for a table task", "Work in this order.", cards=[
            ["1. Create the table", "Open the table in design view. Type each field name and choose its data type."],
            ["2. Set the primary key", "Mark one field (such as student_id) as the primary key."],
            ["3. Save the table", "Save it with the name the task gives, for example STUDENT."],
            ["4. Enter the data", "Open the table in data view and type each record exactly as given. Check spelling."],
        ]),
        CODE("""Field name       Data type     Notes
student_id       Text          Primary key
first_name       Text
last_name        Text
date_of_birth    Date
class_id         Text          Foreign key to the CLASS table
fees_paid        Yes/No""", "text", title="Design view of the STUDENT table"),
        TIP("Type the data carefully. A mistake such as Form5A instead of Form 5A will stop the record appearing in a query."),
        H("Sorting and querying"),
        D("**Sorting** puts records in order (A to Z, smallest to largest, or newest to oldest) using one field. A **query** asks the database a question. It shows only the records that match the **criteria** and the fields you choose.", title="Sort and query"),
        T("Most database programs let you build a query in a grid. You pick the fields to show, type the criteria in the row of the field, and choose the sort order. Behind the grid, the question can be written in SQL. The idea of the query is the same. The following example is written in SQL only to make the question clear."),
        CODE("""STUDENT
student_id | first_name | last_name | date_of_birth | class_id | fees_paid
S001       | Amina      | Njoh      | 2009-03-14    | C1       | yes
S002       | Paul       | Tabi      | 2008-11-02    | C1       | no
S003       | Grace      | Fon       | 2009-07-21    | C2       | yes
S004       | Samuel     | Ndi       | 2009-01-30    | C1       | yes
S005       | Linda      | Mbah      | 2008-12-09    | C2       | no""", "text", title="Data used in the examples"),
        EX("Worked example 1: sort", intro="Sort the STUDENT table by last name from A to Z. Give the order of the last names.", steps=[
            S("Choose the sort field", text="Select the last_name field."),
            S("Choose ascending order", text="Ascending means A to Z."),
            S("Read the result", text="Fon, Mbah, Ndi, Njoh, Tabi."),
        ]),
        EX("Worked example 2: a query with two criteria", intro="List the first name and last name of students in class C1 whose fees are paid, in order of last name.", steps=[
            S("Show these fields", text="first_name and last_name."),
            S("Add the criteria", text="class_id equals C1 and fees_paid is yes. Both must be true, so they go in the same criteria row."),
            S("Sort", text="last_name ascending."),
            S("Result", text="Samuel Ndi and Amina Njoh. Paul Tabi is in C1 but has not paid, so he is not shown."),
        ]),
        CODE("""SELECT first_name, last_name
FROM student
WHERE class_id = 'C1' AND fees_paid = 'yes'
ORDER BY last_name;

Result:
first_name | last_name
Samuel     | Ndi
Amina      | Njoh""", "sql", title="The same query written in SQL"),
        MISTAKE("AND and OR in the criteria", "Criteria in the same row mean AND. Criteria in different rows mean OR. Placing criteria in the wrong rows gives the wrong records."),
        MISTAKE("Not saving the query", "If the task says to save the query, give it the name asked for. Name it before you close the window."),
        H("Web design tasks"),
        T("A web task asks you to build a small page, style it and test it. You write the HTML in a plain text editor, save it as a file ending in .html, and open it in a browser. You met the tags and the style rules in the Web Design topic of this course. Now you use them under time pressure."),
        KEY("Steps for a web task", "Work in small steps and test often.", cards=[
            ["1. Prepare the folder", "Put the page and its image in the same folder."],
            ["2. Write the structure", "Doctype, html, head with title, and body."],
            ["3. Add content", "Headings, paragraphs, a list, an image with alt text, a table, a link."],
            ["4. Add CSS", "Colours, fonts, table borders, centred heading."],
            ["5. Test in the browser", "Save, open the file, look at the result, and change what is wrong."],
        ]),
        CODE("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mountain View Computer Club</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
    h1 { color: #1a5276; text-align: center; }
    table { border-collapse: collapse; }
    th, td { border: 1px solid #333333; padding: 6px; }
  </style>
</head>
<body>
  <h1>Mountain View Computer Club</h1>
  <p>We meet to learn computing skills and build web pages.</p>
  <img src="club.jpg" alt="Club members in the computer lab" width="300">
  <h2>Meeting days</h2>
  <ul>
    <li>Tuesday after school</li>
    <li>Friday after school</li>
  </ul>
  <table>
    <tr><th>Level</th><th>Room</th></tr>
    <tr><td>Form 4</td><td>Lab 1</td></tr>
    <tr><td>Form 5</td><td>Lab 2</td></tr>
  </table>
  <p><a href="contact.html">Contact us</a></p>
</body>
</html>""", "html", title="A small page that meets a typical task"),
        EX("Worked example 3: check the page against the task", intro="The task said: use the title Mountain View Computer Club, centre the main heading in blue, add a picture with alt text, a bulleted list of two meeting days and a table with a header row. Does the page above meet it?", steps=[
            S("Title", text="The title element holds the required name."),
            S("Heading", text="The h1 rule gives a blue colour and text-align: center."),
            S("Picture", text='The img tag has src="club.jpg" and alt text. The picture file must be in the same folder as the page.'),
            S("List and table", text="The ul has two li items. The table has a row of th cells for the header row, and the CSS adds borders."),
        ]),
        H("Testing and common slips"),
        T("Always open your page in the browser after saving. Look at it as the marker will. Click the link. Check that the picture shows. If the picture is missing, check the file name, the capital letters, and whether it is in the same folder."),
        CODE("""Common slips and their cure
Page opens as plain text         saved as .txt; save again as .html
Picture not shown                wrong file name or folder; check src
Style has no effect              typing error in the CSS; check braces and semicolons
Everything after a tag looks big missing closing tag, such as a missing end of h1
Changes do not appear            file not saved, or the browser was not refreshed
Marker cannot find the file      wrong file name or saved in the wrong folder""", "text", title="Web page problems"),
        CODE("""Final checklist for database and web tasks
[ ] Table saved with the right name, fields, data types and primary key
[ ] All records typed exactly as given
[ ] Sort and query use the right fields, criteria and order, and are saved
[ ] Web page saved as .html in the right folder with the exact file name
[ ] Title, headings, list, table, image with alt text and link as asked
[ ] CSS gives the requested colours, alignment and borders
[ ] Page opened in a browser and checked after the last save""", "text", title="Checklist"),
        QUIZ("In a query, class_id = C1 is in the same criteria row as fees_paid = yes. Which records are shown?", ["Records in C1 or with fees paid", "Records in C1 and with fees paid", "Records with fees not paid", "All records"], 1,
             "Criteria in the same row are joined by AND. A record must satisfy both.",
             hint="Same row means AND.",
             feedback=["That would be criteria in different rows.", "", "That is the opposite of the criterion fees_paid = yes.", "A query with criteria filters the records."]),
        QUIZ("Your web page shows as lines of HTML tags in the browser instead of a formatted page. What is the most likely cause?", ["The file was saved as a .txt file", "The title is too long", "The image is too large", "The CSS has no colours"], 0,
             "A browser formats a file only if it is an HTML file. A file saved as .txt is shown as plain text.",
             hint="Look at the file extension.",
             feedback=["", "A long title only changes the tab text.", "A large image does not turn the page into plain text.", "Missing colours would change the look but not show tags."]),
        PQ("A task says: Create a table called BOOK with fields book_id, title, author, year_published and on_loan (yes/no). Which data types and which primary key do you choose?", "book_id: text (or a number), set as the primary key. title: text. author: text. year_published: integer. on_loan: yes/no (Boolean). Save the table with the name BOOK."),
        PQ("Describe how to produce a list of students born after 1 January 2009, in order of date of birth with the oldest first.", "Create a query on STUDENT. Show first_name, last_name and date_of_birth. In the criteria row of date_of_birth, type greater than 2009-01-01 (in the date format used by the program). Sort date_of_birth ascending, so the earliest date, the oldest student, comes first. Save the query with the name given."),
        PQ("A student wrote the link as href='Contact.html' but the file on disk is contact.html, and the link fails in the lab. Explain and correct it.", "File names are matched exactly on many systems, including capital letters. The link must use the same name as the file: contact.html. Always copy the exact file name from the task or the folder."),
        PQ("List the steps you take to test a web page in the last five minutes.", "Save the file. Open (or refresh) it in the browser. Check the title in the tab, the heading, the image, the list and the table. Click each link. Fix any problem in the editor, save, and refresh again. Make a final save and check the file name."),
        SUM(
            "For a table task: set field names and data types, choose a primary key, save with the right name and type the data exactly.",
            "Sort with one field and an order. A query shows chosen fields for records that match all the criteria in one row.",
            "A web page is an HTML file saved with the .html ending, in a folder with its picture.",
            "Add the structure, then content, then CSS, then test in a browser after each save.",
            "Most lost marks are slips: wrong file names, wrong folders, unsaved work, wrong criteria rows. Use the checklists.",
        ),
    ],
))
