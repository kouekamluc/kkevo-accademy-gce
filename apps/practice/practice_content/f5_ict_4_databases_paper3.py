"""Practice sets for Form 5 ICT: Databases and Paper 3 practical."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "form-5")

PRACTICAL = "Practical skills"
DATABASES = "Databases"
EXAM = "Examination"
PAPER3 = "Paper 3 (practical)"

SETS = []

# ------------------------------------------------------------------ Set 1
SETS.append(practice_set(
    module=PRACTICAL, topic=DATABASES,
    title="Tables, fields, records and keys",
    lesson="ict-database-tables-fields-and-keys",
    questions=[
        MC("In a database table, a single row that holds all the data about one student is called a:", [
            C("Field", why="A field is a column, one item of information such as Surname."),
            C("Record", correct=True),
            C("Primary key", why="A primary key is one field that identifies the record, not the whole row."),
            C("Data type", why="A data type says what kind of value a field holds."),
        ], steps=[S("Recall the parts of a table", text="Columns are fields. Rows are records."),
                  S("Match", text="One row of data about one student is a record.")],
           concept="Records and fields", skill="Recall", hint="Think of a table as a grid. Is a row a column or a row?"),
        MC("Which data type is best for a field that holds a phone number such as 677 12 34 56?", [
            C("Number", why="Phone numbers are not used in calculations, and a number type can lose a leading zero or plus sign."),
            C("Yes/No", why="A Yes/No field holds only two values."),
            C("Date/Time", why="A phone number is not a date."),
            C("Text", correct=True),
        ], steps=[S("Ask whether it will be calculated with", text="You never add or average phone numbers."),
                  S("Choose", text="Text keeps spaces, a plus sign and leading zeros.")],
           concept="Choosing data types", skill="Application", hint="Will you ever add two phone numbers together?"),
        MC("Which field is the most suitable primary key for a Students table?", [
            C("StudentID", correct=True),
            C("Surname", why="Two students can have the same surname, so it is not unique."),
            C("Class", why="Many students are in the same class."),
            C("DateOfBirth", why="Two students can be born on the same day."),
        ], steps=[S("A primary key must be unique", text="No two records may have the same value."),
                  S("Check each field", text="Only a unique code such as StudentID is certain to differ for every student.")],
           concept="Primary key", skill="Application", hint="Which field is unique for every student?"),
        MC("A Products table has 5 fields and 40 records. How many records does it hold?", [
            C("5", why="5 is the number of fields (columns)."),
            C("45", why="The numbers of fields and records are not added together."),
            C("41", why="The field names are not a record, so you do not add 1 for the header."),
            C("40", correct=True),
        ], steps=[S("Count rows of data", text="Each record is one row of data."),
                  S("Ignore the header", text="The header row holds field names and is not a record. So there are 40 records.")],
           concept="Records and fields", skill="Recall", hint="Records are rows. Is the header row a record?"),
        MC("In a Loans table, StudentID holds values taken from the primary key of the Students table. In Loans, StudentID is a:", [
            C("Primary key", why="LoanID is the primary key of Loans. StudentID repeats when a student has many loans."),
            C("Calculated field", why="It is stored data, not worked out from other fields."),
            C("Foreign key", correct=True),
            C("Report", why="A report is a printout of data, not a field."),
        ], steps=[S("Where does the value come from?", text="It comes from the primary key of another table."),
                  S("Name it", text="A field that links to another table's primary key is a foreign key.")],
           concept="Foreign key", skill="Concept", hint="Look at where the values of this field come from."),
        MC("One teacher teaches many classes, but each class has only one teacher. This relationship is:", [
            C("One-to-one", why="One-to-one would mean each teacher has exactly one class."),
            C("Many-to-many", why="Many-to-many would mean a class could have several teachers in the table."),
            C("Foreign", why="Foreign is a type of key, not a type of relationship."),
            C("One-to-many", correct=True),
        ], steps=[S("Read from the teacher side", text="One teacher links to many classes."),
                  S("Name it", text="This is a one-to-many relationship from Teachers to Classes. The foreign key TeacherID goes in the Classes table.")],
           concept="Relationships", skill="Concept", hint="Count how many classes one teacher can have, and how many teachers one class can have."),
        MC("A table Loans has the fields LoanID, StudentID, BookTitle, DateBorrowed and Returned. Which choice gives the most suitable data types in that order?", [
            C("Number, Text, Text, Date, Yes/No", correct=True),
            C("Text, Number, Date, Text, Yes/No", why="BookTitle is words and DateBorrowed is a date, so these two types are swapped."),
            C("Number, Text, Text, Text, Text", why="A date should have a date type so it sorts correctly, and Returned has only two values."),
            C("Yes/No, Text, Text, Date, Number", why="LoanID is a number or AutoNumber, not Yes/No, and Returned is not a number."),
        ], steps=[S("LoanID", text="A whole number or AutoNumber code."),
                  S("StudentID and BookTitle", text="Text."),
                  S("DateBorrowed", text="Date, so that dates sort in order."),
                  S("Returned", text="Yes/No, because it has only two values.")],
           concept="Choosing data types", skill="Application", hint="Go field by field and ask what kind of value goes in it."),
        MC("A table has records of 100 students and another table has 400 loans. Which is true about the foreign key StudentID in Loans?", [
            C("It must be different in every loan record", why="That describes a primary key. A student with several loans appears several times."),
            C("It can repeat, and every value must exist in Students", correct=True),
            C("It can be left out because loans do not need to link to students", why="The foreign key is exactly what links each loan to a student."),
            C("It must be a Yes/No field", why="It holds the StudentID codes, which are text."),
        ], steps=[S("Repeats?", text="One student can borrow many books, so a StudentID can appear many times in Loans."),
                  S("Valid values?", text="A loan should only name a student who exists in Students.")],
           concept="Foreign key", skill="Reasoning", hint="Can a student borrow two books? What must be true of the code in each loan?"),
    ]))

# ------------------------------------------------------------------ Set 2
SETS.append(practice_set(
    module=PRACTICAL, topic=DATABASES,
    title="Sorting, searching and calculating with queries",
    lesson="ict-database-queries-sort-search-calculate",
    questions=[
        MC("What is a query?", [
            C("A screen for entering records one at a time", why="That is a form."),
            C("A formatted printout of results", why="That is a report."),
            C("A question that selects the fields and records you want", correct=True),
            C("A copy of the database kept elsewhere", why="That is a backup."),
        ], steps=[S("Recall", text="A query asks the database a question and shows only the matching fields and records.")],
           concept="What a query is", skill="Recall", hint="Think of asking the database a question."),
        MC("Which SQL clause sorts the results?", [
            C("WHERE", why="WHERE chooses which records are shown. It does not sort."),
            C("FROM", why="FROM names the table."),
            C("SELECT", why="SELECT chooses the fields."),
            C("ORDER BY", correct=True),
        ], steps=[S("Match each clause to its job", text="SELECT: fields. FROM: table. WHERE: criteria. ORDER BY: sorting.")],
           concept="SQL clauses", skill="Recall", hint="The word 'order' is a clue."),
        MC("Which query shows the Name and Price of products that cost more than 1000 FCFA?", [
            C("SELECT Name, Price FROM Products WHERE Price > 1000;", correct=True),
            C("SELECT Name, Price FROM Products ORDER BY Price > 1000;", why="ORDER BY sorts. A condition belongs in WHERE."),
            C("SELECT Price > 1000 FROM Products;", why="SELECT lists fields. The condition goes in WHERE."),
            C("SELECT Name, Price FROM Products WHERE Price < 1000;", why="Less than gives the cheap items, the opposite."),
        ], steps=[S("Choose the fields", text="SELECT Name, Price."),
                  S("Choose the table", text="FROM Products."),
                  S("Add the criterion", text="WHERE Price > 1000.")],
           concept="SELECT and WHERE", skill="Application", hint="Which clause holds a condition?"),
        MC("In the Products table, Rice 1kg costs 700 and has 40 in stock, Beans 1kg costs 800 and has 25, and Maize 1kg costs 500 and has 0. The criteria are Category = 'Grains' AND Price < 750. Which products are shown?", [
            C("Rice 1kg only", why="Maize 1kg is also a grain and costs less than 750."),
            C("Rice 1kg, Beans 1kg and Maize 1kg", why="Beans cost 800, which is not less than 750."),
            C("Rice 1kg and Maize 1kg", correct=True),
            C("Beans 1kg only", why="800 is not less than 750."),
        ], steps=[S("Test Rice", text="Grains, and 700 is less than 750: shown."),
                  S("Test Beans", text="Grains, but 800 is not less than 750: not shown."),
                  S("Test Maize", text="Grains, and 500 is less than 750: shown (stock level does not matter).")],
           concept="AND criteria", skill="Application", hint="Test each product against both conditions."),
        MC("In the Products table the oils are Palm oil (1200) and Groundnut oil (1500), and Honey costs 2500. How many products does Category = 'Oils' OR Price > 2000 show?", [
            C("1", why="You may have used AND. With OR, either condition is enough."),
            C("2", why="Honey is not an oil, but it costs more than 2000, so it is also shown."),
            C("0", why="Both oils meet the first condition."),
            C("3", correct=True),
        ], steps=[S("Palm oil", text="Oil: shown."),
                  S("Groundnut oil", text="Oil: shown."),
                  S("Honey", text="Price 2500 is more than 2000: shown. Total 3.")],
           concept="OR criteria", skill="Application", hint="With OR, one true condition is enough."),
        MC("A query must list products from the most expensive to the cheapest. Which sort setting is needed on Price?", [
            C("Ascending", why="Ascending goes from smallest to largest, the cheapest first."),
            C("Descending", correct=True),
            C("Group", why="Grouping does not order the values."),
            C("Unsorted", why="Without sorting, the records appear in the order they were entered."),
        ], steps=[S("Most expensive first", text="The largest price comes first.")],
           concept="Sort order", skill="Application", hint="Largest first, which direction is that?"),
        NUM("A product has Price 900 FCFA and Quantity 30. A calculated field StockValue is Price multiplied by Quantity. What is StockValue in FCFA?", 27000,
            steps=[S("Multiply", math=r"900 \times 30 = 27000")],
            concept="Calculated fields", skill="Calculation", hint="Multiply the two field values.", tolerance=0),
        MC("Why is StockValue (Price multiplied by Quantity) better as a calculated field in a query than a value typed into the table?", [
            C("It updates automatically when Price or Quantity change", correct=True),
            C("It uses less typing but cannot be sorted", why="A calculated field can be sorted like any other column."),
            C("It changes the Price stored in the table", why="A query only shows data. The stored fields do not change."),
            C("It becomes the primary key of the table", why="A calculated field is not stored, so it cannot be the primary key."),
        ], steps=[S("What is stored?", text="Only Price and Quantity are stored."),
                  S("What happens when they change?", text="The query works out StockValue again each time it runs, so it is always correct. A typed value would be out of date.")],
           concept="Calculated fields", skill="Reasoning", hint="What happens to a typed total when the price changes?"),
    ]))

# ------------------------------------------------------------------ Set 3
SETS.append(practice_set(
    module=PRACTICAL, topic=DATABASES,
    title="Forms, reports and accurate data",
    lesson="ict-database-forms-reports-and-accuracy",
    questions=[
        MC("What is the main purpose of a database form?", [
            C("To print results with totals", why="That is the job of a report."),
            C("To make entering, viewing and editing records easier", correct=True),
            C("To back up the data", why="A backup is a separate copy of the database."),
            C("To sort records in a table", why="Sorting is done in a query or on the table."),
        ], steps=[S("Recall", text="A form is a friendly screen for entering and editing records, usually one at a time.")],
           concept="Forms", skill="Recall", hint="Who uses a form: the person typing data, or the reader of a printout?"),
        MC("A validation rule on Quantity says: must be 0 or more. A user types -5. What happens?", [
            C("The record is saved and the value becomes 5", why="The database never changes a value by itself."),
            C("The record is deleted", why="Validation rejects the entry. It does not delete records."),
            C("The database shows an error message and does not accept the value", correct=True),
            C("The value is saved as text", why="The field keeps its data type. Validation blocks the value."),
        ], steps=[S("What does a rule do?", text="It checks each entry when it is typed."),
                  S("Result", text="-5 breaks the rule, so a message appears and the entry is rejected.")],
           concept="Validation rules", skill="Application", hint="What does a validation rule do to a value that breaks it?"),
        MC("A school wants a Class field where users can only choose F4, F5 or F6. Which feature is best?", [
            C("A drop-down list", correct=True),
            C("A report", why="A report presents data. It does not control entry."),
            C("A backup", why="A backup copies the database."),
            C("A calculated field", why="A calculated field works out a value from other fields."),
        ], steps=[S("Fixed choices", text="A drop-down list shows only the allowed values, so spelling mistakes cannot happen.")],
           concept="Controlling data entry", skill="Application", hint="Which feature lets the user pick from a fixed set?"),
        MC("A student code must be the letter S followed by three digits, for example S014. Which feature checks this pattern?", [
            C("A report header", why="A header is a title on a printout."),
            C("A primary key", why="A primary key makes values unique. It does not enforce a pattern."),
            C("A foreign key", why="A foreign key links to another table. It does not set a pattern."),
            C("An input mask", correct=True),
        ], steps=[S("Pattern for typed data", text="An input mask forces the entry to follow a pattern.")],
           concept="Input masks", skill="Concept", hint="Which tool forces a fixed pattern of letters and digits?"),
        MC("A report groups sales by category. Grains total 6700 FCFA and Oils total 3900 FCFA. What should the grand total be?", [
            C("10600", correct=True),
            C("2800", why="You subtracted. A grand total adds the subtotals."),
            C("6700", why="This is only the Grains subtotal."),
            C("10000", why="This is a rounded guess. Add exactly: 6700 + 3900."),
        ], steps=[S("Add the subtotals", math=r"6700 + 3900 = 10600")],
           concept="Report totals", skill="Calculation", hint="A grand total combines all the group subtotals."),
        NUM("Palm oil costs 1200 FCFA. A table stores this price in 3 sale rows (duplicated). The price rises to 1300 FCFA and only 2 rows are updated. How many rows still show the old price?", 1,
            steps=[S("Count", text="3 rows hold the price. 2 are updated, so 3 - 2 = 1 row still shows 1200."),
                   S("Meaning", text="The table is now inconsistent: the same product has two prices.")],
            concept="Duplicate data", skill="Reasoning", hint="Subtract the rows updated from the rows that hold the price."),
        MC("Which is the best way to avoid duplicate data about customers' addresses?", [
            C("Type each address carefully in every record", why="This still stores copies, and a change must be made in many places."),
            C("Store each address once in a Customers table and link other tables with a foreign key", correct=True),
            C("Put all the records in one very large table", why="One large table repeats the same details many times."),
            C("Use a larger font in the form", why="Font size has no effect on duplicate data."),
        ], steps=[S("Store a fact once", text="Keep the address in one Customers table."),
                  S("Link", text="Other tables hold only the CustomerID as a foreign key.")],
           concept="Duplicate data", skill="Concept", hint="Where should a fact be stored so that it changes in one place?"),
        MC("Which is the safest backup plan for a school database?", [
            C("Keep a copy in another folder on the same computer", why="A virus, theft or hard disk failure would destroy both copies."),
            C("Never back up because the data is already saved", why="Saving does not protect against loss or damage of the disk."),
            C("Copy the database to a flash drive kept in a different place, and update the copy every week", correct=True),
            C("Print the table once a year", why="A rare printout cannot restore the database and is out of date."),
        ], steps=[S("Separate place", text="A backup must survive whatever destroys the original."),
                  S("Regular", text="Update it often, so little work is lost.")],
           concept="Backups", skill="Application", hint="Where should the copy be kept, and how often should it be updated?"),
    ]))

# ------------------------------------------------------------------ Set 4
SETS.append(practice_set(
    module=EXAM, topic=PAPER3,
    title="Paper 3 lab habits, word processing and spreadsheets",
    lesson="ict-paper-3-word-processing-and-spreadsheet-tasks",
    questions=[
        MC("You sit down at a practical paper. What should you do first?", [
            C("Start typing task 1 at once", why="Some tasks depend on others. Reading first avoids wasted work."),
            C("Read the whole paper and plan your time", correct=True),
            C("Print every file", why="Print only what the tasks ask for, at the end."),
            C("Close the instructions and work from memory", why="Details such as file names and font sizes are marked. Follow the sheet."),
        ], steps=[S("Plan before you act", text="Read all the tasks, note the marks and divide your time.")],
           concept="Working in the lab", skill="Application", hint="What helps you share your time between tasks?"),
        MC("Which habit best protects your work from a power cut?", [
            C("Save only at the end of the paper", why="A power cut before the end would lose everything."),
            C("Leave the file called Document1", why="An unclear name may not be found by the examiner, and it does not protect the work."),
            C("Save early and often, using the file names given", correct=True),
            C("Save only after the last task is printed", why="By then, a power cut may already have destroyed hours of work."),
        ], steps=[S("Save early", text="Save as soon as you create the file."),
                  S("Save often", text="Press Ctrl and S every few minutes.")],
           concept="Working in the lab", skill="Application", hint="How often should you save?"),
        NUM("A practical paper has 100 marks in all. You have 60 minutes and keep 10 minutes for checking. Sharing the other time by marks, how many minutes should you spend on a task worth 40 marks?", 20,
            steps=[S("Time for the tasks", math=r"60 - 10 = 50 \text{ minutes}"),
                   S("Minutes per mark", math=r"50 \div 100 = 0.5"),
                   S("Task worth 40 marks", math=r"40 \times 0.5 = 20 \text{ minutes}")],
            concept="Time planning", skill="Calculation", hint="First remove the checking time, then share what is left by the marks.", tolerance=0),
        MC("A task asks for lines of text with a space of 1.5 between lines. Which word processing feature do you use?", [
            C("Line spacing", correct=True),
            C("Page break", why="A page break starts a new page."),
            C("Find and replace", why="This changes words, not spacing."),
            C("Insert table", why="A table arranges data in rows and columns."),
        ], steps=[S("Match the wording", text="Space between lines is line spacing.")],
           concept="Word processing features", skill="Application", hint="Which setting controls the gap between lines?"),
        MC("Page numbers must appear at the bottom of every page. Where do you insert them?", [
            C("In the header", why="The header is at the top."),
            C("In the first paragraph", why="Text in the body appears once, not on every page."),
            C("In the footer", correct=True),
            C("In a table", why="A table does not repeat on every page."),
        ], steps=[S("Repeated at the bottom", text="Text or fields that repeat on every page sit in the footer.")],
           concept="Word processing features", skill="Application", hint="Which area repeats at the bottom of every page?"),
        MC("Cells D2 to D4 hold amounts. Which formula puts their total in D5?", [
            C("=D2:D4", why="A range alone is not a calculation."),
            C("D2+D3+D4", why="A formula must start with an equals sign."),
            C("=ADD(D2:D4)", why="Spreadsheets use SUM, not ADD."),
            C("=SUM(D2:D4)", correct=True),
        ], steps=[S("Start with an equals sign", text="Every formula begins with =."),
                  S("Use SUM on the range", text="=SUM(D2:D4) adds D2, D3 and D4.")],
           concept="Spreadsheet formulas", skill="Application", hint="Which function adds a range?"),
        MC("A mark is in D2. Which formula shows Pass when D2 is 20 or more, and Fail otherwise?", [
            C('=IF(D2>20,"Pass","Fail")', why="Greater than 20 leaves out a mark of exactly 20."),
            C('=IF(D2>=20,"Pass","Fail")', correct=True),
            C('=IF(D2<=20,"Pass","Fail")', why="This passes low marks, the opposite."),
            C('=SUM(D2,"Pass","Fail")', why="SUM adds numbers. It cannot choose between words."),
        ], steps=[S("The test", text="D2>=20 means 20 or more."),
                  S("Results", text="If true show Pass, otherwise Fail.")],
           concept="IF function", skill="Application", hint="Does 20 or more include 20 itself?"),
        NUM("Cell D2 holds 8400 and cell F1 holds a rate of 10 percent. A formula in E2 multiplies D2 by F1, with F1 as an absolute reference (a dollar sign before the F and before the 1). What value does E2 show?", 840,
            steps=[S("Convert the rate", math=r"10\% = 0.10"),
                   S("Multiply", math=r"8400 \times 0.10 = 840")],
            concept="Absolute references", skill="Calculation", hint="Change 10 percent into a decimal first.", tolerance=0),
    ]))

# ------------------------------------------------------------------ Set 5
SETS.append(practice_set(
    module=EXAM, topic=PAPER3,
    title="Paper 3 database and web design tasks",
    lesson="ict-paper-3-database-and-web-design-tasks",
    questions=[
        MC("A database task asks you to create a table, enter records, and run a query. In which order should you work?", [
            C("Query, records, table", why="A query needs a table and records to work on."),
            C("Records, table, query", why="You cannot enter records before the table exists."),
            C("Table, records, query", correct=True),
            C("Report, table, records", why="The report comes last, from the query or table."),
        ], steps=[S("Each step needs the one before", text="Build the table, enter the data, then query it.")],
           concept="Database task order", skill="Application", hint="What must exist before you can enter or query data?"),
        MC("A query must show only BookTitle and DateBorrowed, but the criterion is on the Returned field. How do you stop Returned appearing in the results?", [
            C("Delete the Returned field from the table", why="This destroys data. The query only needs to hide the field."),
            C("Leave Returned in the query. Examiners will not mind", why="A query showing extra fields may lose marks."),
            C("Sort the Returned field", why="Sorting does not hide a field."),
            C("Clear the Show box under Returned in the design grid", correct=True),
        ], steps=[S("Use the field for the criterion only", text="Keep Returned in the grid so the criterion works."),
                  S("Hide it", text="Clear its Show box so the result shows only the two fields asked.")],
           concept="Query design", skill="Application", hint="You need the field for the condition but not in the output."),
        MC("A query must show the oldest loans first. How should DateBorrowed be sorted?", [
            C("Descending", why="Descending puts the latest date first."),
            C("Ascending", correct=True),
            C("It does not need sorting", why="The records would appear in the order they were entered, which may not be by date."),
            C("Alphabetically by BookTitle", why="The task asks for dates, not titles."),
        ], steps=[S("Oldest means earliest date", text="Ascending order puts the earliest date first.")],
           concept="Sorting in a query", skill="Application", hint="Which date is the smallest: the oldest or the newest?"),
        NUM("A report lists two sales lines for Grains: 3 kg of rice at 700 FCFA a kg, and 2 litres of palm oil at 1200 FCFA a litre. What is the subtotal of the report in FCFA?", 4500,
            steps=[S("First line", math=r"3 \times 700 = 2100"),
                   S("Second line", math=r"2 \times 1200 = 2400"),
                   S("Subtotal", math=r"2100 + 2400 = 4500")],
            concept="Report totals", skill="Calculation", hint="Work out each line amount first, then add.", tolerance=0),
        MC("Which HTML makes the words Our news a link to the page news.html?", [
            C('<link href="news.html">Our news</link>', why="The link tag in the head connects stylesheets. Links in the page use the a tag."),
            C('<a src="news.html">Our news</a>', why="The a tag uses href, not src."),
            C('<a href="news.html">Our news</a>', correct=True),
            C('<p href="news.html">Our news</p>', why="A paragraph tag does not make a link."),
        ], steps=[S("Anchor tag", text="Use the a tag with an href attribute holding the file name."),
                  S("Link text", text="The words between the tags are what the reader clicks.")],
           concept="HTML links", skill="Application", hint="Which tag makes a link, and which attribute holds its address?"),
        MC("Where is the line that connects style.css to the page placed?", [
            C("In the body, after the last paragraph", why="Stylesheet links belong in the head."),
            C("In the footer text", why="This is not a place for a link tag."),
            C('In the head, as <link rel="stylesheet" href="style.css">', correct=True),
            C("In the file name of the page", why="The page is connected by a link tag, not through its name."),
        ], steps=[S("Where metadata goes", text="Stylesheet links are placed in the head element."),
                  S("The tag", text='<link rel="stylesheet" href="style.css"> names the file.')],
           concept="Linking CSS", skill="Concept", hint="Which part of the page holds information about the page?"),
        MC("A CSS rule is: h1 { color: #00008b; text-align: center; }. What does it do to the heading?", [
            C("Makes it dark blue and left aligned", why="The value center places the heading in the middle."),
            C("Makes it dark blue and centred", correct=True),
            C("Makes the page background dark blue", why="The selector h1 affects only the heading."),
            C("Makes it centred and underlined", why="Colour is set, not underline."),
        ], steps=[S("Read the selector", text="h1 targets level-one headings."),
                  S("Read each declaration", text="color sets the text colour (dark blue). text-align with the value center centres it.")],
           concept="CSS rules", skill="Interpretation", hint="Read each property and its value."),
        MC("You saved style.css but the page shows no styling. What is the best first check?", [
            C("That the page has enough text", why="Amount of text does not affect whether CSS loads."),
            C("That the page has a picture", why="A picture is unrelated to loading CSS."),
            C("That the computer is plugged in", why="The page opens, so the computer is fine; the problem is the link."),
            C("That the link tag names style.css correctly and the file is in the same folder", correct=True),
        ], steps=[S("Find the connection", text="If the stylesheet is not linked or cannot be found, none of its rules apply."),
                  S("Check", text="Look at the href, the file name spelling and the folder, then save and refresh.")],
           concept="Testing a web page", skill="Reasoning", hint="Which line joins the page and the stylesheet?"),
    ]))
