"""Form 5 ICT (O Level 0596): Examination module (Paper 1 and Paper 2).

Draft content. The only exam facts stated here come from the syllabus outline in
apps/academics/gce_curriculum.py: Paper 1 is multiple choice, Paper 2 is structured theory and
Paper 3 is a practical lab. Durations, numbers of questions and weightings are NOT given there, so the
lessons send students to the current GCE Board instructions. Mock lengths and timings are KKEVO
practice settings.
"""

from .dsl import *  # noqa: F403

COURSE = ("ict", "form-5")

LESSONS = [
    # ------------------------------------------------------------------ Paper 1
    lesson(
        module="Examination", topic="Paper 1",
        title="Paper 1: multiple choice strategies for ICT",
        slug="ict-paper-1-multiple-choice-strategies",
        minutes=22,
        summary="How multiple choice works, how to share your time with a two-pass method, how to eliminate wrong options, "
                "and the traps that appear in web, licence, law, spreadsheet and database questions.",
        objectives=[
            "Describe Paper 1 and plan a time budget from any number of questions and minutes",
            "Use the two-pass method and eliminate options to improve your chance of a correct answer",
            "Spot absolute words and other traps in options",
            "Avoid the common traps in web, licence, law, spreadsheet and database questions",
        ],
        key_concepts=["Paper 1", "Multiple choice", "Two-pass method", "Elimination", "Distractor", "Absolute words"],
        blocks=[
            H("Introduction"),
            T("Paper 1 is the **multiple-choice** paper. Each question has one stem (the question) and several options. "
              "One option is correct. The others are called **distractors**: they look reasonable because each one is built "
              "from a real mistake."),
            T("In ICT the paper covers the whole course: web pages, CSS, copyright and licences, the law, the effects of ICT "
              "on society, spreadsheets, word processing and databases. You will not have a computer in front of you. "
              "You must know the ideas and the exact terms."),
            D("The syllabus outline says that **Paper 1 is multiple choice**, **Paper 2 is structured theory** and "
              "**Paper 3 is a practical lab** (word processing, spreadsheets, databases and basic web design).",
              title="What the guide says",
              note="The guide does not give the number of questions, the time or the weighting of each paper. "
                   "Check the current GCE Board instructions and your teacher's notes for those."),
            H("Plan your time"),
            T("Because the exact numbers can change, learn a method instead of a fixed number. Divide the minutes by "
              "the number of questions to get the **average time per question**."),
            EX("Worked example 1: a time budget", intro=(
                "In the KKEVO practice mock, Paper 1 has 40 questions in 60 minutes. (These are KKEVO practice settings, "
                "not official GCE figures.) Plan the time."), steps=[
                S("Average time", math=r"60 \div 40 = 1.5", text="You have 1.5 minutes (90 seconds) per question."),
                S("First pass", text="Aim for about 1 minute on each question. Answer what you know and mark the rest. "
                                     "40 questions at 1 minute is 40 minutes."),
                S("Time left", math=r"60 - 40 = 20", text="You have about 20 minutes for the marked questions and for checking."),
                S("Final minute", text="Make sure every question has an answer."),
            ]),
            KEY("The two-pass method",
                "Do not fight with one hard question while easy marks are waiting later in the paper.",
                cards=[["Pass 1", "Go through all the questions. Answer quickly if you know it. If not, mark it and move on."],
                       ["Pass 2", "Return to the marked questions. Eliminate options and choose the best one."],
                       ["Pass 3", "Use the last minutes to check that nothing is blank and that each answer is on the correct line."]]),
            TIP("A blank can never score. Unless your instructions say otherwise, put an answer for every question. "
                "Each option you remove makes a guess more likely to be right."),
            H("Eliminate options"),
            T("Read the stem first and think of the answer before you look at the options. Then read **all** the options, "
              "even if the first one looks right. Cross out the ones that are clearly wrong. Then compare the ones left."),
            EX("Worked example 2: eliminate", intro=(
                "Which of these is open-source software? A: a cracked copy of a paid word processor. B: LibreOffice. "
                "C: a program that is free to use but whose code is closed. D: a program you must pay for each year."), steps=[
                S("Think first", text="Open source means anyone may see, study, change and share the code, under conditions."),
                S("Remove A", text="A cracked copy is software piracy. It is not open source."),
                S("Remove C and D", text="C describes freeware (free, but closed code). D is proprietary software."),
                S("Choose", text="**B**. LibreOffice is open source."),
            ]),
            H("Absolute words and qualifiers"),
            T("Words such as **always, never, only, all, none, every** make a statement very strong. One exception makes "
              "the whole statement false, so options with these words are often distractors. Words such as "
              "**usually, may, can, some, often** are safer."),
            T("Do not reject an option only because it has an absolute word. Some true statements use them, for example "
              "**a formula in a spreadsheet must start with an equals sign**. Always test the statement against what you know."),
            EX("Worked example 3: absolute words", intro=(
                "Which statement about copyright is correct? A: Copyright exists only if the creator registers the work. "
                "B: Copyright exists automatically when a work is created. C: Everything on the internet is free to copy. "
                "D: Copyright applies only to books."), steps=[
                S("Mark the absolute words", text="A has only, C has everything, D has only."),
                S("Test A", text="Copyright exists automatically, so registering is not needed. A is false."),
                S("Test C and D", text="Photos, music and software are protected too, and most online content is protected. C and D are false."),
                S("Choose", text="**B**. It has no absolute word and it is the true statement."),
            ]),
            H("Traps by area"),
            KEY("Where the distractors hide",
                "Look for these swaps and half-truths.",
                cards=[["Web", "HTML is a markup language, not a programming language. A class is written with a full stop in CSS (.price) and an id with a hash sign (#logo). The href attribute is for links and src is for images. Inline CSS beats internal and external CSS when rules conflict."],
                       ["Licences", "Freeware is free to use but its code is closed. Open source lets you study and change the code. Shareware is a trial that you pay to keep. Copyright is automatic. Found on a search engine does not mean free to use."],
                       ["Laws", "Law No. 2010/012 is about cybersecurity and cybercrime. Law No. 2010/013 is about electronic communications. Both are dated 21 December 2010. ANTIC is the National Agency for Information and Communication Technologies. MINPOSTEL is the Ministry of Posts and Telecommunications. Examiners like to swap the two names."],
                       ["Spreadsheets", "A formula starts with an equals sign. COUNT counts cells that hold numbers only. SUM adds, AVERAGE gives the mean. A relative reference changes when copied, an absolute reference (dollar signs before the column and row) does not."],
                       ["Databases", "A primary key is unique in its own table. A foreign key holds the primary key of another table. WHERE filters records, ORDER BY sorts them, SELECT chooses fields. Phone numbers are stored as text."]]),
            T("Do not memorise this list as a block. Learn each idea in its lesson. Use the list at the end to check which area is "
              "your weak one."),
            H("Common mistakes"),
            MISTAKE("Choosing the first option that looks familiar",
                    "A distractor is built to look familiar. Read every option before you decide."),
            MISTAKE("Reading the stem too fast",
                    "Words such as NOT, EXCEPT, FIRST and BEST change the answer. Underline them in the question."),
            MISTAKE("Spending too long on one question",
                    "Every question is worth the same. Mark it, move on and come back in pass 2."),
            MISTAKE("Changing a correct answer without a reason",
                    "Change an answer only if you find a clear error in your first thinking, not because of a feeling."),
            QUIZ("A paper has 50 questions in 75 minutes. What is the average time per question?",
                 ["1 minute", "1.5 minutes", "2 minutes", "25 seconds"], 1,
                 "75 divided by 50 is 1.5 minutes, that is 90 seconds.",
                 hint="Divide the minutes by the number of questions.",
                 feedback=["That would use only 50 of the 75 minutes.", "",
                           "50 questions at 2 minutes would need 100 minutes.",
                           "That is far too fast and wastes most of the time."]),
            QUIZ("Which option is most likely a distractor?",
                 ["Copyright can protect a photo", "A CSS class is written with a full stop",
                  "Open-source software is never free to change", "A primary key identifies each record"], 2,
                 "The word never makes the statement very strong, and it is false: open-source software may be changed.",
                 hint="Look for an absolute word and then test the statement.",
                 feedback=["This is true: photos are protected.", "This is true: .price is a class selector.", "",
                           "This is true: a primary key is unique for each record."]),
            H("Practice questions"),
            PQ("A student has 45 questions to do in 60 minutes. (a) Find the average time per question. (b) How can the "
               "student use the two-pass method?",
               "(a) 60 divided by 45 is about 1.3 minutes, roughly 80 seconds. (b) In pass 1 answer the questions you know "
               "in about a minute each and mark the hard ones. In pass 2 return to the marked questions and eliminate options. "
               "In pass 3 check that every question has an answer."),
            PQ("Question: Which statement about ANTIC is correct? A: It is the Ministry of Posts and Telecommunications. "
               "B: It is the National Agency for Information and Communication Technologies. C: It is a mobile network. "
               "D: It is an antivirus program. Explain how you would find the answer.",
               "Answer B. Think first: ANTIC is the National Agency for Information and Communication Technologies. A is the "
               "name of MINPOSTEL, so it is the swapped distractor. C and D are invented. ANTIC is a public agency, not a company or a program."),
            PQ("Cells A1 to A5 hold 10, 20, the word absent, 30 and an empty cell. (a) What does COUNT of A1:A5 give? "
               "(b) What does SUM give? (c) What does AVERAGE give?",
               "(a) COUNT counts only cells with numbers: 10, 20 and 30, so 3. (b) SUM is 10 + 20 + 30 = 60. "
               "(c) AVERAGE uses the number cells only: 60 divided by 3 = 20. The text cell and the empty cell are ignored."),
            PQ("Which is the primary key of a table Students: Surname, Class, StudentID or Phone? Explain, and explain "
               "why one of the other options is wrong.",
               "StudentID. A primary key must have a different value for each record. Surname and Class can repeat, "
               "because two students can share a surname or a class. Phone numbers can be shared in a family and can change."),
            SUM("The guide says Paper 1 is multiple choice. Check the current GCE Board instructions for the number of questions and the time.",
                "Divide the minutes by the number of questions to get the average time per question.",
                "Use the two pass method: answer what you know, mark the rest, return, then check for blanks.",
                "Think of the answer first, then eliminate the options that are clearly wrong.",
                "Test options with absolute words, and watch for swapped terms: freeware and open source, ANTIC and MINPOSTEL, COUNT and SUM.",
                "Read the whole stem and every option, and look for words such as NOT and EXCEPT."),
        ],
    ),
    # ------------------------------------------------------------------ Paper 2
    lesson(
        module="Examination", topic="Paper 2",
        title="Paper 2: answering structured theory questions",
        slug="ict-paper-2-structured-theory-answers",
        minutes=24,
        summary="What command words such as state, describe, explain and compare ask for, how marks guide the number of points, "
                "and model answer plans for hardware and software, legal and social, spreadsheet and database questions.",
        objectives=[
            "Explain what the command words state, describe, explain, compare and give two ask you to do",
            "Use the marks as a guide to the number of points to write",
            "Plan answers on hardware and software, legal and social effects, spreadsheet logic and database design",
            "Check an answer against the question before moving on",
        ],
        key_concepts=["Paper 2", "Structured question", "Command word", "Marks as a guide", "Model answer plan"],
        blocks=[
            H("Introduction"),
            T("Paper 2 is **structured theory**. A structured question has a short story (the context) and then parts such as "
              "(a), (b) and (c). Each part asks for a short written answer, and the next part often builds on the previous one."),
            T("A good answer is not long. It is **accurate** and it **matches the question word**. This lesson shows you how."),
            D("The syllabus outline says that Paper 2 is structured theory. It does not give the number of questions, the time "
              "or the weighting.", title="What the guide says",
              note="Check the current GCE Board instructions and your teacher's notes for those details, "
                   "and for how the marks are shown on the paper."),
            H("Command words"),
            T("The first word of a question tells you what kind of answer to write. Many students lose marks because they "
              "write an explanation when the question only asked them to state."),
            KEY("Common command words",
                "Learn what each one asks for. Exact wording on the paper may differ, so read each question carefully.",
                cards=[["State, name, give", "A short answer, a word or a phrase. No explanation is needed."],
                       ["Define", "Give the exact meaning of a term, in a sentence."],
                       ["Describe", "Say what something is like, or what happens, step by step. Use facts, not reasons."],
                       ["Explain", "Give a point and a reason. Use the word because, or so that."],
                       ["Compare", "Write about both things. Use words such as whereas and but. Give similarities and differences."],
                       ["Suggest", "Use what you know on a situation you have not seen. There may be more than one good answer."],
                       ["Discuss", "Give both sides, for example an advantage and a disadvantage, and a short conclusion."]]),
            H("Marks tell you how much to write"),
            T("The number of marks in brackets is a good guide to the number of **separate points** you need. A question for "
              "2 marks usually needs two points. A question that says **give two** needs exactly two. If you write a third "
              "point the examiner may ignore it, so use your best two."),
            T("For an **explain** question, each mark is often one point plus its reason. For example, two marks for explaining "
              "one danger of piracy means one danger and one reason."),
            TIP("Write one point per line or per sentence. Do not repeat the same point in new words, because it will not "
                "earn a second mark. Use the words of the question and the correct technical term."),
            H("Model answer plans"),
            EX("Worked example 1: hardware and software", intro=(
                "A school in Bamenda buys a computer for its library. (a) State the difference between hardware and software. "
                "[2 marks] (b) Give two examples of hardware and one of software. [3 marks]"), steps=[
                S("Read the command words", text="(a) State means a short answer. (b) Give means examples only."),
                S("(a) Two points for two marks", text="Hardware is the physical parts of a computer that you can touch. "
                                                      "Software is the programs and instructions that tell the hardware what to do."),
                S("(b) Three items for three marks", text="Hardware: keyboard, monitor (also mouse, printer, hard disk). "
                                                         "Software: a web browser, a word processor or an operating system."),
                S("Check", text="Both parts are answered with the right number of points, and the answers are short."),
            ]),
            EX("Worked example 2: a legal and social question", intro=(
                "A cyber cafe in Buea uses copied programs. Explain two dangers to the business of using pirated software. [4 marks]"), steps=[
                S("Read the command word", text="Explain means point plus reason. Two dangers means two points, each with a reason."),
                S("Danger 1 (2 marks)", text="The programs may contain viruses or spyware. This can damage the computers or steal customers' data."),
                S("Danger 2 (2 marks)", text="Using pirated software is illegal, so the business can be punished and lose its reputation."),
                S("Check", text="Each danger has a reason after the word so or because. No example is repeated."),
            ]),
            EX("Worked example 3: compare", intro=(
                "Compare internal CSS and external CSS. [4 marks]"), steps=[
                S("Read the command word", text="Compare means write about both and show differences. Aim for two sentences with whereas."),
                S("Where each is written", text="Internal CSS is written in a style element in the head of one page, whereas external CSS is "
                                               "written in a separate file such as style.css."),
                S("How many pages", text="Internal CSS styles that one page only, whereas one external file can style every page that links to it."),
                S("Add the reason", text="So external CSS is better for a whole website, because a change is made once and applies to all pages."),
            ]),
            H("Spreadsheet and database questions"),
            T("These questions test whether you can think like the computer. Follow the rules exactly, one step at a time. "
              "Show your working because a method mark may be given even when the final value is wrong."),
            EX("Worked example 4: spreadsheet logic", intro=(
                "Cell B2 holds the mark 62. (a) State what =IF(B2>=50,\"Pass\",\"Fail\") shows. [1 mark] (b) The formula is copied "
                "down to B3. State how the reference changes. [1 mark] (c) Explain why a pass mark stored in one cell "
                "should use an absolute reference. [2 marks]"), steps=[
                S("(a) Test the condition", text="62 is greater than or equal to 50, so the condition is true and the cell shows Pass."),
                S("(b) Relative reference", text="B2 becomes B3. A relative reference moves to the same position in the new row."),
                S("(c) Absolute reference", text="An absolute reference (dollar signs before the column and row) does not change when copied. "
                                                "So every copy of the formula uses the same pass mark cell, and the pass mark can be changed in one place."),
            ]),
            CODE("""
B2: 62
C2: =IF(B2>=50,"Pass","Fail")      shows Pass
C3: =IF(B3>=50,"Pass","Fail")      after copying down (B2 became B3)

Pass mark kept in cell F1 (absolute reference):
C2: =IF(B2>=$F$1,"Pass","Fail")
C3: =IF(B3>=$F$1,"Pass","Fail")    ($F$1 does not change)
""", "text", title="Listing 1: copying a formula"),
            EX("Worked example 5: database design", intro=(
                "A clinic in Garoua stores patients and visits. Design a table Patients with five fields. State the data type of each "
                "field and the primary key. [6 marks]"), steps=[
                S("Choose the fields", text="PatientID, Surname, FirstName, DateOfBirth, Phone."),
                S("Choose the data types", text="PatientID: text. Surname: text. FirstName: text. DateOfBirth: date. "
                                               "Phone: text, because it is not used in calculations and may start with a zero or a plus sign."),
                S("Choose the primary key", text="PatientID, because each patient has a different value. Surname can repeat."),
                S("Link to the next table", text="A table Visits would hold PatientID as a foreign key, so one patient can have many visits."),
            ]),
            H("Common mistakes"),
            MISTAKE("Explaining when the question says state",
                    "A long explanation does not earn extra marks and costs time. Match the command word."),
            MISTAKE("Answering with an example only",
                    "A word such as LibreOffice names an example. A mark is usually for the idea, so say what open source means too."),
            MISTAKE("Repeating the same point",
                    "Saying piracy is illegal and then it is against the law is one point, not two."),
            MISTAKE("Answering in general when the question gives a context",
                    "If the question is about a cyber cafe, use the cyber cafe in your answer, not a general company."),
            QUIZ("A question says: Give two advantages of external CSS. [2 marks] Which answer is best?",
                 ["One advantage, fully explained in four sentences",
                  "Two short points: one change updates every page, and the design is the same on all pages",
                  "Three advantages in a list",
                  "A definition of CSS"], 1,
                 "Give two means two points. Each short point earns one mark.",
                 hint="Count the marks and the number the question asks for.",
                 feedback=["Only one point is given. A second mark needs a second point.", "",
                           "Only two are asked for. Extra points may be ignored and take time.",
                           "The question asked for advantages, not a definition."]),
            QUIZ("Which command word asks you to give a point and a reason?",
                 ["State", "Name", "Explain", "Give"], 2,
                 "Explain asks for a point and a reason, using because or so that.",
                 hint="Which word means say why?",
                 feedback=["State needs only a short answer.", "Name needs only the word or name.", "",
                           "Give needs only the items asked for."]),
            H("Practice questions"),
            PQ("Explain one effect of the digital divide on a village that has no network. [2 marks]",
               "Point: people in the village cannot use online services such as mobile money, online learning or online information. "
               "Reason: because they have no network or devices, so they miss opportunities that people in towns have."),
            PQ("A shop uses a spreadsheet. Cells C2 to C6 hold quantities. Write formulas to (a) add all the quantities and (b) show "
               "the largest quantity. [2 marks]",
               "(a) =SUM(C2:C6) (b) =MAX(C2:C6). Each formula starts with an equals sign and uses the range C2:C6."),
            PQ("State the difference between a primary key and a foreign key. [2 marks]",
               "A primary key is a field whose value is unique for every record in its own table. A foreign key is a field in one table "
               "that holds the primary key of another table, and it creates the link between the tables."),
            PQ("Name the agency and the ministry whose names are ANTIC and MINPOSTEL. State one thing that Law No. 2010/012 covers. [3 marks]",
               "ANTIC is the National Agency for Information and Communication Technologies. MINPOSTEL is the Ministry of Posts and "
               "Telecommunications. Law No. 2010/012 of 21 December 2010 covers cybersecurity and cybercrime."),
            SUM("Paper 2 is structured theory. Check the current GCE Board instructions for the details of timing and marks.",
                "Read the command word first: state is short, explain needs a reason, compare needs both sides.",
                "Use the marks as a guide to the number of separate points. Give two means two.",
                "Use the context in the question and the correct technical terms.",
                "For spreadsheets and databases, follow the rules step by step and show your working.",
                "Check the answer against the question and do not repeat points."),
        ],
    ),
]
