"""A Level Accounting (0705), Lower Sixth: Year-End Adjustments, Provisions & Control; OHADA Annual Financial Statements;
and the Examination module (Paper 1, Paper 2, Paper 3).

Draft content written from KKEVO's master curriculum blueprint (ACC-0705-L6M4 and L6M5) and the topic list in
apps/academics/gce_curriculum.py. Exam facts are only those of the Board's 2023 Advanced Level subject report for 0705:
three papers weighted 30, 30 and 40; Paper 1 = 50 compulsory multiple-choice questions (in 2023: 25 financial accounting,
10 cost and management accounting, 15 company accounting and taxation); Paper 2 = Cost and Management Accounting (two
sections, five questions answered); Paper 3 = Financial Accounting (Section A financial accounting, Section B company
accounting and taxation, five questions answered). Lower Sixth work is financial accounting, examined mainly in Paper 3.

The OHADA approach (revised SYSCOHADA) is taught. Account numbers are given only where they are standard in the revised
chart; anything that textbooks present differently is marked "check your textbook". VAT is shown at 19.25%, the standard
Cameroonian rate at the time of writing (check the current Finance Law); the income tax rate in the examples is a
teaching value. All company names and FCFA figures are invented for practice. EVERY figure in the statements, journals,
ledgers and schedules below is computed in this file with plain integer arithmetic and checked by assertions, so printed
totals cannot disagree with the workings.
"""

from .dsl import *  # noqa: F403

COURSE = ("accounting", "lower-sixth")

M_ADJ = "Year-End Adjustments, Provisions & Control"
M_FS = "OHADA Annual Financial Statements"
M_EXAM = "Examination"


# ---------------------------------------------------------------- small formatting helpers (exact integer arithmetic)
def n(x):
    """12345 -> '12 345'; negatives keep a minus sign."""
    s = f"{abs(int(x)):,}".replace(",", " ")
    return ("-" if x < 0 else "") + s


def vat(ht, rate_bp=1925):
    """VAT on an amount excluding tax; rate in basis points (1925 = 19.25%). Asserts the result is a whole franc."""
    assert ht * rate_bp % 10000 == 0, ht
    return ht * rate_bp // 10000


def pct(base, p):
    assert base * p % 100 == 0, (base, p)
    return base * p // 100


def journal(title, entries, w=28):
    """Journal in text form. entries = [(date, [(account, name, debit, credit), ...], narration)].
    Asserts that each entry balances."""
    out = [title, f"{'Acct':<6}{'Account':<{w}}{'Debit':>11}{'Credit':>11}"]
    for date, lines, narr in entries:
        td = sum(d for _, _, d, _ in lines)
        tc = sum(c for _, _, _, c in lines)
        assert td == tc, (title, date, td, tc)
        out.append(f"-- {date} " + "-" * max(0, w + 24 - len(date)))
        for acct, name, d, c in lines:
            out.append(f"{acct:<6}{name:<{w}}{(n(d) if d else ''):>11}{(n(c) if c else ''):>11}".rstrip())
        if narr:
            out.append(f"      ({narr})")
    return "\n".join(out)


def row(label, *vals, w=30, c=12):
    cells = "".join(f"{('' if v is None else (v if isinstance(v, str) else n(v))):>{c}}" for v in vals)
    return f"{label:<{w}}{cells}".rstrip()


def ledger(title, dr, cr, w=26):
    """Two-sided account shown stacked (debit then credit); asserts the totals agree."""
    td, tc = sum(a for _, a in dr), sum(a for _, a in cr)
    assert td == tc, (title, td, tc)
    out = [title, "DEBIT"]
    out += [f"  {l:<{w}}{n(a):>12}" for l, a in dr]
    out += [f"  {'Total':<{w}}{n(td):>12}", "CREDIT"]
    out += [f"  {l:<{w}}{n(a):>12}" for l, a in cr]
    out += [f"  {'Total':<{w}}{n(tc):>12}"]
    return "\n".join(out)


LESSONS = []

# ====================================================================== 1. Impairment of current assets
# Doubtful customers of Ets Fokou (invented for practice). VAT 19.25%.
_ab_ht, _ch_ht = 400_000, 300_000
_ab_ttc, _ch_ttc = _ab_ht + vat(_ab_ht), _ch_ht + vat(_ch_ht)
_ab_imp, _ch_imp = pct(_ab_ht, 40), pct(_ch_ht, 30)
assert (_ab_ttc, _ch_ttc, _ab_imp, _ch_imp) == (477_000, 357_750, 160_000, 90_000)
_imp_N = _ab_imp + _ch_imp
_j_imp1 = journal("Journal of Ets Fokou, 31/12/N", [
    ("31/12/N", [("416", "Doubtful customers", _ab_ttc + _ch_ttc, 0),
                 ("411", "Customers", 0, _ab_ttc + _ch_ttc)], "Abena and Che transferred"),
    ("31/12/N", [("6594", "Impairment charge, rec.", _imp_N, 0),
                 ("491", "Impairment of customers", 0, _imp_N)], "40% x 400 000 + 30% x 300 000"),
])
# year N+1
_ab_paid_ttc = 119_250
_ab_paid_ht = 100_000
assert _ab_paid_ht + vat(_ab_paid_ht) == _ab_paid_ttc
_ab_left_ttc, _ab_left_ht = _ab_ttc - _ab_paid_ttc, _ab_ht - _ab_paid_ht
_ab_new = pct(_ab_left_ht, 50)
_bi_ht = 200_000
_bi_ttc = _bi_ht + vat(_bi_ht)
_bi_new = pct(_bi_ht, 30)
assert (_ab_left_ttc, _ab_left_ht, _ab_new, _bi_ttc, _bi_new) == (357_750, 300_000, 150_000, 238_500, 60_000)
_dot = _bi_new
_rev = (_ab_imp - _ab_new) + _ch_imp
assert (_dot, _rev) == (60_000, 100_000)
_491_end = _imp_N + _dot - _rev
assert _491_end == _ab_new + _bi_new == 210_000
_416_end = _ab_left_ttc + _bi_ttc
assert (_416_end, _416_end - _491_end) == (596_250, 386_250)
_profit_eff = -_dot + _rev - _ch_ht
assert _profit_eff == -260_000
_t_sched = "\n".join([
    "Impairment schedule at 31/12/N+1 (FCFA)",
    f"{'Customer':<9}{'TTC':>9}{'HT':>9}{'Rate':>6}{'Need':>9}{'Old':>9}{'Change':>10}",
    f"{'Abena':<9}{n(_ab_left_ttc):>9}{n(_ab_left_ht):>9}{'50%':>6}{n(_ab_new):>9}{n(_ab_imp):>9}{'-' + n(_ab_imp - _ab_new):>10}",
    f"{'Biyong':<9}{n(_bi_ttc):>9}{n(_bi_ht):>9}{'30%':>6}{n(_bi_new):>9}{'0':>9}{'+' + n(_bi_new):>10}",
    f"{'Che':<9}{'lost':>9}{n(_ch_ht):>9}{'-':>6}{'0':>9}{n(_ch_imp):>9}{'-' + n(_ch_imp):>10}",
    f"{'Totals':<33}{n(_ab_new + _bi_new):>9}{n(_imp_N):>9}",
    f"New charge (6594): {n(_dot)}   Reversals (7594): {n(_rev)}",
])
_j_imp2 = journal("Journal of Ets Fokou, year N+1", [
    ("during N+1", [("521", "Bank", _ab_paid_ttc, 0), ("416", "Doubtful customers", 0, _ab_paid_ttc)], "Abena pays part"),
    ("31/12/N+1", [("416", "Doubtful customers", _bi_ttc, 0), ("411", "Customers", 0, _bi_ttc)], "Biyong transferred"),
    ("31/12/N+1", [("651", "Losses on receivables", _ch_ht, 0), ("4431", "VAT invoiced on sales", vat(_ch_ht), 0),
                   ("416", "Doubtful customers", 0, _ch_ttc)], "Che's debt is lost"),
    ("31/12/N+1", [("6594", "Impairment charge, rec.", _dot, 0), ("491", "Impairment of customers", 0, _dot)], "Biyong 30%"),
    ("31/12/N+1", [("491", "Impairment of customers", _rev, 0), ("7594", "Reversal of impairment", 0, _rev)], "Abena 10 000 + Che 90 000"),
])
_t_491 = ledger("Account 491, year N+1", [("Reversals (7594)", _rev), ("Balance c/d", _491_end)],
                [("Balance b/d", _imp_N), ("Charge (6594)", _dot)])
# inventory impairment
_inv_cost, _inv_sp, _inv_sc = 600_000, 520_000, 40_000
_inv_nrv = _inv_sp - _inv_sc
_inv_imp = _inv_cost - _inv_nrv
assert (_inv_nrv, _inv_imp) == (480_000, 120_000)

LESSONS.append(lesson(
    module=M_ADJ, topic="Impairment of current assets",
    title="Impairment of current assets: doubtful customers and inventory under SYSCOHADA",
    slug="acl2-impairment-of-current-assets", minutes=25,
    summary="Transfer doubtful customers to account 416, impair them on the amount excluding VAT, adjust the impairment each year, write off lost debts with the VAT recovered, and impair inventory whose value has fallen below cost.",
    objectives=[
        "Explain the difference between depreciation of a fixed asset and impairment of a current asset",
        "Record a doubtful customer and calculate its impairment on the amount excluding VAT",
        "Prepare an impairment schedule and journalise the new charge, the reversals and a lost debt",
        "Calculate and record the impairment of inventory whose net realisable value is below cost",
    ],
    key_concepts=["Impairment (dépréciation)", "Doubtful customer (416)", "Amount excluding VAT (HT)", "Impairment schedule",
                  "Reversal of impairment", "Irrecoverable debt (651)", "Net realisable value"],
    blocks=[
        H("Introduction"),
        T("Ets Fokou sells building materials on credit in Bafoussam. At the end of the year some customers have paid late, one has disputed an invoice and one has closed his shop. "
          "The ledger still shows the full amounts owed, but the business does not expect to collect all of it. The **prudence** convention (you met it with the postulates and conventions) says that a probable loss must be recorded now, even though it is not yet certain. "
          "In O Level you called this a provision for doubtful debts. At A Level you record it the SYSCOHADA way, customer by customer, with VAT handled correctly. All names and figures are **invented for practice**."),
        D("**Depreciation** (amortissement) spreads the cost of a fixed asset over its useful life; it is not reversed. **Impairment** (dépréciation) records a probable, **reversible** fall in the value of an asset below its book value. "
          "Current assets that can be impaired include receivables (customers), inventory and short-term investments.", title="Depreciation and impairment"),
        D("A **doubtful customer** is a customer whose debt may not be paid in full (late, disputed or in difficulty). The debt is moved, VAT included, from **411 Customers** to **416 Doubtful customers** so that doubtful debts are seen separately. "
          "The impairment is recorded in **491 Impairment of customer accounts**, a credit balance that is deducted from the receivables on the balance sheet.", title="Doubtful customers"),
        KEY("The SYSCOHADA rules for doubtful customers", "Learn these four rules; most marks in an impairment question depend on them.", cards=[
            ["1. Transfer TTC", "Debit 416, credit 411 with the full amount owed, VAT included (toutes taxes comprises, TTC)."],
            ["2. Impair HT", "The impairment is a percentage of the amount **excluding VAT** (hors taxes, HT): if the debt is lost, the VAT invoiced can usually be recovered from the State, so it is not a loss."],
            ["3. Adjust the change", "Each year compare the impairment needed with the impairment already in 491. An increase is a charge (debit 6594, credit 491); a decrease is a reversal (debit 491, credit 7594)."],
            ["4. Lost debt", "Debit 651 Losses on receivables with the HT amount, debit 4431 VAT invoiced with the VAT, credit 416 with the TTC amount, and reverse the whole impairment held for that customer."],
        ]),
        IMG("alacl2-doubtful-debt-flow.svg",
            alt="Flow from account 411 Customers to 416 Doubtful customers, then three outcomes: paid (credit 416 by bank), still doubtful (adjust 491), lost (651 and 4431, reverse 491).",
            caption="Figure 1. The life of a doubtful customer under SYSCOHADA."),
        EX("Worked example 1: the first year",
           intro="At 31/12/N two customers of Ets Fokou are doubtful. Abena owes FCFA 477 000 TTC and the expected loss is 40%. Che owes FCFA 357 750 TTC and the expected loss is 30%. VAT is 19.25%. Record the year-end entries.",
           steps=[
               S("Find the HT amounts", text="Divide by 1.1925: Abena 477 000 ÷ 1.1925 = 400 000; Che 357 750 ÷ 1.1925 = 300 000."),
               S("Impairment needed", text="Abena 40% × 400 000 = 160 000; Che 30% × 300 000 = 90 000; total 250 000."),
               S("Transfer and charge", text="Debit 416, credit 411 with 834 750 (TTC). Debit 6594, credit 491 with 250 000."),
           ], check=r"0.40 \times 400\,000 + 0.30 \times 300\,000 = 250\,000"),
        CODE(_j_imp1, "text", title="Journal, year N"),
        EX("Worked example 2: the next year, with a recovery and a loss",
           intro="During N+1 Abena pays FCFA 119 250; at 31/12/N+1 her expected loss on the balance is 50%. Che is declared insolvent: nothing more will be received. A new customer, Biyong, owing FCFA 238 500 TTC, becomes doubtful with an expected loss of 30%. Prepare the schedule and the entries.",
           steps=[
               S("Abena", text="Balance 477 000 − 119 250 = 357 750 TTC = 300 000 HT. Needed 50% × 300 000 = 150 000. Old 160 000. Reverse 10 000."),
               S("Biyong", text="238 500 ÷ 1.1925 = 200 000 HT. Needed 30% × 200 000 = 60 000. Old 0. Charge 60 000."),
               S("Che", text="Write off: debit 651 with 300 000 HT and 4431 with 57 750 VAT, credit 416 with 357 750. His old impairment of 90 000 is no longer needed: reverse it."),
               S("Totals", text="New charge 60 000 (6594). Reversals 10 000 + 90 000 = 100 000 (7594). Account 491 closes at 150 000 + 60 000 = 210 000."),
           ]),
        CODE(_t_sched, "text", title="Impairment schedule (état des créances douteuses)"),
        CODE(_j_imp2, "text", title="Journal, year N+1"),
        CODE(_t_491, "text", title="Account 491 closes at the impairment still needed"),
        T("On the balance sheet at 31/12/N+1 the doubtful customers appear at gross 596 250, impairment 210 000, net 386 250 (together with the healthy customers in 411). "
          "The effect on the result of year N+1 is: charge 60 000, reversals +100 000, loss on Che 300 000, so the result falls by 260 000. The VAT on Che's debt (57 750) is not a loss because it is recovered; check the current tax rules for the documents needed to recover VAT on a lost debt."),
        H("Impairment of inventory"),
        D("Inventory is valued at cost. If at the year end its **net realisable value** (expected selling price less the costs still needed to sell it) is below cost, the difference is an impairment: debit **6593** (impairment charge on inventory), credit **39** (impairment of inventory; 391 for goods). "
          "Next year the old impairment is reversed (debit 39, credit 7593) and a new one is calculated.", title="Inventory below cost"),
        EX("Worked example 3: damaged goods",
           intro="Goods in the closing inventory cost FCFA 600 000. They are slightly damaged and are expected to sell for FCFA 520 000, with selling costs of FCFA 40 000. Find the impairment.",
           steps=[
               S("Net realisable value", text="520 000 − 40 000 = 480 000."),
               S("Compare with cost", text="600 000 − 480 000 = 120 000 below cost."),
               S("Entry", text="Debit 6593, credit 391 with 120 000. The inventory appears on the balance sheet at gross 600 000, impairment 120 000, net 480 000."),
           ]),
        MISTAKE("Impairing the amount including VAT",
                "The percentage is applied to the HT amount. 40% of 477 000 (190 800) is wrong; 40% of 400 000 (160 000) is right. Transfers between 411 and 416 and the payments, however, are always TTC."),
        MISTAKE("Charging the whole new impairment again",
                "Only the difference between the impairment needed and the impairment already in 491 is recorded, customer by customer. An old impairment that is too large is reversed to 7594."),
        MISTAKE("Forgetting to reverse the impairment of a lost customer",
                "When a debt is written off to 651, the impairment held for that customer must be reversed in full; otherwise 491 keeps a balance for a customer who no longer exists in 416."),
        QUIZ("A doubtful customer owes FCFA 596 250 TTC (VAT 19.25%). The expected loss is 20%. What impairment is needed?",
             ["FCFA 119 250", "FCFA 100 000", "FCFA 96 250", "FCFA 500 000"], 1,
             "HT = 596 250 ÷ 1.1925 = 500 000. Impairment = 20% × 500 000 = 100 000.",
             hint="Remove the VAT before applying the percentage.",
             feedback=["That is 20% of the TTC amount: VAT must be removed first.", "", "That is the VAT contained in the debt, not the impairment.", "That is the HT debt, not the impairment."]),
        QUIZ("Account 491 holds FCFA 80 000 for a customer. At the year end the impairment needed for that customer is FCFA 50 000. The entry is",
             ["Debit 6594, credit 491 with 50 000", "Debit 491, credit 7594 with 30 000", "Debit 6594, credit 491 with 30 000", "Debit 651, credit 416 with 30 000"], 1,
             "The impairment is too large by 30 000, so 30 000 is reversed: debit 491, credit 7594.",
             feedback=["That records the whole new figure as a charge again.", "", "That increases the impairment, but it must fall.", "Nothing is lost yet; 651 is used only when the debt is irrecoverable."],
             title="Quick check 2"),
        TIP("Impairment of doubtful customers is a typical Paper 3 Section A question: the Board's 2023 report describes a question on calculating impairment and losses on doubtful customers with journal entries, which only about 45% of candidates passed. Draw the schedule first (TTC, HT, rate, needed, old, change), then journalise from it. Paper 1 tests the rules: HT base, which account, increase or reversal.",
            title="Exam link"),
        PQ("At 31/12/N a customer owing FCFA 715 500 TTC (VAT 19.25%) becomes doubtful; the expected loss is 25%. Give the two entries.",
           "Transfer: debit 416, credit 411 with 715 500. HT = 715 500 ÷ 1.1925 = 600 000. Impairment = 25% × 600 000 = 150 000: debit 6594, credit 491 with 150 000."),
        PQ("Next year the same customer pays FCFA 238 500 and the rest is declared lost. Give the entries.",
           "Receipt: debit 521, credit 416 with 238 500. Balance lost = 715 500 − 238 500 = 477 000 TTC = 400 000 HT + 77 000 VAT: debit 651 with 400 000, debit 4431 with 77 000, credit 416 with 477 000. Reverse the old impairment: debit 491, credit 7594 with 150 000."),
        PQ("Goods cost FCFA 900 000. They can be sold for FCFA 850 000 after a repair costing FCFA 70 000. Is there an impairment? If so, give the entry and the net figure on the balance sheet.",
           "Net realisable value = 850 000 − 70 000 = 780 000, below cost by 120 000. Debit 6593, credit 391 with 120 000. Balance sheet: gross 900 000, impairment 120 000, net 780 000."),
        PQ("Explain, with reference to accounting conventions, why the impairment of a receivable is reversible but depreciation of a building is not.",
           "Impairment records a probable loss of value that depends on an estimate (prudence); when the estimate changes (the customer pays, or the risk falls), the impairment must be adjusted so that the asset is not understated. Depreciation records the consumption of the asset's useful life (matching of cost with the years that use it); consumed service potential does not come back, so depreciation is not reversed."),
        SUM("Impairment records a probable, reversible fall in value of a current asset; depreciation spreads the cost of a fixed asset.",
            "Move a doubtful debt TTC from 411 to 416; impair it on the HT amount in 491.",
            "Each year compare the impairment needed with the old one: increase to 6594, decrease to 7594.",
            "A lost debt: debit 651 (HT) and 4431 (VAT), credit 416 (TTC), and reverse its impairment.",
            "Inventory below net realisable value is impaired through 6593 and 39."),
    ]))

# ====================================================================== 2. Provisions for risks and charges
# Menuiserie Tchoupo SARL, Douala (invented for practice)
_lit = [2_500_000, 3_000_000]
_lit_paid = 2_800_000
_lit_eff = [-_lit[0], -(_lit[1] - _lit[0]), _lit[1] - _lit_paid]
assert _lit_eff == [-2_500_000, -500_000, 200_000] and sum(_lit_eff) == -_lit_paid
_j_lit = journal("Menuiserie Tchoupo: the lawsuit", [
    ("31/12/N", [("691", "Provision charge", _lit[0], 0), ("191", "Provision for litigation", 0, _lit[0])], "lawyer's estimate"),
    ("31/12/N+1", [("691", "Provision charge", _lit[1] - _lit[0], 0), ("191", "Provision for litigation", 0, _lit[1] - _lit[0])], "estimate raised to 3 000 000"),
    ("during N+2", [("65x", "Other charges (damages)", _lit_paid, 0), ("521", "Bank", 0, _lit_paid)], "court award paid"),
    ("31/12/N+2", [("191", "Provision for litigation", _lit[1], 0), ("791", "Reversal of provisions", 0, _lit[1])], "risk has ended"),
])
_war_sales, _war_rate, _war_old = 40_000_000, 15, 450_000  # rate in tenths of a percent: 1.5%
assert _war_sales * _war_rate % 1000 == 0
_war_need = _war_sales * _war_rate // 1000
_war_inc = _war_need - _war_old
assert (_war_need, _war_inc) == (600_000, 150_000)
# provisions schedule at 31/12/N+1
_ps = [("Litigation (191)", 2_500_000, 500_000, 0, 3_000_000),
       ("Warranties", 450_000, 150_000, 0, 600_000),
       ("Tax audit risk", 800_000, 0, 800_000, 0)]
for _nm, _o, _c, _r, _cl in _ps:
    assert _o + _c - _r == _cl, _nm
_pt = [sum(x[i] for x in _ps) for i in range(1, 5)]
assert _pt == [3_750_000, 650_000, 800_000, 3_600_000]
_t_ps = "\n".join(
    ["Provisions schedule, year N+1 (FCFA)",
     f"{'Provision':<17}{'Opening':>11}{'Charge':>10}{'Reversal':>10}{'Closing':>11}"]
    + [f"{a:<17}{n(b):>11}{n(c):>10}{n(d):>10}{n(e):>11}" for a, b, c, d, e in _ps]
    + [f"{'Total':<17}{n(_pt[0]):>11}{n(_pt[1]):>10}{n(_pt[2]):>10}{n(_pt[3]):>11}"])

LESSONS.append(lesson(
    module=M_ADJ, topic="Provisions for risks and charges",
    title="Provisions for risks and charges: recognising, adjusting and reversing them",
    slug="acl2-provisions-for-risks-and-charges", minutes=24,
    summary="Recognise a provision for risks and charges when a past event creates a probable outflow that can be estimated, record its increase, use and reversal, keep a provisions schedule, and tell it apart from impairment, reserves and contingent liabilities.",
    objectives=[
        "State the conditions for recognising a provision for risks and charges",
        "Distinguish a provision for risks and charges from an impairment, a reserve and a contingent liability",
        "Record the creation, increase and reversal of a provision and explain the effect on each year's result",
        "Prepare a provisions schedule and evaluate the use of provisions",
    ],
    key_concepts=["Provision for risks and charges", "Present obligation", "Probable outflow", "Reliable estimate",
                  "Reversal (reprise)", "Contingent liability", "Provisions schedule"],
    blocks=[
        H("Introduction"),
        T("Menuiserie Tchoupo SARL makes furniture in Douala. At 31 December a former worker has taken the company to court for unfair dismissal, and every chair sold carries a one-year guarantee. "
          "Neither cost has been paid yet, and nobody knows the exact amount. Yet both come from events of this year. A **provision for risks and charges** puts a careful estimate of such costs into this year's accounts. "
          "All names and figures are **invented for practice**."),
        D("A **provision for risks and charges** is a liability whose amount or timing is uncertain. It is recognised at the year end when three conditions hold: "
          "(1) the business has an **obligation** to a third party at the closing date, arising from a **past event**; (2) it is **probable** that money (or other resources) will leave the business to settle it; "
          "(3) the amount can be **estimated reliably**.", title="Provision for risks and charges"),
        IMG("alacl2-provision-tests.svg",
            alt="Decision chart: obligation from a past event? If no, nothing is recorded. If yes, is an outflow probable? If no, disclose a contingent liability in the notes. If yes, can it be estimated reliably? If yes, record a provision; if no, disclose in the notes.",
            caption="Figure 1. Three questions decide between a provision, a note and nothing."),
        KEY("Four ideas that students mix up", "Each one is shown in a different place in the statements.", cards=[
            ["Impairment", "A fall in the value of an **asset** (customers, inventory). Credit 49, 39, 29: deducted from the asset."],
            ["Provision for risks and charges", "A probable **liability** of uncertain amount. Credit 19 (long term) or 499 (short term): shown with liabilities."],
            ["Reserve", "Part of the **profit** kept in the business after the result is known. Not a charge; it is equity."],
            ["Contingent liability", "A possible obligation, or one that cannot be measured. Not recorded: explained in the notes."],
        ]),
        D("Long-term provisions (more than a year) go to **class 19**, for example **191 Provisions for litigation**, with the charge in **691** and the reversal in **791**. "
          "Provisions for risks expected within a year are short-term: **499**, charge **6591**, reversal **7591**, shown in current liabilities. "
          "A provision linked to an event outside ordinary activities uses the HAO accounts. Textbooks differ in the detail of these numbers: check your textbook.", title="Accounts in the revised SYSCOHADA"),
        EX("Worked example 1: a lawsuit over three years",
           intro="At 31/12/N the lawyer estimates that Tchoupo will have to pay FCFA 2 500 000. At 31/12/N+1 she raises the estimate to FCFA 3 000 000. In N+2 the court orders a payment of FCFA 2 800 000, paid by bank. Record each year and show the effect on each result.",
           steps=[
               S("Year N", text="Obligation from a past event (the dismissal), probable payment, reliable estimate: provision 2 500 000. Result −2 500 000."),
               S("Year N+1", text="Needed 3 000 000, held 2 500 000: increase 500 000 (debit 691, credit 191). Result −500 000."),
               S("Year N+2", text="Record the real cost 2 800 000 as a charge, and reverse the whole provision of 3 000 000 (debit 191, credit 791), as the risk has ended. Net effect +200 000."),
               S("Check over the three years", text="−2 500 000 − 500 000 + 200 000 = −2 800 000, exactly the amount paid. Provisions move the cost to the year of the event; they do not change the total."),
           ], check=r"-2\,500\,000 - 500\,000 + 200\,000 = -2\,800\,000"),
        CODE(_j_lit, "text", title="Journal (the damages account is shown as 65x: check your textbook)"),
        EX("Worked example 2: warranties",
           intro="Sales of furniture in N+1 are FCFA 40 000 000. Past experience shows that repairs under the one-year guarantee cost about 1.5% of sales. The warranty provision brought forward is FCFA 450 000. Record the year-end adjustment.",
           steps=[
               S("Provision needed", text="1.5% × 40 000 000 = 600 000."),
               S("Change", text="600 000 − 450 000 = 150 000 increase."),
               S("Entry", text="The guarantee runs for one year, so this is a short-term provision: debit 6591, credit 499 with 150 000. If the provision needed had been lower, the excess would be reversed to 7591."),
           ]),
        T("At the year end the accountant reviews every provision. A provision whose risk has disappeared, like a tax audit that ended without any claim, must be **reversed** in full: keeping it would hide profit."),
        CODE(_t_ps, "text", title="Provisions schedule (it also appears in the notes to the statements)"),
        H("Evaluation: why examiners and auditors watch provisions"),
        T("Provisions apply **prudence**: a probable cost is not ignored just because it is unpaid. But they rest on estimates, so they can be misused. A manager could create a large provision in a good year and reverse it in a bad year to smooth profits, or record a provision for 'general risks' with no real obligation. "
          "The three conditions, the yearly review and the notes to the statements limit this. For tax purposes a provision is deductible only under conditions set by the tax law; check the current General Tax Code (taxation is studied in Upper Sixth)."),
        MISTAKE("Providing for future operating losses or general risks",
                "No past event, no present obligation: no provision. 'Next year may be difficult' is not a reason to record a charge."),
        MISTAKE("Treating a provision as a reserve",
                "A provision is a charge that reduces the result and is shown with liabilities. A reserve is part of the profit kept after the result is known."),
        MISTAKE("Forgetting to reverse a provision when the risk ends",
                "When the cost is paid or the risk disappears, reverse the whole provision (791 or 7591) and record any real cost separately."),
        QUIZ("Which situation requires a provision for risks and charges at 31 December N?",
             ["The managers expect sales to fall in N+1", "A customer has sued the company for faulty goods delivered in N and a payment is probable", "The company plans to buy a new lorry in N+1", "Profit for N is high and the owners want to keep some of it"], 1,
             "The faulty goods are a past event creating a probable payment that can be estimated.",
             hint="Look for a past event that creates an obligation.",
             feedback=["A fall in sales is a future business risk with no obligation.", "", "A planned purchase is a future decision, not an obligation.", "Keeping profit is a reserve, an appropriation of profit."]),
        QUIZ("A provision of FCFA 1 200 000 is held for a lawsuit. The case ends with a payment of FCFA 900 000. What is the net effect on the result of that year?",
             ["Profit falls by 900 000", "Profit rises by 300 000", "Profit falls by 300 000", "No effect"], 1,
             "Charge 900 000, reversal 1 200 000: net +300 000.",
             feedback=["That ignores the reversal of the provision.", "", "The provision was larger than the payment, so profit rises.", "The charge and the reversal are different amounts."],
             title="Quick check 2"),
        TIP("Provisions appear in Paper 1 (which item is a provision, which account, the effect on profit) and inside Paper 3 questions on year-end adjustments and on preparing statements. Write the three conditions when asked to justify a provision, and keep the schedule: opening + charge − reversal = closing.",
            title="Exam link"),
        PQ("A provision for a lawsuit was FCFA 1 800 000 at 31/12/N. At 31/12/N+1 the lawyer estimates FCFA 1 500 000. Give the entry.",
           "The provision is too large by 300 000: debit 191 (provision for litigation), credit 791 (reversal of provisions) with 300 000. The result of N+1 rises by 300 000."),
        PQ("Sales are FCFA 25 000 000 and warranty costs are estimated at 2% of sales. The warranty provision brought forward is FCFA 650 000. Calculate and record the adjustment.",
           "Needed 2% × 25 000 000 = 500 000. Held 650 000. Reverse 150 000: debit 499, credit 7591 with 150 000."),
        PQ("Complete: opening provisions FCFA 2 000 000, charges FCFA 700 000, reversals FCFA 450 000. Closing provisions?",
           "2 000 000 + 700 000 − 450 000 = 2 250 000."),
        PQ("Discuss whether provisions make financial statements more reliable or less reliable.",
           "Plan: (1) More reliable: prudence and matching put a probable cost into the year that caused it, so profit is not overstated and liabilities are complete. (2) Less reliable: provisions depend on estimates; managers can over-provide in good years and reverse in bad years to smooth profit. (3) Safeguards: the three recognition conditions, the yearly review and reversal of provisions no longer needed, the provisions schedule in the notes, and the auditor's work. Conclusion: provisions improve reliability when the rules are applied honestly and disclosed."),
        SUM("A provision for risks and charges is a liability of uncertain amount or timing.",
            "Recognise it only if there is an obligation from a past event, a probable outflow and a reliable estimate; otherwise disclose a contingent liability or do nothing.",
            "Record only the change each year: increase to 691 (or 6591), decrease to 791 (or 7591); long-term provisions in 19, short-term in 499.",
            "When the risk ends, reverse the whole provision and record the real cost; over the life, the total charge equals the cost.",
            "Provisions are not reserves and not impairments; they are reviewed every year and shown in the provisions schedule."),
    ]))

# ====================================================================== 3. Accruals and prepayments
# Ets Ngo Bilong, Yaounde (invented for practice); year ends 31/12/N
_ins_paid, _ins_months_next = 1_200_000, 9
_ins_pre = _ins_paid * _ins_months_next // 12
assert _ins_paid * _ins_months_next % 12 == 0 and _ins_pre == 900_000
_elec = 85_000
_rent_rec, _rent_next = 1_800_000, 4
_rent_adv = _rent_rec * _rent_next // 6
assert _rent_rec * _rent_next % 6 == 0 and _rent_adv == 1_200_000
_comm = 150_000
_wage = 240_000
_profit0 = 5_000_000
_profit1 = _profit0 + _ins_pre - _elec - _rent_adv + _comm - _wage
assert _profit1 == 4_525_000
_j_acc = journal("Ets Ngo Bilong: year-end regularisation, 31/12/N", [
    ("31/12/N", [("476", "Prepaid expenses", _ins_pre, 0), ("625", "Insurance premiums", 0, _ins_pre)], "9/12 of 1 200 000"),
    ("31/12/N", [("605", "Electricity (other purch.)", _elec, 0), ("408", "Suppl., invoices to come", 0, _elec)], "December use"),
    ("31/12/N", [("707", "Ancillary income (rent)", _rent_adv, 0), ("477", "Income in advance", 0, _rent_adv)], "4/6 of 1 800 000"),
    ("31/12/N", [("418", "Cust., invoices to issue", _comm, 0), ("707", "Ancillary income (comm.)", 0, _comm)], "earned, not invoiced"),
    ("31/12/N", [("661", "Wages", _wage, 0), ("428", "Staff, accrued charges", 0, _wage)], "December overtime"),
])
_j_rev = journal("Reversal on 1/1/N+1 and the real invoice", [
    ("01/01/N+1", [("625", "Insurance premiums", _ins_pre, 0), ("476", "Prepaid expenses", 0, _ins_pre)], "reversal"),
    ("01/01/N+1", [("408", "Suppl., invoices to come", _elec, 0), ("605", "Electricity (other purch.)", 0, _elec)], "reversal"),
    ("15/01/N+1", [("605", "Electricity (other purch.)", _elec, 0), ("401", "Suppliers", 0, _elec)], "invoice arrives"),
])
_t_eff = "\n".join([
    "Effect on the result of year N (FCFA)",
    row("Result before adjustments", _profit0, w=34),
    row("+ Insurance prepaid", _ins_pre, w=34),
    row("- Electricity accrued", -_elec, w=34),
    row("- Rent received in advance", -_rent_adv, w=34),
    row("+ Commission accrued", _comm, w=34),
    row("- Overtime accrued", -_wage, w=34),
    row("Corrected result", _profit1, w=34),
])

LESSONS.append(lesson(
    module=M_ADJ, topic="Accruals and prepayments",
    title="Accruals and prepayments: regularising expenses and revenues under SYSCOHADA",
    slug="acl2-accruals-and-prepayments", minutes=24,
    summary="Apply the accrual basis at the year end with the SYSCOHADA regularisation accounts (476, 477, 408, 418, 428), reverse the entries at the start of the next year, and measure the effect on the result and the balance sheet.",
    objectives=[
        "Explain the accrual basis and the independence of financial years",
        "Calculate prepaid and accrued expenses and revenues by time apportionment",
        "Record year-end regularisation entries in the SYSCOHADA accounts and reverse them on the first day of the next year",
        "State the effect of each adjustment on the result and on the balance sheet",
    ],
    key_concepts=["Independence of financial years", "Prepaid expense (476)", "Income received in advance (477)",
                  "Accrued expense (408, 428)", "Accrued income (418)", "Reversal (extourne)"],
    blocks=[
        H("Introduction"),
        T("Ets Ngo Bilong, a wholesaler in Yaoundé, pays its insurance a year in advance, receives rent from a tenant every six months and pays its electricity a month late. "
          "Cash moves at dates that do not match the financial year, so the accounts must be **regularised** at 31 December: each year keeps only the expenses and revenues that belong to it. All figures are **invented for practice**."),
        D("Under the **accrual basis**, an expense or revenue belongs to the year in which the service is used or earned, not the year in which cash is paid or received. The OHADA convention of the **independence of financial years** (indépendance des exercices) applies this to each year.", title="Accrual basis"),
        KEY("Four adjustments and their SYSCOHADA accounts", "Two remove amounts from this year; two add amounts to it.", cards=[
            ["Prepaid expense", "Paid in N for N+1. Debit 476 Prepaid expenses, credit the expense account. A current asset."],
            ["Accrued expense", "Used in N, not yet invoiced or paid. Debit the expense, credit 408 (supplier invoices to come), 428 (staff) or another 'charges to pay' account. A current liability."],
            ["Income received in advance", "Received in N for N+1. Debit the income account, credit 477 Income received in advance. A current liability."],
            ["Accrued income", "Earned in N, not yet invoiced. Debit 418 (customers, invoices to issue), credit the income account. A current asset."],
        ]),
        IMG("alacl2-cutoff-timeline.svg",
            alt="Timeline from 1 October N to 30 September N+1 with the year end on 31 December N: 3 months (300 000) belong to N and 9 months (900 000) to N+1.",
            caption="Figure 1. Time apportionment of an insurance premium of FCFA 1 200 000 paid on 1 October N."),
        EX("Worked example 1: time apportionment",
           intro="On 1/10/N the business paid FCFA 1 200 000 for a year's insurance. On 1/11/N a tenant paid FCFA 1 800 000 rent for six months. Find the amounts to carry forward at 31/12/N.",
           steps=[
               S("Insurance", text="Cover runs October N to September N+1: 3 months in N, 9 months in N+1. Prepaid 9/12 × 1 200 000 = 900 000."),
               S("Rent received", text="November N to April N+1: 2 months in N, 4 months in N+1. Received in advance 4/6 × 1 800 000 = 1 200 000."),
           ], check=r"\tfrac{9}{12} \times 1\,200\,000 = 900\,000"),
        EX("Worked example 2: all the year-end entries",
           intro="In addition: December electricity of FCFA 85 000 has not been invoiced; commission of FCFA 150 000 earned in December has not been invoiced; December overtime of FCFA 240 000 is unpaid. Record the regularisation (VAT ignored for simplicity).",
           steps=[
               S("Prepaid insurance", text="Debit 476, credit 625 with 900 000."),
               S("Electricity", text="Debit 605, credit 408 with 85 000."),
               S("Rent received in advance", text="Debit 707, credit 477 with 1 200 000."),
               S("Commission", text="Debit 418, credit 707 with 150 000."),
               S("Overtime", text="Debit 661, credit 428 with 240 000."),
           ]),
        CODE(_j_acc, "text", title="Journal of regularisation"),
        T("In practice the VAT on an invoice not yet received, or not yet issued, is recorded in a separate State account; textbooks differ on the account used, so check your textbook."),
        CODE(_t_eff, "text", title="Effect on the result"),
        H("Reversing on the first day of the next year"),
        T("The SYSCOHADA method keeps the expense and income accounts as they were recorded during the year and adjusts them through the class 4 regularisation accounts. On 1 January N+1 each entry is **reversed** (extourne). "
          "Then, when the real invoice arrives, it is recorded normally and the two entries cancel out for N+1. Without the reversal, the electricity of December would be charged twice, once in N and again in N+1."),
        CODE(_j_rev, "text", title="Reversal and the real invoice"),
        T("At 31/12/N the balance sheet shows 476 (900 000) and 418 (150 000) with receivables in current assets, and 408 (85 000), 428 (240 000) and 477 (1 200 000) in current liabilities. "
          "In the O Level ledger method you carried these balances down in each expense account; the totals are the same."),
        MISTAKE("Getting the direction of the adjustment wrong",
                "A prepaid expense **reduces** this year's expense (credit the expense). An accrued expense **increases** it (debit the expense). Say 'used in N or not?' before writing the entry."),
        MISTAKE("Counting months wrongly",
                "From 1 October to 31 December is 3 months, not 2. Write the months on a small timeline before multiplying."),
        MISTAKE("Forgetting the reversal",
                "If the regularisation is not reversed on 1 January, the next year's expense or income is counted twice or not at all."),
        QUIZ("On 1/8/N a business pays rent of FCFA 2 400 000 for 12 months. The year ends on 31/12/N. The year-end entry is",
             ["Debit 476, credit 622 with 1 400 000", "Debit 476, credit 622 with 1 000 000", "Debit 622, credit 476 with 1 400 000", "Debit 622, credit 408 with 1 000 000"], 0,
             "August to December is 5 months in N; 7 months (7/12 × 2 400 000 = 1 400 000) are prepaid.",
             hint="Count the months that belong to N+1.",
             feedback=["", "That is the part that belongs to N, not the prepaid part.", "The direction is reversed: prepaid rent is an asset, so 476 is debited.", "Nothing is owed: the rent has been paid."]),
        QUIZ("Which account records income received in N for services to be provided in N+1?",
             ["476", "477", "418", "408"], 1,
             "477 Income received in advance is a current liability.",
             feedback=["476 is for prepaid expenses (an asset).", "", "418 is for income earned but not yet invoiced.", "408 is for supplier invoices still to come."],
             title="Quick check 2"),
        TIP("Regularisation appears in Paper 1 (accounts, direction and time apportionment) and in Paper 3 adjustments before the income statement and the balance sheet. Show the fraction of the year in your working: examiners give method marks for it.",
            title="Exam link"),
        PQ("A loan of FCFA 6 000 000 at 10% a year was taken on 1/9/N. Interest is paid once a year on 31 August. Calculate the interest to accrue at 31/12/N and give the entry.",
           "Interest for September to December = 6 000 000 × 10% × 4/12 = 200 000. Debit 671 (interest on loans), credit the accrued interest account (166 in many textbooks; check your textbook) with 200 000."),
        PQ("A tenant pays FCFA 900 000 on 1/12/N for three months' rent. Calculate the income received in advance and give the entry.",
           "December is 1 month in N; 2 months belong to N+1: 2/3 × 900 000 = 600 000. Debit 707, credit 477 with 600 000."),
        PQ("Before adjustments the result is FCFA 3 200 000. Adjustments: prepaid insurance 400 000, accrued electricity 60 000, income received in advance 300 000, accrued commission 90 000. Find the corrected result.",
           "3 200 000 + 400 000 − 60 000 − 300 000 + 90 000 = 3 330 000."),
        PQ("Explain why the regularisation entries are reversed on 1 January.",
           "The expense and income accounts of N+1 start from zero and the real invoices of N+1 are recorded in full. Reversing moves the amount carried forward back into the N+1 accounts, so that the invoice and the reversal cancel for the part that belongs to N. Without it, the amount would be charged (or credited) twice."),
        SUM("The accrual basis gives each year only its own expenses and revenues (independence of financial years).",
            "Prepaid expense: debit 476, credit the expense. Accrued expense: debit the expense, credit 408 or 428.",
            "Income received in advance: debit the income, credit 477. Accrued income: debit 418, credit the income.",
            "Calculate by time apportionment on a timeline; reverse all regularisation entries on 1 January of the next year."),
    ]))

# ====================================================================== 4. Bank reconciliation
# Quincaillerie Mbah & Co, Bamenda (invented for practice), 31 December N
_bk, _st = 1_846_000, 2_279_500
_unpres = [450_000, 215_000]
_uncr = 380_000
_charges, _transfer, _unpaid = 18_500, 260_000, 120_000
_err = 185_000 - 158_000
_bk_dr = _bk + _transfer + _err
_bk_cr = _charges + _unpaid
_bk_adj = _bk_dr - _bk_cr
_st_dr = sum(_unpres)
_st_cr = _st + _uncr
_st_adj = _st_cr - _st_dr
assert (_err, _bk_adj, _st_adj, sum(_unpres)) == (27_000, 1_994_500, 1_994_500, 665_000)


def _c(v):
    return "" if not v else n(v)


_rec_rows = [("Balances 31/12", _bk, 0, 0, _st), ("Cheques 4521, 4527", 0, 0, sum(_unpres), 0),
             ("Deposit 31/12", 0, 0, 0, _uncr), ("Bank charges", 0, _charges, 0, 0), ("Transfer Mbah", _transfer, 0, 0, 0),
             ("Unpaid cheque Tita", 0, _unpaid, 0, 0), ("Error chq to supplier", _err, 0, 0, 0),
             ("Adjusted balance", 0, _bk_adj, _st_adj, 0)]
_tots = [sum(r[i] for r in _rec_rows) for i in range(1, 5)]
assert _tots[0] == _tots[1] == 2_133_000 and _tots[2] == _tots[3] == 2_659_500
_t_rec = "\n".join(
    ["Bank reconciliation statement at 31/12/N",
     f"{'':<21}{'521 in our books':^20}{'Bank statement':^20}",
     f"{'':<21}{'Debit':>10}{'Credit':>10}{'Debit':>10}{'Credit':>10}"]
    + [f"{r[0]:<21}{_c(r[1]):>10}{_c(r[2]):>10}{_c(r[3]):>10}{_c(r[4]):>10}" for r in _rec_rows]
    + [f"{'Totals':<21}{n(_tots[0]):>10}{n(_tots[1]):>10}{n(_tots[2]):>10}{n(_tots[3]):>10}"])
_j_bank = journal("Entries in the books of Mbah & Co, 31/12/N", [
    ("31/12/N", [("631", "Bank charges", _charges, 0), ("521", "Bank", 0, _charges)], "per statement"),
    ("31/12/N", [("521", "Bank", _transfer, 0), ("411", "Customers (Mbah)", 0, _transfer)], "transfer received"),
    ("31/12/N", [("411", "Customers (Tita)", _unpaid, 0), ("521", "Bank", 0, _unpaid)], "cheque returned unpaid"),
    ("31/12/N", [("521", "Bank", _err, 0), ("401", "Suppliers", 0, _err)], "185 000 recorded for 158 000"),
])
_t_short = "\n".join([
    "Short form (starting from the statement)",
    row("Balance per bank statement", _st, w=32),
    row("Less cheques not yet presented", -sum(_unpres), w=32),
    row("Add deposit not yet credited", _uncr, w=32),
    row("= Adjusted balance in 521", _st_adj, w=32),
])

LESSONS.append(lesson(
    module=M_ADJ, topic="Bank reconciliation",
    title="Bank reconciliation: the four-column statement and the correcting entries",
    slug="acl2-bank-reconciliation", minutes=24,
    summary="Compare account 521 with the bank statement, explain each difference as timing, bank-only item or error, prepare the four-column reconciliation statement, and journalise the items that belong in the business's books.",
    objectives=[
        "Explain why account 521 and the bank statement are mirror images and why their balances differ",
        "Classify each difference as an item for the books or an item for the reconciliation only",
        "Prepare a four-column bank reconciliation statement and the correcting journal entries",
        "Evaluate bank reconciliation as an internal control",
    ],
    key_concepts=["Bank statement", "Mirror image", "Unpresented cheque", "Deposit not yet credited",
                  "Bank charges and direct transfers", "Dishonoured (unpaid) cheque", "Reconciliation statement"],
    blocks=[
        H("Introduction"),
        T("Every month Quincaillerie Mbah & Co in Bamenda receives a statement from its bank. The balance on it never equals the balance of account **521 Banks** in the company's books. "
          "Some differences are only a matter of time, some are items the company has not yet heard of, and some are mistakes. A **bank reconciliation** explains every franc of the difference. All figures are **invented for practice**."),
        D("The bank keeps an account for the business in its own books. What is an **asset** for the business (money at the bank) is a **debt** for the bank. So a deposit is a **debit** in 521 but a **credit** on the statement, and a cheque paid out is a credit in 521 but a debit on the statement. A debit balance in 521 matches a credit balance on the statement.", title="Mirror image"),
        IMG("alacl2-bank-mirror.svg",
            alt="Two accounts side by side: 521 in the business's books with deposits on the debit side and cheques on the credit side, and the bank's account for the business with the same items on the opposite sides.",
            caption="Figure 1. The same operations appear on opposite sides in the two records."),
        KEY("Three kinds of difference", "Each kind is treated differently.", cards=[
            ["Timing (reconciliation only)", "Cheques issued but not yet presented to the bank; deposits made but not yet credited. The bank will record them soon: no entry in the books."],
            ["Items known only to the bank (record in the books)", "Bank charges, interest, direct transfers from customers, standing orders, cheques returned unpaid."],
            ["Errors", "An error in the books is corrected in the books; an error by the bank is reported to the bank and shown in its column."],
        ]),
        EX("Worked example 1: find and classify the differences",
           intro="At 31/12/N account 521 shows a debit balance of FCFA 1 846 000; the statement shows a credit balance of FCFA 2 279 500. Ticking the two records shows: cheques 4521 (450 000) and 4527 (215 000) not yet on the statement; a deposit of 380 000 on 31/12 not yet on the statement; bank charges 18 500; a transfer from customer Mbah 260 000; a cheque from customer Tita 120 000 returned unpaid; and a cheque of 158 000 to a supplier recorded in 521 as 185 000.",
           steps=[
               S("Timing items (statement column)", text="Unpresented cheques 665 000 and the deposit 380 000."),
               S("Bank-only items (book column)", text="Charges 18 500 (credit 521), transfer 260 000 (debit 521), unpaid cheque 120 000 (credit 521)."),
               S("Error in the books", text="Too much was credited: 185 000 − 158 000 = 27 000. Debit 521 with 27 000."),
               S("Adjusted book balance", text="1 846 000 − 18 500 + 260 000 − 120 000 + 27 000 = 1 994 500 debit."),
               S("Adjusted statement balance", text="2 279 500 − 665 000 + 380 000 = 1 994 500 credit. The two agree."),
           ], check=r"1\,846\,000 - 18\,500 + 260\,000 - 120\,000 + 27\,000 = 2\,279\,500 - 665\,000 + 380\,000"),
        CODE(_t_rec, "text", title="Four-column reconciliation statement (état de rapprochement)"),
        T("Read the statement column by column. In the 521 columns, each item is on the side where the company must now record it. In the bank columns, each item is on the side where the bank will record it. "
          "The adjusted balances are equal and on opposite sides: 1 994 500 debit in 521 and 1 994 500 credit at the bank."),
        CODE(_j_bank, "text", title="Journal entries from the reconciliation"),
        CODE(_t_short, "text", title="Another common layout"),
        T("Only the items in the 521 columns are journalised. The bank's columns need no entry: next month's statement will show the cheques and the deposit. If they do not appear within a reasonable time, the accountant investigates (a stale cheque may need to be cancelled)."),
        H("Evaluation: a control, not a guarantee"),
        T("A reconciliation compares two independent records, so it finds errors in either, reveals bank charges and unpaid cheques quickly, and discourages fraud, especially when the person who reconciles does not also sign cheques. "
          "It cannot find a payment recorded in both records for the wrong purpose, and it is useless if it is done months late. That is why businesses reconcile every month."),
        MISTAKE("Putting unpresented cheques in the books",
                "Unpresented cheques and uncredited deposits are already in 521. They are timing differences: they go in the bank columns only."),
        MISTAKE("Forgetting the mirror image",
                "A debit balance in 521 corresponds to a credit balance on the statement. If both are written on the same side, every adjustment goes the wrong way."),
        MISTAKE("Treating an unpaid cheque as a bank charge",
                "A cheque returned unpaid means the customer still owes the money: debit 411 (the customer), credit 521, not an expense."),
        QUIZ("Which item must be recorded in account 521 after the reconciliation?",
             ["A cheque issued on 30 December not yet presented", "A deposit made on 31 December not yet credited", "Interest charged by the bank on an overdraft", "A cheque wrongly entered by the bank in another customer's account"], 2,
             "Interest is known only from the statement, so the business must record it (debit 67, credit 521).",
             hint="Which item has the business not yet recorded?",
             feedback=["It is already in 521; the bank will record it later.", "It is already in 521; the bank will credit it soon.", "", "This is the bank's error; it is shown in the bank columns and reported to the bank."]),
        QUIZ("521 shows a debit balance of FCFA 500 000. The only differences are unpresented cheques of FCFA 80 000. The statement balance should be",
             ["Credit 580 000", "Credit 420 000", "Debit 580 000", "Debit 420 000"], 0,
             "The bank has not yet paid the cheques, so it still holds 80 000 more: credit 500 000 + 80 000 = 580 000.",
             feedback=["", "That subtracts the cheques instead of adding them back.", "Right amount, but a positive balance at the bank is a credit on the statement.", "Wrong side and wrong amount."],
             title="Quick check 2"),
        TIP("Bank reconciliation is a standard financial accounting exercise: Paper 1 asks for an adjusted balance or a classification, and Paper 3 may ask for the corrected 521 and the reconciliation statement. Label each item and show both adjusted balances agreeing.",
            title="Exam link"),
        PQ("521 shows a debit of FCFA 2 150 000. Unpresented cheques FCFA 340 000; deposit not credited FCFA 210 000; bank charges FCFA 12 000 not in the books; a standing order for insurance FCFA 95 000 not in the books. Find the adjusted 521 balance and the statement balance.",
           "Adjusted 521 = 2 150 000 − 12 000 − 95 000 = 2 043 000 debit. Statement = 2 043 000 + 340 000 − 210 000 = 2 173 000 credit."),
        PQ("The books show an overdraft of FCFA 300 000 (credit balance in 521) after all corrections. Unpresented cheques are FCFA 120 000 and a deposit of FCFA 50 000 is not yet credited. What overdraft does the statement show?",
           "The bank has not yet paid 120 000 of cheques, so its overdraft is smaller by 120 000; it has not yet received 50 000, so its overdraft is larger by 50 000: 300 000 − 120 000 + 50 000 = 230 000 overdraft (a debit balance on the statement)."),
        PQ("Give the journal entries for: a direct transfer of FCFA 75 000 from customer Ewane; a cheque of FCFA 64 000 to a supplier recorded in 521 as FCFA 46 000.",
           "Debit 521, credit 411 (Ewane) with 75 000. The cheque was under-recorded by 18 000: debit 401, credit 521 with 18 000."),
        SUM("521 and the bank statement are mirror images: a debit in one is a credit in the other.",
            "Timing differences (unpresented cheques, uncredited deposits) go in the bank columns only.",
            "Items known only to the bank (charges, interest, transfers, unpaid cheques) and errors in the books are recorded in 521.",
            "Both adjusted balances must agree, on opposite sides; reconcile monthly as an internal control."),
    ]))

# ====================================================================== 5. Correction of errors
# Ets Kum Enterprise, Kumba (invented for practice)
_tb_dr, _tb_cr = 15_284_100, 15_357_000
_susp = _tb_cr - _tb_dr
_e1, _e2, _e3, _e4 = 90_000, 72_000, 36_000, 99_000 - 9_900
_e5_ht = 250_000
_e5_vat = vat(_e5_ht)
assert (_susp, _e4, _e5_vat) == (72_900, 89_100, 48_125)
# suspense must clear: debit side = opening debit + corrections debited; credit side = corrections credited
assert _susp + _e4 == _e1 + _e2 == 162_000
_pr0 = 3_480_000
_pr1 = _pr0 - _e1 - _e3 + _e4 + _e5_ht
assert _pr1 == 3_693_100
_j_err = journal("Correcting entries, Ets Kum Enterprise, 31/12/N", [
    ("(1)", [("701", "Sales of goods", _e1, 0), ("47x", "Suspense account", 0, _e1)], "sales overcast"),
    ("(2)", [("401", "Suppliers (Fon)", _e2, 0), ("47x", "Suspense account", 0, _e2)], "debit to Fon omitted"),
    ("(3)", [("624", "Repairs and maintenance", _e3, 0), ("245", "Transport equipment", 0, _e3)], "repairs capitalised"),
    ("(4)", [("47x", "Suspense account", _e4, 0), ("707", "Ancillary income (comm.)", 0, _e4)], "99 000 entered as 9 900"),
    ("(5)", [("411", "Customers (Kum)", _e5_ht + _e5_vat, 0), ("701", "Sales of goods", 0, _e5_ht),
             ("4431", "VAT invoiced on sales", 0, _e5_vat)], "credit sale omitted"),
])
_t_susp = ledger("Suspense account (47x)", [("Difference in trial bal.", _susp), ("(4) Commission", _e4)],
                 [("(1) Sales overcast", _e1), ("(2) Supplier Fon", _e2)])
_t_prof = "\n".join([
    "Statement of corrected result (FCFA)",
    row("Draft result", _pr0, w=34),
    row("(1) Sales overcast", -_e1, w=34),
    row("(2) Supplier not debited", "0", w=34),
    row("(3) Repairs capitalised", -_e3, w=34),
    row("(4) Commission understated", _e4, w=34),
    row("(5) Credit sale omitted (HT)", _e5_ht, w=34),
    row("Corrected result", _pr1, w=34),
])

LESSONS.append(lesson(
    module=M_ADJ, topic="Correction of errors",
    title="Correction of errors: the suspense account, correcting entries and the corrected result",
    slug="acl2-correction-of-errors", minutes=25,
    summary="Classify errors by whether they upset the trial balance, open and clear a suspense account, correct errors by journal entries without erasing anything, and prepare a statement of corrected result.",
    objectives=[
        "Classify errors into those that do and do not affect the agreement of the trial balance",
        "Open a suspense account and clear it with correcting journal entries",
        "Correct errors by reversing or complementary entries, as the OHADA rules require",
        "Calculate the effect of each correction on the result and prepare a statement of corrected result",
    ],
    key_concepts=["Trial balance", "Error of principle", "Error of omission", "Casting error", "Suspense account",
                  "Correcting entry (contre-passation)", "Corrected result"],
    blocks=[
        H("Introduction"),
        T("The accountant of Ets Kum Enterprise in Kumba extracts the trial balance at 31 December and the two totals do not agree. Some errors have caused the difference; others are hidden because the trial balance agrees in spite of them. "
          "At A Level you must find, classify and correct errors, and say how each correction changes the result. All figures are **invented for practice**."),
        D("The **trial balance** lists every account balance; total debits must equal total credits. Its agreement proves only that debits and credits are equal, not that the entries are right.", title="What a trial balance proves"),
        IMG("alacl2-error-types.svg",
            alt="Tree of errors. Trial balance agrees: omission, commission, principle, original entry, complete reversal, compensating. Trial balance disagrees: one side omitted, wrong amount on one side, casting, both entries on one side, transposed on one side; corrected via suspense.",
            caption="Figure 1. Two families of errors."),
        KEY("Errors the trial balance cannot show", "Debits still equal credits, so no suspense account is involved.", cards=[
            ["Omission", "The whole transaction is left out."],
            ["Commission", "Right type of account, wrong person: a payment from Ewane credited to Ebai."],
            ["Principle", "Wrong class of account: repairs (an expense) debited to a fixed asset."],
            ["Original entry", "A wrong amount used on both sides, for example from a wrongly copied invoice."],
            ["Complete reversal", "Right accounts, debit and credit swapped."],
            ["Compensating", "Two errors of the same amount on opposite sides cancel out."],
        ]),
        D("When the totals do not agree and the cause is not found at once, the difference is put in a **suspense account** (a class 47 waiting account; check your textbook for its number) so that the work can go on. "
          "Each error that upset the balance is later corrected through the suspense account until it is clear. Under the OHADA accounting rules, an entry that has been validated is **never erased**: errors are corrected by a new entry, either reversing the wrong entry and recording the right one (contre-passation), or adding a complementary entry for the difference.", title="Suspense account and correcting entries"),
        EX("Worked example 1: open the suspense account",
           intro="The trial balance of Ets Kum Enterprise totals FCFA 15 284 100 debit and FCFA 15 357 000 credit. Open the suspense account.",
           steps=[
               S("Difference", text="15 357 000 − 15 284 100 = 72 900."),
               S("Side", text="The debit side is short, so the suspense account is opened with a **debit** of 72 900 to make the totals agree."),
           ]),
        EX("Worked example 2: correct five errors",
           intro="Then these errors are found: (1) the sales account was overcast by 90 000; (2) a payment of 72 000 to the supplier Fon was credited to 521 but not debited to Fon; (3) repairs to a lorry, 36 000, were debited to the transport equipment account; (4) commission received of 99 000 was correctly banked but entered in the commission account as 9 900; (5) a credit sale to Kum of 250 000 HT (VAT 19.25%) was omitted. Journalise and clear the suspense account.",
           steps=[
               S("(1) Overcast sales", text="Credit side too big by 90 000: debit 701, credit suspense 90 000."),
               S("(2) One side missing", text="Debit side short by 72 000: debit 401 Fon, credit suspense 72 000."),
               S("(3) Error of principle", text="No suspense: debit 624 repairs, credit 245 transport equipment 36 000."),
               S("(4) Wrong amount on one side", text="Credit short by 99 000 − 9 900 = 89 100: debit suspense, credit 707 with 89 100."),
               S("(5) Omission", text="No suspense: debit 411 with 298 125, credit 701 with 250 000 and 4431 with 48 125."),
               S("Suspense cleared?", text="Debits 72 900 + 89 100 = 162 000; credits 90 000 + 72 000 = 162 000. Yes."),
           ], check=r"72\,900 + 89\,100 = 90\,000 + 72\,000"),
        CODE(_j_err, "text", title="Journal of corrections (47x = the suspense account)"),
        CODE(_t_susp, "text", title="The suspense account clears to zero"),
        H("The effect on the result"),
        T("Ask for each correction: does it change an **income or expense** account (class 6, 7 or 8)? If yes, the result changes. If it changes only balance sheet accounts (suppliers, customers, bank, fixed assets against each other), the result does not change."),
        CODE(_t_prof, "text", title="Statement of corrected result"),
        T("Error (3) reduces the result because an expense had been hidden in a fixed asset. (We assume no depreciation was charged on the 36 000; otherwise the depreciation would also be corrected.) Error (2) affects two balance sheet accounts only. For error (5), the VAT is a debt to the State, not income, so only the HT amount changes the result."),
        MISTAKE("Sending every error through the suspense account",
                "Only errors that made the debits and credits unequal use the suspense account. Omission, commission, principle, original entry, reversal and compensating errors are corrected between the accounts concerned."),
        MISTAKE("Erasing or overwriting the wrong entry",
                "OHADA rules forbid erasing. Correct by a new, dated entry with an explanation, so that the audit trail stays complete."),
        MISTAKE("Changing the result for balance sheet corrections",
                "Correcting a debit to the wrong supplier, or a missing debit to a supplier, does not change the result. Only class 6, 7 and 8 accounts change it."),
        QUIZ("Which error will NOT cause the trial balance totals to differ?",
             ["Sales day book undercast by 50 000", "Purchase of office furniture debited to the purchases account", "A payment debited to the supplier but not credited to the bank", "A receipt of 54 000 entered in the customer's account as 45 000"], 1,
             "An error of principle puts the right amount on both sides, in the wrong class of account.",
             hint="Look for an error with equal debits and credits.",
             feedback=["A casting error affects one side only.", "", "A one-sided entry leaves debits larger than credits.", "A wrong amount on one side upsets the totals by 9 000."]),
        QUIZ("A draft profit is FCFA 2 000 000. Rent paid of FCFA 120 000 was debited to the building account. What is the corrected profit?",
             ["FCFA 2 120 000", "FCFA 1 880 000", "FCFA 2 000 000", "FCFA 1 760 000"], 1,
             "The expense was hidden in a fixed asset; moving it to rent reduces profit by 120 000.",
             feedback=["The correction adds an expense, so profit falls.", "", "The correction moves an amount into the income statement.", "That deducts the 120 000 twice."],
             title="Quick check 2"),
        TIP("Errors appear in Paper 1 (classify an error, find its effect on the trial balance or the profit) and in Paper 3 as journal entries, a suspense account and a statement of corrected result. Number each correction, show the suspense account balancing, and state 'no effect' where the result does not change.",
            title="Exam link"),
        PQ("A trial balance shows debits FCFA 8 640 000 and credits FCFA 8 586 000. Open the suspense account, then correct: the purchases account was overcast by 36 000; a discount received of 18 000 was not posted to the discount account.",
           "Debits exceed credits by 54 000, so open the suspense account with a credit of 54 000. Correction 1: debit suspense, credit purchases 36 000. Correction 2: debit suspense, credit discounts received 18 000. Suspense: credit 54 000 = debits 36 000 + 18 000; it clears."),
        PQ("For the corrections in the previous question, state the effect on the result.",
           "Purchases overcast by 36 000: expenses fall, result +36 000. Discount received not posted: income rises, result +18 000. Total +54 000."),
        PQ("A cheque of FCFA 85 000 received from customer Ebai was credited to the account of customer Ewane. Name the error and give the correction.",
           "Error of commission (right class of account, wrong person). Debit 411 Ewane, credit 411 Ebai with 85 000. No suspense account and no effect on the result."),
        SUM("A trial balance that agrees does not prove that the books are right.",
            "Omission, commission, principle, original entry, complete reversal and compensating errors do not upset the totals.",
            "One-sided entries, wrong amounts on one side and casting errors do; the difference goes to a suspense account.",
            "Correct by new journal entries (never erase); the suspense account must clear to zero.",
            "Only corrections that touch class 6, 7 or 8 accounts change the result."),
    ]))

# ====================================================================== 6. The balance sheet
# Nkam Distribution SARL, Nkongsamba (invented for practice): one case for the whole financial statements module.
# Post-closing balances at 31/12/N (after inventory, depreciation, impairment, provisions and regularisation).
NK_DR = [("21", "Software (intangible)", 1_200_000), ("23-24", "Buildings, equipment, vehicles", 20_400_000),
         ("27", "Deposits paid", 600_000), ("31", "Goods (inventory)", 5_000_000), ("411", "Customers", 6_200_000),
         ("416", "Doubtful customers", 700_000), ("476", "Prepaid expenses", 300_000), ("521", "Bank", 1_450_000),
         ("571", "Cash", 450_000)]
NK_CR = [("281", "Amortisation, intangible", 400_000), ("283-284", "Depreciation, tangible", 7_150_000),
         ("491", "Impairment of customers", 280_000), ("101", "Share capital", 10_000_000), ("11", "Reserves", 2_100_000),
         ("13", "Net result for the year", 2_625_000), ("16", "Loans", 7_000_000), ("19", "Provisions, risks", 1_050_000),
         ("401", "Suppliers", 3_400_000), ("441", "State, income tax", 1_125_000), ("43", "Social security", 420_000),
         ("477", "Income in advance", 250_000), ("561", "Bank short-term credit", 500_000)]
NK = {k: v for k, _, v in NK_DR + NK_CR}
NK_TB = sum(v for _, _, v in NK_DR)
assert NK_TB == sum(v for _, _, v in NK_CR) == 36_300_000
# balance sheet lines (gross, amortisation/impairment) and last year's net figures
NB = {}
NB["intang"] = (NK["21"], NK["281"])
NB["tang"] = (NK["23-24"], NK["283-284"])
NB["fin"] = (NK["27"], 0)
NB["stock"] = (NK["31"], 0)
NB["recv"] = (NK["411"] + NK["416"] + NK["476"], NK["491"])
NB["cash"] = (NK["521"] + NK["571"], 0)
_net = {k: g - a for k, (g, a) in NB.items()}
NK_AI = _net["intang"] + _net["tang"] + _net["fin"]
NK_AC = _net["stock"] + _net["recv"]
NK_TA = _net["cash"]
NK_ACTIF = NK_AI + NK_AC + NK_TA
NK_CP = NK["101"] + NK["11"] + NK["13"]
NK_DF = NK["16"] + NK["19"]
NK_RS = NK_CP + NK_DF
NK_PC = NK["401"] + NK["441"] + NK["43"] + NK["477"]
NK_TP = NK["561"]
NK_PASSIF = NK_RS + NK_PC + NK_TP
assert (NK_AI, NK_AC, NK_TA, NK_ACTIF) == (14_650_000, 11_920_000, 1_900_000, 28_470_000)
assert (NK_CP, NK_DF, NK_RS, NK_PC, NK_TP, NK_PASSIF) == (14_725_000, 8_050_000, 22_775_000, 5_195_000, 500_000, 28_470_000)
assert NK_ACTIF == NK_PASSIF
# last year (N-1), net
NK0 = dict(intang=1_050_000, tang=10_050_000, fin=600_000, stock=4_200_000, recv=6_270_000, cash=2_300_000,
           cap=10_000_000, res=1_500_000, rn=1_600_000, loans=5_200_000, prov=900_000, pc=4_770_000, tp=500_000)
NK0_ACTIF = sum(NK0[k] for k in ("intang", "tang", "fin", "stock", "recv", "cash"))
NK0_PASSIF = sum(NK0[k] for k in ("cap", "res", "rn", "loans", "prov", "pc", "tp"))
assert NK0_ACTIF == NK0_PASSIF == 24_470_000
assert NK0["res"] + NK0["rn"] - 1_000_000 == NK["11"]  # N-1 result: 1 000 000 dividends, 600 000 to reserves


def k_(x):
    """FCFA -> thousands, exact."""
    assert x % 1000 == 0
    return n(x // 1000)


def _bl(label, g=None, a=None, net=None, prev=None, w=21):
    f = lambda v: "" if v is None else (k_(v) if v else "-")
    return f"{label:<{w}}{f(g):>8}{f(a):>8}{f(net):>8}{f(prev):>8}".rstrip()


_t_tb = "\n".join(
    ["Nkam Distribution SARL: balances at 31/12/N",
     f"{'Acct':<8}{'Account':<29}{'Debit':>11}{'Credit':>11}"]
    + [f"{a:<8}{b:<29}{n(v):>11}" for a, b, v in NK_DR]
    + [f"{a:<8}{b:<29}{'':>11}{n(v):>11}" for a, b, v in NK_CR]
    + [f"{'':<8}{'Totals':<29}{n(NK_TB):>11}{n(NK_TB):>11}"])
_t_actif = "\n".join([
    "BILAN at 31/12/N - ASSETS (ACTIF), FCFA thousand",
    f"{'':<21}{'Gross':>8}{'Dep/Imp':>8}{'Net N':>8}{'Net N-1':>8}",
    _bl("Intangible", *NB["intang"], _net["intang"], NK0["intang"]),
    _bl("Tangible", *NB["tang"], _net["tang"], NK0["tang"]),
    _bl("Financial", *NB["fin"], _net["fin"], NK0["fin"]),
    _bl("FIXED ASSETS", None, None, NK_AI, NK0["intang"] + NK0["tang"] + NK0["fin"]),
    _bl("Inventories", *NB["stock"], _net["stock"], NK0["stock"]),
    _bl("Receivables", *NB["recv"], _net["recv"], NK0["recv"]),
    _bl("CURRENT ASSETS", None, None, NK_AC, NK0["stock"] + NK0["recv"]),
    _bl("Bank and cash", *NB["cash"], _net["cash"], NK0["cash"]),
    _bl("CASH - ASSETS", None, None, NK_TA, NK0["cash"]),
    _bl("TOTAL ASSETS", None, None, NK_ACTIF, NK0_ACTIF),
])
_t_passif = "\n".join([
    "BILAN at 31/12/N - EQUITY AND LIABILITIES (PASSIF)",
    f"{'FCFA thousand':<29}{'N':>9}{'N-1':>9}",
    f"{'Share capital':<29}{k_(NK['101']):>9}{k_(NK0['cap']):>9}",
    f"{'Reserves':<29}{k_(NK['11']):>9}{k_(NK0['res']):>9}",
    f"{'Net result':<29}{k_(NK['13']):>9}{k_(NK0['rn']):>9}",
    f"{'EQUITY':<29}{k_(NK_CP):>9}{k_(NK0['cap'] + NK0['res'] + NK0['rn']):>9}",
    f"{'Loans':<29}{k_(NK['16']):>9}{k_(NK0['loans']):>9}",
    f"{'Provisions for risks':<29}{k_(NK['19']):>9}{k_(NK0['prov']):>9}",
    f"{'FINANCIAL DEBTS':<29}{k_(NK_DF):>9}{k_(NK0['loans'] + NK0['prov']):>9}",
    f"{'TOTAL STABLE RESOURCES':<29}{k_(NK_RS):>9}{k_(NK0['cap'] + NK0['res'] + NK0['rn'] + NK0['loans'] + NK0['prov']):>9}",
    f"{'CURRENT LIABILITIES':<29}{k_(NK_PC):>9}{k_(NK0['pc']):>9}",
    f"{'CASH - LIABILITIES':<29}{k_(NK_TP):>9}{k_(NK0['tp']):>9}",
    f"{'TOTAL EQUITY AND LIABILITIES':<29}{k_(NK_PASSIF):>9}{k_(NK0_PASSIF):>9}",
])
_t_map = "\n".join([
    "Where the balances go (revised SYSCOHADA)",
    "Class 2 (less 28, 29) ......... Fixed assets",
    "Class 3 (less 39) ............. Inventories",
    "Class 4, debit balances",
    "  (less 49) ................... Receivables",
    "Class 5, debit balances ....... Cash - assets",
    "10 to 15 ...................... Equity",
    "16 to 19 ...................... Financial debts",
    "Class 4, credit balances ...... Current liab.",
    "56 and credit balances of 52 .. Cash - liab.",
])

LESSONS.append(lesson(
    module=M_FS, topic="The balance sheet",
    title="The OHADA balance sheet: from the closing balances to the bilan",
    slug="acl2-ohada-balance-sheet", minutes=26,
    summary="Place every closing balance in the revised SYSCOHADA balance sheet (fixed assets, current assets, cash-assets; equity, financial debts, current liabilities, cash-liabilities) with gross, depreciation and net columns, and check that it balances.",
    objectives=[
        "Name the four annual financial statements of the normal system and the role of the balance sheet",
        "Classify each account balance into the correct block of the revised SYSCOHADA balance sheet",
        "Prepare a balance sheet with gross, depreciation or impairment, net and comparative columns",
        "Explain the meaning of stable resources and the treatment of overdrafts, impairment and the result",
    ],
    key_concepts=["Bilan", "Fixed assets (actif immobilisé)", "Current assets (actif circulant)", "Cash-assets and cash-liabilities (trésorerie)",
                  "Equity (capitaux propres)", "Stable resources (ressources stables)", "Current liabilities (passif circulant)"],
    blocks=[
        H("Introduction"),
        T("Nkam Distribution SARL, a wholesaler in Nkongsamba, has finished its year-end adjustments. Its accountant must now prepare the **annual financial statements**. "
          "In the normal system of the revised SYSCOHADA there are four: the **balance sheet** (bilan), the **income statement** (compte de résultat), the **cash flow statement** (tableau des flux de trésorerie) and the **notes** (notes annexes). "
          "This module follows the same company through all four. Every name and figure is **invented for practice**."),
        D("The **balance sheet** shows, at the closing date, what the entity controls (assets, **actif**) and how they are financed (equity and liabilities, **passif**). It is presented **before appropriation** of the result: the net result of the year appears in equity. "
          "Each asset is shown at **gross** value, less **depreciation and impairment**, giving the **net** value, with last year's net figures for comparison.", title="The bilan"),
        IMG("alacl2-bilan-structure.svg",
            alt="Two columns. Assets: fixed assets, current assets, cash-assets. Equity and liabilities: equity and financial debts (together stable resources), current liabilities, cash-liabilities. Both totals are equal.",
            caption="Figure 1. The blocks of the revised SYSCOHADA balance sheet (simplified)."),
        KEY("The blocks, from long term to short term", "The balance sheet is read from the most permanent items at the top to cash at the bottom.", cards=[
            ["Fixed assets", "Intangible (software, patents), tangible (land, buildings, equipment, vehicles), financial (long-term deposits, investments)."],
            ["Current assets", "Inventories, receivables (customers, other debtors, prepaid expenses). Items outside ordinary activities (HAO) have their own line."],
            ["Cash-assets", "Bank and cash balances, short-term investments, cheques to collect."],
            ["Equity + financial debts = stable resources", "Capital, reserves, result, investment subsidies; plus loans and long-term provisions for risks and charges."],
            ["Current liabilities", "Suppliers, State, social security, staff, customers' advances, income received in advance, short-term provisions."],
            ["Cash-liabilities", "Bank overdrafts and short-term bank credit."],
        ]),
        CODE(_t_map, "text", title="From the chart of accounts to the balance sheet"),
        T("Two balances need care. A **bank account with a credit balance** is an overdraft: it goes to cash-liabilities, not as a negative asset. A **supplier with a debit balance** (an advance paid) is a receivable, not a negative liability. "
          "Foreign currency gains and losses not yet realised appear in separate 'translation difference' lines (écarts de conversion), which you met with foreign currency transactions."),
        EX("Worked example 1: classify the balances",
           intro="Classify: 491 Impairment of customers; 19 Provisions for risks; 477 Income received in advance; 561 Bank short-term credit; 476 Prepaid expenses; 13 Net result.",
           steps=[
               S("Deducted from an asset", text="491 is deducted from receivables (it is not a liability)."),
               S("Stable resources", text="19 is a financial debt; 13 is part of equity."),
               S("Current", text="477 is a current liability; 476 is a receivable (current asset)."),
               S("Cash", text="561 is a cash-liability."),
           ]),
        CODE(_t_tb, "text", title="Post-closing balances (invented for practice)"),
        EX("Worked example 2: build the bilan of Nkam Distribution",
           intro="Using the balances above, prepare the balance sheet at 31/12/N in FCFA thousand.",
           steps=[
               S("Fixed assets", text="Intangible 1 200 − 400 = 800; tangible 20 400 − 7 150 = 13 250; financial 600. Total 14 650."),
               S("Current assets", text="Inventories 5 000. Receivables 6 200 + 700 + 300 = 7 200 gross, less 280 impairment = 6 920. Total 11 920."),
               S("Cash-assets", text="1 450 + 450 = 1 900. Total assets 14 650 + 11 920 + 1 900 = 28 470."),
               S("Stable resources", text="Equity 10 000 + 2 100 + 2 625 = 14 725; financial debts 7 000 + 1 050 = 8 050; total 22 775."),
               S("Short-term and check", text="Current liabilities 3 400 + 1 125 + 420 + 250 = 5 195; cash-liabilities 500. Total 22 775 + 5 195 + 500 = 28 470 = total assets."),
           ], check=r"14\,650 + 11\,920 + 1\,900 = 22\,775 + 5\,195 + 500 = 28\,470"),
        CODE(_t_actif, "text", title="Assets"),
        CODE(_t_passif, "text", title="Equity and liabilities"),
        T("The official revised SYSCOHADA model has more lines (each with a reference code) and a notes column; the layout above keeps the blocks and totals that examiners look for. Check your textbook for the full model."),
        H("Reading the balance sheet"),
        T("Stable resources (22 775) more than cover the fixed assets (14 650): the surplus of 8 125 finances part of the inventories and receivables. This surplus is the working capital, which you will analyse with the functional balance sheet in Upper Sixth. "
          "The comparison with N−1 shows growth: total assets rose from 24 470 to 28 470, while cash-assets fell from 2 300 to 1 900. The cash flow statement will explain why."),
        MISTAKE("Netting the overdraft against the bank balance",
                "Bank balances (cash-assets) and overdrafts or short-term bank credit (cash-liabilities) are shown separately, on opposite sides."),
        MISTAKE("Showing impairment and depreciation as liabilities",
                "Accounts 28, 29, 39 and 49 reduce the assets they relate to. They appear in the 'depreciation and impairment' column of the assets side."),
        MISTAKE("Forgetting the result in equity",
                "The balance sheet is before appropriation: the net result of the year (account 13) is part of equity. A loss is shown as a negative amount in equity."),
        QUIZ("In the revised SYSCOHADA balance sheet, where does a provision for a lawsuit expected to be settled in three years appear?",
             ["Current liabilities", "Financial debts and similar resources", "Deducted from receivables", "Cash-liabilities"], 1,
             "A long-term provision for risks and charges (class 19) belongs with the financial debts, inside stable resources.",
             hint="Is it long term or short term, and is it linked to an asset?",
             feedback=["Only short-term provisions (499) are in current liabilities.", "", "It is not an impairment of an asset.", "Cash-liabilities are bank credits and overdrafts."]),
        QUIZ("Fixed assets net FCFA 9 000 000, current assets FCFA 5 000 000, cash-assets FCFA 1 000 000, current liabilities FCFA 3 500 000, cash-liabilities FCFA 500 000. What are the stable resources?",
             ["FCFA 11 000 000", "FCFA 15 000 000", "FCFA 9 000 000", "FCFA 12 000 000"], 0,
             "Total assets 15 000 000 − 3 500 000 − 500 000 = 11 000 000.",
             feedback=["", "That is total assets.", "That is the fixed assets.", "That forgets the cash-liabilities."],
             title="Quick check 2"),
        TIP("The Board's 2023 report describes a Paper 3 question on preparing the income statement and the statement of financial position (the balance sheet) and asks teachers to teach the format of accounts. Use clear headings, gross, depreciation and net columns, subtotals for each block, and show that the two totals agree.",
            title="Exam link"),
        PQ("A bank account 521 has a credit balance of FCFA 350 000 at the year end, and another bank account a debit balance of FCFA 900 000. How are they shown?",
           "The debit balance (900 000) is a cash-asset. The credit balance (350 000) is an overdraft, shown in cash-liabilities. They are not netted."),
        PQ("Equipment cost FCFA 8 000 000 with accumulated depreciation FCFA 3 200 000; goods FCFA 2 500 000 with impairment FCFA 150 000. Show the lines of the balance sheet.",
           "Equipment: gross 8 000 000, depreciation 3 200 000, net 4 800 000. Inventories: gross 2 500 000, impairment 150 000, net 2 350 000."),
        PQ("Total assets are FCFA 40 000 000. Equity is FCFA 18 000 000, loans FCFA 9 000 000, long-term provisions FCFA 1 000 000 and cash-liabilities FCFA 2 000 000. Find the current liabilities and the stable resources.",
           "Stable resources = 18 000 000 + 9 000 000 + 1 000 000 = 28 000 000. Current liabilities = 40 000 000 − 28 000 000 − 2 000 000 = 10 000 000."),
        SUM("The normal system produces four statements: balance sheet, income statement, cash flow statement and notes.",
            "Assets: fixed assets, current assets, cash-assets, each at gross, depreciation or impairment, and net, with N−1 for comparison.",
            "Equity and liabilities: equity and financial debts (stable resources), current liabilities, cash-liabilities.",
            "Overdrafts are cash-liabilities; accounts 28, 29, 39, 49 reduce assets; the year's result is in equity.",
            "The two totals must agree."),
    ]))

# ====================================================================== 7. Income statement and intermediate balances
# Nkam Distribution SARL, year N (same company). Tax at a teaching rate of 30% (check the current Finance Law).
IS = dict(TA=48_000_000, RA=31_500_000, RB=4_200_000 - 5_000_000, TD=1_200_000, TH=300_000,
          RE=1_100_000, RG=1_400_000, RH=2_600_000, RI=900_000, RJ=200_000, RK=6_300_000,
          TJ=150_000, RL=2_450_000, TK=120_000, RM=620_000, TN=1_800_000, RO=1_300_000, RP=250_000)
IS["XA"] = IS["TA"] - IS["RA"] - IS["RB"]
IS["XB"] = IS["TA"] + IS["TD"]
IS["XC"] = IS["XA"] + IS["TD"] + IS["TH"] - IS["RE"] - IS["RG"] - IS["RH"] - IS["RI"] - IS["RJ"]
IS["XD"] = IS["XC"] - IS["RK"]
IS["XE"] = IS["XD"] + IS["TJ"] - IS["RL"]
IS["XF"] = IS["TK"] - IS["RM"]
IS["XG"] = IS["XE"] + IS["XF"]
IS["XH"] = IS["TN"] - IS["RO"] - IS["RP"]
IS["RS"] = pct(IS["XG"] + IS["XH"], 30)
IS["XI"] = IS["XG"] + IS["XH"] - IS["RS"]
assert (IS["XA"], IS["XB"], IS["XC"], IS["XD"], IS["XE"], IS["XF"], IS["XG"], IS["XH"], IS["RS"], IS["XI"]) == (
    17_300_000, 49_200_000, 12_600_000, 6_300_000, 4_000_000, -500_000, 3_500_000, 250_000, 1_125_000, 2_625_000)
assert IS["XI"] == NK["13"] and IS["RS"] == NK["441"]
_prod = IS["TA"] + IS["TD"] + IS["TH"] + IS["TJ"] + IS["TK"] + IS["TN"]
_chg = (IS["RA"] + IS["RB"] + IS["RE"] + IS["RG"] + IS["RH"] + IS["RI"] + IS["RJ"] + IS["RK"] + IS["RL"] + IS["RM"]
        + IS["RO"] + IS["RP"] + IS["RS"])
assert _prod - _chg == IS["XI"] and (_prod, _chg) == (51_570_000, 48_945_000)


def _il(ref, label, v, bold=False):
    lab = label.upper() if bold else label
    return f"{ref:<4}{lab:<31}{n(v):>12}"


_t_is = "\n".join([
    "Nkam Distribution SARL - income statement, year N",
    _il("TA", "Sales of goods", IS["TA"]),
    _il("RA", "Purchases of goods", -IS["RA"]),
    _il("RB", "Change in inventory of goods", -IS["RB"]),
    _il("XA", "Commercial margin", IS["XA"], True),
    _il("TD", "Ancillary income", IS["TD"]),
    _il("XB", "Turnover (TA+TD)", IS["XB"], True),
    _il("TH", "Other income", IS["TH"]),
    _il("RE", "Other purchases", -IS["RE"]),
    _il("RG", "Transport", -IS["RG"]),
    _il("RH", "External services", -IS["RH"]),
    _il("RI", "Taxes and duties", -IS["RI"]),
    _il("RJ", "Other charges", -IS["RJ"]),
    _il("XC", "Value added", IS["XC"], True),
    _il("RK", "Personnel costs", -IS["RK"]),
    _il("XD", "Gross operating surplus", IS["XD"], True),
    _il("TJ", "Reversals of provisions", IS["TJ"]),
    _il("RL", "Depreciation and provisions", -IS["RL"]),
    _il("XE", "Operating result", IS["XE"], True),
    _il("TK", "Financial income", IS["TK"]),
    _il("RM", "Financial charges", -IS["RM"]),
    _il("XF", "Financial result", IS["XF"], True),
    _il("XG", "Result, ordinary activ.", IS["XG"], True),
    _il("TN", "Proceeds of asset disposals", IS["TN"]),
    _il("RO", "Book value of assets sold", -IS["RO"]),
    _il("RP", "Other HAO charges", -IS["RP"]),
    _il("XH", "Result outside ord. activ.", IS["XH"], True),
    _il("RS", "Income tax (30%, teaching)", -IS["RS"]),
    _il("XI", "Net result", IS["XI"], True),
])
_t_va = "\n".join([
    "Who receives the value added of 12 600 000?",
    row("Staff (personnel costs)", IS["RK"], w=34),
    row("Lenders (financial charges)", IS["RM"], w=34),
    row("State (income tax)", IS["RS"], w=34),
    row("The firm and its owners (rest)", IS["XC"] - IS["RK"] - IS["RM"] - IS["RS"], w=34),
])
assert IS["XC"] - IS["RK"] - IS["RM"] - IS["RS"] == 4_555_000

LESSONS.append(lesson(
    module=M_FS, topic="The income statement and intermediate balances",
    title="The OHADA income statement: the intermediate balances from commercial margin to net result",
    slug="acl2-income-statement-intermediate-balances", minutes=27,
    summary="Prepare the revised SYSCOHADA income statement by nature and calculate its intermediate balances: commercial margin, turnover, value added, gross operating surplus, operating result, financial result, results of ordinary and non-ordinary activities and net result, then interpret them.",
    objectives=[
        "Explain the classification of charges and income by nature in classes 6, 7 and 8",
        "Calculate the intermediate balances XA to XI in the correct order",
        "Prepare an income statement from a list of balances and check it against total income less total charges",
        "Interpret what each balance shows about the business",
    ],
    key_concepts=["Commercial margin (MB)", "Value added (VA)", "Gross operating surplus (EBE)", "Operating result (RE)",
                  "Financial result (RF)", "Result of ordinary activities (RAO)", "Non-ordinary result (RHAO)", "Net result (RN)"],
    blocks=[
        H("Introduction"),
        T("The balance sheet of Nkam Distribution shows a net result of FCFA 2 625 000 for year N. The owners want to know where it came from: from trading? from financing? from selling an old lorry? "
          "The OHADA income statement (compte de résultat) answers these questions by building the result in steps called **intermediate balances**. The figures are those of the previous lesson's company, **invented for practice**."),
        D("Charges and income are classified **by nature**: what was bought or earned (goods, transport, staff, interest), not by department. Ordinary activities use classes 6 and 7; operations outside ordinary activities (HAO: hors activités ordinaires), such as disposals of fixed assets, use class 8, which also holds income tax.", title="By nature, in three groups"),
        IMG("alacl2-sig-cascade.svg",
            alt="Cascade of balances from the top: commercial margin, value added, gross operating surplus, operating result; then financial result added to give the result of ordinary activities; then the non-ordinary result and income tax give the net result.",
            caption="Figure 1. The cascade of intermediate balances in the revised SYSCOHADA income statement."),
        KEY("The balances and how each is found", "Each balance uses the one before it. The letters are the references of the revised SYSCOHADA model.", cards=[
            ["XA Commercial margin", "Sales of goods − purchases of goods ∓ change in inventory of goods (opening − closing)."],
            ["XB Turnover", "Sales of goods + sales of products + services + ancillary income. A measure of activity, not a step of the cascade."],
            ["XC Value added", "Margin + production + other income − other purchases − transport − external services − taxes and duties − other charges."],
            ["XD Gross operating surplus", "Value added − personnel costs. The cash the operations can generate before depreciation and financing."],
            ["XE Operating result", "XD + reversals − depreciation, provisions and impairment charges."],
            ["XF, XG", "Financial result = financial income − financial charges. Result of ordinary activities XG = XE + XF."],
            ["XH, XI", "HAO result = HAO income − HAO charges. Net result XI = XG + XH − workers' participation − income tax."],
        ]),
        T("In the revised SYSCOHADA model, taxes and duties (64) are deducted **before** value added. Some older textbooks, and the simplified O Level layout, deduct them after value added. Check which layout your teacher uses and say which one you follow."),
        EX("Worked example 1: the first balances",
           intro="Nkam Distribution: sales of goods 48 000 000; purchases of goods 31 500 000; opening inventory 4 200 000, closing inventory 5 000 000; ancillary income 1 200 000; other income 300 000; other purchases 1 100 000; transport 1 400 000; external services 2 600 000; taxes and duties 900 000; other charges 200 000; personnel 6 300 000. Find XA, XB, XC and XD.",
           steps=[
               S("Change in inventory", text="Opening − closing = 4 200 000 − 5 000 000 = −800 000 (inventory rose, so the cost of goods sold is lower than purchases)."),
               S("XA", text="48 000 000 − 31 500 000 − (−800 000) = 17 300 000."),
               S("XB", text="48 000 000 + 1 200 000 = 49 200 000."),
               S("XC", text="17 300 000 + 1 200 000 + 300 000 − 1 100 000 − 1 400 000 − 2 600 000 − 900 000 − 200 000 = 12 600 000."),
               S("XD", text="12 600 000 − 6 300 000 = 6 300 000."),
           ], check=r"48\,000\,000 - 31\,500\,000 + 800\,000 = 17\,300\,000"),
        EX("Worked example 2: from operating result to net result",
           intro="Also: reversals of provisions 150 000; depreciation and provision charges 2 450 000; financial income 120 000; interest 620 000; an old lorry with a book value of 1 300 000 was sold for 1 800 000; a penalty of 250 000 (HAO); income tax at a teaching rate of 30%.",
           steps=[
               S("XE", text="6 300 000 + 150 000 − 2 450 000 = 4 000 000."),
               S("XF and XG", text="XF = 120 000 − 620 000 = −500 000. XG = 4 000 000 − 500 000 = 3 500 000."),
               S("XH", text="1 800 000 − 1 300 000 − 250 000 = 250 000."),
               S("Tax and XI", text="Tax = 30% × (3 500 000 + 250 000) = 1 125 000. XI = 3 750 000 − 1 125 000 = 2 625 000, the result in the balance sheet."),
           ]),
        CODE(_t_is, "text", title="Income statement in list form (simplified revised SYSCOHADA model)"),
        T("Check: total income 51 570 000 − total charges 48 945 000 = 2 625 000. Always do this check; it catches a missing line. In a real company the taxable profit differs from the accounting result and a minimum tax may apply: taxation is studied in Upper Sixth."),
        H("Interpreting the balances"),
        T("The **commercial margin** (17 300 000, about 36% of sales of goods) measures the trading performance. The **value added** measures the wealth the business creates beyond what it buys from other firms; it is shared among the staff, the lenders, the State and the business itself. "
          "The **gross operating surplus** shows whether operations generate cash before depreciation and financing; it does not depend on the depreciation method or on how the business is financed, so it is useful for comparing firms. "
          "Separating **ordinary** from **non-ordinary** results shows that only 250 000 of the profit came from one-off events: the core business is profitable."),
        CODE(_t_va, "text", title="Sharing the value added (simplified)"),
        MISTAKE("Using purchases instead of the cost of goods sold",
                "The commercial margin uses purchases adjusted for the change in inventory. An increase in inventory (opening below closing) gives a negative change and raises the margin."),
        MISTAKE("Putting the profit on disposal in the operating result",
                "The proceeds of disposal (TN) and the book value of the asset sold (RO) are HAO items. They belong in XH, not in the operating result."),
        MISTAKE("Deducting depreciation before the gross operating surplus",
                "Depreciation and provision charges come after XD; they are deducted to find the operating result XE."),
        QUIZ("Sales of goods FCFA 20 000 000, purchases of goods FCFA 13 000 000, opening inventory FCFA 1 500 000, closing inventory FCFA 1 000 000. What is the commercial margin?",
             ["FCFA 7 000 000", "FCFA 6 500 000", "FCFA 7 500 000", "FCFA 5 500 000"], 1,
             "Change in inventory = 1 500 000 − 1 000 000 = +500 000. Margin = 20 000 000 − 13 000 000 − 500 000 = 6 500 000.",
             hint="Inventory fell: does the cost of goods sold rise or fall?",
             feedback=["That ignores the change in inventory.", "", "That adds the fall in inventory instead of deducting it.", "That deducts the opening inventory in full instead of the change."]),
        QUIZ("Value added is FCFA 9 000 000, personnel costs FCFA 4 000 000, depreciation FCFA 1 500 000 and interest FCFA 300 000. The gross operating surplus is",
             ["FCFA 5 000 000", "FCFA 3 500 000", "FCFA 3 200 000", "FCFA 4 700 000"], 0,
             "EBE = value added − personnel costs = 9 000 000 − 4 000 000 = 5 000 000.",
             feedback=["", "That is the operating result (after depreciation).", "That also deducts the interest, which is in the financial result.", "That deducts the interest but not the depreciation, mixing two levels."],
             title="Quick check 2"),
        TIP("Paper 1 often asks for one balance from a few figures; Paper 3 may ask for the whole income statement. Write each balance with its name and reference (XA, XC...), show the calculation of the change in inventory, and finish with the check that total income less total charges equals the net result.",
            title="Exam link"),
        PQ("A manufacturer has: sales of products 60 000 000; increase in finished goods inventory (production stocked) 2 000 000; purchases of raw materials 25 000 000; decrease in raw materials inventory 1 000 000; transport and external services 8 000 000; taxes and duties 1 500 000; personnel 15 000 000. Find value added and gross operating surplus.",
           "Production of the year = 60 000 000 + 2 000 000 = 62 000 000. Raw materials consumed = 25 000 000 + 1 000 000 = 26 000 000. VA = 62 000 000 − 26 000 000 − 8 000 000 − 1 500 000 = 26 500 000. EBE = 26 500 000 − 15 000 000 = 11 500 000."),
        PQ("Operating result FCFA 7 200 000; financial income FCFA 300 000; financial charges FCFA 1 100 000; HAO income FCFA 900 000; HAO charges FCFA 1 400 000; income tax FCFA 1 500 000. Find XF, XG, XH and XI.",
           "XF = 300 000 − 1 100 000 = −800 000. XG = 7 200 000 − 800 000 = 6 400 000. XH = 900 000 − 1 400 000 = −500 000. XI = 6 400 000 − 500 000 − 1 500 000 = 4 400 000."),
        PQ("Two shops have the same net result. Shop A has a large positive HAO result and a small result of ordinary activities; Shop B is the reverse. Which is in a stronger position? Explain.",
           "Shop B. Its profit comes from its ordinary activities, which are likely to continue. Shop A's profit depends on one-off events (for example, selling assets), which cannot be repeated every year; its core business is weak."),
        SUM("The OHADA income statement classifies charges and income by nature; HAO items and income tax are in class 8.",
            "XA margin, XB turnover, XC value added, XD gross operating surplus, XE operating result.",
            "XF financial result; XG = XE + XF; XH non-ordinary result; XI = XG + XH − participation − income tax.",
            "Check: total income − total charges = net result = the result in the balance sheet.",
            "Interpret: margin for trading, value added for wealth created, EBE for operating cash, RAO against RHAO for lasting profit."),
    ]))

# ====================================================================== 8. The cash flow statement
# Nkam Distribution SARL, year N (same company)
CF = {}
CF["cafg"] = IS["XI"] + IS["RL"] - IS["TJ"] - IS["TN"] + IS["RO"]
_cafg_ebe = IS["XD"] + IS["TK"] - IS["RM"] - IS["RP"] - IS["RS"]
assert CF["cafg"] == _cafg_ebe == 4_425_000
CF["d_stock"] = NB["stock"][0] - NK0["stock"]
CF["d_recv"] = NB["recv"][0] - (NK0["recv"] + NK["491"])  # gross receivables; impairment unchanged at 280 000
CF["d_pc"] = NK_PC - NK0["pc"]
assert (CF["d_stock"], CF["d_recv"], CF["d_pc"]) == (800_000, 650_000, 425_000)
CF["ZB"] = CF["cafg"] - CF["d_stock"] - CF["d_recv"] + CF["d_pc"]
CF["acq"], CF["disp"] = 6_400_000, IS["TN"]
CF["ZC"] = -CF["acq"] + CF["disp"]
CF["div"] = 1_000_000
CF["ZD"] = -CF["div"]
CF["new_loan"], CF["repay"] = 3_000_000, 1_200_000
CF["ZE"] = CF["new_loan"] - CF["repay"]
assert NK0["loans"] + CF["ZE"] == NK["16"]
CF["ZF"] = CF["ZD"] + CF["ZE"]
CF["ZG"] = CF["ZB"] + CF["ZC"] + CF["ZF"]
CF["ZA"] = NK0["cash"] - NK0["tp"]
CF["ZH"] = NK_TA - NK_TP
assert (CF["ZB"], CF["ZC"], CF["ZF"], CF["ZG"], CF["ZA"], CF["ZH"]) == (3_400_000, -4_600_000, 800_000, -400_000, 1_800_000, 1_400_000)
assert CF["ZA"] + CF["ZG"] == CF["ZH"]
# cross-check against the balance sheets: change in fixed assets (net) = acquisitions - book value sold - depreciation
_dep_N = 2_150_000
_prov_N = IS["RL"] - _dep_N
assert NK_AI - (NK0["intang"] + NK0["tang"] + NK0["fin"]) == CF["acq"] - IS["RO"] - _dep_N == 2_950_000
assert NK["19"] - NK0["prov"] == _prov_N - IS["TJ"] == 150_000


def _cl(ref, label, v=None, tot=None):
    return f"{ref:<4}{label:<30}{('' if v is None else n(v)):>11}{('' if tot is None else n(tot)):>11}".rstrip()


_t_cafg = "\n".join([
    "Self-financing capacity (CAFG), additive method",
    row("Net result", IS["XI"], w=36),
    row("+ Depreciation and provision charges", IS["RL"], w=36),
    row("- Reversals of provisions", -IS["TJ"], w=36),
    row("- Proceeds of disposals", -IS["TN"], w=36),
    row("+ Book value of assets sold", IS["RO"], w=36),
    row("= CAFG", CF["cafg"], w=36),
])
_t_tft = "\n".join([
    "Nkam Distribution - cash flow statement, year N",
    _cl("ZA", "Net cash at 1 January", None, CF["ZA"]),
    _cl("", "CAFG", CF["cafg"]),
    _cl("", "- Increase in inventories", -CF["d_stock"]),
    _cl("", "- Increase in receivables", -CF["d_recv"]),
    _cl("", "+ Increase in current liab.", CF["d_pc"]),
    _cl("ZB", "Operating activities", None, CF["ZB"]),
    _cl("", "Purchases of fixed assets", -CF["acq"]),
    _cl("", "Proceeds of disposals", CF["disp"]),
    _cl("ZC", "Investing activities", None, CF["ZC"]),
    _cl("", "Dividends paid", -CF["div"]),
    _cl("ZD", "Financing from equity", None, CF["ZD"]),
    _cl("", "New loans", CF["new_loan"]),
    _cl("", "Loans repaid", -CF["repay"]),
    _cl("ZE", "Financing from borrowing", None, CF["ZE"]),
    _cl("ZF", "Financing activities (ZD+ZE)", None, CF["ZF"]),
    _cl("ZG", "Change in net cash", None, CF["ZG"]),
    _cl("ZH", "Net cash at 31 December", None, CF["ZH"]),
])

LESSONS.append(lesson(
    module=M_FS, topic="The cash flow statement",
    title="The cash flow statement (TFT): operating, investing and financing flows",
    slug="acl2-cash-flow-statement", minutes=27,
    summary="Build the revised SYSCOHADA cash flow statement: net cash at the start, the self-financing capacity, operating flows after working capital changes, investing and financing flows, and net cash at the end, checked against the balance sheets.",
    objectives=[
        "Define net cash and explain why profit and cash differ",
        "Calculate the self-financing capacity (CAFG) by the additive method and from the gross operating surplus",
        "Prepare a cash flow statement with operating, investing and financing flows from two balance sheets and an income statement",
        "Interpret the flows to explain a rise or fall in cash",
    ],
    key_concepts=["Net cash (trésorerie nette)", "Self-financing capacity (CAFG)", "Operating cash flow", "Investing cash flow",
                  "Financing cash flow", "Working capital changes", "Tableau des flux de trésorerie (TFT)"],
    blocks=[
        H("Introduction"),
        T("Nkam Distribution made a profit of FCFA 2 625 000 in year N, yet its cash fell. The owners are surprised: where did the money go? The **cash flow statement** (tableau des flux de trésorerie, TFT) answers this. "
          "It replaced the old TAFIRE in the revised SYSCOHADA. We use the balance sheets and the income statement of the last two lessons (all figures **invented for practice**)."),
        D("**Net cash** (trésorerie nette) = cash-assets − cash-liabilities. For Nkam: at 1 January 2 300 000 − 500 000 = 1 800 000; at 31 December 1 900 000 − 500 000 = 1 400 000. The TFT explains the change of −400 000.", title="Net cash"),
        IMG("alacl2-tft-structure.svg",
            alt="Net cash at 1 January plus three flows (operating, investing, financing) gives net cash at 31 December. Operating flow is CAFG less the increase in working capital needs.",
            caption="Figure 1. The structure of the cash flow statement."),
        KEY("Three families of flows", "Every receipt or payment belongs to one family.", cards=[
            ["Operating (ZB)", "Cash from ordinary activities: CAFG adjusted for changes in inventories, receivables and current liabilities."],
            ["Investing (ZC)", "Purchases of fixed assets (outflows) and proceeds of their disposal (inflows)."],
            ["Financing (ZF)", "From equity (ZD): capital contributed, investment subsidies, dividends paid. From borrowing (ZE): new loans in, repayments out."],
        ]),
        D("The **self-financing capacity** (capacité d'autofinancement globale, CAFG) is the cash surplus the year's income and charges will generate. It removes from the net result the items that are not cash (depreciation, provisions, reversals) and the disposal items (which go to investing flows). "
          "Additive method: CAFG = net result + depreciation and provision charges − reversals − proceeds of disposals + book value of assets sold. "
          "From the EBE: CAFG = EBE + financial income − financial charges + HAO income (excluding disposals) − HAO charges − income tax.", title="CAFG"),
        EX("Worked example 1: the CAFG of Nkam Distribution",
           intro="Net result 2 625 000; depreciation and provision charges 2 450 000; reversals 150 000; disposal proceeds 1 800 000; book value of the asset sold 1 300 000. Check with the EBE of 6 300 000, financial income 120 000, interest 620 000, HAO penalty 250 000 and income tax 1 125 000.",
           steps=[
               S("Additive method", text="2 625 000 + 2 450 000 − 150 000 − 1 800 000 + 1 300 000 = 4 425 000."),
               S("From the EBE", text="6 300 000 + 120 000 − 620 000 − 250 000 − 1 125 000 = 4 425 000. The two methods agree."),
           ], check=r"2\,625\,000 + 2\,450\,000 - 150\,000 - 1\,800\,000 + 1\,300\,000 = 4\,425\,000"),
        CODE(_t_cafg, "text", title="CAFG"),
        EX("Worked example 2: the operating flow",
           intro="From the balance sheets: inventories rose from 4 200 000 to 5 000 000; gross receivables from 6 550 000 to 7 200 000; current liabilities from 4 770 000 to 5 195 000.",
           steps=[
               S("Inventories", text="+800 000 more inventory ties up cash: −800 000."),
               S("Receivables", text="Customers owe 650 000 more: cash not yet received, −650 000."),
               S("Current liabilities", text="The business owes 425 000 more: cash not yet paid, +425 000."),
               S("Operating flow", text="4 425 000 − 800 000 − 650 000 + 425 000 = 3 400 000."),
           ]),
        EX("Worked example 3: complete the statement",
           intro="During N the company bought equipment for 6 400 000 and sold a lorry for 1 800 000; it paid dividends of 1 000 000; it borrowed 3 000 000 and repaid 1 200 000 of loans.",
           steps=[
               S("Investing", text="−6 400 000 + 1 800 000 = −4 600 000."),
               S("Financing", text="Equity −1 000 000; borrowing +3 000 000 − 1 200 000 = +1 800 000; total +800 000."),
               S("Change in net cash", text="3 400 000 − 4 600 000 + 800 000 = −400 000."),
               S("Check", text="1 800 000 − 400 000 = 1 400 000, the net cash in the closing balance sheet."),
           ], check=r"1\,800\,000 + 3\,400\,000 - 4\,600\,000 + 800\,000 = 1\,400\,000"),
        CODE(_t_tft, "text", title="Cash flow statement (simplified; references as in the revised model, check your textbook)"),
        T("Check the investing figures against the balance sheets: net fixed assets rose from 11 700 000 to 14 650 000 (+2 950 000) = purchases 6 400 000 − book value sold 1 300 000 − depreciation 2 150 000. And loans rose from 5 200 000 to 7 000 000 = 3 000 000 − 1 200 000."),
        H("Interpreting the flows"),
        T("The operations of Nkam generated 3 400 000 of cash, less than the CAFG because inventories and receivables grew with the business. Investment of 4 600 000 was larger than the operating flow, so new borrowing filled part of the gap and cash fell by 400 000. "
          "This is normal for a growing firm, but if investment keeps exceeding operating cash for several years, the firm will depend more and more on lenders. Profit is an accounting measure built on accruals; cash is what pays suppliers, staff and lenders. Both are needed."),
        MISTAKE("Counting depreciation as an outflow of cash",
                "Depreciation is a charge but not a payment. It is added back to the result when calculating the CAFG; the cash went out when the asset was bought (investing flow)."),
        MISTAKE("Putting the profit on disposal in the investing flow",
                "The investing flow shows the full proceeds of disposal (1 800 000). The profit (500 000) is removed from the CAFG by deducting the proceeds and adding back the book value."),
        MISTAKE("Getting the sign of working capital changes wrong",
                "More inventory or more receivables use cash (minus). More current liabilities keep cash in the business (plus). The opposite changes have the opposite signs."),
        QUIZ("Net result FCFA 1 500 000, depreciation FCFA 800 000, reversal of a provision FCFA 100 000, no disposals. The CAFG is",
             ["FCFA 2 200 000", "FCFA 2 400 000", "FCFA 700 000", "FCFA 1 500 000"], 0,
             "1 500 000 + 800 000 − 100 000 = 2 200 000.",
             hint="Add back non-cash charges and remove non-cash income.",
             feedback=["", "That adds the reversal instead of deducting it.", "That deducts depreciation instead of adding it back.", "The net result alone ignores non-cash items."]),
        QUIZ("In which part of the TFT does the repayment of a bank loan appear?",
             ["Operating activities", "Investing activities", "Financing activities", "It does not appear"], 2,
             "Borrowing and repaying loans are financing flows (from borrowing, ZE).",
             feedback=["Interest is in the CAFG, but the repayment of the capital of a loan is financing.", "Investing flows concern fixed assets.", "", "It is a cash payment, so it must appear."],
             title="Quick check 2"),
        TIP("Paper 1 can ask for a CAFG or the family of a flow. A Paper 3 question may give two balance sheets and an income statement. Work in this order: net cash at both dates, CAFG, operating flow, investing flow, financing flow, and finish by checking that the change in net cash matches the balance sheets.",
            title="Exam link"),
        PQ("Net result FCFA 3 000 000; depreciation FCFA 1 200 000; provision charge FCFA 300 000; a machine with a book value of FCFA 400 000 was sold for FCFA 650 000. Calculate the CAFG.",
           "3 000 000 + 1 200 000 + 300 000 − 650 000 + 400 000 = 4 250 000."),
        PQ("CAFG FCFA 4 250 000; inventories fell by FCFA 200 000; receivables rose by FCFA 900 000; current liabilities fell by FCFA 150 000. Calculate the operating cash flow.",
           "4 250 000 + 200 000 − 900 000 − 150 000 = 3 400 000."),
        PQ("Net cash at 1 January is FCFA −300 000 (an overdraft larger than the bank balance). Operating flow +3 400 000; investing flow −5 000 000; financing flow +2 500 000. Find the net cash at 31 December and comment.",
           "−300 000 + 3 400 000 − 5 000 000 + 2 500 000 = 600 000. Net cash has become positive, but only because of new financing: operations alone did not cover the investment."),
        SUM("Net cash = cash-assets − cash-liabilities; the TFT explains its change over the year.",
            "CAFG = net result + depreciation and provisions − reversals − disposal proceeds + book value sold (or start from the EBE).",
            "Operating flow = CAFG − increase in inventories − increase in receivables + increase in current liabilities.",
            "Investing: purchases out, disposal proceeds in. Financing: capital and loans in, dividends and repayments out.",
            "Opening net cash + the three flows = closing net cash; check it against the balance sheet."),
    ]))

# ====================================================================== 9. Notes to the financial statements
# Nkam Distribution SARL, year N (same company)
_fa = [("Intangible", 1_200_000, 0, 0), ("Tangible", 17_200_000, CF["acq"], 3_200_000)]
_fa_close = [o + a - d for _, o, a, d in _fa]
assert _fa_close == [NB["intang"][0], NB["tang"][0]]
_fa_tot = [sum(x[i] for x in _fa) for i in (1, 2, 3)]
assert _fa_tot == [18_400_000, 6_400_000, 3_200_000] and sum(_fa_close) == 21_600_000
_dp = [("Intangible", 150_000, 250_000, 0), ("Tangible", 7_150_000, 1_900_000, 1_900_000)]
_dp_close = [o + c - r for _, o, c, r in _dp]
assert _dp_close == [NB["intang"][1], NB["tang"][1]]
assert sum(c for _, _, c, _ in _dp) == _dep_N and 3_200_000 - 1_900_000 == IS["RO"]
_dp_tot = [sum(x[i] for x in _dp) for i in (1, 2, 3)]
assert _dp_tot == [7_300_000, 2_150_000, 1_900_000] and sum(_dp_close) == 7_550_000
_t_fa = "\n".join(
    ["Note: fixed assets, gross values (FCFA)",
     f"{'':<11}{'Opening':>11}{'Acquired':>11}{'Disposed':>11}{'Closing':>11}"]
    + [f"{a:<11}{n(o):>11}{n(ac):>11}{n(d):>11}{n(c):>11}" for (a, o, ac, d), c in zip(_fa, _fa_close)]
    + [f"{'Total':<11}{n(_fa_tot[0]):>11}{n(_fa_tot[1]):>11}{n(_fa_tot[2]):>11}{n(sum(_fa_close)):>11}"])
_t_dp = "\n".join(
    ["Note: depreciation and amortisation (FCFA)",
     f"{'':<11}{'Opening':>11}{'Charge':>11}{'On disp.':>11}{'Closing':>11}"]
    + [f"{a:<11}{n(o):>11}{n(ch):>11}{n(r):>11}{n(c):>11}" for (a, o, ch, r), c in zip(_dp, _dp_close)]
    + [f"{'Total':<11}{n(_dp_tot[0]):>11}{n(_dp_tot[1]):>11}{n(_dp_tot[2]):>11}{n(sum(_dp_close)):>11}"])
_pv = [("Provisions (19)", NK0["prov"], _prov_N, IS["TJ"]), ("Impairment (491)", NK["491"], 0, 0)]
_pv_close = [o + c - r for _, o, c, r in _pv]
assert _pv_close == [NK["19"], NK["491"]]
_t_pv = "\n".join(
    ["Note: provisions and impairment (FCFA)",
     f"{'':<17}{'Opening':>10}{'Charge':>9}{'Reversal':>10}{'Closing':>11}"]
    + [f"{a:<17}{n(o):>10}{n(ch):>9}{n(r):>10}{n(c):>11}" for (a, o, ch, r), c in zip(_pv, _pv_close)])
_eq0 = NK0["cap"] + NK0["res"] + NK0["rn"]
_eq1 = _eq0 + IS["XI"] - CF["div"]
assert _eq1 == NK_CP
_t_eq = "\n".join([
    "Note: changes in equity (FCFA)",
    row("Equity at 1 January", _eq0, w=32),
    row("+ Net result of year N", IS["XI"], w=32),
    row("- Dividends paid (N-1 result)", -CF["div"], w=32),
    row("Equity at 31 December", _eq1, w=32),
])
_loan_short = 1_400_000
_t_mat = "\n".join([
    "Note: debts by maturity at 31/12/N (FCFA)",
    f"{'':<22}{'Total':>11}{'< 1 year':>11}{'> 1 year':>11}",
    f"{'Loans':<22}{n(NK['16']):>11}{n(_loan_short):>11}{n(NK['16'] - _loan_short):>11}",
    f"{'Suppliers':<22}{n(NK['401']):>11}{n(NK['401']):>11}{'-':>11}",
    f"{'State and social sec.':<22}{n(NK['441'] + NK['43']):>11}{n(NK['441'] + NK['43']):>11}{'-':>11}",
])

LESSONS.append(lesson(
    module=M_FS, topic="Notes to the financial statements",
    title="Notes to the financial statements: policies, movement tables and commitments",
    slug="acl2-notes-to-financial-statements", minutes=23,
    summary="Explain the role of the notes, state what they must disclose (accounting policies, movement tables, maturities, commitments, contingent liabilities, events after the year end) and prepare the main movement tables that link the balance sheet, income statement and cash flow statement.",
    objectives=[
        "Explain why the notes are an integral part of the annual financial statements",
        "List the main information disclosed in the notes under the revised SYSCOHADA",
        "Prepare movement tables for fixed assets, depreciation, provisions and equity, and a maturity analysis of debts",
        "Decide whether an item is recorded in the statements or only disclosed in the notes",
    ],
    key_concepts=["Notes (notes annexes)", "Accounting policies", "Movement table", "Maturity analysis",
                  "Off-balance-sheet commitments", "Contingent liability", "Events after the reporting date"],
    blocks=[
        H("Introduction"),
        T("A bank in Douala is studying a loan request from Nkam Distribution. The balance sheet shows FCFA 7 000 000 of loans, but the bank wants to know more: how much falls due next year? Which depreciation methods were used? Has the company guaranteed anyone else's debt? "
          "The answers are in the **notes**, the fourth annual statement. Figures continue the case of this module (**invented for practice**)."),
        D("The **notes** (notes annexes) complete and explain the balance sheet, the income statement and the cash flow statement. They form one whole with them: a set of statements without its notes is incomplete. "
          "They give information that the totals cannot show: the methods used, the detail of important lines, and risks that are not recorded. The revised SYSCOHADA sets out a standard list of numbered notes for the normal system and a shorter one for the minimal cash system; check your textbook for the list and the numbering.", title="Notes"),
        KEY("What the notes disclose", "Four groups of information.", cards=[
            ["Policies and methods", "Statement of compliance with SYSCOHADA; valuation rules; depreciation methods and rates; inventory method (FIFO or weighted average); treatment of foreign currency; any change of method and its effect on the result."],
            ["Detail of the statements", "Movement tables (fixed assets, depreciation, provisions, equity), receivables and debts by maturity, staff numbers and costs, breakdown of turnover."],
            ["Commitments and risks", "Guarantees given or received, bills discounted not yet due, leases, contingent liabilities (possible obligations not recorded)."],
            ["Events after the year end", "Important events between the closing date and the approval of the accounts, such as a fire or the loss of a major customer."],
        ]),
        EX("Worked example 1: the fixed assets and depreciation tables",
           intro="Nkam's intangible and tangible fixed assets were 18 400 000 gross at 1 January. During N it bought equipment for 6 400 000 and sold a lorry that had cost 3 200 000, with accumulated depreciation of 1 900 000. Accumulated depreciation was 7 300 000 at 1 January and the charge for N was 2 150 000. Prepare the two tables.",
           steps=[
               S("Gross values", text="18 400 000 + 6 400 000 − 3 200 000 = 21 600 000."),
               S("Depreciation", text="7 300 000 + 2 150 000 − 1 900 000 (removed with the lorry) = 7 550 000."),
               S("Links", text="Net fixed assets (excluding the deposits of 600 000) = 21 600 000 − 7 550 000 = 14 050 000; with the deposits, 14 650 000 as in the balance sheet. Book value sold 3 200 000 − 1 900 000 = 1 300 000 = line RO of the income statement."),
           ], check=r"21\,600\,000 - 7\,550\,000 + 600\,000 = 14\,650\,000"),
        CODE(_t_fa, "text", title="Movement of gross values"),
        CODE(_t_dp, "text", title="Movement of depreciation"),
        EX("Worked example 2: provisions and equity",
           intro="The provision for risks was 900 000 at 1 January; a charge of 300 000 and a reversal of 150 000 were made. Equity at 1 January was 13 100 000; the result for N is 2 625 000 and dividends of 1 000 000 were paid out of last year's result.",
           steps=[
               S("Provisions", text="900 000 + 300 000 − 150 000 = 1 050 000 (account 19 in the balance sheet)."),
               S("Equity", text="13 100 000 + 2 625 000 − 1 000 000 = 14 725 000 (equity in the balance sheet)."),
           ]),
        CODE(_t_pv, "text", title="Movement of provisions and impairment"),
        CODE(_t_eq, "text", title="Changes in equity"),
        CODE(_t_mat, "text", title="Maturity analysis (the 1 400 000 due within a year is invented for practice)"),
        T("The maturity table answers the bank's first question: 1 400 000 of the loans must be repaid within a year, which the cash flow forecast must cover. Each movement table ties a balance sheet figure at two dates to a figure in the income statement or the cash flow statement. That is why examiners use them to test whether you understand how the statements fit together."),
        H("Recorded or only disclosed?"),
        T("A probable obligation that can be measured is **recorded** (a provision). A possible obligation, or one that cannot be measured, is only **disclosed** in the notes as a contingent liability. A guarantee given for another company's loan, or bills of exchange discounted but not yet due, are **commitments**: no entry, but a note, because they could become debts. "
          "An event after the year end that gives more evidence about a situation that existed at the closing date (a customer declared bankrupt in January who was already in difficulty in December) leads to an adjustment; an event that arises after the closing date (a fire in February) is disclosed only."),
        MISTAKE("Thinking the notes are optional",
                "The notes are one of the four annual statements of the normal system. Accounts without notes are incomplete."),
        MISTAKE("Forgetting to remove the depreciation of assets sold",
                "When an asset is sold, its accumulated depreciation leaves the depreciation table, just as its cost leaves the gross values table."),
        MISTAKE("Recording a contingent liability",
                "A possible obligation is only described in the notes. Recording it as a provision would understate the result without the conditions being met."),
        QUIZ("Gross fixed assets were FCFA 12 000 000 at 1 January. Acquisitions FCFA 3 000 000; an asset that cost FCFA 1 500 000 was sold. Gross fixed assets at 31 December are",
             ["FCFA 13 500 000", "FCFA 16 500 000", "FCFA 10 500 000", "FCFA 15 000 000"], 0,
             "12 000 000 + 3 000 000 − 1 500 000 = 13 500 000.",
             hint="Opening + additions − disposals at cost.",
             feedback=["", "That adds the disposal instead of subtracting it.", "That subtracts the acquisitions.", "That forgets the disposal."]),
        QUIZ("Which item is disclosed in the notes but NOT recorded in the accounts?",
             ["A guarantee given for a supplier's bank loan", "Depreciation of equipment", "A provision for a lawsuit the company will probably lose", "Wages owing at the year end"], 0,
             "A guarantee is a commitment: it may become a debt, so it is disclosed, not recorded.",
             feedback=["", "Depreciation is a charge recorded in the accounts.", "A probable, measurable obligation is recorded as a provision.", "Wages owing are an accrued expense, recorded in 42."],
             title="Quick check 2"),
        TIP("The notes are tested mostly in Paper 1 (purpose, contents, recorded or disclosed) and inside Paper 3 statement questions where a movement table is part of the working. Present each table as opening + increases − decreases = closing, and check the closing figure against the balance sheet.",
            title="Exam link"),
        PQ("Accumulated depreciation was FCFA 5 400 000 at 1 January. The charge for the year is FCFA 1 600 000. A machine sold during the year had accumulated depreciation of FCFA 900 000. Find the closing accumulated depreciation.",
           "5 400 000 + 1 600 000 − 900 000 = 6 100 000."),
        PQ("Give four items of information that must be disclosed in the accounting policies note.",
           "For example: compliance with the revised SYSCOHADA; the basis of valuation of fixed assets (historical cost); depreciation methods and rates; the inventory valuation method (FIFO or weighted average); the treatment of foreign currency items; any change of method and its effect."),
        PQ("In February N+1, before the accounts of N are approved, a fire destroys a warehouse. Should the accounts of N be adjusted? Explain.",
           "No. The fire arose after the closing date; the warehouse existed and had its value at 31 December. The event is disclosed in the notes (events after the year end) because it is important to users, but the figures of N are not changed."),
        SUM("The notes complete and explain the other three statements and are part of the annual financial statements.",
            "They disclose policies and methods, detailed tables, commitments and contingent liabilities, and events after the year end.",
            "Movement tables: opening + increases − decreases = closing, for gross values, depreciation, provisions and equity.",
            "Probable and measurable obligations are recorded; possible ones and commitments are only disclosed."),
    ]))

# ====================================================================== Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1: fifty accounting multiple-choice questions, method and traps",
    slug="acl2-paper1-multiple-choice", minutes=23,
    summary="How Paper 1 is built (50 compulsory questions across financial, cost and management, and company accounting and taxation), a routine for calculation, journal and classification questions, the traps examiners build into wrong options, and a revision map of the Lower Sixth modules.",
    objectives=[
        "Describe the structure and weight of Paper 1 from the Board's 2023 report",
        "Use a four-step routine for calculation, journal-entry and classification questions",
        "Recognise the typical accounting distractors: VAT included, reversed entries, unfinished calculations, wrong period",
        "Plan revision of the five Lower Sixth modules for Paper 1",
    ],
    key_concepts=["Multiple-choice question", "Stem and options", "Distractor", "HT and TTC", "Debit and credit direction",
                  "Time per question", "Revision map"],
    blocks=[
        H("What Paper 1 is"),
        T("The Board's 2023 Advanced Level report describes Accounting 0705 as three papers weighted 30, 30 and 40. **Paper 1** is 50 multiple-choice questions, all compulsory, marked by computer, one mark each. In 2023 there were 25 questions on financial accounting, 10 on cost and management accounting and 15 on company accounting and taxation. "
          "The Lower Sixth course is financial accounting, so it prepares you for about half of Paper 1 now; the Upper Sixth adds the company, taxation, cost and management topics. In the KKEVO mock that follows this lesson we allow 90 minutes (a KKEVO practice setting, not a Board timing)."),
        D("Each question has a **stem** (the question) and four **options**; one is right and three are **distractors**, wrong answers built on real mistakes. There is no credit for working, so the letter you choose is all that counts.", title="How a question is built"),
        KEY("A routine for every question", "Use it until it is automatic.", cards=[
            ["1. Read the stem", "Underline what is asked: an amount, an entry, a classification, a NOT question. Note HT or TTC, dates and the year end."],
            ["2. Answer first", "Work out the answer on rough paper before you look at the options, so that a distractor cannot lead you."],
            ["3. Match and eliminate", "Find your answer. If it is not there, eliminate options that are surely wrong and check your working."],
            ["4. Check", "Side (debit or credit), sign, VAT, months, and whether the stem asked for the change or the balance."],
        ]),
        H("Three kinds of question"),
        T("**Calculation** questions ask for a figure: an impairment, a margin, a CAFG, an adjusted bank balance. Write the formula, put the numbers in, and check the order of magnitude. "
          "**Entry** questions ask which accounts are debited and credited. Say the event in words first ('the business pays', 'the customer owes'), then choose the accounts. "
          "**Classification and concept** questions ask where an item goes (which block of the balance sheet, which balance of the income statement) or which convention applies."),
        EX("Worked example 1: a calculation",
           intro="A doubtful customer owes FCFA 834 750 TTC (VAT 19.25%). The expected loss is 30%. The impairment is: A 250 425; B 210 000; C 700 000; D 40 425.",
           steps=[
               S("Answer first", text="HT = 834 750 ÷ 1.1925 = 700 000. Impairment = 30% × 700 000 = 210 000."),
               S("Eliminate", text="A is 30% of the TTC amount. C is the HT debt. D is 19.25% of 210 000, VAT applied to the impairment, which has no meaning."),
               S("Choose", text="B."),
           ], check=r"834\,750 \div 1.1925 = 700\,000;\ 0.30 \times 700\,000 = 210\,000"),
        EX("Worked example 2: an entry",
           intro="On 31/12/N rent of FCFA 600 000 has been received for January and February N+1. The year-end entry is: A debit 477, credit 707; B debit 707, credit 477; C debit 476, credit 707; D debit 707, credit 418.",
           steps=[
               S("In words", text="Income received now belongs to next year, so this year's income must be reduced and a debt to provide the service recorded."),
               S("Accounts", text="Reduce income: debit 707. Liability: credit 477 Income received in advance."),
               S("Choose", text="B. A is reversed; C uses the prepaid expenses account; D uses accrued income."),
           ]),
        KEY("Distractors in accounting", "Most wrong options are one of these.", cards=[
            ["VAT included", "The percentage applied to the TTC amount instead of HT, or VAT counted as income or expense."],
            ["Reversed entry", "Right accounts, debit and credit swapped."],
            ["Unfinished calculation", "The first step only: the commercial margin when value added was asked, the HT debt when the impairment was asked."],
            ["Balance or change", "The whole new provision when only the increase is charged, or the reverse."],
            ["Wrong period", "Months counted wrongly in an accrual or a depreciation."],
        ]),
        H("Revision map for the Lower Sixth"),
        CODE("Module                     Ideas Paper 1 can test\n"
             "SYSCOHADA framework        postulates and conventions, classes\n"
             "                           1-9, normal system and SMT, books\n"
             "Commercial operations      invoices and reductions, VAT due,\n"
             "                           packaging, bills, exchange, payroll\n"
             "Valuation of assets        cost of an asset, depreciation,\n"
             "                           disposals, FIFO and weighted average\n"
             "Year-end adjustments       impairment, provisions, accruals,\n"
             "                           bank reconciliation, errors\n"
             "Annual statements          bilan blocks, XA to XI, CAFG and\n"
             "                           cash flows, notes", "text", title="Table 1. What to revise"),
        MISTAKE("Starting from the options", "Options are designed to look right. Work the answer out first, then look for it."),
        MISTAKE("Leaving questions blank", "A blank cannot score. If you are unsure after eliminating, choose the most likely remaining option and mark the question to return to it if time allows."),
        MISTAKE("Spending five minutes on one figure", "All questions are worth one mark. Move on and come back; an easier question later is worth just as much."),
        QUIZ("A question asks: 'Which of the following is NOT deducted from an asset on the balance sheet?' Which account answers it?",
             ["491", "39", "19", "28"], 2,
             "19 is a provision for risks and charges: a liability, not a deduction from an asset.",
             hint="Which account is on the liabilities side?",
             feedback=["491 reduces receivables.", "39 reduces inventories.", "", "28 is accumulated depreciation, deducted from fixed assets."]),
        QUIZ("Sales of goods FCFA 16 000 000; purchases of goods FCFA 10 000 000; opening inventory FCFA 2 000 000; closing inventory FCFA 2 500 000. The commercial margin is",
             ["FCFA 6 000 000", "FCFA 6 500 000", "FCFA 5 500 000", "FCFA 4 000 000"], 1,
             "Change in inventory = 2 000 000 − 2 500 000 = −500 000. Margin = 16 000 000 − 10 000 000 + 500 000 = 6 500 000.",
             hint="Inventory rose: the cost of goods sold is less than purchases.",
             feedback=["The 'unfinished calculation' distractor: the change in inventory is ignored.", "", "The 'reversed sign' distractor: the rise in inventory is deducted.", "Only the opening inventory is deducted, not the change."],
             title="Quick check 2"),
        TIP("Before the examination, make a one-page list of the formulas and account numbers from each module (HT = TTC ÷ 1.1925, CAFG, XA to XI, 416/491/6594/7594, 476/477/408/418) and practise them with the mock paper that follows this lesson.",
            title="Exam link"),
        PQ("Net result FCFA 900 000; depreciation FCFA 400 000; book value of an asset sold FCFA 150 000; proceeds FCFA 200 000. The CAFG is: A 1 250 000; B 1 300 000; C 1 450 000; D 1 350 000.",
           "900 000 + 400 000 − 200 000 + 150 000 = 1 250 000, so A. B (1 300 000) ignores both disposal items. C (1 450 000) adds back the book value but forgets to deduct the proceeds. D (1 350 000) has both signs reversed: it adds the proceeds and deducts the book value."),
        PQ("An insurance premium of FCFA 480 000 for 12 months was paid on 1 September N. The year ends on 31 December. The prepaid amount is: A 160 000; B 320 000; C 120 000; D 360 000.",
           "September to December is 4 months in N; 8 months are prepaid: 8/12 × 480 000 = 320 000, so B. A is the expense of N. C is 3 months. D is 9 months."),
        PQ("Give three checks you make before you finally choose an option in an entry question.",
           "That the debit and credit are not reversed; that the amount is HT or TTC as the entry requires; that the stem asked for the change (charge or reversal) or for the closing balance."),
        SUM("Paper 1 is 50 compulsory multiple-choice questions, 30% of the examination; in 2023 half were on financial accounting.",
            "Routine: read the stem, answer first, match and eliminate, check side, sign, VAT and period.",
            "Distractors: VAT included, reversed entries, unfinished calculations, balance versus change, wrong months.",
            "Never leave a blank; return to hard questions at the end; revise all five modules."),
    ]))

# ====================================================================== Examination 2. Paper 2 (preview)
# high-low
_hl = {"hi": (1_800, 2_940_000), "lo": (1_200, 2_220_000)}
_hl_v = (_hl["hi"][1] - _hl["lo"][1]) // (_hl["hi"][0] - _hl["lo"][0])
assert (_hl["hi"][1] - _hl["lo"][1]) % (_hl["hi"][0] - _hl["lo"][0]) == 0
_hl_f = _hl["hi"][1] - _hl["hi"][0] * _hl_v
assert (_hl_v, _hl_f, _hl["lo"][1] - _hl["lo"][0] * _hl_v) == (1_200, 780_000, 780_000)
_hl_est = _hl_f + 1_500 * _hl_v
assert _hl_est == 2_580_000
# break-even
_be_p, _be_v, _be_f = 5_000, 3_000, 1_600_000
_be_c = _be_p - _be_v
_be_q = _be_f // _be_c
assert _be_f % _be_c == 0 and (_be_c, _be_q, _be_q * _be_p) == (2_000, 800, 4_000_000)
_be_tq = (_be_f + 600_000) // _be_c
assert (_be_f + 600_000) % _be_c == 0 and _be_tq == 1_100
_be_ms = 1_000 - _be_q
assert (_be_ms, _be_ms * 100 // 1_000) == (200, 20)
# FIFO and weighted average
_o_q, _o_p, _b_q, _b_p, _i_q = 100, 1_000, 300, 1_200, 250
_fifo_issue = _o_q * _o_p + (_i_q - _o_q) * _b_p
_fifo_close = (_o_q + _b_q - _i_q) * _b_p
_cump = (_o_q * _o_p + _b_q * _b_p) // (_o_q + _b_q)
assert (_o_q * _o_p + _b_q * _b_p) % (_o_q + _b_q) == 0
assert (_fifo_issue, _fifo_close, _cump, _i_q * _cump, (_o_q + _b_q - _i_q) * _cump) == (280_000, 180_000, 1_150, 287_500, 172_500)
# overhead absorption
_oh, _dlh = 4_800_000, 12_000
_oar = _oh // _dlh
assert _oh % _dlh == 0 and _oar == 400 and 35 * _oar == 14_000
_t_card = "\n".join([
    "Stock card extract (units x unit cost = value)",
    "                     FIFO               W. average",
    f"Opening   100 x 1 000 = 100 000    100 x 1 000 = 100 000",
    f"Purchase  300 x 1 200 = 360 000    300 x 1 200 = 360 000",
    f"Average                            460 000 / 400 = 1 150",
    f"Issue 250 100 x 1 000 + 150 x 1 200  250 x 1 150",
    f"          = {n(_fifo_issue)}                = {n(_i_q * _cump)}",
    f"Closing   150 x 1 200 = {n(_fifo_close)}    150 x 1 150 = {n((_o_q + _b_q - _i_q) * _cump)}",
])

LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2 preview: cost and management accounting basics you can already do",
    slug="acl2-paper2-cost-management-preview", minutes=25,
    summary="What Paper 2 (Cost and Management Accounting) contains according to the Board's 2023 report, and a Lower Sixth preview of four basics it builds on: inventory valuation, the high-low method, contribution and break-even, and overhead absorption.",
    objectives=[
        "Describe the structure of Paper 2 and the topics of its 2023 questions",
        "Value issues and closing inventory by FIFO and weighted average on a stock card",
        "Separate fixed and variable costs by the high-low method and use them to estimate a cost",
        "Calculate contribution, break-even point, margin of safety and an overhead absorption rate",
    ],
    key_concepts=["Cost and management accounting", "Fixed and variable cost", "High-low method", "Contribution",
                  "Break-even point", "Margin of safety", "Overhead absorption rate"],
    blocks=[
        H("What Paper 2 is"),
        T("The Board's 2023 report describes **Paper 2** as Cost and Management Accounting, a three-hour paper in two sections: Section A (cost accounting) has three questions, of which candidates answer two; Section B (management accounting) has three questions, all compulsory. Five questions of equal weight are answered, and the paper is 30% of the examination. "
          "In 2023 the questions covered: separating costs by the high-low method and estimating costs; overhead absorption and a job cost sheet; stock cards by FIFO and weighted average with a trading account; standard costing variances; a cash budget (one of the least well answered); and break-even analysis."),
        D("This is a **preview**. The Lower Sixth course is financial accounting (Paper 3 and part of Paper 1); full cost accounting, budgets, standard costing and investment appraisal are taught in Upper Sixth. But four basics can be learnt now, and one of them, inventory valuation, is already part of your Lower Sixth course.", title="Lower Sixth preview"),
        KEY("Four basics", "Each one appears in a Paper 2 question type.", cards=[
            ["Inventory valuation", "FIFO and weighted average cost (CUMP) on a stock card."],
            ["Cost behaviour", "Fixed costs stay the same in total as activity changes; variable costs change in proportion; semi-variable costs have both parts."],
            ["Contribution and break-even", "Contribution per unit = price − variable cost per unit. Break-even units = fixed costs ÷ contribution per unit."],
            ["Overhead absorption", "Overhead absorption rate = budgeted overheads ÷ budgeted activity (for example direct labour hours)."],
        ]),
        EX("Worked example 1: FIFO and weighted average",
           intro="Opening inventory 100 units at FCFA 1 000; purchase of 300 units at FCFA 1 200; then an issue of 250 units. Value the issue and the closing inventory by FIFO and by the weighted average calculated after the purchase.",
           steps=[
               S("FIFO", text="Issue: 100 × 1 000 + 150 × 1 200 = 280 000. Closing: 150 × 1 200 = 180 000."),
               S("Weighted average", text="(100 000 + 360 000) ÷ 400 = 1 150. Issue 250 × 1 150 = 287 500; closing 150 × 1 150 = 172 500."),
               S("Check", text="Both methods: issue + closing = 460 000, the total cost available."),
           ], check=r"280\,000 + 180\,000 = 287\,500 + 172\,500 = 460\,000"),
        CODE(_t_card, "text", title="Stock card extract"),
        EX("Worked example 2: the high-low method",
           intro="A workshop's monthly costs: highest activity 1 800 hours, total cost FCFA 2 940 000; lowest activity 1 200 hours, total cost FCFA 2 220 000. Find the variable cost per hour and the fixed cost, then estimate the cost of 1 500 hours.",
           steps=[
               S("Variable cost per hour", text="(2 940 000 − 2 220 000) ÷ (1 800 − 1 200) = 720 000 ÷ 600 = 1 200."),
               S("Fixed cost", text="2 940 000 − 1 800 × 1 200 = 780 000 (check: 2 220 000 − 1 200 × 1 200 = 780 000)."),
               S("Estimate", text="780 000 + 1 500 × 1 200 = 2 580 000."),
           ], check=r"\frac{2\,940\,000 - 2\,220\,000}{1\,800 - 1\,200} = 1\,200"),
        EX("Worked example 3: contribution and break-even",
           intro="A product sells for FCFA 5 000; variable cost FCFA 3 000 a unit; fixed costs FCFA 1 600 000 a month. Find the break-even point in units and in value, the sales needed for a profit of FCFA 600 000, and the margin of safety at sales of 1 000 units.",
           steps=[
               S("Contribution", text="5 000 − 3 000 = 2 000 a unit."),
               S("Break-even", text="1 600 000 ÷ 2 000 = 800 units; 800 × 5 000 = FCFA 4 000 000."),
               S("Target profit", text="(1 600 000 + 600 000) ÷ 2 000 = 1 100 units."),
               S("Margin of safety", text="1 000 − 800 = 200 units, that is 20% of sales."),
           ]),
        IMG("alacl2-break-even-chart.svg",
            alt="Break-even chart: a horizontal fixed cost line at 1.6 million, a total cost line rising from 1.6 million, and a sales line from zero crossing the total cost line at 800 units and 4 million francs.",
            caption="Figure 1. Break-even chart for Worked example 3."),
        T("**Overhead absorption**: if a factory budgets overheads of FCFA 4 800 000 and 12 000 direct labour hours, the rate is 4 800 000 ÷ 12 000 = FCFA 400 per hour, and a job that takes 35 hours absorbs 35 × 400 = FCFA 14 000 of overheads. A job cost sheet adds direct materials, direct labour and absorbed overheads."),
        MISTAKE("Choosing the high and low points by cost", "The high-low method uses the highest and lowest **activity** levels, with their costs. Pick by hours or units, not by the cost figures."),
        MISTAKE("Dividing fixed costs by the selling price", "Break-even units = fixed costs ÷ **contribution** per unit, not ÷ price."),
        MISTAKE("Using an average before the purchase", "With the weighted average, recalculate the average cost after each receipt (perpetual) or for the period (periodic), as the question says."),
        QUIZ("Fixed costs are FCFA 900 000; price FCFA 2 500; variable cost FCFA 1 600 a unit. The break-even point is",
             ["360 units", "1 000 units", "563 units", "2 500 units"], 1,
             "Contribution = 900; 900 000 ÷ 900 = 1 000 units.",
             hint="Find the contribution per unit first.",
             feedback=["That divides by the price.", "", "That divides by the variable cost.", "2 500 is the break-even revenue in thousands of francs (1 000 × 2 500), not a number of units."]),
        QUIZ("At 2 000 units total cost is FCFA 1 300 000; at 1 500 units it is FCFA 1 100 000. The variable cost per unit is",
             ["FCFA 400", "FCFA 650", "FCFA 733", "FCFA 100"], 0,
             "200 000 ÷ 500 = 400.",
             feedback=["", "That is the total cost per unit at 2 000 units.", "That is the total cost per unit at 1 500 units.", "That divides the change in cost by 2 000 units instead of by the change in activity (500)."],
             title="Quick check 2"),
        TIP("Paper 2 questions reward clear tables: a stock card with columns for receipts, issues and balance; a high-low working with the two points; a marginal costing statement (sales, variable costs, contribution, fixed costs, profit). The practice paper that follows tests these basics as a preview.",
            title="Exam link"),
        PQ("Opening inventory 200 units at FCFA 500; purchase 300 units at FCFA 600; issue 350 units. Value the closing inventory by FIFO and by weighted average after the purchase.",
           "FIFO: closing 150 units of the latest purchase = 150 × 600 = 90 000. Weighted average: (100 000 + 180 000) ÷ 500 = 560; closing 150 × 560 = 84 000."),
        PQ("Price FCFA 8 000, variable cost FCFA 5 000, fixed costs FCFA 2 400 000. How many units give a profit of FCFA 900 000?",
           "Contribution 3 000. (2 400 000 + 900 000) ÷ 3 000 = 1 100 units."),
        PQ("Overheads of FCFA 6 000 000 are absorbed on 15 000 machine hours. A job uses materials FCFA 80 000, labour FCFA 45 000 and 20 machine hours. Find its total cost.",
           "Rate = 6 000 000 ÷ 15 000 = 400 per machine hour. Overheads 20 × 400 = 8 000. Total = 80 000 + 45 000 + 8 000 = 133 000."),
        SUM("Paper 2 is Cost and Management Accounting: two sections, five questions answered, 30% of the examination.",
            "FIFO issues the oldest costs first; the weighted average uses (cost available ÷ units available).",
            "High-low: variable cost = change in cost ÷ change in activity; fixed cost = total cost − variable part.",
            "Break-even units = fixed costs ÷ contribution per unit; margin of safety = sales − break-even sales.",
            "Overhead absorption rate = overheads ÷ activity base."),
    ]))

# ====================================================================== Examination 3. Paper 3
_p3_ttc, _p3_rate = 1_192_500, 40
_p3_ht = 1_000_000
assert _p3_ht + vat(_p3_ht) == _p3_ttc
_p3_old = 300_000
_p3_need = pct(_p3_ht, _p3_rate)
assert (_p3_need, _p3_need - _p3_old) == (400_000, 100_000)
_t_p3plan = "\n".join([
    "Answer layout for an impairment question",
    "1. Schedule: customer | TTC | HT | rate | needed",
    "             | old | increase | reversal",
    "2. Journal, one entry per event, dated:",
    "   transfers 411 -> 416 (TTC)",
    "   receipts (TTC)",
    "   lost debts: 651 (HT) + 443/4431 (VAT) / 416",
    "   charge 6594 / 491; reversal 491 / 7594",
    "3. Check: closing 491 = total 'needed'",
])

LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 3",
    title="Paper 3: choosing questions and presenting financial accounting answers",
    slug="acl2-paper3-financial-accounting", minutes=24,
    summary="The structure of Paper 3 (Financial Accounting) from the Board's 2023 report, what its questions asked and where candidates lost marks, and a method for planning, laying out and checking journals, schedules and financial statements.",
    objectives=[
        "Describe the two sections of Paper 3 and the choice of questions",
        "Use the 2023 report's comments to know which topics are common and where marks are lost",
        "Plan and lay out a journal, a schedule and a statement so that method marks are earned",
        "Check an answer with control totals before moving on",
    ],
    key_concepts=["Section A financial accounting", "Section B company accounting and taxation", "Question choice",
                  "Workings", "Format of accounts", "Control total"],
    blocks=[
        H("What Paper 3 is"),
        T("**Paper 3** is Financial Accounting, the heaviest paper: 40% of the examination. The Board's 2023 report describes two sections. **Section A** (financial accounting) has four questions and candidates answer three. **Section B** (company accounting and taxation) has three questions and candidates answer two. Five questions of equal weight are answered. "
          "Your Lower Sixth work is the foundation of Section A; Section B (partnerships and companies, share capital, taxation, changes in capital) is taught in Upper Sixth."),
        H("What the 2023 questions asked"),
        T("The report describes Section A questions on: the **impairment of doubtful customers** with journal entries (almost every candidate tried it, but fewer than half succeeded); **ratio analysis** (profitability, liquidity, efficiency, capital structure); **invoices** completed and journalised under the **permanent inventory** system (the easiest question); and the **income statement and statement of financial position** in vertical format. "
          "In Section B, questions on valuing shares, on taxation (calculating the taxable profit and the tax) and on changes in capital were attempted by few candidates and poorly answered; the report suggests these last topics of the programme were not well taught. It also recommends using the recommended textbooks, learning the format of the accounts and writing in blue or black ink, not pencil."),
        KEY("Lessons from the report", "Turn each comment into a habit.", cards=[
            ["Know the formats", "Learn the layout of the journal, the impairment schedule, the income statement and the balance sheet so well that you never hesitate."],
            ["Cover the whole syllabus", "Do not rely on guessing topics. A question you cannot attempt costs a fifth of the paper."],
            ["Show workings", "Number every working and refer to it in the statement; a wrong total with clear workings still earns method marks."],
            ["Use ink", "Answers in pencil are not accepted practice: write in blue or black ink."],
        ]),
        H("Choosing your questions"),
        T("Spend the first minutes reading every question in the section, not just the first one. For each, ask: do I know the format? can I start at once? are there parts I cannot do? Choose the questions where you can earn the most marks, not the shortest-looking ones. "
          "Then share the time equally among the five questions you will answer, and keep to it: an unfinished last question loses more marks than a slightly shorter answer to each."),
        EX("Worked example 1: planning an impairment answer",
           intro="A customer owing FCFA 1 192 500 TTC (VAT 19.25%) has been doubtful since last year with an impairment of FCFA 300 000. At this year end the expected loss is 40%. Plan and answer.",
           steps=[
               S("Plan the schedule", text="TTC 1 192 500; HT 1 192 500 ÷ 1.1925 = 1 000 000; needed 40% × 1 000 000 = 400 000; old 300 000; increase 100 000."),
               S("Journal", text="Debit 6594, credit 491 with 100 000, dated at the year end, with a short narration."),
               S("Control", text="The closing balance of 491 for this customer is 300 000 + 100 000 = 400 000, the amount needed."),
           ], check=r"1\,192\,500 \div 1.1925 = 1\,000\,000;\ 0.40 \times 1\,000\,000 - 300\,000 = 100\,000"),
        CODE(_t_p3plan, "text", title="A layout you can reuse"),
        EX("Worked example 2: presenting a statement",
           intro="A question gives a trial balance and six adjustments and asks for the income statement and the balance sheet. How do you set out the answer?",
           steps=[
               S("Workings first", text="On a separate page, number each adjustment: W1 closing inventory, W2 depreciation, W3 impairment, W4 accruals and prepayments, and so on. Show the arithmetic."),
               S("Income statement", text="Use the order of the intermediate balances (XA to XI) or the vertical layout the question asks for. Write the name of every balance and refer to the workings (for example 'Depreciation (W2)')."),
               S("Balance sheet", text="Gross, depreciation or impairment, net; the blocks in order; subtotals for each block; the result from the income statement in equity."),
               S("Control totals", text="Total assets = total equity and liabilities. If they do not agree, look first at the result, the depreciation and the regularisation accounts, which appear in both statements."),
           ]),
        MISTAKE("Answering four questions from Section A", "Read the rubric: three from Section A and two from Section B. Extra answers waste time and may not be marked."),
        MISTAKE("Journal entries without dates or narrations", "Each entry needs a date, the account numbers and names, the amounts on the correct side and a short narration. These earn marks."),
        MISTAKE("Totals without workings", "A figure that appears from nowhere earns nothing if it is wrong. Number your workings and show the calculation."),
        QUIZ("According to the Board's 2023 report, how many questions does a candidate answer in Paper 3?",
             ["Three from Section A and two from Section B", "All seven questions", "Four from Section A and one from Section B", "Any five from either section"], 0,
             "Section A: four questions, answer three; Section B: three questions, answer two.",
             hint="Each section has its own choice.",
             feedback=["", "There is a choice in both sections.", "Section A allows only three answers.", "The choice is made within each section."]),
        QUIZ("Your balance sheet does not balance by FCFA 250 000, and an accrued expense of FCFA 250 000 was given. What is the most likely cause?",
             ["The accrued expense was charged in the income statement but not shown as a current liability", "The bank balance was copied wrongly", "Depreciation was charged twice", "The share capital is wrong"], 0,
             "An adjustment appears twice: in the income statement and in the balance sheet. A difference equal to one adjustment usually means one side was forgotten.",
             feedback=["", "Possible, but a difference equal to a given adjustment points to that adjustment.", "That would give a difference equal to the depreciation charge.", "Capital is copied from the trial balance and rarely wrong."],
             title="Quick check 2"),
        TIP("Use the Paper 3 practice paper after this lesson as a timed rehearsal (a KKEVO practice setting of 150 minutes for about 20 parts). It mixes all five Lower Sixth modules: invoices and VAT, depreciation and disposals, impairment, accruals, bank reconciliation and the statements.",
            title="Exam link"),
        PQ("List the columns of an impairment schedule and say what the journal must contain for a lost customer.",
           "Columns: customer, amount TTC, amount HT, rate, impairment needed, impairment held, increase, reversal. Lost customer: debit 651 with the HT amount, debit the VAT account (443) with the VAT, credit 416 with the TTC amount, and reverse the impairment held (debit 491, credit 7594)."),
        PQ("You have 3 hours (a practice setting) for five questions. How should you share the time, and why?",
           "About ten minutes to read and choose, then about 30 minutes for each question, leaving some minutes to check totals. Equal marks per question mean equal time; finishing all five earns more than perfecting four."),
        PQ("A candidate writes 'Net result 2 625 000' in the balance sheet but 2 265 000 in the income statement. What check would have found this, and how should the error be traced?",
           "The control total: the balance sheet would not balance (difference 360 000, divisible by 9, a sign of transposed digits). Compare the result in the two statements and copy the income statement figure into equity."),
        SUM("Paper 3 is Financial Accounting, 40% of the examination: Section A answer three of four; Section B answer two of three.",
            "2023 Section A topics: impairment with journals, ratios, invoices with permanent inventory, statements in vertical format.",
            "Read all questions, choose those you can finish, share time equally.",
            "Know the formats, number your workings, date and narrate journal entries, write in ink.",
            "Check every answer with a control total before moving on."),
    ]))
