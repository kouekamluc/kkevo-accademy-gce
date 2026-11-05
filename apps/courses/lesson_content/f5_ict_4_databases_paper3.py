"""Form 5 ICT: Databases (3 lessons) and Paper 3 practical (2 lessons), one practice set each."""

from .dsl import *  # noqa: F403

COURSE = ("ict", "form-5")

PRACTICAL = "Practical skills"
DATABASES = "Databases"
EXAM = "Examination"
PAPER3 = "Paper 3 (practical)"

LESSONS = []

# ------------------------------------------------------------------ Lesson 1
LESSONS.append(lesson(
    module=PRACTICAL,
    topic=DATABASES,
    title="Tables, fields, records and keys",
    slug="ict-database-tables-fields-and-keys",
    minutes=22,
    summary="Understand what a relational database is, design a table with suitable fields and data types, choose a primary key, and link two tables with a foreign key.",
    objectives=[
        "Define database, table, field, record and data type",
        "Choose suitable field names and data types for a table",
        "Explain what a primary key is and choose a good one",
        "Link two tables using a foreign key and describe a one-to-many relationship",
    ],
    key_concepts=["Database", "Table", "Field", "Record", "Data type", "Primary key", "Foreign key", "Relationship"],
    blocks=[
        H("Introduction"),
        T("The library of a secondary school in Bamenda keeps its books and borrowers in a big register. "
          "To find which students have not returned a book, the librarian must read hundreds of lines."),
        T("A **database** stores the same information in an organised way. The computer can then find, sort and count "
          "it in seconds. Microsoft Access, LibreOffice Base and MySQL are examples of database software. "
          "In the exam you may use any relational database program available in your lab."),
        D("A **database** is an organised collection of related data. In a **relational database** the data is kept "
          "in several **tables** that are linked to each other.", title="Definition: database"),
        H("Tables, fields and records"),
        T("A table looks like a spreadsheet grid. Each column holds one kind of information. Each row holds everything "
          "about one thing."),
        KEY("Parts of a table", "Learn these four words well. They appear in many exam questions.", cards=[
            ["Table", "A set of data about one kind of thing, for example Students."],
            ["Field", "A column. It holds one item of information, such as Surname."],
            ["Record", "A row. It holds all the fields for one student, one book or one product."],
            ["Data type", "The kind of value a field may hold: text, number, date or yes/no."],
        ]),
        CODE("""
Students table
StudentID | Surname | FirstName | Class
----------+---------+-----------+------
S001      | Nfor    | Grace     | F5A
S002      | Tabi    | Paul      | F5B
S003      | Mbah    | Esther    | F5A
""", "text", title="Listing 1: a Students table with 4 fields and 3 records"),
        T("In Listing 1 there are 4 fields (StudentID, Surname, FirstName, Class) and 3 records (one per student). "
          "The header row holds the field names. It is not a record."),
        H("Choosing data types"),
        T("When you create a table, you give each field a name and a **data type**. The right type saves space, "
          "stops wrong entries and lets you sort and calculate correctly. Names such as Access and Base use slightly "
          "different words, but the ideas are the same."),
        KEY("Common data types", "Choose the type that matches how the data will be used.", cards=[
            ["Text", "Names, addresses, classes. Also phone numbers and codes, because you never add them up."],
            ["Number", "Quantities, marks and prices that you may calculate with."],
            ["Date/Time", "Dates such as DateBorrowed. Dates then sort in the correct order."],
            ["Yes/No (Boolean)", "Only two possible values, such as Returned: Yes or No."],
        ]),
        T("A phone number such as 677 12 34 56 should be text. If it were a number, a leading zero or a plus sign "
          "could be lost."),
        H("The primary key"),
        D("A **primary key** is a field (or set of fields) whose value is **different for every record**. "
          "It identifies exactly one record. A primary key can never be empty.", title="Definition: primary key"),
        T("Surname is a poor primary key, because two students can share a surname. A first name is just as bad. "
          "Instead we create a unique code, such as StudentID. Many programs can fill such a code in for you with an "
          "AutoNumber field."),
        EX("Worked example 1: designing a market stall table",
           intro="Amina sells foodstuffs at a market stall in Douala. Design a Products table for her. "
                 "Give the field names, data types and the primary key.", steps=[
            S("List the facts to store about each product", text="A code, the name, the category, the price in FCFA and the quantity in stock."),
            S("Choose field names", text="ProductID, Name, Category, Price, Quantity. Use short names with no spaces."),
            S("Choose data types", text="ProductID: number (or text code). Name: text. Category: text. Price: number. Quantity: number."),
            S("Choose the primary key", text="ProductID. Two products can have the same price or even the same name in different sizes, but each ProductID is unique."),
        ]),
        QUIZ("Which field is the best primary key for a Students table?",
             ["Surname", "Class", "StudentID", "FirstName"], 2,
             "StudentID is a unique code. Each student has a different one, so it identifies one record.",
             hint="Which field can never be the same for two different students?",
             feedback=["Two students can have the same surname.", "Many students are in the same class.", "",
                       "Many students can share a first name."]),
        H("Linking tables with a foreign key"),
        T("Suppose the librarian also records which student borrowed which book. If every loan stored the student's "
          "surname, first name and class again, the same details would be typed many times. "
          "Instead we make a second table, Loans, and link it to Students."),
        D("A **foreign key** is a field in one table that holds the primary key values of another table. "
          "It creates the link, called a **relationship**, between the two tables.", title="Definition: foreign key"),
        CODE("""
Loans table
LoanID | StudentID | BookTitle         | DateBorrowed | Returned
-------+-----------+-------------------+--------------+---------
1      | S001      | Things Fall Apart | 2026-10-02   | No
2      | S002      | The River Between | 2026-10-05   | Yes
3      | S001      | Weep Not, Child   | 2026-10-09   | Yes
4      | S003      | Things Fall Apart | 2026-10-12   | No
""", "text", title="Listing 2: a Loans table linked to Students by StudentID"),
        T("In Loans, LoanID is the primary key. StudentID is the foreign key, because its values come from the "
          "primary key of Students. Student S001 appears in two loans. So one student can have **many** loans, "
          "but each loan belongs to **one** student. This is a **one-to-many relationship**."),
        IMG("f5i-er-library.svg",
            alt="Entity relationship sketch: a Students box with StudentID as primary key linked to a Loans box with LoanID as primary key and StudentID as foreign key. The link is marked one to many.",
            caption="Figure 1. An entity relationship sketch. PK means primary key and FK means foreign key."),
        CODE("""
CREATE TABLE Students (
  StudentID  VARCHAR(10) PRIMARY KEY,
  Surname    VARCHAR(30),
  FirstName  VARCHAR(30),
  Class      VARCHAR(10)
);

CREATE TABLE Loans (
  LoanID       INTEGER PRIMARY KEY,
  StudentID    VARCHAR(10),
  BookTitle    VARCHAR(60),
  DateBorrowed DATE,
  Returned     BOOLEAN,
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
""", "sql", title="Listing 3: the same design written in SQL",
             caption="In Access or Base you do the same in Design View, then enter the records in Datasheet View. You do not have to type SQL to use a database."),
        TIP("Create the table on the one side (Students) first and enter its records first. A loan cannot refer to a "
            "StudentID that does not exist yet."),
        H("Common mistakes"),
        MISTAKE("Using a field that can repeat as the primary key",
                "Names, classes and prices can repeat. Use a unique code field."),
        MISTAKE("Storing phone numbers as numbers",
                "Phone numbers are not used in calculations. Store them as text."),
        MISTAKE("Calling the header row a record",
                "The field names are the headings. Only the rows of data are records."),
        MISTAKE("Mixing up primary and foreign keys",
                "StudentID is the primary key in Students but a foreign key in Loans. The same field can play different roles in different tables."),
        QUIZ("In the Loans table, StudentID links each loan to a record in Students. In Loans, StudentID is a:",
             ["Primary key", "Foreign key", "Record", "Data type"], 1,
             "A field that holds the primary key values of another table is a foreign key.",
             hint="Where does this field's data come from?",
             feedback=["The primary key of Loans is LoanID. StudentID repeats in Loans, so it cannot be its primary key.", "",
                       "A record is a whole row, not one field.", "A data type tells what kind of value a field holds."]),
        H("Practice questions"),
        PQ("Define the terms (a) field, (b) record, (c) primary key. Use a pharmacy Medicines table as your example.",
           "(a) A field is one column of data, for example MedicineName or Price. (b) A record is one row holding all the data about one medicine. "
           "(c) A primary key is a field with a different value in every record, for example MedicineCode. It identifies each medicine."),
        PQ("Suggest a data type for each field of a Customers table: CustomerID, FullName, PhoneNumber, DateJoined, IsMember. Explain the choice for PhoneNumber.",
           "CustomerID: text or AutoNumber. FullName: text. PhoneNumber: text, because it is not used in calculations and may start with a zero or a plus sign. "
           "DateJoined: date. IsMember: Yes/No."),
        PQ("A school keeps a Teachers table (TeacherID, Name, Subject) and a Classes table (ClassID, ClassName, TeacherID). "
           "State the primary key of each table and the foreign key. Describe the relationship.",
           "Teachers: primary key TeacherID. Classes: primary key ClassID. The foreign key is TeacherID in Classes, because it holds values from the primary key of Teachers. "
           "One teacher can be linked to many classes, so the relationship is one-to-many from Teachers to Classes."),
        H("Summary"),
        SUM("A relational database stores data in linked tables. A table has fields (columns) and records (rows).",
            "Each field has a data type: text, number, date or yes/no. Choose the type that fits how you will use the data.",
            "A primary key has a different value in every record. A unique code is better than a name.",
            "A foreign key holds the primary key values of another table and creates the relationship.",
            "One student with many loans is a one-to-many relationship. Draw it as an entity relationship sketch."),
    ],
))

# ------------------------------------------------------------------ Lesson 2
LESSONS.append(lesson(
    module=PRACTICAL,
    topic=DATABASES,
    title="Queries: sorting, searching and calculating",
    slug="ict-database-queries-sort-search-calculate",
    minutes=24,
    summary="Build queries that select fields, search with AND and OR criteria, sort results and calculate a new field, and read the same queries written in SQL.",
    objectives=[
        "Explain what a query is and choose the fields to show",
        "Write criteria using comparison operators, AND and OR",
        "Sort the results in ascending or descending order, on one or two fields",
        "Create a calculated field and write the matching SQL SELECT statement",
    ],
    key_concepts=["Query", "Criteria", "AND", "OR", "Sort order", "Calculated field", "SQL"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you built tables. A table can hold hundreds of records. "
          "Amina's stall in Douala has a Products table. She wants to know: which goods are almost sold out, "
          "which are the most expensive, and how much money is tied up in stock?"),
        T("She does not read every row. She asks the database. A **query** is a question you ask a database. "
          "It shows only the fields and records you need."),
        D("A **query** selects, from one or more tables, the fields you want and the records that meet your conditions (the **criteria**). "
          "It can also sort the results and calculate new values. The data stays in the table. The query only shows a view of it.",
          title="Definition: query"),
        H("The sample data"),
        T("All the examples in this lesson use this Products table. Prices are in FCFA."),
        CODE("""
Products
ProductID | Name             | Category   | Price | Quantity
----------+------------------+------------+-------+---------
1         | Rice 1kg         | Grains     |   700 |   40
2         | Beans 1kg        | Grains     |   800 |   25
3         | Palm oil 1L      | Oils       |  1200 |   18
4         | Sugar 1kg        | Sweeteners |   900 |   30
5         | Groundnut oil 1L | Oils       |  1500 |   10
6         | Maize 1kg        | Grains     |   500 |    0
7         | Salt 500g        | Spices     |   300 |   60
8         | Honey 500ml      | Sweeteners |  2500 |    6
""", "text", title="Listing 1: the Products table"),
        H("Selecting fields and sorting"),
        T("In the query design grid of Access or Base, you add the table and choose the fields. "
          "Each chosen field becomes a column in the grid. Under a field you can set **Sort** to Ascending (smallest first, or A to Z) "
          "or Descending (largest first, or Z to A). Behind the scenes the program writes a statement in SQL (Structured Query Language)."),
        KEY("The grid and SQL say the same thing", "You only need one of them in the exam. Use whichever your software gives you.", cards=[
            ["Field row", "SELECT: which fields to show."],
            ["Table row", "FROM: which table to use."],
            ["Criteria row", "WHERE: which records to keep."],
            ["Sort row", "ORDER BY: how to sort. ASC is ascending and DESC is descending."],
        ]),
        CODE("""
SELECT Name, Price
FROM Products
ORDER BY Price DESC;
""", "sql", title="Listing 2: names and prices, most expensive first"),
        CODE("""
Name             | Price
-----------------+------
Honey 500ml      | 2500
Groundnut oil 1L | 1500
Palm oil 1L      | 1200
Sugar 1kg        |  900
Beans 1kg        |  800
Rice 1kg         |  700
Maize 1kg        |  500
Salt 500g        |  300
""", "text", title="Result of Listing 2"),
        H("Searching with criteria"),
        T("A **criterion** is a condition a record must meet to be shown. Use the comparison operators: equals (=), "
          "not equal (<>), greater than (>), less than (<), greater than or equal (>=) and less than or equal (<=). "
          "Text is written in quotes, for example 'Oils'. Numbers have no quotes."),
        T("To use two conditions together:"),
        KEY("AND and OR", "Choose carefully. They give very different results.", cards=[
            ["AND", "Both conditions must be true. In the grid, put both criteria on the same Criteria row."],
            ["OR", "At least one condition must be true. In the grid, put the second criterion on the next row (the 'or' row)."],
        ]),
        EX("Worked example 1: searching with AND and OR",
           intro="Using the Products table, write queries to show (a) the Name, Price and Quantity of grains costing less than 750 FCFA, "
                 "and (b) the Name and Category of products that are oils or cost more than 2000 FCFA.", steps=[
            S("(a) Two conditions that must both be true", text="Category equals 'Grains' AND Price less than 750."),
            S("(a) Check the data", text="Rice 1kg (700) and Maize 1kg (500) are grains under 750. Beans cost 800, so they are left out."),
            S("(b) Either condition may be true", text="Category equals 'Oils' OR Price greater than 2000."),
            S("(b) Check the data", text="Palm oil and Groundnut oil are oils. Honey (2500) costs more than 2000. So three records are shown."),
        ]),
        CODE("""
-- (a) grains under 750 FCFA
SELECT Name, Price, Quantity
FROM Products
WHERE Category = 'Grains' AND Price < 750;

-- (b) oils, or anything over 2000 FCFA
SELECT Name, Category
FROM Products
WHERE Category = 'Oils' OR Price > 2000;
""", "sql", title="Listing 3: queries for worked example 1"),
        CODE("""
Result (a)
Name      | Price | Quantity
----------+-------+---------
Rice 1kg  |   700 |   40
Maize 1kg |   500 |    0

Result (b)
Name             | Category
-----------------+-----------
Palm oil 1L      | Oils
Groundnut oil 1L | Oils
Honey 500ml      | Sweeteners
""", "text", title="Results of Listing 3"),
        QUIZ("Which criteria show the products with 10 or fewer items in stock?",
             ["Quantity < 10", "Quantity <= 10", "Quantity > 10", "Quantity = 10"], 1,
             "Less than or equal to 10 includes 10 itself. In the table it shows Maize (0), Honey (6) and Groundnut oil (10).",
             hint="Does 'or fewer' include 10 itself?",
             feedback=["Less than 10 leaves out the record with exactly 10 (Groundnut oil).", "",
                       "Greater than 10 shows the products with plenty of stock, the opposite.",
                       "Equal to 10 shows only one product."]),
        H("Sorting on two fields"),
        T("Sometimes you sort on a main field and then on a second field to settle ties. "
          "In the design grid, the field further to the left is the main sort. In SQL, list them in order after ORDER BY."),
        CODE("""
SELECT Category, Name, Price
FROM Products
ORDER BY Category ASC, Price DESC;
""", "sql", title="Listing 4: by category A to Z, then dearest first in each category"),
        CODE("""
Category   | Name             | Price
-----------+------------------+------
Grains     | Beans 1kg        |  800
Grains     | Rice 1kg         |  700
Grains     | Maize 1kg        |  500
Oils       | Groundnut oil 1L | 1500
Oils       | Palm oil 1L      | 1200
Spices     | Salt 500g        |  300
Sweeteners | Honey 500ml      | 2500
Sweeteners | Sugar 1kg        |  900
""", "text", title="Result of Listing 4"),
        H("A calculated field"),
        T("A **calculated field** is a new column made by a calculation on other fields. It is not stored in the table. "
          "It is worked out each time the query runs. Amina wants the value of the stock of each product: price multiplied by quantity. "
          "In the grid you type a new field name, a colon, and the calculation, for example StockValue followed by a colon and Price multiplied by Quantity. "
          "In SQL, AS gives the new column its name."),
        EX("Worked example 2: stock value",
           intro="Show each product's Name and its stock value (Price times Quantity), largest value first.", steps=[
            S("Choose the calculation", text="StockValue = Price multiplied by Quantity."),
            S("Work out two values by hand to check", text="Rice: 700 times 40 = 28000. Maize: 500 times 0 = 0."),
            S("Sort", text="Sort the calculated field in descending order so the biggest value comes first."),
            S("Run the query and compare", text="The first row should be Rice 1kg with 28000. See the listings below."),
        ]),
        CODE("""
SELECT Name, Price * Quantity AS StockValue
FROM Products
ORDER BY StockValue DESC;
""", "sql", title="Listing 5: a calculated field"),
        CODE("""
Name             | StockValue
-----------------+-----------
Rice 1kg         |      28000
Sugar 1kg        |      27000
Palm oil 1L      |      21600
Beans 1kg        |      20000
Salt 500g        |      18000
Groundnut oil 1L |      15000
Honey 500ml      |      15000
Maize 1kg        |          0
""", "text", title="Result of Listing 5"),
        TIP("Always check at least one calculated value by hand. If it does not match, you probably used the wrong field."),
        H("Common mistakes"),
        MISTAKE("Mixing up AND and OR",
                "Category = 'Oils' AND Price > 2000 shows no records, because no oil costs more than 2000. Ask yourself: must both be true, or either?"),
        MISTAKE("Putting quotes around numbers or leaving them off text",
                "Write Category = 'Oils' (quotes) and Price < 750 (no quotes)."),
        MISTAKE("Sorting the wrong way round",
                "Ascending means smallest first or A to Z. Descending means largest first or Z to A. Read the question: 'dearest first' is descending."),
        MISTAKE("Typing the result of a calculation into the table",
                "Do not type StockValue into the table. Use a calculated field, so it updates when Price or Quantity change."),
        QUIZ("Which line sorts products from the cheapest to the most expensive?",
             ["ORDER BY Price DESC", "ORDER BY Price ASC", "WHERE Price ASC", "SELECT Price ASC"], 1,
             "ORDER BY Price ASC sorts from the smallest price to the largest.",
             hint="Which clause sorts, and which direction is smallest first?",
             feedback=["DESC puts the largest first, so the most expensive would come first.", "",
                       "WHERE gives a condition. It does not sort.", "SELECT chooses the fields. It does not sort."]),
        H("Practice questions"),
        PQ("A table Products has fields Code, Name, Price and Quantity. Write a query to show the Name and Price of products costing more than 1000 FCFA, from the most expensive to the cheapest.",
           "SELECT Name, Price FROM Products WHERE Price > 1000 ORDER BY Price DESC;"),
        PQ("Using the Products table in Listing 1, which records does this criterion show? Category = 'Grains' AND Quantity > 30",
           "Only Rice 1kg (40 in stock). Beans have 25 and Maize has 0, so they fail the second condition. Both conditions must be true with AND."),
        PQ("Write a query for the Products table that shows Name and a calculated field called NewPrice, which is Price plus 10 percent (multiply Price by 1.1). Give the NewPrice of Rice 1kg.",
           "SELECT Name, Price multiplied by 1.1 AS NewPrice FROM Products (use the multiplication sign between Price and 1.1, and AS to name the new column). For Rice 1kg: 700 multiplied by 1.1 = 770 FCFA."),
        H("Summary"),
        SUM("A query asks a question of the database. It shows chosen fields and the records that meet the criteria.",
            "In SQL: SELECT chooses fields, FROM names the table, WHERE gives the criteria, and ORDER BY sorts (ASC or DESC).",
            "AND needs both conditions true. OR needs at least one true.",
            "Text criteria use quotes. Number criteria do not.",
            "A calculated field is worked out by the query, for example Price multiplied by Quantity. It is not typed into the table."),
    ],
))

# ------------------------------------------------------------------ Lesson 3
LESSONS.append(lesson(
    module=PRACTICAL,
    topic=DATABASES,
    title="Forms, reports and keeping data accurate",
    slug="ict-database-forms-reports-and-accuracy",
    minutes=22,
    summary="Use forms for easy data entry, validation rules and input masks to stop bad data, reports with grouping and totals, and backups. Understand why duplicate data causes errors.",
    objectives=[
        "Explain the purpose of a form and a report",
        "Describe validation rules, input masks and drop-down lists",
        "Describe a report with grouping and totals",
        "Explain why backups matter and why duplicate data causes errors",
    ],
    key_concepts=["Form", "Validation", "Input mask", "Report", "Grouping", "Backup", "Data redundancy"],
    blocks=[
        H("Introduction"),
        T("Amina's helper types new goods into the database all day. Typing straight into a big table is slow and "
          "easy to get wrong. A mistake such as a price of 7000 instead of 700 can cost real money."),
        T("In this lesson you learn how forms make data entry easier, how rules keep the data accurate, "
          "how reports present results for printing, and how to protect the data."),
        H("Forms for data entry"),
        D("A **form** is a screen designed for entering, viewing or editing the records of a table, usually one record at a time. "
          "It shows labels and boxes for the fields.", title="Definition: form"),
        T("A form is friendlier than a plain datasheet. You can add a title, put the fields in a sensible order, "
          "and use drop-down lists or tick boxes. A form can also hide fields the user should not change, such as an automatic ID. "
          "The data you type still goes into the table."),
        H("Keeping data accurate"),
        T("A database is only useful if its data is correct. Two tools stop wrong data being typed."),
        KEY("Two tools that protect data", "Use them together.", cards=[
            ["Validation rule", "A check made when data is entered. Example: Price must be greater than 0. A message appears if the rule is broken."],
            ["Input mask", "A pattern that the entry must follow. Example: a student code must be a letter S followed by 3 digits."],
            ["Drop-down list", "The user picks a value from a fixed list, such as Class: F4, F5 or F6, instead of typing it."],
            ["Required field", "The record cannot be saved if this field is left empty. Primary keys are always required."],
        ]),
        T("Validation checks that data is **reasonable**. It does not prove that it is **true**. "
          "A price of 800 for rice passes the rule 'greater than 0', but it may still be the wrong price. "
          "Checking against the paper source (verification) is a separate step."),
        EX("Worked example 1: choosing the rules",
           intro="For the Loans table, suggest one validation rule or control for each field: LoanID, StudentID, DateBorrowed, Returned.", steps=[
            S("LoanID", text="Use an AutoNumber field, so every ID is unique and nobody types it."),
            S("StudentID", text="Use a drop-down list taken from the Students table, so only existing students can be chosen. Add an input mask if the code has a fixed pattern."),
            S("DateBorrowed", text="Use a date type with a validation rule that the date is not in the future."),
            S("Returned", text="Use a Yes/No field with a default of No. It can only be Yes or No."),
        ]),
        QUIZ("A rule says that Quantity must be a whole number from 0 to 500. What is this called?",
             ["A report", "A validation rule", "A primary key", "A backup"], 1,
             "A validation rule checks data as it is entered and rejects values outside the allowed range.",
             hint="It checks the data when it is typed.",
             feedback=["A report presents data for printing. It does not check entries.", "",
                       "A primary key identifies records. It does not check ranges.", "A backup is a spare copy of the data."]),
        H("Reports"),
        D("A **report** is a formatted printout or screen view of the results of a table or query. "
          "It has a title, headings, page numbers and a neat layout. A report is for reading, not for entering data.",
          title="Definition: report"),
        T("A report can **group** records, for example by Category. It can then work out **totals** (and counts or averages) "
          "for each group and a **grand total** at the end. The report wizard in Access or Base asks which field to group on and which field to sum."),
        T("Here is a short sales table for Amina's stall. It is joined to the Products table to find each amount "
          "(price multiplied by quantity sold). The report groups the amounts by category and adds a subtotal for each group."),
        CODE("""
Sales report: sales of 2 to 4 November 2026

Category: Grains
  Beans 1kg   Qty 4   Amount  3200
  Rice 1kg    Qty 5   Amount  3500
  Rice 1kg    Qty 3   Amount  2100
  Subtotal Grains             8800

Category: Oils
  Groundnut oil 1L   Qty 1   Amount 1500
  Palm oil 1L        Qty 2   Amount 2400
  Palm oil 1L        Qty 3   Amount 3600
  Subtotal Oils               7500

Grand total                  16300
""", "text", title="Listing 1: a grouped report with subtotals and a grand total"),
        CODE("""
SELECT p.Category, SUM(p.Price * s.Qty) AS Subtotal
FROM Sales s
JOIN Products p ON p.ProductID = s.ProductID
GROUP BY p.Category;
""", "sql", title="Listing 2: the totals behind the report",
             caption="Result: Grains 8800, Oils 7500. The grand total is 8800 + 7500 = 16300."),
        TIP("Check a report by adding the subtotals yourself. 8800 + 7500 = 16300, so the grand total is correct."),
        H("Backups and duplicate data"),
        D("A **backup** is a copy of the database stored somewhere else, such as a flash drive, another computer or the cloud. "
          "If the original is lost, damaged or deleted, you restore the copy.", title="Definition: backup"),
        T("Back up regularly, keep the copy in a different place and label it with the date. "
          "A backup kept on the same damaged computer does not help."),
        T("Another danger is **duplicate data**: the same fact stored in many places. This is called data redundancy. "
          "Suppose Amina typed the price of palm oil into every sale row instead of using a Products table:"),
        CODE("""
SaleID | Product     | Price | Qty
-------+-------------+-------+----
1      | Palm oil 1L | 1200  | 2
2      | Palm oil 1L | 1200  | 3
3      | Palm oil 1L | 1200  | 1
""", "text", title="Listing 3: the price is repeated in every row"),
        T("If the price rises to 1300, she must change every row. If she changes only two rows, the table now says "
          "two different prices for the same product. The data is **inconsistent**, and totals will be wrong."),
        T("Splitting the data into linked tables fixes this. The price is stored once, in Products. "
          "Sales only holds the ProductID (the foreign key). One change in Products is then correct everywhere."),
        EX("Worked example 2: spotting the duplication",
           intro="A school Results table repeats each student's full name and class in every subject row. "
                 "Explain two problems and suggest a better design.", steps=[
            S("Problem 1: wasted effort and space", text="The same name and class are typed many times, once for each subject."),
            S("Problem 2: inconsistency", text="If a student moves from F5A to F5B, some rows may be changed and others missed, so the database contradicts itself."),
            S("Better design", text="Keep a Students table (StudentID, Surname, FirstName, Class) and a Results table (ResultID, StudentID, Subject, Mark). Link them with StudentID."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking validation guarantees correct data",
                "Validation only blocks impossible values. A wrong but possible value, such as 800 instead of 700, still gets through. Check against the source."),
        MISTAKE("Keeping the backup in the same place",
                "A backup on the same computer is lost in the same fire, theft or virus. Keep a copy elsewhere."),
        MISTAKE("Typing a total into the table",
                "Totals belong in a query or report, where they are calculated. A typed total becomes wrong when the data changes."),
        MISTAKE("Using a report for data entry",
                "A report is for output only. Use a form to enter data."),
        QUIZ("Why is it better to store a product's price once, in a Products table, than in every sale record?",
             ["It makes the report look nicer", "A price change needs to be made in only one place", "Prices are always text", "It removes the need for a primary key"], 1,
             "With one copy, a change is made once and is correct everywhere. Duplicates can end up different from each other.",
             hint="What happens when the price changes?",
             feedback=["Appearance is not the reason. It is about accuracy.", "",
                       "Prices are numbers, not text.", "Every table still needs a primary key."]),
        H("Practice questions"),
        PQ("State two differences between a form and a report.",
           "A form is used to enter, view or edit records, usually one at a time, and the data goes into the table. "
           "A report is a formatted printout or screen view of results, used for reading and printing, with titles, grouping and totals. You do not enter data in a report."),
        PQ("Describe two ways a database can reduce data entry errors.",
           "Any two of: a validation rule (for example Price greater than 0) rejects impossible values; an input mask forces a pattern such as S followed by three digits; "
           "a drop-down list lets the user pick from fixed choices; a required field stops empty entries; a form with clear labels."),
        PQ("A report lists sales by category. The Grains subtotal is 8800 and the Oils subtotal is 7500. What should the grand total be? What would you check if it showed 15300?",
           "Grand total = 8800 + 7500 = 16300. A value of 15300 is 1000 too small. Check whether a record is missing, a subtotal was entered or calculated wrongly, or a record was filtered out of the query."),
        PQ("Explain why storing the same customer address in many records can cause errors, and say how to avoid it.",
           "When the address changes, some copies may be updated and others missed. The database then holds different addresses for the same customer. "
           "Avoid this by storing the address once in a Customers table and linking other tables to it with a foreign key."),
        H("Summary"),
        SUM("A form is for entering, viewing and editing records. A report is for presenting results, with grouping and totals.",
            "Validation rules, input masks, drop-down lists and required fields stop bad data being entered.",
            "Validation checks that data is reasonable. It does not prove it is true.",
            "A backup is a separate copy kept in a different place. Make backups regularly.",
            "Duplicate data leads to inconsistent records. Store each fact once and link tables with keys."),
    ],
))


# ------------------------------------------------------------------ Lesson 4
LESSONS.append(lesson(
    module=EXAM,
    topic=PAPER3,
    title="Paper 3 practical: working in the lab, word processing and spreadsheet tasks",
    slug="ict-paper-3-word-processing-and-spreadsheet-tasks",
    minutes=22,
    summary="Plan your time in a practical lab, save your work safely, and use a checklist for typical word processing and spreadsheet tasks.",
    objectives=[
        "Describe good habits for working in a timed practical lab",
        "Plan time and name and save files sensibly",
        "Match common word processing tasks to the right feature",
        "Choose and check the right spreadsheet formula, function and reference",
    ],
    key_concepts=["Practical lab", "Time plan", "File naming", "Formatting and layout", "Formula and function", "Absolute reference"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is the practical paper. You sit at a computer and complete tasks with the software. "
          "The examiner marks the files you produce, and sometimes printouts of them. "
          "It tests whether you can use the features, not only whether you know their names."),
        T("The number of tasks and the length of the paper are fixed by the GCE Board. "
          "Check the current GCE Board instructions and your teacher's notes for the exact details. "
          "This lesson gives you habits that help whatever the paper looks like."),
        H("Working well in a timed lab"),
        KEY("Six habits for the practical lab", "Practise them in every computer lesson, so they become automatic.", cards=[
            ["1. Read the whole paper first", "Read every task before you start. Some tasks use files from an earlier one."],
            ["2. Make a time plan", "Divide the time by the tasks, using the marks as a guide. Note when you should finish each task."],
            ["3. Save early and often", "Save as soon as you create a file. Press Ctrl and S every few minutes. A power cut in Bamenda can come at any time."],
            ["4. Name files exactly", "Use the file names the paper gives, or a clear name such as spreadsheet_stall_prices. Never leave a file called Document1."],
            ["5. Follow instructions to the letter", "Font, size, colour, alignment and wording are marked. Do exactly what is asked."],
            ["6. Check before you print or hand in", "Test your formulas, proofread your text and print the right pages. Check headers, footers and your name if requested."],
        ]),
        T("If you are stuck on a step, move on and come back. Do not spend half the paper on one task. "
          "Marks are given for each correct step, so a partly finished task still earns marks."),
        EX("Worked example 1: a time plan",
           intro="A practical lab has 3 tasks and you have 90 minutes (an example only: check the real time). "
                 "Task 1 is worth 20 marks, task 2 is worth 40 marks and task 3 is worth 40 marks. Plan your time, keeping 10 minutes at the end for checking.", steps=[
            S("Time for the tasks", text="90 minutes minus 10 minutes for checking leaves 80 minutes."),
            S("Share by marks", text="There are 100 marks in all, so 80 minutes divided by 100 marks gives 0.8 minutes per mark."),
            S("Task 1", text="20 marks times 0.8 = 16 minutes."),
            S("Tasks 2 and 3", text="40 marks times 0.8 = 32 minutes each."),
            S("Check the total", text="16 + 32 + 32 = 80, plus 10 for checking gives 90 minutes."),
        ]),
        H("Typical word processing tasks"),
        T("Most word processing tasks ask you to type or open a document, format it, and add a few features. "
          "Match each wording of the task to the correct feature."),
        CODE("""
Task wording                         | Feature to use
-------------------------------------+--------------------------------
Make the title centred and bold      | Alignment, Bold
Set the body text to 12 pt, justified| Font size, Justify
Space between lines of 1.5           | Line spacing
Set margins of 2.5 cm                | Page layout, Margins
Put the school name on every page    | Header
Number the pages                     | Footer or page number field
Make a list of items with bullets    | Bullets or numbering
Show information in rows and columns | Insert table
Put a picture beside the text        | Insert picture, text wrapping
Fix spelling mistakes                | Spell check, then proofread
Find and change a word everywhere    | Find and replace
Move the heading to a new page       | Page break
""", "text", title="Listing 1: matching tasks to word processing features"),
        TIP("Spell check does not catch a correctly spelt wrong word, such as 'form' for 'from'. Read your text yourself as well."),
        H("Word processing checklist"),
        CODE("""
[ ] Typed text matches the source exactly (spelling, punctuation)
[ ] Title: font, size, alignment as asked
[ ] Body: font, size, line spacing and alignment as asked
[ ] Margins and page orientation as asked
[ ] Header and footer correct, page numbers present
[ ] Lists, tables and pictures placed and sized correctly
[ ] Spell check run and text proofread
[ ] File saved with the correct name, then printed if asked
""", "text", title="Listing 2: before you leave a word processing task"),
        H("Typical spreadsheet tasks"),
        T("Spreadsheet tasks usually give you data to enter, then ask for formulas, functions, formatting and perhaps a chart. "
          "Remember that a formula starts with an equals sign. Always use cell references, not typed numbers, "
          "so the answer updates when the data changes."),
        CODE("""
   A        B     C           D
1  Item     Qty   Unit price  Amount
2  Rice     12    700         8400
3  Oil      5     1200        6000
4  Sugar    8     900         7200
5  Total                      21600
""", "text", title="Listing 3: a stall's sales sheet"),
        CODE("""
D2:  =B2*C2        (copy down to D4)
D5:  =SUM(D2:D4)   (21600)
E2:  =D2*F1        (amount times a rate stored in F1)
""", "text", title="Listing 4: formulas for Listing 3",
             caption="Check by hand: 12 times 700 = 8400. 5 times 1200 = 6000. 8 times 900 = 7200. The total is 21600."),
        KEY("Choosing the right function", "Say in words what you need, then pick the function.", cards=[
            ["SUM", "Adds a range: =SUM(D2:D4)."],
            ["AVERAGE, MAX, MIN", "Mean, largest and smallest in a range."],
            ["COUNT", "Counts the cells in a range that contain numbers."],
            ["IF", "Gives one result if a test is true and another if not: =IF(D2>=7000,\"High\",\"Low\")."],
            ["ROUND", "Rounds a number to a given number of decimal places."],
        ]),
        T("When you copy a formula down, references change automatically: B2 becomes B3, then B4. "
          "This is a **relative reference**. If a cell must stay the same, such as a rate in F1, "
          "put a dollar sign before the column letter and the row number to make it **absolute**. "
          "The formula in E2 then becomes =D2 times the absolute reference to F1, and it can be copied down safely."),
        CODE("""
E2:  =D2*$F$1      (the rate stays fixed when copied down)
Rate in F1: 10%    E2 = 8400 * 0.10 = 840
""", "text", title="Listing 5: an absolute reference"),
        EX("Worked example 2: a pass or fail column",
           intro="Three students have two test marks each, out of 20. Ada has 14 and 16, Bih has 9 and 12, Cho has 18 and 17. "
                 "Add a Total column, a Result column that shows Pass when the total is 20 or more (otherwise Fail), and the average total.", steps=[
            S("Enter the data", text="Names in column A, Test 1 in B and Test 2 in C, starting at row 2."),
            S("Total in D2", text="=B2+C2, copied down to D4. The totals are 30, 21 and 35."),
            S("Result in E2", text="=IF(D2>=20,\"Pass\",\"Fail\"), copied down. Ada: Pass. Bih: Pass (21 is 20 or more). Cho: Pass."),
            S("Average total", text="=AVERAGE(D2:D4) gives (30 + 21 + 35) divided by 3 = 28.67 to 2 decimal places."),
            S("Check", text="Change Bih's second mark to 5 and the total becomes 14. The Result changes to Fail. This shows the formulas work."),
        ]),
        H("Spreadsheet checklist"),
        CODE("""
[ ] Data typed exactly, in the right cells
[ ] Every calculation is a formula using cell references
[ ] Formulas copied down or across correctly
[ ] Absolute references used where a cell must stay fixed
[ ] Number formats as asked (currency, decimals, percent)
[ ] Column widths wide enough: no #### signs
[ ] Headings bold, borders or shading as asked
[ ] Chart has a title, axis labels and the right type
[ ] Sheet saved, then printed (check the print preview)
""", "text", title="Listing 6: before you leave a spreadsheet task"),
        H("Common mistakes"),
        MISTAKE("Typing the answer instead of a formula",
                "If you type 21600, nothing updates when the data changes, and you lose the marks for the formula. Always use =SUM(D2:D4)."),
        MISTAKE("Not saving until the end",
                "A crash or power cut before you save loses all your work. Save at the start and every few minutes."),
        MISTAKE("Forgetting an absolute reference",
                "Copying a formula that multiplies D2 by F1 down moves F1 to F2, F3 and so on, and the results are wrong. Fix the cell with the dollar signs."),
        MISTAKE("Ignoring small instructions",
                "Items such as font size, alignment, a header or a column width carry marks. Tick each one off the task sheet."),
        QUIZ("A task says 'Put the school name at the top of every page'. Which feature do you use?",
             ["Page break", "Header", "Footer", "Find and replace"], 1,
             "A header repeats text at the top of every page.",
             hint="Text that repeats on every page sits in a special area at the edge.",
             feedback=["A page break moves text to the next page.", "",
                       "A footer repeats at the bottom of the page, not the top.", "Find and replace changes words. It does not repeat them on pages."]),
        QUIZ("Which formula adds the cells D2 to D4?",
             ["=SUM(D2:D4)", "=D2:D4", "SUM(D2+D4)", "=ADD(D2,D4)"], 0,
             "=SUM(D2:D4) adds every cell in the range D2 to D4.",
             hint="A formula starts with an equals sign and uses a function name.",
             feedback=["", "A range alone is not a calculation. It needs a function such as SUM.",
                       "A formula must begin with an equals sign. The plus also adds only D2 and D4, missing D3.",
                       "There is no ADD function in standard spreadsheets."]),
        H("Practice questions"),
        PQ("You have 60 minutes in a practical lab with 3 tasks. Give four habits that will help you gain marks.",
           "Read the whole paper first; make a time plan; save early and often with the correct file names; follow the instructions exactly (fonts, sizes, alignment); "
           "check and proofread before printing. Any four, with a short reason."),
        PQ("A sheet has Quantity in B2:B6 and Unit price in C2:C6. Write a formula for the amount in D2, and a formula for the total of the amounts in D2:D6.",
           "D2: B2 multiplied by C2 (an equals sign, then B2, the multiplication sign, then C2), copied down to D6. The total in D7 is =SUM(D2:D6)."),
        PQ("Cell F1 holds a discount rate of 5 percent. Row 2 has an amount in D2. Write a formula in E2 for the discount that can be copied down. Explain the reference to F1.",
           "E2: D2 multiplied by F1, with a dollar sign before the F and before the 1. Those dollar signs make F1 an absolute reference, so it does not move when the formula is copied to E3, E4 and so on. D2 stays relative so it changes to D3, D4."),
        PQ("List four word processing features you would use to produce a notice with a centred bold title, a bulleted list, a footer with page numbers and 2.5 cm margins.",
           "Alignment (centre) and Bold for the title; Bullets for the list; Footer with a page number field; Page layout (Margins) set to 2.5 cm on every side."),
        H("Summary"),
        SUM("Check the current GCE Board instructions for the length and number of tasks. Read the whole paper first.",
            "Plan your time using the marks, keep time to check, and save early and often with the correct file names.",
            "Match each instruction to a feature: alignment, spacing, margins, header and footer, bullets, tables, pictures, page breaks.",
            "In a spreadsheet use formulas with cell references, the right function (SUM, AVERAGE, IF) and absolute references for fixed cells.",
            "Use a checklist for each task and look at the printout before you hand in."),
    ],
))

# ------------------------------------------------------------------ Lesson 5
LESSONS.append(lesson(
    module=EXAM,
    topic=PAPER3,
    title="Paper 3 practical: database and web design tasks",
    slug="ict-paper-3-database-and-web-design-tasks",
    minutes=24,
    summary="Work through timed database tasks (table, data entry, query, report) and web design tasks (build, style and test a simple page), with checklists and common slips.",
    objectives=[
        "Complete a database task from table design to a printed query and report",
        "Build and style a simple web page that meets a task sheet",
        "Test a page in a browser and a database query against the data",
        "Use checklists to avoid the common slips that lose marks",
    ],
    key_concepts=["Table creation", "Data entry", "Query and report", "Web page", "Styling", "Testing"],
    blocks=[
        H("Introduction"),
        T("Paper 3 may include a database task and a web design task. In the previous lesson you saw the habits for the lab and the "
          "word processing and spreadsheet tasks. This lesson covers the other two. "
          "Check the current GCE Board instructions for the exact tasks and the software you may use."),
        T("Each task is a short chain of steps, and every step has marks. If you follow the sheet in order and test as you go, "
          "you collect marks steadily."),
        H("A database task"),
        T("A typical database task has five steps. Read this example of a task sheet."),
        CODE("""
Task: Bamenda Community Library
1. Create a database named library_yourname.
2. Create a table Loans with these fields:
   LoanID (primary key), StudentID, BookTitle, DateBorrowed, Returned (Yes/No).
3. Enter the 6 records given on the sheet.
4. Create a query that shows BookTitle and DateBorrowed of books
   not yet returned, with the oldest loan first. Save it as qry_notreturned.
5. Create a report from the query with the title "Books not returned",
   then print the table, the query and the report.
""", "text", title="Listing 1: an example database task sheet"),
        EX("Worked example 1: following the task sheet",
           intro="Explain how you would complete steps 2 to 5 of the task in Listing 1.", steps=[
            S("Step 2: build the table", text="Open Design View. Type each field name. Set the data types: LoanID AutoNumber or number, StudentID text, BookTitle text, DateBorrowed date, Returned Yes/No. Set LoanID as the primary key. Save the table as Loans."),
            S("Step 3: enter the data", text="Open Datasheet View or a form. Type the six records exactly as printed. Dates must be typed as dates, and the Returned box ticked only where the sheet says Yes."),
            S("Step 4: build the query", text="Add the Loans table. Choose BookTitle and DateBorrowed. Under Returned type the criteria No (or untick it) and uncheck Show. Set DateBorrowed to sort Ascending. Run it and compare with the data. Save as qry_notreturned."),
            S("Step 5: make the report", text="Use the report wizard on the query. Choose both fields, set the title Books not returned, and check the layout. Print the table, query and report."),
        ]),
        CODE("""
SELECT BookTitle, DateBorrowed
FROM Loans
WHERE Returned = FALSE
ORDER BY DateBorrowed ASC;
""", "sql", title="Listing 2: the query in SQL",
             caption="Some programs write this condition as Returned = 0 or Returned = No. Use what your software shows in the query design."),
        CODE("""
[ ] Table name and field names exactly as the task sheet says
[ ] Correct data type for every field; primary key set
[ ] Every record typed accurately: compare with the sheet
[ ] Query shows only the fields asked and the right records
[ ] Sorting is in the direction asked
[ ] Query and report saved with the names given
[ ] Report has the title; layout is readable; nothing cut off
[ ] Table, query and report printed (check the print preview)
""", "text", title="Listing 3: database task checklist"),
        H("A web design task"),
        T("A web design task asks you to build a simple page in HTML, style it with CSS, and test it in a browser. "
          "You may use a text editor or the editor your lab provides. The page must be saved with the right file name, "
          "such as index.html, in the right folder."),
        CODE("""
Task: Page for Mbouda Youth Club
1. Create index.html with the title "Mbouda Youth Club".
2. Add a main heading and a short paragraph about the club.
3. Add a list of three activities.
4. Add a link to the page contact.html.
5. Style the page with a stylesheet style.css: a light background,
   a centred heading in dark blue, and the text in Arial.
6. Test the page in a browser and print it.
""", "text", title="Listing 4: an example web design task sheet"),
        CODE("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mbouda Youth Club</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Mbouda Youth Club</h1>
  <p>We meet every Saturday to learn, play and serve our town.</p>
  <ul>
    <li>Football</li>
    <li>Computer lessons</li>
    <li>Clean-up days</li>
  </ul>
  <p><a href="contact.html">Contact us</a></p>
</body>
</html>
""", "html", title="Listing 5: index.html"),
        CODE("""
body {
  background-color: #f0f8ff;
  font-family: Arial, sans-serif;
}
h1 {
  color: #00008b;
  text-align: center;
}
""", "css", title="Listing 6: style.css",
             caption="Keep both files in the same folder. The link in the page uses the file name exactly as saved."),
        EX("Worked example 2: testing the page",
           intro="After saving index.html and style.css, explain how you test the page and what you do if the heading is not blue.", steps=[
            S("Open the page", text="Open index.html in a browser. Do not just look at the code. The browser shows what the examiner will see."),
            S("Check each requirement", text="Title in the browser tab, heading, paragraph, three list items, link text, light background, centred blue heading, Arial text."),
            S("Test the link", text="Click Contact us. If contact.html does not exist yet, create it or check the spelling of the file name."),
            S("If the heading is not blue", text="Check that style.css is in the same folder, that the href in the link tag matches its name, that the rule uses the selector h1, and that each line ends with a semicolon. Save and refresh the browser."),
        ]),
        CODE("""
[ ] Files saved with the correct names in the same folder
[ ] DOCTYPE, html, head (with title) and body present
[ ] Required headings, paragraphs, lists, images and links added
[ ] Image files exist; alt text given if asked
[ ] Stylesheet linked in the head; the rules match the task
[ ] Page opened in a browser and every link clicked
[ ] Spelling checked in the text
[ ] Printed as requested
""", "text", title="Listing 7: web design task checklist"),
        H("Common slips that lose marks"),
        MISTAKE("Not saving the query or report with the name given",
                "The examiner looks for the exact names. Rename the objects if you saved them under the default names."),
        MISTAKE("Typing a data entry error",
                "One wrong letter or number in a record can make the query give a wrong answer. After entering, read the table against the sheet."),
        MISTAKE("Showing extra fields in the query",
                "A query asked to show two fields should show only those two. Uncheck Show on fields used only for a criterion."),
        MISTAKE("Wrong file name or location for web pages",
                "A page saved as Index.html.txt or in a different folder from its stylesheet will not be linked correctly. Check names and extensions."),
        MISTAKE("Not testing before printing",
                "Open the page and run the query to see the real result. Checking only the code or the design view is not enough."),
        QUIZ("A query is asked to show the oldest loans first. The date field is sorted:",
             ["Descending", "Ascending", "Not sorted but grouped", "Using a validation rule"], 1,
             "Ascending sorts dates from the earliest to the latest, so the oldest loan comes first.",
             hint="Oldest means earliest date.",
             feedback=["Descending puts the latest date first, the opposite.", "",
                       "Grouping is not sorting.", "A validation rule checks data entry. It does not sort."]),
        QUIZ("After you create style.css, the page shows no styling. What should you check first?",
             ["That the link tag in the head names style.css correctly", "That the paragraph has more words", "That the page has an image", "That the title is bold"], 0,
             "If the stylesheet is not linked correctly, none of its rules apply. Check the file name and the href.",
             hint="Which line connects the page to the stylesheet?",
             feedback=["", "The length of the paragraph does not affect whether CSS loads.",
                       "An image is not needed for CSS to work.", "The title is shown in the tab and is not bold by CSS."]),
        H("Practice questions"),
        PQ("A task asks for a query that shows the Name and Price of products costing less than 1000 FCFA, cheapest first. Write the steps in query design, or the SQL.",
           "Add the Products table; choose Name and Price; under Price type the criteria less than 1000 and set Sort to Ascending; run and check; save with the name given. "
           "SQL: SELECT Name, Price FROM Products WHERE Price < 1000 ORDER BY Price ASC;"),
        PQ("List four checks you make before you print a database report.",
           "The title is correct; the right fields and records are shown; the grouping and totals are correct (add the subtotals yourself); the layout is readable with nothing cut off; "
           "the object is saved with the name given; the print preview looks right. Any four."),
        PQ("Write the HTML to make the text Welcome a level-one heading, followed by a link with the words Our news that opens news.html.",
           "<h1>Welcome</h1> and <a href=\"news.html\">Our news</a>."),
        PQ("A student sets the colour of a heading in style.css, but the browser does not show it. Give three things to check.",
           "The link tag in the head names style.css exactly and the file is in the same folder; the CSS rule uses the right selector (h1) with a colon and a semicolon; "
           "the file has been saved and the browser page refreshed. Also check that there are no spelling errors in the property names."),
        H("Summary"),
        SUM("Follow the task sheet in order. Name every table, query, report and file exactly as asked.",
            "Database task: create the table with correct data types and a primary key, enter the data accurately, run and save the query, build and print the report.",
            "Web task: write the HTML, link a CSS file, save both files in the same folder, then test in a browser.",
            "Test as you go: compare query results with the data, click every link, and read the printout.",
            "Use the checklists. Most lost marks are small slips, not missing knowledge. Check the current GCE Board instructions for the exact tasks."),
    ],
))
