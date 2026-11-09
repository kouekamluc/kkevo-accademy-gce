"""Form 5 Office Practice (O Level 5090), modules 4-6 and the Examination module.

Draft content, written from KKEVO's master curriculum blueprint (it is not a Board syllabus booklet). Office Practice is
not in the Board's 2023 Ordinary Level report, so exam facts follow the blueprint only: Paper 1 is 50 multiple-choice
questions and Paper 2 is a written paper on a case study and administrative procedures; students must check the exact
paper format with their teacher. Names, firms and addresses in the examples are invented. Where textbooks differ
(filing conventions, quorum and proxy rules, letter styles) the lesson says "check your textbook". Filing orders were
verified by script.
"""

from .dsl import *  # noqa: F403

COURSE = ("office-practice", "form-5")

M4 = "Filing & Records Management"
M5 = "Reprography & Office Automation"
M6 = "Meetings & Business Correspondence"
M_EXAM = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ 1. A good filing system
    lesson(
        module=M4, topic="A good filing system",
        title="What makes a good filing system",
        slug="ofp2-good-filing-system",
        minutes=20,
        summary="Why offices file, the essentials of a good filing system, centralized and decentralized filing, and the equipment and tools that keep papers safe and easy to find.",
        objectives=[
            "Define filing and state why an office files its papers",
            "List the essentials of a good filing system",
            "Compare centralized and decentralized filing",
            "Describe common filing equipment and the use of an out-guide",
        ],
        key_concepts=["Filing", "Retrieval", "Centralized filing", "Decentralized filing", "Out-guide", "Guide card"],
        blocks=[
            H("Introduction"),
            T("A manager in a Douala company asks for last March's letter from a supplier. If the secretary finds it in one "
              "minute, the manager can decide at once. If the letter is lost, the company may pay twice or lose a customer. "
              "A good **filing system** is what makes the difference."),
            D("**Filing** is the process of putting documents in an agreed order and place so that they can be found quickly "
              "when they are needed. Finding a document again is called **retrieval**.", title="Filing"),
            H("Why do offices file?"),
            KEY("Purposes of filing",
                "Records are the memory of an organisation. Filing protects that memory.",
                cards=[["To find papers quickly", "Time is not wasted searching. Customers and managers are served faster."],
                       ["To keep evidence", "Letters, invoices and receipts prove what was agreed and what was paid. They may be needed in a dispute or an audit."],
                       ["To help decisions", "Managers use past records to plan, to compare and to avoid mistakes."],
                       ["To protect documents", "Papers kept in folders and cabinets are safe from loss, damage, theft and fire."],
                       ["To give continuity", "When a worker leaves, the next person can find the records and continue the work."]]),
            H("Essentials of a good filing system"),
            T("Not every system is good. An office should test its system against these essentials. Textbooks use slightly "
              "different lists, so check your textbook, but the ideas are the same."),
            KEY("Essentials of a good system",
                "A good system is simple, easy to reach, safe and cheap to run, and it can grow.",
                cards=[["Simple", "Staff understand it quickly and make few mistakes. A complicated system is used wrongly."],
                       ["Accessible and quick", "Files are near the people who use them and any paper can be found in a short time."],
                       ["Flexible and expandable", "New files and new drawers can be added without changing the whole system."],
                       ["Economical", "The cost of staff, space and equipment is small compared with the value of the records."],
                       ["Safe and confidential", "Protected against fire, damp, insects and theft. Private files are locked and only authorised staff may see them."],
                       ["Accurate and up to date", "Papers are filed promptly and in the right folder. Old papers are removed on time."],
                       ["Clearly labelled", "Cabinets, drawers and folders carry clear labels. Guide cards divide the folders."]]),
            MISTAKE("Piling papers 'to file later'",
                    "A heap of unfiled papers is the main reason documents are lost. File every day. Before filing, check that the paper "
                    "has been dealt with and carries a note such as 'for filing' or the initials of the person who handled it."),
            H("Centralized and decentralized filing"),
            T("A company with several departments must decide where its files are kept. There are two main choices."),
            IMG("f5ofp2-central-vs-decentral.svg",
                alt="Two diagrams. On the left, four departments send requests to one central file room. On the right, each of four departments has its own small file store.",
                caption="Figure 1. Centralized filing (left): one file room serves every department. Decentralized filing (right): each department keeps its own files."),
            D("In **centralized filing** the records of the whole organisation are kept in one place, such as a registry, under the "
              "control of specialist file clerks. In **decentralized filing** each department keeps its own files.",
              title="Two ways to organise files"),
            CODE("""CENTRALIZED FILING                     DECENTRALIZED FILING
+ One system for the whole firm        + Files are near the users: no delay
+ Trained file clerks, fewer errors    + Department knows its own papers best
+ Less duplication of papers           + Private papers stay in the department
+ Saves space and equipment            + A problem in one department does not
+ Easy to control and to protect         stop the others
- Delay while files are fetched        - Different systems in different places
- Departments may feel far from files  - Duplicate papers; wasted space
- Confidential papers are seen by      - Untrained staff; more mistakes
  more people                          - Hard to control from the top
- If the registry fails, all suffer""", "text", title="Advantages (+) and disadvantages (-)"),
            TIP("Many offices use a mixture: general records in a central registry and confidential or very busy files (for example "
                "the Human Resources files) in the department."),
            H("Filing equipment and tools"),
            KEY("Common equipment",
                "The choice depends on the size of the office, the number of papers and the money available.",
                cards=[["Vertical filing cabinet", "Drawers hold folders standing on edge, front to back. Common and cheap. Needs room in front to open the drawers."],
                       ["Lateral filing cabinet", "Folders are filed side to side on open shelves or pull-out drawers. Quick to see; needs wall space."],
                       ["Suspension files", "Folders hang from rails in a drawer, so they do not slump. Tabs on top carry labels."],
                       ["Box files, lever-arch files", "Hold loose papers or bound sets of papers on a shelf. Good for small offices and for documents that are still active."],
                       ["Guide cards", "Stiff cards with a tab that divide a drawer into sections (A, B, C... or months) and speed up searching."]]),
            D("An **out-guide** (also called a 'file out' card or requisition slip) is a card placed in the drawer in the place of a "
              "file that has been taken out. It shows the file name, who has it and the date. When the file returns, the out-guide is removed.",
              title="Out-guide"),
            EX("Worked example 1: choose a system",
               intro="A school has an Accounts office, a Records office and a Principal's office. The school wants quick access to student records and safe keeping of the principal's private letters. Suggest a filing arrangement.",
               steps=[
                   S("Identify the needs", text="Student records are used by many staff. The principal's letters are private."),
                   S("Choose for the general records", text="Use centralized filing in the Records office, with one clerk in charge, so every department uses one system."),
                   S("Choose for the private papers", text="Keep the principal's confidential letters in a locked cabinet in the principal's office (decentralized)."),
                   S("Add control", text="Use out-guides and a request book so that every file taken out can be traced."),
               ]),
            EX("Worked example 2: how many hours?",
               intro="A central registry (invented figures) receives 120 requests for files a day. Each request takes a clerk 3 minutes to fetch and return. How many working hours of clerk time are needed in a day?",
               steps=[
                   S("Total minutes", text="120 x 3 = 360 minutes."),
                   S("Change to hours", text="360 / 60 = 6 hours."),
                   S("Meaning", text="One clerk working a six-hour fetching day cannot also do the filing. The office needs more than one clerk or a faster system."),
               ]),
            EX("Worked example 3: using an out-guide",
               intro="The manager takes the file 'Fotso Printing Ltd' on 12 May. What must the clerk do?",
               steps=[
                   S("Before the file leaves", text="Write on a card: file name, name of the borrower, date (12 May)."),
                   S("Place the card", text="Put the out-guide in the drawer exactly where the file was."),
                   S("When the file comes back", text="Return the file to its place and remove the out-guide. If the file is overdue, the card tells the clerk whom to ask."),
               ]),
            QUIZ("Which is an advantage of centralized filing?",
                 ["All departments use one system run by trained clerks", "Files are always in the department that uses them", "No file ever needs to be fetched", "Confidential papers are seen by fewer people"], 0,
                 "One system and trained clerks reduce mistakes and duplication. The other statements describe decentralized filing or are untrue.",
                 hint="Think about who controls the files.",
                 feedback=["", "That is an advantage of decentralized filing.", "In a central registry users must ask for files, so files are fetched all the time.", "In a central registry more people can see the papers, not fewer."]),
            QUIZ("What is the purpose of an out-guide?",
                 ["To show where a file has gone while it is out of the drawer", "To divide the drawer into alphabet sections", "To hold papers still to be filed", "To lock a drawer"], 0,
                 "The out-guide takes the place of the missing file and records who has it and since when.",
                 hint="What do you put in a drawer when a file is taken out?",
                 feedback=["", "That is a guide card.", "Papers waiting to be filed go in a tray, not in the cabinet.", "An out-guide has no locking function."]),
            PQ("State four essentials of a good filing system.",
               "Any four of: simple; quick and accessible; flexible and expandable; economical; safe and confidential; accurate and up to date; clearly labelled."),
            PQ("Give two advantages and two disadvantages of decentralized filing.",
               "Advantages: files are near the users, so no delay; the department knows its own papers; private papers stay in the department. Disadvantages: different systems in different departments; duplicate papers and wasted space; untrained staff make more mistakes; hard to control. (Any two of each.)"),
            PQ("Explain what is meant by retrieval and why it is the main test of a filing system.",
               "Retrieval means finding a document again when it is needed. A system is judged by how quickly and correctly it allows retrieval, because the reason for filing is to be able to use the records later."),
            PQ("A clerk takes a file from the drawer and leaves nothing in its place. What problem may follow and what should have been used?",
               "Nobody will know who has the file or where it is, and other staff may waste time searching or file new papers in the wrong place. An out-guide should have been placed in the drawer."),
            TIP("Filing appears in Paper 1 (multiple choice on definitions, essentials and advantages) and in Paper 2 (for example, advising a firm "
                "on which system to use). Check the exact paper format with your teacher.", title="Exam link"),
            SUM("Filing is putting documents in order and place so that they can be retrieved quickly; the main reasons are speed, evidence, decisions, protection and continuity.",
                "A good system is simple, accessible, flexible, economical, safe, accurate and clearly labelled.",
                "Centralized filing uses one registry for the whole firm; decentralized filing leaves files in each department. Each has advantages and disadvantages, and many firms mix the two.",
                "Equipment includes vertical and lateral cabinets, suspension files, box files and guide cards. An out-guide marks the place of a file that is out."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Classification methods
    lesson(
        module=M4, topic="Classification methods",
        title="Classification methods: alphabetical, numerical, geographical and more",
        slug="ofp2-classification-methods",
        minutes=25,
        summary="The six common ways to arrange files (alphabetical, numerical, alpha-numeric, geographical, chronological, subject), when each suits an office, and how to put files in the correct order.",
        objectives=[
            "Name and describe the main classification methods",
            "Put names, numbers, places and dates in the correct filing order",
            "Choose a suitable method for a given office",
            "State one advantage and one disadvantage of each method",
        ],
        key_concepts=["Classification", "Alphabetical filing", "Numerical filing", "Alpha-numeric filing", "Geographical filing", "Chronological filing", "Subject filing"],
        blocks=[
            H("Introduction"),
            T("In a market, sellers of yams stand in one row and sellers of cloth in another. Customers know where to go. "
              "An office does the same with its papers. **Classification** means grouping and arranging files by a chosen "
              "rule, so that every paper has one clear place."),
            D("A **classification method** is the rule used to arrange files: by name (alphabetical), by number (numerical), by letter and number together "
              "(alpha-numeric), by place (geographical), by date (chronological) or by topic (subject).", title="Classification method"),
            IMG("f5ofp2-filing-methods.svg",
                alt="Six boxes showing the six classification methods with a small example for each: Mba before Mbah, 987 before 1015, A-3 before A-12, Centre before West, newest date first, and Insurance before Rent.",
                caption="Figure 1. Six classification methods with one example each."),
            H("Alphabetical filing"),
            T("Files are arranged in the order of the alphabet, usually by the **surname**, then the first name or initial. "
              "It is the most common method and the easiest to learn."),
            KEY("Basic rules (check your textbook for small differences)",
                "Textbooks differ on details such as titles and company names. Follow the rules of your own textbook and be consistent.",
                cards=[["Surname first", "File 'Mbah Aloys' as Mbah, Aloys. Compare surnames first, then first names or initials."],
                       ["Nothing before something", "A shorter name comes before a longer name that begins with the same letters: Mba before Mbah, and Mbah (no first name) before Mbah, Aloys."],
                       ["Ignore titles", "Mr, Mrs, Miss, Dr and similar titles are not used for the order. They are written after the name in brackets."],
                       ["Organisations", "File under the first word of the name as written (for example Bamenda Hardware under B). Most textbooks ignore 'The' at the start."]]),
            EX("Worked example 1: alphabetical order",
               intro="Arrange these customers for filing (names are invented): Ndi Stella; Mbah Clarisse; Mba Joseph; Nde Emmanuel; Mbarga Paul; Mbah Aloys; Ndi Stanley.",
               steps=[
                   S("Write each as surname, first name", text="Ndi, Stella; Mbah, Clarisse; Mba, Joseph; Nde, Emmanuel; Mbarga, Paul; Mbah, Aloys; Ndi, Stanley."),
                   S("Sort by surname", text="Mba, Mbah, Mbarga come before Nde, Ndi (M before N). Within M: Mba (shortest), Mbah, Mbarga. Nde comes before Ndi because e comes before i."),
                   S("Sort the two Mbah names by first name", text="Aloys before Clarisse. The two Ndi names: Stanley before Stella (a before e)."),
                   S("Final order", text="1 Mba, Joseph  2 Mbah, Aloys  3 Mbah, Clarisse  4 Mbarga, Paul  5 Nde, Emmanuel  6 Ndi, Stanley  7 Ndi, Stella"),
               ]),
            H("Numerical and alpha-numeric filing"),
            T("In **numerical filing** each file gets a number and files are arranged in **number order**, smallest first. Invoices, "
              "orders, patient files and customer accounts are often numbered. A separate alphabetical **index** is needed, "
              "because a clerk must look up a name to find its number. In **alpha-numeric filing** a letter and a number together form the code, for example A-3, B-12."),
            MISTAKE("Sorting numbers as if they were words",
                    "As words, '1015' comes before '987' because 1 comes before 9. As numbers, 987 is smaller than 1015, so 987 comes first. "
                    "File 987, 996, 1015, 1048, 1203, never 1015, 1048, 1203, 987, 996. In alpha-numeric codes, compare the letter first and then the number as a number: A-3, A-12, A-21, B-7."),
            EX("Worked example 2: numerical and alpha-numeric order",
               intro="Arrange the invoice numbers 1048, 987, 1203, 1015, 996 and then the codes B-12, A-3, B-7, A-21, A-12, C-4.",
               steps=[
                   S("Compare as numbers", text="987 < 996 < 1015 < 1048 < 1203."),
                   S("Codes: letters first", text="All the A codes, then the B codes, then C."),
                   S("Within a letter, compare numbers", text="A: 3, 12, 21. B: 7, 12. C: 4."),
                   S("Final order", text="A-3, A-12, A-21, B-7, B-12, C-4."),
               ]),
            H("Geographical filing"),
            T("Files are arranged by **place**: country, region, then town, then customer name. A sales office that covers many towns, or a "
              "post office sorting letters, finds it useful. A name index is needed to find a customer whose town is not known."),
            EX("Worked example 3: geographical order",
               intro="A company files customers by region (alphabetical), then town (alphabetical), then name. The customers (invented) are: Ako Stores, Buea, South-West; Fon Traders, Bamenda, North-West; Ndifor Ltd, Kumba, South-West; Essomba and Sons, Yaounde, Centre; Tchoumi Foods, Bafoussam, West; Mbarga Pharmacy, Douala, Littoral; Njoh Supplies, Limbe, South-West.",
               steps=[
                   S("Sort the regions", text="Centre, Littoral, North-West, South-West, West (C, L, N, S, W)."),
                   S("Within South-West sort the towns", text="Buea, Kumba, Limbe."),
                   S("Write the final order", text="Centre: Essomba and Sons.  Littoral: Mbarga Pharmacy.  North-West: Fon Traders.  South-West: Ako Stores (Buea), Ndifor Ltd (Kumba), Njoh Supplies (Limbe).  West: Tchoumi Foods."),
               ]),
            H("Chronological and subject filing"),
            T("**Chronological filing** arranges papers by **date**. Inside a folder the most recent paper is usually placed at the front, so that "
              "the latest news is seen first (check your textbook, as a few books place the newest at the back). It suits records of daily work, "
              "and a 'tickler' or bring-forward file reminds the office of dates when action is due. **Subject filing** groups papers by "
              "topic, such as Insurance, Rent, Advertising. It suits records about activities, but it needs clear headings, because a letter can fit two subjects; cross-references solve that."),
            EX("Worked example 4: chronological order",
               intro="Place these letters in a folder, newest first: 2 March 2026, 14 March 2026, 2 November 2025, 30 January 2026, 19 December 2025.",
               steps=[
                   S("Compare years", text="2026 dates come before 2025 dates when the newest is first."),
                   S("Order within 2026", text="14 March, 2 March, 30 January."),
                   S("Order within 2025", text="19 December, 2 November."),
                   S("Final order", text="14 March 2026, 2 March 2026, 30 January 2026, 19 December 2025, 2 November 2025."),
               ]),
            KEY("Choosing a method",
                "Match the method to the way people ask for the papers.",
                cards=[["Alphabetical", "Pro: simple, direct. Con: names are spelled in many ways; no privacy."],
                       ["Numerical", "Pro: easy to expand, more confidential. Con: needs an index; two steps to find a file."],
                       ["Alpha-numeric", "Pro: groups related numbered files under a letter. Con: codes must be learned."],
                       ["Geographical", "Pro: grouping by area helps sales and delivery. Con: needs an index; clerks must know the places."],
                       ["Chronological", "Pro: shows the latest first; good for follow-up. Con: hard to find an item if the date is unknown."],
                       ["Subject", "Pro: all papers on a topic together. Con: headings may overlap; needs an index."]]),
            QUIZ("A hospital wants patient files to be hard for visitors to read and easy to expand. Which method fits best?",
                 ["Numerical, with a separate name index", "Alphabetical by surname", "Chronological", "Subject"], 0,
                 "Numbers on the folders tell visitors nothing about the patient, and new numbers are simply added at the end. The index (kept safely) links names to numbers.",
                 hint="Which method puts a name on the folder?",
                 feedback=["", "Names on the folders are easy for anyone to read.", "Chronological filing is not designed for patient records.", "Subject headings do not suit individual patient files."]),
            QUIZ("Which is the correct order of these file numbers: 502, 95, 1010?",
                 ["95, 502, 1010", "1010, 502, 95", "502, 95, 1010", "95, 1010, 502"], 0,
                 "Numbers are compared as numbers: 95 < 502 < 1010.",
                 hint="Compare the sizes of the numbers, not the first digit.",
                 feedback=["", "This is descending order; filing uses ascending order.", "502 is not smaller than 95.", "1010 is greater than 502."]),
            PQ("Arrange for alphabetical filing: Tabi Grace; Tabe Joseph; Ngu Peter; Fon Rita; Tabi Agnes; Ako Samuel; Ngu Paul.",
               "Ako, Samuel; Fon, Rita; Ngu, Paul; Ngu, Peter; Tabe, Joseph; Tabi, Agnes; Tabi, Grace."),
            PQ("Give one advantage and one disadvantage of numerical filing.",
               "Advantage: it is easy to expand (new numbers are added at the end) and it is more confidential because the folder shows only a number. Disadvantage: a clerk must first look up the number in an alphabetical index, so finding a file takes two steps."),
            PQ("A company files its letters by date, newest first. Place these in order: 5 July 2026, 28 June 2026, 11 July 2026.",
               "11 July 2026, 5 July 2026, 28 June 2026."),
            PQ("Why may a subject filing system need cross-references?",
               "A letter may deal with two subjects, for example insurance for a rented building. It can be filed under only one heading, so a cross-reference under the other heading tells the clerk where it is."),
            TIP("Ordering names, numbers, places and dates is a favourite practical question, in Paper 1 (multiple choice) and in Paper 2. "
                "Work slowly, write each item in filing form and tick it off. Check your textbook for its rules on titles and company names.", title="Exam link"),
            SUM("Classification arranges files by one clear rule. The common methods are alphabetical, numerical, alpha-numeric, geographical, chronological and subject.",
                "In alphabetical filing, use the surname then first name, and 'nothing before something'. Numbers are compared as numbers, not as words.",
                "Geographical filing sorts by region, then town, then name. Chronological filing usually puts the newest paper in front.",
                "Choose the method by how people ask for the papers. Numerical, geographical and subject systems need an index."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Indexing and cross-referencing
    lesson(
        module=M4, topic="Indexing and cross-referencing",
        title="Indexing and cross-referencing",
        slug="ofp2-indexing-cross-referencing",
        minutes=20,
        summary="How an index guides the clerk to a file, the main types of index, and how cross-references find a paper that could be filed in two places.",
        objectives=[
            "Define an index and explain why some filing systems need one",
            "Describe card, book, visible and computer indexes",
            "Define cross-referencing and say when it is needed",
            "Write a cross-reference sheet or card for a given case",
        ],
        key_concepts=["Index", "Card index", "Visible index", "Cross-reference", "Cross-reference sheet", "Retrieval"],
        blocks=[
            H("Introduction"),
            T("At the back of your textbook there is an index. You look up 'Minutes' and it tells you the page. "
              "An office index works in the same way: it tells the clerk where a file is. Without it, a numerical system "
              "cannot be used, because nobody remembers which customer has which number."),
            D("An **index** is a list, arranged in a convenient order, that tells the user where a file or record is kept. "
              "**Indexing** is the preparing and keeping up to date of that list.", title="Index"),
            D("**Cross-referencing** means placing a note in one place that tells the reader where a paper, or more information, is kept in another place.",
              title="Cross-reference"),
            H("Types of index"),
            KEY("Common indexes",
                "Each index entry gives the name (or subject), the file number or place, and sometimes the date or the type of record.",
                cards=[["Card index", "One card for each name, kept upright in a drawer in alphabetical order. New cards are easy to insert. Very common."],
                       ["Book index", "Entries written in a bound book with alphabet tabs. Cheap and not easily lost, but it is hard to insert new names in order."],
                       ["Visible (strip) index", "Cards or strips overlap in a frame so the first line of each can be seen without lifting. Quick to scan; used for frequently used lists."],
                       ["Computer index", "A database or spreadsheet. Entries are found by searching for any part of a name or number, and sorted in a second. Needs a backup."]]),
            CODE("""INDEX CARD (numerical filing)
-------------------------------------------
Name:     Mbah, Aloys
File no.: 1048
Address:  P.O. Box 12, Bamenda   (invented)
Opened:   03/02/2026
See also: 1203 (Mbah Trading Co.)
-------------------------------------------""", "text", title="A card index entry (invented)"),
            T("A clerk who is asked for 'Mbah Aloys' finds the card, reads 1048, and goes to the numerical file. If the file is out, the "
              "card index can also show who has it. An index must be **accurate**, **up to date** and **kept separate** from the files "
              "(so that the index is not lost with the files in a fire or theft)."),
            MISTAKE("Never updating the index",
                    "An index that is not updated sends the clerk to the wrong place. Add a card whenever a new file is opened. "
                    "Mark or remove the card when a file is closed, moved or destroyed."),
            H("Why we cross-reference"),
            T("A document is physically in only one place. Yet someone may look for it under several headings. Cross-references "
              "solve this. Typical cases:"),
            KEY("When a cross-reference is needed",
                "Look for any case where the person asking might use a different name.",
                cards=[["Name changed", "A woman changes her surname after marriage, or a firm changes its name. File under the new name and refer from the old one."],
                       ["Two names for one thing", "Firm known by its short name and its full name; person known by two spellings."],
                       ["Two subjects in one paper", "A letter about insurance for a rented building could go under Insurance or under Rent."],
                       ["Linked firms or people", "A parent company and its subsidiary, or two partners."]]),
            T("There are two main forms. A **cross-reference sheet** is a sheet of coloured paper placed in the folder (or the place) "
              "where someone might look, showing where the paper really is. A **cross-reference card** is the same note on an index card. "
              "Some offices make a photocopy of the paper and put it in the second place."),
            CODE("""CROSS-REFERENCE SHEET
------------------------------------------------
File under:   FOTSO PRINTING LTD
Also known as: FP LTD
Papers on this subject are filed under:
  FOTSO PRINTING LTD  (file no. 2217)
Date:  14/05/2026        Initials: M.E.
------------------------------------------------""", "text", title="Cross-reference sheet in the 'FP Ltd' position (names invented)"),
            EX("Worked example 1: a firm changes its name",
               intro="Bamenda Hardware (invented) is renamed 'Nkwen Building Supplies' (invented). Alphabetical files are used. What should the clerk do?",
               steps=[
                   S("Choose the filing name", text="File new papers under the new name, Nkwen Building Supplies (N). Move the old papers into that folder if the firm agrees."),
                   S("Make the cross-reference", text="In the B section make a sheet: 'Bamenda Hardware - see Nkwen Building Supplies'."),
                   S("Update the index", text="Add a card for the new name and mark the old card with the new name."),
               ]),
            EX("Worked example 2: a letter on two subjects",
               intro="A letter from the landlord about a fire insurance clause in the rent contract arrives. The firm uses subject filing with headings 'Insurance' and 'Rent'.",
               steps=[
                   S("Decide the main subject", text="The main purpose of the letter is the rent contract. File the letter under Rent."),
                   S("Cross-reference", text="Place a sheet in the Insurance folder: 'Fire insurance clause - see Rent, letter of 6 May 2026'."),
                   S("Result", text="A clerk looking in either folder finds the letter or the note that leads to it."),
               ]),
            EX("Worked example 3: how many drawers?",
               intro="A firm (invented figures) has 4 500 customers and keeps one index card for each. One drawer holds 900 cards. How many drawers are needed?",
               steps=[
                   S("Divide", text="4 500 / 900 = 5."),
                   S("Add room to grow", text="Exactly 5 drawers would be full at once. The firm should buy a sixth, or choose a computer index, so that new cards can be added."),
               ]),
            KEY("Alphabetical files need an index too?",
                "Not always. Direct systems (alphabetical, where the user asks by name) can be searched without an index. Indirect systems (numerical, geographical, subject) need an index, because the user's request is not the same as the file's order.",
                cards=[["Direct", "Alphabetical: the request and the arrangement are the same (a name)."],
                       ["Indirect", "Numerical, alpha-numeric, geographical and subject systems: look up the index first."]]),
            QUIZ("A clerk places a coloured sheet in the 'Rent' folder saying 'Fire insurance clause - see Insurance'. The sheet is a",
                 ["cross-reference sheet", "guide card", "out-guide", "visible index"], 0,
                 "The sheet points from one place to another where the paper is actually filed.",
                 hint="The sheet does not hold the paper; it points to it.",
                 feedback=["", "A guide card divides sections of a drawer.", "An out-guide marks a removed file.", "A visible index is a list of cards in a frame."]),
            QUIZ("Why should an index be kept separate from the files it refers to?",
                 ["So that if the files are lost or destroyed the index still exists", "To make the system more complicated", "Because files cannot be near any list", "To save paper"], 0,
                 "Keeping the index apart means one disaster (fire, theft) does not take both the files and the key to them.",
                 hint="Think of safety.",
                 feedback=["", "Complication is a fault, not a goal.", "There is no such rule.", "Separation does not save paper."]),
            PQ("Define an index and name two types.",
               "An index is a list that tells the user where a file or record is kept. Types: card index, book index, visible index, computer index (any two)."),
            PQ("Why is an index necessary in numerical filing?",
               "People ask for papers by name, but the files are arranged by number. The index shows the number that belongs to a name, so the clerk can go to the right file."),
            PQ("Mrs Ngu (invented) marries and becomes Mrs Tabi. Papers are filed alphabetically. Explain how the office should handle this.",
               "File new papers under the new surname Tabi (and combine the old papers there). Put a cross-reference under Ngu saying 'Ngu - see Tabi' and update the index card."),
            PQ("List two qualities of a good index.",
               "It should be accurate, up to date, easy to use (clearly arranged), and kept separate from the files."),
            TIP("Cross-reference and index questions appear in Paper 1 as short definitions or choices and in Paper 2 as 'what should the clerk do?' "
                "cases. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("An index tells the user where a file is; it is required whenever the order of the files is not the order of the request.",
                "Types: card, book, visible and computer indexes. Keep the index accurate, up to date and separate from the files.",
                "A cross-reference is a note that leads from one place to where the paper really is. Use it for changed names, two names, and papers on two subjects.",
                "Cross-reference sheets are placed in the files; cross-reference cards go in the index."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Retention and archiving
    lesson(
        module=M4, topic="Retention and archiving",
        title="Retention, archiving and microfilming",
        slug="ofp2-retention-archiving",
        minutes=20,
        summary="How long records are kept, the life cycle from active file to archive or destruction, microfilming, safe disposal, and a retention schedule.",
        objectives=[
            "Explain retention, transfer, archiving and disposal",
            "Describe the life cycle of a record",
            "State the advantages and disadvantages of microfilm and microfiche",
            "Use a retention schedule to find when a record may be destroyed",
        ],
        key_concepts=["Retention period", "Active record", "Archive", "Microfilm", "Microfiche", "Disposal", "Retention schedule"],
        blocks=[
            H("Introduction"),
            T("An office that keeps every paper for ever soon has no room. An office that destroys papers too early may "
              "be unable to prove a payment or answer a tax enquiry. The skill is to keep each record **for the right time**, "
              "then move it or destroy it safely."),
            D("A **retention period** is the length of time a record must be kept. **Archiving** is the long-term storage of "
              "records that are no longer in daily use but must be kept because of their value. **Disposal** is the safe destruction "
              "or transfer of records at the end of their retention period.", title="Retention, archiving, disposal"),
            H("What decides how long to keep a record?"),
            KEY("Factors",
                "Retention is decided by rules and by common sense.",
                cards=[["Law", "Some records must be kept for a minimum time, for example tax, payroll and company records. The periods differ from country to country and change: check the current rules in Cameroon."],
                       ["Business need", "A guarantee, a contract or a loan must be kept for as long as it is in force."],
                       ["Value as history", "Minutes of a company, founding documents and photographs may be kept permanently."],
                       ["Cost and space", "Keeping records costs shelf space, staff time and money, so records with no value should go."]]),
            H("The life cycle of a record"),
            IMG("f5ofp2-record-lifecycle.svg",
                alt="A flow chart: create or receive, active use in the office, semi-active storage in a records store, then either permanent archive or destruction.",
                caption="Figure 1. The life cycle of a record."),
            KEY("The stages",
                "Every record moves along the same road.",
                cards=[["Active", "Used often. Kept near the staff who need it."],
                       ["Semi-active", "Used rarely, but not yet safe to destroy. Moved to a cheaper store (a records room or box store) at the end of its active period. The move is called transfer."],
                       ["Archive", "Records of lasting value are kept for a very long time or permanently, in a safe place with controlled access."],
                       ["Disposal", "Records past their retention period are destroyed in a safe way, or sent to an archive."]]),
            T("Important records that cannot be replaced, such as title deeds, the company's founding documents, and the main accounting records, "
              "are called **vital records**. They need extra protection: a fireproof cabinet or safe, and a copy kept in another building."),
            H("Microfilm and microfiche"),
            D("**Microfilming** photographs documents at a very small size onto film. **Microfilm** is a roll of film; **microfiche** is "
              "a flat sheet of film holding many small pictures (frames). A **reader** enlarges the picture on a screen, and a reader-printer can print it.",
              title="Microfilm"),
            CODE("""MICROFILM: ADVANTAGES (+) AND DISADVANTAGES (-)
+ Saves a great deal of storage space
+ Records are protected from damp, insects and fire if copies are stored apart
+ Copies are cheap and easy to send
+ Long life when stored properly
- Equipment (camera and reader) is costly
- Reading needs a reader; you cannot read the film by hand
- Cannot be changed or updated; new papers need new film
- Poor originals give poor pictures""", "text", title="Microfilm summary"),
            TIP("Many offices today scan documents and keep them electronically (see the lesson on electronic document management). "
                "The reasons are the same as for microfilm: save space and protect the records.", title="Compare"),
            H("Safe disposal"),
            T("Papers with names, bank details or business secrets must not be thrown in a bin. They are shredded, burned or "
              "pulped. Many offices keep a **destruction record**: a list of what was destroyed, when, by whom, and under whose authority, so "
              "that nobody can later say the papers disappeared by accident."),
            MISTAKE("Throwing confidential papers in the bin",
                    "Confidential papers, such as staff salaries, can be read by anyone who finds them. Use a shredder or another safe method, and record the destruction."),
            H("A retention schedule"),
            T("A **retention schedule** is a list that tells staff how long each type of record is kept and what happens afterwards. "
              "The periods below are **invented for practice**; real periods depend on the law and on company policy."),
            CODE("""RETENTION SCHEDULE (periods INVENTED for practice)
Record                  Keep (years)   Then
----------------------  ------------   -----------------
Customer invoices             6        Destroy (shred)
Cash books and ledgers       10        Archive
Staff attendance sheets       2        Destroy (shred)
Contracts (after end)         7        Destroy (shred)
Minute books              Permanent    Archive""", "text", title="Retention schedule"),
            EX("Worked example 1: when can a record go?",
               intro="Using the schedule above, the office holds invoices dated 2021 and staff attendance sheets dated 2024. In which year may each be destroyed?",
               steps=[
                   S("Add the retention period to the year", text="Invoices: 2021 + 6 = 2027. Attendance sheets: 2024 + 2 = 2026."),
                   S("Check the action", text="Both are marked 'destroy (shred)'. Shred them in that year, after the last day of the retention period, and write them in the destruction record."),
                   S("Keep the minute books", text="Minute books are permanent, so they are never destroyed. At the end of their active life they go to the archive."),
               ]),
            EX("Worked example 2: decide the action",
               intro="A clerk finds a 2018 cash book (invented). What should be done under the schedule above?",
               steps=[
                   S("Find the rule", text="Cash books: keep 10 years, then archive."),
                   S("Calculate", text="2018 + 10 = 2028, so the cash book must be kept at least until 2028."),
                   S("Action now", text="It is no longer in daily use, so transfer it to the records store (semi-active). In 2028 it moves to the archive."),
               ]),
            QUIZ("Which of these is a vital record?",
                 ["The land title deed of the company", "Last month's lunch menu", "A routine reminder note", "A used calendar"], 0,
                 "A vital record cannot be replaced and the firm cannot work without it. A title deed proves ownership of property.",
                 hint="Which one could the company not do without?",
                 feedback=["", "A menu has no lasting value.", "A reminder has no lasting value.", "A calendar has no lasting value."]),
            QUIZ("Which is a disadvantage of microfilm?",
                 ["A reader is needed to see the pictures", "It takes a great deal of space", "It cannot be copied", "It is easily destroyed by a small amount of damp whatever the care"], 0,
                 "The film cannot be read by eye; the office needs a reader (and a reader-printer to print).",
                 hint="What do you need before you can read the film?",
                 feedback=["", "Microfilm saves space.", "Copies of microfilm are cheap.", "Properly stored film resists damp."]),
            PQ("Distinguish between retention and archiving.",
               "Retention is how long a record must be kept. Archiving is the long-term storage of records that are no longer in daily use but have lasting value, in a secure place."),
            PQ("State two advantages and one disadvantage of microfilming.",
               "Advantages: it saves a great deal of space; the records are protected and can be copied cheaply. Disadvantage: equipment is costly and a reader is needed (also: records cannot be updated)."),
            PQ("A firm keeps its invoices for 6 years. An invoice is dated 2022. In what year does the retention period end?",
               "2022 + 6 = 2028."),
            PQ("Why should a firm keep a destruction record?",
               "It shows what was destroyed, when and on whose authority. It proves that the papers were destroyed in the normal course of business and not lost or hidden."),
            TIP("Retention and microfilm are standard Paper 1 topics (definitions, advantages and disadvantages). In a Paper 2 case study you may be "
                "asked what to do with old records. Use general rules and say that the exact periods are decided by the law and company policy.", title="Exam link"),
            SUM("A retention period is how long a record must be kept; it depends on the law, business need, historical value and cost.",
                "Records move from active to semi-active (transfer), then to the archive or to safe disposal. Vital records need extra protection.",
                "Microfilm and microfiche save space and protect records but need a reader and cannot be updated.",
                "A retention schedule lists how long each record is kept. Shred confidential papers and keep a destruction record."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Electronic document management
    lesson(
        module=M4, topic="Electronic document management",
        title="Electronic document management",
        slug="ofp2-electronic-document-management",
        minutes=20,
        summary="How an office scans, names, stores, protects and backs up electronic documents, and the advantages and risks compared with paper files.",
        objectives=[
            "Explain what an electronic document management system does",
            "Describe scanning, naming and folder structure for electronic files",
            "Explain backup, access control and security of electronic records",
            "Compare electronic and paper filing",
        ],
        key_concepts=["Electronic document management", "Scanning", "File naming", "Backup", "Access rights", "Metadata", "Cloud storage"],
        blocks=[
            H("Introduction"),
            T("A secretary in Yaounde scans a signed contract with her phone and saves it in a folder on the company's shared drive. "
              "Ten minutes later, a manager in Douala opens it. No cabinet, no courier. This is **electronic document management**."),
            D("**Electronic document management (EDM)** is the capturing, naming, storing, finding, sharing and protecting of documents "
              "in electronic form. A software tool that does this is called a **document management system (DMS)**.", title="Electronic document management"),
            H("Where do electronic documents come from?"),
            KEY("Two sources",
                "Documents enter the system in two ways.",
                cards=[["Born digital", "Created on a computer: letters, spreadsheets, emails, reports."],
                       ["Scanned", "Paper documents are scanned into images (PDF or JPEG). Software called OCR (optical character recognition) can read the text in the image so that it can be searched."]]),
            H("Naming and arranging electronic files"),
            T("An electronic cabinet needs the same discipline as a paper cabinet. A folder called 'New folder (2)' is the electronic "
              "version of a heap of papers. Offices agree a **naming convention** and a **folder structure**."),
            CODE("""FOLDER STRUCTURE (invented example)
Company
  Finance
    2026
      Invoices
      Receipts
  Human Resources
    Contracts
    Leave
  Customers
    Mbah_Aloys

FILE NAME PATTERN:  date_type_name_version
2026-05-14_Invoice_FotsoPrinting_v2.pdf
2026-05-14_Letter_Mbah_v1.docx""", "text", title="A folder structure and a naming pattern"),
            KEY("Good naming habits",
                "Names are the electronic 'labels'. A clear name makes retrieval fast.",
                cards=[["Use a pattern", "Put the date first in the form year-month-day, so that files sort in date order."],
                       ["Be short but clear", "Name the type and the person or firm. Avoid names like 'final', 'final2', 'finalfinal'."],
                       ["No special characters", "Avoid slashes and symbols that some systems reject."],
                       ["Show the version", "v1, v2... shows which draft is current."]]),
            D("**Metadata** is data about a document: its author, date, type, size and keywords. A DMS uses metadata to find documents by searching.",
              title="Metadata"),
            H("Protecting electronic records"),
            KEY("Four protections",
                "Electronic records are not safe just because they are electronic.",
                cards=[["Backup", "A copy made regularly on another device or place (external drive or cloud). A common rule of thumb is 3-2-1: three copies, on two kinds of media, one stored away from the office."],
                       ["Access rights", "Users have passwords and may open, edit or only read according to their job. Confidential folders are limited to a few people."],
                       ["Security software", "Anti-virus and updates protect against malware and loss. Staff must not open suspicious email attachments."],
                       ["Audit trail", "The system records who opened, changed or deleted a file and when."]]),
            MISTAKE("Thinking that a computer file cannot be lost",
                    "Files are lost when a disk fails, a laptop is stolen, a virus attacks or someone deletes by mistake. Without a backup, a single failure can erase years of records. Back up regularly and test that you can restore."),
            T("In places with weak connectivity or electricity cuts, an office needs a plan: save work locally and sync later, use a "
              "surge protector or a UPS (a battery that keeps the computer running for a short time), and keep an offline backup."),
            H("Electronic or paper?"),
            CODE("""ELECTRONIC FILING compared with PAPER FILING
                        Electronic                 Paper
Space                   very little                cabinets and rooms
Finding a document      search in seconds          walk and search
Sharing                 send to many at once       copy or courier
Backup                  easy copies                hard to copy all
Security                passwords, audit trail     locks; can be stolen
Main risks              virus, power cut,          fire, damp, loss,
                        no backup, hacking         theft
Cost                    equipment and software     cabinets and space
Legal use               check the current rules on electronic records""", "text", title="Comparison"),
            TIP("Many offices keep both: paper for signed originals that the law requires, and a scanned copy for daily use. "
                "Check the current rules on which documents must be kept in paper form."),
            EX("Worked example 1: rename the file",
               intro="A clerk saved a scanned invoice as 'scan0023 final.pdf'. The invoice is from Fotso Printing, dated 14 May 2026. Rename it by the pattern date_type_name_version.",
               steps=[
                   S("Date first", text="2026-05-14"),
                   S("Type and name", text="Invoice_FotsoPrinting"),
                   S("Version and extension", text="v1.pdf"),
                   S("Final name", text="2026-05-14_Invoice_FotsoPrinting_v1.pdf"),
               ]),
            EX("Worked example 2: a backup plan",
               intro="A small office has one computer holding all its accounts. Suggest a backup plan.",
               steps=[
                   S("Make a second copy", text="Copy the folder to an external drive every evening."),
                   S("Make a third copy off site", text="Once a week copy to cloud storage or take a drive home (keep it safe)."),
                   S("Test the copy", text="Once a month open a file from the backup to check that it works."),
                   S("Protect access", text="Password the computer and limit who can open the accounts folder."),
               ]),
            EX("Worked example 3: how many pages?",
               intro="A firm scans 40 pages a day for 20 working days (invented figures). Each scanned page is about 0.5 MB. How many megabytes (MB) of storage are used in the 20 days?",
               steps=[
                   S("Pages", text="40 x 20 = 800 pages."),
                   S("Storage", text="800 x 0.5 = 400 MB."),
                   S("Meaning", text="400 MB is small for modern devices, but backups must be made too: three copies need about 1 200 MB."),
               ]),
            QUIZ("Which rule helps a folder of files sort in date order?",
                 ["Start the file name with the date as year-month-day", "Start the file name with the word 'final'", "Use long sentences as names", "Use no dates at all"], 0,
                 "2026-05-14 sorts correctly because the year comes first, then the month, then the day.",
                 hint="Which part of a date must come first to sort correctly?",
                 feedback=["", "'final' sorts every file under F.", "Long names are hard to read.", "Without dates the sort order is by name only."]),
            QUIZ("A computer holding all the firm's records is stolen. Which one thing would have reduced the loss most?",
                 ["A recent backup stored away from the office", "A larger screen", "A faster printer", "A longer file name"], 0,
                 "A backup kept in another place can be restored. The other items do not protect the data.",
                 hint="What lets you restore the records after a theft?",
                 feedback=["", "Screen size does not protect data.", "Printer speed does not protect data.", "Names do not protect data."]),
            PQ("State three advantages of electronic document management over paper filing.",
               "Saves space; documents are found quickly by searching; documents can be shared at once with many people; easy to copy and back up; access can be controlled and recorded (any three)."),
            PQ("What is a backup and why is one copy on the same computer not enough?",
               "A backup is a copy of files kept so that they can be restored after loss. A copy on the same computer is lost together with the original if the computer fails or is stolen, so one copy must be stored on another device or in another place."),
            PQ("Name two ways to control who can see electronic records.",
               "Passwords for each user and different access rights (read only, edit); locking confidential folders; keeping an audit trail. (Any two.)"),
            PQ("Write a good file name for a letter to Mbah dated 3 June 2026, first version, using the pattern date_type_name_version.docx.",
               "2026-06-03_Letter_Mbah_v1.docx"),
            TIP("Electronic records are in the blueprint for Paper 1 and may appear in Paper 2 case studies, for example advising an office that wants to move from paper to computer. Mention backup and security.", title="Exam link"),
            SUM("Electronic document management captures, names, stores, finds, shares and protects documents in digital form.",
                "Use a folder structure and a naming pattern (date first, clear name, version). Metadata and OCR help searching.",
                "Protect records with backup (3-2-1), passwords and access rights, security software and an audit trail.",
                "Electronic filing saves space and speeds retrieval but has its own risks: virus, power cut and loss without backup."),
        ],
    ),
    # ------------------------------------------------------------------ 6. Copying and duplicating methods
    lesson(
        module=M5, topic="Copying and duplicating methods",
        title="Copying and duplicating methods",
        slug="ofp2-copying-duplicating-methods",
        minutes=22,
        summary="The difference between copying and duplicating, how photocopying, spirit and stencil duplicating and offset lithography work, and how to choose by number of copies and cost.",
        objectives=[
            "Distinguish copying from duplicating",
            "Describe photocopying, spirit duplicating, stencil duplicating and offset lithography",
            "Compare the methods by quality, number of copies and cost",
            "Choose the best method for a given job",
        ],
        key_concepts=["Reprography", "Photocopying", "Spirit duplicating", "Stencil duplicating", "Offset lithography", "Master copy", "Running cost"],
        blocks=[
            H("Introduction"),
            T("A school secretary in Bafoussam needs three copies of a letter for the principal's file. Next week she needs 600 copies of "
              "the examination timetable for the whole school. The same method is not best for both jobs. **Reprography** is the "
              "word for all the ways of reproducing documents."),
            D("**Copying** makes one or a few copies directly from an original. **Duplicating** makes many copies from a prepared "
              "**master** (a stencil, a spirit master or a plate). **Reprography** covers both.", title="Copying and duplicating"),
            H("Photocopying"),
            T("A photocopier works by **xerography** (an electrostatic process). In simple terms: light reflected from the original makes a "
              "pattern of electric charge on a drum; powder called **toner** sticks to the charged parts; the toner is pressed onto paper and "
              "fixed by heat. Modern machines also copy in colour, reduce or enlarge, copy both sides, and collate."),
            KEY("Photocopying in brief",
                "The most common method in offices today.",
                cards=[["Advantages", "Fast; no master to prepare; copies a book page, a letter or a drawing; good quality; ideal for a small number of copies."],
                       ["Disadvantages", "The cost per copy stays about the same however many are made, so it becomes expensive for large numbers. Toner and paper cost money, and the machine needs maintenance."]]),
            H("Spirit (hectograph) duplicating"),
            T("The typist or writer works on a **master sheet** backed by a sheet of carbon-like dye (usually purple). The writing becomes a "
              "reverse image on the back of the master. The master is fixed on a drum. As paper passes it, a little **spirit** (alcohol) "
              "softens the dye and a copy of the image is printed on each sheet. The method is cheap and fast for small to medium runs, "
              "but the master wears out, the colour fades, and the quality is lower. It is now old-fashioned."),
            H("Stencil duplicating"),
            T("A **stencil** (a thin wax-coated sheet) is cut by typing with the ribbon disengaged, or by writing with a stylus. The cut "
              "letters let ink pass through. The stencil is wrapped on an inked drum; as paper passes between the drum and a roller, ink is "
              "pressed through the cuts onto the paper. Many hundreds of copies are possible and the stencil can be stored and used again. Quality is "
              "fair; the machine can be hand operated, so it is useful where power is unreliable."),
            H("Offset lithography"),
            T("**Offset lithography** is used by printers for large jobs such as books and newspapers. A **plate** carries the image. The image "
              "parts attract greasy ink; the non-image parts attract water and refuse ink. The plate is wetted and inked, the inked image is "
              "**offset** (transferred) onto a rubber **blanket**, and the blanket presses the image onto the paper. Very high quality and "
              "a very low cost per copy for large quantities, but making the plate and setting up the machine is costly."),
            IMG("f5ofp2-offset-process.svg",
                alt="Three cylinders in a row: the plate cylinder carrying the inked image, the blanket cylinder that takes the image from the plate, and the impression cylinder that presses paper against the blanket.",
                caption="Figure 1. Offset lithography: plate, blanket and impression cylinders."),
            CODE("""COMPARISON (general guide; real machines vary)
Method       Master?        Quality   Number of copies   Cost per copy
-----------  -------------  --------  -----------------  ----------------
Photocopy    none           good      small              same at any number
Spirit       spirit master  fair      small to medium    low
Stencil      stencil        fair      medium to large    low
Offset       metal/paper    very good large to very      lowest for large
             plate                    large              runs; high set-up""", "text", title="Comparing the methods"),
            TIP("A digital duplicator is a modern machine that scans the original and makes its own master automatically, then prints many copies quickly "
                "at a low cost per copy. It does the work of the old stencil duplicator."),
            MISTAKE("Using one method for every job",
                    "A photocopier for 600 copies of a timetable wastes money; an offset press for 3 copies wastes money and time. Match the "
                    "method to the number of copies, the quality needed and the time and money available."),
            EX("Worked example 1: choose the method",
               intro="Choose the best method: (a) 3 copies of a signed letter; (b) 400 copies of a school notice, black and white, tomorrow; (c) 5 000 colour brochures for a trade fair.",
               steps=[
                   S("(a) Very few copies", text="Photocopying: no master and quick."),
                   S("(b) Many copies, quickly, simple quality", text="Duplicating by stencil or a digital duplicator: low cost per copy for hundreds."),
                   S("(c) Thousands, good colour quality", text="Offset lithography by a printer: highest quality and lowest cost per copy for large runs."),
               ]),
            EX("Worked example 2: where does the cost break even?",
               intro="Invented figures: a photocopier costs FCFA 25 a copy. A duplicator needs a master costing FCFA 1 500 plus FCFA 5 a copy. For how many copies do both cost the same? Which is cheaper for 200 copies?",
               steps=[
                   S("Write both costs", text="Photocopier: 25 n. Duplicator: 1 500 + 5 n, where n is the number of copies."),
                   S("Make them equal", text="25 n = 1 500 + 5 n, so 20 n = 1 500, so n = 75 copies."),
                   S("Test 200 copies", text="Photocopier: 25 x 200 = FCFA 5 000. Duplicator: 1 500 + 5 x 200 = FCFA 2 500."),
                   S("Conclusion", text="Above 75 copies the duplicator is cheaper. For 200 copies it saves FCFA 2 500."),
               ]),
            QUIZ("Which method is best for 2 copies of a letter?",
                 ["Photocopying", "Offset lithography", "Stencil duplicating", "Spirit duplicating"], 0,
                 "No master is needed, so the photocopier is quick for a few copies. The other methods need a master or plate whose cost is not worth it.",
                 hint="Which method needs no preparation?",
                 feedback=["", "A plate for two copies would be very costly.", "Cutting a stencil takes time and is not worth it for 2 copies.", "Preparing a master is not worth it for 2 copies."]),
            QUIZ("In offset lithography, what carries the image from the plate to the paper?",
                 ["A rubber blanket", "A stencil", "A spirit master", "A ribbon"], 0,
                 "The inked image is offset onto the blanket cylinder, which presses it onto the paper.",
                 hint="The word 'offset' means 'transferred indirectly'.",
                 feedback=["", "A stencil belongs to stencil duplicating.", "A spirit master belongs to spirit duplicating.", "A ribbon belongs to a typewriter."]),
            PQ("Distinguish between copying and duplicating.",
               "Copying makes one or a few copies directly from the original (for example photocopying). Duplicating makes many copies from a prepared master such as a stencil, spirit master or plate."),
            PQ("State two advantages and one disadvantage of photocopying.",
               "Advantages: quick; no master needed; can copy any document or a page of a book; good quality. Disadvantage: the cost per copy does not fall for large numbers, so it is expensive for a large run."),
            PQ("Explain briefly how stencil duplicating works.",
               "A stencil is cut by typing or writing so that the letters become openings. It is wrapped on an inked drum. As paper passes, ink is pressed through the openings onto the paper, so each sheet carries the image."),
            PQ("With the invented costs in Worked example 2, find the cost of 100 copies by each method and say which is cheaper.",
               "Photocopier: 25 x 100 = FCFA 2 500. Duplicator: 1 500 + 5 x 100 = FCFA 2 000. The duplicator is cheaper by FCFA 500."),
            TIP("This topic is usually tested in Paper 1 with questions on features and choice of method. The Paper 2 case study may ask which method an "
                "office should use for a given job. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("Copying makes a few copies from an original; duplicating makes many from a master. Reprography covers both.",
                "Photocopying (xerography) needs no master and suits few copies. Spirit and stencil duplicating use a master and suit more copies. Offset lithography suits very large, high-quality jobs.",
                "Choose by number of copies, quality, time and cost; compare costs with a simple equation.",
                "A digital duplicator is the modern form of the stencil duplicator."),
        ],
    ),
    # ------------------------------------------------------------------ 7. Collating, binding, shredding and laminating
    lesson(
        module=M5, topic="Collating, binding, shredding and laminating",
        title="Collating, binding, shredding, laminating and franking",
        slug="ofp2-collating-binding-shredding-laminating",
        minutes=20,
        summary="The finishing machines of the office: collating pages into sets, binding, shredding confidential papers, laminating to protect, and franking mail.",
        objectives=[
            "Define collating, binding, shredding and laminating",
            "Describe common binding methods and when to use each",
            "Explain why offices shred papers and what cross-cut shredding adds",
            "Describe a franking machine and its advantages",
        ],
        key_concepts=["Collating", "Binding", "Comb binding", "Spiral binding", "Shredding", "Laminating", "Franking machine"],
        blocks=[
            H("Introduction"),
            T("A Form 5 class in Limbe needs 30 copies of an eight-page handout. After printing, the pages lie in eight piles. "
              "Someone must gather page 1, page 2, up to page 8 into thirty sets, fasten them, and perhaps cover them. These "
              "are **finishing** jobs. They come after copying and before the documents are used or filed."),
            KEY("Four finishing jobs",
                "Learn the four terms exactly.",
                cards=[["Collating", "Gathering printed pages into the correct order to make complete sets."],
                       ["Binding", "Fastening the sets together so that they stay in order, such as a report or a handbook."],
                       ["Shredding", "Cutting paper into strips or small pieces so that it cannot be read."],
                       ["Laminating", "Sealing a document between two layers of clear plastic film for protection."]]),
            H("Collating"),
            T("**Collating** can be done by hand (laying the piles in a row and walking along it) or by a **collator**, a machine "
              "with several trays that takes one sheet from each tray in turn. Many photocopiers can collate as they copy, so each set comes "
              "out in order. A different job is **sorting** (for example sorting mail by destination) and **gathering** is a "
              "word some books use for collating (check your textbook)."),
            EX("Worked example 1: sheets and sets",
               intro="A handout has 18 pages. It is printed on both sides of each sheet. The class needs 25 sets. How many sheets of paper are needed? How many 500-sheet reams is that?",
               steps=[
                   S("Sheets in one set", text="18 pages on both sides gives 18 / 2 = 9 sheets."),
                   S("Sheets for 25 sets", text="9 x 25 = 225 sheets."),
                   S("Reams", text="225 / 500 = 0.45 of a ream, so one ream is enough with 275 sheets left."),
               ]),
            H("Binding"),
            T("Binding keeps pages together and gives a neat finish. The method depends on how many pages, how long the document "
              "must last, and whether pages may need to be added."),
            CODE("""BINDING METHODS (general guide)
Method            How it works                    Good for
----------------  ------------------------------  -------------------------
Stapling          wire staple through the corner  a few pages, short-term
Comb binding      plastic comb through punched    reports; pages can be
                  holes                           added or removed
Spiral (coil)     plastic or wire coil through    manuals, notebooks; opens
                  punched holes                   flat
Thermal binding   heated glue on the cover spine  neat reports, proposals
Perfect binding   glue along the spine            books, magazines
Ring / lever-arch pages punched and clipped in    documents that change,
file              metal rings                     office files""", "text", title="Binding"),
            H("Shredding"),
            T("A **shredder** cuts paper into strips (**strip-cut**) or into small pieces (**cross-cut**). Cross-cut shredding is safer, because "
              "strips can be pieced together. Offices shred documents that contain personal data, salaries, bank details, contracts "
              "and business secrets when the retention period has ended (see the lesson on retention). Keep a record of what was shredded."),
            H("Laminating"),
            T("A **laminator** seals a document between two sheets of plastic film using heat and pressure. The document is "
              "protected from water, dirt and wear, and it stays clean. Offices laminate identity cards, price lists, notices on a wall, maps and "
              "documents handled often. A laminated document cannot be changed and cannot be written on."),
            MISTAKE("Laminating a document that must be updated",
                    "A laminated timetable or price list cannot be corrected without making a new one. Laminate only items that will stay unchanged, or use a version that can be erased with a marker."),
            H("Franking machines"),
            T("A **franking machine** prints a postage mark on envelopes or on labels instead of using stamps. The mark shows the postage "
              "paid and the date. The user pays the postal service in advance for the postage the machine can print, and the meter counts it. "
              "The details of how this is arranged depend on the postal operator, so check the current arrangements."),
            KEY("Advantages of franking",
                "Franking saves time and money in offices with a lot of outgoing mail.",
                cards=[["No stamps to stick", "The envelope is marked in one step, and many letters are franked quickly."],
                       ["Control", "The meter records the postage used, so there is a record and less risk of stolen stamps."],
                       ["Accuracy", "The machine can be set to the exact postage, so letters are not over or underpaid."],
                       ["Advertising", "A slogan or logo can be printed next to the mark (where allowed)."]]),
            EX("Worked example 2: choosing finishing methods",
               intro="An office must (a) prepare a 60-page training manual that opens flat, (b) destroy old salary sheets, (c) protect a notice on the outside notice board from rain.",
               steps=[
                   S("(a) The manual", text="Spiral (coil) binding: the pages lie flat and the coil holds 60 pages."),
                   S("(b) The salary sheets", text="Cross-cut shredding: the information is confidential."),
                   S("(c) The outside notice", text="Laminating: protects against rain and dirt."),
               ]),
            EX("Worked example 3: sets for a meeting",
               intro="Notice, agenda and last minutes are to be collated and stapled for 14 members, one set each, plus 2 spare sets. The notice is 1 page, the agenda 2 pages and the minutes 4 pages, single-sided. How many pages are printed?",
               steps=[
                   S("Pages in a set", text="1 + 2 + 4 = 7 pages."),
                   S("Number of sets", text="14 + 2 = 16 sets."),
                   S("Total pages", text="7 x 16 = 112 pages."),
               ]),
            QUIZ("Gathering printed pages into the correct order to make complete sets is called",
                 ["collating", "binding", "laminating", "franking"], 0,
                 "Collating is putting pages in order. Binding then fastens them.",
                 hint="The word begins with C and has to do with order.",
                 feedback=["", "Binding is fastening.", "Laminating covers with plastic.", "Franking marks postage."]),
            QUIZ("Why is cross-cut shredding safer than strip-cut shredding?",
                 ["The paper is cut into small pieces that are hard to piece together", "It uses less paper", "It makes the paper waterproof", "It prints a postage mark"], 0,
                 "Strips can be re-assembled; small cross-cut pieces are much harder to read again.",
                 hint="Which one leaves smaller pieces?",
                 feedback=["", "Shredding does not use paper.", "That is laminating.", "That is franking."]),
            PQ("List four finishing jobs in an office and say what each does.",
               "Collating (gathers pages into sets), binding (fastens sets), shredding (destroys confidential papers) and laminating (seals documents in plastic). Franking (marks postage) may also be included."),
            PQ("State two advantages of using a franking machine rather than stamps.",
               "Letters are marked quickly with no stamps to stick; the meter records postage used (control); the correct postage is printed accurately; stamp theft is avoided. (Any two.)"),
            PQ("A report of 40 pages will be updated every month and pages may be added. Suggest a binding method and give a reason.",
               "Ring (lever-arch) binding, or comb binding, because pages can be removed and added. A glued (perfect) binding could not be changed."),
            PQ("A handout has 12 pages, printed on both sides. How many sheets are used for 30 sets?",
               "12 / 2 = 6 sheets for each set. 6 x 30 = 180 sheets."),
            TIP("Finishing machines are favourite Paper 1 topics (match the term to its meaning, choose a method). In Paper 2 you may need to recommend equipment for a case. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("Collating arranges pages in order; binding fastens them; shredding destroys confidential papers; laminating protects with plastic.",
                "Common binding methods: staple, comb, spiral, thermal, perfect and ring file. Choose by pages, life and need to change.",
                "Cross-cut shredding is safer than strip-cut. Shred confidential papers and keep a record.",
                "A franking machine prints postage marks instead of stamps and records the postage used."),
        ],
    ),
    # ------------------------------------------------------------------ 8. Computers, printers and scanners
    lesson(
        module=M5, topic="Computers, printers and scanners",
        title="Computers, printers and scanners in the office",
        slug="ofp2-computers-printers-scanners",
        minutes=22,
        summary="The parts of an office computer, the main types of printer and scanner, how to compare speed, quality and running cost, and the benefits and limits of office automation.",
        objectives=[
            "Name the main parts of a computer system and their jobs",
            "Compare inkjet, laser, dot-matrix and thermal printers",
            "Describe flatbed and sheet-fed scanners and the meaning of resolution",
            "Calculate printing time and cost per page from simple data",
        ],
        key_concepts=["Input and output", "Processor", "Storage", "Laser printer", "Inkjet printer", "Dot-matrix printer", "Scanner", "Resolution (dpi)"],
        blocks=[
            H("Introduction"),
            T("A bank office in Douala once ran on typewriters and carbon paper. Today a clerk types a letter once, saves it, prints it, "
              "scans the reply and sends both by email. **Office automation** means using machines, especially computers, to do office tasks "
              "faster, with fewer errors, and with better storage."),
            D("A **computer system** has **hardware** (the physical parts) and **software** (the programs that tell the hardware what to do). "
              "Hardware has four groups: input, processing, storage and output.", title="Computer system"),
            KEY("Parts of a computer system",
                "Learn one example of each group.",
                cards=[["Input devices", "Put data into the computer: keyboard, mouse, scanner, microphone, camera, touch screen."],
                       ["Processor (CPU) and memory", "The CPU carries out instructions. RAM is working memory that loses its contents when power goes off."],
                       ["Storage", "Keeps data for later: hard disk, solid-state drive, flash drive, memory card, cloud storage."],
                       ["Output devices", "Give results to people: monitor, printer, speakers."]]),
            T("**Software** includes the operating system (which runs the computer), and application programs such as a word processor "
              "(letters and reports), a spreadsheet (tables and calculations), a database (records) and email."),
            H("Printers"),
            T("A printer produces a **hard copy** (paper) of what is on the screen. Choose by speed, quality, cost, noise and what you want to print."),
            CODE("""PRINTERS (general guide)
Type          How it prints                  Strengths              Weaknesses
------------  -----------------------------  ---------------------  ---------------------
Inkjet        sprays tiny drops of liquid    cheap to buy, colour,  ink is costly for big
              ink                            good photos            jobs; slow; ink smudges
Laser         toner powder fused by heat     fast, sharp text,      costly to buy; colour
              (like a photocopier)           cheap per page         laser is dearer
Dot-matrix    pins strike a ribbon (impact)  cheap to run, makes    noisy, slow, poor
                                             carbon copies (forms)  quality
Thermal       heat on special paper          small, quiet, no ink   special paper fades;
                                             (till receipts)        poor quality""", "text", title="Comparing printers"),
            TIP("Dot-matrix printers are an impact printer: they can print through several layers of paper at once, so they are still used for "
                "multi-part forms such as invoices. Inkjet and laser printers are non-impact."),
            D("**Printer speed** is measured in pages per minute (ppm). **Print quality** is measured in dots per inch (dpi): more dots give a sharper "
              "page. **Running cost** is the cost of ink or toner, paper and repair for each page printed.", title="Speed, quality, cost"),
            H("Scanners"),
            T("A **scanner** is an input device that copies a paper document or photograph into the computer as a digital image. "
              "A **flatbed** scanner has a glass plate; you lay the page or a book on it. A **sheet-fed** scanner pulls a pile of loose pages "
              "through automatically, which is quick for many pages. A phone camera with a scanning app does the same job in a small office."),
            KEY("Scanning terms",
                "Resolution and file format decide the size and clarity of the scan.",
                cards=[["Resolution (dpi)", "Dots per inch. A higher dpi gives a clearer image and a bigger file. A common setting for text documents is 300 dpi (check your scanner guide)."],
                       ["OCR", "Optical character recognition turns a scanned image of text into text that can be edited and searched."],
                       ["File format", "PDF is common for documents; JPEG for photographs."]]),
            MISTAKE("Scanning everything at the highest resolution",
                    "A very high dpi creates huge files that fill the disk and take long to send by email. Use the lowest setting that keeps the text clear."),
            H("Benefits and limits of office automation"),
            CODE("""BENEFITS                              LIMITS
+ Speed: letters typed once,          - Cost of equipment, software
  corrected easily                      and repair
+ Accuracy: spell and calculation     - Need for electricity and
  checks                                reliable internet
+ Storage: thousands of documents     - Staff need training
  on one disk                         - Viruses, hacking, data loss
+ Sharing: email to many at once      - Job changes: some tasks disappear""", "text", title="Office automation"),
            T("In places with power cuts, offices use a **UPS** (uninterruptible power supply), a battery that gives a few minutes of power so "
              "that work can be saved, and a surge protector against power spikes."),
            EX("Worked example 1: printing time",
               intro="A laser printer prints 20 pages per minute (ppm). How long does it take to print 150 pages? (Ignore warm-up.)",
               steps=[
                   S("Divide pages by speed", text="150 / 20 = 7.5 minutes."),
                   S("Convert", text="7.5 minutes is 7 minutes 30 seconds."),
               ]),
            EX("Worked example 2: cost per page",
               intro="A toner cartridge (invented figures) costs FCFA 36 000 and prints 2 000 pages. Paper costs FCFA 3 a sheet. What is the running cost of one page? What is the cost of 500 pages?",
               steps=[
                   S("Toner per page", text="36 000 / 2 000 = FCFA 18."),
                   S("Add paper", text="18 + 3 = FCFA 21 a page."),
                   S("500 pages", text="21 x 500 = FCFA 10 500."),
               ]),
            EX("Worked example 3: choose the printer",
               intro="Which printer for (a) a shop till receipt, (b) a school office printing 300 pages of text a day, (c) a firm printing invoices on 3-part carbonless forms?",
               steps=[
                   S("(a) Till receipt", text="Thermal printer: small, quiet, no ink."),
                   S("(b) 300 pages a day", text="Laser printer: fast and cheap per page."),
                   S("(c) 3-part forms", text="Dot-matrix (impact) printer: it prints through several layers."),
               ]),
            QUIZ("Which printer uses toner powder and a heat process like a photocopier?",
                 ["Laser printer", "Inkjet printer", "Dot-matrix printer", "Thermal printer"], 0,
                 "A laser printer fuses toner onto paper with heat.",
                 hint="Which printer is the 'cousin' of the photocopier?",
                 feedback=["", "Inkjet uses liquid ink.", "Dot-matrix uses pins and a ribbon.", "Thermal uses heat-sensitive paper."]),
            QUIZ("A scanner is an",
                 ["input device", "output device", "storage device", "printer"], 0,
                 "A scanner sends the image of a document into the computer.",
                 hint="Does data go into the computer or out of it?",
                 feedback=["", "Output devices send results out, like a monitor.", "Storage devices keep data, like a disk.", "A printer is an output device."]),
            PQ("State two differences between a laser printer and a dot-matrix printer.",
               "Laser: fast, quiet, sharp text, non-impact (toner and heat), cannot make carbon copies. Dot-matrix: slow, noisy, poorer quality, impact (pins), can print several layers at once."),
            PQ("Define resolution and state its unit.",
               "Resolution is the amount of detail in a scan or print, measured in dots per inch (dpi)."),
            PQ("A printer prints 25 ppm. How long to print 100 pages?",
               "100 / 25 = 4 minutes."),
            PQ("Give three advantages and two limits of using computers in an office.",
               "Advantages: speed, accuracy, easy storage, easy sharing and editing. Limits: cost of equipment, need for electricity and training, risk of viruses and data loss. (Any three advantages and two limits.)"),
            TIP("Names of devices and their uses are common in Paper 1; in Paper 2 you may be asked to recommend equipment for a case. Give a reason.", title="Exam link"),
            SUM("A computer system has input, processing, storage and output hardware plus software.",
                "Printers: inkjet (liquid ink), laser (toner), dot-matrix (impact, multi-part forms), thermal (heat paper). Speed in ppm, quality in dpi.",
                "A scanner is an input device; flatbed for books, sheet-fed for piles. A higher dpi means a clearer but larger file. OCR makes scanned text editable.",
                "Automation brings speed, accuracy, storage and sharing, but needs money, power, training and protection of data."),
        ],
    ),
    # ------------------------------------------------------------------ 9. Virtual office software
    lesson(
        module=M5, topic="Virtual office software",
        title="Virtual office software and working online",
        slug="ofp2-virtual-office-software",
        minutes=20,
        summary="Tools that let staff work together from different places (email, shared documents, cloud storage, video calls, messaging, calendars), their benefits, risks and safe use, including on low data.",
        objectives=[
            "Explain what a virtual office is",
            "Name the main types of virtual office software and what each does",
            "State the advantages and disadvantages of working virtually",
            "Describe safe use of online tools, including when data and power are limited",
        ],
        key_concepts=["Virtual office", "Cloud storage", "Video conferencing", "Shared document", "Two-step login", "Bandwidth", "Synchronisation"],
        blocks=[
            H("Introduction"),
            T("A small company in Buea has three staff: one in the office, one working from Limbe and one in Yaounde. They share the same "
              "documents, hold a weekly meeting on a video call and agree tasks in a message group. They have no big building. This is a "
              "**virtual office**."),
            D("A **virtual office** is a way of working in which staff work together through the internet and online tools, instead of all "
              "being in one building. **Virtual office software** is the set of programs and online services that make this possible.", title="Virtual office"),
            H("Main kinds of virtual office software"),
            KEY("Tools and their jobs",
                "Examples of products are given only to help you recognise them. Which product an office chooses depends on cost and need.",
                cards=[["Email", "Formal messages with attachments. Keeps a written record. Used with clients and for official letters."],
                       ["Instant messaging", "Quick chat in groups or one-to-one, such as WhatsApp or Slack. Fast but easily mixed with private chat."],
                       ["Video and audio conferencing", "Meetings with people in different places, such as Zoom, Google Meet or Microsoft Teams. Audio-only uses much less data."],
                       ["Shared documents and spreadsheets", "Several people edit the same file online at once, and the changes are saved as versions."],
                       ["Cloud storage", "Files stored on the provider's servers (for example Google Drive, OneDrive) and reached from any device. Also a backup."],
                       ["Calendars and task boards", "Shared diary for meeting times and a board that shows who does what and by when."],
                       ["E-signature and online forms", "Documents signed and forms filled on screen. Check the current rules on which signatures are accepted."]]),
            D("**Cloud storage** means keeping files on internet servers run by a provider, instead of only on your own computer. "
              "**Synchronisation** (sync) means that the copy on your device and the copy in the cloud are updated to match.", title="Cloud storage and sync"),
            H("Advantages and disadvantages"),
            CODE("""VIRTUAL OFFICE
ADVANTAGES (+)                        DISADVANTAGES (-)
+ Saves rent, transport and time      - Needs reliable internet and power
+ Staff can work from different       - Data costs money in some places
  towns or at home                    - Security risks: stolen passwords,
+ Documents are shared at once,         leaked files
  with a history of changes           - Staff may feel alone; slower
+ Cloud storage works as a backup       team spirit
+ Easy to hold meetings without       - Distractions at home; hard to
  travelling                            separate work and private life""", "text", title="Advantages and disadvantages"),
            H("Using it safely"),
            KEY("Safe habits",
                "A virtual office is only as safe as its weakest password.",
                cards=[["Strong, different passwords", "Long passwords, never shared and not the same for every account."],
                       ["Two-step login", "A second proof, such as a code sent to your phone, protects the account even if the password is stolen."],
                       ["Careful sharing", "Share a file only with the people who need it. Choose 'view only' or 'edit' on purpose."],
                       ["Beware of fake messages", "Do not click strange links or open unexpected attachments. Phishing messages try to trick you into giving a password."],
                       ["Public Wi-Fi", "Avoid opening confidential files on open public networks."],
                       ["Backups and updates", "Keep a second copy of important files and keep the software up to date."]]),
            MISTAKE("Sharing a password to 'save time'",
                    "If two people share a password, you cannot tell who did what, and a leak affects everyone. Give each person their own account with the right access level."),
            H("Working on low data and weak power"),
            T("In many parts of Cameroon the internet can be slow, data bundles cost money, and power cuts happen. A good virtual office plans for this."),
            KEY("Practical tips",
                "These are simple actions, not special software.",
                cards=[["Save data", "Join a meeting with audio only, or turn the camera off. Send small files; compress pictures before sending."],
                       ["Work offline", "Many tools let you work offline and sync when the connection returns. Turn on offline mode before you travel."],
                       ["Schedule heavy tasks", "Upload and update large files when the connection is better or cheaper."],
                       ["Protect your work", "Save often; use a power bank or UPS for the router and laptop."]]),
            EX("Worked example 1: choose the tool",
               intro="Choose the best tool: (a) three staff must edit one report together; (b) the director in Yaounde must meet staff in Bamenda tomorrow; (c) a client needs a formal written confirmation of an order.",
               steps=[
                   S("(a) Edit together", text="A shared online document, with comments and version history."),
                   S("(b) Meeting at a distance", text="Video conferencing (or audio conferencing if data is low)."),
                   S("(c) Formal confirmation", text="Email, because it keeps a written record that can be filed."),
               ]),
            EX("Worked example 2: how many calls?",
               intro="A data bundle has 3 GB left. A one-hour video call uses about 0.6 GB (invented figure). How many one-hour video calls can the bundle cover, ignoring all other use? How many one-hour audio calls if audio uses 0.06 GB an hour (invented)?",
               steps=[
                   S("Video", text="3 / 0.6 = 5 calls."),
                   S("Audio", text="3 / 0.06 = 50 calls."),
                   S("Meaning", text="Audio-only calls use a tenth of the data in this example. When data is costly, use audio and keep the camera off."),
               ]),
            EX("Worked example 3: set up a safe account",
               intro="A new staff member joins the virtual office. List the steps to protect her access.",
               steps=[
                   S("Own account", text="Create a personal login. Do not use someone else's."),
                   S("Strong password and two-step login", text="Choose a long password that is used nowhere else, and turn on the second step."),
                   S("Access level", text="Give her access only to the folders she needs, with edit rights only where needed."),
                   S("Training", text="Show her how to spot a phishing message."),
               ]),
            QUIZ("What does cloud storage allow a staff member to do?",
                 ["Reach files from any device with an internet connection", "Print without a printer", "Work only when there is no internet", "Avoid using passwords"], 0,
                 "Files kept on the provider's servers can be opened from any device that is signed in.",
                 hint="'Cloud' means the files are stored on the internet.",
                 feedback=["", "A printer is still needed.", "Cloud storage needs internet to sync.", "Passwords are still needed."]),
            QUIZ("Which action best protects an account if the password is stolen?",
                 ["Two-step login", "Telling a friend the password", "Using the same password everywhere", "Writing the password on a sticky note beside the computer"], 0,
                 "A second proof, such as a code sent to your phone, stops a thief who has only the password.",
                 hint="What stops a thief who knows the password?",
                 feedback=["", "Sharing a password makes the risk larger.", "Using the same password in many places spreads the risk.", "A note beside the computer can be read by others."]),
            PQ("What is a virtual office?",
               "A way of working in which staff in different places work together through the internet and online tools, such as email, video calls and shared documents, instead of all sitting in one building."),
            PQ("State two advantages and two disadvantages of a virtual office.",
               "Advantages: saves rent and transport; staff can work from different places; documents are shared at once. Disadvantages: needs reliable internet and power; data costs; security risks; staff may feel isolated. (Any two of each.)"),
            PQ("Give three ways to use less data in an online meeting.",
               "Use audio only; turn off the camera; send small files or compress pictures; share a link to a shared file instead of attaching it. (Any three.)"),
            PQ("Explain why a phishing message is dangerous and how staff should react.",
               "It pretends to come from a trusted person or company to trick the user into giving a password or opening a harmful file. Staff should not click the link or open the attachment, and should report the message to the office manager."),
            TIP("Virtual office software appears in Paper 1 as definitions and uses of tools, and in Paper 2 as advice to a firm that wants to work online. "
                "Always mention a benefit and a risk, and remember data and power limits.", title="Exam link"),
            SUM("A virtual office lets staff work together through the internet using email, messaging, video conferencing, shared documents, cloud storage and shared calendars.",
                "Benefits: lower cost, flexibility and fast sharing. Risks: internet and power limits, data cost, security and isolation.",
                "Stay safe with strong, separate passwords, two-step login, careful sharing and caution with fake messages.",
                "On low data use audio, small files, offline mode and scheduled uploads."),
        ],
    ),
    # ------------------------------------------------------------------ 10. Types of meetings
    lesson(
        module=M6, topic="Types of meetings",
        title="Types of business meetings",
        slug="ofp2-types-of-meetings",
        minutes=18,
        summary="Why organisations hold meetings and the main types: annual general meeting, extraordinary general meeting, board meeting, committee (standing, ad hoc, sub-committee) and staff meeting.",
        objectives=[
            "Define a meeting and give reasons why organisations hold meetings",
            "Describe the AGM, EGM, board meeting and committee meeting",
            "Distinguish standing, ad hoc and sub-committees",
            "Choose the type of meeting that fits a given situation",
        ],
        key_concepts=["Meeting", "Annual General Meeting", "Extraordinary General Meeting", "Board meeting", "Committee", "Standing committee", "Ad hoc committee"],
        blocks=[
            H("Introduction"),
            T("A cooperative society in Bamenda has 400 members. Once a year all members meet to hear the accounts. The ten directors meet "
              "every month to run the society. A small group of five studies a loan request and reports back. The society holds three "
              "kinds of meeting for three different purposes."),
            D("A **meeting** is a gathering of two or more people, called for a stated purpose, to discuss matters and to make "
              "decisions or recommendations.", title="Meeting"),
            KEY("Why organisations hold meetings",
                "Meetings are a way to share information and to decide together.",
                cards=[["Inform", "Give news and instructions to many people at once."],
                       ["Discuss and advise", "Collect ideas and opinions before a decision."],
                       ["Decide", "Take formal decisions that bind the organisation."],
                       ["Report and account", "Managers report to owners or members on their work and on the money."]]),
            H("The Annual General Meeting (AGM)"),
            D("The **Annual General Meeting** is the meeting of all the members or shareholders, held once every year. It is required by "
              "law or by the rules of the organisation (check the current rules for your type of organisation).", title="AGM"),
            T("Usual business at an AGM: receiving the annual report and accounts, electing or re-electing directors or officers, "
              "appointing the auditors who check the accounts, and (in a company) declaring a dividend. Members receive notice well in advance."),
            H("The Extraordinary General Meeting (EGM)"),
            D("An **Extraordinary General Meeting** (EGM) is a general meeting of members held at any time other than the AGM, to deal "
              "with urgent business that cannot wait until the next AGM.", title="EGM"),
            T("Examples: a proposal to change the rules of the organisation, to sell a major property, or to remove an officer. Often "
              "the notice must say exactly what will be discussed, and only that business may be decided. Who may call an EGM and with what notice depend on the rules, so check your textbook."),
            H("The Board meeting"),
            D("A **board meeting** is a meeting of the directors, who are chosen by the members to manage the organisation. "
              "Boards meet regularly (for example monthly or every quarter) to make policy decisions and to review progress.", title="Board meeting"),
            H("Committees"),
            D("A **committee** is a small group of people chosen by a larger body to study a matter, advise, or act on its behalf. "
              "The committee reports back to the body that appointed it.", title="Committee"),
            KEY("Kinds of committee",
                "The difference is the length of life of the committee.",
                cards=[["Standing committee", "Permanent. Deals with a continuing area, for example Finance or Discipline."],
                       ["Ad hoc (special) committee", "Set up for one task, for example to organise a school anniversary. It ends when the task is done and the report is given."],
                       ["Sub-committee", "A small group chosen from a committee to study one part of its work."],
                       ["Joint committee", "Members come from two or more bodies, for example teachers and parents."]]),
            T("Other meetings: a **staff** (or departmental) meeting is for passing on information and instructions in a firm; a **general** meeting "
              "is for all members of a club or association; a **statutory** meeting is the first meeting of a new public company in some countries' law "
              "(check your textbook, as rules differ and some books omit it). In schools, the **PTA** (Parent-Teacher Association) holds a general meeting and an executive meeting."),
            CODE("""TYPE OF MEETING        WHO ATTENDS                 WHEN                    PURPOSE
Annual General (AGM)   all members/shareholders   once a year            accounts, elections,
                                                                         auditors
Extraordinary (EGM)    all members/shareholders   when urgent business    one special matter
                                                  arises
Board meeting          directors                  regularly (e.g. monthly) manage and decide policy
Standing committee     chosen members             regularly, permanent     continuing area of work
Ad hoc committee       chosen members             for one task only        one task, then report""", "text", title="Summary table"),
            MISTAKE("Mixing up the AGM and the board meeting",
                    "The AGM is for all members, once a year. The board meeting is for the directors only and is held more often. Do not say that the board 'is' the AGM."),
            EX("Worked example 1: which meeting?",
               intro="Decide the type of meeting: (a) every member must hear the annual accounts; (b) the members must vote at once on selling the society's land; (c) ten directors review monthly sales.",
               steps=[
                   S("(a) Annual accounts", text="AGM: all members, yearly."),
                   S("(b) Urgent sale of land", text="EGM: urgent business that cannot wait for the next AGM."),
                   S("(c) Monthly review by directors", text="Board meeting."),
               ]),
            EX("Worked example 2: standing or ad hoc?",
               intro="A school sets up (a) a Finance Committee that serves every year, and (b) a team of four to plan the end-of-year party. Classify each.",
               steps=[
                   S("(a) Finance Committee", text="Standing committee: permanent and continuing."),
                   S("(b) Party team", text="Ad hoc committee: set up for one task and ends after the party."),
                   S("Reporting", text="Both report to the body that appointed them."),
               ]),
            EX("Worked example 3: counting meetings",
               intro="A firm's board meets once a month; the finance committee meets every quarter (every three months); there is one AGM a year (invented plan). How many meetings of these three kinds are held in a year?",
               steps=[
                   S("Board", text="12 meetings."),
                   S("Finance committee", text="12 / 3 = 4 meetings."),
                   S("AGM", text="1 meeting."),
                   S("Total", text="12 + 4 + 1 = 17 meetings."),
               ]),
            QUIZ("Urgent business arises in March, although the AGM is in December. Which meeting is called?",
                 ["Extraordinary General Meeting", "Annual General Meeting", "Standing committee", "Staff meeting"], 0,
                 "An EGM deals with urgent business between AGMs.",
                 hint="The word 'extra' gives a clue.",
                 feedback=["", "The AGM is held once a year, in December in this case.", "A committee cannot replace the members' decision.", "A staff meeting is not a members' meeting."]),
            QUIZ("A committee is set up for one task and ends when the task is done. It is a(n)",
                 ["ad hoc committee", "standing committee", "board", "AGM"], 0,
                 "Ad hoc means 'for this purpose'. It ends when the job is complete.",
                 hint="Is it permanent?",
                 feedback=["", "A standing committee is permanent.", "A board is the permanent body of directors.", "An AGM is a meeting of all members once a year."]),
            PQ("State four reasons why organisations hold meetings.",
               "To give information; to discuss and get advice; to take decisions; to receive reports from managers; to solve problems together. (Any four.)"),
            PQ("Distinguish between an AGM and an EGM.",
               "An AGM is held once every year for all members, for regular business such as accounts, elections and auditors. An EGM can be held at any other time to deal with urgent business that cannot wait for the next AGM."),
            PQ("Give two differences between a standing committee and an ad hoc committee.",
               "A standing committee is permanent and deals with a continuing area; an ad hoc committee is temporary and set up for one task. The standing committee meets regularly through the years; the ad hoc committee ends when it has reported."),
            PQ("A board meets every 2 months. How many board meetings are held in one year?",
               "12 / 2 = 6 meetings."),
            TIP("Types of meetings are a common Paper 1 topic (definitions and match-ups). In a Paper 2 case study you may decide which type of meeting a given problem needs. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("A meeting is a gathering called for a stated purpose to discuss and decide.",
                "The AGM is for all members once a year; an EGM is for urgent business between AGMs; the board meeting is for the directors.",
                "A committee is a small group chosen by a larger body. Standing committees are permanent; ad hoc committees end when their task is done.",
                "Rules about who may call meetings and with what notice differ, so check your textbook and the organisation's rules."),
        ],
    ),
    # ------------------------------------------------------------------ 11. Requirements for a valid meeting
    lesson(
        module=M6, topic="Requirements for a valid meeting",
        title="What makes a meeting valid: notice, agenda, quorum, proxy, motion and resolution",
        slug="ofp2-valid-meeting-requirements",
        minutes=25,
        summary="The conditions that make a meeting valid and its decisions binding: notice, agenda, quorum, proxy, motions, voting and resolutions, with a model notice and agenda.",
        objectives=[
            "List the requirements for a valid meeting",
            "Define notice, agenda, quorum, proxy, motion, amendment and resolution",
            "Draft a notice and an agenda in correct layout",
            "Decide whether a motion is carried from a vote count",
        ],
        key_concepts=["Notice", "Agenda", "Quorum", "Proxy", "Motion", "Amendment", "Resolution", "Casting vote"],
        blocks=[
            H("Introduction"),
            T("Imagine a village development association. Only four of 40 members come to a meeting called with a day's notice, and "
              "they vote to sell the association's land. Is the decision valid? Most rules say no. A meeting must be properly "
              "called and properly held. Otherwise members who were absent can challenge the decisions."),
            KEY("Requirements for a valid meeting",
                "Rules differ between organisations and countries, so use the rules of the organisation and check your textbook. These are the ideas that are almost always required.",
                cards=[["Properly called", "The meeting is called by a person or body that has the power to call it."],
                       ["Proper notice", "Every member who is entitled receives written notice, in the form and the time the rules require."],
                       ["Agenda", "A list of the business to be discussed is sent or shown in advance."],
                       ["Quorum", "The minimum number of members must be present for decisions to be valid."],
                       ["Chairperson", "A properly chosen chairperson controls the meeting."],
                       ["Rules of procedure followed", "Motions, debate and voting follow the rules."]]),
            H("Notice"),
            D("A **notice** of a meeting is a written announcement sent to members telling them the **kind of meeting, the date, time and place**, and "
              "the business to be discussed. The number of days of notice is set by the rules or the law, so we do not give one figure here.", title="Notice"),
            CODE("""                  GREEN VALLEY FARMERS' COOPERATIVE
                  P.O. Box 00, Bamenda   (invented)

                          NOTICE OF MEETING

Notice is hereby given that the Annual General Meeting of the
Cooperative will be held in the Community Hall, Bamenda, on
Saturday 14 March 2026 at 10.00 a.m.

The agenda is attached.

Members who cannot attend may appoint a proxy. Proxy forms must
reach the Secretary not later than 7 March 2026.

By order of the Committee.

(signed)
N. Tabi
Secretary
Date of notice: 20 February 2026""", "text", title="Model notice (all names invented)"),
            H("Agenda"),
            D("An **agenda** is a list of the items of business to be discussed, in the order in which they will be taken. It helps members to prepare "
              "and keeps the meeting on its subject.", title="Agenda"),
            CODE("""                   GREEN VALLEY FARMERS' COOPERATIVE
                   AGENDA, ANNUAL GENERAL MEETING
                   Saturday 14 March 2026, 10.00 a.m., Community Hall

 1. Apologies for absence
 2. Minutes of the last Annual General Meeting
 3. Matters arising from the minutes
 4. Chairperson's report
 5. Treasurer's report and accounts for the year
 6. Election of officers
 7. Appointment of auditors
 8. Any other business
 9. Date of next meeting""", "text", title="Model agenda (names invented)"),
            T("The standard order is the one above. 'Any other business' (AOB) comes last, so that new, important matters can be raised; "
              "decisions on big new matters are better postponed to a properly notified meeting."),
            IMG("f5ofp2-meeting-flow.svg",
                alt="A flow chart of a meeting: notice and agenda sent, quorum checked, chairperson opens, apologies and minutes, business with motion, debate and vote, any other business, close, minutes written.",
                caption="Figure 1. The path from notice to minutes."),
            H("Quorum"),
            D("The **quorum** is the minimum number of members who must be present for the meeting to be able to take valid decisions. It is "
              "fixed by the rules of the organisation or the law (for example 'five members' or 'one third of the members'). If there is no quorum, "
              "the meeting is usually adjourned to another day.", title="Quorum"),
            H("Proxy"),
            D("A **proxy** is a person appointed by a member to attend a meeting and vote for that member. The member signs a **proxy form** "
              "naming the proxy. Many companies allow proxies; many clubs do not, so check the rules.", title="Proxy"),
            H("Motion, amendment, resolution"),
            KEY("From motion to resolution",
                "A decision is made in four steps.",
                cards=[["Motion", "A proposal put to the meeting, usually in the words 'I propose that...'. It needs a proposer and a seconder."],
                       ["Amendment", "A proposed change to the motion, which is discussed and voted on first."],
                       ["Vote", "By show of hands, by a count (a poll), or by secret ballot. The chairperson announces the result."],
                       ["Resolution", "A motion that has been passed becomes a resolution and is recorded in the minutes. An ordinary resolution needs a simple majority (more than half of the votes cast). A special resolution needs a larger majority fixed by the law or rules, so check your textbook."]]),
            D("The **casting vote** is an extra vote given to the chairperson when votes are equal, if the rules allow it.", title="Casting vote"),
            MISTAKE("Counting abstentions as votes against",
                    "A member who abstains does not vote for or against. Check the rules: in a simple majority of votes cast, abstentions are not counted. The meeting is not against the motion because some members abstained."),
            EX("Worked example 1: is there a quorum?",
               intro="The rules of a society (invented) say the quorum is one fifth of its 60 members. At the meeting 11 members are present. May the meeting begin?",
               steps=[
                   S("Find the quorum", text="60 / 5 = 12 members."),
                   S("Compare", text="11 is less than 12, so there is no quorum."),
                   S("Action", text="The meeting cannot take valid decisions. The chairperson adjourns it, or waits a short time if the rules allow, and the secretary records the facts."),
               ]),
            EX("Worked example 2: is the motion carried?",
               intro="At a meeting 50 members are present. On a motion to raise the annual fee, 28 vote for, 15 vote against and 7 abstain. The rules require a simple majority of the votes cast.",
               steps=[
                   S("Votes cast", text="28 + 15 = 43 (the 7 abstentions are not votes cast)."),
                   S("More than half?", text="Half of 43 is 21.5, and 28 is more than 21.5."),
                   S("Result", text="The motion is carried and becomes a resolution. If the rules had needed a majority of all members present (more than 25), 28 would still be enough."),
               ]),
            EX("Worked example 3: a tie and the casting vote",
               intro="On another motion, 20 vote for and 20 against. The rules give the chairperson a casting vote. What happens?",
               steps=[
                   S("Equal votes", text="20 = 20: no majority."),
                   S("Casting vote", text="The chairperson votes once more, so one side has 21 votes."),
                   S("Result", text="The side the chairperson supports wins. Without a casting vote the motion usually fails."),
               ]),
            QUIZ("The minimum number of members who must be present for a meeting to take valid decisions is the",
                 ["quorum", "agenda", "proxy", "minutes"], 0,
                 "The quorum is fixed by the rules. Without it, decisions are not valid.",
                 hint="The word begins with Q.",
                 feedback=["", "The agenda is the list of business.", "A proxy is a person who votes for an absent member.", "Minutes are the record of the meeting."]),
            QUIZ("A motion that has been passed is called a",
                 ["resolution", "notice", "amendment", "proxy"], 0,
                 "Motion is the proposal; resolution is the motion after it has been passed.",
                 hint="The motion has changed status after the vote.",
                 feedback=["", "A notice is a written call to the meeting.", "An amendment is a change proposed to a motion.", "A proxy is an authorised representative."]),
            PQ("List five requirements for a valid meeting.",
               "Properly called; proper notice; an agenda; a quorum present; a chairperson; rules of procedure followed. (Any five.)"),
            PQ("Distinguish between a motion and a resolution.",
               "A motion is a proposal put to a meeting for discussion and vote. A resolution is a motion that has been passed by the required majority and is recorded in the minutes."),
            PQ("The quorum of a committee is one third of its 18 members (invented). How many must be present? If 5 are present, is there a quorum?",
               "18 / 3 = 6 members. 5 is fewer than 6, so there is no quorum."),
            PQ("On a vote, 33 members vote for, 19 against and 8 abstain. Simple majority of votes cast needed. Is the motion carried?",
               "Votes cast = 33 + 19 = 52. Half is 26. 33 is more than 26, so the motion is carried."),
            TIP("Notice, agenda, quorum, proxy, motion and resolution are all in the blueprint for this module. Expect Paper 1 definitions and, in Paper 2, "
                "drafting a notice and agenda. State general rules and say that the exact figures depend on the organisation. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("A valid meeting is properly called, properly notified, has an agenda and a quorum, is chaired and follows the rules.",
                "Notice states the kind of meeting, date, time, place and business; the agenda lists the business in order, ending with any other business.",
                "A quorum is the minimum present; a proxy votes for an absent member; a motion becomes a resolution when passed.",
                "A simple majority is more than half of the votes cast. The chairperson may have a casting vote if the rules allow."),
        ],
    ),
    # ------------------------------------------------------------------ 12. The chairperson, the secretary and minutes
    lesson(
        module=M6, topic="The chairperson, the secretary and minutes",
        title="The chairperson, the secretary and writing minutes",
        slug="ofp2-chairperson-secretary-minutes",
        minutes=25,
        summary="The duties of the chairperson and the secretary before, during and after a meeting, and how to write clear minutes in correct layout from rough notes.",
        objectives=[
            "State the duties of the chairperson before, during and after a meeting",
            "State the duties of the secretary before, during and after a meeting",
            "Define minutes and list what they contain",
            "Write minutes from rough notes in the correct layout",
        ],
        key_concepts=["Chairperson", "Secretary", "Apologies", "Matters arising", "Minutes", "Minute book", "Action point"],
        blocks=[
            H("Introduction"),
            T("Two people decide whether a meeting is a success: the one who leads it and the one who records it. The "
              "**chairperson** controls the meeting and keeps order. The **secretary** prepares it and writes down what is decided. "
              "In a school club these might be the Form 5 class captain and the class secretary."),
            KEY("Duties of the chairperson",
                "The chairperson is the leader of the meeting and must be fair.",
                cards=[["Before", "Agrees the agenda with the secretary; makes sure notice has been given; reads the papers."],
                       ["During", "Opens the meeting on time; checks the quorum; follows the agenda; gives each member a fair chance to speak; keeps order; puts motions to the vote and announces results; uses the casting vote if the rules allow; closes the meeting."],
                       ["After", "Reads and signs the minutes as a true record; sees that decisions are carried out."]]),
            KEY("Duties of the secretary",
                "The secretary is the administrator and the memory of the meeting.",
                cards=[["Before", "Prepares and sends the notice and agenda; books the room; collects reports and papers; records apologies; makes copies for members."],
                       ["During", "Takes the attendance; assists the chairperson with the rules; takes notes of the discussion and of all decisions."],
                       ["After", "Writes the minutes soon after the meeting; has the chairperson check them; sends them out; files them in the minute book; follows up the decisions and answers letters."]]),
            T("A good chairperson is calm, fair, firm and knows the rules. A good secretary is accurate, careful, trusted, "
              "good at writing and able to keep secrets."),
            D("**Minutes** are the official written record of a meeting: who was present, what was discussed, and above all what was **decided**. "
              "The minutes of one meeting are read at the next meeting; if the members agree that they are correct, the chairperson signs them. "
              "They are kept in a **minute book** or file and are a legal record.", title="Minutes"),
            KEY("What minutes contain",
                "In this order, from top to bottom.",
                cards=[["Heading", "Name of the organisation; kind of meeting; date, time and place."],
                       ["Attendance", "Names of those present and of those who sent apologies."],
                       ["Previous minutes", "Read, approved and signed (or corrected)."],
                       ["Matters arising", "Business left over from the last meeting."],
                       ["Items on the agenda", "A numbered paragraph for each item, with the decision, and the name of the person who must act."],
                       ["Any other business and date of next meeting", "Record each matter raised and the date and time of the next meeting."],
                       ["Closing", "The time the meeting ended, then a space for the chairperson's signature and date."]]),
            T("**Style.** Write in the past tense and in the third person ('The Treasurer reported that...'), in plain, short sentences. "
              "Do not record who said what, jokes or arguments; do not give your own opinion. Number the items to match the agenda. "
              "There are two styles: **narrative minutes** (a short story of the discussion and the decision) and **resolution minutes** (the decisions only, "
              "recorded as 'It was resolved that...'). Which style a firm uses depends on its custom; check your textbook."),
            MISTAKE("Writing what everybody said",
                    "Minutes are not a transcript. Record the decision and, where needed, a very short reason. Never write 'Mr X was rude' or 'there was a long quarrel'."),
            CODE("""            GREEN VALLEY FARMERS' COOPERATIVE
   Minutes of the Annual General Meeting held in the Community
   Hall, Bamenda, on Saturday 14 March 2026 at 10.00 a.m.   (invented)

PRESENT:   Mr A. Tabi (Chairperson), Mrs B. Ngu (Treasurer),
           Mr N. Tabi (Secretary) and 37 members (list attached)
APOLOGIES: Mrs C. Fon, Mr D. Mbah

1. MINUTES OF THE LAST MEETING
   The minutes of the meeting held on 15 March 2025 were read,
   approved and signed by the Chairperson.

2. MATTERS ARISING
   There were no matters arising.

3. TREASURER'S REPORT
   The Treasurer presented the accounts for 2025. It was resolved
   that the accounts be adopted. Proposed: Mr E. Njoh.
   Seconded: Mrs F. Ako. Carried unanimously.

4. ELECTION OF OFFICERS
   Mr A. Tabi was re-elected Chairperson for one year.

5. ANY OTHER BUSINESS
   Mrs G. Tchoumi asked for a training day on storage of crops.
   The Secretary will find a date.                 Action: Secretary

6. DATE OF NEXT MEETING
   The next meeting will be on Saturday 13 March 2027.

There being no further business, the Chairperson closed the
meeting at 12.15 p.m.

Signed .............................  Chairperson     Date ...........""", "text", title="Model minutes (all names invented)"),
            EX("Worked example 1: from rough notes to a minute",
               intro="Secretary's rough note: 'Treasurer said fees too low. Long talk. Mr Njoh says raise by 2 000. Mrs Ako agrees. All yes except two. Chair says carried.' Write the minute.",
               steps=[
                   S("Find the decision", text="The fee was raised by FCFA 2 000 (carried by a large majority)."),
                   S("Find proposer and seconder", text="Mr Njoh proposed and Mrs Ako seconded."),
                   S("Write in the past tense", text="'The Treasurer reported that the fees were too low. It was resolved that the annual fee be raised by FCFA 2 000. Proposed: Mr Njoh. Seconded: Mrs Ako. Carried (two against).'"),
                   S("Leave out", text="'Long talk' and similar remarks are not recorded."),
               ]),
            EX("Worked example 2: matters arising and action",
               intro="At the last meeting the Secretary was asked to write to the Council about the market stalls. At this meeting she reports that the letter was sent on 2 February 2026 and no reply has come. Record it.",
               steps=[
                   S("Put it under matters arising", text="Because it comes from the last meeting."),
                   S("Write the minute", text="'The Secretary reported that the letter to the Council had been sent on 2 February 2026 and that no reply had been received.'"),
                   S("Add the action", text="'The Secretary will write a reminder.   Action: Secretary.'"),
               ]),
            EX("Worked example 3: check an attendance count",
               intro="A meeting is attended by the Chairperson, the Secretary, the Treasurer and 37 members. The quorum is 20. Is the meeting valid? How many were present in all?",
               steps=[
                   S("Total present", text="3 officers + 37 members = 40 people."),
                   S("Compare with the quorum", text="40 is more than 20, so there is a quorum."),
                   S("Record", text="'40 members were present. A quorum was present.'"),
               ]),
            QUIZ("Who is responsible for taking notes and writing the minutes?",
                 ["The secretary", "The chairperson", "The treasurer", "The auditor"], 0,
                 "The secretary records what is decided and writes the minutes, which the chairperson signs.",
                 hint="Who is the administrator of the meeting?",
                 feedback=["", "The chairperson leads and signs, but the secretary writes.", "The treasurer deals with money.", "The auditor checks accounts."]),
            QUIZ("Which sentence is correct in the style of minutes?",
                 ["It was resolved that the fee be raised by FCFA 2 000.", "Mr Njoh shouted that the fee must go up!", "We all had a long argument.", "I think the fee is too low."], 0,
                 "Minutes use the past tense, the third person and plain facts; they do not record emotion or personal opinion.",
                 hint="Look for the formal, impersonal sentence.",
                 feedback=["", "This records emotion.", "This is not a decision.", "This is a personal opinion in the first person."]),
            PQ("State four duties of a chairperson during a meeting.",
               "Open the meeting on time; check the quorum; follow the agenda; keep order and give fair chances to speak; put motions to the vote and announce results; use the casting vote if allowed; close the meeting. (Any four.)"),
            PQ("State four duties of a secretary before a meeting.",
               "Prepare and send the notice and agenda; book the room; collect reports and papers; record apologies; prepare copies of papers for members. (Any four.)"),
            PQ("What are minutes, and why are they important?",
               "Minutes are the official written record of a meeting: who attended, what was discussed and what was decided. They are important because they prove what was agreed, remind people of their tasks and are a legal record."),
            PQ("Name five items that normally appear in the minutes of a meeting.",
               "Name of the organisation, date, time and place; those present; apologies; reading and approval of the last minutes; decisions on each agenda item; any other business; date of next meeting; time of closing; signature of the chairperson. (Any five.)"),
            TIP("Minutes are a classic Paper 2 task: you are given rough notes and must write minutes in the correct layout. Number the items, use past tense, record decisions, leave out opinions, and end with the time of closing and the signature line. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("The chairperson leads the meeting fairly and keeps order; the secretary prepares the meeting and writes the minutes.",
                "Minutes are the official, signed record of a meeting. They are written in the past tense and the third person and record decisions, not arguments.",
                "Standard order: heading, attendance and apologies, previous minutes, matters arising, items, any other business, date of next meeting, closing, signature.",
                "Narrative and resolution styles exist; use the style of your textbook or firm."),
        ],
    ),
    # ------------------------------------------------------------------ 13. Business letters
    lesson(
        module=M6, topic="Business letters",
        title="Business letters: parts, layout and style",
        slug="ofp2-business-letters",
        minutes=25,
        summary="The parts of a business letter in their correct order, blocked and semi-blocked layouts, open punctuation, matching salutation and ending, and how to write a clear letter of enquiry or complaint.",
        objectives=[
            "Name the parts of a business letter in the correct order",
            "Describe blocked and semi-blocked layouts and open punctuation",
            "Match salutation with complimentary close correctly",
            "Draft a short business letter that is clear, courteous and complete",
        ],
        key_concepts=["Letterhead", "Reference", "Inside address", "Salutation", "Subject line", "Complimentary close", "Enclosure", "Blocked layout"],
        blocks=[
            H("Introduction"),
            T("A letter may be the only picture a customer has of your firm. A neat, correct letter makes the firm look careful and "
              "trustworthy. A letter with the wrong name or a missing date makes it look careless. Business letters follow a standard "
              "layout so that readers find the information quickly."),
            KEY("Parts of a business letter, from the top",
                "Learn the order. Names in brackets are used only when needed.",
                cards=[["1 Letterhead", "Printed at the top: name of the firm, address, telephone, email (and logo)."],
                       ["2 Reference", "Letters and numbers for filing, such as 'Our ref: SAL/14/26' and 'Your ref:'."],
                       ["3 Date", "Written in full: 14 May 2026."],
                       ["4 Inside address", "Name and address of the person or firm written to."],
                       ["5 Salutation", "'Dear Sir', 'Dear Madam', 'Dear Sir or Madam' or 'Dear Mr Tabi'."],
                       ["6 Subject line", "A short heading telling the reader what the letter is about, often in capitals."],
                       ["7 Body", "Opening paragraph (why you write), middle paragraphs (details), closing paragraph (what you want to happen next)."],
                       ["8 Complimentary close", "'Yours faithfully' or 'Yours sincerely'."],
                       ["9 Signature and name", "Space for the signature, then the typed name and job title."],
                       ["10 Enclosure and copies", "'Enc.' lists what is enclosed; 'cc' shows who else receives a copy."]]),
            T("Salutation and close must be matched. If you do not know the name of the person, you begin 'Dear Sir', 'Dear Madam' or 'Dear Sir or Madam' "
              "and end **Yours faithfully**. If you know the name and begin 'Dear Mr Tabi', you end **Yours sincerely**."),
            CODE("""MATCHING THE SALUTATION AND THE CLOSE
Dear Sir  /  Dear Madam  /  Dear Sir or Madam   ->  Yours faithfully
Dear Mr Tabi  /  Dear Mrs Ngu  /  Dear Ms Fon   ->  Yours sincerely""", "text", title="Salutation and close"),
            H("Layout and punctuation"),
            D("In the **blocked layout** every line starts at the left margin; there are no indents and a blank line separates paragraphs. In the "
              "**semi-blocked layout** the first line of each paragraph is indented. In the **indented** layout, now rare, each line of the inside address "
              "steps in. **Open punctuation** means no commas or full stops in the address, date, salutation and complimentary close (full stops are "
              "still used in sentences). **Closed punctuation** uses them. Blocked layout with open punctuation is the quickest and most common (check your textbook for its preferred style).",
              title="Layouts"),
            IMG("f5ofp2-blocked-letter.svg",
                alt="A diagram of a letter page in blocked layout with labelled blocks from top to bottom: letterhead, reference and date, inside address, salutation, subject line, three body paragraphs, complimentary close, signature and name, enclosure.",
                caption="Figure 1. A letter in blocked layout. All blocks start at the left margin."),
            CODE("""SAMA TRADERS LTD
P.O. Box 00, Douala     Tel: 000 000 000     Email: info@sama.example
(all names, numbers and addresses are invented)

Our ref: SAL/14/26
Your ref: ENQ/9

14 May 2026

The Sales Manager
Fotso Printing Ltd
P.O. Box 00
Bafoussam

Dear Sir or Madam

ENQUIRY FOR EXERCISE BOOKS

We are a bookshop in Douala and we plan to open a stall at the
start of the new school year.

Please send us your price list and terms for 96-page exercise
books in lots of 500 and 1 000. We would also like to know your
discount for cash payment and how long delivery to Douala takes.

We hope to place an order before the end of June and look forward
to your reply.

Yours faithfully

(signature)

J. Ako
Manager

Enc. Sample page of our current order form""", "text", title="A letter of enquiry in blocked layout, open punctuation"),
            T("**Style.** Be clear (one idea in each paragraph), concise (no wasted words), complete (all facts the reader needs: dates, "
              "quantities, prices), courteous (please, thank you) and correct (names, spelling, figures). Many textbooks list these as the 'five Cs' or 'seven Cs'; check your textbook for your list."),
            MISTAKE("Wrong ending for the salutation",
                    "Dear Sir ... Yours sincerely is wrong. If the greeting does not use a name, the ending is 'Yours faithfully'. Also avoid a capital letter for the second word: 'Yours faithfully', not 'Yours Faithfully'."),
            EX("Worked example 1: correct the pairing",
               intro="Correct this letter ending: 'Dear Madam ... Yours sincerely' and 'Dear Mr Tabi ... Yours faithfully'.",
               steps=[
                   S("Look at the salutation", text="'Dear Madam' has no name."),
                   S("First correction", text="Dear Madam ... Yours faithfully."),
                   S("Second", text="'Dear Mr Tabi' has a name, so: Dear Mr Tabi ... Yours sincerely."),
               ]),
            EX("Worked example 2: put the parts in order",
               intro="A clerk has typed these parts in the wrong order: signature and name; salutation; date; body; letterhead; inside address; complimentary close; subject line. Put them in order.",
               steps=[
                   S("Top of the page", text="Letterhead, date (and reference), inside address."),
                   S("Greeting and subject", text="Salutation, subject line."),
                   S("Message and ending", text="Body, complimentary close, signature and name."),
                   S("Final order", text="Letterhead; date; inside address; salutation; subject line; body; complimentary close; signature and name."),
               ]),
            EX("Worked example 3: plan a letter of complaint",
               intro="You ordered 500 exercise books on 2 May 2026 and received 450. Plan the three body paragraphs.",
               steps=[
                   S("Opening paragraph", text="State the order: 500 exercise books, order dated 2 May 2026, delivered on 12 May."),
                   S("Middle paragraph", text="State the problem: only 450 arrived, 50 short. Mention the delivery note number."),
                   S("Closing paragraph", text="Say what you want: send the 50 missing books within seven days or reduce the invoice (500 - 450 = 50 books)."),
               ]),
            QUIZ("A letter begins 'Dear Sir or Madam'. How should it end?",
                 ["Yours faithfully", "Yours sincerely", "Yours truly and love", "With regards, your friend"], 0,
                 "Without a name in the salutation, the usual close is Yours faithfully.",
                 hint="The greeting has no name.",
                 feedback=["", "Yours sincerely is used with a name.", "This is not business style.", "This is not business style."]),
            QUIZ("In a blocked layout with open punctuation,",
                 ["every line begins at the left margin and the address has no commas at line ends", "paragraphs are indented 2 cm", "the address is written on the right", "all words are capitals"], 0,
                 "Blocked: everything at the left margin. Open punctuation: no commas or full stops in the address, date, salutation or close.",
                 hint="Block = one solid block at the left.",
                 feedback=["", "That is semi-blocked.", "The inside address is at the left.", "Capitals are not required."]),
            PQ("List in order the parts of a business letter from the top of the page to the signature.",
               "Letterhead; reference; date; inside address; salutation; subject line; body; complimentary close; signature and typed name (then enclosure and copies)."),
            PQ("Explain how Yours faithfully differs from Yours sincerely.",
               "Yours faithfully is used when the letter begins with Dear Sir, Dear Madam or Dear Sir or Madam (no name). Yours sincerely is used when the letter begins with the person's name, for example Dear Mr Tabi."),
            PQ("What does 'Enc.' at the bottom of a letter mean, and why is it used?",
               "It means enclosure: something is enclosed with the letter, such as an invoice or a brochure. It reminds the writer to include it and tells the reader to look for it."),
            PQ("State three qualities of a good business letter.",
               "Clear, concise, complete, courteous and correct. (Any three; your textbook may use different words for the same ideas.)"),
            TIP("Layout of letters is often tested in Paper 2 (draft a letter from given facts) and in Paper 1 (parts and matching salutations). Use a blocked layout with open punctuation, show every part, and invent no facts that the question does not give. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("A business letter has: letterhead, reference, date, inside address, salutation, subject line, body, complimentary close, signature and name, enclosure and copies.",
                "Dear Sir, Dear Madam or Dear Sir or Madam goes with Yours faithfully. Dear Mr Tabi goes with Yours sincerely.",
                "Blocked layout puts every line at the left margin. Open punctuation leaves out commas and full stops in the address and greeting lines.",
                "A good letter is clear, concise, complete, courteous and correct."),
        ],
    ),
    # ------------------------------------------------------------------ 14. Memorandums, circulars and reports
    lesson(
        module=M6, topic="Memorandums, circulars and reports",
        title="Memorandums, circulars and reports",
        slug="ofp2-memos-circulars-reports",
        minutes=25,
        summary="The layout and uses of an internal memorandum, a circular sent to many people, and a short formal report with terms of reference, findings, conclusions and recommendations.",
        objectives=[
            "Distinguish a memorandum, a circular and a report",
            "Lay out a memorandum correctly",
            "Draft a circular for many recipients",
            "Plan and write a short formal report with recommendations",
        ],
        key_concepts=["Memorandum", "Circular", "Report", "Terms of reference", "Findings", "Conclusions", "Recommendations"],
        blocks=[
            H("Introduction"),
            T("A manager in a Limbe factory needs to tell department heads that Friday's meeting is moved. A shop owner wants to "
              "tell 300 customers about a new opening time. A committee must give the board a written account of three quotations. "
              "Each needs a different document: a **memorandum**, a **circular** and a **report**."),
            KEY("Three documents compared",
                "Choose by who the readers are and what the message is.",
                cards=[["Memorandum", "A short written message sent inside an organisation, between people or departments. No salutation or complimentary close."],
                       ["Circular", "One message sent to many people at the same time, inside or outside the organisation. Copied or printed, with the name of the receiver left general."],
                       ["Report", "A structured account of facts and findings on a subject, usually with conclusions and recommendations, for someone who must decide."]]),
            H("The memorandum"),
            D("A **memorandum** (memo, plural memos or memoranda) is a short written communication used **within** an organisation. "
              "It is quick, informal in tone and leaves a written record. It has a heading with the fields TO, FROM, DATE, REFERENCE and SUBJECT.", title="Memorandum"),
            CODE("""                         SAMA TRADERS LTD
                          MEMORANDUM
                (all names and details are invented)

TO:        All Department Heads
FROM:      Managing Director
DATE:      14 May 2026
REF:       MD/05/26
SUBJECT:   CHANGE OF DATE FOR THE MONTHLY MEETING

The monthly meeting of department heads will now be held on
Friday 22 May 2026 at 9.00 a.m. in the Board Room, not on
Friday 15 May as planned.

Please bring your sales reports for April and send your
apologies to the Secretary if you cannot attend.

                                                    J.A.
Enc. Revised agenda""", "text", title="A memorandum"),
            T("A memo has **no salutation** (no 'Dear...') and **no complimentary close** (no 'Yours...'). The writer usually **initials** it "
              "instead of signing in full. Its language is short and direct. A memo is for internal use only; a letter is for outsiders."),
            H("The circular"),
            D("A **circular** is a message that is sent to a **large number of people** at the same time. The text is the same for everybody, so it "
              "is copied or printed. It may be sent to staff, customers, members or suppliers.", title="Circular"),
            CODE("""                  GREEN VALLEY STORES
          P.O. Box 00, Bafoussam      (invented)

14 May 2026

Dear Customer

NEW OPENING HOURS

From Monday 1 June 2026 the store will open from 7.30 a.m.
to 6.30 p.m. from Monday to Saturday. It will be closed on
Sundays.

We thank you for your custom and look forward to serving you.

Yours faithfully

(signature)
R. Njoh
Manager""", "text", title="A circular to customers"),
            T("**Advantages of circulars:** cheap and fast for large numbers; everybody gets the same message; it leaves a copy for the files. "
              "**Disadvantages:** impersonal; some people do not read it; it cannot answer questions."),
            KEY("Memo or circular?",
                "The difference is mostly about readers.",
                cards=[["Memo", "To a person or department inside the firm. TO, FROM, DATE, SUBJECT. No salutation, no close."],
                       ["Circular", "To many people, often outside as well. Dear Customer / Dear Member / Dear Staff. It has a salutation and a close."]]),
            H("The report"),
            D("A **report** is a written account of an investigation or event, giving facts, conclusions and, where asked, "
              "recommendations. It is written for a person or body that needs to take a decision.", title="Report"),
            T("A short formal report usually has these headings. Some books use slightly different words, so check your textbook."),
            CODE("""REPORT ON THE PURCHASE OF A PHOTOCOPIER
Submitted to: The Managing Director      By: The Purchasing Committee
Date: 14 May 2026                                          (invented)

1  TERMS OF REFERENCE
   To find the best photocopier for the Accounts office and to
   report by 14 May 2026.

2  PROCEDURE
   Three suppliers were asked for quotations. Each machine was
   tested and staff were interviewed.

3  FINDINGS
   Supplier A: FCFA 450 000, slow, cheap toner
   Supplier B: FCFA 480 000, fast, dear toner
   Supplier C: FCFA 435 000, fast, cheap toner, 2-year guarantee

4  CONCLUSIONS
   Supplier C is the cheapest and combines speed with low running costs.

5  RECOMMENDATIONS
   That a machine be bought from Supplier C.

(signed) .................. Chairperson        Date ...........""", "text", title="A short formal report (invented)"),
            KEY("Report headings explained",
                "Keep each part separate.",
                cards=[["Terms of reference", "What the writer was asked to do, for whom and by when."],
                       ["Procedure", "How the facts were collected: interviews, tests, records."],
                       ["Findings", "The facts discovered, not opinions."],
                       ["Conclusions", "What the findings mean."],
                       ["Recommendations", "What the writer advises should be done."]]),
            MISTAKE("Mixing findings with recommendations",
                    "Findings are facts. Conclusions are what the facts mean. Recommendations are what should be done. Writing 'we should buy C' in the findings section confuses the reader."),
            EX("Worked example 1: memo or letter?",
               intro="Which document? (a) A note from the Accounts Manager to the Personnel Manager asking for staff leave records. (b) A note to a supplier in Douala asking for prices.",
               steps=[
                   S("(a) Both people work in the same firm", text="Memorandum."),
                   S("(b) The supplier is outside the firm", text="Business letter, not a memo."),
               ]),
            EX("Worked example 2: prepare a circular",
               intro="A school (invented) will close on Friday 3 July 2026 for the holidays and reopen on Monday 7 September 2026. Plan a circular to parents.",
               steps=[
                   S("Heading", text="School letterhead, date, 'Dear Parent or Guardian'."),
                   S("Subject", text="SCHOOL HOLIDAYS."),
                   S("Body", text="Say that school closes on Friday 3 July 2026 and reopens on Monday 7 September 2026; mention fee reminders if needed."),
                   S("Ending", text="Yours faithfully, signature, name and title of the Principal."),
               ]),
            EX("Worked example 3: use figures in a report",
               intro="In the report above, how much cheaper is Supplier C than Supplier A and Supplier B?",
               steps=[
                   S("C against A", text="450 000 - 435 000 = FCFA 15 000."),
                   S("C against B", text="480 000 - 435 000 = FCFA 45 000."),
                   S("Use", text="These differences support the conclusion that C is the cheapest."),
               ]),
            QUIZ("Which document has no salutation and no complimentary close?",
                 ["Memorandum", "Business letter", "Circular", "Letter of complaint"], 0,
                 "A memo goes to people inside the firm, so it begins with TO and FROM and has no 'Dear'.",
                 hint="Think of the heading TO, FROM, DATE.",
                 feedback=["", "A business letter has both.", "A circular usually has a salutation (Dear Customer).", "A letter of complaint is a business letter."]),
            QUIZ("In a formal report, the part that tells the reader what to do is the",
                 ["recommendations", "findings", "procedure", "terms of reference"], 0,
                 "Recommendations are the writer's advice for action.",
                 hint="Which heading begins with advice?",
                 feedback=["", "Findings are facts.", "Procedure tells how the facts were collected.", "Terms of reference tell what the writer was asked to do."]),
            PQ("Distinguish between a memorandum and a circular.",
               "A memo is a short message inside an organisation to a particular person or department; it has no salutation or close. A circular is one message copied and sent to many people, inside or outside, and it has a general salutation such as 'Dear Customer'."),
            PQ("List the headings of a short formal report in order.",
               "Terms of reference; procedure; findings; conclusions; recommendations (with the title, who it is to and from, date and signature)."),
            PQ("State two advantages and one disadvantage of a circular.",
               "Advantages: cheap and fast for large numbers; the same message for all; a copy kept. Disadvantage: impersonal and cannot answer individual questions."),
            PQ("Three quotations for a printer are FCFA 180 000, FCFA 165 000 and FCFA 172 000 (invented). Which is the cheapest and by how much is it cheaper than the dearest?",
               "The cheapest is FCFA 165 000. The dearest is FCFA 180 000. The difference is 180 000 - 165 000 = FCFA 15 000."),
            TIP("Memos, circulars and reports are common Paper 2 drafting tasks. Use the correct headings, keep the language simple, and use only the facts given in the question. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("A memo is an internal note with TO, FROM, DATE and SUBJECT, and no salutation or close.",
                "A circular is one message sent to many people at once; it has a general salutation such as Dear Customer.",
                "A formal report has terms of reference, procedure, findings, conclusions and recommendations.",
                "Findings are facts, conclusions are meanings, recommendations are advice."),
        ],
    ),
    # ------------------------------------------------------------------ 15. Paper 1
    lesson(
        module=M_EXAM, topic="Paper 1",
        title="Paper 1: multiple-choice strategies",
        slug="ofp2-exam-paper-1-strategies",
        minutes=22,
        summary="How to approach the 50-question multiple-choice paper in Office Practice: planning time, reading stems, eliminating options, avoiding look-alike terms, and checking calculations and orders.",
        objectives=[
            "Describe Paper 1 as set out in the blueprint and say what to check with your teacher",
            "Use a two-pass method and a time plan for 50 questions",
            "Read stems carefully, especially NOT, EXCEPT and BEST",
            "Avoid the most common confusions between similar office terms",
        ],
        key_concepts=["Paper 1", "Stem and options", "Elimination", "Two-pass method", "Look-alike terms", "Time plan"],
        blocks=[
            H("Introduction"),
            T("Fifty questions are waiting. One asks you to order file numbers. The next asks what a quorum is. The next asks which "
              "document has no salutation. You know the content, but a hurried reader loses marks to words like **NOT** and **BEST**. "
              "This lesson is about answering well."),
            D("KKEVO's curriculum blueprint lists **Paper 1** for Office Practice as **50 multiple-choice questions**, and **Paper 2** as a written paper on a "
              "case study and administrative procedures. Office Practice is not covered in the Board's 2023 report that we use for other subjects, so **check the exact paper format "
              "with your teacher** (number of questions, time allowed, whether wrong answers lose marks, and which modules are tested).", title="What we know"),
            TIP("The syllabus covers office organisation, reception and telecommunications, mail, filing and records, reprography and automation, and meetings and correspondence. "
                "Expect questions from every module, so revise all of them. The practice settings in this course are KKEVO's own."),
            H("Time"),
            T("If the blueprint's time of about 90 minutes is right for your paper (check), then 90 / 50 = **1.8 minutes** for each question. "
              "A definition takes 20 seconds; an ordering or calculation takes two or three minutes. Keep to the average and never get stuck."),
            IMG("f5ofp2-exam-timeplan.svg",
                alt="A bar showing 90 minutes: pass 1 up to 55 minutes, pass 2 from 55 to 80 minutes, final check from 80 to 90 minutes.",
                caption="Figure 1. A suggested plan for 90 minutes (KKEVO study advice, not an official rule)."),
            KEY("The two-pass method",
                "Collect the easy marks first.",
                cards=[["Pass 1", "Answer every question you can answer in about a minute. Mark the others lightly and move on."],
                       ["Pass 2", "Return to the marked questions. Use elimination and calculation."],
                       ["Check", "Make sure every question has an answer. Re-read questions with NOT, EXCEPT or ONLY."]]),
            H("Reading the stem and choosing the key"),
            D("The **stem** is the question part. The **key** is the correct option. The **distractors** are the wrong options; each is built from a "
              "common misunderstanding. Read the stem twice, then cross out options that cannot be right.", title="Stem, key, distractors"),
            KEY("Words that change the answer",
                "Circle them in the question paper if you may.",
                cards=[["NOT / EXCEPT", "Find the one false or odd option. Check each option as true or false."],
                       ["BEST / MOST LIKELY", "Several options may be possible. Choose the one that fits all the facts given."],
                       ["FIRST / LAST", "The question is about order. Write the steps in your head."],
                       ["ONLY / ALWAYS / NEVER", "These words are very strong. An option with 'always' is often too strong."]]),
            H("Look-alike terms"),
            T("Many wrong answers come from mixing similar terms. Revise these pairs until you can say the difference at once."),
            CODE("""LOOK-ALIKE PAIRS
Centralized filing        one registry for the whole firm
Decentralized filing      each department keeps its own files
Out-guide                 stands in for a removed file
Guide card                divides a drawer into sections
Cross-reference           note pointing to where a paper is filed
Index                     list showing where each file is kept
Copying                   few copies from the original (photocopier)
Duplicating               many copies from a master (stencil, plate)
Collating                 putting pages in order
Binding                   fastening the sets together
AGM                       all members, once a year
EGM                       all members, urgent business
Motion                    a proposal
Resolution                a motion that has been passed
Quorum                    minimum number present
Proxy                     person who votes for an absent member
Memorandum                internal message, no salutation
Circular                  one message to many people
Yours faithfully          after Dear Sir / Dear Madam
Yours sincerely           after Dear Mr Tabi (a name)""", "text", title="Look-alike terms"),
            EX("Worked example 1: a NOT question",
               intro="Which of the following is NOT a feature of a good filing system? A simple B easy to expand C complicated to use D safe and confidential",
               steps=[
                   S("Mark each option true or false as a feature", text="A true. B true. C false. D true."),
                   S("Choose", text="C is not a feature of a good system, so C is the key."),
               ]),
            EX("Worked example 2: an ordering question",
               intro="File numbers 305, 52, 1 004, 98 are filed numerically, smallest first. Which number comes third?",
               steps=[
                   S("Order by size", text="52, 98, 305, 1 004."),
                   S("Third", text="305."),
                   S("Warning", text="If you sorted as words you would put 1 004 first. Compare numbers by size."),
               ]),
            EX("Worked example 3: a calculation",
               intro="A cost question: a duplicator costs FCFA 3 000 for a master plus FCFA 4 a copy (invented). What do 250 copies cost?",
               steps=[
                   S("Copies", text="4 x 250 = 1 000."),
                   S("Add master", text="3 000 + 1 000 = FCFA 4 000."),
               ]),
            MISTAKE("Choosing the option that sounds important",
                    "A long, official-sounding option is not always right. Check it against the stem. Ask: does this option answer exactly what was asked?"),
            QUIZ("A question has 50 items for 90 minutes. What is the average time for each?",
                 ["1.8 minutes", "2.8 minutes", "0.9 minutes", "5 minutes"], 0,
                 "90 / 50 = 1.8 minutes.",
                 hint="Divide time by number of questions.",
                 feedback=["", "This is too long: 50 x 2.8 is 140.", "This would be 45 minutes for 50 questions.", "This would take 250 minutes."]),
            QUIZ("Which option is the best strategy for a question you cannot answer in two minutes?",
                 ["Mark it, move on, and return in the second pass", "Spend ten minutes on it", "Leave it blank for ever", "Copy your neighbour"], 0,
                 "The two-pass method protects the time for easy marks and leaves time to return.",
                 hint="Do not let one question take the time of five.",
                 feedback=["", "That takes the time of five other questions.", "Always give an answer if wrong answers do not lose marks (check).", "Copying is cheating."]),
            PQ("State two facts about Paper 1 from the blueprint, and one fact you must check with your teacher.",
               "Paper 1 is 50 multiple-choice questions. It tests the office practice modules. You must check the exact paper format, for example time allowed and whether wrong answers lose marks."),
            PQ("Explain the two-pass method in two sentences.",
               "In the first pass answer all the questions you can do quickly and mark the hard ones. In the second pass return to the hard ones with the time that is left, and use the last minutes to check."),
            PQ("Write the difference between a motion and a resolution, and between a memo and a circular.",
               "A motion is a proposal; a resolution is a motion that has been passed. A memo is an internal message to a person or department; a circular is one message sent to many people."),
            PQ("You have done 38 of 50 questions in 55 minutes of a 90-minute paper. How many minutes remain and how many questions are left?",
               "90 - 55 = 35 minutes remain and 50 - 38 = 12 questions are left."),
            TIP("Revise by module using the practice sets, then take the Paper 1 mock under timed conditions. Review every wrong answer and read why the distractor was wrong.", title="Exam link"),
            SUM("Paper 1 is 50 multiple-choice questions (blueprint). Check the exact format with your teacher.",
                "Plan your time (about 1.8 minutes a question if the time is 90 minutes). Use two passes and check at the end.",
                "Read NOT, EXCEPT, BEST and FIRST carefully. Eliminate wrong options and test the last two against the stem.",
                "Learn look-alike pairs and always compare numbers by size, not as words."),
        ],
    ),
    # ------------------------------------------------------------------ 16. Paper 2
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2: case studies and administrative procedures",
        slug="ofp2-exam-paper-2-case-studies",
        minutes=25,
        summary="How to read a case study, understand command words, put procedures in the right order, draft documents from given facts, and plan written answers for the Paper 2 style of question.",
        objectives=[
            "Describe Paper 2 as set out in the blueprint and say what to check with your teacher",
            "Read a case study and pick out the facts, the role and the task",
            "Respond correctly to command words such as list, explain, advise and draft",
            "Put an office procedure in the correct order and draft a short document from given facts",
        ],
        key_concepts=["Paper 2", "Case study", "Command word", "Administrative procedure", "Answer plan", "Drafting"],
        blocks=[
            H("Introduction"),
            T("In Paper 1 you choose an answer. In Paper 2 you **write** and **decide**. The blueprint lists Paper 2 as a written paper on a **case study** "
              "and **administrative procedures**. It carries more of the total marks than Paper 1. Check the exact format, the number of questions and the "
              "time allowed with your teacher; this lesson teaches the skills that fit any such paper."),
            KEY("What a case study paper tests",
                "These are the skills, not the Board's marking scheme (which we do not have).",
                cards=[["Knowledge", "You know the terms: filing methods, meeting documents, copying methods."],
                       ["Application", "You use them on the facts of the case, not on general knowledge only."],
                       ["Procedure", "You know the steps of an office routine and their correct order."],
                       ["Drafting", "You can lay out a notice, agenda, minutes, memo, circular or letter correctly from facts given."],
                       ["Judgement", "You advise: what should the office do, and why?"]]),
            H("Command words"),
            CODE("""COMMAND WORD   WHAT TO DO
State / Name   give the fact in a few words
List           give separate items, one under another
Define         give the exact meaning
Describe       say what it is or how it is done, step by step
Explain        give the reasons: say WHY or HOW
Distinguish    give the difference between two things
Advise         say what the office should do, with a reason
Compare        give similarities and differences
Draft          write the document in correct layout, using the facts given
Calculate      show the working and the unit""", "text", title="Command words"),
            MISTAKE("Writing everything you know",
                    "A long answer on 'filing' does not help if the question asked you to 'advise on a filing method for this firm'. Read the command word and use the facts in the case."),
            H("Reading the case study"),
            T("Read the case twice. First, find the **role** you are playing (for example, office assistant to the manager). "
              "Second, underline the **facts** (names, numbers, dates, problems). Third, read the questions and write the key word of each beside the matching fact."),
            CODE("""CASE STUDY (all names and figures invented)
You are the office assistant at MUKETE AND SONS TRADING LTD, Kumba.
The firm has 25 staff and keeps 400 customer files in heaps on a table.
Customers phone and ask for their invoices by name. Files go missing.
The manager wants (a) a better filing system, (b) a notice and agenda
for the staff savings society meeting on Saturday 6 June 2026 at
10.00 a.m. in the canteen, and (c) a circular to customers about a
new price list.""", "text", title="Part of a case study"),
            EX("Worked example 1: advise on filing",
               intro="Using the case above, advise the manager on a filing method for the 400 customer files. Give reasons.",
               steps=[
                   S("Pick the facts", text="400 customer files; customers ask by NAME; files go missing."),
                   S("Choose the method", text="Alphabetical filing by customer surname or business name, because staff are asked by name and the system is simple."),
                   S("Add support", text="Use folders, guide cards and labelled drawers; an out-guide for files taken out; one person responsible for the registry; file papers daily."),
                   S("Conclude", text="The advice is based on the facts (name requests, missing files) and gives reasons."),
               ]),
            H("Procedures: put the steps in order"),
            T("A procedure is a routine in the right order. Questions may ask you to list or arrange the steps. Learn each procedure as a story with a "
              "beginning and an end."),
            CODE("""ARRANGING A MEETING (one common order; check your textbook)
1  Decide the purpose, date, time and place
2  Book the room and prepare the agenda with the chairperson
3  Send the notice and agenda to members
4  Prepare papers and check the room and equipment
5  Hold the meeting (quorum, minutes of last meeting, business)
6  Write the minutes and have the chairperson check them
7  Send the minutes, file them, follow up the decisions

FILING A PAPER (one common order)
1  Check that the paper is released for filing (initial or stamp)
2  Read it and choose the file name or number
3  Make any cross-reference or index card
4  Sort the papers by file
5  Place each paper in its folder, newest in front
6  Remove any out-guide""", "text", title="Two procedures in order"),
            EX("Worked example 2: draft a notice from the case",
               intro="Draft the notice of the staff savings society meeting in the case study above. The Secretary is Mr A. Tabi (invented). The notice is dated 20 May 2026.",
               steps=[
                   S("Heading", text="Name of the society, the word NOTICE OF MEETING."),
                   S("Details", text="Kind of meeting; Saturday 6 June 2026; 10.00 a.m.; the canteen of Mukete and Sons Trading Ltd, Kumba."),
                   S("Extras", text="Say that the agenda is attached; mention proxies only if the case says they are allowed."),
                   S("Closing", text="'By order of the Committee.' Signature, Mr A. Tabi, Secretary, date of notice 20 May 2026."),
               ]),
            EX("Worked example 3: calculate and recommend",
               intro="The manager asks you to compare two ways of making 600 copies of the price list. A photocopier costs FCFA 25 a copy. A duplicator needs a master costing FCFA 1 500 plus FCFA 5 a copy (invented figures). Advise the manager.",
               steps=[
                   S("Photocopier", text="25 x 600 = FCFA 15 000."),
                   S("Duplicator", text="1 500 + 5 x 600 = 1 500 + 3 000 = FCFA 4 500."),
                   S("Difference", text="15 000 - 4 500 = FCFA 10 500 cheaper."),
                   S("Advise", text="Use the duplicator for 600 copies. Say that the photocopier would be better for a few copies."),
               ]),
            H("Planning your answers"),
            KEY("A simple answer plan",
                "Use it for every question that needs writing.",
                cards=[["Read", "Command word, topic, marks (more marks mean more points)."],
                       ["Plan", "Jot down the points in the margin in the order you will write them."],
                       ["Write", "Separate points with new lines or numbers. One point, one reason."],
                       ["Use the case", "Use names, numbers and facts from the case in the answer."],
                       ["Check", "Does it answer the command word? Is the layout of any document complete?"]]),
            QUIZ("A question says 'Advise the manager'. What must your answer include?",
                 ["A recommendation with a reason based on the case", "A long definition of every term in the topic", "A story about your own school", "Nothing but a list of words"], 0,
                 "Advice has two parts: what to do and why, using facts from the case.",
                 hint="What does 'advise' ask you to give?",
                 feedback=["", "A definition does not give advice.", "Your own school is not the case.", "A list of words does not give a reason."]),
            QUIZ("In arranging a meeting, which step comes first?",
                 ["Decide the purpose, date and place", "Write the minutes", "Send the minutes to members", "File the minutes"], 0,
                 "Planning comes before everything else.",
                 hint="Which step must happen before notice can be sent?",
                 feedback=["", "Minutes are written after the meeting.", "They are sent after they are written.", "They are filed last."]),
            PQ("List four command words and say what each asks you to do.",
               "State: give the fact. List: give separate items. Explain: give reasons. Advise: say what to do with a reason. Draft: write the document in correct layout. (Any four with the meaning.)"),
            PQ("Why is it important to use the facts of the case in your answer?",
               "Case-study questions test application. Marks are given for using the names, figures and problems in the case, not for general statements."),
            PQ("Put in order: send notice; hold the meeting; decide the date; write the minutes; prepare the agenda.",
               "Decide the date; prepare the agenda; send the notice; hold the meeting; write the minutes."),
            PQ("Using the figures in Worked example 3, find the cost of 100 copies by each method and say which is cheaper.",
               "Photocopier: 25 x 100 = FCFA 2 500. Duplicator: 1 500 + 5 x 100 = FCFA 2 000. The duplicator is cheaper by FCFA 500."),
            TIP("In Paper 2 write numbered points, show your working in calculations, and keep documents in their correct layout. Do not invent facts that the case does not give. Check the exact paper format with your teacher.", title="Exam link"),
            SUM("Paper 2 (blueprint): a written paper on a case study and administrative procedures. Check the exact format with your teacher.",
                "Read the case twice: role, facts, task. Respond to the command word. Use the facts of the case.",
                "Learn procedures as ordered steps (arranging a meeting, filing a paper) and drafts as layouts (notice, agenda, minutes, memo, circular, letter, report).",
                "Plan, write in separate points, show calculations, and check the answer against the question."),
        ],
    ),
]
