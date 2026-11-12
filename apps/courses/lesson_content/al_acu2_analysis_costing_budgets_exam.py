"""A Level Accounting (0705), Upper Sixth: Financial Statement Analysis; Cost Accounting: Full & Marginal Costing;
Budgetary Control, Standard Costing & Capital Budgeting; and the Examination module (Paper 1, Paper 2, Paper 3).

Draft content for a reviewer to check against the Board's syllabus. Exam facts are only those of the Board's 2023
Advanced Level subject report for 0705: three papers, Paper 1 = 50 compulsory multiple-choice questions (in 2023: 25 on
financial accounting, 10 on cost and management accounting, 15 on company accounting and taxation), Paper 2 = Cost and
Management Accounting (two sections of three questions: answer two from Section A, cost accounting, and all of Section B,
management accounting; 3 hours), Paper 3 = Financial Accounting (Section A financial accounting, four questions, answer
three; Section B company accounting and taxation, three questions, answer two); weighted 30, 30 and 40.

All FCFA figures are invented for practice. Every figure printed in a statement, schedule or worked example below is
computed in this file with exact integer or Fraction arithmetic and checked with assertions, so the printed totals
cannot disagree with the workings. Layouts follow common Cameroonian school practice for the revised SYSCOHADA; where
textbooks differ (sign of variances, 360 or 365 days, ARR base, treatment of some restatements) the lesson says so.
"""

from fractions import Fraction as Fr

from .dsl import *  # noqa: F403

COURSE = ("accounting", "upper-sixth")

M_FSA = "Financial Statement Analysis"
M_COST = "Cost Accounting: Full & Marginal Costing"
M_BUD = "Budgetary Control, Standard Costing & Capital Budgeting"
M_EXAM = "Examination"


# ---------------------------------------------------------------- formatting helpers (all arithmetic is exact)
def n(x):
    """12345 -> '12 345'; whole Fractions print as integers; negatives keep a minus sign."""
    if isinstance(x, Fr):
        assert x.denominator == 1, x
        x = int(x)
    s = f"{abs(x):,}".replace(",", " ")
    return ("-" if x < 0 else "") + s


def r(label, a=None, b=None, w=30, c=12):
    """One aligned statement line with up to two money columns."""
    fa = "" if a is None else (a if isinstance(a, str) else n(a))
    fb = "" if b is None else (b if isinstance(b, str) else n(b))
    return f"{label:<{w}}{fa:>{c}}{fb:>{c}}".rstrip()


def pct(num, den, dp=1):
    """Percentage rounded to dp decimals, as a string."""
    return f"{float(Fr(num) * 100 / Fr(den)):.{dp}f}"


def dec(x, dp=2):
    return f"{float(x):.{dp}f}"


LESSONS = []

# ====================================================================== 1. The functional balance sheet
# Mfoundi Plastics SA (invented). Gross values.
_f_intang, _f_tang, _f_fin = 2_000_000, 38_000_000, 2_000_000
_f_su = _f_intang + _f_tang + _f_fin                       # stable uses
_f_eq, _f_dep, _f_prov, _f_ltd = 20_000_000, 12_000_000, 1_000_000, 14_000_000
_f_sr = _f_eq + _f_dep + _f_prov + _f_ltd                  # stable resources
_f_frng = _f_sr - _f_su
_f_inv, _f_rec, _f_disc, _f_oth = 6_000_000, 7_500_000, 1_000_000, 500_000
_f_tp, _f_tax = 6_000_000, 2_000_000
_f_oa = _f_inv + _f_rec + _f_disc + _f_oth                 # operating current assets (discounted bills added back)
_f_ol = _f_tp + _f_tax
_f_bfre = _f_oa - _f_ol
_f_hao_a, _f_hao_l = 300_000, 800_000
_f_bfhao = _f_hao_a - _f_hao_l
_f_bfr = _f_bfre + _f_bfhao
_f_cash, _f_od = 1_200_000, 1_700_000
_f_tl = _f_od + _f_disc                                    # cash liabilities include the discounted bills
_f_tn = _f_cash - _f_tl
assert (_f_su, _f_sr, _f_frng) == (42_000_000, 47_000_000, 5_000_000)
assert (_f_bfre, _f_bfhao, _f_bfr) == (7_000_000, -500_000, 6_500_000)
assert _f_tn == _f_frng - _f_bfr == -1_500_000
assert _f_su + _f_oa + _f_hao_a + _f_cash == _f_sr + _f_ol + _f_hao_l + _f_tl == 58_500_000
_f_turn = 84_000_000
_f_days = Fr(_f_bfre * 360, _f_turn)
assert _f_days == 30

_t_fbs = "\n".join([
    "Mfoundi Plastics SA - functional balance sheet (FCFA)",
    "USES (gross values)                    RESOURCES",
    r("Stable uses", None, _f_su, w=36),
    r("  intangible fixed assets", _f_intang, w=36),
    r("  tangible fixed assets", _f_tang, w=36),
    r("  financial fixed assets", _f_fin, w=36),
    r("Stable resources", None, _f_sr, w=36),
    r("  equity", _f_eq, w=36),
    r("  depreciation and impairment", _f_dep, w=36),
    r("  provisions for risks and charges", _f_prov, w=36),
    r("  long-term borrowings", _f_ltd, w=36),
    r("Operating current assets", None, _f_oa, w=36),
    r("  inventory", _f_inv, w=36),
    r("  trade receivables", _f_rec, w=36),
    r("  + discounted bills not yet due", _f_disc, w=36),
    r("  other operating receivables", _f_oth, w=36),
    r("Operating current liabilities", None, _f_ol, w=36),
    r("  trade payables", _f_tp, w=36),
    r("  tax and social payables", _f_tax, w=36),
    r("Non-operating (HAO) receivables", None, _f_hao_a, w=36),
    r("Non-operating (HAO) payables", None, _f_hao_l, w=36),
    r("Cash assets (bank, cash)", None, _f_cash, w=36),
    r("Cash liabilities", None, _f_tl, w=36),
    r("  bank overdraft", _f_od, w=36),
    r("  + discounted bills not yet due", _f_disc, w=36),
    r("Total uses = total resources", None, _f_su + _f_oa + _f_hao_a + _f_cash, w=36),
])
_t_fcalc = "\n".join([
    r("Stable resources", _f_sr, w=40),
    r("- Stable uses", -_f_su, w=40),
    r("Net global working capital (FRNG)", None, _f_frng, w=40),
    r("Operating current assets", _f_oa, w=40),
    r("- Operating current liabilities", -_f_ol, w=40),
    r("Operating WCR (BFE)", None, _f_bfre, w=40),
    r("Non-operating assets - liabilities", None, _f_bfhao, w=40),
    r("Total WCR (BFR)", None, _f_bfr, w=40),
    r("Net cash = FRNG - BFR", None, _f_tn, w=40),
    r("Check: cash assets - cash liabilities", None, _f_cash - _f_tl, w=40),
])
# worked example 2 (short data)
_g_frng, _g_bfr = 8_000_000, 5_000_000
_g_tn = _g_frng - _g_bfr
assert _g_tn == 3_000_000

LESSONS.append(lesson(
    module=M_FSA, topic="The functional balance sheet",
    title="The functional balance sheet: working capital, working capital requirement and net cash",
    slug="acu2-functional-balance-sheet", minutes=25,
    summary="Restate the SYSCOHADA balance sheet by function (investment, financing, operating, cash) at gross values, and "
            "calculate net global working capital (FRNG), the working capital requirement (BFR) and net cash (TN).",
    objectives=[
        "Explain why the functional balance sheet uses gross values and groups items by cycle (investment, financing, operating, cash)",
        "Restate a balance sheet: move depreciation to stable resources and add back discounted bills not yet due",
        "Calculate FRNG, operating and non-operating BFR and net cash, and check that FRNG − BFR = net cash",
        "Interpret the three figures and suggest how a firm with negative net cash can improve its position",
    ],
    key_concepts=["Functional balance sheet", "Stable resources", "Stable uses", "Net global working capital (FRNG)",
                  "Working capital requirement (BFR)", "Net cash (TN)", "Discounted bills not yet due"],
    blocks=[
        H("Why restate the balance sheet?"),
        T("A plastics factory in Douala has a profit every year, yet its manager often waits for the bank to approve an overdraft before paying suppliers. "
          "The ordinary SYSCOHADA balance sheet does not explain why. The **functional balance sheet** answers one question: "
          "are long-term needs paid for with long-term money, and how much short-term money does the operating cycle swallow? "
          "All figures in this lesson are **invented for practice**."),
        D("The **functional balance sheet** (bilan fonctionnel) classifies every item by the cycle it belongs to: **investment** (stable uses), "
          "**financing** (stable resources), **operating** (inventory, trade receivables and payables), **non-operating** (HAO items) and **cash**. "
          "Assets are taken at **gross** value, because the firm is studied as a going concern that must finance the whole original cost of its assets.",
          title="Functional balance sheet"),
        KEY("The four blocks", "Each side has the same blocks, so the gaps between them can be measured.",
            cards=[["Stable uses", "Fixed assets at gross value: intangible, tangible and financial."],
                   ["Stable resources", "Equity + accumulated depreciation and impairment of fixed assets + provisions for risks and charges + long-term borrowings."],
                   ["Current (circulating) items", "Operating: inventory, trade receivables, trade and tax/social payables. Non-operating (HAO): e.g. a receivable on the sale of a fixed asset, a debt to a supplier of fixed assets."],
                   ["Cash", "Cash assets (bank, cash in hand) and cash liabilities (overdrafts, short-term bank credit, discounted bills not yet due)."]]),
        H("The three key figures"),
        F(r"\text{FRNG} = \text{stable resources} - \text{stable uses}", title="Net global working capital"),
        F(r"\text{BFR} = (\text{current assets excluding cash}) - (\text{current liabilities excluding cash})", title="Working capital requirement"),
        F(r"\text{TN} = \text{FRNG} - \text{BFR} = \text{cash assets} - \text{cash liabilities}", title="Net cash"),
        T("The reasoning: whatever long-term money is left after paying for fixed assets (FRNG) is available for the operating cycle. "
          "The operating cycle needs money because inventory and customers' debts tie it up for longer than suppliers wait (BFR). "
          "If FRNG covers BFR, cash is positive; if not, the gap is filled by the bank, so net cash is negative. Because the balance sheet balances, "
          "the two ways of calculating net cash must give the same figure: this is your built-in check."),
        IMG("alacu2-functional-balance-sheet.svg",
            alt="Two columns of blocks: stable uses facing stable resources, current assets facing current liabilities, cash assets facing cash liabilities, with arrows marking FRNG, BFR and net cash.",
            caption="Figure 1. The functional balance sheet and the equation FRNG − BFR = TN."),
        H("Restatements before you start"),
        D("**Depreciation and impairment of fixed assets** leave the asset side (assets go back to gross) and join stable resources: they are profits kept in the business. "
          "**Discounted bills not yet due** (effets escomptés non échus) are added back to trade receivables (the customer has not yet paid) and to cash liabilities "
          "(the bank has advanced the money and can claim it back if the customer defaults).", title="Two restatements you must always make"),
        T("Some textbooks also restate leased assets (crédit-bail): the asset's value is added to stable uses, the accumulated depreciation it would have had "
          "to stable resources and the capital still owed to long-term debt. Others treat impairment of current assets differently. Follow your textbook and your teacher on these points."),
        EX("Worked example 1: Mfoundi Plastics SA",
           intro="Gross fixed assets: intangible 2 000 000, tangible 38 000 000, financial 2 000 000. Equity 20 000 000; accumulated depreciation 12 000 000; provisions for risks 1 000 000; "
                 "long-term loans 14 000 000. Inventory 6 000 000; trade receivables 7 500 000; discounted bills not yet due 1 000 000; other operating receivables 500 000. "
                 "Trade payables 6 000 000; tax and social payables 2 000 000. HAO receivable 300 000; HAO payable 800 000. Bank 1 200 000; overdraft 1 700 000. "
                 "Prepare the functional balance sheet and calculate FRNG, BFR and net cash.",
           steps=[
               S("Stable uses", text="2 000 000 + 38 000 000 + 2 000 000 = 42 000 000."),
               S("Stable resources", text="20 000 000 + 12 000 000 + 1 000 000 + 14 000 000 = 47 000 000."),
               S("FRNG", text="47 000 000 − 42 000 000 = 5 000 000 (positive: fixed assets are fully financed by stable resources)."),
               S("Operating BFR", text="Operating assets 6 000 000 + 7 500 000 + 1 000 000 + 500 000 = 15 000 000; operating liabilities 8 000 000; BFE = 7 000 000."),
               S("Non-operating BFR", text="300 000 − 800 000 = −500 000 (a resource)."),
               S("Total BFR and net cash", text="BFR = 7 000 000 − 500 000 = 6 500 000. TN = 5 000 000 − 6 500 000 = −1 500 000."),
               S("Check", text="Cash assets 1 200 000 − cash liabilities (1 700 000 + 1 000 000) = −1 500 000. Both methods agree."),
           ]),
        CODE(_t_fbs, "text", title="Functional balance sheet (invented for practice)"),
        CODE(_t_fcalc, "text", title="The three key figures"),
        H("Interpreting the figures"),
        T("Mfoundi's FRNG is positive, so the rule of **financial equilibrium** (stable uses financed by stable resources) is respected. But the operating cycle needs 6 500 000 and "
          "the FRNG gives only 5 000 000. The gap of 1 500 000 is borrowed from the bank at short notice. This explains the manager's daily worry: the firm depends on overdrafts and discounting."),
        T("The operating BFR is often expressed in **days of turnover excluding VAT**: BFE ÷ turnover × 360. With a turnover of 84 000 000, "
          "7 000 000 ÷ 84 000 000 × 360 = 30 days. Comparing this figure year by year shows whether the operating cycle is becoming heavier."),
        KEY("Ways to improve negative net cash", "Act on either side of the equation TN = FRNG − BFR.",
            cards=[["Raise FRNG", "New share capital, retained profits, a long-term loan, sale of unused fixed assets."],
                   ["Reduce BFR", "Lower inventory, collect from customers faster, negotiate longer supplier credit."],
                   ["Limits", "A long-term loan adds interest; squeezing suppliers or customers can damage relationships and sales."]]),
        EX("Worked example 2: reading the result",
           intro="A firm has FRNG 8 000 000 and BFR 5 000 000. Find the net cash and comment.",
           steps=[
               S("Net cash", text="TN = 8 000 000 − 5 000 000 = 3 000 000."),
               S("Comment", text="Positive net cash: the firm finances its operating cycle with stable resources and has cash left. "
                                 "If the surplus is very large and stays idle, it may be better invested, so a large positive TN is not always good news."),
           ]),
        MISTAKE("Using net values for fixed assets",
                "In the functional balance sheet fixed assets are at **gross** value and accumulated depreciation goes to stable resources. Using net values gives the financial (liquidity) approach, which is a different tool."),
        MISTAKE("Forgetting the discounted bills",
                "Add discounted bills not yet due to **both** trade receivables and cash liabilities. If you add them to one side only, the balance sheet will not balance and BFR and TN will both be wrong."),
        MISTAKE("Mixing operating and non-operating items",
                "A debt to a supplier of fixed assets or a receivable on the sale of a fixed asset is **HAO** (non-operating). Keep it out of the operating BFR, which measures the trading cycle only."),
        QUIZ("A firm has stable resources of 60 000 000, stable uses of 52 000 000 and a BFR of 10 000 000. Its net cash is",
             ["+18 000 000", "+8 000 000", "−2 000 000", "−10 000 000"], 2,
             "FRNG = 60 000 000 − 52 000 000 = 8 000 000; TN = 8 000 000 − 10 000 000 = −2 000 000.",
             hint="Find FRNG first, then subtract BFR.",
             feedback=["This adds BFR to FRNG instead of subtracting it.", "This is FRNG, not net cash.", "",
                       "This takes BFR as the net cash and forgets FRNG."]),
        QUIZ("Discounted bills not yet due of 2 000 000 are restated. Which pair of changes is correct?",
             ["Trade receivables +2 000 000 and cash liabilities +2 000 000", "Trade receivables −2 000 000 and cash assets +2 000 000",
              "Stable resources +2 000 000 and stable uses +2 000 000", "No change: the bills have already been paid by the bank"], 0,
             "The customer still owes the bill, and the bank can claim the money back if the customer does not pay, so it is short-term bank finance.",
             feedback=["", "This reverses the restatement: the bills must be added back, not removed.",
                       "Discounting is short-term finance; it does not belong to the stable blocks.",
                       "The bank advanced the money, but the risk stays with the firm until the bill falls due."], title="Quick check 2"),
        TIP("Balance-sheet analysis is part of Financial Accounting, so it is examined in Paper 3, and short calculations of FRNG, BFR or net cash can appear in Paper 1. "
            "Always show the two calculations of net cash: the agreement is your proof.", title="Exam link"),
        PQ("Stable resources 35 000 000; gross fixed assets 30 000 000; inventory 4 000 000; trade receivables 5 000 000; trade payables 3 500 000; bank 500 000; overdraft 1 000 000. "
           "Calculate FRNG, BFR and net cash, and check.",
           "FRNG = 35 000 000 − 30 000 000 = 5 000 000. BFR = 4 000 000 + 5 000 000 − 3 500 000 = 5 500 000. TN = 5 000 000 − 5 500 000 = −500 000. "
           "Check: cash assets 500 000 − cash liabilities 1 000 000 = −500 000. Totals: uses 30 000 000 + 9 000 000 + 500 000 = 39 500 000 = resources 35 000 000 + 3 500 000 + 1 000 000."),
        PQ("Explain why accumulated depreciation is treated as a stable resource in the functional balance sheet.",
           "Depreciation is a charge that reduces profit without any cash payment, so the amount stays in the business. It is a resource kept for the long term (to renew the assets), "
           "and assets are shown at gross value, so the depreciation must appear on the resources side."),
        PQ("A firm's operating BFR is 9 000 000 and its turnover excluding VAT is 108 000 000. Express the BFR in days of turnover (360-day year) and comment if last year's figure was 24 days.",
           "9 000 000 ÷ 108 000 000 × 360 = 30 days. The operating cycle now ties up six more days of sales: check inventory levels and customer credit."),
        PQ("Give two ways of improving negative net cash and one limitation of each.",
           "Raise a long-term loan (adds interest and repayments); reduce inventory (risk of stock-outs and lost sales); collect from customers faster (customers may go to competitors)."),
        SUM("The functional balance sheet groups items by cycle and uses gross values; depreciation and provisions join stable resources.",
            "FRNG = stable resources − stable uses; BFR = current assets excluding cash − current liabilities excluding cash.",
            "Net cash = FRNG − BFR = cash assets − cash liabilities: use both as a check.",
            "Add discounted bills not yet due to receivables and to cash liabilities.",
            "Interpret: positive FRNG respects financial equilibrium; TN shows whether the operating cycle is covered."),
    ]))

# ====================================================================== 2. The financial balance sheet
# Kribi Foods SA (invented). Accounting balance sheet at net values.
_k_bld, _k_bld_mv, _k_eqp, _k_nva, _k_dep, _k_dep_st = 20_000_000, 24_000_000, 10_000_000, 1_000_000, 2_000_000, 500_000
_k_inv, _k_safety, _k_rec, _k_rec_lt, _k_cash = 6_000_000, 1_500_000, 5_000_000, 800_000, 1_000_000
_k_cap, _k_res, _k_prof, _k_div = 20_000_000, 2_000_000, 3_000_000, 1_200_000
_k_loan, _k_loan_st, _k_tp, _k_od = 15_000_000, 3_000_000, 4_500_000, 500_000
_k_acc_assets = _k_bld + _k_eqp + _k_nva + _k_dep + _k_inv + _k_rec + _k_cash
_k_acc_liab = _k_cap + _k_res + _k_prof + _k_loan + _k_tp + _k_od
assert _k_acc_assets == _k_acc_liab == 45_000_000
_k_gain = _k_bld_mv - _k_bld
_k_fa = _k_bld_mv + _k_eqp + (_k_dep - _k_dep_st) + _k_safety + _k_rec_lt
_k_ca_inv = _k_inv - _k_safety
_k_ca_rec = _k_rec - _k_rec_lt + _k_dep_st
_k_ca = _k_ca_inv + _k_ca_rec + _k_cash
_k_eq = _k_cap + _k_res + _k_prof - _k_div + _k_gain - _k_nva
_k_lt = _k_loan - _k_loan_st
_k_st = _k_loan_st + _k_div + _k_tp + _k_od
assert (_k_fa, _k_ca, _k_fa + _k_ca) == (37_800_000, 10_200_000, 48_000_000)
assert (_k_eq, _k_lt, _k_st, _k_eq + _k_lt + _k_st) == (26_800_000, 12_000_000, 9_200_000, 48_000_000)
_k_fwc = _k_eq + _k_lt - _k_fa
assert _k_fwc == _k_ca - _k_st == 1_000_000
_k_shares = _k_cap // 10_000
_k_vm = Fr(_k_eq, _k_shares)
assert _k_shares == 2_000 and _k_vm == 13_400
_k_cr = Fr(_k_ca, _k_st)
_k_solv = Fr(_k_fa + _k_ca, _k_lt + _k_st)
_k_auto = Fr(_k_eq, _k_lt + _k_st)
assert (dec(_k_cr), dec(_k_solv), dec(_k_auto)) == ("1.11", "2.26", "1.26")

_t_kacc = "\n".join([
    "Kribi Foods SA - balance sheet at net values (FCFA)",
    r("Buildings (market value 24 000 000)", _k_bld, w=40),
    r("Equipment", _k_eqp, w=40),
    r("Intangible with no resale value", _k_nva, w=40),
    r("Deposits (500 000 back within 1 year)", _k_dep, w=40),
    r("Inventory (1 500 000 safety stock)", _k_inv, w=40),
    r("Receivables (800 000 due after 1 year)", _k_rec, w=40),
    r("Bank and cash", _k_cash, w=40),
    r("Total assets", None, _k_acc_assets, w=40),
    r("Share capital (2 000 shares x 10 000)", _k_cap, w=40),
    r("Reserves", _k_res, w=40),
    r("Profit (1 200 000 to be paid as dividend)", _k_prof, w=40),
    r("Bank loan (3 000 000 due within 1 year)", _k_loan, w=40),
    r("Trade payables", _k_tp, w=40),
    r("Bank overdraft", _k_od, w=40),
    r("Total equity and liabilities", None, _k_acc_liab, w=40),
])
_t_kfin = "\n".join([
    "Kribi Foods SA - financial balance sheet (FCFA)",
    "ASSETS",
    r("More than one year", None, _k_fa, w=40),
    r("  buildings at market value", _k_bld_mv, w=40),
    r("  equipment", _k_eqp, w=40),
    r("  deposits (long part)", _k_dep - _k_dep_st, w=40),
    r("  safety stock", _k_safety, w=40),
    r("  receivables due after 1 year", _k_rec_lt, w=40),
    r("Less than one year", None, _k_ca, w=40),
    r("  inventory (rest)", _k_ca_inv, w=40),
    r("  receivables + short deposit", _k_ca_rec, w=40),
    r("  bank and cash", _k_cash, w=40),
    r("Total", None, _k_fa + _k_ca, w=40),
    "EQUITY AND LIABILITIES",
    r("Adjusted equity (net assets)", None, _k_eq, w=40),
    r("  capital + reserves + profit", _k_cap + _k_res + _k_prof, w=40),
    r("  - dividend to be paid", -_k_div, w=40),
    r("  + unrealised gain on buildings", _k_gain, w=40),
    r("  - non-value asset", -_k_nva, w=40),
    r("Long-term debts (more than 1 year)", None, _k_lt, w=40),
    r("Short-term debts (less than 1 year)", None, _k_st, w=40),
    r("  loan instalment due", _k_loan_st, w=40),
    r("  dividend payable", _k_div, w=40),
    r("  trade payables", _k_tp, w=40),
    r("  bank overdraft", _k_od, w=40),
    r("Total", None, _k_eq + _k_lt + _k_st, w=40),
])
# worked example 2
_k2_perm, _k2_fa, _k2_ca, _k2_st = 30_000_000, 26_000_000, 9_000_000, 5_000_000
assert _k2_perm - _k2_fa == _k2_ca - _k2_st == 4_000_000 and Fr(_k2_ca, _k2_st) == Fr(9, 5)

LESSONS.append(lesson(
    module=M_FSA, topic="The financial balance sheet",
    title="The financial (liquidity) balance sheet: restatements, net assets and solvency",
    slug="acu2-financial-balance-sheet", minutes=25,
    summary="Rebuild the balance sheet by liquidity and maturity (more or less than one year) at realistic values, find the adjusted "
            "net assets and the financial working capital, and judge the firm's liquidity and solvency.",
    objectives=[
        "Explain how the financial balance sheet differs from the functional balance sheet (purpose, values, classification)",
        "Make the usual restatements: market values, non-value assets, dividends to be paid, parts due within one year, safety stock",
        "Calculate adjusted net assets, financial working capital and the net asset value of a share",
        "Calculate and interpret the current, solvency and financial autonomy ratios",
    ],
    key_concepts=["Financial balance sheet", "Liquidity", "Maturity", "Adjusted net assets", "Non-value asset",
                  "Financial working capital", "Solvency"],
    blocks=[
        H("A banker's view of the balance sheet"),
        T("A bank in Kribi is asked to lend to a food-processing company. The banker's question is not how the company organises its cycles, "
          "but: if things go wrong, can it pay its debts as they fall due, and what would really be left for the shareholders? "
          "The **financial balance sheet** answers that question. All figures are **invented for practice**."),
        D("The **financial balance sheet** (bilan financier or bilan liquidité) classifies assets by **liquidity** (how soon they become cash) "
          "and liabilities by **maturity** (how soon they must be paid), using the **one-year** line. Values are **net** and, where the question gives them, **realistic (market) values**.",
          title="Financial balance sheet"),
        KEY("Functional or financial?", "Two tools, two questions.",
            cards=[["Functional", "Gross values, grouped by cycle. Question: how are the activities financed? Users: managers."],
                   ["Financial", "Net or market values, grouped by one-year liquidity and maturity. Question: is the firm solvent and liquid? Users: lenders, shareholders, buyers of the business."]]),
        H("The usual restatements"),
        KEY("Move items across the one-year line or change their value", "Each restatement keeps the balance sheet in balance.",
            cards=[["Market values", "Replace book value by market value; the unrealised gain (or loss) is added to (or deducted from) equity."],
                   ["Non-value assets", "Items that cannot be sold or turned into cash are removed and deducted from equity (textbooks call them non-value or fictitious assets)."],
                   ["Dividend to be paid", "Leave equity and become a short-term debt."],
                   ["Long-term debt due within a year", "That part moves to short-term debts."],
                   ["Safety stock", "The permanent minimum inventory is treated as an asset of more than one year."],
                   ["Receivables or deposits", "The part due after a year moves up; the part recoverable within a year moves down."]]),
        T("Some textbooks also deduct a deferred tax charge from an unrealised gain, or treat part of the profit as tax payable. Follow your textbook's treatment and say what you assumed."),
        H("Results you calculate"),
        F(r"\text{FWC} = (\text{equity} + \text{LT debts}) - \text{assets} > 1\text{ yr} = \text{assets} < 1\text{ yr} - \text{ST debts}",
          title="Financial working capital (FWC)"),
        F(r"\text{Adjusted net assets} = \text{total real assets} - \text{total debts}", title="Net assets (actif net)"),
        F(r"\text{Current ratio} = \frac{\text{assets under one year}}{\text{debts under one year}} \qquad \text{Solvency ratio} = \frac{\text{total assets}}{\text{total debts}}",
          title="Liquidity and solvency"),
        EX("Worked example 1: Kribi Foods SA",
           intro="Use the accounting balance sheet below and the notes in brackets. Prepare the financial balance sheet, then calculate the financial working capital, "
                 "the net asset value per share and the three ratios.",
           steps=[
               S("Assets over one year", text="Buildings at market value 24 000 000 + equipment 10 000 000 + long deposit 1 500 000 + safety stock 1 500 000 + long receivables 800 000 = 37 800 000. "
                                             "The intangible with no resale value is removed."),
               S("Assets under one year", text="Inventory 4 500 000 + receivables 4 200 000 + short deposit 500 000 + cash 1 000 000 = 10 200 000. Total assets 48 000 000."),
               S("Adjusted equity", text="25 000 000 − dividend 1 200 000 + gain 4 000 000 − non-value asset 1 000 000 = 26 800 000."),
               S("Debts", text="Long-term 15 000 000 − 3 000 000 = 12 000 000. Short-term 3 000 000 + 1 200 000 + 4 500 000 + 500 000 = 9 200 000. Total 48 000 000: balanced."),
               S("Financial working capital", text="(26 800 000 + 12 000 000) − 37 800 000 = 1 000 000 = 10 200 000 − 9 200 000."),
               S("Net asset value per share", text="26 800 000 ÷ 2 000 shares = 13 400 per share (nominal value 10 000)."),
               S("Ratios", text="Current ratio 10 200 000 ÷ 9 200 000 = 1.11; solvency 48 000 000 ÷ 21 200 000 = 2.26; autonomy (equity ÷ total debts) 26 800 000 ÷ 21 200 000 = 1.26."),
           ]),
        CODE(_t_kacc, "text", title="Accounting balance sheet (invented for practice)"),
        CODE(_t_kfin, "text", title="Financial balance sheet after restatement"),
        H("Interpreting the results"),
        T("Kribi Foods is **solvent**: its real assets are 2.26 times its debts, so creditors are well covered. Its **liquidity** is thin: assets that become cash within a year "
          "exceed debts due within a year by only 1 000 000 (current ratio 1.11). A delay in collecting from customers could cause a cash problem even though the business is sound."),
        T("The **net asset value per share** (often called the mathematical value of a share) of 13 400 is above the nominal value of 10 000, because the company has kept reserves and its buildings have gained value. "
          "This figure is used when shares are valued, when a partner or shareholder leaves, and when capital is increased (see the company accounting lessons)."),
        EX("Worked example 2: the two calculations agree",
           intro="Equity + long-term debts 30 000 000; assets over one year 26 000 000; assets under one year 9 000 000; short-term debts 5 000 000. Find the financial working capital and the current ratio.",
           steps=[
               S("From the top", text="30 000 000 − 26 000 000 = 4 000 000."),
               S("From the bottom", text="9 000 000 − 5 000 000 = 4 000 000."),
               S("Current ratio", text="9 000 000 ÷ 5 000 000 = 1.8: assets due within a year cover short-term debts 1.8 times."),
           ]),
        MISTAKE("Leaving the dividend in equity",
                "A dividend already decided is money the company owes to shareholders within a few months. Take it out of equity and put it in short-term debts."),
        MISTAKE("Forgetting to split items across the one-year line",
                "Read every note: the part of a loan due within the year, the long part of a receivable, the safety stock. Each changes the working capital and the ratios."),
        MISTAKE("Mixing the two balance sheets",
                "Gross values and depreciation in resources belong to the functional balance sheet. In the financial balance sheet use net or market values and do not add depreciation to equity."),
        QUIZ("Book value of land FCFA 8 000 000; market value FCFA 11 000 000. In the financial balance sheet",
             ["land is shown at 11 000 000 and equity rises by 3 000 000", "land stays at 8 000 000 and a note is added",
              "land is shown at 11 000 000 and short-term debts rise by 3 000 000", "land is shown at 3 000 000"], 0,
             "The asset is restated at market value, and the unrealised gain of 3 000 000 belongs to the shareholders, so it is added to equity.",
             hint="Where does the gain go so that the balance sheet still balances?",
             feedback=["", "The financial balance sheet uses realistic values when they are given.",
                       "The gain is not a debt; nobody must be paid.", "3 000 000 is the gain, not the value of the land."]),
        QUIZ("A loan of FCFA 9 000 000 includes FCFA 2 000 000 repayable within twelve months. In the financial balance sheet",
             ["9 000 000 stays in long-term debts", "7 000 000 in long-term debts and 2 000 000 in short-term debts",
              "2 000 000 in long-term debts and 7 000 000 in short-term debts", "the whole loan becomes short-term"], 1,
             "Only the instalment due within a year moves below the one-year line.",
             feedback=["The 2 000 000 instalment is due within a year.", "", "This reverses the two parts.",
                       "Only the part due within a year is short-term."], title="Quick check 2"),
        TIP("Financial balance sheets and net asset values belong to Financial Accounting (Paper 3), and they support share valuation, which the Board's 2023 report says few candidates handled well. "
            "Lay out both sides, show each restatement and prove that the totals agree.", title="Exam link"),
        PQ("Equity per books FCFA 40 000 000 includes a profit of which FCFA 5 000 000 is to be paid as dividend. Land is worth FCFA 6 000 000 more than its book value, "
           "and there is a non-value asset of FCFA 2 000 000. Calculate adjusted net assets.",
           "40 000 000 − 5 000 000 + 6 000 000 − 2 000 000 = 39 000 000."),
        PQ("Adjusted net assets are FCFA 39 000 000 and the capital is made up of 3 000 shares of FCFA 10 000. Find the net asset value of one share and comment.",
           "39 000 000 ÷ 3 000 = 13 000 per share, above the nominal value of 10 000 because of reserves and the gain on land."),
        PQ("Assets under one year FCFA 12 000 000; debts under one year FCFA 15 000 000. Calculate the financial working capital and the current ratio, and comment.",
           "Working capital = 12 000 000 − 15 000 000 = −3 000 000; current ratio = 0.8. Short-term debts are not covered by short-term assets: a liquidity risk."),
        PQ("Give two differences between the functional and the financial balance sheet.",
           "Values: gross (functional) against net or market (financial). Classification: by cycle (functional) against by liquidity and maturity around one year (financial). "
           "Purpose: financing of activities for managers against solvency and liquidity for lenders and shareholders."),
        SUM("The financial balance sheet ranks assets by liquidity and liabilities by maturity around one year, at net or market values.",
            "Restate: market values (gain to equity), remove non-value assets, move dividends and debt due within a year to short-term debts, move safety stock and long receivables up.",
            "Financial working capital = permanent capital − assets over one year = assets under one year − short-term debts.",
            "Adjusted net assets ÷ number of shares = net asset value of a share.",
            "Solvency compares total assets with total debts; liquidity compares the short-term blocks."),
    ]))

# ====================================================================== 3. Ratio analysis
# Sanaga Traders SA (invented)
_r_s, _r_cos, _r_opx, _r_int = 120_000_000, 84_000_000, 24_000_000, 2_000_000
_r_gp = _r_s - _r_cos
_r_pbit = _r_gp - _r_opx
_r_pbt = _r_pbit - _r_int
_r_tax = _r_pbt * 30 // 100            # teaching rate only
_r_np = _r_pbt - _r_tax
assert (_r_gp, _r_pbit, _r_pbt, _r_tax, _r_np) == (36_000_000, 12_000_000, 10_000_000, 3_000_000, 7_000_000)
_r_nca, _r_inv, _r_inv0, _r_rec, _r_cash = 50_000_000, 14_000_000, 10_000_000, 15_000_000, 3_000_000
_r_tp, _r_ocl, _r_eq, _r_ltd = 10_500_000, 1_500_000, 50_000_000, 20_000_000
_r_cl = _r_tp + _r_ocl
_r_ca = _r_inv + _r_rec + _r_cash
assert _r_nca + _r_ca == _r_eq + _r_ltd + _r_cl == 82_000_000
_r_ce = _r_eq + _r_ltd
_r_purch = _r_cos + _r_inv - _r_inv0
_r_avg = Fr(_r_inv + _r_inv0, 2)
R = {
    "gpm": pct(_r_gp, _r_s), "npm": pct(_r_np, _r_s, 2), "roce": pct(_r_pbit, _r_ce, 2), "roe": pct(_r_np, _r_eq),
    "cr": dec(Fr(_r_ca, _r_cl)), "qr": dec(Fr(_r_ca - _r_inv, _r_cl)), "cash": dec(Fr(_r_cash, _r_cl)),
    "it": dec(Fr(_r_cos) / _r_avg, 1), "idays": dec(360 * _r_avg / _r_cos, 1), "rdays": dec(Fr(_r_rec * 360, _r_s), 1),
    "pdays": dec(Fr(_r_tp * 360, _r_purch), 1), "gear": pct(_r_ltd, _r_ce), "de": pct(_r_ltd, _r_eq),
    "icov": dec(Fr(_r_pbit, _r_int), 1), "at": dec(Fr(_r_s, _r_ce)),
}
assert R == {"gpm": "30.0", "npm": "5.83", "roce": "17.14", "roe": "14.0", "cr": "2.67", "qr": "1.50", "cash": "0.25",
             "it": "7.0", "idays": "51.4", "rdays": "45.0", "pdays": "43.0", "gear": "28.6", "de": "40.0", "icov": "6.0",
             "at": "1.71"}, R
assert _r_purch == 88_000_000

_t_rdata = "\n".join([
    "Sanaga Traders SA - extracts for the year (FCFA)",
    r("Sales (all on credit)", _r_s, w=36),
    r("Cost of sales", _r_cos, w=36),
    r("Gross profit", _r_gp, w=36),
    r("Operating expenses", _r_opx, w=36),
    r("Profit before interest and tax", _r_pbit, w=36),
    r("Interest", _r_int, w=36),
    r("Profit before tax", _r_pbt, w=36),
    r("Tax (30%, teaching rate)", _r_tax, w=36),
    r("Profit after tax", _r_np, w=36),
    "",
    r("Non-current assets", _r_nca, w=36),
    r("Inventory (opening 10 000 000)", _r_inv, w=36),
    r("Trade receivables", _r_rec, w=36),
    r("Bank and cash", _r_cash, w=36),
    r("Equity", _r_eq, w=36),
    r("Long-term loan", _r_ltd, w=36),
    r("Trade payables", _r_tp, w=36),
    r("Other current liabilities", _r_ocl, w=36),
])
_t_rres = "\n".join([
    "Ratio                      Working                   Result",
    f"Gross margin               36.0 / 120.0             {R['gpm']}%",
    f"Net margin (after tax)      7.0 / 120.0             {R['npm']}%",
    f"ROCE                       12.0 / (50.0 + 20.0)     {R['roce']}%",
    f"Return on equity            7.0 / 50.0              {R['roe']}%",
    f"Current ratio              32.0 / 12.0              {R['cr']}",
    f"Quick (acid test) ratio    (32.0 - 14.0) / 12.0     {R['qr']}",
    f"Inventory turnover         84.0 / 12.0              {R['it']} times",
    f"Inventory days             360 / 7                  {R['idays']} days",
    f"Receivables days           15.0 / 120.0 x 360       {R['rdays']} days",
    f"Payables days              10.5 / 88.0 x 360        {R['pdays']} days",
    f"Gearing                    20.0 / 70.0              {R['gear']}%",
    f"Interest cover             12.0 / 2.0               {R['icov']} times",
    "(figures in millions of FCFA)",
])
_t_r2 = "\n".join([
    "Ratio                 Year 1    Year 2",
    "Gross margin %          32.0      30.0",
    "Current ratio           1.90      2.67",
    "Quick ratio             1.20      1.50",
    "Inventory days          40.0      51.4",
    "Receivables days        38.0      45.0",
])

LESSONS.append(lesson(
    module=M_FSA, topic="Ratio analysis",
    title="Ratio analysis: profitability, liquidity, efficiency and capital structure",
    slug="acu2-ratio-analysis", minutes=25,
    summary="Calculate the main profitability, liquidity, efficiency and capital-structure ratios from a set of accounts, and write "
            "a balanced interpretation that compares, explains causes and states the limits of ratios.",
    objectives=[
        "Calculate gross and net margin, ROCE and return on equity",
        "Calculate the current, quick and cash ratios and the inventory, receivables and payables periods",
        "Calculate gearing and interest cover and explain the risk they measure",
        "Interpret ratios by comparison over time or with another firm, and state the limitations of ratio analysis",
    ],
    key_concepts=["Profitability ratios", "Liquidity ratios", "Efficiency (activity) ratios", "Gearing", "Interest cover",
                  "Return on capital employed (ROCE)", "Limitations of ratios"],
    blocks=[
        H("Why ratios?"),
        T("Two traders in Edéa each made a profit of FCFA 7 000 000. One used FCFA 70 000 000 of capital, the other FCFA 20 000 000. Who did better? "
          "Absolute figures cannot answer; a **ratio** relates one figure to another so that firms of different size, or one firm in different years, can be compared. "
          "All figures are **invented for practice**."),
        D("A **ratio** expresses the relationship between two related figures in the accounts, as a percentage, a number of times or a number of days. "
          "On its own a ratio means little; it becomes useful when **compared** with the previous year, with a similar firm, with the industry or with a target.",
          title="Ratio"),
        KEY("Four families of ratios", "The Board's 2023 report lists profitability, liquidity, efficiency and capital structure ratios as what candidates were asked to determine.",
            cards=[["Profitability", "Gross margin = gross profit ÷ sales; net margin = net profit ÷ sales; ROCE = profit before interest and tax ÷ capital employed; return on equity = profit after tax ÷ equity."],
                   ["Liquidity", "Current ratio = current assets ÷ current liabilities; quick ratio = (current assets − inventory) ÷ current liabilities; cash ratio = cash ÷ current liabilities."],
                   ["Efficiency", "Inventory turnover = cost of sales ÷ average inventory; receivables days = receivables ÷ credit sales × 360; payables days = payables ÷ credit purchases × 360; asset turnover = sales ÷ capital employed."],
                   ["Capital structure", "Gearing = long-term debt ÷ (equity + long-term debt); debt to equity = long-term debt ÷ equity; interest cover = profit before interest and tax ÷ interest."]]),
        T("Definitions vary between textbooks: some use 365 days, some measure receivables including VAT against sales including VAT, some define capital employed as total assets less current liabilities "
          "(which here gives the same 70 000 000). Use your textbook's definitions, state the formula in the answer, and be consistent from year to year."),
        EX("Worked example 1: Sanaga Traders SA",
           intro="Using the extracts below, calculate the main ratios of the four families (360-day year).",
           steps=[
               S("Profitability", text=f"Gross margin = 36 000 000 ÷ 120 000 000 = {R['gpm']}%; net margin = 7 000 000 ÷ 120 000 000 = {R['npm']}%; "
                                       f"ROCE = 12 000 000 ÷ 70 000 000 = {R['roce']}%; return on equity = 7 000 000 ÷ 50 000 000 = {R['roe']}%."),
               S("Liquidity", text=f"Current assets = 14 + 15 + 3 = 32 million; current liabilities = 12 million. Current ratio {R['cr']}; quick ratio {R['qr']}; cash ratio {R['cash']}."),
               S("Inventory", text=f"Average inventory = (10 + 14) ÷ 2 = 12 million. Turnover = 84 ÷ 12 = {R['it']} times, about {R['idays']} days."),
               S("Receivables and payables", text=f"Receivables days = 15 ÷ 120 × 360 = {R['rdays']} days. Credit purchases = cost of sales + closing − opening inventory = 84 + 14 − 10 = 88 million; "
                                                  f"payables days = 10.5 ÷ 88 × 360 = {R['pdays']} days."),
               S("Capital structure", text=f"Gearing = 20 ÷ 70 = {R['gear']}%; debt to equity {R['de']}%; interest cover = 12 ÷ 2 = {R['icov']} times."),
           ]),
        CODE(_t_rdata, "text", title="Extracts (invented for practice)"),
        CODE(_t_rres, "text", title="Ratio results"),
        H("From numbers to interpretation"),
        T("An examiner rewards interpretation more than arithmetic. For each family, state the ratio, **compare** it (with last year, a competitor or a norm), "
          "give a likely **cause** from the data, and say what it means for a **user** (manager, lender, shareholder)."),
        EX("Worked example 2: comparing two years",
           intro="The table below compares Sanaga Traders' ratios with the previous year. Interpret the movements.",
           steps=[
               S("Profitability", text="Gross margin fell from 32.0% to 30.0%: selling prices may have been cut to win customers, or purchase costs rose without a price increase."),
               S("Liquidity", text="The current ratio rose from 1.90 to 2.67. This looks safer, but look at what drives it."),
               S("Efficiency explains liquidity", text="Inventory days rose from 40 to 51.4 and receivables days from 38 to 45. More money is tied up in stock and in customers' debts, "
                                                      "which inflates current assets. The 'better' liquidity is partly a sign of weaker control of working capital."),
               S("Conclusion", text="Advise the managers to review pricing and purchasing, reduce slow-moving stock and tighten credit control; a lender would note the adequate interest cover of 6 times."),
           ]),
        CODE(_t_r2, "text", title="Year-on-year comparison (invented for practice)"),
        KEY("Limits of ratio analysis", "Mention these in an evaluation.",
            cards=[["Historical data", "Ratios describe the past year; conditions may have changed."],
                   ["One date", "The balance sheet is a snapshot and may be window-dressed at the year end."],
                   ["Different policies", "Depreciation, inventory valuation and definitions differ between firms, so comparisons can mislead."],
                   ["Inflation and non-financial factors", "Price changes distort comparisons over time; ratios ignore staff skills, reputation and market conditions."]]),
        MISTAKE("Giving the ratio without the formula and the working",
                "Write the formula, substitute the figures, then the answer with its unit (% , times, days). A wrong answer with a correct method still earns credit."),
        MISTAKE("Saying 'higher is always better'",
                "A very high current ratio may mean idle cash or excessive stock; very long payables days may damage supplier relations. Judge each ratio in context."),
        MISTAKE("Using sales instead of cost of sales for inventory turnover",
                "Inventory is valued at cost, so compare it with cost of sales, and use average inventory when the opening figure is given."),
        QUIZ("Current assets FCFA 18 000 000 including inventory FCFA 6 000 000; current liabilities FCFA 8 000 000. The quick ratio is",
             ["2.25", "1.50", "0.75", "3.00"], 1,
             "(18 000 000 − 6 000 000) ÷ 8 000 000 = 1.50.",
             hint="Remove inventory from current assets first.",
             feedback=["This is the current ratio: inventory was not removed.", "", "This uses inventory alone over current liabilities.",
                       "This divides current assets by inventory."]),
        QUIZ("A firm's gearing rises from 20% to 55% after a large bank loan. Which consequence is most likely?",
             ["Shareholders face more risk because interest must be paid even when profit falls", "The firm no longer pays any interest",
              "Liquidity automatically improves every year", "Return on equity must fall"], 0,
             "High gearing means fixed interest commitments; profit after interest becomes more volatile for shareholders.",
             feedback=["", "More debt means more interest, not less.", "The loan may bring cash at first, but repayments and interest reduce cash later.",
                       "If the borrowed money earns more than its interest cost, return on equity can rise."], title="Quick check 2"),
        TIP("Ratio analysis is a Financial Accounting topic for Paper 3; the Board's 2023 report notes a question asking for profitability, liquidity, efficiency and capital-structure ratios. "
            "Short ratio calculations are also natural Paper 1 items. Learn one clear formula for each ratio and practise writing two-sentence interpretations.", title="Exam link"),
        PQ("Sales FCFA 80 000 000; gross profit FCFA 20 000 000; profit before interest and tax FCFA 9 600 000; equity FCFA 40 000 000; long-term loans FCFA 8 000 000. "
           "Calculate the gross margin, ROCE and gearing.",
           "Gross margin = 20 ÷ 80 = 25%. Capital employed = 48 000 000; ROCE = 9 600 000 ÷ 48 000 000 = 20%. Gearing = 8 ÷ 48 = 16.7%."),
        PQ("Cost of sales FCFA 60 000 000; opening inventory FCFA 9 000 000; closing inventory FCFA 11 000 000. Calculate inventory turnover and the inventory period (360 days).",
           "Average inventory = 10 000 000. Turnover = 60 ÷ 10 = 6 times; period = 360 ÷ 6 = 60 days."),
        PQ("Trade receivables FCFA 12 000 000; credit sales FCFA 96 000 000. Calculate receivables days and comment if the firm allows customers 30 days.",
           "12 ÷ 96 × 360 = 45 days. Customers take 15 days longer than allowed: credit control needs tightening (reminders, discounts for early payment)."),
        PQ("Give three limitations of ratio analysis.",
           "Based on past data; balance sheet is one date and may be window-dressed; accounting policies and ratio definitions differ between firms; inflation distorts; non-financial factors are ignored."),
        SUM("A ratio relates two figures; it is useful only when compared over time, with other firms or with a target.",
            "Profitability: gross and net margin, ROCE, return on equity. Liquidity: current, quick and cash ratios.",
            "Efficiency: inventory turnover and days, receivables and payables days, asset turnover. Capital structure: gearing, debt to equity, interest cover.",
            "Interpret: compare, explain the cause from the data, and say what it means for the user.",
            "State the limits: historical, one date, different policies and definitions, inflation, non-financial factors."),
    ]))

# ====================================================================== 4. Cost classification and overhead allocation
# high-low (invented)
_h_lo_h, _h_lo_c, _h_hi_h, _h_hi_c = 2_000, 1_300_000, 3_500, 1_900_000
_h_vc = Fr(_h_hi_c - _h_lo_c, _h_hi_h - _h_lo_h)
_h_fc = _h_lo_c - _h_vc * _h_lo_h
_h_est = _h_fc + _h_vc * 3_000
assert (_h_vc, _h_fc, _h_est) == (400, 500_000, 1_700_000) and _h_hi_c == _h_fc + _h_vc * _h_hi_h
# incorporated charges
_i_fin, _i_nonin, _i_supp = 7_300_000, 400_000, 160_000
_i_inc = _i_fin - _i_nonin + _i_supp
assert _i_supp == 2_000_000 * 8 // 100 and _i_inc == 7_060_000
# Douala Furniture SARL: primary distribution and reciprocal services
_o_prim = {"ADM": 1_200_000, "MNT": 860_000, "SUP": 600_000, "CUT": 2_000_000, "ASM": 1_500_000, "DIS": 900_000}
assert sum(_o_prim.values()) == _i_inc
_o_kA = {"MNT": Fr(1, 10), "SUP": Fr(2, 10), "CUT": Fr(3, 10), "ASM": Fr(3, 10), "DIS": Fr(1, 10)}
_o_kM = {"ADM": Fr(2, 10), "SUP": Fr(1, 10), "CUT": Fr(4, 10), "ASM": Fr(3, 10)}
assert sum(_o_kA.values()) == 1 and sum(_o_kM.values()) == 1
# solve A = 1 200 000 + 0.2 M ; M = 860 000 + 0.1 A  (exactly)
_o_A = (_o_prim["ADM"] + _o_kM["ADM"] * _o_prim["MNT"]) / (1 - _o_kM["ADM"] * _o_kA["MNT"])
_o_M = _o_prim["MNT"] + _o_kA["MNT"] * _o_A
assert (_o_A, _o_M) == (1_400_000, 1_000_000)
_o_fromA = {c: _o_kA.get(c, 0) * _o_A for c in _o_prim}
_o_fromM = {c: _o_kM.get(c, 0) * _o_M for c in _o_prim}
_o_fromA["ADM"] = -_o_A
_o_fromM["MNT"] = -_o_M
_o_sec = {c: _o_prim[c] + _o_fromA[c] + _o_fromM[c] for c in _o_prim}
assert _o_sec == {"ADM": 0, "MNT": 0, "SUP": 980_000, "CUT": 2_820_000, "ASM": 2_220_000, "DIS": 1_040_000}
assert sum(_o_sec.values()) == sum(_o_prim.values())
_o_uow = {"SUP": ("kg of wood bought", 49_000), "CUT": ("machine hours", 1_410), "ASM": ("direct labour hours", 2_220),
          "DIS": ("100 FCFA of sales", 520_000)}
_o_cuow = {c: Fr(_o_sec[c], k) for c, (_, k) in _o_uow.items()}
assert _o_cuow == {"SUP": 20, "CUT": 2_000, "ASM": 1_000, "DIS": 2}
# quiz and practice-question systems
_x = Fr(590_000 + Fr(1, 4) * 300_000) / (1 - Fr(1, 4) * Fr(1, 5))
assert _x == 700_000 and 300_000 + Fr(1, 5) * _x == 440_000
_p = Fr(935_000 + Fr(1, 10) * 450_000) / (1 - Fr(1, 10) * Fr(1, 5))
assert _p == 1_000_000 and 450_000 + Fr(1, 5) * _p == 650_000
assert Fr(3_350_000 - 2_600_000, 2_500) == 300 and 2_600_000 - 4_000 * 300 == 1_400_000
assert 12_500_000 - 300_000 + 250_000 == 12_450_000 and Fr(3_600_000, 1_200) * 3 == 9_000
_o_names = {"ADM": "Administration", "MNT": "Maintenance", "SUP": "Supply", "CUT": "Cutting", "ASM": "Assembly", "DIS": "Distribution"}
_t_dist = "\n".join(
    ["Centre           Primary   From ADM   From MNT  Secondary"]
    + [f"{_o_names[c]:<15}{n(_o_prim[c]):>10}{n(_o_fromA[c]):>11}{n(_o_fromM[c]):>11}{n(_o_sec[c]):>11}" for c in _o_prim]
    + [f"{'Total':<15}{n(sum(_o_prim.values())):>10}{n(sum(_o_fromA.values())):>11}{n(sum(_o_fromM.values())):>11}{n(sum(_o_sec.values())):>11}"]
)
_t_uow = "\n".join(
    ["Centre        Unit of work            Number  Cost/unit"]
    + [f"{_o_names[c]:<13}{u:<22}{n(k):>8}{n(_o_cuow[c]):>11}" for c, (u, k) in _o_uow.items()]
)

LESSONS.append(lesson(
    module=M_COST, topic="Cost classification and overhead allocation",
    title="Cost classification and the distribution of indirect costs, including reciprocal services",
    slug="acu2-cost-classification-overheads", minutes=28,
    summary="Classify costs (direct/indirect, fixed/variable), find incorporated charges, separate a semi-variable cost by the high-low method, "
            "and distribute indirect costs through primary and secondary distribution, solving reciprocal services, to a cost per unit of work.",
    objectives=[
        "Classify costs as direct or indirect and as fixed, variable or semi-variable, and split a semi-variable cost by the high-low method",
        "Calculate incorporated charges from the financial accounts (non-incorporable and supplementary charges)",
        "Complete primary and secondary distribution, solving reciprocal service centres with simultaneous equations",
        "Calculate the cost of the unit of work of each main centre and explain its use",
    ],
    key_concepts=["Direct and indirect costs", "Fixed, variable and semi-variable costs", "High-low method", "Incorporated charges",
                  "Primary distribution", "Secondary distribution", "Reciprocal services", "Unit of work"],
    blocks=[
        H("From the financial accounts to product costs"),
        T("A furniture workshop in Douala sells tables and chairs. The financial accounts show the profit of the whole business, but the owner wants to know what each table costs, "
          "so that she can set prices and drop unprofitable lines. **Cost (analytical) accounting** takes the charges of the financial accounts and traces them to products. "
          "All figures in this lesson are **invented for practice**."),
        D("A **direct cost** can be traced to one product without calculation (wood for a table, the carpenter's hours on it). An **indirect cost** (overhead) is shared by several products "
          "(factory rent, the supervisor's salary) and must be distributed. A **variable cost** changes in total with activity; a **fixed cost** stays the same in total within a range of activity; "
          "a **semi-variable cost** has a fixed and a variable part (electricity with a standing charge).", title="Classifying costs"),
        H("Separating a semi-variable cost: the high-low method"),
        F(r"\text{variable cost per unit} = \frac{\text{cost at highest activity} - \text{cost at lowest activity}}{\text{highest activity} - \text{lowest activity}}", title="High-low method"),
        EX("Worked example 1: maintenance cost",
           intro="Over six months the lowest activity was 2 000 machine hours with a maintenance cost of FCFA 1 300 000, and the highest was 3 500 hours with FCFA 1 900 000. "
                 "Find the variable cost per hour, the monthly fixed cost and the expected cost for 3 000 hours.",
           steps=[
               S("Variable cost per hour", text="(1 900 000 − 1 300 000) ÷ (3 500 − 2 000) = 600 000 ÷ 1 500 = 400."),
               S("Fixed cost", text="1 300 000 − 2 000 × 400 = 500 000 a month."),
               S("Check with the high point", text="500 000 + 3 500 × 400 = 1 900 000."),
               S("Estimate for 3 000 hours", text="500 000 + 3 000 × 400 = 1 700 000."),
           ], check=r"500\,000 + 3\,500 \times 400 = 1\,900\,000"),
        T("Choose the highest and lowest **activity** levels, not the highest and lowest costs. The method uses only two points, so an unusual month distorts it; "
          "regression or a scatter graph uses all the data. Its strength is speed and simplicity."),
        H("Incorporated charges"),
        F(r"\text{incorporated charges} = \text{charges of the financial accounts} - \text{non-incorporable charges} + \text{supplementary charges}", title="Incorporated charges"),
        D("**Non-incorporable charges** (charges non incorporables) are excluded because they are not normal costs of production, for example HAO (exceptional) losses or some provisions. "
          "**Supplementary charges** (charges supplétives) are not in the financial accounts but are added for a fair cost, for example a remuneration of the owners' capital or of the owner's own work.",
          title="Non-incorporable and supplementary charges"),
        EX("Worked example 2: indirect charges to distribute",
           intro="Indirect charges in the financial accounts are FCFA 7 300 000, of which FCFA 400 000 is an exceptional (HAO) loss. The owner's capital of FCFA 2 000 000 is remunerated at 8% a year. "
                 "Find the indirect charges to distribute.",
           steps=[
               S("Supplementary charge", text="8% × 2 000 000 = 160 000."),
               S("Incorporated indirect charges", text="7 300 000 − 400 000 + 160 000 = 7 060 000."),
           ]),
        H("Distributing indirect costs"),
        KEY("The distribution table (tableau de répartition)", "Indirect costs move through three steps.",
            cards=[["Primary distribution", "Share each indirect charge between all centres (main and auxiliary) using a key: floor area for rent, staff numbers for canteen costs, and so on."],
                   ["Secondary distribution", "Empty the auxiliary (service) centres into the main centres, using the percentages given. When two service centres serve each other, solve reciprocal services first."],
                   ["Unit of work", "Divide each main centre's total by its unit of work (machine hour, labour hour, kg bought, 100 FCFA of sales) to get a cost per unit of work, used to charge products."]]),
        IMG("alacu2-overhead-distribution.svg",
            alt="Flow diagram: incorporated indirect charges go by primary distribution into service centres and main centres; service centres are emptied by secondary distribution into main centres; each main centre total is divided by its unit of work.",
            caption="Figure 1. From indirect charges to the cost of a unit of work."),
        D("When two service centres give services to each other, let A and M be their **totals after receiving** each other's share. Write one equation per centre "
          "(total = primary amount + share received from the other) and solve them together. Then distribute A and M in full.", title="Reciprocal services: the algebraic method"),
        EX("Worked example 3: Douala Furniture SARL",
           intro="Primary distribution: Administration 1 200 000; Maintenance 860 000; Supply 600 000; Cutting 2 000 000; Assembly 1 500 000; Distribution 900 000. "
                 "Administration is shared: Maintenance 10%, Supply 20%, Cutting 30%, Assembly 30%, Distribution 10%. Maintenance is shared: Administration 20%, Supply 10%, Cutting 40%, Assembly 30%. "
                 "Units of work: Supply, kg of wood bought (49 000); Cutting, machine hours (1 410); Assembly, direct labour hours (2 220); Distribution, 100 FCFA of sales (sales 52 000 000).",
           steps=[
               S("Equations", math=r"A = 1\,200\,000 + 0.2M \qquad M = 860\,000 + 0.1A"),
               S("Substitute", math=r"A = 1\,200\,000 + 0.2(860\,000 + 0.1A) = 1\,372\,000 + 0.02A"),
               S("Solve", math=r"0.98A = 1\,372\,000 \Rightarrow A = 1\,400\,000,\; M = 860\,000 + 140\,000 = 1\,000\,000"),
               S("Distribute A = 1 400 000", text="Maintenance 140 000; Supply 280 000; Cutting 420 000; Assembly 420 000; Distribution 140 000."),
               S("Distribute M = 1 000 000", text="Administration 200 000; Supply 100 000; Cutting 400 000; Assembly 300 000."),
               S("Totals of main centres", text="Supply 980 000; Cutting 2 820 000; Assembly 2 220 000; Distribution 1 040 000. Their sum is 7 060 000, the same as the primary total."),
               S("Cost of the unit of work", text="Supply 980 000 ÷ 49 000 = 20 per kg; Cutting 2 820 000 ÷ 1 410 = 2 000 per machine hour; Assembly 2 220 000 ÷ 2 220 = 1 000 per labour hour; "
                                                 "Distribution 1 040 000 ÷ 520 000 = 2 per 100 FCFA of sales."),
           ], check=r"A = 1\,200\,000 + 0.2 \times 1\,000\,000 = 1\,400\,000"),
        CODE(_t_dist, "text", title="Distribution table (invented for practice)"),
        CODE(_t_uow, "text", title="Cost of the unit of work"),
        MISTAKE("Distributing only the primary amount of a reciprocal centre",
                "Administration distributes 1 400 000 (its primary 1 200 000 plus the 200 000 received from Maintenance), not 1 200 000. Solve the equations first; then each service centre ends at zero."),
        MISTAKE("Losing money in the table",
                "After secondary distribution the main centres must total exactly the incorporated indirect charges. Check this total before calculating units of work."),
        MISTAKE("Picking the highest and lowest costs in high-low",
                "Use the months with the highest and lowest activity. If a cost is out of line with its activity, the two points are not the cost extremes."),
        QUIZ("Two service centres: X = 590 000 + 0.25Y and Y = 300 000 + 0.2X. What is the total of X to be distributed?",
             ["590 000", "665 000", "700 000", "1 140 000"], 2,
             "X = 590 000 + 0.25(300 000 + 0.2X) = 665 000 + 0.05X, so 0.95X = 665 000 and X = 700 000 (then Y = 440 000).",
             hint="Substitute the expression for Y into the equation for X.",
             feedback=["This ignores the service X receives from Y.", "This stops before moving 0.05X to the left-hand side.", "",
                       "This adds the totals of X and Y together."]),
        QUIZ("A cutting centre has total indirect costs of FCFA 3 600 000 after secondary distribution and works 1 200 machine hours. A product uses 3 machine hours. Its cutting overhead is",
             ["3 000", "9 000", "1 200", "10 800 000"], 1,
             "Cost of the unit of work = 3 600 000 ÷ 1 200 = 3 000 per hour; 3 hours × 3 000 = 9 000.",
             feedback=["This is the cost of one machine hour, not of 3 hours.", "", "This copies the number of hours.",
                       "This multiplies the centre total by 3."], title="Quick check 2"),
        TIP("Overhead distribution is a cost accounting topic, so it belongs to Paper 2 (Section A, cost accounting), and the Board's 2023 report mentions questions on separating costs by high-low and on "
            "overhead absorption for job costing. Expect Paper 1 items on cost classification and on reciprocal-service equations.", title="Exam link"),
        PQ("Activity and cost data: lowest 4 000 units, FCFA 2 600 000; highest 6 500 units, FCFA 3 350 000. Find the variable cost per unit and the fixed cost.",
           "Variable cost = 750 000 ÷ 2 500 = 300 per unit. Fixed cost = 2 600 000 − 4 000 × 300 = 1 400 000."),
        PQ("Charges of the financial accounts FCFA 12 500 000 include FCFA 300 000 of exceptional losses; the owner's work is valued at FCFA 250 000 for the period. Find the incorporated charges.",
           "12 500 000 − 300 000 + 250 000 = 12 450 000."),
        PQ("Service centres P and Q: P = 935 000 + 0.1Q and Q = 450 000 + 0.2P. Find P and Q.",
           "P = 935 000 + 0.1(450 000 + 0.2P) = 980 000 + 0.02P; 0.98P = 980 000; P = 1 000 000; Q = 450 000 + 200 000 = 650 000. "
           "Check: 935 000 + 0.1 × 650 000 = 1 000 000."),
        PQ("Explain why a supplementary charge is added in cost accounting although it is not in the financial accounts.",
           "To compare costs fairly between firms that own their capital or premises and firms that borrow or rent: the opportunity cost of the owner's capital or work is a real economic cost."),
        SUM("Direct costs are traced to products; indirect costs are distributed. Fixed, variable and semi-variable costs behave differently with activity.",
            "High-low: variable cost = change in cost ÷ change in activity, then fixed cost = total cost − variable part.",
            "Incorporated charges = financial charges − non-incorporable + supplementary.",
            "Primary distribution to all centres, then secondary distribution of service centres; solve reciprocal services with simultaneous equations.",
            "Main centre total ÷ number of units of work = cost of the unit of work, used to charge each product."),
    ]))

# ====================================================================== 5. Stock valuation and cost price
# Douala Furniture SARL again (units of work from lesson 4)
_s_q0, _s_v0 = 1_000, 396_000
_s_qb, _s_pb = 5_000, 400
_s_supply = _s_qb * _o_cuow["SUP"]
_s_pc = _s_qb * _s_pb + _s_supply
assert (_s_supply, _s_pc, Fr(_s_pc, _s_qb)) == (100_000, 2_100_000, 420)
_s_cump = Fr(_s_v0 + _s_pc, _s_q0 + _s_qb)
assert _s_cump == 416
_s_issue = 4_500
_s_mat = _s_issue * _s_cump
_s_close = (_s_q0 + _s_qb - _s_issue) * _s_cump
assert (_s_mat, _s_close) == (1_872_000, 624_000) and _s_mat + _s_close == _s_v0 + _s_pc
_s_fifo = _s_v0 + (_s_issue - _s_q0) * 420
_s_fifo_close = (_s_q0 + _s_qb - _s_issue) * 420
assert (_s_fifo, _s_fifo_close) == (1_866_000, 630_000) and _s_fifo + _s_fifo_close == _s_v0 + _s_pc
_s_lab = 1_240 * 1_500
_s_cut = 450 * _o_cuow["CUT"]
_s_asm = 1_240 * _o_cuow["ASM"]
_s_prod = _s_mat + _s_lab + _s_cut + _s_asm
assert (_s_lab, _s_cut, _s_asm, _s_prod) == (1_860_000, 900_000, 1_240_000, 5_872_000)
_s_fq0, _s_fv0, _s_fq = 200, 1_160_000, 1_000
_s_fcump = Fr(_s_fv0 + _s_prod, _s_fq0 + _s_fq)
assert _s_fcump == 5_860
_s_sold = 1_100
_s_cogs = _s_sold * _s_fcump
_s_fclose = (_s_fq0 + _s_fq - _s_sold) * _s_fcump
assert (_s_cogs, _s_fclose) == (6_446_000, 586_000)
_s_sales = _s_sold * 7_000
_s_dist = Fr(_s_sales, 100) * _o_cuow["DIS"]
_s_cp = _s_cogs + _s_dist
_s_res = _s_sales - _s_cp
assert (_s_sales, _s_dist, _s_cp, _s_res) == (7_700_000, 154_000, 6_600_000, 1_100_000)
# reconciliation (separate data)
_s_ar, _s_sup, _s_ni, _s_hao = 2_500_000, 160_000, 400_000, 150_000
_s_fr = _s_ar + _s_sup - _s_ni + _s_hao
assert _s_fr == 2_410_000
assert Fr(600_000 + 2_040_000, 2_000) == 1_320 and 500 * 1_200 + 1_100 * 1_360 == 2_096_000
assert Fr(11_100_000, 2_500) == 4_440 and 2_200 * 4_440 + 640_000 == 10_408_000 and 2_200 * 6_000 - 10_408_000 == 2_792_000
assert Fr(262_000, 1_000) == 262 and 4_000_000 + 300_000 - 250_000 - 5_000 == 4_045_000

_t_stock = "\n".join([
    "Material stock account (CUMP including opening stock)",
    "                     Qty     Unit cost      Amount",
    f"Opening stock     {n(_s_q0):>6}   {'396':>10}   {n(_s_v0):>10}",
    f"Purchases         {n(_s_qb):>6}   {'420':>10}   {n(_s_pc):>10}",
    f"Total             {n(_s_q0 + _s_qb):>6}   {n(_s_cump):>10}   {n(_s_v0 + _s_pc):>10}",
    f"Issues            {n(_s_issue):>6}   {n(_s_cump):>10}   {n(_s_mat):>10}",
    f"Closing stock     {n(_s_q0 + _s_qb - _s_issue):>6}   {n(_s_cump):>10}   {n(_s_close):>10}",
])
_t_cascade = "\n".join([
    "Cost of production (1 000 units)",
    r("Materials used 4 500 kg x 416", _s_mat, w=40),
    r("Direct labour 1 240 h x 1 500", _s_lab, w=40),
    r("Cutting 450 machine h x 2 000", _s_cut, w=40),
    r("Assembly 1 240 labour h x 1 000", _s_asm, w=40),
    r("Production cost", None, _s_prod, w=40),
    "",
    "Finished goods (CUMP): (1 160 000 + 5 872 000) / 1 200 = 5 860",
    r("Cost of 1 100 units sold x 5 860", _s_cogs, w=40),
    r("Distribution 2 per 100 FCFA x 77 000", _s_dist, w=40),
    r("Cost price", None, _s_cp, w=40),
    r("Sales 1 100 x 7 000", None, _s_sales, w=40),
    r("Analytical result", None, _s_res, w=40),
])

LESSONS.append(lesson(
    module=M_COST, topic="Stock valuation and cost price",
    title="From purchase cost to cost price: stock valuation and the analytical result",
    slug="acu2-stock-valuation-cost-price", minutes=26,
    summary="Follow the full-cost cascade: purchase cost, material stock valued by CUMP or FIFO, production cost, finished goods stock, "
            "cost price and analytical result, then reconcile the analytical result with the financial accounting result.",
    objectives=[
        "Calculate the purchase cost of materials, including the supply centre's costs",
        "Value issues and closing stock by the weighted average cost including opening stock (CUMP) and by FIFO",
        "Calculate production cost, cost of goods sold, cost price and analytical result",
        "Reconcile the analytical result with the financial result using supplementary and non-incorporable items",
    ],
    key_concepts=["Purchase cost", "Weighted average cost (CUMP)", "FIFO", "Production cost", "Cost price",
                  "Analytical result", "Reconciliation of results"],
    blocks=[
        H("The full-cost cascade"),
        T("In the previous lesson Douala Furniture SARL found the cost of each unit of work. Now the costs travel with the product: from the wood bought, through the workshop, "
          "to the table that a customer in Bonabéri carries away. Each stage adds costs, and stocks between stages must be valued. All figures are **invented for practice**."),
        IMG("alacu2-cost-cascade.svg",
            alt="Five stacked boxes from purchase cost to material stock, production cost, finished goods stock and cost price, with notes on what each adds, ending with the analytical result equal to sales minus cost price.",
            caption="Figure 1. The full-cost cascade in the OHADA approach."),
        D("**Purchase cost** (coût d'achat) = purchase price + direct purchasing costs + share of the supply centre. **Production cost** (coût de production) = materials used + direct labour + share of the production centres. "
          "**Cost price** (coût de revient) = production cost of the goods sold + distribution costs. **Analytical result** = sales − cost price.", title="Four costs"),
        H("Valuing stock"),
        KEY("Two methods for issues", "Both are accepted; the method must be applied consistently.",
            cards=[["CUMP (weighted average including opening stock)", "Unit cost = (value of opening stock + value of purchases) ÷ (opening quantity + quantity purchased). All issues of the period use this one cost."],
                   ["CUMP after each receipt", "A new average is calculated after every receipt (perpetual inventory)."],
                   ["FIFO (first in, first out)", "Issues are taken from the oldest batch first; closing stock is valued at the latest prices."]]),
        EX("Worked example 1: material stock",
           intro="Opening stock of wood: 1 000 kg valued at FCFA 396 000. Purchases: 5 000 kg at FCFA 400 a kg; the supply centre's cost is FCFA 20 per kg bought (lesson 4). "
                 "4 500 kg are issued to the workshop. Value the issues and closing stock by CUMP and by FIFO.",
           steps=[
               S("Purchase cost", text="5 000 × 400 + 5 000 × 20 = 2 000 000 + 100 000 = 2 100 000 (420 per kg)."),
               S("CUMP", text="(396 000 + 2 100 000) ÷ (1 000 + 5 000) = 2 496 000 ÷ 6 000 = 416 per kg."),
               S("CUMP values", text="Issues 4 500 × 416 = 1 872 000; closing stock 1 500 × 416 = 624 000."),
               S("FIFO values", text="Issues: 1 000 kg at 396 (396 000) + 3 500 kg at 420 (1 470 000) = 1 866 000; closing stock 1 500 × 420 = 630 000."),
               S("Check", text="Both methods share out the same 2 496 000: 1 872 000 + 624 000 = 1 866 000 + 630 000."),
           ]),
        CODE(_t_stock, "text", title="Material stock account (invented for practice)"),
        T("When prices are rising, FIFO gives a higher closing stock and a lower cost of materials used than CUMP, so a higher profit. Neither method changes the total cost; it changes how the cost is split between this period and the next."),
        H("Production cost, cost price and result"),
        EX("Worked example 2: from the workshop to the customer",
           intro="1 000 tables are made using the 4 500 kg of wood (CUMP), 1 240 direct labour hours at FCFA 1 500, 450 machine hours in cutting (2 000 per hour) and the 1 240 labour hours in assembly (1 000 per hour). "
                 "Opening stock: 200 tables valued at FCFA 1 160 000. 1 100 tables are sold at FCFA 7 000. Distribution costs 2 per 100 FCFA of sales. Find the cost price and the analytical result.",
           steps=[
               S("Production cost", text="1 872 000 + 1 860 000 + 900 000 + 1 240 000 = 5 872 000 (5 872 a table)."),
               S("Finished goods CUMP", text="(1 160 000 + 5 872 000) ÷ (200 + 1 000) = 7 032 000 ÷ 1 200 = 5 860."),
               S("Cost of goods sold", text="1 100 × 5 860 = 6 446 000; closing stock 100 × 5 860 = 586 000."),
               S("Distribution and cost price", text="Sales 7 700 000; distribution 77 000 × 2 = 154 000; cost price 6 446 000 + 154 000 = 6 600 000."),
               S("Analytical result", text="7 700 000 − 6 600 000 = 1 100 000 profit, i.e. 1 000 per table sold."),
           ]),
        CODE(_t_cascade, "text", title="Production cost, cost price and result"),
        H("Reconciling with the financial accounts"),
        F(r"\text{financial result} = \text{analytical results} + \text{supplementary} - \text{non-incorporable} + \text{other income} \pm \text{rounding}",
          title="Reconciliation"),
        T("Supplementary charges were added in cost accounting but never paid, so they are added back; non-incorporable charges reduce the financial result but were left out of costs, so they are deducted; "
          "income left out of cost accounting (an HAO gain, for example) is added. Rounding differences on units of work also appear here."),
        EX("Worked example 3: reconciliation",
           intro="The analytical results of all products total FCFA 2 500 000. Supplementary charges were FCFA 160 000, non-incorporable charges FCFA 400 000, and an HAO gain of FCFA 150 000 was left out of cost accounting. Find the financial result.",
           steps=[
               S("Add back supplementary charges", text="2 500 000 + 160 000 = 2 660 000."),
               S("Deduct non-incorporable charges", text="2 660 000 − 400 000 = 2 260 000."),
               S("Add the non-incorporated gain", text="2 260 000 + 150 000 = 2 410 000."),
           ]),
        MISTAKE("Averaging the prices instead of the values",
                "CUMP is total value ÷ total quantity. (396 + 420) ÷ 2 = 408 is wrong because the quantities differ."),
        MISTAKE("Using production cost for the goods sold without the finished goods stock",
                "Goods sold come from the finished goods stock, which mixes the opening stock and this period's production. Value the goods sold at the stock's CUMP (or FIFO), not at this period's production cost."),
        MISTAKE("Adding distribution costs to stock",
                "Distribution costs belong to the goods sold, so they enter the cost price, never the value of stock."),
        QUIZ("Opening stock 400 kg at FCFA 250 (100 000); purchases 600 kg costing FCFA 162 000. The CUMP including opening stock is",
             ["262", "260", "270", "262 000"], 0,
             "(100 000 + 162 000) ÷ (400 + 600) = 262 000 ÷ 1 000 = 262.",
             hint="Total value divided by total quantity.",
             feedback=["", "This averages the two unit prices (250 + 270) ÷ 2.", "This is the unit price of the purchases only.",
                       "This is the total value of the stock, not the cost per kg."]),
        QUIZ("Which item is part of the cost price but not of the production cost?",
             ["Direct labour of the workshop", "Share of the cutting centre", "Distribution costs", "Materials used"], 2,
             "Distribution happens after production, when goods are sold; it is added to the cost of goods sold to give the cost price.",
             feedback=["Direct labour is part of production cost.", "Production centres are part of production cost.", "",
                       "Materials used are part of production cost."], title="Quick check 2"),
        TIP("Stock cards (FIFO and weighted average) and full-cost statements are cost accounting topics for Paper 2. The Board's 2023 report describes a stock valuation question with stock cards "
            "by FIFO and weighted average followed by a trading account, which candidates answered well. Set out stock cards in neat columns: date, quantity, unit cost, amount.", title="Exam link"),
        PQ("Opening stock 500 units at FCFA 1 200; purchases 1 500 units at FCFA 1 360. 1 600 units are issued. Value the issues by CUMP and by FIFO.",
           "CUMP = (600 000 + 2 040 000) ÷ 2 000 = 1 320; issues 1 600 × 1 320 = 2 112 000. FIFO: 500 × 1 200 + 1 100 × 1 360 = 600 000 + 1 496 000 = 2 096 000."),
        PQ("Production cost of 2 000 units FCFA 9 000 000; opening stock 500 units FCFA 2 100 000; 2 200 units sold at FCFA 6 000; distribution costs FCFA 640 000. Find the cost price and analytical result (CUMP).",
           "CUMP = 11 100 000 ÷ 2 500 = 4 440. Cost of goods sold 2 200 × 4 440 = 9 768 000. Cost price 9 768 000 + 640 000 = 10 408 000. Sales 13 200 000. Result 2 792 000."),
        PQ("Analytical result FCFA 4 000 000; supplementary charges FCFA 300 000; non-incorporable charges FCFA 250 000; rounding differences −FCFA 5 000. Find the financial result.",
           "4 000 000 + 300 000 − 250 000 − 5 000 = 4 045 000."),
        PQ("Explain why the choice between FIFO and CUMP changes the profit of the period but not the total cost of the goods.",
           "Both methods share the same total cost between goods used (or sold) and closing stock. When prices change, the split differs, so the cost charged this period and the stock carried forward differ; "
           "the stock's cost is charged in a later period instead."),
        SUM("Purchase cost = price + purchasing costs + supply centre; production cost = materials used + direct labour + production centres.",
            "CUMP = (opening value + purchases value) ÷ (opening quantity + quantity bought); FIFO issues the oldest batches first.",
            "Goods sold are valued from the finished goods stock; cost price = cost of goods sold + distribution costs.",
            "Analytical result = sales − cost price.",
            "Financial result = analytical results + supplementary − non-incorporable + non-incorporated income ± rounding."),
    ]))

# ====================================================================== 6. Job, batch and process costing
_j_oar = Fr(9_000_000, 12_000)
_j_mat, _j_lab, _j_oh = 420_000, 160 * 1_200, 160 * _j_oar
_j_prod = _j_mat + _j_lab + _j_oh
_j_adm = _j_prod * Fr(10, 100)
_j_tot = _j_prod + _j_adm
_j_p_margin = _j_tot / Fr(80, 100)
_j_p_markup = _j_tot * Fr(120, 100)
assert (_j_oar, _j_lab, _j_oh, _j_prod, _j_adm, _j_tot) == (750, 192_000, 120_000, 732_000, 73_200, 805_200)
assert (_j_p_margin, _j_p_markup) == (1_006_500, 966_240)
_t_job = "\n".join([
    "Job cost sheet - Job J47 (invented for practice)",
    r("Direct materials", _j_mat, w=36),
    r("Direct labour 160 h x 1 200", _j_lab, w=36),
    r("Prime cost", None, _j_mat + _j_lab, w=36),
    r("Overhead absorbed 160 h x 750", _j_oh, w=36),
    r("Production cost", None, _j_prod, w=36),
    r("Administration and selling 10%", _j_adm, w=36),
    r("Total cost", None, _j_tot, w=36),
    r("Profit (20% of selling price)", None, _j_p_margin - _j_tot, w=36),
    r("Selling price", None, _j_p_margin, w=36),
])
_b_tot = 1_100_000 + 300 * 1_000 + 300 * 750 + 125_000
assert _b_tot == 1_750_000 and Fr(_b_tot, 500) == 3_500
# process with losses
_p_in, _p_cost, _p_conv, _p_nl_pct, _p_scrap, _p_out = 10_000, 3_000_000, 1_390_000, 5, 40, 9_300
_p_nl = _p_in * _p_nl_pct // 100
_p_cpk = Fr(_p_cost + _p_conv - _p_nl * _p_scrap, _p_in - _p_nl)
_p_ab = _p_in - _p_nl - _p_out
assert (_p_nl, _p_cpk, _p_ab) == (500, 460, 200)
_p_good, _p_abv = _p_out * _p_cpk, _p_ab * _p_cpk
assert _p_good + _p_abv + _p_nl * _p_scrap == _p_cost + _p_conv
assert (_p_good, _p_abv, _p_abv - _p_ab * _p_scrap) == (4_278_000, 92_000, 84_000)
_t_proc = "\n".join([
    "Process account (invented for practice)",
    "DEBIT                         kg        FCFA",
    f"Materials input           {n(_p_in):>6}  {n(_p_cost):>10}",
    f"Conversion costs                  {n(_p_conv):>10}",
    f"Total                     {n(_p_in):>6}  {n(_p_cost + _p_conv):>10}",
    "CREDIT",
    f"Normal loss (scrap @ 40)  {n(_p_nl):>6}  {n(_p_nl * _p_scrap):>10}",
    f"Abnormal loss @ 460       {n(_p_ab):>6}  {n(_p_abv):>10}",
    f"Good output @ 460         {n(_p_out):>6}  {n(_p_good):>10}",
    f"Total                     {n(_p_in):>6}  {n(_p_good + _p_abv + _p_nl * _p_scrap):>10}",
])
# abnormal gain variant (practice question)
_p_gain = 9_600 - (_p_in - _p_nl)
assert _p_gain == 100 and _p_gain * _p_cpk == 46_000 and _p_gain * _p_cpk - _p_gain * _p_scrap == 42_000
# equivalent units
_q_start, _q_done, _q_wip, _q_conv_pct = 8_000, 6_500, 1_500, 40
_q_mat, _q_conv = 2_400_000, 2_840_000
_q_eu_m = _q_done + _q_wip
_q_eu_c = _q_done + _q_wip * _q_conv_pct // 100
_q_cm, _q_cc = Fr(_q_mat, _q_eu_m), Fr(_q_conv, _q_eu_c)
assert (_q_eu_m, _q_eu_c, _q_cm, _q_cc) == (8_000, 7_100, 300, 400)
_q_fin = _q_done * (_q_cm + _q_cc)
_q_wipv = _q_wip * _q_cm + _q_wip * _q_conv_pct // 100 * _q_cc
assert (_q_fin, _q_wipv) == (4_550_000, 690_000) and _q_fin + _q_wipv == _q_mat + _q_conv
_t_eu = "\n".join([
    "Statement of equivalent units",
    "                       Materials   Conversion",
    f"Completed units          {n(_q_done):>7}      {n(_q_done):>7}",
    f"Closing WIP 1 500        {n(_q_wip):>7}      {n(_q_wip * 40 // 100):>7}   (100% / 40%)",
    f"Equivalent units         {n(_q_eu_m):>7}      {n(_q_eu_c):>7}",
    f"Costs (FCFA)          {n(_q_mat):>10}   {n(_q_conv):>10}",
    f"Cost per unit              {n(_q_cm):>5}        {n(_q_cc):>5}",
])
assert Fr(14_400_000, 16_000) == 900 and 400_000 + 35 * 900 == 431_500
assert Fr(1_000_000, Fr(80, 100)) == 1_250_000 and 1_000_000 * Fr(125, 100) == 1_250_000

LESSONS.append(lesson(
    module=M_COST, topic="Job, batch and process costing",
    title="Job, batch and process costing: absorption rates, losses and equivalent units",
    slug="acu2-job-batch-process-costing", minutes=27,
    summary="Choose the costing method that fits the production: job cost sheets with an overhead absorption rate, batch costs per unit, "
            "and process accounts with normal loss, abnormal loss or gain and equivalent units for work in progress.",
    objectives=[
        "Calculate a predetermined overhead absorption rate and complete a job cost sheet and a selling price (margin or mark-up)",
        "Calculate the cost per unit of a batch",
        "Prepare a process account with normal loss, abnormal loss and abnormal gain",
        "Value finished output and closing work in progress using equivalent units",
    ],
    key_concepts=["Job costing", "Overhead absorption rate", "Batch costing", "Process costing", "Normal loss",
                  "Abnormal loss and gain", "Equivalent units", "Work in progress"],
    blocks=[
        H("Three ways of producing, three ways of costing"),
        T("A tailor in Bamenda makes a wedding suit to order; a factory in Limbé makes school bags in batches of 500; a palm-oil mill near Edéa runs fruit through the same stages day and night. "
          "Each needs a different costing method. All figures are **invented for practice**."),
        KEY("Which method?", "The method follows the way the product is made.",
            cards=[["Job costing", "Each order is unique and separately identifiable (repairs, printing, construction, made-to-measure clothing). Costs are collected on a job cost sheet."],
                   ["Batch costing", "A group of identical items is made together. The batch is costed like a job; cost per unit = batch cost ÷ units in the batch."],
                   ["Process costing", "Identical output flows continuously through stages (oil, cement, soap, beer). Costs are averaged over the output of each process."]]),
        H("Job costing"),
        F(r"\text{OAR} = \frac{\text{budgeted overheads}}{\text{budgeted activity (e.g. direct labour hours)}}", title="Predetermined overhead absorption rate"),
        T("The rate is calculated **in advance** from budgets so that a job can be priced when it is finished. At the year end, overheads absorbed (OAR × actual hours) are compared with actual overheads: "
          "the difference is **under-absorbed** (absorbed < actual) or **over-absorbed** (absorbed > actual) and goes to the income statement."),
        EX("Worked example 1: Job J47",
           intro="Budgeted overheads FCFA 9 000 000; budgeted direct labour hours 12 000. Job J47 uses materials FCFA 420 000 and 160 direct labour hours at FCFA 1 200. "
                 "Administration and selling costs are 10% of production cost. The price gives a profit of 20% of the selling price. Prepare the job cost sheet.",
           steps=[
               S("OAR", text="9 000 000 ÷ 12 000 = 750 per direct labour hour."),
               S("Prime cost", text="420 000 + 160 × 1 200 = 420 000 + 192 000 = 612 000."),
               S("Production cost", text="612 000 + 160 × 750 = 612 000 + 120 000 = 732 000."),
               S("Total cost", text="732 000 + 10% × 732 000 = 805 200."),
               S("Selling price with a 20% margin on price", text="Cost is 80% of price: 805 200 ÷ 0.8 = 1 006 500 (profit 201 300)."),
               S("Compare a 20% mark-up on cost", text="805 200 × 1.2 = 966 240: a lower price, because 20% of cost is less than 20% of price."),
           ]),
        CODE(_t_job, "text", title="Job cost sheet"),
        D("A **margin** is profit as a percentage of the **selling price**; a **mark-up** is profit as a percentage of **cost**. A 20% margin equals a 25% mark-up. "
          "Read the question: '20% of selling price' means divide cost by 0.8; '20% on cost' means multiply by 1.2.", title="Margin or mark-up?"),
        H("Batch costing"),
        EX("Worked example 2: a batch of school bags",
           intro="A batch of 500 school bags uses materials FCFA 1 100 000 and 300 direct labour hours at FCFA 1 000; overheads are absorbed at FCFA 750 per labour hour and the machine set-up for the batch costs FCFA 125 000. Find the cost per bag.",
           steps=[
               S("Batch cost", text="1 100 000 + 300 000 + 225 000 + 125 000 = 1 750 000."),
               S("Cost per bag", text="1 750 000 ÷ 500 = 3 500."),
           ]),
        H("Process costing with losses"),
        D("A **normal loss** is the loss expected in normal conditions (evaporation, waste). Its cost is borne by the good output; any **scrap value** reduces the cost. "
          "An **abnormal loss** is a loss above the normal level; an **abnormal gain** is a loss below it. Both are valued at the **same cost per unit as good output** and taken to the income statement.",
          title="Normal and abnormal losses"),
        F(r"\text{cost per unit} = \frac{\text{process costs} - \text{scrap value of normal loss}}{\text{input} - \text{normal loss}}", title="Cost per unit of expected output"),
        EX("Worked example 3: refining process",
           intro="Input 10 000 kg costing FCFA 3 000 000; conversion costs FCFA 1 390 000. Normal loss is 5% of input and is sold as scrap at FCFA 40 a kg. Actual output is 9 300 kg. Prepare the process figures.",
           steps=[
               S("Normal loss", text="5% × 10 000 = 500 kg; scrap value 500 × 40 = 20 000."),
               S("Cost per kg", text="(3 000 000 + 1 390 000 − 20 000) ÷ (10 000 − 500) = 4 370 000 ÷ 9 500 = 460."),
               S("Abnormal loss", text="Expected output 9 500 kg − actual 9 300 kg = 200 kg, valued 200 × 460 = 92 000."),
               S("Good output", text="9 300 × 460 = 4 278 000."),
               S("Check and income statement", text="4 278 000 + 92 000 + 20 000 = 4 390 000. The abnormal loss account receives the scrap value of the 200 kg (8 000), so 84 000 goes to the income statement."),
           ]),
        CODE(_t_proc, "text", title="Process account"),
        H("Work in progress and equivalent units"),
        D("Unfinished units at the end of a period are **work in progress (WIP)**. They are converted into **equivalent units**: 1 500 units that are 40% complete for conversion are worth 600 complete units for that cost. "
          "Materials added at the start are 100% complete.", title="Equivalent units"),
        EX("Worked example 4: valuing output and WIP",
           intro="8 000 units start; 6 500 are finished and 1 500 remain in progress, 100% complete for materials and 40% for conversion. Materials FCFA 2 400 000; conversion FCFA 2 840 000. Value the finished units and the WIP.",
           steps=[
               S("Equivalent units", text="Materials: 6 500 + 1 500 = 8 000. Conversion: 6 500 + 40% × 1 500 = 7 100."),
               S("Cost per equivalent unit", text="Materials 2 400 000 ÷ 8 000 = 300; conversion 2 840 000 ÷ 7 100 = 400."),
               S("Finished units", text="6 500 × (300 + 400) = 4 550 000."),
               S("WIP", text="1 500 × 300 + 600 × 400 = 450 000 + 240 000 = 690 000. Check: 4 550 000 + 690 000 = 5 240 000."),
           ]),
        CODE(_t_eu, "text", title="Equivalent units (invented for practice)"),
        MISTAKE("Valuing the abnormal loss at the average of all input",
                "Abnormal loss and abnormal gain carry the same cost per unit as good output (here 460), so that the good output is not burdened with the abnormal event."),
        MISTAKE("Forgetting the degree of completion",
                "Count WIP at its percentage of completion for each cost element; materials and conversion often differ."),
        QUIZ("Budgeted overheads FCFA 6 000 000; budgeted machine hours 4 000. Actual hours 4 200; actual overheads FCFA 6 150 000. The overhead is",
             ["under-absorbed by 150 000", "over-absorbed by 150 000", "over-absorbed by 300 000", "under-absorbed by 300 000"], 1,
             "OAR = 1 500 per hour; absorbed = 4 200 × 1 500 = 6 300 000; actual 6 150 000; absorbed exceeds actual by 150 000, so over-absorbed.",
             hint="Absorbed = OAR × actual hours; compare with actual overheads.",
             feedback=["Absorbed (6 300 000) is more than actual, so it is over-absorbed.", "", "300 000 compares absorbed with budgeted overheads, not actual.",
                       "Wrong direction and wrong comparison."]),
        QUIZ("A process expects output of 9 000 kg but produces 9 100 kg. The 100 kg is",
             ["an abnormal loss", "a normal loss", "an abnormal gain", "work in progress"], 2,
             "Actual loss was smaller than the normal loss, so there is an abnormal gain of 100 kg.",
             feedback=["A loss above normal would reduce output below 9 000 kg.", "Normal loss is the expected loss, already allowed for in 9 000 kg.", "",
                       "WIP is unfinished output, not extra finished output."], title="Quick check 2"),
        TIP("Job and process costing belong to Paper 2, Section A (cost accounting). The Board's 2023 report describes a question asking for an overhead absorption rate on direct labour hours and a job cost sheet. "
            "Lay out a cost sheet line by line: prime cost, production cost, total cost, profit, price.", title="Exam link"),
        PQ("Budgeted overheads FCFA 14 400 000; budgeted labour hours 16 000. A job uses materials FCFA 250 000, labour FCFA 150 000 and 35 labour hours. Find its production cost.",
           "OAR = 900 per hour. Production cost = 250 000 + 150 000 + 35 × 900 = 431 500."),
        PQ("Total cost of a job is FCFA 1 000 000. Find the price for (a) a 20% margin on selling price; (b) a 25% mark-up on cost.",
           "(a) 1 000 000 ÷ 0.8 = 1 250 000; (b) 1 000 000 × 1.25 = 1 250 000. The two are equal: a 20% margin is a 25% mark-up."),
        PQ("Using worked example 3 (cost per kg 460, normal loss 500 kg, scrap 40 per kg), actual output is 9 600 kg. Find the abnormal gain and its net effect on profit.",
           "Expected output 9 500 kg, so abnormal gain 100 kg × 460 = 46 000. Scrap income lost on 100 kg = 4 000. Net gain to the income statement 42 000."),
        PQ("Explain why WIP must be converted into equivalent units before a cost per unit is calculated.",
           "Unfinished units have received only part of the conversion work. Counting them as whole units would understate the cost per unit of finished output and overvalue the WIP."),
        SUM("Job costing: one cost sheet per order; overheads absorbed by a predetermined rate; compare absorbed and actual overheads.",
            "Batch costing: cost the batch, then divide by the number of units.",
            "Process costing: cost per unit = (costs − scrap of normal loss) ÷ (input − normal loss).",
            "Abnormal loss and gain are valued at the same cost per unit as good output and go to the income statement.",
            "WIP is counted in equivalent units for each cost element."),
    ]))

# ====================================================================== 7. Activity-based costing
_a_units = {"S": 10_000, "D": 2_000}
_a_dlh = {"S": 5_000, "D": 2_000}
_a_pools = {  # activity: (cost, driver, {product: driver quantity})
    "Machine set-ups": (4_200_000, "set-ups", {"S": 10, "D": 20}),
    "Purchase orders": (3_000_000, "orders", {"S": 40, "D": 60}),
    "Machine running": (6_800_000, "machine hours", {"S": 6_000, "D": 2_500}),
}
_a_total = sum(c for c, _, _ in _a_pools.values())
assert _a_total == 14_000_000
_a_rate = {k: Fr(c, sum(q.values())) for k, (c, _, q) in _a_pools.items()}
assert _a_rate == {"Machine set-ups": 140_000, "Purchase orders": 30_000, "Machine running": 800}
_a_abc = {p: sum(_a_rate[k] * q[p] for k, (_, _, q) in _a_pools.items()) for p in _a_units}
assert _a_abc == {"S": 7_400_000, "D": 6_600_000} and sum(_a_abc.values()) == _a_total
_a_abc_u = {p: _a_abc[p] / _a_units[p] for p in _a_units}
_a_oar = Fr(_a_total, sum(_a_dlh.values()))
_a_trad_u = {p: _a_oar * _a_dlh[p] / _a_units[p] for p in _a_units}
assert _a_oar == 2_000 and _a_abc_u == {"S": 740, "D": 3_300} and _a_trad_u == {"S": 1_000, "D": 2_000}
_a_price, _a_direct = {"S": 6_000, "D": 12_000}, {"S": 3_500, "D": 7_000}
_a_prof_t = {p: _a_price[p] - _a_direct[p] - _a_trad_u[p] for p in _a_units}
_a_prof_a = {p: _a_price[p] - _a_direct[p] - _a_abc_u[p] for p in _a_units}
assert _a_prof_t == {"S": 1_500, "D": 3_000} and _a_prof_a == {"S": 1_760, "D": 1_700}
_t_abc = "\n".join(
    ["Activity          Cost       Driver          S      D    Rate"]
    + [f"{k:<16}{n(c):>10}  {d:<13}{n(q['S']):>6}{n(q['D']):>6}{n(_a_rate[k]):>9}" for k, (c, d, q) in _a_pools.items()]
    + ["",
       "Overhead charged     S (10 000 units)    D (2 000 units)",
       f"Set-ups              {n(10 * 140_000):>12}    {n(20 * 140_000):>12}",
       f"Orders               {n(40 * 30_000):>12}    {n(60 * 30_000):>12}",
       f"Machine running      {n(6_000 * 800):>12}    {n(2_500 * 800):>12}",
       f"Total                {n(_a_abc['S']):>12}    {n(_a_abc['D']):>12}",
       f"Per unit             {n(_a_abc_u['S']):>12}    {n(_a_abc_u['D']):>12}",
       f"Traditional per unit {n(_a_trad_u['S']):>12}    {n(_a_trad_u['D']):>12}"]
)
_t_abcp = "\n".join([
    "Per unit (FCFA)          Standard chair   Deluxe chair",
    f"Selling price            {n(6_000):>14}   {n(12_000):>12}",
    f"Direct costs             {n(3_500):>14}   {n(7_000):>12}",
    f"Overhead - traditional   {n(1_000):>14}   {n(2_000):>12}",
    f"Profit - traditional     {n(_a_prof_t['S']):>14}   {n(_a_prof_t['D']):>12}",
    f"Overhead - ABC           {n(740):>14}   {n(3_300):>12}",
    f"Profit - ABC             {n(_a_prof_a['S']):>14}   {n(_a_prof_a['D']):>12}",
])
assert Fr(2_400_000, 30) == 80_000 and 12 * 80_000 == 960_000 and Fr(960_000, 3_000) == 320

LESSONS.append(lesson(
    module=M_COST, topic="Activity-based costing",
    title="Activity-based costing: cost pools, cost drivers and fairer product costs",
    slug="acu2-activity-based-costing", minutes=23,
    summary="Charge overheads to products through activities and their cost drivers, compare the result with a single labour-hour rate, "
            "and evaluate when activity-based costing is worth its cost.",
    objectives=[
        "Explain why a single absorption rate can distort product costs when overheads are driven by activities",
        "Group overheads into activity cost pools, choose cost drivers and calculate a cost driver rate",
        "Charge overheads to products by ABC and compare unit costs and profits with traditional absorption",
        "Evaluate the advantages and limitations of ABC",
    ],
    key_concepts=["Activity-based costing (ABC)", "Activity", "Cost pool", "Cost driver", "Cost driver rate", "Cross-subsidy between products"],
    blocks=[
        H("When one rate is not enough"),
        T("A furniture factory in Douala makes 10 000 standard chairs and 2 000 deluxe chairs. The deluxe chairs come in many colours, so the machines are reset often and many small orders for fabric are placed. "
          "If all overheads are charged by direct labour hours, the standard chairs pay for set-ups and orders caused by the deluxe range. **Activity-based costing (ABC)** corrects this. "
          "All figures are **invented for practice**."),
        D("**Activity-based costing** charges overheads to products according to the **activities** they cause. An **activity** is a task that uses resources (setting up a machine, placing an order). "
          "A **cost pool** collects the cost of one activity. A **cost driver** is the factor that causes the activity's cost to change (number of set-ups, number of orders, machine hours).",
          title="ABC vocabulary"),
        KEY("Four steps", "ABC replaces one rate with one rate per activity.",
            cards=[["1. Identify activities", "Group overheads into cost pools: set-ups, purchasing, machine running, quality control."],
                   ["2. Choose a driver", "For each pool, the factor that causes its cost."],
                   ["3. Driver rate", "Cost pool ÷ total quantity of the driver."],
                   ["4. Charge products", "Driver rate × driver quantity used by each product; divide by units for a cost per unit."]]),
        IMG("alacu2-abc-flow.svg",
            alt="Flow from overhead resources into three activity cost pools, each with its cost driver, then to the two products.",
            caption="Figure 1. Overheads flow through activity cost pools and cost drivers to products."),
        F(r"\text{cost driver rate} = \frac{\text{cost of the activity pool}}{\text{total quantity of the cost driver}}", title="Cost driver rate"),
        EX("Worked example 1: standard and deluxe chairs",
           intro="Overheads FCFA 14 000 000: machine set-ups 4 200 000 (set-ups: S 10, D 20); purchase orders 3 000 000 (orders: S 40, D 60); machine running 6 800 000 (machine hours: S 6 000, D 2 500). "
                 "Output: S 10 000 units using 5 000 direct labour hours; D 2 000 units using 2 000 hours. Compare the overhead per unit by a labour-hour rate and by ABC.",
           steps=[
               S("Traditional rate", text="14 000 000 ÷ 7 000 hours = 2 000 per hour. S: 0.5 h × 2 000 = 1 000 per unit. D: 1 h × 2 000 = 2 000 per unit."),
               S("Driver rates", text="Set-ups 4 200 000 ÷ 30 = 140 000; orders 3 000 000 ÷ 100 = 30 000; machine running 6 800 000 ÷ 8 500 = 800 per machine hour."),
               S("Charge S", text="10 × 140 000 + 40 × 30 000 + 6 000 × 800 = 1 400 000 + 1 200 000 + 4 800 000 = 7 400 000; per unit 740."),
               S("Charge D", text="20 × 140 000 + 60 × 30 000 + 2 500 × 800 = 2 800 000 + 1 800 000 + 2 000 000 = 6 600 000; per unit 3 300."),
               S("Check and compare", text="7 400 000 + 6 600 000 = 14 000 000. The labour-hour rate undercosted the deluxe chair by 1 300 a unit and overcosted the standard chair by 260."),
           ]),
        CODE(_t_abc, "text", title="ABC working (invented for practice)"),
        EX("Worked example 2: what it means for profit",
           intro="Selling prices: S 6 000, D 12 000. Direct costs per unit: S 3 500, D 7 000. Compare profit per unit under each method.",
           steps=[
               S("Traditional", text="S: 6 000 − 3 500 − 1 000 = 1 500. D: 12 000 − 7 000 − 2 000 = 3 000. The deluxe chair looks twice as profitable."),
               S("ABC", text="S: 6 000 − 3 500 − 740 = 1 760. D: 12 000 − 7 000 − 3 300 = 1 700."),
               S("Decision", text="The deluxe range is much less profitable than believed. Management could raise its price, reduce the number of set-ups (larger runs) or order fabric in bigger lots."),
           ]),
        CODE(_t_abcp, "text", title="Profit per unit under each method"),
        KEY("Evaluating ABC", "A balanced view for an essay or a 'discuss' question.",
            cards=[["Advantages", "More accurate product costs where overheads are large and products differ; better pricing and product-mix decisions; shows what causes costs, so managers can control the activities."],
                   ["Limitations", "Costly and time-consuming to set up and run; choosing drivers involves judgement; some costs (the director's salary, rent) have no clear driver and are still shared arbitrarily; little benefit for a firm with one simple product."]]),
        MISTAKE("Dividing a pool by the number of units produced",
                "Divide each pool by the total quantity of its **driver** (set-ups, orders, machine hours), not by units. Units come in only at the end, to find a cost per unit."),
        MISTAKE("Forgetting to check the total",
                "The overheads charged to all products must add back to the total overheads. If they do not, a driver quantity has been missed."),
        QUIZ("A quality-control pool costs FCFA 1 800 000 and there were 60 inspections: product A 15, product B 45. How much is charged to B?",
             ["450 000", "900 000", "1 350 000", "30 000"], 2,
             "Rate = 1 800 000 ÷ 60 = 30 000 per inspection; B: 45 × 30 000 = 1 350 000.",
             hint="Find the rate per inspection first.",
             feedback=["This is the charge to A.", "This splits the pool equally between the two products.", "", "This is the rate per inspection, not B's charge."]),
        QUIZ("ABC is most likely to change product costs significantly when",
             ["overheads are a large share of cost and products use activities very differently", "the firm makes one standard product",
              "almost all costs are direct materials", "all products use the same number of set-ups and orders per unit"], 0,
             "ABC matters when overheads are large and consumed unevenly; otherwise a single rate gives similar results.",
             feedback=["", "With one product all overheads go to it whatever the method.", "If overheads are small, re-allocating them changes little.",
                       "If products use activities in the same proportions, a single rate already charges them fairly."], title="Quick check 2"),
        TIP("ABC is a cost accounting topic for Paper 2 and for Paper 1 calculations (driver rates, charge to a product). In a written answer, finish with a comparison and a decision, not just numbers.", title="Exam link"),
        PQ("A purchasing pool costs FCFA 2 400 000 and 30 orders were placed. Product X needed 12 orders and 3 000 units were made. Find the purchasing cost per unit of X.",
           "Rate = 80 000 per order; X: 12 × 80 000 = 960 000; per unit 960 000 ÷ 3 000 = 320."),
        PQ("Explain why traditional absorption by labour hours tends to overcost high-volume simple products.",
           "Set-up and ordering costs depend on the number of batches and orders, not on labour hours. High-volume products use many labour hours but few set-ups, so a labour-hour rate loads them with costs caused by low-volume complex products."),
        PQ("Give two advantages and two limitations of ABC.",
           "Advantages: more accurate costs; better pricing and product decisions; shows cost causes for control. Limitations: expensive to operate; drivers involve judgement; some overheads have no clear driver; small benefit for simple firms."),
        SUM("ABC charges overheads through activities and the cost drivers that cause them.",
            "Steps: cost pools, cost drivers, driver rate = pool ÷ driver quantity, charge = rate × quantity used.",
            "Check that the overheads charged to all products add back to the total.",
            "A single rate often overcosts simple high-volume products and undercosts complex low-volume ones.",
            "ABC is more accurate but costlier; it is most useful when overheads are large and unevenly consumed."),
    ]))

# ====================================================================== 8. Marginal costing and break-even analysis
_m_p, _m_vprod, _m_vdist, _m_fc, _m_q = 5_000, 2_600, 400, 12_000_000, 8_000
_m_vc = _m_vprod + _m_vdist
_m_c = _m_p - _m_vc
_m_cs = Fr(_m_c, _m_p)
_m_sales = _m_q * _m_p
_m_cont = _m_q * _m_c
_m_prof = _m_cont - _m_fc
assert (_m_vc, _m_c, _m_cs, _m_sales, _m_cont, _m_prof) == (3_000, 2_000, Fr(2, 5), 40_000_000, 16_000_000, 4_000_000)
_m_beq = Fr(_m_fc, _m_c)
_m_bev = _m_fc / _m_cs
_m_mos = _m_sales - _m_bev
assert (_m_beq, _m_bev, _m_mos, Fr(_m_mos, _m_sales)) == (6_000, 30_000_000, 10_000_000, Fr(1, 4))
_m_bemonths = _m_bev / _m_sales * 12
assert _m_bemonths == 9
_m_tq = Fr(_m_fc + 6_000_000, _m_c)
assert _m_tq == 9_000 and Fr(_m_cont, _m_prof) == 4
_t_diff = "\n".join([
    "Differential operating statement (8 000 units)",
    r("Sales 8 000 x 5 000", None, _m_sales, w=36),
    r("Variable production costs", _m_q * _m_vprod, w=36),
    r("Variable distribution costs", _m_q * _m_vdist, w=36),
    r("Total variable costs", None, _m_q * _m_vc, w=36),
    r("Contribution (40% of sales)", None, _m_cont, w=36),
    r("Fixed costs", None, _m_fc, w=36),
    r("Operating result", None, _m_prof, w=36),
])
# limiting factor
_l = {"X": (1_200, 2, 1_000), "Y": (1_500, 3, 800), "Z": (1_000, 1, 1_500)}   # contribution/unit, hours/unit, demand
_l_hours = 5_000
_l_rank = sorted(_l, key=lambda k: -Fr(_l[k][0], _l[k][1]))
assert _l_rank == ["Z", "X", "Y"]
_l_left, _l_plan = _l_hours, {}
for k in _l_rank:
    c, h, d = _l[k]
    q = min(d, _l_left // h)
    _l_plan[k] = q
    _l_left -= q * h
_l_total = sum(_l_plan[k] * _l[k][0] for k in _l_plan)
assert _l_plan == {"Z": 1_500, "X": 1_000, "Y": 500} and _l_left == 0 and _l_total == 3_450_000
_t_lim = "\n".join([
    "Product  Contribution  Hours   Per hour  Rank  Units  Hours used",
    *[f"{k:<9}{n(_l[k][0]):>10}{_l[k][1]:>8}{n(Fr(_l[k][0], _l[k][1])):>10}{_l_rank.index(k) + 1:>6}{n(_l_plan[k]):>7}{n(_l_plan[k] * _l[k][1]):>10}"
      for k in ("X", "Y", "Z")],
    f"Total contribution = {n(_l_total)} FCFA; hours used = {n(_l_hours - _l_left)}",
])
# marginal v absorption
assert (10_000 - 8_000) * Fr(5_000_000, 10_000) == 1_000_000
assert Fr(9_000_000, 1_800) == 5_000 and Fr(9_000_000, Fr(1_800, 4_500)) == 22_500_000

LESSONS.append(lesson(
    module=M_COST, topic="Marginal costing and break-even analysis",
    title="Marginal costing and break-even analysis: contribution, margin of safety and limiting factors",
    slug="acu2-marginal-costing-break-even", minutes=28,
    summary="Separate variable and fixed costs to find contribution, prepare a differential operating statement, calculate the break-even point "
            "in value, quantity and date, the margin of safety and target sales, rank products under a limiting factor, and evaluate CVP analysis.",
    objectives=[
        "Prepare a differential operating statement and calculate contribution and the contribution/sales ratio",
        "Calculate the break-even point in units, in value and as a date, the margin of safety and the sales needed for a target profit",
        "Read and draw a break-even chart",
        "Rank products by contribution per unit of a limiting factor, and state the assumptions and limits of CVP analysis",
    ],
    key_concepts=["Marginal cost", "Contribution", "Contribution/sales ratio", "Differential operating statement", "Break-even point",
                  "Margin of safety", "Limiting factor", "Operating leverage"],
    blocks=[
        H("Why separate fixed and variable costs?"),
        T("A soap maker in Bafoussam asks: how many cartons must I sell before I stop losing money? Full costing cannot answer, because the fixed cost per carton changes with volume. "
          "**Marginal costing** keeps fixed costs as one block for the period and charges products with variable costs only. All figures are **invented for practice**."),
        D("The **marginal cost** of a unit is its variable cost. **Contribution** = sales − variable costs: it first covers fixed costs, then becomes profit. "
          "The **contribution/sales (C/S) ratio** (taux de marge sur coût variable) = contribution ÷ sales.", title="Marginal cost and contribution"),
        D("The **differential operating statement** (compte de résultat différentiel) sets out sales, variable costs (production and distribution), contribution, fixed costs and the result. "
          "It is the starting point of every break-even calculation.", title="Differential operating statement"),
        H("The break-even formulas"),
        F(r"\text{BEP (units)} = \frac{\text{fixed costs}}{\text{contribution per unit}} \qquad \text{BEP (value)} = \frac{\text{fixed costs}}{\text{C/S ratio}}", title="Break-even point"),
        F(r"\text{margin of safety} = \text{budgeted sales} - \text{break-even sales} \qquad \text{sales for target profit} = \frac{\text{fixed costs} + \text{target profit}}{\text{contribution per unit}}",
          title="Margin of safety and target profit"),
        T("Reasoning: each unit sold adds its contribution. Profit is zero when total contribution equals fixed costs, so divide fixed costs by contribution per unit. "
          "Above that volume every extra unit adds its full contribution to profit."),
        EX("Worked example 1: one product",
           intro="Selling price FCFA 5 000; variable production cost 2 600 and variable distribution cost 400 per unit; fixed costs FCFA 12 000 000 a year; budgeted sales 8 000 units spread evenly over the year from 1 January. "
                 "Prepare the differential operating statement and find the break-even point (units, value, date), the margin of safety and the units needed for a profit of FCFA 6 000 000.",
           steps=[
               S("Contribution", text="5 000 − 3 000 = 2 000 per unit; C/S ratio 2 000 ÷ 5 000 = 40%."),
               S("Statement", text="Sales 40 000 000 − variable costs 24 000 000 = contribution 16 000 000 − fixed costs 12 000 000 = profit 4 000 000."),
               S("Break-even", text="12 000 000 ÷ 2 000 = 6 000 units; 12 000 000 ÷ 0.40 = 30 000 000 FCFA."),
               S("Break-even date", text="30 000 000 ÷ 40 000 000 × 12 months = 9 months: break-even is reached at the end of September."),
               S("Margin of safety", text="40 000 000 − 30 000 000 = 10 000 000 FCFA (2 000 units), i.e. 25% of budgeted sales."),
               S("Target profit", text="(12 000 000 + 6 000 000) ÷ 2 000 = 9 000 units (45 000 000 FCFA)."),
           ], check=r"6\,000 \times 2\,000 = 12\,000\,000"),
        CODE(_t_diff, "text", title="Differential operating statement (invented for practice)"),
        IMG("alacu2-break-even-chart.svg",
            alt="Break-even chart: sales revenue line from the origin, total cost line starting at 12 million, fixed cost horizontal at 12 million; they cross at 6 000 units and 30 million; budget at 8 000 units; margin of safety between 6 000 and 8 000 units.",
            caption="Figure 1. Break-even chart for worked example 1."),
        T("**Operating leverage** = contribution ÷ profit = 16 000 000 ÷ 4 000 000 = 4: a 10% change in sales changes profit by about 40%. Firms with high fixed costs have high operating leverage, so their profit is more sensitive to sales."),
        H("Limiting factors"),
        D("A **limiting factor** (key factor) is a scarce resource that stops the firm from meeting all demand, such as machine hours, skilled labour or a material. "
          "To maximise profit, rank products by **contribution per unit of the limiting factor**, not by contribution per unit of product.", title="Limiting factor"),
        EX("Worked example 2: scarce machine hours",
           intro="Only 5 000 machine hours are available. X: contribution 1 200, 2 hours, demand 1 000 units. Y: contribution 1 500, 3 hours, demand 800. Z: contribution 1 000, 1 hour, demand 1 500. Find the best plan.",
           steps=[
               S("Contribution per hour", text="X 600; Y 500; Z 1 000. Rank: Z, X, Y."),
               S("Produce Z first", text="1 500 units × 1 h = 1 500 h; 3 500 h left."),
               S("Then X", text="1 000 units × 2 h = 2 000 h; 1 500 h left."),
               S("Then Y", text="1 500 h ÷ 3 = 500 units."),
               S("Total contribution", text="1 500 × 1 000 + 1 000 × 1 200 + 500 × 1 500 = 3 450 000."),
           ]),
        CODE(_t_lim, "text", title="Limiting factor plan"),
        T("Marginal and absorption costing give different profits when stock levels change, because absorption carries part of the fixed production overhead forward in closing stock. "
          "If 10 000 units are made, 8 000 sold and fixed production overhead is FCFA 5 000 000 (500 a unit), absorption profit is higher by 2 000 × 500 = 1 000 000."),
        KEY("Evaluating break-even analysis", "Useful, but built on simplifying assumptions.",
            cards=[["Uses", "Quick view of risk (margin of safety), pricing and volume decisions, effect of cost changes, target-profit planning."],
                   ["Assumptions", "Costs split exactly into fixed and variable; linear revenue and costs (constant price and variable cost per unit); sales = production; constant sales mix."],
                   ["Limits", "In reality discounts, overtime and bulk buying bend the lines; fixed costs step up at higher volumes; the analysis holds only within the relevant range."]]),
        MISTAKE("Dividing fixed costs by the selling price",
                "Break-even units = fixed costs ÷ **contribution** per unit. Using price ignores the variable cost of each unit."),
        MISTAKE("Ranking by contribution per unit when a factor is scarce",
                "Under a limiting factor, rank by contribution **per unit of the scarce resource**. In example 2, Y has the highest contribution per unit but comes last."),
        QUIZ("Fixed costs FCFA 9 000 000; price FCFA 4 500; variable cost FCFA 2 700. The break-even point is",
             ["2 000 units", "3 333 units", "5 000 units", "1 800 units"], 2,
             "Contribution 1 800; 9 000 000 ÷ 1 800 = 5 000 units.",
             hint="Find the contribution per unit first.",
             feedback=["This divides by the selling price (9 000 000 ÷ 4 500).", "This divides by the variable cost.", "", "This is the contribution per unit, not the break-even point."]),
        QUIZ("Budgeted sales FCFA 60 000 000; break-even sales FCFA 45 000 000. The margin of safety as a percentage of budgeted sales is",
             ["25%", "33.3%", "75%", "15%"], 0,
             "(60 − 45) ÷ 60 = 25%.",
             feedback=["", "This divides by break-even sales instead of budgeted sales.", "This is break-even sales as a percentage of budget.", "This is the margin in millions, not a percentage."], title="Quick check 2"),
        TIP("Break-even analysis is in Paper 2, and the Board's 2023 report describes a compulsory question asking for a differential operating table, break-even in value and quantity and the sales needed for a given profit. "
            "Always start with the differential statement and show the C/S ratio.", title="Exam link"),
        PQ("Fixed costs FCFA 9 000 000; C/S ratio 40%. Budgeted sales FCFA 30 000 000 spread evenly over 12 months. Find break-even sales, the margin of safety and the break-even date.",
           "Break-even = 9 000 000 ÷ 0.4 = 22 500 000. Margin of safety = 7 500 000 (25%). Date = 22.5 ÷ 30 × 12 = 9 months: end of September."),
        PQ("Price FCFA 3 000; variable cost FCFA 1 800; fixed costs FCFA 6 000 000. How many units give a profit of FCFA 2 400 000?",
           "Contribution 1 200. (6 000 000 + 2 400 000) ÷ 1 200 = 7 000 units."),
        PQ("Two products use a scarce material: A gives contribution 2 400 using 4 kg; B gives contribution 1 800 using 2 kg. Which should be made first? Explain.",
           "Contribution per kg: A 600, B 900. Make B first, because each scarce kilogram earns more contribution in B."),
        PQ("State three assumptions of break-even analysis and one way in which reality may differ from each.",
           "Constant price (discounts for bulk sales); constant variable cost per unit (bulk-buying discounts or overtime); fixed costs fixed (a new machine steps them up); sales equal production (stock changes)."),
        SUM("Contribution = sales − variable costs; C/S ratio = contribution ÷ sales.",
            "Break-even units = fixed costs ÷ contribution per unit; break-even value = fixed costs ÷ C/S ratio.",
            "Margin of safety = budgeted − break-even sales; target sales = (fixed costs + target profit) ÷ contribution per unit.",
            "Under a limiting factor, rank products by contribution per unit of the scarce resource.",
            "CVP relies on linear costs and revenue, a fixed/variable split and a constant mix; use it within the relevant range."),
    ]))

# ====================================================================== 9. Budgets and the cash budget
_u_sales = {"Jan": 1_000, "Feb": 1_200, "Mar": 1_500, "Apr": 1_400}
_u_open = 200
_u_months = ["Jan", "Feb", "Mar"]
_u_prod, _u_stock = {}, _u_open
for i, m in enumerate(_u_months):
    close = _u_sales[["Feb", "Mar", "Apr"][i]] * 20 // 100
    _u_prod[m] = _u_sales[m] + close - _u_stock
    _u_stock = close
assert _u_prod == {"Jan": 1_040, "Feb": 1_260, "Mar": 1_480}
_t_prodb = "\n".join([
    "Production budget (units)     Jan     Feb     Mar",
    "Sales                       1 000   1 200   1 500",
    "+ Closing stock (20% next)    240     300     280",
    "- Opening stock               200     240     300",
    f"Production                  {n(_u_prod['Jan']):>5}   {n(_u_prod['Feb']):>5}   {n(_u_prod['Mar']):>5}",
])
_v_price = 2_000
_v_sales = {"Dec": 1_800_000, **{m: _u_sales[m] * _v_price for m in _u_months}}
_v_rec = {}
for prev, m in zip(["Dec", "Jan", "Feb"], _u_months):
    _v_rec[m] = _v_sales[m] * 30 // 100 + _v_sales[prev] * 70 // 100
assert _v_rec == {"Jan": 1_860_000, "Feb": 2_120_000, "Mar": 2_580_000}
_v_mat = {"Jan": 500_000, "Feb": _u_prod["Jan"] * 500, "Mar": _u_prod["Feb"] * 500}
_v_wag = {m: _u_prod[m] * 400 for m in _u_months}
_v_fix = {m: 300_000 - 50_000 for m in _u_months}
_v_eqp = {"Jan": 0, "Feb": 1_500_000, "Mar": 0}
_v_pay = {m: _v_mat[m] + _v_wag[m] + _v_fix[m] + _v_eqp[m] for m in _u_months}
assert _v_pay == {"Jan": 1_166_000, "Feb": 2_774_000, "Mar": 1_472_000}
_v_bal, _v_open = {}, 200_000
_v_o = {}
for m in _u_months:
    _v_o[m] = _v_open
    _v_bal[m] = _v_open + _v_rec[m] - _v_pay[m]
    _v_open = _v_bal[m]
assert _v_bal == {"Jan": 894_000, "Feb": 240_000, "Mar": 1_348_000}


def _row(label, d):
    return f"{label:<26}" + "".join(f"{n(d[m]):>11}" for m in _u_months)


_t_cash = "\n".join([
    f"{'Cash budget (FCFA)':<26}" + "".join(f"{m:>11}" for m in _u_months),
    _row("Opening balance", _v_o),
    _row("Receipts from customers", _v_rec),
    _row("Payments: materials", _v_mat),
    _row("Payments: wages", _v_wag),
    _row("Payments: fixed expenses", _v_fix),
    _row("Payments: equipment", _v_eqp),
    _row("Total payments", _v_pay),
    _row("Closing balance", _v_bal),
])
_vat_c = Fr(2_000_000 * 1925, 10_000)
_vat_d = Fr(520_000 * 1925, 10_000)
assert (_vat_c, _vat_d, _vat_c - _vat_d) == (385_000, 100_100, 284_900)

LESSONS.append(lesson(
    module=M_BUD, topic="Budgets and the cash budget",
    title="The master budget and the cash budget",
    slug="acu2-budgets-cash-budget", minutes=27,
    summary="Explain the purposes of budgeting, build the functional budgets in order (sales, production, purchases, VAT) and prepare a monthly "
            "cash budget with credit sales, timing of payments and non-cash items left out.",
    objectives=[
        "Explain the purposes and benefits of budgeting and identify the principal budget factor",
        "Prepare sales and production budgets, linking production to planned stock levels",
        "Prepare a monthly cash budget with credit sales and delayed payments, excluding non-cash items such as depreciation",
        "Calculate the VAT payable for a month and place it in the cash budget, and interpret the budget's results",
    ],
    key_concepts=["Budget", "Master budget", "Principal budget factor", "Sales budget", "Production budget", "VAT budget",
                  "Cash budget", "Timing of receipts and payments"],
    blocks=[
        H("Planning in money terms"),
        T("A juice maker in Bafoussam expects big sales in the dry season and a large equipment purchase in February. Will there be enough cash to pay the workers every month? "
          "A **budget** answers questions like this before they become emergencies. All figures are **invented for practice**."),
        D("A **budget** is a plan for a future period expressed in money and quantities. The **master budget** brings together the functional budgets (sales, production, purchases, labour, overheads, VAT), "
          "the **cash budget** and the budgeted income statement and balance sheet.", title="Budget and master budget"),
        KEY("Why budget?", "These are the benefits examiners expect; the Board's 2023 report notes that a question asking for the benefits of budgets and a cash budget was among the least well answered.",
            cards=[["Planning", "Forces managers to think ahead and anticipate problems such as a cash shortage."],
                   ["Coordination and communication", "Links departments (sales, production, purchasing) and tells each what is expected."],
                   ["Motivation and responsibility", "Gives targets to managers who help set them."],
                   ["Control", "Actual results are compared with budget; variances show where to act."]]),
        D("The **principal budget factor** is the factor that limits the firm's activity, usually sales demand (sometimes a machine capacity or a material). "
          "Its budget is prepared first and every other budget follows from it.", title="Principal budget factor"),
        H("From sales to production"),
        F(r"\text{production} = \text{sales} + \text{closing stock} - \text{opening stock}", title="Production budget"),
        EX("Worked example 1: production budget",
           intro="Sales: January 1 000, February 1 200, March 1 500, April 1 400 units. Closing stock of finished goods each month is 20% of the next month's sales; opening stock in January is 200 units. Prepare the production budget for January to March.",
           steps=[
               S("January", text="1 000 + 20% × 1 200 − 200 = 1 000 + 240 − 200 = 1 040."),
               S("February", text="1 200 + 20% × 1 500 − 240 = 1 260."),
               S("March", text="1 500 + 20% × 1 400 − 300 = 1 480."),
           ]),
        CODE(_t_prodb, "text", title="Production budget (invented for practice)"),
        H("The cash budget"),
        D("A **cash budget** shows, month by month, the opening cash balance, the cash **receipts** and **payments** expected in that month, and the closing balance. "
          "It records cash when it moves, not when the sale or expense is earned or incurred. **Depreciation** and other non-cash items never appear.", title="Cash budget"),
        EX("Worked example 2: cash budget for January to March",
           intro="Price FCFA 2 000 a unit. 30% of sales are for cash; 70% are paid the following month (December sales were FCFA 1 800 000). Materials cost FCFA 500 a unit produced and are paid the month after purchase (December's bill: FCFA 500 000). "
                 "Wages FCFA 400 a unit produced, paid the same month. Fixed expenses FCFA 300 000 a month including depreciation of FCFA 50 000. Equipment costing FCFA 1 500 000 is paid in February. Opening cash FCFA 200 000. Use the production budget above.",
           steps=[
               S("Receipts", text="Jan: 30% × 2 000 000 + 70% × 1 800 000 = 600 000 + 1 260 000 = 1 860 000. Feb: 720 000 + 1 400 000 = 2 120 000. Mar: 900 000 + 1 680 000 = 2 580 000."),
               S("Materials (one month later)", text="Jan 500 000 (December); Feb 1 040 × 500 = 520 000; Mar 1 260 × 500 = 630 000."),
               S("Wages (same month)", text="Jan 1 040 × 400 = 416 000; Feb 504 000; Mar 592 000."),
               S("Fixed expenses", text="300 000 − 50 000 depreciation = 250 000 cash each month."),
               S("Balances", text="Jan: 200 000 + 1 860 000 − 1 166 000 = 894 000. Feb: 894 000 + 2 120 000 − 2 774 000 = 240 000. Mar: 240 000 + 2 580 000 − 1 472 000 = 1 348 000."),
           ]),
        CODE(_t_cash, "text", title="Cash budget (invented for practice)"),
        T("Interpretation: cash stays positive, but the equipment purchase pulls February down to 240 000, a thin cushion. Management could arrange an overdraft facility in advance, pay for the equipment in instalments, or push customers to pay faster."),
        H("The VAT budget"),
        T("When sales and purchases are subject to VAT, the firm collects VAT on its sales and deducts VAT on its purchases; the difference is paid to the tax administration, normally in the month after the transactions. "
          "This lesson uses **19.25%** as a teaching rate (it is the rate usually quoted for Cameroon); check the current Finance Law and your textbook for the rate and the payment date."),
        EX("Worked example 3: VAT payable",
           intro="January sales excluding VAT FCFA 2 000 000; January purchases excluding VAT FCFA 520 000. VAT at 19.25% (teaching rate). Find the VAT to pay in February.",
           steps=[
               S("VAT collected", text="19.25% × 2 000 000 = 385 000."),
               S("VAT deductible", text="19.25% × 520 000 = 100 100."),
               S("VAT payable in February", text="385 000 − 100 100 = 284 900. In a cash budget with VAT, receipts and payments are shown including VAT and this amount is a February payment."),
           ]),
        MISTAKE("Putting depreciation in the cash budget",
                "Depreciation is not a payment. Only the cash paid for the asset (when it is bought) appears."),
        MISTAKE("Recording credit sales in the month of sale",
                "Cash from credit sales arrives when the customer pays. Split each month's sales by the payment pattern and place each part in the right month."),
        MISTAKE("Forgetting the opening balance or carrying the wrong one forward",
                "Each month's closing balance is the next month's opening balance. Check the chain from the first month to the last."),
        QUIZ("Sales: May FCFA 4 000 000, June FCFA 5 000 000. 40% are cash sales and 60% are received the following month. Cash received in June is",
             ["4 400 000", "5 000 000", "4 600 000", "3 000 000"], 0,
             "40% × 5 000 000 + 60% × 4 000 000 = 2 000 000 + 2 400 000 = 4 400 000.",
             hint="June receives part of June's sales and part of May's.",
             feedback=["", "This assumes all June sales are received in June.", "This applies 60% to June and 40% to May.", "This is only the credit part of June's sales."]),
        QUIZ("Which item should NOT appear in a cash budget?",
             ["Wages paid", "Depreciation of machinery", "Purchase of a delivery van paid in cash", "Loan received from the bank"], 1,
             "Depreciation is a non-cash expense.",
             feedback=["Wages are paid in cash.", "", "Paying for a van is a cash outflow, even though it is a capital item.", "A loan received is a cash inflow."], title="Quick check 2"),
        TIP("Budgets and cash budgets are management accounting topics for Paper 2 (Section B). The 2023 report says the cash budget question was among the least popular and least well answered, "
            "so practise full monthly layouts: opening balance, receipts, payments, closing balance.", title="Exam link"),
        PQ("Sales budget 5 000 units; opening stock 600; required closing stock 800. Find the production budget.",
           "5 000 + 800 − 600 = 5 200 units."),
        PQ("Purchases: March FCFA 900 000, April FCFA 1 100 000. Suppliers are paid 50% in the month of purchase and 50% one month later. Find the payment in April.",
           "50% × 1 100 000 + 50% × 900 000 = 550 000 + 450 000 = 1 000 000."),
        PQ("Give four benefits of budgeting.",
           "Planning ahead; coordination of departments; communication of targets; motivation through agreed targets; control by comparing actual with budget; authorisation of spending."),
        PQ("A cash budget shows a deficit of FCFA 2 000 000 in August only. Suggest two actions and one risk of each.",
           "Arrange a short overdraft (interest cost); delay a capital purchase (lost production); offer customers a discount for early payment (lower revenue); ask suppliers for longer credit (damaged relations)."),
        SUM("A budget is a plan in money and quantities; the master budget combines functional budgets, the cash budget and budgeted statements.",
            "Start from the principal budget factor, usually sales.",
            "Production = sales + closing stock − opening stock.",
            "The cash budget records cash when it moves: split credit sales and delayed payments; leave out depreciation.",
            "VAT payable = VAT collected − VAT deductible, usually paid the following month (check the current rules)."),
    ]))

# ====================================================================== 10. Flexible budgets
_x_bq, _x_aq = 10_000, 9_000
_x_unit = {"Direct materials": 200, "Direct labour": 150, "Variable overhead": 50}
_x_fixed = 1_200_000
_x_mfix, _x_mvar = 200_000, 40
_x_price = 1_000


def _x_budget(q):
    d = {k: v * q for k, v in _x_unit.items()}
    d["Maintenance (semi-variable)"] = _x_mfix + _x_mvar * q
    d["Fixed overhead"] = _x_fixed
    return d


_x_fixedb, _x_flex = _x_budget(_x_bq), _x_budget(_x_aq)
_x_actual = {"Direct materials": 1_850_000, "Direct labour": 1_320_000, "Variable overhead": 470_000,
             "Maintenance (semi-variable)": 570_000, "Fixed overhead": 1_250_000}
_x_asales, _x_fsales, _x_bsales = 8_910_000, _x_aq * _x_price, _x_bq * _x_price
_x_bprof = _x_bsales - sum(_x_fixedb.values())
_x_fprof = _x_fsales - sum(_x_flex.values())
_x_aprof = _x_asales - sum(_x_actual.values())
assert (_x_bprof, _x_fprof, _x_aprof) == (4_200_000, 3_640_000, 3_450_000)
_x_var = {k: _x_flex[k] - _x_actual[k] for k in _x_flex}
assert _x_var == {"Direct materials": -50_000, "Direct labour": 30_000, "Variable overhead": -20_000,
                  "Maintenance (semi-variable)": -10_000, "Fixed overhead": -50_000}
_x_svol = _x_fprof - _x_bprof
_x_cont = _x_price - sum(_x_unit.values()) - _x_mvar
assert _x_cont == 560 and _x_svol == -(_x_bq - _x_aq) * _x_cont == -560_000
assert _x_aprof - _x_bprof == _x_svol + (_x_asales - _x_fsales) + sum(_x_var.values()) == -750_000


def _fa(v):
    return "0" if v == 0 else f"{n(abs(v))} {'F' if v > 0 else 'A'}"


_t_flex = "\n".join(
    [f"{'(FCFA)':<28}{'Fixed':>11}{'Flexed':>11}{'Actual':>11}{'Variance':>12}",
     f"{'Units':<28}{n(_x_bq):>11}{n(_x_aq):>11}{n(_x_aq):>11}",
     f"{'Sales':<28}{n(_x_bsales):>11}{n(_x_fsales):>11}{n(_x_asales):>11}{_fa(_x_asales - _x_fsales):>12}"]
    + [f"{k:<28}{n(_x_fixedb[k]):>11}{n(_x_flex[k]):>11}{n(_x_actual[k]):>11}{_fa(_x_var[k]):>12}" for k in _x_flex]
    + [f"{'Profit':<28}{n(_x_bprof):>11}{n(_x_fprof):>11}{n(_x_aprof):>11}{_fa(_x_aprof - _x_fprof):>12}"]
)
assert 300_000 + 25 * 12_000 == 600_000 and 300_000 + 25 * 9_000 == 525_000

LESSONS.append(lesson(
    module=M_BUD, topic="Flexible budgets",
    title="Flexible budgets: comparing like with like",
    slug="acu2-flexible-budgets", minutes=24,
    summary="Flex the budget to the actual level of activity using cost behaviour (variable, fixed, semi-variable), calculate and label "
            "favourable and adverse variances, separate the sales volume effect, and use the results for budgetary control.",
    objectives=[
        "Explain why a fixed budget is a poor yardstick when actual activity differs from budget",
        "Prepare a flexible budget at the actual level of activity, including semi-variable costs",
        "Calculate favourable and adverse variances against the flexed budget and the sales volume effect",
        "Explain budgetary control, management by exception and the behavioural side of budgets",
    ],
    key_concepts=["Fixed budget", "Flexible budget", "Flexing", "Variance", "Favourable and adverse", "Sales volume variance",
                  "Budgetary control", "Management by exception"],
    blocks=[
        H("Why a fixed budget can mislead"),
        T("A factory planned to make 10 000 crates but made 9 000 because a supplier was late. Its actual material cost is lower than budget. Has the production manager saved money? Not necessarily: "
          "fewer crates should use less material anyway. A fair comparison needs a budget for the 9 000 crates actually made. All figures are **invented for practice**."),
        D("A **fixed budget** is prepared for one planned level of activity. A **flexible budget** is recalculated (**flexed**) for the actual level of activity, using how each cost behaves: "
          "variable costs change in proportion, fixed costs stay the same, semi-variable costs keep their fixed part and change their variable part.", title="Fixed and flexible budgets"),
        F(r"\text{flexed cost} = \text{fixed part} + \text{variable cost per unit} \times \text{actual units}", title="Flexing a cost"),
        D("A **variance** is the difference between actual and budgeted (flexed) results. It is **favourable (F)** if it increases profit (lower cost, higher revenue) and **adverse (A)** if it reduces profit.",
          title="Variance"),
        EX("Worked example 1: flexing to 9 000 units",
           intro="Budget for 10 000 units: materials 200, labour 150 and variable overhead 50 per unit; maintenance 200 000 fixed + 40 per unit; fixed overhead 1 200 000; price 1 000. "
                 "Actual: 9 000 units sold for 8 910 000; materials 1 850 000; labour 1 320 000; variable overhead 470 000; maintenance 570 000; fixed overhead 1 250 000. Prepare the flexible budget and the variances.",
           steps=[
               S("Flex the variable items", text="Materials 9 000 × 200 = 1 800 000; labour 1 350 000; variable overhead 450 000."),
               S("Flex the semi-variable item", text="Maintenance 200 000 + 40 × 9 000 = 560 000."),
               S("Fixed items", text="Fixed overhead stays 1 200 000. Flexed sales 9 000 × 1 000 = 9 000 000. Flexed profit 3 640 000."),
               S("Variances", text="Sales price 90 000 A; materials 50 000 A; labour 30 000 F; variable overhead 20 000 A; maintenance 10 000 A; fixed overhead 50 000 A. Total 190 000 A."),
               S("Check", text="Flexed profit 3 640 000 − 190 000 = actual profit 3 450 000."),
           ]),
        CODE(_t_flex, "text", title="Fixed, flexed and actual (invented for practice)"),
        H("The sales volume effect"),
        T("The original (fixed) budget profit was 4 200 000; the flexed profit is 3 640 000. The difference of 560 000 A is the **sales volume variance**: 1 000 units fewer, each losing a contribution of "
          "1 000 − (200 + 150 + 50 + 40) = 560. Total change in profit = 560 000 A (volume) + 190 000 A (prices and costs) = 750 000 A, which reconciles the budgeted 4 200 000 with the actual 3 450 000."),
        KEY("Budgetary control", "Budgets are used to control, not only to plan.",
            cards=[["Compare", "Actual results against the flexed budget, line by line."],
                   ["Investigate", "Management by exception: look into significant variances, favourable and adverse, and find causes."],
                   ["Act", "Correct the cause, or revise the budget if conditions have changed permanently."],
                   ["People", "Budgets that managers help to set motivate; imposed or unrealistic budgets can lead to padding (budgetary slack) and short-term behaviour."]]),
        EX("Worked example 2: interpreting the variances",
           intro="Explain two of the variances in worked example 1 and suggest who should investigate them.",
           steps=[
               S("Materials 50 000 A", text="More material used or higher prices than standard: the purchasing manager (price) or the production manager (wastage) should explain."),
               S("Labour 30 000 F", text="Less labour cost for 9 000 units: perhaps fewer overtime hours. Check that quality has not suffered."),
               S("Sales price 90 000 A", text="The average price was 990 instead of 1 000, perhaps discounts to win orders: the sales manager should explain."),
           ]),
        MISTAKE("Comparing actual costs with the fixed budget",
                "A lower cost at lower output is not a saving. Flex the budget to actual output first, then compare."),
        MISTAKE("Flexing fixed costs",
                "Fixed costs do not change with activity in the relevant range. Only the variable part of a semi-variable cost is flexed."),
        MISTAKE("Calling every variance below budget 'favourable'",
                "For costs, actual below budget is favourable; for revenue, actual below budget is adverse. Always ask: does it raise or lower profit?"),
        QUIZ("A semi-variable cost is FCFA 300 000 fixed plus FCFA 25 per unit. Budget was 12 000 units; actual output 9 000 units. The flexed cost is",
             ["600 000", "525 000", "450 000", "225 000"], 1,
             "300 000 + 25 × 9 000 = 525 000.",
             hint="Keep the fixed part; flex only the variable part.",
             feedback=["This is the cost at the budgeted 12 000 units.", "", "This flexes the whole 600 000 in proportion (9/12), including the fixed part.", "This forgets the fixed part."]),
        QUIZ("Flexed sales revenue FCFA 9 000 000; actual sales revenue FCFA 8 910 000. The sales price variance is",
             ["90 000 favourable", "90 000 adverse", "8 910 000 adverse", "0, because the volume is the same"], 1,
             "Actual revenue is lower than flexed revenue at the same volume, which reduces profit: adverse.",
             feedback=["Lower revenue reduces profit, so it is adverse.", "", "The variance is the difference, not the actual revenue.",
                       "The volume is the same, which is why the difference is due to price."], title="Quick check 2"),
        TIP("Flexible budgets and budgetary control belong to Paper 2, Section B (management accounting). Set out columns for fixed budget, flexed budget, actual and variance, and mark every variance F or A.", title="Exam link"),
        PQ("Variable cost FCFA 800 a unit; fixed costs FCFA 2 000 000. Budget 5 000 units; actual 4 600 units with total cost FCFA 5 750 000. Find the flexed cost and the total cost variance.",
           "Flexed cost = 2 000 000 + 800 × 4 600 = 5 680 000. Variance = 5 680 000 − 5 750 000 = 70 000 A."),
        PQ("Budget: 8 000 units, price 1 500, variable cost 900. Actual: 7 500 units. Find the sales volume variance in profit terms.",
           "Contribution per unit 600; 500 units fewer × 600 = 300 000 A."),
        PQ("Explain 'management by exception'.",
           "Managers concentrate on significant variances (beyond a set percentage or amount) instead of every line, which saves time and directs attention to what needs action."),
        SUM("A fixed budget is for one activity level; a flexible budget is recalculated for actual activity.",
            "Flex variable costs in proportion, keep fixed costs, flex only the variable part of semi-variable costs.",
            "Variance = flexed − actual for costs; label F if it raises profit, A if it lowers it.",
            "Fixed-budget profit − sales volume variance ± flexed variances = actual profit.",
            "Budgetary control: compare, investigate significant variances, act; involve managers to avoid slack."),
    ]))

# ====================================================================== 11. Standard costing and variances
# standard card per unit
_y_sq, _y_sp = 4, 500          # kg per unit, FCFA per kg
_y_sh, _y_sr = 2, 1_200        # hours per unit, FCFA per hour
_y_vr = 300                    # variable overhead per hour
_y_bfoh, _y_bunits = 4_000_000, 2_500
_y_fr = Fr(_y_bfoh, _y_bunits * _y_sh)               # fixed overhead per hour
assert _y_fr == 800
_y_std_unit = _y_sq * _y_sp + _y_sh * _y_sr + _y_sh * _y_vr + _y_sh * _y_fr
assert _y_std_unit == 6_600
# actual
_y_out, _y_aq, _y_amat, _y_ah, _y_alab, _y_avoh, _y_afoh = 2_400, 9_900, 5_049_000, 4_700, 5_781_000, 1_457_000, 4_100_000
_y_ap, _y_ar = Fr(_y_amat, _y_aq), Fr(_y_alab, _y_ah)
assert (_y_ap, _y_ar) == (510, 1_230)
_y_sqa, _y_sha = _y_out * _y_sq, _y_out * _y_sh
V = {
    "mat_price": (_y_sp - _y_ap) * _y_aq,
    "mat_usage": (_y_sqa - _y_aq) * _y_sp,
    "lab_rate": (_y_sr - _y_ar) * _y_ah,
    "lab_eff": (_y_sha - _y_ah) * _y_sr,
    "voh_exp": _y_ah * _y_vr - _y_avoh,
    "voh_eff": (_y_sha - _y_ah) * _y_vr,
    "foh_exp": _y_bfoh - _y_afoh,
    "foh_vol": (_y_out - _y_bunits) * _y_sh * _y_fr,
    "foh_cap": (_y_ah - _y_bunits * _y_sh) * _y_fr,
    "foh_eff": (_y_sha - _y_ah) * _y_fr,
}
assert V == {"mat_price": -99_000, "mat_usage": -150_000, "lab_rate": -141_000, "lab_eff": 120_000, "voh_exp": -47_000,
             "voh_eff": 30_000, "foh_exp": -100_000, "foh_vol": -160_000, "foh_cap": -240_000, "foh_eff": 80_000}
assert V["foh_cap"] + V["foh_eff"] == V["foh_vol"]
_y_std_total = _y_out * _y_std_unit
_y_act_total = _y_amat + _y_alab + _y_avoh + _y_afoh
_y_tot = sum(V[k] for k in ("mat_price", "mat_usage", "lab_rate", "lab_eff", "voh_exp", "voh_eff", "foh_exp", "foh_vol"))
assert (_y_std_total, _y_act_total, _y_tot) == (15_840_000, 16_387_000, -547_000) and _y_std_total - _y_act_total == _y_tot


def _fa2(v):
    return f"{n(abs(v))} {'F' if v > 0 else 'A'}"


_t_card = "\n".join([
    "Standard cost card - one unit",
    r("Materials 4 kg x 500", 2_000, w=34),
    r("Labour 2 h x 1 200", 2_400, w=34),
    r("Variable overhead 2 h x 300", 600, w=34),
    r("Fixed overhead 2 h x 800", 1_600, w=34),
    r("Standard cost per unit", None, _y_std_unit, w=34),
    "Budget: 2 500 units, 5 000 hours, fixed overhead 4 000 000",
])
_t_comp = "\n".join([
    "Table of comparison for actual output of 2 400 units",
    f"{'Element':<18}{'Standard':>12}{'Actual':>12}{'Variance':>13}",
    f"{'Materials':<18}{n(_y_sqa * _y_sp):>12}{n(_y_amat):>12}{_fa2(V['mat_price'] + V['mat_usage']):>13}",
    f"{'Labour':<18}{n(_y_sha * _y_sr):>12}{n(_y_alab):>12}{_fa2(V['lab_rate'] + V['lab_eff']):>13}",
    f"{'Variable overhead':<18}{n(_y_sha * _y_vr):>12}{n(_y_avoh):>12}{_fa2(V['voh_exp'] + V['voh_eff']):>13}",
    f"{'Fixed overhead':<18}{n(_y_out * 1_600):>12}{n(_y_afoh):>12}{_fa2(V['foh_exp'] + V['foh_vol']):>13}",
    f"{'Total':<18}{n(_y_std_total):>12}{n(_y_act_total):>12}{_fa2(_y_tot):>13}",
])
_t_split = "\n".join([
    "Analysis of the variances (F = favourable, A = adverse)",
    f"Material price      (500 - 510) x 9 900        {_fa2(V['mat_price']):>11}",
    f"Material usage      (9 600 - 9 900) x 500      {_fa2(V['mat_usage']):>11}",
    f"Labour rate         (1 200 - 1 230) x 4 700    {_fa2(V['lab_rate']):>11}",
    f"Labour efficiency   (4 800 - 4 700) x 1 200    {_fa2(V['lab_eff']):>11}",
    f"Var. OH expenditure 4 700 x 300 - 1 457 000    {_fa2(V['voh_exp']):>11}",
    f"Var. OH efficiency  (4 800 - 4 700) x 300      {_fa2(V['voh_eff']):>11}",
    f"Fixed OH expend.    4 000 000 - 4 100 000      {_fa2(V['foh_exp']):>11}",
    f"Fixed OH volume     (2 400 - 2 500) x 1 600    {_fa2(V['foh_vol']):>11}",
    f"Total                                          {_fa2(_y_tot):>11}",
])
assert (300 - 320) * 5_200 == -104_000 and (1_200 * 4 - 5_200) * 300 == -120_000
assert (1_000 - 950) * 3_100 == 155_000 and (3_000 - 3_100) * 1_000 == -100_000

LESSONS.append(lesson(
    module=M_BUD, topic="Standard costing and variances",
    title="Standard costing: material, labour and overhead variances",
    slug="acu2-standard-costing-variances", minutes=28,
    summary="Set standard costs, prepare a table of comparison for the actual output, split the cost variances into price and quantity effects "
            "(materials, labour, variable and fixed overhead) and interpret their causes and interrelationships.",
    objectives=[
        "Explain what a standard cost is and how a standard cost card is built",
        "Prepare a table of comparison between standard cost of actual output and actual cost",
        "Calculate material price and usage, labour rate and efficiency, variable overhead and fixed overhead (expenditure, volume) variances",
        "Interpret variances, link causes between them and explain the limits of standard costing",
    ],
    key_concepts=["Standard cost", "Standard cost card", "Table of comparison", "Price (rate) variance", "Quantity (usage, efficiency) variance",
                  "Fixed overhead expenditure and volume variances", "Favourable and adverse"],
    blocks=[
        H("Measuring performance against a yardstick"),
        T("A furniture maker sets a standard: each cupboard should use 4 kg of glue-board at FCFA 500 a kg and 2 hours of labour at FCFA 1 200. At the end of the month the costs are higher than expected. "
          "Was it the price of the board, wasted board, slow workers or higher wages? **Standard costing** separates these causes. All figures are **invented for practice**."),
        D("A **standard cost** is a carefully predetermined cost of one unit under efficient conditions: a standard **quantity** of each input multiplied by a standard **price**. "
          "The **standard cost card** lists them. Actual results are compared with the **standard cost of the actual output**, not with the budget for planned output.", title="Standard cost"),
        CODE(_t_card, "text", title="Standard cost card (invented for practice)"),
        KEY("Every cost variance splits into two parts", "A price effect and a quantity effect. Notation: SP standard price, AP actual price, SQ standard quantity for actual output, AQ actual quantity.",
            cards=[["Materials", "Price = (SP − AP) × AQ. Usage = (SQ − AQ) × SP."],
                   ["Labour", "Rate = (SR − AR) × actual hours. Efficiency = (standard hours for actual output − actual hours) × SR."],
                   ["Variable overhead", "Expenditure = actual hours × standard rate − actual cost. Efficiency = (standard hours − actual hours) × standard rate."],
                   ["Fixed overhead", "Expenditure = budgeted − actual. Volume = (actual output − budgeted output) × standard fixed cost per unit; it splits into capacity and efficiency."]]),
        IMG("alacu2-variance-tree.svg",
            alt="Tree diagram: the total cost variance splits into materials, labour, variable overhead and fixed overhead; each splits into a price-type and a quantity-type variance; the fixed overhead volume variance splits into capacity and efficiency.",
            caption="Figure 1. The cost variances and how they fit together."),
        T("Sign conventions differ. In the approach used here a positive figure is **favourable** (it raises profit) and a negative one **adverse**. "
          "Many OHADA (French-language) textbooks calculate écart = actual − standard, so a positive écart is unfavourable. Use your textbook's convention and always write F or A."),
        EX("Worked example 1: the table of comparison",
           intro="Actual output 2 400 units. Materials: 9 900 kg bought and used, cost FCFA 5 049 000. Labour: 4 700 hours, paid FCFA 5 781 000. Variable overhead FCFA 1 457 000. Fixed overhead FCFA 4 100 000. "
                 "Use the standard card above. Compare standard cost of actual output with actual cost.",
           steps=[
               S("Standard quantities for 2 400 units", text="Materials 2 400 × 4 = 9 600 kg; labour 2 400 × 2 = 4 800 hours."),
               S("Standard cost of actual output", text="Materials 4 800 000; labour 5 760 000; variable overhead 1 440 000; fixed overhead 3 840 000; total 2 400 × 6 600 = 15 840 000."),
               S("Actual cost", text="5 049 000 + 5 781 000 + 1 457 000 + 4 100 000 = 16 387 000."),
               S("Total variance", text="15 840 000 − 16 387 000 = 547 000 adverse."),
           ]),
        CODE(_t_comp, "text", title="Table of comparison"),
        EX("Worked example 2: analysing the variances",
           intro="Split each element's variance into its two parts.",
           steps=[
               S("Materials", text="Actual price 5 049 000 ÷ 9 900 = 510. Price (500 − 510) × 9 900 = 99 000 A. Usage (9 600 − 9 900) × 500 = 150 000 A. Total 249 000 A."),
               S("Labour", text="Actual rate 5 781 000 ÷ 4 700 = 1 230. Rate (1 200 − 1 230) × 4 700 = 141 000 A. Efficiency (4 800 − 4 700) × 1 200 = 120 000 F. Total 21 000 A."),
               S("Variable overhead", text="Expenditure 4 700 × 300 − 1 457 000 = 47 000 A. Efficiency (4 800 − 4 700) × 300 = 30 000 F. Total 17 000 A."),
               S("Fixed overhead", text="Expenditure 4 000 000 − 4 100 000 = 100 000 A. Volume (2 400 − 2 500) × 1 600 = 160 000 A: capacity (4 700 − 5 000) × 800 = 240 000 A and efficiency (4 800 − 4 700) × 800 = 80 000 F."),
               S("Check", text="249 000 A + 21 000 A + 17 000 A + 260 000 A = 547 000 A, equal to the table of comparison."),
           ]),
        CODE(_t_split, "text", title="Analysis of variances"),
        H("Interpreting variances"),
        T("Variances are linked. Cheaper, poorer board would give a favourable price variance but an adverse usage variance; here both are adverse, so look for a price rise **and** wastage. "
          "The labour force was paid more per hour (adverse rate) but worked faster (favourable efficiency): perhaps more skilled workers were hired. Fewer hours than budgeted (capacity 240 000 A) "
          "suggests lost production time or low demand. Report each variance to the manager who controls it: purchasing for price, production for usage and efficiency, personnel for rates."),
        KEY("Limits of standard costing", "For evaluation answers.",
            cards=[["Standards date quickly", "Inflation and new methods make standards out of date; variances then reflect the standard, not performance."],
                   ["Behaviour", "Managers may chase favourable variances (buying cheap material) at the expense of quality."],
                   ["Fit", "Works best for repetitive production; less useful for one-off jobs or fast-changing services."]]),
        MISTAKE("Using budgeted output instead of actual output for standard quantities",
                "Standard quantity = standard per unit × **actual** output (here 2 400 × 4 = 9 600 kg), never the budgeted 2 500 units."),
        MISTAKE("Valuing the usage variance at actual price",
                "Usage and efficiency variances use the **standard** price; the price variance already captures the price difference on the actual quantity."),
        QUIZ("Standard: 3 kg at FCFA 400 per unit. Actual output 1 000 units used 3 200 kg bought at FCFA 380. The material usage variance is",
             ["80 000 A", "76 000 A", "64 000 F", "80 000 F"], 0,
             "(3 000 − 3 200) × 400 = 80 000 adverse: more material than standard was used.",
             hint="Usage variance = (SQ − AQ) × SP.",
             feedback=["", "This values the excess at the actual price of 380.", "This is the price variance (400 − 380) × 3 200, which is favourable.", "Using more material than standard is adverse, not favourable."]),
        QUIZ("Workers were paid FCFA 1 300 an hour against a standard of FCFA 1 200, and finished the work in fewer hours than standard. The most likely result is",
             ["adverse rate variance and favourable efficiency variance", "favourable rate and favourable efficiency variances",
              "adverse rate and adverse efficiency variances", "no variances, because the effects cancel"], 0,
             "Higher pay rate is adverse; fewer hours is favourable. They may be linked (more skilled workers).",
             feedback=["", "Paying more per hour is adverse.", "Fewer hours than standard is favourable.", "Variances are reported separately even if the totals partly cancel."], title="Quick check 2"),
        TIP("Standard costing is examined in Paper 2, Section B. The Board's 2023 report describes a question asking for a table of comparison and an analysis of variances, with weak scores, "
            "so practise both steps: total comparison first, then each split, then a check that the parts add to the total.", title="Exam link"),
        PQ("Standard 4 kg at FCFA 300 per unit; actual output 1 200 units; actual 5 200 kg at FCFA 320. Calculate the material price and usage variances.",
           "Price (300 − 320) × 5 200 = 104 000 A. Usage (4 800 − 5 200) × 300 = 120 000 A. Total 224 000 A."),
        PQ("Standard 2 hours at FCFA 1 000 per unit; actual output 1 500 units took 3 100 hours at FCFA 950. Calculate the labour rate and efficiency variances.",
           "Rate (1 000 − 950) × 3 100 = 155 000 F. Efficiency (3 000 − 3 100) × 1 000 = 100 000 A. Total 55 000 F."),
        PQ("Give two possible causes of an adverse material usage variance and say who is responsible for each.",
           "Poor-quality material bought cheaply (purchasing manager); wastage by untrained workers or badly maintained machines (production manager)."),
        PQ("Explain why a favourable material price variance is not always good news.",
           "It may come from cheaper, lower-quality material that causes adverse usage, labour efficiency or quality problems and customer complaints."),
        SUM("Standard cost = standard quantity × standard price for one unit; compare with actual using the standard cost of actual output.",
            "Materials: price (SP − AP) × AQ; usage (SQ − AQ) × SP. Labour: rate and efficiency on the same pattern.",
            "Variable overhead: expenditure and efficiency. Fixed overhead: expenditure and volume (capacity + efficiency).",
            "The parts must add up to the total variance in the table of comparison.",
            "Interpret causes, links between variances and responsibility; know your textbook's sign convention."),
    ]))

# ====================================================================== 12. Investment appraisal
_n_inv = 10_000_000
_n_cf = [3_000_000, 3_500_000, 3_000_000, 2_500_000, 2_000_000]
_n_f10 = [Fr(909, 1000), Fr(826, 1000), Fr(751, 1000), Fr(683, 1000), Fr(621, 1000)]
_n_f15 = [Fr(870, 1000), Fr(756, 1000), Fr(658, 1000), Fr(572, 1000), Fr(497, 1000)]
assert [round(1 / 1.10 ** t, 3) for t in range(1, 6)] == [float(x) for x in _n_f10]
assert [round(1 / 1.15 ** t, 3) for t in range(1, 6)] == [float(x) for x in _n_f15]
_n_pv10 = [c * f for c, f in zip(_n_cf, _n_f10)]
_n_pv15 = [c * f for c, f in zip(_n_cf, _n_f15)]
_n_npv10, _n_npv15 = sum(_n_pv10) - _n_inv, sum(_n_pv15) - _n_inv
assert (sum(_n_pv10), _n_npv10, sum(_n_pv15), _n_npv15) == (10_820_500, 820_500, 9_654_000, -346_000)
_n_irr = 10 + 5 * _n_npv10 / (_n_npv10 - _n_npv15)
assert round(float(_n_irr), 1) == 13.5            # interpolation; exact IRR is about 13.4%
# payback
_n_cum, _n_pb = 0, None
for i, c in enumerate(_n_cf):
    if _n_cum + c >= _n_inv and _n_pb is None:
        _n_pb = i + Fr(_n_inv - _n_cum, c)
    _n_cum += c
assert 3_000_000 + 3_500_000 + 3_000_000 == 9_500_000 and Fr(500_000, 2_500_000) == Fr(1, 5)
_n_pb = 3 + Fr(500_000, 2_500_000)
assert _n_pb == Fr(16, 5)                          # 3.2 years
_n_avg = Fr(sum(_n_cf) - _n_inv, 5)
assert _n_avg == 800_000 and Fr(_n_avg, _n_inv) == Fr(8, 100) and Fr(_n_avg, Fr(_n_inv, 2)) == Fr(16, 100)
assert Fr(sum(_n_cf), 5) == 2_800_000 and 4_000_000 // 4 // 8_000_000 * 1 == 0 and Fr(1_000_000, 8_000_000) == Fr(1, 8)
_t_npv = "\n".join([
    "Year   Cash flow   Factor 10%   PV at 10%   Factor 15%   PV at 15%",
    f"0     {n(-_n_inv):>11}        1.000   {n(-_n_inv):>10}        1.000   {n(-_n_inv):>10}",
    *[f"{i + 1:<6}{n(_n_cf[i]):>11}        {float(_n_f10[i]):.3f}   {n(_n_pv10[i]):>10}        {float(_n_f15[i]):.3f}   {n(_n_pv15[i]):>10}"
      for i in range(5)],
    f"NPV                              {n(_n_npv10):>10}                    {n(_n_npv15):>10}",
])
_t_pb = "\n".join([
    "Year   Cash flow   Cumulative",
    f"0     {n(-_n_inv):>11}  {n(-_n_inv):>11}",
    *[f"{i + 1:<6}{n(_n_cf[i]):>11}  {n(-_n_inv + sum(_n_cf[:i + 1])):>11}" for i in range(5)],
])
assert -_n_inv + sum(_n_cf[:3]) == -500_000
# second example (annuity)
_n2_inv, _n2_cf = 6_000_000, 2_000_000
_n2_ann = Fr(3037, 1000)
_n2_npv = _n2_cf * _n2_ann - _n2_inv
assert _n2_npv == 74_000 and round((1 - 1.12 ** -4) / 0.12, 3) == 3.037
assert Fr(8_000_000, 2_000_000) == 4

LESSONS.append(lesson(
    module=M_BUD, topic="Investment appraisal",
    title="Investment appraisal: payback, ARR, NPV and IRR",
    slug="acu2-investment-appraisal", minutes=28,
    summary="Appraise a capital project with payback period, accounting rate of return, net present value and internal rate of return, "
            "and weigh the methods and the non-financial factors in a recommendation.",
    objectives=[
        "Calculate the payback period and the accounting rate of return and state their weaknesses",
        "Discount cash flows with present value factors and calculate the net present value",
        "Estimate the internal rate of return by interpolation",
        "Compare the methods, apply the decision rules and recommend with financial and non-financial reasons",
    ],
    key_concepts=["Payback period", "Accounting rate of return (ARR)", "Time value of money", "Discounting", "Net present value (NPV)",
                  "Internal rate of return (IRR)", "Cost of capital", "Relevant cash flows"],
    blocks=[
        H("Spending money now for returns later"),
        T("A cooperative in Dschang is offered a cassava-processing machine for FCFA 10 000 000. It will earn money for five years. Should it buy? Money received in five years is worth less than money in the hand today, "
          "because today's money can be invested or can pay off a loan. **Investment appraisal** compares the cost now with the returns later. All figures are **invented for practice**."),
        D("**Capital investment appraisal** assesses a long-term project using its **relevant cash flows**: future cash receipts and payments that change because of the project. "
          "Depreciation is not a cash flow and is left out; money already spent (sunk costs) is ignored; interest is normally not included because the discount rate already covers the cost of finance.", title="Relevant cash flows"),
        H("Payback and accounting rate of return"),
        D("**Payback period** = the time needed for cumulative net cash inflows to equal the initial outlay. Decision rule: accept if it is shorter than the firm's maximum payback (or choose the shortest).", title="Payback"),
        D("**Accounting rate of return (ARR)** = average annual accounting profit ÷ initial investment (or ÷ average investment) × 100. Accounting profit = cash inflow − depreciation. "
          "Textbooks differ on the base (initial or average investment): state which you use.", title="ARR"),
        EX("Worked example 1: payback and ARR",
           intro="Initial outlay FCFA 10 000 000 (no residual value). Net cash inflows for years 1 to 5: 3 000 000; 3 500 000; 3 000 000; 2 500 000; 2 000 000. Find the payback period and the ARR.",
           steps=[
               S("Cumulative cash", text="After year 3: 9 500 000 received, so 500 000 is still needed."),
               S("Payback", text="Year 4 brings 2 500 000 evenly, so 500 000 ÷ 2 500 000 = 0.2 of a year: payback 3.2 years (3 years 2.4 months)."),
               S("Average profit", text="Total inflows 14 000 000. Depreciation is 10 000 000 ÷ 5 = 2 000 000 a year. Average inflow 2 800 000, so average profit = 2 800 000 − 2 000 000 = 800 000."),
               S("ARR", text="800 000 ÷ 10 000 000 = 8% on initial investment; 800 000 ÷ 5 000 000 = 16% on average investment."),
           ]),
        CODE(_t_pb, "text", title="Payback table (invented for practice)"),
        KEY("Strengths and weaknesses", "Needed for evaluation.",
            cards=[["Payback", "Simple, favours liquidity and low risk. Ignores cash flows after the payback date and the time value of money."],
                   ["ARR", "Easy and uses profit, which managers know. Based on accounting profit, ignores timing and the time value of money, and definitions vary."]]),
        H("Net present value"),
        D("**Discounting** converts a future cash flow into its **present value** (PV): PV = cash flow × 1 ÷ (1 + r)^t, where r is the discount rate (the firm's cost of capital) and t the year. "
          "**Net present value** = sum of the PVs of all cash flows (including the outlay at year 0). Decision rule: accept if NPV is positive.", title="NPV"),
        F(r"\text{NPV} = \sum_{t=0}^{n} \frac{C_t}{(1+r)^t} \qquad \text{discount factor} = \frac{1}{(1+r)^t}", title="Net present value"),
        T("The factors below are rounded to three decimals, as in a typical present value table. If your table or calculator rounds differently, your answer may differ slightly: this is accepted in examinations."),
        EX("Worked example 2: NPV at 10% and 15%",
           intro="Use the cash flows of worked example 1 and discount at 10%, then at 15%.",
           steps=[
               S("Factors at 10%", text="0.909; 0.826; 0.751; 0.683; 0.621."),
               S("PV at 10%", text="2 727 000 + 2 891 000 + 2 253 000 + 1 707 500 + 1 242 000 = 10 820 500."),
               S("NPV at 10%", text="10 820 500 − 10 000 000 = +820 500: accept."),
               S("PV at 15%", text="Factors 0.870; 0.756; 0.658; 0.572; 0.497 give 2 610 000 + 2 646 000 + 1 974 000 + 1 430 000 + 994 000 = 9 654 000."),
               S("NPV at 15%", text="9 654 000 − 10 000 000 = −346 000: reject at 15%."),
           ]),
        CODE(_t_npv, "text", title="NPV working (invented for practice)"),
        H("Internal rate of return"),
        D("The **internal rate of return (IRR)** is the discount rate at which NPV is zero. Decision rule: accept if IRR is higher than the cost of capital. "
          "Estimate it by **interpolation** between a rate with positive NPV and a rate with negative NPV.", title="IRR"),
        F(r"\text{IRR} \approx L + \frac{\text{NPV}_L}{\text{NPV}_L - \text{NPV}_H}\,(H - L)", title="Interpolation (L = lower rate, H = higher rate)"),
        EX("Worked example 3: IRR",
           intro="Use the two NPVs of worked example 2.",
           steps=[
               S("Substitute", text="IRR ≈ 10 + 820 500 ÷ (820 500 + 346 000) × 5."),
               S("Calculate", text="820 500 ÷ 1 166 500 = 0.7033; × 5 = 3.52; IRR ≈ 13.5%."),
               S("Decide", text="13.5% is above a cost of capital of 10% but below 15%. Interpolation is approximate: the true IRR is about 13.4%.")]),
        IMG("alacu2-npv-profile.svg",
            alt="Graph of NPV against discount rate falling from positive at 10 percent to negative at 15 percent, crossing zero at about 13.5 percent, the IRR.",
            caption="Figure 1. NPV falls as the discount rate rises; the IRR is where the line crosses zero."),
        KEY("Choosing between methods", "A balanced recommendation uses several.",
            cards=[["NPV", "Uses all cash flows and the time value of money; gives the money gain in FCFA; assumes cash flows are reinvested at the cost of capital. Needs a discount rate."],
                   ["IRR", "A percentage that is easy to compare with the cost of capital; can mislead when ranking projects of different size or with changing cash-flow signs."],
                   ["Non-financial factors", "Jobs created, environmental impact, strategic fit, risk and reliability of the forecast, and how the project is financed."]]),
        MISTAKE("Including depreciation in the cash flows",
                "Depreciation is not a cash flow. Use it only in ARR, where profit is needed."),
        MISTAKE("Forgetting to discount the outlay",
                "The outlay at year 0 has a factor of 1.000 and is subtracted as a negative cash flow. Do not subtract it from undiscounted inflows by mistake."),
        MISTAKE("Calling the project good because payback is short",
                "A short payback shows quick recovery of cash, not value. A project with a longer payback may have a much higher NPV."),
        QUIZ("A project has NPV +FCFA 400 000 at 8% and −FCFA 100 000 at 12%. The IRR by interpolation is about",
             ["11.2%", "10.0%", "9.6%", "8.8%"], 0,
             "8 + 400 000 ÷ 500 000 × 4 = 8 + 3.2 = 11.2%.",
             hint="IRR = L + NPV_L ÷ (NPV_L − NPV_H) × (H − L).",
             feedback=["", "This is the midpoint of 8 and 12, not interpolation.", "This uses the wrong fraction of the interval (the lower NPV share, 0.2 × 4 = 0.8, added to 8.8 gives 9.6).", "This adds only 0.8 to 8."]),
        QUIZ("A project's cash flows are discounted at the cost of capital and the NPV is negative. The firm should",
             ["reject it on financial grounds", "accept it because cash flows are positive", "accept it because payback is under 5 years", "recalculate using depreciation"], 0,
             "A negative NPV means the project returns less than the cost of capital.",
             feedback=["", "Positive undiscounted cash flows are not enough.", "Payback ignores the time value of money.", "Depreciation is not a cash flow."], title="Quick check 2"),
        TIP("Capital budgeting appears in Paper 2 (management accounting) and in Paper 1. The blueprint for the course lists payback, ARR, NPV and IRR; check with your teacher which are examined and which table of factors is allowed. "
            "State the factors you use and show every year's calculation.", title="Exam link"),
        PQ("Outlay FCFA 6 000 000; inflows FCFA 2 000 000 a year for 4 years. Calculate the payback period and the NPV at 12% (the four-year annuity factor at 12% is 3.037).",
           "Payback = 6 000 000 ÷ 2 000 000 = 3 years. PV = 2 000 000 × 3.037 = 6 074 000; NPV = +74 000 (marginally acceptable)."),
        PQ("A project costs FCFA 8 000 000 and has total profit over four years of FCFA 4 000 000 after depreciation. Calculate the ARR on initial investment.",
           "Average annual profit = 1 000 000; ARR = 1 000 000 ÷ 8 000 000 = 12.5%."),
        PQ("Give two reasons why NPV is considered better than payback.",
           "NPV uses the time value of money and counts all cash flows over the project's life; payback ignores flows after the payback date and does not discount."),
        PQ("A project has a positive NPV but may cause pollution in the local river. Discuss briefly.",
           "Financially it adds value, but pollution could bring fines, clean-up costs, loss of reputation and harm to the community. A decision should weigh these, perhaps modifying the project to cut pollution."),
        SUM("Use relevant cash flows only: no depreciation, no sunk costs, no interest.",
            "Payback: time to recover the outlay; ARR: average profit ÷ investment; both ignore the time value of money (ARR also uses profit).",
            "NPV = discounted inflows − outlay; accept if positive.",
            "IRR: rate where NPV is zero, estimated by interpolation; accept if above the cost of capital.",
            "Recommend with several methods plus non-financial factors."),
    ]))

# ====================================================================== 13. Examination: Paper 1
assert 5_000 * 0.4 == 2_000 and Fr(9_000_000, 1_800) == 5_000
assert Fr(30_000_000 - 12_000_000, 12_000_000) == Fr(3, 2) and Fr(30_000_000 - 8_000_000 - 4_000_000, 12_000_000) == Fr(3, 2)
assert Fr(2_400_000 + 600_000, 5_000 + 1_000) == 500 and Fr(3_000_000, 600_000) == 5
assert 90 / 50 == 1.8
_p1_ds = Fr(15_000) - Fr(14_400)
assert _p1_ds == 600 and Fr(4_000 * 15_000 + 1_000 * 12_000, 5_000) == 14_400

LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1: multiple-choice strategy across the whole Upper Sixth course",
    slug="acu2-exam-paper-1-multiple-choice", minutes=24,
    summary="How Paper 1 is built (50 compulsory multiple-choice questions on financial, cost and management, and company accounting and taxation), "
            "a time plan, quick checks that catch wrong options, and the traps in calculation questions.",
    objectives=[
        "State the facts of Paper 1 from the Board's 2023 report: 50 compulsory multiple-choice questions, each worth one mark",
        "Plan time and use a two-pass method with elimination and estimation",
        "Use built-in checks (balance sheet totals, contribution, distribution totals) to confirm answers",
        "Recognise how wrong options are built from the typical errors of each Upper Sixth topic",
    ],
    key_concepts=["Paper 1", "Two-pass method", "Elimination", "Quick checks", "Distractors", "Whole-course revision"],
    blocks=[
        H("What Paper 1 is"),
        T("Paper 1 is the multiple-choice paper. In a classroom in Bamenda every candidate answers the same fifty questions, and a computer marks the answer sheets. "
          "There is no partial credit and no explanation of method, so accuracy and speed decide the marks."),
        D("According to the Board's 2023 report for Accounting 0705, Paper 1 is made up of **50 multiple-choice questions, all compulsory**. In 2023, 25 questions were on financial accounting, "
          "10 on cost and management accounting and 15 on company accounting and taxation. Each question is worth **one mark**. The three papers are weighted 30 (Paper 1), 30 (Paper 2) and 40 (Paper 3). "
          "The proportions may change from year to year, so revise all of the course.", title="Paper 1: the official facts"),
        TIP("This course has six Upper Sixth modules. Paper 1 can draw on all of them and on the Lower Sixth financial accounting, so keep your Lower Sixth notes too. Check the exact format with your teacher.", title="Exam link"),
        H("A time plan (KKEVO practice advice)"),
        T("The report does not state a time limit for Paper 1, so check the time on your own paper. Our mock exam uses **90 minutes for 50 questions**, which is 1.8 minutes a question. "
          "This is a KKEVO practice setting, not an official rule."),
        KEY("The two-pass method", "Study advice, not an official rule.",
            cards=[["Pass 1", "Answer every question you can finish in about a minute. Put a mark beside the rest."],
                   ["Pass 2", "Return to the marked questions. Calculation questions are worth the same single mark as definitions, so do the short ones first."],
                   ["Final check", "Make sure every question has an answer: a blank is always a lost mark. Re-read words such as NOT, gross, net, favourable, adverse."]]),
        H("Quick checks that catch wrong options"),
        D("Most calculation questions have a check built into accounting itself: a balance sheet must balance; a distribution table's main centres must total the incorporated overheads; "
          "FRNG − BFR must equal net cash; flexed profit − variances must equal actual profit; contribution − fixed costs must equal profit. Use these before you choose an option.", title="Built-in checks"),
        EX("Worked example 1: break-even in one line",
           intro="Fixed costs FCFA 9 000 000; contribution per unit FCFA 1 800. Options: A 2 000 units; B 5 000 units; C 9 000 units; D 16 200 units. Which is the break-even point?",
           steps=[
               S("Method", text="Break-even units = fixed costs ÷ contribution per unit."),
               S("Calculate", text="9 000 000 ÷ 1 800 = 5 000 units: option B."),
               S("Eliminate quickly", text="C copies a figure from the question; D multiplies instead of dividing; A is the result of 9 000 000 ÷ 4 500 (dividing by the selling price)."),
           ]),
        EX("Worked example 2: a working-capital check",
           intro="Stable resources 30 000 000; stable uses 18 000 000; BFR 12 000 000. What is net cash? Options: A +18 000 000; B +6 000 000; C 0; D −12 000 000.",
           steps=[
               S("FRNG", text="30 000 000 − 18 000 000 = 12 000 000."),
               S("Net cash", text="12 000 000 − 12 000 000 = 0: option C."),
               S("Trap", text="A adds BFR to FRNG; D takes the BFR alone as a deficit.")]),
        EX("Worked example 3: value of a share before a rights issue",
           intro="4 000 old shares are worth 15 000 each. 1 000 new shares are issued at 12 000. Find the value of a share after the issue and the subscription right (DS).",
           steps=[
               S("Value after", text="(4 000 × 15 000 + 1 000 × 12 000) ÷ 5 000 = 72 000 000 ÷ 5 000 = 14 400."),
               S("Right", text="DS = 15 000 − 14 400 = 600."),
               S("Check", text="The final value lies between the old value and the issue price (12 000 < 14 400 < 15 000).")]),
        H("How wrong options are built"),
        T("The writers of multiple-choice questions use real mistakes. Learn them: dividing by the selling price instead of the contribution; leaving out the opening balance; mixing up debit and credit; "
          "forgetting a restatement (discounted bills, dividend payable); using budgeted instead of actual output for standard quantities; applying 'higher is better' to a ratio; using depreciation as a cash flow. "
          "When a result matches one of these, you probably made the same slip."),
        KEY("Ten-second tests before you choose", "Cheap checks that avoid most losses.",
            cards=[["Sign and unit", "Is the answer a profit or a loss, FCFA or a percentage, units or value?"],
                   ["Size", "Does the number make sense? A margin of safety cannot exceed budgeted sales."],
                   ["Wording", "NOT, EXCEPT, gross, net, favourable, adverse, before, after."],
                   ["Method match", "Did you use the method the question names (CUMP, FIFO, high-low, interpolation)?"]]),
        MISTAKE("Choosing the first option that matches a figure from the question",
                "Distractors are built from the figures in the question. Always do the calculation first, then compare with the options."),
        MISTAKE("Spending too long on one calculation",
                "Each question has the same single mark. If a question is taking over two minutes, mark it and come back."),
        MISTAKE("Leaving revision of one module for last",
                "The Board's 2023 report says some candidates had not mastered the last topics of the programme. Spread revision across all modules, including company taxation and capital changes."),
        QUIZ("Paper 1 has 50 compulsory questions. If you plan 90 minutes in all, the average time per question is",
             ["1.5 minutes", "1.8 minutes", "2 minutes", "3 minutes"], 1,
             "90 ÷ 50 = 1.8 minutes.", hint="Divide the total time by the number of questions.",
             feedback=["That would take 75 minutes.", "", "That would take 100 minutes.", "That would take 150 minutes."]),
        QUIZ("A candidate calculates a margin of safety larger than budgeted sales. What should she conclude?",
             ["The answer is probably wrong; the margin of safety cannot exceed budgeted sales", "The firm is very safe", "The firm is making a loss", "Break-even sales were negative"], 0,
             "Margin of safety = budgeted sales − break-even sales, so it cannot exceed budgeted sales when break-even is positive.",
             feedback=["", "A result that is impossible shows a calculation mistake.", "A loss would give a negative margin, not a larger one.", "Break-even sales are not negative here; recheck the formula."], title="Quick check 2"),
        TIP("In the report, Paper 1 had no content errors and the question split was 25 financial, 10 cost and management and 15 company accounting and taxation. Use that as a guide for where to spend revision time, but check with your teacher.", title="Exam link"),
        PQ("Cost of capital 10%. A project has NPV −FCFA 250 000 at 10%. What does this tell you, and what would you check next?",
           "At 10% the project returns less than the cost of capital, so on financial grounds it should be rejected. Check the cash flows and the IRR, and consider non-financial factors."),
        PQ("List three built-in checks you could use on a distribution table, a cash budget and a flexible budget.",
           "Distribution table: main centres' totals equal the primary total and service centres end at zero. Cash budget: each closing balance equals the next opening balance. Flexible budget: flexed profit minus variances equals actual profit."),
        PQ("Explain why 'all of the above' style reasoning is risky when two options look close.",
           "Close options are usually built from two different errors. Redo the calculation and see which wrong method produces the second option; choose the answer your correct method produces."),
        SUM("Paper 1: 50 compulsory multiple-choice questions, one mark each, covering financial, cost and management, and company accounting and taxation.",
            "Plan time, answer easy questions first, return to harder ones, and never leave a blank.",
            "Use built-in checks: balance sheets balance, distribution totals agree, flexed profit reconciles.",
            "Learn how distractors arise from typical errors.",
            "Revise every module, including the last topics of the programme."),
    ]))

# ====================================================================== 14. Examination: Paper 2
_t2 = {"Jan": (1_000, 700_000), "Feb": (1_400, 820_000), "Mar": (1_800, 940_000), "Apr": (1_200, 760_000)}
_t2_vc = Fr(940_000 - 700_000, 1_800 - 1_000)
_t2_fc = 700_000 - _t2_vc * 1_000
assert (_t2_vc, _t2_fc) == (300, 400_000) and 400_000 + 300 * 1_400 == 820_000 and 400_000 + 300 * 1_200 == 760_000
_t2_est = 400_000 + 300 * 1_500
assert _t2_est == 850_000
_t2_oar = Fr(3_600_000, 9_000)
_t2_job = 210_000 + 40 * 700 + 40 * _t2_oar
assert (_t2_oar, _t2_job) == (400, 254_000)
_t2_comp_std, _t2_comp_act = 1_000 * 3_800, 3_950_000
assert _t2_comp_std - _t2_comp_act == -150_000

LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2: Cost and Management Accounting, choosing questions and presenting working",
    slug="acu2-exam-paper-2-cost-management", minutes=26,
    summary="How Paper 2 is set (two sections of three questions: two from cost accounting and all of management accounting), the topics the Board's "
            "2023 report lists, how to present working, and the weaknesses it noticed.",
    objectives=[
        "State the structure of Paper 2 from the Board's 2023 report and the topics the report lists",
        "Plan time across five answers and choose the two Section A questions you can score best",
        "Lay out working so that method marks are visible: formula, substitution, answer, unit",
        "Avoid the mistakes the report highlights, especially on budgets and standard costing",
    ],
    key_concepts=["Paper 2", "Section A cost accounting", "Section B management accounting", "Presentation of working", "Question choice"],
    blocks=[
        H("What Paper 2 is"),
        T("Paper 2 is a written paper on **Cost and Management Accounting**. Unlike Paper 1, the examiner reads your working, so a clear layout can rescue marks even when a figure is wrong."),
        D("Per the Board's 2023 report, Paper 2 has **two sections of three questions each**. Candidates answer **two questions from Section A (Cost Accounting) and all three questions of Section B (Management Accounting)**, "
          "five questions in all. The report says each question carries equal marks (20) and that the paper is a three-hour paper. Use ink (blue or black), not pencil, as the report recommends for Papers 2 and 3.",
          title="Paper 2: the official facts"),
        T("The report describes the 2023 questions in terms of: the nature of cost (separating a cost into fixed and variable parts by the high-low method and estimating future cost), "
          "overhead absorption and job costing, stock valuation by FIFO and weighted average cost with a trading account, standard costing (a table of comparison and analysis of variances), "
          "a cash budget with the benefits of budgets, and break-even analysis. These are the topics of this course's cost and budget modules. Topics change each year, so revise all of them."),
        TIP("Paper 2 maps onto the modules 'Cost Accounting: Full & Marginal Costing' and 'Budgetary Control, Standard Costing & Capital Budgeting'. Check with your teacher whether capital budgeting is examined here.", title="Exam link"),
        H("Choosing and timing"),
        T("Five answers in three hours is about **36 minutes** each (KKEVO planning advice; check your own paper's time). Read all six questions first. In Section A choose the two where you can complete the working. "
          "In Section B you have no choice, so practise all three question types."),
        KEY("What the report says went well and badly", "Paraphrased from the 2023 report.",
            cards=[["Better answered", "Stock valuation by FIFO and weighted average, and overhead absorption with a job cost sheet. Candidates who practised stock cards scored well."],
                   ["Poorly answered", "The cash budget question was among the least and poorest answered; standard costing tables of comparison produced weak marks; break-even questions needed a differential operating table, break-even in value and quantity, and sales for a given profit."]]),
        H("Presenting working"),
        EX("Worked example 1: high-low method",
           intro="Monthly hours and total cost: Jan 1 000 h FCFA 700 000; Feb 1 400 h FCFA 820 000; Mar 1 800 h FCFA 940 000; Apr 1 200 h FCFA 760 000. Estimate the cost for 1 500 hours.",
           steps=[
               S("Choose the extremes of activity", text="Lowest 1 000 h (700 000); highest 1 800 h (940 000)."),
               S("Variable cost per hour", text="(940 000 − 700 000) ÷ (1 800 − 1 000) = 240 000 ÷ 800 = 300."),
               S("Fixed cost", text="700 000 − 1 000 × 300 = 400 000."),
               S("Estimate", text="400 000 + 1 500 × 300 = 850 000."),
               S("Check with a middle month", text="Feb: 400 000 + 1 400 × 300 = 820 000, which agrees with the data."),
           ]),
        EX("Worked example 2: job cost with an absorption rate",
           intro="Budgeted overheads FCFA 3 600 000; budgeted direct labour hours 9 000. A job uses materials FCFA 210 000 and 40 labour hours at FCFA 700. Find the production cost.",
           steps=[
               S("OAR", text="3 600 000 ÷ 9 000 = 400 per hour."),
               S("Prime cost", text="210 000 + 40 × 700 = 238 000."),
               S("Overhead", text="40 × 400 = 16 000."),
               S("Production cost", text="238 000 + 16 000 = 254 000.")]),
        EX("Worked example 3: a table of comparison",
           intro="Standard cost of 1 000 units is FCFA 3 800 each; the actual total cost is FCFA 3 950 000. Present the total variance.",
           steps=[
               S("Standard cost of actual output", text="1 000 × 3 800 = 3 800 000."),
               S("Variance", text="3 800 000 − 3 950 000 = 150 000 adverse."),
               S("Next step", text="Analyse it into price and quantity parts for each input and check that the parts add up to 150 000 A.")]),
        T("Method marks follow clear steps: write the formula, substitute, calculate, add the unit and label (F or A, FCFA, units). Draw a single ruled line under totals. "
          "Keep tables in columns with headings. Write the final answer on its own line."),
        H("Management accounting answers"),
        KEY("Cash budget layout", "A frequent weak point.",
            cards=[["Columns", "One column for each month, rows for opening balance, receipts, payments and closing balance."],
                   ["Receipts", "Place credit sales in the month they are received, not the month of sale."],
                   ["Payments", "Leave out depreciation. Include capital payments when they are paid."],
                   ["Comment", "If asked, say what the budget shows: when a deficit appears and how to finance it."]]),
        KEY("Benefits of budgets", "The report notes that candidates struggled with this part.",
            cards=[["Planning and coordination", "Forces plans and links departments."],
                   ["Control and motivation", "Compares actual with plan; targets motivate if managers share in setting them."]]),
        MISTAKE("Writing only the final figure",
                "If the figure is wrong and there is no working, the mark is zero. Show each step."),
        MISTAKE("Choosing Section A questions by topic title only",
                "Read the whole question. A familiar title can hide an unfamiliar requirement. Count how many parts you can fully complete."),
        MISTAKE("Using pencil or leaving tables incomplete",
                "The Board's report asks for blue or black ink. An unfinished table loses easy marks for the headings and totals."),
        QUIZ("Paper 2 requires candidates to answer",
             ["all six questions", "two from Section A and all three from Section B", "three from Section A and two from Section B", "any five of the six questions"], 1,
             "Section A (Cost Accounting): two of three. Section B (Management Accounting): all three.",
             hint="Recall the structure from the report.",
             feedback=["Candidates answer five.", "", "The numbers are reversed.", "Section B questions are compulsory."]),
        QUIZ("Which shows the best layout for a variance answer?",
             ["The final figure only", "Formula, substitution, answer, and the label F or A", "A paragraph describing the variance", "The figures in a list with no labels"], 1,
             "Method marks reward visible steps, and the label tells the reader whether profit rises or falls.",
             feedback=["No working means no method marks.", "", "Words alone do not show the calculation.", "Unlabelled figures are hard to mark."], title="Quick check 2"),
        PQ("Highest activity 5 000 units, cost FCFA 2 750 000; lowest 3 000 units, cost FCFA 2 150 000. Estimate the cost of 4 000 units.",
           "Variable = 600 000 ÷ 2 000 = 300; fixed = 2 150 000 − 3 000 × 300 = 1 250 000; cost = 1 250 000 + 4 000 × 300 = 2 450 000."),
        PQ("Give three benefits of budgets, as a Section B answer might require.",
           "Planning (anticipate problems); coordination (departments work to one plan); control (actual vs budget variances); motivation (targets); communication; authority for spending."),
        PQ("Outline a plan for a cash budget question in five steps.",
           "1. Read data and the months needed. 2. Work out receipts month by month with credit timing. 3. Work out each payment with its timing, omitting depreciation. 4. Total, and carry balances forward. 5. Comment on any deficit and suggest finance."),
        SUM("Paper 2: two of three Section A (cost accounting) questions and all three Section B (management accounting) questions; equal marks; three hours (per the 2023 report).",
            "Topics reported: nature of cost, overhead and job costing, stock valuation, standard costing, cash budgets, break-even.",
            "Show formula, substitution, answer, unit and F/A labels, in ink.",
            "Practise cash budgets and variance tables, the weakest areas in 2023.",
            "Plan about 36 minutes for each answer; read all questions first."),
    ]))

# ====================================================================== 15. Examination: Paper 3
_t3_nav = 49_500_000
assert Fr(_t3_nav, 5_000) == 9_900
_t3_div, _t3_ret = Fr(3_600_000, 6_000), Fr(1_800_000, 6_000)
assert (_t3_div, _t3_ret) == (600, 300)
_t3_ds = 15_000 - Fr(4_000 * 15_000 + 1_000 * 12_000, 5_000)
assert _t3_ds == 600
_t3_tax = Fr(30, 100) * (14_000_000 + 1_000_000 - 400_000)
assert _t3_tax == 4_380_000 and Fr(30, 100) * 8_400_000 == 2_520_000
_t3_avg = Fr(2_400_000 + 3_000_000 + 3_600_000, 3)
assert _t3_avg == 3_000_000

LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 3",
    title="Paper 3: Financial Accounting, company accounting and taxation",
    slug="acu2-exam-paper-3-financial-accounting", minutes=26,
    summary="How Paper 3 is set (Section A financial accounting, answer three of four; Section B company accounting and taxation, answer two of three), "
            "what the Board's 2023 report says about strong and weak questions, and a method for share valuation, tax and capital changes.",
    objectives=[
        "State the structure of Paper 3 from the Board's 2023 report",
        "Choose questions to bank marks first on the questions the report calls the strength of the paper",
        "Handle the weaker areas: valuation of shares, taxation and modification of capital",
        "Present statements, ratios, journals and computations in a clear examination layout",
    ],
    key_concepts=["Paper 3", "Section A financial accounting", "Section B company accounting and taxation", "Share valuation", "Taxable profit", "Modification of capital"],
    blocks=[
        H("What Paper 3 is"),
        T("Paper 3 is the **Financial Accounting** paper and carries the largest weight of the three papers. It tests statements, invoices and journals, ratios, impairment, and the company topics of this course."),
        D("Per the Board's 2023 report, Paper 3 has **two sections**. **Section A (Financial Accounting)** has four questions, of which candidates answer three. "
          "**Section B (Company Accounting and Taxation)** has three questions, of which candidates answer two. Five questions in all; each carries equal marks (20). "
          "The paper is weighted 40% of the examination. Write in blue or black ink.", title="Paper 3: the official facts"),
        T("The 2023 report listed these question topics: impairment and losses on doubtful customers with journals; ratio analysis (profitability, liquidity, efficiency and capital structure); "
          "purchases and sales of goods with invoices and journal entries under permanent inventory; presentation of the income statement and statement of financial position in vertical format; "
          "valuation of shares (net assets, mathematical value, return, financial value); taxation (a fiscal analysis of expenses and revenue to find taxable profit and the income tax due); and modification of capital "
          "(value before the increase, attribution right, subscription right, journals). The report called the first group the strength of the paper and the last three the weakness."),
        TIP("The financial analysis lessons (ratios) and the capital and tax lessons (company modules of this course) all feed Paper 3. Check with your teacher how the Lower Sixth topics are combined.", title="Exam link"),
        H("Where the marks are"),
        KEY("What the 2023 report said", "Paraphrased.",
            cards=[["Strength", "A student who attended regularly could score about 60% by choosing the questions on ratios, invoices and journals, and statements."],
                   ["Weakness", "Taxation and modification of capital were poorly attempted and seemed not to have been well taught, being the last topics; on share valuation candidates mixed up an average dividend and reserve with the figures of one year only."]]),
        T("Strategy: bank the Section A questions you can do accurately, then choose the Section B questions where you know the formulas. Do not skip the company topics: the marks there are available to those who learned them."),
        H("Weak areas, step by step"),
        EX("Worked example 1: valuing a share",
           intro="A company has net assets (adjusted equity) of FCFA 49 500 000 and 5 000 shares. Over the last 3 years dividends averaged 600 per share. Find the mathematical value and the return rate of a share on that value.",
           steps=[
               S("Mathematical value", text="49 500 000 ÷ 5 000 = 9 900 per share."),
               S("Return", text="Average dividend 600 ÷ 9 900 = about 6.1%."),
               S("Averages", text="If the question gives several years of dividends or reserves, average them over the years named before dividing; do not use one year only.")]),
        EX("Worked example 2: taxable profit",
           intro="Accounting profit FCFA 14 000 000. Include in the fiscal analysis: add back non-deductible expenses FCFA 1 000 000 and deduct non-taxable income FCFA 400 000. Use a teaching rate of 30% (check the current Finance Law).",
           steps=[
               S("Fiscal result", text="14 000 000 + 1 000 000 − 400 000 = 14 600 000."),
               S("Tax", text="30% × 14 600 000 = 4 380 000. The method is an add-back and deduction analysis; the rate and rules are teaching values to check against the current Finance Law and your textbook.")]),
        EX("Worked example 3: a rights issue",
           intro="4 000 old shares are worth 15 000 each; 1 000 new shares are issued at 12 000. Find the value after the issue and the subscription right.",
           steps=[
               S("Value after", text="(4 000 × 15 000 + 1 000 × 12 000) ÷ 5 000 = 14 400."),
               S("Subscription right", text="15 000 − 14 400 = 600."),
               S("Journal", text="Debit bank, credit share capital (and premium if issued above nominal).")]),
        MISTAKE("Mixing an average with a single year",
                "If the question gives several years of dividends or reserves, take the average the question asks for before dividing."),
        MISTAKE("Skipping Section B because it seems hard",
                "The report calls taxation and capital modification weak. Candidates who learn the formulas and the layout earn marks that others miss."),
        MISTAKE("Not linking each calculation to a layout",
                "Present statements in the required layout (vertical format) and journals with a narration. A correct figure in the wrong place loses marks."),
        QUIZ("Paper 3 requires candidates to answer",
             ["three of four Section A and two of three Section B", "two of four Section A and three of three Section B", "all seven questions", "any five of the seven"], 0,
             "The report gives four questions in Section A (answer three) and three in Section B (answer two).",
             hint="Recall the structure from the report.",
             feedback=["", "This swaps the numbers.", "Candidates answer five.", "The paper has section rules."]),
        QUIZ("According to the Board's 2023 report, which area was the weakness of Paper 3?",
             ["Ratio analysis and invoices", "Taxation, modification of capital and share valuation", "Impairment of current assets", "Presentation of the income statement"], 1,
             "The report listed taxation, modification of capital and share valuation as poorly done.",
             feedback=["These were stronger areas.", "", "Impairment is not named in the report as the weakness.", "This was a better-answered question."], title="Quick check 2"),
        PQ("The mathematical value of a share is 9 900 and the average dividend is 600. Calculate the return as a percentage of the mathematical value.",
           "600 ÷ 9 900 × 100 = 6.06%."),
        PQ("4 000 old shares are worth 15 000 each. 1 000 new shares are issued at 12 000. Calculate the subscription right (DS).",
           "Value after = 14 400. DS = 15 000 − 14 400 = 600 per old share."),
        PQ("Accounting profit FCFA 8 000 000. Non-deductible expenses FCFA 600 000. Non-taxable income FCFA 200 000. Find the fiscal result and tax at a teaching rate of 30%.",
           "8 000 000 + 600 000 − 200 000 = 8 400 000; tax = 2 520 000 (teaching rate: check the Finance Law)."),
        PQ("Why does the report advise candidates to use recommended textbooks?",
           "The approach and layout of accounts must follow the syllabus and textbook format, because the examiner marks the correct layout as well as the figures."),
        SUM("Paper 3: Section A (four questions, answer three) and Section B (three questions, answer two); equal marks; ink only.",
            "Bank marks on ratios, invoices and journals, statements, impairment.",
            "Prepare taxation, share valuation and modification of capital: the weak areas in 2023.",
            "Present statements, journals and computations in the correct layout.",
            "Show formulas and steps; do not mix averages with single years."),
    ]))
