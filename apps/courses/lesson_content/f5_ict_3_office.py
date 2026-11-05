"""Form 5 ICT: Practical skills / Office productivity (6 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "form-5")

MODULE = "Practical skills"
OFFICE = "Office productivity"

LESSONS = []

# ------------------------------------------------------------------ 1. Formatting text and paragraphs
LESSONS.append(lesson(
    module=MODULE, topic=OFFICE,
    title="Word processing: formatting text and paragraphs",
    slug="wordproc-formatting-text-paragraphs",
    minutes=20,
    summary="Format characters and paragraphs (font, size, alignment, spacing, bullets, numbering) and use heading styles so a document stays consistent and easy to change.",
    objectives=[
        "Change the font, size, colour and emphasis of selected text",
        "Set alignment, line spacing and spacing between paragraphs",
        "Create bulleted and numbered lists",
        "Explain why styles are better than formatting every line by hand",
    ],
    key_concepts=["Word processor", "Character formatting", "Paragraph formatting", "Alignment", "Line spacing",
                  "Bullets and numbering", "Style"],
    blocks=[
        H("Introduction"),
        T("The editor of a school newsletter in Bafoussam has typed all the articles. The page looks like a long grey "
          "wall of letters. Headings look the same as ordinary text. Nobody wants to read it."),
        T("A **word processor** is a program for writing and designing documents. Microsoft Word, LibreOffice Writer "
          "and Google Docs are examples. Their menus have different names, but the features are the same. In this "
          "lesson you learn the features that make a document clear: character formatting, paragraph formatting and styles."),
        H("Formatting characters"),
        D("**Character formatting** changes how selected letters look. You must first **select** the text, then apply "
          "the change. The main settings are the **font** (the design of the letters, such as Arial or Times New "
          "Roman), the **font size** (measured in points), the **colour**, and emphasis such as **bold**, italic and "
          "underline.", title="Character formatting"),
        T("Where is the command? In most programs it is on the Home tab or in a toolbar at the top. If you cannot "
          "find it, look for a button showing a letter A or the words Bold, Italic or Font."),
        H("Formatting paragraphs"),
        D("**Paragraph formatting** changes a whole paragraph at once. You do not have to select all of it: place the "
          "cursor anywhere inside the paragraph. A new paragraph begins each time you press Enter.",
          title="Paragraph formatting"),
        KEY("Four alignments", "Alignment decides how the lines sit between the left and right margins.",
            cards=[["Left", "Lines start at the left margin. Easiest to read; the usual choice for body text."],
                   ["Centre", "Lines are in the middle. Good for titles."],
                   ["Right", "Lines end at the right margin. Used for dates or addresses."],
                   ["Justify", "Both edges are straight, like a newspaper column. Spaces between words are stretched."]]),
        T("**Line spacing** is the space between lines inside a paragraph. Single spacing (1.0) is compact; 1.5 or "
          "double (2.0) leaves room for reading and for teachers' comments. **Paragraph spacing** is the extra space "
          "before or after a paragraph. Use paragraph spacing to separate paragraphs. Do not press Enter twice to "
          "make a gap, because the empty lines are extra paragraphs that you must delete later."),
        T("A **bulleted list** shows items with dots or small symbols. Use it when the order does not matter, for "
          "example things to bring on a school trip. A **numbered list** shows 1, 2, 3 and so on. Use it when the "
          "order matters, such as the steps to log in to a computer. To make a list, type the items on separate lines, "
          "select them, and click the bullets or numbering button."),
        H("Styles"),
        D("A **style** is a saved set of formatting with a name, such as Heading 1, Heading 2 or Normal. When you "
          "apply a style to a paragraph, all its settings (font, size, colour, spacing) are applied together.",
          title="Style"),
        KEY("Why styles beat manual formatting", "Manual formatting means selecting each heading and changing it by hand.",
            cards=[["Consistency", "Every Heading 1 looks the same. By hand, you may forget one or choose a slightly different size."],
                   ["Speed", "One click applies several settings. Change the style once and every heading updates."],
                   ["Structure", "The program knows which lines are headings. It can then build a table of contents and a navigation pane."]]),
        EX("Worked example 1: format the newsletter title and headings", intro=(
            "The newsletter has a title, three article headings and body text. Make the title stand out and give the "
            "article headings a consistent look."), steps=[
            S("Style the title", text="Select the title line and apply the Title style (or Heading 1). Centre it."),
            S("Style the article headings", text="Select the first article heading and apply the Heading 2 style. Repeat for the other two headings."),
            S("Style the body text", text="Make sure the article text uses the Normal style, in an 11 or 12 point font, aligned left."),
            S("Check", text="All three headings look identical, and the document structure is clear."),
        ]),
        EX("Worked example 2: lists and spacing", intro=(
            "The newsletter lists school events and the steps to enter the writing competition. Format both lists "
            "correctly and make the text easier to read."), steps=[
            S("Decide the list type", text="The events can be in any order, so use bullets. The competition steps must be followed in order, so use numbering."),
            S("Apply the lists", text="Select the event lines and click Bullets. Select the step lines and click Numbering."),
            S("Add breathing space", text="Select the body paragraphs and set line spacing to 1.15 or 1.5, and about 6 points after each paragraph."),
            S("Remove blank lines", text="Delete any empty paragraphs made by pressing Enter twice. Spacing now comes from the paragraph setting."),
        ]),
        EX("Worked example 3: change every heading at once", intro=(
            "The head teacher says all article headings must be dark blue and 14 points instead of black and 13 points. "
            "The newsletter has 12 article headings. How do you do it quickly?"), steps=[
            S("Why it is fast", text="All 12 headings use the Heading 2 style."),
            S("Edit the style", text="Open the Heading 2 style (right-click it in the styles list and choose Modify or Edit)."),
            S("Change the settings", text="Set the colour to dark blue and the size to 14 points, then confirm."),
            S("Result", text="All 12 headings change at once. With manual formatting you would have to change 12 headings one by one and might miss some."),
        ]),
        H("Common mistakes"),
        MISTAKE("Making headings by hand", "Selecting a line and making it bold and bigger looks like a heading, but the "
                "program does not know it is one. Apply a heading style instead."),
        MISTAKE("Pressing Enter to make space", "Extra empty paragraphs create gaps that break when the text changes. Use "
                "paragraph spacing."),
        MISTAKE("Using the space bar to line things up", "Rows of spaces look right on your screen and wrong on another "
                "printer. Use alignment, indents or a table."),
        QUIZ("You press Enter four times to move a paragraph down the page. What is the better method?",
             ["Press the space bar many times", "Set the paragraph spacing before the paragraph", "Make the text bold", "Change the font"], 1,
             "Spacing before or after a paragraph is a setting, so it stays correct if the text changes.",
             hint="Which feature controls the gap around a paragraph?",
             feedback=["Spaces move text sideways, not down, and they print unpredictably.", "",
                       "Bold changes the look of letters, not the gap.", "A font changes the letter design only."]),
        QUIZ("Which is the main advantage of applying a Heading 2 style to all article headings?",
             ["The headings print in colour", "Changing the style changes all the headings at once",
              "The text is checked for spelling", "The document becomes shorter"], 1,
             "Headings with the same style share the same settings, so editing the style updates them all.",
             feedback=["Colour depends on the style settings, not on using a style.", "",
                       "Spelling is checked by the spell checker.", "Styles do not shorten a document."]),
        H("Practice questions"),
        PQ("Give three examples of character formatting and three examples of paragraph formatting.",
           "Character formatting: font, font size, colour, bold, italic, underline (any three). Paragraph formatting: "
           "alignment, line spacing, spacing before or after, indent, bullets, numbering (any three)."),
        PQ("A list of the steps to reset a password must be followed in order. Which kind of list should you use? "
           "Give one reason why using the list button is better than typing the numbers yourself.",
           "Use a numbered list, because the order matters. The numbering button updates all the numbers "
           "automatically if you add, remove or move a step. Typed numbers would have to be changed by hand."),
        PQ("Explain two advantages of using heading styles instead of formatting each heading by hand.",
           "(1) Consistency: every heading with the same style looks identical. (2) Easy change: editing the style "
           "changes all the headings at once. (Also acceptable: the program knows the structure, so it can build a table "
           "of contents.)"),
        SUM("Character formatting changes selected letters: font, size, colour, bold, italic, underline.",
            "Paragraph formatting changes the whole paragraph: alignment, line spacing, spacing before and after, indents.",
            "Use bullets when order does not matter and numbering when it does.",
            "A style is a saved, named set of formatting such as Heading 1 or Normal.",
            "Styles give consistency, save time and let the program understand the structure of the document."),
    ],
))

# ------------------------------------------------------------------ 2. Tables, columns and page layout
LESSONS.append(lesson(
    module=MODULE, topic=OFFICE,
    title="Word processing: tables, columns and page layout",
    slug="wordproc-tables-columns-page-layout",
    minutes=20,
    summary="Insert and format tables, set margins, orientation and columns, add headers, footers and page numbers, and place images with text wrapping.",
    objectives=[
        "Insert a table and format its rows, columns and borders",
        "Set margins, orientation and columns for a page",
        "Add a header, a footer and page numbers",
        "Insert an image and choose a text-wrapping option",
    ],
    key_concepts=["Table", "Cell", "Margin", "Orientation", "Columns", "Header and footer", "Page number", "Text wrapping"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you formatted text and paragraphs. Now you will control the layout of the whole page. "
          "A secondary school in Buea needs a class timetable, a two-column notice and a report with the school name "
          "on every page. Each job uses a different layout feature."),
        H("Tables"),
        D("A **table** arranges information in **rows** (across) and **columns** (down). Each box where a row and a "
          "column meet is a **cell**. Tables are best for information that is naturally in a grid, such as a timetable "
          "or a price list.", title="Table"),
        T("To insert a table, choose the Insert command, then Table, and pick the number of columns and rows. Type in a "
          "cell, then press the Tab key to move to the next cell. Pressing Tab in the last cell adds a new row."),
        KEY("Common table changes", "Select the part of the table first, then use the table tools that appear.",
            cards=[["Add or delete", "Insert a row above or below, insert a column left or right, or delete a row or column."],
                   ["Merge cells", "Join several cells into one. Useful for a title that covers every column."],
                   ["Borders and shading", "Choose line style and background colour. A shaded header row makes the table easier to read."],
                   ["Alignment", "Align text inside cells. Numbers are usually aligned to the right."]]),
        CODE("""
+----------+-----------+-----------+-----------+
| Day      | 8:00      | 10:00     | 12:00     |
+----------+-----------+-----------+-----------+
| Monday   | Maths     | English   | ICT       |
| Tuesday  | Biology   | Maths     | History   |
+----------+-----------+-----------+-----------+
Row 1 is the header row (shaded). Each box is a cell.
""", "text", title="Listing 1: a small timetable table (3 rows, 4 columns)"),
        H("Page layout"),
        T("**Margins** are the blank spaces between the text and the edge of the paper. Wide margins leave room for "
          "binding and notes; narrow margins fit more text. **Orientation** is the direction of the page. "
          "**Portrait** is taller than wide (like a letter). **Landscape** is wider than tall, and suits wide tables "
          "and certificates. The **paper size** for most school work is A4."),
        T("**Columns** divide the text into side-by-side strips, as in a newspaper. A two-column layout makes short "
          "lines that are easy to read. Text fills the first column, then flows to the next. A **column break** forces "
          "text to the top of the next column."),
        H("Headers, footers and page numbers"),
        D("A **header** is text repeated at the top of every page. A **footer** is text repeated at the bottom. You "
          "type it once and it appears on all pages. A **page number** is a special field: the program counts the "
          "pages and prints the right number on each page.", title="Header and footer"),
        T("Typical use: the school name in the header, and the page number in the footer, for example Page 1 of 4. "
          "Never type page numbers by hand: they would be the same on every page."),
        H("Images and text wrapping"),
        T("To add a picture, use Insert, then Picture, and choose the file. You can then resize it. Drag a corner "
          "handle, not a side handle, so the picture keeps its proportions and does not look stretched."),
        KEY("Text wrapping options", "Wrapping decides how the text behaves around the image.",
            cards=[["In line with text", "The picture sits on a line like a big letter. Simple, but hard to position."],
                   ["Square", "Text flows around a box shape on all sides. The most common choice."],
                   ["Tight", "Text follows the outline of the picture."],
                   ["Behind or in front of text", "The picture is a background or covers the text. Use carefully: text may become unreadable."]]),
        EX("Worked example 1: make the class timetable", intro=(
            "Create a timetable for Monday to Friday with 4 lesson periods. Make the header row stand out."), steps=[
            S("Count the cells", text="Rows: 1 header row plus 5 day rows makes 6 rows. Columns: 1 for the day plus 4 periods makes 5 columns."),
            S("Insert the table", text="Insert a table with 5 columns and 6 rows and type the data, using the Tab key to move."),
            S("Format the header", text="Select the first row, make it bold, and shade it in a light colour."),
            S("Finish", text="Set the table to fit the page width and add borders."),
        ]),
        EX("Worked example 2: a two-column notice with a picture", intro=(
            "The school needs a one-page notice about sports day, in two columns, with the school badge at the "
            "left of the first paragraph."), steps=[
            S("Type the text", text="Type the notice and apply the heading and Normal styles."),
            S("Set the columns", text="Select the body text only (not the heading) and choose two columns."),
            S("Insert the badge", text="Insert the picture, resize it from a corner handle, and set the wrapping to Square."),
            S("Position", text="Drag the badge to the left of the first paragraph. The text flows around it."),
        ]),
        EX("Worked example 3: header, footer and page numbers", intro=(
            "A four-page report must show the school name at the top of each page and the page number at the bottom."), steps=[
            S("Open the header area", text="Double-click at the top of a page, or use Insert, then Header."),
            S("Type once", text="Type the school name. It repeats on all four pages."),
            S("Add the page number", text="Go to the footer and insert a page number field. The program numbers the pages 1 to 4."),
            S("Check", text="Scroll through all pages to be sure each shows the name and the right number."),
        ]),
        H("Common mistakes"),
        MISTAKE("Typing the page number by hand", "Every page would show the same number. Insert the page number field."),
        MISTAKE("Setting columns for the whole document by mistake", "The heading is squeezed into one column. Select the "
                "body text first, or insert a section break."),
        QUIZ("A table has 5 rows and 4 columns. How many cells does it have?",
             ["9", "16", "20", "54"], 2,
             "Cells = rows times columns = 5 times 4 = 20.",
             feedback=["That is 5 plus 4. Cells are counted by multiplying.", "That is 4 times 4.", "", "Not a sensible total for a 5 by 4 grid."]),
        H("Practice questions"),
        PQ("State the difference between a header and a footer, and say why a page number should be inserted as a field.",
           "A header is text repeated at the top of every page; a footer is repeated at the bottom. A page number "
           "field is counted by the program, so each page shows its own correct number. Typed numbers would be the "
           "same on every page."),
        PQ("A table has a title that must cover all 4 columns. Which table feature do you use, and which two settings "
           "make the header row easier to read?",
           "Merge the cells of the first row into one. Make the header row bold and add shading (a background colour)."),
        PQ("Explain the difference between portrait and landscape orientation and give one document that suits each.",
           "Portrait is taller than wide: it suits a letter or report. Landscape is wider than tall: it suits a wide "
           "table, a certificate or a timetable with many columns."),
        SUM("A table has rows, columns and cells. Use it for grid data, not spaces or tabs.",
            "Margins, orientation (portrait or landscape) and paper size set up the page.",
            "Columns split text into strips; select only the text you want in columns.",
            "Headers and footers repeat on every page; page numbers must be inserted as fields.",
            "Resize pictures from a corner handle and choose a wrapping option such as Square."),
    ],
))

# ------------------------------------------------------------------ 3. Long documents and mail merge
LESSONS.append(lesson(
    module=MODULE, topic=OFFICE,
    title="Word processing: long documents and mail merge",
    slug="wordproc-long-documents-mail-merge",
    minutes=22,
    summary="Build a table of contents from heading styles, use find and replace and spell check, save a template, and mail merge a letter with a data source.",
    objectives=[
        "Generate a table of contents from heading styles",
        "Use find and replace and the spell checker, and know their limits",
        "Explain what a template is and when to use one",
        "Describe the steps of a mail merge using a main document and a data source",
    ],
    key_concepts=["Table of contents", "Find and replace", "Spell check", "Template", "Mail merge", "Main document", "Data source", "Merge field"],
    blocks=[
        H("Introduction"),
        T("A final-year student in Douala must write a project report of 30 pages. The school also sends the same fee "
          "reminder letter to 200 parents. Doing this by hand wastes days. A word processor has tools for both jobs, "
          "but they work well only if the document was prepared properly. In the first two lessons you learned styles and page layout. Here you use them to manage long documents, then you meet **mail merge**."),
        H("Table of contents"),
        D("A **table of contents** (TOC) lists the headings of a document with their page numbers. The word "
          "processor builds it automatically from the **heading styles**. It looks only for paragraphs that use "
          "Heading 1, Heading 2 and so on.", title="Table of contents"),
        T("To make one: apply Heading 1 to chapter titles and Heading 2 to sections, then place the cursor on the "
          "page where the contents list should be, and choose Insert (or References) then Table of Contents. If you add "
          "text later and the page numbers change, choose Update table. You do not retype anything."),
        MISTAKE("Headings made by hand", "A line that is only bold and big is not a heading to the program. It will not "
                "appear in the table of contents. Always apply a heading style."),
        H("Find and replace, and spell check"),
        T("**Find** looks for a word or phrase in the whole document. **Replace** changes it to something else. Use "
          "**Replace all** to change every match at once. For example, the school name changed, and you replace the old "
          "name with the new name in a 30-page report in one step."),
        T("The **spell checker** underlines words that are not in its dictionary. Right-click a word to see "
          "suggestions, or run the full check from the Review tab. It helps, but it has limits. It does not find a "
          "correct word used wrongly, such as 'their' instead of 'there', or 'form' instead of 'from'. Always read the "
          "document again yourself. Set the language correctly, because a document in French is marked wrong by an "
          "English dictionary."),
        H("Templates"),
        D("A **template** is a document saved as a pattern, with the layout, styles, headers and standard text already "
          "in place. When you open it, the program makes a new copy, and the original template is not changed.",
          title="Template"),
        T("Use a template for documents you make again and again: a school letter with the letterhead, a "
          "weekly report, an invoice. Everyone in the office then produces documents with the same look. To make one, "
          "format the document, then save it as a template (the file type is different, for example a template file). "
          "To use it, choose New from template."),
        H("Mail merge"),
        D("**Mail merge** joins a **main document** with a **data source** to produce one personalised copy for each "
          "record. The main document is the letter typed once, with **merge fields** (placeholders) such as ParentName. "
          "The data source is a table or spreadsheet with one row (record) for each person and one column (field) "
          "for each item of information.", title="Mail merge"),
        IMG("f5i-mail-merge.svg", alt="A main document with three merge fields and a data source with three rows are combined by the merge into three separate letters",
            caption="Figure 1. The merge fills the fields of the main document with each row of the data source."),
        EX("Worked example 1: a table of contents for a report", intro=(
            "Your project report has 4 chapter titles and 10 section headings. You need a contents page that updates itself."), steps=[
            S("Apply styles", text="Apply Heading 1 to the 4 chapter titles and Heading 2 to the 10 section headings."),
            S("Insert the table", text="Put the cursor on the page after the title page and insert a table of contents."),
            S("Result", text="14 entries appear with page numbers, and Heading 2 entries are indented below their chapter."),
            S("Keep it correct", text="After editing, choose Update table and select the page numbers option."),
        ]),
        EX("Worked example 2: replace a name safely", intro=(
            "The report says 'Government Bilingual High School' 17 times. The school renamed it. Change it correctly."), steps=[
            S("Open the tool", text="Open Find and Replace."),
            S("Type both", text="Type the old name in Find and the new name in Replace with."),
            S("Check first", text="Use Find next two or three times to see the matches and confirm they are what you want."),
            S("Replace all", text="Click Replace all. The program reports how many changes it made. It should be 17."),
        ]),
        EX("Worked example 3: mail merge fee reminders", intro=(
            "Mme Njoh, the bursar, must send a fee reminder to 200 parents. Each letter must show the parent's name, the "
            "child's name and the amount owed."), steps=[
            S("Prepare the data source", text="In a spreadsheet, put the headings ParentName, ChildName and Amount in row 1. Add one row per parent. Save the file."),
            S("Write the main document", text="Type the letter once. Leave out the names and amount."),
            S("Connect the list", text="Start the mail merge tool and select the data source file as the recipient list."),
            S("Insert merge fields", text="Place the cursor in each gap and insert the matching field: ParentName, ChildName, Amount."),
            S("Preview", text="Use Preview results and step through a few letters to check names and amounts. Check that none is empty."),
            S("Finish", text="Merge to a new document, or send straight to the printer. You get 200 separate letters."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mail merge with a messy data source", "A name typed in two columns, an empty row or a heading in the wrong "
                "place gives wrong letters. Clean the list first: one heading per column, one record per row, no blank rows."),
        MISTAKE("Trusting the spell checker completely", "It misses real words used wrongly and does not know names. Read the "
                "text through yourself."),
        QUIZ("A report has no entries in its table of contents. The headings are bold and large. What is the most likely cause?",
             ["The spell checker is off", "The headings do not use heading styles", "The margins are too small", "The report is in portrait"], 1,
             "The table of contents is built from heading styles, not from the look of the text.",
             hint="What does the program look for when it builds the table?",
             feedback=["Spell check has no effect on the table of contents.", "",
                       "Margins do not decide which headings are collected.", "Orientation has no effect on the table."]),
        QUIZ("Which pair of items is needed for a mail merge?",
             ["A header and a footer", "A main document and a data source", "A template and a table", "Two copies of the same letter"], 1,
             "The main document has the standard text and merge fields; the data source supplies the details for each person.",
             feedback=["Headers and footers repeat text on pages; they are not merged.", "",
                       "A template can help, but the merge needs a list of data.", "The letter is written once, not twice."]),
        H("Practice questions"),
        PQ("Explain how a table of contents is produced automatically and what you do when the report grows by three pages.",
           "Apply heading styles (Heading 1, Heading 2) to all headings, then insert a table of contents; the program "
           "collects the headings and their page numbers. After the report changes, update the table so the page "
           "numbers are correct."),
        PQ("Give two reasons why a spell checker cannot replace careful proofreading.",
           "It does not find correctly spelt words used wrongly (for example 'their' and 'there'), and it may mark "
           "names and technical terms as wrong or use the wrong language dictionary. A person must read the text for meaning."),
        PQ("A school wants to send a personal invitation to each of 150 guests. Describe the steps of a mail merge.",
           "(1) Make a data source with one row per guest and a column for each detail such as Name. (2) Type the "
           "invitation once as the main document. (3) Connect the data source to the main document. (4) Insert merge fields "
           "where the guest's details go. (5) Preview the results to check them. (6) Finish the merge to get 150 "
           "personalised invitations, to print or save."),
        SUM("A table of contents is built from heading styles, and must be updated when the document changes.",
            "Find and replace changes text everywhere; check the matches before using Replace all.",
            "The spell checker helps but cannot replace reading the text yourself.",
            "A template is a saved pattern for documents you make often.",
            "Mail merge joins a main document with merge fields to a data source and makes one personalised copy per record."),
    ],
))

# ------------------------------------------------------------------ 4. Spreadsheets: cells, formulas and references
LESSONS.append(lesson(
    module=MODULE, topic=OFFICE,
    title="Spreadsheets: cells, formulas and references",
    slug="spreadsheet-cells-formulas-references",
    minutes=22,
    summary="Enter data in cells, write formulas with operators, and explain relative and absolute references when copying formulas, using a shop price list.",
    objectives=[
        "Name cells by column letter and row number and enter text, numbers and formulas",
        "Write formulas with +, -, multiplication, division and brackets",
        "Explain relative and absolute references in words",
        "Copy a formula and predict how the references change",
    ],
    key_concepts=["Spreadsheet", "Cell", "Cell address", "Formula", "Relative reference", "Absolute reference", "Fill handle"],
    blocks=[
        H("Introduction"),
        T("Mr Tabi owns a small provision shop in Mbouda. Each evening he writes the day's sales in an exercise book "
          "and adds them with a calculator. One wrong key and the total is wrong. If a price changes, he must "
          "recalculate everything. A **spreadsheet** program (Microsoft Excel, LibreOffice Calc, Google Sheets) does this "
          "work for you. You type the prices and quantities once, and when a price changes the totals change by "
          "themselves."),
        H("Rows, columns and cells"),
        D("A spreadsheet is a grid. **Columns** run down the page and have letters (A, B, C...). **Rows** run across and "
          "have numbers (1, 2, 3...). A **cell** is the box where a column and a row meet. Its **cell address** is the "
          "column letter followed by the row number, such as B3 (column B, row 3). A **range** is a block of cells, written "
          "with a colon, such as B2:B6.", title="Cells and addresses"),
        T("You can put three kinds of content in a cell: **text** (labels such as Rice), **numbers** (700) and "
          "**formulas** (a calculation). Text is shown on the left of the cell and numbers on the right. If a number "
          "appears on the left, it was probably typed as text, and the program will not calculate with it."),
        CODE("""
     A            B        C      D
1    Item         Price    Qty    Total
2    Rice         700      5      3500
3    Cooking oil  1200     3      3600
4    Sugar        800      4      3200
5    Salt         150      10     1500
6    Soap         250      6      1500

B3 holds 1200.   The range D2:D6 has 5 cells.
""", "text", title="Listing 1: the shop price list (prices in FCFA)"),
        H("Formulas"),
        D("A **formula** is a calculation typed in a cell. It always starts with an equals sign (=). Instead of "
          "typing numbers, it uses cell addresses, so the answer updates when the data changes.", title="Formula"),
        KEY("Operators", "These signs tell the formula what to do.",
            cards=[["+ and -", "Add and subtract. Example: =B2+C2"],
                   ["Multiply", "The sign for multiplication is the asterisk key (see Listing 2). Example: price times quantity."],
                   ["/", "Divide. Example: =D7/5"],
                   ["Brackets", "Work out first what is inside the brackets. Example: =(B2+C2)/2"]]),
        T("The program follows the order you know from mathematics: brackets first, then multiplication and division, "
          "then addition and subtraction. So 60 + 80 / 2 gives 100, but (60 + 80) / 2 gives 70."),
        CODE("""
D2:  =B2*C2         price times quantity for Rice: 700 x 5 = 3500
D7:  =D2+D3+D4+D5+D6   adds the five totals: 13300
""", "text", title="Listing 2: formulas typed in cells D2 and D7",
             caption="In a spreadsheet the asterisk means multiply."),
        H("Copying formulas: relative and absolute references"),
        D("A **relative reference** is a cell address such as B2 that adjusts when you copy the formula. If you copy "
          "=B2 times C2 from row 2 to row 3, it becomes =B3 times C3. The formula keeps the same positions "
          "relative to its new cell.", title="Relative reference"),
        D("An **absolute reference** never changes when copied. You make it absolute by typing a dollar sign before "
          "the column letter and another before the row number, as in Listing 3. Use it for one fixed cell that every "
          "copy of the formula must use, such as a discount rate or an exchange rate.", title="Absolute reference"),
        T("You do not have to type a formula in every row. Type it once, then drag the **fill handle** (the small square "
          "at the bottom-right of the selected cell) down. The formula is copied, and relative references adjust."),
        CODE("""
     A            B        C      D        E                 G
1    Item         Price    Qty    Total    After discount    Discount
2    Rice         700      5      3500     3150              10%
3    Cooking oil  1200     3      3600     3240
...

E2:  =D2*(1-$G$2)     3500 x (1 - 0.10) = 3150
E3:  =D3*(1-$G$2)     D2 became D3 (relative), $G$2 stayed (absolute)
""", "text", title="Listing 3: a discount rate kept in one cell",
             caption="Dollar signs make G2 absolute. The asterisk means multiply."),
        EX("Worked example 1: totals for each item", intro=(
            "Use Listing 1. Write a formula for the total of each item, and find the value of the grand total."), steps=[
            S("Write the first formula", text="In D2 type the formula that multiplies B2 by C2 (see Listing 2). The result is 700 times 5, which is 3500."),
            S("Copy down", text="Drag the fill handle from D2 to D6. D3 multiplies B3 by C3, D4 multiplies B4 by C4, and so on."),
            S("Check the results", text="D2 to D6 show 3500, 3600, 3200, 1500 and 1500."),
            S("Grand total", text="3500 + 3600 + 3200 + 1500 + 1500 = 13300 FCFA. Adding D2 to D6 in a formula, as in Listing 2, gives this."),
        ]),
        EX("Worked example 2: a 10% discount", intro=(
            "Mr Tabi gives a 10% discount at the end of the month. The rate is in G2. Write a formula for the price after "
            "discount and find the discounted grand total."), steps=[
            S("Why absolute?", text="Every row must use the same rate in G2. If G2 were relative, copying down would give G3, G4, and so on, which are empty."),
            S("Write the formula", text="In E2 type the formula in Listing 3: D2 multiplied by (1 minus G2), with dollar signs before the G and the 2. The result is 3500 times 0.90, which is 3150."),
            S("Copy down", text="Copy E2 to E6. Each row keeps the absolute G2 but uses its own D value."),
            S("Total", text="13300 times 0.90 = 11970 FCFA after discount."),
            S("What if", text="Change G2 to 15%. Every total in column E updates at once."),
        ]),
        EX("Worked example 3: predict the copied formula", intro=(
            "The formula in Listing 3 is in E2: D2 multiplied by (1 minus G2), with G2 absolute. It is copied to E5. What does E5 contain?"), steps=[
            S("Column D part", text="D2 is relative. E5 is 3 rows below E2, so D2 becomes D5."),
            S("Dollar part", text="The G2 part is absolute (dollar signs), so it does not change."),
            S("Answer", text="E5 contains the same formula with D5 in place of D2, and G2 still absolute: D5 multiplied by (1 minus G2)."),
        ]),
        H("Common mistakes"),
        MISTAKE("Typing numbers instead of cell addresses", "A formula that multiplies the typed numbers 700 and 5 does not change when the price changes. "
                "Multiply B2 by C2 so the model stays correct."),
        MISTAKE("A relative reference for a fixed cell", "Copying down changes G2 into G3, G4 and so on. Make the fixed cell absolute."),
        QUIZ("Cell C4 contains =A4+B4. It is copied to C7. What does C7 contain?",
             ["=A4+B4", "=A7+B7", "=C7+D7", "=A4+B7"], 1,
             "Both references are relative. C7 is 3 rows below C4, so each row number increases by 3.",
             hint="Are there any dollar signs in the formula?",
             feedback=["That would be right only if both references were absolute.", "",
                       "The columns do not change when copying straight down.", "Both row numbers change, not just one."]),
        H("Practice questions"),
        PQ("State the address of the cell in column C, row 8. Name the three kinds of content that a cell can hold.",
           "C8. A cell can hold text, a number or a formula."),
        PQ("Cell D2 holds the price and E2 holds the quantity. Write a formula in F2 for the total and say what F3 "
           "contains after F2 is copied down.",
           "In F2 write the formula that multiplies D2 by E2. After copying down, F3 multiplies D3 by E3, because "
           "relative references change row by row."),
        PQ("Explain the difference between a relative and an absolute reference, and say which is needed for a "
           "discount rate stored in one cell.",
           "A relative reference changes when the formula is copied; an absolute reference (dollar signs before the "
           "column and row) stays the same. The discount rate needs an absolute reference so all rows use the one cell."),
        SUM("A cell is named by column letter and row number, such as B3; a range such as B2:B6 is a block of cells.",
            "A formula starts with = and uses cell addresses, so results update when data changes.",
            "Brackets are calculated first, then multiplication and division, then addition and subtraction.",
            "A relative reference adjusts when copied; an absolute reference (dollar signs) stays fixed.",
            "Type a formula once and copy it with the fill handle."),
    ],
))

# ------------------------------------------------------------------ 5. Spreadsheets: functions for decisions
LESSONS.append(lesson(
    module=MODULE, topic=OFFICE,
    title="Spreadsheets: functions for decisions",
    slug="spreadsheet-functions-if-lookup",
    minutes=24,
    summary="Use SUM, AVERAGE, MAX, MIN and COUNT on a range, and IF and nested IF to give grades, with the idea of a lookup table, on a class marks sheet.",
    objectives=[
        "Use SUM, AVERAGE, MAX, MIN and COUNT with a range",
        "Write an IF formula with a test and two results",
        "Write a nested IF that gives grades",
        "Describe what a lookup table does",
    ],
    key_concepts=["Function", "Range", "SUM", "AVERAGE", "MAX and MIN", "COUNT", "IF", "Nested IF", "Lookup"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you wrote formulas such as B2 times C2. For bigger jobs, typing every cell is too slow. "
          "A class teacher in Bamenda has the ICT marks of 8 students. She needs the total, the average, the best and "
          "lowest marks, and a grade for each student."),
        H("Functions and ranges"),
        D("A function is a ready-made formula with a name. It is written as a name followed by brackets, with its **arguments** inside: =SUM(B2:B9). "
          "The argument B2:B9 is a **range**: every cell from B2 to B9. Several arguments are separated by commas.",
          title="Function and range"),
        CODE("""
     A       B       C
1    Name    Mark    Grade
2    Ada     72      B
3    Bih     45      F
4    Chi     58      C
5    Dan     91      A
6    Eka     33      F
7    Fon     66      B
8    Gwen    50      C
9    Hans    84      A
""", "text", title="Listing 1: the class marks sheet (marks out of 100)"),
        KEY("Five summary functions", "Each takes a range such as B2:B9.",
            cards=[["SUM", "Adds all the numbers. SUM(B2:B9) gives 499."],
                   ["AVERAGE", "The mean: total divided by how many numbers. AVERAGE(B2:B9) gives 62.375."],
                   ["MAX and MIN", "The largest and smallest numbers. MAX gives 91 and MIN gives 33."],
                   ["COUNT", "How many cells contain numbers (text is not counted). COUNT(B2:B9) gives 8."]]),
        H("Making decisions with IF"),
        D("The **IF** function tests a condition and gives one result if it is true and another if it is false. It has "
          "three parts: the test, the value if true, and the value if false: =IF(test, value if true, value if false).",
          title="IF function"),
        T("A test compares two things. The signs are: greater than (>), less than (<), equal to (=), greater than or "
          "equal to (>=), less than or equal to (<=) and not equal to (<>). Text in a result goes inside double quotes."),
        CODE("""
D2:  =IF(B2>=50,"Pass","Fail")

Ada  B2=72  test 72>=50 is true   -> Pass
Bih  B3=45  test 45>=50 is false  -> Fail
""", "text", title="Listing 2: a simple IF"),
        H("Nested IF for grades"),
        T("A simple IF has only two outcomes. For grades you need several. You can put an IF inside another IF. This "
          "is a **nested IF**. The program tests the conditions in order, and stops at the first one that is true."),
        CODE("""
Grade scale used in this lesson:  80 or more A,  60 to 79 B,  50 to 59 C,  below 50 F

C2:  =IF(B2>=80,"A",IF(B2>=60,"B",IF(B2>=50,"C","F")))

Ada  72:  72>=80 false -> 72>=60 true  -> B
Dan  91:  91>=80 true                  -> A
Eka  33:  false, false, false          -> F
""", "text", title="Listing 3: a nested IF for grades",
             caption="This scale is an example. Use your own school's scale."),
        H("The lookup idea"),
        T("A nested IF with many grades becomes long. A **lookup** is a neater method: you keep the boundaries in a small "
          "table on the sheet, and a lookup function (VLOOKUP, or LOOKUP) searches the table for the row that matches the "
          "mark and returns the grade. To change the scale, you edit the table, not the formulas. For this "
          "course, you need to know the idea: look up a value in a table and return the matching result."),
        CODE("""
Lookup table (cells F2:G5):      F (from)   G (grade)
                                 0          F
                                 50         C
                                 60         B
                                 80         A

Mark 72 falls in the row that starts at 60, so the grade is B.
""", "text", title="Listing 4: a lookup table for the same grades"),
        EX("Worked example 1: summary figures", intro=(
            "Use the marks in Listing 1 (B2 to B9). Write the functions for total, average, highest, lowest and number "
            "of students, and give each result."), steps=[
            S("Total", text="SUM(B2:B9): 72 + 45 + 58 + 91 + 33 + 66 + 50 + 84 = 499."),
            S("Average", text="AVERAGE(B2:B9): 499 divided by 8 = 62.375."),
            S("Highest and lowest", text="MAX(B2:B9) = 91 and MIN(B2:B9) = 33."),
            S("Count", text="COUNT(B2:B9) = 8 students."),
        ]),
        EX("Worked example 2: Pass or Fail", intro=(
            "A mark of 50 or more is a Pass. Write the formula for D2 and say how many students pass."), steps=[
            S("Write the test", text="The test is B2>=50 (is the mark at least 50?)."),
            S("Write the formula", text='=IF(B2>=50,"Pass","Fail"), as in Listing 2. Copy it down to D9.'),
            S("Count the passes", text="Marks of 50 or more: 72, 58, 91, 66, 50, 84. That is 6 students. Note that 50 passes because the test is 'at least'."),
            S("Extra", text="A function called COUNTIF counts the cells that meet a condition, so it can give the 6 directly."),
        ]),
        EX("Worked example 3: grade for Gwen", intro=(
            "Use the nested IF in Listing 3. What grade does Gwen (50) get? Trace each test."), steps=[
            S("First test", text="50 >= 80 is false, so go to the next IF."),
            S("Second test", text="50 >= 60 is false, so go to the next IF."),
            S("Third test", text="50 >= 50 is true, so the result is C."),
            S("Answer", text="Gwen's grade is C. If the third test used 51, she would get F."),
        ]),
        H("Common mistakes"),
        MISTAKE("A wrong range", "SUM(B2:B8) leaves out Hans (B9). Check that the range includes the first and last cells."),
        MISTAKE("Numbers stored as text", "COUNT and SUM ignore numbers that were typed as text (they sit on the left). Retype them as numbers."),
        QUIZ("Which function finds the highest mark in B2:B9?",
             ["SUM(B2:B9)", "COUNT(B2:B9)", "MAX(B2:B9)", "AVERAGE(B2:B9)"], 2,
             "MAX returns the largest number in the range.",
             hint="Look for the function whose name means largest.",
             feedback=["SUM adds the numbers.", "COUNT counts the cells with numbers.", "", "AVERAGE gives the mean."]),
        H("Practice questions"),
        PQ("The marks of 5 students are in cells C2 to C6. Write the functions to find (a) the total, (b) the average, "
           "(c) the lowest mark.",
           "(a) =SUM(C2:C6). (b) =AVERAGE(C2:C6). (c) =MIN(C2:C6)."),
        PQ("Write a formula in D2 that shows Pass if B2 is 50 or more and Fail otherwise. What does it show when B2 holds 50?",
           'In D2 write =IF(B2>=50,"Pass","Fail"). When B2 is 50, the test 50 >= 50 is true, so it shows Pass.'),
        PQ("Write a nested IF that gives A for 80 or more, B for 60 to 79, C for 50 to 59 and F otherwise (mark in B2). "
           "What grade does 66 get?",
           'The formula is =IF(B2>=80,"A",IF(B2>=60,"B",IF(B2>=50,"C","F"))). For 66: 66>=80 is false, 66>=60 is true, so the grade is B.'),
        SUM("A function has a name and arguments, such as SUM(B2:B9); a range uses a colon.",
            "SUM adds, AVERAGE gives the mean, MAX and MIN give the largest and smallest, COUNT counts numbers.",
            "IF has three parts: the test, the value if true and the value if false.",
            "Nested IF handles several outcomes; test from the highest boundary down.",
            "A lookup table finds the matching result for a value and makes a scale easy to change."),
    ],
))

# ------------------------------------------------------------------ 6. Spreadsheets: charts, sorting and what-if models
LESSONS.append(lesson(
    module=MODULE, topic=OFFICE,
    title="Spreadsheets: charts, sorting and what-if models",
    slug="spreadsheet-charts-sorting-whatif-models",
    minutes=24,
    summary="Choose and label the right chart, sort and filter data, and build a budget or loan model where changing one input shows the result.",
    objectives=[
        "Choose a column, line or pie chart to suit the data",
        "Label a chart with a title, axis titles and a legend",
        "Sort and filter a list of data",
        "Change an input in a model and read the new results (what-if)",
    ],
    key_concepts=["Chart", "Column chart", "Line chart", "Pie chart", "Axis title", "Sort", "Filter", "Spreadsheet model", "What-if analysis"],
    blocks=[
        H("Introduction"),
        T("Mr Tabi's sheet shows the totals for each item, but his supplier does not want to read a table of numbers. "
          "He wants a picture that shows which items sell best. His sister, who plans to borrow money to start a small "
          "business, wants to know what happens to her repayments if the interest rate changes. In the previous two lessons you wrote formulas and functions. Now you present results with a chart, organise data by sorting and filtering, and use the sheet as a **model**."),
        H("Choosing the right chart"),
        D("A **chart** turns the numbers of a range into a picture. The right choice depends on what you want to show.",
          title="Chart"),
        KEY("Three common charts", "Select the data first, including the labels, then insert the chart.",
            cards=[["Column or bar chart", "Compares separate categories, such as sales of each item. The bar height shows the value."],
                   ["Line chart", "Shows how something changes over time, such as sales each month. Points are joined by a line."],
                   ["Pie chart", "Shows the parts of one whole, such as how a monthly budget is shared. Use few slices and only when the parts add to a total."]]),
        T("Do not use a pie chart to compare items that are not parts of the same whole. Do not use a line chart for "
          "unrelated categories, because the line suggests a trend that is not there."),
        H("Labelling a chart"),
        T("A chart without labels is a puzzle. Always add: a **title** that says what the chart shows; **axis titles** "
          "(the horizontal axis names the categories or time, and the vertical axis names the quantity and unit, "
          "such as Sales (FCFA)); and a **legend** if the chart has more than one series. Check that the scale starts at "
          "zero, so that the bars give an honest picture."),
        H("Sorting and filtering"),
        D("**Sorting** puts the rows in order, for example from largest to smallest. **Filtering** hides the rows that do "
          "not meet a condition, so you see only the rows you need. Filtering does not delete anything: clearing the "
          "filter brings the rows back.", title="Sort and filter"),
        CODE("""
Item         Total (FCFA)          Sorted, largest first
Rice         3500                  Cooking oil   3600
Cooking oil  3600                  Rice          3500
Sugar        3200                  Sugar         3200
Salt         1500                  Salt          1500
Soap         1500                  Soap          1500

Filter: Total greater than 3000  ->  Rice, Cooking oil, Sugar
""", "text", title="Listing 1: sorting and filtering the shop totals"),
        T("When you sort, select all the columns of the table, or click one cell inside it, so the whole row moves "
          "together. If you sort only one column, the names and numbers no longer match."),
        H("What-if models"),
        D("A **spreadsheet model** represents a real situation with inputs (numbers you can change) and formulas "
          "(results that depend on them). **What-if analysis** means changing an input and watching how the results "
          "change.", title="Spreadsheet model"),
        CODE("""
     A                  B
1    Loan amount        200000
2    Yearly rate        12%
3    Years              2
4    Interest           =B1*B2*B3        -> 48000
5    Total to repay     =B1+B4           -> 248000
6    Monthly payment    =B5/(B3*12)      -> 10333.33

Inputs: B1, B2, B3.   Results: B4, B5, B6.   Change B2 to 10% and all results update.
""", "text", title="Listing 2: a simple loan model",
             caption="This model uses simple interest to keep the idea clear. Real loans may be calculated differently."),
        EX("Worked example 1: choose a chart", intro=(
            "For each job, name the best chart: (a) sales of five items on one day; (b) monthly sales over a year; "
            "(c) how a 150000 FCFA monthly income is shared between rent, food, transport, airtime and savings."), steps=[
            S("Part (a)", text="Separate categories to compare: a column (or bar) chart."),
            S("Part (b)", text="A change over time: a line chart, with the months on the horizontal axis."),
            S("Part (c)", text="Parts of one whole that add to 150000: a pie chart."),
            S("Label them", text="Give each a title and axis titles (except the pie chart, which uses labels or a legend)."),
        ]),
        EX("Worked example 2: a loan what-if", intro=(
            "Use Listing 2. The bank offers the loan at 10% a year instead of 12%. Find the new interest, total and monthly payment."), steps=[
            S("Change one input", text="Change B2 from 12% to 10%. Nothing else is typed."),
            S("Interest", text="200000 times 0.10 times 2 = 40000 FCFA."),
            S("Total and monthly", text="Total = 200000 + 40000 = 240000. Monthly = 240000 divided by 24 = 10000 FCFA."),
            S("Compare", text="Original: 10333.33 a month. New: 10000 a month. The lower rate saves about 333 FCFA each month (8000 FCFA over 24 months)."),
        ]),
        EX("Worked example 3: a budget model", intro=(
            "A student has an income of 150000 FCFA. Rent is 50000, food is 45000, transport is 20000 and airtime and "
            "data are 10000. Find the savings. Then find the balance if the rent rises to 55000."), steps=[
            S("Add the costs", text="50000 + 45000 + 20000 + 10000 = 125000."),
            S("Savings", text="150000 - 125000 = 25000 FCFA."),
            S("What-if: rent 55000", text="Costs = 55000 + 45000 + 20000 + 10000 = 130000. Balance = 150000 - 130000 = 20000."),
            S("Meaning", text="A 5000 increase in rent reduces savings by exactly 5000, from 25000 to 20000."),
        ]),
        H("Common mistakes"),
        MISTAKE("A pie chart for unrelated numbers", "A pie must show parts of one whole. Use a column chart to compare separate items."),
        MISTAKE("A chart with no title or axis titles", "The reader cannot tell what the bars mean or which unit is used."),
        QUIZ("A shop records its sales for each month from January to December. Which chart shows the trend best?",
             ["Pie chart", "Line chart", "No chart; a table is best", "A chart without axes"], 1,
             "A line chart shows change over time.",
             hint="Which chart joins points that follow one another in time?",
             feedback=["A pie shows parts of a whole at one moment, not a trend.", "",
                       "A table is acceptable, but the question asks for a chart that shows the trend.", "Axes are needed to read a chart."]),
        QUIZ("In a loan model, the interest rate in cell B2 is changed from 12% to 10%. What happens to cells that use B2 in a formula?",
             ["Nothing; they must be retyped", "They recalculate automatically", "They are deleted", "They show an error"], 1,
             "Formulas depend on cell references, so the results update when the input changes.",
             feedback=["That would be true only if numbers had been typed instead of formulas.", "",
                       "Changing an input never deletes formulas.", "The formulas are valid, so no error appears."]),
        H("Practice questions"),
        PQ("Name the best chart for each: (a) the number of students in each of five classes; (b) the temperature "
           "every hour for a day; (c) the share of a school's budget spent on each of four items.",
           "(a) Column or bar chart. (b) Line chart. (c) Pie chart."),
        PQ("List four things a good chart should have.",
           "A title, axis titles (with units), a suitable chart type and a legend when there is more than one series. "
           "(A scale starting at zero for bar charts is also accepted.)"),
        PQ("The shop list has columns Item, Price and Quantity. Explain how to see the items from the most expensive to the "
           "cheapest without mixing up the rows, and how to show only the items that cost more than 1000.",
           "Select the whole table and sort by Price, largest first, so each row moves as a whole. To show only items "
           "above 1000, apply a filter on Price with the condition greater than 1000. The other rows are hidden and "
           "not deleted."),
        SUM("Use a column chart to compare categories, a line chart for change over time and a pie chart for parts of a whole.",
            "Give every chart a title, axis titles with units and a legend when needed.",
            "Sorting orders rows; filtering hides rows that do not match. Select the whole table when sorting.",
            "A spreadsheet model has inputs and formulas; the results depend on the inputs.",
            "What-if analysis changes an input and reads the new results."),
    ],
))
