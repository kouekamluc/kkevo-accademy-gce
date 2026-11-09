"""Form 5 Principles of Accounts (O Level 0505): practice sets for End-of-Year Adjustments & Inventory Valuation,
Final Accounts & Specialized Accounts and the Examination module, with two mock papers.

Draft content. Exam facts are only those of the Board's 2023 report for 0505: Paper 1 is 50 multiple-choice questions
(1 hour 30 minutes, 40%); Paper 2 has eight questions of 20 marks, Section A five OHADA questions (any three) and
Section B three IAS/IFRS questions (any two), 3 hours, 60%. The mock papers use KKEVO practice settings. The Paper 2
practice paper is a structured version with numeric and multiple-choice parts because essays cannot be auto-marked.
All FCFA figures are invented for practice. Every answer and every distractor figure below is computed by this file with
plain integer arithmetic (the distractors are the results of the typical wrong methods).
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("principles-of-accounts", "form-5")

M_ADJ = "End-of-Year Adjustments & Inventory Valuation"
M_FIN = "Final Accounts & Specialized Accounts"
M_EXAM = "Examination"


def n(x):
    s = f"{abs(x):,}".replace(",", " ")
    return ("-" if x < 0 else "") + s


class _Bag:
    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.items = []

    def next(self):
        if not self.items:
            self.items = [0, 1, 2, 3]
            self.rng.shuffle(self.items)
        return self.items.pop()


BAG = _Bag(1)


def use(seed):
    global BAG
    BAG = _Bag(seed)


def Q(prompt, correct, wrongs, steps, concept, skill, hint, pos=None):
    """Four-option MC. `wrongs` = [(text, why)] x3; the correct option goes to a balanced position."""
    assert len(wrongs) == 3
    texts = [correct] + [t for t, _ in wrongs]
    assert len(set(texts)) == 4, texts
    pos = BAG.next() if pos is None else pos
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(correct, correct=True))
    return MC(prompt, choices, steps=[S(a, text=b) for a, b in steps], concept=concept, skill=skill, hint=hint)


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit="FCFA"):
    return NUM(prompt, answer, steps=[S(a, text=b) for a, b in steps], tolerance=tol, unit=unit, concept=concept,
               skill=skill, hint=hint)


def NM(prompt, answer, wrongs, steps, concept, skill, hint):
    """A numeric question set as four-option MC. `wrongs` = [(number, why)] x3 (results of typical wrong methods)."""
    return Q(prompt, F_(answer), [(F_(v), w) for v, w in wrongs], steps, concept, skill, hint)


def F_(x):
    return f"FCFA {n(x)}"


# exact topic titles ---------------------------------------------------------------------------------------------
T_CONCEPTS = "Accounting concepts and conventions"
T_CHART = "The SYSCOHADA chart of accounts"
T_EQUATION = "The accounting equation"
T_DOUBLE = "Double entry and ledger posting"
T_TB = "The trial balance"
T_INVOICE = "Invoices, trade discount and financial discount"
T_VAT = "VAT, transport and returnable containers"
T_PSJ = "Purchases and sales journals"
T_RETJ = "Returns journals"
T_GJ = "The general journal"
T_CB1 = "Single and two-column cash books"
T_CB3 = "The three-column cash book"
T_CBA = "The analytical cash book"
T_PETTY = "The petty cash book"
T_BANKREC = "Bank reconciliation statements"
T_CONTROL = "Control accounts"
T_ERR_ND = "Errors not disclosed by the trial balance"
T_SUSP = "The suspense account and errors disclosed"
T_PAY1 = "Payroll: calculating pay"
T_PAY2 = "Payroll: statutory deductions"
T_DEP = "Depreciation methods"
T_DISP = "Disposal of fixed assets"
T_BAD = "Bad debts and provision for doubtful debts"
T_ACC = "Accruals and prepayments"
T_INV = "Inventory valuation: FIFO and weighted average cost"
T_IS = "The OHADA income statement"
T_BS = "The OHADA balance sheet"
T_INC = "Incomplete records and single entry"
T_NPO = "Accounts of non-profit organizations"
T_MAN = "Manufacturing accounts"
T_DEPT = "Departmental accounts"

SETS = []

# ================================================================== 1. Depreciation methods
use(11)
_a = (2_400_000 - 400_000) // 5
_b1 = 800_000 * 20 // 100
_b2 = (800_000 - _b1) * 20 // 100
_c = (1_500_000 - 150_000) * 4 // 15
_d = 900_000 - 900_000 * 10 // 100 * 3
_e = 1_600_000 * 75 * 75 * 75 // 1_000_000
assert (_a, _b1, _b2, _c, _d, _e) == (400_000, 160_000, 128_000, 360_000, 630_000, 675_000)
assert (1_500_000 - 150_000) % 15 == 0 and 1_600_000 * 75 ** 3 % 1_000_000 == 0
SETS.append(practice_set(
    module=M_ADJ, topic=T_DEP, title="Depreciation: straight-line, reducing balance and SYD",
    lesson="acc3-depreciation-methods", questions=[
        Q("Depreciation of a fixed asset is best described as",
          "the spreading of the cost of the asset over its useful life",
          [("a payment of cash to replace the asset", "No cash moves when depreciation is recorded."),
           ("the fall in the market price of the asset each year", "Depreciation allocates cost; it does not measure market price."),
           ("an increase in the value of the asset", "Depreciation reduces the net book value.")],
          [("Idea", "Depreciation shares the cost of the asset over the years in which it earns income.")],
          T_DEP, "Recall", "Think of why a business does not charge the whole cost in year 1."),
        NM(f"A machine costs {F_(2_400_000)}, residual value {F_(400_000)}, useful life 5 years. Find the yearly straight-line charge.",
          _a, [(480000, "That ignores the residual value."), (2000000, "That is the total to depreciate, not divided by the life."), (800000, "That divides by 3 years instead of 5.")], [("Formula", "(cost - residual value) / life"), ("Calculate", "(2 400 000 - 400 000) / 5 = 400 000")],
          T_DEP, "Calculation", "Subtract the residual value before dividing."),
        Q("The correct double entry for the yearly depreciation charge is",
          "debit Depreciation expense; credit Accumulated depreciation",
          [("debit Accumulated depreciation; credit Depreciation expense", "The sides are reversed."),
           ("debit Bank; credit Depreciation expense", "Depreciation involves no cash."),
           ("debit Fixed asset; credit Depreciation expense", "The asset is not debited; depreciation is accumulated in its own account.")],
          [("Expense", "The charge is an expense, so it is debited."), ("Accumulated depreciation", "It builds up as a credit balance.")],
          T_DEP, "Concept", "Which account is the expense?"),
        NM(f"Equipment costing {F_(800_000)} is depreciated at 20% reducing balance. Find the charge for year 2.",
          _b2, [(160000, "That is the year 1 charge, 20% of the cost."), (640000, "That is the NBV after year 1, not a charge."), (32000, "That applies 20% to the year 1 charge.")], [("Year 1", "20% x 800 000 = 160 000; NBV = 640 000"), ("Year 2", "20% x 640 000 = 128 000")],
          T_DEP, "Calculation", "Apply the rate to the net book value at the start of the year."),
        N(f"An asset costs {F_(1_500_000)} with residual value {F_(150_000)} and a life of 5 years. Find the sum-of-the-years'-digits charge for year 2.",
          _c, [("Sum of digits", "5 + 4 + 3 + 2 + 1 = 15"), ("Base", "1 500 000 - 150 000 = 1 350 000"), ("Year 2", "4/15 x 1 350 000 = 360 000")],
          T_DEP, "Calculation", "In year 2, four years of life remain at the start of the year."),
        NM(f"An asset costing {F_(900_000)} is depreciated at 10% a year on cost (straight-line). Find its net book value after 3 years.",
          _d, [(270000, "That is the accumulated depreciation, not the NBV."), (810000, "That subtracts only one year's charge."), (900000, "That is the cost.")], [("Yearly charge", "10% x 900 000 = 90 000"), ("Accumulated", "3 x 90 000 = 270 000"), ("NBV", "900 000 - 270 000 = 630 000")],
          T_DEP, "Calculation", "NBV = cost minus accumulated depreciation."),
        Q("Over the whole life of an asset, the total depreciation by straight-line and by SYD is",
          "the same: cost minus residual value",
          [("larger for SYD, because early charges are bigger", "The yearly pattern differs but the total does not."),
           ("larger for straight-line, because it is even", "Both methods write off the same total."),
           ("equal to the cost, whatever the residual value", "The residual value is not depreciated.")],
          [("Both methods", "They allocate cost - residual value in different patterns."), ("Total", "The totals are equal.")],
          T_DEP, "Reasoning", "Add up the charges in a small example."),
        N(f"A vehicle costing {F_(1_600_000)} is depreciated at 25% reducing balance. Find its net book value at the end of year 3.",
          _e, [("Year 1", "NBV = 75% x 1 600 000 = 1 200 000"), ("Year 2", "75% x 1 200 000 = 900 000"), ("Year 3", "75% x 900 000 = 675 000")],
          T_DEP, "Application", "Each year the NBV is 75% of the previous NBV."),
    ]))

# ================================================================== 2. Disposal of fixed assets
use(12)
_g1 = 800_000 - 500_000
_g2 = 250_000 - _g1
_h = 2_400_000 - 2_400_000 * 25 // 100 * 2
_h2 = 1_000_000 - _h
_i = 1_200_000 - (900_000 - 600_000)
_i2 = 1_200_000 - 350_000
assert (_g1, _g2, _h, _h2, _i, _i2) == (300_000, -50_000, 1_200_000, -200_000, 900_000, 850_000)
SETS.append(practice_set(
    module=M_ADJ, topic=T_DISP, title="Disposal: profit, loss and part-exchange",
    lesson="acc3-disposal-of-fixed-assets", questions=[
        Q("The net book value of an asset at the date of sale is",
          "cost minus accumulated depreciation",
          [("cost plus accumulated depreciation", "Depreciation reduces the book value."),
           ("the sale price", "The sale price is compared with the NBV to find profit or loss."),
           ("cost minus the sale price", "That is not the book value.")],
          [("Definition", "NBV = cost - accumulated depreciation up to the date of sale.")],
          T_DISP, "Recall", "Think of what the balance sheet shows for the asset."),
        N(f"An asset cost {F_(800_000)} and has accumulated depreciation of {F_(500_000)}. Find its net book value.",
          _g1, [("Calculate", "800 000 - 500 000 = 300 000")], T_DISP, "Calculation", "Subtract the accumulated depreciation from cost."),
        Q(f"An asset with cost {F_(800_000)} and accumulated depreciation {F_(500_000)} is sold for {F_(250_000)}. The result is",
          "a loss of FCFA 50 000",
          [("a profit of FCFA 250 000", "That compares the proceeds with zero."),
           ("a profit of FCFA 50 000", "Proceeds are below the NBV, so it is a loss."),
           ("a loss of FCFA 550 000", "That compares the proceeds with cost, not the NBV.")],
          [("NBV", "300 000"), ("Result", "250 000 - 300 000 = -50 000, a loss of 50 000")],
          T_DISP, "Calculation", "Compare the proceeds with the NBV."),
        Q("In a disposal account, a profit on disposal appears",
          "as the balancing figure on the debit side",
          [("as the balancing figure on the credit side", "A loss is the credit balancing figure."),
           ("on the credit side with the proceeds", "The proceeds are credited, but the profit is the debit balancing figure."),
           ("in the bank account", "The bank account only holds the cash received.")],
          [("Debit side", "Cost is debited"), ("Credit side", "Accumulated depreciation and proceeds are credited"), ("Balance", "A debit balancing figure is a profit")],
          T_DISP, "Concept", "Which side already holds the asset's cost?"),
        N(f"A van cost {F_(2_400_000)} and was depreciated at 25% a year on cost for 2 years. Find its net book value at disposal.",
          _h, [("Yearly charge", "25% x 2 400 000 = 600 000"), ("Accumulated", "2 x 600 000 = 1 200 000"), ("NBV", "2 400 000 - 1 200 000 = 1 200 000")],
          T_DISP, "Calculation", "Find the accumulated depreciation first."),
        Q(f"A van with cost {F_(2_400_000)} and accumulated depreciation {F_(1_200_000)} is sold for {F_(1_000_000)}. The loss on disposal is",
          "FCFA 200 000",
          [("FCFA 1 400 000", "That compares the proceeds with the cost."),
           ("FCFA 1 000 000", "That is the sale price, not the loss."),
           ("FCFA 400 000", "That uses twice the correct difference.")],
          [("NBV", "1 200 000"), ("Loss", "1 200 000 - 1 000 000 = 200 000")],
          T_DISP, "Calculation", "Subtract the proceeds from the NBV."),
        N(f"Equipment cost {F_(1_200_000)}; accumulated depreciation {F_(900_000)}. It is part-exchanged with an allowance of {F_(350_000)} against new equipment costing {F_(1_200_000)}. Find the cash to pay for the new equipment.",
          _i2, [("Rule", "Allowance is part of the price of the new asset"), ("Cash to pay", "1 200 000 - 350 000 = 850 000")],
          T_DISP, "Application", "The allowance reduces the amount you pay."),
        Q("Equipment with cost FCFA 1 200 000 and accumulated depreciation FCFA 900 000 is part-exchanged with an allowance of FCFA 350 000. The result on the old equipment is",
          "a profit of FCFA 50 000",
          [("a loss of FCFA 50 000", "The allowance is higher than the NBV of 300 000."),
           ("a profit of FCFA 350 000", "That uses the allowance alone."),
           ("a profit of FCFA 900 000", "That is the accumulated depreciation, not the result.")],
          [("NBV", "1 200 000 - 900 000 = 300 000"), ("Result", "350 000 - 300 000 = 50 000 profit")],
          T_DISP, "Application", "Treat the allowance as the proceeds."),
    ]))

# ================================================================== 3. Bad debts and provision
use(13)
_p1 = (500_000 - 20_000) * 4 // 100
_p2 = 19_200 - 12_000
_p5 = (700_000 - 20_000) - (700_000 - 20_000) * 5 // 100
_p7 = 50_000 + (1_000_000 - 50_000) * 4 // 100 - 30_000
assert (_p1, _p2, _p5, _p7) == (19_200, 7_200, 646_000, 58_000) and (500_000 - 20_000) * 4 % 100 == 0
SETS.append(practice_set(
    module=M_ADJ, topic=T_BAD, title="Bad debts and provision for doubtful debts",
    lesson="acc3-bad-debts-and-provisions", questions=[
        Q("A bad debt is",
          "an amount owed by a customer that cannot be recovered, written off as an expense",
          [("an estimate of debts that may go bad", "That describes the provision for doubtful debts."),
           ("a debt the business owes to a supplier", "That is a payable, not a bad debt."),
           ("a debt that is paid late", "A late payment is still recoverable.")],
          [("Bad debt", "A known loss: debit Bad debts, credit the customer's account.")],
          T_BAD, "Recall", "Think of a customer who has disappeared."),
        NM(f"Receivables are {F_(500_000)}. Bad debts of {F_(20_000)} are written off. A provision of 4% of the remaining receivables is required. Find the new provision.",
          _p1, [(20000, "That applies 4% to 500 000 before the write-off."), (480000, "That is the remaining receivables, not the provision."), (800, "That applies 4% to the bad debt of 20 000.")], [("Remaining receivables", "500 000 - 20 000 = 480 000"), ("Provision", "4% x 480 000 = 19 200")],
          T_BAD, "Calculation", "Write off the bad debts before applying the percentage."),
        Q("The double entry to write off a bad debt is",
          "debit Bad debts; credit the customer's account",
          [("debit the customer's account; credit Bad debts", "That would increase what the customer owes."),
           ("debit Bank; credit Bad debts", "No cash is received."),
           ("debit Provision for doubtful debts; credit Bank", "No cash moves, and the provision is a different entry.")],
          [("Expense", "The loss is debited to Bad debts."), ("Customer", "The customer's account is credited to remove the debt.")],
          T_BAD, "Concept", "Which account shows the loss?"),
        N(f"The provision for doubtful debts was {F_(12_000)} and must now be {F_(19_200)}. What is charged to the income statement for the change in the provision?",
          _p2, [("Change", "19 200 - 12 000 = 7 200 increase"), ("Entry", "Charge the increase as an expense")],
          T_BAD, "Calculation", "Only the change is charged."),
        N(f"Receivables are {F_(700_000)}. A bad debt of {F_(20_000)} is written off and a 5% provision is kept on the rest. Find the net receivables for the balance sheet.",
          _p5, [("After write-off", "700 000 - 20 000 = 680 000"), ("Provision", "5% x 680 000 = 34 000"), ("Net", "680 000 - 34 000 = 646 000")],
          T_BAD, "Application", "Subtract the provision once, after the write-off."),
        Q("The provision for doubtful debts falls from FCFA 38 000 to FCFA 30 000. The entry is",
          "debit Provision for doubtful debts 8 000; credit the income statement 8 000",
          [("debit the income statement 8 000; credit Provision for doubtful debts 8 000", "That would be an increase."),
           ("debit Bad debts 8 000; credit the customer's account 8 000", "That writes off a customer."),
           ("debit Bank 8 000; credit Provision for doubtful debts 8 000", "No cash is involved.")],
          [("Decrease", "38 000 - 30 000 = 8 000"), ("Entry", "Reduce the provision and credit profit")],
          T_BAD, "Concept", "A smaller provision increases profit."),
        N(f"Receivables are {F_(1_000_000)}. A bad debt of {F_(50_000)} is written off; the provision is 4% of the remaining receivables. The old provision was {F_(30_000)}. Find the total charge for doubtful debts in the income statement.",
          _p7, [("New provision", "4% x 950 000 = 38 000"), ("Increase", "38 000 - 30 000 = 8 000"), ("Total", "50 000 + 8 000 = 58 000")],
          T_BAD, "Application", "Add the bad debt and the increase in the provision."),
        Q("A customer whose debt was written off last year pays FCFA 10 000 this year. The entries are",
          "debit the customer's account and credit Bad debts recovered; then debit Bank and credit the customer's account",
          [("debit Bad debts and credit Bank", "That would record a new loss."),
           ("credit Bank and debit Provision for doubtful debts", "The provision is not involved."),
           ("no entry, because the debt was already written off", "The recovery must be recorded as income.")],
          [("Reopen", "Debit the customer, credit Bad debts recovered (income)"), ("Receipt", "Debit Bank, credit the customer")],
          T_BAD, "Reasoning", "The recovery is a gain."),
    ]))

# ================================================================== 4. Accruals and prepayments
use(14)
_q2 = 300_000 - 50_000
_q3 = 480_000 + 40_000
_q5 = 120_000 - 120_000 * 3 // 12
_q6 = 60_000 - 15_000
_q8 = 400_000 - 20_000 + 30_000 + 10_000
assert (_q2, _q3, _q5, _q6, _q8) == (250_000, 520_000, 90_000, 45_000, 420_000)
SETS.append(practice_set(
    module=M_ADJ, topic=T_ACC, title="Accruals and prepayments",
    lesson="acc3-accruals-and-prepayments", questions=[
        Q("The accrual (matching) concept says that",
          "expenses and incomes belong to the year in which they are incurred or earned, not the year of payment",
          [("expenses are recorded only when paid", "That is the cash basis."),
           ("profit is the cash received less the cash paid", "Cash flow is not the same as profit."),
           ("assets are valued at their market price", "That is a different convention.")],
          [("Matching", "Match each cost and income to the period it relates to.")],
          T_ACC, "Recall", "Think of an electricity bill paid in the next year."),
        NM(f"Rent paid in the year is {F_(300_000)}, of which {F_(50_000)} is for next year. Find the rent expense for the year.",
          _q2, [(350000, "That adds the prepayment instead of removing it."), (300000, "That ignores the prepayment."), (50000, "That is the prepayment only.")], [("Remove the prepayment", "300 000 - 50 000 = 250 000")], T_ACC, "Calculation", "Which part belongs to next year?"),
        NM(f"Wages paid are {F_(480_000)} and {F_(40_000)} of wages for the last week are unpaid. Find the wages expense.",
          _q3, [(440000, "That subtracts the accrual."), (480000, "That ignores the accrual."), (40000, "That is the accrual only.")], [("Add the accrual", "480 000 + 40 000 = 520 000")], T_ACC, "Calculation", "The unpaid wages also belong to this year."),
        Q("An accrued expense is shown on the balance sheet as",
          "a current liability",
          [("a current asset", "An accrued expense is owed, so it is a liability."),
           ("a fixed asset", "It is not a long-term resource."),
           ("part of capital", "It is not owner's equity.")],
          [("Accrual", "The business owes the money, so it is a liability.")],
          T_ACC, "Concept", "Does the business owe or is it owed?"),
        NM(f"On 1 October a business pays {F_(120_000)} for 12 months of insurance. The year end is 31 December. Find the prepayment at the year end.",
          _q5, [(30000, "That is the expense for 3 months, not the prepayment."), (120000, "That is the whole payment."), (40000, "That uses 4 months instead of 9.")], [("Months used", "3 months = 30 000"), ("Prepaid", "120 000 - 30 000 = 90 000")], T_ACC, "Application", "Nine months remain."),
        N(f"Interest received in the year is {F_(60_000)}, of which {F_(15_000)} is for next year. Find the interest income for the year.",
          _q6, [("Remove the part in advance", "60 000 - 15 000 = 45 000")], T_ACC, "Calculation", "Income received in advance belongs to next year."),
        Q("Income received in advance, compared with the cash received, causes the profit for the year to",
          "be lower, because that income belongs to next year",
          [("be higher, because the cash is already in the bank", "Cash received is not the year's income."),
           ("stay the same, because no entry is needed", "An adjustment is needed."),
           ("become a loss", "It reduces profit but does not itself create a loss.")],
          [("Effect", "The income for the year is cash received minus the advance")],
          T_ACC, "Reasoning", "Subtract it from the income."),
        N(f"Profit before adjustments is {F_(400_000)}. A bill of {F_(20_000)} is accrued, insurance of {F_(30_000)} is prepaid and commission of {F_(10_000)} is earned but not received. Find the corrected profit.",
          _q8, [("Accrual", "400 000 - 20 000 = 380 000"), ("Prepayment", "+ 30 000 = 410 000"), ("Accrued income", "+ 10 000 = 420 000")],
          T_ACC, "Application", "Decide whether each item raises or lowers profit."),
    ]))

# ================================================================== 5. Inventory valuation
use(15)
_r2 = 120_000 + 800_000 - 150_000
_r3 = (50 * 400 + 150 * 600) // 200
_r4 = 30 * 250
_r5a = (40 * 200 + 60 * 250) // 100
_r5 = 30 * _r5a
_r8 = 350 * ((200 * 500 + 300 * 600) // 500)
assert (_r2, _r3, _r4, _r5a, _r5, _r8) == (770_000, 550, 7_500, 230, 6_900, 196_000)
assert (50 * 400 + 150 * 600) % 200 == 0 and (200 * 500 + 300 * 600) % 500 == 0
SETS.append(practice_set(
    module=M_ADJ, topic=T_INV, title="Inventory: FIFO and weighted average cost",
    lesson="acc3-inventory-fifo-weighted-average", questions=[
        Q("The FIFO method of valuing inventory assumes that",
          "the oldest goods are sold first, so the goods left are the most recent purchases",
          [("the newest goods are sold first", "That describes LIFO, not FIFO."),
           ("all goods are valued at the average of all prices", "That is the weighted average method."),
           ("goods are valued at selling price", "Inventory is valued at cost (or lower NRV).")],
          [("FIFO", "First in, first out: the oldest cost leaves first.")],
          T_INV, "Recall", "Read the initials: first in, first out."),
        NM(f"Opening inventory {F_(120_000)}, purchases {F_(800_000)}, closing inventory {F_(150_000)}. Find the cost of goods sold.",
          _r2, [(1070000, "That adds the closing inventory instead of subtracting it."), (920000, "That ignores the closing inventory."), (150000, "That is the closing inventory only.")], [("Formula", "opening + purchases - closing"), ("Calculate", "120 000 + 800 000 - 150 000 = 770 000")],
          T_INV, "Calculation", "Closing inventory is subtracted."),
        N("Stock is 50 units at FCFA 400, then 150 units are bought at FCFA 600. Find the weighted average cost per unit after the purchase (in FCFA).",
          _r3, [("Total cost", "50 x 400 + 150 x 600 = 20 000 + 90 000 = 110 000"), ("Units", "200"), ("Average", "110 000 / 200 = 550")],
          T_INV, "Calculation", "Divide total cost by total units.", unit="FCFA per unit"),
        NM("Opening stock 40 units at FCFA 200; bought 60 units at FCFA 250; 70 units sold. By FIFO, find the value of the closing inventory (FCFA).",
          _r4, [(6900, "That is the weighted average value."), (8000, "That values 40 units at the oldest price of 200."), (6000, "That values the 30 units left at 200.")], [("Units left", "100 - 70 = 30"), ("Which layer", "The oldest 40 and 30 of the 250 layer are sold, so 30 at 250 remain"), ("Value", "30 x 250 = 7 500")],
          T_INV, "Calculation", "Which layer is sold first?"),
        N("Using the same data (40 units at FCFA 200, then 60 units at FCFA 250, 70 sold), find the closing inventory by weighted average cost after all entries (FCFA).",
          _r5, [("Total cost", "8 000 + 15 000 = 23 000"), ("Average", "23 000 / 100 = 230"), ("Closing", "30 x 230 = 6 900")],
          T_INV, "Calculation", "Find one average for the whole period."),
        Q("Goods cost FCFA 30 000. They can be sold for FCFA 28 000 with selling costs of FCFA 3 000. In inventory they are valued at",
          "FCFA 25 000",
          [("FCFA 30 000", "Inventory is valued at the lower of cost and NRV."),
           ("FCFA 28 000", "Selling costs must be subtracted to find the NRV."),
           ("FCFA 31 000", "That adds the selling costs; they are subtracted.")],
          [("NRV", "28 000 - 3 000 = 25 000"), ("Lower of cost and NRV", "25 000")],
          T_INV, "Application", "Net realisable value = selling price - costs to sell."),
        Q("When purchase prices are rising, FIFO compared with weighted average cost usually gives",
          "a higher closing inventory and a higher profit",
          [("a lower closing inventory and a higher profit", "A lower closing inventory would raise the cost of goods sold."),
           ("a higher closing inventory and a lower profit", "A higher closing inventory lowers the cost of goods sold, raising profit."),
           ("the same closing inventory and the same profit", "The methods give different values when prices change.")],
          [("FIFO", "Leaves the newest, dearer goods in stock"), ("Effect", "Higher closing inventory, lower cost of goods sold, higher profit")],
          T_INV, "Reasoning", "Which prices are left in stock under FIFO?"),
        N("Receipts: 200 units at FCFA 500 and 300 units at FCFA 600. 350 units are issued. Using the weighted average after all entries, find the value of the issues (FCFA).",
          _r8, [("Total cost", "100 000 + 180 000 = 280 000"), ("Average", "280 000 / 500 = 560"), ("Issues", "350 x 560 = 196 000")],
          T_INV, "Application", "The same average is used for the issues and for the closing stock."),
    ]))

# ================================================================== 6. OHADA income statement: layout
use(16)
_s2 = (5_200_000 - 200_000) - 3_100_000
_s3 = 200_000 + 900_000 + 20_000 - 30_000 - 250_000
_s5 = _s2 - 600_000
_s8 = 800_000 - 150_000 - 30_000 - 40_000
assert (_s2, _s3, _s5, _s8) == (1_900_000, 840_000, 1_300_000, 580_000)
SETS.append(practice_set(
    module=M_FIN, topic=T_IS, title="The income statement: layout and balances",
    lesson="acc3-ohada-income-statement-layout", questions=[
        Q("The OHADA income statement lists expenses",
          "by nature (purchases, services, wages, depreciation and so on)",
          [("only as one total", "Expenses are listed on separate lines."),
           ("by department", "That is a departmental account."),
           ("by function only (cost of sales, administration)", "That is the usual IAS/IFRS grouping, not the OHADA layout.")],
          [("OHADA", "Each kind of expense has its own line, which allows the stage-by-stage balances.")],
          T_IS, "Recall", "Think of the words 'by nature'."),
        NM(f"Sales are {F_(5_200_000)}, returns inwards {F_(200_000)} and cost of goods sold {F_(3_100_000)}. Find the commercial margin.",
          _s2, [(2100000, "That does not deduct the returns inwards."), (8100000, "That adds the cost of goods sold."), (1300000, "That also deducts external services (the value added).")], [("Net sales", "5 200 000 - 200 000 = 5 000 000"), ("Margin", "5 000 000 - 3 100 000 = 1 900 000")],
          T_IS, "Calculation", "Deduct returns inwards before the cost of goods sold."),
        NM(f"Opening inventory {F_(200_000)}, purchases {F_(900_000)}, carriage inwards {F_(20_000)}, returns outwards {F_(30_000)}, closing inventory {F_(250_000)}. Find the cost of goods sold.",
          _s3, [(1120000, "That ignores the returns outwards and the closing inventory."), (870000, "That adds the returns outwards instead of subtracting them."), (590000, "That subtracts the closing inventory twice.")], [("Add", "200 000 + 900 000 + 20 000 = 1 120 000"), ("Subtract", "- 30 000 - 250 000 = 840 000")],
          T_IS, "Calculation", "Carriage inwards is added to purchases; returns outwards are subtracted."),
        Q("In the OHADA layout, the balance reached after value added and after personnel costs and taxes is the",
          "gross operating surplus (EBE)",
          [("commercial margin", "The commercial margin comes first."),
           ("operating result", "That is reached after depreciation."),
           ("net result", "That is the last balance.")],
          [("Order", "Margin, value added, gross operating surplus, operating result, net result")],
          T_IS, "Recall", "Count the stages from the top."),
        NM(f"The commercial margin is {F_(1_900_000)} and external services (rent, transport, electricity) are {F_(600_000)}. There is no other income. Find the value added.",
          _s5, [(2500000, "That adds the external services."), (600000, "That is the external services only."), (1900000, "That is the commercial margin before the services.")], [("Value added", "1 900 000 - 600 000 = 1 300 000")],
          T_IS, "Calculation", "Value added = margin + other income - external services."),
        N(f"Value added is {F_(1_300_000)}. Personnel costs are {F_(500_000)} and there are no taxes. Find the gross operating surplus.",
          800_000, [("GOS", "1 300 000 - 500 000 = 800 000")],
          T_IS, "Calculation", "Subtract the personnel costs."),
        Q("Depreciation is deducted",
          "after the gross operating surplus, to reach the operating result",
          [("before value added", "Depreciation is not an external service."),
           ("from sales, before the commercial margin", "The margin only involves goods sold."),
           ("after the net result", "It is an expense that determines the net result.")],
          [("Order", "Depreciation and provisions come after the gross operating surplus")],
          T_IS, "Concept", "Which balance excludes depreciation?"),
        N(f"The gross operating surplus is {F_(800_000)}. Depreciation is {F_(150_000)}, bad debts and the provision {F_(30_000)} and interest paid {F_(40_000)}. Find the net result.",
          _s8, [("Operating result", "800 000 - 150 000 - 30 000 = 620 000"), ("Net result", "620 000 - 40 000 = 580 000")],
          T_IS, "Application", "Interest comes after the operating result."),
    ]))

# ================================================================== 7. Income statement from a trial balance
use(17)
_t1 = 900_000 + 60_000
_t2 = 240_000 - 60_000
_t3 = (2_000_000 - 500_000) * 20 // 100
_t4 = 60_000 + (1_200_000 - 60_000) * 5 // 100 - 40_000
_t6 = 1_200_000 + 9_600_000 + 150_000 - 300_000 - 1_500_000
_t7 = 300_000 - 40_000 - 10_000 + 6_000
assert (_t1, _t2, _t3, _t4, _t6, _t7) == (960_000, 180_000, 300_000, 77_000, 9_150_000, 256_000) and (1_200_000 - 60_000) * 5 % 100 == 0
SETS.append(practice_set(
    module=M_FIN, topic=T_IS, title="Preparing the income statement with adjustments",
    lesson="acc3-income-statement-from-trial-balance", questions=[
        NM(f"Wages in the trial balance are {F_(900_000)}; {F_(60_000)} of wages are owing at the year end. Find the wages expense.",
          _t1, [(840000, "That subtracts the amount owing."), (900000, "That ignores the amount owing."), (60000, "That is the amount owing only.")], [("Accrual", "900 000 + 60 000 = 960 000")], T_IS, "Calculation", "Unpaid wages also belong to the year."),
        NM(f"Insurance in the trial balance is {F_(240_000)}; {F_(60_000)} of it is prepaid. Find the insurance expense in the income statement.",
          _t2, [(300000, "That adds the prepayment."), (240000, "That ignores the prepayment."), (60000, "That is the prepayment only.")], [("Prepayment", "240 000 - 60 000 = 180 000")], T_IS, "Calculation", "Remove the part that belongs to next year."),
        NM(f"Vehicles cost {F_(2_000_000)} with accumulated depreciation of {F_(500_000)}. Depreciation is 20% reducing balance. Find the charge for the year.",
          _t3, [(400000, "That applies 20% to the cost, not the NBV."), (100000, "That applies 20% to the accumulated depreciation."), (1500000, "That is the NBV, not the charge.")], [("NBV", "2 000 000 - 500 000 = 1 500 000"), ("Charge", "20% x 1 500 000 = 300 000")], T_IS, "Calculation", "Apply the rate to the NBV."),
        Q("Which of these does NOT appear in the income statement?",
          "Drawings by the owner",
          [("Depreciation of equipment", "Depreciation is an expense."),
           ("Interest paid on a loan", "Interest is a financial charge."),
           ("Wages", "Wages are an expense.")],
          [("Drawings", "They reduce the owner's capital; they are not an expense.")],
          T_IS, "Concept", "Which item is a withdrawal by the owner?"),
        NM(f"Receivables are {F_(1_200_000)}. A bad debt of {F_(60_000)} is written off; a 5% provision is kept on the rest. The old provision was {F_(40_000)}. Find the total charge for doubtful debts.",
          _t4, [(57000, "That is the whole new provision."), (17000, "That is the change in the provision only."), (120000, "That applies 10% instead of 5%.")], [("New provision", "5% x 1 140 000 = 57 000"), ("Increase", "57 000 - 40 000 = 17 000"), ("Total", "60 000 + 17 000 = 77 000")],
          T_IS, "Application", "Bad debt plus the increase in the provision."),
        N(f"Opening inventory {F_(1_200_000)}, purchases {F_(9_600_000)}, carriage inwards {F_(150_000)}, returns outwards {F_(300_000)}, closing inventory {F_(1_500_000)}. Find the cost of goods sold.",
          _t6, [("Sum", "1 200 000 + 9 600 000 + 150 000 - 300 000 - 1 500 000 = 9 150 000")],
          T_IS, "Calculation", "Add what is bought and subtract what is returned or left."),
        N(f"A draft profit of {F_(300_000)} was calculated before three adjustments: depreciation of {F_(40_000)} not charged, rent of {F_(10_000)} owing, and insurance of {F_(6_000)} prepaid. Find the corrected profit.",
          _t7, [("Depreciation", "300 000 - 40 000 = 260 000"), ("Rent owing", "260 000 - 10 000 = 250 000"), ("Prepaid insurance", "250 000 + 6 000 = 256 000")],
          T_IS, "Application", "Which adjustments lower the profit and which raise it?"),
        Q("The same business prepares one income statement by nature (OHADA layout) and one by function (IAS/IFRS layout). The profit shown is",
          "the same in both",
          [("higher in the OHADA layout", "Only the grouping of the costs differs."),
           ("higher in the IAS/IFRS layout", "Only the grouping of the costs differs."),
           ("different, because the two systems value assets differently", "The same figures are used in both statements.")],
          [("Layouts", "They group the costs differently."), ("Profit", "Both end with the same profit.")],
          T_IS, "Reasoning", "Think about whether the transactions change."),
    ]))

# ================================================================== 8. OHADA balance sheet: layout
use(18)
_u2 = 1_000_000 + 400_000 - 150_000
_u4 = 900_000 - 300_000
_u5 = 4_200_000 - 2_700_000
_u7 = (2_000_000 - 800_000) + (3_000_000 - 1_000_000) + 700_000 + 900_000 + 600_000 + 100_000
assert (_u2, _u4, _u5, _u7) == (1_250_000, 600_000, 1_500_000, 5_500_000)
SETS.append(practice_set(
    module=M_FIN, topic=T_BS, title="The balance sheet: layout and classification",
    lesson="acc3-ohada-balance-sheet-layout", questions=[
        Q("Which of the following is a current asset?",
          "Trade receivables",
          [("Delivery van", "A van is used for several years: a fixed asset."),
           ("Capital", "Capital is the owner's claim."),
           ("Bank loan", "A loan is a liability.")],
          [("Current assets", "Will be turned into cash within a year: inventory, receivables, cash and bank.")],
          T_BS, "Recall", "Which item will become cash within a year?"),
        NM(f"Capital at 1 January is {F_(1_000_000)}, net profit {F_(400_000)}, drawings {F_(150_000)}. Find the closing equity.",
          _u2, [(1550000, "That adds the drawings."), (1400000, "That ignores the drawings."), (850000, "That subtracts the profit.")], [("Add profit", "1 000 000 + 400 000 = 1 400 000"), ("Subtract drawings", "1 400 000 - 150 000 = 1 250 000")],
          T_BS, "Calculation", "Profit adds to capital; drawings reduce it."),
        Q("A bank loan repayable in five years is shown as",
          "a long-term liability",
          [("a current liability", "Only amounts due within a year are current."),
           ("a current asset", "A loan received is owed, not owned."),
           ("part of the capital", "A loan is not the owner's money.")],
          [("Classification", "Due after more than a year: long-term (non-current) liability")],
          T_BS, "Concept", "When must the loan be repaid?"),
        N(f"Machinery cost {F_(900_000)} and accumulated depreciation is {F_(300_000)}. Find the net amount shown on the balance sheet.",
          _u4, [("Net book value", "900 000 - 300 000 = 600 000")], T_BS, "Calculation", "Show cost less depreciation."),
        NM(f"Total assets are {F_(4_200_000)} and equity is {F_(2_700_000)}. Find the total liabilities.",
          _u5, [(6900000, "That adds the two figures."), (2700000, "That is the equity."), (4200000, "That is the total assets.")], [("Equation", "Assets = equity + liabilities"), ("Liabilities", "4 200 000 - 2 700 000 = 1 500 000")], T_BS, "Calculation", "Use the accounting equation."),
        Q("Drawings made by the owner are treated in the balance sheet as",
          "a deduction from equity",
          [("an addition to equity", "Drawings reduce what belongs to the owner."),
           ("a current asset", "Drawings are not an asset."),
           ("an expense in the income statement", "Drawings are not an expense.")],
          [("Drawings", "The owner takes value out of the business, so equity falls.")],
          T_BS, "Concept", "Is the owner's share larger or smaller after drawings?"),
        N(f"Equipment cost {F_(2_000_000)} (depreciation {F_(800_000)}); vehicles cost {F_(3_000_000)} (depreciation {F_(1_000_000)}); inventory {F_(700_000)}; receivables {F_(900_000)}; bank {F_(600_000)}; cash {F_(100_000)}. Find the total assets.",
          _u7, [("Fixed assets", "1 200 000 + 2 000 000 = 3 200 000"), ("Current assets", "700 000 + 900 000 + 600 000 + 100 000 = 2 300 000"), ("Total", "5 500 000")],
          T_BS, "Application", "Use the net amounts for the fixed assets."),
        Q("In IAS/IFRS wording, the bilan is called",
          "the statement of financial position",
          [("the statement of profit or loss", "That is the compte de résultat."),
           ("the trial balance", "The trial balance is a list of ledger balances."),
           ("the cash flow summary", "That is a different statement.")],
          [("Equivalent words", "Bilan = statement of financial position")],
          T_BS, "Recall", "Which statement shows assets and liabilities at a date?"),
    ]))

# ================================================================== 9. Balance sheet from the trial balance
use(19)
_v1 = 1_000_000 - (300_000 + 100_000)
_v2 = (900_000 - 30_000) - (900_000 - 30_000) * 4 // 100
_v3 = 5_000_000 - 300_000 - 400_000
_v5 = 8_000_000 - 5_500_000 - 1_000_000
_v7 = 12_000_000 + 1_800_000 - 2_500_000
assert (_v1, _v2, _v3, _v5, _v7) == (600_000, 835_200, 4_300_000, 1_500_000, 11_300_000) and (900_000 - 30_000) * 4 % 100 == 0
SETS.append(practice_set(
    module=M_FIN, topic=T_BS, title="From the trial balance to a balanced balance sheet",
    lesson="acc3-balance-sheet-from-trial-balance", questions=[
        NM(f"Equipment cost {F_(1_000_000)}. Accumulated depreciation was {F_(300_000)} at the start and the year's charge is {F_(100_000)}. Find the net book value for the balance sheet.",
          _v1, [(700000, "That subtracts only the opening accumulated depreciation."), (900000, "That subtracts only this year's charge."), (400000, "That is the accumulated depreciation, not the NBV.")], [("Accumulated", "300 000 + 100 000 = 400 000"), ("NBV", "1 000 000 - 400 000 = 600 000")],
          T_BS, "Calculation", "Add this year's charge to the accumulated depreciation."),
        N(f"Receivables are {F_(900_000)}. A bad debt of {F_(30_000)} is written off and a 4% provision is kept on the rest. Find the net receivables.",
          _v2, [("After write-off", "870 000"), ("Provision", "4% x 870 000 = 34 800"), ("Net", "870 000 - 34 800 = 835 200")],
          T_BS, "Calculation", "Provision is calculated after the write-off."),
        NM(f"Opening capital is {F_(5_000_000)}, the net result is a loss of {F_(300_000)} and drawings are {F_(400_000)}. Find the closing equity.",
          _v3, [(4900000, "That subtracts only the drawings and adds the loss."), (4700000, "That ignores the drawings."), (5700000, "That adds both the loss and the drawings.")], [("Loss", "5 000 000 - 300 000 = 4 700 000"), ("Drawings", "4 700 000 - 400 000 = 4 300 000")],
          T_BS, "Calculation", "A loss reduces capital."),
        Q("Electricity of FCFA 30 000 is owing at the year end. On the balance sheet it appears as",
          "a current liability",
          [("a current asset", "The business owes the amount."),
           ("a deduction from receivables", "It has no link with the customers' accounts."),
           ("part of equity", "It is owed to the supplier.")],
          [("Accrual", "An accrued expense is a liability.")],
          T_BS, "Concept", "Does the business owe or is it owed?"),
        N(f"Total assets are {F_(8_000_000)}. Equity is {F_(5_500_000)} and the long-term loan is {F_(1_000_000)}. Find the current liabilities.",
          _v5, [("Liabilities", "8 000 000 - 5 500 000 = 2 500 000"), ("Current", "2 500 000 - 1 000 000 = 1 500 000")],
          T_BS, "Application", "Subtract equity, then the long-term part."),
        Q("The two totals of a balance sheet differ by exactly FCFA 1 800 000. Drawings were FCFA 900 000. The most likely error is",
          "drawings were added to capital instead of subtracted",
          [("drawings were left out of the balance sheet", "That would give a difference of 900 000, not 1 800 000."),
           ("depreciation was charged twice", "That would give a difference equal to the depreciation."),
           ("the bank balance was omitted", "That would give a difference equal to the bank balance.")],
          [("Size of the difference", "Adding instead of subtracting gives twice the drawings: 2 x 900 000 = 1 800 000")],
          T_BS, "Reasoning", "Compare the difference with the size of the figure."),
        N(f"Opening equity {F_(12_000_000)} + net result {F_(1_800_000)} - drawings {F_(2_500_000)}: find the closing equity.",
          _v7, [("Add", "12 000 000 + 1 800 000 = 13 800 000"), ("Subtract", "13 800 000 - 2 500 000 = 11 300 000")],
          T_BS, "Calculation", "Profit adds; drawings subtract."),
        Q("The link between the income statement and the balance sheet is that",
          "the net result increases (or, if a loss, decreases) the capital on the balance sheet",
          [("the balance sheet total is added to the income statement", "The statements are separate, linked through capital."),
           ("depreciation is shown only in the balance sheet", "It is an expense in the income statement and a deduction on the balance sheet."),
           ("drawings are an income in the income statement", "Drawings are not income.")],
          [("Link", "Net result is transferred to the capital account; adjustments appear in both statements.")],
          T_BS, "Reasoning", "Where does the profit go at the end of the year?"),
    ]))

# ================================================================== 10. Incomplete records
use(20)
_w1 = 2_000_000 - 600_000
_w2 = 1_500_000 + 260_000 - 200_000
_w3 = 1_000_000 + 220_000 - 150_000
_w4 = (1_400_000 - 1_000_000) + 300_000
_w5 = 600_000 * 140 // 100
_w7 = (1_200_000 - 900_000) + 250_000 - 100_000
_w8 = 800_000 * 100 // 80
assert (_w1, _w2, _w3, _w4, _w5, _w7, _w8) == (1_400_000, 1_560_000, 1_070_000, 700_000, 840_000, 450_000, 1_000_000)
SETS.append(practice_set(
    module=M_FIN, topic=T_INC, title="Incomplete records: capital, sales, purchases and profit",
    lesson="acc3-incomplete-records-single-entry", questions=[
        NM(f"At the start of the year a trader has assets of {F_(2_000_000)} and liabilities of {F_(600_000)}. Find the opening capital.",
          _w1, [(2600000, "That adds the liabilities."), (2000000, "That is the assets, not the capital."), (600000, "That is the liabilities.")], [("Capital", "Assets - liabilities = 2 000 000 - 600 000 = 1 400 000")], T_INC, "Calculation", "A statement of affairs finds capital."),
        NM(f"Opening receivables {F_(200_000)}, closing receivables {F_(260_000)}, cash received from customers {F_(1_500_000)}. Find the credit sales.",
          _w2, [(1440000, "That reverses the change in receivables."), (1500000, "That ignores the change in receivables."), (1960000, "That adds the two balances.")], [("Control account", "Credit sales = receipts + closing - opening"), ("Calculate", "1 500 000 + 260 000 - 200 000 = 1 560 000")],
          T_INC, "Calculation", "Build the receivables control account."),
        N(f"Opening payables {F_(150_000)}, closing payables {F_(220_000)}, payments to suppliers {F_(1_000_000)}. Find the credit purchases.",
          _w3, [("Control account", "Purchases = payments + closing - opening"), ("Calculate", "1 000 000 + 220 000 - 150 000 = 1 070 000")],
          T_INC, "Calculation", "Build the payables control account."),
        NM(f"Capital rose from {F_(1_000_000)} to {F_(1_400_000)}. The owner's drawings were {F_(300_000)} and no capital was introduced. Find the profit.",
          _w4, [(400000, "That forgets to add back the drawings."), (100000, "That subtracts the drawings."), (1700000, "That adds all three figures.")], [("Increase in capital", "400 000"), ("Add drawings", "400 000 + 300 000 = 700 000")], T_INC, "Calculation", "The owner took some profit out."),
        NM(f"Cost of goods sold is {F_(600_000)} and the mark-up is 40% on cost. Find the sales.",
          _w5, [(240000, "That is the gross profit, not the sales."), (600000, "That is the cost."), (1000000, "That divides the cost by 0.6 (a 40% margin).")], [("Sales", "600 000 x 140 / 100 = 840 000")], T_INC, "Calculation", "Mark-up is on cost."),
        Q("A mark-up of 25% on cost is the same as a margin of",
          "20% on sales",
          [("25% on sales", "The base is different: mark-up is on cost, margin on sales."),
           ("75% on sales", "That mixes the cost percentage with the margin."),
           ("30% on sales", "Check with cost 100: profit 25, sales 125, margin 25/125.")],
          [("Example", "Cost 100, profit 25, sales 125"), ("Margin", "25 / 125 = 20%")], T_INC, "Concept", "Take a cost of 100."),
        N(f"Capital rose from {F_(900_000)} to {F_(1_200_000)}. The owner also brought in {F_(100_000)} of new capital and took {F_(250_000)} as drawings. Find the profit for the year.",
          _w7, [("Increase", "300 000"), ("Add drawings", "300 000 + 250 000 = 550 000"), ("Less new capital", "550 000 - 100 000 = 450 000")],
          T_INC, "Application", "New capital is not profit."),
        N(f"Cost of goods sold is {F_(800_000)} and the gross profit margin is 20% of sales. Find the sales.",
          _w8, [("Cost is 80% of sales", "800 000 / 0.80 = 1 000 000")], T_INC, "Application", "If the margin is 20%, the cost is 80% of sales."),
    ]))

# ================================================================== 11. Non-profit organisations
use(21)
_x3 = 500_000 + 60_000 - 40_000
_x4 = 300_000 + 10_000 - 25_000
_x6 = 600_000 - 80_000
_x7 = 120_000 - (80_000 + 10_000)
_x8 = (650_000 + 120_000 + 80_000 + 30_000) - (240_000 + 150_000 + 60_000 + 50_000)
assert (_x3, _x4, _x6, _x7, _x8) == (520_000, 285_000, 520_000, 30_000, 380_000)
SETS.append(practice_set(
    module=M_FIN, topic=T_NPO, title="Non-profit organisations: income and expenditure",
    lesson="acc3-non-profit-organisations", questions=[
        Q("The excess of income over expenditure of a club is called",
          "a surplus",
          [("a profit paid to the members", "A club does not trade for profit to share."),
           ("drawings", "Drawings belong to sole traders."),
           ("the accumulated fund", "The accumulated fund is the club's capital, to which the surplus is added.")],
          [("Term", "A non-profit organisation reports a surplus or a deficit.")], T_NPO, "Recall", "What is the club's result called?"),
        Q("The capital of a non-profit organisation is called",
          "the accumulated fund",
          [("the drawings account", "That belongs to a sole trader."),
           ("the receipts and payments account", "That is a cash summary."),
           ("the surplus", "The surplus is one year's result.")],
          [("Accumulated fund", "Assets - liabilities of the club, increased by surpluses and reduced by deficits.")], T_NPO, "Recall", "Where does the club keep its accumulated surpluses?"),
        NM(f"Subscriptions received are {F_(500_000)}. Members owed {F_(40_000)} at the start and {F_(60_000)} at the end. No subscriptions were paid in advance. Find the subscription income for the year.",
          _x3, [(480000, "That reverses the arrears."), (500000, "That ignores the arrears."), (600000, "That adds both arrears.")], [("Formula", "received + closing arrears - opening arrears"), ("Calculate", "500 000 + 60 000 - 40 000 = 520 000")], T_NPO, "Calculation", "Build the subscriptions account."),
        N(f"Subscriptions received are {F_(300_000)}. At the start {F_(10_000)} had been paid in advance and at the end {F_(25_000)} has been paid in advance. Find the subscription income for the year.",
          _x4, [("Formula", "received + opening advance - closing advance"), ("Calculate", "300 000 + 10 000 - 25 000 = 285 000")], T_NPO, "Calculation", "Advance received last year belongs to this year."),
        Q("Which item appears in the receipts and payments account but NOT in the income and expenditure account?",
          "Purchase of equipment",
          [("Rent paid", "Rent is expenditure in both accounts."),
           ("Depreciation", "Depreciation appears only in the income and expenditure account (no cash)."),
           ("Subscriptions received for the year", "Subscriptions appear in both (adjusted in the income and expenditure account).")],
          [("Capital items", "Equipment bought is a capital payment, so only depreciation of it is expenditure.")],
          T_NPO, "Concept", "Which one is a capital item?"),
        N(f"The assets of a club are {F_(600_000)} and its liabilities are {F_(80_000)}. Find the accumulated fund.",
          _x6, [("Fund", "600 000 - 80 000 = 520 000")], T_NPO, "Calculation", "Use assets minus liabilities."),
        NM(f"Competition entry fees are {F_(120_000)}. Prizes paid are {F_(80_000)} and prizes of {F_(10_000)} are owing. Find the surplus on the competition.",
          _x7, [(40000, "That ignores the prizes still owing."), (120000, "That is the entry fees only."), (200000, "That adds the entry fees and the prizes paid.")], [("Prizes", "80 000 + 10 000 = 90 000"), ("Surplus", "120 000 - 90 000 = 30 000")], T_NPO, "Application", "Include the prizes still owing."),
        N(f"Income: subscriptions {F_(650_000)}, donations {F_(120_000)}, profit on refreshments {F_(80_000)}, competition surplus {F_(30_000)}. Expenditure: rent {F_(240_000)}, referees {F_(150_000)}, printing {F_(60_000)}, depreciation {F_(50_000)}. Find the surplus for the year.",
          _x8, [("Income", "650 000 + 120 000 + 80 000 + 30 000 = 880 000"), ("Expenditure", "240 000 + 150 000 + 60 000 + 50 000 = 500 000"), ("Surplus", "880 000 - 500 000 = 380 000")],
          T_NPO, "Application", "Total each side, then subtract."),
    ]))

# ================================================================== 12. Manufacturing accounts
use(22)
_y2 = 40_000 + 300_000 - 60_000
_y3 = _y2 + 150_000 + 20_000
_y5 = _y3 + 120_000 + 30_000 - 20_000
_y6 = _y5 // 2_900
_y8 = 300_000 + 2_880_000 - 400_000
assert (_y2, _y3, _y5, _y6, _y8) == (280_000, 450_000, 580_000, 200, 2_780_000) and _y5 % 2_900 == 0
SETS.append(practice_set(
    module=M_FIN, topic=T_MAN, title="Manufacturing accounts: prime cost and cost of production",
    lesson="acc3-manufacturing-accounts", questions=[
        Q("Prime cost is made up of",
          "raw materials used, direct labour and direct expenses",
          [("raw materials used and factory overheads", "Factory overheads are added after the prime cost."),
           ("direct labour and office salaries", "Office salaries are not factory costs."),
           ("factory cost less work in progress", "That is the cost of production.")],
          [("Prime cost", "The direct costs of making the goods.")], T_MAN, "Recall", "Which costs can be traced directly to the product?"),
        NM(f"Raw materials: opening {F_(40_000)}, purchases {F_(300_000)}, closing {F_(60_000)}. Find the raw materials used.",
          _y2, [(400000, "That adds the closing materials instead of subtracting them."), (300000, "That ignores the opening and closing materials."), (260000, "That subtracts the closing materials twice.")], [("Calculate", "40 000 + 300 000 - 60 000 = 280 000")], T_MAN, "Calculation", "Closing materials are subtracted."),
        N(f"Raw materials used {F_(280_000)}, direct labour {F_(150_000)}, direct expenses {F_(20_000)}. Find the prime cost.",
          _y3, [("Add", "280 000 + 150 000 + 20 000 = 450 000")], T_MAN, "Calculation", "Add the three direct items."),
        Q("Which of the following is a factory overhead?",
          "Depreciation of factory machinery",
          [("Wages of the machine operators who make the product", "That is direct labour."),
           ("Raw materials used", "That is part of prime cost."),
           ("Office salaries", "Office costs go to the income statement, not the factory.")],
          [("Overheads", "Indirect factory costs: factory rent, power, depreciation of machinery, indirect wages")], T_MAN, "Concept", "Which one cannot be traced to a single product?"),
        NM(f"Prime cost {F_(450_000)}, factory overheads {F_(120_000)}, opening work in progress {F_(30_000)}, closing work in progress {F_(20_000)}. Find the cost of production.",
          _y5, [(570000, "That ignores the work in progress."), (560000, "That reverses the opening and closing work in progress."), (600000, "That adds both work in progress figures.")], [("Factory cost", "450 000 + 120 000 = 570 000"), ("WIP", "570 000 + 30 000 - 20 000 = 580 000")], T_MAN, "Calculation", "Factory cost first, then work in progress."),
        N(f"The cost of production was {F_(580_000)} for 2 900 units. Find the cost per unit.",
          _y6, [("Divide", "580 000 / 2 900 = 200")], T_MAN, "Calculation", "Cost of production divided by units made."),
        Q("An increase in work in progress during the year (closing WIP higher than opening WIP) makes the cost of production",
          "lower than the factory cost",
          [("higher than the factory cost", "Closing WIP is subtracted, so it lowers the cost of production."),
           ("equal to the factory cost", "That is only when opening and closing WIP are equal."),
           ("equal to the prime cost", "Overheads and WIP still change the figure.")],
          [("Rule", "Cost of production = factory cost + opening WIP - closing WIP")], T_MAN, "Reasoning", "What is subtracted?"),
        N(f"Opening finished goods {F_(300_000)}, cost of production {F_(2_880_000)}, closing finished goods {F_(400_000)}. Find the cost of goods sold.",
          _y8, [("Calculate", "300 000 + 2 880 000 - 400 000 = 2 780 000")], T_MAN, "Application", "The cost of production replaces purchases."),
    ]))

# ================================================================== 13. Departmental accounts
use(23)
_z2 = 240_000 * 30 // 120
_z4 = 3_000_000 - (300_000 + 1_800_000 - 400_000)
_z5 = 200_000 * 3_000_000 // 5_000_000
_z6 = 950_000 - 630_000
_z8 = 950_000 * 1000 // 2_000_000
assert (_z2, _z4, _z5, _z6, _z8) == (60_000, 1_300_000, 120_000, 320_000, 475)
SETS.append(practice_set(
    module=M_FIN, topic=T_DEPT, title="Departmental accounts: allocation and comparison",
    lesson="acc3-departmental-accounts", questions=[
        Q("Departmental accounts are prepared so that the owner can",
          "see the gross and net profit of each department",
          [("avoid paying tax", "The purpose is information, not tax avoidance."),
           ("show one total for the whole business only", "That is the opposite of departmental accounts."),
           ("record the cash book", "The cash book is a book of original entry.")],
          [("Purpose", "Compare the performance of each department.")], T_DEPT, "Recall", "Why split the figures?"),
        NM(f"Rent of {F_(240_000)} is shared by floor area: department A has 30 m2 and department B has 90 m2. Find department A's share.",
          _z2, [(120000, "That is an equal share."), (80000, "That uses a ratio of 1 : 2."), (180000, "That is department B's share.")], [("Ratio", "30 : 90 = 1 : 3"), ("Share", "240 000 x 30 / 120 = 60 000")], T_DEPT, "Calculation", "Share in the ratio of the floor areas."),
        Q("The most suitable basis for sharing advertising between departments is",
          "sales of each department",
          [("floor area", "Floor area suits rent, not advertising."),
           ("equal shares for all costs", "Equal shares are only for costs with no better basis."),
           ("closing inventory", "Inventory does not measure advertising benefit.")],
          [("Advertising", "Promotes sales, so share in proportion to sales.")], T_DEPT, "Concept", "What does advertising aim to increase?"),
        N(f"Department A: sales {F_(3_000_000)}, opening inventory {F_(300_000)}, purchases {F_(1_800_000)}, closing inventory {F_(400_000)}. Find the gross profit.",
          _z4, [("Cost of goods sold", "300 000 + 1 800 000 - 400 000 = 1 700 000"), ("Gross profit", "3 000 000 - 1 700 000 = 1 300 000")], T_DEPT, "Calculation", "Cost of goods sold first."),
        NM(f"Advertising of {F_(200_000)} is shared in proportion to sales. Sales are {F_(3_000_000)} for department A and {F_(2_000_000)} for department B. Find department A's share.",
          _z5, [(100000, "That is an equal share."), (80000, "That is department B's share."), (200000, "That is the whole expense.")], [("Ratio", "3 : 2"), ("Share", "200 000 x 3 / 5 = 120 000")], T_DEPT, "Calculation", "Share in the ratio of sales."),
        N(f"Department B has a gross profit of {F_(950_000)} and a share of expenses of {F_(630_000)}. Find its net profit.",
          _z6, [("Net profit", "950 000 - 630 000 = 320 000")], T_DEPT, "Calculation", "Subtract the department's expenses."),
        Q("Purchases and inventory in a departmental account are",
          "recorded directly against each department (not apportioned)",
          [("apportioned in proportion to sales", "These belong to a department directly."),
           ("shared equally between the departments", "Each department has its own purchases and inventory."),
           ("ignored", "They are needed for the cost of goods sold.")],
          [("Direct items", "Know which department bought and holds the goods.")], T_DEPT, "Concept", "Does the business know which department bought the goods?"),
        N(f"Department B has sales of {F_(2_000_000)} and a gross profit of {F_(950_000)}. Find its gross profit as a percentage of sales.",
          47.5, [("Percentage", "950 000 / 2 000 000 x 100 = 47.5%")], T_DEPT, "Interpretation", "Gross profit divided by sales.", tol=0.05, unit="%"),
    ]))

# ================================================================== 14. Examination: Paper 1 strategy set
use(24)
_e2 = 90 * 10 // 50
_e5 = 1_200_000 - 500_000
_e6 = 900_000 - 540_000 - (210_000 - 10_000)
_e8 = 90 - 55 - 10
assert (_e2, _e5, _e6, _e8) == (18, 700_000, 160_000, 25)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 strategy practice",
    lesson="acc3-exam-paper-1-multiple-choice", questions=[
        Q("According to the Board's 2023 report, Paper 1 for Accounting (0505) consists of",
          "50 multiple-choice questions on the whole syllabus, all to be answered",
          [("25 multiple-choice questions, any 20 to be answered", "The paper has 50 questions and all are answered."),
           ("eight written questions", "That describes Paper 2."),
           ("50 questions with a choice of 40", "There is no choice: all questions are answered.")],
          [("Paper 1", "50 compulsory multiple-choice questions, 1 hour 30 minutes, 40% of the marks.")], "Paper 1", "Recall", "Remember the number and the word 'all'."),
        N("Paper 1 lasts 90 minutes and has 50 questions. How many minutes are available for 10 questions, on average?",
          18, [("Average per question", "90 / 50 = 1.8 minutes"), ("For 10", "10 x 1.8 = 18 minutes")], "Paper 1", "Calculation", "Find the time for one question first.", unit="minutes"),
        Q("Paper 1 carries what share of the marks for the whole Accounting examination?",
          "40%",
          [("60%", "That is the weighting of Paper 2."),
           ("50%", "The two papers do not carry equal weight."),
           ("25%", "The weighting is not a quarter.")],
          [("Weights", "Paper 1: 40%; Paper 2: 60%")], "Paper 1", "Recall", "Paper 2 is the larger paper."),
        Q("The two-pass method means",
          "answering the quick questions first, then returning to the marked questions",
          [("answering the questions twice to be sure", "Each question gets one answer; the second pass is for the unanswered ones."),
           ("starting with the hardest questions", "That wastes time at the start."),
           ("leaving the last 30 minutes unused", "Use the time; the last minutes are for checking.")],
          [("Pass 1", "Collect the easy marks"), ("Pass 2", "Use the remaining time on the marked questions")], "Paper 1", "Concept", "Think of how to avoid getting stuck."),
        N("Assets are FCFA 1 200 000 and liabilities FCFA 500 000. Using the accounting equation, find the capital.",
          _e5, [("Equation", "Capital = assets - liabilities"), ("Calculate", "1 200 000 - 500 000 = 700 000")], "Paper 1", "Calculation", "Rearrange assets = capital + liabilities."),
        Q("Sales are FCFA 900 000, cost of goods sold FCFA 540 000 and expenses paid FCFA 210 000, of which FCFA 10 000 is prepaid. The net profit is",
          "FCFA 160 000",
          [("FCFA 150 000", "That ignores the prepayment."),
           ("FCFA 170 000", "That adds the prepayment instead of subtracting it from the expense."),
           ("FCFA 360 000", "That is the gross profit.")],
          [("Expense for the year", "210 000 - 10 000 = 200 000"), ("Net profit", "900 000 - 540 000 - 200 000 = 160 000")], "Paper 1", "Application", "Adjust the expense first."),
        Q("Which term in the OHADA layout means the same as gross profit in the IAS/IFRS layout?",
          "Commercial margin (marge commerciale)",
          [("Value added", "Value added comes after external services."),
           ("Gross operating surplus", "That comes after personnel costs and taxes."),
           ("Net result", "That is the final balance.")],
          [("Equivalent", "Net sales of goods less cost of goods sold = commercial margin = gross profit")], "Paper 1", "Concept", "Which balance comes first?"),
        N("The plan is 55 minutes for pass 1 and 10 minutes for the final check in a 90-minute paper. How many minutes remain for pass 2?",
          _e8, [("Calculate", "90 - 55 - 10 = 25")], "Paper 1", "Application", "Subtract both from the total time.", unit="minutes"),
    ]))

# ================================================================== 15. Examination: Paper 2 strategy set
use(25)
_f3 = (180 - 10 - 10) // 5
_f5 = 500_000 - 80_000 + 30_000
_f7 = 50 * ((100 * 200 + 100 * 300) // 200)
assert (_f3, _f5, _f7) == (32, 450_000, 12_500) and (100 * 200 + 100 * 300) % 200 == 0
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 strategy practice",
    lesson="acc3-exam-paper-2-structure-and-working", questions=[
        Q("According to the Board's 2023 report, Paper 2 has",
          "eight questions: five OHADA questions (answer any three) and three IAS/IFRS questions (answer any two)",
          [("five questions, all compulsory", "Paper 2 has eight questions with a choice in each section."),
           ("eight questions, answer any five from either section", "The choice is fixed by section."),
           ("two sections of four questions, answer all", "Section A has five and Section B has three questions, with a choice.")],
          [("Structure", "Section A: 5 OHADA, any 3. Section B: 3 IAS/IFRS, any 2. 20 marks each.")], "Paper 2", "Recall", "Count the questions in each section."),
        N("How many questions in total must a candidate answer in Paper 2 (three from Section A and two from Section B)?",
          5, [("Add", "3 + 2 = 5")], "Paper 2", "Recall", "Add the two sections.", unit="questions"),
        N("Paper 2 lasts 180 minutes. You plan 10 minutes to read and choose, 10 minutes to check, and equal time for the five answers. How many minutes for each answer?",
          _f3, [("Time for answers", "180 - 10 - 10 = 160"), ("Each", "160 / 5 = 32")], "Paper 2", "Calculation", "Subtract reading and checking time first.", unit="minutes"),
        Q("Section B questions are set in",
          "the IAS/IFRS approach",
          [("the OHADA approach", "OHADA questions are in Section A."),
           ("the French approach only", "Section B uses the IAS/IFRS approach."),
           ("a mixture chosen by the candidate", "Each section has its approach.")],
          [("Section B", "IAS/IFRS wording: statement of financial position, inventory, depreciation")], "Paper 2", "Recall", "Section A is OHADA."),
        N("A bank statement shows FCFA 500 000. Unpresented cheques are FCFA 80 000 and lodgements not yet credited are FCFA 30 000. Find the balance of the updated cash book.",
          _f5, [("Subtract unpresented cheques", "500 000 - 80 000 = 420 000"), ("Add lodgements", "420 000 + 30 000 = 450 000")], "Paper 2", "Application", "Unpresented cheques lower the cash book balance relative to the statement.", unit="FCFA"),
        Q("One error the Board's 2023 report noticed in bank reconciliation statements was that some candidates",
          "transposed the entries, putting the business's bank account entries into the bank statement and the reverse",
          [("used the correct opening balance", "That is correct practice, not an error."),
           ("added the bank charges twice", "The report names the transposition of the entries."),
           ("left the question unattempted", "That was noted for other questions.")],
          [("Report", "Candidates mixed up which entries belong in the cash book and which in the bank statement.")], "Paper 2", "Interpretation", "Think about whose records the entries come from."),
        N("Receipts: 100 units at FCFA 200 and 100 units at FCFA 300. 150 units are issued. By the weighted average after all entries, find the value of the closing inventory (FCFA).",
          _f7, [("Total cost", "20 000 + 30 000 = 50 000"), ("Average", "50 000 / 200 = 250"), ("Closing", "50 x 250 = 12 500")], "Paper 2", "Application", "Divide total cost by total units, then multiply by the units left."),
        Q("The report says a popular question was not always well answered. The best advice for choosing questions is to",
          "choose the questions you can complete, whatever their popularity",
          [("choose the questions most of your class chooses", "Popular questions may still be badly answered."),
           ("choose the shortest-looking questions", "Length does not show difficulty."),
           ("answer only one section", "You must answer the required number from each section.")],
          [("Choice", "Pick topics where you can finish the working and the totals")], "Paper 2", "Reasoning", "What matters is your own strength."),
    ]))

# ================================================================== 16. Paper 1 mock exam A (50 questions, all modules in proportion)
use(26)


def P(topic, skill, prompt, correct, wrongs, working, hint="Read the stem twice, then test each option."):
    return Q(prompt, correct, wrongs, [("Working", working)], topic, skill, hint)


def FF(*xs):
    return [F_(x) for x in xs]


# ---- numbers (all checked) -------------------------------------------------------------------------------
_vat = 200_000 * 1925 // 10000
assert 200_000 * 1925 % 10000 == 0 and _vat == 38_500 and 200_000 + _vat == 238_500
_net_after_td = 200_000 - 200_000 * 10 // 100
_gross_ot = 40 * 1_500 + 8 * 1_500 * 3 // 2
assert (_net_after_td, _gross_ot) == (180_000, 78_000)
_ctl = 300_000 + 1_200_000 - 900_000 - 50_000
_unp = 420_000 - 100_000 + 20_000
_sl = (1_000_000 - 100_000) // 4
_rb2 = (1_000_000 - 1_000_000 * 40 // 100) * 40 // 100
_prov = (500_000 - 20_000) * 4 // 100 - 15_000
_fifo = 30 * 250
_wavg = (50 * 400 + 150 * 600) // 200
_cs = 1_500_000 + 260_000 - 200_000
_sub = 400_000 + 50_000 - 30_000
_cop = 1_000_000 + 80_000 - 120_000
assert (_ctl, _unp, _sl, _rb2, _prov, _fifo, _wavg, _cs, _sub, _cop) == (550_000, 340_000, 225_000, 240_000, 4_200, 7_500, 550, 1_560_000, 420_000, 960_000)

P1_QUESTIONS = [
    # ---------------------------- Module 1: OHADA Conceptual Framework & Double Entry (8)
    P(T_CONCEPTS, "Recall", "Which concept requires the owner's private affairs to be kept separate from the business?",
      "The business entity concept",
      [("The going concern concept", "Going concern assumes the business will continue; it is not about separating the owner."),
       ("The prudence concept", "Prudence avoids overstating profit or assets."),
       ("The historical cost concept", "That records assets at cost.")],
      "The business is treated as separate from its owner."),
    P(T_CONCEPTS, "Concept", "A business records a van at its purchase price and not at its estimated market price. This follows the",
      "historical cost concept",
      [("prudence concept", "Prudence concerns recognising losses early, not the value used."),
       ("matching concept", "Matching links expenses and incomes to the same period."),
       ("business entity concept", "That separates the owner from the business.")],
      "Assets are recorded at the cost paid."),
    P(T_CHART, "Recall", "In the SYSCOHADA chart of accounts, Class 2 accounts are for",
      "fixed assets",
      [("stocks (inventory)", "Stocks are in Class 3."),
       ("third parties (customers and suppliers)", "Third parties are in Class 4."),
       ("expenses", "Expenses are in Class 6.")],
      "Class 2 = actif immobilisé (fixed assets)."),
    P(T_CHART, "Recall", "Customer and supplier accounts belong to which SYSCOHADA class?",
      "Class 4 (third parties)",
      [("Class 1 (long-term resources)", "Class 1 holds capital and long-term loans."),
       ("Class 5 (treasury)", "Class 5 holds bank and cash."),
       ("Class 7 (incomes)", "Class 7 holds incomes such as sales.")],
      "Class 4 = comptes de tiers."),
    P(T_EQUATION, "Calculation", "Assets are FCFA 1 200 000 and capital is FCFA 700 000. The liabilities are",
      F_(500_000), [(x, w) for x, w in zip(FF(1_900_000, 700_000, 1_200_000), ["That adds the two figures.", "That copies the capital.", "That copies the assets."])],
      "Liabilities = assets - capital = 500 000."),
    P(T_EQUATION, "Concept", "A business buys equipment for FCFA 80 000 on credit. The effect on the accounting equation is",
      "assets and liabilities both increase by FCFA 80 000",
      [("assets and capital both increase", "The owner has not put in more money."),
       ("one asset increases and another decreases", "Cash is not used: the purchase is on credit."),
       ("liabilities decrease", "A new debt to the supplier is created.")],
      "Equipment (asset) up, amount owed to the supplier (liability) up."),
    P(T_DOUBLE, "Application", "Goods are sold on credit to Ngu. The correct entries are",
      "debit Ngu's account; credit Sales",
      [("debit Sales; credit Ngu's account", "The sides are reversed."),
       ("debit Bank; credit Sales", "No cash is received."),
       ("debit Purchases; credit Ngu's account", "Purchases is for goods bought.")],
      "The customer owes more (debit); sales income increases (credit)."),
    P(T_TB, "Recall", "Which balance normally appears on the credit side of a trial balance?",
      "Capital",
      [("Drawings", "Drawings are a debit balance."),
       ("Purchases", "Purchases are a debit balance."),
       ("Trade receivables", "Receivables are a debit balance.")],
      "Capital, sales and liabilities are credits."),
    # ---------------------------- Module 2: Commercial Documents & Books of Original Entry (8)
    P(T_INVOICE, "Calculation", "Goods have a list price of FCFA 200 000 and a 10% trade discount is allowed. The invoice amount before VAT is",
      F_(_net_after_td), [(F_(200_000), "That ignores the trade discount."), (F_(220_000), "That adds the discount."), (F_(190_000), "That deducts 5% only.")],
      "200 000 - 20 000 = 180 000."),
    P(T_INVOICE, "Concept", "A trade discount is",
      "deducted on the invoice and not recorded in the ledger accounts",
      [("allowed for early payment and recorded in the discount allowed account", "That is a financial (cash) discount."),
       ("recorded in the cash book", "Trade discount does not pass through the cash book."),
       ("an expense of the buyer", "It simply reduces the price.")],
      "Trade discount reduces the price on the invoice itself."),
    P(T_VAT, "Calculation", "VAT at 19.25% on goods worth FCFA 200 000 (before VAT) is",
      F_(_vat), [(F_(19_250), "That is 19.25% of 100 000, not of 200 000."), (F_(3_850), "That is 1.925% of 200 000."), (F_(40_000), "That uses 20%.")],
      "200 000 x 19.25% = 38 500."),
    P(T_VAT, "Concept", "Returnable containers on an invoice are",
      "charged to the customer but credited back when the containers are returned",
      [("included in the price and never refunded", "They are refunded when returned."),
       ("treated as a trade discount", "A container charge is not a discount."),
       ("sold with the goods as part of the stock", "They remain the seller's property.")],
      "The charge is refunded by a credit when the containers come back."),
    P(T_PSJ, "Recall", "Credit purchases of goods for resale are first recorded in the",
      "purchases journal",
      [("sales journal", "That records credit sales."),
       ("cash book", "Credit purchases do not involve cash yet."),
       ("returns outwards journal", "That records goods returned to suppliers.")],
      "The purchases journal is the book of original entry for credit purchases."),
    P(T_RETJ, "Recall", "A credit note received from a supplier is recorded in the",
      "returns outwards journal",
      [("returns inwards journal", "That records credit notes sent to customers."),
       ("purchases journal", "That records invoices received."),
       ("sales journal", "That records invoices sent.")],
      "Goods returned to a supplier are returns outwards."),
    P(T_RETJ, "Application", "A customer returns goods that were sold on credit. The ledger entries are",
      "debit Returns inwards; credit the customer's account",
      [("debit the customer's account; credit Returns inwards", "The sides are reversed: the customer now owes less."),
       ("debit Purchases; credit the customer's account", "Purchases is for goods bought."),
       ("debit Bank; credit Returns inwards", "No cash is paid yet.")],
      "Sales are reduced (debit) and the customer owes less (credit)."),
    P(T_GJ, "Application", "Which transaction is recorded in the general journal?",
      "Purchase of a machine on credit",
      [("A cash sale of goods", "That goes in the cash book."),
       ("A credit sale of goods", "That goes in the sales journal."),
       ("Payment of rent by cheque", "That goes in the cash book.")],
      "The general journal holds transactions with no special book, such as fixed assets bought on credit."),
    # ---------------------------- Module 3: Cash Books, Petty Cash & Bank Reconciliation (8)
    P(T_CB1, "Recall", "A cash book is",
      "both a book of original entry and a ledger account",
      [("a book of original entry only", "It is also the cash account of the ledger."),
       ("a ledger account only", "It is also where transactions are first recorded."),
       ("a statement sent by the bank", "That is the bank statement.")],
      "The cash book is a double-purpose book."),
    P(T_CB1, "Recall", "A two-column cash book has money columns for",
      "cash and bank",
      [("discount allowed and discount received", "Those are the discount columns of a three-column cash book."),
       ("debit and credit", "Each side has its own columns; the two columns are for cash and bank."),
       ("cash and petty cash", "Petty cash is a separate book.")],
      "Two columns on each side: cash and bank."),
    P(T_CB3, "Concept", "In a three-column cash book, discount received from suppliers is shown in the discount column on",
      "the credit (payments) side",
      [("the debit (receipts) side", "Discount allowed is on the debit side."),
       ("both sides", "Each discount appears on one side."),
       ("neither side; it is not recorded", "It is recorded in the discount column.")],
      "Discount received goes with payments to suppliers: credit side."),
    P(T_CBA, "Recall", "The analytical cash book",
      "has extra columns that analyse each receipt or payment by type",
      [("records only cash sales", "It records all cash and bank transactions."),
       ("has no money columns", "It has cash and bank columns."),
       ("replaces the bank statement", "The bank statement is prepared by the bank.")],
      "Analysis columns split receipts and payments by account."),
    P(T_PETTY, "Calculation", "A petty cashier has a float of FCFA 50 000 under the imprest system. During the period FCFA 38 500 is spent. The amount to restore the float is",
      F_(38_500), [(F_(50_000), "That is the whole float."), (F_(11_500), "That is the cash still in the box."), (F_(88_500), "That adds the two figures.")],
      "The imprest is restored by the amount spent: 38 500."),
    P(T_PETTY, "Concept", "Under the imprest system, at the start of each period the petty cashier has",
      "the same fixed amount (the float)",
      [("whatever is left from last period", "The float is topped up to its fixed amount."),
       ("no cash", "The cashier starts with the float."),
       ("the amount of last period's expenses", "That is the amount reimbursed, not the float.")],
      "The imprest amount is restored at the start of each period."),
    P(T_BANKREC, "Application", "A bank statement shows FCFA 420 000. Unpresented cheques are FCFA 100 000 and lodgements not yet credited are FCFA 20 000. The updated cash book balance is",
      F_(_unp), [(F_(500_000), "That adds the cheques and subtracts the lodgements."), (F_(540_000), "That adds both."), (F_(300_000), "That subtracts both.")],
      "420 000 - 100 000 + 20 000 = 340 000."),
    P(T_BANKREC, "Concept", "A cheque from a customer, banked, is later returned unpaid (dishonoured). In the cash book it is entered",
      "on the credit side of the bank column",
      [("on the debit side of the bank column", "That would increase the bank balance."),
       ("in the discount column", "No discount is involved."),
       ("it is not entered in the cash book", "The cash book must show the lost receipt.")],
      "The earlier receipt is cancelled: credit bank."),
    # ---------------------------- Module 4: Control Accounts, Correction of Errors & Payroll (8)
    P(T_CONTROL, "Calculation", "Sales ledger control account: opening balance FCFA 300 000, credit sales FCFA 1 200 000, receipts from customers FCFA 900 000, returns inwards FCFA 50 000. The closing balance is",
      F_(_ctl), [(F_(600_000), "That forgets the returns inwards."), (F_(650_000), "That adds the returns instead of subtracting them."), (F_(2_450_000), "That adds everything.")],
      "300 000 + 1 200 000 - 900 000 - 50 000 = 550 000."),
    P(T_CONTROL, "Concept", "Which item is NOT entered in the sales ledger control account?",
      "Cash sales",
      [("Credit sales", "Credit sales increase the debtors."),
       ("Cash received from credit customers", "That reduces the debtors."),
       ("Returns inwards", "Returns reduce the debtors.")],
      "Only credit transactions with customers appear in the control account."),
    P(T_ERR_ND, "Concept", "Goods sold to Ngu were wrongly debited to Mbu's account (also a customer). This is an error of",
      "commission",
      [("omission", "The transaction was recorded."),
       ("principle", "The wrong class of account was not used."),
       ("compensating errors", "Only one error is involved.")],
      "Right class of account, wrong account: commission."),
    P(T_ERR_ND, "Concept", "A machine bought was debited to the Purchases account. This is an error of",
      "principle",
      [("commission", "The wrong account of the same class would be commission."),
       ("omission", "The transaction was recorded."),
       ("original entry", "The amount was correct.")],
      "A fixed asset treated as an expense: wrong class, so principle."),
    P(T_SUSP, "Application", "The debit total of a trial balance is FCFA 5 000 more than the credit total. A suspense account is opened with a",
      "credit balance of FCFA 5 000",
      [("debit balance of FCFA 5 000", "That would widen the difference."),
       ("credit balance of FCFA 10 000", "The difference is 5 000."),
       ("it is not needed", "A suspense account balances the trial balance until the error is found.")],
      "Credit the difference to bring the credits up to the debits."),
    P(T_PAY1, "Calculation", "An employee works 40 normal hours at FCFA 1 500 and 8 overtime hours at time and a half. Gross pay is",
      F_(_gross_ot), [(F_(72_000), "That pays the overtime at the normal rate."), (F_(60_000), "That ignores the overtime."), (F_(96_000), "That uses double time.")],
      "60 000 + 8 x 2 250 = 78 000."),
    P(T_PAY1, "Calculation", "A worker is paid FCFA 350 for each unit made and makes 120 units. The pay is",
      F_(42_000), [(F_(4_200), "That is for 12 units: a slip of one zero."), (F_(35_000), "That is for 100 units."), (F_(36_000), "That uses 300 instead of 350 for each unit.")],
      "120 x 350 = 42 000."),
    P(T_PAY2, "Recall", "Which of these is a statutory deduction from an employee's gross pay?",
      "Contribution to the CNPS (social insurance)",
      [("Union dues", "These are voluntary."),
       ("Repayment of a staff loan", "That is agreed with the employer."),
       ("Contribution to a tontine", "That is voluntary.")],
      "Statutory deductions are required by law, such as social insurance and income tax."),
    # ---------------------------- Module 5: End-of-Year Adjustments & Inventory Valuation (8)
    P(T_DEP, "Calculation", "A machine costs FCFA 1 000 000, residual value FCFA 100 000, life 4 years. The straight-line charge for one year is",
      F_(_sl), [(F_(250_000), "That ignores the residual value."), (F_(900_000), "That is the total to depreciate."), (F_(400_000), "That is 40% of the cost.")],
      "(1 000 000 - 100 000) / 4 = 225 000."),
    P(T_DEP, "Calculation", "The same machine is depreciated at 40% reducing balance. The charge for year 2 is",
      F_(_rb2), [(F_(400_000), "That applies 40% to the cost again."), (F_(600_000), "That is the NBV after year 1."), (F_(160_000), "That applies 40% to a wrong base (400 000).")],
      "Year 1 charge 400 000, NBV 600 000; year 2 = 40% x 600 000 = 240 000."),
    P(T_DISP, "Application", "An asset with cost FCFA 800 000 and accumulated depreciation FCFA 500 000 is sold for FCFA 250 000. The result is",
      "a loss of FCFA 50 000",
      [("a profit of FCFA 50 000", "Proceeds are below the NBV of 300 000."),
       ("a loss of FCFA 550 000", "That compares the proceeds with cost."),
       ("a profit of FCFA 250 000", "That treats the proceeds as profit.")],
      "NBV 300 000; proceeds 250 000; loss 50 000."),
    P(T_BAD, "Calculation", "Receivables are FCFA 500 000. A bad debt of FCFA 20 000 is written off; a 4% provision is kept on the rest; the old provision was FCFA 15 000. The charge for the change in the provision is",
      F_(_prov), [(F_(5_000), "That applies 4% before the write-off."), (F_(19_200), "That is the whole new provision."), (F_(20_000), "That is the bad debt written off.")],
      "4% x 480 000 = 19 200; 19 200 - 15 000 = 4 200."),
    P(T_BAD, "Concept", "The entry to write off a bad debt is",
      "debit Bad debts; credit the customer's account",
      [("debit the customer's account; credit Bad debts", "The sides are reversed."),
       ("debit Bank; credit the customer's account", "No cash is received."),
       ("debit Provision for doubtful debts; credit Bank", "No cash moves.")],
      "Expense (debit); remove the debt (credit the customer)."),
    P(T_ACC, "Calculation", "Wages paid in the year are FCFA 480 000 and FCFA 40 000 of wages are owing. The wages expense is",
      F_(520_000), [(F_(440_000), "That subtracts the accrual."), (F_(480_000), "That ignores the accrual."), (F_(40_000), "That is the accrual only.")],
      "480 000 + 40 000 = 520 000."),
    P(T_INV, "Calculation", "Opening stock 40 units at FCFA 200; 60 units bought at FCFA 250; 70 units sold. By FIFO the closing inventory is",
      F_(_fifo), [(F_(6_900), "That is the weighted average value."), (F_(8_000), "That values the units at the oldest cost of 40 x 200."), (F_(6_000), "That values 30 units at 200.")],
      "30 units left, all from the 250 layer: 7 500."),
    P(T_INV, "Calculation", "50 units at FCFA 400 are in stock; 150 units are bought at FCFA 600. The weighted average cost per unit is",
      F_(_wavg), [(F_(500), "That is the simple average of the two prices."), (F_(450), "That does not weight the prices by the units."), (F_(600), "That is the latest price.")],
      "(20 000 + 90 000) / 200 = 550."),
    # ---------------------------- Module 6: Final Accounts & Specialized Accounts (10)
    P(T_IS, "Calculation", "Net sales are FCFA 5 000 000 and cost of goods sold is FCFA 3 100 000. The commercial margin is",
      F_(1_900_000), [(F_(8_100_000), "That adds the figures."), (F_(3_100_000), "That is the cost of goods sold."), (F_(1_300_000), "That also deducts FCFA 600 000 of services (the value added).")],
      "5 000 000 - 3 100 000 = 1 900 000."),
    P(T_IS, "Concept", "In the OHADA income statement, depreciation is deducted",
      "after the gross operating surplus",
      [("before value added", "Depreciation is not an external service."),
       ("from sales", "Depreciation is an expense, not a sales adjustment."),
       ("after the net result", "Depreciation helps to determine the net result.")],
      "Depreciation and provisions come after the gross operating surplus."),
    P(T_BS, "Calculation", "Capital at 1 January is FCFA 1 000 000, net profit FCFA 400 000 and drawings FCFA 150 000. The closing equity is",
      F_(1_250_000), [(F_(1_550_000), "That adds the drawings."), (F_(1_400_000), "That ignores the drawings."), (F_(850_000), "That subtracts the profit.")],
      "1 000 000 + 400 000 - 150 000 = 1 250 000."),
    P(T_BS, "Concept", "A bank loan repayable in five years is shown as",
      "a long-term liability",
      [("a current liability", "It is not due within a year."),
       ("a current asset", "A loan received is owed."),
       ("part of capital", "A loan is not the owner's money.")],
      "Due after more than a year: long-term."),
    P(T_INC, "Calculation", "Opening receivables FCFA 200 000, closing receivables FCFA 260 000, cash received from credit customers FCFA 1 500 000. Credit sales are",
      F_(_cs), [(F_(1_440_000), "That reverses the change in receivables."), (F_(1_500_000), "That ignores the change in receivables."), (F_(1_960_000), "That adds both balances.")],
      "1 500 000 + 260 000 - 200 000 = 1 560 000."),
    P(T_INC, "Calculation", "Capital rose from FCFA 1 000 000 to FCFA 1 400 000; drawings were FCFA 300 000 and no new capital was added. The profit is",
      F_(700_000), [(F_(400_000), "That forgets to add back the drawings."), (F_(100_000), "That subtracts the drawings."), (F_(1_700_000), "That adds all three figures.")],
      "400 000 + 300 000 = 700 000."),
    P(T_NPO, "Calculation", "A club received FCFA 400 000 of subscriptions. Arrears were FCFA 30 000 at the start and FCFA 50 000 at the end. The subscription income is",
      F_(_sub), [(F_(380_000), "That reverses the arrears."), (F_(400_000), "That ignores the arrears."), (F_(480_000), "That adds both arrears.")],
      "400 000 + 50 000 - 30 000 = 420 000."),
    P(T_MAN, "Calculation", "Factory cost is FCFA 1 000 000, opening work in progress FCFA 80 000 and closing work in progress FCFA 120 000. The cost of production is",
      F_(_cop), [(F_(1_040_000), "That reverses the two WIP figures."), (F_(1_200_000), "That adds both WIP figures."), (F_(1_000_000), "That ignores work in progress.")],
      "1 000 000 + 80 000 - 120 000 = 960 000."),
    P(T_DEPT, "Application", "Rent of FCFA 240 000 is shared by floor area: department A has 30 m2 and department B has 90 m2. Department A's share is",
      F_(60_000), [(F_(120_000), "That is an equal share."), (F_(80_000), "That uses a ratio of 1 : 2."), (F_(180_000), "That is department B's share.")],
      "30 : 90 = 1 : 3; A's share = 60 000."),
    P(T_DEPT, "Calculation", "A department has a gross profit of FCFA 950 000 and its share of expenses is FCFA 630 000. Its net profit is",
      F_(320_000), [(F_(1_580_000), "That adds the two figures."), (F_(950_000), "That is the gross profit."), (F_(630_000), "That is the expenses.")],
      "950 000 - 630 000 = 320 000."),
]
assert len(P1_QUESTIONS) == 50
_pos = [next(i for i, c in enumerate(q["choices"]) if c["correct"]) for q in P1_QUESTIONS]
assert sorted(_pos.count(i) for i in range(4)) == [12, 12, 13, 13], [_pos.count(i) for i in range(4)]
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="acc3-exam-paper-1-multiple-choice",
                         mock=True, time_limit_minutes=90, questions=P1_QUESTIONS))

# ================================================================== 17. Paper 2 practice paper A (structured, auto-marked parts)
use(27)
_dep2 = (1_600_000 - 1_600_000 * 25 // 100) * 25 // 100
_dep3 = (1_600_000 - 1_600_000 * 25 // 100) * 75 // 100 * 75 // 100
_dsl = (2_000_000 - 200_000) // 6
assert (_dep2, _dep3, _dsl) == (300_000, 675_000, 300_000)
_units = 100 + 200 + 100
_cost = 100 * 400 + 200 * 500 + 100 * 600
_avg = _cost // _units
_wclose = (_units - 300) * _avg
_fclose = 100 * 600
assert (_units, _cost, _avg, _wclose, _fclose) == (400, 200_000, 500, 50_000, 60_000) and _cost % _units == 0
_upd = 380_000 - 5_000 - 20_000 - 15_000
_unpres = 420_000 + 20_000 - _upd
assert (_upd, _unpres) == (340_000, 100_000)
_ot = 10 * 1_500 * 3 // 2
_gross = 40 * 1_500 + _ot
_ded = _gross * 4 // 100 + 6_000
_net = _gross - _ded
assert (_ot, _gross, _gross * 4 % 100, _net) == (22_500, 82_500, 0, 73_200)
_tl = 50 * 8_000
_td = _tl * 10 // 100
_inv_net = _tl - _td
_vat = _inv_net * 1925 // 10000
assert (_inv_net, _vat, _inv_net + _vat) == (360_000, 69_300, 429_300) and _inv_net * 1925 % 10000 == 0
_ns = 6_000_000 - 100_000
_cogs = 500_000 + 3_200_000 + 80_000 - 600_000
_gp = _ns - _cogs
_exp = 700_000 + (300_000 - 50_000) + 200_000
_np = _gp - _exp
assert (_ns, _cogs, _gp, _np) == (5_900_000, 3_180_000, 2_720_000, 1_570_000)
_subs = 800_000 + 90_000 - 60_000 - 40_000
_refr = 300_000 - 180_000
_surplus = _subs + _refr - 600_000
_fund = 1_000_000 + _surplus
assert (_subs, _refr, _surplus, _fund) == (790_000, 120_000, 310_000, 1_310_000)
_sl_close = 400_000 + 2_500_000 - 2_100_000 - 40_000 - 60_000 - 20_000 - 30_000
_pl_close = 300_000 + 1_600_000 - 1_300_000 - 25_000 - 45_000 - 30_000
assert (_sl_close, _pl_close) == (650_000, 500_000)

P2_QUESTIONS = [
    # Question 1: terminology and depreciation
    Q("Q1 (a) The accrual (matching) concept says that",
      "expenses are matched with the incomes of the period to which they relate",
      [("all expenses are recorded when paid in cash", "That is the cash basis."),
       ("assets are shown at their current market price", "That is not the accrual concept."),
       ("profit is the closing cash less the opening cash", "Profit is not the change in cash.")],
      [("Concept", "Record each cost and income in the period to which it belongs.")], T_CONCEPTS, "Recall", "Think of an expense paid after the year end."),
    N(f"Q1 (b) A vehicle costs {F_(1_600_000)} and is depreciated at 25% reducing balance. Find the charge for year 2.",
      _dep2, [("Year 1", "25% x 1 600 000 = 400 000; NBV 1 200 000"), ("Year 2", "25% x 1 200 000 = 300 000")], T_DEP, "Calculation", "Apply the rate to the NBV at the start of year 2."),
    N(f"Q1 (c) For the same vehicle ({F_(1_600_000)}, 25% reducing balance), find the net book value at the end of year 3.",
      _dep3, [("Year 1 NBV", "1 200 000"), ("Year 2 NBV", "900 000"), ("Year 3 NBV", "675 000")], T_DEP, "Calculation", "Each year the NBV is 75% of the year before."),
    N(f"Q1 (d) A machine costs {F_(2_000_000)}, residual value {F_(200_000)}, life 6 years. Find the straight-line charge for one year.",
      _dsl, [("Formula", "(2 000 000 - 200 000) / 6 = 300 000")], T_DEP, "Calculation", "Subtract the residual value first."),
    # Question 2: inventory costing. Data: opening 100 units at 400; bought 200 at 500; bought 100 at 600; 300 issued.
    N("Q2 (a) A stock card shows: opening 100 units at FCFA 400; purchase of 200 units at FCFA 500; purchase of 100 units at FCFA 600; total issues 300 units. Find the weighted average cost per unit after all entries (FCFA).",
      _avg, [("Total cost", "40 000 + 100 000 + 60 000 = 200 000"), ("Total units", "400"), ("Average", "200 000 / 400 = 500")], T_INV, "Calculation", "Divide the total cost by the total units.", unit="FCFA per unit"),
    N("Q2 (b) Using the data above (opening 100 at 400; 200 at 500; 100 at 600; 300 units issued), find the closing inventory at weighted average cost after all entries (FCFA).",
      _wclose, [("Units left", "400 - 300 = 100"), ("Value", "100 x 500 = 50 000")], T_INV, "Calculation", "Use the average for the period."),
    N("Q2 (c) Using the same data, find the closing inventory by FIFO (FCFA).",
      _fclose, [("Units left", "100"), ("Which layer", "The oldest 300 units are issued first: the 100 left are from the last purchase at 600"), ("Value", "100 x 600 = 60 000")], T_INV, "Calculation", "Which purchase is left at the end under FIFO?"),
    Q("Q2 (d) Using the same data, which method gives the higher profit, and why?",
      "FIFO, because its closing inventory (60 000) is higher than the average cost value (50 000), so the cost of goods sold is lower",
      [("Weighted average, because its closing inventory is higher", "The average method gives the lower closing inventory here (50 000)."),
       ("Both give the same profit, because total cost is the same", "The cost of goods sold differs because the closing inventory differs."),
       ("FIFO, because its cost of goods sold is higher", "A lower, not higher, cost of goods sold gives the higher profit.")],
      [("Closing inventory", "FIFO 60 000; average 50 000"), ("Cost of goods sold", "200 000 - closing: FIFO 140 000; average 150 000"), ("Profit", "Lower cost of goods sold gives higher profit")],
      T_INV, "Reasoning", "Compare the two closing inventory values."),
    # Question 3: bank reconciliation
    N("Q3 (a) The cash book (bank column) shows a debit balance of FCFA 380 000. Not yet recorded in it: bank charges FCFA 5 000, a dishonoured cheque FCFA 20 000 and a standing order payment FCFA 15 000. Find the updated cash book balance.",
      _upd, [("Deduct all three", "380 000 - 5 000 - 20 000 - 15 000 = 340 000")], T_BANKREC, "Calculation", "All three items reduce the bank balance."),
    N("Q3 (b) The bank statement shows FCFA 420 000. Lodgements of FCFA 20 000 are not yet credited. The updated cash book balance is FCFA 340 000. Find the total of the unpresented cheques needed to reconcile.",
      _unpres, [("Equation", "420 000 - unpresented + 20 000 = 340 000"), ("Solve", "unpresented = 440 000 - 340 000 = 100 000")], T_BANKREC, "Application", "Write the reconciliation and solve for the missing figure."),
    Q("Q3 (c) Which of these items requires an entry in the cash book (rather than only an item on the reconciliation statement)?",
      "Bank charges shown on the statement but not in the cash book",
      [("Cheques issued but not yet presented to the bank", "These are already in the cash book; they appear on the reconciliation statement."),
       ("Lodgements recorded in the cash book but not yet credited by the bank", "These are already in the cash book."),
       ("A cheque issued to a supplier and recorded in the cash book", "It is already recorded.")],
      [("Rule", "Items the bank has recorded and the business has not need a cash book entry.")], T_BANKREC, "Concept", "Whose records are missing the item?"),
    # Question 4: payroll
    N(f"Q4 (a) An employee works 10 hours of overtime at time and a half. The normal rate is FCFA 1 500 an hour. Find the overtime pay.",
      _ot, [("Overtime rate", "1 500 x 1.5 = 2 250 an hour"), ("Pay", "10 x 2 250 = 22 500")], T_PAY1, "Calculation", "Find the overtime rate first."),
    N("Q4 (b) The same employee works 40 normal hours at FCFA 1 500 an hour and 10 hours of overtime at time and a half. Find the gross pay.",
      _gross, [("Normal pay", "40 x 1 500 = 60 000"), ("Overtime", "22 500"), ("Gross", "82 500")], T_PAY1, "Calculation", "Add normal pay and overtime pay."),
    N("Q4 (c) Gross pay is FCFA 82 500. Deductions (rates invented for practice): social insurance 4% of gross pay and income tax FCFA 6 000. Find the net pay.",
      _net, [("Insurance", "4% x 82 500 = 3 300"), ("Total deductions", "3 300 + 6 000 = 9 300"), ("Net pay", "82 500 - 9 300 = 73 200")], T_PAY2, "Application", "Total the deductions, then subtract."),
    # Question 5: trading transactions
    N("Q5 (a) An invoice shows 50 units at FCFA 8 000 each with a 10% trade discount. Find the amount after trade discount.",
      _inv_net, [("List price", "50 x 8 000 = 400 000"), ("Discount", "10% = 40 000"), ("Net", "360 000")], T_INVOICE, "Calculation", "Multiply, then deduct the discount."),
    N("Q5 (b) VAT at 19.25% is charged on the amount after trade discount (FCFA 360 000). Find the VAT.",
      _vat, [("VAT", "360 000 x 19.25% = 69 300")], T_VAT, "Calculation", "Apply 19.25% to 360 000."),
    N("Q5 (c) Find the total amount payable on the invoice (net amount FCFA 360 000 plus VAT at 19.25%).",
      _inv_net + _vat, [("Total", "360 000 + 69 300 = 429 300")], T_VAT, "Calculation", "Add the VAT to the net amount."),
    # Question 6: final accounts of a sole trader (income statement)
    N("Q6 (a) A trader's sales are FCFA 6 000 000 and returns inwards FCFA 100 000. Find the net sales.",
      _ns, [("Net sales", "6 000 000 - 100 000 = 5 900 000")], T_IS, "Calculation", "Returns inwards reduce sales."),
    N("Q6 (b) Opening inventory FCFA 500 000, purchases FCFA 3 200 000, carriage inwards FCFA 80 000, closing inventory FCFA 600 000. Find the cost of goods sold.",
      _cogs, [("Calculate", "500 000 + 3 200 000 + 80 000 - 600 000 = 3 180 000")], T_IS, "Calculation", "Carriage inwards is added."),
    N("Q6 (c) Net sales are FCFA 5 900 000 and cost of goods sold FCFA 3 180 000. Find the gross profit (commercial margin).",
      _gp, [("Gross profit", "5 900 000 - 3 180 000 = 2 720 000")], T_IS, "Calculation", "Subtract cost of goods sold from net sales."),
    N("Q6 (d) The gross profit is FCFA 2 720 000. Expenses: wages FCFA 700 000; rent FCFA 300 000 of which FCFA 50 000 is prepaid; depreciation FCFA 200 000. Find the net profit.",
      _np, [("Rent expense", "300 000 - 50 000 = 250 000"), ("Total expenses", "700 000 + 250 000 + 200 000 = 1 150 000"), ("Net profit", "2 720 000 - 1 150 000 = 1 570 000")], T_IS, "Application", "Adjust the rent before totalling."),
    # Question 7: non-profit organisation
    N("Q7 (a) A club received FCFA 800 000 in subscriptions. Members owed FCFA 60 000 at the start and FCFA 90 000 at the end; FCFA 40 000 had been paid in advance at the end (none at the start). Find the subscription income for the year.",
      _subs, [("Formula", "received + closing arrears - opening arrears - closing advance"), ("Calculate", "800 000 + 90 000 - 60 000 - 40 000 = 790 000")], T_NPO, "Calculation", "Build the subscriptions account."),
    N("Q7 (b) Refreshment sales were FCFA 300 000 and refreshment purchases FCFA 180 000 (no inventory). Find the profit on refreshments.",
      _refr, [("Profit", "300 000 - 180 000 = 120 000")], T_NPO, "Calculation", "Show only the profit in the income and expenditure account."),
    N("Q7 (c) Income is subscriptions FCFA 790 000 plus the profit on refreshments FCFA 120 000. Expenditure is FCFA 600 000. Find the surplus for the year.",
      _surplus, [("Income", "790 000 + 120 000 = 910 000"), ("Surplus", "910 000 - 600 000 = 310 000")], T_NPO, "Calculation", "Total the income, then subtract the expenditure."),
    N("Q7 (d) The accumulated fund at the start was FCFA 1 000 000. Find the accumulated fund at the end, given a surplus of FCFA 310 000.",
      _fund, [("Closing fund", "1 000 000 + 310 000 = 1 310 000")], T_NPO, "Application", "A surplus is added to the accumulated fund."),
    # Question 8: control accounts
    N("Q8 (a) Sales ledger control account: opening balance FCFA 400 000; credit sales FCFA 2 500 000; receipts from debtors FCFA 2 100 000; discount allowed FCFA 40 000; returns inwards FCFA 60 000; bad debts written off FCFA 20 000; contra with the purchases ledger FCFA 30 000. Find the closing balance.",
      _sl_close, [("Debits", "400 000 + 2 500 000 = 2 900 000"), ("Credits", "2 100 000 + 40 000 + 60 000 + 20 000 + 30 000 = 2 250 000"), ("Balance", "2 900 000 - 2 250 000 = 650 000")], T_CONTROL, "Application", "Subtract every reduction from the debits."),
    Q("Q8 (b) During the year cash sales were FCFA 800 000. In the sales ledger control account, cash sales are",
      "not entered, because they do not pass through customers' accounts",
      [("entered on the debit side with credit sales", "The report notes that candidates wrongly included cash sales."),
       ("entered on the credit side as receipts", "Cash sales are not receipts from debtors."),
       ("entered as a contra item", "A contra is a set-off with the purchases ledger.")],
      [("Rule", "The control account summarises customers' accounts: credit transactions only.")], T_CONTROL, "Concept", "Do cash sales pass through a customer's account?"),
    N("Q8 (c) Purchases ledger control account: opening balance FCFA 300 000; credit purchases FCFA 1 600 000; payments to suppliers FCFA 1 300 000; discount received FCFA 25 000; returns outwards FCFA 45 000; contra with the sales ledger FCFA 30 000. Find the closing balance.",
      _pl_close, [("Credits", "300 000 + 1 600 000 = 1 900 000"), ("Debits", "1 300 000 + 25 000 + 45 000 + 30 000 = 1 400 000"), ("Balance", "500 000")], T_CONTROL, "Application", "Opening balance and purchases are credits; everything else reduces the balance."),
]
assert len(P2_QUESTIONS) == 28
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="acc3-exam-paper-2-structure-and-working",
                         mock=True, time_limit_minutes=150, questions=P2_QUESTIONS))
