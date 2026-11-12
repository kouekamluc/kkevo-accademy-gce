"""A Level Accounting (0705), Lower Sixth: practice sets for Year-End Adjustments, Provisions & Control, OHADA Annual
Financial Statements and the Examination module.

One 8-question set per lesson (9 topic lessons, 3 examination lessons), plus 'Paper 1 mock exam A' (50 multiple-choice
questions across all five Lower Sixth modules in proportion to their topic counts), 'Paper 2 practice paper A' (a preview
of cost and management accounting basics, auto-markable parts) and 'Paper 3 practice paper A' (financial accounting parts).
Exam facts are only those of the Board's 2023 subject report (three papers weighted 30, 30, 40; Paper 1 = 50 multiple-choice
questions; Paper 2 = Cost and Management Accounting; Paper 3 = Financial Accounting). The timings of the mock papers
(90 and 150 minutes) are KKEVO practice settings, not Board settings. Essays and full statements cannot be auto-marked, so
the Paper 2 and Paper 3 practice papers are structured versions with multiple-choice and numeric parts. All names and FCFA
figures are invented for practice; VAT is 19.25% (check the current Finance Law). Every numerical answer is computed or
asserted in this file.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("accounting", "lower-sixth")

M1 = "Revised SYSCOHADA Conceptual Framework"
M2 = "Commercial Operations, VAT, Packaging & Foreign Currency"
M3 = "Valuation of Assets & Inventory"
M_ADJ = "Year-End Adjustments, Provisions & Control"
M_FS = "OHADA Annual Financial Statements"
M_EXAM = "Examination"


def Q(prompt, correct, wrongs, sol, concept, skill, hint):
    """Four-option MC spec. wrongs = [(text, why)] x3; sol = [(step title, text)]. Position balanced by build()."""
    assert len(wrongs) == 3, prompt
    return {"k": "mc", "prompt": prompt, "correct": correct, "wrongs": wrongs, "steps": sol, "concept": concept,
            "skill": skill, "hint": hint}


def N(prompt, answer, sol, concept, skill, hint, tol=0, unit=""):
    return {"k": "num", "prompt": prompt, "answer": answer, "steps": sol, "concept": concept, "skill": skill,
            "hint": hint, "tol": tol, "unit": unit}


def build(specs, seed):
    """MC/NUM questions with the correct option spread evenly over A-D."""
    rng = random.Random(seed)
    counts = [0, 0, 0, 0]
    out = []
    for s in specs:
        st = [S(a, text=b) for a, b in s["steps"]]
        assert s["concept"] and len(s["concept"]) <= 80, s["concept"]
        assert s["hint"] and s["skill"] and st, s["prompt"]
        if s["k"] == "num":
            out.append(NUM(s["prompt"], s["answer"], steps=st, tolerance=s["tol"], unit=s["unit"], concept=s["concept"],
                           skill=s["skill"], hint=s["hint"]))
            continue
        m = min(counts)
        pos = rng.choice([i for i in range(4) if counts[i] == m])
        counts[pos] += 1
        ch = [C(t, why=w) for t, w in s["wrongs"]]
        assert all(w for _, w in s["wrongs"]), s["prompt"]
        ch.insert(pos, C(s["correct"], correct=True))
        out.append(MC(s["prompt"], ch, steps=st, concept=s["concept"], skill=s["skill"], hint=s["hint"]))
    return out


def vat(ht):
    assert ht * 1925 % 10000 == 0, ht
    return ht * 1925 // 10000


SETS = []

# ---------------------------------------------------------------- 1. Impairment of current assets
assert 715_500 * 10_000 // 11_925 == 600_000 and 600_000 * 20 // 100 == 120_000
assert 210_000 - 150_000 == 60_000 and 750_000 - (700_000 - 60_000) == 110_000
assert vat(200_000) == 38_500 and 238_500 == 200_000 + 38_500
SETS.append(practice_set(
    module=M_ADJ, topic="Impairment of current assets", title="Impairment of doubtful customers and inventory",
    lesson="acl2-impairment-of-current-assets",
    questions=build([
        Q("Which account is debited when a customer becomes doubtful?", "416 Doubtful customers",
          [("491 Impairment of customers", "491 is the impairment account, credited when the impairment is recorded."),
           ("651 Losses on receivables", "651 is used only when the debt is lost for certain."),
           ("6594 Impairment charge", "6594 is the charge, debited with the impairment, not with the debt.")],
          [("Transfer", "The whole debt, VAT included, moves from 411 to 416: debit 416, credit 411.")],
          "Doubtful customer account 416", "Recall", "The debt is moved from the healthy customers account."),
        Q("The impairment of a doubtful customer is calculated on", "the amount excluding VAT (HT)",
          [("the amount including VAT (TTC)", "The VAT can usually be recovered if the debt is lost, so it is not at risk."),
           ("the year's total sales", "The impairment relates to the customer's debt, not to sales."),
           ("the impairment held last year", "Last year's impairment is only compared with the new need.")],
          [("Rule", "Impairment = percentage x HT amount.")],
          "HT base for impairment", "Concept", "Think about which part of the debt can be recovered from the State."),
        N("A customer owes FCFA 715 500 TTC (VAT 19.25%). The expected loss is 20%. Find the impairment (FCFA).", 120_000,
          [("HT", "715 500 / 1.1925 = 600 000."), ("Impairment", "20% x 600 000 = 120 000.")],
          "Impairment calculation", "Calculation", "Divide by 1.1925 first.", unit="FCFA"),
        Q("At the year end the impairment needed for a customer is FCFA 150 000 and the impairment held is FCFA 90 000. The entry is",
          "debit 6594, credit 491 with 60 000",
          [("debit 491, credit 7594 with 60 000", "That is a reversal; here the need is larger than the amount held."),
           ("debit 6594, credit 491 with 150 000", "Only the difference is recorded, not the whole need."),
           ("debit 651, credit 416 with 60 000", "651 is for lost debts only.")],
          [("Compare", "150 000 - 90 000 = 60 000 increase: charge 6594 / 491.")],
          "Increase in impairment", "Application", "Is the need larger or smaller than the amount held?"),
        N("Impairment held FCFA 210 000; impairment now needed FCFA 150 000. How much is reversed to account 7594 (FCFA)?", 60_000,
          [("Difference", "210 000 - 150 000 = 60 000; debit 491, credit 7594.")],
          "Reversal of impairment", "Calculation", "Subtract the smaller from the larger.", unit="FCFA"),
        Q("A debt of FCFA 238 500 TTC is lost (VAT 19.25%). The correct entry is",
          "debit 651 with 200 000, debit 4431 with 38 500, credit 416 with 238 500",
          [("debit 651 with 238 500, credit 416 with 238 500", "The VAT is not a loss: it is debited to the VAT account to be recovered."),
           ("debit 6594 with 200 000, credit 491 with 200 000", "That records an impairment, not a lost debt."),
           ("debit 416 with 238 500, credit 651 with 238 500", "The sides are reversed.")],
          [("HT", "238 500 / 1.1925 = 200 000; VAT = 38 500."), ("Entry", "Debit 651 200 000 and 4431 38 500; credit 416 238 500.")],
          "Lost debt and VAT", "Application", "Split the TTC amount into HT and VAT."),
        N("Goods cost FCFA 750 000. They can be sold for FCFA 700 000 after further selling costs of FCFA 60 000. What impairment (FCFA) is recorded?", 110_000,
          [("Net realisable value", "700 000 - 60 000 = 640 000."), ("Impairment", "750 000 - 640 000 = 110 000.")],
          "Inventory impairment", "Calculation", "Compare cost with selling price less selling costs.", unit="FCFA"),
        Q("Why can an impairment be reversed while depreciation cannot?", "Impairment rests on an estimate that can change; depreciation records consumption that cannot come back",
          [("Impairment is a cash expense", "Neither is a cash payment."),
           ("Depreciation is not an expense", "Depreciation is an expense of the year."),
           ("The law forbids reversing depreciation only for buildings", "No such rule: depreciation records use of the asset in general.")],
          [("Reason", "A probable loss is an estimate (prudence); when the estimate improves it is reversed. Used-up life is not restored.")],
          "Impairment against depreciation", "Reasoning", "Think about what each one estimates."),
    ], seed=11)))

# ---------------------------------------------------------------- 2. Provisions for risks and charges
assert 30_000_000 * 2 // 100 == 600_000 and 600_000 - 450_000 == 150_000
assert 1_200_000 - 900_000 == 300_000 and 2_000_000 + 700_000 - 450_000 == 2_250_000
SETS.append(practice_set(
    module=M_ADJ, topic="Provisions for risks and charges", title="Provisions for risks and charges: tests, entries and effects",
    lesson="acl2-provisions-for-risks-and-charges",
    questions=build([
        Q("Which of these is NOT a condition for recognising a provision?", "The amount has been paid before the year end",
          [("A present obligation from a past event", "This is a required condition."),
           ("A probable outflow of resources", "This is a required condition."),
           ("A reliable estimate of the amount", "This is a required condition.")],
          [("Conditions", "Obligation, probable outflow, reliable estimate. A cost already paid is a charge, not a provision.")],
          "Recognition conditions", "Recall", "A provision covers a cost that is not yet paid."),
        Q("At 31 December a customer has sued the company over goods delivered in the year, and a payment is probable. This requires", "a provision for risks and charges",
          [("an impairment of customers", "The company is the one who may have to pay."),
           ("a reserve", "A reserve is a part of profit kept after the result is known."),
           ("no entry, because the case is not settled", "A probable and measurable obligation must be provided for.")],
          [("Test", "Past event, probable outflow, estimate available: provision.")],
          "Recognising a provision", "Application", "Apply the three conditions."),
        N("Warranty costs are estimated at 2% of sales of FCFA 30 000 000. The provision held is FCFA 450 000. What increase (FCFA) is charged?", 150_000,
          [("Needed", "2% x 30 000 000 = 600 000."), ("Increase", "600 000 - 450 000 = 150 000.")],
          "Warranty provision", "Calculation", "Find the provision needed, then compare.", unit="FCFA"),
        Q("A lawsuit provision of FCFA 1 800 000 is held. The lawyer now estimates FCFA 1 500 000. The entry is", "debit 191, credit 791 with 300 000",
          [("debit 691, credit 191 with 300 000", "That would increase the provision."),
           ("debit 191, credit 791 with 1 500 000", "Only the excess is reversed."),
           ("debit 691, credit 191 with 1 500 000", "That records a new provision and ignores the one held.")],
          [("Excess", "1 800 000 - 1 500 000 = 300 000 reversed.")],
          "Reversal of a provision", "Application", "Is the provision too large or too small?"),
        N("A provision of FCFA 1 200 000 is held. The case ends with a payment of FCFA 900 000. By how much (FCFA) does profit rise in that year, counting the payment and the reversal?", 300_000,
          [("Net", "Reversal 1 200 000 - payment 900 000 = 300 000 gain.")],
          "Effect of settlement on result", "Reasoning", "Compare the reversal with the real cost.", unit="FCFA"),
        Q("A guarantee given for another company's loan that may not need to be paid is", "disclosed in the notes as a contingent liability",
          [("recorded as a provision", "The obligation is only possible, not probable."),
           ("recorded as an impairment", "No asset has lost value."),
           ("ignored completely", "Material contingent liabilities are disclosed in the notes.")],
          [("Rule", "Possible obligation: disclose, do not record.")],
          "Contingent liability", "Concept", "Is the outflow probable?"),
        N("Opening provisions FCFA 2 000 000; charges FCFA 700 000; reversals FCFA 450 000. Find the closing provisions (FCFA).", 2_250_000,
          [("Schedule", "2 000 000 + 700 000 - 450 000 = 2 250 000.")],
          "Provisions schedule", "Calculation", "Opening + charge - reversal.", unit="FCFA"),
        Q("What is the main difference between a provision and a reserve?", "A provision is a charge that reduces the result; a reserve is part of the result kept in equity",
          [("A reserve is a charge; a provision is part of profit", "The two are the wrong way round."),
           ("There is no difference", "They are in different places: a provision with liabilities, a reserve in equity."),
           ("A provision is only for tax", "Provisions cover many risks and charges.")],
          [("Contrast", "Provision = charge (liability); reserve = appropriation of profit (equity).")],
          "Provision against reserve", "Concept", "One is charged before the result is known, the other after."),
    ], seed=12)))

# ---------------------------------------------------------------- 3. Accruals and prepayments
assert 2_400_000 * 7 // 12 == 1_400_000 and 6_000_000 * 10 * 4 // 1200 == 200_000
assert 3_200_000 + 400_000 - 60_000 - 300_000 + 90_000 == 3_330_000
SETS.append(practice_set(
    module=M_ADJ, topic="Accruals and prepayments", title="Regularising expenses and revenues at the year end",
    lesson="acl2-accruals-and-prepayments",
    questions=build([
        Q("Which SYSCOHADA account records an expense paid in advance for next year?", "476 Prepaid expenses",
          [("477 Income received in advance", "477 is for income received in advance, a liability."),
           ("408 Supplier invoices to come", "408 is for expenses used but not yet invoiced."),
           ("418 Customers, invoices to issue", "418 is for income earned but not yet invoiced.")],
          [("Account", "476 is a current asset.")],
          "Prepaid expense account", "Recall", "It is an asset."),
        N("On 1 August rent of FCFA 2 400 000 was paid for 12 months. The year ends on 31 December. Find the prepaid amount (FCFA).", 1_400_000,
          [("Months", "August to December = 5 months; 7 months are prepaid."), ("Amount", "7/12 x 2 400 000 = 1 400 000.")],
          "Prepaid rent", "Calculation", "Count the months that belong to the next year.", unit="FCFA"),
        Q("December electricity has not been invoiced at the year end. The entry is", "debit the electricity expense, credit 408",
          [("debit 476, credit the electricity expense", "That treats it as prepaid."),
           ("debit 408, credit the electricity expense", "The sides are reversed."),
           ("debit the bank, credit 408", "No cash has been paid.")],
          [("Accrual", "Expense used in the year: debit expense; liability: credit 408.")],
          "Accrued expense entry", "Application", "The expense belongs to this year; the cash is still owed."),
        N("A loan of FCFA 6 000 000 at 10% a year was taken on 1 September. Interest is paid annually on 31 August. Find the interest accrued at 31 December (FCFA).", 200_000,
          [("Months", "September to December = 4 months."), ("Interest", "6 000 000 x 10% x 4/12 = 200 000.")],
          "Accrued interest", "Calculation", "Interest for four months only.", unit="FCFA"),
        Q("Rent received in advance is recorded by", "debit rent income, credit 477",
          [("debit 477, credit rent income", "The sides are reversed."),
           ("debit 476, credit rent income", "476 is for prepaid expenses."),
           ("debit 418, credit rent income", "418 is for income earned but not yet invoiced.")],
          [("Entry", "Reduce this year's income; record a liability for the service to be provided.")],
          "Income received in advance", "Application", "Which year does the service belong to?"),
        N("Result before adjustments FCFA 3 200 000. Prepaid insurance 400 000; accrued electricity 60 000; income received in advance 300 000; accrued commission 90 000. Find the corrected result (FCFA).", 3_330_000,
          [("Adjust", "3 200 000 + 400 000 - 60 000 - 300 000 + 90 000 = 3 330 000.")],
          "Effect on the result", "Calculation", "Which adjustments increase profit?", unit="FCFA"),
        Q("Why are regularisation entries reversed on 1 January?", "So the real invoice of the new year is not counted twice",
          [("To hide the expense from the tax authority", "Reversal has nothing to do with hiding items."),
           ("Because accruals are errors", "Accruals are correct at the year end."),
           ("To increase the result of the new year", "The purpose is to avoid double counting, not to change profit.")],
          [("Reason", "The accrual and the later invoice would otherwise both be charged to the same expense.")],
          "Reversal (extourne)", "Reasoning", "What happens when the real invoice arrives?"),
        Q("An accrued expense at the year end is shown on the balance sheet as", "a current liability",
          [("a current asset", "That is for prepaid expenses and accrued income."),
           ("part of equity", "It is owed to someone else."),
           ("a deduction from fixed assets", "It has nothing to do with fixed assets.")],
          [("Position", "Money owed for service already used: current liability.")],
          "Balance sheet effect of accruals", "Concept", "Does the business owe money or is it owed?"),
    ], seed=13)))

# ---------------------------------------------------------------- 4. Bank reconciliation
assert 2_150_000 - 12_000 - 95_000 == 2_043_000 and 2_043_000 + 340_000 - 210_000 == 2_173_000
assert 1_500_000 - 400_000 + 150_000 == 1_250_000
SETS.append(practice_set(
    module=M_ADJ, topic="Bank reconciliation", title="Bank reconciliation: statement, adjusted balances and entries",
    lesson="acl2-bank-reconciliation",
    questions=build([
        Q("A cheque issued on 30 December has not yet been presented to the bank. At the reconciliation it is", "a timing difference shown in the bank columns only",
          [("an error to be corrected in 521", "It is already correctly recorded in 521."),
           ("an item to be debited to 521", "The cheque is already credited in 521."),
           ("a bank charge", "A bank charge is a different item.")],
          [("Rule", "Unpresented cheques need no entry in the books.")],
          "Unpresented cheques", "Concept", "Is the cheque already in our books?"),
        Q("Account 521 shows a debit balance. The bank statement for the same balance shows", "a credit balance",
          [("a debit balance", "The two records are mirror images, so the sides are opposite."),
           ("no balance", "The bank also records the amount it owes the business."),
           ("a balance equal to the cheques issued", "The statement shows the whole balance, not just cheques.")],
          [("Mirror image", "What is an asset for us is a debt for the bank.")],
          "Mirror image", "Concept", "Think of the bank's point of view."),
        N("521 shows a debit of FCFA 2 150 000. Bank charges of FCFA 12 000 and a standing order of FCFA 95 000 are not yet in the books. Find the adjusted 521 balance (FCFA).", 2_043_000,
          [("Adjust", "2 150 000 - 12 000 - 95 000 = 2 043 000.")],
          "Adjusted book balance", "Calculation", "Both items are payments.", unit="FCFA"),
        N("The adjusted balance is FCFA 2 043 000. Cheques of FCFA 340 000 are unpresented and a deposit of FCFA 210 000 is not yet credited. What credit balance (FCFA) does the statement show?", 2_173_000,
          [("Statement", "2 043 000 + 340 000 - 210 000 = 2 173 000.")],
          "Statement balance", "Calculation", "The bank has not yet paid the cheques but also not yet received the deposit.", unit="FCFA"),
        Q("A customer's cheque of FCFA 120 000 is returned unpaid. The entry is", "debit 411 Customers, credit 521 Bank",
          [("debit 631 Bank charges, credit 521", "The customer still owes the money; it is not a bank charge."),
           ("debit 521, credit 411", "That would record a receipt."),
           ("debit 651, credit 411", "The debt is not lost; the customer may still pay.")],
          [("Entry", "The customer owes again: debit 411; the bank balance falls: credit 521.")],
          "Unpaid cheque", "Application", "Who owes the money after the cheque is returned?"),
        Q("The bank wrongly credits the business with another customer's deposit. The business should", "report it to the bank and show it in the bank columns",
          [("debit 521 with the amount", "The money is not ours."),
           ("credit sales", "No sale has taken place."),
           ("ignore it, since the bank's balance is higher", "A mistake in the bank's favour must still be corrected.")],
          [("Rule", "Errors by the bank are reported; errors in the books are corrected in the books.")],
          "Bank error", "Reasoning", "Whose record contains the error?"),
        N("The statement shows a balance of FCFA 1 500 000. Cheques not yet presented total FCFA 400 000 and a deposit of FCFA 150 000 is not yet credited. Find the adjusted balance (FCFA).", 1_250_000,
          [("Short form", "1 500 000 - 400 000 + 150 000 = 1 250 000.")],
          "Short-form reconciliation", "Calculation", "Start from the statement.", unit="FCFA"),
        Q("Which statement best evaluates monthly bank reconciliation as a control?", "It compares two independent records, so it reveals errors and fraud early",
          [("It proves that no error exists in the books", "It cannot find errors that appear in both records."),
           ("It is only useful at the year end", "Frequent reconciliation finds problems while they are fresh."),
           ("It replaces the audit", "It is one control, not a substitute for the audit.")],
          [("Evaluation", "Independent comparison is its strength; timing and errors in both records are its limits.")],
          "Reconciliation as internal control", "Reasoning", "Think of two independent records."),
    ], seed=14)))

# ---------------------------------------------------------------- 5. Correction of errors
assert 8_640_000 - 8_586_000 == 54_000 and 2_000_000 - 120_000 == 1_880_000
assert 5_000_000 - 80_000 - 45_000 + 27_000 == 4_902_000
SETS.append(practice_set(
    module=M_ADJ, topic="Correction of errors", title="Errors, suspense accounts and corrected results",
    lesson="acl2-correction-of-errors",
    questions=build([
        Q("Which error does NOT make the trial balance disagree?", "Office furniture debited to the purchases account",
          [("A payment debited to a supplier but not credited to the bank", "Only one side was recorded."),
           ("The sales day book added up 50 000 too little", "A casting error affects one side only."),
           ("A receipt of 54 000 recorded as 45 000 in the customer's account", "A wrong amount on one side only.")],
          [("Principle", "An error of principle puts the right amount on both sides, in the wrong class.")],
          "Errors not affecting the trial balance", "Concept", "Look for equal debits and credits."),
        N("A trial balance has debits of FCFA 8 640 000 and credits of FCFA 8 586 000. What is the difference to put in the suspense account (FCFA)?", 54_000,
          [("Difference", "8 640 000 - 8 586 000 = 54 000.")],
          "Suspense account", "Calculation", "Subtract the two totals.", unit="FCFA"),
        Q("In that case the suspense account is opened with a", "credit of 54 000",
          [("debit of 54 000", "Debits are already too large."),
           ("credit of 8 640 000", "Only the difference is entered."),
           ("debit of 8 586 000", "The suspense account holds only the difference.")],
          [("Side", "Credits are short, so the suspense account is credited.")],
          "Side of the suspense account", "Application", "Which side is short?"),
        Q("Rent of FCFA 120 000 was debited to the buildings account. The draft profit is FCFA 2 000 000. The corrected profit is", "FCFA 1 880 000",
          [("FCFA 2 120 000", "The correction adds an expense, so profit falls."),
           ("FCFA 2 000 000", "The correction moves an amount into the income statement."),
           ("FCFA 1 760 000", "That deducts the rent twice.")],
          [("Correction", "Debit rent 120 000, credit buildings 120 000. Profit 2 000 000 - 120 000 = 1 880 000.")],
          "Effect on profit", "Application", "An expense was hidden in an asset."),
        N("Draft result FCFA 5 000 000. Sales overcast by 80 000; repairs of 45 000 capitalised in a fixed asset; commission received of 27 000 left out of income. Find the corrected result (FCFA).", 4_902_000,
          [("Sales overcast", "-80 000."), ("Repairs", "-45 000."), ("Commission", "+27 000."), ("Result", "5 000 000 - 80 000 - 45 000 + 27 000 = 4 902 000.")],
          "Statement of corrected result", "Calculation", "Which corrections change income or expenses?", unit="FCFA"),
        Q("A cheque from customer Ebai was credited to customer Ewane. The correction is", "debit 411 Ewane, credit 411 Ebai",
          [("debit suspense, credit 411 Ebai", "Debits and credits are equal, so no suspense account is involved."),
           ("debit 521, credit 411 Ebai", "The bank was already correctly debited."),
           ("debit sales, credit 411 Ewane", "No sale is involved.")],
          [("Commission", "Right class, wrong person: move the amount between the two accounts.")],
          "Error of commission", "Application", "Both accounts are customers."),
        Q("Under the OHADA accounting rules a wrong entry that has been validated must be", "corrected by a new dated entry",
          [("erased and rewritten", "Erasing is forbidden."),
           ("covered with correcting fluid", "Books must keep a clear audit trail."),
           ("left until the next year", "Errors must be corrected when found.")],
          [("Rule", "Never erase: reverse or complete with a new entry.")],
          "No erasing", "Recall", "Think of the audit trail."),
        Q("A debit error of 30 000 in one account is hidden by a credit error of 30 000 in another. It is called", "a compensating error",
          [("an error of omission", "Nothing was left out."),
           ("an error of principle", "The class of account is not the issue."),
           ("an error of original entry", "The same wrong amount was not used on both sides.")],
          [("Name", "Two errors cancel each other, so the trial balance agrees.")],
          "Compensating error", "Recall", "The errors cancel out."),
    ], seed=15)))

# ---------------------------------------------------------------- 6. The balance sheet
assert 40_000_000 - 28_000_000 - 2_000_000 == 10_000_000
assert 4_000_000 + 500_000 + 100_000 - 200_000 == 4_400_000 and 9_000_000 - 3_600_000 == 5_400_000
SETS.append(practice_set(
    module=M_FS, topic="The balance sheet", title="Classifying balances and building the OHADA balance sheet",
    lesson="acl2-ohada-balance-sheet",
    questions=build([
        Q("In the SYSCOHADA balance sheet, account 491 Impairment of customers is", "deducted from receivables",
          [("shown with current liabilities", "It is not a debt; it reduces an asset."),
           ("part of equity", "It is not owner's capital or reserves."),
           ("shown with cash-liabilities", "Cash-liabilities are overdrafts and bank credits.")],
          [("Rule", "Accounts 28, 29, 39 and 49 reduce the assets they relate to.")],
          "Impairment on the balance sheet", "Concept", "Is it a debt or a reduction of value?"),
        Q("A bank account with a credit balance of FCFA 350 000 is shown as", "a cash-liability",
          [("a negative cash-asset", "Overdrafts are not netted against positive balances."),
           ("a current liability", "Bank overdrafts have their own block, cash-liabilities."),
           ("a reduction of equity", "An overdraft is a debt, not owner's money.")],
          [("Overdraft", "A credit balance in 521 is a liability to the bank: cash-liabilities.")],
          "Overdraft classification", "Concept", "Does the bank owe us or do we owe the bank?"),
        N("Total assets are FCFA 40 000 000; stable resources FCFA 28 000 000; cash-liabilities FCFA 2 000 000. Find the current liabilities (FCFA).", 10_000_000,
          [("Balance", "40 000 000 - 28 000 000 - 2 000 000 = 10 000 000.")],
          "Balancing the balance sheet", "Calculation", "Total equity and liabilities equals total assets.", unit="FCFA"),
        Q("The net result of the year appears in the balance sheet", "in equity, before appropriation",
          [("in current liabilities", "It belongs to the owners."),
           ("in current assets", "A result is not an asset."),
           ("only in the notes", "It is shown in the balance sheet itself.")],
          [("Position", "The balance sheet is presented before appropriation of the result.")],
          "Result in equity", "Recall", "Who owns the profit?"),
        N("Customers FCFA 4 000 000, doubtful customers FCFA 500 000, prepaid expenses FCFA 100 000, impairment of customers FCFA 200 000. Find the net receivables (FCFA).", 4_400_000,
          [("Gross", "4 000 000 + 500 000 + 100 000 = 4 600 000."), ("Net", "4 600 000 - 200 000 = 4 400 000.")],
          "Net receivables", "Calculation", "Add the gross items, then deduct the impairment.", unit="FCFA"),
        Q("A provision for a lawsuit expected to be settled in three years is shown in", "financial debts, inside stable resources",
          [("current liabilities", "Only short-term provisions are current."),
           ("deducted from receivables", "It is not an impairment of an asset."),
           ("cash-liabilities", "That block is for bank credit and overdrafts.")],
          [("Class 19", "Long-term provisions for risks and charges belong with financial debts.")],
          "Long-term provision position", "Application", "Is it long term, and is it a liability?"),
        N("Machinery cost FCFA 9 000 000 and has accumulated depreciation of FCFA 3 600 000. Find the net value (FCFA).", 5_400_000,
          [("Net", "9 000 000 - 3 600 000 = 5 400 000.")],
          "Net book value", "Calculation", "Gross minus depreciation.", unit="FCFA"),
        Q("Stable resources are", "equity plus financial debts",
          [("equity plus current liabilities", "Current liabilities are short term."),
           ("current assets plus fixed assets", "That is a total of assets."),
           ("equity minus the result", "The result is part of equity.")],
          [("Definition", "Long-term financing: equity + financial debts.")],
          "Stable resources", "Recall", "Which financing is long term?"),
    ], seed=21)))

# ---------------------------------------------------------------- 7. The income statement and intermediate balances
assert 16_000_000 - 10_000_000 - (2_000_000 - 2_500_000) == 6_500_000
assert 9_000_000 - 4_000_000 == 5_000_000 and 7_200_000 + 300_000 - 1_100_000 == 6_400_000
assert 6_400_000 + (900_000 - 1_400_000) - 1_500_000 == 4_400_000
SETS.append(practice_set(
    module=M_FS, topic="The income statement and intermediate balances", title="Intermediate balances from commercial margin to net result",
    lesson="acl2-income-statement-intermediate-balances",
    questions=build([
        Q("Which is the correct order of the intermediate balances?", "Commercial margin, value added, gross operating surplus, operating result",
          [("Value added, commercial margin, operating result, gross operating surplus", "The cascade starts with the commercial margin and EBE comes before the operating result."),
           ("Gross operating surplus, value added, commercial margin, operating result", "EBE is found from value added, not before it."),
           ("Operating result, gross operating surplus, value added, commercial margin", "That is the reverse order.")],
          [("Cascade", "XA, XC, XD, XE.")],
          "Order of the balances", "Recall", "Margin comes first."),
        N("Sales of goods FCFA 16 000 000; purchases of goods FCFA 10 000 000; opening inventory FCFA 2 000 000; closing inventory FCFA 2 500 000. Find the commercial margin (FCFA).", 6_500_000,
          [("Change", "Opening - closing = -500 000."), ("Margin", "16 000 000 - 10 000 000 + 500 000 = 6 500 000.")],
          "Commercial margin", "Calculation", "Inventory rose, so the cost of goods sold is less than purchases.", unit="FCFA"),
        N("Value added is FCFA 9 000 000 and personnel costs FCFA 4 000 000. Find the gross operating surplus (FCFA).", 5_000_000,
          [("EBE", "9 000 000 - 4 000 000 = 5 000 000.")],
          "Gross operating surplus", "Calculation", "Deduct personnel costs only.", unit="FCFA"),
        Q("The profit on selling an old lorry is shown in", "the result outside ordinary activities (HAO)",
          [("the commercial margin", "The margin concerns goods for resale."),
           ("the operating result", "Disposals of fixed assets are outside ordinary activities."),
           ("the financial result", "Financial result covers interest and similar items.")],
          [("HAO", "Proceeds and book value of assets sold are class 8 items.")],
          "HAO result", "Concept", "Is selling a lorry the business's normal activity?"),
        N("Operating result FCFA 7 200 000; financial income FCFA 300 000; financial charges FCFA 1 100 000. Find the result of ordinary activities (FCFA).", 6_400_000,
          [("Financial result", "300 000 - 1 100 000 = -800 000."), ("RAO", "7 200 000 - 800 000 = 6 400 000.")],
          "Result of ordinary activities", "Calculation", "Add the financial result, which is negative here.", unit="FCFA"),
        Q("Depreciation is deducted", "after the gross operating surplus",
          [("before value added", "Depreciation is not an external purchase."),
           ("before the commercial margin", "The margin concerns trading only."),
           ("after the net result", "The net result is already after depreciation.")],
          [("Position", "XD minus depreciation and provisions gives the operating result.")],
          "Depreciation in the cascade", "Recall", "EBE ignores depreciation."),
        N("Result of ordinary activities FCFA 6 400 000; HAO income FCFA 900 000; HAO charges FCFA 1 400 000; income tax FCFA 1 500 000. Find the net result (FCFA).", 4_400_000,
          [("XH", "900 000 - 1 400 000 = -500 000."), ("Net", "6 400 000 - 500 000 - 1 500 000 = 4 400 000.")],
          "Net result", "Calculation", "Add the HAO result, then deduct tax.", unit="FCFA"),
        Q("Two shops have the same net result. Shop A's profit comes mostly from the sale of a building; Shop B's from trading. The better position is", "Shop B, because ordinary profit is likely to continue",
          [("Shop A, because it sold an asset", "One-off events cannot be repeated each year."),
           ("They are equal, since the net result is the same", "The source of profit matters for the future."),
           ("Shop A, because its HAO result is higher", "A high HAO result shows a weak core business.")],
          [("Interpretation", "Separating RAO from RHAO shows which profit is lasting.")],
          "Interpreting RAO and RHAO", "Interpretation", "Which profit will come again next year?"),
    ], seed=22)))

# ---------------------------------------------------------------- 8. The cash flow statement
assert 3_000_000 + 1_200_000 + 300_000 - 650_000 + 400_000 == 4_250_000
assert 4_250_000 + 200_000 - 900_000 - 150_000 == 3_400_000
assert -300_000 + 3_400_000 - 5_000_000 + 2_500_000 == 600_000 and 2_100_000 - 650_000 == 1_450_000
SETS.append(practice_set(
    module=M_FS, topic="The cash flow statement", title="CAFG, operating, investing and financing flows",
    lesson="acl2-cash-flow-statement",
    questions=build([
        N("Net result FCFA 3 000 000; depreciation FCFA 1 200 000; provision charge FCFA 300 000; a machine with book value FCFA 400 000 sold for FCFA 650 000. Find the CAFG (FCFA).", 4_250_000,
          [("Formula", "Result + charges - reversals - proceeds + book value sold."), ("Calculate", "3 000 000 + 1 200 000 + 300 000 - 650 000 + 400 000 = 4 250 000.")],
          "Self-financing capacity", "Calculation", "Add back non-cash charges and remove the disposal items.", unit="FCFA"),
        Q("Depreciation is added back to the net result in the CAFG because", "it is a charge that does not involve a payment in the year",
          [("it is income", "Depreciation is an expense."),
           ("it is paid to the State", "It is not a payment to anyone."),
           ("it increases the profit", "It reduces profit; adding it back removes a non-cash item.")],
          [("Reason", "The cash left when the asset was bought; depreciation only spreads its cost.")],
          "Depreciation and cash", "Concept", "Does depreciation use cash in the year?"),
        N("CAFG FCFA 4 250 000; inventories fell by FCFA 200 000; receivables rose by FCFA 900 000; current liabilities fell by FCFA 150 000. Find the operating cash flow (FCFA).", 3_400_000,
          [("Adjust", "4 250 000 + 200 000 - 900 000 - 150 000 = 3 400 000.")],
          "Operating cash flow", "Calculation", "Falling inventory releases cash; rising receivables use it.", unit="FCFA"),
        Q("Repayment of a bank loan appears in", "financing activities",
          [("operating activities", "Only interest is in the result; the capital repaid is financing."),
           ("investing activities", "Investing flows concern fixed assets."),
           ("the self-financing capacity", "The CAFG excludes loan repayments.")],
          [("Family", "Borrowing and repaying are financing flows.")],
          "Financing flows", "Recall", "Which flow concerns borrowing?"),
        N("Net cash at 1 January FCFA -300 000; operating flow +3 400 000; investing flow -5 000 000; financing flow +2 500 000. Find the net cash at 31 December (FCFA).", 600_000,
          [("Sum", "-300 000 + 3 400 000 - 5 000 000 + 2 500 000 = 600 000.")],
          "Closing net cash", "Calculation", "Add the three flows to the opening figure.", unit="FCFA"),
        Q("An increase in receivables during the year", "reduces the operating cash flow",
          [("increases the operating cash flow", "Customers who have not yet paid do not bring cash."),
           ("has no effect on cash", "Cash not yet received is tied up in receivables."),
           ("is an investing flow", "It is a working capital change in operations.")],
          [("Sign", "More receivables: minus.")],
          "Working capital sign", "Reasoning", "Has the cash arrived?"),
        N("Cash-assets are FCFA 2 100 000 and cash-liabilities FCFA 650 000. Find the net cash (FCFA).", 1_450_000,
          [("Net cash", "2 100 000 - 650 000 = 1 450 000.")],
          "Net cash", "Calculation", "Cash-assets minus cash-liabilities.", unit="FCFA"),
        Q("A firm shows profit every year, but net cash falls and loans rise. The likeliest explanation is", "investment and working capital use more cash than operations generate",
          [("the firm is making a hidden loss in the income statement", "The profit is real but is not the same as cash."),
           ("depreciation is a cash inflow", "Depreciation is not a cash flow."),
           ("loans are included in the profit", "Loans are not income.")],
          [("Interpretation", "Growth ties up cash in assets, and new loans cover the gap.")],
          "Profit and cash", "Interpretation", "Compare operating flow with investing flow."),
    ], seed=23)))

# ---------------------------------------------------------------- 9. Notes to the financial statements
assert 12_000_000 + 3_000_000 - 1_500_000 == 13_500_000 and 5_400_000 + 1_600_000 - 900_000 == 6_100_000
assert 1_500_000 + 400_000 - 250_000 == 1_650_000
SETS.append(practice_set(
    module=M_FS, topic="Notes to the financial statements", title="Notes: disclosure, movement tables and events",
    lesson="acl2-notes-to-financial-statements",
    questions=build([
        Q("The notes to the financial statements are", "part of the annual financial statements of the normal system",
          [("optional extra information", "Statements without notes are incomplete."),
           ("only needed for companies listed on a stock exchange", "They are part of the statements for all entities in the normal system."),
           ("a copy of the balance sheet", "They explain and complete the other statements.")],
          [("Status", "Balance sheet, income statement, cash flow statement and notes form one set.")],
          "Role of the notes", "Recall", "How many statements form the set?"),
        N("Gross fixed assets were FCFA 12 000 000 at 1 January. Acquisitions FCFA 3 000 000; an asset costing FCFA 1 500 000 was sold. Find the gross value at 31 December (FCFA).", 13_500_000,
          [("Movement", "12 000 000 + 3 000 000 - 1 500 000 = 13 500 000.")],
          "Fixed assets movement table", "Calculation", "Opening + additions - disposals at cost.", unit="FCFA"),
        N("Accumulated depreciation FCFA 5 400 000 at 1 January; charge FCFA 1 600 000; accumulated depreciation of FCFA 900 000 on a machine sold. Find the closing figure (FCFA).", 6_100_000,
          [("Movement", "5 400 000 + 1 600 000 - 900 000 = 6 100 000.")],
          "Depreciation movement table", "Calculation", "The depreciation of the asset sold leaves the table.", unit="FCFA"),
        Q("Which item is disclosed in the notes but NOT recorded in the accounts?", "A guarantee given for a supplier's bank loan",
          [("Depreciation of equipment", "It is a recorded charge."),
           ("Wages owing at the year end", "It is an accrued expense, recorded."),
           ("A provision for a lawsuit the company will probably lose", "A probable, measurable obligation is recorded.")],
          [("Commitment", "A guarantee may become a debt, so it is disclosed.")],
          "Commitments and contingencies", "Concept", "Which item is only a possible obligation?"),
        Q("In February a fire destroys a warehouse, before the accounts of the previous year are approved. The accounts of the previous year are", "not adjusted, but the event is disclosed in the notes",
          [("adjusted by writing off the warehouse", "The warehouse existed at the closing date."),
           ("left without any mention", "A major event after the year end is disclosed."),
           ("restated with a new closing date", "The closing date does not change.")],
          [("Rule", "The fire arose after the closing date: disclose only.")],
          "Events after the year end", "Application", "Did the situation exist at the closing date?"),
        N("Provisions were FCFA 1 500 000 at 1 January; charges FCFA 400 000; reversals FCFA 250 000. Find the closing provisions (FCFA).", 1_650_000,
          [("Movement", "1 500 000 + 400 000 - 250 000 = 1 650 000.")],
          "Provisions movement table", "Calculation", "Opening + charges - reversals.", unit="FCFA"),
        Q("Every movement table in the notes follows the pattern", "opening + increases - decreases = closing",
          [("opening + decreases - increases = closing", "The signs are reversed."),
           ("closing + opening = increases", "That is not a movement identity."),
           ("increases - decreases = opening", "The opening figure is the starting point.")],
          [("Pattern", "The closing figure is checked against the balance sheet.")],
          "Movement table pattern", "Concept", "Start with the opening balance."),
        Q("A possible obligation that depends on an uncertain future event, and cannot be measured reliably, is", "described in the notes as a contingent liability",
          [("recorded as a provision at the best guess", "The conditions for a provision are not met."),
           ("recorded as a reserve", "A reserve is part of profit."),
           ("recorded as an impairment of inventory", "No asset has lost value.")],
          [("Treatment", "Not recorded; disclosed.")],
          "Contingent liability disclosure", "Concept", "Is the outflow probable and measurable?"),
    ], seed=24)))

# ---------------------------------------------------------------- Examination 1. Paper 1 technique
assert 834_750 * 10_000 // 11_925 == 700_000 and 700_000 * 30 // 100 == 210_000
assert 16_000_000 - 10_000_000 + 500_000 == 6_500_000 and 480_000 * 8 // 12 == 320_000
assert 900_000 + 400_000 - 200_000 + 150_000 == 1_250_000
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 technique: routine, calculations and distractors",
    lesson="acl2-paper1-multiple-choice",
    questions=build([
        Q("According to the Board's 2023 report, Paper 1 of Accounting 0705 consists of", "50 multiple-choice questions, all compulsory",
          [("30 multiple-choice questions, choose any 20", "The report gives 50 compulsory questions."),
           ("5 essays, answer 3", "That is not the structure of Paper 1."),
           ("50 questions, answer 40", "All questions must be answered.")],
          [("Fact", "Paper 1: 50 compulsory MCQs, one mark each, marked by computer.")],
          "Structure of Paper 1", "Recall", "Think of the number and the choice."),
        Q("The best first step with a calculation multiple-choice question is to", "work out the answer before reading the options",
          [("read the options and pick the one that looks familiar", "Distractors are built to look familiar."),
           ("choose the longest option", "Length does not show correctness."),
           ("skip it and leave it blank", "A blank cannot score.")],
          [("Routine", "Read, answer first, match, check.")],
          "Answer first", "Concept", "Protect yourself from distractors."),
        N("A doubtful customer owes FCFA 834 750 TTC (VAT 19.25%). The expected loss is 30%. Find the impairment (FCFA).", 210_000,
          [("HT", "834 750 / 1.1925 = 700 000."), ("Impairment", "30% x 700 000 = 210 000.")],
          "Impairment calculation", "Calculation", "HT first.", unit="FCFA"),
        Q("In the question above, the option 250 425 is a distractor built on", "applying the percentage to the TTC amount",
          [("forgetting to apply the percentage", "That would give the HT debt, 700 000."),
           ("reversing the debit and credit", "No entry was asked for."),
           ("counting months wrongly", "No period is involved.")],
          [("Check", "30% x 834 750 = 250 425.")],
          "VAT-included distractor", "Reasoning", "Which base gives 250 425?"),
        N("Sales of goods FCFA 16 000 000; purchases FCFA 10 000 000; opening inventory FCFA 2 000 000; closing inventory FCFA 2 500 000. Find the commercial margin (FCFA).", 6_500_000,
          [("Margin", "16 000 000 - 10 000 000 - (2 000 000 - 2 500 000) = 6 500 000.")],
          "Commercial margin", "Calculation", "The inventory rose.", unit="FCFA"),
        N("Insurance of FCFA 480 000 for 12 months was paid on 1 September. The year ends on 31 December. Find the prepaid amount (FCFA).", 320_000,
          [("Months", "4 months used; 8 months prepaid."), ("Amount", "8/12 x 480 000 = 320 000.")],
          "Prepaid expense", "Calculation", "Count the months that belong to the next year.", unit="FCFA"),
        Q("Time management in a 50-question paper means", "moving on from a hard question and returning to it later",
          [("spending as long as needed on each question", "All questions are worth one mark; time is limited."),
           ("answering only the first thirty questions", "Every question counts and none should be skipped."),
           ("checking each answer five times", "Over-checking wastes time you need for the rest.")],
          [("Strategy", "Mark a doubtful question, continue, and return if time allows.")],
          "Time management", "Application", "Each question has the same value."),
        Q("Which of these is NOT deducted from an asset on the balance sheet?", "19 Provisions for risks and charges",
          [("491 Impairment of customers", "491 reduces receivables."),
           ("39 Impairment of inventory", "39 reduces inventories."),
           ("28 Accumulated depreciation", "28 reduces fixed assets.")],
          [("Rule", "19 is a liability.")],
          "Account classification", "Concept", "Which one belongs on the liabilities side?"),
    ], seed=31)))

# ---------------------------------------------------------------- Examination 2. Paper 2 preview
assert (2_940_000 - 2_220_000) // (1_800 - 1_200) == 1_200 and 2_940_000 - 1_800 * 1_200 == 780_000
assert 1_600_000 // 2_000 == 800 and (1_600_000 + 900_000) // 2_000 == 1_250
assert 6_000_000 // 15_000 == 400 and 20 * 400 + 80_000 + 45_000 == 133_000
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 preview: inventory, cost behaviour, break-even and overheads",
    lesson="acl2-paper2-cost-management-preview",
    questions=build([
        Q("According to the Board's 2023 report, Paper 2 of Accounting 0705 is", "Cost and Management Accounting",
          [("Financial Accounting", "That is Paper 3."),
           ("multiple choice", "That is Paper 1."),
           ("Company Accounting and Taxation only", "That is part of Paper 3, Section B.")],
          [("Fact", "Paper 1 MCQ, Paper 2 cost and management, Paper 3 financial accounting.")],
          "Structure of Paper 2", "Recall", "Match the papers to their subjects."),
        N("Opening inventory 200 units at FCFA 500; a purchase of 300 units at FCFA 600; an issue of 350 units. Find the FIFO value of the closing inventory (FCFA).", 90_000,
          [("Closing units", "500 - 350 = 150 units, all from the latest purchase."), ("Value", "150 x 600 = 90 000.")],
          "FIFO closing inventory", "Calculation", "FIFO issues the oldest units first.", unit="FCFA"),
        N("Using the same data, find the weighted average unit cost after the purchase (FCFA).", 560,
          [("Total cost", "100 000 + 180 000 = 280 000."), ("Average", "280 000 / 500 = 560.")],
          "Weighted average cost", "Calculation", "Total cost divided by total units.", unit="FCFA"),
        N("At 1 800 hours the total cost is FCFA 2 940 000; at 1 200 hours it is FCFA 2 220 000. Find the variable cost per hour (FCFA).", 1_200,
          [("Change", "(2 940 000 - 2 220 000) / (1 800 - 1 200) = 720 000 / 600 = 1 200.")],
          "High-low method", "Calculation", "Cost difference divided by activity difference.", unit="FCFA"),
        N("Price FCFA 5 000; variable cost FCFA 3 000 a unit; fixed costs FCFA 1 600 000. Find the break-even point (units).", 800,
          [("Contribution", "5 000 - 3 000 = 2 000."), ("Break-even", "1 600 000 / 2 000 = 800 units.")],
          "Break-even point", "Calculation", "Fixed costs divided by contribution per unit.", unit="units"),
        N("With the same data, how many units are needed for a profit of FCFA 900 000?", 1_250,
          [("Target", "(1 600 000 + 900 000) / 2 000 = 1 250 units.")],
          "Target profit", "Calculation", "Add the target profit to fixed costs.", unit="units"),
        N("Overheads of FCFA 6 000 000 are absorbed on 15 000 machine hours. A job uses materials FCFA 80 000, labour FCFA 45 000 and 20 machine hours. Find its total cost (FCFA).", 133_000,
          [("Rate", "6 000 000 / 15 000 = 400 per hour."), ("Total", "80 000 + 45 000 + 20 x 400 = 133 000.")],
          "Overhead absorption", "Calculation", "Find the rate per machine hour first.", unit="FCFA"),
        Q("Factory rent of FCFA 300 000 a month, whatever the output, is", "a fixed cost",
          [("a variable cost", "A variable cost changes with output."),
           ("a semi-variable cost", "There is no part that changes with output."),
           ("a direct material cost", "Rent is not a material.")],
          [("Behaviour", "A cost that does not change with activity is fixed.")],
          "Cost behaviour", "Concept", "Does it change with output?"),
    ], seed=32)))

# ---------------------------------------------------------------- Examination 3. Paper 3 technique
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 3", title="Paper 3 technique: choice, layout and control totals",
    lesson="acl2-paper3-financial-accounting",
    questions=build([
        Q("According to the Board's 2023 report, Section A of Paper 3 has four questions and a candidate answers", "three",
          [("four", "There is a choice."), ("two", "Two is the number in Section B."), ("one", "Candidates answer more than one question in Section A.")],
          [("Fact", "Section A: four questions, answer three; Section B: three questions, answer two.")],
          "Structure of Paper 3", "Recall", "Count the questions answered in each section."),
        Q("Section B of Paper 3 is based on", "company accounting and taxation",
          [("cost accounting", "That is Paper 2."), ("multiple choice questions", "That is Paper 1."), ("bank reconciliation only", "Section B is about companies and tax.")],
          [("Fact", "Section A financial accounting; Section B company accounting and taxation.")],
          "Sections of Paper 3", "Recall", "Think of the topics of the Upper Sixth."),
        Q("How many questions in total does a candidate answer in Paper 3, according to the report?", "five",
          [("seven", "Seven are set, but not all answered."), ("three", "Three is the Section A choice only."), ("four", "No section requires four answers.")],
          [("Total", "Three + two = five questions of equal weight.")],
          "Number of questions", "Recall", "Add the answers from the two sections."),
        N("You have 150 minutes (a KKEVO practice setting) and keep 10 minutes for reading and choosing. How many minutes can you give to each of five questions if you share the rest equally?", 28,
          [("Time", "(150 - 10) / 5 = 28 minutes.")],
          "Time sharing", "Application", "Subtract the reading time, then divide.", unit="minutes"),
        Q("A balance sheet is out of balance by exactly the amount of an accrued expense given in the question. The likeliest cause is", "the accrual appears in the income statement but not as a current liability",
          [("the share capital was wrongly copied", "Capital is copied directly and a difference equal to an adjustment points to that adjustment."),
           ("two accruals were recorded twice", "That would give double the difference."),
           ("the bank balance was ignored", "That would give a difference equal to the bank balance.")],
          [("Control", "An adjustment appears twice, so a difference equal to one adjustment means one side was forgotten.")],
          "Control totals", "Reasoning", "The adjustment affects two statements."),
        Q("Which journal entry layout earns the most marks?", "date, account numbers and names, amounts on the correct sides, narration",
          [("amounts only", "The examiner cannot see the accounts."),
           ("account names without amounts", "Amounts are needed."),
           ("a single total for the whole question", "Each entry must be shown separately.")],
          [("Format", "The Board's report stresses teaching the format of accounts.")],
          "Journal layout", "Application", "Think about what the examiner must read."),
        Q("The Board's report advises candidates to write Paper 2 and Paper 3 in", "blue or black ink",
          [("pencil", "The report says not to use pencils."), ("red ink", "Not mentioned and unsuitable."), ("any colour", "The report states blue or black.")],
          [("Fact", "Students should not use pencils in Papers 2 and 3.")],
          "Writing materials", "Recall", "The report mentions pencils."),
        N("A candidate writes the net result as 2 625 000 in the balance sheet but 2 265 000 in the income statement. By how much does the balance sheet fail to balance (FCFA)?", 360_000,
          [("Difference", "2 625 000 - 2 265 000 = 360 000.")],
          "Tracing a difference", "Calculation", "Subtract the two figures.", unit="FCFA"),
    ], seed=33)))

# ---------------------------------------------------------------- Mock: Paper 1 mock exam A (50 questions)
assert 600_000 * 90 * 95 // 10_000 == 513_000 and 2_000_000 * 1925 // 10_000 == 385_000
assert 3_542_000 - 3_311_000 == 231_000 and 120_000 * 3 // 4 == 90_000
assert 1_000_000 - 25_000 == 975_000 and 1_000 * 620 - 1_000 * 600 == 20_000 and 500_000 - 40_000 - 30_000 == 430_000
assert 10_000_000 + 400_000 + 600_000 == 11_000_000 and (5_000_000 - 500_000) // 5 == 900_000
assert 1_000_000 * 60 // 100 * 40 // 100 == 240_000 and 4_000_000 - 2_800_000 == 1_200_000 and 1_500_000 - 1_200_000 == 300_000
assert 150 * 1_200 == 180_000 and (100 * 1_000 + 300 * 1_200) // 400 == 1_150
assert 596_250 * 10_000 // 11_925 == 500_000 and 500_000 * 20 // 100 == 100_000 and 800_000 + 250_000 - 100_000 == 950_000
assert 1_200_000 * 9 // 12 == 900_000 and 2_279_500 - 665_000 + 380_000 == 1_994_500 and 4_000_000 - 150_000 == 3_850_000
assert 9_000_000 + 5_000_000 + 1_000_000 - 3_500_000 - 500_000 == 11_000_000 and 48_000_000 - 31_500_000 + 800_000 == 17_300_000
assert 3_500_000 + 250_000 - 1_125_000 == 2_625_000 and 1_500_000 + 800_000 - 100_000 == 2_200_000 and 12_000_000 + 3_000_000 - 1_500_000 == 13_500_000
_m1 = []
_a = _m1.append
# ---- Module 1: framework (9)
_a(Q("The convention that says an entity is assumed to continue operating in the foreseeable future is", "going concern",
     [("prudence", "Prudence concerns not overstating profit or assets."), ("non-compensation", "Non-compensation forbids netting assets against liabilities."), ("permanence of methods", "Permanence means keeping the same methods from year to year.")],
     [("Convention", "Going concern: assets are not valued at forced-sale prices.")], "Accounting postulates and conventions", "Recall", "Think of 'continuity of operation'."))
_a(Q("An accountant records a probable loss but does not record a probable gain. This applies the convention of", "prudence",
     [("going concern", "That assumes the entity continues."), ("historical cost", "That concerns the basis of valuing assets."), ("materiality", "That concerns the importance of an item.")],
     [("Prudence", "Probable losses are recognised; gains wait until realised.")], "Accounting postulates and conventions", "Concept", "Which convention is cautious?"))
_a(Q("A company changes its depreciation method every year to improve the profit. This breaks the convention of", "permanence of methods",
     [("prudence", "The issue is not caution but consistency."), ("historical cost", "The issue is not the valuation basis."), ("going concern", "The issue is not the entity's continuity.")],
     [("Consistency", "Methods must be kept from year to year unless a change is justified and disclosed.")], "Accounting postulates and conventions", "Application", "What does a yearly change prevent?"))
_a(Q("In the SYSCOHADA chart of accounts, class 2 contains", "fixed assets",
     [("inventories", "Inventories are class 3."), ("ordinary expenses", "Ordinary expenses are class 6."), ("treasury accounts", "Treasury is class 5.")],
     [("Classes", "1 long-term resources, 2 fixed assets, 3 stocks, 4 third parties, 5 treasury, 6 expenses, 7 income, 8 other.")], "The SYSCOHADA chart of accounts", "Recall", "Recall the classes in order."))
_a(Q("The sale of a fixed asset is recorded in class 8 because it is", "outside ordinary activities (HAO)",
     [("an ordinary activity", "Selling lorries is not the business's normal trade."), ("a financial charge", "Financial items are in classes 67 and 77."), ("an off-balance-sheet commitment", "Commitments are in class 9.")],
     [("HAO", "Disposals of fixed assets are class 8 items.")], "The SYSCOHADA chart of accounts", "Concept", "Is it the business's normal activity?"))
_a(Q("The minimal cash system (SMT) is reserved for", "very small entities below turnover limits set by the Uniform Act",
     [("all companies", "Larger entities use the normal system."), ("only listed companies", "Listed companies use the normal system."), ("entities that have no customers", "The criterion is size, not customers.")],
     [("SMT", "A cash-based system for very small entities; check the current limits.")], "The accounting systems", "Recall", "It is about size."))
_a(Q("Under the normal system the annual financial statements are", "the balance sheet, income statement, cash flow statement and notes",
     [("only a cash receipts and payments list", "That is the SMT."), ("the balance sheet only", "Four statements are required."), ("the trial balance and the ledger", "Those are books, not financial statements.")],
     [("Statements", "Four statements form the set.")], "The accounting systems", "Recall", "Count the statements."))
_a(Q("Which of these is a compulsory accounting book?", "the general ledger",
     [("the visitors' book", "It is not an accounting book."), ("the minutes of the staff meeting", "It is not an accounting record."), ("the price list", "It is not a book of account.")],
     [("Books", "Journal, general ledger, trial balance, inventory book.")], "Books, journals and computerized accounting", "Recall", "Which book holds the accounts?"))
_a(Q("A computerised accounting program must still respect the rule that validated entries cannot be", "erased or altered without a traceable correcting entry",
     [("printed", "Printing is allowed."), ("dated", "Dates are required."), ("totalled", "Totals are required.")],
     [("Rule", "Audit trail: correct by a new entry, never by deleting.")], "Books, journals and computerized accounting", "Concept", "What must stay visible for the auditor?"))
# ---- Module 2: commercial operations (13)
_a(N("Goods listed at FCFA 600 000 are sold with successive trade discounts of 10% and 5%. Find the net commercial amount (FCFA).", 513_000,
     [("Cascade", "600 000 x 0.90 x 0.95 = 513 000.")], "Invoicing and trade reductions", "Calculation", "Apply each discount to the previous net figure.", unit="FCFA"))
_a(Q("The financial discount (escompte) given to a customer for prompt payment is recorded by the seller as", "a financial expense (673)",
     [("a reduction of sales", "That is a trade reduction."), ("an operating income", "The seller loses, not gains."), ("it is not recorded", "Unlike trade reductions on the invoice, the escompte is recorded.")],
     [("Record", "Seller: 673; buyer: 773.")], "Invoicing and trade reductions", "Concept", "Which discount is financial?"))
_a(N("VAT at 19.25% on a net sale of FCFA 2 000 000 is (FCFA)", 385_000,
     [("VAT", "2 000 000 x 19.25% = 385 000.")], "Value added tax", "Calculation", "Multiply by 0.1925.", unit="FCFA"))
_a(N("In a month VAT invoiced on sales was FCFA 3 542 000 and deductible VAT was FCFA 3 311 000. How much VAT is payable to the State (FCFA)?", 231_000,
     [("Payable", "3 542 000 - 3 311 000 = 231 000.")], "Value added tax", "Calculation", "Collected less deductible.", unit="FCFA"))
_a(Q("VAT charged by a supplier on goods bought for resale is debited to", "4452 VAT on purchases",
     [("443 VAT invoiced", "443 holds the VAT charged to customers."), ("601 Purchases", "The VAT is recoverable and is not part of the cost."), ("401 Suppliers", "Suppliers are credited with the TTC amount.")],
     [("Account", "Deductible VAT on purchases is 4452.")], "Value added tax", "Recall", "Which account is deductible VAT?"))
_a(Q("Lost packaging (emballages perdus) is", "part of the price of the goods and not returned",
     [("a loan to the customer repayable on return", "That is a returnable container."), ("a fixed asset of the customer", "It is consumed with the goods."), ("an advance paid to the State", "It has no connection with taxes.")],
     [("Definition", "Lost packaging is sold with the goods.")], "Packaging and containers", "Concept", "Is it expected to come back?"))
_a(N("A customer paid a deposit of FCFA 30 000 for each of 4 returnable containers and returns 3 of them in time. What deposit (FCFA) is refunded?", 90_000,
     [("Refund", "3 x 30 000 = 90 000.")], "Packaging and containers", "Calculation", "Refund only the containers returned.", unit="FCFA"))
_a(Q("In a bill of exchange the person who accepts and must pay at maturity is the", "drawee",
     [("drawer", "The drawer issues the bill."), ("endorser", "The endorser transfers it to someone else."), ("bank manager", "The bank is not the party that accepts it.")],
     [("Parties", "Drawer orders, drawee accepts and pays.")], "Bills of exchange", "Recall", "Who is ordered to pay?"))
_a(N("A bill of FCFA 1 000 000 is discounted at the bank for charges of FCFA 25 000 (ignore VAT on the charges). How much does the bank credit (FCFA)?", 975_000,
     [("Proceeds", "1 000 000 - 25 000 = 975 000.")], "Bills of exchange", "Calculation", "Face value less discount charges.", unit="FCFA"))
_a(Q("A foreign currency purchase is recorded at", "the spot rate on the date of the transaction",
     [("the rate at the end of the year", "That is used to translate the balance at the year end."), ("the average rate of the last five years", "No such rule."), ("any rate chosen by the supplier", "The accountant uses the official or bank rate of the date.")],
     [("Rule", "Initial recognition at the spot rate.")], "Foreign currency transactions", "Recall", "Which date's rate?"))
_a(N("A supplier is owed USD 1 000, recorded at FCFA 600 per USD. At the year end the rate is FCFA 620. By how much (FCFA) has the debt increased?", 20_000,
     [("Difference", "1 000 x (620 - 600) = 20 000, an unrealised loss.")], "Foreign currency transactions", "Calculation", "Multiply the dollars by the change in rate.", unit="FCFA"))
_a(N("Gross pay is FCFA 500 000. Employee social contributions are FCFA 40 000 and income tax withheld FCFA 30 000. Find the net pay (FCFA).", 430_000,
     [("Net", "500 000 - 40 000 - 30 000 = 430 000.")], "Payroll", "Calculation", "Deduct the employee's deductions only.", unit="FCFA"))
_a(Q("Employer's social contributions on salaries are", "an additional expense of the employer, not deducted from the employee's pay",
     [("deducted from the employee's gross pay", "Those are the employee's contributions."), ("income of the business", "They are costs, not income."), ("added to the employee's net pay", "They are paid by the employer to the social body.")],
     [("Employer cost", "Total cost to the employer exceeds gross pay.")], "Payroll", "Concept", "Who pays them?"))
# ---- Module 3: valuation (9)
_a(N("A machine costs FCFA 10 000 000 excluding recoverable VAT; transport FCFA 400 000; installation FCFA 600 000. Find the acquisition cost (FCFA).", 11_000_000,
     [("Cost", "10 000 000 + 400 000 + 600 000 = 11 000 000.")], "Acquisition of fixed assets", "Calculation", "Include costs needed to bring it into use.", unit="FCFA"))
_a(Q("VAT on the purchase of a fixed asset that is NOT recoverable is", "added to the cost of the asset",
     [("debited to 4452", "That is for recoverable VAT."), ("charged as an expense immediately", "It is part of the asset's cost."), ("ignored", "The money was spent and must be recorded.")],
     [("Rule", "Non-deductible VAT is part of the cost.")], "Acquisition of fixed assets", "Concept", "Can it be recovered?"))
_a(N("Cost FCFA 5 000 000, residual value FCFA 500 000, life 5 years. Straight-line depreciation for a year is (FCFA)", 900_000,
     [("Annual charge", "(5 000 000 - 500 000) / 5 = 900 000.")], "Depreciation methods", "Calculation", "Depreciable amount divided by life.", unit="FCFA"))
_a(N("An asset costing FCFA 1 000 000 is depreciated at 40% on the reducing balance. The charge in year 2 is (FCFA)", 240_000,
     [("Year 1", "40% x 1 000 000 = 400 000."), ("Year 2", "40% x 600 000 = 240 000.")], "Depreciation methods", "Calculation", "Apply the rate to the net book value.", unit="FCFA"))
_a(Q("The year's depreciation is recorded by", "debit the depreciation charge, credit accumulated depreciation (account 28)",
     [("debit 28, credit the charge", "The sides are reversed."), ("debit the asset, credit the bank", "Depreciation involves no payment."), ("debit the asset, credit equity", "Depreciation is a charge, not a revaluation.")],
     [("Entry", "Charge in class 68; accumulated depreciation in class 28.")], "Depreciation methods", "Application", "It is a charge; the asset is not reduced directly."))
_a(N("An asset cost FCFA 4 000 000 with accumulated depreciation FCFA 2 800 000 and is sold for FCFA 1 500 000. Find the profit on disposal (FCFA).", 300_000,
     [("Book value", "4 000 000 - 2 800 000 = 1 200 000."), ("Profit", "1 500 000 - 1 200 000 = 300 000.")], "Disposal and trade-in of fixed assets", "Calculation", "Proceeds less book value.", unit="FCFA"))
_a(Q("The book value of an asset sold is recorded in", "account 812 (HAO)",
     [("account 701 Sales of goods", "A fixed asset is not sold in the ordinary trade."), ("account 601 Purchases", "It is not a purchase."), ("account 681 Depreciation charge", "That is for depreciation of the year.")],
     [("HAO", "Proceeds 822; book value 812.")], "Disposal and trade-in of fixed assets", "Recall", "Disposals are outside ordinary activities."))
_a(N("Opening inventory 100 units at FCFA 1 000; a purchase of 300 units at FCFA 1 200; 250 units issued. The FIFO closing inventory is (FCFA)", 180_000,
     [("Closing", "150 units remain, all from the latest purchase: 150 x 1 200 = 180 000.")], "Inventory valuation", "Calculation", "FIFO issues the oldest first.", unit="FCFA"))
_a(N("Using the same data, the weighted average unit cost after the purchase is (FCFA)", 1_150,
     [("Average", "(100 000 + 360 000) / 400 = 1 150.")], "Inventory valuation", "Calculation", "Total cost divided by total units.", unit="FCFA"))
# ---- Module 4: year-end adjustments (10)
_a(N("A doubtful customer owes FCFA 596 250 TTC (VAT 19.25%). The expected loss is 20%. The impairment is (FCFA)", 100_000,
     [("HT", "596 250 / 1.1925 = 500 000."), ("Impairment", "20% x 500 000 = 100 000.")], "Impairment of current assets", "Calculation", "Remove VAT first.", unit="FCFA"))
_a(Q("Account 491 holds FCFA 80 000 for a customer and the need falls to FCFA 50 000. The entry is", "debit 491, credit 7594 with 30 000",
     [("debit 6594, credit 491 with 30 000", "That increases the impairment."), ("debit 6594, credit 491 with 50 000", "Only the change is recorded."), ("debit 651, credit 416 with 30 000", "The debt is not lost.")],
     [("Reversal", "80 000 - 50 000 = 30 000.")], "Impairment of current assets", "Application", "Is the need larger or smaller?"))
_a(Q("Which of these is a condition for recognising a provision?", "a probable outflow that can be estimated reliably",
     [("the amount has already been paid", "A paid cost is a charge."), ("the managers expect profits to fall", "That is a future risk with no obligation."), ("the owners want to keep profit in the business", "That is a reserve.")],
     [("Conditions", "Past event, probable outflow, reliable estimate.")], "Provisions for risks and charges", "Concept", "A provision is for a probable cost."))
_a(N("Provisions were FCFA 800 000 at 1 January; charges FCFA 250 000; reversals FCFA 100 000. Closing provisions are (FCFA)", 950_000,
     [("Closing", "800 000 + 250 000 - 100 000 = 950 000.")], "Provisions for risks and charges", "Calculation", "Opening + charges - reversals.", unit="FCFA"))
_a(N("A premium of FCFA 1 200 000 for 12 months was paid on 1 October. The prepaid amount at 31 December is (FCFA)", 900_000,
     [("Months", "9 months belong to the next year."), ("Amount", "9/12 x 1 200 000 = 900 000.")], "Accruals and prepayments", "Calculation", "Count from 1 January to 30 September.", unit="FCFA"))
_a(Q("Commission earned in December but not yet invoiced is recorded by", "debit 418, credit the commission income",
     [("debit the commission income, credit 477", "That is income received in advance."), ("debit 476, credit the commission income", "476 is for prepaid expenses."), ("debit 408, credit the commission income", "408 is for supplier invoices to come.")],
     [("Accrued income", "Asset 418; income of the year.")], "Accruals and prepayments", "Application", "Is it earned or received in advance?"))
_a(N("The statement shows a balance of FCFA 2 279 500. Cheques of FCFA 665 000 are unpresented and a deposit of FCFA 380 000 is not yet credited. The adjusted balance is (FCFA)", 1_994_500,
     [("Adjusted", "2 279 500 - 665 000 + 380 000 = 1 994 500.")], "Bank reconciliation", "Calculation", "Cheques reduce it, the deposit increases it.", unit="FCFA"))
_a(Q("Bank charges shown on the statement but not in the books are recorded by", "debit 631 Bank charges, credit 521",
     [("debit 521, credit 631", "That would increase the bank balance."), ("no entry, because they are timing items", "They are bank-only items that must be recorded."), ("debit 411, credit 521", "No customer is involved.")],
     [("Entry", "Expense and a fall in the bank balance.")], "Bank reconciliation", "Application", "Is it a timing item or a bank-only item?"))
_a(Q("A transaction is entirely left out of the books. The error is one of", "omission",
     [("commission", "That is the wrong person's account."), ("principle", "That is the wrong class of account."), ("compensating", "That is two errors cancelling.")],
     [("Name", "Nothing was recorded, so debits still equal credits.")], "Correction of errors", "Recall", "Was anything recorded?"))
_a(N("Draft profit is FCFA 4 000 000. Closing inventory was overstated by FCFA 150 000. The corrected profit is (FCFA)", 3_850_000,
     [("Correction", "Overstated inventory overstates profit: 4 000 000 - 150 000 = 3 850 000.")], "Correction of errors", "Calculation", "Does overstated closing inventory raise or lower profit?", unit="FCFA"))
# ---- Module 5: annual statements (9)
_a(N("Fixed assets net FCFA 9 000 000; current assets FCFA 5 000 000; cash-assets FCFA 1 000 000; current liabilities FCFA 3 500 000; cash-liabilities FCFA 500 000. The stable resources are (FCFA)", 11_000_000,
     [("Balance", "15 000 000 - 3 500 000 - 500 000 = 11 000 000.")], "The balance sheet", "Calculation", "Total assets less the short-term items.", unit="FCFA"))
_a(Q("In the balance sheet before appropriation, the net result of the year is shown in", "equity",
     [("current liabilities", "It is not owed to a third party."), ("fixed assets", "A result is not an asset."), ("cash-assets", "Profit is not necessarily cash.")],
     [("Position", "Equity includes capital, reserves and the result.")], "The balance sheet", "Recall", "Who owns the profit?"))
_a(N("Sales of goods FCFA 48 000 000; purchases FCFA 31 500 000; opening inventory FCFA 4 200 000; closing inventory FCFA 5 000 000. The commercial margin is (FCFA)", 17_300_000,
     [("Margin", "48 000 000 - 31 500 000 + 800 000 = 17 300 000.")], "The income statement and intermediate balances", "Calculation", "Inventory rose by 800 000.", unit="FCFA"))
_a(Q("The gross operating surplus (EBE) is value added less", "personnel costs",
     [("depreciation", "Depreciation comes after the EBE."), ("income tax", "Income tax comes near the end."), ("interest paid", "Interest is in the financial result.")],
     [("EBE", "XC - personnel costs.")], "The income statement and intermediate balances", "Recall", "Which cost is deducted from value added?"))
_a(N("Result of ordinary activities FCFA 3 500 000; HAO result +250 000; income tax FCFA 1 125 000. The net result is (FCFA)", 2_625_000,
     [("Net", "3 500 000 + 250 000 - 1 125 000 = 2 625 000.")], "The income statement and intermediate balances", "Calculation", "Add the HAO result then deduct tax.", unit="FCFA"))
_a(N("Net result FCFA 1 500 000; depreciation FCFA 800 000; reversal of a provision FCFA 100 000; no disposals. The CAFG is (FCFA)", 2_200_000,
     [("CAFG", "1 500 000 + 800 000 - 100 000 = 2 200 000.")], "The cash flow statement", "Calculation", "Add back charges, remove non-cash income.", unit="FCFA"))
_a(Q("The purchase of equipment for cash is shown in", "investing activities",
     [("operating activities", "Operating flows concern ordinary activities."), ("financing activities", "Financing is about capital and loans."), ("the notes only", "It is a cash flow and appears in the statement.")],
     [("Family", "Fixed asset purchases are investing flows.")], "The cash flow statement", "Recall", "Is it a fixed asset?"))
_a(Q("The notes to the financial statements", "are part of the annual financial statements and explain the other statements",
     [("replace the balance sheet", "They complete it, not replace it."), ("are only for the tax office", "They are for all users."), ("are optional for companies", "They are part of the normal-system set.")],
     [("Role", "Notes complete and explain.")], "Notes to the financial statements", "Concept", "How many statements are in the set?"))
_a(N("Gross fixed assets FCFA 12 000 000 at 1 January; acquisitions FCFA 3 000 000; disposals at cost FCFA 1 500 000. The closing gross value is (FCFA)", 13_500_000,
     [("Closing", "12 000 000 + 3 000 000 - 1 500 000 = 13 500 000.")], "Notes to the financial statements", "Calculation", "Opening + additions - disposals.", unit="FCFA"))
_DIST = [
    [(510_000, "Adds the two discounts into one 15% discount."), (570_000, "Applies only the 5% discount."), (540_000, "Applies only the 10% discount.")],
    [(2_385_000, "This is the TTC amount: VAT is added, not extracted."), (322_851, "Treats 2 000 000 as if it already included VAT (about)."), (38_500, "A decimal slip: 1.925% instead of 19.25%.")],
    [(6_853_000, "Adds the two VAT amounts instead of subtracting."), (3_311_000, "This is the deductible VAT only."), (3_542_000, "This is the VAT invoiced only.")],
    [(120_000, "Refunds the deposit on all four containers."), (30_000, "Refunds one container only."), (60_000, "Refunds two containers; three were returned.")],
    [(1_025_000, "Adds the charges instead of deducting them."), (1_000_000, "Ignores the discount charges."), (25_000, "These are the charges, not the proceeds.")],
    [(620_000, "This is the new total in francs, not the difference."), (600_000, "This is the original debt."), (2_000, "Forgets to multiply by the 1 000 dollars.")],
    [(500_000, "This is the gross pay."), (570_000, "Adds the deductions to the gross pay."), (460_000, "Deducts only the social contributions.")],
    [(10_000_000, "Price only; ignores the cost of bringing the asset into use."), (10_400_000, "Forgets the installation."), (10_600_000, "Forgets the transport.")],
    [(1_000_000, "Ignores the residual value."), (4_500_000, "Does not divide by the life."), (450_000, "Divides by 10 instead of 5.")],
    [(400_000, "This is the year 1 charge."), (160_000, "Applies 40% to the year 1 charge instead of the net book value."), (600_000, "This is the net book value, not the charge.")],
    [(1_200_000, "This is the book value, not the profit."), (1_500_000, "This is the sale price."), (2_800_000, "This is the accumulated depreciation.")],
    [(172_500, "This is the weighted average valuation."), (150_000, "Values the 150 units at the oldest cost."), (280_000, "This is the FIFO value of the issue.")],
    [(1_100, "Takes the simple average of the two prices."), (1_200, "Uses the latest price only."), (1_000, "Uses the opening price only.")],
    [(119_250, "Applies 20% to the TTC amount."), (500_000, "This is the HT debt, not the impairment."), (96_250, "This is the VAT contained in the debt.")],
    [(1_150_000, "Adds the reversal instead of deducting it."), (450_000, "Deducts both the charge and the reversal."), (1_050_000, "Forgets the reversal.")],
    [(300_000, "This is the part used in the year."), (600_000, "Counts 6 months instead of 9."), (1_200_000, "Treats the whole premium as prepaid.")],
    [(3_324_500, "Adds both the cheques and the deposit."), (2_564_500, "Reverses the treatment of the cheques and the deposit."), (1_614_500, "Forgets the deposit not yet credited.")],
    [(4_150_000, "Adds the overstatement instead of deducting it."), (4_000_000, "Makes no correction."), (3_700_000, "Deducts the overstatement twice.")],
    [(15_000_000, "This is total assets."), (11_500_000, "Forgets to deduct the cash-liabilities."), (9_000_000, "These are the fixed assets only.")],
    [(16_500_000, "Ignores the change in inventory."), (18_100_000, "Adds the inventory increase instead of deducting it."), (12_300_000, "Deducts the opening inventory in full.")],
    [(3_750_000, "Forgets the income tax."), (2_125_000, "Deducts the HAO result instead of adding it."), (4_875_000, "Adds the tax instead of deducting it.")],
    [(2_400_000, "Adds the reversal instead of deducting it."), (700_000, "Deducts the depreciation instead of adding it back."), (1_500_000, "Uses the net result alone.")],
    [(16_500_000, "Adds the disposal instead of deducting it."), (10_500_000, "Deducts the acquisitions."), (15_000_000, "Forgets the disposal.")],
]
_ni = 0
for _i, _s in enumerate(_m1):
    if _s["k"] == "num":
        _d = _DIST[_ni]
        _ni += 1
        _f = lambda v: "FCFA " + f"{v:,}".replace(",", " ")
        assert all(v != _s["answer"] for v, _ in _d)
        _m1[_i] = Q(_s["prompt"].replace(" (FCFA)", "").replace("(FCFA)", ""), _f(_s["answer"]), [(_f(v), w) for v, w in _d],
                    _s["steps"], _s["concept"], _s["skill"], _s["hint"])
assert _ni == len(_DIST) == 23, _ni
assert len(_m1) == 50, len(_m1)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="acl2-paper1-multiple-choice",
    mock=True, time_limit_minutes=90, questions=build(_m1, seed=41)))

# ---------------------------------------------------------------- Mock: Paper 2 practice paper A (preview, 25 parts)
assert 100 * 1_000 + 150 * 1_200 == 280_000 and 150 * 1_200 == 180_000 and (100_000 + 360_000) // 400 == 1_150
assert 250 * 1_150 == 287_500 and 150 * 1_150 == 172_500
assert (2_940_000 - 2_220_000) // 600 == 1_200 and 2_940_000 - 1_800 * 1_200 == 780_000 == 2_220_000 - 1_200 * 1_200
assert 780_000 + 1_500 * 1_200 == 2_580_000 and 780_000 + 2_000 * 1_200 == 3_180_000
assert 4_800_000 // 12_000 == 400 and 35 * 400 == 14_000 and 90_000 + 52_500 + 14_000 == 156_500
assert 1_600_000 // 2_000 == 800 and 800 * 5_000 == 4_000_000 and (1_600_000 + 600_000) // 2_000 == 1_100 and (1_000 - 800) * 100 // 1_000 == 20
assert 200_000 + 1_500_000 - 1_300_000 == 400_000 and 1_000 * 2_000 - 1_600_000 == 400_000
_m2 = []
_b = _m2.append
_P = "Paper 2"
# Q1 stock cards
_b(N("Question 1 (preview, Inventory valuation). Opening inventory 100 units at FCFA 1 000; purchase 300 units at FCFA 1 200; issue 250 units. (a) The FIFO value of the issue is (FCFA)", 280_000,
     [("Issue", "100 x 1 000 + 150 x 1 200 = 280 000.")], "Inventory valuation", "Calculation", "The 100 oldest units come first.", unit="FCFA"))
_b(N("Question 1 (b). The FIFO value of the closing inventory is (FCFA)", 180_000,
     [("Closing", "150 x 1 200 = 180 000.")], "Inventory valuation", "Calculation", "How many units remain, and at which cost?", unit="FCFA"))
_b(N("Question 1 (c). The weighted average unit cost after the purchase is (FCFA)", 1_150,
     [("Average", "460 000 / 400 = 1 150.")], "Inventory valuation", "Calculation", "Total cost / total units.", unit="FCFA"))
_b(N("Question 1 (d). The weighted average value of the issue is (FCFA)", 287_500,
     [("Issue", "250 x 1 150 = 287 500.")], "Inventory valuation", "Calculation", "Units issued x average cost.", unit="FCFA"))
_b(Q("Question 1 (e). When prices are rising, which method gives the higher profit, other things equal?", "FIFO, because the cost of goods sold is lower",
     [("Weighted average, because it raises the cost of sales", "Here the average issue value, 287 500, is higher than FIFO's 280 000, so its profit is lower."),
      ("They give the same profit", "Closing inventory differs: 180 000 against 172 500."),
      ("Neither affects profit", "Inventory valuation changes the cost of goods sold and so profit.")],
     [("Compare", "FIFO issue 280 000 < average 287 500, so FIFO profit is higher by 7 500.")], "Inventory valuation", "Reasoning", "Compare the two issue values."))
# Q2 high-low
_b(Q("Question 2 (preview). Monthly cost at 1 800 hours is FCFA 2 940 000 and at 1 200 hours FCFA 2 220 000. (a) The high-low method uses", "the highest and lowest activity levels with their total costs",
     [("the highest and lowest cost figures only", "The points are chosen by activity, not by cost."), ("the average of all months", "That is not the high-low method."), ("the first and last months", "The method uses the extremes of activity.")],
     [("Method", "Pick the highest and lowest activity levels.")], _P, "Concept", "What does 'high' and 'low' refer to?"))
_b(N("Question 2 (b). The variable cost per hour is (FCFA)", 1_200,
     [("Rate", "(2 940 000 - 2 220 000) / (1 800 - 1 200) = 1 200.")], _P, "Calculation", "Difference in cost over difference in hours.", unit="FCFA"))
_b(N("Question 2 (c). The fixed cost per month is (FCFA)", 780_000,
     [("Fixed", "2 940 000 - 1 800 x 1 200 = 780 000.")], _P, "Calculation", "Total cost minus the variable part.", unit="FCFA"))
_b(N("Question 2 (d). The estimated cost of 1 500 hours is (FCFA)", 2_580_000,
     [("Estimate", "780 000 + 1 500 x 1 200 = 2 580 000.")], _P, "Calculation", "Fixed cost + hours x rate.", unit="FCFA"))
# Q3 overhead absorption
_b(Q("Question 3 (preview). Budgeted overheads are FCFA 4 800 000 and budgeted direct labour hours 12 000. (a) The overhead absorption rate is based on", "budgeted overheads divided by budgeted activity",
     [("actual overheads divided by actual sales", "A rate must be known in advance, so it uses budgets."), ("total costs divided by units sold", "That is a cost per unit."), ("fixed costs divided by contribution", "That is the break-even formula.")],
     [("Rate", "Budgeted overheads / budgeted activity.")], _P, "Concept", "Is the rate set before or after the year?"))
_b(N("Question 3 (b). The rate per direct labour hour is (FCFA)", 400,
     [("Rate", "4 800 000 / 12 000 = 400.")], _P, "Calculation", "Divide overheads by hours.", unit="FCFA"))
_b(N("Question 3 (c). Job 17 takes 35 direct labour hours. The overhead absorbed is (FCFA)", 14_000,
     [("Absorbed", "35 x 400 = 14 000.")], _P, "Calculation", "Hours x rate.", unit="FCFA"))
_b(N("Question 3 (d). Job 17 also uses materials of FCFA 90 000 and labour of FCFA 52 500. Its total cost is (FCFA)", 156_500,
     [("Total", "90 000 + 52 500 + 14 000 = 156 500.")], _P, "Calculation", "Add the three elements.", unit="FCFA"))
# Q4 break-even
_b(N("Question 4 (preview). Price FCFA 5 000; variable cost FCFA 3 000 a unit; fixed costs FCFA 1 600 000 a month. (a) The contribution per unit is (FCFA)", 2_000,
     [("Contribution", "5 000 - 3 000 = 2 000.")], _P, "Calculation", "Price minus variable cost.", unit="FCFA"))
_b(N("Question 4 (b). The break-even point is (units)", 800,
     [("Break-even", "1 600 000 / 2 000 = 800.")], _P, "Calculation", "Fixed costs over contribution.", unit="units"))
_b(N("Question 4 (c). The break-even point in value is (FCFA)", 4_000_000,
     [("Value", "800 x 5 000 = 4 000 000.")], _P, "Calculation", "Units x price.", unit="FCFA"))
_b(N("Question 4 (d). Units to be sold to earn a profit of FCFA 600 000:", 1_100,
     [("Target", "(1 600 000 + 600 000) / 2 000 = 1 100.")], _P, "Calculation", "Add the target to fixed costs.", unit="units"))
_b(N("Question 4 (e). The margin of safety at sales of 1 000 units, as a percentage of sales, is (%)", 20,
     [("Margin", "(1 000 - 800) / 1 000 = 20%.")], _P, "Calculation", "Actual minus break-even, over actual.", unit="%"))
# Q5 budgets
_b(N("Question 5 (preview). A cash budget starts with cash of FCFA 200 000, receipts of FCFA 1 500 000 and payments of FCFA 1 300 000. (a) The closing cash is (FCFA)", 400_000,
     [("Closing", "200 000 + 1 500 000 - 1 300 000 = 400 000.")], _P, "Calculation", "Opening + receipts - payments.", unit="FCFA"))
_b(Q("Question 5 (b). Depreciation is NOT included in a cash budget because", "it is not a payment of cash",
     [("it is a receipt", "Depreciation is an expense."), ("it is paid at the year end", "Depreciation is never paid to anyone."), ("it is always zero", "It can be large but is not a cash flow.")],
     [("Reason", "A cash budget lists cash receipts and payments only.")], _P, "Concept", "Does cash move?"))
_b(Q("Question 5 (c). One benefit of budgeting is that it", "lets a business plan for cash shortages and co-ordinate its activities",
     [("guarantees that profit will be reached", "A budget is a plan, not a guarantee."), ("removes the need for accounting records", "Records are still needed to compare actual with budget."), ("increases sales automatically", "It helps planning but sells nothing itself.")],
     [("Benefit", "Planning, co-ordination, control and motivation.")], _P, "Reasoning", "What does planning allow managers to do?"))
# Q6 marginal costing
_b(N("Question 6 (preview). Using the data of Question 4, the profit at sales of 1 000 units is (FCFA)", 400_000,
     [("Profit", "1 000 x 2 000 - 1 600 000 = 400 000.")], _P, "Calculation", "Total contribution minus fixed costs.", unit="FCFA"))
_b(Q("Question 6 (b). Factory rent of FCFA 300 000 a month whatever the output is", "a fixed cost",
     [("a variable cost", "Variable costs change with output."), ("a semi-variable cost", "No part of it changes with output."), ("a direct material cost", "Rent is not a material.")],
     [("Behaviour", "Fixed in total.")], _P, "Concept", "Does it change with output?"))
_b(Q("Question 6 (c). Raw materials used per unit made are", "a variable cost",
     [("a fixed cost", "The total changes with output."), ("an overhead absorbed per hour", "Materials are a direct cost."), ("a period cost", "They are a cost of production.")],
     [("Behaviour", "Variable in total, fixed per unit.")], _P, "Concept", "Does the total change with output?"))
# Q7 paper
_b(Q("Question 7. The Board's 2023 report says candidates answer five questions in Paper 2: two from Section A and", "all three questions of Section B",
     [("one from Section B", "Section B is compulsory in full."), ("two from Section B", "All three are compulsory."), ("none from Section B", "Section B is management accounting and is compulsory.")],
     [("Fact", "Two of three in Section A (cost accounting); all three in Section B (management accounting).")], _P, "Recall", "Count to five."))
assert len(_m2) == 25, len(_m2)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="acl2-paper2-cost-management-preview",
    mock=True, time_limit_minutes=150, questions=build(_m2, seed=42)))

# ---------------------------------------------------------------- Mock: Paper 3 practice paper A (23 parts)
assert 800_000 * 90 // 100 == 720_000 and 720_000 * 2 // 100 == 14_400 and 720_000 - 14_400 == 705_600
assert 705_600 + 44_400 == 750_000 and vat(750_000) == 144_375 and 750_000 + 144_375 == 894_375
assert (4_000_000 - 400_000) // 5 == 720_000 and 3 * 720_000 == 2_160_000 and 4_000_000 - 2_160_000 == 1_840_000 and 2_000_000 - 1_840_000 == 160_000
assert 477_000 * 10_000 // 11_925 == 400_000 and 400_000 * 30 // 100 == 120_000 and 120_000 - 100_000 == 20_000
assert 720_000 * 10 // 12 == 600_000 and 2_000_000 + 600_000 - 45_000 == 2_555_000
assert 900_000 - 15_000 == 885_000 and 885_000 + 300_000 - 100_000 == 1_085_000
assert 6_300_000 - 6_250_000 == 50_000 and 1_200_000 - 30_000 == 1_170_000
assert 5_000_000 - 400_000 == 4_600_000 and 4_600_000 + 150_000 == 4_750_000 and 4_750_000 * 30 // 100 == 1_425_000 and 4_750_000 - 1_425_000 == 3_325_000
assert 2_800_000 - 300_000 - 500_000 + 200_000 == 2_200_000 and 600_000 + 2_200_000 - 3_000_000 + 500_000 == 300_000
_m3 = []
_c = _m3.append
# Q1 invoice
_c(N("Question 1 (Invoicing and trade reductions). Goods listed at FCFA 800 000; remise 10%; escompte 2% for prompt payment; transport charged FCFA 44 400; VAT 19.25%. (a) The net commercial amount is (FCFA)", 720_000,
     [("Net commercial", "800 000 x 0.90 = 720 000.")], "Invoicing and trade reductions", "Calculation", "Apply the remise only.", unit="FCFA"))
_c(N("Question 1 (b). The net financial amount (after the escompte) is (FCFA)", 705_600,
     [("Escompte", "2% x 720 000 = 14 400."), ("Net financial", "720 000 - 14 400 = 705 600.")], "Invoicing and trade reductions", "Calculation", "The escompte is taken on the net commercial amount.", unit="FCFA"))
_c(N("Question 1 (c). The VAT on the invoice (on net financial amount plus transport) is (FCFA)", 144_375,
     [("Base", "705 600 + 44 400 = 750 000."), ("VAT", "750 000 x 19.25% = 144 375.")], "Value added tax", "Calculation", "Add the transport before calculating VAT.", unit="FCFA"))
_c(N("Question 1 (d). The net to pay is (FCFA)", 894_375,
     [("Net to pay", "750 000 + 144 375 = 894 375.")], "Value added tax", "Calculation", "Base plus VAT.", unit="FCFA"))
# Q2 depreciation and disposal
_c(N("Question 2 (Depreciation methods). A machine bought on 1 January for FCFA 4 000 000 has a residual value of FCFA 400 000 and a life of 5 years (straight line). (a) The annual depreciation is (FCFA)", 720_000,
     [("Annual", "(4 000 000 - 400 000) / 5 = 720 000.")], "Depreciation methods", "Calculation", "Depreciable amount over life.", unit="FCFA"))
_c(N("Question 2 (b). It is sold at the end of year 3. Its net book value then is (FCFA)", 1_840_000,
     [("Accumulated", "3 x 720 000 = 2 160 000."), ("NBV", "4 000 000 - 2 160 000 = 1 840 000.")], "Disposal and trade-in of fixed assets", "Calculation", "Cost minus three years of depreciation.", unit="FCFA"))
_c(N("Question 2 (c). It is sold for FCFA 2 000 000. The profit on disposal is (FCFA)", 160_000,
     [("Profit", "2 000 000 - 1 840 000 = 160 000.")], "Disposal and trade-in of fixed assets", "Calculation", "Proceeds minus book value.", unit="FCFA"))
# Q3 impairment
_c(N("Question 3 (Impairment of current assets). A customer owes FCFA 477 000 TTC (VAT 19.25%); the expected loss is 30%. (a) The impairment needed is (FCFA)", 120_000,
     [("HT", "477 000 / 1.1925 = 400 000."), ("Impairment", "30% x 400 000 = 120 000.")], "Impairment of current assets", "Calculation", "Remove VAT first.", unit="FCFA"))
_c(N("Question 3 (b). Impairment of FCFA 100 000 was already held. The increase to be charged is (FCFA)", 20_000,
     [("Increase", "120 000 - 100 000 = 20 000.")], "Impairment of current assets", "Calculation", "Compare the need with the amount held.", unit="FCFA"))
_c(Q("Question 3 (c). The entry for the increase is", "debit 6594, credit 491",
     [("debit 491, credit 7594", "That is a reversal."), ("debit 651, credit 416", "That records a lost debt."), ("debit 416, credit 411", "That transfers the debt; the impairment is a separate entry.")],
     [("Entry", "Charge 6594; impairment account 491.")], "Impairment of current assets", "Application", "An increase is a charge."))
# Q4 accruals
_c(N("Question 4 (Accruals and prepayments). Insurance of FCFA 720 000 for 12 months was paid on 1 November. The prepaid amount at 31 December is (FCFA)", 600_000,
     [("Months", "10 months belong to the next year."), ("Amount", "10/12 x 720 000 = 600 000.")], "Accruals and prepayments", "Calculation", "Two months are used.", unit="FCFA"))
_c(Q("Question 4 (b). Unpaid December electricity of FCFA 45 000 is recorded as", "an expense of the year and a liability in 408",
     [("a prepaid expense in 476", "Nothing has been paid in advance."), ("income received in advance", "It is an expense, not income."), ("no entry until it is paid", "The accrual basis requires the expense in the year used.")],
     [("Accrual", "Debit electricity, credit 408.")], "Accruals and prepayments", "Concept", "Used but not yet invoiced."))
_c(N("Question 4 (c). Result before adjustments FCFA 2 000 000. After the prepaid insurance (+600 000) and the accrued electricity (-45 000), the result is (FCFA)", 2_555_000,
     [("Result", "2 000 000 + 600 000 - 45 000 = 2 555 000.")], "Accruals and prepayments", "Calculation", "Add the prepayment; deduct the accrual.", unit="FCFA"))
# Q5 bank
_c(N("Question 5 (Bank reconciliation). Account 521 shows a debit balance of FCFA 900 000; bank charges of FCFA 15 000 are not yet in the books. The adjusted 521 balance is (FCFA)", 885_000,
     [("Adjusted", "900 000 - 15 000 = 885 000.")], "Bank reconciliation", "Calculation", "Charges reduce the bank balance.", unit="FCFA"))
_c(N("Question 5 (b). Cheques of FCFA 300 000 are unpresented and a deposit of FCFA 100 000 is not yet credited. The statement shows a credit balance of (FCFA)", 1_085_000,
     [("Statement", "885 000 + 300 000 - 100 000 = 1 085 000.")], "Bank reconciliation", "Calculation", "The bank has not yet paid the cheques.", unit="FCFA"))
# Q6 errors
_c(Q("Question 6 (Correction of errors). A trial balance has debits of FCFA 6 300 000 and credits of FCFA 6 250 000. The suspense account is opened with", "a credit of 50 000",
     [("a debit of 50 000", "Debits are already larger; the credit side is short."), ("a credit of 6 250 000", "Only the difference is entered."), ("a debit of 6 300 000", "Only the difference is entered.")],
     [("Suspense", "6 300 000 - 6 250 000 = 50 000 short on the credit side.")], "Correction of errors", "Application", "Which side is short?"))
_c(N("Question 6 (b). Draft profit FCFA 1 200 000. Repairs of FCFA 30 000 were wrongly debited to a fixed asset. The corrected profit is (FCFA)", 1_170_000,
     [("Corrected", "1 200 000 - 30 000 = 1 170 000.")], "Correction of errors", "Calculation", "An expense was hidden.", unit="FCFA"))
# Q7 income statement
_c(N("Question 7 (The income statement and intermediate balances). Operating result FCFA 5 000 000; financial result FCFA -400 000. The result of ordinary activities is (FCFA)", 4_600_000,
     [("RAO", "5 000 000 - 400 000 = 4 600 000.")], "The income statement and intermediate balances", "Calculation", "Add the financial result.", unit="FCFA"))
_c(N("Question 7 (b). HAO result +150 000; income tax at a teaching rate of 30% on (RAO + HAO). The net result is (FCFA)", 3_325_000,
     [("Taxable", "4 600 000 + 150 000 = 4 750 000."), ("Tax", "30% x 4 750 000 = 1 425 000."), ("Net", "4 750 000 - 1 425 000 = 3 325 000.")], "The income statement and intermediate balances", "Calculation", "Tax first, then subtract.", unit="FCFA"))
# Q8 cash flow
_c(N("Question 8 (The cash flow statement). CAFG FCFA 2 800 000; inventories rose by 300 000; receivables rose by 500 000; current liabilities rose by 200 000. The operating cash flow is (FCFA)", 2_200_000,
     [("Operating", "2 800 000 - 300 000 - 500 000 + 200 000 = 2 200 000.")], "The cash flow statement", "Calculation", "Use signs for each working capital change.", unit="FCFA"))
_c(N("Question 8 (b). Opening net cash FCFA 600 000; investing flow -3 000 000; financing flow +500 000. The closing net cash is (FCFA)", 300_000,
     [("Closing", "600 000 + 2 200 000 - 3 000 000 + 500 000 = 300 000.")], "The cash flow statement", "Calculation", "Add the three flows to the opening net cash.", unit="FCFA"))
_c(Q("Question 8 (c). The firm is profitable but its net cash fell from 600 000 to 300 000. The best explanation from the data is that", "investment of 3 000 000 exceeded the operating cash flow of 2 200 000 and new financing of 500 000 did not cover the gap",
     [("depreciation reduced the cash", "Depreciation is not a payment of cash."), ("the firm made a loss", "The question says it was profitable."), ("financing flows were negative", "Financing was +1 000 000.")],
     [("Interpretation", "2 200 000 + 500 000 = 2 700 000 comes in, 3 000 000 goes out: net cash falls by 300 000, from 600 000 to 300 000.")], "The cash flow statement", "Interpretation", "Compare the flows."))
assert len(_m3) == 22, len(_m3)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="acl2-paper3-financial-accounting",
    mock=True, time_limit_minutes=150, questions=build(_m3, seed=43)))
