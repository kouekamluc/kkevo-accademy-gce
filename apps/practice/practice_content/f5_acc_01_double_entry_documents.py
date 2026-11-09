"""Practice sets for Form 5 Principles of Accounts (0505): OHADA Conceptual Framework & Double Entry, and
Commercial Documents & Books of Original Entry (one set per lesson). All FCFA figures are invented for practice."""

from .dsl import *  # noqa: F403

COURSE = ("principles-of-accounts", "form-5")

M1 = "OHADA Conceptual Framework & Double Entry"
M2 = "Commercial Documents & Books of Original Entry"


def n(x):
    return f"{x:,}".replace(",", " ")


def vat(net):
    v, r = divmod(net * 1925, 10000)
    assert r == 0, net
    return v


def Q(prompt, correct, wrongs, pos, step, hint, concept, skill="Concept", math="", feedback=""):
    """4-option MC. `wrongs` = 3 (text, why) pairs; the correct option is inserted at index `pos` (0-3)."""
    assert len(wrongs) == 3 and 0 <= pos <= 3 and len(concept) <= 80
    opts = list(wrongs)
    opts.insert(pos, (correct, ""))
    choices = [C(t, correct=(i == pos), why=w) for i, (t, w) in enumerate(opts)]
    return MC(prompt, choices, [S("Reasoning", math=math, text=step)], concept=concept, skill=skill, hint=hint, feedback=feedback)


def N(prompt, answer, step, hint, concept, skill="Calculation", math="", unit="FCFA", feedback=""):
    assert len(concept) <= 80
    return NUM(prompt, answer, [S("Working", math=math, text=step)], concept=concept, skill=skill, hint=hint, unit=unit, feedback=feedback)


SETS = []

# ------------------------------------------------------------------ 1 concepts
assert min(250000, 210000) == 210000
SETS.append(practice_set(
    module=M1, topic="Accounting concepts and conventions",
    title="Accounting concepts: check your understanding",
    lesson="acc1-concepts-and-conventions",
    questions=[
        Q("A shop owner takes goods from the shop for use at home. Which concept requires this to be treated as drawings and not as a business expense?",
          "Business entity",
          [("Going concern", "Going concern is about the business continuing to operate."), ("Materiality", "Materiality concerns whether an item is large enough to matter."), ("Consistency", "Consistency is about using the same methods each year.")],
          0, "The owner and the business are separate in accounting. Anything the owner takes out is drawings.", "Which concept separates the owner from the business?", "Business entity", "Concept"),
        Q("A delivery van was bought for FCFA 6 500 000. A dealer says it could now be sold for FCFA 7 000 000. The van is recorded at",
          "FCFA 6 500 000 (cost, less depreciation later)",
          [("FCFA 7 000 000", "Historical cost does not use opinions on market value."), ("FCFA 500 000", "That is the difference between the two prices, not the value of the van."), ("FCFA 13 500 000", "Adding the two figures has no meaning.")],
          2, "Under the historical cost concept an asset is recorded at what it cost when bought.", "Which price was actually paid?", "Historical cost", "Concept"),
        Q("Which concept says that Madame Ngo should not include the skill of her best salesperson as an asset in her accounts?",
          "Money measurement",
          [("Duality", "Duality says every transaction has two effects."), ("Prudence", "Prudence is about avoiding overstated profit."), ("Going concern", "Going concern is about continuity.")],
          1, "Only things measurable in money are recorded. The skill of a person cannot be measured reliably in francs.", "Which concept says only facts measured in money are recorded?", "Money measurement", "Concept"),
        N("At the year end a trader's goods cost FCFA 250 000 but could only be sold for FCFA 210 000 net of selling costs. At what value, in FCFA, should the stock be shown?",
          210000, "Prudence: stock is valued at the lower of cost and net realisable value. Lower of 250 000 and 210 000 is 210 000.",
          "Choose the smaller of the two figures.", "Prudence (lower of cost and NRV)", "Application", math=r"\min(250\,000,\ 210\,000) = 210\,000"),
        Q("A trader sells goods on 28 December. The customer pays on 6 January. In which year is the sale recorded?",
          "The year ending in December, by the accruals concept",
          [("The year of payment, when cash arrives", "The accruals concept records income when it is earned, not when cash moves."), ("Both years, split equally", "A sale is not split between years."), ("It is not recorded until the customer has a receipt", "A receipt is not needed to record a sale.")],
          3, "Under accruals (independence of financial years) the sale belongs to the year in which the goods were delivered.", "When were the goods delivered?", "Accruals", "Application"),
        Q("A bookkeeper uses straight-line depreciation one year and a different method the next year without a reason. Which concept is broken?",
          "Consistency (permanence of methods)",
          [("Going concern", "That concerns the future of the business."), ("Business entity", "That concerns the owner and the business being separate."), ("Money measurement", "Money measurement concerns what can be recorded.")],
          0, "Using different methods each year makes years impossible to compare. Consistency means keeping the same method.", "What does consistency require year after year?", "Consistency", "Reasoning"),
        Q("A business stops buying new stock because its owner has decided to close down next month. Which accounting concept can no longer be assumed?",
          "Going concern (continuity)",
          [("Duality", "Duality is not affected by closing."), ("Historical cost", "Cost is still used for recording purchases."), ("Materiality", "Materiality is about size of items.")],
          2, "Going concern assumes the business will continue. When closure is planned, assets must be valued as in a sale.", "Which concept assumes the business will keep operating?", "Going concern", "Reasoning"),
        Q("A box of pencils costing FCFA 2 500 lasts two years, but the bookkeeper writes it off as an expense in the year of purchase. Which concept justifies this?",
          "Materiality",
          [("Prudence", "Prudence is about not overstating profit, but here the reason is the tiny size."), ("Accruals", "Accruals would spread the cost over its life."), ("Duality", "Duality says every entry has a debit and a credit.")],
          1, "The amount is too small to matter, so it is treated simply. This is the materiality concept.", "Why would nobody spread a FCFA 2 500 cost over two years?", "Materiality", "Application"),
    ]))

# ------------------------------------------------------------------ 2 chart of accounts
SETS.append(practice_set(
    module=M1, topic="The SYSCOHADA chart of accounts",
    title="SYSCOHADA classes: check your understanding",
    lesson="acc1-syscohada-chart-of-accounts",
    questions=[
        Q("In the SYSCOHADA chart, fixed assets such as buildings and vehicles are in which class?",
          "Class 2",
          [("Class 1", "Class 1 is long-term resources such as capital and loans."), ("Class 3", "Class 3 is stocks."), ("Class 5", "Class 5 is bank and cash.")],
          0, "Class 2 holds fixed assets.", "Which class comes right after resources?", "SYSCOHADA classes", "Recall"),
        Q("An account whose number begins with 6 is normally an",
          "expense account with a debit balance",
          [("income account with a credit balance", "Income is class 7."), ("asset account with a debit balance", "Assets are classes 2, 3 and 5."), ("expense account with a credit balance", "Expenses have a debit balance.")],
          1, "Class 6 holds expenses of ordinary activities, normally debit.", "What does class 6 contain?", "SYSCOHADA classes", "Recall"),
        Q("Sales of goods are recorded in account 701, which belongs to",
          "class 7, with a credit balance",
          [("class 6, with a debit balance", "The number begins with 7, not 6."), ("class 7, with a debit balance", "Income has a credit balance."), ("class 1, with a credit balance", "Class 1 is resources, not sales.")],
          2, "The first digit gives the class; class 7 is income with a normal credit balance.", "Read the first digit.", "SYSCOHADA classes", "Recall"),
        Q("Which account normally has a credit balance?",
          "401 Suppliers",
          [("411 Customers", "Customers owe us money: debit."), ("571 Cash in hand", "Cash is an asset: debit."), ("601 Purchases", "Purchases are an expense: debit.")],
          3, "Suppliers are owed money by the business, a liability with a credit balance.", "Which one is owed to someone else?", "Normal balances", "Concept"),
        Q("Bank balances and cash in hand are found in class",
          "5",
          [("1", "Class 1 holds capital and long-term loans."), ("3", "Class 3 holds stocks."), ("4", "Class 4 holds third parties such as customers and suppliers.")],
          0, "Class 5 is the treasury class: bank and cash.", "Which class holds money that can be spent at once?", "SYSCOHADA classes", "Recall"),
        Q("A bank gives a business a ten-year loan. In which class would the loan normally be recorded?",
          "Class 1, long-term resources",
          [("Class 5, cash and bank", "The loan is not money available now; it is a resource owed back over time."), ("Class 6, expenses", "Only the interest is an expense; the loan itself is not."), ("Class 7, income", "A loan is not income.")],
          1, "Long-term loans are resources of the business, in class 1.", "Is a ten-year loan a short-term or a long-term resource?", "SYSCOHADA classes", "Application"),
        N("Income from the ordinary activity is found in the class numbered ...", 7, "Class 7 holds income of ordinary activities.", "It comes after class 6 (expenses).", "SYSCOHADA classes", "Recall", unit=""),
        Q("Which list contains only accounts with normal debit balances?",
          "Equipment, Purchases, Cash",
          [("Sales, Capital, Suppliers", "These are all normally credit balances."), ("Equipment, Sales, Wages", "Sales is normally credit."), ("Purchases, Capital, Cash", "Capital is normally credit.")],
          2, "Equipment (asset), Purchases (expense) and Cash (asset) are all debit accounts.", "Look for the list with no income, capital or liability.", "Normal balances", "Reasoning"),
    ]))

# ------------------------------------------------------------------ 3 accounting equation
_eq1 = 6500000 - 1800000
assert _eq1 == 4700000
_eq2 = 5000000 - 3200000
assert _eq2 == 1800000
_eq3 = 2500000 + 900000 - 400000
assert _eq3 == 3000000
_a8 = 8000000 + 1200000 - 700000
assert _a8 == 8500000 and 5000000 + 3000000 + 500000 == 8500000
SETS.append(practice_set(
    module=M1, topic="The accounting equation",
    title="The accounting equation: check your understanding",
    lesson="acc1-accounting-equation",
    questions=[
        Q("Which is the accounting equation?",
          "Assets = Capital + Liabilities",
          [("Capital = Assets + Liabilities", "Capital is what remains after liabilities are deducted."), ("Liabilities = Assets + Capital", "Liabilities are the outsiders' share of the assets."), ("Assets = Capital - Liabilities", "Liabilities are added on the right-hand side, not subtracted.")],
          2, "The assets are financed by the owner (capital) and outsiders (liabilities).", "Who finances the assets?", "Accounting equation", "Recall"),
        N("A business has assets of FCFA 6 500 000 and liabilities of FCFA 1 800 000. What is the capital in FCFA?",
          4700000, "Capital = Assets - Liabilities = 6 500 000 - 1 800 000 = 4 700 000.", "Rearrange Assets = Capital + Liabilities.", "Finding capital", math=r"6\,500\,000 - 1\,800\,000 = 4\,700\,000"),
        Q("A bank loan received by a business is a",
          "liability",
          [("asset only", "The cash received is an asset, but the loan itself is a liability."), ("part of capital", "Capital is the owner's money, not a loan."), ("expense", "A loan is not a cost; only interest is.")],
          1, "A loan must be repaid to the bank, so it is owed to outsiders: a liability.", "Who is owed the money?", "Assets, liabilities, capital", "Concept"),
        Q("Goods are bought on credit for FCFA 400 000. What happens to the equation?",
          "Assets and liabilities both rise by 400 000",
          [("Assets rise and capital rises", "Capital is unchanged by buying goods."), ("Only assets rise", "Creditors, a liability, also rise."), ("Liabilities rise and assets fall", "Stock, an asset, rises.")],
          3, "Stock (an asset) rises and creditors (a liability) rise by the same amount.", "What do we have more of and what do we owe more of?", "Effect of transactions", "Concept"),
        Q("A trader pays a supplier FCFA 150 000 in cash. The effect on the equation is that",
          "assets and liabilities both fall by 150 000",
          [("assets rise and liabilities fall", "Cash falls, so assets fall."), ("capital falls by 150 000", "Paying a debt does not reduce capital."), ("only liabilities fall", "Cash, an asset, also falls.")],
          0, "Cash falls and creditors fall by the same amount.", "What do we have less of and what do we owe less of?", "Effect of transactions", "Concept"),
        N("Opening capital is FCFA 2 500 000. The year's profit is FCFA 900 000 and drawings are FCFA 400 000. Find closing capital in FCFA.",
          3000000, "Closing capital = opening capital + profit - drawings = 2 500 000 + 900 000 - 400 000 = 3 000 000.", "Profit adds to capital; drawings reduce it.", "Capital, profit and drawings", math=r"2\,500\,000 + 900\,000 - 400\,000 = 3\,000\,000"),
        Q("The owner takes FCFA 100 000 cash from the business for private use. What happens?",
          "Assets fall and capital falls by 100 000",
          [("Assets fall and liabilities fall", "No liability is paid."), ("Assets rise and capital rises", "Cash has left the business."), ("Nothing changes", "Cash and capital both fall.")],
          1, "Cash (an asset) falls and the owner's capital falls: drawings.", "Where did the cash go and who does it belong to?", "Drawings", "Concept"),
        Q("A business has assets FCFA 8 000 000, capital FCFA 5 000 000 and liabilities FCFA 3 000 000. It buys a van for FCFA 1 200 000, paying FCFA 700 000 in cash and the rest on credit. What are the total assets afterwards?",
          "FCFA 8 500 000",
          [("FCFA 9 200 000", "You forgot that FCFA 700 000 of cash left."), ("FCFA 7 300 000", "Assets did not fall; the van was added."), ("FCFA 8 000 000", "The van adds more to assets than the cash paid takes away.")],
          2, "Assets rise by the van 1 200 000 and fall by cash 700 000, a net rise of 500 000: 8 500 000. Liabilities rise to 3 500 000, so 5 000 000 + 3 500 000 = 8 500 000.", "Add the van, subtract the cash paid.", "Effect of transactions", "Reasoning",
          math=r"8\,000\,000 + 1\,200\,000 - 700\,000 = 8\,500\,000"),
    ]))

# ------------------------------------------------------------------ 4a double entry rules
SETS.append(practice_set(
    module=M1, topic="Double entry and ledger posting",
    title="Debit and credit rules: check your understanding",
    lesson="acc1-double-entry-rules",
    questions=[
        Q("Which accounts are increased by a debit entry?",
          "Assets, expenses and drawings",
          [("Liabilities, capital and income", "These increase on the credit side."), ("Assets, capital and income", "Capital and income increase on the credit side."), ("Liabilities, expenses and drawings", "Liabilities increase on the credit side.")],
          0, "Remember DEA: Drawings, Expenses, Assets are debited when they increase.", "Which three are 'DEA'?", "Debit and credit rules", "Recall"),
        Q("Goods are sold for cash FCFA 90 000. The correct entry is",
          "Dr Cash 90 000, Cr Sales 90 000",
          [("Dr Sales 90 000, Cr Cash 90 000", "Cash increases (debit) and income increases (credit)."), ("Dr Cash 90 000, Cr Purchases 90 000", "Purchases is not involved in a sale."), ("Dr Capital 90 000, Cr Cash 90 000", "Capital is unchanged by the sale itself.")],
          1, "Cash (asset) rises: debit. Sales (income) rise: credit.", "What increases: cash or sales, and what are their types?", "Debit and credit rules", "Application"),
        Q("Goods for resale worth FCFA 500 000 are bought on credit from Fotso. The entry is",
          "Dr Purchases 500 000, Cr Fotso (creditor) 500 000",
          [("Dr Fotso 500 000, Cr Purchases 500 000", "That would reduce the debt."), ("Dr Purchases 500 000, Cr Cash 500 000", "No cash was paid."), ("Dr Cash 500 000, Cr Fotso 500 000", "No cash was received.")],
          2, "Purchases (expense) rise: debit. The liability to Fotso rises: credit.", "Is cash involved?", "Debit and credit rules", "Application"),
        Q("The owner pays FCFA 600 000 of her own equipment into the business. The entry is",
          "Dr Equipment 600 000, Cr Capital 600 000",
          [("Dr Capital 600 000, Cr Equipment 600 000", "Capital increases, so it is credited."), ("Dr Equipment 600 000, Cr Drawings 600 000", "Drawings is a debit account for money taken out."), ("Dr Cash 600 000, Cr Capital 600 000", "No cash was paid in.")],
          3, "Equipment (asset) rises: debit. Owner's capital rises: credit.", "What did the owner put in, and what does the business owe her?", "Debit and credit rules", "Application"),
        Q("The business pays wages of FCFA 70 000 in cash. Which account is credited?",
          "Cash",
          [("Wages", "Wages is an expense and is debited."), ("Capital", "Capital is not changed by this single entry."), ("Creditors", "Nothing is owed here: it is a cash payment.")],
          0, "Wages (expense) are debited and cash (asset) falls, so it is credited.", "Which asset leaves the business?", "Debit and credit rules", "Application"),
        Q("Customer Etoga pays FCFA 200 000 of the amount he owes, in cash. The entry is",
          "Dr Cash 200 000, Cr Etoga 200 000",
          [("Dr Etoga 200 000, Cr Cash 200 000", "That would mean we paid him."), ("Dr Cash 200 000, Cr Sales 200 000", "The sale was recorded when the goods were delivered."), ("Dr Sales 200 000, Cr Etoga 200 000", "Sales are not changed by the payment.")],
          1, "Cash rises: debit. The debtor owes less: credit Etoga.", "Which asset rises and which asset falls?", "Debit and credit rules", "Application"),
        N("Three entries are made: FCFA 200 000, FCFA 150 000 and FCFA 90 000, each with one debit and one equal credit. What is the total of all the debits, in FCFA?",
          440000, "Debits equal the sum of the three amounts: 200 000 + 150 000 + 90 000 = 440 000.", "Each entry has one debit of the same size as its amount.", "Total debits equal credits", math=r"200\,000 + 150\,000 + 90\,000 = 440\,000"),
        Q("A student writes: Dr Rent 80 000, Cr Capital 80 000 for rent paid by bank transfer. What is the correct entry?",
          "Dr Rent 80 000, Cr Bank 80 000",
          [("Dr Bank 80 000, Cr Rent 80 000", "That would be rent received."), ("Dr Capital 80 000, Cr Rent 80 000", "Capital is not involved in paying a bill."), ("Dr Rent 80 000, Cr Sales 80 000", "Sales is not involved.")],
          2, "Rent (expense) rises: debit. Bank (asset) falls: credit. Capital changes only through profit and drawings.", "Where did the money come from?", "Debit and credit rules", "Reasoning"),
    ]))

# ------------------------------------------------------------------ 4b ledger posting
_b2 = 1200000 - 750000
_b6 = (5000000 + 1200000) - (2400000 + 900000 + 150000)
assert (_b2, _b6) == (450000, 2750000)
assert 900000 - 500000 == 400000 and 700000 - 250000 == 450000
SETS.append(practice_set(
    module=M1, topic="Double entry and ledger posting",
    title="Posting and balancing accounts: check your understanding",
    lesson="acc1-ledger-posting-and-balancing",
    questions=[
        Q("In the details column of the cash account, a debit posting shows",
          "the name of the account that was credited",
          [("the name of the cash account itself", "The details column always names the other account."), ("the date of the invoice only", "The date has its own column."), ("the balance of the account", "The balance is shown only when the account is balanced.")],
          0, "Each posting shows the other account of the entry so the trail can be followed.", "Which account is on the opposite side of the entry?", "Posting", "Recall"),
        N("The debit side of an account totals FCFA 1 200 000 and the credit side FCFA 750 000. What is the balance, in FCFA?",
          450000, "The difference is 1 200 000 - 750 000 = 450 000, a debit balance.", "Subtract the smaller total from the bigger.", "Balancing an account", math=r"1\,200\,000 - 750\,000 = 450\,000"),
        Q("When an account is balanced and the debit side is bigger, the balance c/d is written on",
          "the credit side",
          [("the debit side", "That is where the balance b/d is brought down."), ("both sides", "Only one side gets the c/d line."), ("neither side; it is only noted in the margin", "It is written on the smaller side to make the totals equal.")],
          1, "The balance c/d goes on the smaller (credit) side to make both sides equal. The balance b/d is then written under the total on the debit side.", "Which side is the smaller one?", "Balancing an account", "Concept"),
        Q("A customer's account shows debits of FCFA 900 000 and credits of FCFA 500 000. The balance is",
          "a debit balance of FCFA 400 000: the customer owes us",
          [("a credit balance of FCFA 400 000: we owe the customer", "The debit side is bigger, so it is a debit balance."), ("a debit balance of FCFA 1 400 000", "You added the two sides."), ("a credit balance of FCFA 900 000", "That is not the difference of the two sides.")],
          2, "900 000 - 500 000 = 400 000, with the debit side bigger.", "Which side is bigger?", "Customer accounts", "Application"),
        Q("A supplier's account shows credits of FCFA 700 000 and debits of FCFA 250 000. The balance is",
          "a credit balance of FCFA 450 000, a liability",
          [("a debit balance of FCFA 450 000, an asset", "The credit side is bigger."), ("a credit balance of FCFA 950 000", "You added the two sides."), ("a credit balance of FCFA 250 000", "That is the debit total.")],
          0, "700 000 - 250 000 = 450 000, with the credit side bigger: we owe the supplier.", "Which side is bigger?", "Supplier accounts", "Application"),
        N("A cash account has debits of FCFA 5 000 000 (capital) and FCFA 1 200 000 (sales) and credits of FCFA 2 400 000, 900 000 and 150 000. What is the closing balance, in FCFA?",
          2750000, "Debits 6 200 000; credits 3 450 000; the difference is 2 750 000 (debit).", "Add each side first.", "Balancing the cash account", math=r"6\,200\,000 - 3\,450\,000 = 2\,750\,000"),
        Q("Goods are bought on credit from Mbah. To post the entry, we",
          "debit the Purchases account and credit Mbah's account",
          [("credit the Purchases account and debit Mbah's account", "That would be a return of goods."), ("debit both accounts", "One account is debited and the other credited."), ("credit the Purchases account and the Cash account", "No cash is paid on credit purchases.")],
          1, "Purchases (expense) rise: debit; the debt to Mbah rises: credit.", "Which account is the expense?", "Posting", "Application"),
        Q("After posting, a cash account shows total debits of FCFA 840 000 and total credits of FCFA 960 000. What does this suggest?",
          "There is probably an error, because cash cannot be less than zero",
          [("The business has FCFA 120 000 of cash", "The credit side is bigger, which would mean negative cash."), ("The business made a profit of FCFA 120 000", "Profit is not shown in the cash account."), ("The account must be re-opened with the debit side doubled", "Never adjust totals to force a result.")],
          2, "Cash paid out cannot exceed cash received, so a credit balance on the cash account signals a posting error.", "Can a business spend more cash than it has received?", "Balancing the cash account", "Interpretation"),
    ]))

# ------------------------------------------------------------------ 5 trial balance
_tdeb = 2090000 + 800000 + 500000 + 100000 + 60000
assert _tdeb == 3550000
assert 3000000 + 350000 + 200000 == 3550000
_need = 4300000 - 2150000
assert _need == 2150000
SETS.append(practice_set(
    module=M1, topic="The trial balance",
    title="The trial balance: check your understanding",
    lesson="acc1-trial-balance",
    questions=[
        Q("The main purpose of a trial balance is to",
          "check that total debits equal total credits",
          [("find the profit of the business", "Profit is found in the income statement."), ("show the value of the stock", "Stock is found by counting at the year end."), ("prove that the books contain no errors", "Some errors do not affect the totals.")],
          0, "A trial balance tests arithmetical accuracy of double entry.", "What does double entry guarantee about the two columns?", "Purpose of a trial balance", "Recall"),
        Q("In which column of the trial balance is the Sales balance placed?",
          "Credit",
          [("Debit", "Sales is income, which has a credit balance."), ("Either; it does not matter", "The column must follow the nature of the account."), ("It is not included", "All accounts with balances are included.")],
          1, "Sales is income and has a credit balance.", "Is sales an asset or an income?", "Trial balance columns", "Recall"),
        N("A trial balance has these debit balances: cash 2 090 000, equipment 800 000, purchases 500 000, drawings 100 000 and rent 60 000. What is the debit total in FCFA?",
          3550000, "2 090 000 + 800 000 + 500 000 + 100 000 + 60 000 = 3 550 000.", "Add all five.", "Totalling a trial balance", math=r"2\,090\,000 + 800\,000 + 500\,000 + 100\,000 + 60\,000 = 3\,550\,000"),
        Q("Drawings appear in the trial balance in the",
          "debit column",
          [("credit column", "Drawings reduce capital and are a debit balance."), ("credit column, with capital", "They are kept separate from capital and are debit."), ("neither; drawings are not recorded", "Drawings are recorded in their own account.")],
          2, "Drawings are debit balances.", "Do drawings increase or decrease capital?", "Trial balance columns", "Concept"),
        Q("Which error is NOT shown by a trial balance whose totals agree?",
          "A sale completely left out of the books",
          [("An entry debited with FCFA 54 000 and credited with FCFA 45 000", "The totals then differ, so the error is shown."), ("A debit posted with no matching credit", "The totals then differ."), ("An addition error in a ledger balance", "The totals then differ.")],
          3, "If both sides of an entry are omitted, debits and credits are still equal, so the trial balance agrees.", "Does an omitted entry change the equality of the totals?", "Errors a trial balance cannot find", "Concept"),
        Q("The credit total of a trial balance is FCFA 27 000 higher than the debit total. Which error is a likely cause?",
          "Two digits of a debit figure were swapped when copying",
          [("An asset was recorded in the wrong asset account", "That would not change the totals."), ("The same sale was omitted from both sides", "That would not change the totals."), ("Two errors of equal size on opposite sides", "That would not change the totals (compensating).")],
          0, "A difference divisible by 9 (27 000 / 9 = 3 000) often points to a transposition error in a figure.", "Is 27 000 divisible by 9?", "Transposition errors", "Reasoning"),
        N("The trial balance debit total is FCFA 4 300 000. The credit balances are capital (not yet known), sales 1 400 000 and creditors 750 000. What must the capital balance be, in FCFA, for the totals to agree?",
          2150000, "Credits excluding capital = 1 400 000 + 750 000 = 2 150 000. Capital = 4 300 000 - 2 150 000 = 2 150 000.", "Find what is missing from the credit column.", "Totalling a trial balance", skill="Reasoning", math=r"4\,300\,000 - (1\,400\,000 + 750\,000) = 2\,150\,000"),
        Q("A trial balance does not agree. A bookkeeper adds a made-up figure to the smaller column to make it agree. This is",
          "wrong, because the cause of the difference must be found",
          [("correct, because the totals are now equal", "A forced total hides the error."), ("correct if the figure is small", "Even small errors must be traced."), ("wrong only if the difference is more than FCFA 10 000", "No amount may be forced; use a suspense account and trace the error.")],
          1, "An agreed trial balance is only useful if the books are really in balance. Differences are traced; if they cannot be found at once they go to a suspense account.", "What would a forced figure hide?", "Correcting a trial balance", "Reasoning"),
    ]))

# ------------------------------------------------------------------ 6 invoices and discounts
_n2 = 800000 - 800000 * 15 // 100
assert _n2 == 680000 and 800000 * 15 % 100 == 0
_f4 = 680000 * 3 // 100
assert _f4 == 20400 and 680000 * 3 % 100 == 0
assert 680000 - _f4 == 659600
assert 500000 * 4 // 100 == 20000
SETS.append(practice_set(
    module=M2, topic="Invoices, trade discount and financial discount",
    title="Invoices and discounts: check your understanding",
    lesson="acc1-invoices-and-discounts",
    questions=[
        Q("Who prepares a sales invoice?",
          "The seller",
          [("The buyer", "A buyer sends an order, not the invoice."), ("The bank", "Banks issue statements, not invoices."), ("The tax office", "The tax office does not prepare invoices.")],
          0, "The seller prepares the invoice; the buyer keeps it as a purchase invoice.", "Who sells the goods?", "Invoices", "Recall"),
        Q("Trade discount is",
          "deducted on the invoice and not recorded in the ledger",
          [("recorded as discount allowed", "That is financial discount."), ("given only for early payment", "That is financial discount."), ("recorded as an expense of the buyer", "The buyer records only the net amount.")],
          1, "Trade discount only reduces the invoice value. Only the net amount is entered.", "Does the discount depend on when the customer pays?", "Trade discount", "Concept"),
        N("An invoice lists goods at FCFA 800 000 with 15% trade discount. What is the net commercial amount, in FCFA?",
          680000, "Discount = 800 000 x 15% = 120 000. Net = 800 000 - 120 000 = 680 000.", "Find the discount first, then subtract.", "Trade discount", math=r"800\,000 - 15\% \times 800\,000 = 680\,000"),
        Q("Financial discount is calculated on",
          "the net amount after trade discount",
          [("the gross amount before trade discount", "Trade discount is deducted first."), ("the VAT only", "VAT is not the base."), ("the cash discount received last month", "Each invoice is treated separately.")],
          2, "Trade discount is deducted first; financial discount is then worked out on the net commercial amount.", "Which amount does the buyer really owe?", "Financial discount", "Concept"),
        N("The net amount of an invoice is FCFA 680 000. A 3% financial discount is allowed for payment within 10 days. What is the discount, in FCFA?",
          20400, "680 000 x 3% = 20 400.", "Multiply by 3 and divide by 100.", "Financial discount", math=r"680\,000 \times 0.03 = 20\,400"),
        Q("A customer pays the invoice above (net FCFA 680 000, 3% discount) on day 6. How much cash does the seller receive?",
          "FCFA 659 600",
          [("FCFA 680 000", "The discount applies because he paid within the period."), ("FCFA 700 400", "You added the discount."), ("FCFA 20 400", "That is the discount, not the cash received.")],
          3, "680 000 - 20 400 = 659 600.", "Subtract the discount from the net amount.", "Financial discount", "Application", math=r"680\,000 - 20\,400 = 659\,600"),
        Q("In the seller's books, a financial discount given to a customer is recorded as",
          "discount allowed, an expense",
          [("discount received, an income", "That is the buyer's account."), ("trade discount, a reduction of sales", "Trade discount is not recorded."), ("a rebate of capital", "Capital is not affected.")],
          0, "The seller loses income by giving the discount: discount allowed (expense). The buyer records discount received (income).", "Is the seller gaining or losing?", "Recording discounts", "Concept"),
        Q("A supplier gives an end-of-year bonus of 4% on total purchases of FCFA 500 000 for the year. In OHADA terms this bonus is a",
          "ristourne, FCFA 20 000",
          [("rabais for defects, FCFA 20 000", "A rabais is for defects or poor quality."), ("remise for quantity, FCFA 20 000", "A remise is a reduction given at the time of an order or sale."), ("ristourne, FCFA 120 000", "4% of 500 000 is 20 000, not 120 000.")],
          1, "A ristourne is a period-end bonus on total purchases. 500 000 x 4% = 20 000.", "When is a ristourne given?", "Rabais, remise, ristourne", "Application", math=r"500\,000 \times 4\% = 20\,000"),
    ]))

# ------------------------------------------------------------------ 7 VAT
_v1 = vat(600000)
assert _v1 == 115500
assert 400000 + vat(400000) == 477000
_out = vat(3000000)
_in = vat(1600000)
assert (_out, _in, _out - _in) == (577500, 308000, 269500)
assert vat(20000) == 3850
assert vat(500000) == 96250 and 500000 + 96250 == 596250
_g = 800000 + 40000
assert vat(_g) == 161700 and _g + 161700 + 30000 == 1031700
SETS.append(practice_set(
    module=M2, topic="VAT, transport and returnable containers",
    title="VAT, transport and containers: check your understanding",
    lesson="acc1-vat-transport-containers",
    questions=[
        N("Calculate the VAT at 19.25% on a net amount of FCFA 600 000, in FCFA.",
          115500, "600 000 x 19.25% = 115 500.", "Multiply the net amount by 0.1925.", "Calculating VAT", math=r"600\,000 \times 0.1925 = 115\,500"),
        Q("The total of an invoice with net amount FCFA 400 000, VAT at 19.25%, is",
          "FCFA 477 000",
          [("FCFA 77 000", "That is only the VAT."), ("FCFA 400 000", "That is the net amount."), ("FCFA 323 000", "You subtracted the VAT.")],
          0, "VAT = 400 000 x 0.1925 = 77 000. Total = 477 000.", "Add the VAT to the net amount.", "Calculating VAT", "Calculation", math=r"400\,000 \times 1.1925 = 477\,000"),
        Q("VAT paid to suppliers on goods bought for resale is, to the buyer,",
          "an asset (VAT recoverable)",
          [("an expense of purchases", "Input VAT is recoverable, not a cost."), ("a liability", "VAT collected on sales is the liability."), ("income", "VAT recoverable is not income.")],
          1, "Input VAT can be deducted from output VAT, so it is an asset.", "Can the business get this VAT back?", "Input and output VAT", "Concept"),
        N("In a month, net sales are FCFA 3 000 000 and net purchases are FCFA 1 600 000. VAT is 19.25%. How much VAT is payable to the tax office, in FCFA?",
          269500, "Output VAT 3 000 000 x 0.1925 = 577 500. Input VAT 1 600 000 x 0.1925 = 308 000. Payable = 577 500 - 308 000 = 269 500.", "Output VAT minus input VAT.", "VAT payable", skill="Application", math=r"577\,500 - 308\,000 = 269\,500"),
        Q("An invoice charges FCFA 20 000 for transport, which bears VAT at 19.25%. The VAT on the transport is",
          "FCFA 3 850",
          [("FCFA 385", "The decimal is misplaced."), ("FCFA 38 500", "The decimal is misplaced the other way."), ("nothing; transport carries no VAT", "In our examples transport on the invoice bears VAT.")],
          2, "20 000 x 0.1925 = 3 850.", "Multiply by 0.1925.", "Transport and VAT", "Calculation", math=r"20\,000 \times 0.1925 = 3\,850"),
        Q("Returnable crates are sent with a deposit of FCFA 30 000. When the crates are returned, the buyer",
          "is credited with FCFA 30 000 by a credit note",
          [("pays a further FCFA 30 000", "A returned crate earns a refund, not a charge."), ("pays VAT on the deposit", "A deposit is not a sale."), ("loses the deposit", "The deposit is refunded when the crates come back.")],
          3, "The deposit is refundable, so a credit note is issued on return.", "Is the deposit a sale or a refundable amount?", "Returnable containers", "Concept"),
        N("A customer pays FCFA 596 250 including VAT at 19.25%. What was the net price, in FCFA?",
          500000, "Net price = 596 250 / 1.1925 = 500 000.", "Divide by 1.1925, not subtract 19.25%.", "VAT-inclusive prices", skill="Reasoning", math=r"596\,250 \div 1.1925 = 500\,000"),
        Q("An invoice has goods net FCFA 800 000, transport FCFA 40 000 (both bear VAT at 19.25%) and a returnable container deposit of FCFA 30 000. What is the total to pay?",
          "FCFA 1 031 700",
          [("FCFA 1 001 700", "You did not add the deposit."), ("FCFA 870 000", "You added the deposit but omitted the VAT."), ("FCFA 1 231 700", "You added an extra 200 000; recompute 19.25% of 840 000.")],
          1, "Net 800 000 + 40 000 = 840 000. VAT = 161 700. Total = 840 000 + 161 700 + 30 000 = 1 031 700.", "Add the VAT to goods and transport, then add the deposit.", "Total invoice with VAT", "Application", math=r"840\,000 + 161\,700 + 30\,000 = 1\,031\,700"),
    ]))

# ------------------------------------------------------------------ 8 purchases and sales journals
assert vat(1200000) == 231000
_nets = [400000, 800000, 200000]
_tn = sum(_nets)
_tv = sum(vat(x) for x in _nets)
assert (_tn, _tv, _tn + _tv, vat(_tn)) == (1400000, 269500, 1669500, 269500)
assert vat(2000000) == 385000
SETS.append(practice_set(
    module=M2, topic="Purchases and sales journals",
    title="Purchases and sales journals: check your understanding",
    lesson="acc1-purchases-and-sales-journals",
    questions=[
        Q("Which transaction is entered in the purchases journal?",
          "Goods bought on credit for resale",
          [("Goods bought for cash", "Cash purchases go in the cash book."), ("A delivery van bought on credit", "A fixed asset is recorded in the general journal."), ("Goods sent back to a supplier", "Returns go in the returns outwards journal.")],
          0, "The purchases journal lists only credit purchases of goods for resale.", "Look for the words 'goods', 'credit' and 'resale' together.", "Purchases journal", "Recall"),
        Q("Which transaction is entered in the sales journal?",
          "Goods sold on credit to a customer",
          [("Goods sold for cash", "Cash sales go in the cash book."), ("An old table sold on credit", "A fixed asset is recorded in the general journal."), ("Goods returned by a customer", "Returns go in the returns inwards journal.")],
          1, "Only credit sales of goods in the normal course of trade go in the sales journal.", "Is the customer paying at once?", "Sales journal", "Recall"),
        N("A purchases journal has a net total of FCFA 1 200 000 on one invoice. VAT is 19.25%. How much VAT is entered, in FCFA?",
          231000, "1 200 000 x 0.1925 = 231 000.", "Multiply the net by 0.1925.", "VAT in the journal", math=r"1\,200\,000 \times 0.1925 = 231\,000"),
        Q("A purchases journal has three invoices with net amounts FCFA 400 000, 800 000 and 200 000. VAT is 19.25%. The total of the journal is",
          "FCFA 1 669 500",
          [("FCFA 1 400 000", "You omitted the VAT."), ("FCFA 269 500", "That is only the VAT."), ("FCFA 1 130 500", "You subtracted the VAT.")],
          2, "Net 1 400 000 + VAT 269 500 = 1 669 500.", "Add the three nets, then compute the VAT on the total.", "Totalling a journal", "Calculation", math=r"1\,400\,000 \times 1.1925 = 1\,669\,500"),
        Q("When the sales journal is posted, the VAT total is",
          "credited to the VAT collected account",
          [("debited to the VAT collected account", "VAT collected is a liability, increased by a credit."), ("credited to the Sales account", "VAT is kept separate from sales."), ("debited to the customers' accounts only", "Customers are debited with the whole invoice total, but the VAT account is separate.")],
          3, "VAT charged to customers is owed to the state, so VAT collected is credited.", "Is VAT collected an asset or a liability?", "Posting the sales journal", "Concept"),
        Q("The sales journal has net FCFA 2 000 000 and VAT FCFA 385 000. What total is debited to the customers' accounts?",
          "FCFA 2 385 000",
          [("FCFA 2 000 000", "Customers also owe the VAT."), ("FCFA 385 000", "That is only the VAT."), ("FCFA 1 615 000", "You subtracted the VAT.")],
          0, "Customers owe the net price plus VAT: 2 385 000.", "What must the customer pay in total?", "Posting the sales journal", "Application", math=r"2\,000\,000 + 385\,000 = 2\,385\,000"),
        Q("A shop buys a computer on credit for its office. Where is this recorded first?",
          "In the general journal",
          [("In the purchases journal", "The purchases journal is for goods bought for resale."), ("In the sales journal", "No sale has taken place."), ("In the returns journal", "No goods were returned.")],
          1, "A fixed asset bought on credit has no special journal, so the general journal is used.", "Is the computer bought for resale?", "Books of original entry", "Application"),
        Q("A bookkeeper enters in the sales journal: net FCFA 2 000 000, VAT FCFA 385 000, total FCFA 2 375 000. What is wrong?",
          "The total should be FCFA 2 385 000",
          [("The VAT should be FCFA 395 000", "385 000 is correct: 2 000 000 x 0.1925."), ("The net should be FCFA 2 375 000", "The net is the amount before VAT."), ("Nothing is wrong", "The columns do not cross-check: 2 000 000 + 385 000 = 2 385 000.")],
          0, "Cross-check: net + VAT must equal the total. 2 000 000 + 385 000 = 2 385 000, not 2 375 000.", "Add net and VAT yourself.", "Cross-checking a journal", "Reasoning", math=r"2\,000\,000 + 385\,000 = 2\,385\,000"),
    ]))

# ------------------------------------------------------------------ 9 returns journals
assert 300000 + vat(300000) == 357750
assert 1200000 - 230000 == 970000
assert vat(300000) == 57750
assert 120000 + vat(120000) == 143100 and 715500 - 143100 == 572400
SETS.append(practice_set(
    module=M2, topic="Returns journals",
    title="Returns journals: check your understanding",
    lesson="acc1-returns-journals",
    questions=[
        Q("Returns inwards are",
          "goods returned to us by customers",
          [("goods we return to suppliers", "That is returns outwards."), ("goods bought for cash", "Cash purchases are not returns."), ("goods taken by the owner", "That is drawings.")],
          0, "'Inwards' means into our business, from customers.", "In which direction do the goods move?", "Returns inwards", "Recall"),
        Q("We return damaged goods to a supplier. The document that supports this is a",
          "credit note",
          [("invoice sent by us", "We do not invoice our supplier for goods we return."), ("receipt", "A receipt acknowledges payment."), ("bank statement", "A bank statement shows the bank's records.")],
          1, "A credit note reduces what the buyer owes.", "Which document reduces the amount due?", "Credit notes", "Recall"),
        N("Goods of net value FCFA 300 000 are returned to a supplier. VAT is 19.25%. What is the total of the credit note, in FCFA?",
          357750, "VAT = 300 000 x 0.1925 = 57 750. Total = 300 000 + 57 750 = 357 750.", "Include the VAT that was charged.", "Credit note with VAT", math=r"300\,000 \times 1.1925 = 357\,750"),
        Q("In our books, goods returned by a customer lead to a posting that",
          "credits the customer's account",
          [("debits the customer's account", "The customer now owes less, so the account is credited."), ("credits the Returns inwards account", "Returns inwards is debited."), ("debits the supplier's account", "A customer return does not involve a supplier.")],
          2, "The customer's debt falls, so the customer is credited. Returns inwards and VAT collected are debited.", "Does the customer owe more or less?", "Posting returns inwards", "Concept"),
        N("We owe a supplier FCFA 1 200 000. We return goods and receive a credit note for FCFA 230 000. How much do we now owe, in FCFA?",
          970000, "1 200 000 - 230 000 = 970 000.", "The credit note reduces the debt.", "Supplier account", math=r"1\,200\,000 - 230\,000 = 970\,000"),
        Q("Goods were listed at FCFA 200 000 but a trade discount of 10% was given. They are all returned. At what value is the return recorded (before VAT)?",
          "FCFA 180 000",
          [("FCFA 200 000", "Returns are valued at the price actually charged, after trade discount."), ("FCFA 20 000", "That is the discount."), ("FCFA 220 000", "You added the discount.")],
          3, "Net price = 200 000 - 20 000 = 180 000.", "At what price was the sale really made?", "Valuing returns", "Application", math=r"200\,000 - 10\% \times 200\,000 = 180\,000"),
        Q("A returns outwards journal has net FCFA 240 000 and VAT FCFA 46 200. In posting, the VAT is",
          "credited to VAT recoverable",
          [("debited to VAT recoverable", "We recover less VAT after a return, so the debit balance is reduced by a credit."), ("credited to VAT collected", "VAT collected relates to sales."), ("debited to the supplier only", "The supplier is debited with the total, but VAT has its own account.")],
          1, "Returning goods cancels part of the VAT we reclaimed: credit VAT recoverable.", "Do we recover more or less VAT after the return?", "Posting returns outwards", "Reasoning"),
        N("A customer owed FCFA 715 500 (net 600 000 plus VAT 115 500). He returns goods of net value FCFA 120 000. VAT is 19.25%. How much does he now owe, in FCFA?",
          572400, "Return total = 120 000 + 23 100 = 143 100. Balance = 715 500 - 143 100 = 572 400.", "Reverse the VAT on the returned goods too.", "Customer account after a return", skill="Application", math=r"715\,500 - 143\,100 = 572\,400"),
    ]))

# ------------------------------------------------------------------ 10 general journal
assert 3000000 - 900000 == 2100000
assert 300000 + vat(300000) == 357750
assert 5400000 - 3200000 == 2200000
SETS.append(practice_set(
    module=M2, topic="The general journal",
    title="The general journal: check your understanding",
    lesson="acc1-general-journal",
    questions=[
        Q("Which transaction is recorded in the general journal?",
          "A van bought on credit",
          [("Goods sold on credit", "That is the sales journal."), ("Goods bought on credit for resale", "That is the purchases journal."), ("A cash sale", "That is the cash book.")],
          0, "A fixed asset on credit has no special book, so it goes in the general journal.", "Which item is not trading stock?", "General journal", "Recall"),
        Q("Every journal entry should end with",
          "a narration",
          [("a trial balance", "A trial balance is a separate list."), ("a signature of the customer", "No customer signature is needed."), ("the balance b/d", "That belongs to a ledger account.")],
          1, "The narration explains the entry, starting with 'Being...'.", "What does the reader need to know about why the entry was made?", "Journal layout", "Recall"),
        N("On 1 January a trader has assets of FCFA 3 000 000 and liabilities of FCFA 900 000. What is the capital figure in the opening journal entry, in FCFA?",
          2100000, "Capital = 3 000 000 - 900 000 = 2 100 000.", "Use the accounting equation.", "Opening entry", math=r"3\,000\,000 - 900\,000 = 2\,100\,000"),
        Q("In an opening journal entry, which accounts are credited?",
          "Liabilities and capital",
          [("Assets", "Assets are debited."), ("Expenses", "There are no expenses in an opening entry."), ("Drawings", "Drawings are not an opening balance.")],
          2, "Assets are debited; liabilities and capital are credited, so the entry balances.", "Use Assets = Capital + Liabilities.", "Opening entry", "Concept"),
        N("A computer is bought on credit: net price FCFA 300 000 plus VAT at 19.25%. What is credited to the supplier, in FCFA?",
          357750, "VAT = 57 750. Total credited = 300 000 + 57 750 = 357 750.", "The supplier is owed the price and the VAT.", "Fixed asset on credit", math=r"300\,000 \times 1.1925 = 357\,750"),
        Q("The owner takes goods at cost FCFA 40 000 for private use. The journal entry is",
          "Dr Drawings 40 000, Cr Purchases 40 000",
          [("Dr Purchases 40 000, Cr Drawings 40 000", "That is the reverse."), ("Dr Drawings 40 000, Cr Cash 40 000", "No cash was taken."), ("Dr Capital 40 000, Cr Sales 40 000", "No sale was made.")],
          3, "Drawings increase (debit); the goods leave the purchases (credit).", "Which account is credited to remove the goods?", "Drawings of goods", "Application"),
        Q("A freezer costing FCFA 250 000 was wrongly debited to the Purchases account. The correcting entry is",
          "Dr Equipment 250 000, Cr Purchases 250 000",
          [("Dr Purchases 250 000, Cr Equipment 250 000", "That would increase the error."), ("Dr Equipment 250 000, Cr Cash 250 000", "The cash was already paid."), ("Dr Cash 250 000, Cr Purchases 250 000", "No cash is received.")],
          1, "The amount must leave Purchases (credit) and enter Equipment (debit).", "Where should it have been debited originally?", "Correcting an error", "Application"),
        Q("An opening entry debits assets of FCFA 5 400 000 and credits liabilities of FCFA 3 200 000. What credit to capital is needed for the entry to balance?",
          "FCFA 2 200 000",
          [("FCFA 8 600 000", "You added assets and liabilities."), ("FCFA 3 200 000", "That repeats the liabilities."), ("FCFA 5 400 000", "That is the total of the assets.")],
          0, "Capital = 5 400 000 - 3 200 000 = 2 200 000.", "Debits must equal credits.", "Opening entry", "Reasoning", math=r"5\,400\,000 - 3\,200\,000 = 2\,200\,000"),
    ]))

