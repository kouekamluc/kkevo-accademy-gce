"""Upper Sixth Computer Science (A Level): in-depth lessons for Relational Databases, Object-Oriented
Programming, the Software Project and the Examination practice paper.

KKEVO draft material for review (not Board text). Every SQL query, Python program, closure and dependency
check in these lessons was run when the lessons were written.
"""

from .dsl import *  # noqa: F403

COURSE = ("computer-science", "upper-sixth")

LESSONS = []

# ---------------------------------------------------------------------------
# Relational algebra 1: select and project
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Relational algebra",
    title="Select and project: choosing rows and columns",
    slug="csd-ra-select-project",
    minutes=20,
    summary="Use the two single-relation operators of relational algebra, selection (rows) and projection (columns), evaluate them on a small table and write the matching SQL.",
    objectives=[
        "Describe a relation using the words tuple, attribute, degree and cardinality",
        "Evaluate a selection with simple and combined conditions",
        "Evaluate a projection and explain why duplicate tuples disappear",
        "Combine selection and projection from the inside out and write the equivalent SQL",
    ],
    key_concepts=["Relation", "Tuple", "Attribute", "Degree", "Cardinality", "Selection", "Projection"],
    blocks=[
        H("Introduction"),
        T("A wholesaler at the Bamenda food market keeps a list of goods in stock. The manager asks two kinds of question: \"Which items cost more than 700 FCFA?\" (some rows) and \"What categories do we sell?\" (one column). Relational algebra gives a precise name to each kind of question."),
        T("Relational algebra is a small set of operators. Each one takes one or two relations and produces a new relation, so the output of one operator can be the input of the next. Every SQL query you will write later is built from these operators."),
        D("A **relation** is a table with named columns. Each column is an **attribute**. Each row is a **tuple**. The number of attributes is the **degree** of the relation and the number of tuples is its **cardinality**.",
          title="Relation, tuple, attribute", note="In a relation, no two tuples are identical and the order of the rows does not matter. Every value is atomic: one single value per cell."),
        CODE('''
STOCK
Item      Category   Price  Qty
Tomato    Vegetable  800    40
Plantain  Starch     1500   25
Cassava   Starch     500    60
Pepper    Vegetable  1200   15
Banana    Fruit      300    80
''', "text", title="Table 1: the relation STOCK (degree 4, cardinality 5)"),
        H("Selection: choosing rows"),
        D(r"**Selection** $\sigma_{c}(R)$ keeps only the tuples of $R$ for which the condition $c$ is true. All the attributes are kept. The result has the same degree as $R$ and the same number of tuples or fewer.",
          title="Selection (sigma)", formula=r"\sigma_{\text{Category}=\text{'Starch'}}(\text{STOCK})"),
        T(r"Conditions compare an attribute with a value or with another attribute, using $=$, $\neq$, $<$, $>$, $\leq$, $\geq$. Conditions can be joined with $\wedge$ (AND), $\vee$ (OR) and $\neg$ (NOT)."),
        EX("Worked example 1: selection", intro=r"Evaluate $\sigma_{\text{Price}>700 \wedge \text{Qty}<30}(\text{STOCK})$.", steps=[
            S("Test each tuple against both conditions", text="Tomato: 800 > 700 is true but 40 < 30 is false. Plantain: 1500 > 700 and 25 < 30 are both true. Cassava: 500 > 700 is false. Pepper: 1200 > 700 and 15 < 30 are both true. Banana: 300 > 700 is false."),
            S("Keep the tuples that pass", text="Plantain and Pepper pass. All four attributes are kept."),
            S("Write the result", text="(Plantain, Starch, 1500, 25) and (Pepper, Vegetable, 1200, 15). Degree 4, cardinality 2."),
        ]),
        H("Projection: choosing columns"),
        D(r"**Projection** $\pi_{a_1, a_2, \ldots}(R)$ keeps only the listed attributes of every tuple. Because a relation cannot contain two identical tuples, any duplicates created by dropping columns are removed.",
          title="Projection (pi)", formula=r"\pi_{\text{Category}}(\text{STOCK})"),
        EX("Worked example 2: projection and duplicates", intro=r"Evaluate $\pi_{\text{Category}}(\text{STOCK})$ and say how many tuples the result has.", steps=[
            S("Keep only the Category column", text="The five rows give Vegetable, Starch, Starch, Vegetable, Fruit."),
            S("Remove duplicate tuples", text="Vegetable and Starch each appear twice. A relation holds each tuple once."),
            S("Write the result", text="{Vegetable, Starch, Fruit}: degree 1, cardinality 3."),
        ]),
        CODE('''
SELECT DISTINCT Category FROM STOCK;

Category
---------
Vegetable
Starch
Fruit
(3 rows)
''', "sql", title="Listing 1: the same projection in SQL (run in sqlite3)"),
        TIP("SQL keeps duplicates unless you write DISTINCT. Relational algebra removes them automatically. Without DISTINCT the query above would return 5 rows."),
        H("Combining operators"),
        T("Because every operator returns a relation, you can nest them. Evaluate from the inside out: the innermost bracket first. Selection usually goes inside and projection outside, because projection throws away the columns that the condition may still need."),
        EX("Worked example 3: select then project", intro=r"Find the names of the items that cost more than 700 FCFA and have fewer than 30 in stock: $\pi_{\text{Item}}(\sigma_{\text{Price}>700 \wedge \text{Qty}<30}(\text{STOCK}))$.", steps=[
            S("Evaluate the selection first", text="From worked example 1 the selection gives Plantain and Pepper (both with all four attributes)."),
            S("Apply the projection", text="Keep only Item: {Plantain, Pepper}."),
            S("Write the equivalent SQL", text="SELECT Item FROM STOCK WHERE Price > 700 AND Qty < 30;  This returns Plantain and Pepper when run in sqlite3."),
        ]),
        CODE('''
SELECT Item, Price FROM STOCK WHERE Price > 700;

Item      Price
--------  -----
Tomato    800
Plantain  1500
Pepper    1200
(3 rows)
''', "sql", title="Listing 2: pi Item,Price ( sigma Price>700 (STOCK) )"),
        MISTAKE("Mixing up sigma and pi", r"$\sigma$ chooses rows (it filters) and $\pi$ chooses columns. In SQL the word SELECT matches projection, while the condition after WHERE matches selection. The names are confusing, so learn the symbols by what they do."),
        MISTAKE("Selecting on a column that was projected away", r"$\sigma_{\text{Price}>700}(\pi_{\text{Item}}(\text{STOCK}))$ is invalid: after the projection there is no Price attribute. Select first, then project."),
        QUIZ(r"Relation R has degree 5 and cardinality 12. What can you say about $\sigma_c(R)$?",
             ["Degree 5 and cardinality at most 12", "Degree at most 5 and cardinality 12", "Degree 12 and cardinality at most 5", "Degree 5 and cardinality at least 12"], 0,
             "Selection removes rows but never columns, so the degree stays 5. It keeps the rows that meet the condition, so the cardinality is 12 or fewer.",
             hint="Selection filters rows. What happens to the columns?",
             feedback=["", "That describes projection: columns may be dropped, but selection keeps every column.", "Degree and cardinality are swapped.", "Selection can only keep or remove rows, never add them."]),
        QUIZ(r"Using Table 1, how many tuples does $\pi_{\text{Category}}(\text{STOCK})$ contain?",
             ["5", "3", "2", "1"], 1,
             "There are three different categories: Vegetable, Starch and Fruit. Duplicates are removed.",
             hint="List the Category value of each row, then cross out repeats.",
             feedback=["That counts the duplicates. A relation never holds the same tuple twice.", "", "Only two categories appear twice. The result has every different value once, which is three.", "That would be the case only if all items were in one category."]),
        H("Practice questions"),
        PQ(r"Using Table 1, evaluate $\sigma_{\text{Category}=\text{'Vegetable'} \vee \text{Price}<400}(\text{STOCK})$.",
           "A tuple passes if it is a vegetable or costs less than 400. Tomato and Pepper are vegetables. Banana costs 300. The result is (Tomato, Vegetable, 800, 40), (Pepper, Vegetable, 1200, 15) and (Banana, Fruit, 300, 80). Plantain and Cassava fail both parts."),
        PQ(r"Write a relational algebra expression for the names and quantities of all starch items, and evaluate it.",
           r"$\pi_{\text{Item, Qty}}(\sigma_{\text{Category}=\text{'Starch'}}(\text{STOCK}))$. The selection keeps Plantain and Cassava. The projection gives (Plantain, 25) and (Cassava, 60)."),
        PQ(r"The relation R(Name, Town) has the tuples (Ayuk, Bali), (Ndi, Bali), (Fotso, Bafang). State the result of $\pi_{\text{Town}}(R)$ and explain why it has fewer tuples than R.",
           "The result is {Bali, Bafang}: two tuples. Bali appears twice in the Town column. A relation cannot contain duplicate tuples, so one copy is removed."),
        PQ("Write an SQL query equivalent to the relational algebra expression in Practice question 2, and say what DISTINCT would change.",
           "SELECT Item, Qty FROM STOCK WHERE Category = 'Starch'; It returns Plantain 25 and Cassava 60. DISTINCT is not needed here because the Item values are all different. It matters only when projected columns can repeat, for example selecting only Category."),
        SUM(r"A relation has attributes (columns) and tuples (rows). Degree is the number of attributes; cardinality is the number of tuples.",
            r"Selection $\sigma$ filters rows with a condition and keeps all attributes.",
            r"Projection $\pi$ keeps chosen attributes and removes duplicate tuples.",
            "Evaluate nested expressions from the inside out: select first, then project.",
            "In SQL, WHERE does the selection, SELECT does the projection and DISTINCT removes duplicates."),
    ],
))

# ---------------------------------------------------------------------------
# Relational algebra 2: product and join
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Relational algebra",
    title="Cartesian product and joins: combining two relations",
    slug="csd-ra-product-join",
    minutes=22,
    summary="Combine relations with the Cartesian product, theta join and natural join, work out the degree and cardinality of the result and see which tuples a join loses.",
    objectives=[
        "Form the Cartesian product of two relations and state its degree and cardinality",
        "Explain why a join is a product followed by a selection",
        "Evaluate a theta join and a natural join on small tables",
        "Identify tuples that disappear from a join and write the matching SQL",
    ],
    key_concepts=["Cartesian product", "Theta join", "Equi-join", "Natural join", "Common attribute", "Dangling tuple"],
    blocks=[
        H("Introduction"),
        T("A cocoa and coffee cooperative at Bali keeps farmer details in one relation and the deliveries in another. To print a payment list the secretary needs the farmer's name next to each delivery. That means combining two relations. Relational algebra has one basic way to do it (the Cartesian product) and one practical way (the join)."),
        CODE('''
FARMER                        DELIVERY                CROP
FID  FName   Village          FID  Crop    Kg         Crop    PricePerKg
F1   Ayuk    Bali             F1   Cocoa   120        Cocoa   1000
F2   Fotso   Bafang           F1   Coffee  80         Coffee  1200
F3   Mbarga  Obala            F2   Cocoa   200        Maize   200
F4   Ndi     Bali             F4   Maize   150
''', "text", title="Table 1: the relations used in this lesson"),
        H("Cartesian product"),
        D(r"The **Cartesian product** $R \times S$ pairs every tuple of $R$ with every tuple of $S$. If $R$ has degree $a$ and cardinality $m$, and $S$ has degree $b$ and cardinality $n$, then $R \times S$ has degree $a + b$ and cardinality $m \times n$.",
          title="Cartesian product", formula=r"\text{FARMER} \times \text{DELIVERY}"),
        EX("Worked example 1: size of a product", intro=r"Find the degree and cardinality of $\text{FARMER} \times \text{DELIVERY}$ and describe the problem with the result.", steps=[
            S("Degree", text="FARMER has 3 attributes and DELIVERY has 3, so the product has 3 + 3 = 6 attributes. Both have an attribute called FID, so they are written FARMER.FID and DELIVERY.FID."),
            S("Cardinality", text="FARMER has 4 tuples and DELIVERY has 4, so the product has 4 × 4 = 16 tuples (confirmed by running SELECT COUNT(*) FROM FARMER, DELIVERY in sqlite3)."),
            S("The problem", text="Most of the 16 tuples are nonsense, for example Ayuk (F1) paired with the delivery of F2. Only 4 of them describe a real delivery by its own farmer."),
        ]),
        H("Joins: a product that keeps the sensible pairs"),
        D(r"A **theta join** $R \bowtie_{c} S$ is a product followed by a selection: $R \bowtie_{c} S = \sigma_{c}(R \times S)$. When the condition is an equality between attributes it is called an **equi-join**.",
          title="Theta join and equi-join", formula=r"\text{FARMER} \bowtie_{\text{FARMER.FID}=\text{DELIVERY.FID}} \text{DELIVERY}"),
        D(r"A **natural join** $R \bowtie S$ is an equi-join on all attributes that have the same name in both relations, with each common attribute shown only once.",
          title="Natural join", note="The common attribute is usually a primary key in one relation and a foreign key in the other."),
        EX("Worked example 2: a natural join", intro=r"Evaluate $\text{FARMER} \bowtie \text{DELIVERY}$ using the tables above.", steps=[
            S("Find the common attribute", text="FID is the only attribute name in both relations."),
            S("Match tuples with equal FID", text="F1 matches two deliveries (Cocoa 120 and Coffee 80). F2 matches one. F4 matches one. F3 (Mbarga) matches none."),
            S("Write the result", text="Four tuples with five attributes (FID, FName, Village, Crop, Kg): (F1, Ayuk, Bali, Cocoa, 120), (F1, Ayuk, Bali, Coffee, 80), (F2, Fotso, Bafang, Cocoa, 200), (F4, Ndi, Bali, Maize, 150)."),
            S("Notice what is missing", text="Mbarga does not appear at all, because he has no delivery to be matched with."),
        ]),
        CODE('''
SELECT * FROM FARMER NATURAL JOIN DELIVERY;

FID  FName  Village  Crop    Kg
---  -----  -------  ------  ---
F1   Ayuk   Bali     Cocoa   120
F1   Ayuk   Bali     Coffee  80
F2   Fotso  Bafang   Cocoa   200
F4   Ndi    Bali     Maize   150
(4 rows)
''', "sql", title="Listing 1: the natural join run in sqlite3"),
        T("A theta join can use any comparison (less than, greater than, not equal), not only equality. For example, a join of two price lists could pair every item with every item that is cheaper. In practice most joins are equi-joins on a foreign key."),
        H("Joining three relations"),
        EX("Worked example 3: farmers, deliveries and prices", intro=r"List each farmer's name with the price per kg of each crop delivered, for deliveries above 100 kg: $\pi_{\text{FName, PricePerKg}}(\sigma_{\text{Kg}>100}(\text{FARMER} \bowtie \text{DELIVERY} \bowtie \text{CROP}))$.", steps=[
            S("First join", text="FARMER ⋈ DELIVERY gives the four tuples above."),
            S("Second join on Crop", text="Joining with CROP adds PricePerKg: Cocoa 1000, Coffee 1200, Maize 200. We now have 4 tuples and 6 attributes."),
            S("Select Kg > 100", text="Keeps Ayuk's Cocoa 120, Fotso's Cocoa 200 and Ndi's Maize 150. Ayuk's Coffee 80 is dropped."),
            S("Project FName and PricePerKg", text="(Ayuk, 1000), (Fotso, 1000), (Ndi, 200). The same result appeared when this query was run in sqlite3."),
        ]),
        CODE('''
SELECT FName, PricePerKg
FROM FARMER
NATURAL JOIN DELIVERY
NATURAL JOIN CROP
WHERE Kg > 100;

FName  PricePerKg
-----  ----------
Ayuk   1000
Fotso  1000
Ndi    200
(3 rows)
''', "sql", title="Listing 2: a three-way join"),
        TIP("In SQL, JOIN ... ON a.key = b.key is safer than NATURAL JOIN, because a natural join silently uses every column with the same name, and a new column added later can change the result."),
        MISTAKE("Forgetting that a join loses unmatched tuples", "A farmer with no delivery (Mbarga) disappears from the natural join. If you need to list all farmers, including those with no delivery, you need an outer join in SQL (LEFT JOIN), which is not a basic relational algebra operator."),
        MISTAKE("Writing FROM A, B with no join condition", "Listing two tables in FROM without a WHERE condition gives the full Cartesian product. With 4 farmers and 4 deliveries that is 16 tuples; with large tables it can be millions of rows."),
        QUIZ(r"Relation R has degree 3 and 6 tuples. Relation S has degree 2 and 7 tuples. What are the degree and cardinality of $R \times S$?",
             ["Degree 5 and cardinality 42", "Degree 6 and cardinality 13", "Degree 5 and cardinality 13", "Degree 6 and cardinality 42"], 0,
             "Attributes are placed side by side, so degrees add: 3 + 2 = 5. Every tuple of R is paired with every tuple of S, so cardinalities multiply: 6 × 7 = 42.",
             hint="Which of the two numbers is added and which is multiplied?",
             feedback=["", "That multiplies the degrees and adds the cardinalities, which is the wrong way round.", "Cardinalities are multiplied for a product, not added.", "Degrees are added, not multiplied."]),
        QUIZ(r"In Table 1, which farmer is missing from $\text{FARMER} \bowtie \text{DELIVERY}$ and why?",
             ["Ayuk, because he has two deliveries", "Fotso, because his village is not Bali", "Mbarga, because no delivery has FID F3", "Ndi, because he shares a village with Ayuk"], 2,
             "A natural join keeps only tuples that have a match. No tuple of DELIVERY has FID = F3, so Mbarga's tuple has nothing to join with.",
             hint="Look for an FID in FARMER that never appears in DELIVERY.",
             feedback=["Ayuk appears twice in the result, once for each delivery.", "Village is not the joining attribute, and Fotso's FID F2 does match a delivery.", "", "Sharing a village has no effect: the join compares FID, not Village."]),
        H("Practice questions"),
        PQ(r"Using Table 1, find the degree and cardinality of $\text{FARMER} \times \text{CROP}$.",
           "FARMER has degree 3 and 4 tuples. CROP has degree 2 and 3 tuples. The product has degree 3 + 2 = 5 and cardinality 4 × 3 = 12."),
        PQ("Write a relational algebra expression for the names of the farmers who delivered cocoa, and evaluate it.",
           r"$\pi_{\text{FName}}(\sigma_{\text{Crop}=\text{'Cocoa'}}(\text{FARMER} \bowtie \text{DELIVERY}))$. The join gives four tuples; the selection keeps the two cocoa deliveries, by F1 and F2. The result is {Ayuk, Fotso}."),
        PQ("Explain the difference between a Cartesian product and an equi-join, and say how they are related.",
           r"A Cartesian product pairs every tuple of one relation with every tuple of the other. An equi-join keeps only the pairs where chosen attributes have equal values. An equi-join is a product followed by a selection: $\sigma_{R.a=S.a}(R \times S)$."),
        PQ(r"Evaluate $\pi_{\text{FName, Village, Crop, Kg}}(\sigma_{\text{Kg}>100}(\text{FARMER} \bowtie \text{DELIVERY}))$.",
           "The natural join has four tuples. Kg > 100 keeps (F1, Cocoa, 120), (F2, Cocoa, 200) and (F4, Maize, 150). Projecting gives (Ayuk, Bali, Cocoa, 120), (Fotso, Bafang, Cocoa, 200) and (Ndi, Bali, Maize, 150)."),
        SUM(r"The Cartesian product $R \times S$ has degree $a+b$ and cardinality $m \times n$.",
            r"A join is a product followed by a selection: $R \bowtie_c S = \sigma_c(R \times S)$.",
            "A natural join matches on all attributes with the same name and shows each once.",
            "Tuples with no match (like a farmer with no delivery) do not appear in the join result.",
            "In SQL, always give a join condition: FROM A, B with no WHERE is a full product."),
    ],
))

# ---------------------------------------------------------------------------
# Relational algebra 3: set operations and combined queries
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Relational algebra",
    title="Union, intersection, difference and combined queries",
    slug="csd-ra-set-operations",
    minutes=22,
    summary="Apply union, intersection and difference to union-compatible relations, then build combined expressions such as 'in A but not in B' and write them in SQL with UNION, INTERSECT and EXCEPT.",
    objectives=[
        "State what makes two relations union-compatible",
        "Evaluate union, intersection and difference on small relations",
        "Use difference to find tuples with no match, such as farmers with no deliveries",
        "Translate combined expressions into SQL and check them by running them",
    ],
    key_concepts=["Union compatibility", "Union", "Intersection", "Difference", "Combined expression"],
    blocks=[
        H("Introduction"),
        T("A school in Limbe has a choir and a drama club. The head teacher asks: \"Who is in either club?\", \"Who is in both?\" and \"Who is in the choir but not in drama?\" These three questions are union, intersection and difference. Unlike a join, they work on two relations that have the same shape."),
        D(r"Two relations are **union-compatible** if they have the same degree and the attributes in each position have the same meaning (domain). The names of the attributes may differ, in which case the result usually takes the names of the first relation.",
          title="Union compatibility", note="CHOIR(Name, Form) and DRAMA(Name, Form) are union-compatible. STUDENT(ID, Name, Town) and CHOIR(Name, Form) are not: the degrees differ."),
        CODE('''
CHOIR                DRAMA
Name    Form         Name    Form
Abena   L6           Bih     U6
Bih     U6           Fomba   U6
Nkeng   U6           Tchoua  L6
Tchoua  L6
''', "text", title="Table 1: two union-compatible relations"),
        KEY("The three set operations", "Each result is again a relation, so duplicates never appear.", cards=[
            [r"Union $R \cup S$", "All tuples that are in R, in S or in both."],
            [r"Intersection $R \cap S$", "Only the tuples that are in both R and S."],
            [r"Difference $R - S$", "The tuples that are in R but not in S."],
        ]),
        EX("Worked example 1: the three operations", intro=r"Using Table 1, find $\text{CHOIR} \cup \text{DRAMA}$, $\text{CHOIR} \cap \text{DRAMA}$, $\text{CHOIR} - \text{DRAMA}$ and $\text{DRAMA} - \text{CHOIR}$.", steps=[
            S("Union", text="Take every tuple and write the ones in both only once: (Abena, L6), (Bih, U6), (Fomba, U6), (Nkeng, U6), (Tchoua, L6). That is 5 tuples."),
            S("Intersection", text="(Bih, U6) and (Tchoua, L6) are in both relations. 2 tuples."),
            S("CHOIR minus DRAMA", text="Start with the four choir tuples and remove Bih and Tchoua: (Abena, L6) and (Nkeng, U6)."),
            S("DRAMA minus CHOIR", text="Start with the three drama tuples and remove Bih and Tchoua: (Fomba, U6). Difference is not commutative: R − S and S − R are different."),
            S("Check by counting", text="4 + 3 − 2 = 5, which matches the 5 tuples of the union. In general |R ∪ S| = |R| + |S| − |R ∩ S|."),
        ]),
        CODE('''
SELECT * FROM CHOIR UNION     SELECT * FROM DRAMA;      -- 5 rows
SELECT * FROM CHOIR INTERSECT SELECT * FROM DRAMA;      -- 2 rows
SELECT * FROM CHOIR EXCEPT    SELECT * FROM DRAMA;      -- 2 rows

Name   Form
-----  ----
Abena  L6
Nkeng  U6
(2 rows)               <- output of the EXCEPT query
''', "sql", title="Listing 1: set operations in SQL (run in sqlite3)"),
        TIP("Some database products write MINUS instead of EXCEPT. The idea is identical. Both UNION and INTERSECT also remove duplicates by default; UNION ALL keeps them."),
        H("Combining operators"),
        T("Real questions mix selection, projection, join and set operations. Break the question into parts, write each part as a small expression and then put the parts together."),
        EX("Worked example 2: in the choir but not in drama, Upper Sixth only", intro=r"Write and evaluate an expression for the Upper Sixth students who are in the choir but not in the drama club.", steps=[
            S("Choir members not in drama", math=r"\text{CHOIR} - \text{DRAMA}", text="(Abena, L6) and (Nkeng, U6)."),
            S("Keep only the Upper Sixth", math=r"\sigma_{\text{Form}=\text{'U6'}}(\text{CHOIR} - \text{DRAMA})", text="Abena is L6, so only (Nkeng, U6) remains."),
            S("Project the name", math=r"\pi_{\text{Name}}(\sigma_{\text{Form}=\text{'U6'}}(\text{CHOIR} - \text{DRAMA})) = \{\text{Nkeng}\}"),
        ]),
        H("Difference finds what has no match"),
        T("A join keeps only tuples that match. To find tuples that do not match, use difference on the key attribute and then join back to get the other details. This is how relational algebra expresses \"farmers who have made no delivery\" (see the cooperative tables in the last lesson)."),
        EX("Worked example 3: farmers with no delivery", intro=r"With FARMER(FID, FName, Village) and DELIVERY(FID, Crop, Kg), find the names of farmers who have no delivery.", steps=[
            S("All farmer keys", math=r"\pi_{\text{FID}}(\text{FARMER}) = \{\text{F1, F2, F3, F4}\}"),
            S("Keys that appear in DELIVERY", math=r"\pi_{\text{FID}}(\text{DELIVERY}) = \{\text{F1, F2, F4}\}"),
            S("Difference", math=r"\pi_{\text{FID}}(\text{FARMER}) - \pi_{\text{FID}}(\text{DELIVERY}) = \{\text{F3}\}", text="Both projections have one attribute (FID), so they are union-compatible."),
            S("Join back for the name", math=r"\pi_{\text{FName}}(\text{FARMER} \bowtie (\pi_{\text{FID}}(\text{FARMER}) - \pi_{\text{FID}}(\text{DELIVERY}))) = \{\text{Mbarga}\}"),
        ]),
        CODE('''
SELECT FID FROM FARMER
EXCEPT
SELECT FID FROM DELIVERY;

FID
---
F3
(1 row)
''', "sql", title="Listing 2: the key of the farmer with no delivery"),
        MISTAKE("Using set operations on relations that are not union-compatible", "CHOIR UNION FARMER makes no sense: the degrees differ. Project both relations down to compatible attributes first, as in worked example 3."),
        MISTAKE("Treating difference as symmetric", "CHOIR − DRAMA gives Abena and Nkeng. DRAMA − CHOIR gives Fomba. Always check which relation comes first."),
        TIP(r"Intersection can be written with difference: $R \cap S = R - (R - S)$. Check with Table 1: CHOIR − (CHOIR − DRAMA) = CHOIR − {Abena, Nkeng} = {Bih, Tchoua}, which is the intersection."),
        QUIZ(r"Relation R has 6 tuples, relation S has 5 tuples, and 2 tuples are in both. How many tuples does $R \cup S$ have?",
             ["11", "9", "7", "3"], 1,
             "Add the tuples and subtract the ones counted twice: 6 + 5 − 2 = 9.",
             hint="The tuples in both relations are counted twice if you simply add 6 and 5.",
             feedback=["That adds 6 + 5 and forgets that the 2 common tuples are written only once in a relation.", "", "That subtracts the 2 common tuples twice.", "The union has at least as many tuples as the larger relation, which has 6."]),
        QUIZ("Which expression finds the names of the choir members who are not in the drama club?",
             [r"$\pi_{\text{Name}}(\text{DRAMA} - \text{CHOIR})$", r"$\pi_{\text{Name}}(\text{CHOIR}) \cap \pi_{\text{Name}}(\text{DRAMA})$", r"$\pi_{\text{Name}}(\text{CHOIR} - \text{DRAMA})$", r"$\pi_{\text{Name}}(\text{CHOIR} \cup \text{DRAMA})$"], 2,
             "Difference with CHOIR first gives choir members who are not in drama; projecting Name gives {Abena, Nkeng}.",
             hint="Which relation must come first in a difference to keep the choir members?",
             feedback=["The relations are the wrong way round: this gives the drama members who are not in the choir.", "That is the intersection: members of both clubs.", "", "That is the union: members of either club."]),
        H("Practice questions"),
        PQ("Using Table 1, evaluate the intersection of CHOIR and DRAMA and explain why (Abena, L6) is not in it.",
           "The intersection is {(Bih, U6), (Tchoua, L6)}. (Abena, L6) is in CHOIR but there is no tuple (Abena, L6) in DRAMA, so it is not in both."),
        PQ("List the tuples of the union of CHOIR and DRAMA, and state its cardinality using a formula as a check.",
           "(Abena, L6), (Bih, U6), (Fomba, U6), (Nkeng, U6), (Tchoua, L6): 5 tuples. Check: |CHOIR| + |DRAMA| − |CHOIR ∩ DRAMA| = 4 + 3 − 2 = 5."),
        PQ(r"Write a relational algebra expression for the names of the students who are in exactly one of the two clubs, and evaluate it.",
           r"$\pi_{\text{Name}}((\text{CHOIR} - \text{DRAMA}) \cup (\text{DRAMA} - \text{CHOIR}))$. CHOIR − DRAMA = {Abena, Nkeng}; DRAMA − CHOIR = {Fomba}. The union is {Abena, Nkeng, Fomba}. Bih and Tchoua are in both, so they are left out."),
        PQ("Give the SQL for the farmers with no delivery using EXCEPT, and explain why a plain join cannot find them.",
           "SELECT FID FROM FARMER EXCEPT SELECT FID FROM DELIVERY; returns F3. A join keeps only tuples that find a match, so a farmer with no delivery never appears in it. Difference finds the keys that are in one relation but missing from the other."),
        SUM("Union, intersection and difference need union-compatible relations: same degree and matching attribute meanings.",
            r"$R \cup S$: in either; $R \cap S$: in both; $R - S$: in R but not in S.",
            r"Difference is not symmetric, and $|R \cup S| = |R| + |S| - |R \cap S|$.",
            "Use difference on key attributes to find tuples that have no match, then join back for the details.",
            "SQL uses UNION, INTERSECT and EXCEPT (MINUS in some products)."),
    ],
))

# ---------------------------------------------------------------------------
# Normalization 1: functional dependencies, keys and anomalies
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Normalization",
    title="Functional dependencies, keys and update anomalies",
    slug="csd-nf-functional-dependencies",
    minutes=24,
    summary="Read and write functional dependencies, find candidate keys with the attribute-closure method and show the update, insertion and deletion anomalies that a badly designed table causes.",
    objectives=[
        "Define a functional dependency and state its determinant and dependent attributes",
        "Test a proposed dependency against sample data and against the real-world rule",
        "Find a candidate key by computing attribute closure",
        "Give an example of an update, an insertion and a deletion anomaly",
    ],
    key_concepts=["Functional dependency", "Determinant", "Attribute closure", "Candidate key", "Prime attribute", "Update anomaly", "Insertion anomaly", "Deletion anomaly"],
    blocks=[
        H("Introduction"),
        T("A computer training centre in Bafoussam records every student's course in one big table: the student, the course, the tutor and the mark. It looks convenient, but the same tutor's name is typed again for each student. Sooner or later a typing error or a change of name leaves the table contradicting itself."),
        T("Normalization is the cure. It starts with one question: which attributes determine which? The answer is a set of **functional dependencies**."),
        CODE('''
STUDENT_COURSE
StudentID  StudentName  CourseID  CourseTitle  TutorID  TutorName  Mark
S1         Abena        C1        Databases    T1       Mr Tabi    78
S1         Abena        C2        Networks     T2       Mrs Ewane  64
S2         Bih          C1        Databases    T1       Mr Tabi    55
S3         Nkeng        C3        Web Design   T3       Mr Njoh    71
''', "text", title="Table 1: one table for everything"),
        H("Functional dependencies"),
        D("Attribute (or set of attributes) B is **functionally dependent** on A, written A → B, if every value of A is linked to exactly one value of B. A is the **determinant**. If two tuples agree on A, they must agree on B.",
          title="Functional dependency", note="Read A → B as \"A determines B\"."),
        T("In Table 1 the rules of the centre give these dependencies:"),
        KEY("The dependencies of STUDENT_COURSE", "Each one comes from a rule of the business, not from the sample data alone.", cards=[
            ["StudentID → StudentName", "Each student number belongs to one student."],
            ["CourseID → CourseTitle, TutorID", "Each course has one title and one tutor."],
            ["TutorID → TutorName", "Each tutor number belongs to one tutor."],
            ["StudentID, CourseID → Mark", "A mark belongs to one student on one course. It needs both."],
        ]),
        IMG("al-csd-fd-arrows.svg",
            "Diagram of the attributes of STUDENT_COURSE. StudentID points to StudentName. CourseID points to CourseTitle and TutorID. TutorID points to TutorName. StudentID and CourseID together point to Mark.",
            caption="Figure 1. The functional dependencies of Table 1."),
        MISTAKE("Deciding a dependency from the sample alone", "The four rows of Table 1 would also be consistent with TutorName → TutorID, because the names happen to be different. Data can disprove a dependency (two rows agree on A but differ on B) but it cannot prove one. Decide from the rule of the business: two tutors could share a name, so TutorName does not determine TutorID."),
        H("Keys and attribute closure"),
        D("A **candidate key** is a smallest set of attributes that determines every attribute of the relation. The **primary key** is the candidate key chosen to identify the tuples. An attribute that is part of any candidate key is **prime**; the others are **non-prime** (non-key) attributes.",
          title="Candidate key"),
        D("The **closure** A+ of a set of attributes A is the set of all attributes that A determines, directly or by chaining dependencies. A is a candidate key if A+ is every attribute and no smaller subset of A has that property.",
          title="Attribute closure", note="Method: start with A+ = A. Repeat: if the left side of a dependency is inside A+, add its right side to A+. Stop when nothing new is added."),
        EX("Worked example 1: finding the key by closure", intro="Find the candidate key of STUDENT_COURSE(StudentID, StudentName, CourseID, CourseTitle, TutorID, TutorName, Mark).", steps=[
            S("Try StudentID alone", text="StudentID+ = {StudentID, StudentName}. It stops there, so StudentID is not a key."),
            S("Try CourseID alone", text="CourseID+ = {CourseID} then CourseTitle and TutorID, then TutorName (because TutorID → TutorName). That gives {CourseID, CourseTitle, TutorID, TutorName}. No Mark, no StudentName: not a key."),
            S("Try both together", text="{StudentID, CourseID}+ starts as both. StudentID adds StudentName. CourseID adds CourseTitle, TutorID, then TutorName. The pair adds Mark. All 7 attributes are reached."),
            S("Check it is smallest", text="Neither attribute alone is enough (steps 1 and 2), so the pair is minimal. The candidate key is (StudentID, CourseID). Running the same closure routine in Python gave the same answer."),
        ]),
        T("Notice that CourseID → TutorID and TutorID → TutorName together give CourseID → TutorName. This chaining of dependencies is called **transitivity**, and it is the cause of a problem you will meet in the next lessons."),
        H("Why a bad design causes anomalies"),
        T("In Table 1 every fact about a tutor, a course or a student is repeated or tied to an enrolment. This leads to three kinds of fault called **anomalies**."),
        EX("Worked example 2: the three anomalies in Table 1", intro="Show an update, an insertion and a deletion anomaly in Table 1.", steps=[
            S("Update anomaly", text="Mr Tabi appears in two rows. If his name changes and only one row is edited, the table says both \"Mr Tabi\" and a new name for TutorID T1. The data now contradicts itself."),
            S("Insertion anomaly", text="The centre starts a new course C4 with tutor T4, but no student has enrolled yet. The primary key includes StudentID, which cannot be empty, so the course cannot be recorded."),
            S("Deletion anomaly", text="Nkeng leaves and that row is deleted. That was the only row about Web Design and Mr Njoh, so the course and the tutor vanish from the database."),
            S("The common cause", text="Several different facts (about students, courses, tutors and marks) are stored in one relation. Each fact should be stored once."),
        ]),
        TIP("Storing each fact once is the goal of normalization. In the next lessons the same table is split into smaller tables, step by step, without losing any information."),
        QUIZ("In Table 1, StudentID alone determines which attributes?",
             ["StudentName only", "StudentName and Mark", "CourseTitle and TutorName", "Every attribute"], 0,
             "StudentID → StudentName is the only dependency whose determinant is StudentID alone. A student can have several courses and several marks, so StudentID does not determine them.",
             hint="A student can take more than one course. Which attributes would then have more than one value?",
             feedback=["", "A student can have a different mark on each course, so StudentID alone does not determine Mark.", "Course details depend on the course, and a student can be on more than one course.", "Then StudentID would be a key, but we found its closure has only two attributes."]),
        QUIZ("A relation R(A, B, C, D) has the dependencies A → B, B → C and C, D → A. Which set of attributes has a closure containing all four attributes?",
             ["A", "B, D", "C, D", "Both B, D and C, D"], 3,
             "B, D: B gives C, then C and D give A, and A gives B, so all four are reached. C, D gives A, A gives B, so all four are reached.",
             hint="Compute the closure of each set by repeatedly adding what the dependencies allow.",
             feedback=["A+ = {A, B, C}, because A gives B and B gives C. D is never reached.", "B, D works, but C, D also works, so this is not the only correct set.", "C, D works, but B, D also works, so this is not the only correct set.", ""]),
        H("Practice questions"),
        PQ("Using the rules of Table 1, write down the functional dependency that shows why the tutor's name is repeated and explain the update anomaly it causes.",
           "TutorID → TutorName. Each tutor has one name, but the table stores the tutor name in every row for every student of that tutor. If the name is corrected in one row and not the others, the same TutorID has two different names: an update anomaly."),
        PQ("Compute the closure of {TutorID, StudentID} in STUDENT_COURSE and state whether it is a candidate key.",
           "Start: {TutorID, StudentID}. TutorID gives TutorName; StudentID gives StudentName. The closure is {TutorID, StudentID, TutorName, StudentName}. CourseID, CourseTitle and Mark are not reached, so it is not a key."),
        PQ("Describe one insertion anomaly and one deletion anomaly that arise if a school stores EXAM_RESULT(StudentID, StudentName, SubjectCode, SubjectName, Mark) in a single table with key (StudentID, SubjectCode).",
           "Insertion: a new subject cannot be added to the table until some student has a mark in it, because the key attribute StudentID would be empty. Deletion: if the only result for a subject is deleted, the subject name is lost with it."),
        PQ("A pupil says that Mark → StudentID because every mark in Table 1 is different. Explain why this is not a valid functional dependency.",
           "The marks 78, 64, 55 and 71 are different only by chance in this sample. Two students on different courses can get the same mark, and then one value of Mark would have two StudentIDs. A dependency must hold for every possible set of data under the rules of the business, so it cannot be inferred from a small sample."),
        SUM("A → B means each value of A goes with exactly one value of B; A is the determinant.",
            "Sample data can disprove a dependency but only the business rules can prove it.",
            "The closure A+ is everything A determines; a candidate key is a minimal set whose closure is all the attributes.",
            "Update, insertion and deletion anomalies appear when different facts are stored in one table.",
            "Normalization splits the table so that each fact is stored once."),
    ],
))

# ---------------------------------------------------------------------------
# Normalization 2: unnormalised data, 1NF and 2NF
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Normalization",
    title="From unnormalised data to first and second normal form",
    slug="csd-nf-1nf-2nf",
    minutes=24,
    summary="Remove repeating groups to reach 1NF, then find and remove partial dependencies to reach 2NF, using a cocoa buying centre's delivery notes and checking the result with SQL.",
    objectives=[
        "Explain why a table with repeating groups is not in first normal form",
        "Convert unnormalised data to 1NF and identify its composite primary key",
        "Identify partial dependencies on part of a composite key",
        "Decompose a 1NF relation into 2NF relations without losing information"
    ],
    key_concepts=["Unnormalised data", "Repeating group", "1NF", "Composite key", "Partial dependency", "2NF", "Lossless decomposition"],
    blocks=[
        H("Introduction"),
        T("A cocoa and coffee buying centre in Mbanga writes one delivery note for each buyer's pick-up. A note lists several crops, so the clerk's spreadsheet has several values packed into one record. That is easy to read on paper but hard for a database. This lesson turns such a note into properly structured tables, step by step."),
        CODE('''
NoteNo  Date        BuyerID  BuyerName   | CropCode  CropName  Kg   PricePerKg
301     2026-03-04  B2       Ets Mbanga  | C1        Cocoa     400  1000
                                         | C2        Coffee    150  1200
302     2026-03-05  B5       Mama Tata   | C1        Cocoa     250  1050
303     2026-03-05  B2       Ets Mbanga  | C3        Maize     600  200
                                         | C1        Cocoa     100  1050
                                         | C2        Coffee    90   1200
''', "text", title="Table 1: delivery notes (unnormalised). The four columns after | repeat inside each note."),
        H("First normal form"),
        D("A relation is in **first normal form (1NF)** if every attribute holds a single atomic value, there are no repeating groups of attributes, and each tuple can be identified by a primary key.",
          title="1NF"),
        T("In Table 1 each note holds a repeating group: the crop, the weight and the price occur several times in one note. In a relation every cell must hold one value, so the group cannot stay as it is."),
        EX("Worked example 1: reaching 1NF", intro="Convert Table 1 to first normal form and choose a primary key.", steps=[
            S("Give every crop line its own row", text="Notes 301 and 303 have two and three crop lines, so they become two and three rows. Note 302 gives one row. That makes 6 rows."),
            S("Repeat the note details on each row", text="Each row now carries NoteNo, Date, BuyerID and BuyerName, as well as its own crop line."),
            S("Choose the primary key", text="NoteNo alone is repeated (301 appears twice). CropCode alone is repeated (C1 appears three times). Together (NoteNo, CropCode) is unique in every row, so it is a composite key."),
            S("Write the 1NF relation", text="DELIVERY(NoteNo, Date, BuyerID, BuyerName, CropCode, CropName, Kg, PricePerKg), key (NoteNo, CropCode), with 6 tuples."),
        ]),
        T("The result is in 1NF, but it still repeats facts: \"Ets Mbanga\" is typed in five rows and \"Cocoa\" in three. This is where the second normal form helps."),
        H("Second normal form"),
        D("A **partial dependency** is a dependency of a non-key attribute on only part of a composite primary key. A relation is in **second normal form (2NF)** if it is in 1NF and has no partial dependencies: every non-key attribute depends on the whole key.",
          title="2NF"),
        KEY("The recipe from 1NF to 2NF", "Use it on any relation that has a composite key.", cards=[
            ["Step 1", "List all the functional dependencies from the rules of the business."],
            ["Step 2", "Mark every dependency whose determinant is only part of the key."],
            ["Step 3", "Move each such determinant, with the attributes it determines, to a new relation. The determinant is its primary key."],
            ["Step 4", "Keep the whole key and the attributes that need it in the original relation."],
        ]),
        EX("Worked example 2: removing partial dependencies", intro="Normalize DELIVERY(NoteNo, Date, BuyerID, BuyerName, CropCode, CropName, Kg, PricePerKg) to 2NF.", steps=[
            S("Dependencies", text="NoteNo → Date, BuyerID. BuyerID → BuyerName, so NoteNo → BuyerName as well. CropCode → CropName. (NoteNo, CropCode) → Kg, PricePerKg (the price may differ from note to note)."),
            S("Mark the partial dependencies", text="Date, BuyerID and BuyerName depend on NoteNo alone. CropName depends on CropCode alone. Only Kg and PricePerKg need both parts of the key."),
            S("Create a relation for each partial determinant", text="NOTE(NoteNo, Date, BuyerID, BuyerName) with key NoteNo; CROP(CropCode, CropName) with key CropCode."),
            S("Keep the rest with the whole key", text="NOTE_LINE(NoteNo, CropCode, Kg, PricePerKg) with key (NoteNo, CropCode). NoteNo and CropCode are foreign keys to NOTE and CROP."),
            S("Check by counting", text="NOTE has 3 tuples (one per note), CROP has 3 tuples (one per crop) and NOTE_LINE has 6. Ets Mbanga's name is now stored in 2 rows instead of 5, and Cocoa's name once instead of 3 times."),
        ]),
        CODE('''
NOTE                                      CROP
NoteNo  NoteDate    BuyerID  BuyerName    CropCode  CropName
301     2026-03-04  B2       Ets Mbanga   C1        Cocoa
302     2026-03-05  B5       Mama Tata    C2        Coffee
303     2026-03-05  B2       Ets Mbanga   C3        Maize

NOTE_LINE
NoteNo  CropCode  Kg   PricePerKg
301     C1        400  1000
301     C2        150  1200
302     C1        250  1050
303     C1        100  1050
303     C2        90   1200
303     C3        600  200
''', "text", title="Table 2: the 2NF relations (output of CREATE TABLE ... AS SELECT DISTINCT in sqlite3)"),
        H("Checking that nothing was lost"),
        T("A good decomposition is **lossless**: joining the new relations gives back exactly the original tuples, with none missing and none invented. Joining NOTE_LINE with NOTE on NoteNo and with CROP on CropCode rebuilds the six rows of DELIVERY. We ran this in sqlite3: the join returned the same 6 rows as the original, with 0 rows only in the original and 0 rows only in the rebuilt table."),
        CODE('''
SELECT N.NoteNo, N.BuyerName, C.CropName, L.Kg
FROM NOTE_LINE L
JOIN NOTE N ON L.NoteNo = N.NoteNo
JOIN CROP C ON L.CropCode = C.CropCode
WHERE N.BuyerName = 'Ets Mbanga' AND C.CropName = 'Cocoa'
ORDER BY N.NoteNo;

NoteNo  BuyerName   CropName  Kg
------  ----------  --------  ---
301     Ets Mbanga  Cocoa     400
303     Ets Mbanga  Cocoa     100
(2 rows)
''', "sql", title="Listing 1: the 2NF tables still answer the same questions"),
        TIP("A relation whose primary key is a single attribute is automatically in 2NF if it is in 1NF, because a single attribute has no 'part'. Partial dependencies can only occur with composite keys."),
        MISTAKE("Calling a table 2NF while a transitive dependency remains", "NOTE still has BuyerName depending on BuyerID, which depends on NoteNo. 2NF removes only partial dependencies. The next lesson removes the transitive one."),
        MISTAKE("Splitting the table without keeping the linking key", "If NOTE_LINE did not keep NoteNo and CropCode, there would be no way to join the new tables back together. Every split must leave the key that links the parts."),
        QUIZ("A relation R(A, B, C, D) has primary key (A, B) and the dependencies A → C and A, B → D. Which statement is true?",
             ["R is in 2NF because it has a primary key", "R is not in 2NF because C depends on only part of the key", "R is not in 1NF because it has four attributes", "R is in 2NF because D depends on the whole key"], 1,
             "A → C is a partial dependency: C depends on A, which is only part of the key (A, B). So R is not in 2NF, even though D depends on the whole key.",
             hint="Look for a non-key attribute that depends on only part of the composite key.",
             feedback=["Having a primary key is not enough: 2NF also requires that no non-key attribute depends on part of that key.", "", "The number of attributes has nothing to do with 1NF.", "D depends on the whole key, but C does not, and one partial dependency is enough to break 2NF."]),
        QUIZ("Which of these relations must be in 2NF (assuming it is in 1NF)?",
             ["ORDER_LINE(OrderNo, ProdCode, ProdName, Qty) with key (OrderNo, ProdCode)", "STAFF(StaffID, Name, Town) with key StaffID", "ENROL(StudentID, CourseID, CourseTitle) with key (StudentID, CourseID)", "MARK(StudentID, Subject, StudentName, Mark) with key (StudentID, Subject)"], 1,
             "STAFF has a single-attribute key, so no attribute can depend on only part of it. The other three have composite keys and a non-key attribute (ProdName, CourseTitle, StudentName) that depends on part of the key.",
             hint="Partial dependencies can only happen when the key has more than one attribute.",
             feedback=["ProdName depends on ProdCode alone: a partial dependency.", "", "CourseTitle depends on CourseID alone: a partial dependency.", "StudentName depends on StudentID alone: a partial dependency."]),
        H("Practice questions"),
        PQ("Explain why Table 1 is not in first normal form, and say what you must do to put it in 1NF.",
           "Each delivery note holds a repeating group: several values of CropCode, CropName, Kg and PricePerKg inside one record. A relation requires a single value in each cell. To reach 1NF, write each crop line as its own row (repeating the note details) and choose a primary key that identifies each row, here (NoteNo, CropCode)."),
        PQ("In the 1NF relation DELIVERY, state two partial dependencies and the attribute set that each one depends on.",
           "NoteNo → Date, BuyerID, BuyerName: these depend on NoteNo, which is only part of the key. CropCode → CropName: this depends on CropCode, the other part of the key."),
        PQ("A shop keeps SALE(ReceiptNo, ItemCode, ItemName, Qty, UnitPrice) with key (ReceiptNo, ItemCode). ItemName and UnitPrice depend only on ItemCode. Write the 2NF relations.",
           "ITEM(ItemCode, ItemName, UnitPrice) with key ItemCode; SALE_LINE(ReceiptNo, ItemCode, Qty) with key (ReceiptNo, ItemCode) and ItemCode as a foreign key to ITEM. (If the price at the time of sale must be kept, UnitPrice stays in SALE_LINE.)"),
        PQ("After moving to 2NF, the cocoa name is stored once and a buyer's name twice. Explain how this reduces the update anomaly, and say which problem remains.",
           "If Cocoa is renamed, one row in CROP is changed instead of three rows. A buyer's name is still stored once for each note by that buyer (2 rows for Ets Mbanga), so a change could still be made in one row and missed in the other. That is because BuyerName depends on BuyerID, which depends on NoteNo: a transitive dependency to be removed in third normal form."),
        SUM("1NF: single atomic values, no repeating groups, and a primary key.",
            "To flatten a repeating group, give every item its own row and repeat the parent details.",
            "2NF: in 1NF and no non-key attribute depends on only part of a composite key.",
            "Move each partial determinant and the attributes it determines to a new relation; keep the whole key in the original.",
            "A lossless decomposition gives back exactly the original tuples when the parts are joined."),
    ],
))

# ---------------------------------------------------------------------------
# Normalization 3: 3NF and BCNF
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="Normalization",
    title="Third normal form and Boyce-Codd normal form",
    slug="csd-nf-3nf-bcnf",
    minutes=25,
    summary="Remove transitive dependencies to reach 3NF, test a relation for BCNF using its determinants and decompose a tutoring table without creating false tuples.",
    objectives=[
        "Identify a transitive dependency and remove it to reach 3NF",
        "State the BCNF rule and test whether every determinant is a candidate key",
        "Decompose a relation that is in 3NF but not in BCNF",
        "Explain why a careless decomposition can create false tuples (a lossy join)"
    ],
    key_concepts=["Transitive dependency", "3NF", "BCNF", "Determinant", "Candidate key", "Lossless join", "Dependency preservation"],
    blocks=[
        H("Introduction"),
        T("In the last lesson the delivery notes of the Mbanga buying centre reached second normal form, but the relation NOTE(NoteNo, Date, BuyerID, BuyerName) still repeated a buyer's name for every note. This lesson removes that repetition (third normal form) and then looks at a more demanding rule, Boyce-Codd normal form."),
        H("Third normal form"),
        D("A **transitive dependency** exists when a non-key attribute depends on another non-key attribute, so that it depends on the key only indirectly: Key → A and A → B, where A is not a key and B is a non-key attribute.",
          title="Transitive dependency", note="In NOTE: NoteNo → BuyerID and BuyerID → BuyerName, so BuyerName depends on NoteNo only through BuyerID."),
        D("A relation is in **third normal form (3NF)** if it is in 2NF and has no transitive dependency of a non-key attribute on the key. A slightly more exact test: for every dependency X → A, either X is a superkey or A is a prime attribute (part of a candidate key).",
          title="3NF", note="A memory aid: every non-key attribute depends on the key, the whole key and nothing but the key."),
        EX("Worked example 1: removing the transitive dependency", intro="Normalize NOTE(NoteNo, Date, BuyerID, BuyerName) to 3NF.", steps=[
            S("List the dependencies", text="NoteNo → Date, BuyerID. BuyerID → BuyerName."),
            S("Find the transitive dependency", text="BuyerName depends on BuyerID, which is not a key of NOTE."),
            S("Split", text="BUYER(BuyerID, BuyerName) with key BuyerID, and NOTE(NoteNo, Date, BuyerID) with key NoteNo. BuyerID in NOTE is a foreign key to BUYER."),
            S("Check the data", text="BUYER has 2 tuples: (B2, Ets Mbanga) and (B5, Mama Tata). NOTE has 3 tuples. The name Ets Mbanga is now stored once instead of twice."),
        ]),
        CODE('''
BUYER(BuyerID, BuyerName)                  NOTE(NoteNo, NoteDate, BuyerID)
BuyerID  BuyerName                         NoteNo  NoteDate    BuyerID
B2       Ets Mbanga                        301     2026-03-04  B2
B5       Mama Tata                         302     2026-03-05  B5
                                           303     2026-03-05  B2

CROP(CropCode, CropName)                   NOTE_LINE(NoteNo, CropCode, Kg, PricePerKg)
CropCode  CropName                         key: (NoteNo, CropCode)
C1        Cocoa                            NoteNo -> NOTE, CropCode -> CROP
C2        Coffee
C3        Maize
''', "text", title="Table 1: the final design in 3NF (four relations)"),
        TIP("The design in Table 1 is also a good database design: every relation has one subject (a buyer, a note, a crop, a crop line), and every foreign key can be drawn as a one-to-many relationship."),
        H("Boyce-Codd normal form"),
        D("A relation is in **Boyce-Codd normal form (BCNF)** if for every non-trivial dependency X → A, the determinant X is a superkey (contains a candidate key). In other words, every determinant is a candidate key.",
          title="BCNF", note="BCNF is stricter than 3NF. Every BCNF relation is in 3NF, but not every 3NF relation is in BCNF."),
        T("The difference appears only when a relation has two or more candidate keys that overlap, so that a prime attribute depends on something that is not a key."),
        EX("Worked example 2: testing TUTORING for BCNF", intro="TUTORING(Student, Subject, Teacher) records extra lessons. Each student has one teacher for each subject. Each teacher teaches only one subject. Is it in BCNF?", steps=[
            S("Write the dependencies", text="(Student, Subject) → Teacher. Teacher → Subject."),
            S("Find the candidate keys", text="(Student, Subject) works: it determines Teacher. (Student, Teacher) also works: Teacher gives Subject. So there are two overlapping candidate keys. (A closure check in Python confirmed both.)"),
            S("Check 3NF", text="For Teacher → Subject, Subject is a prime attribute (it is part of the key (Student, Subject)), so the 3NF condition holds."),
            S("Check BCNF", text="The determinant Teacher is not a candidate key: one teacher teaches many students. So TUTORING is in 3NF but not in BCNF."),
            S("Show the anomaly", text="The fact that Mrs Ewane teaches Physics is repeated for each of her students. If she changes subject, every row about her must be changed."),
        ]),
        EX("Worked example 3: decomposing to BCNF", intro="Decompose TUTORING so that every determinant is a candidate key.", steps=[
            S("Split on the offending dependency", text="Teacher → Subject becomes TEACHES(Teacher, Subject) with key Teacher."),
            S("Keep the determinant with the rest", text="STUDENT_TEACHER(Student, Teacher) with key (Student, Teacher). Teacher is a foreign key to TEACHES."),
            S("Check it is lossless", text="Join STUDENT_TEACHER with TEACHES on Teacher. With the sample tuples (Abena, Maths, Tabi), (Abena, Physics, Ewane), (Bih, Maths, Tabi), (Nkeng, Maths, Njoh), the join returns exactly the same 4 tuples (verified in sqlite3)."),
            S("Note the cost", text="The dependency (Student, Subject) → Teacher is no longer inside one relation, so the database cannot enforce it with a key. This is why designers sometimes accept 3NF instead of BCNF."),
        ]),
        CODE('''
-- the correct split: join on Teacher
SELECT ST.Student, TEACHES.Subject, ST.Teacher
FROM ST JOIN TEACHES ON ST.Teacher = TEACHES.Teacher
ORDER BY 1, 2;

Student  Subject  Teacher
-------  -------  -------
Abena    Maths    Tabi
Abena    Physics  Ewane
Bih      Maths    Tabi
Nkeng    Maths    Njoh
(4 rows)

-- a careless split: (Student, Subject) and (Subject, Teacher)
SELECT * FROM BAD1 NATURAL JOIN BAD2 ORDER BY 1, 2, 3;
(7 rows)   <- 3 false tuples, e.g. Bih, Maths, Njoh
''', "sql", title="Listing 1: a lossless split and a lossy split (run in sqlite3)"),
        T("The careless split gives 7 tuples instead of 4. The extra tuples, such as (Bih, Maths, Njoh), say that Bih is taught Maths by Mr Njoh, which is false. A decomposition must be **lossless**: the common attribute of the two parts must be a key of at least one of them. Teacher is the key of TEACHES, but Subject is not a key of either part in the careless split."),
        MISTAKE("Saying that 3NF means every determinant is a key", "That is the BCNF rule. 3NF allows a determinant that is not a key if the attribute it determines is prime. Learn them in order: 3NF removes transitive dependencies; BCNF requires every determinant to be a candidate key."),
        MISTAKE("Splitting on attributes that do not form a key", "Always split on a dependency X → Y: one relation (X, Y), and the other keeps X with the remaining attributes. If you split any other way you may lose information or invent false tuples."),
        QUIZ("A relation R(A, B, C) has key A and the dependencies A → B, B → C. Which normal form is it in?",
             ["BCNF", "3NF but not BCNF", "2NF but not 3NF", "1NF but not 2NF"], 2,
             "The key A is a single attribute, so there is no partial dependency, and R is in 2NF. But C depends on A only through B (a transitive dependency), so R is not in 3NF.",
             hint="Is there a non-key attribute that depends on another non-key attribute?",
             feedback=["BCNF would need every determinant to be a key. B is a determinant and is not a key.", "3NF requires no transitive dependency; B → C with B a non-key attribute breaks it.", "", "A single-attribute key cannot have a partial dependency, so the relation is already in 2NF."]),
        QUIZ("A relation has the dependencies X, Y → Z and Z → Y, and its candidate keys are (X, Y) and (X, Z). Which statement is correct?",
             ["It is in BCNF because it has two keys", "It is in 3NF but not in BCNF", "It is not in 3NF", "It is not in 2NF"], 1,
             "Z → Y has determinant Z which is not a candidate key, so it is not in BCNF. Y is prime (part of the key (X, Y)), so the 3NF condition holds.",
             hint="Test the dependency Z → Y: is Z a candidate key? Is Y a prime attribute?",
             feedback=["Having two candidate keys does not guarantee BCNF: every determinant must be one of them.", "", "3NF holds because Y is a prime attribute in Z → Y.", "No attribute depends on only part of a key without being prime, so 2NF holds."]),
        H("Practice questions"),
        PQ("State the 3NF rule and the BCNF rule in terms of determinants, and say which is stricter.",
           "3NF: for every dependency X → A, X is a superkey or A is a prime attribute (equivalently, no transitive dependency of non-key attributes on the key). BCNF: for every non-trivial dependency X → A, X must be a superkey. BCNF is stricter: every BCNF relation is in 3NF, but a 3NF relation can fail BCNF."),
        PQ("EMPLOYEE(EmpID, Name, DeptCode, DeptName) has key EmpID. DeptCode → DeptName. Show why it is not in 3NF and give the 3NF relations.",
           "EmpID → DeptCode and DeptCode → DeptName, so DeptName depends on the key through DeptCode: a transitive dependency. Split into EMPLOYEE(EmpID, Name, DeptCode) with DeptCode as a foreign key, and DEPARTMENT(DeptCode, DeptName) with key DeptCode."),
        PQ("In the TUTORING relation, give the dependency that violates BCNF and explain why it does not violate 3NF.",
           "Teacher → Subject violates BCNF because Teacher is not a candidate key. It does not violate 3NF because Subject is a prime attribute: it belongs to the candidate key (Student, Subject)."),
        PQ("A student decomposes TUTORING into (Student, Subject) and (Subject, Teacher). Explain why this is a bad decomposition.",
           "The common attribute Subject is not a key of either relation, so joining them pairs every student of a subject with every teacher of that subject. With the sample data the join gives 7 tuples instead of 4, including false ones such as (Bih, Maths, Njoh). The decomposition is lossy: it does not give back the original relation."),
        SUM("A transitive dependency (Key → A, A → B with A not a key) must be removed to reach 3NF.",
            "3NF: every non-key attribute depends on the key, the whole key and nothing but the key.",
            "BCNF: every determinant is a candidate key. It differs from 3NF only for overlapping candidate keys.",
            "Decompose on the offending dependency X → Y into (X, Y) and the rest with X.",
            "A decomposition must be lossless: joining the parts must give exactly the original tuples."),
    ],
))

# ---------------------------------------------------------------------------
# SQL 1: DDL
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="SQL",
    title="SQL data definition: CREATE, ALTER, DROP and constraints",
    slug="csd-sql-ddl",
    minutes=24,
    summary="Create tables with data types, primary and foreign keys and constraints, change them with ALTER TABLE, remove them safely with DROP TABLE and read the real error messages when a constraint stops bad data.",
    objectives=[
        "Write CREATE TABLE statements with suitable data types and constraints",
        "Define primary keys and foreign keys and explain referential integrity",
        "Use ALTER TABLE and DROP TABLE and choose a safe order for dropping related tables",
        "Predict which constraint rejects a given INSERT"
    ],
    key_concepts=["DDL", "CREATE TABLE", "Data type", "Primary key", "Foreign key", "Referential integrity", "NOT NULL", "CHECK", "UNIQUE", "DEFAULT", "ALTER TABLE", "DROP TABLE"],
    blocks=[
        H("Introduction"),
        T("The library of a secondary school in Limbe wants to replace its exercise book with a database of members, books and loans. Before any data goes in, the structure must be defined: the tables, the columns, the type of data in each column and the rules that stop mistakes. In SQL, this is the job of the **Data Definition Language (DDL)**."),
        T("All the statements in this lesson were run in sqlite3, which is built into Python. The commands are standard SQL. Data type names and a few details differ between database products, so check the product you use."),
        D("**DDL** (Data Definition Language) statements create and change the structure of a database: CREATE TABLE, ALTER TABLE and DROP TABLE. **DML** (Data Manipulation Language) statements work on the data inside the tables: INSERT, UPDATE, DELETE and SELECT.",
          title="DDL and DML"),
        IMG("al-csd-library-schema.svg",
            "Three tables: Member (MemberID primary key, Name, Form, Town), Loan (LoanID primary key, MemberID and BookID foreign keys, LoanDate) and Book (BookID primary key, Title, Author, Price, Category). One member and one book each link to many loans.",
            caption="Figure 1. The library database built in this lesson."),
        H("CREATE TABLE and constraints"),
        KEY("Common data types", "Names vary by product. These are the ideas.", cards=[
            ["Whole numbers", "INTEGER (or INT). Used for keys, quantities, prices in whole FCFA."],
            ["Text", "VARCHAR(n) or TEXT. Names, titles, towns. VARCHAR(n) limits the length."],
            ["Decimal numbers", "DECIMAL(p, s) or REAL. Use DECIMAL for money with cents."],
            ["Dates", "DATE. SQLite stores dates as text such as 2026-02-02, which sorts correctly."],
        ]),
        KEY("Constraints: rules the database enforces", "They protect the data even when a program has a bug.", cards=[
            ["PRIMARY KEY", "Identifies each row. Unique and never empty."],
            ["FOREIGN KEY", "A value must exist in the primary key of another table (referential integrity)."],
            ["NOT NULL", "The column cannot be left empty."],
            ["UNIQUE", "No two rows can have the same value in the column."],
            ["CHECK", "The value must satisfy a condition, such as Price > 0."],
            ["DEFAULT", "The value used when none is given."],
        ]),
        EX("Worked example 1: creating the three tables", intro="Write CREATE TABLE statements for Member, Book and Loan. Members are in L6 or U6. Prices must be positive. A loan refers to one member and one book.", steps=[
            S("Create the tables that others refer to first", text="Member and Book have no foreign keys, so they come first. Loan refers to both, so it comes last."),
            S("Member", text="MemberID is the primary key. Name cannot be empty. Form must be L6 or U6. Town defaults to Limbe."),
            S("Book", text="BookID is the primary key. Title cannot be empty. Price must be above 0."),
            S("Loan", text="LoanID is the primary key. MemberID and BookID are NOT NULL and declared as foreign keys that refer to the other tables."),
        ]),
        CODE('''
CREATE TABLE Member (
  MemberID INTEGER PRIMARY KEY,
  Name     TEXT NOT NULL,
  Form     TEXT NOT NULL CHECK (Form IN ('L6', 'U6')),
  Town     TEXT DEFAULT 'Limbe'
);

CREATE TABLE Book (
  BookID   INTEGER PRIMARY KEY,
  Title    TEXT NOT NULL,
  Author   TEXT,
  Price    INTEGER CHECK (Price > 0),
  Category TEXT
);

CREATE TABLE Loan (
  LoanID   INTEGER PRIMARY KEY,
  MemberID INTEGER NOT NULL,
  BookID   INTEGER NOT NULL,
  LoanDate TEXT NOT NULL,
  FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
  FOREIGN KEY (BookID)   REFERENCES Book(BookID)
);
''', "sql", title="Listing 1: the library tables"),
        TIP("SQLite does not check foreign keys unless you run PRAGMA foreign_keys = ON; at the start of each connection. Other database products check them by default."),
        H("Constraints at work"),
        T("The next listing inserts good and bad rows. Each bad row is refused with a message that names the rule it broke. (These are the actual messages from SQLite; other products word them differently.)"),
        CODE('''
INSERT INTO Member (MemberID, Name, Form, Town) VALUES (1, 'Abena', 'L6', 'Buea');   -- ok
INSERT INTO Member (MemberID, Name, Form) VALUES (2, 'Bih', 'U6');                    -- ok, Town = Limbe

SELECT * FROM Member;
MemberID  Name   Form  Town
--------  -----  ----  -----
1         Abena  L6    Buea
2         Bih    U6    Limbe

INSERT INTO Member VALUES (3, 'Nkeng', 'S5', 'Kumba');
  -> CHECK constraint failed: Form IN ('L6','U6')
INSERT INTO Member (MemberID, Form) VALUES (4, 'U6');
  -> NOT NULL constraint failed: Member.Name
INSERT INTO Book VALUES (7, 'Free Book', 'X', -50, 'Novel');
  -> CHECK constraint failed: Price > 0
INSERT INTO Loan VALUES (8, 9, 1, '2026-03-01');
  -> FOREIGN KEY constraint failed        (there is no member 9)
INSERT INTO Loan VALUES (1, 9, 1, '2026-02-02', 0);
  -> table Loan has 4 columns but 5 values were supplied
''', "sql", title="Listing 2: constraints refusing bad data (run in sqlite3)"),
        EX("Worked example 2: which rule refused the row?", intro="A clerk types INSERT INTO Member VALUES (5, NULL, 'U6', 'Bali'); and INSERT INTO Loan VALUES (9, 1, 99, '2026-03-02'); where no book 99 exists. Which constraint rejects each?", steps=[
            S("First statement", text="The Name value is NULL, but Name was declared NOT NULL, so the NOT NULL constraint rejects the row."),
            S("Second statement", text="Loan.BookID = 99 does not exist in Book.BookID, so the FOREIGN KEY constraint rejects the row (referential integrity)."),
            S("Why this matters", text="The rejected rows never reach the table, so no later query can return a loan for a book that does not exist."),
        ]),
        D("**Referential integrity** means that every foreign key value either is NULL or matches an existing primary key value in the table it refers to. A row cannot refer to something that does not exist.",
          title="Referential integrity", note="Entity integrity is the matching rule for primary keys: a primary key is unique and never NULL."),
        H("ALTER TABLE and DROP TABLE"),
        T("Requirements change. ALTER TABLE changes a table that exists, and keeps its data. DROP TABLE removes the table and all its data, so use it with care."),
        CODE('''
ALTER TABLE Member ADD COLUMN Phone TEXT;

SELECT * FROM Member WHERE MemberID = 1;
MemberID  Name   Form  Town  Phone
--------  -----  ----  ----  -----
1         Abena  L6    Buea  NULL

DROP TABLE Member;        -- refused while Loan rows still refer to members
  -> FOREIGN KEY constraint failed

DROP TABLE Loan;          -- drop the table with the foreign key first
DROP TABLE Member;        -- now it is allowed
''', "sql", title="Listing 3: changing and removing tables"),
        T("The order matters. A table that holds foreign keys (the child) must be dropped before the tables it refers to (the parents). Creation works the other way round: parents first, children second."),
        MISTAKE("Creating the child table before its parent", "FOREIGN KEY (MemberID) REFERENCES Member(MemberID) needs Member to exist. Create Member and Book first, Loan last."),
        MISTAKE("Using DROP TABLE when you mean DELETE", "DROP TABLE removes the table itself, its structure and its rows. DELETE FROM removes rows but keeps the table. There is no undo without a backup."),
        QUIZ("Which clause makes sure a Price can never be zero or negative?",
             ["PRIMARY KEY (Price)", "CHECK (Price > 0)", "UNIQUE (Price)", "DEFAULT 0"], 1,
             "A CHECK constraint states a condition that every row must satisfy. INSERT or UPDATE statements that break it are rejected.",
             hint="Which constraint tests a condition on the value?",
             feedback=["A primary key would make each price unique and never empty, but it would not stop negative prices.", "", "UNIQUE would stop two books having the same price, which is not wanted.", "DEFAULT only supplies a value when none is given; 0 would actually be an invalid price."]),
        QUIZ("Loan(LoanID, MemberID, BookID, LoanDate) has foreign keys to Member and Book. In which order should the three tables be created?",
             ["Loan, Member, Book", "Member, Book, Loan", "Loan, Book, Member", "Any order works"], 1,
             "Parent tables (Member and Book) must exist before the child table Loan can refer to them.",
             hint="A foreign key must refer to something that already exists.",
             feedback=["Loan would refer to tables that do not exist yet.", "", "Loan would again come before the tables it refers to.", "In most database products a foreign key must refer to an existing table, so the order matters."]),
        H("Practice questions"),
        PQ("Write a CREATE TABLE statement for Teacher with a primary key TeacherID, a Name that cannot be empty, and a Salary that must be above zero.",
           "CREATE TABLE Teacher ( TeacherID INTEGER PRIMARY KEY, Name TEXT NOT NULL, Salary INTEGER CHECK (Salary > 0) );  In standard SQL Name could be VARCHAR(50) and the key could also be written PRIMARY KEY (TeacherID) as a separate line."),
        PQ("Add a foreign key to a new table Reservation(ResID, MemberID, BookID) so that every reservation refers to an existing member and book, and explain what the foreign key prevents.",
           "CREATE TABLE Reservation ( ResID INTEGER PRIMARY KEY, MemberID INTEGER NOT NULL, BookID INTEGER NOT NULL, FOREIGN KEY (MemberID) REFERENCES Member(MemberID), FOREIGN KEY (BookID) REFERENCES Book(BookID) );  It prevents a reservation for a member or a book that does not exist (referential integrity)."),
        PQ("The statement INSERT INTO Book VALUES (8, 'Atlas', 'T. Fon', 0, 'Science'); is rejected. Which constraint is responsible and why?",
           "The CHECK (Price > 0) constraint: the price 0 does not satisfy the condition, so the row is rejected before it is stored."),
        PQ("Explain the difference between DROP TABLE Member and DELETE FROM Member, and say which one the school should use to remove a student who left.",
           "DROP TABLE Member deletes the table itself with all its rows and structure. DELETE FROM Member removes rows and keeps the table. To remove one leaving student, use DELETE FROM Member WHERE MemberID = ...; (after that student's loans have been dealt with, because of the foreign key)."),
        SUM("DDL defines structure: CREATE TABLE, ALTER TABLE, DROP TABLE. DML works on the data.",
            "Constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, DEFAULT) keep the data valid.",
            "A foreign key must match an existing primary key: this is referential integrity.",
            "Create parent tables before child tables and drop child tables before parent tables.",
            "ALTER TABLE changes a table and keeps its data; DROP TABLE removes both."),
    ],
))

# ---------------------------------------------------------------------------
# SQL 2: DML and single-table queries
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="SQL",
    title="SQL data manipulation: INSERT, UPDATE, DELETE and SELECT with conditions",
    slug="csd-sql-dml-queries",
    minutes=24,
    summary="Add, change and remove rows with INSERT, UPDATE and DELETE, and query one table with WHERE, AND, OR, LIKE, BETWEEN, IN, IS NULL, ORDER BY, DISTINCT and LIMIT, using real output from sqlite3.",
    objectives=[
        "Write INSERT, UPDATE and DELETE statements and explain why WHERE matters",
        "Write SELECT queries with comparison, logical, LIKE, BETWEEN, IN and IS NULL conditions",
        "Sort and limit results with ORDER BY, DISTINCT and LIMIT",
        "Explain how NULL behaves in comparisons"
    ],
    key_concepts=["INSERT", "UPDATE", "DELETE", "SELECT", "WHERE", "LIKE", "BETWEEN", "IN", "NULL", "ORDER BY", "DISTINCT", "Alias"],
    blocks=[
        H("Introduction"),
        T("With the library tables created in the last lesson, the librarian in Limbe can start working with data: register a new member, correct a price, remove a lost book, and ask questions such as \"Which computing books cost more than 6000 FCFA?\" These tasks use the **Data Manipulation Language (DML)**: INSERT, UPDATE, DELETE and SELECT."),
        CODE('''
Book
BookID  Title                   Author          Price  Category
1       Things Fall Apart       Chinua Achebe   3500   Novel
2       Python for Schools      Mbah Ndifor     6000   Computing
3       A Level Physics         T. Fon          8500   Science
4       Database Basics         R. Essomba      7000   Computing
5       The Joys of Motherhood  Buchi Emecheta  4000   Novel
6       Chemistry Notes         NULL            5000   Science

Member
MemberID  Name    Form  Town
1         Abena   L6    Buea
2         Bih     U6    Limbe
3         Nkeng   U6    Buea
4         Tchoua  L6    Dschang
5         Fomba   U6    Bamenda
''', "text", title="Table 1: the data used in this lesson (the authors Mbah Ndifor, T. Fon and R. Essomba are invented for teaching)"),
        H("INSERT, UPDATE and DELETE"),
        CODE('''
INSERT INTO Book (BookID, Title, Author, Price, Category)
VALUES (7, 'Web Design Basics', 'S. Njoh', 5500, 'Computing');   -- name the columns

INSERT INTO Member VALUES (6, 'Ewane', 'L6', 'Kumba');           -- or give a value for every column

UPDATE Book SET Price = Price * 11 / 10 WHERE Category = 'Computing';   -- a 10 percent rise

DELETE FROM Loan WHERE LoanID = 7;                                 -- remove one row
''', "sql", title="Listing 1: the three data-changing statements"),
        EX("Worked example 1: a price rise", intro="The library raises the price of every Computing book by 10 percent. Write the statement, say what it changes and check the result.", steps=[
            S("Write the statement", text="UPDATE Book SET Price = Price * 11 / 10 WHERE Category = 'Computing';"),
            S("Predict", text="Only rows whose Category is Computing change: Python for Schools 6000 becomes 6600 and Database Basics 7000 becomes 7700. The other four books are untouched."),
            S("Check by running it", text="sqlite3 reported 2 rows changed, and SELECT Title, Price FROM Book WHERE Category = 'Computing'; returned Python for Schools 6600 and Database Basics 7700."),
            S("Note the integer arithmetic", text="Price is an integer, so Price * 11 / 10 uses integer division in SQLite. Multiplying by 11 first and dividing second avoids a rounding error on whole numbers like these."),
        ]),
        MISTAKE("UPDATE or DELETE without WHERE", "UPDATE Book SET Price = 0; changes every row, and DELETE FROM Member; removes every member. Always write the WHERE clause first and test it with a SELECT that uses the same condition."),
        EX("Worked example 2: a delete that the database refuses", intro="Delete member 1 (Abena) while she still has loans recorded. What happens, and what is the correct way?", steps=[
            S("Run it", text="DELETE FROM Member WHERE MemberID = 1; is refused with FOREIGN KEY constraint failed, because Loan rows still refer to her."),
            S("Why", text="The foreign key protects referential integrity: a loan would otherwise refer to a member that no longer exists."),
            S("The correct way", text="First delete or archive her loans: DELETE FROM Loan WHERE MemberID = 1; Then DELETE FROM Member WHERE MemberID = 1; works."),
        ]),
        H("SELECT with conditions"),
        T("SELECT chooses the columns, FROM names the table and WHERE chooses the rows. Strings go in single quotes. The order of rows is not guaranteed unless you write ORDER BY."),
        CODE('''
SELECT Title, Price FROM Book WHERE Price >= 4000 AND Category <> 'Science' ORDER BY Price DESC;

Title                   Price
----------------------  -----
Database Basics         7000
Python for Schools      6000
The Joys of Motherhood  4000
(3 rows)

SELECT Title, Price FROM Book WHERE Price BETWEEN 4000 AND 7000 ORDER BY BookID;

Title                   Price
----------------------  -----
Python for Schools      6000
Database Basics         7000
The Joys of Motherhood  4000
Chemistry Notes         5000
(4 rows)

SELECT Name FROM Member WHERE Town IN ('Buea', 'Limbe') ORDER BY MemberID;

Name
-----
Abena
Bih
Nkeng
(3 rows)
''', "sql", title="Listing 2: AND, ORDER BY, BETWEEN and IN (run in sqlite3)"),
        KEY("The condition toolbox", "All of these go after WHERE.", cards=[
            ["Comparison", "=, <> (not equal), <, >, <=, >=. Combine with AND, OR, NOT."],
            ["BETWEEN a AND b", "Includes both ends: BETWEEN 4000 AND 7000 includes 4000 and 7000."],
            ["IN (list)", "Matches any value in the list. Shorter than several ORs."],
            ["LIKE", "Pattern matching: % means any characters, _ means exactly one character."],
            ["IS NULL", "Tests for a missing value. Never use = NULL."],
        ]),
        EX("Worked example 3: patterns and missing values", intro="Find (a) titles that start with Data, (b) titles containing Python or ending in Physics, (c) books with no recorded author.", steps=[
            S("(a) LIKE with a trailing %", text="SELECT Title FROM Book WHERE Title LIKE 'Data%'; returns Database Basics (1 row)."),
            S("(b) Two patterns joined with OR", text="SELECT Title FROM Book WHERE Title LIKE '%Python%' OR Title LIKE '%Physics' ORDER BY BookID; returns Python for Schools and A Level Physics."),
            S("(c) IS NULL", text="SELECT Title FROM Book WHERE Author IS NULL; returns Chemistry Notes."),
            S("The wrong way", text="SELECT Title FROM Book WHERE Author = NULL; returns 0 rows when run. NULL means unknown, and a comparison with an unknown value is never true. Only IS NULL works."),
        ]),
        CODE('''
SELECT DISTINCT Category FROM Book;

Category
---------
Novel
Computing
Science
(3 rows)

SELECT Title, Price FROM Book ORDER BY Price DESC LIMIT 3;

Title               Price
------------------  -----
A Level Physics     8500
Database Basics     7000
Python for Schools  6000
(3 rows)

SELECT Title, Price, Price * 12 / 10 AS PriceWithMargin FROM Book WHERE Category = 'Novel';

Title                   Price  PriceWithMargin
----------------------  -----  ---------------
Things Fall Apart       3500   4200
The Joys of Motherhood  4000   4800
(2 rows)
''', "sql", title="Listing 3: DISTINCT, LIMIT and a calculated column with an alias"),
        TIP("In SQLite, LIKE ignores upper and lower case by default. In other database products it may be case-sensitive. LIMIT is written differently in some products (TOP or FETCH FIRST), but the idea is the same."),
        QUIZ("Using Table 1, how many rows does SELECT Title FROM Book WHERE Author = NULL; return?",
             ["1", "0", "6", "An error message"], 1,
             "Author = NULL is never true, because NULL is unknown and cannot be equal to anything. The query is valid but returns 0 rows. Use IS NULL instead.",
             hint="What does a comparison with an unknown value give?",
             feedback=["That is what IS NULL would return (Chemistry Notes). The = comparison does not work with NULL.", "", "That would be every row, but the condition is never true.", "The statement is valid SQL, so there is no error. It simply matches no rows."]),
        QUIZ("Which condition selects books whose price is from 4000 to 7000 inclusive?",
             ["Price > 4000 AND Price < 7000", "Price BETWEEN 4000 AND 7000", "Price IN (4000, 7000)", "Price = 4000 OR 7000"], 1,
             "BETWEEN includes both end values. In Table 1 it selects 4 books: 6000, 7000, 4000 and 5000.",
             hint="Do the end values 4000 and 7000 have to be included?",
             feedback=["This leaves out the books priced exactly 4000 and 7000.", "", "IN (4000, 7000) matches only those two exact prices.", "This is not a valid way to test two values; the second part is just the number 7000."]),
        H("Practice questions"),
        PQ("Write a query to list the names and towns of Upper Sixth members, in alphabetical order of name, and give the output for Table 1.",
           "SELECT Name, Town FROM Member WHERE Form = 'U6' ORDER BY Name; The U6 members are Bih (Limbe), Nkeng (Buea) and Fomba (Bamenda). In alphabetical order the output is Bih Limbe; Fomba Bamenda; Nkeng Buea."),
        PQ("Write an UPDATE statement that changes the town of member 4 to Kumba, and explain what would go wrong without the WHERE clause.",
           "UPDATE Member SET Town = 'Kumba' WHERE MemberID = 4; Without WHERE, every member's town would be changed to Kumba."),
        PQ("Write a query for novels that cost less than 4000 FCFA, or any book whose author is not recorded, and give the titles using Table 1.",
           "SELECT Title FROM Book WHERE (Category = 'Novel' AND Price < 4000) OR Author IS NULL ORDER BY BookID; Things Fall Apart (novel, 3500) and Chemistry Notes (no author). The Joys of Motherhood costs exactly 4000, so it is not less than 4000."),
        PQ("Explain why SELECT * FROM Book WHERE Author <> 'T. Fon'; does not return Chemistry Notes, even though its author is not T. Fon.",
           "Chemistry Notes has Author = NULL (unknown). A comparison such as NULL <> 'T. Fon' is not true, it is unknown, so the row is not returned. To include it, add OR Author IS NULL."),
        SUM("INSERT adds rows, UPDATE changes rows, DELETE removes rows; always check the WHERE clause.",
            "SELECT lists columns, FROM names the table, WHERE chooses rows, ORDER BY sorts, LIMIT cuts the list.",
            "BETWEEN includes both ends, IN matches a list, LIKE uses % and _ patterns.",
            "NULL means unknown: use IS NULL, never = NULL.",
            "DISTINCT removes duplicate rows from the result; an alias (AS) names a calculated column."),
    ],
))

# ---------------------------------------------------------------------------
# SQL 3: joins
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="SQL",
    title="SQL joins: INNER JOIN, LEFT JOIN and self-joins",
    slug="csd-sql-joins",
    minutes=24,
    summary="Combine two or three tables with INNER JOIN, list rows that have no match with LEFT JOIN and IS NULL, join a table to itself, and avoid the accidental Cartesian product, with every query run in sqlite3.",
    objectives=[
        "Write INNER JOIN queries with table aliases over two and three tables",
        "Explain what a missing ON condition does to the result",
        "Use LEFT JOIN with IS NULL to find rows with no match",
        "Write a self-join and place a filter in the right clause of an outer join"
    ],
    key_concepts=["INNER JOIN", "ON condition", "Table alias", "LEFT JOIN", "Self-join", "Cartesian product"],
    blocks=[
        H("Introduction"),
        T("The Loan table of the school library holds only numbers: which member (MemberID) borrowed which book (BookID) and when. A librarian wants names and titles, not numbers. The names live in Member, the titles in Book. A **join** brings the facts together by matching the foreign key in Loan with the primary key of the other table."),
        CODE('''
Loan                                    Member                Book (short)
LoanID  MemberID  BookID  LoanDate      MemberID  Name        BookID  Title               Category
1       1         1       2026-01-12    1         Abena       1       Things Fall Apart   Novel
2       1         2       2026-01-15    2         Bih         2       Python for Schools  Computing
3       2         2       2026-01-20    3         Nkeng       3       A Level Physics     Science
4       3         4       2026-02-03    4         Tchoua      4       Database Basics     Computing
5       3         2       2026-02-05    5         Fomba       5       The Joys of Motherhood  Novel
6       3         5       2026-02-10                          6       Chemistry Notes     Science
7       5         1       2026-02-11
''', "text", title="Table 1: the library data (Member also has Form and Town: Abena Buea, Bih Limbe, Nkeng Buea, Tchoua Dschang, Fomba Bamenda)"),
        H("Why the ON condition matters"),
        T("If you list two tables in FROM with no condition, SQL returns the Cartesian product: every row of one table paired with every row of the other. With 5 members and 6 books, SELECT COUNT(*) FROM Member, Book; returns 30 (checked in sqlite3), and most of those pairs are meaningless. An **INNER JOIN ... ON** keeps only the pairs where the condition is true."),
        D("**INNER JOIN** returns the rows for which the ON condition is true in both tables. Rows with no match in the other table are left out. The ON condition normally compares a foreign key with the primary key it refers to.",
          title="INNER JOIN", note="INNER is optional: JOIN on its own means INNER JOIN."),
        EX("Worked example 1: member names with loan dates", intro="List each member's name and the date of each loan.", steps=[
            S("Choose the tables", text="Names are in Member and dates are in Loan, so both are needed."),
            S("Choose the matching condition", text="Member.MemberID = Loan.MemberID: the primary key and the foreign key that refers to it."),
            S("Write the query", text="Use the table name before a column name when the same column name is in both tables (MemberID is)."),
        ]),
        CODE('''
SELECT Member.Name, Loan.LoanDate
FROM Member
INNER JOIN Loan ON Member.MemberID = Loan.MemberID
ORDER BY Loan.LoanID;

Name   LoanDate
-----  ----------
Abena  2026-01-12
Abena  2026-01-15
Bih    2026-01-20
Nkeng  2026-02-03
Nkeng  2026-02-05
Nkeng  2026-02-10
Fomba  2026-02-11
(7 rows)
''', "sql", title="Listing 1: a two-table join (7 rows, one per loan)"),
        T("The result has 7 rows, one for each loan. Tchoua is missing, because Tchoua has no loan to be matched with."),
        H("Joining three tables with aliases"),
        T("To show names and titles, Loan must be joined to both Member and Book. A **table alias** (a short name given after the table name) makes the query shorter and is essential for self-joins."),
        EX("Worked example 2: who borrowed which computing book?", intro="List the member name and title for every loan of a Computing book.", steps=[
            S("Start with the linking table", text="FROM Loan L is the centre: it has a foreign key to each of the other two tables."),
            S("Join Member", text="JOIN Member M ON L.MemberID = M.MemberID"),
            S("Join Book", text="JOIN Book B ON L.BookID = B.BookID"),
            S("Add the filter after the joins", text="WHERE B.Category = 'Computing'. ORDER BY M.Name, B.Title gives a stable order."),
        ]),
        CODE('''
SELECT M.Name, B.Title
FROM Loan L
JOIN Member M ON L.MemberID = M.MemberID
JOIN Book   B ON L.BookID   = B.BookID
WHERE B.Category = 'Computing'
ORDER BY M.Name, B.Title;

Name   Title
-----  ------------------
Abena  Python for Schools
Bih    Python for Schools
Nkeng  Database Basics
Nkeng  Python for Schools
(4 rows)
''', "sql", title="Listing 2: a three-table join with a filter"),
        TIP("An older style lists the tables with commas and puts the join condition in WHERE: FROM Member M, Loan L, Book B WHERE M.MemberID = L.MemberID AND L.BookID = B.BookID. It gives the same rows, but it is easy to forget a condition and get a Cartesian product, so prefer JOIN ... ON."),
        H("LEFT JOIN: keeping the rows with no match"),
        D("**LEFT JOIN** returns every row of the left table. For rows with no match in the right table, the right table's columns are filled with NULL.",
          title="LEFT JOIN", note="The left table is the one written before the word JOIN."),
        EX("Worked example 3: members and books with no loans", intro="Find (a) the members who have never borrowed and (b) the books that have never been borrowed.", steps=[
            S("Left join the members to their loans", text="Member M LEFT JOIN Loan L ON M.MemberID = L.MemberID returns 8 rows: the 7 loans plus one row for Tchoua with LoanID NULL."),
            S("Keep the unmatched rows", text="Add WHERE L.LoanID IS NULL. Only Tchoua remains."),
            S("Repeat for books", text="Book B LEFT JOIN Loan L ON B.BookID = L.BookID WHERE L.LoanID IS NULL returns A Level Physics and Chemistry Notes."),
        ]),
        CODE('''
SELECT M.Name, L.LoanID
FROM Member M LEFT JOIN Loan L ON M.MemberID = L.MemberID
ORDER BY M.MemberID, L.LoanID;

Name    LoanID
------  ------
Abena   1
Abena   2
Bih     3
Nkeng   4
Nkeng   5
Nkeng   6
Tchoua  NULL
Fomba   7
(8 rows)

SELECT M.Name FROM Member M LEFT JOIN Loan L ON M.MemberID = L.MemberID
WHERE L.LoanID IS NULL;                       -> Tchoua

SELECT B.Title FROM Book B LEFT JOIN Loan L ON B.BookID = L.BookID
WHERE L.LoanID IS NULL ORDER BY B.Title;      -> A Level Physics, Chemistry Notes
''', "sql", title="Listing 3: LEFT JOIN and the IS NULL test"),
        H("Joining a table to itself"),
        T("To find pairs of members from the same town, join Member to itself. The two copies need different aliases. The condition A.MemberID < B.MemberID stops a member being paired with themselves and stops each pair appearing twice."),
        CODE('''
SELECT A.Name AS Member1, B.Name AS Member2, A.Town
FROM Member A JOIN Member B ON A.Town = B.Town AND A.MemberID < B.MemberID;

Member1  Member2  Town
-------  -------  ----
Abena    Nkeng    Buea
(1 row)
''', "sql", title="Listing 4: a self-join"),
        MISTAKE("Putting a filter on the right table in WHERE after a LEFT JOIN", "Run with WHERE L.LoanDate >= '2026-02-01', the LEFT JOIN returned only 4 rows and lost Abena, Bih and Tchoua: the filter rejects the NULL rows. To keep every member and still filter the loans, put the condition in ON: ... ON M.MemberID = L.MemberID AND L.LoanDate >= '2026-02-01'. That returned 7 rows, with NULL dates for Abena, Bih and Tchoua."),
        MISTAKE("Forgetting the join condition", "FROM Member, Book with no condition returns 30 rows for 5 members and 6 books. Always write ON (or a WHERE condition) for every join."),
        QUIZ("Using Table 1, how many rows does SELECT M.Name FROM Member M INNER JOIN Loan L ON M.MemberID = L.MemberID; return?",
             ["5", "7", "8", "35"], 1,
             "An inner join returns one row per matching pair. There are 7 loans, each matching one member, so there are 7 rows (Nkeng appears 3 times, Abena twice).",
             hint="Count the loans: each loan matches exactly one member.",
             feedback=["That is the number of members. A member with several loans appears several times, and Tchoua (no loan) does not appear.", "", "A LEFT JOIN would return 8 rows, including Tchoua with NULL. An INNER JOIN leaves her out.", "35 would be a Cartesian product of 5 members and 7 loans, which happens when ON is missing."]),
        QUIZ("Which query returns the members who have never borrowed a book?",
             ["SELECT M.Name FROM Member M INNER JOIN Loan L ON M.MemberID = L.MemberID WHERE L.LoanID IS NULL;", "SELECT M.Name FROM Member M LEFT JOIN Loan L ON M.MemberID = L.MemberID WHERE L.LoanID IS NULL;", "SELECT M.Name FROM Member M LEFT JOIN Loan L ON M.MemberID = L.MemberID WHERE L.LoanID = NULL;", "SELECT M.Name FROM Loan L LEFT JOIN Member M ON M.MemberID = L.MemberID WHERE M.MemberID IS NULL;"], 1,
             "A LEFT JOIN keeps every member. Members with no loan have NULL in L.LoanID, so IS NULL selects exactly them.",
             hint="You need a join that keeps the unmatched members, and a correct test for NULL.",
             feedback=["An inner join drops unmatched members, so no row can have a NULL LoanID.", "", "= NULL is never true, so no rows are returned.", "The tables are the wrong way round: this keeps all loans and looks for loans with no member, which the foreign key makes impossible."]),
        H("Practice questions"),
        PQ("Write a query listing each book title with the name of each member who borrowed it, and give the number of rows it returns for Table 1.",
           "SELECT B.Title, M.Name FROM Loan L JOIN Book B ON L.BookID = B.BookID JOIN Member M ON L.MemberID = M.MemberID; It returns 7 rows, one per loan, because every loan matches exactly one book and one member."),
        PQ("Write a query for the titles borrowed by members who live in Buea, and give the output.",
           "SELECT B.Title, M.Name FROM Book B JOIN Loan L ON B.BookID = L.BookID JOIN Member M ON L.MemberID = M.MemberID WHERE M.Town = 'Buea' ORDER BY B.Title, M.Name; Output: Database Basics (Nkeng); Python for Schools (Abena); Python for Schools (Nkeng); The Joys of Motherhood (Nkeng); Things Fall Apart (Abena): 5 rows."),
        PQ("Explain the difference between INNER JOIN and LEFT JOIN, using Tchoua as the example.",
           "An INNER JOIN keeps only the rows with a match in both tables, so Tchoua (no loans) does not appear. A LEFT JOIN keeps every row of the left table, so Tchoua appears once with NULL in the Loan columns."),
        PQ("Write a query for pairs of members who live in the same town and give its output for Table 1.",
           "SELECT A.Name AS Member1, B.Name AS Member2, A.Town FROM Member A JOIN Member B ON A.Town = B.Town AND A.MemberID < B.MemberID; Only Abena and Nkeng share a town (Buea), so the output is one row: Abena, Nkeng, Buea. The condition A.MemberID < B.MemberID avoids pairing a member with themselves and avoids listing the pair twice."),
        SUM("An INNER JOIN with an ON condition keeps only matching rows; with no condition you get a Cartesian product.",
            "Match a foreign key to the primary key it refers to, and use aliases such as L, M and B.",
            "LEFT JOIN keeps every left row and fills missing right columns with NULL; LEFT JOIN with IS NULL finds rows with no match.",
            "A filter on the right table in WHERE turns a LEFT JOIN into an inner join; put it in ON to keep the unmatched rows.",
            "A self-join uses two aliases of the same table."),
    ],
))

# ---------------------------------------------------------------------------
# SQL 4: aggregation, GROUP BY, HAVING and nested subqueries
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Relational Databases",
    topic="SQL",
    title="SQL aggregation, GROUP BY, HAVING and nested subqueries",
    slug="csd-sql-aggregation-subqueries",
    minutes=26,
    summary="Summarise data with COUNT, SUM, AVG, MIN and MAX, group rows with GROUP BY and HAVING, and answer harder questions with nested subqueries using IN, EXISTS and scalar subqueries, all run in sqlite3.",
    objectives=[
        "Use the aggregate functions and explain how they treat NULL",
        "Write GROUP BY queries and decide between WHERE and HAVING",
        "Combine joins with GROUP BY without losing members who have no rows",
        "Write nested subqueries with IN, NOT IN, EXISTS and a single-value comparison"
    ],
    key_concepts=["Aggregate function", "GROUP BY", "HAVING", "Subquery", "Scalar subquery", "IN", "EXISTS", "Correlated subquery", "NULL"],
    blocks=[
        H("Introduction"),
        T("The head librarian in Limbe wants totals and averages, not lists: the number of books in each category, the average price, which member borrows most. SQL answers these with **aggregate functions** that summarise many rows into one value. She also asks questions such as \"Which books cost more than the average?\" where one query must use the answer of another. That is a **subquery**."),
        T("The data are the library tables from the last lessons: 6 books (prices 3500, 6000, 8500, 7000, 4000, 5000), 5 members and 7 loans. Every query here was run in sqlite3."),
        H("Aggregate functions"),
        KEY("The five aggregate functions", "Each takes a column (or * for COUNT) and returns one value for the whole group of rows.", cards=[
            ["COUNT(*)", "Number of rows. COUNT(Author) counts only rows where Author is not NULL."],
            ["SUM(col)", "Total of the values. NULL values are ignored."],
            ["AVG(col)", "Mean of the values, ignoring NULL."],
            ["MIN(col), MAX(col)", "Smallest and largest value."],
        ]),
        CODE('''
SELECT COUNT(*) AS Books, COUNT(Author) AS WithAuthor, SUM(Price) AS Total,
       AVG(Price) AS Average, MIN(Price) AS Cheapest, MAX(Price) AS Dearest
FROM Book;

Books  WithAuthor  Total  Average            Cheapest  Dearest
-----  ----------  -----  -----------------  --------  -------
6      5           34000  5666.666666666667  3500      8500
(1 row)
''', "sql", title="Listing 1: aggregates over the whole table"),
        T("Notice that COUNT(*) gives 6 but COUNT(Author) gives 5, because Chemistry Notes has Author = NULL. On an empty set of rows, COUNT returns 0, but SUM returns NULL (a query for the SUM of the prices of category Music returned NULL when run)."),
        H("GROUP BY and HAVING"),
        D("**GROUP BY** splits the rows into groups that have the same value in the named columns, and each aggregate is calculated once per group. **HAVING** filters the groups after the aggregates are calculated. **WHERE** filters the rows before they are grouped.",
          title="GROUP BY, WHERE and HAVING"),
        EX("Worked example 1: categories with a high total", intro="For books priced above 4000 FCFA, list each category whose total price is more than 8000.", steps=[
            S("WHERE first (rows)", text="Price > 4000 removes Things Fall Apart (3500) and The Joys of Motherhood (4000, which is not above 4000). Four books remain: Python for Schools 6000, A Level Physics 8500, Database Basics 7000, Chemistry Notes 5000."),
            S("GROUP BY Category", text="Computing: 6000 + 7000. Science: 8500 + 5000."),
            S("SUM for each group", text="Computing 13000 and Science 13500."),
            S("HAVING (groups)", text="HAVING SUM(Price) > 8000 keeps both groups. The result has 2 rows."),
        ]),
        CODE('''
SELECT Category, SUM(Price) AS Total
FROM Book
WHERE Price > 4000
GROUP BY Category
HAVING SUM(Price) > 8000
ORDER BY Category;

Category   Total
---------  -----
Computing  13000
Science    13500
(2 rows)

SELECT Category, COUNT(*) AS Titles, AVG(Price) AS AvgPrice
FROM Book GROUP BY Category ORDER BY Category;

Category   Titles  AvgPrice
---------  ------  --------
Computing  2       6500.0
Novel      2       3750.0
Science    2       6750.0
(3 rows)
''', "sql", title="Listing 2: WHERE, GROUP BY and HAVING"),
        TIP("The order SQL works in is: FROM and JOIN, then WHERE, then GROUP BY, then HAVING, then SELECT, then ORDER BY. That is why WHERE cannot use an aggregate such as SUM (the groups do not exist yet) and why HAVING can."),
        H("Grouping after a join"),
        EX("Worked example 2: loans per member", intro="List every member with the number of loans, including those with none, most loans first.", steps=[
            S("Use a LEFT JOIN", text="Member M LEFT JOIN Loan L ON M.MemberID = L.MemberID keeps Tchoua, who has no loans."),
            S("Group by the member", text="GROUP BY M.MemberID, M.Name."),
            S("Count the right column", text="COUNT(L.LoanID) counts only real loans, so Tchoua gets 0. COUNT(*) would count the NULL row and wrongly give Tchoua 1."),
            S("Sort", text="ORDER BY Loans DESC, M.Name."),
        ]),
        CODE('''
SELECT M.Name, COUNT(L.LoanID) AS Loans
FROM Member M LEFT JOIN Loan L ON M.MemberID = L.MemberID
GROUP BY M.MemberID, M.Name
ORDER BY Loans DESC, M.Name;

Name    Loans
------  -----
Nkeng   3
Abena   2
Bih     1
Fomba   1
Tchoua  0
(5 rows)
''', "sql", title="Listing 3: grouping after a LEFT JOIN (with COUNT(*) instead, Tchoua showed 1)"),
        H("Subqueries"),
        D("A **subquery** is a SELECT statement inside another statement, written in brackets. The outer query uses its result. A subquery that returns a single value can be used with =, <, >. One that returns a list of values is used with IN or NOT IN. EXISTS tests whether a subquery returns any row at all.",
          title="Subquery"),
        EX("Worked example 3: three kinds of subquery", intro="Answer each question with a subquery and check by running it.", steps=[
            S("(a) Single value: books dearer than the average", text="WHERE Price > (SELECT AVG(Price) FROM Book). The average is 5666.67, so the result is Python for Schools 6000, Database Basics 7000 and A Level Physics 8500."),
            S("(b) List with IN: members who borrowed Python for Schools (book 2)", text="WHERE MemberID IN (SELECT MemberID FROM Loan WHERE BookID = 2). Result: Abena, Bih, Nkeng."),
            S("(c) Nested one level deeper: members who borrowed any Computing book", text="WHERE MemberID IN (SELECT MemberID FROM Loan WHERE BookID IN (SELECT BookID FROM Book WHERE Category = 'Computing')). Result: Abena, Bih, Nkeng. Work from the innermost query outwards."),
            S("(d) NOT IN and EXISTS", text="Members with no loan: WHERE MemberID NOT IN (SELECT MemberID FROM Loan) gives Tchoua. Members with a loan on or after 1 February 2026: WHERE EXISTS (SELECT 1 FROM Loan L WHERE L.MemberID = M.MemberID AND L.LoanDate >= '2026-02-01') gives Fomba and Nkeng."),
        ]),
        CODE('''
SELECT Title, Price FROM Book
WHERE Price > (SELECT AVG(Price) FROM Book) ORDER BY Price;

Title               Price
------------------  -----
Python for Schools  6000
Database Basics     7000
A Level Physics     8500
(3 rows)

SELECT Name FROM Member
WHERE MemberID IN (SELECT MemberID FROM Loan GROUP BY MemberID HAVING COUNT(*) >= 2)
ORDER BY Name;

Name
-----
Abena
Nkeng
(2 rows)
''', "sql", title="Listing 4: a scalar subquery and a subquery with GROUP BY"),
        MISTAKE("The NOT IN trap with NULL", "If the subquery returns a NULL, NOT IN is never true for any row. Running SELECT Title FROM Book WHERE Author NOT IN (SELECT Author FROM Book WHERE Category = 'Science') returned 0 rows, because Chemistry Notes has Author NULL. Add AND Author IS NOT NULL inside the subquery, or use NOT EXISTS or a LEFT JOIN."),
        MISTAKE("Using WHERE with an aggregate", "WHERE SUM(Price) > 8000 is an error, because WHERE works on single rows. Use HAVING SUM(Price) > 8000 after GROUP BY."),
        MISTAKE("Selecting a column that is not grouped", "SELECT Category, Title, COUNT(*) FROM Book GROUP BY Category is invalid in standard SQL: each group has several titles. SQLite does not stop you and returns an arbitrary title, which is worse. Every selected column must be in GROUP BY or inside an aggregate."),
        QUIZ("Using the library data, which query returns the number of books that have a recorded author?",
             ["SELECT COUNT(*) FROM Book;", "SELECT COUNT(Author) FROM Book;", "SELECT SUM(Author) FROM Book;", "SELECT COUNT(DISTINCT Price) FROM Book;"], 1,
             "COUNT(Author) counts only the rows where Author is not NULL. It returns 5. COUNT(*) counts all 6 rows.",
             hint="Which form of COUNT skips NULL values?",
             feedback=["COUNT(*) counts every row, including the book with no author: it returns 6.", "", "SUM adds numbers; it does not count rows and is not meant for text.", "That counts the different prices (6 of them), not the authors."]),
        QUIZ("What is the difference between WHERE and HAVING?",
             ["WHERE filters groups; HAVING filters rows", "WHERE filters rows before grouping; HAVING filters groups after aggregates are calculated", "They are the same, but HAVING is newer", "WHERE can use aggregates; HAVING cannot"], 1,
             "SQL filters rows with WHERE first, then groups them, then filters the groups with HAVING, which can use aggregate functions.",
             hint="Think about the order: FROM, WHERE, GROUP BY, HAVING.",
             feedback=["This is the wrong way round.", "", "They run at different stages and are not interchangeable.", "It is the other way round: aggregates are allowed in HAVING, not in WHERE."]),
        H("Practice questions"),
        PQ("Write a query for the number of loans each book has had, most borrowed first, for the books that were borrowed. Give the output.",
           "SELECT B.Title, COUNT(*) AS TimesBorrowed FROM Loan L JOIN Book B ON L.BookID = B.BookID GROUP BY B.BookID, B.Title ORDER BY TimesBorrowed DESC, B.Title; Output: Python for Schools 3; Things Fall Apart 2; Database Basics 1; The Joys of Motherhood 1. (Books never borrowed do not appear, because the join is an inner join.)"),
        PQ("Write a query for the categories whose average price is above 5000, and give the output.",
           "SELECT Category, AVG(Price) AS AvgPrice FROM Book GROUP BY Category HAVING AVG(Price) > 5000 ORDER BY Category; Output: Computing 6500.0 and Science 6750.0. Novel averages 3750.0 and is removed by HAVING."),
        PQ("Use a nested subquery to list the books that have never been borrowed, and explain what happens if Loan.BookID could contain NULL.",
           "SELECT Title FROM Book WHERE BookID NOT IN (SELECT BookID FROM Loan) ORDER BY Title; Output: A Level Physics and Chemistry Notes. If Loan.BookID could be NULL, the NOT IN would return no rows at all, because a comparison with NULL is never true. Add WHERE BookID IS NOT NULL inside the subquery or use NOT EXISTS."),
        PQ("Explain why COUNT(*) is wrong for counting loans per member after a LEFT JOIN, and how to correct it.",
           "After a LEFT JOIN, a member with no loans still has one row, with NULL in the Loan columns. COUNT(*) counts that row, so Tchoua would show 1 loan. COUNT(L.LoanID) ignores the NULL and gives 0."),
        SUM("Aggregates (COUNT, SUM, AVG, MIN, MAX) summarise rows into one value and ignore NULL, except COUNT(*).",
            "GROUP BY makes one result row per group; every selected column must be grouped or aggregated.",
            "WHERE filters rows before grouping; HAVING filters groups after aggregates are calculated.",
            "After a LEFT JOIN, count a column from the right table, not *, to get 0 for rows with no match.",
            "Subqueries return a single value (with =, >), a list (IN, NOT IN) or a yes/no test (EXISTS); NOT IN fails if the list contains NULL."),
    ],
))

# ---------------------------------------------------------------------------
# OOP 1: classes, abstraction and encapsulation
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Object-Oriented Programming",
    topic="OOP principles",
    title="Abstraction and encapsulation: protecting data inside objects",
    slug="csd-oop-abstraction-encapsulation",
    minutes=24,
    summary="Build a mobile money Wallet class that hides its balance behind methods (encapsulation), use an abstract class to say what every subclass must do (abstraction), and see what Python private names really do.",
    objectives=[
        "Define class, object, attribute and method with a Python example",
        "Explain encapsulation and show how validation in methods protects an attribute",
        "Explain abstraction and use an abstract class with an abstract method",
        "State accurately what a double-underscore name does in Python"
    ],
    key_concepts=["Class", "Object", "Attribute", "Method", "Encapsulation", "Abstraction", "Abstract class", "Property", "Private attribute"],
    blocks=[
        H("Introduction"),
        T("A mobile money agent in Bafoussam handles hundreds of wallets a day. If every part of the program can change a wallet's balance directly, one careless line can set a balance to a million FCFA, or let a customer withdraw more than they own. Object-oriented programming (OOP) prevents this by keeping the data and the code that is allowed to change it together, inside an **object**."),
        D("A **class** is a blueprint that defines the attributes (data) and methods (behaviour) of a kind of object. An **object** is one instance of a class with its own attribute values. A **method** is a function defined in a class; **self** is the object the method was called on.",
          title="Class and object"),
        KEY("Two principles in this lesson", "The next lesson covers inheritance and polymorphism.", cards=[
            ["Encapsulation", "Bundle data and methods in one class and hide the data, so it can only be changed through methods that check the change."],
            ["Abstraction", "Show only what a user needs (what an object can do) and hide the detail of how it does it."],
        ]),
        H("Encapsulation"),
        T("In the Wallet class below the balance is stored in an attribute whose name starts with two underscores. Outside code does not change it directly. It calls deposit and withdraw, and each of those checks the amount first. The balance can be read through a **property**, a method that is used like an attribute but has no setter, so it cannot be assigned."),
        CODE('''
class Wallet:
    MIN_DEPOSIT = 100

    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = 0
        if balance > 0:
            self.deposit(balance)

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < Wallet.MIN_DEPOSIT:
            raise ValueError("deposit below minimum")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount

    def __str__(self):
        return f"{self.__owner}: {self.__balance} FCFA"
''', "python", title="Listing 1: an encapsulated Wallet class"),
        EX("Worked example 1: using the Wallet", intro="Trace this program and give its output.", steps=[
            S("Create the wallet", text="w = Wallet(\"Abena\", 5000): __init__ sets the balance to 0 and then calls deposit(5000), so the amount passes the minimum check. Balance 5000."),
            S("Deposit and withdraw", text="w.deposit(2500) gives 7500. w.withdraw(1000) gives 6500."),
            S("Print", text="print(w) calls __str__ and shows Abena: 6500 FCFA. print(w.balance) shows 6500."),
            S("Invalid actions", text="w.deposit(50) is below the minimum of 100 and raises ValueError. w.withdraw(99999) is more than the balance and raises ValueError. In both cases the balance stays 6500."),
        ]),
        CODE('''
w = Wallet("Abena", 5000)
w.deposit(2500)
w.withdraw(1000)
print(w)
print(w.balance)
for action, amount in [("deposit", 50), ("withdraw", 99999)]:
    try:
        getattr(w, action)(amount)
    except ValueError as e:
        print("Refused:", e)
try:
    w.balance = 1000000
except AttributeError as e:
    print("AttributeError:", e)

Output:
Abena: 6500 FCFA
6500
Refused: deposit below minimum
Refused: insufficient funds
AttributeError: property 'balance' of 'Wallet' object has no setter
''', "python", title="Listing 2: using the class (output from running it in Python 3.13)"),
        D("**Encapsulation** means bundling the data and the methods that work on it in one class and restricting direct access to the data. Outside code uses the public methods, so the class can guarantee that its data is always valid.",
          title="Encapsulation", note="Benefits: the data is always checked, the inside of the class can change without breaking other code, and the code is easier to test."),
        H("What a private name really means in Python"),
        T("Python has no true private attributes. A name beginning with two underscores, such as __balance, is renamed inside the class to _Wallet__balance (**name mangling**). This stops accidental use, not deliberate use. Languages such as Java and C++ have a private keyword that the compiler enforces."),
        CODE('''
w.__balance = 1000000     # outside the class: creates a NEW attribute
print(w.balance)          # 6500   the real balance is untouched
print(w._Wallet__balance) # 6500   the mangled name still reaches it
''', "python", title="Listing 3: assigning to __balance from outside"),
        TIP("In Python, one underscore (_name) is a convention that means \"internal: please do not use\". Two underscores (__name) trigger name mangling. In an exam, say that Python relies on convention and programmer discipline, while Java enforces private."),
        H("Abstraction"),
        D("**Abstraction** means showing the essential features of something and hiding unnecessary detail. In a class, it means defining *what* an object can do (its interface) without saying *how*. An **abstract class** is a class that cannot be instantiated. It can declare **abstract methods**, which every concrete subclass must implement.",
          title="Abstraction"),
        T("A school's staff are paid in different ways, but every kind of staff member must be able to report a monthly pay. The abstract class Staff states this rule. It does not know how each kind is paid."),
        CODE('''
from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name, base_salary):
        self._name = name
        self._base_salary = base_salary

    @abstractmethod
    def monthly_pay(self):
        """Every kind of staff member must say how it is paid."""

class Bursar(Staff):
    def monthly_pay(self):
        return self._base_salary + 20000

class Cleaner(Staff):
    pass

print(Bursar("Mrs Ewane", 110000).monthly_pay())
for cls in (Staff, Cleaner):
    try:
        cls("X", 1)
    except TypeError as e:
        print("TypeError:", e)

Output:
130000
TypeError: Can't instantiate abstract class Staff without an implementation for abstract method 'monthly_pay'
TypeError: Can't instantiate abstract class Cleaner without an implementation for abstract method 'monthly_pay'
''', "python", title="Listing 4: an abstract class (the exact wording of the TypeError differs between Python versions)"),
        EX("Worked example 2: what the abstract class guarantees", intro="Explain the output of Listing 4.", steps=[
            S("Bursar", text="Bursar implements monthly_pay, so it can be created. 110000 + 20000 = 130000."),
            S("Staff", text="Staff is abstract and cannot be instantiated: a general staff member with no way to calculate pay does not exist."),
            S("Cleaner", text="Cleaner inherits from Staff but does not implement monthly_pay, so it is still abstract and also cannot be created."),
            S("The design benefit", text="Code that handles Staff objects can call monthly_pay() on any of them, knowing that every concrete class has it."),
        ]),
        MISTAKE("Confusing abstraction with encapsulation", "Encapsulation is about protecting data by hiding it behind methods. Abstraction is about simplifying: presenting only the essential features and leaving out the detail. A good answer gives one example of each, such as the private balance (encapsulation) and the abstract monthly_pay (abstraction)."),
        MISTAKE("Saying that private attributes make a program secure", "Making an attribute private is a design tool that prevents mistakes and helps maintenance. It is not security: in Python the mangled name is still reachable."),
        QUIZ("In the Wallet class, why does deposit check that the amount is at least 100 before changing the balance?",
             ["To make the program run faster", "To make sure the object's data is always valid, which is the purpose of encapsulation", "Because Python requires every method to raise an exception", "To hide the balance from the user"], 1,
             "Putting the check inside the method that changes the data means no outside code can store an invalid value. That is encapsulation in action.",
             hint="Who is responsible for keeping the balance valid: the caller or the class?",
             feedback=["The check has no useful effect on speed.", "", "Python does not require this; the exception is the class's way of refusing a bad request.", "Hiding is done by the double underscore name; the check is about validity."]),
        QUIZ("What happens when a program runs Staff(\"X\", 1), where Staff is an abstract class with an abstract method?",
             ["A staff object is created with no pay method", "A TypeError is raised because an abstract class cannot be instantiated", "The abstract method runs and returns None", "A new concrete subclass is created automatically"], 1,
             "An abstract class is an incomplete design. Python refuses to create an object from it.",
             hint="Can you create an object when some of its methods are not implemented?",
             feedback=["Python does not allow this for classes with unimplemented abstract methods.", "", "The method is never called, because no object is created.", "Python never creates subclasses for you."]),
        H("Practice questions"),
        PQ("Define encapsulation and give two benefits, using the Wallet class as your example.",
           "Encapsulation bundles the data (the balance) and the methods that use it (deposit, withdraw) in one class, and restricts direct access to the data. Benefits: the balance can only change through methods that validate the amount, so it is always valid; and the inside of the class (for example how the balance is stored) can change without breaking code that uses the class."),
        PQ("A programmer writes w.balance = 1000000 and Python raises an AttributeError. Explain why.",
           "balance is defined as a property with no setter, so it can be read but not assigned. The only way to change the balance is through deposit and withdraw, which check the amount. This protects the data."),
        PQ("Explain the difference between abstraction and encapsulation and give one example of each from a school system.",
           "Abstraction shows only the essential features and leaves out detail: an abstract class Staff says every staff member has monthly_pay() without saying how it is calculated. Encapsulation hides data behind methods: a Student class keeps its marks in a private attribute and changes them only through add_mark(), which rejects marks outside 0 to 100."),
        PQ("Write a Python class Counter that stores a private count starting at 0, has a method increment() that adds 1 and a read-only property value. Show that value cannot be set.",
           "The class: class Counter with __init__(self) setting self.__count = 0; a method increment(self) doing self.__count += 1; and a method value(self) returning self.__count, decorated with @property. After c = Counter(), c.increment() twice, print(c.value) prints 2. The statement c.value = 10 raises AttributeError because the property has no setter."),
        SUM("A class is a blueprint; an object is an instance with its own attribute values; methods are functions inside the class.",
            "Encapsulation bundles data with the methods that use it and hides the data so it can only change through checked methods.",
            "A property gives read access without allowing assignment.",
            "Abstraction shows the essential interface and hides detail; an abstract class cannot be instantiated and forces subclasses to implement its abstract methods.",
            "Python private names (__x) are name-mangled, not truly private; Java's private is enforced by the compiler."),
    ],
))

# ---------------------------------------------------------------------------
# OOP 2: inheritance and polymorphism
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Object-Oriented Programming",
    topic="OOP principles",
    title="Inheritance and polymorphism: reusing and specialising classes",
    slug="csd-oop-inheritance-polymorphism",
    minutes=25,
    summary="Build subclasses from a Staff superclass, override methods and call super(), use polymorphism to treat different objects through one interface, and choose between inheritance (is-a) and composition (has-a).",
    objectives=[
        "Create a subclass that inherits attributes and methods and adds its own",
        "Override a method and call the superclass version with super()",
        "Explain polymorphism and show it with a list of mixed objects",
        "Distinguish is-a (inheritance) from has-a (composition) relationships"
    ],
    key_concepts=["Inheritance", "Superclass", "Subclass", "Overriding", "super()", "Polymorphism", "Method resolution order", "Composition", "Operator overloading"],
    blocks=[
        H("Introduction"),
        T("A secondary school in Bamenda pays teachers by the number of periods they teach, the bursar a fixed allowance, and the driver by the number of trips. Writing three unrelated classes would repeat the same name, salary and payslip code three times. **Inheritance** lets one class build on another, so the shared parts are written once. **Polymorphism** then lets the payroll treat all staff in the same way."),
        D("**Inheritance** lets a **subclass** (child class) receive the attributes and methods of a **superclass** (parent class), and add or change behaviour. It models an **is-a** relationship: a Teacher is a Staff member.",
          title="Inheritance"),
        D("**Overriding** means a subclass provides its own version of a method that the superclass already defines. **super()** gives access to the superclass version, so the subclass can extend it instead of rewriting it.",
          title="Overriding and super()"),
        IMG("al-csd-uml-staff.svg",
            "UML class diagram: abstract class Staff with monthly_pay and payslip. Teacher, Bursar and Driver each inherit from Staff (hollow arrows). Teacher has a private periods attribute, Driver a private trips attribute, and Driver also overrides payslip.",
            caption="Figure 1. The Staff class hierarchy used in this lesson."),
        H("A class hierarchy for payroll"),
        CODE('''
from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name, base_salary):
        self._name = name
        self._base_salary = base_salary

    @abstractmethod
    def monthly_pay(self):
        """Every kind of staff member must say how it is paid."""

    def payslip(self):
        return f"{self._name} ({type(self).__name__}): {self.monthly_pay()} FCFA"


class Teacher(Staff):
    def __init__(self, name, base_salary, periods):
        super().__init__(name, base_salary)
        self.__periods = periods

    def monthly_pay(self):
        return self._base_salary + self.__periods * 1500


class Bursar(Staff):
    def monthly_pay(self):
        return self._base_salary + 20000


class Driver(Staff):
    def __init__(self, name, base_salary, trips):
        super().__init__(name, base_salary)
        self.__trips = trips

    def monthly_pay(self):
        return self._base_salary + self.__trips * 2000

    def payslip(self):
        return super().payslip() + f" [{self.__trips} trips]"
''', "python", title="Listing 1: the Staff hierarchy"),
        EX("Worked example 1: what each subclass inherits and changes", intro="Describe what Teacher, Bursar and Driver each inherit from Staff and what each adds or overrides.", steps=[
            S("Inherited by all three", text="The attributes _name and _base_salary (set by Staff.__init__) and the method payslip."),
            S("Teacher", text="Adds a private attribute periods and calls super().__init__ so the Staff attributes are also set. Implements monthly_pay as base + 1500 per period."),
            S("Bursar", text="Adds nothing new. It inherits __init__ unchanged and only implements monthly_pay (base + 20000)."),
            S("Driver", text="Adds trips, implements monthly_pay, and overrides payslip: it calls super().payslip() to get the usual text and then adds the number of trips."),
        ]),
        H("Polymorphism"),
        D("**Polymorphism** (\"many forms\") means that the same method call can behave differently depending on the class of the object it is called on. Code can use a superclass type and call a method, and each object runs its own version.",
          title="Polymorphism"),
        CODE('''
team = [Teacher("Mr Tabi", 90000, 12), Bursar("Mrs Ewane", 110000), Driver("Mr Njoh", 60000, 8)]
for s in team:
    print(s.payslip())
print("Total:", sum(s.monthly_pay() for s in team))
print(isinstance(team[0], Staff), isinstance(team[0], Bursar))
print(issubclass(Driver, Staff))
print([c.__name__ for c in Driver.__mro__])

Output (run in Python 3.13):
Mr Tabi (Teacher): 108000 FCFA
Mrs Ewane (Bursar): 130000 FCFA
Mr Njoh (Driver): 76000 FCFA [8 trips]
Total: 314000
True False
True
['Driver', 'Staff', 'ABC', 'object']
''', "python", title="Listing 2: one loop, three behaviours"),
        EX("Worked example 2: tracing the polymorphic loop", intro="Explain how the loop calls the right version of monthly_pay for each object, and check the totals.", steps=[
            S("The loop does not test the type", text="s.payslip() and s.monthly_pay() are written once. Python looks at the class of each object when the call is made (dynamic dispatch)."),
            S("Teacher", text="90000 + 12 × 1500 = 90000 + 18000 = 108000."),
            S("Bursar", text="110000 + 20000 = 130000."),
            S("Driver", text="60000 + 8 × 2000 = 76000. The overridden payslip adds the text [8 trips]."),
            S("Total", text="108000 + 130000 + 76000 = 314000, as printed."),
            S("Adding a new type", text="A Cook class that implements monthly_pay can be added to the list and the loop works without any change."),
        ]),
        T("The last output line shows the **method resolution order**: when a method is called on a Driver, Python looks in Driver first, then Staff, then ABC, then object. isinstance(team[0], Staff) is True because a Teacher is a Staff, and False for Bursar because a Teacher is not a Bursar."),
        H("Polymorphism with operators, and has-a relationships"),
        CODE('''
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))
print(3 + 4, "ab" + "cd")

class Engine:
    def start(self): return "Engine running"
class Car:
    def __init__(self): self.engine = Engine()     # a Car HAS an Engine
    def start(self): return self.engine.start()
print(Car().start())

Output:
(4, 6)
7 abcd
Engine running
''', "python", title="Listing 3: operator overloading and composition"),
        T("The operator + is polymorphic: it adds numbers, joins strings and, with __add__, adds vectors. A class can define __add__ to give + a meaning for its own objects (operator overloading)."),
        KEY("Inheritance or composition?", "Ask which sentence is true.", cards=[
            ["is-a: use inheritance", "A Teacher is a Staff member. A Bursar is a Staff member."],
            ["has-a: use composition", "A Car has an Engine. A School has Staff. The Car holds an Engine object in an attribute."],
        ]),
        MISTAKE("Using inheritance for a has-a relationship", "A Car is not an Engine. If you make Car inherit from Engine, a Car would be treated like an Engine everywhere. Use an attribute that refers to an Engine object instead."),
        MISTAKE("Forgetting to call super().__init__", "In Teacher, leaving out super().__init__(name, base_salary) means the attributes _name and _base_salary are never created, and monthly_pay fails with an AttributeError when it runs."),
        QUIZ("Which statement describes polymorphism?",
             ["A class receives the attributes of another class", "The same method call produces behaviour that depends on the object's class", "Data is hidden inside a class", "A class cannot be instantiated"], 1,
             "Polymorphism means one interface, many forms. In the payroll loop, s.monthly_pay() runs a different method for a Teacher, a Bursar and a Driver.",
             hint="Which option involves the same call giving different results?",
             feedback=["That is inheritance.", "", "That is encapsulation.", "That describes an abstract class."]),
        QUIZ("In Listing 1, what does super().payslip() do inside Driver.payslip?",
             ["It calls the payslip method of the Staff class, so the standard text is produced first", "It creates a new Staff object", "It deletes the Staff version of payslip", "It calls monthly_pay of the Teacher class"], 0,
             "super() refers to the superclass. Driver.payslip reuses Staff.payslip and then adds the number of trips.",
             hint="super() points up the inheritance chain. Which class is above Driver?",
             feedback=["", "super() does not create objects; it gives access to the parent's methods.", "The parent's method is unchanged: overriding does not delete it.", "Teacher is a sibling of Driver, not its parent."]),
        H("Practice questions"),
        PQ("Define inheritance and polymorphism, and give an example of each from the Staff classes.",
           "Inheritance: a subclass receives the attributes and methods of a superclass. Teacher inherits _name, _base_salary and payslip from Staff. Polymorphism: the same method call behaves differently depending on the object's class. Calling s.monthly_pay() on a Teacher, a Bursar and a Driver in the same loop runs three different implementations."),
        PQ("A Cook class is to be added: base salary plus 500 FCFA for each meal served. Write the class so that it works in the payroll loop of Listing 2.",
           "The class: class Cook(Staff) with __init__(self, name, base_salary, meals) that calls super().__init__(name, base_salary) and stores self.__meals = meals, and a method monthly_pay(self) that returns self._base_salary + self.__meals * 500. Because Cook implements monthly_pay, it can be created and put in the team list, and the loop needs no change."),
        PQ("Explain what is wrong with making a class School inherit from Staff, and show a better design.",
           "A School is not a kind of staff member, so the is-a test fails. A school has staff: use composition. The School class holds a list of Staff objects in an attribute, for example self.staff = [], with a method add_staff(member), and its total_pay() method loops over the list."),
        PQ("State what the output of print(isinstance(Bursar(\"A\", 1), Staff)) is, and explain.",
           "True. A Bursar is a subclass of Staff, so an object of Bursar is also an instance of Staff (an is-a relationship). isinstance checks the class and all its superclasses."),
        SUM("Inheritance builds a subclass from a superclass (is-a) so shared code is written once.",
            "A subclass can override a method; super() reaches the superclass version.",
            "Polymorphism: one method call, different behaviour depending on the object's class.",
            "Python searches for a method in the method resolution order: the class, then its parents.",
            "Use inheritance for is-a and composition (an attribute holding another object) for has-a."),
    ],
))

# ---------------------------------------------------------------------------
# Classes in practice 1: UML, constructors, access modifiers
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Object-Oriented Programming",
    topic="Classes in practice",
    title="UML class diagrams, constructors, destructors and access modifiers",
    slug="csd-cls-uml-constructors-access",
    minutes=25,
    summary="Draw and read a UML class diagram with visibility symbols and multiplicities, write constructors with default values, understand class and instance attributes and destructors, and use public, protected and private access correctly.",
    objectives=[
        "Read and draw a UML class diagram with attributes, methods, visibility and relationships",
        "Write a constructor with default parameters and distinguish class and instance attributes",
        "Explain what a destructor is and what Python guarantees about it",
        "Choose public, protected or private access for an attribute and explain the effect"
    ],
    key_concepts=["UML class diagram", "Visibility", "Multiplicity", "Association", "Composition", "Constructor", "Destructor", "Class attribute", "Access modifier"],
    blocks=[
        H("Introduction"),
        T("Before a team writes a library system for a school in Limbe, they draw the classes on paper: what each class stores, what it can do and how the classes are connected. The standard way to draw this is the **UML class diagram** (Unified Modelling Language). After the drawing comes the code, and the code needs constructors to set up each object and access rules to protect its data."),
        H("UML class diagrams"),
        D("A **UML class diagram** shows each class as a box with three compartments: the class name, its attributes and its methods. Lines between the boxes show how the classes are related.",
          title="UML class diagram", note="Attributes are written name : type. Methods are written name(parameters) : return type."),
        KEY("Visibility symbols", "A symbol in front of each member shows who may use it.", cards=[
            ["+ public", "Can be used from anywhere."],
            ["# protected", "For the class and its subclasses (a convention in Python)."],
            ["- private", "For the class itself only."],
        ]),
        KEY("Relationships between classes", "The lines in the diagram use different endings.", cards=[
            ["Association", "A plain line: objects of one class use or know about objects of another (a member borrows a book). Multiplicities such as 1, 0..* or 1..* say how many."],
            ["Inheritance", "A line with a hollow triangle at the parent: the child is a kind of the parent."],
            ["Composition", "A line with a filled diamond at the whole: the parts belong to the whole (a library contains books)."],
        ]),
        IMG("al-csd-uml-library.svg",
            "UML class diagram with three classes. Library has a private name and add_book. Book has a public title, a protected shelf, a private price and the method get_price. Member has a public name and form and the method borrow. Library contains many Books (filled diamond); Member borrows many Books.",
            caption="Figure 1. A library class diagram: composition (Library and Book) and association (Member and Book)."),
        H("Constructors and class attributes"),
        D("A **constructor** is a special method that runs automatically when an object is created. It sets the initial values of the attributes. In Python it is called __init__. In Java and C++ it has the same name as the class and no return type.",
          title="Constructor"),
        D("A **class attribute** belongs to the class and is shared by every object (written in the class body, not on self). An **instance attribute** belongs to one object (written on self in the constructor).",
          title="Class and instance attributes"),
        D("A **destructor** is called when an object is destroyed. In Python it is __del__, but it runs only when the object is no longer referred to, and the exact time is not guaranteed. C++ has destructors written with a tilde (~ClassName). Java has no destructor: its garbage collector frees memory.",
          title="Destructor"),
        CODE('''
class Book:
    count = 0                       # class attribute shared by all objects

    def __init__(self, title, price=3000):
        self.title = title          # public
        self._shelf = "A1"          # protected by convention
        self.__price = price        # private (name mangled)
        Book.count += 1

    def get_price(self):
        return self.__price

    def __del__(self):
        print("Closing record for", self.title)

a = Book("Python for Schools", 6000)
b = Book("Database Basics")
print(Book.count, a.get_price(), b.get_price())
print(a.title, a._shelf)
try:
    print(a.__price)
except AttributeError as e:
    print("AttributeError:", e)
print(a._Book__price)
del a
print("after del a")
print(Book.count)

Output (Python 3.13):
2 6000 3000
Python for Schools A1
AttributeError: 'Book' object has no attribute '__price'
6000
Closing record for Python for Schools
after del a
2
Closing record for Database Basics
''', "python", title="Listing 1: constructors, class attribute, access levels and a destructor"),
        EX("Worked example 1: tracing Listing 1", intro="Explain each line of the output.", steps=[
            S("Line 1", text="Two objects were created, so Book.count is 2. a.get_price() is 6000. For b the default price 3000 was used."),
            S("Line 2", text="title is public and _shelf is only a convention, so both can be read."),
            S("Lines 3 and 4", text="a.__price fails because the real name is _Book__price. Using the mangled name a._Book__price works, which shows that Python's private is a convention enforced by renaming."),
            S("Lines 5 and 6", text="del a removes the only reference to the first object, so Python calls __del__ at once and prints Closing record for Python for Schools. The after message comes next."),
            S("Line 7", text="Book.count is still 2: nothing in the code subtracts 1 when an object is deleted. A destructor does not update class attributes unless you write that code."),
            S("Line 8", text="The second object is destroyed when the program ends, so its message is printed last."),
        ]),
        H("From a UML box to Python code"),
        EX("Worked example 2: UML to code", intro="A UML box shows Student with - name : str, - marks : list, + add_mark(mark : int), + average() : float. Marks must be from 0 to 100. Write the class, test it and give the output.", steps=[
            S("Private attributes", text="The minus signs mean name and marks are private, so use __name and __marks, created in the constructor."),
            S("add_mark validates", text="It raises ValueError if the mark is outside 0 to 100, otherwise appends the mark."),
            S("average handles the empty case", text="If there are no marks, return 0.0 to avoid dividing by zero."),
            S("Test it", text="Add 70, 85, 90: average = 245 / 3 = 81.67, printed as 81.7 when rounded to 1 decimal place. A student with no marks has average 0.0. add_mark(120) raises ValueError."),
        ]),
        CODE('''
class Student:
    def __init__(self, name):
        self.__name = name
        self.__marks = []

    def add_mark(self, mark):
        if not 0 <= mark <= 100:
            raise ValueError("mark must be 0 to 100")
        self.__marks.append(mark)

    def average(self):
        if not self.__marks:
            return 0.0
        return sum(self.__marks) / len(self.__marks)

s = Student("Abena")
for m in (70, 85, 90):
    s.add_mark(m)
print(round(s.average(), 1))
print(Student("Bih").average())
try:
    s.add_mark(120)
except ValueError as e:
    print("Refused:", e)

Output:
81.7
0.0
Refused: mark must be 0 to 100
''', "python", title="Listing 2: the Student class from its UML box"),
        KEY("Choosing an access level", "A simple rule that works for most classes.", cards=[
            ["Attributes: private by default", "Make them private and give access through methods, so the class can validate changes."],
            ["Methods: public if others need them", "The methods other classes call are the class's public interface."],
            ["Protected for subclasses", "Use a single underscore for helpers or data a subclass may need."],
        ]),
        MISTAKE("Thinking the destructor runs at a predictable time", "In Python, __del__ runs when the last reference is removed, which may be at the end of the program, and its timing is not guaranteed. Do not rely on it to save data or release resources. Use a with statement or an explicit close method."),
        MISTAKE("Putting an instance attribute in the class body", "A list written in the class body, such as marks = [], is shared by all objects: every student would share one list of marks. Create instance attributes with self inside __init__."),
        QUIZ("In a UML class diagram, what does the line \"- price : int\" in the attributes compartment mean?",
             ["A public attribute named price of type int", "A private attribute named price of type int", "A protected method named price", "A class attribute named price of any type"], 1,
             "The minus sign means private. The text after the colon gives the type, int.",
             hint="Which visibility symbol is the minus sign?",
             feedback=["A public attribute would be shown with a plus sign.", "", "It is in the attributes compartment, so it is an attribute not a method, and # is protected.", "The type is int, and a class attribute would be shown underlined."]),
        QUIZ("Listing 1 prints Book.count as 2 after del a. What is the reason?",
             ["del a removes the class attribute", "The destructor does not change count, because no code subtracts 1", "Python resets class attributes when an object is deleted", "The second object was created after del a"], 1,
             "Deleting an object does not change class attributes. The count would drop only if __del__ contained Book.count -= 1.",
             hint="Look at what __del__ does in Listing 1.",
             feedback=["The class attribute belongs to the class and survives the deletion of any object.", "", "Python never changes class attributes by itself.", "Both objects were created before del a."]),
        H("Practice questions"),
        PQ("Draw (in words) the UML box for a class Teacher with a private name and salary, a public method pay() that returns an int and a public method teach(subject : str). State what the symbols mean.",
           "Top compartment: Teacher. Attributes compartment: - name : str and - salary : int. Methods compartment: + pay() : int and + teach(subject : str). The minus sign means private (only the class itself may use it). The plus sign means public (any code may call it)."),
        PQ("State the purpose of a constructor and write one for a class Product with a name and a price that defaults to 1000 FCFA.",
           "A constructor runs automatically when an object is created and gives its attributes their starting values. In Python: def __init__(self, name, price=1000): self.name = name; self.price = price. Product(\"Soap\") then has price 1000, and Product(\"Rice\", 22000) has price 22000."),
        PQ("Explain the difference between a class attribute and an instance attribute using a counter of students.",
           "A class attribute, written in the class body (count = 0), is shared by all objects: one copy for the class, for example the number of students created, increased in the constructor with Student.count += 1. An instance attribute, set on self in the constructor (self.name), belongs to one object, so each student has their own."),
        PQ("Describe what is meant by public, protected and private access, and say how Python differs from Java.",
           "Public members can be used from anywhere. Protected members are intended for the class and its subclasses. Private members are for the class only. Java enforces these with keywords (public, protected, private) and the compiler rejects wrong use. Python relies on naming conventions: a single underscore means protected, and a double underscore causes name mangling, which discourages access but does not forbid it."),
        SUM("A UML class box has three compartments: name, attributes and methods; + is public, # is protected, - is private.",
            "Lines show association (with multiplicity), inheritance (hollow triangle) and composition (filled diamond).",
            "A constructor sets the initial state of a new object; Python's is __init__ and can use default parameter values.",
            "A class attribute is shared by all objects; an instance attribute belongs to one object.",
            "A destructor runs when an object is destroyed, but in Python the timing is not guaranteed. Make attributes private by default."),
    ],
))

# ---------------------------------------------------------------------------
# Classes in practice 2: exception handling
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Object-Oriented Programming",
    topic="Classes in practice",
    title="Exception handling in Python: try, except, else, finally and custom exceptions",
    slug="csd-cls-exceptions",
    minutes=24,
    summary="Handle run-time errors with try, except, else and finally, raise your own exceptions, define a custom exception class and close files safely with with, using programs that were run to get their output.",
    objectives=[
        "Distinguish syntax errors, run-time exceptions and logic errors",
        "Write try, except, else and finally blocks and predict the order of the output",
        "Raise built-in exceptions and define a custom exception class",
        "Order except clauses correctly and use with to close files"
    ],
    key_concepts=["Exception", "try", "except", "else", "finally", "raise", "Custom exception", "Exception hierarchy", "with statement"],
    blocks=[
        H("Introduction"),
        T("A teacher in Bamenda types student marks into a program. One day she types the letters abc instead of a number. A program with no error handling stops with a long red message and all the marks typed so far are lost. A program with **exception handling** says \"please type a number\" and carries on."),
        D("An **exception** is an error that is detected while the program is running. If nothing handles it, the program stops. A **handler** catches the exception and lets the program recover.",
          title="Exception"),
        KEY("Three kinds of error", "Only the second kind is handled with try and except.", cards=[
            ["Syntax error", "The code breaks the rules of the language (a missing colon). Python reports it before the program runs. You must fix the code."],
            ["Run-time error (exception)", "The code is valid but something goes wrong while running: a division by zero, a missing file, bad input."],
            ["Logic error", "The program runs but gives wrong results, for example using + instead of *. No exception is raised. Testing finds it."],
        ]),
        H("try, except, else and finally"),
        CODE('''
try:
    ...            # code that might raise an exception
except SomeError:
    ...            # runs only if SomeError was raised in try
else:
    ...            # runs only if try finished with no exception
finally:
    ...            # ALWAYS runs, whether or not there was an exception
''', "python", title="Listing 1: the structure"),
        CODE('''
def read_mark(text):
    try:
        mark = int(text)
    except ValueError:
        print("Not a whole number:", repr(text))
        return None
    else:
        if not 0 <= mark <= 100:
            raise ValueError("mark must be 0 to 100")
        return mark
    finally:
        print("checked", repr(text))

for t in ["72", "abc", "150"]:
    try:
        print("result:", read_mark(t))
    except ValueError as e:
        print("rejected:", e)

Output:
checked '72'
result: 72
Not a whole number: 'abc'
checked 'abc'
result: None
checked '150'
rejected: mark must be 0 to 100
''', "python", title="Listing 2: all four clauses (output from running it in Python 3.13)"),
        EX("Worked example 1: tracing Listing 2", intro="Explain the order of the output for each of the three inputs.", steps=[
            S("Input \"72\"", text="int(\"72\") works, so except is skipped. else runs: 72 is in range, so it returns 72. Before the function returns, finally prints checked '72'. Then the caller prints result: 72."),
            S("Input \"abc\"", text="int(\"abc\") raises ValueError. The except block prints Not a whole number and returns None. finally still runs and prints checked 'abc'. The caller prints result: None."),
            S("Input \"150\"", text="int works, so else runs. 150 is out of range, so the code raises a new ValueError. finally prints checked '150' as the exception leaves the function. The caller's try/except catches it and prints rejected."),
            S("What to remember", text="finally runs in every case, even when the function returns or raises. else runs only when no exception occurred."),
        ]),
        H("Raising and defining exceptions"),
        T("Use raise to signal a problem you have detected yourself. For problems that belong to your own program, define a **custom exception**: a class that inherits from Exception. A good name tells the reader what went wrong, and the object can carry extra data."),
        CODE('''
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"balance {balance} is less than {amount}")
        self.balance = balance
        self.amount = amount

class Wallet:
    def __init__(self, balance): self.balance = balance
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

w = Wallet(5000)
for amt in [2000, 4000, -5]:
    try:
        w.withdraw(amt)
        print("withdrew", amt, "left", w.balance)
    except InsufficientFundsError as e:
        print("Refused:", e, "| short by", e.amount - e.balance)
    except ValueError as e:
        print("Invalid:", e)

Output:
withdrew 2000 left 3000
Refused: balance 3000 is less than 4000 | short by 1000
Invalid: amount must be positive
''', "python", title="Listing 3: a custom exception"),
        EX("Worked example 2: tracing the wallet", intro="Explain each line of the output of Listing 3.", steps=[
            S("2000", text="2000 is positive and not more than 5000. The balance becomes 3000. No exception, so the try block prints the withdrew line."),
            S("4000", text="4000 is more than the balance of 3000, so the method raises InsufficientFundsError(3000, 4000). The first except clause catches it. The short-by figure is 4000 - 3000 = 1000."),
            S("-5", text="The first test in withdraw fails, so it raises ValueError, which is caught by the second except clause."),
            S("Why two except clauses", text="Each kind of problem gets its own message. A custom exception lets the caller tell a lack of money from a bad input."),
        ]),
        H("Good practice"),
        D("Python checks the except clauses from top to bottom and uses the first that matches. Exceptions form a hierarchy: ZeroDivisionError is a kind of ArithmeticError, FileNotFoundError is a kind of OSError, KeyError and IndexError are kinds of LookupError, and ValueError and almost every other exception are kinds of Exception. So a general clause must come after the specific ones.",
          title="The exception hierarchy and order of clauses"),
        CODE('''
try:
    int("abc")
except Exception:          # general clause first: it catches the ValueError
    print("general")
except ValueError:         # never reached
    print("specific")

Output:
general
''', "python", title="Listing 4: the wrong order (the specific clause can never run)"),
        CODE('''
attempts = iter(["abc", "150", "72"])      # pretend these are typed by the user
while True:
    text = next(attempts)
    try:
        mark = int(text)
        if not 0 <= mark <= 100:
            raise ValueError("outside 0 to 100")
    except ValueError as e:
        print("Try again:", e)
    else:
        print("Accepted", mark)
        break

Output:
Try again: invalid literal for int() with base 10: 'abc'
Try again: outside 0 to 100
Accepted 72
''', "python", title="Listing 5: asking again until the input is valid"),
        CODE('''
with open("notes.txt", "w") as f:
    f.write("line one\\n")
print(f.closed)        # True: the file was closed when the block ended, even if an error occurred

try:
    open("missing_file.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e.strerror)

Output:
True
FileNotFoundError: No such file or directory
''', "python", title="Listing 6: with closes the file; FileNotFoundError for a missing file"),
        TIP("In the exam, say which exception each statement could raise: int(text) can raise ValueError; a / b can raise ZeroDivisionError; open(name) can raise FileNotFoundError; my_list[i] can raise IndexError; my_dict[key] can raise KeyError."),
        MISTAKE("A bare except that hides every error", "A clause such as except: (or except Exception: with pass) catches mistakes you did not expect, including typing errors in your own code, and hides them. Catch the specific exception you can handle, and let others stop the program so you can fix them."),
        MISTAKE("Putting too much code in try", "Keep the try block small, with only the statements that can raise the exception. If it is large, an exception from an unrelated line can be handled by the wrong clause."),
        QUIZ("A function contains try: return 10 // n, except ZeroDivisionError: return None, finally: print(\"done\"). What is printed by print(f(0))?",
             ["None", "done then None", "done", "An error message"], 1,
             "10 // 0 raises ZeroDivisionError. The except clause returns None, but finally runs before the function leaves, so done is printed first. Then the caller prints None.",
             hint="finally always runs, even when a return statement is waiting.",
             feedback=["This leaves out the word done: finally prints it before the function returns.", "", "The function returns None, which print then shows.", "The exception is caught by the except clause, so no error message appears."]),
        QUIZ("Which exception does the statement int(\"12x\") raise?",
             ["TypeError", "ZeroDivisionError", "ValueError", "KeyError"], 2,
             "The argument is a string of the right type, but its value cannot be converted: this is a ValueError.",
             hint="The type is right (a string). Is the value suitable?",
             feedback=["A TypeError would arise for a wrong type, such as \"a\" + 1.", "There is no division here.", "", "KeyError belongs to dictionaries."]),
        H("Practice questions"),
        PQ("Write a function safe_divide(a, b) that returns a / b but returns None and prints a message if b is zero. Give the output of safe_divide(10, 4) and safe_divide(5, 0).",
           "The function: try to return a / b; except ZeroDivisionError: print(\"cannot divide by zero\") and return None. safe_divide(10, 4) returns 2.5. safe_divide(5, 0) prints cannot divide by zero and returns None."),
        PQ("Explain the difference between else and finally in a try statement.",
           "else runs only when the try block finished without raising an exception. finally runs in every case, whether an exception occurred or not, and even if the try block contains a return. finally is used for tidy-up such as closing a file."),
        PQ("Define a custom exception InvalidMarkError that stores the invalid mark, and show how a function add_mark raises it and how the caller catches it.",
           "class InvalidMarkError(Exception) with __init__(self, mark): super().__init__(f\"invalid mark {mark}\"); self.mark = mark. In add_mark(mark): if not 0 <= mark <= 100: raise InvalidMarkError(mark). The caller writes try: add_mark(120) and except InvalidMarkError as e: print(\"Refused:\", e.mark), which prints Refused: 120."),
        PQ("A program has except Exception: first and except FileNotFoundError: second. Explain what is wrong and how to correct it.",
           "FileNotFoundError is a kind of Exception, so the first clause catches it and the second clause can never run. The more specific clause must come first, and the general Exception clause last (or not at all)."),
        SUM("An exception is a run-time error; unhandled, it stops the program. Handle it with try and except.",
            "else runs when no exception occurred; finally always runs, even when there is a return.",
            "raise signals a problem; a custom exception is a class that inherits from Exception.",
            "Put specific except clauses before general ones, and catch only what you can handle.",
            "Use with to open files so they are always closed."),
    ],
))

# ---------------------------------------------------------------------------
# Software project 1: analysis, planning and design
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Software Project",
    topic="Individual project",
    title="Project analysis, planning and design: from a real problem to a design document",
    slug="csd-proj-plan-design",
    minutes=25,
    summary="Turn a real user's problem into a project: find the user's needs, write SMART objectives and a time plan, and produce the design documents (data dictionary, tables, algorithms, screens), using a provision store's stock and sales system as the running example.",
    objectives=[
        "Choose a project with a real user and a problem that software can solve",
        "Write measurable (SMART) objectives and separate functional from non-functional requirements",
        "Make a realistic week-by-week plan with a risk list",
        "Produce a data dictionary, table design and algorithm in pseudocode for one feature"
    ],
    key_concepts=["Client", "Requirements", "SMART objectives", "Non-functional requirement", "Project plan", "Risk", "Data dictionary", "Pseudocode", "Prototype"],
    blocks=[
        H("Introduction"),
        T("The individual project asks you to build a working program for a real person and to write a technical report. Many students lose time because they start to code before they know what the program must do. This lesson covers the first two stages, analysis and design, using one running example: a provision store in Nkongsamba whose owner records stock and sales in an exercise book."),
        T("This is a general guide written by KKEVO. The marking scheme, the deadlines and the exact report requirements come from the GCE Board and your teacher, so check them first."),
        IMG("al-csd-project-stages.svg",
            "Flow diagram of six stages: 1 Analysis, 2 Design, 3 Coding, 4 Testing, 5 Evaluation, 6 Report. A dashed arrow from Testing goes back to Design to show that faults found in testing send you back.",
            caption="Figure 1. The stages of the project. This lesson covers stages 1 and 2."),
        H("Stage 1: analysis"),
        D("**Analysis** means finding out exactly what the user needs. You study the current way of working, talk to the user (the **client**), collect sample documents and write down what the new system must do (the **requirements**).",
          title="Analysis"),
        KEY("Ways to find out what the client needs", "Use at least two and keep your notes: they go in the report.", cards=[
            ["Interview", "Ask open questions: How do you record a sale? What takes most time? What goes wrong?"],
            ["Observe", "Watch the client work for an hour. People forget to mention things they do automatically."],
            ["Collect documents", "Copy a page of the exercise book, a receipt, an invoice. These show the data the system must store."],
            ["Questionnaire", "Useful when there are many users, such as 30 teachers."],
        ]),
        T("Suppose the owner of the store says: \"I never know what is out of stock until a customer asks. At the end of the day, adding up the sales takes me an hour and I sometimes make mistakes.\" From this you can state the problem: stock levels are not tracked and daily totals are calculated by hand."),
        D("**SMART objectives** are Specific, Measurable, Achievable, Relevant and Time-bound. Each objective states something that can be tested at the end.",
          title="SMART objectives"),
        EX("Worked example 1: improving vague objectives", intro="Rewrite these three vague statements as measurable objectives for the store project.", steps=[
            S("Vague: \"The system should be easy to use\"", text="Measurable: A new assistant can record a sale of three items after two minutes of training, without help. This can be tested by timing a real person."),
            S("Vague: \"The system should be fast\"", text="Measurable: Recording a sale of up to 10 items takes less than 20 seconds on the store's own phone or laptop."),
            S("Vague: \"The system should track stock\"", text="Measurable: After each sale the stock of every item sold is reduced automatically, and the system lists every item with stock 0 on one screen."),
            S("Why measurable matters", text="At the end of the project you will test each objective and write in the evaluation whether it was met. A vague objective cannot be tested."),
        ]),
        KEY("Requirements", "Write them in two groups.", cards=[
            ["Functional", "What the system must do: record a sale, update stock, print the daily total, list items with no stock."],
            ["Non-functional", "How well it must do it: work with no internet, run on the client's old laptop, store prices in whole FCFA, respond in under a second."],
            ["Constraints", "Limits you must accept: a school-term deadline, no money for paid software, the client's computer skills."],
        ]),
        H("Planning"),
        T("A plan breaks the project into tasks with a time for each. A project in a school term is often 10 to 12 weeks. Leave the last weeks for testing, the evaluation and the report. A common mistake is to plan eight weeks of coding and leave two days for the report."),
        CODE('''
Week  Task                                              Output
1     Interview, observe, collect documents             Notes, sample pages
2     Write objectives and requirements; agree them     Requirements list signed by the client
3     Design: data, screens, algorithms, test plan      Design document
4-6   Code the database and the main features           Working core (test each part as you finish it)
7     Code reports and error handling                   Complete first version
8-9   Test with planned data; show the client; fix      Test table, list of fixes
10    Evaluate against the objectives; client feedback  Evaluation notes
11-12 Write and check the technical report              Final report
''', "text", title="Table 1: a 12-week plan (an example, adjust it to your own dates)"),
        T("A good plan also lists **risks**: things that could delay the project, with a way to reduce each. For example: the client is not available in week 8 (agree dates in week 2); the laptop fails (back up the project every day to a memory stick and a second place); a feature is harder than expected (build the core first and treat extras as optional)."),
        H("Stage 2: design"),
        D("**Design** describes how the system will meet the requirements before you write code. Typical design documents are the data dictionary and table design, class or structure diagrams, algorithms in pseudocode, screen layouts and a test plan.",
          title="Design"),
        EX("Worked example 2: a data dictionary", intro="Design the tables for the store: products, sales and the lines of each sale. Give the data dictionary for Product and a check that the design works.", steps=[
            S("Find the entities", text="Product (what is sold), Sale (one customer visit) and SaleLine (one product in a sale, with a quantity). A sale has many lines, so SaleLine links Sale and Product."),
            S("Write the data dictionary for Product", text="Each field with its type and validation rule (see Table 2)."),
            S("Write the tables in SQL", text="Product, Sale and SaleLine with primary and foreign keys and CHECK constraints (Listing 1)."),
            S("Test the design with sample data", text="Insert three products and four sale lines and run the takings query. The run gave 5500 FCFA for 2 March and 3000 FCFA for 3 March, which agrees with working it out by hand: 2×1500 + 1000 + 1500 and 3×1000."),
        ]),
        CODE('''
Field      Type     Validation                               Example
ProductID  INTEGER  Primary key, unique                      101
Name       TEXT     Not empty, at most 30 characters         Rice 1 kg
Price      INTEGER  Greater than 0 (whole FCFA)              1500
Stock      INTEGER  0 or more                                40
''', "text", title="Table 2: data dictionary for the Product table"),
        CODE('''
CREATE TABLE Product (ProductID INTEGER PRIMARY KEY, Name TEXT NOT NULL,
  Price INTEGER NOT NULL CHECK (Price > 0), Stock INTEGER NOT NULL CHECK (Stock >= 0));
CREATE TABLE Sale (SaleID INTEGER PRIMARY KEY, SaleDate TEXT NOT NULL);
CREATE TABLE SaleLine (SaleID INTEGER NOT NULL, ProductID INTEGER NOT NULL,
  Qty INTEGER NOT NULL CHECK (Qty > 0), PRIMARY KEY (SaleID, ProductID),
  FOREIGN KEY (SaleID) REFERENCES Sale(SaleID),
  FOREIGN KEY (ProductID) REFERENCES Product(ProductID));

SELECT S.SaleDate, SUM(L.Qty * P.Price) AS Takings
FROM Sale S JOIN SaleLine L ON S.SaleID = L.SaleID
JOIN Product P ON L.ProductID = P.ProductID
GROUP BY S.SaleDate ORDER BY S.SaleDate;

SaleDate    Takings
----------  -------
2026-03-02  5500
2026-03-03  3000
(2 rows)
''', "sql", title="Listing 1: the table design and the daily takings query (run in sqlite3)"),
        EX("Worked example 3: designing an algorithm before coding", intro="Design the algorithm that works out the amount due for a sale from a list of line prices and a discount percentage. The store allows a discount from 0 to 50 percent.", steps=[
            S("Inputs and outputs", text="Input: the list of line amounts (price × quantity) and the discount percentage. Output: the amount to pay in whole FCFA."),
            S("Pseudocode", text="IF discount < 0 OR discount > 50 THEN report an error. IF any line is negative THEN report an error. total ← sum of the lines. due ← total − (total × discount DIV 100). Return due."),
            S("Trace with lines 1500 and 2500, discount 10", text="total = 4000. total × 10 DIV 100 = 400. due = 4000 − 400 = 3600."),
            S("Why DIV", text="Whole FCFA only: integer division drops any fraction of a franc. The client agreed this rule in the requirements."),
            S("Plan the tests now", text="The boundary values 0 and 50 and the invalid values 51 and −1 will go in the test plan, to be run in the next lesson."),
        ]),
        TIP("Show the client a paper sketch or a simple prototype of the screens before you code. A change on paper takes a minute; a change in finished code can take a day."),
        MISTAKE("Starting to code before the objectives are agreed", "If the client has not agreed the requirements, you may build the wrong thing, and your evaluation will have nothing to measure against. Get a short written agreement (even a signed page) in week 2."),
        MISTAKE("Choosing a project that is too large", "A system for a whole hospital cannot be finished by one student in a term. Choose one clear problem for one client, and list the extras as future improvements in the report."),
        QUIZ("Which of these is a measurable (SMART) objective?",
             ["The program should be user-friendly", "The program should be quick", "A trained assistant records a sale of 10 items in under 20 seconds", "The program should have many features"], 2,
             "It states a task, a quantity and a time limit, so it can be tested with a stopwatch. The others cannot be tested.",
             hint="Which one has a number you can check at the end?",
             feedback=["User-friendly cannot be measured unless it is turned into something testable.", "Quick has no limit to test against.", "", "Many has no number."]),
        QUIZ("Which requirement is non-functional?",
             ["The system records each sale", "The system lists items whose stock is 0", "The system works without an internet connection", "The system prints the daily total"], 2,
             "A non-functional requirement describes a quality or condition of the system, such as working offline. The others describe things the system does.",
             hint="Which one is about how or where the system works rather than a task?",
             feedback=["This is a task, so it is functional.", "This is a task, so it is functional.", "", "This is a task, so it is functional."]),
        H("Practice questions"),
        PQ("Describe two methods of finding out the client's needs and one thing that each shows that the other might miss.",
           "An interview lets you ask questions and learn the client's priorities and problems in their own words. Observation shows the steps the client actually takes, including habits they forget to mention, such as writing a stock count on the back of an envelope. Documents (receipts, order pages) show exactly what data must be stored and in what form."),
        PQ("A school wants a program to record the library loans. Write three measurable objectives.",
           "For example: (1) A librarian can record a loan in under 15 seconds. (2) The program shows the list of books that are overdue for more than 14 days on one screen. (3) No book can be lent to two members at the same time: the program refuses the second loan with a message. Each has a number or a clear yes or no test."),
        PQ("Explain why the plan for a 12-week project should leave time for testing and the report, and name two risks with a way to reduce each.",
           "Testing finds faults that need time to fix and retest, and the report must describe all stages, so both need time and are often squeezed at the end. Risks: loss of work when the computer fails (back up every day to two places); the client being unavailable (fix meeting dates early); a feature being too hard (build the core first and treat extras as optional)."),
        PQ("Design the algorithm in pseudocode for the amount due when a loan is overdue: 100 FCFA for each full week late, with a maximum charge of 1000 FCFA. Trace it for 25 days late.",
           "INPUT days_late. weeks ← days_late DIV 7. charge ← weeks × 100. IF charge > 1000 THEN charge ← 1000. OUTPUT charge. For 25 days: weeks = 25 DIV 7 = 3, charge = 300, which is not above 1000, so the output is 300 FCFA."),
        SUM("Analysis finds what the client needs by interviews, observation and documents; write what you find in your notes.",
            "SMART objectives are specific and measurable, so that the evaluation can show whether they were met.",
            "Separate functional requirements (what it does) from non-functional ones (how well, on what equipment).",
            "A plan lists tasks, weeks, outputs and risks, and keeps time for testing and the report.",
            "Design before coding: data dictionary, tables, algorithms in pseudocode, screens and a test plan."),
    ],
))

# ---------------------------------------------------------------------------
# Software project 2: testing, evaluation and the technical report
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Software Project",
    topic="Individual project",
    title="Testing, evaluation and the technical report",
    slug="csd-proj-testing-report",
    minutes=25,
    summary="Plan and run unit and integration tests with normal, boundary and erroneous data, evaluate the finished system against its objectives and organise the technical report so that every claim is backed by evidence.",
    objectives=[
        "Write a test plan with normal, boundary and erroneous test data and expected results",
        "Write and run unit and integration tests with Python's unittest module and read a failing test",
        "Evaluate a system against measurable objectives and client feedback",
        "Organise a technical report so that each section links to the project stages"
    ],
    key_concepts=["Unit test", "Integration test", "Acceptance test", "Normal data", "Boundary data", "Erroneous data", "Test plan", "Evaluation", "Technical report"],
    blocks=[
        H("Introduction"),
        T("The store in Nkongsamba is ready to use your program. Before it handles real sales, you must prove that it gives the right answers, including when a customer or an assistant does something unexpected. Testing is how you prove it, and the technical report is where you show the proof."),
        T("This is KKEVO's general guide. The exact report requirements and marking come from the GCE Board and your teacher."),
        H("Kinds of testing"),
        KEY("Three levels of testing", "Test small parts first, then the parts together, then the whole system with the client.", cards=[
            ["Unit test", "Tests one function or class method alone, for example the function that works out the amount due."],
            ["Integration test", "Tests that parts work together: the sale screen, the stock update and the receipt agree with each other."],
            ["Acceptance (user) test", "The client or a real user performs real tasks. It shows whether the objectives are met."],
        ]),
        D("Test data falls into three groups. **Normal data** is typical valid input. **Boundary data** is at the edge of what is allowed: the smallest and largest valid values, and the values just outside them. **Erroneous data** is invalid and must be rejected with a clear message.",
          title="Normal, boundary and erroneous data"),
        EX("Worked example 1: a test plan for a validation rule", intro="A mark must be a whole number from 0 to 100. Choose test data and give the expected result for each.", steps=[
            S("Normal", text="50 is accepted."),
            S("Boundary (edges and just outside)", text="0 accepted, 100 accepted, -1 rejected, 101 rejected. Faults often hide at the edges, for example < instead of <=."),
            S("Erroneous", text="abc and an empty entry are rejected with a message (they are not numbers). 72.5 is rejected if only whole numbers are allowed."),
            S("Always write the expected result before you run the test", text="If you decide after seeing the result, you may accept a wrong answer. Each row in the test table has: test number, what is tested, data, expected result, actual result and pass or fail."),
        ]),
        H("A unit test you can run"),
        T("Python's unittest module lets you write tests as code, run them all in one go and run them again after every change. Here is the function from the design lesson: it works out the amount due after a whole-number percentage discount, with the rule that the discount must be between 0 and 50 and no price may be negative."),
        CODE('''
import unittest

def total_due(prices, discount_percent=0):
    """Total in FCFA after a whole-number percentage discount."""
    if not 0 <= discount_percent <= 50:
        raise ValueError("discount must be 0 to 50")
    if any(p < 0 for p in prices):
        raise ValueError("price cannot be negative")
    total = sum(prices)
    return total - total * discount_percent // 100

def receipt_line(name, qty, price):
    return f"{name} x{qty} = {qty * price}"

class TestTotalDue(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(total_due([1500, 2500], 10), 3600)
    def test_no_discount(self):
        self.assertEqual(total_due([1500, 2500]), 4000)
    def test_boundary_discount_zero(self):
        self.assertEqual(total_due([1000], 0), 1000)
    def test_boundary_discount_fifty(self):
        self.assertEqual(total_due([1000], 50), 500)
    def test_discount_just_over(self):
        with self.assertRaises(ValueError):
            total_due([1000], 51)
    def test_negative_price(self):
        with self.assertRaises(ValueError):
            total_due([-5])
    def test_empty_basket(self):
        self.assertEqual(total_due([]), 0)

class TestIntegration(unittest.TestCase):
    def test_receipt_total_matches(self):
        items = [("Rice", 2, 1500), ("Oil", 1, 2500)]
        lines = [receipt_line(*i) for i in items]
        self.assertEqual(lines[0], "Rice x2 = 3000")
        self.assertEqual(total_due([q * p for _, q, p in items], 10), 4950)

if __name__ == "__main__":
    unittest.main(verbosity=2)

Result of running it (8 tests):
Ran 8 tests in 0.001s
OK
''', "python", title="Listing 1: unit tests and an integration test (run in Python 3.13)"),
        EX("Worked example 2: checking the expected values by hand", intro="Show that the expected values in the test code are right, before trusting the tests.", steps=[
            S("test_normal", text="Lines total 1500 + 2500 = 4000. A 10 percent discount is 4000 × 10 DIV 100 = 400. Amount due 4000 − 400 = 3600."),
            S("test_boundary_discount_fifty", text="1000 × 50 DIV 100 = 500, so the amount due is 1000 − 500 = 500."),
            S("The integration test", text="2 × 1500 = 3000 and 1 × 2500 = 2500 give 5500. A 10 percent discount is 550, so the amount due is 4950."),
            S("The error tests", text="51 is above the largest valid discount and −5 is a negative price, so both must raise ValueError."),
        ]),
        H("When a test fails"),
        T("To see what a failure looks like, the check was changed from 0 <= discount <= 50 to 0 <= discount < 50 (a boundary mistake) and the tests were run again. The boundary test failed, and the others still passed."),
        CODE('''
test_boundary_discount_fifty ... ERROR
...
ValueError: discount must be 0 to 50

Ran 8 tests in 0.002s
FAILED (errors=1)
''', "text", title="Listing 2: the boundary test catches the off-by-one fault"),
        T("Only the test with the value 50 noticed the change. Without boundary data the fault would have stayed hidden until a customer was refused a legal discount. After fixing the code you must run all the tests again, not just the one that failed, because a fix can break something else (this is called **regression testing**)."),
        TIP("In the report, keep the test table, a screenshot of the test run and a short note about each fault found and how it was fixed. Faults found and fixed show good testing; they are not something to hide."),
        H("Evaluation and the report"),
        D("**Evaluation** is your honest judgement of the finished system. For each objective, say whether it was met and prove it with evidence (a test result, a time, a client comment). Then give the client's feedback, the limits of the system and improvements you would make with more time.",
          title="Evaluation"),
        KEY("A structure for the technical report", "Follow the order of the project stages. Use headings, numbered figures and short paragraphs.", cards=[
            ["1. Analysis", "The client and problem, how you found out the needs, the current system, objectives and requirements."],
            ["2. Design", "Data dictionary, tables or classes, algorithms, screen designs, the test plan."],
            ["3. Implementation", "How the system was built: the key parts of the code, explained. Not just a list of code: say why."],
            ["4. Testing", "The test table with actual results, screenshots, faults found and fixed, client testing."],
            ["5. Evaluation", "Each objective with evidence, client feedback, limitations, improvements."],
            ["Appendices", "Full code, sample documents, interview notes, user guide."],
        ]),
        EX("Worked example 3: evaluating one objective", intro="Objective: A trained assistant can record a sale of 10 items in under 20 seconds. Write the evaluation paragraph.", steps=[
            S("State the objective and how it was tested", text="Two assistants, each trained for five minutes, recorded three sales of 10 items while the project author timed them."),
            S("Give the evidence", text="The times were 14, 17 and 19 seconds for the first assistant and 16, 21 and 18 seconds for the second (example figures for illustration)."),
            S("Judge honestly", text="Five of the six sales were under 20 seconds. The objective was mostly met. The one slow sale happened when the assistant searched for a product by scrolling."),
            S("Link to an improvement", text="Add a search box by product name in the next version, which could bring the slowest times below 20 seconds."),
        ]),
        MISTAKE("Testing only normal data", "A test plan with only typical values does not show the system can cope. Always include boundary and erroneous data, as the faulty boundary above shows."),
        MISTAKE("Writing a report that does not match the objectives", "If the evaluation talks about features that were never in the objectives, or ignores objectives that were not met, it is not convincing. Take the objectives from the analysis section and answer each one."),
        QUIZ("A discount must be from 0 to 50 percent. Which set contains only boundary test values?",
             ["25 and 30", "0, 50, -1 and 51", "abc and a blank entry", "10, 20 and 40"], 1,
             "Boundary data tests the edges of the valid range (0 and 50) and the values just outside it (-1 and 51).",
             hint="Boundary means at the edge of the allowed range.",
             feedback=["These are normal values in the middle of the range.", "", "These are erroneous data (not numbers).", "These are normal values in the middle of the range."]),
        QUIZ("Which kind of testing shows that the sale screen, the stock update and the receipt work correctly together?",
             ["Unit testing", "Integration testing", "Proofreading", "Syntax checking"], 1,
             "Integration testing checks that separate parts of the system work together. Unit tests check one part at a time.",
             hint="Together, not one part at a time.",
             feedback=["A unit test checks one function or method alone.", "", "Proofreading is for the report text, not for the program.", "Syntax checking only finds errors in the form of the code."]),
        H("Practice questions"),
        PQ("Distinguish between normal, boundary and erroneous test data, giving one example of each for a rule that says a quantity must be a whole number from 1 to 99.",
           "Normal data is typical valid input: 12. Boundary data is at the edges of the range: 1 and 99 (accepted), 0 and 100 (rejected). Erroneous data is invalid input that the program must reject with a message, such as the word ten, a blank entry or 3.5."),
        PQ("Explain the difference between unit testing and integration testing, with an example from a stock system.",
           "A unit test checks one function on its own, for example that a function that reduces stock after a sale never gives a negative result. An integration test checks that the parts work together, for example that after a sale is recorded on the sale screen, the stock screen shows the new stock and the daily total includes the sale."),
        PQ("A test table has a column for expected result and a column for actual result. Explain why the expected result must be written before the test is run.",
           "If the expected result is written first, it comes from the design and the requirements, not from what the program happens to do. If it were written after seeing the result, a wrong result could be accepted as correct, and faults would be hidden."),
        PQ("Write a short evaluation of the objective: After each sale the stock of every item sold is reduced automatically. Say what evidence you would give and how to be honest if one test failed.",
           "State that the objective was tested by recording 10 sales and comparing stock before and after. Give the evidence: a table or screenshots showing the stock reduced in nine sales. Say that in the tenth sale, an item sold twice on the same sale was reduced only once, describe the fault found, how it was fixed and that all the sales were then retested and passed. Say how the objective is now met and what further tests would be done."),
        SUM("Test in three levels: unit tests for one part, integration tests for parts together and acceptance tests with the client.",
            "Use normal, boundary and erroneous data, and write the expected result before the test is run.",
            "Boundary tests find off-by-one faults; run all tests again after every fix (regression testing).",
            "Evaluate every objective with evidence, include the client's feedback and name limitations and improvements.",
            "Organise the technical report by stages: analysis, design, implementation, testing, evaluation, with appendices."),
    ],
))

# ---------------------------------------------------------------------------
# Examination: how to approach the practice paper
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Examination",
    topic="Practice paper",
    title="Approaching the Upper Sixth Computer Science practice paper",
    slug="csd-exam-practice-paper",
    minutes=22,
    summary="Plan your 90 minutes for the KKEVO Upper Sixth practice paper, revise by topic, use a two-pass method and practise the quick checks that save time on tracing, SQL and complexity questions.",
    objectives=[
        "Plan the time for a 40-question multiple-choice practice paper",
        "Map each Upper Sixth topic to the kinds of question it produces",
        "Use the two-pass method and eliminate wrong options",
        "Do quick checks on code tracing, SQL row counts and growth rates"
    ],
    key_concepts=["Time planning", "Two-pass method", "Elimination", "Tracing", "Topic revision", "Review"],
    blocks=[
        H("Introduction"),
        T("The KKEVO Upper Sixth practice paper has 40 four-option multiple-choice questions on all the topics of the year: data structures, searching and sorting, complexity, relational algebra, normalization, SQL, object-oriented programming, classes in practice and the software project. It is practice material written by KKEVO, not a copy of any Board paper."),
        D("The real paper format, the number of papers and the time allowed are set by the GCE Board. Check them with your teacher. The 40 questions and 90 minutes of this practice paper are KKEVO practice settings, not official figures.",
          title="Check the real format"),
        H("Revise by topic"),
        T("The practice paper covers the whole year, so find out which topics are weakest before you sit it. After you finish, the results page shows your score for each topic and links back to the lessons."),
        KEY("What to expect from each topic", "The kinds of question to practise. Each topic has its own lessons and practice sets.", cards=[
            ["Abstract data types", "Trace push, pop, enqueue and dequeue; build a binary search tree and give a traversal; pointer order when inserting into a linked list."],
            ["Searching and sorting", "Count comparisons in binary search; show the list after a pass of bubble, insertion or selection sort; merge two sorted lists."],
            ["Complexity", "Match code to O(1), O(log n), O(n), O(n squared); say what happens to the time when n doubles."],
            ["Relational algebra", "Evaluate select, project, join and set operations on small relations; degree and cardinality of a product."],
            ["Normalization", "Find keys by closure; spot partial and transitive dependencies; decide 2NF, 3NF or BCNF; name anomalies."],
            ["SQL", "Predict query output and row counts; joins and LEFT JOIN; GROUP BY and HAVING; subqueries; constraints."],
            ["OOP principles", "Define and recognise abstraction, encapsulation, inheritance and polymorphism; predict program output."],
            ["Classes in practice", "UML symbols; constructors and class attributes; the order of output with try, except and finally."],
            ["Individual project", "Normal, boundary and erroneous test data; measurable objectives; the stages and the report."],
        ]),
        H("Planning the time"),
        T("A good plan has two passes. In the first pass you answer every question you can do quickly and mark the rest. In the second pass you return to the marked questions with the time you saved. Finally you use any spare minutes to check."),
        EX("Worked example 1: a time plan for 40 questions in 90 minutes (KKEVO advice)", intro="Make a time plan and say what to do with a long tracing question.", steps=[
            S("Average time per question", text="90 ÷ 40 = 2.25 minutes."),
            S("First pass", text="Aim for 1.5 minutes per question: 40 × 1.5 = 60 minutes. Answer what you can and mark the rest with a question mark on your paper."),
            S("Second pass", text="90 − 60 = 30 minutes for the marked questions. That is about 3 minutes each if you marked 10 questions."),
            S("A long tracing question", text="If after about a minute you are still not sure, mark it and move on. A tracing question is a good one to skip and return to, because it takes the longest and counts the same as a one-line definition."),
            S("Never leave blanks", text="Make your best guess before time ends. In this practice paper a wrong answer costs nothing, but check the real rules with your teacher."),
        ]),
        H("Quick checks that save time"),
        T("Many questions look long but have a fast check. Learn these."),
        EX("Worked example 2: counting printed lines from nested loops", intro="How many times is print executed by: for i in range(4): for j in range(i): print(\"#\")?", steps=[
            S("Count the inner loop for each i", text="i = 0 gives 0 prints, i = 1 gives 1, i = 2 gives 2, i = 3 gives 3."),
            S("Add", text="0 + 1 + 2 + 3 = 6. Run in Python, the program printed 6 lines."),
            S("Link to complexity", text="The count is n(n−1)/2 for n = 4, which is of order n squared."),
        ]),
        EX("Worked example 3: row counts and growth", intro="Two quick questions. (a) How many rows does a query that lists the tables Member and Book in FROM, with no join condition, return if Member has 5 rows and Book has 6? (b) An algorithm takes 3 seconds for n = 1000 and grows as n squared. How long does it take for n = 2000?", steps=[
            S("(a) No join condition", text="That is a Cartesian product: 5 × 6 = 30 rows (checked in sqlite3)."),
            S("(b) Doubling n", text="For n squared growth, doubling n multiplies the time by 2² = 4. So the time is 3 × 4 = 12 seconds."),
            S("The habit", text="Look for the shortcut: a product means multiply, doubling and n squared means multiply by 4."),
        ]),
        KEY("Using elimination", "Even when you cannot work out the answer, you can often remove two options.", cards=[
            ["Check the type of answer", "If the question asks for a number of rows, remove options that are lists of words."],
            ["Check the limits", "A binary search of 15 items cannot need 15 comparisons. Remove impossible values."],
            ["Watch for absolute words", "Always, never and only often make an option false."],
            ["Read NOT and EXCEPT questions twice", "Underline the word NOT. Test each option against the question."],
        ]),
        MISTAKE("Spending too long on one question", "Two extra minutes spent on one question is the time of one or two easy questions you will never reach. Mark it and move on."),
        MISTAKE("Changing answers without a reason", "In the review, change an answer only if you can say what you misread or what mistake you found. A change based only on nerves often turns a right answer into a wrong one."),
        TIP("Use the practice set for this lesson to rehearse the time plan and the quick checks, and then sit the mock paper in one go, timed, with no notes, before you look at the explanations."),
        QUIZ("A 40-question paper lasts 90 minutes. You spend 1.5 minutes on each question in the first pass. How much time is left for the second pass?",
             ["20 minutes", "30 minutes", "45 minutes", "60 minutes"], 1,
             "The first pass takes 40 × 1.5 = 60 minutes. 90 − 60 = 30 minutes remain.",
             hint="Find the first pass time and take it from 90.",
             feedback=["That would be the case if the first pass took 70 minutes.", "", "That would require a first pass of 45 minutes.", "60 minutes is the length of the first pass, not what is left."]),
        QUIZ("You are 90 seconds into a long code-tracing question and still not sure. What should you do?",
             ["Keep going until you finish it", "Mark it, give a quick best guess if you like, and move on", "Leave the paper blank from there", "Start again from question 1"], 1,
             "A marked question can be solved later with the time saved. Moving on protects the easy marks.",
             hint="Which choice protects the questions you can do quickly?",
             feedback=["This risks leaving easy questions unanswered at the end.", "", "A blank can never earn a mark.", "Going back to the start wastes the time already spent."]),
        H("Practice questions"),
        PQ("A 40-question paper lasts 90 minutes. Describe a two-pass plan with times, and say when to use the second pass.",
           "Spend about 60 minutes (1.5 minutes each) on a first pass: answer the questions you can do quickly and mark the others. Use the remaining 30 minutes for a second pass on the marked questions, spending longer on tracing or calculations. Keep a few minutes at the end to check that every question has an answer."),
        PQ("An O(n squared) algorithm takes 5 seconds for n = 500. Estimate its time for n = 1500 and show your reasoning.",
           "Tripling n multiplies the time by 3 squared = 9. So the time is 5 × 9 = 45 seconds."),
        PQ("List the steps you would take to answer a question that asks which statement about a stack is NOT true.",
           "Underline the word NOT. Test each option in turn against what you know about a stack (LIFO, push, pop, peek). Three options will be true. The one that is false is the answer. Check again that you chose the false one, not a true one."),
        PQ("Explain why you should not change an answer in the review unless you can say why it was wrong.",
           "If you cannot explain what you misread or mistook, the change is a guess, and it can turn a correct answer into a wrong one. A change should follow a specific finding, such as noticing that you read the question the wrong way or made an arithmetic mistake."),
        SUM("The real paper format is set by the GCE Board: check it with your teacher. The 40 questions and 90 minutes here are KKEVO practice settings.",
            "Plan two passes: about 60 minutes for the first, 30 for the marked questions, and answer every question.",
            "Revise by topic and use the practice paper's topic scores to decide where to work.",
            "Use quick checks: nested loop counts, row counts of products, growth by doubling.",
            "Eliminate impossible options, read NOT questions twice and change an answer only for a reason."),
    ],
))
