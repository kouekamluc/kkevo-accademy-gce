"""Form 5 Computer Science (O Level 0595): Examination module, Paper 1 lesson.

Draft content. The only exam facts stated here come from the syllabus outline in
apps/academics/gce_curriculum.py: Paper 1 is a 1.5-hour multiple-choice paper covering the whole syllabus.
The number of questions and every other instruction are left to the current GCE Board instructions.
"""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "form-5")

LESSONS = [
    lesson(
        module="Examination", topic="Paper 1",
        title="Paper 1: multiple-choice strategies",
        slug="paper-1-multiple-choice-strategies-cs",
        minutes=25,
        summary="How Paper 1 works (1.5 hours of multiple choice on the whole syllabus) and five strategies: two passes, "
                "elimination, spotting absolute words, tracing code and logic, and avoiding the traps in each topic.",
        objectives=[
            "Describe Paper 1 and work out a time budget from the number of questions",
            "Use the two-pass method and eliminate options you know are wrong",
            "Spot absolute words such as always and never, and test them",
            "Trace code and logic by hand, and recognise the common traps in each syllabus area",
        ],
        key_concepts=["Paper 1 format", "Time budget", "Two-pass method", "Elimination", "Absolute words", "Tracing",
                      "Distractor"],
        blocks=[
            H("Introduction"),
            T("Paper 1 tests the **whole syllabus** in one sitting: web pages, CSS, intellectual property, the "
              "Cameroonian legal framework, the social and economic impact of computers, and the skills you also need "
              "for Paper 2 (logic gates, pseudo-code, trace tables and database design). Every question is short. "
              "Marks are won by speed, care and a clear head. Picture a candidate in a Buea exam hall who spends six minutes on one tricky question and then rushes the last twelve: good strategy would have saved her those marks."),
            D("Paper 1 is a **multiple-choice** paper. It lasts **1.5 hours** (90 minutes) and covers the **whole syllabus**. "
              "For each question you choose one answer from the options given.",
              title="Paper 1 at a glance",
              note="The syllabus guide does not give the number of questions or the rules for recording answers. Check the "
                   "current GCE Board instructions and your teacher's notes for those, and listen to your invigilator."),
            KEY("Your time budget",
                "Divide 90 minutes by the number of questions on your paper. KKEVO's own mock paper has 50 questions, "
                "so it uses 90 ÷ 50 = 1.8 minutes (about 1 minute 48 seconds) for each question.",
                cards=[["First pass", "Answer every question you can do quickly. Mark the hard ones and move on."],
                       ["Second pass", "Go back to the marked questions with the time you saved."],
                       ["Last minutes", "Check that every question has an answer and that each answer is on the right line."]]),
            H("Strategy 1: the two-pass method"),
            T("An average is not a limit for every question. A definition may take 20 seconds. A trace through a loop may take "
              "three minutes. If a question is taking much longer than your average, mark it, choose a temporary answer if "
              "the instructions allow it, and move on. On the second pass you have the time you saved. Check the current GCE Board instructions on whether a wrong answer loses marks; if it does not, a blank answer can never earn a mark."),
            H("Strategy 2: eliminate wrong options"),
            EX("Worked example 1: eliminating options", intro=(
                'In the tag <img src="logo.png" alt="School logo">, which word is the name of an attribute? '
                'A: img. B: src. C: logo.png. D: School logo.'), steps=[
                S("Recall what an attribute is", text="An attribute is a name inside the opening tag that gives extra "
                                                      "information. It is followed by an equals sign and a value in quotes."),
                S("Eliminate by position", text='The words in quotes, logo.png and School logo, are **values**, not attribute '
                                                'names. C and D are out.'),
                S("Eliminate by role", text="img comes straight after the angle bracket. It is the **tag name**, so A is out."),
                S("Answer", text="**B**. src is the attribute name, and logo.png is its value. (alt is also an attribute name, but it is not one of the options.)"),
            ]),
            H("Strategy 3: test absolute words"),
            T("Words such as **always**, **never**, **all**, **only** and **no** claim that something is true without a "
              "single exception. Computing and the law have many exceptions, so an option with an absolute word is often "
              "(not always!) a false statement."),
            EX("Worked example 2: absolute words", intro=(
                "Which statement about open-source software is correct? "
                "A: Open-source software is always free of charge. "
                "B: The source code is published, and users may study, change and share it under the licence terms. "
                "C: Open-source software can never be sold. "
                "D: Open-source software has no licence."), steps=[
                S("Underline the absolute words", text='A says "always". C says "never". D says "no licence".'),
                S("Test each one with a counter-example", text="A: someone may charge for a copy or for support. C: the same. "
                                                               "D: open-source software always comes with a licence such as the GPL or the MIT licence. "
                                                               "A, C and D each have an exception, so they are false."),
                S("Check the remaining option", text="B has no absolute word and matches the definition of open source."),
                S("Answer", text="**B**."),
            ]),
            H("Strategy 4: trace code and logic by hand"),
            T("When a question gives you a few lines of pseudo-code or a small logic circuit, do not guess. Follow it "
              "step by step on paper, exactly as the computer would. Write down the value of each variable after every line."),
            CODE("""total ← 0
FOR i ← 1 TO 4
    total ← total + i × 2
NEXT i
OUTPUT total""", "pseudocode", title="Listing 1", caption="Used in worked example 3."),
            EX("Worked example 3: tracing pseudo-code", intro=(
                "What does the algorithm in Listing 1 output? A: 10. B: 20. C: 8. D: 52."), steps=[
                S("Start", text="total is 0."),
                S("Pass 1 (i = 1)", math=r"\text{total} = 0 + 1 \times 2 = 2"),
                S("Pass 2 (i = 2)", math=r"\text{total} = 2 + 2 \times 2 = 6"),
                S("Pass 3 and pass 4", math=r"6 + 3 \times 2 = 12, \quad 12 + 4 \times 2 = 20"),
                S("Answer", text="**B**: the output is 20. Option A is what you get if you forget the multiplication by 2 "
                                 "(1 + 2 + 3 + 4). Option C is just the last value of i times 2. Option D doubles the whole total "
                                 "on every pass, which is not what the line says."),
            ]),
            CODE("""A B | A AND B | NOT (A AND B) | NOT (A OR B)
0 0 |    0     |       1       |      1
0 1 |    0     |       1       |      0
1 0 |    0     |       1       |      0
1 1 |    1     |       0       |      0""", "text", title="Listing 2", caption="NAND is NOT (A AND B). NOR is NOT (A OR B)."),
            EX("Worked example 4: tracing a circuit", intro=(
                "X = (NOT A) OR (B AND C). Find X when A = 1, B = 1 and C = 0."), steps=[
                S("Left gate", math=r"\text{NOT } A = \text{NOT } 1 = 0"),
                S("Right gate", math=r"B \text{ AND } C = 1 \text{ AND } 0 = 0"),
                S("Final OR gate", math=r"0 \text{ OR } 0 = 0"),
                S("Answer", text="X = 0. The OR gate gives 1 only when at least one input is 1, and here both are 0."),
            ], check=r"X = 1 \text{ needs } A = 0 \text{ or } (B = 1 \text{ and } C = 1)"),
            H("Strategy 5: know the traps in each topic"),
            KEY("Traps to watch for", "Question writers choose wrong options from real mistakes. Learn them.",
                cards=[["HTML5", "A tag is in angle brackets. An attribute sits inside the opening tag (href, src, alt). The closing tag has a slash and no attributes. Tags must close in the reverse order of opening."],
                       ["CSS", "A class selector starts with a dot and an id selector starts with a hash. Each declaration is property, colon, value, semicolon. CSS spells it center and color. Box model, inside to outside: content, padding, border, margin."],
                       ["Intellectual property", "Copyright protects the work itself (the code, text, music, image), not the idea. Freeware is free to use but its code is closed, unlike open source. NC in Creative Commons means non-commercial."],
                       ["Cameroon legal framework", "Law No. 2010/012 is cybersecurity and cybercrime. Law No. 2010/013 is electronic communications. Both are dated 21 December 2010. MINPOSTEL is the ministry that makes policy. ANTIC is the agency for ICT activity and network security."],
                       ["Social and economic impact", "The digital divide is about access and skills, not only money. Automation removes some jobs and creates others. Discussion answers need both sides."],
                       ["Paper 2 skills", "Check NAND and NOR, boundaries such as greater than against greater than or equal to, and the difference between a primary key and a foreign key."]]),
            EX("Worked example 5: copyright or licence?", intro=(
                "Which sentence is correct? "
                "A: Copyright is the creator's legal right to control copying; a licence is the agreement that tells a user what they may do with a copy. "
                "B: A licence is the creator's legal right; copyright is the agreement. "
                "C: Copyright and licence mean exactly the same thing. "
                "D: A licence can never limit how you use software."), steps=[
                S("Spot the absolute word", text='D says "never". Licences often limit copying, changing and sharing, so D is false.'),
                S("Spot the claim of sameness", text="C says the two terms mean exactly the same. They do not: one is a right, the other is permission."),
                S("Compare A and B", text="B swaps the two terms. Copyright belongs to the creator from the moment the work is created. "
                                          "A licence is what the owner gives to users."),
                S("Answer", text="**A**."),
            ]),
            MISTAKE("Choosing the first familiar-looking option",
                    "A wrong option is built to look familiar. Finding your answer among the options does not prove it is right. "
                    "Read all four options before you choose."),
            QUIZ("You are working through a paper and one question is taking much longer than the average time. "
                 "What does the two-pass method tell you to do?",
                 ["Keep working until you have solved it",
                  "Mark it, move on, and return to it after the first pass",
                  "Leave it blank and never look at it again",
                  "Go back and change your answers to the easy questions"], 1,
                 "Marking a hard question and returning later lets you collect the easy marks first.",
                 hint="Think about which questions are cheapest to answer.",
                 feedback=["That can use up time that other questions need.", "",
                           "A question you skip and forget can never earn a mark.",
                           "Changing correct answers without a reason can lose marks you had already earned."]),
            QUIZ("An algorithm runs: x ← 5, then y ← x + 2, then x ← y × 2, then OUTPUT x. What is output?",
                 ["7", "10", "14", "12"], 2,
                 "y becomes 7, then x becomes 7 × 2 = 14.",
                 hint="Write the value of x and y after each line.",
                 feedback=["7 is the value of y, not of x.", "10 is 5 × 2. It uses the old value of x instead of y.", "",
                           "12 is 5 + 7. The last line multiplies, it does not add."]),
            H("Practice questions"),
            PQ('Which of these is correctly nested? A: <p>Welcome to <b>GBHS</b></p>. B: <p>Welcome to <b>GBHS</p></b>. '
               'C: <p>Welcome to <b>GBHS</b>. D: <b><p>Welcome to GBHS</b></p>.',
               "**A**. The tag opened last (b) is closed first, then p is closed. B and D overlap their tags. C never closes the p element."),
            PQ("A box has a content width of 120 px, padding of 15 px on each side and a border of 5 px on each side. "
               "What is the width of the box including its padding and border? A: 140 px. B: 160 px. C: 155 px. D: 120 px.",
               "**B**. 120 + 2 × 15 + 2 × 5 = 160 px. A counts one side of the padding and border only. C counts only the padding and one border. "
               "D is the content alone. Calculate; do not guess."),
            PQ("A student says: 'ANTIC prepares government policy on telecommunications.' Is the student correct? Explain.",
               "No. MINPOSTEL, the Ministry of Posts and Telecommunications, prepares and carries out government policy on posts, "
               "telecommunications and ICT. ANTIC, the National Agency for Information and Communication Technologies, promotes and "
               "regulates ICT activities and is in charge of the security of electronic communication networks and information systems."),
            PQ("Complete a truth table for Q = A AND (NOT B) with the inputs A, B in the order 00, 01, 10, 11.",
               "Row 00: A = 0, so Q = 0. Row 01: A = 0, so Q = 0. Row 10: A = 1 and NOT 0 = 1, so Q = 1. Row 11: NOT 1 = 0, so Q = 0. "
               "The outputs are 0, 0, 1, 0. Q is 1 only when A is 1 and B is 0."),
            SUM("Paper 1 is 1.5 hours of multiple choice on the whole syllabus. Check the current GCE Board instructions for the number of questions and the rules.",
                "Divide 90 minutes by the number of questions to get a time budget, and use two passes.",
                "Eliminate options you know are wrong; wrong options come from common mistakes.",
                "Test absolute words such as always and never with a counter-example.",
                "Trace pseudo-code and circuits on paper, writing down every value.",
                "Learn the traps in each topic: tags and attributes, class and id, copyright and licence, the two 2010 laws, and both sides of an impact answer."),
        ],
    ),
]
