"""A Level Accounting (0705), Upper Sixth: practice sets for Financial Statement Analysis; Cost Accounting: Full &
Marginal Costing; Budgetary Control, Standard Costing & Capital Budgeting; and the Examination module, with Paper 1 mock
exam A, Paper 2 practice paper A and Paper 3 practice paper A.

Draft content. Exam facts are only those of the Board's 2023 Advanced Level report for 0705 (Paper 1: 50 compulsory
multiple-choice questions; Paper 2: Cost and Management Accounting; Paper 3: Financial Accounting; weighted 30, 30, 40).
Time limits of the mock papers are KKEVO practice settings. Essays and long statements cannot be auto-marked, so the
practice papers use numbered questions with multiple-choice and numeric parts. All FCFA figures are invented for
practice. Every answer and every distractor figure is computed in this file with exact arithmetic (distractors are the
results of the typical wrong methods), and assertions check the key results.
"""

import random
from fractions import Fraction as Fr

from .dsl import *  # noqa: F403

COURSE = ("accounting", "upper-sixth")

M_PART = "Partnership Accounting"
M_COMP = "Company Formation, Share Capital & Debentures"
M_MOD = "Modification of Capital, Taxation, Amalgamation & Liquidation"
M_FSA = "Financial Statement Analysis"
M_COST = "Cost Accounting: Full & Marginal Costing"
M_BUD = "Budgetary Control, Standard Costing & Capital Budgeting"
M_EXAM = "Examination"

# exact topic titles (used as `concept` in the mock papers)
T_APPROP = "Appropriation of profits and partners' accounts"
T_GOODW = "Revaluation and goodwill"
T_ADMIT = "Admission of a partner"
T_RETIRE = "Retirement and death of a partner"
T_DISSOL = "Dissolution of a partnership"
T_FORM = "Company formation under OHADA"
T_ISSUE = "Issue of shares"
T_CAPPROP = "Appropriation of company profits"
T_DEBEN = "Debentures"
T_INCR = "Increase of capital"
T_REDUC = "Reduction and amortization of capital"
T_TAX = "Company tax"
T_MERGE = "Mergers"
T_LIQ = "Liquidation"
T_FUNC = "The functional balance sheet"
T_FIN = "The financial balance sheet"
T_RATIO = "Ratio analysis"
T_OVH = "Cost classification and overhead allocation"
T_STOCK = "Stock valuation and cost price"
T_JOB = "Job, batch and process costing"
T_ABC = "Activity-based costing"
T_MARG = "Marginal costing and break-even analysis"
T_BUDG = "Budgets and the cash budget"
T_FLEX = "Flexible budgets"
T_STD = "Standard costing and variances"
T_INV = "Investment appraisal"


def n(x):
    if isinstance(x, Fr):
        assert x.denominator == 1, x
        x = int(x)
    s = f"{abs(x):,}".replace(",", " ")
    return ("-" if x < 0 else "") + s


def F_(x):
    return f"FCFA {n(x)}"


class _Bag:
    """Deals correct-option positions 0-3 in shuffled blocks of four, so they are spread evenly."""

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


def Q(prompt, correct, wrongs, steps, concept, skill, hint, pos=None, diagram="", diagram_alt=""):
    """Four-option MC. `wrongs` = [(text, why)] x3; the correct option goes to a balanced position."""
    assert len(wrongs) == 3
    texts = [correct] + [w for w, _ in wrongs]
    assert len(set(texts)) == 4, texts
    pos = BAG.next() if pos is None else pos
    choices = [C(w, why=y) for w, y in wrongs]
    choices.insert(pos, C(correct, correct=True))
    return MC(prompt, choices, steps=[S(a, text=b) for a, b in steps], concept=concept, skill=skill, hint=hint,
              diagram=diagram, diagram_alt=diagram_alt)


def NM(prompt, answer, wrongs, steps, concept, skill, hint, fmt=F_):
    """A numeric question set as four-option MC. `wrongs` = [(number, why)] x3 (results of typical wrong methods)."""
    return Q(prompt, fmt(answer), [(fmt(v), w) for v, w in wrongs], steps, concept, skill, hint)


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit="FCFA"):
    if isinstance(answer, Fr):
        answer = float(answer)
    return NUM(prompt, answer, steps=[S(a, text=b) for a, b in steps], tolerance=tol, unit=unit, concept=concept,
               skill=skill, hint=hint)


SETS = []

# ====================================================================== 1. The functional balance sheet
use(101)
_a_sr = 30_000_000 + 9_000_000 + 1_000_000 + 12_000_000
_a_frng = _a_sr - 45_000_000
_a_bfe = 8_000_000 + 9_000_000 + 2_000_000 - (7_000_000 + 3_000_000)
_a_tn = _a_frng - _a_bfe
assert (_a_sr, _a_frng, _a_bfe, _a_tn) == (52_000_000, 7_000_000, 9_000_000, -2_000_000)
_a_days = Fr(9_000_000 * 360, 162_000_000)
assert _a_days == 20

SETS.append(practice_set(
    module=M_FSA, topic=T_FUNC, title="FRNG, BFR and net cash from a restated balance sheet", lesson="acu2-functional-balance-sheet",
    questions=[
        Q("In the functional balance sheet, fixed assets are shown at",
          "gross value, with accumulated depreciation added to stable resources",
          [("net book value, as in the published balance sheet", "Net values belong to the financial (liquidity) approach, not the functional one."),
           ("market value at the balance sheet date", "Market values are used to correct the financial balance sheet, not the functional one."),
           ("gross value, with accumulated depreciation deducted from equity", "Depreciation is a resource kept in the business; it is added to stable resources, not deducted.")],
          [("Recall the principle", "The functional approach studies how the whole original cost of the assets was financed."),
           ("So", "Assets at gross value; depreciation and impairment of fixed assets join stable resources.")],
          "Gross values in the functional balance sheet", "Recall", "Think about what the firm had to finance when it bought the assets."),
        Q("A company owes FCFA 4 000 000 to the supplier of a new machine. In the functional balance sheet this debt is",
          "a non-operating (HAO) current liability",
          [("an operating current liability, like trade payables", "Trade payables arise from buying goods and services for the operating cycle; a machine is an investment."),
           ("a stable resource", "It is short-term credit from a supplier, not long-term financing such as a bank loan."),
           ("a cash liability", "Cash liabilities are bank overdrafts and short-term bank credit, not supplier debts.")],
          [("Identify the cycle", "Buying a fixed asset belongs to the investment cycle, outside the operating cycle."),
           ("Classify", "A short-term debt outside the operating cycle is a non-operating (HAO) liability.")],
          "Operating and non-operating items", "Concept", "Ask which cycle the debt comes from."),
        N("Equity FCFA 30 000 000; accumulated depreciation of fixed assets FCFA 9 000 000; provisions for risks and charges FCFA 1 000 000; "
          "long-term loans FCFA 12 000 000; gross fixed assets FCFA 45 000 000. Calculate the net global working capital (FRNG) in FCFA.",
          _a_frng,
          [("Stable resources", "30 000 000 + 9 000 000 + 1 000 000 + 12 000 000 = 52 000 000."),
           ("FRNG", "52 000 000 − 45 000 000 = 7 000 000.")],
          "Net global working capital", "Calculation", "Add up every stable resource first, including depreciation."),
        NM("Inventory FCFA 8 000 000; trade receivables FCFA 9 000 000; discounted bills not yet due FCFA 2 000 000; trade payables FCFA 7 000 000; "
           "tax and social payables FCFA 3 000 000. What is the operating working capital requirement?",
           _a_bfe,
           [(7_000_000, "This leaves out the discounted bills, which must be added back to receivables."),
            (5_000_000, "This subtracts the discounted bills instead of adding them back."),
            (12_000_000, "This deducts only the trade payables and forgets the tax and social payables.")],
           [("Operating assets", "8 000 000 + 9 000 000 + 2 000 000 = 19 000 000."),
            ("Operating liabilities", "7 000 000 + 3 000 000 = 10 000 000."),
            ("BFE", "19 000 000 − 10 000 000 = 9 000 000.")],
           "Operating working capital requirement", "Calculation", "Restate the discounted bills before you subtract."),
        NM("Using FRNG = FCFA 7 000 000 and BFR = FCFA 9 000 000, the net cash is",
           _a_tn,
           [(2_000_000, "This calculates BFR − FRNG; net cash is FRNG − BFR."),
            (16_000_000, "This adds the two figures."),
            (-9_000_000, "This takes BFR alone and forgets FRNG.")],
           [("Formula", "TN = FRNG − BFR."),
            ("Calculate", "7 000 000 − 9 000 000 = −2 000 000: the firm depends on short-term bank credit.")],
           "Net cash", "Calculation", "Which figure is subtracted from which?"),
        Q("An analyst forgot to restate FCFA 3 000 000 of discounted bills not yet due. After the correction",
          "BFR rises by 3 000 000, net cash falls by 3 000 000 and FRNG is unchanged",
          [("FRNG rises by 3 000 000 and BFR is unchanged", "Discounted bills are short-term items; they do not touch the stable blocks."),
           ("BFR falls by 3 000 000 and net cash rises by 3 000 000", "Adding the bills back to receivables increases BFR, and the bank credit increases cash liabilities."),
           ("nothing changes, because the bank has already paid", "Until the bill is due the firm still bears the risk; the restatement is required.")],
          [("Receivables", "+3 000 000 to trade receivables, so BFR + 3 000 000."),
           ("Cash liabilities", "+3 000 000 to cash liabilities, so net cash − 3 000 000."),
           ("Check", "FRNG − BFR = TN still holds: FRNG unchanged, both other figures move by 3 000 000.")],
          "Restating discounted bills", "Reasoning", "The bills are added to two places. Which ones?"),
        Q("A firm has FRNG FCFA 5 000 000, BFR FCFA 6 500 000 and net cash −FCFA 1 500 000. Which comment is best?",
          "Fixed assets are financed by stable resources, but part of the operating cycle is financed by short-term bank credit",
          [("The firm breaks the rule of financial equilibrium because FRNG is negative", "FRNG is positive (5 000 000), so stable resources cover stable uses."),
           ("The firm has idle cash that should be invested", "Net cash is negative: there is no idle cash."),
           ("The firm should reduce FRNG to improve net cash", "Reducing FRNG would make net cash even more negative, since TN = FRNG − BFR.")],
          [("FRNG", "Positive: stable uses are covered."),
           ("TN", "Negative: BFR exceeds FRNG by 1 500 000, filled by overdraft or discounting.")],
          "Interpreting the functional balance sheet", "Interpretation", "Look at the sign of each figure in turn."),
        N("A company's operating BFR is FCFA 9 000 000 and its turnover excluding VAT is FCFA 162 000 000. Express the operating BFR in days of turnover "
          "(360-day year).",
          _a_days,
          [("Formula", "Days = BFE ÷ turnover excluding VAT × 360."),
           ("Calculate", "9 000 000 ÷ 162 000 000 × 360 = 20 days.")],
          "BFR in days of turnover", "Calculation", "Divide BFE by turnover, then multiply by the days in the year.", unit="days"),
    ]))

# ====================================================================== 2. The financial balance sheet
use(102)
_b_net = 50_000_000 - 4_000_000 + 5_000_000 - 1_500_000
assert _b_net == 49_500_000
_b_net2 = 50_000_000 - 4_000_000 + 5_000_000 - 1_500_000 - 0
_b_vm = Fr(_b_net2, 5_000)
assert _b_vm == 9_900 and Fr(50_000_000, 5_000) == 10_000 and Fr(53_500_000, 5_000) == 10_700 and Fr(44_500_000, 5_000) == 8_900
_b_fwc = 26_000_000 + (12_000_000 - 2_000_000) - 33_000_000
assert _b_fwc == 3_000_000
_b_cr = Fr(13_500_000, 9_000_000)
assert _b_cr == Fr(3, 2)

SETS.append(practice_set(
    module=M_FSA, topic=T_FIN, title="Restatements, net assets and liquidity in the financial balance sheet", lesson="acu2-financial-balance-sheet",
    questions=[
        Q("The financial (liquidity) balance sheet classifies assets and liabilities",
          "by liquidity and maturity, using a one-year dividing line",
          [("by cycle: investment, financing, operating and cash", "That is the functional balance sheet."),
           ("in the order of the SYSCOHADA account classes 1 to 5", "Account classes organise the ledger, not this analysis."),
           ("by gross value from the largest to the smallest", "Size is not the criterion, and the financial approach uses net or market values.")],
          [("Purpose", "The lender wants to know what can be paid and when."),
           ("Criterion", "Assets by how soon they become cash; debts by how soon they fall due; the line is one year.")],
          "Classification in the financial balance sheet", "Recall", "Think of the banker's question: when?"),
        Q("Out of the year's profit, the general meeting has decided a dividend of FCFA 2 500 000 payable next month. In the financial balance sheet",
          "equity falls by 2 500 000 and short-term debts rise by 2 500 000",
          [("nothing changes until the dividend is paid", "Once decided, the dividend is owed to shareholders within the year."),
           ("long-term debts rise by 2 500 000", "It is payable next month, so it is a short-term debt."),
           ("equity rises by 2 500 000", "Paying shareholders reduces what remains for them; it does not add to equity.")],
          [("Nature", "A decided dividend is a debt to shareholders."),
           ("Maturity", "Payable next month, so below the one-year line; equity is reduced by the same amount.")],
          "Dividend to be paid", "Concept", "Is the dividend still the shareholders' capital, or money owed to them?"),
        N("Equity per books FCFA 50 000 000 includes profit from which a dividend of FCFA 4 000 000 is to be paid. Land is worth FCFA 5 000 000 more than its book value, "
          "and an intangible asset of FCFA 1 500 000 has no resale value. Calculate the adjusted net assets in FCFA.",
          _b_net,
          [("Start from book equity", "50 000 000."),
           ("Adjust", "− 4 000 000 dividend + 5 000 000 gain − 1 500 000 non-value asset."),
           ("Result", "49 500 000.")],
          "Adjusted net assets", "Calculation", "Each restatement either adds to or deducts from equity."),
        NM("A company has adjusted net assets of FCFA 49 500 000 and 5 000 shares of FCFA 10 000. What is the net asset value of one share?",
           _b_vm,
           [(10_000, "This is the nominal value (or book equity 50 000 000 ÷ 5 000), not the restated value."),
            (10_700, "This does not deduct the dividend to be paid (53 500 000 ÷ 5 000)."),
            (8_900, "This leaves out the gain on land (44 500 000 ÷ 5 000).")],
           [("Formula", "Net asset value per share = adjusted net assets ÷ number of shares."),
            ("Calculate", "49 500 000 ÷ 5 000 = 9 900.")],
           "Net asset value of a share", "Calculation", "Divide the restated net assets by the number of shares."),
        NM("Adjusted equity FCFA 26 000 000; bank loan FCFA 12 000 000 of which FCFA 2 000 000 is repayable within the year; assets over one year FCFA 33 000 000. "
           "The financial working capital is",
           _b_fwc,
           [(5_000_000, "This keeps the whole loan as long-term; the 2 000 000 instalment is short-term."),
            (-7_000_000, "This leaves out the long-term debts, which are part of permanent capital."),
            (-3_000_000, "The sign is reversed: permanent capital minus assets over one year.")],
           [("Permanent capital", "26 000 000 + (12 000 000 − 2 000 000) = 36 000 000."),
            ("Working capital", "36 000 000 − 33 000 000 = 3 000 000.")],
           "Financial working capital", "Calculation", "Which part of the loan is really long-term?"),
        N("Assets under one year total FCFA 13 500 000 and debts under one year total FCFA 9 000 000. Calculate the current ratio (to 2 decimal places).",
          _b_cr,
          [("Formula", "Current ratio = assets under one year ÷ debts under one year."),
           ("Calculate", "13 500 000 ÷ 9 000 000 = 1.50.")],
          "Current ratio", "Calculation", "Short-term assets over short-term debts.", tol=0.01, unit=""),
        Q("A firm's financial balance sheet gives a current ratio of 0.8 and a solvency ratio (total assets ÷ total debts) of 2.5. The best comment is",
          "it is solvent in the long run but may struggle to pay debts falling due within the year",
          [("it is insolvent and should be liquidated", "Assets are 2.5 times the debts, so creditors are well covered overall."),
           ("it has too much idle cash", "A current ratio below 1 shows a shortage, not a surplus, of short-term assets."),
           ("both ratios show a strong short-term position", "The current ratio below 1 is a short-term warning sign.")],
          [("Solvency", "2.5: overall, assets far exceed debts."),
           ("Liquidity", "0.8: short-term assets do not cover short-term debts; a timing problem.")],
          "Liquidity and solvency", "Interpretation", "Separate the long-run question from the short-run one."),
        Q("An analyst moves a safety stock of FCFA 2 000 000 from 'assets under one year' to 'assets over one year'. The financial working capital",
          "falls by 2 000 000",
          [("rises by 2 000 000", "Assets over one year increase, so permanent capital minus them is smaller."),
           ("does not change, because total assets are the same", "Totals are the same, but the split across the one-year line changes."),
           ("falls by 4 000 000", "The stock is moved once; the working capital changes by its amount only.")],
          [("Bottom view", "Assets under one year fall by 2 000 000; short-term debts unchanged."),
           ("Result", "Working capital = assets under one year − short-term debts falls by 2 000 000.")],
          "Safety stock restatement", "Reasoning", "Use the bottom-of-the-balance-sheet formula."),
    ]))

# ====================================================================== 3. Ratio analysis
use(103)
_c_s, _c_cos, _c_pbit, _c_int, _c_eq, _c_ltd = 150_000_000, 105_000_000, 15_000_000, 3_000_000, 60_000_000, 40_000_000
_c_i0, _c_i1, _c_rec, _c_cash, _c_cl = 12_000_000, 16_000_000, 25_000_000, 2_000_000, 20_000_000
_c_data = ("Data (FCFA): sales, all on credit, 150 000 000; cost of sales 105 000 000; profit before interest and tax 15 000 000; interest 3 000 000; "
           "equity 60 000 000; long-term loan 40 000 000; inventory: opening 12 000 000, closing 16 000 000; trade receivables 25 000 000; "
           "bank 2 000 000; current liabilities 20 000 000. ")
assert Fr(_c_s - _c_cos, _c_s) == Fr(30, 100)
assert Fr(_c_pbit, _c_eq + _c_ltd) == Fr(15, 100)
_c_qr = Fr(_c_i1 + _c_rec + _c_cash - _c_i1, _c_cl)
assert _c_qr == Fr(135, 100) and Fr(_c_i1 + _c_rec + _c_cash, _c_cl) == Fr(215, 100)
_c_it = Fr(_c_cos) / Fr(_c_i0 + _c_i1, 2)
assert _c_it == Fr(15, 2)
assert Fr(_c_rec * 360, _c_s) == 60 and Fr(_c_ltd, _c_eq + _c_ltd) == Fr(40, 100) and Fr(_c_pbit, _c_int) == 5


SETS.append(practice_set(
    module=M_FSA, topic=T_RATIO, title="Calculating and interpreting the four families of ratios", lesson="acu2-ratio-analysis",
    questions=[
        Q(_c_data + "The gross margin is",
          "30.0%",
          [("42.9%", "This divides gross profit by cost of sales (a mark-up), not by sales."),
           ("10.0%", "This is the PBIT margin: 15 000 000 ÷ 150 000 000."),
           ("70.0%", "This is cost of sales as a percentage of sales.")],
          [("Gross profit", "150 000 000 − 105 000 000 = 45 000 000."),
           ("Margin", "45 000 000 ÷ 150 000 000 = 30.0%.")],
          "Gross margin", "Calculation", "Gross profit is measured against sales."),
        N(_c_data + "Calculate the return on capital employed (ROCE) as a percentage, with capital employed = equity + long-term loan.",
          15,
          [("Capital employed", "60 000 000 + 40 000 000 = 100 000 000."),
           ("ROCE", "15 000 000 ÷ 100 000 000 × 100 = 15%.")],
          "Return on capital employed", "Calculation", "Use profit before interest and tax.", unit="%"),
        Q(_c_data + "The quick (acid test) ratio is",
          "1.35",
          [("2.15", "This is the current ratio: inventory was not removed."),
           ("0.80", "This is inventory ÷ current liabilities."),
           ("1.25", "This uses receivables only and leaves out the bank balance.")],
          [("Quick assets", "25 000 000 + 2 000 000 = 27 000 000 (current assets without inventory)."),
           ("Ratio", "27 000 000 ÷ 20 000 000 = 1.35.")],
          "Quick ratio", "Calculation", "Which current asset is left out of the quick ratio?"),
        N(_c_data + "Calculate the inventory turnover (number of times), using average inventory.",
          _c_it,
          [("Average inventory", "(12 000 000 + 16 000 000) ÷ 2 = 14 000 000."),
           ("Turnover", "105 000 000 ÷ 14 000 000 = 7.5 times.")],
          "Inventory turnover", "Calculation", "Compare cost of sales with average inventory.", tol=0.05, unit="times"),
        Q(_c_data + "Using a 360-day year, the receivables collection period is",
          "60 days",
          [("85.7 days", "This divides by cost of sales; receivables arise from sales."),
           ("16.7 days", "This expresses receivables as a percentage of sales and stops there."),
           ("6 days", "This is sales ÷ receivables, the number of times receivables turn over, not days.")],
          [("Formula", "Receivables ÷ credit sales × 360."),
           ("Calculate", "25 000 000 ÷ 150 000 000 × 360 = 60 days.")],
          "Receivables collection period", "Calculation", "Receivables are compared with credit sales."),
        Q(_c_data + "Gearing, defined as long-term debt ÷ (equity + long-term debt), is",
          "40.0%",
          [("66.7%", "This is long-term debt ÷ equity (the debt-to-equity ratio)."),
           ("60.0%", "This is equity ÷ capital employed."),
           ("33.3%", "This divides the loan by total equity and liabilities including current liabilities (40 ÷ 120).")],
          [("Capital employed", "60 000 000 + 40 000 000 = 100 000 000."),
           ("Gearing", "40 000 000 ÷ 100 000 000 = 40%.")],
          "Gearing", "Calculation", "Use the definition given in the question."),
        N(_c_data + "Calculate the interest cover (number of times).",
          5,
          [("Formula", "Interest cover = profit before interest and tax ÷ interest."),
           ("Calculate", "15 000 000 ÷ 3 000 000 = 5 times.")],
          "Interest cover", "Calculation", "How many times could the interest be paid out of operating profit?", unit="times"),
        Q("A firm's current ratio rose from 1.6 to 2.4 while its inventory period rose from 35 to 70 days and its cash balance fell. Which interpretation is best?",
          "Liquidity looks better, but the rise comes mainly from slow-moving inventory, so the firm may actually be short of cash",
          [("Liquidity has clearly improved, so no action is needed", "The ratio rose because inventory piled up, while cash fell; this is not real improvement."),
           ("The firm is now insolvent", "A current ratio of 2.4 does not show insolvency; the issue is the quality of current assets."),
           ("Inventory turnover has improved", "A longer inventory period means slower turnover, not faster.")],
          [("Find the driver", "Inventory days doubled, so current assets grew through stock, not cash."),
           ("Judge", "Liquidity depends on how quickly assets become cash; check the quick ratio and reduce stock.")],
          "Interpreting liquidity ratios", "Interpretation", "Ask which current asset made the ratio rise."),
    ]))

# ====================================================================== 4. Cost classification and overhead allocation
use(104)
_d_vc = Fr(1_700_000 - 950_000, 4_000 - 1_500)
_d_fc = 950_000 - _d_vc * 1_500
assert (_d_vc, _d_fc) == (300, 500_000)
_d_inc = 9_800_000 - 500_000 + 3_000_000 * 10 // 100
assert _d_inc == 9_600_000
_d_A = Fr(870_000 + Fr(1, 5) * 400_000) / (1 - Fr(1, 5) * Fr(1, 4))
_d_B = 400_000 + Fr(1, 4) * _d_A
assert (_d_A, _d_B) == (1_000_000, 650_000)
_d_P = Fr(3, 10) * _d_A + Fr(1, 2) * _d_B
assert _d_P == 625_000 and Fr(3, 10) * 870_000 + Fr(1, 2) * 400_000 == 461_000
assert Fr(2_880_000, 1_600) == 1_800

SETS.append(practice_set(
    module=M_COST, topic=T_OVH, title="High-low, incorporated charges and reciprocal service centres", lesson="acu2-cost-classification-overheads",
    questions=[
        Q("In a furniture workshop that makes tables and chairs, which cost is indirect?",
          "Rent of the workshop",
          [("Wood used for a particular table", "Wood can be measured for each table, so it is a direct cost."),
           ("Hours of the carpenter who assembles a chair, paid by the hour", "These hours are recorded per product, so they are direct labour."),
           ("Varnish bought for one customer's order only", "It is bought for one order, so it can be traced directly.")],
          [("Test", "Can the cost be traced to one product without calculation?"),
           ("Answer", "Rent is shared by all products, so it must be distributed: it is indirect.")],
          "Direct and indirect costs", "Concept", "Ask whether the cost can be traced to one product."),
        Q("When production rises from 1 000 to 2 000 units within the normal range, a fixed cost",
          "stays the same in total, so the fixed cost per unit halves",
          [("doubles in total and stays the same per unit", "That is the behaviour of a variable cost."),
           ("stays the same per unit and rises in total", "A fixed cost is fixed in total, not per unit."),
           ("falls in total because of economies of scale", "The total does not change within the relevant range.")],
          [("Total", "A fixed cost does not change with activity within the range."),
           ("Per unit", "The same total is spread over twice as many units, so the cost per unit halves.")],
          "Fixed and variable cost behaviour", "Concept", "Separate the total from the cost per unit."),
        N("The lowest activity of the year was 1 500 machine hours with a power cost of FCFA 950 000; the highest was 4 000 hours with FCFA 1 700 000. "
          "Using the high-low method, calculate the fixed part of the monthly power cost in FCFA.",
          _d_fc,
          [("Variable cost per hour", "(1 700 000 − 950 000) ÷ (4 000 − 1 500) = 750 000 ÷ 2 500 = 300."),
           ("Fixed cost", "950 000 − 1 500 × 300 = 500 000."),
           ("Check", "500 000 + 4 000 × 300 = 1 700 000.")],
          "High-low method", "Calculation", "Find the variable cost per hour first."),
        NM("Charges in the financial accounts FCFA 9 800 000 include an exceptional (HAO) loss of FCFA 500 000. The owner's capital of FCFA 3 000 000 is remunerated at 10%. "
           "The incorporated charges are",
           _d_inc,
           [(10_600_000, "This adds the HAO loss instead of removing it."),
            (9_300_000, "This removes the HAO loss but forgets the supplementary charge."),
            (10_000_000, "This reverses both adjustments.")],
           [("Supplementary charge", "10% × 3 000 000 = 300 000."),
            ("Incorporated charges", "9 800 000 − 500 000 + 300 000 = 9 600 000.")],
           "Incorporated charges", "Calculation", "Remove what is not a normal cost; add what is missing."),
        N("Service centres A and B serve each other: A = 870 000 + 0.2B and B = 400 000 + 0.25A. Calculate the total of A to be distributed, in FCFA.",
          _d_A,
          [("Substitute", "A = 870 000 + 0.2(400 000 + 0.25A) = 950 000 + 0.05A."),
           ("Solve", "0.95A = 950 000, so A = 1 000 000 (and B = 400 000 + 250 000 = 650 000).")],
          "Reciprocal services", "Calculation", "Replace B by its expression in the equation for A."),
        NM("With A = 1 000 000 and B = 650 000 as totals after reciprocal services (primary amounts A 870 000, B 400 000), main centre P receives 30% of A and 50% of B. "
           "How much does P receive in secondary distribution?",
           _d_P,
           [(461_000, "This applies the percentages to the primary amounts instead of the totals after reciprocal services."),
            (300_000, "This is only the share from A."),
            (325_000, "This is only the share from B.")],
           [("From A", "30% × 1 000 000 = 300 000."),
            ("From B", "50% × 650 000 = 325 000."),
            ("Total", "625 000.")],
           "Secondary distribution", "Application", "Apply each percentage to the total after reciprocal services."),
        N("After secondary distribution the assembly centre totals FCFA 2 880 000. Its unit of work is the direct labour hour and 1 600 hours were worked. "
          "Calculate the cost of the unit of work in FCFA.",
          1_800,
          [("Formula", "Centre total ÷ number of units of work."),
           ("Calculate", "2 880 000 ÷ 1 600 = 1 800 per labour hour.")],
          "Cost of the unit of work", "Calculation", "Divide the centre total by the hours."),
        Q("After completing the distribution table, which check proves that no overhead has been lost or counted twice?",
          "The main centres' totals add up to the total of the primary distribution, and each service centre ends at zero",
          [("Each main centre has the same total", "Main centres differ in size; equal totals prove nothing."),
           ("The cost of every unit of work is a whole number", "Costs per unit of work are often rounded; this is not a check."),
           ("The service centres' totals after reciprocal services equal their primary amounts", "After reciprocal services the totals are larger than the primary amounts.")],
          [("Conservation", "Secondary distribution only moves money between centres."),
           ("Check", "So the sum of the main centres must equal the sum of the primary distribution, with service centres at zero.")],
          "Checking the distribution table", "Reasoning", "Secondary distribution moves money; it does not create it."),
    ]))

# ====================================================================== 5. Stock valuation and cost price
use(105)
_e_pc = 2_000 * 650 + 2_000 * 30
assert _e_pc == 1_360_000
_e_cump = Fr(800 * 700 + 1_200 * 760, 2_000)
assert _e_cump == 736
_e_fifo = 800 * 700 + 700 * 760
assert (_e_fifo, 1_500 * _e_cump, 1_200 * 760 + 300 * 700, 1_500 * 700) == (1_092_000, 1_104_000, 1_122_000, 1_050_000)
_e_prod = 1_500 * _e_cump + 600 * 1_400 + 200 * 2_500
assert _e_prod == 2_444_000
_e_fc = Fr(218_000 + _e_prod, 1_100)
assert _e_fc == 2_420
_e_sales = 900 * 3_000
_e_cp = 900 * _e_fc + _e_sales * 5 // 100
assert (_e_sales, _e_cp, _e_sales - _e_cp) == (2_700_000, 2_313_000, 387_000)
assert (900 * 2_444 + 135_000, 900 * 2_420, 2_444_000 + 135_000) == (2_334_600, 2_178_000, 2_579_000)
_e_fr = 1_800_000 + 120_000 - 90_000
assert _e_fr == 1_830_000

_e_stock = "Opening stock 800 units at FCFA 700; purchases 1 200 units at FCFA 760 (purchase cost); 1 500 units issued. "
SETS.append(practice_set(
    module=M_COST, topic=T_STOCK, title="CUMP, FIFO and the cascade to the analytical result", lesson="acu2-stock-valuation-cost-price",
    questions=[
        N("A firm buys 2 000 kg of material at FCFA 650 a kg. The supply centre's cost of the unit of work is FCFA 30 per kg bought. Calculate the total purchase cost in FCFA.",
          _e_pc,
          [("Purchase price", "2 000 × 650 = 1 300 000."),
           ("Supply centre", "2 000 × 30 = 60 000."),
           ("Purchase cost", "1 360 000 (680 per kg).")],
          "Purchase cost", "Calculation", "Add the supply centre's share to the purchase price."),
        NM(_e_stock + "The weighted average cost including opening stock (CUMP) is",
           _e_cump,
           [(730, "This averages the two unit prices without weighting by quantity."),
            (760, "This is the price of the purchases only."),
            (700, "This is the price of the opening stock only.")],
           [("Total value", "800 × 700 + 1 200 × 760 = 560 000 + 912 000 = 1 472 000."),
            ("CUMP", "1 472 000 ÷ 2 000 = 736.")],
           "Weighted average cost (CUMP)", "Calculation", "Divide total value by total quantity.", fmt=lambda v: f"FCFA {n(v)} per unit"),
        NM(_e_stock + "Using FIFO, the value of the 1 500 units issued is",
           _e_fifo,
           [(1_104_000, "This values the issues at the CUMP of 736."),
            (1_122_000, "This takes the newest units first (last in, first out)."),
            (1_050_000, "This values all 1 500 units at the opening price.")],
           [("Oldest first", "800 units at 700 = 560 000."),
            ("Then the purchase", "700 units at 760 = 532 000."),
            ("Total", "1 092 000.")],
           "FIFO valuation of issues", "Calculation", "Use up the opening stock before touching the purchase."),
        N("Materials issued (CUMP) FCFA 1 104 000; direct labour 600 hours at FCFA 1 400; machining centre 200 machine hours at FCFA 2 500 per hour. "
          "Calculate the production cost of the batch of 1 000 units in FCFA.",
          _e_prod,
          [("Labour", "600 × 1 400 = 840 000."),
           ("Machining", "200 × 2 500 = 500 000."),
           ("Production cost", "1 104 000 + 840 000 + 500 000 = 2 444 000.")],
          "Production cost", "Calculation", "Materials + direct labour + production centres."),
        N("Finished goods: opening stock 100 units valued at FCFA 218 000; production 1 000 units costing FCFA 2 444 000. Calculate the CUMP of the finished goods in FCFA per unit.",
          _e_fc,
          [("Total", "218 000 + 2 444 000 = 2 662 000 for 1 100 units."),
           ("CUMP", "2 662 000 ÷ 1 100 = 2 420.")],
          "Finished goods valuation", "Calculation", "Include the opening stock in the average.", unit="FCFA per unit"),
        NM("Using a finished goods CUMP of FCFA 2 420, 900 units are sold at FCFA 3 000. Distribution costs are 5% of sales. The cost price of the units sold is",
           _e_cp,
           [(2_334_600, "This values the goods sold at this period's production cost (2 444) instead of the stock's CUMP."),
            (2_178_000, "This forgets the distribution costs."),
            (2_579_000, "This adds distribution to the cost of all 1 000 units produced, not the units sold.")],
           [("Cost of goods sold", "900 × 2 420 = 2 178 000."),
            ("Distribution", "5% × 2 700 000 = 135 000."),
            ("Cost price", "2 313 000.")],
           "Cost price", "Calculation", "Cost price = cost of goods sold + distribution."),
        N("Continuing: sales are FCFA 2 700 000 and the cost price FCFA 2 313 000. Calculate the analytical result in FCFA.",
          387_000,
          [("Formula", "Analytical result = sales − cost price."),
           ("Calculate", "2 700 000 − 2 313 000 = 387 000 profit.")],
          "Analytical result", "Calculation", "Compare sales with the cost price of the same units."),
        NM("Analytical result FCFA 1 800 000; supplementary charges FCFA 120 000; non-incorporable charges FCFA 90 000. The financial accounting result is",
           _e_fr,
           [(1_770_000, "This deducts the supplementary charges and adds the non-incorporable charges: both signs are reversed."),
            (2_010_000, "This adds both items."),
            (1_590_000, "This deducts both items.")],
           [("Supplementary", "They were counted as costs but never recorded in the financial accounts: add 120 000."),
            ("Non-incorporable", "They are in the financial accounts but not in costs: deduct 90 000."),
            ("Result", "1 800 000 + 120 000 − 90 000 = 1 830 000.")],
           "Reconciliation of results", "Reasoning", "Which side recorded each item?"),
    ]))

# ====================================================================== 6. Job, batch and process costing
use(106)
_f_oar = Fr(7_200_000, 9_600)
assert _f_oar == 750
_f_job = 300_000 + 50 * 1_400 + 50 * _f_oar
assert _f_job == 407_500 and 300_000 + 70_000 == 370_000 and 300_000 + 37_500 == 337_500
assert Fr(600_000) / Fr(75, 100) == 800_000
assert 1_200 * 5_000 - 6_300_000 == -300_000
_f_cpk = Fr(5_000 * 400 + 1_034_000 - 200 * 50, 5_000 - 200)
assert _f_cpk == 630 and 5_000 * 4 // 100 == 200
assert (5_000 - 200 - 4_700) * _f_cpk == 63_000
assert Fr(2_580_000, 4_000 + 1_000 * 30 // 100) == 600

SETS.append(practice_set(
    module=M_COST, topic=T_JOB, title="Job cost sheets, process losses and equivalent units", lesson="acu2-job-batch-process-costing",
    questions=[
        Q("A printer in Buea prints 300 wedding invitations designed for one couple. Which costing method fits best?",
          "Job costing",
          [("Process costing", "Process costing averages costs over continuous identical output, not one customer's order."),
           ("Marginal costing only", "Marginal costing is a way of treating fixed costs, not a method of collecting the cost of an order."),
           ("Activity-based costing of the whole factory", "ABC refines overhead charging; the order itself is still collected on a job cost sheet.")],
          [("Nature of the order", "One customer, one specification, separately identifiable."),
           ("Method", "Collect its costs on a job cost sheet: job costing.")],
          "Choosing a costing method", "Application", "Is the order unique or continuous?"),
        N("Budgeted production overheads are FCFA 7 200 000 and budgeted direct labour hours 9 600. Calculate the overhead absorption rate per direct labour hour in FCFA.",
          _f_oar,
          [("Formula", "OAR = budgeted overheads ÷ budgeted activity."),
           ("Calculate", "7 200 000 ÷ 9 600 = 750 per hour.")],
          "Overhead absorption rate", "Calculation", "Use budgeted, not actual, figures.", unit="FCFA per hour"),
        NM("With an OAR of FCFA 750 per direct labour hour, a job uses materials FCFA 300 000 and 50 labour hours at FCFA 1 400. Its production cost is",
           _f_job,
           [(370_000, "This is the prime cost: the overhead has not been absorbed."),
            (445_000, "This counts the absorbed overhead twice."),
            (337_500, "This leaves out the direct labour.")],
           [("Prime cost", "300 000 + 50 × 1 400 = 370 000."),
            ("Overhead", "50 × 750 = 37 500."),
            ("Production cost", "407 500.")],
           "Job cost sheet", "Calculation", "Prime cost plus absorbed overhead."),
        NM("A job's total cost is FCFA 600 000. The firm wants a profit of 25% of the selling price. The selling price is",
           800_000,
           [(750_000, "This adds 25% of cost (a mark-up), not 25% of price."),
            (450_000, "This deducts 25% from cost."),
            (2_400_000, "This divides cost by 0.25 instead of by 0.75.")],
           [("Cost as a share of price", "If profit is 25% of price, cost is 75% of price."),
            ("Price", "600 000 ÷ 0.75 = 800 000 (profit 200 000 = 25% of 800 000).")],
           "Margin and mark-up", "Calculation", "What percentage of the price is the cost?"),
        Q("The OAR is FCFA 1 200 per machine hour. Actual hours were 5 000 and actual overheads FCFA 6 300 000. The overheads are",
          "under-absorbed by 300 000",
          [("over-absorbed by 300 000", "Absorbed 6 000 000 is less than actual 6 300 000, so it is under-absorbed."),
           ("under-absorbed by 6 300 000", "Only the difference between absorbed and actual is under-absorbed."),
           ("exactly absorbed", "Absorbed and actual overheads differ by 300 000.")],
          [("Absorbed", "5 000 × 1 200 = 6 000 000."),
           ("Compare", "Actual 6 300 000 − absorbed 6 000 000 = 300 000 under-absorbed (an extra charge in the income statement).")],
          "Under- and over-absorption", "Calculation", "Compute absorbed overhead with actual hours."),
        N("A process receives 5 000 kg of material at FCFA 400 a kg and conversion costs of FCFA 1 034 000. Normal loss is 4% of input and is sold as scrap at FCFA 50 a kg. "
          "Calculate the cost per kg of expected output in FCFA.",
          _f_cpk,
          [("Normal loss", "4% × 5 000 = 200 kg; scrap value 10 000."),
           ("Net cost", "2 000 000 + 1 034 000 − 10 000 = 3 024 000."),
           ("Cost per kg", "3 024 000 ÷ (5 000 − 200) = 3 024 000 ÷ 4 800 = 630.")],
          "Cost per unit with normal loss", "Calculation", "Deduct the scrap value and the normal loss units.", unit="FCFA per kg"),
        NM("In the same process (cost per kg FCFA 630, normal loss 200 kg), actual output is 4 700 kg. The value of the abnormal loss in the process account is",
           63_000,
           [(189_000, "This values the whole loss of 300 kg, including the normal loss, at 630."),
            (5_000, "This is only the scrap value of the 100 kg."),
            (40_000, "This uses the material price of 400 instead of the full cost per kg.")],
           [("Abnormal loss", "Expected output 4 800 − actual 4 700 = 100 kg."),
            ("Value", "100 × 630 = 63 000.")],
           "Abnormal loss", "Calculation", "Compare actual output with expected output."),
        N("4 000 units are finished and 1 000 units remain in progress, 30% complete for conversion. Conversion costs are FCFA 2 580 000. "
          "Calculate the conversion cost per equivalent unit in FCFA.",
          600,
          [("Equivalent units", "4 000 + 30% × 1 000 = 4 300."),
           ("Cost per unit", "2 580 000 ÷ 4 300 = 600.")],
          "Equivalent units", "Calculation", "Count WIP at its degree of completion.", unit="FCFA"),
    ]))

# ====================================================================== 7. Activity-based costing
use(107)
_g_rates = (Fr(3_600_000, 45), Fr(2_000_000, 100), Fr(4_400_000, 5_500))
assert _g_rates == (80_000, 20_000, 800)
_g_P = 18 * 80_000 + 30 * 20_000 + 4_000 * 800
_g_Q = 27 * 80_000 + 70 * 20_000 + 1_500 * 800
assert (_g_P, _g_Q, _g_P + _g_Q) == (5_240_000, 4_760_000, 10_000_000)
assert Fr(_g_Q, 2_000) == 2_380 and Fr(10_000_000, 5_000) * 1_000 / 2_000 == 1_000
_g_data = ("Overheads FCFA 10 000 000: set-ups FCFA 3 600 000 (set-ups: P 18, Q 27); materials handling FCFA 2 000 000 (movements: P 30, Q 70); "
           "machining FCFA 4 400 000 (machine hours: P 4 000, Q 1 500). Output: P 8 000 units using 4 000 labour hours; Q 2 000 units using 1 000 labour hours. ")

SETS.append(practice_set(
    module=M_COST, topic=T_ABC, title="Cost driver rates and ABC against a single labour-hour rate", lesson="acu2-activity-based-costing",
    questions=[
        Q("In activity-based costing, a cost driver is",
          "the factor that causes the cost of an activity to change",
          [("the manager responsible for a cost centre", "That is a cost centre manager, not a driver."),
           ("the largest overhead of the firm", "Size does not make a cost a driver; a driver explains why a pool's cost changes."),
           ("the direct labour hour rate used for all overheads", "That is the traditional single rate that ABC replaces.")],
          [("Definition", "A driver is the cause of the activity's cost, e.g. the number of set-ups for the set-up pool.")],
          "Cost drivers", "Recall", "Think of what makes the activity's cost go up."),
        Q("Which is the most suitable cost driver for the activity 'receiving and inspecting deliveries of materials'?",
          "Number of deliveries received",
          [("Direct labour hours in the assembly shop", "Assembly hours do not cause receiving and inspection work."),
           ("Floor area of the factory", "Floor area may drive rent, not inspection of deliveries."),
           ("Number of finished units sold", "Sales volume is not what causes receiving work; deliveries are.")],
          [("Cause", "Each delivery has to be received and inspected."),
           ("Driver", "So the number of deliveries drives the cost.")],
          "Choosing a cost driver", "Application", "What event creates the work?"),
        N(_g_data + "Calculate the cost driver rate for set-ups in FCFA per set-up.",
          80_000,
          [("Total set-ups", "18 + 27 = 45."),
           ("Rate", "3 600 000 ÷ 45 = 80 000 per set-up.")],
          "Cost driver rate", "Calculation", "Divide the pool by the total number of set-ups.", unit="FCFA"),
        NM(_g_data + "By ABC, the total overhead charged to product Q is",
           _g_Q,
           [(2_160_000, "This charges only the set-up pool to Q."),
            (2_000_000, "This shares overheads by labour hours (1 000 of 5 000 hours), the traditional method."),
            (5_240_000, "This is the overhead charged to P, not Q.")],
           [("Rates", "Set-ups 80 000; handling 2 000 000 ÷ 100 = 20 000; machining 4 400 000 ÷ 5 500 = 800."),
            ("Charge Q", "27 × 80 000 + 70 × 20 000 + 1 500 × 800 = 2 160 000 + 1 400 000 + 1 200 000 = 4 760 000.")],
           "Charging overheads by ABC", "Calculation", "Find all three rates, then use Q's driver quantities."),
        N(_g_data + "Using ABC, calculate the overhead per unit of Q in FCFA.",
          2_380,
          [("Total for Q", "4 760 000."),
           ("Per unit", "4 760 000 ÷ 2 000 = 2 380.")],
          "ABC cost per unit", "Calculation", "Divide Q's ABC overhead by its units.", unit="FCFA per unit"),
        Q(_g_data + "With a single labour-hour rate, Q's overhead per unit is FCFA 1 000; with ABC it is FCFA 2 380. What does this show?",
          "The labour-hour rate undercosted Q, so P was carrying overheads caused by Q",
          [("The labour-hour rate overcosted Q", "ABC gives Q a higher cost, so the old rate was too low for Q."),
           ("ABC increases total overheads", "Total overheads stay 10 000 000; only the split changes."),
           ("Q should be sold at 2 380", "2 380 is only its overhead per unit; price also depends on direct costs and the market.")],
          [("Compare", "2 380 − 1 000 = 1 380 more per unit of Q under ABC."),
           ("Meaning", "Q causes many set-ups and movements but uses few labour hours; P was subsidising Q.")],
          "Comparing ABC with traditional absorption", "Interpretation", "Which product's cost went up under ABC?"),
        Q("ABC is likely to give the greatest improvement in cost accuracy for a firm that",
          "makes many different products in batches of very different sizes, with high overheads",
          [("makes one product in one continuous process", "With one product all overheads are charged to it anyway."),
           ("has overheads that are a very small part of total cost", "Re-allocating small overheads changes little."),
           ("uses the same activities in the same proportion for every product", "Then a single rate already charges products fairly.")],
          [("ABC adds value when", "Overheads are large and products consume activities unevenly.")],
          "When ABC is useful", "Reasoning", "When does a single rate distort most?"),
        Q("Which is a genuine limitation of ABC?",
          "Some overheads, such as the general manager's salary, have no clear cost driver and are still shared arbitrarily",
          [("It cannot be used by manufacturing firms", "ABC began in manufacturing and is widely used there."),
           ("It ignores overheads altogether", "ABC is a method of charging overheads."),
           ("It always gives the same result as a labour-hour rate", "It gives different results when activities are consumed unevenly; that is its purpose.")],
          [("Facility-level costs", "Costs that support the whole business have no product-related driver."),
           ("Other limits", "Cost of setting up the system and judgement in choosing drivers.")],
          "Limitations of ABC", "Concept", "Think of costs that no product causes directly."),
    ]))

# ====================================================================== 8. Marginal costing and break-even analysis
use(108)
_h_p, _h_vc, _h_fc = 8_000, 5_200, 14_000_000
_h_c = _h_p - _h_vc
_h_cs = Fr(_h_c, _h_p)
assert (_h_c, _h_cs) == (2_800, Fr(35, 100))
_h_beq, _h_bev = Fr(_h_fc, _h_c), _h_fc / _h_cs
assert (_h_beq, _h_bev) == (5_000, 40_000_000)
assert round(_h_fc / Fr(65, 100)) == 21_538_462 and 5_000 * _h_vc == 26_000_000 and _h_fc * _h_cs == 4_900_000
_h_mos = Fr(6_000 - 5_000, 6_000) * 100
assert round(float(_h_mos), 1) == 16.7
assert Fr(_h_fc + 4_200_000, _h_c) == 6_500
_h_data = "A product sells for FCFA 8 000; its variable cost is FCFA 5 200 a unit; fixed costs are FCFA 14 000 000 a year. "
_be_alt = ("Break-even chart: sales revenue, total cost and fixed cost lines plotted against units sold from 0 to 10 000; a point P where the sales and total cost lines cross, "
           "and a bracket M on the units axis between 6 000 and 8 000 units, where 8 000 is budgeted sales.")

SETS.append(practice_set(
    module=M_COST, topic=T_MARG, title="Contribution, break-even, margin of safety and limiting factors", lesson="acu2-marginal-costing-break-even",
    questions=[
        Q(_h_data + "The contribution/sales ratio is",
          "35%",
          [("65%", "This is variable cost ÷ price, the variable cost ratio."),
           ("53.8%", "This divides contribution by variable cost instead of by price."),
           ("2 800", "This is the contribution per unit, not the ratio.")],
          [("Contribution", "8 000 − 5 200 = 2 800."),
           ("C/S ratio", "2 800 ÷ 8 000 = 35%.")],
          "Contribution/sales ratio", "Calculation", "Contribution compared with the selling price."),
        N(_h_data + "Calculate the break-even point in units.",
          _h_beq,
          [("Contribution per unit", "2 800."),
           ("Break-even", "14 000 000 ÷ 2 800 = 5 000 units.")],
          "Break-even point in units", "Calculation", "Fixed costs divided by contribution per unit.", unit="units"),
        NM(_h_data + "The break-even point in sales value is",
           _h_bev,
           [(26_000_000, "This multiplies break-even units by the variable cost instead of the price."),
            (4_900_000, "This multiplies fixed costs by the C/S ratio instead of dividing."),
            (21_538_462, "This divides fixed costs by the variable cost ratio (65%).")],
           [("Formula", "Break-even value = fixed costs ÷ C/S ratio."),
            ("Calculate", "14 000 000 ÷ 0.35 = 40 000 000 (= 5 000 × 8 000).")],
           "Break-even point in value", "Calculation", "Divide fixed costs by the C/S ratio."),
        N(_h_data + "Budgeted sales are 6 000 units. Calculate the margin of safety as a percentage of budgeted sales (one decimal place).",
          _h_mos,
          [("Margin of safety", "6 000 − 5 000 = 1 000 units."),
           ("Percentage", "1 000 ÷ 6 000 × 100 = 16.7%.")],
          "Margin of safety", "Calculation", "Compare the margin with budgeted, not break-even, sales.", tol=0.1, unit="%"),
        N(_h_data + "How many units must be sold to earn a profit of FCFA 4 200 000?",
          6_500,
          [("Required contribution", "14 000 000 + 4 200 000 = 18 200 000."),
           ("Units", "18 200 000 ÷ 2 800 = 6 500.")],
          "Sales for a target profit", "Calculation", "Contribution must cover fixed costs and the profit.", unit="units"),
        Q("In the break-even chart, what does point P show?",
          "The volume at which total revenue equals total cost, so profit is zero",
          [("The volume at which profit is greatest", "Profit keeps rising to the right of P; P is where it is zero."),
           ("The level of fixed costs", "Fixed costs are shown by the horizontal line, not by P."),
           ("The budgeted level of sales", "Budgeted sales are at 8 000 units, at the right end of M.")],
          [("Read the chart", "P is where the sales revenue line crosses the total cost line."),
           ("Meaning", "Revenue = total cost: the break-even point (here 6 000 units, 30 million).")],
          "Reading a break-even chart", "Interpretation", "What is true where the two lines cross?",
          diagram="alacu2-break-even-chart-q.svg", diagram_alt=_be_alt),
        Q("In the same chart, the bracket M between 6 000 and 8 000 units represents",
          "the margin of safety: how far sales can fall from budget before a loss is made",
          [("the profit made at budgeted sales", "Profit is a vertical distance between the revenue and cost lines, measured in FCFA."),
           ("the fixed costs of the period", "Fixed costs are the horizontal line at 12 million."),
           ("the loss made below break-even", "M lies above the break-even volume, where the firm is in profit.")],
          [("Positions", "6 000 = break-even volume; 8 000 = budgeted sales."),
           ("Meaning", "The gap is the margin of safety: 2 000 units, 25% of budget.")],
          "Margin of safety on a chart", "Interpretation", "What are the two ends of the bracket?",
          diagram="alacu2-break-even-chart-q.svg", diagram_alt=_be_alt),
        Q("Material is scarce. A: contribution FCFA 3 000 using 3 kg; B: FCFA 2 400 using 2 kg; C: FCFA 1 500 using 1 kg. Which product should be made first?",
          "C, because it earns the most contribution per kg",
          [("A, because it has the highest contribution per unit", "Under a limiting factor, rank by contribution per kg: A earns only 1 000 per kg."),
           ("B, because it is in the middle", "B earns 1 200 per kg, less than C's 1 500."),
           ("All equally, because each earns the same per unit of product", "Contributions per unit and per kg differ.")],
          [("Per kg", "A 1 000; B 1 200; C 1 500."),
           ("Rank", "C, then B, then A.")],
          "Limiting factor ranking", "Application", "Divide each contribution by the kg used."),
    ]))

# ====================================================================== 9. Budgets and the cash budget
use(109)
assert 3_600 + 700 - 500 == 3_800
_i_rec = 3_600_000 * 25 // 100 + 3_000_000 * 50 // 100 + 2_400_000 * 25 // 100
assert _i_rec == 3_000_000 and 900_000 + 1_500_000 == 2_400_000
assert 3_600_000 * 25 // 100 + 2_400_000 * 50 // 100 + 3_000_000 * 25 // 100 == 2_850_000
assert 1_500_000 * 40 // 100 + 1_200_000 * 60 // 100 == 1_320_000
assert 350_000 + 2_900_000 - 3_400_000 == -150_000
_i_vat = Fr((6_000_000 - 3_600_000) * 1925, 10_000)
assert _i_vat == 462_000

SETS.append(practice_set(
    module=M_BUD, topic=T_BUDG, title="Production budgets, receipts, payments and VAT in the cash budget", lesson="acu2-budgets-cash-budget",
    questions=[
        Q("The principal budget factor is",
          "the factor that limits the firm's activity, so its budget is prepared first",
          [("the largest figure in the master budget", "Size is not the test; the limiting factor is."),
           ("the closing cash balance of the year", "Cash is an outcome of the budgets, not the starting factor."),
           ("the budget prepared last, to check all the others", "It is prepared first, because the other budgets depend on it.")],
          [("Definition", "The factor that limits activity, usually sales demand."),
           ("Consequence", "Its budget comes first; production, purchases and cash follow from it.")],
          "Principal budget factor", "Recall", "Which budget do all the others depend on?"),
        N("Budgeted sales are 3 600 units. Opening stock of finished goods is 500 units and the required closing stock is 700 units. Calculate the production budget in units.",
          3_800,
          [("Formula", "Production = sales + closing stock − opening stock."),
           ("Calculate", "3 600 + 700 − 500 = 3 800.")],
          "Production budget", "Calculation", "Production must cover sales and build up stock.", unit="units"),
        NM("Sales: March FCFA 2 400 000, April FCFA 3 000 000, May FCFA 3 600 000. Customers pay 25% in the month of sale, 50% the next month and 25% two months later. Cash received in May is",
           _i_rec,
           [(3_600_000, "This records all of May's sales as received in May."),
            (2_400_000, "This leaves out the 25% of March sales received two months later."),
            (2_850_000, "This applies 50% to March and 25% to April: the months are swapped.")],
           [("From May", "25% × 3 600 000 = 900 000."),
            ("From April", "50% × 3 000 000 = 1 500 000."),
            ("From March", "25% × 2 400 000 = 600 000; total 3 000 000.")],
           "Receipts from credit sales", "Calculation", "May receives part of three months' sales."),
        Q("Which item would appear in the budgeted income statement but NOT in the cash budget?",
          "Depreciation of equipment",
          [("Payment for a new machine", "A capital payment is a cash outflow and appears in the cash budget."),
           ("Receipt of a bank loan", "A loan received is a cash inflow."),
           ("Payment of last month's VAT", "VAT paid is a cash outflow.")],
          [("Test", "Does money actually enter or leave the bank?"),
           ("Answer", "Depreciation is a non-cash expense: income statement only.")],
          "Non-cash items", "Concept", "Ask whether cash moves."),
        N("Purchases: June FCFA 1 200 000, July FCFA 1 500 000. Suppliers are paid 40% in the month of purchase and 60% the following month. Calculate the payment to suppliers in July in FCFA.",
          1_320_000,
          [("July's share", "40% × 1 500 000 = 600 000."),
           ("June's share", "60% × 1 200 000 = 720 000."),
           ("Total", "1 320 000.")],
          "Payments to suppliers", "Calculation", "July pays part of July's and part of June's purchases."),
        NM("Opening cash FCFA 350 000; receipts FCFA 2 900 000; payments FCFA 3 400 000. The closing balance is",
           -150_000,
           [(150_000, "The sign is wrong: payments exceed opening cash plus receipts."),
            (-500_000, "This forgets the opening balance."),
            (850_000, "This adds the opening balance to the net outflow instead of combining them.")],
           [("Calculate", "350 000 + 2 900 000 − 3 400 000 = −150 000."),
            ("Meaning", "An overdraft of 150 000 is needed unless action is taken.")],
           "Closing cash balance", "Calculation", "Opening + receipts − payments.", fmt=lambda v: ("−" if v < 0 else "") + f"FCFA {n(abs(v))}"),
        N("A month's sales excluding VAT are FCFA 6 000 000 and purchases excluding VAT FCFA 3 600 000. Using a teaching VAT rate of 19.25%, calculate the VAT payable for the month in FCFA.",
          _i_vat,
          [("VAT collected", "19.25% × 6 000 000 = 1 155 000."),
           ("VAT deductible", "19.25% × 3 600 000 = 693 000."),
           ("VAT payable", "1 155 000 − 693 000 = 462 000.")],
          "VAT payable", "Calculation", "VAT collected minus VAT deductible."),
        Q("A cash budget shows a deficit only in the two months after a large equipment purchase. Which response is most sensible?",
          "Arrange an overdraft or instalment payments in advance to cover the temporary gap",
          [("Cancel all production for the year", "The deficit is temporary; stopping production would destroy the receipts that end it."),
           ("Ignore it, because the annual profit is positive", "Profit does not pay bills on time; a cash shortage can stop the business."),
           ("Increase depreciation to raise cash", "Depreciation is not cash; changing it does not affect the bank balance.")],
          [("Diagnose", "A timing problem caused by one payment."),
           ("Act", "Short-term finance or spreading the payment solves a temporary deficit.")],
          "Using the cash budget", "Application", "Is the problem permanent or temporary?"),
    ]))

# ====================================================================== 10. Flexible budgets
use(110)
assert 350 * 7_200 == 2_520_000
assert 400_000 + 60 * 7_200 == 832_000 and 400_000 + 60 * 8_000 == 880_000 and 880_000 * 9 // 10 == 792_000 and 60 * 7_200 == 432_000
assert 1_980_000 - 1_900_000 == 80_000
assert (8_000 - 7_200) * 450 == 360_000
assert 7_200 * (1_200 - 750) - 2_000_000 == 1_240_000

SETS.append(practice_set(
    module=M_BUD, topic=T_FLEX, title="Flexing costs, labelling variances and the sales volume effect", lesson="acu2-flexible-budgets",
    questions=[
        Q("Budgeted output was 8 000 units but actual output was 7 200. Why should actual costs be compared with a flexible budget rather than the fixed budget?",
          "Because variable costs should be lower at lower output, so only a budget for 7 200 units shows true efficiency",
          [("Because fixed costs always rise when output falls", "Fixed costs stay the same within the relevant range."),
           ("Because the fixed budget is always wrong and should be ignored", "The fixed budget is still used to measure the sales volume effect."),
           ("Because a flexible budget always shows favourable variances", "A flexible budget can show adverse variances; it shows fair ones.")],
          [("Problem", "At 7 200 units, costs naturally fall; comparing with 8 000-unit costs flatters managers."),
           ("Solution", "Flex the budget to 7 200 units and compare like with like.")],
          "Purpose of flexible budgets", "Concept", "What would costs be at the actual output?"),
        N("Material cost is budgeted at FCFA 350 a unit. Actual output is 7 200 units. Calculate the flexed material cost in FCFA.",
          2_520_000,
          [("Flex", "7 200 × 350 = 2 520 000.")],
          "Flexing a variable cost", "Calculation", "A variable cost changes in proportion to output."),
        NM("Power cost is FCFA 400 000 fixed plus FCFA 60 a unit. Budget 8 000 units; actual 7 200 units. The flexed power cost is",
           832_000,
           [(880_000, "This is the cost at the budgeted 8 000 units."),
            (792_000, "This scales the whole budget (880 000 × 0.9), wrongly flexing the fixed part."),
            (432_000, "This forgets the fixed part.")],
           [("Fixed part", "400 000 stays."),
            ("Variable part", "60 × 7 200 = 432 000."),
            ("Flexed cost", "832 000.")],
           "Flexing a semi-variable cost", "Calculation", "Separate the fixed and variable parts."),
        Q("Flexed labour cost FCFA 1 980 000; actual labour cost FCFA 1 900 000. The variance is",
          "80 000 favourable",
          [("80 000 adverse", "Actual cost is below the flexed cost, which raises profit: favourable."),
           ("1 900 000 favourable", "The variance is the difference, not the actual cost."),
           ("Zero, because labour is a fixed cost", "Direct labour is treated here as variable and the figures differ.")],
          [("Difference", "1 980 000 − 1 900 000 = 80 000."),
           ("Label", "Lower cost than allowed: favourable.")],
          "Favourable and adverse variances", "Calculation", "Does the difference raise or lower profit?"),
        N("Budget: 8 000 units; actual: 7 200 units. Contribution per unit is FCFA 450. Calculate the size of the sales volume variance in FCFA (it is adverse).",
          360_000,
          [("Units short", "8 000 − 7 200 = 800."),
           ("Variance", "800 × 450 = 360 000 adverse.")],
          "Sales volume variance", "Calculation", "Lost units times contribution per unit."),
        N("Price FCFA 1 200; variable cost FCFA 750 a unit; fixed costs FCFA 2 000 000. Calculate the flexed budget profit for an actual volume of 7 200 units, in FCFA.",
          1_240_000,
          [("Contribution", "7 200 × (1 200 − 750) = 3 240 000."),
           ("Profit", "3 240 000 − 2 000 000 = 1 240 000.")],
          "Flexed budget profit", "Calculation", "Flex revenue and variable costs; keep fixed costs."),
        Q("Actual sales revenue was FCFA 50 000 below the flexed sales revenue for the same number of units. This variance is",
          "adverse, because lower selling prices reduced profit",
          [("favourable, because the figure is below budget", "For revenue, below budget reduces profit, so it is adverse."),
           ("a sales volume variance", "The volume is the same; the difference comes from price."),
           ("a cost variance, to be explained by production", "It concerns revenue and is the sales manager's responsibility.")],
          [("Effect on profit", "Less revenue means less profit: adverse."),
           ("Cause", "Same units, so the average price was lower (discounts, price cuts).")],
          "Sales price variance", "Reasoning", "Ask what it does to profit."),
        Q("Budgetary slack is",
          "deliberately setting easy targets, for example overstating costs, so that the budget is easy to meet",
          [("the gap between budgeted and actual sales volume", "That is the sales volume difference."),
           ("the unused balance of the cash budget", "Slack is a behavioural problem, not a cash balance."),
           ("the margin of safety in break-even analysis", "The margin of safety is a CVP measure.")],
          [("Behaviour", "Managers judged against a budget may pad it to look good."),
           ("Remedy", "Participation with challenge, and realistic targets.")],
          "Behavioural aspects of budgets", "Recall", "Think about managers protecting themselves."),
    ]))

# ====================================================================== 11. Standard costing and variances
use(111)
assert (400 - 380) * 3_200 == 64_000 and (3_000 - 3_200) * 400 == -80_000
assert (2_000 * 3 - 5_900) * 1_000 == 100_000 and (1_000 - 1_040) * 5_900 == -236_000
assert (1_000 - 960) * 5_900 == 236_000

SETS.append(practice_set(
    module=M_BUD, topic=T_STD, title="Price, usage, rate and efficiency variances", lesson="acu2-standard-costing-variances",
    questions=[
        Q("A standard cost is",
          "a carefully predetermined cost per unit under efficient operating conditions",
          [("the actual cost of the last batch produced", "That is an actual cost; a standard is set in advance."),
           ("the budgeted total cost of all production", "A standard is per unit; the budget covers total planned activity."),
           ("the selling price less the profit margin", "That is a target cost, not a standard built from quantities and prices.")],
          [("Definition", "Standard quantity multiplied by standard price, per unit, set in advance.")],
          "Standard cost", "Recall", "Is it set before or after production?"),
        Q("In variance analysis, actual results are compared with",
          "the standard cost of the actual output",
          [("the standard cost of the budgeted output", "That ignores that output differed from budget."),
           ("last year's actual cost", "Standards, not history, are the yardstick."),
           ("the selling price of the actual output", "Selling price is revenue, not a cost yardstick.")],
          [("Like with like", "Standard quantities are calculated for the output actually produced.")],
          "Table of comparison", "Concept", "Which output was actually made?"),
        N("Standard: 3 kg of material at FCFA 400 a kg per unit. Actual output 1 000 units used 3 200 kg bought at FCFA 380 a kg. Calculate the material price variance in FCFA (favourable is positive).",
          64_000,
          [("Formula", "(SP − AP) × AQ."),
           ("Calculate", "(400 − 380) × 3 200 = 64 000 favourable.")],
          "Material price variance", "Calculation", "Use the actual quantity bought."),
        NM("Using the same data, the material usage variance is",
           -80_000,
           [(80_000, "The sign is wrong: using more than the standard is adverse."),
            (-76_000, "This values the excess 200 kg at the actual price of 380."),
            (64_000, "This is the price variance, not the usage variance.")],
           [("Standard quantity", "1 000 × 3 = 3 000 kg."),
            ("Usage", "(3 000 − 3 200) × 400 = −80 000: 80 000 adverse.")],
           "Material usage variance", "Calculation", "Compare quantities, valued at the standard price.",
           fmt=lambda v: f"FCFA {n(abs(v))} {'favourable' if v > 0 else 'adverse'}"),
        N("Standard: 2 labour hours at FCFA 1 000 per unit. Actual output 1 500 units took 3 100 hours paid at FCFA 950 an hour. Calculate the labour rate variance in FCFA (favourable is positive).",
          155_000,
          [("Formula", "(SR − AR) × actual hours."),
           ("Calculate", "(1 000 − 950) × 3 100 = 155 000 favourable.")],
          "Labour rate variance", "Calculation", "Use the hours actually worked."),
        NM("Using the same data, the labour efficiency variance is",
           -100_000,
           [(100_000, "The sign is wrong: more hours than standard is adverse."),
            (-95_000, "This values the 100 extra hours at the actual rate of 950."),
            (155_000, "This is the rate variance.")],
           [("Standard hours", "1 500 × 2 = 3 000."),
            ("Efficiency", "(3 000 − 3 100) × 1 000 = −100 000: adverse.")],
           "Labour efficiency variance", "Calculation", "Compare hours, valued at the standard rate.",
           fmt=lambda v: f"FCFA {n(abs(v))} {'favourable' if v > 0 else 'adverse'}"),
        Q("A purchasing manager buys cheaper, lower-quality board. Which pair of variances is the most likely result?",
          "Favourable material price variance and adverse material usage variance",
          [("Adverse material price variance and favourable usage variance", "Cheaper material gives a lower price, not a higher one."),
           ("Favourable price and favourable usage variances", "Poor material tends to waste more, so usage is likely adverse."),
           ("No price variance and an adverse labour rate variance", "The price of material changed, so a price variance arises.")],
          [("Link", "A cheaper input lowers the price paid but may raise wastage."),
           ("Lesson", "Variances are interrelated; judge them together.")],
          "Interrelated variances", "Reasoning", "What usually goes with poor-quality material?"),
        Q("The fixed overhead volume variance arises because",
          "actual output differed from the budgeted output on which the fixed overhead rate was based",
          [("fixed overhead spending was higher than budget", "That is the expenditure variance."),
           ("workers were paid above the standard rate", "That is a labour rate variance."),
           ("material prices rose", "That is a material price variance.")],
          [("Rate", "Fixed overhead per unit was set using budgeted output."),
           ("Volume", "Producing more or fewer units than budget over- or under-absorbs the fixed overhead.")],
          "Fixed overhead volume variance", "Concept", "What was the rate based on?"),
    ]))

# ====================================================================== 12. Investment appraisal
use(112)
_q_cf = [1_500_000, 2_000_000, 2_500_000, 1_000_000]
_q_inv = 5_000_000
assert 1_500_000 + 2_000_000 == 3_500_000 and Fr(1_500_000, 2_500_000) == Fr(3, 5)
_q_pb = 2 + Fr(3, 5)
_q_pv = [Fr(c) * f for c, f in zip(_q_cf, [Fr(909, 1000), Fr(826, 1000), Fr(751, 1000), Fr(683, 1000)])]
assert [float(x) for x in _q_pv] == [1_363_500, 1_652_000, 1_877_500, 683_000]
_q_npv = sum(_q_pv) - _q_inv
assert _q_npv == 576_000 and sum(_q_cf) - _q_inv == 2_000_000
assert Fr(sum(_q_cf) - _q_inv, 4) == 500_000 and Fr(500_000, _q_inv) == Fr(1, 10)
assert Fr(3_000_000, 4) / Fr(12_000_000, 2) == Fr(1, 8)
assert 6 + Fr(300_000, 300_000 + 100_000) * 4 == 9
_q_data = "An investment costs FCFA 5 000 000 and earns net cash inflows of FCFA 1 500 000, 2 000 000, 2 500 000 and 1 000 000 in years 1 to 4. "

SETS.append(practice_set(
    module=M_BUD, topic=T_INV, title="Payback, ARR, NPV and IRR decisions", lesson="acu2-investment-appraisal",
    questions=[
        Q("Which item should be excluded from the cash flows used in NPV?",
          "Depreciation of the machine",
          [("Extra raw materials bought because of the project", "A cash outflow caused by the project: include it."),
           ("Sales revenue the project brings in", "A cash inflow caused by the project: include it."),
           ("Extra labour paid because of the project", "A cash outflow caused by the project: include it.")],
          [("Relevant cash flows", "Future cash receipts and payments that change because of the project."),
           ("Depreciation", "A book entry with no cash movement: exclude.")],
          "Relevant cash flows", "Concept", "Which item involves no cash movement?"),
        NM(_q_data + "The payback period is",
           _q_pb,
           [(3.0, "This takes the year in which payback is completed; payback needs the fraction too."),
            (2.0, "After two years only 3 500 000 has been recovered."),
            (4.0, "This is the whole life of the project, not the time to recover the outlay.")],
           [("After 2 years", "1 500 000 + 2 000 000 = 3 500 000; 1 500 000 still needed."),
            ("Year 3", "1 500 000 ÷ 2 500 000 = 0.6 of a year, so 2.6 years.")],
           "Payback period", "Calculation", "Find when the cumulative inflows reach 5 000 000.", fmt=lambda v: f"{float(v):.1f} years"),
        N(_q_data + "Calculate the accounting rate of return on the initial investment (no residual value; depreciation is straight-line).",
          10,
          [("Total profit", "Inflows 7 000 000 − depreciation 5 000 000 = 2 000 000 over 4 years."),
           ("Average profit", "2 000 000 ÷ 4 = 500 000."),
           ("ARR", "500 000 ÷ 5 000 000 = 10%.")],
          "Accounting rate of return", "Calculation", "Average annual profit, not average cash flow.", unit="%"),
        NM(_q_data + "Using discount factors at 10% of 0.909, 0.826, 0.751 and 0.683, the net present value is",
           _q_npv,
           [(2_000_000, "This does not discount: inflows 7 000 000 − 5 000 000."),
            (5_576_000, "This forgets to subtract the outlay."),
            (10_576_000, "This adds the outlay instead of subtracting it.")],
           [("PVs", "1 363 500 + 1 652 000 + 1 877 500 + 683 000 = 5 576 000."),
            ("NPV", "5 576 000 − 5 000 000 = 576 000.")],
           "Net present value", "Calculation", "Discount each inflow, add, then subtract the outlay."),
        Q("A project has a positive NPV at the firm's cost of capital. The decision rule says",
          "accept the project on financial grounds",
          [("reject it, because NPV must be zero", "Zero NPV is the IRR condition; a positive NPV adds value."),
           ("accept only if payback is under one year", "Payback is a separate method with its own rule."),
           ("compare ARR with payback before deciding", "NPV already gives a decision rule.")],
          [("Meaning", "A positive NPV means the project earns more than the cost of capital.")],
          "NPV decision rule", "Concept", "What does a positive NPV mean for value?"),
        N("A project has NPV +FCFA 300 000 at 6% and −FCFA 100 000 at 10%. Calculate the IRR by interpolation (%).",
          9,
          [("Formula", "IRR = L + NPV_L ÷ (NPV_L − NPV_H) × (H − L)."),
           ("Calculate", "6 + 300 000 ÷ 400 000 × 4 = 6 + 3 = 9%.")],
          "Internal rate of return", "Calculation", "Interpolate between the two rates.", unit="%"),
        Q("A firm with a cost of capital of 12% finds that a project's IRR is 9%. The firm should",
          "reject it on financial grounds, because it earns less than the cost of capital",
          [("accept it, because 9% is a positive return", "A positive return below the cost of capital destroys value."),
           ("accept it if payback is under five years", "Payback ignores the time value of money; the IRR rule still says reject."),
           ("ignore IRR and use accounting profit only", "Accounting profit does not discount cash flows.")],
          [("Rule", "Accept if IRR is above the cost of capital."),
           ("Here", "9% < 12%, so the NPV at 12% would be negative.")],
          "IRR decision rule", "Application", "Compare IRR with the cost of capital."),
        Q("Which is a weakness of the payback method?",
          "It ignores cash flows after the payback date and the time value of money",
          [("It requires a discount rate that is hard to find", "Payback does not discount; that is NPV's requirement."),
           ("It always rejects profitable projects", "It can reject or accept either way; the issue is what it ignores."),
           ("It uses accounting profit instead of cash flows", "That is a weakness of ARR; payback uses cash flows.")],
          [("Limitations", "No discounting and nothing counted after the cut-off year.")],
          "Evaluating payback", "Concept", "What does payback not look at?"),
    ]))

# ====================================================================== 13-15. Examination sets (one per exam lesson)
use(113)
assert Fr(90, 50) == Fr(9, 5)
assert Fr(30_000_000 - 18_000_000 - 12_000_000, 1) == 0
assert Fr(240_000, 800) == 300 and 700_000 - 1_000 * 300 == 400_000 and 400_000 + 1_500 * 300 == 850_000
assert 3_800 * 1_000 - 3_950_000 == -150_000
assert Fr(3_600_000, 9_000) == 400 and 210_000 + 40 * 700 + 40 * 400 == 254_000

SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Multiple-choice technique and built-in checks", lesson="acu2-exam-paper-1-multiple-choice",
    questions=[
        Q("According to the Board's 2023 report, Paper 1 of Accounting 0705 consists of",
          "50 multiple-choice questions, all compulsory",
          [("30 multiple-choice questions with a choice of 20", "The report gives 50 compulsory questions."),
           ("5 essay questions of which three are answered", "That describes a written paper, not Paper 1."),
           ("a case study with calculations", "Paper 1 is multiple choice.")],
          [("Recall", "The report: 50 multiple-choice questions, all compulsory, one mark each.")],
          "Facts of Paper 1", "Recall", "Recall the structure from the lesson."),
        N("A candidate plans 90 minutes for 50 questions. How many minutes can she spend on each question on average?",
          1.8,
          [("Divide", "90 ÷ 50 = 1.8 minutes.")],
          "Time planning", "Calculation", "Divide the time by the number of questions.", tol=0.05, unit="minutes"),
        Q("Stable resources FCFA 30 000 000; stable uses FCFA 18 000 000; BFR FCFA 12 000 000. The net cash is",
          "zero",
          [("+18 000 000", "This adds BFR to FRNG instead of subtracting."),
           ("+12 000 000", "This is FRNG alone."),
           ("−12 000 000", "This takes BFR alone as a deficit.")],
          [("FRNG", "30 000 000 − 18 000 000 = 12 000 000."),
           ("Net cash", "FRNG − BFR = 0.")],
          "Quick check: net cash", "Calculation", "Find FRNG first.", pos=1),
        NM("Fixed costs FCFA 9 000 000; contribution FCFA 1 800 a unit. The break-even point in units is",
           5_000,
           [(2_000, "This divides by the selling price of 4 500."),
            (9_000_000, "This copies the fixed costs."),
            (16_200_000, "This multiplies instead of dividing.")],
           [("Formula", "Fixed costs ÷ contribution per unit."),
            ("Calculate", "9 000 000 ÷ 1 800 = 5 000.")],
           "Break-even units", "Calculation", "Divide fixed costs by contribution per unit.", fmt=lambda v: f"{n(v)} units"),
        Q("An answer to a margin of safety question is larger than budgeted sales. What should the candidate do?",
          "Recheck the calculation: the margin of safety cannot exceed budgeted sales",
          [("Choose it, because a larger margin is better", "A result that cannot occur signals a method error."),
           ("Add fixed costs and recalculate", "Adding fixed costs does not address the error."),
           ("Leave the question blank", "A blank scores nothing; recheck and answer.")],
          [("Size test", "Margin of safety = budgeted − break-even sales, so it is at most budgeted sales.")],
          "Estimation and reasonableness", "Reasoning", "Does the number make sense?"),
        Q("Which approach is best for a difficult calculation in Paper 1?",
          "Mark it, answer the easier questions first, and return if time remains",
          [("Spend as long as needed, since every mark counts", "Every question carries the same mark; time is better used elsewhere."),
           ("Guess immediately and never return", "A guess is better than a blank, but marked questions can be revisited."),
           ("Skip all calculations", "Calculation questions are worth the same as others and checks help.")],
          [("Two-pass method", "Bank quick marks first, return to marked questions in pass 2.")],
          "Two-pass method", "Application", "Which approach protects total marks?", pos=3),
        Q("Which pair of facts should a candidate keep in mind about the content of Paper 1?",
          "It may draw on any module, including financial, cost and management, and company accounting and taxation",
          [("It covers only the Upper Sixth cost modules", "The 2023 split included financial and company accounting questions."),
           ("It covers only company accounting", "Company accounting was 15 of 50 in 2023, not all."),
           ("It tests only definitions", "It includes calculations.")],
          [("2023 split", "25 financial, 10 cost and management, 15 company accounting and taxation.")],
          "Content of Paper 1", "Recall", "Recall the split in the report."),
        Q("Which is NOT a valid built-in check?",
          "Checking that the answer has three digits",
          [("Checking that FRNG − BFR equals net cash", "A valid identity."),
           ("Checking that the main centres' totals equal the overhead total", "Valid: distribution moves, not creates, cost."),
           ("Checking that flexed profit minus variances equals actual profit", "Valid reconciliation.")],
          [("Real checks", "Accounting identities that must hold."),
           ("Digits", "The number of digits proves nothing.")],
          "Built-in checks", "Concept", "Which test has no accounting meaning?", pos=2),
    ]))

SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Structure, working layout and quick Paper 2 calculations", lesson="acu2-exam-paper-2-cost-management",
    questions=[
        Q("According to the Board's 2023 report, Paper 2 requires candidates to answer",
          "two questions from Section A (Cost Accounting) and all three from Section B (Management Accounting)",
          [("all six questions", "Candidates answer five questions."),
           ("three from Section A and two from Section B", "The numbers are reversed."),
           ("any five of the six", "Section B is compulsory.")],
          [("Structure", "Two sections of three questions; two from A, all of B.")],
          "Structure of Paper 2", "Recall", "Recall the structure from the lesson."),
        Q("Each of the five answers in Paper 2 carries equal marks. A sensible time plan for a three-hour paper is",
          "about 36 minutes for each answer, with time to read the paper first",
          [("90 minutes on the first question and the rest in the remaining time", "Equal marks call for roughly equal time."),
           ("10 minutes for each answer", "That leaves 130 minutes unused."),
           ("all time on Section A", "Section B is compulsory and worth equal marks.")],
          [("Arithmetic", "180 ÷ 5 = 36 minutes.")],
          "Time planning", "Application", "Divide the time evenly.", pos=3),
        N("Lowest activity: 1 000 hours, cost FCFA 700 000. Highest: 1 800 hours, cost FCFA 940 000. Calculate the variable cost per hour in FCFA.",
          300,
          [("Formula", "(940 000 − 700 000) ÷ (1 800 − 1 000) = 300.")],
          "High-low method", "Calculation", "Use the extremes of activity.", unit="FCFA"),
        N("Using the same data, estimate the total cost of 1 500 hours in FCFA.",
          850_000,
          [("Fixed cost", "700 000 − 1 000 × 300 = 400 000."),
           ("Estimate", "400 000 + 1 500 × 300 = 850 000.")],
          "High-low estimate", "Calculation", "Find the fixed cost first."),
        NM("Budgeted overheads FCFA 3 600 000; budgeted direct labour hours 9 000. A job uses materials FCFA 210 000 and 40 labour hours at FCFA 700. Its production cost is",
           254_000,
           [(238_000, "This is the prime cost without overhead."),
            (16_000, "This is the overhead only."),
            (3_850_000, "This adds the whole overhead budget to the job.")],
           [("OAR", "400 per hour."),
            ("Cost", "210 000 + 28 000 + 16 000 = 254 000.")],
           "Job cost sheet", "Calculation", "Prime cost plus absorbed overhead."),
        Q("Which presentation gives the most method marks in a variance question?",
          "Formula, substitution, calculated answer and a label F or A",
          [("A single final figure", "No working, no method marks."),
           ("A paragraph without figures", "The calculation must be shown."),
           ("A list of figures without labels", "Unlabelled figures hide the method.")],
          [("Method marks", "Visible steps and clear labels.")],
          "Presentation of working", "Application", "What does the examiner need to see?", pos=1),
        Q("Which item must NOT appear in a cash budget?",
          "Depreciation of machinery",
          [("Wages paid", "A cash outflow."),
           ("Cash received from credit sales", "A cash inflow, in the month received."),
           ("Payment for a new machine", "A cash outflow when paid.")],
          [("Cash only", "Depreciation is a non-cash expense.")],
          "Cash budget content", "Concept", "Which item involves no cash?", pos=2),
        Q("The 2023 report described the cash budget question as one of the least and poorest answered. The best use of this advice is",
          "to practise full monthly cash budgets with credit sales and delayed payments",
          [("to skip cash budgets in revision", "Section B is compulsory; avoid gaps."),
           ("to learn only the benefits of budgets", "The report refers to both the benefits and the calculation."),
           ("to memorise last year's figures", "The questions change; learn the method.")],
          [("Action", "Practise the layout: opening balance, receipts, payments, closing balance.")],
          "Learning from the report", "Reasoning", "What skill is weak?", pos=0),
    ]))

SETS.append(practice_set(
    module=M_EXAM, topic="Paper 3", title="Structure and the weak areas: shares, tax and capital", lesson="acu2-exam-paper-3-financial-accounting",
    questions=[
        Q("According to the Board's 2023 report, Paper 3 requires candidates to answer",
          "three of four questions in Section A and two of three in Section B",
          [("all seven questions", "Candidates answer five."),
           ("two of four in Section A and three of three in Section B", "The numbers are swapped."),
           ("any five of the seven", "The section rules apply.")],
          [("Structure", "Section A financial accounting: 4 questions, answer 3. Section B company accounting and taxation: 3 questions, answer 2.")],
          "Structure of Paper 3", "Recall", "Recall the structure from the lesson.", pos=0),
        Q("Which areas did the 2023 report describe as the weakness of Paper 3?",
          "Share valuation, taxation and modification of capital",
          [("Invoices and journals", "These were among the stronger areas."),
           ("Ratio analysis only", "The ratio question was well answered."),
           ("Presentation of financial statements", "Reported as a better-answered question.")],
          [("Report", "Taxation and modification of capital were poorly attempted; share valuation was mixed up.")],
          "Learning from the report", "Recall", "Recall the report's comments.", pos=2),
        NM("Adjusted net assets FCFA 49 500 000; 5 000 shares. The mathematical value of a share is",
           9_900,
           [(10_000, "This is the nominal value, not the restated net asset value."),
            (9_500, "This is not supported by the figures."),
            (247_500_000, "This multiplies instead of dividing.")],
           [("Formula", "Net assets ÷ number of shares."),
            ("Calculate", "49 500 000 ÷ 5 000 = 9 900.")],
           "Share valuation", "Calculation", "Divide net assets by the number of shares.", fmt=lambda v: f"FCFA {n(v)}"),
        Q("A question gives dividends for three years and asks for the average dividend. The correct approach is to",
          "average the three years' dividends before calculating the return",
          [("use only the latest year", "The question asks for an average."),
           ("add the three years and use the total as the dividend", "The total overstates the yearly dividend."),
           ("ignore the dividends and use net assets only", "The return needs the dividend.")],
          [("Report warning", "Candidates mixed up an average and a single year.")],
          "Average dividend", "Application", "What does the question ask for?", pos=1),
        N("Accounting profit FCFA 8 000 000; non-deductible expenses FCFA 600 000; non-taxable income FCFA 200 000. Calculate the fiscal (taxable) result in FCFA.",
          8_400_000,
          [("Add back", "8 000 000 + 600 000 = 8 600 000."),
           ("Deduct", "8 600 000 − 200 000 = 8 400 000.")],
          "Fiscal result", "Calculation", "Add back what is not deductible; deduct what is not taxable."),
        NM("4 000 old shares are worth FCFA 15 000 each; 1 000 new shares are issued at FCFA 12 000. The subscription right per old share is",
           600,
           [(3_000, "This is the gap between old value and issue price."),
            (14_400, "This is the value after the issue."),
            (750, "This divides the gap by 4 instead of 5.")],
           [("Value after", "(60 000 000 + 12 000 000) ÷ 5 000 = 14 400."),
            ("Right", "15 000 − 14 400 = 600.")],
           "Subscription right", "Calculation", "Find the value after the issue first.", fmt=lambda v: f"FCFA {n(v)}"),
        Q("Which journal entry records cash received for newly issued shares at nominal value?",
          "Debit bank, credit share capital",
          [("Debit share capital, credit bank", "This reverses the entry."),
           ("Debit reserves, credit bank", "Reserves are not involved."),
           ("Debit bank, credit reserves", "Cash from share issue is capital, not reserves.")],
          [("Entry", "Cash comes in: debit bank; capital rises: credit share capital.")],
          "Journal for a capital increase", "Concept", "Which account increases?", pos=3),
        Q("Which action best prepares a candidate for the report's weak areas?",
          "Practise taxation, share valuation and capital modification with full layouts",
          [("Revise only ratios and invoices", "Those were the strengths; the weak areas need work."),
           ("Skip Section B", "Two Section B questions must be answered."),
           ("Learn definitions only", "Calculations and layouts earn the marks.")],
          [("Targeting", "Work on the weak areas shown by the report.")],
          "Learning from the report", "Reasoning", "Where were marks lost?", pos=0),
    ]))

# ====================================================================== Paper 1 mock exam A (50 questions)
use(201)


def M(prompt, correct, wrongs, solution, concept, skill, hint):
    return Q(prompt, correct, wrongs, [("Solution", solution)], concept, skill, hint)


# ---- computed values (checked) ----
_a_int = Fr(5, 100) * 4_000_000
_a_resid = 600_000 - (Fr(5, 100) * 4_000_000 + Fr(5, 100) * 2_000_000) - 120_000
_a_A = _a_int + Fr(3, 5) * _a_resid
assert (_a_resid, _a_A) == (180_000, 308_000) and Fr(3, 5) * 600_000 == 360_000
assert 50_000 + 308_000 - 200_000 - 10_000 == 148_000
assert Fr(3, 5) * 500_000 == 300_000 and Fr(2, 3) * 0 == 0
assert 2 * 1_500_000 == 3_000_000
_a_gw = 5 * 1_000_000 - (3_000_000 + 1_000_000)
assert _a_gw == 1_000_000
assert Fr(3, 5) * Fr(4, 5) == Fr(12, 25) and Fr(2, 5) * Fr(4, 5) == Fr(8, 25)
assert Fr(2, 5) * 3_000_000 == 1_200_000
assert Fr(3, 5) - Fr(5, 10) == Fr(1, 10) == Fr(2, 5) - Fr(3, 10)
assert Fr(3, 5) * 800_000 == 480_000
assert Fr(1, 4) * 400 * 10_000 == 1_000_000 and 3_000 * (12_500 - 10_000) == 7_500_000
assert Fr(1, 4) * 3_000 * 10_000 + 7_500_000 == 15_000_000
assert Fr(10, 100) * 12_000_000 == 1_200_000
assert 3_000 - Fr(165, 1000) * 3_000 == 2_505 and Fr(165, 1000) * 3_000 == Fr(495)
assert Fr(8, 100) * 5_000_000 == 400_000 and 1_000 * 9_500 == 9_500_000
assert Fr(60_000_000, 4_000) == 15_000
_a_v1 = Fr(5_000 * 18_000 + 1_000 * 12_000, 6_000)
assert _a_v1 == 17_000 and 18_000 - _a_v1 == 1_000
assert Fr(60_000_000, 5_000) == 12_000 and 15_000 - 12_000 == 3_000
assert Fr(12_000_000, 3_000) == 4_000
assert Fr(30, 100) * (10_000_000 + 1_500_000 - 500_000) == 3_300_000
assert Fr(45_000_000, 5_000) == 9_000 and Fr(9_000, 15_000) == Fr(3, 5) and 5_000 * Fr(3, 5) == 3_000
assert Fr(18_000_000 - 14_000_000 - 1_000_000, 3_000) == 1_000
assert 52_000_000 - 45_000_000 == 7_000_000 and 7_000_000 - 9_000_000 == -2_000_000
assert Fr(13_500_000, 9_000_000) == Fr(3, 2) and Fr(150_000_000 - 105_000_000, 150_000_000) == Fr(3, 10)
assert Fr(25_000_000 * 360, 150_000_000) == 60
_a_vc = Fr(1_700_000 - 1_100_000, 5_000 - 2_000)
assert _a_vc == 200 and 1_100_000 - 2_000 * 200 == 700_000
_a_A2 = Fr(880_000 + Fr(1, 5) * 500_000) / (1 - Fr(1, 5) * Fr(1, 10))
assert _a_A2 == 1_000_000 and 500_000 + Fr(1, 10) * _a_A2 == 600_000
assert Fr(400_000 + 1_290_000, 2_000) == 845 and 500 * 800 + 700 * 860 == 1_002_000
assert Fr(5_400_000, 6_000) == 900 and Fr(1_980_000, 3_000 + Fr(50, 100) * 600) == 600
assert Fr(2_400_000, 30) == 80_000 and 12 * 80_000 == 960_000
assert Fr(6_000 - 3_900, 6_000) == Fr(35, 100) and Fr(8_400_000, 2_100) == 4_000
assert Fr(6_000 - 4_000, 6_000) * 100 > 33.3 and Fr(2_000, 6_000) * 100 < 33.4
assert 3_600 + 700 - 500 == 3_800 and 0.4 * 4_000_000 + 0.6 * 3_000_000 == 3_400_000
assert 300_000 + 25 * 9_000 == 525_000
assert (500 - 520) * 2_400 == -48_000 and (2_400 - 2_520) * 500 == -60_000
assert 2 + Fr(1_200_000, 2_400_000) == Fr(5, 2)
_a_pv = 2_000_000 * (Fr(909, 1000) + Fr(826, 1000) + Fr(751, 1000))
assert _a_pv - 4_800_000 == 172_000

SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="acu2-exam-paper-1-multiple-choice",
    mock=True, time_limit_minutes=90, questions=[
        # ---- Partnership Accounting (10)
        M("A and B have capitals of FCFA 4 000 000 and FCFA 2 000 000. The deed gives 5% interest on capital, a salary of FCFA 120 000 to B, and shares the balance 3 : 2. "
          "Profit before appropriation is FCFA 600 000. A's total share of the profit is",
          F_(308_000),
          [(F_(108_000), "This is only A's share of the balance; A's interest on capital is missing."),
           (F_(360_000), "This shares the whole profit 3 : 2 and ignores interest and salary."),
           (F_(200_000), "This is only A's interest on capital.")],
          "Interest: A 200 000, B 100 000. Salary: B 120 000. Balance 600 000 − 300 000 − 120 000 = 180 000; A takes 3/5 = 108 000. A's total = 200 000 + 108 000 = 308 000.",
          T_APPROP, "Calculation", "Deduct interest and salary before sharing the balance."),
        M("Interest charged on a partner's drawings is",
          "debited to the partner's current account and credited to the appropriation account",
          [("credited to the partner's current account and debited to the appropriation account", "This reverses the entry: the partner pays interest, he does not earn it."),
           ("debited to the capital account only", "Fixed capital is not changed by drawings interest."),
           ("ignored because drawings are not a cost to the firm", "The deed may charge interest to compensate the firm and the other partners.")],
          "The partner is charged, so his current account is debited; the firm's appropriation account receives the income.",
          T_APPROP, "Concept", "Who pays the interest on drawings?"),
        M("A partner's current account has an opening credit balance of FCFA 50 000. During the year she is credited with FCFA 308 000 profit share and debited with drawings FCFA 200 000 and interest on drawings FCFA 10 000. The closing balance is",
          "a credit of FCFA 148 000",
          [("a credit of FCFA 168 000", "This adds the interest on drawings instead of deducting it."),
           ("a credit of FCFA 158 000", "This leaves out the interest on drawings."),
           ("a credit of FCFA 358 000", "This ignores drawings and interest on drawings.")],
          "50 000 + 308 000 − 200 000 − 10 000 = 148 000 credit.",
          T_APPROP, "Calculation", "Credits increase the balance, debits decrease it."),
        M("A and B share profits 3 : 2. Premises are revalued upwards by FCFA 500 000. A's share of the revaluation gain is",
          F_(300_000),
          [(F_(250_000), "This shares the gain equally."),
           (F_(500_000), "This gives the whole gain to A."),
           (F_(200_000), "This is B's share.")],
          "A takes 3/5 of 500 000 = 300 000; the gain is shared in the old profit-sharing ratio.",
          T_GOODW, "Calculation", "Which ratio applies to a revaluation before a change?"),
        M("Goodwill is valued at two years' purchase of average annual profits of FCFA 1 500 000. Goodwill is",
          F_(3_000_000),
          [(F_(1_500_000), "This is one year's profit."),
           (F_(750_000), "This divides the profit by two."),
           (F_(4_500_000), "This uses three years' purchase.")],
          "2 × 1 500 000 = 3 000 000.",
          T_GOODW, "Calculation", "Multiply the average profit by the number of years."),
        M("A and B have capitals totalling FCFA 3 000 000. C is admitted for a 1/5 share and brings FCFA 1 000 000 cash. The goodwill implied by C's payment is",
          F_(1_000_000),
          [(F_(2_000_000), "This ignores the cash that C brings into the firm."),
           (F_(200_000), "This is 1/5 of C's payment, not the implied goodwill."),
           (F_(5_000_000), "This is the implied total value of the firm, not the goodwill.")],
          "If 1 000 000 buys 1/5, the firm is worth 5 000 000. Net assets after admission = 3 000 000 + 1 000 000 = 4 000 000. Goodwill = 5 000 000 − 4 000 000 = 1 000 000.",
          T_ADMIT, "Calculation", "What total value does C's payment imply?"),
        M("A and B share profits 3 : 2. C is admitted with a 1/5 share taken from A and B in their old ratio. The new ratio A : B : C is",
          "12 : 8 : 5",
          [("3 : 2 : 1", "This keeps the old ratio and adds a share for C without adjustment."),
           ("2 : 2 : 1", "This takes C's share equally from A and B, not in their old ratio."),
           ("4 : 4 : 1", "This is not derived from the old ratio.")],
          "A: 3/5 × 4/5 = 12/25; B: 2/5 × 4/5 = 8/25; C: 5/25. Ratio 12 : 8 : 5.",
          T_ADMIT, "Calculation", "Old partners keep 4/5 between them."),
        M("Goodwill is FCFA 3 000 000. B, who has a 2/5 share, retires and the firm's goodwill is revalued. B's share of goodwill is",
          F_(1_200_000),
          [(F_(1_500_000), "This takes half of the goodwill."),
           (F_(1_800_000), "This is A's 3/5 share."),
           (F_(600_000), "This takes 1/5 of the goodwill.")],
          "2/5 × 3 000 000 = 1 200 000.",
          T_RETIRE, "Calculation", "Apply B's profit share to the goodwill."),
        M("A, B and C share profits 5 : 3 : 2. C retires and A and B will share 3 : 2. The gaining ratio of A to B is",
          "1 : 1",
          [("3 : 2", "This is their new sharing ratio, not the ratio in which they gain."),
           ("5 : 3", "This is their old ratio."),
           ("1 : 2", "This is not supported by the new and old shares.")],
          "A: 3/5 − 5/10 = 1/10. B: 2/5 − 3/10 = 1/10. Gaining ratio 1 : 1.",
          T_RETIRE, "Calculation", "Gain = new share − old share."),
        M("On dissolution, assets with a book value of FCFA 5 000 000 are sold for FCFA 4 200 000. The partners share profits 3 : 2. A's share of the realisation loss is",
          F_(480_000),
          [(F_(400_000), "This shares the loss equally."),
           (F_(800_000), "This is the whole loss."),
           (F_(320_000), "This is B's share.")],
          "Loss 800 000; A takes 3/5 = 480 000.",
          T_DISSOL, "Calculation", "Share the loss in the profit-sharing ratio."),
        # ---- Company Formation, Share Capital & Debentures (8)
        M("Under the OHADA Uniform Act, the minimum share capital of an SA is",
          F_(10_000_000),
          [(F_(1_000_000), "This is the default minimum figure for an SARL; check the national rule."),
           (F_(100_000_000), "This is far above the general SA minimum."),
           (F_(5_000_000), "This is not the Uniform Act minimum.")],
          "The SA minimum capital is FCFA 10 000 000 (check the current rule).",
          T_FORM, "Recall", "Recall the SA rule."),
        M("An SA's founders subscribe 400 shares of nominal value FCFA 10 000, payable in cash. The minimum amount payable on subscription is",
          F_(1_000_000),
          [(F_(4_000_000), "This is the whole nominal value."),
           (F_(2_000_000), "This takes half of the nominal value."),
           (F_(400_000), "This divides by the number of shares and not the nominal value.")],
          "At least one quarter of the nominal value must be paid: 1/4 × 4 000 000 = 1 000 000.",
          T_FORM, "Application", "A quarter of the nominal value."),
        M("An SA issues 3 000 shares of nominal value FCFA 10 000 at FCFA 12 500. The share premium is",
          F_(7_500_000),
          [(F_(30_000_000), "This is the nominal capital."),
           (F_(37_500_000), "This is the total issue price."),
           (F_(2_500), "This is the premium per share.")],
          "Premium per share 2 500; total 3 000 × 2 500 = 7 500 000.",
          T_ISSUE, "Calculation", "Premium = issue price − nominal value."),
        M("For the same issue, the premium must be paid in full and one quarter of the nominal value on subscription. The cash received on subscription is",
          F_(15_000_000),
          [(F_(7_500_000), "This is the premium only, or a quarter of the nominal value only."),
           (F_(37_500_000), "This is the entire issue price."),
           (F_(9_375_000), "This takes a quarter of the whole issue price.")],
          "Quarter of nominal: 7 500 000. Premium: 7 500 000. Total 15 000 000.",
          T_ISSUE, "Calculation", "Add the quarter of nominal value and the premium."),
        M("An SA makes a profit of FCFA 12 000 000 with no losses brought forward. The legal reserve allocation (10%) is",
          F_(1_200_000),
          [(F_(2_400_000), "This takes 20%, the ceiling in relation to capital."),
           (F_(120_000), "This is 1% of profit."),
           (F_(10_800_000), "This is the profit after the reserve.")],
          "10% × 12 000 000 = 1 200 000, until the reserve reaches one fifth of the capital.",
          T_CAPPROP, "Calculation", "One tenth of the profit."),
        M("A gross dividend is FCFA 3 000 per share. Using a teaching IRCM rate of 16.5% (check the Finance Law), the net dividend per share is",
          F_(2_505),
          [(F_(2_835), "This applies 5.5% instead of 16.5%."),
           (F_(495), "This is the tax withheld, not the net dividend."),
           (F_(3_000), "This ignores the tax withheld.")],
          "Tax = 16.5% × 3 000 = 495; net = 3 000 − 495 = 2 505.",
          T_CAPPROP, "Calculation", "Deduct the tax withheld."),
        M("A company issues debentures with a nominal value of FCFA 5 000 000 carrying 8% interest. The annual interest is",
          F_(400_000),
          [(F_(40_000), "This is 0.8% of nominal."),
           (F_(4_000_000), "This is 80% of nominal."),
           (F_(500_000), "This is 10% of nominal.")],
          "8% × 5 000 000 = 400 000, always calculated on the nominal value.",
          T_DEBEN, "Calculation", "Interest is a percentage of nominal value."),
        M("1 000 debentures of nominal value FCFA 10 000 are issued at FCFA 9 500. The cash received is",
          F_(9_500_000),
          [(F_(10_000_000), "This is the nominal value."),
           (F_(500_000), "This is the discount."),
           (F_(9_000_000), "This is not derived from the issue price.")],
          "1 000 × 9 500 = 9 500 000; the discount of 500 000 is a cost of borrowing.",
          T_DEBEN, "Calculation", "Cash received = number × issue price."),
        # ---- Modification of Capital, Taxation, Amalgamation & Liquidation (9)
        M("Net assets are FCFA 60 000 000 and there are 4 000 shares. The mathematical value of a share is",
          F_(15_000),
          [(F_(10_000), "This is the nominal value."),
           (F_(240_000_000), "This multiplies net assets by the number of shares."),
           (F_(60_000), "This divides by 1 000 instead of 4 000.")],
          "60 000 000 ÷ 4 000 = 15 000.",
          T_INCR, "Calculation", "Net assets divided by the number of shares."),
        M("5 000 old shares are worth FCFA 18 000 each. 1 000 new shares are issued for cash at FCFA 12 000. The subscription right (DS) per old share is",
          F_(1_000),
          [(F_(6_000), "This is the gap between old value and issue price, not the fall in value."),
           (F_(17_000), "This is the value after the issue."),
           (F_(1_200), "This divides the gap by 5.")],
          "V1 = (5 000 × 18 000 + 1 000 × 12 000) ÷ 6 000 = 17 000. DS = 18 000 − 17 000 = 1 000.",
          T_INCR, "Calculation", "DS is the fall in the share's value."),
        M("4 000 shares have net assets of FCFA 60 000 000. 1 000 free shares are issued by incorporating reserves. The attribution right (DA) per old share is",
          F_(3_000),
          [(F_(12_000), "This is the value after the bonus issue."),
           (F_(15_000), "This is the value before the bonus issue."),
           (F_(600), "This is not derived from the two values.")],
          "V0 = 15 000; V1 = 60 000 000 ÷ 5 000 = 12 000; DA = 3 000.",
          T_INCR, "Calculation", "Net assets do not change in a bonus issue."),
        M("A company has capital of FCFA 30 000 000 in 3 000 shares and losses of FCFA 18 000 000. It reduces capital by the losses by lowering the nominal value. The new nominal value is",
          F_(4_000),
          [(F_(6_000), "This is the reduction per share."),
           (F_(10_000), "This is the old nominal value."),
           (F_(12_000), "This is the new capital in thousands, not a nominal value.")],
          "New capital 12 000 000 ÷ 3 000 shares = 4 000.",
          T_REDUC, "Calculation", "Divide the new capital by the number of shares."),
        M("A share whose nominal value has been repaid out of reserves by amortization of capital is called",
          "a jouissance share",
          [("a preference share", "A preference share carries a priority right, not repayment of nominal value."),
           ("a bonus share", "A bonus share is issued free by incorporation of reserves."),
           ("a founder share", "A founder share is a different security.")],
          "Capital shares are replaced by jouissance shares (actions de jouissance) after amortization.",
          T_REDUC, "Recall", "Which share has been repaid?"),
        M("Accounting profit is FCFA 10 000 000. Non-deductible expenses of FCFA 1 500 000 and non-taxable income of FCFA 500 000 appear in the fiscal analysis. Using a teaching tax rate of 30% (check the Finance Law), the tax is",
          F_(3_300_000),
          [(F_(3_000_000), "This applies the rate to accounting profit and ignores the fiscal adjustments."),
           (F_(3_450_000), "This adds back the expenses but forgets to deduct the non-taxable income."),
           (F_(2_400_000), "This deducts the non-deductible expenses instead of adding them back.")],
          "Fiscal result 10 000 000 + 1 500 000 − 500 000 = 11 000 000; tax 30% = 3 300 000.",
          T_TAX, "Calculation", "Add back, then deduct."),
        M("In a fiscal analysis, which adjustment increases taxable profit?",
          "Adding back an expense that the tax rules do not allow",
          [("Deducting income that is exempt from tax", "This reduces taxable profit."),
           ("Deducting a loss brought forward that the rules allow", "This reduces taxable profit."),
           ("Deducting depreciation at the allowed rate", "This is an allowed expense and reduces taxable profit.")],
          "Expenses not allowed are added back, which increases the taxable profit.",
          T_TAX, "Concept", "Which adjustment works against the company?"),
        M("In a merger, a share of company A is worth FCFA 15 000 and a share of company B is worth FCFA 9 000. B has 5 000 shares. The number of A shares issued to B's shareholders is",
          "3 000",
          [("5 000", "This exchanges one share of A for each share of B, ignoring the difference in value."),
           ("9 000", "This confuses the value per share with the number of shares."),
           ("15 000", "This confuses A's value per share with a number of shares.")],
          "Parity 9 000 ÷ 15 000 = 3/5: 3 A shares for 5 B shares; 5 000 × 3/5 = 3 000.",
          T_MERGE, "Calculation", "Exchange by value, not by number."),
        M("A company in liquidation realises assets for FCFA 18 000 000. Liabilities are FCFA 14 000 000 and liquidation costs FCFA 1 000 000. There are 3 000 shares. The amount per share is",
          F_(1_000),
          [(F_(6_000), "This ignores liabilities and costs."),
           (F_(1_333), "This ignores the liquidation costs."),
           (F_(5_000), "This divides the liabilities by the number of shares.")],
          "Surplus 18 000 000 − 14 000 000 − 1 000 000 = 3 000 000; per share 1 000. Creditors and costs are paid before shareholders.",
          T_LIQ, "Calculation", "Who is paid first?"),
        # ---- Financial Statement Analysis (6)
        M("Stable resources are FCFA 52 000 000 and stable uses FCFA 45 000 000. The net global working capital (FRNG) is",
          F_(7_000_000),
          [(F_(97_000_000), "This adds the two figures."),
           (F_(-7_000_000), "The sign is reversed."),
           (F_(45_000_000), "This copies the stable uses.")],
          "FRNG = 52 000 000 − 45 000 000 = 7 000 000.",
          T_FUNC, "Calculation", "Resources minus uses."),
        M("FRNG is FCFA 7 000 000 and BFR is FCFA 9 000 000. The net cash is",
          F_(-2_000_000),
          [(F_(2_000_000), "This calculates BFR − FRNG."),
           (F_(16_000_000), "This adds the two figures."),
           (F_(-9_000_000), "This ignores FRNG.")],
          "TN = FRNG − BFR = −2 000 000.",
          T_FUNC, "Calculation", "Which is subtracted from which?"),
        M("A dividend decided by the shareholders and payable next month is shown in the financial balance sheet as",
          "a short-term debt, with equity reduced",
          [("part of equity", "It has left equity because it is owed to shareholders."),
           ("a long-term debt", "It is payable within the year."),
           ("an asset", "Nothing is owned; it is owed.")],
          "A declared dividend becomes a debt due within a year.",
          T_FIN, "Concept", "Is it still the shareholders' capital?"),
        M("Assets under one year are FCFA 13 500 000 and debts under one year FCFA 9 000 000. The current ratio is",
          "1.50",
          [("0.67", "This divides debts by assets."),
           ("4.50", "This is the difference, not the ratio."),
           ("2.25", "This is not derived from the two figures.")],
          "13 500 000 ÷ 9 000 000 = 1.50.",
          T_FIN, "Calculation", "Assets over debts."),
        M("Sales are FCFA 150 000 000 and cost of sales FCFA 105 000 000. The gross margin is",
          "30%",
          [("70%", "This is cost of sales as a percentage of sales."),
           ("42.9%", "This divides gross profit by cost of sales (a mark-up)."),
           ("10%", "This is not derived from the two figures.")],
          "Gross profit 45 000 000 ÷ 150 000 000 = 30%.",
          T_RATIO, "Calculation", "Gross profit over sales."),
        M("Trade receivables are FCFA 25 000 000 and all sales (FCFA 150 000 000) are on credit. Using 360 days, the collection period is",
          "60 days",
          [("85.7 days", "This divides by cost of sales."),
           ("6 days", "This is the turnover number, not days."),
           ("16.7 days", "This is the percentage, not days.")],
          "25 000 000 ÷ 150 000 000 × 360 = 60 days.",
          T_RATIO, "Calculation", "Receivables over credit sales times days."),
        # ---- Cost Accounting (10)
        M("At 2 000 units total cost is FCFA 1 100 000; at 5 000 units it is FCFA 1 700 000. By the high-low method the fixed cost is",
          F_(700_000),
          [(F_(1_100_000), "This is the total cost at the low point."),
           (F_(200), "This is the variable cost per unit."),
           (F_(400_000), "This uses the wrong variable cost.")],
          "Variable cost = 600 000 ÷ 3 000 = 200. Fixed = 1 100 000 − 2 000 × 200 = 700 000.",
          T_OVH, "Calculation", "Find the variable cost per unit first."),
        M("Service centres A and B serve each other: A = 880 000 + 0.2B and B = 500 000 + 0.1A. The total of A to be distributed is",
          F_(1_000_000),
          [(F_(880_000), "This ignores the service received from B."),
           (F_(1_050_000), "This is not the solution of the equations."),
           (F_(600_000), "This is the total of B.")],
          "A = 880 000 + 0.2(500 000 + 0.1A) = 980 000 + 0.02A, so 0.98A = 980 000 and A = 1 000 000.",
          T_OVH, "Calculation", "Substitute B into the equation for A."),
        M("Opening stock: 500 units at FCFA 800. Purchases: 1 500 units costing FCFA 1 290 000 in all. The weighted average cost per unit, including the opening stock, is",
          F_(845),
          [(F_(830), "This averages the two unit prices without weights."),
           (F_(860), "This is the price of the purchases only."),
           (F_(800), "This is the price of the opening stock only.")],
          "(400 000 + 1 290 000) ÷ 2 000 = 845.",
          T_STOCK, "Calculation", "Total value over total quantity."),
        M("Using the same data, FIFO values the issue of 1 200 units at",
          F_(1_002_000),
          [(F_(1_014_000), "This values the issue at the weighted average of 845."),
           (F_(1_032_000), "This takes the newest units first (LIFO)."),
           (F_(960_000), "This values all units at the opening price.")],
          "500 × 800 + 700 × 860 = 400 000 + 602 000 = 1 002 000.",
          T_STOCK, "Calculation", "Oldest units first."),
        M("Budgeted overheads are FCFA 5 400 000 and budgeted machine hours 6 000. The overhead absorption rate is",
          F_(900),
          [(F_(1_111), "This divides hours by overheads."),
           (F_(5_400), "This divides overheads by 1 000."),
           (F_(30_000_000), "This multiplies the two budget figures.")],
          "5 400 000 ÷ 6 000 = 900 per hour.",
          T_JOB, "Calculation", "Budgeted overheads over budgeted activity."),
        M("3 000 units are finished and 600 remain in progress, 50% complete for conversion. Conversion costs are FCFA 1 980 000. The conversion cost per equivalent unit is",
          F_(600),
          [(F_(550), "This divides by all 3 600 units, as if the WIP were complete."),
           (F_(660), "This divides by the finished units only."),
           (F_(1_980_000), "This is the total cost.")],
          "Equivalent units 3 000 + 300 = 3 300; 1 980 000 ÷ 3 300 = 600.",
          T_JOB, "Calculation", "Count the WIP at its degree of completion."),
        M("A purchasing pool costs FCFA 2 400 000 and 30 orders were placed. Product X needed 12 orders. The cost charged to X is",
          F_(960_000),
          [(F_(2_400_000), "This is the whole pool."),
           (F_(80_000), "This is the rate per order."),
           (F_(1_440_000), "This is the cost charged to the other products.")],
          "Rate 2 400 000 ÷ 30 = 80 000 per order; X: 12 × 80 000 = 960 000.",
          T_ABC, "Calculation", "Find the cost per order first."),
        M("The selling price is FCFA 6 000 and the variable cost FCFA 3 900. The contribution/sales ratio is",
          "35%",
          [("65%", "This is the variable cost ratio."),
           ("2 100", "This is the contribution per unit."),
           ("53.8%", "This divides the contribution by the variable cost.")],
          "Contribution 2 100 ÷ 6 000 = 35%.",
          T_MARG, "Calculation", "Contribution over price."),
        M("Fixed costs are FCFA 8 400 000 and the contribution is FCFA 2 100 a unit. The break-even point is",
          "4 000 units",
          [("1 400 units", "This divides by the selling price of 6 000."),
           ("8 400 000 units", "This copies the fixed costs."),
           ("17 640 units", "This multiplies instead of dividing.")],
          "8 400 000 ÷ 2 100 = 4 000.",
          T_MARG, "Calculation", "Fixed costs over contribution per unit."),
        M("Budgeted sales are 6 000 units and the break-even point is 4 000 units. The margin of safety as a percentage of budgeted sales is",
          "33.3%",
          [("50%", "This divides by break-even sales instead of budgeted sales."),
           ("66.7%", "This is break-even sales as a percentage of budget."),
           ("2 000%", "This is the margin in units, not a percentage.")],
          "(6 000 − 4 000) ÷ 6 000 = 33.3%.",
          T_MARG, "Calculation", "Compare with budgeted sales."),
        # ---- Budgetary Control, Standard Costing & Capital Budgeting (7)
        M("Budgeted sales are 3 600 units; opening stock 500 units; required closing stock 700 units. Production is",
          "3 800 units",
          [("3 600 units", "This ignores the change in stock."),
           ("3 400 units", "This reverses the stock adjustment."),
           ("4 800 units", "This adds both stocks without taking the opening stock from the total.")],
          "Production = 3 600 + 700 − 500 = 3 800.",
          T_BUDG, "Calculation", "Sales plus closing stock minus opening stock."),
        M("Sales: month 1 FCFA 3 000 000, month 2 FCFA 4 000 000. Customers pay 40% in the month of sale and 60% the following month. Cash received in month 2 is",
          F_(3_400_000),
          [(F_(4_000_000), "This assumes all of month 2's sales are paid in month 2."),
           (F_(2_400_000), "This is the credit part of month 2's sales only."),
           (F_(3_000_000), "This is not derived from the payment pattern.")],
          "40% × 4 000 000 + 60% × 3 000 000 = 1 600 000 + 1 800 000 = 3 400 000.",
          T_BUDG, "Calculation", "Two months of sales contribute."),
        M("A semi-variable cost is FCFA 300 000 fixed plus FCFA 25 per unit. At 9 000 units the flexed cost is",
          F_(525_000),
          [(F_(225_000), "This leaves out the fixed part."),
           (F_(300_000), "This leaves out the variable part."),
           (F_(675_000), "This applies 75 per unit.")],
          "300 000 + 25 × 9 000 = 525 000.",
          T_FLEX, "Calculation", "Keep the fixed part; flex the variable part."),
        M("Standard price FCFA 500 a kg. 2 400 kg were bought at FCFA 520 a kg. The material price variance is",
          "FCFA 48 000 adverse",
          [("FCFA 48 000 favourable", "Paying more than standard is adverse."),
           ("FCFA 10 000 adverse", "This uses 500 kg."),
           ("FCFA 20 adverse", "This is the variance per kg.")],
          "(500 − 520) × 2 400 = −48 000.",
          T_STD, "Calculation", "(Standard price − actual price) × actual quantity."),
        M("The standard is 4 kg per unit at FCFA 500 a kg. Actual output of 600 units used 2 520 kg. The material usage variance is",
          "FCFA 60 000 adverse",
          [("FCFA 60 000 favourable", "Using more than standard is adverse."),
           ("FCFA 50 400 adverse", "This values the excess at an actual price."),
           ("FCFA 120 adverse", "This is the excess in kilograms, not in FCFA.")],
          "Standard quantity 600 × 4 = 2 400 kg; (2 400 − 2 520) × 500 = −60 000.",
          T_STD, "Calculation", "Standard quantity for actual output."),
        M("A project costs FCFA 4 800 000 and earns FCFA 1 600 000, 2 000 000, 2 400 000 and 1 200 000 in years 1 to 4. The payback period is",
          "2.5 years",
          [("2.0 years", "After two years 3 600 000 has been recovered, not 4 800 000."),
           ("3.0 years", "This takes the year in which payback completes."),
           ("4.0 years", "This is the whole life of the project.")],
          "After 2 years 3 600 000 is recovered; 1 200 000 remains; 1 200 000 ÷ 2 400 000 = 0.5, so 2.5 years.",
          T_INV, "Calculation", "Find when cumulative cash equals the outlay."),
        M("A project costs FCFA 4 800 000 and gives FCFA 2 000 000 a year for three years. The discount factors at 10% are 0.909, 0.826 and 0.751. The NPV is",
          "+FCFA 172 000",
          [("+FCFA 1 200 000", "This does not discount: 6 000 000 − 4 800 000."),
           ("−FCFA 172 000", "The sign is reversed."),
           ("+FCFA 4 972 000", "This forgets to subtract the outlay.")],
          "PV = 2 000 000 × 2.486 = 4 972 000; NPV = 4 972 000 − 4 800 000 = +172 000.",
          T_INV, "Calculation", "Discount the inflows, then subtract the outlay."),
    ]))
assert len(SETS[-1]["questions"]) == 50

# ====================================================================== Paper 2 practice paper A and Paper 3 practice paper A
use(202)

# ---------------- Paper 2 data (all checked) ----------------
_v = Fr(2_040_000 - 1_560_000, 4_000 - 2_400)
assert _v == 300 and 1_560_000 - 2_400 * 300 == 840_000 and 840_000 + 3_000 * 300 == 1_740_000
assert Fr(7_200_000, 12_000) == 600
assert 300_000 + 50 * 800 + 50 * 600 == 370_000
assert (370_000 + Fr(10, 100) * 370_000) / Fr(80, 100) == 508_750
assert 7_500_000 - 11_800 * 600 == 420_000
assert Fr(400 * 500 + 1_600 * 550, 2_000) == 540 and 400 * 500 + 1_100 * 550 == 805_000 and 500 * 550 == 275_000
assert 1_500 * 540 == 810_000 and 810_000 - 805_000 == 5_000 and 270_000 + 810_000 == 200_000 + 880_000
assert (400 - 410) * 1_600 == -16_000 and (1_500 - 1_600) * 400 == -40_000
assert (900 - 880) * 1_050 == 21_000 and (1_000 - 1_050) * 900 == -45_000 and 656_000 / 1_600 == 410 and 924_000 / 1_050 == 880
assert 500 * 2 * 900 - 924_000 == -24_000 == 21_000 - 45_000
_rec = {"Jan": 2_000_000 // 2 + 1_600_000 // 2, "Feb": 2_400_000 // 2 + 2_000_000 // 2, "Mar": 2_800_000 // 2 + 2_400_000 // 2}
_pay = {"Jan": 900_000 + 400_000 + 240_000, "Feb": 1_100_000 + 400_000 + 240_000 + 1_200_000, "Mar": 1_300_000 + 400_000 + 240_000}
_bal, _o = {}, 400_000
for _m in ("Jan", "Feb", "Mar"):
    _bal[_m] = _o + _rec[_m] - _pay[_m]
    _o = _bal[_m]
assert _rec == {"Jan": 1_800_000, "Feb": 2_200_000, "Mar": 2_600_000}
assert _pay == {"Jan": 1_540_000, "Feb": 2_940_000, "Mar": 1_940_000}
assert _bal == {"Jan": 660_000, "Feb": -80_000, "Mar": 580_000}
assert Fr(370_000, Fr(8, 10)) == 462_500 and 407_000 * Fr(12, 10) == 488_400 and 4_000 - 2_600 == 1_400 and Fr(11_200_000, Fr(1_400, 4_000)) == 32_000_000 and Fr(11_200_000, 1_400) == 8_000
assert Fr(9_000 - 8_000, 9_000) * 100 > 11.1 and Fr(1_000, 9_000) * 100 < 11.2 and Fr(11_200_000 + 3_500_000, 1_400) == 10_500

_q1 = ("Question 1 (nature of cost). The lowest activity of a workshop was 2 400 machine hours with a total maintenance cost of FCFA 1 560 000; "
       "the highest was 4 000 hours with FCFA 2 040 000. ")
_q2 = ("Question 2 (overheads and job costing). Budgeted overheads are FCFA 7 200 000 and budgeted direct labour hours 12 000. Job K22 uses materials FCFA 300 000 "
       "and 50 direct labour hours at FCFA 800. Administration costs are 10% of production cost. ")
_q3 = ("Question 3 (stock valuation). Opening stock 400 units at FCFA 500. Purchases 1 600 units at FCFA 550. 1 500 units are issued. ")
_q4 = ("Question 4 (standard costing). The standard cost card per unit shows 3 kg of material at FCFA 400 a kg and 2 labour hours at FCFA 900 an hour. "
       "Actual output 500 units used 1 600 kg costing FCFA 656 000 and 1 050 hours costing FCFA 924 000. ")
_q5 = ("Question 5 (cash budget). Opening cash on 1 January is FCFA 400 000. Sales: December 1 600 000, January 2 000 000, February 2 400 000, March 2 800 000; half is paid in the month of sale and half the next month. "
       "Purchases (paid the month after): December 900 000, January 1 100 000, February 1 300 000. Wages 400 000 a month. Other expenses 300 000 a month including depreciation of 60 000. "
       "Equipment costing 1 200 000 is paid in February. ")
_q6 = ("Question 6 (break-even). Selling price FCFA 4 000; variable cost FCFA 2 600 a unit (production 2 200, distribution 400); fixed costs FCFA 11 200 000; budgeted sales 9 000 units. ")

SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="acu2-exam-paper-2-cost-management",
    mock=True, time_limit_minutes=150, questions=[
        M(_q1 + "(a) Using the high-low method, the variable cost per machine hour is",
          F_(300), [(F_(480_000), "This is the difference in cost, not the cost per hour."),
                    (F_(1_600), "This is the difference in hours."),
                    (F_(390), "This averages the costs per hour of the two extremes.")],
          "(2 040 000 − 1 560 000) ÷ (4 000 − 2 400) = 300.", T_OVH, "Calculation", "Change in cost over change in activity."),
        M(_q1 + "(b) The fixed cost for the period is",
          F_(840_000), [(F_(1_560_000), "This is the total cost at the low point."),
                        (F_(720_000), "This is the variable part at the low point."),
                        (F_(1_200_000), "This uses the wrong variable cost.")],
          "1 560 000 − 2 400 × 300 = 840 000.", T_OVH, "Calculation", "Total cost less variable cost at one point."),
        M(_q1 + "(c) The expected cost for 3 000 machine hours is",
          F_(1_740_000), [(F_(900_000), "This is the variable part only."),
                          (F_(2_040_000), "This is the cost at 4 000 hours."),
                          (F_(1_800_000), "This applies 320 per hour.")],
          "840 000 + 3 000 × 300 = 1 740 000.", T_OVH, "Calculation", "Fixed cost plus variable cost."),
        M(_q1 + "(d) An electricity bill with a fixed standing charge plus a charge per unit used is",
          "a semi-variable cost", [("a fixed cost", "The per-unit charge makes the total change with usage."),
                                   ("a variable cost", "The standing charge does not change with usage."),
                                   ("a direct cost", "Direct or indirect describes traceability, not behaviour.")],
          "It has a fixed part and a variable part.", T_OVH, "Concept", "What are its two parts?"),
        M(_q2 + "(a) The overhead absorption rate per direct labour hour is",
          F_(600), [(F_(1_667), "This divides hours by overheads."), (F_(7_200), "This divides overheads by 1 000."),
                    (F_(800), "This is the labour rate.")],
          "7 200 000 ÷ 12 000 = 600.", T_JOB, "Calculation", "Budgeted overheads over budgeted hours."),
        M(_q2 + "(b) The production cost of Job K22 is",
          F_(370_000), [(F_(340_000), "This is the prime cost without overhead."), (F_(30_000), "This is the overhead only."),
                        (F_(407_000), "This includes the administration costs, which are not production costs.")],
          "300 000 + 50 × 800 + 50 × 600 = 370 000.", T_JOB, "Calculation", "Prime cost plus absorbed overhead."),
        M(_q2 + "(c) The price that gives a profit of 20% of the selling price is",
          F_(508_750), [(F_(488_400), "This adds a 20% mark-up to total cost instead of dividing by 0.8."),
                        (F_(462_500), "This divides production cost by 0.8 and ignores the administration costs."),
                        (F_(407_000), "This is the total cost with no profit.")],
          "Total cost 370 000 + 37 000 = 407 000; price = 407 000 ÷ 0.8 = 508 750.", T_JOB, "Calculation", "Cost is 80% of the price."),
        N(_q2 + "(d) Actual overheads were FCFA 7 500 000 and actual direct labour hours 11 800. The overhead under-absorbed is (FCFA)",
          420_000, [("Absorbed", "11 800 × 600 = 7 080 000."), ("Under-absorbed", "7 500 000 − 7 080 000 = 420 000.")],
          T_JOB, "Calculation", "Absorbed overhead uses actual hours."),
        M(_q3 + "(a) The weighted average cost per unit (CUMP) is",
          F_(540), [(F_(525), "This averages the two unit prices without weights."),
                    (F_(550), "This is the price of the purchases only."), (F_(500), "This is the price of the opening stock.")],
          "(200 000 + 880 000) ÷ 2 000 = 540.", T_STOCK, "Calculation", "Total value over total quantity."),
        M(_q3 + "(b) By FIFO, the value of the 1 500 units issued is",
          F_(805_000), [(F_(810_000), "This uses the weighted average of 540."),
                        (F_(825_000), "This values all issues at the latest price of 550."),
                        (F_(750_000), "This values all issues at the opening price.")],
          "400 × 500 + 1 100 × 550 = 805 000.", T_STOCK, "Calculation", "Oldest units first."),
        M(_q3 + "(c) By FIFO, the closing stock of 500 units is valued at",
          F_(275_000), [(F_(270_000), "This is the weighted average value."), (F_(250_000), "This values the stock at the opening price."),
                        (F_(1_080_000), "This is the value of all goods available.")],
          "500 × 550 = 275 000 (check: 805 000 + 275 000 = 1 080 000).", T_STOCK, "Calculation", "The latest purchase remains."),
        M(_q3 + "(d) Compared with the weighted average method, FIFO gives a profit that is",
          F_(5_000) + " higher", [(F_(5_000) + " lower", "FIFO charges less cost here (805 000 against 810 000), so profit is higher."),
                                  (F_(10_000) + " higher", "The difference is 810 000 − 805 000 = 5 000."),
                                  ("the same", "The two methods charge different costs to the period.")],
          "CUMP charges 810 000 and FIFO 805 000, so FIFO profit is 5 000 higher when prices are rising.", T_STOCK, "Reasoning", "Compare the cost of issues."),
        M(_q4 + "(a) The material price variance is",
          "FCFA 16 000 adverse", [("FCFA 16 000 favourable", "Paying more than standard is adverse."),
                                  ("FCFA 40 000 adverse", "This is the usage variance."), ("FCFA 10 adverse", "This is the variance per kg.")],
          "(400 − 410) × 1 600 = −16 000.", T_STD, "Calculation", "Actual price is 656 000 ÷ 1 600 = 410."),
        M(_q4 + "(b) The material usage variance is",
          "FCFA 40 000 adverse", [("FCFA 40 000 favourable", "Using more than standard is adverse."),
                                  ("FCFA 41 000 adverse", "This values the excess at the actual price."), ("FCFA 100 adverse", "This is the excess in kilograms.")],
          "Standard quantity 1 500 kg; (1 500 − 1 600) × 400 = −40 000.", T_STD, "Calculation", "Standard quantity for 500 units is 1 500 kg."),
        M(_q4 + "(c) The labour rate variance is",
          "FCFA 21 000 favourable", [("FCFA 21 000 adverse", "Paying less per hour than standard is favourable."),
                                     ("FCFA 20 000 favourable", "This uses 1 000 hours instead of 1 050."), ("FCFA 45 000 favourable", "This is the efficiency variance (and it is adverse).")],
          "Actual rate 924 000 ÷ 1 050 = 880; (900 − 880) × 1 050 = 21 000 F.", T_STD, "Calculation", "Use the actual hours worked."),
        M(_q4 + "(d) The labour efficiency variance is",
          "FCFA 45 000 adverse", [("FCFA 45 000 favourable", "More hours than standard is adverse."),
                                  ("FCFA 44 000 adverse", "This values the extra hours at the actual rate."), ("FCFA 24 000 adverse", "This is the total labour variance.")],
          "Standard hours 1 000; (1 000 − 1 050) × 900 = −45 000. Total labour 24 000 A.", T_STD, "Calculation", "Standard hours for actual output."),
        M(_q5 + "(a) Cash received from customers in January is",
          F_(1_800_000), [(F_(2_000_000), "This takes all of January's sales."), (F_(1_000_000), "This leaves out December's credit sales."),
                          (F_(800_000), "This is December's credit part only.")],
          "50% × 2 000 000 + 50% × 1 600 000 = 1 800 000.", T_BUDG, "Calculation", "January receives part of two months."),
        M(_q5 + "(b) Total cash payments in February are",
          F_(2_940_000), [(F_(2_000_000), "This leaves out the equipment or the expenses."),
                          (F_(3_000_000), "This includes depreciation in the other expenses."),
                          (F_(1_740_000), "This leaves out the equipment payment.")],
          "Purchases 1 100 000 + wages 400 000 + expenses 240 000 + equipment 1 200 000 = 2 940 000.", T_BUDG, "Calculation", "Depreciation is not a cash payment."),
        M(_q5 + "(c) The closing cash balance at the end of February is",
          "an overdraft of FCFA 80 000", [("a balance of FCFA 80 000", "Payments exceed cash available, so it is an overdraft."),
                                          ("a balance of FCFA 660 000", "This is the January balance."), ("an overdraft of FCFA 740 000", "This subtracts the January balance twice.")],
          "January closing 660 000; February: 660 000 + 2 200 000 − 2 940 000 = −80 000.", T_BUDG, "Calculation", "Carry the January closing balance forward."),
        M(_q5 + "(d) The closing cash balance at the end of March is",
          F_(580_000), [(F_(660_000), "This is the January balance."), (F_(660_000 + 80_000), "This adds the February overdraft instead of deducting it."),
                        (F_(500_000), "This deducts the February overdraft twice.")],
          "−80 000 + 2 600 000 − 1 940 000 = 580 000.", T_BUDG, "Calculation", "Opening + receipts − payments."),
        M(_q5 + "(e) Which item is correctly left out of the cash budget?",
          "Depreciation of 60 000 a month", [("Wages of 400 000 a month", "Wages are paid in cash."), ("The equipment payment in February", "A capital payment is a cash outflow when paid."),
                                             ("Purchases paid the following month", "These are cash payments in the month paid.")],
          "Depreciation is a non-cash expense.", T_BUDG, "Concept", "Which item involves no cash?"),
        M(_q6 + "(a) The contribution per unit is",
          F_(1_400), [(F_(1_800), "This deducts only production costs, forgetting distribution."), (F_(2_600), "This is the variable cost."),
                      (F_(4_000), "This is the selling price.")],
          "4 000 − 2 600 = 1 400.", T_MARG, "Calculation", "Include variable distribution costs."),
        M(_q6 + "(b) The break-even point in sales value is",
          F_(32_000_000), [(F_(8_000_000), "This is the break-even quantity in thousands, not the value."),
                           (F_(11_200_000), "This is the fixed cost."), (F_(36_000_000), "This is the budgeted sales value.")],
          "C/S ratio 1 400 ÷ 4 000 = 35%; 11 200 000 ÷ 0.35 = 32 000 000 (8 000 units).", T_MARG, "Calculation", "Fixed costs over the C/S ratio."),
        M(_q6 + "(c) The margin of safety as a percentage of budgeted sales is",
          "11.1%", [("12.5%", "This divides by break-even sales."), ("88.9%", "This is break-even sales as a percentage of budget."), ("1 000%", "This is the margin in units.")],
          "(9 000 − 8 000) ÷ 9 000 = 11.1%.", T_MARG, "Calculation", "Compare with budgeted sales."),
        M(_q6 + "(d) The number of units that must be sold to earn a profit of FCFA 3 500 000 is",
          "10 500", [("8 000", "This is the break-even point."), ("2 500", "This divides the profit alone by the contribution."),
                     ("9 000", "This is budgeted sales, which gives a profit of 1 400 000.")],
          "(11 200 000 + 3 500 000) ÷ 1 400 = 10 500.", T_MARG, "Calculation", "Contribution must cover fixed costs and profit."),
    ]))
assert len(SETS[-1]["questions"]) == 25, len(SETS[-1]["questions"])

# ---------------- Paper 3 data ----------------
assert 90_000_000 - 63_000_000 == 27_000_000 and Fr(27, 90) == Fr(3, 10)
_pbit = 90_000_000 - 63_000_000 - 17_000_000
assert _pbit == 10_000_000 and Fr(_pbit, 40_000_000 + 10_000_000) == Fr(1, 5)
assert 10_000_000 + 15_000_000 + 3_000_000 == 28_000_000 and Fr(28, 10) == Fr(14, 5) and Fr(18, 10) == Fr(9, 5)
assert Fr(63_000_000, Fr(8_000_000 + 10_000_000, 2)) == 7 and Fr(10_000_000, 50_000_000) == Fr(1, 5)
assert 10_000_000 + 1_000_000 == 11_000_000 and 8_000_000 + 12_000_000 == 20_000_000
_fa_ = 32_000_000
assert Fr(30_000_000 + 8_000_000 - 32_000_000, 1) == 6_000_000
assert 30_000_000 + 8_000_000 + 7_000_000 == 45_000_000 and 45_000_000 - 32_000_000 == 13_000_000
assert 38_000_000 - 32_000_000 == 6_000_000 and 6_000_000 - 7_000_000 == -1_000_000 and 13_000_000 - 7_000_000 == 6_000_000
assert Fr(49_500_000, 5_000) == 9_900 and Fr(2_700_000 + 3_000_000 + 3_300_000, 3) == 3_000_000 and Fr(3_000_000, 5_000) == 600
assert Fr(600, 6) * 100 == 10_000
assert 14_000_000 + 1_000_000 - 400_000 == 14_600_000 and Fr(30, 100) * 14_600_000 == 4_380_000
assert Fr(72_000_000, 6_000) == 12_000 and 15_000 - 12_000 == 3_000
assert 3_000 * 4 == 12_000
assert Fr(4, 10) * 12_000_000 == 4_800_000 and Fr(10, 100) * 12_000_000 == 1_200_000
assert Fr(6_000 * 2_000 // 10_000 * 0 + 600_000 * 1, 1) == 600_000 and 200_000 + 3 * 120_000 == 560_000

_p1 = ("Question 1 (ratio analysis). Sales FCFA 90 000 000 (all on credit); cost of sales 63 000 000; operating expenses 17 000 000; equity 40 000 000; long-term loan 10 000 000; "
       "inventory: opening 8 000 000, closing 10 000 000; trade receivables 15 000 000; bank 3 000 000; current liabilities 10 000 000. ")
_p2 = ("Question 2 (functional balance sheet). Stable resources FCFA 38 000 000; stable uses 32 000 000; operating BFR 7 000 000. ")
_p3 = ("Question 3 (financial balance sheet). Equity FCFA 30 000 000, long-term debts 8 000 000, short-term debts 7 000 000; assets over one year 32 000 000. ")
_p4 = ("Question 4 (valuation of shares). Net assets (adjusted equity) FCFA 49 500 000; 5 000 shares; dividends of the last three years FCFA 2 700 000, 3 000 000 and 3 300 000. ")
_p5 = ("Question 5 (company tax). Accounting profit FCFA 14 000 000; expenses not deductible for tax 1 000 000; income not taxable 400 000. Use a teaching tax rate of 30% (check the current Finance Law). ")
_p6 = ("Question 6 (increase of capital). A company has 4 000 shares and net assets FCFA 60 000 000. It issues 1 000 free shares by incorporating reserves and, at the same time, 1 000 new shares at FCFA 12 000 in cash. ")
_p7 = ("Question 7 (appropriation). A company's profit is FCFA 12 000 000. The legal reserve takes 10% of the profit. ")
_p8 = ("Question 8 (partnership). A and B (capitals FCFA 4 000 000 and 2 000 000) are allowed 5% interest on capital and share the balance 3 : 2. Profit before appropriation FCFA 600 000. ")
assert 600_000 - 300_000 == 300_000 and 200_000 + Fr(3, 5) * 300_000 == 380_000

SETS.append(practice_set(
    module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="acu2-exam-paper-3-financial-accounting",
    mock=True, time_limit_minutes=150, questions=[
        M(_p1 + "(a) The gross margin is", "30%", [("70%", "This is cost of sales as a percentage of sales."), ("42.9%", "This divides gross profit by cost of sales."),
                                                   ("11.1%", "This is the operating profit margin.")],
          "27 000 000 ÷ 90 000 000 = 30%.", T_RATIO, "Calculation", "Gross profit over sales."),
        M(_p1 + "(b) The return on capital employed (ROCE) is", "20%", [("25%", "This uses equity alone as capital employed."), ("11.1%", "This uses sales as the base."),
                                                                         ("17%", "This uses the operating expenses.")],
          "Profit before interest and tax 90 − 63 − 17 = 10 million; capital employed 50 million; 10 ÷ 50 = 20%.", T_RATIO, "Calculation", "Capital employed = equity + long-term loan."),
        M(_p1 + "(c) The current ratio is", "2.8", [("1.8", "This is the quick ratio."), ("0.36", "This divides liabilities by assets."), ("3.0", "This is not derived from the figures.")],
          "Current assets 10 + 15 + 3 = 28 million; 28 ÷ 10 = 2.8.", T_RATIO, "Calculation", "Add inventory, receivables and bank."),
        M(_p1 + "(d) The quick ratio is", "1.8", [("2.8", "This is the current ratio."), ("1.0", "This is inventory over current liabilities."), ("0.3", "This is the cash ratio.")],
          "(28 − 10) ÷ 10 = 1.8.", T_RATIO, "Calculation", "Remove inventory."),
        M(_p1 + "(e) The inventory turnover, using average inventory, is", "7 times", [("6.3 times", "This uses closing inventory only."), ("10 times", "This divides sales by closing inventory."),
                                                                                       ("9 times", "This is not derived from the cost of sales.")],
          "Average inventory (8 + 10) ÷ 2 = 9 million; 63 ÷ 9 = 7.", T_RATIO, "Calculation", "Cost of sales over average inventory."),
        M(_p2 + "(a) The net global working capital (FRNG) is", F_(6_000_000), [(F_(7_000_000), "This is the BFR."), (F_(70_000_000), "This adds the two stable blocks."), (F_(-6_000_000), "The sign is reversed.")],
          "38 000 000 − 32 000 000 = 6 000 000.", T_FUNC, "Calculation", "Resources minus uses."),
        M(_p2 + "(b) The net cash is", F_(-1_000_000), [(F_(1_000_000), "This calculates BFR − FRNG."), (F_(13_000_000), "This adds FRNG and BFR."), (F_(-7_000_000), "This ignores FRNG.")],
          "TN = 6 000 000 − 7 000 000 = −1 000 000.", T_FUNC, "Calculation", "FRNG minus BFR."),
        M(_p3 + "(a) The financial working capital is", F_(6_000_000), [(F_(-6_000_000), "The sign is reversed."), (F_(38_000_000), "This is permanent capital."),
                                                                          (F_(32_000_000), "This is assets over one year.")],
          "(30 000 000 + 8 000 000) − 32 000 000 = 6 000 000.", T_FIN, "Calculation", "Permanent capital minus assets over one year."),
        M(_p3 + "(b) The assets under one year are", F_(13_000_000), [(F_(45_000_000), "This is total assets."), (F_(7_000_000), "This is the short-term debts."), (F_(6_000_000), "This is the working capital.")],
          "Total assets 30 + 8 + 7 = 45 million; 45 − 32 = 13 million.", T_FIN, "Calculation", "Total assets minus assets over one year."),
        M(_p4 + "(a) The mathematical value of a share is", F_(9_900), [(F_(9_000), "This is not derived from net assets."), (F_(10_000), "This is the nominal value."), (F_(247_500_000), "This multiplies instead of dividing.")],
          "49 500 000 ÷ 5 000 = 9 900.", T_INCR, "Calculation", "Net assets over the number of shares."),
        M(_p4 + "(b) The average dividend per share over the three years is", F_(600), [(F_(660), "This takes the latest year only (3 300 000 ÷ 5 000)."), (F_(540), "This takes the first year only (2 700 000 ÷ 5 000)."),
                                                                                         (F_(1_800), "This adds the three years' dividends per share.")],
          "Average dividend 9 000 000 ÷ 3 = 3 000 000; per share 600.", T_INCR, "Calculation", "Average the years before dividing."),
        M(_p4 + "(c) The financial value of a share, capitalising the average dividend of 600 at 6% (check your textbook's definition), is", F_(10_000),
          [(F_(36), "This multiplies the dividend by the rate."), (F_(3_600), "This multiplies 600 by 6."), (F_(9_900), "This is the mathematical value.")],
          "600 ÷ 0.06 = 10 000.", T_INCR, "Calculation", "Dividend divided by the rate of return."),
        N(_p5 + "(a) The fiscal (taxable) result is (FCFA)", 14_600_000, [("Add back", "14 000 000 + 1 000 000 = 15 000 000."), ("Deduct", "15 000 000 − 400 000 = 14 600 000.")],
          T_TAX, "Calculation", "Add back what is not deductible; deduct what is not taxable."),
        M(_p5 + "(b) The tax due is", F_(4_380_000), [(F_(4_200_000), "This applies the rate to accounting profit."), (F_(4_500_000), "This applies the rate to 15 000 000, forgetting the non-taxable income."),
                                                      (F_(14_600_000), "This is the fiscal result, not the tax.")],
          "30% × 14 600 000 = 4 380 000.", T_TAX, "Calculation", "Apply the rate to the fiscal result."),
        M(_p5 + "(c) A non-deductible expense, in a fiscal analysis, is", "added back to the accounting profit", [("deducted from the accounting profit", "That would lower taxable profit."),
                                                                                                                      ("ignored completely", "It must be added back."), ("treated as a tax credit", "It is not a credit.")],
          "Expenses disallowed by tax rules are added back.", T_TAX, "Concept", "Which direction does an add-back move the profit?"),
        M(_p6 + "(a) The value of a share after both increases is", F_(12_000), [(F_(15_000), "This is the value before the increases."), (F_(12_000_000), "This is the issue price in thousands, not the share value."),
                                                                                  (F_(10_000), "This is the nominal value.")],
          "Net assets 60 000 000 + 12 000 000 = 72 000 000; shares 4 000 + 1 000 + 1 000 = 6 000; 72 000 000 ÷ 6 000 = 12 000.", T_INCR, "Calculation", "Add the cash to net assets and all shares."),
        M(_p6 + "(b) The fall in the value of an old share is", F_(3_000), [(F_(12_000), "This is the value after the increases."), (F_(15_000), "This is the value before."), (F_(2_000), "This is not derived from the two values.")],
          "15 000 − 12 000 = 3 000.", T_INCR, "Calculation", "Before minus after."),
        M(_p6 + "(c) In the journal, the incorporation of reserves is recorded by", "debiting reserves and crediting share capital",
          [("debiting share capital and crediting reserves", "This reverses the entry."), ("debiting bank and crediting share capital", "No cash is received in a free issue."),
           ("debiting reserves and crediting bank", "No cash leaves in a free issue.")],
          "Reserves become capital: debit reserves, credit share capital (nominal value of the free shares).", T_INCR, "Concept", "Which accounts change in a bonus issue?"),
        M(_p7 + "(a) The legal reserve allocation is", F_(1_200_000), [(F_(2_400_000), "This takes 20% of the profit."), (F_(120_000), "This takes 1% of the profit."), (F_(10_800_000), "This is the profit after the reserve.")],
          "10% × 12 000 000 = 1 200 000.", T_CAPPROP, "Calculation", "One tenth of the profit."),
        M(_p7 + "(b) The allocation to the legal reserve stops being compulsory when the reserve reaches", "one fifth of the share capital",
          [("one tenth of the share capital", "One tenth is the percentage of profit allocated."), ("the whole share capital", "The ceiling is lower."), ("half the share capital", "The ceiling is lower.")],
          "The Uniform Act ceiling is one fifth (20%) of the share capital (check your textbook).", T_CAPPROP, "Recall", "Recall the legal reserve rule."),
        M(_p8 + "(a) A's total share of the profit is", F_(380_000), [(F_(180_000), "This is only A's share of the balance."), (F_(360_000), "This shares the whole profit 3 : 2."), (F_(200_000), "This is only A's interest.")],
          "Interest: A 200 000, B 100 000. Balance 600 000 − 300 000 = 300 000; A takes 3/5 = 180 000. Total 380 000.", T_APPROP, "Calculation", "Deduct interest before sharing the balance."),
        M(_p8 + "(b) A goodwill account is opened when a partner is admitted because", "the new partner pays for a share of the firm's reputation and earning power that is not in the books",
          [("goodwill is a physical asset", "Goodwill is intangible."), ("the new partner's capital must equal the old partners'", "Capitals need not be equal."), ("tax law requires it", "It is an accounting adjustment, not a tax rule.")],
          "Goodwill is the value of the firm above its net assets; the old partners are compensated for their share of it.", T_GOODW, "Concept", "What does goodwill represent?"),
    ]))
assert len(SETS[-1]["questions"]) == 22, len(SETS[-1]["questions"])
