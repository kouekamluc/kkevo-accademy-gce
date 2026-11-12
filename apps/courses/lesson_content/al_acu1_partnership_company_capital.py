"""Upper Sixth Accounting (A Level 0705): Partnership Accounting; Company Formation, Share Capital & Debentures;
Modification of Capital, Taxation, Amalgamation & Liquidation.

Draft content written from KKEVO's curriculum blueprint (ACC-0705-U6M1 to U6M3) and the GCE Board's 2023 Advanced Level
subject report. Exam facts stated are only those of the report: three papers weighted 30, 30 and 40; Paper 1 = 50
multiple-choice questions (in 2023: 25 financial accounting, 10 cost and management accounting, 15 company accounting and
taxation); Paper 2 = Cost and Management Accounting; Paper 3 = Financial Accounting, with a Section B on company accounting
and taxation.

OHADA company law facts are given only where they are well established (Uniform Act on commercial companies: SA minimum
capital FCFA 10 000 000, quarter of the nominal value of cash shares paid on subscription and the rest within three years,
legal reserve of one tenth of the profit until it reaches one fifth of the capital). Cameroon tax rates (company tax,
minimum tax, IRCM) are TEACHING VALUES labelled "check the current Finance Law and your textbook". SYSCOHADA account
numbers are the usual textbook ones; textbooks differ, so the lessons say "check your textbook" where it matters.
All FCFA figures are invented for practice. EVERY figure is computed in this file with plain Python integer or Fraction
arithmetic and checked with assertions (ledgers and journals balance), so printed totals cannot disagree with the workings.
"""

from fractions import Fraction as Fr

from .dsl import *  # noqa: F403

COURSE = ("accounting", "upper-sixth")

M_PART = "Partnership Accounting"
M_COMP = "Company Formation, Share Capital & Debentures"
M_MOD = "Modification of Capital, Taxation, Amalgamation & Liquidation"


# ---------------------------------------------------------------- small formatting helpers (all arithmetic is exact)
def n(x):
    """12345 -> '12 345'; Fractions must be whole numbers; negatives keep a minus sign."""
    if isinstance(x, Fr):
        assert x.denominator == 1, x
        x = int(x)
    assert x == int(x), x
    x = int(x)
    s = f"{abs(x):,}".replace(",", " ")
    return ("-" if x < 0 else "") + s


def r(label, a=None, b=None, w=30, c=12):
    """One aligned statement line with up to two money columns."""
    fa = "" if a is None else (a if isinstance(a, str) else n(a))
    fb = "" if b is None else (b if isinstance(b, str) else n(b))
    assert len(label) <= w, label
    return f"{label:<{w}}{fa:>{c}}{fb:>{c}}".rstrip()


def split(amount, ratio):
    """Share `amount` in `ratio` exactly (asserts whole francs)."""
    t = sum(ratio)
    out = [Fr(amount * k, t) for k in ratio]
    assert all(x.denominator == 1 for x in out), (amount, ratio)
    return [int(x) for x in out]


def ledger(title, dr, cr):
    """Stacked ledger account: debit side then credit side, both totalled; asserts that the two totals agree."""
    td, tc = sum(a for _, a in dr), sum(a for _, a in cr)
    assert td == tc, (title, td, tc)
    assert all(len(l) <= 32 for l, _ in dr + cr), (dr, cr)
    out = [title, "DEBIT"]
    out += [f"  {l:<32}{n(a):>12}" for l, a in dr]
    out += [f"  {'Total':<32}{n(td):>12}", "CREDIT"]
    out += [f"  {l:<32}{n(a):>12}" for l, a in cr]
    out += [f"  {'Total':<32}{n(tc):>12}"]
    return "\n".join(out)


def journal(entries):
    """entries: list of (heading, [(debit account, amount)], [(credit account, amount)]); asserts debits = credits."""
    out = []
    for head, dr, cr in entries:
        assert sum(a for _, a in dr) == sum(a for _, a in cr), (head, dr, cr)
        assert all(len(l) <= 36 for l, _ in dr) and all(len(l) <= 32 for l, _ in cr), (dr, cr)
        out.append(head)
        out += [f"Dr {l:<36}{n(a):>12}" for l, a in dr]
        out += [f"     Cr {l:<32}{n(a):>14}" for l, a in cr]
        out.append("")
    return "\n".join(out).rstrip()


def columns(title, names, dr, cr, w=26, c=11, bal_label="Balance c/d"):
    """Columnar partners' account. dr/cr: lists of (label, [amounts per partner or None]).
    Adds 'Balance c/d' on the side that balances each column; returns (text, closing balances: + = credit)."""
    k = len(names)
    sd = [sum((row[i] or 0) for _, row in dr) for i in range(k)]
    sc = [sum((row[i] or 0) for _, row in cr) for i in range(k)]
    bal = [sc[i] - sd[i] for i in range(k)]
    dr = dr + [(bal_label, [b if b > 0 else None for b in bal])]
    cr = cr + [("Balance c/d (debit)", [-b if b < 0 else None for b in bal])] if any(b < 0 for b in bal) else cr
    tot = [max(sd[i], sc[i]) for i in range(k)]

    def line(label, row):
        assert len(label) < w, label
        return (f"{label:<{w}}" + "".join(f"{('' if v is None else n(v)):>{c}}" for v in row)).rstrip()

    out = [title, f"{'':<{w}}" + "".join(f"{x:>{c}}" for x in names), "DEBIT"]
    out += [line(" " + l, row) for l, row in dr]
    out.append(line(" Total", tot))
    out.append("CREDIT")
    out += [line(" " + l, row) for l, row in cr]
    out.append(line(" Total", tot))
    return "\n".join(out), bal


LESSONS = []

# ====================================================================== 1. Appropriation of profits and partners' accounts
_names1 = ["Ndi", "Ayuk", "Fon"]
_cap1 = [6_000_000, 4_000_000, 2_000_000]
_ioc1 = [c * 10 // 100 for c in _cap1]
_draw1 = [2_400_000, 1_600_000, 1_200_000]
_iod1 = [d * 10 // 100 // 2 for d in _draw1]          # drawn evenly: half a year on average
_sal1 = [0, 0, 1_200_000]
_np1 = 9_040_000
_resid1 = _np1 + sum(_iod1) - sum(_sal1) - sum(_ioc1)
_sh1 = split(_resid1, [3, 2, 1])
assert _ioc1 == [600_000, 400_000, 200_000] and _iod1 == [120_000, 80_000, 60_000]
assert _resid1 == 6_900_000 and _sh1 == [3_450_000, 2_300_000, 1_150_000]
_t_app1 = "\n".join([
    "NAF Building Supplies: profit and loss appropriation",
    r("Net profit for the year", None, _np1),
    r("Add interest on drawings:"),
    *[r(f"  {nm}", v) for nm, v in zip(_names1, _iod1)],
    r("", None, sum(_iod1)),
    r("", None, _np1 + sum(_iod1)),
    r("Less salary: Fon", None, _sal1[2]),
    r("Less interest on capital:"),
    *[r(f"  {nm}", v) for nm, v in zip(_names1, _ioc1)],
    r("", None, sum(_ioc1)),
    r("Residual profit", None, _resid1),
    r("Shared 3:2:1"),
    *[r(f"  {nm}", v) for nm, v in zip(_names1, _sh1)],
    r("", None, sum(_sh1)),
])
_open1 = [500_000, 300_000, -100_000]          # + credit, - debit
_t_cur1, _bal1 = columns(
    "Current accounts", _names1,
    [("Balance b/d (debit)", [None, None, 100_000]), ("Drawings", _draw1), ("Interest on drawings", _iod1)],
    [("Balance b/d", [500_000, 300_000, None]), ("Interest on capital", _ioc1), ("Salary", [None, None, 1_200_000]),
     ("Share of residual profit", _sh1)])
assert _bal1 == [2_030_000, 1_320_000, 1_190_000]
assert [_open1[i] + _ioc1[i] + _sal1[i] + _sh1[i] - _draw1[i] - _iod1[i] for i in range(3)] == _bal1
# guaranteed minimum for Fon
_fon_total = _sal1[2] + _ioc1[2] + _sh1[2]
_short = 3_000_000 - _fon_total
_bear = split(_short, [3, 2])
assert _fon_total == 2_550_000 and _short == 450_000 and _bear == [270_000, 180_000]
# example 3: dated drawings (product method)
_dated = [(600_000, 10), (600_000, 6), (400_000, 3)]
_iod_dated = [Fr(a * 10 * m, 100 * 12) for a, m in _dated]
assert _iod_dated == [50_000, 30_000, 10_000] and sum(_iod_dated) == 90_000
# practice-question figures
assert 5_000_000 * 5 // 100 == 250_000
_pq_res = -1_800_000 + 0 - 2_000_000 - 600_000
assert _pq_res == -4_400_000 and split(-_pq_res, [1, 1]) == [2_200_000, 2_200_000]
assert [_sh1[0] - _bear[0], _sh1[1] - _bear[1], _sh1[2] + _short] == [3_180_000, 2_120_000, 1_600_000]
assert sum(range(12)) == 66 and Fr(300_000 * 12 * 66, 100 * 12) == 198_000
assert 5_000_000 + 200_000 - 1_400_000 - 1_000_000 == 2_800_000 and 5_000_000 - 1_400_000 - 1_000_000 == 2_600_000
assert 5_000_000 - 200_000 - 1_400_000 - 1_000_000 == 2_400_000 and 5_000_000 + 200_000 - 1_400_000 == 3_800_000

LESSONS.append(lesson(
    module=M_PART, topic="Appropriation of profits and partners' accounts",
    title="Partnership appropriation account, capital and current accounts",
    slug="acu1-partnership-appropriation", minutes=25,
    summary="Share a partnership's profit as the deed says: interest on capital and drawings, salaries, residual profit in the profit-sharing "
            "ratio and any guaranteed minimum; then write up fixed capital accounts and current accounts.",
    objectives=[
        "State what a partnership deed covers and the rules textbooks apply when there is no deed",
        "Prepare a profit and loss appropriation account with interest on capital, interest on drawings, salaries and residual profit",
        "Calculate interest on drawings from dates and amounts, and deal with a guaranteed minimum share",
        "Write up columnar capital and current accounts under the fixed capital method",
    ],
    key_concepts=["Partnership deed", "Appropriation account", "Interest on capital", "Interest on drawings",
                  "Partner's salary", "Profit-sharing ratio", "Fixed and fluctuating capital", "Current account",
                  "Guaranteed minimum profit"],
    blocks=[
        H("Why partners need an appropriation account"),
        T("Three friends, Ndi, Ayuk and Fon, run a building-materials shop in Bamenda. Ndi put in the most money, Fon works full time in "
          "the shop, and Ayuk helps at weekends. A fair share of profit must reward **money**, **work** and **risk** separately. "
          "The **profit and loss appropriation account** does this. It starts from the net profit and shows exactly where every franc goes. "
          "All figures in this lesson are **invented for practice**."),
        D("A **partnership** is a business owned by two or more persons who share its profits and losses. In OHADA law the general "
          "partnership is the **société en nom collectif (SNC)**, whose partners are personally liable, jointly and severally, for its debts.",
          title="Partnership"),
        D("The **partnership deed** (or agreement) is the written contract between the partners. It usually states: the capital each "
          "partner contributes, the profit-sharing ratio, interest on capital and on drawings and their rates, partners' salaries, "
          "interest on partners' loans, limits on drawings, and what happens on admission, retirement, death or dissolution.",
          title="Partnership deed"),
        KEY("When there is no agreement", "Most A Level textbooks apply the default rules of the English Partnership Act 1890. "
            "Check your textbook and your teacher's notes, because Cameroon's commercial law is OHADA law.",
            cards=[["Profits and losses", "Shared equally."],
                   ["Interest on capital", "None."],
                   ["Salaries", "None."],
                   ["Interest on drawings", "None."],
                   ["Partner's loan", "Interest at 5% a year."]]),
        H("The appropriation account"),
        KEY("Order of the appropriation account", "Start with net profit, then:",
            cards=[["Add", "Interest charged on drawings (partners pay it to the firm)."],
                   ["Deduct", "Partners' salaries and interest on capital (rewards for work and money)."],
                   ["Share", "The residual profit (or loss) in the profit-sharing ratio."]]),
        IMG("alacu1-appropriation-flow.svg",
            alt="Flow diagram: net profit plus interest on drawings, less salaries and interest on capital, leaves residual profit shared in the profit-sharing ratio; all items go to the partners' current accounts.",
            caption="Figure 1. The appropriation account divides the profit; every item ends in a partner's current account."),
        D("**Interest on a partner's loan** is not an appropriation. It is an expense of the business, charged in the income statement "
          "**before** net profit is found, because the partner is acting as a lender.", title="Loan interest is different"),
        EX("Worked example 1: the appropriation account",
           intro="Ndi, Ayuk and Fon have fixed capitals of FCFA 6 000 000, 4 000 000 and 2 000 000. The deed allows interest on capital at "
                 "10% a year, a salary of FCFA 1 200 000 to Fon, interest on drawings at 10% a year, and residual profit in the ratio 3:2:1. "
                 "Drawings, taken evenly through the year, were 2 400 000, 1 600 000 and 1 200 000. Net profit is FCFA 9 040 000.",
           steps=[
               S("Interest on capital (10%)", text="600 000, 400 000 and 200 000: total 1 200 000."),
               S("Interest on drawings", text="Drawings taken evenly are outstanding for half a year on average: 10% × 2 400 000 × 6/12 = 120 000; "
                                             "Ayuk 80 000; Fon 60 000. Total 260 000."),
               S("Residual profit", text="9 040 000 + 260 000 − 1 200 000 (salary) − 1 200 000 (interest on capital) = 6 900 000."),
               S("Share 3:2:1", text="6 900 000 ÷ 6 = 1 150 000 per part: Ndi 3 450 000, Ayuk 2 300 000, Fon 1 150 000."),
           ]),
        CODE(_t_app1, "text", title="Appropriation account (invented for practice)"),
        H("Capital and current accounts"),
        D("Under the **fixed capital method** the capital accounts show only the agreed capital; salaries, interest, profit shares and drawings "
          "go to a separate **current account** for each partner. Under the **fluctuating capital method** there are no current accounts and all "
          "these items go straight to the capital accounts, so capital changes every year.", title="Fixed and fluctuating capital"),
        EX("Worked example 2: current accounts",
           intro="Continue example 1. At the start of the year the current accounts were: Ndi FCFA 500 000 credit, Ayuk 300 000 credit, "
                 "Fon 100 000 debit (Fon had overdrawn). Prepare the current accounts.",
           steps=[
               S("Credit side (what the firm owes the partner)", text="Opening credit balances, interest on capital, salary, share of residual profit."),
               S("Debit side (what the partner has taken)", text="Opening debit balance, drawings, interest on drawings."),
               S("Ndi", text="500 000 + 600 000 + 3 450 000 − 2 400 000 − 120 000 = 2 030 000 credit."),
               S("Fon", text="200 000 + 1 200 000 + 1 150 000 − 100 000 − 1 200 000 − 60 000 = 1 190 000 credit. Ayuk: 1 320 000 credit."),
           ]),
        CODE(_t_cur1, "text", title="Columnar current accounts (invented for practice)"),
        EX("Worked example 3: guaranteed minimum share",
           intro="Suppose the deed also guarantees Fon a total of at least FCFA 3 000 000 a year (salary + interest + share), with any shortfall "
                 "borne by Ndi and Ayuk in their profit-sharing ratio 3:2.",
           steps=[
               S("Fon's total", text="1 200 000 + 200 000 + 1 150 000 = 2 550 000."),
               S("Shortfall", text="3 000 000 − 2 550 000 = 450 000."),
               S("Borne 3:2", text="Ndi 270 000 and Ayuk 180 000 less; Fon 450 000 more. Residual shares become 3 180 000, 2 120 000 and 1 600 000."),
           ], check=r"3\,180\,000 + 2\,120\,000 + 1\,600\,000 = 6\,900\,000"),
        T("**Interest on drawings from dates.** When drawings are dated, charge each one for the months from its date to the year end. "
          "Example: year end 31 December, rate 10%. Drawings of 600 000 on 1 March (10 months), 600 000 on 1 July (6 months) and 400 000 on "
          "1 October (3 months) give 50 000 + 30 000 + 10 000 = **90 000**."),
        MISTAKE("Putting loan interest in the appropriation account",
                "Interest on a partner's loan is an expense that reduces net profit. Only interest on capital, interest on drawings, salaries and "
                "profit shares belong in the appropriation account."),
        MISTAKE("Adding interest on drawings to the partner",
                "Interest on drawings is a charge **against** the partner: debit the current account and add it to the profit available for sharing."),
        MISTAKE("Sharing net profit instead of residual profit",
                "Salaries and interest on capital come first. Only what is left (residual profit) is shared in the profit-sharing ratio. "
                "The Board's 2023 report asks teachers to teach the approach and format of accounts: label every line."),
        QUIZ("A partner lent the firm FCFA 2 000 000 at 10% a year. Where is the interest of 200 000 recorded?",
             ["In the appropriation account, as a deduction before residual profit", "In the income statement, as an expense before net profit",
              "On the debit side of the partner's current account", "In the capital account as extra capital"], 1,
             "The partner acts as a lender, so the interest is an expense of the business (and is credited to the partner's loan or current account).",
             hint="Is the partner acting as an owner or as a lender here?",
             feedback=["Only rewards to partners as owners are appropriations.", "",
                       "The partner receives the interest, so it is credited to the partner, not debited.",
                       "Interest is income to the partner, not new capital."]),
        QUIZ("Net profit 5 000 000; interest on capital 1 400 000; salaries 1 000 000; interest on drawings 200 000. What is the residual profit?",
             ["2 400 000", "2 600 000", "2 800 000", "3 800 000"], 2,
             "5 000 000 + 200 000 − 1 400 000 − 1 000 000 = 2 800 000.",
             hint="Interest on drawings increases the amount to share.",
             feedback=["This subtracts interest on drawings instead of adding it.",
                       "This ignores interest on drawings altogether.", "",
                       "This forgets to deduct the salaries."], title="Quick check 2"),
        TIP("Partnership accounts can appear in Paper 1 multiple choice and in the Financial Accounting paper (Paper 3). "
            "Set out the appropriation account in the vertical format with labels, then the columnar current accounts.", title="Exam link"),
        PQ("Two partners, Eta and Mua, share profits equally with no deed. Mua lent the firm FCFA 5 000 000 at the start of the year. "
           "Using the textbook default rules, how much loan interest does Mua receive, and where is it shown?",
           "Default rate 5% a year: 5% × 5 000 000 = 250 000. It is an expense in the income statement (credited to Mua's loan or current account), "
           "not an appropriation."),
        PQ("Ebot and Ngo share profits 1:1 after interest on capital (Ebot 1 200 000, Ngo 800 000) and a salary of 600 000 to Ngo. "
           "The firm made a net loss of FCFA 1 800 000. Find each partner's share of the residual loss.",
           "Residual = −1 800 000 − 1 200 000 − 800 000 − 600 000 = −4 400 000. Each partner bears 2 200 000. "
           "Interest and salary are still credited because the deed says so; the loss is shared after them."),
        PQ("A partner drew FCFA 300 000 at the end of each month (12 drawings) and interest on drawings is 12% a year. Find the interest on drawings.",
           "Each drawing is outstanding for 11, 10, ..., 0 months: 66 months in total. Interest = 300 000 × 12% × 66/12 = 198 000 "
           "(equivalent to charging the total of 3 600 000 for an average of 5.5 months)."),
        PQ("Explain two advantages of keeping fixed capital accounts with separate current accounts.",
           "1. The capital agreed in the deed stays visible, so interest on capital is easy to calculate. "
           "2. The current account shows clearly whether a partner has drawn more than his or her share of profit (a debit balance), "
           "which helps the partners control drawings."),
        SUM("The deed sets capital, ratio, interest, salaries and drawings rules; without one, textbooks use the 1890 Act defaults (equal shares, 5% on loans).",
            "Appropriation: net profit + interest on drawings − salaries − interest on capital = residual profit shared in the ratio.",
            "Interest on a partner's loan is an expense before net profit, not an appropriation.",
            "Fixed capital method: capital accounts stay fixed; current accounts take the appropriations and drawings.",
            "A guaranteed minimum is topped up by the other partners in the ratio the deed states."),
    ]))

# ====================================================================== 2. Revaluation and goodwill
_pr2 = [4_200_000, 4_800_000, 5_400_000]
_avg2 = Fr(sum(_pr2), 3)
_gw_avg = _avg2 * 2
_wavg2 = Fr(sum(p * w for p, w in zip(_pr2, [1, 2, 3])), 6)
_gw_w = _wavg2 * 2
_normal2 = 20_000_000 * 15 // 100
_super2 = _avg2 - _normal2
_gw_sp = _super2 * 3
_gw_cap = _super2 / Fr(15, 100)
assert (_avg2, _gw_avg, _wavg2, _gw_w) == (4_800_000, 9_600_000, 5_000_000, 10_000_000)
assert (_normal2, _super2, _gw_sp, _gw_cap) == (3_000_000, 1_800_000, 5_400_000, 12_000_000)
_t_gw = "\n".join([
    "Profits: 4 200 000 (yr 1), 4 800 000 (yr 2), 5 400 000 (yr 3)",
    "",
    "Method 1: average profit x 2 years' purchase",
    r("  Average = 14 400 000 / 3", n(_avg2), w=38),
    r("  Goodwill = 4 800 000 x 2", n(_gw_avg), w=38),
    "Method 2: weighted average (weights 1, 2, 3) x 2",
    r("  Weighted = 30 000 000 / 6", n(_wavg2), w=38),
    r("  Goodwill = 5 000 000 x 2", n(_gw_w), w=38),
    "Method 3: super profit x 3 years' purchase",
    r("  Normal profit 15% x 20 000 000", n(_normal2), w=38),
    r("  Super profit 4 800 000 - 3 000 000", n(_super2), w=38),
    r("  Goodwill = 1 800 000 x 3", n(_gw_sp), w=38),
])
assert sum(p * w for p, w in zip(_pr2, [1, 2, 3])) == 30_000_000
_rev = {"Premises": (10_000_000, 12_000_000), "Equipment": (3_000_000, 2_600_000), "Inventory": (2_500_000, 2_350_000)}
_allow_old, _allow_new = 50_000, 2_000_000 * 5 // 100
_net_rev = sum(b - a for a, b in _rev.values()) - (_allow_new - _allow_old)
_rsh = split(_net_rev, [3, 2])
assert _allow_new == 100_000 and _net_rev == 1_400_000 and _rsh == [840_000, 560_000]
_led_rev = ledger("Revaluation account",
                  [("Equipment (decrease)", 400_000), ("Inventory (decrease)", 150_000),
                   ("Allowance for doubtful debts", 50_000), ("Profit: Achu capital (3/5)", _rsh[0]),
                   ("Profit: Bih capital (2/5)", _rsh[1])],
                  [("Premises (increase)", 2_000_000)])
_gsh = split(_gw_avg, [3, 2])
assert _gsh == [5_760_000, 3_840_000]
_j_gw = journal([("Goodwill raised and kept in the books (average profit method)",
                  [("Goodwill", _gw_avg)], [("Achu capital (3/5)", _gsh[0]), ("Bih capital (2/5)", _gsh[1])])])
# practice question figures
_pq2_avg = Fr(3_000_000 - 600_000 + 3_600_000, 3)
assert _pq2_avg == 2_000_000 and _pq2_avg * 3 == 6_000_000
assert (2_500_000 - 12_000_000 * 12 // 100) * 4 == 4_240_000
assert split(900_000 - 300_000, [2, 1]) == [400_000, 200_000]
assert 15_000_000 * 12 // 100 == 1_800_000 and (3_500_000 - 1_800_000) * 3 == 5_100_000 and 3 * 3_500_000 == 10_500_000

LESSONS.append(lesson(
    module=M_PART, topic="Revaluation and goodwill",
    title="Revaluation of assets and the valuation of goodwill in a partnership",
    slug="acu1-revaluation-goodwill", minutes=24,
    summary="When the partners or their ratio change, assets are revalued and goodwill is valued so that each old partner keeps the gains "
            "made while he or she was a partner. Prepare a revaluation account and value goodwill by three methods.",
    objectives=[
        "Explain why assets are revalued and goodwill is valued when a partnership changes",
        "Prepare a revaluation account and share the result in the old profit-sharing ratio",
        "Value goodwill by average profits, weighted average profits and super profits",
        "Record goodwill raised and kept in the books",
    ],
    key_concepts=["Revaluation account", "Old profit-sharing ratio", "Goodwill", "Years' purchase",
                  "Weighted average profit", "Super profit", "Normal return"],
    blocks=[
        H("Why revalue when the partnership changes?"),
        T("Achu and Bih run a printing business in Buea and share profits 3:2. Their premises were bought years ago for 10 000 000 and "
          "are now worth 12 000 000. If a new partner joins at the old book values, he or she would share in a gain that Achu and Bih earned. "
          "So before any **change in the partnership** (a new ratio, admission, retirement or death), the partners revalue the assets and "
          "value the goodwill. All figures here are **invented for practice**."),
        D("A **revaluation account** is a temporary account that records increases and decreases in the values of assets and liabilities. "
          "Its balance (profit or loss on revaluation) is shared among the **old** partners in their **old** profit-sharing ratio.",
          title="Revaluation account"),
        KEY("Revaluation entries", "Think of the revaluation account like a small income statement for value changes.",
            cards=[["Asset increases", "Debit the asset, credit revaluation."],
                   ["Asset decreases", "Debit revaluation, credit the asset."],
                   ["Liability or allowance increases", "Debit revaluation, credit the liability or allowance."],
                   ["Balance", "Profit: debit revaluation, credit old partners' capitals in the old ratio. Loss: the reverse."]]),
        EX("Worked example 1: revaluation account",
           intro="Achu and Bih (3:2) agree new values: premises from 10 000 000 to 12 000 000; equipment from 3 000 000 to 2 600 000; "
                 "inventory from 2 500 000 to 2 350 000; the allowance for doubtful debts on receivables of 2 000 000 to be raised from 50 000 to 5%.",
           steps=[
               S("Increase", text="Premises +2 000 000 (credit revaluation)."),
               S("Decreases", text="Equipment −400 000, inventory −150 000, extra allowance 100 000 − 50 000 = 50 000: total 600 000 (debit revaluation)."),
               S("Profit on revaluation", text="2 000 000 − 600 000 = 1 400 000."),
               S("Share in the OLD ratio 3:2", text="Achu 840 000, Bih 560 000, credited to their capital accounts."),
           ]),
        CODE(_led_rev, "text", title="Revaluation account (invented for practice)"),
        T("If the partners do not want the new values in the books, textbooks use a **memorandum revaluation account**: the net gain is credited to "
          "the old partners in the old ratio and debited to all partners in the new ratio, so the asset values stay unchanged. Check your textbook."),
        H("Goodwill"),
        D("**Goodwill** is the value of a business as a whole above the fair value of its separate net assets. It comes from reputation, "
          "location, loyal customers, skilled staff and good suppliers. In the OHADA chart it corresponds to the **fonds commercial**. "
          "It is an intangible asset: it can only be sold with the business.", title="Goodwill"),
        KEY("Three valuation methods", "The deed or the question tells you which method to use.",
            cards=[["Average profits", "Goodwill = average profit × number of years' purchase."],
                   ["Weighted average", "Recent years get bigger weights; goodwill = weighted average × years' purchase."],
                   ["Super profits", "Super profit = average profit − normal return on capital employed; goodwill = super profit × years' purchase."]]),
        D("**Years' purchase** is the number of years of profit (or super profit) a buyer is willing to pay for. **Normal return** is the profit an "
          "ordinary business would earn on the same capital: capital employed × normal rate of return.", title="Two words to know"),
        EX("Worked example 2: three methods",
           intro="Profits for three years were 4 200 000, 4 800 000 and 5 400 000. Capital employed is 20 000 000 and the normal rate of return 15%. "
                 "Value goodwill at (a) two years' purchase of average profit, (b) two years' purchase of weighted average profit (weights 1, 2, 3), "
                 "(c) three years' purchase of super profit.",
           steps=[
               S("(a) Average profit", text="14 400 000 ÷ 3 = 4 800 000; goodwill = 2 × 4 800 000 = 9 600 000."),
               S("(b) Weighted average", text="(4 200 000 × 1 + 4 800 000 × 2 + 5 400 000 × 3) ÷ 6 = 30 000 000 ÷ 6 = 5 000 000; goodwill = 10 000 000."),
               S("(c) Normal return", text="15% × 20 000 000 = 3 000 000."),
               S("(c) Super profit and goodwill", text="4 800 000 − 3 000 000 = 1 800 000; goodwill = 3 × 1 800 000 = 5 400 000."),
           ]),
        CODE(_t_gw, "text", title="Goodwill valuation (invented for practice)"),
        T("Some textbooks also **capitalize the super profit**: goodwill = super profit ÷ normal rate = 1 800 000 ÷ 15% = 12 000 000. "
          "Use this only when the question asks for it."),
        EX("Worked example 3: goodwill kept in the books",
           intro="Achu and Bih decide to record goodwill of 9 600 000 (method a) and keep it in the books. Record it.",
           steps=[
               S("Debit", text="Goodwill account 9 600 000 (a new intangible asset)."),
               S("Credit old partners in the old ratio", text="Achu 3/5 = 5 760 000; Bih 2/5 = 3 840 000."),
           ]),
        CODE(_j_gw, "text", title="Journal entry"),
        T("**Evaluation.** Goodwill values are estimates. Past profits may not continue; the number of years' purchase is a matter of agreement; the "
          "normal rate of return is a judgement. This is why many partnerships do not keep goodwill in the books: they use it only to adjust "
          "the partners' capitals (next lesson)."),
        MISTAKE("Sharing the revaluation result in the new ratio",
                "The gain or loss arose before the change, so it belongs to the **old** partners in the **old** ratio."),
        MISTAKE("Using total profit instead of super profit",
                "In the super-profit method subtract the normal return first; only the excess is multiplied by the years' purchase."),
        MISTAKE("Ignoring a loss year in the average",
                "A loss is a negative profit: subtract it when you add the years, then divide by the number of years."),
        QUIZ("In a revaluation account, an increase in the allowance for doubtful debts is recorded as:",
             ["A credit to the revaluation account", "A debit to the revaluation account", "A debit to the receivables account",
              "A credit to the partners' capital accounts"], 1,
             "A bigger allowance reduces the value of receivables, so it is a loss: debit revaluation, credit the allowance.",
             hint="Does a larger allowance make the business worth more or less?",
             feedback=["A credit would be a gain; a bigger allowance is a loss.", "",
                       "The allowance account is credited; the receivables account itself is not changed.",
                       "Only the final balance of the revaluation account goes to the partners."]),
        QUIZ("Average profit is 3 500 000, capital employed 15 000 000, normal return 12%. Goodwill is three years' purchase of super profit. Find goodwill.",
             ["10 500 000", "5 400 000", "1 700 000", "5 100 000"], 3,
             "Normal return = 1 800 000; super profit = 1 700 000; goodwill = 3 × 1 700 000 = 5 100 000.",
             hint="Find the normal return on capital first.",
             feedback=["This is three years' purchase of the whole average profit.",
                       "This multiplies the normal return by three.",
                       "This is the super profit for one year only.", ""], title="Quick check 2"),
        TIP("Revaluation and goodwill are the first steps of any admission, retirement or death question in Paper 3 and can be tested alone in "
            "Paper 1. Show the method you use for goodwill in a short working before the ledger accounts.", title="Exam link"),
        PQ("Profits for three years were 3 000 000, a loss of 600 000, and 3 600 000. Value goodwill at three years' purchase of average profit.",
           "Average = (3 000 000 − 600 000 + 3 600 000) ÷ 3 = 2 000 000. Goodwill = 3 × 2 000 000 = 6 000 000."),
        PQ("Average profit is 2 500 000; capital employed 12 000 000; normal rate 12%. Value goodwill at four years' purchase of super profit.",
           "Normal return = 1 440 000; super profit = 1 060 000; goodwill = 4 × 1 060 000 = 4 240 000."),
        PQ("X and Y share 2:1. On revaluation, land rises by 900 000 and machinery falls by 300 000. Show how the result is shared.",
           "Profit on revaluation = 600 000, shared in the old ratio 2:1: X 400 000, Y 200 000 (credited to their capital accounts)."),
        PQ("Discuss two reasons why the goodwill of a partnership is difficult to value.",
           "1. It depends on future profits, which are uncertain; past profits are only a guide. "
           "2. The number of years' purchase and the normal rate of return are agreed by negotiation, so different partners can reach different figures. "
           "Evaluation: because of this uncertainty, firms often use goodwill only to adjust capitals instead of keeping it as an asset."),
        SUM("Revalue assets and liabilities before any change; share the revaluation result in the OLD ratio.",
            "Asset up: debit asset, credit revaluation. Asset down or allowance up: debit revaluation.",
            "Goodwill = average (or weighted average) profit × years' purchase, or super profit × years' purchase.",
            "Super profit = average profit − normal return on capital employed.",
            "Goodwill raised and kept: debit goodwill, credit old partners' capitals in the old ratio."),
    ]))

# ====================================================================== 3. Admission of a partner
_old3, _new3 = [Fr(3, 5), Fr(2, 5)], [Fr(2, 5), Fr(2, 5), Fr(1, 5)]
_sac3 = [_old3[0] - _new3[0], _old3[1] - _new3[1]]
assert _sac3 == [Fr(1, 5), 0]
_gw3 = 5_000_000
_gw_in = [int(_gw3 * f) for f in _old3]
_gw_out = [int(_gw3 * f) for f in _new3]
assert _gw_in == [3_000_000, 2_000_000] and _gw_out == [2_000_000, 2_000_000, 1_000_000]
_rev3 = 1_000_000 - 300_000 - 100_000
_rsh3 = split(_rev3, [3, 2])
assert _rev3 == 600_000 and _rsh3 == [360_000, 240_000]
_t_cap3, _bal3 = columns(
    "Capital accounts", ["Eko", "Tabi", "Manga"],
    [("Goodwill written off", _gw_out)],
    [("Balance b/d", [8_000_000, 6_000_000, None]), ("Bank", [None, None, 4_000_000]),
     ("Revaluation profit", [_rsh3[0], _rsh3[1], None]), ("Goodwill raised", [_gw_in[0], _gw_in[1], None])])
assert _bal3 == [9_360_000, 6_240_000, 3_000_000]
# balance sheet after admission
_bs3_before = {"Land": 6_000_000, "Equipment": 4_000_000, "Inventory": 3_000_000, "Receivables (net)": 2_500_000, "Bank": 1_500_000}
assert sum(_bs3_before.values()) == 17_000_000 == 3_000_000 + 14_000_000
_bs3_after = {"Land": 7_000_000, "Equipment": 4_000_000, "Inventory": 2_700_000, "Receivables (net)": 2_400_000, "Bank": 5_500_000}
assert sum(_bs3_after.values()) == 21_600_000 == 3_000_000 + sum(_bal3)
_t_bs3 = "\n".join([
    "Balance sheet after admission (summary)",
    *[r(k, v) for k, v in _bs3_after.items()],
    r("Total assets", None, sum(_bs3_after.values())),
    r("Capitals: Eko", _bal3[0]),
    r("          Tabi", _bal3[1]),
    r("          Manga", _bal3[2]),
    r("", None, sum(_bal3)),
    r("Payables", None, 3_000_000),
    r("Total equity and liabilities", None, sum(_bal3) + 3_000_000),
])
# example 2: new ratio when the newcomer takes 1/5 equally from both
_n2 = [Fr(3, 5) - Fr(1, 10), Fr(2, 5) - Fr(1, 10), Fr(1, 5)]
assert _n2 == [Fr(1, 2), Fr(3, 10), Fr(1, 5)] and sum(_n2) == 1
# example 3: premium paid in cash for goodwill (old partners 3:2, newcomer takes 1/4 from them in old ratio)
_gw_e3 = 4_800_000
_prem3 = _gw_e3 // 4
_psh3 = split(_prem3, [3, 2])
assert _prem3 == 1_200_000 and _psh3 == [720_000, 480_000]
_n3 = [Fr(3, 5) * Fr(3, 4), Fr(2, 5) * Fr(3, 4), Fr(1, 4)]
assert _n3 == [Fr(9, 20), Fr(6, 20), Fr(5, 20)]
_j3 = journal([("Premium for goodwill paid into the firm by the new partner",
                [("Bank", _prem3)], [("Eko capital (sacrifice 3/5)", _psh3[0]), ("Tabi capital (sacrifice 2/5)", _psh3[1])])])
# practice question figures
assert [Fr(1, 2) * Fr(2, 3), Fr(1, 2) * Fr(2, 3) + Fr(0), Fr(1, 3)] == [Fr(1, 3), Fr(1, 3), Fr(1, 3)]
assert 6_000_000 * Fr(1, 4) == 1_500_000
assert [8_000_000 * 3 // 4 - 8_000_000 * 2 // 4, 8_000_000 // 4 - 8_000_000 // 4, -(8_000_000 // 4)] == [2_000_000, 0, -2_000_000]
assert 6_000_000 * 3 // 4 == 4_500_000 and 1_500_000 * 4 == 6_000_000

LESSONS.append(lesson(
    module=M_PART, topic="Admission of a partner",
    title="Admission of a new partner: new ratio, goodwill adjustment and capital accounts",
    slug="acu1-admission-of-partner", minutes=25,
    summary="When a partner joins, find the new and sacrificing ratios, revalue the assets, adjust goodwill through the capital accounts "
            "(or record a premium paid in cash), and prepare the capital accounts and balance sheet of the new firm.",
    objectives=[
        "Calculate a new profit-sharing ratio and each old partner's sacrifice",
        "Adjust goodwill through the capital accounts when goodwill is not to remain in the books",
        "Record a premium for goodwill paid in cash by the new partner",
        "Prepare columnar capital accounts and the balance sheet after admission",
    ],
    key_concepts=["Admission", "New profit-sharing ratio", "Sacrificing ratio", "Gaining ratio",
                  "Goodwill adjustment", "Premium for goodwill", "Capital contribution"],
    blocks=[
        H("A new partner joins"),
        T("Eko and Tabi run a pharmacy supplies business in Limbe and share profits 3:2. They admit Manga, a qualified pharmacist, who brings "
          "4 000 000 in cash. Manga will now share the profits, including the profits that come from the reputation Eko and Tabi built. "
          "So Manga must **pay for** the share of goodwill gained, and the old partners keep the revaluation gains made before the admission. "
          "All figures here are **invented for practice**."),
        KEY("Four steps on admission", "Work in this order.",
            cards=[["1. Ratios", "New ratio; sacrifice of each old partner = old share − new share."],
                   ["2. Revaluation", "Revalue assets; share the result in the OLD ratio (previous lesson)."],
                   ["3. Goodwill", "Credit old partners in the OLD ratio, debit all partners in the NEW ratio (if goodwill is not kept)."],
                   ["4. Capital", "Credit the new partner with the cash or assets brought in; prepare the new balance sheet."]]),
        D("The **sacrificing ratio** is the ratio in which the old partners give up part of their shares to the new partner: "
          "sacrifice = old share − new share. The **gaining ratio** is its opposite: gain = new share − old share.",
          title="Sacrificing ratio"),
        IMG("alacu1-admission-ratio.svg",
            alt="Two bars: the old ratio Eko 3/5 and Tabi 2/5; the new ratio Eko 2/5, Tabi 2/5 and Manga 1/5. Eko's lost fifth is highlighted as the sacrifice.",
            caption="Figure 1. Old and new ratios: only Eko gives up a share (1/5) to Manga."),
        EX("Worked example 1: admission with goodwill not kept in the books",
           intro="Eko and Tabi (3:2) have capitals of 8 000 000 and 6 000 000. Manga is admitted and brings 4 000 000 in cash; the new ratio is 2:2:1. "
                 "Goodwill is valued at 5 000 000 and is not to remain in the books. Land is revalued up by 1 000 000, inventory down by 300 000, "
                 "and an extra allowance of 100 000 is needed on receivables.",
           steps=[
               S("Sacrifice", text="Eko 3/5 − 2/5 = 1/5; Tabi 2/5 − 2/5 = 0. Only Eko gives up a share."),
               S("Revaluation", text="1 000 000 − 300 000 − 100 000 = 600 000 profit, shared 3:2: Eko 360 000, Tabi 240 000."),
               S("Goodwill raised (old ratio 3:2)", text="Debit goodwill 5 000 000; credit Eko 3 000 000, Tabi 2 000 000."),
               S("Goodwill written off (new ratio 2:2:1)", text="Debit Eko 2 000 000, Tabi 2 000 000, Manga 1 000 000; credit goodwill 5 000 000."),
               S("Net effect", text="Eko +1 000 000 (his sacrifice, 1/5 × 5 000 000), Tabi 0, Manga −1 000 000: the newcomer has paid for the goodwill."),
           ]),
        CODE(_t_cap3, "text", title="Capital accounts after admission (invented for practice)"),
        CODE(_t_bs3, "text", title="Summary balance sheet of the new firm"),
        T("Check: before admission assets were 17 000 000 (capitals 14 000 000 + payables 3 000 000). Revaluation adds 600 000 and Manga's cash adds "
          "4 000 000, giving 21 600 000. Goodwill was raised and written off, so it does not appear."),
        EX("Worked example 2: finding the new ratio",
           intro="Eko and Tabi share 3:2. Manga is admitted for a 1/5 share, which he takes **equally** from Eko and Tabi. Find the new ratio.",
           steps=[
               S("Each gives up", text="1/5 ÷ 2 = 1/10."),
               S("New shares", text="Eko 3/5 − 1/10 = 1/2; Tabi 2/5 − 1/10 = 3/10; Manga 1/5."),
               S("Ratio", text="1/2 : 3/10 : 1/5 = 5/10 : 3/10 : 2/10, so the new ratio is 5:3:2."),
           ], check=r"\tfrac{5}{10} + \tfrac{3}{10} + \tfrac{2}{10} = 1"),
        EX("Worked example 3: premium for goodwill paid in cash",
           intro="Instead, Manga takes a 1/4 share from Eko and Tabi in their old ratio 3:2, and pays a premium for goodwill in cash into the firm. "
                 "Goodwill is valued at 4 800 000.",
           steps=[
               S("Manga's share of goodwill", text="1/4 × 4 800 000 = 1 200 000."),
               S("Sacrificing ratio", text="Taken in the old ratio, so the sacrifice ratio is 3:2."),
               S("Credit the sacrificing partners", text="Eko 720 000 and Tabi 480 000 (credited to capital)."),
               S("New ratio", text="Eko 3/5 × 3/4 = 9/20; Tabi 2/5 × 3/4 = 6/20; Manga 5/20: ratio 9:6:5."),
           ]),
        CODE(_j3, "text", title="Journal entry: premium for goodwill"),
        T("If the premium is paid **privately** to the old partners (not into the firm), no entry is made in the firm's books. "
          "If goodwill is **kept** in the books, only the first goodwill entry (old ratio) is made and the goodwill account stays as an asset."),
        MISTAKE("Writing off goodwill in the old ratio",
                "Goodwill is credited in the OLD ratio (old partners built it) and debited in the NEW ratio (all partners now share it). "
                "Using the same ratio twice cancels the entry and the newcomer pays nothing."),
        MISTAKE("Crediting the premium in the new ratio",
                "A premium compensates the partners who gave up a share, so it is credited in the **sacrificing** ratio."),
        MISTAKE("Sharing revaluation gains with the new partner",
                "The newcomer was not a partner when the values changed: share revaluation results in the old ratio only."),
        QUIZ("Old ratio A:B = 1:1. C joins; new ratio A:B:C = 2:1:1. What is the sacrificing ratio of A and B?",
             ["1:1", "2:1", "0:1, B alone sacrifices", "1:0, A alone sacrifices"], 2,
             "A: 1/2 − 2/4 = 0; B: 1/2 − 1/4 = 1/4. Only B gives up a share.",
             hint="Write both ratios as fractions with the same denominator.",
             feedback=["This assumes both sacrifice equally; compute old − new for each.",
                       "This is the new ratio of A and B, not their sacrifice.", "",
                       "A's new share 2/4 equals the old 1/2, so A gives up nothing."]),
        QUIZ("Goodwill of 6 000 000 is not to stay in the books. The new partner's share is 1/4. By how much does the new partner's capital fall "
             "as a result of the goodwill entries?",
             ["1 500 000", "6 000 000", "Nothing", "4 500 000"], 0,
             "The new partner is debited with 1/4 × 6 000 000 = 1 500 000 when goodwill is written off in the new ratio.",
             hint="The new partner is only in the write-off entry.",
             feedback=["", "That is the total goodwill, shared by all partners in the new ratio.",
                       "The newcomer is debited in the write-off entry.",
                       "This is the old partners' total share of the write-off."], title="Quick check 2"),
        TIP("Admission questions in Paper 3 usually ask for the revaluation account, the capital accounts in columnar form and the new balance sheet. "
            "Write the ratios (old, new, sacrifice) at the top of your answer before any ledger work.", title="Exam link"),
        PQ("Agbor and Besong share 1:1. Che is admitted for a 1/3 share taken from them in their old ratio. Find the new ratio.",
           "Each old partner keeps 1/2 × 2/3 = 1/3. New ratio Agbor : Besong : Che = 1/3 : 1/3 : 1/3 = 1:1:1."),
        PQ("Old partners X and Y share 3:1. Z is admitted; the new ratio is 2:1:1. Goodwill is 8 000 000 and is not kept. Show the net effect on each capital.",
           "Raised in old ratio 3:1: X +6 000 000, Y +2 000 000. Written off 2:1:1: X −4 000 000, Y −2 000 000, Z −2 000 000. "
           "Net: X +2 000 000, Y 0, Z −2 000 000. Check: X's sacrifice 3/4 − 2/4 = 1/4 of 8 000 000 = 2 000 000."),
        PQ("A new partner pays a premium of 1 500 000 in cash into the firm for a 1/4 share of goodwill. What is total goodwill, and who receives the premium?",
           "Goodwill = 1 500 000 × 4 = 6 000 000. The premium is credited to the old partners' capital accounts in their sacrificing ratio."),
        PQ("Explain why a new partner should pay for goodwill.",
           "Goodwill is built by the old partners (reputation, customers). The new partner will share future profits that come from it, so he or she "
           "compensates the old partners for the share of goodwill given up. Without this, the old partners would lose value on admission."),
        SUM("Sacrifice = old share − new share; the new partner's gain equals the old partners' total sacrifice.",
            "Revaluation result goes to the old partners in the old ratio.",
            "Goodwill not kept: credit old partners in the old ratio, debit all partners in the new ratio.",
            "Premium paid into the firm: debit bank, credit old partners in the sacrificing ratio.",
            "Finish with columnar capital accounts and the new balance sheet; check that it balances."),
    ]))

# ====================================================================== 4. Retirement and death of a partner
_rv4 = split(500_000, [2, 2, 1])
_gin4 = split(2_500_000, [2, 2, 1])
_gout4 = split(2_500_000, [1, 1])
assert _rv4 == [200_000, 200_000, 100_000] and _gin4 == [1_000_000, 1_000_000, 500_000] and _gout4 == [1_250_000, 1_250_000]
_t_cap4, _bal4 = columns(
    "Capital accounts on Mbah's retirement", ["Kum", "Lum", "Mbah"],
    [("Goodwill written off", [_gout4[0], _gout4[1], None]), ("Bank", [None, None, 900_000]),
     ("Mbah loan account", [None, None, 3_000_000])],
    [("Balance b/d", [5_000_000, 4_000_000, 3_000_000]), ("Current account", [None, None, 300_000]),
     ("Revaluation profit", _rv4), ("Goodwill raised", _gin4)])
assert _bal4 == [4_950_000, 3_950_000, 0]
_due4 = 3_000_000 + 300_000 + 100_000 + 500_000
assert _due4 == 3_900_000 == 900_000 + 3_000_000
_gain4 = [Fr(1, 2) - Fr(2, 5)] * 2
assert _gain4 == [Fr(1, 10), Fr(1, 10)] and 2_500_000 * Fr(1, 10) == 250_000
_sched4 = []
_out = 3_000_000
for _y in range(1, 4):
    _int = _out * 10 // 100
    _sched4.append((_y, _out, _int, 1_000_000, _int + 1_000_000))
    _out -= 1_000_000
assert _out == 0 and [s[2] for s in _sched4] == [300_000, 200_000, 100_000]
_t_loan4 = "\n".join(["Year  Opening loan  Interest 10%  Repayment     Total"] +
                     [f"{y:<4}{n(o):>13}{n(i):>14}{n(rp):>11}{n(t):>10}" for y, o, i, rp, t in _sched4])
# death of Fru
_prof_death = Fr(8_000_000 * 3, 12) * Fr(1, 4)
_ioc_death = Fr(4_000_000 * 10 * 3, 100 * 12)
assert _prof_death == 500_000 and _ioc_death == 100_000
_ex4 = [("Capital", 4_000_000), ("Current account (credit)", 250_000), ("Interest on capital to death", 100_000),
        ("Share of profit to death", 500_000), ("Share of goodwill (1/4 x 6 000 000)", 1_500_000), ("Share of revaluation profit", 200_000)]
_due_ex = sum(a for _, a in _ex4) - 300_000
assert _due_ex == 6_250_000
_t_ex4 = "\n".join(["Amount due to Fru's executors"] + [r(l, a, w=38) for l, a in _ex4] +
                   [r("Less drawings to date of death", "(300 000)", w=38), r("Amount due to executors", None, _due_ex, w=26)])
_led_ex4 = ledger("Fru's executors account",
                  [("Bank (first payment)", 2_000_000), ("Balance c/d (owed to executors)", 4_250_000)],
                  [("Fru capital (amount due)", _due_ex)])
# practice question figures
assert Fr(12_000_000 * 8_000_000, 40_000_000) == 2_400_000 and 2_400_000 // 4 == 600_000
assert split(3_000_000, [3, 2, 1]) == [1_500_000, 1_000_000, 500_000]
assert Fr(3, 5) - Fr(3, 6) == Fr(1, 10) and Fr(2, 5) - Fr(2, 6) == Fr(1, 15) and 9_000_000 * 4 // 12 // 3 == 1_000_000
assert Fr(1, 2) - Fr(2, 6) == Fr(1, 6) and 3_000_000 // 6 == 500_000

LESSONS.append(lesson(
    module=M_PART, topic="Retirement and death of a partner",
    title="Retirement and death of a partner: amount due, goodwill and the executors' account",
    slug="acu1-retirement-death", minutes=25,
    summary="Find the amount due to a retiring partner or to a dead partner's executors after revaluation, goodwill and profit to the date of "
            "death, adjust the continuing partners' capitals, and settle the amount in cash or by a loan.",
    objectives=[
        "Calculate the amount due to a retiring partner after revaluation and goodwill adjustments",
        "Adjust goodwill through the capital accounts using the gaining ratio of the continuing partners",
        "Record payment in cash, a loan account and the interest on that loan",
        "Calculate a deceased partner's share of profit to the date of death and prepare the executors' account",
    ],
    key_concepts=["Retirement", "Gaining ratio", "Amount due to a retiring partner", "Loan account",
                  "Death of a partner", "Profit to the date of death", "Executors' account"],
    blocks=[
        H("A partner leaves"),
        T("Kum, Lum and Mbah run a transport business in Bafoussam. After many years Mbah decides to retire. The firm must pay him what it owes: "
          "his capital, his current account, and his share of the gains and goodwill that exist on the day he leaves. When a partner dies, the same "
          "amount is owed to the **executors** (the persons who settle the estate). All figures are **invented for practice**."),
        D("The **amount due to a retiring partner** = capital + current account credit balance + share of revaluation profit + share of goodwill "
          "+ share of profit and interest to the date of leaving − drawings and any debit balances.", title="Amount due"),
        D("The **gaining ratio** is the ratio in which the continuing partners gain the retiring partner's share: gain = new share − old share. "
          "When goodwill is not kept, the continuing partners are debited for the goodwill they gain, and the retiring partner is credited.",
          title="Gaining ratio"),
        EX("Worked example 1: retirement",
           intro="Kum, Lum and Mbah share 2:2:1. Capitals: 5 000 000, 4 000 000 and 3 000 000; Mbah's current account has a credit of 300 000. "
                 "On Mbah's retirement assets are revalued up by 500 000 and goodwill is valued at 2 500 000, not to be kept. Kum and Lum will share 1:1. "
                 "Mbah receives 900 000 in cash and the rest stays as a loan at 10% a year.",
           steps=[
               S("Revaluation (old ratio 2:2:1)", text="Kum 200 000, Lum 200 000, Mbah 100 000."),
               S("Goodwill raised (old ratio)", text="Kum 1 000 000, Lum 1 000 000, Mbah 500 000."),
               S("Goodwill written off (new ratio 1:1)", text="Kum 1 250 000, Lum 1 250 000. Each gains 1/2 − 2/5 = 1/10 and pays 250 000 net."),
               S("Amount due to Mbah", text="3 000 000 + 300 000 + 100 000 + 500 000 = 3 900 000."),
               S("Settlement", text="Bank 900 000; loan account 3 000 000."),
           ]),
        CODE(_t_cap4, "text", title="Capital accounts (invented for practice)"),
        T("Mbah's capital account closes at zero. His **loan account** is a liability of the firm. Interest on it is an **expense** in the income statement, "
          "like interest on any other loan."),
        CODE(_t_loan4, "text", title="Repayment of Mbah's loan: 1 000 000 a year plus 10% interest"),
        H("Death of a partner"),
        T("When a partner dies during the year, the firm must find the partner's share of profit **from the start of the year to the date of death**. "
          "The deed usually says how: either time-apportion the previous year's profit, or use sales to date × (last year's profit ÷ last year's sales). "
          "Interest on capital and drawings are also calculated to the date of death."),
        EX("Worked example 2: amount due to executors",
           intro="Fru, who had a 1/4 share, died on 31 March; the year ends on 31 December. His capital was 4 000 000 and his current account 250 000 credit. "
                 "Interest on capital is 10% a year. Profit to date of death is based on last year's profit of 8 000 000. Goodwill is 6 000 000 and his share of "
                 "revaluation profit is 200 000. His drawings to 31 March were 300 000.",
           steps=[
               S("Profit to date of death", text="8 000 000 × 3/12 × 1/4 = 500 000."),
               S("Interest on capital", text="4 000 000 × 10% × 3/12 = 100 000."),
               S("Goodwill share", text="1/4 × 6 000 000 = 1 500 000."),
               S("Amount due", text="4 000 000 + 250 000 + 100 000 + 500 000 + 1 500 000 + 200 000 − 300 000 = 6 250 000."),
               S("Transfer", text="Debit Fru's capital, credit Fru's executors account 6 250 000."),
           ]),
        CODE(_t_ex4, "text", title="Statement of amount due (invented for practice)"),
        CODE(_led_ex4, "text", title="Executors' account after a first payment of 2 000 000"),
        T("**Evaluation.** Paying a large amount at once can drain the firm's cash. This is why deeds often allow payment by instalments, with interest, "
          "and why some partnerships take out insurance on partners' lives. Check your textbook for the joint life policy method if your class uses it."),
        MISTAKE("Debiting the retiring partner with goodwill",
                "The retiring partner is only credited with goodwill (old ratio). Only the continuing partners are debited (new ratio)."),
        MISTAKE("Treating loan interest as an appropriation",
                "After retirement the former partner is a lender. Interest on the loan is an expense, not a share of profit."),
        MISTAKE("Taking a full year's profit for a partner who died during the year",
                "Apportion profit and interest to the date of death using the method the deed gives."),
        QUIZ("A, B and C share 3:2:1. C retires; A and B continue in the ratio 3:2. What is A's gain?",
             ["1/10", "1/6", "3/5", "1/15"], 0,
             "A's new share 3/5 − old share 3/6 = 18/30 − 15/30 = 3/30 = 1/10. (B gains 2/5 − 2/6 = 1/15.)",
             hint="Gain = new share − old share. Use a common denominator.",
             feedback=["", "This is C's whole share, not A's part of it.",
                       "This is A's new share, not the gain.", "This is B's gain, not A's."]),
        QUIZ("The previous year's net profit was 9 000 000. A partner with a 1/3 share died on 30 April (year end 31 December). Profit to the date of "
             "death is time-apportioned. What is the partner's share?",
             ["3 000 000", "250 000", "1 000 000", "1 500 000"], 2,
             "9 000 000 × 4/12 × 1/3 = 1 000 000.",
             hint="January to April is four months.",
             feedback=["This is a full year's share.", "This uses one month instead of four months.", "",
                       "This uses a 1/2 share instead of the partner's 1/3."],
             title="Quick check 2"),
        TIP("Retirement and death questions in Paper 3 often combine revaluation, goodwill and the capital accounts, then ask for the loan or "
            "executors' account. Present a separate statement of the amount due before the ledger accounts.", title="Exam link"),
        PQ("A partner with a 1/4 share died. Sales from the start of the year to the date of death were 12 000 000. Last year's sales were 40 000 000 and "
           "net profit 8 000 000. Using the sales basis, find the partner's share of profit to the date of death.",
           "Profit to date = 12 000 000 × 8 000 000 ÷ 40 000 000 = 2 400 000. Share = 1/4 × 2 400 000 = 600 000."),
        PQ("X, Y and Z share 3:2:1. Z retires. Goodwill is 3 000 000 and is not kept; X and Y continue 1:1. Show the goodwill entries.",
           "Raise in old ratio 3:2:1: debit goodwill 3 000 000; credit X 1 500 000, Y 1 000 000, Z 500 000. "
           "Write off in new ratio 1:1: debit X 1 500 000, Y 1 500 000; credit goodwill 3 000 000. Net: X 0, Y −500 000, Z +500 000 "
           "(Y alone gains Z's share: 1/2 − 2/6 = 1/6 = 500 000)."),
        PQ("A retiring partner is owed 3 000 000, to be repaid in three equal yearly instalments with 10% interest on the balance outstanding. "
           "Find the total paid in the first year.",
           "Instalment 1 000 000 + interest 10% × 3 000 000 = 300 000. Total 1 300 000."),
        PQ("Discuss two problems a partnership faces on the retirement of a partner and how the deed can reduce them.",
           "1. Cash: paying the amount due at once can leave the firm short of cash; the deed can allow payment by instalments with interest. "
           "2. Valuation disputes about goodwill and assets; the deed can fix the valuation method in advance. "
           "Evaluation: the firm may also lose the partner's skills and customers, which no deed can prevent."),
        SUM("Amount due = capital + current account + revaluation share + goodwill share + profit and interest to date − drawings.",
            "Goodwill not kept: credit all old partners in the old ratio, debit continuing partners in the new ratio.",
            "Continuing partners gain in the gaining ratio: new share − old share.",
            "Unpaid amount goes to a loan account (retirement) or an executors' account (death); its interest is an expense.",
            "On death, apportion profit and interest to the date of death by time or by sales, as the deed says."),
    ]))

# ====================================================================== 5. Dissolution of a partnership
_assets5 = {"Premises": 8_000_000, "Vehicles": 3_000_000, "Inventory": 2_000_000, "Receivables": 1_500_000}
_bank5 = 500_000
_pay5, _loan5, _caps5 = 1_800_000, 1_000_000, [6_000_000, 4_000_000, 2_200_000]
assert sum(_assets5.values()) + _bank5 == _pay5 + _loan5 + sum(_caps5) == 15_000_000
_led_real5 = ledger("Realisation account",
                    [("Premises", 8_000_000), ("Vehicles", 3_000_000), ("Inventory", 2_000_000), ("Receivables", 1_500_000),
                     ("Bank: dissolution expenses", 300_000)],
                    [("Bank: premises sold", 9_000_000), ("Bate capital: vehicle taken", 2_400_000), ("Bank: inventory sold", 1_600_000),
                     ("Bank: receivables collected", 1_350_000), ("Discount on payables", 50_000),
                     ("Loss: Ashu capital (2/5)", 160_000), ("Loss: Bate capital (2/5)", 160_000), ("Loss: Che capital (1/5)", 80_000)])
_loss5 = (8_000_000 + 3_000_000 + 2_000_000 + 1_500_000 + 300_000) - (9_000_000 + 2_400_000 + 1_600_000 + 1_350_000 + 50_000)
assert _loss5 == 400_000 and split(_loss5, [2, 2, 1]) == [160_000, 160_000, 80_000]
_bankbal5 = _bank5 + 9_000_000 + 1_600_000 + 1_350_000 - 300_000 - 1_750_000 - _loan5
assert _bankbal5 == 9_400_000
_t_cap5, _bal5 = columns(
    "Capital accounts on dissolution", ["Ashu", "Bate", "Che"],
    [("Realisation: vehicle", [None, 2_400_000, None]), ("Realisation: loss", [160_000, 160_000, 80_000])],
    [("Balance b/d", _caps5)], bal_label="Bank (final settlement)")
assert _bal5 == [5_840_000, 1_440_000, 2_120_000] and sum(_bal5) == _bankbal5
_led_bank5 = ledger("Bank account",
                    [("Balance b/d", _bank5), ("Realisation: premises", 9_000_000), ("Realisation: inventory", 1_600_000),
                     ("Realisation: receivables", 1_350_000)],
                    [("Realisation: expenses", 300_000), ("Payables (1 800 000 less 50 000)", 1_750_000), ("Ashu loan", _loan5),
                     ("Ashu capital", _bal5[0]), ("Bate capital", _bal5[1]), ("Che capital", _bal5[2])])
# Garner v Murray
_gm_caps = [4_000_000, 2_000_000, 1_000_000]
_gm_def = 300_000
_gm_share = split(_gm_def, [4, 2])
assert _gm_share == [200_000, 100_000]
assert split(_gm_def, [2, 2]) == [150_000, 150_000]
# practice question figures
assert (2_000_000 + 900_000) - (1_700_000 + 600_000) == 600_000 and split(300_000, [3, 1]) == [225_000, 75_000]

LESSONS.append(lesson(
    module=M_PART, topic="Dissolution of a partnership",
    title="Dissolution of a partnership: realisation account, settlement and Garner v Murray",
    slug="acu1-dissolution", minutes=25,
    summary="When a partnership ends, close the assets to a realisation account, record sales, takeovers and costs, pay creditors and loans, "
            "share the realisation profit or loss and settle the partners in cash, including the case of an insolvent partner.",
    objectives=[
        "State the order in which cash is used on dissolution",
        "Prepare the realisation account, the partners' capital accounts and the bank account",
        "Record an asset taken over by a partner and discounts received from creditors",
        "Apply the rule in Garner v Murray when a partner cannot pay a debit balance",
    ],
    key_concepts=["Dissolution", "Realisation account", "Realisation profit or loss", "Asset taken over by a partner",
                  "Order of payment", "Insolvent partner", "Garner v Murray"],
    blocks=[
        H("Ending a partnership"),
        T("Ashu, Bate and Che have run a furniture workshop in Kumba for ten years. Ashu wants to move abroad, and the partners decide to **dissolve** "
          "(end) the partnership. The assets will be sold, the debts paid and whatever is left shared among the partners. The accounts must show who "
          "receives how much. All figures are **invented for practice**."),
        D("A **realisation account** is the account in which the assets are closed at book value, the proceeds of sale (or the agreed value when a partner "
          "takes an asset) are credited, and dissolution costs are debited. Its balance is the **profit or loss on realisation**, shared in the profit-sharing ratio.",
          title="Realisation account"),
        IMG("alacu1-dissolution-steps.svg",
            alt="Six steps in order: transfer assets to realisation; sell assets or let partners take them; pay creditors and costs; repay partners' loans; "
                "share the realisation profit or loss; settle capitals in cash so the bank closes at zero.",
            caption="Figure 1. The order of work on dissolution."),
        KEY("Order in which cash is used", "Textbooks follow this order, which reflects partnership law.",
            cards=[["1", "Outside creditors and the costs of dissolution."],
                   ["2", "Loans made by partners (they rank before capital)."],
                   ["3", "Partners' capitals, after the realisation profit or loss is shared."]]),
        EX("Worked example 1: realisation account",
           intro="Ashu, Bate and Che share 2:2:1. Balance sheet: premises 8 000 000, vehicles 3 000 000, inventory 2 000 000, receivables 1 500 000, bank 500 000; "
                 "payables 1 800 000, loan from Ashu 1 000 000, capitals 6 000 000, 4 000 000 and 2 200 000. Premises sell for 9 000 000; Bate takes the vehicles "
                 "at 2 400 000; inventory sells for 1 600 000; receivables pay 1 350 000; payables are settled for 1 750 000; dissolution costs are 300 000.",
           steps=[
               S("Debit realisation", text="All assets except bank at book value (14 500 000) plus costs 300 000 = 14 800 000."),
               S("Credit realisation", text="Proceeds 9 000 000 + 1 600 000 + 1 350 000, Bate's vehicles 2 400 000, discount on payables 50 000 = 14 400 000."),
               S("Loss on realisation", text="14 800 000 − 14 400 000 = 400 000, shared 2:2:1: 160 000, 160 000, 80 000."),
               S("Capitals", text="Ashu 6 000 000 − 160 000 = 5 840 000; Bate 4 000 000 − 2 400 000 − 160 000 = 1 440 000; Che 2 200 000 − 80 000 = 2 120 000."),
           ]),
        CODE(_led_real5, "text", title="Realisation account (invented for practice)"),
        CODE(_t_cap5, "text", title="Capital accounts"),
        CODE(_led_bank5, "text", title="Bank account: it closes at zero"),
        T("Check: cash available after paying creditors and Ashu's loan is 9 400 000, exactly the total of the capital balances (5 840 000 + 1 440 000 + 2 120 000). "
          "A partner who takes an asset is **debited** with its agreed value in his capital account, just as if he had paid cash."),
        H("When a partner cannot pay: Garner v Murray"),
        T("If, after the realisation loss, a partner's capital account has a **debit** balance, that partner must pay the firm. If he is insolvent and cannot pay, "
          "the deficiency is a further loss to the other partners. Textbooks apply the English case **Garner v Murray (1904)**: the solvent partners bear the deficiency "
          "in the ratio of their **last agreed capitals** (capitals in the last balance sheet before dissolution), not in their profit-sharing ratio. "
          "A deed can set a different rule; check your textbook and your teacher's notes."),
        EX("Worked example 2: an insolvent partner",
           intro="Ebai, Fru and Gwan share profits 2:2:1. Their last agreed fixed capitals were 4 000 000, 2 000 000 and 1 000 000. After realisation, Gwan's "
                 "capital shows a debit balance of 300 000 and he is insolvent. How is the deficiency shared?",
           steps=[
               S("Ratio to use", text="Last agreed capitals of the solvent partners: 4 000 000 : 2 000 000 = 2:1."),
               S("Share the deficiency", text="Ebai 2/3 × 300 000 = 200 000; Fru 1/3 × 300 000 = 100 000."),
               S("Not the profit ratio", text="Using 2:2 (equal) would give 150 000 each, which is wrong under Garner v Murray."),
           ]),
        T("**Evaluation.** The rule treats the deficiency as a loss of capital, but it makes the partners who contributed more capital bear **more** of a loss "
          "caused by someone else. Many think this is unfair, which is why some deeds replace it with sharing in the profit-sharing ratio."),
        MISTAKE("Putting cash in the realisation account",
                "Cash (bank) is not realised: it stays in the bank account. Only the other assets go to the realisation account."),
        MISTAKE("Crediting the partner who takes an asset",
                "The partner receives an asset, so his capital is **debited**; the realisation account is credited."),
        MISTAKE("Paying capitals before partners' loans",
                "Partners' loans are repaid before any capital is returned."),
        QUIZ("A partner takes over a car valued at FCFA 1 200 000 on dissolution. What is the entry?",
             ["Debit realisation, credit partner's capital", "Debit bank, credit realisation", "Debit partner's capital, credit realisation",
              "Debit car, credit partner's capital"], 2,
             "The partner receives value, so his capital is debited; the realisation account is credited as if the car were sold.",
             hint="Does the partner receive or give value?",
             feedback=["This would mean the firm owes the partner more.", "No cash moves when a partner takes an asset.", "",
                       "The car's book value is already in the realisation account; the takeover is recorded there."]),
        QUIZ("Under Garner v Murray, a deficiency of an insolvent partner is borne by the solvent partners in the ratio of:",
             ["Their profit-sharing ratio", "Their last agreed capitals", "Their current account balances", "Equally"], 1,
             "The case decided that the deficiency is a capital loss shared in the ratio of the last agreed capitals.",
             hint="The case treats the deficiency as a loss of capital, not of profit.",
             feedback=["This applies to the realisation loss, not to the deficiency.", "",
                       "Current accounts are not used in the rule.", "Equal sharing is the default for profits, not for this deficiency."],
             title="Quick check 2"),
        TIP("Dissolution questions in Paper 3 ask for the realisation account, the capital accounts and the bank (cash) account. The bank account must close at zero: "
            "use this to check your answer.", title="Exam link"),
        PQ("Machinery with a book value of 2 000 000 is sold for 1 700 000 and an unrecorded asset is sold for 600 000; costs are 900 000. "
           "Find the net result of these items in the realisation account.",
           "Debits: 2 000 000 + 900 000 = 2 900 000. Credits: 1 700 000 + 600 000 = 2 300 000. Loss on these items = 600 000."),
        PQ("Two partners share 3:1. Realisation shows a loss of 300 000. Share the loss.",
           "3:1 gives 225 000 and 75 000."),
        PQ("Why must a partners' loan be repaid before partners' capital on dissolution?",
           "A loan is a debt of the firm, like an outside creditor, although it ranks after outside creditors. Capital is the owners' interest and is repaid "
           "only from what is left after all debts are paid."),
        PQ("Discuss whether Garner v Murray is a fair rule.",
           "For: the deficiency is treated as a loss of capital, so it is shared in the ratio of capital. Against: partners who put in more capital "
           "bear more of a loss caused by another partner's insolvency, and the rule ignores the profit-sharing agreement. Conclusion: many deeds exclude it."),
        SUM("Close all assets except bank to the realisation account; credit proceeds and assets taken by partners; debit costs.",
            "Discounts received from creditors are a realisation gain.",
            "Order of payment: creditors and costs, partners' loans, then capitals.",
            "Share the realisation result in the profit-sharing ratio; the bank account closes at zero.",
            "Garner v Murray: an insolvent partner's deficiency is borne by solvent partners in the ratio of last agreed capitals."),
    ]))

# ====================================================================== 6. Company formation under OHADA
_nom6, _kind6, _cash6 = 10_000, 500, 1_500
_cap6 = (_kind6 + _cash6) * _nom6
_kindv6 = _kind6 * _nom6
_called6 = _cash6 * _nom6 // 4
_uncalled6 = _cash6 * _nom6 - _called6
assert (_cap6, _kindv6, _called6, _uncalled6) == (20_000_000, 5_000_000, 3_750_000, 11_250_000)
_j6a = journal([
    ("(1) Subscription of the capital",
     [("4611 Contributors, in kind", _kindv6), ("4612 Contributors, cash", _called6), ("109 Contributors, uncalled", _uncalled6)],
     [("1011 Capital, uncalled", _uncalled6), ("1012 Capital called, not paid", _kindv6 + _called6)]),
    ("(2) Building handed over", [("231 Buildings", _kindv6)], [("4611 Contributors, in kind", _kindv6)]),
    ("(3) Cash paid in (bank or notary)", [("521 Bank", _called6)], [("4612 Contributors, cash", _called6)]),
    ("(4) Called capital now paid", [("1012 Capital called, not paid", _kindv6 + _called6)], [("1013 Capital called and paid", _kindv6 + _called6)]),
])
_j6b = journal([
    ("(5) Call of the remaining three quarters", [("4613 Shareholders, called unpaid", _uncalled6)], [("109 Contributors, uncalled", _uncalled6)]),
    ("(6) Capital status changes", [("1011 Capital, uncalled", _uncalled6)], [("1012 Capital called, not paid", _uncalled6)]),
    ("(7) Shareholders pay", [("521 Bank", _uncalled6)], [("4613 Shareholders, called unpaid", _uncalled6)]),
    ("(8) Capital fully paid", [("1012 Capital called, not paid", _uncalled6)], [("1013 Capital called and paid", _uncalled6)]),
])
assert _kindv6 + _called6 + _uncalled6 == _cap6
# SARL example
_sarl = {"Ambe (cash)": 1_500_000, "Bih (cash)": 900_000, "Chu (van)": 600_000}
assert sum(_sarl.values()) == 3_000_000 and 3_000_000 // 10_000 == 300
_j6c = journal([
    ("Subscription (parts fully paid)", [("4612 Contributors, cash", 2_400_000), ("4611 Contributors, in kind", 600_000)],
     [("1013 Capital called and paid", 3_000_000)]),
    ("Van handed over", [("245 Transport equipment", 600_000)], [("4611 Contributors, in kind", 600_000)]),
    ("Cash paid in", [("521 Bank", 2_400_000)], [("4612 Contributors, cash", 2_400_000)]),
])
# practice question figures
assert 4_000 * 10_000 // 4 == 10_000_000 and 4_000 * 10_000 - 10_000_000 == 30_000_000

LESSONS.append(lesson(
    module=M_COMP, topic="Company formation under OHADA",
    title="Forming an SARL or an SA under OHADA and recording the capital",
    slug="acu1-company-formation-ohada", minutes=25,
    summary="Compare the main OHADA company forms, follow the stages of forming an SA, and record subscription, contributions in cash and in kind, "
            "calls and payment of capital with the SYSCOHADA capital accounts.",
    objectives=[
        "Compare the SNC, SARL, SA and SAS under the OHADA Uniform Act on commercial companies",
        "State the main legal rules on the capital of an SA and describe the stages of its formation",
        "Record the subscription, contributions in kind and in cash, calls and payment of capital",
        "Explain how the status of capital moves from uncalled to called and paid",
    ],
    key_concepts=["OHADA Uniform Act on commercial companies", "SARL", "SA", "Share capital", "Nominal value",
                  "Contribution in cash", "Contribution in kind", "Called-up capital", "RCCM"],
    blocks=[
        H("From partnership to company"),
        T("Mungo Agro, a group of farmers' partners near Mbanga, wants to build a fruit-processing plant. They need more capital than a partnership can raise, "
          "and they do not want each owner to risk his personal property. The answer is a **company**: a separate legal person whose owners' liability "
          "is limited to their contributions. In Cameroon, companies are governed by the **OHADA Uniform Act on commercial companies and economic interest "
          "groups** (revised in 2014). All figures are **invented for practice**."),
        KEY("Main forms of commercial company", "The Uniform Act provides several forms; these four are the ones you meet most.",
            cards=[["SNC (société en nom collectif)", "General partnership: partners are traders, with unlimited joint and several liability."],
                   ["SARL (société à responsabilité limitée)", "Private limited company: one or more partners, liability limited to contributions, capital divided into equal parts (parts sociales); parts are not freely transferable to outsiders."],
                   ["SA (société anonyme)", "Public limited company: one or more shareholders, capital divided into shares (actions), run by a board of directors or a sole general administrator; a statutory auditor is required."],
                   ["SAS (société par actions simplifiée)", "Simplified joint-stock company added in 2014: very free organisation set by the statutes."]]),
        D("For an **SA** the Uniform Act sets a minimum capital of **FCFA 10 000 000**. Cash shares must be paid up by **at least one quarter of their nominal value** "
          "on subscription, and the rest within **three years**, when the board calls it. Contributions in kind are paid in full when the shares are issued and "
          "are valued by an independent **commissaire aux apports** (auditor of contributions).", title="Capital rules for an SA"),
        D("For an **SARL** the Uniform Act sets a default minimum capital of FCFA 1 000 000 and a minimum nominal value of FCFA 5 000 per part, but it lets each "
          "member state fix its own minimum. Cameroon has used this option, so **check the current rule** with your teacher and textbook before quoting a figure.",
          title="Capital of an SARL"),
        IMG("alacu1-sa-formation-steps.svg",
            alt="Five stages in a column: statutes drafted and signed; subscription of shares with at least a quarter paid; funds deposited with a notary or bank; "
                "declaration of subscription and payment before the notary; registration in the RCCM, which gives legal personality.",
            caption="Figure 1. Main stages in forming an SA."),
        T("The company becomes a legal person only on **registration in the RCCM** (Registre du Commerce et du Crédit Mobilier). In Cameroon the formalities "
          "can be completed at a **CFCE** (Centre de Formalités de Création d'Entreprises), a one-stop shop. Formation costs (notary, registration, publication) "
          "are treated as expenses of the year under the revised SYSCOHADA; older textbooks capitalised them as preliminary expenses. Check your textbook."),
        H("Recording the capital"),
        KEY("Status of capital (class 1)", "SYSCOHADA follows the capital through three stages. Account numbers are the usual textbook ones; check your textbook.",
            cards=[["1011", "Capital subscribed, uncalled (the company has not yet asked for it)."],
                   ["1012", "Capital subscribed, called, not paid."],
                   ["1013", "Capital subscribed, called and paid."]]),
        KEY("Contributors (class 4 and 109)", "These accounts record what shareholders owe.",
            cards=[["4611 / 4612", "Contributions in kind / in cash promised on subscription."],
                   ["109", "Contributors, capital subscribed but uncalled (shown as a deduction from capital in the revised balance sheet)."],
                   ["4613", "Shareholders, capital called but not yet paid."]]),
        EX("Worked example 1: formation of an SA",
           intro="Mungo Agro SA is formed with a capital of 20 000 000: 2 000 shares of 10 000. 500 shares are issued for a building valued at 5 000 000; "
                 "1 500 shares are paid in cash, one quarter on subscription.",
           steps=[
               S("Contribution in kind", text="500 × 10 000 = 5 000 000, fully paid."),
               S("Cash shares", text="1 500 × 10 000 = 15 000 000; quarter called now: 3 750 000; uncalled: 11 250 000."),
               S("Subscription entry", text="Debit 4611 5 000 000, 4612 3 750 000 and 109 11 250 000; credit 1011 11 250 000 and 1012 8 750 000."),
               S("Payment", text="Building received (231), cash received (521), then 1012 is transferred to 1013 for 8 750 000."),
           ]),
        CODE(_j6a, "text", title="Journal: formation (invented for practice)"),
        EX("Worked example 2: calling the rest",
           intro="Two years later the board calls the remaining three quarters (11 250 000), and all shareholders pay.",
           steps=[
               S("Call", text="Debit 4613, credit 109: the amount becomes a debt of the shareholders."),
               S("Status", text="Debit 1011, credit 1012: the capital is now called."),
               S("Payment", text="Debit 521, credit 4613; then debit 1012, credit 1013. All 20 000 000 is now called and paid."),
           ]),
        CODE(_j6b, "text", title="Journal: call and payment"),
        EX("Worked example 3: an SARL",
           intro="Ambe, Bih and Chu form an SARL with capital 3 000 000 in 300 parts of 10 000. Ambe pays 1 500 000 and Bih 900 000 in cash; Chu contributes a van "
                 "valued at 600 000. The parts are fully paid at once.",
           steps=[
               S("Subscription", text="Debit 4612 2 400 000 and 4611 600 000; credit 1013 3 000 000."),
               S("Contributions received", text="Debit 245 (transport equipment) 600 000 and 521 (bank) 2 400 000; credit 4611 and 4612."),
           ]),
        CODE(_j6c, "text", title="Journal: SARL formation"),
        MISTAKE("Crediting capital with only the cash received",
                "The capital account shows the whole capital subscribed. What is not yet paid is recorded in 109 or 4613 (amounts owed by shareholders)."),
        MISTAKE("Treating a contribution in kind as partly paid",
                "Contributions in kind are paid in full on issue: the asset is handed over to the company."),
        MISTAKE("Mixing up SARL and SA rules",
                "The quarter-paid rule and the FCFA 10 000 000 minimum are SA rules. For an SARL, check the national rule."),
        QUIZ("Under the OHADA Uniform Act, what is the minimum capital of an SA?",
             ["FCFA 1 000 000", "FCFA 5 000 000", "FCFA 10 000 000", "FCFA 100 000 000"], 2,
             "The minimum capital of an SA is FCFA 10 000 000.",
             hint="It is ten times the SARL default figure.",
             feedback=["This is the SARL default figure, which member states may change.", "This figure is not set by the Act.", "",
                       "This is far above the general SA minimum."]),
        QUIZ("A shareholder subscribes 200 cash shares of nominal value 10 000 in an SA. What is the minimum he must pay on subscription?",
             ["500 000", "2 000 000", "200 000", "1 000 000"], 0,
             "At least one quarter of nominal value: 200 × 10 000 ÷ 4 = 500 000.",
             hint="One quarter of the nominal value of cash shares.",
             feedback=["", "This is the full nominal value, which can be paid within three years.",
                       "This is one tenth, not one quarter.", "This is one half."], title="Quick check 2"),
        TIP("Company formation can appear in Paper 1 multiple choice (legal rules, account numbers) and in Section B of the Financial Accounting paper "
            "(Paper 3), which the Board's 2023 report lists as company accounting and taxation. Write the account numbers and names in every journal line.",
            title="Exam link"),
        PQ("An SA is formed with 4 000 cash shares of 10 000, one quarter paid on subscription. Give the amounts in 1013 and 109 after payment.",
           "Capital 40 000 000. Paid: 10 000 000 in 1013 (called and paid). Uncalled: 30 000 000 in 1011, with 109 (contributors, uncalled) 30 000 000."),
        PQ("Give three differences between an SARL and an SA.",
           "1. Capital: an SA has a minimum of FCFA 10 000 000; an SARL's minimum is set by national law (check). "
           "2. Transfer: SA shares are in principle freely transferable (the statutes may add approval clauses); SARL parts need the partners' approval to go to outsiders. "
           "3. Management: an SARL is run by one or more managers (gérants); an SA by a board of directors or a general administrator, with a compulsory statutory auditor."),
        PQ("When does a company acquire legal personality, and why does it matter to the accountant?",
           "On registration in the RCCM. From that date the company owns its assets and owes its debts in its own name, so its accounts are separate from the "
           "founders' accounts."),
        PQ("A partner contributes a building valued at 8 000 000 to a new SA. Write the two entries.",
           "Subscription: debit 4611 Contributors, in kind 8 000 000; credit capital (1012 then 1013, or directly 1013) 8 000 000. "
           "Handover: debit 231 Buildings 8 000 000; credit 4611 8 000 000."),
        SUM("OHADA company forms: SNC (unlimited liability), SARL, SA and SAS (limited liability).",
            "SA: minimum capital FCFA 10 000 000; cash shares at least 1/4 paid on subscription, the rest within 3 years; contributions in kind fully paid and valued by an auditor.",
            "SARL capital minimum: set by national law under the Act; check the current Cameroon rule.",
            "Capital moves 1011 (uncalled) → 1012 (called, unpaid) → 1013 (called and paid); shareholders' debts are in 109, 4611, 4612 and 4613.",
            "Legal personality comes with registration in the RCCM."),
    ]))

# ====================================================================== 7. Issue of shares
_q7, _nom7, _iss7 = 3_000, 10_000, 12_500
_prem7 = (_iss7 - _nom7) * _q7
_sub7 = (_nom7 // 4 + (_iss7 - _nom7)) * _q7
_unc7 = (_nom7 - _nom7 // 4) * _q7
assert (_prem7, _sub7, _unc7) == (7_500_000, 15_000_000, 22_500_000)
_j7a = journal([
    ("(1) Subscription: 1/4 of nominal + whole premium",
     [("4612 Contributors, cash", _sub7), ("109 Contributors, uncalled", _unc7)],
     [("1011 Capital, uncalled", _unc7), ("1012 Capital called, not paid", _nom7 // 4 * _q7), ("1051 Share premium", _prem7)]),
    ("(2) Cash received", [("521 Bank", _sub7)], [("4612 Contributors, cash", _sub7)]),
    ("(3) Called capital paid", [("1012 Capital called, not paid", _nom7 // 4 * _q7)], [("1013 Capital called and paid", _nom7 // 4 * _q7)]),
])
assert _nom7 // 4 * _q7 == 7_500_000
# second call of 3 750 per share; Tita (200 shares) defaults; Nfor (100 shares) pays the final call in advance
_call7 = 3_750 * _q7
_arr7 = 3_750 * 200
_adv7 = 3_750 * 100
_bank7 = _call7 - _arr7 + _adv7
assert (_call7, _arr7, _adv7, _bank7) == (11_250_000, 750_000, 375_000, 10_875_000)
_j7b = journal([
    ("(4) Second call: 3 750 per share", [("4613 Shareholders, called unpaid", _call7)], [("109 Contributors, uncalled", _call7)]),
    ("(5) Capital status", [("1011 Capital, uncalled", _call7)], [("1012 Capital called, not paid", _call7)]),
    ("(6) Money received", [("521 Bank", _bank7)],
     [("4613 Shareholders, called unpaid", _call7 - _arr7), ("4616 Payments in advance", _adv7)]),
    ("(7) Tita is in default", [("4617 Defaulting shareholders", _arr7)], [("4613 Shareholders, called unpaid", _arr7)]),
    ("(8) Paid part of the call", [("1012 Capital called, not paid", _call7 - _arr7)], [("1013 Capital called and paid", _call7 - _arr7)]),
])
# sale of the defaulting shareholder's shares
_proc7, _int7, _cost7 = 1_100_000, 30_000, 20_000
_refund7 = _proc7 - _arr7 - _int7 - _cost7
assert _refund7 == 300_000
_led7 = ledger("4617 Defaulting shareholders (Tita)",
               [("4613: call unpaid", _arr7), ("Interest for late payment", _int7), ("Bank: costs of sale", _cost7),
                ("Bank: balance refunded to Tita", _refund7)],
               [("Bank: proceeds of sale", _proc7)])
# English-textbook forfeiture (practice question)
_ff_paid, _ff_disc = 100 * 6_000, 100 * (10_000 - 8_000)
assert (_ff_paid, _ff_disc, _ff_paid - _ff_disc) == (600_000, 200_000, 400_000)
# practice figures
assert 2_000 * (2_500 + 1_500) == 8_000_000 and 2_000 * 1_500 == 3_000_000
assert 10_000 // 4 + 3_000 == 5_500 and 500_000 + 15_000 + 10_000 - 450_000 == 75_000

LESSONS.append(lesson(
    module=M_COMP, topic="Issue of shares",
    title="Issue of shares: premium, calls, payments in advance and defaulting shareholders",
    slug="acu1-issue-of-shares", minutes=25,
    summary="Record an issue of shares at a premium, the calls on capital, payments made in advance and calls in arrears, and the sale of a defaulting "
            "shareholder's shares (with the English-textbook forfeiture method for comparison).",
    objectives=[
        "Calculate the amount payable on subscription when shares are issued at a premium",
        "Record calls, payments in advance and calls in arrears with the SYSCOHADA accounts",
        "Account for the sale of a defaulting shareholder's shares and the refund of any surplus",
        "Compare the OHADA treatment with forfeiture and reissue in English textbooks",
    ],
    key_concepts=["Nominal value", "Issue price", "Share premium", "Call", "Calls in advance", "Calls in arrears",
                  "Defaulting shareholder", "Forfeiture"],
    blocks=[
        H("Shares are not always issued at nominal value"),
        T("Bamenda Dairy SA has been profitable for years. When it issues new shares, a buyer pays more than the nominal value of 10 000, because each "
          "share gives a claim on reserves and future profits. The extra amount is the **share premium**. Shareholders do not always pay what is "
          "called on time: some pay early and some not at all. This lesson records all these cases. Figures are **invented for practice**."),
        D("The **nominal value** (par value) is the face value of a share fixed by the statutes. The **issue price** is what the subscriber pays. "
          "**Share premium** (prime d'émission, account 1051) = issue price − nominal value. It belongs to the shareholders but is **not** capital.",
          title="Nominal value, issue price, premium"),
        KEY("What must be paid on subscription?", "For cash shares in an SA:",
            cards=[["Capital", "At least one quarter of the nominal value."],
                   ["Premium", "The whole premium, at once."],
                   ["Later", "The rest of the nominal value, on calls by the board within three years."]]),
        EX("Worked example 1: issue at a premium",
           intro="Bamenda Dairy SA issues 3 000 shares of nominal value 10 000 at 12 500. On subscription the minimum legal amount is paid.",
           steps=[
               S("Premium", text="12 500 − 10 000 = 2 500 per share; 3 000 × 2 500 = 7 500 000."),
               S("Paid on subscription", text="2 500 (quarter of nominal) + 2 500 (premium) = 5 000 per share; 3 000 × 5 000 = 15 000 000."),
               S("Uncalled capital", text="7 500 per share; 3 000 × 7 500 = 22 500 000."),
               S("Entries", text="Credit 1051 with the premium, 1012 with the called capital and 1011 with the uncalled capital."),
           ]),
        CODE(_j7a, "text", title="Journal: issue at a premium (invented for practice)"),
        H("Calls, payments in advance and arrears"),
        D("A **call** is a demand by the company for part of the unpaid capital. **Payments in advance** (calls in advance, account 4616) are amounts a "
          "shareholder pays before they are called: they are a debt of the company until the call is made. **Calls in arrears** are amounts called but not "
          "paid: the shareholder becomes a **defaulting shareholder** (account 4617) and usually owes interest for late payment.",
          title="Three words"),
        EX("Worked example 2: a call with an early payer and a defaulter",
           intro="The board calls 3 750 per share on the 3 000 shares. Tita, who holds 200 shares, pays nothing. Nfor, who holds 100 shares, pays this call and "
                 "also the final call of 3 750 in advance.",
           steps=[
               S("Amount called", text="3 000 × 3 750 = 11 250 000."),
               S("Arrears", text="Tita: 200 × 3 750 = 750 000."),
               S("In advance", text="Nfor: 100 × 3 750 = 375 000 (for the final call)."),
               S("Bank receives", text="11 250 000 − 750 000 + 375 000 = 10 875 000."),
               S("Capital paid", text="Only 10 500 000 of this call is transferred to 1013; Tita's 750 000 stays in 1012 until it is paid."),
           ]),
        CODE(_j7b, "text", title="Journal: second call"),
        H("Selling a defaulting shareholder's shares"),
        T("Under OHADA law, if a shareholder does not pay after a formal notice (**mise en demeure**), the company may sell his shares. The proceeds pay what he owes "
          "(the call, interest for late payment and the costs of sale). Any surplus is refunded to him; any shortfall remains his debt. "
          "Check your textbook for the waiting periods and for the exact accounts it uses."),
        EX("Worked example 3: sale of Tita's shares",
           intro="Tita's 200 shares are sold for 1 100 000. He owes the call of 750 000 and interest for late payment of 30 000; the costs of sale are 20 000.",
           steps=[
               S("What Tita owes", text="750 000 + 30 000 + 20 000 = 800 000."),
               S("Surplus refunded", text="1 100 000 − 800 000 = 300 000 paid to Tita."),
               S("Capital", text="The company now has the call money: debit 1012, credit 1013 for 750 000. The buyer becomes the shareholder."),
           ]),
        CODE(_led7, "text", title="Account 4617 closes at zero"),
        KEY("Forfeiture in English textbooks", "Some A Level books use the English method. Learn it if your class uses it; check your textbook.",
            cards=[["Forfeit", "Debit share capital with the amount called on the shares; credit the unpaid calls, and credit a forfeited shares account with what the shareholder had paid."],
                   ["Reissue", "Debit bank with the reissue price and forfeited shares with any discount; credit share capital."],
                   ["Close", "The balance of forfeited shares is a gain: transfer it to a capital reserve."]]),
        MISTAKE("Calling only a quarter of the premium",
                "The premium is paid in full on subscription; only the nominal value can be paid in stages."),
        MISTAKE("Crediting capital with calls in advance",
                "Money paid in advance is a liability (4616) until the call is made; it is not yet paid-up capital."),
        MISTAKE("Keeping all the proceeds of the defaulter's shares",
                "The company keeps only what the defaulter owes; the surplus is refunded to him."),
        QUIZ("Shares of nominal value 10 000 are issued at 13 000. What is the minimum amount payable per share on subscription?",
             ["2 500", "5 500", "3 000", "13 000"], 1,
             "A quarter of nominal (2 500) plus the whole premium (3 000) = 5 500.",
             hint="Quarter of nominal value plus all of the premium.",
             feedback=["This forgets the premium.", "", "This is only the premium.", "The nominal value can be paid in stages."]),
        QUIZ("A shareholder pays 400 000 for a call that has not yet been made. Where is it credited?",
             ["1013 Capital called and paid", "1051 Share premium", "4617 Defaulting shareholders", "4616 Payments in advance"], 3,
             "It is a debt of the company to the shareholder until the call is made.",
             hint="Has the company asked for this money yet?",
             feedback=["Capital is credited only when the call is made and paid.", "Premium is the excess of issue price over nominal value.",
                       "4617 is for shareholders who have NOT paid.", ""], title="Quick check 2"),
        TIP("Issues of shares appear in Paper 1 multiple choice and in Section B of Paper 3 (company accounting). Show the per-share working (quarter, premium, "
            "uncalled) before the journal, and name each account.", title="Exam link"),
        PQ("2 000 shares of 10 000 are issued at 11 500, with the legal minimum paid on subscription. Find the cash received and the premium.",
           "Per share: 2 500 + 1 500 = 4 000; cash 2 000 × 4 000 = 8 000 000. Premium 2 000 × 1 500 = 3 000 000."),
        PQ("A defaulting shareholder owes a call of 500 000, interest 15 000 and sale costs 10 000. His shares are sold for 450 000. What happens?",
           "He owes 525 000; the sale brings 450 000, so a shortfall of 75 000 remains his debt (the 4617 account keeps a debit balance of 75 000)."),
        PQ("English method: 100 shares of 10 000, fully called, are forfeited after the holder paid 6 000 per share. They are reissued at 8 000 each, fully paid. "
           "Find the amount transferred to capital reserve.",
           "Forfeited shares account is credited with the 600 000 paid. Discount on reissue: 100 × 2 000 = 200 000 (debit). Balance 400 000 to capital reserve."),
        PQ("Explain why a share premium is not part of share capital, and who it belongs to.",
           "Capital is fixed at the nominal value in the statutes. The premium is an extra amount paid by new shareholders so that they do not take a share of "
           "existing reserves for free. It belongs to all shareholders as a reserve-like item (1051) and can later be incorporated into capital."),
        SUM("Premium = issue price − nominal value; it is paid in full at subscription and credited to 1051.",
            "Cash shares: at least 1/4 of nominal on subscription, the rest on calls within three years.",
            "Calls: debit 4613, credit 109; then 1011 → 1012; payment moves 1012 → 1013.",
            "Payments in advance go to 4616; calls in arrears move to 4617 (defaulting shareholders).",
            "A defaulter's shares can be sold; he receives any surplus and owes any shortfall. English books use forfeiture and reissue."),
    ]))

# ====================================================================== 8. Appropriation of company profits
_cap8, _sh8, _lr8_old, _np8, _rbf8 = 50_000_000, 5_000, 8_000_000, 18_600_000, 340_000
_lr8 = min(_np8 // 10, _cap8 // 5 - _lr8_old)
assert _np8 % 10 == 0 and _lr8 == 1_860_000
_dist8 = _np8 - _lr8 + _rbf8
_stat8 = (_np8 - _lr8) * 5 // 100
assert _dist8 == 17_080_000 and _stat8 == 837_000 and (_np8 - _lr8) * 5 % 100 == 0
_fd8 = _cap8 * 6 // 100
_fd8ps = _fd8 // _sh8
_rest8 = _dist8 - _stat8 - _fd8 - 2_000_000
_sd8ps = (_rest8 // _sh8) // 100 * 100
_sd8 = _sd8ps * _sh8
_rnf8 = _rest8 - _sd8
assert (_fd8, _fd8ps, _rest8, _sd8ps, _sd8, _rnf8) == (3_000_000, 600, 11_243_000, 2_200, 11_000_000, 243_000)
_div8 = _fd8 + _sd8
_ircm8 = _div8 * 165 // 1000
assert _div8 == 14_000_000 and _ircm8 == 2_310_000 and _div8 * 165 % 1000 == 0
_netps8 = (_fd8ps + _sd8ps) * 835 // 1000
assert _netps8 == 2_338 and (_fd8ps + _sd8ps) * 835 % 1000 == 0 and _netps8 * _sh8 == _div8 - _ircm8
_t_app8 = "\n".join([
    "Appropriation of the profit for the year",
    r("Net profit for the year", None, _np8),
    r("Less legal reserve (10%)", None, _lr8),
    r("", None, _np8 - _lr8),
    r("Add profit brought forward", None, _rbf8),
    r("Distributable profit", None, _dist8),
    r("Less statutory reserve 5%", None, _stat8),
    r("Less first dividend 6%", None, _fd8),
    r("Less optional reserve", None, 2_000_000),
    r("Available for super dividend", None, _rest8),
    r("Super dividend 2 200 x 5 000", None, _sd8),
    r("Profit carried forward", None, _rnf8),
])
assert _np8 - _lr8 + _rbf8 - _stat8 - _fd8 - 2_000_000 - _sd8 == _rnf8
_j8 = journal([
    ("Appropriation decided by the general meeting",
     [("131 Net profit for the year", _np8), ("121 Profit brought forward", _rbf8)],
     [("111 Legal reserve", _lr8), ("112 Statutory reserve", _stat8), ("118 Other reserves", 2_000_000),
      ("465 Dividends payable", _div8), ("121 Profit brought forward", _rnf8)]),
    ("Tax withheld on dividends (IRCM, teaching rate)", [("465 Dividends payable", _ircm8)], [("447 State, tax withheld", _ircm8)]),
    ("Net dividends paid", [("465 Dividends payable", _div8 - _ircm8)], [("521 Bank", _div8 - _ircm8)]),
])
# example 2: legal reserve capped and prior losses
_base8b = 6_000_000 - 1_000_000
_lr8b = min(_base8b // 10, 20_000_000 // 5 - 3_600_000)
assert _base8b // 10 == 500_000 and _lr8b == 400_000
# example 3: partly paid shares
_fd_full, _fd_part = 10_000 * 6 // 100, 2_500 * 6 // 100
assert (_fd_full, _fd_part) == (600, 150)
_tot8c = 4_000 * (_fd_full + 1_000) + 2_000 * (_fd_part + 1_000)
assert _tot8c == 6_400_000 + 2_300_000 == 8_700_000
# practice question figures
assert min(9_000_000 // 10, 30_000_000 // 5 - 5_500_000) == 500_000
assert (7_350 // 100) * 100 == 7_300 and 4_000 * 165 // 1000 == 660
assert min((12_000_000 - 2_000_000) // 10, 40_000_000 // 5 - 7_000_000) == 1_000_000 and 12_000_000 - 2_000_000 - 1_000_000 == 9_000_000
assert (9_000_000 - 2_000_000) // 4_000 == 1_750 and 4_000 * 1_700 == 6_800_000 and 7_000_000 - 6_800_000 == 200_000 and 2_800 * 165 // 1000 == 462

LESSONS.append(lesson(
    module=M_COMP, topic="Appropriation of company profits",
    title="Appropriation of company profits: reserves, dividends and the IRCM",
    slug="acu1-company-profit-appropriation", minutes=25,
    summary="Share an SA's profit as OHADA law and the statutes require: the legal reserve, statutory and optional reserves, the first dividend and super "
            "dividend, the balance carried forward, and the tax withheld on dividends (IRCM).",
    objectives=[
        "Calculate the legal reserve: one tenth of the profit (after prior losses) until the reserve reaches one fifth of the capital",
        "Find the distributable profit and appropriate it in the order set by the statutes",
        "Calculate the first dividend and a super dividend rounded per share, with the balance carried forward",
        "Record the appropriation, the tax withheld on dividends and the payment",
    ],
    key_concepts=["Legal reserve", "Statutory reserve", "Optional reserve", "Distributable profit", "First dividend",
                  "Super dividend", "Retained profit (report à nouveau)", "IRCM"],
    blocks=[
        H("Who decides what happens to the profit?"),
        T("Bamenda Dairy SA made a profit. The directors cannot simply pay it all out. OHADA law requires a reserve to protect creditors, the statutes add "
          "their own rules, and only then does the **ordinary general meeting** of shareholders decide on dividends. The accountant prepares the "
          "appropriation table. All figures are **invented for practice**."),
        D("Each year at least **one tenth (10%)** of the profit for the year, **minus any losses brought forward**, must be put to the **legal reserve** "
          "(account 111). The allocation stops being compulsory when the legal reserve reaches **one fifth (20%) of the share capital**.",
          title="Legal reserve (OHADA Uniform Act)"),
        D("**Distributable profit** = profit for the year − losses brought forward − legal and statutory reserves + profit brought forward (credit balance of 121).",
          title="Distributable profit"),
        IMG("alacu1-company-profit-appropriation.svg",
            alt="Column of steps: net profit, minus losses brought forward, minus legal reserve, minus statutory reserves, plus profit brought forward, gives "
                "distributable profit, then first dividend, optional reserves, super dividend, and the remainder carried forward.",
            caption="Figure 1. Order of appropriation in a typical set of statutes. Check the order in each question."),
        KEY("Reserves and dividends", "The statutes decide the details.",
            cards=[["Statutory reserve (112)", "Required by the company's own statutes, e.g. 5% of profit."],
                   ["Optional reserve (118)", "Voted freely by the general meeting."],
                   ["First dividend", "A statutory interest on paid-up capital not yet amortized, e.g. 6%."],
                   ["Super dividend", "An extra equal amount per share, usually rounded down; the remainder is carried forward (121)."]]),
        D("Dividends paid to shareholders are taxed by withholding: the company keeps the **IRCM** (impôt sur le revenu des capitaux mobiliers) and pays it to "
          "the State. This lesson uses a **teaching rate of 16.5%** (15% plus a 10% additional council tax on it). Check the current Finance Law and your textbook.",
          title="Tax on dividends (IRCM)"),
        EX("Worked example 1: full appropriation",
           intro="Capital 50 000 000 (5 000 fully paid shares of 10 000). Legal reserve already 8 000 000. Profit for the year 18 600 000; profit brought forward "
                 "340 000. Statutes: legal reserve, then 5% statutory reserve on profit after legal reserve, first dividend 6%, and the meeting votes an optional "
                 "reserve of 2 000 000 and a super dividend rounded down to the nearest 100 per share.",
           steps=[
               S("Legal reserve", text="10% × 18 600 000 = 1 860 000. Ceiling: 20% × 50 000 000 = 10 000 000; 8 000 000 + 1 860 000 is below it."),
               S("Distributable profit", text="18 600 000 − 1 860 000 + 340 000 = 17 080 000."),
               S("Statutory reserve", text="5% × (18 600 000 − 1 860 000) = 837 000."),
               S("First dividend", text="6% × 50 000 000 = 3 000 000, i.e. 600 per share."),
               S("Super dividend", text="17 080 000 − 837 000 − 3 000 000 − 2 000 000 = 11 243 000; ÷ 5 000 = 2 248.6, rounded down to 2 200 per share = 11 000 000. "
                                         "Carried forward: 243 000."),
           ]),
        CODE(_t_app8, "text", title="Appropriation table (invented for practice)"),
        CODE(_j8, "text", title="Journal: appropriation, IRCM and payment"),
        T("Gross dividend per share = 600 + 2 200 = 2 800. With the 16.5% teaching rate, IRCM = 462 and the shareholder receives **2 338** net per share "
          "(2 310 000 withheld in total)."),
        EX("Worked example 2: ceiling and prior losses",
           intro="Capital 20 000 000; legal reserve 3 600 000; profit 6 000 000; losses brought forward 1 000 000. Find the legal reserve allocation.",
           steps=[
               S("Base", text="6 000 000 − 1 000 000 = 5 000 000; 10% = 500 000."),
               S("Ceiling", text="20% × 20 000 000 = 4 000 000; room left = 4 000 000 − 3 600 000 = 400 000."),
               S("Allocation", text="The smaller amount: 400 000. After this the reserve is at its ceiling and further allocations are optional."),
           ]),
        EX("Worked example 3: shares not fully paid",
           intro="4 000 shares are fully paid (10 000) and 2 000 shares are paid up by one quarter (2 500). The first dividend is 6% of the amount paid up, and a "
                 "super dividend of 1 000 is given to every share. Find the total dividend.",
           steps=[
               S("First dividend per share", text="Fully paid: 6% × 10 000 = 600. Quarter paid: 6% × 2 500 = 150."),
               S("Total per share", text="1 600 and 1 150."),
               S("Total", text="4 000 × 1 600 + 2 000 × 1 150 = 6 400 000 + 2 300 000 = 8 700 000."),
           ]),
        MISTAKE("Taking 10% for the legal reserve after it has reached its ceiling",
                "Always compare 10% of the profit (after prior losses) with the room left below 20% of capital and take the smaller."),
        MISTAKE("Adding the profit brought forward before the legal reserve",
                "The legal reserve is calculated on the profit of the year less losses brought forward, not on profit brought forward."),
        MISTAKE("Paying the gross dividend to shareholders",
                "The company withholds the IRCM and pays it to the State; shareholders receive the net dividend."),
        QUIZ("Capital 30 000 000; legal reserve 5 500 000; profit for the year 9 000 000, no losses brought forward. What is the legal reserve allocation?",
             ["900 000", "6 000 000", "500 000", "Nil"], 2,
             "10% × 9 000 000 = 900 000, but the ceiling is 6 000 000 and only 500 000 of room is left.",
             hint="Compare 10% of profit with the room left below 20% of capital.",
             feedback=["This ignores the ceiling of 20% of capital.", "This is the ceiling itself, not the allocation.", "",
                       "The reserve has not yet reached its ceiling, so an allocation is still required."]),
        QUIZ("After the first dividend, 7 350 per share is available for a super dividend, rounded down to the nearest 100. What happens to the rest?",
             ["It is paid as a cash bonus", "It is carried forward in 121 (profit brought forward)", "It is added to the legal reserve",
              "It is paid to the State"], 1,
             "The super dividend is 7 300; the remaining 50 per share is carried forward to the next year in 121.",
             hint="Where does undistributed profit wait?",
             feedback=["Only the declared dividend is paid.", "", "The legal reserve takes only its legal allocation.",
                       "Tax is withheld on dividends paid, not on profit carried forward."], title="Quick check 2"),
        TIP("Appropriation of profits is a Paper 1 favourite (legal reserve, distributable profit) and appears in Section B of Paper 3. "
            "Lay out a vertical table, then the journal entry. Show the ceiling check for the legal reserve.", title="Exam link"),
        PQ("Capital 40 000 000 (4 000 shares). Legal reserve 7 000 000. Profit 12 000 000; loss brought forward 2 000 000. Find the legal reserve allocation "
           "and the distributable profit (no statutory reserve).",
           "Base 10 000 000; 10% = 1 000 000; room 8 000 000 − 7 000 000 = 1 000 000; allocation 1 000 000. "
           "Distributable = 12 000 000 − 2 000 000 − 1 000 000 = 9 000 000."),
        PQ("Continue: the first dividend is 5% and the rest is paid as a super dividend rounded down to the nearest 100 per share. Find the dividend per share "
           "and the amount carried forward.",
           "First dividend 5% × 40 000 000 = 2 000 000 (500 per share). Remainder 7 000 000 ÷ 4 000 = 1 750 → 1 700 per share = 6 800 000. "
           "Total dividend 2 200 per share; carried forward 200 000."),
        PQ("A shareholder receives a gross dividend of 4 000 per share. Using the 16.5% teaching rate, find the IRCM withheld per share and the net dividend.",
           "IRCM = 16.5% × 4 000 = 660; net = 3 340 per share. (Check the current rate with the Finance Law.)"),
        PQ("Why does OHADA law require a legal reserve?",
           "To protect creditors: profits kept in the company strengthen its equity and cannot be distributed, so the company is better able to bear future losses "
           "and pay its debts. The ceiling (20% of capital) stops the rule from blocking dividends forever."),
        SUM("Legal reserve: 10% of (profit − losses brought forward) until it reaches 20% of capital; take the smaller of 10% and the room left.",
            "Distributable profit = profit − losses b/f − legal and statutory reserves + profit b/f.",
            "First dividend on paid-up, unamortized capital; super dividend rounded per share; remainder carried forward (121).",
            "Entries: debit 131 (and 121), credit 111, 112, 118, 465 and 121.",
            "The company withholds IRCM on dividends (teaching rate 16.5%; check the Finance Law) and pays the net dividend."),
    ]))

# ====================================================================== 9. Debentures (bonds)
_nb9, _nom9, _ip9, _rp9, _rate9, _yrs9 = 10_000, 10_000, 9_800, 10_200, 8, 5
_cash9 = _nb9 * _ip9
_redv9 = _nb9 * _rp9
_prem9 = _redv9 - _cash9
assert (_cash9, _redv9, _prem9) == (98_000_000, 102_000_000, 4_000_000)
_j9a = journal([
    ("Issue of 10 000 bonds at 9 800, redeemable at 10 200",
     [("Bond subscribers", _cash9), ("Bond redemption premium", _prem9)], [("161 Bond loan (redemption value)", _redv9)]),
    ("Subscriptions received", [("521 Bank", _cash9)], [("Bond subscribers", _cash9)]),
])
_rows9 = []
_out = _nb9
for _y in range(1, _yrs9 + 1):
    _int = _out * _nom9 * _rate9 // 100
    _red = 2_000 * _rp9
    _rows9.append((_y, _out, _int, 2_000, _red, _int + _red))
    _out -= 2_000
assert _out == 0
assert [x[2] for x in _rows9] == [8_000_000, 6_400_000, 4_800_000, 3_200_000, 1_600_000]
assert [x[5] for x in _rows9] == [28_400_000, 26_800_000, 25_200_000, 23_600_000, 22_000_000]
assert sum(x[4] for x in _rows9) == _redv9
_t_sched9 = "\n".join(["Yr  Bonds left  Interest 8%  Redeemed    Repayment      Annuity"] +
                      [f"{y:<3}{n(o):>10}{n(i):>13}{n(b):>10}{n(rd):>13}{n(a):>13}" for y, o, i, b, rd, a in _rows9] +
                      [f"{'Tot':<3}{'':>10}{n(sum(x[2] for x in _rows9)):>13}{n(10_000):>10}{n(_redv9):>13}{n(sum(x[5] for x in _rows9)):>13}"])
assert sum(x[2] for x in _rows9) == 24_000_000 and sum(x[5] for x in _rows9) == 126_000_000
_am9 = _prem9 // _yrs9
assert _am9 == 800_000
_j9b = journal([
    ("End of year 1: interest", [("671 Interest on bond loans", 8_000_000)], [("521 Bank", 8_000_000)]),
    ("End of year 1: 2 000 bonds redeemed at 10 200", [("161 Bond loan (redemption value)", 20_400_000)], [("521 Bank", 20_400_000)]),
    ("Premium written off (straight-line)", [("Amortization of bond premium", _am9)], [("Bond redemption premium", _am9)]),
])
# constant annuity (redemption at par, for the formula)
_C, _i, _N = 100_000_000, 0.08, 5
_a = _C * _i / (1 - (1 + _i) ** -_N)
assert round(_a) == 25_045_645 and round(_a - 8_000_000) == 17_045_645
assert abs((_a - 8_000_000) / 10_000 - 1_704.56) < 0.01
# accrued interest practice question: 50 000 000 at 9%, interest paid each 30 September, year end 31 December
assert 50_000_000 * 9 * 3 // (100 * 12) == 1_125_000
assert 5_000 * 10_000 * 12 // 100 == 6_000_000 and 5_000 * (10_500 - 9_900) == 3_000_000

LESSONS.append(lesson(
    module=M_COMP, topic="Debentures",
    title="Debentures (bonds): issue, interest, redemption schedule and redemption premium",
    slug="acu1-debentures", minutes=25,
    summary="A bond (debenture) loan raises long-term money from many lenders. Record its issue below par and redemption above par, build a redemption "
            "schedule by equal instalments, understand the constant-annuity formula, and write off the redemption premium.",
    objectives=[
        "Explain nominal value, issue price, redemption price and redemption premium of a bond",
        "Record the issue of a bond loan and the payment of interest",
        "Prepare a redemption schedule by equal instalments and calculate a constant annuity",
        "Compare bonds with shares as a source of finance",
    ],
    key_concepts=["Debenture (bond, obligation)", "Nominal value", "Issue price", "Redemption price",
                  "Redemption premium", "Coupon interest", "Redemption schedule", "Constant annuity"],
    blocks=[
        H("Borrowing from many lenders"),
        T("A cement company in Douala needs 100 000 000 for a new kiln. Shareholders do not want to give up control, and one bank will not lend it all. The company "
          "issues a **bond loan** (emprunt obligataire): 10 000 bonds of 10 000 each, sold to many investors. In English textbooks bonds are often called "
          "**debentures**. Under OHADA law bonds are issued mainly by public limited companies (SA); check your textbook for the conditions. All figures are **invented for practice**."),
        D("A **bond** is a negotiable security giving its holder the right to interest each year and to repayment at a set date. Bondholders are **creditors**, not owners: "
          "they do not vote, and interest is an expense that must be paid whether or not there is a profit.", title="Bond (obligation)"),
        KEY("Four prices of a bond", "Interest is always calculated on the nominal value.",
            cards=[["Nominal value", "The face value (10 000), the base for interest."],
                   ["Issue price", "What the subscriber pays (here 9 800: issued below par)."],
                   ["Redemption price", "What the company repays (here 10 200: redeemed above par)."],
                   ["Redemption premium", "Redemption price − issue price, a cost of borrowing spread over the life of the loan."]]),
        EX("Worked example 1: the issue",
           intro="10 000 bonds of nominal value 10 000 are issued at 9 800, redeemable at 10 200, interest 8% a year, redeemed over 5 years.",
           steps=[
               S("Cash raised", text="10 000 × 9 800 = 98 000 000."),
               S("Amount to repay", text="10 000 × 10 200 = 102 000 000."),
               S("Redemption premium", text="102 000 000 − 98 000 000 = 4 000 000."),
               S("Entry", text="Credit the bond loan with the redemption value; debit subscribers with the cash and the premium account with the difference."),
           ]),
        CODE(_j9a, "text", title="Journal: issue (invented for practice)"),
        T("Many textbooks record the bond loan at its redemption value, as here, with the premium as a separate debit balance that is written off over the life "
          "of the loan. Account numbers and the exact method vary: check your textbook."),
        H("Redemption by equal instalments"),
        EX("Worked example 2: redemption schedule",
           intro="The company redeems 2 000 bonds at the end of each year. Prepare the schedule.",
           steps=[
               S("Interest", text="8% of the nominal value of bonds still outstanding: year 1, 10 000 × 10 000 × 8% = 8 000 000; year 2, 8 000 × 10 000 × 8% = 6 400 000; and so on."),
               S("Repayment", text="2 000 × 10 200 = 20 400 000 each year."),
               S("Annuity", text="Interest + repayment: 28 400 000 in year 1, falling by 1 600 000 a year to 22 000 000."),
               S("Check", text="Total repaid 102 000 000 = redemption value of all bonds; total interest 24 000 000."),
           ]),
        CODE(_t_sched9, "text", title="Redemption schedule (amounts in FCFA)"),
        IMG("alacu1-bond-annuities.svg",
            alt="Bar chart of five yearly annuities: a constant redemption part of 20.4 million and an interest part falling from 8 million to 1.6 million.",
            caption="Figure 1. Equal redemptions: the annuity falls because interest falls."),
        CODE(_j9b, "text", title="Journal: year 1"),
        T("The premium of 4 000 000 is written off here by the straight-line method (800 000 a year). Some textbooks write it off in proportion to the interest "
          "of each year, which gives larger amounts in early years. Use the method your question gives."),
        H("Redemption by constant annuity"),
        F(r"a = C \times \frac{i}{1 - (1 + i)^{-n}}", title="Constant annuity"),
        T("Here C is the amount borrowed (at nominal value), i the interest rate and n the number of years. For C = 100 000 000, i = 8% and n = 5 (redemption at par): "
          "a ≈ 25 045 645. Year 1 interest is 8 000 000, so about 17 045 645 of capital is repaid, which is about 1 705 bonds. Because bonds are repaid in whole "
          "numbers, the number redeemed each year is rounded and the annuity is only approximately constant. Check your textbook's rounding method. "
          "A third method, **in fine**, repays all bonds at the end and pays only interest before that."),
        EX("Worked example 3: the constant annuity",
           intro="Find the constant annuity for a loan of 100 000 000 at 8% over 5 years, and the capital repaid in year 1.",
           steps=[
               S("Factor", math=r"\frac{0.08}{1 - 1.08^{-5}} \approx 0.250456"),
               S("Annuity", math=r"a \approx 100\,000\,000 \times 0.250456 \approx 25\,045\,645"),
               S("Capital repaid in year 1", text="25 045 645 − 8 000 000 (interest) ≈ 17 045 645, about 1 705 bonds of 10 000."),
           ]),
        MISTAKE("Calculating interest on the issue price",
                "Interest is on the nominal value of the bonds still outstanding, never on the issue or redemption price."),
        MISTAKE("Treating bond interest as an appropriation of profit",
                "Bondholders are lenders: interest is a financial expense (671) charged before profit."),
        MISTAKE("Forgetting the redemption premium",
                "When the issue price is below the redemption price, the difference is a cost to spread over the life of the loan."),
        QUIZ("5 000 bonds of nominal value 10 000 carry 12% interest. They were issued at 9 900 and are redeemable at 10 500. What is the yearly interest?",
             ["5 940 000", "6 300 000", "6 000 000", "3 000 000"], 2,
             "12% × 5 000 × 10 000 = 6 000 000. Interest uses the nominal value.",
             hint="Which of the three prices is used for interest?",
             feedback=["This uses the issue price.", "This uses the redemption price.", "", "This is the redemption premium, (10 500 − 9 900) × 5 000."]),
        QUIZ("Which statement about bondholders is correct?",
             ["They vote at the general meeting", "They are creditors who receive interest even when there is no profit",
              "They receive dividends from the distributable profit", "They are repaid after the shareholders on liquidation"], 1,
             "Bondholders lend money; interest is a contractual expense.",
             hint="Are bondholders owners or lenders?",
             feedback=["Only shareholders vote.", "", "Dividends are paid to shareholders.", "Creditors, including bondholders, are paid before shareholders."],
             title="Quick check 2"),
        TIP("Bond loans can appear in Paper 1 multiple choice and in Section B of Paper 3. Build the schedule in a table with a check line (total repaid = redemption "
            "value), then write the journal entries for the year asked.", title="Exam link"),
        PQ("A bond loan of 50 000 000 at 9% pays interest every 30 September. The year ends on 31 December. Find the accrued interest at the year end.",
           "Three months (October to December): 50 000 000 × 9% × 3/12 = 1 125 000. Debit interest expense, credit accrued interest payable."),
        PQ("5 000 bonds of 10 000 are issued at 9 900, redeemable at 10 500. Find the redemption premium.",
           "Redemption value 52 500 000 − cash raised 49 500 000 = 3 000 000 (600 per bond)."),
        PQ("For the schedule in example 2, find the annuity in year 4 and explain why it is lower than in year 1.",
           "Bonds outstanding at the start of year 4: 4 000. Interest 4 000 × 10 000 × 8% = 3 200 000; repayment 20 400 000; annuity 23 600 000. "
           "It is lower because interest is charged only on the bonds still outstanding."),
        PQ("Evaluate bonds compared with new shares as a way for an SA to raise 100 000 000.",
           "For bonds: no loss of control (bondholders do not vote); interest is a deductible expense for tax (check the rules); existing shareholders keep all extra profit. "
           "Against: interest must be paid even in bad years and the capital must be repaid, so gearing and risk rise. Shares carry no fixed charge but dilute control. "
           "Conclusion: bonds suit a company with stable profits and cash flows."),
        SUM("Interest = rate × nominal value of bonds outstanding; it is an expense (671), not an appropriation.",
            "Redemption premium = redemption price − issue price, spread over the life of the loan.",
            "Equal instalments: same number of bonds each year, so the annuity falls as interest falls.",
            "Constant annuity: a = C × i ÷ (1 − (1 + i)^−n); bonds redeemed each year are rounded.",
            "Bondholders are creditors: no vote, paid before shareholders."),
    ]))

# ====================================================================== 10. Increase of capital
_N10, _nom10, _assets10, _liab10 = 4_000, 10_000, 85_000_000, 25_000_000
_eq10 = _assets10 - _liab10
_V0 = Fr(_eq10, _N10)
assert _eq10 == 60_000_000 and _V0 == 15_000
# cash issue 1 for 4 at 12 000
_n10, _E10 = 1_000, 12_000
_V1 = Fr(_eq10 + _n10 * _E10, _N10 + _n10)
_DS = _V0 - _V1
assert _V1 == 14_400 and _DS == 600 and (_V0 - _E10) * Fr(_n10, _N10 + _n10) == _DS
assert 4 * _V0 == 60_000 and 5 * _V1 == 60_000 + 12_000 and 4 * _V1 + 4 * _DS == 60_000
assert 50 // 4 == 12 and 50 - 12 * 4 == 2
_j10a = journal([
    ("Subscription of 1 000 new shares at 12 000 (fully paid)", [("4612 Contributors, cash", 12_000_000)],
     [("1013 Capital called and paid", 10_000_000), ("1051 Share premium", 2_000_000)]),
    ("Cash received", [("521 Bank", 12_000_000)], [("4612 Contributors, cash", 12_000_000)]),
])
# bonus issue 1 for 4 from reserves (alone)
_Vb = Fr(_eq10, _N10 + 1_000)
_DA = _V0 - _Vb
assert _Vb == 12_000 and _DA == 3_000 and _V0 * Fr(1_000, 5_000) == _DA
# double increase: cash 1 for 4 then bonus 1 for 5
_V2 = Fr(_eq10 + 12_000_000, 6_000)
_DA2 = _V1 - _V2
assert _V2 == 12_000 and _DA2 == 2_400 and _V1 * Fr(1, 6) == _DA2
_t_eq10 = "\n".join([
    f"{'Equity at each stage':<26}{'Before':>12}{'After cash':>12}{'After bonus':>12}",
    f"{'Capital':<26}{n(40_000_000):>12}{n(50_000_000):>12}{n(60_000_000):>12}",
    f"{'Share premium':<26}{n(0):>12}{n(2_000_000):>12}{n(2_000_000):>12}",
    f"{'Reserves':<26}{n(20_000_000):>12}{n(20_000_000):>12}{n(10_000_000):>12}",
    f"{'Equity (net assets)':<26}{n(60_000_000):>12}{n(72_000_000):>12}{n(72_000_000):>12}",
    f"{'Number of shares':<26}{n(4_000):>12}{n(5_000):>12}{n(6_000):>12}",
    f"{'Value per share':<26}{n(_V0):>12}{n(_V1):>12}{n(_V2):>12}",
])
assert 40_000_000 + 20_000_000 == 60_000_000 and 50_000_000 + 2_000_000 + 20_000_000 == 72_000_000 == 60_000_000 + 2_000_000 + 10_000_000
_j10b = journal([("Bonus issue: 1 000 free shares from reserves", [("118 Other reserves", 10_000_000)], [("1013 Capital called and paid", 10_000_000)])])
# conversion of debt practice question
assert 800 * 12_500 == 10_000_000 and 800 * 10_000 == 8_000_000
# practice question figures
_pqV0 = Fr(48_000_000, 3_000)
_pqV1 = Fr(48_000_000 + 1_000 * 12_000, 4_000)
assert _pqV0 == 16_000 and _pqV1 == 15_000 and _pqV0 - _pqV1 == 1_000 and (16_000 - 12_000) * Fr(1, 4) == 1_000
assert Fr(48_000_000, 4_000) == 12_000 and 16_000 - 12_000 == 4_000

LESSONS.append(lesson(
    module=M_MOD, topic="Increase of capital",
    title="Increase of capital: cash issues, bonus issues, DS and DA",
    slug="acu1-increase-of-capital", minutes=25,
    summary="Value a share by net assets, then record and analyse capital increases by new cash (with a preferential subscription right, DS), by "
            "incorporation of reserves (with an attribution right, DA), by conversion of debt, and a double increase.",
    objectives=[
        "Calculate the mathematical (book) value of a share from the net assets",
        "Calculate the theoretical value after a cash issue and the preferential subscription right (DS)",
        "Calculate the value after a bonus issue and the attribution right (DA), including a double increase",
        "Record capital increases by cash, incorporation of reserves and conversion of debt",
    ],
    key_concepts=["Mathematical value of a share", "Issue price", "Preferential subscription right (DS)",
                  "Attribution right (DA)", "Incorporation of reserves (bonus issue)", "Conversion of debt", "Double increase"],
    blocks=[
        H("Why increase capital?"),
        T("Littoral Plastics SA in Douala wants to build a second factory. It can borrow, or it can increase its capital. A capital increase brings **new money** "
          "(cash issue), turns **reserves** into capital (bonus issue), or turns a **debt** into capital (conversion). Each method changes the value of an old share, "
          "and the law protects old shareholders with **rights**. The Board's 2023 report notes that few candidates attempted a question on a double increase of "
          "capital, so practise this lesson carefully. All figures are **invented for practice**."),
        D("The **mathematical value** (valeur mathématique, book or intrinsic value) of a share = net assets ÷ number of shares. "
          "Net assets = real value of assets − all liabilities (equal to equity after any revaluation).", title="Mathematical value"),
        EX("Worked example 1: cash issue and the DS",
           intro="Littoral Plastics has 4 000 shares of nominal value 10 000. Assets at real value are 85 000 000 and liabilities 25 000 000. It issues 1 000 new "
                 "shares (1 for 4) at 12 000, fully paid in cash.",
           steps=[
               S("Value before", text="Net assets 85 000 000 − 25 000 000 = 60 000 000; V0 = 60 000 000 ÷ 4 000 = 15 000."),
               S("Value after", text="(60 000 000 + 1 000 × 12 000) ÷ 5 000 = 72 000 000 ÷ 5 000 = 14 400."),
               S("DS", text="V0 − V1 = 15 000 − 14 400 = 600 per old share."),
               S("Check with the formula", text="(V0 − issue price) × n ÷ (N + n) = 3 000 × 1 000 ÷ 5 000 = 600."),
           ]),
        D("The **preferential subscription right (DS, droit préférentiel de souscription)** lets each old shareholder buy new cash shares before outsiders, in proportion "
          "to his holding. Its theoretical value is the fall in the share's value: DS = V0 − V1 = (V0 − E) × n ÷ (N + n), where E is the issue price, N the old shares "
          "and n the new shares.", title="DS"),
        T("**Why the right matters.** A shareholder with 4 shares had 4 × 15 000 = 60 000. If he subscribes 1 new share for 12 000 he holds 5 × 14 400 = 72 000, "
          "exactly 60 000 + 12 000. If he does not subscribe, he sells his 4 rights for 4 × 600 = 2 400: 4 × 14 400 + 2 400 = 60 000. Either way he loses nothing. "
          "A holder of 50 shares can subscribe 12 new shares (using 48 rights) and sell the other 2 rights."),
        CODE(_j10a, "text", title="Journal: cash issue at a premium"),
        EX("Worked example 2: bonus issue and the DA",
           intro="Instead, the company incorporates 10 000 000 of reserves into capital by issuing 1 000 free shares (1 for 4).",
           steps=[
               S("Net assets", text="Unchanged at 60 000 000: reserves simply become capital."),
               S("Value after", text="60 000 000 ÷ 5 000 = 12 000."),
               S("DA", text="15 000 − 12 000 = 3 000 per old share = V0 × n ÷ (N + n) = 15 000 × 1 000 ÷ 5 000."),
           ]),
        D("The **attribution right (DA, droit d'attribution)** gives each old shareholder free shares in proportion to his holding. Its value is DA = V0 − V1 = "
          "V0 × n ÷ (N + n). The company's net assets do not change, only the number of shares.", title="DA"),
        EX("Worked example 3: double increase",
           intro="Littoral Plastics first makes the cash issue of example 1 (1 for 4 at 12 000) and then a bonus issue of 1 for 5 (1 000 shares) from 10 000 000 of reserves. "
                 "The new cash shares also receive bonus shares.",
           steps=[
               S("Value before", text="V0 = 15 000."),
               S("After the cash issue", text="V1 = 14 400; DS = 600."),
               S("After the bonus issue", text="V2 = 72 000 000 ÷ 6 000 = 12 000; DA = 14 400 − 12 000 = 2 400 = 14 400 × 1 ÷ 6."),
               S("Entries", text="Cash issue as in example 1; bonus: debit reserves 10 000 000, credit capital 10 000 000."),
           ]),
        CODE(_t_eq10, "text", title="Equity at each stage (invented for practice)"),
        CODE(_j10b, "text", title="Journal: bonus issue"),
        IMG("alacu1-capital-increase-values.svg",
            alt="Bar chart of value per share: 15 000 before, 14 400 after the cash issue (DS = 600) and 12 000 after the bonus issue (DA = 2 400).",
            caption="Figure 1. Value per share in the double increase."),
        T("If both increases are decided **at the same time**, or if the new cash shares do not take part in the bonus issue, the calculation changes. "
          "Textbooks treat these cases differently: always follow the order and conditions in the question, and check your textbook."),
        KEY("Conversion of debt", "A creditor (for example a bondholder or a supplier) accepts shares instead of repayment.",
            cards=[["Entry", "Debit the debt account; credit capital with the nominal value and a premium account (conversion premium) with any excess."],
                   ["Effect", "No cash moves; liabilities fall and equity rises, so gearing falls."]]),
        MISTAKE("Using nominal value instead of mathematical value",
                "DS and DA depend on the real value of a share (net assets ÷ shares), not on its nominal value."),
        MISTAKE("Forgetting the new shares in the second increase",
                "In a double increase, divide by the total number of shares after each stage, including those just issued (unless the question excludes them)."),
        MISTAKE("Thinking a bonus issue brings new money",
                "Net assets do not change in a bonus issue; only reserves are moved to capital."),
        QUIZ("A company has 3 000 shares with net assets of 48 000 000. It issues 1 000 new shares for cash at 12 000. What is the DS?",
             ["4 000", "1 000", "15 000", "16 000"], 1,
             "V0 = 16 000; V1 = (48 000 000 + 12 000 000) ÷ 4 000 = 15 000; DS = 1 000.",
             hint="Find the value before and after.",
             feedback=["This is V0 − issue price; multiply by n ÷ (N + n).", "", "This is the value after the issue.",
                       "This is the value before the issue."]),
        QUIZ("In a bonus issue (incorporation of reserves), what happens to the company's net assets?",
             ["They increase by the amount of reserves incorporated", "They decrease by the amount of reserves incorporated",
              "They do not change", "They increase by the nominal value of the new shares"], 2,
             "Reserves become capital: both are equity, so total equity and net assets are unchanged.",
             hint="Does any money come in or go out?",
             feedback=["No new money comes in.", "Nothing leaves the company.", "", "The nominal value moves from reserves to capital inside equity."],
             title="Quick check 2"),
        TIP("Capital increases appear in Section B of Paper 3 and in Paper 1. Write V0, V1 (and V2) with their workings before calculating DS and DA, then the journal.",
            title="Exam link"),
        PQ("A company with 3 000 shares and net assets 48 000 000 makes a bonus issue of 1 for 3. Find the value after and the DA.",
           "Value after = 48 000 000 ÷ 4 000 = 12 000. DA = 16 000 − 12 000 = 4 000 (= 16 000 × 1 ÷ 4)."),
        PQ("A supplier owed 10 000 000 accepts 800 shares of nominal value 10 000 in full settlement. Record the conversion.",
           "Debit the supplier (payables) 10 000 000; credit capital 8 000 000 and conversion premium 2 000 000 (800 × 2 500)."),
        PQ("Explain why the law gives old shareholders a preferential subscription right.",
           "New shares are issued below the value of old shares, so the value per share falls. The right lets old shareholders keep their share of the company "
           "or sell the right to recover the loss in value; it also protects their voting power from dilution."),
        PQ("Compare a cash issue with a bonus issue for the company and for a shareholder.",
           "Cash issue: new money for investment; old shareholders must pay or sell their DS. Bonus issue: no new money; it adjusts capital to the real size of the "
           "company, makes shares cheaper per unit and may signal confidence; shareholders receive DA and their wealth is unchanged."),
        SUM("Mathematical value = net assets ÷ number of shares.",
            "Cash issue: V1 = (net assets + n × E) ÷ (N + n); DS = V0 − V1 = (V0 − E) × n ÷ (N + n).",
            "Bonus issue: net assets unchanged; DA = V0 − V1 = V0 × n ÷ (N + n).",
            "Double increase: compute values stage by stage in the order given.",
            "Conversion of debt: debit the debt, credit capital and premium; no cash moves."),
    ]))

# ====================================================================== 11. Reduction and amortization of capital
_cap11, _sh11, _loss11 = 30_000_000, 3_000, 18_000_000
_eq11 = _cap11 - _loss11
assert _eq11 == 12_000_000 and _eq11 < _cap11 // 2
_newnom11 = (_cap11 - _loss11) // _sh11
assert _newnom11 == 4_000 and _sh11 * 2 // 5 * 10_000 == _eq11
_j11a = journal([("Reduction of capital to absorb losses", [("1013 Capital called and paid", _loss11)], [("129 Losses brought forward", _loss11)])])
# repayment of excess capital
_j11b = journal([
    ("Reduction by repayment: 2 000 per share on 5 000 shares", [("1013 Capital called and paid", 10_000_000)], [("4619 Shareholders, to repay", 10_000_000)]),
    ("Repayment", [("4619 Shareholders, to repay", 10_000_000)], [("521 Bank", 10_000_000)]),
])
assert 5_000 * 2_000 == 10_000_000 and (50_000_000 - 10_000_000) // 5_000 == 8_000
# amortization 25% of nominal on 4 000 shares from reserves
_am11 = 4_000 * 2_500
assert _am11 == 10_000_000
_j11c = journal([
    ("Amortization voted: 2 500 per share from reserves", [("118 Other reserves", _am11)], [("4619 Shareholders, to repay", _am11)]),
    ("Payment to shareholders", [("4619 Shareholders, to repay", _am11)], [("521 Bank", _am11)]),
    ("Capital status changes (total capital unchanged)", [("1013 Capital called and paid", _am11)], [("1014 Capital paid, amortized", _am11)]),
])
# dividends with jouissance shares: 1 000 shares fully amortized, 3 000 capital shares, distributable 9 000 000, first dividend 6%
_fd11 = 3_000 * 10_000 * 6 // 100
_sd11 = Fr(9_000_000 - _fd11, 4_000)
assert _fd11 == 1_800_000 and _sd11 == 1_800 and 3_000 * (600 + 1_800) + 1_000 * 1_800 == 9_000_000
_t_div11 = "\n".join([
    "Dividends after amortization (distributable 9 000 000)",
    r("First dividend 6% on 3 000 capital shares", 1_800_000, w=42),
    r("Super dividend 1 800 on 4 000 shares", 7_200_000, w=42),
    r("Total", 9_000_000, w=42),
    "",
    "Per capital share:   600 + 1 800 = 2 400",
    "Per jouissance share:       1 800",
])
# partly amortized all shares: first dividend on 7 500
assert 7_500 * 6 // 100 == 450
# practice question figures
assert (40_000_000 - 12_000_000) // 4_000 == 7_000 and 28_000_000 // 10_000 == 2_800 == 4_000 * 7 // 10

LESSONS.append(lesson(
    module=M_MOD, topic="Reduction and amortization of capital",
    title="Reduction of capital and amortization of capital",
    slug="acu1-reduction-amortization-capital", minutes=24,
    summary="Reduce capital to absorb losses or to repay surplus capital, and amortize capital by repaying the nominal value of shares out of reserves; "
            "record the entries and see the effect on later dividends (jouissance shares).",
    objectives=[
        "Explain why a company reduces its capital and the creditor-protection rule when losses are large",
        "Record a reduction to absorb losses, by lowering nominal value or the number of shares",
        "Record a reduction by repayment of surplus capital",
        "Record an amortization of capital and calculate dividends on capital shares and jouissance shares",
    ],
    key_concepts=["Reduction of capital", "Losses brought forward", "Nominal value", "Repayment of capital",
                  "Amortization of capital", "Jouissance share (action de jouissance)", "Capital share"],
    blocks=[
        H("Making capital smaller"),
        T("After several bad years, a timber company in Bertoua has a large debit balance of losses brought forward. Its balance sheet shows capital of 30 000 000, "
          "but its real equity is only 12 000 000. It cannot pay dividends until the losses are cleared. One solution is to **reduce the capital** so that it matches "
          "reality. Other companies have more capital than they need and **repay** part of it, or **amortize** it. All figures are **invented for practice**."),
        D("A **reduction of capital** lowers the share capital in the statutes, by reducing the nominal value of each share or the number of shares. "
          "It is decided by an **extraordinary general meeting** because it changes the statutes. When it is not caused by losses, creditors may object "
          "and ask for guarantees.", title="Reduction of capital"),
        D("Under the OHADA Uniform Act, if losses make an SA's equity fall **below half of its share capital**, the shareholders must decide whether to dissolve the "
          "company; if they do not, it must, within a set period, reduce its capital by the losses or restore its equity. Check your textbook for the exact time limits.",
          title="When losses are large"),
        EX("Worked example 1: reduction to absorb losses",
           intro="Capital 30 000 000 in 3 000 shares of 10 000; losses brought forward 18 000 000; no reserves. The meeting reduces capital by the amount of the losses.",
           steps=[
               S("Equity", text="30 000 000 − 18 000 000 = 12 000 000, less than half the capital (15 000 000)."),
               S("Method A: lower nominal value", text="12 000 000 ÷ 3 000 = 4 000 per share."),
               S("Method B: fewer shares", text="Keep 10 000 per share and exchange 5 old shares for 2 new: 3 000 × 2/5 = 1 200 shares, capital 12 000 000."),
               S("Entry", text="Debit capital 18 000 000; credit losses brought forward (129) 18 000 000. No cash moves."),
           ]),
        CODE(_j11a, "text", title="Journal: reduction for losses (invented for practice)"),
        T("A capital cannot be reduced below the legal minimum (FCFA 10 000 000 for an SA) unless it is increased again straight afterwards to at least the minimum. "
          "Reducing and then increasing at once is called a **coup d'accordéon**."),
        EX("Worked example 2: repayment of surplus capital",
           intro="A company has capital 50 000 000 in 5 000 shares and more cash than it needs. It repays 2 000 per share.",
           steps=[
               S("Amount", text="5 000 × 2 000 = 10 000 000; new nominal value 8 000."),
               S("Entries", text="Debit capital, credit shareholders' capital to repay (4619); then pay by bank."),
               S("Effect", text="Cash and capital both fall: creditors lose part of their protection, which is why they may object."),
           ]),
        CODE(_j11b, "text", title="Journal: repayment"),
        H("Amortization of capital"),
        D("**Amortization of capital** is the repayment to shareholders of all or part of the nominal value of their shares **out of profits or reserves**. "
          "The capital in the statutes does **not** change: account 1013 is transferred to 1014 (capital amortized). A fully repaid share becomes a "
          "**jouissance share** (action de jouissance): it keeps its vote and its right to super dividends and to the liquidation surplus, but it loses the "
          "first dividend and the repayment of its nominal value on liquidation.", title="Amortization"),
        EX("Worked example 3: amortization and later dividends",
           intro="(a) A company with 4 000 shares of 10 000 amortizes 2 500 per share out of reserves. (b) Another company with 4 000 shares of 10 000 has fully "
                 "amortized 1 000 shares chosen by lot (they are jouissance shares); the other 3 000 are not amortized. It has 9 000 000 to distribute; its statutes "
                 "give a first dividend of 6% of non-amortized capital and the rest equally to every share.",
           steps=[
               S("(a) Amortization of 2 500", text="4 000 × 2 500 = 10 000 000 debited to reserves and paid; 1013 → 1014 for 10 000 000."),
               S("(a) Later first dividend", text="6% × 7 500 = 450 per share instead of 600."),
               S("(b) First dividend", text="First dividend only on 3 000 capital shares: 3 000 × 600 = 1 800 000."),
               S("(b) Super dividend", text="(9 000 000 − 1 800 000) ÷ 4 000 = 1 800 on every share."),
           ]),
        CODE(_j11c, "text", title="Journal: amortization of 2 500 per share"),
        CODE(_t_div11, "text", title="Dividend table for company (b)"),
        MISTAKE("Thinking amortization reduces the capital",
                "Capital stays the same in total; only its status changes (1013 → 1014). In a reduction, capital itself falls."),
        MISTAKE("Paying out cash in a reduction for losses",
                "A reduction to absorb losses is a book entry only: debit capital, credit losses. No money leaves the company."),
        MISTAKE("Giving jouissance shares the first dividend",
                "The first dividend is interest on capital not yet repaid; a fully amortized share does not receive it."),
        QUIZ("A company with capital 40 000 000 (4 000 shares) absorbs losses of 12 000 000 by reducing nominal value. What is the new nominal value?",
             ["7 000", "3 000", "10 000", "8 000"], 0,
             "(40 000 000 − 12 000 000) ÷ 4 000 = 7 000.",
             hint="Capital after reduction divided by the number of shares.",
             feedback=["", "This is the reduction per share, not the new nominal value.", "This is the old nominal value.",
                       "This subtracts 2 000 per share instead of 3 000."]),
        QUIZ("Which statement about amortization of capital is correct?",
             ["It reduces the share capital in the statutes", "It is paid out of profits or reserves and leaves total capital unchanged",
              "It is used to absorb losses", "It cancels the voting rights of the shares"], 1,
             "Shareholders receive their nominal value early from profits or reserves; 1013 becomes 1014 but the total capital stays the same.",
             hint="Where does the money come from, and what happens to account 101?",
             feedback=["That is a reduction of capital.", "", "Absorbing losses is a reduction, not an amortization.",
                       "Jouissance shares keep their vote."], title="Quick check 2"),
        TIP("Reductions and amortizations of capital appear in Paper 1 and with other capital changes in Section B of Paper 3. Always say whether cash moves "
            "and whether the capital in the statutes changes.", title="Exam link"),
        PQ("Capital 40 000 000 (4 000 shares of 10 000); losses brought forward 12 000 000. Give the new nominal value if losses are absorbed by reducing nominal value.",
           "40 000 000 − 12 000 000 = 28 000 000; ÷ 4 000 = 7 000 per share. Entry: debit capital 12 000 000, credit 129 12 000 000."),
        PQ("In the same company, how many shares of 10 000 would remain if the number of shares were reduced instead, and in what exchange ratio?",
           "28 000 000 ÷ 10 000 = 2 800 shares: 10 old shares for 7 new (4 000 × 7/10 = 2 800)."),
        PQ("Why may creditors object to a reduction of capital by repayment, but not to a reduction to absorb losses?",
           "Repayment sends cash to shareholders and lowers the capital that guarantees creditors. Absorbing losses only recognises a loss that has already happened: "
           "no asset leaves the company, so creditors are no worse off."),
        PQ("Explain the difference between a capital share and a jouissance share.",
           "A capital share has not been repaid: it receives the first dividend and its nominal value on liquidation. A jouissance share has been fully amortized: "
           "it keeps its vote, super dividend and share of any liquidation surplus, but receives no first dividend and no repayment of nominal value."),
        SUM("Reduction for losses: debit capital, credit 129; lower the nominal value or the number of shares; no cash moves.",
            "If equity falls below half the capital, shareholders must decide on dissolution or reduce capital (check the time limits).",
            "Reduction by repayment: debit capital, credit 4619, then pay; creditors may object.",
            "Amortization: repay nominal value from reserves; capital stays the same, 1013 → 1014.",
            "Jouissance shares get no first dividend but share in super dividends."),
    ]))

# ====================================================================== 12. Company tax
_acc12, _add12, _ded12 = 18_000_000, [("Fines and penalties", 400_000), ("Personal expenses of the owner", 250_000), ("Depreciation above the allowed rate", 650_000)], [("Dividends received (exempt, teaching case)", 300_000)]
_fisc12 = _acc12 + sum(a for _, a in _add12) - sum(a for _, a in _ded12)
assert _fisc12 == 19_000_000
_t12 = _fisc12 * 30 // 100
_cac12 = _t12 // 10
_tot12 = _t12 + _cac12
_ca12 = 250_000_000
_min12 = _ca12 * 22 // 1000
assert (_t12, _cac12, _tot12, _min12) == (5_700_000, 570_000, 6_270_000, 5_500_000) and _ca12 * 22 % 1000 == 0
_due12 = max(_tot12, _min12)
assert _due12 == 6_270_000
_t_fisc12 = "\n".join([
    "Fiscal analysis (teaching rates: check the Finance Law)",
    r("Accounting profit before tax", None, _acc12, w=44),
    "Add back (not deductible):",
    *[r(f"  {l}", a, w=44) for l, a in _add12],
    r("", None, sum(a for _, a in _add12), w=44),
    "Deduct (exempt or taxed elsewhere):",
    *[r(f"  {l}", a, w=44) for l, a in _ded12],
    r("Fiscal (taxable) profit", None, _fisc12, w=44),
    r("Company tax 30%", None, _t12, w=44),
    r("Additional council tax 10% of the tax", None, _cac12, w=44),
    r("Tax from the profit basis", None, _tot12, w=44),
    r("Minimum tax 2.2% x 250 000 000", None, _min12, w=44),
    r("Tax due (the higher)", None, _due12, w=44),
])
_net12 = _acc12 - _due12
assert _net12 == 11_730_000
_j12 = journal([
    ("Income tax of the year", [("891 Income tax", _due12)], [("441 State, income tax", _due12)]),
    ("Payment of the tax", [("441 State, income tax", _due12)], [("521 Bank", _due12)]),
])
# example 2: loss carried forward; minimum tax wins
_fis2, _loss2, _ca2 = 8_000_000, 3_000_000, 120_000_000
_base2 = _fis2 - _loss2
_tax2 = _base2 * 30 // 100 * 11 // 10
_min2 = _ca2 * 22 // 1000
assert (_base2, _tax2, _min2) == (5_000_000, 1_650_000, 2_640_000) and max(_tax2, _min2) == _min2
# example 3: accounting loss but fiscal profit
_acc3 = -1_000_000
_fis3 = _acc3 + 1_500_000 + 700_000
assert _fis3 == 1_200_000 and _fis3 * 30 // 100 * 11 // 10 == 396_000
_min3 = 90_000_000 * 22 // 1000
assert _min3 == 1_980_000
# practice figures
assert 4_000_000 * 3 // 10 == 1_200_000 and 20_000_000 + 600_000 - 200_000 == 20_400_000

LESSONS.append(lesson(
    module=M_MOD, topic="Company tax",
    title="Company tax: fiscal analysis, taxable profit and the minimum tax",
    slug="acu1-company-tax", minutes=24,
    summary="Move from the accounting profit to the taxable (fiscal) profit by adding back non-deductible expenses and deducting exempt income, "
            "apply the company tax rate, compare with the minimum tax on turnover, and record the tax. Rates are teaching values.",
    objectives=[
        "Explain why the accounting profit and the fiscal profit differ",
        "Carry out a fiscal analysis: add back non-deductible expenses and deduct exempt income and losses carried forward",
        "Calculate company tax and compare it with the minimum tax on turnover",
        "Record the income tax and calculate the profit after tax",
    ],
    key_concepts=["Accounting profit", "Fiscal (taxable) profit", "Reintegration", "Deduction", "Company tax",
                  "Minimum tax", "Loss carried forward", "Additional council tax"],
    blocks=[
        H("Two profits, one business"),
        T("The accountant of a bakery in Yaounde finds a profit of 18 000 000 in the income statement. The tax inspector finds a different number. Both can be right: "
          "accounting follows the accounting rules, while tax follows the **tax code**, which refuses to accept some expenses and exempts some income. "
          "The **fiscal analysis** passes from one to the other. Candidates in the Board's 2023 report found this topic hard (very few attempted it), "
          "so a clear method is worth marks. All figures are **invented for practice**."),
        D("**Company tax** (impôt sur les sociétés) is a tax on the **fiscal profit** of companies. The General Tax Code and the annual Finance Law set the rates and "
          "rules. This lesson uses **teaching values**: a rate of **30%**, an **additional council tax of 10% of the tax**, and a **minimum tax of 2.2% of turnover**. "
          "**Check the current Finance Law and your textbook** because rates and thresholds change, and some taxpayers have different rates.", title="Company tax (teaching values)"),
        KEY("From accounting profit to fiscal profit", "Four steps, always in this order.",
            cards=[["1. Start", "Accounting profit (or loss) before tax."],
                   ["2. Add back", "Expenses recorded but not deductible: fines, personal expenses of owners, depreciation above the allowed rate, gifts above limits."],
                   ["3. Deduct", "Income that is exempt or taxed elsewhere, and (where allowed) losses brought forward."],
                   ["4. Result", "Fiscal profit, the base for the tax rate."]]),
        EX("Worked example 1: fiscal analysis and tax",
           intro="Accounting profit 18 000 000. Included in expenses: fines 400 000, personal expenses of the owner 250 000, and depreciation 650 000 above the allowed rate. "
                 "Included in income: dividends received of 300 000, treated here as exempt. Turnover is 250 000 000.",
           steps=[
               S("Add back", text="400 000 + 250 000 + 650 000 = 1 300 000."),
               S("Deduct", text="300 000 of exempt dividends."),
               S("Fiscal profit", text="18 000 000 + 1 300 000 − 300 000 = 19 000 000."),
               S("Tax", text="30% × 19 000 000 = 5 700 000; additional council tax 10% × 5 700 000 = 570 000; total 6 270 000."),
               S("Minimum tax", text="2.2% × 250 000 000 = 5 500 000, lower than 6 270 000, so the tax due is **6 270 000**."),
           ]),
        CODE(_t_fisc12, "text", title="Fiscal analysis (invented for practice)"),
        CODE(_j12, "text", title="Journal: tax of the year"),
        T("The profit **after tax** is 18 000 000 − 6 270 000 = **11 730 000**. This is the net profit that the general meeting appropriates (previous lessons). "
          "Account numbers (89 and 441) are the usual textbook ones: check your textbook."),
        H("The minimum tax"),
        D("The **minimum tax** (minimum de perception) is a tax on **turnover** that a company pays even when it makes a loss or a small profit. "
          "The company pays the **higher** of the tax calculated on its profit and the minimum tax (teaching convention: compare the two amounts "
          "after additional council tax). Why? A tax on turnover is hard to avoid, which protects State revenue.", title="Minimum tax"),
        EX("Worked example 2: loss brought forward, minimum tax applies",
           intro="Fiscal profit before losses is 8 000 000; a tax loss of 3 000 000 from an earlier year may be carried forward (check the number of years allowed). "
                 "Turnover is 120 000 000.",
           steps=[
               S("Taxable base", text="8 000 000 − 3 000 000 = 5 000 000."),
               S("Tax", text="30% × 5 000 000 = 1 500 000, plus 10% = 1 650 000."),
               S("Minimum tax", text="2.2% × 120 000 000 = 2 640 000."),
               S("Due", text="The higher figure: 2 640 000."),
           ]),
        EX("Worked example 3: accounting loss but fiscal profit",
           intro="Accounting result −1 000 000. Fines 1 500 000 and other non-deductible items 700 000 are included in expenses. Turnover 90 000 000.",
           steps=[
               S("Fiscal profit", text="−1 000 000 + 1 500 000 + 700 000 = 1 200 000."),
               S("Tax on profit", text="30% × 1 200 000 = 360 000; with 10%, 396 000."),
               S("Minimum tax", text="2.2% × 90 000 000 = 1 980 000, which is higher and is due."),
           ]),
        T("**Evaluation.** The minimum tax can be unfair to a firm in a poor year: it pays tax with no profit. Its supporters say that firms must contribute fairly "
          "and that it discourages under-declaring profits. Many systems let the minimum tax paid be set against tax due in later years: check the current rules."),
        MISTAKE("Adding back items that are already deductible",
                "Only expenses the tax code refuses are added back. Check each item: ordinary wages, rent and interest within limits are deductible."),
        MISTAKE("Subtracting the tax from the accounting profit before the fiscal analysis",
                "Start from the profit BEFORE tax. The tax is the result of the analysis, not an input."),
        MISTAKE("Forgetting to compare with the minimum tax",
                "Always compute both amounts and take the higher."),
        QUIZ("Accounting profit 10 000 000; non-deductible expenses 2 000 000; exempt income 500 000. What is the fiscal profit?",
             ["11 500 000", "12 500 000", "7 500 000", "8 500 000"], 0,
             "10 000 000 + 2 000 000 − 500 000 = 11 500 000.",
             hint="Add back expenses refused; deduct exempt income.",
             feedback=["", "This adds the exempt income instead of deducting it.", "This subtracts the non-deductible expenses.",
                       "This subtracts both items."]),
        QUIZ("A company makes an accounting loss and has a turnover of 50 000 000. Which statement is correct (teaching rules)?",
             ["It pays no tax because it has no profit", "It pays at least the minimum tax on its turnover",
              "It pays tax on its loss at 30%", "It pays the additional council tax only"], 1,
             "The minimum tax is based on turnover, so it is due even without profit.",
             hint="What is the base of the minimum tax?",
             feedback=["Turnover-based minimum tax applies even in a loss year.", "", "A loss gives no tax on profit.",
                       "The additional council tax depends on the tax computed."], title="Quick check 2"),
        TIP("Company tax appears among company accounting and taxation questions (Paper 1 multiple choice and Section B of Paper 3). In 2023 the Board's report asked "
            "candidates to analyse expenses and revenue to find the taxable profit. State the rates you use and mention that rates come from the current law.",
            title="Exam link"),
        PQ("Accounting profit 20 000 000; fines 600 000 are not deductible; exempt income 200 000. Find the fiscal profit.",
           "20 000 000 + 600 000 − 200 000 = 20 400 000."),
        PQ("Fiscal profit 4 000 000, teaching rate 30%, no other taxes. Turnover 30 000 000 and minimum tax 2.2%. Which tax is due?",
           "Profit tax 1 200 000; minimum tax 660 000; the higher, 1 200 000, is due (before any additional council tax)."),
        PQ("Why must the accountant keep accounting profit and fiscal profit separate?",
           "The accounts must follow accounting rules (true and fair view) while tax follows the tax code. Mixing them would distort the financial statements "
           "or understate tax. The fiscal analysis is a bridge between the two."),
        PQ("Discuss one advantage and one disadvantage of the minimum tax for a young business.",
           "Advantage: simple and predictable, and it deters false losses. Disadvantage: a young firm often has low profit in its first years, but still pays tax on turnover, "
           "which weakens its cash. Evaluation: some systems exempt new firms for a period or allow the minimum tax to be credited later: check the Finance Law."),
        SUM("Fiscal profit = accounting profit + non-deductible expenses − exempt income (and losses brought forward where allowed).",
            "Teaching values: 30% company tax, 10% additional council tax on it, 2.2% minimum tax on turnover. Check the Finance Law.",
            "Pay the higher of the tax on profit and the minimum tax.",
            "Entry: debit 891 income tax, credit 441 State income tax; profit after tax = accounting profit − tax.",
            "Keep accounting and fiscal profit separate."),
    ]))

# ====================================================================== 13. Mergers
_A_na, _A_n = 90_000_000, 6_000
_B_assets, _B_liab, _B_n = 50_000_000, 17_000_000, 3_000
_B_na = _B_assets - _B_liab
_VA, _VB = Fr(_A_na, _A_n), Fr(_B_na, _B_n)
assert (_B_na, _VA, _VB) == (33_000_000, 15_000, 11_000)
_ratio13 = _VB / _VA
assert _ratio13 == Fr(11, 15)
_newA = Fr(_B_n * 11, 15)
assert _newA == 2_200
_nomcap13 = 2_200 * 10_000
_prem13 = _B_na - _nomcap13
assert (_nomcap13, _prem13) == (22_000_000, 11_000_000)
assert Fr(_A_na + _B_na, _A_n + 2_200) == 15_000
_j13 = journal([
    ("Merger by absorption of B (entries in A)",
     [("Assets taken over from B", _B_assets)],
     [("Liabilities taken over from B", _B_liab), ("1013 Capital called and paid", _nomcap13), ("1054 Merger premium", _prem13)]),
])
# example 2: with a cash balance (soulte)
_B2_na = 32_000_000
_sh2 = 2_000
_nom2 = _sh2 * 10_000
_soulte = 2_000_000
_prem2 = _B2_na - _nom2 - _soulte
assert (_nom2, _prem2) == (20_000_000, 10_000_000) and _soulte <= _nom2 // 10 and _sh2 * 15_000 == _nom2 + _prem2
_j13b = journal([
    ("Merger with a cash balance (soulte) paid by A",
     [("Assets taken over", 50_000_000)],
     [("Liabilities taken over", 50_000_000 - _B2_na), ("1013 Capital called and paid", _nom2), ("1054 Merger premium", _prem2), ("521 Bank (soulte)", _soulte)]),
])
# example 3: a shareholder
assert 150 * 11 // 15 == 110 and 150 * 11 % 15 == 0 and 110 * 15_000 == 150 * 11_000
assert 40 * 11 // 15 == 29 and 40 * 11 % 15 == 5
# practice figures
assert Fr(36_000_000, 3_000) == 12_000 and Fr(12_000, 16_000) == Fr(3, 4) and 2_400 * 3 // 4 == 1_800
assert 3_000 * 3 // 4 == 2_250 and 2_250 * 10_000 == 22_500_000 and 36_000_000 - 22_500_000 == 13_500_000 and Fr(5, 8) != Fr(2, 5)

LESSONS.append(lesson(
    module=M_MOD, topic="Mergers",
    title="Mergers: absorption, exchange ratio and merger premium",
    slug="acu1-mergers", minutes=24,
    summary="In a merger by absorption one company takes over another's assets and liabilities in exchange for new shares. Value both companies, find the "
            "exchange ratio, the new shares, the merger premium and the entries.",
    objectives=[
        "Distinguish a merger by absorption from a merger by creating a new company, and explain why companies merge",
        "Value both companies by net assets and find the exchange ratio",
        "Calculate the shares issued, the capital increase and the merger premium",
        "Record the merger in the absorbing company, including a cash balance (soulte)",
    ],
    key_concepts=["Merger", "Absorbing company", "Absorbed company", "Exchange ratio", "Merger premium", "Cash balance (soulte)", "Net assets"],
    blocks=[
        H("Two companies become one"),
        T("Two cement-products companies in Douala compete for the same customers. Their owners agree that one company, **A**, will take over the other, **B**. "
          "B disappears without a formal liquidation: its assets and liabilities pass to A, and B's shareholders receive shares of A. "
          "This is a **merger by absorption** (fusion-absorption). In a **merger by creation** both companies are dissolved and a new company is formed. "
          "Under OHADA law mergers follow a procedure with a merger plan and approval by the extraordinary general meetings; check your textbook for the steps. "
          "All figures are **invented for practice**."),
        D("A **merger** is an operation in which one or more companies transfer all their assets and liabilities to another company, in return for shares of that company "
          "given to their shareholders. The **absorbed company** is dissolved; the **absorbing company** increases its capital.", title="Merger"),
        KEY("Why merge?", "Reasons commonly given in textbooks.",
            cards=[["Size", "Economies of scale: lower unit costs and more bargaining power."],
                   ["Market", "Fewer competitors and a bigger share of the market."],
                   ["Risk", "Spreading risk across more products or areas."],
                   ["Limits", "Culture clashes, job losses and integration costs often reduce the gains."]]),
        IMG("alacu1-merger-absorption.svg",
            alt="Company B's net assets move to company A; A issues new shares to B's shareholders at the exchange ratio; B is dissolved.",
            caption="Figure 1. Merger by absorption."),
        KEY("Method", "Four steps for the calculation.",
            cards=[["1. Value", "Value of a share of each company, usually net assets ÷ number of shares."],
                   ["2. Ratio", "Exchange ratio = value of a B share ÷ value of an A share."],
                   ["3. New shares", "Shares issued by A = B shares × exchange ratio."],
                   ["4. Premium", "Merger premium = net assets received − nominal value of the new shares (− any cash balance)."]]),
        EX("Worked example 1: exchange ratio and merger premium",
           intro="A has net assets 90 000 000 and 6 000 shares of 10 000. B has assets 50 000 000, liabilities 17 000 000 and 3 000 shares of 10 000. A absorbs B.",
           steps=[
               S("Values", text="A: 90 000 000 ÷ 6 000 = 15 000. B: (50 000 000 − 17 000 000) ÷ 3 000 = 33 000 000 ÷ 3 000 = 11 000."),
               S("Exchange ratio", text="11 000 ÷ 15 000 = 11/15: 15 B shares exchange for 11 A shares."),
               S("New A shares", text="3 000 × 11/15 = 2 200 shares; capital increase 2 200 × 10 000 = 22 000 000."),
               S("Merger premium", text="33 000 000 − 22 000 000 = 11 000 000."),
               S("Check", text="A's value after: (90 000 000 + 33 000 000) ÷ 8 200 = 15 000, unchanged, so nobody gains or loses."),
           ]),
        CODE(_j13, "text", title="Journal in A (invented for practice)"),
        EX("Worked example 2: a cash balance (soulte)",
           intro="Another merger: B's net assets are 32 000 000 (assets 50 000 000, liabilities 18 000 000). A issues 2 000 shares of 10 000 (value 15 000 each) and pays "
                 "2 000 000 in cash to B's shareholders to round off the exchange.",
           steps=[
               S("Nominal value issued", text="2 000 × 10 000 = 20 000 000."),
               S("Premium", text="32 000 000 − 20 000 000 − 2 000 000 = 10 000 000."),
               S("Check on the value", text="2 000 × 15 000 = 30 000 000 = 20 000 000 + 10 000 000, and 30 000 000 + 2 000 000 cash = 32 000 000."),
               S("Limit", text="The Uniform Act limits the cash balance to a fraction of the nominal value of the shares issued (textbooks say 10%): check your textbook."),
           ]),
        CODE(_j13b, "text", title="Journal in A: merger with a cash balance"),
        EX("Worked example 3: what a shareholder receives",
           intro="Using example 1, a shareholder holds 150 B shares and another holds 40.",
           steps=[
               S("150 B shares", text="150 × 11/15 = 110 A shares (value 110 × 15 000 = 1 650 000 = 150 × 11 000)."),
               S("40 B shares", text="40 × 11/15 = 29.33: he receives 29 A shares and a cash balance or buys/sells rights for the 5 remaining B shares (fraction of a share)."),
           ]),
        T("**Evaluation.** The exchange ratio depends on how the companies are valued. Net assets ignore goodwill and future profits, so a profitable company with few "
          "assets may feel under-valued. In practice, valuations use several methods (net assets, profits, market value). Check your textbook for the methods your class uses."),
        MISTAKE("Using nominal values for the exchange ratio",
                "Nominal values are the same here (10 000), but the real values differ. The ratio compares real (mathematical) values."),
        MISTAKE("Treating the merger premium as profit",
                "The merger premium is part of equity (a premium, like a share premium), not income."),
        MISTAKE("Forgetting B's liabilities",
                "Only net assets (assets − liabilities) are worth shares. The absorbing company takes over the debts too."),
        QUIZ("A share of A is worth 20 000 and a share of B is worth 8 000. What is the exchange ratio, in A shares for B shares?",
             ["2 A shares for 5 B shares", "5 A shares for 2 B shares", "1 for 1", "5 A shares for 8 B shares"], 0,
             "8 000 ÷ 20 000 = 2/5: 2 A shares for 5 B shares.",
             hint="Divide the value of a B share by the value of an A share.",
             feedback=["", "This inverts the ratio.", "The values differ, so the ratio is not 1.",
                       "This divides the wrong way round and mixes up the values."]),
        QUIZ("What happens to the absorbed company in a merger by absorption?",
             ["It becomes a subsidiary of the absorbing company", "It is dissolved without a separate liquidation, and its assets and liabilities pass to the absorbing company",
              "It keeps its assets but changes its name", "It is liquidated and its cash is paid to creditors only"], 1,
             "Transfer of everything to A, with B's shareholders receiving A shares.",
             hint="Where do B's assets and debts go?",
             feedback=["A subsidiary survives as a company; here B disappears.", "", "B no longer exists as a company.",
                       "Shareholders receive shares of A; there is no separate liquidation."], title="Quick check 2"),
        TIP("Mergers appear among the company topics in Paper 1 multiple choice and in Section B of Paper 3. Show the value per share of each company, the exchange ratio "
            "and the premium calculation before the journal entry.", title="Exam link"),
        PQ("A has 4 000 shares worth 16 000 each. B has net assets 36 000 000 and 3 000 shares. Find the exchange ratio.",
           "B's share: 36 000 000 ÷ 3 000 = 12 000. Ratio 12 000 ÷ 16 000 = 3/4: 3 A shares for 4 B shares."),
        PQ("Using the data above, find the number of new A shares (nominal 10 000), the capital increase and the merger premium.",
           "New shares 3 000 × 3/4 = 2 250. Capital increase 22 500 000; premium 36 000 000 − 22 500 000 = 13 500 000."),
        PQ("Give two reasons why a merger may fail to create value.",
           "1. Different cultures and systems cost time and staff goodwill. 2. The price paid (the exchange ratio) may have over-valued the absorbed company, "
           "so the absorbing company's shareholders lose value. Evaluation: success depends on integration and on a fair valuation."),
        PQ("Explain why liabilities are subtracted before valuing the absorbed company.",
           "Shareholders own only what remains after debts are paid. The absorbing company takes over the debts, so it must pay for assets net of liabilities."),
        SUM("Merger by absorption: B is dissolved and its assets and liabilities pass to A for new A shares.",
            "Value of each share = net assets ÷ shares; exchange ratio = value of a B share ÷ value of an A share.",
            "New shares = B shares × ratio; capital increase = new shares × nominal value.",
            "Merger premium = net assets received − nominal value issued − any cash balance (soulte).",
            "Check: the value of an A share after the merger equals the value before if the exchange is fair."),
    ]))

# ====================================================================== 14. Liquidation
_pref14, _sec14, _ord14 = 8_000_000, 10_000_000, 12_000_000
_liab14 = _pref14 + _sec14 + _ord14
_cost14 = 2_000_000
_cap14, _n14 = 40_000_000, 4_000
assert _liab14 == 30_000_000


def _stmt14(sales):
    out = [r("Proceeds of the assets sold", None, sales, w=40)]
    out.append(r("Less liquidation costs", None, _cost14, w=40))
    avail = sales - _cost14
    out.append(r("Available for creditors", None, avail, w=40))
    out.append(r("Preferential creditors (staff, State)", None, _pref14, w=40))
    out.append(r("Secured creditors", None, _sec14, w=40))
    out.append(r("Ordinary creditors", None, _ord14, w=40))
    left = avail - _liab14
    out.append(r("Left for shareholders", None, left, w=40))
    return "\n".join(out), left


_t_a, _left_a = _stmt14(80_000_000)
assert _left_a == 48_000_000
_boni14 = _left_a - _cap14
assert _boni14 == 8_000_000 and _boni14 // _n14 == 2_000 and _cap14 // _n14 == 10_000
_t_a += "\n" + "\n".join([r("Repayment of capital 4 000 x 10 000", None, _cap14, w=40),
                          r("Liquidation surplus (boni)", None, _boni14, w=40),
                          r("Boni per share", None, _boni14 // _n14, w=40)])
_t_b, _left_b = _stmt14(62_000_000)
assert _left_b == 30_000_000 and _left_b // _n14 == 7_500 and _cap14 - _left_b == 10_000_000
_t_b += "\n" + "\n".join([r("Capital repaid (loss for shareholders)", None, _left_b, w=40),
                          r("Repaid per share", None, _left_b // _n14, w=40),
                          r("Loss of capital per share", None, (_cap14 - _left_b) // _n14, w=40)])
# insolvent case
_sales_c, _ord_c = 25_000_000, 10_000_000
_avail_c = _sales_c - _cost14
_after_c = _avail_c - _pref14 - _sec14
assert _avail_c == 23_000_000 and _after_c == 5_000_000
assert Fr(_after_c, _ord_c) == Fr(1, 2)
_t_c = "\n".join([
    "Insolvent company (invented for practice)",
    r("Proceeds of the assets sold", None, _sales_c, w=40),
    r("Less liquidation costs", None, _cost14, w=40),
    r("Available for creditors", None, _avail_c, w=40),
    r("Preferential creditors paid in full", None, _pref14, w=40),
    r("Secured creditors paid in full", None, _sec14, w=40),
    r("Left for ordinary creditors", None, _after_c, w=40),
    r("Ordinary creditors owed", None, _ord_c, w=40),
    r("Dividend: 50 francs in each 100 owed", None, "50%", w=40),
    r("Shareholders receive", None, 0, w=40),
])
assert 3_000_000 * 50 // 100 == 1_500_000
# practice figures
assert 60_000_000 - 3_000_000 - 35_000_000 == 22_000_000 and 22_000_000 - 20_000_000 == 2_000_000 and 2_000_000 // 2_000 == 1_000
assert Fr(15_000_000, 20_000_000) == Fr(3, 4) and 36_000_000 // 4_000 == 9_000

LESSONS.append(lesson(
    module=M_MOD, topic="Liquidation",
    title="Liquidation of a company: order of payment, liquidation surplus and loss",
    slug="acu1-liquidation", minutes=23,
    summary="When a company is dissolved, a liquidator sells the assets, pays costs and creditors in the legal order, repays shareholders' capital and shares "
            "any surplus; learn the order of payment and the three outcomes: surplus, partial repayment of capital, and insolvency.",
    objectives=[
        "Explain what dissolution and liquidation are and why a company may be liquidated",
        "State the order in which a liquidator uses the cash",
        "Calculate the liquidation surplus (boni) per share and the repayment of capital when assets raise too little",
        "Calculate the dividend to ordinary creditors when a company is insolvent",
    ],
    key_concepts=["Dissolution", "Liquidation", "Liquidator", "Preferential creditor", "Secured creditor",
                  "Ordinary creditor", "Liquidation surplus (boni)", "Insolvency"],
    blocks=[
        H("The end of a company"),
        T("A trading company in Limbe has finished its business and its shareholders vote to close it. Or a company has lost so much money that it cannot continue. "
          "In both cases the company is **dissolved** and a **liquidator** is appointed to turn the assets into cash, pay the debts and share what remains. "
          "The company keeps its legal personality during the liquidation, only for the needs of the liquidation. The Board's 2023 report says that the last "
          "topics of the programme were poorly taught, which is a good reason to learn this lesson well. All figures are **invented for practice**."),
        D("**Dissolution** is the decision or event that ends the life of the company: expiry of its term, completion of its object, a decision of the shareholders, a "
          "court decision, or losses that reduce equity below half of the capital without any remedy. **Liquidation** is the process that follows: the liquidator "
          "collects the assets, pays the debts and shares the surplus. After liquidation the company is **struck off** the register (RCCM).", title="Dissolution and liquidation"),
        IMG("alacu1-liquidation-order.svg",
            alt="Five steps in order: liquidation costs; preferential and secured creditors; ordinary creditors; repayment of shareholders' capital; liquidation surplus shared among shares.",
            caption="Figure 1. Order of use of the cash in a liquidation."),
        KEY("Order of payment", "Textbook order for a liquidation. In a collective insolvency procedure the OHADA law on insolvency has its own detailed ranking: check your textbook.",
            cards=[["1. Costs", "The costs of the liquidation, including the liquidator's fees."],
                   ["2. Preferential and secured creditors", "Staff wages, the State's taxes and secured lenders, in the order set by law."],
                   ["3. Ordinary creditors", "Paid in proportion to what they are owed, if the cash is not enough."],
                   ["4. Shareholders: capital", "Paid-up capital not yet amortized is repaid."],
                   ["5. Shareholders: surplus", "Any further surplus (boni) is shared as the statutes say, usually equally per share."]]),
        EX("Worked example 1: a surplus",
           intro="A company has capital 40 000 000 (4 000 shares of 10 000, fully paid). Its liabilities are: preferential 8 000 000, secured 10 000 000, ordinary 12 000 000. "
                 "The assets are sold for 80 000 000 and liquidation costs are 2 000 000.",
           steps=[
               S("Available", text="80 000 000 − 2 000 000 = 78 000 000."),
               S("Creditors", text="8 000 000 + 10 000 000 + 12 000 000 = 30 000 000, all paid in full."),
               S("Left for shareholders", text="78 000 000 − 30 000 000 = 48 000 000."),
               S("Capital then surplus", text="Capital 40 000 000 (10 000 per share); boni 8 000 000, i.e. 2 000 per share. Each share receives 12 000."),
           ]),
        CODE(_t_a, "text", title="Liquidator's statement, surplus case (invented for practice)"),
        EX("Worked example 2: assets raise too little",
           intro="Same company, but the assets are sold for only 62 000 000.",
           steps=[
               S("Available", text="62 000 000 − 2 000 000 = 60 000 000; creditors 30 000 000 are paid in full."),
               S("Left", text="30 000 000 for shareholders, less than the capital of 40 000 000."),
               S("Per share", text="30 000 000 ÷ 4 000 = 7 500: the shareholders lose 2 500 on each share."),
           ]),
        CODE(_t_b, "text", title="Liquidator's statement, loss case"),
        EX("Worked example 3: an insolvent company",
           intro="Assets are sold for 25 000 000. Liquidation costs 2 000 000. Preferential creditors 8 000 000, secured 10 000 000, ordinary creditors 10 000 000.",
           steps=[
               S("Available", text="25 000 000 − 2 000 000 = 23 000 000."),
               S("Preferential and secured", text="8 000 000 + 10 000 000 = 18 000 000 paid in full; 5 000 000 left."),
               S("Ordinary creditors", text="5 000 000 ÷ 10 000 000 = 50%: each creditor receives 50 francs in each 100 owed. A creditor owed 3 000 000 receives 1 500 000."),
               S("Shareholders", text="Nothing."),
           ]),
        CODE(_t_c, "text", title="Insolvent company"),
        T("**Limited and unlimited liability.** In an SA or SARL, shareholders lose at most what they invested. In an SNC the partners remain personally liable for "
          "unpaid debts, as in the partnership lessons. The figures above assume the liquidator has already sold every asset and collected every debt."),
        T("**Evaluation.** The legal order protects workers and the State first and shareholders last, because shareholders take the risk in return for profit. "
          "Critics say secured lenders such as banks are protected so strongly that ordinary suppliers, often small businesses, rarely recover much. Check your textbook for "
          "the current legal ranking."),
        MISTAKE("Repaying shareholders before the creditors",
                "Shareholders are paid last. If the cash does not cover the creditors, they receive nothing."),
        MISTAKE("Forgetting the liquidation costs",
                "The costs of the liquidator come out of the proceeds before any creditor is paid."),
        MISTAKE("Sharing the surplus before repaying capital",
                "First repay the capital (nominal value paid up, not yet amortized); only what is left is the boni."),
        QUIZ("Who is paid LAST in a liquidation?",
             ["Ordinary creditors", "The liquidator", "Shareholders", "Staff for wages owed"], 2,
             "Shareholders are owners; they receive what is left after all the creditors have been paid.",
             hint="Who takes the biggest risk?",
             feedback=["Ordinary creditors are paid before shareholders.", "The liquidator's costs are paid first.", "",
                       "Wages owed rank among the preferential claims."]),
        QUIZ("After paying costs and creditors, 36 000 000 remains for 4 000 shares of 10 000 fully paid. What does each share receive?",
             ["9 000", "10 000, and the shareholders keep a surplus", "12 000", "10 000 plus 5 000 of boni"], 0,
             "36 000 000 ÷ 4 000 = 9 000, less than the 10 000 paid in, so there is a loss of capital and no boni.",
             hint="Divide what is left by the number of shares.",
             feedback=["", "There is not enough cash to repay the capital in full.", "12 000 would need 48 000 000.",
                       "No boni arises until capital is fully repaid."], title="Quick check 2"),
        TIP("Liquidation is the last topic of the company programme and one that the Board's 2023 report says candidates found hard. "
            "Use the layout of the liquidator's statement: proceeds, costs, creditors in order, then shareholders. Check each total.", title="Exam link"),
        PQ("Assets are sold for 60 000 000. Costs 3 000 000; creditors 35 000 000; capital 20 000 000 (2 000 shares of 10 000). Find the boni per share.",
           "Available 57 000 000; after creditors 22 000 000; capital 20 000 000; boni 2 000 000 ÷ 2 000 = 1 000 per share (each share receives 11 000 in all)."),
        PQ("An insolvent company has 15 000 000 for ordinary creditors who are owed 20 000 000. How much does a creditor owed 4 000 000 receive?",
           "15 000 000 ÷ 20 000 000 = 75%; 75% × 4 000 000 = 3 000 000."),
        PQ("Why are shareholders paid after creditors?",
           "Creditors lent money with a fixed claim and no share of the profit; shareholders accepted risk for the chance of profit. So the law pays the fixed claims first and "
           "leaves the shareholders with whatever remains, which may be nothing."),
        PQ("Distinguish dissolution from liquidation.",
           "Dissolution is the event or decision that ends the company's life. Liquidation is the process after it: collecting assets, paying debts and sharing the surplus, "
           "ending with the company being struck off the register."),
        SUM("Dissolution ends the company; the liquidator then sells assets, pays costs and creditors and shares what is left.",
            "Order: costs, preferential and secured creditors, ordinary creditors, shareholders' capital, then surplus (boni).",
            "If cash is short, ordinary creditors share it in proportion to their claims; shareholders receive nothing.",
            "Boni per share = (cash left − capital repaid) ÷ number of shares.",
            "Keep to the legal order and check your textbook for the ranking within creditors."),
    ]))
