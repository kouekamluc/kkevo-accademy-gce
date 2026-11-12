"""A Level Accounting (0705), Lower Sixth: modules "Revised SYSCOHADA Conceptual Framework",
"Commercial Operations, VAT, Packaging & Foreign Currency" and "Valuation of Assets & Inventory".

All FCFA figures are invented for practice. Every total and balance below is computed and checked by the
asserts in this file. SYSCOHADA account numbers are the main accounts of the revised chart (2017); sub-account
numbers and Cameroon tax and payroll rates are teaching values to check against the current Finance Law and
your textbook. Draft content: a teacher should check it against the Board's syllabus."""

from fractions import Fraction as _Fr

from .dsl import *  # noqa: F403

COURSE = ("accounting", "lower-sixth")

M1 = "Revised SYSCOHADA Conceptual Framework"
M2 = "Commercial Operations, VAT, Packaging & Foreign Currency"
M3 = "Valuation of Assets & Inventory"

VAT_RATE = _Fr(1925, 10000)  # 19.25 %: teaching rate, check the current Finance Law


def n(x):
    """1234567 -> '1 234 567' (integers only, so a rounding slip cannot hide)."""
    assert int(x) == x, x
    x = int(x)
    s = f"{abs(x):,}".replace(",", " ")
    return "-" + s if x < 0 else s


def m(x):
    """Number for LaTeX: 1234567 -> 1\\,234\\,567."""
    return n(x).replace(" ", r"\,")


def vat(net):
    v = VAT_RATE * net
    assert v.denominator == 1, net
    return int(v)


def journal(entries, aw=6, nw=26, cw=11):
    """Aligned journal text. entries = [(heading, [(account, name, debit, credit), ...]), ...].
    Every entry must balance; the caller gets the text."""
    out = [f"{'Acct':<{aw}}{'Account name':<{nw}}{'Debit':>{cw}}{'Credit':>{cw}}"]
    for head, lines in entries:
        d = sum(x[2] for x in lines)
        c = sum(x[3] for x in lines)
        assert d == c, (head, d, c)
        out.append(head)
        for acct, name, dr, cr in lines:
            assert len(name) <= nw - 1, name
            out.append(f"{acct:<{aw}}{name:<{nw}}{(n(dr) if dr else ''):>{cw}}{(n(cr) if cr else ''):>{cw}}".rstrip())
        out.append(f"{'':<{aw}}{'Totals':<{nw}}{n(d):>{cw}}{n(c):>{cw}}")
    return "\n".join(out)


def rows(lines, w=34, a=12):
    """Two-column statement: (label, amount or '' or None for a rule line)."""
    out = []
    for lab, amt in lines:
        if lab is None:
            out.append("-" * (w + a))
        elif amt == "" or amt is None:
            out.append(lab)
        else:
            out.append(f"{lab:<{w}}{n(amt):>{a}}")
    return "\n".join(out)


def grid(head, widths, body, left=1):
    """Aligned table: the first `left` columns left-aligned, others right. Integers are formatted with n()."""
    def cell(v, w, i):
        s = n(v) if isinstance(v, int) else str(v)
        return f"{s:<{w}}" if i < left else f"{s:>{w}}"
    out = ["".join(cell(h, w, i) for i, (h, w) in enumerate(zip(head, widths)))]
    out.append("-" * sum(widths))
    for r in body:
        if r is None:
            out.append("-" * sum(widths))
        else:
            out.append("".join(cell(v, w, i) for i, (v, w) in enumerate(zip(r, widths))).rstrip())
    return "\n".join(out)


LESSONS = []

# ------------------------------------------------------------------ 1. postulates and conventions
_nc_rec, _nc_pay = 2500000, 1800000
assert _nc_rec - _nc_pay == 700000
_pr_debt0, _pr_debt1 = 6000000, 6240000
_pr_loss = _pr_debt1 - _pr_debt0
assert _pr_loss == 240000
_pr_rec0, _pr_rec1 = 3000000, 3150000
assert _pr_rec1 - _pr_rec0 == 150000

LESSONS.append(lesson(
    module=M1,
    topic="Accounting postulates and conventions",
    title="The revised SYSCOHADA conceptual framework: postulates and conventions",
    slug="acl1-postulates-and-conventions",
    minutes=24,
    summary="The revised SYSCOHADA framework sets the aim of the accounts (a true and fair view), the qualities of useful information and the postulates and conventions, such as going concern, prudence, substance over form and non-compensation, that every accountant applies.",
    objectives=[
        "Explain the purpose of the SYSCOHADA conceptual framework and the qualities of useful financial information",
        "State and apply the main postulates and conventions, including substance over form, non-compensation and intangibility of the opening balance sheet",
        "Decide which convention justifies a given accounting treatment",
        "Evaluate conflicts between conventions, for example prudence against the true and fair view",
    ],
    key_concepts=["Conceptual framework", "True and fair view", "Postulate", "Convention", "Going concern", "Prudence", "Substance over form", "Non-compensation", "Intangibility of the opening balance sheet", "Permanence of methods"],
    blocks=[
        H("Introduction"),
        T("A bank in Douala is asked to lend FCFA 50 million to a cocoa exporter in Kumba. The loan officer has never visited the firm. She reads its balance sheet and income statement and trusts them only because she knows that every accountant in the OHADA zone follows the same basic rules. Those rules are the conceptual framework."),
        T("At O Level you met the main accounting concepts. At A Level you must know how the **revised SYSCOHADA** organises them, apply the newer ones (such as substance over form and non-compensation) and judge which one should win when two of them pull in different directions."),
        D("The **revised SYSCOHADA** is the accounting system set out in the OHADA Uniform Act on accounting law and financial reporting (AUDCIF), adopted in 2017 and applied to the individual accounts of entities from the 2018 financial year. Its **conceptual framework** states the purpose of financial statements, the qualities they must have and the postulates and conventions used to prepare them.",
          title="Definition: revised SYSCOHADA and its conceptual framework"),
        D("The financial statements must give a **true and fair view** (image fidele) of the assets, the financial position and the result of the entity. The postulates and conventions are the means; the true and fair view is the aim.",
          title="The objective: true and fair view"),
        KEY("Qualities of useful information", "Information is useful only if it has these qualities.", cards=[
            ["Relevance", "It can change a user's decision, and it arrives in time to do so."],
            ["Reliability", "It is free from material error and bias, and it shows what it claims to show."],
            ["Comparability", "It can be compared from year to year and between entities, which needs consistent methods."],
            ["Understandability", "A reader with reasonable knowledge of business can understand it."],
        ]),
        H("Postulates and conventions"),
        T("A **postulate** is a basic assumption about the environment in which accounts are kept (for example, that the entity will continue to operate). A **convention** is an agreed rule for recording and presenting (for example, recording assets at historical cost). Textbooks differ on which items they call postulates and which conventions, so check your textbook; the meaning of each item is what matters in the examination."),
        KEY("The basic assumptions", "These describe the setting in which the accounts are prepared.", cards=[
            ["Entity", "The entity is separate from its owners. Their private dealings are not the entity's transactions."],
            ["Going concern (continuity of operation)", "The entity is assumed to continue in the foreseeable future, so assets are not valued at forced-sale prices."],
            ["Periodicity (independence of financial years)", "Life is cut into financial years, normally of twelve months. Income and expenses go to the year they belong to, whatever the date of payment."],
            ["Monetary unit", "Transactions are recorded in one currency of account, the FCFA in Cameroon, and the value of money is treated as stable."],
        ]),
        KEY("The recording and presentation rules", "These guide how amounts are measured and shown.", cards=[
            ["Historical cost", "Assets are recorded at their cost when acquired, not at a current guessed value."],
            ["Prudence", "Probable losses and liabilities are recorded as soon as they are known; gains are recorded only when realised."],
            ["Permanence of methods", "The same methods of valuation and presentation are used from year to year; a change must be justified and explained in the notes."],
            ["Materiality (significant importance)", "Only information that could influence a decision needs separate, detailed treatment."],
            ["Substance over form", "Transactions are recorded according to their economic reality, not only their legal form."],
            ["Non-compensation", "Assets and liabilities, and income and expenses, are shown separately and are not set off against each other."],
            ["Intangibility of the opening balance sheet", "The opening balance sheet of a year must be exactly the closing balance sheet of the previous year."],
            ["Transparency", "Information is presented clearly and honestly, without hiding anything significant."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: substance over form", intro="Etoga Transport signs a location-acquisition contract (a lease that ends with the lessee becoming the owner) for a truck worth FCFA 30 000 000. Legally the leasing company owns the truck until the last payment. How should Etoga treat the truck?", steps=[
            S("Look at the economic reality", text="Etoga uses the truck for most of its life, bears its risks and will own it at the end. Economically it has bought the truck on credit."),
            S("Apply the convention", text="**Substance over form**: the revised SYSCOHADA requires the lessee to record the truck as a fixed asset and the amount owed to the lessor as a debt (location-acquisition debts are in class 1, account 17)."),
            S("Effect", text="The truck is depreciated by Etoga, and each payment is split between repayment of the debt and interest. Under the old legal-form view the payments would simply have been rent."),
        ]),
        EX("Worked example 2: non-compensation", intro="Fotso SARL sells goods to Mbah Stores and also buys from it. At the year end Mbah Stores owes Fotso FCFA " + n(_nc_rec) + " and Fotso owes Mbah Stores FCFA " + n(_nc_pay) + ". How are these shown in Fotso's balance sheet?", steps=[
            S("Identify the two items", text="A receivable (customer, class 4, asset) and a payable (supplier, class 4, liability)."),
            S("Apply non-compensation", text="They are shown separately: customers " + n(_nc_rec) + " under assets, suppliers " + n(_nc_pay) + " under liabilities."),
            S("Why not net them", math=m(_nc_rec) + " - " + m(_nc_pay) + " = " + m(_nc_rec - _nc_pay), text="Showing only a net 700 000 would hide the size of both risks: the risk that Mbah does not pay and the debt Fotso must settle. Netting is allowed only where a legal right of set-off exists and both parties intend to settle net; check your textbook for the exact condition."),
        ]),
        EX("Worked example 3: prudence and unrealised differences", intro="At the year end, a debt to a supplier in the United States recorded at FCFA " + n(_pr_debt0) + " would cost FCFA " + n(_pr_debt1) + " at today's exchange rate. A receivable from a customer in Nigeria recorded at FCFA " + n(_pr_rec0) + " is now worth FCFA " + n(_pr_rec1) + ". What does prudence require?", steps=[
            S("Unrealised loss on the debt", math=m(_pr_debt1) + " - " + m(_pr_debt0) + " = " + m(_pr_loss), text="The loss is probable, so a provision of " + n(_pr_loss) + " is charged against this year's result."),
            S("Unrealised gain on the receivable", math=m(_pr_rec1) + " - " + m(_pr_rec0) + r" = 150\,000", text="The gain is not yet realised, so it is **not** taken to the result. It is kept aside in the balance sheet (you meet the method in the lesson on foreign currency)."),
            S("Conclusion", text="Prudence treats gains and losses differently on purpose: losses when probable, gains when realised."),
        ]),
        EX("Worked example 4: intangibility of the opening balance sheet", intro="An accountant finds in March of year N+1 that closing stock at 31 December N was overstated. Can she simply change the opening figure of year N+1?", steps=[
            S("State the rule", text="The opening balance sheet of N+1 must equal the closing balance sheet of N, which has already been approved."),
            S("Correct properly", text="The error is corrected through the accounts of year N+1 (with an explanation in the notes), not by altering the opening balances. You study this in the lesson on correction of errors."),
        ]),
        H("Evaluation: when conventions conflict"),
        T("Conventions sometimes pull in opposite directions, and A Level questions often ask you to discuss this. **Prudence against the true and fair view**: an over-cautious manager who creates excessive provisions builds hidden reserves; profit is understated and the view is no longer fair. Prudence means caution, not deliberate understatement. **Historical cost against relevance**: cost is objective and can be checked against invoices, but after years of rising prices a building bought long ago is shown far below its value, so the balance sheet is less relevant to a lender. **Going concern against prudence**: if a business is about to close, going concern no longer holds and assets must be valued at what they will fetch, even if that is below cost."),
        MISTAKE("Using prudence to justify any understatement", "Prudence allows provisions for probable losses only. Writing down assets or creating provisions with no real risk breaks the true and fair view and the reliability of the accounts."),
        MISTAKE("Setting off a receivable and a payable with the same person", "Non-compensation requires them to be shown separately. Netting is the exception, not the rule."),
        MISTAKE("Naming the convention without applying it", "Examiners want the link: 'by substance over form, the leased truck is recorded as an asset because Etoga controls it', not just 'substance over form'."),
        QUIZ("A trader shows his customer balances and supplier balances as one net figure in the balance sheet. Which convention does this break?",
             ["Permanence of methods", "Non-compensation", "Going concern", "Monetary unit"], 1,
             "Assets and liabilities must be shown separately; setting them off breaks non-compensation.",
             hint="Which rule forbids setting one amount against another?",
             feedback=["Permanence is about keeping the same methods each year.", "", "Going concern is about the entity continuing.", "The monetary unit is about the currency of account."]),
        QUIZ("A company records a truck held under a location-acquisition contract as its own fixed asset although the lessor still legally owns it. This applies",
             ["historical cost", "prudence", "substance over form", "materiality"], 2,
             "Economic reality (control and use of the truck) is preferred to legal form.",
             hint="Is the treatment based on the legal owner or on who really uses and controls the truck?",
             feedback=["Historical cost is about the value used, not about who records the asset.", "Prudence is about anticipating losses.", "", "Materiality is about the size of an item."]),
        PQ("Distinguish between a postulate and a convention, giving one example of each.",
           "A **postulate** is a basic assumption about the setting in which accounts are kept, for example **going concern** (the entity will continue to operate). A **convention** is an agreed rule for recording and presenting, for example **historical cost** (assets recorded at their cost when acquired). Textbooks classify some items differently; the explanation is what earns marks."),
        PQ("Explain, with an example, how prudence may conflict with the true and fair view.",
           "Prudence requires probable losses to be recorded early and gains only when realised. Taken too far, a manager may create provisions for risks that are not probable, for example a large provision for a lawsuit nobody has filed. Profit and assets are then understated, the accounts are biased and they no longer give a true and fair view. The conflict is resolved by limiting provisions to losses that are probable and can be estimated."),
        PQ("Discuss two strengths and two limitations of the historical cost convention.",
           "Plan. Strengths: (1) objective and verifiable, since the cost is on an invoice; (2) simple and cheap to apply, and it prevents managers inflating assets with optimistic valuations. Limitations: (1) in times of rising prices, old assets are shown far below their current value, so the balance sheet is less relevant; (2) depreciation based on old costs is too low, so profit is overstated compared with the cost of replacing the asset. Evaluation: historical cost remains the general rule because reliability matters to lenders and tax officers, but notes to the accounts and, where the law allows, revaluations reduce its limits."),
        TIP("Exam link: the conceptual framework is tested mainly in Paper 1 multiple choice, where financial accounting formed the largest group of questions in the Board's 2023 report. It also gives the reasons behind treatments in Paper 3 Financial Accounting (stock at the lower of cost and net realisable value, provisions, leased assets). When a question asks 'which convention', give the name and one sentence linking it to the facts."),
        SUM("The revised SYSCOHADA framework aims at a true and fair view of assets, financial position and result.",
            "Useful information is relevant, reliable, comparable and understandable.",
            "Basic assumptions: entity, going concern, periodicity, monetary unit.",
            "Recording rules: historical cost, prudence, permanence of methods, materiality, substance over form, non-compensation, intangibility of the opening balance sheet, transparency.",
            "Conventions can conflict; prudence is caution, not deliberate understatement."),
    ],
))

# ------------------------------------------------------------------ 2. chart of accounts
_main_accounts = """Class 1  Long-term resources
 10 Capital            11 Reserves
 12 Retained earnings  13 Net result of the year
 14 Investment grants  15 Regulated provisions
 16 Loans              17 Location-acquisition debts
 19 Provisions for financial risks and charges
Class 2  Fixed assets
 21 Intangible assets  22 Land
 23 Buildings, installations and fittings
 24 Equipment, furniture, transport, biological
 25 Advances paid on fixed assets
 26 Participating interests  27 Other financial assets
 28 Depreciation       29 Impairment of fixed assets
Class 3  Stocks
 31 Goods for resale   32 Raw materials
 33 Other supplies     36 Finished products
 38 Stocks in transit  39 Impairment of stocks
Class 4  Third parties
 40 Suppliers          41 Customers
 42 Staff              43 Social bodies (CNPS)
 44 State              47 Sundry debtors, creditors
 48 Non-ordinary (HAO) receivables and payables
 49 Impairment of third-party accounts
Class 5  Treasury
 51 Values to collect  52 Banks
 56 Bank credits       57 Cash in hand
 59 Impairment of treasury items"""

_exp_inc = """Class 6  Ordinary expenses       Class 7  Ordinary income
 60 Purchases, stock changes     70 Sales
 61 Transport                    71 Operating grants
 62 External services A          72 Own work capitalised
 63 External services B          73 Change in stock of products
 64 Taxes and duties             75 Other income
 65 Other expenses               77 Financial income
 66 Staff costs                  78 Transfers of charges
 67 Financial expenses           79 Reversals of provisions
 68 Depreciation charges
 69 Provision charges
Class 8  Other expenses and income
 81 Book value of fixed assets sold
 82 Proceeds of fixed assets sold
 83 HAO expenses        84 HAO income
 85 HAO provision charges  86 HAO reversals
 87 Workers' profit share  88 Balancing grants
 89 Tax on the result"""

_ch_entries = [
    ("1 Mar  Goods bought on credit, invoice S41", [("601", "Purchases of goods", 1200000, 0), ("4452", "VAT on purchases", vat(1200000), 0), ("401", "Suppliers", 0, 1200000 + vat(1200000))]),
    ("4 Mar  Office computer on credit", [("244", "Office equipment", 800000, 0), ("4451", "VAT on fixed assets", vat(800000), 0), ("481", "Fixed asset suppliers", 0, 800000 + vat(800000))]),
    ("9 Mar  Old delivery van sold on credit", [("485", "Receivable on disposal", 2500000, 0), ("822", "Proceeds of disposals", 0, 2500000)]),
    ("31 Mar Electricity paid by bank", [("605", "Other purchases (power)", 150000, 0), ("521", "Bank", 0, 150000)]),
]
assert vat(1200000) == 231000 and vat(800000) == 154000
_ch_j = journal(_ch_entries)
_ch_dr = sum(x[2] for _, ls in _ch_entries for x in ls)
assert _ch_dr == 1431000 + 954000 + 2500000 + 150000 == 5035000

LESSONS.append(lesson(
    module=M1,
    topic="The SYSCOHADA chart of accounts",
    title="The revised SYSCOHADA chart of accounts: classes 1 to 9 and coding transactions",
    slug="acl1-syscohada-chart-of-accounts",
    minutes=24,
    summary="The revised SYSCOHADA chart has nine classes: 1 to 5 for the balance sheet, 6 to 8 for the result and 9 for commitments and cost accounting. The decimal code tells you the nature of an account, its normal balance and whether an item is ordinary (AO) or not (HAO).",
    objectives=[
        "Describe the structure of the revised SYSCOHADA chart and its decimal coding",
        "Give the main two-digit accounts of classes 1 to 8 and the role of class 9",
        "Identify contra accounts (depreciation, impairment, trade reductions) and normal balances",
        "Code transactions to the correct accounts and separate ordinary (AO) from non-ordinary (HAO) items",
    ],
    key_concepts=["Chart of accounts", "Class", "Main account", "Decimal coding", "Contra account", "Ordinary activities (AO)", "Non-ordinary activities (HAO)", "Class 9"],
    blocks=[
        H("Introduction"),
        T("Two accountants, one in Garoua and one in Abidjan, can read each other's ledgers without a word of explanation, because both use the same numbered chart of accounts. At O Level you learned the classes. At A Level you must code real transactions, including fixed assets, disposals, taxes and provisions, to the right account."),
        D("The **chart of accounts** (plan des comptes) is the standard numbered list of accounts. In the revised SYSCOHADA it uses a **decimal code**: the first digit is the **class**, two digits give the **main account**, three digits a **divisional account**, and more digits **sub-accounts** that an entity may create for its own needs.",
          title="Definition: chart of accounts and decimal coding"),
        IMG("alacl1-syscohada-classes.svg", alt="Nine boxes: classes 1 to 5 under balance sheet accounts (long-term resources, fixed assets, stocks, third parties, treasury); classes 6, 7 and 8 under result accounts (ordinary expenses, ordinary income, other expenses and income); class 9 under off balance sheet and analysis.",
            caption="Figure 1. The nine classes of the revised SYSCOHADA chart."),
        T("Example of coding: **2** = fixed assets; **24** = equipment, furniture, transport and biological assets; **245** = transport equipment. The deeper you go, the more precise the account. Sub-account numbers vary between textbooks and entities, so in this course we give the main account and add a divisional number only where it is standard."),
        H("Classes 1 to 5: the balance sheet accounts"),
        CODE(_main_accounts, "text", title="Main accounts of classes 1 to 5 (check divisional numbers in your textbook)"),
        H("Classes 6 to 9: the result and the rest"),
        CODE(_exp_inc, "text", title="Main accounts of classes 6, 7 and 8"),
        T("**Class 9** holds off-balance-sheet commitments (for example guarantees given or received) and the accounts of management (cost) accounting. It is not part of the balance sheet or income statement."),
        KEY("Patterns worth learning", "The code is not random; these patterns help you in Paper 1.", cards=[
            ["Second digit 8 or 9", "In classes 2 to 5, accounts 28, 29, 39, 49 and 59 are **contra accounts**: depreciation and impairment, deducted from the gross value of the asset. They have a credit balance."],
            ["Ordinary versus HAO", "Classes 6 and 7 hold ordinary activities (AO). Class 8 holds items outside ordinary activity (HAO), such as disposals of fixed assets (81 and 82), plus workers' profit share and tax on the result."],
            ["Mirror accounts", "Many expense and income accounts mirror each other: 673 discounts allowed and 773 discounts received; 676 exchange losses and 776 exchange gains; 81 book value of assets sold and 82 their proceeds."],
            ["Purchases are expenses", "601 Purchases of goods is a class 6 expense. Stock appears in class 3 only through inventory entries (account 6031 records the change in stock of goods)."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: code the transactions", intro="Ngono Distribution (VAT at the teaching rate of 19.25%) has four transactions in March: (1) goods bought on credit, FCFA 1 200 000 before VAT; (2) an office computer bought on credit, FCFA 800 000 before VAT; (3) an old delivery van sold on credit for FCFA 2 500 000 (VAT ignored); (4) electricity of FCFA 150 000 paid by bank (VAT ignored). Journalise them.", steps=[
            S("(1) Goods for resale", text="Expense 601, recoverable VAT on purchases 4452, supplier 401. VAT = 1 200 000 x 19.25% = 231 000."),
            S("(2) Office computer", text="A fixed asset, class 2 (244), VAT on fixed assets 4451, and the supplier of a fixed asset is account **481**, not 401. VAT = 154 000."),
            S("(3) Sale of the van", text="Not an ordinary sale: the receivable is **485** and the proceeds go to **822** (class 8, HAO). The van's book value is removed later through 812 (lesson on disposals)."),
            S("(4) Electricity", text="A non-stocked supply, class 60 (605 other purchases), paid from the bank 521."),
            S("Check", math=r"1\,431\,000 + 954\,000 + 2\,500\,000 + 150\,000 = 5\,035\,000", text="Total debits equal total credits for each entry and for the month."),
        ]),
        CODE(_ch_j, "text", title="Journal of Ngono Distribution, March (FCFA, invented for practice)"),
        EX("Worked example 2: AO or HAO?", intro="Classify: (a) sale of goods to a customer; (b) sale of a used machine; (c) a fine paid for late filing of a tax return; (d) interest received on a bank deposit.", steps=[
            S("(a) Sale of goods", text="Ordinary activity: **701** (class 7)."),
            S("(b) Sale of a used machine", text="Not ordinary: **822** proceeds and **812** book value (class 8)."),
            S("(c) Tax fine", text="Penalties are generally treated as HAO expenses (83) in SYSCOHADA textbooks; check your textbook, as some classify them among other ordinary expenses."),
            S("(d) Interest received", text="Ordinary financial income: class 77."),
        ]),
        EX("Worked example 3: read a code", intro="What do these tell you: 2845, 4194, 6031, 7019?", steps=[
            S("2845", text="Starts with 28: depreciation of fixed assets; 2845 is depreciation of transport equipment (245). A contra-asset with a credit balance."),
            S("4194", text="Class 4, customers group (41): an amount owed **to** customers for returnable packaging deposits (you meet it in the packaging lesson). Credit balance."),
            S("6031", text="Change in stock of goods: debited for opening stock and credited for closing stock."),
            S("7019", text="Trade reductions (rabais, remises, ristournes) granted on sales, a contra account to 701: debit balance."),
        ]),
        MISTAKE("Crediting 401 for a fixed asset supplier", "Suppliers of fixed assets are recorded in 481, so that trade debts and investment debts are shown separately. 401 is for suppliers of goods and services."),
        MISTAKE("Putting disposals in class 7", "The sale of a fixed asset is not an ordinary sale. Proceeds go to 822 and the book value to 812, both in class 8."),
        MISTAKE("Assuming every class 4 account is a debit", "41 customers is usually a debit, but 4194 (deposits owed to customers), 40 suppliers, 42 staff, 43 CNPS and 44 State are usually credits. Decide from the meaning."),
        QUIZ("Which account is credited when a business buys a delivery van on credit?",
             ["401 Suppliers", "481 Fixed asset suppliers", "245 Transport equipment", "411 Customers"], 1,
             "Debts to suppliers of fixed assets go to 481.",
             hint="Is the van stock for resale or an investment?",
             feedback=["401 is for suppliers of goods and services used in ordinary trade.", "", "245 is debited: it is the asset itself.", "411 is customers, who owe the business money."]),
        QUIZ("Accounts 28, 39 and 49 have in common that they",
             ["are expenses of the year", "are contra accounts with a credit balance", "belong to class 8", "are off-balance-sheet commitments"], 1,
             "They are depreciation and impairment accounts deducted from assets.",
             hint="Look at the second digit and think about what is deducted from an asset.",
             feedback=["The expenses are in classes 68 and 69, not 28, 39, 49.", "", "They are in classes 2, 3 and 4.", "Commitments are in class 9."]),
        PQ("Explain the structure of the SYSCOHADA account code using 2845 as an example.",
           "First digit **2**: class 2, fixed assets. **28**: main account, depreciation of fixed assets. **284**: depreciation of equipment, furniture and transport (mirrors 24). **2845**: depreciation of transport equipment (mirrors 245). Each extra digit gives more detail."),
        PQ("State the account to debit and the account to credit: (a) wages for the month due to staff; (b) a customer pays by bank transfer; (c) depreciation charge on equipment for the year.",
           "(a) Dr 66 Staff costs (661), Cr 42 Staff (422 remuneration due). (b) Dr 521 Bank, Cr 411 Customers. (c) Dr 681 Depreciation charges, Cr 284 Depreciation of equipment (the 28 account matching the asset)."),
        PQ("Why does the revised SYSCOHADA separate ordinary (AO) items from non-ordinary (HAO) items? Give two examples of HAO items.",
           "So that the result of the normal, repeating business (the ordinary result) can be read separately from one-off events that will not recur; this helps users forecast and compare years. Examples: proceeds and book value of fixed assets sold (82 and 81); HAO expenses and income such as certain penalties or gifts (83, 84); HAO provision charges (85)."),
        TIP("Exam link: Paper 1 often tests the class or main account of an item, and in Paper 3 every journal entry must show account numbers and names. The Board's 2023 report asked teachers to teach the approach and format of accounts, so write the number and the name on every line."),
        SUM("Decimal coding: first digit class, two digits main account, more digits detail.",
            "Classes 1 to 5: balance sheet; 6 and 7: ordinary result; 8: HAO items, profit share and tax; 9: commitments and cost accounting.",
            "28, 29, 39, 49, 59 are contra accounts with credit balances.",
            "Fixed asset suppliers: 481; disposals: 812 and 822 with receivable 485.",
            "Always give both the number and the name of the account."),
    ],
))

# ------------------------------------------------------------------ 3. accounting systems
_sm = dict(rec=18400000, d0=300000, d1=750000, paid=11200000, c0=900000, c1=600000, s0=1500000, s1=2100000,
           rent=1200000, wages=2400000, transp=650000, equip=3000000, life=5)
_sm_sales = _sm["rec"] + _sm["d1"] - _sm["d0"]
_sm_purch = _sm["paid"] + _sm["c1"] - _sm["c0"]
_sm_cogs = _sm["s0"] + _sm_purch - _sm["s1"]
_sm_gm = _sm_sales - _sm_cogs
_sm_oth = _sm["rent"] + _sm["wages"] + _sm["transp"]
_sm_dep = _sm["equip"] // _sm["life"]
_sm_res = _sm_gm - _sm_oth - _sm_dep
_sm_pay_all = _sm["paid"] + _sm_oth + _sm["equip"]
_sm_cash = _sm["rec"] - _sm_pay_all
assert (_sm_sales, _sm_purch, _sm_cogs, _sm_gm) == (18850000, 10900000, 10300000, 8550000)
assert (_sm_oth, _sm_dep, _sm_res, _sm_pay_all, _sm_cash) == (4250000, 600000, 3700000, 18450000, -50000)

# quiz and practice figures
assert 9000000 + 650000 - 400000 == 9250000 and 9000000 - 650000 + 400000 == 8750000
_pq_s = 12600000 + 500000 - 200000
_pq_p = 8100000 + 400000 - 700000
_pq_c = 900000 + _pq_p - 1300000
assert (_pq_s, _pq_p, _pq_c, _pq_s - _pq_c, _pq_s - _pq_c - 2300000) == (12900000, 7800000, 7400000, 5500000, 3200000)

_sm_tbl = rows([
    ("Receipts from customers", _sm["rec"]),
    ("Payments to suppliers of goods", -_sm["paid"]),
    ("Rent, wages and transport paid", -_sm_oth),
    ("Equipment bought for cash", -_sm["equip"]),
    (None, None),
    ("Net cash flow of the year", _sm_cash),
])
_sm_res_tbl = rows([
    ("Sales (18 400 000 + 750 000 - 300 000)", _sm_sales),
    ("Purchases (11 200 000 + 600 000 - 900 000)", _sm_purch),
    ("Opening stock", _sm["s0"]),
    ("Less closing stock", -_sm["s1"]),
    ("Cost of goods sold", _sm_cogs),
    (None, None),
    ("Gross margin", _sm_gm),
    ("Rent, wages and transport", -_sm_oth),
    ("Depreciation (3 000 000 / 5)", -_sm_dep),
    (None, None),
    ("Result of the year (profit)", _sm_res),
], w=42)

LESSONS.append(lesson(
    module=M1,
    topic="The accounting systems",
    title="The normal system and the minimal cash system (SMT)",
    slug="acl1-normal-and-minimal-cash-systems",
    minutes=24,
    summary="The revised SYSCOHADA offers two accounting systems: the normal system, with full double entry and four financial statements, and the minimal cash system (SMT) for very small entities, kept mainly from receipts and payments and adjusted at the year end for stocks, receivables and payables.",
    objectives=[
        "Describe the normal system and the minimal cash system (SMT) and say which entities use each",
        "List the financial statements produced under each system",
        "Convert cash receipts and payments into sales, purchases and a result using receivables, payables and stocks",
        "Evaluate the SMT for a small Cameroonian business",
    ],
    key_concepts=["Normal system", "Minimal cash system (SMT)", "Turnover threshold", "Cash basis", "Accrual basis", "Financial statements"],
    blocks=[
        H("Introduction"),
        T("A tailor in Bamenda with two apprentices and a large trading company in Douala cannot be asked to keep the same books. The tailor has no accountant and sells mostly for cash; the company has hundreds of credit customers, a bank loan and shareholders. The revised SYSCOHADA therefore gives two **accounting systems**, chosen according to the size of the entity."),
        D("The **normal system** (systeme normal) applies to most entities. It uses full double entry with the whole chart of accounts and produces four financial statements: the **balance sheet**, the **income statement**, the **cash flow statement** (TFT) and the **notes**.",
          title="Definition: the normal system"),
        D("The **minimal cash system** (systeme minimal de tresorerie, SMT) is reserved for very small entities whose annual turnover does not exceed limits fixed by the Uniform Act. The figures usually quoted are FCFA 60 million for trading entities, 40 million for craft entities and 30 million for service entities; check the current text and your textbook. The entity records mainly its **receipts and payments** and prepares simplified statements at the year end.",
          title="Definition: the minimal cash system (SMT)"),
        T("Under the earlier SYSCOHADA there was also a simplified (allege) system for medium entities. The 2017 revision kept only the normal system and the SMT; check your textbook if it still mentions the old system."),
        KEY("Normal system and SMT compared", "Same purpose, different depth.", cards=[
            ["Records", "Normal: journal, general ledger, trial balance and inventory book, full double entry. SMT: mainly a receipts and payments (cash) book, plus lists of receivables, payables and stock at the year end."],
            ["Basis", "Normal: accrual basis, every transaction recorded when it happens. SMT: cash basis during the year, adjusted at the year end."],
            ["Statements", "Normal: balance sheet, income statement, cash flow statement and notes. SMT: a simplified balance sheet, a simplified result statement and notes (check your textbook for the exact names)."],
            ["Who", "Normal: any entity above the SMT limits, and any entity that chooses it. SMT: very small entities below the limits."],
        ]),
        H("From cash to result: the year-end adjustment"),
        T("Cash records alone do not give the profit. A sale is earned when goods are delivered, even if the customer pays next year; a supplier invoice is an expense when the goods arrive, even if it is paid later; equipment is not an expense of one year. So the cash figures are adjusted:"),
        F(r"\text{Sales} = \text{receipts} + \text{closing receivables} - \text{opening receivables}", title="Sales from receipts"),
        F(r"\text{Purchases} = \text{payments} + \text{closing payables} - \text{opening payables}", title="Purchases from payments"),
        F(r"\text{Cost of goods sold} = \text{opening stock} + \text{purchases} - \text{closing stock}", title="Cost of goods sold"),
        EX("Worked example 1: the cash view", intro="Madame Ewane runs a provision shop under the SMT. For the year: receipts from customers FCFA 18 400 000; paid to suppliers 11 200 000; rent, wages and transport paid 4 250 000; equipment bought for cash 3 000 000 (life 5 years). Opening and closing figures: receivables 300 000 and 750 000; payables to suppliers 900 000 and 600 000; stock 1 500 000 and 2 100 000. What does the cash book show?", steps=[
            S("Total payments", math=r"11\,200\,000 + 4\,250\,000 + 3\,000\,000 = 18\,450\,000"),
            S("Net cash flow", math=r"18\,400\,000 - 18\,450\,000 = -50\,000", text="On a cash view the shop seems to have lost 50 000."),
        ]),
        CODE(_sm_tbl, "text", title="Cash summary (FCFA, invented for practice)"),
        EX("Worked example 2: the result after adjustments", intro="Use the same figures to find the true result of the year.", steps=[
            S("Sales", math=r"18\,400\,000 + 750\,000 - 300\,000 = 18\,850\,000", text="Customers owe more at the end, so sales were higher than receipts."),
            S("Purchases", math=r"11\,200\,000 + 600\,000 - 900\,000 = 10\,900\,000", text="Part of the payments settled last year's debts."),
            S("Cost of goods sold", math=r"1\,500\,000 + 10\,900\,000 - 2\,100\,000 = 10\,300\,000"),
            S("Gross margin", math=r"18\,850\,000 - 10\,300\,000 = 8\,550\,000"),
            S("Depreciation instead of the cash cost of equipment", math=r"3\,000\,000 \div 5 = 600\,000"),
            S("Result", math=r"8\,550\,000 - 4\,250\,000 - 600\,000 = 3\,700\,000", text="A **profit of FCFA 3 700 000**, although cash fell by 50 000: the money went into equipment, stock and credit to customers."),
        ]),
        CODE(_sm_res_tbl, "text", title="Result of Madame Ewane's shop (FCFA)"),
        EX("Worked example 3: which system?", intro="Which system should each entity use? (a) a hairdressing salon with turnover FCFA 18 million; (b) a building-materials trader with turnover FCFA 95 million; (c) a carpentry workshop with turnover FCFA 35 million. Use the limits quoted above.", steps=[
            S("(a) Services, 18 million", text="Below the 30 million services limit: may use the **SMT**."),
            S("(b) Trading, 95 million", text="Above the 60 million trading limit: **normal system**."),
            S("(c) Craft, 35 million", text="Below the 40 million craft limit: may use the **SMT**. Any entity may still choose the normal system."),
        ]),
        H("Evaluation"),
        T("The SMT is cheap and simple: a small trader who could not pay an accountant can still keep legal records and show a result to a microfinance institution. Its limits are that the cash book alone misleads (as the example shows, cash fell while profit was good), information on debts and stock is collected only once a year, and errors are harder to find without double entry. As the business grows past the limits it must move to the normal system, which costs more but gives managers and lenders far better information."),
        MISTAKE("Taking net cash flow as profit", "Receipts minus payments is a cash movement. Profit needs the adjustments for receivables, payables, stock and depreciation."),
        MISTAKE("Adjusting in the wrong direction", "Closing receivables are added to receipts (sales not yet paid for); opening receivables are subtracted (cash received this year for last year's sales). The same logic applies to payables."),
        MISTAKE("Treating the purchase of equipment as an expense", "Equipment is a fixed asset. Only its depreciation for the year reduces the result."),
        QUIZ("Receipts from customers FCFA 9 000 000; opening receivables 400 000; closing receivables 650 000. Sales for the year are",
             ["FCFA 8 750 000", "FCFA 9 250 000", "FCFA 9 650 000", "FCFA 10 050 000"], 1,
             "Sales = 9 000 000 + 650 000 - 400 000 = 9 250 000.",
             hint="Add what customers still owe at the end; remove what they owed at the start.",
             feedback=["You reversed the adjustment.", "", "You added the closing receivables but forgot to remove the opening ones.", "You added both balances."]),
        QUIZ("Which statement is produced under the normal system but not required in the same form under the SMT?",
             ["A receipts and payments record", "The cash flow statement (TFT)", "A list of stock at the year end", "A result for the year"], 1,
             "The normal system produces four statements including the TFT; the SMT produces simplified statements.",
             hint="Which of the four normal-system statements is about flows of cash by activity?",
             feedback=["The SMT is built on a receipts and payments record.", "", "Both systems need the year-end stock.", "Both systems find a result."]),
        PQ("Distinguish between the normal system and the minimal cash system under the revised SYSCOHADA.",
           "The **normal system** is used by entities above the SMT limits: full double entry, the whole chart of accounts, accrual basis, and four statements (balance sheet, income statement, cash flow statement, notes). The **SMT** is for very small entities below turnover limits (usually quoted as 60, 40 and 30 million FCFA for trading, craft and services; check the current text): records mainly receipts and payments, adjusted at the year end, with simplified statements."),
        PQ("A small trader under the SMT received FCFA 12 600 000 from customers and paid suppliers FCFA 8 100 000. Receivables rose from 200 000 to 500 000, payables fell from 700 000 to 400 000, and stock rose from 900 000 to 1 300 000. Other expenses paid: 2 300 000. Find sales, purchases, cost of goods sold and the result.",
           "Sales = 12 600 000 + 500 000 - 200 000 = **12 900 000**. Purchases = 8 100 000 + 400 000 - 700 000 = **7 800 000**. Cost of goods sold = 900 000 + 7 800 000 - 1 300 000 = **7 400 000**. Gross margin = 12 900 000 - 7 400 000 = 5 500 000. Result = 5 500 000 - 2 300 000 = **FCFA 3 200 000 profit**."),
        PQ("Evaluate the usefulness of the minimal cash system for a market trader who wants a loan.",
           "Plan. For: simple and cheap; gives legal records and a result the lender can read; encourages small traders to keep books at all. Against: during the year only cash is visible, so the trader may not see growing debts or stock; without double entry, errors and omissions are harder to detect; lenders may want fuller statements for larger loans. Judgement: suitable while the business is small, provided the year-end adjustments are done carefully; as turnover grows the normal system becomes necessary and more useful."),
        TIP("Exam link: the systems appear in Paper 1 multiple choice (which system, which statements), and the cash-to-result adjustments are the same skills used for incomplete records in Paper 3. Always set out the formula first, then the figures."),
        SUM("The revised SYSCOHADA has two systems: the normal system and the minimal cash system (SMT).",
            "Normal system: full double entry, accrual basis, four statements (balance sheet, income statement, TFT, notes).",
            "SMT: very small entities below turnover limits (check the current figures); mainly receipts and payments.",
            "Sales = receipts + closing receivables - opening receivables; purchases are found the same way from payments and payables.",
            "Cash flow is not profit: adjust for receivables, payables, stock and depreciation."),
    ],
))

# ------------------------------------------------------------------ 4. books, journals, computerised accounting
_sj_rows4 = [("3 Apr", "Abena", "F201", 600000), ("12 Apr", "Bello", "F202", 900000), ("25 Apr", "Abena", "F203", 400000)]
_sj4_body = []
_sj4_ht = _sj4_tva = _sj4_ttc = 0
_sj4_cust = {}
for _d, _c, _f, _h in _sj_rows4:
    _t = vat(_h)
    _sj4_body.append([_d, _c, _f, _h, _t, _h + _t])
    _sj4_ht += _h
    _sj4_tva += _t
    _sj4_ttc += _h + _t
    _sj4_cust[_c] = _sj4_cust.get(_c, 0) + _h + _t
assert (_sj4_ht, _sj4_tva, _sj4_ttc) == (1900000, 365750, 2265750)
assert _sj4_cust == {"Abena": 1192500, "Bello": 1073250} and sum(_sj4_cust.values()) == _sj4_ttc
_sj4_tbl = grid(["Date", "Customer", "Inv", "Net", "VAT", "Total"], [7, 9, 5, 10, 9, 11],
                _sj4_body + [None, ["Totals", "", "", _sj4_ht, _sj4_tva, _sj4_ttc]], left=3)
_sj4_central = journal([("30 Apr  Centralisation of the sales journal", [
    ("411", "Customers", _sj4_ttc, 0), ("701", "Sales of goods", 0, _sj4_ht), ("443", "VAT invoiced", 0, _sj4_tva)])])

# six-column trial balance: account -> (opening balance signed, Dr movements, Cr movements); + = debit
_tb6 = {
    "101": (-5000000, 0, 0),
    "244": (2000000, 0, 0),
    "31": (1000000, 0, 0),
    "401": (-500000, 1500000, 1200000 + vat(1200000)),
    "411": (800000, _sj4_ttc, 1900000),
    "4452": (0, vat(1200000), 0),
    "443": (0, 0, _sj4_tva),
    "521": (1700000, 1900000, 1500000),
    "601": (0, 1200000, 0),
    "701": (0, 0, _sj4_ht),
}
_tb6_names = {"101": "Capital", "244": "Equipment", "31": "Goods", "401": "Suppliers", "411": "Customers",
              "4452": "VAT on purchases", "443": "VAT invoiced", "521": "Bank", "601": "Purchases", "701": "Sales"}
_tb6_body = []
_tot = [0] * 6
for _a, (_o, _md, _mc) in _tb6.items():
    _c = _o + _md - _mc
    _r = [max(_o, 0), max(-_o, 0), _md, _mc, max(_c, 0), max(-_c, 0)]
    _tot = [x + y for x, y in zip(_tot, _r)]
    _tb6_body.append([_a] + [x if x else "" for x in _r])
assert _tot[0] == _tot[1] == 5500000
assert _tot[2] == _tot[3] == 7096750
assert _tot[4] == _tot[5]
_tb6_close = _tot[4]
assert _tb6_close == 7696750
_tb6_tbl = grid(["Acct", "Open Dr", "Open Cr", "Flow Dr", "Flow Cr", "Close Dr", "Close Cr"], [5, 10, 10, 10, 10, 10, 10],
                _tb6_body + [None, ["Total"] + _tot])
_tb6_key = chr(10).join("   ".join(f"{a} {nm}" for a, nm in list(_tb6_names.items())[i:i + 3]) for i in range(0, 10, 3))
assert _tb6["411"][0] + _tb6["411"][1] - _tb6["411"][2] == 1165750
assert _tb6["401"][0] + _tb6["401"][1] - _tb6["401"][2] == -431000
assert _tb6["521"][0] + _tb6["521"][1] - _tb6["521"][2] == 2100000

LESSONS.append(lesson(
    module=M1,
    topic="Books, journals and computerized accounting",
    title="Compulsory books, the centralising system and computerised accounting",
    slug="acl1-books-journals-computerised",
    minutes=26,
    summary="OHADA law requires a journal, a general ledger, a trial balance and an inventory book. Most firms use auxiliary journals centralised monthly, auxiliary ledgers that agree with collective accounts, a six-column trial balance, and software that posts each validated entry automatically.",
    objectives=[
        "List the compulsory accounting books and the rules for keeping them",
        "Explain the centralising system: auxiliary journals, centralisation, auxiliary ledgers and collective accounts",
        "Prepare a centralisation entry and a six-column trial balance",
        "Describe the workflow and controls of computerised accounting and evaluate it",
    ],
    key_concepts=["Journal", "General ledger", "Trial balance", "Inventory book", "Auxiliary journal", "Centralisation", "Collective account", "Six-column trial balance", "Validation", "Audit trail"],
    blocks=[
        H("Introduction"),
        T("A supermarket in Yaounde issues hundreds of sales invoices a day. If each one were written as a separate entry in one journal and posted one by one to the ledger, the accountant would never finish. The answer is a **system** of books in which work is divided, totalled and centralised, and today usually done by software."),
        H("The compulsory books"),
        KEY("Books required by the Uniform Act", "Under the normal system an entity keeps these books (check your textbook for the exact wording of the law).", cards=[
            ["Journal (livre-journal)", "Records every transaction in date order, with the accounts debited and credited and a reference to the document."],
            ["General ledger (grand livre)", "Groups the entries account by account, so the balance of each account can be found."],
            ["Trial balance (balance generale)", "Lists all accounts with their totals and balances; total debits must equal total credits."],
            ["Inventory book (livre d'inventaire)", "Records the year-end inventory of assets and liabilities and the financial statements."],
        ]),
        T("The books must be kept in date order, without blank spaces or alterations; a mistake is corrected by a new entry (for example a reversing entry), never by erasing. Records and supporting documents are kept for a long period, commonly stated as ten years; check the current rule."),
        H("The centralising system"),
        D("In the **centralising system**, transactions of the same kind are first recorded in **auxiliary journals** (sales, purchases, bank, cash and miscellaneous operations, OD). At the end of each month the totals of each auxiliary journal are posted in one **centralisation entry** to the general journal and the general ledger.",
          title="Definition: centralising system"),
        D("A **collective account** (such as 401 Suppliers or 411 Customers) in the general ledger shows the total owed by or to all customers or suppliers. The details are kept in **auxiliary ledgers**, with one account per customer or supplier. The total of the auxiliary balances must agree with the collective account.",
          title="Definition: collective account and auxiliary ledger"),
        IMG("alacl1-centralising-system.svg", alt="Flow chart: documents go to auxiliary journals, then monthly centralisation to the general ledger; auxiliary journals also feed auxiliary ledgers, which agree with collective accounts 401 and 411; the ledger gives the trial balance, then the statements.",
            caption="Figure 1. The centralising system. The dashed line means the auxiliary ledgers must agree with the collective accounts."),
        EX("Worked example 1: the sales journal and its centralisation", intro="Ngono Distribution issued three credit sales invoices in April (VAT at the teaching rate of 19.25%). Prepare the sales journal, the centralisation entry and the customers' auxiliary balances.", steps=[
            S("VAT on each invoice", math=r"600\,000 \times 19.25\% = 115\,500;\ 900\,000 \times 19.25\% = 173\,250;\ 400\,000 \times 19.25\% = 77\,000"),
            S("Totals of the journal", math=r"\text{Net } 1\,900\,000 + \text{VAT } 365\,750 = 2\,265\,750"),
            S("Centralisation entry", text="Debit 411 with the total of the invoices; credit 701 with the net total and 443 with the VAT total."),
            S("Auxiliary ledger check", math=r"\text{Abena } 1\,192\,500 + \text{Bello } 1\,073\,250 = 2\,265\,750", text="Equal to the debit to the collective account 411."),
        ]),
        CODE(_sj4_tbl, "text", title="Sales journal, April (FCFA, invented for practice)"),
        CODE(_sj4_central, "text", title="Centralisation entry"),
        H("The six-column trial balance"),
        T("A **six-column trial balance** shows, for every account, the opening balance (debit or credit), the movements of the period (total debits and total credits) and the closing balance. Each pair of columns must have equal totals, which gives three checks instead of one."),
        EX("Worked example 2: six-column trial balance", intro="Ngono Distribution's April activity: the sales journal above; FCFA 1 900 000 received from customers by bank; goods bought on credit for 1 200 000 plus VAT; FCFA 1 500 000 paid to suppliers by bank. Prepare the six-column trial balance.", steps=[
            S("Opening columns", text="From the balance sheet at 31 March: total debits = total credits = 5 500 000."),
            S("Movement columns", math=r"2\,265\,750 + 1\,900\,000 + 1\,200\,000 + 231\,000 + 1\,500\,000 = 7\,096\,750", text="Total debit movements; the credit movements give the same total."),
            S("Closing balance of each account", text="Opening + debits - credits. Customers: 800 000 + 2 265 750 - 1 900 000 = 1 165 750 debit. Suppliers: -500 000 + 1 500 000 - 1 431 000 = 431 000 credit. Bank: 1 700 000 + 1 900 000 - 1 500 000 = 2 100 000 debit."),
            S("Closing totals", math=r"\text{Close Dr} = \text{Close Cr} = 7\,696\,750"),
        ]),
        CODE(_tb6_tbl + "\n\n" + _tb6_key, "text", title="Six-column trial balance at 30 April (FCFA)"),
        H("Computerised accounting"),
        T("Accounting software follows the same logic. The accountant sets up the chart of accounts, the journal codes and the customer and supplier files; enters each document once; **validates** the entry; and the software posts it to the ledgers and produces trial balances and statements on demand. **Matching** (lettrage) links each invoice to its payment, so unpaid items are listed automatically."),
        KEY("Controls in a computerised system", "Software removes arithmetic errors but not all errors.", cards=[
            ["Access rights", "Each user has a password and can do only the tasks allowed (enter, validate, close a period)."],
            ["Validation and closing", "Once validated and the period closed, an entry cannot be changed; a correction is a new entry. This keeps the records reliable, as the law requires for paper books."],
            ["Audit trail", "Every entry keeps its author, date and document reference, so it can be traced."],
            ["Backups", "Regular copies are kept off site; power cuts and theft of computers are real risks."],
        ]),
        T("**Evaluation.** Computerised accounting is fast, totals and balances are always correct, and reports are available at any time. But a wrong account code or a wrong amount is posted just as quickly as a right one; errors of principle and omission still need human checks. Software, training and reliable power cost money, and data can be lost without backups. For most firms the benefits outweigh the costs, provided controls are in place."),
        MISTAKE("Posting each invoice to 411 and also posting the centralisation total", "Each invoice goes to the customer's auxiliary account; the general ledger account 411 receives only the monthly total. Posting both doubles the debt."),
        MISTAKE("Thinking the computer finds all errors", "A balanced trial balance only proves that debits equal credits. Compensating errors, wrong accounts and omissions are not revealed, whether by hand or by software."),
        MISTAKE("Adding opening and movement columns in the same direction for every account", "Closing balance = opening debit balance + debits - credits. For an account with an opening credit balance, treat it as negative, as for 401 above."),
        QUIZ("The auxiliary customers ledger shows balances of 450 000, 1 200 000 and 350 000. The collective account 411 shows 2 100 000. What should the accountant conclude?",
             ["The accounts agree", "There is a difference of 100 000 to investigate", "411 should be changed to 2 000 000 at once", "The trial balance cannot balance"], 1,
             "450 000 + 1 200 000 + 350 000 = 2 000 000, which differs from 2 100 000 by 100 000. The cause must be found before correcting.",
             hint="Add the auxiliary balances and compare.",
             feedback=["The total of the auxiliary balances is 2 000 000, not 2 100 000.", "", "A correction is made only after the cause is found, by a correcting entry.", "The general trial balance can still balance; the difference is between the ledger and its auxiliary."]),
        QUIZ("Which is NOT one of the compulsory books of the normal system?",
             ["Journal", "General ledger", "Inventory book", "Petty cash voucher file"], 3,
             "The compulsory books are the journal, the general ledger, the trial balance and the inventory book.",
             hint="Three of these are books required by the law; one is a set of supporting documents.",
             feedback=["The journal is compulsory.", "The general ledger is compulsory.", "The inventory book is compulsory.", ""]),
        PQ("Explain three advantages of the centralising system over a single journal.",
           "(1) **Division of work**: different clerks keep the sales, purchases, bank and cash journals at the same time. (2) **Fewer postings**: the general ledger receives monthly totals, not every transaction. (3) **Control**: auxiliary ledgers must agree with collective accounts, and journal totals can be cross-checked, so errors are found quickly."),
        PQ("In May a purchases journal shows net 2 400 000, VAT 462 000 and total 2 862 000. Give the centralisation entry.",
           "Dr 601 Purchases of goods 2 400 000; Dr 4452 VAT on purchases 462 000; Cr 401 Suppliers 2 862 000. (Check: 2 400 000 x 19.25% = 462 000; 2 400 000 + 462 000 = 2 862 000.)"),
        PQ("Evaluate the replacement of manual books by accounting software in a medium-sized firm in Cameroon.",
           "Plan. Benefits: speed; arithmetic always right; instant trial balances, ageing of customers and statements; matching of invoices and payments; easier tax returns. Costs and risks: purchase and training; dependence on power and computers; errors of principle still possible; data loss or fraud without passwords, backups and an audit trail. Judgement: worth it for a medium firm if controls (access rights, closing of periods, backups) are set up and staff are trained."),
        TIP("Exam link: Paper 1 asks about the books, the centralising system and controls; Paper 3 questions start from journals and end in statements. In a long question, keep a neat working trial balance: the Board's 2023 report stresses the correct format of accounts."),
        SUM("Compulsory books: journal, general ledger, trial balance, inventory book; no erasures, corrections by new entries.",
            "Centralising system: auxiliary journals totalled monthly and centralised to the general journal.",
            "Auxiliary ledgers must agree with the collective accounts 401 and 411.",
            "A six-column trial balance checks opening balances, movements and closing balances.",
            "Software posts validated entries automatically; access rights, closing, audit trail and backups protect the records."),
    ],
))

# ------------------------------------------------------------------ 5. invoicing and trade reductions
_iv_gross = 200 * 20000
_iv_rab = _iv_gross * 5 // 100
_iv_a = _iv_gross - _iv_rab
_iv_rem = _iv_a * 10 // 100
_iv_nc = _iv_a - _iv_rem
_iv_esc = _iv_nc * 2 // 100
_iv_nf = _iv_nc - _iv_esc
_iv_port = 60000
_iv_base = _iv_nf + _iv_port
_iv_vat = vat(_iv_base)
_iv_ttc = _iv_base + _iv_vat
assert (_iv_gross, _iv_rab, _iv_a, _iv_rem, _iv_nc) == (4000000, 200000, 3800000, 380000, 3420000)
assert (_iv_esc, _iv_nf, _iv_base, _iv_vat, _iv_ttc) == (68400, 3351600, 3411600, 656733, 4068333)
assert _iv_gross * 95 * 90 // 10000 == _iv_nc  # single equivalent rate 14.5 %
_iv_cost = 200 * 13500
assert _iv_cost == 2700000

_iv_tbl = rows([
    ("200 bags of rice x 20 000", _iv_gross),
    ("Less rabais 5% (damaged packing)", -_iv_rab),
    ("Net after rabais", _iv_a),
    ("Less remise 10% (quantity)", -_iv_rem),
    ("NET COMMERCIAL AMOUNT", _iv_nc),
    ("Less escompte 2% (prompt payment)", -_iv_esc),
    ("NET FINANCIAL AMOUNT", _iv_nf),
    ("Transport charged (port)", _iv_port),
    (None, None),
    ("Amount subject to VAT", _iv_base),
    ("VAT 19.25%", _iv_vat),
    (None, None),
    ("NET TO PAY", _iv_ttc),
], w=36)

_iv_seller = journal([
    ("Invoice F75: sale to Tabi Stores", [("411", "Customers", _iv_ttc, 0), ("673", "Discounts allowed", _iv_esc, 0),
                                          ("701", "Sales of goods", 0, _iv_nc), ("707", "Transport charged", 0, _iv_port),
                                          ("443", "VAT invoiced", 0, _iv_vat)]),
    ("Permanent inventory: cost of goods sold", [("6031", "Change in stock of goods", _iv_cost, 0), ("31", "Goods for resale", 0, _iv_cost)]),
])
_iv_buyer = journal([
    ("Invoice F75 from Kamga Wholesale", [("601", "Purchases of goods", _iv_nc, 0), ("611", "Transport on purchases", _iv_port, 0),
                                          ("4452", "VAT on purchases", _iv_vat, 0), ("401", "Suppliers", 0, _iv_ttc),
                                          ("773", "Discounts received", 0, _iv_esc)]),
    ("Permanent inventory: goods into stock", [("31", "Goods for resale", _iv_nc + _iv_port, 0), ("6031", "Change in stock of goods", 0, _iv_nc + _iv_port)]),
])
assert _iv_nc + _iv_port == 3480000

_cn_net = 100000
_cn_vat = vat(_cn_net)
assert _cn_vat == 19250
_cn_j = journal([
    ("Seller: credit note A12 (later rabais)", [("7019", "Reductions granted", _cn_net, 0), ("443", "VAT invoiced", _cn_vat, 0), ("411", "Customers", 0, _cn_net + _cn_vat)]),
    ("Buyer: credit note A12 received", [("401", "Suppliers", _cn_net + _cn_vat, 0), ("6019", "Reductions obtained", 0, _cn_net), ("4452", "VAT on purchases", 0, _cn_vat)]),
])

_rv_ttc = 2039175
_rv_base = _Fr(_rv_ttc) / (1 + VAT_RATE)
_rv_gross = _rv_base / _Fr(855, 1000)
assert _rv_base == 1710000 and _rv_gross == 2000000
# practice question figures
assert 600000 * 90 * 95 // 10000 == 513000 and 513000 * 98 // 100 == 502740 and vat(502740 + 49260) == 106260
assert 502740 + 49260 + 106260 == 658260 and 513000 + 49260 + 106260 == 658260 + 10260 == 668520

LESSONS.append(lesson(
    module=M2,
    topic="Invoicing and trade reductions",
    title="Complex invoices: successive reductions, financial discount, transport and VAT",
    slug="acl1-invoicing-trade-reductions",
    minutes=26,
    summary="A full invoice applies trade reductions one after another (rabais, remise, ristourne), then the financial discount (escompte), adds transport, and charges VAT on the result. Trade reductions on the invoice are not recorded; the escompte is, and later reductions go through credit notes.",
    objectives=[
        "Complete an invoice with successive trade reductions, financial discount, transport and VAT",
        "Find the single equivalent rate of successive reductions and work an invoice backwards from the net to pay",
        "Journalise an invoice in the books of the seller and of the buyer, including permanent-inventory entries",
        "Record a credit note for a reduction granted after the invoice",
    ],
    key_concepts=["Gross amount", "Rabais", "Remise", "Ristourne", "Net commercial amount", "Escompte", "Net financial amount", "Port (transport charged)", "Credit note (avoir)", "Single equivalent rate"],
    blocks=[
        H("Introduction"),
        T("Kamga Wholesale in Douala sells 200 bags of rice to Tabi Stores in Bamenda. Some bags have torn packing, the order is large and Tabi pays at once. Each fact reduces the price in a different way, and each reduction is treated differently in the books. At A Level you must complete such invoices, sometimes with figures missing, and record them for both parties."),
        D("**Trade reductions** (reductions commerciales) lower the price itself. A **rabais** is given for a defect in quality or conformity; a **remise** for a large quantity or the buyer's status; a **ristourne** on the total of purchases over a period. A **financial discount** (escompte) is given for payment before the due date; it is a financial cost to the seller and a financial income to the buyer.",
          title="Definitions: trade reductions and financial discount"),
        KEY("The order of calculation on the invoice", "Each reduction is calculated on the amount left after the previous one.", cards=[
            ["1. Gross amount", "Quantity x unit price."],
            ["2. Trade reductions in cascade", "Rabais, then remise, then ristourne, each on the previous net figure. Result: the **net commercial amount**."],
            ["3. Escompte", "On the net commercial amount. Result: the **net financial amount**."],
            ["4. Transport (port)", "Added when the seller charges it."],
            ["5. VAT", "On the net financial amount plus transport, at the teaching rate of 19.25% (check the current Finance Law)."],
        ]),
        F(r"\text{Single equivalent rate} = 1 - (1 - r_1)(1 - r_2)", title="Successive reductions"),
        H("Worked examples"),
        EX("Worked example 1: complete the invoice", intro="Kamga Wholesale invoices 200 bags of rice at FCFA 20 000: rabais 5% (damaged packing), remise 10% (quantity), escompte 2% (payment at once), transport charged 60 000, VAT 19.25%.", steps=[
            S("Gross amount", math=r"200 \times 20\,000 = 4\,000\,000"),
            S("Rabais 5%", math=r"4\,000\,000 \times 5\% = 200\,000;\ \text{net } 3\,800\,000"),
            S("Remise 10% on 3 800 000, not on 4 000 000", math=r"3\,800\,000 \times 10\% = 380\,000;\ \text{net commercial } 3\,420\,000"),
            S("Escompte 2% on the net commercial amount", math=r"3\,420\,000 \times 2\% = 68\,400;\ \text{net financial } 3\,351\,600"),
            S("Add transport and charge VAT", math=r"(3\,351\,600 + 60\,000) \times 19.25\% = 656\,733"),
            S("Net to pay", math=r"3\,411\,600 + 656\,733 = 4\,068\,333"),
        ], check=r"4\,000\,000 \times (1 - 0.145) = 3\,420\,000"),
        CODE(_iv_tbl, "text", title="Invoice F75, Kamga Wholesale to Tabi Stores (FCFA, invented for practice)"),
        T("Check with the single equivalent rate: 1 - 0.95 x 0.90 = 0.145, so the two trade reductions together are 14.5%, not 15%. Successive reductions are never simply added."),
        EX("Worked example 2: record the invoice for both parties", intro="Journalise invoice F75 in the books of Kamga (seller) and Tabi Stores (buyer). Both use permanent inventory; the rice cost Kamga FCFA 13 500 a bag.", steps=[
            S("What is recorded", text="The rabais and remise on the invoice are **not** recorded: sales and purchases are recorded at the net commercial amount, 3 420 000. The escompte **is** recorded: 673 for the seller, 773 for the buyer."),
            S("Seller", text="Debit 411 with the net to pay and 673 with the escompte; credit 701 (net commercial), the transport income account and 443 (VAT)."),
            S("Buyer", text="Debit 601, transport on purchases and 4452; credit 401 with the net to pay and 773 with the escompte."),
            S("Permanent inventory", math=r"\text{Seller: } 200 \times 13\,500 = 2\,700\,000 \text{ out of stock};\ \text{buyer: } 3\,420\,000 + 60\,000 = 3\,480\,000 \text{ into stock}", text="The buyer's stock enters at purchase cost (price plus transport). Textbooks differ on whether the escompte is deducted from that cost; follow your teacher's method."),
        ]),
        CODE(_iv_seller, "text", title="Books of Kamga Wholesale (seller)"),
        CODE(_iv_buyer, "text", title="Books of Tabi Stores (buyer)"),
        T("Account numbers: 707 is the group of ancillary income where transport charged to customers is recorded, and 611 is transport on purchases. Some textbooks use different sub-accounts (for example 6015 for costs on purchases); check yours. The main accounts 401, 411, 443, 4452, 601, 673, 701 and 773 are standard."),
        EX("Worked example 3: a reduction after the invoice", intro="After delivery Tabi complains about quality and Kamga grants a further rabais of FCFA 100 000 net by credit note A12. Record it for both parties.", steps=[
            S("VAT on the credit note", math=r"100\,000 \times 19.25\% = 19\,250", text="A credit note reduces both the price and the VAT."),
            S("Seller", text="Debit 7019 reductions granted 100 000 and 443 VAT 19 250; credit 411 with 119 250."),
            S("Buyer", text="Debit 401 with 119 250; credit 6019 reductions obtained 100 000 and 4452 VAT 19 250."),
        ]),
        CODE(_cn_j, "text", title="Credit note A12 in both sets of books"),
        EX("Worked example 4: working backwards", intro="An invoice shows a net to pay of FCFA 2 039 175 including VAT at 19.25%. There were successive remises of 10% and 5%, no escompte and no transport. Find the gross amount.", steps=[
            S("Remove VAT", math=r"2\,039\,175 \div 1.1925 = 1\,710\,000", text="Divide; do not subtract 19.25% of the total."),
            S("Single equivalent factor", math=r"0.90 \times 0.95 = 0.855"),
            S("Gross amount", math=r"1\,710\,000 \div 0.855 = 2\,000\,000"),
        ]),
        MISTAKE("Calculating each reduction on the gross amount", "In example 1 the remise is 10% of 3 800 000 (380 000), not 10% of 4 000 000. Each reduction is on the previous net figure."),
        MISTAKE("Recording the rabais and remise shown on the invoice", "Reductions on the invoice itself are not entered; the sale and purchase are recorded at the net commercial amount. Only reductions granted later, by credit note, go to 7019 and 6019."),
        MISTAKE("Charging VAT before deducting the escompte", "VAT is charged on the net financial amount plus transport. Follow the order of the key idea above every time."),
        QUIZ("Successive trade reductions of 20% and 10% are equivalent to a single reduction of",
             ["30%", "28%", "72%", "2%"], 1,
             "1 - 0.80 x 0.90 = 1 - 0.72 = 0.28, so 28%.",
             hint="Multiply the factors that remain, (1 - 0.20)(1 - 0.10).",
             feedback=["Reductions in cascade are not added.", "", "72% is what remains, not the reduction.", "2% is the product of the rates, which has no meaning here."]),
        QUIZ("On a sales invoice, which item is recorded in the seller's books?",
             ["The remise for quantity", "The rabais for defects", "The escompte for prompt payment", "The gross amount before reductions"], 2,
             "The escompte is a financial expense of the seller (673). Trade reductions on the invoice are not recorded.",
             hint="Which reduction is financial rather than commercial?",
             feedback=["A remise on the invoice is not recorded.", "A rabais on the invoice is not recorded.", "", "Sales are recorded at the net commercial amount, not gross."]),
        PQ("Goods listed at FCFA 600 000 are invoiced with remises of 10% and 5%, escompte 2%, transport 49 260 and VAT at 19.25%. Calculate the net commercial amount, the net financial amount, the VAT and the net to pay.",
           "Net commercial: 600 000 x 0.90 x 0.95 = **513 000**. Escompte 2% = 10 260; net financial = **502 740**. VAT base = 502 740 + 49 260 = 552 000; VAT = 552 000 x 19.25% = **106 260**. Net to pay = 552 000 + 106 260 = **FCFA 658 260**."),
        PQ("Using the figures of the previous question, journalise the invoice in the books of the buyer.",
           "Dr 601 Purchases 513 000; Dr 611 Transport on purchases 49 260; Dr 4452 VAT on purchases 106 260; Cr 401 Suppliers 658 260; Cr 773 Discounts received 10 260. Check: debits 668 520 = credits 668 520."),
        PQ("Distinguish between a rabais, a remise, a ristourne and an escompte, and state which of them is recorded when it appears on the original invoice.",
           "Rabais: reduction for defective or non-conforming goods. Remise: reduction for quantity or the buyer's status. Ristourne: reduction on the total of purchases over a period. Escompte: financial discount for paying before the due date. On the original invoice only the **escompte** is recorded (673 seller, 773 buyer); the trade reductions simply lower the amount recorded."),
        TIP("Exam link: invoices appear in Paper 1 calculations and in Paper 3 Financial Accounting. In the Board's 2023 report, a Paper 3 question asked candidates to complete invoices and journalise them under permanent inventory; almost every candidate attempted it, with scores from zero to full marks. Set out the invoice line by line as in example 1 and label each figure."),
        SUM("Order: gross, rabais, remise, ristourne (cascade), net commercial, escompte, net financial, transport, VAT, net to pay.",
            "Successive reductions: single rate = 1 - (1 - r1)(1 - r2); never add the rates.",
            "Trade reductions on the invoice are not recorded; the escompte is (673 seller, 773 buyer).",
            "Later reductions use a credit note: 7019 for the seller, 6019 for the buyer, with the VAT reversed.",
            "Work backwards by dividing: by 1.1925 to remove VAT, by the remaining factors to remove reductions."),
    ],
))

# ------------------------------------------------------------------ 6. value added tax
_ch_sales = [("Producer", 0, 1000000), ("Wholesaler", 1000000, 1400000), ("Retailer", 1400000, 2000000)]
_ch_body = []
_ch_paid = 0
for _who, _buy, _sell in _ch_sales:
    _out, _in = vat(_sell), vat(_buy)
    _ch_paid += _out - _in
    _ch_body.append([_who, _buy, _sell, _out, _in, _out - _in])
assert _ch_paid == vat(2000000) == 385000
_ch_tbl = grid(["Stage", "Buys", "Sells", "Out VAT", "In VAT", "Pays"], [11, 10, 10, 9, 8, 8],
               _ch_body + [None, ["Total paid", "", "", "", "", _ch_paid]])

_mar = dict(sales=18400000, goods=9600000, transp=400000, serv=1200000, equip=6000000, cred=150000)
_v_out = vat(_mar["sales"])
_v_g, _v_t, _v_s, _v_e = vat(_mar["goods"]), vat(_mar["transp"]), vat(_mar["serv"]), vat(_mar["equip"])
_v_ded = _v_g + _v_t + _v_s + _v_e
_v_due = _v_out - _v_ded - _mar["cred"]
assert (_v_out, _v_g, _v_t, _v_s, _v_e) == (3542000, 1848000, 77000, 231000, 1155000)
assert (_v_ded, _v_due) == (3311000, 81000)
_v_decl = rows([
    ("VAT invoiced on sales (18 400 000)", _v_out),
    ("Less deductible VAT:", ""),
    ("  on goods bought (9 600 000)", -_v_g),
    ("  on transport (400 000)", -_v_t),
    ("  on services (1 200 000)", -_v_s),
    ("  on equipment (6 000 000)", -_v_e),
    ("Less credit brought forward", -_mar["cred"]),
    (None, None),
    ("VAT DUE for March", _v_due),
], w=36)
_v_j = journal([
    ("31 Mar  March VAT declaration", [("443", "VAT invoiced", _v_out, 0), ("4451", "VAT on fixed assets", 0, _v_e),
                                      ("4452", "VAT on purchases", 0, _v_g), ("4453", "VAT on transport", 0, _v_t),
                                      ("4454", "VAT on services", 0, _v_s), ("4449", "VAT credit to carry", 0, _mar["cred"]),
                                      ("4441", "State, VAT due", 0, _v_due)]),
    ("15 Apr  Payment of March VAT", [("4441", "State, VAT due", _v_due, 0), ("521", "Bank", 0, _v_due)]),
])
_apr_out, _apr_in = vat(12000000), vat(14000000)
_apr_cr = _apr_in - _apr_out
assert (_apr_out, _apr_in, _apr_cr) == (2310000, 2695000, 385000)
_apr_j = journal([("30 Apr  April VAT declaration (credit)", [("443", "VAT invoiced", _apr_out, 0), ("4449", "VAT credit to carry", _apr_cr, 0),
                                                              ("4452", "VAT on purchases", 0, _apr_in)])])
_car = 10000000
assert vat(_car) == 1925000 and _car + vat(_car) == 11925000
assert _Fr(175, 1000) * _Fr(11, 10) == VAT_RATE
# quiz and practice figures
assert vat(5600000) - vat(3200000) - 120000 == 342000
assert vat(4000000) - vat(4800000) == -154000

LESSONS.append(lesson(
    module=M2,
    topic="Value added tax",
    title="VAT: the mechanism, deductible VAT and the monthly declaration",
    slug="acl1-value-added-tax",
    minutes=25,
    summary="VAT is collected at every stage on the value added and borne by the final consumer. A business deducts the VAT it paid from the VAT it invoiced, declares the difference each month, pays it or carries a VAT credit forward, and records the declaration through accounts 443, 445, 4441 and 4449.",
    objectives=[
        "Explain the fractional mechanism of VAT and why the business is only a collector",
        "Distinguish VAT invoiced, deductible VAT, non-deductible VAT, VAT due and VAT credit",
        "Prepare a monthly VAT declaration and journalise it and its payment",
        "Evaluate VAT as a tax from the point of view of firms and consumers",
    ],
    key_concepts=["Value added tax (VAT, TVA)", "VAT invoiced (output VAT)", "Deductible VAT (input VAT)", "Non-deductible VAT", "VAT due", "VAT credit", "VAT declaration"],
    blocks=[
        H("Introduction"),
        T("When a family in Ebolowa buys a bag of cement, the price includes VAT. The cement factory, the wholesaler and the hardware shop have each paid part of that VAT to the State already. Nobody in the chain is taxed twice, and the family, the final consumer, bears the whole tax. This lesson shows how that happens and how a business accounts for it."),
        D("**Value added tax** (VAT, TVA in French) is an indirect tax on consumption, collected in fractions at each stage of production and distribution. Each registered business charges VAT on its sales and deducts the VAT it paid on its purchases, so it pays to the State only the VAT on the value it has added.",
          title="Definition: VAT"),
        T("In Cameroon textbooks use a general rate of **19.25%**: a VAT of 17.5% plus an additional council tax of 10% of that VAT (17.5% x 1.10 = 19.25%). Rates, exemptions and deadlines are set by the Finance Law and can change, so treat these as teaching values and check the current rules. In the examination, use the rate given in the question."),
        H("The fractional mechanism"),
        EX("Worked example 1: VAT along a chain", intro="A producer sells cement to a wholesaler for FCFA 1 000 000 before VAT; the wholesaler sells it to a retailer for 1 400 000; the retailer sells it to consumers for 2 000 000. Show the VAT each pays.", steps=[
            S("Producer", math=r"1\,000\,000 \times 19.25\% = 192\,500", text="No VAT on purchases in this simple example, so it pays 192 500."),
            S("Wholesaler", math=r"269\,500 - 192\,500 = 77\,000", text="VAT invoiced 1 400 000 x 19.25% = 269 500, less the 192 500 paid to the producer."),
            S("Retailer", math=r"385\,000 - 269\,500 = 115\,500"),
            S("Total received by the State", math=r"192\,500 + 77\,000 + 115\,500 = 385\,000 = 2\,000\,000 \times 19.25\%", text="Exactly the VAT paid by the consumers on the final price."),
        ]),
        CODE(_ch_tbl, "text", title="VAT paid at each stage (FCFA, invented for practice)"),
        H("Accounts and rules"),
        KEY("VAT accounts in the revised SYSCOHADA", "Main account 44 State; check sub-account numbers in your textbook.", cards=[
            ["443 VAT invoiced", "VAT charged on sales. Credit balance: owed to the State."],
            ["445 Deductible (recoverable) VAT", "VAT paid to suppliers: 4451 on fixed assets, 4452 on purchases, 4453 on transport, 4454 on services. Debit balance."],
            ["4441 State, VAT due", "The amount payable after the monthly declaration. Credit balance until paid."],
            ["4449 State, VAT credit to carry forward", "When deductible VAT is larger than VAT invoiced. Debit balance, used against next month's VAT."],
        ]),
        F(r"\text{VAT due} = \text{VAT invoiced} - \text{deductible VAT of the month} - \text{credit brought forward}", title="Monthly declaration"),
        KEY("Rules to apply (check the current tax code)", "These general rules are the ones textbooks use.", cards=[
            ["When VAT becomes chargeable", "For sales of goods, generally on delivery; for services, generally when the price is collected."],
            ["Conditions for deduction", "A proper invoice showing the VAT, and an expense used for taxable operations."],
            ["Non-deductible VAT", "The tax code excludes some items (for example certain passenger vehicles and some entertainment costs). Their VAT is part of the cost of the item."],
            ["Declaration", "Monthly, with payment by a fixed day of the following month (commonly the 15th); check the current deadline."],
        ]),
        EX("Worked example 2: the March declaration", intro="Ngono Distribution's March figures, before VAT: sales 18 400 000; goods bought 9 600 000; transport on purchases 400 000; maintenance services 1 200 000; new equipment 6 000 000. VAT credit brought forward from February: 150 000. Find the VAT due and journalise the declaration and its payment.", steps=[
            S("VAT invoiced", math=r"18\,400\,000 \times 19.25\% = 3\,542\,000"),
            S("Deductible VAT", math=r"1\,848\,000 + 77\,000 + 231\,000 + 1\,155\,000 = 3\,311\,000", text="Goods 9 600 000, transport 400 000, services 1 200 000 and equipment 6 000 000, each at 19.25%."),
            S("VAT due", math=r"3\,542\,000 - 3\,311\,000 - 150\,000 = 81\,000"),
            S("Entries", text="Debit 443 to cancel the VAT invoiced; credit each 445 account and 4449 to cancel them; credit 4441 with the balance. On payment, debit 4441 and credit the bank."),
        ]),
        CODE(_v_decl, "text", title="VAT declaration for March (FCFA)"),
        CODE(_v_j, "text", title="Journal entries"),
        EX("Worked example 3: a VAT credit", intro="In April the business invoiced sales of 12 000 000 and bought goods for 14 000 000 (before VAT) to build up stock. Record the declaration.", steps=[
            S("Compare", math=r"\text{invoiced } 2\,310\,000 < \text{deductible } 2\,695\,000", text="The State owes the business the difference."),
            S("Credit", math=r"2\,695\,000 - 2\,310\,000 = 385\,000", text="Debit 4449 with 385 000; it reduces May's VAT due. Nothing is paid in April."),
        ]),
        CODE(_apr_j, "text", title="April declaration"),
        EX("Worked example 4: non-deductible VAT", intro="A company buys a passenger car for its director for 10 000 000 before VAT. Assume the tax code makes VAT on this vehicle non-deductible. At what cost is the car recorded?", steps=[
            S("VAT", math=r"10\,000\,000 \times 19.25\% = 1\,925\,000"),
            S("Cost", math=r"10\,000\,000 + 1\,925\,000 = 11\,925\,000", text="Non-deductible VAT is part of the cost: debit 245 with 11 925 000 and credit 481 with the same amount. No entry in 4451."),
        ]),
        H("Evaluation"),
        T("For firms, VAT is in principle **neutral**: it is collected and paid over, not an expense. In practice it costs them time and cash: a firm that buys heavily or exports can carry VAT credits for months, which ties up its money. For consumers, VAT is easy to collect and hard to evade along the chain, but it is **regressive**: poorer households spend a larger share of their income on taxed goods. Exemptions of basic foodstuffs, where they exist, reduce this effect; check the current list."),
        MISTAKE("Treating deductible VAT as an expense", "VAT on purchases (445) is a claim on the State, not part of cost, unless the tax code makes it non-deductible."),
        MISTAKE("Forgetting the credit brought forward", "Last month's VAT credit (4449) reduces this month's VAT due. Leave it out and the business overpays."),
        MISTAKE("Paying VAT on the VAT credit month", "When deductible VAT exceeds VAT invoiced, there is no payment; the difference is carried forward in 4449."),
        QUIZ("In May: VAT invoiced 1 078 000; deductible VAT 616 000; credit brought forward 120 000. VAT due is",
             ["FCFA 462 000", "FCFA 342 000", "FCFA 582 000", "FCFA 1 694 000"], 1,
             "1 078 000 - 616 000 - 120 000 = 342 000.",
             hint="Start from the VAT invoiced and remove everything deductible, including last month's credit.",
             feedback=["You forgot the credit brought forward.", "", "You added the credit instead of deducting it.", "You added VAT invoiced and deductible VAT."]),
        QUIZ("When deductible VAT for a month is larger than VAT invoiced, the business",
             ["pays the difference to the State", "records a VAT credit in 4449 and uses it next month", "records the difference as an expense", "cancels its purchases"], 1,
             "The State owes the business; the credit is carried forward against future VAT due.",
             hint="Who owes whom when more VAT was paid than collected?",
             feedback=["Nothing is payable when the State owes the business.", "", "The difference is a claim, not an expense.", "Purchases are unaffected."]),
        PQ("Explain, with a numerical example, why VAT is said to be borne by the final consumer and not by businesses.",
           "Each business deducts the VAT it paid from the VAT it charged, so it pays only VAT on its own value added. Example: producer sells at 1 000 000 (VAT 192 500), wholesaler at 1 400 000 (pays 269 500 - 192 500 = 77 000), retailer at 2 000 000 (pays 385 000 - 269 500 = 115 500). The State receives 385 000 in total, exactly the VAT paid by consumers on 2 000 000. The businesses have collected it and passed it on."),
        PQ("In June a trader's sales before VAT are FCFA 5 600 000 and purchases before VAT are 3 200 000. There is a VAT credit of 120 000 from May. Using 19.25%, find the VAT due and give the journal entry for the declaration.",
           "VAT invoiced = 5 600 000 x 19.25% = 1 078 000. Deductible = 3 200 000 x 19.25% = 616 000. VAT due = 1 078 000 - 616 000 - 120 000 = **342 000**. Entry: Dr 443 VAT invoiced 1 078 000; Cr 4452 VAT on purchases 616 000; Cr 4449 VAT credit 120 000; Cr 4441 State, VAT due 342 000."),
        PQ("Discuss two advantages and two disadvantages of VAT as a source of government revenue.",
           "Plan. Advantages: (1) broad base and steady yield, since everyone consumes; (2) collected in stages, so evasion at one stage is partly caught at the next, and businesses act as unpaid collectors. Disadvantages: (1) regressive, taking a larger share of poor households' income; (2) compliance costs and VAT credits that tie up firms' cash, especially exporters. Judgement: an efficient tax if exemptions or reduced rates protect basic goods and refunds of credits are paid promptly."),
        TIP("Exam link: VAT calculations and entries appear in Paper 1 and inside Paper 3 questions on trading operations; VAT also appears in the cash budget in the Upper Sixth (Paper 2). Lay out the declaration as in example 2 and name each 44 account."),
        SUM("VAT is collected at each stage on value added; the final consumer bears it.",
            "Teaching rate 19.25% = 17.5% plus 10% council tax on the VAT; check the current Finance Law.",
            "VAT due = VAT invoiced - deductible VAT - credit brought forward; a negative result is a credit (4449).",
            "Declaration entry: Dr 443; Cr 445 accounts and 4449; Cr 4441 VAT due. Payment: Dr 4441, Cr bank.",
            "Non-deductible VAT is added to the cost of the item."),
    ],
))

# ------------------------------------------------------------------ 7. packaging and containers
_pk_n, _pk_dep, _pk_ret, _pk_rep = 50, 3000, 40, 2400
_pk_total = _pk_n * _pk_dep
_pk_retv = _pk_ret * _pk_dep
_pk_refund = _pk_ret * _pk_rep
_pk_boni = _pk_retv - _pk_refund
_pk_kept = (_pk_n - _pk_ret) * _pk_dep
_pk_kvat = vat(_pk_kept)
assert (_pk_total, _pk_retv, _pk_refund, _pk_boni, _pk_kept, _pk_kvat) == (150000, 120000, 96000, 24000, 30000, 5775)
assert _pk_total - _pk_retv - _pk_kept == 0
_pk_cust = _pk_total - _pk_refund + _pk_kvat
assert _pk_cust == 59775 == _pk_kept + _pk_kvat + _pk_boni

_pk_seller = journal([
    ("2 May  Deposit on 50 crates", [("411", "Customers", _pk_total, 0), ("4194", "Customers, deposits", 0, _pk_total)]),
    ("30 May 40 crates back at 2 400", [("4194", "Customers, deposits", _pk_retv, 0), ("411", "Customers", 0, _pk_refund), ("70x", "Boni on packaging", 0, _pk_boni)]),
    ("30 May 10 crates kept", [("4194", "Customers, deposits", _pk_kept, 0), ("411", "Customers", _pk_kvat, 0), ("70x", "Sale of packaging", 0, _pk_kept), ("443", "VAT invoiced", 0, _pk_kvat)]),
])
_pk_buyer = journal([
    ("2 May  Deposit on 50 crates", [("4094", "Suppliers, packaging", _pk_total, 0), ("401", "Suppliers", 0, _pk_total)]),
    ("30 May 40 crates returned", [("401", "Suppliers", _pk_refund, 0), ("608", "Packaging (mali)", _pk_boni, 0), ("4094", "Suppliers, packaging", 0, _pk_retv)]),
    ("30 May 10 crates kept", [("608", "Purchases of packaging", _pk_kept, 0), ("4452", "VAT on purchases", _pk_kvat, 0), ("4094", "Suppliers, packaging", 0, _pk_kept), ("401", "Suppliers", 0, _pk_kvat)]),
])
_pk_4194 = rows([("Deposit on 50 crates (credit)", _pk_total), ("Less 40 returned (debit)", -_pk_retv),
                 ("Less 10 kept (debit)", -_pk_kept), (None, None), ("Balance of 4194", 0)], w=32)
# practice figures
assert 80 * 2500 == 200000 and 60 * (2500 - 2000) == 30000 and 60 * 2000 == 120000 and vat(20 * 2500) == 9625

LESSONS.append(lesson(
    module=M2,
    topic="Packaging and containers",
    title="Packaging: lost packaging, returnable containers, deposits, boni and mali",
    slug="acl1-packaging-and-containers",
    minutes=24,
    summary="Lost packaging is part of the price; returnable containers are lent against a deposit recorded in 4194 (seller) and 4094 (buyer). When containers come back at a lower price the seller makes a boni and the buyer a mali; containers kept are treated as sold, with VAT.",
    objectives=[
        "Distinguish lost (non-returnable) packaging from returnable containers lent against a deposit",
        "Record the deposit, the return and the non-return of containers in the books of the seller and the buyer",
        "Calculate the boni (seller's gain) and the mali (buyer's loss) when containers are taken back below the deposit price",
        "Explain the VAT treatment of deposits and of containers kept",
    ],
    key_concepts=["Lost packaging", "Returnable container", "Deposit (consignation)", "Return price (prix de reprise)", "Boni", "Mali", "4194 and 4094"],
    blocks=[
        H("Introduction"),
        T("A drinks distributor in Douala delivers 50 crates of soft drinks to a bar in Akwa. The drinks are sold; the crates and bottles are only lent and must come back. The bar pays a deposit so that it has a reason to return them. If some are lost, broken or kept, the deposit pays for them."),
        D("**Packaging** (emballages) is the material that holds goods during transport and sale. **Lost packaging** (emballages perdus) goes to the customer with the goods and is part of the selling price. **Returnable containers** (emballages consignes), such as crates, gas bottles or drums, are lent to the customer against a **deposit** (consignation) that is refunded when they come back.",
          title="Definition: lost packaging and returnable containers"),
        KEY("How each type is treated", "Decide first whether the packaging comes back.", cards=[
            ["Lost packaging", "Bought by the seller as packaging (608 purchases of packaging, or a packaging stock in class 3). When sold with the goods it is part of the price and of the VAT base."],
            ["Returnable containers, seller", "The deposit is a debt to the customer: credit **4194** Customers, debts for packaging consigned. It is not a sale and, at invoicing, is outside the VAT base."],
            ["Returnable containers, buyer", "The deposit is a claim on the supplier: debit **4094** Suppliers, receivables for packaging to return."],
            ["Containers owned for long use", "Crates a firm owns and uses for several years may be fixed assets; cheaper ones are kept in stock. Check your textbook's rule."],
        ]),
        H("Return below the deposit price: boni and mali"),
        D("Containers are often taken back at a **return price** (prix de reprise) lower than the deposit, because of wear. The difference is a **boni** (gain) for the seller, who refunds less than it received, and a **mali** (loss) for the buyer, who gets back less than it paid.",
          title="Definition: boni and mali",
          formula=r"\text{Boni} = \text{number returned} \times (\text{deposit price} - \text{return price})"),
        T("Containers **not returned** by the deadline are treated as sold to the customer at the deposit price. VAT then becomes due on them. In this course we treat the deposit price as a price before VAT and invoice VAT on it; some textbooks treat it differently, and the VAT treatment of the boni also varies, so follow your teacher's method."),
        H("Worked examples"),
        EX("Worked example 1: the seller's books", intro="On 2 May a distributor delivers drinks with 50 crates consigned at FCFA 3 000 each. On 30 May the bar returns 40 crates, taken back at 2 400 each, and keeps the other 10. VAT 19.25% on crates kept. Record the packaging entries in the seller's books.", steps=[
            S("Deposit", math=r"50 \times 3\,000 = 150\,000", text="Dr 411, Cr 4194. The drinks themselves are invoiced separately with VAT, as usual."),
            S("Return of 40 crates", math=r"40 \times 3\,000 = 120\,000;\ 40 \times 2\,400 = 96\,000", text="Cancel the deposit on the 40 crates (Dr 4194 120 000); credit the customer only with the return value (Cr 411 96 000)."),
            S("Boni", math=r"40 \times (3\,000 - 2\,400) = 24\,000", text="Credited to an income account of class 70 (the sub-account varies by textbook)."),
            S("10 crates kept", math=r"10 \times 3\,000 = 30\,000;\ \text{VAT } 30\,000 \times 19.25\% = 5\,775", text="Dr 4194 30 000 and Cr sale of packaging 30 000; Dr 411 and Cr 443 with the VAT."),
            S("Check 4194", math=r"150\,000 - 120\,000 - 30\,000 = 0", text="Every crate is accounted for, so the deposit account is cleared."),
        ]),
        CODE(_pk_seller, "text", title="Seller's books: packaging entries (FCFA, invented for practice; 70x = income sub-account to check)"),
        CODE(_pk_4194, "text", title="Account 4194 in the seller's books"),
        EX("Worked example 2: the buyer's books", intro="Record the same events in the books of the bar.", steps=[
            S("Deposit", text="Dr 4094 150 000, Cr 401 150 000: the bar has a claim for the crates."),
            S("Return", text="Cancel the claim on 40 crates (Cr 4094 120 000); the supplier owes only 96 000 (Dr 401 96 000); the mali of 24 000 is an expense (debited to a packaging expense account such as 608)."),
            S("Crates kept", text="They become the bar's own packaging: Dr 608 30 000, Dr 4452 VAT 5 775; Cr 4094 30 000 and Cr 401 5 775."),
            S("Net cost to the bar", math=r"24\,000 + 30\,000 + 5\,775 = 59\,775", text="Equal to what the seller gained or sold: the two sets of books mirror each other."),
        ]),
        CODE(_pk_buyer, "text", title="Buyer's books: packaging entries"),
        EX("Worked example 3: what the customer finally pays for packaging", intro="How much does the bar owe the distributor for packaging after 30 May?", steps=[
            S("Deposit charged less refund", math=r"150\,000 - 96\,000 = 54\,000"),
            S("Add VAT on crates kept", math=r"54\,000 + 5\,775 = 59\,775", text="This is the net effect of the packaging entries on 411."),
        ]),
        MISTAKE("Recording the deposit as a sale", "A deposit is a debt to the customer (4194), refundable when containers come back. It is not income and, at invoicing, carries no VAT."),
        MISTAKE("Refunding at the deposit price when the question gives a lower return price", "The refund is at the return price; the difference is the boni (seller) or mali (buyer)."),
        MISTAKE("Leaving 4194 with a balance after all containers are settled", "Every container is either returned or kept. Cancel the deposit on both groups, and the account balances to zero for that delivery."),
        QUIZ("A seller consigned 60 crates at FCFA 2 500 and takes back 60 crates at FCFA 2 000. Its boni is",
             ["FCFA 120 000", "FCFA 30 000", "FCFA 150 000", "FCFA 500"], 1,
             "60 x (2 500 - 2 000) = 30 000.",
             hint="Boni per crate times the number returned.",
             feedback=["That is the refund at the return price.", "", "That is the full deposit.", "That is the boni on one crate only."]),
        QUIZ("In the buyer's books, the deposit paid on returnable containers is debited to",
             ["608 Purchases of packaging", "4094 Suppliers, receivables for packaging to return", "4194 Customers, debts for packaging", "601 Purchases of goods"], 1,
             "The buyer has a claim on the supplier for the containers: 4094.",
             hint="Is the deposit an expense or something the buyer expects to get back?",
             feedback=["608 is used only for packaging the buyer keeps or for the mali.", "", "4194 is used by the seller, not the buyer.", "The deposit is not goods for resale."]),
        PQ("A gas distributor delivers 80 gas bottles consigned at FCFA 2 500 each. Later 60 are returned at a return price of 2 000 each and 20 are kept. VAT 19.25% is charged on bottles kept. Journalise the packaging entries in the distributor's books.",
           "Deposit: Dr 411 200 000; Cr 4194 200 000 (80 x 2 500). Return: Dr 4194 150 000 (60 x 2 500); Cr 411 120 000 (60 x 2 000); Cr boni (income, class 70) 30 000. Kept: Dr 4194 50 000; Cr sale of packaging 50 000; Dr 411 9 625; Cr 443 9 625 (50 000 x 19.25%). Check 4194: 200 000 - 150 000 - 50 000 = 0."),
        PQ("Distinguish between lost packaging and returnable containers, and explain why a deposit is not treated as a sale.",
           "Lost packaging is sold with the goods and is part of the price and the VAT base. Returnable containers are lent to the customer and must come back. The deposit is money the seller must refund when they return, so it is a **debt** to the customer (4194), not income; only containers that are not returned become a sale."),
        PQ("Explain why the boni of the seller equals the mali of the buyer for the same return.",
           "Both are the difference between the deposit and the return price on the containers returned. The seller keeps that difference (a gain) and the buyer loses it (an expense). The two sets of books record the same transaction from opposite sides, so the amounts are equal."),
        TIP("Exam link: packaging often appears inside a Paper 3 trading-operations question, together with invoices and VAT, and in Paper 1 calculations of boni and refunds. Show the deposit, return and kept containers as three separate lines."),
        SUM("Lost packaging is part of the price; returnable containers are lent against a deposit.",
            "Seller credits 4194 with the deposit; buyer debits 4094.",
            "Return at a lower price: seller's boni, buyer's mali, equal to number returned x (deposit - return price).",
            "Containers kept are treated as sold at the deposit price, and VAT becomes due (methods vary; follow your teacher).",
            "After all containers are settled, 4194 and 4094 balance to zero for that delivery."),
    ],
))

# ------------------------------------------------------------------ 8. bills of exchange
import datetime as _dt

_bx_v = 2400000
_bx_days = (_dt.date(2025, 6, 30) - _dt.date(2025, 4, 16)).days
assert _bx_days == 75 == 14 + 31 + 30
_bx_esc = _Fr(_bx_v * 9 * _bx_days, 36000)
assert _bx_esc == 45000
_bx_esc = int(_bx_esc)
_bx_com = 4000
_bx_cvat = vat(_bx_com)
_bx_agio = _bx_esc + _bx_com + _bx_cvat
_bx_net = _bx_v - _bx_agio
assert (_bx_cvat, _bx_agio, _bx_net) == (770, 49770, 2350230)
_bx_agio_tbl = rows([
    ("Nominal value of the bill", _bx_v),
    ("Discount 2 400 000 x 9% x 75/360", -_bx_esc),
    ("Bank commission", -_bx_com),
    ("VAT on commission (19.25%)", -_bx_cvat),
    (None, None),
    ("Net proceeds credited to bank", _bx_net),
], w=36)

_bx_j = journal([
    ("1 Apr   Bill accepted by Fotso", [("412", "Customers, bills", _bx_v, 0), ("411", "Customers", 0, _bx_v)]),
    ("16 Apr  Bill discounted", [("521", "Bank", _bx_net, 0), ("675", "Discount on bills", _bx_esc, 0), ("631", "Bank charges", _bx_com, 0),
                                 ("4454", "VAT on services", _bx_cvat, 0), ("412", "Customers, bills", 0, _bx_v)]),
])
_bx_drawee = journal([
    ("1 Apr   Bill accepted (drawee)", [("401", "Suppliers", _bx_v, 0), ("402", "Suppliers, bills", 0, _bx_v)]),
    ("30 Jun  Bill paid at maturity", [("402", "Suppliers, bills", _bx_v, 0), ("521", "Bank", 0, _bx_v)]),
])
_rn_v, _rn_days = 1200000, 60
_rn_int = _Fr(_rn_v * 12 * _rn_days, 36000)
assert _rn_int == 24000
_rn_int = int(_rn_int)
_rn_new = _rn_v + _rn_int
assert _rn_new == 1224000
_rn_j = journal([
    ("Old bill cancelled", [("411", "Customers", _rn_v, 0), ("412", "Customers, bills", 0, _rn_v)]),
    ("Interest charged to the customer", [("411", "Customers", _rn_int, 0), ("77", "Financial income", 0, _rn_int)]),
    ("New bill accepted", [("412", "Customers, bills", _rn_new, 0), ("411", "Customers", 0, _rn_new)]),
])
_dh_fee = 5000
_dh_j = journal([("Discounted bill unpaid: bank debits us", [("411", "Customers", _bx_v + _dh_fee, 0), ("521", "Bank", 0, _bx_v + _dh_fee)])])
assert _bx_v + _dh_fee == 2405000
# quiz and practice figures
assert (_dt.date(2025, 9, 15) - _dt.date(2025, 7, 22)).days == 55
assert int(900000 * 8 * 40 / 36500) == 7890
assert _Fr(1800000 * 10 * 55, 36000) == 27500
assert 1800000 - 27500 - 2000 - vat(2000) == 1770115
assert _Fr(900000 * 8 * 40, 36000) == 8000

LESSONS.append(lesson(
    module=M2,
    topic="Bills of exchange",
    title="Bills of exchange: acceptance, discounting, endorsement, dishonour and renewal",
    slug="acl1-bills-of-exchange",
    minutes=26,
    summary="A bill of exchange is an order by the drawer to the drawee to pay a sum on a fixed date. The holder may keep it to maturity, endorse it to a supplier or discount it at a bank, which deducts interest and commissions. Dishonoured bills go back to the customer; renewed bills include interest.",
    objectives=[
        "Identify the parties to a bill of exchange and a promissory note and the stages in the life of a bill",
        "Calculate the discount (agio) and the net proceeds when a bill is discounted",
        "Journalise acceptance, discounting, endorsement, collection, dishonour and renewal for the drawer and the drawee",
        "Explain the advantages and risks of bills for traders",
    ],
    key_concepts=["Bill of exchange (lettre de change, traite)", "Promissory note (billet a ordre)", "Drawer", "Drawee", "Payee", "Acceptance", "Endorsement", "Discounting", "Agio", "Dishonour", "Renewal"],
    blocks=[
        H("Introduction"),
        T("A building-materials wholesaler in Douala sells to a contractor in Bafoussam who will pay in three months. The wholesaler needs cash now to restock. If the contractor signs a bill of exchange, the wholesaler can take the bill to its bank and receive most of the money immediately. Bills turn a simple debt into a document that can be transferred and sold."),
        D("A **bill of exchange** (lettre de change or traite) is a written order by which one person, the **drawer** (tireur, usually the seller), orders another, the **drawee** (tire, the buyer), to pay a stated sum on a stated date (the **maturity**) to a third person, the **payee** (beneficiaire), or to the drawer. The drawee signs it to show **acceptance**. A **promissory note** (billet a ordre) is written by the debtor himself, promising to pay.",
          title="Definition: bill of exchange and promissory note"),
        IMG("alacl1-bill-of-exchange.svg", alt="Diagram: the drawer (seller) sells goods on credit to the drawee (buyer), sends the bill for acceptance and receives it back accepted; the drawer then discounts or endorses it, and the holder at maturity, a bank or supplier, presents it to the drawee, who pays.",
            caption="Figure 1. The life of a bill of exchange."),
        KEY("What the holder can do with an accepted bill", "Four choices, each with its own entry.", cards=[
            ["Keep it to maturity", "Send it to the bank for collection a few days before the due date; the bank collects and charges a fee."],
            ["Endorse it", "Sign it over to one of its own suppliers to settle a debt (Dr 401, Cr 412)."],
            ["Discount it", "Sell it to the bank before maturity; the bank pays the nominal value less the agio."],
            ["Accounts used (check sub-accounts)", "Drawer: 412 Customers, bills receivable. Drawee: 402 Suppliers, bills payable. Discount: 675; bank charges: 631; values sent for collection: main account 51."],
        ]),
        H("Discounting: the agio"),
        F(r"\text{Discount} = \frac{V \times t \times n}{36\,000}", title="Commercial discount (V value, t annual rate in %, n days, 360-day year)"),
        T("The **agio** is everything the bank deducts: the discount (interest), commissions and the VAT on commissions. The **number of days** runs from the day after the discount date to the maturity date inclusive; some banks add one or more bank days or charge a minimum, so check your textbook."),
        EX("Worked example 1: the net proceeds", intro="On 1 April Fotso accepts a bill for FCFA 2 400 000 due on 30 June, drawn by Ngono Distribution. On 16 April Ngono discounts it at 9% a year. Commission 4 000 plus VAT at 19.25%. Find the net proceeds.", steps=[
            S("Days", math=r"14 \text{ (17 to 30 April)} + 31 \text{ (May)} + 30 \text{ (June)} = 75"),
            S("Discount", math=r"\frac{2\,400\,000 \times 9 \times 75}{36\,000} = 45\,000"),
            S("Commission and VAT", math=r"4\,000 + 4\,000 \times 19.25\% = 4\,000 + 770 = 4\,770"),
            S("Net proceeds", math=r"2\,400\,000 - 45\,000 - 4\,770 = 2\,350\,230"),
        ]),
        CODE(_bx_agio_tbl, "text", title="Discount note from the bank (FCFA, invented for practice)"),
        EX("Worked example 2: entries for the drawer and the drawee", intro="Journalise the acceptance and the discount in Ngono's books, and the acceptance and payment in Fotso's books.", steps=[
            S("Drawer, acceptance", text="The ordinary debt becomes a bill: Dr 412, Cr 411."),
            S("Drawer, discount", text="Dr bank with the net proceeds, Dr 675 with the discount, Dr 631 with the commission, Dr 4454 with its VAT; Cr 412 with the nominal value. Some textbooks keep the bill in 412 until maturity and credit a bank-credit account (56) instead, because Ngono remains liable if Fotso does not pay; follow your teacher."),
            S("Drawee", text="On acceptance Dr 401, Cr 402. At maturity Dr 402, Cr bank."),
        ]),
        CODE(_bx_j, "text", title="Books of Ngono Distribution (drawer)"),
        CODE(_bx_drawee, "text", title="Books of Fotso (drawee)"),
        H("Dishonour and renewal"),
        EX("Worked example 3: a discounted bill is dishonoured", intro="Suppose Fotso does not pay on 30 June. The bank debits Ngono's account with the bill plus FCFA 5 000 of fees.", steps=[
            S("Who bears the loss", text="The drawer guaranteed the bill, so the bank recovers from Ngono."),
            S("Entry", math=r"2\,400\,000 + 5\,000 = 2\,405\,000", text="Dr 411 Customers (Fotso again owes, plus the fees), Cr 521 Bank. If Ngono still held the bill, it would simply debit 411 and credit 412."),
        ]),
        CODE(_dh_j, "text", title="Dishonoured discounted bill (drawer)"),
        EX("Worked example 4: renewal with interest", intro="A customer cannot pay a bill of FCFA 1 200 000 due 31 May and asks for 60 more days. The drawer agrees to replace it with a new bill including interest at 12% a year.", steps=[
            S("Interest", math=r"\frac{1\,200\,000 \times 12 \times 60}{36\,000} = 24\,000"),
            S("New bill", math=r"1\,200\,000 + 24\,000 = 1\,224\,000"),
            S("Entries", text="Cancel the old bill (Dr 411, Cr 412); charge the interest (Dr 411, Cr 77 financial income); record the new bill (Dr 412, Cr 411)."),
        ]),
        CODE(_rn_j, "text", title="Renewal in the drawer's books"),
        T("**Evaluation.** Bills give the seller a legal document that is easy to enforce, can be discounted for immediate cash and can settle its own debts by endorsement. The costs are the agio and the risk that remains: if the drawee defaults, the drawer must repay the bank. For the buyer, a bill gives time to pay but a dishonoured bill damages its credit standing."),
        MISTAKE("Counting the day of discount", "Count from the day after the discount date to the maturity date inclusive: 16 April to 30 June is 75 days, not 76."),
        MISTAKE("Using a 365-day year", "Commercial discount uses a 360-day year: divide by 36 000 when the rate is in percent."),
        MISTAKE("Forgetting the VAT on the commission", "The agio includes VAT on bank commissions (the discount interest itself carries none in our examples). Leave it out and the net proceeds are wrong."),
        QUIZ("A bill of FCFA 900 000 is discounted 40 days before maturity at 8% a year (360-day year). The discount is",
             ["FCFA 72 000", "FCFA 8 000", "FCFA 7 890", "FCFA 800"], 1,
             "900 000 x 8 x 40 / 36 000 = 8 000.",
             hint="Use V x t x n / 36 000.",
             feedback=["That is a full year's interest.", "", "That uses a 365-day year.", "You divided by 360 000."]),
        QUIZ("In the drawee's books, accepting a bill drawn by a supplier is recorded as",
             ["Dr 412, Cr 411", "Dr 401, Cr 402", "Dr 402, Cr 401", "Dr 401, Cr 521"], 1,
             "The ordinary supplier debt becomes a bill payable.",
             hint="The drawee owes money: which two supplier accounts are involved?",
             feedback=["412 and 411 are the drawer's accounts.", "", "This reverses the entry.", "Nothing is paid at acceptance."]),
        PQ("A bill of FCFA 1 800 000 due on 15 September is discounted on 22 July at 10% a year. Commission 2 000 plus VAT 19.25%. Calculate the net proceeds and journalise the discount in the drawer's books.",
           "Days: 9 (23 to 31 July) + 31 (August) + 15 (September) = 55. Discount = 1 800 000 x 10 x 55 / 36 000 = 27 500. VAT on commission = 2 000 x 19.25% = 385. Net = 1 800 000 - 27 500 - 2 000 - 385 = **FCFA 1 770 115**. Entry: Dr 521 Bank 1 770 115; Dr 675 Discount on bills 27 500; Dr 631 Bank charges 2 000; Dr 4454 VAT 385; Cr 412 Customers, bills 1 800 000."),
        PQ("Explain three ways in which the holder of an accepted bill can use it before or at maturity.",
           "(1) **Keep it** and send it to the bank for collection at maturity. (2) **Endorse** it to a supplier to settle a debt. (3) **Discount** it at a bank to receive cash at once, less the agio. In cases 2 and 3 the drawer still guarantees payment if the drawee defaults."),
        PQ("Evaluate the use of bills of exchange by a wholesaler that sells on credit to small retailers.",
           "Plan. For: a written, accepted debt is easier to enforce; it can be discounted for immediate cash or endorsed to suppliers, which helps working capital. Against: discounting costs interest and commissions; the wholesaler remains liable on discounted bills if retailers default; renewals and dishonours add costs and admin. Judgement: useful for reliable customers and when cash is short, but the wholesaler must still assess customers' credit carefully."),
        TIP("Exam link: discount calculations (days, agio, net proceeds) are typical Paper 1 items; journal entries for bills appear in Paper 3 trading-operations questions. Show the day count line by line."),
        SUM("A bill is an order by the drawer to the drawee to pay on a fixed date; the drawee accepts it.",
            "Drawer: Dr 412, Cr 411 on acceptance. Drawee: Dr 401, Cr 402.",
            "Discount = V x t x n / 36 000; agio = discount + commissions + VAT on commissions.",
            "Discounted bill: Dr bank (net), 675, 631, 4454; Cr 412 (some textbooks use a bank-credit account until maturity).",
            "Dishonour sends the debt back to 411 with fees; renewal replaces the bill with a new one including interest."),
    ],
))

# ------------------------------------------------------------------ 9. foreign currency transactions
_fx_usd, _fx_r0, _fx_r1, _fx_r2 = 20000, 600, 615, 610
_fx_h = _fx_usd * _fx_r0
_fx_c = _fx_usd * _fx_r1
_fx_p = _fx_usd * _fx_r2
_fx_ul = _fx_c - _fx_h
_fx_rl = _fx_p - _fx_h
assert (_fx_h, _fx_c, _fx_p, _fx_ul, _fx_rl) == (12000000, 12300000, 12200000, 300000, 200000)
assert -_fx_ul + (_fx_ul - _fx_rl) == -_fx_rl  # N: -300 000; N+1: +100 000; total = actual loss

_fx_j1 = journal([
    ("10 Nov N  Import invoice, 20 000 USD at 600", [("601", "Purchases of goods", _fx_h, 0), ("401", "Suppliers", 0, _fx_h)]),
    ("31 Dec N  Debt restated at 615", [("478", "Conversion diff. (asset)", _fx_ul, 0), ("401", "Suppliers", 0, _fx_ul)]),
    ("31 Dec N  Provision for exchange loss", [("697", "Financial provision chg", _fx_ul, 0), ("194", "Provision exch. losses", 0, _fx_ul)]),
])
_fx_j2 = journal([
    ("1 Jan N+1  Reversal of restatement", [("401", "Suppliers", _fx_ul, 0), ("478", "Conversion diff. (asset)", 0, _fx_ul)]),
    ("15 Feb N+1 Payment at 610", [("401", "Suppliers", _fx_h, 0), ("676", "Exchange losses", _fx_rl, 0), ("521", "Bank", 0, _fx_p)]),
    ("15 Feb N+1 Provision no longer needed", [("194", "Provision exch. losses", _fx_ul, 0), ("797", "Financial reversals", 0, _fx_ul)]),
])

_fg_gbp, _fg_r0, _fg_r1, _fg_r2 = 10000, 760, 780, 775
_fg_h, _fg_c, _fg_p = _fg_gbp * _fg_r0, _fg_gbp * _fg_r1, _fg_gbp * _fg_r2
_fg_ug, _fg_rg = _fg_c - _fg_h, _fg_p - _fg_h
assert (_fg_h, _fg_c, _fg_p, _fg_ug, _fg_rg) == (7600000, 7800000, 7750000, 200000, 150000)
_fg_j = journal([
    ("1 Dec N   Export sale, 10 000 GBP at 760", [("411", "Customers", _fg_h, 0), ("701", "Sales of goods", 0, _fg_h)]),
    ("31 Dec N  Receivable restated at 780", [("411", "Customers", _fg_ug, 0), ("479", "Conversion diff. (liab.)", 0, _fg_ug)]),
    ("1 Jan N+1 Reversal of restatement", [("479", "Conversion diff. (liab.)", _fg_ug, 0), ("411", "Customers", 0, _fg_ug)]),
    ("20 Jan N+1 Received at 775", [("521", "Bank", _fg_p, 0), ("411", "Customers", 0, _fg_h), ("776", "Exchange gains", 0, _fg_rg)]),
])
# practice figures
assert 5000 * 590 == 2950000 and 5000 * (610 - 590) == 100000 and 5000 * (580 - 590) == -50000

LESSONS.append(lesson(
    module=M2,
    topic="Foreign currency transactions",
    title="Foreign currency transactions: spot rates, conversion differences and exchange gains and losses",
    slug="acl1-foreign-currency-transactions",
    minutes=26,
    summary="Foreign currency items are recorded at the rate of the day and restated at the closing rate: unrealised losses go to 478 with a provision, unrealised gains go to 479 and are not income. Settlement gives realised gains (776) or losses (676).",
    objectives=[
        "Record a purchase or sale in a foreign currency at the rate on the transaction date",
        "Restate unsettled foreign currency items at the closing rate using 478 and 479",
        "Apply prudence: provide for unrealised losses and leave unrealised gains out of the result",
        "Record settlement and the realised exchange gain or loss, and explain why euro transactions give none",
    ],
    key_concepts=["Spot rate", "Closing rate", "Conversion difference (ecart de conversion)", "478 Conversion difference, asset", "479 Conversion difference, liability", "Provision for exchange loss", "Realised exchange gain or loss", "Fixed parity FCFA-euro"],
    blocks=[
        H("Introduction"),
        T("A Douala importer buys spare parts from the United States, payable in dollars in three months. Between the order and the payment the dollar can rise or fall against the FCFA, so the importer may end up paying more or fewer francs than recorded. Accounting must record the debt in FCFA, follow it at the year end, and show the gain or loss fairly."),
        D("A **foreign currency transaction** is one priced in a currency other than the FCFA. It is recorded in FCFA at the **spot rate** (the exchange rate on the transaction date). At the year end, receivables and debts still unsettled are converted at the **closing rate**; the difference is a **conversion difference** (ecart de conversion).",
          title="Definition: foreign currency transaction"),
        T("The FCFA used in Cameroon and the other CEMAC states has a **fixed parity** with the euro: 1 euro = 655.957 FCFA. Transactions in euros therefore produce no exchange differences. Examples in this lesson use the US dollar (USD) and the pound sterling (GBP), whose rates move; all rates are invented for practice."),
        KEY("The SYSCOHADA treatment at the year end", "Prudence decides how gains and losses are treated.", cards=[
            ["Unrealised loss", "Debt worth more or receivable worth less at the closing rate: debit **478** Conversion difference, asset; credit the debt or receivable. Then a **provision for exchange loss** (194) is charged to the result."],
            ["Unrealised gain", "Debt worth less or receivable worth more: debit the receivable or debt; credit **479** Conversion difference, liability. Nothing goes to the result."],
            ["Next year", "The restatement entries are reversed at the start of the year, so the debt or receivable returns to its historical value."],
            ["Settlement", "The difference between the historical value and the amount actually paid or received is a **realised** loss (676) or gain (776)."],
        ]),
        T("Account numbers 478, 479, 676, 776 and 194 are the standard SYSCOHADA accounts; the expense and reversal accounts for the provision (697 and 797 here) are financial provision accounts whose exact sub-numbers vary between textbooks."),
        H("Worked examples"),
        EX("Worked example 1: an import debt over the year end", intro="On 10 November N, Ngono Distribution buys goods for 20 000 USD, payable on 15 February N+1. Rates (FCFA per USD, invented): 10 November 600; 31 December 615; 15 February 610. Record the purchase and the year-end entries.", steps=[
            S("Historical value", math=r"20\,000 \times 600 = 12\,000\,000", text="Dr 601, Cr 401."),
            S("Value at the closing rate", math=r"20\,000 \times 615 = 12\,300\,000", text="The debt has grown: an unrealised loss."),
            S("Unrealised loss", math=r"12\,300\,000 - 12\,000\,000 = 300\,000", text="Dr 478, Cr 401 with 300 000. The debt appears in the balance sheet at 12 300 000."),
            S("Prudence", text="The probable loss is charged to the result of year N by a provision: Dr financial provision charge, Cr 194, 300 000."),
        ]),
        CODE(_fx_j1, "text", title="Year N in the importer's books (FCFA, rates invented for practice)"),
        EX("Worked example 2: payment in year N+1", intro="Continue example 1 into year N+1.", steps=[
            S("Reverse the restatement on 1 January", text="Dr 401, Cr 478, 300 000: the debt is back to 12 000 000."),
            S("Amount paid", math=r"20\,000 \times 610 = 12\,200\,000"),
            S("Realised loss", math=r"12\,200\,000 - 12\,000\,000 = 200\,000", text="Dr 401 12 000 000; Dr 676 Exchange losses 200 000; Cr bank 12 200 000."),
            S("Release the provision", text="The risk has ended: Dr 194, Cr financial reversals, 300 000."),
            S("Check the total effect", math=r"\text{N: } -300\,000;\ \text{N+1: } -200\,000 + 300\,000 = +100\,000;\ \text{total } -200\,000", text="Over the two years the result bears exactly the real loss of 200 000."),
        ]),
        CODE(_fx_j2, "text", title="Year N+1 in the importer's books"),
        EX("Worked example 3: an export receivable with an unrealised gain", intro="On 1 December N a Kribi exporter sells timber for 10 000 GBP. Rates (FCFA per GBP, invented): 1 December 760; 31 December 780; 20 January N+1 when paid, 775.", steps=[
            S("Historical value", math=r"10\,000 \times 760 = 7\,600\,000", text="Dr 411, Cr 701."),
            S("At the closing rate", math=r"10\,000 \times 780 = 7\,800\,000", text="The receivable is worth 200 000 more: an unrealised gain."),
            S("Year-end entry", text="Dr 411, Cr 479, 200 000. **No income** is recorded in year N: the gain is not realised (prudence)."),
            S("Year N+1", math=r"10\,000 \times 775 - 7\,600\,000 = 150\,000", text="After reversing the restatement, the receipt of 7 750 000 gives a realised gain of 150 000 (Cr 776)."),
        ]),
        CODE(_fg_j, "text", title="The exporter's books"),
        H("Evaluation"),
        T("The SYSCOHADA method is prudent and reliable: the balance sheet shows debts and receivables at their current value, losses hit the result early, and income is never anticipated. Its critics say it is **asymmetric**: an exporter with a likely gain shows nothing, while an importer with a likely loss shows it at once, so two firms in similar positions report different results. Firms reduce the risk itself by invoicing in euros where possible, which the fixed parity makes free of exchange risk, or by hedging with their banks."),
        MISTAKE("Taking an unrealised gain to income", "An unrealised gain is credited to 479, a balance sheet account. It becomes income (776) only when the receivable is collected or the debt paid."),
        MISTAKE("Forgetting the provision", "The 478 entry alone does not reduce the result. The provision for exchange loss is what charges the probable loss to the year."),
        MISTAKE("Computing the realised loss from the closing rate", "Because the restatement is reversed, the realised difference is measured from the historical rate: 610 - 600, not 610 - 615."),
        QUIZ("At the year end a debt of 10 000 USD, recorded at 590 FCFA per USD, is restated at a closing rate of 600. The entry is",
             ["Dr 401, Cr 479 100 000", "Dr 478, Cr 401 100 000", "Dr 676, Cr 401 100 000", "No entry until payment"], 1,
             "The debt has grown by 10 000 x (600 - 590) = 100 000: an unrealised loss in 478, then a provision.",
             hint="Is the debt now bigger or smaller in FCFA?",
             feedback=["479 is used for unrealised gains; this is a loss.", "", "676 is for realised losses at settlement.", "Unsettled items are restated at the year end."]),
        QUIZ("Why do purchases invoiced in euros not produce exchange differences for a Cameroonian firm?",
             ["Euro transactions are exempt from accounting", "The FCFA has a fixed parity with the euro", "Banks absorb the differences", "They are recorded at the closing rate only"], 1,
             "1 euro = 655.957 FCFA, fixed, so the rate on the invoice date equals the rate on payment.",
             hint="What is special about the euro rate for the FCFA?",
             feedback=["They are recorded like any other transaction.", "", "Banks do not absorb exchange differences.", "They are recorded at the rate of the day, which never changes."]),
        PQ("A firm sells goods for 5 000 USD when 1 USD = 590 FCFA. At the year end the rate is 610. The customer pays the next year when the rate is 580. Journalise all entries and state the effect on the result of each year.",
           "Sale: Dr 411, Cr 701, 2 950 000 (5 000 x 590). Year end: receivable worth 5 000 x 610 = 3 050 000, unrealised gain 100 000: Dr 411, Cr 479, 100 000; no effect on the result of year 1. Year 2: reverse (Dr 479, Cr 411, 100 000). Receipt 5 000 x 580 = 2 900 000: Dr 521 2 900 000; Dr 676 Exchange losses 50 000; Cr 411 2 950 000. Effect: year 1 nil; year 2 a realised loss of **50 000**."),
        PQ("Explain the difference between a conversion difference and a realised exchange gain or loss.",
           "A **conversion difference** arises at the year end when an unsettled foreign currency item is restated at the closing rate; it is unrealised and recorded in balance sheet accounts 478 (loss) or 479 (gain); only the loss affects the result, through a provision. A **realised** gain or loss arises when the item is settled: the FCFA actually paid or received differs from the historical value, and the difference goes to 776 or 676 in the result."),
        PQ("Discuss whether the asymmetric treatment of unrealised exchange gains and losses gives a true and fair view.",
           "Plan. For: prudence; gains may disappear before settlement (as in example 3, where the gain fell from 200 000 to 150 000); avoids distributing profits not yet earned. Against: two similar firms report different results; the balance sheet shows the gain in 479 but the income statement ignores it, which some users find inconsistent; IFRS takes both gains and losses to profit. Judgement: within SYSCOHADA's prudent framework the treatment is defensible, and the notes should explain the exposure so users can judge."),
        TIP("Exam link: foreign currency can appear in Paper 1 (which account, which rate) and in Paper 3 Section A as part of trading or year-end questions. Write the rates and the FCFA value at each date in a small table before journalising."),
        SUM("Record foreign currency transactions at the spot rate of the transaction date.",
            "At the year end restate unsettled items at the closing rate: losses to 478 (plus a provision, 194), gains to 479 (no income).",
            "Reverse the restatement at the start of the next year.",
            "On settlement, the difference from the historical value is a realised loss (676) or gain (776).",
            "Euro transactions give no differences: 1 euro = 655.957 FCFA, fixed."),
    ],
))

# ------------------------------------------------------------------ 10. payroll
# Teaching values modelled on the rates quoted in Cameroonian textbooks; check the current Finance Law and CNPS rules.
PR_CNPS_EE = _Fr(42, 1000)      # employee pension contribution
PR_CNPS_ER = _Fr(42, 1000)      # employer pension contribution
PR_FAM = _Fr(7, 100)            # employer family allowances
PR_ACC = _Fr(175, 10000)        # employer work-accident rate (lowest risk group)
PR_CFC_EE, PR_CFC_ER, PR_FNE = _Fr(1, 100), _Fr(15, 1000), _Fr(1, 100)
PR_SCALE = ((0, 2000000, 10), (2000000, 3000000, 15), (3000000, 5000000, 25), (5000000, 10 ** 12, 35))


def _irpp_annual(base):
    t = _Fr(0)
    for lo, hi, r in PR_SCALE:
        if base > lo:
            t += (min(base, hi) - lo) * _Fr(r, 100)
    return t


_pr_base_sal, _pr_rate = 380000, 2000
_pr_sen = _pr_base_sal * 5 // 100
_pr_ot = int(_pr_rate * (8 * _Fr(12, 10) + 4 * _Fr(13, 10)))
_pr_transp = 31400
_pr_g = _pr_base_sal + _pr_sen + _pr_ot + _pr_transp
assert (_pr_sen, _pr_ot, _pr_g) == (19000, 29600, 460000)
_pr_A = 12 * _pr_g
_pr_taxbase = _pr_A * _Fr(7, 10) - _pr_A * PR_CNPS_EE - 500000
_pr_irpp_y = _irpp_annual(_pr_taxbase)
assert (_pr_taxbase, _pr_irpp_y) == (3132160, 383040)
_pr_irpp = int(_pr_irpp_y / 12)
_pr_cac = _pr_irpp // 10
_pr_cnps = int(_pr_g * PR_CNPS_EE)
_pr_cfc = int(_pr_g * PR_CFC_EE)
_pr_rav = 5850
_pr_ded = _pr_cnps + _pr_irpp + _pr_cac + _pr_cfc + _pr_rav
_pr_net = _pr_g - _pr_ded
_pr_adv = 50000
_pr_pay = _pr_net - _pr_adv
assert (_pr_irpp, _pr_cac, _pr_cnps, _pr_cfc, _pr_ded, _pr_net, _pr_pay) == (31920, 3192, 19320, 4600, 64882, 395118, 345118)
_pr_er = [int(_pr_g * r) for r in (PR_CNPS_ER, PR_FAM, PR_ACC, PR_CFC_ER, PR_FNE)]
assert _pr_er == [19320, 32200, 8050, 6900, 4600]
_pr_er_cnps = sum(_pr_er[:3])
_pr_er_tax = sum(_pr_er[3:])
_pr_cost = _pr_g + sum(_pr_er)
assert (_pr_er_cnps, _pr_er_tax, _pr_cost) == (59570, 11500, 531070)
_pr_state = _pr_irpp + _pr_cac + _pr_cfc + _pr_rav
assert _pr_state == 45562

_pr_slip = rows([
    ("Base salary", _pr_base_sal),
    ("Seniority bonus 5%", _pr_sen),
    ("Overtime (8 h x 120%, 4 h x 130%)", _pr_ot),
    ("Transport allowance", _pr_transp),
    (None, None),
    ("GROSS PAY", _pr_g),
    ("CNPS pension, employee 4.2%", -_pr_cnps),
    ("IRPP (from the annual scale)", -_pr_irpp),
    ("CAC 10% of IRPP", -_pr_cac),
    ("CFC employee 1%", -_pr_cfc),
    ("RAV (from its scale)", -_pr_rav),
    (None, None),
    ("NET PAY", _pr_net),
    ("Less advance taken on 15th", -_pr_adv),
    (None, None),
    ("NET TO PAY", _pr_pay),
], w=36)
_pr_irpp_tbl = rows([
    ("Annual gross (460 000 x 12)", _pr_A),
    ("Less professional costs 30%", -_pr_A * 3 // 10),
    ("Less CNPS pension 4.2%", -int(_pr_A * PR_CNPS_EE)),
    ("Less annual abatement", -500000),
    (None, None),
    ("Taxable base", int(_pr_taxbase)),
    ("10% on first 2 000 000", 200000),
    ("15% on next 1 000 000", 150000),
    ("25% on remaining 132 160", 33040),
    (None, None),
    ("Annual IRPP", int(_pr_irpp_y)),
    ("Monthly IRPP (divide by 12)", _pr_irpp),
], w=34)
assert 200000 + 150000 + 33040 == _pr_irpp_y and _pr_taxbase - 3000000 == 132160
_pr_j = journal([
    ("15 Mar  Advance on salary in cash", [("421", "Staff, advances", _pr_adv, 0), ("571", "Cash", 0, _pr_adv)]),
    ("31 Mar  March payroll", [("661", "Salaries and wages", _pr_g, 0), ("421", "Staff, advances", 0, _pr_adv),
                               ("431", "CNPS", 0, _pr_cnps), ("447", "State, taxes withheld", 0, _pr_state),
                               ("422", "Staff, pay due", 0, _pr_pay)]),
    ("31 Mar  Employer's charges", [("664", "Social charges", _pr_er_cnps, 0), ("641", "Taxes on salaries", _pr_er_tax, 0),
                                   ("431", "CNPS", 0, _pr_er_cnps), ("447", "State, taxes withheld", 0, _pr_er_tax)]),
    ("31 Mar  Net pay transferred", [("422", "Staff, pay due", _pr_pay, 0), ("521", "Bank", 0, _pr_pay)]),
])
# practice question (gross 300 000)
_pq_A = 12 * 300000
_pq_base = _pq_A * _Fr(7, 10) - _pq_A * PR_CNPS_EE - 500000
assert _pq_base == 1868800 and _irpp_annual(_pq_base) == 186880
assert round(_Fr(186880, 12)) == 15573 and int(300000 * PR_CNPS_EE) == 12600
assert [int(300000 * r) for r in (PR_CNPS_ER, PR_FAM, PR_ACC, PR_CFC_ER, PR_FNE)] == [12600, 21000, 5250, 4500, 3000]
assert 300000 + 12600 + 21000 + 5250 + 4500 + 3000 == 346350

LESSONS.append(lesson(
    module=M2,
    topic="Payroll",
    title="Payroll: gross pay, CNPS, IRPP and the payroll entries",
    slug="acl1-payroll",
    minutes=28,
    summary="Gross pay adds base salary, bonuses, overtime and allowances. The employer withholds the employee's CNPS contribution and the taxes on salary (IRPP from a scale, CAC, CFC, RAV), pays the net, and adds its own CNPS and payroll charges. All rates here are teaching values to check.",
    objectives=[
        "Calculate gross pay including seniority bonus, overtime at increased rates and allowances",
        "Compute the employee's deductions, including IRPP from an annual progressive scale, and the net pay",
        "Calculate the employer's contributions and the total cost of an employee",
        "Journalise the payroll, the employer's charges, advances and payments using classes 42, 43, 44 and 66",
    ],
    key_concepts=["Gross pay", "Seniority bonus", "Overtime increment", "CNPS contributions", "IRPP progressive scale", "CAC", "CFC", "RAV", "Net pay", "Employer's charges", "Total employment cost"],
    blocks=[
        H("Introduction"),
        T("At the end of each month an accounts clerk in Limbe turns hours, bonuses and allowances into a payslip, withholds social contributions and taxes, pays each worker, and later pays the CNPS and the tax office. At O Level you used flat teaching rates. At A Level you meet the real structure: an IRPP calculated on a progressive annual scale, employer contributions, advances and the full set of entries."),
        D("**Rates and scales here are teaching values** modelled on those quoted in Cameroonian textbooks. Contribution rates, ceilings, the IRPP scale, allowances that are exempt and the RAV and local development tax (TDL) scales are set by law and change. Always use the rates given in an examination question, and check the current Finance Law and CNPS rules for real payrolls.",
          title="Important: teaching values"),
        H("From base salary to gross pay"),
        KEY("Elements of gross pay", "Everything the employee earns before deductions.", cards=[
            ["Base salary", "The salary for the employee's category under the collective agreement or contract."],
            ["Seniority bonus", "A percentage of base salary that rises with years of service."],
            ["Overtime", "Hours beyond the legal week, paid at an increased rate. Teaching rates: first 8 hours +20%, next hours +30% (night and holiday hours higher); check the current decree."],
            ["Allowances and benefits", "Transport, housing, responsibility allowances and benefits in kind. Some are partly exempt in real payroll; in this lesson all are treated as taxable and contributory."],
        ]),
        KEY("Deductions and employer charges (teaching values)", "Who pays what, on gross pay.", cards=[
            ["Employee", "CNPS pension 4.2% (on pay up to a monthly ceiling, often quoted as 750 000); IRPP from the scale; CAC 10% of the IRPP; CFC 1%; RAV from a fixed scale (and TDL where your textbook includes it)."],
            ["Employer", "CNPS pension 4.2%; family allowances 7%; work accidents 1.75% to 5% by risk group; CFC 1.5%; FNE (National Employment Fund) 1%."],
        ]),
        F(r"\text{Taxable base} = \text{annual gross} - 30\%\ \text{professional costs} - \text{CNPS pension} - 500\,000", title="IRPP base (teaching method)"),
        T("IRPP scale used in this lesson (annual): 10% up to 2 000 000; 15% from 2 000 001 to 3 000 000; 25% from 3 000 001 to 5 000 000; 35% above 5 000 000. Monthly IRPP is the annual figure divided by 12. Pay below a minimum is exempt from IRPP; check the current threshold."),
        H("Worked examples"),
        EX("Worked example 1: gross pay", intro="Mr Tchoua, an accounts clerk, has a base salary of FCFA 380 000, a 5% seniority bonus, a transport allowance of 31 400 and, in March, 12 hours of overtime at an hourly rate of 2 000 (8 hours at +20%, 4 hours at +30%).", steps=[
            S("Seniority bonus", math=r"380\,000 \times 5\% = 19\,000"),
            S("Overtime", math=r"2\,000 \times (8 \times 1.2 + 4 \times 1.3) = 2\,000 \times 14.8 = 29\,600"),
            S("Gross pay", math=r"380\,000 + 19\,000 + 29\,600 + 31\,400 = 460\,000"),
        ]),
        EX("Worked example 2: IRPP from the annual scale", intro="Find Mr Tchoua's monthly IRPP and CAC, treating March pay as typical of the year.", steps=[
            S("Annual gross", math=r"460\,000 \times 12 = 5\,520\,000"),
            S("Taxable base", math=r"5\,520\,000 - 1\,656\,000 - 231\,840 - 500\,000 = 3\,132\,160", text="30% professional costs = 1 656 000; CNPS pension 4.2% = 231 840."),
            S("Apply the scale", math=r"200\,000 + 150\,000 + 132\,160 \times 25\% = 383\,040"),
            S("Monthly IRPP and CAC", math=r"383\,040 \div 12 = 31\,920;\ \text{CAC} = 10\% \times 31\,920 = 3\,192"),
        ]),
        CODE(_pr_irpp_tbl, "text", title="IRPP working (FCFA, teaching scale)"),
        EX("Worked example 3: net pay and employer's cost", intro="Complete the payslip. RAV on this pay (teaching scale) is 5 850. Mr Tchoua took an advance of 50 000 in cash on 15 March.", steps=[
            S("Employee deductions", math=r"19\,320 + 31\,920 + 3\,192 + 4\,600 + 5\,850 = 64\,882", text="CNPS 4.2% of 460 000 = 19 320; CFC 1% = 4 600."),
            S("Net pay", math=r"460\,000 - 64\,882 = 395\,118;\ \text{net to pay} = 395\,118 - 50\,000 = 345\,118"),
            S("Employer's charges", math=r"19\,320 + 32\,200 + 8\,050 + 6\,900 + 4\,600 = 71\,070", text="Pension 4.2%, family allowances 7%, work accidents 1.75%, CFC 1.5%, FNE 1%."),
            S("Total cost of the employee", math=r"460\,000 + 71\,070 = 531\,070"),
        ]),
        CODE(_pr_slip, "text", title="Payslip of Mr Tchoua, March (FCFA, invented for practice; teaching rates)"),
        EX("Worked example 4: the entries", intro="Journalise the advance, the payroll, the employer's charges and the bank transfer of net pay.", steps=[
            S("Advance", text="Dr 421 Staff, advances; Cr cash."),
            S("Payroll", text="Dr 661 with gross pay; Cr 421 to recover the advance, Cr 431 CNPS (employee share), Cr 447 State with IRPP, CAC, CFC and RAV withheld (45 562), Cr 422 with the net to pay."),
            S("Employer's charges", text="Dr 664 social charges (CNPS: 59 570) and 641 taxes on salaries (CFC and FNE: 11 500); Cr 431 and 447."),
            S("Payments", text="Dr 422, Cr bank for net pay. Later Dr 431 and Dr 447, Cr bank when the CNPS and the tax office are paid."),
        ]),
        CODE(_pr_j, "text", title="Payroll entries for March"),
        T("Sub-accounts for each tax and for the CNPS branches vary between textbooks (for example separate sub-accounts of 447 for IRPP, CAC, CFC and RAV, and of 431 for pensions and family allowances). The main accounts 42, 43, 44, 66 and 64 are what matters."),
        MISTAKE("Calculating CAC on gross pay", "CAC is 10% of the IRPP, not of gross. Here 3 192, not 46 000."),
        MISTAKE("Applying the highest IRPP rate to the whole base", "The scale is progressive: each rate applies only to its slice. 25% x 3 132 160 would be far too much."),
        MISTAKE("Debiting employer charges to 661", "661 records gross pay. The employer's own contributions go to 664 (social charges) and 64 (taxes on salaries)."),
        QUIZ("Gross pay is FCFA 460 000. Which figure is the employee's net pay before the advance?",
             ["FCFA 395 118", "FCFA 345 118", "FCFA 388 930", "FCFA 531 070"], 0,
             "460 000 - 64 882 = 395 118. The advance then reduces the amount still to pay.",
             hint="Deduct only the employee's contributions and taxes.",
             feedback=["", "That is after the advance: the net still to pay.", "That deducts the employer's charges, which the employee does not pay.", "That is the employer's total cost."]),
        QUIZ("In the payroll entry, the IRPP withheld from employees is credited to",
             ["661 Salaries", "431 CNPS", "447 State, taxes withheld", "422 Staff, pay due"], 2,
             "The employer owes the IRPP to the State until it pays it over.",
             hint="To whom does the employer pay the IRPP?",
             feedback=["661 is debited with gross pay.", "431 is for social security contributions.", "", "422 is the net pay owed to staff."]),
        PQ("Using the teaching method and scale of this lesson, calculate the monthly IRPP and CAC of an employee whose gross pay is FCFA 300 000 a month (round to the nearest franc).",
           "Annual gross 3 600 000. Taxable base = 3 600 000 - 1 080 000 (30%) - 151 200 (CNPS 4.2%) - 500 000 = **1 868 800**. IRPP = 10% x 1 868 800 = 186 880 a year (all within the first band). Monthly IRPP = 186 880 / 12 = **15 573**. CAC = 10% x 15 573 = **1 557**."),
        PQ("For the same employee (gross 300 000), calculate the employer's charges and the total monthly cost using the teaching rates.",
           "CNPS pension 4.2% = 12 600; family allowances 7% = 21 000; work accidents 1.75% = 5 250; CFC 1.5% = 4 500; FNE 1% = 3 000. Charges = **46 350**. Total cost = 300 000 + 46 350 = **FCFA 346 350**."),
        PQ("Explain why the total cost of an employee to the business is higher than the gross pay, and why the net pay is lower.",
           "The employer adds its own contributions (CNPS pension, family allowances, work accidents, CFC, FNE), so the **cost** is gross plus employer charges. The employee's own contributions and taxes (CNPS, IRPP, CAC, CFC, RAV) are deducted from gross, so the **net** is lower. The business collects the employee deductions and pays them, with its own charges, to the CNPS and the State."),
        TIP("Exam link: payroll appears in Paper 1 calculations and inside Paper 3 questions. The question gives the rates: use them exactly, show the base of each deduction (gross or IRPP) and keep the employee and employer columns separate."),
        SUM("Gross pay = base salary + bonuses + overtime + allowances.",
            "Employee deductions (teaching values): CNPS 4.2%, IRPP from a progressive annual scale, CAC 10% of IRPP, CFC 1%, RAV from a scale.",
            "Employer charges (teaching values): CNPS 4.2% + 7% + work accidents, CFC 1.5%, FNE 1%; cost = gross + charges.",
            "Entries: Dr 661, Cr 421/431/447/422; Dr 664 and 64, Cr 431 and 447; then payments.",
            "All rates change with the law: use the question's rates and check the current Finance Law."),
    ],
))

# ------------------------------------------------------------------ 11. acquisition of fixed assets
_aq_price = 18000000
_aq_rem = _aq_price * 5 // 100
_aq_net = _aq_price - _aq_rem
_aq_tr, _aq_inst, _aq_test, _aq_train = 600000, 900000, 300000, 400000
_aq_cost = _aq_net + _aq_tr + _aq_inst + _aq_test
_aq_vat_a = vat(_aq_cost)
_aq_vat_t = vat(_aq_train)
_aq_ttc = _aq_cost + _aq_train + _aq_vat_a + _aq_vat_t
_aq_adv = 5000000
assert (_aq_rem, _aq_net, _aq_cost, _aq_vat_a, _aq_vat_t, _aq_ttc) == (900000, 17100000, 18900000, 3638250, 77000, 23015250)
assert _aq_ttc - _aq_adv == 18015250
_aq_tbl = rows([
    ("Catalogue price", _aq_price),
    ("Less remise 5%", -_aq_rem),
    ("Transport to the factory", _aq_tr),
    ("Installation", _aq_inst),
    ("Testing before use", _aq_test),
    (None, None),
    ("COST OF THE MACHINE", _aq_cost),
    ("Not in cost: staff training", _aq_train),
    ("Not in cost: recoverable VAT", _aq_vat_a + _aq_vat_t),
], w=34)
_aq_j = journal([
    ("10 Jan  Advance paid to the dealer", [("251", "Advances on fixed assets", _aq_adv, 0), ("521", "Bank", 0, _aq_adv)]),
    ("1 Mar   Invoice for machine and training", [("241", "Industrial equipment", _aq_cost, 0), ("63", "Training (ext. service)", _aq_train, 0),
                                                 ("4451", "VAT on fixed assets", _aq_vat_a, 0), ("4454", "VAT on services", _aq_vat_t, 0),
                                                 ("481", "Fixed asset suppliers", 0, _aq_ttc)]),
    ("1 Mar   Advance set against invoice", [("481", "Fixed asset suppliers", _aq_adv, 0), ("251", "Advances on fixed assets", 0, _aq_adv)]),
])
_ip = dict(materials=6000000, labour=3500000, overheads=1500000)
_ip_cost = sum(_ip.values())
assert _ip_cost == 11000000
_ip_j = journal([("31 Dec  Warehouse built by own staff", [("231", "Buildings", _ip_cost, 0), ("72", "Own work capitalised", 0, _ip_cost)])])
# practice figures
assert 12000000 * 90 // 100 + 450000 + 250000 == 11500000 and 11500000 + 300000 == 11800000

LESSONS.append(lesson(
    module=M3,
    topic="Acquisition of fixed assets",
    title="Acquiring fixed assets: recognition, cost and entries",
    slug="acl1-acquisition-of-fixed-assets",
    minutes=24,
    summary="A fixed asset is recorded when the entity controls it, expects benefits for more than one year and can measure its cost. Cost is the price after trade reductions plus costs needed to make the asset ready for use; training, general overheads and recoverable VAT are excluded.",
    objectives=[
        "State the conditions for recognising a tangible or intangible fixed asset",
        "Calculate the acquisition cost by including and excluding the right costs",
        "Journalise a purchase with an advance, VAT and a fixed asset supplier, and an asset produced by the entity",
        "Explain how capitalising or expensing a cost changes profit and the balance sheet",
    ],
    key_concepts=["Fixed asset", "Recognition criteria", "Acquisition cost", "Directly attributable costs", "Intangible asset", "Own work capitalised", "Advance on fixed assets", "Capital and revenue expenditure"],
    blocks=[
        H("Introduction"),
        T("A cassava-processing cooperative in Bertoua buys a grating machine. The invoice shows the price, a discount, transport, installation, a test run and two days of staff training. Which of these belong to the machine and which are expenses of the year? The answer decides both the value of the machine and the profit."),
        D("A **fixed asset** (immobilisation) is an asset the entity **controls**, from which it expects **economic benefits** over more than one financial year, and whose **cost can be measured reliably**. It is held for use in the business, not for resale. Fixed assets are **tangible** (land, buildings, machines, vehicles) or **intangible** (software, patents, licences, some development costs).",
          title="Definition: fixed asset and recognition criteria"),
        KEY("What goes into the acquisition cost", "Cost = everything needed to bring the asset to its place and make it ready for use.", cards=[
            ["Include", "Purchase price after trade reductions (rabais, remise); non-recoverable taxes and import duties; transport and handling to the site; installation and site preparation; testing; professional fees (for example an architect); the estimated cost of dismantling and restoring the site, where there is an obligation."],
            ["Exclude", "Recoverable VAT (it goes to 4451); staff training; general administration and overheads; advertising and opening costs; costs incurred after the asset is ready for use, such as repairs and maintenance."],
            ["Check your textbook", "Whether a financial discount (escompte) on an asset purchase is deducted from cost and whether borrowing costs may be included differ between textbooks."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: the cost of a machine", intro="The cooperative buys a machine from a Douala dealer. Catalogue price FCFA 18 000 000; remise 5%; transport 600 000; installation 900 000; testing 300 000; staff training 400 000; VAT 19.25% on everything invoiced (recoverable). Find the cost of the machine.", steps=[
            S("Net price", math=r"18\,000\,000 - 900\,000 = 17\,100\,000"),
            S("Add costs needed to make it ready", math=r"17\,100\,000 + 600\,000 + 900\,000 + 300\,000 = 18\,900\,000"),
            S("Leave out the rest", text="Training (400 000) is an expense of the year. Recoverable VAT is a claim on the State, not cost."),
        ]),
        CODE(_aq_tbl, "text", title="Cost of the machine (FCFA, invented for practice)"),
        EX("Worked example 2: the entries with an advance", intro="On 10 January the cooperative paid an advance of FCFA 5 000 000. The invoice arrived on 1 March. Journalise.", steps=[
            S("Advance", text="Dr 251 Advances paid on fixed assets, Cr bank. The machine is not yet owned."),
            S("VAT on the invoice", math=r"18\,900\,000 \times 19.25\% = 3\,638\,250;\ 400\,000 \times 19.25\% = 77\,000"),
            S("Invoice total", math=r"18\,900\,000 + 400\,000 + 3\,638\,250 + 77\,000 = 23\,015\,250", text="Dr 241 Industrial equipment, Dr the training expense (class 63), Dr 4451 and 4454; Cr 481 Fixed asset suppliers."),
            S("Use the advance", math=r"23\,015\,250 - 5\,000\,000 = 18\,015\,250", text="Dr 481, Cr 251 with 5 000 000; the dealer is still owed 18 015 250."),
        ]),
        CODE(_aq_j, "text", title="Journal of the cooperative"),
        EX("Worked example 3: an asset built by the entity", intro="A company builds a warehouse with its own staff: materials 6 000 000, direct labour 3 500 000, overheads directly attributable to the construction 1 500 000. How is it recorded at the year end?", steps=[
            S("Production cost", math=r"6\,000\,000 + 3\,500\,000 + 1\,500\,000 = 11\,000\,000"),
            S("Why an income account", text="The materials and wages have already been charged as expenses during the year. Crediting **72 Own work capitalised** cancels their effect on the result, and the warehouse appears as an asset: Dr 231, Cr 72."),
        ]),
        CODE(_ip_j, "text", title="Asset produced by the entity"),
        KEY("Intangible assets", "Same criteria, more judgement.", cards=[
            ["Bought", "Software, licences, patents and trademarks bought from others are recorded in 21 at their cost."],
            ["Developed internally", "Research is always an expense. Development costs are capitalised only when the project is technically feasible, the entity intends and is able to complete and use or sell it, future benefits are probable and costs are measured reliably."],
            ["Never recognised", "Internally generated brands, customer lists and the reputation of the business (goodwill created internally)."],
        ]),
        H("Evaluation: capital or revenue expenditure?"),
        T("Recording a cost as an asset (capital expenditure) raises profit this year and spreads the cost over later years through depreciation. Recording it as an expense (revenue expenditure) lowers this year's profit. A manager who wants a good result may be tempted to capitalise repairs or training; one who wants to pay less tax may expense new equipment. The recognition rules and the materiality convention exist to stop both: a cost is capitalised only if it creates future benefits beyond the year, and very small items can be expensed even if they last."),
        MISTAKE("Including recoverable VAT in cost", "Recoverable VAT goes to 4451. Only non-deductible VAT (for example on certain passenger cars) is part of cost."),
        MISTAKE("Capitalising training or repairs", "Training staff to use a machine does not make the machine itself ready; it is an expense. Repairs after the asset is in use are expenses unless they extend its life or capacity."),
        MISTAKE("Crediting 401 for the asset supplier", "The supplier of a fixed asset is 481, and advances on assets are 251, not 409."),
        QUIZ("Which cost is included in the cost of a new machine?",
             ["Training of operators", "Installation on its base", "Recoverable VAT", "A repair in its second year"], 1,
             "Installation is necessary to make the machine ready for use.",
             hint="Which cost is needed before the machine can work?",
             feedback=["Training is an expense of the year.", "", "Recoverable VAT is a claim on the State.", "Repairs after it is in use are expenses."]),
        QUIZ("A firm builds a shed with its own workers. The entry to recognise the shed is",
             ["Dr 231, Cr 521", "Dr 231, Cr 72 Own work capitalised", "Dr 6 expenses, Cr 231", "Dr 72, Cr 231"], 1,
             "Materials and wages are already in expenses; crediting 72 neutralises them and the shed becomes an asset.",
             hint="The costs were already recorded as expenses. What must be credited?",
             feedback=["No cash is paid at this stage; the costs were paid earlier.", "", "This would reduce the asset.", "This reverses the correct entry."]),
        PQ("A van is bought: list price 12 000 000, remise 10%, signwriting with the company name 450 000, delivery 250 000, first year's insurance 300 000, VAT recoverable. Calculate the cost of the van and say what happens to the items you exclude.",
           "Cost = 12 000 000 x 90% + 450 000 + 250 000 = 10 800 000 + 700 000 = **FCFA 11 500 000**. Signwriting and delivery are needed to make the van ready for the business. Insurance (300 000) is an expense of the year (with a prepayment adjustment if it covers the next year). Recoverable VAT goes to 4451."),
        PQ("State the conditions under which development costs may be recorded as an intangible fixed asset.",
           "Research costs are always expensed. Development costs are capitalised only if: the project is technically feasible; the entity intends to complete it and can use or sell the result; future economic benefits are probable (a market or an internal use exists); adequate resources are available; and the costs can be measured reliably. If any condition fails, they are expensed."),
        PQ("Explain how wrongly capitalising a repair of FCFA 2 000 000 affects the financial statements.",
           "Expenses are understated by 2 000 000, so profit is overstated by that amount (less any depreciation charged on it). Fixed assets are overstated in the balance sheet. In later years depreciation on the wrong asset reduces profit, so the error moves profit between years and breaks the true and fair view."),
        TIP("Exam link: cost of fixed assets is a frequent Paper 1 item (which costs to include) and the first step of Paper 3 questions on depreciation and disposals. List each cost with 'include' or 'exclude' before adding."),
        SUM("Recognise a fixed asset when it is controlled, gives benefits beyond one year and has a measurable cost.",
            "Cost = net price + costs needed to make it ready for use (transport, installation, testing, fees, dismantling where required).",
            "Exclude recoverable VAT, training, general overheads and later repairs.",
            "Entries: advance Dr 251; invoice Dr 2x and 4451, Cr 481; assets built in-house Dr 2x, Cr 72.",
            "Capital versus revenue expenditure decides both profit and the balance sheet."),
    ],
))

# ------------------------------------------------------------------ 12. depreciation methods
# Example 1: straight line with prorata (machine of lesson 11)
_dp_cost, _dp_life = 18900000, 6
_dp_ann = _dp_cost // _dp_life
_dp_first = _dp_ann * 10 // 12
_dp_last = _dp_ann * 2 // 12
assert (_dp_ann, _dp_first, _dp_last) == (3150000, 2625000, 525000)
_dp_sched = [_dp_first] + [_dp_ann] * 5 + [_dp_last]
assert sum(_dp_sched) == _dp_cost
_dp_body, _acc = [], 0
for _i, _d in enumerate(_dp_sched):
    _acc += _d
    _dp_body.append([f"N+{_i}" if _i else "N", _d, _acc, _dp_cost - _acc])
_dp_tbl = grid(["Year", "Charge", "Accumulated", "NBV"], [6, 11, 13, 12], _dp_body)
assert _dp_body[-1][3] == 0

# Example 2: declining balance, coefficient 2, switch to straight line
_db_cost, _db_life, _db_coef = 12000000, 5, 2
_db_rate = _Fr(_db_coef, _db_life)
_db_nbv = _db_cost
_db_rows, _db_charges = [], []
for _y in range(_db_life):
    _left = _db_life - _y
    _dec = _db_nbv * _db_rate
    _sl = _Fr(_db_nbv, _left)
    _ch = max(_dec, _sl)
    assert _ch.denominator == 1
    _ch = int(_ch)
    _db_rows.append([f"N+{_y}" if _y else "N", _db_nbv, int(_dec), int(_sl), _ch, _db_nbv - _ch])
    _db_charges.append(_ch)
    _db_nbv -= _ch
assert _db_charges == [4800000, 2880000, 1728000, 1296000, 1296000] and _db_nbv == 0
_db_tbl = grid(["Year", "Opening", "40%", "SL rest", "Charge", "Closing"], [6, 11, 10, 10, 10, 10], _db_rows)
_sl_nbv = [_db_cost - 2400000 * k for k in range(6)]
assert [x / 1000000 for x in _sl_nbv] == [12, 9.6, 7.2, 4.8, 2.4, 0]

# Example 3: components
_cp = [("Structure", 90000000, 40), ("Roof", 18000000, 15), ("Lifts, wiring", 12000000, 10)]
_cp_tot = sum(c for _, c, _ in _cp)
_cp_ch = [c // y for _, c, y in _cp]
assert _cp_tot == 120000000 and _cp_ch == [2250000, 1200000, 1200000] and sum(_cp_ch) == 4650000
assert _cp_tot // 40 == 3000000
_cp_tbl = grid(["Component", "Cost", "Life", "Charge"], [15, 13, 6, 11],
               [[nm, c, f"{y}", c // y] for nm, c, y in _cp] + [None, ["Total", _cp_tot, "", sum(_cp_ch)]])

# Example 4: derogatory depreciation (accounts straight line, tax declining)
_dg_rows = []
_dg_net = 0
for _i, _fisc in enumerate(_db_charges):
    _diff = _fisc - 2400000
    _dg_net += _diff
    _dg_rows.append([f"N+{_i}" if _i else "N", 2400000, _fisc, _diff if _diff > 0 else "", -_diff if _diff < 0 else "", _dg_net])
assert _dg_net == 0
assert [r[3] for r in _dg_rows][:2] == [2400000, 480000] and [r[4] for r in _dg_rows][2:] == [672000, 1104000, 1104000]
_dg_tbl = grid(["Year", "Book SL", "Tax DB", "To 851", "To 861", "151 bal"], [6, 10, 10, 10, 10, 10], _dg_rows)
_dg_j = journal([
    ("31 Dec N    Depreciation for the accounts", [("681", "Depreciation charges", 2400000, 0), ("2845", "Depr. of transport eq.", 0, 2400000)]),
    ("31 Dec N    Excess tax depreciation", [("851", "HAO regulated prov. chg", 2400000, 0), ("151", "Derogatory depreciation", 0, 2400000)]),
    ("31 Dec N+2  Tax charge now lower: reversal", [("151", "Derogatory depreciation", 672000, 0), ("861", "HAO reversals", 0, 672000)]),
])
# quiz and practice figures
assert 9000000 // 4 * 9 // 12 == 1687500
assert 8000000 * 3 // 10 == 2400000 and 5600000 * 3 // 10 == 1680000
assert 6000000 * 25 // 100 == 1500000

LESSONS.append(lesson(
    module=M3,
    topic="Depreciation methods",
    title="Depreciation: straight line with prorata, declining balance, components and derogatory depreciation",
    slug="acl1-depreciation-methods",
    minutes=28,
    summary="Depreciation spreads cost less residual value over the useful life: straight line with a prorata from the date of use, declining balance with a switch to straight line, separate components, and derogatory depreciation (851/151) for extra tax depreciation.",
    objectives=[
        "Calculate straight-line depreciation with a prorata in the first and last years and build a schedule",
        "Calculate declining-balance depreciation with a coefficient and the switch to straight line",
        "Apply the component approach required by the revised SYSCOHADA",
        "Record depreciation and derogatory (excess tax) depreciation, and evaluate the choice of method",
    ],
    key_concepts=["Depreciation", "Depreciable amount", "Useful life", "Prorata temporis", "Straight-line method", "Declining-balance method", "Coefficient", "Component approach", "Derogatory depreciation", "Net book value"],
    blocks=[
        H("Introduction"),
        T("A delivery van loses value through use and age. Depreciation is how accounting spreads its cost over the years it serves, so that each year's profit bears its fair share. At A Level you must handle part years, the declining method used for tax, buildings split into components, and the difference between depreciation for the accounts and for tax."),
        D("**Depreciation** (amortissement) is the systematic allocation of the **depreciable amount** of an asset (cost less any residual value) over its **useful life**. It is recorded each year: Dr 681 Depreciation charges, Cr the 28 account of the asset. The asset's **net book value** (NBV) is cost less accumulated depreciation.",
          title="Definition: depreciation"),
        F(r"\text{Annual charge} = \frac{\text{cost} - \text{residual value}}{\text{useful life}}; \quad \text{first year} = \text{annual charge} \times \frac{\text{months (or days) of use}}{12}", title="Straight line"),
        EX("Worked example 1: the machine of the last lesson", intro="Straight line starts on the date the asset is put into service; textbooks count part years in months or in days (360-day year), so use the question's method. The machine costing FCFA 18 900 000 is put into service on 1 March N. Useful life 6 years, no residual value, year end 31 December.", steps=[
            S("Annual charge", math=r"18\,900\,000 \div 6 = 3\,150\,000"),
            S("Year N: 10 months", math=r"3\,150\,000 \times \tfrac{10}{12} = 2\,625\,000"),
            S("Last year N+6: the 2 months left", math=r"3\,150\,000 \times \tfrac{2}{12} = 525\,000"),
            S("Check", math=r"2\,625\,000 + 5 \times 3\,150\,000 + 525\,000 = 18\,900\,000"),
        ]),
        CODE(_dp_tbl, "text", title="Straight-line schedule (FCFA, invented for practice)"),
        H("2. Declining balance"),
        D("Under the **declining-balance** method (degressif) the rate is the straight-line rate multiplied by a **coefficient**, applied each year to the opening NBV. Teaching coefficients: 1.5 for a life of 3 or 4 years, 2 for 5 or 6 years, 2.5 above 6 years (check the current tax rules). When straight line on the remaining NBV over the remaining life gives a larger charge, the method **switches** to straight line, so the asset is fully depreciated at the end of its life. In the first year the prorata runs from the first day of the month of acquisition; textbooks differ on how the following years are counted, so follow yours.",
          title="Definition: declining balance", formula=r"\text{Rate} = \frac{1}{n} \times \text{coefficient}"),
        EX("Worked example 2: declining balance", intro="A vehicle bought on 2 January N for FCFA 12 000 000; life 5 years; coefficient 2. Prepare the schedule.", steps=[
            S("Rate", math=r"\tfrac{1}{5} \times 2 = 40\%"),
            S("Years N and N+1", math=r"12\,000\,000 \times 40\% = 4\,800\,000;\ 7\,200\,000 \times 40\% = 2\,880\,000"),
            S("Year N+2: compare", math=r"4\,320\,000 \times 40\% = 1\,728\,000 > 4\,320\,000 \div 3 = 1\,440\,000", text="Declining is still higher."),
            S("Year N+3: switch", math=r"2\,592\,000 \div 2 = 1\,296\,000 > 2\,592\,000 \times 40\% = 1\,036\,800", text="From now on, straight line: 1 296 000 in N+3 and N+4."),
            S("Check", math=r"4\,800\,000 + 2\,880\,000 + 1\,728\,000 + 1\,296\,000 + 1\,296\,000 = 12\,000\,000"),
        ]),
        CODE(_db_tbl, "text", title="Declining-balance schedule (SL rest = NBV divided by years left)"),
        IMG("alacl1-nbv-methods.svg", alt="Line graph of net book value from 12 million to zero over 5 years. The straight-line NBV falls evenly by 2.4 million a year; the declining-balance NBV falls fast at first (7.2 million after year 1, 4.32 after year 2) then slowly, reaching zero at year 5.",
            caption="Figure 1. Net book value under straight line and declining balance for the same vehicle."),
        H("3. The component approach"),
        T("The revised SYSCOHADA requires the **component approach**: when parts of an asset have significantly different useful lives, each part is recorded and depreciated separately. A building's structure may last 40 years, but its roof and lifts need replacing much sooner."),
        EX("Worked example 3: a building in components", intro="An office building costs FCFA 120 000 000: structure 90 000 000 (40 years), roof 18 000 000 (15 years), lifts and wiring 12 000 000 (10 years). Find the annual charge, and compare with one 40-year life.", steps=[
            S("Each component", math=r"\tfrac{90\,000\,000}{40} = 2\,250\,000;\ \tfrac{18\,000\,000}{15} = 1\,200\,000;\ \tfrac{12\,000\,000}{10} = 1\,200\,000"),
            S("Total", math=r"2\,250\,000 + 1\,200\,000 + 1\,200\,000 = 4\,650\,000"),
            S("Single life", math=r"120\,000\,000 \div 40 = 3\,000\,000", text="Ignoring components would understate the yearly cost by 1 650 000 and overstate profit."),
        ]),
        CODE(_cp_tbl, "text", title="Component depreciation"),
        H("4. Derogatory depreciation"),
        T("Tax rules may allow faster depreciation than the economic method used in the accounts. The extra tax depreciation is recorded as **derogatory depreciation** (amortissement derogatoire), a regulated provision: Dr 851 HAO regulated provision charges, Cr 151. When the tax charge later becomes smaller than the accounting charge, the provision is reversed: Dr 151, Cr 861."),
        EX("Worked example 4: accounts straight line, tax declining", intro="For the vehicle of example 2, the accounts use straight line (2 400 000 a year) and tax uses declining balance. Find the derogatory entries.", steps=[
            S("Year N", math=r"4\,800\,000 - 2\,400\,000 = 2\,400\,000", text="Excess: Dr 851, Cr 151."),
            S("Year N+1", math=r"2\,880\,000 - 2\,400\,000 = 480\,000", text="Excess again: 151 now 2 880 000."),
            S("Years N+2 to N+4", math=r"2\,400\,000 - 1\,728\,000 = 672\,000;\ 2\,400\,000 - 1\,296\,000 = 1\,104\,000", text="Tax charge lower: reverse 672 000, then 1 104 000 twice. 151 ends at zero."),
        ]),
        CODE(_dg_tbl + chr(10) * 2 + _dg_j,"text", title="Derogatory depreciation and entries in years N and N+2"),
        T("**Evaluation.** Straight line is simple and suits assets used evenly (buildings, furniture). Declining balance matches assets that lose value fast or give more service early (vehicles, computers) and lowers taxable profit early, helping cash flow. The component approach is more accurate but needs more records. Whatever the method, permanence of methods requires it to be kept from year to year."),
        MISTAKE("Starting straight-line depreciation on the invoice date", "Straight line starts when the asset is put into service. If an asset is bought in March but installed in May, count from May."),
        MISTAKE("Applying the declining rate to cost every year", "The declining rate applies to the opening NBV, not to the original cost."),
        MISTAKE("Forgetting to switch", "Compare each year with NBV divided by the years left. Without the switch, the asset is never fully depreciated."),
        QUIZ("A machine costing FCFA 9 000 000 with a 4-year life is put into service on 1 April. Straight-line depreciation for the first year ending 31 December is",
             ["FCFA 2 250 000", "FCFA 1 687 500", "FCFA 562 500", "FCFA 3 375 000"], 1,
             "9 000 000 / 4 = 2 250 000 a year; 9 months: 2 250 000 x 9/12 = 1 687 500.",
             hint="Count the months from 1 April to 31 December.",
             feedback=["That is a full year's charge.", "", "That is 3 months, from January to March.", "That uses a coefficient of 1.5 as if declining."]),
        QUIZ("Under declining balance with a 30% rate, an asset costs FCFA 8 000 000. The charge for year 2 is",
             ["FCFA 2 400 000", "FCFA 1 680 000", "FCFA 1 600 000", "FCFA 5 600 000"], 1,
             "Year 1: 2 400 000; NBV 5 600 000; year 2: 5 600 000 x 30% = 1 680 000.",
             hint="Apply the rate to the NBV at the start of year 2.",
             feedback=["That applies the rate to cost again.", "", "That is 20% of cost, the straight-line rate.", "That is the NBV, not the charge."]),
        PQ("A computer costing FCFA 6 000 000 (life 4 years, coefficient 1.5) is bought on 2 January. Prepare the declining-balance schedule with the switch to straight line.",
           "Rate = 1/4 x 1.5 = 37.5%. Year 1: 6 000 000 x 37.5% = 2 250 000; NBV 3 750 000. Year 2: compare 37.5% x 3 750 000 = 1 406 250 with 3 750 000 / 3 = 1 250 000; take **1 406 250**; NBV 2 343 750. Year 3: 37.5% x 2 343 750 = 878 906 (rounded) against 2 343 750 / 2 = 1 171 875; switch: **1 171 875** in years 3 and 4. Total: 2 250 000 + 1 406 250 + 1 171 875 x 2 = 6 000 000."),
        PQ("Explain the component approach and why it gives a truer view than depreciating a building as one asset.",
           "Parts of an asset with significantly different useful lives are recorded and depreciated separately (structure, roof, lifts). Each part's cost is spread over its own life, so the yearly charge reflects the real consumption of the asset. A single long life would understate depreciation in early years, overstate profit, and leave the cost of replaced parts (a new roof) to be treated wrongly."),
        PQ("Distinguish between depreciation and derogatory depreciation, giving the accounts used for each.",
           "**Depreciation** records the economic loss of value of the asset in the accounts: Dr 681, Cr 28. **Derogatory depreciation** is the extra depreciation allowed by tax rules over the accounting depreciation; it is a regulated provision for tax purposes, not a loss of value: Dr 851, Cr 151 when tax depreciation is higher, and Dr 151, Cr 861 when it later becomes lower."),
        TIP("Exam link: depreciation schedules and prorata calculations are core Paper 1 and Paper 3 skills; Paper 3 often continues into the disposal of the asset (next lesson). Present schedules in columns: year, opening NBV, charge, accumulated depreciation, closing NBV."),
        SUM("Depreciable amount = cost - residual value, spread over the useful life; Dr 681, Cr 28.",
            "Straight line starts when the asset is put into service, with a prorata in the first and last years.",
            "Declining balance: rate = (1/n) x coefficient on opening NBV; switch to straight line when that gives more.",
            "Components with different lives are depreciated separately (revised SYSCOHADA).",
            "Excess tax depreciation: derogatory depreciation, Dr 851 / Cr 151; reversal Dr 151 / Cr 861."),
    ],
))

# ------------------------------------------------------------------ 13. disposal and trade-in
_ds_cost, _ds_life = 15000000, 5
_ds_ann = _ds_cost // _ds_life
_ds_y = [_ds_ann * 6 // 12, _ds_ann, _ds_ann * 9 // 12]
_ds_acc = sum(_ds_y)
_ds_nbv = _ds_cost - _ds_acc
_ds_price = 7500000
_ds_res = _ds_price - _ds_nbv
assert (_ds_ann, _ds_y, _ds_acc, _ds_nbv, _ds_res) == (3000000, [1500000, 3000000, 2250000], 6750000, 8250000, -750000)
_ds_j = journal([
    ("30 Sep N  Depreciation to date of sale", [("681", "Depreciation charges", _ds_y[2], 0), ("2845", "Depr. of transport eq.", 0, _ds_y[2])]),
    ("30 Sep N  Van removed from the books", [("2845", "Depr. of transport eq.", _ds_acc, 0), ("812", "Book value of assets sold", _ds_nbv, 0), ("245", "Transport equipment", 0, _ds_cost)]),
    ("30 Sep N  Sale on credit", [("485", "Receivable on disposal", _ds_price, 0), ("822", "Proceeds of disposals", 0, _ds_price)]),
])
_ds_acct = "\n".join([
    "Disposal account (IAS-style presentation)",
    f"{'Dr':<34}| Cr",
    f"{'Van at cost':<22}{n(_ds_cost):>11} | {'Accumulated depr.':<20}{n(_ds_acc):>11}",
    f"{'':<34}| {'Proceeds of sale':<20}{n(_ds_price):>11}",
    f"{'':<34}| {'Loss on disposal':<20}{n(-_ds_res):>11}",
    f"{'Total':<22}{n(_ds_cost):>11} | {'Total':<20}{n(_ds_acc + _ds_price - _ds_res):>11}",
])
assert _ds_acc + _ds_price - _ds_res == _ds_cost

_ti_new, _ti_allow = 20000000, 8000000
_ti_vat = vat(_ti_new)
_ti_ttc = _ti_new + _ti_vat
_ti_cash = _ti_ttc - _ti_allow
_ti_res = _ti_allow - _ds_nbv
assert (_ti_vat, _ti_ttc, _ti_cash, _ti_res) == (3850000, 23850000, 15850000, -250000)
_ti_j = journal([
    ("30 Sep N  New van from the dealer", [("245", "Transport equipment", _ti_new, 0), ("4451", "VAT on fixed assets", _ti_vat, 0), ("481", "Fixed asset suppliers", 0, _ti_ttc)]),
    ("30 Sep N  Old van taken in part-payment", [("481", "Fixed asset suppliers", _ti_allow, 0), ("822", "Proceeds of disposals", 0, _ti_allow)]),
    ("30 Sep N  Old van removed from the books", [("2845", "Depr. of transport eq.", _ds_acc, 0), ("812", "Book value of assets sold", _ds_nbv, 0), ("245", "Transport equipment", 0, _ds_cost)]),
    ("30 Sep N  Balance paid by bank", [("481", "Fixed asset suppliers", _ti_cash, 0), ("521", "Bank", 0, _ti_cash)]),
])
# quiz and practice figures
assert 4000000 - 2500000 == 1500000 and 1800000 - 1500000 == 300000
assert 10000000 // 4 * 3 + 10000000 // 4 * 6 // 12 == 8750000 and 10000000 - 8750000 == 1250000 and 1000000 - 1250000 == -250000
assert 6000000 - 3600000 == 2400000 and 2000000 - 2400000 == -400000

LESSONS.append(lesson(
    module=M3,
    topic="Disposal and trade-in of fixed assets",
    title="Disposal and trade-in of fixed assets: 812, 822 and the HAO result",
    slug="acl1-disposal-and-trade-in",
    minutes=25,
    summary="When a fixed asset is sold, depreciation is first brought up to the date of sale; the asset leaves the books with its accumulated depreciation and its net book value goes to 812; the price goes to 822. In a trade-in the dealer's allowance is the sale price of the old asset.",
    objectives=[
        "Bring depreciation up to the date of disposal",
        "Journalise the removal of the asset, the sale price and the receipt using 812, 822 and 485",
        "Calculate the gain or loss on disposal and relate it to the HAO result",
        "Record a trade-in (part-exchange) of an old asset against a new one",
    ],
    key_concepts=["Disposal", "Complementary depreciation", "Net book value", "812 Book value of fixed assets sold", "822 Proceeds of disposals", "485 Receivable on disposal", "Gain or loss on disposal", "Trade-in allowance"],
    blocks=[
        H("Introduction"),
        T("After two and a half years a transport company in Ngaoundere sells a delivery van to buy a bigger one. The sale is not part of its ordinary activity of carrying goods, so the revised SYSCOHADA keeps it out of the ordinary result: the gain or loss appears among the non-ordinary (HAO) items. At O Level you used a disposal account; here you use the SYSCOHADA accounts and compare the two."),
        D("A **disposal** removes a fixed asset from the books because it is sold, exchanged, scrapped or destroyed. The **gain or loss on disposal** is the price obtained less the **net book value** (cost less accumulated depreciation) on the date of disposal.",
          title="Definition: disposal and gain or loss",
          formula=r"\text{Gain (loss)} = \text{proceeds (822)} - \text{net book value (812)}"),
        KEY("The four steps", "Always in this order.", cards=[
            ["1. Depreciation to date", "Charge depreciation from the start of the year to the date of disposal: Dr 681, Cr 28."],
            ["2. Remove the asset", "Dr 28 with all accumulated depreciation; Dr 812 with the net book value; Cr the asset account (2x) with its cost."],
            ["3. Record the price", "Dr 485 Receivable on disposal (or the bank); Cr 822 Proceeds of disposals."],
            ["4. Collect", "Dr bank, Cr 485 when paid."],
        ]),
        T("The result of the disposal is not booked in a separate entry: 822 minus 812 shows it in the HAO part of the income statement. VAT on sales of used assets depends on the tax rules (and on whether VAT was deducted when the asset was bought); our examples ignore it, so check your textbook."),
        H("Worked examples"),
        EX("Worked example 1: sale of a van", intro="A van costing FCFA 15 000 000 was put into service on 1 July N-2; straight line over 5 years; year end 31 December. It is sold on credit on 30 September N for 7 500 000.", steps=[
            S("Annual depreciation", math=r"15\,000\,000 \div 5 = 3\,000\,000"),
            S("Depreciation already charged", math=r"\text{N-2: } 6 \text{ months} = 1\,500\,000;\ \text{N-1: } 3\,000\,000"),
            S("Step 1: to the date of sale", math=r"3\,000\,000 \times \tfrac{9}{12} = 2\,250\,000"),
            S("Accumulated depreciation and NBV", math=r"1\,500\,000 + 3\,000\,000 + 2\,250\,000 = 6\,750\,000;\ \text{NBV} = 15\,000\,000 - 6\,750\,000 = 8\,250\,000"),
            S("Result", math=r"7\,500\,000 - 8\,250\,000 = -750\,000", text="A loss of FCFA 750 000 in the HAO result."),
        ]),
        CODE(_ds_j, "text", title="Sale of the van (FCFA, invented for practice)"),
        CODE(_ds_acct, "text", title="The same result with a disposal account"),
        T("Both methods give the same loss of 750 000. The SYSCOHADA method shows the proceeds and the book value separately in the income statement (822 and 812) instead of only the net figure."),
        H("Trade-in (part-exchange)"),
        D("In a **trade-in** the supplier of a new asset takes the old asset as part-payment. The **trade-in allowance** is the price received for the old asset: it is credited to 822, and the new asset is recorded at its full price, not the price less the allowance.",
          title="Definition: trade-in"),
        EX("Worked example 2: trade-in of the same van", intro="Instead of selling the van for cash, the company buys a new van on 30 September N for FCFA 20 000 000 plus VAT 19.25% (recoverable). The dealer takes the old van at 8 000 000 and the rest is paid by bank.", steps=[
            S("New van", math=r"20\,000\,000 + 3\,850\,000 = 23\,850\,000", text="Dr 245 20 000 000 and 4451 3 850 000; Cr 481 23 850 000."),
            S("Old van as part-payment", text="Dr 481, Cr 822 with the allowance of 8 000 000."),
            S("Remove the old van", text="As in example 1 (after depreciation to 30 September): Dr 2845 6 750 000, Dr 812 8 250 000, Cr 245 15 000 000."),
            S("Pay the balance", math=r"23\,850\,000 - 8\,000\,000 = 15\,850\,000"),
            S("Result", math=r"8\,000\,000 - 8\,250\,000 = -250\,000", text="A loss of 250 000."),
        ]),
        CODE(_ti_j, "text", title="Trade-in entries"),
        KEY("Other ways an asset leaves", "Same logic, different proceeds.", cards=[
            ["Scrapped, fully depreciated", "Dr 28, Cr 2x with the cost; nothing goes to 812 or 822 because the NBV is nil."],
            ["Destroyed and insured", "Remove the asset through 812 as usual; the insurance compensation is a non-ordinary income (class 8; check the account in your textbook)."],
            ["Given away or stolen", "NBV to 812 with no proceeds: the whole NBV is a loss."],
        ]),
        MISTAKE("Forgetting depreciation for the part year", "Before removing the asset, charge depreciation from the start of the year to the date of disposal. Without it, the NBV and the loss are wrong."),
        MISTAKE("Recording the new asset at the cash paid", "In a trade-in the new asset is recorded at its full price (20 000 000), not at the cash paid after the allowance."),
        MISTAKE("Putting the price in 701 or the gain in 7", "Disposals are HAO: proceeds in 822, book value in 812."),
        QUIZ("An asset cost FCFA 4 000 000; accumulated depreciation at the date of sale is 2 500 000; it is sold for 1 800 000. The result is",
             ["a gain of 300 000", "a loss of 700 000", "a gain of 1 800 000", "a loss of 2 200 000"], 0,
             "NBV = 4 000 000 - 2 500 000 = 1 500 000; 1 800 000 - 1 500 000 = 300 000 gain.",
             hint="Find the NBV first.",
             feedback=["", "You compared the price with the accumulated depreciation.", "That is the proceeds, not the result.", "You compared the price with the cost."]),
        QUIZ("In SYSCOHADA, the net book value of an asset sold is debited to",
             ["681", "812", "822", "485"], 1,
             "812 Book value of fixed assets sold.",
             hint="Which class 8 account mirrors 822?",
             feedback=["681 is the depreciation charge.", "", "822 receives the proceeds (credit).", "485 is the receivable for the price."]),
        PQ("Equipment cost FCFA 10 000 000 on 1 January N-3 (straight line, 4 years). It is sold for cash 1 000 000 on 30 June N. Calculate the result and journalise.",
           "Annual charge 2 500 000. Depreciation N-3 to N-1: 7 500 000; N to 30 June: 1 250 000; total **8 750 000**. NBV = 10 000 000 - 8 750 000 = **1 250 000**. Loss = 1 000 000 - 1 250 000 = **250 000**. Entries: Dr 681 / Cr 284 1 250 000; Dr 284 8 750 000, Dr 812 1 250 000, Cr 24 10 000 000; Dr 521 / Cr 822 1 000 000."),
        PQ("A dealer sells a new machine for FCFA 9 000 000 (VAT ignored) and takes an old machine as part-payment at 2 000 000. The old machine cost 6 000 000 and has accumulated depreciation of 3 600 000 at that date. Give the entries and the result.",
           "New machine: Dr 24 9 000 000, Cr 481 9 000 000. Allowance: Dr 481 2 000 000, Cr 822 2 000 000. Old machine: Dr 284 3 600 000, Dr 812 2 400 000, Cr 24 6 000 000. Balance paid: Dr 481 7 000 000, Cr bank. Result = 2 000 000 - 2 400 000 = **loss of 400 000**."),
        PQ("Why does the revised SYSCOHADA show proceeds and book value of disposals separately in class 8 rather than as part of ordinary income?",
           "Selling fixed assets is not the entity's ordinary activity and does not repeat each year. Showing 822 and 812 in the HAO section keeps the ordinary result comparable from year to year and lets users see the size of the disposals, not just the net gain or loss."),
        TIP("Exam link: disposals usually follow a depreciation schedule in Paper 3 Section A and appear in Paper 1 as 'find the gain or loss'. Show the NBV working before the entries, and label every account with its number."),
        SUM("First charge depreciation up to the date of disposal.",
            "Remove the asset: Dr 28 (accumulated), Dr 812 (NBV), Cr 2x (cost).",
            "Price: Dr 485 or bank, Cr 822; result = 822 - 812 in the HAO section.",
            "Trade-in: new asset at full price; allowance credited to 822 as the price of the old asset.",
            "A disposal account gives the same result; SYSCOHADA shows the two sides separately."),
    ],
))

# ------------------------------------------------------------------ 14. inventory valuation
# Movements of one product (units, unit price): opening, buy, sell, buy, sell
_iv_open = (100, 1000)
_iv_mv = [("3 Mar", "in", 100, 1200), ("8 Mar", "out", 120, None), ("15 Mar", "in", 120, 1300), ("22 Mar", "out", 150, None)]


def _fifo():
    layers = [list(_iv_open)]
    out, cogs = [], []
    for d, k, q, p in _iv_mv:
        if k == "in":
            layers.append([q, p])
            out.append((d, "in", q, p, q * p, sum(l[0] for l in layers), sum(l[0] * l[1] for l in layers)))
        else:
            need, cost = q, 0
            while need:
                take = min(need, layers[0][0])
                cost += take * layers[0][1]
                layers[0][0] -= take
                need -= take
                if layers[0][0] == 0:
                    layers.pop(0)
            cogs.append(cost)
            out.append((d, "out", q, cost // q if cost % q == 0 else None, cost, sum(l[0] for l in layers), sum(l[0] * l[1] for l in layers)))
    return out, cogs, layers


def _cump_perp():
    qty, val = _iv_open[0], _iv_open[0] * _iv_open[1]
    out, cogs = [], []
    for d, k, q, p in _iv_mv:
        if k == "in":
            qty += q
            val += q * p
            out.append((d, "in", q, p, q * p, qty, val))
        else:
            avg = _Fr(val, qty)
            cost = avg * q
            assert cost.denominator == 1
            cost = int(cost)
            qty -= q
            val -= cost
            cogs.append(cost)
            out.append((d, "out", q, int(avg), cost, qty, val))
    return out, cogs, (qty, val)


_f_rows, _f_cogs, _f_left = _fifo()
_c_rows, _c_cogs, _c_left = _cump_perp()
_avail_q = 100 + 100 + 120
_avail_v = 100 * 1000 + 100 * 1200 + 120 * 1300
assert (_avail_q, _avail_v) == (320, 376000) and _avail_v - 100000 == 276000
_sold_q = 120 + 150
_close_q = _avail_q - _sold_q
_f_cogs_t, _c_cogs_t = sum(_f_cogs), sum(_c_cogs)
_f_close = sum(l[0] * l[1] for l in _f_left)
_c_close = _c_left[1]
assert _f_cogs == [124000, 187000] and _f_cogs_t == 311000 and _f_close == 65000 == 50 * 1300
assert _c_cogs == [132000, 183000] and _c_cogs_t == 315000 and _c_close == 61000
assert _f_cogs_t + _f_close == _avail_v == _c_cogs_t + _c_close
_cump_per = _Fr(_avail_v, _avail_q)
assert _cump_per == 1175
_p_close = int(_cump_per * _close_q)
_p_cogs = _avail_v - _p_close
assert (_p_close, _p_cogs, _close_q) == (58750, 317250, 50)
_p_sales = 120 * 1500 + 150 * 1500
assert _p_sales == 405000
_gp = {"FIFO": _p_sales - _f_cogs_t, "CUMP perpetual": _p_sales - _c_cogs_t, "CUMP periodic": _p_sales - _p_cogs}
assert _gp == {"FIFO": 94000, "CUMP perpetual": 90000, "CUMP periodic": 87750}


def _card(rows, title):
    head = f"{'Date':<8}{'Move':<5}{'Qty':>5}{'Unit':>7}{'Amount':>10} |{'Stock qty':>10}{'Stock value':>13}"
    lines = [title, head, "-" * len(head)]
    lines.append(f"{'1 Mar':<8}{'open':<5}{100:>5}{1000:>7}{n(100000):>10} |{100:>10}{n(100000):>13}")
    for d, k, q, p, amt, sq, sv in rows:
        lines.append(f"{d:<8}{k:<5}{q:>5}{(n(p) if p else 'mixed'):>7}{n(amt):>10} |{sq:>10}{n(sv):>13}")
    return "\n".join(lines)


_f_card = _card(_f_rows, "FIFO stock card (perpetual) - 'mixed' = more than one layer")
_c_card = _card(_c_rows, "CUMP stock card (perpetual) - unit cost recalculated after each receipt")
_cmp_tbl = grid(["Method", "Cost of sales", "Closing stock", "Gross margin"], [18, 15, 15, 14],
                [["FIFO", _f_cogs_t, _f_close, _gp["FIFO"]], ["CUMP perpetual", _c_cogs_t, _c_close, _gp["CUMP perpetual"]],
                 ["CUMP periodic", _p_cogs, _p_close, _gp["CUMP periodic"]]])
_pur = 276000
_inv_j = journal([
    ("Perpetual (FIFO): purchases in the month", [("601", "Purchases of goods", _pur, 0), ("401", "Suppliers (VAT ignored)", 0, _pur)]),
    ("Perpetual (FIFO): goods received into stock", [("31", "Goods for resale", _pur, 0), ("6031", "Change in stock of goods", 0, _pur)]),
    ("Perpetual (FIFO): cost of the two sales", [("6031", "Change in stock of goods", _f_cogs_t, 0), ("31", "Goods for resale", 0, _f_cogs_t)]),
])
assert 100000 + _pur - _f_cogs_t == _f_close
_inv_p = journal([
    ("Periodic (CUMP) at the year end: cancel opening stock", [("6031", "Change in stock of goods", 100000, 0), ("31", "Goods for resale", 0, 100000)]),
    ("Periodic (CUMP) at the year end: record closing stock", [("31", "Goods for resale", _p_close, 0), ("6031", "Change in stock of goods", 0, _p_close)]),
])
_nrv_unit = 1250
_nrv_imp = (1300 - _nrv_unit) * 50
assert _nrv_imp == 2500 and 50 * _nrv_unit == 62500
_nrv_j = journal([("31 Dec  Impairment of stock to net realisable value", [("659", "Impairment charges", _nrv_imp, 0), ("391", "Impairment of stocks", 0, _nrv_imp)])])
# practice figures
assert 200 * 500 + 300 * 600 == 280000 and (280000) / 500 == 560 and 200 * 500 + 100 * 600 == 160000

LESSONS.append(lesson(
    module=M3,
    topic="Inventory valuation",
    title="Inventory valuation: FIFO and weighted average cost (CUMP), perpetual and periodic",
    slug="acl1-inventory-valuation",
    minutes=28,
    summary="Stock is valued at the lower of cost and net realisable value. Cost is found by FIFO or by weighted average (CUMP). The perpetual system updates stock after every movement; the periodic system counts at the end. The method changes cost of sales, closing stock and profit.",
    objectives=[
        "Prepare FIFO and CUMP stock cards under the perpetual (permanent) inventory system",
        "Calculate the end-of-period CUMP and closing stock under the periodic system",
        "Compare the effect of each method on cost of sales, closing stock and gross margin",
        "Journalise stock movements with accounts 31, 601 and 6031 and apply the lower of cost and net realisable value",
    ],
    key_concepts=["Inventory (stock)", "FIFO", "Weighted average cost (CUMP)", "Perpetual (permanent) inventory", "Periodic inventory", "Stock card", "Net realisable value", "Impairment of stock", "Change in stock (6031)"],
    blocks=[
        H("Introduction"),
        T("A wholesaler in Douala buys the same sack of flour at different prices during the month. When she sells 120 sacks, which purchase price is the cost of those sacks? The answer is a matter of method, and the method changes both the profit and the value of stock in the balance sheet."),
        D("**Inventory** (stock) is made up of goods held for sale, materials and supplies, and products in progress or finished. It is valued at the **lower of cost and net realisable value** (the expected selling price less the costs to sell). **Cost** is found by an allowed method: **FIFO** (first in, first out: the oldest units are sold first, so closing stock carries the newest prices) or **CUMP** (cout unitaire moyen pondere, the weighted average cost).",
          title="Definition: inventory, FIFO and CUMP"),
        F(r"\text{CUMP} = \frac{\text{value of opening stock} + \text{value of purchases}}{\text{units in opening stock} + \text{units purchased}}", title="Weighted average cost (periodic: once for the whole period)"),
        KEY("Two inventory systems", "They differ in when stock is updated.", cards=[
            ["Perpetual (permanent) inventory", "A stock card is kept for each item; every receipt and issue is recorded, so stock and cost of sales are always known. With CUMP the average is recalculated after every receipt."],
            ["Periodic (intermittent) inventory", "Stock is counted only at the end of the period. Cost of sales is found by: opening stock + purchases - closing stock. With CUMP one average is used for the whole period."],
        ]),
        H("Worked examples"),
        T("One product. Opening stock: 100 units at FCFA 1 000. Movements: 3 March buy 100 at 1 200; 8 March sell 120; 15 March buy 120 at 1 300; 22 March sell 150. Selling price FCFA 1 500 a unit. Prices exclude VAT. All figures are invented for practice."),
        EX("Worked example 1: FIFO stock card", intro="Prepare the FIFO stock card and find the cost of sales and closing stock.", steps=[
            S("Sale on 8 March: 120 units", math=r"100 \times 1\,000 + 20 \times 1\,200 = 124\,000", text="The oldest 100 units first, then 20 of the 3 March units. 80 units at 1 200 remain."),
            S("Sale on 22 March: 150 units", math=r"80 \times 1\,200 + 70 \times 1\,300 = 96\,000 + 91\,000 = 187\,000", text="50 units at 1 300 remain."),
            S("Closing stock and cost of sales", math=r"50 \times 1\,300 = 65\,000;\ 124\,000 + 187\,000 = 311\,000"),
            S("Check", math=r"100\,000 + 276\,000 - 65\,000 = 311\,000", text="Opening stock plus purchases less closing stock gives the same cost of sales."),
        ]),
        CODE(_f_card, "text", title="FIFO (FCFA)"),
        EX("Worked example 2: perpetual CUMP", intro="Prepare the CUMP stock card, recalculating the average after each receipt.", steps=[
            S("After 3 March", math=r"\tfrac{100\,000 + 120\,000}{200} = 1\,100", text="Sale on 8 March: 120 x 1 100 = 132 000; 80 units left, value 88 000."),
            S("After 15 March", math=r"\tfrac{88\,000 + 156\,000}{200} = 1\,220", text="Sale on 22 March: 150 x 1 220 = 183 000; 50 units left, value 61 000."),
            S("Cost of sales", math=r"132\,000 + 183\,000 = 315\,000", text="Check: 376 000 - 61 000 = 315 000."),
        ]),
        CODE(_c_card, "text", title="CUMP perpetual (FCFA)"),
        EX("Worked example 3: periodic CUMP and comparison", intro="Under the periodic system, find the single CUMP for March, the closing stock and the cost of sales. Then compare the three results.", steps=[
            S("Units and value available", math=r"100 + 100 + 120 = 320 \text{ units};\ 100\,000 + 120\,000 + 156\,000 = 376\,000"),
            S("CUMP", math=r"376\,000 \div 320 = 1\,175"),
            S("Closing stock (50 units counted)", math=r"50 \times 1\,175 = 58\,750"),
            S("Cost of sales", math=r"376\,000 - 58\,750 = 317\,250"),
            S("Gross margin", math=r"\text{Sales } 270 \times 1\,500 = 405\,000", text="FIFO 94 000; perpetual CUMP 90 000; periodic CUMP 87 750."),
        ]),
        CODE(_cmp_tbl, "text", title="Comparison of the three results (FCFA)"),
        T("When purchase prices **rise**, as here, FIFO gives the **lowest cost of sales, the highest closing stock and the highest profit**; averages lie between. When prices fall the order reverses. The total cost of sales plus closing stock is always the same (376 000), so over the life of the business the methods give the same total profit: they differ only in timing."),
        H("Journal entries and net realisable value"),
        T("Under the revised SYSCOHADA the stock of goods is in account 31, the purchases in 601, and the change in stock in 6031. In the perpetual system the goods received and the cost of goods sold are recorded as they happen; the net effect on 6031 is the change in stock (100 000 down to 65 000, a decrease of 35 000 charged to the result). Under the periodic system 6031 is used only at the year end."),
        CODE(_inv_j, "text", title="Perpetual system, FIFO (FCFA)"),
        CODE(_inv_p, "text", title="Periodic system, CUMP, at the year end"),
        EX("Worked example 4: lower of cost and net realisable value", intro="At the year end the 50 units (FIFO cost 1 300 each) could be sold for only 1 250 each, net of selling costs. Should stock be written down?", steps=[
            S("Compare per unit", text="Cost 1 300 is above net realisable value 1 250, so stock is valued at 1 250 (prudence)."),
            S("Impairment", math=r"50 \times (1\,300 - 1\,250) = 2\,500", text="Dr 659 impairment charges (current assets), Cr 391 Impairment of stocks. Stock appears at 65 000 less 2 500 = 62 500."),
        ]),
        CODE(_nrv_j, "text", title="Impairment entry (account sub-numbers to check in your textbook)"),
        T("**Evaluation.** FIFO matches the usual physical flow of perishable goods and gives a balance sheet close to current prices, but in inflation it makes profit look higher and so raises tax. CUMP smooths price changes and is easy to apply, but the average may not match any real purchase. Permanence of methods requires the same method every year. In Cameroon textbooks follow the choice of methods allowed by the Uniform Act: FIFO and CUMP are accepted, and LIFO is not; check your textbook."),
        MISTAKE("Averaging the unit prices", "The CUMP is total value divided by total units, not the simple average of 1 000, 1 200 and 1 300 (which is 1 166.67)."),
        MISTAKE("Using one CUMP for the whole period in a perpetual system", "In the perpetual system the average is recalculated after every receipt and applied to the following issues."),
        MISTAKE("Valuing closing stock at selling price", "Stock is valued at cost (or net realisable value if lower), never at the selling price: profit is recognised only when goods are sold."),
        QUIZ("Opening stock 200 units at FCFA 500; purchases 300 units at FCFA 600. The periodic CUMP is",
             ["FCFA 550", "FCFA 560", "FCFA 600", "FCFA 500"], 1,
             "(200 x 500 + 300 x 600) / 500 = 280 000 / 500 = 560.",
             hint="Total value divided by total units.",
             feedback=["That is the simple average of the two prices.", "", "That is the latest price.", "That is the opening price."]),
        QUIZ("When purchase prices are rising, which method gives the highest profit?",
             ["FIFO", "CUMP", "They give the same profit", "It depends on the sales price only"], 0,
             "FIFO charges the oldest, cheapest cost to sales, so cost of sales is lowest and profit highest.",
             hint="Which method sells the oldest, lowest-cost units first?",
             feedback=["", "CUMP is between the two extremes.", "They give the same total over the life of the business but not in a given period.", "Sales price is the same for all methods."]),
        PQ("Stock of an item: opening 200 units at FCFA 500; 5 June buy 300 at 600; 20 June sell 400. Using FIFO and perpetual inventory, find the cost of the sale and the closing stock.",
           "Sale of 400: 200 x 500 + 200 x 600 = 100 000 + 120 000 = **220 000**. Closing stock: 100 units at 600 = **60 000**. Check: 100 000 + 180 000 - 60 000 = 220 000."),
        PQ("For the same data, find the cost of the sale under perpetual CUMP and compare it with FIFO.",
           "After the purchase: 500 units, value 280 000; CUMP 560. Cost of the sale = 400 x 560 = **224 000**; closing stock 100 x 560 = **56 000**. CUMP gives a higher cost of sales than FIFO (224 000 against 220 000) and a lower closing stock because prices rose."),
        PQ("Discuss the effect of the choice of FIFO or CUMP on a firm's profit and tax in a period of rising prices.",
           "Plan. FIFO: lowest cost of sales, highest closing stock and profit, so more tax now, but the balance sheet shows stock close to current cost. CUMP: smooths the change, a middle profit and tax. Total profit over the life of the business is the same; only timing differs. Evaluation: the choice should reflect the real flow of goods and be applied consistently; changing methods to manage profit breaks permanence of methods and must be disclosed."),
        TIP("Exam link: the Board's 2023 report describes a Paper 2 (Cost and Management Accounting) question on stock valuation in which candidates prepared stock cards using FIFO and weighted average cost and then a trading account; it was answered by all candidates, with scores from 8 to 20 out of 20. The same skills appear in Paper 1. Always lay out a stock card with quantity, unit cost and value columns, and prove your cost of sales by opening stock + purchases - closing stock."),
        SUM("Stock is valued at the lower of cost and net realisable value; impairment goes to 659/391.",
            "FIFO: oldest costs go to sales; closing stock carries the latest prices.",
            "CUMP: perpetual recalculates after each receipt; periodic uses one average for the period.",
            "In rising prices FIFO gives the highest profit; totals are the same over time.",
            "Cost of sales = opening stock + purchases - closing stock; accounts 31, 601 and 6031."),
    ],
))
