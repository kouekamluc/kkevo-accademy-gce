"""Form 5 Principles of Accounts (O Level 0505): End-of-Year Adjustments & Inventory Valuation, Final Accounts &
Specialized Accounts, and the Examination module (Paper 1, Paper 2).

Draft content. Exam facts are only those of the Board's 2023 Ordinary Level report for 0505: Paper 1 = 50 multiple-choice
questions, all answered, 1 hour 30 minutes, 40% of the marks; Paper 2 = eight questions of 20 marks each, Section A five
OHADA-approach questions (any three), Section B three IAS/IFRS-approach questions (any two), 3 hours, 60% of the marks.
The OHADA approach is taught and short notes show where IAS/IFRS wording differs. Layouts of the SYSCOHADA statements
are simplified school versions: check your textbook and your teacher's layout. All FCFA figures are invented for
practice. EVERY figure in the statements, schedules and ledgers below is computed by this file with plain Python
arithmetic (integers, with assertions that each ledger and each balance sheet balances), so printed totals cannot
disagree with the workings.
"""

from .dsl import *  # noqa: F403

COURSE = ("principles-of-accounts", "form-5")

M_ADJ = "End-of-Year Adjustments & Inventory Valuation"
M_FIN = "Final Accounts & Specialized Accounts"
M_EXAM = "Examination"


# ---------------------------------------------------------------- small formatting helpers (all arithmetic is exact)
def n(x):
    """12345 -> '12 345'; negatives keep a minus sign."""
    x = int(round(x)) if float(x) == int(x) else x
    s = f"{abs(x):,}".replace(",", " ")
    return ("-" if x < 0 else "") + s


def r(label, a=None, b=None, w=27, c=11):
    """One aligned statement line with up to two money columns."""
    fa = "" if a is None else (a if isinstance(a, str) else n(a))
    fb = "" if b is None else (b if isinstance(b, str) else n(b))
    return f"{label:<{w}}{fa:>{c}}{fb:>{c}}".rstrip()


def ledger(title, dr, cr):
    """Stacked ledger account: debit side then credit side, both totalled; asserts that the two totals agree."""
    td, tc = sum(a for _, a in dr), sum(a for _, a in cr)
    assert td == tc, (title, td, tc)
    out = [title, "DEBIT"]
    out += [f"  {l:<32}{n(a):>10}" for l, a in dr]
    out += [f"  {'Total':<32}{n(td):>10}", "CREDIT"]
    out += [f"  {l:<32}{n(a):>10}" for l, a in cr]
    out += [f"  {'Total':<32}{n(tc):>10}"]
    return "\n".join(out)


def sl(cost, resid, life):
    return [(cost - resid) // life] * life if (cost - resid) % life == 0 else None


def db(cost, rate_pct, years):
    """Reducing balance: returns [(charge, accumulated, net book value)] for each year (rate as a whole percent)."""
    out, acc = [], 0
    for _ in range(years):
        nbv = cost - acc
        ch = nbv * rate_pct // 100
        assert nbv * rate_pct % 100 == 0
        acc += ch
        out.append((ch, acc, cost - acc))
    return out


def syd(cost, resid, life):
    total = life * (life + 1) // 2
    out = []
    for k in range(life):
        part = (cost - resid) * (life - k)
        assert part % total == 0
        out.append(part // total)
    return out


LESSONS = []

# ====================================================================== 1. Depreciation methods
_c, _s, _l = 1_000_000, 100_000, 4
_sl = sl(_c, _s, _l)
_db = db(_c, 40, _l)
_sy = syd(_c, _s, _l)
assert _sl == [225_000] * 4 and sum(_sy) == _c - _s == 900_000
assert [x[0] for x in _db] == [400_000, 240_000, 144_000, 86_400] and _db[-1][2] == 129_600
_t_methods = "\n".join([
    "Machine: cost 1 000 000, residual 100 000, 4 years",
    "Year   Straight-line  Reducing 40%   SYD",
    *[f"{k + 1:<7}{n(_sl[k]):>10}{n(_db[k][0]):>14}{n(_sy[k]):>10}" for k in range(4)],
    f"{'Total':<7}{n(sum(_sl)):>10}{n(sum(x[0] for x in _db)):>14}{n(sum(_sy)):>10}",
])
_t_nbv = "\n".join([
    "Net book value at the end of each year",
    "Year   Straight-line  Reducing 40%   SYD",
    *[f"{k + 1:<7}{n(_c - _sl[0] * (k + 1)):>10}{n(_db[k][2]):>14}{n(_c - sum(_sy[:k + 1])):>10}" for k in range(4)],
])
_led1 = ledger("Depreciation expense account (year 1)", [("Accumulated depreciation", 225_000)],
               [("Income statement", 225_000)])
_led2 = ledger("Accumulated depreciation account (end of year 2)",
               [("Balance c/d", 450_000)], [("Balance b/d (year 1)", 225_000), ("Depreciation expense (year 2)", 225_000)])
assert 225_000 * 2 == 450_000
# example 2: computer, reducing balance 20%
_pc = db(500_000, 20, 3)
assert _pc == [(100_000, 100_000, 400_000), (80_000, 180_000, 320_000), (64_000, 244_000, 256_000)]
_t_pc = "\n".join([
    "Computer: cost 500 000, 20% reducing balance",
    "Year  Opening NBV  Charge  Accumulated   NBV",
    *[f"{k + 1:<6}{n(500_000 - (_pc[k - 1][1] if k else 0)):>10}{n(_pc[k][0]):>9}{n(_pc[k][1]):>12}{n(_pc[k][2]):>9}" for k in range(3)],
])
# example 3: van SYD
_vs = syd(4_600_000, 100_000, 5)
assert _vs == [1_500_000, 1_200_000, 900_000, 600_000, 300_000] and sum(_vs) == 4_500_000
_t_van = "\n".join([
    "Van: cost 4 600 000, residual 100 000, 5 years",
    "Sum of digits = 5+4+3+2+1 = 15; base = 4 500 000",
    *[f"Year {k + 1}: {5 - k}/15 x 4 500 000 = {n(_vs[k]):>10}" for k in range(5)],
    f"Total depreciation               = {n(sum(_vs)):>10}",
])

LESSONS.append(lesson(
    module=M_ADJ, topic="Depreciation methods",
    title="Depreciation: straight-line, reducing balance and sum-of-the-years'-digits",
    slug="acc3-depreciation-methods", minutes=24,
    summary="Depreciation spreads the cost of a fixed asset over its useful life. Calculate the yearly charge by straight-line, "
            "diminishing (reducing) balance and sum-of-the-years'-digits, and record it in the ledger.",
    objectives=[
        "Explain why a business depreciates a fixed asset (the matching idea, not a fall in market value)",
        "Calculate the yearly charge by the straight-line, reducing balance and sum-of-the-years'-digits methods",
        "Record depreciation: debit the expense, credit accumulated depreciation, and find the net book value",
        "Choose the method that fits a question and show the working in an organised schedule",
    ],
    key_concepts=["Depreciation", "Straight-line", "Reducing (diminishing) balance", "Sum-of-the-years'-digits", "Residual value", "Net book value"],
    blocks=[
        H("Why we depreciate"),
        T("Mama Rose buys a grinding mill for her shop in Bafoussam. She expects to use it for four years. She does not want "
          "all the cost in the first year's profit, because the mill helps her earn money in all four years. Accountants "
          "share the cost of the asset over the years it is used. This sharing is called **depreciation**. "
          "All the figures in this lesson are **invented for practice**."),
        D("**Depreciation** is the part of the cost of a fixed asset that is charged as an expense in each year of its useful life. "
          "It spreads cost; it does not measure the market price of the asset and it is not a payment of cash.", title="Depreciation"),
        D("**Cost** is the price paid plus the expenses needed to bring the asset into use (transport, installation). "
          "**Residual value** (scrap value) is the amount expected when the asset is sold or scrapped at the end of its life. "
          "**Net book value (NBV)** = cost minus accumulated depreciation. **Accumulated depreciation** is the total charged so far.",
          title="Four words to know"),
        T("In the OHADA approach the yearly charge is called a **dotation aux amortissements** and the total so far is "
          "the **amortissements** (accumulated amount). In the IAS/IFRS approach the words are **depreciation expense** and "
          "**accumulated depreciation**. The idea is the same."),
        H("Method 1: straight-line"),
        KEY("Straight-line", "The same amount every year.",
            cards=[["Formula", "Yearly charge = (cost − residual value) ÷ useful life in years"],
                   ["Use it when", "The asset gives the same benefit each year, for example a building or office furniture."]]),
        KEY("Reducing balance", "A fixed percentage of the net book value at the start of the year, so the charge falls each year.",
            cards=[["Formula", "Yearly charge = rate % × net book value at the start of the year"],
                   ["Use it when", "The asset loses more usefulness in its early years, for example a vehicle or a computer."],
                   ["Note", "The residual value is not subtracted before applying the rate unless the question says so."]]),
        KEY("Sum-of-the-years'-digits",
            "Add the digits of the years of life (4 years: 4 + 3 + 2 + 1 = 10). Year 1 takes 4/10 of (cost − residual value), year 2 takes 3/10, "
            "and so on. The charge falls by the same amount each year and the total depreciation equals cost − residual value.",
            cards=[["Formula", "Charge in year k = (years of life left at the start of year k) ÷ (sum of digits) × (cost − residual value)"]]),
        EX("Worked example 1: one machine, three methods",
           intro="A machine costs FCFA 1 000 000. The residual value is FCFA 100 000 and the life is 4 years. Compare the three methods "
                 "(reducing balance at 40%).",
           steps=[
               S("Straight-line", text="(1 000 000 − 100 000) ÷ 4 = 225 000 each year."),
               S("Reducing balance 40%", text="Year 1: 40% × 1 000 000 = 400 000. Year 2: 40% × 600 000 = 240 000. Year 3: 40% × 360 000 = 144 000. Year 4: 40% × 216 000 = 86 400."),
               S("SYD", text="Digits sum to 10 and the base is 900 000. Charges: 4/10 = 360 000, 3/10 = 270 000, 2/10 = 180 000, 1/10 = 90 000."),
               S("Present the schedule", text="Put the three methods side by side so that the totals can be checked."),
           ]),
        CODE(_t_methods, "text", title="Schedule of annual charges (invented for practice)"),
        T("Look at the totals. Straight-line and SYD both depreciate exactly cost minus residual value (900 000) over the life. "
          "Reducing balance leaves 129 600 on the books at the end of year 4, because a fixed percentage never reaches zero."),
        IMG("f5acc3-depreciation-methods.svg",
            alt="Bar chart of yearly depreciation for four years: straight-line is level, reducing balance and sum-of-the-years'-digits fall each year.",
            caption="Figure 1. Yearly charge under the three methods for the machine above."),
        H("Recording depreciation in the ledger"),
        D("Each year: **debit** Depreciation expense (dotations aux amortissements), **credit** Accumulated depreciation (amortissements). "
          "The expense is closed to the income statement. The accumulated depreciation stays as a credit balance and is "
          "subtracted from the cost of the asset on the balance sheet.", title="Double entry"),
        CODE(_led1 + "\n\n" + _led2, "text", title="Straight-line ledger entries (invented for practice)"),
        EX("Worked example 2: reducing balance",
           intro="A computer cost FCFA 500 000 on 1 January of year 1. The business uses 20% reducing balance. Find the charge for each of three years "
                 "and the NBV at the end of year 3.",
           steps=[
               S("Year 1", text="20% × 500 000 = 100 000. NBV = 400 000."),
               S("Year 2", text="Apply the rate to the NBV, not to the cost: 20% × 400 000 = 80 000. NBV = 320 000."),
               S("Year 3", text="20% × 320 000 = 64 000. Accumulated depreciation = 244 000, so NBV = 256 000."),
           ]),
        CODE(_t_pc, "text", title="Reducing balance schedule (invented for practice)"),
        EX("Worked example 3: sum-of-the-years'-digits",
           intro="A delivery van costs FCFA 4 600 000, residual value FCFA 100 000, life 5 years. Find the charge for each year.",
           steps=[
               S("Sum of the digits", text="5 + 4 + 3 + 2 + 1 = 15."),
               S("Base amount", text="4 600 000 − 100 000 = 4 500 000."),
               S("Charge each year", text="Year 1 = 5/15 × 4 500 000 = 1 500 000; then 1 200 000, 900 000, 600 000 and 300 000."),
               S("Check", text="1 500 000 + 1 200 000 + 900 000 + 600 000 + 300 000 = 4 500 000 = cost − residual value."),
           ]),
        CODE(_t_van, "text", title="SYD working (invented for practice)"),
        MISTAKE("Using the original cost every year in reducing balance",
                "The rate is applied to the **net book value at the start of the year**. Using the cost each year gives the straight-line "
                "answer by accident. The Board's 2023 report says many candidates could not apply the reducing balance method, so practise it."),
        MISTAKE("Forgetting the residual value in SYD and straight-line",
                "Subtract the residual value first. In reducing balance, follow the question: usually the percentage is applied to NBV only."),
        MISTAKE("Calling depreciation a cash payment",
                "Depreciation is a book entry. No money leaves the business when the entry is made; the cash was spent when the asset was bought."),
        QUIZ("Using the machine of the lesson (cost 1 000 000, residual 100 000, 4 years), which method gives the largest charge in year 1?",
             ["Straight-line, 225 000", "Reducing balance at 40%, 400 000", "SYD, 360 000", "All three give the same charge in year 1"], 1,
             "40% × 1 000 000 = 400 000, which is larger than 360 000 (SYD) and 225 000 (straight-line).",
             hint="Work out the year 1 charge by each method and compare.",
             feedback=["Straight-line spreads the cost evenly, so its year 1 charge is the smallest here.", "",
                       "SYD gives 4/10 × 900 000 = 360 000, which is less than 400 000.",
                       "The methods differ from year 1 onwards."]),
        QUIZ("Which statement about depreciation is correct?",
             ["It records the fall in the market price of the asset", "It is a cash payment into a special fund",
              "It spreads the cost of the asset over its useful life", "It is added to the cost of the asset on the balance sheet"], 2,
             "Depreciation is the allocation of cost to the years in which the asset is used.",
             feedback=["The market price may fall by a different amount; depreciation follows the allocation method.",
                       "No cash is paid; it is a book entry.", "",
                       "Accumulated depreciation is subtracted from cost, giving the net book value."], title="Quick check 2"),
        TIP("Depreciation (including reducing balance) is one of the end-of-year adjustments the Board's report lists for Paper 2, and "
            "it can also appear in Paper 1 multiple-choice questions. Draw a schedule: year, opening NBV, charge, accumulated, closing NBV.",
            title="Exam link"),
        PQ("A tractor costs FCFA 6 400 000 with a residual value of FCFA 400 000 and a life of 5 years. Find the straight-line charge for one year.",
           "(6 400 000 − 400 000) ÷ 5 = 1 200 000."),
        PQ("Equipment costs FCFA 800 000 and is depreciated at 25% reducing balance. Find the charge in year 2 and the NBV at the end of year 2.",
           "Year 1: 25% × 800 000 = 200 000, NBV 600 000. Year 2: 25% × 600 000 = 150 000, NBV 450 000."),
        PQ("An asset costs FCFA 1 500 000, residual value FCFA 150 000, life 3 years. Find the SYD charge for each year.",
           "Digits 3 + 2 + 1 = 6; base 1 350 000. Year 1 = 3/6 × 1 350 000 = 675 000; year 2 = 2/6 × 1 350 000 = 450 000; year 3 = 225 000. Total 1 350 000."),
        PQ("Write the double entry for a yearly depreciation charge of FCFA 225 000.",
           "Debit Depreciation expense (dotations aux amortissements) 225 000; credit Accumulated depreciation (amortissements) 225 000."),
        SUM("Depreciation spreads the cost of a fixed asset over its useful life; it is not cash and not market value.",
            "Straight-line: (cost − residual) ÷ life. Reducing balance: rate × NBV at the start of the year. SYD: (years left ÷ sum of digits) × (cost − residual).",
            "Entry: debit depreciation expense, credit accumulated depreciation. NBV = cost − accumulated depreciation.",
            "Show a schedule and check that the totals agree with cost − residual (straight-line and SYD)."),
    ]))

# ====================================================================== 2. Disposal of fixed assets
_dc, _dadep, _dpro = 1_000_000, 600_000, 450_000
_dnbv = _dc - _dadep
assert (_dnbv, _dpro - _dnbv) == (400_000, 50_000) and _dc * 20 // 100 * 3 == _dadep
_led_p = ledger("Disposal of machinery account (profit case)",
                [("Machinery (cost)", _dc), ("Profit on disposal", _dpro - _dnbv)],
                [("Accumulated depreciation", _dadep), ("Bank (sale proceeds)", _dpro)])
_dloss = _dnbv - 330_000
assert _dloss == 70_000
_led_l = ledger("Disposal of machinery account (loss case)",
                [("Machinery (cost)", _dc)],
                [("Accumulated depreciation", _dadep), ("Bank (sale proceeds)", 330_000), ("Loss on disposal", _dloss)])
_t_sum = "\n".join([
    "Cost                          " + n(_dc).rjust(10),
    "Less accumulated depreciation " + n(_dadep).rjust(10),
    "Net book value                " + n(_dnbv).rjust(10),
    "Sale proceeds                 " + n(_dpro).rjust(10),
    "Profit on disposal            " + n(_dpro - _dnbv).rjust(10),
])
# part exchange
_vc, _va, _vallow, _vnew = 3_000_000, 1_800_000, 1_500_000, 4_500_000
_vnbv = _vc - _va
assert _vnbv == 1_200_000 and _vallow - _vnbv == 300_000 and _vnew - _vallow == 3_000_000
_led_x = ledger("Disposal of old vehicle account",
                [("Vehicle (cost)", _vc), ("Profit on disposal", _vallow - _vnbv)],
                [("Accumulated depreciation", _va), ("New vehicle (allowance)", _vallow)])
_led_y = ledger("New vehicle account (cost)",
                [("Disposal account (allowance)", _vallow), ("Bank (balance paid)", _vnew - _vallow)],
                [("Cost of new vehicle", _vnew)])

LESSONS.append(lesson(
    module=M_ADJ, topic="Disposal of fixed assets",
    title="Disposal of fixed assets: the disposal account, profit, loss and part-exchange",
    slug="acc3-disposal-of-fixed-assets", minutes=22,
    summary="When a fixed asset is sold, compare the proceeds with its net book value to find the profit or loss, and record it with a disposal account, including a part-exchange.",
    objectives=[
        "Calculate the net book value of an asset at the date of sale",
        "Find the profit or loss on disposal by comparing proceeds with net book value",
        "Prepare a disposal account, putting profit on the debit side and loss on the credit side",
        "Record a part-exchange allowance when an old asset is traded in for a new one",
    ],
    key_concepts=["Disposal", "Net book value", "Profit or loss on disposal", "Disposal account", "Part-exchange"],
    blocks=[
        H("Selling a fixed asset"),
        T("A transport company in Douala sells an old truck and buys a new one. The old truck was in the books at cost, with depreciation "
          "built up over the years. When it is sold, the books must remove the truck and its accumulated depreciation and record the "
          "difference between the **sale price** and the **book value**. All figures here are **invented for practice**."),
        D("The **net book value (NBV)** at the date of sale is cost minus accumulated depreciation up to that date. "
          "**Profit on disposal** = proceeds − NBV when proceeds are higher. **Loss on disposal** = NBV − proceeds when proceeds are lower.",
          title="Profit or loss on disposal"),
        T("A profit or loss on disposal appears because depreciation was only an estimate. If the asset sells for more than its NBV, "
          "too much depreciation was charged in the past, so there is a profit. In the OHADA approach this result belongs to the "
          "exceptional items (**hors activités ordinaires**, HAO): the sale price and the book value of the asset sold are shown as "
          "separate lines. In the IAS/IFRS approach we speak of a **gain or loss on disposal**. Check your textbook for the layout used in your class."),
        KEY("Four steps for a disposal",
            "Follow the same four steps each time.",
            cards=[["1. Cost", "Take the asset's cost from the asset account."],
                   ["2. Accumulated depreciation", "Include depreciation up to the date of disposal. Follow the question about part years."],
                   ["3. NBV and result", "Compare proceeds with NBV."],
                   ["4. Disposal account", "Debit cost, credit accumulated depreciation, credit proceeds; the balancing figure is the profit (debit) or loss (credit)."]]),
        EX("Worked example 1: sale at a profit",
           intro="A machine cost FCFA 1 000 000 and was depreciated at 20% of cost per year (straight-line). After 3 years it is sold for "
                 "FCFA 450 000 by bank transfer. Find the profit or loss and prepare the disposal account.",
           steps=[
               S("Accumulated depreciation", text="20% × 1 000 000 = 200 000 a year; 3 years give 600 000."),
               S("Net book value", text="1 000 000 − 600 000 = 400 000."),
               S("Result", text="450 000 − 400 000 = 50 000 profit."),
               S("Disposal account", text="Debit the cost and the profit. Credit the accumulated depreciation and the proceeds. Both sides total 1 050 000."),
           ]),
        CODE(_t_sum, "text", title="Disposal summary (invented for practice)"),
        CODE(_led_p, "text", title="Disposal account, profit case"),
        EX("Worked example 2: sale at a loss",
           intro="The same machine is instead sold for FCFA 330 000. Find the loss and prepare the disposal account.",
           steps=[
               S("Loss", text="NBV 400 000 − proceeds 330 000 = 70 000 loss."),
               S("Disposal account", text="Debit the cost (1 000 000). Credit the accumulated depreciation (600 000), the proceeds (330 000) and the loss (70 000). Both sides total 1 000 000."),
               S("Transfer", text="The loss of 70 000 is a debit in the income statement (an expense)."),
           ]),
        CODE(_led_l, "text", title="Disposal account, loss case"),
        D("In a disposal account a **profit** is the balancing figure on the **debit** side, and a **loss** is the balancing figure on the "
          "**credit** side. If the two sides do not agree after you enter cost, depreciation and proceeds, the balancing figure is the result.",
          title="Where the result goes"),
        H("Part-exchange"),
        T("Sometimes the old asset is traded in against a new one. The dealer allows an amount for the old asset and you pay the rest. "
          "Treat the **allowance** as the sale proceeds of the old asset, and as part of the cost of the new asset."),
        EX("Worked example 3: part-exchange of a vehicle",
           intro="A vehicle cost FCFA 3 000 000. Accumulated depreciation is FCFA 1 800 000. It is traded in for a new vehicle costing "
                 "FCFA 4 500 000, with an allowance of FCFA 1 500 000. The balance is paid by bank. Find the result and the entries.",
           steps=[
               S("NBV of the old vehicle", text="3 000 000 − 1 800 000 = 1 200 000."),
               S("Result", text="Allowance 1 500 000 − NBV 1 200 000 = 300 000 profit."),
               S("Balance paid", text="4 500 000 − 1 500 000 = 3 000 000 by bank."),
               S("Accounts", text="Disposal account: the allowance is credited. New vehicle account: the allowance is debited together with the bank payment, giving the cost of 4 500 000."),
           ]),
        CODE(_led_x + "\n\n" + _led_y, "text", title="Part-exchange ledger entries"),
        MISTAKE("Using cost instead of NBV to find the profit",
                "The profit or loss compares the proceeds with the **net book value**, not with the original cost. Always work out NBV first."),
        MISTAKE("Putting the loss on the debit side",
                "In the disposal account the cost is already on the debit side. A loss is the figure that makes the credit side equal the debit side, so it is on the credit side."),
        MISTAKE("Forgetting to remove the accumulated depreciation",
                "When the asset leaves the books, its accumulated depreciation must also leave. Credit the accumulated depreciation to the disposal account; otherwise the balance sheet keeps depreciation on an asset that no longer exists."),
        QUIZ("An asset cost FCFA 800 000 and has accumulated depreciation of FCFA 500 000. It is sold for FCFA 250 000. The result is",
             ["A profit of FCFA 250 000", "A loss of FCFA 50 000", "A profit of FCFA 50 000", "A loss of FCFA 300 000"], 1,
             "NBV = 800 000 − 500 000 = 300 000. Proceeds 250 000 are lower, so the loss is 50 000.",
             hint="Find the net book value first.",
             feedback=["That compares the proceeds with zero, not with the NBV.", "",
                       "Proceeds are less than NBV, so this is a loss, not a profit.",
                       "That subtracts the proceeds from the cost; the right comparison uses NBV."]),
        QUIZ("In the disposal account, the profit on disposal appears",
             ["On the debit side", "On the credit side", "Only in the bank account", "In the capital account"], 0,
             "The cost is debited; with the credits for depreciation and proceeds, a profit is the debit balancing figure.",
             feedback=["", "A loss is the credit balancing figure.", "The bank account holds only the cash received.", "Profit moves to the income statement, then to capital."],
             title="Quick check 2"),
        TIP("Disposal questions link depreciation and the disposal account. The Board's report lists depreciation among the tested adjustments. "
            "Practise the four steps: cost, accumulated depreciation, NBV, result.", title="Exam link"),
        PQ("A computer cost FCFA 600 000 and has accumulated depreciation of FCFA 360 000. It is sold for FCFA 300 000. Find the profit or loss.",
           "NBV = 600 000 − 360 000 = 240 000. Profit = 300 000 − 240 000 = 60 000."),
        PQ("A van cost FCFA 2 400 000 and is depreciated at 25% a year on cost for 2 years, then sold for FCFA 1 000 000. Find the result.",
           "Accumulated depreciation = 25% × 2 400 000 × 2 = 1 200 000. NBV = 1 200 000. Loss = 1 200 000 − 1 000 000 = 200 000."),
        PQ("State the entries in the disposal account for the van in the previous question.",
           "Debit: Van (cost) 2 400 000. Credit: Accumulated depreciation 1 200 000; Bank 1 000 000; Loss on disposal 200 000. Both sides total 2 400 000."),
        PQ("Equipment cost FCFA 900 000, accumulated depreciation FCFA 600 000. It is part-exchanged for new equipment costing FCFA 1 200 000 with an allowance of FCFA 350 000. Find the result and the cash to pay.",
           "NBV = 300 000. Allowance 350 000 − 300 000 = 50 000 profit. Cash to pay = 1 200 000 − 350 000 = 850 000."),
        SUM("Net book value = cost − accumulated depreciation at the date of disposal.",
            "Profit = proceeds − NBV (if positive); loss = NBV − proceeds (if positive).",
            "Disposal account: debit cost; credit accumulated depreciation and proceeds; profit is a debit balance, loss is a credit balance.",
            "Part-exchange: the allowance is the proceeds of the old asset and part of the cost of the new asset."),
    ]))

# ====================================================================== 3. Bad debts and provision for doubtful debts
_bd1, _bd2 = 25_000, 15_000
_btot = _bd1 + _bd2
_brec = 800_000
_bnet = _brec - _btot
_bprov = _bnet * 5 // 100
_bopen = 30_000
assert (_btot, _bnet, _bprov, _bprov - _bopen) == (40_000, 760_000, 38_000, 8_000) and _bnet * 5 % 100 == 0
_led_bd = ledger("Bad debts account (year 1)",
                 [("Kamga (written off)", _bd1), ("Ndi (written off)", _bd2)], [("Income statement", _btot)])
_led_pr1 = ledger("Provision for doubtful debts account (year 1)",
                  [("Balance c/d", _bprov)], [("Balance b/d", _bopen), ("Income statement (increase)", _bprov - _bopen)])
_b2 = 600_000
_bprov2 = _b2 * 5 // 100
assert _bprov2 == 30_000 and _bprov - _bprov2 == 8_000
_led_pr2 = ledger("Provision for doubtful debts account (year 2)",
                  [("Income statement (decrease)", _bprov - _bprov2), ("Balance c/d", _bprov2)], [("Balance b/d", _bprov)])
_t_is = "\n".join([
    "Income statement extract, year 1",
    r("Bad debts written off", 40_000),
    r("Increase in provision (38 000 - 30 000)", 8_000, w=42),
    r("Total charge for doubtful debts", 48_000, w=42),
])
assert 40_000 + 8_000 == 48_000
_t_bs = "\n".join([
    "Balance sheet extract, end of year 1",
    r("Trade receivables (800 000 - 40 000)", _bnet, w=42),
    r("Less provision for doubtful debts", -_bprov, w=42),
    r("Net trade receivables", _bnet - _bprov, w=42),
])
assert _bnet - _bprov == 722_000

LESSONS.append(lesson(
    module=M_ADJ, topic="Bad debts and provision for doubtful debts",
    title="Bad debts and the provision for doubtful debts",
    slug="acc3-bad-debts-and-provisions", minutes=22,
    summary="Write off debts that will never be paid, estimate a provision for debts that may not be paid, and show the charge in the income statement and the net amount on the balance sheet.",
    objectives=[
        "Distinguish a bad debt from a doubtful debt",
        "Record a bad debt written off and a bad debt recovered",
        "Calculate a provision for doubtful debts as a percentage and record an increase or a decrease",
        "Show receivables net of the provision on the balance sheet",
    ],
    key_concepts=["Bad debt", "Doubtful debt", "Provision for doubtful debts", "Bad debt recovered", "Net receivables"],
    blocks=[
        H("Customers who do not pay"),
        T("Papa Njoh sells goods on credit to shops in Bamenda. Most customers pay, but a few never do. Profit must not be overstated by "
          "counting money that will never arrive. Two ideas protect the accounts: **writing off** debts that are certainly lost, and "
          "making a **provision** for debts that may be lost. All figures are **invented for practice**."),
        D("A **bad debt** is an amount owed by a customer that cannot be recovered (the customer is bankrupt, has disappeared, or refuses to pay and cannot be forced). "
          "It is an **expense**, written off by crediting the customer's account.", title="Bad debt"),
        D("A **provision for doubtful debts** is an amount set aside from profit because some receivables (debtors) are expected to go bad, "
          "although we do not yet know which ones. It is a percentage estimate of the remaining receivables. "
          "In the OHADA approach this is the **dépréciation des créances clients**; in the IAS/IFRS approach it is often called an **allowance for receivables**. "
          "Account names and numbers differ between textbooks: use the names your teacher gives.", title="Provision for doubtful debts"),
        KEY("Two different entries",
            "Do not mix the two. Bad debts are known losses. The provision is an estimate.",
            cards=[["Bad debt written off", "Debit Bad debts (expense). Credit the customer's account (trade receivables)."],
                   ["Provision for doubtful debts", "Debit the income statement with the increase (credit it with a decrease). Credit or debit the provision account."],
                   ["Order", "First write off the bad debts. Then calculate the provision on the receivables that are left."]]),
        EX("Worked example 1: write-off and provision",
           intro="At the end of year 1 trade receivables are FCFA 800 000. Two customers are bad: Kamga FCFA 25 000 and Ndi FCFA 15 000. "
                 "The business keeps a provision of 5% of the remaining receivables. The provision account has a credit balance "
                 "of FCFA 30 000 brought down from last year. Find the charge to the income statement.",
           steps=[
               S("Write off the bad debts", text="25 000 + 15 000 = 40 000. Receivables left = 800 000 − 40 000 = 760 000."),
               S("New provision", text="5% × 760 000 = 38 000."),
               S("Compare with the old provision", text="38 000 − 30 000 = 8 000 increase, so 8 000 is charged to the income statement."),
               S("Total expense", text="Bad debts 40 000 + increase in provision 8 000 = 48 000."),
           ]),
        CODE(_led_bd + "\n\n" + _led_pr1, "text", title="Ledger entries, year 1 (invented for practice)"),
        CODE(_t_is + "\n\n" + _t_bs, "text", title="Where the figures go"),
        T("The balance sheet shows receivables **less** the provision, so the reader sees the amount the business really expects to collect "
          "(722 000). Receivables in the ledger stay at 760 000; the provision is not taken out of the customers' accounts."),
        EX("Worked example 2: the provision falls",
           intro="In year 2 receivables, after write-offs, are FCFA 600 000 and the rate is still 5%. The old provision is FCFA 38 000. Find the entry.",
           steps=[
               S("New provision", text="5% × 600 000 = 30 000."),
               S("Change", text="38 000 − 30 000 = 8 000 decrease."),
               S("Entry", text="Debit the provision account 8 000; credit the income statement 8 000. A decrease **reduces** the expenses (or adds to profit)."),
           ]),
        CODE(_led_pr2, "text", title="Provision account, year 2"),
        H("Bad debts recovered"),
        T("Sometimes a customer whose debt was written off pays later. Reopen the customer's account for the payment, then credit "
          "the amount to **Bad debts recovered** (an income). For example, if Ndi pays FCFA 10 000 later: (1) debit Ndi's account 10 000 and credit Bad debts recovered 10 000; (2) debit Bank 10 000 and credit Ndi's account 10 000."),
        MISTAKE("Calculating the provision before writing off bad debts",
                "The percentage is applied to the receivables **after** the bad debts are written off (760 000 in the example, not 800 000)."),
        MISTAKE("Charging the whole provision to the income statement",
                "Only the **change** in the provision goes to the income statement. If the old provision was 30 000 and the new one is 38 000, charge 8 000."),
        MISTAKE("Treating a decrease as an expense",
                "If the new provision is smaller, the difference is credited to the income statement and increases profit."),
        QUIZ("Receivables are FCFA 500 000. Bad debts of FCFA 20 000 are written off. A provision of 4% is required and the old provision was FCFA 15 000. What is charged to the income statement for the change in the provision?",
             ["FCFA 4 200", "FCFA 5 000", "FCFA 19 200", "FCFA 20 000"], 0,
             "Receivables after write-off = 480 000. 4% of 480 000 = 19 200. Increase = 19 200 - 15 000 = 4 200.",
             hint="Remove the bad debts before applying the percentage.",
             feedback=["", "That applies 4% to 500 000 (giving 20 000, less 15 000) before the bad debts are removed.",
                       "That is the whole new provision. Only the change is charged.", "That is the bad debt written off, a separate expense."]),
        QUIZ("Which treatment is correct for a provision that needs to fall from FCFA 38 000 to FCFA 30 000?",
             ["Debit the income statement with 8 000", "Credit the income statement with 8 000", "Debit the bank account with 8 000", "Write off 8 000 as bad debts"], 1,
             "A smaller provision releases 8 000 back to profit: debit the provision account, credit the income statement.",
             feedback=["That would be an increase in the provision.", "", "The bank is not involved: no cash moves.", "Bad debts are customers who will not pay; this is a change in an estimate."],
             title="Quick check 2"),
        TIP("The Board's 2023 report mentions end-of-year adjustments as an examined area. Questions give a rate and ask for the charge in the income statement and the receivables in the balance sheet. "
            "Check that your answer uses the receivables after write-offs.", title="Exam link"),
        PQ("Trade receivables are FCFA 400 000 and bad debts of FCFA 16 000 are to be written off. The provision is 5% of the remaining receivables. Find the new provision.",
           "400 000 − 16 000 = 384 000. 5% × 384 000 = 19 200."),
        PQ("The old provision was FCFA 12 000 and the new one is FCFA 19 200. What is charged to the income statement?",
           "19 200 − 12 000 = 7 200 increase, charged as an expense."),
        PQ("Show how receivables appear on the balance sheet when receivables are FCFA 384 000 and the provision is FCFA 19 200.",
           "Trade receivables 384 000, less provision 19 200, net 364 800."),
        PQ("A debt of FCFA 10 000 written off last year is paid this year. Give the double entry.",
           "Debit Bank 10 000; credit Bad debts recovered 10 000 (through the customer's account if it was reopened)."),
        SUM("A bad debt is a known loss: debit bad debts (expense), credit the customer's account.",
            "A provision is an estimate on the receivables that remain after write-offs.",
            "Only the change in the provision goes to the income statement: an increase is an expense, a decrease adds to profit.",
            "The balance sheet shows receivables less the provision; recovered bad debts are income."),
    ]))

# ====================================================================== 4. Accruals and prepayments
_a_paid, _a_acc = 84_000, 14_000
_a_ins, _a_ins_m = 120_000, 3
_a_ins_exp = _a_ins * _a_ins_m // 12
_a_ins_pre = _a_ins - _a_ins_exp
assert (_a_paid + _a_acc, _a_ins_exp, _a_ins_pre) == (98_000, 30_000, 90_000) and _a_ins * _a_ins_m % 12 == 0
_a_rent_rec, _a_rent_adv = 240_000, 40_000
_a_com_rec, _a_com_acc = 150_000, 25_000
_la = ledger("Electricity account", [("Bank (paid)", _a_paid), ("Balance c/d (accrued)", _a_acc)],
             [("Income statement", _a_paid + _a_acc)])
_lb = ledger("Insurance account", [("Bank (paid)", _a_ins)],
             [("Income statement (3 months)", _a_ins_exp), ("Balance c/d (prepaid)", _a_ins_pre)])
_lc = ledger("Rent received account", [("Income statement", _a_rent_rec - _a_rent_adv), ("Balance c/d (in advance)", _a_rent_adv)],
             [("Bank (received)", _a_rent_rec)])
_ld = ledger("Commission received account", [("Income statement", _a_com_rec + _a_com_acc)],
             [("Bank (received)", _a_com_rec), ("Balance c/d (accrued)", _a_com_acc)])
# profit effect table
_p0 = 500_000
_p1 = _p0 - _a_acc + _a_ins_pre - _a_rent_adv + _a_com_acc
assert _p1 == 561_000
_t_eff = "\n".join([
    "Profit before the four adjustments    " + n(_p0).rjust(8),
    "Electricity accrued (more expense)    " + n(-_a_acc).rjust(8),
    "Insurance prepaid (less expense)      " + n(_a_ins_pre).rjust(8),
    "Rent received in advance (less income)" + n(-_a_rent_adv).rjust(8),
    "Commission accrued (more income)      " + n(_a_com_acc).rjust(8),
    "Corrected profit                      " + n(_p1).rjust(8),
])
_t_bs4 = "\n".join([
    "Balance sheet items created by the four adjustments",
    r("Current asset: prepaid insurance", _a_ins_pre, w=40),
    r("Current asset: accrued commission", _a_com_acc, w=40),
    r("Current liability: electricity owing", _a_acc, w=40),
    r("Current liability: rent in advance", _a_rent_adv, w=40),
])

LESSONS.append(lesson(
    module=M_ADJ, topic="Accruals and prepayments",
    title="Accruals and prepayments: matching expenses and income to the year",
    slug="acc3-accruals-and-prepayments", minutes=22,
    summary="Adjust expenses and incomes so that each year bears only what belongs to it: accrued and prepaid expenses, accrued income and income received in advance, in the ledger and on the balance sheet.",
    objectives=[
        "Explain the matching idea: an expense or income belongs to the year in which it is used or earned, not the year in which cash moves",
        "Adjust expense accounts for accruals and prepayments",
        "Adjust income accounts for accrued income and income received in advance",
        "Show each adjustment in the income statement and the balance sheet and explain its effect on profit",
    ],
    key_concepts=["Accrual", "Prepayment", "Accrued income", "Income received in advance", "Matching"],
    blocks=[
        H("The year gets the costs that belong to it"),
        T("A shop in Yaoundé pays its electricity bill for December in January. A trader pays a year's insurance in October. "
          "If we only counted the cash paid in the year, the profit would be wrong. The **accrual concept** (also called the "
          "**matching concept**) says: record expenses and incomes in the year they relate to, not in the year the cash moves. "
          "All figures here are **invented for practice**."),
        D("An **accrued expense** (accrual) is an expense of this year that has not yet been paid. A **prepaid expense** (prepayment) "
          "is an amount paid this year for a future year. In the OHADA approach these are **charges à payer** and **charges constatées d'avance**.",
          title="Expenses"),
        D("**Accrued income** is income earned this year but not yet received. **Income received in advance** is cash received this year for a future "
          "year. In the OHADA approach these are **produits à recevoir** and **produits constatés d'avance**. In IAS/IFRS wording they are "
          "often called accrued income and deferred income.", title="Incomes"),
        KEY("What happens to profit",
            "Learn the four effects. They also tell you where each balance sheet item appears.",
            cards=[["Accrued expense", "Expense increases, profit falls. Shown as a current liability."],
                   ["Prepaid expense", "Expense decreases, profit rises. Shown as a current asset."],
                   ["Accrued income", "Income increases, profit rises. Shown as a current asset."],
                   ["Income received in advance", "Income decreases, profit falls. Shown as a current liability."]]),
        EX("Worked example 1: electricity accrued",
           intro="Electricity paid during the year is FCFA 84 000. The December bill of FCFA 14 000 is unpaid at the year end. Find the expense and show the account.",
           steps=[
               S("Expense for the year", text="84 000 paid + 14 000 owing = 98 000."),
               S("Adjustment", text="Add 14 000 to the debit side as the balance carried down. The income statement takes 98 000."),
               S("Next year", text="The 14 000 comes down as a credit balance (an amount owed)."),
           ]),
        CODE(_la, "text", title="Electricity account"),
        EX("Worked example 2: insurance prepaid",
           intro="On 1 October the business paid FCFA 120 000 for 12 months of insurance. The year ends on 31 December. Find the expense for the year and the prepayment.",
           steps=[
               S("Months used", text="October, November, December = 3 months."),
               S("Expense", text="3 ÷ 12 × 120 000 = 30 000."),
               S("Prepayment", text="120 000 − 30 000 = 90 000 is carried down as a debit balance (an asset)."),
           ]),
        CODE(_lb, "text", title="Insurance account"),
        H("Income accounts"),
        EX("Worked example 3: income received in advance and income accrued",
           intro="Rent received during the year is FCFA 240 000, of which FCFA 40 000 is for next year. Commission received is FCFA 150 000, "
                 "but FCFA 25 000 more was earned and is still to come. Find the income for the year.",
           steps=[
               S("Rent", text="240 000 − 40 000 in advance = 200 000 earned this year."),
               S("Commission", text="150 000 + 25 000 accrued = 175 000 earned this year."),
               S("Balances carried down", text="Rent: 40 000 credit balance (a liability). Commission: 25 000 debit balance (an asset)."),
           ]),
        CODE(_lc + "\n\n" + _ld, "text", title="Income accounts"),
        CODE(_t_eff, "text", title="Effect on profit (invented for practice)"),
        CODE(_t_bs4, "text", title="Where the balances appear on the balance sheet"),
        MISTAKE("Adding a prepayment to the expense",
                "A prepayment is the part of the amount paid that belongs to the **next** period. Subtract it from the cash paid to find the expense."),
        MISTAKE("Mixing the sides of the account",
                "For an expense: cash paid + accrual, or cash paid − prepayment. For an income: cash received + accrued income, or cash received − income in advance."),
        MISTAKE("Counting cash instead of the year's amount",
                "A question that says 'the amount paid was FCFA 84 000' is not asking for 84 000 as the expense when an accrual exists. Read the adjustment note."),
        QUIZ("Rent paid in the year is FCFA 300 000. FCFA 50 000 of this relates to next year. The rent expense for the year is",
             ["FCFA 350 000", "FCFA 300 000", "FCFA 250 000", "FCFA 50 000"], 2,
             "The prepayment of 50 000 is taken out: 300 000 − 50 000 = 250 000.",
             hint="Which part of the payment belongs to this year?",
             feedback=["That adds the prepayment instead of removing it.", "That ignores the adjustment.", "", "That is only the prepayment."]),
        QUIZ("Interest of FCFA 12 000 earned this year has not yet been received. It is",
             ["A current liability", "Accrued income, a current asset", "A prepaid expense", "Income received in advance"], 1,
             "Income that is earned but not yet received is owed to the business, so it is a current asset.",
             feedback=["A liability is something the business owes.", "", "Prepaid expenses are costs paid early, not income.", "Income in advance has been received already."],
             title="Quick check 2"),
        TIP("Adjustments appear in Paper 2 final-accounts questions and in Paper 1 multiple choice. Write each adjustment on its own line in the working: "
            "figure given, adjustment, figure for the income statement.", title="Exam link"),
        PQ("Wages paid are FCFA 480 000. Wages of FCFA 40 000 for the last week are unpaid. Find the wages expense.",
           "480 000 + 40 000 = 520 000."),
        PQ("Annual rent of FCFA 720 000 was paid on 1 July for the 12 months ending 30 June next year. The year end is 31 December. Find the rent expense and the prepayment.",
           "Six months used: 6/12 × 720 000 = 360 000 expense. Prepayment = 360 000."),
        PQ("Interest received is FCFA 60 000. FCFA 15 000 was received for next year. Find the interest income for the year.",
           "60 000 − 15 000 = 45 000."),
        PQ("Profit before adjustments is FCFA 400 000. A bill of FCFA 20 000 is accrued and FCFA 30 000 of insurance is prepaid. Find the corrected profit.",
           "400 000 − 20 000 + 30 000 = 410 000."),
        SUM("Match each expense and income to the year it relates to.",
            "Accrued expense: add to the expense, show a liability. Prepaid expense: subtract from the expense, show an asset.",
            "Accrued income: add to the income, show an asset. Income received in advance: subtract from the income, show a liability.",
            "Always check the effect on profit and the balance sheet side."),
    ]))

# ====================================================================== 5. Inventory valuation
_ev = [("1 Jan", "buy", 100, 500), ("10 Jan", "buy", 100, 600), ("15 Jan", "sell", 150, None),
       ("20 Jan", "buy", 100, 700), ("28 Jan", "sell", 90, None)]


def _fifo(events):
    layers, lines, cogs = [], [], 0
    for d, k, u, p in events:
        if k == "buy":
            layers.append([u, p])
            lines.append(f"{d:<7}Receive {u:>3} @ {p} = {n(u * p):>7}")
        else:
            need, first = u, True
            while need:
                take = min(need, layers[0][0])
                cogs += take * layers[0][1]
                lines.append(f"{d if first else '':<7}Issue   {take:>3} @ {layers[0][1]} = {n(take * layers[0][1]):>7}")
                first = False
                layers[0][0] -= take
                need -= take
                if layers[0][0] == 0:
                    layers.pop(0)
        bal = " + ".join(f"{a}@{b}" for a, b in layers)
        lines.append(f"       Balance: {bal} = {n(sum(a * b for a, b in layers))}")
    return lines, cogs, sum(a * b for a, b in layers)


def _mov(events):
    units, val, lines, cogs = 0, 0, [], 0
    for d, k, u, p in events:
        if k == "buy":
            units += u
            val += u * p
            lines.append(f"{d:<7}Receive {u:>3} @ {p} = {n(u * p):>7}")
        else:
            avg = val // units
            assert val % units == 0
            cogs += u * avg
            units -= u
            val -= u * avg
            lines.append(f"{d:<7}Issue   {u:>3} @ {avg} = {n(u * avg):>7}")
        lines.append(f"       Balance: {units} units, value {n(val)}, average {val // units if units else 0}")
        assert val % units == 0
    return lines, cogs, val


_fl, _fcogs, _fclose = _fifo(_ev)
_ml, _mcogs, _mclose = _mov(_ev)
_tu = sum(u for _, k, u, _p in _ev if k == "buy")
_tc = sum(u * p for _, k, u, p in _ev if k == "buy")
_sold = sum(u for _, k, u, _p in _ev if k == "sell")
assert (_tu, _tc, _sold) == (300, 180_000, 240) and _tc % _tu == 0
_wavg = _tc // _tu
_wclose, _wcogs = (_tu - _sold) * _wavg, _sold * _wavg
assert (_fcogs, _fclose, _mcogs, _mclose, _wavg, _wcogs, _wclose) == (138_000, 42_000, 141_000, 39_000, 600, 144_000, 36_000)
assert _fcogs + _fclose == _mcogs + _mclose == _wcogs + _wclose == _tc
_t_cmp = "\n".join([
    "                      FIFO   Moving avg  Period avg",
    f"Closing inventory {n(_fclose):>9}{n(_mclose):>12}{n(_wclose):>12}",
    f"Cost of goods sold{n(_fcogs):>9}{n(_mcogs):>12}{n(_wcogs):>12}",
    f"Goods available   {n(_tc):>9}{n(_tc):>12}{n(_tc):>12}",
])

LESSONS.append(lesson(
    module=M_ADJ, topic="Inventory valuation: FIFO and weighted average cost",
    title="Valuing inventory: FIFO and weighted average cost",
    slug="acc3-inventory-fifo-weighted-average", minutes=26,
    summary="Value closing inventory and the cost of goods sold with FIFO and with weighted average cost (after each receipt and after all entries) using a stock card.",
    objectives=[
        "Explain why the method of valuing inventory changes profit",
        "Prepare a stock card with the FIFO method",
        "Calculate weighted average cost after each receipt and after all entries",
        "Compare the closing inventory and cost of goods sold from the methods, and apply the lower of cost and net realisable value",
    ],
    key_concepts=["Inventory (stock)", "FIFO", "Weighted average cost", "Stock card", "Cost of goods sold", "Net realisable value"],
    blocks=[
        H("Why valuation matters"),
        T("A shop in Limbe buys the same carton of soap at different prices during the month: FCFA 500, then 600, then 700. "
          "At the end of the month some cartons are left. Which price do we use to value them? Different choices give a different "
          "closing inventory and so a different profit. The accounts must use one method consistently. All figures are **invented for practice**."),
        D("**Inventory** (also called **stock**) is the goods held for sale at the date of the statement. "
          "**Cost of goods sold** = opening inventory + purchases − closing inventory. A higher closing inventory gives a lower cost of goods sold and a higher profit.",
          title="Inventory and its effect on profit"),
        D("**FIFO** (first in, first out) assumes the oldest goods are sold first, so the closing inventory is valued at the most recent prices. "
          "**Weighted average cost** values goods at an average price. In the OHADA approach this is the **CMUP** (coût moyen unitaire pondéré); "
          "SYSCOHADA and IAS 2 both accept FIFO and weighted average cost. Textbooks differ on names: check yours.", title="Two methods"),
        KEY("Two ways to calculate the weighted average",
            "Both are used in examinations. Read the question for the method requested.",
            cards=[["After each receipt (moving average)", "After every purchase, divide the total value of the goods in stock by the number of units. Issue at that average until the next purchase."],
                   ["After all entries (period average)", "Wait until the end of the period. Divide the total cost of all opening stock and purchases by the total units. Value both the issues and the closing stock at this one average."]]),
        T("The Board's 2023 report says that many candidates could not calculate and apply the average cost for the period when asked to prepare a stock slip "
          "by the weighted average cost after all entries method. Practise both calculations."),
        EX("Worked example 1: the data",
           intro="The stock card of one product: opening inventory (1 Jan) 100 units at FCFA 500; 10 Jan bought 100 units at FCFA 600; 15 Jan sold 150 units; "
                 "20 Jan bought 100 units at FCFA 700; 28 Jan sold 90 units. Find the closing inventory by FIFO.",
           steps=[
               S("Units", text="Available 100 + 100 + 100 = 300. Sold 150 + 90 = 240. Closing = 60 units."),
               S("15 Jan issue", text="The oldest 100 units cost 500 each = 50 000. The other 50 come from the 600 layer = 30 000. Total 80 000."),
               S("28 Jan issue", text="The remaining 50 at 600 = 30 000, then 40 of the 700 layer = 28 000. Total 58 000."),
               S("Closing inventory", text="60 units remain at 700 each = 42 000. Cost of goods sold = 80 000 + 58 000 = 138 000."),
           ]),
        CODE("\n".join(_fl), "text", title="FIFO stock card (invented for practice)"),
        EX("Worked example 2: weighted average after each receipt",
           intro="Use the same data. After every purchase, find the average cost of the stock and issue at that cost.",
           steps=[
               S("After 10 Jan", text="Stock: 200 units worth 50 000 + 60 000 = 110 000. Average = 110 000 ÷ 200 = 550."),
               S("15 Jan issue", text="150 × 550 = 82 500. Balance: 50 units, 27 500."),
               S("After 20 Jan", text="Stock: 150 units worth 27 500 + 70 000 = 97 500. Average = 650."),
               S("28 Jan issue", text="90 × 650 = 58 500. Closing: 60 units, 39 000. Cost of goods sold = 82 500 + 58 500 = 141 000."),
           ]),
        CODE("\n".join(_ml), "text", title="Moving average stock card"),
        EX("Worked example 3: weighted average after all entries",
           intro="Use the same data. Calculate one average for the whole period and value the issues and the closing stock at it.",
           steps=[
               S("Total cost", text="50 000 + 60 000 + 70 000 = 180 000."),
               S("Total units", text="100 + 100 + 100 = 300."),
               S("Average", text="180 000 ÷ 300 = 600 per unit."),
               S("Values", text="Closing stock: 60 × 600 = 36 000. Cost of goods sold: 240 × 600 = 144 000. Check: 36 000 + 144 000 = 180 000."),
           ]),
        CODE(_t_cmp, "text", title="The three results side by side"),
        T("Prices were rising, so FIFO gave the highest closing inventory (42 000) and so the highest profit. In a period of falling prices "
          "the order would reverse. Each method is acceptable if it is used consistently and if it is stated in the accounts."),
        D("Inventory is valued at the **lower of cost and net realisable value (NRV)**. NRV = expected selling price − the costs needed to sell it. "
          "If damaged goods costing FCFA 20 000 can only be sold for FCFA 12 000 after costs of FCFA 2 000, the NRV is 10 000 and the inventory is valued at 10 000.",
          title="The prudence rule"),
        MISTAKE("Averaging the prices instead of weighting them",
                "The simple average of 500, 600 and 700 is 600 only by coincidence here. Always divide the **total cost** by the **total units**, so that a purchase of more units counts for more."),
        MISTAKE("Mixing the two weighted average methods",
                "After each receipt gives a new average each time. After all entries gives one average for the whole period. Do not use the opening average for later issues in the period method."),
        MISTAKE("Valuing the closing stock from the oldest layer in FIFO",
                "In FIFO the oldest goods are sold first, so the goods left are the **newest**."),
        QUIZ("Using FIFO, the data above give a closing inventory of FCFA 42 000. Which description of this figure is correct?",
             ["60 units at the latest price of FCFA 700", "60 units at the average price of FCFA 600", "40 units at 700 and 20 units at 600", "60 units at the oldest price of FCFA 500"], 0,
             "FIFO values the units left at the most recent purchase prices. Here all 60 come from the last purchase at 700: 60 × 700 = 42 000.",
             hint="Which goods are sold first under FIFO?",
             feedback=["", "600 is the period average, not FIFO.", "By 28 Jan the whole 600 layer was issued, so no units at 600 remain.", "The oldest goods are issued first."]),
        QUIZ("In a period when purchase prices are rising, FIFO compared with weighted average usually gives",
             ["A lower closing inventory", "A higher closing inventory and a higher profit", "The same profit", "A lower cost of goods sold but a lower profit"], 1,
             "FIFO leaves the newest, more expensive goods in stock, so the closing inventory is higher, cost of goods sold is lower and profit is higher.",
             feedback=["It gives a higher closing inventory when prices rise.", "", "The methods give different closing inventory, so profit differs.", "A lower cost of goods sold gives a higher profit, not a lower one."],
             title="Quick check 2"),
        TIP("Inventory costing is a Paper 2 topic named in the Board's 2023 report. Set out a stock card or schedule, check that closing inventory plus cost of goods sold equals the cost of goods available, and state the method you used.",
            title="Exam link"),
        PQ("Opening stock 40 units at FCFA 200, then a purchase of 60 units at FCFA 250. 70 units are sold. Using FIFO, find the closing inventory.",
           "Available 100 units; closing 30 units. The oldest 40 and 30 of the 250 layer are sold, so the 30 left are at 250: 7 500."),
        PQ("Using the data in the previous question, find the weighted average cost after all entries and the closing inventory.",
           "Total cost = 40 × 200 + 60 × 250 = 8 000 + 15 000 = 23 000; units 100; average 230. Closing stock = 30 × 230 = 6 900."),
        PQ("Stock is 50 units at FCFA 400 each. A purchase of 150 units at FCFA 600 follows. Find the weighted average cost after the purchase.",
           "Value = 20 000 + 90 000 = 110 000; units 200; average = 550."),
        PQ("Goods cost FCFA 30 000. They can be sold for FCFA 28 000 with selling costs of FCFA 3 000. At what value are they included in inventory?",
           "NRV = 28 000 − 3 000 = 25 000. Cost is 30 000, so the lower value, 25 000, is used."),
        SUM("Cost of goods sold = opening inventory + purchases − closing inventory; closing inventory affects profit.",
            "FIFO: the oldest goods are issued first, the closing stock is at the newest prices.",
            "Weighted average: total cost ÷ total units, either after each receipt or once after all entries.",
            "Value inventory at the lower of cost and net realisable value, and use the same method every year."),
    ]))

# ====================================================================== 6. OHADA income statement, lesson 1: the layout
# Mbarga Shop (invented for practice): used again in the balance sheet lesson
M = dict(sales=8_000_000, retin=100_000, oinv=600_000, purch=4_500_000, carr=150_000 - 50_000, retout=200_000, cinv=700_000,
         rent=400_000, wages=900_000, transp=150_000, dep=300_000, interest=50_000, comm=120_000)
M["netsales"] = M["sales"] - M["retin"]
M["cogs"] = M["oinv"] + M["purch"] + M["carr"] - M["retout"] - M["cinv"]
M["margin"] = M["netsales"] - M["cogs"]
M["ext"] = M["rent"] + M["transp"]
M["va"] = M["margin"] + M["comm"] - M["ext"]
M["ebe"] = M["va"] - M["wages"]
M["op"] = M["ebe"] - M["dep"]
M["net"] = M["op"] - M["interest"]
assert (M["netsales"], M["cogs"], M["margin"], M["va"], M["ebe"], M["op"], M["net"]) == \
       (7_900_000, 4_300_000, 3_600_000, 3_170_000, 2_270_000, 1_970_000, 1_920_000)
_t_m_is = "\n".join([
    "Mbarga Shop - income statement, year to 31 Dec",
    r("Sales of goods", M["sales"], w=32),
    r("Less returns inwards", -M["retin"], M["netsales"], w=32),
    r("Opening inventory", M["oinv"], w=32),
    r("Purchases + carriage inwards", M["purch"] + M["carr"], w=32),
    r("Less returns outwards", -M["retout"], w=32),
    r("Less closing inventory", -M["cinv"], w=32),
    r("Cost of goods sold", None, -M["cogs"], w=32),
    r("COMMERCIAL MARGIN", None, M["margin"], w=32),
    r("Commission received", None, M["comm"], w=32),
    r("External services (rent, transport)", None, -M["ext"], w=32),
    r("VALUE ADDED", None, M["va"], w=32),
    r("Personnel costs (wages)", None, -M["wages"], w=32),
    r("GROSS OPERATING SURPLUS", None, M["ebe"], w=32),
    r("Depreciation charge", None, -M["dep"], w=32),
    r("OPERATING RESULT", None, M["op"], w=32),
    r("Financial charges (interest)", None, -M["interest"], w=32),
    r("NET RESULT (profit)", None, M["net"], w=32),
])
_t_m_ias = "\n".join([
    "Same business, IAS/IFRS style (by function)",
    r("Revenue", None, M["netsales"], w=32),
    r("Cost of sales", None, -M["cogs"], w=32),
    r("Gross profit", None, M["margin"], w=32),
    r("Other income (commission)", None, M["comm"], w=32),
    r("Distribution and admin. costs", None, -(M["ext"] + M["wages"] + M["dep"]), w=32),
    r("Finance cost", None, -M["interest"], w=32),
    r("Profit for the year", None, M["net"], w=32),
])
assert M["margin"] + M["comm"] - (M["ext"] + M["wages"] + M["dep"]) - M["interest"] == M["net"]

LESSONS.append(lesson(
    module=M_FIN, topic="The OHADA income statement",
    title="The OHADA income statement: the layout and the cascade of balances",
    slug="acc3-ohada-income-statement-layout", minutes=26,
    summary="Understand how the OHADA income statement (compte de résultat) builds the net result through commercial margin, value added, gross operating surplus and operating result, and how it differs from the IAS/IFRS layout.",
    objectives=[
        "State the purpose of the income statement and the idea of listing expenses by nature",
        "Calculate cost of goods sold, commercial margin, value added, gross operating surplus, operating result and net result",
        "Arrange a simple income statement in the OHADA order",
        "Explain how the IAS/IFRS income statement (gross profit, expenses by function) gives the same profit",
    ],
    key_concepts=["Income statement (compte de résultat)", "Commercial margin", "Value added", "Gross operating surplus", "Operating result", "Net result"],
    blocks=[
        H("What the income statement shows"),
        T("Mbarga runs a shop in Ebolowa. At the end of the year she wants to know one thing: did the business make a profit, and where did it come from? "
          "The **income statement** answers this by comparing the incomes of the year with the expenses of the same year. "
          "In the OHADA approach it is called the **compte de résultat**. All figures are **invented for practice**."),
        D("The **income statement** lists the incomes (products) and expenses (charges) of a period and gives the **net result**: a profit if incomes are larger, a loss if expenses are larger.",
          title="Income statement"),
        D("The OHADA statement lists expenses **by nature**: purchases, services, wages, depreciation, interest, each on its own line. "
          "It shows the result in stages (balances) so the reader can see where profit is created. The IAS/IFRS approach usually groups expenses **by function** "
          "(cost of sales, distribution, administration) or by nature. Both approaches end with the same profit.", title="By nature and by function"),
        IMG("f5acc3-income-statement-cascade.svg",
            alt="Five boxes from top to bottom: commercial margin, value added, operating profit before depreciation, operating result, net result.",
            caption="Figure 1. The cascade of balances in a simplified OHADA income statement."),
        KEY("The balances, step by step",
            "Each balance equals the one above plus or minus the next group of lines. The layout below is a simplified school layout. Check your textbook for the exact line names your class uses.",
            cards=[["Commercial margin", "Net sales of goods − cost of goods sold. This is the same figure as gross profit."],
                   ["Value added", "Commercial margin + other operating income − external services (rent, transport, insurance, electricity)."],
                   ["Gross operating surplus (EBE)", "Value added − taxes and duties − personnel costs."],
                   ["Operating result", "Gross operating surplus − depreciation and provisions − losses on receivables."],
                   ["Net result", "Operating result ± financial result (interest) ± exceptional items (HAO) − income tax if any."]]),
        D("**Cost of goods sold** = opening inventory + purchases + carriage inwards − returns outwards − closing inventory. "
          "**Net sales** = sales − returns inwards. **Commercial margin** = net sales − cost of goods sold.", title="The first stage"),
        EX("Worked example 1: the commercial margin",
           intro="Sales are FCFA 8 000 000 and returns inwards FCFA 100 000. Opening inventory FCFA 600 000, purchases FCFA 4 500 000, carriage inwards FCFA 100 000, "
                 "returns outwards FCFA 200 000, closing inventory FCFA 700 000. Find the commercial margin.",
           steps=[
               S("Net sales", text="8 000 000 − 100 000 = 7 900 000."),
               S("Cost of goods sold", text="600 000 + 4 500 000 + 100 000 − 200 000 − 700 000 = 4 300 000."),
               S("Commercial margin", text="7 900 000 − 4 300 000 = 3 600 000."),
           ]),
        EX("Worked example 2: the whole statement",
           intro="Add: commission received FCFA 120 000; rent FCFA 400 000; transport FCFA 150 000; wages FCFA 900 000; depreciation FCFA 300 000; "
                 "interest paid FCFA 50 000. Prepare the income statement and find the net result.",
           steps=[
               S("Value added", text="3 600 000 + 120 000 − (400 000 + 150 000) = 3 170 000."),
               S("Gross operating surplus", text="3 170 000 − 900 000 = 2 270 000."),
               S("Operating result", text="2 270 000 − 300 000 = 1 970 000."),
               S("Net result", text="1 970 000 − 50 000 = 1 920 000 profit."),
           ]),
        CODE(_t_m_is, "text", title="OHADA-style income statement (simplified)"),
        T("Now see the same business in the IAS/IFRS style. The profit for the year is the same: only the grouping of the costs is different. "
          "Note that the Board's 2023 report says that in the question on final accounts of sole traders only the income statement was required; so practise this statement by itself."),
        CODE(_t_m_ias, "text", title="IAS/IFRS-style income statement (by function)"),
        MISTAKE("Putting returns on the wrong line",
                "Returns inwards reduce sales. Returns outwards reduce purchases. Do not subtract returns inwards from purchases."),
        MISTAKE("Leaving carriage inwards out of cost of goods sold",
                "Carriage inwards is part of the cost of getting the goods ready for sale. Carriage outwards (delivery to customers) is a selling expense."),
        MISTAKE("Subtracting depreciation before value added",
                "Depreciation is deducted after the gross operating surplus. Value added and gross operating surplus are before depreciation."),
        QUIZ("Net sales are FCFA 5 000 000 and cost of goods sold FCFA 3 100 000. External services are FCFA 600 000. There is no other income. The value added is",
             ["FCFA 1 300 000", "FCFA 1 900 000", "FCFA 2 500 000", "FCFA 4 400 000"], 0,
             "Commercial margin = 5 000 000 − 3 100 000 = 1 900 000. Value added = 1 900 000 − 600 000 = 1 300 000.",
             hint="Find the commercial margin first.",
             feedback=["", "That is the commercial margin, before external services.", "That subtracts only cost of goods sold from sales and adds the services.", "That subtracts external services from net sales only."]),
        QUIZ("Which item is deducted after the gross operating surplus?",
             ["Wages", "Rent", "Depreciation", "Returns inwards"], 2,
             "Depreciation and provisions come after the gross operating surplus; wages come before it.",
             feedback=["Wages (personnel costs) are deducted to reach the gross operating surplus.", "Rent is an external service deducted for value added.", "", "Returns inwards reduce sales at the start."],
             title="Quick check 2"),
        TIP("The Board's 2023 report lists presentation of final accounts of sole traders as an examined topic, and Paper 1 may ask about balances such as gross profit and net profit. Learn the order of the balances and write the name of each total.",
            title="Exam link"),
        PQ("Sales FCFA 3 000 000, returns inwards FCFA 50 000, cost of goods sold FCFA 1 800 000. Find the commercial margin.",
           "Net sales = 2 950 000. Margin = 2 950 000 − 1 800 000 = 1 150 000."),
        PQ("Commercial margin is FCFA 1 150 000, other income FCFA 30 000, external services FCFA 280 000, personnel costs FCFA 400 000. Find value added and gross operating surplus.",
           "Value added = 1 150 000 + 30 000 − 280 000 = 900 000. Gross operating surplus = 900 000 − 400 000 = 500 000."),
        PQ("Gross operating surplus is FCFA 500 000, depreciation FCFA 120 000, interest paid FCFA 20 000. Find the net result.",
           "Operating result = 380 000. Net result = 380 000 − 20 000 = 360 000 profit."),
        PQ("A business has opening inventory FCFA 200 000, purchases FCFA 900 000, carriage inwards FCFA 20 000, returns outwards FCFA 30 000 and closing inventory FCFA 250 000. Find the cost of goods sold.",
           "200 000 + 900 000 + 20 000 − 30 000 − 250 000 = 840 000."),
        SUM("The income statement gives the net result for a period by comparing incomes and expenses of the same period.",
            "OHADA layout lists expenses by nature and shows the result in stages: commercial margin, value added, gross operating surplus, operating result, net result.",
            "Cost of goods sold = opening inventory + purchases + carriage inwards − returns outwards − closing inventory.",
            "The IAS/IFRS layout (gross profit, expenses by function) gives the same profit."),
    ]))

# ====================================================================== 7. Income statement, lesson 2: from trial balance with adjustments
# Ngwa Traders (invented for practice): reused in the balance sheet lesson
NT_DR = [("Land and buildings", 12_000_000), ("Equipment (cost)", 3_000_000), ("Vehicles (cost)", 4_000_000),
         ("Opening inventory", 1_200_000), ("Purchases", 9_600_000), ("Carriage inwards", 150_000),
         ("Returns inwards", 250_000), ("Wages", 1_800_000), ("Rent", 600_000), ("Electricity", 210_000),
         ("Insurance", 240_000), ("Transport (distribution)", 320_000), ("Taxes and duties", 150_000),
         ("Interest paid", 120_000), ("Trade receivables", 2_400_000), ("Bank", 1_500_000), ("Cash", 200_000),
         ("Drawings", 900_000)]
NT_CR = [("Sales", 16_000_000), ("Returns outwards", 300_000), ("Trade payables", 1_700_000), ("Loan (long term)", 2_000_000),
         ("Provision for doubtful debts", 80_000), ("Acc. depreciation: equipment", 600_000),
         ("Acc. depreciation: vehicles", 1_200_000), ("Commission received", 150_000), ("Capital (1 Jan)", 16_610_000)]
assert sum(a for _, a in NT_DR) == sum(a for _, a in NT_CR)
NT = dict(NT_DR + NT_CR)
NT_TB_TOTAL = sum(a for _, a in NT_DR)
_t_tb = "\n".join(
    ["Trial balance, 31 December", f"{'Account':<28}{'Debit':>12}{'Credit':>12}"]
    + [f"{k:<28}{n(v):>12}{'':>12}" for k, v in NT_DR]
    + [f"{k:<28}{'':>12}{n(v):>12}" for k, v in NT_CR]
    + [f"{'TOTAL':<28}{n(NT_TB_TOTAL):>12}{n(NT_TB_TOTAL):>12}"])
# adjustments
NA = dict(cinv=1_500_000, dep_eq=NT["Equipment (cost)"] * 10 // 100,
          dep_veh=(NT["Vehicles (cost)"] - NT["Acc. depreciation: vehicles"]) * 25 // 100,
          baddebt=40_000, elec_acc=30_000, ins_pre=60_000, comm_acc=20_000)
NA["recv_after"] = NT["Trade receivables"] - NA["baddebt"]
NA["prov_new"] = NA["recv_after"] * 5 // 100
NA["prov_inc"] = NA["prov_new"] - NT["Provision for doubtful debts"]
assert (NA["dep_eq"], NA["dep_veh"], NA["recv_after"], NA["prov_new"], NA["prov_inc"]) == (300_000, 700_000, 2_360_000, 118_000, 38_000)
assert (NT["Trade receivables"] - NA["baddebt"]) * 5 % 100 == 0
NI = {}
NI["netsales"] = NT["Sales"] - NT["Returns inwards"]
NI["purch_net"] = NT["Purchases"] + NT["Carriage inwards"] - NT["Returns outwards"]
NI["cogs"] = NT["Opening inventory"] + NI["purch_net"] - NA["cinv"]
NI["margin"] = NI["netsales"] - NI["cogs"]
NI["comm"] = NT["Commission received"] + NA["comm_acc"]
NI["rent"] = NT["Rent"]
NI["elec"] = NT["Electricity"] + NA["elec_acc"]
NI["ins"] = NT["Insurance"] - NA["ins_pre"]
NI["transp"] = NT["Transport (distribution)"]
NI["ext"] = NI["rent"] + NI["elec"] + NI["ins"] + NI["transp"]
NI["va"] = NI["margin"] + NI["comm"] - NI["ext"]
NI["ebe"] = NI["va"] - NT["Taxes and duties"] - NT["Wages"]
NI["dep"] = NA["dep_eq"] + NA["dep_veh"]
NI["loss"] = NA["baddebt"] + NA["prov_inc"]
NI["op"] = NI["ebe"] - NI["dep"] - NI["loss"]
NI["fin"] = -NT["Interest paid"]
NI["net"] = NI["op"] + NI["fin"]
assert (NI["netsales"], NI["purch_net"], NI["cogs"], NI["margin"], NI["comm"], NI["elec"], NI["ins"], NI["ext"], NI["va"], NI["ebe"],
        NI["dep"], NI["loss"], NI["op"], NI["net"]) == (15_750_000, 9_450_000, 9_150_000, 6_600_000, 170_000, 240_000, 180_000,
                                                      1_340_000, 5_430_000, 3_480_000, 1_000_000, 78_000, 2_402_000, 2_282_000)
_t_adj = "\n".join([
    "Workings for the adjustments",
    "1 Closing inventory ........ 1 500 000",
    "2 Equipment: 10% x 3 000 000 .... 300 000",
    "  Vehicles: 25% of NBV",
    "   (4 000 000 - 1 200 000)=2 800 000",
    "   25% x 2 800 000 ......... 700 000",
    "3 Bad debt to write off ...... 40 000",
    "  Receivables left: 2 360 000",
    "  Provision 5% = 118 000; old 80 000",
    "  Increase to charge ........ 38 000",
    "4 Electricity owing ......... 30 000",
    "5 Insurance prepaid ......... 60 000",
    "6 Commission earned, unpaid .. 20 000",
])
_t_nis = "\n".join([
    "Ngwa Traders - income statement, year to 31 Dec",
    r("Sales of goods", NT["Sales"], w=34),
    r("Less returns inwards", -NT["Returns inwards"], NI["netsales"], w=34),
    r("Opening inventory", NT["Opening inventory"], w=34),
    r("Purchases + carriage in", NT["Purchases"] + NT["Carriage inwards"], w=34),
    r("Less returns outwards", -NT["Returns outwards"], w=34),
    r("Less closing inventory", -NA["cinv"], w=34),
    r("Cost of goods sold", None, -NI["cogs"], w=34),
    r("COMMERCIAL MARGIN", None, NI["margin"], w=34),
    r("Commission received (150+20)", None, NI["comm"], w=34),
    r("Rent", -NI["rent"], w=34),
    r("Electricity (210 000 + 30 000)", -NI["elec"], w=34),
    r("Insurance (240 000 - 60 000)", -NI["ins"], w=34),
    r("Transport", -NI["transp"], w=34),
    r("External services", None, -NI["ext"], w=34),
    r("VALUE ADDED", None, NI["va"], w=34),
    r("Taxes and duties", None, -NT["Taxes and duties"], w=34),
    r("Wages", None, -NT["Wages"], w=34),
    r("GROSS OPERATING SURPLUS", None, NI["ebe"], w=34),
    r("Depreciation (300 000+700 000)", None, -NI["dep"], w=34),
    r("Bad debts + provision increase", None, -NI["loss"], w=34),
    r("OPERATING RESULT", None, NI["op"], w=34),
    r("Interest paid", None, NI["fin"], w=34),
    r("NET RESULT (profit)", None, NI["net"], w=34),
])
_ias_exp = NT["Wages"] + NI["rent"] + NI["elec"] + NI["ins"] + NI["transp"] + NT["Taxes and duties"] + NI["dep"] + NI["loss"] + NT["Interest paid"]
assert NI["margin"] + NI["comm"] - _ias_exp == NI["net"] and _ias_exp == 4_488_000

LESSONS.append(lesson(
    module=M_FIN, topic="The OHADA income statement",
    title="Preparing the income statement from a trial balance with adjustments",
    slug="acc3-income-statement-from-trial-balance", minutes=28,
    summary="Work from a trial balance and a list of adjustments (inventory, depreciation, bad debts and provision, accruals and prepayments) to the net result, with a schedule of workings.",
    objectives=[
        "Read a trial balance and pick out the income statement items",
        "Apply closing inventory, depreciation, bad debts, provision, accruals and prepayments to the right lines",
        "Prepare a complete income statement and check that it ties back to the trial balance",
        "Show how the IAS/IFRS layout gives the same profit",
    ],
    key_concepts=["Trial balance", "Adjustments", "Workings schedule", "Net result", "Matching"],
    blocks=[
        H("The method"),
        T("Ngwa Traders is a sole trader's business in Kumba. At the year end the accountant has a trial balance and a list of notes. "
          "The steps are always the same. All figures are **invented for practice**."),
        KEY("Five steps for the income statement",
            "Work in order. Do not try to do everything at once.",
            cards=[["1. Sort", "Mark each trial-balance item as income statement or balance sheet."],
                   ["2. Workings", "Calculate each adjustment in a small schedule."],
                   ["3. Adjust", "Put the adjusted figure on each income-statement line."],
                   ["4. Balances", "Margin, value added, gross operating surplus, operating result, net result."],
                   ["5. Check", "Re-add the totals and keep the net result for the capital account and the balance sheet."]]),
        CODE(_t_tb, "text", title="Trial balance (invented for practice)"),
        T("The notes at the year end are: (1) closing inventory FCFA 1 500 000; (2) depreciate equipment at 10% of cost (straight-line) and vehicles at 25% reducing balance; "
          "(3) write off a bad debt of FCFA 40 000, then keep a provision of 5% of the remaining receivables; (4) electricity of FCFA 30 000 is owing; "
          "(5) FCFA 60 000 of insurance is prepaid; (6) commission of FCFA 20 000 has been earned but not yet received."),
        EX("Worked example 1: the workings",
           intro="Calculate each adjustment.",
           steps=[
               S("Depreciation", text="Equipment 10% × 3 000 000 = 300 000. Vehicles: NBV = 4 000 000 − 1 200 000 = 2 800 000; 25% × 2 800 000 = 700 000. Total 1 000 000."),
               S("Bad debt and provision", text="Receivables after write-off = 2 400 000 − 40 000 = 2 360 000. 5% = 118 000. Old provision 80 000, so charge 38 000. Total charge for doubtful debts = 40 000 + 38 000 = 78 000."),
               S("Accruals and prepayments", text="Electricity 210 000 + 30 000 = 240 000. Insurance 240 000 − 60 000 = 180 000. Commission 150 000 + 20 000 = 170 000."),
           ]),
        CODE(_t_adj, "text", title="Schedule of workings"),
        EX("Worked example 2: cost of goods sold and the margin",
           intro="Use the trial balance and the closing inventory.",
           steps=[
               S("Net sales", text="16 000 000 − 250 000 = 15 750 000."),
               S("Purchases", text="9 600 000 + 150 000 carriage inwards − 300 000 returns outwards = 9 450 000."),
               S("Cost of goods sold", text="1 200 000 + 9 450 000 − 1 500 000 = 9 150 000."),
               S("Commercial margin", text="15 750 000 − 9 150 000 = 6 600 000."),
           ]),
        EX("Worked example 3: down to the net result",
           intro="Continue to the net result.",
           steps=[
               S("Value added", text="6 600 000 + 170 000 − (600 000 + 240 000 + 180 000 + 320 000 = 1 340 000) = 5 430 000."),
               S("Gross operating surplus", text="5 430 000 − 150 000 taxes − 1 800 000 wages = 3 480 000."),
               S("Operating result", text="3 480 000 − 1 000 000 depreciation − 78 000 doubtful debts = 2 402 000."),
               S("Net result", text="2 402 000 − 120 000 interest = 2 282 000 profit."),
           ]),
        CODE(_t_nis, "text", title="Income statement of Ngwa Traders"),
        T("In the IAS/IFRS style the same data give: revenue 15 750 000; cost of sales 9 150 000; gross profit 6 600 000; other income 170 000; "
          "operating and finance expenses 4 488 000 (wages 1 800 000, rent 600 000, electricity 240 000, insurance 180 000, transport 320 000, taxes 150 000, "
          "depreciation 1 000 000, bad debts and provision 78 000, interest 120 000); profit for the year 2 282 000. "
          "The profit is the same. Only the grouping of lines changes."),
        MISTAKE("Using unadjusted figures",
                "The trial balance electricity is 210 000, but the expense for the year is 240 000. Always use the adjusted figure."),
        MISTAKE("Charging the whole provision",
                "Only the **increase** in the provision (38 000) is an expense, not the full 118 000."),
        MISTAKE("Putting drawings or capital in the income statement",
                "Drawings are the owner's withdrawals. They reduce capital and are not an expense. Capital is not an income either."),
        QUIZ("In the trial balance, insurance is FCFA 240 000 and FCFA 60 000 of it is prepaid. The insurance expense in the income statement is",
             ["FCFA 300 000", "FCFA 240 000", "FCFA 180 000", "FCFA 60 000"], 2,
             "The prepayment belongs to next year, so 240 000 − 60 000 = 180 000.",
             hint="Which part of the payment belongs to this year?",
             feedback=["That adds the prepayment.", "That ignores the adjustment.", "", "That is the prepayment, not the expense."]),
        QUIZ("The gross operating surplus is FCFA 3 480 000, depreciation FCFA 1 000 000, doubtful debts FCFA 78 000 and interest FCFA 120 000. The net result is",
             ["FCFA 2 282 000", "FCFA 2 402 000", "FCFA 2 480 000", "FCFA 3 360 000"], 0,
             "3 480 000 − 1 000 000 − 78 000 = 2 402 000 operating result; minus interest 120 000 = 2 282 000.",
             feedback=["", "That is the operating result before interest.", "That ignores the doubtful debts and interest.", "That deducts only interest."],
             title="Quick check 2"),
        TIP("Presenting final accounts of sole traders was examined in Paper 2 in the Board's 2023 report (the income statement was asked for). Practise the full sequence from a trial balance. Show every working so that a mistake in one figure does not lose all the marks.",
            title="Exam link"),
        PQ("Wages in the trial balance are FCFA 900 000 and FCFA 60 000 of wages are owing. Find the wages expense.",
           "900 000 + 60 000 = 960 000."),
        PQ("Vehicles cost FCFA 2 000 000 with accumulated depreciation FCFA 500 000. Depreciation is 20% reducing balance. Find the charge.",
           "NBV = 1 500 000. Charge = 20% × 1 500 000 = 300 000."),
        PQ("Receivables are FCFA 1 000 000. A bad debt of FCFA 50 000 is written off, and a 4% provision is kept. The old provision was FCFA 30 000. Find the total charge for doubtful debts.",
           "Provision = 4% × 950 000 = 38 000. Increase = 8 000. Charge = 50 000 + 8 000 = 58 000."),
        PQ("Net sales FCFA 2 000 000, cost of goods sold FCFA 1 200 000, other expenses FCFA 500 000. Find the net result.",
           "2 000 000 − 1 200 000 − 500 000 = 300 000 profit."),
        SUM("Sort the trial balance, do the workings, adjust each line, calculate the balances and check.",
            "Use adjusted figures: accruals add to the expense, prepayments subtract, only the change in the provision is charged.",
            "Drawings and capital are not income statement items.",
            "The IAS/IFRS layout groups the same costs differently and gives the same profit."),
    ]))

# ====================================================================== 8. OHADA balance sheet, lesson 1: layout
MB_FIX = [("Equipment", 2_000_000, 800_000), ("Vehicles", 3_000_000, 1_000_000)]
MB_CUR = [("Inventory", 700_000), ("Trade receivables", 900_000), ("Bank", 600_000), ("Cash", 100_000)]
MB_FIXN = sum(c - d for _, c, d in MB_FIX)
MB_CURN = sum(v for _, v in MB_CUR)
MB_TA = MB_FIXN + MB_CURN
MB_EQ = 2_400_000 + M["net"] - 720_000
MB_TL = MB_EQ + 1_000_000 + 800_000 + 100_000
assert (MB_FIXN, MB_CURN, MB_TA, MB_EQ) == (3_200_000, 2_300_000, 5_500_000, 3_600_000) and MB_TL == MB_TA
_t_mb_a = "\n".join([
    "Mbarga Shop - ASSETS at 31 Dec",
    f"{'':<20}{'Gross':>10}{'Deprec.':>10}{'Net':>10}",
    "Fixed assets",
    *[f"  {nm:<18}{n(c):>10}{n(d):>10}{n(c - d):>10}" for nm, c, d in MB_FIX],
    f"{'Total fixed assets':<20}{n(sum(c for _, c, _d in MB_FIX)):>10}{n(sum(d for _, _c, d in MB_FIX)):>10}{n(MB_FIXN):>10}",
    "Current assets",
    *[f"  {nm:<18}{'':>20}{n(v):>10}" for nm, v in MB_CUR],
    f"{'Total current assets':<40}{n(MB_CURN):>10}",
    f"{'TOTAL ASSETS':<40}{n(MB_TA):>10}",
])
_t_mb_l = "\n".join([
    "Mbarga Shop - EQUITY AND LIABILITIES",
    "Equity",
    r("  Capital at 1 January", 2_400_000, w=36),
    r("  Net result for the year", M["net"], w=36),
    r("  Less drawings", -720_000, w=36),
    r("Total equity", None, MB_EQ, w=36),
    r("Long-term loan", None, 1_000_000, w=36),
    "Current liabilities",
    r("  Trade payables", 800_000, w=36),
    r("  Accrued expenses", 100_000, w=36),
    r("Total current liabilities", None, 900_000, w=36),
    r("TOTAL EQUITY AND LIABILITIES", None, MB_TL, w=36),
])
_t_mb_ias = "\n".join([
    "IAS/IFRS wording (statement of financial position)",
    "Non-current assets 3 200 000",
    "Current assets 2 300 000",
    "  = Total assets 5 500 000",
    "Equity 3 600 000",
    "Non-current liabilities 1 000 000",
    "Current liabilities 900 000",
    "  = Total equity and liabilities 5 500 000",
])

LESSONS.append(lesson(
    module=M_FIN, topic="The OHADA balance sheet",
    title="The OHADA balance sheet: layout, gross, depreciation and net",
    slug="acc3-ohada-balance-sheet-layout", minutes=26,
    summary="Arrange assets (fixed and current, with gross, depreciation and net columns) and equity and liabilities in the OHADA balance sheet, and see why the two totals must agree.",
    objectives=[
        "State what a balance sheet shows and why both sides total the same",
        "Classify an item as a fixed asset, current asset, equity, long-term liability or current liability",
        "Show fixed assets at gross, accumulated depreciation and net amount",
        "Calculate closing equity from capital, net result and drawings and name the IAS/IFRS equivalents",
    ],
    key_concepts=["Balance sheet (bilan)", "Fixed assets", "Current assets", "Equity", "Liabilities", "Net book value"],
    blocks=[
        H("A snapshot of the business"),
        T("The income statement tells the story of a year. The **balance sheet** (**bilan** in the OHADA approach) is a photograph taken on the last day of the year. "
          "It lists what the business **owns** (assets) and where the money to own them came from: the owner (equity) and other people (liabilities). "
          "We continue with Mbarga's shop in Ebolowa. All figures are **invented for practice**."),
        IMG("f5acc3-balance-sheet-layout.svg",
            alt="Two blocks side by side: assets on the left, equity and liabilities on the right, with equal totals.",
            caption="Figure 1. Both sides of the balance sheet add up to the same total."),
        D("The accounting equation is **Assets = Equity + Liabilities**. A balance sheet is this equation written out in detail at one date.", title="Why it balances"),
        D("**Fixed assets** (actif immobilisé) are held for long-term use: land, buildings, equipment, vehicles. "
          "**Current assets** (actif circulant) are used up or turned into cash within a year: inventory, receivables, and cash and bank (treasury). "
          "In IAS/IFRS wording these are non-current assets and current assets.", title="Assets"),
        D("**Equity** (capitaux propres) is what belongs to the owner: capital plus the net result less drawings. "
          "**Long-term liabilities** (dettes financières) are loans repayable after more than a year. "
          "**Current liabilities** (passif circulant) are due within a year: trade payables, accrued expenses. A bank overdraft is a liability.", title="Equity and liabilities"),
        KEY("Order of presentation",
            "Layouts differ between textbooks. A common school order follows.",
            cards=[["Assets", "Fixed assets first (gross, depreciation, net), then current assets: inventory, receivables, cash and bank."],
                   ["Equity and liabilities", "Equity first, then long-term liabilities, then current liabilities."]]),
        EX("Worked example 1: classify the items",
           intro="Classify: vehicles, trade payables, inventory, bank loan repayable in five years, capital, trade receivables, accrued expenses.",
           steps=[
               S("Fixed asset", text="Vehicles."),
               S("Current assets", text="Inventory, trade receivables."),
               S("Equity", text="Capital."),
               S("Long-term liability", text="Bank loan repayable in five years."),
               S("Current liabilities", text="Trade payables, accrued expenses."),
           ]),
        EX("Worked example 2: closing equity",
           intro="Capital at 1 January was FCFA 2 400 000. The net result for the year was FCFA 1 920 000 (from the previous lesson) and drawings were FCFA 720 000. Find the closing equity.",
           steps=[
               S("Add the result", text="2 400 000 + 1 920 000 = 4 320 000."),
               S("Subtract drawings", text="4 320 000 − 720 000 = 3 600 000."),
           ]),
        EX("Worked example 3: build the balance sheet",
           intro="Equipment cost FCFA 2 000 000 (depreciation 800 000); vehicles cost FCFA 3 000 000 (depreciation 1 000 000); inventory FCFA 700 000; receivables FCFA 900 000; "
                 "bank FCFA 600 000; cash FCFA 100 000; loan FCFA 1 000 000; trade payables FCFA 800 000; accrued expenses FCFA 100 000. Prepare the balance sheet.",
           steps=[
               S("Fixed assets (net)", text="Equipment 1 200 000 + vehicles 2 000 000 = 3 200 000."),
               S("Current assets", text="700 000 + 900 000 + 600 000 + 100 000 = 2 300 000. Total assets = 5 500 000."),
               S("Equity and liabilities", text="Equity 3 600 000 + loan 1 000 000 + current liabilities 900 000 = 5 500 000."),
               S("Check", text="Assets 5 500 000 = equity and liabilities 5 500 000."),
           ]),
        CODE(_t_mb_a, "text", title="Assets (invented for practice)"),
        CODE(_t_mb_l, "text", title="Equity and liabilities"),
        CODE(_t_mb_ias, "text", title="Same totals in IAS/IFRS wording"),
        MISTAKE("Showing fixed assets at cost only",
                "The balance sheet shows the net book value: cost minus accumulated depreciation. Show gross, depreciation and net so that readers see the age of the assets."),
        MISTAKE("Treating drawings as an expense or ignoring them",
                "Drawings reduce the owner's equity. They are not in the income statement. Subtract them from equity."),
        MISTAKE("Putting a loan repayable in five years under current liabilities",
                "Only amounts due within a year are current liabilities. A five-year loan is a long-term liability."),
        QUIZ("Which of these is a current asset?",
             ["Delivery van", "Trade receivables", "Capital", "Bank loan"], 1,
             "Trade receivables will turn into cash within a year, so they are current assets.",
             hint="Which item will turn into cash within a year?",
             feedback=["A van is used for several years: a fixed asset.", "", "Capital is the owner's claim: equity.", "A loan is owed to the bank: a liability."]),
        QUIZ("Capital at 1 January FCFA 1 000 000, net profit FCFA 400 000, drawings FCFA 150 000. Closing equity is",
             ["FCFA 1 550 000", "FCFA 1 250 000", "FCFA 1 400 000", "FCFA 850 000"], 1,
             "1 000 000 + 400 000 - 150 000 = 1 250 000.",
             feedback=["That adds the drawings instead of subtracting them.", "", "That forgets the drawings.", "That subtracts the profit instead of adding it."],
             title="Quick check 2"),
        TIP("Balance sheet classification is a typical Paper 1 multiple-choice area, and Paper 2 final-accounts questions expect a clear layout. Always show the totals and check that they agree.",
            title="Exam link"),
        PQ("Machinery cost FCFA 900 000 with accumulated depreciation FCFA 300 000. Show it on the balance sheet.",
           "Gross 900 000, depreciation 300 000, net 600 000."),
        PQ("Assets total FCFA 4 200 000. Liabilities are FCFA 1 500 000. Find the equity.",
           "4 200 000 − 1 500 000 = 2 700 000."),
        PQ("Capital is FCFA 3 000 000, profit FCFA 500 000, drawings FCFA 200 000. Find the closing equity.",
           "3 000 000 + 500 000 − 200 000 = 3 300 000."),
        PQ("Name three current liabilities.",
           "Examples: trade payables, accrued expenses, bank overdraft (also taxes owing and income received in advance)."),
        SUM("The balance sheet is a snapshot: assets = equity + liabilities.",
            "Fixed assets are shown at gross cost, accumulated depreciation and net book value; current assets include inventory, receivables and cash and bank.",
            "Closing equity = opening capital + net result − drawings.",
            "Long-term liabilities fall due after more than a year; current liabilities within a year."),
    ]))

# ====================================================================== 9. Balance sheet, lesson 2: from the trial balance
NB = {}
NB["land"] = NT["Land and buildings"]
NB["eq_dep"] = NT["Acc. depreciation: equipment"] + NA["dep_eq"]
NB["veh_dep"] = NT["Acc. depreciation: vehicles"] + NA["dep_veh"]
NB["eq_net"] = NT["Equipment (cost)"] - NB["eq_dep"]
NB["veh_net"] = NT["Vehicles (cost)"] - NB["veh_dep"]
NB["fix"] = NB["land"] + NB["eq_net"] + NB["veh_net"]
NB["recv_net"] = NA["recv_after"] - NA["prov_new"]
NB["cur"] = NA["cinv"] + NB["recv_net"] + NA["ins_pre"] + NA["comm_acc"] + NT["Bank"] + NT["Cash"]
NB["ta"] = NB["fix"] + NB["cur"]
NB["eqty"] = NT["Capital (1 Jan)"] + NI["net"] - NT["Drawings"]
NB["cl"] = NT["Trade payables"] + NA["elec_acc"]
NB["tl"] = NB["eqty"] + NT["Loan (long term)"] + NB["cl"]
assert (NB["eq_dep"], NB["veh_dep"], NB["eq_net"], NB["veh_net"], NB["fix"], NB["recv_net"], NB["cur"], NB["ta"], NB["eqty"], NB["cl"], NB["tl"]) == \
       (900_000, 1_900_000, 2_100_000, 2_100_000, 16_200_000, 2_242_000, 5_522_000, 21_722_000, 17_992_000, 1_730_000, 21_722_000)
assert NB["ta"] == NB["tl"]
_t_nb_a = "\n".join([
    "Ngwa Traders - ASSETS at 31 Dec",
    f"{'':<19}{'Gross':>12}{'Deprec.':>11}{'Net':>11}",
    f"{'Land and buildings':<19}{n(NB['land']):>12}{'0':>11}{n(NB['land']):>11}",
    f"{'Equipment':<19}{n(NT['Equipment (cost)']):>12}{n(NB['eq_dep']):>11}{n(NB['eq_net']):>11}",
    f"{'Vehicles':<19}{n(NT['Vehicles (cost)']):>12}{n(NB['veh_dep']):>11}{n(NB['veh_net']):>11}",
    f"{'FIXED ASSETS':<42}{n(NB['fix']):>11}",
    f"{'Inventory':<42}{n(NA['cinv']):>11}",
    f"{'Trade receivables (net)':<42}{n(NB['recv_net']):>11}",
    f"{'Prepaid insurance':<42}{n(NA['ins_pre']):>11}",
    f"{'Accrued commission':<42}{n(NA['comm_acc']):>11}",
    f"{'Bank':<42}{n(NT['Bank']):>11}",
    f"{'Cash':<42}{n(NT['Cash']):>11}",
    f"{'CURRENT ASSETS':<42}{n(NB['cur']):>11}",
    f"{'TOTAL ASSETS':<42}{n(NB['ta']):>11}",
])
_t_nb_l = "\n".join([
    "Ngwa Traders - EQUITY AND LIABILITIES",
    r("Capital at 1 January", NT["Capital (1 Jan)"], w=34),
    r("Add net result", NI["net"], w=34),
    r("Less drawings", -NT["Drawings"], w=34),
    r("EQUITY", None, NB["eqty"], w=34),
    r("Long-term loan", None, NT["Loan (long term)"], w=34),
    r("Trade payables", NT["Trade payables"], w=34),
    r("Accrued electricity", NA["elec_acc"], w=34),
    r("CURRENT LIABILITIES", None, NB["cl"], w=34),
    r("TOTAL EQUITY AND LIABILITIES", None, NB["tl"], w=34),
])
_led_cap = ledger("Capital account (year)",
                  [("Drawings", NT["Drawings"]), ("Balance c/d", NB["eqty"])],
                  [("Balance b/d", NT["Capital (1 Jan)"]), ("Net result (income statement)", NI["net"])])
_t_rec = "\n".join([
    "Receivables: 2 400 000 - 40 000 = 2 360 000",
    "Provision 5% x 2 360 000        =   118 000",
    "Net receivables                 = 2 242 000",
])

LESSONS.append(lesson(
    module=M_FIN, topic="The OHADA balance sheet",
    title="Preparing the balance sheet from a trial balance and linking it to the income statement",
    slug="acc3-balance-sheet-from-trial-balance", minutes=28,
    summary="Take the adjusted trial balance of the previous lesson to a balanced balance sheet: net fixed assets, net receivables, prepayments and accruals, and equity updated with the net result and drawings.",
    objectives=[
        "Move each trial-balance item to the right place in the balance sheet after adjustments",
        "Calculate net book values, net receivables, and the amounts for prepayments, accrued income and accruals",
        "Update the capital account with the net result and drawings and check that the balance sheet balances",
        "Trace an error when the two totals disagree",
    ],
    key_concepts=["Adjusted balances", "Net book value", "Net receivables", "Capital account", "Balance check"],
    blocks=[
        H("From the trial balance to the balance sheet"),
        T("Return to Ngwa Traders in Kumba (the trial balance and notes are in the previous lesson, all figures **invented for practice**). "
          "The income statement gave a net profit of FCFA 2 282 000. Now we prepare the balance sheet. Every adjustment affects both statements: the same number appears in the income statement and on the balance sheet."),
        KEY("Where each adjustment goes",
            "Each adjustment has two effects, one in each statement.",
            cards=[["Depreciation", "Income statement: expense. Balance sheet: added to accumulated depreciation, reducing net fixed assets."],
                   ["Bad debts and provision", "Income statement: expense. Balance sheet: receivables reduced by the write-off and the provision."],
                   ["Accruals and prepayments", "Income statement: expense or income adjusted. Balance sheet: a liability or an asset."],
                   ["Closing inventory", "Income statement: reduces cost of goods sold. Balance sheet: a current asset."],
                   ["Net result and drawings", "Added to and subtracted from capital."]]),
        EX("Worked example 1: fixed assets",
           intro="Equipment cost FCFA 3 000 000, accumulated depreciation FCFA 600 000 before this year, charge FCFA 300 000. Vehicles cost FCFA 4 000 000, accumulated depreciation FCFA 1 200 000, charge FCFA 700 000. Land and buildings FCFA 12 000 000 are not depreciated. Find the net fixed assets.",
           steps=[
               S("Equipment", text="Accumulated depreciation 600 000 + 300 000 = 900 000. Net = 3 000 000 − 900 000 = 2 100 000."),
               S("Vehicles", text="1 200 000 + 700 000 = 1 900 000. Net = 4 000 000 − 1 900 000 = 2 100 000."),
               S("Total", text="12 000 000 + 2 100 000 + 2 100 000 = 16 200 000."),
           ]),
        EX("Worked example 2: current assets",
           intro="Closing inventory FCFA 1 500 000; receivables FCFA 2 400 000 less a bad debt of FCFA 40 000 and a provision of 5%; prepaid insurance FCFA 60 000; accrued commission FCFA 20 000; bank FCFA 1 500 000; cash FCFA 200 000. Find the current assets.",
           steps=[
               S("Net receivables", text="2 400 000 − 40 000 = 2 360 000. Provision = 118 000. Net = 2 242 000."),
               S("Add", text="1 500 000 + 2 242 000 + 60 000 + 20 000 + 1 500 000 + 200 000 = 5 522 000."),
               S("Total assets", text="16 200 000 + 5 522 000 = 21 722 000."),
           ]),
        CODE(_t_rec, "text", title="Receivables working"),
        CODE(_t_nb_a, "text", title="Assets of Ngwa Traders"),
        EX("Worked example 3: equity and liabilities",
           intro="Capital at 1 January FCFA 16 610 000; net profit FCFA 2 282 000; drawings FCFA 900 000; long-term loan FCFA 2 000 000; trade payables FCFA 1 700 000; electricity owing FCFA 30 000. Complete the balance sheet.",
           steps=[
               S("Closing equity", text="16 610 000 + 2 282 000 − 900 000 = 17 992 000."),
               S("Current liabilities", text="1 700 000 + 30 000 = 1 730 000."),
               S("Total", text="17 992 000 + 2 000 000 + 1 730 000 = 21 722 000, which equals the total assets."),
           ]),
        CODE(_t_nb_l, "text", title="Equity and liabilities of Ngwa Traders"),
        CODE(_led_cap, "text", title="The capital account in ledger form"),
        T("The totals agree at 21 722 000. This is a good sign, but it does not prove that every figure is right: an error that affects both sides equally would not show. "
          "If the totals disagree, check in this order: (1) the addition of each column; (2) the net result transferred; (3) drawings subtracted, not added; "
          "(4) each adjustment entered on both statements; (5) every trial-balance account used once."),
        H("IAS/IFRS notes"),
        T("The statement of financial position shows **non-current assets** (16 200 000) and **current assets** (5 522 000), then **equity** (17 992 000), "
          "**non-current liabilities** (the loan, 2 000 000) and **current liabilities** (1 730 000). The numbers are the same. "
          "Trade receivables may be shown net, or gross with a note on the allowance; follow the question."),
        MISTAKE("Adding drawings to capital",
                "Drawings reduce the equity. Add the profit; subtract drawings."),
        MISTAKE("Forgetting that an accrued expense is a liability and a prepayment is an asset",
                "Electricity owing (30 000) is a current liability. Insurance prepaid (60 000) is a current asset. Putting them on the wrong side makes the totals disagree."),
        MISTAKE("Deducting the provision from receivables twice",
                "The provision is taken off once on the balance sheet. The ledger balance of receivables is not changed by the provision."),
        QUIZ("Vehicles cost FCFA 4 000 000. Accumulated depreciation at the start was FCFA 1 200 000 and the year's charge is FCFA 700 000. The net book value is",
             ["FCFA 2 100 000", "FCFA 2 800 000", "FCFA 3 300 000", "FCFA 1 900 000"], 0,
             "Accumulated depreciation = 1 200 000 + 700 000 = 1 900 000. Net = 4 000 000 − 1 900 000 = 2 100 000.",
             hint="Add this year's charge to the accumulated depreciation first.",
             feedback=["", "That forgets this year's charge.", "That subtracts only this year's charge.", "That is the accumulated depreciation, not the net amount."]),
        QUIZ("If total assets are FCFA 21 722 000 and total equity and liabilities are FCFA 21 692 000, which is the most likely error?",
             ["Drawings were added to capital", "An accrued expense of FCFA 30 000 was left out of liabilities", "The bank balance was counted twice", "The net profit was added to capital twice"], 1,
             "Liabilities are short by 30 000, exactly the accrued electricity. A missing liability makes the right-hand total too small.",
             feedback=["That would make the difference 1 800 000 (twice the drawings).", "", "That would make the assets larger by 1 500 000.", "That would make the equity side larger by 2 282 000."],
             title="Quick check 2"),
        TIP("Balance sheets in Paper 2 depend on correct adjustments in the income statement: the net result flows into capital. If your balance sheet does not balance, check the difference against the adjustments before changing other figures.",
            title="Exam link"),
        PQ("Equipment cost FCFA 1 000 000, accumulated depreciation FCFA 300 000 at the start, the year's charge FCFA 100 000. Find the net book value.",
           "Accumulated depreciation = 400 000. Net = 600 000."),
        PQ("Receivables FCFA 700 000, bad debt written off FCFA 20 000, provision 5% of the rest. Find the net receivables.",
           "Remaining 680 000. Provision = 34 000. Net = 646 000."),
        PQ("Opening capital FCFA 5 000 000, net loss FCFA 300 000, drawings FCFA 400 000. Find the closing equity.",
           "5 000 000 − 300 000 − 400 000 = 4 300 000."),
        PQ("Assets total FCFA 8 000 000. Equity is FCFA 5 500 000 and long-term loan is FCFA 1 000 000. Find the current liabilities.",
           "Liabilities = 8 000 000 − 5 500 000 = 2 500 000. Current liabilities = 2 500 000 − 1 000 000 = 1 500 000."),
        SUM("Each adjustment appears in both statements: income statement and balance sheet.",
            "Net fixed assets = cost − (opening accumulated depreciation + this year's charge); net receivables = receivables after write-off − provision.",
            "Closing equity = opening capital + net result − drawings.",
            "Total assets must equal total equity and liabilities. When they do not, trace the difference."),
    ]))

# ====================================================================== 10. Incomplete records and single entry
IR = dict(o_eq=500_000, o_inv=400_000, o_rec=300_000, o_bank=250_000, o_cash=50_000, o_pay=350_000,
          rec_from_cust=4_700_000, cash_sales=500_000, paid_sup=3_100_000, exp_paid=900_000, drawings=600_000,
          c_rec=400_000, c_pay=450_000, c_inv=500_000, exp_acc=40_000, dep=100_000)
IR["o_assets"] = IR["o_eq"] + IR["o_inv"] + IR["o_rec"] + IR["o_bank"] + IR["o_cash"]
IR["o_cap"] = IR["o_assets"] - IR["o_pay"]
IR["credit_sales"] = IR["c_rec"] + IR["rec_from_cust"] - IR["o_rec"]
IR["sales"] = IR["credit_sales"] + IR["cash_sales"]
IR["purch"] = IR["c_pay"] + IR["paid_sup"] - IR["o_pay"]
IR["cogs"] = IR["o_inv"] + IR["purch"] - IR["c_inv"]
IR["gp"] = IR["sales"] - IR["cogs"]
IR["exp"] = IR["exp_paid"] + IR["exp_acc"]
IR["np"] = IR["gp"] - IR["exp"] - IR["dep"]
IR["bank"] = IR["o_bank"] + IR["rec_from_cust"] + IR["cash_sales"] - IR["paid_sup"] - IR["exp_paid"] - IR["drawings"]
IR["c_assets"] = (IR["o_eq"] - IR["dep"]) + IR["c_inv"] + IR["c_rec"] + IR["bank"] + IR["o_cash"]
IR["c_liab"] = IR["c_pay"] + IR["exp_acc"]
IR["c_cap"] = IR["c_assets"] - IR["c_liab"]
assert (IR["o_assets"], IR["o_cap"], IR["credit_sales"], IR["sales"], IR["purch"], IR["cogs"], IR["gp"], IR["np"], IR["bank"], IR["c_assets"], IR["c_cap"]) == \
       (1_500_000, 1_150_000, 4_800_000, 5_300_000, 3_200_000, 3_100_000, 2_200_000, 1_160_000, 850_000, 2_200_000, 1_710_000)
assert IR["c_cap"] - IR["o_cap"] + IR["drawings"] == IR["np"]
_t_soa = "\n".join([
    "Statement of affairs at 1 January",
    r("Equipment", IR["o_eq"], w=30), r("Inventory", IR["o_inv"], w=30), r("Receivables", IR["o_rec"], w=30),
    r("Bank", IR["o_bank"], w=30), r("Cash", IR["o_cash"], w=30),
    r("Total assets", None, IR["o_assets"], w=30),
    r("Less payables", None, -IR["o_pay"], w=30),
    r("CAPITAL at 1 January", None, IR["o_cap"], w=30),
])
_t_rcv = "\n".join([
    ledger("Receivables control account",
           [("Balance b/d", IR["o_rec"]), ("Credit sales (balancing)", IR["credit_sales"])],
           [("Bank (from customers)", IR["rec_from_cust"]), ("Balance c/d", IR["c_rec"])]),
    "",
    ledger("Payables control account",
           [("Bank (to suppliers)", IR["paid_sup"]), ("Balance c/d", IR["c_pay"])],
           [("Balance b/d", IR["o_pay"]), ("Credit purchases (balancing)", IR["purch"])]),
])
_t_trad = "\n".join([
    "Trading and income statement (year)",
    r("Sales (4 800 000 + 500 000)", None, IR["sales"], w=32),
    r("Opening inventory", IR["o_inv"], w=32),
    r("Purchases", IR["purch"], w=32),
    r("Less closing inventory", -IR["c_inv"], w=32),
    r("Cost of goods sold", None, -IR["cogs"], w=32),
    r("Gross profit", None, IR["gp"], w=32),
    r("Expenses (900 000 + 40 000)", -IR["exp"], w=32),
    r("Depreciation", -IR["dep"], w=32),
    r("Net profit", None, IR["np"], w=32),
])
_t_cap = "\n".join([
    "Profit from the change in capital",
    r("Closing capital", IR["c_cap"], w=32),
    r("Less opening capital", -IR["o_cap"], w=32),
    r("Increase in capital", IR["c_cap"] - IR["o_cap"], w=32),
    r("Add drawings", IR["drawings"], w=32),
    r("Net profit", IR["np"], w=32),
])
_t_bank = "\n".join([
    ledger("Bank summary",
           [("Balance b/d", IR["o_bank"]), ("From customers", IR["rec_from_cust"]), ("Cash sales banked", IR["cash_sales"])],
           [("To suppliers", IR["paid_sup"]), ("Expenses paid", IR["exp_paid"]), ("Drawings", IR["drawings"]), ("Balance c/d", IR["bank"])]),
])
assert 400_000 * 100 // 80 == 500_000 and 800_000 * 125 // 100 == 1_000_000

LESSONS.append(lesson(
    module=M_FIN, topic="Incomplete records and single entry",
    title="Incomplete records and single entry: finding capital, sales, purchases and profit",
    slug="acc3-incomplete-records-single-entry", minutes=26,
    summary="When there is no full double-entry system, build a statement of affairs, summarise the bank, use control accounts to find sales and purchases, and prepare the income statement.",
    objectives=[
        "Explain why a small business may keep incomplete records and what is missing",
        "Prepare a statement of affairs to find capital at a date",
        "Find credit sales and credit purchases with total receivables and payables accounts",
        "Calculate profit from the change in capital and from the trading and income statement, and use mark-up and margin to find a missing figure",
    ],
    key_concepts=["Incomplete records", "Single entry", "Statement of affairs", "Capital", "Credit sales", "Mark-up and margin"],
    blocks=[
        H("When the books are incomplete"),
        T("Tabi sells provisions from a stall in Mamfe. She does not keep a full set of books. She has a bank statement, a pile of invoices, and a note of "
          "what customers owe. At the year end she wants her profit. Accountants use the information to **rebuild** the missing records. "
          "All figures here are **invented for practice**."),
        D("**Incomplete records** (or **single entry**) means that the business does not keep a full double-entry system. It may have only a cash or bank record and lists of receivables and payables. "
          "The income statement and balance sheet are prepared by working from what is known to what is missing.", title="Incomplete records"),
        D("A **statement of affairs** is a list of the assets and liabilities at a date. **Capital = assets − liabilities.** It is the same calculation as a balance sheet but without double-entry proof.", title="Statement of affairs"),
        KEY("Five steps",
            "Work through them in order.",
            cards=[["1. Opening capital", "Statement of affairs at the start of the year."],
                   ["2. Summarise cash and bank", "Add up receipts and payments to find the missing figures."],
                   ["3. Control accounts", "Find credit sales (receivables) and credit purchases (payables)."],
                   ["4. Statements", "Trading and income statement, then the closing statement of affairs."],
                   ["5. Check", "Closing capital = opening capital + profit − drawings."]]),
        CODE(_t_soa, "text", title="Opening position (invented for practice)"),
        EX("Worked example 1: opening capital",
           intro="At 1 January Tabi's assets are equipment FCFA 500 000, inventory FCFA 400 000, receivables FCFA 300 000, bank FCFA 250 000, cash FCFA 50 000. She owes suppliers FCFA 350 000. Find her capital.",
           steps=[
               S("Total assets", text="500 000 + 400 000 + 300 000 + 250 000 + 50 000 = 1 500 000."),
               S("Capital", text="1 500 000 − 350 000 = 1 150 000."),
           ]),
        EX("Worked example 2: the missing sales and purchases",
           intro="Receipts from customers by cheque were FCFA 4 700 000 and cash sales (all banked) FCFA 500 000. Receivables at the end were FCFA 400 000. "
                 "Payments to suppliers were FCFA 3 100 000 and payables at the end were FCFA 450 000. Find credit sales and purchases.",
           steps=[
               S("Credit sales", text="Receivables control account: opening 300 000 + credit sales = receipts 4 700 000 + closing 400 000. Credit sales = 4 700 000 + 400 000 − 300 000 = 4 800 000."),
               S("Total sales", text="4 800 000 + 500 000 cash sales = 5 300 000."),
               S("Purchases", text="Payables control account: purchases = payments 3 100 000 + closing 450 000 − opening 350 000 = 3 200 000."),
           ]),
        CODE(_t_rcv, "text", title="Control accounts used to find the missing figures"),
        EX("Worked example 3: the bank and the profit",
           intro="Other facts: expenses paid FCFA 900 000, drawings FCFA 600 000, FCFA 40 000 of expenses are owing, depreciation of equipment FCFA 100 000, closing inventory FCFA 500 000. Find the net profit and the closing capital.",
           steps=[
               S("Closing bank", text="250 000 + 4 700 000 + 500 000 − 3 100 000 − 900 000 − 600 000 = 850 000."),
               S("Cost of goods sold", text="400 000 + 3 200 000 − 500 000 = 3 100 000. Gross profit = 5 300 000 − 3 100 000 = 2 200 000."),
               S("Net profit", text="2 200 000 − (900 000 + 40 000) − 100 000 = 1 160 000."),
               S("Closing capital", text="1 150 000 + 1 160 000 − 600 000 = 1 710 000."),
           ]),
        CODE(_t_bank, "text", title="Summary of the bank"),
        CODE(_t_trad, "text", title="Statement from the rebuilt figures"),
        CODE(_t_cap, "text", title="Profit from the change in capital (check)"),
        T("The two ways of finding profit agree at 1 160 000. The change in capital method is quick when you do not have enough information for a full income statement, but it does not show how the profit was earned. "
          "The closing assets are 2 200 000 and the liabilities 490 000, so the closing capital is 1 710 000."),
        D("**Mark-up** is profit as a percentage of cost. **Margin** is profit as a percentage of sales. If the mark-up is 25% on cost, a cost of FCFA 800 000 gives sales of 800 000 × 125 ÷ 100 = 1 000 000. "
          "The gross profit is 200 000, which is 20% of sales. Use mark-up or margin to find sales, cost of goods sold or missing inventory when records are lost.", title="Mark-up and margin"),
        MISTAKE("Using cash received as credit sales",
                "Receipts from customers are not sales. Credit sales = receipts + closing receivables − opening receivables."),
        MISTAKE("Mixing up mark-up and margin",
                "A 25% mark-up is a 20% margin. Read which base the question uses: cost for mark-up, sales for margin."),
        MISTAKE("Forgetting drawings in the capital method",
                "Closing capital − opening capital understates profit by the amount the owner has taken out. Add the drawings back."),
        QUIZ("Opening capital FCFA 1 000 000, closing capital FCFA 1 400 000, drawings FCFA 300 000. The profit for the year is",
             ["FCFA 700 000", "FCFA 400 000", "FCFA 100 000", "FCFA 1 700 000"], 0,
             "Increase in capital 400 000 + drawings 300 000 = 700 000.",
             hint="Find the increase in capital first, then add what the owner took out.",
             feedback=["", "That is only the increase in capital; drawings must be added back.", "That subtracts the drawings instead of adding them.", "That adds all three figures."]),
        QUIZ("Opening receivables FCFA 200 000, closing receivables FCFA 260 000, cash received from customers FCFA 1 500 000. Credit sales are",
             ["FCFA 1 440 000", "FCFA 1 560 000", "FCFA 1 500 000", "FCFA 1 960 000"], 1,
             "Credit sales = 1 500 000 + 260 000 − 200 000 = 1 560 000.",
             feedback=["That reverses the change in receivables.", "", "That ignores the change in receivables.", "That adds the opening and closing receivables."], title="Quick check 2"),
        TIP("Incomplete records is part of the final accounts area of the syllabus. Show each working (opening capital, control accounts, bank summary) before the statements, because the working marks are available even if the final profit is wrong.",
            title="Exam link"),
        PQ("A trader's assets at the start are FCFA 2 000 000 and liabilities FCFA 600 000. Find the capital.", "2 000 000 − 600 000 = 1 400 000."),
        PQ("Credit purchases: opening payables FCFA 150 000, closing payables FCFA 220 000, payments to suppliers FCFA 1 000 000. Find purchases.",
           "1 000 000 + 220 000 − 150 000 = 1 070 000."),
        PQ("The cost of goods sold is FCFA 600 000 and the mark-up is 40% on cost. Find sales and the gross profit.",
           "Sales = 600 000 × 140 ÷ 100 = 840 000. Gross profit = 240 000."),
        PQ("Capital rose from FCFA 900 000 to FCFA 1 200 000 and the owner also added FCFA 100 000 new capital. Drawings were FCFA 250 000. Find the profit.",
           "Increase in capital 300 000 + drawings 250 000 − new capital 100 000 = 450 000."),
        SUM("With incomplete records, rebuild the missing information from what is known.",
            "Capital = assets − liabilities; profit = closing capital − opening capital + drawings − new capital introduced.",
            "Credit sales = receipts + closing receivables − opening receivables; purchases = payments + closing payables − opening payables.",
            "Mark-up is on cost, margin is on sales: a 25% mark-up is a 20% margin."),
    ]))

# ====================================================================== 11. Non-profit organisations
CL = dict(o_cash=180_000, subs=640_000, don=120_000, comp_fees=120_000, refr_sales=210_000,
          rent=240_000, refs=150_000, prizes=80_000, refr_buy=130_000, print_=60_000, equip_buy=200_000,
          arrears_o=50_000, adv_o=20_000, arrears_c=70_000, adv_c=30_000, prizes_owing=10_000, dep=50_000, equip_o=300_000)
CL["rec_total"] = CL["o_cash"] + CL["subs"] + CL["don"] + CL["comp_fees"] + CL["refr_sales"]
CL["pay_total_before"] = CL["rent"] + CL["refs"] + CL["prizes"] + CL["refr_buy"] + CL["print_"] + CL["equip_buy"]
CL["c_cash"] = CL["rec_total"] - CL["pay_total_before"]
CL["subs_inc"] = CL["subs"] + CL["arrears_c"] + CL["adv_o"] - CL["arrears_o"] - CL["adv_c"]
CL["comp_surplus"] = CL["comp_fees"] - (CL["prizes"] + CL["prizes_owing"])
CL["refr_profit"] = CL["refr_sales"] - CL["refr_buy"]
CL["inc_total"] = CL["subs_inc"] + CL["don"] + CL["refr_profit"] + CL["comp_surplus"]
CL["exp_total"] = CL["rent"] + CL["refs"] + CL["print_"] + CL["dep"]
CL["surplus"] = CL["inc_total"] - CL["exp_total"]
CL["fund_o"] = CL["equip_o"] + CL["o_cash"] + CL["arrears_o"] - CL["adv_o"]
CL["equip_c"] = CL["equip_o"] + CL["equip_buy"] - CL["dep"]
CL["assets_c"] = CL["equip_c"] + CL["c_cash"] + CL["arrears_c"]
CL["liab_c"] = CL["adv_c"] + CL["prizes_owing"]
CL["fund_c"] = CL["assets_c"] - CL["liab_c"]
assert (CL["rec_total"], CL["pay_total_before"], CL["c_cash"], CL["subs_inc"], CL["comp_surplus"], CL["refr_profit"], CL["inc_total"], CL["exp_total"],
        CL["surplus"], CL["fund_o"], CL["equip_c"], CL["assets_c"], CL["liab_c"], CL["fund_c"]) == \
       (1_270_000, 860_000, 410_000, 650_000, 30_000, 80_000, 880_000, 500_000, 380_000, 510_000, 450_000, 930_000, 40_000, 890_000)
assert CL["fund_o"] + CL["surplus"] == CL["fund_c"]
_t_rp = ledger("Receipts and payments account (cash book summary)",
               [("Balance b/d", CL["o_cash"]), ("Subscriptions", CL["subs"]), ("Donations", CL["don"]),
                ("Competition entry fees", CL["comp_fees"]), ("Refreshment sales", CL["refr_sales"])],
               [("Rent of ground", CL["rent"]), ("Referees' fees", CL["refs"]), ("Competition prizes", CL["prizes"]),
                ("Refreshment purchases", CL["refr_buy"]), ("Printing", CL["print_"]), ("Equipment bought", CL["equip_buy"]),
                ("Balance c/d", CL["c_cash"])])
_t_subs = ledger("Subscriptions account (adjustment)",
                 [("Arrears b/d", CL["arrears_o"]), ("Income and expenditure", CL["subs_inc"]), ("In advance c/d", CL["adv_c"])],
                 [("In advance b/d", CL["adv_o"]), ("Bank received", CL["subs"]), ("Arrears c/d", CL["arrears_c"])])
_t_comp = ledger("Competition account",
                 [("Prizes paid", CL["prizes"]), ("Prizes owing", CL["prizes_owing"]), ("Surplus to income and exp.", CL["comp_surplus"])],
                 [("Entry fees", CL["comp_fees"])])
_t_ie = ledger("Income and expenditure account (year)",
               [("Rent of ground", CL["rent"]), ("Referees' fees", CL["refs"]), ("Printing", CL["print_"]), ("Depreciation", CL["dep"]),
                ("SURPLUS to accumulated fund", CL["surplus"])],
               [("Subscriptions", CL["subs_inc"]), ("Donations", CL["don"]), ("Profit on refreshments", CL["refr_profit"]),
                ("Surplus on competition", CL["comp_surplus"])])
_t_fund = "\n".join([
    "Balance sheet extract at year end",
    r("Equipment (300 + 200 - 50)", CL["equip_c"], w=30), r("Subscriptions owing", CL["arrears_c"], w=30), r("Cash and bank", CL["c_cash"], w=30),
    r("TOTAL ASSETS", None, CL["assets_c"], w=30),
    r("Accumulated fund 1 Jan", CL["fund_o"], w=30), r("Add surplus", CL["surplus"], w=30), r("Accumulated fund", None, CL["fund_c"], w=30),
    r("Subscriptions in advance", CL["adv_c"], w=30), r("Prizes owing", CL["prizes_owing"], w=30),
    r("TOTAL FUND AND LIABILITIES", None, CL["fund_c"] + CL["liab_c"], w=30),
])
assert CL["fund_c"] + CL["liab_c"] == CL["assets_c"]

LESSONS.append(lesson(
    module=M_FIN, topic="Accounts of non-profit organizations",
    title="Accounts of non-profit organisations: receipts and payments, income and expenditure",
    slug="acc3-non-profit-organisations", minutes=28,
    summary="Prepare the receipts and payments account, adjust subscriptions for arrears and advances, and prepare an income and expenditure account that shows a surplus or deficit for a club or society.",
    objectives=[
        "Explain how a non-profit organisation's accounts differ from those of a trader (surplus or deficit, accumulated fund)",
        "Prepare a receipts and payments account and find the closing balance",
        "Calculate subscription income for the year using arrears and advances (a subscriptions adjustment account)",
        "Prepare an income and expenditure account, including the profit on a refreshment stall and a competition account, and the accumulated fund",
    ],
    key_concepts=["Non-profit organisation", "Receipts and payments account", "Income and expenditure account", "Subscriptions", "Accumulated fund", "Surplus and deficit"],
    blocks=[
        H("Clubs do not make profit, but they keep accounts"),
        T("A youth football club in Bamenda collects subscriptions from members, receives a few donations, pays for a ground and referees, and runs a small refreshment stall. "
          "Nobody owns the club to share profit. The committee still needs to show members what happened to their money. "
          "The Board's 2023 report notes that most candidates avoided the question on non-profit organisations, so learn this topic well. All figures are **invented for practice**."),
        D("A **non-profit organisation** (club, society, association) exists to provide a service to members, not to make profit for owners. Its result is a **surplus** (income higher than expenditure) or a **deficit**. "
          "Its capital is the **accumulated fund**.", title="Non-profit organisation"),
        D("The **receipts and payments account** is a summary of the cash book: all cash and bank received on the debit side, all paid on the credit side, with the balance carried down. "
          "It follows **cash**, includes capital items such as equipment bought and does not adjust for amounts owing or paid in advance.", title="Receipts and payments account"),
        D("The **income and expenditure account** is like an income statement. It shows the income and expenditure **of the year** (accrual basis), adjusted for arrears, amounts owing and depreciation, and excludes capital items. "
          "The balance is the surplus or deficit, which is added to or subtracted from the accumulated fund.", title="Income and expenditure account"),
        KEY("Receipts and payments or income and expenditure?",
            "A common source of lost marks.",
            cards=[["Receipts and payments", "Cash basis. Includes capital items and opening/closing balances. No adjustments."],
                   ["Income and expenditure", "Accrual basis. Revenue items only. Adjusted for subscriptions owing/in advance and accruals. Includes depreciation."]]),
        EX("Worked example 1: receipts and payments account",
           intro="The club had FCFA 180 000 in cash and bank on 1 January. It received subscriptions FCFA 640 000, donations FCFA 120 000, competition entry fees FCFA 120 000 and refreshment sales FCFA 210 000. "
                 "It paid rent FCFA 240 000, referees FCFA 150 000, prizes FCFA 80 000, refreshment purchases FCFA 130 000, printing FCFA 60 000 and bought equipment for FCFA 200 000. Prepare the account.",
           steps=[
               S("Receipts", text="180 000 + 640 000 + 120 000 + 120 000 + 210 000 = 1 270 000."),
               S("Payments", text="240 000 + 150 000 + 80 000 + 130 000 + 60 000 + 200 000 = 860 000."),
               S("Balance carried down", text="1 270 000 − 860 000 = 410 000."),
           ]),
        CODE(_t_rp, "text", title="Receipts and payments account (invented for practice)"),
        H("Subscriptions: the adjustment account"),
        D("Subscriptions for the year = cash received + arrears at the end + subscriptions paid in advance at the start − arrears at the start − subscriptions in advance at the end. "
          "The easy way is a **subscriptions account** and the balancing figure.", title="Subscription income"),
        EX("Worked example 2: subscriptions for the year",
           intro="Members owed FCFA 50 000 at the start and had paid FCFA 20 000 for the new year. At the end members owe FCFA 70 000 and have paid FCFA 30 000 in advance. Cash received in the year was FCFA 640 000. Find the income for the year.",
           steps=[
               S("Credit side", text="In advance b/d 20 000 + bank 640 000 + arrears c/d 70 000 = 730 000."),
               S("Debit side before the balancing figure", text="Arrears b/d 50 000 + in advance c/d 30 000 = 80 000."),
               S("Income for the year", text="730 000 − 80 000 = 650 000 (the figure for the income and expenditure account)."),
           ]),
        CODE(_t_subs, "text", title="Subscriptions account"),
        H("Refreshments and competitions"),
        T("When an activity pays its own way, show only its **profit** (or surplus) in the income and expenditure account. "
          "The refreshment stall: sales 210 000 − purchases 130 000 = profit 80 000. The competition: entry fees 120 000 − prizes (80 000 paid + 10 000 owing) = surplus 30 000."),
        CODE(_t_comp, "text", title="Competition account"),
        EX("Worked example 3: the income and expenditure account",
           intro="Prepare the account. Depreciation of equipment is FCFA 50 000. The equipment purchase is a capital item, so it is not an expense.",
           steps=[
               S("Income", text="Subscriptions 650 000 + donations 120 000 + refreshment profit 80 000 + competition surplus 30 000 = 880 000."),
               S("Expenditure", text="Rent 240 000 + referees 150 000 + printing 60 000 + depreciation 50 000 = 500 000."),
               S("Surplus", text="880 000 − 500 000 = 380 000, added to the accumulated fund."),
           ]),
        CODE(_t_ie, "text", title="Income and expenditure account"),
        CODE(_t_fund, "text", title="The accumulated fund and the balance sheet"),
        T("The accumulated fund at 1 January was 510 000 (assets 530 000: equipment 300 000, cash 180 000, subscriptions owing 50 000; less subscriptions in advance 20 000). "
          "At the end it is 510 000 + 380 000 = 890 000, and the balance sheet totals 930 000 on both sides. In IAS/IFRS wording you may see 'surplus or deficit for the year' and 'accumulated fund' or 'reserves'. Check your textbook."),
        MISTAKE("Putting the purchase of equipment in the income and expenditure account",
                "Equipment bought is a capital payment. Only depreciation of the equipment is expenditure."),
        MISTAKE("Using cash received as subscription income",
                "Adjust for arrears and advances. Cash received (640 000) and income for the year (650 000) are different here."),
        MISTAKE("Forgetting that a non-profit organisation has no capital account",
                "Its capital is the accumulated fund, and the surplus or deficit is added to or subtracted from it."),
        QUIZ("Which item appears in the receipts and payments account but NOT in the income and expenditure account?",
             ["Rent paid", "Equipment bought", "Depreciation", "Donations received for general use"], 1,
             "Equipment bought is a capital item: cash is paid, but only depreciation is expenditure.",
             hint="Which one is a capital item?",
             feedback=["Rent is expenditure and also a payment.", "", "Depreciation is only in income and expenditure (no cash is paid).", "General donations are revenue income and are in both."]),
        QUIZ("Subscriptions received in the year FCFA 400 000. Arrears at the start FCFA 30 000, at the end FCFA 50 000. No advances. Subscription income is",
             ["FCFA 420 000", "FCFA 380 000", "FCFA 400 000", "FCFA 480 000"], 0,
             "Income = 400 000 + 50 000 − 30 000 = 420 000.",
             feedback=["", "That subtracts the closing arrears and adds the opening arrears (the wrong way).", "That ignores the arrears.", "That adds both arrears."], title="Quick check 2"),
        TIP("Accounts of non-profit organisations are named in the Board's 2023 report as a Paper 2 topic: the question asked for an adjustment account for subscriptions, competition prizes and an income and expenditure account. "
            "Practise the subscriptions account until it is automatic.", title="Exam link"),
        PQ("Subscriptions received FCFA 500 000. Owing at the start FCFA 40 000, owing at the end FCFA 60 000. Find the income for the year.",
           "500 000 + 60 000 − 40 000 = 520 000."),
        PQ("Subscriptions received FCFA 300 000; paid in advance at the start FCFA 10 000 and at the end FCFA 25 000. Find the income for the year.",
           "300 000 + 10 000 − 25 000 = 285 000."),
        PQ("The income is FCFA 520 000 and the expenditure FCFA 450 000. State the result and where it goes.",
           "Surplus of 70 000, added to the accumulated fund."),
        PQ("Assets of a club are FCFA 600 000 and liabilities FCFA 80 000. Find the accumulated fund.", "600 000 − 80 000 = 520 000."),
        SUM("A non-profit organisation reports a surplus or deficit and has an accumulated fund instead of capital.",
            "Receipts and payments account: cash summary including capital items. Income and expenditure account: accrual basis, revenue items only, with depreciation.",
            "Subscription income = received + closing arrears + opening advances − opening arrears − closing advances.",
            "Show an activity's profit or surplus (refreshments, competitions) and add the result to the accumulated fund."),
    ]))

# ====================================================================== 12. Manufacturing accounts
MF = dict(rm_o=150_000, rm_buy=1_200_000, rm_carr=30_000, rm_c=180_000, dl=900_000, de=50_000,
          ind_wages=200_000, f_rent=240_000, power=180_000, power_owing=20_000, f_dep=120_000,
          wip_o=100_000, wip_c=130_000, units=1_440, fg_o=300_000, fg_c=400_000, sales=4_600_000, other=900_000)
MF["rm_used"] = MF["rm_o"] + MF["rm_buy"] + MF["rm_carr"] - MF["rm_c"]
MF["prime"] = MF["rm_used"] + MF["dl"] + MF["de"]
MF["oh"] = MF["ind_wages"] + MF["f_rent"] + MF["power"] + MF["power_owing"] + MF["f_dep"]
MF["factory"] = MF["prime"] + MF["oh"]
MF["cop"] = MF["factory"] + MF["wip_o"] - MF["wip_c"]
MF["unit"] = MF["cop"] // MF["units"]
MF["cogs"] = MF["fg_o"] + MF["cop"] - MF["fg_c"]
MF["gp"] = MF["sales"] - MF["cogs"]
MF["np"] = MF["gp"] - MF["other"]
assert (MF["rm_used"], MF["prime"], MF["oh"], MF["factory"], MF["cop"], MF["unit"], MF["cogs"], MF["gp"], MF["np"]) == \
       (1_200_000, 2_150_000, 760_000, 2_910_000, 2_880_000, 2_000, 2_780_000, 1_820_000, 920_000)
assert MF["cop"] % MF["units"] == 0
_t_mf = "\n".join([
    "Manufacturing account for the year",
    r("Opening raw materials", MF["rm_o"], w=32),
    r("Purchases of raw materials", MF["rm_buy"], w=32),
    r("Carriage inwards", MF["rm_carr"], w=32),
    r("Less closing raw materials", -MF["rm_c"], w=32),
    r("Raw materials used", None, MF["rm_used"], w=32),
    r("Direct labour", None, MF["dl"], w=32),
    r("Direct expenses", None, MF["de"], w=32),
    r("PRIME COST", None, MF["prime"], w=32),
    r("Indirect wages", MF["ind_wages"], w=32),
    r("Factory rent", MF["f_rent"], w=32),
    r("Power (180 000 + 20 000 owing)", MF["power"] + MF["power_owing"], w=32),
    r("Depreciation of machinery", MF["f_dep"], w=32),
    r("Factory overheads", None, MF["oh"], w=32),
    r("FACTORY COST", None, MF["factory"], w=32),
    r("Add opening work in progress", None, MF["wip_o"], w=32),
    r("Less closing work in progress", None, -MF["wip_c"], w=32),
    r("COST OF PRODUCTION", None, MF["cop"], w=32),
])
_t_mt = "\n".join([
    "Trading account (goods made at cost)",
    r("Sales", None, MF["sales"], w=32),
    r("Opening finished goods", MF["fg_o"], w=32),
    r("Cost of production", MF["cop"], w=32),
    r("Less closing finished goods", -MF["fg_c"], w=32),
    r("Cost of goods sold", None, -MF["cogs"], w=32),
    r("Gross profit", None, MF["gp"], w=32),
    r("Selling and admin. expenses", None, -MF["other"], w=32),
    r("Net profit", None, MF["np"], w=32),
])
assert 3_200_000 - MF["cop"] == 320_000

LESSONS.append(lesson(
    module=M_FIN, topic="Manufacturing accounts",
    title="Manufacturing accounts: prime cost, factory cost and cost of production",
    slug="acc3-manufacturing-accounts", minutes=26,
    summary="Prepare a manufacturing account for a business that makes the goods it sells: raw materials used, prime cost, factory overheads, work in progress, cost of production and the unit cost.",
    objectives=[
        "Distinguish direct costs (prime cost) from factory overheads",
        "Calculate raw materials used, prime cost, factory cost and cost of production",
        "Adjust for opening and closing work in progress and for accruals in factory costs",
        "Transfer the cost of production to the trading account and find the unit cost",
    ],
    key_concepts=["Manufacturing account", "Prime cost", "Factory overheads", "Work in progress", "Cost of production", "Unit cost"],
    blocks=[
        H("Making the goods you sell"),
        T("A furniture workshop in Kribi buys timber, pays carpenters, runs machines, and then sells the finished tables and chairs. "
          "A shop only needs to know the cost of what it **bought**. A workshop must also work out the cost of what it **made**. "
          "The **manufacturing account** shows this cost. All figures are **invented for practice**."),
        IMG("f5acc3-manufacturing-flow.svg",
            alt="Flow from direct materials, labour and expenses to prime cost, then plus factory overheads to cost of production, then to the income statement.",
            caption="Figure 1. From direct costs to the cost of production."),
        D("**Prime cost** = raw materials used + direct labour + direct expenses. These costs can be traced directly to the goods made. "
          "**Factory overheads** are the other costs of running the factory (indirect wages, factory rent, power, depreciation of machinery). "
          "**Factory cost** = prime cost + factory overheads.", title="Prime cost and overheads"),
        D("**Work in progress** (WIP) is goods started but not finished at the date of the statement. "
          "**Cost of production** = factory cost + opening WIP − closing WIP. The cost of production is transferred to the trading account in place of purchases.", title="Work in progress"),
        KEY("The layout, step by step",
            "Learn the order. Each total has a name.",
            cards=[["Raw materials used", "Opening raw materials + purchases + carriage inwards − closing raw materials."],
                   ["Prime cost", "Raw materials used + direct labour + direct expenses."],
                   ["Factory cost", "Prime cost + factory overheads (adjust for accruals and prepayments)."],
                   ["Cost of production", "Factory cost + opening WIP − closing WIP."],
                   ["Unit cost", "Cost of production ÷ number of units made."]]),
        EX("Worked example 1: prime cost",
           intro="Opening raw materials FCFA 150 000; purchases FCFA 1 200 000; carriage inwards FCFA 30 000; closing raw materials FCFA 180 000; direct labour FCFA 900 000; direct expenses FCFA 50 000. Find the prime cost.",
           steps=[
               S("Raw materials used", text="150 000 + 1 200 000 + 30 000 − 180 000 = 1 200 000."),
               S("Prime cost", text="1 200 000 + 900 000 + 50 000 = 2 150 000."),
           ]),
        EX("Worked example 2: factory cost and cost of production",
           intro="Factory overheads: indirect wages FCFA 200 000, factory rent FCFA 240 000, power FCFA 180 000 plus FCFA 20 000 owing, depreciation of machinery FCFA 120 000. Opening WIP FCFA 100 000, closing WIP FCFA 130 000. Find the cost of production.",
           steps=[
               S("Overheads", text="200 000 + 240 000 + (180 000 + 20 000) + 120 000 = 760 000."),
               S("Factory cost", text="2 150 000 + 760 000 = 2 910 000."),
               S("Cost of production", text="2 910 000 + 100 000 − 130 000 = 2 880 000."),
           ]),
        CODE(_t_mf, "text", title="Manufacturing account (invented for practice)"),
        EX("Worked example 3: the trading account and the unit cost",
           intro="The workshop made 1 440 units. Finished goods: opening FCFA 300 000, closing FCFA 400 000. Sales FCFA 4 600 000. Selling and administration expenses FCFA 900 000. Find the unit cost, gross profit and net profit.",
           steps=[
               S("Unit cost", text="2 880 000 ÷ 1 440 = 2 000 per unit."),
               S("Cost of goods sold", text="300 000 + 2 880 000 − 400 000 = 2 780 000."),
               S("Gross profit", text="4 600 000 − 2 780 000 = 1 820 000."),
               S("Net profit", text="1 820 000 − 900 000 = 920 000."),
           ]),
        CODE(_t_mt, "text", title="Trading account and net profit"),
        T("Some firms transfer the goods to the trading account at a **market price** rather than at cost, to see how much of the profit comes from making the goods. "
          "For example, if the goods made at a cost of 2 880 000 are transferred at 3 200 000, the **manufacturing profit** is 320 000. "
          "The follow-up treatment (a provision for unrealised profit on closing finished goods) is beyond this lesson. Check your textbook if your teacher includes it."),
        MISTAKE("Putting office costs in factory overheads",
                "Only the costs of the factory belong in the manufacturing account. Office and selling costs go to the income statement."),
        MISTAKE("Using purchases in the trading account",
                "A manufacturer replaces purchases by the cost of production. Do not use both."),
        MISTAKE("Forgetting work in progress",
                "Add the opening WIP and subtract the closing WIP after factory cost. An increase in WIP lowers the cost of production."),
        QUIZ("Which of these is part of prime cost?",
             ["Factory rent", "Wages of the machine operator who makes the product", "Depreciation of machinery", "Office salaries"], 1,
             "Direct labour (the wages of the people who make the product) is part of prime cost.",
             hint="Which cost can be traced directly to the goods?",
             feedback=["Factory rent is an overhead.", "", "Depreciation of machinery is an overhead.", "Office salaries are not factory costs."]),
        QUIZ("Factory cost FCFA 1 000 000, opening WIP FCFA 80 000, closing WIP FCFA 120 000. The cost of production is",
             ["FCFA 960 000", "FCFA 1 040 000", "FCFA 1 200 000", "FCFA 1 000 000"], 0,
             "1 000 000 + 80 000 − 120 000 = 960 000.",
             feedback=["", "That adds the closing WIP and subtracts the opening WIP (reversed).", "That adds both WIP figures.", "That ignores work in progress."], title="Quick check 2"),
        TIP("The manufacturing account is part of the final accounts section of the syllabus. The order of totals (prime cost, factory cost, cost of production) is the usual way of awarding working marks, so label every total.",
            title="Exam link"),
        PQ("Raw materials: opening FCFA 40 000, purchases FCFA 300 000, closing FCFA 60 000. Find the raw materials used.", "40 000 + 300 000 − 60 000 = 280 000."),
        PQ("Raw materials used FCFA 280 000, direct labour FCFA 150 000, direct expenses FCFA 20 000. Find the prime cost.", "280 000 + 150 000 + 20 000 = 450 000."),
        PQ("Prime cost FCFA 450 000, factory overheads FCFA 120 000, opening WIP FCFA 30 000, closing WIP FCFA 20 000. Find the cost of production.",
           "Factory cost = 570 000. Cost of production = 570 000 + 30 000 − 20 000 = 580 000."),
        PQ("The cost of production in the previous question was for 2 900 units. Find the cost per unit.", "580 000 ÷ 2 900 = 200."),
        SUM("A manufacturer prepares a manufacturing account before the trading account.",
            "Prime cost = materials used + direct labour + direct expenses; factory cost = prime cost + factory overheads.",
            "Cost of production = factory cost + opening WIP − closing WIP, and it replaces purchases in the trading account.",
            "Unit cost = cost of production ÷ units made."),
    ]))

# ====================================================================== 13. Departmental accounts
DP = {"A": dict(sales=3_000_000, oi=300_000, pur=1_800_000, ci=400_000), "B": dict(sales=2_000_000, oi=200_000, pur=1_100_000, ci=250_000)}
for _k, _v in DP.items():
    _v["cogs"] = _v["oi"] + _v["pur"] - _v["ci"]
    _v["gp"] = _v["sales"] - _v["cogs"]
assert (DP["A"]["cogs"], DP["B"]["cogs"], DP["A"]["gp"], DP["B"]["gp"]) == (1_700_000, 1_050_000, 1_300_000, 950_000)
_alloc = [("Rent", 500_000, (60, 40), "floor area"), ("Wages", 900_000, (2, 1), "staff numbers"),
          ("Advertising", 200_000, (3_000_000, 2_000_000), "sales"), ("General expenses", 100_000, (1, 1), "equally")]
DPX = {"A": 0, "B": 0}
_alines = [f"{'Expense':<17}{'Total':>9}  {'Basis':<14}{'Dept A':>9}{'Dept B':>9}"]
for nm, tot, (wa, wb), basis in _alloc:
    a = tot * wa // (wa + wb)
    b = tot - a
    assert tot * wa % (wa + wb) == 0
    DPX["A"] += a
    DPX["B"] += b
    _alines.append(f"{nm:<17}{n(tot):>9}  {basis:<14}{n(a):>9}{n(b):>9}")
_alines.append(f"{'Total':<17}{n(sum(t for _, t, _, _ in _alloc)):>9}  {'':<14}{n(DPX['A']):>9}{n(DPX['B']):>9}")
_t_alloc = "\n".join(_alines)
assert DPX == {"A": 1_070_000, "B": 630_000}
DP["A"]["np"] = DP["A"]["gp"] - DPX["A"]
DP["B"]["np"] = DP["B"]["gp"] - DPX["B"]
TOTNP = DP["A"]["np"] + DP["B"]["np"]
assert (DP["A"]["np"], DP["B"]["np"], TOTNP) == (230_000, 320_000, 550_000) and TOTNP == DP["A"]["gp"] + DP["B"]["gp"] - 1_700_000


def _drow(label, a, b, sign=1):
    return f"{label:<22}{n(sign * a) if a is not None else '':>11}{n(sign * b) if b is not None else '':>11}{n(sign * (a + b)) if a is not None else '':>11}"


_t_dept = "\n".join([
    "Departmental income statement",
    f"{'':<22}{'Clothing':>11}{'Footwear':>11}{'Total':>11}",
    _drow("Sales", DP["A"]["sales"], DP["B"]["sales"]),
    _drow("Opening inventory", DP["A"]["oi"], DP["B"]["oi"]),
    _drow("Purchases", DP["A"]["pur"], DP["B"]["pur"]),
    _drow("Less closing inventory", DP["A"]["ci"], DP["B"]["ci"], -1),
    _drow("Cost of goods sold", DP["A"]["cogs"], DP["B"]["cogs"]),
    _drow("GROSS PROFIT", DP["A"]["gp"], DP["B"]["gp"]),
    _drow("Expenses (allocated)", DPX["A"], DPX["B"]),
    _drow("NET PROFIT", DP["A"]["np"], DP["B"]["np"]),
])
_gpA, _gpB = DP["A"]["gp"] * 1000 // DP["A"]["sales"], DP["B"]["gp"] * 1000 // DP["B"]["sales"]
assert (_gpA, _gpB) == (433, 475)

LESSONS.append(lesson(
    module=M_FIN, topic="Departmental accounts",
    title="Departmental accounts: allocating expenses and comparing departments",
    slug="acc3-departmental-accounts", minutes=24,
    summary="Prepare trading and income statements for each department of a business, apportion shared expenses on a fair basis, and compare gross and net profit by department.",
    objectives=[
        "Explain why a business with several departments prepares separate accounts for each",
        "Prepare departmental gross profits from sales, purchases and inventory",
        "Apportion shared expenses using a suitable basis (floor area, staff, sales or equal shares)",
        "Calculate net profit by department and compare gross profit percentages",
    ],
    key_concepts=["Departmental accounts", "Apportionment", "Basis of allocation", "Departmental gross profit", "Departmental net profit"],
    blocks=[
        H("One shop, two departments"),
        T("A store in Douala has a clothing department and a footwear department. The owner pays one rent and one wage bill, and she wants to know which department earns more. "
          "Departmental accounts split the sales, costs and profit of each department. All figures are **invented for practice**."),
        D("**Departmental accounts** are trading and income statements prepared separately for each part of a business, so the owner can see which departments make the most profit and which need action.", title="Departmental accounts"),
        D("Some costs belong to one department (its purchases, its inventory). Others are shared. Shared costs are **apportioned** using a fair **basis**: "
          "rent by floor area, wages by number of staff (or time), advertising by sales, and costs with no better basis, equally.", title="Apportionment"),
        KEY("Steps",
            "The same steps every time.",
            cards=[["1. Gross profit", "Prepare the trading section for each department: sales − cost of goods sold."],
                   ["2. Apportion", "Share each general expense on a basis, and show the calculation."],
                   ["3. Net profit", "Departmental gross profit − the share of expenses."],
                   ["4. Check", "The departmental figures must add up to the totals for the whole business."]]),
        EX("Worked example 1: departmental gross profit",
           intro="Clothing: sales FCFA 3 000 000, opening inventory FCFA 300 000, purchases FCFA 1 800 000, closing inventory FCFA 400 000. Footwear: sales FCFA 2 000 000, opening inventory FCFA 200 000, purchases FCFA 1 100 000, closing inventory FCFA 250 000.",
           steps=[
               S("Clothing", text="Cost of goods sold = 300 000 + 1 800 000 − 400 000 = 1 700 000. Gross profit = 3 000 000 − 1 700 000 = 1 300 000."),
               S("Footwear", text="Cost of goods sold = 200 000 + 1 100 000 − 250 000 = 1 050 000. Gross profit = 2 000 000 − 1 050 000 = 950 000."),
               S("Total", text="1 300 000 + 950 000 = 2 250 000."),
           ]),
        EX("Worked example 2: apportion the expenses",
           intro="Shared expenses: rent FCFA 500 000 (floor areas 60 m² and 40 m²); wages FCFA 900 000 (2 staff and 1 staff); advertising FCFA 200 000 (in proportion to sales); general expenses FCFA 100 000 (shared equally).",
           steps=[
               S("Rent", text="60 : 40 = 3 : 2. Clothing 300 000; footwear 200 000."),
               S("Wages", text="2 : 1. Clothing 600 000; footwear 300 000."),
               S("Advertising", text="Sales 3 000 000 : 2 000 000 = 3 : 2. Clothing 120 000; footwear 80 000."),
               S("General expenses", text="50 000 each. Totals: clothing 1 070 000; footwear 630 000."),
           ]),
        CODE(_t_alloc, "text", title="Apportionment schedule (invented for practice)"),
        EX("Worked example 3: net profit and comparison",
           intro="Prepare the departmental statement and compare the departments.",
           steps=[
               S("Clothing net profit", text="1 300 000 − 1 070 000 = 230 000."),
               S("Footwear net profit", text="950 000 − 630 000 = 320 000."),
               S("Total", text="230 000 + 320 000 = 550 000 = 2 250 000 − 1 700 000 total expenses."),
               S("Percentages", text="Gross profit on sales: clothing 1 300 000 ÷ 3 000 000 = 43.3%; footwear 950 000 ÷ 2 000 000 = 47.5%."),
           ]),
        CODE(_t_dept, "text", title="Departmental income statement"),
        T("Footwear has lower sales but makes a **higher** net profit (320 000 against 230 000), because its margin is higher and it carries a smaller share of the costs. "
          "A fair basis matters: another basis would move profit from one department to the other. The owner should use the result as a guide, not as proof that one department should be closed. "
          "Costs that would remain even if a department were closed (for example rent) do not disappear."),
        MISTAKE("Sharing every expense equally",
                "Use a basis that reflects the use: rent by floor area, wages by staff or time, advertising by sales. Equal shares are only for expenses with no better basis."),
        MISTAKE("Apportioning stock figures",
                "Purchases and inventories belong to each department directly. They are not apportioned."),
        MISTAKE("Totals that do not agree",
                "Check that the departmental columns add to the total column and that the shared expenses allocated equal the expenses in the trial balance."),
        QUIZ("Which basis is the most suitable for apportioning rent between departments?",
             ["Sales of each department", "Floor area of each department", "Number of customers", "Closing inventory"], 1,
             "Rent is the cost of space, so floor area is the natural basis.",
             hint="What does rent pay for?",
             feedback=["Sales suits costs like advertising, not space.", "", "Customers do not measure the space used.", "Closing inventory does not measure the space used."]),
        QUIZ("Total shared expenses are FCFA 900 000, shared in the ratio 2 : 1. Department A's share is",
             ["FCFA 300 000", "FCFA 450 000", "FCFA 600 000", "FCFA 800 000"], 2,
             "2/3 × 900 000 = 600 000.",
             feedback=["That is the share of department B (1/3).", "That is half, used when shares are equal.", "", "That does not follow from a 2 : 1 ratio."], title="Quick check 2"),
        TIP("Departmental accounts belong to the final accounts section. Show your apportionment schedule with the basis for each expense, because this is where working marks are earned.",
            title="Exam link"),
        PQ("Rent FCFA 240 000 is shared by floor areas of 30 m² and 90 m². Find each department's share.",
           "Ratio 1 : 3. First department 60 000; second department 180 000."),
        PQ("Sales FCFA 1 000 000, cost of goods sold FCFA 600 000. Find the gross profit and the gross profit percentage.",
           "Gross profit 400 000; 400 000 ÷ 1 000 000 = 40%."),
        PQ("Gross profits are FCFA 400 000 and FCFA 300 000. Expenses allocated are FCFA 250 000 and FCFA 270 000. Find each department's net profit.",
           "400 000 − 250 000 = 150 000; 300 000 − 270 000 = 30 000."),
        PQ("Name a suitable basis for apportioning (a) electricity, (b) insurance of inventory.",
           "(a) floor area or machine hours; (b) value of average inventory held (any reasonable basis stated)."),
        SUM("Departmental accounts show the gross and net profit of each part of the business.",
            "Purchases and inventory belong to each department; shared expenses are apportioned on a suitable basis.",
            "The departmental figures must add up to the totals for the whole business.",
            "Use the results with care: apportionment is a choice, and some costs would remain if a department were closed."),
    ]))

# ====================================================================== 14. Examination: Paper 1
_p1_eq = 750_000 - 300_000
_p1_np = 900_000 - 540_000 - (210_000 - 10_000)
assert (_p1_eq, _p1_np) == (450_000, 160_000)
_p1_cogs = 120_000 + 800_000 - 150_000
assert _p1_cogs == 770_000

LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1: multiple-choice strategies for Principles of Accounts",
    slug="acc3-exam-paper-1-multiple-choice", minutes=22,
    summary="How Paper 1 works (50 multiple-choice questions, 1 hour 30 minutes), a time plan, the two-pass method, quick checks for calculation questions and the traps in accounting wording.",
    objectives=[
        "Describe Paper 1: 50 multiple-choice questions on the whole syllabus, all answered, 1 hour 30 minutes",
        "Plan the 90 minutes with a two-pass method and about 1.8 minutes a question on average",
        "Use elimination, estimation and quick checks (the accounting equation, debit equals credit) for calculation questions",
        "Avoid the common traps: sides of an account, gross and net, cost and market value, OHADA and IAS/IFRS wording",
    ],
    key_concepts=["Paper 1", "Two-pass method", "Elimination", "Estimation", "Quick checks", "OHADA and IAS/IFRS wording"],
    blocks=[
        H("What Paper 1 is"),
        T("Paper 1 is the multiple-choice paper. A candidate in a school in Buea opens it and finds fifty questions that run from accounting concepts to departmental accounts, with short calculations and "
          "questions on wording. This lesson is about how to collect those marks."),
        D("According to the Board's 2023 report, Paper 1 has **50 multiple-choice questions** covering the whole 0505 syllabus. All questions must be answered. "
          "The time allowed is **1 hour 30 minutes** and the paper is worth **40%** of the marks for the whole examination. Paper 2 is worth 60%.", title="Paper 1: the official facts"),
        TIP("The questions can come from any part of the syllabus: concepts and double entry, documents and books of original entry, cash books and bank reconciliation, control accounts, errors and payroll, "
            "end-of-year adjustments and inventory, and final accounts and specialised accounts. The 2023 report says candidates often did not master the whole syllabus, so do not leave a module out.", title="Exam link"),
        H("A time plan"),
        T("90 minutes divided by 50 questions is **1.8 minutes** a question. Word questions take about 30 seconds. Calculation questions may take three minutes. Do the quick ones first and bank the time."),
        KEY("The two-pass method",
            "This is KKEVO study advice, not an official rule.",
            cards=[["Pass 1 (about 55 minutes)", "Answer every question you can do within about two minutes. Mark the others and move on."],
                   ["Pass 2 (about 25 minutes)", "Return to the marked questions. Use elimination and the quick checks below."],
                   ["Check (about 10 minutes)", "Make sure every question has an answer. Re-read words such as not, except, gross, net, debit and credit."]]),
        H("Quick checks for calculation questions"),
        D("**The accounting equation**: assets = capital + liabilities. **Double entry**: total debits = total credits. **Net profit** = incomes − expenses (after adjustments). "
          "**Net book value** = cost − accumulated depreciation. **Cost of goods sold** = opening inventory + purchases − closing inventory. Check each answer against the equation that applies.", title="Four anchors"),
        EX("Worked example 1: use the accounting equation",
           intro="Assets are FCFA 750 000 and liabilities FCFA 300 000. The options are: A 1 050 000; B 450 000; C 300 000; D 750 000. Which is the capital?",
           steps=[
               S("Write the equation", text="Capital = assets − liabilities."),
               S("Calculate", text="750 000 − 300 000 = 450 000."),
               S("Check the options", text="A adds the figures; C and D copy a figure from the question. The answer is B."),
           ]),
        EX("Worked example 2: adjusting before the answer",
           intro="Sales FCFA 900 000, cost of goods sold FCFA 540 000, expenses paid FCFA 210 000 including FCFA 10 000 prepaid. What is the net profit?",
           steps=[
               S("Adjust the expense", text="Expense for the year = 210 000 − 10 000 = 200 000."),
               S("Calculate", text="900 000 − 540 000 − 200 000 = 160 000."),
               S("Trap", text="The distractor 150 000 ignores the prepayment (900 000 − 540 000 − 210 000)."),
           ]),
        EX("Worked example 3: reading the sides",
           intro="Which account is debited when a customer returns goods that were sold on credit?",
           steps=[
               S("What is being recorded?", text="The goods come back, so sales are reduced (Returns inwards is debited) and the customer owes less."),
               S("Entry", text="Debit Returns inwards; credit the customer's account (trade receivables)."),
               S("Elimination", text="An option that debits the customer's account is wrong: the customer owes less, so the account is credited."),
           ]),
        H("Traps in the wording"),
        CODE("""OHADA term               IAS/IFRS term
Compte de resultat       Statement of profit or loss
Bilan                    Statement of financial position
Marge commerciale        Gross profit
Amortissement            Depreciation
Stock                    Inventory
Creances clients         Trade receivables
Fournisseurs             Trade payables
Capitaux propres         Equity
Charges a payer          Accrued expenses
Charges constatees
  d'avance               Prepaid expenses""", "text", title="Two sets of words for the same ideas"),
        T("Paper 1 may use either set of words. If you see 'gross profit' or 'commercial margin', know that they are the same figure. If you see 'inventory' or 'stock', the idea is the same. "
          "The Board's report says the syllabus is bi-cultural (OHADA and IAS/IFRS) and that candidates should master both approaches."),
        MISTAKE("Choosing the first option that matches a figure in the question",
                "Distractors are built from the figures in the question. Always do the calculation, then compare."),
        MISTAKE("Mixing up debit and credit for liabilities and incomes",
                "Assets and expenses increase on the debit side. Liabilities, capital and incomes increase on the credit side."),
        MISTAKE("Ignoring the adjustment in a profit question",
                "Accruals, prepayments, depreciation and provisions change the profit. Check the question for adjustments before calculating."),
        QUIZ("Paper 1 has 50 questions and lasts 90 minutes. The average time for each question is",
             ["1.5 minutes", "1.8 minutes", "2 minutes", "3 minutes"], 1,
             "90 ÷ 50 = 1.8 minutes.",
             hint="Divide the time by the number of questions.",
             feedback=["That would give 75 minutes in total.", "", "That would take 100 minutes in total.", "That would take 150 minutes in total."]),
        QUIZ("Assets are FCFA 1 200 000 and capital FCFA 700 000. The liabilities are",
             ["FCFA 1 900 000", "FCFA 700 000", "FCFA 500 000", "FCFA 1 200 000"], 2,
             "Liabilities = assets − capital = 500 000.",
             feedback=["That adds the two figures.", "That copies the capital.", "", "That copies the assets."], title="Quick check 2"),
        PQ("State two official facts about Paper 1.", "It has 50 multiple-choice questions on the whole syllabus (all answered), it lasts 1 hour 30 minutes and it carries 40% of the marks."),
        PQ("Cost of goods sold: opening inventory FCFA 120 000, purchases FCFA 800 000, closing inventory FCFA 150 000. Find it.", "120 000 + 800 000 − 150 000 = 770 000."),
        PQ("Which statement is the IAS/IFRS name for the bilan?", "The statement of financial position."),
        PQ("Give one benefit of the two-pass method.", "You collect the easy marks first, and you keep time for the harder questions without getting stuck."),
        SUM("Paper 1: 50 multiple-choice questions, all answered, 1 hour 30 minutes, 40% of the marks, whole syllabus.",
            "Plan the time: about 1.8 minutes a question on average; two passes and a final check.",
            "Use the accounting equation, debit equals credit and the adjustments as quick checks.",
            "Know both OHADA and IAS/IFRS wording."),
    ]))

# ====================================================================== 15. Examination: Paper 2
_bk_cb, _bk_chg, _bk_dis, _bk_so = 380_000, 5_000, 20_000, 15_000
_bk_upd = _bk_cb - _bk_chg - _bk_dis - _bk_so
_bk_stmt, _bk_unp, _bk_unc = 420_000, 100_000, 20_000
assert _bk_upd == 340_000 and _bk_stmt - _bk_unp + _bk_unc == _bk_upd
_t_cbu = "\n".join([
    "Updated cash book (bank column)",
    r("Balance per cash book (Dr)", _bk_cb, w=34),
    r("Less bank charges", -_bk_chg, w=34),
    r("Less dishonoured cheque", -_bk_dis, w=34),
    r("Less standing order", -_bk_so, w=34),
    r("Updated cash book balance", None, _bk_upd, w=34),
])
_t_brs = "\n".join([
    "Bank reconciliation statement",
    r("Balance per bank statement", _bk_stmt, w=34),
    r("Less unpresented cheques", -_bk_unp, w=34),
    r("Add lodgements not yet credited", _bk_unc, w=34),
    r("Balance per updated cash book", None, _bk_stmt - _bk_unp + _bk_unc, w=34),
])
# stock slip: weighted average after all entries (period average)
_wa_units = 200 + 300
_wa_cost = 200 * 500 + 300 * 600
_wa_avg = _wa_cost // _wa_units
_wa_issue = 350 * _wa_avg
_wa_close = (_wa_units - 350) * _wa_avg
assert (_wa_cost, _wa_avg, _wa_issue, _wa_close) == (280_000, 560, 196_000, 84_000) and _wa_cost % _wa_units == 0
_t_slip = "\n".join([
    "Receipts: 200 @ 500 = 100 000; 300 @ 600 = 180 000",
    "Total: 500 units, cost 280 000",
    "Average = 280 000 / 500 = 560",
    "Issues: 350 x 560 = 196 000",
    "Closing: 150 x 560 = 84 000",
    "Check: 196 000 + 84 000 = 280 000",
])

LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2: choosing questions, presenting working and using both approaches",
    slug="acc3-exam-paper-2-structure-and-working", minutes=26,
    summary="How Paper 2 is set (eight questions, Section A OHADA any three, Section B IAS/IFRS any two, 3 hours), the topics the Board's report lists, a time plan, presentation of working and the mistakes the examiners noticed.",
    objectives=[
        "State the structure of Paper 2: eight questions of 20 marks, Section A (five OHADA, answer any three) and Section B (three IAS/IFRS, answer any two), 3 hours",
        "Choose questions by strength and plan about 32 minutes for each of five answers",
        "Present working in clear statements and schedules with labelled totals",
        "Avoid the errors named in the Board's report: transposed bank reconciliation, reducing balance, weighted average after all entries, control accounts and non-profit accounts",
    ],
    key_concepts=["Paper 2", "Section A and Section B", "OHADA and IAS/IFRS", "Working", "Bank reconciliation", "Weighted average", "Control accounts"],
    blocks=[
        H("What Paper 2 is"),
        T("Paper 2 is the written paper. The Board's 2023 report calls its questions problem-solving questions. You choose which to attempt, you show every step, and you must be able to work in both the OHADA and the IAS/IFRS approaches."),
        D("Paper 2 has **eight questions** drawn from the whole syllabus. **Section A** has five questions on the **OHADA approach**; answer **any three**. "
          "**Section B** has three questions on the **IAS/IFRS approach**; answer **any two**. Each question carries **20 marks**. "
          "The paper lasts **3 hours** and carries **60%** of the marks. A candidate who answers more questions than required is not penalised, but the best answers in each section are counted.", title="Paper 2: the official facts"),
        IMG("f5acc3-paper2-plan.svg", alt="A bar showing 10 minutes to read, five blocks of 32 minutes for the answers, and 10 minutes to check.",
            caption="Figure 1. One way to plan the 3 hours (KKEVO study advice, not an official rule)."),
        H("What the 2023 report says was tested"),
        T("The Board's report lists the topics of the eight questions in the 2023 session: accounting terminology and depreciation; inventory costing methods; end-of-year adjustments with a bank reconciliation; "
          "payroll; trading transactions with an invoice; final accounts of a sole trader (the income statement); accounting for non-profit organisations; and control accounts. "
          "The questions were spread across the whole syllabus. Do not guess which topics will come: revise them all."),
        KEY("What examiners noticed",
            "From the Board's 2023 report. These are the errors to avoid.",
            cards=[["Bank reconciliation", "Some candidates transposed the entries, putting the business's bank account entries into the bank statement and the reverse."],
                   ["Depreciation", "Many could not apply the reducing balance method."],
                   ["Inventory costing", "Many could not calculate the average cost for the period (weighted average after all entries)."],
                   ["Control accounts", "Some included cash sales and cash purchases, did not treat contra items properly, and mishandled the balances given."],
                   ["Payroll", "Overtime rates were not understood; some candidates had not covered the topic."],
                   ["Non-profit organisations", "The most avoided question; do not skip the topic."]]),
        T("The report also says that popular questions were not always the best answered: one of the most popular questions had one of the lowest pass rates. Choose the questions you can do best, not the ones everyone chooses."),
        H("Presenting working"),
        D("Examiners can only give marks for what they can see. Use headings, a column for the figures, labelled totals and a short working for each adjustment. "
          "A correct method with one slip still earns marks; a bare wrong answer earns none.", title="Working earns marks"),
        EX("Worked example 1: a bank reconciliation done in the right order",
           intro="The cash book (bank column) shows a debit balance of FCFA 380 000. The statement shows FCFA 420 000. Not in the cash book: bank charges FCFA 5 000, a dishonoured cheque FCFA 20 000 and a standing order FCFA 15 000. "
                 "Cheques of FCFA 100 000 are unpresented and FCFA 20 000 of lodgements are not yet credited. Reconcile.",
           steps=[
               S("Update the cash book first", text="380 000 − 5 000 − 20 000 − 15 000 = 340 000."),
               S("Start from the bank statement balance", text="420 000 − 100 000 unpresented cheques + 20 000 lodgements not credited = 340 000."),
               S("Check", text="Both give 340 000. If they differ, one of the signs is wrong."),
           ]),
        CODE(_t_cbu + "\n\n" + _t_brs, "text", title="Bank reconciliation (invented for practice)"),
        EX("Worked example 2: a stock slip with the weighted average after all entries",
           intro="Receipts: 200 units at FCFA 500 and 300 units at FCFA 600. Issues total 350 units. Find the average cost, the value of the issues and the closing inventory.",
           steps=[
               S("Total cost and units", text="200 × 500 + 300 × 600 = 100 000 + 180 000 = 280 000 for 500 units."),
               S("Average", text="280 000 ÷ 500 = 560."),
               S("Issues and closing stock", text="350 × 560 = 196 000. Closing 150 × 560 = 84 000. Total 280 000."),
           ]),
        CODE(_t_slip, "text", title="Stock slip working"),
        EX("Worked example 3: planning the paper",
           intro="You have 180 minutes. You plan 10 minutes for reading and choosing, 10 minutes for checking, and equal time for five answers. How long is each answer?",
           steps=[
               S("Time for answers", text="180 − 10 − 10 = 160 minutes."),
               S("Per answer", text="160 ÷ 5 = 32 minutes."),
               S("Adjust", text="If one question is calculation-heavy (final accounts), take a few minutes from a shorter question, but never leave a question blank."),
           ]),
        H("Both approaches"),
        T("Section A uses OHADA wording (compte de résultat, bilan, amortissement, charges à payer). Section B uses IAS/IFRS wording (statement of profit or loss, statement of financial position, depreciation, accrued expenses). "
          "The ideas are the same, so learn the equivalent words. The Board's report recommends that teachers and students master both approaches."),
        MISTAKE("Starting with a question that you cannot finish",
                "Spend two minutes at the start choosing. A question that begins well and then stops loses more than a question you can complete."),
        MISTAKE("Giving a bare answer",
                "Write the formula or the working in a column. Even a slip in addition still earns method marks."),
        MISTAKE("Mixing the sides in a reconciliation",
                "Update the cash book first, then reconcile from the statement balance. Bank statement entries are the bank's view, which is the opposite of the cash book."),
        QUIZ("How many questions must a candidate answer in Paper 2 (any section)?",
             ["Five: any three from Section A and any two from Section B", "All eight", "Three from each section", "Any five from either section"], 0,
             "The report states: Section A, five OHADA questions, answer any three; Section B, three IAS/IFRS questions, answer any two.",
             hint="Add the numbers from each section.",
             feedback=["", "All eight are not required.", "Section B only requires two.", "The rule is fixed by section."]),
        QUIZ("A reconciliation starts with the bank statement at FCFA 500 000. Unpresented cheques are FCFA 80 000 and lodgements not credited are FCFA 30 000. The cash book balance should be",
             ["FCFA 450 000", "FCFA 550 000", "FCFA 610 000", "FCFA 420 000"], 0,
             "500 000 − 80 000 + 30 000 = 450 000.",
             feedback=["", "That adds the cheques and subtracts the lodgements: wrong way round.", "That adds both.", "That subtracts both."], title="Quick check 2"),
        TIP("In Paper 2 each question carries 20 marks. The Board's report does not give mark splits inside questions, so always write the working for every part.", title="Exam link"),
        PQ("State the number of questions in Paper 2 and how many you must answer from each section.", "Eight questions. Any three from Section A (five OHADA questions) and any two from Section B (three IAS/IFRS questions)."),
        PQ("Why is it unwise to choose a question only because it is popular?", "A question can be popular and still be badly answered. Choose the topics where you can complete the working."),
        PQ("Cash book balance FCFA 200 000; bank charges not recorded FCFA 4 000. Find the updated cash book balance.", "200 000 − 4 000 = 196 000."),
        PQ("Receipts: 100 units at FCFA 200 and 100 units at FCFA 300; 150 units are issued. Find the average cost and the value of the closing inventory (weighted average after all entries).",
           "Total cost 50 000 for 200 units; average 250. Closing 50 × 250 = 12 500."),
        SUM("Paper 2: eight questions of 20 marks; Section A five OHADA (any three), Section B three IAS/IFRS (any two); 3 hours; 60%.",
            "Plan about 32 minutes for each of five answers, with time to read at the start and check at the end.",
            "Show working, label totals, and know the equivalent OHADA and IAS/IFRS words.",
            "Learn the errors the report names: bank reconciliation, reducing balance, average cost, control accounts, payroll overtime and non-profit accounts."),
    ]))
