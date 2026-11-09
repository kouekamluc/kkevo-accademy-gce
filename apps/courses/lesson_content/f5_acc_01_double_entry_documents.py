"""Form 5 Principles of Accounts (O Level 0505), modules "OHADA Conceptual Framework & Double Entry" and
"Commercial Documents & Books of Original Entry". All FCFA figures are invented for practice.
Draft content: check against the official syllabus and your textbook."""

from .dsl import *  # noqa: F403

COURSE = ("principles-of-accounts", "form-5")

M1 = "OHADA Conceptual Framework & Double Entry"
M2 = "Commercial Documents & Books of Original Entry"

VAT_RATE = 1925  # 19.25 % written as 1925 / 10000 (check the current rate)


def n(x):
    """1234567 -> '1 234 567'"""
    return f"{x:,}".replace(",", " ")


def vat(net):
    v, r = divmod(net * VAT_RATE, 10000)
    assert r == 0, net
    return v


def tacc(title, dr, cr, w=14, a=10):
    """Aligned T-account text. dr and cr are lists of (label, amount). Adds balance c/d, totals and balance b/d."""
    dr = list(dr)
    cr = list(cr)
    td = sum(x for _, x in dr)
    tc = sum(x for _, x in cr)
    bal = td - tc
    if bal > 0:
        cr.append(("Balance c/d", bal))
        tot = td
    elif bal < 0:
        dr.append(("Balance c/d", -bal))
        tot = tc
    else:
        tot = td
    blank = " " * (w + 1 + a)

    def cell(rows, i):
        if i < len(rows):
            return f"{rows[i][0]:<{w}} {n(rows[i][1]):>{a}}"
        return blank

    out = [title, f"{'Dr':<{w + 1 + a}} | Cr"]
    for i in range(max(len(dr), len(cr))):
        out.append(f"{cell(dr, i)} | {cell(cr, i)}".rstrip())
    line = f"{'Total':<{w}} {n(tot):>{a}}"
    out.append(f"{line} | {line}")
    if bal > 0:
        out.append(f"{'Balance b/d':<{w}} {n(bal):>{a}} |")
    elif bal < 0:
        out.append(f"{blank} | {'Balance b/d':<{w}} {n(-bal):>{a}}")
    return "\n".join(out)


def tb(rows, w=22, a=11):
    """Trial balance text. rows are (account, 'D' or 'C', amount). Checks nothing: the caller asserts."""
    out = [f"{'Account':<{w}} {'Debit':>{a}} {'Credit':>{a}}"]
    td = tc = 0
    for name, side, amt in rows:
        if side == "D":
            td += amt
            out.append(f"{name:<{w}} {n(amt):>{a}} {'':>{a}}")
        else:
            tc += amt
            out.append(f"{name:<{w}} {'':>{a}} {n(amt):>{a}}")
    out.append("-" * (w + 2 * a + 2))
    out.append(f"{'Totals':<{w}} {n(td):>{a}} {n(tc):>{a}}")
    return "\n".join(out)


LESSONS = []

# ------------------------------------------------------------------ 1. concepts
_stock = [("Rice (50 bags)", 120000, 150000), ("Cooking oil (30 cans)", 200000, 150000), ("Soap (20 boxes)", 80000, 90000)]
_stock_val = [min(c, r) for _, c, r in _stock]
assert _stock_val == [120000, 150000, 80000] and sum(_stock_val) == 350000
_stock_cost = sum(c for _, c, _ in _stock)
assert _stock_cost == 400000
_stock_tbl = f"{'Item':<22}{'Cost':>9}{'Net sale':>10}{'Value in':>10}\n{'':<22}{'value':>9}{'value':>10}{'accounts':>10}\n" + "\n".join(
    f"{nm:<22}{n(c):>9}{n(r):>10}{n(min(c, r)):>10}" for nm, c, r in _stock) + f"\n{'Total':<22}{n(_stock_cost):>9}{n(sum(r for *_, r in _stock)):>10}{n(sum(_stock_val)):>10}"

LESSONS.append(lesson(
    module=M1,
    topic="Accounting concepts and conventions",
    title="Accounting concepts and conventions",
    slug="acc1-concepts-and-conventions",
    minutes=20,
    summary="Accounting concepts are the basic rules every accountant follows so that accounts are fair and comparable: business entity, money measurement, historical cost, going concern, accruals, prudence, consistency, materiality and duality.",
    objectives=[
        "Define accounting and say why businesses keep accounts",
        "State and explain the main accounting concepts and conventions",
        "Apply a concept to a short situation, for example the business entity and prudence concepts",
        "Name the OHADA wording of the main principles and note where IAS/IFRS wording differs",
    ],
    key_concepts=["Accounting", "Business entity", "Money measurement", "Historical cost", "Going concern", "Accruals", "Prudence", "Consistency", "Materiality", "Duality"],
    blocks=[
        H("Introduction"),
        T("Madame Ngo sells foodstuffs at the market in Bafoussam. She puts the day's money in the same pocket as her taxi fare and her children's school fees. At the end of the month she cannot say whether the shop made a profit. "
          "She needs records, and she needs everybody who reads them to follow the same rules."),
        D("**Accounting** is the process of identifying, recording, classifying, summarising and interpreting the financial transactions of a business so that owners, banks, tax officers and others can make decisions.",
          title="Definition: accounting"),
        T("The rules that make accounts fair and comparable are called **concepts** (basic ideas) and **conventions** (accepted habits). Under the OHADA system, which Cameroon uses together with other member states, many of them are written as 'principles' in the accounting law (the Uniform Act on accounting). In this lesson you learn the ones examiners ask about most. Check your textbook for the exact list your teacher uses."),
        H("The main concepts"),
        KEY("Concepts about what we record", "Four ideas decide what goes into the books and at what value.", cards=[
            ["Business entity", "The business is separate from its owner. Money or goods the owner takes for private use are recorded as **drawings**, not as business expenses."],
            ["Money measurement", "Only facts that can be measured in money (here FCFA) are recorded. The skill of a manager or a good location is not recorded."],
            ["Historical cost", "Assets are recorded at what they cost when bought, not at today's guessed market value."],
            ["Going concern (continuity)", "We assume the business will keep operating for the foreseeable future, so assets are not valued as if they were being sold off tomorrow."],
        ]),
        KEY("Concepts about when and how we record", "Five more ideas guide the timing and the care taken.", cards=[
            ["Accruals (independence of financial years)", "Income and expenses belong to the period in which they are earned or used, not the period in which the cash moves."],
            ["Prudence", "Do not overstate profit or assets. Record likely losses early; record gains only when they are certain."],
            ["Consistency (permanence of methods)", "Use the same method year after year, so that years can be compared. Change only for a good reason and say so."],
            ["Materiality", "Very small items need not be treated in full detail. A box of pens may be written off as an expense even though it lasts more than a year."],
            ["Duality (dual aspect)", "Every transaction has two effects, so every entry has a debit and an equal credit. This is the basis of double entry."],
        ]),
        TIP("OHADA and IAS/IFRS wording. The OHADA system speaks of prudence, continuity of operation, permanence of methods, historical cost, independence of financial years and the 'true image' (image fidele) of the accounts. The IAS/IFRS approach, taught in Section B of Paper 2, uses 'going concern', 'accruals basis' and 'true and fair view'. The ideas are the same; learn both sets of words."),
        H("Worked examples"),
        EX("Worked example 1: business entity", intro="Mr Tabi owns a shop in Limbe. In March he takes goods that cost FCFA 40 000 from the shop for his family. Which concept applies and how is it treated?", steps=[
            S("Identify the concept", text="The business and the owner are separate people in accounting: the **business entity** concept."),
            S("Decide the nature of the transaction", text="The goods left the business but were not sold to a customer. This is the owner taking value out of the business."),
            S("Record it", text="It is **drawings** of FCFA 40 000, valued at cost. It is not an expense of the shop and it is not a sale. It reduces the owner's capital."),
        ]),
        EX("Worked example 2: prudence and the value of stock", intro="At the year end a shop holds three lines of goods. Prudence says stock is valued at the **lower of cost and net realisable value** (the price it can really be sold for, less selling costs). Values are in FCFA, invented for practice.", steps=[
            S("List cost and net sale value of each line", text="See the table below."),
            S("Choose the lower figure for each line", text="Rice: 120 000 is lower than 150 000, so 120 000. Cooking oil: 150 000 is lower than 200 000, so 150 000 (a loss is recorded now). Soap: 80 000."),
            S("Add the values chosen", math=r"120\,000 + 150\,000 + 80\,000 = 350\,000", text="The stock appears at FCFA 350 000, not at its cost of FCFA 400 000."),
        ]),
        CODE(_stock_tbl, "text", title="Stock valuation (FCFA, invented for practice)"),
        EX("Worked example 3: accruals", intro="In December a trader in Douala delivers goods worth FCFA 300 000 to a customer, who promises to pay in January. In which year is the sale recorded?", steps=[
            S("Apply the accruals concept", text="The sale is earned when the goods are delivered, not when the cash arrives."),
            S("Decide the year", text="The sale belongs to **December**, the year of delivery. The customer is shown as a debtor at the year end."),
        ]),
        MISTAKE("Valuing assets at what they might sell for", "Beginners write that a building bought for FCFA 30 000 000 should be shown at today's price. Under historical cost the asset stays at cost (less depreciation, which you meet later). The one exception in our work is stock, valued at the lower of cost and net realisable value because of prudence."),
        MISTAKE("Confusing prudence with pessimism", "Prudence does not mean inventing losses. It means not recording profit before it is certain and recording a probable loss as soon as you know about it."),
        MISTAKE("Mixing private and business money", "If the owner pays a private electricity bill from the business bank account, it is drawings. Putting it in the expenses reduces profit wrongly and breaks the business entity concept."),
        QUIZ("A trader takes a FCFA 15 000 radio from her shop stock for her bedroom. Which concept tells us to treat this as drawings?",
             ["Going concern", "Business entity", "Materiality", "Consistency"], 1,
             "The business entity concept separates the owner from the business, so anything the owner takes out is drawings.",
             hint="Which concept says the owner and the business are two different people?",
             feedback=["Going concern is about the business continuing, not about who owns what.", "", "Materiality is about small items being treated simply.", "Consistency is about using the same method each year."]),
        QUIZ("Why is a factory machine bought for FCFA 5 000 000 still recorded at its cost even if a dealer now says it is worth FCFA 6 000 000?",
             ["Because of prudence only", "Because of historical cost", "Because of duality", "Because of money measurement"], 1,
             "Assets are recorded at cost. Opinions on current value are not used in the books.",
             hint="Think about which concept uses the price actually paid.",
             feedback=["Prudence matters for losses; historical cost is the direct reason here.", "", "Duality is about the two effects of each transaction.", "Money measurement says what is recorded, not at what value."]),
        PQ("State any four accounting concepts and give one sentence on each.",
           "Any four of: business entity (business separate from owner); money measurement (only facts measurable in money are recorded); historical cost (assets at purchase cost); going concern (business will continue); accruals (income and expenses go to the period they belong to); prudence (do not overstate profit or assets); consistency (same methods each year); materiality (small items need not be treated in detail); duality (every transaction has a debit and a credit)."),
        PQ("Mr Ayuk's shop bought 10 sacks of beans for FCFA 20 000 each. At the year end the sacks can only be sold for FCFA 16 000 each. At what value should the stock appear, and which concept is used?",
           "Cost 10 x 20 000 = 200 000; net realisable value 10 x 16 000 = 160 000. Stock is valued at the lower figure, **FCFA 160 000**, because of the **prudence** concept."),
        PQ("A bookkeeper changes the method of valuing stock every year to make the profit look better. Which concept does this break, and why does it matter?",
           "It breaks **consistency (permanence of methods)**. Accounts of different years can no longer be compared, and profit may be manipulated."),
        TIP("In Paper 1 multiple choice, concept questions give a short situation and ask which concept applies. Read the situation for the key idea: owner taking goods (entity), 'can be sold for less' (prudence), 'same method as last year' (consistency), 'cost price' (historical cost). Paper 2 Question 1 in the Board's 2023 session asked candidates to explain accounting terms, and many avoided it, so learn each definition in one clear sentence."),
        SUM("Accounting records, classifies and summarises financial transactions so people can decide.",
            "Business entity: owner and business are separate; owner's withdrawals are drawings.",
            "Historical cost, money measurement and going concern decide what is recorded and at what value.",
            "Accruals, prudence, consistency and materiality guide timing and care; duality gives every entry a debit and a credit.",
            "Stock is valued at the lower of cost and net realisable value."),
    ],
))

# ------------------------------------------------------------------ 2. chart of accounts
LESSONS.append(lesson(
    module=M1,
    topic="The SYSCOHADA chart of accounts",
    title="The SYSCOHADA chart of accounts: classes 1 to 8",
    slug="acc1-syscohada-chart-of-accounts",
    minutes=20,
    summary="SYSCOHADA gives every account a number. The first digit shows the class (1 to 8), so you can tell at once whether an account is a resource, an asset, a stock, a third party, cash, an expense or an income.",
    objectives=[
        "Explain what a chart of accounts is and why OHADA countries use one",
        "Name the eight classes of the SYSCOHADA plan and what each contains",
        "Give the class of a common account from its name or number",
        "State the normal balance (debit or credit) of accounts in each class",
    ],
    key_concepts=["Chart of accounts", "SYSCOHADA", "Class of accounts", "Account number", "Normal balance"],
    blocks=[
        H("Introduction"),
        T("A school keeps its registers in order: each class has a number, and each student has a number inside it. A chart of accounts does the same for money. Instead of every shop inventing its own names, businesses in all OHADA countries use one numbered list, so an accountant in Douala, Dakar or Libreville reads the same accounts the same way."),
        D("A **chart of accounts** is the numbered list of all the accounts a business may use. **SYSCOHADA** is the accounting system of the OHADA (Organisation for the Harmonisation of Business Law in Africa) member states, and its chart groups accounts into **classes**; our course uses classes 1 to 8.",
          title="Definition: SYSCOHADA chart"),
        T("The first digit of an account number is its class. The second digit gives the main group, and further digits give detail. For example 41 is the group of customers (class 4) and 411 is the ordinary customer account."),
        H("The eight classes"),
        CODE("""Class  Name                             Examples
1      Long-term resources              101 Share capital, 162 Loans
2      Fixed assets                     23 Buildings, 24 Equipment
3      Stocks                           31 Goods for resale
4      Third parties                    401 Suppliers, 411 Customers
5      Cash and bank                    521 Bank, 571 Cash in hand
6      Expenses (ordinary activities)   601 Purchases, 661 Wages
7      Income (ordinary activities)     701 Sales of goods
8      Other expenses and income        Non-ordinary items (HAO)""", "text", title="SYSCOHADA classes (check numbers against your textbook)"),
        T("Classes 1 to 5 are **balance sheet accounts**: they describe what the business owns and owes. Classes 6 and 7 are the accounts of the year's expenses and income, used to find the profit. Class 8 holds exceptional items outside the ordinary activity, such as the sale of a fixed asset. Class 9 (analytical accounting) is not needed at this level."),
        KEY("What is in each balance sheet class", "Remember the order: resources, then what they buy, then day-to-day dealings.", cards=[
            ["Class 1", "Capital, reserves, profit or loss brought forward, and long-term loans from banks (resources that stay a long time)."],
            ["Class 2", "Fixed assets: land, buildings, machines, vehicles, furniture, computers. Used for several years."],
            ["Class 3", "Stocks of goods, raw materials and supplies waiting to be sold or used."],
            ["Class 4", "Third parties: suppliers (we owe), customers (they owe us), staff, state (taxes, VAT), social bodies such as CNPS."],
            ["Class 5", "Bank balances, cash in hand and other money that can be spent at once."],
        ]),
        H("Normal balances"),
        T("Each account normally has a balance on one side, depending on what it is. Learn the pattern and you can check a trial balance quickly."),
        CODE("""Class  Normal balance  Reason
1      Credit          Owner and lenders provide the resources
2      Debit           Assets
3      Debit           Assets
4      Either          Customers: debit. Suppliers: credit.
5      Debit           Assets (a bank overdraft is credit)
6      Debit           Expenses
7      Credit          Income""", "text", title="Normal balance by class"),
        TIP("Some accounts have names that mislead. 'Purchases' (class 6) is an expense account, even though it records goods bought, so it is debit. 'Sales' (class 7) is income, so credit. VAT recoverable is a debit balance in class 4; VAT collected on sales is a credit balance in class 4."),
        H("Worked examples"),
        EX("Worked example 1: find the class", intro="Give the class of each account: (a) Delivery van, (b) Money owed to a supplier, (c) Rent paid, (d) Cash in hand, (e) Sales of goods.", steps=[
            S("(a) Delivery van", text="It lasts several years: a fixed asset, class **2**."),
            S("(b) Money owed to a supplier", text="A third party: class **4** (account 401)."),
            S("(c) Rent paid", text="A cost of running the business: class **6**."),
            S("(d) Cash in hand", text="Money available at once: class **5** (account 571)."),
            S("(e) Sales of goods", text="Income of the ordinary activity: class **7** (account 701)."),
        ]),
        EX("Worked example 2: normal balance", intro="State whether each account normally has a debit or a credit balance: 245 Vehicles, 411 Customers, 401 Suppliers, 701 Sales, 661 Wages.", steps=[
            S("Vehicles (class 2)", text="An asset: **debit**."),
            S("Customers 411", text="Customers owe us, so they are assets: **debit**."),
            S("Suppliers 401", text="We owe suppliers, so it is a liability: **credit**."),
            S("Sales 701 (class 7)", text="Income: **credit**."),
            S("Wages 661 (class 6)", text="Expense: **debit**."),
        ]),
        EX("Worked example 3: choose the account", intro="A trader pays FCFA 150 000 monthly rent by bank transfer. Which accounts, by class, are involved?", steps=[
            S("The expense", text="Rent is a cost of operating: class 6 (in the group for external services; check your textbook for the sub-number your teacher uses)."),
            S("The bank", text="Money leaves the bank account: class 5, account 521 Bank."),
            S("Direction", text="The expense increases, so it is debited; the bank asset decreases, so it is credited."),
        ]),
        MISTAKE("Using the wrong class for 'purchases of equipment'", "Goods bought to resell go to 601 Purchases (class 6). A machine bought to use for years is a fixed asset in class 2. The same shop invoice can contain both kinds of item; split them."),
        MISTAKE("Thinking class 4 is always a debit", "Class 4 holds both what customers owe us (debit) and what we owe suppliers, staff and the state (credit). Decide from the meaning of the account, not the class alone."),
        QUIZ("An account numbered 701 belongs to which class and what is its normal balance?",
             ["Class 6, debit", "Class 7, credit", "Class 7, debit", "Class 1, credit"], 1,
             "The first digit 7 means income; income normally has a credit balance.",
             hint="Read the first digit, then ask whether it is an expense or an income.",
             feedback=["Class 6 is expenses, and 701 starts with 7.", "", "Class 7 is correct but income has a credit balance.", "Class 1 is long-term resources, and the number starts with 7."]),
        QUIZ("Which item belongs in class 2?",
             ["Stock of rice", "Delivery van", "Bank balance", "Wages"], 1,
             "Class 2 is fixed assets; a delivery van is used for several years.",
             hint="Which one is used in the business for many years?",
             feedback=["Stock is class 3.", "", "Bank is class 5.", "Wages are an expense in class 6."]),
        PQ("Name the eight classes of the SYSCOHADA chart used in this course.",
           "1 Long-term resources; 2 Fixed assets; 3 Stocks; 4 Third parties; 5 Cash and bank (treasury); 6 Expenses of ordinary activities; 7 Income of ordinary activities; 8 Other expenses and income (non-ordinary, HAO)."),
        PQ("Why do OHADA countries use a common chart of accounts?",
           "A common numbered chart makes the accounts of all businesses use the same names and structure. This makes them comparable, easier to audit and tax, and understood by banks and investors across the member states."),
        PQ("Classify these accounts by class number: Buildings, Closing stock of goods, Customers, Interest on loan, Capital.",
           "Buildings: class 2. Stock of goods: class 3. Customers: class 4. Interest on loan: class 6 (financial expense). Capital: class 1."),
        TIP("In Paper 1, expect questions like 'Which class holds fixed assets?' or 'An account starting with 6 is...'. Learn the eight classes by heart: 1 resources, 2 fixed assets, 3 stock, 4 third parties, 5 cash, 6 expenses, 7 income, 8 other. Sub-numbers vary between textbooks, so rely on the class."),
        SUM("SYSCOHADA gives every account a number; the first digit is the class.",
            "Classes: 1 resources, 2 fixed assets, 3 stocks, 4 third parties, 5 cash and bank, 6 expenses, 7 income, 8 other items.",
            "Classes 1 to 5 describe the balance sheet; classes 6 and 7 give the profit.",
            "Normal balances: assets and expenses are debit; resources and income are credit; class 4 depends on the account."),
    ],
))

# ------------------------------------------------------------------ 3. accounting equation
# Amounts in FCFA thousands for the table: cash, stock, equipment, creditors, capital
_eq_state = dict(cash=0, stock=0, equip=0, cred=0, cap=0)
_eq_tx = [
    ("1 Owner puts in cash", dict(cash=3000, cap=3000)),
    ("2 Buys equipment, cash", dict(cash=-800, equip=800)),
    ("3 Buys goods on credit", dict(stock=500, cred=500)),
    ("4 Sells goods cost 200 for 350", dict(cash=350, stock=-200, cap=150)),
    ("5 Pays supplier 300", dict(cash=-300, cred=-300)),
    ("6 Owner takes cash 100", dict(cash=-100, cap=-100)),
]
_eq_rows = []
for _lab, _d in _eq_tx:
    for _k, _v in _d.items():
        _eq_state[_k] += _v
    _a = _eq_state["cash"] + _eq_state["stock"] + _eq_state["equip"]
    _lc = _eq_state["cred"] + _eq_state["cap"]
    assert _a == _lc, _lab
    _eq_rows.append(f"{_lab[0]}  {_eq_state['cash']:>5} {_eq_state['stock']:>5} {_eq_state['equip']:>5} |{_eq_state['cred']:>5} {_eq_state['cap']:>6} | {_a:>5} = {_lc:>5}")
assert _eq_state == dict(cash=2150, stock=300, equip=800, cred=200, cap=3050)
_eq_tbl = "No  Cash Stock Equip| Cred Capital|  Assets = Cap+Liab\n" + "\n".join(_eq_rows)
_eq_key = "\n".join(f"{lab}" for lab, _ in _eq_tx)

# worked example numbers
_ex_assets = 4200000 + 1800000 + 900000 + 600000
_ex_liab = 1500000 + 700000
_ex_cap = _ex_assets - _ex_liab
assert (_ex_assets, _ex_liab, _ex_cap) == (7500000, 2200000, 5300000)
_ex_cap2 = _ex_cap + 1100000 - 300000
assert _ex_cap2 == 6100000

LESSONS.append(lesson(
    module=M1,
    topic="The accounting equation",
    title="The accounting equation: assets, capital and liabilities",
    slug="acc1-accounting-equation",
    minutes=22,
    summary="The accounting equation says Assets = Capital + Liabilities. Every transaction changes the two sides in a way that keeps them equal, and profit, losses and drawings change capital.",
    objectives=[
        "Define assets, liabilities and capital (owner's equity)",
        "State the accounting equation and its rearrangements",
        "Show the effect of a transaction on the equation and keep both sides equal",
        "Explain how profit, loss and drawings change capital",
    ],
    key_concepts=["Asset", "Liability", "Capital", "Accounting equation", "Net assets", "Profit", "Drawings"],
    blocks=[
        H("Introduction"),
        T("Mr Ngu opens a small shop in Bamenda with FCFA 3 000 000 from his savings. Everything the shop owns came from somewhere: from his savings, or from people the shop owes. "
          "That simple idea is the whole of the accounting equation."),
        D("An **asset** is something of value the business owns or controls (cash, stock, equipment, money owed by customers). A **liability** is something the business owes to outsiders (suppliers, bank loans). **Capital** (the owner's equity) is what the business owes to its owner.",
          title="Definitions: asset, liability, capital"),
        KEY("The accounting equation", "What the business has equals what it owes to the owner plus what it owes to outsiders.", cards=[
            ["Assets = Capital + Liabilities", "The most used form. The left side shows what the business owns; the right side shows who financed it."],
            ["Capital = Assets - Liabilities", "Capital is also called **net assets**: what would be left for the owner after all debts were paid."],
            ["Liabilities = Assets - Capital", "Useful when the amount owed is the unknown figure."],
        ]),
        IMG("f5acc1-accounting-equation.svg", alt="A balance with Assets on the left (cash, stock, equipment, debtors) and Capital plus Liabilities on the right (owner's capital, creditors, loans), kept equal.", caption="Figure 1. The two sides of the accounting equation are always equal."),
        H("How transactions change the equation"),
        T("Every transaction has two effects. Sometimes both effects are on the same side (one asset goes up, another goes down), so the totals do not change. Sometimes both sides grow or both shrink together. The sides stay equal after every transaction. This is the **duality** concept from the first lesson."),
        T("Profit adds to capital, because the business has gained value that belongs to the owner. A loss reduces capital. **Drawings** (the owner taking cash or goods for private use) also reduce capital. Follow Mr Ngu's first six transactions. All figures are in FCFA thousands and are invented for practice."),
        CODE(_eq_key, "text", title="The six transactions"),
        CODE(_eq_tbl, "text", title="Effect on the equation (FCFA thousands, invented for practice)"),
        T("Check any row of the last column: the two totals are equal each time. In transaction 4 the goods cost 200 but were sold for 350, so cash rose by 350, stock fell by 200 and the difference of 150 is profit, which raised capital. In transaction 6 capital fell by the drawings of 100."),
        H("Worked examples"),
        EX("Worked example 1: find the missing figure", intro="On 31 December a trader in Douala has: premises FCFA 4 200 000, equipment 1 800 000, stock 900 000 and cash 600 000. He owes a bank loan of 1 500 000 and suppliers 700 000. Find his capital.", steps=[
            S("Add the assets", math=r"4\,200\,000 + 1\,800\,000 + 900\,000 + 600\,000 = 7\,500\,000"),
            S("Add the liabilities", math=r"1\,500\,000 + 700\,000 = 2\,200\,000"),
            S("Use Capital = Assets - Liabilities", math=r"7\,500\,000 - 2\,200\,000 = 5\,300\,000", text="His capital is **FCFA 5 300 000**."),
        ], check=r"7\,500\,000 = 5\,300\,000 + 2\,200\,000"),
        EX("Worked example 2: capital at the next year end", intro="In the following year the same trader makes a profit of FCFA 1 100 000 and takes drawings of FCFA 300 000. What is his new capital?", steps=[
            S("Start with the opening capital", text="FCFA 5 300 000 from example 1."),
            S("Add profit and subtract drawings", math=r"5\,300\,000 + 1\,100\,000 - 300\,000 = 6\,100\,000"),
            S("State the answer", text="Closing capital is **FCFA 6 100 000**. This is the rule: closing capital = opening capital + profit - drawings (+ any extra capital paid in)."),
        ]),
        EX("Worked example 3: show the effect", intro="Without a table, say what happens to Assets, Liabilities and Capital when a shop (a) buys a freezer FCFA 450 000 on credit from a supplier, and (b) pays FCFA 150 000 of that debt in cash.", steps=[
            S("(a) Buys on credit", text="Equipment (asset) rises by 450 000 and creditors (liability) rise by 450 000. Both sides rise by 450 000; capital does not change."),
            S("(b) Pays part of the debt", text="Cash (asset) falls by 150 000 and creditors (liability) fall by 150 000. Both sides fall by 150 000; capital does not change."),
            S("Result", text="After (a) and (b): assets are 300 000 higher than before and liabilities are 300 000 higher than before, so the equation still holds."),
        ]),
        MISTAKE("Treating a loan as capital", "A loan from a bank is a **liability**. Capital is only the money the owner has put in plus the profit left in the business, minus drawings. If you add the loan to capital, both sides will still agree but the report to the bank will be wrong."),
        MISTAKE("Forgetting that drawings reduce capital", "Cash taken home by the owner is not an expense of the business and is not a loss. It is drawings, and capital falls by that amount."),
        QUIZ("A business has assets of FCFA 9 000 000 and liabilities of FCFA 2 500 000. What is the capital?",
             ["FCFA 11 500 000", "FCFA 6 500 000", "FCFA 9 000 000", "FCFA 2 500 000"], 1,
             "Capital = Assets - Liabilities = 9 000 000 - 2 500 000 = 6 500 000.",
             hint="Which way do you rearrange Assets = Capital + Liabilities to find capital?",
             feedback=["You added the liabilities instead of subtracting them.", "", "That is the total of the assets, not the owner's share.", "That is the liabilities, not the capital."]),
        QUIZ("Which transaction increases both assets and liabilities?",
             ["Owner pays more cash into the business", "Goods are bought on credit", "Customer pays a debt in cash", "Rent is paid in cash"], 1,
             "Buying goods on credit adds stock (asset) and creditors (liability).",
             hint="Look for a transaction where something is gained and something is owed.",
             feedback=["That raises assets and capital, not liabilities.", "", "One asset (cash) rises and another (debtors) falls; nothing else changes.", "Cash falls and capital falls (an expense reduces profit)."]),
        PQ("Define asset, liability and capital, and write the accounting equation.",
           "An asset is something of value owned or controlled by the business. A liability is an amount owed to outsiders. Capital is the amount owed to the owner (assets minus liabilities). **Assets = Capital + Liabilities.**"),
        PQ("A shop owner starts with cash FCFA 2 000 000. She buys goods for FCFA 600 000 paying cash, then buys a till for FCFA 250 000 on credit. Write the assets, liabilities and capital at the end.",
           "Cash 2 000 000 - 600 000 = 1 400 000; stock 600 000; till 250 000. Assets = 1 400 000 + 600 000 + 250 000 = **2 250 000**. Liabilities (creditors) = **250 000**. Capital = 2 250 000 - 250 000 = **2 000 000** (unchanged)."),
        PQ("Opening capital is FCFA 3 000 000. During the year profit is FCFA 800 000, the owner pays in FCFA 500 000 more and takes drawings of FCFA 350 000. Find closing capital.",
           "3 000 000 + 800 000 + 500 000 - 350 000 = **FCFA 3 950 000**."),
        TIP("Paper 1 usually asks you to find one missing figure in the equation or to say which side a transaction affects. Write Assets = Capital + Liabilities first, then insert the numbers. In IAS/IFRS wording, capital is called 'equity' and the equation is written Assets - Liabilities = Equity; the meaning is the same."),
        SUM("Assets = Capital + Liabilities; capital = assets - liabilities.",
            "Every transaction keeps both sides equal; this is the duality concept.",
            "Profit and extra capital increase capital; losses and drawings reduce it.",
            "Closing capital = opening capital + profit - drawings (+ capital paid in).",
            "A loan is a liability, not capital."),
    ],
))

# ------------------------------------------------------------------ 4a/4b double entry and ledger
# One story reused by lessons 4a, 4b and 5 (Mr Ngu's shop, FCFA, invented for practice)
ENTRIES = [
    (1, "Owner pays capital into the business", "Cash", "Capital", 3000000),
    (2, "Buys equipment, pays cash", "Equipment", "Cash", 800000),
    (3, "Buys goods on credit from Fotso", "Purchases", "Creditors", 500000),
    (4, "Sells goods for cash", "Cash", "Sales", 350000),
    (5, "Pays part of the debt to Fotso", "Creditors", "Cash", 300000),
    (6, "Owner takes cash for private use", "Drawings", "Cash", 100000),
    (7, "Pays shop rent in cash", "Rent", "Cash", 60000),
]


def jtext(entries, w=26, a=10):
    out = []
    for no, _desc, dr, cr, amt in entries:
        out.append(f"{no}  Dr {dr:<{w}} {n(amt):>{a}}")
        out.append(f"   Cr {cr:<{w}} {'':>{a}} {n(amt):>{a}}")
    return "\n".join(out)


def ledger_sides(account, entries):
    d, c = [], []
    for no, _desc, dr, cr, amt in entries:
        if dr == account:
            d.append((f"{cr} ({no})", amt))
        if cr == account:
            c.append((f"{dr} ({no})", amt))
    return d, c


def ledger_balance(account, entries):
    d, c = ledger_sides(account, entries)
    return sum(x for _, x in d) - sum(x for _, x in c)


_accounts = ["Cash", "Capital", "Equipment", "Purchases", "Creditors", "Sales", "Drawings", "Rent"]
_bals = {a: ledger_balance(a, ENTRIES) for a in _accounts}
assert _bals == {"Cash": 2090000, "Capital": -3000000, "Equipment": 800000, "Purchases": 500000,
                 "Creditors": -200000, "Sales": -350000, "Drawings": 100000, "Rent": 60000}
assert sum(_bals.values()) == 0  # debits equal credits

_cash_acc = tacc("CASH ACCOUNT", *ledger_sides("Cash", ENTRIES))
_cred_acc = tacc("CREDITORS ACCOUNT (Fotso)", *ledger_sides("Creditors", ENTRIES))
_cap_acc = tacc("CAPITAL ACCOUNT", *ledger_sides("Capital", ENTRIES))
_cust_acc = tacc("ETOGA (CUSTOMER) ACCOUNT", [("Sales", 600000)], [("Cash received", 400000)])
assert "200 000" in _cust_acc

_rules = """Type of account   Increase with   Decrease with
Asset             Debit           Credit
Expense           Debit           Credit
Drawings          Debit           Credit
Liability         Credit          Debit
Capital           Credit          Debit
Income            Credit          Debit"""

LESSONS.append(lesson(
    module=M1,
    topic="Double entry and ledger posting",
    title="Double entry: debit and credit rules and journal entries",
    slug="acc1-double-entry-rules",
    minutes=25,
    summary="In double entry every transaction is recorded twice: a debit in one account and an equal credit in another. Assets, expenses and drawings increase with debits; liabilities, capital and income increase with credits.",
    objectives=[
        "State the double entry principle and the meaning of debit and credit",
        "Apply the debit and credit rules to assets, liabilities, capital, income, expenses and drawings",
        "Analyse a transaction into the two accounts affected and the side of each",
        "Write the entries for a series of transactions in journal form",
    ],
    key_concepts=["Double entry", "Debit", "Credit", "Account", "Drawings", "Dual aspect", "Narration"],
    blocks=[
        H("Introduction"),
        T("When Mr Ngu pays FCFA 800 000 cash for a freezer, two things happen at once: the shop gets a freezer and the shop loses cash. A good record shows both. This is the idea behind double entry, used by every accounting system in the world, including SYSCOHADA."),
        D("**Double entry** means every transaction affects at least two accounts: one account is **debited** and another is **credited** with the same amount. **Debit** (Dr) means the left side of an account; **credit** (Cr) means the right side. They do not mean 'good' or 'bad'.",
          title="Definition: double entry, debit, credit"),
        IMG("f5acc1-t-account.svg", alt="A T-shaped account with the word Debit on the left and Credit on the right, and the rule that assets and expenses increase on the left and liabilities, capital and income increase on the right.", caption="Figure 1. A T-account: the left side is the debit side, the right side is the credit side."),
        H("The debit and credit rules"),
        CODE(_rules, "text", title="Rules for each type of account"),
        KEY("A way to remember", "Three things grow on the debit side and three on the credit side.", cards=[
            ["Debit side grows", "**D**rawings, **E**xpenses, **A**ssets (DEA): what the business has or spends."],
            ["Credit side grows", "**L**iabilities, **I**ncome, **C**apital (LIC): where the money came from or what is earned."],
        ]),
        TIP("Under SYSCOHADA the same rules apply. Class 2, 3 and 5 accounts (assets) and class 6 (expenses) are debited to increase them; class 1 (capital and loans) and class 7 (income) are credited to increase them. Third-party accounts of class 4 follow their nature."),
        H("Analysing a transaction: three questions"),
        T("For any transaction ask: (1) Which two accounts are affected? (2) What type is each (asset, liability, capital, income, expense, drawings)? (3) Is each increasing or decreasing? The rules then tell you the side."),
        H("Worked examples"),
        EX("Worked example 1: cash purchase of equipment", intro="Mr Ngu pays FCFA 800 000 cash for a freezer.", steps=[
            S("Accounts affected", text="Equipment (asset) and Cash (asset)."),
            S("Direction", text="Equipment increases: debit. Cash decreases: credit."),
            S("Entry", math=r"\text{Dr Equipment } 800\,000 \qquad \text{Cr Cash } 800\,000"),
        ]),
        EX("Worked example 2: purchase of goods on credit", intro="He buys goods for resale worth FCFA 500 000 from Fotso, to be paid later.", steps=[
            S("Accounts affected", text="Purchases (expense, class 6) and Creditors, that is what he owes Fotso (liability)."),
            S("Direction", text="Purchases increase: debit. The liability increases: credit."),
            S("Entry", math=r"\text{Dr Purchases } 500\,000 \qquad \text{Cr Creditors (Fotso) } 500\,000"),
        ]),
        EX("Worked example 3: drawings", intro="The owner takes FCFA 100 000 cash from the till for private use.", steps=[
            S("Accounts affected", text="Drawings (reduces capital, so it is debited like an expense) and Cash (asset)."),
            S("Direction", text="Drawings increase: debit. Cash decreases: credit."),
            S("Entry", math=r"\text{Dr Drawings } 100\,000 \qquad \text{Cr Cash } 100\,000"),
        ]),
        T("Here are all seven transactions of the story, written in journal form. Read each line with its rule: assets and expenses debited when they rise; capital, liabilities and income credited when they rise."),
        CODE(jtext(ENTRIES), "text", title="Entries for Mr Ngu's first transactions (FCFA, invented for practice)"),
        CODE("\n".join(f"{no}  {desc}" for no, desc, *_ in ENTRIES), "text", title="What each number means"),
        T("Check the total of the debit amounts: every line has a matching credit of the same size, so total debits equal total credits. This equality is the foundation of the trial balance in a later lesson."),
        MISTAKE("Thinking debit means 'decrease'", "Debit increases an asset or an expense and decreases a liability, capital or income. Think of the type of account first, then apply the rule."),
        MISTAKE("Forgetting the second entry", "A one-sided entry makes the books out of balance. If you debit Cash, ask at once: which account is credited?"),
        MISTAKE("Crediting sales instead of debiting cash", "When a customer pays cash, the **cash** (asset) increases, so cash is **debited**. Sales (income) is **credited**."),
        QUIZ("The owner pays more money into the business bank account. Which entry is correct?",
             ["Dr Capital, Cr Bank", "Dr Bank, Cr Capital", "Dr Bank, Cr Drawings", "Dr Capital, Cr Sales"], 1,
             "Bank (asset) increases: debit. Capital (owner's money in) increases: credit.",
             hint="What type of account is Bank, and what happens to it?",
             feedback=["That would mean the owner took money out.", "", "Drawings is for money taken out, and it is a debit account.", "No sale has happened, so Sales is not involved."]),
        QUIZ("Which account is debited when the business pays wages of FCFA 70 000 in cash?",
             ["Cash", "Wages", "Capital", "Creditors"], 1,
             "Wages are an expense; expenses increase on the debit side. Cash is credited.",
             hint="Is wages an asset, an income or an expense?",
             feedback=["Cash decreases, so it is credited.", "", "Capital is changed by the final profit, not by each payment.", "No debt is involved in a cash payment."]),
        PQ("State the debit and credit entry for each: (a) sold goods for cash FCFA 90 000; (b) paid a supplier FCFA 40 000 in cash; (c) bought a computer on credit FCFA 300 000.",
           "(a) Dr Cash 90 000, Cr Sales 90 000. (b) Dr Creditors (supplier) 40 000, Cr Cash 40 000. (c) Dr Equipment (computer) 300 000, Cr Creditors 300 000."),
        PQ("Why do total debits always equal total credits in a correct set of books?",
           "Every transaction is entered twice with equal amounts: one debit and one credit. So the sum of all debits equals the sum of all credits."),
        PQ("Name the type of account (asset, liability, capital, income, expense or drawings) and the side that increases it: Bank loan, Rent paid, Sales, Vehicles, Drawings.",
           "Bank loan: liability, credit. Rent paid: expense, debit. Sales: income, credit. Vehicles: asset, debit. Drawings: debit."),
        TIP("In Paper 1 and Paper 2 Question 5 (trading transactions), the quickest method is to name the two accounts, then write Dr or Cr using the rules. Always show the narration (a short explanation) when asked to write journal entries."),
        SUM("Double entry: every transaction has a debit and an equal credit.",
            "Debit = left, credit = right. Debit increases assets, expenses and drawings.",
            "Credit increases liabilities, capital and income.",
            "Analyse each transaction: two accounts, their types, and the direction of change.",
            "Total debits equal total credits."),
    ],
))

LESSONS.append(lesson(
    module=M1,
    topic="Double entry and ledger posting",
    title="Posting to the ledger and balancing accounts",
    slug="acc1-ledger-posting-and-balancing",
    minutes=25,
    summary="The ledger holds one account for each item. Entries are posted from the journal to the debit side of one account and the credit side of another; at the end of the period each account is totalled and balanced.",
    objectives=[
        "Explain what the ledger is and how it differs from the journal",
        "Post entries to ledger accounts, showing the other account",
        "Balance an account: totals, balance c/d and balance b/d",
        "State whether an account has a debit or a credit balance",
    ],
    key_concepts=["Ledger", "Posting", "Balance c/d", "Balance b/d", "Debit balance", "Credit balance", "Folio"],
    blocks=[
        H("Introduction"),
        T("A teacher records each student's marks in one big exercise book, then one page per student. The book of first record is like the journal. The pages per student are like the ledger accounts. "
          "In accounting, the journal records transactions in time order; the ledger collects them by account, so you can see at once how much cash is left or how much a supplier is owed."),
        D("The **ledger** is the book (or file) of accounts: one account for each asset, liability, capital item, income and expense. **Posting** is copying an entry from the book of original entry to the right side of the right ledger accounts.",
          title="Definition: ledger and posting"),
        T("An account has a heading, a **debit** (left) side and a **credit** (right) side. Each line shows the date, the **other account** involved (so you can trace the entry), and the amount. In larger systems a **folio** number gives the page of the other account."),
        KEY("Posting rule", "For each journal entry make two postings.", cards=[
            ["Debit posting", "Write the amount on the **debit** side of the account debited. In the details column write the name of the account credited."],
            ["Credit posting", "Write the amount on the **credit** side of the account credited. In the details column write the name of the account debited."],
        ]),
        H("Balancing an account"),
        D("To **balance** an account: (1) add up each side; (2) find the difference; (3) write the difference on the smaller side as **balance c/d** (carried down) so that both sides are equal; (4) write the total on both sides at the same level; (5) bring the balance down under the total on the opposite side as **balance b/d** (brought down). If the debit total is bigger, the account has a **debit balance**; otherwise a **credit balance**.",
          title="How to balance"),
        H("Worked examples"),
        EX("Worked example 1: the cash account", intro="Post the seven transactions of Mr Ngu's shop (listed in the previous lesson) to the cash account and balance it. Amounts in FCFA, invented for practice.", steps=[
            S("Find the cash entries", text="Cash is debited in transactions 1 (capital 3 000 000) and 4 (sales 350 000). Cash is credited in 2 (equipment 800 000), 5 (Fotso 300 000), 6 (drawings 100 000) and 7 (rent 60 000)."),
            S("Add the sides", math=r"\text{Dr } 3\,000\,000 + 350\,000 = 3\,350\,000 \qquad \text{Cr } 800\,000 + 300\,000 + 100\,000 + 60\,000 = 1\,260\,000"),
            S("Balance", math=r"3\,350\,000 - 1\,260\,000 = 2\,090\,000", text="The difference goes on the credit side as balance c/d. It comes down on the debit side as balance b/d: Mr Ngu has FCFA 2 090 000 in cash."),
        ]),
        CODE(_cash_acc, "text", title="Cash account (FCFA)"),
        EX("Worked example 2: the creditors account", intro="Balance the account of the supplier Fotso.", steps=[
            S("Credit side", text="Transaction 3: goods on credit, 500 000."),
            S("Debit side", text="Transaction 5: payment, 300 000."),
            S("Balance", math=r"500\,000 - 300\,000 = 200\,000", text="The credit side is bigger, so the balance is a **credit balance** of FCFA 200 000: the shop still owes Fotso that amount."),
        ]),
        CODE(_cred_acc, "text", title="Creditors account (FCFA)"),
        EX("Worked example 3: a customer's account", intro="Mr Etoga buys goods on credit for FCFA 600 000. He later pays FCFA 400 000 in cash. Show his account.", steps=[
            S("Debit what he owes", text="Sales on credit: debit his account 600 000 (an asset: he owes us)."),
            S("Credit what he pays", text="Cash received: credit his account 400 000."),
            S("Balance", math=r"600\,000 - 400\,000 = 200\,000", text="The debit side is bigger, so it is a **debit balance** of FCFA 200 000: he still owes us that amount."),
        ]),
        CODE(_cust_acc, "text", title="Etoga account (FCFA, invented for practice)"),
        T("The other accounts of the story are simple, with one entry each. After posting, the balances are shown below. Debit balances are on the left, credit balances on the right."),
        CODE("Account       Debit balance  Credit balance\n" + "\n".join(
            f"{a:<12}{(n(v) if v > 0 else ''):>14}{(n(-v) if v < 0 else ''):>16}" for a, v in _bals.items()), "text", title="Balances after all seven transactions (FCFA)"),
        CODE(_cap_acc, "text", title="Capital account (only one entry, so no balancing needed beyond the total)"),
        MISTAKE("Writing the account's own name in the details column", "The details column shows the **other** account of the entry. If you write 'Cash' in the cash account, the trail is lost."),
        MISTAKE("Putting the balance c/d on the bigger side", "Balance c/d goes on the **smaller** side, to make both sides equal. The balance b/d then goes on the **bigger** side's side, on the opposite side from c/d."),
        MISTAKE("Calling every balance 'a debit'", "Check the sides. A bigger debit side gives a debit balance; a bigger credit side gives a credit balance."),
        QUIZ("The debit side of an account totals FCFA 750 000 and the credit side FCFA 480 000. What is the balance?",
             ["Credit balance 270 000", "Debit balance 270 000", "Debit balance 750 000", "Credit balance 1 230 000"], 1,
             "750 000 - 480 000 = 270 000, and the debit side is bigger, so it is a debit balance carried down on the credit side and brought down on the debit side.",
             hint="Subtract the smaller total from the bigger one, then see which side was bigger.",
             feedback=["The debit side is the bigger one, so it is a debit balance.", "", "That is the debit total, not the difference.", "You added the sides instead of subtracting."]),
        QUIZ("What does 'balance b/d' mean?",
             ["The balance carried down at the end of the period", "The balance brought down at the start of the next period", "The bank deposit", "A balance that cannot be explained"], 1,
             "b/d means brought down: it is the opening balance of the next period, on the side opposite to the c/d.",
             hint="b stands for brought.",
             feedback=["That is balance c/d.", "", "It has nothing to do with the bank.", "A balance can always be explained by the entries."]),
        PQ("Open and balance a cash account from these entries: Dr capital 900 000; Dr sales 120 000; Cr rent 80 000; Cr purchases 250 000. State the balance and its side.",
           "Debit side 900 000 + 120 000 = 1 020 000. Credit side 80 000 + 250 000 = 330 000. Balance = 1 020 000 - 330 000 = **690 000 debit** (balance c/d on the credit side, balance b/d on the debit side)."),
        PQ("Why is a customer's account a debit balance but a supplier's account a credit balance?",
           "A customer owes us money, which is an asset (debit). A supplier is owed money by us, which is a liability (credit)."),
        PQ("List the five steps of balancing an account.",
           "Add each side; find the difference; write it on the smaller side as balance c/d; write the equal total on both sides; bring the balance down on the opposite side as balance b/d."),
        TIP("Paper 2 Question 5 (trading transactions) has asked for entries and accounts from a list of transactions. Show each posting with the other account's name, and always carry the balance down. A neat layout earns the presentation marks."),
        SUM("The ledger holds one account per item; posting copies each journal entry to two accounts.",
            "Each posting shows the other account in the details column.",
            "To balance: add both sides, put the difference on the smaller side as balance c/d, total both sides, bring down the balance b/d.",
            "A bigger debit side gives a debit balance; a bigger credit side gives a credit balance.",
            "Customers' accounts are normally debit; suppliers' accounts are normally credit."),
    ],
))

# ------------------------------------------------------------------ 5. trial balance
_tb1_rows = [(a, "D" if v > 0 else "C", abs(v)) for a, v in _bals.items()]
_tb1_rows.sort(key=lambda r: (r[1] == "C", ["Cash", "Equipment", "Purchases", "Drawings", "Rent", "Capital", "Sales", "Creditors"].index(r[0])))
_tb1 = tb(_tb1_rows, w=14, a=11)
assert sum(a for _, s, a in _tb1_rows if s == "D") == sum(a for _, s, a in _tb1_rows if s == "C") == 3550000

_tb2_rows = [("Premises", "D", 12000000), ("Vehicles", "D", 4500000), ("Purchases", "D", 6200000), ("Debtors", "D", 1350000),
             ("Bank", "D", 2100000), ("Cash", "D", 150000), ("Rent", "D", 480000), ("Wages", "D", 1200000), ("Drawings", "D", 600000),
             ("Sales", "C", 9800000), ("Creditors", "C", 900000), ("Bank loan", "C", 3000000), ("Capital", "C", 14880000)]
assert sum(a for _, s, a in _tb2_rows if s == "D") == sum(a for _, s, a in _tb2_rows if s == "C") == 28580000
_tb2 = tb(_tb2_rows, w=14, a=11)

_tb3_good = [("Equipment", "D", 1200000), ("Purchases", "D", 800000), ("Debtors", "D", 540000), ("Cash", "D", 300000), ("Rent", "D", 120000),
             ("Capital", "C", 1500000), ("Sales", "C", 1000000), ("Creditors", "C", 460000)]
assert sum(a for _, s, a in _tb3_good if s == "D") == sum(a for _, s, a in _tb3_good if s == "C") == 2960000
_tb3_bad = [r if r[0] != "Debtors" else ("Debtors", "D", 450000) for r in _tb3_good]
_tb3 = tb(_tb3_bad, w=14, a=11)
assert sum(a for _, s, a in _tb3_bad if s == "D") == 2870000 and 2960000 - 2870000 == 90000 and 90000 % 9 == 0

LESSONS.append(lesson(
    module=M1,
    topic="The trial balance",
    title="The trial balance: extracting, totalling and checking",
    slug="acc1-trial-balance",
    minutes=22,
    summary="A trial balance lists every ledger balance in a debit or a credit column. If the books are in balance the two totals are equal, but equal totals do not prove that the books are free from error.",
    objectives=[
        "Define a trial balance and state its purpose",
        "Extract balances from ledger accounts and place them in the correct column",
        "Total the columns and decide whether the trial balance agrees",
        "Name the errors that a trial balance does and does not reveal",
    ],
    key_concepts=["Trial balance", "Debit column", "Credit column", "Arithmetical accuracy", "Transposition error"],
    blocks=[
        H("Introduction"),
        T("After a month of recording, Mr Ngu has seven accounts with many entries. Has he made any mistake? A quick test exists. If every entry had a debit and an equal credit, then the debit balances added together must equal the credit balances added together. The list used for this test is the trial balance."),
        D("A **trial balance** is a list of the balances of all ledger accounts at a given date, with debit balances in one column and credit balances in the other. Its main purpose is to check the arithmetical accuracy of the double entry, and it is the starting point for preparing the final accounts.",
          title="Definition: trial balance"),
        H("How to prepare it"),
        KEY("Four steps", "Do them in this order.", cards=[
            ["1 Balance every account", "Total each ledger account and find its balance, as in the last lesson."],
            ["2 List the accounts", "Write each account name in a list, with the date of the trial balance at the top."],
            ["3 Place each balance", "A debit balance goes in the debit column; a credit balance goes in the credit column. Accounts with no balance are left out."],
            ["4 Total and compare", "Add each column. Equal totals mean the books balance."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: trial balance from the ledger", intro="Extract a trial balance from the ledger of Mr Ngu's shop built in the last lesson. The balances are: Cash 2 090 000 (Dr), Equipment 800 000 (Dr), Purchases 500 000 (Dr), Drawings 100 000 (Dr), Rent 60 000 (Dr), Capital 3 000 000 (Cr), Sales 350 000 (Cr), Creditors 200 000 (Cr).", steps=[
            S("Place the balances", text="Assets, expenses and drawings are debit balances; capital, income and liabilities are credit balances."),
            S("Add the debit column", math=r"2\,090\,000 + 800\,000 + 500\,000 + 100\,000 + 60\,000 = 3\,550\,000"),
            S("Add the credit column", math=r"3\,000\,000 + 350\,000 + 200\,000 = 3\,550\,000", text="Both totals are FCFA 3 550 000: the trial balance agrees."),
        ]),
        CODE("Mr Ngu - Trial balance (FCFA, invented for practice)\n" + _tb1, "text", title="Trial balance"),
        EX("Worked example 2: a larger trial balance", intro="Fotso Stores (invented for practice) lists these balances at 31 December. Prepare the trial balance and check it: Premises 12 000 000, Vehicles 4 500 000, Purchases 6 200 000, Debtors 1 350 000, Bank 2 100 000, Cash 150 000, Rent 480 000, Wages 1 200 000, Drawings 600 000, Sales 9 800 000, Creditors 900 000, Bank loan 3 000 000, Capital 14 880 000.", steps=[
            S("Sort by nature", text="Assets (premises, vehicles, debtors, bank, cash), expenses (purchases, rent, wages) and drawings are debit. Sales, creditors, bank loan and capital are credit."),
            S("Total the debit column", math=r"12\,000\,000 + 4\,500\,000 + 6\,200\,000 + 1\,350\,000 + 2\,100\,000 + 150\,000 + 480\,000 + 1\,200\,000 + 600\,000 = 28\,580\,000"),
            S("Total the credit column", math=r"9\,800\,000 + 900\,000 + 3\,000\,000 + 14\,880\,000 = 28\,580\,000", text="The totals agree."),
        ]),
        CODE("Fotso Stores - Trial balance at 31 December (FCFA)\n" + _tb2, "text", title="Trial balance"),
        EX("Worked example 3: totals that do not agree", intro="A trial balance shows the totals below. Find the cause of the difference. The debtors figure should be 540 000 but was copied as 450 000.", steps=[
            S("Find the difference", math=r"2\,960\,000 - 2\,870\,000 = 90\,000", text="Credits are bigger than debits by FCFA 90 000 (see the totals below)."),
            S("Use the nine test", text="A difference that divides exactly by 9 often means two digits were swapped (a **transposition**): 90 000 / 9 = 10 000. The numbers 540 and 450 are such a pair."),
            S("Correct it", text="Debtors should be 540 000. The debit total then becomes 2 960 000 and agrees with the credits."),
        ]),
        CODE("Trial balance as first extracted (FCFA)\n" + _tb3, "text", title="Totals do not agree"),
        H("What the trial balance proves, and what it does not"),
        T("A trial balance that agrees shows that total debits equal total credits. It does not prove the books are right. These errors leave the totals equal, so the trial balance does not reveal them: an entry **omitted** completely; an entry made in the **wrong account of the right class** (commission); an entry in the wrong **type** of account (principle); an amount wrong in the **original entry** and posted correctly; **compensating** errors (two mistakes that cancel); **reversal** of the debit and credit. You will study these errors in a later module."),
        T("Errors that do change the totals include a one-sided entry, a wrong balance carried down, and an amount posted with a different figure on each side (such as the transposition above)."),
        MISTAKE("Putting a credit balance in the debit column", "Check the nature of each account. A bank overdraft is a credit balance even though 'bank' is usually an asset. A trader whose customers account has a credit balance (customer overpaid) is rare; check the ledger."),
        MISTAKE("Forcing the totals to agree", "Never enter a made-up figure to balance. A balancing figure may be placed in a suspense account (later lesson), but the error must still be found."),
        MISTAKE("Leaving out an account with a balance", "A missing account is the commonest reason a long trial balance does not agree. Count the ledger accounts and the lines on your list."),
        QUIZ("Which balance is placed in the credit column of a trial balance?",
             ["Machinery", "Sales", "Wages", "Drawings"], 1,
             "Sales is income, which has a credit balance. The others are an asset, an expense and drawings, which are debit balances.",
             hint="Which of these four is an income?",
             feedback=["Machinery is an asset: debit.", "", "Wages are an expense: debit.", "Drawings reduce capital and are debit."]),
        QUIZ("A trial balance agrees. Which statement is correct?",
             ["The books contain no errors at all", "Total debits equal total credits, but some errors may remain", "The profit is correct", "All entries were posted to the right accounts"], 1,
             "Equal totals show arithmetical accuracy only. Some errors do not change the totals.",
             hint="What does a trial balance actually test?",
             feedback=["Errors such as omissions and compensating errors are not detected.", "", "Profit depends on correct classification, which is not tested.", "Posting to a wrong account of the same class is not detected."]),
        PQ("Define a trial balance and give two uses.",
           "A trial balance is a list of ledger balances at a date, in debit and credit columns. Uses: it checks the arithmetical accuracy of the double entry, and it provides the figures from which the final accounts are prepared."),
        PQ("Prepare the totals of a trial balance with debit balances: cash 400 000, equipment 1 500 000, purchases 900 000, and credit balances: capital 2 000 000, sales 650 000, creditors 150 000. Do the totals agree?",
           "Debit total = 400 000 + 1 500 000 + 900 000 = 2 800 000. Credit total = 2 000 000 + 650 000 + 150 000 = 2 800 000. **They agree.**"),
        PQ("Name three errors that a trial balance does not disclose.",
           "Any three of: error of omission, error of commission, error of principle, error of original entry, compensating error, error of reversal."),
        TIP("In Paper 1, expect questions on which errors the trial balance reveals and on where an account belongs in the columns. In Paper 2 you are often given a list of balances and asked to prepare the trial balance and then the final accounts. List the accounts in the order given and tick each one off."),
        SUM("A trial balance lists ledger balances in debit and credit columns.",
            "If the double entry is arithmetically right, the two totals are equal.",
            "Assets, expenses and drawings are debit; capital, liabilities and income are credit.",
            "A difference divisible by 9 may be a transposition error.",
            "Equal totals do not prove that there are no errors."),
    ],
))

# ------------------------------------------------------------------ 6. invoices and discounts
_L1 = 50 * 18000
_L2 = 20 * 12000
_gross = _L1 + _L2
_trade = _gross * 10 // 100
_net = _gross - _trade
_fin = _net * 2 // 100
_pay = _net - _fin
assert (_L1, _L2, _gross, _trade, _net, _fin, _pay) == (900000, 240000, 1140000, 114000, 1026000, 20520, 1005480)
assert _gross * 10 % 100 == 0 and _net * 2 % 100 == 0


def inv_line(qty, desc, price, amount, w=20):
    return f"{qty:>3} {desc:<{w}}{n(price):>8}{n(amount):>11}"


_inv = "\n".join([
    "KAMGA WHOLESALE, Douala            Invoice K101",
    "To: Tabi Stores, Bamenda           Date: 3 March",
    "",
    f"{'Qty':>3} {'Description':<20}{'Price':>8}{'Amount':>11}",
    inv_line(50, "Bags of rice", 18000, _L1),
    inv_line(20, "Cartons tomato paste", 12000, _L2),
    f"{'Gross amount':<32}{n(_gross):>11}",
    f"{'Less trade discount 10%':<32}{'-' + n(_trade):>11}",
    f"{'Net commercial amount':<32}{n(_net):>11}",
    "",
    "Terms: 2% financial discount if paid",
    "within 10 days of the invoice date.",
])

_ex3_list = 400000
_ex3_trade = _ex3_list * 25 // 100
_ex3_net = _ex3_list - _ex3_trade
_ex3_fin = _ex3_net * 5 // 100
_ex3_pay = _ex3_net - _ex3_fin
assert (_ex3_trade, _ex3_net, _ex3_fin, _ex3_pay) == (100000, 300000, 15000, 285000)

_rist = 8000000 * 3 // 100
assert _rist == 240000

LESSONS.append(lesson(
    module=M2,
    topic="Invoices, trade discount and financial discount",
    title="Invoices, trade discount and financial discount",
    slug="acc1-invoices-and-discounts",
    minutes=22,
    summary="An invoice is the seller's bill. Trade discount is deducted on the invoice and is not recorded; financial discount is a reduction for quick payment and is recorded as discount allowed or received. Rebates, remises and ristournes are price reductions of different kinds.",
    objectives=[
        "Describe an invoice, a credit note and a debit note and say who prepares each",
        "Calculate gross amount, trade discount and net commercial amount",
        "Calculate financial discount and the amount actually paid",
        "Distinguish rebate (rabais), remise and ristourne, and say how each discount is recorded",
    ],
    key_concepts=["Invoice", "Trade discount", "Net commercial amount", "Financial discount", "Rabais, remise, ristourne", "Credit note"],
    blocks=[
        H("Introduction"),
        T("When Tabi Stores in Bamenda buys rice and tomato paste from a wholesaler in Douala, the wholesaler sends a paper that lists what was sold, at what price, and how much to pay. That paper is the first record of the sale for both businesses. Every entry in the books starts from a document like this."),
        D("An **invoice** is a document prepared by the seller that shows the goods or services supplied, their quantity, price, any deductions, and the amount payable. The seller's copy is a **sales invoice**; the buyer's copy is a **purchase invoice**. Invoices are numbered, so they can be traced.",
          title="Definition: invoice"),
        KEY("Related documents", "These documents all start the accounting records.", cards=[
            ["Credit note", "Sent by the seller to reduce the buyer's debt, for example when goods are returned or a price was too high."],
            ["Debit note", "Sent to increase the amount due, for example when the invoice was too low. Often written by the buyer to ask for credit."],
            ["Statement of account", "A summary sent monthly by the seller of invoices, credit notes and payments, so the buyer can check the balance."],
        ]),
        H("Trade discount"),
        D("**Trade discount** is a reduction in the list price given to a buyer because of quantity, status (for example a wholesaler buying from a manufacturer) or regular trade. It is shown on the invoice, and **is not recorded in the ledger**: only the net amount is entered.",
          title="Definition: trade discount",
          formula=r"\text{Net commercial amount} = \text{Gross amount} - \text{Trade discount}"),
        T("In the OHADA system the trade reductions are named by their reason: a **rabais** (rebate) is given for defects or poor quality; a **remise** (discount) is given for a large order or the buyer's status; a **ristourne** (rebate or bonus) is given at the end of a period for a large total of purchases. Together they are called RRR. Check your textbook for how your teacher translates them."),
        CODE(_inv, "text", title="Invoice (FCFA, invented for practice; VAT is added in the next lesson)"),
        H("Financial discount"),
        D("**Financial discount** (escompte de reglement) is a reduction allowed to a customer who pays quickly, within a stated number of days. It is a financial matter, not a price reduction, so it **is recorded**. The seller records **discount allowed** (an expense); the buyer records **discount received** (an income). Financial discount is calculated on the net commercial amount.",
          title="Definition: financial discount"),
        EX("Worked example 1: the invoice", intro="Find the net commercial amount of invoice K101 above.", steps=[
            S("Value each line", math=r"50 \times 18\,000 = 900\,000 \qquad 20 \times 12\,000 = 240\,000"),
            S("Gross amount", math=r"900\,000 + 240\,000 = 1\,140\,000"),
            S("Trade discount 10%", math=r"1\,140\,000 \times 10\% = 114\,000"),
            S("Net commercial amount", math=r"1\,140\,000 - 114\,000 = 1\,026\,000", text="The buyer will record purchases of **FCFA 1 026 000**."),
        ]),
        EX("Worked example 2: paying within the discount period", intro="Tabi Stores pays invoice K101 on the 8th day. Find the cash paid and the entries (VAT ignored for now).", steps=[
            S("Discount", math=r"1\,026\,000 \times 2\% = 20\,520", text="The financial discount is calculated on the net amount, 1 026 000."),
            S("Cash paid", math=r"1\,026\,000 - 20\,520 = 1\,005\,480"),
            S("Buyer's entry", text="Dr Supplier (Kamga) 1 026 000; Cr Bank 1 005 480; Cr Discount received 20 520. The supplier's account is cleared."),
            S("Seller's entry", text="Dr Bank 1 005 480; Dr Discount allowed 20 520; Cr Customer (Tabi) 1 026 000."),
        ]),
        EX("Worked example 3: both discounts", intro="List price FCFA 400 000, trade discount 25%, financial discount 5% for payment within 7 days. What is paid on day 5?", steps=[
            S("Trade discount", math=r"400\,000 \times 25\% = 100\,000", text="Net commercial amount = 400 000 - 100 000 = 300 000."),
            S("Financial discount on the net amount", math=r"300\,000 \times 5\% = 15\,000"),
            S("Amount paid", math=r"300\,000 - 15\,000 = 285\,000"),
        ]),
        T("A ristourne is worked out the same way, but it comes after the year. If a supplier gives a 3% ristourne on total purchases of FCFA 8 000 000, the buyer receives a credit of 8 000 000 x 3% = FCFA 240 000."),
        MISTAKE("Recording trade discount in the books", "Trade discount is on the invoice; only the net amount is entered in the books. Do not open a discount account for it."),
        MISTAKE("Calculating financial discount on the gross amount", "Financial discount is worked out on the amount after trade discount. In example 2 that is 1 026 000, not 1 140 000."),
        MISTAKE("Taking financial discount when the buyer paid late", "If the buyer pays after the stated period, there is no discount. The buyer pays the full net amount."),
        QUIZ("An invoice shows gross FCFA 600 000 and a trade discount of 20%. What is the net commercial amount?",
             ["FCFA 120 000", "FCFA 480 000", "FCFA 520 000", "FCFA 720 000"], 1,
             "Trade discount = 600 000 x 20% = 120 000. Net = 600 000 - 120 000 = 480 000.",
             hint="First find the discount in francs, then subtract.",
             feedback=["That is the discount, not the net amount.", "", "You took 80 000 off, which is not 20%.", "You added the discount instead of subtracting."]),
        QUIZ("Which discount is recorded in the ledger?",
             ["Trade discount", "Financial discount", "Both", "Neither"], 1,
             "Financial discount (for prompt payment) is recorded as discount allowed or received. Trade discount only changes the invoice value.",
             hint="Which discount depends on when the customer pays?",
             feedback=["Trade discount is deducted on the invoice and not recorded.", "", "Only one of the two is recorded.", "Financial discount is recorded."]),
        PQ("Define trade discount and financial discount, and say which one is entered in the ledger.",
           "Trade discount: a reduction on the list price for quantity or status, shown on the invoice. Financial discount: a reduction allowed for prompt payment. Only the **financial** discount is entered in the ledger (discount allowed or discount received)."),
        PQ("Goods listed at FCFA 500 000 are sold with 15% trade discount and 4% financial discount for payment in 10 days. Find the cash received if the customer pays in 6 days.",
           "Trade discount 500 000 x 15% = 75 000; net = 425 000. Financial discount 425 000 x 4% = 17 000. Cash received = 425 000 - 17 000 = **FCFA 408 000**."),
        PQ("Explain the difference between rabais, remise and ristourne.",
           "Rabais: reduction for defects or low quality. Remise: reduction for a large order or the buyer's status. Ristourne: end-of-period bonus for a large total of purchases."),
        TIP("Paper 2 Question 5 (trading transactions) gives a list of transactions with discounts. Tabulate each invoice: gross, trade discount, net, then financial discount. In IAS/IFRS wording, discount allowed and discount received are shown as expense and income, and the same two kinds of discount are taught."),
        SUM("An invoice is the seller's bill; the buyer keeps it as a purchase invoice. Credit notes reduce the amount due.",
            "Net commercial amount = gross amount - trade discount; only the net amount is recorded.",
            "Financial discount rewards prompt payment, is calculated on the net amount and is recorded (discount allowed or received).",
            "Rabais is for defects, remise for quantity or status, ristourne for a period total."),
    ],
))

# ------------------------------------------------------------------ 7. VAT, transport, containers
_net2 = _net
_v = vat(_net2)
_tr = 40000
_trv = vat(_tr)
_dep = 50000
_goods_tr_net = _net2 + _tr
_vat_tot = _v + _trv
_total = _goods_tr_net + _vat_tot + _dep
assert (_v, _trv, _vat_tot, _total) == (197505, 7700, 205205, 1321205)
assert vat(_goods_tr_net) == _vat_tot
_out = vat(8000000)
_in = vat(5200000)
assert (_out, _in, _out - _in) == (1540000, 1001000, 539000)
_incl = 1192500
assert vat(1000000) == 192500 and 1000000 + 192500 == _incl

_inv2 = "\n".join([
    f"{'Net commercial amount (goods)':<34}{n(_net2):>11}",
    f"{'Transport charged':<34}{n(_tr):>11}",
    f"{'Net amount subject to VAT':<34}{n(_goods_tr_net):>11}",
    f"{'VAT 19.25%':<34}{n(_vat_tot):>11}",
    f"{'Deposit on 20 returnable crates':<34}{n(_dep):>11}",
    "-" * 45,
    f"{'TOTAL TO PAY':<34}{n(_total):>11}",
])
_dr = _net2 + _tr + _vat_tot + _dep
assert _dr == _total
_vat_tbl = "\n".join([
    f"{'Output VAT (collected on sales 8 000 000)':<44}{n(_out):>10}",
    f"{'Input VAT (paid on purchases 5 200 000)':<44}{n(_in):>10}",
    "-" * 54,
    f"{'VAT payable to the tax office':<44}{n(_out - _in):>10}",
])
_entry_buyer = "\n".join([
    f"Dr Purchases (601)                {n(_net2):>11}",
    f"Dr Transport on purchases         {n(_tr):>11}",
    f"Dr VAT recoverable (445)          {n(_vat_tot):>11}",
    f"Dr Returnable containers deposit  {n(_dep):>11}",
    f"   Cr Supplier (401)                         {n(_total):>11}",
])

LESSONS.append(lesson(
    module=M2,
    topic="VAT, transport and returnable containers",
    title="VAT, transport charges and returnable containers",
    slug="acc1-vat-transport-containers",
    minutes=24,
    summary="VAT at 19.25% (check the current rate) is added to the net price and is collected for the state. Transport is part of the invoice and bears VAT; returnable containers carry a deposit that is credited back when they are returned.",
    objectives=[
        "Calculate VAT on a net amount and find the amount including VAT",
        "Distinguish output VAT (collected) from input VAT (recoverable) and find VAT payable",
        "Treat transport charges on an invoice",
        "Account for the deposit on returnable containers and its refund",
    ],
    key_concepts=["VAT (TVA)", "Input VAT", "Output VAT", "VAT payable", "Carriage inwards", "Returnable container", "Deposit"],
    blocks=[
        H("Introduction"),
        T("When you buy a phone card or a bag of cement from a registered business, part of the price goes to the state as value added tax. In French it is the TVA (taxe sur la valeur ajoutee). The business does not keep this money. It collects it from customers and pays it over, after deducting the VAT it paid to its own suppliers."),
        D("**VAT** is a tax on the value added at each stage of production and sale. In Cameroon the standard rate used in textbooks is **19.25%** (a VAT of 17.5% with a council surcharge of 10% of the VAT). Rates and rules change, so **check the current rate** before using it in real life; in an exam, use the rate given in the question.",
          title="Definition: VAT"),
        KEY("Input and output VAT", "A VAT-registered business deals with VAT in two directions.", cards=[
            ["Output VAT (VAT collected)", "VAT charged to customers on sales. It is a **liability**: the business owes it to the state. Credit balance in the VAT collected account."],
            ["Input VAT (VAT recoverable)", "VAT paid to suppliers on purchases. It is an **asset**: the state will allow the business to deduct it. Debit balance in the VAT recoverable account."],
            ["VAT payable", "Output VAT minus input VAT. If input is bigger, the business can claim the difference back or carry it forward."],
        ]),
        F(r"\text{VAT} = \text{net amount} \times 19.25\% \qquad \text{Total} = \text{net amount} \times 1.1925", title="VAT formulae"),
        H("Transport and returnable containers"),
        T("**Transport** (carriage) charged on an invoice is part of what the buyer pays and normally bears VAT. For the buyer, transport on goods bought (**carriage inwards**) is a cost of getting the goods; for the seller, transport on goods sold (**carriage outwards**) is a selling cost."),
        D("A **returnable container** (crate, drum, bottle crate) is packing that the seller lends for a **deposit**. The deposit is charged on the invoice. When the containers are returned the seller issues a credit note and the deposit is repaid or deducted. The deposit is not a sale and, in our examples, carries no VAT; check your textbook for the rule your teacher uses.",
          title="Definition: returnable container and deposit"),
        EX("Worked example 1: VAT on invoice K101", intro="Invoice K101 has a net commercial amount of FCFA 1 026 000. Transport of FCFA 40 000 is charged and 20 returnable crates carry a deposit of FCFA 50 000. Find the total to pay.", steps=[
            S("VAT on the goods", math=r"1\,026\,000 \times 19.25\% = 197\,505"),
            S("VAT on the transport", math=r"40\,000 \times 19.25\% = 7\,700", text="Total VAT = 197 505 + 7 700 = 205 205."),
            S("Add everything", math=r"1\,026\,000 + 40\,000 + 205\,205 + 50\,000 = 1\,321\,205", text="The buyer pays **FCFA 1 321 205**, of which 50 000 is a refundable deposit."),
        ], check=r"1\,066\,000 \times 0.1925 = 205\,205"),
        CODE(_inv2, "text", title="Foot of the invoice (FCFA, invented for practice)"),
        EX("Worked example 2: the buyer's entry, then the return of the crates", intro="Record invoice K101 in the books of Tabi Stores. Later the 20 crates are returned.", steps=[
            S("Journal entry on receipt", text="Debit the expense and asset accounts, credit the supplier with the total."),
            S("Check the entry balances", math=r"1\,026\,000 + 40\,000 + 205\,205 + 50\,000 = 1\,321\,205", text="Total debits equal the credit to the supplier."),
            S("When the crates are returned", text="Credit note for 50 000: Dr Supplier 50 000; Cr Returnable containers deposit 50 000. The supplier now is owed 50 000 less."),
        ]),
        CODE(_entry_buyer, "text", title="Journal entry in the books of Tabi Stores (FCFA)"),
        EX("Worked example 3: VAT payable for the month", intro="In a month a trader sells goods with net value FCFA 8 000 000 and buys goods with net value FCFA 5 200 000 (invented for practice). Find the VAT payable.", steps=[
            S("Output VAT", math=r"8\,000\,000 \times 19.25\% = 1\,540\,000"),
            S("Input VAT", math=r"5\,200\,000 \times 19.25\% = 1\,001\,000"),
            S("VAT payable", math=r"1\,540\,000 - 1\,001\,000 = 539\,000", text="The trader pays **FCFA 539 000** to the tax office."),
        ]),
        CODE(_vat_tbl, "text", title="VAT summary (FCFA)"),
        EX("Worked example 4: finding the net price from the VAT-inclusive price", intro="A customer pays FCFA 1 192 500 including VAT at 19.25%. Find the net price and the VAT.", steps=[
            S("Divide by 1.1925", math=r"1\,192\,500 \div 1.1925 = 1\,000\,000"),
            S("VAT", math=r"1\,192\,500 - 1\,000\,000 = 192\,500", text="Net price FCFA 1 000 000; VAT FCFA 192 500."),
        ]),
        MISTAKE("Taking VAT off with a simple subtraction", "To remove 19.25% from a VAT-inclusive price, divide by 1.1925. Subtracting 19.25% of the inclusive price gives the wrong answer."),
        MISTAKE("Treating VAT on purchases as an expense", "Input VAT is recoverable: debit VAT recoverable (an asset), not purchases. Only a business that cannot recover VAT treats it as part of the cost."),
        MISTAKE("Adding VAT to the container deposit by habit", "The deposit is repaid when the crates come back. In our examples it carries no VAT; follow the question if it says otherwise."),
        QUIZ("Net amount FCFA 2 000 000. VAT at 19.25% is",
             ["FCFA 385 000", "FCFA 192 500", "FCFA 2 385 000", "FCFA 1 615 000"], 0,
             "2 000 000 x 19.25% = 385 000.",
             hint="Multiply the net amount by 0.1925.",
             feedback=["", "That is the VAT on 1 000 000.", "That is the total including VAT, not the VAT.", "You subtracted the VAT from the net amount."]),
        QUIZ("A trader's output VAT is FCFA 900 000 and input VAT is FCFA 640 000. What is the VAT payable?",
             ["FCFA 1 540 000", "FCFA 260 000", "FCFA 640 000", "FCFA 900 000"], 1,
             "VAT payable = output - input = 900 000 - 640 000 = 260 000.",
             hint="Which one reduces the amount owed to the state?",
             feedback=["You added the two.", "", "That is the input VAT only.", "That is the output VAT only."]),
        PQ("A shop sells goods for FCFA 3 600 000 net of VAT. Calculate the VAT at 19.25% and the invoice total.",
           "VAT = 3 600 000 x 0.1925 = **693 000**. Total = 3 600 000 + 693 000 = **FCFA 4 293 000**."),
        PQ("Net purchases of the month: FCFA 2 400 000. Net sales: FCFA 4 000 000. VAT 19.25%. Find the VAT payable.",
           "Output VAT = 4 000 000 x 0.1925 = 770 000. Input VAT = 2 400 000 x 0.1925 = 462 000. VAT payable = 770 000 - 462 000 = **FCFA 308 000**."),
        PQ("Explain what happens to the deposit on returnable containers when they are returned.",
           "The seller issues a credit note for the deposit. The buyer's debt falls by the deposit (or the deposit is repaid in cash). It is not a sale or an expense."),
        TIP("VAT appears in Paper 1 (calculations of VAT and totals) and in Paper 2 Question 5 on trading transactions. Always show: net, VAT, total. State the rate you used. For IAS/IFRS questions the rate is given; the method is the same."),
        SUM("VAT = net amount x 19.25% (check the current rate); total = net x 1.1925.",
            "Output VAT is owed to the state; input VAT is recoverable; payable = output - input.",
            "Transport charged on the invoice bears VAT.",
            "The deposit on returnable containers is refunded by a credit note when they are returned.",
            "To remove VAT from a VAT-inclusive price, divide by 1.1925."),
    ],
))

# ------------------------------------------------------------------ 8. purchases and sales journals


def vjournal(title_name, rows):
    """rows: (date, name, ref, net). VAT and total are computed. Returns text and totals."""
    out = [f"{'Date':<6}{title_name:<14}{'Ref':<6}{'Net':>10}{'VAT':>9}{'Total':>10}"]
    tn = tv = tt = 0
    for d, nm, ref, net in rows:
        v = vat(net)
        tn += net
        tv += v
        tt += net + v
        out.append(f"{d:<6}{nm:<14}{ref:<6}{n(net):>10}{n(v):>9}{n(net + v):>10}")
    out.append("-" * 55)
    out.append(f"{'Totals':<26}{n(tn):>10}{n(tv):>9}{n(tt):>10}")
    assert tn + tv == tt
    return "\n".join(out), tn, tv, tt


_pj_rows = [("03/03", "Kamga Whsle", "K101", 800000), ("09/03", "Mbah Traders", "M45", 360000), ("15/03", "Kamga Whsle", "K118", 520000),
            ("22/03", "Nkeng Supply", "N7", 240000), ("28/03", "Mbah Traders", "M60", 400000)]
_pj, _pn, _pv, _pt = vjournal("Supplier", _pj_rows)
assert (_pn, _pv, _pt) == (2320000, 446600, 2766600)
_sup = {}
for _d, _nm, _r, _net in _pj_rows:
    _sup[_nm] = _sup.get(_nm, 0) + _net + vat(_net)
assert _sup == {"Kamga Whsle": 1574100, "Mbah Traders": 906300, "Nkeng Supply": 286200}
assert sum(_sup.values()) == _pt

_sj_rows = [("05/03", "Etoga", "201", 600000), ("12/03", "Fon", "202", 240000), ("19/03", "Ndzi", "203", 1200000), ("26/03", "Etoga", "204", 360000)]
_sj, _sn, _sv, _st = vjournal("Customer", _sj_rows)
assert (_sn, _sv, _st) == (2400000, 462000, 2862000)
_cus = {}
for _d, _nm, _r, _net in _sj_rows:
    _cus[_nm] = _cus.get(_nm, 0) + _net + vat(_net)
assert _cus == {"Etoga": 1144800, "Fon": 286200, "Ndzi": 1431000} and sum(_cus.values()) == _st

_ppost = "\n".join([
    "Totals to the general ledger:",
    f"  Dr Purchases (601)          {n(_pn):>10}",
    f"  Dr VAT recoverable (445)    {n(_pv):>10}",
    "Each invoice to the supplier's account:",
] + [f"  Cr {k:<24}{n(v):>10}" for k, v in _sup.items()] + [
    f"  Total credits to suppliers  {n(sum(_sup.values())):>10}"])
_spost = "\n".join([
    "Each invoice to the customer's account:",
] + [f"  Dr {k:<24}{n(v):>10}" for k, v in _cus.items()] + [
    "Totals to the general ledger:",
    f"  Cr Sales (701)              {n(_sn):>10}",
    f"  Cr VAT collected (443)      {n(_sv):>10}",
    f"  Total credits               {n(_sn + _sv):>10}"])
assert _pn + _pv == sum(_sup.values()) and _sn + _sv == sum(_cus.values())

LESSONS.append(lesson(
    module=M2,
    topic="Purchases and sales journals",
    title="The purchases journal and the sales journal",
    slug="acc1-purchases-and-sales-journals",
    minutes=25,
    summary="Credit purchases of goods for resale are listed in the purchases journal and credit sales in the sales journal. Each journal is totalled monthly and posted to the general ledger, while every invoice is also posted to the supplier's or customer's account.",
    objectives=[
        "Explain why businesses use books of original entry (journals)",
        "Enter credit purchases and credit sales, with VAT, in the purchases and sales journals",
        "Total and cross-check the columns of a journal",
        "Post the journals to the general ledger and to the supplier and customer accounts",
    ],
    key_concepts=["Book of original entry", "Purchases journal", "Sales journal", "Invoice number", "General ledger", "Personal ledger"],
    blocks=[
        H("Introduction"),
        T("A busy shop receives dozens of invoices every month. Writing a ledger entry for each one separately would take a long time and be easy to get wrong. So businesses first list each document in a book called a journal, in date order, and post the totals to the ledger once a month."),
        D("A **book of original entry** (or journal) is the book in which a transaction is first recorded, from a source document such as an invoice. The **purchases journal** records invoices for goods bought **on credit for resale**. The **sales journal** records invoices for goods sold **on credit**.",
          title="Definition: purchases and sales journals"),
        KEY("What does not go in these journals", "Do not mix transactions.", cards=[
            ["Cash purchases and sales", "These go to the cash book (a later module), not to these journals."],
            ["Assets on credit", "A freezer or a computer bought on credit is a fixed asset. It goes in the general journal (last lesson of this module), not in the purchases journal."],
            ["Returns", "Goods sent back are recorded in the returns journals (next lesson)."],
        ]),
        H("Layout and posting"),
        T("Each line has the date, the name of the supplier or customer, the invoice number, the **net** amount (after trade discount), the VAT, and the total. We record invoices **after trade discount**. The three money columns cross-check: net + VAT = total, line by line and in the totals."),
        EX("Worked example 1: the purchases journal", intro="Tabi Stores buys goods on credit in March. Enter the invoices and total the journal (VAT 19.25%). All figures are in FCFA and are invented for practice. 3 Mar Kamga Wholesale, invoice K101, net 800 000. 9 Mar Mbah Traders, M45, net 360 000. 15 Mar Kamga Wholesale, K118, net 520 000. 22 Mar Nkeng Supplies, N7, net 240 000. 28 Mar Mbah Traders, M60, net 400 000.", steps=[
            S("Calculate the VAT on each net amount", text="For example, 800 000 x 19.25% = 154 000; 360 000 x 19.25% = 69 300."),
            S("Fill the three columns", text="Total = net + VAT on each line."),
            S("Add the columns", math=r"\text{Net } 2\,320\,000 + \text{VAT } 446\,600 = 2\,766\,600", text="Check: 2 320 000 x 19.25% = 446 600. The columns agree."),
        ]),
        CODE(_pj, "text", title="Purchases journal, March (FCFA)"),
        EX("Worked example 2: posting the purchases journal", intro="Post the journal.", steps=[
            S("General ledger", text="Debit the Purchases account with the net total 2 320 000. Debit the VAT recoverable account with 446 600."),
            S("Supplier accounts", text="Credit each supplier's account with each invoice total. Kamga: 954 000 + 620 100 = 1 574 100. Mbah: 429 300 + 477 000 = 906 300. Nkeng: 286 200."),
            S("Check", math=r"1\,574\,100 + 906\,300 + 286\,200 = 2\,766\,600", text="Total credited to suppliers equals the journal total, and equals the debits 2 320 000 + 446 600."),
        ]),
        CODE(_ppost, "text", title="Posting the purchases journal"),
        EX("Worked example 3: the sales journal", intro="Tabi Stores sells goods on credit in March: 5 Mar Etoga, invoice 201, net 600 000; 12 Mar Fon, 202, net 240 000; 19 Mar Ndzi, 203, net 1 200 000; 26 Mar Etoga, 204, net 360 000. VAT is 19.25%. Enter, total and post.", steps=[
            S("Calculate VAT and totals", text="600 000 gives VAT 115 500; 240 000 gives 46 200; 1 200 000 gives 231 000; 360 000 gives 69 300."),
            S("Add the columns", math=r"2\,400\,000 + 462\,000 = 2\,862\,000"),
            S("Post", text="Debit each customer's account with the invoice total. Credit Sales with 2 400 000 and VAT collected with 462 000 (a liability)."),
        ]),
        CODE(_sj, "text", title="Sales journal, March (FCFA)"),
        CODE(_spost, "text", title="Posting the sales journal"),
        MISTAKE("Using the gross amount instead of the net", "Enter the amount after trade discount. The discount never appears in the ledger."),
        MISTAKE("Posting the VAT to the wrong side", "On purchases, VAT is debited (recoverable asset). On sales, VAT is credited (owed to the state). Remember the supplier or customer account gets the full invoice total."),
        MISTAKE("Entering cash sales in the sales journal", "The sales journal is for credit sales only. A cash sale is recorded in the cash book."),
        QUIZ("Which transaction is recorded in the purchases journal?",
             ["Goods bought for cash", "Goods bought on credit for resale", "A van bought on credit", "Goods returned to a supplier"], 1,
             "The purchases journal is for credit purchases of goods for resale.",
             hint="Look for 'goods', 'credit' and 'resale' together.",
             feedback=["Cash purchases go in the cash book.", "", "A van is a fixed asset: general journal.", "Returns go in the returns outwards journal."]),
        QUIZ("A sales journal has net FCFA 1 000 000 and VAT FCFA 192 500. What is posted to the debit side of the customers' accounts in total?",
             ["FCFA 1 000 000", "FCFA 192 500", "FCFA 1 192 500", "FCFA 807 500"], 2,
             "Customers owe the full invoice total: 1 000 000 + 192 500 = 1 192 500.",
             hint="Customers pay the net price and the VAT.",
             feedback=["That is the net sales only.", "That is the VAT only.", "", "You subtracted the VAT."]),
        PQ("Why is the purchases journal totalled and posted to the Purchases account only once a month, but each invoice is posted to a supplier's account?",
           "The Purchases and VAT accounts need only the totals, which saves many entries. Each supplier's account must show the individual invoices so the amount owed to that supplier is known."),
        PQ("A purchases journal has two invoices with net amounts FCFA 500 000 and FCFA 300 000. Calculate VAT at 19.25% and the total, and state the entries posted from the totals.",
           "Net total 800 000; VAT = 800 000 x 0.1925 = 154 000; total 954 000. Dr Purchases 800 000; Dr VAT recoverable 154 000; Cr suppliers 954 000 (each invoice to its supplier's account)."),
        PQ("Which two columns of a sales journal add up to the third?",
           "Net sales + VAT = invoice total."),
        TIP("Paper 2 Question 5 (trading transactions) has examined purchases and sales of goods. Show the journal with VAT, the totals, and the posting. In the IAS/IFRS approach the VAT may be called sales tax and the books may be named day books; the layout is the same."),
        SUM("The purchases journal lists credit purchases for resale; the sales journal lists credit sales.",
            "Enter net amounts after trade discount, with VAT and total columns.",
            "Totals go to the general ledger (Purchases and VAT, or Sales and VAT); each invoice total goes to the personal account.",
            "Cash transactions and fixed assets do not go in these journals."),
    ],
))

# ------------------------------------------------------------------ 9. returns journals
_rj_out = [("07/03", "Kamga Whsle", "CN12", 160000), ("20/03", "Mbah Traders", "CN03", 80000)]
_rj_o, _ron, _rov, _rot = vjournal("Supplier", _rj_out)
_rj_in = [("10/03", "Etoga", "CN1", 120000), ("27/03", "Fon", "CN2", 40000)]
_rj_i, _rin, _riv, _rit = vjournal("Customer", _rj_in)
assert (_ron, _rov, _rot) == (240000, 46200, 286200)
assert (_rin, _riv, _rit) == (160000, 30800, 190800)
_kamga = 1574100 - (160000 + vat(160000))
assert _kamga == 1383300
_kamga_acc = tacc("KAMGA WHOLESALE ACCOUNT", [("Returns (CN12)", 190800)], [("Purchases K101", 954000), ("Purchases K118", 620100)])
assert "1 383 300" in _kamga_acc

LESSONS.append(lesson(
    module=M2,
    topic="Returns journals",
    title="Returns inwards and returns outwards journals",
    slug="acc1-returns-journals",
    minutes=22,
    summary="Goods sent back by customers are listed in the returns inwards (sales returns) journal, and goods we send back to suppliers in the returns outwards (purchases returns) journal. Both are based on credit notes and include VAT.",
    objectives=[
        "Explain why goods are returned and which document supports the return",
        "Distinguish returns inwards from returns outwards",
        "Enter returns with VAT in the correct journal and total it",
        "Post the returns journals and find the net effect on a supplier or customer account",
    ],
    key_concepts=["Returns inwards", "Returns outwards", "Credit note", "Sales returns", "Purchases returns", "RRR"],
    blocks=[
        H("Introduction"),
        T("Tabi Stores receives 40 cartons of tomato paste, and 8 of them are damaged. The shop sends those 8 back. The supplier agrees and sends a paper reducing the amount owed. That paper is a credit note, and it starts the record of a return."),
        D("**Returns inwards** (sales returns) are goods sent back to us by our customers. **Returns outwards** (purchases returns) are goods we send back to our suppliers. In both cases a **credit note** supports the entry. In the SYSCOHADA plan returns are included with the RRR (rabais, remises, ristournes) accounts; many textbooks keep the names returns inwards and returns outwards. Check your textbook.",
          title="Definition: returns inwards and outwards"),
        KEY("Whose point of view?", "Same event, two different books.", cards=[
            ["We send goods back to a supplier", "Our books: **returns outwards journal**. The supplier's account is debited, because we now owe less."],
            ["A customer sends goods back to us", "Our books: **returns inwards journal**. The customer's account is credited, because they now owe less."],
        ]),
        T("The return is valued at the **net price** actually charged, after trade discount, and the VAT charged on those goods is also reversed. The returns journal has the same three money columns as the purchases and sales journals."),
        EX("Worked example 1: the returns outwards journal", intro="Tabi Stores returns damaged goods: 7 Mar to Kamga Wholesale (credit note CN12) net 160 000; 20 Mar to Mbah Traders (CN03) net 80 000. VAT 19.25%.", steps=[
            S("VAT on each return", text="160 000 x 19.25% = 30 800; 80 000 x 19.25% = 15 400."),
            S("Totals of each line", text="160 000 + 30 800 = 190 800; 80 000 + 15 400 = 95 400."),
            S("Column totals", math=r"240\,000 + 46\,200 = 286\,200"),
        ]),
        CODE(_rj_o, "text", title="Returns outwards journal, March (FCFA, invented for practice)"),
        T("Posting: debit each supplier's account with the line total (we owe less). Credit the **Returns outwards** account with the net total 240 000 and credit **VAT recoverable** with 46 200 (we recover less VAT, so the debit balance is reduced). Debits to suppliers 190 800 + 95 400 = 286 200, equal to the credits 240 000 + 46 200."),
        EX("Worked example 2: the returns inwards journal", intro="Customers return goods: 10 Mar Etoga (credit note CN1) net 120 000; 27 Mar Fon (CN2) net 40 000.", steps=[
            S("VAT on each return", text="120 000 x 19.25% = 23 100; 40 000 x 19.25% = 7 700."),
            S("Totals", math=r"160\,000 + 30\,800 = 190\,800"),
            S("Post", text="Credit each customer's account with its total (they owe less). Debit **Returns inwards** with 160 000 and debit **VAT collected** with 30 800 (we owe the state less)."),
        ]),
        CODE(_rj_i, "text", title="Returns inwards journal, March (FCFA, invented for practice)"),
        EX("Worked example 3: the net effect on a supplier's account", intro="Kamga Wholesale's account has credit entries for invoices K101 (954 000) and K118 (620 100). The credit note CN12 for 190 800 is received. What does Tabi Stores still owe Kamga?", steps=[
            S("Credit side", math=r"954\,000 + 620\,100 = 1\,574\,100"),
            S("Debit side", text="CN12 returns: 190 800."),
            S("Balance", math=r"1\,574\,100 - 190\,800 = 1\,383\,300", text="Tabi Stores owes Kamga **FCFA 1 383 300** (a credit balance)."),
        ]),
        CODE(_kamga_acc, "text", title="Supplier account after the return (FCFA)"),
        MISTAKE("Valuing the return at the gross price", "Return the goods at the price actually charged, after trade discount. If the invoice price is 160 000 net, the return is 160 000 net."),
        MISTAKE("Mixing up inwards and outwards", "Inwards = coming into our business (from customers). Outwards = going out of our business (to suppliers). Think of the direction of the goods."),
        MISTAKE("Forgetting to adjust VAT", "A return cancels the sale or purchase, so the VAT on the goods is also cancelled."),
        QUIZ("A customer returns goods to us. In which journal do we record it?",
             ["Purchases journal", "Sales journal", "Returns inwards journal", "Returns outwards journal"], 2,
             "Goods coming back from a customer are returns inwards.",
             hint="Which way do the goods move, into our business or out of it?",
             feedback=["The purchases journal records goods we buy.", "The sales journal records goods we sell.", "", "Outwards is for goods we send back to suppliers."]),
        QUIZ("Net returns outwards FCFA 400 000 with VAT 19.25%. What is the debit to the supplier's account?",
             ["FCFA 400 000", "FCFA 77 000", "FCFA 477 000", "FCFA 323 000"], 2,
             "VAT = 400 000 x 0.1925 = 77 000. Total = 477 000.",
             hint="Include the VAT that was charged on the goods.",
             feedback=["That is the net only; the supplier also charged VAT.", "That is only the VAT.", "", "You subtracted the VAT."]),
        PQ("Distinguish returns inwards from returns outwards and name the document that supports them.",
           "Returns inwards: goods sent back by customers. Returns outwards: goods we send back to suppliers. Both are supported by a credit note."),
        PQ("Tabi Stores returns goods of net value FCFA 200 000 to a supplier. Calculate VAT at 19.25% and state the entries.",
           "VAT = 38 500; total 238 500. Dr Supplier 238 500; Cr Returns outwards 200 000; Cr VAT recoverable 38 500."),
        PQ("A customer owes FCFA 715 500 (net 600 000 plus VAT 115 500) and returns goods of net value 120 000. What does the customer owe now?",
           "Return total = 120 000 + 23 100 = 143 100. Balance = 715 500 - 143 100 = **FCFA 572 400**."),
        TIP("In Paper 1, expect a question on which journal, or which account is debited or credited for a return. Say 'inwards' for customers and 'outwards' for suppliers. In IAS/IFRS wording they are 'sales returns' and 'purchases returns'."),
        SUM("Returns inwards: goods back from customers. Returns outwards: goods back to suppliers.",
            "A credit note supports each return.",
            "Value returns at the net price and reverse the VAT.",
            "Returns outwards: debit supplier, credit returns outwards and VAT recoverable. Returns inwards: credit customer, debit returns inwards and VAT collected."),
    ],
))

# ------------------------------------------------------------------ 10. general journal


def gj(rows, narration, w=24, a=11):
    """rows: (account, dr, cr)."""
    td = sum(r[1] for r in rows)
    tc = sum(r[2] for r in rows)
    assert td == tc, (td, tc)
    out = [f"{'Account':<{w}}{'Debit':>{a}}{'Credit':>{a}}"]
    for acct, d, c in rows:
        out.append(f"{acct if d else '   ' + acct:<{w}}{(n(d) if d else ''):>{a}}{(n(c) if c else ''):>{a}}")
    out.append(f"({narration})")
    return "\n".join(out)


_open = [("Premises", 10000000, 0), ("Vehicles", 3500000, 0), ("Stock of goods", 1200000, 0), ("Debtors", 800000, 0), ("Bank", 1500000, 0), ("Cash", 100000, 0),
         ("Creditors", 0, 700000), ("Bank loan", 0, 2000000), ("Capital", 0, 14400000)]
assert sum(r[1] for r in _open) == 17100000 == 2700000 + 14400000
_g1 = gj(_open, "Being opening balances at 1 January")
_comp = 480000
_compv = vat(_comp)
assert _compv == 92400 and _comp + _compv == 572400
_g2 = gj([("Equipment (computer)", _comp, 0), ("VAT recoverable on assets", _compv, 0), ("Digitech (supplier)", 0, _comp + _compv)], "Being computer bought on credit, invoice D77")
_g3 = gj([("Drawings", 40000, 0), ("Purchases", 0, 40000)], "Being goods taken by the owner for private use")
_g4 = gj([("Equipment (freezer)", 250000, 0), ("Purchases", 0, 250000)], "Being freezer wrongly debited to Purchases, now corrected")

LESSONS.append(lesson(
    module=M2,
    topic="The general journal",
    title="The general journal: opening entries, assets on credit and corrections",
    slug="acc1-general-journal",
    minutes=24,
    summary="The general journal records transactions that fit no other book: opening entries, assets bought or sold on credit, owner's drawings of goods, adjustments and corrections. Each entry shows accounts, amounts and a narration.",
    objectives=[
        "Say which transactions belong in the general journal",
        "Write a journal entry with debit lines, credit lines and a narration",
        "Prepare an opening journal entry from a list of assets and liabilities",
        "Journalise a purchase of a fixed asset on credit and a correction of an error",
    ],
    key_concepts=["General journal", "Journal entry", "Narration", "Opening entry", "Correction of an error"],
    blocks=[
        H("Introduction"),
        T("The sales journal and the purchases journal handle the daily goods. But what about the day a shop buys a computer on credit, or when the owner takes goods for the home, or when a bookkeeper finds that an amount went to the wrong account? None of these fits the other books. The general journal is the book for these 'other' transactions."),
        D("The **general journal** (journal proper) is the book of original entry for transactions that are not recorded in the special journals or the cash book. Each entry gives the date, the accounts to debit and credit, the amounts, and a **narration**: a short explanation starting with 'Being...'.",
          title="Definition: general journal"),
        KEY("What goes in the general journal", "Learn this list.", cards=[
            ["Opening entries", "The assets, liabilities and capital at the start of a business or a new year."],
            ["Fixed assets on credit", "Buying or selling equipment, vehicles or buildings on credit."],
            ["Drawings of goods", "The owner takes goods for private use."],
            ["Corrections and adjustments", "Correcting errors, writing off bad debts, depreciation and year-end adjustments (later modules)."],
        ]),
        T("The layout has the debit lines first (the account name at the left), then the credit lines indented slightly, then the narration in brackets. The total of the debit column must equal the total of the credit column."),
        EX("Worked example 1: opening entry", intro="On 1 January a trader has: premises 10 000 000, vehicles 3 500 000, stock 1 200 000, debtors 800 000, bank 1 500 000, cash 100 000. He owes creditors 700 000 and a bank loan 2 000 000. Prepare the opening journal entry. (FCFA, invented for practice.)", steps=[
            S("Add the assets", math=r"10\,000\,000 + 3\,500\,000 + 1\,200\,000 + 800\,000 + 1\,500\,000 + 100\,000 = 17\,100\,000"),
            S("Add the liabilities and find capital", math=r"17\,100\,000 - (700\,000 + 2\,000\,000) = 14\,400\,000", text="Capital is the balancing figure from the accounting equation."),
            S("Write the entry", text="Debit all assets, credit all liabilities and capital. Totals: debits 17 100 000 = credits 2 700 000 + 14 400 000."),
        ]),
        CODE(_g1, "text", title="Opening journal entry (FCFA)"),
        EX("Worked example 2: a fixed asset bought on credit", intro="The trader buys a computer on credit from Digitech: invoice D77, net price FCFA 480 000 plus VAT at 19.25%.", steps=[
            S("VAT", math=r"480\,000 \times 19.25\% = 92\,400", text="Total payable = 572 400."),
            S("Choose the accounts", text="The computer is an asset (debit). VAT on assets is recoverable (debit). The supplier of the asset is a creditor (credit)."),
            S("Check", math=r"480\,000 + 92\,400 = 572\,400", text="Debit total equals the credit."),
        ]),
        CODE(_g2, "text", title="Computer bought on credit"),
        T("Do not use the purchases journal for this entry: that journal is only for goods bought for resale."),
        EX("Worked example 3: goods taken by the owner", intro="The owner takes goods at cost FCFA 40 000 for private use.", steps=[
            S("Accounts", text="Drawings increase (debit). The goods leave the stock, so Purchases is credited."),
            S("Entry", text="Dr Drawings 40 000; Cr Purchases 40 000."),
        ]),
        CODE(_g3, "text", title="Drawings of goods"),
        EX("Worked example 4: correcting an error", intro="A freezer costing FCFA 250 000, paid in cash, was wrongly debited to the Purchases account. Correct it.", steps=[
            S("What went wrong", text="A fixed asset was recorded as an expense: an error of principle. Purchases is overstated by 250 000, Equipment is understated."),
            S("What the correction must do", text="Take it out of Purchases (credit) and put it into Equipment (debit)."),
        ]),
        CODE(_g4, "text", title="Correction of an error"),
        MISTAKE("Leaving out the narration", "Every journal entry needs a narration. It tells the reader why the entry was made, which helps auditors and teachers who mark your work."),
        MISTAKE("Using the purchases journal for equipment", "Only goods bought for resale go in the purchases journal. Equipment, vehicles and furniture on credit go in the general journal."),
        MISTAKE("Opening entries that do not balance", "Check that total debits (assets) equal total credits (liabilities plus capital). If not, capital is wrong."),
        QUIZ("Which transaction is recorded in the general journal?",
             ["Goods sold on credit to a customer", "Goods bought on credit for resale", "A delivery van bought on credit", "A cash sale"], 2,
             "A fixed asset bought on credit has no special journal, so it goes in the general journal.",
             hint="Which of these is NOT trading stock?",
             feedback=["That is the sales journal.", "That is the purchases journal.", "", "That is the cash book."]),
        QUIZ("In an opening journal entry, which accounts are credited?",
             ["Assets", "Liabilities and capital", "Expenses", "Drawings"], 1,
             "Assets are debited; liabilities and capital are credited, so the entry balances.",
             hint="Use the accounting equation: Assets = Capital + Liabilities.",
             feedback=["Assets are debited.", "", "No expenses appear in an opening entry.", "Drawings are not part of the opening balance sheet."]),
        PQ("List four kinds of transaction recorded in the general journal.",
           "Opening entries; purchase or sale of fixed assets on credit; drawings of goods; correction of errors. (Also adjustments such as depreciation and bad debts, in later modules.)"),
        PQ("Prepare the opening entry: assets cash 300 000, stock 700 000, equipment 1 500 000; liability creditors 400 000.",
           "Capital = 2 500 000 - 400 000 = 2 100 000. Dr Cash 300 000, Dr Stock 700 000, Dr Equipment 1 500 000 (total 2 500 000). Cr Creditors 400 000, Cr Capital 2 100 000 (total 2 500 000). Being opening balances."),
        PQ("A shop buys furniture on credit: net FCFA 200 000 plus VAT at 19.25%. Journalise it.",
           "VAT = 38 500; total 238 500. Dr Furniture 200 000; Dr VAT recoverable on assets 38 500; Cr Supplier 238 500. Being furniture bought on credit."),
        TIP("Examiners expect a date, correct account names, amounts in the right column and a narration. In Paper 2, journal entries are often asked for corrections and adjustments. In the IAS/IFRS approach the same journal is used; VAT may be shown as sales tax."),
        SUM("The general journal records transactions that fit no other book.",
            "Each entry: debit lines, credit lines (indented), narration beginning 'Being...'.",
            "Opening entry: debit assets, credit liabilities and capital.",
            "Fixed assets on credit and corrections of errors are recorded here, not in the purchases journal.",
            "Total debits must equal total credits."),
    ],
))

