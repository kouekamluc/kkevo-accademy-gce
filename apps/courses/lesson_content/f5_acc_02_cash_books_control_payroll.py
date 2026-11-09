"""Form 5 Principles of Accounts: Cash Books, Petty Cash & Bank Reconciliation, and Control Accounts, Correction of Errors & Payroll
(10 lessons, one practice set each).

Every ledger, cash book, reconciliation and payroll table in the CODE blocks below is built by the small helpers at the top of
this file, and the totals the text quotes are checked with assert statements, so a figure cannot drift from the table.
All payroll rates are TEACHING RATES invented for practice; the current legal rates must be checked.
"""

from .dsl import *  # noqa: F403

COURSE = ("principles-of-accounts", "form-5")

M_CASH = "Cash Books, Petty Cash & Bank Reconciliation"
M_CTRL = "Control Accounts, Correction of Errors & Payroll"
T_CB1 = "Single and two-column cash books"
T_CB3 = "The three-column cash book"
T_CBA = "The analytical cash book"
T_PETTY = "The petty cash book"
T_BANK = "Bank reconciliation statements"
T_CTRL = "Control accounts"
T_ERR1 = "Errors not disclosed by the trial balance"
T_ERR2 = "The suspense account and errors disclosed"
T_PAY1 = "Payroll: calculating pay"
T_PAY2 = "Payroll: statutory deductions"


# ---------------------------------------------------------------- table helpers (used to build the CODE blocks)
def m(n):
    """Whole francs with a space between thousands: 12 000."""
    return f"{n:,}".replace(",", " ")


def fmt_row(cells, widths):
    cells = list(cells) + [None] * (len(widths) - len(cells))
    out = []
    for c, w in zip(cells, widths):
        if c is None or c == "":
            out.append(" " * w)
        elif isinstance(c, int):
            out.append(m(c).rjust(w))
        else:
            out.append(str(c).ljust(w))
    return " ".join(out)


def ledger_auto(lw, rw, left, right, bal_cols, free_cols=(), heads=None, bd="Balance b/d", cd="Balance c/d", lc=0):
    """Two-sided ledger text. Column 0 is the label. Balanced columns get Balance c/d and Balance b/d; free columns
    (such as discount) are only totalled. Returns (text, balances, totals_left, totals_right)."""
    nl, nr = len(lw), len(rw)
    left = [list(r) + [None] * (nl - len(r)) for r in left]
    right = [list(r) + [None] * (nr - len(r)) for r in right]
    sl = {c: sum(r[c] or 0 for r in left) for c in list(bal_cols) + list(free_cols)}
    sr = {c: sum(r[c] or 0 for r in right) for c in list(bal_cols) + list(free_cols)}
    cdl, cdr = [None] * nl, [None] * nr
    bdl, bdr = [None] * nl, [None] * nr
    bal = {}
    for c in bal_cols:
        d = sl[c] - sr[c]
        bal[c] = d
        if d > 0:
            cdr[c] = d
            bdl[c] = d
        elif d < 0:
            cdl[c] = -d
            bdr[c] = -d
    if any(v is not None for v in cdl):
        cdl[lc] = cd
        left.append(cdl)
    if any(v is not None for v in cdr):
        cdr[lc] = cd
        right.append(cdr)
    n = max(len(left), len(right))
    left += [[None] * nl] * (n - len(left))
    right += [[None] * nr] * (n - len(right))
    tl, tr = [None] * nl, [None] * nr
    for c in bal_cols:
        t = max(sl[c], sr[c])
        tl[c] = tr[c] = t
    for c in free_cols:
        tl[c], tr[c] = sl[c], sr[c]
    wl, wr = sum(lw) + nl - 1, sum(rw) + nr - 1
    rule = "-" * wl + "-+-" + "-" * wr
    lines = []
    if heads:
        lines += [fmt_row(heads[0], lw) + " | " + fmt_row(heads[1], rw), rule]
    for a, b in zip(left, right):
        lines.append(fmt_row(a, lw) + " | " + fmt_row(b, rw))
    lines += [rule, fmt_row(tl, lw) + " | " + fmt_row(tr, rw), rule]
    if any(v is not None for v in bdl) or any(v is not None for v in bdr):
        bdl[lc] = bd if any(v is not None for i, v in enumerate(bdl) if i != lc) else None
        bdr[lc] = bd if any(v is not None for i, v in enumerate(bdr) if i != lc) else None
        lines.append(fmt_row(bdl, lw) + " | " + fmt_row(bdr, rw))
    return "\n".join(lines), bal, tl, tr


def table(widths, heads, rows, total=None, rule_char="-"):
    """Simple one-sided table with a header row, optional total row."""
    w = sum(widths) + len(widths) - 1
    lines = [fmt_row(heads, widths), rule_char * w]
    lines += [fmt_row(r, widths) for r in rows]
    if total is not None:
        lines += [rule_char * w, fmt_row(total, widths), rule_char * w]
    return "\n".join(lines)


LESSONS = []

# ------------------------------------------------------------------ 1. Single and two-column cash books
_t1, _b1, _, _ = ledger_auto(
    [5, 14, 8], [5, 14, 8],
    [("1 Jun", "Balance b/d", 85000), ("2 Jun", "Sales", 40000), ("6 Jun", "J. Tabi", 15000)],
    [("3 Jun", "Rent", 25000), ("5 Jun", "Purchases", 30000), ("8 Jun", "Wages", 12000)],
    bal_cols=[2], lc=1, heads=[("Date", "Details", "FCFA"), ("Date", "Details", "FCFA")])
assert _b1[2] == 73000
_CB1 = "Dr                       CASH BOOK of Mama Ngo                Cr\n" + _t1

_t2, _b2, _, _ = ledger_auto(
    [11, 7, 7], [11, 7, 7],
    [("Balance b/d", 50000, 300000), ("Sales", 60000, None), ("Cash (C)", None, 70000),
     ("R. Fon", None, 90000), ("Bank (C)", 30000, None)],
    [("Eno", None, 120000), ("Bank (C)", 70000, None), ("Rent", 20000, None),
     ("Cash (C)", None, 30000), ("Salaries", None, 85000)],
    bal_cols=[1, 2], heads=[("Details", "Cash", "Bank"), ("Details", "Cash", "Bank")])
assert _b2[1] == 50000 and _b2[2] == 225000
_CB2 = _t2

LESSONS.append(lesson(
    module=M_CASH,
    topic=T_CB1,
    title="Single and two-column cash books",
    slug="acc2-single-two-column-cash-books",
    minutes=22,
    summary="The cash book records every receipt and payment of money. A single-column book holds cash only; a two-column book has cash and bank columns, and a contra entry moves money between them.",
    objectives=[
        "Explain why the cash book is both a book of original entry and a ledger account",
        "Write up a single-column cash book and balance it",
        "Write up a two-column cash book with cash and bank columns",
        "Record contra entries and say why they are not posted to other accounts",
    ],
    key_concepts=["Cash book", "Receipts (debit side)", "Payments (credit side)", "Contra entry", "Balance carried down", "Bank overdraft"],
    blocks=[
        H("Introduction"),
        T("Mama Ngo runs a provision store in Bafoussam. Every day money comes in from customers and goes out for rent, stock and wages. "
          "If she wrote each one in a different book, she would soon lose track. Instead she keeps one book for all money movements: the **cash book**."),
        D("The **cash book** is the book where all receipts and payments of cash and of money in the bank are first recorded. It is a "
          "**book of original entry** (the first place a transaction is written) and also the **cash account** (and bank account) of the ledger.",
          title="Cash book"),
        KEY("Which side?", "The cash book follows the usual double-entry rules for an asset account.", cards=[
            ["Debit side (left)", "Money coming IN: cash sales, money from debtors, capital introduced."],
            ["Credit side (right)", "Money going OUT: rent, purchases for cash, wages, payments to creditors."],
        ], note="In the SYSCOHADA chart, cash is in class 5 (cash in hand and bank accounts). The rules are the same."),
        T("Because the cash book is already an account, items are **not** entered in the cash book and then again in the cash account. "
          "Each item is entered once in the cash book, and the other side of the entry is posted to the ledger account named in the details column."),
        H("The single-column cash book"),
        T("A single-column cash book has one money column on each side. It is used by a trader who handles only cash. Mama Ngo starts "
          "June with FCFA 85 000 in cash. Her transactions are: 2 June, cash sales 40 000; 3 June, paid rent 25 000; 5 June, bought "
          "goods for cash 30 000; 6 June, received 15 000 from a debtor, J. Tabi; 8 June, paid wages 12 000."),
        CODE(_CB1, "text", title="Single-column cash book (FCFA)",
             caption="The balance c/d is the figure that makes both sides equal. It is brought down on the debit side on the next day."),
        EX("Worked example 1: balancing the cash book", intro="Balance Mama Ngo's cash book at 8 June.", steps=[
            S("Add the debit side", math=r"85\,000 + 40\,000 + 15\,000 = 140\,000"),
            S("Add the credit side (before the balance)", math=r"25\,000 + 30\,000 + 12\,000 = 67\,000"),
            S("Find the balance", math=r"140\,000 - 67\,000 = 73\,000", text="Write 73 000 on the credit side as Balance c/d so that both sides total 140 000."),
            S("Bring it down", text="Write Balance b/d 73 000 on the debit side below the totals. This is the cash she still has on 9 June."),
        ]),
        TIP("A cash balance is always a debit balance. You cannot pay out more cash than you hold. If your cash balance comes out on the credit side, you have made an error."),
        H("The two-column cash book"),
        T("Most businesses also have a bank account. The **two-column cash book** has a **cash** column and a **bank** column on each side. "
          "Cheques received and paid, and bank transfers, go in the bank column."),
        D("A **contra entry** is a transaction where both the debit and the credit are in the same cash book, because money moves between "
          "cash and bank. It is marked **C** in the folio column. Depositing cash in the bank: debit bank, credit cash. Withdrawing cash "
          "from the bank for office use: debit cash, credit bank.", title="Contra entry"),
        T("A trader opens July with cash 50 000 and bank 300 000. Transactions: 2 July, cash sales 60 000; 3 July, paid cheque to a supplier, Eno, 120 000; "
          "4 July, banked cash 70 000; 6 July, received a cheque from a customer, R. Fon, 90 000; 8 July, paid rent in cash 20 000; "
          "10 July, withdrew 30 000 from the bank for the till; 12 July, paid salaries by bank transfer 85 000."),
        CODE(_CB2, "text", title="Two-column cash book (FCFA)",
             caption="Dates are left out so the table fits a phone screen. In the exam always write the date of every entry."),
        EX("Worked example 2: balancing two columns", intro="Find the closing cash and bank balances.", steps=[
            S("Cash debit side", math=r"50\,000 + 60\,000 + 30\,000 = 140\,000"),
            S("Cash credit side", math=r"70\,000 + 20\,000 = 90\,000"),
            S("Cash balance", math=r"140\,000 - 90\,000 = 50\,000", text="Both columns are balanced separately."),
            S("Bank debit side", math=r"300\,000 + 70\,000 + 90\,000 = 460\,000"),
            S("Bank credit side", math=r"120\,000 + 30\,000 + 85\,000 = 235\,000"),
            S("Bank balance", math=r"460\,000 - 235\,000 = 225\,000", text="The cash balance is 50 000 and the bank balance is 225 000, both brought down on the debit side."),
        ]),
        KEY("Posting from the cash book", "Contra entries are complete inside the cash book, so nothing is posted to another account.", cards=[
            ["Not contra", "Post the other side to the ledger account named (Sales, Rent, Eno, R. Fon)."],
            ["Contra (C)", "Both sides are already in the cash book. Do not post anywhere."],
        ], note="The cash book itself is not posted to the cash account again; it is that account."),
        D("A **bank overdraft** happens when the bank lets a business pay out more than it has deposited. The bank column then has a **credit** "
          "balance (the bank is owed money). Only the bank column can have a credit balance, never the cash column.", title="Overdraft"),
        MISTAKE("Posting a contra entry to the ledger", "When cash is banked, the debit and the credit are both in the cash book. Writing 'Bank' in the ledger again "
                "records the same transaction twice."),
        MISTAKE("Putting the entry on the wrong side", "Cash received goes on the debit (left) side. Many candidates put a payment on the debit side because it 'feels' like a cost."),
        MISTAKE("Forgetting to bring the balance down", "After the totals, write the balance b/d on the opposite side from the balance c/d. Without it the next period starts from nothing."),
        QUIZ("Which entry is a contra entry?", [
            "Cash sales of 60 000 paid into the bank the next day",
            "Paying a supplier by cheque",
            "Banking 70 000 of cash takings",
            "Receiving a cheque from a debtor",
        ], 2, "Banking cash moves money between two cash-book columns: debit bank, credit cash. Both entries are in the cash book.",
             hint="A contra needs both sides in the cash book.",
             feedback=["The sale is a normal entry: its other side is the Sales account.", "The other side is the supplier's account.", "", "The other side is the debtor's account."]),
        QUIZ("Which of these balances is impossible in the cash column?", [
            "A debit balance of 50 000", "A credit balance of 5 000", "A nil balance", "A debit balance of 1 000"],
             1, "You cannot pay out more cash than you have, so the cash column cannot have a credit balance. (The bank column can, as an overdraft.)",
             hint="Think of a till drawer.",
             feedback=["That is normal.", "", "All cash can be spent, leaving nil.", "That is normal."], title="Quick check 2"),
        TIP("Paper 1 asks which side an item goes on, what a contra entry is, and the balance of a column. Paper 2 may ask you to write up and balance a two-column cash book. Draw the columns carefully and total each separately."),
        PQ("A trader had cash 24 000 on 1 May. Cash sales were 18 000 and she paid 9 000 for transport. Find her cash balance.", "Debit side: 24 000 + 18 000 = 42 000. Credit side: 9 000. Balance = 42 000 − 9 000 = 33 000 debit."),
        PQ("On 5 March a business banked 40 000 of cash. Write the entry in the two-column cash book and say whether it is posted to any ledger account.",
           "Debit side: Bank column, 40 000, details 'Cash (C)'. Credit side: Cash column, 40 000, details 'Bank (C)'. It is a contra entry, so it is not posted to any other account."),
        PQ("The bank column of a cash book shows debit total 150 000 and credit total 172 000. Find the balance and say what it means.",
           "Credit total is higher: 172 000 − 150 000 = 22 000 credit balance. The business is overdrawn by 22 000 at the bank."),
        SUM("The cash book is a book of original entry and also the cash and bank account.",
            "Receipts go on the debit side and payments on the credit side.",
            "A two-column cash book has cash and bank columns, each balanced separately.",
            "A contra entry moves money between cash and bank and is not posted elsewhere.",
            "Cash cannot have a credit balance; the bank column can (an overdraft)."),
    ],
))

# ------------------------------------------------------------------ 2. The three-column cash book
_t3, _b3, _tl3, _tr3 = ledger_auto(
    [10, 5, 7, 7], [10, 5, 7, 7],
    [("Bal. b/d", None, 40000, 250000), ("A. Kum", 2000, 48000, None), ("Sales", None, 36000, None),
     ("Cash (C)", None, None, 60000), ("C. Mbah", 2000, None, 78000)],
    [("B. Nji", 5000, None, 95000), ("Bank (C)", None, 60000, None), ("Stationery", None, 9000, None),
     ("D. Ayuk", 3000, None, 57000)],
    bal_cols=[2, 3], free_cols=[1], bd="Bal. b/d", cd="Bal. c/d",
    heads=[("Details", "Disc.", "Cash", "Bank"), ("Details", "Disc.", "Cash", "Bank")])
assert _tl3[1] == 4000 and _tr3[1] == 8000          # discount allowed, discount received
assert _b3[2] == 55000 and _b3[3] == 236000          # closing cash and bank
assert 40000 + 48000 + 36000 == 124000 and 60000 + 9000 == 69000 and 124000 - 69000 == 55000
assert 250000 + 60000 + 78000 == 388000 and 95000 + 57000 == 152000 and 388000 - 152000 == 236000
assert 2000 + 2000 == 4000 and 5000 + 3000 == 8000
assert 50000 * 4 // 100 == 2000 and 80000 * 25 // 1000 == 2000 and 80000 - 2000 == 78000
assert 120000 * 5 // 100 == 6000 and 120000 - 6000 == 114000
assert 1500 + 2000 + 700 == 4200 and 3000 + 800 == 3800
_CB3 = _t3

_KUM = ("Dr          A. KUM (debtor)                    Cr\n"
        "1 Aug Balance b/d  50 000 | 2 Aug Cash                48 000\n"
        "                          | 2 Aug Discount allowed     2 000\n"
        "                          |                           ------\n"
        "                   50 000 |                           50 000")

LESSONS.append(lesson(
    module=M_CASH,
    topic=T_CB3,
    title="The three-column cash book with discounts",
    slug="acc2-three-column-cash-book",
    minutes=22,
    summary="The three-column cash book adds a discount column to the cash and bank columns. Discount allowed is on the debit side, discount received on the credit side, and the discount columns are totalled, not balanced.",
    objectives=[
        "Distinguish cash discount from trade discount",
        "Record discount allowed on the debit side and discount received on the credit side",
        "Balance the cash and bank columns and total (not balance) the discount columns",
        "Post the discount totals to the discount accounts",
    ],
    key_concepts=["Cash (settlement) discount", "Discount allowed", "Discount received", "Three-column cash book", "Posting discount totals"],
    blocks=[
        H("Introduction"),
        T("A wholesaler in Douala tells her customers: 'Pay within 10 days and take 4% off.' A customer who owes 50 000 pays 48 000 and the debt is cleared. "
          "The 2 000 not paid is a **cash discount**. The two-column cash book has nowhere to show it, so we add a third column."),
        D("A **cash discount** (also called a **settlement discount**) is a reduction in the amount owed, given to a customer who pays promptly. "
          "It is a financial discount and it is recorded in the books because it happens when payment is made.", title="Cash discount"),
        D("A **trade discount** is a reduction in the list price of goods given by the seller to a trade buyer. It is taken off on the invoice, so it is "
          "**never** recorded in the cash book or in the ledger.", title="Trade discount"),
        KEY("Two discounts, two sides", "Think from the point of view of the business that keeps the books.", cards=[
            ["Discount allowed", "We give it to a debtor who pays early. It is an expense for us. Written in the discount column on the DEBIT side."],
            ["Discount received", "A creditor gives it to us when we pay early. It is a gain for us. Written in the discount column on the CREDIT side."],
        ], note="In the SYSCOHADA chart these are the accounts for discounts granted (escomptes accordés) and discounts obtained (escomptes obtenus); check the exact wording in your textbook."),
        H("Why the sides are the way they are"),
        T("When A. Kum pays 48 000 to clear a debt of 50 000, her account must be credited with the full 50 000: 48 000 cash and 2 000 discount. "
          "The cash book shows cash received (debit cash 48 000). The matching debit for the 2 000 is the expense Discount Allowed. "
          "So the discount sits on the debit side beside the cash."),
        CODE(_KUM, "text", title="The debtor's account", caption="Both the cash and the discount are credited in A. Kum's account, so the debt is cleared."),
        T("For a creditor the sides reverse. We pay B. Nji 95 000 to clear 100 000. His account is debited 100 000. The cash book shows cash paid (credit bank 95 000) and the "
          "discount received 5 000 on the credit side."),
        H("A three-column cash book"),
        T("A business opens August with cash 40 000 and bank 250 000. Transactions: A. Kum pays 48 000 cash to settle 50 000; B. Nji is paid by cheque 95 000 to settle 100 000; "
          "cash sales 36 000; cash banked 60 000; C. Mbah's cheque of 78 000 settles 80 000; stationery bought for cash 9 000; D. Ayuk is paid by cheque 57 000 to settle 60 000."),
        CODE(_CB3, "text", title="Three-column cash book (FCFA)",
             caption="Scroll sideways on a small phone. The discount columns are only totalled; cash and bank are balanced."),
        EX("Worked example 1: closing balances", intro="Find the cash and bank balances from the cash book above.", steps=[
            S("Cash debit side", math=r"40\,000 + 48\,000 + 36\,000 = 124\,000"),
            S("Cash credit side", math=r"60\,000 + 9\,000 = 69\,000", text="The 60 000 is the cash banked (a contra entry)."),
            S("Cash balance", math=r"124\,000 - 69\,000 = 55\,000"),
            S("Bank balance", math=r"(250\,000 + 60\,000 + 78\,000) - (95\,000 + 57\,000) = 388\,000 - 152\,000 = 236\,000"),
        ]),
        EX("Worked example 2: total the discount columns", intro="Find the discount totals and say where they are posted.", steps=[
            S("Discount allowed (debit side)", math=r"2\,000 + 2\,000 = 4\,000", text="From A. Kum and C. Mbah."),
            S("Discount received (credit side)", math=r"5\,000 + 3\,000 = 8\,000", text="From B. Nji and D. Ayuk."),
            S("Post the totals", text="Debit Discount Allowed account 4 000. Credit Discount Received account 8 000. The two totals are not set off against each other, and no balance c/d is written under the columns."),
        ]),
        EX("Worked example 3: find the discount", intro="C. Mbah owed 80 000 and was allowed a 2.5% cash discount. How much did she pay and how much was the discount?", steps=[
            S("Discount", math=r"2.5\% \times 80\,000 = 2\,000"),
            S("Cash paid", math=r"80\,000 - 2\,000 = 78\,000", text="The cash book shows bank 78 000 and discount allowed 2 000 on the debit side."),
        ]),
        TIP("Check each line: the cash (or bank) amount plus the discount equals the amount cleared in the personal account. If a customer clears 80 000 and pays 78 000, the discount is 2 000."),
        MISTAKE("Balancing the discount columns", "Only the cash and bank columns are balanced. The two discount columns are on opposite sides, belong to different accounts and are just added up."),
        MISTAKE("Entering a trade discount in the cash book", "A trade discount is deducted on the invoice before any entry is made. Only a cash (settlement) discount for early payment goes in the discount column."),
        MISTAKE("Putting discount received on the debit side", "Discount received goes on the CREDIT side, next to the payment. Discount allowed goes on the debit side, next to the receipt."),
        QUIZ("Joseph pays his supplier 57 000 by cheque to clear a debt of 60 000. How is the 3 000 recorded in his cash book?", [
            "Discount allowed, debit side", "Discount received, credit side", "Discount received, debit side", "It is not recorded"],
             1, "He pays the supplier, so the entry is on the credit side. A reduction given to him is a discount received.",
             hint="He is paying, and the supplier is giving the reduction.",
             feedback=["Discount allowed is what the business gives to customers.", "", "Discount received is always on the credit side.", "A cash discount is recorded; only a trade discount is not."]),
        QUIZ("The discount allowed column total is posted to the", [
            "credit of the Discount Allowed account", "debit of the Discount Allowed account", "credit of the Discount Received account", "bank account"],
             1, "Discount allowed is an expense, so its account is debited with the column total.",
             hint="Discount allowed is an expense for the business.",
             feedback=["An expense is debited.", "", "That account takes the discount received column.", "The bank balance is not affected by the discount column."], title="Quick check 2"),
        TIP("In Paper 2 questions on cash books, you will often have to write up a three-column cash book from a list and then balance it. In Paper 1 expect questions on the side of each discount and on trade versus cash discount."),
        PQ("A debtor owes 40 000 and pays 38 000 in full settlement. Which discount is it, on which side of the cash book, and how much?", "Discount allowed, 2 000, on the debit side. The debtor's account is credited 40 000 (38 000 cash and 2 000 discount)."),
        PQ("Over a month the discount allowed entries were 1 500, 2 000 and 700, and the discount received entries were 3 000 and 800. Give the totals and the postings.",
           "Discount allowed 1 500 + 2 000 + 700 = 4 200: debit the Discount Allowed account. Discount received 3 000 + 800 = 3 800: credit the Discount Received account."),
        PQ("A supplier is owed 120 000. The business pays by cheque and takes a 5% discount. How much is paid and where is the discount recorded?",
           "Discount received 5% × 120 000 = 6 000. Cheque 120 000 − 6 000 = 114 000, credit side, bank column. Discount 6 000 on the credit side, discount column."),
        SUM("A cash discount is for early payment and is recorded; a trade discount is deducted on the invoice and is not recorded.",
            "Discount allowed is on the debit side of the cash book; discount received on the credit side.",
            "The cash and bank columns are balanced; the discount columns are only totalled.",
            "The totals are posted to the Discount Allowed (debit) and Discount Received (credit) accounts.",
            "Individual discounts are in the personal accounts through the cash and discount entries."),
    ],
))

# ------------------------------------------------------------------ 3. The analytical cash book
_rec = [
    ("3 Nov", "Cash sales", 45000, 45000, None, None),
    ("4 Nov", "J. Tabi", 20000, None, 20000, None),
    ("5 Nov", "Cash sales", 38000, 38000, None, None),
    ("6 Nov", "Owner capital", 100000, None, None, 100000),
    ("7 Nov", "Cash sales", 52000, 52000, None, None),
]
_pay = [
    ("3 Nov", "Purchases", 30000, 30000, None, None, None),
    ("4 Nov", "Wages", 15000, None, 15000, None, None),
    ("5 Nov", "Rent", 25000, None, None, 25000, None),
    ("6 Nov", "Purchases", 22000, 22000, None, None, None),
    ("7 Nov", "B. Nji", 40000, None, None, None, 40000),
    ("7 Nov", "Wages", 15000, None, 15000, None, None),
]
_rt = [sum((r[i] or 0) for r in _rec) for i in range(2, 6)]
_pt = [sum((r[i] or 0) for r in _pay) for i in range(2, 7)]
assert _rt == [255000, 135000, 20000, 100000] and _rt[0] == sum(_rt[1:])      # cross-cast of receipts
assert _pt == [147000, 52000, 30000, 25000, 40000] and _pt[0] == sum(_pt[1:])  # cross-cast of payments
assert 20000 + 255000 - 147000 == 128000
_REC = table([5, 13, 8, 8, 8, 8], ["Date", "Details", "Total", "Sales", "Debtors", "Capital"], _rec, total=["", "Totals"] + _rt)
_PAY = table([5, 12, 8, 8, 7, 7, 9], ["Date", "Details", "Total", "Purch.", "Wages", "Rent", "Creditors"], _pay, total=["", "Totals"] + _pt)
_SUMMARY = "\n".join([
    "Opening cash balance      " + m(20000).rjust(9),
    "Add total receipts        " + m(255000).rjust(9),
    "Less total payments       " + ("(" + m(147000) + ")").rjust(9),
    "                          " + "-" * 9,
    "Closing cash balance      " + m(128000).rjust(9)])
assert 20000 + 255000 - 147000 == 128000

LESSONS.append(lesson(
    module=M_CASH,
    topic=T_CBA,
    title="The analytical cash book",
    slug="acc2-analytical-cash-book",
    minutes=22,
    summary="The analytical cash book shows each receipt and payment in a total column and again in an analysis column (sales, debtors, wages, rent). The analysis totals are posted to the ledger once, and they must cross-cast to the total column.",
    objectives=[
        "Explain what an analytical cash book is and why OHADA-style records use it",
        "Analyse receipts and payments into columns",
        "Cross-cast: check that the analysis columns add up to the total column",
        "Post the column totals and find the closing cash balance",
    ],
    key_concepts=["Analytical cash book", "Analysis column", "Total column", "Cross-casting", "Posting column totals"],
    blocks=[
        H("Introduction"),
        T("A busy shop in Bamenda takes cash from many customers every day and pays for goods, wages and rent. Posting every cash sale one by one to the Sales account "
          "would be slow. If the cash book also puts each amount into a column named **Sales**, the shop can add the column once a month and post a single total."),
        D("An **analytical cash book** (the OHADA approach) is a cash book in which every receipt and payment is entered in a **total column** and also in an "
          "**analysis column** that tells what the money was for. The analysis column totals are posted to the ledger accounts.", title="Analytical cash book"),
        KEY("How an analytical cash book is arranged", "The receipts and the payments each have their own total column.", cards=[
            ["Receipts", "Total column, then analysis columns such as Sales, Debtors, Capital and Other receipts."],
            ["Payments", "Total column, then analysis columns such as Purchases, Wages, Rent, Creditors and Other payments."],
        ], note="The columns are chosen to suit the business. A business can also add a VAT column; check the questions for the columns you are given."),
        H("The rule of every row"),
        T("Each row has the **same amount** in the total column and in exactly one analysis column. (Sometimes an item is split, for example an amount that includes VAT; the parts "
          "then add up to the total.) This is what makes the check at the bottom possible."),
        D("**Cross-casting** means adding the totals of all the analysis columns across the page and checking that they equal the total of the total column. "
          "If they do not agree, there is an error in one row or in an addition.", title="Cross-casting"),
        H("A week of receipts"),
        T("Mama Ngo's shop opened the week of 3 November with cash 20 000. Here are the receipts. Cash sales 45 000, 38 000 and 52 000 go to Sales. A debtor, J. Tabi, "
          "paid 20 000, which goes to Debtors. The owner added 100 000 of her own money, which goes to Capital."),
        CODE(_REC, "text", title="Analytical cash book: receipts (FCFA)",
             caption="Sales 135 000 + Debtors 20 000 + Capital 100 000 = 255 000, the total column. The columns cross-cast."),
        H("A week of payments"),
        CODE(_PAY, "text", title="Analytical cash book: payments (FCFA)",
             caption="Purchases 52 000 + Wages 30 000 + Rent 25 000 + Creditors 40 000 = 147 000. The columns cross-cast."),
        EX("Worked example 1: cross-cast and balance", intro="Check the two analysed tables and find the closing cash balance.", steps=[
            S("Cross-cast the receipts", math=r"135\,000 + 20\,000 + 100\,000 = 255\,000", text="This equals the total column, so the receipts are correct."),
            S("Cross-cast the payments", math=r"52\,000 + 30\,000 + 25\,000 + 40\,000 = 147\,000", text="This equals the total column."),
            S("Closing balance", math=r"20\,000 + 255\,000 - 147\,000 = 128\,000", text="The cash book is balanced the usual way: opening balance plus receipts less payments."),
        ]),
        CODE(_SUMMARY, "text", title="Cash summary"),
        EX("Worked example 2: a missing column total", intro="The payments total column is 147 000. Purchases are 52 000, rent 25 000 and creditors 40 000. Find the wages total.", steps=[
            S("Add the known analysis columns", math=r"52\,000 + 25\,000 + 40\,000 = 117\,000"),
            S("Subtract from the total column", math=r"147\,000 - 117\,000 = 30\,000", text="The wages column must total 30 000. It agrees with the two wage payments of 15 000."),
        ]),
        H("Posting the totals"),
        T("The column totals are posted once. Receipts: credit Sales 135 000, credit the debtors' control account 20 000 (each debtor's own account is credited with their own amount, for example J. Tabi 20 000), credit Capital 100 000. "
          "Payments: debit Purchases 52 000, Wages 30 000, Rent 25 000, and the creditors' control account 40 000 (with B. Nji's own account debited 40 000). "
          "The cash account itself is the cash book, so no posting is made to it."),
        EX("Worked example 3: choose the column", intro="Name the column for each item: (a) a customer on credit pays 15 000; (b) the shop pays 12 000 for electricity; (c) goods bought for cash 18 000.", steps=[
            S("(a) Money from a debtor", text="Receipts, Debtors column."),
            S("(b) Electricity", text="Payments. There is no Electricity column, so it goes in the Other payments column (or in a column named for it if the book has one)."),
            S("(c) Goods for resale bought for cash", text="Payments, Purchases column."),
        ]),
        TIP("When you are given a ready-made analysed cash book, find the column heading first. An amount in the wrong column is the main source of errors."),
        MISTAKE("Cross-casting forgotten", "Adding only down each column does not catch an amount that was put in two columns or in none. Add across the totals as well and check against the total column."),
        MISTAKE("Posting the total column to a ledger account", "The total column only gives the check and the balance. The ledger accounts get the analysis column totals, not the total column."),
        QUIZ("The main purpose of an analysis column in a cash book is to", [
            "avoid writing the date", "allow the column total to be posted to a ledger account in one entry",
            "balance the cash book automatically", "replace the trial balance"], 1,
             "Analysis columns group items of the same kind so that one total can be posted instead of many entries.",
             hint="Think about posting many sales.",
             feedback=["The date is still written.", "", "Balancing is done with the total column.", "The trial balance is still prepared from the ledger."]),
        QUIZ("A payments total column is 80 000. The analysis columns are Purchases 35 000, Wages 20 000 and Rent 15 000. What does this show?", [
            "The cash book is correct", "The analysis columns are 10 000 short", "The total column is 10 000 too high", "Rent is wrong"],
             1, "35 000 + 20 000 + 15 000 = 70 000, which is 10 000 less than 80 000. An item was left out of the analysis or entered wrongly.",
             hint="Add the three analysis columns and compare.",
             feedback=["The columns do not cross-cast.", "", "The error could be in either; the check only shows a difference of 10 000.", "The check does not point to one column."], title="Quick check 2"),
        TIP("Exam questions give columns or ask you to design them. Paper 2 may ask you to fill an analysed cash book from a list and post the totals; Paper 1 asks about the purpose of the book."),
        PQ("A receipts total column shows 60 000. Cash sales are 25 000 and debtors 18 000. What amount remains for other receipts?", "60 000 − 25 000 − 18 000 = 17 000."),
        PQ("Payments for the week were: purchases 40 000; wages 12 000; purchases 8 000; rent 20 000. Find the Purchases column total and the total payments.",
           "Purchases 40 000 + 8 000 = 48 000. Total payments 40 000 + 12 000 + 8 000 + 20 000 = 80 000, which equals 48 000 + 12 000 + 20 000."),
        PQ("Opening cash was 30 000. Total receipts were 180 000 and total payments 150 000. Find the closing balance.", "30 000 + 180 000 − 150 000 = 60 000."),
        SUM("An analytical cash book shows each amount in a total column and in an analysis column.",
            "The analysis column totals are posted to the ledger, so many entries become one.",
            "Cross-cast: the analysis totals must add up to the total column.",
            "The cash balance is opening balance plus total receipts less total payments.",
            "Choose the column from the nature of the item: sales, debtors, purchases, wages, rent and so on."),
    ],
))

# ------------------------------------------------------------------ 4. The petty cash book
_pc = [
    ("2 Mar", "Stamps", 3000, 3000, None, None, None),
    ("3 Mar", "Taxi fare", 4500, None, 4500, None, None),
    ("4 Mar", "Paper, pens", 7500, None, None, 7500, None),
    ("5 Mar", "Soap, brooms", 6000, None, None, None, 6000),
    ("6 Mar", "Taxi fare", 2500, None, 2500, None, None),
    ("7 Mar", "Exercise books", 5000, None, None, 5000, None),
]
_pw = [8, 5, 14, 7, 6, 6, 6, 8]
_ph = ["Receipts", "Date", "Details", "Total", "Post.", "Travel", "Stat.", "Cleaning"]
_ptot = [sum((r[i] or 0) for r in _pc) for i in range(2, 7)]
assert _ptot == [28500, 3000, 7000, 12500, 6000] and _ptot[0] == sum(_ptot[1:])
_float, _spent = 50000, _ptot[0]
_bal = _float - _spent
assert _bal == 21500 and _bal + _spent == _float
_pl = [fmt_row(_ph, _pw), "-" * (sum(_pw) + len(_pw) - 1)]
_pl.append(fmt_row([_float, "1 Mar", "Cash book"], _pw))
for r in _pc:
    _pl.append(fmt_row([None] + list(r), _pw))
_pl.append("-" * (sum(_pw) + len(_pw) - 1))
_pl.append(fmt_row([None, None, "Totals"] + _ptot, _pw))
_pl.append(fmt_row([None, "7 Mar", "Balance c/d", _bal], _pw))
_pl.append("-" * (sum(_pw) + len(_pw) - 1))
_pl.append(fmt_row([_float, None, "Total", _float], _pw))
_pl.append("-" * (sum(_pw) + len(_pw) - 1))
_pl.append(fmt_row([_bal, "8 Mar", "Balance b/d"], _pw))
_pl.append(fmt_row([_spent, "8 Mar", "Cash book"], _pw))
_PETTY = "\n".join(_pl)
assert _bal + _spent == 50000
# example 2
assert 80000 - 62400 == 17600
_J = ("Dr  Postage               3 000\n"
      "Dr  Travel                7 000\n"
      "Dr  Stationery           12 500\n"
      "Dr  Cleaning              6 000\n"
      "    Cr  Main cash book (reimbursement)   28 500")

LESSONS.append(lesson(
    module=M_CASH,
    topic=T_PETTY,
    title="The petty cash book and the imprest system",
    slug="acc2-petty-cash-book",
    minutes=22,
    summary="A petty cash book records small payments. Under the imprest system the petty cashier starts each period with a fixed float and is refunded exactly what was spent, so the float is restored.",
    objectives=[
        "Explain why a business keeps a petty cash book",
        "Describe the imprest system and the float",
        "Write up and balance a petty cash book with analysis columns",
        "Work out the reimbursement and post the analysis totals",
    ],
    key_concepts=["Petty cash", "Imprest system", "Float", "Petty cash voucher", "Reimbursement", "Analysis columns"],
    blocks=[
        H("Introduction"),
        T("The secretary of a school in Buea buys stamps, pays a taxi fare for a parcel and buys cleaning soap. These payments are small. Recording each of them in the main cash book "
          "would crowd it with trivial entries and tempt the head cashier to handle coins all day. So a junior employee, the **petty cashier**, looks after a small fund and writes the payments in a **petty cash book**."),
        D("**Petty cash** is a small amount of cash kept for minor expenses such as postage, fares, refreshments and cleaning materials. "
          "The **petty cash book** is the book of original entry for these payments.", title="Petty cash"),
        D("Under the **imprest system** the petty cashier starts each period with an agreed amount called the **float** (or imprest). At the end of the period the head cashier "
          "pays back exactly the amount spent, so the float is restored to its original size.", title="Imprest system"),
        IMG("f5acc2-imprest-cycle.svg", alt="Cycle: head cashier gives a float, petty cashier pays against vouchers, the book is totalled, the head cashier reimburses the amount spent and the float is restored.",
            caption="Figure 1. The imprest cycle. The amount reimbursed always equals the amount spent."),
        KEY("Rules of the imprest system", "These rules give control over small cash.", cards=[
            ["Fixed float", "The petty cashier starts every period with the same amount, for example 50 000."],
            ["Vouchers", "Every payment is supported by a petty cash voucher, signed by the person paid and approved by a supervisor."],
            ["Reimbursement", "The cash book pays back only what was spent, so cash plus vouchers always equals the float."],
        ], note="The size of the float is chosen by the business. The numbers in this lesson are invented for practice."),
        H("Writing up the petty cash book"),
        T("The petty cashier receives a float of 50 000 on 1 March. The payments (each with a voucher) are: 2 March, stamps 3 000; 3 March, taxi fare 4 500; 4 March, paper and pens 7 500; "
          "5 March, soap and brooms 6 000; 6 March, taxi fare 2 500; 7 March, exercise books 5 000. The book has a receipts column on the left, a total column for payments and four analysis columns."),
        CODE(_PETTY, "text", title="Petty cash book (FCFA)",
             caption="Post. = postage, Stat. = stationery. After the book is balanced the head cashier pays the 28 500 spent, restoring the float to 50 000."),
        EX("Worked example 1: totals and balance", intro="Add the columns and find the balance and the reimbursement.", steps=[
            S("Total spent", math=r"3\,000 + 4\,500 + 7\,500 + 6\,000 + 2\,500 + 5\,000 = 28\,500"),
            S("Cross-cast the analysis", math=r"3\,000 + 7\,000 + 12\,500 + 6\,000 = 28\,500",
              text="Postage 3 000; Travel 4 500 + 2 500 = 7 000; Stationery 7 500 + 5 000 = 12 500; Cleaning 6 000."),
            S("Balance still in the box", math=r"50\,000 - 28\,500 = 21\,500", text="This is carried down as Balance c/d."),
            S("Reimbursement", text="The head cashier pays 28 500, the amount spent. The petty cashier has 21 500 + 28 500 = 50 000 again, which equals the float."),
        ]),
        H("Posting from the petty cash book"),
        T("The petty cash book is a book of original entry only: it is not part of the ledger. The totals of the analysis columns are posted to the debit of the expense accounts. "
          "The matching credit is the payment of 28 500 in the main cash book, which already records the reimbursement."),
        CODE(_J, "text", title="Posting the analysis totals", caption="Each analysis total is a debit in its expense account."),
        EX("Worked example 2: a different float", intro="A float of 80 000 is used. During the month payments of 62 400 are made. What is the reimbursement and what is left in the box before it?", steps=[
            S("Amount to reimburse", text="Exactly the amount spent: 62 400."),
            S("Cash left before reimbursement", math=r"80\,000 - 62\,400 = 17\,600"),
            S("After reimbursement", math=r"17\,600 + 62\,400 = 80\,000", text="The float is back to 80 000."),
        ]),
        TIP("Imprest check: balance c/d plus the total spent must equal the float. If they do not, a voucher is missing or an addition is wrong."),
        MISTAKE("Reimbursing a round amount", "Under the imprest system the amount refunded is the exact total of the vouchers, not a round amount. Otherwise the float is not restored."),
        MISTAKE("Posting the petty cash book as if it were a ledger account", "The petty cash book is a book of original entry. Post the analysis totals to the expense accounts and the reimbursement is a payment in the main cash book."),
        MISTAKE("Forgetting the opening float in the receipts column", "The float is the first entry (or the balance b/d plus the reimbursement). Leave it out and the balance will not agree."),
        QUIZ("In the imprest system, the amount paid by the head cashier to restore the float is", [
            "always the size of the float", "a round number agreed each time", "the exact amount spent in the period", "the balance left in the box"], 2,
             "The amount reimbursed equals the amount spent, so cash in hand plus the refund equals the float again.",
             hint="Float = cash left + amount spent.",
             feedback=["That is only true when the whole float was spent.", "A round figure would leave the float too high or too low.", "", "That is what is already in the box."]),
        QUIZ("The petty cashier's analysis columns total 12 400 but the total column is 13 400. What should the cashier do?", [
            "Post both figures", "Find the missing 1 000 in the rows", "Reduce the float", "Change the total to 12 400"], 1,
             "The columns must cross-cast. Check each voucher against its row to find the 1 000 that was not analysed.",
             hint="A control check has failed.",
             feedback=["The difference first has to be explained.", "", "The float does not change.", "That would hide a possible error."], title="Quick check 2"),
        TIP("Paper 1 asks about the purpose of the imprest system and the reimbursement; Paper 2 can ask you to write up and balance a petty cash book. Always total and cross-cast the analysis columns."),
        PQ("A float of 60 000 is kept. During a month, 46 800 is spent. Find the balance left and the reimbursement.", "Balance 60 000 − 46 800 = 13 200. Reimbursement 46 800. After refund 13 200 + 46 800 = 60 000."),
        PQ("Give two reasons why a business uses a petty cash book.", "It keeps small payments out of the main cash book, so that book is shorter and clearer; and a junior employee handles small cash while the vouchers give control."),
        PQ("Analysis totals for a month are: postage 4 000; fares 9 500; refreshments 3 500. Total spent is 17 000. State the posting of the analysis totals.",
           "Debit Postage 4 000, debit Travel 9 500, debit Refreshments 3 500. Credit the main cash book (reimbursement) 17 000 (4 000 + 9 500 + 3 500 = 17 000)."),
        SUM("Petty cash covers small payments; the petty cash book is a book of original entry.",
            "Under the imprest system the float is fixed and the refund equals the amount spent.",
            "Every payment is backed by a voucher and entered in the total column and an analysis column.",
            "Cash left plus the amount spent equals the float.",
            "The analysis totals are debited to the expense accounts; the refund is a payment in the main cash book."),
    ],
))

# ------------------------------------------------------------------ 5. Bank reconciliation statements
_cb, _chg, _so, _dc, _dh = 312000, 4000, 15000, 30000, 20000
_upd = _cb - _chg - _so + _dc - _dh
_unp = 45000 + 28000
_unc = 60000
_stmt = _upd + _unp - _unc
assert _upd == 303000 and _unp == 73000 and _stmt == 316000
assert _stmt - _unp + _unc == _upd                      # working back from the statement gives the updated cash book

def _line(label, amt, w=54, neg=False):
    v = "(" + m(amt) + ")" if neg else m(amt)
    return label.ljust(w - 11) + v.rjust(11)

def _rule(w=54):
    return "-" * w

_UPDATE = "\n".join([
    _line("Balance per cash book (bank column)", _cb),
    _line("Less: bank charges", _chg, neg=True),
    _line("Less: standing order, insurance", _so, neg=True),
    _line("Add: direct credit from E. Fon", _dc),
    _line("Less: dishonoured cheque", _dh, neg=True),
    _rule(),
    _line("Updated cash book balance", _upd),
    _rule()])
_REC1 = "\n".join([
    "Bank reconciliation statement at 31 December",
    _line("Balance per updated cash book", _upd),
    _line("Add: unpresented cheques (45 000 + 28 000)", _unp),
    _rule(),
    _line("", _upd + _unp),
    _line("Less: uncredited lodgments", _unc, neg=True),
    _rule(),
    _line("Balance per bank statement", _stmt),
    _rule()])
_BACK = "\n".join([
    _line("Balance per bank statement", _stmt),
    _line("Less: unpresented cheques", _unp, neg=True),
    _line("Add: uncredited lodgments", _unc),
    _rule(),
    _line("Updated cash book balance", _stmt - _unp + _unc),
    _rule()])
# overdraft example
_o_cb, _o_unp, _o_unc = -18000, 20000, 12000
_o_stmt = _o_cb + _o_unp - _o_unc
assert _o_stmt == -10000
_OVER = "\n".join([
    _line("Balance per cash book (overdrawn)", 18000, neg=True),
    _line("Add: unpresented cheques", _o_unp),
    _rule(),
    _line("", abs(_o_cb + _o_unp)),
    _line("Less: uncredited lodgments", _o_unc, neg=True),
    _rule(),
    _line("Balance per bank statement (overdrawn)", 10000, neg=True),
    _rule()])
assert _o_cb + _o_unp == 2000 and 2000 - 12000 == -10000
_w = [28, 18, 19]
_RULES = "\n".join([
    fmt_row(["Item", "Update cash book?", "On reconciliation"], _w), "-" * 67,
    fmt_row(["Bank charges, interest", "Yes: credit bank", "-"], _w),
    fmt_row(["Standing order, direct debit", "Yes: credit bank", "-"], _w),
    fmt_row(["Direct credit from customer", "Yes: debit bank", "-"], _w),
    fmt_row(["Dishonoured cheque", "Yes: credit bank", "-"], _w),
    fmt_row(["Unpresented cheque", "No", "Add to balance"], _w),
    fmt_row(["Uncredited lodgment", "No", "Deduct from balance"], _w)])

LESSONS.append(lesson(
    module=M_CASH,
    topic=T_BANK,
    title="Bank reconciliation statements",
    slug="acc2-bank-reconciliation-statements",
    minutes=25,
    summary="A bank reconciliation statement explains the difference between the bank balance in the cash book and the bank statement. First update the cash book for items only the bank knew; then bridge the updated balance to the statement with timing differences.",
    objectives=[
        "Explain why the cash book and the bank statement usually disagree",
        "Update the cash book for bank charges, standing orders, direct credits and dishonoured cheques",
        "Prepare a reconciliation statement using unpresented cheques and uncredited lodgments",
        "Handle an overdraft and avoid transposing the entries",
    ],
    key_concepts=["Bank statement", "Updated cash book", "Unpresented cheque", "Uncredited lodgment", "Standing order", "Direct credit", "Dishonoured cheque", "Bank reconciliation statement"],
    blocks=[
        H("Introduction"),
        T("At the end of December a shop in Douala looks at its cash book and sees a bank balance of 312 000. The bank statement says 316 000. Is somebody wrong? "
          "Usually not. The shop and the bank keep two records of the same account, and each hears about some transactions before the other. A **bank reconciliation statement** explains the difference."),
        D("A **bank statement** is the bank's own record of a customer's account, sent to the customer. A **bank reconciliation statement** is a "
          "calculation prepared by the business to show that the balance in its cash book and the balance on the bank statement differ only for known reasons.", title="Reconciliation"),
        KEY("The bank's point of view", "The bank statement is written from the bank's side.", cards=[
            ["Our cash book", "A balance in the bank is an asset for us: a DEBIT balance in our cash book."],
            ["The bank's books", "The same money is a liability for the bank: a CREDIT balance on the statement."],
        ], note="Candidates often copy cash book entries into the bank statement or the other way round. A deposit is a debit in our cash book but a credit on the statement."),
        H("Why the two balances differ"),
        T("Some items are on the bank statement but not yet in the cash book. We must correct the cash book for them. Other items are in the cash book but have not reached the bank "
          "statement because of timing. These are the reconciling items."),
        CODE(_RULES, "text", title="Where each item goes",
             caption="The first four are errors of omission in our own cash book. The last two are only timing differences."),
        D("An **unpresented cheque** is a cheque the business has written and entered in its cash book but that the payee has not yet taken to the bank, so the bank has not paid it.", title="Unpresented cheque"),
        D("An **uncredited lodgment** is money the business has paid into the bank and entered in its cash book, but the bank has not yet shown on the statement (for example a deposit made late in the day).", title="Uncredited lodgment"),
        H("The two steps"),
        T("Step 1: compare the statement with the cash book. Tick items that appear in both. Everything on the statement that is not in the cash book goes into the cash book, giving the **updated cash book balance**. "
          "Step 2: take the updated balance and add the unpresented cheques and deduct the uncredited lodgments. The result must equal the balance on the bank statement."),
        T("The shop's cash book has a bank balance of 312 000 (debit). The statement balance is 316 000. The statement shows bank charges 4 000; a standing order for insurance 15 000; a direct credit from customer E. Fon 30 000; "
          "and a customer cheque of 20 000 that was dishonoured. The cash book shows two cheques written but not yet cleared: 45 000 and 28 000. A deposit of 60 000 was banked on 31 December and is not yet on the statement."),
        CODE(_UPDATE, "text", title="Step 1: update the cash book", caption="The new balance is 303 000."),
        CODE(_REC1, "text", title="Step 2: the reconciliation statement",
             caption="The result agrees with the bank statement balance of 316 000."),
        IMG("f5acc2-bank-reconciliation.svg", alt="Four boxes: updated cash book 303 000, add unpresented cheques 73 000, less uncredited lodgments 60 000, giving the bank statement balance 316 000.",
            caption="Figure 1. The reconciliation as a bridge from the updated cash book to the bank statement."),
        EX("Worked example 1: update and reconcile", intro="Use the figures above.", steps=[
            S("Update the cash book", math=r"312\,000 - 4\,000 - 15\,000 + 30\,000 - 20\,000 = 303\,000",
              text="Charges, the standing order and the dishonoured cheque reduce our bank money. The direct credit increases it."),
            S("Unpresented cheques", math=r"45\,000 + 28\,000 = 73\,000", text="The bank has not paid them yet, so the bank still shows this money."),
            S("Add and deduct", math=r"303\,000 + 73\,000 - 60\,000 = 316\,000",
              text="The deposit is not yet on the statement, so it is deducted. The result equals the statement balance."),
        ]),
        EX("Worked example 2: start from the statement", intro="Prove the same thing the other way round.", steps=[
            S("Reverse the adjustments", math=r"316\,000 - 73\,000 + 60\,000 = 303\,000",
              text="Deduct unpresented cheques and add uncredited lodgments. The answer is the updated cash book balance."),
        ]),
        CODE(_BACK, "text", title="Starting from the bank statement balance"),
        EX("Worked example 3: an overdraft", intro="The updated cash book shows the business overdrawn by 18 000. Unpresented cheques are 20 000 and uncredited lodgments 12 000. What does the bank statement show?", steps=[
            S("Start with a negative balance", math=r"-18\,000"),
            S("Add unpresented cheques", math=r"-18\,000 + 20\,000 = 2\,000"),
            S("Deduct uncredited lodgments", math=r"2\,000 - 12\,000 = -10\,000",
              text="The statement shows an overdraft of 10 000."),
        ]),
        CODE(_OVER, "text", title="Overdraft reconciliation", caption="Brackets mean the business owes the bank."),
        TIP("After step 1 the cash book is your starting figure. Only unpresented cheques and uncredited lodgments are used in step 2. A cheque dishonoured or a bank charge is never an unpresented cheque."),
        MISTAKE("Transposing the entries", "Do not copy the bank column of the cash book on to the statement or the statement on to the cash book, and do not reverse debit and credit. Start from one balance and bridge to the other."),
        MISTAKE("Adjusting the wrong balance for a timing item", "Unpresented cheques and uncredited lodgments are timing differences. They do not change the cash book; they only appear in the reconciliation."),
        MISTAKE("Forgetting the signs for an overdraft", "When the balance is overdrawn, treat it as negative, then add or deduct the same items as before."),
        QUIZ("Which item requires an entry in the cash book?", [
            "An unpresented cheque", "An uncredited lodgment", "Bank charges shown on the statement", "A cheque written and entered in the cash book"], 2,
             "Bank charges are known only to the bank. The business must enter them (credit bank) in its cash book.",
             hint="Which item did the business not know about until the statement came?",
             feedback=["Already in the cash book.", "Already in the cash book.", "", "Already in the cash book."]),
        QUIZ("Updated cash book balance 80 000. Unpresented cheques 12 000. Uncredited lodgments 20 000. The bank statement shows", [
            "112 000", "72 000", "88 000", "92 000"], 1,
             "80 000 + 12 000 − 20 000 = 72 000.", hint="Add the unpresented cheques and deduct the lodgments.",
             feedback=["Both items were added.", "", "Items were reversed: 80 000 − 12 000 + 20 000.", "The lodgments were ignored: 80 000 + 12 000."], title="Quick check 2"),
        TIP("The Board's 2023 report for 0505 says bank reconciliation is regularly tested, that many candidates had little mastery of it, and that some transposed the entries between the cash book and the statement. Practise it until the two steps are automatic."),
        PQ("Cash book bank balance 150 000. Statement shows a direct debit of 8 000 and bank interest charged 2 000 not yet in the cash book; unpresented cheques 25 000. Find the statement balance.",
           "Updated cash book 150 000 − 8 000 − 2 000 = 140 000. Add unpresented cheques: 140 000 + 25 000 = 165 000 on the statement."),
        PQ("A cheque for 20 000 received from a customer was banked and has bounced. What entry does the business make?", "Credit the bank column of the cash book 20 000 and debit the customer's account 20 000 (the debt is restored)."),
        PQ("Updated cash book balance 303 000. Statement balance 316 000. Unpresented cheques total 73 000. What lodgments are uncredited?", "303 000 + 73 000 − uncredited = 316 000, so uncredited = 376 000 − 316 000 = 60 000."),
        SUM("The cash book and the bank statement keep the same account from two sides; the statement is a credit when we have money.",
            "Step 1: update the cash book for items only the bank knew: charges, standing orders, direct credits and dishonoured cheques.",
            "Step 2: updated cash book balance + unpresented cheques − uncredited lodgments = balance on the bank statement.",
            "Timing items never change the cash book.",
            "For an overdraft use negative numbers and the same rules."),
    ],
))

# ------------------------------------------------------------------ 6. Control accounts
_hd = [("Item", "FCFA"), ("Item", "FCFA")]
_s, _sb, _, _ = ledger_auto(
    [22, 9], [22, 9],
    [("Bal. b/d (debit bal.)", 180000), ("Credit sales", 640000), ("Dishonoured cheques", 12000), ("Bal. c/d (credit bal.)", 5000)],
    [("Bal. b/d (credit bal.)", 4000), ("Cash and cheques", 560000), ("Discount allowed", 14000), ("Returns inwards", 26000),
     ("Bad debts written off", 8000), ("Contra: PLCA", 20000)],
    bal_cols=[1], bd="Bal. b/d (debit bal.)", cd="Bal. c/d (debit bal.)", heads=_hd)
assert _sb[1] == 205000 and 180000 + 640000 + 12000 + 5000 == 837000 and 4000 + 560000 + 14000 + 26000 + 8000 + 20000 + 205000 == 837000
_SLCA = "SALES LEDGER CONTROL ACCOUNT (total debtors)\n" + _s

_p, _pb, _, _ = ledger_auto(
    [22, 9], [22, 9],
    [("Bal. b/d (debit bal.)", 2000), ("Cash and cheques paid", 410000), ("Discount received", 9000), ("Returns outwards", 18000), ("Contra: SLCA", 20000)],
    [("Bal. b/d (credit bal.)", 150000), ("Credit purchases", 480000), ("Bal. c/d (debit bal.)", 3000)],
    bal_cols=[1], bd="Bal. b/d (credit bal.)", cd="Bal. c/d (credit bal.)", heads=_hd)
assert _pb[1] == -174000 and 2000 + 410000 + 9000 + 18000 + 20000 == 459000 and 150000 + 480000 + 3000 == 633000 and 633000 - 459000 == 174000
_PLCA = "PURCHASES LEDGER CONTROL ACCOUNT (total creditors)\n" + _p
_TOT = 205000 - 203000
assert 120000 + 420000 + 8000 + 15000 - 90000 == 473000

_p3, _, _, _ = ledger_auto(
    [22, 9], [22, 9],
    [("Bal. b/d", 90000), ("Credit sales (missing)", 473000)],
    [("Cash and cheques", 420000), ("Discount allowed", 8000), ("Returns inwards", 15000)],
    bal_cols=[1], bd="Bal. b/d", cd="Bal. c/d", heads=_hd)
_MISS = _p3

LESSONS.append(lesson(
    module=M_CTRL,
    topic=T_CTRL,
    title="Sales and purchases ledger control accounts",
    slug="acc2-control-accounts",
    minutes=25,
    summary="A control account summarises many personal accounts in one total account. The sales ledger control account holds total debtors and the purchases ledger control account holds total creditors; only credit transactions are included.",
    objectives=[
        "Explain what a control account is and why it is kept",
        "Prepare a sales ledger control account and a purchases ledger control account",
        "Treat credit balances in the debtors ledger and debit balances in the creditors ledger correctly",
        "Handle contra items and leave out cash sales and cash purchases",
    ],
    key_concepts=["Control account", "Total debtors", "Total creditors", "Contra item", "Credit balances b/d", "Missing figure"],
    blocks=[
        H("Introduction"),
        T("A wholesaler in Bafoussam has 200 customers who buy on credit. Each has a personal account in the sales ledger. At the end of the month the trial balance does not balance. "
          "Which of the 200 accounts holds the error? Searching them all takes days. A **control account** gives the wholesaler a single account whose closing balance should equal the total of the 200 balances. If it does not, the error is in the ledger."),
        D("A **control account** (or total account) is an account that summarises the totals of many personal accounts in one ledger. The **sales ledger control account** (total debtors; "
          "in SYSCOHADA the customers' group account, class 4) and the **purchases ledger control account** (total creditors; suppliers' group account) are the two most common.", title="Control account"),
        KEY("What a control account does", "It is a check and a safeguard.", cards=[
            ["Locates errors", "If the control balance does not equal the sum of the individual balances, there is an error to find."],
            ["Gives totals quickly", "Total debtors and total creditors are known without adding every account."],
            ["Helps stop fraud", "One person can keep the control account while another keeps the personal accounts."],
        ]),
        H("What goes in the sales ledger control account"),
        T("Include only transactions that change the personal accounts of debtors: **credit** sales, money received from debtors, discount allowed to debtors, returns inwards, bad debts written off and similar items. "
          "The figures come from the books of original entry: the total of the sales journal, the returns inwards journal, the cash book (debtors column and discount allowed), and the general journal."),
        KEY("Sales ledger control account", "The same rules as for any account: items that increase debtors on the debit side; items that reduce them on the credit side.", cards=[
            ["Debit side", "Opening debit balances, credit sales, dishonoured cheques, closing credit balances (customers who have overpaid)."],
            ["Credit side", "Cash and cheques received from debtors, discount allowed, returns inwards, bad debts written off, contra with the purchases ledger, opening credit balances, closing debit balances."],
        ]),
        D("A **contra item** (set-off) arises when a person is both a customer and a supplier. Instead of paying each other, the two debts are set off against each other. "
          "It is credited in the sales ledger control account and debited in the purchases ledger control account.", title="Contra item"),
        D("**Cash sales and cash purchases are never entered in control accounts**, because they do not create debtors or creditors. The Board's 2023 report for 0505 records that candidates included cash purchases and cash sales, did not understand contra items, and mishandled the balances given.", title="Candidate mistake"),
        CODE(_SLCA, "text", title="Sales ledger control account (FCFA)", caption="Both an opening credit balance (4 000) and a closing credit balance (5 000) are shown on their own sides."),
        EX("Worked example 1: the closing balance", intro="Find the closing total debtors from the account above.", steps=[
            S("Debit side", math=r"180\,000 + 640\,000 + 12\,000 + 5\,000 = 837\,000", text="Opening debit balances, credit sales, the dishonoured cheque and the credit balances carried down."),
            S("Credit side before the balance", math=r"4\,000 + 560\,000 + 14\,000 + 26\,000 + 8\,000 + 20\,000 = 632\,000"),
            S("Balance c/d", math=r"837\,000 - 632\,000 = 205\,000", text="Total debtors with debit balances is 205 000. It is brought down on the debit side. The credit balances of 5 000 are shown separately."),
        ]),
        H("The purchases ledger control account"),
        T("This mirrors the sales account. Credit purchases, the opening credit balances and closing debit balances go on the credit side. Payments to suppliers, discount received, returns outwards and the contra go on the debit side."),
        CODE(_PLCA, "text", title="Purchases ledger control account (FCFA)", caption="The contra of 20 000 appears on the debit side here and on the credit side in the sales ledger control account."),
        EX("Worked example 2: total creditors", intro="Find the closing credit balances of the purchases ledger.", steps=[
            S("Debit side", math=r"2\,000 + 410\,000 + 9\,000 + 18\,000 + 20\,000 = 459\,000"),
            S("Credit side before the balance", math=r"150\,000 + 480\,000 + 3\,000 = 633\,000"),
            S("Balance c/d", math=r"633\,000 - 459\,000 = 174\,000", text="Total creditors is 174 000. It is a credit balance, brought down on the credit side."),
        ]),
        H("Finding a missing figure"),
        T("A control account can also be used to find an unknown figure, such as credit sales. A trader has opening debtors of 90 000, closing debtors of 120 000, received 420 000 from debtors, allowed discount of 8 000 and had returns inwards of 15 000."),
        CODE(_MISS, "text", title="Finding credit sales", caption="The missing figure is the one that makes the two sides equal."),
        EX("Worked example 3: credit sales", intro="Find the credit sales for the year.", steps=[
            S("Credit side items", math=r"420\,000 + 8\,000 + 15\,000 + 120\,000 = 563\,000", text="Include the closing balance as the balancing figure on the credit side."),
            S("Debit side known item", text="Opening debtors 90 000."),
            S("Missing figure", math=r"563\,000 - 90\,000 = 473\,000", text="Credit sales are 473 000."),
        ]),
        TIP("Before you start, copy the list of balances given into two groups: those from the sales ledger and those from the purchases ledger. Place each on its own side of the right account, and never mix them."),
        MISTAKE("Including cash sales", "Cash sales do not make a debtor. They are in the sales account and the cash book, not in the control account."),
        MISTAKE("Ignoring the contra", "A contra is entered twice, once in each control account. Forgetting it leaves both closing balances wrong by the same amount."),
        MISTAKE("Putting a credit balance b/d on the debit side", "A debtor with a credit balance (an overpayment) belongs on the credit side of the sales ledger control account at the start, and on the debit side at the end."),
        QUIZ("Which item is NOT entered in the sales ledger control account?", [
            "Credit sales", "Returns inwards", "Cash sales", "Discount allowed"], 2,
             "Cash sales do not create debtors, so they stay out of the control account.",
             hint="Which of these do not involve a customer who owes?",
             feedback=["Credit sales create debtors.", "Returns reduce what debtors owe.", "", "Discount allowed reduces debtors."]),
        QUIZ("A person owes you 15 000 for goods. You owe the same person 15 000 for stock. By agreement the two debts are set off. In the sales ledger control account this is a", [
            "debit of 15 000", "credit of 15 000", "credit of 30 000", "no entry"], 1,
             "The debt owed by the customer is cancelled, so the debtor total falls: credit the sales ledger control account. The matching debit is in the purchases ledger control account.",
             hint="Does the debtor total go up or down?",
             feedback=["That would increase debtors.", "", "Only 15 000 is set off.", "The set-off changes both control accounts."], title="Quick check 2"),
        TIP("Paper 2 of the 2023 session included a question on control accounts, in which both the debtors' and creditors' accounts were to be prepared. Paper 1 asks what goes on which side and what to leave out."),
        PQ("Opening debtors 60 000. Credit sales 200 000. Cash sales 80 000. Cash from debtors 170 000. Discount allowed 5 000. Returns inwards 10 000. Find closing debtors.",
           "Leave out the cash sales. Debit side: 60 000 + 200 000 = 260 000. Credit side: 170 000 + 5 000 + 10 000 = 185 000. Closing debtors: 260 000 − 185 000 = 75 000."),
        PQ("Opening creditors 40 000. Credit purchases 150 000. Payments to creditors 120 000. Discount received 4 000. Returns outwards 6 000. Find closing creditors.",
           "Credit side: 40 000 + 150 000 = 190 000. Debit side: 120 000 + 4 000 + 6 000 = 130 000. Closing creditors: 190 000 − 130 000 = 60 000."),
        PQ("The sales ledger control account closes with 205 000. The list of the personal balances adds up to 203 000. What does this tell you?",
           "The 2 000 difference means an error: an item was posted wrongly to a personal account or to the control account, or a balance was added wrongly. The error must be found."),
        SUM("A control account summarises many personal accounts; its balance should agree with the list of personal balances.",
            "Only credit transactions with debtors (or creditors) are included; cash sales and cash purchases are left out.",
            "Sales ledger control: debit credit sales; credit receipts, discount allowed, returns inwards, bad debts, contra.",
            "Purchases ledger control is the mirror image.",
            "A contra appears in both control accounts, on opposite sides; the missing figure balances the account."),
    ],
))

# ------------------------------------------------------------------ 7. Errors not disclosed by the trial balance
def jrn(entries, w=(30, 10, 10)):
    """entries: list of (heading, [(account, amount, 'Dr'|'Cr'), ...]). Checks debits = credits."""
    out = []
    for head, lines in entries:
        assert sum(a for _, a, s in lines if s == "Dr") == sum(a for _, a, s in lines if s == "Cr"), head
        out.append(head)
        for acc, amt, side in lines:
            if side == "Dr":
                out.append(fmt_row(["  Dr " + acc, amt, None], w))
            else:
                out.append(fmt_row(["      Cr " + acc, None, amt], w))
        out.append("")
    return "\n".join(out).rstrip()

_J7a = jrn([
    ("(a) Omission: credit sale of 30 000 to M. Etoa not recorded", [("M. Etoa", 30000, "Dr"), ("Sales", 30000, "Cr")]),
    ("(b) Commission: 25 000 from Nkeng put in Nkemeng's account", [("Nkemeng", 25000, "Dr"), ("Nkeng", 25000, "Cr")]),
    ("(c) Principle: van 2 400 000 debited to Motor Expenses", [("Motor Vehicles", 2400000, "Dr"), ("Motor Expenses", 2400000, "Cr")]),
])
_J7b = jrn([
    ("(d) Original entry: invoice of 54 000 recorded as 45 000", [("Debtor", 9000, "Dr"), ("Sales", 9000, "Cr")]),
    ("(e) Compensating: Sales and Purchases both overcast by 10 000", [("Sales", 10000, "Dr"), ("Purchases", 10000, "Cr")]),
    ("(f) Reversal: 18 000 from debtor T debited to T, credited to cash", [("Cash book", 36000, "Dr"), ("T (debtor)", 36000, "Cr")]),
])
assert 54000 - 45000 == 9000 and 2 * 18000 == 36000
_profit0 = 3150000
_adj = [("Van charged to Motor Expenses (principle)", 2400000), ("Repair of 30 000 charged to Motor Vehicles", -30000),
        ("Invoice undercast by 9 000 (original entry)", 9000), ("Sale of 30 000 omitted", 30000)]
_profit1 = _profit0 + sum(a for _, a in _adj)
assert _profit1 == 5559000
_W7 = (46, 12)
_STAT7 = "\n".join(
    [fmt_row(["Net profit per draft accounts", _profit0], _W7)] +
    [fmt_row([("Add: " if a > 0 else "Less: ") + n, abs(a)], _W7) for n, a in _adj] +
    ["-" * 59, fmt_row(["Corrected net profit", _profit1], _W7), "-" * 59])

LESSONS.append(lesson(
    module=M_CTRL,
    topic=T_ERR1,
    title="Errors not disclosed by the trial balance",
    slug="acc2-errors-not-disclosed-by-trial-balance",
    minutes=24,
    summary="Six kinds of error leave the trial balance in balance: omission, commission, principle, original entry, compensating errors and complete reversal. Each is put right with a correcting journal entry, and some change the profit.",
    objectives=[
        "Explain why a balanced trial balance does not prove the books are right",
        "Name and recognise the six errors not disclosed by the trial balance",
        "Write the correcting journal entry for each",
        "Adjust profit for errors that affect it",
    ],
    key_concepts=["Error of omission", "Error of commission", "Error of principle", "Error of original entry", "Compensating error", "Complete reversal", "Correcting journal entry"],
    blocks=[
        H("Introduction"),
        T("A shopkeeper in Limbe prepares her trial balance and both totals are 8 450 000. She sighs with relief. But a customer's payment went into the wrong account and nobody has noticed. "
          "A balanced trial balance only shows that total debits equal total credits. It does not prove that every entry is in the right account or has the right amount."),
        D("An **error not disclosed by the trial balance** is a mistake that does not change the equality of total debits and total credits, so the trial balance still agrees. "
          "These errors are found by checking, by the bank reconciliation, by control accounts or by people querying a statement.", title="Errors not disclosed"),
        KEY("The six errors", "Remember them as: O C P O C R.", cards=[
            ["Omission", "A transaction is left out completely. Both the debit and the credit are missing."],
            ["Commission", "The right type of account is used but the wrong account: for example a debtor, but the wrong one."],
            ["Principle", "An item is put in the wrong class of account: a capital item as an expense, or private spending as a business expense."],
            ["Original entry", "A wrong amount is used for both the debit and the credit."],
            ["Compensating", "Two separate errors of the same size on opposite sides cancel each other."],
            ["Complete reversal", "The correct accounts are used but the debit and credit are swapped."],
        ]),
        H("Examples of each error"),
        T("**Omission.** A credit sale of 30 000 to M. Etoa is never entered in the sales journal. No debit and no credit are made. The trial balance agrees but both Sales and Etoa's debt are 30 000 too low."),
        T("**Commission.** A cheque of 25 000 from Nkeng is credited to the account of Nkemeng, a different debtor with a similar name. Debits equal credits, but two personal accounts are wrong."),
        T("**Principle.** The purchase of a delivery van for 2 400 000 is debited to Motor Expenses instead of Motor Vehicles. A fixed asset has been treated as an expense, so profit is understated."),
        T("**Original entry.** An invoice of 54 000 is read as 45 000 and entered at 45 000 in both the debtor's account and the sales account. The debit and credit agree, but both are 9 000 short."),
        T("**Compensating.** The Sales account is overcast (added up too high) by 10 000, and the Purchases account is also overcast by 10 000. The errors cancel in the trial balance."),
        T("**Complete reversal.** Debtor T pays 18 000. The clerk debits T's account and credits cash, instead of debiting cash and crediting T. The totals still agree."),
        H("Correcting journal entries"),
        T("Every correction is made through the **general journal** with a narration, never by crossing out the old figures. To correct, write the entry that cancels the wrong effect and puts in the right one."),
        CODE(_J7a, "text", title="Correcting entries (a) to (c)", caption="Dr and Cr show the side of each account. In each journal the debits equal the credits."),
        CODE(_J7b, "text", title="Correcting entries (d) to (f)", caption="For a complete reversal the entry is double the amount: it removes the wrong entry and then makes the right one."),
        EX("Worked example 1: error of commission", intro="Nkeng's cheque of 25 000 was credited to Nkemeng. Write the correction.", steps=[
            S("What happened", text="Credit Nkemeng 25 000 (wrong). It should have been credit Nkeng 25 000."),
            S("Cancel the wrong credit", text="Debit Nkemeng 25 000. This makes his account right again."),
            S("Make the right credit", text="Credit Nkeng 25 000."),
            S("Check", text="Debit 25 000 = credit 25 000. Total debtors do not change."),
        ]),
        EX("Worked example 2: complete reversal", intro="18 000 received from T was debited to T and credited to cash. Show why the correction is 36 000.", steps=[
            S("Position now", text="Cash is 18 000 lower than before and T's account is 18 000 higher (the opposite of what should have happened)."),
            S("Position needed", text="Cash 18 000 higher, T's account 18 000 lower."),
            S("Difference", math=r"18\,000 + 18\,000 = 36\,000", text="So debit Cash 36 000 and credit T 36 000."),
        ]),
        H("Errors and profit"),
        T("Some errors change profit and some do not. Errors of commission between two personal accounts, and complete reversals between balance sheet accounts, do not change profit. "
          "Errors that affect an income or expense account usually do: an omitted or understated sale, or an asset treated as an expense. A compensating error may or may not change profit; it depends on the accounts involved."),
        CODE(_STAT7, "text", title="Correcting net profit (FCFA)",
             caption="For this exercise cost of sales is ignored. Profit was understated by the van and the invoice and sale; it was overstated by the capitalised repair."),
        EX("Worked example 3: corrected profit", intro="Draft net profit is 3 150 000. Correct it for the errors in the statement.", steps=[
            S("Van treated as expense", math=r"+\,2\,400\,000", text="Expenses were too high, so profit was too low. Add back."),
            S("Repair charged to the asset", math=r"-\,30\,000", text="Expenses were too low, so profit was too high. Deduct."),
            S("Invoice and omitted sale", math=r"+\,9\,000 + 30\,000", text="Sales were too low, so add."),
            S("Total", math=r"3\,150\,000 + 2\,400\,000 - 30\,000 + 9\,000 + 30\,000 = 5\,559\,000"),
        ]),
        TIP("To find the correcting entry, say what was done, say what should have been done, then write the entry that moves from one to the other."),
        MISTAKE("Thinking a balanced trial balance means no errors", "These six errors leave it balanced. The trial balance only shows arithmetic agreement of the double entry."),
        MISTAKE("Using the suspense account for these errors", "None of these errors affects the trial balance totals, so no suspense account is needed. Correct them through the journal."),
        MISTAKE("Correcting a reversal with the single amount", "A complete reversal needs twice the original amount, because the wrong entry must first be cancelled."),
        QUIZ("The purchase of office furniture was debited to Purchases. This is an error of", [
            "omission", "commission", "principle", "original entry"], 2,
             "An asset (furniture) was treated as an expense (purchases of goods for resale). It is a wrong class of account.",
             hint="Was it the wrong account of the same class, or the wrong class?",
             feedback=["Something was entered; it was not left out.", "Commission is the wrong account in the same class (personal, real or nominal).", "", "The amount was right."]),
        QUIZ("A rent payment of 18 000 was entered as 8 100 in the cash book and the rent account. The correcting entry is", [
            "Dr Rent 9 900, Cr Cash 9 900", "Dr Cash 9 900, Cr Rent 9 900", "Dr Rent 18 000, Cr Cash 18 000", "Dr Rent 8 100, Cr Cash 8 100"], 0,
             "Rent and cash were both understated by 18 000 − 8 100 = 9 900. The correction debits Rent and credits Cash for 9 900.",
             hint="Find the difference between the right and wrong amounts.",
             feedback=["", "The sides are reversed.", "That would repeat the whole payment.", "That would repeat the wrong amount."], title="Quick check 2"),
        TIP("In Paper 2 you may be asked to name the type of error, write the journal and show the effect on profit. In Paper 1, expect to be given a transaction and asked which error type it is."),
        PQ("A credit purchase of 52 000 from a supplier was not entered in any book. Name the error and give the correcting entry.", "Error of omission. Debit Purchases 52 000; credit the supplier's account 52 000."),
        PQ("Rent of 40 000 was posted to the Rates account. Name the error and give the correction. Does profit change?", "Commission (wrong account of the same kind, both expenses). Debit Rent 40 000, credit Rates 40 000. Profit does not change."),
        PQ("A credit sale of 27 000 was entered as 72 000 in both sales and the debtor's account. Name the error, correct it and say how profit changes.",
           "Error of original entry. Debit Sales 45 000, credit the debtor 45 000 (72 000 − 27 000 = 45 000). Profit falls by 45 000, because sales were overstated."),
        SUM("A balanced trial balance does not prove the books are right.",
            "The six errors not disclosed are omission, commission, principle, original entry, compensating and complete reversal.",
            "Each is corrected through the general journal with a narration.",
            "A complete reversal is corrected with twice the original amount.",
            "Errors on income or expense accounts change profit; errors between personal accounts do not."),
    ],
))

# ------------------------------------------------------------------ 8. The suspense account and errors disclosed
_dr8, _cr8 = 6486000, 6500000
_diff8 = _cr8 - _dr8
assert _diff8 == 14000
_TB8 = "\n".join([
    fmt_row(["Trial balance totals", "Debit", "Credit"], (26, 10, 10)), "-" * 48,
    fmt_row(["Totals as extracted", _dr8, _cr8], (26, 10, 10)),
    fmt_row(["Suspense (difference)", _diff8, None], (26, 10, 10)), "-" * 48,
    fmt_row(["Totals agree", _dr8 + _diff8, _cr8], (26, 10, 10)), "-" * 48])
assert _dr8 + _diff8 == _cr8
_J8 = jrn([
    ("(1) Rent 40 000 not posted to the Rent account (one side only)", [("Rent", 40000, "Dr"), ("Suspense", 40000, "Cr")]),
    ("(2) Sales account overcast by 10 000", [("Sales", 10000, "Dr"), ("Suspense", 10000, "Cr")]),
    ("(3) Sale of 62 000 credited to Sales as 26 000", [("Suspense", 36000, "Dr"), ("Sales", 36000, "Cr")]),
])
_s8, _sb8, _, _ = ledger_auto(
    [24, 9], [24, 9],
    [("Difference per TB", 14000), ("Sales (error 3)", 36000)],
    [("Rent (error 1)", 40000), ("Sales (error 2)", 10000)],
    bal_cols=[1], heads=[("SUSPENSE ACCOUNT", "FCFA"), ("", "FCFA")])
assert _sb8[1] == 0 and 14000 + 36000 == 50000 == 40000 + 10000
assert 62000 - 26000 == 36000 and 36000 % 9 == 0
assert 40000 + 10000 - 36000 == 14000                          # net effect of the three errors equals the difference
assert 900000 - 40000 - 10000 + 36000 == 886000
_STAT8 = "\n".join([
    fmt_row(["Net profit per draft accounts", 900000], (40, 10)),
    fmt_row(["Less: rent not posted", 40000], (40, 10)),
    fmt_row(["Less: sales overcast", 10000], (40, 10)),
    fmt_row(["Add: sale credited at 26 000 not 62 000", 36000], (40, 10)),
    "-" * 51, fmt_row(["Corrected net profit", 886000], (40, 10)), "-" * 51])
_J8b = jrn([("Purchases returns of 7 500 not credited to the Purchases Returns account", [("Suspense", 7500, "Dr"), ("Purchases Returns", 7500, "Cr")])])
assert 2750000 - 2742500 == 7500

LESSONS.append(lesson(
    module=M_CTRL,
    topic=T_ERR2,
    title="The suspense account and errors disclosed by the trial balance",
    slug="acc2-suspense-account-and-disclosed-errors",
    minutes=25,
    summary="When a trial balance will not agree, the difference is placed in a suspense account. Each error found is corrected by a journal entry that uses the suspense account, until its balance is nil. Errors that cause the difference are those that change the debits or the credits only.",
    objectives=[
        "Name errors that the trial balance discloses",
        "Open a suspense account for a trial balance difference and on which side",
        "Write correcting journal entries involving the suspense account",
        "Check that the suspense account closes to nil and adjust profit",
    ],
    key_concepts=["Suspense account", "Trial balance difference", "Single-sided entry", "Transposition error", "Casting error", "Correcting journal"],
    blocks=[
        H("Introduction"),
        T("It is late. The trial balance totals should be equal but they are not. The debit total is 6 486 000 and the credit total is 6 500 000. "
          "The accountant cannot wait to find the error before the accounts are needed, so she opens a **suspense account** to hold the difference until it is explained."),
        D("A **suspense account** is a temporary account in which the difference on a trial balance is placed so that the trial balance agrees, until the errors causing it are found and corrected.", title="Suspense account"),
        H("Errors that the trial balance discloses"),
        KEY("What makes a trial balance disagree", "These errors upset the equality of total debits and credits.", cards=[
            ["One-sided posting", "Only the debit or only the credit of a transaction was posted."],
            ["Different amounts", "The debit and the credit were posted with different amounts; a transposition (digits swapped, such as 62 as 26) is a common cause."],
            ["Addition errors", "A column was added up wrongly (casting error), or a balance was carried forward wrongly."],
            ["Trial balance slips", "A balance was left out, entered twice or put on the wrong side when the trial balance was drawn up."],
        ], note="A difference divisible by 9 often points to transposed digits. This is a clue, not a proof."),
        H("Which side is the suspense account?"),
        T("The suspense account is the balancing figure. If the credit total is bigger, put the difference on the **debit** side of the suspense account (and the debit column of the trial balance). If the debit total is bigger, it goes on the credit side."),
        CODE(_TB8, "text", title="Trial balance with suspense", caption="The credit total is 14 000 larger, so suspense is a debit of 14 000."),
        T("Three errors are found: (1) rent of 40 000 paid by cheque was entered in the cash book but not posted to the Rent account; (2) the Sales account was overcast by 10 000; "
          "(3) a credit sale of 62 000 was correctly debited to the customer but credited to Sales as 26 000."),
        CODE(_J8, "text", title="Correcting entries", caption="Each entry involves the suspense account because each error upset the trial balance."),
        CODE(_s8, "text", title="The suspense account after the corrections", caption="Both sides total 50 000, so the account balance is nil."),
        EX("Worked example 1: one error at a time", intro="Show how each error affects the suspense account.", steps=[
            S("Error 1", text="The debit of 40 000 to Rent was missing, so debits were short. Debit Rent 40 000 and credit Suspense 40 000, which lowers the suspense debit."),
            S("Error 2", text="Sales credits were 10 000 too high. Debit Sales 10 000 to reduce them. Credit Suspense 10 000."),
            S("Error 3", text="Sales credits were 36 000 too low (62 000 − 26 000). Credit Sales 36 000. Debit Suspense 36 000."),
            S("Check", math=r"\text{Suspense:}\; 14\,000 + 36\,000 = 40\,000 + 10\,000 = 50\,000", text="The balance is nil, so all errors causing the difference have been found."),
        ]),
        EX("Worked example 2: a credit suspense", intro="Total debits are 2 750 000 and total credits 2 742 500. Open the suspense account and clear it, given that purchases returns of 7 500 were never credited to the Purchases Returns account.", steps=[
            S("Difference", math=r"2\,750\,000 - 2\,742\,500 = 7\,500", text="Debits are larger, so suspense is a credit of 7 500."),
            S("Correction", text="Debit Suspense 7 500; credit Purchases Returns 7 500."),
            S("Result", text="The suspense balance of 7 500 credit is cancelled by the debit. It is nil."),
        ]),
        CODE(_J8b, "text", title="Correcting entry for example 2"),
        H("Effect on profit"),
        T("Errors involving income or expense accounts change profit. In the example, the Rent account was short of an expense of 40 000 (profit overstated), Sales were overstated by 10 000, and Sales were understated by 36 000."),
        CODE(_STAT8, "text", title="Correcting net profit (FCFA)", caption="Total effect: profit falls by 14 000, the same as the original suspense difference."),
        EX("Worked example 3: corrected profit", intro="Draft net profit was 900 000. Find the corrected profit.", steps=[
            S("Rent", math=r"900\,000 - 40\,000 = 860\,000", text="An unrecorded expense reduces profit."),
            S("Sales overcast", math=r"860\,000 - 10\,000 = 850\,000", text="Sales were too high."),
            S("Sale undercredited", math=r"850\,000 + 36\,000 = 886\,000", text="Sales were too low by 36 000."),
        ]),
        TIP("A suspense account must end the exercise with a nil balance. If it does not, an error is still missing. A suspense balance that is never explained must never be hidden in the final accounts."),
        MISTAKE("Using suspense for errors the trial balance does not disclose", "Omission, commission, principle, original entry, compensating and reversal errors do not cause a difference. They are corrected without suspense."),
        MISTAKE("Wrong side for the opening difference", "The side of the suspense account is the side that is short in the trial balance. If credits are bigger, debit the suspense account."),
        MISTAKE("Treating the suspense account as an asset or an expense", "It is a temporary holding account. It does not belong in the final accounts when all errors have been found."),
        QUIZ("A trial balance has debits 840 000 and credits 835 500. The suspense account is", [
            "debit 4 500", "credit 4 500", "debit 840 000", "credit 835 500"], 1,
             "The debit total is bigger, so the credit side is short by 4 500. Credit the suspense account 4 500.",
             hint="Which side needs more to agree?",
             feedback=["That is the wrong side.", "", "Only the difference is used.", "Only the difference is used."]),
        QUIZ("Which error will make the trial balance disagree?", [
            "A credit sale entered in neither book", "A payment debited to the wrong debtor", "A purchase of 8 000 debited to Purchases but credited to the supplier as 800",
             "A sale of 5 000 entered as 5 500 in both books"], 2,
             "The debit and credit have different amounts (8 000 and 800). The difference of 7 200 disagrees.",
             hint="Which entry has unequal sides?",
             feedback=["An omission leaves debits equal to credits.", "Commission leaves the totals equal.", "", "The same wrong amount on both sides leaves the totals equal."], title="Quick check 2"),
        TIP("Paper 2 questions often give a list of errors and ask you to prepare a suspense account and journal entries. Write the debit and credit for each error and check that the suspense account ends at nil."),
        PQ("A trial balance shows debits 3 120 000 and credits 3 150 000. Open the suspense account (side and amount).", "The credit total is bigger by 30 000, so the suspense account is a debit balance of 30 000."),
        PQ("The suspense account in the previous question is explained by a purchase of goods for 30 000 from a supplier that was credited to the supplier but not debited to Purchases. Write the correcting entry.",
           "Debit Purchases 30 000, credit Suspense 30 000. The suspense account is cleared."),
        PQ("A sale of 51 000 was credited to the Sales account as 15 000. Calculate the difference and say what type of error it is. Give the correcting entry if the trial balance has shown suspense.",
           "51 000 − 15 000 = 36 000 (divisible by 9, a transposition). Credit Sales 36 000 and debit Suspense 36 000."),
        SUM("A suspense account holds a trial balance difference until the errors are found.",
            "The suspense account goes on the side that is short in the trial balance.",
            "Errors that upset the totals are one-sided postings, unequal amounts, casting errors and slips in drawing up the trial balance.",
            "Each correction is a journal entry using suspense; the account must end at nil.",
            "Errors on income or expense accounts change profit."),
    ],
))

# ------------------------------------------------------------------ 9. Payroll: calculating pay
from fractions import Fraction as _Fr

def _ot(rate, hrs, mult):
    """Overtime pay as a whole number of francs (exact fraction arithmetic)."""
    v = _Fr(rate) * _Fr(hrs) * _Fr(mult)
    assert v.denominator == 1
    return int(v)

_emp = [("Ayuk", 40, 750, 8, "1.5"), ("Nkeng", 40, 900, 5, "1.5"), ("Tabe", 36, 1000, 0, "1.5")]
_pr = []
for _n, _h, _r, _o, _mu in _emp:
    _np = _h * _r
    _op = _ot(_r, _o, _Fr(_mu))
    _pr.append((_n, _h, _r, _np, _o, _op, _np + _op))
assert [r[6] for r in _pr] == [39000, 42750, 36000] and sum(r[6] for r in _pr) == 117750
_PAYSHEET = table([6, 5, 6, 8, 5, 8, 8], ["Name", "Hours", "Rate", "Normal", "OT h", "OT pay", "Gross"],
                  _pr, total=["Total", None, None, sum(r[3] for r in _pr), sum(r[4] for r in _pr), sum(r[5] for r in _pr), sum(r[6] for r in _pr)])
assert sum(r[3] for r in _pr) == 102000 and sum(r[5] for r in _pr) == 15750 and 102000 + 15750 == 117750
# Mbah: weekday overtime and Sunday double time
assert 40 * 800 == 32000 and _ot(800, 6, "1.5") == 7200 and _ot(800, 4, 2) == 6400 and 32000 + 7200 + 6400 == 45600
_MBAH = "\n".join([
    fmt_row(["Normal pay: 40 h x 800", 32000], (36, 9)),
    fmt_row(["Weekday overtime: 6 h x 800 x 1.5", 7200], (36, 9)),
    fmt_row(["Sunday overtime: 4 h x 800 x 2", 6400], (36, 9)),
    "-" * 46, fmt_row(["Gross pay", 45600], (36, 9)), "-" * 46])
assert 320 * 150 == 48000 and 180 * 120 == 21600 and max(21600, 25000) == 25000
assert 150000 + 20000 + 15000 + 12000 == 197000
assert 40 * 600 + _ot(600, 4, "1.5") == 27600 and 38 * 500 + _ot(500, 6, "1.5") == 23500 and 460 * 85 == 39100 and 180000 + 25000 + 10000 + 8000 == 223000
_SAL = "\n".join([
    fmt_row(["Basic salary", 150000], (30, 9)),
    fmt_row(["Housing allowance", 20000], (30, 9)),
    fmt_row(["Transport allowance", 15000], (30, 9)),
    fmt_row(["Overtime", 12000], (30, 9)),
    "-" * 40, fmt_row(["Gross pay", 197000], (30, 9)), "-" * 40])

LESSONS.append(lesson(
    module=M_CTRL,
    topic=T_PAY1,
    title="Payroll: calculating gross pay",
    slug="acc2-payroll-calculating-pay",
    minutes=24,
    summary="Gross pay is everything an employee earns before deductions. It is built from time-rate pay, overtime at a higher rate, piece-rate pay and allowances. Overtime rates apply only to the hours above the normal hours.",
    objectives=[
        "Define payroll, gross pay and net pay",
        "Calculate time-rate pay and overtime pay at different rates",
        "Calculate piece-rate pay, including a guaranteed minimum",
        "Prepare a simple wages sheet with totals",
    ],
    key_concepts=["Payroll", "Time rate", "Overtime", "Piece rate", "Guaranteed minimum", "Allowances", "Gross pay"],
    blocks=[
        H("Introduction"),
        T("At the end of the month a workshop owner in Douala must pay 12 employees. One is paid by the hour, one by the number of chairs made, one a monthly salary. "
          "To pay them correctly and keep proper records, she prepares a **payroll**. This lesson is about the first part: finding what each employee has earned. The next lesson deals with deductions."),
        D("**Payroll** is the process of calculating and recording what each employee is paid, and the deductions from it. The record kept is the **wages sheet** or payroll.", title="Payroll"),
        D("**Gross pay** is the total earned before any deductions: basic pay, overtime, bonuses and allowances. **Net pay** is what the employee takes home after deductions: gross pay minus deductions.", title="Gross and net pay"),
        KEY("Gross pay in one line", "Gross pay = basic pay + overtime pay + allowances (+ bonus or commission, if any).", cards=[
            ["Time rate", "Pay for hours worked: hours × rate per hour. Overtime is paid for hours above the normal hours."],
            ["Piece rate", "Pay for units produced: units × rate per unit. A guaranteed minimum may apply."],
            ["Salary", "A fixed monthly amount plus allowances and any overtime."],
        ]),
        H("Time rate and overtime"),
        T("A worker paid by the hour receives hours × hourly rate for normal hours. **Overtime** is work beyond the normal hours and is usually paid at a higher rate. "
          "The multiple is a teaching rate in this lesson: one and a half times the normal hourly rate on ordinary days (time and a half) and twice the normal rate on Sundays and public holidays (double time). "
          "These are invented for practice. Employers' rules and the labour law set the real rates, so check the current rules or the figures given in the question."),
        D("The **overtime rate** is a multiple of the normal hourly rate. 'Time and a half' means the worker is paid 1.5 times the hourly rate for each overtime hour, not 1.5 times the whole day's pay. "
          "A '50% premium' means the same: normal rate plus half as much again.", title="Overtime rate"),
        EX("Worked example 1: time rate with overtime", intro="Ayuk is paid 750 per hour for a normal week of 40 hours. Last week he worked 48 hours. Overtime is paid at time and a half (teaching rate). Find his gross pay.", steps=[
            S("Normal pay", math=r"40 \times 750 = 30\,000"),
            S("Overtime hours", math=r"48 - 40 = 8"),
            S("Overtime rate", math=r"750 \times 1.5 = 1\,125", text="The overtime rate is 1 125 per hour."),
            S("Overtime pay", math=r"8 \times 1\,125 = 9\,000"),
            S("Gross pay", math=r"30\,000 + 9\,000 = 39\,000"),
        ]),
        EX("Worked example 2: two overtime rates", intro="Mbah earns 800 per hour. In one week she worked 40 normal hours, 6 hours of weekday overtime at time and a half, and 4 hours on Sunday at double time (teaching rates). Find her gross pay.", steps=[
            S("Normal pay", math=r"40 \times 800 = 32\,000"),
            S("Weekday overtime", math=r"6 \times 800 \times 1.5 = 7\,200"),
            S("Sunday overtime", math=r"4 \times 800 \times 2 = 6\,400"),
            S("Gross pay", math=r"32\,000 + 7\,200 + 6\,400 = 45\,600"),
        ]),
        CODE(_MBAH, "text", title="Mbah's pay (FCFA, teaching rates)"),
        H("Piece rate"),
        T("A **piece-rate** worker is paid for the number of units produced. A tailor sewing school uniforms at 150 per uniform who finishes 320 uniforms earns 320 × 150 = 48 000. "
          "Some employers add a **guaranteed minimum**, so that a worker who is slow or unlucky still earns a basic wage: the pay is the larger of the piece-rate earnings and the guaranteed minimum."),
        EX("Worked example 3: piece rate with a guaranteed minimum", intro="A worker is paid 120 per unit and is guaranteed at least 25 000 a week. In one week she makes 180 units. What does she earn?", steps=[
            S("Piece-rate earnings", math=r"180 \times 120 = 21\,600"),
            S("Compare with the guarantee", text="The guarantee is 25 000, which is more than 21 600."),
            S("Gross pay", text="She is paid the guaranteed 25 000. In a week when she makes 220 units, 220 × 120 = 26 400 would exceed the guarantee and she would be paid 26 400."),
        ]),
        H("Salary with allowances"),
        CODE(_SAL, "text", title="Salary gross pay (FCFA)", caption="Allowances are part of gross pay. The next lesson shows what is then deducted."),
        H("A wages sheet"),
        T("A wages sheet lists every employee with hours, rate, normal pay, overtime and gross pay, and totals each column. The totals are useful: they give the total gross pay the business must account for."),
        CODE(_PAYSHEET, "text", title="Wages sheet, one week (FCFA)", caption="Overtime at time and a half (teaching rate). Tabe worked 36 hours, so he has no overtime."),
        EX("Worked example 4: check the totals", intro="Check the totals of the wages sheet.", steps=[
            S("Add the normal pay", math=r"30\,000 + 36\,000 + 36\,000 = 102\,000"),
            S("Add the overtime pay", math=r"9\,000 + 6\,750 + 0 = 15\,750", text="Nkeng: 5 × 900 × 1.5 = 6 750."),
            S("Cross-check the gross total", math=r"102\,000 + 15\,750 = 117\,750", text="Adding the gross column gives 39 000 + 42 750 + 36 000 = 117 750. Both ways agree."),
        ]),
        TIP("The Board's 2023 report for 0505 says many candidates scored zero on payroll and did not master overtime rates, or did not understand how they apply. Practise finding the normal hours, the overtime hours and the correct multiple."),
        MISTAKE("Paying the overtime rate on all the hours", "Only the hours above the normal hours get the higher rate. The first 40 hours are paid at the normal rate."),
        MISTAKE("Using 1.5 as the pay instead of the multiple", "Time and a half means 1.5 × the hourly rate for each overtime hour. It does not mean 1.5 hours or an extra half of the total week's pay."),
        MISTAKE("Forgetting that allowances are part of gross pay", "Housing and transport allowances are added before any deductions are calculated."),
        QUIZ("A worker earns 600 per hour. Normal week 40 hours. She works 44 hours. Overtime is at time and a half. Her gross pay is", [
            "24 000", "26 400", "28 800", "27 600"], 3,
             "Normal pay 40 × 600 = 24 000. Overtime 4 × 600 × 1.5 = 3 600. Total 27 600.",
             hint="Pay the first 40 hours at 600 and only the extra 4 at the higher rate.",
             feedback=["That ignores the overtime.", "That pays the 4 extra hours at the normal rate: 44 × 600 = 26 400.", "That pays the 4 extra hours at double time (4 × 1 200).", ""]),
        QUIZ("Which of these is included in gross pay?", [
            "Housing allowance", "Pension contributions deducted", "Income tax withheld", "Net pay"], 0,
             "Gross pay is everything earned before deductions, so allowances are included. Contributions and tax are deductions.",
             hint="Is it earned or deducted?",
             feedback=["", "A deduction, not part of gross pay.", "A deduction.", "Net pay is gross pay after deductions."], title="Quick check 2"),
        PQ("A worker is paid 500 per hour for a normal week of 38 hours and works 44 hours. Overtime is at time and a half. Find the gross pay.", "Normal 38 × 500 = 19 000. Overtime 6 hours × 500 × 1.5 = 4 500. Gross pay 23 500."),
        PQ("A piece-rate worker is paid 85 per unit and made 460 units. Find the gross pay.", "460 × 85 = 39 100."),
        PQ("A salaried employee earns basic pay 180 000, housing allowance 25 000, transport allowance 10 000 and overtime 8 000. Find the gross pay.", "180 000 + 25 000 + 10 000 + 8 000 = 223 000."),
        SUM("Gross pay is what is earned before deductions; net pay is gross pay less deductions.",
            "Time rate pay is hours × rate; overtime hours are paid at a higher multiple of the hourly rate.",
            "Piece rate pay is units × rate per unit; a guaranteed minimum is the least the employee is paid.",
            "Allowances are part of gross pay.",
            "Overtime multiples used here are teaching rates; use the figures given in the question or the current rules."),
    ],
))

# ------------------------------------------------------------------ 10. Payroll: statutory deductions
# TEACHING RATES, invented for practice. They are not the law.
R_CNPS, R_IRPP, R_CAC, R_CFC, RAV_FLAT, R_ER = _Fr(3, 100), _Fr(8, 100), _Fr(10, 100), _Fr(1, 100), 1500, _Fr(10, 100)

def _ded(g):
    cnps = R_CNPS * g
    irpp = R_IRPP * g
    cac = R_CAC * irpp
    cfc = R_CFC * g
    vals = [cnps, irpp, cac, cfc, RAV_FLAT]
    assert all(_Fr(v).denominator == 1 for v in vals)
    vals = [int(v) for v in vals]
    return vals, sum(vals), g - sum(vals)

_v, _td, _net = _ded(250000)
assert _v == [7500, 20000, 2000, 2500, 1500] and _td == 33500 and _net == 216500
_er = int(R_ER * 250000)
assert _er == 25000 and 250000 + _er == 275000
_SLIP = "\n".join([
    "PAYSLIP: A. Ayuk, March (teaching rates)",
    fmt_row(["Gross pay", 250000], (30, 10)), "Deductions:",
    fmt_row(["  CNPS 3% of gross", _v[0]], (30, 10)),
    fmt_row(["  IRPP 8% of gross", _v[1]], (30, 10)),
    fmt_row(["  CAC 10% of IRPP", _v[2]], (30, 10)),
    fmt_row(["  CFC 1% of gross", _v[3]], (30, 10)),
    fmt_row(["  CRTV / Rav (flat amount)", _v[4]], (30, 10)),
    "-" * 41, fmt_row(["Total deductions", _td], (30, 10)),
    fmt_row(["NET PAY", _net], (30, 10)), "-" * 41])
assert 250000 - 33500 == 216500
_v15, _t15, _n15 = _ded(150000)
assert _v15 == [4500, 12000, 1200, 1500, 1500] and _t15 == 20700 and _n15 == 129300 and int(R_ER * 400000) == 40000 and 200000 - 27000 == 173000
_JP = jrn([
    ("Payroll for March (employee side)", [
        ("Salaries and wages", 250000, "Dr"), ("CNPS, employee share", _v[0], "Cr"), ("IRPP payable", _v[1], "Cr"),
        ("CAC payable", _v[2], "Cr"), ("CFC payable", _v[3], "Cr"), ("CRTV / Rav payable", _v[4], "Cr"), ("Bank (net pay)", _net, "Cr")]),
    ("Employer's contribution (teaching rate 10%)", [("Employer social charges", _er, "Dr"), ("CNPS payable, employer share", _er, "Cr")]),
], w=(36, 10, 10))
_two = [("Ayuk", 180000), ("Nkeng", 320000)]
_rows, _tot = [], [0] * 8
for _n, _g in _two:
    _vv, _tdd, _nn = _ded(_g)
    _rows.append((_n, _g, *_vv, _tdd, _nn))
for _r in _rows:
    for _i in range(8):
        _tot[_i] += _r[_i + 1]
assert _tot == [500000, 15000, 40000, 4000, 5000, 3000, 67000, 433000]
assert _rows[0][1:] == (180000, 5400, 14400, 1440, 1800, 1500, 24540, 155460) and _rows[1][1:] == (320000, 9600, 25600, 2560, 3200, 1500, 42460, 277540)
assert 500000 - 67000 == 433000
_PAYR = table([6, 8, 6, 7, 5, 5, 5, 7, 8], ["Name", "Gross", "CNPS", "IRPP", "CAC", "CFC", "Rav", "Deduct", "Net"],
              _rows, total=["Total"] + _tot)

LESSONS.append(lesson(
    module=M_CTRL,
    topic=T_PAY2,
    title="Payroll: statutory deductions and net pay",
    slug="acc2-payroll-statutory-deductions",
    minutes=25,
    summary="Employers must deduct certain amounts from gross pay by law (CNPS, IRPP, CAC, CFC, CRTV/Rav) and pay them over to the bodies concerned. Net pay is gross pay less these deductions. All rates in this lesson are invented teaching rates.",
    objectives=[
        "Name the statutory deductions in the syllabus and say in general terms what each is for",
        "Calculate each deduction at the rates given in a question",
        "Find total deductions and net pay, and prepare a payslip and a payroll summary",
        "Record the payroll in a journal entry and distinguish employee deductions from the employer's own cost",
    ],
    key_concepts=["Statutory deduction", "CNPS", "IRPP", "CAC", "CFC", "CRTV / Rav", "Net pay", "Employer's contribution"],
    blocks=[
        H("Introduction"),
        T("When Ayuk looks at his payslip, the gross pay is 250 000 but the amount that reaches his bank account is smaller. The employer has taken some money off and will pass it to the "
          "bodies it belongs to. These are **statutory deductions**: deductions required by law, not chosen by the employer."),
        D("**Statutory deductions** are amounts that the law requires an employer to take from an employee's gross pay and pay over to a social fund, to the tax authority or to another body. The employer is only the collector.", title="Statutory deduction"),
        D("**Teaching-rate warning.** The names and purposes below follow the Cameroon payroll in general terms. Every percentage and amount used in calculations in this lesson is a **teaching rate invented for practice**. "
          "Real rates, bands, reliefs and ceilings change and the real IRPP is worked out on bands after allowances. In an exam, use the rates stated in the question and check the current rules in your textbook or with your teacher.", title="Not the law"),
        H("The deductions named in the syllabus"),
        KEY("What each deduction is for", "In general terms only; check the current rules.", cards=[
            ["CNPS", "Caisse Nationale de Prévoyance Sociale, the national social security fund. Contributions help to pay benefits such as pensions. The employee pays a share and the employer pays a larger share."],
            ["IRPP", "Impôt sur le Revenu des Personnes Physiques, the personal income tax on earnings. The employer withholds it from pay and pays it to the tax authority."],
            ["CAC", "Centimes Additionnels Communaux, an extra levy worked out as a percentage of the IRPP, for local councils."],
            ["CFC", "The contribution to the Crédit Foncier du Cameroun, a housing finance institution. The employee has a deduction and the employer also contributes."],
            ["CRTV / Rav", "The audiovisual fee (redevance audiovisuelle) that supports the national broadcaster, CRTV. It is often a flat amount linked to the pay band."],
        ], note="Some textbooks show CRTV and Rav as separate lines, others as one. Check your textbook. If a question gives an amount for each, deduct both."),
        H("Calculating a payslip"),
        T("Teaching rates for this lesson: CNPS 3% of gross; IRPP 8% of gross; CAC 10% of the IRPP (not of gross); CFC 1% of gross; CRTV / Rav a flat 1 500. The employer's own CNPS contribution is 10% of gross (teaching rate)."),
        CODE(_SLIP, "text", title="Payslip (FCFA)", caption="All rates are teaching rates. The CAC is a percentage of the IRPP, not of the gross pay."),
        EX("Worked example 1: one payslip", intro="Calculate each deduction and the net pay for gross pay of 250 000.", steps=[
            S("CNPS", math=r"3\% \times 250\,000 = 7\,500"),
            S("IRPP", math=r"8\% \times 250\,000 = 20\,000"),
            S("CAC", math=r"10\% \times 20\,000 = 2\,000", text="Work on the IRPP, not on the gross pay."),
            S("CFC", math=r"1\% \times 250\,000 = 2\,500"),
            S("Total deductions", math=r"7\,500 + 20\,000 + 2\,000 + 2\,500 + 1\,500 = 33\,500", text="The flat CRTV / Rav of 1 500 is the last item."),
            S("Net pay", math=r"250\,000 - 33\,500 = 216\,500"),
        ]),
        H("A payroll summary"),
        T("The wages sheet for the month lists every employee with the deductions. The totals show how much the employer must pay over to each body."),
        CODE(_PAYR, "text", title="Payroll summary (FCFA, teaching rates)", caption="Net pay total 433 000 = gross 500 000 − deductions 67 000."),
        EX("Worked example 2: check the summary", intro="Verify Nkeng's line and the totals.", steps=[
            S("Nkeng, gross 320 000", math=r"9\,600 + 25\,600 + 2\,560 + 3\,200 + 1\,500 = 42\,460",
              text="CNPS 3% = 9 600; IRPP 8% = 25 600; CAC 10% of 25 600 = 2 560; CFC 1% = 3 200; Rav 1 500."),
            S("Nkeng's net pay", math=r"320\,000 - 42\,460 = 277\,540"),
            S("Total net pay", math=r"155\,460 + 277\,540 = 433\,000", text="Check: 500 000 − 67 000 = 433 000."),
        ]),
        H("Recording the payroll"),
        T("The payroll is recorded in the journal. The gross pay is the expense. The deductions are liabilities, because the employer owes them to the bodies concerned. The net pay is paid to the employees. The employer's own contribution is an extra cost for the employer: it is not deducted from the employee."),
        CODE(_JP, "text", title="Payroll journal (teaching rates)", caption="Debits 250 000 = credits 250 000. The employer's cost is gross pay 250 000 + 25 000 = 275 000."),
        EX("Worked example 3: the employer's total cost", intro="What does Ayuk's employment cost the business for the month?", steps=[
            S("Gross pay", text="250 000, of which 33 500 is passed to other bodies and 216 500 goes to Ayuk."),
            S("Employer's CNPS contribution", math=r"10\% \times 250\,000 = 25\,000"),
            S("Total cost", math=r"250\,000 + 25\,000 = 275\,000"),
        ]),
        TIP("A question usually gives the rates and the method. Calculate every deduction from the right base (gross, or IRPP for the CAC), add them and subtract from gross to get the net pay. The Board's 2023 report found payroll one of the weakest questions."),
        MISTAKE("Calculating the CAC on gross pay", "CAC is a percentage of the IRPP. If IRPP is 20 000 and CAC is 10%, CAC is 2 000, not 25 000."),
        MISTAKE("Deducting the employer's contribution from the employee", "The employer's CNPS share is an extra cost for the employer and is not taken from the employee's pay."),
        MISTAKE("Treating deductions as the employer's income", "The employer only collects them and owes them to the bodies concerned until they are paid."),
        QUIZ("Which deduction is calculated as a percentage of another deduction?", [
            "CNPS", "CAC", "CFC", "Net pay"], 1,
             "The CAC is an extra levy worked out as a percentage of the IRPP.",
             hint="One of these has 'additional' in its name.",
             feedback=["CNPS is based on gross pay.", "", "CFC is based on gross pay here.", "Net pay is a result, not a deduction."]),
        QUIZ("Gross pay 200 000. Total deductions 27 000. The net pay is", [
            "227 000", "173 000", "27 000", "200 000"], 1,
             "200 000 − 27 000 = 173 000.", hint="Net pay is the take-home amount.",
             feedback=["That adds the deductions.", "", "That is the deductions.", "That is the gross pay."], title="Quick check 2"),
        PQ("Gross pay is 150 000. Teaching rates: CNPS 3%, IRPP 8%, CAC 10% of IRPP, CFC 1%, CRTV / Rav 1 500. Find the net pay.",
           "CNPS 4 500; IRPP 12 000; CAC 1 200; CFC 1 500; Rav 1 500. Total 20 700. Net pay 150 000 − 20 700 = 129 300."),
        PQ("An employer pays gross wages of 400 000 and its own CNPS contribution is 10% (teaching rate). Find the employer's total cost.", "10% × 400 000 = 40 000. Total cost 440 000."),
        PQ("Explain in one sentence each what the CNPS and the IRPP are for.", "CNPS: a social security fund whose contributions help pay benefits such as pensions. IRPP: personal income tax withheld from pay and paid to the tax authority."),
        SUM("Statutory deductions are required by law: CNPS, IRPP, CAC, CFC and the CRTV / Rav fee are the ones in the syllabus.",
            "The employer collects them and owes them to the bodies concerned.",
            "Net pay = gross pay − total deductions; CAC is a percentage of the IRPP.",
            "The employer's own contribution is an extra cost for the employer.",
            "All percentages used here are teaching rates; use the rates given in the question and check the current rules."),
    ],
))
